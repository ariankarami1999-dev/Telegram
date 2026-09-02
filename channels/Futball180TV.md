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
<img src="https://cdn5.telesco.pe/file/kVPcs8LmLfkXZhz0w2Rhq5r88gGNGhPVrfCaghVghIPdy4_ff_xCDpmWDmMC0ok7cHb5E6nA9kIE3kjSmwko865LzX-QcVtKzZ37yNp12sF_pU_noeJBh-rKqVf-kNyh3dPA5T5gL2A5vG372j9iQ8T35m2u2hGWybXHDimd-Bh1SHequrgRqmrcwVXhIG1yEy4I7rRpfXUHBq3JB-pW8da0ktfsABrlmn8y1R1LLfzkM2qdOr9OT7CLRg5bs8R409YmMao7Ur0ppIF09PYpcah353HadHwE5B4OttV2PJhw0svhDGn3jgdKammbAajyW1rX8aguS-yi4myA38prnw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 431K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 20:13:26</div>
<hr>

<div class="tg-post" id="msg-105368">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a8cd40ab6.mp4?token=aVr2PdyfSYaiyOe-VTppd-zvSbtVEJlo-GBPvfvRWzF1-dtItRAPlAumwUvErMpZE1yx-s01ZD723fHbpnBbncmErbMj1tKkPcJ14QUJPHD-kmxnrlTonZNkrasWeF6ELCWhVDhM6-omvByjKruXfZzMVQdBOVzfHYW3bL28Jhm39yGpA2qa3bPDeH2lA-ksjXnB4EdxqX9QLsjwr7xJriXETSkcmdiB4jf8M5fECNZRApSgaWmr3GsMz-84yKDDMA0kgbfxZEmitL28Lqg-X3bB9T8gvZwFXMfLBpUeWqC2NRkoxT7PAa0yZC9-r4eHUzI1GquXIQs6t-sh4Wjn3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a8cd40ab6.mp4?token=aVr2PdyfSYaiyOe-VTppd-zvSbtVEJlo-GBPvfvRWzF1-dtItRAPlAumwUvErMpZE1yx-s01ZD723fHbpnBbncmErbMj1tKkPcJ14QUJPHD-kmxnrlTonZNkrasWeF6ELCWhVDhM6-omvByjKruXfZzMVQdBOVzfHYW3bL28Jhm39yGpA2qa3bPDeH2lA-ksjXnB4EdxqX9QLsjwr7xJriXETSkcmdiB4jf8M5fECNZRApSgaWmr3GsMz-84yKDDMA0kgbfxZEmitL28Lqg-X3bB9T8gvZwFXMfLBpUeWqC2NRkoxT7PAa0yZC9-r4eHUzI1GquXIQs6t-sh4Wjn3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
موقعیت خطرناک یاسر‌آسانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 123 · <a href="https://t.me/Futball180TV/105368" target="_blank">📅 20:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105367">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a811272008.mp4?token=d_0YvEIH6yZYNXrmgUNF5sO0oAv9UvjB_pwYI0ZBbRFDbsIDw17HVMgEAtlLYTNc0JR92QxBKER592lvGv6uZx2j0Pv-jVQEq7-s4Z9J0dnBYwc8uNwsercFONrVFI5ijW0S3MhJxMuE9ItI6pinK0GcZnQ6HMoD4sbv5Co5fg0bdarqXDT2n_4JGoluwn_nsmHZfZ5-D9qaLSA3mXw9LQ7JpcSDnUVUW3hwV4q3folUT1agRg1s4Wj9ObFzXI2dqyJIPnwy6NTLAmTIb5Oqe5qtQRMpkhMFa2eAmtkve_9-Ta-930RsmPDixPaPxI97Er44n0CTPhVUg_8BOoDKnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a811272008.mp4?token=d_0YvEIH6yZYNXrmgUNF5sO0oAv9UvjB_pwYI0ZBbRFDbsIDw17HVMgEAtlLYTNc0JR92QxBKER592lvGv6uZx2j0Pv-jVQEq7-s4Z9J0dnBYwc8uNwsercFONrVFI5ijW0S3MhJxMuE9ItI6pinK0GcZnQ6HMoD4sbv5Co5fg0bdarqXDT2n_4JGoluwn_nsmHZfZ5-D9qaLSA3mXw9LQ7JpcSDnUVUW3hwV4q3folUT1agRg1s4Wj9ObFzXI2dqyJIPnwy6NTLAmTIb5Oqe5qtQRMpkhMFa2eAmtkve_9-Ta-930RsmPDixPaPxI97Er44n0CTPhVUg_8BOoDKnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
فرصت عالی علی علیپور به بیرون رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/Futball180TV/105367" target="_blank">📅 19:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105366">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a4f888f78.mp4?token=jmwlW1FinfdS3Tfhdhx1jKkmN-tjPhYDkoWRl_3DX6D-xD_7HtyW6xp5ws3RFkqnLbvYXrtmtpeM29i7OcL9WKD4NDhEjVTXKB4NovW1HyQsCa4FnkRpOWKKqADrQ5ZXrMKZcJleAHBj6nwXGSd7XpJ42HdmhUB9X-8mOtcqFk6GVSkb3fkCtdkyZ_ig-gySdk7aHJApchYM2htgIZu_gnMeCMvuGlKBfVcbR2mztOq8Ah0s5_EU-VSaTiE_6HaDCqgx87AK8YU7MvLqADE79fH_DQLLTL4Po0TN-yDO7ktXLSRad21UbWVtz2u2Y5FCfV2DO_BfHk5fJYtKr-fSbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a4f888f78.mp4?token=jmwlW1FinfdS3Tfhdhx1jKkmN-tjPhYDkoWRl_3DX6D-xD_7HtyW6xp5ws3RFkqnLbvYXrtmtpeM29i7OcL9WKD4NDhEjVTXKB4NovW1HyQsCa4FnkRpOWKKqADrQ5ZXrMKZcJleAHBj6nwXGSd7XpJ42HdmhUB9X-8mOtcqFk6GVSkb3fkCtdkyZ_ig-gySdk7aHJApchYM2htgIZu_gnMeCMvuGlKBfVcbR2mztOq8Ah0s5_EU-VSaTiE_6HaDCqgx87AK8YU7MvLqADE79fH_DQLLTL4Po0TN-yDO7ktXLSRad21UbWVtz2u2Y5FCfV2DO_BfHk5fJYtKr-fSbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
بهروز رهبری فرد: خیلی دوست داشتم که جلالی در این بازی باشد چون نقطه قوت استقلال همان سمت است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/105366" target="_blank">📅 19:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105365">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYmWye0K-mxnIW4gdetwwifNFQXA-Vv2EPar0R5ZRqppqfpNPYMMdrZjansSrawdwzFn1ZsdY8JmV5vuhWcDoXHNCWMASdDZG2nm3CdOw-wKG2uxp_G_37KsE10XsSUvb9MBGevjCoUHzNnXCi0kJHaiABp6hVTjGezsE19gpb5SjFHZ4H4VC9nV11OmRKFPkVi1yVSxLoNUirDB3-0w4CBUFCwDt5kpPk1EqzZIS2ZWsmxhmipPO_BSOUikdBydJr97SSzqgx_yyhy5s40aeosy9ESYi1MzIvOH8jUmigNqEoe0uXysejr3M2CQK1v31j9Q5IiFr1fBtXEB0TmKKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
ظاهرا جدید صالح‌حردانی در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/Futball180TV/105365" target="_blank">📅 19:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105364">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04c8c7c65b.mp4?token=WksoWu2kvJkmxXWTLeorOYl7mthhBdoJrjeQ5Qv2hoGX0J10YJnvVlaw4tRTMjZ6dxVmEXtmxDP1XVE1rjhhPOOSC-Q8YnMA4zs9m12-63ZC3J4ONk42pGMsMFq5sunfsj5inUN9kUiZbTqOpnFfJ6OfsDqSRKpSEz1qHFe1krb1FeVZ13Z0kLcjmaPVW2ootQCNoBCkxd9nHTBCgSWLG_ZOvFm-Nkb3-Jfd3jg0XinlTHsfVNc5_GcBznraRDuKV1Hr56PE2tuApDOYS0-WdWl4tm-RmvT7-1XOScbUW43xRqlSda9dxsalAEUmO19UqfY_mGKhKeSxsGRfNgW8tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04c8c7c65b.mp4?token=WksoWu2kvJkmxXWTLeorOYl7mthhBdoJrjeQ5Qv2hoGX0J10YJnvVlaw4tRTMjZ6dxVmEXtmxDP1XVE1rjhhPOOSC-Q8YnMA4zs9m12-63ZC3J4ONk42pGMsMFq5sunfsj5inUN9kUiZbTqOpnFfJ6OfsDqSRKpSEz1qHFe1krb1FeVZ13Z0kLcjmaPVW2ootQCNoBCkxd9nHTBCgSWLG_ZOvFm-Nkb3-Jfd3jg0XinlTHsfVNc5_GcBznraRDuKV1Hr56PE2tuApDOYS0-WdWl4tm-RmvT7-1XOScbUW43xRqlSda9dxsalAEUmO19UqfY_mGKhKeSxsGRfNgW8tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
😳
😳
به‌قرآن خاک کسخل‌خیزی داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/105364" target="_blank">📅 18:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105363">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da52ed6cf.mp4?token=ULOXbaXjAX7wEMOTSuqH8OOFVuTZOOztfbTEFJBEDIBTX_MXAJ42G8TUT4plEmYut5_luhDYxXTvReKyS4_7SJ8Ww1-7OqkAwfkrBwPY58oYCm8BvYrSR2EEvT2WAEl3612ZTXzwp2gQYw1Wl40vxVasHlwOAJ4atmsq13Uu7DNrphC8fY3nYAhgXk0mKbuOS53ZDLlZoQnPRY1RharkjBm94SHjK8_9kWaPA8-WAzvX3NWNixMqeN1OA3eZm9XglrOwfq4dflODeJxR12NmwQ5voTEbQza2yALagZVKt2pQP-rebxvaedG-T8dFJtJQBXJq0FGRGUjUvget27yEpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da52ed6cf.mp4?token=ULOXbaXjAX7wEMOTSuqH8OOFVuTZOOztfbTEFJBEDIBTX_MXAJ42G8TUT4plEmYut5_luhDYxXTvReKyS4_7SJ8Ww1-7OqkAwfkrBwPY58oYCm8BvYrSR2EEvT2WAEl3612ZTXzwp2gQYw1Wl40vxVasHlwOAJ4atmsq13Uu7DNrphC8fY3nYAhgXk0mKbuOS53ZDLlZoQnPRY1RharkjBm94SHjK8_9kWaPA8-WAzvX3NWNixMqeN1OA3eZm9XglrOwfq4dflODeJxR12NmwQ5voTEbQza2yALagZVKt2pQP-rebxvaedG-T8dFJtJQBXJq0FGRGUjUvget27yEpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
🇮🇷
🇮🇷
هوادار استقلال به سبک هوادار معروف غنایی در جام‌جهانی، با طلسم اژدها وارد ورزشگاه شده
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/105363" target="_blank">📅 18:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105362">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4866011c8d.mp4?token=bKmd6tpPFIeqObrYMaRUkRJ16yw_LmBrHLPQcH5EKu873v9UJUt0CVxyVSW9Z-xafEMYnGMpcGc3bwyDeNsQgNGyYaoqTCVqmk9q1IqO9FQwzupqyAKK9iyDjpaOHUW3FZs7NpC_5Ak9CuDRv_9exUPWydeqHNy_pGvwUTPzwz_R0jQ3XNAwQq0jHl3zK6hHK6lqTlA5i4ZwnQcBdfiosZMsL3o1llTVtbYISbAGaRgUGfbHtExxj7LaBZuqMeNgQ6USsLfa02nc7JA4rold0aDiivN_SgqCfqVzdL5oUjX2w293Aeg-eGtsntc2vP-RSUhklxq_UGbLjHSPnDq1AnZI6uA1Lz-BPZ2dnGodoYpzdiie7VodpOkWA83744XQrP1_CViIIJsnu3UXBZ_qnOUnioJ1ruWlAu18pQMUdjGC4F0KSLDbWrMH2MavYyAPDENHCrNo9IREY-5tjQDd0GejsSRrefg2c34pkRHqXSf1rmS15ZjsdKOywYDmsJlYVMyMVaWs_d2T2qPErLO7coDmkc2t1waJ7q2eeqkDpDGwL4_yJPyIdiJnCOOFGk3xLkZVQNqI_knWwml5Z9H94h7SK4fJXrL__NgYF38SVmDnLhYLziVcvwthNmbCc3ON_TXoOFhx3kJwXupqIM-HqnhMpOpmfIn3bq34lxPIrbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4866011c8d.mp4?token=bKmd6tpPFIeqObrYMaRUkRJ16yw_LmBrHLPQcH5EKu873v9UJUt0CVxyVSW9Z-xafEMYnGMpcGc3bwyDeNsQgNGyYaoqTCVqmk9q1IqO9FQwzupqyAKK9iyDjpaOHUW3FZs7NpC_5Ak9CuDRv_9exUPWydeqHNy_pGvwUTPzwz_R0jQ3XNAwQq0jHl3zK6hHK6lqTlA5i4ZwnQcBdfiosZMsL3o1llTVtbYISbAGaRgUGfbHtExxj7LaBZuqMeNgQ6USsLfa02nc7JA4rold0aDiivN_SgqCfqVzdL5oUjX2w293Aeg-eGtsntc2vP-RSUhklxq_UGbLjHSPnDq1AnZI6uA1Lz-BPZ2dnGodoYpzdiie7VodpOkWA83744XQrP1_CViIIJsnu3UXBZ_qnOUnioJ1ruWlAu18pQMUdjGC4F0KSLDbWrMH2MavYyAPDENHCrNo9IREY-5tjQDd0GejsSRrefg2c34pkRHqXSf1rmS15ZjsdKOywYDmsJlYVMyMVaWs_d2T2qPErLO7coDmkc2t1waJ7q2eeqkDpDGwL4_yJPyIdiJnCOOFGk3xLkZVQNqI_knWwml5Z9H94h7SK4fJXrL__NgYF38SVmDnLhYLziVcvwthNmbCc3ON_TXoOFhx3kJwXupqIM-HqnhMpOpmfIn3bq34lxPIrbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
شباهت گل‌های این فصل دو تیم به گل‌های به یاد ماندنی داربی‌های گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/105362" target="_blank">📅 18:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105361">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1BdJeHVit_MMNSkJvIQGrZE-Jrf0mwAGvGKnHkSBqDhwsZqD_hFS6y1bG6smQPgKA0aWc2e3O58BFSKOM-xdzNNzCo9tPnLQSE2gSzOI0vXl_EEZlh5qZSY4vJmC_4LX36J4fD8hF_-lF-MtmSLc5FL8O_DE_roMy4bCCwWpFeEdaCAMkXhze0pKv4m7vT2ugQlOIbrqSbDKrI1tUdMqhLvDI__RfFOqZjvYwTq3pscwexQgg_jxH2iCBE6QXLAYRv_rjLbnf6P7xo3pdAEmCh6tCuD8rCHMv2gm2m7Cs8IKM3Zwo4c6lGgt7L2WAIRtvF-CWcs_QySxVyQbkdxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇮🇷
🇮🇷
لیست‌کامل بازی امشب دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/105361" target="_blank">📅 18:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105360">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e961f8ed7f.mp4?token=hoQ0fs7sXu4MGZwfUyIJnWQQCrN1dHt495z2Ner93mq3vbMD6dkh-ZFbxM8y4oLv3PRN7H4zpKArK2aGKZD0prYAU72rr3Hl-_JK8EFtxnDe3K05Dkkzo6PGfLlw8_RQZe56i5SUpzYOaFWPMefwkkkebSwu9iVx-UqfyzmYPtJUfOVDoiChZOOp3WFrHVdj5vFhmfbsw0iNCWWJ_eQF4V49YHM54PtRt_hkzRBRUPzKw55Tz9iWw9cZzi6MWcLqMvdO3RZ_AWeL3MSmZG1LtqVT5G9fH1Ur95MzRetg7C7VZNr0mrphnXnVgZsZMJpRqlN2Ei79OvdenillDKXkmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e961f8ed7f.mp4?token=hoQ0fs7sXu4MGZwfUyIJnWQQCrN1dHt495z2Ner93mq3vbMD6dkh-ZFbxM8y4oLv3PRN7H4zpKArK2aGKZD0prYAU72rr3Hl-_JK8EFtxnDe3K05Dkkzo6PGfLlw8_RQZe56i5SUpzYOaFWPMefwkkkebSwu9iVx-UqfyzmYPtJUfOVDoiChZOOp3WFrHVdj5vFhmfbsw0iNCWWJ_eQF4V49YHM54PtRt_hkzRBRUPzKw55Tz9iWw9cZzi6MWcLqMvdO3RZ_AWeL3MSmZG1LtqVT5G9fH1Ur95MzRetg7C7VZNr0mrphnXnVgZsZMJpRqlN2Ei79OvdenillDKXkmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
🇮🇷
یاسر آسانی رو به هواداران پرسپولیس کری‌خوانی را آغاز کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/105360" target="_blank">📅 18:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105359">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d420dd3220.mp4?token=vwWNC-SCaYTx5upRzpNgxffsiBh6LLEIlcgnwDkC5sDE5J2pTBMFOlmzxkBP0kRSEUoUbMuYCwlQXiXalH8Yp6-BGgOcT52TjdfwWqBIYz9X2-Kk6Gbfc7F2pg7__wbgOea9brYdSMeU1G6VyuP_PfcVH4uV6sz3if2Cmw50-07kyjDpuCxFy441Fedb2ATB3cEHp1inWKBtscv_YndSTU1LzQaa_8xVbTqRCx3TsBDRjYomTWXWlii58JiVZH8vy7erTuky0ONZEAhL8nI10ENIa6ESlwN7Ox38F6kJzf2V8YpvVv1ukiofuSIkci08EznTiDwcm_R21f3un5DXwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d420dd3220.mp4?token=vwWNC-SCaYTx5upRzpNgxffsiBh6LLEIlcgnwDkC5sDE5J2pTBMFOlmzxkBP0kRSEUoUbMuYCwlQXiXalH8Yp6-BGgOcT52TjdfwWqBIYz9X2-Kk6Gbfc7F2pg7__wbgOea9brYdSMeU1G6VyuP_PfcVH4uV6sz3if2Cmw50-07kyjDpuCxFy441Fedb2ATB3cEHp1inWKBtscv_YndSTU1LzQaa_8xVbTqRCx3TsBDRjYomTWXWlii58JiVZH8vy7erTuky0ONZEAhL8nI10ENIa6ESlwN7Ox38F6kJzf2V8YpvVv1ukiofuSIkci08EznTiDwcm_R21f3un5DXwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
سیروس دین محمدی: قبلا اگر مساوی می شد حداقل ما همدیگر را در زمین می زدیم جذاب می شد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/105359" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105358">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8LRbzLwVRZJkb7Y6uTwv-5IdQgJ5EY7heRrtsqVEesGHJPu9QKmiLwDBzWsTSB6I0vLVkKzsVtjTAJkDt0PHSFDm3KJkOImqJD143pA6hmGFMd6eIlZQ4VjGjtEQ-w1Uo4nGX7lmgPmFR47-JDupbj3kAE518z7VPRNI62NVkuoE55U5EzNaAEb6MXovXqr2wnellXG_QNzgQldPk-UoMOn7Kgu1bAPhTgSaGmQB_DrKElA-b2KqjzzojJdOw_HgQKOvDxXw17KpPa2uRQUCp03yWiCo5coi8oP60cM-ZYg7eNb757UH41uii_Jh7DTC9IIrtBr5jUG6yRZLQcC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
مقایسه نتایج سرخابی‌ها در دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/105358" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105357">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105357" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/105357" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105356">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-hrujK9eBUyA87Grklk8MlV1FnvnVFaVlziulZCyLUxYMVC_WwovSne8jwxhUH7UYRHwIYVHoGzuLv49U8E_aUFduS_MBLLeFv5fXNTu3nqwiliBZPJjLt9Uqiyeg6UugNfAMk9_gIxsoM8fNOMmxdbB3EyXqvtOopTXKrVdYxk1kVSHv49XaCjERTFtyM7lOyf-7EoEkAO0PpWcyVjU28ORGXC8fr0F8kg6fB50a_pF0tnQL225jLtUwTsyRfKiF8adUyxxJcVirNy1toMsvByMfBEYF3IYYd2Tx2JOSiVPmF3uf_OcpbAzpZuG1DewGAgrFc0vTz-J7ebOvErPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
استقلال
🆚
پرسپولیس
⚽️
پیش‌بینی دربی رو در
TrexBet
از دست نده!
📉
نگاهی به 5 دربی اخیر:
2 برد پرسپولیس | 0 برد استقلال | 3 مساوی
4 گل پرسپولیس | 2 گل استقلال
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/105356" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105355">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iC07juO-wf-7AgvZ-9fpaipnfXzHSROuz3WV-7HKxCAHOf0I7ZySUkP-PsjPCCsCXMTzbF3lOYD5vddcbXSJL_lR1_KaY0kXFQhD_rzWVACd00b6E7zUAill1f1_3YZwK_iYuFyhcjVKGWBQF1w4xTUGuDVi5K3l7qRQMS-249FywiNN4FvR6cQMqRs_6qG22gVYfFYu1ySPwVSBQ0KS_OWSeSvN-mdxQfahNeSWbrH1Ivqq_tQzf2w_4acU3Dac90Q4NODeBo4XesxR185RDu387xi3xwc5-74fTLEH0qKBNiNQSFrk3vFFi5Z9T4-gJHFWT6o94RKhvTHMoPcTyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب پرسپولیس مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/105355" target="_blank">📅 18:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105354">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbrUjZqRE6K8PXf7IdU0EYd8LZxaFQv7gfdNSoO3o_2gXu7G68ReIIL-bAW6ZS3Qcfv74I8xABCYOA9mf2O3gPtTcY17Zog12dJmQifSqKYV5_ieXTuEruZZIhZ9InafT9ICHjriT_HrUL2Y1_lwVKwQ4HAX-_9F3AFQB3QmS8PsYBfmynGTJk8p-D7aeSsW2sElqII79d61yKP-yrRTvQyakn162bm3j8-A4U86ZUMb6_WLi4uOFDf8OaKVk7EwcVKrtOiVsTGYvHVtgcnWXSk58z4FXt3Ql0SqgTNjqzHvkk8prFcRi-qU3FOpaXIe2VWKywiWX4_4HbnrK2RWtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب پرسپولیس مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/105354" target="_blank">📅 18:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105353">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nisZeuDhLadDZZlqHG042_ESm3unRMS-iwgQWyjhduWRigZouPoHfz6ZbhIWYboHJafBWp8yXGRlPwaTySQa6RlMtl3-qfz6Zy-YdwynHdgG-OSK6l6P4JQl51GLY0aTRLn64H3zIaHU24d_h7jvmjpRpXRzGkGmTiAnew39kGtkYbMEQysPWMEb_6WFnYof78H8OwFrCZLPIbux57DWqy0XpyX7cgNYOwnLNoAhhmXdaI2EV2W09sOYRanFZ-ywks2CgXT-XhgQKPjstIsxx_Rd_wzt4C1sStMrX4bSgXiiZaCvi0wyYvKP4Jlc4IALwpZE_jVo9YAusv27M0tfXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب استقلال مقابل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/105353" target="_blank">📅 18:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105352">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HScihtSH_gyvMudnnr9bw61FDbx0juIG2YAeSBReDcSMNkM4qx6CBQG4Helh9AJ9RfLH0VNXIGqGG1Xkv4_qkNejACTuDXhGr8Xa7kTcYBO3-uS8I889_WBc13cjXCODfhTGW4XkX_8a0d8Vm238fBgmdPcvCNNLjxAl-oYYy3-SHI3VF94SSdJwvT6vFrrwVwqYlDTW0nvGLcY22vlbBMdT0mHOUPp-T-KN25EaZDHAjM7_qghmwvpJW6xFyIMNYoPVCre_sKGQM02sI9FhNPs2N0XQ_75_k0ih-xfVSh0RmPVPhjlO43IILFWWSH6eteR3-xcJfSc4ubsVrLJXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب استقلال مقابل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/105352" target="_blank">📅 18:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105351">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a83d7c6e.mp4?token=PGwKau2WILkPNOQ877YlDUrNVmPMEk4EwMH7m8fyFU1Q5jLSf-CoaMCmDTv_5ujsy4J9ebMPWFjVpOKUxBIG4htuSnH3OxQs672xxkjzGbCymttAsVsj8dTgXp9GfJ0whbrKHS8H1Z25xRkuJbS54UYW4RbKFMb3uUqVmUEID8QH2DxPyVYH2ofr2oZ506HyN25IQGjOioj_98wdPJ1RyMOrspyuZE3R9v6kFnsEgHEsFK13vzWBzRirJ1OK5HPYYUn6fEigKGyhqwKmqli1tt0qfECtLtFV8udgNULPCf3k0KyPm9aYFmZk5xCd_dMQuKuCU1Aw9MR77CHubwV7Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a83d7c6e.mp4?token=PGwKau2WILkPNOQ877YlDUrNVmPMEk4EwMH7m8fyFU1Q5jLSf-CoaMCmDTv_5ujsy4J9ebMPWFjVpOKUxBIG4htuSnH3OxQs672xxkjzGbCymttAsVsj8dTgXp9GfJ0whbrKHS8H1Z25xRkuJbS54UYW4RbKFMb3uUqVmUEID8QH2DxPyVYH2ofr2oZ506HyN25IQGjOioj_98wdPJ1RyMOrspyuZE3R9v6kFnsEgHEsFK13vzWBzRirJ1OK5HPYYUn6fEigKGyhqwKmqli1tt0qfECtLtFV8udgNULPCf3k0KyPm9aYFmZk5xCd_dMQuKuCU1Aw9MR77CHubwV7Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
😳
ترمیم‌ناخن‌های علیپور در آستانه دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/105351" target="_blank">📅 18:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105350">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9531a98f1.mp4?token=a_4JKuT4EkXBg_KOEk-bASA5mp1A1bPjJVFwXINpFbwAMU0ypP8aIC49O1VGd3KLvLmXlWC1PQyWEi6Szo-VkkuTDFC3buU7uqXoz4_e8gczR58QAOwljTya78hc2OtNZ2Yss7AfDb8BVJ4n8WPAILEsIngdA4KJPk_jH1R3vMbsyRD6nQiG49KC0ShKBbIzr6k430MYu16q6VmFL4kKDovH4CTLHlTFDFhDlM1h8xRxD5E-KDitcCZDTPeb4_vSrI_yEdvQFEVHpzhXM3-awz5cXM5dpjU2Q6UnMtoVz_EkBYQyIwhfWdjmAe9JYzISGWnf2WqplQpwaLg3zlMIHx00gVlnpVwpFcDdOLA4eaYIQZ2n_y9WjKAxrxBQcmcnEP1-BqVCFqqGEJJvQUusyjVLMmzVQlECqw9-NqvxGuK2XgvkZJKDPTvbDB68oVPNEAFx1hPlT2Smp3lFk1atwx9Jvlekg2gqtbdBwAI4RXMVgLhSSUf8MrpVO4mtx8mlX0DufYteuoWwvPkQo9YblDgWvYJ1dHAJL2wAxhLcfgZGb1mdDyzbvL02NcXqsfmc9_B8xLYWIzX5gy9ynyde4HZnXZr3Bp8RfVAub_-EfRByTqNgOCz387_iWNFJNf9RWfUjg9m_AROXowzEm1G15BiwSikyTz1LZYRpOSZYdRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9531a98f1.mp4?token=a_4JKuT4EkXBg_KOEk-bASA5mp1A1bPjJVFwXINpFbwAMU0ypP8aIC49O1VGd3KLvLmXlWC1PQyWEi6Szo-VkkuTDFC3buU7uqXoz4_e8gczR58QAOwljTya78hc2OtNZ2Yss7AfDb8BVJ4n8WPAILEsIngdA4KJPk_jH1R3vMbsyRD6nQiG49KC0ShKBbIzr6k430MYu16q6VmFL4kKDovH4CTLHlTFDFhDlM1h8xRxD5E-KDitcCZDTPeb4_vSrI_yEdvQFEVHpzhXM3-awz5cXM5dpjU2Q6UnMtoVz_EkBYQyIwhfWdjmAe9JYzISGWnf2WqplQpwaLg3zlMIHx00gVlnpVwpFcDdOLA4eaYIQZ2n_y9WjKAxrxBQcmcnEP1-BqVCFqqGEJJvQUusyjVLMmzVQlECqw9-NqvxGuK2XgvkZJKDPTvbDB68oVPNEAFx1hPlT2Smp3lFk1atwx9Jvlekg2gqtbdBwAI4RXMVgLhSSUf8MrpVO4mtx8mlX0DufYteuoWwvPkQo9YblDgWvYJ1dHAJL2wAxhLcfgZGb1mdDyzbvL02NcXqsfmc9_B8xLYWIzX5gy9ynyde4HZnXZr3Bp8RfVAub_-EfRByTqNgOCz387_iWNFJNf9RWfUjg9m_AROXowzEm1G15BiwSikyTz1LZYRpOSZYdRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
کری‌خوانی بازیکن اسبق پرسپولیس برای امیرحسین صادقی: آخرین باری که استقلال دربی را برد، دلار ۴ هزار تومان بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/105350" target="_blank">📅 18:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105349">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a801f0de.mp4?token=tz2Cdqw3Od6Ymj0cwJk1pp3aVVCyW0qNWI77MInITv751DpuFiaP6l6_PIP9bclqPebtrmW3LUUK8Y5Vgslt8exkIytWgPxzpWt-_NeRfscf9Q5Fy614qK2WM4iY5ghwsKVstNvbRy4jgw6kZRXinxaEhA_LmY9g3eiFbhsn7_7yjtcOl6uK-Wd0d1R5IldtKuC8zyO2E4pEGUC3tou_AJsNuQKbKJLINRQGnD09rq6f6Pn3VPQOoAqel_B80K-q0bPYnijhFBegBdn0KXCWAVpRzCVOdVfNd7IuGi96uOe3mmlNe41MRjbV5DogGuP7AWtHXbLD_mZK_kIFEWfzdC_A-ZWfPW3qHSK7i-ygEKMEwpV0T2FiVZzmra18qBCIF6PrSSGMlemGEhQZ4pHgztUUIhwrwm6VrstepnpoHxmrdJnQiVqgoV9uYk0zDrm6Y3tA95PzJGnWYrCK6iyHS18albVv9cNuOJm05fVagZ07pIo8vXDt_czgdFl2SRgOOJBBiQkTSPo1ytTyaW3wsBydhO-XOQARYkCesDRiubHcJ-DkR2IwzB503qi0HP64xgko6BuApTh7l0BlAo9wXY21wpTAhFCPgHaSUuaYK6NH_IThIHVEHc5uhqAkiVufeAVYJr0Z9u4xKnKJmKzZ1VMEwKsqNem2LcgRXlCK3no" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a801f0de.mp4?token=tz2Cdqw3Od6Ymj0cwJk1pp3aVVCyW0qNWI77MInITv751DpuFiaP6l6_PIP9bclqPebtrmW3LUUK8Y5Vgslt8exkIytWgPxzpWt-_NeRfscf9Q5Fy614qK2WM4iY5ghwsKVstNvbRy4jgw6kZRXinxaEhA_LmY9g3eiFbhsn7_7yjtcOl6uK-Wd0d1R5IldtKuC8zyO2E4pEGUC3tou_AJsNuQKbKJLINRQGnD09rq6f6Pn3VPQOoAqel_B80K-q0bPYnijhFBegBdn0KXCWAVpRzCVOdVfNd7IuGi96uOe3mmlNe41MRjbV5DogGuP7AWtHXbLD_mZK_kIFEWfzdC_A-ZWfPW3qHSK7i-ygEKMEwpV0T2FiVZzmra18qBCIF6PrSSGMlemGEhQZ4pHgztUUIhwrwm6VrstepnpoHxmrdJnQiVqgoV9uYk0zDrm6Y3tA95PzJGnWYrCK6iyHS18albVv9cNuOJm05fVagZ07pIo8vXDt_czgdFl2SRgOOJBBiQkTSPo1ytTyaW3wsBydhO-XOQARYkCesDRiubHcJ-DkR2IwzB503qi0HP64xgko6BuApTh7l0BlAo9wXY21wpTAhFCPgHaSUuaYK6NH_IThIHVEHc5uhqAkiVufeAVYJr0Z9u4xKnKJmKzZ1VMEwKsqNem2LcgRXlCK3no" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
هوادار پرسپولیسی خطاب به استقلال: دربی اصلی ما با پیکانه، شما ده سال مارو نبردید
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/105349" target="_blank">📅 17:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105348">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2dc5b376.mp4?token=q4hnUw91OUXVWjvykDXaQwr14Y7kuvqhMgHwZzXUFNTNs8QklEnE8L4_KanzpRDNNglkEvLsjlQGSQpPYM3rK3rf1os539DImV5cFQGwBh6GvgM5yY9mFLozUd5wX9kTYW2u717YmQuckRdznrB0H-zEIsjNfvxTuHGrc0O_xjV9VRPod3QQAxVSm3B5LN8_FpzjAGzxLO1L0uUP__8TKOds_9wtBpky3QwlZNEisPwVDqiwRqBHpitm9T5WHLnEHFA4cRLWaxZ0Ft-REiGuNsOhqqLKxw63YSM35ptSrXjkURDQ0ImhvIprVJX9CXnxZUqtYxdOV5JFzt96vO1NDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2dc5b376.mp4?token=q4hnUw91OUXVWjvykDXaQwr14Y7kuvqhMgHwZzXUFNTNs8QklEnE8L4_KanzpRDNNglkEvLsjlQGSQpPYM3rK3rf1os539DImV5cFQGwBh6GvgM5yY9mFLozUd5wX9kTYW2u717YmQuckRdznrB0H-zEIsjNfvxTuHGrc0O_xjV9VRPod3QQAxVSm3B5LN8_FpzjAGzxLO1L0uUP__8TKOds_9wtBpky3QwlZNEisPwVDqiwRqBHpitm9T5WHLnEHFA4cRLWaxZ0Ft-REiGuNsOhqqLKxw63YSM35ptSrXjkURDQ0ImhvIprVJX9CXnxZUqtYxdOV5JFzt96vO1NDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
کری‌خوانی هواداران کودک استقلال برای پرسپولیس: ما با پرسپولیس کری و دعوایی نداریم؛ پاس رفت آسیا قهرمان شد اما شما نشدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/105348" target="_blank">📅 17:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105347">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4634665f37.mp4?token=Ypt8xhLYE6NDAk_b2j98Oxe0VElxQktWHPG4Zm2ZYEff2b9UI0JPlA02FGJnBF-D5Kj3BAN7eA9TFuATexg5SDEiSR7lz4uGnvohmoqRdlQLdPD8S6JaEqt0vqsqdoSAjUjSDPiUsm6P0-8VCs0eN1oN0j4fDx-sZBHJZA1dnwZ7sh8vHy7A7tqRTxj7iZBtKfCKQkGJDi1qXv1pKzbJ_pTCeiDUb0zlg_pKPBpUKaDwT946tghgWlH2jerOBzvT6mPQa18y-F1bVMDtTPAa7GvM1k3-ysrbZHn2DVl3bb3Bsl6c2fweN538Xor8uGsj5tmWymx_vTgLkK87YlKMmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4634665f37.mp4?token=Ypt8xhLYE6NDAk_b2j98Oxe0VElxQktWHPG4Zm2ZYEff2b9UI0JPlA02FGJnBF-D5Kj3BAN7eA9TFuATexg5SDEiSR7lz4uGnvohmoqRdlQLdPD8S6JaEqt0vqsqdoSAjUjSDPiUsm6P0-8VCs0eN1oN0j4fDx-sZBHJZA1dnwZ7sh8vHy7A7tqRTxj7iZBtKfCKQkGJDi1qXv1pKzbJ_pTCeiDUb0zlg_pKPBpUKaDwT946tghgWlH2jerOBzvT6mPQa18y-F1bVMDtTPAa7GvM1k3-ysrbZHn2DVl3bb3Bsl6c2fweN538Xor8uGsj5tmWymx_vTgLkK87YlKMmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
🔥
نمایی از ورزشگاه نقش‌جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/105347" target="_blank">📅 17:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105346">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1699b2c157.mp4?token=hst-60FZEEDXcFE40o3aSv3j8hbf-FBc7ArZah1DZah4NZVZjaKEdZftZo_OiMkXmqZR9gXFaKWJ_y0pIEZDTw8e0S2NwYtrYLsEiwrDF55Nt_NlNjMeTbaYb8NRcYmA_0UeqtJJsheG_rR7FoclQ182VY-CHYI8iGG59Tz1qtwNqM32zlK9vSXEnsqj7RlhKW202KbCOFTojNDBYhL3c7Lo1mNyjKUJo8sjo-aQq6luYYls1fe5V5hQSrV5bUOi7aq_TSxhL9Ek9gxez1GG-w3Jr1bQOmR2Ckl4oGbExS4GZzsKAcnyqVBK9hBcLouHvopMdFFSk7ZD3Si_SnfIcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1699b2c157.mp4?token=hst-60FZEEDXcFE40o3aSv3j8hbf-FBc7ArZah1DZah4NZVZjaKEdZftZo_OiMkXmqZR9gXFaKWJ_y0pIEZDTw8e0S2NwYtrYLsEiwrDF55Nt_NlNjMeTbaYb8NRcYmA_0UeqtJJsheG_rR7FoclQ182VY-CHYI8iGG59Tz1qtwNqM32zlK9vSXEnsqj7RlhKW202KbCOFTojNDBYhL3c7Lo1mNyjKUJo8sjo-aQq6luYYls1fe5V5hQSrV5bUOi7aq_TSxhL9Ek9gxez1GG-w3Jr1bQOmR2Ckl4oGbExS4GZzsKAcnyqVBK9hBcLouHvopMdFFSk7ZD3Si_SnfIcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کری خوانی هواداران زن دو تیم پیش از دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/105346" target="_blank">📅 17:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105345">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef377348e.mp4?token=tE5l0Eke0Hmxm_p6fAUsAwnvOR_j1uN9Tl7Kp5XAbwD16BnC9JYNuYzrgE5sErkjorc-YnMyxGMYTsndArn7Ema43dF-d1HBdAP2Zhxgs0RbqQLHm4Ty77pJkf__TejuESqmQEgsft9DcBv5JeDhMTAV0lmeHze8L91bvUcBXEM0KbnLrndO6ZAugwdhblilR0bOJG7hmIs3nRgQOZLTi1jzanCMGv72XGGRiNGnfVV4zYOpfvg1OSNKDbFNt8uouDmfupFmPRKNY5r9XEtNv3KhThCsQAbPyvVmubfYHTszWItTxf1gfc4gTb2KEyrdcwq5Kt_9ujl_Z34i-iOFkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef377348e.mp4?token=tE5l0Eke0Hmxm_p6fAUsAwnvOR_j1uN9Tl7Kp5XAbwD16BnC9JYNuYzrgE5sErkjorc-YnMyxGMYTsndArn7Ema43dF-d1HBdAP2Zhxgs0RbqQLHm4Ty77pJkf__TejuESqmQEgsft9DcBv5JeDhMTAV0lmeHze8L91bvUcBXEM0KbnLrndO6ZAugwdhblilR0bOJG7hmIs3nRgQOZLTi1jzanCMGv72XGGRiNGnfVV4zYOpfvg1OSNKDbFNt8uouDmfupFmPRKNY5r9XEtNv3KhThCsQAbPyvVmubfYHTszWItTxf1gfc4gTb2KEyrdcwq5Kt_9ujl_Z34i-iOFkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔥
و بالاخره جانشینان رودری معرفی شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105345" target="_blank">📅 16:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105344">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boeiFEgPKMlwA9DANSZvr6_sjj71zqA9jk3w0M4dDjlUjTP0eqVEHedKpZBfhqYbJWTXXrnFTE9btC0asAPje3HBk6ghmmpFFKUYy-WYZIPguonXoQW_wmi8OW5oqi-3A2Ax_DdypQHX3RsvZeMn7UITEDxWuqnmWp98TwwGIF1nm5eCC5umkEP0TAiHgbczGcFYpEfAzvATbbJ9vCu3KPbFueJShazXvw5pTY_WXN0iQWTyFwwwz4YdljxbcsgqEVYGrTGLyl5J9-lUhDSJ7YD8JmBgB1W5Q02UDy9Z8QqLewhj9odjtqc6yqnySdAiGjeH2UUVlwujjpfSu1d9FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: انزو فرناندز از چلسی به منچسترسیتی با رقم ۱۲۵ میلیون پوند
🤯
🤯
🤯
HERE WE GO
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105344" target="_blank">📅 16:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105343">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1Gg_3zuUVYPhyJLO56bASaZivXixyxJAvD5VN8GhuzgzjrCBexUaJBTppyyD1WVGsknjF3dt17mbkW8F9fixzqehLprdRxcgYn0SCRfMM47oAaLAdKnqh51c7-yvxvXt7q1jsKUK7dNn4FLD0qOYFM8fzKXgDe5e-mW8GRVd47DaLxSnv0HNi-0_klLDzYM3eduGQOsS8W4ONBrRmXZcZ1G8jcJO1crX0XtC3EUIeds1izGj3huF4d2mgQP6MMW_H2hjOOd54ax_4vFRk9wrn27xosIxoB8sFdURTkb1nRajLniidPNrGvLuGH68p-6PxsagF28JCx9jOXYyinCmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
مقایسه سن ترکیب اصلی رئال و بارسا؛ تیم فلیک فقط یه بازیکن متولد دهه نود داره
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105343" target="_blank">📅 16:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105342">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91b6a8d69.mp4?token=E7jW2gnEgMq2eJTjS9JMHhCW5fwp3gd4NeBMju1BW_5VATx2oE9QKtzuUuQUOfYQQ4rWNYO_bIHSBObVA7UF4uSz5BKNeAbiCepzt1_Ova33cQm-79Ua6_LKjeF8oBPpZWxRUz6BwMRPTKBywA2ConPBr2h-28pZzPnKbzXdX-CwmHMe6ZwM-TNqtb99dWwDyygnHoagPOn2rWeNRj2uVzh1boz0tFugr7SdjgefTVYgZpymbqV5mGIX9E7NwucL8bYK-qriyA8G88U-ebo7o7GI2G6OQhHrJGHYkFYHQxLmpESfJeYrZCtS5ubQGm1tbEQ68by6UHOoM-sg9ruJBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91b6a8d69.mp4?token=E7jW2gnEgMq2eJTjS9JMHhCW5fwp3gd4NeBMju1BW_5VATx2oE9QKtzuUuQUOfYQQ4rWNYO_bIHSBObVA7UF4uSz5BKNeAbiCepzt1_Ova33cQm-79Ua6_LKjeF8oBPpZWxRUz6BwMRPTKBywA2ConPBr2h-28pZzPnKbzXdX-CwmHMe6ZwM-TNqtb99dWwDyygnHoagPOn2rWeNRj2uVzh1boz0tFugr7SdjgefTVYgZpymbqV5mGIX9E7NwucL8bYK-qriyA8G88U-ebo7o7GI2G6OQhHrJGHYkFYHQxLmpESfJeYrZCtS5ubQGm1tbEQ68by6UHOoM-sg9ruJBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظ لئو. خداحافظ تا تولد یک اعجوبه دیگر در آرژانتین.
🩵
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105342" target="_blank">📅 15:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105341">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9af28d1f54.mp4?token=o5YiHAqfvXjtNhCfPWyTzijVwJYGckT6facBIf77RpPoGTvAw2oFyfg1W-6iJJ4koZavmpqgqS1cp3bYvj6m_UpFuVxg5xMM7ZKJVAJ2cCOiR1prj-_f9ur4SI6agJUW6mzFgcmpsZSk7jx8iUvgq-CHYCr54qKy5b64iZLD3pX408piNPebNjo3xssB0kJCGMxQc_FSlg1RH3OCv2e_QG2oaZX7l9PkF8qelru2KFH8mz6gmAolgXohG8vOYCHy43SzTbRx7XKmR8Zch8Pijn3FxO67f3ijcUvhewrUHL9Juuom1DXGVlQ3Qe7VJuQ2F29HDSAUfzSQ2SwZ_FcdoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9af28d1f54.mp4?token=o5YiHAqfvXjtNhCfPWyTzijVwJYGckT6facBIf77RpPoGTvAw2oFyfg1W-6iJJ4koZavmpqgqS1cp3bYvj6m_UpFuVxg5xMM7ZKJVAJ2cCOiR1prj-_f9ur4SI6agJUW6mzFgcmpsZSk7jx8iUvgq-CHYCr54qKy5b64iZLD3pX408piNPebNjo3xssB0kJCGMxQc_FSlg1RH3OCv2e_QG2oaZX7l9PkF8qelru2KFH8mz6gmAolgXohG8vOYCHy43SzTbRx7XKmR8Zch8Pijn3FxO67f3ijcUvhewrUHL9Juuom1DXGVlQ3Qe7VJuQ2F29HDSAUfzSQ2SwZ_FcdoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇮🇷
🇮🇷
دربی فقط یک بازی نیست…
⚔️
یه حسه، یه خاطره‌ست، یه جنگ برای افتخاره.
🔥
۹۰ دقیقه‌ای که هیچ‌کس نمی‌تونه نسبت بهش بی‌تفاوت باشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105341" target="_blank">📅 15:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105340">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3a4e2ac35.mp4?token=U9RpxwCgR0pAdyx008LJyhEiqxvowpx06FbqmyZVlnbB5VJZbBvZ-syazBY8oTNSEVf5wHj8-sC2Zb1c9_1uG7oIY3afv-4Y7K2TVHZniACJflfdf2TFkcqJzV7P0iJ8qOjZZXx0GuGnNuBHQjsx9cXjGHkwTJy67rCWXd8diOKaPQIjYvgexnwHBjZCQvXwXs4PIZH20PZy4RCZTCJ36LaNH_ccJ_xFyFcOolqexi5ckIGvD5hNhz5FnKWFd4MOu9UL2xCz0Jx-Zpo8_VPzIs_9e5CBT71cICI044_fkQHVtcqgzjnXddFkDrXOT1SbIaAJnk2wiH5VsbYtDA9OqW2kDTeY0Q3jHnNoXwcmm-36HluCbvidUzs91wdVxvNbmuyxtB2ffpRPuZUg1lQs4_ru4W8A6eRPyU5gzD8d17ZYwczOBfZP4REQqJriO0Tg6IM7L2fU-ihy2fUpGzwUdmsqiF3854gtPGDmqftumwz533LSP-r3nYKNO5FvYJ89IirhU0HLVUqqpQSBk8fQ6x5irL616MFyTIGI4RgETHqdnyYkNr87Dkh-kqYxSmVq1MAoAHpK44qZXrz1VH7xHqlSRehQ-GPuTgCRAbSoe0-uA0eKU1_gh3Zj8Tl9YcATQdFYnH2m97y0rEB5A73dQgA4Gk7K5Am2MqooyD_eKak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3a4e2ac35.mp4?token=U9RpxwCgR0pAdyx008LJyhEiqxvowpx06FbqmyZVlnbB5VJZbBvZ-syazBY8oTNSEVf5wHj8-sC2Zb1c9_1uG7oIY3afv-4Y7K2TVHZniACJflfdf2TFkcqJzV7P0iJ8qOjZZXx0GuGnNuBHQjsx9cXjGHkwTJy67rCWXd8diOKaPQIjYvgexnwHBjZCQvXwXs4PIZH20PZy4RCZTCJ36LaNH_ccJ_xFyFcOolqexi5ckIGvD5hNhz5FnKWFd4MOu9UL2xCz0Jx-Zpo8_VPzIs_9e5CBT71cICI044_fkQHVtcqgzjnXddFkDrXOT1SbIaAJnk2wiH5VsbYtDA9OqW2kDTeY0Q3jHnNoXwcmm-36HluCbvidUzs91wdVxvNbmuyxtB2ffpRPuZUg1lQs4_ru4W8A6eRPyU5gzD8d17ZYwczOBfZP4REQqJriO0Tg6IM7L2fU-ihy2fUpGzwUdmsqiF3854gtPGDmqftumwz533LSP-r3nYKNO5FvYJ89IirhU0HLVUqqpQSBk8fQ6x5irL616MFyTIGI4RgETHqdnyYkNr87Dkh-kqYxSmVq1MAoAHpK44qZXrz1VH7xHqlSRehQ-GPuTgCRAbSoe0-uA0eKU1_gh3Zj8Tl9YcATQdFYnH2m97y0rEB5A73dQgA4Gk7K5Am2MqooyD_eKak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
🇮🇷
🇮🇷
سریع‌‌ترین گل‌های تاریخ دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105340" target="_blank">📅 14:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105339">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_rCrZjuT_EpmI16Ea24LYj0bsmuwJEardjXHtILbKJI8bJdx1nTwazzP9NhvExhL1FONlxpkQ5xdGGcZ1pT_O-tYnXrJuw5_swwhUW7fi8i2NeL8xDEHhcU2eJdUdmNktXeIaf70X0a4K4MS0ZPcOwzYoL0mUWc7s8b23sFZj_lSQsjwY-e-RS6JYV3TIQlpIxd7sl2SN_qAN9y2ORrXUQ5L-GtL8WJamVSJH7w-FwCm50D_kcWa-OSy-dNQ4_pOaI1wT9ikkT_hfwLmx1eZ36m9KaeszxfXNgnwkZzt7rrJBuGvFbdaymWFfZ_MUz3MgnAUoaQ1j0yVH30FKdWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
💵
قیمت دلار تو دربی قبلی ۱۲۰ بود و الان در کمتر از یک سال رسید ۲۲۰؛ قدرت گنده‌گوز منطقه
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105339" target="_blank">📅 14:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105338">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d7c8fe82.mp4?token=T0NB2t9KM8lBqFIvuilTH-0iUbgnYQS65ro0q7c0hHH-giptMqcrFZAxanDGlju-47Dj_q8rOrOi7VO8bukxPCJrmullnKpv82DuoKLCdkE557WwHnVozE_A6-G3F43pJer3mGtAUnALTd9cmnn_-4Itaj3hIiDZatsevg3se19tmYQ5684RwHEl3pvanxKuOpRmzbCnDxor_UwM6oCAMncKR1xzQcUU0b0MHyhQI_y2uVi-PkrhViY2LSzIJfq25V7kGtbwCXLaKiCc5OTgdpdfFkj1Im7MNbapA5AfrT8AfG1VJGNOUGrskvYi5bw_hT4w5U2hSpJjcE1-jfvROjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d7c8fe82.mp4?token=T0NB2t9KM8lBqFIvuilTH-0iUbgnYQS65ro0q7c0hHH-giptMqcrFZAxanDGlju-47Dj_q8rOrOi7VO8bukxPCJrmullnKpv82DuoKLCdkE557WwHnVozE_A6-G3F43pJer3mGtAUnALTd9cmnn_-4Itaj3hIiDZatsevg3se19tmYQ5684RwHEl3pvanxKuOpRmzbCnDxor_UwM6oCAMncKR1xzQcUU0b0MHyhQI_y2uVi-PkrhViY2LSzIJfq25V7kGtbwCXLaKiCc5OTgdpdfFkj1Im7MNbapA5AfrT8AfG1VJGNOUGrskvYi5bw_hT4w5U2hSpJjcE1-jfvROjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
زنده از ورزشگاه نقش‌جهان در فاصله ۵ ساعت تا دربی حساس پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105338" target="_blank">📅 14:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105337">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
بهترین گلهای استقلال در دربی‌های لیگ برتری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105337" target="_blank">📅 14:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105336">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
بهترین گلهای پرسپولیس در دربی‌های لیگ برتری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105336" target="_blank">📅 14:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105335">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfQWGdEnbMmO5oAQezBukKV80n9Ko00SkslClWQiEBRPJmrPRiJ9MNW_GeCdWhZafIhJ_wlBDx3KGJ2fB-XqD9OXN_KICM62QbbxwugBNdkfObMZJ1uSmk00BHSN9Iwa5VQQE9Y-TtunlVQ-bVUgH6TEBOmz0BLwcwMv36gIQYhXWHL6rjZxrBW34AOpBiuXZaK6Iu2IwMHnrmKrlycMVvrxrTN2D3eKs4P6eMy3O7k-QSyLUSIiOWUlwtXtSNG6st4nb4kcFJ62BYqRxHGILM7HIrEkeViMpRYMZXVlVLxEJrl843ypHwO8-wB6KKTNKFQ62p4q9yH0dviJp3Kwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😳
💵
خارکسده
افسار پاره کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105335" target="_blank">📅 13:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105334">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhO39cyp02I62mDm7Y1H4JXN8tOjBsTFJrNGgFENbBIKpxDRuaqrcyvfNV6pQHIIkSmc_sXdxpP6pGlaO45UdNkDjqiwC4LUN1yW5I3l6NH4njlNnGKEyNvoMTe12Pf5PLV4ygL4x3lntFAG1Miz7O_MiATCHSrVemEEKPrNwLPv0-YM-Blu_P8awMIpv3sS9sDmFgpNH6tYG5QugtN8miH6DK1omEO8nGBf_ZeV37wF8rTMRXCSQ8FLdh-18QKAwjom28WNFsVjrLU3TU64foAj6W7iE8ZtgXWaVHLc3N47UVKpKOj0v958twmWOHO99k3Eqp2rFulhd6YGlsN00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
مسیر‌ فوتبالی عجیب‌وغریب آلوارو موراتا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105334" target="_blank">📅 13:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105333">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40825ae46d.mp4?token=XhDMmXQitcjhsZenCdnfZi0kpNGYhLDmDiAJs1PhExCMSbzBDCH7UjeIGNd81_mR3GyRws-fF9G0ia69vIlpkQiBe_Qm0KuIR3X9pU7A0VnZ8ny0Zf9g2fbqkTJtiRM0O2_TUYgxuYSkk6eVIqR_jy6ykTYV1H8d5TX4z1RYBwhlrjScWq8aE_h7EkU-7aNeFrPcKKyvLhhneRLPo8AM7PWnNM3rdqZjZfX8HTBw2LNGUUl41OmJG9WLr8DWHpQ_40W9OOmhNdazbuZBvFs-FmT7fqVXXHLTRKtDz1hdJy6D8ca5sOWeyGva21G0rWdXTgBl6mK1czgjpXPlETrIag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40825ae46d.mp4?token=XhDMmXQitcjhsZenCdnfZi0kpNGYhLDmDiAJs1PhExCMSbzBDCH7UjeIGNd81_mR3GyRws-fF9G0ia69vIlpkQiBe_Qm0KuIR3X9pU7A0VnZ8ny0Zf9g2fbqkTJtiRM0O2_TUYgxuYSkk6eVIqR_jy6ykTYV1H8d5TX4z1RYBwhlrjScWq8aE_h7EkU-7aNeFrPcKKyvLhhneRLPo8AM7PWnNM3rdqZjZfX8HTBw2LNGUUl41OmJG9WLr8DWHpQ_40W9OOmhNdazbuZBvFs-FmT7fqVXXHLTRKtDz1hdJy6D8ca5sOWeyGva21G0rWdXTgBl6mK1czgjpXPlETrIag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
امیرحسین‌صادقی: اگر همین‌الان میخواستم در دربی و فوتبال بازی کنیم، دستمزدی که باید میگرفتم بیشتر از ۱۵۰ میلیارد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105333" target="_blank">📅 13:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105332">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc8f3b366.mp4?token=lL8N-UjM1L1YJS0busozqQae52m7fhyJFP6PvLxQUG5CNdpe7wuQC6SE-QmqBjjb68HydLyxttmxt1a4HsPw7fZ1mD3ZFGio_HmWKydz7a9mbR7OngP2LK9r2Zh7asrRVfRRQE6BA3YW-6ppHy7CfYqPW6GiS2o_nzX6gzQPQdOHn0m4qfkHF_E1BaRshl0D0lQ2ivAWn75IBIM9vlWuZ030L7cKSRu8aNGiUEH7SIJEiqQMOS2Mrriz36-LL_V3ccWMMreO-VWOhzCcF9io08muoLd3Hc6axhk-JpPCutotj7syJak4KS45VRQtS6NQ1Zkn9FDesq8asAFpU8lCug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc8f3b366.mp4?token=lL8N-UjM1L1YJS0busozqQae52m7fhyJFP6PvLxQUG5CNdpe7wuQC6SE-QmqBjjb68HydLyxttmxt1a4HsPw7fZ1mD3ZFGio_HmWKydz7a9mbR7OngP2LK9r2Zh7asrRVfRRQE6BA3YW-6ppHy7CfYqPW6GiS2o_nzX6gzQPQdOHn0m4qfkHF_E1BaRshl0D0lQ2ivAWn75IBIM9vlWuZ030L7cKSRu8aNGiUEH7SIJEiqQMOS2Mrriz36-LL_V3ccWMMreO-VWOhzCcF9io08muoLd3Hc6axhk-JpPCutotj7syJak4KS45VRQtS6NQ1Zkn9FDesq8asAFpU8lCug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
حمله مهدی‌فنونی‌زاده در آستانه دربی به بازیکنان سرخابی: عارف آقاسی ١۴٠ میلیارد از استقلال گرفت؛ قیمت بازیکنان فعلی ١٠٠ میلیون است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105332" target="_blank">📅 12:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105331">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105331" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105331" target="_blank">📅 12:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105330">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGbRGuPmqLiA_JdqsOVZTFxWSHdt-l20tN2L6LybN_o7zVBNDq_Sb6oWTi2X8dkLemgKl3hGjVVQw2UmiCoC0cdg1ZvYxCnhcKxdZlqwDToT1m12XnTFcscQ3UNaKWGzbLzOayfzv4wdFwNmX2LIUIlLme5YT7bMRUAccqrfkbiCbOpOsE1_RKJBzguoueUhvhVElemYEAUvSxPj8cGbirAg5VcYsOoTmyRTvmALzRzLo2AK4CAKcvIPK-KYMFPqd3c6ilacmTildP48HgkFTE_LdmJbd5-Dp18lSXZ45U2n3T63EEHBX-vKnxjmOqBSPY8K8wCk5ggguY-LoQr4rQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105330" target="_blank">📅 12:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105329">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1137b6f537.mp4?token=hB7pCjIlLA8_8bwIucSQQJxClQz9nBzVHYBD-r47GAFx9q7Jh_8UuEME7b2B2GkZeyB4bal-v9L7r-ANNbVr5LYKlI9FfdPVDUipNIRaPbZlH-2XvuNViUMV5hsP_ZiBxgSzttfX5VEkKRNEWkoFd0mOx8VbyGoTHzYRcCnCiFF5tiPL_rlQi_jgtSAmnRn-4TAlu5zknOH4c6jzEYWr6rvfqszL1I2fkTsILf1oi4VdDIlLMjGRHldtsSOPVOimER_3RcUK4v7d-lKkmGnswhUoWcHbTJLz6oiy-J119XtWYbbEQiVhwpvzmDjdUT9qsfbsoZ3_NleM8exINLJExye8378wC-aGANV4_b_LkE2pmvjt23D4sEW1hWp2QF-7UmcwFsdE1cxhkPswiK4ebKU0zfuG7wJj5j9c8xvURBcAWTlB6tq8aVluUr3Q2Uq3EylYAOVbEP0hRz1JD--W0A880-yKWM0h0gUh_IIn5dtTN6TggbYV62SPWXB9tcIEDV4HZG63cK1dzn4SP6k-F_9Bga5jFe9QpuTaJ-fXivsaXN-wBSjlKxpck_-OBwNVFe5kti8CqhEB-pbg4bxaZbJywqX5sJ4Z7wpzt1hkHIvP-51PuzB31-oKljAKvboJMk-YW4mki19qJxZrnLPniR2npCyNVcMicQRGfKQ6LqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1137b6f537.mp4?token=hB7pCjIlLA8_8bwIucSQQJxClQz9nBzVHYBD-r47GAFx9q7Jh_8UuEME7b2B2GkZeyB4bal-v9L7r-ANNbVr5LYKlI9FfdPVDUipNIRaPbZlH-2XvuNViUMV5hsP_ZiBxgSzttfX5VEkKRNEWkoFd0mOx8VbyGoTHzYRcCnCiFF5tiPL_rlQi_jgtSAmnRn-4TAlu5zknOH4c6jzEYWr6rvfqszL1I2fkTsILf1oi4VdDIlLMjGRHldtsSOPVOimER_3RcUK4v7d-lKkmGnswhUoWcHbTJLz6oiy-J119XtWYbbEQiVhwpvzmDjdUT9qsfbsoZ3_NleM8exINLJExye8378wC-aGANV4_b_LkE2pmvjt23D4sEW1hWp2QF-7UmcwFsdE1cxhkPswiK4ebKU0zfuG7wJj5j9c8xvURBcAWTlB6tq8aVluUr3Q2Uq3EylYAOVbEP0hRz1JD--W0A880-yKWM0h0gUh_IIn5dtTN6TggbYV62SPWXB9tcIEDV4HZG63cK1dzn4SP6k-F_9Bga5jFe9QpuTaJ-fXivsaXN-wBSjlKxpck_-OBwNVFe5kti8CqhEB-pbg4bxaZbJywqX5sJ4Z7wpzt1hkHIvP-51PuzB31-oKljAKvboJMk-YW4mki19qJxZrnLPniR2npCyNVcMicQRGfKQ6LqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
چرا محمودفکری مانند کریم باقری در تیم ملی فوتبال ایران موفق نشد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105329" target="_blank">📅 12:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105328">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7p1kAJJgJHmeIT_Q0862ftWFXR11fCApKSeii7i9NvZ8N71RTGNyo40Lx5-P3STQv1kbfwOrrmtp_BFOd7ifLPub_PxBiOQrryTMECzYTjgiFFEglOGZP6kG_KqSh2uYx5JeuLSeJ4kmrddonhLheykoHMej9CymF3RgIuY21egJfSe7kjhlwnxcoD_u4sW3YmGk8cye7NGh8pF6GwOlxaILoksSBq2RkcTPk02VjJ4qnG7_6tI_TwuZOZ6eLrPC22EHmtBVKjeZ_yhOug4IPqUaimg0mr5SO_j_Hpd5n80-OwmBY1TH_lu3mF4NaQV2TrZXu0ClWZr7Hv3H4-xFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💸
🇮🇷
🇮🇷
ارزشمندترین بازیکنان فعلی سرخابی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105328" target="_blank">📅 11:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105327">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f75defa90.mp4?token=ONEicbSkrF6nY55XHZ9aXBruTxJRr4J-JHzyiEP7qSOPSlw14EQfG2asbut75mnhRAFYciayrogGfg6i8IFP-0L_0-OJw_9BpfNRAvFYHMQD_-vxVUJN0Km1s32pjRv5Q_hYMb49PoWZW6IJyiFfbBnXlfD2Ctm98fjQABvO64qai_ZKpG5G39hRUMw5nOtfDJdg4ft-l83Lrs-TAxWBO5uN7_yE7n4pFBV4OPKONTy9BysXLIOlCJDEBoYXHe_tK8queXNVjUMLwHZzxd2tHTJGYndJi2jc68bj1Xx7kOYh4ZAOpJ6z3R2zeQyYkgEHLF5CFBEIx7yvGOFelO7K231lMFgEhSDe5zKCf7HKlHYakNcZGoN6O1IAuVOmTxpQ5Xp0KOpxNe7TBvK_f7ZloFZMktqU4R-6IHaJAvPHM4EbxSPIvNF2ZoehBHisvBx3c_nC2bC57V3Zx5Fd4YpDedEJ8X2wpOoSUYdqHdkh8TN94s68Xl-5PRdHnN1o7jDqbchnRbSxAP4CVrQGSxK8JNkNiwMjcorGI8R05ieJHy3q9UuIq8WSgCRGdV9u1i8pejR1w5NGAEaUdQB8_2jEgLp7ic2ndq4ktzQ2qrO-836C_MFppfu9LxFWac-ywMdtzMz77hoNDmszzhA-om1-OOuicy7-u8Q6sn98i8Bn1go" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f75defa90.mp4?token=ONEicbSkrF6nY55XHZ9aXBruTxJRr4J-JHzyiEP7qSOPSlw14EQfG2asbut75mnhRAFYciayrogGfg6i8IFP-0L_0-OJw_9BpfNRAvFYHMQD_-vxVUJN0Km1s32pjRv5Q_hYMb49PoWZW6IJyiFfbBnXlfD2Ctm98fjQABvO64qai_ZKpG5G39hRUMw5nOtfDJdg4ft-l83Lrs-TAxWBO5uN7_yE7n4pFBV4OPKONTy9BysXLIOlCJDEBoYXHe_tK8queXNVjUMLwHZzxd2tHTJGYndJi2jc68bj1Xx7kOYh4ZAOpJ6z3R2zeQyYkgEHLF5CFBEIx7yvGOFelO7K231lMFgEhSDe5zKCf7HKlHYakNcZGoN6O1IAuVOmTxpQ5Xp0KOpxNe7TBvK_f7ZloFZMktqU4R-6IHaJAvPHM4EbxSPIvNF2ZoehBHisvBx3c_nC2bC57V3Zx5Fd4YpDedEJ8X2wpOoSUYdqHdkh8TN94s68Xl-5PRdHnN1o7jDqbchnRbSxAP4CVrQGSxK8JNkNiwMjcorGI8R05ieJHy3q9UuIq8WSgCRGdV9u1i8pejR1w5NGAEaUdQB8_2jEgLp7ic2ndq4ktzQ2qrO-836C_MFppfu9LxFWac-ywMdtzMz77hoNDmszzhA-om1-OOuicy7-u8Q6sn98i8Bn1go" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
مارک‌کلاتنبرگ: پنالتی تراکتور در بازی مقابل شمس‌آذر گرفته نشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105327" target="_blank">📅 11:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105325">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCCwLpGQ-D_75hRTnxVdYqCqzQ9ENFC_nODzgHdGyPmkvHy-u6RHE2EtoZyJTIjsBawZm8w5Eo22HWBfSQ4l__fQg3nu9SV4Q4vSLl2rGJJ99jgTzjV8LoEj46sG8xgk8D_w-UJtdIk5ZYfT-TaFAovnT6KWzd0-lt1MQjrXkzQ_MHT6Ln9kHKqZH5wGIep1JZIygrXqk8rPgKk9ZZs0z-QYhqYBhlTNwiKAXPpgg5gTCBiIJ95dhkPl_OzILkaNw-vmoq5cu7ACedxkgz81lTqr0gbLjFWhbTklFEMefUvPzz41xAkflWfLkQCryWyQ1q2qgCVfNOxe_WK5EfReUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKuBkaSB__DDa72YDEUUkiFNzVRly3bPjQ8QWndZOj_NxzE_SaKvTatIkjlgaQYx3rsQXKj6qt8BhVp9VeeJljyvEyUGLG14Mrawh_gqR7GX2Kj8bpDH0V1e4IXaeLHm2Mazlg3XscerXC3kCOY_cNGOR37cEpzZ2yx9X45ce8GvZ3W5eunmSPEt92niXv89VVHkCij0k7X7LYH2XIf5L0IGMBnY9H0XFD2MftvOJY_zvZ0Bn8ZUNMevpjt4xe6m8W4txN88Vyc0SuHL6IiosDN1ubi7hBte0tqsa9zS50LxGes-Csfc2gUNcKuLYgOik2VoIKMejdy8vWzczOz2CQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر سرخابی‌ها برای دربی امروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105325" target="_blank">📅 11:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105324">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">▶️
👀
🇮🇷
🇮🇷
مروری بر دیرهنگام‌ترین‌گل‌های دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105324" target="_blank">📅 11:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105323">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHpDA8yfzidtt2yEagXrGMAhzSfECTLHsjaWWCO32f_2TuLepFbGY6YekEV1JsUwG55DKVqBh0znCeL3VcX1Vb5-Ff9CmvlTQvQkdb-32XRZ_h0AMRTLyUjcb1LIgbEe67ISG2i0kMFXUIEAy-Bsia3WQe6XDwpb3PB0-gayvDI83y7VrSeNCtYLRcY22mMYu9D8jPwy2EsfNn8Dxxy9ekuW7UOW6vCnQC-MLc2kJhP7NF6VFnRVpTqK_Nk5GBOUnl8CEZaEzTD5wfRWmoj2jxL97-OUm60UPxakvHgZ1XvMfZ7b2VEY_5AhJxT7yYCcfZyzyFqHaDwKyspTD0xe4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✅
🇮🇷
🇮🇷
مقایسه افتخارات رسمی سرخابی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105323" target="_blank">📅 10:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105322">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3bce317a.mp4?token=CYBzW2jjONq4IgVZTOrpKe-Sbjt9AyxDvY0kWspSeFAFP41z9QN54hCZKkfH18HMoXvlDvF96_8TIDaC4EzPhgundUNDLag_W-BdMepiCj82Qa-vA_9-1ivH01D93DcwkSdu-fOz5mlYXEMLy6IhdXSN0kBUmkldHtALtNO-24brQx-UZ3kmPs0eo12YLEu3icvVNflfNHc92JCkJkjb2QsED7X4tmk_cIX2nOH8ch5-dg7xU_n0QLpN6XY5Ul3f7u2odo7OyXnWS8eYOpZXCaEaac0WEH4VgZ2gowSnKDxuNwtir3BySSubc35zYAmNHFKsX1goilu9JS0F38OGBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3bce317a.mp4?token=CYBzW2jjONq4IgVZTOrpKe-Sbjt9AyxDvY0kWspSeFAFP41z9QN54hCZKkfH18HMoXvlDvF96_8TIDaC4EzPhgundUNDLag_W-BdMepiCj82Qa-vA_9-1ivH01D93DcwkSdu-fOz5mlYXEMLy6IhdXSN0kBUmkldHtALtNO-24brQx-UZ3kmPs0eo12YLEu3icvVNflfNHc92JCkJkjb2QsED7X4tmk_cIX2nOH8ch5-dg7xU_n0QLpN6XY5Ul3f7u2odo7OyXnWS8eYOpZXCaEaac0WEH4VgZ2gowSnKDxuNwtir3BySSubc35zYAmNHFKsX1goilu9JS0F38OGBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😂
🇮🇷
محمد نوری سرمربی صنعت‌نفت در کنفرانس خبری دیروز تیمش بازهم شاهکار خلق کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105322" target="_blank">📅 10:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105321">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
🇮🇷
🇮🇷
سه‌دقیقه فوق‌العاده شنیدنی و دیدنی با نوید استادرحیمی از دربی‌های جنجالی و خاطره‌انگیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105321" target="_blank">📅 09:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105320">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca6813881.mp4?token=C6INRLYrkrev9DpFaknK6U8ubfDG41jgrK_y2i-m86FnObgjg6obtmEcG9Uf_HowJIzvWaQZ_X6FcbSQCutUI3Bw2DvWQASZOiMYhSnBzK4IvOSpN4dlcnMLI6h_6-wbHAagrTaBHFkS-PpfrCJYJahh6Rn1eakQovHrzpZnGOvhwsQCVe1BZZr4oLo5DQPBcI8O2o5JbjK3FACY24KN13S79wSqqxiTDwKDYeNdC6QAQ0SeNWp2HWxMVEqPaahPxK15EvK-fGv24PfR3PQancSwYbjUtW9BrOv8G9_FQ_8Cfmi3GLPDB4jTGHP72mmV9U1SoeJFj4zEMKwzoghdZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca6813881.mp4?token=C6INRLYrkrev9DpFaknK6U8ubfDG41jgrK_y2i-m86FnObgjg6obtmEcG9Uf_HowJIzvWaQZ_X6FcbSQCutUI3Bw2DvWQASZOiMYhSnBzK4IvOSpN4dlcnMLI6h_6-wbHAagrTaBHFkS-PpfrCJYJahh6Rn1eakQovHrzpZnGOvhwsQCVe1BZZr4oLo5DQPBcI8O2o5JbjK3FACY24KN13S79wSqqxiTDwKDYeNdC6QAQ0SeNWp2HWxMVEqPaahPxK15EvK-fGv24PfR3PQancSwYbjUtW9BrOv8G9_FQ_8Cfmi3GLPDB4jTGHP72mmV9U1SoeJFj4zEMKwzoghdZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
🇮🇷
فقط اونجایی که صداسیما زیر نویس میکرد دیگه نیاین ظرفیت تکمیله
🥲
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105320" target="_blank">📅 09:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105319">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇷
🇮🇷
یه ایرانی رفتی از دربی کشور زیمباوه برامون ویدیو گرفته؛ به دربی سرخابی‌های خودمون تشبیه‌ش کرده
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105319" target="_blank">📅 09:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105318">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105318" target="_blank">📅 08:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105317">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebf67c803.mp4?token=p951tuyC6GI1nYxjsRoUQPZiv8M0CwVYFMjp7mI-IUTCzqu2ndIsd3cKThBuCvXjdUL98XDXzDdvemt71kYDPsWXfGeWBm3Xov6riaxfVql3zv36SAnxXd0HH380-wshNCjojy-MBTauu13yTTmbfMNwNBeGJ_7K2IiYYzhx6cxtfXkBN5Aw7Pl3iFZJGtiPKp49GYXKUQIBrNsl2aqv63bt6cOrtJZsuitNgQuhGNhWinYcCHJgE1I3wSA5YRprrla7ImTt80VsuIbhcrFcsGerCODkU6geOv_QIBSIdwxUxJjSx5t1GsZrXVd7pKjtP693f8DRYdN8kSNkB8eZo54jzPPGLKVFoKDS4acWDqPhlbAGN6GwIRqNB8dR3ONSuNwu8NEWsHtehs_nrgliRMVUxH-EqKuo4o1vBuoluHn1VBsxoJChLRkj1kvcLA-nPDiFGc58zEUt7Kw4LB8jDTeI_9S5a5szrtQH1TM9yfzSsrGf0GhZi5H-DcMadRcOlVAGCze7LhDD4VwJsBz4i9d_eEmXM02jSX2WaSjlg8GixfPf31QnQFODiqDu-oflGxyfc7WhWeXeNOTghIZQhIxdWlVi0yEk2QyElXPF3Me0TnXKVH8jQOM0xAI2fzo5tboN3k8DIK-vljIFJX2rwdGwvtFr1R3_Hs108FYmzao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebf67c803.mp4?token=p951tuyC6GI1nYxjsRoUQPZiv8M0CwVYFMjp7mI-IUTCzqu2ndIsd3cKThBuCvXjdUL98XDXzDdvemt71kYDPsWXfGeWBm3Xov6riaxfVql3zv36SAnxXd0HH380-wshNCjojy-MBTauu13yTTmbfMNwNBeGJ_7K2IiYYzhx6cxtfXkBN5Aw7Pl3iFZJGtiPKp49GYXKUQIBrNsl2aqv63bt6cOrtJZsuitNgQuhGNhWinYcCHJgE1I3wSA5YRprrla7ImTt80VsuIbhcrFcsGerCODkU6geOv_QIBSIdwxUxJjSx5t1GsZrXVd7pKjtP693f8DRYdN8kSNkB8eZo54jzPPGLKVFoKDS4acWDqPhlbAGN6GwIRqNB8dR3ONSuNwu8NEWsHtehs_nrgliRMVUxH-EqKuo4o1vBuoluHn1VBsxoJChLRkj1kvcLA-nPDiFGc58zEUt7Kw4LB8jDTeI_9S5a5szrtQH1TM9yfzSsrGf0GhZi5H-DcMadRcOlVAGCze7LhDD4VwJsBz4i9d_eEmXM02jSX2WaSjlg8GixfPf31QnQFODiqDu-oflGxyfc7WhWeXeNOTghIZQhIxdWlVi0yEk2QyElXPF3Me0TnXKVH8jQOM0xAI2fzo5tboN3k8DIK-vljIFJX2rwdGwvtFr1R3_Hs108FYmzao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
روایت فرشید باقری از درگیری عجیب سیدجلال و مهدی رحمتی در دربی ۸۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/105317" target="_blank">📅 08:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105314">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
اگه استقلالی هستی، به هیچ وجه این کانال رو از دست نده!
⭐️
💙
📸
پوشش کامل بازی‌ها با عکس و فیلم‌های اختصاصی توسط خبرنگاران و عکاسان ما
📰
اخبار و حواشی داغ آبی‌ها
🎁
🎁
و قسمت جذاب کار: هر هفته قرعه‌کشی به همراه کلی جایزه
🔥
🔥
اینجا فقط یک عضو ساده نباش، محتواتو بفرست…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/105314" target="_blank">📅 01:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105313">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqyZOePlrS2Vr_hEp5UOv3C52BKHaQ4TiKcr5R1AIcufxkCeZAFyJsDgKE8_HI5-Pf1JU9k-uBZpiBxfYrn6sl2huPEtWDDjZXkpSRoHHAnAF7BtY6RJNy7BBQymWdx-JExQfZjTJVJN-3PCPGqD8ElTnPFUpUR5pj31IlmDeheDW0CI3hYdXwTM_KM3gdnfks6wlGnmNTouPJWZImKgqrIP1LU0BWxuJIaZu-f3W6OgYetVGUJXrZgh5Xxq-mtQN_32IMGYUJbqFa1-jJRTblMeU3sHxbGWrWWIESG-gC7-69QIp2Lp9RVyEsAjfxaUtmElYPneqGYZc4FTsr2_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگه استقلالی هستی، به هیچ وجه این کانال رو از دست نده!
⭐️
💙
📸
پوشش کامل بازی‌ها با عکس و فیلم‌های اختصاصی توسط خبرنگاران و عکاسان ما
📰
اخبار و حواشی داغ آبی‌ها
🎁
🎁
و قسمت جذاب کار: هر هفته قرعه‌کشی به همراه کلی جایزه
🔥
🔥
اینجا فقط یک عضو ساده نباش، محتواتو بفرست و منتشرش کن
🔥
با استقلال... برای استقلال
👇
💙
@Esteghlaal_twitter
@Esteghlaal_twitter</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/105313" target="_blank">📅 01:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105312">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/105312" target="_blank">📅 01:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105311">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⭕️
⭕️
با توجه به نزدیکی به دربی پایتخت و بازدهی فوق‌العاده تبلیغات تا پایان هفته، اگر تمایل به همکاری و انجام تبلیغات مدنظر خود داشته باشید، با ×تخفیف ویژه× در مجموعه تبلیغاتی تیوا با بیش از ۱۵ کانال مختلف ورزشی و غیر ورزشی در خدمت شما عزیزان هستیم   برای هماهنگی…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/105311" target="_blank">📅 01:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105310">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
⚠️
یک فرد ناشناس در مشهد با خودرو به تجمعات جانفدایان ولایت حمله کرده و تعدادی کشته شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/105310" target="_blank">📅 01:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105309">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f42b196ef1.mp4?token=pVoPN1UA_8SBdiRAr1mNeDgZYE7B3qwF7Uomx5JrwG6t87dMSvcvpIoLGOFhBVgSSp3dvLfJMNv2DlvXFFF8ibOzFZ82F4jGbViNih_wvar0taBfd2RPHGoMCegdfEjONpFjGIzxJ31OVez20Z4QARAN0JTq76ybk5DeVRptkB0G0ehj0fZ2wK-ROHHrRKt1ARlvI_teje2qAeL5ErpluAWJtqLMHXU3Go28zopM14ykP8Gzt6GQxRZLK0jpSI_nVlexAnzKjkiIbYJrjTCAgWlVIA_oiAKEKmlfuw1bQ6r6zRzdTS0Cjv5j_O9n40WPGHLrq8ypV9DngmREbrTacA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f42b196ef1.mp4?token=pVoPN1UA_8SBdiRAr1mNeDgZYE7B3qwF7Uomx5JrwG6t87dMSvcvpIoLGOFhBVgSSp3dvLfJMNv2DlvXFFF8ibOzFZ82F4jGbViNih_wvar0taBfd2RPHGoMCegdfEjONpFjGIzxJ31OVez20Z4QARAN0JTq76ybk5DeVRptkB0G0ehj0fZ2wK-ROHHrRKt1ARlvI_teje2qAeL5ErpluAWJtqLMHXU3Go28zopM14ykP8Gzt6GQxRZLK0jpSI_nVlexAnzKjkiIbYJrjTCAgWlVIA_oiAKEKmlfuw1bQ6r6zRzdTS0Cjv5j_O9n40WPGHLrq8ypV9DngmREbrTacA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
تصاویر دوربین مداربسته از حملات پیاپی به نزدیکی یک مراسم عروسی سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/105309" target="_blank">📅 00:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105308">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq5HGNYYhH8lISe8Uk4pL0Si_umgtf3ieMCpaUtdprT6M34hP34Dd8nXo5xQIsHEbGN4U_mZ5QVAfLw_elmH4XUkuIXaw_krptp-joFkGakfEE7NIJRyzOpt9W-oxa_ogAY9KVe1FO7uqM2DEaJn-YkHP8dJ97luvti4cagWNDFB0cSjArwJmfNbi6LhvH_TAc5z_qhYbwcAbQG_koZljXfZwjoYfYhrvI8WGTY-Kg16P8Ytp_rGAFFfoLr6jBelOApHVJ_jwkD89cSykZHjcvvw0IyI0yDSnxjeCA5_DFpj82dU-UIAZfB78qYf_N2Ehz-zKao8-Rwq-jwk8zQEkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/105308" target="_blank">📅 00:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105307">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/105307" target="_blank">📅 00:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105306">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180
#فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی اطراف استان اصفهان نرسیده و این اتفاق تقریبا بعید است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/105306" target="_blank">📅 00:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105305">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cf9805271.mp4?token=LEyXm73BM25sA11qXQpRGA-imLqcg-YWSQfx8m205hWi9v6wOuLPUxXRnN07N-s6j9AumJZj9ibglCVQ4ty3JfokptvtWf1yU69qnKwWPXQH93H0hO7u3CxT9nV2D9JeJcbWI-8iD4DfYoc9VEUMTPnuFkaDzVThI0IC50uWKFR-VBbP3MjMPMvVSUCgY-7Jh13IJCHKWdy4QdA1iX4vXfPwlhMsCFm0bXqvvzmo46S2U3TrwSEfXjMNO27HqAgOCl2OkvJBkJRs2FFaCSgpPLvu-K0k_Niw9aqkWFKTmvsixwb8GejCV-THdc9B3ju8ysvMvykk1-0721IPAyWYIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cf9805271.mp4?token=LEyXm73BM25sA11qXQpRGA-imLqcg-YWSQfx8m205hWi9v6wOuLPUxXRnN07N-s6j9AumJZj9ibglCVQ4ty3JfokptvtWf1yU69qnKwWPXQH93H0hO7u3CxT9nV2D9JeJcbWI-8iD4DfYoc9VEUMTPnuFkaDzVThI0IC50uWKFR-VBbP3MjMPMvVSUCgY-7Jh13IJCHKWdy4QdA1iX4vXfPwlhMsCFm0bXqvvzmo46S2U3TrwSEfXjMNO27HqAgOCl2OkvJBkJRs2FFaCSgpPLvu-K0k_Niw9aqkWFKTmvsixwb8GejCV-THdc9B3ju8ysvMvykk1-0721IPAyWYIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
⚠️
یک فرد ناشناس در مشهد با خودرو به تجمعات جانفدایان ولایت حمله کرده و تعدادی کشته شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/105305" target="_blank">📅 00:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105304">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcaf59f19.mp4?token=E6hbezdGrZ_E-Ju2vRz2MHf2CGa4bI7BAqyRWyXIXELT_g0Uj1z4b0HsHRxfc_P7OgAv2giXqas1pmQdxRWn7YNaEcI3Ws2NR9Xv66VXIXGOtBICAWtBoZ8PN9wuL68Kz29VRzHhxoQ57RFwzQOcB9_8JVZgJiSoQ--aujaHcOkE2HtSCsTk0KhPf73gvE0z3o3k67QBeF7OvMQmBweGd0aM9zkhMewATZL56e3JkLXPYxujj-D5Q2qlCIwA9LUjmnUUUwnNUWKO2v0VpWI82ywD8wXBXGEvbMnqHp5xj9XY7LnOKBKtwv92AFj1MtiJk_cBQRGOkax5FpSNCVxgSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcaf59f19.mp4?token=E6hbezdGrZ_E-Ju2vRz2MHf2CGa4bI7BAqyRWyXIXELT_g0Uj1z4b0HsHRxfc_P7OgAv2giXqas1pmQdxRWn7YNaEcI3Ws2NR9Xv66VXIXGOtBICAWtBoZ8PN9wuL68Kz29VRzHhxoQ57RFwzQOcB9_8JVZgJiSoQ--aujaHcOkE2HtSCsTk0KhPf73gvE0z3o3k67QBeF7OvMQmBweGd0aM9zkhMewATZL56e3JkLXPYxujj-D5Q2qlCIwA9LUjmnUUUwnNUWKO2v0VpWI82ywD8wXBXGEvbMnqHp5xj9XY7LnOKBKtwv92AFj1MtiJk_cBQRGOkax5FpSNCVxgSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
جملات قصار و واکنش منصوریان به حکم انضباطی علیه الطلبه؛ از جیب خودم خرج می‌کنم رای برگردد! مستقیم می‌ریم CAS؛ یونس محمود ١۵ سالش بود من بوندسلیگا بازی می‌کردم
❌
⚠️
در شرایطی که دیدار الطلبه و نوروز در هفته سوم لیگ عراق با برتری ۱-۰ شاگردان علیرضا منصوریان به پایان رسیده بود، کمیته انضباطی فدراسیون فوتبال عراق حکم به شکست ۳-۰ الطلبه داده است.
😀
دلیل این تصمیم حضور همزمان ۲ بازیکن الطلبه با پیراهن شماره ۷۷ اعلام شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/105304" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105303">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3i2oZOPf4Le0diYhwYF4fI_silP99jbbOa_8_wQK9Tn--lztGk55b1wf2R5KTqu5yAWt882SaRuTHsu_8K5pokmP9Ff-nriEKP4mjzwG1xcDTZrHyyFuK4kzCSGe3N3-QEbm48hwVzcZS9R3dTB-i1dun4FfKMxM3m7bgyAyi8yPqoLY1Ii1L1A6Nt9JV7LSK5vpzB39KorwAVAg4pJGt_qPRFXh38bbEyzv7ioDoS07rHVM7l0gP7hLSU-7YN-zdLMeXJJei7wMC0Vcv997_6MJWk6qR4ExCQEkxVGuhwzf2u4gxzpsqrg3Hh_JAd0wuGf3fDHbA6wuFme9XQrgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسمی؛ اندیایه با قراردادی پنج ساله به ارزش 65 میلیون پوند از اورتون به سیتی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/105303" target="_blank">📅 23:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105302">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
گزارشات فعالیت شدید پدافندی در شرق تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/105302" target="_blank">📅 23:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105301">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👍
🇮🇷
بانوان جذاب ملوانی در بازی با پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/105301" target="_blank">📅 23:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105300">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f706e532c0.mp4?token=qXr1_hOcA8ou9kNSR2AT2M3LjihUshfRSB_xCDr4Wh9QRiw1o90L-sKfFDdGUhKfYhvO_GpKCuEAXn7tI-IWib6kaaS2qrwj8TquDfkbScJadIe-u-XiyML5W7VUNSaVA27XcmFCJC_gcoRSDDDAk5_rP7bJrJm2DlpICkQv6ucHOasdV1ScrN8WMnmlZcoOixau03BoWM3yx3zMIJJXkdRkcm5Ce1yABRdBYr--nOSd55rqAHwo9CPxPJo0Pi8OgpJI9Q4oBWKUapkFhzLao39oBdXO1IZ_JtECqGzR4f2vzO2lCTDZBIK10w2vdKhxmIVcIIqupZYG3GEw4xvy6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f706e532c0.mp4?token=qXr1_hOcA8ou9kNSR2AT2M3LjihUshfRSB_xCDr4Wh9QRiw1o90L-sKfFDdGUhKfYhvO_GpKCuEAXn7tI-IWib6kaaS2qrwj8TquDfkbScJadIe-u-XiyML5W7VUNSaVA27XcmFCJC_gcoRSDDDAk5_rP7bJrJm2DlpICkQv6ucHOasdV1ScrN8WMnmlZcoOixau03BoWM3yx3zMIJJXkdRkcm5Ce1yABRdBYr--nOSd55rqAHwo9CPxPJo0Pi8OgpJI9Q4oBWKUapkFhzLao39oBdXO1IZ_JtECqGzR4f2vzO2lCTDZBIK10w2vdKhxmIVcIIqupZYG3GEw4xvy6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🔴
خداداد عزیزی: داور عجله داشت بازی تمام شود
. چجوری 2 دقیقه اعلام کردید؟ وقت اضافه را کی می‌گیره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/105300" target="_blank">📅 22:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105299">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f17ff9c0b.mp4?token=p7Oiv9q_hQRvZzXttUi0RuOLwIvaRawa--C2fA5cMKw_EV0G3gw1J3lxLkqdhVFlM3_kde9RjkJztLWvja-WVBQN7MXxAtcTnaKObcnlDu9dCwFpzbtahsp2fMxgZaJDRu46PTt6MlGX5biRJfq0b7W9lE__UGVrv_XL4K-1EBuSRZgRm0PAVX_ieK2zQ6zRlf01pDOB4zGVzkj-sJ56GA3NxGKJNklTXcQqIN4J2y6FZaefq779Kx9UvruXh1SSJ-SmVivD7H15oV8VEQJuC-tt9dZ5Ufw2ImA0uAJa-0f9FjbQIBknQCSALYM_4gy6HBk3lOodTgMuKs1HQIhLQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f17ff9c0b.mp4?token=p7Oiv9q_hQRvZzXttUi0RuOLwIvaRawa--C2fA5cMKw_EV0G3gw1J3lxLkqdhVFlM3_kde9RjkJztLWvja-WVBQN7MXxAtcTnaKObcnlDu9dCwFpzbtahsp2fMxgZaJDRu46PTt6MlGX5biRJfq0b7W9lE__UGVrv_XL4K-1EBuSRZgRm0PAVX_ieK2zQ6zRlf01pDOB4zGVzkj-sJ56GA3NxGKJNklTXcQqIN4J2y6FZaefq779Kx9UvruXh1SSJ-SmVivD7H15oV8VEQJuC-tt9dZ5Ufw2ImA0uAJa-0f9FjbQIBknQCSALYM_4gy6HBk3lOodTgMuKs1HQIhLQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇮🇷
🇮🇷
همچنان از بانوان پرشور اهوازی در حاشیه بازی استقلال و فولاد خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/105299" target="_blank">📅 22:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105298">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=hWYQFxBov_lRn5OoPtGetnk25nxSfIv9kvu67wjc-S9TAAvqU592w3Ubi9-SX7fhQeKVP_WZcoOec3tiBKfvAcEoxcM1CZyDyF_b2xWJfdpvwymnl_qArJThCQKOy3VeoUHGAv7MDhxeosOWH8hSleLLG0H8j9Up04J79suPYHYFyhyKCYqVdfPHtOgAeLnlIHnaXmTmFYAEGOBn2g6DXcjTN1MfMBSkjVul8ils_znAwtvDCiNeMRQdc-dvokN1C94Kck333zRBv0u3fpwn_weR5KVWbxhTq5QSIvGCtybFI-NSZtaFfAgg3ZWf8UbRqMSc389w86rURgk-ONU2-7rM3GXGXA0ZXZGtDT3ofxFx2jByaW1Cpj-WuUE9X_K6nspt37LobRxSLG-xLLe8Kub6HR08rXWPU63nt4Dhc8ePlUTgKme9YRwNMIEMR1JSk_uS1G9sNk1Ckz23ljes-31vSo1efSQVo92ePMVKuKGqyRrf235SGs7OuUuMhRq2fHA4qS2Y4-8WAh4Ukgoy9HW5kqL0mSZNkuZyJJll8pDAkAiZzzd8FbMqBul1DRtQZRiLmR-eFog65OMLM0kHtZUa5fpVVLJb7--WctaOtgSjxh101oSV0mA9r0bM89XAPuz2KO6vToZXbIKkDmR2z3TE7k9Gs2spxBmMCL5lLcc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=hWYQFxBov_lRn5OoPtGetnk25nxSfIv9kvu67wjc-S9TAAvqU592w3Ubi9-SX7fhQeKVP_WZcoOec3tiBKfvAcEoxcM1CZyDyF_b2xWJfdpvwymnl_qArJThCQKOy3VeoUHGAv7MDhxeosOWH8hSleLLG0H8j9Up04J79suPYHYFyhyKCYqVdfPHtOgAeLnlIHnaXmTmFYAEGOBn2g6DXcjTN1MfMBSkjVul8ils_znAwtvDCiNeMRQdc-dvokN1C94Kck333zRBv0u3fpwn_weR5KVWbxhTq5QSIvGCtybFI-NSZtaFfAgg3ZWf8UbRqMSc389w86rURgk-ONU2-7rM3GXGXA0ZXZGtDT3ofxFx2jByaW1Cpj-WuUE9X_K6nspt37LobRxSLG-xLLe8Kub6HR08rXWPU63nt4Dhc8ePlUTgKme9YRwNMIEMR1JSk_uS1G9sNk1Ckz23ljes-31vSo1efSQVo92ePMVKuKGqyRrf235SGs7OuUuMhRq2fHA4qS2Y4-8WAh4Ukgoy9HW5kqL0mSZNkuZyJJll8pDAkAiZzzd8FbMqBul1DRtQZRiLmR-eFog65OMLM0kHtZUa5fpVVLJb7--WctaOtgSjxh101oSV0mA9r0bM89XAPuz2KO6vToZXbIKkDmR2z3TE7k9Gs2spxBmMCL5lLcc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
حمله شدید اللحن شجاع خلیل زاده به عادل فردوسی پور: همه می دانند فردوسی پور با تراکتور مشکل دارد!
💬
شجاع خلیل زاده: من دو سال است که فحش می‌خورم اما خم به ابرو نیاوردم/ فشارهای زیادی روی من است و خدا را شاهد می‌گیرم که در مقطعی می‌خواستم از فوتبال خداحافظی کنم اما این کار را انجام ندادم/ دو سال فحاشی به من شد. تمامی این فحش‌ها تقدیم به عادل فردوسی‌پور/ همه مردم تبریز می‌دانند عادل فردوسی‌پور با تراکتور مشکل دارد/ از زمان برنامه 90 همین بود، الان هم همین است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/105298" target="_blank">📅 22:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105297">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1acbc66f12.mp4?token=nO_-9DejqQenu7ECtkoqAG1rupYcSuZxygABvkCmREQV4tu36hleCH62vK1lcd3qZ9yG4B9lES69bYC8-xo7AvVSxRTckV3QTw5cNGlwbGS0hNkGuhLOJ8EIk_pTdZasg7thxFLV7R9ndEW85Z0DM5tW7jBxhXNaZfJ1x5sF-Aqki8y3ns5Gxip6XDRyWmK6uNwDqsYHb8A77ddUTP8FC-BEb_JxyPj90QhGk0opxP3P-SnrSRIIN17XtqDplb8auYxoXiTLuyGXQw--_13b5p_3OxwuSTfvh0lM02jsO1fc6LFMiaYGDJ6JVcxtFKVD43F2IzKXh5e2MQwQ2YlKMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1acbc66f12.mp4?token=nO_-9DejqQenu7ECtkoqAG1rupYcSuZxygABvkCmREQV4tu36hleCH62vK1lcd3qZ9yG4B9lES69bYC8-xo7AvVSxRTckV3QTw5cNGlwbGS0hNkGuhLOJ8EIk_pTdZasg7thxFLV7R9ndEW85Z0DM5tW7jBxhXNaZfJ1x5sF-Aqki8y3ns5Gxip6XDRyWmK6uNwDqsYHb8A77ddUTP8FC-BEb_JxyPj90QhGk0opxP3P-SnrSRIIN17XtqDplb8auYxoXiTLuyGXQw--_13b5p_3OxwuSTfvh0lM02jsO1fc6LFMiaYGDJ6JVcxtFKVD43F2IzKXh5e2MQwQ2YlKMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
تناقض عجیب در صحبت‌های پیام‌صادقیان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/105297" target="_blank">📅 22:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105296">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
آغاز حملات موشکی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/105296" target="_blank">📅 21:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105295">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2a82a31c.mp4?token=iTWNZk-VhbNPTUMC83f5keqZSU8GXQXfGS1q91LhySPM8-Bbs7_GSw1W8vGMuRb8vQTakcLO9Elvd06RUv4xKjSrRXLcu564UYhmROIiHgMTZK_6-KxiipXRV5Hk-yZUTY2uXraVv6DWYx-bqkQ-gYoJ2FZDJFoT93x-pre8TBcixxfrSjWsPsA7iTN3p2ZEuhzSmco_tOwQjRMiHTJoxscKXTwM7-TaePeA7raDcGRbzJ1i05j4D783RzlATxHlvxPKpU6t-b4sfsO-PDBZ3N3Y96M97bVmr73J-lbt6nogIH2RvEJi-o8KpRNxR0UCeEfmQwPeHzUyX2GviNt6Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2a82a31c.mp4?token=iTWNZk-VhbNPTUMC83f5keqZSU8GXQXfGS1q91LhySPM8-Bbs7_GSw1W8vGMuRb8vQTakcLO9Elvd06RUv4xKjSrRXLcu564UYhmROIiHgMTZK_6-KxiipXRV5Hk-yZUTY2uXraVv6DWYx-bqkQ-gYoJ2FZDJFoT93x-pre8TBcixxfrSjWsPsA7iTN3p2ZEuhzSmco_tOwQjRMiHTJoxscKXTwM7-TaePeA7raDcGRbzJ1i05j4D783RzlATxHlvxPKpU6t-b4sfsO-PDBZ3N3Y96M97bVmr73J-lbt6nogIH2RvEJi-o8KpRNxR0UCeEfmQwPeHzUyX2GviNt6Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
افشاگری فرشید باقری بازیکن اسبق استقلال: پاتوسی سر پنالتی چیپ دربی با فرشید اسماعیلی درگیر شد و ما جداشون کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/105295" target="_blank">📅 21:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105294">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8d66f699.mp4?token=ryKc2Ha6ZGp3aglJaObHfGqYMiaZtrk_hMKkuTyO5hZSAp8vk0d4O6uICL2FLu-qGtF2OTodmmJnk8j5MyeOt7nWqG7rCZRvVetTjKYhdMBULJAoHPZUwTQqqas06SaNUuLLyPpj-dSyLlqIE-WX9URPR7xYCpxbLZA5sf_h4kpx_zKgg7hB8SLlJaV5N-xUbmoXugjz08MWRMkTpCkFs3ogcZXQjerKY5VI6Yl6jMIMEmA4ba4EMNen23gzpVXbYPMsUrouzoFYOCiUMZWGMAttBkc-_xqW9eZCiI-M5j6Y1rp66hW9K16FgYbp6s_xkWBWcqeeZ1yjjQb803ONUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8d66f699.mp4?token=ryKc2Ha6ZGp3aglJaObHfGqYMiaZtrk_hMKkuTyO5hZSAp8vk0d4O6uICL2FLu-qGtF2OTodmmJnk8j5MyeOt7nWqG7rCZRvVetTjKYhdMBULJAoHPZUwTQqqas06SaNUuLLyPpj-dSyLlqIE-WX9URPR7xYCpxbLZA5sf_h4kpx_zKgg7hB8SLlJaV5N-xUbmoXugjz08MWRMkTpCkFs3ogcZXQjerKY5VI6Yl6jMIMEmA4ba4EMNen23gzpVXbYPMsUrouzoFYOCiUMZWGMAttBkc-_xqW9eZCiI-M5j6Y1rp66hW9K16FgYbp6s_xkWBWcqeeZ1yjjQb803ONUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇮🇷
💥
خانم‌مریم‌یکتایی هستن مجری تلویزیون جم‌اسپورت و گلر جدید تیم‌بانوان باشگاه استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/105294" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105293">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMpkzKASoZnqI_PHIAkBAldG_ddV2cdw35xM6zEjwPAJBfxiUiuTt6FAhG2BJgehIvcho4B91sely-3flFZDrXC08KFKFiJ5hgr3JqlwoY-ZaPoRyGbkorJpJkcDyuMNbiXSMbJQnITv-yYgiibcWrz1VIJEb13JfbWqDnrbp_E1HbGgVaPmMZ5YsLLmRTexupTYcK5p9gL6bHAhSihxFblhdpYdt2NuKRqBa_vZdxG4YCrOMHWO8dkTONym0CnHsvM4Tq0pf4KgbzyupZv-lFW4Y_X2prx7mlrf30QSd5-B74NBTe1dG9SAAjZJRYuHCXJevpUXOTN_Mh_f74pQWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
#فوووووری
از ترامپ:
🔻
‏"در حال حاضر، ایالات متحده حملات هوایی را علیه اهداف ایرانی در نزدیکی تنگه هرمز انجام می‌دهد. این حملات گسترده و قدرتمند هستند و در پاسخ به تلاش ناموفق ایران برای کارگذاری مین‌های دریایی در این تنگه (که در حال حاضر عاری از مین است، زیرا مین‌ها یا به طور کامل جمع‌آوری شده‌اند یا منفجر شده‌اند) و همچنین شلیک هشت موشک توسط ایران به پایگاه نظامی ما در اردن انجام شده است.
🔻
اگر ایران به این حمله توجیه‌پذیر پاسخ دهد، مجدداً و با قدرت بیشتری و در سطحی بالاتر مورد حمله قرار خواهد گرفت، اما این بزرگترین حمله نخواهد بود. بزرگترین حمله هنوز در انتظار ایران است و وقتی به پایان برسد، از جمهوری اسلامی ایران تقریباً هیچ چیز باقی نخواهد ماند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/105293" target="_blank">📅 21:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105292">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/649b5fb52a.mp4?token=rYa9GAUARFvM0XBETDB3US-UFbTzwjxi5Fiy2Cz_W6KkxVT40zgmo1g1V7uHIGbS1yk9O-rBOwP8H42-3eM7aGYDFq1qhR68fzn6MoNsFq1C34QI7Gazn5BnV5Fkrb-d97WTyL_tWOV16W2EMn69A4H-7xqI8MEUJf9vdSYZSCOaVP_f7z5qEyq2EMc4WRMtKMBAaa4yhu_bNAVjcXSTK4JYCxHFfWJjgT_zlCAGpPVmuJpiYeX8_BJbipmXVJ4KdLejtsH5__kZbhRl-mszMF-VdATCVVhli5VHRVqJlcXuMAJA32HD8K3TVJD7H8DFOxzZD1pvrYzoI3tzg7Zm1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/649b5fb52a.mp4?token=rYa9GAUARFvM0XBETDB3US-UFbTzwjxi5Fiy2Cz_W6KkxVT40zgmo1g1V7uHIGbS1yk9O-rBOwP8H42-3eM7aGYDFq1qhR68fzn6MoNsFq1C34QI7Gazn5BnV5Fkrb-d97WTyL_tWOV16W2EMn69A4H-7xqI8MEUJf9vdSYZSCOaVP_f7z5qEyq2EMc4WRMtKMBAaa4yhu_bNAVjcXSTK4JYCxHFfWJjgT_zlCAGpPVmuJpiYeX8_BJbipmXVJ4KdLejtsH5__kZbhRl-mszMF-VdATCVVhli5VHRVqJlcXuMAJA32HD8K3TVJD7H8DFOxzZD1pvrYzoI3tzg7Zm1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🍷
تلاش خداداد عزیزی‌ برای یاد دادن اصطلاحات پیک زدن در زبان فارسی به اشترکالی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/105292" target="_blank">📅 20:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105291">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0375b01ecb.mp4?token=XMMaB7eT0C8I1j20UxTl_6Jx21OVtB03Ty7wRIjDJ2KiyifFvd6SlFUw-GNwBmnOy4Kj6zJa23E1i3q_PsAwTuW9l_gO7YY9gyEzHabQDirBXxjBb1QF1KvybQikRM3DLZ53S-Phaz7K00Qrq_5iUoZvr63EudIHdrWr4_ogPOA4rKHXA0_DI1BDMSvbjnbFmrO6_vTrEw1vDJ2gYsK1Ob21WwjwoYGh1v7uuEqHeqz_g7M25zbaz3aT9-tGyXxBB40MFVatX-Tp7TwMN14vs1iiPNYA2KhmBMjZxpy1HAXpSxEKOOwGtwmmfqLA4Gcz6PNV4M33MCpzKEJ90BfLxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0375b01ecb.mp4?token=XMMaB7eT0C8I1j20UxTl_6Jx21OVtB03Ty7wRIjDJ2KiyifFvd6SlFUw-GNwBmnOy4Kj6zJa23E1i3q_PsAwTuW9l_gO7YY9gyEzHabQDirBXxjBb1QF1KvybQikRM3DLZ53S-Phaz7K00Qrq_5iUoZvr63EudIHdrWr4_ogPOA4rKHXA0_DI1BDMSvbjnbFmrO6_vTrEw1vDJ2gYsK1Ob21WwjwoYGh1v7uuEqHeqz_g7M25zbaz3aT9-tGyXxBB40MFVatX-Tp7TwMN14vs1iiPNYA2KhmBMjZxpy1HAXpSxEKOOwGtwmmfqLA4Gcz6PNV4M33MCpzKEJ90BfLxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به جمع بزرگان تاریخ منچستریونایتد خوش اومدی، برونو فرناندز
👏🏻
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/105291" target="_blank">📅 20:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105290">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zog9VsdLKAEb1DeYqfIryqsA5xNzjJtTHBLH4Q9xSOBwF3aGF4zNXXNU3mocORTOncItZD4lr5uVYsvyp6k2VWPelipSHV0HFw2lc2qztQ9qT5cuQMXzad4SMDmhl-rxhhDscaonmTdBQo85N5oirh0nRqhecYQqPzjLWI8vDs8PvmLms8S4CWKQrjUUsHC4kMfrE_LNO0WWieFPm9LV_bfDZg-oIQD5uJf6Qj39yjt7x6xanZVFmVWwd1qZ7R036_F_BJi_QBLcBXzAHEc79_dpFpWvEI007pYObGvWaCNK3iZIe_0Ux8xqhQpaQlYndDdENQNE0zU5VR0511SLdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
ترکیب الهلال برای دیدار با الاهلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/105290" target="_blank">📅 20:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105289">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
موج جدید حملات ارتش آمریکا به مناطقی از بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/105289" target="_blank">📅 20:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105288">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVjOeG19pz7xsC4HqSRwPOstgPABvkov1E4mCdMJ29KJ9hPgGwcB6tg07pit6VoFOLCNSNKIhJyRkh-dlkOIe8yzc61Uwb5kOWiKbpo23DJT27h2F9TUXcRFF0ZhftM5KfhBZbaTRJe0NEYkl5YkhN5IJjtZF9riXI1oEk05BVAUlTxY-vVhoxE-4_sBnRTaD4NdR8_E6X9zRfBJOZqCiBsqfguVsWBbO5K_9nin3GAJFbPL4J5YrDDe3PoLapYlNOnYspnK9hP5MJduHn_JhXfRqWAzxvP41KEo0PsFxcFp1WcVfCMWUstD0-Nkcodp44u5hLC_Yl__KjkeA6s-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
ترکیب
الهلال برای دیدار با الاهلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/105288" target="_blank">📅 19:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105287">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
موج جدید حملات ارتش آمریکا به مناطقی از بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/105287" target="_blank">📅 19:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105286">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
آغاز حملات آمریکا به نواحی جنوبی ایران از جمله میناب، کنارک، چابهار، قشم و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/105286" target="_blank">📅 19:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105285">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
متئو مورتو: مارک کاسادو با قراردادی قرضی به لاکرونیا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/105285" target="_blank">📅 19:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105284">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nn6I9XlmvFGE8gj1KHIvqWWqbekushy2xGRkcc7ve1hCKFkX58_ufCvTcKBfbr-u_Ys0zCrjsZ6OMzHKIFG9p9W4yd1EBal4bSTX_3CMg9UcZ1Zefm1Wju7dZrzxB64In4w0RcaKOsxWMDE_2C3aGMs4qC8kU7JfwmClkir6143y1UbZzrPIg16XQiBtNzvOR7MWLmg70OJbsztaDJgezbInnj2YlSQSf2yjhnaqQhzZRCZpuYtBQjyaoTjwQEVfHX1gBgfEhgWSMZM6xhMdq9z2Kex5iFg1pfSGVbBmpW8QXhkECXoxsn06VGH1tSsFSt86KGAZ9keN8KkT9MOu-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
متئو مورتو: مارک کاسادو با قراردادی قرضی به لاکرونیا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/105284" target="_blank">📅 19:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105283">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
آغاز حملات آمریکا به نواحی جنوبی ایران از جمله میناب، کنارک، چابهار، قشم و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105283" target="_blank">📅 19:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105282">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🎙
🇮🇷
صحبت‌های سهراب بختیاری‌زاده سرمربی استقلال در نشست خبری پیش از دربی:
🔵
دربی همیشه خاطره‌انگیز است و بازی‌ای است که در تاریخ برای بازیکنان ثبت می‌شود. ما شاید موقعیت‌های بیشتر و بهتری نسبت به فولاد داشتیم ولی استفاده نکردیم ولی از بازیکنانم با توجه به شرایط هوایی اهواز راضی هستم. امیدوارم بی دقتی هفته قبل را فردا جبران کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105282" target="_blank">📅 19:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105281">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAcidw2mdTI8OYI0hD67Gl-fvz7Z2JEnry_czVuWZMGjMj1qbDk_fJpOP1BR9N0pFcdmX7qw_2U_xZ81f45iRtTN34VtouUONCHhqzJ5JC88HHmguf9summD3UlYYuHq50HyBrnL6QPvl-zTTiFeLeOX5LGzYQb3Q0-dTi8EJ6Y-GjxiUtHJKejqgS9rmA9ZKGe_fxZJZUC4HZd1aF4dkd5-XyEUYrg_2oYV5xBndJS27LSeFeW11xgj-LOn-EVg7u94ocFXiyGuTdCCY3yIjbbhMz2hV8bWacO2AQQTDa7dXrehQfDb_84fTI2ntdlCE18smMBsjebNlG9tkaY4vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از دیمارزیو: منچسترسیتی و چلسی به توافق نهایی برای انزو فرناندز دست یافتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105281" target="_blank">📅 19:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105280">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33c4f0d2a1.mp4?token=AWVmWvA3KABZf6LP4k5ESx7ZYX5-tqdJLJJXofL2k4YG6w5JbuYt_7ILkNQcjKsimiwig20-HjT_i11-ftFCAY9RM7EBIip0__9YADGDhjXIK3oBu0Ag5CaaezxgBNzx36miS9g1e0QOUw9GdaWREY9kvXnjcgr5MO-dxy99ZsUPLvZb3gx3lkYbRDh_EHLsM4YpfWAYZM6kSvrw6RvO1UrXu7S9X5RMZ3doNYn6nT018VakbTwnRNhJk588cm3I5NPCmOaxoGhJYtV6Zb1uh_Seio1_9n9tNPkC0r7Yg-pWjHbkgeIpL2uE1hpP_fhbJu15KV2CAAk-MooZLEIheg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33c4f0d2a1.mp4?token=AWVmWvA3KABZf6LP4k5ESx7ZYX5-tqdJLJJXofL2k4YG6w5JbuYt_7ILkNQcjKsimiwig20-HjT_i11-ftFCAY9RM7EBIip0__9YADGDhjXIK3oBu0Ag5CaaezxgBNzx36miS9g1e0QOUw9GdaWREY9kvXnjcgr5MO-dxy99ZsUPLvZb3gx3lkYbRDh_EHLsM4YpfWAYZM6kSvrw6RvO1UrXu7S9X5RMZ3doNYn6nT018VakbTwnRNhJk588cm3I5NPCmOaxoGhJYtV6Zb1uh_Seio1_9n9tNPkC0r7Yg-pWjHbkgeIpL2uE1hpP_fhbJu15KV2CAAk-MooZLEIheg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
🇮🇷
هوادار پرسپولیس در آستانه دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105280" target="_blank">📅 19:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105279">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QE7v4LVC1vWwK0iR7ASYF9P5-KvBYVtHb7FixZi0oo4uPf5qHrYq_A2vpMWG6SZUDfWYy7vBUBFeHEktleEzfdlH1xkBuls2TutNBfeapKWIk0l0PlU0ZxH4JM3YqfwxaHiDOhJrFWiUq-9E-b5V691YsFFj4sRfoFRi-4JWi3RzBPoqoXxanQIiYTa6uahbK21LTB6dOVoKq_kYHMohrCfwFh7rIK21uW9tH-iFNgBpTeEHaSaKHt6hXxU2d3s-Ao1oJYGbHQyRkzdlZRRyEv3YwNAYAPH32L_uM0jCBytFyAKff_WbQ4d9vgGHKe6GiwGY8WdB6q2ja-uQIIefig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر باشگاه‌استقلال برای دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105279" target="_blank">📅 18:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105278">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07cf132574.mp4?token=D7TYXAgxyxl0HR54H8-jyWPzbZclq7lJTA7uYHru5e4U6esuJWQBGm72Hz_vLZPoH3nF5tMeWc_HTFbZR2pAw4ejz_QiM1OH1AELbumKKnAdJWWXnhD-POJ5lKfJKQKg65uPchc9wnIJLqEQicw7JQtvkAbL2X69o9ioaovOWbSSJeihwY8fBPRcbKe5RESpd3qB8MU7A7xTGM8G-Qkn7XSMo26DLckla7OYXCsla6kbbUcGegMXxVKypm0imtQ7FQLvYtcs-QAzC7fu4y8B8-glpt2-I9nxyggyvHpNTq8sCYsmafz8Hye_vSkvcQFFm11jczrwpEtc-YVaglhQZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07cf132574.mp4?token=D7TYXAgxyxl0HR54H8-jyWPzbZclq7lJTA7uYHru5e4U6esuJWQBGm72Hz_vLZPoH3nF5tMeWc_HTFbZR2pAw4ejz_QiM1OH1AELbumKKnAdJWWXnhD-POJ5lKfJKQKg65uPchc9wnIJLqEQicw7JQtvkAbL2X69o9ioaovOWbSSJeihwY8fBPRcbKe5RESpd3qB8MU7A7xTGM8G-Qkn7XSMo26DLckla7OYXCsla6kbbUcGegMXxVKypm0imtQ7FQLvYtcs-QAzC7fu4y8B8-glpt2-I9nxyggyvHpNTq8sCYsmafz8Hye_vSkvcQFFm11jczrwpEtc-YVaglhQZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
⚽️
تحلیل‌گر شبکه‌‌ورزش کشور عراق: یحیی‌گل‌محمدی تمرکزی روی تیمش دهوک نداره و معتقدم میخواد به لیگ‌ایران و سپاهان اصفهان بره!
📊
یحیی در چهار بازی ابتدایی فصل لیگ‌عراق موفق به کسب برد نشده و هر ۴ بازی رو مساوی گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105278" target="_blank">📅 18:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105277">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGrg_vNE4yDIaFK-ABNmmmXNvkO2Y9ISNVRlkKpqyp7J0OrCbVsqZI4z-9nzSBrA5MBHHKR4EjyzcmRw9_Nb26ZgC2pCZr4tc_4CdtLSfYDkCX2_y2ELOMdP9mCFcNizjuszLXf4ryVTjYSAJcvxlQeZ41N2pBKao_g7W_6balOgwhnQeV5pG4Gj1yvmIbHhlYEyYqs9JAfwZy46JYBcF048ipuOqamfApWNxm_LYKDVJvSQQdNF7i4RFagZbXnlctKA_jv1nWaFWICZhmIT8YSxQbvRZsp4Br3gPyudJ6DIi70tarrqzEL5WKGDTDMFJQCeQTJLjpi21q23onoNog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب تراکتور تبریز مقابل شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105277" target="_blank">📅 18:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105276">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7b5a30f12.mp4?token=HvpQoswHyCSbU2TKtjYj0nrMoPsVUfE4491S7ld7mE9Eb39XhEnb5985UQ3R6ZT3SWRpQ5Tzd3CvMrW1QPz_kwjU5KhnTS-gdMzsGyfb9ZcGAFqxG2UOX5W8TmGO97xakSiyCSBLOfsOfHkfbhq2mFKj8Zv2Ma5gQG77-Gl0X4FYDbYftA0R7Rf7YS36CAxZjHeql7sEJ2QUiVtAet2X73R5wUYoiqf2XtCnB4_yrpBqQwRdzIAghVOCC8_52MHUDZPznsDbgkfQAYW57HyGgcwdRDtv4V2oH7Dfw1sUa7MxesTK7hIYjhd9mP5pwFIl5L0Lc9qyaUOXayVIJ-U6tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7b5a30f12.mp4?token=HvpQoswHyCSbU2TKtjYj0nrMoPsVUfE4491S7ld7mE9Eb39XhEnb5985UQ3R6ZT3SWRpQ5Tzd3CvMrW1QPz_kwjU5KhnTS-gdMzsGyfb9ZcGAFqxG2UOX5W8TmGO97xakSiyCSBLOfsOfHkfbhq2mFKj8Zv2Ma5gQG77-Gl0X4FYDbYftA0R7Rf7YS36CAxZjHeql7sEJ2QUiVtAet2X73R5wUYoiqf2XtCnB4_yrpBqQwRdzIAghVOCC8_52MHUDZPznsDbgkfQAYW57HyGgcwdRDtv4V2oH7Dfw1sUa7MxesTK7hIYjhd9mP5pwFIl5L0Lc9qyaUOXayVIJ-U6tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان‌چالش ترند این‌روزهای فضای‌مجازی
😂
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105276" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105275">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105275" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105275" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105274">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMxZXyFQvdUWkLDbxku-fIr1jLN_-Kxf7T5TpIvprMBDKn8HaeQ0ds1nPlaFax3S4i6lCFVzI3ez-QUJSi8C6IkgpuWzXFw3NsQF2SqMsS0yZ7n-Pmn5JwGk98Ur0O7649EoXKddcW27d34EMyJjApKl3twHsQBE_ZMqVP1ngZL3QmfIfmtsf8xtrwDglpZg0KJrLja0tCE7mziLs3qCiV1bAr2lFQVsMOOHV2HBuETZ2_TKa6JBUji54KKAALYiw6EjWg-9UwqWrgCHufHWvfRLuxFSKDtmqyaPBmKWLs6EvgnDHUE5g4kf65sGzZpC3LbKVuSLXT6y25qX2a56rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105274" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105273">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9737ed01b1.mp4?token=YrQtUWsAItKG6i1ngnWV0GPcB1oD_UH0m8PACxNJkAwIbz58lxXZNIkgrsWiAWX1xh2qkrqC_EQEbkBOo9p8D39CAHFGRix6SzZD2XrQ_J8DP8mvGT-ZB-JUXIRul6K0VhfBRUWV-_qY6XLfpjJmM1ZmFRwfBZeS7_lCHAw-4p2FOsYlhf0JuzB-2dYddDj79j5Ddd1V9EEwV__5zYeaFR-HVtfUV2e02Z_c-A67UTdnTK8s1SK30WBmGGbfGyXs9KK2uMO-mQHaV8YyV7y3CC0rDkezOTiMje3_Q2G6LGbLnbgpJoiS7OcvlsIEmnsfEBiqM69tiHEdbk_fsmsEEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9737ed01b1.mp4?token=YrQtUWsAItKG6i1ngnWV0GPcB1oD_UH0m8PACxNJkAwIbz58lxXZNIkgrsWiAWX1xh2qkrqC_EQEbkBOo9p8D39CAHFGRix6SzZD2XrQ_J8DP8mvGT-ZB-JUXIRul6K0VhfBRUWV-_qY6XLfpjJmM1ZmFRwfBZeS7_lCHAw-4p2FOsYlhf0JuzB-2dYddDj79j5Ddd1V9EEwV__5zYeaFR-HVtfUV2e02Z_c-A67UTdnTK8s1SK30WBmGGbfGyXs9KK2uMO-mQHaV8YyV7y3CC0rDkezOTiMje3_Q2G6LGbLnbgpJoiS7OcvlsIEmnsfEBiqM69tiHEdbk_fsmsEEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
پلیس‌فتا در واکنش به صحبت‌های دیشب: به پرونده پیام صادقیان قطعا رسیدگی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105273" target="_blank">📅 17:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105272">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/273bbacf0c.mp4?token=sD4cuBaeVfzMHOI5RWibk8lgAtkMQN-FXvRQQX04VOLByJO36VhnsCsjFW_npeDx06MmxR7DLX49G6zWd3Od7-S44xSOVB65RqieRxg2xT_TbrdJO_frkm5nl5xQYIBdHkVbCw8LAVqJpBTHH-4n5GdGVRu-TzPDrjD6ZBxavf1Wn3IA6uwJr4mnf8qY75mej5iBcWXN8MSGLvFzbeKtC_50tzaB_sHeKKTn9p1mBDZ7Rm2wTOdE-8Ta3ZVnop6DptzEQ8c_REJysfayKTJ-KTpK70Gjq_Nuqadw2fxVG5zNh8JIGUiK4bVwFazX7CRvnTuY6mDDbZJY4hilmkYqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/273bbacf0c.mp4?token=sD4cuBaeVfzMHOI5RWibk8lgAtkMQN-FXvRQQX04VOLByJO36VhnsCsjFW_npeDx06MmxR7DLX49G6zWd3Od7-S44xSOVB65RqieRxg2xT_TbrdJO_frkm5nl5xQYIBdHkVbCw8LAVqJpBTHH-4n5GdGVRu-TzPDrjD6ZBxavf1Wn3IA6uwJr4mnf8qY75mej5iBcWXN8MSGLvFzbeKtC_50tzaB_sHeKKTn9p1mBDZ7Rm2wTOdE-8Ta3ZVnop6DptzEQ8c_REJysfayKTJ-KTpK70Gjq_Nuqadw2fxVG5zNh8JIGUiK4bVwFazX7CRvnTuY6mDDbZJY4hilmkYqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
تیم‌نروژ با قرار گرفتن در رده ۱۲ فیفا، بهترین رتبه سالیان اخیر خودشو کسب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105272" target="_blank">📅 17:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105271">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1b930efe.mp4?token=c-mW4IyN4FB0LZTE23wx8rtQWJKcSqVpe2fbpWOcyO6axhZKT5zuEVpN8G_ZsR0c1t4QVr10Q4dWue0U8tBpL70z1oY_nIDED3a3fyBPYcrDDRN1L81NIVtKyx21p9c-k5itkBci2MWcltdURIOMac9sxm1aRbi5zPTvxM2kCZyQd9_OVoKiXmLAV3PHJ5XoZKLg0wboceHD62dt2ljjXuGuwxckASxmG8ZAw9B4V8F_tneecUu_AMvoDfaCpZcdjmgpwtXbn0dZsfC33lC64mT7T0wac6t-Si3Hp3vdKZGzw2gUYXosdpiwnXFJbrvAAtlzODKAWVrKtk-XYVViGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1b930efe.mp4?token=c-mW4IyN4FB0LZTE23wx8rtQWJKcSqVpe2fbpWOcyO6axhZKT5zuEVpN8G_ZsR0c1t4QVr10Q4dWue0U8tBpL70z1oY_nIDED3a3fyBPYcrDDRN1L81NIVtKyx21p9c-k5itkBci2MWcltdURIOMac9sxm1aRbi5zPTvxM2kCZyQd9_OVoKiXmLAV3PHJ5XoZKLg0wboceHD62dt2ljjXuGuwxckASxmG8ZAw9B4V8F_tneecUu_AMvoDfaCpZcdjmgpwtXbn0dZsfC33lC64mT7T0wac6t-Si3Hp3vdKZGzw2gUYXosdpiwnXFJbrvAAtlzODKAWVrKtk-XYVViGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
صحبت‌های هوادار تراکتور پیش از بازی با شمس‌آذر: ممنون از نیازمند و ایری برای گل و پاس‌گل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105271" target="_blank">📅 17:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105270">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKfRNQykJORr2a4i24CSIqo7TEjax8VMnpd1qhRGrmWzJdeFHYrfGZTUVgHQV1_OykKDQTdrjnvN9aXZfEcyjm1rUBDeerPM4g886j6str648-neLWL88SMHOogKgDW7JP8lCEGJiQ2-MifhgaFw6RwLFctItantXOK0WPudmkQsYj1xoqstg5540SZ5a6Za8s5dASkD2_1a3oXlZ3THDZUjD_3dSkAYbHj0JuUVTDZRIrrx9YY42dLdVdKVQE6Au5eGYTkoY1uIOg-bF2XSabsscZPRE0_imHFdRE6Nemnyy99AVHFVX5q5O-eg9kEFp_1u9Fe72YY2sFMumgsjhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تاریخ اولین ال‌کلاسیکو فصل مشخص شد:
‏
📆
• یکشنبه 3 آبان‌ماه
‏
⏰
• ساعت 23:30 به وقت تهران.
‏
⚽️
• ورزشگاه اسپاتیفای نیوکمپ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105270" target="_blank">📅 17:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105269">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtZzCfWL75ySSZQ6zUnfuhxrDbdKGWg2O5FVAoLCvub36-vSLSUryw8Q4YNXqVOp0Anfl_W5t2JB9Nm252R4IcWTIpAaSFnaL2Otd-vcL8P1jf1gQOGhTnYEykyx5upftXwqkNOtfvN-ndIJ5HGeXtGmy6oGG237rebIr6cw-vTof7_w_eoyvVjgS6cJSfH_vsN5qmOSAr78B3IjI-SlGP4Pf9zmVAQ2iOgAyl79aE45TATCOKrSKZUY7yD9WYmqg9vTdUWV4HC9PmaOjuY-3zIJLnzvuxiz5cDqFKkddRRG1Hj0xbn6qtEz40r8ZjiBqTO-kvotuhwUruvDrI6uUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🇪🇸
🇪🇸
مقایسه عملکرد هانسی‌فلیک و مورینیو در تاریخ الکلاسیکو فوتبال اسپانیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105269" target="_blank">📅 16:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105268">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oC8CXhK6OpXbA0lDgJf9tblaTpGozLoQXct4P_ws4HqhyZtzyL0PAXC-ioGBNOy9zx3rx5iohv0xZYBYGtOrMYLnwCiFI297qFtafh85lOMpC_zfOqiEoKPDuK5df9QDrqn8o_bnwudiCREJ_zLGdgsTh_qmYDZSd9iVwO-VgDL8jYq2VuHj17vp3GND_zS0UzDcw0Xd_PaJjNlgDAtcNjj1PLDjGTKuD2NsS2Xyw-sA50Yk18Hy-r0S24BitbLcYDgGoV_KPHlQBsBmBPu0mddjLOrR381FNkuvFGjjWhQZPMC3QEi4gnXYQfRfJfeS4VJj8OX2daIZk4S2ky0TaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
💥
در آخرین ماه از تابستون یه نگاهی بندازیم به بهترین فیلم‌ها از سال 2000 تا به الان که اگر فرصت دارید در این اوضاع شخمی مملکت نگاه کنید. سیو کنید بدردتون میخوره
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105268" target="_blank">📅 16:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105267">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dfdcc87e9.mp4?token=pjSCdIq-IP9ugffYGha3Kp7jNHXuCARjZfh_zUp-nrRrIKtyfu6vJJ3NvbQurOo8vxR4tB6tUrzPPNweNbQaO22v3NzNnCHxFg2ABjl4jI_mJLk_uSdZsbRUx_zOKb7CacV0oEePfA20nA6j7NdYMeI9isq_otlJpQgYqbygGsY9YT8D3VX0EfsZ66OCV6X79mf2NE_wRqbwjcjlie0N9NY4FC5xOUzShSrSEO_Z4sp913mVJfwv0TxmNAcySbVFVI1UcdTDJ6jhqAZUUefSUHKZjaPYMcV0U5LglzDuKj7f5ktu3h6Pn_RKeYrUgjT43Yj8gIW89vCXU3sPjHpZ95kGFjyPHV6LEbPfCH9IyyD181bi7QE6vPyAYP_4nBNrMpcRwPFpSwJnRTXGCDGwKDS57mzn6G86RzCI0F3Tlm77X_JjfFa4jWadEzGu95Bb0PyW2k_iZT36GGb8c1SDjSRcjRdDYmPUYMEfKpE2QZ-VjtTOKwftVW_FsLaGM48h_1hGQzMG5Ll5HN-hLLymOSk5mzIwmBzBlyHmFJSbsMJVTYa2Wc-j13f2dWArbfTQQPOKlfyBbR69Wxz4nYGxNMTbFDEqMFT59vQ8G4kAAbzucbWoZejI3YtNB2XFJ7bM26Pm3VVJEFl8JU-1i33mnFweZwEYdYcCwy4tXy9jG0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dfdcc87e9.mp4?token=pjSCdIq-IP9ugffYGha3Kp7jNHXuCARjZfh_zUp-nrRrIKtyfu6vJJ3NvbQurOo8vxR4tB6tUrzPPNweNbQaO22v3NzNnCHxFg2ABjl4jI_mJLk_uSdZsbRUx_zOKb7CacV0oEePfA20nA6j7NdYMeI9isq_otlJpQgYqbygGsY9YT8D3VX0EfsZ66OCV6X79mf2NE_wRqbwjcjlie0N9NY4FC5xOUzShSrSEO_Z4sp913mVJfwv0TxmNAcySbVFVI1UcdTDJ6jhqAZUUefSUHKZjaPYMcV0U5LglzDuKj7f5ktu3h6Pn_RKeYrUgjT43Yj8gIW89vCXU3sPjHpZ95kGFjyPHV6LEbPfCH9IyyD181bi7QE6vPyAYP_4nBNrMpcRwPFpSwJnRTXGCDGwKDS57mzn6G86RzCI0F3Tlm77X_JjfFa4jWadEzGu95Bb0PyW2k_iZT36GGb8c1SDjSRcjRdDYmPUYMEfKpE2QZ-VjtTOKwftVW_FsLaGM48h_1hGQzMG5Ll5HN-hLLymOSk5mzIwmBzBlyHmFJSbsMJVTYa2Wc-j13f2dWArbfTQQPOKlfyBbR69Wxz4nYGxNMTbFDEqMFT59vQ8G4kAAbzucbWoZejI3YtNB2XFJ7bM26Pm3VVJEFl8JU-1i33mnFweZwEYdYcCwy4tXy9jG0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ربات وزنه‌بردار چینی وسط مسابقات جهانی وزنه‌ خودشو رو میز داور ول داد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105267" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105266">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b94f1ee2b.mp4?token=hdaogDJiUiRAQvlLSRwM4P0A6gO9sL6D7-6E0rXN5aca5cIBLAJJOcnrF12xp54y356gOcJFjvEzfyubJhY9QzGSI2C9yseWqPoKY8SaKGFneDdljHDJogUb6oo7jTJTO-U2ghI2kN-tPZMk4Sf8wPjWOoV0egqrYm_h5RNgKhfndfLR8zeSxIlhgZZmZsvmGD1CFZaXyFQg3jjtZiST4A7WOOn1Gp8CXkRmVxsCbFsm0gT9Vd-aJd8qHKfJ0sghLqJJt0rnSebQNrXCX6gVMQW9JroJi4jlblaSaf208Y15gJBmwvaZtxkY55FEzmpxpYWj4-c4yjHgls0_dMsbqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b94f1ee2b.mp4?token=hdaogDJiUiRAQvlLSRwM4P0A6gO9sL6D7-6E0rXN5aca5cIBLAJJOcnrF12xp54y356gOcJFjvEzfyubJhY9QzGSI2C9yseWqPoKY8SaKGFneDdljHDJogUb6oo7jTJTO-U2ghI2kN-tPZMk4Sf8wPjWOoV0egqrYm_h5RNgKhfndfLR8zeSxIlhgZZmZsvmGD1CFZaXyFQg3jjtZiST4A7WOOn1Gp8CXkRmVxsCbFsm0gT9Vd-aJd8qHKfJ0sghLqJJt0rnSebQNrXCX6gVMQW9JroJi4jlblaSaf208Y15gJBmwvaZtxkY55FEzmpxpYWj4-c4yjHgls0_dMsbqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
پیتر کراوچ در سال ۲۰۰۵ فکر می‌کرد بالاخره مخ یک دختر اسپانیایی زیبا در هتل را زده؛ اما جیمی کاراگر خیلی زود فهمید این «دختر اسپانیایی» کیست!
🗣️
کاراگر همه‌چیز را جلوی هم‌تیمی‌ها تعریف کرد و کراوچ تازه فهمید دختری که به او علاقه‌مند شده، همسر ژابی آلونسو بوده!
🙂
کراوچ سال‌ها بعد در پادکست گری نویل این ماجرا را تأیید کرد: «فکر می‌کردم به خاطر جذابیتم از من خوشش اومده!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105266" target="_blank">📅 15:40 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
