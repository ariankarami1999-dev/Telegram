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
<img src="https://cdn5.telesco.pe/file/Yg0vjgrv1Ox2Ty-ArkAxqB_5TKLeR3ZWGpdFSEFx6-OIZDkKfrwy_0R5jnVa_gzUpsOWUK1dVV-5JgBxsIHP_VTVbk73YU1FDTmCTbYpuWa3Wu83z46eCsORyolQ4irgm_pQlnFoPnG_4YpcFoSmzEtYJGq93aRc-nqxYFZMyVMCMtXFUBv3Ow1G8E9U-Q-3x09DqIX3WWNdcRdFZKnCvy76Yq0Xy92x3MeCVKzYrr6A3HpWAKHUkwk1cu2HM3Tf5YuRcUnAbQbbxhs-eXPx-Xo4j6IPSq7fHMJ_tZN5FOtJEs5HlSsliEI3Xexc0fEB_n-BMTxjqCNHAEIoXn_fhQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 654K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 03:26:36</div>
<hr>

<div class="tg-post" id="msg-97720">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkvYvI0Qv7ALJ5CqcrQydzDsuA1EHUZcBELTEafwjFnHMnA9cDZjAzVxMKjAdivgHufh_vSkXmoe1EtmFlEYVawycGTf-pkFB3t59KMXnM2i24QRQQFl9ZC85fn8a_uHBlIcpdB40Qg6TmhGsXUfeJOBvxXT393gHNMhtW6gqEYpJ0ComZHOUS6_wMZJ6r90JPlOALpzlXRYIMPDcDM8839RAWa-OD9SNM2UsySAGA8pOgvCSGiPtQ7mgRdLfQ0yZZmNJqFVJsjUMOZeOxR22uXsKNhe7pYklnlTTmy2znkY4L96pfTS4PmXFhdbIiMnzFiElnrtwouTl5lT8j0fbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو هدف درستی رو برای شوتش انتخاب کرد
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/97720" target="_blank">📅 02:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97717">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ro3FsnLBIXLt_Yp6Q8342hJud7JNz22sFnqhNB_Tm5r-cpCMrNctsyXC5muhHIgOD8lyrcbVb94DiRZsEKlnRw-J1ttOORlYcsmFs85stTe6_Gmd144bK6NY-NOao7GaFZqJOyZeYeug2Iq2y62HvwAqDSAcTy1PMgz9Bg-U36LVlOnZAomvaYJbfqY3AScYC3WZe9OAJAAQtZO0JJ9H51c3yYkD73cXaWM4dNgsxukIJZBNTTKyNv6vLMLBkyH4e3y0iEBZt0XVmQNZajL-S1I9vHTpyqSfqVpjIS00_bhYVTXJaXEoSL6D2fM2CcE71mw0Ppos-boZqvBmBkMTaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2dA-hEGaq-Ttw34PZ0KLsjonDYs1Zij-v9CIh9T6saZPCM0NvUC2zIDyj8gQS7u-i7dypnnpG2kPNzvFDRfEXnhVmGVItuirYFOjHsJaWRzTHCHUPAFvhgstDjp6QgN8JSEpRZyo5zNueYZb-E7qwo0JZQDfW93mk-K58PLwi905a_gFYzTjvACRcYfZtTFeniu8PWOrytQWFGJQ0r-dN9cq3_esvbTDXe5KvuIFsuHD_nZ9wSG8XaQOWR89oqvITLMHgBdgo3s-p7LkdhVR0t8JGZOErocPhmJu2iO1x4xWdMcwIiWXr7XvpL0s5_L8VLMahFa6HlMj2iyFiBPPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">The Last Dance
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/Futball180TV/97717" target="_blank">📅 02:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97716">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf30b3eba6.mp4?token=KqJHIYTfMAzu5W_du4TkoegTVTCDLQV8tMu-4mGSbCE-E03yA1Rzhat7n4eAt4pi0TNr68lelc2ML4fVXRsbOpbgWzDUM66rWUh7dngjKez8XL_eGDIptYInqRXufOa488tq0uCdx7jEDecbNGx9FarLAPTUZEv5feoG94kVGaocLt8UQeyF7KEY3rxf56ytcL4kPTVEwtRnCmSrb8xFFgxF3fsc9vlLN2Z2c_5-J0jMg2nOXN2nCJlMTSf-QDXMUAgMg-rBda-Q7P_Vw7T94Lb26Myfy6EUJDnLFXDdVRcUvk0jQDi12jA-fhicGYSSuB5q3bm3esadphN3PBKIUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf30b3eba6.mp4?token=KqJHIYTfMAzu5W_du4TkoegTVTCDLQV8tMu-4mGSbCE-E03yA1Rzhat7n4eAt4pi0TNr68lelc2ML4fVXRsbOpbgWzDUM66rWUh7dngjKez8XL_eGDIptYInqRXufOa488tq0uCdx7jEDecbNGx9FarLAPTUZEv5feoG94kVGaocLt8UQeyF7KEY3rxf56ytcL4kPTVEwtRnCmSrb8xFFgxF3fsc9vlLN2Z2c_5-J0jMg2nOXN2nCJlMTSf-QDXMUAgMg-rBda-Q7P_Vw7T94Lb26Myfy6EUJDnLFXDdVRcUvk0jQDi12jA-fhicGYSSuB5q3bm3esadphN3PBKIUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک حمایت کوچیک از مردم مصیبت دیده ونزوئلا یا نادیده نگرفتن یک خبرنگار دارای معلولیت؛ هر کدوم رو در نظر بگیرید جود از این آزمون نیز سربلند عبور کرد
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/Futball180TV/97716" target="_blank">📅 02:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97715">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کم کم بریم سراغ بازی
🔥</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/Futball180TV/97715" target="_blank">📅 02:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97714">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQRFrUEk4UoJwF1T3DrOqvWKiq8bQO3DW5qmPWNdLlpfipZJFTJXtglPk3VLgQ1pFApSVbZpyfftAA14il81YxZbRE9fcNePVc2y1-wG_9IFoYnZE22TGZLvR8TR-HSwP9RM-6aPgJkaELJfz8YL-DSkzd_olbPqvg0ThzjQc9sFg6lvgdfoXegFtKb3WVqtVQ3OdMmFywKGm4ECupuHzM5lVJyT2msgdrKcfJ24T5B4WUqViS_TwDrF-XwaWzzYF4lk1ju2EVJfdy-rWgsdlelTKtGmPH4k2MMyhPXIZc8W9LUlbg14ZR5cLHs9nvumNPvj6HF_jSjSZvazJJPpbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو رونالدو به مسن ترین بازیکن تاریخ تبدیل شد که تو مراحل حذفی‌ جام جهانی بازی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/Futball180TV/97714" target="_blank">📅 02:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97713">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/Futball180TV/97713" target="_blank">📅 02:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97712">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD1wsEhARGeFj0X_n10v7iooZ-jolC9KT2s8u4nBwDPbGfCIhn6bNyPKFL6vSsLgKkueWMeoSG5dwUL20_CUfzwKPmX0OMsZ8pdPTfPjQxVjnxPs2cOYyqeH4dnYLsTtpnKPkkIhFajlDMplaYzfVPgsMy_LLMdvkVb5qVwRx7r452JepuXb9TVdR5XigfyIPUifDhVJoQl5jMEvZzrJykQtM048KM2KWmi_rSOkUY8X1a5yo0-XrCxoSxiE7slmeGCuSBpr1OhqtpyKhR_0gEBOEE_T8r6p5R9vltcjbgeiogseczBpeoYb1tQ3vN2munu3ynmtmIPIGMV6e3KUoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/Futball180TV/97712" target="_blank">📅 02:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97711">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🔴
⭕️
⭕️
⭕️
مارکا اسپانیا: دیگو ژوتا ستاره پرتغالی لیورپول ساعاتی پیش در سانحه رانندگی درگذشت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/Futball180TV/97711" target="_blank">📅 01:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97710">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
😐
🤩
پیمان حدادی مدیرعامل پرسپولیس:
اگر قرار بود نام تیم گل‌گهر به آسیا معرفی بشه چرا تورنمنت برگزار کردید که تیم ما ببازه و تحقیر بشه؟ الان پاسخ آبروی رفته مارو کی میده؟ به آسیا شکایت کردیم و حق ما هست بریم لیگ‌قهرمانان!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97710" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97709">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8bcd50e5.mp4?token=UODkvwS3mil9I9uRMB5sQkk3pcIaDzopH6v1QuC4sEKqx1mHoWYfX9Whmfrzll4N3z2TlArTswTX9pPXDaQ76P3cdHYOhwspdHS8oeuM6BlJLRtCg0l96E3lTjF2mOLhIaP66biHeSyEPexbisjq-uIP-C5slHn1aiV8X26kmFhYbj9CZkLlHJw04-7XZhhHCo9STwa94C0pXXeXi0vNWimRnw1_VfUO8UYeWVdmgqQEKXXkXjGKWzGmA-KgFpw9FSqsR0Q83tzM_DuzkckvqbyRhVuyRUeU9kSyqofTvt_Wp33baLUTzZ7WFlJAIOTLR0UhRDNMR3ZYt2atkfWRMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8bcd50e5.mp4?token=UODkvwS3mil9I9uRMB5sQkk3pcIaDzopH6v1QuC4sEKqx1mHoWYfX9Whmfrzll4N3z2TlArTswTX9pPXDaQ76P3cdHYOhwspdHS8oeuM6BlJLRtCg0l96E3lTjF2mOLhIaP66biHeSyEPexbisjq-uIP-C5slHn1aiV8X26kmFhYbj9CZkLlHJw04-7XZhhHCo9STwa94C0pXXeXi0vNWimRnw1_VfUO8UYeWVdmgqQEKXXkXjGKWzGmA-KgFpw9FSqsR0Q83tzM_DuzkckvqbyRhVuyRUeU9kSyqofTvt_Wp33baLUTzZ7WFlJAIOTLR0UhRDNMR3ZYt2atkfWRMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خواهر رونالدو:
رونالدو بعد جام جهانی از تیم ملی پرتغال خداحافظی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/97709" target="_blank">📅 01:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97708">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRgZa_S13M5CuIx7rnNY0n564qkMTNFmb2srhMW4gZFivd3EYYLqR0XAIhD60FsS5dSzOpj0m-DjJZZcOF0r9g33chDK_qGdaAcouu5DBiQofu3VMRiwRQrK9ETwPzZtik16ID0NOdFmAR21VSSf0ci9yjoydKi_C_5SgNJshn8sln_l00qEvw84njsh0A_nhmQyfLDaZpSvgii0_OrOBb2Xg75PZRPJWgZRZBTWEq5P3ynD82nT5fuE1a_iEdGS8uHBhVvBJqoTyG1pLbGjl5OYRwDuc5fbCRCrFoIv7P9EgFp-b6QPlbWwnOAY2Jp4vkIBYpEeDYGal7yuqpscuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
لامین یامال در مورد احتمال رویارویی با کریستیانو رونالدو در مرحله یک‌هشتم نهایی:
«مهم نیست که با پرتغال یا کرواسی بازی کنیم، اما افتخار بزرگی برای من خواهد بود که مقابل کریستیانو رونالدو بازی کنم. در نهایت، مهم‌ترین چیز پیروزی در بازی است.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97708" target="_blank">📅 01:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97707">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esQZkyFDoG7iAn4VNFtTIqAePExtmmCid-sNrvjfrG1YpS-J_tcJ41UUnmtg6qwVhtf8IidTLVsi_TzHzqMX-YMUHr61Cpt1n9PNlDndhOsJ52RjNb6gul3piulbn-gUpIF8GtVOHPMzSz0f5dXj3XNugSo03D9a8pypnMaVvBaahEp-II66jWYNror-yRlGFTd7jx2-PgecCagKZ4RMMWsx4LWw27TjvddQdoV6R1fS_0lTgx3Beyye0WQieS5oEWH5JaI22vxUsEs1cL-z0cJr2uCi4CpJfgYIaMqEKBKTPC5RL-HQHGHZYHykIZmkUnLUVhSCrgO521gd0U8Z-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇭🇷
🇵🇹
ترکیب رسمی پرتغال و کرواسی اعلام شد؛ ساعت 02:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/97707" target="_blank">📅 01:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97706">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tghNrJMsMxhafrG0KhbLhIr8rTiuPlxWSoII9nxkoD8ZM7ZdVrUDQcrFa5ePHlOtE5-N7z3kM-Y-0SHsw17AHTxvZ0P9bOr3m3i_WluxqE74PqBBk9XFvwnkDzKzAwxDkb2dmmp52-7qRI1nRmN-Ozf3Js_9KhmYoxMINlF3UqAgiJxirRy-wf5TGaWnvCadObMu-VJJNGdQRpsAR4rcJw1B8zVkvIXUV8c4rKbGI0zG_J-5biciPIpkk4hG9pezRiPOXztm4BPqxSQ5CaBz7fGKYUVFJ_MpyXv6BhINnzoggWfh7i_mcRSWo8yEriae0Yh-G1cs7Yo6OiFd8nigRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇭🇷
🇵🇹
ترکیب رسمی پرتغال و کرواسی اعلام شد؛ ساعت 02:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97706" target="_blank">📅 01:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97705">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4FTyr1bHQG7fysTuIcJDWITLl5qoUmI6yD1xYEO6_LVS7NKk1eq2P1POzXSBkkpZ0AbMveZu2TZQfS09WVY7kFAEcVm7TFJt0dng2W-rI8iLTcNX9ldHzwblG9KhGoKKxB_VYfgsvuDmBIC3U5zKM_DlkfI1bwQ2SPW2ivr1TMP-OVVJdu1gTfgeYmjII5NfyIzezDNGgukcVBJ2_M8KPnpwxeSWHc2wu1BlQ73k4XoT0klVRFi_ydLFwcsy-dqfpFtH5um3K7oBxtP4Fk_nea4VPwihscD6eHHqBnCtJ9s8cmUTCeXyjjCnk83uBDlhpFirELZ5BzlJJDB1ik6Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
میکل اویازاربال وارد لیست گلزنان جام جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97705" target="_blank">📅 00:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97704">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adfzGnODDvNw9Kpdl4s9rH4gYaSTzWaEImsC0nqD-roLI4pu32jUHgoCz1ML2lNGqmzpEL5RiON5ltzuhzE3DIeEea6LGC-vshjAx6zw-YJsGiKJZijYeypU9cklfNkR2IekZPqavJSWZ1o9tFwk24WJk8lsWWkeuemCRRCYWc_6TUCMkWxsXQKJXiUgYLXF4nrGz3D99699IvzeC7S6WYWcmblKwE7K2fJBTMQAHjJNBe9annTJ1XhD92pG-BGZJdzO-b9FrkBlaxXA6GfH4Xwnm5lNXy6JlHQ_2QF8rvS-shpE-JauzgRbT12bGnNLNvfz0LhlBSFSr9AAgGQvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🇵🇹
آب زنید راه راااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97704" target="_blank">📅 00:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97703">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uiua-HHynSGzFKVYchOIVdTNKAu0p0O3aXBYNL56dCQm8MYhWicjBHVk5XAMTLne0Xbo2S4woBNRj2W0EYuI_rPzf1CwSNMRChvAZoy4R0LijFw-ZTf9NOdbeExLZahjXIeyL1kPWb3iT3qm-uLSEVBIzFGRfBnDgURfrMmW9j797AKBEORHEajKPW1VOUv2STXnGr3ZSqhSAxEpeB4T7n0ok1GDpflgQx4uJ9tE8JwRZXgE-hUrmEKVV0zpagkmKFQw4B1USzeVO8gAzvAuGhKmPNEFxyi17YYqKPx66t7LeP_HnllX7iUFjdseneFJtHz2yQI7l45Rpy3BN0JgdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
لامین‌یامال بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/97703" target="_blank">📅 00:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97702">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMMcdGSfL1J0YJ8pD3u0Vy8bP4jWQLT6rF3gOIei9MSoWFt1MZojkPlYGj9aQZpGI73RYTtc-NrK9xXHo5J2zprNi8o941memcQhlH966q3oi4fIqiE6faD2e63hF1vmtYdQq6eA-PBvaN1zbDYq7bYUMzAWe9-Lxh6pziO6gKFr7Y7BOWyuJXzzZDy-9A3ukX6MLF1Nuh_HUzj0q75Yx0dnnfyAQ-tVCvtYar_zTCeTuJ_8G1C2OrYhRAFypNaflcKyFuLBJmfdcKCM5ixwdqqf_GtnYiieZ_O00hzbQ8Nt3fzlD4wUeSB5S_3vZyPOUYgtXW6vU1Giflwtkm6Ziw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
‏
📊
لامین یامال در مقابل اتریش:
✅
60 لمس توپ.
✅
28 پاس موفق از 31 پاس.
✅
6 شوت.
✅
4 شوت به سمت دروازه.
✅
5 دریبل موفق از 8 دریبل.
✅
5 بار تصاحب توپ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97702" target="_blank">📅 00:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97701">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhYfvFLyZlu_aiMYqpnN8tYca0wfpjnwXyH0HbNzuOSV5xrQZrULc2h4GaHxZtfL6IcSrr7FU6gpUGTVm9Xpu2F2nO6Ozq38Xo-svzY3Wz97yaqApdouYwhD-BgPGTV5DINPKYrTg-ni_Z57i1T9XNMhnCTNkIPG2VTaaV4o2XlDGaZsHd322IPCVGU_BgneKWafkgDAxt4VRA1lE8KYaOV_duAAesOwiS0UdGPiXnVsX0u5uT5Kj5olpbb9Nosi9XIs9MTnjFDmKLIzM-O8C2Wu73T9rkglwMaWqDnfjD79nUZuGzbN8cguwul0sFPG91V95bGvcFXdqJ3wMmH2pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
اسپانیا در تمام ۹ بازی خود در مسابقات بزرگ، زمانی که لامین یامال در ترکیب اصلی تیم حضور داشت، پیروز شده است (جام ملت‌های اروپا + جام جهانی).
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/97701" target="_blank">📅 00:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97700">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIaY4T82lKCT1LjsS2UDQTr7AoQPPN-K7M0H1rvY5FYcQYGwm2FdW0APtJVofkk7gCKzRv4cD16ScrbrhjCnrSKX2ysrqTRJx7joDVDVYhbkr4a6AHIL7PYcDbNm2cGROvy3gaznmoiZPoGup4AxDQ5NTI9S-tN8A3cwB1kqpaNj0FAl_iR8R-e6J3Ciy3cJtVnnZ5r7bHbHQHRI9dbG5F5jatEqJQd5Txie5ntZAzLkeOtfAL9bF7Q5QexfoXTEmj8BZmKUE2OB8whP4-TWGGnTYiVsIKHiJVdg0gT2O_8zxpZ3C2NOWb5E1KyUbCudHd5EXAe8_til0g1XBIuqBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
📊
پاس گل اول اسپانیا، پاس گل سوم اسپانیا، رئال واقعا ستاره خریده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/97700" target="_blank">📅 00:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97699">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfLEINLLiUCT7wb2zLLGhRFtHfooknuQELTAPYqXGlbKEkNW6sX7MP7-t4tDj8XyOU0T0CSxTU_1PdF0ClsGm3AEmWyXrGIlxkUvXlf7QoV75H-uijcjhiafEPZBPxJgeKy4QAe8j6FFf_4jvSY2UH0uhPm1H4k0jWoDqyG19a_7DgkU_UVFH2jCYqgaJNcz4V9Bt5LE7ukUqnurUGGhT4R3LnGhPlkce3Z6LScgqmnphMdhzPcCqN9tvkDTICFGzu-o5KXM_Gih4pVkmZLIY77Bo08j8jz2GCc5WQAFsYji3kwJM9ZtcpXJvJEDLOpELl_XjpWmcgc6VFRsBoxgbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اسپانیا برای اولین بار از زمان قهرمانی‌اش در سال ۲۰۱۰، در یک بازی حذفی در جام جهانی به پیروزی رسید.
❌
مقابل روسیه (۲۰۱۸)
❌
مقابل مراکش (۲۰۲۲)
✅
مقابل اتریش (۲۰۲۶
)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97699" target="_blank">📅 00:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97698">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szTYz_Rn_Jb7cFQyvxneTFW-FGfojpK4ykzzZ3fUa2CLK4BZWRxv4skrlUaFjQMokFBCHJR-lhIyVIRKbsIgA5IsLidNznEbASi3-lq609Nbyl7N5hC7NaVqPnixTvGg5BsbzJlIon3zbWWCSWUJ0DS1AXy6izhTC7mVNbKzCrN_UeRFSY6M0n9OQKn9R7fB_Tmm-9iscjT4wmtjD2m6yixdgLcvfuPOUIfQC253N9FGQPahEOBSuaEdBAenPxndwRziexF4QwWKAZYpJ5hBn3ZN3jNHAWcLebsdyvFFH0X9kGffP64IXyU4vbqEOCQdlW_X9cXjxUHypPKzCDNBkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی|شب باشکوه ماتادورها؛ اسپانیا با صلابت صعود کرد!
🇪🇸
اسپانیا
😆
-
😏
اتریش
🇦🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97698" target="_blank">📅 00:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97697">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4DugZr3FPPSuNhrBe8LFQKClI7lCE6Qw9TW391kEc7pOI8SsJLlW7eZ6GXmrh2Zce6MTsU08YVsWFlQuyOXsA8fJtG7GJWpXgYcZPekUtbQ7caqy0rRJMSz3potP2-vaAXX_RazEXy0dkXJcR_gkWoWswhjZxxqhztHCHRlYhprOTaXdf2XIHeXT6iqIhkqPllBS3u9cJVIvlnuUDl19cs0kp4yWs6QZaciXAg9hlgBzT2XVMB_k4UxdZoaIA32M1e_IZDYbhb4SERJ2SK56AnfTh5NzYFOF9LDu38YGwGgxSpxpqAV0naqGXN0cLpX-A6D5Zysnh4YaZYoZOi2yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی|شب باشکوه ماتادورها؛ اسپانیا با صلابت صعود کرد!
🇪🇸
اسپانیا
😆
-
😏
اتریش
🇦🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/97697" target="_blank">📅 00:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97696">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🏆
پایان بازی|شب باشکوه ماتادورها؛ اسپانیا با صلابت صعود کرد!
🇪🇸
اسپانیا
😆
-
😏
اتریش
🇦🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/97696" target="_blank">📅 00:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97695">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/md8larUU0Q5kK-ctYS6m3l_VlsA5frtAMK6af1N26yykQjLEF5p_Ww7QTxSteTs6daolUbVIB1Hu2E0Z-o8M8E4-Ms3I9WP8QJzgoVJBk5QzO1gNLl1JBMINV0CrXILyYQOyN5gWcDX8o7Dk3kJdtBHbCIXkt-czndWzIp70iRhDWWk59No21JGn5XdQ3-kyjGqql6kmhEOQDAnlN5sNRxq-YYlIYDNsNrvSKbRo2tgTwBof4ZMYhSg5eOsMVqIQ2P5bY1wf0-tkvlGfSk8dZzgshuCaEl4MVuHLaepTwmIXuUzPHLMZ1nYJO5-_CO7PUGMP_p94v6K-ufnEj0Mkow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی|شب باشکوه ماتادورها؛ اسپانیا با صلابت صعود کرد!
🇪🇸
اسپانیا
😆
-
😏
اتریش
🇦🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97695" target="_blank">📅 00:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97694">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nN65hz49hC6qVpdbri_4U6IADU0i-aqHoPy7j4I1we2ODb69AE2_F5saMWIRi_sRXK2LJQRzf3KSe02nWtYozmy4pgH7ciwg2Rb55_Wqyk03v9rS2cjhIC46mxCfRAuXAnvcP8yanzRlvlZsD1pGa9pzoemO4LL0ccT1n6bNiisxqfiedZdGc6XvfQDZMpgXjpKVcqzX8WmP06-ffYhtfnZ_pMWpGvGxJikrXAyaFrX-eGZLRdxWCWvoDnHzjH9qi13tul-GRsTqLlRRlGaA4C-F23MYrYuhh8H457KxT2TmGSCOOAbjsAVCrkauHZ_-KKIPkzMGynnDFzdTc401pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش یامالو
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/97694" target="_blank">📅 00:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97693">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/839d973694.mp4?token=DQkGEKNdNpKO8qTklyDJgfVwQkmkcMBumuR-HyVivc93vHi4nkY2XOSK_dWO-PHwkFBYcQQ9zuRoK6GIXejCo4K6FLvUQO39qBwHfLwplxsiSCEb0koeyMwvb-o2r4As9JcAJJ2XNEQZ01UvmXJPwYk4pSnzGGbSUJALopxC8nzFWRxXJAtZ2DfAzDkug90bkyDP4fRl43MOsrvbJwcTm8kN_4d5Q4Zj5ursVXRWATA8_iJ020kxkPIA8297Y_BuKR42skRT7GokIei_nJkVLR6CnNXKrgLEk4_8QFU58tl3X9GcBwfuyKHMgH8z0fRsXMAfnDuaUgX0ZBtCXNNq8amo0cnUSlcIvf-90nd6M5vr5uIKRrP0tfeZKBZkWZJ3WnXHdLsOyfxLkxCzzgJntLPxbd9HbkivPHGnBhX4Urf-ohCl75w2w1ppRIG7O4X2HzhCehwuuz53nGUcLZrsqkxdMqp3sljOz9k-VcvD8l3mXIV6OUdmAS_jF6x2WAYyq6c0P5wz36PzRSL3dzD86nb9j_ZmOIRrfeqD7X9Mc63JxjREyjqsc6AcxRUo_P_3CUj0Pr8UCi2K6I62Apy3t0-gFWAWUi7tbnd-RRzssV_Jla-Ha5b5FUFn6deVTJYSdvS6dBOS5X4vMuw2cY3lm9COG_0ozwu4Tusi9W26-kE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/839d973694.mp4?token=DQkGEKNdNpKO8qTklyDJgfVwQkmkcMBumuR-HyVivc93vHi4nkY2XOSK_dWO-PHwkFBYcQQ9zuRoK6GIXejCo4K6FLvUQO39qBwHfLwplxsiSCEb0koeyMwvb-o2r4As9JcAJJ2XNEQZ01UvmXJPwYk4pSnzGGbSUJALopxC8nzFWRxXJAtZ2DfAzDkug90bkyDP4fRl43MOsrvbJwcTm8kN_4d5Q4Zj5ursVXRWATA8_iJ020kxkPIA8297Y_BuKR42skRT7GokIei_nJkVLR6CnNXKrgLEk4_8QFU58tl3X9GcBwfuyKHMgH8z0fRsXMAfnDuaUgX0ZBtCXNNq8amo0cnUSlcIvf-90nd6M5vr5uIKRrP0tfeZKBZkWZJ3WnXHdLsOyfxLkxCzzgJntLPxbd9HbkivPHGnBhX4Urf-ohCl75w2w1ppRIG7O4X2HzhCehwuuz53nGUcLZrsqkxdMqp3sljOz9k-VcvD8l3mXIV6OUdmAS_jF6x2WAYyq6c0P5wz36PzRSL3dzD86nb9j_ZmOIRrfeqD7X9Mc63JxjREyjqsc6AcxRUo_P_3CUj0Pr8UCi2K6I62Apy3t0-gFWAWUi7tbnd-RRzssV_Jla-Ha5b5FUFn6deVTJYSdvS6dBOS5X4vMuw2cY3lm9COG_0ozwu4Tusi9W26-kE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل سوم اسپانیا به اتریش دبل اویارزابال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97693" target="_blank">📅 00:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97692">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دبل اویارزابال
چه پاسی داد کوکوریااااا</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/97692" target="_blank">📅 00:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97691">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گلللللللللللل سوم اسپانیا</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/97691" target="_blank">📅 00:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97690">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbvcsz1CyOpVn5c61Plcky7TxF7LC05bZPIF9eqTpwUmdFLSYO9tBqunO3ZZDR873nn_D2Eo9NERUuRTIGL3wtVRJkFjVbX9AMeC9FiFs37ixnk3QH4QmRXjJaBFJVBZNPtR4Iro5SV6LxhZvEynpPk15lqCPASCXbX8oaIOpTux34rYDT1xOK8AhfW1z6WomGxbyoO9NKUm2QSTvv_2ZSy_6Bc1JBm8SsuJtYeE3Awv4E5gJ9iu9hWM6bjrYgkiOl13BwoVTnPN8f7abo2MmwEicUvp37XRueutUeoULSORwzIfVm4UKvN7M6VfRn0cdS-MWY3Tkd1gWRjaoVr_YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راموس در کنار همسر دوس داشتنیش بانو پیلار
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97690" target="_blank">📅 00:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97689">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8GllpX2gtpd70t1E6a5mAkWCSc51UIOAjcYuHKdbLcTG92fU3U4ys9urpu_4TkPI-BaNiynf6WsmiNe7Xk7sD219VVnbzCwiQ02Gzz2UwTQkVaxCC0AdvL-DB6GPhqRQvhRcqD7m1hb90CHpw2ZaZDxGfc0irlITj2FiYp9MDDDRInDd1ZIJesFfqOTnePHwt4kb_NJSSQAzYAD_yY_EqSn1qtz6LmZAAwtuQozQQcz8LfUBnI9gaTBVG9lzY_sDJeDvRqZ-vlOZ7y7KTnCrhfZRHxuEG7ZPHAy-u27-vZj16RADmfV-_LzRCYWrUl-uV1Si9Uicy5SOnFjplbOcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین شوت در چارچوب توی جام جهانی :
🔴
کیلیان امباپه: ۱۳
🟠
وینیسیوس جونیور: ۱۰
🟡
هری کین و لیونل مسی: هرکدام ۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97689" target="_blank">📅 00:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97688">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0e3d7bd523.mp4?token=hmRosbBTicQFV2FfH_ztZdaI8X9-oKX5Pbzp32WuhQMIV5WQ6kNpgT7fBvgY2phP0uE7k7U6FcqC3-nwY818Y0xm01VbQdZ3CGneo7hgh_VSaStu5-z69AlZcSN6HM0ljBhj24N_stEMs2LiVX0Qa_ZVGvwtQDLzeywMlR89vAhWhHnCKPMbG3XYovGcp1BYOcUpVHNe4BJpsUnk4iAcaVc8sY9AjUB4aTAwlrh2MM_Aw7GapsXPNYatDQrD3RJFdteZyf1TYUV73dELxMajTNOuCK925U0b76xKChQXqIpbkj4EOJ2JSFbelyaFWfL2O3uKv-Sa-CIoytqCVHrUUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0e3d7bd523.mp4?token=hmRosbBTicQFV2FfH_ztZdaI8X9-oKX5Pbzp32WuhQMIV5WQ6kNpgT7fBvgY2phP0uE7k7U6FcqC3-nwY818Y0xm01VbQdZ3CGneo7hgh_VSaStu5-z69AlZcSN6HM0ljBhj24N_stEMs2LiVX0Qa_ZVGvwtQDLzeywMlR89vAhWhHnCKPMbG3XYovGcp1BYOcUpVHNe4BJpsUnk4iAcaVc8sY9AjUB4aTAwlrh2MM_Aw7GapsXPNYatDQrD3RJFdteZyf1TYUV73dELxMajTNOuCK925U0b76xKChQXqIpbkj4EOJ2JSFbelyaFWfL2O3uKv-Sa-CIoytqCVHrUUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم اسپانیا توسط پدرو پورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/97688" target="_blank">📅 00:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97687">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پدرو پوروووووو</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/97687" target="_blank">📅 23:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97686">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گلللللللللللل دوم اسپانیاااا</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97686" target="_blank">📅 23:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97685">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بریم سراغ نیمه دوم</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97685" target="_blank">📅 23:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97684">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJSDW3IYJyZn4EmAM9YCTlayOcm2ZeybtYLakHGjRHjUm3dSIqIKjAIR2eFpRB4H_TMDyKa5QeOIn0mQgBpUdpegk6wzBs2zobWx3dYe0VXkHFbgVo8hSqHz7f2MZaxs3yi9Me7_dgLgMsWXdOMPFbLYGv5ujhAxaW-Y5dqOCYeGxGMMj7acIucbvexdduoov0HVDfw8ZtvQaqsYxf1qUT2YUybxKeb_f07Q8V1Qk56eF7LH6XCF3DB9tajiyObPX9wrwqjWYL9T_8W9yvgiEd6elpoz_D8EmuBVxKeQrBR4LDTCttLjFAm48qlZ0wO0IEEeo295l0FuvKWR4wRhCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر هوادار اسپانیا: نیازی به ترس نیست، یامال اینجاس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97684" target="_blank">📅 23:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97683">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdLZR-B6YxMBUqeR6SmtNaQvFxuaukBh87C_Ma8d6b9ftw9saCfmUfpbyNZwbD4070_gWhfI37ee_SZLXRD5v77NSVZxcFw1-nFWd22GuU664L2nteLCq8w5fJlpFL0JeW_BloCvwn9WY_9Tr2fil8LZWkUichd5di7ag6IbvIUrxOSzxZhNP4hxt8Kca1LU5Lxb-ArgGKbwgDK0cpJ3ODrscFQrTVodlljSY77Lzbg5wbPf5TDffp-Uj8NtOv_erOYlR1bUOl79Vbh0RcrkwsThQON313TW_7uosGkWGVC_JzIrYCrhol2hE-pM3vQLZoymN04iPuRVwXBqUmmFkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
رشد همزمان انس جهانی و قیمت طلا در ایران
📊
همزمان با عبور انس جهانی طلا از محدوده
۴۱۰۰ دلار
، قیمت طلا در بازار ایران هم به مرز
۱۷.۵ میلیون تومان
نزدیک شد.
🌐
مشاهده قیمت معاملاتی طلا در میلی</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/97683" target="_blank">📅 23:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97682">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFwD8FRrv7UtQuMlNIzrrqlKv41D-fGgqji54eP9DCctP5AL0hi6HBA99NFurLxDapPkOJ0rsn9KtY_of84tHH5d_ao3JkNyNidfbFEeroyUKcx-CLQEtB_keoXYqdZayssDVMPRSS9qeFCoOEKE9jhpWwSpc3IqFxY8VpyM1ZVTASDftTqbOcF_TuKKN2qBynXiMDkKSVUzuBpT0mDyhEiUQCjrIglbDBTzkSD-Sj24u6a_eiMEzjJ7Fki0bs0uAuCkDoymtz1nepBg0nnKeYGVA53xqEBqwf5g7peQc26p0Um1MyRMCJFvlygDnzgnRYAxAX3cYiNCRZI9ta2qaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اویارزابال در 10 بازی اخیر اسپانیا 11 گل به ثمر رسانده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/97682" target="_blank">📅 23:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97681">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پایان نیمه اول؛ اسپانیا 1 اتریش 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/97681" target="_blank">📅 23:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97680">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0033c4efc.mp4?token=j38GQm3WyinpyBoReXRniUH8aREHb3uaKvuIc0XNtiexz74ECqPl27ay60cT-jpGgia1o3iQan1HliPKkvsXgFmnUtCnucU_Owf8-CnZ5V32l4WWF2y8buge-DYJBoW_J6ryQe8Z_OCo2gN6O0JCllgogwYttOc-IeYYTjQOCtg0iHBaglUZ9ubcvKlbzKHrxL0a-7RLQdzCQTCmxjh53Qk924xCFKuRK_Uz9H8wIXoYez89Szgkf13hWxojmICUk0X7q93JSkml0Y8HG4Q2bE65BRV7PiSbcGeCE1kitwyUqYblegamEQJlacZP_Gdzmc9GTccWXKnh-Nf1qGUezTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0033c4efc.mp4?token=j38GQm3WyinpyBoReXRniUH8aREHb3uaKvuIc0XNtiexz74ECqPl27ay60cT-jpGgia1o3iQan1HliPKkvsXgFmnUtCnucU_Owf8-CnZ5V32l4WWF2y8buge-DYJBoW_J6ryQe8Z_OCo2gN6O0JCllgogwYttOc-IeYYTjQOCtg0iHBaglUZ9ubcvKlbzKHrxL0a-7RLQdzCQTCmxjh53Qk924xCFKuRK_Uz9H8wIXoYez89Szgkf13hWxojmICUk0X7q93JSkml0Y8HG4Q2bE65BRV7PiSbcGeCE1kitwyUqYblegamEQJlacZP_Gdzmc9GTccWXKnh-Nf1qGUezTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل اول اسپانیا به اتریش توسط اویارزابال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97680" target="_blank">📅 23:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97679">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پاس گل کوکوریا</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97679" target="_blank">📅 23:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97678">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اویارزابالللللل</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97678" target="_blank">📅 23:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97677">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گلللللللللللل اول اسپانیا زد</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97677" target="_blank">📅 23:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97676">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گلللللللللللل اول اسپانیا کوکوریا</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97676" target="_blank">📅 22:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97675">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گلللللللللللل اول اسپانیا کوکوریا</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97675" target="_blank">📅 22:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97674">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqCC4K4PEYC-YzXp2eRsxQ18GeESNEeqhTlPYVGxliGN1B8Z0zDd4Zv8OacQCp5QXPnD72Iaw-9wIJlVdx9lbBMbvn50vxBQE2lrGDvBGBW8UKCo5FFjix5zECMkVycsx0_Mqq_XG0LnkfvJdJ5EXAnq-8sjfEzf6uFKH05QjNfz8gRHhU3FifVZ1twKHTDPxJrZcSgHbgZq_nrtamGMlZtU1LQOOc5wwnqh3hV4Q_aiVYcYjrQgpmOIFXnu4F4SDD4iieAw7ZBgsboIK4ikNdyLMaVeNIHr2K_XpECf9GlgbGwLmEyI21XNcm3CQMoe0jGE-mFgCfS-X_FXL8Wstg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97674" target="_blank">📅 22:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97673">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شروع بازی اتریش و اسپانیا</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97673" target="_blank">📅 22:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97671">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tyqIXDe6WHXKTyixLym-oGrG-7ewmI8oFSVedrRxFYuIie0TEewjVLBWKICtiHHCYVbDzM9xjFegXblqGEjpftJBpoBblJ6A-tMkMClZF5N8iZNCvuZiwIC-jG2vMTOU0AyT6B-gwNgFpdfvZxxVimtLMpu9Y6KUXla0JunSbS9uHechc2Dg1a2cETQBOnxWm2t-ylJzgM3P4qjH641JNTzchmfufRYIFF0sETUEBvWa_UKDkRhpr_vE6_Q6JBEew44CNrG_H_0JDGjAJ_U5UM3nnilR1KixYg0NzdKem4SnaIwoa9zn0mfr7z7BPIMmYSwzMKb8RurU7HaGINrQng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aomp9aOkvMKcn0IInxroDzdU5-aYYa0nJ5n06hgxYfyNQBiKPBK2cLKaLhn7OligIwqR8eSnyypnzQQbncxzxHPh65Ao5Pw-mBkRRvtyPNsnZ6hTNos1S3Qrl9H59AsHYIUV3tXxP8d_XR5fSXjDNikUZLy8WeS5kSqZQZVehkcFlPzkLUXbln2Wymhdyd8ZlalMeqmwtuhptjBzXdmLofW2jn0LCJaE5aaV1KToi1XzuTnNPKiBu0OOFcux19rq9DYfvwnUCIRn43KdJ0M6vtXwQ_DAXsgv17_Q_0G30BFKHZI0sUmSkmNstJVgB3VeaH7j9D9M3xIXnJcRYBtKYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یامال با گردنبند بتمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/97671" target="_blank">📅 22:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97670">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😆
تراکتور باعث شد مردم از استقلال و پرسپولیس بِکَنند؛
‼️
زنوزی: در رسانه سخت است قبول کنند تراکتور پرهوادار است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97670" target="_blank">📅 21:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97669">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🔴
زنوزی: طرفداران تراکتور از گالاتاسرای و فنرباغچه بیشتر هستند
😆
😆
😆
در ترکیه ابتدا طرفدار تراکتور هستند سپس تیم شهرشان. خیابان‌های تبریز شلوغ‌تر از خیابان‌های استانبول بود. امکان نداره طرفدار گالاتاسرای، فنرباغچه و بشیکتاش بیشتر از تراکتور باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/97669" target="_blank">📅 21:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97668">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InbN56RKUknnSa9MgsCfQYAfKvBhTERwvTEqVRTB2QKWe3adm93q-bPgMvWZjBGYGzBYiQ1HSJAsA_PHehPQWj0mbFakzPIAT5lBPIlKA8k5eo7Hwl5wiyc85Ez3AwxEMeutGIXlI0_mPA5Oev8f8iZsuObrPw9Mp13g_gMZoTnJrO74XA4axMs7MXNHPuNyfueOMuYyPWaqjWIqNMXCEq-ZBAU7xYIVrB7NqXqFBE1hTyWYHPCFgJu5jV-T3l-4svOgkSnu_GD-HwQx0rLH6ndw58fLEOlJ3I4uSRZrQqynq6WxUcvz5C1KOwpk7jDiXQK-mETeuNFwAqWyQH7p0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو |
❤️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آلوارو رودریگز از باشگاه الچه به بورنموث پیوست. رئال‌مادرید ۱۲.۵ میلیون یورو از این انتقال را تصاحب خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97668" target="_blank">📅 21:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97667">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxc-l-9rTb9jsmAGxBEaPOEYNfaDq6aLIPzA2hLQzl5gjcvTsSZYx1Fu3f6L9OvWQYziIa4FalqyXd6Q41AFRE6VKPSDS3_z9Bo63LRZm7JeKvcbb6SMcZVj8GP5ZiqZYzsdsklslH10dVGq_wLYXZyyXIrCfmxtGuIMkBgqO9wrtWhiGotbbKAMI55t8n6NZnrVRZBS4BqQhjnY6cKZ2GGG5kZYt_egqro_9O0JL41CmEqv_hxZBpHjEVU2iPI7Rvn4EmGAz_Gj99ju0IR_8Frftb-MvnzRlk_7Vfr3h58okI3Eg0GGLJazwgeMEAh3yFE-gBdbZBkLhBY_bniGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اعلام خبرگزاری ها ایجنت اوسیمن در مادریده و در حال مذاکره با اتلتیکو مادرید است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97667" target="_blank">📅 21:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97666">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFq32o165lC1SRi2rGmgXfq70u6jpPJyCbJxjKHCP99OqreQarfT1zBQs0piB-hJTbqxe8G7NUX78i8Z0EL8d3A1ZJSryQpEVuDjkeTm-YSsxyPEHLMWNbpdyvjL6feAMS16l664i8bHDDaI2ldQUxOHKo21dYNIxdj3mTH4k0PXEYrLZxz0H-zZ54cliUVvQA6FoUrVIEmjmpnWozzokYZ91iFF2EtthD3boGQgjeT-hDLaSAgIzipgtYNIn7nJ0H_r-NwpNmk-8p6dGKWkN9ySGxEEdr-GsSRMCrfsHmmsPs6Y-OTDaLbtESqJeDSiMeLurVw8BykDh2jqippixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇹
شماتیک ترکیب اتریش مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97666" target="_blank">📅 21:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97665">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqtiDSTytkPTNC9e-9qFJEl0FVrQnQNohgZF7YqOHEtSuPnDbhvRIChC8nCNxuQbWtWNmbspDHHZljd0VUIIEqmVoD2jVbhnDWPojp_5v3zIIQwRBlXIs1oF1FNquwKBvLY5pEKygH48TSs7st8dCc4JnAm3MRZAq1p9SyMh1sLtjY9MZ2jxnOnGVGKeOiKZy3JXp9bi0P7JcbBOW06w-wHxcgD0E_lRbo3qlVtsmZziIyv1Z3nIHtaLbv9nlu6W0iaYFR_xAQyub0-lc8Ofblu3Hvi8L424buMJJX8rVIMiMXY3QdepiTgGhp02SU04sCdHmsO6f75cJ6VBamNtUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه لازم نیست بین انتخاب‌های تصادفی یا تحلیل‌های زیاد سردرگم بشی…
🎖️
همه‌چیز برات به‌صورت پکیج‌های آماده با ریسک و سود متفاوت آماده شده.
🔝
فقط
پکیج مخصوص خودت
رو انتخاب کن و وارد همون بخش شو.
🏆
ویژه مسابقات جام جهانی فوتبال ۲۰۲۶ | ۱۱ تیر
⸻
🟢
CORE
📊
انتخاب‌های کم‌ریسک و مطمئن
🔗
ورود به پکیج:
https://betegram.com/share/betslip/NPKLR49657
⸻
🟡
PRO
📊
پیش‌بینی‌های متعادل با سود بهتر
🔗
ورود به پکیج:
https://betegram.com/share/betslip/TCUMQ94076
⸻
🔴
ELITE
📊
پیش‌بینی‌های ویژه با بیشترین پتانسیل سود
🔗
ورود به پکیج:
https://betegram.com/share/betslip/AUZNP38876</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97665" target="_blank">📅 21:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97663">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b19RaGmaGnkk2CY3eq2ENUJOOkDtPFUZEY0xbIyErgiDc-3nGD9MME3ydRG_-CPKUbQ4EkMkmQP_07fI5xlM9KJ-3qL96178hI5wML7BvEHgUlRlP1N2l9BihagV_r2dBKYYgh-JlVhMiscxXVaYfGTRNoFJwWVLYRK8NmJvU7z9WaWFbjVXcu0KwBNMkxLBYcwHWreHnjuirpge7ZOPaG4EjlcwVo5PAw9l_ffjtJh9EWJm7a6v42JiWJO3yNwnmt5thHNLNncpdk_LOaIaTSftLHvJaQ_TGUP-5CSrMBUVTbFHRSVrOgMfv4LCJokqzB4nTAqt2dO0XSLssi3SVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
⚽️
اتحادیه فوتبال اروپا اعلام کرد که هر بازیکنی که در حین صحبت در داخل زمین، دهان خود را بپوشاند، در لیگ قهرمانان اروپا فصل آینده، اخراج یا جریمه نخواهد شد.
❌
🔴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/97663" target="_blank">📅 21:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97662">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usLX2o6UIqu0oR6vAcCquw3bgxTo30UGkipf5563yQcCdaArnLmzKE7qjXENRP1YO54jUBONTAQoykTpAYnL9vCmhbEe9fzVq3uyef7GF6PXhV92iS--gFfPjVxEND4QnPx_OEHHhNu-74dddsArgWRMBF7zMQ40UY0KgZdNqGlhvw_XkRhi8tHwEqWWseC2VJZPIGXvXLVp7KBieHLBWYIABnSCdQ2XbtOdxBnzbK33YzRRg-jJvqTb_2hMqFkNxY0grkh0hSOnCWlqnBzD4_N9L2SNwFksArxLD4RBh6NSbdB6C6SUiCim5AX9DuFWE-A1WkbMYydHnAvqfQ5E-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
رافینیا امروز بخشی از تمریناتش را روی چمن انجام داد و روند ریکاوری‌اش را ادامه داد. او همچنان شانس حضور در فهرست برزیل برای دیدار یکشنبه مقابل نروژ را دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97662" target="_blank">📅 21:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97661">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdeH2liNcA-CPwX5UlJMGbLYozbOoPFpgyJhoCXFqNUFSs9274dfQm8fmk1dFrf_AJHthU8dYFqRIbEPxWJ4LNvF3l4AYhdVJGC8F0RB0knCGbqVt-rB1bn0nNhOs1fBeYknX0Md-3Vvoe57SpoSCBxVP13z5sG6WxxYiOS3PhtvIpA0dE1zEYM_Jyh5dLC_lGaoj0EXjL2SIYmD6o0BRlwrueGSbSUEbAE9v1ljF4Q0eDWQKisxM-sHLrfae3oqUOusLpMfA4qdab1hgc7WTDnFNo7cVGTIHFG4TieoQ_jUznRldH6laWiMM3LPsxBC6Y6CGB4in1EjwduBpBcHQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترکیب اسپانیا مقابل اتریش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/97661" target="_blank">📅 20:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97660">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcacf03f8a.mp4?token=jDef8R_ZzqSQksyJLfeY5QMGUZVG36QGX7Jw4OKW6By8w_l8sFB8XrUuLZS0JPnnTv8njh1JC2u0ZN51RR73RJyBNkaHPnWN3gsbYv7Wwg29auZhLVa8fBhocH1hEiBZPSXwn9TUTpNPwCslx0dSsJt19PeBeB0u8N0-0KuuTAVKLrSvhdh4KOYCZi1N2qoOcVkZpLwLY4XJ8gSMMCSDnBGpfm3Ea905p3ZyyyLQ0WYWY1svbC5inx1Ztu4tEXg43Z5NQW0Cy6zDdtIeFbLYCg-ovgDwSnGgb0u8tNOVCaAb1MIeBnSPO-d5_7hLPROnRVK4bHeXS-mWFHCiAyMHzYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcacf03f8a.mp4?token=jDef8R_ZzqSQksyJLfeY5QMGUZVG36QGX7Jw4OKW6By8w_l8sFB8XrUuLZS0JPnnTv8njh1JC2u0ZN51RR73RJyBNkaHPnWN3gsbYv7Wwg29auZhLVa8fBhocH1hEiBZPSXwn9TUTpNPwCslx0dSsJt19PeBeB0u8N0-0KuuTAVKLrSvhdh4KOYCZi1N2qoOcVkZpLwLY4XJ8gSMMCSDnBGpfm3Ea905p3ZyyyLQ0WYWY1svbC5inx1Ztu4tEXg43Z5NQW0Cy6zDdtIeFbLYCg-ovgDwSnGgb0u8tNOVCaAb1MIeBnSPO-d5_7hLPROnRVK4bHeXS-mWFHCiAyMHzYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
جیمی‌جامپ دیشب جام‌جهانی فیلم دوربین نصب شده روی بدنش رو هنگام ورود به زمین منتشر کرده که خیلی باحاله ببینید
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/97660" target="_blank">📅 20:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97659">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57b10cb97.mp4?token=ATfOgovPvivIfg7i2uSwo-En7tcLgNbbKCsNbZA1WhgmD-JFtxU1sTMd7JpwVVnCkLxi2ghJCBiv0Fg1xSUK3qDs-H-yUgb-xFQ-5QwQ-4oWDnExB2uWHk7HFKL1OZ-onVMAotFuKtLB8d6XNqKwzb99cfUsWKGUCvOhXw7JFXorLT8E2-gClRlR4C1aanLi5XSxauktrHSXryL6WXglQchjZutQ8ThzEucyZ-sKk-XwUPw4CbEBY5v_6eDCVp78OoMi-m8hDy5HXnFdJAHPZAEhOBFv-E_VlsyBcbg_H4iqaqivAvyMiRaRvv8iPeUAL7skItJQKIUgdQL4aAszSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57b10cb97.mp4?token=ATfOgovPvivIfg7i2uSwo-En7tcLgNbbKCsNbZA1WhgmD-JFtxU1sTMd7JpwVVnCkLxi2ghJCBiv0Fg1xSUK3qDs-H-yUgb-xFQ-5QwQ-4oWDnExB2uWHk7HFKL1OZ-onVMAotFuKtLB8d6XNqKwzb99cfUsWKGUCvOhXw7JFXorLT8E2-gClRlR4C1aanLi5XSxauktrHSXryL6WXglQchjZutQ8ThzEucyZ-sKk-XwUPw4CbEBY5v_6eDCVp78OoMi-m8hDy5HXnFdJAHPZAEhOBFv-E_VlsyBcbg_H4iqaqivAvyMiRaRvv8iPeUAL7skItJQKIUgdQL4aAszSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
ذوق‌زدگی مردم کانادا از دیدن کریستیانو رونالدو اطراف هتل محل اقامت پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/97659" target="_blank">📅 20:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97658">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCPxK-8P0vssjx7pTv960FBKwg11sqv_l2f8OE1pUSAWgXWEZSzH9Cor53_x4AS-f4VbXW3tOxmduzzmFiIEyegSdObk_NU1WeWpRzDXYx7IP-wCThEkIUK5wHrS0cyoycSWKddw6RLo9gNEpek-HhFC44tA_SeN8ACMzR4PGRtea2QFbQTBQR_hA1gketG0ZvwnlN777e8xh_SiwsahzKl8Clo83lKUmuP8wsPyqGPNjKXuo-BuJ9ovhWv2R8QTGcceMuLNdaslo-3TKPKtHuWWXGhBOVccnwz64cejVTcEaYKxhDMW8qFEYX0rF2kyrP6If50O2lfBv0afs58lfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
— نیکولا شیرا:
🇪🇸
رئال‌مادرید به توافق نهایی با انزو فرناندز برای انعقاد قرارداد تا سال 2032 دست یافت و مذاکرات با چلسی برای تکمیل معامله آغاز شده
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/97658" target="_blank">📅 20:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97657">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYdtOeNFeeGo-5KMDVvA0T-8na749d4f9Opkp3J_B5a2aRePXFad9FjJ9VpuOt4pRr1hD-RmKh0b5alefwbnVa1E3Qp_msXA3yCtPZ4jusjisSkn3o3Og7e8NLCTf-Wbik6_Qp_75ki2tvBsKURmZn-LC6_FDVEXZKZzV6C7P_fsPQhrlihUzfFL7YSleKgn_1-qNkMeHlL7e4CV1P0qqYN3lnGrLuoJs7KxaNn3LFx7cjtCBvy1aXjlQlYgE80INEzQx_iptktfTf1u1jDUDnHg7_OoP0x8eUIkvAl8egH0Z3dyIakO8SvYergMF4c6G2jKKUwySIGQg4OjrhDOcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇦🇹
🎙️
رالف رانکینک سرمربی اتریش:
"لامین‌یامال امشب هیچ کاری انجام نخواهد داد، ما تمام فضاها را در مقابل او مسدود خواهیم کرد و خبری از گلزنی این بازیکن نیست."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97657" target="_blank">📅 19:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97656">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnsdS0y41F9BlpVZZJel4OgacvxiNKsfoxh40W5CUaiCMcMkKmEF-Fuvj-vWM69-l4-HquUAd-H9SzILb1YRwOKeR5Cz9lGwv17ihhGI-HwFL9Eb46vptkoW7rowfPkQjMxw2FoJHyv-vDNoGe_hViKJhtwm07lOGOdf68YU83DMjFu7048MKJKd7-R0oZPsjDafKfgFtdgzYFwDQuX3V0-cKmFKfEomndn3V9UkZDYqMu61klJaD3M2cj27SSZgmtcDbGxgyAOPTUyS36gEJ-3KyOWUA5vB9LjRcrVRPPDb4zsQcmc4M7GRuMKmNxMHyAQTbqUonJYJyzG_kuHr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💸
🔴
#فوری
دی‌ماریزیو
:
باشگاه میلان، ارزش رافائل لیائو برای فروش را بین 60 تا 70 میلیون یورو تخمین زده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97656" target="_blank">📅 19:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97655">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0b8DArmR3pJN8gdwz6jGdyaMYMMwpPUTKnr2fj-w6dsoHdJDY3Jl1gYx9_xXwkbtUgCfmOdrw3zjeUH4RQt1mkilbJHhu35Z9gYHTqB6VcbDAHNE0mOlF_CaykkWTZDbiMV2-l-PBb8Qi1xYmWafKZ7J-7cn4JnELY_Cogr1FEo4fnsXk_r5DDco3GKd3glNivvGQPS0lUezwTbo_8-cCWwEqXhGAo490WUZ09vM-qEQ9dVumzDqpf5jOnhisO0S-IwTxyljcE0UW2WEzl9i5iL98D3nNOY-h18zrec7VqqIcy6bb5mL24B7-gy8dUUlpOVxmCOeBwDHwVrBraG0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🤯
📊
یامال بهترین رکورد گلزنی و پاس گل در مرحله حذفی مسابقات بزرگ تاریخ تیم ملی اسپانیا را دارد:
🔴
— یک پاس گل در مقابل گرجستان
🔴
— یک پاس گل در مقابل آلمان
⚽️
— یک گل در مقابل فرانسه
🔴
— یک پاس گل در مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97655" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97654">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97654" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97653">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pzbX6kCcanh9ocPeP8W45t2rwI0qv63gQRm50DLpJ9rJ2gKLoMFTEtShVyAb-7f8AN1a0zsmbBBDJGZYlOEEBBQ29W-RXEW1vQclMm6xTjOWlukbbQr9g15ADmR1TgNbnPhE7F55AEiJN3zRtmCdCZ067dJjZeNYvqHBfvlkLmG9S4XIuoduZNho-QJJ5rbzO0G1A2zTa0ZW8mkvmvUzj4aqaURE3oD7QN_9-YjHzvfj5WYT0k_WyVxamCcSpl9BM1ME8XIgefvutCoKu3DdbLlvSs7VlrDQp031WcWNEf7iMKpRfQghxVDTSqFr6tvriC02UkXehHv4Q-0Y7BoxhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97653" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97652">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🔵
موندودپورتیو: بارسا به قانون 1:1 برگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97652" target="_blank">📅 19:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97651">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4659792849.mp4?token=bZDHp8wQt3UDTOrTM_pMyEcemeFa3b-r_zv8_Lplsh2WSDSkbka5Io4TA26BfJUZeDI1ux_Rqt5a2DEMPLzesLm4SJojwWzf4Da9I3beYp8XyfL0rX0YN2LqX8UsKUiwB4jz8wrB9E-oCbCEXFMFI2Rx1JlY5FDJSZdfomw2v2dUi7OS49JoJHD7SGuwpF3domzg7tTi8JTyfXEIyr9QbsE4oUEug0Rky6FQeQSBkoyq0sGNOAvMO_9-O020mBGCD3DAldPeqhVryD4MB3ICfSWx4hyOFz3ywDms4U-ZqwPMw-RQpxVozgq_XvVktnKLuGvwzdhS9gPiZ-Ncn8on8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4659792849.mp4?token=bZDHp8wQt3UDTOrTM_pMyEcemeFa3b-r_zv8_Lplsh2WSDSkbka5Io4TA26BfJUZeDI1ux_Rqt5a2DEMPLzesLm4SJojwWzf4Da9I3beYp8XyfL0rX0YN2LqX8UsKUiwB4jz8wrB9E-oCbCEXFMFI2Rx1JlY5FDJSZdfomw2v2dUi7OS49JoJHD7SGuwpF3domzg7tTi8JTyfXEIyr9QbsE4oUEug0Rky6FQeQSBkoyq0sGNOAvMO_9-O020mBGCD3DAldPeqhVryD4MB3ICfSWx4hyOFz3ywDms4U-ZqwPMw-RQpxVozgq_XvVktnKLuGvwzdhS9gPiZ-Ncn8on8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
متن خبر: خداداد عزیزی دقایقی‌پیش مدعی منتفی شدن حضور اسکوچیچ در پرسپولیس شد
✔️
❗️
🤩
واقعیت در پرسپولیس: جنگ قدرت شدیدا در باشگاه شدت گرفته و چند نفر اصلی بدنبال فرو کردن گزینه‌های خودشون به نیمکت سرخپوشان هستند. صحبت‌های خداداد عزیزی هم با دستور زنوزی رخ داده تا جو اطراف پرسپولیس متشنج بشه و به نوعی زنوزی از اسکوچیچ بابت نحوه جدایی‌ش قبل بازی حساس آسیایی فصل قبل، انتقام بگیره. اسکوچیچ همچنان نزدیک‌ترین به نیمکت پرسپولیس هست مگر اینکه زور برخی نفرات از پیمان حدادی بیشتر باشه...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97651" target="_blank">📅 19:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97650">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmz4V4dQmCsLtgBG8d8ZxW5esvwQs5inF7jdDTvpz7Kj5HytHGknpmh2iqlMIs5Q6DoZYZYZRmOAhNrLBaVOiS4gy0ogJWv-PNx80dAV9WsVClCUR0Fv19khXQNIvC8bZPlIV6uFLfoLMVAuDgD8JO5cUim1J24ByO712OPcUemBH3WFv1umvQ1WfAixlA7TamJXoWn7SRvblrnr8Z2N4h8YJE2CvzpAbGU3T5YXBqkn7990MGFit9RbCVlHRLkB8fhJX-PfNKQBHP92OUFrdsPluSwINxIN-ZEL6ZKkX0jYVQ3snjOJ5seBVXPAFA3xTacvEmuN3U063PQOkpKflw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
کدام حریف، سخت‌ترین حریفی بود که با او روبرو شده‌اید؟
🚨
🎙️
لامین یامال
🇪🇸
:
"نونو مندز، او خیلی خوب است، واقعاً عالی است، من از بازی کردن در برابرش لذت می‌برم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/97650" target="_blank">📅 19:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97649">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🔵
موندودپورتیو:
بارسا به قانون 1:1 برگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97649" target="_blank">📅 19:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97648">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUygjnNANjNssIPJ4XcmmIM_fWGjWwthBE-vIQuPnLUC7QQ9p08A8HGrK6xX-jv5JzhQgEctlvryfk1yCR2idZYqG-4YGVSwg1G0jBkMAVX4tYd172PAZly9RSCGqBhA2nft-78EzLSreP7bUWbpok1SfJPoj23J0UZMoFeVAw0RYkYRTl19Jrtiv_cC-p1aRjdXisluhXHD9C75ecRHcoug_DurM2yfm-8kPEuF_E3CU0oUqdVF5BzitzZwm2cHHaRRO5byHqVYC8TkcZI1XYyOOX0Iq7XP4rboiyXnLISxh3eRmyhQhcQhBDkhyA-BUoyO4H2Z8_UXtbg5uXNB8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
🇧🇷
فوری از رامون آلوارز:
احتمال خروج وینیسیوس در این تابستان از رئال مادرید وجود داره! باشگاه رئال مادرید از قبل با نمایندگان وینیسیوس در مورد احتمال جدایی او صحبت کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/97648" target="_blank">📅 19:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97647">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUviXAexIHm4n3z2U8CWj3s3jKLwooufYtZkVo86vldGXjxyoUWX0rbGZzLueDJPc4D07Kr6Y7SnzFLhOYNrl54t2C8bFT9_3E-DpssN1iiVU7LIRvu1z4BGfzdGzaxN8R7es4b7f6OhqZuqB6avmwnnnYwVGJUSRqu4Sl3BoNK3v_EqB9dCx9FgJQq7qQ6ylLef6jOM22dHi7TJzneGY4mv1tXypNfDdZS6Vrwuqkthk9mgUXeUsb-YNn_RnHTl6SU-35Rf46esBEik5HD-8Pm6NAYrZBixKdTPjVvRl-ipKX6ppPA2dxG1RnvDzSqsNWjF3UfJB79osMKCH1q-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فوری از فلوریان پلتنبرگ:
فدراسیون فوتبال آلمان به ناگلزمن توصیه کرده امروز خودش استعفا بده؛ وگرنه خودشون مجبور میشن اخراجش کنن.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97647" target="_blank">📅 18:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97646">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irUqvSOudRgPfcv18IbzzJ3gT4wtmNB74-fzC3bgTSyAVIBSptmnjBsBP9hFL1RU1aXGFHTiUGCB17jJlosNhbiC52fW7eI7L3oTLEeFwRLQCtvuqo3fHKDeujk0AFFfsNMHzPi_EOslL4p24IxwOheG5b3J2B_Oyj0A4KSoOuM5wtKgusmUHYzTI5u6umwY9pMb7MceHeuFFYXghpUaA0UoJ1NqTtV3BEJVjftx7tdL3_WJwhDF-H-AttIuSCu4cZdSepnyDCAuyqdm85BJgbKZuD8DMe41eesTEtwOWl5BoojLYsrdihCl5gIYPG3RGT5RfP5phbidE0tMwll48A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🚨
اسکای آلمان:
یولیان ناگلزمن در طول جام جهانی هیچ گفت‌وگوی خصوصی و رو‌در‌رویی با بازیکنان آلمان نداشته و ترجیح می‌داده پیام‌هایش را از طریق ویس در واتساپ برای آن‌ها ارسال کند.
📱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/97646" target="_blank">📅 18:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97645">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f55154a43.mp4?token=dGf0hS0SzslDND8waSRDpVwUDBi8xsC0Rx7pk8Hg4DAPPyFriM1T-eL8_xDCBnxin4CW69g_thjFlf7MUseS7v-GDuBMFSf1IsE6FxZMmvcTMN6pqIRjAssM9lPIKkoRFOgIC-IduMtGkcU_8iSiaHcauKVF0BIV8ua49I1vq-hGPZ3OtJsXI9znTUpNZYf6kW3eIbmjJaH2FKMqEwLgCt8pztkFiac3sCSqSyRDGv1uufq0-npedR1fOXDVQlE8_nBqC3Zm5hHsr5oe_fKLntaHm1p4L-jQkrzn60fijVIhQBgaVDRi_TVPmRwmdjsF_7UqyCe-zpl1jK1t7lPUew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f55154a43.mp4?token=dGf0hS0SzslDND8waSRDpVwUDBi8xsC0Rx7pk8Hg4DAPPyFriM1T-eL8_xDCBnxin4CW69g_thjFlf7MUseS7v-GDuBMFSf1IsE6FxZMmvcTMN6pqIRjAssM9lPIKkoRFOgIC-IduMtGkcU_8iSiaHcauKVF0BIV8ua49I1vq-hGPZ3OtJsXI9znTUpNZYf6kW3eIbmjJaH2FKMqEwLgCt8pztkFiac3sCSqSyRDGv1uufq0-npedR1fOXDVQlE8_nBqC3Zm5hHsr5oe_fKLntaHm1p4L-jQkrzn60fijVIhQBgaVDRi_TVPmRwmdjsF_7UqyCe-zpl1jK1t7lPUew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇾
عاشق پاراگوئه و کوهستان هاش هستم.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/97645" target="_blank">📅 18:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97644">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUDpE5Z0gqi9CiItg_g0CtGt4JnyQ1pte6HLsChSX_UbgTpA-_eRQ3mG_kjPDTpUwGAuAqspySyBaHmtj9JdwveJd10ksa3C9wF-2oNi8R8T4vjtNoeLXdI-pajAL7plDqla84it9KR8LQBsilJXM5U9WvCiFbL31sV5fKNYWHGOrUfb-lzhERKk7P55t3hd9idEf8PIjxF78hmT6m5b9P36p84Y0mMNm6-q7GnigT2N_7UoGstElR2vn_pOFiMXzoU_du3kgHR1lNfbebo4P1u7kiQLIxHTqH8qFS8zynW4KzTT3-EcXTx_F3EjiaQQabhXehQqQwsDN-W64GCvpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
بازی فردای پرتغال مقابل کرواسی، دقیقا با سالروز درگذشت دیوگو ژوتا مصادف شده.
🤍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97644" target="_blank">📅 18:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97643">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQaDtMrdCKZXwHsHbgYDBDBMg-Y62G7x4ngOMAtoOqorfa-gvcWWpf1KM4W-pLU5x7wyfm9dogTjdUTTC3dlK6DPDWPUBTjVc1lbgnOxT4KhS59gByQaipO5WrIBND-zvm05Ub_8ttI0-01O5T-ZCkXBkrKyz-mRxyvVt6x7ll9ofttS31xbtYulGBZR9sMGc1Bdt5esjbCYxE-ABAK1LCSH_TNmpH_PsQ96gHYApdN9Tuo3NnTVuNETN6KvXxACLjGG-GeZfLiDgynTmUCtg8Ynf8S4GYSZl5gXe7VzTdfawVWspvI4aiIiAlYlW1m5Gn7PyHPQn4fWns9uw2pnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇩
سرمربی تیم ملی کنگو سباستین دیسابر قبل از شروع بازی مقابل انگلستان خبر فوت پدرش را دریافت کرد و با این حال تصمیم گرفت تیم را هدایت کند.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/97643" target="_blank">📅 18:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97642">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97642" target="_blank">📅 18:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97641">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a4c734a62.mp4?token=aTik8msWZThrqUerGUpTRqfpLhol2-9UguiMHh9MSxepjrxQuXIWyl1vyQkifgXGDHUgAaHeEZkrds1sy6-HgiMFVEDCApXY8PPllnJSOVazBisQiqkkcf5i2VPVaCdG5MKGylrahnfJDPgd_iSg_KFr3GhqVqwRpxAvVhkCrk3x3_qO10qKnI-sgIH71ulJEKguClFlgWQni9e3R056LkuxsYsbg0ocnEznomvY1QGZbR4jcdwb8Htn3NM4KbYA-PrCFcvppvrm1puMOT59zhab9DjjY7SxWEdHv5G6cX5R9SdCX9J7j-tcK_z370UFRSfOo0z2hKB8GyCKRZeSlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a4c734a62.mp4?token=aTik8msWZThrqUerGUpTRqfpLhol2-9UguiMHh9MSxepjrxQuXIWyl1vyQkifgXGDHUgAaHeEZkrds1sy6-HgiMFVEDCApXY8PPllnJSOVazBisQiqkkcf5i2VPVaCdG5MKGylrahnfJDPgd_iSg_KFr3GhqVqwRpxAvVhkCrk3x3_qO10qKnI-sgIH71ulJEKguClFlgWQni9e3R056LkuxsYsbg0ocnEznomvY1QGZbR4jcdwb8Htn3NM4KbYA-PrCFcvppvrm1puMOT59zhab9DjjY7SxWEdHv5G6cX5R9SdCX9J7j-tcK_z370UFRSfOo0z2hKB8GyCKRZeSlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇲🇽
پلیس مکزیک: در جریان شادی مردم این کشور پس از صعود به ⅛نهایی، حدود ۱۰ نفر بدلیل ازدحام جمعیت کشته شدند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97641" target="_blank">📅 17:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97640">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2308c1db6.mp4?token=YT1GAEnsu-SJwiyUvgoD_jUL7cc7HBIWtZD2Mkf57DOsnB1z5qnA1U-5pqWs8hACF2uRlBALolm_a7tyc9pD9Naykr2uHm4Y-K5EhESk9n9GzkHU30WTxOktjHcF-uAMrCRItKieOfB7dNn_V931oI3I59J9vTuJsY2Tp9urBhTpYfxWbq_sE9fS3rByX2Cnu181WnLYDu3EGKV2D6ZN8xSSGfIOGpdKpFFSRhrj9pZ5r8HvhLi77Q6i75v4N2iLLCXHcEsy_F_BDNQhX35wVAbPzt9m2ZztCRUew6AcLMta8uCT6lgOL84X58hszg60lCREDHvPVNwhTlE6KmOAAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2308c1db6.mp4?token=YT1GAEnsu-SJwiyUvgoD_jUL7cc7HBIWtZD2Mkf57DOsnB1z5qnA1U-5pqWs8hACF2uRlBALolm_a7tyc9pD9Naykr2uHm4Y-K5EhESk9n9GzkHU30WTxOktjHcF-uAMrCRItKieOfB7dNn_V931oI3I59J9vTuJsY2Tp9urBhTpYfxWbq_sE9fS3rByX2Cnu181WnLYDu3EGKV2D6ZN8xSSGfIOGpdKpFFSRhrj9pZ5r8HvhLi77Q6i75v4N2iLLCXHcEsy_F_BDNQhX35wVAbPzt9m2ZztCRUew6AcLMta8uCT6lgOL84X58hszg60lCREDHvPVNwhTlE6KmOAAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طوری که باز کیپ‌ورد و‌ آرژانتین داره پیش میره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/97640" target="_blank">📅 17:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97639">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f7799c99f.mp4?token=kViICLD7LUAeKPrtjwK7TxSFLsx5wVuCSgufXHCw20DYqz2CJupSgpdZuzuTbYlEt0VTl4mGON9CFeb8L6FhjfAkoaWKSfYfPs7a22rehcqc5-83GiLUnqbrxCH1doWa1eYNxMK9lBfPDa_pNumJHDcwyR1RrluhK-LvpUXy0-aSigXMxQWqomJPVX4u7R52bG7_fW6vN4dy-mDXyVX7-U1HL_8lnH6B3u2r52tm25sGNwIU98cgQn4Q-v7NtfmDYhGNvML_2RKpHJtM_8wpB_ftlydD50ZJnVBmc6CDHW6oxjPe6QE4W2yEexf09t7eNtU8ih-Jl1vry7TF88cZ0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f7799c99f.mp4?token=kViICLD7LUAeKPrtjwK7TxSFLsx5wVuCSgufXHCw20DYqz2CJupSgpdZuzuTbYlEt0VTl4mGON9CFeb8L6FhjfAkoaWKSfYfPs7a22rehcqc5-83GiLUnqbrxCH1doWa1eYNxMK9lBfPDa_pNumJHDcwyR1RrluhK-LvpUXy0-aSigXMxQWqomJPVX4u7R52bG7_fW6vN4dy-mDXyVX7-U1HL_8lnH6B3u2r52tm25sGNwIU98cgQn4Q-v7NtfmDYhGNvML_2RKpHJtM_8wpB_ftlydD50ZJnVBmc6CDHW6oxjPe6QE4W2yEexf09t7eNtU8ih-Jl1vry7TF88cZ0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
وضعیت آقای‌گل‌های جام‌جهانی ۲۰۲۶:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97639" target="_blank">📅 17:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97638">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad14f6b1ec.mp4?token=XHrKulCgeKmwkddhvUopn-I_GAFkP82kv22FcUL4PDnzgLm-1QjcwbMfvGE11PbAS9eR9bAQ3CQz-ojDjbWVIdHxg1vGW57_dO-Nlls3w1FRY6K8i6UxFxM49AUTdMOm1h29Rwd0oCNX51WAEHRmqSupBc3lLVm7F0jY0FeC3ZdNNdkQDXTxbimtLuLVp2AOT_-5Xn0OCjH4V-3YFR7lMurJ1xJpQYLiHHQX_hCYr5CV-FixZK3rPYdRmE_lneWyrb81rV0S-OkD8bHI3Z6KAdfxU5D4KuA5uOWk0l_dLTCAqm9mELwpSY93tliiW7UZgmmpv9qZ9H9XfyxHHVo3gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad14f6b1ec.mp4?token=XHrKulCgeKmwkddhvUopn-I_GAFkP82kv22FcUL4PDnzgLm-1QjcwbMfvGE11PbAS9eR9bAQ3CQz-ojDjbWVIdHxg1vGW57_dO-Nlls3w1FRY6K8i6UxFxM49AUTdMOm1h29Rwd0oCNX51WAEHRmqSupBc3lLVm7F0jY0FeC3ZdNNdkQDXTxbimtLuLVp2AOT_-5Xn0OCjH4V-3YFR7lMurJ1xJpQYLiHHQX_hCYr5CV-FixZK3rPYdRmE_lneWyrb81rV0S-OkD8bHI3Z6KAdfxU5D4KuA5uOWk0l_dLTCAqm9mELwpSY93tliiW7UZgmmpv9qZ9H9XfyxHHVo3gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های ستاره تیم‌ملی فوتسال بانوان درباره رقم قرارداد‌های بازیکنان در لیگ‌برتر فوتسال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/97638" target="_blank">📅 16:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97637">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M16ByK_Zs-UwK2eEf3fQOxw6hvyLDD_9m6hWGUsMR8rJduFCg4_REs7zrfNS9Y5yeUGGW-DqbPd-QOCxfIhwj0RONN4vmTRRxfdQMvWmMpwDqz8rjK30MFAlNjGL5W004Gv4ffKAsFFzsFGujQUkwiwat0esQHu3HM2oIAEsMU_nQGib9GJuvWNdeFIv5IhzL2TLHeSD-5hkm_7KbcYPBl_-LMSngKHLM-NaqKAfz0jdxOuy6EfHG9lFB-lw8FacXIYTZcdUNXlSe2eaxX9MOw7gyufIHKH2EewFgNmrSKYGuoZ53dlIhA7MavJN2FrKf6Ccq8xHrF7aq_jWpfi3TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
منچسترسیتی اعلام کرد الیوت اندرسون را به مبلغ 130 میلیون یورو با قراردادی 5 ساله با امکان تمدید یک سال دیگر به خدمت گرفته است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/97637" target="_blank">📅 16:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97634">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fpMemTSf23FaHw1644-V1d5jKB5kx6bpTlg9e8wkNawGOa0D0ag4eB9yDPAjNM5VLdG_MYX3Xa6aCPhis2FQYUjSbmJkbM_gr9H9fej_zM3RzzKwexhlZpJCaOgi6YXDTlxrxcBoP-FJglYzZLbJGpnrMTXlr3i8xlcpvfBi1ha-m-Y8rB5TZYOYPGj6wCF8a6KguvwaR7xJnWTQY0nUlCW4apaGzIjLlonb0UlTyVBwiWE6s2ZqO3o8Sh1SzXp8UNf6dabJ6eTGFbPDfNhw04CDR_YrO4QCK082d6YTNvoljuaUB0-RkR0VYI85FI4MIyfSS2oXHucooU7Seuuryg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCD__zBBbgpfc9AHRz2x4_abtsFUSll9a0rYjVNzFJ3nZLB-DLsMm9yR3He-DNPsXLDWxSDO3qLs1a83sldl3sQLSHSwHxOVC9IygWnEGie6nCxSvCIttX43THqgB63m73CqKuryrHfwNy8mjo_vTU2PKvHY9xTKlYRRubdvdigT5Ehtqzsns0rwg90MbD1FuOAngFYynx3HpMvN65eENsWJtjeqy9QVcKOZhVWZZ_oncxs3BEXidtVk1zs_JYnaYAGjC3ULaisNaeC_vmr5QuIU4d3YFsKN6VzicPgQFq-nY1D6EC6xVVJpjzRt6pbKuNx5bCnYxa6oRwKrauP-Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJyO3l0LluZRj89l8TeRr3MpbmdfG7vNprOpVcAIglx0LgaINns8z0wB3l3RrnU9lrCPbefn0Y3xD20Ha9Uynz_2ofMj-DiUYaCsJSQzySbvRz0bHJs0lv0xRneJTf3jF045XybnXXAAyMN_ymhJxNZgTZzGf5Oh-tBL5klmEtCENrNFwiOfrYqZsDsNJR5sTT7z1SQygMfO4u-04ikcInMAVeQ-_kLE3ciOtxdpYtScAdJnDPo6QwDc_JS4fJ2AQJ_pteXlrZA8OW9K3DpUFEqm-R1TSz_41YS_yNBy8C_L04AToerH1HyobxAvaXGPG3VwQE8IBy6JiPi9M9I1Ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🏆
فیل‌وفنجون سکوهای جام‌جهانی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/97634" target="_blank">📅 16:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97633">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuPEp7WngtHZPf0Cya1bnpxSrbRa1bj-nHjT13DlSlFNLA4tBQ2d8HFoVtBrDnQkdbkYH5tNhJgXnVPYHhvtF8ht1RXGVsdcJidwe_TeJS_1YsBfknvawn4eDfNTmK_-5Lcn9Br8ex8QGd7_mxwtpfOlL292AUos5N1zvjyKWradMwrtPKZEbf05bBdIXVn7XJnmKufUMaH7UtnD8jiyKdgNXWkNVs5rx4fc86S304Ca4C1hVUkqTxMcNHXlc-maKkCT68Ehih66wBWmfxCmwPJBtspdTP49cx8TBh8mx_mZ982-xUrYxAr6PyUYM6zhTOAGgUTJtWdRoEyKR86RCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
عملکرد مکزیک تو بازی های اخیرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/97633" target="_blank">📅 16:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97632">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gvCgKycss72G8mbHNVeiJxcroku-6jjbBvXlmuZ8_pC8cJZy0nW6GzO2cwmTMJ7Bv3ZFm1JqKcA9mWfnLjy1CbbpkH2WeXB8EF_EdN3X3P9Po_5PTKoSZK97Q36TQx3ta8QhlrB_KigoylhLIUQx9ergt177_movSI5sDPj3IVPOpHSvAKeZGT0vWDI1hG6iXb6ArdOHpIEb-FTrocBd3BEVTzuZ1AyMyBYZRI3v7cPUkQ1tL7s9vKt1hhuZEjn9PoOqrdJdioq7Pcrk64_IM27jl9bz6gXRCfjyVAnQ2JzdptiFnBcC6NVw13L8jBYPzPpANZpCzyEfVNg1q7l7OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تام‌الاختیار مدیرعامل هلدینگ چادرملو در باشگاه با انتشار تصویر خبر «آسیایی شدن چادرملو» در سایت‌های رسمی فدراسیون فوتبال و سازمان لیگ ایران نوشت:
طبق اعلام این دو سایت، چادرملوی اردکان آسیایی شده. آیا کسی منبع معتبرتری سراغ دارد؟
با استناد به همین منابع، تیمی که در زمین حریفانش را شکست داده، به آسیا خواهد رفت.
ما به زودی تیم‌مان را مهیای این مسابقات خواهیم کرد.
مطمئن باشید از حقوق مردم اردکان و استان یزد، به هیچ وجه نخواهیم گذشت و به هر تصمیمی غیر از این هم واکنش محکم و قانونی نشان می‌دهیم.
مسئول جمع کردن این افتضاح هم فدراسیون فوتبال و شخص آقای تاج است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97632" target="_blank">📅 16:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97631">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1f0184f6.mp4?token=KH11pu8NrrvVAlExUWsurYJUfp-Jr_D0i_b7LBSEXRQjII9zFaty3V1VamYzC-1o_cMq5-lQ8Q3WkkBV53HtIHbxiGDlcDnCRpuXofKO2e-45wf7-vD3UEv1eYx5KfWpGvpk_xmTvtHHHJmGoiB83wcDk-5eQlFSI4QWb2VrWdoSzW8GhA55avpQastybXrLEnDqqn1Ie_a2HaUAv_Q2KR-h5RwiDLSBpRWZUwFLly5ZCpNKa5ePXwp5vjWhw-5rz51bu7ONhrFQ4UiuRGND5ZMsYG4BCHj5yLC5QwPSTNyCkUui2VgOv8lyo2IbHLVzbz2qLAs66HM3W6IYNVUJPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1f0184f6.mp4?token=KH11pu8NrrvVAlExUWsurYJUfp-Jr_D0i_b7LBSEXRQjII9zFaty3V1VamYzC-1o_cMq5-lQ8Q3WkkBV53HtIHbxiGDlcDnCRpuXofKO2e-45wf7-vD3UEv1eYx5KfWpGvpk_xmTvtHHHJmGoiB83wcDk-5eQlFSI4QWb2VrWdoSzW8GhA55avpQastybXrLEnDqqn1Ie_a2HaUAv_Q2KR-h5RwiDLSBpRWZUwFLly5ZCpNKa5ePXwp5vjWhw-5rz51bu7ONhrFQ4UiuRGND5ZMsYG4BCHj5yLC5QwPSTNyCkUui2VgOv8lyo2IbHLVzbz2qLAs66HM3W6IYNVUJPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇵🇹
تصوری که پرتغال از بازی کرواسی داره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97631" target="_blank">📅 16:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97630">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f836625f.mp4?token=mF37VE734kQTE5gfbVg3Gy3WpQ0Y-AW1NfZOIKc5VNMoJ9FBD9A8htnorp2yjiCZ2WGCMbnCjKf_I4gzfcbRox515bdo7XAJ_ZofVZwVe5w9dl2_qHJ23noV81vPJDOHn8n_qgyYBSZY4zCNAW6bJuPFjtwxWtw8dnNCsZLoi5XnuIBrdxfCceOWA63if2dQeMGAtvAHAfRh8UrkZApVpu0-_BGmm0z1qmSits3H4eEjwk6Obj-v_v6QWO4sgQrgSywErrgH1QLviqOmPBcrY1MGIpXDRim_iT_NpTgA50yNtTZ7EyDvlFglDf1V4CRBXP-RMBAfVwiTzS62WFkSYYcRkqgU8tHxXruhFtKdx5VB8TZgjGlIvAGk5Y_h-3cqlxFGik4aa7KpPsHTUnTa5vr9StRfXZZsX7suRm_GGSesm-8gcFmk951lbBk6j-fMiAfwET_mYOVYPcO99ir5JuSQpOaOdky1x2iDeFF3AKbaacHwwFQRUm9pig7h2aL0SQEMCBVLqiY9ceSdIFg43PUyp2tMJRTe3-29ii8Ui_Ej7k2uIPCM52DX8qt5HA_8mWWlRXcZ7iYiVt-gnmqtOe7JHeU71jRpawx8GVaATTNJHBlGvRhsOBku4RIaJWQAnmu6iJ7pLvK-9ubfjwTT83XJcbTb2dEUDO5SPfgWeyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f836625f.mp4?token=mF37VE734kQTE5gfbVg3Gy3WpQ0Y-AW1NfZOIKc5VNMoJ9FBD9A8htnorp2yjiCZ2WGCMbnCjKf_I4gzfcbRox515bdo7XAJ_ZofVZwVe5w9dl2_qHJ23noV81vPJDOHn8n_qgyYBSZY4zCNAW6bJuPFjtwxWtw8dnNCsZLoi5XnuIBrdxfCceOWA63if2dQeMGAtvAHAfRh8UrkZApVpu0-_BGmm0z1qmSits3H4eEjwk6Obj-v_v6QWO4sgQrgSywErrgH1QLviqOmPBcrY1MGIpXDRim_iT_NpTgA50yNtTZ7EyDvlFglDf1V4CRBXP-RMBAfVwiTzS62WFkSYYcRkqgU8tHxXruhFtKdx5VB8TZgjGlIvAGk5Y_h-3cqlxFGik4aa7KpPsHTUnTa5vr9StRfXZZsX7suRm_GGSesm-8gcFmk951lbBk6j-fMiAfwET_mYOVYPcO99ir5JuSQpOaOdky1x2iDeFF3AKbaacHwwFQRUm9pig7h2aL0SQEMCBVLqiY9ceSdIFg43PUyp2tMJRTe3-29ii8Ui_Ej7k2uIPCM52DX8qt5HA_8mWWlRXcZ7iYiVt-gnmqtOe7JHeU71jRpawx8GVaATTNJHBlGvRhsOBku4RIaJWQAnmu6iJ7pLvK-9ubfjwTT83XJcbTb2dEUDO5SPfgWeyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های بامزه نعیمه‌نظام‌دوست درباره خیانت پیکه به شکیرا
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/97630" target="_blank">📅 15:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97629">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsDCMOyoxPQOv90uXppXtcoySJApt-LjpAyEVNMv30CSfUvtEqyY_8x6SlguVV6C83TVjURnm_laHG-uofAt0pMPCzd0fPfvaXPdm2T9dnzk0t9B_NXrLyENUPCFOY_ASVwnojNjAfeg8HFwqWkz792MiLxXq8hDdkMFO5SoRjJsT0W4j9kbTWtT84ATp4yFiYgzGpiTohwNDEGoGEt6X5_R-8lZddaF80t_5DIerPrfKor71GVhs25kppU7ofxIRpXL0UL8Np1I2xxoLI-3i9qymc_m6h5c1ioYVUQJr7-Ydmjmir3r70Tm0UPLmvf8egMNJ0naq87-O8f75oYKoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
تیم ملی آرژانتین برای کل مدت حضورش در جام جهانی، ۵۰۰ کیلوگرم گوشت با خودش به محل مسابقات برده
🥩
گوشت‌های انتخاب‌شده شامل این موارد بودن:
💥
فلنک استیک؛ فیله گوساله؛ اسکرت استیک؛ فلنک استیک شکم‌پر؛ پیکانیا؛ ران گوساله؛ دنده گوساله؛ ریب‌آی استیک؛ استریپ استیک؛  تری‌تیپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/97629" target="_blank">📅 15:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97628">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29cb7614f.mp4?token=cX_OjZNU6P-V9e06CFMSKpVinMEg2Wu7JxuXGi88ZZI-SdN432bodnToNaNfo_AdD9IHB9xxFHe7a2nSQlF4Deg6xkCK5lJKLhDP859WU9uVAdOUVjs05Hy0rVccvSoXyhTUooWIpS3FtIEPbyhI50AJzBRfDjbnpuoOW_r9apNygBcsu5mN8o0Oe8Bv55_V7-hGwTJNXR97WWJaGJSxlf8s9sT6MuGISOJJafjgQNZpkbR0POMEszIfu4v1xOnhUALj1HsM-_h-f3k6vTEa6VwYRfZcCVC4HMtj1qFDBYOTcBCPv7KFLSs7IsZYFysgs_90dcA4VZT8BNS0hB2VJSCTFoY-9ioiSOWMs_PO-BjolTCDbB_YxOGgRIf8UfojKXKB9xOI0FpKhJmf7qEClP53o0xcHw9nawJRu4UgJBXu5zUntZA6Y9EIlEJpCYGaU5MsH0e-B--CF-jZ5dRkT_VYA9eS0LU16__59kUTurbE8JwUWLNHW-gprbwM_q72NM3yc1PEyOrE2zS9jJZhu6DDGJHiW6oJM0px8v6dzraLWYyYLIdneA7KQ72fjJu-EGgFtvBHtQ6UdyMV6JP-4Qpl7bDBVzrtPCTLGlCJsFZEGU5sf3AVM57jBw2zRVa6wyedgsRWhqjeuJut9-zHlsfS9GxiLqhXrfUu8Pa3sZc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29cb7614f.mp4?token=cX_OjZNU6P-V9e06CFMSKpVinMEg2Wu7JxuXGi88ZZI-SdN432bodnToNaNfo_AdD9IHB9xxFHe7a2nSQlF4Deg6xkCK5lJKLhDP859WU9uVAdOUVjs05Hy0rVccvSoXyhTUooWIpS3FtIEPbyhI50AJzBRfDjbnpuoOW_r9apNygBcsu5mN8o0Oe8Bv55_V7-hGwTJNXR97WWJaGJSxlf8s9sT6MuGISOJJafjgQNZpkbR0POMEszIfu4v1xOnhUALj1HsM-_h-f3k6vTEa6VwYRfZcCVC4HMtj1qFDBYOTcBCPv7KFLSs7IsZYFysgs_90dcA4VZT8BNS0hB2VJSCTFoY-9ioiSOWMs_PO-BjolTCDbB_YxOGgRIf8UfojKXKB9xOI0FpKhJmf7qEClP53o0xcHw9nawJRu4UgJBXu5zUntZA6Y9EIlEJpCYGaU5MsH0e-B--CF-jZ5dRkT_VYA9eS0LU16__59kUTurbE8JwUWLNHW-gprbwM_q72NM3yc1PEyOrE2zS9jJZhu6DDGJHiW6oJM0px8v6dzraLWYyYLIdneA7KQ72fjJu-EGgFtvBHtQ6UdyMV6JP-4Qpl7bDBVzrtPCTLGlCJsFZEGU5sf3AVM57jBw2zRVa6wyedgsRWhqjeuJut9-zHlsfS9GxiLqhXrfUu8Pa3sZc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
جیمی‌جامپ‌های بازی دیشب از این‌زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/97628" target="_blank">📅 15:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97627">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6859ad42ee.mp4?token=bVJzPvMg7TK_wQCVjfSSDYpWh14Xz47hws5k9CKM3TtGNEtgTsrF9wJ4_cJJVjpQA0tbVf7vlU-kHnMoz4-gHYZMj21uYI06XTqEk9UFpeouLQES6JysLUKuHdJJKcfSmuglNeJK2o03f_FnIZddX1mJpggm6StDqbf48Yy2ZRZS3pYrTstJU0pf3sHolHEQtl_W2rsnCCzO-xSNRbtV-q3hggpDNwlvrDWQlCVaA2yKq_cF5KPe0FLkljkmmdHEIRq6-VT8P2XQG4rW0nfzPRR98ZqMBVddCJhOPkl3KNBGZop6l8BjLvF2Gmb6aabxo0hyVZdZT5gulZg6_RQkgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6859ad42ee.mp4?token=bVJzPvMg7TK_wQCVjfSSDYpWh14Xz47hws5k9CKM3TtGNEtgTsrF9wJ4_cJJVjpQA0tbVf7vlU-kHnMoz4-gHYZMj21uYI06XTqEk9UFpeouLQES6JysLUKuHdJJKcfSmuglNeJK2o03f_FnIZddX1mJpggm6StDqbf48Yy2ZRZS3pYrTstJU0pf3sHolHEQtl_W2rsnCCzO-xSNRbtV-q3hggpDNwlvrDWQlCVaA2yKq_cF5KPe0FLkljkmmdHEIRq6-VT8P2XQG4rW0nfzPRR98ZqMBVddCJhOPkl3KNBGZop6l8BjLvF2Gmb6aabxo0hyVZdZT5gulZg6_RQkgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ژکو داشت مصاحبه میکرد که اونور زیادی سر و صدا میکردن یهو برگشت گفت هیس همه ساکت شدن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97627" target="_blank">📅 14:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97626">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAlTaJ_QN280UjpuRAXsezSmtHE8E1jTLa88PAu2zk1Cd4zJns_HeNjOy5dhpUHyCjDf8hH7RX_hrtg--SKM85zfevf3N_SBh-QVF1g__Liz7uW26l4RQoARI9dMMad9XhuYp_tJkJGmvnPOGqbBNLTBj6UM5UiB2mcpn-FgpR0cIqJe57T1xGVPvd4n0YMHSJgnxkQ_IxqUqkBahzk2hZZ07_Z2mBG50mDSrgJvxZdR1Rjewq3-u8qwSDqodF6tZJXLXy4RDuRBT1zvOe7TCHO6xP-qTDz8FnAOQd9bJ1Z3gVaYvFg2V5JRRCGRfJ3mF_V8NAr_X4TOhNpKiZ69_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97626" target="_blank">📅 14:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97625">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41d7e1df1.mp4?token=ebe_YJUEnHkatq6DQ7XQojUVhA9X-RuGlzWftiYwdyzINQygqb2Df12G2KvXELuQe8hyJ35_dQmkTFDUF27VMc0MpMMtG7Ac1ViWuWrpSLf9QKfXVCWlhdGYYYfGCZiE9oFBC92O6J8-tQUUBKn4GS_3qfTj1jbFPNluzF3unr9pQTKcupNPToXdl8DS01AMxHeapgNnYWFDcP1CfwLGfpd9d4L4AxURIVegvFgZoBq_ns5l3-lMsqNT8Aeh1BLEMATkwZ4Rbu3BIS7Qws4N1URjbKHRv0YDbhwTDfG6vriFN9R1OR7wMTeWYs6_EE9-tR6rPMDv0PmWpLa_0fo5cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41d7e1df1.mp4?token=ebe_YJUEnHkatq6DQ7XQojUVhA9X-RuGlzWftiYwdyzINQygqb2Df12G2KvXELuQe8hyJ35_dQmkTFDUF27VMc0MpMMtG7Ac1ViWuWrpSLf9QKfXVCWlhdGYYYfGCZiE9oFBC92O6J8-tQUUBKn4GS_3qfTj1jbFPNluzF3unr9pQTKcupNPToXdl8DS01AMxHeapgNnYWFDcP1CfwLGfpd9d4L4AxURIVegvFgZoBq_ns5l3-lMsqNT8Aeh1BLEMATkwZ4Rbu3BIS7Qws4N1URjbKHRv0YDbhwTDfG6vriFN9R1OR7wMTeWYs6_EE9-tR6rPMDv0PmWpLa_0fo5cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم ایران که نصف شب فوتبال میبینن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/97625" target="_blank">📅 14:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97624">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koQOvvvSqC6dSymvRgWPHvf4gOblUWOCVRzSvjsMZhacs80hWpV4s7emeZ48q4CUjp68XH_HNVaN6kAfRo2sXTfbLvtXA-uLfckpatbQr9pzxO8GzU0RPAp__2-aW0dZ1mhuG-KULblsAH-NMhELeeBo-9y3b30ATiietZXO2rkoF1PbknWaqntGdPYKt-bHSRdPfrWNLcVHBnzVic56SA1jmj6cN5kWwzx5vSpvWjlcAY195e2uzFilDeeCphSUphGBf5JLGGMj2DlwDN8gyHfkp9QpnMq4GVb5fTUA8QYZX269McnVegxkwKH_O3mIGZihaBaBd-P9gd-j2BreyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
علاقه رئال مادرید با انزو فرناندز:
👀
🎙
خاویر پاستوری (وکیل انزو فرناندز):
چه کسی رئال مادرید را دوست ندارد.. من حتی آنجا بازی نکردم اما الان در مادرید زندگی می‌کنم. انزو همچنین دوستش (جولیان آلوارز) را آنجا دارد و بیشتر اوقات فراغتشان را با هم می‌گذرانند. و جولیان هم برای انجام برخی امور کاری به دیدنم می‌آید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/97624" target="_blank">📅 14:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97623">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6470fe1aae.mp4?token=TzLMrOi22wASZb_a0yBa8IY_zZjqLATcYy6056VTuLtYbOq71iHgW6p9Rd9Yq0aOz6FV65x5pq0Z2Z88Eu2sRQtAN5NG355dWWL7lEabC4q9HMtn003vcFcKguLriDqaEOlXfV6vg2vNscRmo1llYPYd8s3Tm5l21Tb72wyBap_B4UduWW32VUNMAPdt2FjAghYP1cTBc3V1vVdNw0PNBeKeKhCg_6nuC5DgpFgjaU62DHUmmiFXzO1DjOLnaVgYagdoSGUqLi58aPNMC3sXdat6I1SdITpaw9Qt87leFAYsYwLvcdD7bqjWsTx_qFqmiLbdsn2LJNzVamWkX8xjdhDzXPd_744tcdv3SsBobLFQb3nh83EMUFyJhNDdw1FgpOCAU8kmlxNubf7mrG79pZMd4pWuYRUEdpodo_3oBlXn7kQqVGH0rv2_JH0zCEFxKYZ4MZjCLD7vGpoW1ntpgoWDSlX996m0t8yJgZ9b4NIMHES0YrpB9Uku25JAbN6ZboILL6hU_DsazhNVTP9k9Vv8gRMk5achz6Zo1wfuccbg4ngB20MH2nrt2eR5KDEf9ENfotyezmXh48BvVaaNunGUHAr7wMi6HKWrba7UOxvDAXmSZLaHIUGyePdnBIKeFovLqANple0hmXvJDeVl1ajPLRAHwC6A0-FNp4zJMEI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6470fe1aae.mp4?token=TzLMrOi22wASZb_a0yBa8IY_zZjqLATcYy6056VTuLtYbOq71iHgW6p9Rd9Yq0aOz6FV65x5pq0Z2Z88Eu2sRQtAN5NG355dWWL7lEabC4q9HMtn003vcFcKguLriDqaEOlXfV6vg2vNscRmo1llYPYd8s3Tm5l21Tb72wyBap_B4UduWW32VUNMAPdt2FjAghYP1cTBc3V1vVdNw0PNBeKeKhCg_6nuC5DgpFgjaU62DHUmmiFXzO1DjOLnaVgYagdoSGUqLi58aPNMC3sXdat6I1SdITpaw9Qt87leFAYsYwLvcdD7bqjWsTx_qFqmiLbdsn2LJNzVamWkX8xjdhDzXPd_744tcdv3SsBobLFQb3nh83EMUFyJhNDdw1FgpOCAU8kmlxNubf7mrG79pZMd4pWuYRUEdpodo_3oBlXn7kQqVGH0rv2_JH0zCEFxKYZ4MZjCLD7vGpoW1ntpgoWDSlX996m0t8yJgZ9b4NIMHES0YrpB9Uku25JAbN6ZboILL6hU_DsazhNVTP9k9Vv8gRMk5achz6Zo1wfuccbg4ngB20MH2nrt2eR5KDEf9ENfotyezmXh48BvVaaNunGUHAr7wMi6HKWrba7UOxvDAXmSZLaHIUGyePdnBIKeFovLqANple0hmXvJDeVl1ajPLRAHwC6A0-FNp4zJMEI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمجیدهای زلاتان و مورینیو از ایران فیک بود؟
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/97623" target="_blank">📅 14:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97622">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/un7ldE6mFKyG6hwiiYLLWs4twH3mnBh5zx1p3xWbl7HwHIbxaNOSDNc8r914DuRNNOFa8-PsFBTb018M043lQtYOfOC4eC546r5Nmak-stxz9Dx8TyA4dzgk5b-ThUx4AtGyr-srfeMpBss4b4kXf4TCf4KFJTD3INFi8fEAho7kt8SjyCP0ng8YN28q9_ees1rIZhfQEgwF67P158zl0I-fJvbWztWvej7yD0wAkPuOlrEG_vvWt2Ej-e020F1zo0bDmZ5l1dKj12ok0UuLUe29a7fQtoKL7S2DBabJyKRTR2vs_tDygF7THME2LFtCyApc8i1lkbQLdYj-3kkznQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇳🇱
#فوووووری
؛ ترشتگن با عقد قراردادی به تیم فوتبال آژاکس‌پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97622" target="_blank">📅 14:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97621">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl0sQXYgrPaV71T2132nZeEhIiQv_l6lzpx2k3s3JZqzg3dQ81dnQ_pbyCn_h5OM9a5X4-Peoh29HVwozEgKkua0mR-8NBlIiL7NBZiRl9cpLujX97vCaJZ3VXDleqRA560RoyHP7Ysk-d0n8BIgDI-QEGrRxa7ta2901Hon1xoI4bK7Dn5SdNX9ID0ygRX5PXbsKbT78u6pPcQtA6tKRBQdub591pV-4x_RqWEwykQLRz4pBhM97TL3KtdFOSFK5tjbEsADUisidkZ4jANRATgpcT1rmxoS00pLTLsfq2wCWtXYEYHQ3orNG-Zvfhd16MwH_ps698hEaUZQ22zFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
#فوووووری #اختصاصی_فوتبال‌180
🔴
با تصمیم نهادهای امنیتی و توصیه به ارکان فدراسیون فوتبال، امیر قلعه‌نویی با توجه به فعالیت‌های اخیر در دو سه ماه گذشته، روی نیمکت تیم‌ملی برای جام ملت‌های آسیا خواهد بود و خبری از تغییر سرمربی نیست. این موضوع پس از حذف ایران…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/97621" target="_blank">📅 14:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97620">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97620" target="_blank">📅 14:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97619">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2f0deb63b.mp4?token=ThGgp30V5E64CIPfsizivfocgjRZiz1lUBeZ1HZuovVmSm3WpTrKsqRHls1P8kwIyBVqgGboVSUECuZCs6bfYpIXrH5rbiQJNoQsXEv2ABAyMEVMpnLjcXLaMEGuTXEiuc-41pVWACd3BOuboP9-KBYAVZqpjt-wA_4bqGG-2JqQQ3E6AIALM1U32ZhEw-_fosKrOKGJ_Ukmlf7g-zNw49ucUNVAXgo0pywYBV-m79svVkbc5SM3hT0prxm6txAXfqZ048ei_kZ55BtpXQAqUDmSpAMkLuyOAB1vkuLRDhwYH3ytiUKnELkeNLgJh36Dux4zNy-TbI-jzkcDBCqYvrX6GmM7jeU5wx1-eGCz4rVIZ3S3ChLLUvIYVeAKreldOv9QrrKUt46qXnE7SDohr_nH3zkjHWgBgq2I8k4AuvVEU2x0JrhxJjdPvuFblRj7vMGzI5hSchXFRXPTPrjAuYRErifMBWQCe_KdwQz3U2kOcfAjFTxjbk6Y7Tr_Gz1_PWYGGkvcHRJIEvnrbs2IfTnlnsz5fyASH65axAKetpkiKtSrya5B64ZqpP1b5FkdC_4rCCBA91GBP7DcV31sfhYUwtA7SWWzpEzt5AmeqOyYWrjO_cD00WrI6_FiOc6upgPtF2hQ7etZaH8JPYdPojFR0MfHJt3iLdTbqq8ADxE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2f0deb63b.mp4?token=ThGgp30V5E64CIPfsizivfocgjRZiz1lUBeZ1HZuovVmSm3WpTrKsqRHls1P8kwIyBVqgGboVSUECuZCs6bfYpIXrH5rbiQJNoQsXEv2ABAyMEVMpnLjcXLaMEGuTXEiuc-41pVWACd3BOuboP9-KBYAVZqpjt-wA_4bqGG-2JqQQ3E6AIALM1U32ZhEw-_fosKrOKGJ_Ukmlf7g-zNw49ucUNVAXgo0pywYBV-m79svVkbc5SM3hT0prxm6txAXfqZ048ei_kZ55BtpXQAqUDmSpAMkLuyOAB1vkuLRDhwYH3ytiUKnELkeNLgJh36Dux4zNy-TbI-jzkcDBCqYvrX6GmM7jeU5wx1-eGCz4rVIZ3S3ChLLUvIYVeAKreldOv9QrrKUt46qXnE7SDohr_nH3zkjHWgBgq2I8k4AuvVEU2x0JrhxJjdPvuFblRj7vMGzI5hSchXFRXPTPrjAuYRErifMBWQCe_KdwQz3U2kOcfAjFTxjbk6Y7Tr_Gz1_PWYGGkvcHRJIEvnrbs2IfTnlnsz5fyASH65axAKetpkiKtSrya5B64ZqpP1b5FkdC_4rCCBA91GBP7DcV31sfhYUwtA7SWWzpEzt5AmeqOyYWrjO_cD00WrI6_FiOc6upgPtF2hQ7etZaH8JPYdPojFR0MfHJt3iLdTbqq8ADxE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای مکزیک از فوتبال یهو سوئیچ میشن رو بوکس؛ لامصب چجوری همو میزنن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/97619" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97618">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJ6pK0I_kW21hWcCjMnywzd7vEw7RL9E3WW_PT7SLHk0Dsv2cg-s3O7frpkLls5xfbAEd0tWy1Y4AqpwYpPJEd7lxdffhGkLrEnZEncME3Ya2_cvH-7sCBLeeKR8-rtaNTi9Lrx5qO5otXsZgWQNySemJdMmAI9YqP3xkftxHNQp18Sy-atT9UuhoWEMaWB2yVJnWqq6kOfFFsR37Lco87drBRP2xOAXxEx8pqW-Y4lQ16DX5dO2haEDKLI_OLWIwPfxyTdu80KLVICIGTY1d-FKUHSasIBP9Rv9LYpEThl1fkYctW1f_eYLCh_g3XMPt7a4yeN58Iz0O-5eRPWHIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی کازورلا از فوتبال خداحافظی کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/97618" target="_blank">📅 13:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97617">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAp_-NQlJya52TjTrAqfmlD8Jy0ZTiaC5n3RO4Z-Ev_4NPhrnlG7sFJXoRBP3_0NnvBonsargucghoymRnhi7iAvJqF-AZ6ohPN1CDgtm4PQK2VnzpgiO81Q3GOQcjp7VX7tdZBkh0QOyT-uORTBO0iuuydg9tNtsJC8DjXRj2CTsqQDrktHKtyENSNnumZJGqcJ1KZaO2jVk0BNs1IrBk4sOdAIrBtJOXVkuSDXWIl0amQ_QqCAXG06xJlCxR_O6SCAgmpouSWpXw3lCszy8hl0sFvPFU1s0hm2n4z_3S-apUG06azs-_EZFrOG8yKJu3V7JgovKc2OIAq809tOeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
🔥
مکزیکی‌های جذاب در حاشیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/97617" target="_blank">📅 13:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97616">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e7dc94b5.mp4?token=OEl-MUQ3VwKSdyBBe2SjHN3T3KMD4AvKxy-L_DuzZgI33hMfsJWZjGx-7AiSsb5iq0BB-Ern108di3zbaGHAYdocjgEHkyTgu05gQT3v2gJqX3FbOFzZyH_P-QbZlSmrDXt2jCMiJT7STRLv_LcN3ubJF7avuGytMLVSmmbv_2oArnNfgZxXgJsDx-brMH3ysDmO528eu2Mw5QOZ1DSOh5XEIYe8Y532IwwONXQSwENDRyogSaL3RkXuxn3g9gTnMOsxfGLn5bsHTGFcAg3rHEWBnOF37kx2bhn0VK4kBEsEkgp6vvj4clJTNNVA4c-0wZOhgB_TcIJHHvET3e-Zcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e7dc94b5.mp4?token=OEl-MUQ3VwKSdyBBe2SjHN3T3KMD4AvKxy-L_DuzZgI33hMfsJWZjGx-7AiSsb5iq0BB-Ern108di3zbaGHAYdocjgEHkyTgu05gQT3v2gJqX3FbOFzZyH_P-QbZlSmrDXt2jCMiJT7STRLv_LcN3ubJF7avuGytMLVSmmbv_2oArnNfgZxXgJsDx-brMH3ysDmO528eu2Mw5QOZ1DSOh5XEIYe8Y532IwwONXQSwENDRyogSaL3RkXuxn3g9gTnMOsxfGLn5bsHTGFcAg3rHEWBnOF37kx2bhn0VK4kBEsEkgp6vvj4clJTNNVA4c-0wZOhgB_TcIJHHvET3e-Zcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ما تو ایران چه کار خوبی کردیم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/97616" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97615">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjdUZEE24Nod2R8H3pI1GDE38MadHzn31SL5uhXarwmq02ZgKPR9Reb5_NdFu5Wg1WFs_Le8v3r0BHY2lYjOLyz9eTyRDIsYEKq4Jf-_bcG1hm5ADMGU1dKQqSGP6JmuHXd8LGYxCZAoknx13OYdAM410JJFJdCx1DZQc3nDfuvbgW1XT3Hlq0hvHoSlpky3dHdWZ4UzA0XU_SSahM8lrpM_2_W0NpdNTMXKl2EHyrBdkF_yQsJA3wUT5F8e-q8xgA4adjijqT3waNFCPgUQZsqD5J1OenWBD4TPeKsOKXX_WtkSrzBoPrPy97VCTgL3DhsXMhz4OmuSEtoX4RTusg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
از حواشی بازی مکزیک و اکوادور
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/97615" target="_blank">📅 13:02 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
