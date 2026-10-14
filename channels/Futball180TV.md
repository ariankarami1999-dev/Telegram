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
<img src="https://cdn5.telesco.pe/file/NPgNU6Upn7n_QkiwczOxy6nsArHPrZjdfeAj97nBBnnxr1yw0fEZ6LDS2Ah_NaP-gWEFHYNpvTi-497vBifLfy_CyjZTXEfNobQ-tIgZjONrcGCba0g-1sDUc9YmsarFiGHM9-6S656QuvGc_G1stUEGZ4VLL9K--4wFBELcGmbliQorYTsYH7i1u-o5L3KWZmHl5pEAseUphXqCqqYTz8iiZgY-rkILNk9UU0-bb8dosRB5qKBf0dThdJfegHluIZ6-TwtoaBjiErPpd498FuiSUFkAYbBlLMfet1MZIzoeQcLjEfqSVwtPXXSqfqVBq4qHKP-MzqWup6BtWkm23Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 382K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 16:41:30</div>
<hr>

<div class="tg-post" id="msg-108680">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f36bfce94.mp4?token=aG-cZYVoXxI-Exl6jLqdLpEadw4rEe5_uvzeca6xHZ8dJrWGb9cvH5X5guVvV3hrfeArIjeBHTRut0Q0N95jh9o39ZKuo0yejN-GvPe6GxAKkMeg4Bs1yaTXm12FkDIWK7KamjpKwceY_06d_S-d8hmIJAjD2ngOgVuOGjiglGDrXHuJ2Sncm0ltz95Vx9_-zIKc6TU1SHSski8KsgrGDMXkSHk8NOfYJY14FF2w9rcLfdSno1ZFAf5Ah1-SeBcoxyAp8iqT3wZOD4tlN6PX0xrDn1OKYU2Y-Po0TviI4rHGGXPPYZ8VHlO0UgiIdrffIZgH1xrrLz7mLM4qMKj4bG5CZkz3C2v7PhvSib2bgHg6FqV1wu5lzmRLljjsEomQPQoCwL1W352D1QLQD_75L5BMvqomyjfOjwkUl07v2hAq4-Vh_i8mjYgtxGEWEK7DFsZSBQAycR-cnCtZoEmK87LBGdie8-GFOO97vdZ9chBjXhMYRejm7IKHqUm16vWUv0eMfdF_nU9MDoXooqrsKO7bJFUGhrYGXL6kzhJzoxrqvV9cWANYVlKanFRxkRx569fFf0hdxYREhnnbqCh-dRUVpUPcESEYLEIQR2xNffcy_gn4XhKxU4URJ84mWCIkSzHsmj4IN4JgYacVw84du5HHGQ4t6mbDwvEfdrcgjpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f36bfce94.mp4?token=aG-cZYVoXxI-Exl6jLqdLpEadw4rEe5_uvzeca6xHZ8dJrWGb9cvH5X5guVvV3hrfeArIjeBHTRut0Q0N95jh9o39ZKuo0yejN-GvPe6GxAKkMeg4Bs1yaTXm12FkDIWK7KamjpKwceY_06d_S-d8hmIJAjD2ngOgVuOGjiglGDrXHuJ2Sncm0ltz95Vx9_-zIKc6TU1SHSski8KsgrGDMXkSHk8NOfYJY14FF2w9rcLfdSno1ZFAf5Ah1-SeBcoxyAp8iqT3wZOD4tlN6PX0xrDn1OKYU2Y-Po0TviI4rHGGXPPYZ8VHlO0UgiIdrffIZgH1xrrLz7mLM4qMKj4bG5CZkz3C2v7PhvSib2bgHg6FqV1wu5lzmRLljjsEomQPQoCwL1W352D1QLQD_75L5BMvqomyjfOjwkUl07v2hAq4-Vh_i8mjYgtxGEWEK7DFsZSBQAycR-cnCtZoEmK87LBGdie8-GFOO97vdZ9chBjXhMYRejm7IKHqUm16vWUv0eMfdF_nU9MDoXooqrsKO7bJFUGhrYGXL6kzhJzoxrqvV9cWANYVlKanFRxkRx569fFf0hdxYREhnnbqCh-dRUVpUPcESEYLEIQR2xNffcy_gn4XhKxU4URJ84mWCIkSzHsmj4IN4JgYacVw84du5HHGQ4t6mbDwvEfdrcgjpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇮🇷
صحبت‌های جالب بانوی هوادار خیبر
: رویای من حضور مانوئل نویر در خیبر است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 529 · <a href="https://t.me/Futball180TV/108680" target="_blank">📅 16:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108679">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50fbec86e.mp4?token=gIKczPKuvuctnerP57Svu9gZg5kHwxiFV6YHYINoGmojtZ_cfhFSHaQiimLR0qTxdJ_VzArw4V4Esuu94-mkMci8bIysQoNILAhhjsVwoPe6KaLAUCQzPIW8zzN4TfURksZSPD94GAVGnXs1uWg3GlT4PJa6wUvKvyrP5z_oZEP94fJTAxmhmHi0mh3TutueTBOPcZwupmDKNicOEICPfBAbM01mB_ohQxTCa46qTSm_P5wTPMc_DTvzXUrkgNIQSUkLZmTVAxS8pYuy_vC3SJguWsjiWwuaWjYJvQSkvV9IexOs4Kwg26fzGDWPHC5dUFLIzi_XTVNOluy1WxxxtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50fbec86e.mp4?token=gIKczPKuvuctnerP57Svu9gZg5kHwxiFV6YHYINoGmojtZ_cfhFSHaQiimLR0qTxdJ_VzArw4V4Esuu94-mkMci8bIysQoNILAhhjsVwoPe6KaLAUCQzPIW8zzN4TfURksZSPD94GAVGnXs1uWg3GlT4PJa6wUvKvyrP5z_oZEP94fJTAxmhmHi0mh3TutueTBOPcZwupmDKNicOEICPfBAbM01mB_ohQxTCa46qTSm_P5wTPMc_DTvzXUrkgNIQSUkLZmTVAxS8pYuy_vC3SJguWsjiWwuaWjYJvQSkvV9IexOs4Kwg26fzGDWPHC5dUFLIzi_XTVNOluy1WxxxtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیری آنری: چرا اون رابونا رو زدی؟⁣
یامال: اونجوری قشنگ‌تر بود.⁣
تیری آنری: سه‌گانه ممکنه؟⁣
یامال: همیشه ممکنه، ما بارساییم و به نظر من، بهترین تیم دنیا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/108679" target="_blank">📅 16:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108678">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/Futball180TV/108678" target="_blank">📅 16:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108677">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hFLOMrq6PhvvtxN_3ko9fjUSQQyEo7i_FpuKn7t0NW-v_AJn7D0f-Pi3pT9Jo2Yxvn3U7C7iDbgqFaJHwHkxcfpd0UJcz9q_cP3OmXsSS8ADVoYcj-LTiRcBFmxPp_G8zanSaU4YMMhRpCZawuM6Umzz0th79iUxh7bfX86XhEezZioCwChNi84n5J0rOc0ppl5Nhtu8PeAjATH5iHUoMJcbq4221G4SdUeHiz2nnve2js4cYRupi2c1i14_k8FOMJABcVaPH6dZnl4KIPihM0R4_iwZpwhylLVwyau-gPUoWCUkP6tM7R8m3GUcrO6De8BtdZ-rJ6GPWSuWwANbdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/Futball180TV/108677" target="_blank">📅 16:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108676">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a2dc84c7.mp4?token=aVQHUebJTDya8Ls3YqKiOxwOODmqBzSWalPoFg7iNS9XKM_JqmLLBeXp1llryQ2SICTi89kp2jGq8EqOwMJvulJj4GttaUpe-2OH8G735HQUrAf7tJ_wsV-4Am1KjDpLL7vqqZHhvSJmDX0te6K4ueBkGCVjL2_s9vS1I60mKRxTkOlx_TBccRqmLspOGPmnqf2L5IT6X3FH4RWnAAjm4LAX201uPmGC1sTdWBlJjKRMsxvtUtIK0DIeElR-iozhtzoJyRoG0RZ5UHU5y9AtJScVJ9OXuj4F5DdGMQPaGUroRktaKqtqL41udDVRExYDg7n0iamQmZl9EbA24of8uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a2dc84c7.mp4?token=aVQHUebJTDya8Ls3YqKiOxwOODmqBzSWalPoFg7iNS9XKM_JqmLLBeXp1llryQ2SICTi89kp2jGq8EqOwMJvulJj4GttaUpe-2OH8G735HQUrAf7tJ_wsV-4Am1KjDpLL7vqqZHhvSJmDX0te6K4ueBkGCVjL2_s9vS1I60mKRxTkOlx_TBccRqmLspOGPmnqf2L5IT6X3FH4RWnAAjm4LAX201uPmGC1sTdWBlJjKRMsxvtUtIK0DIeElR-iozhtzoJyRoG0RZ5UHU5y9AtJScVJ9OXuj4F5DdGMQPaGUroRktaKqtqL41udDVRExYDg7n0iamQmZl9EbA24of8uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
هوادار بارسلونا دیشب در استادیوم گالا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/Futball180TV/108676" target="_blank">📅 16:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108675">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOR-YTVJy9apBIq9r9sQ9iNLmOlR1MWQFjkv_kPeRppksZWyfHAWfuT43une56IP4tXdDL4N3-SAGFk0F9AH90ojodtRqOZIcDO80PqT4aIVQmFpQNoSg0jGqb3-LwWfvwxTG125R4QXUXcPaqFx1KXJvIkIRpCa4gJnzDao1Yt-EfhD3oFrZOUmWit3LNIkCPrZKo9KSQ_9acpq7xWO8emR0bAmjWpBli2xHKJZZob87dRjOLFp7_CuOZ2KxCdSmM9Dk17S3zCOsunlJ0eOlosotcbQTCLOkKUzv7ZzLiVTs1lRnJANS_y4gDdmQezcu8JOYgZX5LXkGaqLuIDDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
ترکیب پرسپولیس مقابل خیبر خرم‌آباد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/Futball180TV/108675" target="_blank">📅 16:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108674">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1611c80de0.mp4?token=VaYePdAGmRsrTa7cG7b4WHH4oYx2RsTQhun6FRUD9rByWou7OWASg3-DLpX8h8QVkhXUDdv9vbXz1zyIS9CC2Pe9CpXjT7qnc1BblGLA4a3UmZb3VhPFzETiAIVzo7PH2qeeMDqb8v1upc8sNi3GdObfoc41YFWf-m2WEUXvgDAR9iCRIKRy2xVjfRqf9tXIT9meISw70HdKdSgFcc58mAQ1PggAVO5aDTRieaJBfI6qjJuRWsbIM-wr1temPRMOv1i5rZkS7_qiXyVvwPpW8f1P18_LHn0q_WaSvgWsfYk_yhxTClz8cWW6DvSBHJ1fvtNSfSINWwpUZ135qMnSyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1611c80de0.mp4?token=VaYePdAGmRsrTa7cG7b4WHH4oYx2RsTQhun6FRUD9rByWou7OWASg3-DLpX8h8QVkhXUDdv9vbXz1zyIS9CC2Pe9CpXjT7qnc1BblGLA4a3UmZb3VhPFzETiAIVzo7PH2qeeMDqb8v1upc8sNi3GdObfoc41YFWf-m2WEUXvgDAR9iCRIKRy2xVjfRqf9tXIT9meISw70HdKdSgFcc58mAQ1PggAVO5aDTRieaJBfI6qjJuRWsbIM-wr1temPRMOv1i5rZkS7_qiXyVvwPpW8f1P18_LHn0q_WaSvgWsfYk_yhxTClz8cWW6DvSBHJ1fvtNSfSINWwpUZ135qMnSyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
کنایه‌جالب ژوله به درگیری دبیر و فوتبالی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/108674" target="_blank">📅 15:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108673">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/995cae6ace.mp4?token=VIYVjoDCLslK5EhJksBCW9cJpyzXLxT5XEtlA7t9aXI5MtpQ0N4FI_a_Opn601feZR0Z_m1XA11B3WcTajdBdbTIZUfWHX64V2M9r7m_MfJQOmue95m5PbxIX3dzo1n-YtP1qXpcJnEAMvNbSnZsBZVS857XmCIKyVJ81FYd0SLabj1kM8qD58YC-9xMK9hFso9GoMh6g_eZnIDB7pEk3_pVT_6t6ZEpnnd6ReaoQDYRXlN1CQhfizdeUAC3P-pj9Qi0BKDFDEQrDTS26teRl4EJtWvBNM_T0zgr_oUdxmQwwryKrxiY8P9gT3IiMGgMu3mhh4-ob5tGlMiYMQxv1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/995cae6ace.mp4?token=VIYVjoDCLslK5EhJksBCW9cJpyzXLxT5XEtlA7t9aXI5MtpQ0N4FI_a_Opn601feZR0Z_m1XA11B3WcTajdBdbTIZUfWHX64V2M9r7m_MfJQOmue95m5PbxIX3dzo1n-YtP1qXpcJnEAMvNbSnZsBZVS857XmCIKyVJ81FYd0SLabj1kM8qD58YC-9xMK9hFso9GoMh6g_eZnIDB7pEk3_pVT_6t6ZEpnnd6ReaoQDYRXlN1CQhfizdeUAC3P-pj9Qi0BKDFDEQrDTS26teRl4EJtWvBNM_T0zgr_oUdxmQwwryKrxiY8P9gT3IiMGgMu3mhh4-ob5tGlMiYMQxv1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🔴
هوادار خیبر: اینجا اصلا پرسپولیسی نداریم؛ بیرانوند بچه سوم را بیاورد و معاف شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/Futball180TV/108673" target="_blank">📅 15:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108672">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2535928121.mp4?token=UI0aRZCuK8Brr2sfbqOJGdY5Z9xesM3jGbBJ43rd157ZZTEBGiPhcFI4rIB_ZmnozU6sG_GXVIAK8IjExxeQdjDt7b9a26vvkBheTE2vpmYAoLwlCugjHwBOvskPqZKtnTxRwAQIGIO49ySNGf-xGEtG_9Ei0q-HozDU8fXKg05osdGB6Qw01OqWVCyMpLaDe76LUs3ZHbbZGn6RIE1XW0FGySnRRqVF6NV-BZP7b1rVgqdXJ4qML3gX6fgRItibRvgq1vLRAcytEbgFFYEA778vqsNUq8IX9Ss5FnFwxMUS8pXSJUp431Vuj-zcWOdP261WDx9B7BkiUkAvBKIkkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2535928121.mp4?token=UI0aRZCuK8Brr2sfbqOJGdY5Z9xesM3jGbBJ43rd157ZZTEBGiPhcFI4rIB_ZmnozU6sG_GXVIAK8IjExxeQdjDt7b9a26vvkBheTE2vpmYAoLwlCugjHwBOvskPqZKtnTxRwAQIGIO49ySNGf-xGEtG_9Ei0q-HozDU8fXKg05osdGB6Qw01OqWVCyMpLaDe76LUs3ZHbbZGn6RIE1XW0FGySnRRqVF6NV-BZP7b1rVgqdXJ4qML3gX6fgRItibRvgq1vLRAcytEbgFFYEA778vqsNUq8IX9Ss5FnFwxMUS8pXSJUp431Vuj-zcWOdP261WDx9B7BkiUkAvBKIkkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
کلا هفته خوبی برای گیس کِش سیوس نبود. ویرجینیا هم ازش جدا شد.
💔
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/Futball180TV/108672" target="_blank">📅 15:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108671">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33db152fe.mp4?token=s6I4vaZ-d4DqC2na2lKYUdptuuKhNWIapAyIYxVpgWbVvRkH7G0tIkvh4uutYEdldyzzU-SeqeLeZAwtl8awYBqwIW0CO4vNmc0IAIia7KqswfSXhrlW94Em0vpeW_3IvdOp8_pIOGv4or2VV6WzD5jhGDB_eo6PepJ0yWFEW6m518FU0cHWY1PfbGt_9pycaBSMAqiN5OJCfrGOpQGuo-urE_p-Z09SvYCqk0q5OnS8-jfXQY3iKM5rLyJF9IF6R48CqqkvFys9Iu1rgMVT3G_1NKrby7cyyeOEqJhso7DZnhYrtCJ2WhphKfKOjZtuJ5KPJHsD1MngmXV57zIHIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33db152fe.mp4?token=s6I4vaZ-d4DqC2na2lKYUdptuuKhNWIapAyIYxVpgWbVvRkH7G0tIkvh4uutYEdldyzzU-SeqeLeZAwtl8awYBqwIW0CO4vNmc0IAIia7KqswfSXhrlW94Em0vpeW_3IvdOp8_pIOGv4or2VV6WzD5jhGDB_eo6PepJ0yWFEW6m518FU0cHWY1PfbGt_9pycaBSMAqiN5OJCfrGOpQGuo-urE_p-Z09SvYCqk0q5OnS8-jfXQY3iKM5rLyJF9IF6R48CqqkvFys9Iu1rgMVT3G_1NKrby7cyyeOEqJhso7DZnhYrtCJ2WhphKfKOjZtuJ5KPJHsD1MngmXV57zIHIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥶
حجم‌صدایی که دیشب در ورزشگاه گالاتاسرای از سوی هواداران تولید میشد، معادل شنیده شدن صدای اره‌برقی یا هلیکوپتر از نزدیکه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/Futball180TV/108671" target="_blank">📅 14:50 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108670">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9VPwlHHscs8zGXJs7iaOHSaUdUJ3v3CtOGLJKC-LDLyV-_p_jGu54nWbE5X2uBSazj5Pez65bZ3N67Zrsztl-87O6ozIN0aohTJGXv6uPMrB9x9LHWMdn2ZGdan0eCGWzQT8zcgFgF9wneBGhsAuVNmlB-vPpEre-76j0aGcvUH70r_F3yKAzITw770x8FY-GdY0a1fjtQnglIcjmaAlCt6qNaXw1Tghgabgjx4xRK3DgLYCfYxhJV-CyFVRBTaI066s1doIzwOIjgAOqfHcIyKaluO9eW0fxP_SiHAli01B4TaeZe4w7BI-CMXCEa28FpodaVlM7LlQUSKBNXUHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول لیگ‌نخبگان آسیا پس از پایان هفته‌دوم
🗓
برنامه هفته‌سوم نمایندگان ایران:
🇮🇷
استقلال - شباب‌الاهلی
🇦🇪
در امارات
🇦🇪
العین - تراکتور
🇮🇷
در امارات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/Futball180TV/108670" target="_blank">📅 14:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108669">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8eb9d1b0.mp4?token=WdLBwYYfdl_-CD7ywENS8eWJiu4qSBAR1JmkcvFlPpO9OB_fzAwpY1qyIWe7ko-K3xgWL6Z6mjh4IrbItbU6bKVJijkk3TtxtKgw1IZUA_1bafw0eCJEpAbdCXfpcs8BNQXdLxe3eycUZIQW-mzHmaY1hkGJVPHA3NA22BaDtxTnykNgAtFd1je4Ag14BS2YhisZWfNJ38AzhTo_wHlNAQUyeWh56P4sSMCp1JYvEGfXyZrIIW-ynPhf2aFAOCbEGWVGJ-4BAeFIBSbKRkp1IU6Qlr9wey8PEAOAQzY3wXKAW6Bkfu5f3ffh5os09foozpi7TRecUXPema_A0DtJjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8eb9d1b0.mp4?token=WdLBwYYfdl_-CD7ywENS8eWJiu4qSBAR1JmkcvFlPpO9OB_fzAwpY1qyIWe7ko-K3xgWL6Z6mjh4IrbItbU6bKVJijkk3TtxtKgw1IZUA_1bafw0eCJEpAbdCXfpcs8BNQXdLxe3eycUZIQW-mzHmaY1hkGJVPHA3NA22BaDtxTnykNgAtFd1je4Ag14BS2YhisZWfNJ38AzhTo_wHlNAQUyeWh56P4sSMCp1JYvEGfXyZrIIW-ynPhf2aFAOCbEGWVGJ-4BAeFIBSbKRkp1IU6Qlr9wey8PEAOAQzY3wXKAW6Bkfu5f3ffh5os09foozpi7TRecUXPema_A0DtJjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇹🇷
گالاتاسرای 1-4 بارسلونا!
بارسای ترسناکِ فلیک به هیچ تیمی رحم نمی کنه!
☠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/Futball180TV/108669" target="_blank">📅 14:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108668">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uY80S_aCYgkzu3_-MBl_zPCfvfY4VFdBjLjFmzmFuuD7enULAYllkn2JMeOVEDU6LKda8fb_46J6x1Bz7jmGN16N_7JzTLYQ6FIA17m-V9fyzVlYBDb1tIucXEmF3hP-aBCWgMh4XYaH0laP2_lUDZtbGEprvwa-UG5AtW6rzvkDqEV28LM6dJrQX6uYvX6RTivK-XkDGhczHiVO1duJ77u7aSQWNXGN30kBOLsBGijYWy-wYaKcNqTtAwVKCeoEpsKmTesjDHLTOQdkeZOmCf5u1_Tf5zTZHt26uNXtRlQN9L7BWfxW82esDDxKmm0ULNrvHumh0XqPTTfj39Lhug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
✔️
با توجه به برتری استقلال مقابل تیم های قطری در دو بازی قبلی، امتیاز ایران از فوتبال قطر بیشتر شده تا شانس برای حفظ سهمیه‌های فصول آتی در آسیا بیشتر شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/108668" target="_blank">📅 13:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108667">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/805c98c083.mp4?token=qr64Ce01NZVeTHoK3rqCsENeepfxALu-y3GFy5iNRBmPUC-Jbm4m8W9kW4CgH6Y0_M2A2dCQqWkEH9ZfNRevzHxcQtucgA-BfMe-m11L2x7nCrd3u9Gg5w3xVJP-zEjXAAP83fPsBU1SNlB_8X0uAlsSoRwdmEq1k7g00IqDsB956RtRj6Rq7yAS-Jset7_klkdW-EuTIKngG3TScxN6mh4qU4pzJB1CpB_76i8gTVPqv0IG9zkypNBREogzkzUTmMCaSJMLWIs5bci8B2FUb-gc3lZKA_w7cW1ncPZbPXTfkc1JmwgexP9HWW0ma0UxNR8KVI5RzapNGUxAOiJ_ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/805c98c083.mp4?token=qr64Ce01NZVeTHoK3rqCsENeepfxALu-y3GFy5iNRBmPUC-Jbm4m8W9kW4CgH6Y0_M2A2dCQqWkEH9ZfNRevzHxcQtucgA-BfMe-m11L2x7nCrd3u9Gg5w3xVJP-zEjXAAP83fPsBU1SNlB_8X0uAlsSoRwdmEq1k7g00IqDsB956RtRj6Rq7yAS-Jset7_klkdW-EuTIKngG3TScxN6mh4qU4pzJB1CpB_76i8gTVPqv0IG9zkypNBREogzkzUTmMCaSJMLWIs5bci8B2FUb-gc3lZKA_w7cW1ncPZbPXTfkc1JmwgexP9HWW0ma0UxNR8KVI5RzapNGUxAOiJ_ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
صحبت‌های جنجالی پیروز قربانی خطاب به فجرسپاسی پس از شکست دیروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/108667" target="_blank">📅 13:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108666">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37d4792646.mp4?token=VzXi_WrhYJ_Few0r_-xv06-dUoYTrNCls0eX9CAybvhXwL2vaDUfJUHZG-cuGnSHnYz53FDEWiI0w0gr0jsf4crwdyoPQYWcPcBfKEmYSTRsi5xUhA_JQTdsrJmoY2qJhjeAAEegvJSOh8uHz7Zd03y3BBE5qKrx0cQLdVQw_8R0FxWK2ZTYx6QX6tWHk8iYqblwXPOu01kWC8nz5BfjRI7aSxdCl-YezcfFzxdDgEravF_wQHOZNvybGl-u2_CMD5tF7ZsF1BkxSiit7uhbrPB1mLCVAIXP-tCoo04OYJ3ZCb8FF3oxsr2SjU7mr8ZZRgvBjHT8HJraO3eqsdym6g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37d4792646.mp4?token=VzXi_WrhYJ_Few0r_-xv06-dUoYTrNCls0eX9CAybvhXwL2vaDUfJUHZG-cuGnSHnYz53FDEWiI0w0gr0jsf4crwdyoPQYWcPcBfKEmYSTRsi5xUhA_JQTdsrJmoY2qJhjeAAEegvJSOh8uHz7Zd03y3BBE5qKrx0cQLdVQw_8R0FxWK2ZTYx6QX6tWHk8iYqblwXPOu01kWC8nz5BfjRI7aSxdCl-YezcfFzxdDgEravF_wQHOZNvybGl-u2_CMD5tF7ZsF1BkxSiit7uhbrPB1mLCVAIXP-tCoo04OYJ3ZCb8FF3oxsr2SjU7mr8ZZRgvBjHT8HJraO3eqsdym6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
این کلیپ شاهکار از کنسرت چند تا پسر توی خوابگاه دانشجویی، فقط توی چند ساعت میلیونی بازدید خورده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/108666" target="_blank">📅 13:19 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108665">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a20b75a47.mp4?token=cy5Eovj3IlmFCKD19Ot3iChz9XmXHJ9ygreckOHTVpnJNH-sl0Fu6awM7_CE1hSLHTv8xSZrQKQ0uIAAZX-MCJJFw9tOas5fUQK_JkOH9RU3sRJItEQJwrlz6iU_9qcAj3M4dmXrlVjdixRnXp4wAmaTg8YlaFmsFokYZtxsEIihIosAKVkdMyykn9QR0Psd2nqmsqvxxaG4wXajA87UIll2Md6di7ShFp4NbBGWi7ibCCO7FIPUWsG4y2svz5sGLdE7saR50SWxXfHvKSz73JuQhl7m4OsKTmS--1D8lbM5C1aXPJI8obI4DmvCYEHjJo02qFCGNc8qyhqevWfwNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a20b75a47.mp4?token=cy5Eovj3IlmFCKD19Ot3iChz9XmXHJ9ygreckOHTVpnJNH-sl0Fu6awM7_CE1hSLHTv8xSZrQKQ0uIAAZX-MCJJFw9tOas5fUQK_JkOH9RU3sRJItEQJwrlz6iU_9qcAj3M4dmXrlVjdixRnXp4wAmaTg8YlaFmsFokYZtxsEIihIosAKVkdMyykn9QR0Psd2nqmsqvxxaG4wXajA87UIll2Md6di7ShFp4NbBGWi7ibCCO7FIPUWsG4y2svz5sGLdE7saR50SWxXfHvKSz73JuQhl7m4OsKTmS--1D8lbM5C1aXPJI8obI4DmvCYEHjJo02qFCGNc8qyhqevWfwNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
💥
حرکت زیبا و دیدنی دیشب لامین‌یامال قبل از شروع بازی مقابل گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/108665" target="_blank">📅 13:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108664">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raxnv-HOCLq5XSvGfDPVo7rgGnkPkzmcQLwKH9fuodsClf9pXvpmOuap_uIfvr8nqczV4K5cL71b3braPWRDDZNK7-knxJFRNCFMrEuFjSAA_fxdb_1566GWLg2Iu8LUZkwpqCalQX24oXvBzWY23fCXB-6WgFQY7K1aedQUsov403Btp5JWZwFyB9MMsyb5XE1VgUmZx53fV8ptMqq5UekDUuFMxNWapqwtZG0PLfa2U1-Pp5D9J-w5kEVIKH3cq77fZVj3ud1IlpBHMxcCUy9L1tEmuAOM8c1eW458ntEaisEJLI8GIeSuU0TXGtNgQBw_JLGFx_X-rrCe6ZeMSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⁉️
🇪🇸
کدام تیم‌ها در لیگ اسپانیا بیشترین گل‌هایی را که به دلیل استفاده از سیستم VAR باطل شده است، داشته‌اند؟
🤔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/108664" target="_blank">📅 12:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108663">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e1b2f756.mp4?token=DyP4DoW4_UlUsk-E70jQT3t0uuqMWN8-sCDo_BBYtoNBs04x5MhdzFFkRhQA12PDG-syZ7mElPR0bXOtC8jqKH-jqMm_dsMu43Zp-R1elPODCbsgmH2_ZKtRXxEXFbBvCr6SSEEGSMArsY-Tuq6DzDwv_eTC5AZBwfOy3UiwNux-HSM8xxUzcp8T_2b_1SO5JQBXLQmyBmkg6-eLKdJqwgC_DZb7eKSpumqKbLnHMl1b3uh93ESSKQIBxK899wtKeRbsXqgKfrMDH2rsMN99yzuYwJwsl4dz7qrVcu7XRVnujfagOXBP8Pl6Y6ZP4WbCjYeyNZFWCenDQT5d-dKVGWXUv9qPR3rkeWkA_TstzwGqhYfg3Jv4itEuzfqLGVkMYgBOGFEd-u8VjNpEt5CslSbV7OGbQCDf09C2prAEiuFPMrKsDJrOBaBtKh_itqP0WvNEcgzq9zYMrwoAyAMm-ziqIKzM5pJ_kOqJGE9ttvYj5EFiasjIlehKW-ORDBq0wwRncU0H5PYQWoynM5gOpg_7XF68YIwg2Sx4ZJrlwwWs2WJ1uvbsvMo2CtKZ6aFD9nwOaXRUurrFy5bZ48ANVHnJYpxyiLBwGn-g2DoGKUNQCoK9Q_LlRDONq1OYzVnNbSKgbLC81b99QIbz_-mLBcSDPcmeJB_kBY2yLoj7I6k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e1b2f756.mp4?token=DyP4DoW4_UlUsk-E70jQT3t0uuqMWN8-sCDo_BBYtoNBs04x5MhdzFFkRhQA12PDG-syZ7mElPR0bXOtC8jqKH-jqMm_dsMu43Zp-R1elPODCbsgmH2_ZKtRXxEXFbBvCr6SSEEGSMArsY-Tuq6DzDwv_eTC5AZBwfOy3UiwNux-HSM8xxUzcp8T_2b_1SO5JQBXLQmyBmkg6-eLKdJqwgC_DZb7eKSpumqKbLnHMl1b3uh93ESSKQIBxK899wtKeRbsXqgKfrMDH2rsMN99yzuYwJwsl4dz7qrVcu7XRVnujfagOXBP8Pl6Y6ZP4WbCjYeyNZFWCenDQT5d-dKVGWXUv9qPR3rkeWkA_TstzwGqhYfg3Jv4itEuzfqLGVkMYgBOGFEd-u8VjNpEt5CslSbV7OGbQCDf09C2prAEiuFPMrKsDJrOBaBtKh_itqP0WvNEcgzq9zYMrwoAyAMm-ziqIKzM5pJ_kOqJGE9ttvYj5EFiasjIlehKW-ORDBq0wwRncU0H5PYQWoynM5gOpg_7XF68YIwg2Sx4ZJrlwwWs2WJ1uvbsvMo2CtKZ6aFD9nwOaXRUurrFy5bZ48ANVHnJYpxyiLBwGn-g2DoGKUNQCoK9Q_LlRDONq1OYzVnNbSKgbLC81b99QIbz_-mLBcSDPcmeJB_kBY2yLoj7I6k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
صحبت‌های جنجالی قلعه‌نویی علیه فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/108663" target="_blank">📅 12:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108662">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiST7Xo67ImuVs3KhJXbnoNhjurDUKNiiiKT7gzQS8sWaHV0w7ta9gdLV89Nl6flFYSJo_o1dB3Az-KpJBwqfhy9W4BecB7nlVqmUOybCrYgYkyQDeosx_7_HBWYdpBPqK2dO3Wz7_g_NRC1tHNlmSpUtUSEz1GmGieaW8CBPU7_6NJqEPf9ohNTZqA4NryOFhA-6oqhoqpxpFwGuUrw9qXBJoWRmI4-PQqW52KPtFIo287wsyFg3LI8uToGqo3cPNBPZnvLhEmOLYlWrH1cJERNFwJxWQjYJnHQmfKLhRzUU5TQg9aLVWnEJlZMJUKJMqK17c4uSP_9jHxrEmXdRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیجان فوتبال رو با لیگ ایرانسل چند برابر کن و با پیش‌بینی نتایج، امتیازت رو ببر بالا!
✨
🎁
هرچی پیش‌بینیت دقیق‌تر باشه، شانست برای بردن جوایز جذاب مثل موتور، اسکوتر، پلی‌استیشن ۵ و... بیشتر میشه.
همین الان به سوپراپلیکیشن ایرانسل‌من سر بزن و اولین پیش‌بینیت رو ثبت کن:
ثبت پیش‌بینی (هایپرلینک شود)</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/108662" target="_blank">📅 12:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108661">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be51a8784d.mp4?token=YBUOUYhvHfN2Urnd4vpogAUekkji5ew7baKb15HMfytakiaZ7niMvz-qjauWE4RnIeUQeVUuNnBo0iZ2mHJOAzY5gvb_mWWmDcFKhK_l0ygSNf2jR6m10ejnAfgtQlcS6TQZsh_bXN99MGgMJmvClUEM5hhJuqlu8n-leFbFQn-kKQGio908N27rPBmr_RcQNiyropGbJyjYnd4aaXib2ENnpetEcwVfL2cxj4UIFk6pggdB-EoLNwO64Le2Dit5BLM_8wV88I1nXUPKqYOHBenqDqC5Th6pgWMnL5xNp9Dzqmc8yx9z6gxZVYAvE-752R1EZjldTNfTCIAxnHSf8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be51a8784d.mp4?token=YBUOUYhvHfN2Urnd4vpogAUekkji5ew7baKb15HMfytakiaZ7niMvz-qjauWE4RnIeUQeVUuNnBo0iZ2mHJOAzY5gvb_mWWmDcFKhK_l0ygSNf2jR6m10ejnAfgtQlcS6TQZsh_bXN99MGgMJmvClUEM5hhJuqlu8n-leFbFQn-kKQGio908N27rPBmr_RcQNiyropGbJyjYnd4aaXib2ENnpetEcwVfL2cxj4UIFk6pggdB-EoLNwO64Le2Dit5BLM_8wV88I1nXUPKqYOHBenqDqC5Th6pgWMnL5xNp9Dzqmc8yx9z6gxZVYAvE-752R1EZjldTNfTCIAxnHSf8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب یامال جایزش رو به دوس‌دخترش هدیه داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/108661" target="_blank">📅 11:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108660">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c48214e32.mp4?token=ZLOtZPDGe0eD1Qsk5g9HW8AUjw-HLtE2b05P-9X0MQTKXCyz15DDGCQfpvQXQzLC2y_LNnNvj3uXKZY6Ucfv23dg6tiCtV_x9CtQzAWuwLDvdDG0km75_orxSobSyH0B_NIWO8-QrOVoMtirVIMNKsceLl7JNgaJ80v_RU7Yfg1HlGF0FDHqYRylYiUirAUOyrCFh1XlBtmecuT3ng0llDwsEEaUAIuXUEnGzO6UAcDhJfZPKZPborEGY07PWirQebs837Z55PRn86QKzayfJI8OIlntd7wF0l-XxAFgtGDe4axHTg0NFYVJl-sbHeZw1-r-1xtfpp2Dhg30ioXMAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c48214e32.mp4?token=ZLOtZPDGe0eD1Qsk5g9HW8AUjw-HLtE2b05P-9X0MQTKXCyz15DDGCQfpvQXQzLC2y_LNnNvj3uXKZY6Ucfv23dg6tiCtV_x9CtQzAWuwLDvdDG0km75_orxSobSyH0B_NIWO8-QrOVoMtirVIMNKsceLl7JNgaJ80v_RU7Yfg1HlGF0FDHqYRylYiUirAUOyrCFh1XlBtmecuT3ng0llDwsEEaUAIuXUEnGzO6UAcDhJfZPKZPborEGY07PWirQebs837Z55PRn86QKzayfJI8OIlntd7wF0l-XxAFgtGDe4axHTg0NFYVJl-sbHeZw1-r-1xtfpp2Dhg30ioXMAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داره یه صدایی میاد
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/108660" target="_blank">📅 11:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108659">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108659" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/108659" target="_blank">📅 11:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108658">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ccp0VLEPR-KqRA7gLZHVWRYUXFSGGg-1mJgofAJ9NvF3S9EqQggxkk6SjehSogEa-KWIJtrNJBz4QPjUw6s7LnsC621HeynjRUkX1j734wPYrTzmSKgoTVTY3gMCvkSzjGyPw1Q2U_vOPDzHWFKNytO9NLHTndNvIyF5cq7sNS_eaCjOMXy2zQjkbUU2Pae3Qyhge5ZJsOiIODud1vhbS68wc-iSCCO3xpAdLiMMb9AEyv_kgVB6O9bJreoL_BD0LdfRRRLZvuYOT73r8gIj03s2jGjsG9KWNYTcD8oNllcR4veqtIlBkGyxNSChAKVfYWaFdDpkI6oKmMKF9p69Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
لیورپول
🆚
لاسک
فنرباغچه
🆚
استون ویلا
دورتموند
🆚
بودو/گلیمت
پاریسن‌ژرمن
🆚
منچستر سیتی
پورتو
🆚
رئال بتیس
رئال مادرید
🆚
رم
پرسپولیس
🆚
خیبر
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت، ووچر، کریپتوکارنسی
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/108658" target="_blank">📅 11:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108657">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bfab0b19.mp4?token=vBN5EDfZjWyYkrkt5hM0gSa_PvZMDSVrm9vO0r1lFzI7_ho9omCfQTjWJTfvM7EgUfXqaxWGeNnLRDfE6ArfAjSFUAZ70lqRHFiNlXwKClZdzwJBiUydWradhu0FXMGykxCeILg3wt1KwfuhSXOs7SMjLSCLqbRDHMKt9ZTu6s3yByOexRTsJ_pPHqLZW4JifOhGULHiAYInHl4venY7p2D42wOvqMs7KAIVKu5M0FK2Olq4ee_DB-TZ-Z6hANtDyzWvAQJHOX7cPB_-Z8IS8tBPxLW_BBww9gtVzmsfBSjurGpDQzw9dHdgiH0qbXpsXMEDjodXqsQIJU_pbzkXnU5uTUeLe12Fn3fz5Hy8yqoSDlz71cmSCgjIdmejnyTYm_j98F5aBW5jx7hyMJHq1hkMKd4CGjVgN96aaWHH18XfwXxUUw3otrm-QyUnmlojCRi-Mlom2xOnsEOlhPpORbb-V3wA-jjgq73ynC4Q6NpKvq-zCjEJZcMw6n6tkRg2hj8i7rG41HOh3rzP2QYGTu1GW1OQJKzwujUrVWYWbMvN_rBNOvRu3FVaj6xS5UeEVPm9tT8sD68oq85dx-VBhCp9ojZXzv3ifjEnLS93YxRgOw6PbayxHfBj2RESnoHmzjr71cfRGWafQCqObPETshkLK3yCjLskbwM9yo-gtVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bfab0b19.mp4?token=vBN5EDfZjWyYkrkt5hM0gSa_PvZMDSVrm9vO0r1lFzI7_ho9omCfQTjWJTfvM7EgUfXqaxWGeNnLRDfE6ArfAjSFUAZ70lqRHFiNlXwKClZdzwJBiUydWradhu0FXMGykxCeILg3wt1KwfuhSXOs7SMjLSCLqbRDHMKt9ZTu6s3yByOexRTsJ_pPHqLZW4JifOhGULHiAYInHl4venY7p2D42wOvqMs7KAIVKu5M0FK2Olq4ee_DB-TZ-Z6hANtDyzWvAQJHOX7cPB_-Z8IS8tBPxLW_BBww9gtVzmsfBSjurGpDQzw9dHdgiH0qbXpsXMEDjodXqsQIJU_pbzkXnU5uTUeLe12Fn3fz5Hy8yqoSDlz71cmSCgjIdmejnyTYm_j98F5aBW5jx7hyMJHq1hkMKd4CGjVgN96aaWHH18XfwXxUUw3otrm-QyUnmlojCRi-Mlom2xOnsEOlhPpORbb-V3wA-jjgq73ynC4Q6NpKvq-zCjEJZcMw6n6tkRg2hj8i7rG41HOh3rzP2QYGTu1GW1OQJKzwujUrVWYWbMvN_rBNOvRu3FVaj6xS5UeEVPm9tT8sD68oq85dx-VBhCp9ojZXzv3ifjEnLS93YxRgOw6PbayxHfBj2RESnoHmzjr71cfRGWafQCqObPETshkLK3yCjLskbwM9yo-gtVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
با داغ شدن دوباره بحث تخلفات منچسترسیتی پس از برد قاطع این تیم مقابل لیورپول، مروری داشته باشیم بر دیدگاه یورگن کلوپ درباره این پرونده؛ پرونده‌ای که لیورپول و دیگر رقبای سیتی از ذی‌نفعان اصلی اون به شمار میرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/108657" target="_blank">📅 11:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108656">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbwvOiPXXvkTEkZEYnGmZfxzAJHl1VKtoXFRayKIY-b4749xaSGEGscpWsKAHnIj9jip0j2kNVrT_TRamK-8FiEmiKatWelxD_zS5RvsPdYK8UI2DPRFFZjnvs5yFM05FTaaOsfL58H18TOZhjKofOcISmHORa0H2DCqFuoiZOeS2gRNz87ZxDc29UHBwyGKE-VCC-0ZB0v1p8LIpV-BrjwtmFyKAQxmcmyzfTl7pQHi8VXh31pRI6VezuDt2MwCOIGIDHhQD4SabJVxhEDsz3H0JP2UqtnA9VJzP2qs0uwqaTxQAVji9RlWE1idXnGs5YljoWs3NVnQXy7sEMizjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
براساس آزمایشات اولیسه، رزاقی‌نیا هافبک استقلال بدلیل مصدومیت حدود سه هفته از میادین دور خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/108656" target="_blank">📅 10:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108655">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9746e98953.mp4?token=CmsXpyEIHkJY5z0ChrKKvoHcUE6lpeHASeI48KMGdHawOsrQYZ6YxsLvfX2E2pCGYPqkhKllp-RO-L9Br8eWPPOdizc9x9Zf79lW-WyZ-utLquW600x8fxS-ZX_OveQnAg5hVDPW2gBoqM48mwb-mIUgazKiJq6-lmJIIR9YC0WErUVs_FUiLnaLqYqCHBSKPWKXPcE864QCUODjgaEFtr6GIERQEK_D744sWjT9RMmwniikHcT_TLPguxZYDT8WgT4o8oJd5EyI-jQ5RlGoYbOHAyk5dqtvD9qEpGR4Ul4rj3qg_8X0HbbUIcnWWKPYsRA0ArEkeaHu9Zy10Z5YGznHQGCwMOZxHsejTLHCHX0iVKpOkIZvZoevSgeCXrqL3Vapq20luXlFx_ESaqgwJ3hEw2J394-ptxBZmuurWktor4aCzQ4yzJ7gb8Es13MX0L9ExYgfx3XCGBLHDV9kyZF9zxH51ytRWZnUhJMVhQUxYlOU7VFkZskJ-rqoeBr0H1We9AANTzQk3WaOekm1uhbOsU5HK5q3ApnDihEV1rjML4zzuZ2j57cuN_CE6pil5iUHux-yIkgdqw70Sq5lF_kqEsLmcsf7oXQ6ayyGfIF6DfUrmEeCMDnDSXoDqOz1Cp19P1eZOXs1KEabnW8pkeGe-XDtlSpdsffhJ8DkNjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9746e98953.mp4?token=CmsXpyEIHkJY5z0ChrKKvoHcUE6lpeHASeI48KMGdHawOsrQYZ6YxsLvfX2E2pCGYPqkhKllp-RO-L9Br8eWPPOdizc9x9Zf79lW-WyZ-utLquW600x8fxS-ZX_OveQnAg5hVDPW2gBoqM48mwb-mIUgazKiJq6-lmJIIR9YC0WErUVs_FUiLnaLqYqCHBSKPWKXPcE864QCUODjgaEFtr6GIERQEK_D744sWjT9RMmwniikHcT_TLPguxZYDT8WgT4o8oJd5EyI-jQ5RlGoYbOHAyk5dqtvD9qEpGR4Ul4rj3qg_8X0HbbUIcnWWKPYsRA0ArEkeaHu9Zy10Z5YGznHQGCwMOZxHsejTLHCHX0iVKpOkIZvZoevSgeCXrqL3Vapq20luXlFx_ESaqgwJ3hEw2J394-ptxBZmuurWktor4aCzQ4yzJ7gb8Es13MX0L9ExYgfx3XCGBLHDV9kyZF9zxH51ytRWZnUhJMVhQUxYlOU7VFkZskJ-rqoeBr0H1We9AANTzQk3WaOekm1uhbOsU5HK5q3ApnDihEV1rjML4zzuZ2j57cuN_CE6pil5iUHux-yIkgdqw70Sq5lF_kqEsLmcsf7oXQ6ayyGfIF6DfUrmEeCMDnDSXoDqOz1Cp19P1eZOXs1KEabnW8pkeGe-XDtlSpdsffhJ8DkNjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
رویانیان مدیرعامل سابق پرسپولیس و رییس پلیس سابق ایران: راه حجاب، گشت ارشاد و برخورد فیزیکی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/108655" target="_blank">📅 10:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108654">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0060865794.mp4?token=oib_dkmp6cU0wenbgIKAKEd_U24qTW3-ZQbpL2x643gtI0kSlNq0WdwPCI77AAZ70J6iypjmjwR7UoLcrW5ydlGwpwZHbbhwvWPuC8bNyMPsC2Q4iaYiRcMe6WplTGP2Kul_jhhrSHUyxUJ1OPoOGj2B0Kpq0qCu-M-hPu4QPLxQgr2L5ccNMwFf6wen9Q7j4DKSn1k6vvdLE_VFNlvuCRUqD2oMq-CYqlw5cS0pUDgg40dVOZWGOQ6COPzWR3AQroN4hr_9EPWWbwSDSjWJZfVJxtkkkBNjcV-LvonFp8SALzoBuEg5QOnsLxd14CNhIcMU6LJw9MTufb5dJALfUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0060865794.mp4?token=oib_dkmp6cU0wenbgIKAKEd_U24qTW3-ZQbpL2x643gtI0kSlNq0WdwPCI77AAZ70J6iypjmjwR7UoLcrW5ydlGwpwZHbbhwvWPuC8bNyMPsC2Q4iaYiRcMe6WplTGP2Kul_jhhrSHUyxUJ1OPoOGj2B0Kpq0qCu-M-hPu4QPLxQgr2L5ccNMwFf6wen9Q7j4DKSn1k6vvdLE_VFNlvuCRUqD2oMq-CYqlw5cS0pUDgg40dVOZWGOQ6COPzWR3AQroN4hr_9EPWWbwSDSjWJZfVJxtkkkBNjcV-LvonFp8SALzoBuEg5QOnsLxd14CNhIcMU6LJw9MTufb5dJALfUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشتِ احتمالی ستاره های منچسترسیتی در صورتِ سقوط این تیم.
😕
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/108654" target="_blank">📅 09:50 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108653">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1661f71c8.mp4?token=ToQHgdsnlfLF9dehkTEytlMXF8Prg-B1Cpw7vDLk3VtTxP-Zm8TFJXRbKiFhTvTWo-7I68T4eFkFRZT9OkgQ1q2Sz82v0hI4dpptMExH7fe9wVYrpD1fkqxDYkJwTXRKrcjI71aABYCoVWvR0DdOrnu13pLwnIyLFVQSzIHSZhfDIy4d1WhLGpEhFERTqOpdTrxOUi3WfsLEBy2NtAg5aEw-I5VDg9Tg3tE-KLdG6Gn3NIsXYhXfiyBBb4OCZGz5CmTomaPmZAyouorgJj5lFgxmTfjV9Our7CrNo8T2yRfSXopi8YqJqGRINvL_vX-3da6H5mg_hsUp89UHBKV1eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1661f71c8.mp4?token=ToQHgdsnlfLF9dehkTEytlMXF8Prg-B1Cpw7vDLk3VtTxP-Zm8TFJXRbKiFhTvTWo-7I68T4eFkFRZT9OkgQ1q2Sz82v0hI4dpptMExH7fe9wVYrpD1fkqxDYkJwTXRKrcjI71aABYCoVWvR0DdOrnu13pLwnIyLFVQSzIHSZhfDIy4d1WhLGpEhFERTqOpdTrxOUi3WfsLEBy2NtAg5aEw-I5VDg9Tg3tE-KLdG6Gn3NIsXYhXfiyBBb4OCZGz5CmTomaPmZAyouorgJj5lFgxmTfjV9Our7CrNo8T2yRfSXopi8YqJqGRINvL_vX-3da6H5mg_hsUp89UHBKV1eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سامسونگ هم داره آیفون می‌سازه؟!
👀
🔥
طبق کانسپت‌ها و شایعات جدید، گلکسی S27 Ultra ممکنه یکی از بزرگ‌ترین تغییرات طراحیچند سال اخیر سامسونگ رو تجربه کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108653" target="_blank">📅 09:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108652">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd1136457e.mp4?token=TA1WQEjQ-FlUIc5sKTbNeq6u8DgQo7W5Ne603_ypc_4Ut-TUTzq5OR21q_frfkewpg6m5IvaRflJ9AhnoIXp-bLGA3BomQFuZFOVVjZFZDfZkiYU92T-CNf_yEFJ78CQ7m7x1laTob5uOfXJtrYEy0XvuuWfH4Jo-G7a4C_MvQgPHx8hOXSxMjdP3qnm1oIDK6eemeHmQkiq2X8Ee4X3ovlK6ANQA2OkgYFMPziwxtltHo9eABgwc38kjxZ5hcu5Bii5Zy0kIYBIM9-V3wENvc8NVkQgkUNnGK_-QUrzY0KLzpRfyYq0d2MjQc6LtPGkyDjovWnhZeLli03ExNF8c1GSCBxmr1Ewcb_Y4N9LdhgPUPohZrqmBGphLW6btTD1oYxvb8xEoBoz5YOFsc3orb9q88Oa6Ju12OmQVOLeNf35aOCa15KVN_7DoN4Q3EghImxHQ_zbJKaNOUZ4nq5Kl3CSESfVe-PvV1iQA0FAVH-8vaLPKnB18OBhdd5_4kMeq-M6nzeA5eJpfyHra6coNKPHGfC5ZGw0jLHuiZE1TMUytgrDs8pTfCd7Mm10IxgnY2bz0pTzPwqeRiFghq7XthfrQSQZuHRoN1vI6KQIaMXe5qT7DYo6TCzHIcOZLqVj1UtAJ-THeYGT1TP_9Y_aeJfMvH8NrdFaNOELC74uADA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd1136457e.mp4?token=TA1WQEjQ-FlUIc5sKTbNeq6u8DgQo7W5Ne603_ypc_4Ut-TUTzq5OR21q_frfkewpg6m5IvaRflJ9AhnoIXp-bLGA3BomQFuZFOVVjZFZDfZkiYU92T-CNf_yEFJ78CQ7m7x1laTob5uOfXJtrYEy0XvuuWfH4Jo-G7a4C_MvQgPHx8hOXSxMjdP3qnm1oIDK6eemeHmQkiq2X8Ee4X3ovlK6ANQA2OkgYFMPziwxtltHo9eABgwc38kjxZ5hcu5Bii5Zy0kIYBIM9-V3wENvc8NVkQgkUNnGK_-QUrzY0KLzpRfyYq0d2MjQc6LtPGkyDjovWnhZeLli03ExNF8c1GSCBxmr1Ewcb_Y4N9LdhgPUPohZrqmBGphLW6btTD1oYxvb8xEoBoz5YOFsc3orb9q88Oa6Ju12OmQVOLeNf35aOCa15KVN_7DoN4Q3EghImxHQ_zbJKaNOUZ4nq5Kl3CSESfVe-PvV1iQA0FAVH-8vaLPKnB18OBhdd5_4kMeq-M6nzeA5eJpfyHra6coNKPHGfC5ZGw0jLHuiZE1TMUytgrDs8pTfCd7Mm10IxgnY2bz0pTzPwqeRiFghq7XthfrQSQZuHRoN1vI6KQIaMXe5qT7DYo6TCzHIcOZLqVj1UtAJ-THeYGT1TP_9Y_aeJfMvH8NrdFaNOELC74uADA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
📊
آنالیز تاکتیک جذاب این‌فصل آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/108652" target="_blank">📅 09:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108651">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f591d52518.mp4?token=FfL7zgWiZAwMi0pEUWPL1jW9Nl8Zu35X3cHZJtqzQRqGV-o41hNfdQE32Wxrc8NfWFVmkdJy1iEJa09bfF7T8O9njlxBOkuVVncdFZgSuBCzWkL2ZTA7JEdvSgH6OikJ5I9IeHXrjU7lrVwPCDuNlegkAQrmP8-6V9fB7zyQM1Fo7FIjXpMHQRatHmA-PzRZsmim52-wuV5UNNr8YLDUZfSVXy8llbgAT3tBfanwNP7prDE05Qxi0UQR084_8LXMeDdFcxCRoOapYvKR6XrDCMe3f8_Q6qRoulMngPXz1bZeIgwilpu4-1LG0HF-evi8tH4ClQXgNBbeSl00kXw7Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f591d52518.mp4?token=FfL7zgWiZAwMi0pEUWPL1jW9Nl8Zu35X3cHZJtqzQRqGV-o41hNfdQE32Wxrc8NfWFVmkdJy1iEJa09bfF7T8O9njlxBOkuVVncdFZgSuBCzWkL2ZTA7JEdvSgH6OikJ5I9IeHXrjU7lrVwPCDuNlegkAQrmP8-6V9fB7zyQM1Fo7FIjXpMHQRatHmA-PzRZsmim52-wuV5UNNr8YLDUZfSVXy8llbgAT3tBfanwNP7prDE05Qxi0UQR084_8LXMeDdFcxCRoOapYvKR6XrDCMe3f8_Q6qRoulMngPXz1bZeIgwilpu4-1LG0HF-evi8tH4ClQXgNBbeSl00kXw7Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
مرور خاطره گل عقربی اولیویه ژیرو به کریستال پالاس، با بازگشت اسطوره به امارات⁣
ژیرو: من آدم متواضعی هستم و اشتباه برداشت نکنید، اما فکر نکنم دیگه مثلش رو ببینید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/108651" target="_blank">📅 08:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108650">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب :)
😊
😂
میگی نه؟ بیا تو چنلمون و ببین!
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/108650" target="_blank">📅 01:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108649">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q9Xp9ZCFkMMFSyjNT1snvDM76XMThrv0bz9EEOnnq6jRkgL8V_2OhkmKDDdJPZd5mGcSVlrMfkg47TMnY6MUFlMpd48cPuSPFcxZd2P0HkqVUxFvBhELXYgBqiwyyL6P1AMqyqMsMpiufUQfJqhKHH6OoIDzmYR671rV_nLz2mgyPtHKlui3cQyn4_SEO0jbWHBvkApAsNtBLqNkv4NBswO0tkcPhEv2FpnhSK8pGtBVvJ1SeIKd1NlDCc3AGqqf7DEPbXmm2Dx5DIOiJe8NRd-0_Mv9YFHbVK5OyNuq9jLD5tGzXw417OGUFtM0Mzkfam9HBPs7L2LlInKzKKdBYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب :)
😊
😂
میگی نه؟ بیا تو چنلمون و ببین!
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108649" target="_blank">📅 01:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108648">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108648" target="_blank">📅 01:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108647">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umsottd_yq9PLsI2BmyNIcj_dwqu8GQOL7Sp_Z1uhWRRRJBpaQVlKZ5eVCHI_82ziszezUHot4eENmt6n1IK0U2l3uSSkqSizVKLvq_gyQBcl2ykN0QnlQookB6Msy7jTVWy-pFlDI9qLXFoZniu_i9A1KXOq9RvekzV5ewU291fS-QSSGuIX4W7xGsNGpxgEExvmjD7TUUTe6g8uK_G3hjNiw9M6fDVQLuxaNHk-Zy3ncB8Hts6_yf4uV_ivJqTFINLXMHjDdB49h1B97h7cCn0J0PxZuKh5pyYSF4vKKYoACXhBl6zvzILPZklCBT4-y6fCZNH52GNzHMJxgVwBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🏆
هفته‌دوم لیگ‌قهرمانان اروپا؛ دهمین برد در دهمین بازی فصل؛ جهنم استانبول هم مانع پیروزی پرگل شاگردان فلیک نشد
🇪🇸
بارسلونا
😀
-
😃
گالاتاسرای
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108647" target="_blank">📅 00:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108646">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phcVDrau2wBXwHGF02Z1kv9mHJudVTRF2OHoN7vYmAkdMwzhilzTBGPh-Gv83hAn2zssLgP3YCGP6BWYA2auwLpYZLPZWbqE6HfFKc450UHDMe6gGJ5THWe-voLmFu-VRR6Kb5u0oKaa1Jt5007tn4n2BeV3fL3edpHGxQS-mHhFm42goTQho3THTBNc4DT_RWaNXfDka8eVze-mFAcb8KBZvmrY8JefeSObddEvl4qbByG2EOsvmwbIp59uftD1S63rV_t4n-HuOOci3HrTWbPYjYK1OkjvnEUH735cHizyFMjUf7qT072NE-zviXSNkqpcxgIyrFE_NWalhFSEog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
نتایج بازی‌های امشب لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108646" target="_blank">📅 00:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108645">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lv-zbuo4VtEtF_eNCA30vz7LvnO7962xJ-_yW4PHQtRz93H0seDxPuzmFdEXo5T7u9GBg06ssUksOZ_27M7yffp--zK70r4b-TzfiUslvA5BOSL0az5sXu1Fmd-tFL-U_grdv4OVLZyk_fzr9GcFlCkaHlQA0u3il-096qxMk8PhehwDrKSPpcCd0KqSjLvbj9-KxPXGpMNS5Uc6CPyqH55wwKLl0xjWMD5CSdCFYZKRDxXmnyICwYpUvAEOepxSSj5A2Omt8btPE8lw2rY0DSqfz4nf36HUL7-HCjOZqVz5N2h1ZWo8ZpsEKvGB0FVYltN2u6OPMy_LiaAsBMnlGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
لیگ قهرمانان اروپا | در همان ثانیه‌های ابتدایی غافلگیر شدند؛ وضعیت کریک در منچستریونایتد بحرانی شد
🇪🇸
اتلتیکومادرید
😀
-
😏
منچستریونایتد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108645" target="_blank">📅 00:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108644">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ev8hxMfRLctKz1ad1Juok_-ABRwLwHdTb-LduQRGzTMJAMq_B3Eki3GhGvejS7rQcgZP6ynmk2B1Y-iTDUW-ed024W7lxoa30hhRxd1YpBAShNt29T_kEUKviUppoOz8P7e_dqzLnbQlmkdIC6jIV8qbwIMfoaEs1ic5u9iRwV91mGMlWVly9h1R1KgjsqYXWVN5aP1AG1xQuHambXpBN_ljFbU8fApYExGcGyCfztQJ-SFnoK9MmIJBtCPxzGL7HL5uJvBrDE_nIM68MAj6-kuGRwOzFdTR-o87LIjCKL148qCCxKghabESmt6xXAk0Ne1ly2VUJIJbJK3MLlKbNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
لیگ قهرمانان اروپا | تساوی دور از انتظار بایرن‌مونیخ مقابل نماینده نروژ؛ توقف شاگردان کمپانی در دیداری جذاب
🇳🇴
وایکینگ
😆
-
😆
بایرن‌مونیخ
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/108644" target="_blank">📅 00:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108643">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbm4I8ibe-hszfFeLw_vY6LlkjIPGrMYQFTubTpAyDM8BOf1CUFZZ6qpUs3OySBq5j9NrUullUMVDYxXK8O2-XrEaVqjAy0k1unyuj08UwQ7IK0nIiQlvh8eH8c7tJ6s_olPiKLKBzUgMoL6txaQMqy7F4fzwc9afB2gN08ByQiNrQ5qEoEwWid9LZFyZVQ8249Fo8MOsm2G14swhBXPGGcEDOg4NchFaDLh85c3CPnGC1aVdnYuPEdZ45Bw6wZl-RloGTRjKjpLy_DRKe8-rRl9RwW6ttTrnHj8uTVlxAAYJif_VSL2_1xnAJ9XEzYr9aUmC06SQV-2nXd4tKfInA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🏆
هفته‌دوم لیگ‌قهرمانان اروپا؛ دهمین برد در دهمین بازی فصل؛ جهنم استانبول هم مانع پیروزی پرگل شاگردان فلیک نشد
🇪🇸
بارسلونا
😀
-
😃
گالاتاسرای
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108643" target="_blank">📅 00:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108642">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/def4417737.mp4?token=lw8o2DopQKFV9fgBEGpFY74XpZ7NcA96QOtrsBympLQhEs6LWbTjf_7sRkGqusN1er_4NMEBPSzH-50dXnE49GgBunt6t01i1aUvP5uwO6NKmhroavyQO9s52Q4SPMvL7JRYLCr8TU0selC_TJHEeuanRmdHbAgdyqQaFg1W7yf4auJ5FXTmspU42nuBHLsZHEjWZDmjCAaRM87SWmgeh54VnJGNkQeeJVDNdIUmLtPNF_oaeTWOAvXKXgptOFtpALfRZxir0C9kroyWh3_X-MGYvTbxxM8_wvWvOmVjTZMLAyNSIG6AdIh1P4ISYF2iEeHlbPNgUX0fzcfyLnvGy2DOD5VC-Qo5JMkxoFUiiI0sOtAJ68Vw5JUVq-BiJYr3oT-FbN5A2LceujuC1yv-nXrTZHsvBD6is_1kInlQ3kddHiBtY6x3B2bwUiN0bfYd02R52XzxH9T1kjx2ciHQGlyP7Z6GP1sv8J6la2YpTab7eCh8DvJMdZnZiOQNsUAOoKlfyfCc4JBJJjcZ9YCM-aBM8LHIti_LfaeCWRBY_QnebOZX2R1BSh9HzdYM0AxODM79oUeAOCC5-n5Iv4rqYLM0e-DQpNZN9-EsVVysq95nF1pzf9fihZSrng5BzYsL-lK6dCm5Eu67rBpssfi3VOQp_YtpYxbiwNySJOVAcAM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/def4417737.mp4?token=lw8o2DopQKFV9fgBEGpFY74XpZ7NcA96QOtrsBympLQhEs6LWbTjf_7sRkGqusN1er_4NMEBPSzH-50dXnE49GgBunt6t01i1aUvP5uwO6NKmhroavyQO9s52Q4SPMvL7JRYLCr8TU0selC_TJHEeuanRmdHbAgdyqQaFg1W7yf4auJ5FXTmspU42nuBHLsZHEjWZDmjCAaRM87SWmgeh54VnJGNkQeeJVDNdIUmLtPNF_oaeTWOAvXKXgptOFtpALfRZxir0C9kroyWh3_X-MGYvTbxxM8_wvWvOmVjTZMLAyNSIG6AdIh1P4ISYF2iEeHlbPNgUX0fzcfyLnvGy2DOD5VC-Qo5JMkxoFUiiI0sOtAJ68Vw5JUVq-BiJYr3oT-FbN5A2LceujuC1yv-nXrTZHsvBD6is_1kInlQ3kddHiBtY6x3B2bwUiN0bfYd02R52XzxH9T1kjx2ciHQGlyP7Z6GP1sv8J6la2YpTab7eCh8DvJMdZnZiOQNsUAOoKlfyfCc4JBJJjcZ9YCM-aBM8LHIti_LfaeCWRBY_QnebOZX2R1BSh9HzdYM0AxODM79oUeAOCC5-n5Iv4rqYLM0e-DQpNZN9-EsVVysq95nF1pzf9fihZSrng5BzYsL-lK6dCm5Eu67rBpssfi3VOQp_YtpYxbiwNySJOVAcAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم بایرن‌مونیخ به وایکینگ‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108642" target="_blank">📅 00:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108641">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گلگلگل سوم وایکینگ‌ها به بایرن‌مونیخ</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108641" target="_blank">📅 00:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108640">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdfe06f9c.mp4?token=YUdFdvIZk_FjdSJbHYLQ8qcsMMoB13xfXIs7IhnoZmpAt1SOMlDzDVahI1eYT1dSAvDGsVjYHfvJWijW5lmrtAsw1_EARJlW5G_bbdoEauk2nm-g_ACkV1HXdxN_jR-eJ3HkHRKRryIhWflwCwVk038IDo1q_L0NtML7CTbksfqkbnnbhWeAeatW2HQQV-9RxgFf_FhkQOkkDUxRhAU_JFDEWfO_KptFJ3EnVenfDkDxWgIa87nUKxxT2sc-ZCp-EVdiIqI_tf2BUl7W5EAiWP8Hzw5O6tdkpFEhg6mtrBdUA8oQ3_mdmDz8XGthhsF7GrHWdVZXRQM47dWQ5ujuGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdfe06f9c.mp4?token=YUdFdvIZk_FjdSJbHYLQ8qcsMMoB13xfXIs7IhnoZmpAt1SOMlDzDVahI1eYT1dSAvDGsVjYHfvJWijW5lmrtAsw1_EARJlW5G_bbdoEauk2nm-g_ACkV1HXdxN_jR-eJ3HkHRKRryIhWflwCwVk038IDo1q_L0NtML7CTbksfqkbnnbhWeAeatW2HQQV-9RxgFf_FhkQOkkDUxRhAU_JFDEWfO_KptFJ3EnVenfDkDxWgIa87nUKxxT2sc-ZCp-EVdiIqI_tf2BUl7W5EAiWP8Hzw5O6tdkpFEhg6mtrBdUA8oQ3_mdmDz8XGthhsF7GrHWdVZXRQM47dWQ5ujuGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم اتلتیکو مادرید به منچستر توسط لوکمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108640" target="_blank">📅 00:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108639">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گلگلگگلگلگلگلگ اتلتیکومادرید دومیو زددددد</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108639" target="_blank">📅 00:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108638">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d76e2a5b60.mp4?token=I8XdDQJsXX5Vb3coYtPX7K0mvaZZbuImuOlHniHldVr2x4j8f3w4KO5v--NjQPefSqZ-PNjnG8jByjPvEDciwlYE9z3TiXatAnmxi98FFCUeGw7Q3ZO6GiQkGWFsAxuA-K_ge11sBZq2LlWdFENORlgl79AhP7LXfK9IfB_aQ86xmLCYNRgFD8pWvhS8u_-0sLx8B26mWJpjSBSK7GioidXgR6XnjAyNq6Ft-XDzyFahqqxhx1UGJNQh1lwLhgh-Jroxsb17wES5H5th6lZvAJryRz6e14CpmIGHAC-ghrPQVBI5Do3qRxo2NP9qfyc2EVkdd16qa_StKLP6VBxlFYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d76e2a5b60.mp4?token=I8XdDQJsXX5Vb3coYtPX7K0mvaZZbuImuOlHniHldVr2x4j8f3w4KO5v--NjQPefSqZ-PNjnG8jByjPvEDciwlYE9z3TiXatAnmxi98FFCUeGw7Q3ZO6GiQkGWFsAxuA-K_ge11sBZq2LlWdFENORlgl79AhP7LXfK9IfB_aQ86xmLCYNRgFD8pWvhS8u_-0sLx8B26mWJpjSBSK7GioidXgR6XnjAyNq6Ft-XDzyFahqqxhx1UGJNQh1lwLhgh-Jroxsb17wES5H5th6lZvAJryRz6e14CpmIGHAC-ghrPQVBI5Do3qRxo2NP9qfyc2EVkdd16qa_StKLP6VBxlFYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم بایرن‌مونیخ توسط لوئیز دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/108638" target="_blank">📅 00:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108637">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🟥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لنی‌یورو جلو اتلتیکومادرید اخراج شد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108637" target="_blank">📅 00:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108636">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🟥
🇩🇪
مایکل اولیسه بدلیل دریافت کارت قرمز بازی هفته بعدی مقابل آرسنال رو از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/108636" target="_blank">📅 00:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108635">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلگلگلگلگگلگلگل سوم بایرن مونیخ به وایکینگ‌ها</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108635" target="_blank">📅 00:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108634">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b2a48903.mp4?token=QUJP0wyPcTOe3aVerirz2zwKfRKboKd1-WPTfo5SjDMMyFFsokgYwjVlqnRuzoRIoRubQevxA4vJjzHHNNX9VxSjse-PCAi54DxLrsQGmSOr46Ua9My81RgqGUVO5BdJY_sAOkjwdrqwcPMgwVwG16cSgxuVG5Xnxje4GR-aZ223jDnz8uaWeuQ88MA7witSN8V0mFhCPlIoQe98nnEfF3T5WYXInOCqmoyx-cj2GNnY-d0pMFZSkk8cdUoZlFWbLzm-nLPhscgq-lRwIdOB0F_ZfNjbPG6mCLaLZwbJtwRi95m4y54dv7rPppN0_CwuE4rX2pkQvQvDGbugCKsloQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b2a48903.mp4?token=QUJP0wyPcTOe3aVerirz2zwKfRKboKd1-WPTfo5SjDMMyFFsokgYwjVlqnRuzoRIoRubQevxA4vJjzHHNNX9VxSjse-PCAi54DxLrsQGmSOr46Ua9My81RgqGUVO5BdJY_sAOkjwdrqwcPMgwVwG16cSgxuVG5Xnxje4GR-aZ223jDnz8uaWeuQ88MA7witSN8V0mFhCPlIoQe98nnEfF3T5WYXInOCqmoyx-cj2GNnY-d0pMFZSkk8cdUoZlFWbLzm-nLPhscgq-lRwIdOB0F_ZfNjbPG6mCLaLZwbJtwRi95m4y54dv7rPppN0_CwuE4rX2pkQvQvDGbugCKsloQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌چهارم بارسلونا به گالاتاسرای توسط آدیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108634" target="_blank">📅 23:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108633">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گلگلگلگلگگلگل سوم آرسنال به لیل</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/108633" target="_blank">📅 23:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108632">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پاس گل از گابریل ژسوس
🔥
🔥
🔥
😂</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/108632" target="_blank">📅 23:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108631">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گل زیبای کریم آدیمیییییییییییی</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/108631" target="_blank">📅 23:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108630">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گلگگلگلگلگلگگلگلگل چهارم بارساااااا</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108630" target="_blank">📅 23:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108629">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گلگلگلگگلگلگل دوم آرسنال به لیل</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108629" target="_blank">📅 23:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108628">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EC1aHlQOCK30e4nUqcNvhO-5_IEoDcxXxaYC5RWtv9qZHAmDv0OBhFGb-ycZjNfhhORuODsO3iPnYfpk_xUR0IrPb_7AkQZpXoVvaQrQgjmwPQe35rzre991zxYp8AenjDP7O5nUjvb09awUnlqHmKE_qWcrxwaqUYKpdDVD87PmmRYbTIrjZvH0aKdsZr0Nohzd2cBO_AxUBhwpGz-7relDPpqOWEo2N3NcYHW3hf_tPIOJFLAL_J98oW3s0nfE_xf1skca55my4UtOZV8OWX3jROWMNxCsWa2vZd3ilDyYMBX2YVs8FQfa2GzicrQ8RmLH3uUXSuuChXnG8Ukv4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
▶️
🇪🇺
نتایج بازی‌های تا این لحظه</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/108628" target="_blank">📅 23:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108627">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گلگلگلگگلگلگل آرسنال یکی به لیل زددددد</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/108627" target="_blank">📅 23:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108626">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf53f669cc.mp4?token=tgfK6j7UBgv42DdFvcHSGhJNKhGlw6GXIdZsDFGxOAqMY0ME0ADQnjFWnsIVJU4Z-VaFuXifhzDidnXISPGhRad8JToL7Xpr0kQx-Ub5WV4R0O6MxYlQgj7FDdOBIg3XgK3ZHGnCSYXTpnecla94_UdwDmzp4LbhRil7Fm4eN4y-Dmlh-RKSPnntwj05qwzGE8wMf6wWLPD6f3w2TTOeyWpWzFxMG-utrZy-81yUq_tWASMz_nodZEAEEdF0TTGnqqq4KkHbYMuvYZKDTgi0PzFW27KkciZ6_HVru1nhbyFbD7rBaUFN1gBgPg37UCkM1USAySLStUc6KgELPkXwGKZJz_HYRshMH51im8Pht-1ZLJkI7R3TzeD2lq7uGtSFPpKchaqBxBBFrEbVMTieYf15LPWUFu2egTGlBXGf2b0IBpMPDFXe6kK7qjArzxztT0c1rH61-A3mV6p53245C4z9ggecTC2xxVW8XQyJUehbBT6NeXCqaZ6PRYdBrJ5TxiEENommhFLBlfuLN_p-DH_A_LSMJLAjizN51ChoFRD-gP98wPn8SJKP3w0cNEBtSk6yYYhtyjZykWQcuiddi5Hhd7KcOI0G-Z4uM5pQfINMMV8CBKSAurl76UEFGcO2NQQLbi9FVG1OU_DhCXMtF93DN06TQBW9QFozO63qkkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf53f669cc.mp4?token=tgfK6j7UBgv42DdFvcHSGhJNKhGlw6GXIdZsDFGxOAqMY0ME0ADQnjFWnsIVJU4Z-VaFuXifhzDidnXISPGhRad8JToL7Xpr0kQx-Ub5WV4R0O6MxYlQgj7FDdOBIg3XgK3ZHGnCSYXTpnecla94_UdwDmzp4LbhRil7Fm4eN4y-Dmlh-RKSPnntwj05qwzGE8wMf6wWLPD6f3w2TTOeyWpWzFxMG-utrZy-81yUq_tWASMz_nodZEAEEdF0TTGnqqq4KkHbYMuvYZKDTgi0PzFW27KkciZ6_HVru1nhbyFbD7rBaUFN1gBgPg37UCkM1USAySLStUc6KgELPkXwGKZJz_HYRshMH51im8Pht-1ZLJkI7R3TzeD2lq7uGtSFPpKchaqBxBBFrEbVMTieYf15LPWUFu2egTGlBXGf2b0IBpMPDFXe6kK7qjArzxztT0c1rH61-A3mV6p53245C4z9ggecTC2xxVW8XQyJUehbBT6NeXCqaZ6PRYdBrJ5TxiEENommhFLBlfuLN_p-DH_A_LSMJLAjizN51ChoFRD-gP98wPn8SJKP3w0cNEBtSk6yYYhtyjZykWQcuiddi5Hhd7KcOI0G-Z4uM5pQfINMMV8CBKSAurl76UEFGcO2NQQLbi9FVG1OU_DhCXMtF93DN06TQBW9QFozO63qkkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی بایرن‌مونیخ به وایکینگ‌ها هری کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/108626" target="_blank">📅 23:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108625">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">لوووووویز دیازززززززز</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/108625" target="_blank">📅 23:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108624">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">لوووووویز دیازززززززز</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/108624" target="_blank">📅 23:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108623">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گلگلگگلگلگلگلگلگ سوم بایرن‌مونیخ</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/108623" target="_blank">📅 23:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108622">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">هری کین دبل کرددددددد</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/108622" target="_blank">📅 23:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108621">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بایرن‌مونیخ مساویووووو زددددددد</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/108621" target="_blank">📅 23:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108620">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گلگلگلگگلگلگلگلگگل</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108620" target="_blank">📅 23:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108619">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/93ba7eabbb.mp4?token=jzi8ZMA0-cVCVrHswgu35PWwC-B1lM0BgltlL4ulpmepDzOjzJ-TPhw9gsI0ej98CCR1qpML_qXT9BQsh0_RwiJYynnF63k0RZfJkEMzjAev47iyG8eUG62lsCW2s-QqkrmYfLLa3uD1a7qQTTkQIoQB6Uke967DmULCmxaCipbhpp463DJyqSCgZBML-Lw3ri-OGBiiiqmWlxpm_Q8kNHa4eCMcVTV7pQQ8K6KG3ycudOziFZRqHpnEl11k2IAaUEg0bJ0BpebwfFFG4RXmDah4d-jTHv48Wch347MWR-QbnjZQwlfGFlZFsb9GWf2pska9-m-mNjWtiG463k-Uj7QfEBt6IDilsO9jLuPPc8v0ua8qvANRGVMssI9fEq-6CQ5A8wkL8yDiHIrwkmVpyii0sLmkwV93SXWXlmdc_7rQd1qWdK11tOPzdjYyC8-6WpE47AxbrvT2tkrdP1X7ZpstHJNbFoibCuM9pMZbPBPBmFH92wNQJ04ezfEXKD8_QXFMm2ec-vdrM6FEjYHhkVSzJITm1nHRyKsXL0CoFLXjYL_uBp1H42inkOmh921wuNdd7dlpOg_V9FfkSGwk5Tp6wps_nF0HmFUheWiaU3jyJANojc6zlsCKMYCp7pgymTZiQVxBDBn_c91zUhjNlxBdBof19JPfT3tMXNefSRA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/93ba7eabbb.mp4?token=jzi8ZMA0-cVCVrHswgu35PWwC-B1lM0BgltlL4ulpmepDzOjzJ-TPhw9gsI0ej98CCR1qpML_qXT9BQsh0_RwiJYynnF63k0RZfJkEMzjAev47iyG8eUG62lsCW2s-QqkrmYfLLa3uD1a7qQTTkQIoQB6Uke967DmULCmxaCipbhpp463DJyqSCgZBML-Lw3ri-OGBiiiqmWlxpm_Q8kNHa4eCMcVTV7pQQ8K6KG3ycudOziFZRqHpnEl11k2IAaUEg0bJ0BpebwfFFG4RXmDah4d-jTHv48Wch347MWR-QbnjZQwlfGFlZFsb9GWf2pska9-m-mNjWtiG463k-Uj7QfEBt6IDilsO9jLuPPc8v0ua8qvANRGVMssI9fEq-6CQ5A8wkL8yDiHIrwkmVpyii0sLmkwV93SXWXlmdc_7rQd1qWdK11tOPzdjYyC8-6WpE47AxbrvT2tkrdP1X7ZpstHJNbFoibCuM9pMZbPBPBmFH92wNQJ04ezfEXKD8_QXFMm2ec-vdrM6FEjYHhkVSzJITm1nHRyKsXL0CoFLXjYL_uBp1H42inkOmh921wuNdd7dlpOg_V9FfkSGwk5Tp6wps_nF0HmFUheWiaU3jyJANojc6zlsCKMYCp7pgymTZiQVxBDBn_c91zUhjNlxBdBof19JPfT3tMXNefSRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول بایرن‌مونیخ به وایکینگ‌ها توسط هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/108619" target="_blank">📅 23:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108618">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c86178bbb0.mp4?token=RdM9CepxAY5noZM57ei6IurSbGG2hLhpsI2Pu8f-F6Zt7eXwE7F6oSyuc7fW68-9dPoq8MAezhQsc5kpbkuLaklw1FSzgtVzmVdmqlNusEIcgSkfnDcz0SNQRLLJRhPjwu0pY6E75vjVoG_pBUoVKYW2Bz-jtgpGtHRPM0bGteyXhjLJevm53yxHW0AQQpxx6Hq-D7xfzBJS1tBj7iZmUhPSQa7RUbGPLaX2DfAHM8Hb99CLF3JoV2-6lPpVP4LnBfCWOvm7sc33sI6KQEqUQKgwO6iThTWgCWxG-v98Rsm1n98YfveEzHAHReQeSucpQBlitodzSvwftokFh7IJXGd-s2JyRFK5v468i7ixwkLrKPQPzAPrvkgVe_O1iUd_h01WS-O9WpWIjueVe2udwJqwNVzuZY2KjRucFJk5Gf6hrgLgm_cYnY41sbQdzpKEPuaLTWTJFZkc7LF2ywK7CO39GO8F6aI07B1tnVVlpg1uNQ5Zr9MCqNZTHIMCCemIFcPLrvdm50WLunR9ZyBBDjtFjheJee3I6vQkQXdEZ_zr4WpJZORT_g7FLQE77ODd876pO5Bzjlh2pnBOlTf61jNVSUts95JDlboO1-yOTMSaehEqTb3pA9uAqR2y1ck50eA4KHCDY8Egk9Sa94KL0z-Uy1qrKngovhEwdgYyHSE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c86178bbb0.mp4?token=RdM9CepxAY5noZM57ei6IurSbGG2hLhpsI2Pu8f-F6Zt7eXwE7F6oSyuc7fW68-9dPoq8MAezhQsc5kpbkuLaklw1FSzgtVzmVdmqlNusEIcgSkfnDcz0SNQRLLJRhPjwu0pY6E75vjVoG_pBUoVKYW2Bz-jtgpGtHRPM0bGteyXhjLJevm53yxHW0AQQpxx6Hq-D7xfzBJS1tBj7iZmUhPSQa7RUbGPLaX2DfAHM8Hb99CLF3JoV2-6lPpVP4LnBfCWOvm7sc33sI6KQEqUQKgwO6iThTWgCWxG-v98Rsm1n98YfveEzHAHReQeSucpQBlitodzSvwftokFh7IJXGd-s2JyRFK5v468i7ixwkLrKPQPzAPrvkgVe_O1iUd_h01WS-O9WpWIjueVe2udwJqwNVzuZY2KjRucFJk5Gf6hrgLgm_cYnY41sbQdzpKEPuaLTWTJFZkc7LF2ywK7CO39GO8F6aI07B1tnVVlpg1uNQ5Zr9MCqNZTHIMCCemIFcPLrvdm50WLunR9ZyBBDjtFjheJee3I6vQkQXdEZ_zr4WpJZORT_g7FLQE77ODd876pO5Bzjlh2pnBOlTf61jNVSUts95JDlboO1-yOTMSaehEqTb3pA9uAqR2y1ck50eA4KHCDY8Egk9Sa94KL0z-Uy1qrKngovhEwdgYyHSE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌سوم بارسلونا به گالاتاسرای توسط گوردون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/108618" target="_blank">📅 23:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108617">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c2159385.mp4?token=Kw55fpUnUvyF7LKnmRuSgXwiPRLbBpmi5Q_V3wHRKPir_PO0NpuqSNnsIerPRAeSaK4TO0yB3h1xfA_rZo-SMsVfEtOzgxWTLuDLU57t3GxDvUEztnJ7L4QmVGf4Lcxi92hkHOFJQaMwL2lhM0IwHR_xkSTOZM8vcbe8nP-tO1U0U3MJdkFjSNMJilSym20kLwHTds5jy3RE3mizcGdc1v4omPyOYze1QvMhWjwndAJGaQbgsUzc-Wb49yTSzODqwHQh95dnOtEvdy15pwaFg5U45CLYjZm1XKTBVFwkBLytrzz7OE4_GpbMyIP4NQTu3b9JbsyZdRKgKUa1VQF_dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c2159385.mp4?token=Kw55fpUnUvyF7LKnmRuSgXwiPRLbBpmi5Q_V3wHRKPir_PO0NpuqSNnsIerPRAeSaK4TO0yB3h1xfA_rZo-SMsVfEtOzgxWTLuDLU57t3GxDvUEztnJ7L4QmVGf4Lcxi92hkHOFJQaMwL2lhM0IwHR_xkSTOZM8vcbe8nP-tO1U0U3MJdkFjSNMJilSym20kLwHTds5jy3RE3mizcGdc1v4omPyOYze1QvMhWjwndAJGaQbgsUzc-Wb49yTSzODqwHQh95dnOtEvdy15pwaFg5U45CLYjZm1XKTBVFwkBLytrzz7OE4_GpbMyIP4NQTu3b9JbsyZdRKgKUa1VQF_dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم بارسلونا به گالاتاسرای توسط لوپز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/108617" target="_blank">📅 23:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108616">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سوپر دریبل و حرکت فوق‌العاده یامال فقط
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/108616" target="_blank">📅 23:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108615">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آنتونی گوردون</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/108615" target="_blank">📅 23:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108614">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بارسلوناااااااا</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/108614" target="_blank">📅 23:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108613">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگ سوووووووم</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/108613" target="_blank">📅 23:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108612">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گلگلگگلگلگگگل بایرن‌مونیخ یکی زد هری کین</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/108612" target="_blank">📅 23:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108610">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سوپر پاس گل لامین‌یامال
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108610" target="_blank">📅 23:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108609">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فرمین لوووووپزززززز</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108609" target="_blank">📅 23:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108608">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/108608" target="_blank">📅 23:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108607">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گوردون دروازه خالی زد بیرون
😂
😂
😂
😂
😳</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/108607" target="_blank">📅 23:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108606">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvxjAOKxGWEqEoik5jCVM4yuM1Y-AubLwdrgAWiZ5KO3g-kNaCWFQI4ALp0gyEfnoyVdsBQXBXIYHP31I7jgUj3W49GZ4-N3yORLQ57AgLxgnfP1QfLR7ASZjxIKebacEFfFVsWG0cDub5fTJd6haZOqquKk17V3wJ0hO0KPHlBnqLHJgfvjyJa3cQaRrCMyo2qiKKCysbZWQKnulKkt2fYk6mNL8KVvQkx_iDsdkpciV8u2Y2RXEhLnvaEBhcXHSU5d5XiRLQFmpU82TSqvrWJwvTICoH5FbEMZ6x3HkUezrB8oCaObTad4bT0EeCip7MlzOenk7wU6ZreqXcCVQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج کامل نیمه‌اول مسابقات امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108606" target="_blank">📅 23:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108605">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گلر گالاتاسرای ۵ تا گل خریده برا تیمش</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/108605" target="_blank">📅 23:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108604">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78ba46272.mp4?token=RnztQc9I3kKVCHyp4tnxMLYWUq0UzloSi6tphihU6C-ElhY6sHhhTali1Ngp3HuNhcsUcMa_v7FJeRYkWqHi-H3Yv4N0joxACsO4YTIhpD5HpNtNFWTzaXZyNrZLMEcxXZah4MG3DCBdQlO3A-RlrKYhjZj6RGVP-RWW_0o5PE5iIX0ZSxl6kd-T7pTic0CQw9zZHzhNw5jnv78eSwhioJ9hErKNpozDHNfYoR6-JdnkA6XCqNJ0Ocfg3Sk76DB2aU4Tun4fgNbkSfjdqRlKUeCu1XzvsNwn2VgyBiezqKgVt--apTQr7pR-x7xYvWirSrQhA-Tiohn-TaEH6rTbOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78ba46272.mp4?token=RnztQc9I3kKVCHyp4tnxMLYWUq0UzloSi6tphihU6C-ElhY6sHhhTali1Ngp3HuNhcsUcMa_v7FJeRYkWqHi-H3Yv4N0joxACsO4YTIhpD5HpNtNFWTzaXZyNrZLMEcxXZah4MG3DCBdQlO3A-RlrKYhjZj6RGVP-RWW_0o5PE5iIX0ZSxl6kd-T7pTic0CQw9zZHzhNw5jnv78eSwhioJ9hErKNpozDHNfYoR6-JdnkA6XCqNJ0Ocfg3Sk76DB2aU4Tun4fgNbkSfjdqRlKUeCu1XzvsNwn2VgyBiezqKgVt--apTQr7pR-x7xYvWirSrQhA-Tiohn-TaEH6rTbOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل اول بارسلونا به گالاتاسرای توسط کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/108604" target="_blank">📅 23:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108603">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اتلتیکومادرید دومیوووووو به یونایتد زدددددد که رد شد</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/108603" target="_blank">📅 23:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108602">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گلگلگگلگلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/108602" target="_blank">📅 23:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108601">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رفته وار داره بررسی میشه</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/108601" target="_blank">📅 23:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108600">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رفته وار داره بررسی میشه</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/108600" target="_blank">📅 23:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108599">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اسطوره ژائو کانسلوووووووووو
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/108599" target="_blank">📅 23:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108598">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بارساااااااا</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/108598" target="_blank">📅 23:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108597">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108597" target="_blank">📅 23:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108596">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d28a95756e.mp4?token=Na0iEgjB5Lj0z1ULZyAB3u5gJXs9TyyKVk4Dz_aWlk7a2oO0wIE3mRf-ugcVR5n317axfyNr_8CLeo6moq_9bCLi9zhQUiDTOFLjx4HVDDVjgN2BLZ7AHbxaLSGSnwv1lII0v-PYbVNK-trHCIBHq8BzmocwrWREN9huu87rY82auyuykDM8nsKRqkM8JsZchfLA30wIAEbrU07m39PoxOIzbqpsMHuguhfkGPTQ-1vvHwP3R_lu0GppZ9TOH64MUYwH_eMrJZipt96mGwb7Tsx49vOJFcWFwfuhlqoRlmAbi0aa4GXvQ5EpB95Wb3BAAVG31Z5eJkbLHr42fvmaGAsiRNNfJ0lmIN0LQYKkcbtxPOIDAIj3mO8k2t3w7Wp39FkLPvL3-zHfAhnLOTBOgdG9WzQDNZkctIPa6qBvOMuZ1x3DdQHydJ4HuWhz00X2rBApoqeBZ2ElV5MoZB5UiFzO2YX9TvQbS5OcQ8f0Vc3paNm3LRgWp4H3CzBaOEd_Q4xcrNIg_2SsxKv-m46nfNuPoHpXun4o33d9tOB-amgXhnO6j9Sihepgna8OnakjSRBdujq9NQCDP87tpb-E5cHa8qi4SUqWQ1SGR2BwifxsIay0B9IUMoC3VY5Ew-08fFEGpDIvlZf5RBy8JbUWDdlbr92aRKfFtGOM2OKS7CA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d28a95756e.mp4?token=Na0iEgjB5Lj0z1ULZyAB3u5gJXs9TyyKVk4Dz_aWlk7a2oO0wIE3mRf-ugcVR5n317axfyNr_8CLeo6moq_9bCLi9zhQUiDTOFLjx4HVDDVjgN2BLZ7AHbxaLSGSnwv1lII0v-PYbVNK-trHCIBHq8BzmocwrWREN9huu87rY82auyuykDM8nsKRqkM8JsZchfLA30wIAEbrU07m39PoxOIzbqpsMHuguhfkGPTQ-1vvHwP3R_lu0GppZ9TOH64MUYwH_eMrJZipt96mGwb7Tsx49vOJFcWFwfuhlqoRlmAbi0aa4GXvQ5EpB95Wb3BAAVG31Z5eJkbLHr42fvmaGAsiRNNfJ0lmIN0LQYKkcbtxPOIDAIj3mO8k2t3w7Wp39FkLPvL3-zHfAhnLOTBOgdG9WzQDNZkctIPa6qBvOMuZ1x3DdQHydJ4HuWhz00X2rBApoqeBZ2ElV5MoZB5UiFzO2YX9TvQbS5OcQ8f0Vc3paNm3LRgWp4H3CzBaOEd_Q4xcrNIg_2SsxKv-m46nfNuPoHpXun4o33d9tOB-amgXhnO6j9Sihepgna8OnakjSRBdujq9NQCDP87tpb-E5cHa8qi4SUqWQ1SGR2BwifxsIay0B9IUMoC3VY5Ew-08fFEGpDIvlZf5RBy8JbUWDdlbr92aRKfFtGOM2OKS7CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم وایکینگ‌ها به بایرن‌مونیخ
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108596" target="_blank">📅 23:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108595">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بایرن‌مونیخ دومیوووووو خورد از وایکینگ
😐
😳</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/108595" target="_blank">📅 23:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108594">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/108594" target="_blank">📅 23:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108593">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
گل دوم مردودددددد شدددددددد</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108593" target="_blank">📅 23:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108592">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">صحنه رفته وار بررسی بشه</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/108592" target="_blank">📅 23:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108591">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کوووووون فلیک داره پاره میشههههههههه</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108591" target="_blank">📅 23:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108590">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گالاتاسرای دومیوووووووو زددددددددد</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/108590" target="_blank">📅 23:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108589">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/108589" target="_blank">📅 23:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108588">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a56bd8725.mp4?token=KitnzblSi9llbnT_b0mNah5_ucOk6sAhp_B08bga6hZdi98DKX1iQMhZrxfZljBk6qoFBVsvLTvOoWVAMdbVJy86-k9gtoZOZODd6vRx4ex3AG5MrMosCLVzG8hmK4ujR925brAErHJMdvDq2QiVYrrs_cxQ4Xiigybl1bz8Nft9JWn2IFzx6BLLplb-iQn36WuOAjH8woPnF0kWIxCG9nMMGIxwO_5nIypoErSGuGqLIfTKtauUzEWmCDi64Ts6JunX_CI045H8S9AEmkvvkJEogjEhdDeurdXmZhn2ge-GWM6KQsecxwQYgXF1T4diQph-igd5pc9YK9_pSGPMDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a56bd8725.mp4?token=KitnzblSi9llbnT_b0mNah5_ucOk6sAhp_B08bga6hZdi98DKX1iQMhZrxfZljBk6qoFBVsvLTvOoWVAMdbVJy86-k9gtoZOZODd6vRx4ex3AG5MrMosCLVzG8hmK4ujR925brAErHJMdvDq2QiVYrrs_cxQ4Xiigybl1bz8Nft9JWn2IFzx6BLLplb-iQn36WuOAjH8woPnF0kWIxCG9nMMGIxwO_5nIypoErSGuGqLIfTKtauUzEWmCDi64Ts6JunX_CI045H8S9AEmkvvkJEogjEhdDeurdXmZhn2ge-GWM6KQsecxwQYgXF1T4diQph-igd5pc9YK9_pSGPMDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇹🇷
گل اول گالاتاسرای به بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108588" target="_blank">📅 23:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108587">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گالاتاسرای زددددددددد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108587" target="_blank">📅 22:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108586">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گلگلگگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108586" target="_blank">📅 22:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108585">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">لیل یکی به آرسنال زد</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108585" target="_blank">📅 22:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108584">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">لیل یکی به آرسنال زد</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108584" target="_blank">📅 22:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108583">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گل‌اول وایکینگ به بایرن‌مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108583" target="_blank">📅 22:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108582">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee25b8b605.mp4?token=ABVA2KYxGZ9KKsS-tRz6q7cGrv850ued2ZxeEWLqgSs5Z33i5mRrdOTCAe7Ja8whCYmf-DUgLm-YaOwWWvjuOn-qUuSpA_KHRToTZULXUnmzmhCubGAJHWeF-8_rFGzTdGV1ZINkx98nMsc_sgn-lNDPDgWPH_J9-RrzK_2hgnA4FB0fpE1NmU_bEb8Q0ZZLlyrK5mSQCxR82si8caddagqL0_p_GHU9sxH7NkM4lV-PKh7OukGhxZI625El86su_y3d3LI9aLGlkVviVkbevzBO1EXIhCLVnLKFhh2ifWmkY6u61PbVrt8d2AraBjr8odZmWYPvNZNsvacux_TCEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee25b8b605.mp4?token=ABVA2KYxGZ9KKsS-tRz6q7cGrv850ued2ZxeEWLqgSs5Z33i5mRrdOTCAe7Ja8whCYmf-DUgLm-YaOwWWvjuOn-qUuSpA_KHRToTZULXUnmzmhCubGAJHWeF-8_rFGzTdGV1ZINkx98nMsc_sgn-lNDPDgWPH_J9-RrzK_2hgnA4FB0fpE1NmU_bEb8Q0ZZLlyrK5mSQCxR82si8caddagqL0_p_GHU9sxH7NkM4lV-PKh7OukGhxZI625El86su_y3d3LI9aLGlkVviVkbevzBO1EXIhCLVnLKFhh2ifWmkY6u61PbVrt8d2AraBjr8odZmWYPvNZNsvacux_TCEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
به نام خدا و گل؛ گل اول اتلتیکو مادرید به منچستر یونایتد توسط باریوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108582" target="_blank">📅 22:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108581">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گلگلگلگگلگلگل اتلتیکو یکی به یونایتد زدددد</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108581" target="_blank">📅 22:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108580">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بایرن‌مونیخ یکی از وایکینگ خورد</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108580" target="_blank">📅 22:33 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
