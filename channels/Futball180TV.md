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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 10:41:44</div>
<hr>

<div class="tg-post" id="msg-105323">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XutpHViR1j6Gqj4cT16QOS5xky8PUxzuC-iR4Y3oQ8VvBbwkleSyWopCyAQdakVxRRrgOmxDsp2yk-tH_Yty9HnsEUqlwLNn6Yv2-xIR5oraP_i9-B4RHPm9Z9X-S6SikOQoAOHCnzQRHoMQAA3DKa8zhufYmNaxkrnl6GVT6jKqnH44iQQQ27Wm8rxLCgdMND3aG9ep7ztuuw_dpay1kyl04V_ex2Np57i5M83_Ritq_OeP5AjbMzutdfxBr6JQUu1FsJQyUcOCvImuWGogjdPspICkNmImdt9CMV3xFMUyqNPjh0FGHYBS8rSfgiJYr6Ij6Q6zCAvsPDo87tV2Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✅
🇮🇷
🇮🇷
مقایسه افتخارات رسمی سرخابی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 729 · <a href="https://t.me/Futball180TV/105323" target="_blank">📅 10:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105322">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3bce317a.mp4?token=r5wTg7pS8otEohByJVldztFm6IFGwlKqQszoT50ps2JW7WR5rPfo1VdGCKn-iDJcUGGVzb6183jy639gRRpnwCLeOY1_1YIcg9sq28bDA-F58zpsRFTyoXNKPSbZXCPbKPvW7T2bWmJwwbrbu5fmbwN1AFK9yIse_YRopaWK0SOBfeup1iK359Kb8z4kKYidJsGf2-FGQ8N8McSiqRu7eFdiFbWH253B7OsiY6gCjNZ183zfh0euIRtn-FtuyzzaC6nAu3VmWIzivvfHCRoY1O2bPxIR8MGWsIoRL2ez98VCYm1j68lUbN8_BA3y4J0yLNreNAPqAx4A0C57_Kec1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3bce317a.mp4?token=r5wTg7pS8otEohByJVldztFm6IFGwlKqQszoT50ps2JW7WR5rPfo1VdGCKn-iDJcUGGVzb6183jy639gRRpnwCLeOY1_1YIcg9sq28bDA-F58zpsRFTyoXNKPSbZXCPbKPvW7T2bWmJwwbrbu5fmbwN1AFK9yIse_YRopaWK0SOBfeup1iK359Kb8z4kKYidJsGf2-FGQ8N8McSiqRu7eFdiFbWH253B7OsiY6gCjNZ183zfh0euIRtn-FtuyzzaC6nAu3VmWIzivvfHCRoY1O2bPxIR8MGWsIoRL2ez98VCYm1j68lUbN8_BA3y4J0yLNreNAPqAx4A0C57_Kec1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😂
🇮🇷
محمد نوری سرمربی صنعت‌نفت در کنفرانس خبری دیروز تیمش بازهم شاهکار خلق کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/Futball180TV/105322" target="_blank">📅 10:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105321">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
🇮🇷
🇮🇷
سه‌دقیقه فوق‌العاده شنیدنی و دیدنی با نوید استادرحیمی از دربی‌های جنجالی و خاطره‌انگیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/Futball180TV/105321" target="_blank">📅 09:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105320">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca6813881.mp4?token=K4ZLEuaOLBDf7qTom71NNz8G_xlPmziDme87LvuCm7WRlyRqfehjKNgUrfJryMWAAgh4ufhhpRQlX2kNB_uK_aIf_CIpbJ_ekjynmKW_e9tEW21LjFLYjhgR-KRHkhsXOL1XljQr6yetaRPD9znaZMSllzJrQml4CAobpNKRAUleIZNk3tGO_Ssl6jqNwWJ5tde_UmAPZe2jeyVsgt-A1luvFAdAIiqUfPE-XR534aGAtnRWl1ZZT6LXIajW-d5AITFYojZik_OU4-syVvhUndWGuisRYptXlfOWudw00hqu4nKUfbGlO5MUdRus_4nNRKu6IW0X5-LplWJ4A_X9Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca6813881.mp4?token=K4ZLEuaOLBDf7qTom71NNz8G_xlPmziDme87LvuCm7WRlyRqfehjKNgUrfJryMWAAgh4ufhhpRQlX2kNB_uK_aIf_CIpbJ_ekjynmKW_e9tEW21LjFLYjhgR-KRHkhsXOL1XljQr6yetaRPD9znaZMSllzJrQml4CAobpNKRAUleIZNk3tGO_Ssl6jqNwWJ5tde_UmAPZe2jeyVsgt-A1luvFAdAIiqUfPE-XR534aGAtnRWl1ZZT6LXIajW-d5AITFYojZik_OU4-syVvhUndWGuisRYptXlfOWudw00hqu4nKUfbGlO5MUdRus_4nNRKu6IW0X5-LplWJ4A_X9Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
🇮🇷
فقط اونجایی که صداسیما زیر نویس میکرد دیگه نیاین ظرفیت تکمیله
🥲
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/Futball180TV/105320" target="_blank">📅 09:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105319">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
🇮🇷
یه ایرانی رفتی از دربی کشور زیمباوه برامون ویدیو گرفته؛ به دربی سرخابی‌های خودمون تشبیه‌ش کرده
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/Futball180TV/105319" target="_blank">📅 09:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105318">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی…</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/Futball180TV/105318" target="_blank">📅 08:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105317">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebf67c803.mp4?token=XT3P2MrCyTNH7wKPceh9A3BydlO53RyQ-A5ElGO6E0E0Cazmf1v8w8r00Ql_KQl466V6rPVF30nWwR71N6Wlrq50h_I2p-bC0qVxQ-rCN0Ikm5OLVZzAX7aMfHz1dO414afENXLVZXfcd3ROpX3rvbvtdP_ONzAqQ8ewMmFmVlc_hkZVjaDVR7uY4zaGh3pZ3U4ODXX9fcLqkJoYS1erLUcipOuQSDTP25waDuAWTSrvSY_ikDr48sugEBof5zlDOgwjQzybs2qCMBZA0WZ3cI5_VyM6J1kQo3R3bjH63uq-39mZLPKZJVIqr3Pvn-E5v4eAPcQ7cQtCoETp8fGHlTgoOyRd0BlYEU7sLfJXHtqD8y4Tzfyey51MR3iwsf3JmrX4Mk_dJLVN9Ezl_l-2ZS7J7fKpOMcSU3tbhjJdIyiHPNfTpa13zZ9uXCSlpT30XwBv2a2XLk3l7ymUqM8i6cdAasYmouHuPEHUmnhePKCrZPfm3vlHDIZYwSYhgfwkxv4pjycXzRQtL1R4i6ZR3IjpQ-OFArt_r7EdjJNXQPtjIyjm8LDdn31Xfu878F2whcrph-XTtIYkUt_rUYKr6hSm7a42n_Nq9LrN_2uLOSYL8m-YwX1_5Rrx6Kaker3OsC00rNLP0DrARP4i_HTWinuJaeUxSokO3_uTpOYbrIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebf67c803.mp4?token=XT3P2MrCyTNH7wKPceh9A3BydlO53RyQ-A5ElGO6E0E0Cazmf1v8w8r00Ql_KQl466V6rPVF30nWwR71N6Wlrq50h_I2p-bC0qVxQ-rCN0Ikm5OLVZzAX7aMfHz1dO414afENXLVZXfcd3ROpX3rvbvtdP_ONzAqQ8ewMmFmVlc_hkZVjaDVR7uY4zaGh3pZ3U4ODXX9fcLqkJoYS1erLUcipOuQSDTP25waDuAWTSrvSY_ikDr48sugEBof5zlDOgwjQzybs2qCMBZA0WZ3cI5_VyM6J1kQo3R3bjH63uq-39mZLPKZJVIqr3Pvn-E5v4eAPcQ7cQtCoETp8fGHlTgoOyRd0BlYEU7sLfJXHtqD8y4Tzfyey51MR3iwsf3JmrX4Mk_dJLVN9Ezl_l-2ZS7J7fKpOMcSU3tbhjJdIyiHPNfTpa13zZ9uXCSlpT30XwBv2a2XLk3l7ymUqM8i6cdAasYmouHuPEHUmnhePKCrZPfm3vlHDIZYwSYhgfwkxv4pjycXzRQtL1R4i6ZR3IjpQ-OFArt_r7EdjJNXQPtjIyjm8LDdn31Xfu878F2whcrph-XTtIYkUt_rUYKr6hSm7a42n_Nq9LrN_2uLOSYL8m-YwX1_5Rrx6Kaker3OsC00rNLP0DrARP4i_HTWinuJaeUxSokO3_uTpOYbrIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
روایت فرشید باقری از درگیری عجیب سیدجلال و مهدی رحمتی در دربی ۸۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105317" target="_blank">📅 08:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105314">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105314" target="_blank">📅 01:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105313">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbwzC9XFp4k2mSfu9-w8192ZG2T-B830MTFrmX541-eYzVQFsnp1YVgyPDtHTbbgJ2rp5NsjuFRuhHIEi0_fA3aEkLAK4vpqF2qN9Hun6WUq1b2UpGMTx_gdes0vNYhzV8-LDoBQaGMvNY1b8_HEenENewFWFLBlDbiHsdKUjOtR3cAtcijNoH4L89VR32GoB9hh_riP7P8RjbRqKEz23V1gyOXBwpUGXvjwpdOMAmC5FCzjjKW5BZ7CcP7g4SWPVv_IgpbEBq-AbRvtjtPYhQnmaGTG20pMi7o3U5GNyQiz8BvRET21XLz07SCJ3Q8yeZ16a-RGSbJNNT6ZjHAc5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105313" target="_blank">📅 01:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105312">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105312" target="_blank">📅 01:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105311">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⭕️
⭕️
با توجه به نزدیکی به دربی پایتخت و بازدهی فوق‌العاده تبلیغات تا پایان هفته، اگر تمایل به همکاری و انجام تبلیغات مدنظر خود داشته باشید، با ×تخفیف ویژه× در مجموعه تبلیغاتی تیوا با بیش از ۱۵ کانال مختلف ورزشی و غیر ورزشی در خدمت شما عزیزان هستیم   برای هماهنگی…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105311" target="_blank">📅 01:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105310">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
⚠️
یک فرد ناشناس در مشهد با خودرو به تجمعات جانفدایان ولایت حمله کرده و تعدادی کشته شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105310" target="_blank">📅 01:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105309">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f42b196ef1.mp4?token=czWeYcGuHu_CPc3U8Z2hf7AS6tUl4coJlKUvq20UF_hCEIVeLjUwyBZXFjv-XpER2HLm6GV1Lx-IuW80hs08VI9DBNJ8KZF_EEZGBSmIbA230Swx_Gg8_niybH8LmPV9fCgvYgKWOR7Z2om4nz2n3gztq43dWCMUSzPoZheJ2SSM8mIi28H1RTBPYec2H3rMo8cFZAAX45BgrGaiCYdMDmt-BcTL5LQzBLM48iEJXeJeQiEFukV3JdcwONpPSicV44i-llbx8CNhjTvC3qn4eobSdedOuEG1XMlu12SCnH9bDMfGkt-c2D_GUDYJ1wVlqET1_NnpHvCb0EWmvQiRjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f42b196ef1.mp4?token=czWeYcGuHu_CPc3U8Z2hf7AS6tUl4coJlKUvq20UF_hCEIVeLjUwyBZXFjv-XpER2HLm6GV1Lx-IuW80hs08VI9DBNJ8KZF_EEZGBSmIbA230Swx_Gg8_niybH8LmPV9fCgvYgKWOR7Z2om4nz2n3gztq43dWCMUSzPoZheJ2SSM8mIi28H1RTBPYec2H3rMo8cFZAAX45BgrGaiCYdMDmt-BcTL5LQzBLM48iEJXeJeQiEFukV3JdcwONpPSicV44i-llbx8CNhjTvC3qn4eobSdedOuEG1XMlu12SCnH9bDMfGkt-c2D_GUDYJ1wVlqET1_NnpHvCb0EWmvQiRjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
تصاویر دوربین مداربسته از حملات پیاپی به نزدیکی یک مراسم عروسی سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/105309" target="_blank">📅 00:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105308">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAMjrewbGufGPB0qyWzC6k4uBblf56I8Csk3nVMXofGVx0aX_O58jby84L16o4yVLZAdooo4R_N1u8xbp5J4xq0GWqejV37uIyzChxA7Tyg8KoU-xPFxXTve5rvAfgGyJaWz8fEoDh-IkbRYBSjLVUHcA61gx3j7Iw-HawW4b0LybL0JMWEieCSqpguL4PY8NErcJTWkSWDMEwu9Pra_Nmcmn6mw4c2bUhfdIb7hvC6nQfZSS8hZoKT8mqzUDuBabM9JVgmo3EaSSdHbh76Ld4kNz6A4HRAM-oulQIBJYmmQbD2V7C5V0XfU_iTQ9oCKLpUmYQlT0yMtAMCcoGNquA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/105308" target="_blank">📅 00:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105307">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105307" target="_blank">📅 00:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105306">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180
#فوووووری
❌
شورای تامین استان اصفهان در صورت تشدید حملات و درگیری‌ها تا ساعات آینده صبح فردا جلسه‌فوری تشکیل خواهد داد و در صورت ملتهب بودن شرایط قرار است بازی دربی را بدون تماشاگر اعلام کنند. هرچند تا این لحظه سطح درگیری‌ها به نواحی اطراف استان اصفهان نرسیده و این اتفاق تقریبا بعید است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/105306" target="_blank">📅 00:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105305">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cf9805271.mp4?token=bXOnqYBsbgI6LIJEQ4ruK_YP4NHvhC5Vv-KExsrFfbmgEKyulWonUrN89Q8kuKeetLkKfLT2_KdmSlXui2JFNdRVFSMmASmf07FUBqYMFdkNOV_2lVQBg-1zZBcvUlBGXn9KWjzuL-GLUWul8_CdobfaXhFEccfEFWJksPrHCmwj7pZFmGYb7pTFqmAH3gpugUMEzzmSclnZvX9jaoOPl7VA3hZhvRQwbZ1RFKsH0gylRloBRMLwWlX356eKKCrqxDGLjJkNFrtK2SqkUKmfEYaycE8C49Phdoqv2fQySRZWQ2ElvQq9Z88W6oX-Qtq7r6_eqfdB7rtZP0vw1RrE7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cf9805271.mp4?token=bXOnqYBsbgI6LIJEQ4ruK_YP4NHvhC5Vv-KExsrFfbmgEKyulWonUrN89Q8kuKeetLkKfLT2_KdmSlXui2JFNdRVFSMmASmf07FUBqYMFdkNOV_2lVQBg-1zZBcvUlBGXn9KWjzuL-GLUWul8_CdobfaXhFEccfEFWJksPrHCmwj7pZFmGYb7pTFqmAH3gpugUMEzzmSclnZvX9jaoOPl7VA3hZhvRQwbZ1RFKsH0gylRloBRMLwWlX356eKKCrqxDGLjJkNFrtK2SqkUKmfEYaycE8C49Phdoqv2fQySRZWQ2ElvQq9Z88W6oX-Qtq7r6_eqfdB7rtZP0vw1RrE7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/105305" target="_blank">📅 00:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105304">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcaf59f19.mp4?token=fG7zsvtibOTJ6Xgf7J-cZTtlXPcxgBmI7vZfpk1ll3HbyU4eGck1FxBt3yjgsZ6kfah8Ikd639Nxx5iOIlY7ZFj1_OZpzID6_uUPs2hhVNl1KpDSffA9iZnOEVoOUMgBjuxzkMfUKIVE1IbscdZ2fAnzUi3JSEX21FK5fQ-7vITsqigYoPdE_THtpq0bnP17LSZ_jNfbvx7YVWg6QSIQASCEGMVgzuSe2VeK7OWPLxzYtdJoemTp26IOqdUm5t6dEv8mz6m5eWFFKX3ntEVB-LhY6PO4kjj4lqLTwBPsgMTmhmyPZalCfQonuMf7Ryj4XgEnSsrvfzLVDz5tqTVdbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcaf59f19.mp4?token=fG7zsvtibOTJ6Xgf7J-cZTtlXPcxgBmI7vZfpk1ll3HbyU4eGck1FxBt3yjgsZ6kfah8Ikd639Nxx5iOIlY7ZFj1_OZpzID6_uUPs2hhVNl1KpDSffA9iZnOEVoOUMgBjuxzkMfUKIVE1IbscdZ2fAnzUi3JSEX21FK5fQ-7vITsqigYoPdE_THtpq0bnP17LSZ_jNfbvx7YVWg6QSIQASCEGMVgzuSe2VeK7OWPLxzYtdJoemTp26IOqdUm5t6dEv8mz6m5eWFFKX3ntEVB-LhY6PO4kjj4lqLTwBPsgMTmhmyPZalCfQonuMf7Ryj4XgEnSsrvfzLVDz5tqTVdbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/105304" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105303">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6jNj0153gp1TpkvWA4GqpI1Wz6cLmk7p8o6cczuwMUUzWKvt3Yg9j9cnKyNxKvJulFzXEnL1vAktJ4j3JhIMsV9jUA-SrZILZAH0epoMs5Yq2S_Eq8Uwo-BePXn25-DmQRNVa-jqdIIpFK2cc4Ut8XgKALfq44Fuw7GNYuAxDKcTNiTisVPd9SItpt00gqTm0hjdjjEi7NlEBIzZVnVTnoN06hiZn6lBluqis7DCdi2svnSpAb4dfw94zax5tBwdr2R3Oe56sBbMiRKAl-RrZDVbBazMLG3MtSOo_CwozkXvWUvjUyoF_Hh1zQxl9SgtVVjMKsWUiNoi_JIkA-RoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسمی؛ اندیایه با قراردادی پنج ساله به ارزش 65 میلیون پوند از اورتون به سیتی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/105303" target="_blank">📅 23:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105302">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
گزارشات فعالیت شدید پدافندی در شرق تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/105302" target="_blank">📅 23:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105301">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👍
🇮🇷
بانوان جذاب ملوانی در بازی با پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/105301" target="_blank">📅 23:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105300">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f706e532c0.mp4?token=h236NRUo6NE9asCMoWNXjv6GrxnY-yg5_RRd6Ml9W95xMk98jjQWRo5h9P2j0PRCkExQapjcW18OKKAZY336Ren0I9Fk07UjKkjWjDnjaj9re2KV8idvMl4Gn31xfnmUf7v2ZwSYSgs3UUqopY10x6tZU9JgBsZn9ULy6fRV7iYpWGUygP0HoqkIuKllTgoIe4it118DlTbbWv1ZxMEt-waQEsC-1OaDaBIXkwNSbZmZl_HMqgz3JX4md2dqNJ3bgjxQLphu2hm00PVMGNmzwk8kpw_bvvsde9mwhwfsczfaYdM69Prhsh9tPd84c2nz_WNEHcIR5eRTjPB2-YMT9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f706e532c0.mp4?token=h236NRUo6NE9asCMoWNXjv6GrxnY-yg5_RRd6Ml9W95xMk98jjQWRo5h9P2j0PRCkExQapjcW18OKKAZY336Ren0I9Fk07UjKkjWjDnjaj9re2KV8idvMl4Gn31xfnmUf7v2ZwSYSgs3UUqopY10x6tZU9JgBsZn9ULy6fRV7iYpWGUygP0HoqkIuKllTgoIe4it118DlTbbWv1ZxMEt-waQEsC-1OaDaBIXkwNSbZmZl_HMqgz3JX4md2dqNJ3bgjxQLphu2hm00PVMGNmzwk8kpw_bvvsde9mwhwfsczfaYdM69Prhsh9tPd84c2nz_WNEHcIR5eRTjPB2-YMT9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/105300" target="_blank">📅 22:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105299">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f17ff9c0b.mp4?token=aymtm9CrGXUHizv2_OTEfwLKhOU4pEDZacdsT5K7o8dMiqMW1AdM1yq_s1VuIuyH4hfWXlr--O20wRvVcMq0a67C4ugpIq8mz4Qx2K-LOhn0Ddef8tfO_R3W047BE-UP3GCZjWXvu-yth6jwNau4gYJXgEb5QhtJCO3uJZimet2yhIhhWGso0Km9wowbk7iodMAoAiNMTI94uOvi_ZBa4wiy00RTtZPaL6L0zPxzVlE6j_eOUqk_35VCeMKsh2vHUcXn33Bz_JYXMV337s7rVi4Q9aEf21VtCZ6n9w6Iww56QNZ3Nt32Z7sKw_F2_8n5ixypEfGCjgapHTIlBf1aKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f17ff9c0b.mp4?token=aymtm9CrGXUHizv2_OTEfwLKhOU4pEDZacdsT5K7o8dMiqMW1AdM1yq_s1VuIuyH4hfWXlr--O20wRvVcMq0a67C4ugpIq8mz4Qx2K-LOhn0Ddef8tfO_R3W047BE-UP3GCZjWXvu-yth6jwNau4gYJXgEb5QhtJCO3uJZimet2yhIhhWGso0Km9wowbk7iodMAoAiNMTI94uOvi_ZBa4wiy00RTtZPaL6L0zPxzVlE6j_eOUqk_35VCeMKsh2vHUcXn33Bz_JYXMV337s7rVi4Q9aEf21VtCZ6n9w6Iww56QNZ3Nt32Z7sKw_F2_8n5ixypEfGCjgapHTIlBf1aKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇮🇷
🇮🇷
همچنان از بانوان پرشور اهوازی در حاشیه بازی استقلال و فولاد خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/105299" target="_blank">📅 22:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105298">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=frZ5gOD8rFSi2J5YMgrh7zoxPDjwyHvtWqICIVH0lAHoEqnSbtvJHll9S_4wIA-8dcfkoEq6oaArSpnTXq-TNgGD61H_FUo4A-u2hPKn7yLgkKwdRlrah5z5AdKjrfIFpsKJ9QHAsZOnh-rMby1bLbsRyzXjTm5k84u5ATSV6x0Wcc3gIH0Cj2a9VmqTd-vFESKEmU72XJyuCJSWUmVNju7eToCQNTi42YCgGYeDk8nteRFYrOOz-AhJWZTkfDTKgxEcMNKEaCEs57Nb-b9D34B7D4kYygLFKLL6pnjZ0xbRy-ycpzNcncB1-_pwy21K9oAiFlHVh1jFc2M-HFtU6izFRmKNztIolc52bXUFxDoyxZ7kMECvZAJl5341UPWlK9YMkCgl63VX61kyslSqB433fXz2KrOO08UJ4Ux6EqDUhHlk0MsI_kyhP_jvMTSp7FbZjvleQ_DLSZDXxXANa6uzZpgGxag3GqftSKTf0z8eKW-xWCEXnyAerfwoGn11AC1eS_hOw4RmfnDYtiMeM9-tPmjJX3NP57QlGpZwo9tF_2fV23pEb9FRjF-9f-1-gWJQ_UrqcvIM6hFQibpLdyXqo3t7TtG7Fk2OXL6UMwAlouL9smwP-EOnw1Cz-5lthjhkduB1BgnsQnPxxsi03st6I8n4J4WRYnwwO9Y8A0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=frZ5gOD8rFSi2J5YMgrh7zoxPDjwyHvtWqICIVH0lAHoEqnSbtvJHll9S_4wIA-8dcfkoEq6oaArSpnTXq-TNgGD61H_FUo4A-u2hPKn7yLgkKwdRlrah5z5AdKjrfIFpsKJ9QHAsZOnh-rMby1bLbsRyzXjTm5k84u5ATSV6x0Wcc3gIH0Cj2a9VmqTd-vFESKEmU72XJyuCJSWUmVNju7eToCQNTi42YCgGYeDk8nteRFYrOOz-AhJWZTkfDTKgxEcMNKEaCEs57Nb-b9D34B7D4kYygLFKLL6pnjZ0xbRy-ycpzNcncB1-_pwy21K9oAiFlHVh1jFc2M-HFtU6izFRmKNztIolc52bXUFxDoyxZ7kMECvZAJl5341UPWlK9YMkCgl63VX61kyslSqB433fXz2KrOO08UJ4Ux6EqDUhHlk0MsI_kyhP_jvMTSp7FbZjvleQ_DLSZDXxXANa6uzZpgGxag3GqftSKTf0z8eKW-xWCEXnyAerfwoGn11AC1eS_hOw4RmfnDYtiMeM9-tPmjJX3NP57QlGpZwo9tF_2fV23pEb9FRjF-9f-1-gWJQ_UrqcvIM6hFQibpLdyXqo3t7TtG7Fk2OXL6UMwAlouL9smwP-EOnw1Cz-5lthjhkduB1BgnsQnPxxsi03st6I8n4J4WRYnwwO9Y8A0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/105298" target="_blank">📅 22:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105297">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1acbc66f12.mp4?token=nVr9qQPitRX_pH1LS1d3_7t8e6oxRP36GGNMyZLoqlVyedIxkhVK5QNRp1LqOVJ-mJ4Lj0WDdCclBskZ-uxn4EksoGmowSr9ObubZ6YeOSVImoSgB_1O5e9suOU68t2pYkQC0leqwfyuA9zobT70OfvpSkethFmMh9uID-2kO69IPRdS0gPjw7xuOTMSqtFvvqSTxGuS2-lSfjl-vh0-LEcodlpgxEdHmdtbnITB4V4X7S2dOFglESRL-2nLm6VgAYX1N26w_hiPq-OsHvtB--7sW9wkPXJBuzpbj2ZKbz61QX4cLJOcvNnR9LAlc11LCq91hFNjqoiw8nubKqCrzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1acbc66f12.mp4?token=nVr9qQPitRX_pH1LS1d3_7t8e6oxRP36GGNMyZLoqlVyedIxkhVK5QNRp1LqOVJ-mJ4Lj0WDdCclBskZ-uxn4EksoGmowSr9ObubZ6YeOSVImoSgB_1O5e9suOU68t2pYkQC0leqwfyuA9zobT70OfvpSkethFmMh9uID-2kO69IPRdS0gPjw7xuOTMSqtFvvqSTxGuS2-lSfjl-vh0-LEcodlpgxEdHmdtbnITB4V4X7S2dOFglESRL-2nLm6VgAYX1N26w_hiPq-OsHvtB--7sW9wkPXJBuzpbj2ZKbz61QX4cLJOcvNnR9LAlc11LCq91hFNjqoiw8nubKqCrzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
تناقض عجیب در صحبت‌های پیام‌صادقیان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/105297" target="_blank">📅 22:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105296">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
آغاز حملات موشکی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/105296" target="_blank">📅 21:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105295">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2a82a31c.mp4?token=dgxLNUANp-z0UHo4KHxGPlKK92U_C1B11fqj3alCXrcHqI4GbJPI1w4_USwuEdShGrQKHlXBv3bXfL9G5oKyV26yQ20SsZI3w6nskuqgaad28hnulUC0ovBFl1mJFHEw2gK1gXXnMwCcXb2dBkvPPtj5MXvevUp2SoOLll1EuVWK8d0k7PH2uLFOANN3JxokdGEU2yV9tG4khY4fmwpdNmbIZnhIM3I69feyHSWNbtm7Wk5aN_rgt8NL3rOGaCIbyB1WvvbUnQLOnEc006ushDQwC3XAQq1jiiMYfvIZ-LQJTrMKTGu8O_JFLLaCmPTOzlxbpXGnb_BIPMN-E3c7rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2a82a31c.mp4?token=dgxLNUANp-z0UHo4KHxGPlKK92U_C1B11fqj3alCXrcHqI4GbJPI1w4_USwuEdShGrQKHlXBv3bXfL9G5oKyV26yQ20SsZI3w6nskuqgaad28hnulUC0ovBFl1mJFHEw2gK1gXXnMwCcXb2dBkvPPtj5MXvevUp2SoOLll1EuVWK8d0k7PH2uLFOANN3JxokdGEU2yV9tG4khY4fmwpdNmbIZnhIM3I69feyHSWNbtm7Wk5aN_rgt8NL3rOGaCIbyB1WvvbUnQLOnEc006ushDQwC3XAQq1jiiMYfvIZ-LQJTrMKTGu8O_JFLLaCmPTOzlxbpXGnb_BIPMN-E3c7rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
افشاگری فرشید باقری بازیکن اسبق استقلال: پاتوسی سر پنالتی چیپ دربی با فرشید اسماعیلی درگیر شد و ما جداشون کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/105295" target="_blank">📅 21:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105294">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8d66f699.mp4?token=AR72EBba5VRLdhMsy015AcZhjDFTUd_Pl2f_6MBR2-OJPWm7ktRPZEfPkcUhVqcfnB5nbk224FEXqNIibabyzf0F3bJtdI7F09rLE0i00DgkReEnyuSBAEt9JnlY4DF3gVY2D9EMgZqP-ma-bGAR5Fk9ExWefF1oBgU46a-2DuuU1FU70rSqsx3KU55NXnxDgNDE7SgfoVhF_f09jzhHAltGk5HEyAH1bpko9u6kPZWwas-wkSPnNnEV9LvENr-CQJbtKK-Q0nfUCifLSbTGY6BDV4SBgrhPOdnSa4k8DPOlT7wRKcaM3Wj-Tri2_NNFgMpM7OpziXP_cO9CGiDDQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8d66f699.mp4?token=AR72EBba5VRLdhMsy015AcZhjDFTUd_Pl2f_6MBR2-OJPWm7ktRPZEfPkcUhVqcfnB5nbk224FEXqNIibabyzf0F3bJtdI7F09rLE0i00DgkReEnyuSBAEt9JnlY4DF3gVY2D9EMgZqP-ma-bGAR5Fk9ExWefF1oBgU46a-2DuuU1FU70rSqsx3KU55NXnxDgNDE7SgfoVhF_f09jzhHAltGk5HEyAH1bpko9u6kPZWwas-wkSPnNnEV9LvENr-CQJbtKK-Q0nfUCifLSbTGY6BDV4SBgrhPOdnSa4k8DPOlT7wRKcaM3Wj-Tri2_NNFgMpM7OpziXP_cO9CGiDDQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇮🇷
💥
خانم‌مریم‌یکتایی هستن مجری تلویزیون جم‌اسپورت و گلر جدید تیم‌بانوان باشگاه استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/105294" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105293">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFdSsDuEIWUGDFAE7bwjbAqvtiGACCNCiJQP2aZ7sK62VwGnFm9mQEQBFUEaTFG4vdZ8fnhvvNyyT1lz3sQmKPY_pL2rN3HH0X2FkSfxRVHCPLLIi9V1_SXWCDo1Wkq-8MzjloisE5DZOHCettJU1r2lJ7RlAC8YuKnonE9eXC6OsP-Tc7i8z6P8fM1c4TH_cV0vJsOrFiRNCFC3rGA0TFvP7MecPAdSab81feb4qJETO78Kq34eDcShWfUi_LMyQDzGI-mJCubiedDrOjaqcIT7guG7Doku_NTmsbTWTgY8t634BU9Efn67se8BdVeO3YITobEm0z9VxTmMjLLT9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/105293" target="_blank">📅 21:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105292">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/649b5fb52a.mp4?token=TtrAgbP8yAQZCzcpf43asniCHz2lfeb12hMcbc2i8JZfTfM-SySllRlO92gqjYTdQ9uTutgjIDGVM0828RS0o33ox9JvPcHR2as7star9w0X3pkxYl-85eCWZwSCmSIAL-mS6XYXATs8QYtVuBMkpAS--_CSouoc19iRjdhfGZ-Wa3yiKwIeS4gSBn2e0amg3To3Ia6Ca4zWPeAuubb87Ii_8BX8RucJDTC---9TzypR7LrbhTfh-w3TufQKc1nlT6iOuLdv7O7pEzbjpZnFMlOlJvE91z7ZXCTmv3YaYlBQanlot6YqpuvhEsVJJbVmAjSbcqrbJdXY53p0nBxLOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/649b5fb52a.mp4?token=TtrAgbP8yAQZCzcpf43asniCHz2lfeb12hMcbc2i8JZfTfM-SySllRlO92gqjYTdQ9uTutgjIDGVM0828RS0o33ox9JvPcHR2as7star9w0X3pkxYl-85eCWZwSCmSIAL-mS6XYXATs8QYtVuBMkpAS--_CSouoc19iRjdhfGZ-Wa3yiKwIeS4gSBn2e0amg3To3Ia6Ca4zWPeAuubb87Ii_8BX8RucJDTC---9TzypR7LrbhTfh-w3TufQKc1nlT6iOuLdv7O7pEzbjpZnFMlOlJvE91z7ZXCTmv3YaYlBQanlot6YqpuvhEsVJJbVmAjSbcqrbJdXY53p0nBxLOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🍷
تلاش خداداد عزیزی‌ برای یاد دادن اصطلاحات پیک زدن در زبان فارسی به اشترکالی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/105292" target="_blank">📅 20:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105291">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0375b01ecb.mp4?token=oXLOiuYl3i3DKE_QTU4i7IMefRkH3GxnaOL8m_P4rpefwi9iZYNSh5l0ol9DKtVxNYzOtsjgDYMk5Fa3oBRnBxCx4XqxFB6bBuVywGr93vtTRz6DWdSS-3Iaj_MCnCx1sR9IoG6qoFh6UlO1WjmO5v9d5TfbIqBwadViZ8nRMwZwdWfUnoN8wsFWS-_XGyN44LI4CvXWbPGXu3IMU5vaWwEgLSqY42AZPEuh8woh8be3uBjOb83dlIgqZXhaeh7fm2F0FTj_8jiqY5VN1FJQAVRMpp80BTZ-TljxwRZhV8AeqUxMte1O7BPwRLAZEBmP3KOKG_X2nXbWBNgTeEmokA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0375b01ecb.mp4?token=oXLOiuYl3i3DKE_QTU4i7IMefRkH3GxnaOL8m_P4rpefwi9iZYNSh5l0ol9DKtVxNYzOtsjgDYMk5Fa3oBRnBxCx4XqxFB6bBuVywGr93vtTRz6DWdSS-3Iaj_MCnCx1sR9IoG6qoFh6UlO1WjmO5v9d5TfbIqBwadViZ8nRMwZwdWfUnoN8wsFWS-_XGyN44LI4CvXWbPGXu3IMU5vaWwEgLSqY42AZPEuh8woh8be3uBjOb83dlIgqZXhaeh7fm2F0FTj_8jiqY5VN1FJQAVRMpp80BTZ-TljxwRZhV8AeqUxMte1O7BPwRLAZEBmP3KOKG_X2nXbWBNgTeEmokA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به جمع بزرگان تاریخ منچستریونایتد خوش اومدی، برونو فرناندز
👏🏻
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/105291" target="_blank">📅 20:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105290">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUJsJWYZcA-xVAnsG2V0a2O2h2EoGv4W66iZpCeerds6WmS7A9J6RzvKvT2I0_CGsFia0PKW9yvEvT5da_dUEMVqFJUgYLZG12h4fEQ63Ya03Q9yujUa30w4ZpbLWUj1l_xkcI7T0pka7k31tegww6kYfI5K6lX-Q18jmrg43YDwaZcTUvQVVlD19XmcBdVPilX_gKln0hOHQTkZtag5w6sftriBs8fnuCI1XWq-2NfLPPL33ONZOu9Z2ouYASbTe3ZeIJpdKpJWM2qMPOYfxAxYE0jAivysompQWETvnrsJYoQLyFaXS24S4KaBfb8tWXM-9ipq8rm3yPeuHntYcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
ترکیب الهلال برای دیدار با الاهلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/105290" target="_blank">📅 20:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105289">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
موج جدید حملات ارتش آمریکا به مناطقی از بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/105289" target="_blank">📅 20:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105288">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rx9RiendHpRAli4eIVb6og7eQ_uNSWaBtVU1o5J3SJnON2ZxLiIa2TTYbvI4wbXd0TBu2hINjtv9Azw7_HYK7bZNU-ncrg8gcD2PdWaVwoq-RWLT8YchaU3AaRTLszizF449b6brADmSYWd27J2Hfv5dEY5UPUqTPBvllKdMU6l6jbGdtKCSGprqykmp86KNls-t22JTtEgL4_qt0NWtB5P3NWx-xHf04DZHbST9wNx0zOmWoah6C6E23vP86CsQcXHVLvy-qU3WMben-iDZ8LK1Y3S0P_NSfpnWkvmeSgwOMYh9YZ6oC0zOUgu27XJmHqSBecwpE_ibpcBJ0SvdTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
ترکیب
الهلال برای دیدار با الاهلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/105288" target="_blank">📅 19:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105287">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
موج جدید حملات ارتش آمریکا به مناطقی از بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/105287" target="_blank">📅 19:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105286">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
آغاز حملات آمریکا به نواحی جنوبی ایران از جمله میناب، کنارک، چابهار، قشم و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/105286" target="_blank">📅 19:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105285">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
متئو مورتو: مارک کاسادو با قراردادی قرضی به لاکرونیا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/105285" target="_blank">📅 19:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105284">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxYagZSMAkf1f4Gkxi9eQXyxPenbs2_qaecBIpG8ySDtHx6kcPYMXpynvVkugQ-BJzTcQDw2puXLnGNWK6Ie_kibceTjCEOTUuOzfUMKJDfKo5kdVxQdjSYuqmfk31PbbMAcDuPeT-_rKzjoLUxVfQSyTqyNidRVWPdjWbvyi2xCyDh0dYh22JFSEhLGZOpcrWAdC8IsY_GF0nR6a9l4MESYLqk9IdrzrANBw1u75qPa_i5-D66cThaT3GWk6eonZVJchgnffV3mvNcig908R0z06ful3b-O6dasL1Jkz53_Af58mSE8Z0f66fjVFQy-QOwhVHFLFQ4OV2z-CvT9Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
متئو مورتو: مارک کاسادو با قراردادی قرضی به لاکرونیا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/105284" target="_blank">📅 19:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105283">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
⭕️
آغاز حملات آمریکا به نواحی جنوبی ایران از جمله میناب، کنارک، چابهار، قشم و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105283" target="_blank">📅 19:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105282">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🎙
🇮🇷
صحبت‌های سهراب بختیاری‌زاده سرمربی استقلال در نشست خبری پیش از دربی:
🔵
دربی همیشه خاطره‌انگیز است و بازی‌ای است که در تاریخ برای بازیکنان ثبت می‌شود. ما شاید موقعیت‌های بیشتر و بهتری نسبت به فولاد داشتیم ولی استفاده نکردیم ولی از بازیکنانم با توجه به شرایط هوایی اهواز راضی هستم. امیدوارم بی دقتی هفته قبل را فردا جبران کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105282" target="_blank">📅 19:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105281">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep68WtputvOLQKNgMleraEHooJ0GVEL7DBD6VHhGv1zD0ympnnadbmcvQRoVhRPCV0rfwvVl2c8gCds-zzyTIBKHMQMoee74nVC3ftQUBxMeRaSWHmkF4okbE9jNLAHjrtMzol0MqpfE4ZMUfKi_7cfpoNTqglEmmSHE3JS-lQtpCG7xCQ5OCXrLy0ZTm6lG70Z_0CCM3279WGHxLL1XMMtyvrAp1Qyh9VObJLpWgOw2aDGpG3baqxpSkdHiBnfKjSAkRirvAZPE7voW6UCGgCQuM3xLMOJnZximrpyLNlCbenTO6yWo5hhTFvhheiDGj-ku-x8p9wY215XqbgoFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از دیمارزیو: منچسترسیتی و چلسی به توافق نهایی برای انزو فرناندز دست یافتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105281" target="_blank">📅 19:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105280">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33c4f0d2a1.mp4?token=ehsUe-oD2nCHqboDG8XyJALrbXOAKciUOUhxPYKBeVd3jNv-J1aqgpjKxMCxiMnKDr3FgGMo1KzBA4V-Bt_lqfaKrdT5j6YE6syeo2P-zTuGg7p7gn_gTiQUQghqLFXgI-Y-BWvXuVO4bz4aM-51YeNXw3aUMJa0OYhZIKcXaAuAPP5wH6tWFLaLjYvP7IK3OtqaL9Wnxl9HAcNKE4zyMmVgPRthQsT5QPwuYefRVsDge5YYziV9e1JtzVZA6QZIK66ihxL9V_rG8Ej1Lwt93_8QqEQl_8Q7MrNgZRSOuE5U_dXLUFQpc7mD-0GVlST0881NgNZ1EZCPQYIgcG7zqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33c4f0d2a1.mp4?token=ehsUe-oD2nCHqboDG8XyJALrbXOAKciUOUhxPYKBeVd3jNv-J1aqgpjKxMCxiMnKDr3FgGMo1KzBA4V-Bt_lqfaKrdT5j6YE6syeo2P-zTuGg7p7gn_gTiQUQghqLFXgI-Y-BWvXuVO4bz4aM-51YeNXw3aUMJa0OYhZIKcXaAuAPP5wH6tWFLaLjYvP7IK3OtqaL9Wnxl9HAcNKE4zyMmVgPRthQsT5QPwuYefRVsDge5YYziV9e1JtzVZA6QZIK66ihxL9V_rG8Ej1Lwt93_8QqEQl_8Q7MrNgZRSOuE5U_dXLUFQpc7mD-0GVlST0881NgNZ1EZCPQYIgcG7zqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
🇮🇷
هوادار پرسپولیس در آستانه دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105280" target="_blank">📅 19:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105279">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVY1YHymWSYi0tVl9bwWjA0Ckrud6iiGF9ivMZG5q1cw6wLfZn8r-mXZ7iU8Q1UlJ24G2YsRu4Q2b_A3Zj0nbjG_VvFfPOX8JrZzuDXP6jiOYWADiKk2qkTDkYOT6Sbwr8FC-Tv_qiooOGwvgZolmnrOgNvWx-Q2wFYAQbZlzptEQ3L7EEbI6zSYp7kJYBk3-ZqV45V1PCQezVpE0W1s77lukZuiMAzrv7Ra2xyb30ZOvGCtExipOwuGxSl5rADVgjFnTVY_pjjASGH1fGxz7cg2CJKXyGf8HIrrmLTezKk_JsQ51fjia8CWLCVv82TGzgfIu6u6GTU1UJgv5Dp0OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر باشگاه‌استقلال برای دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105279" target="_blank">📅 18:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105278">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07cf132574.mp4?token=G3bpoDAPE7nbUJYmWfsqPjvrrZsnGRY0z1jTbelG3AWmPzShmxkDBWkG28FBmhxr6ghjbEc-Iqwm7P0d5u0oH1kfL04BMZwh7A2nlzddeZGLV5qBavmIvuMIzvM9WlpJ8Z-m9lwxcaCw2Y0MmzMmi__qtY9ibR0x3QNJ6XI5djkeGq84dxPIVt0_dVeNcHyeL9p88-FR6asJaByN0dfCiv8dkssPfrbN9mlGxO_rr6kC0W3qAmHYb8fwJ3Nh0QPapOiHLc7RGsBIi9jMkpo3EMlwfxO69yZEcWp7oXfywtD6FgULdBYoWKu9_6eHRtJx89S3UB_V-HX6sYJDCsBo-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07cf132574.mp4?token=G3bpoDAPE7nbUJYmWfsqPjvrrZsnGRY0z1jTbelG3AWmPzShmxkDBWkG28FBmhxr6ghjbEc-Iqwm7P0d5u0oH1kfL04BMZwh7A2nlzddeZGLV5qBavmIvuMIzvM9WlpJ8Z-m9lwxcaCw2Y0MmzMmi__qtY9ibR0x3QNJ6XI5djkeGq84dxPIVt0_dVeNcHyeL9p88-FR6asJaByN0dfCiv8dkssPfrbN9mlGxO_rr6kC0W3qAmHYb8fwJ3Nh0QPapOiHLc7RGsBIi9jMkpo3EMlwfxO69yZEcWp7oXfywtD6FgULdBYoWKu9_6eHRtJx89S3UB_V-HX6sYJDCsBo-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105278" target="_blank">📅 18:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105277">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guPZup19PF0Zwh8ryaUIQ9984gYgjsWIorWCFtunM335sUmAR5CbGJ3Hjf7_apsGGIg7xvtVbi-iQjZT7Zcaf_40a6vGxG6MlyvTuxnpv-rHZ911DpiuGmKJo0oO0xXmpj5zk5ss-lMEnQEy4jz_RgNKNB2ywZnc2bXuVdHuBVWcSHjQTHXDzfPK3B3OimO3wFLph6lthuaPOeo3yXgcGo2Ptq9syXl4jQaxOgSh6ZrOTpmI6_JHjIBJCsOR7wNwSs2OkILIzuApvgT65pvTiFDQPfN-R1Orbp9F-YosFLP2gJxuvLRMLTPhU3fqRNw0oH2VMVMC8ugRFp01cmLAVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب تراکتور تبریز مقابل شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105277" target="_blank">📅 18:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105276">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7b5a30f12.mp4?token=XHk3_408Imdbun2KdhuF68dShHRoG5bZs7TRBVdwy0AIuBU-Kz9zBxyxHfyr2A9QLrPrQ-IxX6QkpQVsdIfbBS3r-AvMCOLKVv_8_9XcCc3IjudWp9YLfHt-7BM2EBlqYSlKalKreLbkizLtvzI9o6-XI8udRG49rs89SqsA1mW9bqbi3njoQDwkcT00UMssR_wApI7COnRRqI4bTY8NlgILIP8Ss4hom-L6FmZrrL2OXMM9SonvxpQo2skdUw-GfrwjypRrMXuHCK_5ipSMwkfAavuuAOy8cKGSPzS1zaDRV3Kd92P8_ExHb3m7cvIuKEAiTL9Ay1W8_VpvNqxKHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7b5a30f12.mp4?token=XHk3_408Imdbun2KdhuF68dShHRoG5bZs7TRBVdwy0AIuBU-Kz9zBxyxHfyr2A9QLrPrQ-IxX6QkpQVsdIfbBS3r-AvMCOLKVv_8_9XcCc3IjudWp9YLfHt-7BM2EBlqYSlKalKreLbkizLtvzI9o6-XI8udRG49rs89SqsA1mW9bqbi3njoQDwkcT00UMssR_wApI7COnRRqI4bTY8NlgILIP8Ss4hom-L6FmZrrL2OXMM9SonvxpQo2skdUw-GfrwjypRrMXuHCK_5ipSMwkfAavuuAOy8cKGSPzS1zaDRV3Kd92P8_ExHb3m7cvIuKEAiTL9Ay1W8_VpvNqxKHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان‌چالش ترند این‌روزهای فضای‌مجازی
😂
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105276" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105275">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105275" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105274">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRp58W9o8CtofwGTSMvAnhu1boa8YoNKl06f3hWODBw-l6k_96JQY2hAyzSD2U2o3apSaReKTy0vlFk2FcUpBxbn9PAMeSeiYrQFpm512X_GwPp3qnDX5xPfGvpRGApl2TcI3KoYDB-aFYSBy4qu789T6E3wF7jJc8nwKd11vq3tLZBMjDAVMllNkOnpCXJyvswDHgVAeCfWxiOCUTo3xFUCJNQqJlJCvZv96tkNOiJluj_ay7pP8ivI7t50SwHzHJGBFHbMRUIArr8gWNbOr1u00JPuwMOmuHo93v6EV-9E0M7GVVQIHtMiPL12o8c51fiGPZQejOc6k7Wl-wfCtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105274" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105273">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9737ed01b1.mp4?token=fr-LOWoj-FLHkI4zxXonCMSVpm6abHhv6tA4kW8OvW8kQ1uJBuM5VblDWsvqBFK7bRcDftB7mbgUh4ByD3kB1ojOXoJYRWPPvPN9BLDQQdmadScpgWrXxMcjVXzI3j44l1USoixVSu8roMj-NAIfqbnQmXkDYgBe9ixtBVJc6wzwluk3WxKDyIRHaOBPJfhU2IUIwNC_znd7EENbMjQfTen6Vdpyucpw2GHnRytEyM9I542PMk08yM03-fWNQIpJPSu_vBB8vwnLKAl20PepXyKLHV2f1nSuwVOVnoGmF5wiw0VIUrTYqU7Ikz7q441gyMP3bOM6BOt-JEyasM0Ymg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9737ed01b1.mp4?token=fr-LOWoj-FLHkI4zxXonCMSVpm6abHhv6tA4kW8OvW8kQ1uJBuM5VblDWsvqBFK7bRcDftB7mbgUh4ByD3kB1ojOXoJYRWPPvPN9BLDQQdmadScpgWrXxMcjVXzI3j44l1USoixVSu8roMj-NAIfqbnQmXkDYgBe9ixtBVJc6wzwluk3WxKDyIRHaOBPJfhU2IUIwNC_znd7EENbMjQfTen6Vdpyucpw2GHnRytEyM9I542PMk08yM03-fWNQIpJPSu_vBB8vwnLKAl20PepXyKLHV2f1nSuwVOVnoGmF5wiw0VIUrTYqU7Ikz7q441gyMP3bOM6BOt-JEyasM0Ymg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
پلیس‌فتا در واکنش به صحبت‌های دیشب: به پرونده پیام صادقیان قطعا رسیدگی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105273" target="_blank">📅 17:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105272">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/273bbacf0c.mp4?token=FanW2O5senH5D8VtKUeBjYPfbKzBjBEn3MBxC1A0ROmjHUK4-Kzn0fEp7AEQ_NufzDI3KtYTpHdna4kHcbuLCkwCzR64b1ZNGvKS7B4kGwNil8DlMEO4TnX6WE_l-WX_DxWgj4sQU2MqilyuODdzu-7J1g3kaDFIdRtBO9NEUkVm4pR2wJSTx1wySGnuoWy00CvspFi3fLMar1z_xXnGQUt98rHvUCx_ujtJxOQI_6oCp7COcHIc_1xDQgBWe6HbFUnTmQJOoSaXjdCCHp2SDGvFdF15oHbZ_Ks5GStMJSxOwWZsUaoxuYdiF5PRodJt4QwgDyn21y0iIwUBBGbUMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/273bbacf0c.mp4?token=FanW2O5senH5D8VtKUeBjYPfbKzBjBEn3MBxC1A0ROmjHUK4-Kzn0fEp7AEQ_NufzDI3KtYTpHdna4kHcbuLCkwCzR64b1ZNGvKS7B4kGwNil8DlMEO4TnX6WE_l-WX_DxWgj4sQU2MqilyuODdzu-7J1g3kaDFIdRtBO9NEUkVm4pR2wJSTx1wySGnuoWy00CvspFi3fLMar1z_xXnGQUt98rHvUCx_ujtJxOQI_6oCp7COcHIc_1xDQgBWe6HbFUnTmQJOoSaXjdCCHp2SDGvFdF15oHbZ_Ks5GStMJSxOwWZsUaoxuYdiF5PRodJt4QwgDyn21y0iIwUBBGbUMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
تیم‌نروژ با قرار گرفتن در رده ۱۲ فیفا، بهترین رتبه سالیان اخیر خودشو کسب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105272" target="_blank">📅 17:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105271">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1b930efe.mp4?token=ub1swnPO_F-Q0xXIOBVYoaW6KfpIxtm9ZGnI1ElK7FZ_0_t-kXYZ8H51Z7l7gD6-VCQuh6u6k-Lb0kCJ_CBYhBS3mbaK0N52zQUamdGSWms89K8rq2g6uV_kLA7l88u62Fe_0FJK74zKNzdtA8wp33RCiySU_ESscyL0c-RXebF5HvRBtPuKx0Qlwu_dOcLVMx9h08mnc1KdT3x3uI4aQ0eGJ3pztRzELg_kwQ1dp3YBKeawDKQ6BSeQz6jT0zUmpxib_t_I8uG_D1xvatLK2rwcU5kodT3_dLgLHW0cmfZ-S4LynnRShNRYSLDUI5s70JROdopWogXSe1n_k5cZzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1b930efe.mp4?token=ub1swnPO_F-Q0xXIOBVYoaW6KfpIxtm9ZGnI1ElK7FZ_0_t-kXYZ8H51Z7l7gD6-VCQuh6u6k-Lb0kCJ_CBYhBS3mbaK0N52zQUamdGSWms89K8rq2g6uV_kLA7l88u62Fe_0FJK74zKNzdtA8wp33RCiySU_ESscyL0c-RXebF5HvRBtPuKx0Qlwu_dOcLVMx9h08mnc1KdT3x3uI4aQ0eGJ3pztRzELg_kwQ1dp3YBKeawDKQ6BSeQz6jT0zUmpxib_t_I8uG_D1xvatLK2rwcU5kodT3_dLgLHW0cmfZ-S4LynnRShNRYSLDUI5s70JROdopWogXSe1n_k5cZzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
صحبت‌های هوادار تراکتور پیش از بازی با شمس‌آذر: ممنون از نیازمند و ایری برای گل و پاس‌گل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105271" target="_blank">📅 17:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105270">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOV8ROzXCdoV9w6reBmLFv_BHyE8T51Wd44GN8RPtsf1IwisMSN5JXpy8uocECHPSOihP_QpoJ1d_Tm6c1qjOEbwBgjOKs5voTSOGdlxP_JvJQJQLTidCfB3ogKIMOyZ60qcMbkMJbzJXxQ5GBF_XtqFrU9qY9s4ZetyNh24zSJCXt9LbbamHNh7qWwfRQxv-Dc2vXsVCD91fP378oO4VUEhcjRyIMnp9eiCjraWtoyCAGuPGFgd1oxSfys7niV9f9A6Ru_Xkn4q2Nr3kW4cCoPWioY9dnQGeabohuwfG0J1qUiH6V0ssxGvcOt-TvLr4XuY9QELEgkpLFQkwuCnLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105270" target="_blank">📅 17:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105269">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx6DTASKio92OEZ6Txd4w6o_7Gtxjg3rgVwvnkog01f36F1LBktBn84BuTrcy9Ruxm5U5V9EeIJS3BKyCCPUHuqQXIiViE_KfAt7RHtQJsTRPlB_eocUE7dR7368Xi5t5WNsGERdUqy0az5U6SbeNI2J6SMhGgTKF5Z828jf66XgqYNiDiZ4t2keKF6cK3Zwumc0E8kQyBe2ursF71IzFuqaY03CDZHozO5X1re_J6NFCzGL-MU0v1cWRAIjr_pHxi8-EZRNM4dP6evNreBeHWNyNhcPsB3S_AG8woRNE5PP78oZDlgWhIVQn3dHZRX1Bzr5swG2DPw0EU2Dsk1v6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🇪🇸
🇪🇸
مقایسه عملکرد هانسی‌فلیک و مورینیو در تاریخ الکلاسیکو فوتبال اسپانیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105269" target="_blank">📅 16:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105268">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjAqfzhW6-JGNcMVUCf3VEYWnKhkkRpCQLzzrMJnVi3xcIHJTtFYg-bIbBh-T7sSBdiKU9KuOrKTXzJltqdbhBptWOPbu_QdkboihoO8-BpOTKEekCnPPjDHLDUq-TdX_odY3UK09I02Ma1S1t_ChFyFAKjvmCwN8TCtwNPMkyjBPnoFnXuzz6zfB9qTNeq7HAxnuTKRVnjk8nO74lvxH5ML2ORc3YiK4yeiHXG72aRjDH_0ES1VxlGW-9zTQiubdJNxmuOUZE6Wuhs_epYdOgULFkIVyecGq45C35NtF_7EnGkn--lLnSW8QoEY4NXutO0DQGuq6CleHGnlmUVa1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
💥
در آخرین ماه از تابستون یه نگاهی بندازیم به بهترین فیلم‌ها از سال 2000 تا به الان که اگر فرصت دارید در این اوضاع شخمی مملکت نگاه کنید. سیو کنید بدردتون میخوره
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105268" target="_blank">📅 16:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105267">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dfdcc87e9.mp4?token=n1eKTd0KqE47ZGFHhKm-trM7N0j8BqPJNqdR6qnmBs8hcppojdGO8wDgAjtmN_lm7RHOqZ0ZA5Gi0cyg2uyVtUalpBvMgccRwAyWbhrBYjknIokYqpMd0ECsbzMAcKhpXLN0S1YPJehxKRSGEm8vfOZ9DsvYdIeyNTZmERQr7oRZ8eiaaGYhwWvWJidVDO8ikqdJP5eivLOQ4JgQp_bxKD2S-xVSgTmNExVQ6Vn5vj8GgGtT2XvNGBRuy0Utd-gK8pWkEyPtJrjobA2vtkwl0AkTlfPTCjCPlDYmeXPCHKOpShP12AeT40z2Fq8ANhNQOxJ38PaWjYiH1JJ4lRK6cRtdDNkCiaHP2UcPdnRLCv5rNBq9VKNuawFsLwndXD7-ZRy9d97nsRALwxpUrqmn6eYbCrbrp-D3w87caqJ22xOnlziMxSRqSklGkoeYDXXa2kRlzJH6wbsJtiZqEmHxwWTMPmn7ltLQANSQv_OZAG1NPLMHn0f1nPON83IGEG7rNkDSiYNvTXC5N_j1Z6opiZGYpz6NzNWoQAE_rspnxpQp0gxMOc7uinK6U_dMWfHkpURBsLGws8_vC2tcrH_xY-heqEAk-Q1TaTlKBxtoljyUmviZmCxWPz2E5bbXrjnhV7PDinBEDUP8_eglli7DVZYz0sLyjW1ly4SJ9EhlXb4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dfdcc87e9.mp4?token=n1eKTd0KqE47ZGFHhKm-trM7N0j8BqPJNqdR6qnmBs8hcppojdGO8wDgAjtmN_lm7RHOqZ0ZA5Gi0cyg2uyVtUalpBvMgccRwAyWbhrBYjknIokYqpMd0ECsbzMAcKhpXLN0S1YPJehxKRSGEm8vfOZ9DsvYdIeyNTZmERQr7oRZ8eiaaGYhwWvWJidVDO8ikqdJP5eivLOQ4JgQp_bxKD2S-xVSgTmNExVQ6Vn5vj8GgGtT2XvNGBRuy0Utd-gK8pWkEyPtJrjobA2vtkwl0AkTlfPTCjCPlDYmeXPCHKOpShP12AeT40z2Fq8ANhNQOxJ38PaWjYiH1JJ4lRK6cRtdDNkCiaHP2UcPdnRLCv5rNBq9VKNuawFsLwndXD7-ZRy9d97nsRALwxpUrqmn6eYbCrbrp-D3w87caqJ22xOnlziMxSRqSklGkoeYDXXa2kRlzJH6wbsJtiZqEmHxwWTMPmn7ltLQANSQv_OZAG1NPLMHn0f1nPON83IGEG7rNkDSiYNvTXC5N_j1Z6opiZGYpz6NzNWoQAE_rspnxpQp0gxMOc7uinK6U_dMWfHkpURBsLGws8_vC2tcrH_xY-heqEAk-Q1TaTlKBxtoljyUmviZmCxWPz2E5bbXrjnhV7PDinBEDUP8_eglli7DVZYz0sLyjW1ly4SJ9EhlXb4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ربات وزنه‌بردار چینی وسط مسابقات جهانی وزنه‌ خودشو رو میز داور ول داد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105267" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105266">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b94f1ee2b.mp4?token=fBS8SMeBWcDCE6THSpMUeBpJkDRqlTkiKoOvBKyTY0cQ-kTy490n6mpHk8vBSCj1kGXRQMwD6PCTFB8gUJM32IyWttMh5H18XiwOJurydO3DzjvUsR83hRmpcf3LvsNxd-LkR_TlIj-51TV5y1czHKDhKSGBLIbI6hAqHa0x2ANw5rP4JCl-5vQSbDVoiBt_K3cPoWaOm4FXJeWVmSqmwcwDW2zWs2iCYAQ1oGybBvQvJih_V-9ggxtpgotQHWh63MTJJjJx3XKd08w7I2tx30LBPzYysFv8zLHkFGfDFt4oFrUwoWTxgdGrv2vQEhsS5MLK4ZnUguAcK7pt98EG5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b94f1ee2b.mp4?token=fBS8SMeBWcDCE6THSpMUeBpJkDRqlTkiKoOvBKyTY0cQ-kTy490n6mpHk8vBSCj1kGXRQMwD6PCTFB8gUJM32IyWttMh5H18XiwOJurydO3DzjvUsR83hRmpcf3LvsNxd-LkR_TlIj-51TV5y1czHKDhKSGBLIbI6hAqHa0x2ANw5rP4JCl-5vQSbDVoiBt_K3cPoWaOm4FXJeWVmSqmwcwDW2zWs2iCYAQ1oGybBvQvJih_V-9ggxtpgotQHWh63MTJJjJx3XKd08w7I2tx30LBPzYysFv8zLHkFGfDFt4oFrUwoWTxgdGrv2vQEhsS5MLK4ZnUguAcK7pt98EG5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105266" target="_blank">📅 15:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105264">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38daf6a490.mp4?token=H2MKV1fuMm259VCvQjMxmkvwjIJrCuuXqWvK9ujaAZfEyjgCP0CTRu-0_Ifo8eoTTsFdW0QydzJUTtv-oL884DRmu--BNOgsiTj_mQ9ZvOBjBmLL_aral9VHDInv4fs_RmiN9Q3HME34_qCvkin5RkbZ9v-5H6hKnnmlUuD1QabGWsEPWnAionaHi9FRvB3ig6rA7SE6dWvv70Hl1_hL_r9VH9rlQPDFAs7XbQoS95olrVtcVIcZ9OqKX5mL6htz_6j1DxtfAFCcd0dgJvkCqwhexGaVm-bdJWTQv0LU7Fp-9ee_SVAIau7H-F0-F1aYI1DxmPPprDkfh5uSrzNlyzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38daf6a490.mp4?token=H2MKV1fuMm259VCvQjMxmkvwjIJrCuuXqWvK9ujaAZfEyjgCP0CTRu-0_Ifo8eoTTsFdW0QydzJUTtv-oL884DRmu--BNOgsiTj_mQ9ZvOBjBmLL_aral9VHDInv4fs_RmiN9Q3HME34_qCvkin5RkbZ9v-5H6hKnnmlUuD1QabGWsEPWnAionaHi9FRvB3ig6rA7SE6dWvv70Hl1_hL_r9VH9rlQPDFAs7XbQoS95olrVtcVIcZ9OqKX5mL6htz_6j1DxtfAFCcd0dgJvkCqwhexGaVm-bdJWTQv0LU7Fp-9ee_SVAIau7H-F0-F1aYI1DxmPPprDkfh5uSrzNlyzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
⚠️
واکنش عادل‌فردوسی‌پور به حرکات منشوری شجاع خلیل‌زاده و عارف حاجی‌عیدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105264" target="_blank">📅 15:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105263">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1a906213.mp4?token=r2wHOo0C1V7-HQku-42Z3E_gdLOwmsVQ4zusXtnJHC4euCC1TyuwJZ2xaEShIql4hr66QcXu4Unf_ryGuEqGd1moXR0umnXLKTZne4nD9KeG8UhunsDWKHdkHoZMQGnCl-1J9GC1BXF0YjMMDox_PGfnLy0NTQqBDpm1Vfn1GnI6o-UgrYfsWuTxZzYy4sEcFUbli5mqeAA9WbmVMnjzxhgWoz_92T6nSlKqU6D6sb91-pg9CnZ603tm6jS13EM6FfkFXYdZNvbMJ7FHbwGyKclOfdLPxL0Aj99fFQDA29MOm9eZcScL9LB4RgaD1P_LxjNZRjB7YobCwl9PAHqXhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1a906213.mp4?token=r2wHOo0C1V7-HQku-42Z3E_gdLOwmsVQ4zusXtnJHC4euCC1TyuwJZ2xaEShIql4hr66QcXu4Unf_ryGuEqGd1moXR0umnXLKTZne4nD9KeG8UhunsDWKHdkHoZMQGnCl-1J9GC1BXF0YjMMDox_PGfnLy0NTQqBDpm1Vfn1GnI6o-UgrYfsWuTxZzYy4sEcFUbli5mqeAA9WbmVMnjzxhgWoz_92T6nSlKqU6D6sb91-pg9CnZ603tm6jS13EM6FfkFXYdZNvbMJ7FHbwGyKclOfdLPxL0Aj99fFQDA29MOm9eZcScL9LB4RgaD1P_LxjNZRjB7YobCwl9PAHqXhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای دخترای جنوبِ ایران
🫶🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105263" target="_blank">📅 15:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105262">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JetAHRqO8t7sKt-Q6NPwlLgOqS8IiLreHTEwkF5knAC67KfD8tmJr4NDfQdwWjNVuDxSRnn0Et2ylqM_LlsGSS8amhBjrBbtiMzcrwuycu9Oa2rHP7xz-XFP-HJ3iexSWlhnSL96XYRNegvB8WEJc4_3JP4K2yy9P6TyC3vqsXY66EOcqMLAkKtWbfj0YZp-qsG69ZbwD_rb5hm-31sI70vWhZPcQbYFfLWVQR06HSZq_v0mMrUPgPXGjxa6jg0hOoWMmyhop8NXCKv5ZWk0c8TdsQ23urWZoSRhnK5jNR481-ZBiYsH8ONSmEKEQCHxDJdaQxJo5ACylR3WSGSboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇮🇷
هوادار بانوی تیم‌فوتبال تراکتور تبریز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105262" target="_blank">📅 14:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105261">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93b254714.mp4?token=kHXKaorHWSJKc6dyj0otYI2S-HLJRz_wUvCnvQkItfPwKqEPn-wXTQ76-sHoudn6bb-90ihymajp4W7muMtcYDZ_Aq1fZXthJlbfPuuBMjmqRIUk-wgCT-Y9OX5aHVgEYn0fxz2ciD3zxUPWBnGuGYLEX36nxcTBFUAG3aK6vifY5ejj9dOCLv0CM2YhPATqqiTI5hzXKtFnyMOt3ZVNXhSk_IBq6VgBV-HZZ9Q55YqIMRfQKFw_Gu41FPP99K2LdpbeVp5J5JuTQ7JhdI6Sud_6RxFf7gXfoineufAT3gSVhX36QAis3VF2W1mn3Qck3UWC7KBY4i2SCOC6iwhqRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93b254714.mp4?token=kHXKaorHWSJKc6dyj0otYI2S-HLJRz_wUvCnvQkItfPwKqEPn-wXTQ76-sHoudn6bb-90ihymajp4W7muMtcYDZ_Aq1fZXthJlbfPuuBMjmqRIUk-wgCT-Y9OX5aHVgEYn0fxz2ciD3zxUPWBnGuGYLEX36nxcTBFUAG3aK6vifY5ejj9dOCLv0CM2YhPATqqiTI5hzXKtFnyMOt3ZVNXhSk_IBq6VgBV-HZZ9Q55YqIMRfQKFw_Gu41FPP99K2LdpbeVp5J5JuTQ7JhdI6Sud_6RxFf7gXfoineufAT3gSVhX36QAis3VF2W1mn3Qck3UWC7KBY4i2SCOC6iwhqRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
بدون‌شرح‌ترین‌ویدیو امروز...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105261" target="_blank">📅 14:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105260">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411e9bcdcb.mp4?token=QqegKNDC4LahwtaOTqDkt6CuB9rEKaw8DzXWpSZaoTr-hPKx7fMFAupVS7eMcNXn0fempq-3BYjy3Kwvkk1vXDjLL2-GxUeM-By-k0B2YEaRdlJE2q44aZvsctFyd3nRtKIh4Eu6atIsMswN7ri7RJfcD1Is-qfqadqVC4AB4w7yAjKrIgHBa0F-IheBWbukeHdi-l9yUHrCWtz9Y1W2FYEZOxbMOjEF_1wZ1kP6g4NM0c2KKCfdqODQvv3nP8hdJYgXOjgyYqmb3YrXX7l4NAdjzRocg_zS4Gq7S37r4-CYlKwUZA5A3Yo3PFC5zaKlPoRsYPZmPZ-nrEelZrQIhAJYiAVtGgrobKnFHAsGx2Zc4b4FhtY5CY7Z1emdHVdH-s9sqACX0adLq9nPTNjmAW1Y9-Kj3g18r39RCx9cVYJhbx_q27qhW7ib4w-SKBEXKN_ieVg-FFcoihK-XseiRIQdP6w-l4KDytX32zmRND-Oubn0yyI4-B1voZ4d2yIcvephO2p54-bCW3J0xxAdUhJkYrU38gqyaBarbrMhnff5bej661cHLBsTtRUqvOz1CYjbV5iMCtp2ByAKWfRPM5GANFIv1aNeHLai94mVNQe2qa6sJxqQWh25vgNp5Y7YUb8I01oUVdpDpRjTcC0C8lY1ZZJnIT3ANVdMujW54cY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411e9bcdcb.mp4?token=QqegKNDC4LahwtaOTqDkt6CuB9rEKaw8DzXWpSZaoTr-hPKx7fMFAupVS7eMcNXn0fempq-3BYjy3Kwvkk1vXDjLL2-GxUeM-By-k0B2YEaRdlJE2q44aZvsctFyd3nRtKIh4Eu6atIsMswN7ri7RJfcD1Is-qfqadqVC4AB4w7yAjKrIgHBa0F-IheBWbukeHdi-l9yUHrCWtz9Y1W2FYEZOxbMOjEF_1wZ1kP6g4NM0c2KKCfdqODQvv3nP8hdJYgXOjgyYqmb3YrXX7l4NAdjzRocg_zS4Gq7S37r4-CYlKwUZA5A3Yo3PFC5zaKlPoRsYPZmPZ-nrEelZrQIhAJYiAVtGgrobKnFHAsGx2Zc4b4FhtY5CY7Z1emdHVdH-s9sqACX0adLq9nPTNjmAW1Y9-Kj3g18r39RCx9cVYJhbx_q27qhW7ib4w-SKBEXKN_ieVg-FFcoihK-XseiRIQdP6w-l4KDytX32zmRND-Oubn0yyI4-B1voZ4d2yIcvephO2p54-bCW3J0xxAdUhJkYrU38gqyaBarbrMhnff5bej661cHLBsTtRUqvOz1CYjbV5iMCtp2ByAKWfRPM5GANFIv1aNeHLai94mVNQe2qa6sJxqQWh25vgNp5Y7YUb8I01oUVdpDpRjTcC0C8lY1ZZJnIT3ANVdMujW54cY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
دیشب‌کریم‌آدیمی بنده‌خدا فکر کرد چون ۱۰ دقیقه تو زمین بازی کرده دیگه بعد بازی نباید تمرین کنه که دستیار فلیک این‌شکلی کاسه‌کوزشو میشکنه و دور تا دور نیوکمپ کنار نفرات ذخیره تمرینش میده
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105260" target="_blank">📅 14:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105259">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c284d93a.mp4?token=SvF-AOTAOJ7wv4859tHT5N4-ySO8i2jy5qwrGfojmTNArweNRqQlQXBKsEbwqIaoS2VGUh7GERYCjkAiPR_A02SxdkwaJKEk3BzX5gd3BU-ChiLay3CFdRnHyc2uWPKQZQzfM4t3FANK23vxvbylsVUVsv7z9dtHT4BwHsENfTmll5FvOeHSs2BELMWwh5vYloLPROMJcMojJ7MT-fWYM8OnVfWXcGNWySuBl5abUS_VR3s9T1GaH7rIc4sdHULn9YGj4VPQhjQbog1sZTLHQs9LcRbswXJM16SvDDGhBb9J2BIoQjVlteRj9wB5dFpu8UQsdkPUlQzIzdHdd18Rpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c284d93a.mp4?token=SvF-AOTAOJ7wv4859tHT5N4-ySO8i2jy5qwrGfojmTNArweNRqQlQXBKsEbwqIaoS2VGUh7GERYCjkAiPR_A02SxdkwaJKEk3BzX5gd3BU-ChiLay3CFdRnHyc2uWPKQZQzfM4t3FANK23vxvbylsVUVsv7z9dtHT4BwHsENfTmll5FvOeHSs2BELMWwh5vYloLPROMJcMojJ7MT-fWYM8OnVfWXcGNWySuBl5abUS_VR3s9T1GaH7rIc4sdHULn9YGj4VPQhjQbog1sZTLHQs9LcRbswXJM16SvDDGhBb9J2BIoQjVlteRj9wB5dFpu8UQsdkPUlQzIzdHdd18Rpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
عملکرد پشم‌ریزون دیشب لامین‌یامال برای بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105259" target="_blank">📅 13:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105258">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4862134a1c.mp4?token=jfWbCeh8DAv0j33xCEXsjCNFfaSUyRHA6N87cjyuIL7-dea6zn-H3l_m54qDthGGLei6Qy4bI6K5dM_g5DOacBSsAhoihET-hSGZXNzXp0u25QCEYH-wVlBcEW0VQLs05tAhnQ7rrzwvXEei98f6veCQGBhIRpF9S9HRrWMO1rb-XgDwLV6f8o951LeyJHwjLMfG7idbay3ikgKSMYcl_9kZJc3l-0Wnic5z-wpE4W9zwVj8O2GvNKMnZsuyWGoB4bby31LwxUo3YWFHpFyoqbSNzK3kmgpLrXa0wMspQxBox1hw0n9dPP1f3MHuoOWlxMW4me6G2tOlntXjPpnVCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4862134a1c.mp4?token=jfWbCeh8DAv0j33xCEXsjCNFfaSUyRHA6N87cjyuIL7-dea6zn-H3l_m54qDthGGLei6Qy4bI6K5dM_g5DOacBSsAhoihET-hSGZXNzXp0u25QCEYH-wVlBcEW0VQLs05tAhnQ7rrzwvXEei98f6veCQGBhIRpF9S9HRrWMO1rb-XgDwLV6f8o951LeyJHwjLMfG7idbay3ikgKSMYcl_9kZJc3l-0Wnic5z-wpE4W9zwVj8O2GvNKMnZsuyWGoB4bby31LwxUo3YWFHpFyoqbSNzK3kmgpLrXa0wMspQxBox1hw0n9dPP1f3MHuoOWlxMW4me6G2tOlntXjPpnVCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
محسن نامجو مرتیکه دلقک در کنسرت نیویورک، شانزده شهریور سال ۱۳۹۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105258" target="_blank">📅 12:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105257">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از دیمارزیو: منچسترسیتی و چلسی به توافق نهایی برای انزو فرناندز دست یافتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105257" target="_blank">📅 12:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105256">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950b2c8673.mp4?token=Ud7fBZuPkbwvfiqQ3Cfw4XbHiV4icC9GsKua8_lH1CY8M_BjcSqQP7in2JFdhwaRQYmukYHmYnBm-U0mDT0rE7hrSKIl9lO0NZyZ1b_xNVIvlnEbjTdnMjHGu6eABTW0NjN18Xw6EJj4ppOL7vrTCR5yyz356l8UY5ra4VGv2_R0Z9TLlrr1ZPHD9pJSK5HjzanbHraUTqBLc-ZYZ-VE215lkAnzMHNbgYYnVHDqge49b_P_6NVG-rUymWgazIxTTYcMDZSNtTWFUwgKog_3L2wEP7MfmUwBnHESPrCt9ZA4iswcFXUyybb2fWLbxhmuVYpfqGqJTpFNq3v6AJm1KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950b2c8673.mp4?token=Ud7fBZuPkbwvfiqQ3Cfw4XbHiV4icC9GsKua8_lH1CY8M_BjcSqQP7in2JFdhwaRQYmukYHmYnBm-U0mDT0rE7hrSKIl9lO0NZyZ1b_xNVIvlnEbjTdnMjHGu6eABTW0NjN18Xw6EJj4ppOL7vrTCR5yyz356l8UY5ra4VGv2_R0Z9TLlrr1ZPHD9pJSK5HjzanbHraUTqBLc-ZYZ-VE215lkAnzMHNbgYYnVHDqge49b_P_6NVG-rUymWgazIxTTYcMDZSNtTWFUwgKog_3L2wEP7MfmUwBnHESPrCt9ZA4iswcFXUyybb2fWLbxhmuVYpfqGqJTpFNq3v6AJm1KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
مجتبی‌پوربخش: تا جایی که اطلاع دارم، وضعیت جسمی علی‌کریمی خوب است، فشاری بر او وجود ندارد و صفحه شخصی‌اش نیز در اختیار خودش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105256" target="_blank">📅 12:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105255">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVesPkHadudGBpPI732Uz3D5NOtwgxsg9hT40V1XntGVe0xy8ea30dzPL8JqOdKYVEFoEnkSGHdR2xzCHOMqyF7EVmTNtOKasS_e3htJj7XHkqeSSt7lw4pUbZ8P19wLpn5OoItW56EQdFfVdG1Fr615Ev7H3WJ3jFzTCIDSymF6yIkPCtBnBZ1D_PQgUbE-PhxoDCAbZ-xV_FHY9UzrGhjLe5F3tlcMlZVQspOazDWVWJ34uc6F_n2smLXjHwgT-2SOOcrpbvSfT1yWsF3AOoMWzB4xG02f5SZ-VU0kZrj3Qvpa5fDse3Bl9Pni8zm3JnyqroKIeR_9xWsiQRXHXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
نتایج سه‌بازی ابتدایی بارسا و رئال در لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105255" target="_blank">📅 12:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105254">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f53a6fd8f.mp4?token=tTU6BnN-EQMjoPJw1dwj96uteHg-NQbpNks3pJeAf2YE_ggULdmhLInvgQFvqiWkK5CJuL4jtgxp2pcdYQQAqil6kgkyolsmJvCN3hJnVzC6AKnCFN8_quRO8q_fkWK0h9gH6406AUWGABwwY8mkAbTWZd_shDErAp0gxBz84gS1uiNkIXcJegAdKYwBsdaaD40xoStj4PfkwCN9Vb-IAVDSwTVpxu8DKdSIKHHIxIO24SpSBi5fucOfjsj8uErpYm8I-2GafHFYKNW2VA0gusAn60NJyDgI8C5bbTT6XPNOKwKj_YqHncGp80RBtTQNBK-8_BavRBIz6tstQQ0gnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f53a6fd8f.mp4?token=tTU6BnN-EQMjoPJw1dwj96uteHg-NQbpNks3pJeAf2YE_ggULdmhLInvgQFvqiWkK5CJuL4jtgxp2pcdYQQAqil6kgkyolsmJvCN3hJnVzC6AKnCFN8_quRO8q_fkWK0h9gH6406AUWGABwwY8mkAbTWZd_shDErAp0gxBz84gS1uiNkIXcJegAdKYwBsdaaD40xoStj4PfkwCN9Vb-IAVDSwTVpxu8DKdSIKHHIxIO24SpSBi5fucOfjsj8uErpYm8I-2GafHFYKNW2VA0gusAn60NJyDgI8C5bbTT6XPNOKwKj_YqHncGp80RBtTQNBK-8_BavRBIz6tstQQ0gnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
ویدیو زیبای و دیدنی حمید سحری پس از اعلام خبر خداحافظی اسطوره لیونل‌مسی از تیم‌ آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105254" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105253">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105253" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105253" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105252">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8DiQk5zoI47f0nm4GAzy7hbilWkSbwWdv0gRZDiSp7FtKncibR-_NcqccRAE8ZplaZa5fI0FLbmt5cVuiNXNKDvCk5jBBGnCOGOybYf6vFXKSonLwosdi0Oy6pf88EvJLk-K7FwtScET1GRrZwJtmTuRBeh-DaK0pw5R6tmmcbrMNqMdCH30vWIbbHYNXpI_OyNSkQrr8nrf2wwcWL2YDvOF20FFP0cAnnoR9PyMoWzepEwn0uVXpSAubXm0jhnF3Ae_BwD_dvX5ZJTXnvn5kFeo1U0UY49igzAiasu4mDzMBQoj0xMogyfgHY2YtRXBV-ihfOm21sOIEAFbzyNCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش بینی کنید.
مونزا
🆚
تورینو
دورتموند
🆚
هامبورگ
کرمونزه
🆚
پارما
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105252" target="_blank">📅 11:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105251">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f62060bab.mp4?token=fXNZLlFBv8kslfnYKmK3khaYZx9hUgdUAJWzyc_DiIRN9BAQ7ZqIv8BCAJC_TAQ_Y5-mWAq_F3KkUnMiAhscKd980txrjNAuMqkuJ60x-fUA_0cxntbmv30cnFMtMbYf2ejuPspDhCevSi3D6Ds7lBntFpONtg7UAJ8VuX-2Mrv93v_6yH-Be74Y2iSw1sjcrXlCbYO3FAh3VCoSbrHwJmj9MH3tP2nf6Btwfz5jJnCMfLd30Ccj3AE3-1auCytcN1WTBVlqTmqWn9H9YcTcT0AAEuiKlm7bbXhVGWoUcwIVaUL_6w7QVKseot9eCtSyy28sR0U205JB4OBlavz3bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f62060bab.mp4?token=fXNZLlFBv8kslfnYKmK3khaYZx9hUgdUAJWzyc_DiIRN9BAQ7ZqIv8BCAJC_TAQ_Y5-mWAq_F3KkUnMiAhscKd980txrjNAuMqkuJ60x-fUA_0cxntbmv30cnFMtMbYf2ejuPspDhCevSi3D6Ds7lBntFpONtg7UAJ8VuX-2Mrv93v_6yH-Be74Y2iSw1sjcrXlCbYO3FAh3VCoSbrHwJmj9MH3tP2nf6Btwfz5jJnCMfLd30Ccj3AE3-1auCytcN1WTBVlqTmqWn9H9YcTcT0AAEuiKlm7bbXhVGWoUcwIVaUL_6w7QVKseot9eCtSyy28sR0U205JB4OBlavz3bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
🇮🇷
فرشید باقری: خداروشکر به پرسپولیس نرفتم؛ آبم با آنها تو یک جوی نمی‌رود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105251" target="_blank">📅 11:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105250">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbad291eb3.mp4?token=a2d_cA7l62anDL14kPm6aw2CgvUx1E6zKT_j7Sga5QZlyqiodkvp2Nr3jLFuUk3VJEsGAwsMCDutxsccU_tJWRqt8YD0xjgnJn00BEyYrG1m4A5U1hjOzcZNuFtFG9srS-EoyHrVq_9Ywnn2vrAd9_tC6ww7T_czsztvUPPaCCI82haNpThXgoPmIkGtlFgSOXPVojoOiRXhBfELhrABVpgQRnPgXaT2wkIqLWELqra-0sWJIbB36RLV111Cbn0B8d1NxxNiBoi4jc3wLPlShAiqNIG9O-FE_-wQRP-pHOlWAyrLBifznVML-8Mxr_YCZpo_c93ggxRmNZwYAsAz-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbad291eb3.mp4?token=a2d_cA7l62anDL14kPm6aw2CgvUx1E6zKT_j7Sga5QZlyqiodkvp2Nr3jLFuUk3VJEsGAwsMCDutxsccU_tJWRqt8YD0xjgnJn00BEyYrG1m4A5U1hjOzcZNuFtFG9srS-EoyHrVq_9Ywnn2vrAd9_tC6ww7T_czsztvUPPaCCI82haNpThXgoPmIkGtlFgSOXPVojoOiRXhBfELhrABVpgQRnPgXaT2wkIqLWELqra-0sWJIbB36RLV111Cbn0B8d1NxxNiBoi4jc3wLPlShAiqNIG9O-FE_-wQRP-pHOlWAyrLBifznVML-8Mxr_YCZpo_c93ggxRmNZwYAsAz-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
🏴󠁧󠁢󠁥󠁮󠁧󠁿
وضعیت سخت‌افزاری ورزشگاه اولدترافورد که وسط بازی از سقف ورزشگاه آب میچکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105250" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105249">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGz0-iVAeroolAj-nO1KBEQVykg5WfKgr3Uj7xJ18uEDC6-cgH8zxlXTlkIy8_DuLTPQv0ZyZF9vAewlX_wSO6X1q7MpC_tbDGNA3T0WU4bbNsrRMTVfs7yHxdLnH8SLhLc-ODthEL-L0mUJb_8XjE_0CiCwuFJVBBjovKQUG46borqOQaFywi4QwvDkEEjGY2qZ1bLsY_1aO3hym97D-Qk7680z6OoddotkFoRftR4FCWfzPIWWjyb2kbRbJDUfOM_x7Q-9LuYTp5hTjw2fA_HVw3XGN587F08Sy4LJhYTbjvcoVWZ3xtle5dkpG9-NF-RbF3EqXGQ2kaq46yIQ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
پوستر باشگاه‌استقلال برای دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105249" target="_blank">📅 10:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105248">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a276b65ea.mp4?token=KgZfeuSuHtW-fFT3Wb9KRk3_7JBDWnmL52BRqjKSzP_Blz04On5mMG5bfCs5g5mwk8yn4myhUJkDtQknsMYplnWBZ-6br9qbbaqmFcQbOiZBlYZq4OA7ooL-cW6ytq_lfuPIFyRZdbhTJamiOq9sDTXf9ZCFp1D1GprX6bYv0mtpSrbtTJDYbKyhOyuVnVuWSbho81z0LlyTSNOuE2Sw2723EIlbAaU854Nhkr3cAXGAY6A4Uuve-Q0LSTNg7A7oSnh4HJMtNpJGAGomyup0BzQURac0HZaxy9cf3AAfMafGwK8_jzmt63KhdrbJwzgAkzC6X0SZ-V_UvxTI9BZdsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a276b65ea.mp4?token=KgZfeuSuHtW-fFT3Wb9KRk3_7JBDWnmL52BRqjKSzP_Blz04On5mMG5bfCs5g5mwk8yn4myhUJkDtQknsMYplnWBZ-6br9qbbaqmFcQbOiZBlYZq4OA7ooL-cW6ytq_lfuPIFyRZdbhTJamiOq9sDTXf9ZCFp1D1GprX6bYv0mtpSrbtTJDYbKyhOyuVnVuWSbho81z0LlyTSNOuE2Sw2723EIlbAaU854Nhkr3cAXGAY6A4Uuve-Q0LSTNg7A7oSnh4HJMtNpJGAGomyup0BzQURac0HZaxy9cf3AAfMafGwK8_jzmt63KhdrbJwzgAkzC6X0SZ-V_UvxTI9BZdsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
افشاگری شب‌گذشته داشعلی‌منصوریان از فساد شدید در ساختار فوتبال عراق
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/105248" target="_blank">📅 10:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105247">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6PhYbykf5tXxxchxc61wtyUEnLveu8buPio0tbIwDavap99i20_1yfSc5I-CUAVPiYBJvYnyvZcyyoAuKt1Kn7EMpYVfBY2Q0Y3yV-RE29rhSk3zosv5IA5HJbSxWZqD8Qw-zGIJsJD8oB_XNOYfvhWDKO7gr-6tmrQ9H_u-kNrlS4twA602UaVHVaVO_sOtxGXDQvlo1R6DgbXLKswzGAleW1jnLpjjUzr1tnNw89JoHf--1HWHpf_C1GTwgtwVvoKL2jmH7UiR2pE6doDK_PP2tPO7aXlBgnrbQqJb6mLvyoa9AMxH7LlWAiPZKTX66UbLkjAiY9Tfh4UerMXyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
با حکم کمیته انضباطی، شکایت دو تیم سپاهان و مس‌شهربابک از استقلال بابت بازی غیرقانونی یاسر‌آسانی مردود شد و این بازیکن مشکلی برای همراهی استقلال ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/105247" target="_blank">📅 10:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105246">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1b1a2663.mp4?token=OW2jhjk3XaQi333o2yHn5hu7hRcZXLWdSKX4dHBffPpPFOhJ_7zT7WffE8_EO4lzgKmrLMJ5r9oiN9zrshKQOV7JhHLMGAjmVUftu0c91mtnikgdthwSxchn59OmEjzPoBWvJDvZ5GUlptqCuac0vZbH04NojEqR16ULTmRJk9pvCfm3ZYI8R_qKtkUzKMBlgW7IDQjbArbz4GUcEO_PVAq8HwXhakTdEiXDc8ytpwpA-odHmv5s9btBRRH3WBXhmxhtoV-QpsNuk-8d-f_mmYoLs23OsZfvFZ3ZTvHbFF2y0zw3VGn4YB6lwqkWFA7iM67svSnJ-nh61IOgtwnq9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1b1a2663.mp4?token=OW2jhjk3XaQi333o2yHn5hu7hRcZXLWdSKX4dHBffPpPFOhJ_7zT7WffE8_EO4lzgKmrLMJ5r9oiN9zrshKQOV7JhHLMGAjmVUftu0c91mtnikgdthwSxchn59OmEjzPoBWvJDvZ5GUlptqCuac0vZbH04NojEqR16ULTmRJk9pvCfm3ZYI8R_qKtkUzKMBlgW7IDQjbArbz4GUcEO_PVAq8HwXhakTdEiXDc8ytpwpA-odHmv5s9btBRRH3WBXhmxhtoV-QpsNuk-8d-f_mmYoLs23OsZfvFZ3ZTvHbFF2y0zw3VGn4YB6lwqkWFA7iM67svSnJ-nh61IOgtwnq9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
‼️
عمو رشید دهن سرویس درکی از دیدن برنامه با خانواده نداره
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/105246" target="_blank">📅 09:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105245">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f95056c4.mp4?token=GnCfiAlDSkxQTBVwJyoYdRjjhtS8ywaxJMJbyenC5Xtp4t-Nu8snWJXWve1ZyekGOyKlBrEtCq7CRln2Hr8-ftTxuhxLYDBkZZFqLieVJhZvXc-BDnsBSHvMpQEoAOXur4dQkfVixef6b82FVaYTP3pNtIUB2MVDby8ApDWFTSbErB0FV5ZOy_KbjHpO29qXVH4FEj_jcrIZo4RL-xQrCeJ-64rB6EaDg11MosMLhQ2wFkQoet2awIkNFciyK1RBVn-6Wz6s1t4xh-yqTilQD1K3JJYE-3NQZBzC6T-cdHFD1FwsafDPftemnkwGe9w4_PaCovYWpe5wYBbfYW3QHIzMNt2nu1saz1-H8zJX-ySEs1fQPeT8uEF8TyeS26TvirJEq2uS5IYtYx2MSuB061WKdieOk98B2DyvaFOQL63OxwiB-cnoB5YdVxofYgRwIzqdG5ShpiD3HXuLSdq4gOYqAGmw9bcLWRgcBsK-5cJFTEjOEWlLsbL8ZTgO-U1lIufr_uk_Q-JXCayfJyDxGTYMtbdhBT4zswQy6uMuMqHqxoGTEX-29_YzwCrBkp5TJY9ZgZ-W11xZNtwOr3Xnf-5NVnx-kAPAl8xNLmMNxJaW27n0w3vMcDqnSqMOsfpz8fFyJBu38ADbQXhk6DpQpZzT7AAXzQDO_8go5jROTFk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f95056c4.mp4?token=GnCfiAlDSkxQTBVwJyoYdRjjhtS8ywaxJMJbyenC5Xtp4t-Nu8snWJXWve1ZyekGOyKlBrEtCq7CRln2Hr8-ftTxuhxLYDBkZZFqLieVJhZvXc-BDnsBSHvMpQEoAOXur4dQkfVixef6b82FVaYTP3pNtIUB2MVDby8ApDWFTSbErB0FV5ZOy_KbjHpO29qXVH4FEj_jcrIZo4RL-xQrCeJ-64rB6EaDg11MosMLhQ2wFkQoet2awIkNFciyK1RBVn-6Wz6s1t4xh-yqTilQD1K3JJYE-3NQZBzC6T-cdHFD1FwsafDPftemnkwGe9w4_PaCovYWpe5wYBbfYW3QHIzMNt2nu1saz1-H8zJX-ySEs1fQPeT8uEF8TyeS26TvirJEq2uS5IYtYx2MSuB061WKdieOk98B2DyvaFOQL63OxwiB-cnoB5YdVxofYgRwIzqdG5ShpiD3HXuLSdq4gOYqAGmw9bcLWRgcBsK-5cJFTEjOEWlLsbL8ZTgO-U1lIufr_uk_Q-JXCayfJyDxGTYMtbdhBT4zswQy6uMuMqHqxoGTEX-29_YzwCrBkp5TJY9ZgZ-W11xZNtwOr3Xnf-5NVnx-kAPAl8xNLmMNxJaW27n0w3vMcDqnSqMOsfpz8fFyJBu38ADbQXhk6DpQpZzT7AAXzQDO_8go5jROTFk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚪️
افشاگری پشم‌ریزون عادل فردوسی‌پور از ریخت و پاش چند صد هزار یورویی مسئولان تیم‌ملی جوانان و امید در اردوی ترکیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105245" target="_blank">📅 09:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105244">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5c71afe0.mp4?token=EMLDzbOagpp_af2QcQKhNU9YxRk6fYnFpy1H9Lo-IgBCoJ00jMdWkpdKCQjXebgSWnvSJVwYMsDZoSL0ab3XuQnj00837GsJOJ0QIFeoB08wWKYYVf4dgi7YzEwgaSCKniDsyRAE0bVHCYuO7ObGw7Qn1BXsT8ZYwIgT1FFQg3kYwOEEwooxKZgmib7NPI9dT-3Z2Na7YTe4CYVMy7eSLqFYp6zXlAGAeIGaSBY3faPskZgrcxNKWcIiF2Dd0SRX0uilV45EXHpE6DvUVr95T5m4HKrGugfY6BxpoFeUhD9WaGAvtbjHpcJ6uejNJ3oX7LhUlwHDGJLc45nXUjYuOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5c71afe0.mp4?token=EMLDzbOagpp_af2QcQKhNU9YxRk6fYnFpy1H9Lo-IgBCoJ00jMdWkpdKCQjXebgSWnvSJVwYMsDZoSL0ab3XuQnj00837GsJOJ0QIFeoB08wWKYYVf4dgi7YzEwgaSCKniDsyRAE0bVHCYuO7ObGw7Qn1BXsT8ZYwIgT1FFQg3kYwOEEwooxKZgmib7NPI9dT-3Z2Na7YTe4CYVMy7eSLqFYp6zXlAGAeIGaSBY3faPskZgrcxNKWcIiF2Dd0SRX0uilV45EXHpE6DvUVr95T5m4HKrGugfY6BxpoFeUhD9WaGAvtbjHpcJ6uejNJ3oX7LhUlwHDGJLc45nXUjYuOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو خواهر پژمان‌جمشیدی از برادرش در بدو ورود به کشور کانادا پس از رفع مشکل ممنوع‌الخروج بودنش بابت پرونده اتهام به تجاوز !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/105244" target="_blank">📅 09:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105242">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fa9c53173.mp4?token=V-Qg8mIv9Zt2CCaivRmJmHob9NXJzsucDwGik-QVx2f9jCa5RODyoj3Efa8SjkE2q_umRsxDzFAJ4MKEZyZkex8Uwj0JEj19HNVd9xsVrjZm5TIkMwFs-zCmfh-Fm1FoTpv189PTmsjt-QP6Old4aAwUcdPbg8nw0T4RUR5rE-9eSIegvYDlONdHTMJjtjzlWPWHgGOh4rxS0MIfU9RcVTXyZ32qqX9oIaunQenAN614mdUdIEpBvxL_lUJSo62MrAQztZRbmzcO6zg1VzdYboqJR-1OkmzmYPOb068f1al3h9ASzNmiU2ahcJd6FTOIWYEm_oVtQbLIHEn6DLiE6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fa9c53173.mp4?token=V-Qg8mIv9Zt2CCaivRmJmHob9NXJzsucDwGik-QVx2f9jCa5RODyoj3Efa8SjkE2q_umRsxDzFAJ4MKEZyZkex8Uwj0JEj19HNVd9xsVrjZm5TIkMwFs-zCmfh-Fm1FoTpv189PTmsjt-QP6Old4aAwUcdPbg8nw0T4RUR5rE-9eSIegvYDlONdHTMJjtjzlWPWHgGOh4rxS0MIfU9RcVTXyZ32qqX9oIaunQenAN614mdUdIEpBvxL_lUJSo62MrAQztZRbmzcO6zg1VzdYboqJR-1OkmzmYPOb068f1al3h9ASzNmiU2ahcJd6FTOIWYEm_oVtQbLIHEn6DLiE6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های عادل فردوسی‌پور در اولین برنامه فصل‌جدیدش پس از حواشی فیلتر شدن سایتش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105242" target="_blank">📅 08:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105238">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CakckxvlzpOjQOYKKV-DgNuolGiJ-M1mIrGnxCJGQ1tHTSDfLGODxOoOxnuNlk4dI9VsIa4PUUkJCgr1fSgQh7-nFUqRDvZnl_aa9QR4TY-AQtGxRzJ_f7tYOeLCWrVD9V0Mp5ygUPAY6E2ehqPZVOMrRFDBMLmU753Uq0cpRmUeCdJR_CAPwaMMi6JTclZlFdTkwUAPz3qWVp08BGmhN3ogjFOc5MOq82wDaA4K-lubD7-nFhJBi4HuQTsAhVrOmk6tnBmOLEM3wB68OBBe-BJb_uibXduEp6s1TCIz0paXD3pN5YButu0AD_2PrZuNO9LlTvmnB9fxS7NMTTc2vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلیك: 91 پیروزی در 120 مسابقه با بارسا.
🥶
ژاوی: 91 پیروزی در 143 مسابقه
با بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/105238" target="_blank">📅 01:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105237">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVjcAlRc2H_AlZk-LzdTIhazEKk3W7exXWdmlGHWmQ47vYqp8qRXR3tYBIMMH7gLQxsuouy1EVZWOtKobCVtn2ZUWnnySh02sgI774_IHPGebbfyzjaKXIHsZDwUFHM40wrHJVCJkXqH7UT6Afo6aRavuTOkvHLw317Sdps-oiiuBvECr3AI_4gPO9Fz32ivt4OgRYA433mXKzuznlfc26bSL9eQ0AJF_4soEc27X2jeWaWQe2dIKtpr7oVnc4OumAWKV41D2rNZg0323KsnmBdLu-B2JpLdLc8J9DJ7ItLwEa6DK4UupiWsNN7tLxcC1Ri97m6CrVZ16Bmlr3hjww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: مودریک از چلسی به تاتنهام با قراردادی قرضی HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105237" target="_blank">📅 01:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105236">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7XMmdYWjnc7sB4Lvu186qb0-z3yevf1Tt0Tpr_9DAx4A86NkslqyWs2YQlKVLcYkNTKiuEQcHfPfu7mlvKIB6t2TEZnGCc29GkZ7AHgr5kNLn60msX0BheN_cxPVua-U4FxqLhlbaCs633IBNXDq6Gbn1bAIRNkd0W5qzMSWaqqMwiSvhPhaRe03wlaPaKl8ZEPg3AErF88qYZvjaoTpEjyyMSd3DkeYrBePdK_NgLcxYjklo3YzLUAXgk0uEKcid9Ma-Tw9UCuE0jccHtDuYdRciJr2WdiRmCOF1_tvYFfLOR6ThoGZP-oH0B5_YXYmvqtQPNCSc0BymdZujH4BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌سوم لالیگا؛ بلوگرانا روی نوار برد؛ پیروزی پرگل در شب بریس رافینیا و‌ یامال
🇪🇸
بارسلونا
😄
-
😀
رایووایکانو
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105236" target="_blank">📅 01:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105235">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">لامین‌یامال دبل کرددددد</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105235" target="_blank">📅 00:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105234">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بارسا پنجمییییی</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105234" target="_blank">📅 00:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105233">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گگگگگگگگگل</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/105233" target="_blank">📅 00:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105232">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجار متعدد در سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/105232" target="_blank">📅 00:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105231">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی استون ویلا 0-1 آرسنال با گزارش هوتن خداپرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/105231" target="_blank">📅 00:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105229">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گلگگلگلگل چهارم بارسلونا با دبل رافینیا</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105229" target="_blank">📅 00:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105228">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
🎙
توضیحات پیام صادقیان درباره جنجال سایت شرطبندی؛ من اصلا نمی دانستم این سایت چیست و فقط تبلیغ می کردم، تا الان یک بار هم وارد این سایت‌ها نشدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/105228" target="_blank">📅 00:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105225">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گلگلگلگلگلگل دوم رایووایکانو</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105225" target="_blank">📅 00:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105224">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گلگلگگلگلگلگ سوم بارسلوناااااا</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105224" target="_blank">📅 00:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105223">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گلگلگگلگلگلگ سوم بارسلوناااااا</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105223" target="_blank">📅 00:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105222">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd706ab6a6.mp4?token=WGPI9eBE-nRDBjFFhYKwlE3cMnruFEO6ZRUK7FDx9JvXBW-s1b9LNsEJL2C0C5oJ56dJ2DFExpfkP2tDPdKtd-8UGVK8o5mC-M0GlVg0o6eOgG8ROwjERFdngOU1NN6zEHLBO5DR6Fa0PcWaUYuXouabsnMI7eqsUJZ1syCNS4iCeGdfLf0fTT4v5HkEwJgVvtTiMcx0zyThuwjIosLQBBjjgaXbWKOmSZDGhbVY-SSfKAk6kJGNj2216dXhpJdhuLu6yIX201V3tdrM1ymWNQIk1A2x_6O7bUY5XXVk9uDbWwn_L9icw7DMASSsj4JngRNB8VrPe8Rzr6rDpFEXlyG-s5lS-oat3xCgNTjDZlTpxfA2BV09iTytQh9QH7xMEUwtvDZ4P5mTAX4JSdTMkpKP5eh4KUYRTJO28mNJDL1qotFspJhEElUp2xYobTSNQnw2NwLSglpVhLN940t6ANCi4l_ykxvuXAwOj6s9bxxmd49sQA_K1qA-NI8lyvLTsqEORA5EsEa_HydbD1mEwQLOCzOM1A6aE7YkqyGv1eSdG7SlST78xIPcjTY20VooWvzsbidsdEDsgXo-zucpNcIqq5xldRZ0pmQezUNTJjFdbisSKGtWdGI5OGoHbt4YPPgepWAceg6OVKHtQvv-4pjdPsVzcuJSvmdiSuTUbQk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd706ab6a6.mp4?token=WGPI9eBE-nRDBjFFhYKwlE3cMnruFEO6ZRUK7FDx9JvXBW-s1b9LNsEJL2C0C5oJ56dJ2DFExpfkP2tDPdKtd-8UGVK8o5mC-M0GlVg0o6eOgG8ROwjERFdngOU1NN6zEHLBO5DR6Fa0PcWaUYuXouabsnMI7eqsUJZ1syCNS4iCeGdfLf0fTT4v5HkEwJgVvtTiMcx0zyThuwjIosLQBBjjgaXbWKOmSZDGhbVY-SSfKAk6kJGNj2216dXhpJdhuLu6yIX201V3tdrM1ymWNQIk1A2x_6O7bUY5XXVk9uDbWwn_L9icw7DMASSsj4JngRNB8VrPe8Rzr6rDpFEXlyG-s5lS-oat3xCgNTjDZlTpxfA2BV09iTytQh9QH7xMEUwtvDZ4P5mTAX4JSdTMkpKP5eh4KUYRTJO28mNJDL1qotFspJhEElUp2xYobTSNQnw2NwLSglpVhLN940t6ANCi4l_ykxvuXAwOj6s9bxxmd49sQA_K1qA-NI8lyvLTsqEORA5EsEa_HydbD1mEwQLOCzOM1A6aE7YkqyGv1eSdG7SlST78xIPcjTY20VooWvzsbidsdEDsgXo-zucpNcIqq5xldRZ0pmQezUNTJjFdbisSKGtWdGI5OGoHbt4YPPgepWAceg6OVKHtQvv-4pjdPsVzcuJSvmdiSuTUbQk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
ادعای بابایی مدیرعامل چادرملو: سه‌جانبه را برگزار کردند تا پرسپولیس آسیایی شود
❌
صحبت‌های علیرضا بابایی، مدیرعامل چادرملو، درباره پرونده جنجالی معرفی نماینده به آسیا/ رانت اطلاعاتی، دلیل گله از گل‌گهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105222" target="_blank">📅 00:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105221">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8MRe3TgT9xj4SDL2F8_7JigFuXmhRUPsW6r0KoNnJECyf4QxrS9VS_ZY4UMrblYoEJrwXEuGy5y53UOHj_tEb4-VNS7dnJCM1WfSwim5I9MPPRXPh0cVV9RwZ0ImMGurVMge5xKYoSDgbOIdi2iU6XEoEFRoIkMYC2vnxQoEh51j83QKUJEekR8ajwDiQfK7YBU6znlW4IbzoRJ53oRegf82tLNOqZS5TuI8BsgIqIyWKCVrL598MEbL8LsKaUlsNFyNCHyhIZyFam70XqUdWY29cgW_x3ayRVcaU90prw0m_3JZcS5CeTMnqs-PFY5wc702kKaohPg7FnEA3UvVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
🇮🇷
در نشست امروز کمیته داوران، موعود بنیادی‌فر نظر منتخب اعضای این کمیته بدلیل تجربه بالاتر نسبت به کوپال‌ناظمی بوده و قرار شده قضاوت بازی روز چهارشنبه که حواشی بسیاری خواهد داشت، به بنیادی‌فر واگذار شود تا بازی به درستی مدیریت شود. هنوز تیم داوری رسما…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105221" target="_blank">📅 23:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105218">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گلگگلگلگل دوم بارسلونا لامین‌یامال</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105218" target="_blank">📅 23:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105217">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گلگلگگلگلگلگلگ تساوی بارسلونا</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105217" target="_blank">📅 23:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105215">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گلگلگلگگلگلگلگلگل اول رایووایکانو
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105215" target="_blank">📅 23:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105214">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1302c5c0.mp4?token=JXHWEbKBit3zGFQbDRR2IZOlAkXrkIB4A2opp4YvArRE_c_xMoH-USmR-ZHEW4EL_iffFG78iTml8Qi_PkpQ1WL_cwcbYuxDFdAbl7tw_SWM41DyeJDMpTKmdLKbBzd6DC7HObct9WSMbTJ_EoKqL-ECOKZII1w-I-y89Mkcax7hIuAk4HQQU_8bGjh__Ox28V2WVRmS4ITN6FKjR29daxqP4ApPLeLLGNTwY1zruk2fSYxIzIaSjH28Mb1_hbKcm5vqFFw3YzIv1XqMqH02BTl2AHlcPKVBUz5TtuLnm806TqOs8s8yYpWvEmnW6__VoRDHsVnJqgcVgwZOTmzVAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1302c5c0.mp4?token=JXHWEbKBit3zGFQbDRR2IZOlAkXrkIB4A2opp4YvArRE_c_xMoH-USmR-ZHEW4EL_iffFG78iTml8Qi_PkpQ1WL_cwcbYuxDFdAbl7tw_SWM41DyeJDMpTKmdLKbBzd6DC7HObct9WSMbTJ_EoKqL-ECOKZII1w-I-y89Mkcax7hIuAk4HQQU_8bGjh__Ox28V2WVRmS4ITN6FKjR29daxqP4ApPLeLLGNTwY1zruk2fSYxIzIaSjH28Mb1_hbKcm5vqFFw3YzIv1XqMqH02BTl2AHlcPKVBUz5TtuLnm806TqOs8s8yYpWvEmnW6__VoRDHsVnJqgcVgwZOTmzVAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
در اولین معاینات پزشکی از مهدی ترابی مشخص شده که این بازیکن دچار پارگی رباط صلیبی شده است! معاینات تکمیلی قرار است امروز انجام شود و نتایج آن اعلام‌خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/105214" target="_blank">📅 22:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105213">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇷
مصاحبه‌های منتخب هفته چهارم لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105213" target="_blank">📅 22:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105212">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/782a933b7c.mp4?token=PpsdLgFjX0YPlCZAKQXcaWWhH1nlf_B8FUpJGXJnSx1feOoyPLgIJfbG6GED7TyQRfDtnsiT1ABWVdxdsLyaZvTSfOQifbuMdBtAoke9yiE8T0omBU5ofLFfkvz8xn5uHdGW1WSZNy6efOvtbZAB5nhSUM-vnCz4Ujgv6oFQ1_w3c_734g2qJnV7rcaDk1xQyLLZESl6zOk64RMdfIalPVKwT81PvllMBzeCumuZtb_TfSDtmSrZ5T7I626ox4wjFsJrE2ZFNdDapWxdkUauUugXyi-_IN8Bdj48vvHzvzv-GSuEm6XZajqxDR8ioaV9nVhHRHOOvQAqocf_hfoJaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/782a933b7c.mp4?token=PpsdLgFjX0YPlCZAKQXcaWWhH1nlf_B8FUpJGXJnSx1feOoyPLgIJfbG6GED7TyQRfDtnsiT1ABWVdxdsLyaZvTSfOQifbuMdBtAoke9yiE8T0omBU5ofLFfkvz8xn5uHdGW1WSZNy6efOvtbZAB5nhSUM-vnCz4Ujgv6oFQ1_w3c_734g2qJnV7rcaDk1xQyLLZESl6zOk64RMdfIalPVKwT81PvllMBzeCumuZtb_TfSDtmSrZ5T7I626ox4wjFsJrE2ZFNdDapWxdkUauUugXyi-_IN8Bdj48vvHzvzv-GSuEm6XZajqxDR8ioaV9nVhHRHOOvQAqocf_hfoJaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لحظاتی با گابریل‌ژسوس خرید جدید بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105212" target="_blank">📅 22:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105211">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5TPbvGckzu37P3bMEz4X2n_3F2BhzvoKv0evw1xCMoZWbfbHaLTf74r0PVej-T7feR2zcZqErxuqxmBkfNFGmzHXU2tYkuVJnajzX1C-yErag3V-YrikimDXsgKaLdJ_H88JjV6fsOMouQou1s6CFk_ymCtRv28ufacwdM3ZykXeCmDcTyeqKyBWmOqEznW0YA3qBbKLdL-4HTbHkNDiHaRjz76WnZKpBidNA5YuU5ieWPKmW917fe5fjT0lwyHgXs_jXEQxFx5eg4DsXVPZyph8kxYQOzn059dwPpvbB5nGapMJilj_G2_2fDp_hIxWxGanRjaeJiOQk0gCFFN7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: ایلمان اندیایه از اورتون به منچسترسیتی؛ HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105211" target="_blank">📅 21:51 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
