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
<img src="https://cdn5.telesco.pe/file/PR7HEnNfexSLnQAMZvN-2xy4IoABrpSMe3yAJY7tPm6wdlkTDWODgbJBa4-SYabZKT-vqnG1VXcTsYht7YCunyJ5ZOPq-BKGBKqflXqH8LqgbxoXayHnio_JTKaVV_08xBUvl8lyKmNI_5zt8qB510MdyIC2rWIhEwK8D_ftUFBhpUnB7l1-VeGDN369_TnfX4zZRHmbT4ve5gv3fOtLfnBmc4Cpr6OL5_0Dsqb6iuzGychrdCrMibk2Om6E8eE4UTR32BFDqmQ1PMLMA705dluSU37PYNmK8VxNOoO8Waf_WTOir4-82tmoMAGGQ9io_B30UBmqz_zpCa69chAZFQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 495K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 05:21:00</div>
<hr>

<div class="tg-post" id="msg-102731">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZBQ0UvPjeSkAIM5XXQ05YZY0GM-uJoIobbeZkM-j09BjKf1kzh2FzAP0IsTzNEFBWHEbg0P6JPhcpEtjNvnA_TguQjRZs6_33zay_bPCly3f5oR9y7dKKNApxvQ5C8fkhCv_EJbrxZFdlgOExRZO3NDuugY0UyTn9HNxT4qZFW-O-I1OW3RYfWJG9foN44wJS3xHy8LaYoY5oLQav3f4CqCukR_JL7vZ7drWwF1XJJ2L-OZFPQUyrQM-iutuIdzRHfNr6uEXRFJFn9EvLfk2RPYtqf1CFDNpovvBvZOL7tPiBGupvuuAzX9w88PiCiORVvXkq43GaFAgle3v58npA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
✅
💔
#رسمیییییی
؛ اتحادیه فوتبال اروپا، تعداد کارت‌های زردی که منجر به محرومیت می‌شود را در لیگ قهرمانان اروپا از 3 به 4 افزایش داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/Futball180TV/102731" target="_blank">📅 01:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102730">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYxRQ_qsTry8zeXsnrjWUic4g9S7IonhTZ9SMBdFeZyyGWbcnovX6wqVQScVOXcWeSEiSecOmYThrKlexzKQT1PXSeamZZ23Ih0C0Af70cWodBLSj6A051F7rWmi8MZ3od8_ALuZ3zLajpGS49qiXo5ZCjZthYhbQQ7UUqfC4E3ISzX9kWxfbfyBaLF0QrYxLm90KUMCXGAarunLPliYMVfRmzoctfvejiTPNNDKQC6pK_zBohjCbRSUq623Fl9GqfURtn4ZfJa4xNHs6UGDlxX9oGLmChIfvKB2znJyiUuxTizIeeM3VaLHOXCwbAeDQz4QbmeMFrOcfYGIN9fs9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
؛ به نقل از روزنامه SER، جلسه سرنوشت‌ساز رئال‌مادرید با نمایندگان وینیسیوس جونیور فردا چهارشنبه برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/102730" target="_blank">📅 01:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102729">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ffk7-L3npFGMy0Flq_mWoy05F2RMmpl-LHSR0RJWoflP20YmUAPYzQRKUNCSuWJ_JeHhaSFDiF49inpzxv3sLlMrXQBVfz-7TScOYriOZm7Md33feTKsgJwIlkJcL_EmoSpCkfqp-ioBHl-Ux_NaQIiIj2QeFA7QBBTfl5s1OvEFGw9-1gZyDJ44-1-ReUZhc7T7pPqhBi4Lp8eakJPWw1__O7OWY24Ssq4cryHwGTFwED0w3-CksCDpRdkP_1tTib-HN3zBIhwI7QfmyDaMV8GwrZHn4SDXLbpEXLxCjAINbtWgORa9VqXSkyTswJvcDi2RsOwGGFJI5yEhhSsmVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
👤
جوادحسین‌نژاد در مراسم رونمایی از کیت‌جدید تیم ماخاچ‌قلعه روسیه حضور یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/102729" target="_blank">📅 01:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102728">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0hnk9ShkY1fzA7xMKcKzetk9dIdI2Vcd6ByScyE9BlBNfVR92_MAz9qmljanHcauAm3DurxUFxuPAzYG5m4tFfeCONJhlK6WLIE865hd0ORP5NoD0pumO66Wn1rDKirnYqJ9UzmYbM_-Fm7Yw5AqCQRlp2R9vetq1m-jyvhPlDcm8X8UNK66Wa40_x-29q3dTQ5IpgJU61HU2Q01JZZpym3WjbYkWgN-CHx6uAhNqZCl4kKgUOPHwCfZUA4CEJOYu6dilPqbRevUxr3PxmiAaVE6aGY8LyfyG8-ovX6iwdjgUg76kurVtjqynS_XoaGgF6WVtGs8zo5RP4OpteEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت انگشتهای دیدا در مراسم تشییع بارزی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/102728" target="_blank">📅 01:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102726">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c707c5bf8.mp4?token=E14PUGz4yIVFO2LAAoORoo8injMsEWdIfNQ8NBbuOaTV_QUXKSdaH5C-GxEpImIHH9JLDec0Ur5aeHpDoQ2IXgQg85q4dEHcxxJ71XLgv0t83-_uRfILyaurE0xYUrtkaB5v7CC9c5HA3HEWg-IkJt-PV39Ffqg-6dSrzhfyL9Lh_EFrz4jUuECTD2XUur1X9SuQGwlfnwiAQJKNrmFOBpqVoPpdAJZXdrm8wTONeGaI8sWTuQCmQMYlk0F6eCeIVcRm91Z2dh7HNd-R1jyTIfaYPsRaDReRJ9vR0TmqKbduyEq2utY9BN5jUao6qAeoBYgptXbYBoyg_2oYIrzDkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c707c5bf8.mp4?token=E14PUGz4yIVFO2LAAoORoo8injMsEWdIfNQ8NBbuOaTV_QUXKSdaH5C-GxEpImIHH9JLDec0Ur5aeHpDoQ2IXgQg85q4dEHcxxJ71XLgv0t83-_uRfILyaurE0xYUrtkaB5v7CC9c5HA3HEWg-IkJt-PV39Ffqg-6dSrzhfyL9Lh_EFrz4jUuECTD2XUur1X9SuQGwlfnwiAQJKNrmFOBpqVoPpdAJZXdrm8wTONeGaI8sWTuQCmQMYlk0F6eCeIVcRm91Z2dh7HNd-R1jyTIfaYPsRaDReRJ9vR0TmqKbduyEq2utY9BN5jUao6qAeoBYgptXbYBoyg_2oYIrzDkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
فریادهای مجری کشمیری تلویزیون جمهوری اسلامی درباره تنگه هرمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102726" target="_blank">📅 01:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102725">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5XIXA2DSq7M6FhIrJJSlyrKhvzzQqP4W58NrGobspwdImmBDpanBv25uZk0CsDeUbxI1BIL89QLqUDt_i5aHhawsQg5OunaSHI1N-3FsnXCNEUZljlThfCrDCoAMBXGwfCW-jzBIGwFEEjdTQCLAkis3o0kKwtJ_Dd-b3rsqwrVNFx5WcDnYTT6P0UByaQS3K1IRtxxwF9h4eKPCGwuVw5HzWAAkrJimY9iywgj0UlXcbVRLxWpa2l8cmVtHTycdjei2y0Ejz3Ta_GkwcFpwUFOG-apN8RCUS2Ec42ZG3kOq5ANl_C7ZnvY8NyTzTei6mgL3iQONrRCx3lOfKA6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
باشگاه لیورپول درحال تلاش برای جذب ابراهیم امبایه‌ بازیکن PSG است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/102725" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102724">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
بازگشت ستاره سابق استقلال در آستانه بازگشت دوباره قرار گرررررررفت
💣
💣
💣
💣
https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/102724" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102723">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qWfzYlPl0Kvu7gJ6oRJFPqJngKzIQtRGeCqvUTCZEYAz1VgDuwLKH9XPZ5_dGkE3VG05ffE5VblPQ0thJbngueXg-Gtxqt457Yn_qyWTdZONkhe8Z0KHf6Rie6UYC1JKsuiflQ9-ZWqY7n4TN5Oqs1zWNnW50kvn7tkBSo4sUBkJDvEtIO506n2aONexXw0ty1121U6fpVGpaO-OJMVVMsdMtmJ0Moz6jWPEcKXMba7lT-hVOt5rA9okUuBPyDr9sg2MEDGN7DDiYdsCSKj5m1QPqIno9Z-WkSR6MspGukXbbokC2K3BB_K-RRxWdM5ztk5NeGEEqL2jbCzmzhHcRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازیکن را به استقلال پیشنهاد داده است</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/102723" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102720">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUrPfvyjyjHWhr-To9k7TIIhq-6BkJFvqVduwjqd3YBG92LZYA7ggcAJob7y5zCEUB-AVAwioIK5a4PXRgjRaCKE8ffI63zTj-SxMirL6VT-d1OFHzQW6kDbO1UgDbW8ZcOMr0p4CWZKlxfdRjLDGXcj4dygW3sOMnFq02YC_LLiwpD1xyJqBCwOqozDHbiOs5bVTNk_I5CRf9UNhTCdYL6uWss4D0Mf2Yg4o7fJtak8aIwhllIYRJN8UJdWewLaFxSd41FDtqN1YwmDSj861Gk_FlkDksEI1GQih8UUNWngEukkJWy8kbsCHyV9Jq-AsiVdSUfHFKSpFGeq8ht6zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GMIfFiIo9fn-Z9WaloJzMk60EIxUH8kEA2XZbp1ErWMHiaW8w3at4vLO3VVumQ9kyQQMXmqSY73Je_daIJdH1ZfK-eta8S6s1IFp36sccdCwYviX4me2h34_u41d-69tmOla17BL1_tHgZ2OBDWanOzzd3gEL4eO9pOzuoUTEkaUmabLk6puVNHvQ-AMCOUmTy4VocU2Bhq7nxFu-uvKEa7quzqB4fGNQ29o91Q8e4rgQEaDqbiPCmbNTgv2RRn_jsAB9xpWLM6-pFZsN_ugvYRyfWQZLfINiV2bejOLikUkMoEp5zW0bK4L6VKztQSkk271_G9i37nhwk7y4BFczA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUrsmRM4w9VPn-Pl4b6TUn10qQf6JSmArSWtXUpCSHH-yrSAR0uO80w7CXX4-s0V0KaU7Omn1RR4__riTUDEAmx3Z273GoDZJOiU_ojNOkhNNYOKqcGYp2VlK54RSKK5kELQlxv4CSOZ7Dc3i5n5rQyj56sI8euLg0K36EqZWExr_-hFO-J7mtGFBcz_iuLW_mUu3EfnX408m7Ii_0h7yo_MuTDxz3ygBGoCfkbpVVycOcQ_pHkkp-fLUzMFewsj6KD6ZegmKM-UebKMYUXP-h9Iyntb-XmiCVwtraKr7TAUO8k4W-1_P27yaoJgOCSbXuxTUO6dtGWzSa44k4dzyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو اینا رو با کپشن: « اسباب بازی های من » پست کرده
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/102720" target="_blank">📅 00:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102719">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhu0m8nJhuIwdyxLKTZkg-JDCLu-QGqKPt5AZO0zrhCf00Bet7g8O6Fu7YAT_HOvds6X6ayFZHcp1d4vZKie3SddOfjZ5lyXnSZeZiRjBT5YYhOz_9b5Upr_HYyWzWz5oWgMyrXPhChq8_SZp3mq3u1FPj-laA26g9HNkZZlhsZJgsV_dJZrqta5eYBKehR3oosjAMF13OFg8ty_k7ojBfwoiNRSP3tfzmWEvJabNagHWWIAtXPRB7cR1yDWM99e5aON2gzNlz2EC8ByP7szJfzjwdKjSTyA1o7UG0NPw9_W6vUafXBYsuPN2ZHxz3Jg4kxqKr49cN_5HYRjCUA6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🔵
۵ سال پیش در چنین روزی؛ لیونل‌مسی اسطوره بارسلونا پس از سال‌ها درخشش بدلیل مشکلات مالی کاتالان‌ها از این تیم جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102719" target="_blank">📅 00:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102718">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSu_oe_Auh7UGBMdqZtGESjxg3D3_xfnxPZrNIe75_RqGlU1RukzhB4oAT2sSl1L50Rz9U7bwnoHw94y_PAomZjIYR4C_R1dRu02R-Tl0F0dHYag6Uq2Gxye2ohyrWsxoQqiBxigXCXHvCfmX9uyRN4w5CCTUKnjXFUYh4o3v2sUYKshBCG_TP3Y8a06WrDkt04x7e0J1i6pU0nq_im_7wm5Vfa2AUSIQ2AHb5B4OIbjIDLh7xtDr1Ng3krfYvpST1ti9OZlzKqSa7OR6lt4Th1xtQ_fr_SrmFYu4EDLoI5ltDloATPtp0dBDFAJaLocW0IuRKCNiYD9Eb76WAydGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇹🇷
فنرباغچه ترکیه بدنبال جذب پاولیدیس مهاجم بنفیکا هست و برای این انتقال باید رقمی بیش از ۵۰ میلیون یورو پیشنهاد بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/102718" target="_blank">📅 00:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102717">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfkrmJSN7-i8EOpu4q2hffjxJ9gEO7_ndi-d4nzTnTt1FjSFAeAWlvCBm3SJHRlnu492L4ySLJ5sIrWqNZV5m2uvJs60S096dE9bfrLjgvw-7IO05B1dAVmKfwG0S9ED-LIMETKCJH_OrGNuXJgTSjQ2JcqV6J69By8KfrJ1dqO29BCxI-7POBz3i5ggWAAAzCH5su-hwdk6CxDXu343L-84KFps3jZugBrThJgfpc4eMWMGY1M2WQxmnHTqDZIGuscEWb6J5QCy-39djqskQO7QHQ17y68J1wW29R0mSJw52S_z9s5a420SZJFzwsGO8JW_yOcH6H3qzAoRIPn9PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/102717" target="_blank">📅 00:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102716">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NTHnxdxM5M-huQtcVp809YTbWQ6kB1C0HilXnsSshgFE5fgssC-0VZMqE2LgHiaPjEHFw-Q5RbVqSJeuemhdegJG_KfbVsrxkzEAeKKS1rLohyS4rQftuULAdw6q-xZEQ9xvg7k671-i5EbWchJr3UPqUZ79sUv5UpWxvLvudchHECkxXKQp757ELAzu2rEqCSRFSPayLg8vtp3-d5PEvRVvHQ_a-oULqVRfZ7Nv-WjNxO3S7k2D2wBcBt6hYkuD3pDUiSV4WlHCYHAgF04Rv3YypYw_UShFsXMhQ3YHkPTyE2Q8UhjH9LDZ1SKGpWDhE7zEPitSe5GiF58D1jlEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
جرارد رومرو خبرنگار نزدیک به بارسلونا: امروز تو مادرید دکو با ایجنت آلوارز دیدار داشته. طرفین میخوان هرکاری برای نهایی شدن این قرارداد انجام بدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102716" target="_blank">📅 23:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102715">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5UP0zJBsVhzhz1rvsLhaif0yXTvndCI01nd_n1ZuqRrlqhy33-eK-qq8uPHObNG8wHpVZw2i0KXN15DxAv-juTRQHXSYOshw9UYVXT0CbvZzJJiESsTLgU9Lu0RPDz_5HEUEhxLnpoX3Iky1paHvPqB91e-atji6Zwq1aik5PxWYcdiaW4-cgGpug0xXOjbocYy_H6w8Rw-XzG8QofYBGEYDQYpFi9ETchgGZeYo2wWa4Rs213UTB3INB2Cr8DDznetiLZWxwtluH4A42ahgYSMF4WCAbT7_BOL225FdVdmZQ2158va3KAMZOsZ7qrQdG2H4lvdybDTPyqHbXXvGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رونالدو و پوستکوگلو تو تمرینات النصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102715" target="_blank">📅 22:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102714">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hge0yQmggCcbhCBCydkdrx_dRg5IaEyciZgGKwobSeNuYC6pbTP5UQ95vfDtLdxzuOi9d8fE_KZJ4Pay9yXN3Dm8H2RHogQZt9QcfwXVNX1Xkbir4hBMa6vrwncpnALFaQIfPT26tTIarJbzKWiIYloivh1DjrXFA88myZ8b2y1o-qqNPe-TQC4XhF0O16_pANSr-lHboHJfiXt5LSMjvU7WSTdC0JZtJPebEl7Ro_D5rgfE6iYdeHsj-YuLO87N9gf0pzJWozVmrKH6XALR0VTMobRrf0F1E7D2hIlXdepRymflr7mZgzRV7tlkUcXOuMpTQ19q3A-4qEqviSWz_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102714" target="_blank">📅 22:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102713">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3689824738.mp4?token=hcv9ZNzKKEYGx3fQ1mEsPRuO4IebKZA7-9dwGeTBWNugq1vazLpo5NjBaMFeb-Vi3uy8KHXfF2df7ZJVrU8u3dQJZiGY8JA63UueMXhBU9DZ2-EA4-oT5fCtz-XatOqbbFog9fO_kxmQqnUcF67DvD8wj975NLjs1Pw3S-J8gjG8X7BacfddJIYkobRV-l1JD0X3K39BPRSS-tLVzvzyARAuWibE9q9TvR59jzPZ459SajXG8cBbIKyJekAoI6Dl0I9xdsYRWHx9on_M7KjasH0OrcX_-UwvZgoklHSgjaDLxCrVCsgJWmtde34BbU7a5DwFNOXBlRyfA1sOIO3igA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3689824738.mp4?token=hcv9ZNzKKEYGx3fQ1mEsPRuO4IebKZA7-9dwGeTBWNugq1vazLpo5NjBaMFeb-Vi3uy8KHXfF2df7ZJVrU8u3dQJZiGY8JA63UueMXhBU9DZ2-EA4-oT5fCtz-XatOqbbFog9fO_kxmQqnUcF67DvD8wj975NLjs1Pw3S-J8gjG8X7BacfddJIYkobRV-l1JD0X3K39BPRSS-tLVzvzyARAuWibE9q9TvR59jzPZ459SajXG8cBbIKyJekAoI6Dl0I9xdsYRWHx9on_M7KjasH0OrcX_-UwvZgoklHSgjaDLxCrVCsgJWmtde34BbU7a5DwFNOXBlRyfA1sOIO3igA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
یه سرباز روسی توی دونتسک اوکراین لخت خوابیده بود و داشت افتاب میگرفت که يهو…..
❌
تصاویر مناسب دیدن برای همه نیست.....
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102713" target="_blank">📅 21:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102712">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIHMkWJ2vBmylzIS-Xlvo5D7p9svGngx2OEn72UtQ1JclTUL2_fOozf7iyIRB6Th_R82lk-_m_nPe7r9qXY7n5Qe0rhoUxfwRzGL6wFOKMNFMHWrTJDUpJ_pQvjXburYMeRjBLKZVXwlRD2Iad-JPV1kZZJ3k70Cm0-f6UjRegAiVhqhfBDVxN79EbTe-fBQ-HAJOsLIBlfuZZ36VomZ6gCQNJ0dwrQQV5qM2fD-oALEuyw_f2GnP9e0Znyyp2rU8IMwB2zs7O91xl2OS9MH03YGQxfNYJnpMIB3y1SCieaeHI9PVv5egfgdaCwrfUmreU-mlfNt64uQ0x5m7F4SiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدری از پسر تبدیل به مرد شد
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102712" target="_blank">📅 21:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102711">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrjYYzzm4Nojd3rztrjdBYfJnNfvme-4nxML7MRHOl2wqZfDUjHgSgnHoq2IHKmtSHQF6jiLXmb8IdelnaacpsmeQLphBBKdsLAzhXwE6_5labmj8hF7BuwTPUf0v8ytOgm7AxEGAzcUELlzAvhD4a-raebtZ0vNGUSA9cMwDmwbc1acOsFny3pox-cMUn5gXJkru_HyCidIRxzOgfR1OPmwf2HkOz06apYyvGNMMVmpc3rYDCsEZyAcnzWrlk3ViYyb4IQfX8tOFQsDXf-NEJbolmhhrslqY-HybN5bWRtLZCqamOQpGYSNOQsqa4Kg_QQWC236qTy-FxSWA9Yzyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل زده در 10 فصل اخیر 5 لیگ معتبر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102711" target="_blank">📅 21:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102710">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/at9g2xbaGzqwp3pA95rm4JHP3PUxNMk5BA9tpjOtdtHECQ62WvfhXNi3tH2CZs3mpwWIchcvKAdfUYx7YC4Xr0pxghzWrgtEo_MP1ekXPw8RDIEAJqaTh7t1bhPvX6e4cK9PhEjvZeDatsJpfaAn2h7_gzJ4a28tAcXWKzQgOxLc89p4AeU7Z-LvMVcA4Of6j-ukvLLLuQ7XwdTMwQtMaqXR7u_0ywNQpfSaMLFIzpsSQ9Z6VTCMiZ30Wd_Kk4wsfAil6QOkQ4nGD4Tozqy-QdFCfwyac8QpFokTIamZTm_DxHn69GSpXxWEjzPiqQKtWTePak8BClW0cXdA96UxtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
رامین‌رضاییان خطاب به مدیران استقلال: دست از اینکه منو بذارید جلو هوادار بردارید. من حرفامو تو زمین میزنم نه فضای مجازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102710" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102709">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMayle_26TOtK7J_9IA7TDW_pnTwA_r0cnnzeZI_q5Eg5ZXeHkEr1B4gx_mJyZBe_xddbKQ8td-07HiRl-uQDGpyiIRNX5-KXefQnvQM7OVIBdMrOYJd_1ah0WwVaQ4Y0OEZCT5CRB-fhSlZP01cezGX9Xo1uwYsPSWi_PtZ0KTDiBVdIROezLaCS_SaFTze_msYlU3QrHkirRg_vh_11zi85xTvo-80MS93MphVOSkqpVnDmEkfeEACERtQS5KoUYHi6DK_cXVTTdXO-nygk3Hr6sJrvAsn-Rv1ciRhnZWDVLXX-G0ouTgYIpjmSyq0efKBONUYZCeJoD2m23saiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری
؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102709" target="_blank">📅 20:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102707">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PVndqOc5tM-lc1bpiJVz2fkk3_j6d72rJAeqNJWZwrPGf0JR6aw6MAdxqhAhoEgLbWJ71tb2WLSeSXCyv5znKaaRnf3EoPtKulsTFjE-rES-BwrRErsJmSmPYY9q3kBgLjBMTYtdc0w4OmJVbtxJb8VihOYRwNT6vIu3BviIx0s6M_l24iAuYVRxgDswHO2UhadCJQtOsH_gvndxcmaRsydYePvZgkzqWAhmtkV8buUZh0IzmOK1Mp-hhfWom0HcbvxgKZfoyjjJU_MF03p4GLpuKL348B4nG8HP0gpuUFQY344dNGM0fM8zA-9DdM4IT2qpeFOOW3RInnnPzCX0PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tGJG8gxBc8UhysTcR_LEgrXKpz9qDc3g5q66ADYBHn1VfBoV-jXE5AaJbOHTY8bCNkUQj6FgdvZTjRAZiOI73k0i_rjA2iREuhzFzvGzhJ3Z8_88rWvySzGDt_bJ4YJWnJf7uRhdpkW9RvMtCgZulrtst4imTR3A2powATfkN7MgeMztg-6mBjiN16vujjUmHzVZdjN8f7j0hlqLPiuEMMv-QlSJXzzLLcaBJhulYliaD8LKDhJcIxifrJ51pgygGK2Up_9Egy9Lvdo2gfgjMCvdwLQWAvYpDCmWI3QXms8gl5qyItm1EBhZOdQS4KfDrU8iZRxoQts_PyXZ0C4iEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
ویریجینیا:
من اصلا حسودی نمی‌کنم. به نظرم وینی جونیور خیلی هات و سکسیه؛ اتفاقا باید همین‌جوری عکسای بدون پیرهنش رو بذاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102707" target="_blank">📅 20:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102706">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW7_qQzPAOvHv6eiVHq6vhkD8R77o12bHAQbNxY1uSL_UUsBZk6cZnnT9lEr0OBWA2E1KQQxzo7Om8xOsuIK8ID2hiG_Iz2alqM4xkURMfNoEfKd6q9hjhmjzapjN8LuTTc9TePwagW4sdK4dX_KgCaGOL1FKfrWW52TyOxoDmjC1cfJkqzHC3hukCrAsC4fSoEIOAU7TWacAguJOr2eN7CXEcTPz2KbBi966oOc6vvVS9e-07Nj-NuzO4whSR57iWPs6-48VN03VKcY_7Gmm3xYH0Ys6VRFhJ7jClJbYBuQOsl_D4d-L3S9xUlz5O2W2i6OU1OwG_cGBMIuA3RBPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
فووووری از فابریزیو رومانو؛ سیتی به دنبال جذب پدرو نتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102706" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102705">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b139a17c.mp4?token=Yc31eviIVhlxLTqxJyRiYyAUMjWy8l9vjgHviaPXX_NKYevmBdpM8QY-SxbwW-ln6q7_195SBCh-dkKolddXegl1NnavRzDmbQ4W1DgSf_GV1qi8UVemT3cGYs29ulUSkUc1CTzh9mTy_ougGVCpyTEBDZBaPlvWqWRQXZXnFODIDyXqeQpf2bH9Z0GOf7MT1tjGTjO7w4R-jBG2wUlwxUPwR-7BHrrCd53GxzBSVMVllyoeG2NIzEf1KUlO_rAJhQje22YXQrnqjTGGgv7sfd6JF0Y8cv4tXB8hbKca-bpVCCE-k5jygLjY3urfzltbf8uzL3clE7b_kabjtrlF2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b139a17c.mp4?token=Yc31eviIVhlxLTqxJyRiYyAUMjWy8l9vjgHviaPXX_NKYevmBdpM8QY-SxbwW-ln6q7_195SBCh-dkKolddXegl1NnavRzDmbQ4W1DgSf_GV1qi8UVemT3cGYs29ulUSkUc1CTzh9mTy_ougGVCpyTEBDZBaPlvWqWRQXZXnFODIDyXqeQpf2bH9Z0GOf7MT1tjGTjO7w4R-jBG2wUlwxUPwR-7BHrrCd53GxzBSVMVllyoeG2NIzEf1KUlO_rAJhQje22YXQrnqjTGGgv7sfd6JF0Y8cv4tXB8hbKca-bpVCCE-k5jygLjY3urfzltbf8uzL3clE7b_kabjtrlF2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⚽️
#فوووووری
و
#رسمیییییی
: تریلر جهانباز FC 27 منتشششششر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102705" target="_blank">📅 19:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102704">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISxYPZRyLEnyjoegFslWzIXUmbgdmZhyjS0NU54cj-Q3oTVtFW440Ovl9gSQeqCdJvEvc4RmMXKbPTPrqhOJnb-VunjPrEbxKXsjuVsRz_qsIoqYAUoCJZo69aYDE-6d6Em0xYXFKmEpp0jAv5sCaTJu-rh_5qHv72rNzQkRBGo_XXaku7jjEDShBB44ShT8gWGt-t2XjVZ64NDZ_8U8i5UlLSL921f3GiyY2On6YDVv-veRJ9_bSkyOjGbRZ2SCkTwDF5H121p5CGaKNvcn0vAwxApR1h9o_sLHXg375D2RNqWzLDZshWnB8uPquI-4t3Iby_4DJ_eGVXiVrH1KKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
👤
پست جدید خاله جورجینا در تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102704" target="_blank">📅 19:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102702">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rc4YbGMVcNPeLSzeRaspAHQHIsez-55Zylyjl-3fEFmo2-qN_FZRYRVHoLaAgpYxFiodpx291KbBGpfX3gOcKfec0hxFzqU7wLmI7Yywds1F9VPVp7PUVdiu7nG6ATHGZapqTdb5hVn0pafdreId7UIF71nYXjIfSfA_28b_jRI2OQx5r09YCdnl5czAVe1zBYf6BfDvkTHrYhMd1lGjSkhFyHyj0abZCFabO99qOqt8Gxmk_joHBvhStYxARdMPRiVmUY1FAzMnCPd-d2DN5Q6I6dI6nRlQFWclO1TEx_vWfZkidEL0hz9cyGsj9PdX0ujfylSuADQtNidSBd8r6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8lxRnwBA5QHIglGFVopTlnKNKI1jZOsaLYYDD9OPK_a7qXGuaEH6i26K-b6LKHtgRackHu3yWqfg9iSoR1tQc8mkuuZQGIBSQXrk6yIHCQW48uE4kyR0hzCxzCbarAdb8RcuUjLANYO5Zut0EHZvAh8KnvhgCW2pQA0mz3hbOB89PFDve3u92_iAXwnd7t0IsayFAm8EwHRKfiliCrvcgU9E3NvgmPwg3o1eOmrJoC9S_1t-OsUPhf2gbTKwK4r3k52yUST7TylzYR2OWK4zQs6YSwZ2OgTk_gtc7x2WOmiAN9_ftPNQdDCx6ZTkMneFhzTcIX4SuVZWt1YR894vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
رونمایی موناکو از کیت سوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102702" target="_blank">📅 19:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102700">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94b7db1a6b.mp4?token=h9V90l693rzxXz3iPx2QvHOFDU7_7hbHCwC1dTADCa-ybQROC0JHPbxX7x94Ew9T5v_4gmWjYyJxytH4gnrq67skWzqdllK8oegwJj6bZMXQoxe7oUaIMOM6ptr51_EtgYmpci3FzOWeLnnqWv_cPcUSIIFLJdFCcOm-WiIF6u0kLUYmEUHyTJwG0oBvCDGVXRcTvaZzdynHOrExtFRGLuwL5XV0gOoKLjTaKxP5N_0XFQdPr9IhZ83TwQptxtyv-wzMDHHfhCAsS1iOhAetQEOxFIp4TLJalQ_bq_ohSUFcnUl8sCAigAwvb7TPY50mySoyU5xfcJmCfBUBeNxqwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94b7db1a6b.mp4?token=h9V90l693rzxXz3iPx2QvHOFDU7_7hbHCwC1dTADCa-ybQROC0JHPbxX7x94Ew9T5v_4gmWjYyJxytH4gnrq67skWzqdllK8oegwJj6bZMXQoxe7oUaIMOM6ptr51_EtgYmpci3FzOWeLnnqWv_cPcUSIIFLJdFCcOm-WiIF6u0kLUYmEUHyTJwG0oBvCDGVXRcTvaZzdynHOrExtFRGLuwL5XV0gOoKLjTaKxP5N_0XFQdPr9IhZ83TwQptxtyv-wzMDHHfhCAsS1iOhAetQEOxFIp4TLJalQ_bq_ohSUFcnUl8sCAigAwvb7TPY50mySoyU5xfcJmCfBUBeNxqwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
مطمئنم شکیرا ومپایره مگه میشه آخه تو 50 سالگی اینجوری باشی و با 30 سالگیت فرقی نکنی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102700" target="_blank">📅 19:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102699">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd0cef8d4.mp4?token=pyqH_vA2Dacvponh4AHC-E35Cyhn7BlpsgIYxczEN-i70bkalXjar6G2cEF0DG6oWEufq8dDIrDzlnWoeO-aszDDEEJZenjv2XAIZnsh2X8ifdChD42fMGpsqxhl0FWe5l7q8QpH4Y0U7DEdsmRlDSzlUlLa77dPzUPmvJ4Yda8Ji2J7ciZP_Stam0yqSBS5ZM5mWthq7a7bqpL-K5jwKCdGRGqgwAVCMLN2jFgMVRgfLJvePfivTHE_TYer9UVuNeahBgUxTqWWYQx6a-S5hDu7dg3d78qpeYLGjYgRmNAWWvbwZ-BIXJNCUdE-DhkG0ALOUAw66X8iBHEpsifssw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd0cef8d4.mp4?token=pyqH_vA2Dacvponh4AHC-E35Cyhn7BlpsgIYxczEN-i70bkalXjar6G2cEF0DG6oWEufq8dDIrDzlnWoeO-aszDDEEJZenjv2XAIZnsh2X8ifdChD42fMGpsqxhl0FWe5l7q8QpH4Y0U7DEdsmRlDSzlUlLa77dPzUPmvJ4Yda8Ji2J7ciZP_Stam0yqSBS5ZM5mWthq7a7bqpL-K5jwKCdGRGqgwAVCMLN2jFgMVRgfLJvePfivTHE_TYer9UVuNeahBgUxTqWWYQx6a-S5hDu7dg3d78qpeYLGjYgRmNAWWvbwZ-BIXJNCUdE-DhkG0ALOUAw66X8iBHEpsifssw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره خنده دار پیمان حسینی از عکس گرفتن با دخترهای بلاروسی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102699" target="_blank">📅 19:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102698">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJNwkAi0zu2F_lxeGtaUozy_FqKZcJhe8t8X8j7w0MK9CteAMvrbNAy0upBcogla085h3gSy_N7HAV6txCtcpSs9_0Co3R-G8FVibJiqTeYGYKCZF9L5PN-V-B3PS4UcuMIOwGaCgSHD-VZMJW0Ya7v75G-oaMc0tObIbbmjseG7cSARlfy3FM6SAQvmTqudlPjq8ZgQ2zet-RTKC5ngo3GlH8WEviax3QjSWOKTGlfr9naFie5GH6rzL3v63Hl3I05CroSWXV1G30AM1etJtQh60_SurSPguLZoEZ1xrgYgKRexAqDGqAikxdpgn2XqMuiMwejZtQGBovXpAbWKiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102698" target="_blank">📅 19:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102697">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8Xi0zXGUFmevZ_CjQb0Cx8h9XRYnRoQAcnoRLXK8bThD4f7XV-kM9U6YVZzd8leuKCPUBMKEc3iq4KG_a4bWvb3iu0--ok6ICvYPNRYA-Ouh0HsASGGjOksaSHJSaNBoO-mOLnmdYLZ3twKg56ThBT-aHdTHatznxS2h_FHII7CWjoLkhZaC54YwDMoIy6d8IQ-Bp46OrvRydQyKEbotYxqd55CKypJP_jgIv6D67uUCd7FgI278fe8cHmec3O8Q4LbjLLrr1FDBKouGYm8lkg4tl5lb1_bGnI3jLXx0VKP-6HymrVhr-2n70yPuNmgD9Se4t54ORpP9bURDdYR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇹🇷
#فوووووری
از رومانو: ترابوزان‌اسپور ترکیه اولین پیشنهاد رسمی خود به مدت دو فصل را به محمد صلاح ارائه کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102697" target="_blank">📅 19:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102696">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlKJXyCjAw5gDNEDNhN283lGTQb1yobskak4nj8EgcKbsA3w1pDUn-N802y6MRfEudehSjyHeoqZWxDdHMjs6OnsouYxkasZ7_QbwOWlcEGuQulwz_pSbjI4Fwyl7idTu9cCPuNb3sm60x7PX-RkP4N6w7Tb6UAMH0bc9-I8VARQBK-B_ErDCwwkeBKhMkNx6BPnBlg2T1YFA03QM20ZszXlIF4k-ezPgWOQufC1SHml-r3prpMYWqAwBiYCK-ZbHiR2YclGRDbiWt1edsEopU8w2Tcm9Agfmc0TcDx2K1P3ZLAK1GuNT2wiC2BrcdQ4e8J7M9CFvqSqsNfIajoQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#رسمیییییی
؛ علی‌نعمتی با عقد قراردادی به تیم لوسیل قطر پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102696" target="_blank">📅 19:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102695">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b46370582.mp4?token=kBdLpk91-pesx0hC5jPeD3z6VI6sXkpwu_Dv0Pw0JvX7iWBPqRSuq6pq-eGPirTb1xeKIKOOKJntvl2hwirpV4nvOu-yVWm4nSTD6qZReUtg4scx1bcokwrBkXp87TXibmXnK6kT-1JLL-1pEaKmOvkPSy_9qEP9MpIAJLa4qY2Whsq33Xn8MDV8z8sV_uF63QvzFdx3TAutapI4CD380jKn4ZCnY54X-osskn2jTRo4RmssrjD2p0HZceXCt5PH9EC5uPfVOSUCUus0mPOUj8e2nSd6411XazNWvUjAPum3odb8p-2YsixRmMKE-zDfGM72thAwvJDNWYzKmGF1ool8GVvjSfp-eht75bvy7Jyn_XxG112d4NOglppPwQBKftw3OUMB2hCDiklQwDzkQVD9614XmhPMQfHNqdFFJwueh1CZj9KqCyqaJcLtfrsjIRS9NWUSqD-IGvj30Gqm6sJbI9h4kYj9Fm5nqPJ64U67Bca9XjHyxHsb2yLrL229_mdxyWSigrZt7bKwb1EwEgO1oedY0GgTc9UejhyjNKVwILg5DIhPCxIP1LNHctdS7bbKm3pLy0tIGMaON92TA92OVoYyoJTVvtv68pjDoYRArC1D5MDqFzlbT4Z5uTr0AFd2Os9hx2DpTlVULwI1GzG0DeKbHZjiRBmOCPIdnBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b46370582.mp4?token=kBdLpk91-pesx0hC5jPeD3z6VI6sXkpwu_Dv0Pw0JvX7iWBPqRSuq6pq-eGPirTb1xeKIKOOKJntvl2hwirpV4nvOu-yVWm4nSTD6qZReUtg4scx1bcokwrBkXp87TXibmXnK6kT-1JLL-1pEaKmOvkPSy_9qEP9MpIAJLa4qY2Whsq33Xn8MDV8z8sV_uF63QvzFdx3TAutapI4CD380jKn4ZCnY54X-osskn2jTRo4RmssrjD2p0HZceXCt5PH9EC5uPfVOSUCUus0mPOUj8e2nSd6411XazNWvUjAPum3odb8p-2YsixRmMKE-zDfGM72thAwvJDNWYzKmGF1ool8GVvjSfp-eht75bvy7Jyn_XxG112d4NOglppPwQBKftw3OUMB2hCDiklQwDzkQVD9614XmhPMQfHNqdFFJwueh1CZj9KqCyqaJcLtfrsjIRS9NWUSqD-IGvj30Gqm6sJbI9h4kYj9Fm5nqPJ64U67Bca9XjHyxHsb2yLrL229_mdxyWSigrZt7bKwb1EwEgO1oedY0GgTc9UejhyjNKVwILg5DIhPCxIP1LNHctdS7bbKm3pLy0tIGMaON92TA92OVoYyoJTVvtv68pjDoYRArC1D5MDqFzlbT4Z5uTr0AFd2Os9hx2DpTlVULwI1GzG0DeKbHZjiRBmOCPIdnBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این خانم باتجربه نکات خوبی رو در مورد دفاع شخصی به خانم ها میگه، حتما ببینید :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102695" target="_blank">📅 19:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102694">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wsfl2lj2JMIgSlmrMCInOqgfkAxdevHeVQAZAUGEq6HZC5hJCTTlozZTxvGgZaNAyerMeVLL3uA0ctvav5EMNIyGYv0hLk1X9mmQjXDg25En-nDUdwUv7d6Jv0R-ddp_oo81a1139sd6F3gMN7XjpVKvNkmAKJs7pfU9FYN_DJp9n9rbjwA-WG9xwil_chHzbXFymUi-LUTmay79LMlBk3MMtnxpZCQmeU-z5NtGIPWZsHSqs_eeAQx6E7wpUWuB8dWXxuhwwwKa-nqWKDPaCwop5tlfuvWw3yfT1Dy7eGSX-YTmV-hm606RPA6dMgiMC-NNdo4s0QTWQhf0y01NaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی برای حمایت از بازسازی مناطق آسیب‌ دیده در سیرا اوئیسته مادرید، 80 هزار یورو کمک کرد.
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102694" target="_blank">📅 18:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102693">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iD2jUiZh0l6DghX-Ln8C7uA8c8ARl2q6jAz7vx_QaMm3XmUfqu3paDqlaDX_bMl1sGxsQAplXnFxgjvhzUcI4NQew8BC2Pvqg3r7Z2DW2Luxd2O5R_jjfWjaqSdRJcIhx1U5AoydVfABhlWedCct4d0EAaUjYj5kfONmIY4o3cTf6fLZYmMEHl7HurE8QEitKQlfLVD8kaqLe9i9bhPOvJtDz40BQC5c_kdSKupb9AhDN1ANam4Nl-pTceupbLf4IPlT3KCkDgZ2FeoGqFhV8g75Gh4S4LC4VTQsEeWNrYxPMxHFkHkJ5s1taCrGLlYouc1I2JPt09do8xr1gaNKOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇮
هروه‌رنار سرمربی تیم‌ملی ساحل‌عاج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102693" target="_blank">📅 18:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102692">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f0d298b0.mp4?token=urZhn5loDbJ3_szNlt9pE6JbmrprSkCWSkV_H3JxZRuz7Mi_fy8EyRUrIYbfAY_YlrRu9G6MiJd8ZwssF9DVdvuMlOhF4Eh13CWaDMOMLPBwshcqP7Gw7X8CjxP9AAIWqof3IXHtUL6iO__7chkTzkM25MD1rRkyv8JMgeLZ8aE9NdWmO92Lr8thtloy_iQfZudZWG08oWAsNytB2-oiADyXmMzMoSOHllDF0hwbmep-ia5CxnZx8_ygecU4AXr7SrTpHEP9aaNTfGlzYTbuCqNpESh4fJUS42qSQtY5QjKYU5z8b9w6suG4Hjo7S62UOXFtsyR47Peh3TumQsjhAzhvSeqx8YE2QDwDc9KvctTDESf2n3lcKlsthNPoxjylcLQfXmdX-GuAX0i2rFIq8tWjrQidvPquhfatsCOJ8zjko_ekrJnjwqVYcfxZNVfhw7Jqny4a1Y9nN37gMlwo7txgTgDGmOQLXi7UrqP7uHI8MM-5FsHX3VIgz-689hYvHOuKoTRqcmRsGOx_EJZVFq0Vc-KZx9iGejS8sYPunhv5NT-GJorKndm4nfp82dA7L1f-v5Gw7-glM1ugwdHJmgpUACIAGorPJ1Q7pJNQyVmmQ_Qe01Zo1qn0KxHG_tvkkcCspM-GasaQ-hv85JoGS4PG3YtXLFaLh_5t3UHOziM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f0d298b0.mp4?token=urZhn5loDbJ3_szNlt9pE6JbmrprSkCWSkV_H3JxZRuz7Mi_fy8EyRUrIYbfAY_YlrRu9G6MiJd8ZwssF9DVdvuMlOhF4Eh13CWaDMOMLPBwshcqP7Gw7X8CjxP9AAIWqof3IXHtUL6iO__7chkTzkM25MD1rRkyv8JMgeLZ8aE9NdWmO92Lr8thtloy_iQfZudZWG08oWAsNytB2-oiADyXmMzMoSOHllDF0hwbmep-ia5CxnZx8_ygecU4AXr7SrTpHEP9aaNTfGlzYTbuCqNpESh4fJUS42qSQtY5QjKYU5z8b9w6suG4Hjo7S62UOXFtsyR47Peh3TumQsjhAzhvSeqx8YE2QDwDc9KvctTDESf2n3lcKlsthNPoxjylcLQfXmdX-GuAX0i2rFIq8tWjrQidvPquhfatsCOJ8zjko_ekrJnjwqVYcfxZNVfhw7Jqny4a1Y9nN37gMlwo7txgTgDGmOQLXi7UrqP7uHI8MM-5FsHX3VIgz-689hYvHOuKoTRqcmRsGOx_EJZVFq0Vc-KZx9iGejS8sYPunhv5NT-GJorKndm4nfp82dA7L1f-v5Gw7-glM1ugwdHJmgpUACIAGorPJ1Q7pJNQyVmmQ_Qe01Zo1qn0KxHG_tvkkcCspM-GasaQ-hv85JoGS4PG3YtXLFaLh_5t3UHOziM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📅
شش سال پیش در همچین روزی ایکر کاسیاس از فوتبال حرفه‌ای خداحافظی کرد.
"عده ای برای پر کردن زمین می‌آیند٬ عده ای برای تاریخ"
⚪️
🔺
ایکر کاسیاس از دسته ی دومی هاست٬ خیابان ها هرگز ایکر مقدس٬ یکی از بهترین گلر های تمام دوران رو فراموش نخواهند کرد :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102692" target="_blank">📅 18:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102691">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5e14ddfd.mp4?token=vk7eTBLQgkUS2mhzR1LGgbvOHLFipo0gvjGzLi3luDCQkZcbYVCl9EYroS2C1TpQd1jKAaEGgM58JGLUrzG8Mm5cpUrCEYbBttM9m6JloNqIsuLrblwjmbbbuqZXk5ZdO7iGup_MS56x24Wovre-MafwfpO5SVqrYDBJCz_uubE2P1mXAwVoawPyb2nhpJWVo2-0UyDxW7RDuBeWwvsJIOOjVjaEj65kOGF_6MMKiYUt9SUSTq8x5qIjLUJLQxBZ3UurMUaPznXMWSOLGf4Fl0dUTQ0w7-Ft-JrE9z2rj3Y4LZYO4t0F05YImAfqyOX_NxxP3HJdlHObFPKRSzP5EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5e14ddfd.mp4?token=vk7eTBLQgkUS2mhzR1LGgbvOHLFipo0gvjGzLi3luDCQkZcbYVCl9EYroS2C1TpQd1jKAaEGgM58JGLUrzG8Mm5cpUrCEYbBttM9m6JloNqIsuLrblwjmbbbuqZXk5ZdO7iGup_MS56x24Wovre-MafwfpO5SVqrYDBJCz_uubE2P1mXAwVoawPyb2nhpJWVo2-0UyDxW7RDuBeWwvsJIOOjVjaEj65kOGF_6MMKiYUt9SUSTq8x5qIjLUJLQxBZ3UurMUaPznXMWSOLGf4Fl0dUTQ0w7-Ft-JrE9z2rj3Y4LZYO4t0F05YImAfqyOX_NxxP3HJdlHObFPKRSzP5EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
#نوستالژی
؛ دیدار فرزند رونالدو با مسی فوق ستاره فوتبال جهان در حاشیه مراسم توپ‌طلا سال ۲۰۱۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102691" target="_blank">📅 18:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102690">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxylJGOYH8HFsHwOwwLSx1vKSsnZDZ9bxckDkNc7ewtGjlwV22D1Jfjqk6IitF1BhK_6G1yIH80Llr7bO-FsqoD6NPu19zIP6prUy7XBuupm8CIEZP6-gyggDzPX7_MlWPyrHY-Lq1hZKsNaomTwhAhPdqGvQyIwu-8xTTBTRfrBupbFPQChIEnjUopDHIcH_itVNtu8q3Cmw644-0wUNAGapNbNsSaBaQJRqAtt2nZcaEt8MTPXrhtQuukgonFCY7XQpHU9ok4igYOGZFHb7HMkwfo-OZXd25U8qqErGwGiVzrAVLQ7jnWkfkdR8CzDgNxERs4mIpl68lYJNNPy8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
بازیکن سال 2003 آفریقا: ساموئل اتوئو
🟢
بازیکن سال 2004 آفریقا: ساموئل اتوئو
🟢
بازیکن سال 2005 آفریقا: ساموئلاتوئو
🟠
بازیکن سال 2006 آفریقا: دیدیه دروگبا
🟠
بازیکن سال 2009 آفریقا: دیدیه دروگبا
🟢
بازیکن سال 2010 آفریقا: ساموئل اتوئو
🟢
بهترین گلزن ساحل عاج: دیدیه دروگبا.
🟠
بهترین گلزن کامرون: ساموئل اتوئو.
✨
بزرگترین مهاجمان تاریخ آفریقا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102690" target="_blank">📅 17:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102689">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
⭕️
🇺🇸
روبیو وزیر خارجه آمریکا: مذاکرات بسیار خوبی برای بازگشایی تنگه هرمز در جریان است و احتمالا امشب یا فردا یک بیانیه مشترک صادر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102689" target="_blank">📅 17:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102688">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRaaU0Ee2Q_ia-1DEAERHkMMB1NG36pHwElJZM_Mg_vyA_71ugd8sNBnf6xAmHddxjnAE3oGyFHuvXFg2zj9EDoRaE0PIwXCq7KR6fLMtPza4hsEkW0AkP2q4WMeZ7KvEiiZKwD4X68aKfHlAOIek8rweScXncYitekfd1f3hREKnYIp7IpWJu_p86uzuM1fPnZaJNx3_omUgJC6T4S0o20ewLPyqWvNeorpHEd3qHoRrq8_Y2O2Xqlw1ffUPLUNk7Weje2p_idbPiNXAReFI7zMMotUZ2z3Ww1F4EppJTaO53lQOrHiWjJRSP3AKAFjqCoMLex3rSOcnUZWEJMEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
چلسی صدر جدول تیم های با بیشترین خریدهای بالای 100 میلیون یورو در تاریخ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102688" target="_blank">📅 17:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102686">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAIedibtgAfqpuFnhbmI40DgrjsSPYU2XdI3QiUTYVDtZyc_IjUscdTXDh4HFVJhcWC8y5zCG49FZTRRvOAZ4kYwCP1HC8fsl0zv8d6vT1G5wvKqL84-bP7z8yeCYogrH7wsULPWAYVDfL12SjJhBjGpG46K2ndT0FN2GMj-7NuQEy0YhvmizHMOV50dUNFiqp7V39s6NCvkBNbW6z6nmuVjtbYe-q15KcS4YUq0Zvx2UrhYN8-3kF_Ol-t94sZ4q7zkh_zqakePlhLlV_Ntzl4FVRSRY-vJFNKX7N02Z2K86KSE723gzuEx2Oa1gMeKFQcb-yksofvyBuz0WcppwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7APQ9i1SCYeoLwn5uFJofVylrKUHAhDFKlcZ-9m00DDwljJiEVMkUmHUq0Rv8Nt8t_ej6YzHg4C9h5yJJSRfsJvoW-RldWOvgbpLo5Gesya_uN4UyR_ZFNJjAQ6IjlkXD3tAJpPsFVs2nlHaHSLeOWZaXqwb7gc2QntRA0JiIfZqHfRnvvaTgq6S02nKp973Wpszz1zRP2sSyAOmfHRMMVlLZPoPQ9MG8tbBlpss88puZVhcQkveAiZc_k4GDHhqnrFGTXAb_SfHNstOnmWRoOASvvz8znRt7gXA442x9tbOwSvJ9C5HsKzUVSsx8788oPTXsmx1485JrOfmlTnhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تغییرات رودریگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102686" target="_blank">📅 17:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102685">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AceDAJz9KevIt_jqG7J5qMyC4bkHzsrPhPJp5-zBLv-DhbPLY8PwL2pUs04bD_1G0mTm40w26hsrBHdo6_1eN72_rplBaoK1dPhFs_x4Vsv8kqamQ3P06RM5DImNQZ_W8weli0fCw5SA7P1pDioxA35Bd9PsCIJiUX8MWu5DeJxyqatQ-VIpBUVsOREHzGCDBNxCwd6uhfEC25BgBT55NiOGMzLYEARBQBAXypCRcuFr4MZk1ATFJAAitTyKuz75IS2_y36M7UXgaqvRax5xfaFu6JSm0qO2xlPhHEQhOnrpu8dTmasBD6tGMSgH5pbVdJlHXhPpBJKzlth6SWyaZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
14 سال پیش همچین روزی؛ باشگاه یوونتوس پل پوگبا رو به صورت رایگان به خدمت گرفت.
🟣
پیرلو: روز اولی که پل پوگبا با ما تمرین کرد، همه خندیدیم چطور منچستریونایتد می‌تونست اجازه بده بازیکنی مثل پوگبا رایگان به تیم ما ملحق بشه؟
🟣
بوفون با خنده به سمتم اومد گفت: واقعاً پوگبا الان مجانی به اینجا اومده و منچستر اجازه داده؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102685" target="_blank">📅 17:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102684">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78b336809.mp4?token=D_dBb6o-tWyYaIP-PySxBC2tcXLcCm93yFh7TjCIpXxelhdThwM2RoH3nArvX_zWxHZiIVKMltTPIZRe2LQaM7V67T0auLDx6f5xht8BgxaUiyLIdzmzQVdD1tm9FLfqzOAmx8wiIChMxgDIdv1AiqE_PuB5uHvZLJ8A-vTnvMYmd_5R2yfxV_NnEHUzrOnINNbzoU586Q5DqnKcFjIjDaUo8HxEslZgY6Rz_-PJh3zLekMofxDkvZavJW6ggQKxAERaxnQT6EIVsx2rKXavUDIiTdeCjNR7mFFbNCnEkZVA7zyVKBdNvdOJr6NVOexZDKYxxrzgSGQUhWKvH3Y62Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78b336809.mp4?token=D_dBb6o-tWyYaIP-PySxBC2tcXLcCm93yFh7TjCIpXxelhdThwM2RoH3nArvX_zWxHZiIVKMltTPIZRe2LQaM7V67T0auLDx6f5xht8BgxaUiyLIdzmzQVdD1tm9FLfqzOAmx8wiIChMxgDIdv1AiqE_PuB5uHvZLJ8A-vTnvMYmd_5R2yfxV_NnEHUzrOnINNbzoU586Q5DqnKcFjIjDaUo8HxEslZgY6Rz_-PJh3zLekMofxDkvZavJW6ggQKxAERaxnQT6EIVsx2rKXavUDIiTdeCjNR7mFFbNCnEkZVA7zyVKBdNvdOJr6NVOexZDKYxxrzgSGQUhWKvH3Y62Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
امشب، سالروز تولد پهلوان مسعود ذات‌پرور است؛ مردی که از باورهایش عقب‌نشینی نکرد، شرافتش را با هیچ چیز معامله نکرد و در کنار مردمش ایستاد.
🔹
نام او برای بسیاری، یادآور ایستادگی، غیرت و وفاداری به اصولی است که به آن‌ها ایمان داشت.
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102684" target="_blank">📅 17:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102683">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTz4h5Y6YdUbIj2XoqCzx5TDNGP9KFWrjy_9uwrN-wAZFCDFOf1T5rnFYhVgfPVfnb84olORucEsboAPjpyqZoRYqLw4rzGXLeU__ov1db_5_QPaGPCx7XYtrLXIV9yRafXhozbN3k9INIDhmFX4PCiqMk7Fqk0SBEo0wpv_c_pfpFl5uGoceBICjiaYyPH52JcGZu4SS_WqtYJYo8FZMDMYv0srkT4DZ19U6KbfWz9nPBqaeNFJsLBeplzYHd1IXGh6AFJZlcEu9NVAFTXT12Qo4bwdO3cOStXNT6z33Za1gSyk3VSufzWZkfEa1cDK6g4enkljd7iSf73OgW1igg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پست جدید بیژن مرتضوی درباره مصاحبه همسرش با مجید واشقانی و شایعات بازگشت به ایران: تا وقتی جمهوری اسلامی حاکمه به حرمت خون‌های ریخته شده در ۱۸ و ۱۹ دی‌ماه به ایران نمیام
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102683" target="_blank">📅 16:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102682">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3348f33cc.mp4?token=duOYeyf7E6Sn6c-P73vvY5K4EC2CaWah3XM0Pf3Kdgu33zSa3i7wvRDCEdWYjyIoD2G6-JB9BalytHHsa-Qre7RyEF6AIADocf3wG85bqd94qv1GDcVVROEofMPu-8slgBQFlpI5uwChdAN0stHFh0Oxxztp5YS2tXZeDmYBbSSNH7ij1rlBCAiSOaIPD0llrPFgbtGJJJEj4hGo5qX17vIYPRnSY03YkA4i-OqU05gHrW1YC_k_V0TxD4zK3wHd8hQ_cHMWJRICCeIJ-3Ef4vtl0BuACG-0r_wetHbb5rxwYHkRE2ht4lbuJ2qmHXovISVAJjIpOxL1-JYIO9qmgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3348f33cc.mp4?token=duOYeyf7E6Sn6c-P73vvY5K4EC2CaWah3XM0Pf3Kdgu33zSa3i7wvRDCEdWYjyIoD2G6-JB9BalytHHsa-Qre7RyEF6AIADocf3wG85bqd94qv1GDcVVROEofMPu-8slgBQFlpI5uwChdAN0stHFh0Oxxztp5YS2tXZeDmYBbSSNH7ij1rlBCAiSOaIPD0llrPFgbtGJJJEj4hGo5qX17vIYPRnSY03YkA4i-OqU05gHrW1YC_k_V0TxD4zK3wHd8hQ_cHMWJRICCeIJ-3Ef4vtl0BuACG-0r_wetHbb5rxwYHkRE2ht4lbuJ2qmHXovISVAJjIpOxL1-JYIO9qmgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#نوستالژی
؛ هتریک رویایی علی کریمی جلو کره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102682" target="_blank">📅 16:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102681">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018847c7b0.mp4?token=MkvA7fZmT6vUnUIBA-ghHRQ-2Fs8F6yZxlRT98vJR5STqoLdmtALTLczMUEWPGqPMUNaol7q-XGPCVV-skSJnJM8hooacRlzEOrj-XGH9EQHj1J9wR4sDA2CpskF6y3HfelgdwElXqXOqP1NQhrj6bUswmBNL6WN3dfBjdmz19RGVRd1QwDpsGxekpaho1ZX0E6tqt4hw4RdiquBb9H0SN95uRP0hF8akHRkkenPuyuTfO5tGOb45BQht39EhhNAL4anJ1Sq3GcnbP23LX1vnDhRDZqFqqRfpEoaez3Qh-kfXLtiSR6eDtF0hAM2G-p9Ri2TW0YdgWw3njENiwaQzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018847c7b0.mp4?token=MkvA7fZmT6vUnUIBA-ghHRQ-2Fs8F6yZxlRT98vJR5STqoLdmtALTLczMUEWPGqPMUNaol7q-XGPCVV-skSJnJM8hooacRlzEOrj-XGH9EQHj1J9wR4sDA2CpskF6y3HfelgdwElXqXOqP1NQhrj6bUswmBNL6WN3dfBjdmz19RGVRd1QwDpsGxekpaho1ZX0E6tqt4hw4RdiquBb9H0SN95uRP0hF8akHRkkenPuyuTfO5tGOb45BQht39EhhNAL4anJ1Sq3GcnbP23LX1vnDhRDZqFqqRfpEoaez3Qh-kfXLtiSR6eDtF0hAM2G-p9Ri2TW0YdgWw3njENiwaQzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
عشق‌وحال یامال و زیدی همچنان ادامه داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102681" target="_blank">📅 16:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102680">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmhAxLhU0z5G196wG4GSEPRI2rxIZUDufWIxB6RnLP0H4Wombqmb_2D5EAwUEqrGmaScH2t_xjB6VYCb82TqRNpXiTZ16UqR-4ox8K9ltgIU-OKdbWLvhbs2RgkTaquA9HrQegZ-s-0P6i1rXOqnioHTRSurQZFzxGoojmgyRTMKguivSLnPUB5tr4xBNFzq6RUsVZZ5X3DJ0fY-Q68oS8YMvTzlksIiHEHW_6b2N7NUWUe8j2XvyIs7tomcLF-bGH1AI5gNc3QEBpQ1a1uF3cm7n_JAAQ3xmOKiKKjORKeerpFb64j9Muhwr87Sqgs5nItAZmjq9dAhP3FKaqWkiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
🇪🇸
آمار جاودانه کریس‌رونالدو با رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102680" target="_blank">📅 16:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102679">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5903f6c3b.mp4?token=EXJwwX7dvhboKSAWNPMl2IFDk0lW06Q6jbXfn_ojuwU_M5jkZ1nzCGhgp4rxXYTCbjmXjzzQai237ajSY9isj5Rh1muXjJx5NEbczVdqmqVX-Ee0NZut7oDVugiDqepjgf0t9Mwujt2DdvdwDhhFtYQ1DuDVIE2R788TDNZ2XywP9YMPADeE7fkyZ-OyUBaYEaGfwNI9ZJGCumNydJc1QkB2TE5Rc-lmov9PMd_PVwgCDQVJYRj3JoaINCRof_oVlrmGViCQeZ5Hm3YJPfAFhSxZHEEjfqKNCuxz-q0n53wErq18zn3QEo6iiFadNfWu7Apo0Stmmvr5n4XKML9YDXsDMtcFpO4BgzwwQc2GrcOboNT5brjrIQ7KL46JVlW48wfQgHjEWxgjetvHxErKt0__BYoJ-xuvV8IKRV_ZpXPFc6EQXa3xcILzbMQreiF-t8fiDZSfdIUI6rnsvkJvMHqIyFaextqY3BghnpFoVhTPdU0L47vYNNv1wqEO8oE39kv4liFpfF2BTBe825NCiejcJsWCuIpnW4WvPDCnjJyzIMipGrJqLa0ObhcFkP3IXsTLmG0bUdhGc8IuC-IJ7BC1HKQT8VoWhmnQBwPHiay_-wSJkyUxgxWh0-O3ogiXRFPNPar9eAhRYqynFuVhBmWmpd6QwUhHFyqQm2m6_GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5903f6c3b.mp4?token=EXJwwX7dvhboKSAWNPMl2IFDk0lW06Q6jbXfn_ojuwU_M5jkZ1nzCGhgp4rxXYTCbjmXjzzQai237ajSY9isj5Rh1muXjJx5NEbczVdqmqVX-Ee0NZut7oDVugiDqepjgf0t9Mwujt2DdvdwDhhFtYQ1DuDVIE2R788TDNZ2XywP9YMPADeE7fkyZ-OyUBaYEaGfwNI9ZJGCumNydJc1QkB2TE5Rc-lmov9PMd_PVwgCDQVJYRj3JoaINCRof_oVlrmGViCQeZ5Hm3YJPfAFhSxZHEEjfqKNCuxz-q0n53wErq18zn3QEo6iiFadNfWu7Apo0Stmmvr5n4XKML9YDXsDMtcFpO4BgzwwQc2GrcOboNT5brjrIQ7KL46JVlW48wfQgHjEWxgjetvHxErKt0__BYoJ-xuvV8IKRV_ZpXPFc6EQXa3xcILzbMQreiF-t8fiDZSfdIUI6rnsvkJvMHqIyFaextqY3BghnpFoVhTPdU0L47vYNNv1wqEO8oE39kv4liFpfF2BTBe825NCiejcJsWCuIpnW4WvPDCnjJyzIMipGrJqLa0ObhcFkP3IXsTLmG0bUdhGc8IuC-IJ7BC1HKQT8VoWhmnQBwPHiay_-wSJkyUxgxWh0-O3ogiXRFPNPar9eAhRYqynFuVhBmWmpd6QwUhHFyqQm2m6_GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
هفت کارت قرمز عجیب دروازه‌بانان فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102679" target="_blank">📅 15:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102678">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_gAsO4fwokhWg73phhtb0Hzyxx1nimNG3gVv5-vG6_f7FEBJOugILEfGFY5GN2iDmNoUxyeFYYtaPFz03SB4_1P3qpwJHaDlvpqKcYTjmGQ-Zi_YT4iKZmCMpa_GLhQXqfSwylNjNcMDPPiNM6nrb3GpUUUZWI-k4TweGW7L2_ZUVhU3k7ZQrhTYmZi1EOgN114ml4Q6JjVLX6F6Jm0YRN9awcbO21b8a5PGJZqCTFamiaqgz7w2W3M4B1_qKCIhWv6eY-FQZy6TXP8T93z9Jr91PAuXACqmgbGEVi6Ntq2vDoMiAKSgbMRHC7cAvPD-zSechzfHZck4GdSCGlT6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
💥
عملکرد ۴ مهاجم برتر دهه‌اخیر اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102678" target="_blank">📅 15:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102677">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PodPkMOONQRiKN1ZULP-VEZMy2SFnTLRmoH7jjJrGDoW3ga2lDWDpm5TRWl1oIGA66BTyGG--RqIn9FTWMCyw7N1m6aCePdNCNDu6Bpscgf1gOSDbszP5iuZfRUgUH6gfUSNaDWncK7TBcxCy0lDjWeailgHwV50-1lwKIeZ8P7Fdlg4-OTYJp-roPwlPRd7FZ7ekZHyTEoeOE8py2Cg6vwfA9Y7e72AhInL7WN1Du4uMJojOkMAfC3tNAttsM9jNnu_HtJ4aeCnpMVr-PwuCTzfaxwpT3eu4ok4BykD8ejJrXRFvhmuBF02Xv8f-d1qopyva_LKLXwg4XbUmekQlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پاریس؟
🎙
فران تورس: خیلی خوبه که باشگاه هایی مثل پاریس بهت علاقه داشته باشن! هواداران بارسا باید احترام خودشونو به من نشون بدن تا بمونم، فقط باید بهم ثابت کنن که دوسم دارن و بیان باهام برای تمدید قرارداد مذاکره کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102677" target="_blank">📅 14:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102676">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b59000aa4.mp4?token=vwd_j7NI6bxEj5kynlSpV7GAjKlpYCoq1JXQo97c-tuaXFvEQpe-jxJkporhasONJNFyqihMAwZpvOI9ccYEvciFTqHj77xHirgtOYbpY1wgI0PYUAMQu0TIFguCnCh66e3QUCJOdRlUtX2LAgGTXAaPyAATEyIKAX2whZ5hgZo-pZzFzebhJmFY6egIS5XWkIX9hRku-BCykM3LuDhNZhqeCG2MxQ8-iGV7c5vqSnZR7Y2ZVt7PdInQQtqxqsS1epnmJZxDwhMYg4H6nMD5IMZeF29WJkrZHRRRV1mUVrdmCez4ERIKYUdDSB5sP29AmOdSBlZpYQ-qVkleDTqOig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b59000aa4.mp4?token=vwd_j7NI6bxEj5kynlSpV7GAjKlpYCoq1JXQo97c-tuaXFvEQpe-jxJkporhasONJNFyqihMAwZpvOI9ccYEvciFTqHj77xHirgtOYbpY1wgI0PYUAMQu0TIFguCnCh66e3QUCJOdRlUtX2LAgGTXAaPyAATEyIKAX2whZ5hgZo-pZzFzebhJmFY6egIS5XWkIX9hRku-BCykM3LuDhNZhqeCG2MxQ8-iGV7c5vqSnZR7Y2ZVt7PdInQQtqxqsS1epnmJZxDwhMYg4H6nMD5IMZeF29WJkrZHRRRV1mUVrdmCez4ERIKYUdDSB5sP29AmOdSBlZpYQ-qVkleDTqOig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
برخی از ریدمان‌های اساطیر‌فوتبال :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102676" target="_blank">📅 14:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102675">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsCq9nrrBZc7lB_j5-JFDT8toDoZu_ex3bjytn_I9VQ-YpL42TCxUhL2dWrSaZGR3QXJbv68jDWOJvCEnMvWLYsPokfY4KBRYINNChlSG1WruvIe-aI8J-trKvxo-636Y9UW0P0R8Mlr5WfoZkwIk0K_8Vp-StbxLzFidSNoYnd9QQeA-hx8uAPIkGGrwDZldjKl0gSTVO7EZ0KdVi8xIMv793vqTZ2ZWdLuj7mDuztRyR_rzv7--MgTnTjuIayZ-BAO2smm22CZYAJ4m1AXZGZg5khm0GDM02TJ30g1V6fAUbOjMr5IyBXuIHDP7OpCjxfSqetmVX1tAFrQiNVlNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اولین جلسه تمرینی ژابی آلونسو با تیم اصلی چلسی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102675" target="_blank">📅 14:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102674">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb25fb54e6.mp4?token=ajQoKc_cK5smMuIohkkDcFl74wpN_UfTERjGTr3ngZtNiFOTr0Nb-Om5_bwjJxQ10a8vBjyaNvQ4dDl6m8iHwJ2HqysVvOoee9U7g5zMxncL7El4jx_IQFAeXqvo6EcJ9iFi_GA8T1Cy8AMX6Hwxhj357BSRPAHHbCNzZUNudx1o1_OU5jox5BKqdoU3_Z6VewP5V7dk1_iK1xq-BDIvI8b9HziBHtmFq44sAgbzpD48hxLe_FoVsl6NNfyBx5AHDx-z0EGo0-xCAtZMiMdpmjB0X9mqd06JrXqNHTIJAc4cSx6vIDQD1RoMqg9mZ8mr6ZlZcCzV3Ye5rrwqgSVV4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb25fb54e6.mp4?token=ajQoKc_cK5smMuIohkkDcFl74wpN_UfTERjGTr3ngZtNiFOTr0Nb-Om5_bwjJxQ10a8vBjyaNvQ4dDl6m8iHwJ2HqysVvOoee9U7g5zMxncL7El4jx_IQFAeXqvo6EcJ9iFi_GA8T1Cy8AMX6Hwxhj357BSRPAHHbCNzZUNudx1o1_OU5jox5BKqdoU3_Z6VewP5V7dk1_iK1xq-BDIvI8b9HziBHtmFq44sAgbzpD48hxLe_FoVsl6NNfyBx5AHDx-z0EGo0-xCAtZMiMdpmjB0X9mqd06JrXqNHTIJAc4cSx6vIDQD1RoMqg9mZ8mr6ZlZcCzV3Ye5rrwqgSVV4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
مثلث آلبا، سوارز و مسی که بارسلونا رویایی فصل ۲۰۱۸/۲۰۱۹ رو رهبری می‌کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102674" target="_blank">📅 14:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102673">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uddSkdMqVbiVvHvKEFA2YBT3yqdXttXqOU4inZe0TFYpFy3Hs_et4i_Ti8IcV80RMTCM4lqr5_ayiA_ApwWRKC6OyVFFcymFCRv6Ctd1gpKfOQTzfq91GF_dvJHeEpObgpxnKhld-55DSL5LEJ-FYrNU7h-y0MbFgJnaWTsuA5HHjPHugPiTd0KthgrH4STTVCoi5MNIfMmjiC-2MDoR_0ErNxyDh0rKehZNlqJicgQla79PBv4mDJ7mqMIi2KdpoaZtJRlkpmD59s6bKqu52y2gbMmgQeQxmxdY1RNZqD3QH4jUpt3kcRA4cSvmQKMNbhmk740ZGunGRgwv8qKDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس سنگین ایکاردی به وندا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102673" target="_blank">📅 14:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102672">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
شهرک صنعتی شمس آباد انفجار رخ داد که عضو هیات مدیره شهرک اومد مصاحبه کرد و گفت یه مخزن ترکیده و چیز خاصی نیست نگران نباشید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102672" target="_blank">📅 13:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102671">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYneKf2wQNk7SU92LdR1uNwUFprIhxhB-vEHjivezSFNOWWgleCXKmnFzLC8ghjXz5ptvu9Ca5BFJ5aUmiJAgCnGg2avmmM24W2ia71VnJppefOgv06F0eMvn-sTGskRwuVBg8NRVugWVB1YzUYcyBtoQ1Mul_KqUBRY0HTTC57EXiDreToO_4Pcl57mVdorpBiWJr1yCjWOozOhqwy4yLm7AGwfwekRnC7hjAexl0jI4uTFt5kdoo3e1ftgdr2lStS-1pI9NxgoVcV0iiMkgriKsBFPTqO6MLMgB9c81fHPtdn9_Mqm5od4gYhe45Tq07vA4GewEctrNN75aO-DZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تو سبزوار یه مرد بخاطر اینکه زنش پیراهن امضا شده پرسپولیس رو به اشتباه شسته و امضای بازیکنان پرسپولیس پاک شده، درخواست طلاق داده و به زنش گفته که کل مهریه‌ت رو یکجا میدم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102671" target="_blank">📅 13:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102670">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627a83e0e2.mp4?token=rAvlGOb1ifLYVlnAMuIXqmkcKnZUZDW6ZGuaLePr9zS3FSHXXYpHYVLaKuKIaQJ68yA4KM_nz9BwHOnniyP5kobMPMoXInqaM8e4yGaGL6cDORiHYVoDyzDnUzuNE4yoqM_0tK3Mlu7qJneo9OnpY0LV-T1B6YdPvzaX9-xPCqhppitQz1x4COoIyc0mWTVeHTtJpTCQa_yyyj6HeHk1kfOGakrQ-lw9GN7cmQBVOhB6Cq5s6n-6nZkWhiIdImbZIafCH9IdGhPnUiJRM-30PUGtA50udmCx2jgFrmVnQJy8d08yBI3FPKqiCVRHIX97RLzQhHNW1rOuVODPXRU0_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627a83e0e2.mp4?token=rAvlGOb1ifLYVlnAMuIXqmkcKnZUZDW6ZGuaLePr9zS3FSHXXYpHYVLaKuKIaQJ68yA4KM_nz9BwHOnniyP5kobMPMoXInqaM8e4yGaGL6cDORiHYVoDyzDnUzuNE4yoqM_0tK3Mlu7qJneo9OnpY0LV-T1B6YdPvzaX9-xPCqhppitQz1x4COoIyc0mWTVeHTtJpTCQa_yyyj6HeHk1kfOGakrQ-lw9GN7cmQBVOhB6Cq5s6n-6nZkWhiIdImbZIafCH9IdGhPnUiJRM-30PUGtA50udmCx2jgFrmVnQJy8d08yBI3FPKqiCVRHIX97RLzQhHNW1rOuVODPXRU0_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
روایت‌ایووبی بازیکن سابق آرسنال از تقابل با مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102670" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102669">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0lnW2zh2935B3zBXcON8noJY6Fe7cw57oJn9Rk0gVBFagS_G8nbHKuw2K3aTAV5IWnmD4x6vsd1mfQ_mAIXKiJao2v6SiSy9t3c2BH4LyZ3GSq9YsIx-pbiMGGI5vv19bVv0p3IJY_NQ6KMKcNiSL7iwuheTFUTCffIhWPOde4qOyv_AIecVYz5SugwJ5CiPk4QHCDkwbWFl3begoeiYWMpeR-8DlWCrIdLca4wdiYb3FSXi33-9F15SgLT_tsBI3-cV4asnlCFGCAOT2teBKpLpLQ-rPJCCJYn2fpvjTzh92jO17nSqjIPny58neJvwVvYS543vq3legOjLsvSKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
متئو مورتو: باشگاه استون‌ویلا درحال مذاکره فشرده با اتلتیکومادرید برای جذب متئو روجری است و احتمالا تا ساعات‌آتی این معامله نهایی می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102669" target="_blank">📅 13:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102668">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e611ac196.mp4?token=je4TKnCHKyRcVC73VvkyiAtdHZvsa050wK6LqSXgJWux5qRnfTuY979xRPNzjboz2GhbDK6ORohgNRbBtpyqYeJGXP4_FqeKZfTCxKED201uYNKnRvNKtXBnjWx8sBQeYrrySSgCpoIheGMb4GD2_VIkY-Kr4m85ZlM5R7xPiU4snUG0-WjBysigFNv2GtpzlBMJoq9jqo0HNSyFjrxi78xt5lBjasmI2E9-gFN3JeSDZhufto30Qs11Xw9zJHeP7NmcDQDhV8xmbIMuctnwohjb5uO7q3Lp6lI3Y8x8AmQkBx--6EXjc0Tptpjbsoufkm1s24baiq_ZwUZGTYWQ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e611ac196.mp4?token=je4TKnCHKyRcVC73VvkyiAtdHZvsa050wK6LqSXgJWux5qRnfTuY979xRPNzjboz2GhbDK6ORohgNRbBtpyqYeJGXP4_FqeKZfTCxKED201uYNKnRvNKtXBnjWx8sBQeYrrySSgCpoIheGMb4GD2_VIkY-Kr4m85ZlM5R7xPiU4snUG0-WjBysigFNv2GtpzlBMJoq9jqo0HNSyFjrxi78xt5lBjasmI2E9-gFN3JeSDZhufto30Qs11Xw9zJHeP7NmcDQDhV8xmbIMuctnwohjb5uO7q3Lp6lI3Y8x8AmQkBx--6EXjc0Tptpjbsoufkm1s24baiq_ZwUZGTYWQ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
اوکراین دیروز کسخل شده و با پهپاد یه ساحل تو روسیه رو هدف گرفته که چنتا مردم عادی کشته و خیلیا مجروح شدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102668" target="_blank">📅 13:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102667">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937fee7ba7.mp4?token=L86nNkaTxxbkgnsxYpPZZuPY4BQ8hvOrbEoDPFaoDd6SfqessfKGAcl7bcSeqRD4YlH_wjgrp9kfbl8CbNr-bVKTV-C6lQFdNQBwBERyOC4MXRAX141T8mnaelfYBtwWqZKRSSghgFNcbY59HeUBQ4ZOvaJL4PoTr1vsJibDyhWI68Ra38E9_B6ecoAiYL8EInkY4XBUVpoutR4QlXhF-eFnCCZoSd7atNasmKTMDWaA7pvL4XRp6n5AhuOKsOpsN7mQ7ZTvM9Hw6QdDPUcqw-HRx2cSKR4WfSS266XvOjiiCJ-5PjdoBB2tgZILoaCIlqyz9jgfEIMYhrfm7PqoWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937fee7ba7.mp4?token=L86nNkaTxxbkgnsxYpPZZuPY4BQ8hvOrbEoDPFaoDd6SfqessfKGAcl7bcSeqRD4YlH_wjgrp9kfbl8CbNr-bVKTV-C6lQFdNQBwBERyOC4MXRAX141T8mnaelfYBtwWqZKRSSghgFNcbY59HeUBQ4ZOvaJL4PoTr1vsJibDyhWI68Ra38E9_B6ecoAiYL8EInkY4XBUVpoutR4QlXhF-eFnCCZoSd7atNasmKTMDWaA7pvL4XRp6n5AhuOKsOpsN7mQ7ZTvM9Hw6QdDPUcqw-HRx2cSKR4WfSS266XvOjiiCJ-5PjdoBB2tgZILoaCIlqyz9jgfEIMYhrfm7PqoWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❗️
دلیل اینکه چرا کورتوا یک‌دهه جزو برترین دروازه‌بان فوتبال اروپا قرار داره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102667" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102666">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=lauvV2FFJVHo2MTIth5cE0mBsD32ROsHo2wg1p4PPbZhK2KMbrI7ucU8M8cmy42hDJ6TUCNV6tjs830uTbbM9TAyxVHCbxSUGMqIEmf6mdpmN3cbLPkZMqgd5br-gS8UGd4BizJsJJlfM9CrEedLCQkptYxnILDTsJiHltB8me8j5DzSVQa9eno0aLoYej9A38SKOggMtMv5kNKdt1DeEgMf0tox0YV9cB-Lx5dA6RSP3CVwaWOxKIC72dHLQqggPRnZzA4ROxdtJyXPjWGfes3o900gB1pRURZRR_IcvID-5acpKw4eNzwed84rW1tCIl78GsMC9n4Y7aoFw8WA-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=lauvV2FFJVHo2MTIth5cE0mBsD32ROsHo2wg1p4PPbZhK2KMbrI7ucU8M8cmy42hDJ6TUCNV6tjs830uTbbM9TAyxVHCbxSUGMqIEmf6mdpmN3cbLPkZMqgd5br-gS8UGd4BizJsJJlfM9CrEedLCQkptYxnILDTsJiHltB8me8j5DzSVQa9eno0aLoYej9A38SKOggMtMv5kNKdt1DeEgMf0tox0YV9cB-Lx5dA6RSP3CVwaWOxKIC72dHLQqggPRnZzA4ROxdtJyXPjWGfes3o900gB1pRURZRR_IcvID-5acpKw4eNzwed84rW1tCIl78GsMC9n4Y7aoFw8WA-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇰🇷
هونگ میونگ-بو، سرمربی کره جنوبی در جام جهانی ۲۰۲۶ مجبور شد در برابر مجلس ملی کره حاضر شود!
‼️
او توسط نمایندگان مجلس درباره تک‌تک تصمیمات تاکتیکی‌اش بازخواست شد. از تعویض‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی، همه‌چیز زیر ذره‌بین پارلمان قرار گرفت.
هونگ در ابتدای جلسه از مردم کره عذرخواهی کرد و مسئولیت نتایج را برعهده گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102666" target="_blank">📅 12:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102665">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9e48b7ed.mp4?token=LiHI1698vRAuNF-RNJVRRIGueS_TRUfxbLrbfuRxklJOvAy8sVnyjn948gUPJqnSUEUrKi93pv0q4oKgTennv3mSEbv2GlLDORhR2Qp-rKKUeocQwzuU7ax0o41C2IwiaaNdCIe5yCnLC4WvpIFwnt96mNbXqcH8mjP88kb8pjvPqvi59jwl5_IzVeOTFYoXATV9RXkqRVu2pcpcFNxPEzHj-HIAyUiVJ1IIyqmDqQs__DWT4x2b-MpLQBqHVNRvaCYqQ5Mc_wK1v8S9zLb1x06ItKTu0qCOMdx1NcDyDYUyRfCsAnm0cC-SIdF62SjNp_w5S2KTyJiUINOEtRSAbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9e48b7ed.mp4?token=LiHI1698vRAuNF-RNJVRRIGueS_TRUfxbLrbfuRxklJOvAy8sVnyjn948gUPJqnSUEUrKi93pv0q4oKgTennv3mSEbv2GlLDORhR2Qp-rKKUeocQwzuU7ax0o41C2IwiaaNdCIe5yCnLC4WvpIFwnt96mNbXqcH8mjP88kb8pjvPqvi59jwl5_IzVeOTFYoXATV9RXkqRVu2pcpcFNxPEzHj-HIAyUiVJ1IIyqmDqQs__DWT4x2b-MpLQBqHVNRvaCYqQ5Mc_wK1v8S9zLb1x06ItKTu0qCOMdx1NcDyDYUyRfCsAnm0cC-SIdF62SjNp_w5S2KTyJiUINOEtRSAbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
گشت‌وگذار امباپه و اکسپوزیتو کف بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102665" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102664">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmcbSASf6ahmdruyUaRKsgcUXVL14JQ-qbN6Hj7Tkwxa5Djlrg8hK_rYPSCg20newivWtSf9qqPmPBqDY9zmJ0dznP0i9ZdnCx5v5mz8wAfAdO9wxhXaNmTPYVDe0XMfFF8oTNJdzEtv3anVxl3P7z2qjzfT4jVhnr75w8TuvN01Gif3EyW1Cv-W3hd-YG6e7s2nNLkW-uL9cQl-i_eAurDBPxuAjjm58761YqvPsUI5IDUd83-63yheed9slqaapdAu6EoALg2m3RdRY6BlITnsTlu1r7trD8gnDPYwIC6KdXx63Q6a0SKb6rXCLxBB2JV9nzuR_8t_Gml2XBBRzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🟡
فلوریان‌پلتنبرگ: بایرلورکوزن درحال مذاکره با الاتحاد برای جذب موسی‌دیابی است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102664" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102663">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnX9hYdJfHUcpFrxrmy1N4lU-9IgLf0-ea-s3OPI7fDCXBnVnrvBp15inhnBuWGK1sXbDjIqJwctk6cEHcDzeeB0tnBSLzR72qGqfUmjBCFVw6cTw5pqrSMAxRPwL5JIe2lWZWY5GKrH8JvHvR_EMEZP1qpivGko8Q0psYBVPQJa4SVf9VY36xF07UQw1TpvugZe-xOv6uWzJsljH8R8CLVs7MwVVro8S8Mz6AbstU3GQAgrP4xQzzMZBUUylwFB1JXMXg5f1vBusRnrxdhhZ9JmOyGv1LS0PBsrtAs0RZzJWpprrRS-uyta8s4xMvxHyN8GoLaig_CRToQBVRJPnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⚽️
فیفا با انتشار بیانیه‌ای خبر حمایت دونالد ترامپ از اینفانتینو را تکذیب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102663" target="_blank">📅 11:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102662">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbXjX9KmSLLxNgUrMt0ha5tXY0j9ORg298_EFKNRMlpos2iFdXCcYausWGNKGBcFC1vyBNBt0JmGyg9_fzif5nKOSgr_rUcuQzpm3qR_Gqekz0G5GAyxowEmD_YJED7xT2ao5VDnXB5NelSBcWAXfNTomXm90PG700PziUviuqdiUzdtJoqeS1kHzTbDq-4_BpWRueWhB-7vfYg7eroK-aVhWtkTSFKkSczroLZ_lWCT90iDRtIVO7eRi4yhfL4i8NO4NRRx6Cxh4uHPkV3PTvBO-JqQRiEUq7_hbRBvOlhjufs43tp9Vymk-D-N4kZN1GMi8fB_dNoW101Ox4GwIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
⚽️
#فوووووری
از مارکا: رودری دست رد به سینه سایر باشگاه‌ها زده و گفته که فقط به رئال‌مادرید میرم. قراره بزودی این معامله تکمیل بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102662" target="_blank">📅 11:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102661">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u5DjSSrdO-Nz6VOhVRAgYzAhiz8SktEqAuj3rKmJ9yCTAZK6nSNEItJzIdARcEMNKlZGXx4EedIsLWYd-l2Pf7eazxrEZbIl47mkXbLwIFokdxDRslrsfIaGYeclfquWLwrz8XSQbWZHBuXzarOLID4J9I6CKgxOFxXEiu6u2lesihOqWO90T65w8K-3gFGeLuglklLcGIIqJXz80clAYDzKldXga7Y3bhyLfcThZz4fUro1vNjlircbQrX5TsDISn8oOQnqned-XkCDgQECuSyA6SVgpJxISzyE-ca-j5CegfxdDI7fD_XAMMJ30l7GJiSeJltgVu_Hz1Wc62JT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#رسمیییییی
؛ نی‌لاند دروازه‌بان تیم‌ملی نروژ با عقد قراردادی به لایپزیگ آلمان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102661" target="_blank">📅 11:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102660">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
‼️
😆
😆
🎙
ساکت الهامی: 55 میلیون تومان دادم کت شلوار آنچلوتی را خریدم تهش ۶ تا از استقلال خوردیم و باختم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102660" target="_blank">📅 11:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102659">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFozIT92OyDsZvmGbDL6pdiRZoA0ORcwwVnuT-E_Tamg5bB3WD1qhUxtOwlfyMRAZIgrd3dX6-JIqjfX_517SHXTO7yk56WJ0jV-Mgwm9KrBd6QP6L_cPx9nzYPZuz3qDOX0v5Y332uuuWrGaOgCM6Vb2Ge24Hi45HR6zCRJnhCtZ5XJixGhMRCPkwF1cH-Q5quLO0y-iyBUMhOL4lGeHFUntjgMVmdM3iHxG04mPrPx2jvG5r0sqolgHHcrLhR7xyzhZvQ8yLmlPBFig6-CQrolCMS7Ik6JQi3qf7mUgW9efq_bjXQKZEEIQXUs0YomKd69u052UH7n1Q6QTVMUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژاکس آمستردام از جذب مارک آندره تراشتگن به صورت قرضی تا پایان فصل از بارسلونا خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102659" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102658">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf1a57969.mp4?token=eg84m10_wD9NHsYz0BnWq-_uJhn-RbuWcj3FukbrlI7s3lqwVaZ3O3ELyD0IVUUFE8lT1xqtGJBI3X3l_wtjTnVAi9yO6Dq-C2F23TrCHJx-cO8-uTmZ5sCB-kNmdKKAGvb5QAxVvqWsSYmGNd3kApE_l1YI46jEukRBJsD6OcofLkekHRhLVbR86BHUJ7UowkpLw5mXIBkEdu8Q8Q7BIr0fsZPK-gAxa4wXxBGRmVj7uhQpo_lm9s92u7egMXRSB1YaqljY7DRc-w62pYKGGiEzZIvn0ljRu9MdSyAkF494APrll7cNrlpTlsgI1wA6bA2c8ZbNjhBDLtI3u0uCPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf1a57969.mp4?token=eg84m10_wD9NHsYz0BnWq-_uJhn-RbuWcj3FukbrlI7s3lqwVaZ3O3ELyD0IVUUFE8lT1xqtGJBI3X3l_wtjTnVAi9yO6Dq-C2F23TrCHJx-cO8-uTmZ5sCB-kNmdKKAGvb5QAxVvqWsSYmGNd3kApE_l1YI46jEukRBJsD6OcofLkekHRhLVbR86BHUJ7UowkpLw5mXIBkEdu8Q8Q7BIr0fsZPK-gAxa4wXxBGRmVj7uhQpo_lm9s92u7egMXRSB1YaqljY7DRc-w62pYKGGiEzZIvn0ljRu9MdSyAkF494APrll7cNrlpTlsgI1wA6bA2c8ZbNjhBDLtI3u0uCPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
پدر تشریفات ایران آداب استفاده از آسانسور و پله برقی رو بهمون یاد میده که بنظر هیچوقت نمیتونیم رعایت کنیم
😂
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102658" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102657">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a0e4679b6.mp4?token=EI_6HTaKTj012GwVCeMwVP0Eh0ojgqsiat9sT1CxRvyCwiy6va_h-7Ssu4W7hKddRIU8sTwQNufDvIdCSa8ZvhFmiWpgPrm5epcejSqcHUIfIAicJn_5YlwXcEj37w0tvusXVW48ReQZ8UjEiAalmFfV1wrieOhnlV6wVshrWitxkiSjmKoPN9MEIArCzITmEVywIpQQoSq47yHJ6PhK5tOLh5VbmYGqbhCLBQATV3XqReOmTQb-UVVPvND-0tbL_Evhp56i9U1fRMDhMjl4MZLycKesr9I40zM9pjbnYIotnWZnPkGx3Lyaay74x_gotu1diJZjcDt6muQxyP6MBw9qmXwjSRVpUJXVv40zYBuVjP44Qd6yvvKl2CwUnNyj9BXNRe-PPwkno4wNSzbfxaj7i4r-zeckPUErc8M8jwXP0K0-_SbksE7mnXnJLqop98EJBeXmDWaSrIgUENr18wAXc0IOXhTp0QMigyBNVlECc3VODmB6oPfYZWpEKyxgYFKZmfqOV5WKNTdlF2FZ8ngsU7iZfTC1DirpnNmw2cY2oOaW2c3BaS7r98LPTXa_GEWxMTAZCYjz3nJFVN-5D2LTDNENKfD54eIJQfS5nT8fYpRVcTr8m2KsCZUv9kF83lCM5W0TRYurfO4-HydFWeOFnWjSKYJVcrkD1bvgcq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a0e4679b6.mp4?token=EI_6HTaKTj012GwVCeMwVP0Eh0ojgqsiat9sT1CxRvyCwiy6va_h-7Ssu4W7hKddRIU8sTwQNufDvIdCSa8ZvhFmiWpgPrm5epcejSqcHUIfIAicJn_5YlwXcEj37w0tvusXVW48ReQZ8UjEiAalmFfV1wrieOhnlV6wVshrWitxkiSjmKoPN9MEIArCzITmEVywIpQQoSq47yHJ6PhK5tOLh5VbmYGqbhCLBQATV3XqReOmTQb-UVVPvND-0tbL_Evhp56i9U1fRMDhMjl4MZLycKesr9I40zM9pjbnYIotnWZnPkGx3Lyaay74x_gotu1diJZjcDt6muQxyP6MBw9qmXwjSRVpUJXVv40zYBuVjP44Qd6yvvKl2CwUnNyj9BXNRe-PPwkno4wNSzbfxaj7i4r-zeckPUErc8M8jwXP0K0-_SbksE7mnXnJLqop98EJBeXmDWaSrIgUENr18wAXc0IOXhTp0QMigyBNVlECc3VODmB6oPfYZWpEKyxgYFKZmfqOV5WKNTdlF2FZ8ngsU7iZfTC1DirpnNmw2cY2oOaW2c3BaS7r98LPTXa_GEWxMTAZCYjz3nJFVN-5D2LTDNENKfD54eIJQfS5nT8fYpRVcTr8m2KsCZUv9kF83lCM5W0TRYurfO4-HydFWeOFnWjSKYJVcrkD1bvgcq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
▶️
آخرین فصل‌ لیونل‌مسی در بارسلونا
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102657" target="_blank">📅 10:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102656">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برترین گل‌های محمد صلاح در تاریخ لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102656" target="_blank">📅 10:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102655">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxdzH3v2AIhcrCN2ascbZFnTuzf_z-7UrZ3iAIuyZcOqMzLN8FXHHS1L4N7kHgxrl4HhEtcehfNJzi4E_moWr_nvVUmI1JIkptM70OIiF1YJW4S5f9-lhQIbe_PTfoS2kdgHsVZktloSXUhgTaF7T1cjN2DODN1aQipKeqaG0oO5S2HKoi-qEuOXpEYorrJty9d8u6e3BumLLpLWS_15jMBzceJBrM__-mpNZviz5mTUN-gAVhoHG-yE3roxcLsbMusQYYwQCgWdZUEB6q1iPuI3aNXFyOQRn9lIj6LAh5XbdyIt2AreMs6H4qdUh_LhFidfKT542GVUSjgMLzs1cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
مدیرورزشی لایپزیگ: دیومانده به محض بهبود بیماری خود به اردوی تیم در اتریش ملحق میشه. دیومانده بازیکن تیم ماست و به قراردادش پایبنده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102655" target="_blank">📅 10:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102654">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👀
🇪🇸
🇪🇸
یادی‌کنیم از بازی دو سال قبل و پیش‌فصل الکلاسیکو که حسابی جنجالی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102654" target="_blank">📅 09:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102653">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
‼️
😔
🇮🇷
پرزیدنت مسعود پزشکیان در واکنش به جنجال‌های ۲۴ ساعت اخیر: استعفا نخواهم داد و خواهم ایستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102653" target="_blank">📅 09:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102652">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f47080196.mp4?token=PEq_WUwA4BPJ2V9nUbIncu6v3FdGJb76KEXgyumLjEq5q8E5D-Goz8hvCARGqTbZspBz3cqDydmJHrOrjXKc8bRUDamP9VldgvliNCyQIuefTCj5apNo1Mlc9zDmrReQfC1u_rKiR57LqcvJaA-i3fL5DdzHs9HpUJMLRIznfNnGHSUN9KZ7XnKpECw-hsgwci_rTlqW83rVQFPgP7gWb7r4y6Jf6Has2sudB7OYURNvU7uHd95rbNH3dryzenYE7K2bYB6sQmK6kZ0riVDUIf-nlCyFuEA1-ikAWbMDNWy2Vgem9WQJohMr41vLksn8UusjMqgbMLoAKaFXgCe7rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f47080196.mp4?token=PEq_WUwA4BPJ2V9nUbIncu6v3FdGJb76KEXgyumLjEq5q8E5D-Goz8hvCARGqTbZspBz3cqDydmJHrOrjXKc8bRUDamP9VldgvliNCyQIuefTCj5apNo1Mlc9zDmrReQfC1u_rKiR57LqcvJaA-i3fL5DdzHs9HpUJMLRIznfNnGHSUN9KZ7XnKpECw-hsgwci_rTlqW83rVQFPgP7gWb7r4y6Jf6Has2sudB7OYURNvU7uHd95rbNH3dryzenYE7K2bYB6sQmK6kZ0riVDUIf-nlCyFuEA1-ikAWbMDNWy2Vgem9WQJohMr41vLksn8UusjMqgbMLoAKaFXgCe7rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
روایت دیوید بکهام از میراث فرگوسن در یونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102652" target="_blank">📅 09:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102651">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5Edg6He4eU0mPjQnbCSQME3Id8RrgvgHxnxqkxXfONGzz0Mzra7fVKo6L0UY035ES9Fp8ldxYCysknKL0nexwKrDRGXHboTkud3Vn7q5M6plGUAYdt5zuXC8RmPltjbFZJRbvnvoKAliHw3VlfVhzOCJ7JcmDBy0gcNCjgzV6jXvcHDGzxly2qROP0JcLhPM5A_l00KumblD9wzono1mnyBpCtnQDyQRVNdGIxn7dex9t-Ma58NZCAlrWgR_9qjwsPYikNjOw6XyxP-KrPHOvYEBFMYXqXwuOuzWGwyWmxFv7husoPgEII6x3Fm-YtnEo_pK1-cR5puSxidVDablA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
کشور عربستان سعودی در حال ساخت بزرگترین شهر ورزشی جهان با بودجه ۱۰ میلیارد دلار است.
🤯
این پول معادل هزینه خرید ۸ بمب افکن B2 یا ساخت ۱۰ تا برج خلیفه ست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102651" target="_blank">📅 09:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102650">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWmpAXSCvERwqSdV9vXb7G2zKyhm4BUkhWxxmO_F35UU-xJAQRLBYWXh1IR0PAX16WltgD-sZkASjNX5ONxWg7gg35v7IW4xDnTN3xv3RuVfX_RBX2SgLeJgiO-sNlNjb5diAdJuujxofn1B4LlTvnknsrQ5lO_VLfdrEEkJGSYDZZ-XtQjdFOJRcGdJW1N54wuaa8JBoouBHZagRq3tu8SuSa-nWoZw6ORZ6ecWMzu8LfFwbqW9frcHOjh4XdJjW6SX8NUfatvpj3AQhaJzbrZ6AyTt9M8ZoHXPq0ETRH1Ll78Y33bz7eQxgIuJOvRSbAi_dRrCF1B6Pi2J5YWWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از نشریه سان‌انگلیس: باشگاه استون‌ویلا بدنبال جذب مارک‌برنال ستاره بارسلونا است و قصد دارد رقم ۳۰ میلیون یورو برای جذب این ستاره جوان پرداخت کند. هرچند که بارسایی‌ها این بازیکن را غیرقابل‌فروش اعلام کرده‌اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/102650" target="_blank">📅 02:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102649">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d8f16631.mp4?token=meg7Z9s2EEkVLVxvB3EMWMEwt_n_xxO3MXHrenk9bIH5LDVgxV8exAF1rLA_zoOSQZ0w23mLjq9g4zRwxN3E2twlez3_76af9WJr1jNYx1bXBIP-RmpsoAUvTomujQf79gtZ8JComno2Fx3yYwxrHKEC-Lr6OHE3DLGAWLE1JXbaMw1F979PwGTktEzgXnxGMtLK3pIW6nXcprai1rkdz-KQFbKb6gzXt_-4DciCM7WD6JGJBIZ4YEzp_YetrqRq1NNZyufX9PD3deTF9wVL1zgeMBSU0-KyefgtPlW9jYXMpYGqmj0yR8MeTCE50nOsNUbGAIx5s4DEHX_goNNH3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d8f16631.mp4?token=meg7Z9s2EEkVLVxvB3EMWMEwt_n_xxO3MXHrenk9bIH5LDVgxV8exAF1rLA_zoOSQZ0w23mLjq9g4zRwxN3E2twlez3_76af9WJr1jNYx1bXBIP-RmpsoAUvTomujQf79gtZ8JComno2Fx3yYwxrHKEC-Lr6OHE3DLGAWLE1JXbaMw1F979PwGTktEzgXnxGMtLK3pIW6nXcprai1rkdz-KQFbKb6gzXt_-4DciCM7WD6JGJBIZ4YEzp_YetrqRq1NNZyufX9PD3deTF9wVL1zgeMBSU0-KyefgtPlW9jYXMpYGqmj0yR8MeTCE50nOsNUbGAIx5s4DEHX_goNNH3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا سپاه به پایگاه آمریکا در کویت حمله کرده و آتش‌سوزی رخ داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/102649" target="_blank">📅 02:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102648">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🇪🇸
#فوووووری از ESPN: رئال‌مادرید پیشنهاد دستمزد ۲۲ میلیون یورویی در سال به وینیسیوس ارائه کرده و قصد افزایش این رقم را ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/102648" target="_blank">📅 02:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102647">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3ukQ--BLMCXTWpQdmau1iLL1mJFO2WBg3KCqgt-0O6m8Ow3ffQE889t-5-iqA4EinZ9CiAifVzGaT_7Y77LTtxe6DmulX0n8ruo198pT-wNzmbi6kraDhHRHNdI7Q58vKOt6PZcCnXLl0Pzr0erkQUTdSOQuEntZ3BfCeNnnnIeQSoCe4xAZFVW50AnRSpSi1k5dcP4f3ee0hSdpND73dIWAcJCIeZjOoP63e7JwTPx-Z5fz4UsIQABRAWp-8qSkVDhyoRk8CzoqdxNp-Eiwpq3EJvuBOxc7n7_18x-GuaEzTtMSUDPDTUHf2-jxlj0MqulrJGlUhc76wiRtFp6MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از ESPN: رئال‌مادرید پیشنهاد دستمزد ۲۲ میلیون یورویی در سال به وینیسیوس ارائه کرده و قصد افزایش این رقم را ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/102647" target="_blank">📅 02:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102646">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZHTPHeHIYc7ndoCihV6h73PpKtuvJ9U3ChwTIXYXlcb1uqJMegaGjOKlGbMJijERhP2AtJgRuC7YNuUEzWaXLlv9VDzGo1cYpQgNfAZWaycaVTfbUJL67xT5fCNpSmGAHvwkV-AhiTplPjrMJVDcn_ewQ0XJt0VGo0ctC64b40dWthTXXTRp_na0Sr0VGgpx5pkz0bkowexXL-PtuN4Lk_rnB001y3SaojfcRZubkZJucJnOJQryIgUcLPww7oalxhmx5cvzYTXHp40Ja5AayaNeCreC0h_XSYhcNaQcGKA8J2SzMyjS-lb7TvslOWxnqcPirh08fFZeMC4niNi5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
بن جیکوبز:
چفرین و ناصر الخلیفی در سالزبورگ دیدار میکنن تا درباره تحریم جام باشگاه‌های جهان در صورتی که اینفانتینو همچنان رئیس فیفا بمونه تصمیم بگیرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/102646" target="_blank">📅 00:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102645">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLVuidIFT4_AK1brlkujuHNc7KeL_oo1Ulh_w6bjghKXz5PypwVGfVqoyOczSFflQucFu-E-JkGeATgxQUqtVqWR3j3qeT8BGa70pLwrrtDSNw1xCPPym8lUyMu2cPiGIZZxqhFUnK4SKv8LWFYSUqiHyzXTDaCq-vvKbLrLdVhzFTi8pJuXSxelA_NpQsJKpB_PPLcCYtYqa4mDdY6xPSX75cTLxturaevw0b5m2iqmjfNjBf4MIlB98eZ-aFarH-yRYcS9fy7mK8QoMvKtbr-irlTpgUg-UczSMnnRFJSwOjGR2qacwCZeevT3tQA2TaG95sFokQAFs0oQ8L6jUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پاریس؟
🎙
فران تورس:
خیلی خوبه که باشگاه هایی مثل پاریس بهت علاقه داشته باشن! هواداران بارسا باید احترام خودشونو به من نشون بدن تا بمونم، فقط باید بهم ثابت کنن که دوسم دارن و بیان باهام برای تمدید قرارداد مذاکره کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102645" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102644">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی #فووووووری
❌
با تایید تار تار و اعلام رسمی ایجنت بازیکن قرارداد نهایی شد
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102644" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102643">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vPEjb9UvcZuo26o16TrZ3q00py0lLRKxjNIWkyM7VJNcd1S2ea3LNSO1otgB4ffWfXzdea9x4G8e8WryJf8VLe_lFOOXRdwMgjDyfNeuy_GX162NNWq2D-XMIRZBsdsbHnQM8oSgU8qsYRi-3SBsSMwSRmamjVOUB34DkWkiwBrqr6VS6B9hGMeIKx_mA3bxMsqXOXEa2_ubkWt64G-jK8aYsVkG31qIcrmirtLJvHsmlhOcjgS9skG-aI2K7A4hRTpmuZYy_wdKXVtClaTY1TF8tNs9sOlRLPm1mgNFpd5PvOLM7nfoFSN6O0IA5etyM5NWGrT_SXrNtHLdTd8M5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
🔴
تارتار تایید داد؛ پرسپولیس بار دیگر خواهان جذب</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102643" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102642">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqYuHjqYB6-grNmAgBSHw3H8H0b-BRGl7ZwUsCQONoiF2yD55OaE5yA3zbYD7Cbq-vbgTc7NdMXJ774HyEzqj90z0tO8dYdRnbml7wlS2uKFSukv_kpIXUAQW16ITO0YZ7iwjw5Ac7dbUcwnvQc4-aQzsPgXIDpjPXJdjJOcmGwcdl6dvJMA07XP094rFWkedvVOfl9jCfuJV9zfcGou9ZfAxZQ6KFWq2125OWbM8dQ7PASI0eE_6-EaoyCGAFyDl0PiEpXDExkj6OJNCLkeHTUkGwxQwNCJaalr4rwHCloLOsdF3toJIWXP_75xsuktBcD-bjnfml6tyK5K9L9qkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
برناردو سیلوا:
بی صبرانه منتظر کار کردن با مورینیو هستم، اون کسیه که برای فوتبال پرتغال خیلی مهمه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102642" target="_blank">📅 00:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102641">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b215f0831.mp4?token=B662M2v-J5MzdPMpPF7rnvMhfMpg9nHkA76VEDBvJi63RbUQN70SSkrzKcT1bogdzKVmblOUL2oxgNkQfk8eMfoyJv3jOqiyW66Z_0RH9lR4DGLP3dJcZ1b_Y4zAGfyQjMeqZyLmCvDdoplbalnL1V0UrgaGhl5Ru2dBXqauGaxedS_q4NWBM_Fd8132T3jmxwTD2sj56cmwMpHbQn6V9UjQcGo5m3Xf3oc8yQtdB2OjwNLbOmru5UdezAoNivEIjySZ6zhd5DFfvLCMHuHv65h5ZNicPNRzyyQdiHd9cu0FCLFrAstQsA1S9a_FrvxIwqUnqJPaQ5uemVUBGsipCmSudQ7Pq7h0bOUERLkAnA8m6F4wLiH3yudrc3rdZI0tdCHvXoPngLNkPPL74UHp_okCFNMcQtHwA1r146S8kWyEL_rqmJMJlZ1clMTJm2QL_FS43eaV7CgAOZSTy1D1u9ZGeoC7_ZS8_vpF81cu1de4z2_JkNigNfYTt5hOrrFGQm7ceq_n1WNjeCPHOD72ViIOQqTQaKo85Sli_MrvXTzXu3kpVz3DX_BOtbwjhHtjefoPBu1UYXHTGqE7BUXdsJfa5UpX5gNzEKgqf-0QNm8PmyJkau36FOCLCXpDdn1k6Cygq8WxZIwo6mGUEsQub0lNdLpVyvwF_VPkuJoa4kI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b215f0831.mp4?token=B662M2v-J5MzdPMpPF7rnvMhfMpg9nHkA76VEDBvJi63RbUQN70SSkrzKcT1bogdzKVmblOUL2oxgNkQfk8eMfoyJv3jOqiyW66Z_0RH9lR4DGLP3dJcZ1b_Y4zAGfyQjMeqZyLmCvDdoplbalnL1V0UrgaGhl5Ru2dBXqauGaxedS_q4NWBM_Fd8132T3jmxwTD2sj56cmwMpHbQn6V9UjQcGo5m3Xf3oc8yQtdB2OjwNLbOmru5UdezAoNivEIjySZ6zhd5DFfvLCMHuHv65h5ZNicPNRzyyQdiHd9cu0FCLFrAstQsA1S9a_FrvxIwqUnqJPaQ5uemVUBGsipCmSudQ7Pq7h0bOUERLkAnA8m6F4wLiH3yudrc3rdZI0tdCHvXoPngLNkPPL74UHp_okCFNMcQtHwA1r146S8kWyEL_rqmJMJlZ1clMTJm2QL_FS43eaV7CgAOZSTy1D1u9ZGeoC7_ZS8_vpF81cu1de4z2_JkNigNfYTt5hOrrFGQm7ceq_n1WNjeCPHOD72ViIOQqTQaKo85Sli_MrvXTzXu3kpVz3DX_BOtbwjhHtjefoPBu1UYXHTGqE7BUXdsJfa5UpX5gNzEKgqf-0QNm8PmyJkau36FOCLCXpDdn1k6Cygq8WxZIwo6mGUEsQub0lNdLpVyvwF_VPkuJoa4kI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
برخی از بهترین گل‌های کاشته تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102641" target="_blank">📅 23:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102640">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290de4f011.mp4?token=E86Fuhy4yDoYI4LSJLYcpXgV0b1ExYE8EGmHNDcFQsL8u30tQBhm8S3M9Imtl8NJm5J6Q1JXFg5V4W05T9IULtk3hmGLLCqZAhp9-BVxiiWfK3iX0vz-66vE7xdDG9hvKuYLHKtkpupUlCFaFcUvme1h1bt9cEWnMraixdf95RWJTpgeGnmdeM0rignCDgXuE5H-AQ_6J-3TSQMPm5ES06k8qCqnzB8yhmqfSFzxGPgmAQEv9KPtX-MKWdkW1918tKq2ewYwo9wXjIA6sZp2A3ZQ4XtYaPdBKgVVtbZ_1gEGGd6OM5z9vOQBixvqlLEDk8VPrxNxvZicz1keKxv-2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290de4f011.mp4?token=E86Fuhy4yDoYI4LSJLYcpXgV0b1ExYE8EGmHNDcFQsL8u30tQBhm8S3M9Imtl8NJm5J6Q1JXFg5V4W05T9IULtk3hmGLLCqZAhp9-BVxiiWfK3iX0vz-66vE7xdDG9hvKuYLHKtkpupUlCFaFcUvme1h1bt9cEWnMraixdf95RWJTpgeGnmdeM0rignCDgXuE5H-AQ_6J-3TSQMPm5ES06k8qCqnzB8yhmqfSFzxGPgmAQEv9KPtX-MKWdkW1918tKq2ewYwo9wXjIA6sZp2A3ZQ4XtYaPdBKgVVtbZ_1gEGGd6OM5z9vOQBixvqlLEDk8VPrxNxvZicz1keKxv-2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮‍💨
چرا بزرگ شدیم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102640" target="_blank">📅 23:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102639">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbMgyrQaPkzT8GavSn1BtShad_yowTS5VGA5uJ1ucO5pV25ODlyWeNVOGkQT1ibR7Ku1ub5NbGkajcmy-jGU0T2e5Aww08O3nlFp0k6F5VgXeg2xsUOiqRmSZD-OTGwO1WV-kW2tvFYGft8mPeoMFl_fa5yUjnCSl34kKrJYMCPyxEcry8dvyaovNU77asAOzqhYlgQepAyfwpolyNF4Gr5HyYprTDtCGvShfC8gQ6_8nVe9D80hpoOptb3R54BkxLivfpN2XfWJpHHJb-Ychc2L_qiD2bNE_WTBjXBx9mP2jmM3oDwlOaLTfsVntEUb1CTcHvHTbSLQ5-JNFRmGcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برناردو سیلوا : رئال مادرید بهترین باشگاه تاریخ فوتباله، نه گفتن به پیشنهاد این تیم غیرممکن بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102639" target="_blank">📅 22:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102638">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدنیاکالا- کفش ویتنام و اروپا در بانه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMKxDAe5_VaniwsjRd9e1veOXTL60AM-T9q6hG38QZgt9b2nD3NtHpgPTRL9I5drVyBwn5Dzbbszv8Ru5Q3Bw1k9p_DO0i-xuDNI-CdDRuJr5HTWjKNuWM8cFwv1Jm3RyA9lzp0z1EHlExm7i3tKVA7UAeRlHX3XsxIF0MbPxZD-tkaxnxqG545W398xk1hX4XCG3L0JHwkxQghNMO5LkKCxD1OJF1R_jSv_VkeHUSin_0kzdnzkPMOiYVZAQaBIs9If9GxljRxDa0BnaL7ITygsCJN7nVRNCr6syQJqnyqtEZ2Eu-BWdT3fPjQbc2mNz8JQxbs0lxARH_68dwXpKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102638" target="_blank">📅 22:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102637">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac45ed94d.mp4?token=fGBr5NUzC-fELSPFKJ0M3sYJalThpag2bfRqZSm3PyBHfs9MHSMPRyFlJhLdnfkKXlU1FX1Hvw3fA49HSXy6mCa2EaPoeJSy47xHgFimXoBJv-Um9qkUATM2WuQptnJZ1aYkwRkxTuUp02b5SjhY60ogupO-aG5Ayglwa1pbJeZDse6q9xrrW9qA_A756LDeScoOAz3JSeq6DFyXtrj1oGE5DqfInnu_hK966vF7Np-N4O-H36TUigETwP66Dmcti_0_uFFkpXhTo27BHZ7W9jpUe7wxemhqZuFLuVIL_ft3XUmXDgi5SLKt_7v-llqlzS6a7l641X1H_C19dB5mtwbHnwNGFrJPz0hEUr5CFcww9ckrC3lw7_rUWg4eIV91Wx2cfk92zpBuvnL22uQhkUBw4Lc9ae0iuFP8bkMh9NF46dxDAk35pEUAQ6btOQoxVh-kfo9KNZ8jDj5Cr7op_3G4qgyDcMrUhCZEkyd5E4W3CfoJCril8PfdDPFl7vm1rsHcum0w7douMYR8Qr9CSNPnMwGQJzuDwToHUWuz1ZA5GtKvHoSZHT-pg_GamFSmCgb0tm72MJn7L3bnWQqV1w8Jno_LQbY7Hz1IbTZCzGl_saZlvD9RkelHDeISbNkgkIEiZ3E2gyNHGaLYj6bSHhkONAJclr76Zo6b79gQqOs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac45ed94d.mp4?token=fGBr5NUzC-fELSPFKJ0M3sYJalThpag2bfRqZSm3PyBHfs9MHSMPRyFlJhLdnfkKXlU1FX1Hvw3fA49HSXy6mCa2EaPoeJSy47xHgFimXoBJv-Um9qkUATM2WuQptnJZ1aYkwRkxTuUp02b5SjhY60ogupO-aG5Ayglwa1pbJeZDse6q9xrrW9qA_A756LDeScoOAz3JSeq6DFyXtrj1oGE5DqfInnu_hK966vF7Np-N4O-H36TUigETwP66Dmcti_0_uFFkpXhTo27BHZ7W9jpUe7wxemhqZuFLuVIL_ft3XUmXDgi5SLKt_7v-llqlzS6a7l641X1H_C19dB5mtwbHnwNGFrJPz0hEUr5CFcww9ckrC3lw7_rUWg4eIV91Wx2cfk92zpBuvnL22uQhkUBw4Lc9ae0iuFP8bkMh9NF46dxDAk35pEUAQ6btOQoxVh-kfo9KNZ8jDj5Cr7op_3G4qgyDcMrUhCZEkyd5E4W3CfoJCril8PfdDPFl7vm1rsHcum0w7douMYR8Qr9CSNPnMwGQJzuDwToHUWuz1ZA5GtKvHoSZHT-pg_GamFSmCgb0tm72MJn7L3bnWQqV1w8Jno_LQbY7Hz1IbTZCzGl_saZlvD9RkelHDeISbNkgkIEiZ3E2gyNHGaLYj6bSHhkONAJclr76Zo6b79gQqOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
دوران پرایم‌اسطوره مانوئل نویر در بایرن‌مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102637" target="_blank">📅 22:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102635">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HcpZX34bV6IbC4O0BsnRQlBTC35GZQEKWdqeV9v4vxOSUjqiK1ywxLA8pIzQh2s8rG7Xc-P8wa4NdcpuyjhQshdC3I7-2HU-oldTY9e9IKTmGYqo6gQUoM33Za4RiRb7kLLYjF7uqCLiAElekUJBsI6dHVSIaWHPKXUBcGt50YJDMBrKCezORxrHAcqQffH9XzdIyFx5FG1u6P1bhigSmXshzujQdbiFldtPm1fi3v2GLbsmmPYcEv9oswCL9oN_3arqqSkFtn_ysvjlI9AcxD34L_S8fEe7S9BVCzqY3xJhJVG_5p8yDIPXYMEkumNtSZ7lrubvReQvSBPaOGc2UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0fK7GS7h2g0YwYwRr2cGpiYr3D6ssPl7GtklIxJPT73rnacyWtjs3BnYcOWFMSe03jmfZNoSxVZvxGDUxZPpgmVKmsvrGDsWKxnzwJqkquWAwZBYgDs2B2BkgAlhgZlxJlGKZxCPfTNrZrnBtce_I7QAbgfiR0IekSEbjDLZbo9pElD5A5ONA5135QS2d3nX7rIsLgR-MWxIqWfA1eVC5-1zhgCLfXvmvEEGUs8QZypYhNqh4GWHwAKLZvvvdqxVmfkRQKimMykguKl3ALkMlTWxV-elxrd7LeY7YHF06JlMiIQJHVnLBef1-aVu4OnRKLU58RGcYM5n3SDQ8Q9bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وندا چقدر چاق شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102635" target="_blank">📅 21:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102634">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cbde7fbeb.mp4?token=l4Hfvexy9xZy_XRyMIhgn2ByZHrJsykaIoVxPqwUNAPFaaxklTz98o2UAY_Mxl9XaNsG2b0MTuRIqQ0DjFgKioqrNseoYptN8I-uFFmZwS520mM-IqZ61bvw_z2lDTtd7p61PvCAeJIgIQAUPF_VuUAOd_kJJmc4G2RNqSAHn2NJoByzJ-0XvDBiGO5Fy6UVzMREKhJqUjSV428kdDjnx2vol9tNDrKrUzi_oahrjxtXxU-ntlvx1jA_VRNecn6sItCNShxVKLvsMurNyVwoGA42JLC3tUeoXRe-nw-oX5apM1YoamnW6QMnTHE_Tx80SRNlJl3xDfX8ULVxiY15Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cbde7fbeb.mp4?token=l4Hfvexy9xZy_XRyMIhgn2ByZHrJsykaIoVxPqwUNAPFaaxklTz98o2UAY_Mxl9XaNsG2b0MTuRIqQ0DjFgKioqrNseoYptN8I-uFFmZwS520mM-IqZ61bvw_z2lDTtd7p61PvCAeJIgIQAUPF_VuUAOd_kJJmc4G2RNqSAHn2NJoByzJ-0XvDBiGO5Fy6UVzMREKhJqUjSV428kdDjnx2vol9tNDrKrUzi_oahrjxtXxU-ntlvx1jA_VRNecn6sItCNShxVKLvsMurNyVwoGA42JLC3tUeoXRe-nw-oX5apM1YoamnW6QMnTHE_Tx80SRNlJl3xDfX8ULVxiY15Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوانین به ظاهر ساده فوتبال که نکات کوچک ولی مهمی دارد و در لیگ برتر گاها داستان ایجاد می کتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102634" target="_blank">📅 21:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102633">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b862859bc.mp4?token=I65y8hXF3bshSxKco_DiC9wmZFxqtKgQ0xlEr9nGCYm-wR6gCO_D8vyklih6qZ8RYmcHeqGNBnjAm_EtMiVnjldVSs0jfc7TzqpnM9it_z-EntaTAPf-n7tU0ape7lma7F8xUBkr41aSrMsKH54IHp1GEaflgofQhm3IJevG74RJ_2WupOvXApEiGajSbv1i1EOWn9cgleAx2WBc0XXrI2mV5QfTP7_XVSTaNkafU3N-ZolYRd4zRbpauR0cbsDZTX89rrqAJK2PKKGeSii6kdqoG14BCnBsf06SbSdVneLavFjosb_qp8fxsxKRM9dDODVAAwtx7-AdqyEbqjQu7RKoa9Hs3V2FjOIfPgMdi0i1G1Jkg4FyoVVb48MK3L_rtCjKKjYqCulAkzpG5CenlS8LocHUVL8zPM3GwVEZUjQ1Jr6aJOqLZZe8uKfKVMuhwEDKg8ulhBHWAt8Id2AFFqCwDTTPhfKDKji5zmuFiSPc9PRAjiToojX-fV2tUls0hvrZNydCkhDPpj-zYHqNm6GE55B75B_KMDugFLuA65uxFY91b2FWNo-qw-nx8FaG4oIhmVyv31NhNO4UlXJd4cp9tDLPCYZNKkcjy0zJTCtKYPB2o5hWelLK_1tdTCXcGxGXv8DsUeSq97UA3iq-I9BmXSslh0_roRqCRtQbbwk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b862859bc.mp4?token=I65y8hXF3bshSxKco_DiC9wmZFxqtKgQ0xlEr9nGCYm-wR6gCO_D8vyklih6qZ8RYmcHeqGNBnjAm_EtMiVnjldVSs0jfc7TzqpnM9it_z-EntaTAPf-n7tU0ape7lma7F8xUBkr41aSrMsKH54IHp1GEaflgofQhm3IJevG74RJ_2WupOvXApEiGajSbv1i1EOWn9cgleAx2WBc0XXrI2mV5QfTP7_XVSTaNkafU3N-ZolYRd4zRbpauR0cbsDZTX89rrqAJK2PKKGeSii6kdqoG14BCnBsf06SbSdVneLavFjosb_qp8fxsxKRM9dDODVAAwtx7-AdqyEbqjQu7RKoa9Hs3V2FjOIfPgMdi0i1G1Jkg4FyoVVb48MK3L_rtCjKKjYqCulAkzpG5CenlS8LocHUVL8zPM3GwVEZUjQ1Jr6aJOqLZZe8uKfKVMuhwEDKg8ulhBHWAt8Id2AFFqCwDTTPhfKDKji5zmuFiSPc9PRAjiToojX-fV2tUls0hvrZNydCkhDPpj-zYHqNm6GE55B75B_KMDugFLuA65uxFY91b2FWNo-qw-nx8FaG4oIhmVyv31NhNO4UlXJd4cp9tDLPCYZNKkcjy0zJTCtKYPB2o5hWelLK_1tdTCXcGxGXv8DsUeSq97UA3iq-I9BmXSslh0_roRqCRtQbbwk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاس‌گل‌هایی که ارزشش اندازه یک‌گل بوده
👀
💥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102633" target="_blank">📅 21:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102632">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c26f6b0dfb.mp4?token=CyPV1sd_4hedJ1HIRzjF8q4fA6OIujBRXb-djGMKuGI1Jv_ksXAUs5lkmu6UlKt5_YOVVhMnTsWv7XwA98xCFTO9tUAZTXHAvw3y7JyzQbKE9Za4Ehu4-UHk4htbaUSIr1thFdqslgVWG4XbLMgrwmHgzeqmdo-2SV1sQGjc392ihJu4I54IJaNyAgW2rwceSYmnuKWI1T3JzQLrCefF5k__GTd_2gKgiKYfLiOtD4HMGhCr6pNvXiUFWdn2ftc7TTdDq5idjJC0iZjraUuAJhrSKZF2OTnJ1qAkWQqw95biUWmQ5pcirWFj43XIw84vf-nGyYfICN4jeaTMie4PEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c26f6b0dfb.mp4?token=CyPV1sd_4hedJ1HIRzjF8q4fA6OIujBRXb-djGMKuGI1Jv_ksXAUs5lkmu6UlKt5_YOVVhMnTsWv7XwA98xCFTO9tUAZTXHAvw3y7JyzQbKE9Za4Ehu4-UHk4htbaUSIr1thFdqslgVWG4XbLMgrwmHgzeqmdo-2SV1sQGjc392ihJu4I54IJaNyAgW2rwceSYmnuKWI1T3JzQLrCefF5k__GTd_2gKgiKYfLiOtD4HMGhCr6pNvXiUFWdn2ftc7TTdDq5idjJC0iZjraUuAJhrSKZF2OTnJ1qAkWQqw95biUWmQ5pcirWFj43XIw84vf-nGyYfICN4jeaTMie4PEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فران تورس درباره آینده و باشگاه رویاییش: "میخوام خوشحال باشم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102632" target="_blank">📅 20:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102631">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6wFZKc_wn5HUtlPEos7TfQAvh-4pf-aW06tuiCmzU5j_0HIcHieO6LhBncohkai0Opfs0Bfq_8gpRrnfiiRqdeeeysg4ZzvQWiZSGAoBqowUGAUgJtsChRfqrnxxDzes6orAeSaoqULfzLxU2f9sRXfU7aUBktcL6svj7lzPX7PVO0-9L7WavuPLZlA5-FQ1XA9oSSXhGjhmLxDRrREPJP_EYsrlbnuTK-JPbNxx68q79WvtjLsK3iQP9OlKMzbdF79b13jRtPhLG6XQVzQz1bnpW4hXmZhPRGNg8qQOLeLZ9iCRpqEsyOkUU5T-TCytjoGaa8jqRerdKpH0gdZYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
تلگراف|ترامپ تمام تلاشش رو میکنه تا جیانی اینفانتینو همچنان به عنوان رئیس فیفا به کارش ادامه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102631" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102629">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tJyJTGzgWynVSxqi-_jB7ZofiuMunbijm-22ZxB5RPg_KQmpQLuXtxXjXt4T05KudjxuCCoNvx5RMBKkUMedRnc3Z198rw74msKcGdTj_01toQwkYrmMXBKgRA_6105W8VvxyBhjIy31bffTX25hGVzFpEFJ1u19Q7vJHf2IpZRNI6jyShqf2L5sYmaK1nCtEIQK7h3GRRg-7pSZed2ofL_oJ1oJubL3bL7zIsZ13lHlTmHsbDVOSBpo4pweAS3jK64VFj9YMP1B6eg99vN9PnY4jUDiAL_3N6imfC3ATM5vI7eE5-pyFjNFw1n3QBwSK67l26IGpI6IpCi1i6ixCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k28rmDjoWCRvc8r_JDLh77GtZUr_a2hxtIBOG9uTHUyMd5Q-rrBL_YqAGho96-LdMVLfu7kJyGieHJFvYcFDVHqEwxW7qAkB29VdPsSgW0ITOwPhGvb5PQ2YP-WugtM7fvQXqSajDe3ShMF44GAavHYbSt7OlTYSXfDYSUFEIANzNqV2T8xmldhe2CrEygKhPWjRkY30S2omnsbrAuMdvTnKak66S_CQSvB-V3v15mCKeVk7pKGPDxrxNu9xAg8Gw-Pz3tBKMhWBlP5ObN6lhBqBw3HzJMSvT6ID1ScJOYo9KstgLJr2YzQIRRWXSbQs4GPhc_XFuqVRlsTRMIYYlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
حضور مودریک در تمرینات چلسی بعد از ۲۰ ماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102629" target="_blank">📅 20:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102628">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVTbDNvfxhH2P5d1YoBMy-KhY2rUiCRPeLS9VBMgO1dUXXRRVcV_71TGHOORdC3dXujJTCPNC8Q_ryqD_VfZvZZzPqf5cQ5UIBjW5txkyksUHbSkG8VesTzZOi0TnIbIkz1HmBC4nCTnCDgeaWNS6Az5F4MWscVx3oquN_oxqNURgYoVZCGQE7rlARnCt3-rEVcuzlfz5wXbvNqyE-94bngjp0-9RVQ3jdXnAx_klfSgk5wyk7Ywfq3T8OuGGYm-J-v_-ACaZy3v6zaFNL14z_3-mvY7zghCBbHD4iIfC_gkC2B42P0WehDB06TluPO_tDeIfc9jViCJx9NeFrZpjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فران تورس:
در حال حاضر با بارسا قرارداد دارم ولی تو دنیای فوتبال شما هیچوقت نمیدونید چه اتفاقی قراره رخ بده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102628" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102627">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/590393501c.mp4?token=qap5EQbBpDTxY7mvLWqjxXTvPXZFojSCydnEOS_4AfaYqpDtQgrWovQhZxHFlBwRa8DNlDalTHHNaJUK_EJox32r9HSZEw_LDXPUtDuXjN3HhkVn3HzDXd_6KWv10Nyh5vWj3jXrUbJR6oZB85r9EHOxXOUzVxDR7k_Mdm8lk474eD2ylxJA6nFeRCbnQ3TBbDySam5br45zV67vW4pj6NlpdooEFFW7gGDFrCcV5CiRMuuO32p0Lv3vvPhpvYrVD-4f7PIhyHBZKEr_Sr2-fjmqZ2lbf577B6krywlULUnFZPIebuKOVv-sp1TRrju4kCDHEFG9vIxRW260MIM7AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/590393501c.mp4?token=qap5EQbBpDTxY7mvLWqjxXTvPXZFojSCydnEOS_4AfaYqpDtQgrWovQhZxHFlBwRa8DNlDalTHHNaJUK_EJox32r9HSZEw_LDXPUtDuXjN3HhkVn3HzDXd_6KWv10Nyh5vWj3jXrUbJR6oZB85r9EHOxXOUzVxDR7k_Mdm8lk474eD2ylxJA6nFeRCbnQ3TBbDySam5br45zV67vW4pj6NlpdooEFFW7gGDFrCcV5CiRMuuO32p0Lv3vvPhpvYrVD-4f7PIhyHBZKEr_Sr2-fjmqZ2lbf577B6krywlULUnFZPIebuKOVv-sp1TRrju4kCDHEFG9vIxRW260MIM7AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلیچ: علی دایی مردمی هست، من مردمی نیستم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102627" target="_blank">📅 19:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102626">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/IZNC37n8rGYVu595FrBIijr82hY7jJE7jTkCyRg3qfNEOTscbmh2tcU8j4fERGNXODNpSoHWjLqDxnWtFUK3aDggvdiWLu348qqG8IiFsYVrfCD_0EO3neuEcf_o8jwQjP8bEyPGBnsr-b-IyIjsXXyJQL7GC13aqi5Cs_w2NBe03izDXhgI8SwJCFSwrqiS48fq8zJi53J0eUjSMSgyhIT5yAkN9I3KmcsZeUPhDmhg8gCdGZqOumbM23fT0eGV8o7lxXk3vUkx2K5QSgYnyXAutHWRwt45wflYFYv6SXtJrp2AV7YKguhZQ6PCdvldvj9ExICm4PsD5IPijYoKsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
باشگاه لایپزیگ اعلام کرد که پیتر گولاشی، یکی از اسطوره‌های این تیم، به ویارئال پیوست.
این دروازه‌بان در 11 فصل با لایپزیگ حضور داشت:
- 362 بازی
- 117 مسابقه کلین‌شیت
• در سال 2016 با این تیم به بوندسلیگا صعود کرد.
• 2 بار قهرمان جام حذفی آلمان شد.
• 1 بار قهرمان سوپرجام آلمان شد.
• 3 بار بهترین دروازه‌بان بوندسلیگا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102626" target="_blank">📅 19:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102625">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJQihNxO9dgdJY70n8Pg8Y88CkNNolKoaQBhmekQTS8PTUIjTdxMp-ccOP_Vax4L-hrvTvqw0lc63IqWD-fJj1hKQQruES1_NphfY2EppTrEFUVUe-t9MWBzTL6FHyiz6u2eKQ_Q2sdRe1FXgIkpQHnrRNqVnQgqvm612-X6NZddK55wo8m2noD8c3v9q2q6Mq-V7sa8dmGSc0UMSdYEHxkxd_q83_Oz36mpJsuBeMTOeHbt1rm8_L0Dxd5LEzj2NnK0MCpb1BXZoMq48Iq1di7_uWHze7s8WoXJ4nLXXfuaoYbOPop_eH90A27txaMTFB-xDVXcPUekmrjmCdEcFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رونمایی رسمی چلسی از جردن هندرسون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102625" target="_blank">📅 19:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102624">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD1NN3oXYziTy87Fha3JWj9cEzbpqD09zTJfwy26rFhSZpnZvZwqS7ui6tdo0wdLMJk6RctZhILjOfDdgix7aBMh2DUHv1QqvKqkm8bvjdkphBI6U0Xihh99fLa6P6bXaKWT0-FZgUd5sVcF4WflnxuAAsvj0CM82pTu6-9xDikeK8QwITF1clfjRaRMLnnr_c0pP5qdC0S4D0CUFcpJW-T0kdEwCMD58eaqqx1BqM3bIdixdlK4utm5DFwUHtU_FZ-1XibEvKH7HiveMikN40-jbr_v0VrXXM_5NUvOVgc9yQqyEC3BCaowPFA1TywIDMzu7csdQptEtKvy6p91fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیاس یایسله به کمپ نیوکاسل رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102624" target="_blank">📅 18:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102623">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16357a3407.mp4?token=pY7OvA7-TUSC9bh643ZCO8kFyk3vVp_vnFlH2uO0Q8MpeAei1gK1PH7qvEFc3I5BEhLOYZj4rVq6s7iQ7sgGelPDIifeWsaYVppxGubTZMFnTkDd88frOfX4VsyyQjcVjwh12is4z_IIS-Uws8NwsA0WRk2KkWhIaT0bMqhkq9WtcH16eJzRdAYHh2KdA76lZYYtfc4puZySwTqgyu2BtBMEUrEqNRMgAcwm2zxvUOKlnsA1_DiN0LfVXwxcdTrjIgOOa7zjLIojzit1qwkb4n2Q0-8GSasZyIZRBx6o6yoTVi7kjyUyfz7td8heErspLt2dJF2n8xwYvcDU7DJmbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16357a3407.mp4?token=pY7OvA7-TUSC9bh643ZCO8kFyk3vVp_vnFlH2uO0Q8MpeAei1gK1PH7qvEFc3I5BEhLOYZj4rVq6s7iQ7sgGelPDIifeWsaYVppxGubTZMFnTkDd88frOfX4VsyyQjcVjwh12is4z_IIS-Uws8NwsA0WRk2KkWhIaT0bMqhkq9WtcH16eJzRdAYHh2KdA76lZYYtfc4puZySwTqgyu2BtBMEUrEqNRMgAcwm2zxvUOKlnsA1_DiN0LfVXwxcdTrjIgOOa7zjLIojzit1qwkb4n2Q0-8GSasZyIZRBx6o6yoTVi7kjyUyfz7td8heErspLt2dJF2n8xwYvcDU7DJmbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا فوتبال ایران بهمون یه ممد مایلی دیگه بدهکاره.
😂
یادش بخیر...
واقعا فاز عجیبی داشت
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102623" target="_blank">📅 18:25 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
