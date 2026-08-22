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
<img src="https://cdn5.telesco.pe/file/C4yyA_OGXzxTMD1TbEaZwocKFwSyDm-JML8txVZlMWwPQx41CX0TvJCWT1QAafIgJWrG-bUTKgRTaPFat7Ulkam3wnCWNuOC3CuSivyRS85_AqxCmWZ5XTXNsmNk2zhxnhGa4cf7LRRkNPSt7mAmodJQfhouFU6o0d9QTbW8xGJyPKrz6FPykaVfzb5-U2wPWWml-xTfwquAun_X4CtsrDguOmtf58u18XzULFi9WTEMDjZSQx_6ehwLLSwy5yfU4iWw0NW2KOi0Nvt05bItTFxSZK4PU-_-x9a8Dqghx_McmOQ_ts4QHQNOsNipWxlaG62xpdI3aPBRWM32AJBbnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 450K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 15:50:14</div>
<hr>

<div class="tg-post" id="msg-104368">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc446632ea.mp4?token=HhEpvr9VxH6e-0V5YzVMEeXgCb0UBS6NmtPhqpAJ8di_9M83l1tfY-zU0KAIO_RKeQNeVJv41ljE_giOzrQryG_VJtFG1HxDJfBgJ9g3C0bcHY1IzE-DgNrDYkzsl6Qy06WiCgu_7GTNvQMV2XOW82tR7GlputCjiuuh9OBJXdYK4OUoHrOgbXfe_1zSp_XWD7_1slpq9NzOBmoaIEI0sIVdt22UefT6XyrwX_sBkolHSwIfCpsIwPNQWkbDp6uBxH0YDZr2Yy_Iq8eH5Y7zmGUJDN8XMiDBC_EexUUH1__tSePPSIYR4Jfc41eS4Te5gZ05LHhb2FT-nrLXRDw0Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc446632ea.mp4?token=HhEpvr9VxH6e-0V5YzVMEeXgCb0UBS6NmtPhqpAJ8di_9M83l1tfY-zU0KAIO_RKeQNeVJv41ljE_giOzrQryG_VJtFG1HxDJfBgJ9g3C0bcHY1IzE-DgNrDYkzsl6Qy06WiCgu_7GTNvQMV2XOW82tR7GlputCjiuuh9OBJXdYK4OUoHrOgbXfe_1zSp_XWD7_1slpq9NzOBmoaIEI0sIVdt22UefT6XyrwX_sBkolHSwIfCpsIwPNQWkbDp6uBxH0YDZr2Yy_Iq8eH5Y7zmGUJDN8XMiDBC_EexUUH1__tSePPSIYR4Jfc41eS4Te5gZ05LHhb2FT-nrLXRDw0Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
▶️
این ویدیو بسیار کاربردی برای زمانی که در باشگاه، دستگاهی برای تمرین خاص وجود نداره و باید از راه‌های جایگزین حرکات رو انجام داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 304 · <a href="https://t.me/Futball180TV/104368" target="_blank">📅 15:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104367">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0deddd0d6c.mp4?token=ZpvKUYq15MGih6olatWyDRbhFlZJKfWFgPBx_3-7Ww4L51s63Q7RF-l18scxMTnyC8sRCApyiAP4mueFVr2c-0_T8B9layP0zHfCLVldBOd7t48Iwnx5RvhfPZfEuwx4YcWY1nd5OAEZp4jeEb09nGEzDNVyzXlZgOW85vuGHQ97cDM9L6cliltAeaHvlaEynckLdoWrybsYxhrpcoIyDSazIBm8oI5ZzaubS_eh_DTybcwtnM7g9Lpq86w2vuG6saApHoi7A2WGiTSXwkV83lUhmPs3ZYYD013L2dkVeahHg1xGEib2YhXn5BneMNEI_0Zx9HWw_jqVDwJeW8O_5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0deddd0d6c.mp4?token=ZpvKUYq15MGih6olatWyDRbhFlZJKfWFgPBx_3-7Ww4L51s63Q7RF-l18scxMTnyC8sRCApyiAP4mueFVr2c-0_T8B9layP0zHfCLVldBOd7t48Iwnx5RvhfPZfEuwx4YcWY1nd5OAEZp4jeEb09nGEzDNVyzXlZgOW85vuGHQ97cDM9L6cliltAeaHvlaEynckLdoWrybsYxhrpcoIyDSazIBm8oI5ZzaubS_eh_DTybcwtnM7g9Lpq86w2vuG6saApHoi7A2WGiTSXwkV83lUhmPs3ZYYD013L2dkVeahHg1xGEib2YhXn5BneMNEI_0Zx9HWw_jqVDwJeW8O_5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
هیچوقت این مصاحبه تاریخی مدیرعامل ابومسلم روی آنتن زنده با عادل فراموش نمیشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/Futball180TV/104367" target="_blank">📅 15:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104366">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b033bca880.mp4?token=aKy5ZyXrSm4dqDDTuhjEWqYzzaDtVTsaY7sqa8Y_sWQsjVinen212OEgu2emVewbGk15zKYoMBX-3SCM2qoEOEq4Cp3-ldO86KNFM--NyUxGey52LpN4Q3gOxIB7jOdD7lyfj1Lx4h25hG8jcUecmzxrCfDprLLUYyzphjY2CUBzlwH3MICI6rnDe57V4Lz5d2qixYB8lEkKV9hsSD25kHcxK0eo2Tiz3DNUFg3OOBHypkGo5GHFupHgwXBVu8DbrGFs12t_Un7P-QPvmiPUSXRxeplAdVhnulYNN-glh6lO0X1y2EwLBgDhRLcuQL6OGewo-84AzJ4Kj0kPjE0kjoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b033bca880.mp4?token=aKy5ZyXrSm4dqDDTuhjEWqYzzaDtVTsaY7sqa8Y_sWQsjVinen212OEgu2emVewbGk15zKYoMBX-3SCM2qoEOEq4Cp3-ldO86KNFM--NyUxGey52LpN4Q3gOxIB7jOdD7lyfj1Lx4h25hG8jcUecmzxrCfDprLLUYyzphjY2CUBzlwH3MICI6rnDe57V4Lz5d2qixYB8lEkKV9hsSD25kHcxK0eo2Tiz3DNUFg3OOBHypkGo5GHFupHgwXBVu8DbrGFs12t_Un7P-QPvmiPUSXRxeplAdVhnulYNN-glh6lO0X1y2EwLBgDhRLcuQL6OGewo-84AzJ4Kj0kPjE0kjoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
لحظاتی با لائوتارو گزینه احتمالی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/Futball180TV/104366" target="_blank">📅 15:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104365">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9536e07d63.mp4?token=Gt8nb-qAJJXkANMa_pDbOYLpY5vkcbGV2ASXgoanRVeRsjwXk82qqUvDraIv49sYaTJcY8pGJi2Mp9ygzwWZEspi1OccRmGUIW0l9X7iIrfkVQx9VP0buc1MUyWMTXIpcOo4xrIiP2sWNaxOb82a2yp9v7xiUZotc2LEot63CI2vYE2BcdUFyyjoMhIRop-NrtPPFetBjh0fF53fg_m8QBp1fSJbj0OluW2WqQe-OtiU2CnacQ22iQ34I5dtAeop8altQQlbOpP8d_4dSbSplGi74TJu5Z7fKLIoGodhciW3IbzUMFRiVZ46dut1dSK4W9wtDutxG1UwnpiCDGaoOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9536e07d63.mp4?token=Gt8nb-qAJJXkANMa_pDbOYLpY5vkcbGV2ASXgoanRVeRsjwXk82qqUvDraIv49sYaTJcY8pGJi2Mp9ygzwWZEspi1OccRmGUIW0l9X7iIrfkVQx9VP0buc1MUyWMTXIpcOo4xrIiP2sWNaxOb82a2yp9v7xiUZotc2LEot63CI2vYE2BcdUFyyjoMhIRop-NrtPPFetBjh0fF53fg_m8QBp1fSJbj0OluW2WqQe-OtiU2CnacQ22iQ34I5dtAeop8altQQlbOpP8d_4dSbSplGi74TJu5Z7fKLIoGodhciW3IbzUMFRiVZ46dut1dSK4W9wtDutxG1UwnpiCDGaoOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇪🇸
توصیه های دیدیه‌دروگبا به دیامونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/Futball180TV/104365" target="_blank">📅 14:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104364">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a301749a37.mp4?token=NSAaKF_qCNDExGodvqiQO3Pz-151uj3lgNcWX0ODC3NSesF8RTNKlaQNftxlTbuS-eMtWMDAhi680H8hPwb3ykXIPoMhGCMfOUk4fcnNiw9BTJc3oGMk3H5dzXVLCBU7kCCsROHtC4nIo2SjHF4OmN9Xd9BP0oBErEtqbOonnGYElmXKcfQ_rqHfnlJRH-u6HA-xr8VD835fV2Q-sJ5gX2GAC4nJZYtHtf_Y_fw9hGzbrIfWGjM5EFDR5a4BFgfzbgfi5n8twgrjlvaE-xTM15sqfs7Nxl4vva3l7-3tpjWrJSYBn59YbscnhNCqcEt6lGP3Dnil0GkJf2ew1UJ67g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a301749a37.mp4?token=NSAaKF_qCNDExGodvqiQO3Pz-151uj3lgNcWX0ODC3NSesF8RTNKlaQNftxlTbuS-eMtWMDAhi680H8hPwb3ykXIPoMhGCMfOUk4fcnNiw9BTJc3oGMk3H5dzXVLCBU7kCCsROHtC4nIo2SjHF4OmN9Xd9BP0oBErEtqbOonnGYElmXKcfQ_rqHfnlJRH-u6HA-xr8VD835fV2Q-sJ5gX2GAC4nJZYtHtf_Y_fw9hGzbrIfWGjM5EFDR5a4BFgfzbgfi5n8twgrjlvaE-xTM15sqfs7Nxl4vva3l7-3tpjWrJSYBn59YbscnhNCqcEt6lGP3Dnil0GkJf2ew1UJ67g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
بهنام ابوالقاسم‌پور: برای پژمان جمشیدی سند گذاشتم و او را آوردم بیرون ولی هنوز نرفتم سندم رو در بیاورم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/Futball180TV/104364" target="_blank">📅 14:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104363">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a5d5ff55a.mp4?token=LqitNLK6qmz1RxlSpB-IUTvjI-vi0J2qwM3W_WEh0HoqyD_kSnhuxKmluJltzBqwVIvjq0JFCB_RqpHoEFh2VrMnIHDhT5lic90aAymKTpYMSa_7ue3x4d6RA_NuszGQ3xEsf3yKdwub608tbAag5diUOJ2gbAATt6L4U7ad1H9W3KJD35Blyp05Sw_nTI-lRee5ftMIXlRh2ovT4c7KWZHReo0TrxK2j5iJQwrN6dOqjt2Kcx8gFfzrvc_9pn6fB-U3doYtxxfVw1f0NEAZ0qoehXD6wEe67MK6fcj9te3WXH9ZcvkIFTXzf8EpS35rdpro_q1HwceMr0B4n-VEAyOnsOvnBRLlqfe24AAOIt6OOQQWr2HcAeJd4h585aT_KhFcFsj8lAeW4orsHaa2M8rCCMxKvgq734WLFIyIaS1zTAtp9t0qong1h-R1Wa4K8AJQTgudxNrnvI9Wm-UfINqksMpzpCcElyqePsuMKiPI5VXnxDv_odHA3ZTk3TUHlEi3RmziMooiGQVSMdEu0yUZRuUnzhtsUnPBLoIiHyyrKisbVIbDcPTHFDHj8-kz5Gp7cWyiaJxij0xHaBMBoGcr3VBS49BdDy3VqNBbw1iXGwYJEDkDHjsX6xBGkApQw2e_VVt-FNnv6yCCm41BWbO9tSMXK5dLtDcZSkWqJcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a5d5ff55a.mp4?token=LqitNLK6qmz1RxlSpB-IUTvjI-vi0J2qwM3W_WEh0HoqyD_kSnhuxKmluJltzBqwVIvjq0JFCB_RqpHoEFh2VrMnIHDhT5lic90aAymKTpYMSa_7ue3x4d6RA_NuszGQ3xEsf3yKdwub608tbAag5diUOJ2gbAATt6L4U7ad1H9W3KJD35Blyp05Sw_nTI-lRee5ftMIXlRh2ovT4c7KWZHReo0TrxK2j5iJQwrN6dOqjt2Kcx8gFfzrvc_9pn6fB-U3doYtxxfVw1f0NEAZ0qoehXD6wEe67MK6fcj9te3WXH9ZcvkIFTXzf8EpS35rdpro_q1HwceMr0B4n-VEAyOnsOvnBRLlqfe24AAOIt6OOQQWr2HcAeJd4h585aT_KhFcFsj8lAeW4orsHaa2M8rCCMxKvgq734WLFIyIaS1zTAtp9t0qong1h-R1Wa4K8AJQTgudxNrnvI9Wm-UfINqksMpzpCcElyqePsuMKiPI5VXnxDv_odHA3ZTk3TUHlEi3RmziMooiGQVSMdEu0yUZRuUnzhtsUnPBLoIiHyyrKisbVIbDcPTHFDHj8-kz5Gp7cWyiaJxij0xHaBMBoGcr3VBS49BdDy3VqNBbw1iXGwYJEDkDHjsX6xBGkApQw2e_VVt-FNnv6yCCm41BWbO9tSMXK5dLtDcZSkWqJcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
بخشی‌دیگر از مصاحبه اخیر و جنجالی حسن روشن که‌ کی‌روش رو هم مورد عنایت قرار میده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/104363" target="_blank">📅 14:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104362">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdb917925e.mp4?token=efj3kfxpsQylKXAbBVH_8bEvmaL6hL_dukAGxt52JCCm6dR2lE8dsyXtLhctF9BBeZuJfDFosiJ5fZzrFqc6Ki1XQyOjXsShPz43oxlNJcqygMqY5KFvpy0q_ZgNfR1WAbNyOJYlEMwzJXiLKVjaxWbdttAdmz9B_nchKpzoio1MfmyIQRX4oSb8lwtvxfCuyGCV6xeBkE0zU0Z3mZIcOhg8mwxS2O1VDY22BgPCbcVUQj7sh7zRJBNScnOIONsoBRL22W5SxsFsjuqov1w8pyyA0ch7zjttvhl2nHFczevQhEENirtANj3iDE4ye9NjiaNcefUIVg2NDQ4-UAl0yxpBZoGDMH2iX02JTD7AZvZXtjuMwpbm3zg3g6Hd9t5gg1L1GxRSu0S01-zGH9_OrYwiE2nVlcBlSsjnaWGOU5sN3Iyne7U2uO8tU6lCrRBPvjHWlOnGFBJng9vj45D7DIJWQtUiIyqrbp3RV-T5W3ncfBeHlNqfGTBHURoMicQQGjZGsBihlN_cVIGJVo6SFfY2VRNGJMtmBEla4WcHZfPiF8ZLjPt0EpjJH-QaWyTmghaO3CEVIY2ddV1xcBM9zNBCq3F_NRi2aBpTasTiXnOGVXjjxkiCmEwPIiA576A6x36wArGSLBTeBDNMFDpmcJOw6o9AUS484B_Jhi5UWA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdb917925e.mp4?token=efj3kfxpsQylKXAbBVH_8bEvmaL6hL_dukAGxt52JCCm6dR2lE8dsyXtLhctF9BBeZuJfDFosiJ5fZzrFqc6Ki1XQyOjXsShPz43oxlNJcqygMqY5KFvpy0q_ZgNfR1WAbNyOJYlEMwzJXiLKVjaxWbdttAdmz9B_nchKpzoio1MfmyIQRX4oSb8lwtvxfCuyGCV6xeBkE0zU0Z3mZIcOhg8mwxS2O1VDY22BgPCbcVUQj7sh7zRJBNScnOIONsoBRL22W5SxsFsjuqov1w8pyyA0ch7zjttvhl2nHFczevQhEENirtANj3iDE4ye9NjiaNcefUIVg2NDQ4-UAl0yxpBZoGDMH2iX02JTD7AZvZXtjuMwpbm3zg3g6Hd9t5gg1L1GxRSu0S01-zGH9_OrYwiE2nVlcBlSsjnaWGOU5sN3Iyne7U2uO8tU6lCrRBPvjHWlOnGFBJng9vj45D7DIJWQtUiIyqrbp3RV-T5W3ncfBeHlNqfGTBHURoMicQQGjZGsBihlN_cVIGJVo6SFfY2VRNGJMtmBEla4WcHZfPiF8ZLjPt0EpjJH-QaWyTmghaO3CEVIY2ddV1xcBM9zNBCq3F_NRi2aBpTasTiXnOGVXjjxkiCmEwPIiA576A6x36wArGSLBTeBDNMFDpmcJOw6o9AUS484B_Jhi5UWA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آنفیلد تا پاپارا پارک⁣؛ ایزاک، هوادار سرسخت لیورپول و محمد صلاح، به دعوت ترابزون‌اسپور مهمان این باشگاه شد تا بار دیگر با اسطوره‌اش دیدار کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/104362" target="_blank">📅 13:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104361">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwq4ZgrDIfny8uTuDN1uTQZS3pQNexDc4RJMIJ0R-OyXn0r819qXf30T1svQlZwHb0zYn7JppDgCSjCJkPlVCj9W8awM54cPYsoItGtuRn26qFI7jp1Xh1LeYP60awRs9aZcbYYR_1YJHx9DJ7ZadZ4rxeT8Ck6qbypVgX_5TJuWR86zHprNclz9pqvkciSv-1NwGzw7Qnc6yDZUMucgbRNnmpaVtbPa1GB-YJBfNGTPb43C8bQqyc51fWfnREbCOJv2Fc7zL9yeHLr8UECFYnoyWlqrDoXQczl2UF9Y0hVpv_oLANXLyjbtPFpwdH9vLu8RG8faU_-67OGKy-aU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
شماره پیراهن این‌فصل بازیکنان منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/104361" target="_blank">📅 13:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104360">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57b5cc35a2.mp4?token=N4Y-imwv2L35jKXuq_abKzJ740f-cq6SQh-AQb9y-IdE78a6HnXSsD7-lHKnQKQ-JW1dIWB_IwUJjtor_nf9uxjIrfetaHWPROZTVVoz88M8UgN3_pqpprL61ftbeCiGpXeuetGiQFzuYtJV5BnoH0gWMjdDPZwLvtKjN_VgS3bDPqFbs5gstuH7EC793hruBcvPYjz7sbDcIhQJm1MRD9apPfwAtFQsNMl0rG26WFuczaNZRcf8IknnXR0eZ-W60bjNpDaHncoGpsEPD2dQ1a7eIKReMolJLZyUqnEmMAos0-KGWF_1JPxJJkPeUPcINHqGtOPA136i2CUb0TsuVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57b5cc35a2.mp4?token=N4Y-imwv2L35jKXuq_abKzJ740f-cq6SQh-AQb9y-IdE78a6HnXSsD7-lHKnQKQ-JW1dIWB_IwUJjtor_nf9uxjIrfetaHWPROZTVVoz88M8UgN3_pqpprL61ftbeCiGpXeuetGiQFzuYtJV5BnoH0gWMjdDPZwLvtKjN_VgS3bDPqFbs5gstuH7EC793hruBcvPYjz7sbDcIhQJm1MRD9apPfwAtFQsNMl0rG26WFuczaNZRcf8IknnXR0eZ-W60bjNpDaHncoGpsEPD2dQ1a7eIKReMolJLZyUqnEmMAos0-KGWF_1JPxJJkPeUPcINHqGtOPA136i2CUb0TsuVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو وایرال شده از کنسرت خیابونی در تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/104360" target="_blank">📅 13:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104359">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjWx21_cbCRvffczX05sdwfEvj0dnLrDKzb1i_tC-cwKurXAUPudJaAFuii-5xjSHGHliFl_5IgFXv94tp1P24-bayoWHXQiB_AcA4MzkHe2QJkeKDOCDz6ZrVraxiM8USCqf-W6yIGxy-ZU-n2ZBmB1KNjZgp3i__7AwpN0ff-mcbzEnIHfj-XTJ8RqDPO2jr6XyYrwbavc8lze57K0FhSEyI3qb0CBcRah65Fu-Ka7la-PZX4cWC_peuXlOM2cKY38VTfurGshff1gLBzbVVCvGyMU5YG0dG18P-7dHUUyK-cRAhtBdl79B1wXEzwjWms7esfvQ5WgyWI_fnlpxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
اعلام لیست نهایی بازیکنان تیم ملی امید برای بازی‌های آسیایی ناگویا؛ امیرحسین حسین‌زاده تنها بازیکن بزرگسال این لیست است.
🇮🇷
بازیکنان استقلال: محمد خلیفه، رزاقی‌نیا، اسماعیل قلی‌زاده، سعید سحرخیزان
🇮🇷
بازیکنان پرسپولیس: دانیال‌ایری، فرزین معامله‌گری، پوریا لطیفی‌فر، پوریا شهرابادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/104359" target="_blank">📅 12:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104358">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc7ebac37.mp4?token=G3JHJNL3xBxLwr8FUzTiJZAKLvGoOPm-3OV-2w121GQUgKVRmm3D7xfv6NmpWnPzsahJ97QQmjZCjDiHRWhr8WmNySpzcOH7kIMTyRktRPn24_QcFHHgRLJoBpHjLh1AF_0OAebyw0tr_QTFjFne0gn0l96gLmdulp4hQnSinSokxM9ZCXk1WsqGAh0cIkdKvo8c1CRJ8UbagY18iPz2sCxorUA-eV6OUFbL23MPaz7rSaiK__ZjrdzMQmubeNLQkhwyfWvVbCs084elPkEHOOZTKfI-6tLKbOEjzG6M9-dRyRjrUAl3r2-Y0FH_1nQ0RYL4_-mmeSNlQaDlWIDwUVpPRfr8DiZxt47oTBAALlQkcf6eKbrFbrEu8eUWMNJUHQDVfAGz5qZVW3MkIIHn9S3Kp6hhouu267_DGgdBgDT9eAdvMhOshu9BCUoIjdAmLSXRCssPEZc57YB9v-w2zsKvpR8kH1tFJT79W-nC4SjfUTYhq4CukQ0miPH34dvOqb8SqApb6iVgH8nxvvSBT9f8jOd-vX7Tab5ZHxOUU1Naz_3JYfyefwGxUhb1_oEagrnxUFX-upiSAy9S2aeFHC1vG15mzuPAze0EJYggRlQbj9TugkmtLnOeQy3EWOAGrsIwfFQXypca66WvT8eEczWFkXKL6qoEQGs-XkkewcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc7ebac37.mp4?token=G3JHJNL3xBxLwr8FUzTiJZAKLvGoOPm-3OV-2w121GQUgKVRmm3D7xfv6NmpWnPzsahJ97QQmjZCjDiHRWhr8WmNySpzcOH7kIMTyRktRPn24_QcFHHgRLJoBpHjLh1AF_0OAebyw0tr_QTFjFne0gn0l96gLmdulp4hQnSinSokxM9ZCXk1WsqGAh0cIkdKvo8c1CRJ8UbagY18iPz2sCxorUA-eV6OUFbL23MPaz7rSaiK__ZjrdzMQmubeNLQkhwyfWvVbCs084elPkEHOOZTKfI-6tLKbOEjzG6M9-dRyRjrUAl3r2-Y0FH_1nQ0RYL4_-mmeSNlQaDlWIDwUVpPRfr8DiZxt47oTBAALlQkcf6eKbrFbrEu8eUWMNJUHQDVfAGz5qZVW3MkIIHn9S3Kp6hhouu267_DGgdBgDT9eAdvMhOshu9BCUoIjdAmLSXRCssPEZc57YB9v-w2zsKvpR8kH1tFJT79W-nC4SjfUTYhq4CukQ0miPH34dvOqb8SqApb6iVgH8nxvvSBT9f8jOd-vX7Tab5ZHxOUU1Naz_3JYfyefwGxUhb1_oEagrnxUFX-upiSAy9S2aeFHC1vG15mzuPAze0EJYggRlQbj9TugkmtLnOeQy3EWOAGrsIwfFQXypca66WvT8eEczWFkXKL6qoEQGs-XkkewcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
‼️
#فوووووری
از بختیاری‌زاده: ناراحتی کوشکی؟‌ حرکت او حرفه‌ای نبود و فردا مقابل سپاهان نیمکت‌نشین است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/104358" target="_blank">📅 12:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104357">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5711b4d86b.mp4?token=UKPFfNRVhDopdQDlHBDdcK-juMoZEDUB690afTjKVDet89V-RIMhTZkvYQcuU2h-pNu8wtPSAjTPuRJ2zbupeZweZmPsQXzBR1b7AGfjRs0OC5HG_HQ_zFSlCKrtgLtvw_pRuMFRpm1NuDBpM6x_GbbsXUDwYkaJOAcHXAjlPz11QwhI8VojbDuowiRLd1XnSMyB9Jt5kZMoT6Eay1LFyYmGXCw98oBtzxXGTHSj40gjguhALkIlQnI1aBbzc4qZbZ7l_1PG4nVAFuj4QO7kA9dZRnlRo5YvaTRGcmy5Y4mRXK6RYU8v3YHLR73GtdxIYtX_ssM29BTQpmXZ7eSOQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5711b4d86b.mp4?token=UKPFfNRVhDopdQDlHBDdcK-juMoZEDUB690afTjKVDet89V-RIMhTZkvYQcuU2h-pNu8wtPSAjTPuRJ2zbupeZweZmPsQXzBR1b7AGfjRs0OC5HG_HQ_zFSlCKrtgLtvw_pRuMFRpm1NuDBpM6x_GbbsXUDwYkaJOAcHXAjlPz11QwhI8VojbDuowiRLd1XnSMyB9Jt5kZMoT6Eay1LFyYmGXCw98oBtzxXGTHSj40gjguhALkIlQnI1aBbzc4qZbZ7l_1PG4nVAFuj4QO7kA9dZRnlRo5YvaTRGcmy5Y4mRXK6RYU8v3YHLR73GtdxIYtX_ssM29BTQpmXZ7eSOQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
نظر جمعی از هواداران اتلتیکو مادرید درباره ماندن خولیان آلوارز و واکنش دیگو سیمئونه به توهین برخی هواداران در استادیوم به ستاره آرژانتینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/104357" target="_blank">📅 12:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104356">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONUPX3Ydo2Q0g7rDo2Pzp7vsYu4ShNftyiBg1a7-YDHa4noNUv94hGX6ctqMlKrIREAS0D-Kqn8bvvi3sM8d2lwxdNUQBzrbzl2BWS25iW1iMfD-dgANz-UWv9CadTlD2DXe_4DCMKmETzhq3C-sOV6kaYQuh8y3GxaOs63twt4DWdHXio8Q72w-U-Wjxea8mxzBTn7UcdDCmh_H5g5zeUf5nh4Y_854s3NhNyn34pUGHXak4r178pj_4B1oStLhq78dbqnL6YqOEqVljz25IrBPCbowZvq3CTDIBu-y-DPnZNUqBNwcCqUAbXm1baTnKQK_cknYRh_-XrAmSy4SSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🚨
مالکوم با عقد قراردادی پس از جدایی از الهلال به تیم‌الجزیره امارات پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/104356" target="_blank">📅 12:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104355">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpHnLkSIeEiJWKLDjP5Ccxo6bCGrUIPTKDWWDdH9OL9ED4wGPf_WK1_uHuq_0QjciUho5SYrcbcoS9dnnNpa93OI5DAcdUb-zEz4Dcnn3oySglFHbabYxIgxafoz8vMlXFHHHTz4niYuZvVBA3bVOdgiEcbXm5wejIVdkyuVz0gSGqHITwBFAEWp8loU4-4mG8EhCNo7ufMQMUhDO1L9Xr0quWUHGr-XUStfTbhN5AdQW_MwKiAbXp1_YeayW9N1eaxK4uCGMIm6HZ4KW_CbBwXXMf7iwhOAmRsdfYhCmZVwMl21YyN6ynKhJKj5g0E8Odr2wIZDBFaVE3xabXeKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
سایت برنامه عادل فردوسی‌پور پس از گذشت چندین هفته رفع‌فیلتر شد و در دسترس قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/104355" target="_blank">📅 12:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104354">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab7bebaf5f.mp4?token=l3rJAGwO6b8BVUdilEjZUjL-L8kJDptNPKwfEZXrf9Ld3LAij4fRxCl-Qkn7rYLNBEVOTHoHgSrF_lhpPHpwzyE2_z7iu7NRgpPPSfQ9s9L36qDmu-a-EHlSPvGS_nlzY5aDjGtCuMC7_Kaql0-DMJVD0-IODByoG0joZd3fzogQL1rSdaXo3hNj81qdCDXMEsIfbM1VuCd8_ehVsOcXENlzHcyRU_keQDsIR6aX0ys3X17-15v0Hz5c0qQgicqhwV9H5iy4p6ZUDN72X9qEPL_dpMOpSdoyZdYTEq7baGVQro_tZFIJAshqjB2nix3uKPosnsxR8LiRu2-ytogZ6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab7bebaf5f.mp4?token=l3rJAGwO6b8BVUdilEjZUjL-L8kJDptNPKwfEZXrf9Ld3LAij4fRxCl-Qkn7rYLNBEVOTHoHgSrF_lhpPHpwzyE2_z7iu7NRgpPPSfQ9s9L36qDmu-a-EHlSPvGS_nlzY5aDjGtCuMC7_Kaql0-DMJVD0-IODByoG0joZd3fzogQL1rSdaXo3hNj81qdCDXMEsIfbM1VuCd8_ehVsOcXENlzHcyRU_keQDsIR6aX0ys3X17-15v0Hz5c0qQgicqhwV9H5iy4p6ZUDN72X9qEPL_dpMOpSdoyZdYTEq7baGVQro_tZFIJAshqjB2nix3uKPosnsxR8LiRu2-ytogZ6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نگاه طنز به معروف ترین دعواهای تاریخ فوتبال.
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104354" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104353">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
حجت‌کریمی مدیرعامل تراکتور: متاسفانه قانون ورزشکار قهرمان برای معافیت سربازی شامل علیرضا بیرانوند نشده است و به احتمال بسیار زیاد باید این بازیکن راهی سربازی شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/104353" target="_blank">📅 11:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104352">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4qlsL5NmKDJ0FhB0YS6aseB6iuoQF5LTyz0eQnOjzBbj7bCWLgmpM-yf0sySW57XgdMjGbTC5XrflJwMkeOb63OOUa-fA7rSg1UCb2noWYqJX_xZX4pIaqiFIDTJS8KrM1Yv9x9JNOBm9y8Pxnajmc4YPDOUFyoRulvXyKtzJKe4JG-naKMfdDxD5EIkUBldgPLexGN-Pi1K8HTxDa30Lea8l9_X5fkVQE53BNpgin_iby9hJdmmxcvcN4ByHTvoJ1aXBG6VNaIS31Vh9tXKcUWCe74-kQSqSNQ7u6PIIYWWonuXJIeAnLbQix3SXwRa1NCRonqUlD_HOI1LBM0fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
حجت‌کریمی مدیرعامل تراکتور: متاسفانه قانون ورزشکار قهرمان برای معافیت سربازی شامل علیرضا بیرانوند نشده است و به احتمال بسیار زیاد باید این بازیکن راهی سربازی شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/104352" target="_blank">📅 11:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104351">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJNK-hCM2IHziSi-nrXk6TS3piHZTdI0-MxyhLL_v_Ut__iDr6wTr7kbnKkHvBwLCceX5okRGkdrJhIVRJwK-71QlHC4mcto73BgYhuVk5ltDEmh9xwR4t7oGmZIz7Md647ctiA11C7IGTgu93hanmZn4lQpLCvCu8gv3stykoMRz-x81ZpE01jii2IHXqCgIA19029JF4ygP3zmVGfbIJa4rQIHRoGgbp8mQKj-umechDJ8MXXjuVJVzjFOFAXRhupzjlgFVM_k7hUHo9FV-bdXXp48g0CelhSrDT0UotUmY3U8QPBn-ARHHH7nQ6VA0d59c4LidmrjhhMOBveOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
اعلام اسامی داوران هفته‌سوم لیگ‌برتر
🇮🇷
🇮🇷
استقلال - سپاهان / پیام حیدری
🇮🇷
🇮🇷
پرسپولیس - تراکتور/ امیر عرب‌براقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/104351" target="_blank">📅 11:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104350">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehP6u837aUXxUvujHS0le1n9HS0Uz_Z3Iwj0S0QZJKtuCl4NR0E8T3Th7sriFVpOBZ-Kmx0P6xR-8kK3LJivCkD-Rhigtw1r36nNG8qiWTcLdmZR4-XthajDivABWlJNMXPDfv8CUjRpObaLbMTcIu-TqsWEd0_rZBRqvUXNdLDxr4hAzBwSWE5HfL6HQOd2SipQy90fSpREXtdS3WisnQ14ec8jBeIHeivOKgn9oxG6jrpsjGSlF7jrH-JemGUaz7JqVldovC07Ne1RBDgwlvPHopkrd-fdDr38rRrg0X6w_Rq6SXwy8O_bAOHA1_4ZAfBsFldaoJNFFrAJH9i9LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
پوستر باشگاه استقلال برای دیدار با سپاهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/104350" target="_blank">📅 11:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104349">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/104349" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/104349" target="_blank">📅 11:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104348">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEoopY6RrQlGXzHIQYxhBSNnjKFfajsUMHRgVWdrB9aaTqI5eeOIRYJPpyBC1-r57bulqnAVKWXKBWd3hk_4NdQaFwO7dwDCJ4pFu5GHyHCdo7mcABmKnhkZIAYUUbnye1QBU-hi6Qpc67nHIU3Z23UBolc2YkwkcPtxOwDhMkA7_N1ZsbfffZULwZy0Fl5oW2EjNt_Q2yvqNj7yqsnNrHntUobBXiwsV6y_45IwcOWa4BYhwsHxKiNrkU55GGHT220tn5mT-1eoNgC1Hj_kST_rP9BWiNOZiaYFzPU6hA5Bn8FPFzU-3L8b3Hz1cp3VddZel05LgJXTRm-DgI0_Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a31
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/104348" target="_blank">📅 11:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104347">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb94b21a1.mp4?token=vKj8T_cTkxNoB3YZXPejKWTWAVHO5dQuK3cMDLPDM6UhgZ_4DjhnMx-uYTa4DvstNSTdyL2G_Tk35VcrcxsyAx8qMOW_pqXx6IpevoQALVedmZu7Dd4Aokxr2oXzPH1hnjjyThshU45YDtB0x_JmM09vhWu50zsWrdHZ9HV1dE8Y2v_fz4yOmN1VY-M8e4UtGrapStLyfShscU9NJBCFmqVClMvuExj921Dh36So2336dXP-azs4d5QIj9czYvbG5opR8hEGztE-eqQSVSrWvsc7tKmSqUeH2jLQHM7tzlESdfDTz9ErtIR1q7YDbwCSxnmcYvJ8TxvL_OFdH23SRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb94b21a1.mp4?token=vKj8T_cTkxNoB3YZXPejKWTWAVHO5dQuK3cMDLPDM6UhgZ_4DjhnMx-uYTa4DvstNSTdyL2G_Tk35VcrcxsyAx8qMOW_pqXx6IpevoQALVedmZu7Dd4Aokxr2oXzPH1hnjjyThshU45YDtB0x_JmM09vhWu50zsWrdHZ9HV1dE8Y2v_fz4yOmN1VY-M8e4UtGrapStLyfShscU9NJBCFmqVClMvuExj921Dh36So2336dXP-azs4d5QIj9czYvbG5opR8hEGztE-eqQSVSrWvsc7tKmSqUeH2jLQHM7tzlESdfDTz9ErtIR1q7YDbwCSxnmcYvJ8TxvL_OFdH23SRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
روایت امیرحسین اصلانیان از خوردن حکم سرمربیگری احمدرضاعابدزاده توسط آقای مدیرعامل و واکنش علی پروین به این انتصاب پرحاشیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/104347" target="_blank">📅 11:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104346">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80db36926b.mp4?token=nS2UPvO5SO3qzjdHJArWmUUlzxbYPUisFJmYrpmDLdU1XfgC5-jVY6P1Qs60HB_S7Zjh_wtN6wSk23r1fVHI8T-Np7mE8-UWeLXgHhc7F8nCBPhXNg5o5T84mSxkCVtSDZvIV7KK7ybQMJiTXxSAbmQfYP5lA2sbEydjiN72uE41Oe3HSHwmBOuDSZ6KepY0SpCS1AJ6r8M3p9NjQrDUa6gsDqIv5NezPRiaymViONfHHgHOf_z75-Q6wW5quy3LcBYoZbCXu9t42wwV_tPeU4jk3HdqULSI2jwfOvCQK6nSjhCQYGbWXbCmDh7sbQLzAMkDKgUOliCp7dnGJVCuIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80db36926b.mp4?token=nS2UPvO5SO3qzjdHJArWmUUlzxbYPUisFJmYrpmDLdU1XfgC5-jVY6P1Qs60HB_S7Zjh_wtN6wSk23r1fVHI8T-Np7mE8-UWeLXgHhc7F8nCBPhXNg5o5T84mSxkCVtSDZvIV7KK7ybQMJiTXxSAbmQfYP5lA2sbEydjiN72uE41Oe3HSHwmBOuDSZ6KepY0SpCS1AJ6r8M3p9NjQrDUa6gsDqIv5NezPRiaymViONfHHgHOf_z75-Q6wW5quy3LcBYoZbCXu9t42wwV_tPeU4jk3HdqULSI2jwfOvCQK6nSjhCQYGbWXbCmDh7sbQLzAMkDKgUOliCp7dnGJVCuIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تنگه فلوریدا را هم ببندیم؛ ایده کمتر شنیده شده از استاد خوش‌چشم، کارشناس ثابت صداوسیما که متاسفانه از سوی مسئولان لشکری و کشوری اهمیت داده نشد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/104346" target="_blank">📅 10:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104345">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0566a44cfc.mp4?token=qslj7xAF7EXkLJ6DSRBdUO_COM0oWagujs3ksSGawRzqMc2O9kOTCafg3N1bp9YTGaG0iPxiUdAU8lJifPljrAtZIAFgbusVmQcrtfOGXU2VaemnyGKzVqxA0IGnjtjIKkFjAu9NViU2aZqzMVd3fozry2uaSFNlgibhCOUd8ZqjIoesPUgpUs4q0dNd_shTlF_L56-6p1icSvswkjUrb_cSGlEx8byL5xxZP3CJUOSslZkPL_0VTiJMpmgP0crF5bvoELMMH8xb82QTb35wZmvSrgSKEuxECsCrznbNorzDLbrgCqb4g9DJdo-e_yyWfnpjUbv14TwVDMRdgAs3Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0566a44cfc.mp4?token=qslj7xAF7EXkLJ6DSRBdUO_COM0oWagujs3ksSGawRzqMc2O9kOTCafg3N1bp9YTGaG0iPxiUdAU8lJifPljrAtZIAFgbusVmQcrtfOGXU2VaemnyGKzVqxA0IGnjtjIKkFjAu9NViU2aZqzMVd3fozry2uaSFNlgibhCOUd8ZqjIoesPUgpUs4q0dNd_shTlF_L56-6p1icSvswkjUrb_cSGlEx8byL5xxZP3CJUOSslZkPL_0VTiJMpmgP0crF5bvoELMMH8xb82QTb35wZmvSrgSKEuxECsCrznbNorzDLbrgCqb4g9DJdo-e_yyWfnpjUbv14TwVDMRdgAs3Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
جانشین سرخیو بوسکتس در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/104345" target="_blank">📅 10:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104344">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65173b5bd.mp4?token=sFw3GekdiCkhCuX6uY22MPGUftvhu5vzjxAIm63aS2XDUNZcrhXjbLaiqULUdEJaspy9MVnnmGUhFArOsTQ1USA9s548mR103N7OrxwdrFiycTQ-I_BLMpqx04R34666eaVcehynR8FwpchQ7Njs_N6B7Eo7pezWo1HbXuqBy0zfitMESz7u93zA8SVxm4vCAC0a8S5-o-emz1cnYwrNh0zMfqlbB7jd1OG4ujvlumjtvp3uCj9jd3I8f_7i_zi5EiABQsypXl8JXLugBvoXOyqa92zQtPOV-a76QRmaCFQf_MoEH3O_m9h8NQbhy9qudpfZWXMxbgfoX79EUghdxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65173b5bd.mp4?token=sFw3GekdiCkhCuX6uY22MPGUftvhu5vzjxAIm63aS2XDUNZcrhXjbLaiqULUdEJaspy9MVnnmGUhFArOsTQ1USA9s548mR103N7OrxwdrFiycTQ-I_BLMpqx04R34666eaVcehynR8FwpchQ7Njs_N6B7Eo7pezWo1HbXuqBy0zfitMESz7u93zA8SVxm4vCAC0a8S5-o-emz1cnYwrNh0zMfqlbB7jd1OG4ujvlumjtvp3uCj9jd3I8f_7i_zi5EiABQsypXl8JXLugBvoXOyqa92zQtPOV-a76QRmaCFQf_MoEH3O_m9h8NQbhy9qudpfZWXMxbgfoX79EUghdxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✔️
پیام‌کودکان جنوبی خطاب به‌خانم‌مجری که میگفت جنوب ایران فدای لبنان و فلسطین: اشتباه نکن خانم مجری ما جنوبی ها فدای هیچ کشوری نیستیم ما فقط فدای کشورمون ایران هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104344" target="_blank">📅 09:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104343">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bde2485a2.mp4?token=vK1MQisMR_u563iNdixZ4Y4O-D7zV1fmI0AfViDQ5hXOWG3s4OuBhuFohFMVzA36r__T-qXBOf8Y0dXvCLbSCFKxhUByAr9xE0sGcPlti2rrcr7gBKU1NG_xhe1Hd3gNDhLEi33kK6QtaunREJRjQvdQMhfWfGUH5aUErVya8aEi0PN7_HJaU7RnJMdVQl5p9hbczluDv2SG2iWQJVGAN6cb3D3_oxzPS-wDCP8GzY-kPRqWeF3hBrb-b3ADbhVCCUZKtQ52baMBQdLFyKfJpVGvZal0hQtX5qVxG9edr8eyJVK2zV3h8wOqeiwD_k_YrxITk073C8VyvH-c3E4Snw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bde2485a2.mp4?token=vK1MQisMR_u563iNdixZ4Y4O-D7zV1fmI0AfViDQ5hXOWG3s4OuBhuFohFMVzA36r__T-qXBOf8Y0dXvCLbSCFKxhUByAr9xE0sGcPlti2rrcr7gBKU1NG_xhe1Hd3gNDhLEi33kK6QtaunREJRjQvdQMhfWfGUH5aUErVya8aEi0PN7_HJaU7RnJMdVQl5p9hbczluDv2SG2iWQJVGAN6cb3D3_oxzPS-wDCP8GzY-kPRqWeF3hBrb-b3ADbhVCCUZKtQ52baMBQdLFyKfJpVGvZal0hQtX5qVxG9edr8eyJVK2zV3h8wOqeiwD_k_YrxITk073C8VyvH-c3E4Snw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
نحوه آموزش فوتبال در کشور متخاصم آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104343" target="_blank">📅 09:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104342">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l24BOFWI9tBjHmN1yfX6YBqOT5VJV7UBeXDfRIxAyupArXnb6DNFIm-I89IqV6uWnXoporfBuW_Fbc2ft1WX2vjhyKKs1N89bWRSO-yceWTH4tlBj8zE7NKuQuB2oraoXapkNa0xO9MkFMjp5uueqcZbcWeJuDmPblCL6We2s_aE2p_-65X1kr_Zm1QelRATPaI_Ad91CiqUjXv2VYFahKFZl5cCxRrg3vIp2Bvw37JFPkK6X99d-K7UhlaNREp72ncpapm4fObXMvqs2NM8SmRYlDvvgzgfrxXhZSP9-6wH8v0V4h_5uNcjLAbcBIERej-1ETy0KHlAbQgu0vQbsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
شانس‌تیم‌ها برای قهرمانی اروپا‌بعد از پیوستن رودری به باشگاه بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104342" target="_blank">📅 09:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104341">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fb4qOLl0Z2pc08g0_JjGp2nnB5-cFWsm7rOvY_Z7jQCXBKqEEIPem2CZI3lHAo90ZF7jSjFx8WMn0wQNM-mDs6AzNuLjfc3GdAcK2XAQc4gKQm6TQ2ZnTtJDf6MyC-QgJAYGrZru4i0aLnAEzGaro_GMFfLCj3n-G2VpdUzHTehNTuTUtgrJzmslRjbk935kPHsnlJalv2EOuvh0I9VylWB_fb-7XCRNOR1pLdH_waA590p1IRPYVmoQy1EKzF7Zk9QgpGJATtLPSyntBTCf8TC4jKs39thzFIScMtTGk7elpQrsEcpPvU7yS1MKxXO1XR7h0GQ1U58ZDbIukjNI0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
استوری هیدالگو، مدیر برنامه آلوارز  «هرگز از یک دروغگو نپرسید که چرا دروغ گفته است چون برای این‌که دلیلش را توضیح دهد، مجبور است دوباره دروغ بگوید.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/104341" target="_blank">📅 02:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104340">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
استوری هیدالگو، مدیر برنامه آلوارز  «هرگز از یک دروغگو نپرسید که چرا دروغ گفته است چون برای این‌که دلیلش را توضیح دهد، مجبور است دوباره دروغ بگوید.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/104340" target="_blank">📅 01:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104339">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tE8QQP1R3FyjsrmktKuICsEh6F2-CyJPhGkd7O49l7sLv66V_bREm7X9DMg7JBniYjyD7MK91Pc0P3eRdfdUpXmUgK_5PdezkfaM_Vvh09NzJqnRJFiCD5TWakMvEEwy2zi4Qk_SAgFzlSUgfqO3CWAcTOW1rYCCop8XAz1nhISjsIlox1MeqP8N3jkzUVEEwVcDoWZER4-J2oQJgg9_BmVDQxAS_kpVrQYT0OO4-LHsJ341pGx03F-pG0C3ErH42RCtjnxS_JMrWX-IkhYNtPkRrUkTcBhetUrAq7Y39e7SE1WyLo6VUsf6nGtYcdyvVdF0-E6uZsWkz8ECUlqqGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
استوری هیدالگو، مدیر برنامه آلوارز
«هرگز از یک دروغگو نپرسید که چرا دروغ گفته است چون برای این‌که دلیلش را توضیح دهد، مجبور است دوباره دروغ بگوید.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/104339" target="_blank">📅 01:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104338">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZwuwrzQvDuF1YqaJH-UmUN8z8wAbejOe33OpWMYx4hC3g2sSfW7jEj7V0AmOC1IlB0By0lGtsm8UpLdoWHdV5yYFe0SNTUIgCTBVF2ppYaUwaP2ziNoG8o9V_WhrLUsJE48OwPjXtOGmgIx3Vl3eocwPhIgO41bWSxTiZplQfPDMMxEcvAA4LnDmppflKDGLYPcheEL1YVu8NjuqjDFBfIwYo4A-VR1yagUf2aQfYGm_8R5laXkwE-rsbbSz_S2mRiBGdjajm4HjC8cTaDV4WT3Gq0pTENeZyJuand2AjPwjMYGKIkg7yoSJfJC_cDVlqA1tAVohM4V2pRx4Laoeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
پس از پیروزی آرسنال مقابل کاونتری سیتی، میکل آرتتا به پیروزی شماره [150] خود به عنوان مربی توپچی‌ها در [249] مسابقه در لیگ برتر دست یافت.
🔥
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/104338" target="_blank">📅 00:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104337">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/104337" target="_blank">📅 00:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104336">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=KVi-Zojk-8apO_EN_q-qVcPk0Fj3OwRGMYecFdtezJ_IwUYv30d0nU1XdMX5xutQmGnLzq7etZdl7s0JV_YnW61QLLSlLLz7JsIPdp58JeRMaeZLVfXmqplr-TLUP_mJgVP3jVaqKeeDOLtFYW9oinyLp7fA5iYJpy1MZ1jIWm8PWf5Xk_PbEfqd5Acv_SyKvbYC21tzlzokMipZ5NcwPCC0mMZrxnL9GktqOKmcINrBTwOaqXtlDRqyJq2gDnJ14AkffxiXkks7LOSYq24rWir4gYNaajUtlJA5e1FF5n6NQa0HX9gqsVdsklcs_wvSTEIXg66DhrGRfZexOWjnJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=KVi-Zojk-8apO_EN_q-qVcPk0Fj3OwRGMYecFdtezJ_IwUYv30d0nU1XdMX5xutQmGnLzq7etZdl7s0JV_YnW61QLLSlLLz7JsIPdp58JeRMaeZLVfXmqplr-TLUP_mJgVP3jVaqKeeDOLtFYW9oinyLp7fA5iYJpy1MZ1jIWm8PWf5Xk_PbEfqd5Acv_SyKvbYC21tzlzokMipZ5NcwPCC0mMZrxnL9GktqOKmcINrBTwOaqXtlDRqyJq2gDnJ14AkffxiXkks7LOSYq24rWir4gYNaajUtlJA5e1FF5n6NQa0HX9gqsVdsklcs_wvSTEIXg66DhrGRfZexOWjnJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+UfR2NG4GjAMwNTQ0</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/104336" target="_blank">📅 00:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104335">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e4cd1601ff.mp4?token=HbHZQyhRMpuW5bhgZ2ca6DPZrbjUDJyfHrgHm8Iw2iH0XAetWrYkOEP1wocBSYpRnJAHLOKbo4Mc6PWGWRAzvLGxJ4KuM36CA77_nubcgGfzGgq39mpS9u_EyMjZFgJrNfIYTwpJKczaSZ9_cmvvo9H9vY7bISU-8JJlHEj1YTzqphvaiOaf9XJbZj_b-RRlvDbFcObiR3uC-U3TssYXHL6bF0huDAhPT2HasVz3eBUQZuqwE3_PzRPaM2X7QnHCVn5A6_DqKCYb7LlW8L67VQn1yEPAT7nNFPusDt4EQ6XgYuiA83zH8QlHHwYYTAvh89_PY3Od4nQk7InOGEc3BJ-3RlWm8xCie134OHjc0bEFKsncQ0ZXXDWj3UXJrx593x0a-lrGy8snUvrDbQ4BkXq0wumOiO0MHNHod3N-kI7652RVTlNBN1pqLQXi38TeAJH8d8HBxQBIwGoXD4xCZ6degy0K62BLx4_OgGLYlqYl7lehhzSZSYYSNouVgX2saYS5zxt7PXLNnPGjNpRIXtfifFzU7l-nneFHKL3y1pmvgYrgToy8mPzo3NGOaqXOWsrb5uKw9C4A8t7PpZZar9LPsM7XIqPWYXSo6u06CsAhQj_YLGeLq2EVMAro-zj_viv9PJwWg7X5tMzjEPcK7nY2_wUM60DNK4dfk6gsjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e4cd1601ff.mp4?token=HbHZQyhRMpuW5bhgZ2ca6DPZrbjUDJyfHrgHm8Iw2iH0XAetWrYkOEP1wocBSYpRnJAHLOKbo4Mc6PWGWRAzvLGxJ4KuM36CA77_nubcgGfzGgq39mpS9u_EyMjZFgJrNfIYTwpJKczaSZ9_cmvvo9H9vY7bISU-8JJlHEj1YTzqphvaiOaf9XJbZj_b-RRlvDbFcObiR3uC-U3TssYXHL6bF0huDAhPT2HasVz3eBUQZuqwE3_PzRPaM2X7QnHCVn5A6_DqKCYb7LlW8L67VQn1yEPAT7nNFPusDt4EQ6XgYuiA83zH8QlHHwYYTAvh89_PY3Od4nQk7InOGEc3BJ-3RlWm8xCie134OHjc0bEFKsncQ0ZXXDWj3UXJrx593x0a-lrGy8snUvrDbQ4BkXq0wumOiO0MHNHod3N-kI7652RVTlNBN1pqLQXi38TeAJH8d8HBxQBIwGoXD4xCZ6degy0K62BLx4_OgGLYlqYl7lehhzSZSYYSNouVgX2saYS5zxt7PXLNnPGjNpRIXtfifFzU7l-nneFHKL3y1pmvgYrgToy8mPzo3NGOaqXOWsrb5uKw9C4A8t7PpZZar9LPsM7XIqPWYXSo6u06CsAhQj_YLGeLq2EVMAro-zj_viv9PJwWg7X5tMzjEPcK7nY2_wUM60DNK4dfk6gsjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌سوم آرسنال توسط اودگارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/104335" target="_blank">📅 23:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104334">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ecf24c9409.mp4?token=A1PaCy21dWDV_wTc81bKQfdFcj4qZr6fPdUI7B_NCEZfXkeKhkbSKzludvqM2IsugG7ItIlAf90dLNRZU3wb37gyiQdLQKhTRrNyyYLO55FO1DbEaabLBdiFSIzOIlCFrWeXfN04fmXVXhPlrBF1XemaE9JyLJSa73TkjGDX2Zsw1DRwjq0nglbzMT6KZTzt7Pu9Y-VWzYWO1YglNbaHzMGfwgfSNTSTWw5rUUo2zbb_6wfJSfZyeGHwQ7VVFlAtMXddFM2nG5c9uJEUyWKnvvkEOTwySUNs7t9OW3jb6ZsMiW64s7h1p6GCUznukEpWdqSdxMKy9IC1MnMUC_CSWLBSKsXimAlUjUVcKu1Foyy_oEBNfQb6BX7vgx3Ddy3drSK_Mc1VaSkoEF-gfJnXI3nJL8w903EQFdM5ZHBDGSmFMOEZZl0dnMUMs8ahiIiTfeKguQkbDJ5rj-jGzUTy5xXQZzequvkFMt5JiDm2Dil65Ng5LCD2n_wgHjljc5SVgEQ_Iw2twqeBceTI3z4G5rbNp4HhSZpsJw0Qn-c3jtB7wDHI_UrtzEAP7VzBeupdNT26NOqVsRgKXl1VS-qYmdMKoeYQ2GaonlIvGAIcikA2wZXPqLVpCuosHuggD1yEOd9EBTvZ8QeZfk57S8MMJPOQBo28zouiNN3QK2nmycU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ecf24c9409.mp4?token=A1PaCy21dWDV_wTc81bKQfdFcj4qZr6fPdUI7B_NCEZfXkeKhkbSKzludvqM2IsugG7ItIlAf90dLNRZU3wb37gyiQdLQKhTRrNyyYLO55FO1DbEaabLBdiFSIzOIlCFrWeXfN04fmXVXhPlrBF1XemaE9JyLJSa73TkjGDX2Zsw1DRwjq0nglbzMT6KZTzt7Pu9Y-VWzYWO1YglNbaHzMGfwgfSNTSTWw5rUUo2zbb_6wfJSfZyeGHwQ7VVFlAtMXddFM2nG5c9uJEUyWKnvvkEOTwySUNs7t9OW3jb6ZsMiW64s7h1p6GCUznukEpWdqSdxMKy9IC1MnMUC_CSWLBSKsXimAlUjUVcKu1Foyy_oEBNfQb6BX7vgx3Ddy3drSK_Mc1VaSkoEF-gfJnXI3nJL8w903EQFdM5ZHBDGSmFMOEZZl0dnMUMs8ahiIiTfeKguQkbDJ5rj-jGzUTy5xXQZzequvkFMt5JiDm2Dil65Ng5LCD2n_wgHjljc5SVgEQ_Iw2twqeBceTI3z4G5rbNp4HhSZpsJw0Qn-c3jtB7wDHI_UrtzEAP7VzBeupdNT26NOqVsRgKXl1VS-qYmdMKoeYQ2GaonlIvGAIcikA2wZXPqLVpCuosHuggD1yEOd9EBTvZ8QeZfk57S8MMJPOQBo28zouiNN3QK2nmycU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم آرسنال توسط بوکایو ساکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/104334" target="_blank">📅 23:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104333">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/889cf6b1f7.mp4?token=jBi3B7bJqjjPEfoFx9xQrog0uUGKV_9szuOnxwdNMExzPgbnC9Dp-6dLLZ_qJARpELvIfejIzpCQRKP12IBftDn1H3OINfHzeyki0DR_hTEloExPWfyrY4zFduBx7Ikpzkt08uXdpH_1bL_JpNDCfwZFVbXbeyL1G_3leFwZK3Oww_t5QqECebwh-xJbIM3FwIdwUFGMYZCTdMbq_wso1mfE1r6LR12ZIXOL61dbw5xksHzZlWpWRcnu2GVR10Dz1_y1cKr4OARRQbmv1RBBwUM8epH6h_x1hyd4qjpYVWzu7SDruBWwPqh4UIaiUezB6itQJP3-FmPPvmdsl8EaZmfzkN0q6Q3BTiQIWyCeEE6MRCAhLNQx4zo7aGZ0ZTTd8grxLSbTiN9bQEuKLK1WbrUdr0HGOusKOsqsshwCcVTVGya17LhtSPVNBDqt8_TQ5N-G9AmnljjBc-xUJ4Qw7Gt0Cx-Lk0f2Wz8FTDQFYbwpDpOqVFmfyPy_FpiURIhP2FqedXJ2Rlz4PyRXdAoaVLzprK2UVD72GyLc0WrjjxtDqcjJAo6mCnLLhcF9ZbUfwUuXh-Spzh2-VfWUZhWGDUBUxFEZsUXAzhSrkadV4UIN5t5LszNBWDByx_pKLr98jKQ1gRwJhgm5R6Umgfk2hX8QAmo04HnGjYPGodtyLT4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/889cf6b1f7.mp4?token=jBi3B7bJqjjPEfoFx9xQrog0uUGKV_9szuOnxwdNMExzPgbnC9Dp-6dLLZ_qJARpELvIfejIzpCQRKP12IBftDn1H3OINfHzeyki0DR_hTEloExPWfyrY4zFduBx7Ikpzkt08uXdpH_1bL_JpNDCfwZFVbXbeyL1G_3leFwZK3Oww_t5QqECebwh-xJbIM3FwIdwUFGMYZCTdMbq_wso1mfE1r6LR12ZIXOL61dbw5xksHzZlWpWRcnu2GVR10Dz1_y1cKr4OARRQbmv1RBBwUM8epH6h_x1hyd4qjpYVWzu7SDruBWwPqh4UIaiUezB6itQJP3-FmPPvmdsl8EaZmfzkN0q6Q3BTiQIWyCeEE6MRCAhLNQx4zo7aGZ0ZTTd8grxLSbTiN9bQEuKLK1WbrUdr0HGOusKOsqsshwCcVTVGya17LhtSPVNBDqt8_TQ5N-G9AmnljjBc-xUJ4Qw7Gt0Cx-Lk0f2Wz8FTDQFYbwpDpOqVFmfyPy_FpiURIhP2FqedXJ2Rlz4PyRXdAoaVLzprK2UVD72GyLc0WrjjxtDqcjJAo6mCnLLhcF9ZbUfwUuXh-Spzh2-VfWUZhWGDUBUxFEZsUXAzhSrkadV4UIN5t5LszNBWDByx_pKLr98jKQ1gRwJhgm5R6Umgfk2hX8QAmo04HnGjYPGodtyLT4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول آرسنال توسط کای‌هاورتز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/104333" target="_blank">📅 22:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104332">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو و متئو مورتو:
🇮🇹
برای مالکان و همه افراد حاضر در اینتر، لائوتارو مارتینز فقط کاپیتان نیست؛ او نماد باشگاه است.
❌
هر پیشنهادی که ممکن است برسد، بررسی نخواهد شد. موضع مالکان کاملاً قاطع است.
✔️
با ایجنت او تماس گرفته شده است؛ با این حال، تاکنون هیچ تماسی بین بارسلونا و اینتر وجود نداشته است.
🚫
اینتر قاطعانه ایستاده و پیام‌های بسیار واضح و مستقیمی ارسال می‌کند مبنی بر اینکه لائوتارو غیرقابل فروش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/104332" target="_blank">📅 22:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104331">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPYRR1XffU4KhE-aRSxs-K5jbqEHdGIFpAY_U52lG37q8zvR5PsH92BkW4CSxkntsib3Bjefkb8L3J0Fylp2lIJNCUkwJN0idCGQqBQ7SGmRuXpwdZSNQUhV_QNQ-LNZ9SW8WD_xR_tX7OHC-qspXqO64MsUB9S0qyoWN5k1JCB3mnl-7DlRDAQl3AmuZTYPYObtwi7Pkp7YlDvlIaRb900ziyb8nbZRh3YcHom6l9fuCwqTA2Lg223kXupK-i_ZglNY45_LEId4Cq91iMSfRRpHxNkv8LKyVa5mqfsyQB651BtXoasSYDK0XYwykyqhkmXS3rtp6K1tKfD9EBpy-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔵
#رسمیییییی
؛ مالکوم از الهلال جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/104331" target="_blank">📅 22:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104330">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsWr_rQPDmX6Fa-Q16zPEatbkzf2fQ9o2TzA-qO_F8RMhorU3AasnQOG8_6vAkHdAVPTij2ix6zB8vV6inbkZ2GnyflX5N7P1KqHe3bY7cclk2v7QcUTCkXIUmCN1M6-l0Av7-5gYK1LSCnFhmuC0dnhEHp6v7z9bJL3IFVw3UH-8YgImkiY0ym_GOBi4eWxIRQWfh5MgySOZynJJhCqu-UqTr5ny10cp8an5dpKN19IQXbbWPsaEuo6WYYNdiQN4Y43GQEcB9gLcwiJc7JJJi8IM_Am9sWJ_pQzIPztT-P89u5R22gqFHgM1eynDyZsCDQMGn7DGmFI6M6NEgNUnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
از متئو مورتو: بارسلونا از انتقال خولیان آلوارز دست کشیده و این بازیکن رسما از برنامه‌های فلیک خارج شده
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/104330" target="_blank">📅 22:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104329">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f670f0bd57.mp4?token=ADzc6T2pqefEuYjzYD3-o0w69dl_o-swUN8P0wyxqTwLH_-QdORoeP--LjT3qosVbTC4If_P-8xoqxkooWpz5GtsT1CrXMIn6RFKLJN01Kuc0LRRGlrgwnGBavbb3eW9fg81tNsiia-IKltLtPIYsnq7IFpwhegeME2nXsdL12FDGyQcX64nYDyb9UG1eom0Cl607kpR7aZ_42EUmXjQrCRxlCK9NXWCApABA7x5uz5PEgHimyd6hCrZX3gYpVfOy2zeGtQR_Az4yG_PHhw1kOkUpsuTfqTnRydpsUnL8DfRJAd9n2HVr21fWddbv4barDvT8sbzAv9CeaezZOVdyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f670f0bd57.mp4?token=ADzc6T2pqefEuYjzYD3-o0w69dl_o-swUN8P0wyxqTwLH_-QdORoeP--LjT3qosVbTC4If_P-8xoqxkooWpz5GtsT1CrXMIn6RFKLJN01Kuc0LRRGlrgwnGBavbb3eW9fg81tNsiia-IKltLtPIYsnq7IFpwhegeME2nXsdL12FDGyQcX64nYDyb9UG1eom0Cl607kpR7aZ_42EUmXjQrCRxlCK9NXWCApABA7x5uz5PEgHimyd6hCrZX3gYpVfOy2zeGtQR_Az4yG_PHhw1kOkUpsuTfqTnRydpsUnL8DfRJAd9n2HVr21fWddbv4barDvT8sbzAv9CeaezZOVdyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
حس و‌ حال مردم وقتی مسئولین درباره افزایش قیمت بنزین صحبت میکنن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/104329" target="_blank">📅 22:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104328">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKOe0HiO3DxP5e7HLuQbHa1p3Hj192rlnNlySOTjxa9zq_-DLgaB6FjnA86-eVtFQm4mhcWRW1DccecB4_RodQp31fxXLav0ODpKoHnriSR7JHwPn30YV907cVhkvV7hXFCint60yAlY-XyO1_jaOfDZLwg5LXBZD81gN9PhJOBOCzPHuGY_-AzlaNKs9I7dIGQjI9aNn7cVlgLyc_flXS4sv4ZN7upWqIQxeHwWDlITpMo9T4JlT8NkQTbsiwnmLR7nnMHrAfCrnhdjEA_1KKc3klDGFd1D8LWcUZ8Fe86zZ5baFUkw3pdTNNsfTA1LuK0qQDN9Zq-JsQvIsDM2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#رسمیییییی
؛ کورتیس جونز بازیکن لیورپول با عقد قراردادی راهی اینتر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/104328" target="_blank">📅 21:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104327">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtcMgm_riC2ATCEykw898VQj894armpHR54iO6-WRdVIKaNY6zb3PooeHxu9aQBTsHbGUwOh4V0PfHYVktwc0IIThiDfDnn1SXBHKZi8uqT9KCzU42R0dX9SGro4nEbiOLWtuHuKSW2AZxNcJNuDRHK2vrM4XYLB7zRjtTEtN08T9SPxDf76O0hPZ0vChgJFsOryJ6dAU96lrR6VY6lVZo2ARn9a3C0T4jmsYxmbSuGVvQVm1kyifw7WxErkOQE0kkieMOyXMgwj5Pyg-a_DR1A3emfVe952EJRnEfjqBc4HXjaPKqk8lHRpD9R5I4_-TvO0yTRmkW9omvdA-aKolg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گلزنی رونالدو در شب پیروزی 4-0 النصر مقابل الریاض
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104327" target="_blank">📅 21:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104326">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91919c1481.mp4?token=NfJJhKykmS8UpzzxrkvVd4AK1g-76HMiWTgwsAtxdvK8bKBNOGv7H8ujJ1uHbaVlaR8KLzHu1yOFF2cCdbYS70NcocxlHQ7y8wPElF22kCGyYjYAEJK1CounSPXWFpKqZdJ-RwSWHs4fX3ZZM8yw-jDDD3j5x4w2qkF13BBxhp_t5cAznW7xX_0h-cSZdNo6zmER1Axa-IWBI8Lxqv1CxCtvrScDYcXDlGd9k40blDCnW9DiSPPZG24Kla1s75SJ-OhUoEUSCuowcmIepfTt1voou5B_ZMHQNXRAbHeIHn_QESK8CLBqkMqiujDLwDngKUP4xx5GFhxaXZUZygBTqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91919c1481.mp4?token=NfJJhKykmS8UpzzxrkvVd4AK1g-76HMiWTgwsAtxdvK8bKBNOGv7H8ujJ1uHbaVlaR8KLzHu1yOFF2cCdbYS70NcocxlHQ7y8wPElF22kCGyYjYAEJK1CounSPXWFpKqZdJ-RwSWHs4fX3ZZM8yw-jDDD3j5x4w2qkF13BBxhp_t5cAznW7xX_0h-cSZdNo6zmER1Axa-IWBI8Lxqv1CxCtvrScDYcXDlGd9k40blDCnW9DiSPPZG24Kla1s75SJ-OhUoEUSCuowcmIepfTt1voou5B_ZMHQNXRAbHeIHn_QESK8CLBqkMqiujDLwDngKUP4xx5GFhxaXZUZygBTqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گلزنی رونالدو در شب پیروزی 4-0 النصر مقابل الریاض
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104326" target="_blank">📅 21:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104325">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e061ffb68.mp4?token=Ax9DnHnXnyBZFbb5RNTu5JlSgER7xmR2oWAvXELqOT7XO9nPJyh3kL-xiz0vqRM605imbgsR2iFxfaYKzQWVddWgzfwd5MWeU4rLhTU-eLnlUtH7BjUFwJEUQH6YG01Wq_VNp5jKVPsxpUG5AFF74Bh_RWulmSHhDRiflnbSPEOEKQHJ41zh5vNHH1nzE8k22fumnr5vm-SqMvNBHGqAVAodiUjrSwP_Ca-l8dfohzb0lNVABQqT3sPL8Xzb-QhBo2NwH96aezSy8-zHtKord7UMpd44YI3Y_9j7lB6__F9HPjTyQkCU7EtOZKqaYE2LIvQOQ426Qi-Thyf0Z3p6yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e061ffb68.mp4?token=Ax9DnHnXnyBZFbb5RNTu5JlSgER7xmR2oWAvXELqOT7XO9nPJyh3kL-xiz0vqRM605imbgsR2iFxfaYKzQWVddWgzfwd5MWeU4rLhTU-eLnlUtH7BjUFwJEUQH6YG01Wq_VNp5jKVPsxpUG5AFF74Bh_RWulmSHhDRiflnbSPEOEKQHJ41zh5vNHH1nzE8k22fumnr5vm-SqMvNBHGqAVAodiUjrSwP_Ca-l8dfohzb0lNVABQqT3sPL8Xzb-QhBo2NwH96aezSy8-zHtKord7UMpd44YI3Y_9j7lB6__F9HPjTyQkCU7EtOZKqaYE2LIvQOQ426Qi-Thyf0Z3p6yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
واکنش دیدنی و واکاشیزومایی گلر الریاض روی موقعیت تک به تک کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104325" target="_blank">📅 21:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104324">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdplxfF9K5FO49cessI156WUJ2kN2U5Fmib-nDmDYj5ePYOn1u1FDXsmbFl_R9IMD2wakw2WqaBb-_gIaVHqM-wKAYcQFjXz_sA5E300JGWgKV3fKeBfnfO39vHWSKbTjrqk0-GAK2N0NzgYVNduWe-o6AuWjsmAFZgKrao3cnm6ajFPOUFPEe3Kc3Dep1JAmrt5tg5LQ8bCmHB3X7FePcMRE3IrCX61dhqHxZ-VXvrPP_lU1VOuVHhNlGjXgusZNyObEOjTG6rUcvEqi8erBK_9AdWltew1huIf7WyDwypx_Wo9UvsWVjKywHJBOzATaWXzs7PC4sV68MGvybquBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیبببب آرسنال مقابل کاونتری‌؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104324" target="_blank">📅 21:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104323">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9ah3wiv_eNQYzvh8G8aE3mVn7CbaFuJ1XZp6F9M3lPPp3nGOMWyR97pZZTj2CsXDovaD0bwOI3RFsq7BpUoNRDZlB44OulculkuCtkoBEAf2yyf1Zlq2MR3RUxqlzTbsKTBWi0j4GIXeRjVdr0LUKzlNvLWOtRfRT7zhvK9JRo4hGZNmzwDWIOpRx92V8N-qGgOUB--QYIuPHPmgP8BbvLyvo-r4QIPqoSY7EHSOuk4Rxa2g5AE1AKDyrQq3-3vIvqaqbp0jIVzQU2-a5WZBnutS84LSs9JeFzIU3KlhEMD454NRz4WZS-ChN3gRXTbTGazM7HnLvKwIsNzh6JUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته اول لیگ انگلیس
🏴
آرسنال
🆚
کاونتری
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗓
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی در بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104323" target="_blank">📅 21:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104321">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5c212597e.mp4?token=HswiXbvaOWhSpFJQsgsd86MsZni1zjqg8gvo78l6nTvAxkWlY1zpIGDRs95HAWhH-MHzO2tCMvrqHbRC6Cv_Wa0Q3EaCYQZg2KcoOok58BsYoB2Ddach4EZ0Yw7d2VO6EO-JjXaz_i2gQhRFESVnH_aWEPkfA3X5v1V4wAI6poc9fD3w3AdfyyhPfqUrNrF31wydokWcea31KfIaaIharfeAzZiMCw2g3qQ-L34P1bIj8h798iRacXf0VDUhd0fXvm2WQjt194Y8Y62bdoMSqk3ADesOVuDTpxY6yJlkVvGK1QvyuoZ8q-qtECQEn_ZXK2tY3676A50CSt-NQoi5_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5c212597e.mp4?token=HswiXbvaOWhSpFJQsgsd86MsZni1zjqg8gvo78l6nTvAxkWlY1zpIGDRs95HAWhH-MHzO2tCMvrqHbRC6Cv_Wa0Q3EaCYQZg2KcoOok58BsYoB2Ddach4EZ0Yw7d2VO6EO-JjXaz_i2gQhRFESVnH_aWEPkfA3X5v1V4wAI6poc9fD3w3AdfyyhPfqUrNrF31wydokWcea31KfIaaIharfeAzZiMCw2g3qQ-L34P1bIj8h798iRacXf0VDUhd0fXvm2WQjt194Y8Y62bdoMSqk3ADesOVuDTpxY6yJlkVvGK1QvyuoZ8q-qtECQEn_ZXK2tY3676A50CSt-NQoi5_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
‼️
تاجرنیا با کنایه به پرسپولیس:
🔺
اگر استقلال قهرمان اعلام نشود از طریق فیفا و AFC اقدام می‌کنیم اما مثل دیگران با لابی های سیاسی پیگیری نمی‌کنیم، این تبعیض باید تمام شود، آفسایدی که قهرمانی را از استقلال گرفت از ذهن هواداران پاک نخواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104321" target="_blank">📅 21:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104320">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9ApoSs23lv32_q0bzZNxDyf_NAUpwhHRloK_9tyZPcUku5Zm1PJY76Bqh180U1cw_BBn4AOXeW7miiOBbNiz8MVM0ibk9qGs0486P_IPlrjcMWK3fe7zLhYiQuuNd-jqCBxOQn4B3ioyxNcOzUrnB0RdvALTBCKpSr8hPnB0343re_C1qX7P4zSPTe7aPy7LILtecqYu2tYoInI37Nvl9ww2wDRUAB164kB-MHRhT1N07u_bFdQpsv2ZkPDTc96Ekjh8BcBPaOnDVvSWq3cSDz2Ts65W5Kbufchpm5OBy5bE84qdlhAVmyv2GrQ1ZQKriQIiXUosYkSilz4Eh66QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
لائوتارو دل‌کامپو (El Ninee)، استریمر آرژانتینی و فرد نزدیک به اطرافیان خولیان آلوارز
:
🔻
اگه بارسلونا مجبور بشه منتظر بمونه تا اتلتیکو اول خولیان رو به آرسنال بفروشه و بعد سراغ خریدش بره، اتلتیکو هم باید فکرِ خرید بازیکن از بارسا رو برای همیشه از سرش بیرون کنه.
🔻
یادتون باشه یکی از جاذبه‌های بزرگ اتلتیکو برای بازیکن‌های سطح بالا، موندن تو اسپانیا و مدعی بودن تو همه جام‌هاست. اون‌ها با در افتادن و جنگیدن با بارسا، دارن پل‌هایی رو خراب می‌کنن که قبلاً باهاش امثال لوئیس سوارز یا داوید ویا رو جذب کرده بودن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104320" target="_blank">📅 21:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104319">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CuSch-oc2IHkMdK5naU4TFznQTJXdLDYsjFeLjmHa8ScDcxVAXbl1X_A5UftwV9tRSbZGbgEAxwlLsdyEFDB2MkdV-YPf7Ot4MWa8ZHztyM1ONmSNxjDvtZXspbGZCdA3Qpx91AhNn5HACdWyBjwSAJE9826wy0N--acjKw9DSeQW1HfbM9fYjGetRCcLFWHLBTlSpBrmLAOxiFTm3zBubBu0VAJSE00yTn_AgczO-eYi7NqpS_CvDvJfoFPq8x4THFR5Z0AtfUqtMQTxTjX2mIT23LxqrOIwaOc3YahxDCQf-JKWCjjLIfMXpxMh4PQS3gFAX4qq_6cMvCYGKN86Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از بن‌جیکوبز: باشگاه تاتنهام بزودی قرارداد خود با عمر مرموش ستاره سیتیزن‌ها را نهایی خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104319" target="_blank">📅 20:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104318">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrJjujChkbq62RQETSPUGhhPXVeD7vhfaScjZ5s6KlqyXVsvzuTISQSc6o8GpbGPaq5pbkkdVNe_VNn_qmBJUveXC-U4hFzjD5kpGDaeQc7ck7-e92Foavg9Y9fD57f-SQvWUYXmqUGUr5lx8DFIQ50Wkwl3rua5cHbVn66ZrRuIgwTI8oglGz_e7VpJYXeQADpyqL8gceu7Kpy-zrBqDCu4Nr-EqV23P8tlr--T4OsiSjz9cttohSapZK9hcq4TM0HO3WeOeffzdk80rzA9kIynzTN2IDAh4kDT7TNTsDrZNLBOXaJABihWx74g3NrCJqGC4p1eAne36ZWL9cee0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از بازیکنان لیگ‌فوتبال بانوان پاراگوئه
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104318" target="_blank">📅 20:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104317">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDIke9QNectM36JYED0P5rArpdjWLtx8sMYvuKdXhRnnfxwgKT393nhsgWrEEmeWgj8rAnf5a62TLGbTEkCUx94EXV7YJCneqy8PbSJHWJ1qMXc2HkNJPfI3vJP99poJz8XwadoXsDbJHWI8wzpuW52Z9nOEN7vWvi79Yu5lthR4BDfOyZa8MksMT3QrKW0ebgbpxGH49UVoj7MBri8bHCFiemKtMRK8OrxdSCS_I5sVLhMQ5DKAuTbZ546SEh37g3OVcsQ--8ZYUY4qKlqF-h49KR0YZkivQC_rMAZ6NzwtqGzR80Z3ks3MKeb630nODYvaICagPkBURbEiRv7PnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
میگل آنخل خیل مارین:
🔻
اتلتیکو مادرید به حمایت از خولیان آلوارز و کمک به او برای ارائه بهترین عملکردش ادامه خواهد داد. این باشگاه اجازه نخواهد داد باشگاه‌های دیگر در استراتژی آن دخالت کنند یا تلاش کنند تا تیم را از هم بپاشند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104317" target="_blank">📅 20:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104316">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c62d1ca0c.mp4?token=CTWAGEqwGZqeipkxQDaV_Wbz5n6r3HEmUn74w7A6y6MUU1BpiRXaZ5CGHF89MIZoJ1Uc5y9UVglYBbD4jFhsDimA19PssEUnaoVfbHyjZMJngm1vwyCD7Zeu57fFTdY-upbNed0hsTySTLclJMUkJr5GB7fAa-PlgZW1wWLurfCo8f1A_msMXaP_Y9VrpDx2heCZgEsiC6YT1IBw_ztmSCnQqdBCplSpxcmHHVpVxpVxEX4EJbHu9svPDbziKoT0hp3IL5ccsrBnbcqMexlI4Iq49Z5a0HgmlzirnouzXjEk-0dWypejbWPy1Dyx8YGLGcWc82QZmwD9PQlXgm8Uog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c62d1ca0c.mp4?token=CTWAGEqwGZqeipkxQDaV_Wbz5n6r3HEmUn74w7A6y6MUU1BpiRXaZ5CGHF89MIZoJ1Uc5y9UVglYBbD4jFhsDimA19PssEUnaoVfbHyjZMJngm1vwyCD7Zeu57fFTdY-upbNed0hsTySTLclJMUkJr5GB7fAa-PlgZW1wWLurfCo8f1A_msMXaP_Y9VrpDx2heCZgEsiC6YT1IBw_ztmSCnQqdBCplSpxcmHHVpVxpVxEX4EJbHu9svPDbziKoT0hp3IL5ccsrBnbcqMexlI4Iq49Z5a0HgmlzirnouzXjEk-0dWypejbWPy1Dyx8YGLGcWc82QZmwD9PQlXgm8Uog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
خاطره عجیب حنیف عمران‌زاده از شکست سنگین استقلال در دربی
:
🔺
آرش برهانی را پرویز مظلومی وینگر گذاشت تا رامین بترسه ولی رامین در محوطه جریمه ما پارک کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104316" target="_blank">📅 20:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104315">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2950ea1958.mp4?token=FWE1Y64LMnjCFlOowyet9yunmTNFoLtvHX8zASl--oeHDffWgJQ5mY-CZkT0JZOTvyR7csYU-UgY_o7NDIfcg5UL06FMgDGFMYrt1qQBE3nBe97CRgyhm87IShV0c-wgJJHiIMLpwsK82RjVK8VakRkA9bQqMhJdeA52yloK88Sn5YI1BmFN-703aRLfPyY7b3vxtiys1h_oCUYs4lb7lNQDSBf-Da60ORddZwzsognIFXahbpU13U1UivBzC8-tTc7eLibxpTm4dLR5Xbw5v9gGZjVWBrvavrs95RginxH6AWJUFsTuVwUNgU3ymANA0pIsksSWYBgjPYoRWYS-N3koHbpJymC26IrBym49OJwsgMJ0ejjGIpn5NjKBgtDryu5WDoGYA3IJAs0axlHdvv3eASmS74RTlGPoghOnify6gisHtXde_8McsK4nXyui8ZuS5CICqmBSTsUQxokdoxQIsHo1K1KxPgXrbp6wV0rBL65_0XdND-yLYeXgtDXcMKaj7k0dQMmr_4KUowM1zECMgBUgcbenjsMkyMtquaNSxL4aQfogL9br0ZGCOkCvYGgtDJP4ay69zCsejWGu4kfLmzA_ZucfPxSfcpZWhUyRhVgSpRTH4HMQ9SOcgnMwEA86NT1CVliwZ2I9fROniQFeMYs_oXpk-EjBvIqYFV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2950ea1958.mp4?token=FWE1Y64LMnjCFlOowyet9yunmTNFoLtvHX8zASl--oeHDffWgJQ5mY-CZkT0JZOTvyR7csYU-UgY_o7NDIfcg5UL06FMgDGFMYrt1qQBE3nBe97CRgyhm87IShV0c-wgJJHiIMLpwsK82RjVK8VakRkA9bQqMhJdeA52yloK88Sn5YI1BmFN-703aRLfPyY7b3vxtiys1h_oCUYs4lb7lNQDSBf-Da60ORddZwzsognIFXahbpU13U1UivBzC8-tTc7eLibxpTm4dLR5Xbw5v9gGZjVWBrvavrs95RginxH6AWJUFsTuVwUNgU3ymANA0pIsksSWYBgjPYoRWYS-N3koHbpJymC26IrBym49OJwsgMJ0ejjGIpn5NjKBgtDryu5WDoGYA3IJAs0axlHdvv3eASmS74RTlGPoghOnify6gisHtXde_8McsK4nXyui8ZuS5CICqmBSTsUQxokdoxQIsHo1K1KxPgXrbp6wV0rBL65_0XdND-yLYeXgtDXcMKaj7k0dQMmr_4KUowM1zECMgBUgcbenjsMkyMtquaNSxL4aQfogL9br0ZGCOkCvYGgtDJP4ay69zCsejWGu4kfLmzA_ZucfPxSfcpZWhUyRhVgSpRTH4HMQ9SOcgnMwEA86NT1CVliwZ2I9fROniQFeMYs_oXpk-EjBvIqYFV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
Premier Legaue is Back
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104315" target="_blank">📅 19:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104312">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Koe04OvAPNN9b0xT5lmhFqxTLKaX0aeocqXYEK80c9_FFGkMS_UKB1uPDMERApOMZx4yYaM6BRWZiWkY0D_IA1ydKOchUuuB50q6acOvIkn7dcTfvTu_Xa1Fi_a_oR8fSgNjU4EXfqjZQaNalb_jcvgfcpFhrdjEQ2d6GL736WbB62wAtL9kJ5BkmwOVBK8YiX9kL_PoKKV0BnIFjE4KpZSfoGR-8PaAicujOcd0s6PXqrWajKyb2Mi1Xj3KzWcY2cGxB-1CiYfh8GWpBXQtlDh0tW2pvSNA4CllvaXJdmr50lenMjhPtgA3CG_Nx2t3HiPh-34xj4scJkXAx1w6lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#رسمیییییی
؛ قرارداد رودری ستاره جدید باشگاه بارسلونا در لالیگا ثبت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104312" target="_blank">📅 18:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104311">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👀
🤯
یکی از سخت‌ترین مسیرهای مانع جهان ملقب به «Obstacle Course Racing» به اختصار OCR
🔻
ایدا ماتیلده، ورزشکار حرفه‌ای این رشته، وارد مسیری می‌شود که برای عبور از آن فقط قدرت بدنی کافی نیست.
🔻
بالا رفتن، پرش، آویزان ماندن، حفظ تعادل و عبور سریع از موانع مختلف؛ هر بخش، ترکیبی متفاوت از قدرت، استقامت، چابکی و کنترل بدن را به چالش می‌کشد.
🔻
مسابقات عبور از موانع، رشته‌ای است که ورزشکار باید مجموعه‌ای از موانع فیزیکی را در سریع‌ترین زمان ممکن پشت سر بگذارد.
🔻
بعضی از این مسیرها آن‌قدر دشوار طراحی می‌شوند که حتی ورزشکاران حرفه‌ای را هم به مرز توانایی‌هایشان می‌رسانند.⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104311" target="_blank">📅 18:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104310">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">امروز تو ویپاری رو برد آرسنال
⚽️
100 دلار بزارید 245 دلار (25.000.000تومان‌بونوس میده)  سود کنید.
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104310" target="_blank">📅 18:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104309">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari (3).apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/104309" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر WEPARI
😀
😃
😄
😁
🔥
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 120% اولین واریز
‼️
🔥
بونوس برای 4 واریز اول
‼️
⚽️
بونوس ورزشی هر دوشنبه و چهار شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🔥
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
📌
آموزش نصب برای IOS
g39
✔
https://t.me/WePariFarsi</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104309" target="_blank">📅 18:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104308">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHlgM1fK7c_C_E6EqbICgZdrllfzRct5zvw9d-Ob_Ud0v32dQ2at3ywThfjE3089S0Pn3FU0ZTkPpa7rGSq7MBnUDqLsQ_wIEk5zfLBm5ZYKg-T1iFiLy4DnYGgLZhWl8WdZA0XWnUhEm_SO0_fL4EmbKwYvugkII7QbTiFdlr-pKSRAJUo7K1w4j_YZHu_rzpXM0-A-CBFrmKWhR5mjhDsybRolTCWBc7WtUsXgJnE6j_VXb4uE09gkuFIuwJ_o1kthwmcjgq_zIl_YMaC3UzF-GoMcpJSrK4Wz4bOy25L_7bcfXQF8965NiFc9bMxduMCM1yLkzzkaM6c_3tnoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
#رسمیییییی
؛ باشگاه سپاهان اعلام کرد که سعید واسعی و امید نورافکن بدلیل مصدومیت دیدار روز یکشنبه مقابل استقلال را از دست می‌دهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/104308" target="_blank">📅 18:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104307">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHl5FWd9A3AUHOEvdqa5ikHwrRUdrpeUlAXtRx3GNkP8RYLRhkH3kVPkSkjdNoJXftbwp-x2Zmt4IYhLz69qCzmxCUrSAmKyxGhIHrgNYcOAKRh_I8XVQ0eCZRIMbZKrtKT0dYlnMy8lLCFWqt9IZ8HO9SqE8gK-Zp7jHEAOcYjlKrfp7RNpW69WYjm42jKvPrXjaPPtCUcmSx175RpKiUcwehXZ0UGsiUb5WYoPvo7m7sgoyUCvY4lI2ADuOjAX6GrK3mOCuFVyuUwEGg2ULJNfO3VMsKuUbRgwPTKYyAxQeiRGvV_kX4COBri_Xef_nouNOimPRX5CKz5j3nid4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇵🇹
نیمکت‌نشین رونالدو در بازی امروز النصر مقابل الریاض در هفته‌دوم لیگ‌عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104307" target="_blank">📅 18:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104306">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z0cDz9HqXghiPMXWBrdDlz32_jE73RlsrF35k12DWeS1yO5oJIyXxdZpbU8JsKcuOKZclyKSyOCQc3tVWpKwyxR3_Cp3IGmf0_0qn2d0Xolr2uAlRxDpCicYRV8OpYJ0lmhRpX1Vcw5jgkV9gyDfl115R4bEgJAHOVAsvBWTVA_35XGYkeUh7i9VPmktV1ZJGwrmUgfMSxLbq0tVgJirnEKrf1BuDrhviRsPeDrT2IUj28Kzq0kQrjLXLRw7dCldJ1HR8Z8FLZbCvy5T5GNo29cu9bJAb9rWI1Knjm05DnH56CYdXxL0b43LTDWa2yydEPT357ApKFxTDa0LI6navA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
#فوووووری
؛ جرایم انضباطی فیفا پس از اتفاقات فینال جام‌جهانی فوتبال:
❌
لئاندرو پاردس: 10 مسابقه محروم شد
❌
مولینا: 7 مسابقه محروم شد
❌
گاوی و آلمادا: هر کدام 1 مسابقه محروم شدند
❌
فدراسیون فوتبال آرژانتین: ۳۲۰ هزار دلار جریمه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/104306" target="_blank">📅 17:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104305">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPZMrPNm_bC9NuM-YaSnLD3KqM7zUbuDKWN7pa7jMHh4hRKuS1QufcP3uYJkyhlQThEE9y2yQrgMbkS55GgcB_NPWCIcUcLKsKnxA-vj7McgheiZMS5i10J4vU4t-N57FDLkMjHqrNd25mEclgvz3lhSMwz8k6txoczc1Ndp5AwqoGsHF4NkR_HS91oWP-tPXjoLsPn72MyOCgGyNIA9tz8RDacJMnkGDCZFrerGCca4hZOlh3_nzXHSXSBFLTFqU0rganiiB_6T8fMgbKbNjlDk_NDR4cvuvJSZzIEQVg6nChrQUWY1xBPO0PkQDo-D0FP_-9oroJPt-9cyZDr24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
لیست تیم‌فوتبال رئال‌مادرید برای دیدار فرداشب هفته‌دوم لالیگا مقابل اسپانیول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104305" target="_blank">📅 17:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104304">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOslcqUXwXuc6tASWAkncMLgwie6x_YAtefxZOFJGEjjOwu8HGS4ukZKzrtP7k9WpBq8qcrPTdI-XeMhMhxPIRlYWOqjAco9vNYhRM5cblXk_2BmjT0uZ9WJkMTdxYuxDxmGoxaDxMzzD79avj4FrSb1xfm4qnxo4Am-vFEjhkaesehdZFwgQSUqZ4bQOcd4AqqW7y4GX6flyA8Y-WOhMOMvs986KOknZtarEQ2GN-RVtEd1Bz8TDIfgN1IWvVRbwZ5IR2ywmy3h8GUSM7BBHFRQyjrn-MdImODvU0ZJVx0Z5YTQUCVhlI6E9EB01kL3wRNdps_PJ5MH5MNc2xguFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اتمام حجت اتلتیکو با آلوارز با سه پیشنهاد:
🫱🏻‍🫲🏻
تمدید قرارداد و عذرخواهی از هواداران
😡
سکونشینی تا پایان‌فصل در اتلتیکو
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مذاکره و رفتن به تیم آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104304" target="_blank">📅 17:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104303">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a482d69c0.mp4?token=U0VsQwOIvvq4jTJD5wVsjjqFs6kIntYl-ZEQiLI3LI9qBwRiNXaMQFc5u3cQn8xEzRy8cmWfiOTKPQgj7RI9pFb7Uw7SENmTJOr7pW3hLCbKous4n7OuR5pnLVne_7AZnXaLoAXCTwrqNc5O2bbFIJPQqYv9imyhitzSiMBNjXaMFN3TOYdjJxs7h2XpixNwRA3xqvUDIuz6MPtxgh6nm6HDn2FYibtoQ-alnqNScfJA6pW6fgd2g26JPD2l6bmItzA9_g0tJisJXg0grnWK0-ShiTNb-AuBH944EvZfFKg1wm_gdKRWiFkvDoBnNBa2_BaMnlNNDqmSHbj2ZKnLdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a482d69c0.mp4?token=U0VsQwOIvvq4jTJD5wVsjjqFs6kIntYl-ZEQiLI3LI9qBwRiNXaMQFc5u3cQn8xEzRy8cmWfiOTKPQgj7RI9pFb7Uw7SENmTJOr7pW3hLCbKous4n7OuR5pnLVne_7AZnXaLoAXCTwrqNc5O2bbFIJPQqYv9imyhitzSiMBNjXaMFN3TOYdjJxs7h2XpixNwRA3xqvUDIuz6MPtxgh6nm6HDn2FYibtoQ-alnqNScfJA6pW6fgd2g26JPD2l6bmItzA9_g0tJisJXg0grnWK0-ShiTNb-AuBH944EvZfFKg1wm_gdKRWiFkvDoBnNBa2_BaMnlNNDqmSHbj2ZKnLdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی توپ، داور را از بازی خارج کرد!
😳
🏐
🔻
در جریان یکی از مسابقات والیبال در سانتو دومینگو، توپ با شدت به صورت داور زن مسابقه برخورد کرد. ضربه به حدی بود که او دیگر قادر به ادامه داوری نبود و در ادامه، عوامل حاضر در سالن او را از زمین مسابقه خارج کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104303" target="_blank">📅 17:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104302">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
واقعیت‌های فوتبال امروز و‌ ۱۰۰ صدسال گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104302" target="_blank">📅 16:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104301">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b4df9ad5e.mp4?token=sVs0XqYAxQ0aB0YBm_cWSe0kTjDnS7Dw9wVZrvXwFIfiwQJRWKyK0MuKnhyHw2iGvBwIXWJB3fyMYhqafSTBHcbPABpPzbOjAiP4wFiW4WF6kCW8Phm7_BmNcg1mYU-kKbaq-4VkP7iWSRlTQoxHvlJx4Zltzs3TGevzGB4uNgAsacLmCRjBUcPMCyjhT8qhU9Fs3gW5QRHQTTed3dOu0ZL6WKGy_Wovf_CzV2Ck7Oekv2T9NhpgcxtZnvRsFSjdoE2ABn_gBRPtK40w5NIcF6lzeWNDYCVtza5-Ow1G4kOzdabXDgbaQoxjhaOulZ0XqrSGYcX6rYlIyg2gIlPj-gueAMiTRTdA_cj95FjmV0Ijo9dnBmHZagRzlH4xKZBxxgZ2Ywpq5zGTHmXoOoEWHNNDp_RdnbKs7deGSraum9jiJU1Q3p8rlv6hvX4L46RhAZi1FONSvrkBoURwva5Lj2g5WVWXa7jsfhZyJLz6jTvEol_ISe4zaG7IS3ERJOrH_QvnxJPTadbDScFp6lrbrQjDdkXwD6GPqDARr2JVOCASN8B9pge60Al4OQtBYhd0KZ774iyUIrDq5DzENB6mJ15KrKKQmbq-qAv2KyrjO2DB7IiEWYCLEu2m8r8tFK_sVw2leNyBXN5yIl7WcLDynb1R0Eq1UdQxkbvofdA3Pr4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b4df9ad5e.mp4?token=sVs0XqYAxQ0aB0YBm_cWSe0kTjDnS7Dw9wVZrvXwFIfiwQJRWKyK0MuKnhyHw2iGvBwIXWJB3fyMYhqafSTBHcbPABpPzbOjAiP4wFiW4WF6kCW8Phm7_BmNcg1mYU-kKbaq-4VkP7iWSRlTQoxHvlJx4Zltzs3TGevzGB4uNgAsacLmCRjBUcPMCyjhT8qhU9Fs3gW5QRHQTTed3dOu0ZL6WKGy_Wovf_CzV2Ck7Oekv2T9NhpgcxtZnvRsFSjdoE2ABn_gBRPtK40w5NIcF6lzeWNDYCVtza5-Ow1G4kOzdabXDgbaQoxjhaOulZ0XqrSGYcX6rYlIyg2gIlPj-gueAMiTRTdA_cj95FjmV0Ijo9dnBmHZagRzlH4xKZBxxgZ2Ywpq5zGTHmXoOoEWHNNDp_RdnbKs7deGSraum9jiJU1Q3p8rlv6hvX4L46RhAZi1FONSvrkBoURwva5Lj2g5WVWXa7jsfhZyJLz6jTvEol_ISe4zaG7IS3ERJOrH_QvnxJPTadbDScFp6lrbrQjDdkXwD6GPqDARr2JVOCASN8B9pge60Al4OQtBYhd0KZ774iyUIrDq5DzENB6mJ15KrKKQmbq-qAv2KyrjO2DB7IiEWYCLEu2m8r8tFK_sVw2leNyBXN5yIl7WcLDynb1R0Eq1UdQxkbvofdA3Pr4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
بعضی‌وقتا دیدن اینجور مسابقاتی‌از فوتبال دیدن پریمیرلیگ ایران جذاب‌تره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104301" target="_blank">📅 16:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104300">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🇪🇸
لیواکوویچ سنگربان تیم فوتبال فنرباغچه ترکیه به باشگاه بارسلونا   HERE WE GO
✅
✅
✅
✅
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104300" target="_blank">📅 15:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104299">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6jcCIpZHdmnJ847hyxzaa64woINE_IIZbamz-LNcNG-FxySArcWm8uhXSBKGOvn9xZfA-Q8WOj2eWjo3DQx7dKkSU6PJGjRBSb-TOY4Qm4CUuBQ3wtdS07ikaYQxa7YO0sbUz9sFhG03Bd_go-U3s2W3xVe0Y3It1_KXYX71V8LxWax0Qf-gDGwRiARnWdqd1e_AZg58vEApZgrtlBGjqVPU_FDzvC4e9A5Wko0U-OuOoDSysm1R2enSd7RFWI7fenlECyjp7xiNztt9BD8_kNbN-ooDONQ7nnW2Hvxi3idNU3jZwZo_5XEJAhndNCRasM_IBE2ZLOPfAefm_faiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇹🇷
#فوووووری از روزنامه اسپورت: بارسلونا و فنرباغچه برای انتقال لیواکوویچ به توافق رسیدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104299" target="_blank">📅 15:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104298">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuGU0PRFEoEduhtDai4oYVn2rELKRWx9VwAv8KegKXi7uRpM3eRmRnSxNjU_HWHGp7crq1rlZpADACSaSBvO1RHWjdGqsLKhNEhXfxlMmUJkVnsNYn1qWRh5_Fgz81gMtyR6K1P4xevycor2-0Vv3ngiH-Q9m2i2EXvDQkkVFN5G7acYwQUaCxgnXqbzLgkwXk3i_OAGVmu4onYrladss2xMRij4Smz6IxzjadQKXylgU3K0byLYLQk6ATNfvnT7UC5DA30ZbJwZmVMWlnEK_Ap3tIkYxUeCLGDDueA0_3nH0GCmdcIUGfmf5GVXKKUdm7PsCMtYja0Y8pDuIZjlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇹🇷
#فوووووری
از روزنامه اسپورت: بارسلونا و فنرباغچه برای انتقال لیواکوویچ به توافق رسیدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/104298" target="_blank">📅 15:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104297">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sP9cfiqGMkU6QBY5r5B8lRi5p-i_6ug2vM1yH3Dk6BJBJcgTQBQ48IjMqq7v11SQ7ycaDkOCWXHeUcsiWksFtPlJQ8LcQt29E2phZyNiNupbAvNaCJ4hix0t2VONNC8aPUwvbMXaG--nA_69VPdTFsnHK71VIjm06xpw3DINuJnDjtZN62aYSvPb8HDjZW4E6lhdL-IpIT5kiwwX27FBadWeEuODG3hZZPEU4HiXUdjIic4X5DwEQWl8SjNchFRFyQuv8Q9r6sEvA-I-P1KRC4pLT-yGEiZezDd6P-fgtCtb_B1EWKXTVyq-hmA0fEevctPnaqWDVWYkEoygJZ3h7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اتمام حجت اتلتیکو با آلوارز با سه پیشنهاد
:
🫱🏻‍🫲🏻
تمدید قرارداد و عذرخواهی از هواداران
😡
سکونشینی تا پایان‌فصل در اتلتیکو
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مذاکره و رفتن به تیم آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104297" target="_blank">📅 15:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104296">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXG8V-OYOjhXwUu6f-Y5iN5pIljCU_K4Mk5X63bFCIh1lkuFSMkBy4SWBpLw9l61Mo7vpfyY-0_wG0lB8O14mw2J2GkP_ySsLp18MRnQGvMoLqy0nJY-LwIWnGO5CPIBe7dKBKBZavXqdLieqKSAOeiVdk0K-QixMBwUJX9sGILeKjnWncumG3KFiHMDGthFFXeNDQlb4XKBK6iLWvr6Y9KsHLE_wUN6vgrMrI77284L4oLdBoW8oEEyXuYA7fc1kyik4tXP3cWf2DJxZKYGrzFlHjfB5RhwDJl-On_O3vION3qUdcJ1YxTJXZE5Fu97DQbCWnruZiJ7hBtji77c8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
میزان هزینه آرسنال برای بازیکنان خط دفاعی
🇳🇱
یورین تیمبر — 34 میلیون پوند
🇫🇷
ویلیام سالیبا — 27 میلیون پوند
🇧🇷
گابریل — 27 میلیون پوند
🇮🇹
ریکاردو کالافیوری — 34 میلیون پوند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بن وایت — 50 میلیون پوند
🇪🇸
کریستین موسکوئرا — 13 میلیون پوند
🇪🇨
پیرو هینکاپیه — 45 میلیون پوند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ازری کونسا — 51 میلیون پوند
💸
🤯
🤯
مجموعا: 281 میلیون پوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104296" target="_blank">📅 15:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104295">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsDBhvJ0GfaepJPAtPXF_-JE4jBgzYmNqRRBKH-nc1qPb6SEovnS4XhQUqhRQX7ginG-uwFb-a2MaVJotNwxE4LFqyHzNV4rRf8VW2jtQmFl1hAzc0Qw2QQ0FGcaVeKjoVfLXq0lGMdcELaOX-emxjTomFdxuZDWvsdA3vb9-DFjVi6J5vEGlxX7lp3pnU-hTJWvVB0Eil4pa01evWxdHNSaZHQtr_nNqIlBcu0kPVyPdIVmjw8bsK0vuKm_7oI3LcKkrTUL8_w2COAfPJc36y_Z90ThV_yrteEas43mHV2RrloZzuaGbkFuq6lVi3YnlvQzvPUnEbZZXJHwNHLx1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ایشالا آلوارز تا ۴ سال آینده دووم بیاره
😂
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104295" target="_blank">📅 14:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104294">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b326cd073e.mp4?token=pb3SxEXFnqh1CB7XXwgrJLOqvkdUa7Reov58P_Vrkx0cKmnfCODma1xHbKEf_-F7sNWxcGZ_Kv-ZENpd4aznawEGlXRMTSQBbAAddRzIyuucULY-GdDSy29VVRRLijlR4Jk3BacPe_GKZDOoK4z7UnsZMfoFZHeyG52JdkHGtfNElmNNW47qmtFGRlOlwRozHdgp0pzbsqFVYAj99jokSXAdoGKOzU8QQX9BwxxYQE4qC04ugdKKE0mJPhlxuNxG4UcYZfvlGMEvZfBYoP4m_2Ne1Tt096PgDOi6PV0HT2p_gZ54c88CB_3QkMtZ6M9ps0HzZ94-f4bEjsu2uEwv2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b326cd073e.mp4?token=pb3SxEXFnqh1CB7XXwgrJLOqvkdUa7Reov58P_Vrkx0cKmnfCODma1xHbKEf_-F7sNWxcGZ_Kv-ZENpd4aznawEGlXRMTSQBbAAddRzIyuucULY-GdDSy29VVRRLijlR4Jk3BacPe_GKZDOoK4z7UnsZMfoFZHeyG52JdkHGtfNElmNNW47qmtFGRlOlwRozHdgp0pzbsqFVYAj99jokSXAdoGKOzU8QQX9BwxxYQE4qC04ugdKKE0mJPhlxuNxG4UcYZfvlGMEvZfBYoP4m_2Ne1Tt096PgDOi6PV0HT2p_gZ54c88CB_3QkMtZ6M9ps0HzZ94-f4bEjsu2uEwv2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
وحشی‌بازی آرائوخو تو تمرینات لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104294" target="_blank">📅 14:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104293">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R52IU4I4pelMCvKX-hVy3IhcA7GgiW-_8c78hjl3og2g7y7i5Vk0SDM-eh40jk6nk_L7u95jpF3R6YqNA1fICkeWwRO9GP3bnfzQHKB17J7NwG_8wj0WjTLfBidWZVrSeiIyt-Q7DIjAwjp_VgolbK-6Yn7mEYZKBOsdGpD1niGvPlZuzuf-Tm43XYkf5qbvMVYgRac9cP7_CgSVu41q-eCZGcnPDyzM2uqgOUcPQs7tx7fUDv72VyWA3AF67gI3QPEHiTVBPjQcf_Ld1ABCMFrjGgk00bAyR6PivreqbulrViNuXRuvgqLnU2rE3VVI_rEBhTcYT-N0Q7QYQv7IKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🤯
تمام تیم‌هایی که ژائو کانسلو در اون بوده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104293" target="_blank">📅 14:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104292">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da3520408.mp4?token=NO9t_brwtsLfknwnu8e0HKtGEn8_zffXHCgJgz2AWZriYwRe8up5F-n6VLznQjS6OKu7vWTQGYf1FgoTe2N7rB9tPW42GdpFY-JUIOnBrYCpdgRwnAgaYmweFqc1h1BtNbezkbL1D-_u-I9HNSFhMPrxIMYYM0C8tfKkAn6Lz4bj0PQS_MhO4ZCZcBineLtbyO6-M837cNzUxrtXNN6N-PUr-TeejkAYJfX1EzKxaCXtKBoG7cATWembF_y7LUD2bKpKKWDlxyUj0tr9qb2K4UhxtgHNcd3VLhhubqLnIlN79bWMh8V9q8OTuUKQ87RIW02LZFPeJQBOxuMtM_29iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da3520408.mp4?token=NO9t_brwtsLfknwnu8e0HKtGEn8_zffXHCgJgz2AWZriYwRe8up5F-n6VLznQjS6OKu7vWTQGYf1FgoTe2N7rB9tPW42GdpFY-JUIOnBrYCpdgRwnAgaYmweFqc1h1BtNbezkbL1D-_u-I9HNSFhMPrxIMYYM0C8tfKkAn6Lz4bj0PQS_MhO4ZCZcBineLtbyO6-M837cNzUxrtXNN6N-PUr-TeejkAYJfX1EzKxaCXtKBoG7cATWembF_y7LUD2bKpKKWDlxyUj0tr9qb2K4UhxtgHNcd3VLhhubqLnIlN79bWMh8V9q8OTuUKQ87RIW02LZFPeJQBOxuMtM_29iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
شباهت فوق‌العاده عجیب گل‌فصل‌گذشته علیپور‌ به سپاهان با گل این‌هفته حسین‌زاده به این تیم؛ فقط واکنش حسینی‌ رو ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/104292" target="_blank">📅 13:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104291">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f86c9cb5.mp4?token=GQqsW7rBOfOOlNx8HloWqLQDV9A3xKnA9cRPjl69qU3JQM1Ts8S2AmAPOKepbJ49uBbK8lOzWDZv3bMaNpKBUD_1AQDG3BKqX8is3IiqGCbOufX-Gd4vQpLpHzDqvRsKtCqLjglRoGP-lroBm644fWLPpRJTHxmUvjT60_fgBK1RYh0U5pxYFBSUMVoPjUxIWGOxmnIYrHrSlE1SrNGrTUgBrw97eFDotUjtnFTNiga7NPxxxjsufxRxj6kmnuqPKHDk9BpmvO245lVGyfGtYyg2CJy75yC6C1oipcsWwcdVJ0yO1wiROqltV0-lfPS1byADlh60YS7tSCFTj6Dm1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f86c9cb5.mp4?token=GQqsW7rBOfOOlNx8HloWqLQDV9A3xKnA9cRPjl69qU3JQM1Ts8S2AmAPOKepbJ49uBbK8lOzWDZv3bMaNpKBUD_1AQDG3BKqX8is3IiqGCbOufX-Gd4vQpLpHzDqvRsKtCqLjglRoGP-lroBm644fWLPpRJTHxmUvjT60_fgBK1RYh0U5pxYFBSUMVoPjUxIWGOxmnIYrHrSlE1SrNGrTUgBrw97eFDotUjtnFTNiga7NPxxxjsufxRxj6kmnuqPKHDk9BpmvO245lVGyfGtYyg2CJy75yC6C1oipcsWwcdVJ0yO1wiROqltV0-lfPS1byADlh60YS7tSCFTj6Dm1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
هو شدن فرنکی‌دی‌یونگ توسط هواداران بارسا حین ورود به زمین در بازی جام خوان‌گمپر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/104291" target="_blank">📅 13:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104290">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyvsuwPbyMAyyxKuKVAtWqirpcceJJITCcqtdRmZEW-A4K94MQx_oR7qafWAx5W1JMVhwJM-vZuHIen7H10durjYdTujHnN_qtuPVjFEKrA_g46SZxQ3SLfYUXD6K108sbqsInnH-ZKqMJ6-IwuO9hPsf5SB_yrsyoKKWGQa9BVDTJ3LggQdWIYpyLKQbn59CBCSSI6GxlZ2WHPhRXgDl-8oWtXpVd4779USXQi8a4W7oc0oaoWYQhgwso1sWsIjG_P0nLsxVKgVYaceWlD1DgYlPyhye5iZjQzRt0f3mMqnVbx_TGuVAztJ92bNpF5f9x8rfc4JdO2d-rwJD-lqdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
گستون‌ایدول خبرنگار مطرح آرژانتین: بارسلونا با اطرافیان لائوتارو صحبت کرده اما هنوز پیشنهاد رسمی نفرستاده. اینتر شدیدا برای موندن لائوتارو پافشاری میکنه چون در فاصله ۱۰ روز تا پایان نقل‌وانتقالات قرار نیست مهاجمی جذب کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/104290" target="_blank">📅 13:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104289">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDFyKrEZcyMgj5JAKaSfhiJpls5-LvwKPOgpy8c5NQLEphS3cWweGCMCbSDBHi9YNjMk46CheA8JSMftnDTAVJMI0hV20NVbBGW8NJqcRQe9BCl4ePGinEXrPePk5UBWX-Epf9NyoJxi64MoIu-g1Z5U15XrB70AFK7Kz-4jbjp_PvVIY_gMQbrKZs2wpP9aagKFlqEASkU3JR7wNs8VoHUip_QwDn8hnRA-CHDO3iU8FegGGcGxYmLLuYqh6maSgYVVEg32OnOLk6H-rjHwO5uL1MOlx8_PJwN-k5f1X8E42K3tbjjJ6qfASmy4towWZt-loF18P3HyWDd8yKoNnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚑
🇮🇷
#فوووووری
؛ ابوالفضل جلالی بدلیل مصدومیت از ناحیه کشاله‌ران دو دیدار آینده پرسپولیس مقابل تراکتور و ملوان رو از دست داده و وضعیت نامشخصی برای دربی داره. پزشکان حداقل ۱۴ روز استراحت رو برای این بازیکن در نظر گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/104289" target="_blank">📅 12:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104288">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cstWoZQCvcRAH8PqdSMH_qbFav1fZyLLXNXV4TCczrs_4pwoBfc8mjljtgAqsMEmj4x3hQw8InSgekAiAhYKcjNtka4FURX6-F6j-F4M81W8-YZbAzWaKa_MHRZpYiqyUCAxU3PwNNKmty0BVSnL2KNkFJWLsgKnhMWHsWAB82jF_3qlDqiamAxqJqsRLEVQa2B8FctqC-o8d1HUmoMKvBjIbfDzxR6T0W9A-iBYLznGs-JNRRHEbsKI6BUuT0qh0Cv-k6DpWBXViLc4Wbec_qQ1yE8c3L7ImJxPgP1TvmkJhYLgqgxdzzck3HuU8BtPkTW51czs3ZST0Na0MBAZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
❌
👤
#فوووووری
؛ علیرضا بیرانوند در لیست تیم امید برای بازی‌های آسیایی ناگویا قرار نداره و طبق صحبت‌های سال گذشته نظام‌وظیفه، باید از روز اول مهرماه راهی سربازی بشه مگر اینکه اتفاق دیگه‌ای رخ بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/104288" target="_blank">📅 12:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104287">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c4e9318b3.mp4?token=iDM_hKD1_cFYukc5zsgMwe8s3CT2I2N4I_QkuBqH7rnTvquGeFIIQDhlYLrBj2qoGOBlO4XjScXqaQGphSNNQEiHCUW7lp5D2rWvnHlH5QBVbgYOrPm3klso4K5i3yI80qqTMuUmeR9-57XFoqUYQk1ShKj_A9h9L74VW0XUhElniRBnZVX0L_57kUj05GObCR67D-hE_N646ZaLbQnMIpSWpvAE-m00S1MTq98_Tuc-hfnf6A6ZYtYphsBK6z6AqLX44FdDiI9aoTqy49fNIX26yrX7k27S0lhG8V0krfmTRN1jivnEHQu4FxjXEmQgKlKPDQc_T14PJqmW-7cz5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c4e9318b3.mp4?token=iDM_hKD1_cFYukc5zsgMwe8s3CT2I2N4I_QkuBqH7rnTvquGeFIIQDhlYLrBj2qoGOBlO4XjScXqaQGphSNNQEiHCUW7lp5D2rWvnHlH5QBVbgYOrPm3klso4K5i3yI80qqTMuUmeR9-57XFoqUYQk1ShKj_A9h9L74VW0XUhElniRBnZVX0L_57kUj05GObCR67D-hE_N646ZaLbQnMIpSWpvAE-m00S1MTq98_Tuc-hfnf6A6ZYtYphsBK6z6AqLX44FdDiI9aoTqy49fNIX26yrX7k27S0lhG8V0krfmTRN1jivnEHQu4FxjXEmQgKlKPDQc_T14PJqmW-7cz5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
😐
شب گذشته در اقدامی عجیب، حراست سیتی سنتر خلیج فارس اهواز، با ادعای حفظ نظم، آرامش خانواده و جلوگیری از مزاحمت برای دختران، از ورود پسران مجرد به این مجموعه جلوگیری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/104287" target="_blank">📅 12:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104285">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLv5i0IZNvlW49Vyw-_lqF1cYfKtxkQqGfCuCiFKRII6CVXAQXzH59Tn3y8tFMfYOefh6v2-R9n7E8XtBurAQ9Xv5AXgFJhj_M7Vnhvzxqri2m26R5CTQuCCnUWTBE-j0Zkf6D9JI29EQmzh_p7D7Kb-cn9YgWdUhQ5Thy8V7gtJsZrWXdjliU60lwbCKDgpL1SiNRjRtzLQ1Bu2jloD25pJ_l9DgMK8aV0LCBQgxqHm1LigafYTZRqCoavDVTmflWyogtDXrPthgv3txSniYn97S4epWgAkBQehuXqUuyHfeT5kSOP8UvWRhnCC0BN2JaNbizU06ybDOEuzpHyspQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PXvk9rVWyyUY22wTTLXIKOUw0UyIc7XFUgXjcgcCtiKIjwis6QFU4Z5EuhrhoW1ypTlvAsrx8j3Uwm_t_YzZU8p_UbWHxaEx3DPmIasp0GD0AF6DWlYrupUxkdRUifdXBTlNP0RtWFy5lhCBRLIeCvqoo-KAtaak9ncsvJInLPidmmruWQmhBHZXnsAPETXWa1vK3UCo3CQto2sUFQ8LZSH3kgD8jRrf663wPO_ohgfLxskQ9wJ9KMxu2VXPpCY6jKKnBazyLaCdby-cHlGgAJrMhjMzz9nd8qIUJ7VN8QM05pce4DiX6ZuzpLWQC5KypjEW6MNafxYVCk4vyuKpRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
‼️
بنرهای ضد آلوارز در ورودی‌کمپ اتلتیکو:
یه دونه بنرم اون پشت زدن نوشتن: گمشو برو خولیان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/104285" target="_blank">📅 12:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104284">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baadddf33a.mp4?token=LH1gicA_bRt17JvRI2W6QfGvYQSrhZfC1wDKci8IHgplojFH36Q6tSYZIbqvUoBGIZ4_CuN-5qOvfnysp3u9_8vrOW8ubdCoTM5KUByWwPhsD4u4lIVFqMbeJTvhXGHwMgfNg0fafB771yB43Mcq_-2JrOZcGtoH2EWTAb-yAYq0sQqd50Tb5cakaLBq8hxRENeUGve6CkgUDC6hxI8iZ-Dgf5PN7NtfJE4tBBrQ7OqB_O13babsBoiVl5KWLOXf_ymQkJuwPVITqmh9yCpsX-nIG6MM66IkwLXmbC9v2ls4lwF3YBKaRum9OrscwGCXPUp-lJ0y_Mink6kp7FU3Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baadddf33a.mp4?token=LH1gicA_bRt17JvRI2W6QfGvYQSrhZfC1wDKci8IHgplojFH36Q6tSYZIbqvUoBGIZ4_CuN-5qOvfnysp3u9_8vrOW8ubdCoTM5KUByWwPhsD4u4lIVFqMbeJTvhXGHwMgfNg0fafB771yB43Mcq_-2JrOZcGtoH2EWTAb-yAYq0sQqd50Tb5cakaLBq8hxRENeUGve6CkgUDC6hxI8iZ-Dgf5PN7NtfJE4tBBrQ7OqB_O13babsBoiVl5KWLOXf_ymQkJuwPVITqmh9yCpsX-nIG6MM66IkwLXmbC9v2ls4lwF3YBKaRum9OrscwGCXPUp-lJ0y_Mink6kp7FU3Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
مهدی شریفی: بهمنی گفت تیم ها بعد از بازی با استقلال از این تیم شکایت نکنند/ از نظر سازمان لیگ یاسر آسانی برای همراهی استقلال مشکلی ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/104284" target="_blank">📅 11:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104283">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ba668970.mp4?token=Ty-4zitJ6NW24Fo4aCRnQqxD-6BUwZ0kTSXw6SGzrTBxGu5fDPWPB8aP1dW5-dYvTJjkvOzDUpnt-oAAzDnuGPnwqE0URbJSFzcB4rIbYaMvjVtFgqq3VofhLlWgTjyTZEWj3U0dy0HxAwCzNGx-crzj0iblui5TchDXTny7NHCircm-ugPtNXBG5fHi5z29NX2nMUnTZmzzzGm_lq3HghinQkiVckbXbTwdNiBFV0ywwybmi2VtNyP7fshpyJ4zEpKs3wSuxVTulMfrrJPexMEYXmSlBEx2JYdm-Bg1NAvhFn9dTv-xmtTqgmmkd622MIy4MCj4z4CxJ9yKj2ZsUQn3TuZjfwlZXizV5BViNsASVyJqheugZ6TBIKFZ4_VfdhKL-273vx2hE35AtxC8weX9AOfNKYoZ-4dJX_mpoWy6NKDSaRnkfw6tXT3RiChCDmhmxkH5lRiq51F45poHZPVPIJTX5TB2ozqvF_zgnF99PU-GlNhbFEl4IXhgrSHSmlAAeH3g1GvP-2dCkP1p42eDM3jZkTNngyqAK3rxhE-V62iKIGRUcrdvgeB02Aj6hdM_bzVEbkAcn3-1sPFnmg4MYyVf94_yS9FeNnw-_B1vv7iYAnKINzXJQwyGZAX7Jg8_faW2_WvStSl5qsag9oLTlAmJouO7h40C5R3Eox0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ba668970.mp4?token=Ty-4zitJ6NW24Fo4aCRnQqxD-6BUwZ0kTSXw6SGzrTBxGu5fDPWPB8aP1dW5-dYvTJjkvOzDUpnt-oAAzDnuGPnwqE0URbJSFzcB4rIbYaMvjVtFgqq3VofhLlWgTjyTZEWj3U0dy0HxAwCzNGx-crzj0iblui5TchDXTny7NHCircm-ugPtNXBG5fHi5z29NX2nMUnTZmzzzGm_lq3HghinQkiVckbXbTwdNiBFV0ywwybmi2VtNyP7fshpyJ4zEpKs3wSuxVTulMfrrJPexMEYXmSlBEx2JYdm-Bg1NAvhFn9dTv-xmtTqgmmkd622MIy4MCj4z4CxJ9yKj2ZsUQn3TuZjfwlZXizV5BViNsASVyJqheugZ6TBIKFZ4_VfdhKL-273vx2hE35AtxC8weX9AOfNKYoZ-4dJX_mpoWy6NKDSaRnkfw6tXT3RiChCDmhmxkH5lRiq51F45poHZPVPIJTX5TB2ozqvF_zgnF99PU-GlNhbFEl4IXhgrSHSmlAAeH3g1GvP-2dCkP1p42eDM3jZkTNngyqAK3rxhE-V62iKIGRUcrdvgeB02Aj6hdM_bzVEbkAcn3-1sPFnmg4MYyVf94_yS9FeNnw-_B1vv7iYAnKINzXJQwyGZAX7Jg8_faW2_WvStSl5qsag9oLTlAmJouO7h40C5R3Eox0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
حمید بلان عصبی در بازی پریشب فولاد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/104283" target="_blank">📅 11:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104282">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/104282" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104282" target="_blank">📅 11:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104281">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAa1s0diytNmOGvEKoYxiyyJOp_lSNe7S9t9mal_cnRigom5qhO7kWzRx-Du2fkdbQm15_6kpZ4AEyG7HlMPfPeQ6eG5xpQu3f7JJwLbVaX2Uo2eUWWj5ioIU5fOKvDu7KoZqn5Q3JmcFBXpdgAow7T-RGhxHyHqf1LZKrtOT5on0pTefNwMcG5beL5m_9PE3BW9zaxXN0iTS1HpMXoObx2vrFkZAaK0OcPWug5mXZHC7MQfrAfFz7ecnwUcKYuJ8EWj5EmHaQtTbPUuXkYT896b7bhyM08sLsSvW4kAMz-85hmaFY7gjAr88mjGkChgntz8pIbjMgCCugXxN1dwPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r30
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104281" target="_blank">📅 11:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104280">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf8127dc6.mp4?token=nmfb5fiIPehzhvOhAj9jY-LUw_LrP_HNDb2KNFEDBn4oZDxRn5IoM8kn3UBoIb3iA2568j4MblWLV3SaqqXH8ut8RMvFiE4ln9PuhmOVsS0AaHAzwbZFRkDXZ-W71kKFDg3OFUXeq6GKpwTJQEHt2gMHylCTx3XWsclRJcAi7atqTwDDqyyR5TjCU9Mg94i7tJlIYz5Faw9mFaVBKNOImcEeqaN7i4wPRPP0lK9vdP1tF-gOA6gkNstiXspFFr8EP9yLlvTsp4q29h3vIwFSHQp6z-PVDpHIzSGQUIWEuJxNCvfG3C2SGmaSl9hKHYf83K0RbJYSnHRijVDqjNscSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf8127dc6.mp4?token=nmfb5fiIPehzhvOhAj9jY-LUw_LrP_HNDb2KNFEDBn4oZDxRn5IoM8kn3UBoIb3iA2568j4MblWLV3SaqqXH8ut8RMvFiE4ln9PuhmOVsS0AaHAzwbZFRkDXZ-W71kKFDg3OFUXeq6GKpwTJQEHt2gMHylCTx3XWsclRJcAi7atqTwDDqyyR5TjCU9Mg94i7tJlIYz5Faw9mFaVBKNOImcEeqaN7i4wPRPP0lK9vdP1tF-gOA6gkNstiXspFFr8EP9yLlvTsp4q29h3vIwFSHQp6z-PVDpHIzSGQUIWEuJxNCvfG3C2SGmaSl9hKHYf83K0RbJYSnHRijVDqjNscSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🎙
خواهر پژمان‌جمشیدی در واکنش به افشاگری شاکی پرونده برادرش: پژمان جوونی کرده و میکنه. اگر اتفاقی افتاده نوش جونش
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/104280" target="_blank">📅 11:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104279">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fb6e5fa0e.mp4?token=aKk1fmwx-ZySUWSxKcHS4PGSyVeXxq9IMz_iVE09bieYADIjzDc263s6NrTVE5UgsKFDBh_qjzXkjLyTP8U_4j-Im1U9gHuZTxCuM-_xOqMTAVMbi2SvMiUr_QKPsfSb2H7n5D0kEwe3LbdpTeFpyuogdOijLpQCE0tSPI1V-x2_FNV5oYBaenkJA6WK5QBHMN9abHNzhG_grKfZ6yE-gdMwxoS8-ZoZyxn06FVojC2FrTKR7cFrNa_dcLTSTJmCk1NFJqJf78Buw-lsvbbj07zgOySYHGQybtCUeOBuH0_uwkVUrlNEuEe56HhCbMdVCKY347FFYd25YrfpmDV5Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fb6e5fa0e.mp4?token=aKk1fmwx-ZySUWSxKcHS4PGSyVeXxq9IMz_iVE09bieYADIjzDc263s6NrTVE5UgsKFDBh_qjzXkjLyTP8U_4j-Im1U9gHuZTxCuM-_xOqMTAVMbi2SvMiUr_QKPsfSb2H7n5D0kEwe3LbdpTeFpyuogdOijLpQCE0tSPI1V-x2_FNV5oYBaenkJA6WK5QBHMN9abHNzhG_grKfZ6yE-gdMwxoS8-ZoZyxn06FVojC2FrTKR7cFrNa_dcLTSTJmCk1NFJqJf78Buw-lsvbbj07zgOySYHGQybtCUeOBuH0_uwkVUrlNEuEe56HhCbMdVCKY347FFYd25YrfpmDV5Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
یادی‌کنیم از مشاجره تاریخی علی‌دایی و عادل فردوسی‌پور در آنتن زنده برنامه نود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/104279" target="_blank">📅 11:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104278">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeImdkylCRgVc1MdBCnycIXhfow8Fe5DGIJE6rkYy0MVttnLX2OXCf0SgpNXs7K3UMciKtR_s4Cr6kcSFRv09lGQiydh1FSCvu6j3o3nFtTSZn2y7wiUrHEbrn1ZHtjQyjaKhyCv33SB01qhCRTf_BeWrU3IEPIpV7GjBuupVRRM-_m46YpBr6lbE0a0i51IgjzYbL2VX9EhwJY0xMw0qXT5hRTFa2f-7UPUfHEpjpFkEEWlZs6q7AbSfVlZh29GGbqeacbJzIehqdN2uKEzx6aU4I-HACejbPyZNhRZifO3n3laf8tR70KU9KUkV83GbD_YW-8MUKJxbZPMiURB9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
🚨
🚨
توتواسپورت ایتالیا:
❌
فعلا هیچ پیشنهاد رسمی یا مذاکره‌ای بین بارسلونا و اینتر برای لائوتارو وجود نداره!
⚽️
بارسلونا ارزش او را حدود ۸۰ تا ۸۵ میلیون یورو می‌داند، اما اینتر لائوتارو را غیرقابل‌فروش می‌داند و حتی در صورت موافقت خود بازیکن هم حاضر به مذاکره نیست.
❗️
🇮🇹
در حال حاضر، ماندن لائوتارو در اینتر بسیار محتمله و انتقالش به بارسلونا فقط یک احتمال تئوری محسوب میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/104278" target="_blank">📅 10:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104277">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f89a3d29.mp4?token=fnCaWs6my8cKxSQSjWqDRf-GkPlDc2XTTl2VICvtEu125dtOZIcwRQCNnlEH0fHhISVtbOyUlVGYhGb_zibAXXIdljEtaLszM_SUwNLa8MBgNlHfjRjs1gZqYpv7JgqJD2a2CpItDOqZIRqaQwniHJO_ZBkoi8a-6jbKENrIqKIukulQTnLTPjg7VfMlx9HRLD-rNRCfsWG5AZDdDTrfFzSGLQatcBXPFTx2Q9Q-fmPNDesY3yge-0OR2ZYcYnyDQuR8Zpp9G9v_VduRQtzpK_DE_Et0fBhMg1-oJp6KQxnBfWjHIxjvZZaWT8ef4t4Xoz9yrJhTkAn0dxzFP8Am6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f89a3d29.mp4?token=fnCaWs6my8cKxSQSjWqDRf-GkPlDc2XTTl2VICvtEu125dtOZIcwRQCNnlEH0fHhISVtbOyUlVGYhGb_zibAXXIdljEtaLszM_SUwNLa8MBgNlHfjRjs1gZqYpv7JgqJD2a2CpItDOqZIRqaQwniHJO_ZBkoi8a-6jbKENrIqKIukulQTnLTPjg7VfMlx9HRLD-rNRCfsWG5AZDdDTrfFzSGLQatcBXPFTx2Q9Q-fmPNDesY3yge-0OR2ZYcYnyDQuR8Zpp9G9v_VduRQtzpK_DE_Et0fBhMg1-oJp6KQxnBfWjHIxjvZZaWT8ef4t4Xoz9yrJhTkAn0dxzFP8Am6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بغض و ناراحتی کوین دیبروین بعد از تصمیم عدم تمدید قرارداد با منچستر سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/104277" target="_blank">📅 09:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104276">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11ab942df.mp4?token=rU43Yj-PCqEaUpBBHaaJxvMf4l1bHtGnJ0hEt1QtAgNWpgsRidy30YvaXxOoppvhEQBsDnsG3mbFLHzXaYtjvt3dWrUTKCH5sEjIZJn_mEDXd5FL31vKrh66ZJIuY1-yMBhCLih5RmX25ZRwi_2q4E8LLtC5Cutem5BVsOjnACt1P9G4NryNDBtNarId675sxvCd6HMHEmtbazvrb4Wt9dRTYN3EnN4Qz1FtmV8w3MHObMahrEjHeV2G8rqSgSI8Mr81Gr--RySZuOVuMr_Kx0BgUhQxU5OaNP7a6mvUPMgI2dhIPGWv98RxqnRFVmIGLfrz6oWU3q7HULh3niIeig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11ab942df.mp4?token=rU43Yj-PCqEaUpBBHaaJxvMf4l1bHtGnJ0hEt1QtAgNWpgsRidy30YvaXxOoppvhEQBsDnsG3mbFLHzXaYtjvt3dWrUTKCH5sEjIZJn_mEDXd5FL31vKrh66ZJIuY1-yMBhCLih5RmX25ZRwi_2q4E8LLtC5Cutem5BVsOjnACt1P9G4NryNDBtNarId675sxvCd6HMHEmtbazvrb4Wt9dRTYN3EnN4Qz1FtmV8w3MHObMahrEjHeV2G8rqSgSI8Mr81Gr--RySZuOVuMr_Kx0BgUhQxU5OaNP7a6mvUPMgI2dhIPGWv98RxqnRFVmIGLfrz6oWU3q7HULh3niIeig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ربات انسان‌نمای جدید شرکت چینی یونی‌تری روبوتیک که با نام «سوپرمن» معرفی شده، تنها چند روز پس از انتشار تصاویر توانایی‌هایش، با یک برخورد شدید در آزمایش سرعت خبرساز شده است.
یونی‌تری روز ۱۷ اوت اعلام کرد این نمونه آزمایشی که طی کمی بیش از سه ماه توسعه یافته، توانسته به سرعت ۱۲٫۶۶ متر بر ثانیه، معادل حدود ۴۵٫۶ کیلومتر در ساعت برسد؛ رقمی که اندکی بالاتر از برآورد اوج سرعت یوسین بولت در دوی ۱۰۰ متر است. این شرکت همچنین مدعی شده «سوپرمن» قادر است از حالت ایستاده تا ارتفاع دو متر بپرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/104276" target="_blank">📅 09:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104275">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0af9a107.mp4?token=PYJkJS5O1u_nQdONAKzbPMSfZPL33o-4D1M2j37Do_uKmXYdapBs0MncU9JaMWacc8jSWUt8imI5gEF7IZ6KLBw54B5f8oiMVheWqlc4sPhF0H7n38aaqyTwkweIulKjXzCYsCpW5vlXUSBJPTJAeOdpu4hVFBiz1LD1LhBIO8yppMw13hZPE2gxDa3whvRatFRXk2aSajIF_DRnlCKeZcmYIw3lAjMugI7m1gaNSEs1C-U9ouO1roMJ7B82o546Cq1JyYK7GPAL8throNrTRkIOhaG8w7tzfNTIhsAJLJMBDudhhgOagbSRHBPR0Eda9kc2RBoWSUpJUjb519P81Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0af9a107.mp4?token=PYJkJS5O1u_nQdONAKzbPMSfZPL33o-4D1M2j37Do_uKmXYdapBs0MncU9JaMWacc8jSWUt8imI5gEF7IZ6KLBw54B5f8oiMVheWqlc4sPhF0H7n38aaqyTwkweIulKjXzCYsCpW5vlXUSBJPTJAeOdpu4hVFBiz1LD1LhBIO8yppMw13hZPE2gxDa3whvRatFRXk2aSajIF_DRnlCKeZcmYIw3lAjMugI7m1gaNSEs1C-U9ouO1roMJ7B82o546Cq1JyYK7GPAL8throNrTRkIOhaG8w7tzfNTIhsAJLJMBDudhhgOagbSRHBPR0Eda9kc2RBoWSUpJUjb519P81Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای پرسپولیس خطاب به هوادار روشن‌دل: علی‌پروین برو دیگهههههه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/104275" target="_blank">📅 09:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104274">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzFlBqSV24oitn0aLLRaQX22yFxeyIOL2R114A_zF-vf0wAFlyKybkExSZwOmCrYuPnBN4678bXQAtqF96THHSx1KeTyJSITPab3ZSJxDPH4NTCe-Sd2aqe_4EU_BbM3vAr3thF2IQkZvYk_XiKy5KBGSZnIOFtCI3HbF6bqVArzWeEZBSGw1dGwj6xFY4IxiCYmFP5aSBjl2h_RMW9mJqqUtgGO12aHJa4MBrpV24Uah6HpFvPI3lFxdO6WNerJKzxxsdP-5GmMMUUNWpZ_mEWSF-V-jlSEeEKL4wnimuaZA4L3Gp2eFbgaRtqLsF5bhg7HuhgrmtkX4oENA7vPdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#
فوووووری
از رومانو: ساوینیو وینگر سیتی به تاتنهام با رقم ۷۵ میلیون پوند!
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/104274" target="_blank">📅 02:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104273">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2e63463aa.mp4?token=McXiqyziTqn9peC7jCM75RGEs2nSThlYJ9cHc5eo-5LXpwrW5vLqDAmbmBD2fv3Z8qgmFtIg49SD3YolE65DJvmfNSXVCJApVhwszzkz72BG8Tdv1LeRzLY0wYgBC1Uq2Vh4IAxlvEzyEqOpc-8TxUe2ioFPujxjbBCTbblfWAM8nv--eNWWRIDv7KxyQVXQ0KlYqT_GM6elrAlOvhJlfrTsb3g-55ElinbZZWGnvB1iO4wAFxLQjEzKjFuY6W-HWpdBnEdsSMBAmZW_n8fNixXQshcesnJReDwoS46kxIWXD7Vr4_4lTC2oC4sNMEBtNuxjrwAtbMB-F0jgQoSPIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2e63463aa.mp4?token=McXiqyziTqn9peC7jCM75RGEs2nSThlYJ9cHc5eo-5LXpwrW5vLqDAmbmBD2fv3Z8qgmFtIg49SD3YolE65DJvmfNSXVCJApVhwszzkz72BG8Tdv1LeRzLY0wYgBC1Uq2Vh4IAxlvEzyEqOpc-8TxUe2ioFPujxjbBCTbblfWAM8nv--eNWWRIDv7KxyQVXQ0KlYqT_GM6elrAlOvhJlfrTsb3g-55ElinbZZWGnvB1iO4wAFxLQjEzKjFuY6W-HWpdBnEdsSMBAmZW_n8fNixXQshcesnJReDwoS46kxIWXD7Vr4_4lTC2oC4sNMEBtNuxjrwAtbMB-F0jgQoSPIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
😳
حسن‌روشن پیشکسوت استقلال : ساپینتو آدم کصکشی بود
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/104273" target="_blank">📅 01:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104272">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d167412a.mp4?token=G31-TuIG9xHbCuE9awQwtdH4lX2EwWyEETU5mbDknkBxC98KuEsOfHYekSOsoXqaK_7n4FrZcwd2_yLL3LBz0bRIYUkF_f2gVCjiQ5KTJ5NEwGIWZL2xqlrxvRbdWoOtiBOfyO51shOpXPnTw4LazqwKwOgalmtph5fDrXHiF4JYe0T-H3zqzAJMa8uNnlgC_F8nGmWfFIMxbQZ6WbpwEs_l-KOTxQ3IJa-JkqfJK1g-oUgQCQ8rovYhL7KKLMIOsXDWj32Ylp7UlAxzGkp9ZOLxQTuQSRP0ly-SW4PAr5gIwDLX_gHDNbGOxol4ws5PEUBauBuQys-isb9pnZE37A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d167412a.mp4?token=G31-TuIG9xHbCuE9awQwtdH4lX2EwWyEETU5mbDknkBxC98KuEsOfHYekSOsoXqaK_7n4FrZcwd2_yLL3LBz0bRIYUkF_f2gVCjiQ5KTJ5NEwGIWZL2xqlrxvRbdWoOtiBOfyO51shOpXPnTw4LazqwKwOgalmtph5fDrXHiF4JYe0T-H3zqzAJMa8uNnlgC_F8nGmWfFIMxbQZ6WbpwEs_l-KOTxQ3IJa-JkqfJK1g-oUgQCQ8rovYhL7KKLMIOsXDWj32Ylp7UlAxzGkp9ZOLxQTuQSRP0ly-SW4PAr5gIwDLX_gHDNbGOxol4ws5PEUBauBuQys-isb9pnZE37A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
😍
🇪🇸
قشنگ مشخصه یامال دلش بچه میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/104272" target="_blank">📅 01:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104271">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c7cda8f28.mp4?token=suATpfRruCDhRNvTMefX3HcU_YZf04fJiSU7Xha6RqBnuD5N5qdaBSmj3tRlYE6dzHxg8hgMqlfAMArlcy1K9e1GoReBj_hqeX0vpvhuWePz-hy6aDxB5pwJkZK80gmAYBmaa6HKR-EZzMEHdk5ToOG-naAp2YjNisGkg0oc8DWqNZCdME45onfDKS2Yuz4sXk9V47ULiXs0sPyl3hhiPV4l7pl36kSZRKHfErvUrN3jyUicI6yBNShSrBkT_SKqaCZxY_Mf5uJxpxBONEaS1iYSoGQT4pCRZ8R6E1mKnzAnBJhb4EXU7yi4ayvocxkpy1xHeJSNUE9l5lnfKmEqaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c7cda8f28.mp4?token=suATpfRruCDhRNvTMefX3HcU_YZf04fJiSU7Xha6RqBnuD5N5qdaBSmj3tRlYE6dzHxg8hgMqlfAMArlcy1K9e1GoReBj_hqeX0vpvhuWePz-hy6aDxB5pwJkZK80gmAYBmaa6HKR-EZzMEHdk5ToOG-naAp2YjNisGkg0oc8DWqNZCdME45onfDKS2Yuz4sXk9V47ULiXs0sPyl3hhiPV4l7pl36kSZRKHfErvUrN3jyUicI6yBNShSrBkT_SKqaCZxY_Mf5uJxpxBONEaS1iYSoGQT4pCRZ8R6E1mKnzAnBJhb4EXU7yi4ayvocxkpy1xHeJSNUE9l5lnfKmEqaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😳
نحوه سوپر مخ‌زدن شیرازیا وسط بازی فجر
لاشی تو ورزشگاه با گوشی قلب میفرسته واسه جایگاه بانوان از اون ورم یه دختر قلب میفرسته واسش
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/104271" target="_blank">📅 00:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104270">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هایلایت بازی الفیحا 0-3 الهلال با گزارش شایان آقایی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/104270" target="_blank">📅 00:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104269">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fdf2dd188.mp4?token=a3UnHMdg0Jnoo82GqX3Smko2sqlemqvWVDZZ7ruy_RJTvqm_ktsr72buYeAHtD3LDh3tKldLzFOrKzNi92e9Fl41skzBQygLmN2Z45WqnvIn31oib-cxtvJU7AzHQV9lF-bRduwWD8I9mR5fKm98R3zwuhtGo04qZ6SX21OAJHnRVQojBXl1hdaw6VZw0u0NFSw-TXhaCbJlAjbHEyFzJy8Z_tC7CnjWijuHzNms1G664BQIU0Z5MsGjXHQqt4mTmuy7fYvgV3VGrShTbGiLakYHPOZ2nUZn_XEM4vGT_7VlgU55JY1eodL_oHLYUYVEQWzclzulAJRt1ATjeGP-qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fdf2dd188.mp4?token=a3UnHMdg0Jnoo82GqX3Smko2sqlemqvWVDZZ7ruy_RJTvqm_ktsr72buYeAHtD3LDh3tKldLzFOrKzNi92e9Fl41skzBQygLmN2Z45WqnvIn31oib-cxtvJU7AzHQV9lF-bRduwWD8I9mR5fKm98R3zwuhtGo04qZ6SX21OAJHnRVQojBXl1hdaw6VZw0u0NFSw-TXhaCbJlAjbHEyFzJy8Z_tC7CnjWijuHzNms1G664BQIU0Z5MsGjXHQqt4mTmuy7fYvgV3VGrShTbGiLakYHPOZ2nUZn_XEM4vGT_7VlgU55JY1eodL_oHLYUYVEQWzclzulAJRt1ATjeGP-qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف اوایل تیرماه: اگر به سوئیس نمی‌ رفتم، ۱۲ میلیارد دلار ایران آزاد نمی‌شد
❌
همتی، دیشب: یک دلار هم از پول‌های بلوکه‌ شده ایران آزاد نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/104269" target="_blank">📅 00:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104266">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1230d6d53d.mp4?token=LonatazTt-SO2JM_FwKCMCVs_-5YI-c14iPLf6evdccytnijNpmEiyeRsZuh-sR_iftBk_cDOZOf2glHWwYkwL6BHv-4dcrLDiuov5iQgeRwEW_Rss7XVke8ctEXiwV2HJL9R0wWJ7cmspiWoB0T4bAJBOfwNO-d_t4OErSJqYaGSPN6_mv3fUWACmhpTrfo9X8xKWrzq5idzykGklufl_2WsnG1mcOhrvTDaqBka2Yb4GRXF_SDW3nygIp667D8rkNZ_Hgkv20DEeCPxYaSO-5vPUXKiTJ-JvcWLtlP2UUdy3Q5VTNltA-F-47Z5VIP2eyegO5y23ECaLheqJflyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1230d6d53d.mp4?token=LonatazTt-SO2JM_FwKCMCVs_-5YI-c14iPLf6evdccytnijNpmEiyeRsZuh-sR_iftBk_cDOZOf2glHWwYkwL6BHv-4dcrLDiuov5iQgeRwEW_Rss7XVke8ctEXiwV2HJL9R0wWJ7cmspiWoB0T4bAJBOfwNO-d_t4OErSJqYaGSPN6_mv3fUWACmhpTrfo9X8xKWrzq5idzykGklufl_2WsnG1mcOhrvTDaqBka2Yb4GRXF_SDW3nygIp667D8rkNZ_Hgkv20DEeCPxYaSO-5vPUXKiTJ-JvcWLtlP2UUdy3Q5VTNltA-F-47Z5VIP2eyegO5y23ECaLheqJflyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
💙
نقل قول مهم میثاقی از کمیته انضباطی: دوستان اعلام کرده اند چون فسخ قرارداد یاسر آسانی در سازمان لیگ ثبت نشده است بنابر قوانین داخلی هیچ مشکلی برای بازی کردن ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/104266" target="_blank">📅 00:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104265">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoZJq_wHT9c6VdjSLst9mDFItjzOQA0oRsaKqUcCI0wNR3WVzaaRWOoaAjUA7qmLUpoju0ZlVjech5p8M5HflDQUnyz2qkOU6u_TF1jbPrkn9D57cPk0-3G3gW-UXpHP9NbeDdfbxbgSa2i2WieGzYu0yOGT2QpZ6OWCYAmGV_dBm2qXnJbm2LnNVmACACECpxQhe8TYEWK41rG0fIMyzltFdsFoPIU0k3gcijOE_Um5HffQFGqOwGLgvapy3hBWExB8ZvOz1_e5-2OkVRzsrztPcO64KgZ8JeD7xrdw8e7rspLjqYlxgiA-UYVNkplIzETF6oyGhL2nXvVTrT_Obw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مارکا: متئو آلمانی اکنون به لندن رفته تا کارهای انتقال نیکولاس جکسون به اتلتیکو مادرید رو نهایی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/104265" target="_blank">📅 00:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104264">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e2e98ceda.mp4?token=o9F-1_Ia1-UAHyLL91z6Eppz4r9yaQEEhRJ7i8FXnVSQPCmo9ylMVP7VtfZG6jOjEYuJ2re0xQjoUEw0dp1u2m5Vu2A-3yw_T9POKmxmVgyCcntvPU_YyJHqyfhyHpmjF9qsvQXCArFU583DdfDTnRg7Uun-F5HnY9LvL-DjcR3ikCsSbHcle8y1SYNfG48GD4xv-VV0r0yOc6LS7lIWX4n9nFTAseBDW9ob6PQLLVDy0ssDCaTXuibsA0EGWeksM2fGuqJh9UxYxdyDPjuXRl60t9ft_nswmQJUcrFLDQ-52Y1uC6kuKa8OD_kmwrfP_VRxuVDSyNMgrl8tPRYUaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e2e98ceda.mp4?token=o9F-1_Ia1-UAHyLL91z6Eppz4r9yaQEEhRJ7i8FXnVSQPCmo9ylMVP7VtfZG6jOjEYuJ2re0xQjoUEw0dp1u2m5Vu2A-3yw_T9POKmxmVgyCcntvPU_YyJHqyfhyHpmjF9qsvQXCArFU583DdfDTnRg7Uun-F5HnY9LvL-DjcR3ikCsSbHcle8y1SYNfG48GD4xv-VV0r0yOc6LS7lIWX4n9nFTAseBDW9ob6PQLLVDy0ssDCaTXuibsA0EGWeksM2fGuqJh9UxYxdyDPjuXRl60t9ft_nswmQJUcrFLDQ-52Y1uC6kuKa8OD_kmwrfP_VRxuVDSyNMgrl8tPRYUaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
حجت الله بهمنی سخنگوی سازمان لیگ: یاسر آسانی یک قرارداد 2 ساله با باشگاه استقلال دارد و در سازمان لیگ هم ثبت شده است و درحال گذراندن آن است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/104264" target="_blank">📅 00:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104262">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1449e6d243.mp4?token=Fo8KYE3uas5V2LKQNFo1bM3JbrlCxdEOWrWx9LdKFwgV2YLNOXPNzIslacKmoF31CJOCWvV3dQ7qXWVv8RQel2K0G02Q6Oc4ha0ze2Gvb3CXgvVtH24lCVL1eWDSgPkXE_IEVdAJbvr-NYIyQm3L32AduaPYLVX3oRvVLTkFHpw_1rDWLL6TQYT0o-RlamdozqWdcECcNn1UCFer3jZqhS3kqZ39tvsw8igM3xa9QcYO0zkHHk2LNudl64g5OgZcR7I2M0RM7WFeCn0pRE_3uxPx2fEG638ZCC4UQi4ApVua-prBGkkJHh9YXOgCB_33OE1knZ-9kmv8VwxkiiTbeUD-1Spg46wmpDKMBT268ycf5Tvy5PjkA2wZD_SAgrsy_PnZ07va_e850pBEzJE58IOXel_JRA-gky949pF2xOZCQiHpdMToXnn6OQYsj2GI1hG9FfesuPiDcLPmBaHiBcEeFN6mTIntLQOgr7gNV8g87KGIgupEy5KE00UnXkhXMVpJqpkwlWCZLgZIsA4UC3ecvk61fUdjKxqntwUdmFH7flin945KGAdec3WbyCOE71fIVbNZs9hAuP33eKe4V57HqgHAWHoWMY0PTlgvhpZ8JaAOTEZmYGeH2_7RDCu99kvrjQfpWubdGMOYqO65PFyUeRLAeh9V75hiisImnow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1449e6d243.mp4?token=Fo8KYE3uas5V2LKQNFo1bM3JbrlCxdEOWrWx9LdKFwgV2YLNOXPNzIslacKmoF31CJOCWvV3dQ7qXWVv8RQel2K0G02Q6Oc4ha0ze2Gvb3CXgvVtH24lCVL1eWDSgPkXE_IEVdAJbvr-NYIyQm3L32AduaPYLVX3oRvVLTkFHpw_1rDWLL6TQYT0o-RlamdozqWdcECcNn1UCFer3jZqhS3kqZ39tvsw8igM3xa9QcYO0zkHHk2LNudl64g5OgZcR7I2M0RM7WFeCn0pRE_3uxPx2fEG638ZCC4UQi4ApVua-prBGkkJHh9YXOgCB_33OE1knZ-9kmv8VwxkiiTbeUD-1Spg46wmpDKMBT268ycf5Tvy5PjkA2wZD_SAgrsy_PnZ07va_e850pBEzJE58IOXel_JRA-gky949pF2xOZCQiHpdMToXnn6OQYsj2GI1hG9FfesuPiDcLPmBaHiBcEeFN6mTIntLQOgr7gNV8g87KGIgupEy5KE00UnXkhXMVpJqpkwlWCZLgZIsA4UC3ecvk61fUdjKxqntwUdmFH7flin945KGAdec3WbyCOE71fIVbNZs9hAuP33eKe4V57HqgHAWHoWMY0PTlgvhpZ8JaAOTEZmYGeH2_7RDCu99kvrjQfpWubdGMOYqO65PFyUeRLAeh9V75hiisImnow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
بهمنی: استقلال به عنوان میزبان دربی، ۹۰ درصد گنجایش ورزشگاه را در اختیار خواهد داشت
!
استقلال میزبان است و ۹۰ درصد ورزشگاه در دربی در اختیار استقلال خواهد بود/ استقلال ۹۰ درصد گنجایش ورزشگاه را در اختیار خواهد داشت و بازی برگشت، این موضوع برعکس خواهد بود/ تمام تلاشمان را می‌کنیم تا دربی با قانون ۹۰ به ۱۰ برگزار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/104262" target="_blank">📅 00:06 · 30 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
