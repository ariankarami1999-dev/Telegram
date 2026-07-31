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
<img src="https://cdn5.telesco.pe/file/Z94rPtLCt9ntGAgePpfzjchZ_JqVA6gFLKnzwPb3nDFBUWn-8CFcOZ_hGqrI7v92SHOaH-haX17CN7KzjNTijwlSs4YdsIVsMgf2g0igPslQW_M0LlyX129bxZSZBVK2Yht-qWqOss4w-810z4Poit7_Z_wMMk4kJG-_09YypHEYvGDsV7x0wUZRe7zAMPcSiPWSpw4IsTgx9XLrUnZ8AB4XLL4Yovm9GtZ96PABwTcU509d4HPAGs4ff9FSofaVf-33dgWpiEtMG8HA_sbRNFCediNf8beyW7P1W1OoHqb_pnxrWvwv7yQGyGw0VTc-gMmiDhXA52vyY6FOzIDu-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 508K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 20:50:37</div>
<hr>

<div class="tg-post" id="msg-102461">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=FJjh-TZXDgnf3E5VYZbRvSXsl63DboUaVzRP6v6Wh75ES1Ff_8N88r7Aw9R8fZwwMUtOmwvwe6onb16eDZdNs70d_6mQQPzq2JXnTE5CX9DSWL1pgMFdTFN4lgZBSySOyetjXvCooZfviB1fSky02mUVV5rUzSTTQyVl02p3EzH_XrIxABhgCzI2uCQNLvf7pVKZdjwmZcpe6LixHIHuWkVIPPHG_wDDnjG3mew_-TGzxtrKEOkrYiYtyvMIYWkBP_vWv5W66GP2FTMVNTMqr_7V4cn9dlcjrNvU5g2sa6mb8Jsm8TsPAStlIroctrcTh8GpFU_HMeTC0bZLrma5GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=FJjh-TZXDgnf3E5VYZbRvSXsl63DboUaVzRP6v6Wh75ES1Ff_8N88r7Aw9R8fZwwMUtOmwvwe6onb16eDZdNs70d_6mQQPzq2JXnTE5CX9DSWL1pgMFdTFN4lgZBSySOyetjXvCooZfviB1fSky02mUVV5rUzSTTQyVl02p3EzH_XrIxABhgCzI2uCQNLvf7pVKZdjwmZcpe6LixHIHuWkVIPPHG_wDDnjG3mew_-TGzxtrKEOkrYiYtyvMIYWkBP_vWv5W66GP2FTMVNTMqr_7V4cn9dlcjrNvU5g2sa6mb8Jsm8TsPAStlIroctrcTh8GpFU_HMeTC0bZLrma5GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شزنی جنس رسیده بهش و مشغول دلقک‌بازی تو تمرین بارساست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 307 · <a href="https://t.me/Futball180TV/102461" target="_blank">📅 20:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102460">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=tgSDTrUn6R3D9BeGCHW1lFzyWUgh-hPKlwxh25tpNDXUho12_a5xhoUFAiFCT3TG4vprB-eNoiJeKsMeC2myToABXPpKS8RjrdiqyCrOgAizW3t7G7OxORK134_4UzCdp_3RE6629A2-jcS6Q3SzY02UEa0Bu3wq-53dAIJJuObhdxOhNZ_E0ffUgmcGIELUn3PRx4E2Gkp3U3l1O9JFF7yYR3TdpxhFtclbHd9K2KoyHxpEr1SfCZz3eqqH2d7z7Q5CbdWetz9-JA3Ho2coxWZb_9mdmK0pCAITgIeWB2PQ8gxRn-Xg69xqu8VFlXjn6FBdhtITDwXk_DOdYIRuYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=tgSDTrUn6R3D9BeGCHW1lFzyWUgh-hPKlwxh25tpNDXUho12_a5xhoUFAiFCT3TG4vprB-eNoiJeKsMeC2myToABXPpKS8RjrdiqyCrOgAizW3t7G7OxORK134_4UzCdp_3RE6629A2-jcS6Q3SzY02UEa0Bu3wq-53dAIJJuObhdxOhNZ_E0ffUgmcGIELUn3PRx4E2Gkp3U3l1O9JFF7yYR3TdpxhFtclbHd9K2KoyHxpEr1SfCZz3eqqH2d7z7Q5CbdWetz9-JA3Ho2coxWZb_9mdmK0pCAITgIeWB2PQ8gxRn-Xg69xqu8VFlXjn6FBdhtITDwXk_DOdYIRuYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کول پالمر:
برای بازی مکزیک - انگلیس بیدار موندم، ولی بین دو نیمه خوابم برد!
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/102460" target="_blank">📅 20:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102459">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhtgBuSIVtECjWBENH7A2P_QF9ZTv2zzfC_ePoOR3zayZBlpak5o-kPqYxdYgMVp7_veupnruqgUugWyGBoWTXDJzgzIzKYJS6NqxdaSnghR8MTM7hN1vGRnZBgcYHKf5_d4Y8U3eXQWfo4OhilodFvs11p-vsyE3KphQA9zEYkA10hc-0D5kDeZfGFVHwiuFnunDrU-BoYcxaSmVDYir_kOmTESPxbLX2c3kBXqTBbFjruauuEGdtbOUV-F4F_QslPQKI4cSyDzOcnKg7C42iYwSw6LTmxL38RpagxcasSDKH3dWInrY6AmbLVB8nf0vVIv6YviSTVevCW4EU6jig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/102459" target="_blank">📅 20:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102458">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opCd1VFSW15xEgcBW6YJbJknArSUXy7EfzriyoZgcGHCxAAQyDLN5fmTOWq7XP_eYopItp4D2hBMp6f3CisT8MZXN8p95nY6JwYDdUYovURFgiP1zeuif_pj1lMr4mGlTgEqMhzLZlmZx-Zc8smhmwRcS5rpNgQT9rQJxRh180RD3mAVXATLwtC9wid0TQmRdkinHPIjuD17_o-_8uSCj_nKM_wSYljcYPoG9Tz2FTC-HRs0_T9oBksJuXC6Lw0YQp2t4i3NkNesZ1EswVBo9x9ztUdWZCdTnmp4Xur-0ZagijAVT7bAd2Tx3P-ajz5X83zsez9-fx8pIOw2C7ErOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
فقط سه بازیکن توی ۱۰ فصل اخیر تونستن در ۵ لیگ معتبر اروپا هم بیش از ۲۰۰ گل بزنن و هم حداقل ۵۰ پاس گل ثبت کنن:
😀
محمد صلاح
🇫🇷
کیلیان امباپه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/102458" target="_blank">📅 20:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102457">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4HqdcUXfQm1v0M5NiPy9CDp9c4bkVvrYhaKqcrPOcD38jMrt1me9sOF7dBVQp-gVmGhorfVCZeqMkNzgxZ1Nl2-GnecM9lU-EEqe1v1qimldDYj5WUCLpYyxJ3rihSPIcF7lZoU9SLlGw5OYVWBX5i_Jy-7BXXN4Kqnfw7qN39qVGKoOn_SVbtkkDni0z921Enw9ooGrm1Js1Pa6cDyMFcEpAsq4GxhsHt49IsOXSizHgNTWN1Cm8Xh0n-mOzlYirBq6a6RAomLVQn91FBa4jH66VW4BSLqJ8LYt-vneeCrtGbukI0pYfzqZ1XEQHvFYK_EwfLO-QbZTcKej_OG4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/Futball180TV/102457" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102456">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/Futball180TV/102456" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102455">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1OiiTiAzpQE9z4tIIarAGBsZLubtLzpzz_gtv6oPhGkCN4pEZH3PD6MYw4nVFqPiQ3p5VXqWuMJdcYxcqdVeX0hD-mP9FLqrJSHep6qfCIRoIWKtEZfTkusblUSmSiAdQF9om7Pnq61dFKGbkjjL3aQdLPqzlf6P6eAzqIoWqAWlilqGa5c_cETZh0z5EwT4YDPUjSwB_mcrt6Db0WTWncBXqOsKdWy84KqeTxYlwy1EhXzaGBj9ROE4xqgw9S1Fkc4gVuAfPQTrJc_byNajYQoEG633bfSpI58-6crbxvpCIfTEl5liTYoZ7ju5o41J2bROz5kQgTfPP-HNoIFHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/Futball180TV/102455" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102454">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fq-0VXPVp2KNEzL2HBUrLP5QK-RWmC5B5AWV67s6rePpeAuMDO3pDexGxT3kXxFJ2WvCMEe9zsZt5UiIh1POgp8I2Pl_fegZW0AecYlS26chqSGCM5x7Qy6YvyOZnc3ZMTX_TeOziMfnQu4rQSv3CJ7KEajbG9Hb6hTfSMOZYtz46tYlPajU4HwEIiiOwBRkHLRtaljtxdFbMqFV7m8w82gDr8qyrPCxMRoVEhsu1T4rCZeYwx75CwdwPvwOVJq4DdWeoIq_nAnEmT5_bXNcwKI_zukk_980cbJ-N9Ww-i5DBqh6ZsfysMB4S9mfj3dQCfONk3jQPti54Z16PrIFUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇯🇲
وینی و عشقش تو تعطیلات در جامائیکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/Futball180TV/102454" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102453">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
📹
🔵
🟠
پخش زنده بازی دوستانه استقلال و فولاد ساعت 17:30 از لینک زیر
👇
https://t.me/+E5pLb4kNVJZiOGI8</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/Futball180TV/102453" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102452">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاسمیرو به همراه خونواده که دیروز به این شکل بعد از معارفه عکس دست‌جمعی گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/Futball180TV/102452" target="_blank">📅 19:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102451">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNG5RdvSPi8u1ASpS3YfgBHZFBwKhILKWZ2pD9_iuzFQhTwVY2lsIiXUX2F5HOtr5fUQpz72k2C4LoyYQELL_AT8-3DjxybKxUvMncYkGGmWWj4B0emGgBQ5Lv9Nt65s8xNJKFB-W7HYITVG4hEPD_y2UjFJK74N6wYmwoE0sadFvosPu5IbfNxbja-JPjtEiGFHLlJuoxYr-eYCeekUDwx2arLPR1vW2noP1MSfG0g0yfp69c7SIPlZxXJQz-j-_F2ag3INGxMy0rhFA_ZKnrxypUK7XJpXbA5zCxIuy5tr2xHJt-o_s53XqgiU7Q_oezwGhUlS_xyr66-rsF_Ejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
رسانه ESPN برزیل: رئال‌مادرید هیچگونه افزایش مبلغی در پیشنهاد تمدید قرارداد به وینیسیوس ارائه نمی‌دهد و پیشنهاد فعلی همان آخرین پیشنهاد تمدید قرارداد است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/102451" target="_blank">📅 19:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102450">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEAyZD0fMXqr9TqhztnbA_tpX9MNbRDl4B7a2Rd4cIMazhFVCZZeCM3nqzBykjg1KjfjZXAOVycjuavd0FVe0O1y6LCkYFf-hXsQGUSxiCk4gk8d_1e1-CCwVK9OQAv7ayy_bbGcY-9k08CAeU9RcoLm2Gjh_6e3Y3FFcO243meLaYLkpwMsqcSLEZvqcxpsQZ9zMnHslpf5_zPn2B7yO9KVvqoZNRZr-HEUSS6D7b3jsgjVx5BrsAN4tmo8xQl2cvmT1XHmkcmBQhPEGUDzecao6eBRvIcoqOgvADfATzvA3ixHuXjVOnsE0x9R9lDAq2YJPkMWD371CBANiju8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
اینفانتینو: جام‌جهانی ۲۰۳۰ بهترین دوره از تاریخ این مسابقات خواهد بود چون در کشور زیبای مراکش برگزار می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/102450" target="_blank">📅 19:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102449">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBRzI5io77aSJ4atP-ROH80g7vDE7PCdw4DlAsAhThWrDG0kGViyC3GrMl9kEP14G0IWoLg7RSds1spO33gz8ulsihmXyOAaqIbEa1K9yUmSQrlu5G0BeBh5mKmoVt9jQDfbuBWuvzaCXgbXMw-etB0W_nCpUjpDsqzcFXsSkfkTij4mTF6f766FXRoaAfEwT3TqTaOhI7NANr2YOjmjKIFDghXxtTzFGizBXNKR0bW8ZnoCInB8knIV23RzTK868XJaereWYUs9u_PbTp_uDC_4cyHQDHeqi8y5N06EPe_HEsviiNaTL8pvWoRXcbuLlGK6KFba6-nqeg9F2H1woA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس تعدادی از بازیکنای فوتبال
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/Futball180TV/102449" target="_blank">📅 19:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102448">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0Qe0UW7ry8ViU6hKg0Y_BUKAkXxPU0dNEJ9l96vyu0ouQe7I8ErWwNh2IVZoXNWqiNRxWThAluM9KCh3FO4YHJszGhOXjFvI116wKFajjYer5rtbGkrXiBDC0Q_SyBI8fNmq6Rq7_xw_rqPrHm64FOej-LD8g-nQnrNpoAT9N_JoB4sYul__B9mcQYTIrOUvykiXt3k9Kf9WXBovdQuDpu6MGkOL5OBJ5ylSbyn0S2oSr3Od4N0ppgk_WhwY0ejVC-ViFlFI77e-q8QhbrZMCN25QinOOmfaPHxCB-rCEhlgL3liYlcsSCucJhRT_SINNorEBWKx0DJwDsL0Hms7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
اسپی:
انتقالم به مادرید خیلی یهویی اتفاق افتاد و همه چیز خیلی سریع انجام شد، رویایی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/Futball180TV/102448" target="_blank">📅 19:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102444">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m8qIWCyleJRdKB6tVvTkOa41IbCNeJ7pby18dqoEKVs-esrrPGOrCIuPvzFNnIesC9CZDO6DbM70DzI5rSYmQ5DEA2FhJdakSHDMP2hjwVkYN5JuMdAiGj7_1UJC-KUJ5N9VImplYPjUVga64RzqtMzAisSaqX6kpKX9kXVBJETDfq4wqy_B3U8MQvCB8PaE9z2E9M46JmACF0grULJH-UQ3-Q35tiP3-Ey1OpXo075ecScTkr1SSV6LDit4S55y6bjFy0NMWmdgzZvKDiLfO5lWS1Sf8xulxYFEOgFmpK2lRvuaLsbBxnSWMuWKFgdAilxAsnfmh8MlLx8WZTYIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZiYK-7JxQ5JAt24REBfX6p-z2mFRmLq0Op64pPYS75nItESM5qFCNycAyqysPghDVVKbcV6aZV_6ar5TyYERRuahuM7GTNl0jZ2OLIknZzklQrMk5Vg0FkUJG1PFiWAB0njw2NG1Zs1s5AZMQJnPCFXkGSAWNvOqY60kDQ1jHr843p-4tkLxpJ1ElEJOXLMMoAfFcDERNKZOL6dFyV2v1FaU5mPKdK0FdWPm0iUMnpbVmwErXbCarKDGRaABUdc1vPu6f4r83_bqnVYrbZRU9zV5Dt1Gv8zwH34slFJ3g7V7phq3h8a9nNvY78-m2ZYP44w36lnA7PFNa600Aq4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTcvSAD8FEF9bd36t-v2h-jYCEjvqARmEH6fCILiuiyiwepIbrmtB5IxzQPlFTa3ogsaCB4dWOqnQpPepITVZJ8tLFEVtFFW3HBRIUq6W3hctzIWqBtZIJD1xLTnvEFlPegMWHThjZJ9UqS8vgFhGUeoI06f-2GHwqU6KHgVgXaY3JeCc0Xt_gxOHRO-x27oh0B5qEyPKQQ0aawWHRNbo57vtxFkw5ll10J2DrXo9L5SXPMPzJqoAePyrkTbNK57NRcMPQ5gucq_UndZ8M24NpPrTg3az8Bpqiiucfagr7jYCui-hEfakvK3Nz1FtN2ZQFiJX7hT1exN_vSwxW5EVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vFSJi6921B9EfUAfWDcGskbw15JcMCFEVjFKEdMpCd6MYh0RCjUsjB7NmNMe7EsndHg-6SgSqzZqMkfCQv_0ywAcVtTuBz4GOUEoUptz1wc6GRe1514zdvTHkOh4Kk8Q_Kj4mfaJnVx7GMsWux5GrOrYljJUkja1UAoO_Jxznys02S5I8H08LW9lS8G4_0EQfCOZDgPM1EVJQNjMA9r5aeTU_0c6_OvzSWx48JO82VFiU4LMUYYpRfa1gThmmsDNyAfwuRrO4XePkptt6SVR09yPGeDOn_pxXITaZdfK-jRydunkBVllOYG02gbR7jwoy3ImewDD6AJ_HRnn5DRIrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال لامین یامال با دوست دخترش اینس گارسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/102444" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102443">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbFwt3Cx86RuRJocw5Fk-gmShKIordBCWxMlID6MoD2qbMOtb25iLJm2A7Wl9zFsK3ZPHTCJRwSyh1it4qpzzR2Z3RslW7rNKmYp4gNTR4i3kOxBzKHSxz36Q7IGLY5tIVGOF3OsCCQu44q29KiXGjR_Y1P_Z4Z7S2kUOMDy-NX1c26IqVaA_uDmnAe2bz7WQQtUfdjqVoToYaRDf5Z9D_NNM9qiMnTFkQQHg_bCRLJRRKohXaPruKoonwRZED0Wuw8E1Uu1Q6V_fuME_XI-sYDmefxjXD7Yj5Dlb6skMjEfS52JAQ6h5UOvY-0exyygncqYFtpGj4qqmCfw_HDSfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی دوستانه مقابل فولاد</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/Futball180TV/102443" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102442">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCtdyR1eJUsR55mnjVKZ6tu1yuZadyRUkYSr9Pl22TAgDoxR0rtLBMsWneM4_8LjXWV4k928JSBhznZcNfCw0tuPWZTvWGbeJ62_p3lkyRGIukGRiwiFKqn_c02HzJorIiT0XsSaXvUsbgfNvWOlSUfZqErqbX4ETOa9F5IrL0fLT5yD7J_PO_WzTLWtFCVovD13qKfKlU9QxrK0Friaic9JTh1A7CJVi-TgKALP2kJl6Tr8_6RU5qfNHz3pTCwmaSZ229PbqaspvkcThgPaULG4gfNeT0Act1KDv4I5U5v8xYjo21L-OIlxO3J-ZR2Eii2BSO0a-myCD-HXfpEg6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوووووری محرومیت دوپینگ میخائیلو مودریک لغو شد و او به زودی به اردوی چلسی در هنگ کنگ ملحق میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/102442" target="_blank">📅 18:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102440">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXy46wjlBCZW5XWbfkfIgxKzYS_A9ZBhdQNQVtEtqc_u5X0YyOVDhtDrVFbMEP93hcs6iJ3QVdOracJDaijEWWGpsPiL7DaJ3I2OpIlVw7C-wNvK-OJTiyxWEzd9IARVtyf-59OzLa-rHmDTOzSIYM3xDN1tjrfXnnUgREF1cPnITRJHcUG_oCCZlOEaVOVOan8imrZmSpboM3pCbF0f1Y-MAoe5i9KcY1zerC84HJAp9J3J0rSY0YBgY1uIjo62wFBBZzw6huqVmBrEtpfjfkn-ip5rPC-0O2m9ynZEPtHm2iz-GT9TYx71OwB92rlt6ZDTE1JTUUCepCvURDDZfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mqDpH5M5NX0_RAB2X8LHChxv6AnmEeIOdIwdSjHzLyAZcCj7icTvH8ocQZAeR4ZWkq5T_6T7FHzGBPDH3SvhM2ufp1eZzcdRz8lFXivCi3VYHgPE3bzZ1bMS_OwOj6DcWPYvKM9VP5WS5T0uEMKMpSf2fmKWkBP5mP2h1FRjVPK0BUKsIHvnCWxwJS-CzQPeX5m2oWowhbasJJwzZvmXcxmQd9EwcFd4ROfSneSVRbzq3aYJgXdNxeFx-evLiU3EwL1OyAoCpcA3CAb6KRkD-etbiXKrJsCtYINcfRumSFfImc8mLgdJvJ6Usi3bueyFCXDl5BBY7oQ96kxFhZENzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیر شدیم و خودمون خبر نداریم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/102440" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102439">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NbVKRlzhM5cL6FPH10PQjjm6-vmj4sPuLLaTmGvUVPooVo7FrFT8aPMnqaWH4rb0aD1VjCT1bfiKsB4W4S-zgN1Wn3-h_tVlVlJ4FCh1U_pPEWKiha87LNRfl_WqQGWaHTJzZTriIN3YeX3jEgzSTBlauJ4aANzQA6BtvD4zo3cLdZlJmMm8ZtaRIWxASGT3EhxC2yPUinmnMf2XqSi30J-F_aqA_ybuh6sohScemmCQT437qCo3P6ZtRZk04rTuLNXSso1ERyQEUnSS2YoC5YIoTW-SO_kJN2SP6hFdS--PTbxJ7AQadkeLZ5YZL9ZXND8Aes0Ii-IvKm9rLlOrLmjtR6i_CGu2xqEgcu0FC2nbzxB7NIErnzXKs9J1jySiwebYTtdX-Ij5tw5p-EkoEnAuTpiH3u1MSmPDlGsLdOHynPUQ3dSoXbYbUt1pI9WnWZPJ1C0Lhj8Z5az2tWvBazZghk3riXC1fN70_QVtxmabier65dmeCbdbj4KvdEm15bReQgL3smXB9-7qUCFJ7YYZyMCz8gz_yAFYBoQ_dxRsRZwboj8HTij4ZLd7S6w5UPLOmKmXlwtFaJGy0f46MqTw8JUH0rMuDp55pemy7VqCKdeUY2qm2YhJa5yJfZTuRJS0P3pxZvf4qASkavPQ5VpvXPtI3w0kvA7ulc7DtqI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NbVKRlzhM5cL6FPH10PQjjm6-vmj4sPuLLaTmGvUVPooVo7FrFT8aPMnqaWH4rb0aD1VjCT1bfiKsB4W4S-zgN1Wn3-h_tVlVlJ4FCh1U_pPEWKiha87LNRfl_WqQGWaHTJzZTriIN3YeX3jEgzSTBlauJ4aANzQA6BtvD4zo3cLdZlJmMm8ZtaRIWxASGT3EhxC2yPUinmnMf2XqSi30J-F_aqA_ybuh6sohScemmCQT437qCo3P6ZtRZk04rTuLNXSso1ERyQEUnSS2YoC5YIoTW-SO_kJN2SP6hFdS--PTbxJ7AQadkeLZ5YZL9ZXND8Aes0Ii-IvKm9rLlOrLmjtR6i_CGu2xqEgcu0FC2nbzxB7NIErnzXKs9J1jySiwebYTtdX-Ij5tw5p-EkoEnAuTpiH3u1MSmPDlGsLdOHynPUQ3dSoXbYbUt1pI9WnWZPJ1C0Lhj8Z5az2tWvBazZghk3riXC1fN70_QVtxmabier65dmeCbdbj4KvdEm15bReQgL3smXB9-7qUCFJ7YYZyMCz8gz_yAFYBoQ_dxRsRZwboj8HTij4ZLd7S6w5UPLOmKmXlwtFaJGy0f46MqTw8JUH0rMuDp55pemy7VqCKdeUY2qm2YhJa5yJfZTuRJS0P3pxZvf4qASkavPQ5VpvXPtI3w0kvA7ulc7DtqI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چند تا از شوت های کارلوس رو ببینید، زمانی که فوتبال تا این حد راجب کسب و کار و پول نبود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/102439" target="_blank">📅 18:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102438">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=u1S4RuGzqHXpa-yhuVPthbxyZlA_Zc6SEH6w0ZteVJzcwZWLzuBXo6Sg4_sTEy_jKVUX8AHx_1uqF9HliTcouVs8Bq8sukg5M8vczGu7l6U70QcrR2d55XbEpdofTbNO782G1wWf6_6TFhYkjcqVWwCIu93dUM-beKdNvlZh-OYWBYvr3bXPmqnoHNmHm9EGQe8umarmmSbqq0FejJd4yJawqTmGXETJ1PTClxB2BFvuFeJbTbOlSUijwBq6Zle4bG7k09dW7ktaa6Rceeni-TlcurXuYXchIkYbyaU8iiCURy-K_PK4QTsFfTaThhScouNs5Ht6PIW_Uy9gZ-00Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=u1S4RuGzqHXpa-yhuVPthbxyZlA_Zc6SEH6w0ZteVJzcwZWLzuBXo6Sg4_sTEy_jKVUX8AHx_1uqF9HliTcouVs8Bq8sukg5M8vczGu7l6U70QcrR2d55XbEpdofTbNO782G1wWf6_6TFhYkjcqVWwCIu93dUM-beKdNvlZh-OYWBYvr3bXPmqnoHNmHm9EGQe8umarmmSbqq0FejJd4yJawqTmGXETJ1PTClxB2BFvuFeJbTbOlSUijwBq6Zle4bG7k09dW7ktaa6Rceeni-TlcurXuYXchIkYbyaU8iiCURy-K_PK4QTsFfTaThhScouNs5Ht6PIW_Uy9gZ-00Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی‌از وینیسیوس‌جونیور در سن ۱۶ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/102438" target="_blank">📅 18:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102436">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HISrN8-TZZvfekThLd0nnki5xAHr7G2Vjn4XN18g1GstHXzjdqXecv4esEHDwjE_J1mqmZRyLv-QsGhmHEKMQFa9r_I5O8_fxe8pq5bHiJ2CwHsBqyTg6qHMfFkwqdPGQ6_PQM6GQ0FY7PRGpQbjLSROl2TIKFj8HQujj_D4_gySBYwmlS4fXWuv9REuBCmTqm03CTrRX_Ecxh9gf8iJDNrzDTE95uNPEadRmwKRSJ63WxoJfMlsYX3R3ekhihY4FGRUIrCVcIZaKVqQNe0Fkju1dFRX3YJMAY8bTGx_GYNN8JyFy29taucnjhw3p_P-fEIFoZpEEup92r5Ijar70A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p81RHJGNuFTl2HMIPVGUyG6_Skd_WkFK3fkqvC3Emt6SkwEXIim0Rz1JeCBHOQTXkjmRGjaT9KUl_EhsiorZ4WZkv23CTixoJ9dO-ZDAbwc6iztcmbWtJEai1_OcGeCOQN0KiORht3HmNCV9Ith3HTZIPJBFlhNm7f369AJDokomimCU2VA8rmUPfKtD-3xGfTTD1scFWXN-HByj4YBhpkt-GWK2Y8eeSY5GX1Zz8ns04XMwnci92hIulJy2jZgsujFLCBaRq0H6jMwbZE4kmKfZlFuAafjPSRnZN5Jvz6LkdTWQ9NiELms8FyZpO5pMVpP9eFWeX70L2KbYTZ7ymQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
فوری، محرومیت سنگین چلسی:
🗣
باشگاه چلسی به مبلغ 10 میلیون پوند جریمه شد.
🗣
همچنین، به طور تعلیقی از ثبت بازیکن جدید در دو دوره نقل و انتقال محروم خواهد شد. به این معنی که اگر بار دیگر خطایی انجام دهد این بار پنجره قطعی بسته خواهد شد.
🗣
در ابتدا 6 امتیاز از مجموع امتیازات چلسی در فصل آینده کسر شد، اما باشگاه درخواست تجدیدنظر داد و این رأی باطل شد.
🗣
این رای بخاطر تخلفات نقل و انتقالاتی در دوره آبراموویچ مالک قبلی باشگاه صادر شده است. مالکان جدید این باشگاه خود این تخلفات را گزارش دادند که باعث تخفیف در حکم نهایی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/102436" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102435">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=Evh7HnQtq4sjPHDxwBuPZNEnTLTGxqyJjDVYZl7bfW-fxIEg1fMI8AxejFf8OGdW5dXMk5DkviBDjz9KpgxCOFRX91bDChtc8UOl7svOnTOWI_COPU4DclRDFN_FGqhl4TbCZGVAh6v2fVpryy3UuBNSwj8UH3v3bOUU8Z0wu_wv_oMEBrHVt2tynwsD_lTwFEoS30fYh3oiljdM3aezzAXMLpnWOXJhcWFEggfPjad9aOb0XVH7ZNIN3JAFT18OUujrAPPMnQu2OVUQTYkr6sdy9m90cC50WTPZbXxbk__WKgIXd71CVzZ7Pn-gnJv9sxkIoawYweqw7e0mg-WfY41QU9ReK0lo6tDY8sxDGwGrDqf7rJTLwbwAHB_xO9hQSJILpiWK0_jw45tGOjdBazjDZHKY2F3ouu3UrWuRgvjM8rW98EoxPPOG7OyxsCkWIzC6_GEMR4tyAMOkyLeZ-8GlnLDpY5yuu6gsaOXdu2B5uUuuY-QHjsaNfXNZ7BF4lXyDMauKZWv17czUjKS2RQtoqgkr0E5Zjk1ypVI5oHBxYp4v4VhnkUCXOSEkLz9Ot4Uy1QeymV7J0ke0v070iQ1vrEPBW6uIUVGKy65bn74wWTo6iKSsm8GxRM2VLGgYs24_ibinubjdhMPnwYi4Zi1mWgrN1XkEaWeOzpRyx0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=Evh7HnQtq4sjPHDxwBuPZNEnTLTGxqyJjDVYZl7bfW-fxIEg1fMI8AxejFf8OGdW5dXMk5DkviBDjz9KpgxCOFRX91bDChtc8UOl7svOnTOWI_COPU4DclRDFN_FGqhl4TbCZGVAh6v2fVpryy3UuBNSwj8UH3v3bOUU8Z0wu_wv_oMEBrHVt2tynwsD_lTwFEoS30fYh3oiljdM3aezzAXMLpnWOXJhcWFEggfPjad9aOb0XVH7ZNIN3JAFT18OUujrAPPMnQu2OVUQTYkr6sdy9m90cC50WTPZbXxbk__WKgIXd71CVzZ7Pn-gnJv9sxkIoawYweqw7e0mg-WfY41QU9ReK0lo6tDY8sxDGwGrDqf7rJTLwbwAHB_xO9hQSJILpiWK0_jw45tGOjdBazjDZHKY2F3ouu3UrWuRgvjM8rW98EoxPPOG7OyxsCkWIzC6_GEMR4tyAMOkyLeZ-8GlnLDpY5yuu6gsaOXdu2B5uUuuY-QHjsaNfXNZ7BF4lXyDMauKZWv17czUjKS2RQtoqgkr0E5Zjk1ypVI5oHBxYp4v4VhnkUCXOSEkLz9Ot4Uy1QeymV7J0ke0v070iQ1vrEPBW6uIUVGKy65bn74wWTo6iKSsm8GxRM2VLGgYs24_ibinubjdhMPnwYi4Zi1mWgrN1XkEaWeOzpRyx0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درگیری کورتیس‌جونز، سیمیکاس و سوبوسلای بر سر بازوبند کاپیتانی لیورپول در بازی دوستانه اخیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/102435" target="_blank">📅 17:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102433">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHwFcDHMp2wBbiK2JF9ErBGXAVY4KJL7ojrHa0TX_v_kQX0L9MNn6WtxCrotCZh7OgPJ15spZ2hP5B-CxZnkg9IUCr5b-vwu3xUVPNl0IwNJ51Zbomf6Jy0HShz95s7A2xpE6HfosHXLVsjyZZe0vz7QcsZGt3wrhWZJubFEiQ8v8e1v5ClcZlWDOHGazj-cCcsPFoXuI3JlPlOxmh4s8yVQEtj6fZtlqS-ASMfVGgH4UFu21O94u5Rc0HkfWjwc_XBNSCw85KSE-3rxgASC6mWakRxfTocPZnmvdvBBcle0qCXmuVhhHiDQqrOiatxDomElRmPmnfwpU8OIncNb_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RN0cl0AK3F78DCu7MMEwnpFJWqqKprTfA2AAfNCM5As8y1i-XS08PPhTDvrMJgkxHgPcW3PhkGGom8Ch0kPOidDq9SojmvN7yWlfzUVx-nvfM6M05ZpZy16FrkWSGO79z8UQ6feSYU8X0226U83uWtuE31zmJqV7BaZTAKUeQWgmmUZhAnUpwu3np5pKV7ixlyPlNs6fHgcPOnWGWvm_CxVwPphtKTxWtyzMkMjHdJydxMV2CrHG-7x-i5gBhnLS1S6uDCMqts0NMPR812z1DukBt1e0vDBbx8T7KxiZQo899gtffKYQ8_reIxSrdiSC25vLYj-3nsQLLrfipOCH6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ال اسپانیول:
پرتغال و اسپانیا اعلام کردن اگه اینفانتینو پیشنهاد خصوصی سازی جام جهانی رو پس نگیره از میزبانی جام جهانی 2030 کناره گیری خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/102433" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102432">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96363baca3.mp4?token=umVhdByQNsT-UhaeU8M9STAx70Qu1Ur8hRfCZlyCpuGPgyi-uA2GWms-SQ6DUjnKkG3qs50aF4nhP9B0mU7qNRdWcWkZnFfI_JO69aLP5V1Dmc93IgWN2oG7CA9jutExSZ5_NtU3cMMzVBLcqirMJbA86WWp-kYJFM_MCduj_RSNOGLLc9bFQPA9nPFJik9C_an7l6H9MzwaXrgG1BcejYBJk-EDEP0ridpZVVQ9MshO8twXVo2tIKX9qXufqGBUZBc8LdZuJeOghMiQ6aMs4PeZMQJu7qYWIMF-mfYL4qGpqonOAJsxuFvH84mEkwWyRDEfdsVDGc3J7IxkVYSBkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96363baca3.mp4?token=umVhdByQNsT-UhaeU8M9STAx70Qu1Ur8hRfCZlyCpuGPgyi-uA2GWms-SQ6DUjnKkG3qs50aF4nhP9B0mU7qNRdWcWkZnFfI_JO69aLP5V1Dmc93IgWN2oG7CA9jutExSZ5_NtU3cMMzVBLcqirMJbA86WWp-kYJFM_MCduj_RSNOGLLc9bFQPA9nPFJik9C_an7l6H9MzwaXrgG1BcejYBJk-EDEP0ridpZVVQ9MshO8twXVo2tIKX9qXufqGBUZBc8LdZuJeOghMiQ6aMs4PeZMQJu7qYWIMF-mfYL4qGpqonOAJsxuFvH84mEkwWyRDEfdsVDGc3J7IxkVYSBkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مرزها برای میزبانی از زائران اربعین آماده‌تر از همیشه
🔹
در آستانه اربعین حسینی، پروژه‌های عمرانی و زیرساختی در پایانه‌های مرزی کشور با هدف تسهیل تردد زائران اجرا شده است.
🔹
در مهران ظرفیت خدمات و زیرساخت‌های برق، آب و روشنایی تقویت شده، در شلمچه بازسازی و نوسازی بخش‌های مختلف پایانه انجام گرفته، چذابه با توسعه امکانات رفاهی تجهیز شده، باشماق به سامانه‌های هوشمند مدیریت تردد مجهز شده، تمرچین توسعه زیرساخت‌های خدماتی و ساماندهی محوطه را پشت سر گذاشته و در خسروی نیز سالن‌های مسافری، پارکینگ‌ها و فضاهای خدمت‌رسانی توسعه یافته‌اند.
🔹
همه این اقدامات با یک هدف انجام شده است؛ سفری ایمن‌تر، روان‌تر و آرام‌تر برای زائران اربعین
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/102432" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102431">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">💥
🧐
رونالدو، پسرش و جورجینا درحال عشق و حال در گرمای تابستونی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/102431" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102430">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=FgUtw-r60oDau7n9IVJWuZJ2h6tzMQObG3cJfxmo-EOxP2jYzutSPjThv5O4iOA_IY4nHhGKQrSFmoi6gMj-86fb8YQzOsb4-XOQlzknvr61owqv_74umg69RwuVRlULqvJJRoJmMm_SEy0dc83YRkFgCzwUbvMdcQB6tu9OHB61ZukbOpUt4y-oDCmlOb4VjTr6Bh--wmAaj5L_X8zAz5M3g1pCAFor-DV6S0ieTVVQJifGgRfVQ4QZVkPFWtE5334cozrONcrFKWMhtARUNzQtgVh_b_wYHNZ0pPX_nTdYHqCVERtHn7_DTfyJ-SxznuIbeWttC5GYBBZsiWFg9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=FgUtw-r60oDau7n9IVJWuZJ2h6tzMQObG3cJfxmo-EOxP2jYzutSPjThv5O4iOA_IY4nHhGKQrSFmoi6gMj-86fb8YQzOsb4-XOQlzknvr61owqv_74umg69RwuVRlULqvJJRoJmMm_SEy0dc83YRkFgCzwUbvMdcQB6tu9OHB61ZukbOpUt4y-oDCmlOb4VjTr6Bh--wmAaj5L_X8zAz5M3g1pCAFor-DV6S0ieTVVQJifGgRfVQ4QZVkPFWtE5334cozrONcrFKWMhtARUNzQtgVh_b_wYHNZ0pPX_nTdYHqCVERtHn7_DTfyJ-SxznuIbeWttC5GYBBZsiWFg9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
🎙
تمجید جالب کاسمیرو از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/102430" target="_blank">📅 17:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102429">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=oHS00TsnqkM_SA1MJRP-pk3yHsZFHF9oR_EwVAVTFqWb6P7bA1iGdGYEXs9OIVF2Nk5F5n81uYs6r-ji5bg3Gy-acOXeJ6Eo3-EJmXIkdBmUusptln6m86OOsljARsTrW6dY4Fn3mkm5cX0VSaKCYJ_PqCFDhVS8qhbqSiJS_441XfloMkDqrUCXh-K_9Z7OQUafUHCFtnMiSc7JJ4NxV1AOcnLtCxU0nWXhpDfAM1inkKhjkfWs5AI5ZiEF0hU2kIq0RewfHg6ZxlS4KD7OqTLLvGSBqRzIXcWRdms5Y6pNMdk2dRSlrpeeBgfs6KnhQgtyIkDtQFvoEB-kJ0ZKjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=oHS00TsnqkM_SA1MJRP-pk3yHsZFHF9oR_EwVAVTFqWb6P7bA1iGdGYEXs9OIVF2Nk5F5n81uYs6r-ji5bg3Gy-acOXeJ6Eo3-EJmXIkdBmUusptln6m86OOsljARsTrW6dY4Fn3mkm5cX0VSaKCYJ_PqCFDhVS8qhbqSiJS_441XfloMkDqrUCXh-K_9Z7OQUafUHCFtnMiSc7JJ4NxV1AOcnLtCxU0nWXhpDfAM1inkKhjkfWs5AI5ZiEF0hU2kIq0RewfHg6ZxlS4KD7OqTLLvGSBqRzIXcWRdms5Y6pNMdk2dRSlrpeeBgfs6KnhQgtyIkDtQFvoEB-kJ0ZKjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
یادی‌کنیم از بازی تاریخی ایران و قطر با گزارش جذاب عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102429" target="_blank">📅 16:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102428">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=XXBL4ux_HV034ypaftx85bkH8zkZqLF9-88R3IKceiysSy9a3Tbklb8z4tk2n_yloglBOQUZdIFgdNHVqwl-_cLwpaRbPx827QxrQ2GXXX6zj8hC4KuYdmTA4xdRrAJE2jaUvigTYFSWYgQeqmc-nCaGu6iUHqkKsnig0D-Q6To9AvFjGW9ZzoVusS4aOjKzBF0c635u3f-aZDj491VaeXcLkTDCcJo_EkRgaxzN6Q685Elm9y3j-tHQ3qqWic8Nhv_kNBT2vJH8geWn3-_XI66C4MSe-Fv5t4tKp58107HATWbpl7J7r7OjV7dug_q1BZv3oGa9Oz9oBYKenftiHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=XXBL4ux_HV034ypaftx85bkH8zkZqLF9-88R3IKceiysSy9a3Tbklb8z4tk2n_yloglBOQUZdIFgdNHVqwl-_cLwpaRbPx827QxrQ2GXXX6zj8hC4KuYdmTA4xdRrAJE2jaUvigTYFSWYgQeqmc-nCaGu6iUHqkKsnig0D-Q6To9AvFjGW9ZzoVusS4aOjKzBF0c635u3f-aZDj491VaeXcLkTDCcJo_EkRgaxzN6Q685Elm9y3j-tHQ3qqWic8Nhv_kNBT2vJH8geWn3-_XI66C4MSe-Fv5t4tKp58107HATWbpl7J7r7OjV7dug_q1BZv3oGa9Oz9oBYKenftiHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیاز بود یه آیتم جدا برا لحظات تاریخی فیروز خان کریمی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102428" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102427">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=VqAl1faROEG2VGU0ggFZuDFcfB0t6dD1BdEMsbg0uqhUUZVgx5QsEVqgvEYHAwWSwLOvdoeswd-4t0sc1PKOVm110JFrahn6pIQtm9qY_1gXHWBlLoatD1jRaQUlWl-o_4_02LED8_YDwDyw0kDEMR6qeJau1oFWWgnE_n9tlQLoluWoWcMCscLyBdntR-9EL0wJkm9VBjQBGxfyDhFXC0HIvhN2wO4Xn-d0jSN7Vjb_VRm06RFwimxrdEAKXk7yHor4h7MS5j8j3lXjUK8SASnQrg5J4oR6Yfo7sieALFxW5LBHuCAILcwMLux0C--8FE1vnk7zAw-Xr-ZX-HvKmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=VqAl1faROEG2VGU0ggFZuDFcfB0t6dD1BdEMsbg0uqhUUZVgx5QsEVqgvEYHAwWSwLOvdoeswd-4t0sc1PKOVm110JFrahn6pIQtm9qY_1gXHWBlLoatD1jRaQUlWl-o_4_02LED8_YDwDyw0kDEMR6qeJau1oFWWgnE_n9tlQLoluWoWcMCscLyBdntR-9EL0wJkm9VBjQBGxfyDhFXC0HIvhN2wO4Xn-d0jSN7Vjb_VRm06RFwimxrdEAKXk7yHor4h7MS5j8j3lXjUK8SASnQrg5J4oR6Yfo7sieALFxW5LBHuCAILcwMLux0C--8FE1vnk7zAw-Xr-ZX-HvKmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
▶️
رکورد پرش سه گام جاناتان ادواردز (۱۹۹۵) با ۱۸.۲۹ متر ثبت شد و ۳۰ سال پابرجاست. این دستاورد استثنایی در دو و میدانی تحسین شده است. ادواردز در مصاحبه اخیر بر تکنیک منحصر به فرد و هماهنگی قدرت و تکنیک تأکید کرد. او پیشرفت رشته را با شکستن رکورد توسط نسل جدید ورزشکاران مفید می‌داند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/102427" target="_blank">📅 16:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102426">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=XgIL1xFEgqpFi7MiVK8jmsJLAmswmVSgSCzCqy2FpiAUxuxmPFS6ecLNJAwPzqN9iw5PHVS10tmhMctgIOI3mC1TsuG4EihV2qSEWZb0ZVIVoB_oZYZAiC4CYJRstGvRplGMaCsEb0Ll5RHHOckzmmXD1smMgTE4Xj8TnykCblimnSbT5Mod9Zz91X4l-WbF3kCAMNhzSP5QVF2vuKl7gr-U87oUEC6tTXe73zkwxmpGLLi0DirDbBRKsHP0c1p6UzVz7IEOcSosbqIGlzMEr2fYZCsGnr_VGRoG5gfLRMK41xexJbXeLUy764vdlEYmPN0wlJe3IKrkvJs3n3ilhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=XgIL1xFEgqpFi7MiVK8jmsJLAmswmVSgSCzCqy2FpiAUxuxmPFS6ecLNJAwPzqN9iw5PHVS10tmhMctgIOI3mC1TsuG4EihV2qSEWZb0ZVIVoB_oZYZAiC4CYJRstGvRplGMaCsEb0Ll5RHHOckzmmXD1smMgTE4Xj8TnykCblimnSbT5Mod9Zz91X4l-WbF3kCAMNhzSP5QVF2vuKl7gr-U87oUEC6tTXe73zkwxmpGLLi0DirDbBRKsHP0c1p6UzVz7IEOcSosbqIGlzMEr2fYZCsGnr_VGRoG5gfLRMK41xexJbXeLUy764vdlEYmPN0wlJe3IKrkvJs3n3ilhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو کمتر دیده شده از مارادونا و فن‌پرسی
💘
💘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102426" target="_blank">📅 15:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102425">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43f315425.mp4?token=e3UbMDRw95mJIJHS347Jdcjh5XzV3UnN_suk4LRUICTGI6LbeCWYcUEAJel8GnpSpXUxTSvQnvYsFm3JFxHwZa8N7ni3i_MZQH5bt0b5C-tu2NkqwqvIq6XR4ubFNPySfbtoNRnhRmuh7cdUmbNQbxEVsp0B3LSrsMyCsHEDH3pyT7QicYYntnvxSeApbDIOQyAnIVAq0SiSEeCUvP2z4C48zHSI0T9akMRZgTOE102Zlmqs7DsbUH-qjyfX-2tiEBXPtzZ-QS0bjkynuyLm_xYxCi5hOq9JPIvzeZe_JoZel278-a8JEbok27UwgUu0oWt1vEUs4YJ4SRZWaINKIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43f315425.mp4?token=e3UbMDRw95mJIJHS347Jdcjh5XzV3UnN_suk4LRUICTGI6LbeCWYcUEAJel8GnpSpXUxTSvQnvYsFm3JFxHwZa8N7ni3i_MZQH5bt0b5C-tu2NkqwqvIq6XR4ubFNPySfbtoNRnhRmuh7cdUmbNQbxEVsp0B3LSrsMyCsHEDH3pyT7QicYYntnvxSeApbDIOQyAnIVAq0SiSEeCUvP2z4C48zHSI0T9akMRZgTOE102Zlmqs7DsbUH-qjyfX-2tiEBXPtzZ-QS0bjkynuyLm_xYxCi5hOq9JPIvzeZe_JoZel278-a8JEbok27UwgUu0oWt1vEUs4YJ4SRZWaINKIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⚠️
تجسمی از المپیک اگر تهران برگذار میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102425" target="_blank">📅 15:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102424">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGnN3_Kt7emR2rbKOccUqylzUyUlAnkeyPs_ZZnVPpJ-DWdPvs76TjDBkFC0pBAbZgc3azO2T9fODosyEYxdYFq0L_CvT2Zn8gBt_yJUV3FFT3MEtRqKJmdHNoCHdygl4VqBk-x0kckRlP9oqyfjefP8qVLn9Mu-jL-Wyo8KDWrgxetyEpeJIWW3_kf8Q1_2CrwK8gL0d1LJLaHHPa1gxxVOA8SzpHYuVvKgLtifUxCVq_nyVDpZT7PwwfE9XMbutgM_jJjrz8s_bQJ1JwqibfDrBR0U5GMtUaVY7ykFURPIZmHfl2R_vHyoz0xdbhZq7U11h2WVfQSw9LGYG7NjCryo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGnN3_Kt7emR2rbKOccUqylzUyUlAnkeyPs_ZZnVPpJ-DWdPvs76TjDBkFC0pBAbZgc3azO2T9fODosyEYxdYFq0L_CvT2Zn8gBt_yJUV3FFT3MEtRqKJmdHNoCHdygl4VqBk-x0kckRlP9oqyfjefP8qVLn9Mu-jL-Wyo8KDWrgxetyEpeJIWW3_kf8Q1_2CrwK8gL0d1LJLaHHPa1gxxVOA8SzpHYuVvKgLtifUxCVq_nyVDpZT7PwwfE9XMbutgM_jJjrz8s_bQJ1JwqibfDrBR0U5GMtUaVY7ykFURPIZmHfl2R_vHyoz0xdbhZq7U11h2WVfQSw9LGYG7NjCryo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🔥
👀
۵ گل زیبا و برتر اولیویر ژیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102424" target="_blank">📅 15:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102423">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=inBN7lvOH8hovwQv33D0yAb1Cjwh7Qlya4ef-xnuoU6s6MFyqqeRFRV0dukCz-dWIefi0PwBxlZX3w5eG1eDIfHq41V9DcWhI9ZQ0nJZAtO9MtzD_hH_r0pNK1jPJpYUiHPwqfQnYmULn4Gyyiacjac2EhbioHNWwhEdE24vknr_6SOmiZwlVh14yezA0SG-spovpxNNVDKD4MhCiudfgtmD7L4SWF69N73Ui0THIJEoqTXKdbXQEaJeAcjDuI-k5UTj30ZvhrMUbgNm3KO_nQIsdA2sCNFBLfRp74qlirURBPxaiTR5_KkcEOiHoYKGXB8__I-E2t2iJzKYEDVqIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=inBN7lvOH8hovwQv33D0yAb1Cjwh7Qlya4ef-xnuoU6s6MFyqqeRFRV0dukCz-dWIefi0PwBxlZX3w5eG1eDIfHq41V9DcWhI9ZQ0nJZAtO9MtzD_hH_r0pNK1jPJpYUiHPwqfQnYmULn4Gyyiacjac2EhbioHNWwhEdE24vknr_6SOmiZwlVh14yezA0SG-spovpxNNVDKD4MhCiudfgtmD7L4SWF69N73Ui0THIJEoqTXKdbXQEaJeAcjDuI-k5UTj30ZvhrMUbgNm3KO_nQIsdA2sCNFBLfRp74qlirURBPxaiTR5_KkcEOiHoYKGXB8__I-E2t2iJzKYEDVqIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
سه دقیقه با لیونل مسی ورژن 2014/15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102423" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102422">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rywlk-lHzeNCeoeNN_Jiqx2xrNkirD6Vu503ukSJHy5a53Fqd6feQcP956JIBaM8h-1nm5YfqPTwkrWE5iNbrywnhDt5WdB0TygfginqH89hg8RWGb2zGKrxYSdEFOP0pQE4QCnGnTn5LSzFliJQX4A1egRiJbQzX5D85R9R3Aivzo_Yg3xKElYIysI9HX9nDyfGeY8IcDO0SW4XfftbzaIEykBFOhCAClljRSOpKBXvYzshWo8npqy00R0jkrW07_c9WQ19OSBXTcTDGHPabEyn2R3xYr4wl5w2WOE8gcGRiLnoWn5dKLZ89VEsYtu2jUROeeH2DE4vI5E9wPkjYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
لیست رئال‌مادرید برای بازی با فیورنتینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102422" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102421">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0ZBbWq5loshZJ6Jw6jKA2YRi7w-LzEGOHvKahPWpW7XNE3ZKN-OphaNBUX9ASFDdSTLjYlHNlPm9mInz8wBAx5JxemcpDCTOzE8UaiWOIGAPyKk95YyLtHVGKD0-44A8MsDmcZ9o9flRerclvKkI9tdH2nGezdZTKzwRCGNoOC3aknhsUr2B8WZNvbK-Dg0yLjM2sChpPM0nkfQda2y9vnFPukhPux3wuy_ohu8lzttFnUEtfoKBlp0Moyb5uY7QXQnpKzTrfmO1IBoK55IlaL1_XeC6TKAb74VKD95sJSTHjJXdkBDu_8x1wT-ZEPQwuxQSRlx_eBXAKaud0_Hlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
#فوووووری
از نشریه اکیپ فرانسه: آرسنال با نیوکاسل بر سر انتقال برونو گیمارش به مبلغ ۹۰ میلیون یورو به توافق‌نهایی دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102421" target="_blank">📅 14:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102420">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=P-2j7ZHXIPyArZpKhltpMbvbIIXhwtfz1Wet7fxpq_51Xj-1_hb-QAtC5Fmq-XHnWYZnxlqAVWUpetlm0oZKGX4anuDAAJQHzFYduglTADZ8B_6WGPZ6GXDD1M3zllKj2EOGQQctC9nixZHJUeywgNyTUfN1cNojppBMeDQ1F3x7w08swEDIkB7jO-OPSJvALuPtYpjiSE2ro3MBo-Bw_OA_4tao2c6okxqHBsU3O2kKp0oUDlkzxTkFZDDszUJQIwXsZCqcD73oKPjFljlGyhv66Os-HpMY8myC_ThNdzKkOOvljH6L3WBmcgqFc20FOT39ZD71P7ZSSXVvoyWtTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=P-2j7ZHXIPyArZpKhltpMbvbIIXhwtfz1Wet7fxpq_51Xj-1_hb-QAtC5Fmq-XHnWYZnxlqAVWUpetlm0oZKGX4anuDAAJQHzFYduglTADZ8B_6WGPZ6GXDD1M3zllKj2EOGQQctC9nixZHJUeywgNyTUfN1cNojppBMeDQ1F3x7w08swEDIkB7jO-OPSJvALuPtYpjiSE2ro3MBo-Bw_OA_4tao2c6okxqHBsU3O2kKp0oUDlkzxTkFZDDszUJQIwXsZCqcD73oKPjFljlGyhv66Os-HpMY8myC_ThNdzKkOOvljH6L3WBmcgqFc20FOT39ZD71P7ZSSXVvoyWtTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
✅
یوسفی: زمین و تماشاگر که ندارید، لیگ را پلی استیشنی برگزار کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102420" target="_blank">📅 14:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102419">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9889076a09.mp4?token=ligMdqapXWUeSUbke9KuZoLiuLT1s_n0IXtW96I1W1v2fdEYifk2SkfF76IXipGhHnN2rm9fpdPRO1auoPBMM8DrYZTrz8pPZKAsFMtcG3Z8zsneXPbEh9rJdWm0ndwRL83X1DPHcGfCeCW8NXBqBqxMI5kImHaTTApbrRX7ZMKkwXyzJrbu-Eivaa-bDR_nVEGtNnUNZYLWlhCUfskn5PRvX7BYlg6ySjcDFpbvl1zxJQtmkeNAH8hT8FPWXqB-u_NMvL8Nag45vpO0OPojhlIJQLJ7ZYNuX9-tbNr6v0PMOwkvD9KeLYgUpDL-2PdMO179vVYLxmer5HM90EtSMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9889076a09.mp4?token=ligMdqapXWUeSUbke9KuZoLiuLT1s_n0IXtW96I1W1v2fdEYifk2SkfF76IXipGhHnN2rm9fpdPRO1auoPBMM8DrYZTrz8pPZKAsFMtcG3Z8zsneXPbEh9rJdWm0ndwRL83X1DPHcGfCeCW8NXBqBqxMI5kImHaTTApbrRX7ZMKkwXyzJrbu-Eivaa-bDR_nVEGtNnUNZYLWlhCUfskn5PRvX7BYlg6ySjcDFpbvl1zxJQtmkeNAH8hT8FPWXqB-u_NMvL8Nag45vpO0OPojhlIJQLJ7ZYNuX9-tbNr6v0PMOwkvD9KeLYgUpDL-2PdMO179vVYLxmer5HM90EtSMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
💥
روزی که پیتر چک آماده ترین گلر آن دوران فوتبال میخکوب شد و این اثر هنری شاعر رو تماشا کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102419" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102418">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EteR7XqaN5FUFgLlu8vFNX0_Ki3NNllHo04vCpjlVF_9v8CtrAun7pD-xHWe7QOkgiMnBaseSRrWEvLWswUyIJeCwsYQ8_5n6UaVNNas8JXlnUL8PV_46GNPwTJnLvj_82i5Su6Ql-IxdRrRe995HYPnL_Qq9h2Adpr4aI2TQ-o166-uNthzenKVnND1yNxxV4PzHwDhB-tZbzxJKRQdULi0KupU8mPMtqm_JE0yLd4FfDZ2hCSAo2nzrQN3ltkg9cgMi2JAspz6nMR_z6QcwsDVNt-r9aRlbI1E8dUOQPN6s8LNjl99oqOXxwqs0RBT3_o_FuOcb2SaIHxH77NqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کارلوس اسپی تو تمرینات رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102418" target="_blank">📅 13:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102417">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFsubHB4HPc3NDVspKB5sf82GciA4_ImB1xkQ7AJ4WJJSbJ07irfQbVBXuWkj0tHYLbJreKFgHcl_hdB9qEezM1b115qxmCYoDzFm4NIZ6S3KpSmlWACwg8V8UGv9lJ1BiWDgUv1wxZAm0cze_9OGayhuHSNri5SM6mLSOqqYaUayALeQKrKb42utQe1ly27Ddlebd6edBZeBT_y0Gf6BQMPp7L72UauCYwXwruToBs-iiMePAPsbwjSYkLSm5aY-fW7IHxEq3zPMragAJPF1MBHwcpATyBgJrSlwP5iJ205qeVsLC4ysmpxFMz2XO1L7UbPyfmFtVe7NpThfDXy5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
روزنامه اسپورت: دو باشگاه آرسنال و تاتنهام به رقابت برای جذب فران‌تورس پیوستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102417" target="_blank">📅 13:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102416">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=XPbjlkJf9SiLoeo4rC2LUhrl3XSKByIqCortcUDzSW6yuwWql6wqXjPT6Ervbep4LgYFtSgodFCgkm2E1tSmLuiaU_GLUpWvUMc5My5MfFa6P0GOqPzl9cU6etN5DY2jvNZv-OePuUi-FcQqv0UVbRPIp8brV1kXyVuxv_Bl1hS-r7zBZhnwLVTLCXpB915ZZHR4RWkCgxaO_wRLkxt8eIyQFKCwMX2Yys6J_m3Uurq_nFJ0jcWCo2EG7yI744QdE1GZJpkQeusZk9m8Y8VysYFQznLLAHCAZon2AyGbVFx6L3CAkKlngxOdrjW6hcl-reZ5Dwl1e_S9PIOB22KdNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=XPbjlkJf9SiLoeo4rC2LUhrl3XSKByIqCortcUDzSW6yuwWql6wqXjPT6Ervbep4LgYFtSgodFCgkm2E1tSmLuiaU_GLUpWvUMc5My5MfFa6P0GOqPzl9cU6etN5DY2jvNZv-OePuUi-FcQqv0UVbRPIp8brV1kXyVuxv_Bl1hS-r7zBZhnwLVTLCXpB915ZZHR4RWkCgxaO_wRLkxt8eIyQFKCwMX2Yys6J_m3Uurq_nFJ0jcWCo2EG7yI744QdE1GZJpkQeusZk9m8Y8VysYFQznLLAHCAZon2AyGbVFx6L3CAkKlngxOdrjW6hcl-reZ5Dwl1e_S9PIOB22KdNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های بامزه رونالدو از ارتباط صمیمی با پسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102416" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102415">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=v1LZzdyZc_QPndIy4f580icj87kauh6VV-S1Ji3-7pERiHV2AWA7vKymm3baHJu0ib_XeE7jjg0dki4e9Ar-9wp5vWJgO5N4ZC76u9KwalAS8GapDWZ10n4DGIdIfg_qgPkTU3cBPGmr8ipCUNnDh2lb4UEeDnDgWMHux0ZLUm-KIjldTZ1QfEOnjnlmE5QA_Tfw4xNCfqxL1P6SoheuNBEqC4kAlC4V1qcaW9FH7P3mYYxnpHjvYFD2Sbr2bukY9wa7S5__k5aleU1DM2hLQXwB9kw3cIwZyN7elGOOxdbg-E3Z5RPD6uMHeeyad_JAgKlu3K0lfoynVI2w4yISjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=v1LZzdyZc_QPndIy4f580icj87kauh6VV-S1Ji3-7pERiHV2AWA7vKymm3baHJu0ib_XeE7jjg0dki4e9Ar-9wp5vWJgO5N4ZC76u9KwalAS8GapDWZ10n4DGIdIfg_qgPkTU3cBPGmr8ipCUNnDh2lb4UEeDnDgWMHux0ZLUm-KIjldTZ1QfEOnjnlmE5QA_Tfw4xNCfqxL1P6SoheuNBEqC4kAlC4V1qcaW9FH7P3mYYxnpHjvYFD2Sbr2bukY9wa7S5__k5aleU1DM2hLQXwB9kw3cIwZyN7elGOOxdbg-E3Z5RPD6uMHeeyad_JAgKlu3K0lfoynVI2w4yISjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🔵
درخواست کودکان جنوبی کشور در وضعیت جنگی از رامین‌رضاییان بازیکن استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102415" target="_blank">📅 13:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102414">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=c8z2cbeLKgt7OoFzChOGLNUoF4hl_uk5aH3mxNSZMcN_rwZRw7u8wlPDy4XG4PslKLVly4QUA8UEDLuACjKVedJMtJR-1_6Cm97smGGAAjKK41YrBji2ONgr-DbIjxAHQFECvJyRHJPb3M4Lpqei1GIYqEuC_4jSPrdhe4nU8eQxqYB5CesUBryGAK5qVJdwFTr1Xx6hIOtMJyNd2NwUXE9cWuQpxp4hJS4SpOc7WTiNR9n3n8nKlrwghTblatLxqL3bEDWVZzKHNIwBxzfi13MWqMi36kQ6kmgra8sD3ZtQH-Ew84d8Jxkq81_FJnAitqqbYMw7JxxgLXxZzOBDAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=c8z2cbeLKgt7OoFzChOGLNUoF4hl_uk5aH3mxNSZMcN_rwZRw7u8wlPDy4XG4PslKLVly4QUA8UEDLuACjKVedJMtJR-1_6Cm97smGGAAjKK41YrBji2ONgr-DbIjxAHQFECvJyRHJPb3M4Lpqei1GIYqEuC_4jSPrdhe4nU8eQxqYB5CesUBryGAK5qVJdwFTr1Xx6hIOtMJyNd2NwUXE9cWuQpxp4hJS4SpOc7WTiNR9n3n8nKlrwghTblatLxqL3bEDWVZzKHNIwBxzfi13MWqMi36kQ6kmgra8sD3ZtQH-Ew84d8Jxkq81_FJnAitqqbYMw7JxxgLXxZzOBDAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
نصیحت اسطوره‌رونالدو به امباپه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102414" target="_blank">📅 12:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102413">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🤩
#فوووووری فابریزیو رومانو: آلن هالیلوویچ استعداد برباد رفته بارسلونا در آستانه امضای قرارداد با پرسپولیس قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102413" target="_blank">📅 12:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102412">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=Izrc80HCjYv9FhwZfqoTxtH7Gxq5iWZmPCdh9pH0j2o6owm-wZ95H1PGFonyeWBKYu19ZTXgHvhex6ANzIlkiKj-nD59_jmQBACumb8kc66eRMvlMIymtmciL5o--c7IBLp7aq4WdNnPAlEpTGfa5PZlDakZq0IlSJtCTqfZ_7Dc0Q6gVJQ7WGIYNHHxb85crRgeOMrQqc23kf5zlc06NkzcyzOpff3zPFGBW0w6S1KxqKNtwVUv7qFTdpebeHJu0gxB05B-EBialBQ3h4EXXJ8rVV0Pw6vMM0IiwEfeBde044I5PGyOohJ9T2N_3qD16P3hsyr7xT0PX0r_dG4bsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=Izrc80HCjYv9FhwZfqoTxtH7Gxq5iWZmPCdh9pH0j2o6owm-wZ95H1PGFonyeWBKYu19ZTXgHvhex6ANzIlkiKj-nD59_jmQBACumb8kc66eRMvlMIymtmciL5o--c7IBLp7aq4WdNnPAlEpTGfa5PZlDakZq0IlSJtCTqfZ_7Dc0Q6gVJQ7WGIYNHHxb85crRgeOMrQqc23kf5zlc06NkzcyzOpff3zPFGBW0w6S1KxqKNtwVUv7qFTdpebeHJu0gxB05B-EBialBQ3h4EXXJ8rVV0Pw6vMM0IiwEfeBde044I5PGyOohJ9T2N_3qD16P3hsyr7xT0PX0r_dG4bsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇧🇷
آنچلوتی: "در هایدریشن بریک نیمه دوم بازی جلو نروژ اشتباه کردم تیم رو تغییر دادم که باعث شد کنترل بازی از دستمون در بره و ببازیم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102412" target="_blank">📅 12:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102411">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=EBZeBcWkmOwxfU2mt07N9FAuluqdkzMLCEdAPkYOHpLK9HhcNouUF7dc52Pzebfb87ITNWcAQiwJuTzaZNgJdjLTTBnqXvb25bltLzjxR9eThanlcUgOyJ2pH3YHCTL5PebSD3wZCsfcuiIitgTrh1d7yA4KB-oIK4T7s60A7nklMqL01w9f7bUQkwEd9ZkTJsvKi21A__HkKhQHkS8WQhSk3pDhprXCb2vTMQHlRVGgHiHFm8lQzd47s4qBMRyAwwJ23qBFWqmHhBq0SYBUc5x3QMyj0Zo9SgvFrIQClOG617lPU5dfRatL-Z9rW9aHNYorgU0QSfd_Gx0BMauvjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=EBZeBcWkmOwxfU2mt07N9FAuluqdkzMLCEdAPkYOHpLK9HhcNouUF7dc52Pzebfb87ITNWcAQiwJuTzaZNgJdjLTTBnqXvb25bltLzjxR9eThanlcUgOyJ2pH3YHCTL5PebSD3wZCsfcuiIitgTrh1d7yA4KB-oIK4T7s60A7nklMqL01w9f7bUQkwEd9ZkTJsvKi21A__HkKhQHkS8WQhSk3pDhprXCb2vTMQHlRVGgHiHFm8lQzd47s4qBMRyAwwJ23qBFWqmHhBq0SYBUc5x3QMyj0Zo9SgvFrIQClOG617lPU5dfRatL-Z9rW9aHNYorgU0QSfd_Gx0BMauvjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
جواد موگویی که اخیرا در گفتگو با عراقچی یه سری اطلاعات حساس تهران رو داده بود، این سری اطلاعات مسکونی مقامات نظامی و ... هم افشا کرد
😳
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102411" target="_blank">📅 12:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102410">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=aeCm49yvCWSiL77lQU-lI0JqQz61z-hMB8_QgN9cl_zOIFPX-DfFIy_6nemxPliq2dZTyEIA5Fb6Cv2quKZOArZZjYvF12_ykZ--5eA1nar4bVszh2i2aT8apdZIJaHQg4uVfQGPcuQXijYV7VKTd7jKeUhA7WM-3AyicZ9Ou5i1LLCtQcIn9UiObem6ExSxtrDWUxInZ6oeLjDw2jpZP7WK59wi3FQ7F--zNya88YHlIazTwam0_hUpwH9FKmPHHYRwLpa2chbqBVq8IgWX8lWj9Bj5Qw5ROlkM7XnL3vHFAnjqGJMDD93a72RHQ0TzeF5yOX_Y3lQMNepVJKcFWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=aeCm49yvCWSiL77lQU-lI0JqQz61z-hMB8_QgN9cl_zOIFPX-DfFIy_6nemxPliq2dZTyEIA5Fb6Cv2quKZOArZZjYvF12_ykZ--5eA1nar4bVszh2i2aT8apdZIJaHQg4uVfQGPcuQXijYV7VKTd7jKeUhA7WM-3AyicZ9Ou5i1LLCtQcIn9UiObem6ExSxtrDWUxInZ6oeLjDw2jpZP7WK59wi3FQ7F--zNya88YHlIazTwam0_hUpwH9FKmPHHYRwLpa2chbqBVq8IgWX8lWj9Bj5Qw5ROlkM7XnL3vHFAnjqGJMDD93a72RHQ0TzeF5yOX_Y3lQMNepVJKcFWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
🔴
‼️
علیرضا بابایی مدیرعامل چادرملو: تورنمنت سه جانبه به دلیل کمک به پرسپولیس برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102410" target="_blank">📅 12:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102409">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=RzCkqd1wndnwMQgUAB0b7tNjMm1N0Z-jLV6ij4NsvAWp4EKK3xcnLtHzj4iR6q80hxWwmbXKyXPux0We230jTzkej0muGtN0wenNU9T57Yns3vmcNWPbcWnfabHA2HSdWjeIYPE-x4XnawTfkgh8WQ9mtBejIBWa0UUb1KcLeQQfyTngoCqmrYzEo_uXquvDW7WmQjTDTDQHsfcwrei3TxjAyZ6GHEmpa3kXtYNMJjPUFv_EOThasMwhvPg52C1amhl95cfof7bbCEWYauRD0SQ8d71Y27Dt0Fg1Pu959gu-mOo80IusxhJ57-BYouEb_JVqTBs0eLoIsLmGze9dAF4f5aplsbngjmtaIV_V9DNhsbyqjPiMO7AUyR1lUmiXTZFPwreoPH9cPoGCuQooDtPiHryHQ7Es9XXDTaTS9uVwRXqn_JWPN1KsoEKN7-w6kRY4sc6GIjYEZ3JQKFjyRqArKBA6Y7MQIrHEeYgw6L22iwBqGANrWncraMlfkIG0BLUxv3lu8yvRss5OmF8rSaXpSTardjH-ywplPDoOWsYEWVOGNrlKfgKLfCGUHslaJk3j3N1ICtu14vq1X1rPnkHCo0uN7U13CapnWUtW7bltKNNfmmMCDdpnWKwtp8h_rNE0-l_jXNHxn-Uc4v6K55nhEIsnU3baVjbpDyMijPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=RzCkqd1wndnwMQgUAB0b7tNjMm1N0Z-jLV6ij4NsvAWp4EKK3xcnLtHzj4iR6q80hxWwmbXKyXPux0We230jTzkej0muGtN0wenNU9T57Yns3vmcNWPbcWnfabHA2HSdWjeIYPE-x4XnawTfkgh8WQ9mtBejIBWa0UUb1KcLeQQfyTngoCqmrYzEo_uXquvDW7WmQjTDTDQHsfcwrei3TxjAyZ6GHEmpa3kXtYNMJjPUFv_EOThasMwhvPg52C1amhl95cfof7bbCEWYauRD0SQ8d71Y27Dt0Fg1Pu959gu-mOo80IusxhJ57-BYouEb_JVqTBs0eLoIsLmGze9dAF4f5aplsbngjmtaIV_V9DNhsbyqjPiMO7AUyR1lUmiXTZFPwreoPH9cPoGCuQooDtPiHryHQ7Es9XXDTaTS9uVwRXqn_JWPN1KsoEKN7-w6kRY4sc6GIjYEZ3JQKFjyRqArKBA6Y7MQIrHEeYgw6L22iwBqGANrWncraMlfkIG0BLUxv3lu8yvRss5OmF8rSaXpSTardjH-ywplPDoOWsYEWVOGNrlKfgKLfCGUHslaJk3j3N1ICtu14vq1X1rPnkHCo0uN7U13CapnWUtW7bltKNNfmmMCDdpnWKwtp8h_rNE0-l_jXNHxn-Uc4v6K55nhEIsnU3baVjbpDyMijPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
علیرضا بابایی مدیرعامل چادرملو: بازیکنان را از پای دیگ نذری آوردیم و با خواست خدا پرسپولیس را شکست دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102409" target="_blank">📅 12:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102408">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=hTfDp_W3Qa--rmRTY5hUPsEqYi0632tXR0DNmRz4hEVZcH-BsPUMi5m0satUgTJu8agFfe_FjxYc2NxWLLXTbG7ddPg4TMwxMZ-OaTBtEdsUxoT884FQqfzwlRpZWMNZZmHmvXZUEpb9ykLb9Gu-N3IFiH-_5GfEdnQdPHXTUaoSO5OaHCbishizOMaT1oZ9_eCwrxJJLcoRhJ5pO-E_y5pNg0kJsAsX3VBDX6t9QRyPtN-jIULsx7SiFLB7LIw9LrGNm-JYe6YSLoQoz0FqmQrSYBvqhlpyxfJpeYYK5NQ5R822CtidJheFTBrzk6rDu-teCWjKukRgtKX5knvXvXVoYiqY9nTVpzEQqCiHeC_jwIuv5iiRTF7P4dunYfuXsTVNGdQujlQL3MvEMRukirn238SlZULPoBP466JMCwYY6XaDOy4SdVjJqr_2RhI-4l6EvfHzRWlqb-3J2kLbBssy0L22mCY6PTxX64Z5IQ-FZL7syZbW_GN6JaByBm1dDArvlX_ErfFJiVXtKTcFMBzuC_5DQh-03wS_HRcs2IKpF4G6vud7MhisQ_1s1r8vgbVP6n3EwsVl8K7tnFqXbKkk0q18OzR-dGXqqQFCffxXGL1PcfYrJphor4-_AWBii8z_qEKtMF0br2Qjsldt4g1TmqwQFggGfenOPmQVvNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=hTfDp_W3Qa--rmRTY5hUPsEqYi0632tXR0DNmRz4hEVZcH-BsPUMi5m0satUgTJu8agFfe_FjxYc2NxWLLXTbG7ddPg4TMwxMZ-OaTBtEdsUxoT884FQqfzwlRpZWMNZZmHmvXZUEpb9ykLb9Gu-N3IFiH-_5GfEdnQdPHXTUaoSO5OaHCbishizOMaT1oZ9_eCwrxJJLcoRhJ5pO-E_y5pNg0kJsAsX3VBDX6t9QRyPtN-jIULsx7SiFLB7LIw9LrGNm-JYe6YSLoQoz0FqmQrSYBvqhlpyxfJpeYYK5NQ5R822CtidJheFTBrzk6rDu-teCWjKukRgtKX5knvXvXVoYiqY9nTVpzEQqCiHeC_jwIuv5iiRTF7P4dunYfuXsTVNGdQujlQL3MvEMRukirn238SlZULPoBP466JMCwYY6XaDOy4SdVjJqr_2RhI-4l6EvfHzRWlqb-3J2kLbBssy0L22mCY6PTxX64Z5IQ-FZL7syZbW_GN6JaByBm1dDArvlX_ErfFJiVXtKTcFMBzuC_5DQh-03wS_HRcs2IKpF4G6vud7MhisQ_1s1r8vgbVP6n3EwsVl8K7tnFqXbKkk0q18OzR-dGXqqQFCffxXGL1PcfYrJphor4-_AWBii8z_qEKtMF0br2Qjsldt4g1TmqwQFggGfenOPmQVvNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
مشکل ایمنی ورزشگاه‌ها به لالیگا هم رسیده‌ و تیم رایووایه‌کانو نمیتونه از استادیوم خانگی خودش در فصل‌آینده استفاده کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102408" target="_blank">📅 12:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102407">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=XzEt7Y7hISi-cDjUUgKb6k75w9H0-AfgB5Ey-Khfky_R8TkncnLhZF_3ygZuwHZBfu7IRemZV1gniDuGFpuMDhNh84gqwTbo7Ga_DxOc6mc0LemHlxDmFTIWqiy1WPxXHsjOAMsj28qEKe4PkHxkguKS3G5NqzXdzrWdqZ5zehqUDEkXa-jEM_qPUYoohFI591QM_P2qkvyekEpv5gqbY_Nqt4SSQYHok2OXgtIFETF7LlIZlWZX5YoPytcH2XZfrzMYedfVoHk2F-xdDyQTScytQZY2HQeMztPAoE6qQU46EyBLrphxONzDqRlqTaztfaONTigENqK_JWH9Gv-stg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=XzEt7Y7hISi-cDjUUgKb6k75w9H0-AfgB5Ey-Khfky_R8TkncnLhZF_3ygZuwHZBfu7IRemZV1gniDuGFpuMDhNh84gqwTbo7Ga_DxOc6mc0LemHlxDmFTIWqiy1WPxXHsjOAMsj28qEKe4PkHxkguKS3G5NqzXdzrWdqZ5zehqUDEkXa-jEM_qPUYoohFI591QM_P2qkvyekEpv5gqbY_Nqt4SSQYHok2OXgtIFETF7LlIZlWZX5YoPytcH2XZfrzMYedfVoHk2F-xdDyQTScytQZY2HQeMztPAoE6qQU46EyBLrphxONzDqRlqTaztfaONTigENqK_JWH9Gv-stg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو وایرال شده از صحبت‌های تلخ و بامزه یک ایرانی حین ورود به‌تونلی در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102407" target="_blank">📅 11:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102406">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262957043c.mp4?token=n0_YmwG4LIqx_NN_zOTqfcuSU-qvKHy_3Ti_VGOnH0uvu-LNjTLrjypURbmEK4ebHvQT148GAd-ibqtXyq_FFdGPnLWSX1ct3gUVrKRy_TcHNqeGnSaMLzvM0kI_kYRyisbCEVrMf6qOFtXXXeK5PkFJ0qGHfGlNQClWUZwFoJPVPey05SOZ9Epnbg8rxrRQ8PP037U9nKW3yiyor2aPuMOyGrdXv7mQ-ovO0zDvjlZaC8k1kMJDDwOZfjDxsD9dBl39AGnZpM9pE5V8wNyY4DEStJPxW8OCcbfJfVYoV5slVbvwGSg-Mm3vSEUW3QXnzBPehNE8oqISUllAtKTNgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262957043c.mp4?token=n0_YmwG4LIqx_NN_zOTqfcuSU-qvKHy_3Ti_VGOnH0uvu-LNjTLrjypURbmEK4ebHvQT148GAd-ibqtXyq_FFdGPnLWSX1ct3gUVrKRy_TcHNqeGnSaMLzvM0kI_kYRyisbCEVrMf6qOFtXXXeK5PkFJ0qGHfGlNQClWUZwFoJPVPey05SOZ9Epnbg8rxrRQ8PP037U9nKW3yiyor2aPuMOyGrdXv7mQ-ovO0zDvjlZaC8k1kMJDDwOZfjDxsD9dBl39AGnZpM9pE5V8wNyY4DEStJPxW8OCcbfJfVYoV5slVbvwGSg-Mm3vSEUW3QXnzBPehNE8oqISUllAtKTNgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرایز خاص‌ ژابی‌آلونسو برای فصل‌آینده؛ رونمایی از ستاره ۱۷ ساله قزاقستانی چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102406" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102405">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=UnPIE_XkIgYljwrt_Qj6FsE0FaCB4AWzN2ZlSZYRSDiKTvKJKOXYE2_JJPLctjZOXqornLZayscHCJgehbsjurnCZIepvwfHdO6cf2TMpiSwgvx5GitND_U6hQU8Ztf34ML0fnW8sdAsiF4GB7g_eqfPdpaZXZ7ZasummX7hRwmbu_okuTBDQUdE4DeoJ0OP-RizUtn39Ez2GI_trdR3qRK8La_k55ZamIcUaNxoI4DqkV9wQbuNim5T1oIB2-_XzUIRuizEwG6DqJq9zUDYulgPyUnUF5FAPoOLT82XuyRcju_2jlkrvW9w4MyAGIKO2rJrsdWQONr89MM_AckU-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=UnPIE_XkIgYljwrt_Qj6FsE0FaCB4AWzN2ZlSZYRSDiKTvKJKOXYE2_JJPLctjZOXqornLZayscHCJgehbsjurnCZIepvwfHdO6cf2TMpiSwgvx5GitND_U6hQU8Ztf34ML0fnW8sdAsiF4GB7g_eqfPdpaZXZ7ZasummX7hRwmbu_okuTBDQUdE4DeoJ0OP-RizUtn39Ez2GI_trdR3qRK8La_k55ZamIcUaNxoI4DqkV9wQbuNim5T1oIB2-_XzUIRuizEwG6DqJq9zUDYulgPyUnUF5FAPoOLT82XuyRcju_2jlkrvW9w4MyAGIKO2rJrsdWQONr89MM_AckU-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
آماده‌سازی استادیوم نیوکمپ برای فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102405" target="_blank">📅 11:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102404">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=kAXXN6j-M9Cn94WEzXUS-LoPZO-XiGqjlUU9sA1cod_29-_TBINZjjVCgaTq8hfe7dWPwB8QFybty2XMqFSYG3qIuYFLHllkM3US3FRlBlXUGUI6FWBEjLmLMr74Lj2ftAVMXREqrkmQT9AvA8IriRNdANpJk5I1gGaRmmtzqpp_oRTYsOiQP6ah2hC-mVyZSYmCwc5SVSo9R9SgOvDlYSvB_Hq39WMuZUehBM2UcRKkMF5s9fcwxFy31A4KbX74azjKGwsPTnecrt2yJkwFEzwCydKSh4tPgGTNZG_aIkBODTnblNblDZk-kqqrxbmJoP5wPcI-tIZbRrzBD9hLgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=kAXXN6j-M9Cn94WEzXUS-LoPZO-XiGqjlUU9sA1cod_29-_TBINZjjVCgaTq8hfe7dWPwB8QFybty2XMqFSYG3qIuYFLHllkM3US3FRlBlXUGUI6FWBEjLmLMr74Lj2ftAVMXREqrkmQT9AvA8IriRNdANpJk5I1gGaRmmtzqpp_oRTYsOiQP6ah2hC-mVyZSYmCwc5SVSo9R9SgOvDlYSvB_Hq39WMuZUehBM2UcRKkMF5s9fcwxFy31A4KbX74azjKGwsPTnecrt2yJkwFEzwCydKSh4tPgGTNZG_aIkBODTnblNblDZk-kqqrxbmJoP5wPcI-tIZbRrzBD9hLgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پاسخ‌تند و کنایه‌آمیز مهدی‌رحمتی به صحبت اخیر معدی‌قایدی: بذارید تو‌ توهم خودش بمونه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102404" target="_blank">📅 10:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102403">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
کیت‌دوم فصل‌آینده منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102403" target="_blank">📅 10:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102402">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=TJEOIp7dNRPZgckON6clqMBnqc4fs22cZ0n47l0IcMTAY8iuL0RLCsZD8qEoMjGd3zcvhhQWELnDcqww_HgvENDG4yEodMR_wyiD3WTVdX-IIZiTwsEQt2iKhlwUdgqRuUVbSqKfAN6Ejh6vfVYXbzz5fyRuby7Mimqu1pY4NP7Nz5aNSM5nCRsexxUzNqrj-rZA3Ha384ZFtfGRmxuO_OAeaoZ95pjRbS1y1K8RHmigfPToslndIHTSE4kE9SdusaccrWnr5h94cBQaex2H924JrvBrvg9A8p3f5U0yZsS_AnZBpQvPqPB-kxzoan8d4CDAf8E4sg-dYTUmrGOaDoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=TJEOIp7dNRPZgckON6clqMBnqc4fs22cZ0n47l0IcMTAY8iuL0RLCsZD8qEoMjGd3zcvhhQWELnDcqww_HgvENDG4yEodMR_wyiD3WTVdX-IIZiTwsEQt2iKhlwUdgqRuUVbSqKfAN6Ejh6vfVYXbzz5fyRuby7Mimqu1pY4NP7Nz5aNSM5nCRsexxUzNqrj-rZA3Ha384ZFtfGRmxuO_OAeaoZ95pjRbS1y1K8RHmigfPToslndIHTSE4kE9SdusaccrWnr5h94cBQaex2H924JrvBrvg9A8p3f5U0yZsS_AnZBpQvPqPB-kxzoan8d4CDAf8E4sg-dYTUmrGOaDoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری شدید فیل‌فودن ستاره سیتی به همراه مادرش با چنتا از مردم در یکی از کلاب‌های شهر منچستر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102402" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102401">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=gdYFGpOuizG6BBVJl2i7Ede6zT0kETkZURJBZKI3KkOcr-tTYzz5EnrLSb7Kmp2ZIxiZm5qSkJ9CBdx9O0IZK7AF7mXSkK-8MXqEhjOvn5tPngrQkS66z1GXlzgYEzoeWxv8MEndnE67-33IMIC_EXGgyYlNPuJCigQrKQgVTIgH3tQrnXJDY-_5w04KKUU7dxhzDA1FOYAZEhSPYgn1942V3uzznIg2KnzzEwJ65tvJGaAqrR1mO0nPjwxzfD5ADZ7TPfIaWFpmfE_Xz6OI3qNDORqNUcG4vPHDWzkB805Hb96HjgdgyJNNittHSsFR5VEbjKgLmUQJerYTdVv4XAHaZE9m61lGXY0sa-gAKAx_kC4wpFqfdcxrUxLveQ2eYsVSOYCo51ZCf4v-9HNy50hY6eL12OKegDQD1DJ3Lycbch0tKNLovxaqi_aQKxyfd8A8-KYo-kkd9-DpLDJe5Ua1pgYxyfBaleOsCa0Wr8m0PXqhiGHlHQahuwIhrzWi9SFzJUpLgnHkroOA4_I3yoiFiBe8RKORhLb4CQyOJfpjGuddxaLKPIonCZPnZuEKM4LMfYoDTxpt1kXT566-TgFFxcGvOq-qBOVJuMwK4mVl1BIkO8NZzbhpHVi4JSs4XCYE_Nq0KkHbyP6fpTgpAPWcUE8gSoHzCbMs16uC-Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=gdYFGpOuizG6BBVJl2i7Ede6zT0kETkZURJBZKI3KkOcr-tTYzz5EnrLSb7Kmp2ZIxiZm5qSkJ9CBdx9O0IZK7AF7mXSkK-8MXqEhjOvn5tPngrQkS66z1GXlzgYEzoeWxv8MEndnE67-33IMIC_EXGgyYlNPuJCigQrKQgVTIgH3tQrnXJDY-_5w04KKUU7dxhzDA1FOYAZEhSPYgn1942V3uzznIg2KnzzEwJ65tvJGaAqrR1mO0nPjwxzfD5ADZ7TPfIaWFpmfE_Xz6OI3qNDORqNUcG4vPHDWzkB805Hb96HjgdgyJNNittHSsFR5VEbjKgLmUQJerYTdVv4XAHaZE9m61lGXY0sa-gAKAx_kC4wpFqfdcxrUxLveQ2eYsVSOYCo51ZCf4v-9HNy50hY6eL12OKegDQD1DJ3Lycbch0tKNLovxaqi_aQKxyfd8A8-KYo-kkd9-DpLDJe5Ua1pgYxyfBaleOsCa0Wr8m0PXqhiGHlHQahuwIhrzWi9SFzJUpLgnHkroOA4_I3yoiFiBe8RKORhLb4CQyOJfpjGuddxaLKPIonCZPnZuEKM4LMfYoDTxpt1kXT566-TgFFxcGvOq-qBOVJuMwK4mVl1BIkO8NZzbhpHVi4JSs4XCYE_Nq0KkHbyP6fpTgpAPWcUE8gSoHzCbMs16uC-Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
نظر سرالکس فرگوسن درباره‌مثلث جادویی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102401" target="_blank">📅 10:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102400">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=UKPcElKguh2ahkdSwQdZpP98hZm-BXH4aAQ6isMLjWAZaJf4_5qs6eHaUJZQoUPnd__lA749f97UH5ryudQfHf0ajIIQwKAlzCWTol-bJyPy8ahUiTqu7FyPEIn0qk7gz6ZQunjpn-2vdpPZVYqhKUhGGKdil0P1KbYSmmDgYogYwQFG1svjfaJjbcTJh19jwqqRVgDbqQh2gxkLYvkSBjM-RpTVATvga9jwO_Nra51i02RiONC6DYTcuxA8L16goEgxTRo5h3jn1BDnCjjbMZel6YCXj_SV8NwAwkXemGRF3bRRl7MJc3IhZRwSOEZENEqk2Yn4SzXq11qyVSJuH3-xsA-nH24t7Vw4oMECvEmpxBKWg1cSrMkfARP86gWBmzfOKgTRQhOvYwm68qjQd77XgZrffekFsSuN8BQI-Ugs7-VLjM3G0R48pDxLTvGimT0JskR6rl0dTdwx6hwrLzJ2B51GmMABA2s_sUsZG6wVqy38Gx4aGi0N0AmId7x23mjE7OZFnrPfQ8r8iexGP4_JzNKQf2__zipscBTjvUYPCq-VPatJd3FvgjKjPLJ2mV3Wl1M8YuUWKl93McWIkR0zMzpn0tRrvBQuqKTBM3iduGgUqkYhKWuCDgbiqa3koPg3eS0dqMAKdGMLN_tw3s9oYy1PnNFEmQ95h1CzePQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=UKPcElKguh2ahkdSwQdZpP98hZm-BXH4aAQ6isMLjWAZaJf4_5qs6eHaUJZQoUPnd__lA749f97UH5ryudQfHf0ajIIQwKAlzCWTol-bJyPy8ahUiTqu7FyPEIn0qk7gz6ZQunjpn-2vdpPZVYqhKUhGGKdil0P1KbYSmmDgYogYwQFG1svjfaJjbcTJh19jwqqRVgDbqQh2gxkLYvkSBjM-RpTVATvga9jwO_Nra51i02RiONC6DYTcuxA8L16goEgxTRo5h3jn1BDnCjjbMZel6YCXj_SV8NwAwkXemGRF3bRRl7MJc3IhZRwSOEZENEqk2Yn4SzXq11qyVSJuH3-xsA-nH24t7Vw4oMECvEmpxBKWg1cSrMkfARP86gWBmzfOKgTRQhOvYwm68qjQd77XgZrffekFsSuN8BQI-Ugs7-VLjM3G0R48pDxLTvGimT0JskR6rl0dTdwx6hwrLzJ2B51GmMABA2s_sUsZG6wVqy38Gx4aGi0N0AmId7x23mjE7OZFnrPfQ8r8iexGP4_JzNKQf2__zipscBTjvUYPCq-VPatJd3FvgjKjPLJ2mV3Wl1M8YuUWKl93McWIkR0zMzpn0tRrvBQuqKTBM3iduGgUqkYhKWuCDgbiqa3koPg3eS0dqMAKdGMLN_tw3s9oYy1PnNFEmQ95h1CzePQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
شباهت حرکت‌های یامال و اولیسه
🔥
😮‍💨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102400" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102399">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=VwO77NikwdRKioVUg2rlbKli-NzhLqM9cnVeVe1rbEaMJ8QEZicRvXKaoME8CpHRN5sCP5cautRtMBGICG-cWQgt9mp1VhDrWuKilaKBKsncGmGEmX1pBzz3Nuu5HYXcdBGPrBto5Um52EMGTE9lq4Sm3kFED9D0HoTMcMgOevF3_OSp4-dB60HJo7ycmqrmnvIgpJPqIcXeiFSHqyWveskK5SXF8pnPeCpKYIUXoqdWPTxqKZqsaWeuiLfPT7I9VO48PUv_RQCeGX5Au0mZQ5_utr-06w9UNOTUEgg70Fihlbd41NigLilf1_7xBNQyPVCDHAFyIHcUK1T4-v0neI1uyDUa5k7UOEmi76HTYuB4vUxzvwCoF0nhuKWNXlrryAe5IiHUUA899CcVR7D-pClnqD2peFVi6mo_SRDpfZSfFQTC5ijWCiARoKXoVj8NdcKLtlUcW-gEq3mJJStT1Kja1eASDa-W7BWwRErkioM6abUZ50IdPO5r99vSjg2A9R8L19xk8EBM5Bl32LGRfmlNDLhxfSI7HnESEVlJs_CDkwJ7bY38LA2xeLH5KJO1JQPqbz-F1phk7oQPXJSBLi1pZ4ueEQNlqj8bKoSFXoGhDtCm63fn_CjxrJEaXqdCWrim4ZtP0Jc8NPWXpp3GJ1zztS--7hz7SkvTbpztJoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=VwO77NikwdRKioVUg2rlbKli-NzhLqM9cnVeVe1rbEaMJ8QEZicRvXKaoME8CpHRN5sCP5cautRtMBGICG-cWQgt9mp1VhDrWuKilaKBKsncGmGEmX1pBzz3Nuu5HYXcdBGPrBto5Um52EMGTE9lq4Sm3kFED9D0HoTMcMgOevF3_OSp4-dB60HJo7ycmqrmnvIgpJPqIcXeiFSHqyWveskK5SXF8pnPeCpKYIUXoqdWPTxqKZqsaWeuiLfPT7I9VO48PUv_RQCeGX5Au0mZQ5_utr-06w9UNOTUEgg70Fihlbd41NigLilf1_7xBNQyPVCDHAFyIHcUK1T4-v0neI1uyDUa5k7UOEmi76HTYuB4vUxzvwCoF0nhuKWNXlrryAe5IiHUUA899CcVR7D-pClnqD2peFVi6mo_SRDpfZSfFQTC5ijWCiARoKXoVj8NdcKLtlUcW-gEq3mJJStT1Kja1eASDa-W7BWwRErkioM6abUZ50IdPO5r99vSjg2A9R8L19xk8EBM5Bl32LGRfmlNDLhxfSI7HnESEVlJs_CDkwJ7bY38LA2xeLH5KJO1JQPqbz-F1phk7oQPXJSBLi1pZ4ueEQNlqj8bKoSFXoGhDtCm63fn_CjxrJEaXqdCWrim4ZtP0Jc8NPWXpp3GJ1zztS--7hz7SkvTbpztJoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شیرجه زد، گرفتش، زد زمین، شوتش کرد!⁣ جوک خنده‌دار بیلی مک‌کالاک ماساژور سابق چلسی درباره‌ی پتر چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102399" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102398">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osf77JZMjnR1ljAUpHfggq72kLoeONKtp7WBnqIKkffUGW0rh46L9eP4lSvRCb2VG2qOQkBEwzYAqFXClZ-FGG0-brDcMhH2j0CU4UGcFSS52RBmFbOnuVWcWY2-P5rxJ-UYcsfROnMkguQ1P7DsZgPqJ8UGNZ0wY_nCjbz_mTr_AJzFE9gPPGTh3wLG9L3pWAw4E7iC60H3sY6DO6XJC6Newy_KsjbSv9s9Tshf-I4DMU-KF4PP2JaUfJNcE951EbpmLkNiD4MVOxPe5sNyAP_RO5GQFqnvr0fJU-xIj7qNByEEC-TOEsw-H9X39hNo4Tz1vHSXH0LLiKpINBYtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🇮🇹
لحظاتی پیش، فرانکو بارسی، اسطوره فوتبال ایتالیا، در سن ۶۶ سالگی درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102398" target="_blank">📅 09:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102397">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=WeuxuNeMHExlXZ5NSCuMjONq0quGIyCYFpOoXpooFNNlTr5CVNihboOlma7ynArWPjXv3l-Q43KMXF31_2aOcB6tD40HweRhBJOpcHr9VfBDBYlqNzNQ_ySLZPOz2b8sQIv9hBxXBVMqD1qq9txmQJWc9lAFdjIA9NkIjwCTp4T5OCF6Ph5HJol1yWAKHw8S-jphvI0gI81ueVm718fMfx9LaF4C38G8DesOZxvw9mA4s4Xp_xSIhr65CDgmimusRHnz7sTfxH7_1ZvHt-1OzIG2BVrLHH1OiO1Zxi06tDWPXuuBoV5hp44Ne5slza-s4rkW7NUJkjcRd4YHRde-bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=WeuxuNeMHExlXZ5NSCuMjONq0quGIyCYFpOoXpooFNNlTr5CVNihboOlma7ynArWPjXv3l-Q43KMXF31_2aOcB6tD40HweRhBJOpcHr9VfBDBYlqNzNQ_ySLZPOz2b8sQIv9hBxXBVMqD1qq9txmQJWc9lAFdjIA9NkIjwCTp4T5OCF6Ph5HJol1yWAKHw8S-jphvI0gI81ueVm718fMfx9LaF4C38G8DesOZxvw9mA4s4Xp_xSIhr65CDgmimusRHnz7sTfxH7_1ZvHt-1OzIG2BVrLHH1OiO1Zxi06tDWPXuuBoV5hp44Ne5slza-s4rkW7NUJkjcRd4YHRde-bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت فوتبالیا اوایل هر فصل
🤧
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102397" target="_blank">📅 09:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102396">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=UKqg2sO5XpAo0qM6BTevDoSp7CY9xxRNYMNcyTRhQRRk40P4iII9Rh1lSA2a1EKlSxKBZt_N6mJIXTJXY07Vcih0Vy-7u4yN9eHNqWiNqdDNbpifTBjPfCMZMz11ULqkG7bPPJXbd88E4JimNQE3-BZ3zHsQ3GKQJbPBVuqidEU-VT3XjwUFbK9dYDDFaQFRoNXPWqhpEyvkcGkRIogE9Py0MqKonqr2TciKA5ZzKuS3DqirpAo1CtyDaIir6FLYZxXzM6IGelwjSl6M40y-EUcxmoVOXj1QYMwbzqmcDRimYpkVNAFt9vOeI-VLkq-VrPfO_NHXaa9FMNYycKV2dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=UKqg2sO5XpAo0qM6BTevDoSp7CY9xxRNYMNcyTRhQRRk40P4iII9Rh1lSA2a1EKlSxKBZt_N6mJIXTJXY07Vcih0Vy-7u4yN9eHNqWiNqdDNbpifTBjPfCMZMz11ULqkG7bPPJXbd88E4JimNQE3-BZ3zHsQ3GKQJbPBVuqidEU-VT3XjwUFbK9dYDDFaQFRoNXPWqhpEyvkcGkRIogE9Py0MqKonqr2TciKA5ZzKuS3DqirpAo1CtyDaIir6FLYZxXzM6IGelwjSl6M40y-EUcxmoVOXj1QYMwbzqmcDRimYpkVNAFt9vOeI-VLkq-VrPfO_NHXaa9FMNYycKV2dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
نظر پرز وقتی مورینیو میگه وینیسیوس رو بدیم به تیم‌های دیگه تو این پنجره نقل و انتقالاتی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102396" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102395">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_u7idLXAIG0vsP4aiU8-O2EsBv0O-bv1-Qgb5ZYNuVJw4SjcCmn6bbBHxsMBgwkb8C7-7ZpDr516zr4tOVTqiqKhhXZrSXTl71IMRiJz9SypQ83qNgFQTBkAAjtk_PaR7pAY5jeX_zmRgJsiZGNLTxJI4vaxb8rjFMJqcHcyiZm3En_iGxb4K4xn_xyzHsAFldCsg2kddCuEQMTb1ARv1Y_apexfoQar1xPb9f12w0mqKE4QPoQuWEps_813KEiFZeBWN0KhdrjCH4GxJyDtwmjeU4XA5hE2V4kj6Ne6e-P_vyUzxAZEnwFM9QniE1_MPoxWJp9mGyxkaSSnsnVSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
رومانو: حاضرم قسم‌بخورم که دیومانده بازیکن رئال‌مادرید شده و فقط تا وقتی لایپزیگ بازیکن جدیدی نگیره قراره رونمایی رسمی انجام نشه. اگر این اتفاق نیفتاده باشه از حرفه‌ خبرنگاری خودم کنار میرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/102395" target="_blank">📅 03:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102394">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laP4yYUHSSwYc9Bzfh2bBl0ZnwHtyNcK2nAk2RFvWNPSEwvdx9Fe02csrGurmyTIJPryZzPSbO3Z95zDKDo_2saEFEvXiiD656nZXwNO45ZMvX_oz4W201vN1lhPes8DauLiiZK5n795o4klZ4HfmZn2d4Rs3RdpFh4ZE6smWbGMVocXa-1N4U8vJdgE30svhejWNyuzNlZl4rqPS0Re4dW0IsuXPMPMxDRpmLoM_zOunsQzDKFYu4Sr9wmryxuYs83284VjH3_0i05UUkR2QXDi1pG4OZv8I2TUtrS5tk2SznoQWhVrIPYb8OK3H8p49aW542L8PdYqN9lSuLcWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کاسمیرو:
خوشحالم که اینجا هستم و به لئو مسی کمک میکنم، او پادشاه فوتبال است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102394" target="_blank">📅 03:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102390">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NYZbJUyHka4TPFVRci2eZ8fdLqtpqa21jx6uCz7JnYYITQxTVbj0KJ3rf5lsr4WhEQvrtumZ73B8n1Vxi0_rMZ8Kbxmf8VUywKN3iZD6L1k50VJi91XFMlk0Bh6gFMMxXUkmR4OhmsU-EH-UOSot4MKZMaP53TupTEC7NV6i7R_RVgph9XLX6wtK7GYbf02uNokvYMoj8digyF5bppNcZC3YSO5WX21OQZhS9dsdYm0Lfbe1APQjHWsWi0RslvmnxFp7nCZzgAmrDvUT-470CuIbsKo7q4HAFcR7fpj2S5qgcSIZ2XOG78O81gLZOKeEBLVfoibK9QMAxGEYhZ6DsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HkajkO8Hu5rADSKcoh8iUusBJFeE2QAS4lntFzBuqS_I3OtBpZOzr1SHshB5jnY6g7QVZ1IQvxMNRl7xOiQ7UkUWqCoI4nSSNHpXV2Xx6T-Q6DTxb_pXQtkpI1WAKsAdKj2YQirRYyndqBaB7ZVX8LdPESXTGA-pTxW1-FTVmJF7JcG6VLLmUTbguv8ALeWJVGI21ZYDLLjvZLL-ND3QJmMMRuEU2jJpjdEPwAIrVA6DurkamV8ZN-CCmBh99GYgm3a7PMdteN12I_1MhJL35CZAcMymUlBQ6mWn4zXJeHnxF7dFQZryzYr4jMP9GGWwN_8f_woxJYptgAKjKwkOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WkOhnDBCfJOg5pesjJPxJG3zkMrrCQFlxjyODOtKUFPdBno7i4bfBFMxe7EutKDWGAJefSmZwVLrdysMD134c1tZf7yqe3m8iWhRqcnW8TaWZ5Rl1K3Zz7GJwiTI38KaxmqmQTWJWxNav1781f--oihROOaCg_1C_x5l5BAAPFYI3uGch_N0eC8ISLGOumMltP7CzsbR32FXjPgCq6qeG14gcaCWDta49AK2VpS8vYJliznJXuCgYS0BKdmPisXshMUTu5YMdEWNVIOVRTn9ZnrZ3MlCRiHMqgrC9q8_U1JQELnQRoFvxgK87Or6o2oImQBB0liVxJuMxONA29nSWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ckzvb4vQbE6PcpKVP6iAAMgylaNGXwYnb3F5GO0gcFCbJFcZ2ZMznIz82qwQslXSwhjkqCMySdMbNkd93vnSyOB2EEs1ANKz5G3NdQgi5KUpWo5_VepV7x94h7zWvUtbRViCRyk3pSEIpaFeH5xXgtguBj5uAXXasfa7pQ8ja9EfWKfsibB-fKWP-VvLqZSiSNbzRGwMUgymACHlxRJjVemUfMbBwJRJsPrF-qtFvqlJrI-5QmG5TCIIVq4c0YyglOwYRVptbljtKemboOU-WGhsIRxiELYjWfr1QcBQfLKB-PHmYQuh3ro3Z5MFDEBcYK-VL-Xj7n42JXD0kDm1uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریس و جونیور و جورجینا رفتن عشق و حال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/102390" target="_blank">📅 00:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102389">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/511459b235.mp4?token=IHEXFEMrdcfu8b8HQ1pm7EBgOmcwxUKFLdOBYhDTmq9nC1O6xbO0a_PS3CT40yXv1dNy95w7bAOCvmQ3psuPbn1HUiKcsWAN9CQ6K14OLwxU5OtbTdj0K4oq1LG64BE1szkoAAIksnjwf7bbyTK1J_XKxp4riDrAwfYjvxmQwk3aXZKQohwvIDtCXgMKL4y_ffFxpO33zFZbcO0VjLwVbvSO_BUmVJFH3ANwmWIUqtg_84R9WenSYReHCZzVLzk58RdY4kVJqRaZhmgH3XzDoddYB7GQR5BQv3nMd7W2-DusHSvRdy9DELeUL7Bny104y4BgDSAi7FCFroDxgKSQNUQa1yNRkn7kDTs7_J02GiT0Ur4ctdUl_mlT3cQ3NRz4iFUSf-gPSy_benFYCA0GPRxh9FziDogoY5fmpZf490rafzkdFRwlOYdKGzmHvCGsAZ43r-Ghgvp9QkrhtVYqKQNk4r2_9tLfqIbGrnNwz5UKz4g7Dq_Z7-Z0jglh54dsgoHST2h0xPuuT2kdvtt2qSMC5SS_m70XR9Bt3sMisV9WxXrogeoCyg98s7aXSpbPYaG1xvJL7X-QV9aUm2pQr9tmoynSPoNj_w_SU5sAfrfhs0kDDlkEAMWSLHQO6XrhCQtqJDXE-DUZ9Y-DG0UbNPJDQTSxbX_WDc-XTjYmpdE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/511459b235.mp4?token=IHEXFEMrdcfu8b8HQ1pm7EBgOmcwxUKFLdOBYhDTmq9nC1O6xbO0a_PS3CT40yXv1dNy95w7bAOCvmQ3psuPbn1HUiKcsWAN9CQ6K14OLwxU5OtbTdj0K4oq1LG64BE1szkoAAIksnjwf7bbyTK1J_XKxp4riDrAwfYjvxmQwk3aXZKQohwvIDtCXgMKL4y_ffFxpO33zFZbcO0VjLwVbvSO_BUmVJFH3ANwmWIUqtg_84R9WenSYReHCZzVLzk58RdY4kVJqRaZhmgH3XzDoddYB7GQR5BQv3nMd7W2-DusHSvRdy9DELeUL7Bny104y4BgDSAi7FCFroDxgKSQNUQa1yNRkn7kDTs7_J02GiT0Ur4ctdUl_mlT3cQ3NRz4iFUSf-gPSy_benFYCA0GPRxh9FziDogoY5fmpZf490rafzkdFRwlOYdKGzmHvCGsAZ43r-Ghgvp9QkrhtVYqKQNk4r2_9tLfqIbGrnNwz5UKz4g7Dq_Z7-Z0jglh54dsgoHST2h0xPuuT2kdvtt2qSMC5SS_m70XR9Bt3sMisV9WxXrogeoCyg98s7aXSpbPYaG1xvJL7X-QV9aUm2pQr9tmoynSPoNj_w_SU5sAfrfhs0kDDlkEAMWSLHQO6XrhCQtqJDXE-DUZ9Y-DG0UbNPJDQTSxbX_WDc-XTjYmpdE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی‌پور بعد از کلیپ دست‌بوسی که ازش منتشر شد یه کلیپ گرفته و میگه ویدیوهایی از گذشته من رو گزینشی منتشر کردن. هجمه عجیبی علیه من اومده! من اگه قرار بود چاپلوسی کنم الان تو صداوسیما کار میکردم و نَود رو داشتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/102389" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102388">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_FH1k1ZwMAewWQz1HZBViNIYq-gzQFvnZiw386zvuAiFTzgJ-ZNnSDYQWSSc5JH9ogWmvCG3kOx1SgQA-mdsoM0F2BSK0vG3L6Ia3Bcdly5PKRmEIodXyGSpu1F1QyC0L4xmWHOIVM_xLmu_8BKn9bNAWbQul3xJcDDfAtKGBmEWqdI5evhpQR_oMwakrdwoX1A5hK4Yc_4f_q2bMJidCDrkBHOQ7twNKjpQsfRkMRdO55zNO24ZU5YAL2OGk5PoNQWsuc0DI2vQysZZZaC2HiMobc1mwdgP3opn_zhHILx7bQJo4lbp_7XoyENgKigM3EvPSdrG7XSUQgYT2Ui-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری: کارلوس اسپی شده با بند فسخ به مبلغ 25 میلیون یورو به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102388" target="_blank">📅 00:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102387">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NITs-2flHMiUvHBj0CFL_NkTZmapdAX1LbTrKqThhXduXbP57IaU-OKuHeE6yhNwJl9Jce3utOfHEkwZOiXexZkuLvEXqMbI2kdVgvyImQJa1a2ZKA6t6zdytE-Q8nE-MVl9DrrWyGOY4jRVtufTASJ2gU5O4vBQZyZWcRoKe3290n8Q2M3s73_n-G4V1pPaQZjr8y0hW7GgrfnsrJKgU6pRD-HFoJdpAzRPCB9fxQ0rBVzbW4WhnschNfjs-T9o4B2S9xKEFGeeow53Fh_yOjOAQoqI6qYmfxPrlA6G0sJ6FIAMni4m1u0OYyHqWLaxhFZR4P_RuurHocXO03C30g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری بلینگهام که رو دستای زیدش خوابش برده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/102387" target="_blank">📅 23:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102386">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae65f1051a.mp4?token=lPBud4eys8u10gZff32F8Fh15jNXcqkdU8Hd1h_0lMnwUR6-dSKAHzEVKd0PPAzGPF8FMLSg7Q73pw1CjTpe97ioTZlqcthXhZgqPyvfrdAdgkk6N9hlM-045MLD6z8sjJf6Yvzr1RKarfXws8YcLR3y3inoxUjjwEmvNgtlWslRjtfhtHbY3hXJbZVQSG5gvYJcpTeiNgHo7RpyPX7aM-P0V0G_O6etMRKXPE8egYOV5WKQ59vpUDn8NUr4vz3-lHpeaBQD_kBUqeZuByvGTSH4zdQsXPFiR1vS-d9Kg_cOn61C3QHbQBUciY63dxfvcovck-ze_0azpfZIghq7fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae65f1051a.mp4?token=lPBud4eys8u10gZff32F8Fh15jNXcqkdU8Hd1h_0lMnwUR6-dSKAHzEVKd0PPAzGPF8FMLSg7Q73pw1CjTpe97ioTZlqcthXhZgqPyvfrdAdgkk6N9hlM-045MLD6z8sjJf6Yvzr1RKarfXws8YcLR3y3inoxUjjwEmvNgtlWslRjtfhtHbY3hXJbZVQSG5gvYJcpTeiNgHo7RpyPX7aM-P0V0G_O6etMRKXPE8egYOV5WKQ59vpUDn8NUr4vz3-lHpeaBQD_kBUqeZuByvGTSH4zdQsXPFiR1vS-d9Kg_cOn61C3QHbQBUciY63dxfvcovck-ze_0azpfZIghq7fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
روایتی جالب از تمرین‌های پاری‌سن‌ژرمن؛ جایی که حتی امباپه هم از دقت باورنکردنی مسی شگفت‌زده شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102386" target="_blank">📅 23:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102385">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7gjYHAAxZy4-ZjYd8OZlECv9imyBeUgyufCnlzs1oukMgisFNyC759ZCJZ647wcgQ61JHd4aTD4S3zQh6gbqtdhZFUUN4W6gR1swqgTtmTtve-R9QyJyXhi_a0GvKO3pJ2PCahLLwnO4Zf9yDoQyPzLipIKJDlYW6pDVFQ7ivr9jk3RrMy6NZXzOPXK0I0XYNlwzCvBHeqpy_xM8OjudjMI4PR3zpO0yRkamKFgC_GCNZiew132qnoqz3TvdtsUsRiK-GPVP9MlvzAPTfocrV7s3ve9mO8GosiPXCrz6cyB2zWhAJ-nC2L7oNzfDmtggraP_h0MAj2CW4AXPH9E9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اولی هوینس:
ما حتی به امپراطور چین هم اولیسه رو نمی‌فروشیم چه برسه به رئال مادرید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102385" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102384">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh_pvFLaf7QMLfIANROO-l12KwALbKAKdMGYajKnAHO-mLeVDMdRv8iDSsvhQVH8HGP7pD_7CyI68n__TC5r6h2vChB5sigiElrMFneLgpyi951mU7JfQizKOBYranH1rXV7CBLdV-AZbaqCRCNDyWMiIR6wBzIlbvMXSuv1IzwaZpVxXjR6UYr98_q-a8vcOr6N2RJ28o911hDZiz4BTi0pPfogA_HjP_Ka8PszmBcyMOnQBQVR3yl3kz3xluG5MbK7IdK-4dwi_ver-MfX00EsSCFneMbUCKGbSNefqHvQLBSDmDwtENAXlXEf1EsnpTJ2y7CM_BgYX-0CveeR3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال تو این تابستون شاهکار کرده و همه اینارو فروخته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102384" target="_blank">📅 22:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102382">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/atWAmnSjT4bprpfIaEEOTqmQEK0lVlhWX4MFUKKkbfKVy2yBA4gfX8eAl5srgv0OjkqthUZqkU6bLyeXmL4pvKM8LiwDLJBFuZfJ3dU4JLcFEVO2VLYzIM1Cdzag9KkTYsUMvBBEx3TjL92DhsUcz-39EgM8by_ytOl8HSwhKKQzfbO1Pib0frV8IoCYocnrJifarS9BNZ_DwDYsMMIGvjPWBsG1b9_G5OW0nMOB6F2qo_9tcXhO2SyWXdQQIEO2rsGBF1ZZNPkelThiLWc140HjcI6O6uOl2XhVYaxkRa_nQQLC4AiebTWwzehN0Tx1Yd2gAtnblcCqDxPUMEqH_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BN0g0idpnp5pEhy7iWnIy5TYZXOhiGO741nMfjLwkae6rK88Mox2sIpvFo7wuMU_enF1LJ4_XDeb0e0SDig30H4OxGf85rADY4J8oiz8TEB8fA3zKo2aZ2wKyfcmrs2_p1GCbHge2KSMp01A-ssch7QZL08NkLhfRfDXGqTPzuyhZ5Z4mykUxOS6gwyHGtZxlbkEjW5lw9pNrwAzJPluDZpH3hMb5qQ4ZMSYP1-w9ftvXPB6GDH79yK-WJeWKehvoKFL20exw4KUsegne3EA9Og-1EbjIkJCDZW0SdXXqxUS32bEe4FKYYK0wAcP40eshQy9nZsJ5MPwIr0EnpN1Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در 2003
🆚
رونالدو در 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102382" target="_blank">📅 22:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102381">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-text">▶️
زودتر حرکت کن؛ راحت‌تر زیارت کن
🔹
همه راه‌ها به عشق حسین(ع) ختم می‌شود؛ اما زمان سفر می‌تواند تجربه زیارت را متفاوت کند.
🔹
اگر سفر خود را به روزهای اوج تردد موکول نکنید، هم مسیرتان آرام‌تر خواهد بود، هم زمان انتظار کمتر و هم خدمات بهتر.
🎥
این ویدئو را ببینید و بدانید چرا
«سفر با برنامه»
، بهترین همراه زائران اربعین است.
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102381" target="_blank">📅 22:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102380">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eloQMACYoLtYSnLlaQKzMp1mo6au8BE_QCyUZ1h7nWa1hlLHfIg2MoDjHWCPqzRTz4nOKuQP8e3EaHaAvGbmgCnq0Ropbupm4GYe0NXOXR67rAAEgPtCtFSnoEFp0oDco_ZhBhaadMk_R5ZiI1_5fvSRAmjOCm9d0c4-Ito1lZGgQoG_G6viflTzsVpqGwsaejz37l5rxvH7wKYbi1agKyu6_upS5SIC4K2GXn9twbAPTWN57f7OuUcCjqkcxHVLO-FwfenSb7fuUYS-ZgU9ssHdmBfbK9iwXFCUc1VG7bGqOMtFFEXoBt-w8F8Xk0T2-aXpxkVIxIp1x6aUSmPeJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری: کارلوس اسپی شده با بند فسخ به مبلغ 25 میلیون یورو به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102380" target="_blank">📅 22:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102379">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuUiImotJDtaKl0CtiFz0RUAIYr1H9LJnZaqIJHQoU_MTyU6Ec0yTrOngYDR-Vt4rEyqhUaX0cNW8ccci7CCSPJgsEXJLofUHsNbwvbXF5n7Rfs2FvqRCVe5Ykx9jrAZ4OFSzRLogroCdhsbhm1PszVGb6IIoUt12MovNUSHIhGRws5uyW7V2XegVxOTnO34JLSJyTwOrUqDybRwUeTFdvxe7rDyGK_9pOG2a5c-fb4MMDfILWMYLGcabuCn3Yn8c6RQcyrlcI-GPuKavbL3V3hywoYARH94JA0oLL80XoRkeCl32yXd3xzab0HCH6GRGTo89_Vhql_rd1efKNBs1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییرات وینی تو  فیفا اعمال شد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102379" target="_blank">📅 22:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102378">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jce02MTBaj9xf58a-OPOlAEB4j8j7ohGVat6pg_HtSAWcha9_vsLQ2g1co2nZD-GnmBuTgzu89EV2A7Ilkkr2NeB8Z7sHWvy68MDTwiSNfgOGfzClctpDiLlEXM-xujANXy0-lvY6TgWmCLqHP8iugjFEevZiqUfn7jCDatWZmp_EGwnqczBIuyFZ_RcJWPDUpR5HUC5zYjeXyjf6tIcXY66pCmkLxXvHPoT4-Prjt8wntV72psH2Npo_P3LtoTdSGLhGWsDFf9FanY_ZvFTUsnxgS_CfFlT6uKR_9Kh1BbnAc0H1MRlHDgweVrWe88D-pDA3Sz1WVt--OMp5DK1DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بایرن طبق معمول به این تیمه تجاوز کرد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102378" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102377">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0VRj1njnHvAdjlMAxM-4WW6Yao1EZcvjxA9itlv1IqvGUAa3HIRhPTwDRbjvJylSkHs_dLDiZCnXHJUC4sURFVKw7_oS6RB7t5suPNQYpskTvH-1ibnjhlPxRTmF9NOhh3oH0nVXP0TO3Sa0blfO-7k-SalLij06Srnj5RlrLLrUQpK8zg0uz2HZ326wJMXl6rK9I-Q3V3680e8hlF40AfCEf7XLX3obK5CUKBClH7GYkFLgvC_fKQUI71chZZdBmn2UeTiot3RAulUB61kwUg_cEmRVeNPZ6l6f3JBQkOPLNDGJrSf3KbOvg7pReQXFMIiZlgnqS5B5KmNMB0vCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه فدراسیون انگلیس:
ما در کنار همکاران اروپایی خود ایستاده‌ایم و بطور کامل از موضع مشترک آن‌ها حمایت میکنیم، ما با برنامه‌های فیفا مخالفیم، جام جهانی متعلق به فوتبال است و همیشه همین‌طور خواهد ماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102377" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102375">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TULZAk0S_spW0zjpVjI1qpO2bfB-uXPyXITEbYRky4PH7L_ZUJZZScbUWYZ00x3jkNk2Dh6fUSihCzaNcFSp_K7AtraNBIT_OrCbZyvKrpxH91itQVW7_MKqRlaXzWi6McLn9Otpfr14xGudmJRQ6DhGzv4P6ZOmQlJTIV18ScQqo8n9BSqHxaNKS91a3g2xyznoZk8aXIz0GAT4Doep3MarQ66fDmZ0W3dfPxaNZoY7gqYtVV_tAuhDaKxAkUMBWLpmwAJYI_F-f6h1D97YnfOCMBxGSSGRF4Yzed-7eSqKJtwkrvv83R18pQrIeE0OVZdPopwPaxifj0JFmyyn0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
اسکای‌اسپورت: منچسترسیتی برای فروش رودری حداقل ۷۵ میلیون یورو میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102375" target="_blank">📅 20:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102373">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsTqRVuz4CU3pEu8mfQX2lnX5Xz1uim2Lajmgn0YUD3zEBX9oLUs2ZFzgHxzdaHz7Ej-BiiVJxJLzUpJAWwBXIkSYGuf9lQiHAoA5Qzgm72SFgDdYYJmXMmqyO6YW2Omv3C6nupYstWpm8v8pUcNl9KK-Fb36UcgY-iE1upvZp_2grSYaU9ocR8bOqKzv-JKaEATOb0cnEJITgO6Q7w4zelg-SjW62PB44kZQ5D8J54AY3GLQn4NFpeQVsbaAE1h4smUxAJXDfqMLODmBx8HyHUfrGy8I530Tf318ZyFAsLpDxwGaWK5X7Mjve50cYkkhL_KVLQkbelDkyYLKLo7vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d9c0f441.mp4?token=hVCz1rs7DSyby-1PkdDO1IFQRXL8NGnSvmkXxdIaJm6raUMlFDtIlMYmug4syzIl15K2PIjN5JeYYD3Yb4yWgd0zS618CoSlI5ObuYwWWLdLC2wS68bISPX-qKgzMd59upWE6Wryh3JE7IpxM8VwO-gM7kRI0_BtWh8JZIfK2YQuZWA41GIRMtotCvgYfsw4L2j4iOl1K0f1KhFtl_ZQ1OQfzqzC0cjVefFgAC8XSH_VExcStpoZP3C5OHAMZoloXp6A9GAPbZN8usMlz_T0M3-ZVhAsP25Tzw6MmQZOf5YwZIjbWhcGANSkqP2AisoLYwlLHLO9bpdixDDFSpNIag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d9c0f441.mp4?token=hVCz1rs7DSyby-1PkdDO1IFQRXL8NGnSvmkXxdIaJm6raUMlFDtIlMYmug4syzIl15K2PIjN5JeYYD3Yb4yWgd0zS618CoSlI5ObuYwWWLdLC2wS68bISPX-qKgzMd59upWE6Wryh3JE7IpxM8VwO-gM7kRI0_BtWh8JZIfK2YQuZWA41GIRMtotCvgYfsw4L2j4iOl1K0f1KhFtl_ZQ1OQfzqzC0cjVefFgAC8XSH_VExcStpoZP3C5OHAMZoloXp6A9GAPbZN8usMlz_T0M3-ZVhAsP25Tzw6MmQZOf5YwZIjbWhcGANSkqP2AisoLYwlLHLO9bpdixDDFSpNIag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
استر اکسپوزیتو درباره آشنایی‌اش با کیلیان امباپه:
ما در مادرید با هم آشنا شدیم. حکیمی به من گفت که کیلیان خجالتیه و خودش نتونسته شماره‌ام رو بخواد، برای همین حکیمی شماره‌ام رو از طرف اون گرفت. چند روز بعد همدیگه رو دیدیم و بقیه‌اش تبدیل به تاریخ شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102373" target="_blank">📅 20:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102369">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xy_W2uJxCH7e-wn70-Kczs40pNPmc7Ik3zEEsmTYyJvWnyhkSP8fX70GXl6E0a_0EQJgOJ_0bC4RTgqkckwBel2J1urcnAE1UYGLvDhX_MucRrWhD9cEjiFxzkzmt9DKqnGKCl6IFrswhzPiW1wCzsmFScPHJhfQ26dE7TymWZUqlbhL4s72kqUH-hHVIRoR4r8oZ8Wm7LE8JiSWLJgPOVJM-evdTKrzPuPh5UoT8V4ZY-dlyjpmRbWYmvwaGYZ4NnfRxdk5vXSJ_OWKZ6EuYaA0eXKu2KOkzQ57AjroWWjOTHK2njFMfwwG3-d03ssuxW7z1GMb8lh_XM0eFvZXbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6BI7W0Rf60zaR-tVoxa3aBqu3LLcAoc43YRaBve4FODQHyMAJaVPJhF3NH4wBYglfP3am8gfAlIBSK6kjUofThHJsbvIjTJJe46kJ17odfTVSG8qZmNqCKpQQ3kRkxA9bh9rmuHT6wR8Gy7oiCqOZBEt2pJvCUSUQMas8xza7U60Pup1HxWFpxH3y-nol5FBrmqSIVfVNrB4wI8oLy1LCS7eX9RrK1KpgaAMIopNxEvJxHeKj-6hwBPUdG0_GCIttMfQsTfROBm6P6DEsa856df2BRoIpXMRf2dzLAbh3j-eDWPU6nQnkz2aiDVT6-oOD6tMvH8srHWJXJo7BV27g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNsIiq_b1HYAMetLvZ6GgkcbP7d6OM0jeTG8uRCXCLaAav_LDxajgTMV_dVPDxK6rIQu34sa5fVPjlvXnIzXbvkO0iGE-aF5aE6X0Gei0OPDp33R8Z5PNnH3AyNN94uPXMtcNowIx9yXEUoLaMhv5vRX_DMaHRAeX_-uAFyb8VAzfZEYyQk2lpjsmC12bqESB0dOwoFQSdISUlf9D4FL5F40TayVrqqd_DO0XneIfZBpimDLd94JhxAMG0iuwgTt2nrKSIF9JuQ7CDrHDaNW16DnPPp84RHIBo6oNnv59xSNaDqiWBCws1wuEskSKevA5rptw7ISr2ltUyNXooYBfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BoPWcA14LyabDBKDtguIuhSIHE9advbEn9EaZkJTu9KFyfNoA2EQQ81YI3K8lReCtfV7ZSB3ac4BWB7wwZaPjkkWg9fyoJA-WKnCOJ-MOadXIN-zyF2Q5DfKTRnU0aCoVxL5zRDvefY9gigtItYvXydtcSV7ZVVB-Jnqolsp3QeqwuDK9ayo1sVWseI3KpoY9hpRzdj_9J4flkJfEeMXs17_MEiHqbbp9vZUkAP8i61e-Y-7ypXLDHlAignXdgHmZJMqr7cvePV3AHh-_zhty1UHPXN5T6yUCseQTpasTQO_ETVgKtd26aUUP8CNXgiqdC_eegju9rrME9U-jdHSlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
چلسی در همین پنجره نقل‌وانتقالاتی حدود ۳۴۲ میلیون یورو هزینه کرده!
💰
💸
خریدهای آبی‌ها:
🔺
مورگان راجرز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— ۱۳۸ میلیون یورو
🔺
مکسنس لاکروآ
🇫🇷
— ۶۰ میلیون یورو
🔺
مارکو پالسترا
🇮🇹
— ۵۷ میلیون یورو
🔺
ژئووانی کوئندا
🇵🇹
— ۵۰ میلیون یورو
🔺
امانوئل امه‌گا
🇳🇱
— ۲۵ میلیون یورو
🔺
آلوز دنر
🇧🇷
— ۱۰ میلیون یورو
🔺
دستان ساتپایف
🇰🇿
— ۲.۴ میلیون یورو
⏳
بزودی رسمی میشن:
🔺
والنتین بارکو
🇦🇷
🔺
جردن هندرسون
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔺
دنی ولبک
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102369" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102368">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b486c4e528.mp4?token=ntY8M2Gvfm33q4oln70ndKNnWtRdoAYsJazOY2osEi-9Y2FK-7s0arbQ_DwKGhnZ0utrBbhH0ZAdINGJ4cFJUWk7SaOZ32it913Y-A6J67-1kqIwR2NdmlEgSrfhXyClqZRquSRtRiCJsq7CQvNdTWkO8DSxwRdTZOBzajxYqS-hNo7dS7-ozNxBig48q0pTBAHiMupMhit3BAyFKDePW2Ojwd9fT8jJbkqvHJcMzyIWSbiC-wIJrConu-us7YltPj7H2NheKSQvp3sAVWdyKwe1vv21vgKg4WMD5kqQ41HvzCsGqFUaJUmnwrhKu1O3EFkPSbsTUeHG6rb3lTzXtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b486c4e528.mp4?token=ntY8M2Gvfm33q4oln70ndKNnWtRdoAYsJazOY2osEi-9Y2FK-7s0arbQ_DwKGhnZ0utrBbhH0ZAdINGJ4cFJUWk7SaOZ32it913Y-A6J67-1kqIwR2NdmlEgSrfhXyClqZRquSRtRiCJsq7CQvNdTWkO8DSxwRdTZOBzajxYqS-hNo7dS7-ozNxBig48q0pTBAHiMupMhit3BAyFKDePW2Ojwd9fT8jJbkqvHJcMzyIWSbiC-wIJrConu-us7YltPj7H2NheKSQvp3sAVWdyKwe1vv21vgKg4WMD5kqQ41HvzCsGqFUaJUmnwrhKu1O3EFkPSbsTUeHG6rb3lTzXtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🔴
🔵
تاجرنیا: «ما و تراکتور، بصره را به خاطر نزدیک بودن به مرز، به عنوان ورزشگاه میزبان انتخاب کرده‌ایم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102368" target="_blank">📅 19:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102366">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjZjlBEDD-XCtpMUQq6TEiKO_a0PdPdxIPNze9ZOS7UVR1fskcA_DQT2JQkULgo8XDsogfadl6qOO4xPtwKhVRcCxrh2Kf8qaZrKDvhnDxDeojXmsQYH7v6kumIlLJlp4FiAlFO4BMn4JWGjiOaekGdTcgKIwWeezcgJqJffkgMsr1Wpdtfr5d2_TDhJ77_4x_v1KOir23RBzGZuYgVHm9yhmACbI37MaH2S7UXiJspMcGDsmgcRu9Dhnyf_cT00_WUWuEJcenOxF-e48vQaaiVTCu-JPxQbW0W1nnmE1JsHaLdYxkEpqqp-edehV3_0Z4ILQ2wqWD9SP7JIDGj4zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
✅
تیم‌فوتبال پرسپولیس در دومین بازی تدارکاتی در اردوی ترکیه مقابل آلانیا اسپور این کشور با تک‌گل علی‌علیپور به برتری دست‌یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102366" target="_blank">📅 19:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102364">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFEH8zQ1uuqjhO6JY9SC8u7mwo2Xp7JkSwn9LiBwNytlZIJPXyEPAkUXe8W4IG-XhPMGD-R_9AJi5kHIMHruTsyToClH33CeZbFfEDHjfR6HcdXdflOpDEJBPQD2p2LGRqiRNgjKJTPzp5oTl-lyOZsvBvSe5DYwoXrGuPR-li97Gg1il0D6yDvVHXQBQTt11YRD2YL3_5IcghV6m_OXL3ypiyIO5HfVzlvB51RDdoHuQVtwMbma6bM1MZOmfiS318e4SQrOJ6mi_RLzYdxxKX1gFQyLLG9T-0mOmP_TotPcetVmz3iwRlId7oNqCN-idzpynK-ut8V21NRf1hgXyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08c0c36c9e.mp4?token=FI1X9G7Q8dYoixaCpRkESTvKaSssGN0QmcdNPCB_pC7ARXt_gXOcZ8ROx-Ci09wNG7mQC0xHI6-YsWW_x4QKoOuBpH1gnc0eiidn0n3tjRCLafzMY2mLZ0CngI632EjrFSHj8dQQldmz7LtwHQn58eNT1DVN2cIpfHTtQX_fDXkJaiMOrSKFuPKCzMMMzsmHtn5KW1gMsK3Un7waTPoVnPK24FfmeeUabrPTFDnn3VndMFxO7ZDjM4h7GiGbGlu9ioRauK2HIKptTF5HMRLX7qbKWAapaEsbAiW7EmwRbn2gMBzZBsO5GCGwbxTqOZ8eUh7IlcRIQ18HyuC_qP0JFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08c0c36c9e.mp4?token=FI1X9G7Q8dYoixaCpRkESTvKaSssGN0QmcdNPCB_pC7ARXt_gXOcZ8ROx-Ci09wNG7mQC0xHI6-YsWW_x4QKoOuBpH1gnc0eiidn0n3tjRCLafzMY2mLZ0CngI632EjrFSHj8dQQldmz7LtwHQn58eNT1DVN2cIpfHTtQX_fDXkJaiMOrSKFuPKCzMMMzsmHtn5KW1gMsK3Un7waTPoVnPK24FfmeeUabrPTFDnn3VndMFxO7ZDjM4h7GiGbGlu9ioRauK2HIKptTF5HMRLX7qbKWAapaEsbAiW7EmwRbn2gMBzZBsO5GCGwbxTqOZ8eUh7IlcRIQ18HyuC_qP0JFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اولیسه درحال لذت بردن از تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102364" target="_blank">📅 19:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102362">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6BMK8aYh5yoqxpp4SOB-myfVmaG0Cq-TElOGqmSvkwdkdmWHYblyHTla8PwOOBUVqW0eyehZ33kciWOMMYurdgU7Y_-FJh_cqGwq5mcW4QN2WW9M306Pi_5EJcF7drPhTt_tEW-sRLDU0ith3fKRG2WUBxFNwSV5pbBcShlehcdlV1YKTL_zwLYUGuhkuo-kZQq17UA8p-xbyffnF50weIqar6cINUIfvzAv6RAonMU56MP2B_WxK6wvPBnfY0QGAUWc6Yb2OQT8Ay1oOsu9hXa9CNVo1I5i1hGPWhd4puvvKQpw2ff-XP8pfD1t51InjSCVqd7kP8ifagf-IdR9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3645ae0183.mp4?token=h8aYdc0nwHnXD0TP-7R0zP9ad1FI0bmswAiDAILG9ctjpC4w3k7LUJE_Bs3LsO81_ZJNYFixcoEvpjIcToTkfEAwa7jfjBtRqNUcBBEeMj98eTKM_VZCUyi1_AdoCQAPYzuxrBXC7h1bNdQaaIQdrfSSupLEciQkWZ2z1svUwcg9xEBILaEN5FXfNenZfKbxWPuRzxE77XoSzCfdn6WLxQXm6eklY5LgFzp5B0IPpKH_Ylf788kPgXIqGwlBZ_o_dWDmaDrc707EXqRhRxqrpxgDnI92AheREGKrEaE5bw-wqW1bC8iL8Ycc6hKjnat0oYZW6RVi4JokG6lbMS2unA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3645ae0183.mp4?token=h8aYdc0nwHnXD0TP-7R0zP9ad1FI0bmswAiDAILG9ctjpC4w3k7LUJE_Bs3LsO81_ZJNYFixcoEvpjIcToTkfEAwa7jfjBtRqNUcBBEeMj98eTKM_VZCUyi1_AdoCQAPYzuxrBXC7h1bNdQaaIQdrfSSupLEciQkWZ2z1svUwcg9xEBILaEN5FXfNenZfKbxWPuRzxE77XoSzCfdn6WLxQXm6eklY5LgFzp5B0IPpKH_Ylf788kPgXIqGwlBZ_o_dWDmaDrc707EXqRhRxqrpxgDnI92AheREGKrEaE5bw-wqW1bC8iL8Ycc6hKjnat0oYZW6RVi4JokG6lbMS2unA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول، رپر آرژانتینی و دوست‌دختر سابق لامین یامال، در مصاحبه‌ای مدعی شد که رابطه‌اش با ستاره بارسلونا فقط برای بیشتر دیده شدن بوده:
راستش باید اینو اعتراف کنم. مهم نیست وایرال بشه یا با واکنش منفی روبه‌رو بشم؛ من سال گذشته فقط با لامین وارد رابطه شدم چون می‌خواستم اسمم بیشتر دیده بشه و به کار موسیقی‌ام کمک کنه. با این حال برای اون خوشحالم و امیدوارم اینس مثل من ازش استفاده نکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102362" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102360">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WO4Bi8RWNcV4V7L8tAPjyTLfWNUDjTXCaIT6pQyd_DLVELuxH_p9SS6Dg8FgxKLwWZwnv9qY9gku0kQcDmmuaFH95EWwEC67fEqOhQ3No0GcpTjMtRuE4-e-ieXVz4e9tzZ8gC3odBgBn3xL2v2uHAvz1WZ89w7fUBvcN48rlS9Y2Cc_6CIVDcIkvhsAsIjRH0MnTOIphhBYWKs2EJQA1Cf3Mkz6Gh26T0RNWH2wF2Z41gvWwtmAuNn62UncBT6HWbtxFQ-cNrvMT745UO4DJp5uPKYapy_WyWtrO33n4kBgnMQtZqvPbVCLhVidG6eqFffY6e4HcurpaMwX-Y-Hjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IbmwR0B1OBEv3cdLqTxBBW_pkdwLE9x2BPF1aBL3lSQWxGhQ_vPuYT6vbG2mBpsyKdsqQgwQhzyHR_Iiu4aUsUxJVt0TpQd6yDJERVPYaHf3dpJAPYs4lD3OzTwgRvjmPc93DVACN4sqh9CUiAscW3nzEXcDz7sOgKGkKYdyOrLSlQp4Kb_XNMCQzsDCkearebUTi2LPS0O17MqSpu9aKZQWE7L5RblZ8hPWHR_nqOVlJbzApRYOCd4wNtaf7U0RE-6OuTZ-6VR-ta_i5a146dqxNspWSIH2EPMdto9OyLFWQSqT6FcbKGFxaarYQpYicEs_Zv_fTsT8GE-BOn7leQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇦🇷
طبق گزارش‌ها، لیساندرو مارتینز و الکسیس مک‌آلیستر بعد از پیروزی آرژانتین مقابل انگلیس در جام جهانی، برای خانه‌هایشان در انگلیس نیروی امنیتی خصوصی گرفتن. گفته میشه بعد از حواشی جشن پیروزی و نمایش یک بنر جنجالی درباره جزایر فالکلند، به خاطر بالا بودن احساسات و احتمال واکنش هواداران انگلیسی، برای چند روز مراقبت امنیتی در نظر گرفتند. البته گزارشی از حمله یا خرابکاری علیه خانه‌های آنها منتشر نشده و این فقط یک اقدام احتیاطی بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102360" target="_blank">📅 18:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102358">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lUecA82JLo2NbaxaVo3ywIBqN3QwDJmecRm7fdkSyigS2KSo1FfvkVxQyVZiHqkls-xuydAW7nsrE0IZNcZGg5V9RM7eng-E68xV2UrcFPOaCAMfpgbHPCif7lq9yYdTXO-EXDGrLayIpg3Fa1guCFwElcK8KbrY-KkQxOeucuRdi4BhSjc7r7opeE6Oh_Iz0kHmky_newm5RQYl_d4Z55xF1zVCDEbg98vwNo3T3AreEowlkK08wW-aIVkmX5zNtU6MpV-aBs52ep5M6XZhc30Xo0Nln-HzoLSaVP1Q_pStWz9wXBjazEaOQUL4SnevREZThjPfSs1x9Bzs0V3gyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ltLXLwikUDJGNTM3KiHXjglaLoCPcMP7rhKzcOPGthkFHux9XNM7vznCpTXSF_xjCWHLmMQuYaWEh-3kB6WNtBBuLhCBAlMNWcTd2k083VnXycydqqLQP-kBhxj36fhPS1RJQlVEopHn-ZTMBmSuY0TnSjkR_x5kPTwy3Plz3EIrAe55GZCe1IbANhyx8D-jdpRprDIvaDBg0D4gWqVbCn5Hijioto-f30wibFXbL8YS73jKEnmdXUmw68BHxCSA4vlv4F4hnb7iLO4NBv2LxBxm1Q901MGROjuqYLJ9tfprYkVLcdb8SeIg8E-48nElS37OsYeum1skm8ZRm6lLPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
نیکو ویلیامز و دوست‌دخترش آینهی گارسیا جدایی‌شون رو اعلام کردن. طبق ادعاهای منتشرشده، گفته میشه آینهی نیکو رو در ایبیزا و روی یک قایق در حالی دیده که مست بوده و کنار سه دختر دیگه حضور داشته. بعد از این اتفاق هم وسایلش رو جمع کرده و جزیره رو ترک کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102358" target="_blank">📅 18:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102357">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e33cfddb.mp4?token=iFUb28aBqfabKv3ovw6bLUo0Hk-pKHifW4eAHqT3aUZ_mZQp5fHuLd8abxbcCXnH05cf0-kOwcJkWY2Yc-jy3VcO4rW4gu8zvh1rIogoeAy-BFqkY8OGYEf8MR6vKyyreth6g3gGhpF0jJqGdJ2E93Dj6zNgrq1u1EpLl3edBNeaavK7J-PtOdG7vzUhIppHDNJGQaaVhF1VVRjk5x1Ygm9r8jhKvTA5mG-eyO_hdT3wFfmsWHXRw6-ZvCca59tUvTVngOPSpE86IBplLp7lDWlwFUMCv3pSdBz3bPSdOM-u-6c5hSP8NHF6HBgf5SP5_afrqH5HMyl05Uoi5hGLkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e33cfddb.mp4?token=iFUb28aBqfabKv3ovw6bLUo0Hk-pKHifW4eAHqT3aUZ_mZQp5fHuLd8abxbcCXnH05cf0-kOwcJkWY2Yc-jy3VcO4rW4gu8zvh1rIogoeAy-BFqkY8OGYEf8MR6vKyyreth6g3gGhpF0jJqGdJ2E93Dj6zNgrq1u1EpLl3edBNeaavK7J-PtOdG7vzUhIppHDNJGQaaVhF1VVRjk5x1Ygm9r8jhKvTA5mG-eyO_hdT3wFfmsWHXRw6-ZvCca59tUvTVngOPSpE86IBplLp7lDWlwFUMCv3pSdBz3bPSdOM-u-6c5hSP8NHF6HBgf5SP5_afrqH5HMyl05Uoi5hGLkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی ترامپ‌نادان با بازیکن غول‌پیگر فوتبال آمریکایی؛ بعدش که مزه میریزه از اتاقش بیرونشون میکنه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102357" target="_blank">📅 18:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102356">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5a8032cf.mp4?token=Wa5JFpsP4l9LCRpaGJf_jurUqu9DYlRC0vDS_371GbO30LZfX3cut7Lfas1dTgkTKWsT4gWdv4Un3FYdrwgC0ACaIsjH7Zskyey5j187nu8xLPuAyf7-mX9q10RSlZ06j67Pqv2cthZQs8DRK80cw1XMFfHbxGHzLiHR-32NB5p7VnAFi768azsKv5XH5V31c-CcwrDPmQCl9u0BSxP0OojYf6Gsyy3yBznyKVjsb9M4_eMdmPmqhgD2Sc3AAm4bCZ9fc_2JxSn_G7lQGEUMR86Fulu7XkrmRamAKtH73yhNJRfSqp8LE_nqXY6vNXx2985PkR2pAWNgvToWMk0xsqWkCSdQvDAVAJEYyXL3jAzJXbQbtAhzNUyfO2YW1er8sQcJnxEqjhZM1KRrsVPbb1ResTD4ZglN-vEKjagJ5-JjAE99lZekTRWR1MGA7dmf5s8mmTNaLrAFs_HTg73I15nqBbktzg_2GbS0EDXH-gco0M_vwlk6eclm2edaSQucnWQ22w-IseAOwSuJc17wrb7pCWOMfTBoBoKog3kevePoHUz1PJfu833bmXMWiDDyFafV1DTAb0UKwmVKBoaV736W1kRZu83nc37clScRpcJ9ZiBCgJgbaANHZWlS9GNJKxmu2LaavjTTtEXM2Q0U8vFfJ20jd0FG4mdW4sw9AH4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5a8032cf.mp4?token=Wa5JFpsP4l9LCRpaGJf_jurUqu9DYlRC0vDS_371GbO30LZfX3cut7Lfas1dTgkTKWsT4gWdv4Un3FYdrwgC0ACaIsjH7Zskyey5j187nu8xLPuAyf7-mX9q10RSlZ06j67Pqv2cthZQs8DRK80cw1XMFfHbxGHzLiHR-32NB5p7VnAFi768azsKv5XH5V31c-CcwrDPmQCl9u0BSxP0OojYf6Gsyy3yBznyKVjsb9M4_eMdmPmqhgD2Sc3AAm4bCZ9fc_2JxSn_G7lQGEUMR86Fulu7XkrmRamAKtH73yhNJRfSqp8LE_nqXY6vNXx2985PkR2pAWNgvToWMk0xsqWkCSdQvDAVAJEYyXL3jAzJXbQbtAhzNUyfO2YW1er8sQcJnxEqjhZM1KRrsVPbb1ResTD4ZglN-vEKjagJ5-JjAE99lZekTRWR1MGA7dmf5s8mmTNaLrAFs_HTg73I15nqBbktzg_2GbS0EDXH-gco0M_vwlk6eclm2edaSQucnWQ22w-IseAOwSuJc17wrb7pCWOMfTBoBoKog3kevePoHUz1PJfu833bmXMWiDDyFafV1DTAb0UKwmVKBoaV736W1kRZu83nc37clScRpcJ9ZiBCgJgbaANHZWlS9GNJKxmu2LaavjTTtEXM2Q0U8vFfJ20jd0FG4mdW4sw9AH4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
یادی‌کنیم از کینگ‌کمالی از اساطیر بدنسازی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102356" target="_blank">📅 17:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102355">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a15854e8.mp4?token=SDG9U6C483ktaxEZjNtKOAYWwpdU9MtVHPluTSBL2ERxPDeNaFnidgb0tAPz7gY-4u-H-V4gtvQapvnY5n8b1qWytHOc1C75HpDuATB7a74fq-ZWBSe5FECGZAep07OH6-4VJPIRcwT5AxeTvafZbpmcy_XBn6KglTKsVtqL2XsmbpbmtzLp_Lqq-t0p-s1l3RjvpmereEWGYX2ojBBtINdSc1EM6UW_MTMCEzwajiay3Fiizp90dbZw4TMro1TV2l8jNK7e3LyoYuab5SysJ-ybYSOvdzjCSZ2jdnXD5aG25QqyL7UfFDb5_y4X7_-hPyezvNHJUorxn17qf5YxAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a15854e8.mp4?token=SDG9U6C483ktaxEZjNtKOAYWwpdU9MtVHPluTSBL2ERxPDeNaFnidgb0tAPz7gY-4u-H-V4gtvQapvnY5n8b1qWytHOc1C75HpDuATB7a74fq-ZWBSe5FECGZAep07OH6-4VJPIRcwT5AxeTvafZbpmcy_XBn6KglTKsVtqL2XsmbpbmtzLp_Lqq-t0p-s1l3RjvpmereEWGYX2ojBBtINdSc1EM6UW_MTMCEzwajiay3Fiizp90dbZw4TMro1TV2l8jNK7e3LyoYuab5SysJ-ybYSOvdzjCSZ2jdnXD5aG25QqyL7UfFDb5_y4X7_-hPyezvNHJUorxn17qf5YxAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
وضعیت این‌روزهای هانسی‌فلیک در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102355" target="_blank">📅 17:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102354">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=ne4Xi2LTpD8kOE_kLP0OC2PjeZxfRzROR-1Fvb3jrrJlKbfFIJhhYMx3qgF2zvPd1UyEstdkKk3c7lAzrMp_hIr2YHS-ZiPDxAyc88iKpQ6O8dbK24PxVPqwDnKQe52XDuRFDgriM6WQ1Jh-UAM6kh1qWtk6x2DV1RmkLu12rXAD8cot5JMsr-qZk-aE_gozc4PBGNuXjS31GocWaAJ_I8KmsErVRBP2UgF6kEYrC4kCJZF4SV2vPG0H3kgCsPNYjqoSlX3mDmetiw50VPpZiigbZRwMZG62jumRMoQwLpmbr6TwOiMhqLXX9jIBxsPvZwqUrkj5G72u1dlT-SmXIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=ne4Xi2LTpD8kOE_kLP0OC2PjeZxfRzROR-1Fvb3jrrJlKbfFIJhhYMx3qgF2zvPd1UyEstdkKk3c7lAzrMp_hIr2YHS-ZiPDxAyc88iKpQ6O8dbK24PxVPqwDnKQe52XDuRFDgriM6WQ1Jh-UAM6kh1qWtk6x2DV1RmkLu12rXAD8cot5JMsr-qZk-aE_gozc4PBGNuXjS31GocWaAJ_I8KmsErVRBP2UgF6kEYrC4kCJZF4SV2vPG0H3kgCsPNYjqoSlX3mDmetiw50VPpZiigbZRwMZG62jumRMoQwLpmbr6TwOiMhqLXX9jIBxsPvZwqUrkj5G72u1dlT-SmXIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
‌‌ ‌ ‌ یه ویدیوی وحشتناک ۱۰ دقیقه‌ای از
این حرومزاده منتشر شده
🔗
🔞
مشاهده ویدیوی کامل</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102354" target="_blank">📅 17:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102353">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzWkwgD73fnn_3MMeBd8jS8zu7Vmo9PgWBiB7AUE1upLrbYRdfdzbRLBFlIer3aTSQGWDBiSvfX_QdS5_EZAfkm9utZhjOp6O3TkrLkDE643_kOSBnTrFZtua9cwHGjbxNNNSGqn2vAVQlweEiq4iLhqysg9ymrBXItnPxPn238IJvTfxjc4GuTIYnAYiXBnSE3bbW_b30f-NaT0zXn0VIM1ydEWxZ90kNpYOKc_7IivL7_r74x12T1CUOzxY5Q_NBco3kEEp4QoSXPiGhSOn-uh8Ql8pDLSgCG8zRLSpvMoBep66vx3ojJueZ8CMCk4pOzCR6IqCC0grxyfr_9k7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
رئال مادرید، پیشنهاد رسمی ۵۱ میلیون پوند برای جذب رودری از منچسترسیتی ارائه کرده است.
❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی قصد فروش او را ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102353" target="_blank">📅 16:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102352">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f25fd06c.mp4?token=iMqRRBGMTO-n_xgl2F4t2fDFgLfz8tqw4-H0NyJ04gpEGkK6ybQ3AMnrY3Rdk-vcW01EDow9iuPYKKkK2VdtP8FZnTZM_q2YtumgucGjpDezgRoxodwtBQrpgwSqMR2CLbGW0xtWjCow0oMjoT_uU1XPWY2XRhmTnRHBdus2petk5VARhfLStbyXawXaF9bhhG3T-2aNzGzbRnwaDR3Lbf75xpvtfsrdoF2iHtHbT7sD13lIIw58GhbzFVm804zDAVgjI3YxrfQLQskqU45UrbtxhuZZ0iSwbTPlrojX9sUtvOnHv5VmU6COFpo2ZRLjG22U-recojyONXr_7co4MAh_gjZzDWQQWplK0o4hya1dHQo96vHS5bLBiEiCIat1Ev9kaKXHilOSLFEbHKUfSRNaF08kuvia6oEt1k3x5pDsQhXtnlFTaPdcdoVb9TdwCwaB7YtvgQO59W9bkt01G95yJ1Cy5E978BwON8l45oKKgN6xGxxZVMGk_yMOwI1UiMIDPgKJBOLPAg1jTc4An0R38sOHP9AMuLRkuZfcn9OCo2WtGvHnOP4D22WU924MGE7FOVzDaGsnHpC6HokPpLeQ0wuhTlgDfIKVUvHkaGLacwVRBKvLnqeDXQtJiYmxwHkWlbEjdq4E_st8MHgJX6HdhJCgg7pH6yxEqAAqsyE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f25fd06c.mp4?token=iMqRRBGMTO-n_xgl2F4t2fDFgLfz8tqw4-H0NyJ04gpEGkK6ybQ3AMnrY3Rdk-vcW01EDow9iuPYKKkK2VdtP8FZnTZM_q2YtumgucGjpDezgRoxodwtBQrpgwSqMR2CLbGW0xtWjCow0oMjoT_uU1XPWY2XRhmTnRHBdus2petk5VARhfLStbyXawXaF9bhhG3T-2aNzGzbRnwaDR3Lbf75xpvtfsrdoF2iHtHbT7sD13lIIw58GhbzFVm804zDAVgjI3YxrfQLQskqU45UrbtxhuZZ0iSwbTPlrojX9sUtvOnHv5VmU6COFpo2ZRLjG22U-recojyONXr_7co4MAh_gjZzDWQQWplK0o4hya1dHQo96vHS5bLBiEiCIat1Ev9kaKXHilOSLFEbHKUfSRNaF08kuvia6oEt1k3x5pDsQhXtnlFTaPdcdoVb9TdwCwaB7YtvgQO59W9bkt01G95yJ1Cy5E978BwON8l45oKKgN6xGxxZVMGk_yMOwI1UiMIDPgKJBOLPAg1jTc4An0R38sOHP9AMuLRkuZfcn9OCo2WtGvHnOP4D22WU924MGE7FOVzDaGsnHpC6HokPpLeQ0wuhTlgDfIKVUvHkaGLacwVRBKvLnqeDXQtJiYmxwHkWlbEjdq4E_st8MHgJX6HdhJCgg7pH6yxEqAAqsyE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مملکت به شدت عجیب و غریبی داریم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102352" target="_blank">📅 16:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102351">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/138f735fee.mp4?token=q_jdF0TIFqFF_IHN7NZ1UE1lz3kE8N3x7qdf9PoS2nAWmU_ep2X2fKXGwcdd_vOeak4LmtjV7TDaAFtni0Tzev9GovMjCoiPA7_MXb5vZi9sJlrNwDk7AB_1kYnDMO8B5XIkmtXtdoXfjnzm9nlZlxfRiyAEuwUqF1p8_loh05Oka2uOrRhy_lZePgdBUtb3J-ydpAmAF3-p__11hnD_KemqHje7e3Jkrtk0aOtz51iig6pk--pS18UspM7eT7DQ3lGsvvvWyPOtvCY9EjlsROSC6XIzqHIHPwDNTQobcK8IqIwkIUoNCseYRCJwb8QPV7M1e4J5pIwbrLqj8woguw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/138f735fee.mp4?token=q_jdF0TIFqFF_IHN7NZ1UE1lz3kE8N3x7qdf9PoS2nAWmU_ep2X2fKXGwcdd_vOeak4LmtjV7TDaAFtni0Tzev9GovMjCoiPA7_MXb5vZi9sJlrNwDk7AB_1kYnDMO8B5XIkmtXtdoXfjnzm9nlZlxfRiyAEuwUqF1p8_loh05Oka2uOrRhy_lZePgdBUtb3J-ydpAmAF3-p__11hnD_KemqHje7e3Jkrtk0aOtz51iig6pk--pS18UspM7eT7DQ3lGsvvvWyPOtvCY9EjlsROSC6XIzqHIHPwDNTQobcK8IqIwkIUoNCseYRCJwb8QPV7M1e4J5pIwbrLqj8woguw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
برترین‌های تاریخ از زبان رودری ستاره اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102351" target="_blank">📅 16:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102350">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇪🇺
🇪🇸
یادی‌کنیم از آخرین قهرمانی بارسلونا در اروپا با مثلث تاریخی کاتالان‌ها در خط‌حمله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102350" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102349">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BotHvYuw20mA7GKQcKhNS_xpDqCwRjExI8upfEWG1SVty5AcQG0vLxVZ72pAPkEa8McsDeh2dQ-NxqHNW88is-AJeT5nMyWUzIhG6GN6ZXM6GvAhAEt4Zm0XKHrTVi5O7vCDOj9a7qODwG2gKBfW3ukyTTSbKfw13s7I7QwRpwqUGBPZa2i5gyu-4GENU98SqqezOibDTfTzkm1eAwiVi-6F4S_JxTeP8qDdZ03aVe-8ZMkjqvP_VVZWaS4UZv47iBN9jFXHHahkSEMHzqAijR3XDvjUAAQ9hZ0jZHc8lG2JM94hKFeRsBkf_brumzPth6IdWkGT7FKtD5RL0023eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گونزالو گارسیا به فولام پیوست
۴۰ میلیون یورو
۲ میلیون بند پاداشی
۳۰٪ از فروش بعدی به رئال مادرید میرسد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102349" target="_blank">📅 15:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102348">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88e7b9804.mp4?token=nHne8e95HOHJ1iu2CAH1IfbIEAFGtHRdK-8jk3x3h4Kb2L_5rvwlL6Z_S0xa5dXlf9hlOfCyZdT0w5inNBl9xnWYG1sX6O3KY7wfH6pJK3oZwahkVsy5YmB4V6ihudo9dBk6X5K2naRJtRcUM26gSXlHLQOFwBLSyEkJSr5Pf2HLqmj_FHSYRbdBJyC5GsFyO2hYXLkeIM1jdxl1ohTBy0oPG9Nwydv0_ooBWcDW0Nz0ELGkmCRqRit6hRpyRSSf0_zhh0Rpiuf5btL2_2L8CeRL3oZaHXzPtJBT2iMfKfbTg2REmPNsWP1rBnFyHoCUhhga1xQ3z_Lope-9UVQQFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88e7b9804.mp4?token=nHne8e95HOHJ1iu2CAH1IfbIEAFGtHRdK-8jk3x3h4Kb2L_5rvwlL6Z_S0xa5dXlf9hlOfCyZdT0w5inNBl9xnWYG1sX6O3KY7wfH6pJK3oZwahkVsy5YmB4V6ihudo9dBk6X5K2naRJtRcUM26gSXlHLQOFwBLSyEkJSr5Pf2HLqmj_FHSYRbdBJyC5GsFyO2hYXLkeIM1jdxl1ohTBy0oPG9Nwydv0_ooBWcDW0Nz0ELGkmCRqRit6hRpyRSSf0_zhh0Rpiuf5btL2_2L8CeRL3oZaHXzPtJBT2iMfKfbTg2REmPNsWP1rBnFyHoCUhhga1xQ3z_Lope-9UVQQFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
💥
حالا که بحث تیم‌ملی داغ شده، این تیم‌ملی و بازیکنانش بنظر از همه سر تر بودن :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102348" target="_blank">📅 15:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102347">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0063915b2d.mp4?token=HbOsFmvvE-7k7He7-frIbsHW3QrzVS-QYyfVan73okNHgyNvHQYe8MZFWKvEcUUC0VsibqfAcEVSZFAf_JlYJhGkSA3k6Ct_b02LJvaEfhwrS6DjY7_qBeaFcEA_KOATKKV30Rqw7LyIjGeZpOFlODjUmzmmeX1iJr3lT3hZuGRgaeKxIm7tLaTC5kEpfo48B3JvB-pyEqzQG6ybFH1b5Dxx4hLyHpzH36eH5GUZWFO7p8sQ7ip3sfT3YBfqmB2kGyeW74WC6Ol2G_hNsdTXgJ4ketN_Dnl1OGuDd7i6cM2BYmrvZcYvMmKkzvRRXtFBb2OJCqW7EH870q27ybnz1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0063915b2d.mp4?token=HbOsFmvvE-7k7He7-frIbsHW3QrzVS-QYyfVan73okNHgyNvHQYe8MZFWKvEcUUC0VsibqfAcEVSZFAf_JlYJhGkSA3k6Ct_b02LJvaEfhwrS6DjY7_qBeaFcEA_KOATKKV30Rqw7LyIjGeZpOFlODjUmzmmeX1iJr3lT3hZuGRgaeKxIm7tLaTC5kEpfo48B3JvB-pyEqzQG6ybFH1b5Dxx4hLyHpzH36eH5GUZWFO7p8sQ7ip3sfT3YBfqmB2kGyeW74WC6Ol2G_hNsdTXgJ4ketN_Dnl1OGuDd7i6cM2BYmrvZcYvMmKkzvRRXtFBb2OJCqW7EH870q27ybnz1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره‌بامزه از زبان فیروز کریمی
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102347" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102346">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2314f18179.mp4?token=LoLe38gW5b_E9arQcz86mqrWHF1t4xabejd7YjVXqkg6DgAV_pmxGtJmzQqZ-i-vgZLYr7kJxIZqTM7qtn2EquvRAQlN-EF9-ccb34RWKkZ1to45QnSC87zBYbwQlZPCmuliBtNVPxl17EQNpEeScH0lKRgSQGSp6i-gLFxHh76qEU8jyL0vYzHN8mJLVoqDdXP2EyWMeUTMiU4XVxQ8bJ5wQ7RF_WJ2ExITlS-T_UUKc6RDiqHkZa_oJIgZvbqE69rCvKgD5d8QwAg3Kblb4doXyfHpJF9mMW7NpeudZl2WjMET7QguNvh4flQEj_BsB44pGHUySFgVg_kfWRNFAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2314f18179.mp4?token=LoLe38gW5b_E9arQcz86mqrWHF1t4xabejd7YjVXqkg6DgAV_pmxGtJmzQqZ-i-vgZLYr7kJxIZqTM7qtn2EquvRAQlN-EF9-ccb34RWKkZ1to45QnSC87zBYbwQlZPCmuliBtNVPxl17EQNpEeScH0lKRgSQGSp6i-gLFxHh76qEU8jyL0vYzHN8mJLVoqDdXP2EyWMeUTMiU4XVxQ8bJ5wQ7RF_WJ2ExITlS-T_UUKc6RDiqHkZa_oJIgZvbqE69rCvKgD5d8QwAg3Kblb4doXyfHpJF9mMW7NpeudZl2WjMET7QguNvh4flQEj_BsB44pGHUySFgVg_kfWRNFAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
تمرینات پیش‌فصل بادیگارد لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102346" target="_blank">📅 15:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102345">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇪🇸
🔥
۵ گل زیبا در تاریخ باشگاه بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102345" target="_blank">📅 14:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102344">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e80cceff6.mp4?token=FfAIru8lT9aBzlBCFyQFvX5K6R5ZHD9cyb_w-oCDhBnogzmGP1BpbfujzkQCPShtOAQkUUpkKXOZMlIzXCIY7kFKNbL6b6usqp3PWA5x-rqL_CY_HR1PSUEyLFJssF_QDHJESG9hFERJtBF2eR-qhHhBojYxVOzJKrDPm1WDlNiZmYkTHq51gSceIxjb1sX0waKEYn-CQFpLzUh4Ux9yRsgtIixYrhZru-dGmQlR10LlwCpaCudjCIVmw2boOqe7hp2j6E2nF_XIahIOgkm9Funkmo69W-l_MCv0osXd-8Kym0mJC1yZGZNoPn59gk4mki2Jjn6t-L_-Eycjz4RmqBj6IO1-nORZhCohWUX661jT0BN9_ef9EOAhtBpJqvTLXhNocBr6h0alDhne4zUCuRE4mEtglaUjJdkx78wGl1HhLcL8CQTwsl6fFvyDxQfs-3inswverbiQSMIjog8MxsLpwFJGZH7GPLwig47pwHqTsPe_BXMFj26MZnSpMZOEctxEneiOTvzEPzPS9EdUo7Jdi84q9dswveZBn7GaeJdZcHu-E1cRsw8kr1CThT4hB6rrw6EXHSAzZsnJlAk0O2ADKq-v0lpcMGJ8Xz3rxlJdXB1XGPXutdPfbX7ykwOTsyDEv66RAplplp5s_sFM7Gmrx8VkgnTw9jG_HiJqvDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e80cceff6.mp4?token=FfAIru8lT9aBzlBCFyQFvX5K6R5ZHD9cyb_w-oCDhBnogzmGP1BpbfujzkQCPShtOAQkUUpkKXOZMlIzXCIY7kFKNbL6b6usqp3PWA5x-rqL_CY_HR1PSUEyLFJssF_QDHJESG9hFERJtBF2eR-qhHhBojYxVOzJKrDPm1WDlNiZmYkTHq51gSceIxjb1sX0waKEYn-CQFpLzUh4Ux9yRsgtIixYrhZru-dGmQlR10LlwCpaCudjCIVmw2boOqe7hp2j6E2nF_XIahIOgkm9Funkmo69W-l_MCv0osXd-8Kym0mJC1yZGZNoPn59gk4mki2Jjn6t-L_-Eycjz4RmqBj6IO1-nORZhCohWUX661jT0BN9_ef9EOAhtBpJqvTLXhNocBr6h0alDhne4zUCuRE4mEtglaUjJdkx78wGl1HhLcL8CQTwsl6fFvyDxQfs-3inswverbiQSMIjog8MxsLpwFJGZH7GPLwig47pwHqTsPe_BXMFj26MZnSpMZOEctxEneiOTvzEPzPS9EdUo7Jdi84q9dswveZBn7GaeJdZcHu-E1cRsw8kr1CThT4hB6rrw6EXHSAzZsnJlAk0O2ADKq-v0lpcMGJ8Xz3rxlJdXB1XGPXutdPfbX7ykwOTsyDEv66RAplplp5s_sFM7Gmrx8VkgnTw9jG_HiJqvDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فرشاد محمدی‌مرام درتست گزارشگری سال ۱۳۹۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102344" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102343">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWKWfF4cwbA2gT4AJSmsPYOqvffljEo6sBmCbcHaiAmemTtjoF4VzwE14JAfnSHsQHpg8YNHYM5nZIAcuWmDGiVNdxKOfY-m1qLXIsVtOkUSmuRvJcguw8dxS2K_F8UQtrTVTj0Cc7LSDMZx_Es0c8eRrRvHm0xpFG9G5CgLT4CDrakfR185UlS5C2-vB_XpCA1FnW5ochB-2cFqrM2KR9ur93Pyt_2sykE2t1BUo8ecWtACcTRwE9vJ_E6CO1P-QzYyrkaZOqXWrun_4r1Z6NA063V-O5V2qah64WUo3Pnflb7a5AYb6WTNwC_OvcRy9hje_SvccTfCJdCVSboKUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔹
رسمی؛ نیو راموس مصدوم شد و حدودا یه ماه و نیم از میادین دوره‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102343" target="_blank">📅 14:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102342">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3336c43202.mp4?token=oLQSr9BxX5LkTRlr4fywiYDEs077yA87AwGPHa2b_y0GpNu75h3TaFzCEre5ajMaWkS2lKWOAq2RXDzJlnaF2XmXUdlLI092s8vwDuPuJg3UiPGwp9rIu0q21B_X1pfQ5Yww7fCybLAu_xJ1T-O0Y1NMRwqXscPEwOmeN8OykBniSV-x_kKkgSG5oG7u_4kTf6tLG28T7LLTdF2f2oNvHL7wnwJNtIu2yoP54yibkOeXpkKkQFlOeCsnv-X_gnp83sZpelYFn5pHjcNwDei8Zg-Imio1JQc4SQXvCsmxCwEmYMhv0aP7T3q2ui_wguvNo8sXU2fOvmo09OaNMGDPvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3336c43202.mp4?token=oLQSr9BxX5LkTRlr4fywiYDEs077yA87AwGPHa2b_y0GpNu75h3TaFzCEre5ajMaWkS2lKWOAq2RXDzJlnaF2XmXUdlLI092s8vwDuPuJg3UiPGwp9rIu0q21B_X1pfQ5Yww7fCybLAu_xJ1T-O0Y1NMRwqXscPEwOmeN8OykBniSV-x_kKkgSG5oG7u_4kTf6tLG28T7LLTdF2f2oNvHL7wnwJNtIu2yoP54yibkOeXpkKkQFlOeCsnv-X_gnp83sZpelYFn5pHjcNwDei8Zg-Imio1JQc4SQXvCsmxCwEmYMhv0aP7T3q2ui_wguvNo8sXU2fOvmo09OaNMGDPvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
رتبه بندی سوپر گل های فرناندو تورس ستاره سابق باشگاه لیورپول و تیم ملی اسپانیا، توسط خودش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102342" target="_blank">📅 14:00 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
