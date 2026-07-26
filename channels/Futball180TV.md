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
<img src="https://cdn5.telesco.pe/file/tRDeUf4nd-Hd2dQli_4ieI5g3K2y7QIDthao4l0wpJEiRhAPgQmfqD0tQpclN2B8KMteoXTmcIFCWwQ3rYFWJX7kBPaSpOyUIuWt1xLsSkYi6DTpx1W6gLgcJbY5Y314h_tjhRgvrwLW8mdkmYD2gChVXAN0XDwEWnH7NgMQ9HeNCnwwsAw3xWG6f1jBCyCtu37CDRltWicqak5h0aLXisJdgJ-C8jLcOAaOUyd0kYAONl5x354HcM6ejViEfo-jH3w9Wz4Xi8IGvmySLS-aZobiSoomXW_wlsTVkTK8pIvarPN2p7so0LG1kkgZrnAJamWvjI8gTaRJUvlreJ7mXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 525K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 23:39:17</div>
<hr>

<div class="tg-post" id="msg-102033">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=dCZ-T5VzxtsTbZ7By1V1guxkLG12Cjqt1-bSLFK-PaGXf2rLbFPqmB4nkq01XdP1ZoXS1EH6droN2ImsEYiBU3r1ee8iCYLCX3t4iN41nCnc9PkyA4GXUWcBdQKOiyjUIWwKQLHHdgO9_Zpgw-KsJKw6iej0zVeAoKX9zGmDYK1D3LKRLHcafx0e2LGJxvGS2wi02bZkP6p_KlKPMGEfqduO98Vt-hpBZ7Q5iaFnnmzjJmwrJl5jbh5K1kr7yJYDmzyslw-dUCA8FGz-jI5twHcNbySmX9Xg_8q94qj7y_zyHAAYYr-lCBY-O9DcFP4brtOk2UFRyOySjaR1E1KXcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=dCZ-T5VzxtsTbZ7By1V1guxkLG12Cjqt1-bSLFK-PaGXf2rLbFPqmB4nkq01XdP1ZoXS1EH6droN2ImsEYiBU3r1ee8iCYLCX3t4iN41nCnc9PkyA4GXUWcBdQKOiyjUIWwKQLHHdgO9_Zpgw-KsJKw6iej0zVeAoKX9zGmDYK1D3LKRLHcafx0e2LGJxvGS2wi02bZkP6p_KlKPMGEfqduO98Vt-hpBZ7Q5iaFnnmzjJmwrJl5jbh5K1kr7yJYDmzyslw-dUCA8FGz-jI5twHcNbySmX9Xg_8q94qj7y_zyHAAYYr-lCBY-O9DcFP4brtOk2UFRyOySjaR1E1KXcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
وضعیت این‌روزهای لیونل‌مسی در تعطیلات:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/102033" target="_blank">📅 23:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102032">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0SzL98f-p1xRc9J3ivfPtYtQiv53Depu0QX44KBvUb3UcsQUoN_M6s3LqXmssimPK7Mtou9mjDza-LHUHAHEEBHughAvZY0uVWeB1xiaem-wspzuJ3YmsO9W4Gkb_tIO2iYSu9zxvOLFZQ0WkG2ZO4zbhbNy20XvS6QIcX_L_MIq0rqzu5nf8bjNLO6CNvDBuI-6CwFdywjKk5__i5rTaS55dakYgI5s8rSsd82-f9jKY6NwPqp0BU2BR7uuU6AUQmGEyDpopvhNNnpFfzPDgHPnDcEte6yT_4oFHCohSvzcvb1Z6X7Hz4JMXRe5EPoqk-h6coyIOJroCuLKJyX3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📮
🇮🇹
دیس فلوریان پلتنبرگ به رومانو: بعضیا همیشه میخوان اول باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/Futball180TV/102032" target="_blank">📅 23:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102031">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUxIlRX8zuSMpcS1Ajlm6MLt3Q9Pl4QgU30JfZBLev4xpHQzTZWdcMg1x429Si6trJTywi_u-gybyO2kgICr6fexMdYVHQItv8JaXJgRp8smcKy1Y1sLj4UA1Uydvr3jMyaQ7_zhT6iXMhx6o_EMttg6Ujug_VH3kKtPqSZso5Zml1ocN965qQ1gIaHEG-tI1JLCHuR94V1ZAsVT9JNCS_QCiGDGaotTW9zYDFgidFhqx0ZhL3UmMwS6sGNniJTeWLYUzbSf0gTJA_5y9Gx3JNd0glPZK8d-3DXNO9VeYbrwQEquO3HcP8MnoA2hlQsucadjuRC3c5vEqICi70xGsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
فلوریان پلتنبرگ اصرار داره که هنوز هیچ توافقی (حتی توافقی اولیه) بین لایپزیگ و رئال مادرید حاصل نشده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/Futball180TV/102031" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102030">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/Futball180TV/102030" target="_blank">📅 23:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102029">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=FRssKzQhuxaVfBREX2ueCtI_hTuAHubwHFgsqOmU0irBXAy8GP7gC9yBuyf80exXTP4XFJbgBjxK7i-XcTtIyWsQeGRn1Kipg7f7ODtnWEQHN_7iVHq1NZOJK9quhTvciT_Nl7b6kyNAuUt7v2R3qw0B1mvHEMzuths57XbLQM_w8Df9bFPJzk2yZb-kXn6Gr3XmLLiFx-ObGM5IQC50pgfE6M2CrMZFQXL0SpwUnFKgGJmYmE3K4CSzZhshdSrJTIc8zaQOlNvnIyVU0Ca7lpVRH_u3Zi4x2_ngl6i62PtH-BPmYpctHcH5JerLnVTm0K0RdwV1w0BMxgjJ8830Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=FRssKzQhuxaVfBREX2ueCtI_hTuAHubwHFgsqOmU0irBXAy8GP7gC9yBuyf80exXTP4XFJbgBjxK7i-XcTtIyWsQeGRn1Kipg7f7ODtnWEQHN_7iVHq1NZOJK9quhTvciT_Nl7b6kyNAuUt7v2R3qw0B1mvHEMzuths57XbLQM_w8Df9bFPJzk2yZb-kXn6Gr3XmLLiFx-ObGM5IQC50pgfE6M2CrMZFQXL0SpwUnFKgGJmYmE3K4CSzZhshdSrJTIc8zaQOlNvnIyVU0Ca7lpVRH_u3Zi4x2_ngl6i62PtH-BPmYpctHcH5JerLnVTm0K0RdwV1w0BMxgjJ8830Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره فوتبال مملکت علی‌آقا دایی
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/102029" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102028">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY2JFDMzsbW8L6RRvY2qUxmdkdLjQrEcu_-wjNMgoQ-H1EpXmsmMYpOvR04_WdK53Wekoo2HSiWu_IL40Ytkt14rb1zI-6uxs_z6Jcr1qtA-4y31kmE3bk2FF1ePNuBZ5-Exm7EHQ7qkSwdPHSfjqzcKpgI__5l_W4UkFLFErq_sy1ex53eaXhVoUtWFkP2BJonrzR1ZD4DZG_Rm_iAFdMOG5CfVkPLKa2kQtN15iFlqLMxk8-4I7XE8CNt0-c6_bH5EYUwhRElKHJx_BFRzz3D1Dnhn-cvYuxERj3Lx3lJ2hJwBqizJ6r3wgitJ2wJKlmTys0tNICQ8nJSx8Sv-XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👀
رومانو:
🔺
خرید دیومانده بیش از 100 میلیون یورو برای رئال مادرید آب خورد.
🔺
مدت قراردادش هم تا سال 2031 هست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/Futball180TV/102028" target="_blank">📅 22:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102027">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xt_XajTURcDUD5hbNel_ZBCYMlP-EwDCo5PRi3h1LGZ3GtIUQs76eHvaHOFfqim5DExA8NidvudbtcgSK-2r5Uz2Ys3i1XAjihA-4vdunSOZm-WtM5bO8ItpMabUim870jPYACMWDzOa441nMN7vs4fNUdSTiwaQDQsSAC1r5Wgwd0rON_CQktnqL3ntYR5zh96Go0Cx_bze5cpU9DufD33szDjIL74Bkr631d2hY2wYZXooIKcmdBz8r-jIjw8QH5k7g3wNcBKR8eqKJFXfAzWJdIR0NzjRfYYtR8ZFOcknfPansDoEAa3i6t9WPBvwinwPs6riNn05RKyNspTtHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار پرز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/Futball180TV/102027" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102026">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/102026" target="_blank">📅 22:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102025">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tofSIsTrqfLcoSC9EJsV_ErDB-Niej7QCFYN197iX-b_UDhbQ_0GaEyHTfGdXmspPhuqfBVSjzXtOAcpQ3tvSgxsHV_9gmSxH4KMbEgc45Y0ORLL961rswsPb7rabGOBhU7Au8O6xiqAo2pJi42ohX8x1JHQToJwuvS0aZVooVZ1kAiQf5Ntd5bkvjXj5xC8f0Y1yZckWu-aeQTkWhTZapCe1m0a68k1kqJXRp3Gfa1RbYWQ9U3_hzaMXVz3_ePiWb7XERiMgI7NP4uEkWv0JCJd7cihRb8QIDKjB0V-DAUCcKF4-_MS0iT0aBt8DDmbp2MyTxJ3jnnXbz8k65_3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
اسپورت: خولیان الوارز گفته میخواد یه قدم دیگه برای پیوستن به بارسا برداره و بزودی انجامش میده . نهایت تا ۱۰ روز اینده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/Futball180TV/102025" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102024">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpA1myXDX3jdUpo6PspsHbMq1k-tqiJpN3mGYBmwD3XoPoJAJKQhj1XYjnnVTHMsOvMCo_oXQIJwxiLPDz1gjIFvRdUf8nJ-fjM4OjjPXlSBv3eVgK-lBBLUixBIYGrkfXYC73jihtoF73sBApDjod1oeeU9JTwrzcvFPMq9vJwkjMNb3JjaWT2VDBYFbM-Ydo-8J3xcdqdCs72GyYoPu8yrXfv72Rw0AnW4SVubAUlpcN_OFT05tIRefc_wQo27ZMC7pVrJIxPwbE0qRHH_8P5NdAoGJ-T8lJEYu7W69RQus2pIKL066_CX75Xi4AkFsGKK91VQ8NdEXZTubJGchg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی
از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست.
𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/Futball180TV/102024" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102023">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=BbDyRDe2uaPqO9h_XTou3bFQrZ4JUgHDPZdBDaTVkPAxalp9waXzT0xoB3CacwpV2XNSQZ9UJqS_azxz7pVDSw7z6R7PjF8EzwuJ7nFK2dUVvsaHbw0SJ7fUA62T08kmED4XHITlmySChw9bx4dVGtWbW_rn6i_jXeq0K91NQhAf6giXZrj9OJ5v-EOqJY4MSyvuqWoWYWcYm3lnE5I3S1I8hLTMqX1Z413MZhqfmSvDpLYWcsr8TBKFMHr6A3fGsWEHppFmFUnMl0FHsjjg0yDCMPyKnr--Mt8aEVVaUBRl44kdYUmoBF-tJtOlUMlQ1wtcw__jh1vk_LgnKWoWYylSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=BbDyRDe2uaPqO9h_XTou3bFQrZ4JUgHDPZdBDaTVkPAxalp9waXzT0xoB3CacwpV2XNSQZ9UJqS_azxz7pVDSw7z6R7PjF8EzwuJ7nFK2dUVvsaHbw0SJ7fUA62T08kmED4XHITlmySChw9bx4dVGtWbW_rn6i_jXeq0K91NQhAf6giXZrj9OJ5v-EOqJY4MSyvuqWoWYWcYm3lnE5I3S1I8hLTMqX1Z413MZhqfmSvDpLYWcsr8TBKFMHr6A3fGsWEHppFmFUnMl0FHsjjg0yDCMPyKnr--Mt8aEVVaUBRl44kdYUmoBF-tJtOlUMlQ1wtcw__jh1vk_LgnKWoWYylSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
آنخل دی‌ماریا: مسی نشون داد که یکی از بهترین‌های تاریخه و تا وقتی که خودش بخواد میتونه همچنان ادامه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/102023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102022">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_ita4ixEJYZOJq6yoLCs--evlJZ_dMw23E7cT2kcRVbaeC5U2EtQHUlmSIOkE57bbkwvdBn8wtEaOdkuO2C88fSJHN4AsqTQq2MElKTinqm3R5-AQyWXiwH0eEc-D7DkiX8444cB-0qBTW-PVkxE7w43-FOjgE3RNa33oxn0lAgeBib_FWyRvqp7KgFAtrqiE7VIBCNUUUJqYvTmEe0RG6jPH1kiPGr4JM0c2sDZechUq6IZ9locLS8T_TQ4TlMKQJzXAcbyJ2V0_6cEcXCVfQf5ButoCwHRXB44SGisQqvcHOJvFt2igOvtT55pRdZj4iOXaWdzEnDgn8ueVSAnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚪️
عمق اسکواد رئال مادرید برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/102022" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102021">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KC-GqpSn9n8otiyt60-JC8T44SBQrJVBimRxUpRw18xz9cV3Zt7pMy3LuzfsarNFbqJBkyK3_Z9-U0I8uawpK6xq-d2eSilQSgS_8zWeN1fRQCt_pEaPpUC19khUOEkNjB5z4Fgbchn00xu_T_Q7RiegBxW-2QNJWsnm3f1tgISlgCNt5vOVzcSDQ7z-oI2ssgunDUJkKBvwRlo_HyEhP-B5Ik_Xwt16Mbug5jZ74vRzcUE3Y4DDHcW2skb5wOv4HUy3RuETqLbV6Z7UtfsXjrz1jWX5IfqyoZVbI41zTjqLajYY4YrD4OdAk-VyjFWyQAhgDXxt3Z0XBGWIVG22F2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KC-GqpSn9n8otiyt60-JC8T44SBQrJVBimRxUpRw18xz9cV3Zt7pMy3LuzfsarNFbqJBkyK3_Z9-U0I8uawpK6xq-d2eSilQSgS_8zWeN1fRQCt_pEaPpUC19khUOEkNjB5z4Fgbchn00xu_T_Q7RiegBxW-2QNJWsnm3f1tgISlgCNt5vOVzcSDQ7z-oI2ssgunDUJkKBvwRlo_HyEhP-B5Ik_Xwt16Mbug5jZ74vRzcUE3Y4DDHcW2skb5wOv4HUy3RuETqLbV6Z7UtfsXjrz1jWX5IfqyoZVbI41zTjqLajYY4YrD4OdAk-VyjFWyQAhgDXxt3Z0XBGWIVG22F2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
امیرحسین صادقی: وحید مرادی من و فرزاد را در هتل المپیک آشتی داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102021" target="_blank">📅 21:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102020">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZD3ijjJ1aTS24mY_Rygmr4WOXMKvks_TS8LiZB1HPwvMrUGGCAIRcE4dK_LydXoB9vqP9JYK0PHYDsBU-FuYI_DVyy06rQVHvkq4EQmeru2oNqjH_jm9fdWfVVKqiFMgGmiQxT7NW0HDrCBwDd7CuoK1jCHGup2wMGjpWlSMuyryOLj4WzhKrybr3oWdz-jXRD4oqH5MWvgizyh5v4JSg58CbLXZRpb-6j6tZj5ZA4wjMRrNKzuU5YLbTWedS9NUeUOtY543W6Dw5YDJrztmpnnEigaO9wFMGUOPhQEM4WRjA-eBFaqq59CTX_r0apZlS5GEPdqwq4Der2bocmcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🚨
پژمان جمشیدی که به تجاوز متهم شده بود، در رای نهایی دادگاه از این اتهام تبرئه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102020" target="_blank">📅 20:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102019">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPw1aOMjox-UMnzZshTqh9WMW_7YcLHigq86U-jGYCeJuwmqGBzEhcB8DmhQhMQJAlOZOyRAJSDg7y-6N-zHA5fwa8hm8UVHZTsPljXGilaqkkDPCdXgAovtxUeu1Br3ZqXJqF35bVBG7OZqp7CFvVIw62JuwkvQPF9MYK9zTEQjNDvFguJ1jtVNkvbNAXu2pUrSQfB37nEaUET-TL9BDGRJeYZNsT9kfV9P3pjeseHQD4Uny-MTEcBGFKrlx5tdbWtGNl4P9CDnzNpym1mKUDLuZT9v2YcZALJV0xX1Il3cSgYidJ0PmmbDSrQO5lncA7f4ZtH32PAvVGTCFF4r1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
آرانچا رودریگز: انتظار میرود که یان دیوماندی این هفته به تمرینات رئال مادرید بپیوندد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102019" target="_blank">📅 20:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102018">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHb3DupinzCjKs9RTEj2uFaUU6B86fV0jz-5D2WGqLU7Z1rT6eoGCI-4Dpf-eiaVJeMfRKTQgguYxnZDupNMX_W1Tf9V5l4OAzQBJQbUt6bsiXsNJjAuLHogAZLIFV6vtsSTsfRZqXpGtRU7ZNgskp_u1wolQwJ8W2ly-QcvPGpzMaCVZKgi6Gc0y09BGZA6ogHmK9P9Ui2QLfKFdU7OnLG9EZ-R_JF-NYlIxThsOtPe9iQ1N0Nk103Z9FPhobfkgvtPeu8-FSsdM3IB-8AOJh6p2FgaCWX1p5A24VlDFddhGp2b1YT0Yv9cM7iGkbNkRXJgEhRHD4YBw67eoA_KgtEuY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHb3DupinzCjKs9RTEj2uFaUU6B86fV0jz-5D2WGqLU7Z1rT6eoGCI-4Dpf-eiaVJeMfRKTQgguYxnZDupNMX_W1Tf9V5l4OAzQBJQbUt6bsiXsNJjAuLHogAZLIFV6vtsSTsfRZqXpGtRU7ZNgskp_u1wolQwJ8W2ly-QcvPGpzMaCVZKgi6Gc0y09BGZA6ogHmK9P9Ui2QLfKFdU7OnLG9EZ-R_JF-NYlIxThsOtPe9iQ1N0Nk103Z9FPhobfkgvtPeu8-FSsdM3IB-8AOJh6p2FgaCWX1p5A24VlDFddhGp2b1YT0Yv9cM7iGkbNkRXJgEhRHD4YBw67eoA_KgtEuY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنتا سوپرگل قیچی‌برگردون ببینیم تا روحمون ارضا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102018" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102016">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/disIQeNdOJg7MHZUyC71gJkw-IapSdHKNQA7-rTZTOQQSKu9G_wfZGDAi6uESJvWHxH31-_4k5ZX4uba45v_N6Rhf0txg6ypDf5j6fktDinaXmnBNAFjbqOlSJpfi33GadOBQpfoUPoTVTE2C-DHW7WEJyzZ11YvejWdSCTv6xDUq0xNpVPZrny9kpIIfJ4PbEdcEJpAA17WEjRNAm3_veFOotF16FnABl6fZM4DmFjb88oTNVEF8A3b__TQ5GcuYCHRQK6FWFOr0y8tQuIG5ih7y87D-9wEqho1fOAZn6yCDl67mUZvoj-k7ZOPLrrgWSjCQEaNiA0M0oCPnRiYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZiSM61rNXzVDBm_uDKlBrFmk7_tJl0MRr2HWVR5dT2VzGk5loe0lIPOmJJ1z7q4XJ9cV-2EuzSfSmHXyH-M6B8raGmvoUrRriB3StyCPPy6KSv2DV4SV709MOwyxElcifDwqLF0OYgjRtKGyAoieZWqfeC00ulob5xp2OcFEbhD3yPZFwb7ln73iLe9BI684_DOudqAoxFspmtLAAs6qJyDT1ev6j5Ea1YcNM0nqA4RvUFCoBtHWnMLzjRITedFlV1ONshKhmIFTc5Ct_V07H40OYV7fWcr5E0DplQDf92L5FCi8L333Dbvg8EUc91s_zJKLb0RNJHk6zeIWwdg7CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
لواندوفسکی:
شاید مجبور باشیم ۱۰۰ یا ۲۰۰ سال دیگه صبر کنیم و منتظر بمونیم تا دوباره بازیکنی مثل مسی ببینیم.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102016" target="_blank">📅 19:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102015">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGaumk_K7w6fdIlq76rrHnLn9LhL-UNL70VNkEXLuO0JiK7WGNqjU3uMO07uhSXFb6viZWDVJSjwed1nhy1N_1sAthqQhZyBQjCTnHEm7jpTzLpLgN-W3VpWQEAYg1qfSCX58X1WfrpAsGhl16S_YoASvbIN2k8ngXjidAWTxySq-Sy1IK_KSY-CrBGFQNlIrJWlLqihHv2FcExslHtvcz0SsPR8nhOsrq-StYzJ5ZpcfASgDDtPT9ZjyNgrvCyCf2CSeZxa9wUhhSNYqcMmEAPlG_8LwztaSq3CqznQi7mB54V2EgzBdpfjvpumyNtsGGqBxRVzMJk8WXDZ0twAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
گران‌ترین انتقال‌های تاریخ فوتبال با در نظر گرفتن تورم:
🥇
رونالدو: ۸۰ میلیون پوند → ۲۹۲ میلیون پوند
🥈
ادن هازارد: ۱۵۰ میلیون پوند → ۲۴۵ میلیون پوند
🥉
آلن شیرر: ۱۵ میلیون پوند → ۲۳۸ میلیون پوند
نیکولا آنلکا: ۲۳.۵ میلیون پوند → ۲۲۶ میلیون پوند
فیلیپه کوتینیو: ۱۴۲ میلیون پوند → ۲۱۷ میلیون پوند
پل گاسکوئین: ۵.۵ میلیون پوند → ۱۹۷ میلیون پوند
مارک اوورمارس: ۲۵ میلیون پوند → ۱۹۶ میلیون پوند
گرت بیل: ۸۶ میلیون پوند → ۱۹۲ میلیون پوند
استن کولیمور: ۸.۵ میلیون پوند → ۱۷۹ میلیون پوند
ریو فردیناند: ۳۰ میلیون پوند → ۱۷۵ میلیون پوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102015" target="_blank">📅 19:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102014">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=qGdI5Tc5W7dCEEp78-c4_BH9LiLoqcflXId0tLsRI0mGwAKmwcKctEbmKcsj53B5svpWCxxie_PzhmRapNza5eox99AxxWyIDIUVt1GQzPevtdhRaG7a-mrDZI3d_7cuEzC7niE2LNG_MWGxWCC_ZiGU0aoEcidTCwAoMN1g0cep0ngGSJJP1PEW9-yg9pen0cgjvw2IWEIp2KA7rZO9_4F01ryLmUglevmknJ2y2M6cZKG8W9ehTeIQ0nPwI7vHLPtKEi33EjYHXFcFSPbjR6Tk3dSPv94Is32WQIiUrUvrYUhBM02hRouxT25-TD7w073jZdKM4YR3rVidj-fbAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=qGdI5Tc5W7dCEEp78-c4_BH9LiLoqcflXId0tLsRI0mGwAKmwcKctEbmKcsj53B5svpWCxxie_PzhmRapNza5eox99AxxWyIDIUVt1GQzPevtdhRaG7a-mrDZI3d_7cuEzC7niE2LNG_MWGxWCC_ZiGU0aoEcidTCwAoMN1g0cep0ngGSJJP1PEW9-yg9pen0cgjvw2IWEIp2KA7rZO9_4F01ryLmUglevmknJ2y2M6cZKG8W9ehTeIQ0nPwI7vHLPtKEi33EjYHXFcFSPbjR6Tk3dSPv94Is32WQIiUrUvrYUhBM02hRouxT25-TD7w073jZdKM4YR3rVidj-fbAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الگوت کیه؟
دیومانده: رونالدو
رونالدو یا مسی؟ مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102014" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102013">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=rRa6muO8xH7zo6sJudkRl7_bXI1ZAYvYtGf1ONPrHxkoeqXHbY7aOevxdRlP0np9QX6Fdxlndp732Ez_Dl4HUb6sklyx7eshA53glxS1pwDDqr6oLZu1G-cqSZUF5hloZ83HPhGczh2D-6FsMy91VWYyJ_U6wtUIp7cFjtw59UImFhCNT7ND5jEQxF6TuervxPdWcjBCH6JKwk8G-WePTN6kB73aC3QDFkunpvewXe3nAyVD8bgm0YxilIWIe0VvQcqrIDaohzqUCL46IjLiSo-WF5hoAsrN3JKL9fOrSFDGN4dg_YbGOwwEabo-aDW2SlI6BUIDPGN39418mSblzotd_ofi-LdkOYYqtvj4WPz0B48WF__T9CTzPljqUC7ZP4EbGuZxgNzXk8325H4fjuqQqBBu2264k1wdDdvtoDTEGadXg5mdC0k7usphs-IiJyKc_OU2Byj1MxNDB92BY3uCXFHExYyvhfmLeVLSKgowMo4j1Fr4wxKnRkIAPeVjxP4ipKYnVY8MLxLFQEq8wd66ChR1n7kyrW8y3TgB7LvYyl-Gb17PUy9F2mnKy024IDW30y7EuWGG80HnbjUbdhFDKGMLzrIgtTjHOoNgKRRW0c1ZYfBUpP8YuIKjZLaosrXbIECmKvuzdDwHzBCv1bF_LQ2ghXCzsUMB8g3nVAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=rRa6muO8xH7zo6sJudkRl7_bXI1ZAYvYtGf1ONPrHxkoeqXHbY7aOevxdRlP0np9QX6Fdxlndp732Ez_Dl4HUb6sklyx7eshA53glxS1pwDDqr6oLZu1G-cqSZUF5hloZ83HPhGczh2D-6FsMy91VWYyJ_U6wtUIp7cFjtw59UImFhCNT7ND5jEQxF6TuervxPdWcjBCH6JKwk8G-WePTN6kB73aC3QDFkunpvewXe3nAyVD8bgm0YxilIWIe0VvQcqrIDaohzqUCL46IjLiSo-WF5hoAsrN3JKL9fOrSFDGN4dg_YbGOwwEabo-aDW2SlI6BUIDPGN39418mSblzotd_ofi-LdkOYYqtvj4WPz0B48WF__T9CTzPljqUC7ZP4EbGuZxgNzXk8325H4fjuqQqBBu2264k1wdDdvtoDTEGadXg5mdC0k7usphs-IiJyKc_OU2Byj1MxNDB92BY3uCXFHExYyvhfmLeVLSKgowMo4j1Fr4wxKnRkIAPeVjxP4ipKYnVY8MLxLFQEq8wd66ChR1n7kyrW8y3TgB7LvYyl-Gb17PUy9F2mnKy024IDW30y7EuWGG80HnbjUbdhFDKGMLzrIgtTjHOoNgKRRW0c1ZYfBUpP8YuIKjZLaosrXbIECmKvuzdDwHzBCv1bF_LQ2ghXCzsUMB8g3nVAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگر قصد دارید سفر اربعین را با اتوبوس راهی مرز شوید، پیدا کردن بلیت را به سپاس بسپارید
🔹
سامانه پایش آنلاین سفر (سپاس) با اتصال به همه درگاه‌های رسمی فروش اینترنتی بلیت اتوبوس امکان مشاهده و مقایسه ظرفیت‌ها را در یک سامانه فراهم کرده است تا سریع‌تر و آسان‌تر بلیت مناسب سفر خود را پیدا کنید.
🔹
از ۲۷ تیر پیش‌فروش بلیت سفرهای اربعین آغاز شده است. برای برنامه‌ریزی آسان‌تر سفر به سامانه سپاس مراجعه کنید:
🔗
sepas.rmto.ir
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/102013" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102012">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102012" target="_blank">📅 19:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102011">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCUjXKE_6QSCWDkO5tZ_u1_scJEimc7zdcjulMuLpXlFqhUvxaxyoNiJfFCZob7uJg7qK4LGYIBCAVmpSa3GwpuHnwhzBVCdnHFVYv6F_A5_uiN5ZOG8VrCscwq-QEX330_UiBPKJanuO8AobDNUlSIkVvPDdxakwGYKBRKzIH4rCvL-4KlFvGDxBhpylUJusIfiXacSjiQuskwOmxJExlZmZI_z3bp1iSTpfU6ZMt0WZ6lRYU4KBWXNMKPmn-eQHaYSR-q7u3AUnDAA-akMQfL1ThJyjGMAJbEfqx44FpWYLecCIRXYD8E9rDg1alqiZFN10zrI-U-Xa6t5F1rgog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102011" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102010">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/746abba13b.mp4?token=mqYdcIYIzVyM9bDqsdKHcKy_xjiGNA7B_L5y_PpEEshQsO6F2aB_Gy7aLImwU0QDoXJy00e8DPqtXuLIF9ZgLcjWojmAMebyEWKrp4lN3UdNP33b3i1Ky-tEFBP0tl5DSVJZKdrl5nXxrIIm-Yr6JrTX_oal_YOji5Bn3m1b_U3Ov8iJ9oj0hY40NiS3nL7ZY8922BnY4k2HRnKlZz1eJbx2koxerZ9hYF2w7YGakhhk6MKWvH7bSTt6fwrldsVnfao0lDmARpmLRLvOJqOa8RhXKrrNdBWEJq1NWalGar5YsSeYTCnJ7OfbRcSUhsnWFtsroakwfH1f-TeAlGXY0kGiVdNHGYr_uHyUkfN0VmJtZSa-3ZdZ2bcvNilky1kx-pWIPxMjkan_Zd_KI3A58bBcwZxWZ9P8oK7QjcDp82-s5b_j1mnd4MOrGtnaXbzYV6FCZOj-E3eavlnkovqOV0apEquP-2t5XAmBErCB2VzeV2eH8lGCeWym3oGjVpb2d0X02sspiA_1xwaypu50f_s66BAb2cuEHWqcI-1v9ra1qqv310j8DJfwdfDdMGS0IEXX0S5KrXjGCzJve3xa31LPKajVab5wNtFXdYJ0sCJL9zzEAcnyETcWMrxw6LyMs6X5OHhhnWJmJ-OisZy1M73sWzMMO78T7FLdFA50Z5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/746abba13b.mp4?token=mqYdcIYIzVyM9bDqsdKHcKy_xjiGNA7B_L5y_PpEEshQsO6F2aB_Gy7aLImwU0QDoXJy00e8DPqtXuLIF9ZgLcjWojmAMebyEWKrp4lN3UdNP33b3i1Ky-tEFBP0tl5DSVJZKdrl5nXxrIIm-Yr6JrTX_oal_YOji5Bn3m1b_U3Ov8iJ9oj0hY40NiS3nL7ZY8922BnY4k2HRnKlZz1eJbx2koxerZ9hYF2w7YGakhhk6MKWvH7bSTt6fwrldsVnfao0lDmARpmLRLvOJqOa8RhXKrrNdBWEJq1NWalGar5YsSeYTCnJ7OfbRcSUhsnWFtsroakwfH1f-TeAlGXY0kGiVdNHGYr_uHyUkfN0VmJtZSa-3ZdZ2bcvNilky1kx-pWIPxMjkan_Zd_KI3A58bBcwZxWZ9P8oK7QjcDp82-s5b_j1mnd4MOrGtnaXbzYV6FCZOj-E3eavlnkovqOV0apEquP-2t5XAmBErCB2VzeV2eH8lGCeWym3oGjVpb2d0X02sspiA_1xwaypu50f_s66BAb2cuEHWqcI-1v9ra1qqv310j8DJfwdfDdMGS0IEXX0S5KrXjGCzJve3xa31LPKajVab5wNtFXdYJ0sCJL9zzEAcnyETcWMrxw6LyMs6X5OHhhnWJmJ-OisZy1M73sWzMMO78T7FLdFA50Z5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی فوتبال تبدیل به یک فیلم و اثر هنری میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102010" target="_blank">📅 19:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102009">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIJgcZvLa0gMwKEiZAkvr1tMRnw1Ltcr_u4hwmDGtYL65hCHatdAshi1vS5X4ttHwW4I7nkuPZ2wMR6VDipfn3x-S4F-Ynv3Sp4O3WJbHCclm_7_VFXuCa8AQENUmSOSHqH8IILfBh5bGveaa1E6ItjE1iNhRQo-9M-9k-fKjsqEC7qO0UlPEKn1gihBHdOq7X91s-LJ77QEw68WvWfdjTui3aZw3XVMcz0YIdoIgDC7bKddCXUX_OAxvGoOBdNLlupsQD2Ervj9FScK4eBO2UDJZJId9lxTB1xndfXX5sOvS0gr0L0QGFKbMn-HGV_YDcEu1F83iZPXCTaMvRhCyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
اشرف بن عیاد:
کار تمامه، مدیرای بارسا متوجه شدن که موضع اتلتیکو برای فروش آلوارز تغییر نمیکنه و نمیفروشنش، حالا بارسا منتظر واکنش آلوارزه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102009" target="_blank">📅 18:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102007">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZY2DMqis11xS3DKmeVF67eeAO8YO0jaYLXa2MdWVaGfL0bF10-KOV2zFWnKBlKZ4CzWCLWyMSR9ex2uU2jh8_7n1gibvkzqNBo5wc0cwmLwiPuTduPeaX2MmM-y-F5Eecv32RvZV_TJpVf4dIECdEgiw3dZGg2_H3hYh8eHq7XS58pHUcv2WhN4krxIi51RuM73TUe-fI8olG10VypwrmIlbX3xQHT0Ls8GRFMeL83XGQI6LuTzP-FeT5JE4JnhNObmUj22X2H45h67dI-unhuc5fKvTE8nDKNVCTnb_Z3pXpeTbhK4awVJMnvqhqoyXwUGeAqca86u8abDcSKx1fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjplECNd6w1eP8Ecmg9lqP1OS7Kw0BkBFIxxwpBq1sh94cUi4JsV2WTOcMFPWaZUc7vsJxyO5w8JKLQlk1Wv6M-kFLJ_sXLf2dSMSR_jGWB6jPrUKHUyiBP4UvQzQ75_iDEurL5jZ83usRGe26sq2LRcoImQONxA7apJuKQ7wH80GdSgnm9daK6pMlfvi1CRy4DR5WEfYzbzA0BgFXyGSI-tuL3m6cenv_RILWiaGQUs8iyLNqa1fOz7S-7gfj164FC6vJw7b_UdislY-w4p9QNOmmaOLUZO2crvi09KLBFDYrPsSIh6vU_wHO0EFdBeAsVE0C-VssKeyX3ApTNR5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تاریخچه رابطه‌‌های وینیسیوس جونیور:
• 2021 —
🇧🇷
ماریا جولیا مازالی
• 2022 —
🇪🇸
اِستر اکسپوزیتو
• 2023 —
🇧🇷
لورنا ماریا
• 2024 —
🇧🇷
جولیا رودریگز
• 2025 —
🇧🇷
ویرجینیا فونسکا
• 2026 —
🇧🇷
ویرجینیا فونسکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102007" target="_blank">📅 18:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102006">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=d-bPtCp0zhClmzwIwmsqtkv3AKF2SeUoZVKoHykFPj2ALHe7vzm04Z-T6duDQZ1RToD4Kf2OwVT03DgIQELXlFD2OdoTvzx4oIXKagCpYdHKvV-7kYoruXHtJWvl9IotGMYfnk8tYTfVbiYqfN6jBjXLMIfURMcKg2WQowf8_k2XoVDL9w_qGxXEKxEwlWtQLYmYyKIrD-i-YKyrnqX67kVMS0emu5nKZtFT_qD4JHeLNpZRzK-vIrShz0-LSf3rgcP-6uGu2Q1d2u9er2gzfxC5ZVKzfyR1hFml_6Pvuyb1PKNjjXOmff0txs5nCc8sjc-yHC2If84MBM2dCxIxHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=d-bPtCp0zhClmzwIwmsqtkv3AKF2SeUoZVKoHykFPj2ALHe7vzm04Z-T6duDQZ1RToD4Kf2OwVT03DgIQELXlFD2OdoTvzx4oIXKagCpYdHKvV-7kYoruXHtJWvl9IotGMYfnk8tYTfVbiYqfN6jBjXLMIfURMcKg2WQowf8_k2XoVDL9w_qGxXEKxEwlWtQLYmYyKIrD-i-YKyrnqX67kVMS0emu5nKZtFT_qD4JHeLNpZRzK-vIrShz0-LSf3rgcP-6uGu2Q1d2u9er2gzfxC5ZVKzfyR1hFml_6Pvuyb1PKNjjXOmff0txs5nCc8sjc-yHC2If84MBM2dCxIxHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خشونت بی‌سابقه در لیگ‌فوتسال بانوان برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102006" target="_blank">📅 18:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102005">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLZEjrbjYXDs65sHL-Vq5gNHATZwsOorviY5zUBz621DL_sFspkemVCl87P2RBGP0kdSzr-izNSfUsrINA_NV81LaLLwDVVRugT2_SCpBhjPmSF6Zzsqh3GkbjxAR3O2QRoLIL_xMfCpCsCUFMyA-kyoobPgxBmuoPVAy70U7Z2VMo8PKVm8Rk448Tw2Q1LQWkXBsKRRnxLnJHqGTpZCJsOfx76g9Ap_4foUj4qBn8KjaQu0-PULisEWOyJ8u4yy2QsRARsgBjRs7h9Is-hpjUTAU4tygVCdwbDn9RJHwaLNfy5JuOisAbLtqIwQ5y0HonT6FH19Y6aiJbl0tUjsOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇪🇸
رقبای احتمالی رئال‌مادرید در سید یک UCL که با دو تیم از این تیم‌های در تصویر بازی میکنه
🇮🇹
اینتر
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🇩🇪
بایرن‌مونیخ
🇫🇷
پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102005" target="_blank">📅 17:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102004">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iw6A3W5ftWWNPz0w47eaJqUR05u71KxD8-FJSyOcxOzK-K_uq-aEtica3m_vclMXzJ7USRv5cS-71n27pWdAACFajSDh_8FIHgt0r655zFjZhs1iAlb_NBHKffFfzIE19Zc7N3Smk05vVQ-bszcQSs3qOGf3OcMt3U9NbTSZGHN-epDpYMFJiE0tPU082ygwkGnhdZq7DPIn5eHV431GljCc3AlilyU9cj0MaBJFOfCTx-fjA90z0U_1wHr4jjlU9Jn8NyhkYtvgBUNe105X-Oax273MEC-zWOU94x7j126PYvxKXk7UGwF68KJn_LCkuewcyk9GD7SYLmn2aPmNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
فولام قصد دارد یک پیشنهاد بزرگ به رئال مادرید برای جذب گونزالو گارسیا ارائه دهد. آربلوا می‌خواهد او را به تیم خود بیاورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102004" target="_blank">📅 17:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102003">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmNT9Hn7o_yCZrqnFxvXqhteA92zCHf5r13mndhaBkC_y-xqbuuKVbkrVWSzd4K-ivt2Tl9IvqjxNXJbmpX4C14yrQdxPley-9hp7xZ0Ps0BUy-XkP0Y-gqdguuhtyHSX5vq1LvG4cX13x3pDBcfXnBZGZZ4YGQ-cmP5P4gjmJ1SuF6Le45XUeX2QZXgCfjmj6qYZobw5G3YND4XUFaWONHoWGXeH1cylAiUQCH4uWYJhXZo6kCnzZ9hdFNBiYNm7i1GfQhPtgVxFC5YYQaGASF0ozNwr9ttCj0m6qsRvpApFKBYsk_GzXeptE1uJn7RLMNXXgv_WVdxnYD4jo_WYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی اونا:
باشگاه الریان قطر پیشنهاد خود برای جذب جیدون سانچو ارائه کرد
باشگاه قطری در تلاش است تا وینگر انگلیسی را متقاعد کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102003" target="_blank">📅 17:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102001">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🏅
فوری؛ لینک پخش زنده بازی پرسپولیس و پیرامیدز مصر گذاشته شد
💬
@squadify_ir</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102001" target="_blank">📅 17:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102000">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=PwvMlyTbG4qQObJus6uOcEQEvAOlOSmpPSQejVr6MF6j5YMDbyakY6_KAacFBUEoFTp495UfFOqe6u0Y2Za6_zj4z0OB-tugPiNfipKlqzPAmenPLHBoplHiLa9VeGP6phPQnGOd_Bxwl9uqPCh57vxURR-W9XUY4QMV-kBxanL-aczNzmlbQDRu-ZTI6wlKW15rbJbJOMXfH0Eam5uVygDkQfbHjIWIaSXThzYq7p3_fviRCEPeWfNgbDqYGHDKUO3k8_Sc0tsoaPWK3DwT7v7FRDG39TxCB1MFmd1xtOrgxCWWkXIeJEE4zOcJw-mebo9UHCcIHP17OYWtV2UZ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=PwvMlyTbG4qQObJus6uOcEQEvAOlOSmpPSQejVr6MF6j5YMDbyakY6_KAacFBUEoFTp495UfFOqe6u0Y2Za6_zj4z0OB-tugPiNfipKlqzPAmenPLHBoplHiLa9VeGP6phPQnGOd_Bxwl9uqPCh57vxURR-W9XUY4QMV-kBxanL-aczNzmlbQDRu-ZTI6wlKW15rbJbJOMXfH0Eam5uVygDkQfbHjIWIaSXThzYq7p3_fviRCEPeWfNgbDqYGHDKUO3k8_Sc0tsoaPWK3DwT7v7FRDG39TxCB1MFmd1xtOrgxCWWkXIeJEE4zOcJw-mebo9UHCcIHP17OYWtV2UZ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
آنتونی جاشوا، قهرمان سابق بوکس سنگین وزن جهان، از آهنگ سیاوش قمیشی برای آهنگ ورود خودش استفاده کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102000" target="_blank">📅 17:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101999">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=ZLZO28Dh3zeU9draEWyYp1uZJPykZJrJVRu045gh6ghKeErjQHmNf4f0dvLJS2kbHBXR9Pj7i_FuFZ7LLnWkdGXQzz7WY-FUF8II6GxVEI4afFhBhjk5qWkbT-LrXVz7G-s5e0M_e5VyATrnqz31jy-yb1jPNS-Xkfx9UX1UQfZ8LKPzGN4GxR-8fZGm_YLJcF_-Cv3M-1QR6_790x0Tm40wiP3-F4_9U2vhtY3UjPcSG5DbeDAdl6Y6-zw54uPgcj5-7n6_f12ep_5FO1cluierFyWs2ojUaWw_FFdFlj5RxjlTNmS9YtDb0YxXKLiK9PSW76LlWL6LzwIv2qa5kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=ZLZO28Dh3zeU9draEWyYp1uZJPykZJrJVRu045gh6ghKeErjQHmNf4f0dvLJS2kbHBXR9Pj7i_FuFZ7LLnWkdGXQzz7WY-FUF8II6GxVEI4afFhBhjk5qWkbT-LrXVz7G-s5e0M_e5VyATrnqz31jy-yb1jPNS-Xkfx9UX1UQfZ8LKPzGN4GxR-8fZGm_YLJcF_-Cv3M-1QR6_790x0Tm40wiP3-F4_9U2vhtY3UjPcSG5DbeDAdl6Y6-zw54uPgcj5-7n6_f12ep_5FO1cluierFyWs2ojUaWw_FFdFlj5RxjlTNmS9YtDb0YxXKLiK9PSW76LlWL6LzwIv2qa5kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
قلنج‌گیر معروف ایرانی که با درودافای مملکت ویدیو میگرفت توسط پلیس بازداشت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101999" target="_blank">📅 16:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101998">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=a5vx3SOS8krd1wca2a6p6iqRz_orx78s99w_4V-XMxypEiul96mkv4hkteMFze2IEZyM5LwnMR70kJjyCE8uyMf_uW_lVoCsMqUfYcYELHq4XMrWnX8UYA7pGmk-mXmevYCftIZt_4B-rkrVquBFsvfSxpChGMy7tm9IiDa6R6FrAkFwj3lqbCA31wAgI32mDi4y6pwVQ3HoOzR-LSqu8x1M5OJPQvXjCQEJcZ01pRx-tOigaSIMpP6lMDUmD7dv9NyZ7tn3LoKtQpcnkApGmWUfiqdbOPFDKGpn57xMuuIiPcH-dGyW5eEr1uTHOjDyofsp7Zj8d6fgYfEPVA5ZlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=a5vx3SOS8krd1wca2a6p6iqRz_orx78s99w_4V-XMxypEiul96mkv4hkteMFze2IEZyM5LwnMR70kJjyCE8uyMf_uW_lVoCsMqUfYcYELHq4XMrWnX8UYA7pGmk-mXmevYCftIZt_4B-rkrVquBFsvfSxpChGMy7tm9IiDa6R6FrAkFwj3lqbCA31wAgI32mDi4y6pwVQ3HoOzR-LSqu8x1M5OJPQvXjCQEJcZ01pRx-tOigaSIMpP6lMDUmD7dv9NyZ7tn3LoKtQpcnkApGmWUfiqdbOPFDKGpn57xMuuIiPcH-dGyW5eEr1uTHOjDyofsp7Zj8d6fgYfEPVA5ZlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
اسلحه به دست منتظر آمریکایی‌ها
صداوسیما: مردم بندر جاسک به صورت خودش با اسلحه در ساحل قدم میزنند و در انتظار ورود نیروهای آمریکایی هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101998" target="_blank">📅 16:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101997">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5IIOOZMqGArxmlyddT8b9KFJWSfSMotBFQ4ZyvOzEkC7KZ8a0J6cgjwNJz0dAKftJimRL05lIkroCWDr7FL2WthtyVt9yqGAonA9vPI5l3y5jmQnGQJ_EBOVqIiyJ85RX166CBkuuNrj1U0QwzJuopYLylVs29qHhFmyQU6EtsYNnH0A-XuFQf1uSXIP-cAFD4vyYYfsQTrEZVJFzvPw7TNgJ8PLMndL8jjghiDAgYBU1LQj4frXZY01Etj28hKjMQT09rUChtNiDPrZfKF1a2i8S6ESuWnJyY1n1jTldxeY3i97bcJGcbaYXS_OWW7wYoZaX9kIGa8xzZYtAaruQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنانی که با همسر یا پارتنر هم‌تیمی‌هاشون وارد رابطه شدن:
🇦🇷
مائورو ایکاردی و همسر مکسی لوپز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری و دوست‌دختر وین بریج
🇩🇪
مسوت اوزیل و دوست‌دختر کریستیان لِل
😀
تیبو کورتوا و دوست‌دختر کوین دی‌بروینه
👀
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101997" target="_blank">📅 16:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101996">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=j84v1O1-5UDA9SmmLlr2ESJgYR8G0Gj27Jp60Qd8P2vz7iUm6SvvWnsG1vLHR2Zj2LIWcWvw5pWWpjh_cS8ZygSeLZlwUwC16ocSqpv01f74RxdIEBb6Xpht88O_AsDH6G9HzV7Vm3F_W4PRCkvH0dfcGsOocTSSjs6XTBXcRK9vnzDR4T_hIpvtx5WEv8KeCq1l5Fpa33NsC7OZQ7zZIgw2wDFtAONXareylLAMB2WxSEnPfNvZ_QeZ99RlDkpbA6OQfIm5Nk5f0xT1Ku0s1b4uU-HmuAciPEAYpm56CeXqpZbsxSpGnbODLUo3rwUjPVCx9MXEp6p6SFFBb5_Ukg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=j84v1O1-5UDA9SmmLlr2ESJgYR8G0Gj27Jp60Qd8P2vz7iUm6SvvWnsG1vLHR2Zj2LIWcWvw5pWWpjh_cS8ZygSeLZlwUwC16ocSqpv01f74RxdIEBb6Xpht88O_AsDH6G9HzV7Vm3F_W4PRCkvH0dfcGsOocTSSjs6XTBXcRK9vnzDR4T_hIpvtx5WEv8KeCq1l5Fpa33NsC7OZQ7zZIgw2wDFtAONXareylLAMB2WxSEnPfNvZ_QeZ99RlDkpbA6OQfIm5Nk5f0xT1Ku0s1b4uU-HmuAciPEAYpm56CeXqpZbsxSpGnbODLUo3rwUjPVCx9MXEp6p6SFFBb5_Ukg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
علی علیپور: حتی خود پرتغالی‌ها هم کیروش رو گردن نمی‌گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101996" target="_blank">📅 15:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101995">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4Qi7qBDCosFh9mQDSgLEVG46ZPfLyniBSxV65GvYdqKrYVlZodmwuGgBeTPXiJVCn0ri9EOoi5K-k--esPw92VlU9sc2CiuV_3GDSW5AkPhapy6lUHDnjiASwz54vi72m3gfyjQmt90JLF11ZCpcFBjjkiUtIIJo-VpqohctZjzUzq-apegTfuZ-9YuDYDfscbX4BFPx0b5-6kXtQuKx8y4oJiCyrP0eG7svtAHx1ffWXJ3iXDOZPm60_zlHElIj-n8PlnP3XW6jdjSj2DKzOcojZ3wMN0tUfwPa5RvoMg_kU4jGiPNHlYdE_6goDRFC994heCZnff43_0wB6ItGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📉
می‌دونستید؟ فقط چند هفته قبل از جام جهانی، اینس گارسیا، دوست‌دختر لامین یامال، حدود
۲۵ هزار
فالوور در اینستاگرام داشت. از زمانی که با لامین وارد رابطه شده، تعداد دنبال‌کننده‌هایش به
۴ میلیون نفر
رسیده است. فقط در روز فینال جام جهانی هم حدود
۱.۵ میلیون
فالوور به دست آورد. همین رشد انفجاری باعث شده چندین برند بزرگ برای همکاری تبلیغاتی سراغش بروند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101995" target="_blank">📅 15:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101994">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🔴
فوری از رومانو: لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101994" target="_blank">📅 15:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101993">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZnE2pk8xWfK8kaX1EUhJxXjaFdzzCvaXZhWlo7UrULxUEoPd3XMxlMYXw7DPjqH0yryv1HPIsJY8DTbzJ4eH4VLz8tSZVjIbcFFswFIEW5ngY_44KuS45pz9qkPCPjfiU-V292VaxQL_qqT5yP7WnjONzyJWtqlaH0o_Emtf5Hk-wXGYj__oTVbdq3ufOzBm8r_mFsOvEtSvgsexVmoRFEBi2EW-f-NNIzQqRSwRkV751EQsDG_cZK9aIWD2sY-jI_BQNmxzqxmmEMmV4qoFnRK_Mo8IOiLS-TaHV9-BnqlGWa2PmShTBULP-ruFNiGkBE-dSesgKnLQ3I6k7jLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فوری از رومانو:
لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101993" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101992">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=Zx4z_I_QaQRpEqemvT-zEO7CIpyT6oHuQk3i3105fRggopLN6tXN_D0LNdRCAJsTPLaFjVbLPEr3u3n7uVlCjl9KxC0dUlVTsg0ZS-zB3CHMEvKL65Wxl-7p6Ne6D2sYOWSM3muW_onSZwOXEvsNv4m-FA0HZuJgCA9_VorQOwV_r6k1qIsRs2qNPKhif2JnUsLWptvf2v5ygXyx7wpMv5Q0wLDwF-TKUPX_aP8IjgJ-9QASPpmjd-RWN1lGtvijpmbq_tCFjkjMuj3vVrmV1zlkTWTAHx61EF49hoDL0rzwM9DsEfjkGhfkrN2L8xyjEteb3k7YBOZU1OiNTzV1YC4r8kea-dzDDUtMe3GhVg4ANqxlZBh9qLsBetfNkuapLiQkVh7q2_RnKprPDEbxZeFSMomceF8kwlBOT6lIVfVzAL0R5ES7yM8Y6sR4DLxe3XIA2lx7byqW0IoWSHpMVYfjwVbZY_pS3Fy-6WuQ5Xqm0nfQrytqgf9lDHNwMwgcy50oJSCSZtwDxNT5wVc-XmfhIS2y7FQOjmk59tNMsREkU5m6EUP-K5gQMuAv83gGa1_psYdtr8kv4EeIlNmzHNDM6tR_LczZOfjQysQ5DcnnSpltjZKQvfMgX70JahX_PE5DrIjaTdGvibbSt7alL5m6xnXA2SFSbR1Z_awDX-U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=Zx4z_I_QaQRpEqemvT-zEO7CIpyT6oHuQk3i3105fRggopLN6tXN_D0LNdRCAJsTPLaFjVbLPEr3u3n7uVlCjl9KxC0dUlVTsg0ZS-zB3CHMEvKL65Wxl-7p6Ne6D2sYOWSM3muW_onSZwOXEvsNv4m-FA0HZuJgCA9_VorQOwV_r6k1qIsRs2qNPKhif2JnUsLWptvf2v5ygXyx7wpMv5Q0wLDwF-TKUPX_aP8IjgJ-9QASPpmjd-RWN1lGtvijpmbq_tCFjkjMuj3vVrmV1zlkTWTAHx61EF49hoDL0rzwM9DsEfjkGhfkrN2L8xyjEteb3k7YBOZU1OiNTzV1YC4r8kea-dzDDUtMe3GhVg4ANqxlZBh9qLsBetfNkuapLiQkVh7q2_RnKprPDEbxZeFSMomceF8kwlBOT6lIVfVzAL0R5ES7yM8Y6sR4DLxe3XIA2lx7byqW0IoWSHpMVYfjwVbZY_pS3Fy-6WuQ5Xqm0nfQrytqgf9lDHNwMwgcy50oJSCSZtwDxNT5wVc-XmfhIS2y7FQOjmk59tNMsREkU5m6EUP-K5gQMuAv83gGa1_psYdtr8kv4EeIlNmzHNDM6tR_LczZOfjQysQ5DcnnSpltjZKQvfMgX70JahX_PE5DrIjaTdGvibbSt7alL5m6xnXA2SFSbR1Z_awDX-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظات خنده‌دار از زنده‌یاد اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101992" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101991">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=fqowHwKHJzDdSFMuW2DST2-RWwL-lbAhOicYnBiwYML6fJnEn-aDLi_JkmPiu5N2eATO3-1nQ_5dyHwq7V8F0y2SaeXvL_7w9oCTnMtjxObF_UX7YkyirmZZ38moMS-8OsrfYxPnwqMjumAKyFaRDXME2evT_eSQK3IZ2yPl1UiY4H3i7p3N4LJ_wP8FN0WeOZi8cv2E2-QibXVFCcMMXES9_JDgDdskPjyLU3--HJFqU7gFgZyMR4Feuoi7oFeAhP8jJN8BL1HXXw3xhj3OxBMhIPCoKlGAH88oRVF-F0WU2qFprhDW58hx-8pEXYGAOXAEXJ7Fx26S9vOfugjJTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=fqowHwKHJzDdSFMuW2DST2-RWwL-lbAhOicYnBiwYML6fJnEn-aDLi_JkmPiu5N2eATO3-1nQ_5dyHwq7V8F0y2SaeXvL_7w9oCTnMtjxObF_UX7YkyirmZZ38moMS-8OsrfYxPnwqMjumAKyFaRDXME2evT_eSQK3IZ2yPl1UiY4H3i7p3N4LJ_wP8FN0WeOZi8cv2E2-QibXVFCcMMXES9_JDgDdskPjyLU3--HJFqU7gFgZyMR4Feuoi7oFeAhP8jJN8BL1HXXw3xhj3OxBMhIPCoKlGAH88oRVF-F0WU2qFprhDW58hx-8pEXYGAOXAEXJ7Fx26S9vOfugjJTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
دستاورد دیگه تیم‌ملی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101991" target="_blank">📅 14:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101989">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmD6Qk8V2gG-pD0ClVilVwV04PY7XZ7wE1iV5aOOckLY_MPwOa3tvyNbYYGlGZrHkHaPiJ7Bn8PF3w2bcKYyaf-zdYMd03mANFJStqY2Di_kmvBSV34H46274NXbPSq3-twu4c5vdGHF-8geU3dyyNNdJrLInKup05srcL8T3jGdTRHZUqjy2_ip94u_EnzdjmRtdBA86ydOe35B56STmwZQJdFPJBPJpPOAjYba8oVJkOiEtkUBFV6vrL8Tgn2y4FsMSVLSqO77P_b0iSg4Kz7G3s73nidvA2hjbFY_FmOzwMv9vobgN_OsVjjFNGNzp12s4UDb5cYYUn1YPyHYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGA_jezv4vipmckUzCKPoZPRMIlaggerESym9tsewcirkp-pxL4-YIkkcD2aFl2vNDFniF_owAa9IjRMXSr6NTQlDc5T2tXc7-9tDTcn6cmoy3QRnWBUmsVJ1fKnCjUsm7xUIY5rBboN6UFhoLrRT5FUD3QjnGb7rvBRHwU2zg5A6_njwO0vWdX7QQ-ut9-TMMKGNOmWvIW5hyRXF_pxRpmNz6PWaV5k-j94i382AKiHq4N8Le9JdHPe728ZC4MgGISEMSJKYlN46-nxXTy_oka208JhUzitHbGoiJAJY1nukIcEAOn1h6j8SMWp7ne8-KUdW61kfc2wixO_VfpUBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اینس گارسیا، دوست‌دختر جدید لامین یامال به این موضوع که گفته میشد باعث جدایی او و نیکی نیکول شده، واکنش نشون داد:
من به کسی آسیب نمیزنم، چیزی رو از دست کسی نگرفته‌ام؛ فقط دارم زندگی خودمو میکنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101989" target="_blank">📅 14:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101988">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=H_HMFxGVqIXEFlNoye9rX7UIW2rSD4pNtvkjXqBjzpHLKqf23VMBhvTdXtnnItdy3VMIEeeokNaEx0VS3Abc_fFPF3PuTZ7ri2-j9LIhMtAxGpmfxwiSBCneFxO9XK-jnSh3gKfHveN69jhPUoRaeXGmut1lc5H0JZgCko_cW-LNy2kpf4Wop5cNvxRAHC7rShKexIemSpDxnGye0LkzZYFT4naxiZQgFj0cH1chTa4vnyl-Y2pQL2ftDK1yGpfVAEYVxrQl7lTxzPssUNfq9_F6k6aNhR42p1nU-gnbeeRShbE9vJpLCrlXF6C6LMB2UhCPYNJAsIJVJITLe8Dt3SI1EdBlPVRXrARGrxKNzgeZ3LmJipO04veYfjavJONFCW4sztI-JGUPCfhOpEm1tAr7duOfpNRWG3dbKibQaCydebLU0SF6smoD6z9VVBIEiLWHqj_i2PtHxnQDCV7f2YBvG_LM-hz686xITJnaAysJnrKZnCiCogcN7sRbKSN4oUuemaiTs0KZiQ-nwIPcydkZqI6cBPFAP3jxH60Dt0YkESggoviU7hUcrewHcIqsSM9iBXrR-0W0jvb_7V72c9J-DUMhTeL8SCPniJnTTNx5m8V8Cpr0vPUyKqlWTCaMANn2QGI56dG3wNgutLAC3Bug9MHTqp3oMPKW3MgFR38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=H_HMFxGVqIXEFlNoye9rX7UIW2rSD4pNtvkjXqBjzpHLKqf23VMBhvTdXtnnItdy3VMIEeeokNaEx0VS3Abc_fFPF3PuTZ7ri2-j9LIhMtAxGpmfxwiSBCneFxO9XK-jnSh3gKfHveN69jhPUoRaeXGmut1lc5H0JZgCko_cW-LNy2kpf4Wop5cNvxRAHC7rShKexIemSpDxnGye0LkzZYFT4naxiZQgFj0cH1chTa4vnyl-Y2pQL2ftDK1yGpfVAEYVxrQl7lTxzPssUNfq9_F6k6aNhR42p1nU-gnbeeRShbE9vJpLCrlXF6C6LMB2UhCPYNJAsIJVJITLe8Dt3SI1EdBlPVRXrARGrxKNzgeZ3LmJipO04veYfjavJONFCW4sztI-JGUPCfhOpEm1tAr7duOfpNRWG3dbKibQaCydebLU0SF6smoD6z9VVBIEiLWHqj_i2PtHxnQDCV7f2YBvG_LM-hz686xITJnaAysJnrKZnCiCogcN7sRbKSN4oUuemaiTs0KZiQ-nwIPcydkZqI6cBPFAP3jxH60Dt0YkESggoviU7hUcrewHcIqsSM9iBXrR-0W0jvb_7V72c9J-DUMhTeL8SCPniJnTTNx5m8V8Cpr0vPUyKqlWTCaMANn2QGI56dG3wNgutLAC3Bug9MHTqp3oMPKW3MgFR38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
چنتا سوپرگل نامزد پوشکاش ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101988" target="_blank">📅 14:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101986">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KrHqV0Tg68Un3shsf_WJkWdaM9zgKeJrcGgWQggleuV6pSWHZc4yFHBnSSEIlVAuNawgRCXCRxjb89MkcJhf0qdqdQxDtJ-gLZLNK4E0GISkD-yMmwYgYRxQiwabAPAEOc3kO99VFfa-A76XenDHTfIUGHBf5ZjOtJWAYUXvNrFaSi8ToPOwHMq3uz9fBkprwoGGeM4SQZluWMe03pLWfmsEgJCwsiggBnjYV1gG11W5GznhRnmRJ6JmBEgVu5HgtHHUvaxoUg2F27TpdI8BIZNSbp13Lm_Y1p6MSwUm67urw9ddU5hGJpMkekm466aNl_GFzv1Ytv3F5mgaCfH5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uialL1mv6dUXR2_hWVGJEUci8y2wRm-b78GTXyUKSn6MFmNsJQ_asxsqkIFPYmGIJeb5eY5wqznPf-ZXrOYhzlpi9dDxGp3xNoCNyXFFHLydeb7PdPwQegxVOmdUkALgvnX4icJDQnR1r91loefS6qfk0C9_cnhzTrGDWhgxhfxEYJsrsN08lKSGUFU7iypbZRmKJaaUzPFWXOmZF1hn7wq6bBO0HbO-samXmMyGUcbNQz3vw9ZC4MocIq-EDftk-RRhabKCCsRLqkjTna2R6BU7LuwIOEW-YdeY4lRmKupTach-lhoZ5OhevkCXtVdqpExCjorTL6VO3TwhaMA01w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تاریخچه رابطه‌‌های لامین یامال:
• 2022 — سینگل
• 2023 — آلیسا
🇷🇺
• 2024 — الکس پادیلا
🇪🇸
• 2025 — فاطی واسکز
🇪🇸
• 2025 — کلاودیا باول
🇪🇸
• 2025 — نیکی نیکول
🇦🇷
• 2026 — اینس گارسیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101986" target="_blank">📅 13:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101984">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjzplorUJdOOeL3o-seugnWW1WsTP83233W5YuDO2P43MSRE_n1r_r-0tAou42RE2m0KRLtX4N1HPeGF-vMls6RBP_qETS_nrpJ0lTqbtTdQOlEjYNE086Gbsfs5zzmd_ylaG3MqPIvSR9hXC6xoD7XDf9a4d6QgvRYNb5vqIENEJV3BQzg9gx2QoO5GyoeRgr2CXyToIWy5kWZqG5wFyyiVgCv_qrEUbrBwFQdPPhLqBJRFgfl0eZ6YLhybA5PM8hh2eR0D1a6VnDTRcyPKqkta7wniK1zx-dhqIyzSKZmtWrs3xN8daN_YARHyq7JQYk5M4eTNnKKfjBZTkgGFGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QEo4Q1luxdVPcb1LBbhh2AJPmDr5DYt_M_kGELCvhnff8dKPlPXA42bXw31WRwT175gGLBiGEyXYzVvU1ymW7V5RdHPrum32Va6B5RrKZa-j_65vntPhPL3lfC8w-XN3RUd7hX0vNJ8uhsLRaUzx2q5WzS1DgR6I-JoKPwoHgqNa-DnN_3bRPJO2uqHvrKP2uYt6MVtddCiIj7NONfgA44gWjAXV7ZDS1LwGpWP7V6KC7zKm_eNqzd469bP4lWtJyvI8tnZVg8a0XizHcdKCkwBwBiWGm_0sGLTrwXcufAaui85ok62CKAHimfdpYQ5LpbqCrGbGy1TN9ioDYo9TPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
جسیکا توگا دوست‌دختر سابق وینیسیوس جونیور:
این فوتبالیست‌های سیاه‌پوست فقط از نژادپرستی شکایت میکنن ولی همیشه با زنان سفیدپوست و بلوند وارد رابطه میشن. اونا هیچ‌وقت با یک زن سیاه‌پوست وارد رابطه نمیشن یا چنین رابطه‌ای رو علنی نمیکنن دلیلش چیه؟ جوابش واضح و مشخصه! خواهشا این سیاه‌پوستا فاز آدمای اخلاق‌مدار رو برندارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101984" target="_blank">📅 13:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101983">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101983" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101982">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgAGmWD0E5qLy7cmqgUfVKo3ukMbsBO1PWvpyI-0xTSQSPqho_J2GGdJ1DAvFTXUGGVurpFrpMbyHFsbR922xugLrZH1Q9U7EdOIsPaKtEFSw9BluxOl2TCnhIRR4NQ7mn4s0I9LAB-tlWxix1ZJ7qNcGw5VBOG3KU9PZX4_sOPLcJl3Lvolvd5o7Df2GXsNLxh35XmLBJIX_vaHBX9_bUuCVdwpPKs4Zw98WxSahd0V8gvTp0e0GNtp3uvJFweLYHrP3P5ZIti1oReliKRfnSUwJMF6cnZjCyTTQ-_-ZcDvHP9zkU4hWPS5rz4-P9cbeZ914xEvSIObipNkagBQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101982" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101980">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShcSl3clP76t2Frq6l39gbD6wX4pk5d2TxT7wUhrX8HKwc-V2bRssWtInPgGRYRFC_sQPPFuakeHDeUYhk0dq6WfvS5eLbWkXuGs4FX9goew_uDvMKWG4G2Ic2vCXrdZOk0Ac8OY9fHh7KCYixPA057rtFBWM5jNo9Y8GhavU4TIYWDS5F6kvQYmtm5vuf0PlPz0DP67aiQ2Lx3hoKXu1YdvbF9yfiM4ovTO5k08OU5OkBT8aq3_9q0DPDJZ-kXmwdSoPZc4G4aGrlf3YNwkJMZJ71bi3bwX5dZvsd9YLIRUs2hWrMLotH9fGtzoXByMW2mlau6NCtnff5FHaUwGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLgNzB-yr20cdVU7GNVZlrokvxBo-_vXjM99n9U_A_x6JCQV5fvCbuQJPmF1cUeAz2Rd_d0JssueIKnTehBGkaItIeL_Dncbw_SzxbcoFyj5h-I3f7dxY1tywnZqW-LNUyOxk2YMhUoq54wtLXOaK3_x9Ez2CO-ovTvhscRKdT5KnYYlzxMyIRY4uu2jcQFpXvsBX0wca0tpdd0e7_0pluCpCOgETtJqHHXNv0UXpf71tgXUMbTii9ePuavRPk6r9CPzt0lQODZL-X-l7HSYNwGC-F1kVjFm36NnB3ZHEY-0BRnqkvp6cRICGwYc2jOcby_DsFbkbFFcPBU7X0j_vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📅
🔵
17 سال پیش توی همچین روزی بارسلونا 46 میلیون یورو + اتوئو رو به اینتر داد تا زلاتان رو از اینتر جذب کنه.
🔵
🔺
فصل بعد اینتر تونست با حضور اتوئو یکی از موفق ترین فصلای فوتبالی تاریخشو رقم بزنه:
🏆
سری‌آ
🏆
لیگ قهرمانان اروپا
🏆
کوپا ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101980" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101978">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iWdVSJPqE0zOVoKbsOgrpYeB-ceXhHFbFAr6gk-Y4E8-DrhfTIS1hKXvopq_76Zxvv1K7awC0fsEIXdjnh-c0dCgERFll7nGRdA0gbRjO2b7Me2lz2X46SxeDYs2CEPAiIoW_SPnM5_nSE-NdHoAu_NJj8OOyCUSkGyJ6Pre0zS0Flyl2LM_aNqWAuEaiRiVx20UJI_s_Lbgb92joOSuM_6k69v6Cn2joXIUPMTu0ANonOya6DrHwZjdApGFrzeE0DjtVTTnU1ieTk0oV8NEcFQ3bvvLbQQGaz61V2XNPIyXG_Ux5-Ai91D3EuX9QK_FKWagHzUheXwCc3ykfYANqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQgCDL9ANL0rWnjkQVE4vfe6_t32VQVq8nJEmdPzd0FMwHSEFxO4GWL37xVzW9Ctrraulm70RfhPfol7yeF_AnGFLQMe7xd44HSmCWys4Ax2nUfgVp0BoLHeThuinNPKk3SWJ6xAiCQD9psNFu3c0CREu2UWsZjg8fNIQIxUvJsRPPE2o_6xEBqpKaY_T3qOVhQtoEu6nJvpuZ82KRhr0cSPRtL8C7IG7lOVwPjGEj1veOPfgowfDlYgeOvH7dPqgRW0PemuPAdnA8Q47Eoq7CnPrqDG_E8d3-p7zcn8byAFhQKDPIWiU2Vtu-ZPUq-crzPCf8iLOrI78e_KJ4UHpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
الساندرو نستا درباره غیبت ایتالیا در سه جام جهانی متوالی:
باورنکردنیه! پسرم تقریبا ۱۸ سالشه و هیچ‌وقت ندیده ایتالیا توی جام جهانی بازی کنه. وقتی بهش میگم ما واقعا جام جهانی رو بردیم، تقریبا باورش نمیشه. میگه: واقعا؟ برای نسل بچه‌های امروز، دیدن ایتالیا در جام جهانی انگار داستانی از یک دوران خیلی دور و گذشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101978" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101977">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJ2Tpu1mSUo6lUGoRt4zOU4RLbRPzTgRD_kmDYoRMJMtCziXUfihPJUm1mTe-XdnzQVnlBlq6UO--QzosV69Zyd3rFQth5AX_pLisyKqQGHckHNFOlJXh5pY7l1goE978bow6FPLWK2F-2dd1lBsQEKQRniAtpnDqwzPlCD57LCqBB4MMvEzKUFGTbVc_wmfo5MLs8OstIBh2BaNuymKtGWzCDGJ-1YV8c4oHEgWFiSZ-jBPi_npHLE0P0yF2c9Fsurps6b3ZOtageK5h5YkucoXdscrmfUKVe_oEhUZ7HGMKYZ6lnjzMZtyugeW3LA35whjH9Ssgp1stfHdCVO09Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
ترکیب آرسنال اگه همه شایعات نقل و انتقالاتی به واقعیت تبدیل بشن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101977" target="_blank">📅 12:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101976">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKgkDaKvEYeRHrCTmvFXpUUakjUge5VkcxevSTvVoZmvYJTgCb9Bu7Hs2XpN3UKldu5TTYfHRuhM4bjpmVl4hZ_zwpHKmGMm6JHNw8pjmb60iMdQU2WrNkFFgvOuNFHNLmlUceuPxiiOJ6S8bc-8yNDqCGbS_qD51uFRvRPWRLIEIJkVv_qFSw9JbksFDCg5jIgz8h6viISWVgoW-vkt8rz1kbBidI1vY3VE1SAWXwPMaoStR9NnI6yOz68ulG8xTQbJT4s-Q4kQ0UJXHg9G49HVLEGQdK2R6WI4vs92pMaR4smSpwsnqk1Rn0c-fAki2m0M8AQf_g6S8WlxsGKp7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
طبق گزارش‌ها، بدهی‌های النصر عربستان به حدود ۱ میلیارد دلار نزدیک شده و همین موضوع توانایی این باشگاه برای جذب بازیکنان جدید را محدود کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101976" target="_blank">📅 12:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101975">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=cfcLKdvSY-48oI6jcBc1Mub76I2ALfX9QtoO88GH0thauFtJ1j_XETAiorEMCtUGwN6hQyCprO_Bo1KmjG0gkzoQwsIrgmXx6WU_00nDTxBTXsdMt9LdHU5niPeW_gUR77xcIRRFTPqImeiWrZRayeMUWOVdAgp4Uvqvm8okLWPvTG9fwWLZyXm5XAKE3UOdJkVLHGsFqGk8i7965Z8JxPobUE3n7frT7fecbGba89uRcSH2kZkoIHsOr7bR0uEm-2EYXWOJRf9hnR8RhAODs4QPr6Im8cS9I0UlI_a2lvHCSdGYtKWjKAv5G0NmT1bjoQOjKFYi3hGaBtSlF5_blw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=cfcLKdvSY-48oI6jcBc1Mub76I2ALfX9QtoO88GH0thauFtJ1j_XETAiorEMCtUGwN6hQyCprO_Bo1KmjG0gkzoQwsIrgmXx6WU_00nDTxBTXsdMt9LdHU5niPeW_gUR77xcIRRFTPqImeiWrZRayeMUWOVdAgp4Uvqvm8okLWPvTG9fwWLZyXm5XAKE3UOdJkVLHGsFqGk8i7965Z8JxPobUE3n7frT7fecbGba89uRcSH2kZkoIHsOr7bR0uEm-2EYXWOJRf9hnR8RhAODs4QPr6Im8cS9I0UlI_a2lvHCSdGYtKWjKAv5G0NmT1bjoQOjKFYi3hGaBtSlF5_blw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خارکسده جزیره برا ایرانه
✔️
خارک و سه‌جزیره برا ایرانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101975" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101974">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2mV_9QhXFdwEIgJfAzZioqbZuKQnR7Toukn0PHXzEEtc2HivFbLh8acj7BMYkpfWMf9Ttuv1tLUxIKGlnw2EmXlP3jEXs8AE27gouimJ-rC0b5v-W3HScL4NGSRumcrG4YVvolKG2YOZ_xNhadMwXCSBHjbki6cC-Ly2rSh7cUUPusLA0HMLNZa5U-QJC86Ui092hAgbCBz7OA5_3jnhKi4UF-C7iTwYLoII7CgJiUXtMvjwkZIOCBT8hNz5Fcbf8nDOt7f38uJPAmtI8cjUv2FHyirlIUsve8LkAhfKkMShJSVZqDIxfsGREFvqfr7vpXcf47QqeJluDPXEZGj-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انزو و خانواده تو تعطیلات
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101974" target="_blank">📅 11:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101973">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeQkt5f6Fzl30yKE4s76DMq_kyRq8Ysi8un9dbD4QacUhGw4uulOaq9PuPyLynqqsW9VxG1h2BmKkKgMo5V2b0xb0KtcrAM1DYZYWgVpB_S-EMkY1d1y0HSB207ruhpWidJSMljrYdZNwPwWJmjH3yBV19mgF2418PLQjHVKnMhBjgxQphXETf8bXYj7iBZudRVOOsg9_WRzWpARsSLt7cVZCRtIp2I8v0JszmU0Ztsa6xxTLRw5nxpES8xYwfhcQyccSYoviF4OCwISZHy1iSKWwbmr8blVOzooGQ4AnjYRPyEMyhly7aw6-0AlI_yBhh4wlyTAMp-7hIlR7Gr4kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
‼️
مانوئل نویر:
🔺
هرگز آن لحظه را فراموش نمی‌کنم. مسی بواتنگ رو رد کرد و درست جلوی من گل زد.
🔺
بعد از مسابقه، بواتنگ شوکه شده بود و گواردیولا به او گفت: «احساس گناه نکن، این کاری است که مسی با همه می‌کند.» سپس به ما گفت: «حتی اگر صد سال هم مربیگری کنم، دیگر هرگز مربی بازیکنی مثل او نخواهم شد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101973" target="_blank">📅 11:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101972">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=LoysXymrGRkarkYbC5batakBs4W8k2aYKlcbeytZmREgU_VkFCGS0_rbWlKCZjxoRGN9HnFLvkgXR18ZNVWUUz6uSMSwq1lMGJlyuyXUeWbEKiq6jNtxturYPUaNqNuhuW3k9JZ6L94GPupCP4Bz7fvAaCP8MA3_wPFiCovfOfqp_crYniZheXquJLxhW-0_OCoA4VD_y672dlIp6JTbhJNe0_gTl9Fbz29LlgD2m2cgN4un3WHaZBSZUj8tqe6GJK13EWJfmsqazG0pMkXxduSA2EhO6gZoc2AQIllJxMWENeLq-59cM9Z_otHheR9Q7xIAnchsVtkR9rythltj8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=LoysXymrGRkarkYbC5batakBs4W8k2aYKlcbeytZmREgU_VkFCGS0_rbWlKCZjxoRGN9HnFLvkgXR18ZNVWUUz6uSMSwq1lMGJlyuyXUeWbEKiq6jNtxturYPUaNqNuhuW3k9JZ6L94GPupCP4Bz7fvAaCP8MA3_wPFiCovfOfqp_crYniZheXquJLxhW-0_OCoA4VD_y672dlIp6JTbhJNe0_gTl9Fbz29LlgD2m2cgN4un3WHaZBSZUj8tqe6GJK13EWJfmsqazG0pMkXxduSA2EhO6gZoc2AQIllJxMWENeLq-59cM9Z_otHheR9Q7xIAnchsVtkR9rythltj8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیوزلندیا اینطوری از بازیکنای تاتنهام استقبال کردن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101972" target="_blank">📅 10:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101970">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzQ3MEB5V-9Ln5bgy6TMQdDh__Pt8y-dSwlxL_535mwbBXsT0qe7J-ckoCaf1uXhjJtoQMHsBrZ6fGSsJ50YW3pjgCxXgf_uREtVtuIMi8OhBwcwCi28gYK48fduR54DOdLGEsyD_zwS9LjI2MJLLCf54N_FO5w8eEijxlC-f08A5uj3i2O9k59-q0s4GcMAl15jYqt8tEAYgqFej2YDaUHNEazRBDmdFyyEhBCH3u5Dkiy_-8o-QFWdPY6V2WEXNvMDwXmVxbYrnHRqK3yndNtFvbtAo0iCxZplcL7EKrLSj6QSVyUs72f6lOSbnFCUXnXdgC1tiFxZFMzIEqT0ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pyg08WvzI0wPv9YFPUt27qYS_yq6eXkHvZWfSfl6BqCyHhiHGQEIFXMoyvK0DxgyiPN0gIpBeIEG0EQxfoTJX0xzF5UcPS0z6GJguhbfrWSCThpNPmqp7ntFXKPBOMH5pXTBlMUcA_YWHK1zsVGToRImtiSyirZws11sp0_LrNw7MmzBWKRw_BAbFtO46MM3MKOvsU0JzgihB4HP28ssLnlZ9NBX4kUiBnoJbuZYGBt1aST5CD3RdyRw57NOQBP5eTlzbt2yFh0LNC64z-jAcMasW4oHZuk4r5cuMc7iJvp5QarwXCsSzG_-TWtCWXC2fE5eCPOcia4vy8RQ8NAn3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پدری داره تعطیلاتش رو اینجوری تو اسنپ چت میگذرونه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101970" target="_blank">📅 10:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101968">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XC_0B4Ki-YL2FIEBj18_XVslgdyu_nbaLckxXKJg8niPa7OJf1CT_CErgs0QjA2cft-3VLxvMhlKui6KXc2m4B6Be_vxE16moaKt0LKTYF6y7zARDxsCAnk_LC5BYdOwoV4qOZWZsKWNaWiBSdnze4aKe1Lpc01S8aNCxFaOs0F7Fmtqsm1_kK97kbawPHvp3saEwhZgtXvJcrFOBZj5UCD7QcSUXYtWsYmz_K4BSNTo6WIPAQHrVp4QzJ-76asepIaIqJbpHQpmxJpA5wxfMW0CvDCOQN845CbJ9RoCjyw8_RjF34mC56MF7O9AiRshf6KfcqUuO_uzfC_rFYQe5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjoXO2cj_mWv6zc1JLzTCdShfmHfKMd_1L6rT2gwVgCpFlLG8OtqEavxfcNU0maLQRDcAvKJ-eZOhzS_2Cotnm-MNS1jhEsD0TV6wtWk2W6PIHO2pcls4mP5zvHtHsE42fPjT9ALTovppgRTyD2Vq6hd5-SBjVBhNC5-VfmS8APFqSa_6h9jhLNwg4abEm4Zs0o5mLf4WTNOZS6952S6HdF8F2zXi8W7BSjGWNjREqgvCqzbgQ_Xz1LROtPigftUJYjMTEaxmZFvJcSbk9mEk8_N7HDy1McqsyUACRDXKMBwxIvPCzHSLw7AeGa2f8tQ31fInHpbMRJJzeTT4SAjEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
😞
میگن نیکولاس پپه بعد کات کردن با اکسش تیانا ترامپ ( پ.ورن استار ) الانم داره با لانا رودز وارد رابطه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101968" target="_blank">📅 10:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101967">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrYu30168jFEZuWOqhrfc_gLrMCsOfrF2Bdc8JH0puy8DBY_G-xOAu_rls9tOcBCNPamEFDXnFfJU0VSJWARHNe8J4FonmoL24vCukcTKeL35Zj-zC85CPzohXRmFzW_er_6eHskcvqSA5omQwzyS3kZ8WQdwTgdrw6dAJbV6OSj5_FVQ-eiM2MF9ypfCZ732gvEWQDtd1tSg32ILic84z0eQU61ve9v-CiRWAOa38t8i4on4iQuhHLCWjhokUzcksaTsbgwTuF-dGLWPExSvTlxZGmZ9SCA2vVn8p6uIxGDJ7BozNWK1PeTS-CrMbGfo1OEp_c5zUdMxEhIIaU02g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
موندودپورتیوو:
اگر بارسلونا نتواند خولیان آلوارز را جذب کند، دیگر هیچ مهاجم نوکی هم نخواهد خرید. بعد از جذب آنتونی گوردون و کریم آدیمی، مدیران باشگاه احساس نمیکنند نیازی فوری به خرید مهاجم داشته باشند و معتقدند فصل آینده فران تورس، دنی اولمو و رافینیا هم می‌توانند در نوک خط حمله بازی کنند.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101967" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101966">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsjEXqk3kCfq_gNW5r-Olk7tCSxN0Fbx9eoCgSG5l_mosl0ijOkVPiEpaZeQvoIVl1edXAggI-XaCtCa1pJRc2zi7HFutvz4Y70ehHogc6CM2dBto__ZbenO0eAsY3NUlpgDMlGCCCHymujZXO38_NqAGgWVjeU0B148Evd2QUr0iPDV4Gtku2oHh3FVXkfGpsWNFzLlMDSH-zMn-kZ2JmfPUEtVT_KltzFTAtjVoIDzeWwAJ3jxV2PkMTLU0GRfVUyj7XikqIFs773z0YCyv7UM642e-57uLEyA3392h416jjvgmkQxJX6bLaOin3TfOGI6pz3RL-uu83WEiZuvrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
–
فابریزو رومانو:
⚪️
در ساعات آینده، باشگاه رئال مادرید یک پیشنهاد جدید به باشگاه لایپزیگ برای جذب دیومانده ارسال خواهد کرد.
🔻
این پیشنهاد از 100 میلیون یورو بیشتر خواهد بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101966" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101964">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ScsUOPzxFqL4hHZsg3Xt_YHa7ez6TdKuyIYb7cw4mmq6_4q0tTLec3a-F6KvyR0rV7dNG-K_dos92b4VNGxsOecDgah7d9QDC2ecKA10KB-P2gkVftqly4Oqt7iadA4oUinbFzEUiA-zlJkuIy8o-11epmGytfLpPYjJywXGMGwuMhU47LFpP5FAvfTq2-ikLdyUCFfXLMP_M62w9PJuayxSvuV7OoMQ3yDdM843nsS74oFS8sPgxPQUL8yITYg7IXqjgjJ5_e0fDGJxrHQBMgvhb9OuEdwgizMa_zwlyTEtx6eHMvoxM62oXEZ_deetrfQ9daz-U5GFxv8rA-CP3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcetmY_RuQVIKuIc0LUJC2pQeLH3hduGJw-_yeXvvylvRGdwAgmYze48lz4adVyMkhjpuQS8lAw4dVx2iJa5yR82msX6JuW-YBrgnifiX8F67m0S6MAr0mksRditGgkxaKJb-RVdIn6ZArBKNi0OernROs5eiNwpvhd_33fFnU-ksln9zUZBY__wGwZtlynv-e-aADxu30KGgEgE_us14E4zkUYlxsOjtedfxSJNjTd54UCOSw8tjPrmo0ReEXWC-DsCb8P4fHOXSwDwSDfqg0dnwsT766COnNJi-CyAaouOBjCYOJBcInYjx7frH-gc3kZpXTR2DlYnZxz2e4MFVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سوفیا رین شایعه‌ای مبنی بر اینکه حاضره شبی رو با کیلیان امباپه، آقای گل جام جهانی، بگذرونه رد کرد: من هیچ‌وقت با امباپه شب رو نمی‌گذرونم. هنوز باکره‌ام و خودم رو برای همسر آینده‌ام نگه داشته‌ام!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101964" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101963">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwruBE9RaajbYmbcT_xegnXpWVINW9a_kSsiWx-tzVMzAujGpYjxX11JcZY8bxtu-JazCNhFJlwV6-iXv9aKzwa-0a1-ehKbcZFxCoBENKdhY8hloVAQOkQ83ZuFtaXycqc7CSZ-IHhR_94qRaFRjrwnZCR7Z2pj8wws26EYKeAj4FlRUZI_CqHNu_daK29dC7u9JZfdjS6nPb84bEZsmkf_pPK-wyYx9NFVwAcK5jmuIRSq41ksiGFA0xzbN27u324grmnOL_nAn8A6ex7EsAuM8Ypl_bhVd2mIxEyqu-_WWSoO_lrZh3yPyJKJuTKkrHi5KzgFWCjy85MldbPDNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رونالدوی برزیلی درباره کریستیانو رونالدو:
فکر میکنم بازیکن‌های خیلی کمی مثل او از بدنشان مراقبت می‌کنند و این‌قدر اشتیاق پیشرفت دارند. من تمرین میکردم چون مجبور بودم، اما او تمرین میکند چون عاشقش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101963" target="_blank">📅 09:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101962">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=YE8kDSLyoVgEoHeyLM9UlK19XERYgrHXTh6rle02GGPG2yGC4aRNZefWGgLcS_0GDUsfQulMkNU9xLEVaqOiQUxR6Byoc10F9MHbJX_CC_ploqothsVf9-irUN9jcKYX_LtpKFgm4B2bClLNcQm_yLzTxX7P2Nb9yMR1c6B0DcqI_V8V3XHOTqrx1ZZMzJ2oWlAMfYkNyFH33dBQPEApf3H_7Le6QOaxBLgaS93I3FrTXhcuUFUM0WVbbyTnkMYBz3FwvVc2TSAmUYpMQ5J_6fIoXb91huKbzYtcW6Ri8CZIY7SUjB-qsDd6s3XVO84t7iUqi3By7G5mHqjnufca2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=YE8kDSLyoVgEoHeyLM9UlK19XERYgrHXTh6rle02GGPG2yGC4aRNZefWGgLcS_0GDUsfQulMkNU9xLEVaqOiQUxR6Byoc10F9MHbJX_CC_ploqothsVf9-irUN9jcKYX_LtpKFgm4B2bClLNcQm_yLzTxX7P2Nb9yMR1c6B0DcqI_V8V3XHOTqrx1ZZMzJ2oWlAMfYkNyFH33dBQPEApf3H_7Le6QOaxBLgaS93I3FrTXhcuUFUM0WVbbyTnkMYBz3FwvVc2TSAmUYpMQ5J_6fIoXb91huKbzYtcW6Ri8CZIY7SUjB-qsDd6s3XVO84t7iUqi3By7G5mHqjnufca2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚡️
بخشی از گفتگوی جذاب بکهام، زیدان و زلاتان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101962" target="_blank">📅 09:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101960">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QlK41rAi8fzGJs8DkhOpxw-WkuEt-Epvgte2WqZP8Oi2RR5bdXPDZJPlmGvWnHC5M2L7jkqKdQbaaBQN24vf0YJan_KvYCNTxvhwXCZ9J39uVkUPUwudQt7Q3_hLojad8iAJRQFcCpGBt4-l5gafxTWJYknuK37tAV4Jlu7VlRlbK6aHZZoaqw6v6mFxpTQsqgzhT8iLjpo96lI9N_49DShZ0iWr1MdipPH6ufLh2QZpRg7r32qW2CXWqNbnkIOL6cQqx4VmmR_X44uoND7OtuxbdTl_8e8SzyUvKigsx0tPmDP3PcW1QRGFT3-ZlISZIlszN2NVU971tLgnYbtWIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYkrh-rmVJ1Jyq2P1ChfjXS_2mvSwu4ntUAxTTcmmN__L-Z44uNFr9iP9iTcAZ-wDMALdhep5PEsnW5PyP6ASVobgY-PeYjzN1bnPoRV7XmK1aPKGNpZFSVr3w7gv9nKzva9FfrGDy5jwwqcV4EyKWtVRU28wouRn_ohBnIIfv_7D5izymVc35wrVX9A9dOVuE0OMo7X2fzUsj1u93xPQwxfrdrtG-T4mUxaamt1nn7YJxn0YUUD0k5mSI2AJ81CC76GfL4yLSYlrGb1QjNraZPJAf7h48p5aA0-SKtk4yHVw4txOxRQvSrR8NWKcVtwmVogUrjONGjo-f4HbnavXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریستیانو و جورجینا قراره ۱ آگوست با هم ازدواج کنن بالاخره. تبریک به این دو نوگل دیرشکفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101960" target="_blank">📅 07:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101959">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDo44yi2AnznDu23tGS-oEUf08LugAlnu2suuI5xHMe0-AS0BRoD7Mxx356dnqNHsu4QMCRInuEukvoh3pLNwx5YZji1j14aRPCm8fwggrcpr71E4rD9dTTUt-ctlKY3723siy_XMump3HhC_qNXjQ8I6n9FOuKAN4S-cNwkQxJ3y4jiePUt1-dC618C-olAls2gPA1fgJ5bEGmheUhkWZrcYEtRVM78pw9SRJs75htXm3pSP68AyRRu1gkl0FKiZhh8OwLiLLh7gvaqCfYmZRpk3otTnBx1swA5q_Tt6MFXmn7dwfWfzONQm9LXSh5IorU00VYudv_1XG91S31C8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👑
موندو:
تعجب نکنید ولی احتمالش زیاده که لاپورتا پرونده نقل و انتقالات بارسلونا رو بدون جذب مهاجم ببنده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101959" target="_blank">📅 06:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101958">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=K_gY4zoUNAxikdGPhiTC0vZlrhMPcEsWpnCPsQZR2Nh1Ql4h_wzbTZXEflJsbaRibC_4LTHnsaxMp7XQHAy2SxsVPuMHFsQBbrafLQSNHWktClKSCbMHE3iFe_HcZe0FdpDASIUEgD2ygO3GkM0DJh7Cr8AvPzeJs9pIswQaz7xQxulFji1jxoeylPw6YRBVvegoTuetHiTYoU0BFKhexodbPRbjumZdwKxRydOntbuEqdAR5FukfPFpLEGzNGBirVzzskB5NJvcC3cdJcCtJG7hEESQyNzmVynSSLPCPkN8Z0pPZEIGUg4zWyhqxbsQiEwgNVakkNYDfvE55kGFog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=K_gY4zoUNAxikdGPhiTC0vZlrhMPcEsWpnCPsQZR2Nh1Ql4h_wzbTZXEflJsbaRibC_4LTHnsaxMp7XQHAy2SxsVPuMHFsQBbrafLQSNHWktClKSCbMHE3iFe_HcZe0FdpDASIUEgD2ygO3GkM0DJh7Cr8AvPzeJs9pIswQaz7xQxulFji1jxoeylPw6YRBVvegoTuetHiTYoU0BFKhexodbPRbjumZdwKxRydOntbuEqdAR5FukfPFpLEGzNGBirVzzskB5NJvcC3cdJcCtJG7hEESQyNzmVynSSLPCPkN8Z0pPZEIGUg4zWyhqxbsQiEwgNVakkNYDfvE55kGFog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101958" target="_blank">📅 06:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101955">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bJHKRUC0H1u75UDW-90MtP6gty26tkfNtUifNZcmAhMl2gmUDgwI7LqyMyLzXEKBpM4YVFnMpQlCycVKQRVHGTE85DOoF-B0oZwJf8-IYm6tKCmzXwIjEcziIeukr4WBti-3Hiwv4cAluJZZdUPhmpGm0GbkEQRlfgVPPPTvmxDw7Lk24AOb1F4djEm-0KkZuzOSqVgEog058Jte4IwzL4YZQ1QKakAc7JeTd9QEZeaJVg_aZe7CPYFE2YcJXpG4td0Gpy2u5D62hTJmYfm53a1Ts6lijtOOqQDY_JeF_BpmwAbIlRF7_aocOmNJK66E-udqBGgQVJA7qbH6qJIjqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pa3CigfCwsO8kJOalyw3SsfSgtuA4kD9KQQpK-x3w8DkLcmG8yGv8-ARxWd_vXoBY28JbQDVKViPvIaL1IWfQurDps4B9s1YNAO1Byc4SBB4rM6VsftGCIts4FuW5t7FHlvdfPg9kD8RqoLQlvxOzPG_cFJ09ePFM4cUHd6CophN7fjhQ2kqTG8A9EQHQuapxLJNLC7kDnpQVS-9D9aHOUOpUozWa0aGO4tqytBjf85WVxTdKC77bSomjyIo42ngM1cqlHyAR8ySJJ0cUSE-v_Z5wwhOdhPqVrmS0mcYRzGuBld-G0kZrd9ncYBvN8o3kkt_ICcFjaVDK8lDemCgBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=oSVUp1p6LWJGKcT409Nm7rzIYSMFUMeeLnVRvW0za9OK4ffleYjP4WBFJke-NvwLYnarflV9bVnCbdoJdcuV4KjXibCASrdmFQLz618B4ZYsDfKNgX_rnxtfxNgh4UTuUkAriGpR2Es2umcWukDHT1od8URrleak0ok-EEeDk12FX_m58TH07-JDzW0jfHwzVSBzborGnvDt14pF8FtO8RTxipAPwX7SG_Pri9NXPsg5xvu46UoCGzXop1aRtfPEnnA8VvYMyx3nXddVm7crCRJdPmqX572B062cIxAV-EMpvEHWQTkJKfh-9M2ah-xasF6-AfBfK3gS7MuLls-Yvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=oSVUp1p6LWJGKcT409Nm7rzIYSMFUMeeLnVRvW0za9OK4ffleYjP4WBFJke-NvwLYnarflV9bVnCbdoJdcuV4KjXibCASrdmFQLz618B4ZYsDfKNgX_rnxtfxNgh4UTuUkAriGpR2Es2umcWukDHT1od8URrleak0ok-EEeDk12FX_m58TH07-JDzW0jfHwzVSBzborGnvDt14pF8FtO8RTxipAPwX7SG_Pri9NXPsg5xvu46UoCGzXop1aRtfPEnnA8VvYMyx3nXddVm7crCRJdPmqX572B062cIxAV-EMpvEHWQTkJKfh-9M2ah-xasF6-AfBfK3gS7MuLls-Yvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101955" target="_blank">📅 06:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101954">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThLxIsKt-K4B-MxOsr_BybkgHV1NcbFdrooAN_vlbsSz0wRgdiSPl4pvtyidizzxzGS7YgWuJ7srBiJX4aWzYfuynPNa-biB9CRoEM4Lw8xRZXtlvExW4Fl_fNED6LdG8w4Cm6cydZ5MaKY0_4X8eFlFcWTvdO7QsVxklYU1EVgSEdp0KkHmDE4zZjXseOCdgrT8BV-WEeFOozXAGtLBifFpe73HeNaQQvxAY5fNSL--epj0pW8p19wVKzhjuTTgaq_bEkOARRsXCG0dZln9jCkxrggDv0O94oiQXPLo0EeIqzkXdnMa1JE1psTJDuzkBlC6xB2mzPpsKvDDRNSCvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
مسی امروز اینجوری تو روزاریو شکار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/101954" target="_blank">📅 01:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101953">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu340NzGwjky_7khcc9N5kleLrSjtUHNVFlV6EHixTlN3AViceSQXAgr67875nJyQxNfkhHtxNuDoGvWsKepL5At3gRUWx2kpFbwIUZy-eFeY7ePT86JVdZWfF4kVQqw-YreU0p7RH120EMJaZEUn0NfXN1qMf34GuUrmW3D5HY0R3fO3wOH9ta93dd8a3AY91HVVDCx0EHHm5x_fQKkiQvTLhNACRcmYDTpB1SZuIous6mqMFAucrNE6ow7EQdUmjYaa4SmeKD0_xx5e3bywpuLlNw3n7LVtgh-jJTCjLLtk2OmQThFjf9EKJgBqIqAXeS3vqr9T1bLOUCcpReGWYFTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu340NzGwjky_7khcc9N5kleLrSjtUHNVFlV6EHixTlN3AViceSQXAgr67875nJyQxNfkhHtxNuDoGvWsKepL5At3gRUWx2kpFbwIUZy-eFeY7ePT86JVdZWfF4kVQqw-YreU0p7RH120EMJaZEUn0NfXN1qMf34GuUrmW3D5HY0R3fO3wOH9ta93dd8a3AY91HVVDCx0EHHm5x_fQKkiQvTLhNACRcmYDTpB1SZuIous6mqMFAucrNE6ow7EQdUmjYaa4SmeKD0_xx5e3bywpuLlNw3n7LVtgh-jJTCjLLtk2OmQThFjf9EKJgBqIqAXeS3vqr9T1bLOUCcpReGWYFTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوکاس هرناندز: «کیلیان، اگه قرار بود یه تتو بزنی، چی انتخاب می‌کردی؟
🔺
کیلیان امباپه:
فکر نمیکنم هیچ‌وقت تتو بزنم. دوست دارم مردم من رو به خاطر کاری که توی زمین انجام دادم به یاد بیارن، نه به خاطر تتوهایی که روی بدنم دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101953" target="_blank">📅 01:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101952">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQRD_hYiK0qnZmiZ_fUwuKcP_doFDbHqKiwXiuyizeCbQv6MimLPZtyr-ZcXEib4CQ8GPF7vx-vhHW1oOrVCYBf83fLt3fgfLNMVr5plyzO9XD_z9_mffwTIWUluPdPMhrXQ2t4rGvim-q7_-5MRQV53sorlRB_z3JfPL9Q37_vKSwRWtmcBURp3IktbyWZYfJZ53L_JZ6cD3uf0ONurA8rmE6eXD6Wr0ONV48Wl2gABJWwj88Z-JxJS3Fy06br5-FiPhSwQ3ZH37ZSUhrxotBNqt4RTzK9vyTLyWie-9gWg0GHUNXgtTrL3dZs8HJlrdBpeQlf4MB8bChhMqKfFDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
امباپه و پارتنرش بانو اکسپوزیتو‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101952" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101951">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHVdi2VNuCGWJrzg7tKXYcP9CGPf2lLVheP7o5Fr8CEJI3-Oj1DmjHNONM4GYcddcjzACZ8r7-q1eRu7stIDovWD5rfRNsrx3zBL5UAtdN4Iwp0QjxKn8DQUTf9iw4wbK15TqzE-WhK4cFwHZ8oOQm9xvDHhjouX79Tmb0WNeYA2wJmIxapesyWrDX5Yt-C-TDV2z6deUwsX-QZHOETB-9w9wUJw8f4nwTUByGkIIRXYQHMjbyQfpZpmldc09X6E2BJLVbzxc2ZAOQVO3PLbM3ohNw6n60P4kx67cqqPBJwtDCfshPKuVmJNSMiQtNiMSl5hQaA2KQUqpEmSAXnIaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی خوشتیپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101951" target="_blank">📅 00:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101950">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63dd42dc4d.mp4?token=U1DkGoKToNSmapbQRBevyVgOCjf5Js3_NdMc21WX-OBVHn4ZhBmq6Gwgr0V4BpP3X8Oeq0BJvqi2WsZojWUWPDkPXSEhy21DM387FsoXzFe0zjtxdPk_CR2xg1wGzgBW_yUCeGdumI2BABd-hu3C7UhEcO2brSjUqROqkx46LuGx3hca86EUCn7qtniRjy57AklCgl6LwjDWCJccFizmZQiqT3bmw-m-aQdrGTb1Ydx2crPOBwUayrd2m5Ns60MNbjF8Se5p-FmhujHDTezdsGULA7d_FYvdI0CogYMLlH7AujB6mi8_kYJTkMC8TwZNTi2NPV8bcHnpMV9yDiMR_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63dd42dc4d.mp4?token=U1DkGoKToNSmapbQRBevyVgOCjf5Js3_NdMc21WX-OBVHn4ZhBmq6Gwgr0V4BpP3X8Oeq0BJvqi2WsZojWUWPDkPXSEhy21DM387FsoXzFe0zjtxdPk_CR2xg1wGzgBW_yUCeGdumI2BABd-hu3C7UhEcO2brSjUqROqkx46LuGx3hca86EUCn7qtniRjy57AklCgl6LwjDWCJccFizmZQiqT3bmw-m-aQdrGTb1Ydx2crPOBwUayrd2m5Ns60MNbjF8Se5p-FmhujHDTezdsGULA7d_FYvdI0CogYMLlH7AujB6mi8_kYJTkMC8TwZNTi2NPV8bcHnpMV9yDiMR_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ری‌اکشن هالند به میم هایی که ازش ساختن.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/101950" target="_blank">📅 00:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101949">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drOOXttxm5tw1Ef24I4oPsaWhksr0S6Ivwv0QrxLQg_ZmarKePU6BXGUF8SizaTMpVyQp_22ggez9znSTr4JjBGCWcWazg9xnpoMZy27Js3JK3eFhEnoJHH3LIDQmS0CqMU0OPV3MA_4Lo8NsXtPApzwOGEdVjPhD534o1hXl92LqDfjVV9d27LOX0l_SutExNbusWOT9bHZzVu_NVobkJ83BPnR-mjUnF1WhBL3JgcLZqCxJK3de2uPPIqpOAGe2bGQ-s3qw2-2yCiIiPwXG2ZcxWpNIhDy982Tfa40bZkpAOSFDbo1HQick5tx-_ck4_YzCZOPKfoVrqLiUPlE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/101949" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101948">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlgS6AdwyTMMp9-_tLRzGILQxtthYuLFjeEWFmgO4TF6LG7cRYKHax3cvh4mT2qmX2g3wLKUiAwsaNaNph5fZsdQPIu6MwoyqcmPJ0ZCaRK5vgVw-CxR71IZwr6W9WEqJs9HeqSDq87_KNPQ2bXGdwUBFpEDb5deaHMV4s6lnJkQvhrYkcudIcCTmlHoCMnN25-NhTScUgURwZTQNwRYMjagld9U29cVVqzR4-0RQ8ZU25HZSqSrHME_jFoK7mesSq_tbNE_QR2Gbp-tOTHQlDTKMEAp3rEK8G2W3a7eb6ex3nXOlhq0H5AFIlA1BMqL96LtMBYjnOki3DJwULReCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔹
ساشا تاوليری: باشگاه الهلال میخواد مبلغی در حدود 120 الی 150 میلیون دلار برای جذب لوئیز دیاز هزینه کنه! اونا بودجه 350 میلیون دلاری برای نقل و انتقالات کنار گذاشتن و این تازه آغاز کار اوناست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/101948" target="_blank">📅 23:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101946">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/daDKPPPRjAzvZ_ZKFYBw4hUbrfFv8uwKp3b3JSTnpQc7YyMISR7QD6rNLfS0d0p_DTopVeWCD6RvPO-acOve33AXo_wkZh4P7pXAoJrO4WQDxnWWAFhW9tN1F3dxQXY9hzGBp9lJlzLzdJVq2rYn_RdZPtZ2AaO2nVCbYKWPd-KTj5cA-47j5-NYSKzWSiHBoMm7J-7l5_tqwYo1w_OO-UII2IA6HXThRqMI44Cll6eynBs9Rlz2L3ECILSgrlp7qOCWR3uKZb217hvLhWvzhg2PASyziH7omQcUgjICc1DfmBx_qNghIRbuoQ6HrG1Tpthwm2FDBAaLZMyKQf8XZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LE3mn9A84KIGIeB0ZQVXsYX9Uf_sg53k53niR1pZ3onQJ_IJH5TrTKrksYGUcZUbDD02VQBaWd796syQ62bfBBNggDmwvnCGk9_OzqmI8gIIVE_LqEc5NNHNrJZNWEFZ0NjhnJQ0Gt0lYwG4tdRC-lj2ybOHKdiTu60RM1S6LWgeHeiWK-_2swlo0zyNQZ8Htf_he211M2NjSueD1QEjruTZRFLmwMPLdMzEv9dkDhxsv_Tt8ewhY8h-J0QkkcA-FdimbgjlMOX_gGBQx0R9YsHrst3nUJpyb0ZXbsq3LAr0Z7vRB-ftcuKgPN4GxA3PLOVxV7uJIHNoMuqd8YxpsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سرخیو راموس درباره اینکه بین کریستیانو رونالدو و لیونل مسی کدام را انتخاب میکند:
برای من جواب این بحث خیلی ساده است؛ اگر فردا فینال داشته باشم و فقط بتوانم یکی را انتخاب کنم، کریستیانو رونالدو را برمی‌دارم. مسی لحظات جادویی خلق میکند که کمتر کسی قادر به انجامش است، اما کریستیانو این حس را به تو می‌دهد که فرقی نمیکند بازی چطور پیش برود، بالاخره راهی برای بردن پیدا میکند. چیزی که بیشتر از همه تحسینش می‌کنم همین است. استعداد یک چیز است، اما در اوج فشار درخشیدن چیز دیگری. وقتی کریستیانو در تیم تو باشد، همه تا سوت آخر به برد ایمان دارند، چون او بارها این را ثابت کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101946" target="_blank">📅 23:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101945">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1ZRCfQJ8omOm_dvPFSNYkYn7xgCYhwd0dFQVMJ2_jLrrC-MahssrCcdx5279lYNvnJel4pTZoNhqVmAKoqlXkCRR1BPZO2lyYt0h31UaYPogXkTTR9onMALcCNsgnCKF6x6TjSDS6aIVo6owtzBO0Ps7Nttfttw5tHViStJT9sT6feL-Tkg9ceS3gyTfziy517inZmI5Mv5dnpdC9xXdN28wqwuhxmk-gA_a8cskg-cJsPW1UQmoYBfO6wcMLlMnQ13lV4oM3jg8jGAB2_pAVTNrLxUzAdiJ6YXHvjcSZH6bRISRCAo00Dic4d8wZPzIQO3_Bxd6Qp8RCTnVDIoHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
به نقل از فابریس هاوکینز:
مایکل اولیسه تمایل دارد به رئال مادرید بپیوندد، اما بایرن مونیخ درخواست او را رد کرده است. رئال مادرید تمایلی به درگیری با بایرن ندارد، زیرا رابطه بسیار خوبی بین این دو باشگاه وجود دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101945" target="_blank">📅 23:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101944">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amwsLs15vQwerunlIBvfiHwVrfbDj4_jrXo0jOBRwbRN7sC0QbMAxhmDGJio0PSU7weI6-XAxi3n9jtLaoO8HkuZuVilfWpSQDMugiM1NE1_F86b6BMAsC85fFwnP41j1vV1pPCpPpOdGM2SZcX41JQH8nQpYXX7rGn0u48r21VibdbQlfs0Ay194INHejYTwAQCVY2sAijo0VK6FEgLuTQlDwMpbnvnaOeo5k63f69rNYefmgIfz-hQWNQAoMZY9wv8jJDpXikkR_Hks8vspYGYwE5t87CRPdzKrvtJV4E2XsLtt1qcHwCuHLCM9bD4NslU0uUfICF9XoZP-TXMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101944" target="_blank">📅 22:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101943">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tD2iLGYQiP8MAu8xXnfZn8HIVQc0Sr3NzvpBky2b-wNdn1HNoIN2Q1PGbb_Q6cwiD_4e3xUjBsfre4J72OkZN7fKYh-aTC8VG_I5jUs4xWlb_Q9MhriLGiBlm_NAwR7QQlz7QPMMfknj-AG4AL-iT68Kehyo5_lEbGZNEyyjk5QzcTrbJTcwSTLE2YZMNZONT8kk-rw0zbtCfc5LFJIlndgXERWf-qeKRRfnctX1JAOuCZ0I2CPpRHwG5uNDNyANtWNgztJfCrZDN-33cIp18BoXYZ4wQeM7r4rCh79_tBnR_wOwyvrCm4WAvOjEg3Mo8MrlG6Biloah3vSxmQxzzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
رئال مادرید و یان دیومانده به‌ صورت رسمی بر سر شرایط شخصی قرارداد به توافق رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101943" target="_blank">📅 22:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101942">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOBU7Aa8Ro4xj9pi13IBvVBfjXq6RG2MacCHhWiQ6nLyG14Y7Pq3MU_E1-YrB3La9WC-t6d0fYkNLeGc_0F0NyVTxdzcf_BzWu9YFib01-NAav1ja7bb8gSwVbUDBBNF6pyBjGwo9INJOcXrt4x-ygMg2olaI8RF0zzfiDtkl2LjaBvw5Hr2GopkwMo8VYFBMv0ArUeEjrEvPcaeDb8AfTzT93Q4XNPjIUdmtl-ehrpcevbgjV2ev28YNKrIB-OpPdiPj4G6d-9vA1PQSfyz8W8RqACFtN3WEuhdNgvib0Q7Xe4t6kMHI63SQbpVuHitcvb9bs7Ty5_JR8bcB3JrXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
ترکیب احتمالی رئال مادرید برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101942" target="_blank">📅 22:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101941">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d89mPcDDMVRVovn7KqjrLv6ZHx07m2yXhpmoE6UYp37yjY_UoD26maeWQtXgR_X6sHz6vRM3MNYUz5thq2URX2PNWjS_Lwc7HGevvj2qCNuTUznApZtkEyMfJGgHYBV--viQ7p31NHjPojsExurJKdDpZ262Kb5S4k8cFl6Qe4imwRrBvKmAdEeDkMK8TDxpkrQ78tYRkFqfslKdtqkULx6jgtdiN-Xw2UKQoRAKZR2rVob2-J_ItdEpdZwv1xruUaXQc7F_0jLIPZ8PEXbd4IlYA__CvvvToHuqhafy3izaThNrY1LM-SgXFUXyc9ufS8EzksmfZmUPWnTXP8-Vvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از قشنگترین تصاویر جام جهانی؛ مارک کوکوریا قهرمانی رو در کنار پسرش متئو که مبتلا به اوتیسمه جشن میگیره.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101941" target="_blank">📅 22:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101938">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSAO37rQgqcqUP0SvsU8swIBs4J9CrbINsKxR9GdO_W6otGAXV2hXooe2o375htcYDBpqlui4kD6TIvNO4VcYucvLmuM-sCMky08qdvH6IQrCVgDxfwa9ceQqwcIgxVqeudwcOb708ggmf6xB2eY4bt5cUdyJkVaeTF1yklLZ19OJprS1e-u78RfPkROch1dqvO1JFkBX2Fbr9jdvkrurmoyi5VvPXG2SOAzzNmna6Mm21fjH8zu4Ixz1nPYXqd4NHPpYim_JWCGJj6HkOpQ03V6TabTUax7NF21VuJu3wO2KJEAXUKsEeL4u07Eou2zGMZ1b2nlxBV2dbkiw6hvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/leoVh6TF63MQSN8T9I1aZb0mrrK-emi3j_PYJC7ty9w6TGQdNUdEGGVsDh3kbRKVNaXIgBqZbl7bHQ3znht2jVrKPr8D-CDFgrz7yXOLJxeEQOJyRtW8MTJdUVs6nbWH_cez7IcCbo1avvsKJsvs37m2KGNZfa4Qx_e2jc9UpLPNxsx9W_BwPyPaT8M1aRYNgg5F_Q9xE9TJOr_puBF16k2MVA7cdxOX4cCuq0Hp3MJ1SFcTp7jDaceEzcrNVpL4tgYptaHXwD4RDJ-wKRJoJcVzWem3LCTPwBMA7pVk6iNuA_VZJTSZd0h0E_f9qSNkiYFuU8pKuWLvsAI9OyZD8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EoyXsb2Ypqm2lXnk7yi3eld3wc5lbzO726xtJJZbihe1AOenf4Hk4VFA_4MaLf7WIWhrDS3KBArLkwIwClj9ChZWXFAX44oT72eW5vlYPaGtioeUQgNMtGd4kIpDIj2g6QsONS4b0Aw5oBcpFlIN_9TJ1d3tFNjKJTjfbSS8k6GBvCZSzaCydO38roHgffUwvWFJo-v89fNgbC_F38zhxkp0P-YUP6ZgkZxfL1M0e7i8Ex9Bt-7ciILgbX26wRlC-CA1y_hjxMQOatT7yPH1orYgGZs3tUJNm93EHKdYmNvZnRd8wkdXeIzTiHyYUjF1TugoNkcnfMuASDx3b5NfNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇳
😆
امروز تو یه حرکت پشم‌ریزون دانشجوهای هندی تو اعتراضاتشون ضد نخست‌وزیر هند، عکس امباپه رو هم آوردن و محتوای بنراشون هم اینا بوده:
«دیکتاتور امباپه شکستِ سیستماتیک را تحمل نمی‌کند. همین حالا استعفا بده!»
«۱۲ سال در قدرت، و تمام چیزی که از مودی(نخست‌وزیر هند) نصیبمان شد، نسخهٔ پرمیوم امباپه بود.»
«دیکتاتور را پیدا کن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101938" target="_blank">📅 21:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101937">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRu-MkwMKsdNSOdxScXYZs46_UofXLP-P4HeJrAM7cF0jRM-YLV462Aub-69iI3waFCejAWeNgrGrnnyVC0qGQ4ep_G5etq6aCSsJnfpB2u2DjsSoLNEVZqItxne68Cu-6sI3jTkBmQ_GJ6D6ld7UbWiLGMvWo6B1KA8kDllHdzTeV2mhyQEPoy_AEj6z9meesCV5VxiagsiIj5EFcW-6fj4gjcCuS9sknOAhBnVYQGiQf8n0IbSS8bgnVDbPH5xuYLXs4C5qJJnYDGdwr6LkraXXHSJ8SrXIkEJB3lwYpzOW24mpIcaj8l3ZxARPfBYxIHAesoeG_Ufcg5Ls3dERA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلاتان ابراهیموویچ: "بین این دو باشگاه، این سوال پیش میاد که کدوم یکی احمق‌تره؟ لایپزیگ که پیشنهاد 100 میلیون پوندی رو رد کرد، یا رئال مادرید که 100 میلیون پوند برای این بازیکن معمولی پیشنهاد داد؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101937" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101936">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGD1OF6ca9YhORjU1QuRbu4ChhR_vTCdE9ChivIzFLmB_QMJGCFPgWB__PotVF6HAPAwluIH2uyw_mJFwGOCFXObyQ6mzx_Pzl0kg5vBR0kQN_MMcOYaPDFSLgRvmi1LtR8eyA5NKGfvZGMNdlBx_I97qWj55CqX9bBnm5chTV1Ob6uUkH31BxDfPjrox8cxKlT2FIujMtlQzBNcxDOGGZsmiwCZEF9rMlp2xonYHYYwLEfpuiZ9dpfXMrt5VHSMZjFg6JeO1pYjiDZRza_1ZGd2_qJsuowy_xJgs-itF1AGEQqUsqNia-YMILfO2ywpGXHOqsMOxV82WIE1FADMlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
محمد خلیفه، گلر جوان و ملی‌پوش آلومینیوم به استقلال
پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101936" target="_blank">📅 21:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101935">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHR4Zz0OBUEZfX1Sj_lM--8x-y6pskjZK0b_OTEL9QPCwkTQDWP0kxgo9mwDNwlKRr5Gbc-NroJoUMEIrzgBVV0ePKLNLZHq-YBBwoe_7-k6-vnieAkS7sh2zOiyzGO7nvuX62WH4qZ7k-l_N38K6zx5pWVW3Ktna1OwujKYYdalSUCQaZvjmp_nYuOq4JL0nbGUi_wwWziDb46QJoYW3BDzz_bjmHAOMmsLwe2gmnK9fs_nu0Wu5Lwx0KoiW-6ywYEYtRuQYwVlL1waWbZuux1tAONgafGvPuMZitKOOTo7emCZHJLoEv_wo6T7FSuXkwjdZZG4PmLOPi6SEIzisQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ماریو بالوتلی:
یه بار زلاتان ابراهیموویچ منو با رافائل لیائو مقایسه کرد، ولی جوری حرف زد که انگار می‌خواست بگه بالوتلی بازیکن خوبی نیست.! منم فقط یه عکس از جام قهرمانی لیگ قهرمانان اروپا استوری کردم و زلاتان رو تگ کردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101935" target="_blank">📅 21:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101934">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLPIff1SYNQQ0TDwC0cLKoKCI16j9w0M1djszE-z_2oQUnZFpHbNKhjT-I0bMvgQD0b5fZzoG4YztfUxlSQfu8UA0ll5sph8jrhHm1fYix9qwMcrUAncIK05sEQWsSFPJYkFmd2gZOpno7bnNUTLn8pBuNLMg-sHCF63rSknFjt7NSEVDoKhnU6g6ehYfdVQoAeXDp_9n5EivBssyeqBw_nC5d5FY2EwoWu6x8_Ns4dyp7RDZK_bZE-W2hpJUC48Nfoj7bYXjJNbUZ7mAtTbsvxIHLf1-00W-Yyz7oeVT1iY2MdGfTOazd7dUIPM6MkQBqnDR8vNVlhKS_wF3SHH8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
کریستوف فرویند مدیر ورزشی بایرن مونیخ:
اولیسه به رئال مادرید؟ این موضوع اصلا برای ما مطرح نیست. او این فصل هم نقش مهمی در بایرن مونیخ ایفا خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101934" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101932">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oiVEVp62yKxQgHUegt1H2Y3OPKdkOVfNc3CVQrnEgN5T_2B19ZUTwhkUlpumTicxNRcNBDiIhXEXUPR4RfFD0UMH3l7VZf47p_75SMEprs5ZHbZbaN41EikiEFYoT1AwIYt9p7RhcO8KTxQWap3EthYbrBk5IPiMCxS6o24TUuaquHbw-1JWUwUaMXGQSN72m4arCLzjrbwYZLlt6WR_ee9yi9hEn8P1IVBILdKMXXa2Mr97mIpX2slVTeWZ4LTm05C6RXjQDE2az3cXpISAsq55WmWq-5jkEEp9OJNc9yU4Vp9-cSbC2Hp--Bi2HmzYXA5aaj_HAsenqNja-_Ru5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfGGxa7-G2lkUsPjxwqyYqS4OUgsbXJ_XyWswZAXGxfhx-ZESH4ylzKV-PSh-KmZr2-6Bo6s97-UJZVYt1Lhu-klP2keb-N8ZE6CrSXXPWO9fMzR8wPZIKVZrxmxja0UfCYk5KBcKDbROfp2DZy_6KKDHty-nOgdFtg3cdhyLWd57YJOuHJR23gtlzg5e7QVGKafbdfr4Hwk2oMSp926wo_rsTM-WH2zGT0XiCx7v6iiGXz-G9vbXkgzKonzPBK_oWiWJF3fXLb2Ih75MbUCHLM971289Zu-qIIHEtx4j2xo7MfAvxbaZOJRuVYaANzs9bg5gmgihPvNczsORsP_VQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
براهیم دیاز هم از پارتنرش لوز مندز خواستگاری کرد و رفت قاطی مرغا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101932" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101930">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7aT4L1eTWOpgBUmQ7amlG6b1kDK_WHyH9cbQH7khMU_Xu9qNESlvh3k9IiAcjUMr4ZS3aG0JVvxhTYBI2gQGqxmMGne8gzCujFzX5rbM8s8lzfNl74SiU4-Zzlj2UO-iuDVbNW4sbrVdQlGhNSkPzUKpdE3HCVh6t0x6RpXMKW_qppKOHnhXnmYxvbWTqCPRHtLhdAJ8XxLTClfUgcNmbFPrIp8dUN7IRMSJliFHG8cWV7z4MdcwQKasNOR0M2CW-80GOJQGnKvu9znhm9g_HnGReWyxjCVum8fPpURtL8ZrmBBsxHzTz4o152bTnrcZEOYCFDpCXp6Jba9M93SUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=pyWMzWQiCBIbu3uL3mPkSOsfQg2PQN7Q4yE1NXj7PPORcPKcZ1DT3m5GkqJPYxGyX6UZL59Dw78mXZX0aA4AMTCZNKX6snP1zdnhqXGFnW4WD2_JVKLZJd5gv2PrGLFp_tjaGfBuXw9Lp_wQtPUj9lw5Xbz7qkYGgo0Mfxx5qNhOnmGsu0D13E7o9tAaHPAplg2bg19NTviYnSfFREF1iwf2F1B24HBdaWe6bVFO3QHHlRryKv4Z5ud0p58MNAy3ikvZ1e9PQEizyLpYRmNhLTpPML3ZnvICfI7a6jz9vPEzCib2PgtGZwJmNwUE9L6aazeCD9eJRfev9cykZw40LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=pyWMzWQiCBIbu3uL3mPkSOsfQg2PQN7Q4yE1NXj7PPORcPKcZ1DT3m5GkqJPYxGyX6UZL59Dw78mXZX0aA4AMTCZNKX6snP1zdnhqXGFnW4WD2_JVKLZJd5gv2PrGLFp_tjaGfBuXw9Lp_wQtPUj9lw5Xbz7qkYGgo0Mfxx5qNhOnmGsu0D13E7o9tAaHPAplg2bg19NTviYnSfFREF1iwf2F1B24HBdaWe6bVFO3QHHlRryKv4Z5ud0p58MNAy3ikvZ1e9PQEizyLpYRmNhLTpPML3ZnvICfI7a6jz9vPEzCib2PgtGZwJmNwUE9L6aazeCD9eJRfev9cykZw40LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برگام عجب سلیطه‌ایه این! اینس گارسیا دوست‌دختر یامال، بعد از موج انتقادهایی که به خاطر جدایی از دوست‌پسر سابقش گرفت، یه ویدیو منتشر کرد و گفت:
من به خاطر پول یا شهرت لامین باهاش وارد رابطه نشدم. خودم درآمد دارم. از وقتی با لامین وارد رابطه شدم، بیشتر از چیزی که اون برای من خریده، براش هدیه گرفتم. کلی وسیله گرون‌قیمت براش خریدم، ولی اون فقط یه جفت دمپایی برام گرفته که حتی ۷۵ دلار هم ارزش نداره! بعد هم برای اثبات حرفش، کتونی‌های گرونی که برای لامین خریده بود رو نشون داد و در کنارش دمپایی‌ای که لامین براش خریده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101930" target="_blank">📅 20:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101929">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJ6keJNmgHUHwdeGP1F5I70pZrDPbeOkaljUwBxqYC3UnwsnKpnQQemaqfiAYhJmw5LTvZcd44YLw1efzd6o-mIEDSpKiiqJUCFyviW9s34pbthbWB9666V3xb_7bkr-YDGQzPilYsbBHYS28blYLEglyWvCnu9UBC8-T9-xrxIUWOEEIXgL3GrksW67dgWmXv-RtK8F7XqykC8PVSZit6OSfdM7jRurOYx1SeYVgh_7EYvORO0AGLVvjiSDoTl3Vie0HGJ-90AAnLEhLDM1_iMt2saVx2znW7a-FYZmXyM6TBWc8NgdUdjbBEK-OlQnycgGETLBUbEt4oyUzTX6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پوریا لطیفی‌فر هافبک گل‌گهر با قراردادی ۴ ساله به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101929" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101928">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62941770b7.mp4?token=DECJ-FhyyjOEX34nhUWlgS4wcD0jD0xSVixNKlgockUw69pwm7DIVaNEmM1E2TkobBVG5huk2hH7jXeU9sVOOM8v8W1R8EF8Stq2USCHHRrApv9_XlY1VYSoN_Qo9CxNEs6iBdn5eE42i6q_iXgbH3gLGaVLiYiWUR7PoMbwQfcRosjWEoPh1fV3vZAdfZb3_QwminOZsNVAIpSFZyuCJLqCbsc7PnS-RY3QHHN3Qq7tu5T71MpEC8EAlTI72nSc2x74gj5wF4PY_yQbI3KI3Rkyp1ygcLMJsfczBS2Ohi4B49M9X1IIO4HU2v3vHrwp41wodbBMTcf-JNPJwwQr9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62941770b7.mp4?token=DECJ-FhyyjOEX34nhUWlgS4wcD0jD0xSVixNKlgockUw69pwm7DIVaNEmM1E2TkobBVG5huk2hH7jXeU9sVOOM8v8W1R8EF8Stq2USCHHRrApv9_XlY1VYSoN_Qo9CxNEs6iBdn5eE42i6q_iXgbH3gLGaVLiYiWUR7PoMbwQfcRosjWEoPh1fV3vZAdfZb3_QwminOZsNVAIpSFZyuCJLqCbsc7PnS-RY3QHHN3Qq7tu5T71MpEC8EAlTI72nSc2x74gj5wF4PY_yQbI3KI3Rkyp1ygcLMJsfczBS2Ohi4B49M9X1IIO4HU2v3vHrwp41wodbBMTcf-JNPJwwQr9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
استمرار، استمرار، استمرار تا رسیدن به هدف
این ذهنیت منحصربفرد ترین بازیکنیه که دنیای فوتبال به خودش دیده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101928" target="_blank">📅 20:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101923">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xna6Isg3Lf5uyt6rBQzUTYw1zfTDXLWHVZ8vrdmNlj1aOVeNOmVfHotP5ZNYUTTiGyC_6NuButO3u1GKk_jVFmce5cvY_JH4mp-sY8TIuiywC2HC-7bNMCEQzHhl-LqR0aUqHQpvLiUIz0ihsQWFOH7yQ41l1j1aSfBi6bSGh6gLRWo0vkjUV9HHvX6HTqD3FOxEKA0kTTkZtkUW5T6Y_QaHqoUsSf0vGl1YMzI-z84-Av4Qjzsllzz7i_a_Bua7z_lUKeR_IWsltV2kCKcdKsH0s5r-b4lodz6_S50uUNIzN99Gw3V6N0Si-UNN12x4AIejh4pjYcJdxbhOiV5w6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MprDEw6MNblnItEmqFG8Ry8pieKx88Vpv2gz0xqVwQrE044P_ihsxPg0y9ZlUl3sn9BFO_7gMUUbbLFjoR-NLizNAc_PMfITsAuRZRbxYOidIvifTfVhtsF8eXVoZ9m26sS7OHI0RU_LEdIrNTVuC2a_FtKQw4FNnkU9aBgs4QAxbF1PQaFb4jdnk7hlc4qGc2lQvUwauUZtaw8eZm0Jhx6NPa7AoJp9RLKLATjdI0axmQ78x-H-ZOn_nVsqUcIgqJ8bGv_gu-V0kr302SP3f5RrfNTs8Mxsekw1fhlD9lJoVOknITHVyzfHb9Y9MeuNXRpsfslBXcq94JSDgMEBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IBRnzIe4cjcBbSD7r4zu2DQzAt02koZUn5L1U4iLbIRmRHU56zhnpQFmdsHmwBn7-YL6Il-ZJdcdp0UpC7nLUuKlmljVux-wTKDqGxj5IMNE4KcfH3TfO0x3arAuaXEtuhWBLthqkRZh_EAPpx2WL1TqTsY7y-AHEzK8nRF-uUACaLzf-OdG9J_SyqwfuCGqLTYKPfOOsIW_gfjP2fpkwo0VgsBD-ZS2zv-3KvU5lyIRJdUwaiYos7EQHt83F5-Sb4-WcqV5n2BRboXuEuUqCJXP3GfUhQNjRoidCIUa6Sr9FZUzIby66Q0ItXcDEd5qP-GPLR7hEW2xvUZkZr-ARQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=Gl56nOddLnkrhBwnZ35R9zD20PHXJBmBUHdbbG0LJgCouLvMA6djLfwHJ37gcZlq19NhkkEcwpSk1WpSxdkypMgEC7n7vnL5YyiiQhS67UEgNeboTmMBnv_WuGeab4nK4cNUt-__QWelfZP8msybSc37SjfHbZGjNJXnNUw_KLimqLyNOsO49FxZdkfBY16R46blmJOXwN89hw4BSbHev00Eeii_e3MdpQRTmN0VpQJwm27U3ksgqxyIxcq8jJ25FXEe_LL7pzXLgpJ5Jit4nKS4Wj3UCrrJjkmMQWi6Pqfl06zlcHoacPL9cHJ1JfYbFpuDnM5L_HzkG_2dKC1k2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=Gl56nOddLnkrhBwnZ35R9zD20PHXJBmBUHdbbG0LJgCouLvMA6djLfwHJ37gcZlq19NhkkEcwpSk1WpSxdkypMgEC7n7vnL5YyiiQhS67UEgNeboTmMBnv_WuGeab4nK4cNUt-__QWelfZP8msybSc37SjfHbZGjNJXnNUw_KLimqLyNOsO49FxZdkfBY16R46blmJOXwN89hw4BSbHev00Eeii_e3MdpQRTmN0VpQJwm27U3ksgqxyIxcq8jJ25FXEe_LL7pzXLgpJ5Jit4nKS4Wj3UCrrJjkmMQWi6Pqfl06zlcHoacPL9cHJ1JfYbFpuDnM5L_HzkG_2dKC1k2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدری تو تعطیلات در چین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101923" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101922">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xa2_7SkyqPiNneqaL7SBR56AIGL6d6B0WYcDZc9ZzPOjo8JGMm1WmuIYgWJGBLrc5FP3NyRyd9BeacwgC3_npknbZTPpK-zzgrCwv-AmIKFcKd0eK13xpiDVUHfZmIP72MiO3QArpNcdwFnVe_rWAZ2UajTKr7nmc-9Xe4qVGn2lsYNQQkY-ujTwqVhR1_28uaBFNbvyjGfa93LEeqTslAsbme445rwM5MGoM1h5z6PEajlVaZgTFLp0Ttg7m0cEQMpk8UeXAAaFXxSw2Ian8JaG2DGmcyfgMeGdarPg4zEiLXNzqvYGqrkU8p4KafO-Ju5zhOzSmXNU2xKyhIvK3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔥
همه مدل کیت فوتبالی فقط 570 تومن!
🔥
⚽️
از کلاسیک‌ترین کیت‌های نوستالژی تا جدیدترین کیت‌های باشگاهی و ملی دنیا با قیمتی که هیچ جا پیدا نمی‌کنی!
😮‍💨
❤️‍🔥
👕
کیفیت بالا
💰
قیمت مستقیم از تولیدکننده
🔥
تنوع فوق‌العاده از تیم‌های محبوب دنیا
✅
دارای نماد الکترونیک
✅
امکان خرید حضوری
🚚
ارسال سریع به سراسر کشور با کمترین هزینه
اگر عاشق فوتبال و استایل فوتبالی هستی، این فرصت رو از دست نده
👊
⚽️
💚
کانال تلگرام برای دیدن مدل‌ها و سفارش:
تخفیف  ویژه  برای سفارش از طرف ما
👇
👇
👇
عضورت در کانال
https://t.me/esportsofficiall</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101922" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101921">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=qzrWEuvRyYWCvexdemwzeup4RB28uY-GOQDlouD4E6O0dC0NXGKsVGAhBs8FJzi6I085CFgQW8PBnQad5crbcQrnequcn0JK5yrhh3mEw7m6TG-PkRDGBv-GJECnPfyfOdiY0tZi3K77qFQ1z1_G42PNKl3vO7ADBqNK62O8TweOgE6f3EE1h8m-TaUVJ7syKgX5tSVlw70EyPCpU5xg9NHfXqPiJ8kDVcSFLYTZFf23GBZUIwg2d9FiZKUBfADIK-i2vLh4gLgIDAAhv73NUYhJoL_GEhf_8wgv5RfElCJCjXb9byfpUG1igIHaF2TP6UxdMFc_GUEn-AeKFU0ASw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=qzrWEuvRyYWCvexdemwzeup4RB28uY-GOQDlouD4E6O0dC0NXGKsVGAhBs8FJzi6I085CFgQW8PBnQad5crbcQrnequcn0JK5yrhh3mEw7m6TG-PkRDGBv-GJECnPfyfOdiY0tZi3K77qFQ1z1_G42PNKl3vO7ADBqNK62O8TweOgE6f3EE1h8m-TaUVJ7syKgX5tSVlw70EyPCpU5xg9NHfXqPiJ8kDVcSFLYTZFf23GBZUIwg2d9FiZKUBfADIK-i2vLh4gLgIDAAhv73NUYhJoL_GEhf_8wgv5RfElCJCjXb9byfpUG1igIHaF2TP6UxdMFc_GUEn-AeKFU0ASw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
تو شیراز یه ایونت ورزشی برگزار کرده بودن که چهارتا کم عقل سر دختر دعواشون میشه و طوری همو میزننن که کم مونده بود بمیرن‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101921" target="_blank">📅 20:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101919">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tmi3fb6S3aMMeQsY0p_EdkoMWrJ2uLNuzghoC8QMhJohBFZSBeSmTR9h-sHcBLhVVgfYeCiE93_8mWR2-eWC13JXxE0CPrI1ThPXzLmJXzW3TJfXRG4CXXULVadbI4hmOBk2zdnf2lnbZm1Z7lI4pQRnpjK9kpZM1djFi6c5rNk-PhO4wS_SvkLL8iLcUaj9RuZcdZcy1R9yr_VJw9Yjj1b9EEVkG815haSKzGNk5CdhAAGxug9n8nAMehkxBFsjNdyjDQzOllmxxbf3AuHL0Vy56T3jbwxkquUpx4vGm7ILeXXwQCDqIpryXyCfhBUJ8Uqs-GulRCx7f6OXKafX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jpl_mg3a1hIMTtYn1q2vDq5nILJbDyinGClU_g_cK-BhBw3AIgMc2XWEKWFe-5fTAY6IqVPVAIAMCDhK6-xP2C4ececkk8zi_Wev9aeAq1H0uB_0Cq5UDKhlk_LLJ4Rg-l031JsDhm5N-5ka-PFnsIUgDgiHiRVXLKC--wXdztODLliYvm9oED5MAUtx1BnLdctOVhBl0rVU0SGJ2VAWCi2Z3-TwQy9efdlqxhqYIJm5f3JN9fZtedQzBgNMGhvx0okpOfB1G5-Z8NLCl3FnouKAB_gA6uAXoyaLS6UTcGUwwLSoU3BZWVUZVfbsInXp2LN9nMln2QoBVVGvgw3M6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇪🇸
فرناندو تورس یکی از آندرریتدترین فوتبالیست‌های تاریخه.
افتخاراتش شامل:
🏆
جام جهانی ۲۰۱۰
🇪🇺
یورو ۲۰۰۸
🇪🇺
یورو ۲۰۱۲
🇪🇺
لیگ قهرمانان اروپا ۲۰۱۲
🇪🇺
لیگ اروپا ۲۰۱۳
🇪🇺
لیگ اروپا ۲۰۱۸
🇬🇧
جام حذفی انگلیس ۲۰۱۲
خیلی‌ها دوران سخت اواخر دوران حرفه‌ای تورس رو به یاد میارن و تمام چیزهایی که به دست آورده بود رو فراموش می‌کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101919" target="_blank">📅 20:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101918">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMlTAx7RhzsapXHPY631Dy-o5J5spm8qcHEGvTB1lZ117ZOqKdnsb8qjdPKP3rya-ATepHPgwYtgkJlRYhT2cL7bw1nnytBpbwbcmIO6bm1WLjyuj705PXvnRvqsb-wQNBlb4kwOxDPG7L0RxA_W1E7nDxHwpm1ywMZKRRdMgdOsD1CllvKegSyAtKwpBqpe5hYnpTM9Oxa4BUlUdHPeBDTEUZ4kwUbpc-W4Vvwn588gCYJLPU8FWzYoQ1Ng7sPQI6JoSTwn4DXmrMEu0RxRvXtTDQhRfXs9dunuvGRVv7SbXqp20Z53umOnZ0tnBKKy9yrgbBNgMtmvRhvUNqqwWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اسکای اسپورت:
هری کین بلافاصله پس از پایان تعطیلات تابستانی خود مذاکرات را برای تمدید قرارداد با بایرن مونیخ آغاز خواهد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101918" target="_blank">📅 19:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101917">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/779a683584.mp4?token=arkvp-RlHSpeCTXrUZeXhn5UQEkMIpyxmQVuX_xJ5eazPo16BLZiQzN_y_sYEfhsRdBM_f31yw2yPMHch8AHKkVJ0hO9L8YZHugxifss-qWW8RMreLTITORNpnEWEP6njCK7LPuCK0vfGw9vaYkBBWrPJdpg8gzOWWkdpVUdOopQybTy3URrOoQliXhYrMdQ4Dmq9BOQuD36vhfw-Lsr7ZxguswboS84429FgNWVEJZnrW0h0ZH4ZWjeQzlcnMCV0oOx1EtO0P_46nqBc_XwUzS-IsK844v74yYvEEbKCq0cuqUA9SDj7glr1cHKAt0Parj_-GXDmm0ixj8KHXZGfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/779a683584.mp4?token=arkvp-RlHSpeCTXrUZeXhn5UQEkMIpyxmQVuX_xJ5eazPo16BLZiQzN_y_sYEfhsRdBM_f31yw2yPMHch8AHKkVJ0hO9L8YZHugxifss-qWW8RMreLTITORNpnEWEP6njCK7LPuCK0vfGw9vaYkBBWrPJdpg8gzOWWkdpVUdOopQybTy3URrOoQliXhYrMdQ4Dmq9BOQuD36vhfw-Lsr7ZxguswboS84429FgNWVEJZnrW0h0ZH4ZWjeQzlcnMCV0oOx1EtO0P_46nqBc_XwUzS-IsK844v74yYvEEbKCq0cuqUA9SDj7glr1cHKAt0Parj_-GXDmm0ixj8KHXZGfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
رونالدوی برزیلی سرعت یک وینگر، قدرت یک شماره ۹ و تکنیک یک بازی‌ساز رو همزمان داشت.
🇧🇷
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101917" target="_blank">📅 19:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101916">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3ffe3c02.mp4?token=Zqdt9gmk1IUrC6SFnpxiv9NSlwFo9ZRB-jyz4WtCgD5hFpfshm0gPK_GVJEtTtFjhasZDZ-2R7Y-_QvX-TkcYhuj90uN6o97Hl8e2sbQZ1sgi73dm78Lc0muOgwupLUn69aK7OsFrjotZrvjaMW1fgURCHO9mm9c_0E3dkxhFnAul8oAumD9OPwEWliZlQa6kcuvDIg4y7lbXvq_JOcba8Gd--QYKKxPtazHoAHSFTXof8fXu91IvcqKC0HxQ8X38XqQB9aehOpz_mcoLEgsz6SUv-ShRVlk3QzC-0Xa84KWYJKH-1H5EFZJ2lxeJuXbmpzXd2ys_MEvZ3JvyQkSJEs4TvDYHyuXTLGdGbBieY6mT_DbeI3im3QL2ynrdQjQGspUyglGxzBDbh8dJAc1bbw2b6z0T7plFHTO6ee0X-vug1XsZCVwAJdCZn8QhCQamCSZ9yZwfTzSCQf8HnfWJriYFFbROJBor6k7epCsXu5lPeFSzffxcX2RU1grvrHtKPFqRMNCQThOCxu3UrznXZAUeMNNtF8sswjObvaPnaq-NxCAIxy9DXkMpfmWpY0HeF2gW-mbZFmcXVjqILP9SKi8j3TU-J77XADBQig2wID0yvZ29W-Slsvj1LNYrVZBjzNaaUDCTsdx3Jg-ELN249xP0-2FNRK0IR4HuFMaw08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3ffe3c02.mp4?token=Zqdt9gmk1IUrC6SFnpxiv9NSlwFo9ZRB-jyz4WtCgD5hFpfshm0gPK_GVJEtTtFjhasZDZ-2R7Y-_QvX-TkcYhuj90uN6o97Hl8e2sbQZ1sgi73dm78Lc0muOgwupLUn69aK7OsFrjotZrvjaMW1fgURCHO9mm9c_0E3dkxhFnAul8oAumD9OPwEWliZlQa6kcuvDIg4y7lbXvq_JOcba8Gd--QYKKxPtazHoAHSFTXof8fXu91IvcqKC0HxQ8X38XqQB9aehOpz_mcoLEgsz6SUv-ShRVlk3QzC-0Xa84KWYJKH-1H5EFZJ2lxeJuXbmpzXd2ys_MEvZ3JvyQkSJEs4TvDYHyuXTLGdGbBieY6mT_DbeI3im3QL2ynrdQjQGspUyglGxzBDbh8dJAc1bbw2b6z0T7plFHTO6ee0X-vug1XsZCVwAJdCZn8QhCQamCSZ9yZwfTzSCQf8HnfWJriYFFbROJBor6k7epCsXu5lPeFSzffxcX2RU1grvrHtKPFqRMNCQThOCxu3UrznXZAUeMNNtF8sswjObvaPnaq-NxCAIxy9DXkMpfmWpY0HeF2gW-mbZFmcXVjqILP9SKi8j3TU-J77XADBQig2wID0yvZ29W-Slsvj1LNYrVZBjzNaaUDCTsdx3Jg-ELN249xP0-2FNRK0IR4HuFMaw08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یکی از مصاحبه‌های چندوقت پیش کریستیانو رونالدو که اون گفت او قصد نداره یک‌ روزی مربی بشه و بیشتر به مالکیت یک باشگاه فکر میکنه. او همچنین درباره اهمیت مراقبت از ستاره‌های جوانی مثل جود بلینگام و لامین یامال صحبت کرد و گفت باشگاه‌ها باید به رشد و آینده این بازیکنان توجه ویژه‌ای داشته باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101916" target="_blank">📅 19:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101914">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvDGt_nUAcL-2qwgJqVFu_P-UzwXvlsJSQw0-v3WorjC7nKalw5nCnkKqP49bYYAAqgDoHLF0b4Ikkr5Inq-hQXC2AexM2jgInwDGh9uCvH-YeC2m7SBjT_NhWrf8xKboAzGj-AmA0CPoQWgTUHbd10XKV3MVIFpPMiOSFhWVy4lH-Ji3DlLqw3n-spTxTua6wiQyWO5OJCe06JPvS-u-VSEN0qYwb-SWlOULvUMtdsCyuQoFdgqYn7qS6CnvV9als9Qv20ugRvl6aRnXsVYLGmOisqVXEu3LbZmx4Z1yFm-9UOqPeuvcHRzJsPOLfkM4sWfrx5Dvdg7hnPG3MUcDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9c742e9e0.mp4?token=PEtGE21RX9thk-HvNbFDNf7maLtoH57adr1bRJ-Y81jjEotOnadunKTholuqNI0S2FQGZ_wTGta_6XexROFSe9drkeTPo0bV7vUAMz_Z0ohLqv3SfaNMUwLz2oMgwg3x74Mp5MeZ8BCOFB1AQuDq9xvnIATx1jQH5H2RRrpUCYghQj6HhIuFJFmTaUTx1yBIu94zumylwm5Q3LY7Ufij4wqHCcPiFbzmNNcjPPPYD3vyZYZ8Cu_tTwzdC9b3me8LIyJDkC6v_3xpib3EYVyPueRkupUwMLPBgFz6th7dH26XaAMDsglNoys54OSHCOf6OIZXMuWCLTfqH1kqvtRr_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9c742e9e0.mp4?token=PEtGE21RX9thk-HvNbFDNf7maLtoH57adr1bRJ-Y81jjEotOnadunKTholuqNI0S2FQGZ_wTGta_6XexROFSe9drkeTPo0bV7vUAMz_Z0ohLqv3SfaNMUwLz2oMgwg3x74Mp5MeZ8BCOFB1AQuDq9xvnIATx1jQH5H2RRrpUCYghQj6HhIuFJFmTaUTx1yBIu94zumylwm5Q3LY7Ufij4wqHCcPiFbzmNNcjPPPYD3vyZYZ8Cu_tTwzdC9b3me8LIyJDkC6v_3xpib3EYVyPueRkupUwMLPBgFz6th7dH26XaAMDsglNoys54OSHCOf6OIZXMuWCLTfqH1kqvtRr_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
طبق گزارش‌ها، لائورا ایگلسیاس، دوست‌دختر رودریگو دی‌پائول، گفته او حتی ۱۰ درصد توجهی که به لیونل مسی دارد را به او نمیدهد. او مدعی شده بعد از شکست در فینال جام جهانی، دی‌پائول دیگر حتی کنار او نخوابیده و رابطه‌شان به جایی رسیده که به فکر پایان دادن به آن است. گفته می‌شود او معتقد است دیگر بازگشتی در کار نخواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101914" target="_blank">📅 19:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101913">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_YQoZAYHMaMU_cx2SvJzzY26XTEu9ssYPRlL5vpk6_8BZLVzhY3XdubrbRrDttBlZ3r7Q6V_kesO8To6jm1-h4xARFWZIJpqja3WnIgB-Rk1WTBaxaBeIY8IJeKojem7fdfBE_6gKSEmGJ9lr2N-vfUB8CetvVq4XzTB5CvMBcfKsZR5gzbTZqEswih_g4O-fph20EKhioImQsWlb0MZpWRZXtwFBmyxPonUPs6yI6DV8Wkdb9_SWIEJOtDwb3kQnMqfb75j4zkOIya5SzYDSvxESvT8TK8-uHyTR775W4DOZ8Nh6dcjfAIupvp0l5FK9TTVZ9cC03Hzrz_LczLHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
تلگراف: ژوزه مورینیو با انتقال وینیسیوس جونیور به آرسنال در این تابستون مخالفه.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101913" target="_blank">📅 18:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101911">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cp1T-vuUePcdPevXk78cbFt9YSAnlcHeKpAUcBLT6Dh4zRv0wacJ18Ehcr2xgkhDqPL_AMwWmX2wGDj7UtcEpn1eEc7XGPVdzHXhpsOl0aDZ7-jXKvUNgPmLHMD-0pOhaeQbZtFmzcXfHA62r0MsI5H0aMjzDHjyQ8X7KS_zZ8PFFsxWuUlMH5cB5qUkLFRtZF4lPXxw401sAS9N47gWtQfbISaPjdnixUiCwevazXQi53tVqXeCepk1KCVxBiEelAxpgC_Cg7RHlrfLGUjujnyiy16QHSXVzqXJp3XQbf3dAzj9wCoScpCLogvP7nuKg66_3bZI10QP8lziFhjP8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHFtaNZXBh4oUs2V3MF7i9PCFqzed2Uzd4aJjqZ_6oOYeVA75vzVQu64Xg3BE0702ck38u5ckFCvNpHD-XGCCjgcsrkYVaFGuu0b4zmjBd96qP93AODIK4AoUk6E90C8exXPHOylyY6QkeYPdR4I_wXaoLnAM-s_Ca7Y0nqBel-Ms5FSNpqqljquzqjJPG3UxJ5FmOmqBd2aQ2Yu8J5rsKdfY2Y29EDh4iWihrPZBy3A37Paws9sLKROIbW22Fb04gdQcOq7gZMFtXBbYvXRX6-6QbBaR_mMcVAv-DrJizwNC_M0OK8bI55de3ZlS6sHEyFsrlsQtpGCI3ELXdx4rQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
رامون آلوارز:
اگر انتقال رودری و دیومانده نهایی شود، رئال مادرید ۲۶ بازیکن در فهرست خود خواهد داشت. در این صورت، باشگاه مجبور خواهد شد حداقل یک بازیکن را از فهرست خود حذف کند تا با محدودیت تعداد بازیکنان مطابقت داشته باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101911" target="_blank">📅 18:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101910">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSzllW7gBzFuyrv4lu47IfLAnWYk-VLfu7i9DlmGUsMofy0G0FLSX7nbCG-cBBmsw_DQ_u7RYQPk5u814gD-sc0QcEMfO1Wz1-YUuOS_Bd5ktyd7l_TNcMPVWUpaSbbrVpoMqJyfk_YiniQcfpmLnUr7FrzIh4RlTVsOmoSt9G1EQFUrKjlC1noVb60Dj7rGKUZccA2LkJmlEdGT_XdfSDCFKqMLmtLCqvuvNxgJDhXtDxwKZgSU1GmHwF3SKtDjJPAwT3SzkkjumOyaLkVuBz3ByBbvRIzEmx_A0JcY_XzNP2VHplJfexeqTpocpW0mPQf5OoQppSsmUA_HCTLpQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ربات هوشمند تهران پی تو ۳۰ ثانیه خرید کن
😍
فروش یووچر، استارز و تلگرام پریمیوم بدون احراز هویت و ثبت نام.
تحویل فوری زیر ۳۰ ثانیه.
درگاه رسمی بانکی و مجوز فعالیت
✅
@Tehranpay_bot
@Tehranpay_bot
همین الان استارت بزن و راحت خرید کن
تلگرام استارز با ۴۰ درصد تخفیف
😍
یا داخل سایت رسمی بخر
🔽
https://tehranpay.net/utopia/</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101910" target="_blank">📅 18:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101907">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1qR7E7h-lsI8piEPu1LjPcG1yRmpb5M3b9r9CmJVnE9jmCJdAh4S48rzSXtYTa1IteX9s3RokTDxav90YZT_gbnjodlGvhISdZtrq-a_nUT9iBUEth-oWX9eIdWCF7ZwZs__khD4EYdMmh5kR189Rd6dcHgIm5nAnjIRrlG8c2XyFNSjY4GeZaOlT31Br2idYPGipBn1pyCc6hylBvKlscgQoEgwgSjh4QkGca_j-hEhw86AhsTN9syl8MBWB-hj6xbnl_tw1L1wzmprMianQG5tWEXXjuaySakmGwSs-HiNqVutNVtNqw_wXN4AttFIk3VyrGhnnVPF5JsqgOAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kglC7GlCXY9_GX-KPEJ311iW2Zu8fKr6uEGBM3JniCKjk8Im92H_tP8zWqZXzFVCPKiq-AF-Xuy9FNCJk6tE0urJrbz12SR1YVilZiY776aoAkKPAtrSKWkzGeOnyncHRSV9gpkXmqePXlza0jJTCSzxNnty64e7gHkIaRmAdgkVh-t_EutoSyJJuP3xVcxX8nBhnRSoPGs_OAXQZLuGnAMH32xsNOWKKMngVRJYcZD7YteGGTj8PObVCjjnn9PTcP20SmlBTwdmamDm_ymnCF5HLKB4DlxOu7b1M3o4ufos698me4Uta6rTi6eXz8MdmxbexXAy1HXROhwwvI5nxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d05827d11.mp4?token=W35H7iWd8hoCCDkNp2OG-zKPXgYZBRtSq4ctNiEmtlntdZhY440NgGYsUTwn1ycozWejsK7zizhj3CbK8BFZA80NGBMqb2C4O5AtNLcxGzBfKwDesXrnckzc_jajh6atH4caAbJXgzL17BVV9Q_6ms4C7P9Kj4KGYqpu6Q09LCSzxKdMVZUoo_iUqhZomlMybK5l7zDmUSqaD12KP8nQN_aPae1OAiyEc7yFTTLE-IYPZVXds4qvuGixPEJ5Gn8ybnzXuyYLnbIDNvZHQc2L3Dyn-G5W6CzfHRQoVcl0ov_gGHod3pze2qhKN68YAGbCJwty4EcbzdYrYfc4K9ZjSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d05827d11.mp4?token=W35H7iWd8hoCCDkNp2OG-zKPXgYZBRtSq4ctNiEmtlntdZhY440NgGYsUTwn1ycozWejsK7zizhj3CbK8BFZA80NGBMqb2C4O5AtNLcxGzBfKwDesXrnckzc_jajh6atH4caAbJXgzL17BVV9Q_6ms4C7P9Kj4KGYqpu6Q09LCSzxKdMVZUoo_iUqhZomlMybK5l7zDmUSqaD12KP8nQN_aPae1OAiyEc7yFTTLE-IYPZVXds4qvuGixPEJ5Gn8ybnzXuyYLnbIDNvZHQc2L3Dyn-G5W6CzfHRQoVcl0ov_gGHod3pze2qhKN68YAGbCJwty4EcbzdYrYfc4K9ZjSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
رودری درباره جنجال‌های جوایز فردی‌اش:
فهمیدم مهم نیست چه چیزی به دست بیارم، همیشه یه عده هستن که میگن بازیکن دیگه‌ای شایسته‌تر بوده. وقتی توپ طلا رو بردم گفتن وینیسیوس باید می‌برد، حالا که توپ طلای جام جهانی رو گرفتم میگن باید به مسی می‌رسید. این بخشی از فوتباله. به نظرات مردم احترام میذارم؛ مسی و وینیسیوس بازیکنان بزرگی هستن و مقایسه شدن با اون‌ها خودش افتخاره. اما بابت جوایزی که با سال‌ها تلاش، فداکاری و ثبات به دست آوردم عذرخواهی نمیکنم. هیچ‌کس نمیتونه ارزش زحماتی که کشیدم رو زیر سوال ببره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101907" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101906">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbd3d9241.mp4?token=DuWUNPvpMhgjPvXZd5U-WQl--QEujzo3MWWPEPMkfdSA4dy7Kt0SdaGkbvPuyMwDMMTVAddx4TUlIE2v2J0_wRFZh5pMayWA2KTC3ib014xRFOK7du1qNDS8HvhNOKF-WHNoQRVE4ItEvGAGQVPejwruLslSEjTt6PMwe7fHk5hcQkejECJrMymOVdgOPTIFw6va3FSM17-J_WbB-Lk_J2wFTZBp--ZDAcn8T707RdjN6pd69nGMp_hPCSELhkEdoq3vnqUG6tvJkIYXN0rjPB_It7MHmlP2a-SWgrBp-I9IkayZZog8JdEmfEYr1h1qNdcgBMouTcTwX96KmAQcWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbd3d9241.mp4?token=DuWUNPvpMhgjPvXZd5U-WQl--QEujzo3MWWPEPMkfdSA4dy7Kt0SdaGkbvPuyMwDMMTVAddx4TUlIE2v2J0_wRFZh5pMayWA2KTC3ib014xRFOK7du1qNDS8HvhNOKF-WHNoQRVE4ItEvGAGQVPejwruLslSEjTt6PMwe7fHk5hcQkejECJrMymOVdgOPTIFw6va3FSM17-J_WbB-Lk_J2wFTZBp--ZDAcn8T707RdjN6pd69nGMp_hPCSELhkEdoq3vnqUG6tvJkIYXN0rjPB_It7MHmlP2a-SWgrBp-I9IkayZZog8JdEmfEYr1h1qNdcgBMouTcTwX96KmAQcWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
حالا که اینقدر امروز دربارش صحبت شده یه کم یان دیومانده ببینیم.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101906" target="_blank">📅 18:31 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
