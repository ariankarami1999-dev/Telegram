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
<img src="https://cdn5.telesco.pe/file/b286uuEr2HykUh3sspM44DvyTD6wkTz7WRqs9UvE78b9WurSwgm2DRO_5fI-NKln9enchnkccnOAmFsZZt4lHg6nb98uWwQgxuXKb0SjOhC5rZLZlVGqNWbifBg7cW-uMLeDF6CIEDIfkOYWmuHit4T8oWfvpkYfTgae3HO4sRoxxclLNdzpGJdy0yCxIMKPyOGlhRashMCR5_gnVkSIb2xC3o9KpJDMOWbg_e0ytexBJhgpltLF2O1WtaRNLuYDK7Pi0TdelIK-PIksolR3HsD2jfiAcV8wnqNKaFE70XP0JulAf2bEbbi40z6ozSOh_8_yBi9hAD6gAJ_AmUCArg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 677K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 18:08:14</div>
<hr>

<div class="tg-post" id="msg-94686">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9f6fcf9f4.mp4?token=Ud5RS7Qy9Dt3d8Zt8qk8fvutdULP9aJZEaKR4vpyzmkckA2GjuaOlJviOG6I_GY2TGIrL1lQdP1X8bh19TN2ZJD2-9vQLmXdNh-wK5gCZC_7jyJKdm1N5cHuEqRCZbvsdaG9ikN4b618SWy280EJIs2j8N74s_lFXMs9ijDL1-PRziF9GNcJwONll-J5e5grGnR9QhO_sf5YVAP3_WF-MucuIu-_Gj6SjEWlnGMifr90U7IoaC62H3nrK_mnznpBW1Qf1iPpNR0s9hwAX6PdPQHew09xoWNfmVEqpYD77oQO7V2sfmiwGmo8h3z7lGgcwsdzc2Q8osMj8BFdZIDUdHrwu4nSa7ncuAz3Qzlv5DAasZsD7dv6BgYEBHdkm4kEMoyb4rufCH6kyIJemKfeSNcneaGt4eb9wlBDVC1lmpoxPzUsTssepBo6Jd7mrSMmh8ULv7G2C7IGptMlxH4oR_CFTLl0lX_5sHaMT1Y9ZnCpyUQV5k1cj3jAtn1HQFCWxYYKLzWikKwBGHLAV-oT4EYIbIbBTjqpywsMoG3I8qGRaU-R6Wyk5B279EdKiCajt5w4cVE2KWKDo8VbZ3Z7pSTlI1nHB-8MsydnBBdmPZA_36u15j3XQ3R_ypWy6b_ZfGxxC6UauiYs0KbPftJ_E5cc9oDJv-S5gMSIw45Al3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9f6fcf9f4.mp4?token=Ud5RS7Qy9Dt3d8Zt8qk8fvutdULP9aJZEaKR4vpyzmkckA2GjuaOlJviOG6I_GY2TGIrL1lQdP1X8bh19TN2ZJD2-9vQLmXdNh-wK5gCZC_7jyJKdm1N5cHuEqRCZbvsdaG9ikN4b618SWy280EJIs2j8N74s_lFXMs9ijDL1-PRziF9GNcJwONll-J5e5grGnR9QhO_sf5YVAP3_WF-MucuIu-_Gj6SjEWlnGMifr90U7IoaC62H3nrK_mnznpBW1Qf1iPpNR0s9hwAX6PdPQHew09xoWNfmVEqpYD77oQO7V2sfmiwGmo8h3z7lGgcwsdzc2Q8osMj8BFdZIDUdHrwu4nSa7ncuAz3Qzlv5DAasZsD7dv6BgYEBHdkm4kEMoyb4rufCH6kyIJemKfeSNcneaGt4eb9wlBDVC1lmpoxPzUsTssepBo6Jd7mrSMmh8ULv7G2C7IGptMlxH4oR_CFTLl0lX_5sHaMT1Y9ZnCpyUQV5k1cj3jAtn1HQFCWxYYKLzWikKwBGHLAV-oT4EYIbIbBTjqpywsMoG3I8qGRaU-R6Wyk5B279EdKiCajt5w4cVE2KWKDo8VbZ3Z7pSTlI1nHB-8MsydnBBdmPZA_36u15j3XQ3R_ypWy6b_ZfGxxC6UauiYs0KbPftJ_E5cc9oDJv-S5gMSIw45Al3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇺🇸
آمریکایی جماعت اینجوری لب‌ساحل کنار زیدش بازی فوتبال کشورشو میبینه
😮‍💨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/Futball180TV/94686" target="_blank">📅 18:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94684">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
پاکستان: مذاکرات فنی ایران و آمریکا فردا در سوئیس برگزار می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/Futball180TV/94684" target="_blank">📅 17:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94683">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c3e66478.mp4?token=iITPCwIDHGTVDZIDojY1gLlj5A__llEGsEp_Sotqiect71lE_3cgCybD646Y8MSR06tGLk4dVEoVTu8bpNGKeUnFBq-sTnHb1U-Jyc7EwKT1LsvTUGJlbXId9U57Q20UDjQ4WX30jhnkxquEmQ6sULcwlV4K7K0vyfTOO_I7DedbTBKnzfiEUsor4G5qTiVZvkN3YLxRPov1dMOALHG3s4WTlgkB0lqV1L6TpDV4GXtSpe7UxX_vqcoKs_5_qn4NQpEa02ws3lcLpUlaXjRY6kxvi-JIobxU4wWHf9xrnsKvR7ilfyCufcHTv2a31tdCVIMzGQ4kWf-JUiqtqpBauw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c3e66478.mp4?token=iITPCwIDHGTVDZIDojY1gLlj5A__llEGsEp_Sotqiect71lE_3cgCybD646Y8MSR06tGLk4dVEoVTu8bpNGKeUnFBq-sTnHb1U-Jyc7EwKT1LsvTUGJlbXId9U57Q20UDjQ4WX30jhnkxquEmQ6sULcwlV4K7K0vyfTOO_I7DedbTBKnzfiEUsor4G5qTiVZvkN3YLxRPov1dMOALHG3s4WTlgkB0lqV1L6TpDV4GXtSpe7UxX_vqcoKs_5_qn4NQpEa02ws3lcLpUlaXjRY6kxvi-JIobxU4wWHf9xrnsKvR7ilfyCufcHTv2a31tdCVIMzGQ4kWf-JUiqtqpBauw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
آلمان عزیز امشب بازی داره
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/Futball180TV/94683" target="_blank">📅 17:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94682">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea2896bfd.mp4?token=hqiOh6qAinYW-wNWvC6QLXUY-i4hiExA0qB54_JmdwZpfUAjk4dbMZ0z3IJSFfRLyZpml6mcxVH3RZeqSrjKZRq8sxa0_Q9svhmVsvVaYYe8AUgmMAben2dl8NzZEIF7f-j5uvNWQFIFwit2WAtzaZI21j9czFtwVoF9PK3B8bump0FSWAeihRkMjRwZIFkPoFbU9EW5IXGnk-WkX08-701K6IraiMNs2CMm3cwJiGGUXmmyQcK43dmxiSAZdPOArgsXfGRFu1N3deDpZPCf0WLXr5gGBqPYnpa-Rnkm1ttPhUBvv3YQsSqh2Fsolpaph621QwnWSNnbN5U2SLgV6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea2896bfd.mp4?token=hqiOh6qAinYW-wNWvC6QLXUY-i4hiExA0qB54_JmdwZpfUAjk4dbMZ0z3IJSFfRLyZpml6mcxVH3RZeqSrjKZRq8sxa0_Q9svhmVsvVaYYe8AUgmMAben2dl8NzZEIF7f-j5uvNWQFIFwit2WAtzaZI21j9czFtwVoF9PK3B8bump0FSWAeihRkMjRwZIFkPoFbU9EW5IXGnk-WkX08-701K6IraiMNs2CMm3cwJiGGUXmmyQcK43dmxiSAZdPOArgsXfGRFu1N3deDpZPCf0WLXr5gGBqPYnpa-Rnkm1ttPhUBvv3YQsSqh2Fsolpaph621QwnWSNnbN5U2SLgV6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابوطالب‌خطاب به رونالدو: داداش مگه ۲ سالته
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/Futball180TV/94682" target="_blank">📅 17:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94681">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40d0e5cc13.mp4?token=SZ6fnjrBlha1JZZeJfjpr31KtJTSCVO7IhR5uHL_c4zlBqfenol-qyla4v5Q5ZrRO3kF-wFKZL1rb65zbD_grKNJ3BvNH-VHkg35Tpd2rGMVuJYXI41iML-IjEQPxPmtWPK8QYIa0OmlD1ScBIg74Bx_7gIIxDd97pjV3-9UGHDro9XvMN_j8QDSMCIhGVsku7DopLOucq7LbqxdYX269fzyStT_150VKANOUO9PzQfp40SSt7OqEMdlidsGPDyLJPjcIIgylwblhsDA89wVP60iWZ0PzkmmSqz61y_9E3h-tSV_qa4ZC9UZhH_RVj8xUd-mLHDHwwplAOI2eLm_YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40d0e5cc13.mp4?token=SZ6fnjrBlha1JZZeJfjpr31KtJTSCVO7IhR5uHL_c4zlBqfenol-qyla4v5Q5ZrRO3kF-wFKZL1rb65zbD_grKNJ3BvNH-VHkg35Tpd2rGMVuJYXI41iML-IjEQPxPmtWPK8QYIa0OmlD1ScBIg74Bx_7gIIxDd97pjV3-9UGHDro9XvMN_j8QDSMCIhGVsku7DopLOucq7LbqxdYX269fzyStT_150VKANOUO9PzQfp40SSt7OqEMdlidsGPDyLJPjcIIgylwblhsDA89wVP60iWZ0PzkmmSqz61y_9E3h-tSV_qa4ZC9UZhH_RVj8xUd-mLHDHwwplAOI2eLm_YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاشیا رو ببین نعمت خدا رو چجوری حیف و میل میکنن
😢
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/Futball180TV/94681" target="_blank">📅 17:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94680">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vX75PdT0AH9mXt_HJRjAXqjTsO18kXcwY1fjfVUP97A96FOj8rLustSGjlQW1sJxPAhJMFlZh3EO5k8WUw9gca9MxRu7lofCMnp0JSo9LCTSGCcdjmJlSxaaUzpXGgisApoxH1u47f_HYjYA2qXQCnzdwe2E873YytJFVD6E0C0hX9-GV6zlHWvdNNJyY0a-FwjCpPJxlkSSCHSkWQUXtibj_imUslixJS-wTDLFF9v0kplfVyh4VYYqO_pdifDRGKYDWNveJC4Ejh1LtB3ioiipTDMBpetcOleFJh37OntB1196rqyQyhWBhKMGpwtEQGbHZdqB4l-EkQIwAUJICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مارکا:
بنجامین ششکو گزینه جایگزین بارسلونا در صورت شکست در پروژه آلوارز در تابستان امسال است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/94680" target="_blank">📅 17:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94679">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a1e82acc.mp4?token=Qxj2AINY-qDP_0QkW8dmeCqMlR429gkRsIcjuExQr18-5NIZNRfbIrVzwpi6Rt5itL0BrMrVNyh7YyUw0Ci1h-V6QSqYURk53i6LY7Bs5a62YA7AOQLhvGhxult3N6-Io_G9M2-d1zbWNfFU86ZqYCWu5-K-4VtON5MWRzhXoEBciBkZlT_-D6zBml0XbMPq1MoexZ8JbTHHT0qpJZuXmI2TavxejDe4Xq5IenCg2q5geI-HASi7FT1K_pZQ0kioEUkZaXwyE0t7WKBOjH7CRVqlfevtn0b0JeaLGCy1TWezf2yxch6Mbzfe98AlB7p13f6mqMx3QBJMhddZpIJ0LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a1e82acc.mp4?token=Qxj2AINY-qDP_0QkW8dmeCqMlR429gkRsIcjuExQr18-5NIZNRfbIrVzwpi6Rt5itL0BrMrVNyh7YyUw0Ci1h-V6QSqYURk53i6LY7Bs5a62YA7AOQLhvGhxult3N6-Io_G9M2-d1zbWNfFU86ZqYCWu5-K-4VtON5MWRzhXoEBciBkZlT_-D6zBml0XbMPq1MoexZ8JbTHHT0qpJZuXmI2TavxejDe4Xq5IenCg2q5geI-HASi7FT1K_pZQ0kioEUkZaXwyE0t7WKBOjH7CRVqlfevtn0b0JeaLGCy1TWezf2yxch6Mbzfe98AlB7p13f6mqMx3QBJMhddZpIJ0LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🏆
واکنش تونی کروس به حواشی خطای مسی مقابل الجزایر:
"این احتمال وجود داره که اگه یه بازیکن دیگه تو همین موقعیت بود، کارت قرمز می‌گرفت... یعنی دقیقاً تو همین شرایط. حالا بذار یه چیزی بگم که شاید خیلی‌ها ازم شاکی بشن هرچند فکر کنم همین الانشم شاکی‌ان! ولی به نظر من مشکلی نداره..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/94679" target="_blank">📅 17:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94678">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ba1b9f67.mp4?token=Mlq-CSFekGgaJ8jBH4xaeiHCOybgw6oMhngu6Ks2Phz39JlDPJnZ2WAFHeWSL8QPT18cIE7qK3qM0x_WHbpx4bqWxOs4zqIufU1ZIZCS5qF2CFGLHLvSflEERUfvd8OPSrE_eaVRO3dd6UhfyyH0wWLC52N_I0EZuz9UO25D4EwzmIMQMCkA07itS_0pSQENLm49EnBGr0_W4SjGHdK9cXng9oNQm6xYpLQdCrGHhCckd4hh1VvFbkLDF0-3akL5m5okrZz85mwTYTPAWfAuTiRj1uLn9BSUU4UgLljyGYAF2kSJPq6qGfi2mdOGe29J7Zj7Q2ieoAUJbFJKBiMzbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ba1b9f67.mp4?token=Mlq-CSFekGgaJ8jBH4xaeiHCOybgw6oMhngu6Ks2Phz39JlDPJnZ2WAFHeWSL8QPT18cIE7qK3qM0x_WHbpx4bqWxOs4zqIufU1ZIZCS5qF2CFGLHLvSflEERUfvd8OPSrE_eaVRO3dd6UhfyyH0wWLC52N_I0EZuz9UO25D4EwzmIMQMCkA07itS_0pSQENLm49EnBGr0_W4SjGHdK9cXng9oNQm6xYpLQdCrGHhCckd4hh1VvFbkLDF0-3akL5m5okrZz85mwTYTPAWfAuTiRj1uLn9BSUU4UgLljyGYAF2kSJPq6qGfi2mdOGe29J7Zj7Q2ieoAUJbFJKBiMzbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
روایت عجیب یک هوادار فوتبال از رفتار زشت مدیران دزد ایران‌خودرو بعد جام‌جهانی روسیه!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/94678" target="_blank">📅 17:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94674">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d6AuiY3Oz2hdDdXlLlazt1JsSLkrLgf_7EQkQgkWUUG9H_GayfkigLEO8MweOi8m4Z3lHZbdSHYXsKGlgOLYD_wWGpAl3Yj268PCLOkdDMI2t9YyQF1Zkdt20e4LVO-l5GQmmshqr8GAdpHiU41rGXJ1ZPApExkoMGCHePGLSahhhL0dR4jbz4jFy1R4sbeyb80XmDf4MUv-LAjk-86JxwFhZTZtus6MnQJMpR4tqboOBPM2suphPWkNfYeQhY61u6rInVDSYXmGVhkNXhDROivjq2vox70_WwCBZhX20oRVW4r6ncm1Ip58Mpzil0NHIwojCiOvD7HbVrqa3kOo_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IveCkmjXkm430fwpMdIL9EEEB_4B3_avhgnKUl_WSj4wfpSDnHxyHDFjcLzRzlOuvdXXqnxRDvfD_NC_4JBQZcjuv3x9sxTcXlc_HbSPAIBnabxl8R0WQZLwpTm1khCv6mAXJwoSGS0oOUJhAzY2jbZ3ue0Fj0EfQDHplJm4tXQ1XibjptvZMtO7u2b4mYNJEn25tRPGbTjoLCIoWeqPr04N29EK1Iic7IjweueygGsMwpcVRFw1bHM8FqGUrwvI4Uyy2GAc6pVb_z3Nd02wxdKX22Pi5uuLWat3dYiH5yGOvnp_rLPdjGkdx3pvlQhC_le-_DopyD88uRLUHqQaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FxIUAM57xcTtQgltI1EA110xiq5R4PsRTDx_y7e2odXDRJMHQlGsUwBssU2ltqhH_L8RR7RgkJoyQhMQeo4nOVwm3sBguV6VBo1MA7BBP7pn8h8_t1ujFMLqLdB82Jl1A7VcHUf9cQPm_OZcdMp3naNKxtVuUzRVG9h2Tlt1Ppaej5lrxnYDAmYyaSmd21FhShdwgsftY7gcwooxGiMCeH-TcQNhtsx-Oq9SLL_JEqxa3Uk4T37JANFuri8qXYLyp5mG2V9Nb40bU0vDjH5uBJ93V_-S1P888VflabmnfV5PvZIyasctFWnL9N-omY1Z4Z-EwaiRRLgMhtUagtKtAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5Cp6jFrdX6Qku6px4Fbb6ItHuj-fMpr6QCpSYSAZnc99PEAK5rlhwuWZr-uB9cHsRDB-P32C6oaX23s5GzuZxrRXKsnFs6kZ6wkSYs6-nr-uiuSgdb1GYyDgyNa2swcb0CSb1uC3BIIUAIzVO-RXeaA1XCsyYX1of9SmHztl--N7iwosdKDjJ4xTkD_yd_9fvYutYW9KPDVsHX0gcUzoBM1uktpixCZPTO_AFReTIdREpD-ICNpUWnpq4C83vsT4Lzw86WgX7Rg5tBcStQENJHBlvfKQMCyqJIy4pt1ANzq0d3QNnGPTkacnT41_kWvz-8pWKtGLDBdAklTt_ZoCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌐
اولین پست‌های لیونل مسی تو اینستاگرام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/94674" target="_blank">📅 16:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94673">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
فوووووری؛ طبق اعلام قرارگاه مرکزی خاتم‌الانبیا با توجه به حملات اسرائیل به لبنان، تنگه هرمز بسته شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/94673" target="_blank">📅 16:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94672">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f2f6a0fd.mp4?token=C9PLBKwJ9gB_YW33bmEhxuxog85CpzOzdS8ok7lCGhZP7PkXF88q_Owmu4MHPIJS0di2-1eLalp7sE5g5cfiLcF1d5ri2nyA5-H-ZOwBH-XONdJHgW6tEUmDqzrp5-MbTxi9SMQWfCi9j74CIMTua-h1jTXE1J3_TKePnHXIrRWQK1Nq9XUuIZlY7wlygpSRv2csO-xNmXHOn4yTW61rCpbx9_DugxxzL41CqyzT0mTKX-6SJVbV3cXSGDBDSKMvB6BADexcED6NylOvI9Th7V4rSTWv8KpNzV74ZMNmgBMnckKYV7FK-S-t6iy2BCpN9wup_0rrQXU255e4xBENCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f2f6a0fd.mp4?token=C9PLBKwJ9gB_YW33bmEhxuxog85CpzOzdS8ok7lCGhZP7PkXF88q_Owmu4MHPIJS0di2-1eLalp7sE5g5cfiLcF1d5ri2nyA5-H-ZOwBH-XONdJHgW6tEUmDqzrp5-MbTxi9SMQWfCi9j74CIMTua-h1jTXE1J3_TKePnHXIrRWQK1Nq9XUuIZlY7wlygpSRv2csO-xNmXHOn4yTW61rCpbx9_DugxxzL41CqyzT0mTKX-6SJVbV3cXSGDBDSKMvB6BADexcED6NylOvI9Th7V4rSTWv8KpNzV74ZMNmgBMnckKYV7FK-S-t6iy2BCpN9wup_0rrQXU255e4xBENCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
🇺🇸
ذوق‌زدگی این‌بانوی آمریکایی وقتی کراششو دیشب وسط بازی دید:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/94672" target="_blank">📅 16:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94671">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEENWu9ZfVG86dpHInLDoKTkqAc-oeQ11qllJYpe0DbZTu5sjoTkycnBPet_lXQIv7lym1vvgeouoVl95w-PEscbt-st2kd0X-vtnck6Zx4L0XP56M2f-0JSNFVmy0m0ZcbX4uEab6zKeulSMsrck7cE_VJbMIbjkxRg2y4MK0IiWXt0K361mb4JrZy2JmC1seifWTz6vxCOChr6ryz1T8cKHnmCdnW3uaLiJ35M6i-Bbf6PumuLMJuJh4BMLnDtkyZJjYrfIW9BC2WMmiWExtp5uHmf5W4hDJdFjJLJVD0LTisHO-cOzSpXnCjUUco9mnk2JKhEAMDu9kkaVSTIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
کول‌پالمر و زیدی تو تعطیلات؛ ایشون پیشاپیش توپ طلا رو برده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/94671" target="_blank">📅 16:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94670">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b719b1cac.mp4?token=mUmC2e0bZmnP6yLisLofflsorvt5beeszOU-eONRQ3LPe9FbRtJJztVcCz0H5WyHk7o-QkkDKus6beAocF4qe0bUaKC2aQYsDmy0LK_iM1pdonUUMZvNpcDSqfJ4uCUNqlGXxAsoZI8wEAYbrCwTpS1kQ_r_W6c-pLuxr1ezkfKqYm3ZTAEU6Z4DTLvEKxOtBWPEqD_CfEC82jpd0u8iOTMdAnKn2gWe__Y--wk0npbGhvmWzIwZFpcRPMEFI4ju2MF0lb8GDwz3InoPABEUFiFGuinnGQPxxZu5hm-60WFolFBfa9rPecjNQHwSfhtSu3L8jBQf6mu6Tv6gc9-PwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b719b1cac.mp4?token=mUmC2e0bZmnP6yLisLofflsorvt5beeszOU-eONRQ3LPe9FbRtJJztVcCz0H5WyHk7o-QkkDKus6beAocF4qe0bUaKC2aQYsDmy0LK_iM1pdonUUMZvNpcDSqfJ4uCUNqlGXxAsoZI8wEAYbrCwTpS1kQ_r_W6c-pLuxr1ezkfKqYm3ZTAEU6Z4DTLvEKxOtBWPEqD_CfEC82jpd0u8iOTMdAnKn2gWe__Y--wk0npbGhvmWzIwZFpcRPMEFI4ju2MF0lb8GDwz3InoPABEUFiFGuinnGQPxxZu5hm-60WFolFBfa9rPecjNQHwSfhtSu3L8jBQf6mu6Tv6gc9-PwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
سوسن پرور تو برنامه قیاسی: ژیمناستیک خوبه چون میخوابی پاهاتو میدی بالا
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/94670" target="_blank">📅 16:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94669">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👀
🇨🇦
🏆
در و دافای ایرانی مقیم کانادا که شدیدا از موفقیت این کشور در جام‌جهانی خوشحالن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/94669" target="_blank">📅 16:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94668">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cd9b0ec79.mp4?token=nCouZR69S-59YTKbSLO00CcSArMxzdy6euw8uvbCJ3ldGSc_cKJo2vdLk6N6mdOb0ToPUJcCd-jWkcgQl2Imr_9SO8F2Q4Q-IToGtujDXJEekRgSOjhlKDqhhbELBMyprfPCQ8vzTmpvLqXuJS5pdLTvLQMyuAntBfZ7ht_hvcnRpeKE36ohniDaoC2BXf5qLdDBdLy5exTeH_e-RbmpROgF62MhyBVtlXyVpe1lQHxnVLdZExmTri7dBfI1vk5CSvC4dXt3CNAM0MFe_HlDjhWIzUL1jEaLwsHL_2UL04Qz3l8iu-8KBVuCpdBFnGoK9FF-53YbG8USywZ-Qw8tRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cd9b0ec79.mp4?token=nCouZR69S-59YTKbSLO00CcSArMxzdy6euw8uvbCJ3ldGSc_cKJo2vdLk6N6mdOb0ToPUJcCd-jWkcgQl2Imr_9SO8F2Q4Q-IToGtujDXJEekRgSOjhlKDqhhbELBMyprfPCQ8vzTmpvLqXuJS5pdLTvLQMyuAntBfZ7ht_hvcnRpeKE36ohniDaoC2BXf5qLdDBdLy5exTeH_e-RbmpROgF62MhyBVtlXyVpe1lQHxnVLdZExmTri7dBfI1vk5CSvC4dXt3CNAM0MFe_HlDjhWIzUL1jEaLwsHL_2UL04Qz3l8iu-8KBVuCpdBFnGoK9FF-53YbG8USywZ-Qw8tRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇩🇪
بازیکنان آلمان قبل بازی امشب مقابل ساحل‌عاج این شکلی تو فرودگاه تفتیش بدنی شدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/94668" target="_blank">📅 16:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94667">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa21338643.mp4?token=vVUongkj9Csp8_NVXHv17MGJua2V80W7KTEIyOCNUK9qCIL_aLWygO6OK2_EYotYazrzEL6iu_60R-J65AQ_P9KyDF-YLXzv9hYqBbf3vE4PNi5NscVn9zlMMiG9qx45JKqVqeEzGamTwhAIpjsieYMJEvF4oyMj21CvzNSK8QV0kmmNTe_zIl-r3MEsYUB7oR2klrVFgLWNI-HFQu1cqEWrNZNujYIoln--zMVp99DED1jXV78-P87Za0jd7b1-8iCsQfW9jWBuq6A494d8eHkGM5GmKxhUihPW1n5klFxeNiN3Fv8h-YT-GMDgFah3Jh8u2DvUmgt2clvCGyvmqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa21338643.mp4?token=vVUongkj9Csp8_NVXHv17MGJua2V80W7KTEIyOCNUK9qCIL_aLWygO6OK2_EYotYazrzEL6iu_60R-J65AQ_P9KyDF-YLXzv9hYqBbf3vE4PNi5NscVn9zlMMiG9qx45JKqVqeEzGamTwhAIpjsieYMJEvF4oyMj21CvzNSK8QV0kmmNTe_zIl-r3MEsYUB7oR2klrVFgLWNI-HFQu1cqEWrNZNujYIoln--zMVp99DED1jXV78-P87Za0jd7b1-8iCsQfW9jWBuq6A494d8eHkGM5GmKxhUihPW1n5klFxeNiN3Fv8h-YT-GMDgFah3Jh8u2DvUmgt2clvCGyvmqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
🏆
وضعیت عراق حریف بعدی فرانسه بعد شکست سنگین قطر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/94667" target="_blank">📅 15:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94666">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIiMFsbcvxBozwhq3fs4fpe9qCyOkLrAy1T0ZsYgVOJRuuPV81kxx1bMu2Lv-_HHzuNTfFcNxdVvWIk4jZsoqhWBzFth2QfPDcT4X6AqdcMQZGNL9Keg7fcGXJVxfGOOerX9owwFnopqr_m-qVsQ0FFes-FRIYaDjaqvyN_jQZHLLIeU38GfJLOh5REMPDuCgO1eYbZ4XRZB1SlF89nSvwTr9i6TtwBaNJ13F0dm0O9ggxEs_x2O4dpk1GpqLRtSlOJJM7XAgM7zWYLAfzyUn9RHY9y_CueSxlNdQc2t8j4UiKL5EbDYaLSUmnoWlrLQUDzVH5hOskGuAPx7lUIJTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
پر هزینه‌ترین میزبانی‌های تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/94666" target="_blank">📅 15:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94665">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3LvZOD9xu46K-b6gPP6UgnXtVgj1dS4hwDZ4E5GtwCIT_xwBrBJNToxTUd9SlysQZpR5p7erXPHAr3o3nTqd4vJ27UAYM05ITv8XMDHwRkuMBlXgcMG3Tt3OgxXdqVJhS7nQsJfmnU9gnckLKrMeE_f9Gl91eYJe8__NS42k_L44uRP_jZjSji6BbiVVaVuP3nOzd5V0-JgRUXJIRL3wrDOZIL0q5nFWL8ziZ0ovm0NMMaABzonS2sDgMpG_k3-jC_B3bpm-I6fIudEr9TNhCbiH1HyD_0-OEwff7H4MHC7I6E_179OdXscYbyjiyH1JBWfTPaPonU88sJ5Ini6cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🟣
رومانو: کاسمیرو به اینترمیامی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/94665" target="_blank">📅 15:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94664">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDYtt6N4-up1cIOoUFe9x_rpFQds2nT4iTVw9ualcP1_TysON5m2D_XMba2WrdENkTdg7xQ1PePHRh285dUj8eoPc85qT9ra-V86dKwgieaiHIV1HjwP54yDJFA9ZGMyWIyBFC06OpueXLw5s8Wpz6mseO2tr-EPdiAbXed4yCbfJYB91cSJdEHS8VfioeyPN5niwgsHd5fcDSYA5UVw23zn52LMx0LrOm_3oDYZ9QYCprfKha6D4JFvJOEHmfw5Qk8JcmgJ9Rm1Myr0MmqhdulAeYWBmfrQX1nIjx4pr2aiufbcHzeKCGZldglnNrpimELpreKzR0utOszhu2q8pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توی فیلادلفیا مجسمه راکی به مجسمه بدشانسی معروفه، هوادارای برزیل هم به این شکل رفتن کیت آرژانتین تنش کردن تا آرژانتین بدشانسی بیاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/94664" target="_blank">📅 14:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94663">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d39566eee1.mp4?token=C1LEjXHtdV163c0ilymW7jrFLXyPI0EpVWUjcjAkF1bnlthi8HVKoY-jqF_WcVD_oktJG4MGbgkGCnwJGZvQwcA0w27Ry9a1wyrCtauCqa35GjAQvz6qSw62orGkHU9kbOG6w2I8kl0tCt2649gAbblCkOAgZ-tVH6FKgocddWJ0hbVo1tGV9rhORcd5Fwhh4FEBiinI-y6iOQSGSv4y1_U-WUPUbyCzf6AMwZLBFKmKRuGBX-4ISNOhh6XPSoxrcrYEfHIBCpCZ4T-OdlbCmf1675YMRbtbgIPVhVxYhmFwlDJZjvVJItWy5iHJ4FEG_OVcQG-rjfhiN4T-K2ij0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d39566eee1.mp4?token=C1LEjXHtdV163c0ilymW7jrFLXyPI0EpVWUjcjAkF1bnlthi8HVKoY-jqF_WcVD_oktJG4MGbgkGCnwJGZvQwcA0w27Ry9a1wyrCtauCqa35GjAQvz6qSw62orGkHU9kbOG6w2I8kl0tCt2649gAbblCkOAgZ-tVH6FKgocddWJ0hbVo1tGV9rhORcd5Fwhh4FEBiinI-y6iOQSGSv4y1_U-WUPUbyCzf6AMwZLBFKmKRuGBX-4ISNOhh6XPSoxrcrYEfHIBCpCZ4T-OdlbCmf1675YMRbtbgIPVhVxYhmFwlDJZjvVJItWy5iHJ4FEG_OVcQG-rjfhiN4T-K2ij0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
فلسفه کولینگ‌بریک جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/94663" target="_blank">📅 14:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94662">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/94662" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/94662" target="_blank">📅 14:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94661">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_5wygKxvHXbBsOnhhpieV4fNqXswX3wXDOZE7w0FEBVtbTaj2FcLnQl-mhNwmNoKn9m36ntoIvCX6d3WHwmaYeFsY-78KuvEvTI4XDkO_RpgON0SjE8s_XOUbRbkpF6K05AItAF4sF83AXPpkXBC9bqylDqI2yIBQDyqHGN16TxMCp_L8kKnU4rQmSWTIjWYzVEtS1WrHDxSZm2EHkcJ0aRZKOulPje_CTeayahTgiHIdrZmDcTtYSi-y8oCEsjmXm49ur2yWQX_5aEqHgNvT5xNEYAEDJZhHApcD2GsBqctk_nMZCx_Qg9rLhBV-TnArTBic6Bs3gbO3ZjzdqL_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/94661" target="_blank">📅 14:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94660">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016b0353a5.mp4?token=EnyC_5kIAR48d39GLXEpjXu57RNQVZcOGPVbpNpDRaV4x9pYSfxnYeuO4ZlyAYX-Z0bzG4zCCTE3DmiCr-dI990Y2Dwppk1QYe5TLVsFEif7JUrGIa5wGvcXY9K2gTm2sHEOEcIRPzP58nAtmeaoPF3h1Da_pk8GhR6GWFCVSeQ3m-p9j2EQN9loiEfNukXmsqVp8d_AAMhqV8YE8Vrlzl84-v6-oPd16e8SbNU-5e3g1afpKZt_DqeyilAKdf9gHvj7KqlYGkUmwDmuOAFuoEFDLjjv90xO9LbKMWL8ICj84k_iwsT1RSBmqwFAvROYN2-5OGyDDCoIsLjXjnplsq3erY7b4XV-YEYPd5DOOhQPfJoAAOiyNJr7XgLKHKQifEVuWeKMkjLje0mSLJj1pfcneJ1Lw59OUeMOH5EpBYOL-xO4Mzqj4UymYcvK7cphXF6J9dIg4TagaH0p7z8h53HG1-SU0xaE8S1SKVfAPzL9gWH5gIAibW6iLYj1QFbJfEzXjJh2YPWJCO7CGLmRD5JKgmXMR90lW62jKZOSuqrmdF_SzSqZh7SWonAgRa3kXeI_FH188580NZh1ROE-BbrUBTRHLzIlXTKhqU6iiwn75fSaE-0DyJQbr56L61slmr-HwNnjZVzN1r41a6RuLR2UmKBC_VMik8dHDNBZ7zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016b0353a5.mp4?token=EnyC_5kIAR48d39GLXEpjXu57RNQVZcOGPVbpNpDRaV4x9pYSfxnYeuO4ZlyAYX-Z0bzG4zCCTE3DmiCr-dI990Y2Dwppk1QYe5TLVsFEif7JUrGIa5wGvcXY9K2gTm2sHEOEcIRPzP58nAtmeaoPF3h1Da_pk8GhR6GWFCVSeQ3m-p9j2EQN9loiEfNukXmsqVp8d_AAMhqV8YE8Vrlzl84-v6-oPd16e8SbNU-5e3g1afpKZt_DqeyilAKdf9gHvj7KqlYGkUmwDmuOAFuoEFDLjjv90xO9LbKMWL8ICj84k_iwsT1RSBmqwFAvROYN2-5OGyDDCoIsLjXjnplsq3erY7b4XV-YEYPd5DOOhQPfJoAAOiyNJr7XgLKHKQifEVuWeKMkjLje0mSLJj1pfcneJ1Lw59OUeMOH5EpBYOL-xO4Mzqj4UymYcvK7cphXF6J9dIg4TagaH0p7z8h53HG1-SU0xaE8S1SKVfAPzL9gWH5gIAibW6iLYj1QFbJfEzXjJh2YPWJCO7CGLmRD5JKgmXMR90lW62jKZOSuqrmdF_SzSqZh7SWonAgRa3kXeI_FH188580NZh1ROE-BbrUBTRHLzIlXTKhqU6iiwn75fSaE-0DyJQbr56L61slmr-HwNnjZVzN1r41a6RuLR2UmKBC_VMik8dHDNBZ7zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
انتقادات شدید مجتبی‌پوربخش از مسؤلان فدراسیون بابت تغییر کمپ تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/94660" target="_blank">📅 14:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94659">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07af1e396e.mp4?token=uhkROgfG1E_in2puNYNLgIzhchhL6hnizaOXsVQkL8u409k-s3GYjOENpdCjhjN-Lex046tSMvMsBuyxSMCCmgLS6ddVGE9VQ45yVag-EFjec_5IsFSgv-cB9dTH8RA1-E9kQmfm9cZ6nhz6Y0fOjsQ__xK1ItNGH0ltlG5Uf3lODOpe5anYc9M9Jdjcn_Bqw9skxKjTX5YLto6L5iQKaZZXda_iQoT7hXR0lnM2DQx7p7XnvFvHIv4WzlWy7aonG5fmaLu4tkCnCjImO657gvmXEfX2NDT2hyqOYmXk43B5TYXtbFmVZc5q2-iRHQACpST7yge74UZrBJ7fGjoMIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07af1e396e.mp4?token=uhkROgfG1E_in2puNYNLgIzhchhL6hnizaOXsVQkL8u409k-s3GYjOENpdCjhjN-Lex046tSMvMsBuyxSMCCmgLS6ddVGE9VQ45yVag-EFjec_5IsFSgv-cB9dTH8RA1-E9kQmfm9cZ6nhz6Y0fOjsQ__xK1ItNGH0ltlG5Uf3lODOpe5anYc9M9Jdjcn_Bqw9skxKjTX5YLto6L5iQKaZZXda_iQoT7hXR0lnM2DQx7p7XnvFvHIv4WzlWy7aonG5fmaLu4tkCnCjImO657gvmXEfX2NDT2hyqOYmXk43B5TYXtbFmVZc5q2-iRHQACpST7yge74UZrBJ7fGjoMIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این روزا در خیابان های مکزیک چه میگذرد
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/94659" target="_blank">📅 14:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94658">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acdd4f1167.mp4?token=knRo3QQU1GuuIlpZekmzHLvMTZRprDURrMOI8SBJcoFhDktXHwA3VXMLp8IzM5dKQmjwZfNW3lgWnoBRLmsEiBXDeR8CcaIuAkKx6Vs2VKxw0Sv1EbYIZdpSWPTgCfJyJDuzK2DvUycLHAOmhqAJQ32RHMB6c216GRDR_-c7q62wZ_k4v-UJLyhO5ZH86YObpb3vmbt0KHc67HffEH_n7foWGx17ov2Ak_lemL4VasQWPvwMqQiw2gShBBzn2EGudpL6sunY8-BKHw1CTT6vbDyGojXYqH6WmpOjyfvWsUD_LAKFOy5DyvnULoEiqRJW2ta0rH6WQEus_dVEOjBPfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acdd4f1167.mp4?token=knRo3QQU1GuuIlpZekmzHLvMTZRprDURrMOI8SBJcoFhDktXHwA3VXMLp8IzM5dKQmjwZfNW3lgWnoBRLmsEiBXDeR8CcaIuAkKx6Vs2VKxw0Sv1EbYIZdpSWPTgCfJyJDuzK2DvUycLHAOmhqAJQ32RHMB6c216GRDR_-c7q62wZ_k4v-UJLyhO5ZH86YObpb3vmbt0KHc67HffEH_n7foWGx17ov2Ak_lemL4VasQWPvwMqQiw2gShBBzn2EGudpL6sunY8-BKHw1CTT6vbDyGojXYqH6WmpOjyfvWsUD_LAKFOy5DyvnULoEiqRJW2ta0rH6WQEus_dVEOjBPfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🎙
🇧🇷
وقتی عادل فردوسی‌پور، حتی بعد از گذشت ۳ دهه از شرکت در مسابقه هفته، یکی از اولین قاب‌هایش در تلویزیون همچنان به برزیلی‌ها و اسامی کاملشان علاقه دارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/94658" target="_blank">📅 14:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94657">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPxCRsudOXG1VcFyDdfZ3NOEaV6Gmy58Kv9YgQd8JXAwN_8J61L4mYCaY3S9qYFdN8Vnqvzih9KkHweOgSPGTSCnXDPtNgIJ0Ss7g2Ey5O6oGNjzLZr7CKVT3OiGWQa3oxaHIfKhJCa3e6t5fEAoxk_3XfuiO0yz95m9fEBFNhFNKD1YpBinMvgvQIRLxRDkAnsnu-NNcPamMXfRxFiL8yF15aSpOp4LXqAU8VDOZbAfuauNJlgOx1QJ0ofU-4ElfBU1FiHwyg64hmZlntEgrJS19Zb6VxDFipPgifMznQa9MgRWjwgp4mVWqZQ11SLG7FBVbXYz8LzfP4dwopz-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🚨
فابریزیو رومانو:
آلوارو کارراس این تابستان در رئال مادرید خواهد ماند. مورینیو با حفظ او به‌عنوان جانشین و ذخیره کوکوریا موافق است، به‌خصوص که احتمال جدایی فران گارسیا از باشگاه وجود دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/94657" target="_blank">📅 14:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94656">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">😐
❌
فدراسیون پنج ستاره ایران تصمیم گرفت که سهمیه بازیکنان خارجی لیگ‌برتر رو در سال آتی به ۴ بازیکن کاهش بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/94656" target="_blank">📅 14:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94655">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI3IICUraYlgjcGVn41WSuzX7LZecoRngpp7aor2ND5M1DIhsurbLq95XyyLpSRZQXpzPTlJHCplU7nMkjxCeh-hUW6ekAOrPzgjqJug7OYZzDrkKnjct0O94aUBGKgEee8KgzJlz94RpDt5rzupBgcZ5LLEs5Tu-ByC975Duij8TAaUk2ANvA6xLHRlzmLDXc_acCcKw3V2_pe2IUINB_0lzO2-Gd2ByR0f_5go8QmPg8TLM68XEjvsOLkEJBtXX9mZaQGqYwNDR4kwl_NAzPvTwIsU9ArjlSqe9iy-njEKK9OcI_cyGEt-q7vWeDwM9IYeuSnzzIt26np2UioBwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فووووری
؛ رئال‌مادرید بدنبال جذب هینکاپیه برای تقویت خط دفاع خود است. آرسنال این بازیکن را فروشی نمیدونه اما در صورت رسیدن پیشنهاد نجومی ممکنه نظرش عوض بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94655" target="_blank">📅 14:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94654">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6b2f32a1b.mp4?token=m-lbb0STkjlPFFWHLzSUDT1TGW6Z2jV08U6dtfMCxwO9KXkzLIEx4Nj6h0q3Slphv5S0wdTZTDDyg1fBLqHpwEfwbXbrFOFTlxKqoV8QAFGMEb6Z8R3MdWwDW5fr5TitFHtC7Uwn5Il3U1gmMseN33hzLnyljdiw7fI-Wncw_R2WDzVWG9f_V1Y2yuhTL0QFWmLhkg_xFk_-r_7QkpYFNHEV_JIVvKrYcBKsTKX_vkycDhr8LDJtA_9n6uhztFYYicOeE8lwJH3NQrNvPGynHs-rmAbGUhMRfABP5Yw23pwV2lwLzyN3nYl7XFoJ5RBBrhQlm_7qX2AYexRivEZwAE4qwi8CimLK6RG3FBJIwLsWPSSeaj-xBs9ei38atYP0E_ZRiM3OKyLiH28M2JnaYM_JGXJtyg8l0w8HX8YVtS_FlpDy3XwUCwqn__7B5NiPA7EaLlz2lzPYIr25I9PmtklaqPJtxDgmdYNLK43iVhPwVzqmCNDYvmlGSa3anJ7MtLMvfTESUczt1e6X1--e2tZJHrcfKy1iR9Dq57HbAU-fIksNZ7-wnSQEKSCUoKdB1rlitT_5bGkjcx5GI48ujKRz0o_ItspO28GaxRVkzET8Nxy9VjZm99q3v6toUg9cThVy8k3Qngwlnjs8DKkZbzCa6iNS1Op2JZsrybg3SSY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6b2f32a1b.mp4?token=m-lbb0STkjlPFFWHLzSUDT1TGW6Z2jV08U6dtfMCxwO9KXkzLIEx4Nj6h0q3Slphv5S0wdTZTDDyg1fBLqHpwEfwbXbrFOFTlxKqoV8QAFGMEb6Z8R3MdWwDW5fr5TitFHtC7Uwn5Il3U1gmMseN33hzLnyljdiw7fI-Wncw_R2WDzVWG9f_V1Y2yuhTL0QFWmLhkg_xFk_-r_7QkpYFNHEV_JIVvKrYcBKsTKX_vkycDhr8LDJtA_9n6uhztFYYicOeE8lwJH3NQrNvPGynHs-rmAbGUhMRfABP5Yw23pwV2lwLzyN3nYl7XFoJ5RBBrhQlm_7qX2AYexRivEZwAE4qwi8CimLK6RG3FBJIwLsWPSSeaj-xBs9ei38atYP0E_ZRiM3OKyLiH28M2JnaYM_JGXJtyg8l0w8HX8YVtS_FlpDy3XwUCwqn__7B5NiPA7EaLlz2lzPYIr25I9PmtklaqPJtxDgmdYNLK43iVhPwVzqmCNDYvmlGSa3anJ7MtLMvfTESUczt1e6X1--e2tZJHrcfKy1iR9Dq57HbAU-fIksNZ7-wnSQEKSCUoKdB1rlitT_5bGkjcx5GI48ujKRz0o_ItspO28GaxRVkzET8Nxy9VjZm99q3v6toUg9cThVy8k3Qngwlnjs8DKkZbzCa6iNS1Op2JZsrybg3SSY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو عجیب منتشر شده از مراسم محرم در یکی از محله‌های تهران
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94654" target="_blank">📅 14:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94653">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38da867d39.mp4?token=sVHMAcVVeWIujqOCxQp7Nq6HjBfc6miCR8tOHzrsVwj6UN5sTXmNpBDprfvjrDujsL3GVBHMf9p6d_d9LP3VlyNSfOdupMsoPm4SYa-XDxjhvhxIiefEVZIDUBC2p9MU4PNyYBYhfOVJJ01gRfTucJOeeL26ZuxIpCZth9jEi8bG_fvA96DaBl3M1I9zzpDcNiqEOITx_EAIR4kRdcJtzkYsUwdo8ft3nHWjhmK-_I9rT9u6gO3E_skSoAjvI9DccKIILsahppdu_pAymaJeSKdwtJyB7OHtwC7tln0aEJalw4ng9ikC14jp3tPhQDNdpW8hJM6W5ffXC-Mrfqe-uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38da867d39.mp4?token=sVHMAcVVeWIujqOCxQp7Nq6HjBfc6miCR8tOHzrsVwj6UN5sTXmNpBDprfvjrDujsL3GVBHMf9p6d_d9LP3VlyNSfOdupMsoPm4SYa-XDxjhvhxIiefEVZIDUBC2p9MU4PNyYBYhfOVJJ01gRfTucJOeeL26ZuxIpCZth9jEi8bG_fvA96DaBl3M1I9zzpDcNiqEOITx_EAIR4kRdcJtzkYsUwdo8ft3nHWjhmK-_I9rT9u6gO3E_skSoAjvI9DccKIILsahppdu_pAymaJeSKdwtJyB7OHtwC7tln0aEJalw4ng9ikC14jp3tPhQDNdpW8hJM6W5ffXC-Mrfqe-uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇹🇷
حیف شد ترکیه از جام حذف شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/94653" target="_blank">📅 13:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94652">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9405536d1.mp4?token=H7TwrRqpwvx5Izwef8gv0CzIw_PQfECMVx2GsWQGXXdAYM8pSthozkSwo4qHF1w3g5u3ymtOcYyRp0dleFM8xeCXda2NyjILOXd0ojt8OWNYYs6ovRoqW9HRUGVfMY_Uucmot7qpGPrnJMhgEhNy7QX1ioieThncDUHsZo8ddD0pHkD8Hgf78BiL4Ed24WfTUXxY9J6UeSsh_r6VbGopdUAzeExiVDHx5KOqjG0B9xfVyU-NbiYOREhFHCl85R-A9kzWPafoVJ5j81gLio3Hdbhy-LUehXwM7wTVZ49J9M5N7GMF_5tMF6Edjj4jkQekjcqreuBu7hGWPvSHf0BAwQp24_KDzBkRJfgt01H1okUIgbkcXvMKngV8bnbOo9nFuTbtNprVCTpbe0ncnNu0KH3ensMo_3TGN6ZKlo4s4Ouc5edbbBu1_Yjc-1u2SWB0bvtkh292SpZPJSaNz2xqCgiKTyImCe2iRIVUPB8aMX4_s77dSzARuTtna0o4UIOrzXRquI6120P5yqhXxximESilXiemzRLI0wURalzj62H7gXlincbts7zg088zN3ZqiZOuGTx0a-HUZA_27lPgM7ygQqvE0klRkvxq8EpV3vWFh1m2Htu6NVL089aQgSL6wJglHYmV0qB8v6uJeK8NBBeXw2c9rD_6G9TLjafTXCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9405536d1.mp4?token=H7TwrRqpwvx5Izwef8gv0CzIw_PQfECMVx2GsWQGXXdAYM8pSthozkSwo4qHF1w3g5u3ymtOcYyRp0dleFM8xeCXda2NyjILOXd0ojt8OWNYYs6ovRoqW9HRUGVfMY_Uucmot7qpGPrnJMhgEhNy7QX1ioieThncDUHsZo8ddD0pHkD8Hgf78BiL4Ed24WfTUXxY9J6UeSsh_r6VbGopdUAzeExiVDHx5KOqjG0B9xfVyU-NbiYOREhFHCl85R-A9kzWPafoVJ5j81gLio3Hdbhy-LUehXwM7wTVZ49J9M5N7GMF_5tMF6Edjj4jkQekjcqreuBu7hGWPvSHf0BAwQp24_KDzBkRJfgt01H1okUIgbkcXvMKngV8bnbOo9nFuTbtNprVCTpbe0ncnNu0KH3ensMo_3TGN6ZKlo4s4Ouc5edbbBu1_Yjc-1u2SWB0bvtkh292SpZPJSaNz2xqCgiKTyImCe2iRIVUPB8aMX4_s77dSzARuTtna0o4UIOrzXRquI6120P5yqhXxximESilXiemzRLI0wURalzj62H7gXlincbts7zg088zN3ZqiZOuGTx0a-HUZA_27lPgM7ygQqvE0klRkvxq8EpV3vWFh1m2Htu6NVL089aQgSL6wJglHYmV0qB8v6uJeK8NBBeXw2c9rD_6G9TLjafTXCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇲🇽
🇰🇷
درسته مکزیکی‌ها داخل زمین به کره حال نداد اما خانوماشون بیرون زمین حسابی جبران کردن
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/94652" target="_blank">📅 13:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94651">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ff9b3624.mp4?token=NtP0ErcjoqXFEFC14nrQg9w0pQ8DiMI39cae89yynlnnmW3L4UqjNAI2a6BC_FRn-1hFAaPbVhrJeP7F9pdmUtRSUQpMiz0g_4Fx17oUKT9BzMVDDnkK07Y9p67SvVDBiCBHvBEf8_CyZAvaDDx3WpSJrrW5fvP2TkeTnY3k3xpjC05g-OXgjz8AcLp59Py2-Q5cDvGVzW5jzSb4tCvc1tcUJrKsSlQkSrchpIW2kg4LZ8fRkXrFVttaTYrxreGmzsKmlooAOncjWPBHtIU7NuDcrQpxEEArMS4fSiJDQuwOJattVsqUHP6oVYAuOQ3dDDWrnHm6hq88eoL8dsrTLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ff9b3624.mp4?token=NtP0ErcjoqXFEFC14nrQg9w0pQ8DiMI39cae89yynlnnmW3L4UqjNAI2a6BC_FRn-1hFAaPbVhrJeP7F9pdmUtRSUQpMiz0g_4Fx17oUKT9BzMVDDnkK07Y9p67SvVDBiCBHvBEf8_CyZAvaDDx3WpSJrrW5fvP2TkeTnY3k3xpjC05g-OXgjz8AcLp59Py2-Q5cDvGVzW5jzSb4tCvc1tcUJrKsSlQkSrchpIW2kg4LZ8fRkXrFVttaTYrxreGmzsKmlooAOncjWPBHtIU7NuDcrQpxEEArMS4fSiJDQuwOJattVsqUHP6oVYAuOQ3dDDWrnHm6hq88eoL8dsrTLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خوشگل ترین بازیکن جام جهانی از نظر خانما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/94651" target="_blank">📅 13:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94650">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7248f9196c.mp4?token=ggkxDB3-YyJGUTopuxhGv-UGM6gcYLjk_OStqTUn_p7ZfWsRigLJkfVNtFJ49PfXRjwQ3nTE5PEKZJHvlgU4h4gcQgfc2xrwdDDFTpFPDYMxF7PTIuT7b8dYvzkI6SGdcX2sLzetIPVUyS_u4YQSEPxK7iqNHo-Rsnk6-YkcuMkv8Kt-oDKiYzkAY7VcPD_1_rXBLDo8NRY6Mx0kvzgwqa4tNfb4KV-9pxr8oA8ZU33fp-M2TAY5ubhKvSBPtFMatnnVUYncylRlS5JnFvLEQrr2JfffQ6_lbA3GE-NmOD_CSznKu8WnT53XYafeEqZnQCCZshccQWtskigmsT6Vag3aBuKoEgxaVuOCqGDbYMBMsjvvolluFsfCDViPBO5cxulblDan_2iTzbrS4GCQkM2yBchURyOtJDQ7qdpbR66h3jm9h52xMIakszFb6w7uNK-8FSYCUdlx7gz3IHqdDfh1lQju1D5VDEGV3pt3gdBm0TlWROVCaE3AkR75pidido2YZLTWlXSsMX6NxEHHBuyqsJ2wuL9McGM4S7G8mMH3kwIbDvie2T2GoKB60FEOJKGM2DZsQu-V5ngSp6rytKoYqDUo8sXKMYBcBsZ-eEp47u3NVfbG2HCzA97hBDOcjhqgziGdieS5i4Vu_vTmYtyBhlL0y7Cv2SKk3hv2vEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7248f9196c.mp4?token=ggkxDB3-YyJGUTopuxhGv-UGM6gcYLjk_OStqTUn_p7ZfWsRigLJkfVNtFJ49PfXRjwQ3nTE5PEKZJHvlgU4h4gcQgfc2xrwdDDFTpFPDYMxF7PTIuT7b8dYvzkI6SGdcX2sLzetIPVUyS_u4YQSEPxK7iqNHo-Rsnk6-YkcuMkv8Kt-oDKiYzkAY7VcPD_1_rXBLDo8NRY6Mx0kvzgwqa4tNfb4KV-9pxr8oA8ZU33fp-M2TAY5ubhKvSBPtFMatnnVUYncylRlS5JnFvLEQrr2JfffQ6_lbA3GE-NmOD_CSznKu8WnT53XYafeEqZnQCCZshccQWtskigmsT6Vag3aBuKoEgxaVuOCqGDbYMBMsjvvolluFsfCDViPBO5cxulblDan_2iTzbrS4GCQkM2yBchURyOtJDQ7qdpbR66h3jm9h52xMIakszFb6w7uNK-8FSYCUdlx7gz3IHqdDfh1lQju1D5VDEGV3pt3gdBm0TlWROVCaE3AkR75pidido2YZLTWlXSsMX6NxEHHBuyqsJ2wuL9McGM4S7G8mMH3kwIbDvie2T2GoKB60FEOJKGM2DZsQu-V5ngSp6rytKoYqDUo8sXKMYBcBsZ-eEp47u3NVfbG2HCzA97hBDOcjhqgziGdieS5i4Vu_vTmYtyBhlL0y7Cv2SKk3hv2vEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🏆
صحبت‌های جالب یک خانواده اندیمشکی که هفت نفری با یه پرشیا در سال ۲۰۱۸ رفتن روسیه تا جام‌جهانی رو ببینن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/94650" target="_blank">📅 13:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94649">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d04b34885f.mp4?token=IT52MNzwmmps4ptrKfBBBOxibr3piLmLLPernhlOgn87BJWNsFA5f4hmyB1-vlvLXguh1742UsX9hfd_i6S7_iuzJ9hN9cHl66fX8kxw0sCzai6BSQaqacZKkld4hh-fNI-x_K89C98DdAXSpxNkGXlEwfjpc05KOyoMPCLfsr79SjERrmrNbPKoCTUcqWjxQoN0Y8JqB2ZmxdZj7Y2GxEgXVzSOlrQCrC12qH4FHRsHcviQRXO7ZRFX8iVzcyL8fdoLP8trRANStyEl3LnSAGT0Yve4H3x1N9FtOfBQH71v0n-j9bzeOB3yEftF46iZh9VUffaYOtF-XQDZOLJDHkmYqE8sirV_4WXqpVtPZ3IOa2fheLu8g4CtlrWuAs2gATmqyrdWqdhFIIpVIqaEs_KrbBKnqguvjg4vlvDVzuhfuZcXCcCfBdz8N5idT61l86kxZtYB_X3hbdF7SL3fbyUhm1OjwwKtsfB_OvjosAWCMUH-Jue8YbNn4Y5DD7Dzw9QgCFC-XuO6J-pwKWTEim5xhgzpI7kMXox6xX4HUlAAgSosJE-W0Pq_Pi6BatILhdZ1FtgqN15RwdRO_8F3GPM-RRXoQqlHOqhrVRairrt4VYfcozJTblW5pLc-JnrJi7R2V1AtosuW68YrGPGszT8s50Ywca5rmyYX3SWsulo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d04b34885f.mp4?token=IT52MNzwmmps4ptrKfBBBOxibr3piLmLLPernhlOgn87BJWNsFA5f4hmyB1-vlvLXguh1742UsX9hfd_i6S7_iuzJ9hN9cHl66fX8kxw0sCzai6BSQaqacZKkld4hh-fNI-x_K89C98DdAXSpxNkGXlEwfjpc05KOyoMPCLfsr79SjERrmrNbPKoCTUcqWjxQoN0Y8JqB2ZmxdZj7Y2GxEgXVzSOlrQCrC12qH4FHRsHcviQRXO7ZRFX8iVzcyL8fdoLP8trRANStyEl3LnSAGT0Yve4H3x1N9FtOfBQH71v0n-j9bzeOB3yEftF46iZh9VUffaYOtF-XQDZOLJDHkmYqE8sirV_4WXqpVtPZ3IOa2fheLu8g4CtlrWuAs2gATmqyrdWqdhFIIpVIqaEs_KrbBKnqguvjg4vlvDVzuhfuZcXCcCfBdz8N5idT61l86kxZtYB_X3hbdF7SL3fbyUhm1OjwwKtsfB_OvjosAWCMUH-Jue8YbNn4Y5DD7Dzw9QgCFC-XuO6J-pwKWTEim5xhgzpI7kMXox6xX4HUlAAgSosJE-W0Pq_Pi6BatILhdZ1FtgqN15RwdRO_8F3GPM-RRXoQqlHOqhrVRairrt4VYfcozJTblW5pLc-JnrJi7R2V1AtosuW68YrGPGszT8s50Ywca5rmyYX3SWsulo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل خودت رو بزن!!!
🔹
با افتتاح حساب غیرحضوری در باران بانک کشاورزی، از برندگان
۹۳میلیون
تومن
اعتبار خرید باش!
🔹
۹۳
سال قدمت
۹۳
برنده در هر روز.
🔹
برای شرکت در ‌قرعه‌کشی
اینجا
رو کلیک کن.
شرکت در ‌قرعه‌کشی
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/94649" target="_blank">📅 13:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94648">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9be9e31008.mp4?token=BXAQmnFUul7MS21Jb-atUuanBbB5OkMX7D4kAk2ekKWRfBkTqRVxT4ahEmjE8JR91vysaTLERnXIfCIgG-A4XcWq5dK2fDlZwanfMzhW9nd1FDx11XbZy5ctxeH02nQQqhoV5MjSDzjPP1LU-djRFREB_s2IvMqb4bFwW_LHSfsjN5LN-IILW1yloISasQLERlUifa6ikbc6FxbFaolXm-Igqei8L5SxBV7HGC1GwuGoWvabmKkEeTBOAqmW1bDQuXkt6JrANMKvgX8j2woYIT0JZG3ZG9kUav33chY300F8ot-qGw03IucqcSy1gUTg1g2Qj6wUhM02Iv6Eug8Rmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9be9e31008.mp4?token=BXAQmnFUul7MS21Jb-atUuanBbB5OkMX7D4kAk2ekKWRfBkTqRVxT4ahEmjE8JR91vysaTLERnXIfCIgG-A4XcWq5dK2fDlZwanfMzhW9nd1FDx11XbZy5ctxeH02nQQqhoV5MjSDzjPP1LU-djRFREB_s2IvMqb4bFwW_LHSfsjN5LN-IILW1yloISasQLERlUifa6ikbc6FxbFaolXm-Igqei8L5SxBV7HGC1GwuGoWvabmKkEeTBOAqmW1bDQuXkt6JrANMKvgX8j2woYIT0JZG3ZG9kUav33chY300F8ot-qGw03IucqcSy1gUTg1g2Qj6wUhM02Iv6Eug8Rmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇭🇹
چالش هوادار آمریکایی برای منتخب‌ایران
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/94648" target="_blank">📅 13:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94647">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68cb5604e4.mp4?token=KAy9cvh3oEdxi_LQMDZlHU8O7zDDp0vNdNnyaIEDJNqKeFuGyc6OFzCANB5AiTQAB0971kQaUXFUry2jXOPfAA9PdSwlnlYftbgKrPhGTjx1EtCguYcSrcSdyvGxLUsblwh4u_cLk1cgR9KDxToiDepzHdcCDHOxUn0-qRuJiwKbx0UnLow_vGDTxIBafNpUXc_Q5RubuM2mpLu9Blc-1dTSKT2C01Sym86m0cuNGn4TvebilIDpgPmilZvTZEBBbpn6EtkSEUQvRBVpQ4yHP1ypCpTU-lEVRb-df2yz8Gk2Qm0G4hd8_IVGvMy2-b0wG5z0jqZp2xDNN7r44VgEsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68cb5604e4.mp4?token=KAy9cvh3oEdxi_LQMDZlHU8O7zDDp0vNdNnyaIEDJNqKeFuGyc6OFzCANB5AiTQAB0971kQaUXFUry2jXOPfAA9PdSwlnlYftbgKrPhGTjx1EtCguYcSrcSdyvGxLUsblwh4u_cLk1cgR9KDxToiDepzHdcCDHOxUn0-qRuJiwKbx0UnLow_vGDTxIBafNpUXc_Q5RubuM2mpLu9Blc-1dTSKT2C01Sym86m0cuNGn4TvebilIDpgPmilZvTZEBBbpn6EtkSEUQvRBVpQ4yHP1ypCpTU-lEVRb-df2yz8Gk2Qm0G4hd8_IVGvMy2-b0wG5z0jqZp2xDNN7r44VgEsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇩🇿
🇦🇷
رسانه‌های الجزایر این‌شکلی به اخراج نشدن مسی در بازی با آرژانتین کنایه زدن :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/94647" target="_blank">📅 12:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94646">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5wbUCy_R9iB4b9WhUPdZQXlOnrUw-CtMGeQxvYUmbMugBPadkEwTBnB9Za-uxaufQwlI_bfScpZTtCEo7IiRKimthRGHrsVp8jjZu5F-b2keOrrXbfB2Wdk6f2mNxQL2btGtZzMTc7yGKOpCoW8Wz5Op0DXZ1da_LlVsudXZlSTmsmhSBN-Wx0Kc0bltMpy4FKNQuythwQnvKKTNYJhmTiGZ-wKdnusS_NcVCYzkFMARiKIR868rYtO2Tq_K_wC7CgijmJanTgJumQZLzGTbiVKwJ9IRa0CbceuWbeQOmbO296xhdpED937nyOC-EIr_os7KU2zOK2gg550uhdfXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
آردا گولر:
در دوران بازی‌ام با تیم ملی، هر کاری که بتوانم انجام میدهم تا این جام جهانی را فراموش کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/94646" target="_blank">📅 12:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94645">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c72290d26.mp4?token=VtWz7oF_RYkCrBC-gytKnq1WPFXBn1u8b-TSfm_LTcDknpXZpQKb7noE5C5kzXv1MhTw_eBt3wfy7X5mJ9AQS1joXkjRFOfGJOA5u6qAsYOXI_kk15neaZQtA2JioOFvVEsepAgI4mGfJQPoLvrkusYSiVoLvmrPLMvOEBZXmQ72fH8Uo3pULcWbDida8Q7MgNU2OhKFDOlLS9F9wLAXmGb7lOn_d41PF5sfMv8OURpXyVEomA8WuLVIzyTz_6evlHPq5Grl8k6aT9ZI2A-TosYYZq-7QhvTVPhXqWM50M6kcaioiOimVW8ce4JZ11S4MDLjxdK8C0pnGMnwczyb1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c72290d26.mp4?token=VtWz7oF_RYkCrBC-gytKnq1WPFXBn1u8b-TSfm_LTcDknpXZpQKb7noE5C5kzXv1MhTw_eBt3wfy7X5mJ9AQS1joXkjRFOfGJOA5u6qAsYOXI_kk15neaZQtA2JioOFvVEsepAgI4mGfJQPoLvrkusYSiVoLvmrPLMvOEBZXmQ72fH8Uo3pULcWbDida8Q7MgNU2OhKFDOlLS9F9wLAXmGb7lOn_d41PF5sfMv8OURpXyVEomA8WuLVIzyTz_6evlHPq5Grl8k6aT9ZI2A-TosYYZq-7QhvTVPhXqWM50M6kcaioiOimVW8ce4JZ11S4MDLjxdK8C0pnGMnwczyb1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇵🇹
اقدام جالب هواداران پرتغال بعد بازی کنگو در تمیز کردن سکوهای استادیوم محل بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/94645" target="_blank">📅 12:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94644">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
لیگ‌برتر فوتبال ایران در فصل‌آینده با حضور ۱۸ تیم برگزار خواهد شد و این فصل هیچ تیمی از لیگ‌برتر سقوط نخواهد کرد. همچنین بزودی تورنمنت سه جانبه میان گل‌گهر، چادرملو و پرسپولیس برای سهمیه آسیایی برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/94644" target="_blank">📅 12:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94643">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c445efe2.mp4?token=f7tF8dbNjPQWphbn_Lzvi6e1BlHCmKaJZK5jbP-0-NtEEOxRRnDSlWSytextPAHz6iUtlvCWeGr6PMXC6BbMgYKzeygJ1ClZ84GD3IDIqwNPB3esaOlHILg5Gf6gcO1iowuar2s2-PysS80DMvctgLpiqobjZ8Pm9_9ye_A0oHUlCTOZkuinYhVY6AjHx4pu-f9RJlYk1NaYzTm6Np74MPl1ex5ESHcu8UFuVIDZxSn368cVhHOuJO4EF5pAzkYhEma3ZGUfQG4YcZe1n44MzgHgYA5IQtqAwDRb0udJvTHcJXs63SVVXjVtx_bkHeaP-Ejm9fM_Tt1I69EBQPUWoDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c445efe2.mp4?token=f7tF8dbNjPQWphbn_Lzvi6e1BlHCmKaJZK5jbP-0-NtEEOxRRnDSlWSytextPAHz6iUtlvCWeGr6PMXC6BbMgYKzeygJ1ClZ84GD3IDIqwNPB3esaOlHILg5Gf6gcO1iowuar2s2-PysS80DMvctgLpiqobjZ8Pm9_9ye_A0oHUlCTOZkuinYhVY6AjHx4pu-f9RJlYk1NaYzTm6Np74MPl1ex5ESHcu8UFuVIDZxSn368cVhHOuJO4EF5pAzkYhEma3ZGUfQG4YcZe1n44MzgHgYA5IQtqAwDRb0udJvTHcJXs63SVVXjVtx_bkHeaP-Ejm9fM_Tt1I69EBQPUWoDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏆
🇺🇸
صحبت‌های جالب هادی‌عقیلی درباره دلایل رشد فوتبال کشور آمریکا با پوچتینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/94643" target="_blank">📅 12:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94642">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCyoX0ovWA90lcNQ446a4Mep9lGZuCe5U38xOKp7kJ_XEIMoB6uzpegOX_gY0MDnKmxDUbBZKHSb1c5a6oaHqxlWiPPiwVZM293QIw8mbOUWPaX_nbpXQyPZgSVMFswBzeyS0knVNWTh9HOLWoRFClPWA_A90p9hyhM8xajR_9LMGnyri7ERIageDfb7B_SXRhp8Lrf6b4nME_SKzqGrxPpIW_3F-4VRsbPHw8krgOoZDjid3-g-WKevwWegyJH0FBGMlNrhcOrAiOW8C4uFL-Tt67i6YFgvzBataZYZpwOTTu9NRjjMPxbVDKrHorVxZxk2GnpL-F9UIdGK_biIjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
وینیسیوس جونیور در جام جهانی 2026:
◀️
بهترین بازیکن بازی مقابل مراکش
◀️
بهترین بازیکن بازی مقابل هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/94642" target="_blank">📅 11:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94641">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXO62iQ99v6-Pfa4JRtj8TizRPetrRxQ3_i6sxXq9JNCuRalA5RHUFzLLDGawzYqb3R4uacvwein6GcNgo5o5cauXfAvUVH1e_pXrbdpLkEd_kb2Jcih7rexqPfBCi4z4l23X0Idyy2eYWTkZor-0cKB1EshBWS3yCuMOquvhbbUq2xvbpcBwNP7Ft9XTg1WZbiwF21pIOXaHJkVMIXkqkeqaa6x5Y7ldhFXmTETQwS1fnQ37Sfym9jZe5MHvQXZo01HojHAo-uvaM84Z_nxmuOpX1-qkb9iJR1HwRKECg79w4ephBmUmMvI5h0q8kKTJEhfDEZVyq_Kz_jmxR-WCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
تیبو کورتوا:
ایرانی ها یک مدافع راست به نام رامین رضاییان دارند که زیاد در حملات شرکت می‌کند و ارسال‌های دقیقی انجام می‌دهد و باید مراقب او باشیم او میتواند برای تیم ما خطرآفرین باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/94641" target="_blank">📅 11:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94640">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4XQrH3Jxc4k7_y4WAe13EJL4IJVA52zSB6ZlNvhDV_P9nlxk0UoTlIGApM1hQsoIDpyhSgsSUPbC1tMYI2Y_Xkd1auOk4SAD62H_Ja2nDW2EEtBuIRtBYe7ylHX1fgytZCjBeKLb1kJD3Ny08_vjmwNFpeYUeIDFk1kRLLBhKKTzK9GCYvyob6cwfEmqdc7SJ2PvwGQ__WMhnQSja3cYmuQG8GmZdiwoeNOCjB7ASddpUYhoYl5_9AvVTodMtgplLNbeHFubAMVSS8Ewcu7UHycEQtID0SCT9sEbiAI0QQWrWVMtTN45COQd59Z_7FtD87fQgfAFhgJTndO8sQ_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
🏆
تیم‌هایی که تاکنون در جام جهانی ۲۰۲۶ موفق به گلزنی نشده‌اند:
🇹🇷
ترکیه — ۰ گل
🇪🇸
اسپانیا — ۰ گل
🇩🇿
الجزایر — ۰ گل
🇭🇹
هائیتی — ۰ گل
🇪🇨
اکوادور — ۰ گل
🇨🇻
کیپ ورد — ۰ گل
🇵🇦
پاناما — ۰ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/94640" target="_blank">📅 11:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94639">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6bcd7de2.mp4?token=P4eFAaps_o3iaZg2EbQLXjsJlx4PwpzOfET786voVOfz5kyfJ8Ghu3vE-HjnQ1xVlDz3O4b47M1-s66zcv8FVfk_a6mvGjWs2y1kkge3z6bjUAbSao1pi9eZ9WDHamrzIJmU1GrdAcrPsZIf_vIiIl_TNORzyPsA70332Vij7DGiJ7PjUVtGf2SLW53-pAYO5ZUetnaPrX2wu5YQ7SFcMoYFoGZKMgq_dICguottiBjPodNXhNZ0U0uQxcjiOJkwqGBQuN2U-QWU_4Efv9lp9g-kmYoLUuQpdHDeKwa8_GiExiIqFmXulzxnjmLMfN9hpbmtAKl442mikgnP7C097Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6bcd7de2.mp4?token=P4eFAaps_o3iaZg2EbQLXjsJlx4PwpzOfET786voVOfz5kyfJ8Ghu3vE-HjnQ1xVlDz3O4b47M1-s66zcv8FVfk_a6mvGjWs2y1kkge3z6bjUAbSao1pi9eZ9WDHamrzIJmU1GrdAcrPsZIf_vIiIl_TNORzyPsA70332Vij7DGiJ7PjUVtGf2SLW53-pAYO5ZUetnaPrX2wu5YQ7SFcMoYFoGZKMgq_dICguottiBjPodNXhNZ0U0uQxcjiOJkwqGBQuN2U-QWU_4Efv9lp9g-kmYoLUuQpdHDeKwa8_GiExiIqFmXulzxnjmLMfN9hpbmtAKl442mikgnP7C097Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇲🇽
حرکات موزون بازیکنان و سرمربی در رختکن مکزیک بعد صعود به مرحله حذفی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/94639" target="_blank">📅 11:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94638">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b6c764c3b.mp4?token=rBdOhwDxif2sD5PLixCvg8LFWXbEFvKfJvPN7_h7ErzhbAG70dAKORsCR_ZbD2ECanf8gd_AR1R4a1CsEw7EhTHx-b5al5l6oGE38L8U0032LKnvRZsHKIZ9MY4h3UVHDTq69YOihZDGvhOgjBtVkhscTJbHd9Sfw9xxW5KTJq8FD0AZqSRMuMxIAPYiml0xMaLU7DfGZxDj3HcKX_QztsAZKrGvwj2r1QsiogXh6e1y6pWx5xl0fOvX6tBW1uBcW0V6AD5-GQ_jSApHYHexsicohe3sdOer1DRxL-AubyK83Kj0eKGyRxcabf_ihXK1Ry8I1w4Zqfs89S2vj1arrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b6c764c3b.mp4?token=rBdOhwDxif2sD5PLixCvg8LFWXbEFvKfJvPN7_h7ErzhbAG70dAKORsCR_ZbD2ECanf8gd_AR1R4a1CsEw7EhTHx-b5al5l6oGE38L8U0032LKnvRZsHKIZ9MY4h3UVHDTq69YOihZDGvhOgjBtVkhscTJbHd9Sfw9xxW5KTJq8FD0AZqSRMuMxIAPYiml0xMaLU7DfGZxDj3HcKX_QztsAZKrGvwj2r1QsiogXh6e1y6pWx5xl0fOvX6tBW1uBcW0V6AD5-GQ_jSApHYHexsicohe3sdOer1DRxL-AubyK83Kj0eKGyRxcabf_ihXK1Ry8I1w4Zqfs89S2vj1arrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
اقدام تحسین‌برانگیز یک‌پدر ایرانی درحال نمایش فوتبال برای پسر نابیناش که در رسانه‌های بین‌المللی حسابی مورد توجه قرار گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/94638" target="_blank">📅 10:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94637">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f084797b56.mp4?token=TcIx1bROJRxrWmJfzoILwTwFRSG_RJvN2YKX_9vnv679pJLAvAzaq6scnfWgjuD_qnDxskreSW3Qs-wQTxKtwUTz-zsEtrF2Jp8mNWZUS0O40qdlwDnGpCaPYe6CZ3FEFXOYYZwrYttlAgEZy0a4spsCX5Ilfsew97Fn1fdldAb1xTaek-9xpPalTejf1joYH4FcDyxzvOdROTtkfTM6n52RZofX7mG0VbGoQPsZsHIs686Ji9lePyXs2sMqX-DES8FfM-OrkpV3xxnnd3I7Nfocu3Ce9nI6ih6QzBP-HVcX0YoHjJUQBru5KGuRtS5KBLq-cVJBHaL-3rxmuUAjuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f084797b56.mp4?token=TcIx1bROJRxrWmJfzoILwTwFRSG_RJvN2YKX_9vnv679pJLAvAzaq6scnfWgjuD_qnDxskreSW3Qs-wQTxKtwUTz-zsEtrF2Jp8mNWZUS0O40qdlwDnGpCaPYe6CZ3FEFXOYYZwrYttlAgEZy0a4spsCX5Ilfsew97Fn1fdldAb1xTaek-9xpPalTejf1joYH4FcDyxzvOdROTtkfTM6n52RZofX7mG0VbGoQPsZsHIs686Ji9lePyXs2sMqX-DES8FfM-OrkpV3xxnnd3I7Nfocu3Ce9nI6ih6QzBP-HVcX0YoHjJUQBru5KGuRtS5KBLq-cVJBHaL-3rxmuUAjuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
🇳🇴
شادی‌ جذاب هواداران نروژی‌ در‌ جام‌جهانی به بیمارستان‌ها هم رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/94637" target="_blank">📅 10:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94636">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇧🇪
🎙
تیبو کورتوا دروازه‌بان بلژیک: در بازی فرداشب آماده گلباران ایران هستیم چون برای صدرنشینی و صعود باید برنده شویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/94636" target="_blank">📅 10:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94635">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d6852b83.mp4?token=kODNXc3-_HLjSxcVAmle6lgyVVZlW_-m-Vzeb-11sCi2ZbV5-0oGUGeGJT4zYSKrRAWcAQUmlrTb8oEeB2ZzeZe6_jVwuNHf41ZLSnEBjLHwjL5syy3eVQPPG0HRFe9wD2FXeu-ToF297QeM3mOFdAsrd0EzMcxeu072Un_8aw2LT2n_lXOD2ZKWMms6L4o3pUZf0XcN7_quZT3wia8YcFF1ahywJBN-79zpRnT50yKgCeujdO0iuh5pAt_rKW-gde_xr6k9EmU9PURThc1hS_aPYFeOQTPU750Di9Cvs4C5Tvv7HPCHwj8g0NESbM0zOeIv2X82twImrkwmFmGMmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d6852b83.mp4?token=kODNXc3-_HLjSxcVAmle6lgyVVZlW_-m-Vzeb-11sCi2ZbV5-0oGUGeGJT4zYSKrRAWcAQUmlrTb8oEeB2ZzeZe6_jVwuNHf41ZLSnEBjLHwjL5syy3eVQPPG0HRFe9wD2FXeu-ToF297QeM3mOFdAsrd0EzMcxeu072Un_8aw2LT2n_lXOD2ZKWMms6L4o3pUZf0XcN7_quZT3wia8YcFF1ahywJBN-79zpRnT50yKgCeujdO0iuh5pAt_rKW-gde_xr6k9EmU9PURThc1hS_aPYFeOQTPU750Di9Cvs4C5Tvv7HPCHwj8g0NESbM0zOeIv2X82twImrkwmFmGMmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🇲🇽
🇰🇷
هوادارای مکزیک برا اینکه کره‌ای ها ناراحت نشن بعد بازی دیروز با پسراشون لب‌بازی داشتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/94635" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94634">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYezfBE-88-HS20ZYDZ1YlDr_igNH8EnKYBVx8pFlviqoqRhWteu5yopLP5Lla-mFydUtPpTjvWrF1EwPcrKiW0qbieBRqSjIwWvUnvSqvw57ha9E5s7KoDYkd-zuly1Wh-vM7ihGXR0NB2DQe5-UKD4QwHbMkY5Q41NpI3K2s4HDf9FgWETwmY_FLrPbcxdt3DLRAELm45b08W9RG5OmB6g5eZOtTgQ6HHLRj-4mHAa900Qmbx5k7vLime3T8sCgRaoSCCQtdSpfs8LktQ6ZgRqiYO1NwN1fPoAvnA7byB3vA7WyvnCetdD2s_qSu8Q0uLkvcX4SmpxFBowvOlacw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇧🇷
#فووووووری؛ شایعات رسانه‌های برزیل: رافینیا بدلیل مصدومیت از ناحیه همسترینگ ادامه جام‌جهانی را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/94634" target="_blank">📅 10:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94633">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzxsTYjLtAarmfLsirmL_rSTpa7tdpnMSfsxpx9Xt09QyNWWu3mJrlF1jVjuRVcwmiNUe1dirzVOe9UKYqvg5DISij7Rgj6_vbvj7OY5GQ5MuCtky6KAmf6HVWQtbqZYuT_KBs7M6mgMRKla0XMplR6Jnl9aaktUIkdXRHbMLBWg9ljLk97GtmK1Pxdv9rGY9NM8yAEOHYxmqOXBmsB-kZWdzsWhG9vORFD1978NFs8fFqOMhOQJ4YRvtIX2N8Z3Z-RV5U0aO7ZePwF_SOsXwwOeYB9t0sqnSbb74ITyMLfIxG8N5NNb4kzkRN1B9vU19szJgv61Lq0G9haDZNLD6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
فوووووری؛
با اعلام آنچلوتی نیمار هفته آینده جلوی اسکاتلند میتونه بازی کنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/94633" target="_blank">📅 10:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94632">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060b592f3d.mp4?token=t-uBFyLE9zGko_-_kjAXu7wgBpBr5cXZZO2BkXe9cjeS4-J3gjOgYu-MOaTJU-DeUgwLYeHAO5bCyeF4No4ngoBvP4IXjM0-N4GlBCxhjgNkSZujSBzbSTq7FxiJAFKPyzTWf95ITFJ4ZGZDxPVD0mFB_FxwmjjkmPWdolgIQaxr1wLaESSFk6YpNojx6PXo3j346E0z4jWWtMLB3KX_VpM63wAO9nIuuD0TcT38qoB-1EGVAg5BPlOd9JH1H1BpIpWjI-u2nBUXzErcbSQLJHHqPbL-uSamh4XQI33PCTwQBUypbO8F-nnTFyHWU3EdSR6svVhmicUPOkUjiaXOUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060b592f3d.mp4?token=t-uBFyLE9zGko_-_kjAXu7wgBpBr5cXZZO2BkXe9cjeS4-J3gjOgYu-MOaTJU-DeUgwLYeHAO5bCyeF4No4ngoBvP4IXjM0-N4GlBCxhjgNkSZujSBzbSTq7FxiJAFKPyzTWf95ITFJ4ZGZDxPVD0mFB_FxwmjjkmPWdolgIQaxr1wLaESSFk6YpNojx6PXo3j346E0z4jWWtMLB3KX_VpM63wAO9nIuuD0TcT38qoB-1EGVAg5BPlOd9JH1H1BpIpWjI-u2nBUXzErcbSQLJHHqPbL-uSamh4XQI33PCTwQBUypbO8F-nnTFyHWU3EdSR6svVhmicUPOkUjiaXOUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁳󠁣󠁴󠁿
شومبول اسکات‌مک‌تومینای تو بازی دیشب با مراکش که حسابی وایرال شده
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/94632" target="_blank">📅 10:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94631">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4864edf2.mp4?token=lj6UQXKxhgYQVKlYCNa6qrCEWgZrJSRT0uTVA8SvwrzuxGBj5B27tpe1GKASs-0660-pSkNXRKTZ1JsMI0Opw73h79K1RGrccvorZWVV6um6nJ8_d55boxYo-b55z5EB-6MFMIoTmC7H9HVjN1soQ2JEa4aO8UE4i7bmzxR0w8XxSZnzjYd7UZ1WbwORZJNMIqh6CADs-SSJWJzqv6ictpDTAkeK9j9eZKSTPJLOzyL6O7zS67YzxoMx2Kha7AUv1t_hWSvofwazGlVfVO_rZPzwsnEiz085sggSjG5Vze5mE4lrCYNBdJs2KeoAI5uTzXr6bvcQ5pWHhec1YJZudQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4864edf2.mp4?token=lj6UQXKxhgYQVKlYCNa6qrCEWgZrJSRT0uTVA8SvwrzuxGBj5B27tpe1GKASs-0660-pSkNXRKTZ1JsMI0Opw73h79K1RGrccvorZWVV6um6nJ8_d55boxYo-b55z5EB-6MFMIoTmC7H9HVjN1soQ2JEa4aO8UE4i7bmzxR0w8XxSZnzjYd7UZ1WbwORZJNMIqh6CADs-SSJWJzqv6ictpDTAkeK9j9eZKSTPJLOzyL6O7zS67YzxoMx2Kha7AUv1t_hWSvofwazGlVfVO_rZPzwsnEiz085sggSjG5Vze5mE4lrCYNBdJs2KeoAI5uTzXr6bvcQ5pWHhec1YJZudQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇿🇦
بازیکنان آفریقای جنوبی بعد از مساوی مقابل چک، جواهرات و ساعت‌های لوکسی به ارزش بیش از 50 هزار دلار پاداش گرفتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/94631" target="_blank">📅 09:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94627">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qybBZSvn1_D_htqD0vYMsl0zVStAMKK9d72baJGdaPRigrEO2w-4BY7GMMezLMYmLeDczYVQ_YBtAApliFBbWpV0W72ts4d6QqnZDRO-ZCYOX4eR-QzUfNGN9_lavqclZAuLjfoUsbkcjmAn2hNbJIdlzmO8HtbDoJVn98lCReEAFKTDPuv7tO0WnWt5xp04l2kJ3Ce4OINQelOEPceNs8_JkElrUTbungXLImdh2xX5oxOj75itHf1qaMQfRaqs0DcUQlXpVJUmDt7yos8ZE9n6OWHyXtdqb9A-lz2E8EH4ADkb-wl-xP-iuE4Q-SSEvAzi28Ht-cbTm1tLU32fWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gkLxKkt_vlI1DQB5H4TiN7vTLAqinmg5qVZUmqUGjoq1Y-y_6YStPnsQxLpXLk5Wx9mLgoDdEJGajandYeBLubhTc3flD8dtmIikAM-23hAG3rxqlevR42H0v4xWLlpMxKeCHPWsVx0BSstWKw78ambwCaceD-5oH2F-u-6kkXMV1Ou8gsBdu27NbDwkWJq7b1eST6JKtUw5cjrjOAHNQC9YrrWjJMJ5ImBIWCbYgvrNaKg1zNqLqe9KRhiOnP0ZfVFeWfGYQYKMwGqxPZjjH3YvBoWtpkKvbJQL_OEiIxCMns1QEyQ7OsXRCj6tx9Rnt4MJHlEu1zuc21ypSjY0Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ft4LSv9Mpo6tr_X7aP2JlhWNO3XqzUNugvQa5AV-zp_4obNqq2Ac_B0GKg5vc1y-7QHXjMmlzPQ7A2sNfFKIXHOD1idXeG_uiFYRZmwxUYaWdPXZUwlRL7c_btewknxFt8zYQnAofPU-qv_gf3cLGrulk_Ro_4_hJPuMW88osl_L7ZiP4j0hlgb09juWc1C4F32YwY_NSyQItaIj7uUZopJ_OqGNqeXYoD4zbldNHrdBfBb9QHZQX36AXmjteljaiWb4clh3d8lLAHczNwE6g_lbaKDMtvLTMMlJ6KLr1dmjdaOLEx6_O2Ugr48YLqIK6fJ1MbFGg__JFJfV19oCAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eo7mDHkiHyGD8sX3hn6NJGVcz8ye443AulmIsE3MmVqAHh-h_8cniN1OG3rmCicdoWC_yMJZU8BIxxXjn7cf-nMh_HSyQub-9egUPGKrllc1T5kfWAFI30YxUPSDZLvIgvhG8is2CXwlCC66E8rsX5MokFhneh7iqGvN2iWr-W1_h_vxtbrTXvGhMHOqzY_ETxR_RLYeP3Y3H2Zc5oOmgkqzFrNNMpvf1jLnEOyOI-6Q1KtnSx9jLqA-Hr8Ukt7kJMmW_NFJgJHyoLGZa6acfV5dpr95PBL6vel--qcsInOpB4SaAieQ2X4QEJIVmNcQMEvST06zd5gUFgXSkCkd5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇹🇷
هوادار ترکیه در روز ریدمان کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/94627" target="_blank">📅 09:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94626">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c7c76bf8a.mp4?token=B3yzPWX7kP_QJHiNRogvSTgZmtXug6lhp-xlyi42-BzbgDkHCjtBCC72rDDIgsP8fD5zoAj99d8jBul_828vbPmi5Z1cf5uXifhI_y8-nxawwER0EADdqJ26vzrVyP2KN8DH18usNkMNVZ--8jV2whjbrDoTQVFf8JQeLQY1ittnTsqqGlOlZVpAV-rq88fVCS7mDGitQ_jY7788SLMnBBiH8lxqJUL9UFpuiRRidUccXyW23ynmZO07lq0aFlSXT_HRALmdugB4CPrhEp_geYcvCtyiWuSqGDpdf9yj9wsGTPZ_REblIKbudTwT7GdOQJrNYZKrBnYlTiH83d4Paw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c7c76bf8a.mp4?token=B3yzPWX7kP_QJHiNRogvSTgZmtXug6lhp-xlyi42-BzbgDkHCjtBCC72rDDIgsP8fD5zoAj99d8jBul_828vbPmi5Z1cf5uXifhI_y8-nxawwER0EADdqJ26vzrVyP2KN8DH18usNkMNVZ--8jV2whjbrDoTQVFf8JQeLQY1ittnTsqqGlOlZVpAV-rq88fVCS7mDGitQ_jY7788SLMnBBiH8lxqJUL9UFpuiRRidUccXyW23ynmZO07lq0aFlSXT_HRALmdugB4CPrhEp_geYcvCtyiWuSqGDpdf9yj9wsGTPZ_REblIKbudTwT7GdOQJrNYZKrBnYlTiH83d4Paw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇲🇽
مکزیکی‌ها داغ و جذاب بعد صعود از گروه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/94626" target="_blank">📅 09:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94625">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d20f3a10.mp4?token=nb9YFfd-iiPI7UaVE3p27VYAV_53Xj4hfzTtKOGXQMA6yz4Na14NcV9IXybuUtWTQYJneKycRnMu5V6ltYeGXDTSrNkNyCtPzf0Cw_3s1JXHKYSOSAMg6prrd0fW8jCa2Vy_aC_imi1gkoZYazaGsEs6cIGfLqAb8T01PNsAZy9uJMrYFagrqAZKFv2bYkRpVDyuvpV60R3lMIFQbheZGx85B15rHorxFbNyLkHRXcaIl9dcRywAueP1Cd-YzfejaKzBnwjezYjxWIn2aH9SfhEGGXSJ-NTOMc3PBPtAIleIPBtc-OCYBrOV7zjtunOELM5kBH_WlfbyGJX2yuaEsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d20f3a10.mp4?token=nb9YFfd-iiPI7UaVE3p27VYAV_53Xj4hfzTtKOGXQMA6yz4Na14NcV9IXybuUtWTQYJneKycRnMu5V6ltYeGXDTSrNkNyCtPzf0Cw_3s1JXHKYSOSAMg6prrd0fW8jCa2Vy_aC_imi1gkoZYazaGsEs6cIGfLqAb8T01PNsAZy9uJMrYFagrqAZKFv2bYkRpVDyuvpV60R3lMIFQbheZGx85B15rHorxFbNyLkHRXcaIl9dcRywAueP1Cd-YzfejaKzBnwjezYjxWIn2aH9SfhEGGXSJ-NTOMc3PBPtAIleIPBtc-OCYBrOV7zjtunOELM5kBH_WlfbyGJX2yuaEsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
بدل‌مارادونا رفته کف لس‌آنجلس سفره پهن کرده چنتا حرکت میزنه مردم بهش پول بدن
🌟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/94625" target="_blank">📅 09:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94624">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🙂
🇹🇷
آردا گولر بازیکن گنده‌گوز ترکیه هفته‌قبل: ما از هیچ تیمی نمی‌ترسیم و فقط به میخوایم صعود کنیم و مطمئنم موفق میشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/94624" target="_blank">📅 09:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94623">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7068c129f6.mp4?token=m85kIj1JqxqaHFZ-_dJwpK3Zo1XkNCe0PibiRFOax0tJTomDddz3Ww1W7KeHl83hK2LHJKiA_bJpkWH6yeoII03seW54iEhfkvKH-1luXO664hSivJypBYqWXFuf46LMi2j2rHihpM1vOsH7QNkKQSoSOMKxcsakAFq2E6mEuuCUuihtsbh_jFlXc_YzrCM1MJTszbh_4h3QW9_PEgk2wwLFFIrB07xrCF3t_8Uo268uBbXZwuKw4zTYp-JQEe3T6WM0mIBsqgMZm85sDv5-2Wzt0dHEhwzLso-dFycTQbHjnzpemrXSdd8w4ldi2mU9RDU3zHagkTZ5lz1aDftusw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7068c129f6.mp4?token=m85kIj1JqxqaHFZ-_dJwpK3Zo1XkNCe0PibiRFOax0tJTomDddz3Ww1W7KeHl83hK2LHJKiA_bJpkWH6yeoII03seW54iEhfkvKH-1luXO664hSivJypBYqWXFuf46LMi2j2rHihpM1vOsH7QNkKQSoSOMKxcsakAFq2E6mEuuCUuihtsbh_jFlXc_YzrCM1MJTszbh_4h3QW9_PEgk2wwLFFIrB07xrCF3t_8Uo268uBbXZwuKw4zTYp-JQEe3T6WM0mIBsqgMZm85sDv5-2Wzt0dHEhwzLso-dFycTQbHjnzpemrXSdd8w4ldi2mU9RDU3zHagkTZ5lz1aDftusw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
رونالدو که تو اردوی پرتغال حضور داره، جورجینا رو فرستاده خونه تا واسه پسرش که ۱۶ ساله میشه تولد بگیره. پسرش اینقدری بکیرشه که حد نداره
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/94623" target="_blank">📅 09:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94622">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EACkQgOuQDkLPU9icNtyHZLio-mEiRwgGekJzpCjJD3GSCcDnO5kpdH2KfR8i9j4JUCJGyFqGOcGdRaZq8lXTzY6dpqe6bMr7Ml4Kb6Dy1hcQMS3QjdQ5iAcqLr6_HWTxcntrj_1fEtKt1dIyu8PjiZF29FZR8Jcf1dK5MAegsIxQAvI_MwZ6WXhorsFTwSK2CqsPrc2a7IQ8hamquXSPfx6lrY9LLzYkD0XlBKGRwhu8epSCvlftYIHvJD24KgHf8plziUk0XJk4G3WMVENorR_URLthfhfPwAPbc2umFuFjibRqVfdIIMCP3NjYzDRlOlcqt53uVY55loiQ0V_LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
ترکیه در دو بازی در جام جهانی:
۳۰ شوت مقابل استرالیا: ۰ گل
۳۲ شوت مقابل پاراگوئه: ۰ گل
۶۲ شوت، ۰ گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/94622" target="_blank">📅 09:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94621">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8g-ENfUS_Kjrl8Nq6mnZBFksA1gVrpLh40awbgF8qixhmo_37Zm64nCzwhJ14YD7e-p9U2PmQsglycLE_Itz0mPEwN642leBJQgVaMFPUD0tq2JMNINbCzo5odxV64qaRDJeVeyRTSV1mS-OyM0qtgEinVhPyL6UFB-t7S0qI59DWSBOaE9EwV4mf6xXyzj-pmQy9J90MOyih7jkGIESl6uf_NtCi60IrdU00Ce97L2aEK1E2miVIEN9wKn9jiAXBmwtHZ4Z5mkqLiMyHYGSFR6N0KppRLEdjCZDFYyHU3-0gLJ-p5NNz-WtQ_ixlw9iuXCoA39VwLjZczIynVRFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
نمودار مراحل حذفی جام‌جهانی؛ آمریکا و مکزیک به عنوان صدرنشین صعود کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/94621" target="_blank">📅 08:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94620">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVaEamukH2xxFqnRl6GZU6ZwW5Kj3-6CgVAbKyJmhiX9L8rlMPk6WegecXJj8QarUMIboA-FbMwn7E5G7ivEbeNBusItS24BmACJm06YYczMfAbCo-DUyq1zumuEuav92VTA4VNQnHtKKmXv4908oOqVOMxU3LMHkmuCSovjj3VnODEcC8cygm8SbkiUs96jLkjYF3ttNjO5XjOfzR6oW0goqXjDiUJOG4RhwrQWgZ8ajdVu_d9oPS-TPimLm7oRZGN0-fv2Q2_byGhF6vsvGtatJxxGWo-49lGW3qgPLdwSOkSSFCEttera2wE0D66dxaTfTn-if8H7kBJC1LD-FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🙂
🇹🇷
آردا گولر بازیکن گنده‌گوز ترکیه هفته‌قبل: ما از هیچ تیمی نمی‌ترسیم و فقط به میخوایم صعود کنیم و مطمئنم موفق میشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/94620" target="_blank">📅 08:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94617">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/srW50-S47mPvpt_YVah6qo_bQX1P4OWYB1hiv8kJ0rXcm9_6g--O4YxfXlHpIcLVFU-fVmtxBM06f3Dv6fimxbyQoGsTFV2QJ9dh7sOVVhZpB603Ozmyyt82OEbXeoW33cgB0gNsFFZatiJZCwn8OXsT5QCw_Q2zTxUD7Y6_qQY8fnYp3xZ_UK7qfB8sbzT6vqTZo4pIYf7vXo2QiXi_9_LSnWnKtA7s_t2pqdzmNec3QOOjh-HXfxehGx9yxW7EswXxYJd8xUce4MVgvDxf1FbP1RKIAqejO474_hTl8jUpWiwE_89CfdT5ECLDXLm0EqRH8gLocWdF73GJJeqgcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YcbJX1OskfLEo29ifGIW9q26PnvcNE-cmJV17ZiDnxs5SWxK78TOguffhs7U0oIKWkUi9UCJ_pikEzYx8q_JzHx-1ULzFbeTY8xdrwGl3Q25lAPYLMIIHnEw2yolwmsFgwiE-krTxBMxXSkUu5jOm1A5Cuu3TDVOgY6_MWGiAV0g7ogaYLMhcZss9m9KYo08zVNM7KCiSEtj2xTXdkS-SqB4RRLhaJ2RaGrogDbNMO0-FrGeAcIB0yosQRvQktf7m7AqutgW4MCohpQ0AVT1XrXBIzqeIuMAhi2bl43FNf4e88UdZZrqKVqO0_PHN0_m7hfVDLeYkCfxv4j3-Cy7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJB3aUnIixEOuYzs-jNx4PfEwtN8gsj2Am4icZrnkJx5gFPjK2V8Sn2geZMEDxccbB-mChGA7El3-EjQclacRNPaRMrtV9suAboIMnftn07YH7xph-VqaUeyhD0dtlPn_cTOSfEIlhGhWESGuGls8axjYPP6U10Lk31StpgUGFo3fi5rn_v-cz8p4Kdf2r8MaYYAGOoaSd_zbrv1_qntvB8x__iBQrcz-eJXHRXOHQ5NvdiOYxtl3rK9rati0YTsxzoUoq4UPVho1Tz_grzmFVnjeBaRDnSvOtM5V2IBS4sTO4dosdJ3iGyeKO7t02CZAOD9WGNJr6wz7NlIESI1HQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
حسرت بازیکنان ترکیه بعد از حذف از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/94617" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94615">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlVkAAKdyi1FfDjIZsvIepNAyzpVw419uBdtXXd1LY5K9IivfQSVOxIWnz6F3J3n0JONEuHTQxYAV6m5QGJgX9hVZvsTP86esuCKoqtN3_1DDSyVa1Brv5jp1M3AROEJUcO22n1l7n26UTTMk4i_VC1cxTI3e0JiW9S5bnYW7ZBuj1zl6rCNSXJFDZM-_3tk-YfvtkEs1tMxj1XM2sIw4aiivSm2hes4TOZepACrMal6PqRa0G4YOG3Q3y7WV51hFJ-_frwW-ypVUB5kZqX97G9K7ydOa1y7gWircDeisf_zF-8ul8Wc5nDLNmEriX0nSMZ_5cqQHGPMD64g2k9zLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|مقاومت فوق‌العاده پاراگوئه ده‌نفره برای کسب سه امتیاز مقابل ترک‌ها؛ شانس با تیم آمریکای جنوبی یار بود
🇵🇾
پاراگوئه
😃
-
😏
ترکیه
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/94615" target="_blank">📅 08:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94614">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTjkxNNoWKxdoMtiI3TJmqwUR93znzfBglCGQyawq5o1Xti-TEkkl1hjt-5kP9CiMUIgEdGawhaKN4HXSzANpNiap6sNrUujt8BOx709eO9QG1TKAT9JilTwl_EKbuE1ANPQ18cLaKJNEICJtaeWWwkidUByKoSmWLgkNVIIfDEXTPvlerLoLe3IIoN6YDAw9aP5DkZVvHaz_84BDjvGytNlyqxx1-4fC9snLBdjeH9Ad7DQWU5Lw8mccSgmlKYhn34b-E0OXOz0eaqbc7zX2VIjtedEXaoSxzDzxt3_VahRcTMY_dVPpPu5g721J3YNl8A2P3YMxt2XK7JuuGBiTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی
|مقاومت فوق‌العاده پاراگوئه ده‌نفره برای کسب سه امتیاز مقابل ترک‌ها؛ شانس با تیم آمریکای جنوبی یار بود
🇵🇾
پاراگوئه
😃
-
😏
ترکیه
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/94614" target="_blank">📅 08:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94613">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
۷ دقیقه تا حذف تقریبا قطعی ترکیه</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/94613" target="_blank">📅 08:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94612">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🏆
🇧🇷
#فووووووری
؛ شایعات رسانه‌های برزیل: رافینیا بدلیل مصدومیت از ناحیه همسترینگ ادامه جام‌جهانی را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/94612" target="_blank">📅 08:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94611">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آغاز نیمه دوم بازی</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/94611" target="_blank">📅 07:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94610">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgECCb652Pjo1dssVDJbWFMUP0rvIok-mfiV6CuJyBZNY-PCCjsfulv98uXQD2VaphEZH3X_duZY3cJ_WjEk8q96PQs0hU_biL209dGS0kJ2Tf_c0NVifpq35H5XqJMfar1o7VfUETfRsCyaO9yUz8doBlUW25vCmMBzmkAtcl_CEtdBH0ppbvO06bje5FuGpKrdk9nGiwwIatWGI7ehU5YFxn9xWbowylST27okUHRR9waFcR6YPOFKcTaD2KXdEasQBghcSYSL2wJMlHWfI_ippGIqb_2Un4hOMV5xCc5YLWVR4vhM7wiwl6GLqrhgEH-7xIdGjzXWdt82twNRSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🏆
میکل‌آلمیرون اولین‌بازیکن تاریخ است که با قانون موسوم به "پرستیانی" یا همان  دست بر دهان هنگام صحبت کردن با بازیکن حریف، اخراج شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/94610" target="_blank">📅 07:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94609">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivIR3a4RyFmE01BZUUr1o1scpMZ6JnLGxtzAtXWaWNCl6zeq6tW4DOeOUiUSmcaRVz6w031zF-vlx-68q8f-plSDWv0-RjPgJz3326jOe08HjKQJbA_wb8E6tpS0RN4GmvnB3n53hnRfp7qIIxOcwmVkT9mYbvBNra8DmmFB95FxqIrdQZdTl9bP8l7lQdePwHjjNDG6ZFKSY8KQcBuFOqYvfbkNyRy9UtS7gVbe4nLS9izZcjirRhpXZPTkeVFztZRJ6aUlVSu6tAJqRtP-w_p1Z9_CBanjmSUA_o8MHupcH45kIRJ4RK_i2C858m_fum82mRI07Jv4g1ou4yqkPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇾
گل پاراگوئه به ترکیه در ثانیه 64
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/94609" target="_blank">📅 07:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94608">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odxWZAml7Ccy5_ClLFQiHPETT6S5sUrgN17RgVLuZxduH0N2OjjPIank0G4pym-pK2x1DPL0mZsMF0GfakutL9tFJO-Ois0SowsBUjBTiqs00FdxgT5IoBY8EPcxwYCYwxK-UUy4LpPk_cR2Rmo45WlJynu0OCaUyqw-8OOcd-2gQ4PBmAXUard8jw2GxrnfW3hboHhwILfgBiTYxPuwc4YxYtyBRhxOiYdP-mzQYMt9-ZAcgRmBJX8a8fAt6UWV3lcKGOKwu0-xux5YmvXjqKN7Kh5-nypuP0Krx97Vm3AZT63it9pxUHplZr-Q8s28YAxocjGYWxena2LxdDm01Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داور بازی چون آلمیرون دستشو گذاشت جلو دهنش و با بازیکن ترکیه حرف زد، اخراجش کرد :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/94608" target="_blank">📅 07:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94607">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a087e0f84.mp4?token=bS6t3VL4UiY7xXqkPOv-UIROT3f5M6SRjcZWw_R2AkBC8WgujTQOnPEYlBO31-mSVsQfNO-VvCDlpo8ber2DvIQQJXsV6S_H6VDOhkOxSeni2TTOQkLleorHLgabBglQTphi9gCz6Ci8aqYMqwHiOlUsvRdFYxIE_M7rwwdduTkQLjsVWVvTDpR5fffd7ss0ScozrW5JEK2yw-AaJS28dDO5G4Ebfox3nY9rQvKYjaFkIzUr-YbAsyIEI8dEWO1T0sWU8kNzfM10qVjMPgpmo6eGXbNSbs026f6Xx1MgR_r2uKZiK-T_h9GWG3wJ11XwNKBWV6nu3HJ8F0hklNySbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a087e0f84.mp4?token=bS6t3VL4UiY7xXqkPOv-UIROT3f5M6SRjcZWw_R2AkBC8WgujTQOnPEYlBO31-mSVsQfNO-VvCDlpo8ber2DvIQQJXsV6S_H6VDOhkOxSeni2TTOQkLleorHLgabBglQTphi9gCz6Ci8aqYMqwHiOlUsvRdFYxIE_M7rwwdduTkQLjsVWVvTDpR5fffd7ss0ScozrW5JEK2yw-AaJS28dDO5G4Ebfox3nY9rQvKYjaFkIzUr-YbAsyIEI8dEWO1T0sWU8kNzfM10qVjMPgpmo6eGXbNSbs026f6Xx1MgR_r2uKZiK-T_h9GWG3wJ11XwNKBWV6nu3HJ8F0hklNySbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇾
گل پاراگوئه به ترکیه در ثانیه 64
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/94607" target="_blank">📅 06:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94606">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترکیه خداست
😂
😂</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/94606" target="_blank">📅 06:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94605">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دقیقه 1</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/94605" target="_blank">📅 06:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94604">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پشمامممممم پاراگوئه زد</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/94604" target="_blank">📅 06:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94603">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شروع بازی ترکیه - پاراگوئه</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/94603" target="_blank">📅 06:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94602">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc234e406.mp4?token=YEZ59Sdzp7vb7-0LmLYaJuBFmoZ8h0sW1d6bHjOnHP6keOBbFQtFbUF6WBO9TalmJ_A6rtIhPBmYi7rqT0I1oK1k9Vgp1qxmW3lOx4EAiRucgB6trq3VBRw1cd9xxPcFrVvQm2G8kcW11FXRF-1RIUVVIQM185OlNP_Wfm36iRVqPIGG4fewJwZU1m53SCksf_uui7N22uudubbh6l-fKJIbSkdFrF-jhHVJSHLyLXvAwqDsQDwqJ9vKjVeuLSQfH0EEUHzyzk9KQCCCWQsYdzE1BXjQ4pIEnRfm8ZfN1LLTRzMwm-0BJgr-SYiBZLS1ZGl128KJyLseNeCeessryg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc234e406.mp4?token=YEZ59Sdzp7vb7-0LmLYaJuBFmoZ8h0sW1d6bHjOnHP6keOBbFQtFbUF6WBO9TalmJ_A6rtIhPBmYi7rqT0I1oK1k9Vgp1qxmW3lOx4EAiRucgB6trq3VBRw1cd9xxPcFrVvQm2G8kcW11FXRF-1RIUVVIQM185OlNP_Wfm36iRVqPIGG4fewJwZU1m53SCksf_uui7N22uudubbh6l-fKJIbSkdFrF-jhHVJSHLyLXvAwqDsQDwqJ9vKjVeuLSQfH0EEUHzyzk9KQCCCWQsYdzE1BXjQ4pIEnRfm8ZfN1LLTRzMwm-0BJgr-SYiBZLS1ZGl128KJyLseNeCeessryg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار حمید سحری از اولین برد برزیل تو جام جهانی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/94602" target="_blank">📅 06:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94600">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgiJQ8IxJLcuO0uHcGEiEBmUzM3Ea8DlR-3SNmDbholu1ZBbl6mkhiqwGbpKTL-3A7LYFfunOu9U0_r9uJlkju6nGT-CQwNv_5UgiS5EBzpEa5TDnqfvWpTzizaO6JYKJ0Syvb1dHBSpY6vcFofGPJdBAl1UZLVO9YT13pJ4rT4LhiZ9Q-7cvIAg5lynapEqy3QZ81y5QQv6Mog7xJqYxuIlSyQD36L2CcDHhyszXJdOSzn2TecP4GqUAosc2LKcBpEsDaMUmVNIjXe_-vmFGiDu7h5d86B9S2eLAsHqBFE6Z-hhqoyLYUHQbJ18SFznQhg5AQCxqSWM3ehDWUSUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
📊
آما
ر
وینیسیوس جونیور زیر نظر کارلو آنچلوتی :
‏199 بازی
‏
91 گل
‏68 پاس گل
159
مشارکت در 199 بازی!
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/94600" target="_blank">📅 06:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94599">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efbvu1rdVwte_P1Diq3RgTDJbNEbn4auFw0a0CAhOaGKzsbS6tHzlCBX76JyrP_wzDu0nnmAJ159GdHaV_ljDOrVc-vGATyeF5vAXXZOdva6zU0d-4nw7mBoolF2l6SIYGyDxFbpkaGjnPXUq-i8l-8m1liypZY3FApCFj8stJX5AOyujlC5hDgRIwHAHRq2RFypfYB-wkvh3IgazchsHezoP87XWSeAZYuR2FmZ2444RRFusCaPMsLkcfxl146h5_zsU1L1WEHqqwoafLZxe97yKYOQdCw_RdmJBayke96UPtxdLIsUBoIEp8tTeMj3oKmSLzg2RgQMnsoWhnJ8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان کمرم رگ‌به‌رگ شد از سنگینیِ این عکس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/94599" target="_blank">📅 06:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94598">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrylDIu5pTjMWkC-ogGXJW_GFvMWX1W_Rm2ObK6j_UycYysS2pGCfCll8ibKKAAnBo-0drHX8k8XWWv2iNcGrn59DAZAkijUmh4WyKLKNV3Pqpnp8ZlPCAvBmpc-EoHwkqowHUx88aXt_V_XAUBqpZXhIBU_7R1ImcHYdikDrQjm3RZFvMOKLn9q8JbnjAEvjvZjXlcISCRMJp6_pFBM-oMttKyuplGT1ilGLzG9BHeD5R2xKZuD-geAjysW3nmJ3TCifBwwM-1YBLiVrkoRKjGcBX_yHcW_0Rl_pNiGPnMvKmJ40_9I9pis9Fm8HLgwQ4XRqZx2NFEzWFANXXj5CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | برتری قاطع شاگردان کارلتو در شب گلزنی وینیسیوس و بریس کونیا
🇧🇷
برزیل 3 -
🇭🇹
هائیتی 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94598" target="_blank">📅 06:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94597">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cm8KRvcKkkoOlrZbl0n8gK_b2KR0zHDK9_34kvNZU7JME9jBwuxNNXkcBZvzdkd1DgghK628KyZs4JNm2fMZzcqPdjG1m7KSqN7nVDedDuj1rUsz_kgUDWXn45adTNeb_SVdGWuSNhwpXUkq4qYBAERvtJvM-sQ8m-lyiVc6x5CPBxl2nGep9GGm40yZw8T0BrtKSgw_Qtna0L2VdyQxquuCEhFBJ0naMqma_NnbsRVWZEeXpzpwvbEoTRCZs1bw0dJtUDJMgZAdDeNl8HmSU0lSMAE6jmW62S0zdZsYXivlKjx0RpSTljoGBfoeERFuXq2itjtTiYN4cACcc6gkWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | برتری قاطع شاگردان کارلتو در شب گلزنی وینیسیوس و بریس کونیا
🇧🇷
برزیل 3
-
🇭🇹
هائیتی
0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94597" target="_blank">📅 06:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94596">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GthIed7gPf69z_FCMgKa1ZETEhlqkhmZw3mpeL6hul02U3WHH0QaZMHFXgX-9bI5qxTVIR9JKeDuv6THfSmeQhOdOqZQ636x_4gj1Gdx9CtVcp4ImdN6ctErgL9v_6wqt2jvi_gzVDOinpQ05TMRBeS6d89bSpEbzxz94xTgkA3MnDoatN88t5NZKtmQuO027jR1wtx572XvscqzaT9Mt6xtN7kxk_QY_2TUvJ2eto14iNQ9UHVLsYYb6yHa-1FToSQ9ZoMXZiuPdbezsjO0OznysGABOSlLucv_BJ3MGKEcTM6nju565lXWgzVpbCL8IV2alcaXy3iK4WQL9NRisw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🔺
خوشحالی گل وینیسیوس به سبک کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/94596" target="_blank">📅 05:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94595">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Myelft9R4JFUbAvRrwPSLelWP5HFIKsEkr6Yyh5cvCgF0MrmK-ikUpC8mloDps0UKuFr_ubt9EuZIAEA5P2qO6zELRLi0SZaUmXyGr1hNnZ9qUuHxLnWuYD8caThf3jL7JpbE6SRvFWmQByzmwVvAEyMFgv6r95bYWoOeoDKqbzal5TBCFGTniY0EowuzC9NLJE-0us_aCCe7LLNwa_OPuKTUZO8eIk5NW0SYMmhCteR2aNNpb9pdZKzy4zEh9dlfWyE_GzdgllTmg9mdZvnuAVfIrAWoxHtitsAV3HaQSUo_G6fulrmba4wBT4ncbR2Yvn2iUx79FC8ohUHOiv3Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرف 2.9 میلیون دلار روی اینکه بازی برزیل - هائیتی زیر 4 تا گل داره بت زده
⁉️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/94595" target="_blank">📅 05:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94594">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اندریک زد ولی آفساید</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/94594" target="_blank">📅 05:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94593">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پله زمانه وارد بازی شد</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94593" target="_blank">📅 05:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94592">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a84e25e78.mp4?token=rN_DlJn5tQ0bQ7Iydv7_2MXYSK_8lXRysDYkyQuq_Oqwcf9T9A4nAVHsCDZYLYIHXtljpuojXoEO5lv1Dc3fyZ4CRLkbapWwwqibi3Qq0EO5T7I2GWUC5kqr61bk0RbmwwMYnjdbc7IWMnY5dZ4hts_98PyIPojeaxhBopvi_O546kiC62lyuT-6cqEa1m-yMOvAAmWYumJpib17dowFT2rr2u1nouM7vjeJo6wnVcZFhOw5A9LQMCT5FSRBr21_g2o7J9l6dWDETRGpTu0XOY-_rZ_2KMEBZxFWomJsTIFCspWd66XhthzlKjjoxwM1hdNP6ZIwyzrbZ3HBCDjgdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a84e25e78.mp4?token=rN_DlJn5tQ0bQ7Iydv7_2MXYSK_8lXRysDYkyQuq_Oqwcf9T9A4nAVHsCDZYLYIHXtljpuojXoEO5lv1Dc3fyZ4CRLkbapWwwqibi3Qq0EO5T7I2GWUC5kqr61bk0RbmwwMYnjdbc7IWMnY5dZ4hts_98PyIPojeaxhBopvi_O546kiC62lyuT-6cqEa1m-yMOvAAmWYumJpib17dowFT2rr2u1nouM7vjeJo6wnVcZFhOw5A9LQMCT5FSRBr21_g2o7J9l6dWDETRGpTu0XOY-_rZ_2KMEBZxFWomJsTIFCspWd66XhthzlKjjoxwM1hdNP6ZIwyzrbZ3HBCDjgdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وینیسیوس: ۳ گل در جام جهانی
رونالدینیو: ۲ گل در جام جهانی
کاکا: ۱ گل در جام جهانی
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94592" target="_blank">📅 05:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94590">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iHtIDhEACZINVlvgMRLXBwsJgsmauJRjLJ8TBN-7KUdqZ5xfb-sxDheO8CYb667o02hULyCDkSnxWz4Km51goFTDC-WvzPuk54T3Z3AeT3LfHEnOzKhPK5mr84P4wIoE5Vo-I7YJATbdQWRsLKvwCntVvl-bDoS0WDUXcCVd9GWre4ICeqIf_kATO9E9EXB-FptTnKGlCi4DGXkYWF3ceKca4l2roCD8hpC-Gl-oqnnDyOv3YbZI9j4TLqZwKvsch63pAwSSDyUTpzWj7l0s79RgApxYqHFrv3RoiCAwT8SFwUU1LLCTBGkxzjJo0Nnn-dNh2Htq3AgAmEAglFg_GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PzkyXZiJElYOK2i3szv4Qevf-vWn8R59ExQmMZTbEkb9E8BHtHfHXYqjpTUvo5V1w0CI1MWxiUNRF-mgXZgjjGZhIwgEyYT-UG7DOkjgkuqtomkU4TcCBTBUPWQLwZZ9I4RWzB4R7NmQSsnQ7bKPmxUVVdAcilV4WVSEPH4CI3bphYkJ8E0wMWKAlj83Ib7QIlFky2eTb4PjqcB06zY_pUlcC2j47Q2WPQ3REl7HECFnPx5oL0ak1dl-GRy59HXKEX_l2TOjHJRnlomdsG3_vB9U-Jl7cyGaZtlBTdVuxHAdYE-CwBtcc1srNaacn-KsSLWCL0V2fJOBFjvTFQWBnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇾
🇹🇷
ترکیب ترکیه و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94590" target="_blank">📅 05:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94589">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(ммd)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ea15ec78.mp4?token=mz8BxAaFh0NSs1CXq9dtYh-isJwsYPxUL7BkmknZEn8sJE2lkcVwJlhr4V2C0e0VB3nwNsDoSl18dLsmthjo0XE_XooUL_ZkEG5t0hKB8HwzVWprhENqs3I2bGx7wmcnn48lAoynaVRj7CR9wc6th3irCiDVpmdeZkMEzOyZmNBCyggmd1pWajwPNa6KlJJg0ZvFxo2AT50H6nggxLuvo1fQt9uR-CSXX5wlPf0kh6K0Yh5qRrib2v2HRyEuxGk0AM47LycQloxiRtUu4kMMLVvuoPcZmvQXJZ4Mel33DNRHvo6AfnVhzkkBa-NFUp-U0W9UqoyI6tkzrR0iVQ17og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ea15ec78.mp4?token=mz8BxAaFh0NSs1CXq9dtYh-isJwsYPxUL7BkmknZEn8sJE2lkcVwJlhr4V2C0e0VB3nwNsDoSl18dLsmthjo0XE_XooUL_ZkEG5t0hKB8HwzVWprhENqs3I2bGx7wmcnn48lAoynaVRj7CR9wc6th3irCiDVpmdeZkMEzOyZmNBCyggmd1pWajwPNa6KlJJg0ZvFxo2AT50H6nggxLuvo1fQt9uR-CSXX5wlPf0kh6K0Yh5qRrib2v2HRyEuxGk0AM47LycQloxiRtUu4kMMLVvuoPcZmvQXJZ4Mel33DNRHvo6AfnVhzkkBa-NFUp-U0W9UqoyI6tkzrR0iVQ17og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بازیکنای برزیل یه دروازه خالی گل میکنن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/94589" target="_blank">📅 05:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94588">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بریم برا نیمه دوم بازی
🔥</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94588" target="_blank">📅 05:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94587">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udubfJ3xmfQvazrrbEZtlROj_eF5oOARuh9awWm-cmS5IdU_1NtaD5H2LJ2CzGCvuK5BXKXnPbh2aMvxjlknnDZOVsqTtkZKrBLvIN9szK5sNuKI67ABRmP9vAWc1hJIUZQ3esXxlm-gauVXXUh5-BboU-cFPOq93FzTCMDqL8mSZEETZPkBQuecY0XBrr3uB9AUP9MJkRoiBqvRLKGWZ9wYNz4LZoBU-dIydMg_vjYCJLLUei-S1SNCR8-ZhytuXBrn2SdmvVu9GOECFVcrNeCRjZYnF0FlyjO3CbiwmFfTPHMUSPlpPEUG0r8k8Eesd8k439fPxbNKX_srBpVqjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
آمار فاجعه‌آمیز برای رافینیا این فصل :
🔺
پنجمین مصدومیت رافینیا در این فصل
🔺
رافینیا به مدت ۱۱۲ روز در این فصل به دلیل مصدومیت در بارسلونا و تیم ملی حضور نداشت.
🔺
رافینیا به دلیل مصدومیت ۲۴ بازی این فصل رو از دست داد.
🔺
در مهم‌ترین مرحله این فصل در بارسلونا مصدوم بود و در جام‌جهانی هم مصدوم شده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/94587" target="_blank">📅 05:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94586">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw3GsjlNf6xAGJydr0FUl28kmS3rpeVJSXRQcRpOW4ZrICyAbVxylE9u2RtBD5wfZ-dzxxBOJU7bnFoBgQWUGhw6WcioFyEwCJoo4U1qYFyxY4nADqLGSOntJlorvP-0cdAidrob2NxhsI-yhpZF7iwvMz2P8k4L-b-khYfeLIwAA8L8MM-ZiLTtp3K45ZtyIJXb4DP47_CBgTzmUhSKVG5BIDezNhRzqwPcP8StRDF6Ry6zcxD9iNhaClezapdPEKVcjM1unjgz_-s1hrtMBg5QxhkHhr7PZLOr72ApbCuc3MAKyOJhO_AZg7wUTjnEqKmL9frMFc7HhPkUsdSqnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
وینیسیوس جونیور در 6 بازی حضور در جام‌جهانی 6 مشارکت در گلزنی ثبت کرده
🔥
🔥
⚽️
3 گل
👟
3 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/94586" target="_blank">📅 05:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94585">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9330025fac.mp4?token=kNhyEsEs3OGjavyskOLRV8OAh08qQ1wZkeMUbKdvZiVwdJGPUnAUAFRV6hl69zajsig2GYMQN0wY2HA3MOatyvursJTphgAOa5lxfp0P7qafjSEEcB3C3k6nkcM6pLZPg6KOcfJycRbUnPx-gc6I6Vbu5xd38ICESdEpUa3DG_T_4rYexhi4EpdmdrYG0jeSCDogAOVGLYhwnTktLeU9kC6LAm2MScCGx-huF1g0MJjQRJSOsEH9FuZAedf5IZuSesyUbLJu_yIq5x-YpEYgbQaR1x0rIC4TOeDqBXlIUYDqTSJddVPnW5gRxr0cC4VoRLJ_GKIo2xRm5CF4pYMBRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9330025fac.mp4?token=kNhyEsEs3OGjavyskOLRV8OAh08qQ1wZkeMUbKdvZiVwdJGPUnAUAFRV6hl69zajsig2GYMQN0wY2HA3MOatyvursJTphgAOa5lxfp0P7qafjSEEcB3C3k6nkcM6pLZPg6KOcfJycRbUnPx-gc6I6Vbu5xd38ICESdEpUa3DG_T_4rYexhi4EpdmdrYG0jeSCDogAOVGLYhwnTktLeU9kC6LAm2MScCGx-huF1g0MJjQRJSOsEH9FuZAedf5IZuSesyUbLJu_yIq5x-YpEYgbQaR1x0rIC4TOeDqBXlIUYDqTSJddVPnW5gRxr0cC4VoRLJ_GKIo2xRm5CF4pYMBRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🔥
گللللل وینیسیوس به هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/94585" target="_blank">📅 04:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94584">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وینیسیوس</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94584" target="_blank">📅 04:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94583">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سومیییییی</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94583" target="_blank">📅 04:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94582">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a4caa6b9.mp4?token=T6x-hIyKMhgxboyVNNprh65VfA-EdmK4TjFN9uz3YuBv8Wo1Xh5Od1P-cHn_S6Qd12eihcKmXt8QJf_hk1g0RjRyk39hXPmdeIQ7bJK9btrT9wLz1mp6KrhorL01vZfHdBpJxR5X6e19DFjUX_wvH_e2eShw6dylvlLFT-qoCTi4LIOdzlffgzN4DJNe8HWutbo-_gwRJDR9d1OLXuUpgjRcCgi2GekcYMdyc8prNFT_i3aeV8-Ymvgzo8u77n6622nSDdCP2ZCPiZQS71Xpj7mWXILF37f1_Ehi0mCwbHEgOPYzmwZySUXpnZQRtl1-CVUBjix0uB_T5IdU5UWxaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a4caa6b9.mp4?token=T6x-hIyKMhgxboyVNNprh65VfA-EdmK4TjFN9uz3YuBv8Wo1Xh5Od1P-cHn_S6Qd12eihcKmXt8QJf_hk1g0RjRyk39hXPmdeIQ7bJK9btrT9wLz1mp6KrhorL01vZfHdBpJxR5X6e19DFjUX_wvH_e2eShw6dylvlLFT-qoCTi4LIOdzlffgzN4DJNe8HWutbo-_gwRJDR9d1OLXuUpgjRcCgi2GekcYMdyc8prNFT_i3aeV8-Ymvgzo8u77n6622nSDdCP2ZCPiZQS71Xpj7mWXILF37f1_Ehi0mCwbHEgOPYzmwZySUXpnZQRtl1-CVUBjix0uB_T5IdU5UWxaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
دبل کونیا مقابل هائیتی
شادی بعد از گلش فقط
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94582" target="_blank">📅 04:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94581">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رافینیا بگا رفت و تعویض شد</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/94581" target="_blank">📅 04:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94580">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اوه اوه</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94580" target="_blank">📅 04:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94579">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">عجب پاس گلی داد وینی</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/94579" target="_blank">📅 04:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94578">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دبل کرد، کونیااااااا</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/94578" target="_blank">📅 04:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94577">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دبل کرد، کونیااااااا</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/94577" target="_blank">📅 04:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94576">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دومییییی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94576" target="_blank">📅 04:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94575">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گللللللل</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94575" target="_blank">📅 04:38 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
