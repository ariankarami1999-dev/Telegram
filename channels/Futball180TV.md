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
<img src="https://cdn5.telesco.pe/file/gNNVh2833jllNBAAH0LtGceiQcALpzka1QtHFEjyV2-vEJydTmamlHEyCM4cWvCzGzfPZROuz29eXgqDhzrBDAt_EeGVWUFJ8Za8-uBiExI8_oaAaS-DnjZaOIzumN-DCI8oi03mS2fymuFA_itAzKqDNGDXc_gqKbPNJ97heZ03tq4NhSQeSIbiTVDDfY5zFnA0rCiu1rxZWfvx4R58G-ntJbB02j5ev6sxDuG4UWiOAGa14KOcQ_U6cd5ywP5eugl11OuUwU-1Gou5u1SU1lMuids4XdZz5x1tlNWe9XIVGe72ueAJz3MotP7TDt1YyIjtK3o6D3hrIgu5Mr0OiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 513K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 01:26:55</div>
<hr>

<div class="tg-post" id="msg-92727">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348e53e8ff.mp4?token=tN-Mg-VCvCYMDM4YquNdeI0JKKwsUuN3SPdzcjSKJ0Ld_-6xzWWo-Oe5ssT8uUwDdXhpi1mRXgiQABqHqtN0V2UknVhANEvOc9ZdMWs1OWdL0KD2vQtxeuLnMqc64E3lTJyvbequTNQVuLrGaT0Fqwb2cUVFO_IoerPw6pwZvg67evPro6P-b08aNw4gW9NM9DLQRn0c9ficZ6S8PcwAlmNIeY0gRX4Fz-H4MmVeWaE1sG9RVw8irWwjnPmPeLuSIs1jt4nYwkib-kgq3cgYIoLIf8OoiY6HfVzmB79D3wQTmJty7-lLNWj7wurIf3bYXZ6OY_X5Pv8w84D4sX-1gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348e53e8ff.mp4?token=tN-Mg-VCvCYMDM4YquNdeI0JKKwsUuN3SPdzcjSKJ0Ld_-6xzWWo-Oe5ssT8uUwDdXhpi1mRXgiQABqHqtN0V2UknVhANEvOc9ZdMWs1OWdL0KD2vQtxeuLnMqc64E3lTJyvbequTNQVuLrGaT0Fqwb2cUVFO_IoerPw6pwZvg67evPro6P-b08aNw4gW9NM9DLQRn0c9ficZ6S8PcwAlmNIeY0gRX4Fz-H4MmVeWaE1sG9RVw8irWwjnPmPeLuSIs1jt4nYwkib-kgq3cgYIoLIf8OoiY6HfVzmB79D3wQTmJty7-lLNWj7wurIf3bYXZ6OY_X5Pv8w84D4sX-1gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
خانواده وینیسیوس در استادیوم مت‌لایف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/Futball180TV/92727" target="_blank">📅 01:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92726">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d498d84b.mp4?token=VNWotA8mKXK6xhrQEZfpkRwAFiAmbF0G6fwMiaLMf7lAqgtrDiU9o_ryGIW8pEBp2-K_Q-PyHMgNiSzO2OE3GxFl_-ACRhdopprOXUDxu0XkV44hOhuSPnvCJbSe-lVhwg4qhIA9uS23lzte4vicqXiBtrM9Jmjrpo90AU_RVO4hHnt-bCLq8lX-76IzhSwFOl5UBQ9eGZb0TO_2vNjFFkAepGNTg5qCulugrQpOsf_GtNUTJ3yUnk83dcgyvZdVbYUlzuwNOmmOWumVCgs90iTAmzz0ORuRjvOrbsEY49T5lClnDK_NTnfHbP9ZtW6OvRkQtDQsRf78iY5SiW4KYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d498d84b.mp4?token=VNWotA8mKXK6xhrQEZfpkRwAFiAmbF0G6fwMiaLMf7lAqgtrDiU9o_ryGIW8pEBp2-K_Q-PyHMgNiSzO2OE3GxFl_-ACRhdopprOXUDxu0XkV44hOhuSPnvCJbSe-lVhwg4qhIA9uS23lzte4vicqXiBtrM9Jmjrpo90AU_RVO4hHnt-bCLq8lX-76IzhSwFOl5UBQ9eGZb0TO_2vNjFFkAepGNTg5qCulugrQpOsf_GtNUTJ3yUnk83dcgyvZdVbYUlzuwNOmmOWumVCgs90iTAmzz0ORuRjvOrbsEY49T5lClnDK_NTnfHbP9ZtW6OvRkQtDQsRf78iY5SiW4KYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نيمار همراه با تراویس اسکات از روی سکو ها قراره بازیو ببینن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/Futball180TV/92726" target="_blank">📅 01:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92725">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">۲۰۰۰ دلار روی برد برزیل بت زدم پس اگر گل خورد و اینجا بی ادبی کردم ببخشید ، از الان بگم
😐
استرسسسس
گاییده
منو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/Futball180TV/92725" target="_blank">📅 01:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92716">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2DYcKKtfgj1z-UbOUUS5WuREk2h_ulIK5is3DCsHUHHwstEzhbZyuakkrrgutfJPNTEgPpEdRJjocRRN0JWssR0pp63FFNL0ZsigVJHXncz4LPbByuJ6tjdJbAPtnFVZMItnPGdQXzMMzv5T9jc0YeGw1ooAxRBe21etkkrVz8iIUimP5tMMPO6R3fzO5YHwOG8PqJgXOv7OtXbxeE41Zrs2xWLeYFSo5jzsLkdrF_qgsUxzMJ0vKWJ2pCrY2rgGInCrkwYn7VdGnOrtBvqG9fFSI6BkZUW1BQGSkXErrGkjGYnQXdkbLeNwE0npQTpQCkETY9JOBKAQ1OnT_oKJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkEK4PkXAYoK_XWBcS8r7QWAN-iYMjuUXckTz9ArE66SbGi2fUpyW8zeiDY8ulFdsH6F7DJPEvJhhH_c6es0EbaykFqLiA4HTNmnWO43KeuZxEmTEK7tu0FOd2GBQYwE5HHcElZ70SG7A6eDctTuggA5oLGT8blhbeKozFEib5KGxsfMvfn93NvtptCJsseQphIIkg3rj0nWcxRUkUVzxeqU3cHyLhm1CLESekgNAoioRGa0Ydb0KEQc4IA2w-Mup80vX2Gzwo_-mibE333xAsRc3w8K6FO2oQB-pd_mXE-_Aa5z9RGkBh9VzPc7TiZ7oROGPQo30ZQSCdJihpJ4GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfRsR6ACbZAU9okI7WBsrgqxqkz0YUAENPVx0q7CSOrpnN1Q8OpsSOQ6SkagEjOfURE8pmQ97811pqVwN7YW_JkDVwllQCCjLYi3_L-XC_W6uK7O8XojFCeitLY5YGTF07IXcQq0CpldRJMoYsXuVm0L7dtu06Lm-0nbllrYlriFXKVOihhLa5QN3sU_sPXdkJc9Pyft3ulul-HZjdHOawIuYElgiSWmzn-t-jtvZAte_wpDNEc_d3DlaAQbfZVQQZSRBpsUbg-V2tHZKlP_cJnk5QNN9uSuRzpTeZz0zUJ2qMTnAU-scHcF7xNUe0PTf3ZjW-b2fQcHy-F0qMSrlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/em3guflenZzH5Evh6Of0OqsPED9W0AwO-4gUa8PblRjP0RMt8CeuyY0WKHbxAz7PBk-tppLAqBTMJZkUxcCgrhONSOU860AVRZsTAn758HGe2r80luT9ILqlqZJPLzHBB_PxSwk8IQ0DVkBmXBEYDrd33hPaoUx1saiS58UO8BD2CyPSjiTwuKLqYMVpR8bPRAZBoYiQS9ZGARzkqJM23WP1syYJ63GVaocXi2VGV-tkZr1UWPmHHkZ0b17Vb778p2TNCz1I5rPfLLYI-6H7wZOvaRHkDTjtXnXErfZpZeFkqtQ4Hza_VWsrPyaMjYzGhIun7uiekWIPqfQPiBCS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O9u-2MZXL6hxNjav8l1qhHVxfI-Qd5RT6kZyPB4sWraLaFixBPJQzadVlJLV3ikQyUWSx-mVMsM4cbSjCzlWOJDAdREi6XKGPPG4JPE3WHKmpakTwRbW7nufVNiD5GAJZmPcG6HjPlsQ2AIyj4aIUd1HVOw0Scn4m4r4rCFqnsT8Ca8eeqvUmR4h6vW8YMZwFqxXht6IXcMY_Gl151Mu61KkOJ3GrP31j8cnbeTDGhl4x5GGRf1HCr53bYHfNWonuzwHvUMQEu8FRs-wpXLhbFW7I9ZmGrFXHdcpskZLnNhx21I8ekoHPssNiA8dD6LnEQb7gXdxvB-2MTfuI81Ivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VHbyASEptNl974eFL2PeBO30vtYtRFNrcU8qv9tCmN7YtZKXLqxUvF3o_TLJIHOo5MmAR4toNXaGDGF-EytsXtVN-XXemwuO4ax4tGfeKtfwyVshMD_Jo9wjwdsrZ5Xd7lYcpbbevx0VarnPkEjgwCiEZg7juYvVv3MT5W6hb5oBIFb5-GLOu2S954ZJzweTDvfctJRExu7_0USlMW1iSOpadYwXxBiHzO-abC2SJIvl5Wcr45im0MjgvG9NS80BVw5fONQitvtJKNemJYukEDipYn-UB4AdMla9QoKv3Vv7hSFu5M-o1xfLxXodzkmod_JOdfqs1zk4ZDrWdnsydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rJGA4usEQefbaZyQLHk2hyi1euXCgiLn2hPrKuipPxsu9pimzLII-nrtHJJzRsSLEZZRWqf6-eEbgtwuCFKeKiWKWP-2xTmVEoTwq3jZTBkqkBPZP2lInHiaxbK27MKzFfFKQvb-eJa6nI_JVM9oIz_CZ5ItucNEf3BS0Ombvuvzl7OV-020u9oEtOr8dI3qkPpFjoY9NlRRtypbyxQhvwBxbJegdEaU7qKLIRnpcLNhFQY0Eqjxq_y6BheqDqbeaHbrGVK9VImvfl7qkj4AxlskSICxJVfLxGI8Ptgb9kN9h6Jkwiw5FMT8SVrtFAOYN-8gwFRNaK6nj2eGcxhOUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rjOcXozHOW-c-z88z94pmxD_94FNyKmDouNzSrBOd-1bvBin6ad_5v3cpU9Fw2j7SZgZXAq6_Tfi0IM3D0VTxTdNmCt0P0w6NRSyY-Q0tO9Q7Vcq57hmqV8v3Px0xMlbcERVY6rXg4rMMMwXu8OEYnnM72DtMmGMnmAB14m5urcDwoEuUBPbS4UQpmMVIwYzk5yolZePGajV1Pc-YcPJJ-lth1rsECXgnW0jtJ7IE4R63O_1Jy0aAYqoKGqr9x41fpXUnncW-zKJV4zjQu217bemp9C-SROi7OLGGW_emaDMTHCSkuBPiEDTZ4EvoWbDh-3coTZuIv7hlMTW_C1gHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FprqC5mEfXUKsQmpa4Sx4IFtPhszlZxoI_gZrvGWXZFpsA4s-XCDRC0eAszql5710omSgZ-Qn7WN3gonRXAHP6ewRY1Zz9_LiadNWyqtrOIr1qVDpt4QqRtoZdmoss_scX67vcxRZK5vWPkWzwPj6nrOJn8n08DKIT5ZuG--y8xcLqnBAlu3DUeZPWjBC-fc_LjQarMFQxCE5ESwCJJn6TK_nH6isekIA3fm2G0a8aRj2vqwslLxAAEdyr1coCEnyC-xxDaIRTgO79M5Li-MEsfGXSqw2msiNQoeLpAcdwSm9rshqEMDFXqzN7IRNV2D81GasAzawCdMWTPIfMC_3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاتای جذاب از نیمار فنا
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/92716" target="_blank">📅 01:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92715">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f94225cfe4.mp4?token=U-m1LzmOX4Q5rBtnZEmmgRD3Fl4A2vDdP-4KdOq1rjVDgmfWSZ4hryT7QUY0s59MrvEQ8bYcMK76T1_crIxKRMoFyOUblPgUA6Ny16f6goVib_8NnoaZDHTO3KJK6y51fGFuzHwKrCySoYEvWPGMO0cxWxYyrW_oE2xQhwGn9SbaFY3EAb-X7YDWVRybE61TXkEhHlG4oDF8ur5iBfrXURCeQ2kJeDhrcuo6KyJ4h6HpaqJYG4Ts2zr_ZSvyeRv7Eg_iL6b_D-wVpSH7xkJe8pHEwfsPG7qotElhRrGDCx9ga0Nzk1y1djRjtmIALutussKFR3Nhw00AaH0k32UkmDErSspQv6B6pL0X6ZNUu-xOqs0ZzUQMiRqnQsm7PteZ_BWVOQrKPGH2vJLlcqzi6lp3rfxxbAR1M2SfTvoAEm8bpeXDQF7vG_Y1wGoEBZt5PtSvR1r_D7ZD4P2VkmSygVPdG8X8HcCA-fB6ChQkmFjAEQxg6b3-GYy6EWM7CUfCt4nAdwIDMVbUCwVKIUdTfl4Q8ghIcTc1j6uKnIG6pIb0pTdx8GAwy2jgXXOZslfjpDyhtsh_XMHctVGViYsN2liPH-moY5lwNNW2TP6FY-B74qnT1BGPnu6PWjQXcpwUGdSoa4UrfoqrcGQx1rUZq3eaVAhq4b95z_IoPBhDU20" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f94225cfe4.mp4?token=U-m1LzmOX4Q5rBtnZEmmgRD3Fl4A2vDdP-4KdOq1rjVDgmfWSZ4hryT7QUY0s59MrvEQ8bYcMK76T1_crIxKRMoFyOUblPgUA6Ny16f6goVib_8NnoaZDHTO3KJK6y51fGFuzHwKrCySoYEvWPGMO0cxWxYyrW_oE2xQhwGn9SbaFY3EAb-X7YDWVRybE61TXkEhHlG4oDF8ur5iBfrXURCeQ2kJeDhrcuo6KyJ4h6HpaqJYG4Ts2zr_ZSvyeRv7Eg_iL6b_D-wVpSH7xkJe8pHEwfsPG7qotElhRrGDCx9ga0Nzk1y1djRjtmIALutussKFR3Nhw00AaH0k32UkmDErSspQv6B6pL0X6ZNUu-xOqs0ZzUQMiRqnQsm7PteZ_BWVOQrKPGH2vJLlcqzi6lp3rfxxbAR1M2SfTvoAEm8bpeXDQF7vG_Y1wGoEBZt5PtSvR1r_D7ZD4P2VkmSygVPdG8X8HcCA-fB6ChQkmFjAEQxg6b3-GYy6EWM7CUfCt4nAdwIDMVbUCwVKIUdTfl4Q8ghIcTc1j6uKnIG6pIb0pTdx8GAwy2jgXXOZslfjpDyhtsh_XMHctVGViYsN2liPH-moY5lwNNW2TP6FY-B74qnT1BGPnu6PWjQXcpwUGdSoa4UrfoqrcGQx1rUZq3eaVAhq4b95z_IoPBhDU20" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
حاجی ینی ریدمممممم
😂
😂
😂
ابوطالب‌حسینی امشب شیث‌رضایی رو‌ دعوت کرده بود بعد داشت فضا رو احساسی می‌کرد که مثلا شیث فکر کنه مادرش تو استودیو حضور داره یهو از ممد نصرتی رونمایی کرد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/92715" target="_blank">📅 01:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92714">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhWET-xLm_BQVK0ia0joi7Evx9VNW53ij3RYVXQyH0sP5s-tistnnT_Bko4ruDCSyQ_wAvdyLkrlSvwb1guieIx66cf_x5ym0VK4D8E_Kzw9Z3iqjhV2pxh6tp1A40NyQ-ezYHQTVHb9oycj0-kfFaV8XY5eFlqhOK_Bl5WX72CejWDiYrva6QlJPmgZUZeRYv1fqTpKgQv7hdaUY7bQU5_dKZrrQDueuT6A4dfgiQw1XBzeA5SkzOt-isPT_e90KBmfJ6nPqpDkU1BqJxnYA7eJ3AfeNlLpIeem8vhU00Kd7zZ98Gsz8ZSiWDeVBKj530kgs8_bApudrFA51j2rZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇰🇷
🙂
تو حاشیه تمرینات امروز، بازیکن کره‌جنوبی داشت وسط تمرین یواشکی از گوشیش استفاده می‌کرد که یه نفر از کادرفنی این تیم اومد گوشیشو ازش گرفت
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/92714" target="_blank">📅 01:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92713">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5295136.mp4?token=QH2uukYOpRbssr05AhgDbH_qwLbiM9HgHau6yFNOHbxApKoOI40jYavwdoFsDWID2XRReKDfmIxcX9F8TukWdX9vUmYpUQJpXBHJeg1uK9XBE4WA86MNDnmC11anEAlhjchCnfsLO0TBlEHHA2QVUoGVpHER8L4kzxtYiQa9-hue9OUSI3DPsNWy7ioGTxSHMqgc3CGPvmlII91RxZ6zz5tYR-FlpqYtmFzVKtzwUomXB9p7KXVeZzIaKq-Cqn8nTCwdx1ib772ssK2lTvDxSKFtl1mqiirH7r2CrgaNvNlC5bJxvq0kI6K9QqtMA0U--l_sgA4hMbdiRFGMSTPsag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5295136.mp4?token=QH2uukYOpRbssr05AhgDbH_qwLbiM9HgHau6yFNOHbxApKoOI40jYavwdoFsDWID2XRReKDfmIxcX9F8TukWdX9vUmYpUQJpXBHJeg1uK9XBE4WA86MNDnmC11anEAlhjchCnfsLO0TBlEHHA2QVUoGVpHER8L4kzxtYiQa9-hue9OUSI3DPsNWy7ioGTxSHMqgc3CGPvmlII91RxZ6zz5tYR-FlpqYtmFzVKtzwUomXB9p7KXVeZzIaKq-Cqn8nTCwdx1ib772ssK2lTvDxSKFtl1mqiirH7r2CrgaNvNlC5bJxvq0kI6K9QqtMA0U--l_sgA4hMbdiRFGMSTPsag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
آقااااا جیمی‌جامپ بازی قبلی رو دریابیددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/92713" target="_blank">📅 01:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92712">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15ed350a6.mp4?token=nmoQBl54IQMjoWwb4JrQF-mvQHuM_G0acSuGdArIcFtkISTd_v4e5FFwi6FEobAXxKbNXZu705SWQ-i9OqoaqpbO2eyh2AHkl894OINFYh-ERJqVw9f9nU9iy_p9DgKkBVfvQiZsqU0QTeChI_0QP3nm-PRPk92-DNl_Oz81oDlovR5vfN2UsDmZZKw_bwz_l3OIoUS4uLXq38GTn2dDIcEaCa6mukFTui7l_iGRD_gyK8kaBiwk7Iob4ZRbOVzEF7dmXJVSi4VPtT9f8ThqMaBdTP9GAUMQeMaAdKS65pHXpyfLWyzln5ytk1EHWqnY5EZz4d_6pe5V_X6jHqHh9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15ed350a6.mp4?token=nmoQBl54IQMjoWwb4JrQF-mvQHuM_G0acSuGdArIcFtkISTd_v4e5FFwi6FEobAXxKbNXZu705SWQ-i9OqoaqpbO2eyh2AHkl894OINFYh-ERJqVw9f9nU9iy_p9DgKkBVfvQiZsqU0QTeChI_0QP3nm-PRPk92-DNl_Oz81oDlovR5vfN2UsDmZZKw_bwz_l3OIoUS4uLXq38GTn2dDIcEaCa6mukFTui7l_iGRD_gyK8kaBiwk7Iob4ZRbOVzEF7dmXJVSi4VPtT9f8ThqMaBdTP9GAUMQeMaAdKS65pHXpyfLWyzln5ytk1EHWqnY5EZz4d_6pe5V_X6jHqHh9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
هواداران اسکاتلندی در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/92712" target="_blank">📅 01:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92711">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnMKQ3WxWTIFgSvWVGiLgFimE0tgWjnUXQbijfRTpLKUr_GgKKM4ZxzMVrkY5rxAlrBwyJvdVGQlAXy6reki-M1Ja__ZPW2D0XFK_TmZPRbrPdlB-Ydhz0zP5FOhRSt_kXfCyffElwsBNXS9_FafNbdOrU2BEUgVVIRh98FnBAADmnALCOJhFZpAkt2M9B3IUnAGn8N2h1ZwikOrIlSLLydkk-80OrMFYtfQB6WhHNQTDwrZtq6fVMAZazL3vcPcQ_t6OyVPrQ4_21m95YRlhMq9Yf9pzaZc6q5Hmq5YTysTK2veTRcll1Q4MZOQqfmLxW4errMO3gT6no_8s9kK3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوئیس با این آمار نبرد
😐
😐
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/92711" target="_blank">📅 01:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92710">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwD3b4yajv_dy-FzQ_HQVrgXqn-U17dqzHfIaScRXNCfaWbfgW0nGm09rdGQ8gpYQKvwZtRYQtu07DcQfyiL82X0kgqoqMIBXSzYZe0UIEoJZ0WJCd40VQ6SDjE2te-wiidovzTrpkgjauVg4v0uuWmzz2_Ls7a0NWhc_VfjBDca_e4w0Btz42gjV9hJJMb0Z7kqCulh1VYFPWAUBi4PqKdFohjD60v8WG6lbvyM79_NNZ4eiV_LD57-L28EbZCdi7VNljQ4nAtWUrmrn_A4v3N4lVxAtpabvGq8aEkF1I9d3zac7NpI-G7HTeT0e4UuOGZ2IlmJPyNibIJCVmIq3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
دریافت مدرک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_chat
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/92710" target="_blank">📅 01:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92709">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMYUGoNPEY8fHDIX9aXJAVrvhH4em2MV_QONG19bCJlamgUtyo6cnwAygtIJzG5gVW_pJYBh0NpZHI2sPJDlnSw4-kbfFXorKAn_kaN0ZoUwuXNr1lpHaKFGWoHdXeiN35-9OPaU6XTUN-KAnAiD6_n6a0IrwzcrRgpfCv0c4WcU-Xv-zF5DNqPlJQgog3eW--7Vb5k0wrfQ82PpgKabG3z3F4U4DuNunPtnDVhQpRqDe9gut0ZOo0d4_ynP77EPnqEvhuI9ut_ZJqGMWUhXJllHJ7f7ksrnZlbxZe-5F9Gs-PL9mqX-IhMrpI8pjGAA0ndJoQSjv7MNw3hXdsoN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/92709" target="_blank">📅 01:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92708">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAFMT92UD7ZNYTjdhG3ieXbN3gWNhyTzufWXewcAGkULZJMgE563SukIRWjm3L9vwluQt8euBky-3srrxYyz83Ilj1-QpKT1EPHYr9jLL_m4WmzPcoARpBhMJMHj8-vttrIHrGcMp_Tm3e28ZLB8htP_u7VtIyIgTRZXejPnmF8lED4WoWXLMkthe5GRJwh3mTK-OBkpD1Gc4mbQIbW8z0wmDxL44fU1MvVDehCI5TT59gUY3CZ8sAibL3iw-VFqsW-xW5PBsfdZj65i3dYe0y_73ZHjZbvEmH4eGoGp_4CPGjCaqqPeDX-uxmBEgRxXFz1n21gu9IZMSLU7-J6_Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از نیمار دوست داشتنی قبل بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92708" target="_blank">📅 00:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92707">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcGm544FGkqdKENHuqu_pIO-21F2zmeZ70uHC0oa3tTKa59OWYfOdviQg-tzRl5194fDl-61xSjGtfhp5OBvsqut4zx_5tpEq4XTf13_5Duxmyi_Hou3md6o8qpAyIIrwxLiLYjvkThkIHE7LsgZDcEtP0ix-r6qzi9K9BdwHp5zsN3Q7XFVqlaCe1H5T2YlI5q7qv7NaAjS_8MM8njWa6OyEZnlRQmTm-voWgoYOobR7F26FS8KatSaV0fmxInBZL1wjifHBuWK9MIUSrXVG9U7bA4DM-QfVYp45kq_zulZgijZaXAIY4AQrtVjn-cBwiOlom3p-RXoghOnDihxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|کار بزرگ  قطر در گام‌اول؛ سوئیس با ستارگانش به تساوی‌دست یافت
🇶🇦
قطر
😃
-
😃
سوئیس
🇨🇭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92707" target="_blank">📅 00:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92706">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqwCHkKNRYRLQKzqOdOugicvbovkdGBsocde1J50yABTlF6ErePgpkYV0_5C4REDZMIvh5Fi1AFIEOO_9S3hVlIIa4B44wAF2ZFOVa74NDpf58nLu93vZ4batPNV0voEC6I0k_wOqn3JyXyPZCNkD-_zVjOcn2XZOJm2DH873ihINkvjEiHO0W1yUUvP5NGhmIiCzsvP1JLc0c1gawTIghiDnnh6CGzN-rcHHzIEYvgzd-n2q8m10QCd1qgco9HN_Cu769QPGHV99ETyCX_kLx-ewO0Kd5bf5d18YqRMxRP7UG0Wbq2CySuE_Vw6D9wMVEW9nwWtUv_2-fvLcOggfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات گنگ از اشرف حکیمی قبل از بازی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92706" target="_blank">📅 00:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92704">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0Js7klBcJGDbi9xC_pbZuOJwzjt2_qpsjyUIsCoq7KQEhw6LyT9gG8nP5tLEZ1PlIFAIALPP_sxWQtDZnntPY83W3bp-dVSO-hQ9SPY5exUC4DP01oWMrT_gGAYIngSSFAvAkhpwJo5DsQM5AcUUwg_Sw8bq0to-ku8fjrbZEeXHIxdrsMm1NOw4QsR8879YjgzFySS3rjPeTPDzv3UZ70J34jnZj722F6xZ6PI4OYvFUDl9GvAj9b7OCPUjZIuIBOBoAtIOt6ca5QnUu81ctoqGypDXp41I0OkQXPbWgUMq3YndogBcHyAwKBObPv-5pb63JvYpsrBcFhMTG2u0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🙂
🏆
جدول دیدنی گروه B جام‌جهانی در پایان هفته‌اول مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92704" target="_blank">📅 00:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92703">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewk-vRmtKAw37h08qKGMXGQxyF9GW9SmF9_dKAeLJPm1pBtqm3Cp1IAnGBpkxa6yaqg_k8gCajvycWq-16nfZolXmju-yOljZ_NIfMSZI2iEjtwE3wsZ6JVsymcemRVKTPtHNDLd_4_-5_ggqZGoUIH1Phkm_sRfdYbnSJsuJ1OKeuAFj-E0Cfl4w2bTsjPXfC0UIBov15jOqW55j-CSuqi73IDxxXBttluhdiYtw-2UNyvRY341ZelTG_vo4DZFMDJGV7uSn930ys17fxiitzXE96DGY4vh7WqfCt3KGE-6jdVDfvxSdQzY6JeTEbHYlBafIVf_41qEw-dUEqx2SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|کار بزرگ  قطر در گام‌اول؛ سوئیس با ستارگانش به تساوی‌دست یافت
🇶🇦
قطر
😃
-
😃
سوئیس
🇨🇭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92703" target="_blank">📅 00:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92702">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpct1ZMp-FXduVr10ux0MyySYHOH92zzio65s2QuMLbcsj_bZz2G3lnD9E3vmb9XMseiau9hZLdrOiOKDmICKBBYy2qQ9QrPH__JtGdzcqyD_OKkb87aJ-OHZmWYsNPuqVrVDUEpOqg1zUsGMD1UisxWr8AVEIgEqp1PW3aN_7D98abyRxOnffw64RuDbo6sItq2gG9rpKVLX8I67bSkwfRBhKrvBWXRuol02BvwQlIognYiDlpSvCxkE8k5CMm0kLGjMOzbpE_QRdXSMhcNMPUDNW-ByuHSPH6By7Xz9wH-lo38U8nFvw0EwhgPEcg7Hb62qDi1k9spITj9oobhYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇶🇦
#فکت
؛ بوعالم خوخی دومین بازیکن قطری تاریخه که موفق به گلزنی در جام‌جهانی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92702" target="_blank">📅 00:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92701">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🏆
🇨🇭
گل‌اول سوئیس به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92701" target="_blank">📅 00:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92700">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5Q8TxG-lgBDyU74IQmxBrTXwGlG5W0ebv0EK8YEZ6uCnvePL7angvBxB-zDjSVL4o_WRBuVhuwJeVN0UDsaz3PJxu4ObFqx2uVrFq0yzq5dF_dzWWQwm1UGIRMUkY5ouJo8CEj6zxpz1CaExOxVPoggLwLCrq712UJSGTvS7xyQSCNE3msVwI3JpX0-gA8ljW9ok2wjRYBjeqOuEEohbXd6TvmlDKFiLAeqzchtCMpYF2rtZkYyBsgSKcAu6m30HnbLO17CpNCtYG1Bd_ZK7KsTT_rbdUuNbDhuHp_o4-WmgkcULWTxcM6ayIyOg5wgdb78Q_qEZJqNPp6Jv5DHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوئیس با این آمار نبرد
😐
😐
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92700" target="_blank">📅 00:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92699">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egIZ_gAHY-j62khg7axr-BhRhoNXpQnqhpGlLFZ6GMymDHB2i8rnfPOjNNog6OYDJbsMczhHZRlt53Mk5HJmpKvuPDJyUEx1Kg8spKUtwcgZml5OGKm5vDnRSPqVSfBhJdCc9Z82gILuhWNQWwnQh0qpMgXxeVN7n360UQkIQZTD9mVVwREiYhch1N18T36PCMFgpLvwdnGnx8y8YdW6jGU6YY15wyoDFilkxy9jP0NVS1BTsQA-GCYiTiDIbJGzWSD4vhPmQdoCBcFoB6uMhMAoIoMuhPDPjkYQpR0p4Ip_MSJjbIe_zqEk6rSyG1oWUr0MK60FPRosWpc9EFXn1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
گل‌تساوی قطر به سوئیس در دقیقه ۹۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92699" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92698">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بازیکنای قطر بعد از بازی ریختن وسط زمین
😂
😂</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92698" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92697">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf4bc984f2.mp4?token=Gb9ZalqCqZ60xRzYdltXbQQ7eBzeAaZlaBAAtjFOSJnMHI0fzKLlDF5aYVI9Xair2SdekzlEQsxRxvja6VcLPSxcqZEnSaf9tgFq78qd877RHYz6hEPaS_AcIsX0fwMc857p3TaNMk1PP2lDW77mODuRrcWk6fT2CmXTfIwH-hTb15ATrwohC6JlU7apET33oSFR-t-qysV2IR0_pygeVC4nTWhRLaJbiBOM6FCHIfDplHnG0DCLESngH_JpnBfzm51b-KPC4j1WOnpRDXpfRWJRV5wJ-o0lth9WCiAyMNgkB7a3pIMJsXylTKDHbAiV_p2yXyLdHk0B3MelfkC_rJPOLqLNi8IaXseQhZadSktOH2Mzmv4yZOgtUxYYxKq6FCHDDQyPQXq3rNn7MWA4A0Pa-lqqyb4O3IIGeLKqgDdiKHhQBibBZ020TAg2Y1UWFhQwKxum5IFnR3bDSiEjxFBP_9LIIQ2tsoGDNR1PBTNEzmcK38R3ET4WjurT17PYtm_jvSHEzkP-_sN2e8PO_67VO5enusNzxkLNX-2GrAeABsTIpkq2NnO-uP2BryDgf__1sgA5Iw1yHqw-28C17Mdlak0FjTZjeJOPQw0ElPDS6Qqf5RV3ntxgT66P55Lq9k7GA28wYjyiQHHEApR7qP_F4mqTiPehx3aB-D_MqoY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf4bc984f2.mp4?token=Gb9ZalqCqZ60xRzYdltXbQQ7eBzeAaZlaBAAtjFOSJnMHI0fzKLlDF5aYVI9Xair2SdekzlEQsxRxvja6VcLPSxcqZEnSaf9tgFq78qd877RHYz6hEPaS_AcIsX0fwMc857p3TaNMk1PP2lDW77mODuRrcWk6fT2CmXTfIwH-hTb15ATrwohC6JlU7apET33oSFR-t-qysV2IR0_pygeVC4nTWhRLaJbiBOM6FCHIfDplHnG0DCLESngH_JpnBfzm51b-KPC4j1WOnpRDXpfRWJRV5wJ-o0lth9WCiAyMNgkB7a3pIMJsXylTKDHbAiV_p2yXyLdHk0B3MelfkC_rJPOLqLNi8IaXseQhZadSktOH2Mzmv4yZOgtUxYYxKq6FCHDDQyPQXq3rNn7MWA4A0Pa-lqqyb4O3IIGeLKqgDdiKHhQBibBZ020TAg2Y1UWFhQwKxum5IFnR3bDSiEjxFBP_9LIIQ2tsoGDNR1PBTNEzmcK38R3ET4WjurT17PYtm_jvSHEzkP-_sN2e8PO_67VO5enusNzxkLNX-2GrAeABsTIpkq2NnO-uP2BryDgf__1sgA5Iw1yHqw-28C17Mdlak0FjTZjeJOPQw0ElPDS6Qqf5RV3ntxgT66P55Lq9k7GA28wYjyiQHHEApR7qP_F4mqTiPehx3aB-D_MqoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
گل‌تساوی قطر به سوئیس در دقیقه ۹۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92697" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92696">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سوئیس کیری کیری نبردددددد
😂
😂
😂
🤣
🤣</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92696" target="_blank">📅 00:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92695">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اللههههههه اکبرررررررر
😂
😂
😂
🤣
🤣</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92695" target="_blank">📅 00:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92694">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یا خدااااااا
🔥
🔥
🔥
🔥
😐
😐
🔥
🔥
😐</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92694" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92692">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">چه دقیقه اییییییییییبی</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92692" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92691">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پشمام قطر گل مساوی رو زدددد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92691" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92690">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">قطررررررررر زدددددددد
🔥
🔥
🔥
🔥
😐</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92690" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92689">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گللللللل قطر</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92689" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92688">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گلگلگلگلگللگلگلگل</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92688" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92687">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX9cCsUMgReuoVHEefJJcs4ZTR-NhG6UGks4nuqDXyFJE-rwl5MYPkiXKxoFDx6AYB-1bGVj557PKQRupru0JheAUYjhcxQrsI3Eb6irYD6wABuAjlGQ2X6cPVOoONxHxfpZC1DXgATyRXdmV9aJaUmMSBl2KcInuKR4S4dmtvwCVhxNQsy0aaZLe0nrWjAcFjKs2tUt343zcJpACSlwKTkr3ywM9Ya0x5YOmyHI_hmK3pe_UUcZT_vss0hRW2wrinECfEYA61LsTBU2bUK3HlFY7VdZnSKXrEUCv63S3_n3bpJq4gI4sT49huFuGcKnzKHv8FdKGwhhsdQ1QTRP6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بشر انگار نه انگار 41 سالشه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92687" target="_blank">📅 00:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92685">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بازیکنای سوئیس تو بازی امشب عجیب کص پا بودن وگرنه نتیجه جور دیگه رقم میخورد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92685" target="_blank">📅 00:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92684">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SL8V6jxmr8Bf0Qpb-CUEnRCN25_WmHQwfoBFkRD4Wp5jPZKWFzpLhJ7KrtGHEw4gVXG_Ee3dUlq7E3v_axjRXHaVCX8N0ELirh94WupCrCcQ9acYFakFLT6wnd9OD3DoyBe78R0-TXYXoVLd7VdwACdObNGM8dO24cijFPnQSETFdtMXs12ppBQpJtEJYkmNIpyaghPaoGK5GiEHofR3j37F6i_6BsHt2nOWF8RX_Eexzts7WFJaBP8ZPJ-lnemTSoryuhsF7YOu9N0XRW8M-BzjreCRVHRnyfwwDRZUR7Qva5zx6KyGgs5cdOcIUX6xZu3o2VTgnWDdGSV4TaIeuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
🏆
کلوپ در مورد کولینگ بریک:
فوتبال گروگان مدیران اجرایی شده که تو دفتر‌های  خنک و مجهز خودشون نشستن. این وقفه‌ها رو به عنوان «سپر حفاظت از سلامت بازیکنان» و مبارزه با گرما معرفی کردن، اما در واقعیت قفس طلایی برای اسپانسرها هستن.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92684" target="_blank">📅 00:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92683">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3a1d64a3.mp4?token=v7MpeVm7YiM5SNhfLABSWJqJ6iyQANhHxuXTxCetmQO-fe7StpTRaHkxLhGtNFuCugTVNPKrXvyAntly0C6_4ymSfMcS3W-NBiBPy8vheKVirfG7GQ18sDsg33YVGjgeDav9wWVvOSRcxsg9mKUVKfiQW4F1xabsHhM3hJqjvGLZXvdqRYl3WZTtiWBLATN14YYH3cMpfuH8DDnDHNV9QpNijDdXPSoMaQsUFyq_rsJoBnSr37Z2fmkUSD_gNJ__CHmTu5t6Gi2OWRHSTj8dLNUlGOiLgHlYtQ1lYJJu28j4fiIsvFXjUPqH45VQ-8tk_sriz0bCbezG1NhTGxDHqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3a1d64a3.mp4?token=v7MpeVm7YiM5SNhfLABSWJqJ6iyQANhHxuXTxCetmQO-fe7StpTRaHkxLhGtNFuCugTVNPKrXvyAntly0C6_4ymSfMcS3W-NBiBPy8vheKVirfG7GQ18sDsg33YVGjgeDav9wWVvOSRcxsg9mKUVKfiQW4F1xabsHhM3hJqjvGLZXvdqRYl3WZTtiWBLATN14YYH3cMpfuH8DDnDHNV9QpNijDdXPSoMaQsUFyq_rsJoBnSr37Z2fmkUSD_gNJ__CHmTu5t6Gi2OWRHSTj8dLNUlGOiLgHlYtQ1lYJJu28j4fiIsvFXjUPqH45VQ-8tk_sriz0bCbezG1NhTGxDHqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
آفتاب‌گیری رونالدو و رفقاش در سواحل آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92683" target="_blank">📅 00:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92682">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi0_ozdJwqZszQBnV4EZu4azFYV9dlsfX628fngZiN-uV-wr9ygBnZCCKVToYG_tRVeTTNBl25pCUVD4SbwUCIPluuPbBUaAJChYFxMf_8oAG2iOsLFDTCwe5ijYIuwqytndPXzStWOelmDyEcrpSpNEWmouXMbmqvBaiXfOKWdvZvzfv1sYgOVrUjZpNFXuXVLXN4fFmQdFYByCn6rmYMAWiUnsOpuCdTffKfOrWX73-84sog6FdoMtHOVva_hkyEeO7ysViUdS3TSU1V2GKlgFiR6x7DilvVvTOC119AoNf2WEoecmreHCCWYTeZW9Y7ijyUKD0RWz7cXYPPBozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇧🇷
ترکیب تیم‌ملی برزیل مقابل مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92682" target="_blank">📅 00:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92681">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8gOGKal05fJi6eiPU7MpY2WBQLUJD2lzywYQPTEMU0IiYLbV9yNcidrD8z4H6EdRPgdHrdrJYANHWR1EibkVt8bsmekqhoXtA2NIZ7Te4BXvRk_FFUGUoiH1XLL16Kbu_R5386t8T9y1sqDKmJDZD2hkY9SHGtMG5PtSR1C3s9UqjnshigYV85De4hD_XNNHDAV9ezDCmhN75thNFHIk1iNDIZ3kd8VQjClsz477lJO8LJQfHuT_QosoVW5pAGsiX7RPFJh6hUnmolDEoeNhCP-U0JLZbuyD1W6HWk22SnlmobKd-xW043gE7tqijNL_sXuBdaIKeJGLnKP26gpXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیگو سیمئونه: «من بازی خولیان آلوارز رو دوست دارم و اونو به همه بازیکنان ترجیح میدم مگر اینکه حرفی از مسی وسط باشه.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92681" target="_blank">📅 23:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92680">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">قطر تا اینجا کون اورده ۴ ۵ تایی نشده</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92680" target="_blank">📅 23:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92679">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نیمه دوم بازی شروع شد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/92679" target="_blank">📅 23:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92676">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U89P75MdcfrogNGyOCVU4k9LbcECqMc6rvKfG3gwzDYaf1zd_NdF49PJlrHL-626o2T4JXsp4llxaCfpdTGmirx4N2ibfL8UK1_WtpWptH7Z0PrUE7jm7jvmHSL6wDamlW0-nStLxcxdkoZdurTc7XG1qvPZRg61E86CTMuH2kx__ulNHN6icE4VUJBUbDOoFROl0lNRxk7OFyr657_W0ilpUCYCsr6jeg18ERaPEEhkS8OfwmlaPKV_7HWxDN-oiLfXtZQ-jUSe30jEC7UqOGANEXtj1e4znB2kTfVVyJ2L1O7L7dT1AMLnRMXH1Heu2MGvXQjiRZRt4h4akYpsEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKPjN3jh1YMiod3YXi_30x0v9o1pLTH8pZb1az3RfDbzWap9HQwUY2gVtVzMA7aVoPSwgGzaKStS5hkMrCtdf8NsRn2p6jfWdRCPlyWfnTLV8U7UPJuDB9zR1IXePOd370y6hg4BZWmHsRLsqp-pSvBLLn9359nbcY-FIP7zVbESm2zSqLtgsNENzqoB4fLDtaZszPZy85p9LN1eqIIVGeGIJ26g4hhigo_6H5GOaHdxuLN_OQvb28PRMPXGkkL-cd0hXdzdpCN8h5GCYQxN-34aDcBZNXOudzm6KH6s_dVgfVh4q7qK0xqIRw4pG3CvR7-ScYWv7Nq3GqbrzIoa-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VjH-DTR6yUIy2EZlEXq9ZwisrCMLAcRUONAgBV_PbrnKq-5njVkJvllEYnfmMhWu7HdcR2D7Qa0PKi5lhgsBR_43kkz8mwdf4L36QmEOTzLTCNh8bJ3YAkRwvEBtwo1GQ0VfEKRewAv4LMwKqrqlHp499HSkBEvBbZ9v-b2PK29876VUtCe7rppyE_hGmDoiLHesspYtgkrFtjW2CKFpEd06o6ZfKLApPMp5WGT67ViWnY2iKXQL_Uy9WV69x4R4ms_obByiy84UJhRfry3YDikc_ZPk4eh_VWehJLdZSulhFS4fLHmJpRsKPBLsmP3adtQtwlkmhbLw2XWwfnPpYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇪
بازیکنای آلمان از بازرسی ها پشماشون ریخته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92676" target="_blank">📅 23:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92675">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qtDVKGiXO5T9nLLmhbPEPKk6Pk9nJuxf7KsGVSmxYMAUESYkLGf5WcOUoP1up5mTTKgGVvj3bSFXFa5TkYDnWm5ZrgURKj3YAo3r_Xtn2rFCyb12Yl2SAnIoXYhuTu4oeMJt_OvH3RtgjlzXVoYdcujwFS61kXJfswjBs34gc0IjrdSCKK2k3LdnY8Qh8rv2uBy0MQz-W29OnU9WqtDyxS_nSCUyIEZluKNLW1DfALj1nNLu226CDga2I3bPFYgHQ1WhVImnzrw-gLFaRIP6pp8WqDhUtQCQnSHZ9rpmEql6pAeZF9IL1ZUBExJU6JH1Udi6A0PqXyShuqL5gV_7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وطن بالاتره یا شوهر؟🫩
وطن
👍🏻
شوهر
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92675" target="_blank">📅 23:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92673">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZoI1cfwlycI53kH0WoDiKrQkVmZICp_wCO16rbDMHIfpm6LArgf_ZyD7QfrqBzZW4NIcns4K4b0em86v5Q7BQ85nVpb6luNI8idsErwITCVQYiVIMJafr5l7XRGL9G2BL6biFb2Qk0sAVfzfy8JZ7BkgTzZe1tYK4ZMvOi9Dhm-FjAiDitTY-xuYo238K0RVbfjiySiYw8jtfh-9aW8nF88sbfHEgNIXCjs1IigeUXyR6MpFrVk_6batsydaMQ_63oscAFDrmKANLc5O9-foCa1Ow512Gq39H8Z0wUeVFNaQ5gFUMTgul84nCsdH8pV-DC18uBaQW_SaZ8hUkzprw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XtiVtaRL3CuqZdGxPpdawmz3Sbj_bPGXp7QBlBZsnq0ZgqDGzzdXx1DAJa80mS8AgsFIfUSPBrb54NvwSGp8EQESt_F2GSJHsMDnp84pu0feoqM3yfRxdNCxWGEgqfbDHCepjctL9xCDp5xmrBD_lMQ9aNmQgBBGeli0WHE9m2ufKhXzG6iEYeRTANqcdS4kqwbMARHGSrWL4bU36iy2BDN-KzfiGT7Gl5uGE9chNEKPljalSZirtsiyCfv-FBy3TytpZm09EPtgwQFn43OiXcnwTMuBIODzHMkZBWN_pN3mH7Jq4S5DvpBtGMPAx2_c3zBsl2cHKReVRgxmjpxKJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریس رونالدو لباسا رو کنده تا سواحل آمریکا رو جلا بده
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92673" target="_blank">📅 23:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92672">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcVr-CdEdYAyfrwfNZ2wvF57ylzKFY_1gBkgL5aqtVeoKiFpnB1RC74pxQYta0Ok-SHyDEBOkG7rTKyHYUIBOtx13eADD5C9Ttwof70z89WQUA-bEvT8fSpyUye99UlSju-n4pGwABEuT_I_I3aDiB4mrGSXCe51fhsylHoSezQkKTWC6VBCE0EE9qlppOn-w2MorEBtIl1v6M7JACxQt8anhImvi8tDW6v7Kl16Q44iVQyOnVXTjoQz__h7EMB_cYa9rlNnJ4gvfBiWHp56IxicNuognQqViiouW-e0LPGGFRfiSPgrXT_nuI3kxbf8w7XwK5LFs8nZVqNOb5uJ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ماتئو مورتو: آلوارو آربلوا در حال مذاکره با فولام برای سرمربیگری این تیم است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92672" target="_blank">📅 23:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92671">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvuK2f3VBWTGGsl63eR-PKpqb7Nx_8eWY5hgEHKb2jI234HUop6QkQmnVHAJYnTB2o2j90na5pTyEU6Jgt07vGVHrV_iSNgDkCop5Yy25ZqvZqMZc4Yus33ap3lpZGJ0bGF-3X5Uf2YwqrT5mT88arJGSserHCs8-2QZQinzsfFHj6v3nYao1Biz_XlT3F4uyyCHx-iWEBx7OXRfZQsxaNC30VNdBPMuRC2gNvjsCZ-LVU9fz4ogilz6RUFmOzryBAjysxPk7ICj_Sdf7QnmW769h3h3So8mPvXyXDhY7nbABtr-2zGG4hr4ghAVLynoA_eHa_v1lTGAUDlF4gBabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
این توپو بازیکنای سوئیس گل نکردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92671" target="_blank">📅 23:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92670">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNVrW3BzcwWYKcXrFOSlzsYqD_xlwF5u2ltQFJ0heBJHlEDrH7EsOdjnY6dFv__JYA1ImjILeuCQZcG4xfVdXl8lvbFft8G7eppTMNucTqaB6GhCIvcxXe-Dkokxrbd3eeorZg9lVDUGbyYw4BK4uzc0rC594dKIOsVmkgtxCp8OMM8DUYNnWWUIoHFVnhIGBthdk56KZfQz5E9PamKvHGwnXn8mJsVseJqXqhKEnV-ODJGlyTcQMKy1uuaUsk73mJS3KQreAO5bogN2I3iNrro-0ocDJ09m3kRFlU6_23WJYHidZ3je5q2Lg870QQZDcf4IKD1iG4CWW7Ws8a3n7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماتون بریزه
دروازبان قطر ۵ تا توپ رو سیو کرد و تو ۴۵ دقیقه نمره ۷.۷ گرفت
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/92670" target="_blank">📅 23:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92669">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پایان نیمه اول
⬛️
🇶🇦
0️⃣
🏆
1️⃣
🇨🇭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/92669" target="_blank">📅 23:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92668">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">واااااای چیووو نزدددد سوئیس</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/92668" target="_blank">📅 23:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92666">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">چه سوپر سیوی داشت گلر سوئیس</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/92666" target="_blank">📅 23:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92665">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gueaukzKjw9CHlF7AD2fTXzkD9BqrnuaGMIqn_OV0znYaf6_Jh9O-qF_OoqMBxm2DoBXPrjSFrgfhPUhRQrcTUkax39xakcWg_6D7QscjyhDW8bJB2z59Yfe8p-XKrFDLkRxlVKRgKrWUkk-CQmRgesAXVGfZZYP12LVNTV-mp8jUc0g_1AiObnQP5k1SQZVim8n80-q6_HE3J8wS4WHWi5Rknqi0e4NMq9yxi1ocXvWDgmkbIRlkDv7gENt55jfDU_n1wOCGWjgCmkNOQFAcg_8XM_LOkwXwHgbaGj1cJScrx6y6itAeU3Puqy6zp7JlpFH0MSbhh0YmHfamoEi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گل‌های امبولو در چهار تورنمنت بزرگ اخیر:
⚽️
یورو 2020
⚽️
⚽️
جام جهانی 2022
⚽️
⚽️
یورو 2024
⚽️
جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/92665" target="_blank">📅 23:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92664">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04f957d097.mp4?token=mJ8Uks_yHUfaQvI-CSwai69xV3JCSB5-9guu1CJFtD5LkO280mRH2bo6g_wa_w69x4M6i9nLiVblOuQW-gF3X4R_epQ4Eo2n6laoM_8HVpgxpCmJLfIKFkKwuA9EV4NV4Rrq-hhHlHCkYzdPmnDM7rcLZ6rlmNu8B_2zn7OHX8HYhqieSUi0kl2OaGvy8lLYbzoLfunVSAKUYhhD19bwY6ytND__K95ivX9QFf2xOvVZ_cnnEQd4y4QdxvOcHEiko6ll7I4AYc_OPZSoU0opVUlrzCWpcLzJpiVuf1lC2t7yeYlyLoxcIAgfgZOBjF921NDSEewD1Otd9BVSBK5Y3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04f957d097.mp4?token=mJ8Uks_yHUfaQvI-CSwai69xV3JCSB5-9guu1CJFtD5LkO280mRH2bo6g_wa_w69x4M6i9nLiVblOuQW-gF3X4R_epQ4Eo2n6laoM_8HVpgxpCmJLfIKFkKwuA9EV4NV4Rrq-hhHlHCkYzdPmnDM7rcLZ6rlmNu8B_2zn7OHX8HYhqieSUi0kl2OaGvy8lLYbzoLfunVSAKUYhhD19bwY6ytND__K95ivX9QFf2xOvVZ_cnnEQd4y4QdxvOcHEiko6ll7I4AYc_OPZSoU0opVUlrzCWpcLzJpiVuf1lC2t7yeYlyLoxcIAgfgZOBjF921NDSEewD1Otd9BVSBK5Y3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇨🇭
گل‌اول سوئیس به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/92664" target="_blank">📅 23:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92662">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پنالتی برای سوئیس</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/92662" target="_blank">📅 22:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92661">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پنالتی برای سوئیس</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/92661" target="_blank">📅 22:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92660">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سوئیس نزدیک بود بزنه که گلر قطر واکنش نشون داد</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/92660" target="_blank">📅 22:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92659">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بازی قطر و سوئیس شروع شد</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/92659" target="_blank">📅 22:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92658">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tvq5HV-glAO4KWocW0R65d7aPBsRBN-S8gTO4Cbg7D84pcGaHfCe4z606LruRdzhLcTQfU2zbpoiHpXQt3OIjEJcEsGA7OKybFeOan7374XVNxJvNi4T7GGn7Z--nU3_FL7ZdPiWcatXu4DGXyRLP-25h3SQyddAdluuxOYMgXC0XCiFiVhfZEkJKzm-ax1XW-yM1t1zYHjXrQjEic5k2dUnOr8GuFUzX2ZpYz1LQmX_189cXcM6bmJjhPfpzuuOWDjAREU-Qqvgsw38o45OomCfkuG5jrCIoGHncvkY0__j_24fKEyAdf6AJs2MENC5qXHWxa7xA5fFkOUOks8kNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🔺
توییت جدید نیمار در توییتر؛ امشب قراره بازی کنه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/92658" target="_blank">📅 22:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92657">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnKjRNIfyvcwx93wEr0z0mSKjpKjAJb-e-6PjcBEUO_p4p6iIGEMQN0VuLUhlc0cnmRqJ7xOHQHB6uNrhN3YWHUtcozM37sjQ1j9g-QqBUp_tkBD6Jd3adIQHImrshsArAgDRZo3DAMl1A9rDt7FGoQjIh9droq91_rW5EIPiMDlGSV0mJ5V4CyK0E6fnUP164jNGAB951Bb9RS5gY_vOj5RH8CdoKLUifwy-00HDlq5u0lTYz-v8NJp_DrnAg7RUvDfosNAIQPUFi3Z-dC5jrC1hKTtUaI_hhnf_jhqDJqrm94qd0VkEhtUjb6Rgk_yRsPQFAirSBmHuJ-ePWefUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
📊
🏆
براساس نظرسنجی‌ها از تماشاگران، رضایت مردم از میزبانی آمریکا به نسبت کانادا و مکزیک در مقام بالاتری قرار داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/92657" target="_blank">📅 22:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92656">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90512a635.mp4?token=KkYYcfo9ORkjSk8duxlVuhM7CizLXE2g3YiEqj9fGRKITgj-z5-tIjqrM6RGKOQHuPHSB5UJOtA1ABLqBsquA03r4zIO7_swvRJtlJFOUlij4oEyoYH1ocNYmgy4rdv_-Jhu6JWi0GYMD9RPXSQoVO_OdzkrbivwPHKjAVf3x3QiNC8tLrltnaXcR4DGweFSI7-HXa4INjMJPZJHwL_7MaAN9siLyE-s8YTEmfhHu11r3EAZT6X3jiBnx7wSPibH7FTaz9IKOuphwghGmJTwtLBz_5HZNOI6lkOELprjhgSaoUp6wYj9I6WpQhy-OmV8UW61yc0JIyi3r8ycAziesw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90512a635.mp4?token=KkYYcfo9ORkjSk8duxlVuhM7CizLXE2g3YiEqj9fGRKITgj-z5-tIjqrM6RGKOQHuPHSB5UJOtA1ABLqBsquA03r4zIO7_swvRJtlJFOUlij4oEyoYH1ocNYmgy4rdv_-Jhu6JWi0GYMD9RPXSQoVO_OdzkrbivwPHKjAVf3x3QiNC8tLrltnaXcR4DGweFSI7-HXa4INjMJPZJHwL_7MaAN9siLyE-s8YTEmfhHu11r3EAZT6X3jiBnx7wSPibH7FTaz9IKOuphwghGmJTwtLBz_5HZNOI6lkOELprjhgSaoUp6wYj9I6WpQhy-OmV8UW61yc0JIyi3r8ycAziesw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
🏆
مراکشی‌ها در آستانه بازی امشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/92656" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92655">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pN00bfxvSb9hMqZors80Ldlgh9VCZdwu3l4EsD7DZTSdlviqvb6FijxwNlsj1Y8UHeptf0t8J8x49Lb2bLOLcAgPlWmLYl1nh7kUGkQhRtqAnj7-Idduc0prJrFqLkc8499NhTaRQBLWCioXqdn3Iggmi0h0-i1tk31tnW54sasFWgGdOVAk2MPtfJWFfjrNYmmIgNssoNA5acFr4KhiW1iHgMbQ2nSuRJaokV4Fn6DPvCCiMGa6RK6zB2kD1FYnKySdA4jslNTSrA8RdxD_7zhwHVzHM3cViIJpyWDhXD7wphu_pvuc0encgXU5aRflNoq0vKhDY4VCjEufiBw1kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوووووووری
؛ رومانو: روبن‌آموریم گزینه اصلی هدایت فصل‌بعدی میلانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/92655" target="_blank">📅 21:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92654">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1__dzuJaOgAridJqcSCLe36Dic4F9ZKNmazUXQVrlAdrh3Sq48rqKgn51Q4RbAdhpBzLAUHMk9yQkC0JcsY2pIOpHcZ5ixyc6D6P8E65QnRXohG7YWi8JHd9TZzO-EvwTPFk8AuaZapHeR8ioV-e36teK5FGtNNTKBYcRiZxoE7DBIare7H-7LKysp6YVEil39BSTziSwVC-gMlDeTiRk7LF_qdYuvq9hhn4IQpCZ09J-I3oSJsij9SwR3j9eKJebkrPaa4m80-xCLJhOmg5dt3f4N6y5T5aAX9YZHI-1xoK3MpbouxSUQqSgB8grtW4pLdKVULtq6jXCiLYoZCfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇲🇦
اعلام‌ترکیب‌مراکش‌مقابل‌برزیل
؛ ساعت 01:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/92654" target="_blank">📅 21:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92653">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhtGtpXGPoJRkIx7zKeTPndQhneRTCDTpEFDVseL4JS-x4gdGXpH8i8pwQ1dlqRcgT3AeqoPUP6jWLCE30Z-OcgQZ6hfE6-VCphlqvfrWc-H2Hj505X5cdLUH5I9TESyCKQZAlXhL8790kvuG9KxcnT87RubpcjQAmqZbDFHvRCvIAuIAeJGfqUkZP-0oA7jM5g1WdYeNEXmTcLu8gclMkKBEFWmbnymZ6hRodl5BVmLG_yG2yJ_9kIjA_IdmQFcbi2fmg1F6l7dhl_vcaP2Q3MnnjTyxu-VYvWGuxlu6P2hcD6pDGY-1oN7tqEZc9X-rQCDkPecVyPUpNV-zDrbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👀
🇳🇱
فرنکی‌دی‌یونگ
: ‏
🗣️
هیچ تیمی از بازی مقابل تیم هلند در جام جهانی لذت نخواهد برد. ‏ما سرعت‌های بالا، توان بدنی و قد بلندی داریم و همچنین در مالکیت توپ و حملات سریع و خطرناک تخصص داریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/92653" target="_blank">📅 21:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92652">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/028f0149ec.mp4?token=hWUxM84eHgfNJxIkQSVIYtDAXirsAqHgy6rjaRmnpDql-FZ8TRsClKOxDDbaNp6yvQFob1jgkz2Uu5pqA0vlu0mSiENFVjM1YVgiUiYojG8OmCZtP0DhN9PYmd8gL_--JTrpLCSWt90HjkHkTCzGfR43XRVItDjxg2BU8bnBVTeFJqEtZ2SMV9WYDdQeXnu3UjlKjL4oJ5_3LazZLQ0zM4O0hrLR6Qff1viww0J4bfOJCzgWDY5_dUpyK2v0rEPNyJmv8oeRyeTj3fcsN2LIS3MhBKzq7s3ufTrWlOyiSjg3OyS2EqXPDJgIcB-mahBt2nqWhI_rULBaKIgtOJCScw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/028f0149ec.mp4?token=hWUxM84eHgfNJxIkQSVIYtDAXirsAqHgy6rjaRmnpDql-FZ8TRsClKOxDDbaNp6yvQFob1jgkz2Uu5pqA0vlu0mSiENFVjM1YVgiUiYojG8OmCZtP0DhN9PYmd8gL_--JTrpLCSWt90HjkHkTCzGfR43XRVItDjxg2BU8bnBVTeFJqEtZ2SMV9WYDdQeXnu3UjlKjL4oJ5_3LazZLQ0zM4O0hrLR6Qff1viww0J4bfOJCzgWDY5_dUpyK2v0rEPNyJmv8oeRyeTj3fcsN2LIS3MhBKzq7s3ufTrWlOyiSjg3OyS2EqXPDJgIcB-mahBt2nqWhI_rULBaKIgtOJCScw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نظر پیروز قربانی برای برخورد مجدد احتمالی ایران و آمریکا تو جام جهانی به همدیگه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92652" target="_blank">📅 21:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92650">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0i1bk1tu7cAnAKLeDUtwoECwf_A5CRXWcJhnCh-JYFIE1AIYiaVs2akDbLxIfdEqFHOlRv6zHKneufS7vjdMHjcXz-FZLi4P9O38pd9_KD69rjhF44P84iJC4_qalsQEIQtwgCkEIqNIOi_vLj-2rF0sZoHO6nA1sUDhI9o66k0-VDeLvwAAw3jSOuH9EX00Yd2Ayr-2STNJmyN4pBoCFQF_mPJOXJuRrqPnCrZK_PhK4E7n5ncE82PHepmJU7C9IJA-Aud5cJXeifBWTi5RgPVCrJJRLMtWZSp-Ct5ylEQeLLVnvRHIM7bQAEe8eo6KQuEKp9_mo9ISana_Z9HgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
پست جدید ترامپ کنار رهبر کره شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/92650" target="_blank">📅 21:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92649">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VifODHDDDC0gpE5JkqaV0C462vobRtfVogMZT_B3VjM4njoAht261eF1HnbswYGGMJOSnrRgpz20WSJOPCX2kOxy4Iq-S1thFvtC3TQCOGTgCl8NB_m9aPW1RN6DXUqxsNweqeuDo-JnG7drC713KYqL9mHd_AL3VwUCn2jcfqmkAohUrLIAZdCM8FV8w1Qvke0xsI2042_3C29fNmo2M8xzbVxPHCwKrVZPCiDky2z1U1rPTiJ7sAUwfSmtWSb-cse0VA3r9Typ4X1GqdstBf-M43pp-cKe7sEvHjRCVcXY7e1-4cToleK8f_MXygOBnYaNUNIvd5Q_iJZymn0K2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هر پیش‌بینی دقیق = شارژ کیف پول
در لیگ پیش‌بینی «همراه من»، برنده فقط خوش‌شانس‌ها نیستند؛ هر پیش‌بینی دقیق، بدون قرعه‌کشی جایزه دارد.
«پیش‌بینی دقیق» یعنی درست نتیجه بازی (برد، باخت یا مساوی) به همراه تعداد گل‌های هر دو تیم ثبت شده باشد.
۳۴ روز هیجان، ۳۴ میلیارد تومان جایزه! هر روز یک میلیارد تومان جایزه نقدی بین برندگان پیش‌بینی‌های درست همان روز تقسیم می‌شود.
💳
سهم هر مسابقه نیز مستقیما به کیف پول همراه اول پیش‌بینی‌کنندگان دقیق آن بازی واریز خواهد شد.
@mcinews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/92649" target="_blank">📅 21:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92648">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIICFmv1acV5St677KtpiFTKdcr2jmU9BbjxbwWRtnTpYNuHLXs7DtTP6ThUsfAAacyNatH5msOjsaVUcldC0zGmvgM_8oFf1Ex3QtgRlzGGopSvxAu5O_7lbfPuNGGcbJJ2W1NsSiKBKub4ojENZP4W76GV0aetuLRnO8WcI7w896S9LAm-cSpZfGdP2GHV6Me5Jim7GliTqiheqA3bTJ_I7k9B5MsVghlwG048gbB2qZEeknAiU7KJMzEUlcENVVCdIalQvsgAd90FxlEf7_L87_Md1a0LZ7Udhd0Pz2T450_8B5csT9c3yop7LdbOQbKgQxoCN_kk_HCc4CAW-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکیپ : دولت آرژانتین فهرستی از 13000 پدر آرژانتینی که نفقه بچه هاشون رو پرداخت نکردن رو به ایالات متحده ارائه داده تا اجازه حضور در ورزشگاه رو به اون‌ها ندن و فقط در صورت تسویه میتونن به آمریکا سفر کنن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92648" target="_blank">📅 21:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92647">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwylTuYgLru0PYIrS9mFA8Ua3_SfuJePi3mVpusLvUXoWt-s7u554WasuN00iYXS01wzKBB9EpVV2icGjvWTrnbJv6AtuP5flph8oEsh-vYfezKUpwzRoO7pMPzeQgTloB-0kcIakSxuRf5qYXwTexTvaIgkL-3yxOPgPPt8EXk-vYw-DIydNML18U1-RTgVrXM7P14OssczJO2BPh8-i1QpMAB5JEwYcGGYrkYVmtK3kPqD115D3lqVaXV6TviQqr640bbTcNiX_Xd-Ul0NA4RNms0uh5u27UXadpDzNUSx1gnLPBQDBG9bcsBaRH9hOLXKEjSQq1f2WAgskPGKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
🇲🇦
نمایی زیبا و دیدنی از استادیوم مت‌لایف محل بازی امشب برزیل و مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/92647" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92646">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP1SbAhbHd6WpQfXB5yRyNVDO4WfhOJGV4TFZflmGM8c9jJdbL0umUzIJ1VkJrJ3Sa0qltXBbRZH7Ywbh9TDg3k8DQ9A53wEEoHVmMzG79HFWXmWuS9WRzt98sdj9HXCKxFtSf8HCDGMKOJd7zhOZSuQEu-tiLP9OPaYywgQoTHhT3s3nNtfUjB05S46kaxcui7bdCDKJV5iMgaxW4p2V4ec2JgmI13fOx4CrOB-G8Q1eEXv-uXtdj-_cPjhz31VAojrI6NlJiAHV0zAqDcS55loFkELosmqIviq_wwAXHnSwSq7_UlF5JhpLcOrdoEYxNNI2WYTqVSvWNgAEBfrgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت طلا، دلار و سکه پس از توییت ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/92646" target="_blank">📅 21:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92644">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mrTwKFF4cLXVBD8VXkXVlSv1buvjRgvJIulKTrGZDJjKYzCexeGLXU3MxbAN_coERvHQN9Ox16iT0-3o251-Dhv1nhoDJ2xWKKFd-TxwK79oyIH1US_O_m8ELD2_DqNcaR_dXR_jrKIsbqrlSLKuZvouSFct49XGhjTpdhMpf8Agp8eH58i0g4W0pieMP-UYIJ9Wz5KkTInQ0EVdRigdAaEhL8A0qVoqPwx94UiBcfZJfSEl5PkNKC-9WOn48PK2tc6PKjy1kn-pIPCBv_oiK59dhRDQLgbnwnF033ekWdChYfKiV1qMBrjFIK9u2y6mBOvlsap4CwKMOmFLR5BVaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sim3wS4O6VN4VYjWEBejLd5EmDwK58aFcmaFq39Xsv3ZTOci2iU6LFS7I3_zMoqF3nvtdEWpu-PgeazkHu-VMK4viFmrEDsC81p9pmemzqxk5nahYKO87q5M6kY-rADnbKnbNQz_vxTkmkszXbK-3O4Qgy4HDJIXbU1JstV79xi5F8Ream30H1ks5Wjl4lDFwCozrm7m4MqB9q2Gv46oreXWKbzjNpTerhqdI7y5Oy3BhxhqImlcl4Fw2ABFB9_KRmDLzKiE3UlesUbSXElE6ogn0zCyBGMWRzkQ9WBEb_MnuaWaoXTgSCDcQzIQpQ2E87eJm0n4A4L0OcHdYAgwIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🏆
🇶🇦
🇨🇭
ترکیب قطر و سوئیس مقابل هم؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/92644" target="_blank">📅 21:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92643">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKIUqxQwiwudx-1-SU89wpnB1TMMIl60Sf4H-CKbwfAh4lwH96_kIYL0awjI6_t4TrrC9Ikg0g2pQ1quSuhU3M8WaWg2ULVG5krIWpU8bJt74GtxsVtDZU7ugP9xpOHdVhUgL9Cw98FA2K_ZZccFegRY17-CM1otsFWtcWuZ78VYvzJPnNp6VPuDb8ggOOJO1M92QPlyKY9mNFZXY1Cm5Wv7O9Dn8uEPHL-vVVxbAwTC4FN3LfZGEefbE0bPFOMOvuV0bd9pPbnHhyT0GtdiO6KFv-7xb2sJPi6jGxHU9Ub-qAHrc4BXEhLtAxnYU_gM8exiGTmSPxKDi_bFdIZztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
به گفته‌منابع برزیلی، نیمار در بازی بامداد فردا مقابل مراکش برای حفظ روحیه هم تیم‌های خودش روی نیمکت قرار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/92643" target="_blank">📅 21:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92642">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLMGQi7JIGqyv85EaVmDZpxCedgCKbquXMWn2mIy2qDth7kcaz0JLDuaOOzs10Yu1qLpPmEFbPivpFh7JU1CVjwtJuPe1YY6Wxj_rIsN433zJ2N9WVh_rEdZHgVnc8QF6Eky_G4fdJsH8MTif2WzN76Z56p2FTWKzrq9cvnuwQ9fWIfSNp_Ox488wZxYAD-UxlBqLqqG5JMra3-3-SZBdPr3OGxuXVNlpbK3rb_9NMBhYap0pIwEbUWUxVDCeM1vFQL1JneYjfmvTlbu-D1LOD0IVAd2mC6dZUYfy4io8sFFQGIAx7rBvm_PMAiZSuR9WJwfA0UzGKchizZVGkqgRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هلند
🇳🇱
-
🇯🇵
ژاپن
🏆
جام جهانی ۲۰۲۶ - گروه F
⏰
یکشنبه ساعت ۲۳:۳۰
🏟
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
🚑
بازیکنان مصدوم:
یورین تیمبر
از هلند و
واتارو اندو
از ژاپن به علت مصدومیت در این دیدار غایب هستند.
👨‍⚖️
حقایق داور:
🟨
میانگین کارت زرد:
۳.۸۵
کارت در هر بازی
🟥
میانگین کارت قرمز:
۰.۲۶
کارت در هر بازی
🧠
نه گفتن بخش مهمی از استراتژی است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/92642" target="_blank">📅 21:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92639">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtdAEgO4nSM_JSBgj-BpJDQDBgJcgUJuQFzyfMiI6Jjt-8qry7hOO7wbU-2ilDU2RSA0IxhKaHX0n0vqNKO2gJsp2EreSOG4E54pBi7G2mq4NaBMvmDgoH7cz4QdXVk57Agp9oEHtIC_ftcOwoZEDxdxDYu0Is0HzEdY5icVIXRpjVW2fdLnaZwXjLgPZ5RICNXtmOJzb3AEPXqGtq_9CPhxvN6sYi8khlME29mciCqzS9oivi-RlO_MCGs-aXuyTtY6Z1QMj6EhEh3SJEum0q920KX2LTiXVgNXofN2VxreGZn49RIsv6QoTPkJzmvXu84Ol9yYeWVBPDWQ_SfDjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخت‌ترین روز زندگی بارسایی ها اگه این اتفاق بیفته
😊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/92639" target="_blank">📅 20:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92638">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh9x9mb9zfuHhlLNOqqBAtMuhI5gbYfrwcLVaAVZqWcqLM2tV-0Lo4HaXwKEOtuGzOnsTZNP-tEWhWExretTQj9OWcnPI_Zw5pXy5JWhXVywEHzf5yuxuxMeodZabMr3_ZMcnqt_Z1so475JSdOF7m6hLqX1JClqbIU6S2_nmuJMvej2HiQLK0c9eIfFNxEkbgQrra-jLZ1Mwt-z54JAeSrCSpK0Hio98cQNZeW2kDhty50QU1yTPqf7iD-0xD4UhEg2bOQ2V9m9MRXJcBgRW0GLfwc9GJGbhj48BFGk2quYBW-mk4pRoQZhVyz6chhvolEHUBf9fhvPyM3n3JSU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر قلعه نویی برای صعود به جام جهانی ۱۳۶ فاکینگ میلیارد پاداش گرفته از فدراسیون
😳
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/92638" target="_blank">📅 20:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92637">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XX6AuztlkQ5XqluwUstg25SKijUwvKc3yEARndSHEaf8wx7qYZRCaXO_B8pIebDqoAhfHjtUvac8EyRlbtm9hBsPeLWnYzvU8RBMj4fP22c6c8jv7H5vmUIf0iX8r4Xb0iVMPwphRHtiqf2_EsfysMyavkV-YxIA0RsOI8J4SrwPpx8xQoYM_Nm3laO39o-2JL5hDdOgBWr8LZsNJCmpt6RboP-v-MPfRy9cwQoO00Xn-otKyq0CFvKZnIBcz0eBbz8TYPWg8wrLVOc6s29ABjAXQ0oBmi9jMcU1EOXa0UsbAJj8zH8O-ToXPnjk0ASgyjuKDTxAmD6O4DR8qcMubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇶🇦
🇨🇭
نمایی از ورزشگاه سان‌فرانسیسکو ساعاتی‌قبل از برگزاری دیدار قطر و سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/92637" target="_blank">📅 20:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92636">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🚨
♨️
با اعلام ترامپ، توافق جمهوری اسلامی و آمریکا فردا در پاکستان امضا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/92636" target="_blank">📅 20:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92635">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H1Ga7N2ELdEovr9-_q-K1djhegLfBqvOYDzVzh3Cid7DXuphr1dV01GK8GqM72dgn91MMVE2LiALVM-swr-GdCwBXnFM1FhHQwbsQBLjWKQoukW9EuZn-xZ3BAWrPOd6AKcRzkOpNgzJenPlAiYm4VeQ8f-qUYZ6-8NdlOaU9fs5z7LOsI6DDGIlSNef7gtDdlnpTTBmdOeWdQb0rJ7H3kN-jxdFvPKlKCoy6FGJgO6G2m4Mk7n_VkQvMAhQu8XGs9VcvmtZSakdohcQizmp_DanZkSYFEmUsYHLRXGMxi-_bT9dRBC4Buil_IY6-aYF72vRRgeLpnmLKrYuYdcGwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
به گفته‌منابع برزیلی، نیمار در بازی بامداد فردا مقابل مراکش برای حفظ روحیه هم تیم‌های خودش روی نیمکت قرار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/92635" target="_blank">📅 20:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92634">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
🚨
♨️
با اعلام ترامپ، توافق جمهوری اسلامی و آمریکا فردا در پاکستان امضا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/92634" target="_blank">📅 20:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92633">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14d347ca72.mp4?token=STguFEELq-KbH7sqRkmzv8ZyqZWaRWtLrMOa2m2mYMxAYdZ1VVodaLeZc8j8cWz2UQ3vCiNty_3dQ-n6NdRw3jd6rXpWPJw_xunOr2rG5CWlJ5yHI_ainsUKi0cq_F2M3q6M-_VyIOMa8RrLrtgRx5607ImlNIlgtKxSeoAUrvcJq0Fkot5KFgHNXnZ6JQ2iOSxII51kaJtqjYdXKwFFliX7zHUJNP2UTZOitnLpSRNm9wjLSOakaJlP1UwM2IbxFkUhUAI9LpJT3_negixyef6hBVVjJbxdN-ny1e16CXyJvzELVQUbq2XdiGmuDIllzU-W16Fatvm5RyZEiUEaGjWrwFjFe02PBA1RPlXwShjMX8ONLAc8QaVuy-9OM1fhPHJmXw5b5oFq9a9Kkt5FmZsAkXgz5hNwY4PGPE_6bl0hIO_ix5KVQrkGvc6IvBOfzbKImG_BMjkO9isQKm5iBewDGdGn-doO5o5Sa92HChPq3RHTMdOfWEQeIkQKn9bCAVzTOP2ZSOWCEcLEtcYDwBWLZlIXfFeIjdWmFzsEYC9HibQPL4aA301a1e387EhF90lY_WAnlQah4sXoIi99sNjF4FPMs8yBcOTShlbrZ_eI2V_o4_5eL1mA--TE3WhxJuhKRt9J1iEkPFDfSkLkHqMx-W8Dt7rM9-k47pcUgTs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14d347ca72.mp4?token=STguFEELq-KbH7sqRkmzv8ZyqZWaRWtLrMOa2m2mYMxAYdZ1VVodaLeZc8j8cWz2UQ3vCiNty_3dQ-n6NdRw3jd6rXpWPJw_xunOr2rG5CWlJ5yHI_ainsUKi0cq_F2M3q6M-_VyIOMa8RrLrtgRx5607ImlNIlgtKxSeoAUrvcJq0Fkot5KFgHNXnZ6JQ2iOSxII51kaJtqjYdXKwFFliX7zHUJNP2UTZOitnLpSRNm9wjLSOakaJlP1UwM2IbxFkUhUAI9LpJT3_negixyef6hBVVjJbxdN-ny1e16CXyJvzELVQUbq2XdiGmuDIllzU-W16Fatvm5RyZEiUEaGjWrwFjFe02PBA1RPlXwShjMX8ONLAc8QaVuy-9OM1fhPHJmXw5b5oFq9a9Kkt5FmZsAkXgz5hNwY4PGPE_6bl0hIO_ix5KVQrkGvc6IvBOfzbKImG_BMjkO9isQKm5iBewDGdGn-doO5o5Sa92HChPq3RHTMdOfWEQeIkQKn9bCAVzTOP2ZSOWCEcLEtcYDwBWLZlIXfFeIjdWmFzsEYC9HibQPL4aA301a1e387EhF90lY_WAnlQah4sXoIi99sNjF4FPMs8yBcOTShlbrZ_eI2V_o4_5eL1mA--TE3WhxJuhKRt9J1iEkPFDfSkLkHqMx-W8Dt7rM9-k47pcUgTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇲🇽
هوادار مکزیکی که برا ورود به ورزشگاه رو سینه‌هاش پرچم کشورشو میکشه
😈
😈
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/92633" target="_blank">📅 20:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92632">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkEasbVF_xpMT8-MrBRsU6BEyQacmU8P6D-UD4-4y9lk2ZfXEQCHI2i7r3_-Vp7uRyoMSEndARlDzh-T1knizRhS89i231xgbVW95vPt5l3142oSDrb40DD6hw9cdZAkhA4QticdKnd3YlJJMHWqLgdNcH65cd4LAgyi5Sg0gEEli6IyVNmmmJ_Y2rbNJsucj7zTNu6GXEWtUcOgDn0Ks0LOK8vJ8-E2y_R6v6Jh12k2xFzuWhLX64SMNZN0vESn5Uj83EeZJz5JU9MjkPWObO3UL1aj0-WRaJztF-K0EwUd1SZBS29zx7-DAwKGHzZliky2tSXOSETk5CX3KCWQtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇩🇪
🇪🇸
🌪️
شرکت آدیداس برای بازیکنان تیم ملی آلمان و اسپانیا جلیقه‌های خنک‌کننده ویژه‌ای مجهز به فن‌هایی که مه آب سرد پخش می‌کنند، فراهم کرده است. همچنین کادر پزشکی و امدادگران در زمین تمرین به طور کامل آماده‌باش هستند تا در صورت بروز هرگونه وضعیت اضطراری ناشی از گرمای شدید، اقدام کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92632" target="_blank">📅 20:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92630">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eX6sgEEaywc7KqxTuJMPK62uTfIgGvFcQQkGI2bMep5X_Tt7IwMMNHOup_e8hRcvDNpM8uKgN5ICTWM1bYGTo6kK6CfWyL6nxbap0dgUa8EI6eedSsb5Zb_totL8cC2EjUcgNHXLG44OpaXEfhR4vxy76lytQT516g5SGAkk_IHSL84NRA0LWxlDA2osAU_AbEeX7iStDTB7mpacCeiEM4yNZUE285HM6kRfB-0AOmflMDIyRZ6B4envlncbjcCmq_qr6CRBC3eyszwPmfoepgvtXdEcIezWz8q29typl4CRw5Q_FuHnnq3qkguwpsnD8DRuFVh3brSNHkYvo2bavg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووری
؛ رومانو: لوکا مودریچ از تصمیم بازنشستگی صرف نظر کرده و اگر شرایط مناسب باشه دوست داره به فصل دیگه در میلان ادامه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/92630" target="_blank">📅 20:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92629">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2a7ddedc51.mp4?token=fVZntnMWdbAlU9xnlLz2ZIIf3GHS-IY3PftvTU5_veHmG5KYjv0riJJM7QEvFv8qnokv7CBeiNI2pyanS0R2dzQYL28lwMhbEkdDzW_vqRdMNT4eviosGWP4_AJYeXylK9E4x1PBl0TVjESn7zCoU4qiuVvCfSiSo8yPUcdr3eQpt8K-i2nt9p07jQlXQwLQ__aG4r3TmjGPmZnIPqX-XX91LN1SKc8AqsJdsYans_oFAW5b0dj3iC8qM7KnPC2AJiSSI0Q7in3X7h5M1XCXeE3wPN_aAVi4TrYp6DwegLNKeQmZu5oeRhU_PiOUQTlXciaFEHss7mUo7HezsROI9AQgyhQ78fc7SJKXAPRB8_yGJxacNLZbJvzP4R0TyAftnnqv3lnr21upJrOc6SZqOJy7Thwt28Wvu9IxLPmp_qUDyym8S-jRFtD-xKIzVDXYqAxXguPP3GB65vSU9N37ywCBYRJsHbt7FRctsIUR8ONbeP-reVCH9e4EkKcfrviHpNO26mm7w2cpc0JDr75fAwbGoXKfzGXBZLgbdDp1vYUsmFc4qXjelGafrnBToAt0KseIZVSJi5DHIMnNLGeNTFsLRdP2tKnj6z-iA6Zkz0RbHOGjdzqB1UvNx8FjISli-XONK-K6zFJ2fh-kHCt7eKdriyaG3RGO5QvhAKGLOM8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2a7ddedc51.mp4?token=fVZntnMWdbAlU9xnlLz2ZIIf3GHS-IY3PftvTU5_veHmG5KYjv0riJJM7QEvFv8qnokv7CBeiNI2pyanS0R2dzQYL28lwMhbEkdDzW_vqRdMNT4eviosGWP4_AJYeXylK9E4x1PBl0TVjESn7zCoU4qiuVvCfSiSo8yPUcdr3eQpt8K-i2nt9p07jQlXQwLQ__aG4r3TmjGPmZnIPqX-XX91LN1SKc8AqsJdsYans_oFAW5b0dj3iC8qM7KnPC2AJiSSI0Q7in3X7h5M1XCXeE3wPN_aAVi4TrYp6DwegLNKeQmZu5oeRhU_PiOUQTlXciaFEHss7mUo7HezsROI9AQgyhQ78fc7SJKXAPRB8_yGJxacNLZbJvzP4R0TyAftnnqv3lnr21upJrOc6SZqOJy7Thwt28Wvu9IxLPmp_qUDyym8S-jRFtD-xKIzVDXYqAxXguPP3GB65vSU9N37ywCBYRJsHbt7FRctsIUR8ONbeP-reVCH9e4EkKcfrviHpNO26mm7w2cpc0JDr75fAwbGoXKfzGXBZLgbdDp1vYUsmFc4qXjelGafrnBToAt0KseIZVSJi5DHIMnNLGeNTFsLRdP2tKnj6z-iA6Zkz0RbHOGjdzqB1UvNx8FjISli-XONK-K6zFJ2fh-kHCt7eKdriyaG3RGO5QvhAKGLOM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
انتقاد شدید و عجیب
نبویان
: من خیلی ناراحتم این چیزی نبود که رهبر پیشین گفت. پیش‌نویس توافق بازتاب خواسته‌های آمریکا است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/92629" target="_blank">📅 20:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92628">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhTH6Y2xzHmx9tm20QfhmVeInZL_K8Nc2KSByNiiqINsewmEGqtVi_w0Q9Hy-iFNCXlYSRC8r_prKn6t_Y8faLTQoqMZvfgS-pCN0S5gDoMSiGAU6-fnvn1giHp_SFlNY2_fsC2HBEczk-R16shnIIomkB_cLUf-iAvhWIAasPAuqzueU2KUYKwePrcwIK_dkpnjeI-f3jDvkkGDdqaihW705_SwYlMnKWTlypWJa-DNi7BrhZCyq_Ju0pBGFruviYPreHxWnrRSiu6d8gQuxtKGoLzsl2RzL1ygdE5NPFh6-uZQ9XYe7ePoQHj8XL4Ocl5V9TAIYgD3ARtcFuJvSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
ویژه جام جهانی ۲۰۲۶
هیجان بزرگ‌ترین تورنمنت فوتبال دنیا فقط داخل زمین نیست… بیرون زمین هم جریان داره
⚽
به مناسبت جام جهانی ۲۰۲۶، یک پیشنهاد ویژه برای همراهان فعال در نظر گرفته شده:
📌
از ۲۱ خرداد تا ۲۸ تیر
📌
هر روز ۲۶٪ بونوس روی بالاترین واریزی روزانه
یعنی در تمام مدت جام جهانی، هر روز می‌تونی با یک شرط کاملا رایگان  وارد فضای پیش‌بینی و هیجان مسابقات بشی
🔥
🌍
از روز شروع بازی ها  تا فینال
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/92628" target="_blank">📅 20:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92623">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DIsrwLPMntSMhY5MxRMHDMLB_JdSUb-_KLv5gaq3-G8VOMYcyVaDZKHrH6Koh2JKB-2hCYR7cADETCbPvCeW3-r_lisB6ybELU2NykMa54OPHpsDmZUzgDt4BfURrhKXHzFcXwkXbRCUrkqpI_XgP9UkF1W8oqVw557ghZj8xaZhzlaM09yDdCTX4NAJUQYzihvgfdI1TI6RPSYKI--AdkEga71y4b-7dohA17chdkJdefDI4OF6Iw0T5C9DfGEc7K1YbyBEF61-ZsDLFgg0_WyVhKPzHx9kbGumw8hejiZ7f4kN4G87VKWuxD5zV3GiK1DfizdoXpykMeCYkg9JVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oJaai3hPt68LQVt6n6tSO853yWfyko4hg3oJ45TIqBptIePocOyVOsUp-31A-I9GSNAQh_iJKBtq3pi-Jb9ZtYTteMmibZJLfgJ-0qzUTQkBqBPcXXmmUvSXlRNmpeB0rFcy3AvQ62mF3vheeoZJ1nJY548qqNXi56ZnaJSzjokGhpH-qXzcCdrK7So2TAKuNftudppU7Uw3lV_6n0GlkdKTvqy9R1WW9ErWMlj3xxZ5ymBVzyv1aj5FqAOOVN4vQ19WIi5eQzEK_EUrKI4RmFJhXbb4A8GlSnVBBncXhJiLClVDlUB9CPsvozkgAGT5ualqmvsKgx3XRWEmktu7pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇲🇦
ورزشگاه مت‌لایف در آمریکا با ظرفیت 82500 نفر که بازی برزیل و مراکش داخلش برگزار خواهد شد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/92623" target="_blank">📅 19:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92622">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbT-eki8aGzlDWBL4Mrx_KShuMQxg1yL2vyVQvkMkMXUiHE8RwRec2Zsii2E8talsMQbQdtaFX6UjPi_MqKTZ3TYgQ4V7vAD0PzdM4DrTWvAe82XSfe_QCx0MUwhqju84Oz0igRQ8sxVZCnkUFymIzeHXTw-55y5-4MkYH1ZQfzy3Cnnvgijp6K80Y9lgPvjrg6jRsUSLe4EbEguvXiWehFx6H3VOBGguHwWbqNfUDx347H9mraFmaEt1rYTlOHzEm4SUXrB3d1s3l2IjUIbi_J4qiau8Z5oDifeSStyAbDh_tGZvahXJETNh0P2sO0s_H949jP9NXkoweoxYf5hkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
الکس کروک:
برادلی بارکولا درخواست جدایی از پاری سن ژرمن رو داده، لیورپول و آرسنال به جذب او علاقه‌مند هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/92622" target="_blank">📅 19:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92620">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a5c97851.mp4?token=MFQ9SMEUXLxOyTbePsB_bXIaOqBcWKj41wNL0l0IsCLCgLdVZNHMiP5Ta0eI6BGCb3HrGSZClZUczFZ3Oa4TLS6Hfco3IzU7xxKUq1XUMzt43HzH7pScXXBNLfX32MeTiAWv-SDS2lch_kmepx6V6TdsYVsbA56s4RdiBBWJdMrOIrCyklQUo0Ui6jKDjK1_iRCgGKfuR2PkQkEyzE_oQvscn_KijYRR6-JT2fwhkFLd4tf0NnHdWJlxeWY7GUn5qbKg9w5dOzGl8gKeYoSL89YHTbnpqFqcorNzvCx73Qo_w8lV7M88R786hHYZBuZsZ8OnUSMg--oEB1o5w1lXig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a5c97851.mp4?token=MFQ9SMEUXLxOyTbePsB_bXIaOqBcWKj41wNL0l0IsCLCgLdVZNHMiP5Ta0eI6BGCb3HrGSZClZUczFZ3Oa4TLS6Hfco3IzU7xxKUq1XUMzt43HzH7pScXXBNLfX32MeTiAWv-SDS2lch_kmepx6V6TdsYVsbA56s4RdiBBWJdMrOIrCyklQUo0Ui6jKDjK1_iRCgGKfuR2PkQkEyzE_oQvscn_KijYRR6-JT2fwhkFLd4tf0NnHdWJlxeWY7GUn5qbKg9w5dOzGl8gKeYoSL89YHTbnpqFqcorNzvCx73Qo_w8lV7M88R786hHYZBuZsZ8OnUSMg--oEB1o5w1lXig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇲🇦
یه هوادار برزیلی اومد برا مراکشیا کری بخونه که اینجوری طرف مقابل بهش ریددددد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/92620" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92619">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P44aR6Wtp3DgS_2c3IXb15YEL8Hp6LhIwQzyCd7b7JCYnjE45G8VyPgbOsrMYDtwWw88B2zuAd6Ys8bqEV6bwYqO0l26qpVl7-9KfxGpWp6Iza3I6kBYPcBo6rm9fPY1DQDgf1QH4AdTWbeAEnL5ct0pPlDCPf-xSEBxrFgqkN4JS65OI96tlppgO0ICaZfnfQpW4OV3bf1LQAH-aR-n97TaDmoJNTLE-apWjdtfXoaJtjLmZU68Ti8KlpviUIZ_fpUvudcWeB6ZhYzm0CCjl3fyb5F91OUOLoLtIjFYmF8YpvacL6nxGjO_wzRttet-eSTbdA3p2k4sJPTERtYq0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلو آنچلوتی: «احساس فشار و ترس خوب است. اگر بدون ترس بروی، با شیر روبرو می‌شوی و فکر می‌کنی که گربه است!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/92619" target="_blank">📅 19:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92618">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdef04be15.mp4?token=PLC2kwTa00oANP3qqIqRAR-arViQJEW7dYeqPV9YUohWCtJ6L97qDf1k9RtQ8z2D5vrT87m6zMU8uD8MnhF8jxHJfj0ejt2kmOMPAl6uhvclObWCpODAXuEfLyPoTjBDTJWvTrFSPlXaBlcSQ2CEKZJesNjHlXJQOIQUU3KWqtNI6huzDtJVeng2makpAZdURt_qhJzSqg2pz280FWkFBOAF-kP-fJbuumQHSGGLQuN7A26s634Vd43f3VTfBcc8rxqWEOTZO5CteJhhymZEUFUhm_3wdnciq5mUMnmaOyBHp9gFE0FwP10MlJqSBYNvOcN1l6VD2F52JksuqMXOvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdef04be15.mp4?token=PLC2kwTa00oANP3qqIqRAR-arViQJEW7dYeqPV9YUohWCtJ6L97qDf1k9RtQ8z2D5vrT87m6zMU8uD8MnhF8jxHJfj0ejt2kmOMPAl6uhvclObWCpODAXuEfLyPoTjBDTJWvTrFSPlXaBlcSQ2CEKZJesNjHlXJQOIQUU3KWqtNI6huzDtJVeng2makpAZdURt_qhJzSqg2pz280FWkFBOAF-kP-fJbuumQHSGGLQuN7A26s634Vd43f3VTfBcc8rxqWEOTZO5CteJhhymZEUFUhm_3wdnciq5mUMnmaOyBHp9gFE0FwP10MlJqSBYNvOcN1l6VD2F52JksuqMXOvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمامممم طرف عرق ریخته توی محفظه شبیه گوشی
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/92618" target="_blank">📅 19:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92617">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxl2oANwc02-qlm1MuEBXPrljQYgmJM9oo1hx7o14-e0tBWXV6fpP18aetdvK28spsgLiCthTLUltbAhmFPfDtnCx52ElmId9y9xOuUIgpWDXLfmNcurchTFVm8qR3qCxDxlV0OrLByBAuB4Cva9coOjBZ8nGN3UbfJsuzonHekKLtYZnj2ORVB-he3A3Ro3ewbBh3gKS6nLZPZxgsu-4ij-WNa0KwVOTXPv5i-1xwBJYVK-XZNQb1vsg9CIu33mipAVu33hA15z7qxzMFxfLjNzqsBstIFJgkcVRx3BhNcLWxHjR1cR9PbPmTzjNBkZL0Zhiy4eFS82Lkpw-fhiJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید بکهام : انگلیس‌ قهرمان جام جهانی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/92617" target="_blank">📅 19:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92616">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🔴
#فوری
🇮🇷
🇺🇸
🇮🇱
وزارت خارجه پاکستان رسما اعلام کرد توافقنامه فردا به امضا خواهد رسید
🔴
@Perspolis @RedStarFc</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/92616" target="_blank">📅 19:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92615">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q55bsOc8WIv9xNcZzcj-9SvHaak752S8fbjlUBD_31M0Cmd5cHol0PP3sLSTnIiByEeKGGk8ulyefPmqA6MDB11zNiGhVwCTkZg_tGYZDAGa7cWwl3D3qhTpQ2D7t8qULGUKH5UVAiELwIwJhQvs_TKk0sWhJ83f4D7JfWhs-j4n8s0kQGamU4us-ShA2GEu3pWUUFcI1vCuu00SWQnYyBNABNTG0JN738oBWd41IiUkMoJebMTpDYb5oQVgUKv2WZRy9RzkPa09IwMvyHeKX9IPaoYl-R0CTfUPxqQP0fjJOR2qTkRpHPPl1ibe1BLDXiBt1YqwQnbxi5HsY00WYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
‏تو پلی مارکت مردم شرط بستن که رونالدو تو جام جهانی گریه می‌کنه یا نه
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/92615" target="_blank">📅 19:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92613">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWbXgb8Yrnl5XA-MYeELi_-sXrZkfh5-VYVRIsiH9tOQSJmJbOg7_Eem-lcOidqo7gH4TFrvajhcb9gGZ_4sUwyuFNnsr7Xq69nsNOnurIDfl0T9pADIfFIzvrI-MG89cKvTaOW-mxd5TSqOp7Rp638V10Pu28kpnLfYNk-lj1izS1OLuoTLA0S8hKt5ckt7Gx99sZG_E-XLw_Ntx0_LvBm_ibjKygmMuWkkG-bKig44pfoQMFRwFxqq6h4M0CN-r5T3mI_-k4f3anL35Mx0ZDkZYkJ4gsueYZy1bFWTt34UkKhg21SqwtJDz-9Vc64ShhwvuXJUeczvbAz6f30djA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
فابریتزیو رومانو:
🔻
آرسنال بزودی قرارداد آرتتا رو تمدید خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/92613" target="_blank">📅 19:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92612">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXH4WuUFATfvpEumxGpvO80XZTzO3ElvJXhdveC1vaBy3r6-NneITGtwq4UETDXefJ2t-tSU6QoNp8PeyAUZY7iKfjJHcILK9hs_TLufEECDfsQgPocSLmbl-JhVifqKjXj2GZK9xFVcMvDJOYLKaY-JS9X4eSIePBy52veOz__Fgwh7mfQPOn8OBVWW47deIftSl4m5XmFjEcoH5HuZSx23pYic7scpRNZ46RKvB5oyVNzn-9FgF_LnW1WNpYXKMrNHNWEHtON3j9wxPSBk3xQrDnjJHIm9GstDUjlCxa0i7XuMw0IEBiPcuXf9NGZS0LnJyBJm_gSTexS0D2p6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ماتئو مورتو: آلوارو آربلوا در حال مذاکره با فولام برای سرمربیگری این تیم است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/92612" target="_blank">📅 18:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92611">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8848bc0e2e.mp4?token=V9-V8Vca67aWLrcwXk8wqPnaJHTb4Bos639W-QhsELtHGrOTQkbZ9lX7sjNZsPd9UbvOTmTPDE9d3Pg4w21bU_zCL2sEDjRWIBDleZFxrC6Jo6aE-HVgKom60JrJfjgEf3fAFoaWNpPYj0vx1nL4fdzxPsb0HknO3o6lu-BeVh1KM-gsQi7YMcYzkkYinFRmuC27mhHlUJ3yp-awiMazdfwWFgLGD-rVlbx5gUw3yYQ41mWV8PpCG50hfjoj2ZTZ5d6j-13EWUMLvAUdIGt27GuLE37ZqwUSx_ORKm7N3U98BB1UNkhJqAUcfehNPFI-lWERvpMbgqjzIq36oZXd-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8848bc0e2e.mp4?token=V9-V8Vca67aWLrcwXk8wqPnaJHTb4Bos639W-QhsELtHGrOTQkbZ9lX7sjNZsPd9UbvOTmTPDE9d3Pg4w21bU_zCL2sEDjRWIBDleZFxrC6Jo6aE-HVgKom60JrJfjgEf3fAFoaWNpPYj0vx1nL4fdzxPsb0HknO3o6lu-BeVh1KM-gsQi7YMcYzkkYinFRmuC27mhHlUJ3yp-awiMazdfwWFgLGD-rVlbx5gUw3yYQ41mWV8PpCG50hfjoj2ZTZ5d6j-13EWUMLvAUdIGt27GuLE37ZqwUSx_ORKm7N3U98BB1UNkhJqAUcfehNPFI-lWERvpMbgqjzIq36oZXd-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پوچ بال ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/92611" target="_blank">📅 18:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92610">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ac29a7f7.mp4?token=BHwSURqjBC9ayDwjmXRdVvQU0EBGDPK9CrjK5lgzEP1NHB98boqzT62Lzd8frPdBPx0oh0_OgOptnXff7Hl-6X5t9iM-bD4s_edTTBUdNQdOtkz41FdwKu0qC73hW4_gfldGfyQnxtw7s9TgF5-Enee6uW2HdxMi93OcFlS87UIwItEtxIEmztD_Xej4t5MOyyH6R1cUYveeGqawSn53sYNdAG2E2tmq7kltfWufNyUJaUdg1YqK2rHL4hvArEx1KCKhpXgoqypd5rg8xaGVTmpsqGu6ziRRZSbqShdc_Fi5nO03xg86vUe3z5ooo3ybmdjzgHGtL-oHdQAdl1t_PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ac29a7f7.mp4?token=BHwSURqjBC9ayDwjmXRdVvQU0EBGDPK9CrjK5lgzEP1NHB98boqzT62Lzd8frPdBPx0oh0_OgOptnXff7Hl-6X5t9iM-bD4s_edTTBUdNQdOtkz41FdwKu0qC73hW4_gfldGfyQnxtw7s9TgF5-Enee6uW2HdxMi93OcFlS87UIwItEtxIEmztD_Xej4t5MOyyH6R1cUYveeGqawSn53sYNdAG2E2tmq7kltfWufNyUJaUdg1YqK2rHL4hvArEx1KCKhpXgoqypd5rg8xaGVTmpsqGu6ziRRZSbqShdc_Fi5nO03xg86vUe3z5ooo3ybmdjzgHGtL-oHdQAdl1t_PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
ابوطالب‌حسینی و کنایه به امیر‌ قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/92610" target="_blank">📅 18:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92609">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
فوری؛ وزارت خارجه پاکستان رسما اعلام کرد توافقنامه ایران و آمریکا فردا به امضا خواهد رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/92609" target="_blank">📅 18:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92608">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CltuzjB0pBDkfzp_Vz0E8Ajv6_Mx-oxiX5uyv8xvIOSwGRn0KjFcwk-sjh2sI0kvzlyKV3xMbwIac2zp860oWiZOXjWZEUvcRCUHNyhOi2XFkYpPiP1M9sgpzIid4dMWzqYWj9SWgIi2L20dy5Twoof0YQFs8mCXDRWb7Kul6ZUUnBh8GWINgauMT35tIJiN4RLTX5GYlwGlTZK-jrRRQVfOrXjvnZEt4vGnY0bU2fszNb1EcaGtryaZVzHAjftUHyJxaMi2F8ebkF2SUM9VUgIU4IMw20OVmSMI--UL_6TcwdrgMcXXrwyahmPgHEdCd5YKEiql5FDoanV3eth_Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
بیشترین تاثیرگذاری روی گل‌های تیم ملی بین بازیکنان حاضر در جام جهانی ۲۰۲۶.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/92608" target="_blank">📅 18:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92607">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_t4jQ4vI8I6ZBEESgi-ZhDhWPf0bzP_9eS3Km7P5MX7NIj4pT-v2OhuOHDZq-vVBIxMyGO2vdbNfVgX4-RubG0ylejS-l7GfpgfkVyR3wwfL0ND-6W9tzsIUvDgWHlcsB6RVB0mz1RD6hUsCIwXWK7ttDGIVScC0gnrYO_PQTkVlKU3DctWMAvqho8WDsiWeAKxeMH0pTzZHqjsVXMjd17nar29gkpEK2Vwt16DuECq3yMlxd5KzrAraV5LVZ1Abcabyg0vJ33qVvBm-vzHAVVvj3w1FjSo982wsvKJzUCS9mKmZJfIAoPLOe1wijnTWGidlrKO5R1kxJ4Faq6ZLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوستر باشگاه دهوک عراق برای یحیی گل‌محمدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/92607" target="_blank">📅 18:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92606">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mF4uamuUmClaPie4lYgycoCZmu05fBHImCOR7dsfksXvYnfqIDLvsrcEqUgPQOtLz9IwMkHn34jcixnDCbsk6q7Sp3eUksfzMv88WkZRGlDpjpZlY1Ed5V1Dgc6Ni5mvn3bPlZ02QSvQa6qrQnRuRX7YvVZAVT83jyoXBLHA-zbb62aFM_h-4KdGqxiYUgw5OPZEeOd-wSmv_hZtYh0uSchRp4BToYmiQ9yXPkENb2KLBPc9KmXdx_wkFF1SktUsaB4kgo-GiDTYbf4i5EG9NraILTHXXUck-bATQrZFYVERDg3H_oW1gQ4WgLtnuc3bxlL8DTPNPqEasWuXhNegDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
مائوریسیو پوچتینو:
رئیس‌جمهور ترامپ ازم پرسید پوچ به نظرت میتونیم قهرمان جام جهانی بشیم؟ منم بهش گفتم: چرا که نشه؟آره قطعا میتونیم آقای رئیس‌جمهور.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92606" target="_blank">📅 18:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92605">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMyUeMatdtworXhoo7mHEDzyt-AFoUsIj-Sj9rFbtQcAUdhAkuc4enPQwIPz9uhBprBY5qQeQWTymgO-S7njOBTBaDYkVNhkF8AmzLbo07m1gnLIXu_vQAvsd7SDzHkhBZe99fjbvTw-euqwE-4hg0ini-7bfIrwOgoK7o2tCCoQeL-qh8_e6ufCwJx67Bb_4FD0QZ9UaEia3_MqeA-0IOXDVfmT3KU95VVZEmJznCyYNghatIkC75SLqF6vDiXhJisOnr85X96uhq0w31_4rqd7Xx8gW2wVUh3-sHGgoUuCXMac1t_3aVChh7ECpsLRwgFf8ni1FGI9QdV6cxOofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر زننده اولین گل جام جهانی
🏆
هستند
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/92605" target="_blank">📅 18:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92604">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_JNdyjM8D_QO6vSbKHqpxtx61TSGBbgxcsvxEH23Hx_y9ecVYyYmWkEk7l-fUytADwyHjGVftbHtLjDt7rcf0Y2w_BpQpGIHLFeAmHVLTZ5-tZC6FCcBzmp9u7CiyCb1mdJzbMJw2kaySs7xVEcC7paRzyJIHB4p3kSavR2A3ILk5dAmoDsVkrkmgXlFZE2l5D7e8F0GkmpAy4juNzWMDeqE0r6cKSBMdrj7OjRhvzDPGzs5KgLmJu32czRqBsr8BNtaR5Qyvj3_J33gH58h5HIA00OkEsnLXPI9rEqGfS8hthv4QhiRHNz0U4mljVN30hCWqVER5NMJSYREDm0mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گری نویل:
همه درباره استعدادهای انگلیس حرف می‌زنن، اما ما فقط یک بازیکن واقعا در سطح جهانی داریم و اون هری کینه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/92604" target="_blank">📅 18:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92603">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IisWXp45ncgP77ZI3QkUlSsBXRTNnx2pxf3p-jbnbVfecZep589rR4lE0taR2ucUIl3oo0znWKv332VJ6tZ-KKqyn89gpupEspCJ6yeru-KFFCNIKa3r2W-TdG_YlDVDXQ6ZTaBCwcQZl4lxqZZ-kao5jIfR5jjmgDETa_s_qSi4uSddzn7gyD4IQAFOXgnLTg8G0914e8n93TXv_V79oARvorOl1Ksa-zCi2TocH-AK_5848UOYNWjWutBd7H6wmQpgS0n0BpOf5E3J5d1x0upe5_NhQ3zwxTAUITVIiaPL8TT1MFCoJSNGQk7RgTv7E-zPjrFDPnIdwhA8sUfQHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🇧🇦
درسته‌بوسنی نتونست مقابل کانادا برنده بشه ولی این هوادارش عجیب چشم کارگردان رو گرفته بود
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/92603" target="_blank">📅 17:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92602">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb924a92cb.mp4?token=DuMdLLlR7uJX0OJ7GPiQVmimGMtXeZpSomsDXMAd0H1g7RFqbkylKYTtznPtNbEOgRU2JFs4Q8DAkW88AkWpW7jLvomx0tz5sJXmrltRDfEfu5NZeHn7bU6Pq7yfJwCkHVFd1EisA1727CXBhN7bYmiF-tta_m3bQcbXV3xAsMvxPZpgvIEGcxhhFuX8-CSzzhXYPONzjfeF3sMIvHWj6udKd9dlohoWGhzLKhdHee41yxoWtQ1nvL2XqhmpC1IXg3rlCIUVFEbiJvI55tID-sKUj0Ti9vQJqDKb_tYkBCCCioGgPkelA0H52spzLjNepuJji9u5HtBP-urwbUSYRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb924a92cb.mp4?token=DuMdLLlR7uJX0OJ7GPiQVmimGMtXeZpSomsDXMAd0H1g7RFqbkylKYTtznPtNbEOgRU2JFs4Q8DAkW88AkWpW7jLvomx0tz5sJXmrltRDfEfu5NZeHn7bU6Pq7yfJwCkHVFd1EisA1727CXBhN7bYmiF-tta_m3bQcbXV3xAsMvxPZpgvIEGcxhhFuX8-CSzzhXYPONzjfeF3sMIvHWj6udKd9dlohoWGhzLKhdHee41yxoWtQ1nvL2XqhmpC1IXg3rlCIUVFEbiJvI55tID-sKUj0Ti9vQJqDKb_tYkBCCCioGgPkelA0H52spzLjNepuJji9u5HtBP-urwbUSYRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🏆
کل‌کل برزیلی‌ها و مراکشی‌ها‌ در خیابونای آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/92602" target="_blank">📅 17:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92601">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">از جام جهانی تا لیگ ملت های والیبال ! هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در بت ویژن در نمیره ! فقط کافیه یه شب از گلچین فرم های بت ویژن تا استفاده کنی تا ببینی چرا سایتا دنبال ترور ادمین این چنلن بیا اینجا تا ببینی فرق ما با بقیه چیه
💸
💸
💸
💸
…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92601" target="_blank">📅 17:42 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
