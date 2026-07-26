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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 00:54:15</div>
<hr>

<div class="tg-post" id="msg-102034">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1wfxSpDixJNz0fbYTrnmQjgqieMonMXvEG18_i_Gwrtd0el2SGREgA8r3kj3LxnDhB4WIANch1vTSisVs1i8V3e5FLcxBJV4f5Q1oNH2NgvG0XCbEjUvLBMMYU1eCvSM12yYpK243vyGbX_Tc57_zLYBjCJw5sd5fVPgS1Bj_Dx1NR8U-XXqd_g1-k2gzWL4ZNG1T0lNEKnnqRX5i24YlDefhy502c3oT_sSgngM-8GAooSSAm01U_geD5X9xY3L8tNvLplg9dmXd7-iPIpKZEcalApo15x32rluUWYWOH_VALh-aSr-wH-rF53IavoJyIKP2FS7g5VY5OBenCCPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تلگراف:
مدیرای آرسنال معتقدن وینیسیوس جونیور همون بازیکنیه که میتونن باهاش چمپیونزلیگ بگیرن و هرچی واسش خرج کنن ارزش داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/Futball180TV/102034" target="_blank">📅 00:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102033">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/Futball180TV/102033" target="_blank">📅 23:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102032">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0SzL98f-p1xRc9J3ivfPtYtQiv53Depu0QX44KBvUb3UcsQUoN_M6s3LqXmssimPK7Mtou9mjDza-LHUHAHEEBHughAvZY0uVWeB1xiaem-wspzuJ3YmsO9W4Gkb_tIO2iYSu9zxvOLFZQ0WkG2ZO4zbhbNy20XvS6QIcX_L_MIq0rqzu5nf8bjNLO6CNvDBuI-6CwFdywjKk5__i5rTaS55dakYgI5s8rSsd82-f9jKY6NwPqp0BU2BR7uuU6AUQmGEyDpopvhNNnpFfzPDgHPnDcEte6yT_4oFHCohSvzcvb1Z6X7Hz4JMXRe5EPoqk-h6coyIOJroCuLKJyX3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📮
🇮🇹
دیس فلوریان پلتنبرگ به رومانو: بعضیا همیشه میخوان اول باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/Futball180TV/102032" target="_blank">📅 23:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102031">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUxIlRX8zuSMpcS1Ajlm6MLt3Q9Pl4QgU30JfZBLev4xpHQzTZWdcMg1x429Si6trJTywi_u-gybyO2kgICr6fexMdYVHQItv8JaXJgRp8smcKy1Y1sLj4UA1Uydvr3jMyaQ7_zhT6iXMhx6o_EMttg6Ujug_VH3kKtPqSZso5Zml1ocN965qQ1gIaHEG-tI1JLCHuR94V1ZAsVT9JNCS_QCiGDGaotTW9zYDFgidFhqx0ZhL3UmMwS6sGNniJTeWLYUzbSf0gTJA_5y9Gx3JNd0glPZK8d-3DXNO9VeYbrwQEquO3HcP8MnoA2hlQsucadjuRC3c5vEqICi70xGsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
فلوریان پلتنبرگ اصرار داره که هنوز هیچ توافقی (حتی توافقی اولیه) بین لایپزیگ و رئال مادرید حاصل نشده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/102031" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102030">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/102030" target="_blank">📅 23:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102029">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/102029" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102028">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/102028" target="_blank">📅 22:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102027">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xt_XajTURcDUD5hbNel_ZBCYMlP-EwDCo5PRi3h1LGZ3GtIUQs76eHvaHOFfqim5DExA8NidvudbtcgSK-2r5Uz2Ys3i1XAjihA-4vdunSOZm-WtM5bO8ItpMabUim870jPYACMWDzOa441nMN7vs4fNUdSTiwaQDQsSAC1r5Wgwd0rON_CQktnqL3ntYR5zh96Go0Cx_bze5cpU9DufD33szDjIL74Bkr631d2hY2wYZXooIKcmdBz8r-jIjw8QH5k7g3wNcBKR8eqKJFXfAzWJdIR0NzjRfYYtR8ZFOcknfPansDoEAa3i6t9WPBvwinwPs6riNn05RKyNspTtHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار پرز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/102027" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102026">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/102026" target="_blank">📅 22:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102025">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tofSIsTrqfLcoSC9EJsV_ErDB-Niej7QCFYN197iX-b_UDhbQ_0GaEyHTfGdXmspPhuqfBVSjzXtOAcpQ3tvSgxsHV_9gmSxH4KMbEgc45Y0ORLL961rswsPb7rabGOBhU7Au8O6xiqAo2pJi42ohX8x1JHQToJwuvS0aZVooVZ1kAiQf5Ntd5bkvjXj5xC8f0Y1yZckWu-aeQTkWhTZapCe1m0a68k1kqJXRp3Gfa1RbYWQ9U3_hzaMXVz3_ePiWb7XERiMgI7NP4uEkWv0JCJd7cihRb8QIDKjB0V-DAUCcKF4-_MS0iT0aBt8DDmbp2MyTxJ3jnnXbz8k65_3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
اسپورت: خولیان الوارز گفته میخواد یه قدم دیگه برای پیوستن به بارسا برداره و بزودی انجامش میده . نهایت تا ۱۰ روز اینده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/102025" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102024">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102024" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102023">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102022">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_ita4ixEJYZOJq6yoLCs--evlJZ_dMw23E7cT2kcRVbaeC5U2EtQHUlmSIOkE57bbkwvdBn8wtEaOdkuO2C88fSJHN4AsqTQq2MElKTinqm3R5-AQyWXiwH0eEc-D7DkiX8444cB-0qBTW-PVkxE7w43-FOjgE3RNa33oxn0lAgeBib_FWyRvqp7KgFAtrqiE7VIBCNUUUJqYvTmEe0RG6jPH1kiPGr4JM0c2sDZechUq6IZ9locLS8T_TQ4TlMKQJzXAcbyJ2V0_6cEcXCVfQf5ButoCwHRXB44SGisQqvcHOJvFt2igOvtT55pRdZj4iOXaWdzEnDgn8ueVSAnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚪️
عمق اسکواد رئال مادرید برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102022" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102021">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102021" target="_blank">📅 21:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102020">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZD3ijjJ1aTS24mY_Rygmr4WOXMKvks_TS8LiZB1HPwvMrUGGCAIRcE4dK_LydXoB9vqP9JYK0PHYDsBU-FuYI_DVyy06rQVHvkq4EQmeru2oNqjH_jm9fdWfVVKqiFMgGmiQxT7NW0HDrCBwDd7CuoK1jCHGup2wMGjpWlSMuyryOLj4WzhKrybr3oWdz-jXRD4oqH5MWvgizyh5v4JSg58CbLXZRpb-6j6tZj5ZA4wjMRrNKzuU5YLbTWedS9NUeUOtY543W6Dw5YDJrztmpnnEigaO9wFMGUOPhQEM4WRjA-eBFaqq59CTX_r0apZlS5GEPdqwq4Der2bocmcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🚨
پژمان جمشیدی که به تجاوز متهم شده بود، در رای نهایی دادگاه از این اتهام تبرئه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102020" target="_blank">📅 20:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102019">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPw1aOMjox-UMnzZshTqh9WMW_7YcLHigq86U-jGYCeJuwmqGBzEhcB8DmhQhMQJAlOZOyRAJSDg7y-6N-zHA5fwa8hm8UVHZTsPljXGilaqkkDPCdXgAovtxUeu1Br3ZqXJqF35bVBG7OZqp7CFvVIw62JuwkvQPF9MYK9zTEQjNDvFguJ1jtVNkvbNAXu2pUrSQfB37nEaUET-TL9BDGRJeYZNsT9kfV9P3pjeseHQD4Uny-MTEcBGFKrlx5tdbWtGNl4P9CDnzNpym1mKUDLuZT9v2YcZALJV0xX1Il3cSgYidJ0PmmbDSrQO5lncA7f4ZtH32PAvVGTCFF4r1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
آرانچا رودریگز: انتظار میرود که یان دیوماندی این هفته به تمرینات رئال مادرید بپیوندد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102019" target="_blank">📅 20:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102018">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102018" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102016">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102016" target="_blank">📅 19:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102015">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102015" target="_blank">📅 19:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102014">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102014" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102013">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=p2E521Q6bfDkh8ypl__vUmRRuKTmWEMPkt3ocBe9Yd9XPnzmkoUhSDwZgrd6GB2tyUSLWelMJZOqa-UKk2zAxqDuY1P61_YQAdTHDFVXpn-NY5GMDWH_6Uc1HiXDMR6NFxejrScEK5UKBGXDqkrSzPduONfS5t2NeUCR7qBcKuoT6RJ1YxiPQgCP6xJzdF8JIyFf6ap2krprvByL8th53QunbVBuFRzr-M46il-FIYhYBuhNqo_-OgwO0h5eFgBC2w-Z2S76EgqBru9a5fhIHLBEAg6Yuyrh-dBnd5xReUIY0R4BzJswD538jqmuyhye_8cWQJCcf5VgPelBAaNPAVtb4iE2nBpKm5jVNye_8DkS00RhyWREM_NrhSMi8hh-Tg6IWx27BcFZSyg5fc6nkK7y8HDuF3xgiS_emn-MIG08eAn0Mk1EASNKYcEgD8RQWtDBbtaqsSRBVX6Oh_efL7mIIRZ-NMKlflzwPuA4-TZ7LBIo0b4EzP_EigRrFpMaJuU9OrC2q05LXeyelR3C9zUhGe8ndce-9HTNVLv4d8jIumqiPbvF6MxE5QCPsJxqnCbDsDB1mPu_XQO5V7CZ3LL_tvSLL4e7TYuhIEzxP8fNMk58TJXx80sLG89xWFrD93oBwnDZpwnhYy9OwKCsMb3IGQBL5nX6IKtqZAAhLmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=p2E521Q6bfDkh8ypl__vUmRRuKTmWEMPkt3ocBe9Yd9XPnzmkoUhSDwZgrd6GB2tyUSLWelMJZOqa-UKk2zAxqDuY1P61_YQAdTHDFVXpn-NY5GMDWH_6Uc1HiXDMR6NFxejrScEK5UKBGXDqkrSzPduONfS5t2NeUCR7qBcKuoT6RJ1YxiPQgCP6xJzdF8JIyFf6ap2krprvByL8th53QunbVBuFRzr-M46il-FIYhYBuhNqo_-OgwO0h5eFgBC2w-Z2S76EgqBru9a5fhIHLBEAg6Yuyrh-dBnd5xReUIY0R4BzJswD538jqmuyhye_8cWQJCcf5VgPelBAaNPAVtb4iE2nBpKm5jVNye_8DkS00RhyWREM_NrhSMi8hh-Tg6IWx27BcFZSyg5fc6nkK7y8HDuF3xgiS_emn-MIG08eAn0Mk1EASNKYcEgD8RQWtDBbtaqsSRBVX6Oh_efL7mIIRZ-NMKlflzwPuA4-TZ7LBIo0b4EzP_EigRrFpMaJuU9OrC2q05LXeyelR3C9zUhGe8ndce-9HTNVLv4d8jIumqiPbvF6MxE5QCPsJxqnCbDsDB1mPu_XQO5V7CZ3LL_tvSLL4e7TYuhIEzxP8fNMk58TJXx80sLG89xWFrD93oBwnDZpwnhYy9OwKCsMb3IGQBL5nX6IKtqZAAhLmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/102013" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102012">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102012" target="_blank">📅 19:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102011">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCUjXKE_6QSCWDkO5tZ_u1_scJEimc7zdcjulMuLpXlFqhUvxaxyoNiJfFCZob7uJg7qK4LGYIBCAVmpSa3GwpuHnwhzBVCdnHFVYv6F_A5_uiN5ZOG8VrCscwq-QEX330_UiBPKJanuO8AobDNUlSIkVvPDdxakwGYKBRKzIH4rCvL-4KlFvGDxBhpylUJusIfiXacSjiQuskwOmxJExlZmZI_z3bp1iSTpfU6ZMt0WZ6lRYU4KBWXNMKPmn-eQHaYSR-q7u3AUnDAA-akMQfL1ThJyjGMAJbEfqx44FpWYLecCIRXYD8E9rDg1alqiZFN10zrI-U-Xa6t5F1rgog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102011" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102010">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102010" target="_blank">📅 19:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102009">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIJgcZvLa0gMwKEiZAkvr1tMRnw1Ltcr_u4hwmDGtYL65hCHatdAshi1vS5X4ttHwW4I7nkuPZ2wMR6VDipfn3x-S4F-Ynv3Sp4O3WJbHCclm_7_VFXuCa8AQENUmSOSHqH8IILfBh5bGveaa1E6ItjE1iNhRQo-9M-9k-fKjsqEC7qO0UlPEKn1gihBHdOq7X91s-LJ77QEw68WvWfdjTui3aZw3XVMcz0YIdoIgDC7bKddCXUX_OAxvGoOBdNLlupsQD2Ervj9FScK4eBO2UDJZJId9lxTB1xndfXX5sOvS0gr0L0QGFKbMn-HGV_YDcEu1F83iZPXCTaMvRhCyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
اشرف بن عیاد:
کار تمامه، مدیرای بارسا متوجه شدن که موضع اتلتیکو برای فروش آلوارز تغییر نمیکنه و نمیفروشنش، حالا بارسا منتظر واکنش آلوارزه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102009" target="_blank">📅 18:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102007">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZY2DMqis11xS3DKmeVF67eeAO8YO0jaYLXa2MdWVaGfL0bF10-KOV2zFWnKBlKZ4CzWCLWyMSR9ex2uU2jh8_7n1gibvkzqNBo5wc0cwmLwiPuTduPeaX2MmM-y-F5Eecv32RvZV_TJpVf4dIECdEgiw3dZGg2_H3hYh8eHq7XS58pHUcv2WhN4krxIi51RuM73TUe-fI8olG10VypwrmIlbX3xQHT0Ls8GRFMeL83XGQI6LuTzP-FeT5JE4JnhNObmUj22X2H45h67dI-unhuc5fKvTE8nDKNVCTnb_Z3pXpeTbhK4awVJMnvqhqoyXwUGeAqca86u8abDcSKx1fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmLDLWxdx3JUdOAHxkMkVAzYi699Q-Gsvi2-FAIaL9Bmc5dsNj5-RlSG5Rim8cAO5kKO4UzOQ-EcgW3auMuuW8O_P76f8QyFyU18u7CXdeyqOQHiciCtlrNpw5kip88Fnc0_Sa9vxwryd2pmluw146fLZDIcVVDrbBUa_eKa76nSi6ZkuB2QOowfIc0x3mQPJm5pF6QP54FOWejghV1loT5ll2CPhG7e7nmtkNCLaySSjD2tiodMhCdZNnmNxyOi10s4LHGg-zmL-rxFH8R3_ql-nf_mR3G7tVTpVFMwAZYQHLLy0spljlKl0hSlAcr6HGJhC9WggLBUwvKQGPBCGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102007" target="_blank">📅 18:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102006">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=Jo6T3pe_RQQjMtQ7JzYwwhHuJH6cpbJd97DHtsrXu8q6ADjkdI6sZLrFDyZv9CnKsXCDyKosXrYDjqSM1s4wYgcpIuu2iVi37pRbR58638_OhRMT-sQZiSTZ6fCZ597iNQs6xmaaO3A7e2vfXsrXDy8P1p_NFkXOOEPMXvLvrAykiN8vVbT4L5dxm2kZQTNDv8n9At6oEwD9ZKEV-Wqj2WCTUMs0dT_ApYG1I3ZO1yFHa6nXjQ3HCrqzUtyyxiFUGWyT1gHqWHfuHvSrqr4VEEncpOV0K4hlOncdvTjMarlxjhozjEoiW8YYUhU5LLw6tOoviFdielOJSgNjF_Ha2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=Jo6T3pe_RQQjMtQ7JzYwwhHuJH6cpbJd97DHtsrXu8q6ADjkdI6sZLrFDyZv9CnKsXCDyKosXrYDjqSM1s4wYgcpIuu2iVi37pRbR58638_OhRMT-sQZiSTZ6fCZ597iNQs6xmaaO3A7e2vfXsrXDy8P1p_NFkXOOEPMXvLvrAykiN8vVbT4L5dxm2kZQTNDv8n9At6oEwD9ZKEV-Wqj2WCTUMs0dT_ApYG1I3ZO1yFHa6nXjQ3HCrqzUtyyxiFUGWyT1gHqWHfuHvSrqr4VEEncpOV0K4hlOncdvTjMarlxjhozjEoiW8YYUhU5LLw6tOoviFdielOJSgNjF_Ha2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خشونت بی‌سابقه در لیگ‌فوتسال بانوان برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102006" target="_blank">📅 18:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102005">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102005" target="_blank">📅 17:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102004">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iw6A3W5ftWWNPz0w47eaJqUR05u71KxD8-FJSyOcxOzK-K_uq-aEtica3m_vclMXzJ7USRv5cS-71n27pWdAACFajSDh_8FIHgt0r655zFjZhs1iAlb_NBHKffFfzIE19Zc7N3Smk05vVQ-bszcQSs3qOGf3OcMt3U9NbTSZGHN-epDpYMFJiE0tPU082ygwkGnhdZq7DPIn5eHV431GljCc3AlilyU9cj0MaBJFOfCTx-fjA90z0U_1wHr4jjlU9Jn8NyhkYtvgBUNe105X-Oax273MEC-zWOU94x7j126PYvxKXk7UGwF68KJn_LCkuewcyk9GD7SYLmn2aPmNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
فولام قصد دارد یک پیشنهاد بزرگ به رئال مادرید برای جذب گونزالو گارسیا ارائه دهد. آربلوا می‌خواهد او را به تیم خود بیاورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102004" target="_blank">📅 17:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102003">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmNT9Hn7o_yCZrqnFxvXqhteA92zCHf5r13mndhaBkC_y-xqbuuKVbkrVWSzd4K-ivt2Tl9IvqjxNXJbmpX4C14yrQdxPley-9hp7xZ0Ps0BUy-XkP0Y-gqdguuhtyHSX5vq1LvG4cX13x3pDBcfXnBZGZZ4YGQ-cmP5P4gjmJ1SuF6Le45XUeX2QZXgCfjmj6qYZobw5G3YND4XUFaWONHoWGXeH1cylAiUQCH4uWYJhXZo6kCnzZ9hdFNBiYNm7i1GfQhPtgVxFC5YYQaGASF0ozNwr9ttCj0m6qsRvpApFKBYsk_GzXeptE1uJn7RLMNXXgv_WVdxnYD4jo_WYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی اونا:
باشگاه الریان قطر پیشنهاد خود برای جذب جیدون سانچو ارائه کرد
باشگاه قطری در تلاش است تا وینگر انگلیسی را متقاعد کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102003" target="_blank">📅 17:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102001">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🏅
فوری؛ لینک پخش زنده بازی پرسپولیس و پیرامیدز مصر گذاشته شد
💬
@squadify_ir</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102001" target="_blank">📅 17:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102000">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102000" target="_blank">📅 17:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101999">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101999" target="_blank">📅 16:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101998">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101998" target="_blank">📅 16:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101997">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101997" target="_blank">📅 16:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101996">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101996" target="_blank">📅 15:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101995">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101995" target="_blank">📅 15:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101994">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🔴
فوری از رومانو: لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101994" target="_blank">📅 15:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101993">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZnE2pk8xWfK8kaX1EUhJxXjaFdzzCvaXZhWlo7UrULxUEoPd3XMxlMYXw7DPjqH0yryv1HPIsJY8DTbzJ4eH4VLz8tSZVjIbcFFswFIEW5ngY_44KuS45pz9qkPCPjfiU-V292VaxQL_qqT5yP7WnjONzyJWtqlaH0o_Emtf5Hk-wXGYj__oTVbdq3ufOzBm8r_mFsOvEtSvgsexVmoRFEBi2EW-f-NNIzQqRSwRkV751EQsDG_cZK9aIWD2sY-jI_BQNmxzqxmmEMmV4qoFnRK_Mo8IOiLS-TaHV9-BnqlGWa2PmShTBULP-ruFNiGkBE-dSesgKnLQ3I6k7jLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فوری از رومانو:
لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101993" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101992">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101992" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101991">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101991" target="_blank">📅 14:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101989">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmD6Qk8V2gG-pD0ClVilVwV04PY7XZ7wE1iV5aOOckLY_MPwOa3tvyNbYYGlGZrHkHaPiJ7Bn8PF3w2bcKYyaf-zdYMd03mANFJStqY2Di_kmvBSV34H46274NXbPSq3-twu4c5vdGHF-8geU3dyyNNdJrLInKup05srcL8T3jGdTRHZUqjy2_ip94u_EnzdjmRtdBA86ydOe35B56STmwZQJdFPJBPJpPOAjYba8oVJkOiEtkUBFV6vrL8Tgn2y4FsMSVLSqO77P_b0iSg4Kz7G3s73nidvA2hjbFY_FmOzwMv9vobgN_OsVjjFNGNzp12s4UDb5cYYUn1YPyHYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGA_jezv4vipmckUzCKPoZPRMIlaggerESym9tsewcirkp-pxL4-YIkkcD2aFl2vNDFniF_owAa9IjRMXSr6NTQlDc5T2tXc7-9tDTcn6cmoy3QRnWBUmsVJ1fKnCjUsm7xUIY5rBboN6UFhoLrRT5FUD3QjnGb7rvBRHwU2zg5A6_njwO0vWdX7QQ-ut9-TMMKGNOmWvIW5hyRXF_pxRpmNz6PWaV5k-j94i382AKiHq4N8Le9JdHPe728ZC4MgGISEMSJKYlN46-nxXTy_oka208JhUzitHbGoiJAJY1nukIcEAOn1h6j8SMWp7ne8-KUdW61kfc2wixO_VfpUBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اینس گارسیا، دوست‌دختر جدید لامین یامال به این موضوع که گفته میشد باعث جدایی او و نیکی نیکول شده، واکنش نشون داد:
من به کسی آسیب نمیزنم، چیزی رو از دست کسی نگرفته‌ام؛ فقط دارم زندگی خودمو میکنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101989" target="_blank">📅 14:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101988">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101988" target="_blank">📅 14:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101986">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101986" target="_blank">📅 13:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101984">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjzplorUJdOOeL3o-seugnWW1WsTP83233W5YuDO2P43MSRE_n1r_r-0tAou42RE2m0KRLtX4N1HPeGF-vMls6RBP_qETS_nrpJ0lTqbtTdQOlEjYNE086Gbsfs5zzmd_ylaG3MqPIvSR9hXC6xoD7XDf9a4d6QgvRYNb5vqIENEJV3BQzg9gx2QoO5GyoeRgr2CXyToIWy5kWZqG5wFyyiVgCv_qrEUbrBwFQdPPhLqBJRFgfl0eZ6YLhybA5PM8hh2eR0D1a6VnDTRcyPKqkta7wniK1zx-dhqIyzSKZmtWrs3xN8daN_YARHyq7JQYk5M4eTNnKKfjBZTkgGFGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QEo4Q1luxdVPcb1LBbhh2AJPmDr5DYt_M_kGELCvhnff8dKPlPXA42bXw31WRwT175gGLBiGEyXYzVvU1ymW7V5RdHPrum32Va6B5RrKZa-j_65vntPhPL3lfC8w-XN3RUd7hX0vNJ8uhsLRaUzx2q5WzS1DgR6I-JoKPwoHgqNa-DnN_3bRPJO2uqHvrKP2uYt6MVtddCiIj7NONfgA44gWjAXV7ZDS1LwGpWP7V6KC7zKm_eNqzd469bP4lWtJyvI8tnZVg8a0XizHcdKCkwBwBiWGm_0sGLTrwXcufAaui85ok62CKAHimfdpYQ5LpbqCrGbGy1TN9ioDYo9TPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
جسیکا توگا دوست‌دختر سابق وینیسیوس جونیور:
این فوتبالیست‌های سیاه‌پوست فقط از نژادپرستی شکایت میکنن ولی همیشه با زنان سفیدپوست و بلوند وارد رابطه میشن. اونا هیچ‌وقت با یک زن سیاه‌پوست وارد رابطه نمیشن یا چنین رابطه‌ای رو علنی نمیکنن دلیلش چیه؟ جوابش واضح و مشخصه! خواهشا این سیاه‌پوستا فاز آدمای اخلاق‌مدار رو برندارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101984" target="_blank">📅 13:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101983">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101983" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101982">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgAGmWD0E5qLy7cmqgUfVKo3ukMbsBO1PWvpyI-0xTSQSPqho_J2GGdJ1DAvFTXUGGVurpFrpMbyHFsbR922xugLrZH1Q9U7EdOIsPaKtEFSw9BluxOl2TCnhIRR4NQ7mn4s0I9LAB-tlWxix1ZJ7qNcGw5VBOG3KU9PZX4_sOPLcJl3Lvolvd5o7Df2GXsNLxh35XmLBJIX_vaHBX9_bUuCVdwpPKs4Zw98WxSahd0V8gvTp0e0GNtp3uvJFweLYHrP3P5ZIti1oReliKRfnSUwJMF6cnZjCyTTQ-_-ZcDvHP9zkU4hWPS5rz4-P9cbeZ914xEvSIObipNkagBQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101982" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101980">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101980" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101978">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iWdVSJPqE0zOVoKbsOgrpYeB-ceXhHFbFAr6gk-Y4E8-DrhfTIS1hKXvopq_76Zxvv1K7awC0fsEIXdjnh-c0dCgERFll7nGRdA0gbRjO2b7Me2lz2X46SxeDYs2CEPAiIoW_SPnM5_nSE-NdHoAu_NJj8OOyCUSkGyJ6Pre0zS0Flyl2LM_aNqWAuEaiRiVx20UJI_s_Lbgb92joOSuM_6k69v6Cn2joXIUPMTu0ANonOya6DrHwZjdApGFrzeE0DjtVTTnU1ieTk0oV8NEcFQ3bvvLbQQGaz61V2XNPIyXG_Ux5-Ai91D3EuX9QK_FKWagHzUheXwCc3ykfYANqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQgCDL9ANL0rWnjkQVE4vfe6_t32VQVq8nJEmdPzd0FMwHSEFxO4GWL37xVzW9Ctrraulm70RfhPfol7yeF_AnGFLQMe7xd44HSmCWys4Ax2nUfgVp0BoLHeThuinNPKk3SWJ6xAiCQD9psNFu3c0CREu2UWsZjg8fNIQIxUvJsRPPE2o_6xEBqpKaY_T3qOVhQtoEu6nJvpuZ82KRhr0cSPRtL8C7IG7lOVwPjGEj1veOPfgowfDlYgeOvH7dPqgRW0PemuPAdnA8Q47Eoq7CnPrqDG_E8d3-p7zcn8byAFhQKDPIWiU2Vtu-ZPUq-crzPCf8iLOrI78e_KJ4UHpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
الساندرو نستا درباره غیبت ایتالیا در سه جام جهانی متوالی:
باورنکردنیه! پسرم تقریبا ۱۸ سالشه و هیچ‌وقت ندیده ایتالیا توی جام جهانی بازی کنه. وقتی بهش میگم ما واقعا جام جهانی رو بردیم، تقریبا باورش نمیشه. میگه: واقعا؟ برای نسل بچه‌های امروز، دیدن ایتالیا در جام جهانی انگار داستانی از یک دوران خیلی دور و گذشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101978" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101977">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJ2Tpu1mSUo6lUGoRt4zOU4RLbRPzTgRD_kmDYoRMJMtCziXUfihPJUm1mTe-XdnzQVnlBlq6UO--QzosV69Zyd3rFQth5AX_pLisyKqQGHckHNFOlJXh5pY7l1goE978bow6FPLWK2F-2dd1lBsQEKQRniAtpnDqwzPlCD57LCqBB4MMvEzKUFGTbVc_wmfo5MLs8OstIBh2BaNuymKtGWzCDGJ-1YV8c4oHEgWFiSZ-jBPi_npHLE0P0yF2c9Fsurps6b3ZOtageK5h5YkucoXdscrmfUKVe_oEhUZ7HGMKYZ6lnjzMZtyugeW3LA35whjH9Ssgp1stfHdCVO09Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
ترکیب آرسنال اگه همه شایعات نقل و انتقالاتی به واقعیت تبدیل بشن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101977" target="_blank">📅 12:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101976">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKgkDaKvEYeRHrCTmvFXpUUakjUge5VkcxevSTvVoZmvYJTgCb9Bu7Hs2XpN3UKldu5TTYfHRuhM4bjpmVl4hZ_zwpHKmGMm6JHNw8pjmb60iMdQU2WrNkFFgvOuNFHNLmlUceuPxiiOJ6S8bc-8yNDqCGbS_qD51uFRvRPWRLIEIJkVv_qFSw9JbksFDCg5jIgz8h6viISWVgoW-vkt8rz1kbBidI1vY3VE1SAWXwPMaoStR9NnI6yOz68ulG8xTQbJT4s-Q4kQ0UJXHg9G49HVLEGQdK2R6WI4vs92pMaR4smSpwsnqk1Rn0c-fAki2m0M8AQf_g6S8WlxsGKp7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
طبق گزارش‌ها، بدهی‌های النصر عربستان به حدود ۱ میلیارد دلار نزدیک شده و همین موضوع توانایی این باشگاه برای جذب بازیکنان جدید را محدود کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101976" target="_blank">📅 12:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101975">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=azU9Lw71GN4CI_3821xp9urr-Ct-7vllcK_Loqz2ZbetDajdd1ZSI1ieKDP7yzOg4ENTv8ygjlThFZyDDgu482tvaxvIH7VPDj0MAXk7bzuMbpY8jg0x8Mk_jH01Jy-6kaPO18tmfug_6nQlSTDSzXOXuqEi83CSob_hyNYh82EZv_znD7TVpGqAhgAK5_qVuO73lFmeraBwYn1MZF_soejB-_-_ACja_tH8h3VHneO4O8v3zFOJCW7HqPsfKYoRQ-Yo6RQo7HU1w4IrUNNvo2zQ6lDtLfT144BNkFbAgZPMDj4seWS_36h9UKJY3h-9HCNiyps-oiK00Low3G1F6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=azU9Lw71GN4CI_3821xp9urr-Ct-7vllcK_Loqz2ZbetDajdd1ZSI1ieKDP7yzOg4ENTv8ygjlThFZyDDgu482tvaxvIH7VPDj0MAXk7bzuMbpY8jg0x8Mk_jH01Jy-6kaPO18tmfug_6nQlSTDSzXOXuqEi83CSob_hyNYh82EZv_znD7TVpGqAhgAK5_qVuO73lFmeraBwYn1MZF_soejB-_-_ACja_tH8h3VHneO4O8v3zFOJCW7HqPsfKYoRQ-Yo6RQo7HU1w4IrUNNvo2zQ6lDtLfT144BNkFbAgZPMDj4seWS_36h9UKJY3h-9HCNiyps-oiK00Low3G1F6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خارکسده جزیره برا ایرانه
✔️
خارک و سه‌جزیره برا ایرانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101975" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101974">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2mV_9QhXFdwEIgJfAzZioqbZuKQnR7Toukn0PHXzEEtc2HivFbLh8acj7BMYkpfWMf9Ttuv1tLUxIKGlnw2EmXlP3jEXs8AE27gouimJ-rC0b5v-W3HScL4NGSRumcrG4YVvolKG2YOZ_xNhadMwXCSBHjbki6cC-Ly2rSh7cUUPusLA0HMLNZa5U-QJC86Ui092hAgbCBz7OA5_3jnhKi4UF-C7iTwYLoII7CgJiUXtMvjwkZIOCBT8hNz5Fcbf8nDOt7f38uJPAmtI8cjUv2FHyirlIUsve8LkAhfKkMShJSVZqDIxfsGREFvqfr7vpXcf47QqeJluDPXEZGj-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انزو و خانواده تو تعطیلات
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101974" target="_blank">📅 11:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101973">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5mFhazAFIoAaRIKDZmpZO7Dx67wfOHZuzSBsjRik35SukiUiaQPdReb5qattFc1QrCdtLj6XGJAzdfWwEpql08VGmd4jRVo4vVjCUnHuEgltEvaRLRRjOlDfqYNHar3_GQcgwujOsMzdNJm918wpQRvAxTbvDYnZczwOFOE5oN35o22s_dqqsXAb1fIGr0ruhjOiyGahrBwti8tYz27kURk-K_5C7QQFK8q8ojtTpd8C4B_zbJJrlIYdxCtQLMluf68_sLnYaK7Abhbv3IXt2qZtLhuRzS1pq-5ww25EIR3nmds7BJ3n8zgoWl-_qoT0zIzFrbR_GbCiD4rS3aNSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
‼️
مانوئل نویر:
🔺
هرگز آن لحظه را فراموش نمی‌کنم. مسی بواتنگ رو رد کرد و درست جلوی من گل زد.
🔺
بعد از مسابقه، بواتنگ شوکه شده بود و گواردیولا به او گفت: «احساس گناه نکن، این کاری است که مسی با همه می‌کند.» سپس به ما گفت: «حتی اگر صد سال هم مربیگری کنم، دیگر هرگز مربی بازیکنی مثل او نخواهم شد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101973" target="_blank">📅 11:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101972">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=VnkD_byJYV3dcNNJiKcBY1kcIvFX7dl4WdvO4XwKN-XBsEMZ4PEGPLgEQgx3w_TkHRrrO4u026Fx6zyGBoYtjPh7F9XhFs75Bm6zg_KaVsZ_RVHgXGrKAWTlHsAgVyS9mI0IxfkpsLFMH2zcd8PJs8rx3JiFOfxe9ZQiqZiry1F0zyClBDF9EGAsMRXmWjxGXG25hmzhWracGDH01hztg_k0p5JwO7-lFzbIZLyIo8RBMLejv7CHU9oyHKD_RhkC2tMj72Ae469TmB54HARd3c8qLQfIHx_XrWkTN8N5QqiYk1pB1Ak3Zq7mMlK_zZIrtqJkfvNoKRS6-4Fzwr0LFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=VnkD_byJYV3dcNNJiKcBY1kcIvFX7dl4WdvO4XwKN-XBsEMZ4PEGPLgEQgx3w_TkHRrrO4u026Fx6zyGBoYtjPh7F9XhFs75Bm6zg_KaVsZ_RVHgXGrKAWTlHsAgVyS9mI0IxfkpsLFMH2zcd8PJs8rx3JiFOfxe9ZQiqZiry1F0zyClBDF9EGAsMRXmWjxGXG25hmzhWracGDH01hztg_k0p5JwO7-lFzbIZLyIo8RBMLejv7CHU9oyHKD_RhkC2tMj72Ae469TmB54HARd3c8qLQfIHx_XrWkTN8N5QqiYk1pB1Ak3Zq7mMlK_zZIrtqJkfvNoKRS6-4Fzwr0LFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیوزلندیا اینطوری از بازیکنای تاتنهام استقبال کردن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101972" target="_blank">📅 10:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101970">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OuEBiisLdqyGC1RVdyAeqXvI4rXtQlyyXPIn6MujdMxA0OohotgTzLm22HIPPQXjL_DJInSJLfvsr4048mOr_KejV0fpTfmDHIFXYkBkU1GXcV2tWLJwqn9mPLzfFWJc9iTsvYU1f1cOcg7cor2vaGySznYdcNpzFy7sVpHaqSnniUJ7qLPUiUQPKf_XehZaOtIiUZJDkgrpj9N0AzlSuo7mCz2sjInUl8JVulqPrD3W7MV3FcEA8xLvNo7wMSMcxuGZ3k3qvvA54ZKpC1onUoG0jxYfSK_yDHUuN1WQVp1pj4p3gCPI4YGW3GArM21_uAahWtEH4QKed34nRhPQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOGjvGu2-HeAYqz0epZ2oNoDYiugMLGodJA5DPqWQJZGyKx0KJjPb_kFvv6Exz9n_uvCeRM0_AjikataL7Vbw84QuBg8ysfRELJkpTIGiPmk3ED0eknp6xsOVgxQ9-fKSJx7XZ4VcCCfFCgt8fmZib8SsoxCxAK2eWEDSpRQI5C60WuRILbNXqJnSHVfGwKRyYFakdSOE-aImjB54tnwV0MTMg9WTVaqcgQyvaFK_Oxu5mW_oCCk8CzI7qG98Gdnqya8wOQjM5Rxt5MvcTrM7DYhyobRTenLt7aa9MBfnox-c-xWQ5OQx4Bp-sFVaqvq4Ps54rECm1oQ5nND93gvqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پدری داره تعطیلاتش رو اینجوری تو اسنپ چت میگذرونه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101970" target="_blank">📅 10:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101968">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXlMOeJ1eGIHdYz1-rSmz3DzWtQZvE0AlO2mtR4toSTQyASokNoLmvAn19ugTHwSxZfzFkNrlfrUQXP3NHQga84PivCZz2kz0tscTekzPxqYndvGXMq4_EAI5jVZ0G4fo5U4JLJ1Ey79ATrrX342RD4zPXPgRU3z8uBqdglZHrgFlbR1GKFww2atekHzxRqd1ONu5-i8YC1iGdjoYqbtwtgc6BoRau-ftDcix9Z6S2VPbT2dpVrwevwtr5khqi73oUTc2aZd2IDeqtMig2TJPNKPLapEJ6FJG7zVquhBSL3QZHwFbc4FwnOOGSfzQubepDhOIYEz8Z5ZUbGG3vfjmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/trs9jtpfXxcxfVZ77HDIuuza3usybEoQZOD-ZCWNLiSIIUFVjFihTJEdPhm4Miuqy5OjMJx3OAa61Wv-34mSSpyRX3Acw5iAwJIQybnY5wul47LoR_Z5iCqrVo66LvFKIZbFkG85rejN_XPuoa8rUISkHGhBUWT8WlC29RxHHL9aBwRZaG7FGs5fOilq5Xp-zjAF8ZUpT-v67ToYTipG4odPmlpgw554bTgskbZMnlQVzRa2pPQT_Bt7rq-84gFTthWwB7_3tUlBPDcSpTehvfDaquFzxgFWY8acBfXCO1J4TDtafSgBnpHJONAltcs1EysB9up1PIF5shvjt-3p1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
😞
میگن نیکولاس پپه بعد کات کردن با اکسش تیانا ترامپ ( پ.ورن استار ) الانم داره با لانا رودز وارد رابطه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101968" target="_blank">📅 10:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101967">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3EQi_YKrkBl8ZhqutqMMbj2CcfzxpI6n8pmdl0w0yDf5jWHuUzZGSIey6X8pAlP3BVD5dtlu9y83yJXD5N_usC9zmPHIq3oXkAx7ZmNvlCUq8xrktvLRCKLkn3AUeqPV0cX4XpKLetOCbZrwqIYT1SIg_4xfpcdl_Qb6ywckciIfzwiorFtQxmJJ93BNmdVZ14Xy1HUZghPZN-S9-OlPmWfJ--7xEL7UrzwPvCTB9VeusWnkAikpeyBMvmM2wMubQpaTY5buYxelzCrOLWF53gXbhdyU7z7uuCj5sT3KvpU2uF6G9gToR74JMJ_Ipq23nJeDzUte4yVHqrd_h18ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
موندودپورتیوو:
اگر بارسلونا نتواند خولیان آلوارز را جذب کند، دیگر هیچ مهاجم نوکی هم نخواهد خرید. بعد از جذب آنتونی گوردون و کریم آدیمی، مدیران باشگاه احساس نمیکنند نیازی فوری به خرید مهاجم داشته باشند و معتقدند فصل آینده فران تورس، دنی اولمو و رافینیا هم می‌توانند در نوک خط حمله بازی کنند.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101967" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101966">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSZzCuDQ8fNE2TBGeDzoWsUxeIj5BAiZ-TUTQ4NTmTJsUwKIKKrGOItdHYGaO8oSexCVaKsGPusJIyPAajVcXZETPUslJgOpEsYTkiaNnw_jZ5IuLPcZ0bi384jmpK6sApHl7rAgbhhseFVbksxwZzYyCVz9KeL6b5Xkwcyv27J_LbWEE6IVMtE9eKL2J7Ij6qJq5X4UI3mGhyP2aFPW4c6kkAkXRKD9jgCy2d9KXJXnh23fQXQ70NvMFbj9fJT7AVTFNfoGMsgUDIRfBu3zIbfrq2KgtXmT6XNTEqRxm5ijW1f6UoM98VSyOzojMtS2YzJg7PzecTMH2ggHXrXQQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101966" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101964">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M8njiDWKuiQgeMoFOqQZrYmWYlEgIgl-i7R6g1Oc5IxJ7YTAx7FDY4Q_HN6pERW-GhFnRcCUjvrpRqSVyj_dK3QkpNomJAL363sa7oaT8CrAi8sCPVIdxefuuNqzK7QsfGVhF88qjOJ2Aa5t0_2rzFgv_gWUSjx5JGDNTTRy6-CR1GLKhMAxXner6WNCqptXRXKdVESjfJzjGqbmgBwPf1Q_jd075vyuTLJtbZrjzArZ8V49kg0kWE7hfRBIgRzJ39bp__qNfgl5BBjo2bxQO6VibMWZ7jP5YVqmDieKMmnTfb3Pck8ErvW5RZWQUGehped4UIIQBZrMdYu-GaFhTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/meg62nQ6QeXpr40eH-c-9R9lRz_ZlaJpVqK40xYf3wcn9Hm9qfzSSvrYck70YNZGE8Bs5-FY4Kod5MAEd1EpOx5h3LhR_w9qUtyHjv3Uei2Hgx-9KdT1K5-wbczKur1zs4aip2m0iJuptcdWzf1PGT4fW6FdjBhXpkufBqHQvs6Cc2ZAgpaZfDOq_B0-XjOj_YEbNw00wUIGjPrNhEWCLM-9jAJlu5RO4Oe4H1p_RDEwoWlDmyx5TqX7-B4yjOO5Qfsz_X-U-q2BMExHYuK9FxKaMs8FcdmRH-uUTZUe8KrL3gcASBUfgvPPtAJvPo5tc337cARQCp3dLeaaFTCsCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سوفیا رین شایعه‌ای مبنی بر اینکه حاضره شبی رو با کیلیان امباپه، آقای گل جام جهانی، بگذرونه رد کرد: من هیچ‌وقت با امباپه شب رو نمی‌گذرونم. هنوز باکره‌ام و خودم رو برای همسر آینده‌ام نگه داشته‌ام!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101964" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101963">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hW5KO4HHlm4B7GnFYUHPyo3IMjSwOYktzPiFr8un4CC6QUq-J8RypCLI0lIY7BRFccMXCRuQ48SAFVu4QzKRFzG7mm3BqhfjM_Tg0W2pTojOQKDGBBXB9y908nJh9UaCVL8PdMZPfiKONfpHd8n6qLvctg0IfDWUwWykpbAebxS_HI4wQ1H4aEatYZlkNUs7r-H5L2oBb8svW8nTfimacPsOUnNzdXnYU1JzO9aCRlbsy4KA13O0eLLIlUsc1iCBApEAc1Er7Zm3J_RUSOxvubOGgMwd3OMxjYzxWjkGWCCfJVKS6arN4xDD2kXt3jcW-sTUuAilrZtnA0vr3cXt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رونالدوی برزیلی درباره کریستیانو رونالدو:
فکر میکنم بازیکن‌های خیلی کمی مثل او از بدنشان مراقبت می‌کنند و این‌قدر اشتیاق پیشرفت دارند. من تمرین میکردم چون مجبور بودم، اما او تمرین میکند چون عاشقش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101963" target="_blank">📅 09:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101962">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=cZLuUBmGVCJBYDSztylg_49pHhLvBNrusGgu1spZLjzx1PAT2KAhpXqW_wOKB8oLioYN7QgCquJ0lAPMwA7GZlC2DiAzRiLF9lRI0_sv9FLud84rb21RaWLrHQmi-MwjL2_mgGzgtES3OgHpB0SFu2kPNmqSuY7oiZOKl1A0SGB6flNemT79i2ONQesOOxoZsn8K5Xe0yxbw2nldi4hvyxk7dA9F3kDbrpB4_JN0W4iKl0tHKHupPZ39MREvFwDXAoh8FOkBGFwL4_esotEFb_RikpvNDzFwbwicm7GEGigeH-xVLpwGQUjWWi31oGNgjEwUe0fNwclUwpDIRExwqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=cZLuUBmGVCJBYDSztylg_49pHhLvBNrusGgu1spZLjzx1PAT2KAhpXqW_wOKB8oLioYN7QgCquJ0lAPMwA7GZlC2DiAzRiLF9lRI0_sv9FLud84rb21RaWLrHQmi-MwjL2_mgGzgtES3OgHpB0SFu2kPNmqSuY7oiZOKl1A0SGB6flNemT79i2ONQesOOxoZsn8K5Xe0yxbw2nldi4hvyxk7dA9F3kDbrpB4_JN0W4iKl0tHKHupPZ39MREvFwDXAoh8FOkBGFwL4_esotEFb_RikpvNDzFwbwicm7GEGigeH-xVLpwGQUjWWi31oGNgjEwUe0fNwclUwpDIRExwqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚡️
بخشی از گفتگوی جذاب بکهام، زیدان و زلاتان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101962" target="_blank">📅 09:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101960">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AefgnEq2mofhOcBQ7vobCTP3wwlLqlKqlyCvfs_a3n1CeYovHXZeLyVgkCPsTPPEKz-dCeJZQ_4bZVWsjxBV4uUxTr3B2IQwaU3JwpQQwZrHDTIsPQh2DXfrAW2zG5Odd3EiRq2jZGBLha3VwnrMWYt5l4EKbb0YlExaf-eSZ5nBKM1rS7VBvNWEqoxJurYIU5cb1xKDp8V6kNNSTW20l_7ioZPousaH6Eb_WhcF_pxAGAKRw__0T8YAaeKAEZpsCuRWFT6WvLh1aiCqnDPrJpzP55QYPRoS_70Ri5C42ks7NQGulx9_JbB4HnSxKGtPHmkOlOCbizFDwzoXD2eEJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4QCHzeswesu41ymkyQd96UU-Vq1jLGi-NU1C7qcJPI2ZNNhY97nBZ9N_rirzSIRJE1YLWEmcxeA122Jae8PZ0Mlp9kBP24tBbpdcMJ8-i3Xg7IXBC3-jPa8VCiGarQCkyN69XuKi4ukJGOvw9eOg147rsnFGMU3y17zGlezerNODErbf700-9VQkUWL1L97yl5TR-zC1MWk1a2QrFGv8_4oxdmYgFQF09zwUF-CaNoKucByX6LuZN-tBgUEJGtWSJIkt66USNOKPuGZaKZzXJ5VIpXeP1OPDH-z6Tm5igVKevHA7Yo7rY2jdDbE95rlIRsZ1TGPZIKEUdeS6bPJ3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریستیانو و جورجینا قراره ۱ آگوست با هم ازدواج کنن بالاخره. تبریک به این دو نوگل دیرشکفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101960" target="_blank">📅 07:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101959">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoPgl7IuPwKs6arMKqhTE5SPnsvoW2dtHUrC5uN-zm3eYSZWMIOEkDprix5VqWIpynTB7gbaZJiqxqAQWyt9Vbb4Xx-Ze5b0sa25LCBLSqL6MF_agqVugSJ8iTi0KhigcwM_oCjMutuGc8n-cJI2T7BHiY77UtuH8anu36pTC2HNh3mGlodhUBpfIUBbqYT6MgNxVXvMHDAo_9KQYXRbpbkqbXqlgjFt-1Iqvg8denFQJOHPMSe2uPJ__JqZUA7r3wwovU6gX5hwFS7sAN4auxSrOZPt13sc7M-5jDy1y5k3zgfKc02L1uG58FCeqSq_Ez5hvHQey7XylmPTq450DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👑
موندو:
تعجب نکنید ولی احتمالش زیاده که لاپورتا پرونده نقل و انتقالات بارسلونا رو بدون جذب مهاجم ببنده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101959" target="_blank">📅 06:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101958">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=EqjpZG3q9q6_z5hz9hkhweeOijaPL3gv4SZ7AhRha-mSShKpEIec2S_x8e8yhtlAaeQLPlfaYYbPb9g690L1l3GHqxLZs4bM4CVED9jg69vejabh5c7511TKDzs-rR8PAnKTJ1JNoSeCDTc3IhhSIXDqkdksLl6l54n6Jj_ePGXB8cXRyeWMyjv_x4kBe7x7kq7FJpUQU8FLw-E9wlP3yrFiWKnjdPqa3RUSACeaMEHAQWkPnBYLsiyp-QTqSxgEKPKI_rEWPLvtfsfFXRXRt1lg524-UG4vnbUytwvZ5C9G4BnqD0sy354eap_bcLMAqUSK3no3EqdvW3_RyCNJ-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=EqjpZG3q9q6_z5hz9hkhweeOijaPL3gv4SZ7AhRha-mSShKpEIec2S_x8e8yhtlAaeQLPlfaYYbPb9g690L1l3GHqxLZs4bM4CVED9jg69vejabh5c7511TKDzs-rR8PAnKTJ1JNoSeCDTc3IhhSIXDqkdksLl6l54n6Jj_ePGXB8cXRyeWMyjv_x4kBe7x7kq7FJpUQU8FLw-E9wlP3yrFiWKnjdPqa3RUSACeaMEHAQWkPnBYLsiyp-QTqSxgEKPKI_rEWPLvtfsfFXRXRt1lg524-UG4vnbUytwvZ5C9G4BnqD0sy354eap_bcLMAqUSK3no3EqdvW3_RyCNJ-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101958" target="_blank">📅 06:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101955">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JFXUv_ANZ4njC3MPQvFKVV5VoEMleKfbSWQ-sNBRQcIxvdSlhX_qX346fHBNpMOpyPuOKXdfq81-lj2lv3GmuDyk9tSqweuXUXefHTa87Uu0krpvGjlbHoYgHPunva6VYFzO-L-kfWGtYGa7YkNKICOFvHxm4ArADkvCuViTYZIb7bi7fd9LlV_OfDWtxPDJBHDDuH3xnLsMBFxWEAbDzC2RpjLTi4Y4kpyaXzmFdXJHezvoY9drBfgcB4jFWwYXa_mn4yG--xBzHnvUIGwWKaCnN2BRW6QSpMPzT45UYhNcHp3-zmKgsV1pDjc0qM0sq5PWd4EWHf-Eh0wtgh9Fug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZiSn-duIiAKX1I6nZTs7ciO1QHNrvTwTj8i17QbG1bCB4Yb7S5zYTBUDHafyC39haX6kvH-wUx57dCZQgcZm6Hd9fCqHAKxnu0xU1xI86CEXUB69emGYxJOFzQVI_DOsnWckTpm87gqNuOEbtfi0zKXWdtFdI4SmZE4X1TIK7OakgH9xcLeYQJr0i3aXBgq1KkVx0LnxJHuE8jWRSw8bwXwuFE8mSVCTFPujbt2Vq1kXVUASzGSv8JrZYTDTUVSQgFA4Ty6_1F2KCnu87nlYLMGcC8RoVMzCHpSoAWySicXRpxfK4HbQANskkORMBMxfgagjDZx02e3ys3yGAZKJlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=XjvmQFPzU4Vz--jwaaCCWdLFZnaYlTMullj2d_LxY7TgGqbg2v7zuEzt1OMasEayV1hDHOJrynYEaJf-HTr3aTr4m1NhlPo0BtxF4lTwaQGM4J8fbBKj7UrIZPNXi5bINrci4YQghA7QUSZL22-NMuyAlaiau2yQA5FueQIxcQ4cZwxFxKSGiRHE3LOYSv1PYe2p2o1dqk9rcQTue8kqzneEbitmK_6uGocXgY7NtjtPLRECietsIHeZwaE6d0FP1K3ndTpnINLm05pSfpjqWpXjzoHgt8A160SfovJ4urCLdBzfWcMvQeLUdyOc9VzQ-RvgmsqFEJHXRc88-qQObA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=XjvmQFPzU4Vz--jwaaCCWdLFZnaYlTMullj2d_LxY7TgGqbg2v7zuEzt1OMasEayV1hDHOJrynYEaJf-HTr3aTr4m1NhlPo0BtxF4lTwaQGM4J8fbBKj7UrIZPNXi5bINrci4YQghA7QUSZL22-NMuyAlaiau2yQA5FueQIxcQ4cZwxFxKSGiRHE3LOYSv1PYe2p2o1dqk9rcQTue8kqzneEbitmK_6uGocXgY7NtjtPLRECietsIHeZwaE6d0FP1K3ndTpnINLm05pSfpjqWpXjzoHgt8A160SfovJ4urCLdBzfWcMvQeLUdyOc9VzQ-RvgmsqFEJHXRc88-qQObA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101955" target="_blank">📅 06:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101954">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdZ_3yo6Ow6VrCflo7hflkquydDsYzWWWvpmouOIy28ycGng4aI6eLkMDkDtTzmGlIzaMNiUflkJvXc2d_xdkPTONaGPnufOqs8GmueUwWn6cnPcvzMGJBFmpv6hZxXfxHYidq-3YSpOevLRysRDn8CecVTEjcRzpoiEnRAR8UtIFM5aEr7ySyKZGXLwaYKtYxjQAPr-EnKtBu1HpxG4EkYjikwLTprsRRjnqvKWGn1jmdcwvzArcWWrto3ovKTmAqwuKJJ6UhqoYnlqNMHXRrEJeL3axEe2BUa96Yizg5DP_pRuLH1zQj_AtVukzyid4bHlfQDzQinJkmXwktddaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
مسی امروز اینجوری تو روزاریو شکار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/101954" target="_blank">📅 01:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101953">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu3zCs_uQ0zzhl66iyWPSefcSQWw-lfaF4VW3J9Xe6lPwCz_I_okEsqv1wrOtdIYYRjK8ZgOnm2q6n2ekvA15LFKEDwPmiOFU5TIxoF0vOxBv3kIesz9NFiOLTkGi1IDCIzuXgQNRcueyxqF1iWaFyAjhHxM_1CkPt0a0I338zrt8cV4POosBRd1L0w9x6rXbptATf5xhUJZOhIRFtYm15jAwxMl4MPscN88C2dMQHdXCXqiz1_QB9YBHrGg7eW8Ru0wCJfz5_IWnVSYXtXJdF6u_Uga4CTSzTdF3_4v7sobJwUHOzmZVBeWYoxFFiWkZ7SrkHkxpG9z1706eUHrF6BkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu3zCs_uQ0zzhl66iyWPSefcSQWw-lfaF4VW3J9Xe6lPwCz_I_okEsqv1wrOtdIYYRjK8ZgOnm2q6n2ekvA15LFKEDwPmiOFU5TIxoF0vOxBv3kIesz9NFiOLTkGi1IDCIzuXgQNRcueyxqF1iWaFyAjhHxM_1CkPt0a0I338zrt8cV4POosBRd1L0w9x6rXbptATf5xhUJZOhIRFtYm15jAwxMl4MPscN88C2dMQHdXCXqiz1_QB9YBHrGg7eW8Ru0wCJfz5_IWnVSYXtXJdF6u_Uga4CTSzTdF3_4v7sobJwUHOzmZVBeWYoxFFiWkZ7SrkHkxpG9z1706eUHrF6BkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوکاس هرناندز: «کیلیان، اگه قرار بود یه تتو بزنی، چی انتخاب می‌کردی؟
🔺
کیلیان امباپه:
فکر نمیکنم هیچ‌وقت تتو بزنم. دوست دارم مردم من رو به خاطر کاری که توی زمین انجام دادم به یاد بیارن، نه به خاطر تتوهایی که روی بدنم دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101953" target="_blank">📅 01:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101952">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8JiEAHSpEC9eNFhNrEpMvIizuTN-t3bo6nlBVVzC2pzD8sS7y9Jm-Nw3xC07_ljvht1DXu1TKZTH8lGxFBDzw35tk3kqZRqOr2ts7jXr9eZ2VyzTYZF8gDrwek5vvXv3uvdE3Jw5JTJh1j9LG54qyJqyDC4ZUVb8QC1AH1T_XitQNCHb7rF2tI7FpuKKIxBFRf20vwLEOwCjSLetmsBERZgjPBrVR_jxapEYgZBeNrWBWIAG-p7L5beQRB1kxXdFV1lpRwGtvm4ynOW03XL00YVL2H6d_xGI2Ba6kSup7ZFF-r08_wu-nx7I69-g3tyfHOtv28FkzOhj111JrpRGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
امباپه و پارتنرش بانو اکسپوزیتو‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101952" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101951">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNZtEvEG67y_r61Eu11l5JXWmhRuEhOeZ60gKO8SuHwqpnGpYPQlNVw2A2pRcXCO0vmNvjHREMsfX3dd3cVWdYvExfvtLE_8fKm0q19T9c_YoTGWx2YpT2sz4fO4IBEbOCQdxWfz3CwC2-1op9fyxaoJPOHjvZj3OFaYzwgUZ8OWPZXo8UrVryyHEvDMFLMP0brXLS71_0dGxRNP3p99UUQEd2N_FkOeQoIuYi2Z5vPTfs6GJePrYdFkc0QXxi-U-p6wz1U70bSt4H11tiSTX8arJkNfIz3x6zFwM3ev9yheeU2TXabAbZzZYlU8f1oochQ-5nbtRpGKtiSz0UWSfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی خوشتیپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101951" target="_blank">📅 00:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101950">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63dd42dc4d.mp4?token=uVE9y7V1a8LqnwMuS2R0ov9ytSDawaA_QgVE0R8ksXjFV_JrCC0Zc3ow4F8W4CkoMXojztxIubdXW6OcULvnsZcHa4xf31UmZdSz3qt8dF3tnBhCzq_UQzmnWxJb-3KQuCXea8kMrYw2q1Tj-PSi-11DBY6CRyS9xAYuHjQeGZlntsLciw664aVJT0HFTuCAX9aoP2qly_qZVLVeDnJ4JdjhDHKhwO_y_T1mxYJsmF0-fdINBorkTJslbl4OFsfPfqJaSk94B-XzIOZR4tfVWLNOqBlq-jm7nU7_c58KxzP1NU4hPhQf5oRPSzlM49wXEWKA9YvdzcdXsN0AExGG4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63dd42dc4d.mp4?token=uVE9y7V1a8LqnwMuS2R0ov9ytSDawaA_QgVE0R8ksXjFV_JrCC0Zc3ow4F8W4CkoMXojztxIubdXW6OcULvnsZcHa4xf31UmZdSz3qt8dF3tnBhCzq_UQzmnWxJb-3KQuCXea8kMrYw2q1Tj-PSi-11DBY6CRyS9xAYuHjQeGZlntsLciw664aVJT0HFTuCAX9aoP2qly_qZVLVeDnJ4JdjhDHKhwO_y_T1mxYJsmF0-fdINBorkTJslbl4OFsfPfqJaSk94B-XzIOZR4tfVWLNOqBlq-jm7nU7_c58KxzP1NU4hPhQf5oRPSzlM49wXEWKA9YvdzcdXsN0AExGG4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ری‌اکشن هالند به میم هایی که ازش ساختن.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/101950" target="_blank">📅 00:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101949">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFAjpeb59wYrTW1JQKfyBwCmKLeFZ88aL_HnmulyJ36J9FGHRLHoLwXJj5herCHQjdN1OJD_o5dFTIAanUB4BD1r-i5p1QQaL7q_dFNnX1oRmpXc5O5EmN36L7E0mRnA81dy4B0f_LzhunD26yiTRIBS6xDyDcV2izFAKY4rP_D8ErUwbsQlfX_aQV3PgCAsmRf7C5jtFgT2M3D9lUgAhkAHteVfCH2620Ybu-McTPhjWg0SWVj6wpjzrcWyjmQOn3VNgEB-PNI-jEz8mX8iain3V0Et55URJPuba2RBlx6M3moaeu14odylkAZdwgnzLn8XpA59BtpUeI7NH8rxGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101949" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101948">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1g4yGawof9j3QGozj_aii6t4zsm0ckDey5zCWoItFg3hbohOolYzRVOXwUW_7Xk9Oaq9HbhMehmhwm-ntxf7ZHXRB_WI7cdzKeHcOfuhIClLJ_M18Vew7LN8iKIdCtAt62LrEYSe9f2DU5AsK0EjrLC7sGFfzOi1dkfYSaEK2_Cz8VyfgrGxlR_7jUd2YvqnOvuwd3N-7ikbB5tvlh3jDinPm94YzsL6ntlm3xU25mRS04ffeYZZpI9DxpRbn57skraqZC7Ht9Ld3Q4KG8nBR-bUW20VGedW2XB5NxaSlRP2L-wHmDlEqF7K_U6-AYLUQoK20mIAOyAWteyJfX5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔹
ساشا تاوليری: باشگاه الهلال میخواد مبلغی در حدود 120 الی 150 میلیون دلار برای جذب لوئیز دیاز هزینه کنه! اونا بودجه 350 میلیون دلاری برای نقل و انتقالات کنار گذاشتن و این تازه آغاز کار اوناست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/101948" target="_blank">📅 23:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101946">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NnZF6K8LEqBsg_yRU_MNpvjnQZVuS47zKpiJHHbzDPrf8Q0TYuZSy6HbY-CT_6m6zVqsIKtiyForxwzBYV1z8sDw7mL2EQ5X_4aPFJgnxlozpuiDxGulU-ccWror07ebwewaDs47v6hPzH-hn9ftK4ZYAFo-FvTrCzI4VHW8s25P4hYovAY2Z4LXVwQ5IvXD7HFGm3hLUjKDpeUXnbVWUvXurDp43CnfK0u-EHhPAdjJTdzZg9cVNJXjaSY7HcthBtwjHMPWyb-DvvUr3Ylx19z4fDIQDiZJ759k_RAP3TGnpmuUM9ob7GPLQSdCUXkZxgefcg33DIM5PlR4ThSDHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PcgNnhOaDfo0_1iqrgkVdYkmTckv07WSbbygeA336ekLhl1WJ-mGNr6lQk9EqYTF_8Q0yHI5yJbRnrIIDoggmB-Cdr-64TJY7sw-mmvmkMNz6R1eX_wu-4auOf6f48b3trJl_bK9T_erHKxo-_pGEIE2DR34S4SE_C9JTDM7_hTJzNpCl1jZPDai4EVXGEFwnXwlzPObvVn-Ao6Dn56comnq0nnD_dIMUMNZ4yYFTtk5E8FcbGrEnmRaPCZns4DzP9orcwBfi8dP1nPkTzRSkFg_xaXPzh-Q0kPBbSGzIEi2PI6cEt6mKf4X9VH7btlBArIxVILfxxc1LImhXLxLJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سرخیو راموس درباره اینکه بین کریستیانو رونالدو و لیونل مسی کدام را انتخاب میکند:
برای من جواب این بحث خیلی ساده است؛ اگر فردا فینال داشته باشم و فقط بتوانم یکی را انتخاب کنم، کریستیانو رونالدو را برمی‌دارم. مسی لحظات جادویی خلق میکند که کمتر کسی قادر به انجامش است، اما کریستیانو این حس را به تو می‌دهد که فرقی نمیکند بازی چطور پیش برود، بالاخره راهی برای بردن پیدا میکند. چیزی که بیشتر از همه تحسینش می‌کنم همین است. استعداد یک چیز است، اما در اوج فشار درخشیدن چیز دیگری. وقتی کریستیانو در تیم تو باشد، همه تا سوت آخر به برد ایمان دارند، چون او بارها این را ثابت کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/101946" target="_blank">📅 23:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101945">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8jf5Zz0hfdo_JtN5rhlMdm-tpx5XoJKqG6o5c9GbhRiJJe4wkDydIzsWFqtJ8kDG9QWRSMY7GS6cgBdk3t-DISRPzgGx4NIaNxetQdj2X_6AJDrop_654fSJVf7Y6kxBU6aJDdz5TSoKsKveEDt19IVz0Xv7e80PNe-KGwye6mzQj362ZY-h7qjCrcscjwNfaDCUITFERy2MUy-Fc-3S0sUEHykWiY2RUFc59TyJuRKEhOJuM4RIJTiAwdz8Qd_RnEcLrVE_RUAMnN-1l3i634KiC_m16RNGid_xKgbpFRt13A0T4IE-uz2TDRh3N3jQwJyUv1zYSj4iMxXDrFVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
به نقل از فابریس هاوکینز:
مایکل اولیسه تمایل دارد به رئال مادرید بپیوندد، اما بایرن مونیخ درخواست او را رد کرده است. رئال مادرید تمایلی به درگیری با بایرن ندارد، زیرا رابطه بسیار خوبی بین این دو باشگاه وجود دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101945" target="_blank">📅 23:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101944">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwAYvpINozU43DUzZawOGZLJ3cdsNW4vwIDLUjrGvE7ca9N2sFMvr8jtSCwJqz3ltaYfyXZJShkIZBDh0MqUW3fHOnS4kAqnnAP5-fX87Ku2j3qt_wXrei60lvvEkv90JWfRVvNNrHe1ourABeqxixw3GLvIgYdJIdWbv3iUVjaku9gLtRANyDL6ikqEm13gzCOhNNSQlpueYdeO3lzWwZqnQBkt5naKHHcl52dGl2ZQaGyjsSYz-Kv7lFOdEmPxAy49Nyhn5pjAYTyxRtIOZtlOiF2UODz-BimgBdKp8yzj35fG5qxs6549gJbA58PP7lVt9xu5jqwGsefYtIs-PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101944" target="_blank">📅 22:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101943">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqXZJPCKsFv4pbr75PYJXFHqaV2s2Yg0nMqiejbJ0HsRcY0qSq7ePv23UKf7cUuGcggI_n2fD5YWEgOJ6cjN8MN5CwbJcXtpSVLMTy4dLlv40cbk-v3OGCQwmUy3XXchhZ92rvBvcAJeN8jES9sBHL0fxBduPvQq9jXSy826rotMoR6ZouLs7tDwm8as6w_6ycMZGFGRp60gJX4bDsQjC4KoO9IKBafvRprG_ZIDdJiD_XXD7NYz751z3TDCwMpZFcSn98YqX0R2FSlygB8WLj6epS9Z0bclTIJFAZrh_SL3ZPWkJHadrd5JPA2k0GFElX5Mb2xtwu3_dCFr1be6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
رئال مادرید و یان دیومانده به‌ صورت رسمی بر سر شرایط شخصی قرارداد به توافق رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101943" target="_blank">📅 22:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101942">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwpZyfNeF3JSVVMxNcsfdNo7e3dESmAXvcgJO3ctuNa4mf1_XGWOJH0_C6_NhChtMrtj52NFPmUgEiu8lnfr2QqHp4QX17EqAKrxIl-PBQ1M4p5q1joIMMIBY_FWnI9lpkSkLeXd3WCq7o9MQNdQdXnD7vZlPgbSB9vrHwP7RLDm8VoPDe_8T9D3z5luwyTOYF326qpYT2LhvZadmHDHvlpGCQAQlBCMNz3lf1mUyuifLumqnd8U_B2SFiC0akD2eavIQoo69mZsFcx7Osm8VmyOhyWPSJM3x1qZqF68ghnI8sZCQGK0ok2ZGRGnDqAEPe5_fvz9tKGGoItRC0gEzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
ترکیب احتمالی رئال مادرید برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101942" target="_blank">📅 22:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101941">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_4vSpTJeVT5I3YAt-zMDzFm7QjpjGCsWOtBwJS-DyQWOywDokPe2iGKKTGayDON2TMOGbufPcTKbcl6LLmplHDp-ldXEB7Ui0yNMI1tx51Tlgw6puSUmU45ApE6n1Ta4MzQ5TmB5d_jNBwi9lQgD93-vJSOteQwrkeBAfWtxTwUjofTbJjUhxNLR1Suzpnblkm51th3NeroeEU4y8aOqDOWmy8KbbKSl6f4jUv53-OjjaFykZuL3soxIj2XnH01UXbU_bifctzLJEOaQI9unlnnilhnKZQNnfc2GHYhp0D2AiWw-DmnX2r9f4NHzXylQZuUKpfF9uUbx2_1BhcUng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از قشنگترین تصاویر جام جهانی؛ مارک کوکوریا قهرمانی رو در کنار پسرش متئو که مبتلا به اوتیسمه جشن میگیره.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101941" target="_blank">📅 22:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101938">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EgDZ9zFHsMntHUIRRsY1-9jP7Ix7MZQ1AXrP6P0FaMFjBxPFvrHaggzcXDHipWFhLQHyCs6ntplBd82xdgxEUHwI_d_VRR-M24J3miGYqavjqqFwMSuhgWOSv0hoWwaH2DDjTyL91jGsXr7QBwdcoasnlekWUCXK2gpVCg6qmJS620CvTQd-mCH6JCcwDoQZEHFwr2zDMy1OgLbE6mhNLsT9PJU4fd36gpsI0a1-UD2dA7KUY-VfFimrxDPUs14cc1kejumz14F7iz9wc4f_P1b6jyEKEmFpIJEYeZrrbvNvklgndeRo9DK61uuq5DaIfvZ-lLrBikvjg_LIF_vzPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDunWDyOiwMv2B2JZcepO2jzP-q7jb24NsKMGeSTJ4XuLoiNr-_rEixKcqM3Gr6GP67oTS2dZ8pBHHYW7_7_J7HroYD3CKQ14dfn13WvPVn3XeLjXJ85g5Ffw8oS0vwJxB_Gv3UL4-qzpwuM0YhHSlY_ZMtREokWHhK7Ut-lnShTNJu247ZDE8J0izcDzcydx2BG3o4CALcRA9HV0sCz9APvfUWnoT70l3SpBDfBFcQyGoSyTu8kYnMc8ts0jGDRu2z8thsSCIhPQ1UG0ioCSoH-NHyuqZjoeBLsZtmOyxdb3ILaZaKL5GrDzfdgZesC0DN2TC1EwFbwtS3ADEsaxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MOKSQ-AwNh8xzEC24V_zODXyVsvkPAALMuoEfdynzPR_MQpv9kD9BwcK4il4n56WIKlFoCuPF7RVpWs7HOLKsb2Qnar7AXNBh8Kz69QOSVMlIlGT37Vg_i26Jt5Gbb-lqSxzWOlheKbuL2KVaB5qY5bUL0KS9DXTh7yO87OG3DvuAphfXVfKWNplZgrf1EfTbYM4WA4jqJr-4NAHHojYRyiGBPy88udl-ANSp9HCiuUGl_lxgnJvgK8DbSQ9I9BAuKAsfjg1PlMcD6LYYb6P3mvOaoy9j4y-DQQM7Q0_x0oVy8-kipQf02iITZFT3uagJ-W3mzHp2fiYUw5jVoUVUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇳
😆
امروز تو یه حرکت پشم‌ریزون دانشجوهای هندی تو اعتراضاتشون ضد نخست‌وزیر هند، عکس امباپه رو هم آوردن و محتوای بنراشون هم اینا بوده:
«دیکتاتور امباپه شکستِ سیستماتیک را تحمل نمی‌کند. همین حالا استعفا بده!»
«۱۲ سال در قدرت، و تمام چیزی که از مودی(نخست‌وزیر هند) نصیبمان شد، نسخهٔ پرمیوم امباپه بود.»
«دیکتاتور را پیدا کن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101938" target="_blank">📅 21:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101937">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWemb-S3gFQKVsA7v-qDk7ub5rTyY-fpi28-oFXIW1VKsiQE3eju_Eu7tUPbd9-Dm5piTF1F1n0Lj93zyJYWl0I8vyWK4v1NrsRgf0AID5c7B2BCBFGQSmK5AKJbIrWX8Uvu7cw4GXW7jFXjsBjsr9Wmt67Dz4UWNNqGngvP8DhGmrbMQi-claF0A3fllcchoXpnNTDEtjDzYZjbUjo40n5ejg9ewx8J-rTSGYyQCHYiAcAZkUVHTKLTik8YIOF3AgzAvJaJ3vgE8S9h63x-IG3RDpL5Grr6v5yB6XJkffmqXbQZ3A81an5S7cOEK-5q915YUN5VgTbClgeOe4KTiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلاتان ابراهیموویچ: "بین این دو باشگاه، این سوال پیش میاد که کدوم یکی احمق‌تره؟ لایپزیگ که پیشنهاد 100 میلیون پوندی رو رد کرد، یا رئال مادرید که 100 میلیون پوند برای این بازیکن معمولی پیشنهاد داد؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101937" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101936">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEpSm1tlicjSesxsSRMaWAaHDEF7T5TE-gsSyEK-1hz5_hHjTnvEaTv6Cxklv2mL5XYhgmQEcphf_p8kedLNyAQ2ePbIoySD-y6z35l6iFAskMyyQ_j8f5GgPsnol1NS8zJpr1CTcUkBP-jh4PDXV1THxFGXRcgHO9njdc4IaSW0VFt1AdX673fNPeNR5LhK2lNbmr9IZcyGQr-ROXu3pqiffS8LlrgYtMVsAzzJEFe39loWTFU637EnbVyS3G4ebv-Jhe2ZZQwc6Eu2X_yOXQIvbVoR6CXx5U0Q57VK4eFO7lmuLaHKQPUbEM7llsmZBFQOdmslGD7KZ3QWoTI59A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
محمد خلیفه، گلر جوان و ملی‌پوش آلومینیوم به استقلال
پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101936" target="_blank">📅 21:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101935">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVLNh9Y4vjCgOICL_gQtTBjnKS7E1pMW-iN2oY7D65Rg2goR_Ba6VSd657iA8AbjcM8BtWRk2ZyNMegynFbFGSMQw_LLpL33caJrBEyQi-pjwbG1Y274-Y_45JbQN7eHh9yGJCDZpDsVjjgIZS5khXI4mkEPpp_Yy_1uMdG0p2QqUc4_7PNlNliJZS9Y0QBsg96ZldS0W-cQHbYFXNRBQ7RlE8VDrPLRgo6gG1eIgaWTKsSLG-ImKOO-EEZrt3si7PI5gTPZe_GIxErEvFuNDMU2e76_CSvAkogyi5CJ_obp7fhQzbOis-q1lLM6-TsCw-3P_o0xRhCzXDcup-NIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ماریو بالوتلی:
یه بار زلاتان ابراهیموویچ منو با رافائل لیائو مقایسه کرد، ولی جوری حرف زد که انگار می‌خواست بگه بالوتلی بازیکن خوبی نیست.! منم فقط یه عکس از جام قهرمانی لیگ قهرمانان اروپا استوری کردم و زلاتان رو تگ کردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101935" target="_blank">📅 21:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101934">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ae_UcKYmuOpexHqagSMsO1DbnY0wT3DIMFmghv3JqgFpe-YXbN7_yCWAsBNueEAl4iou8UxX-FhdqW5Tr2SQTSmfNv7WWBVZmTTaO1lQhApcbVU2b-8NZwIpSM7lJeguXsvDWgoSEnbzxj_u1L9nLkv2jq_VcFpR-wvpCnvtbvF6aUqv_BpmRytsmiW_R3-7BkumRZSxVrVgFRuWLY6yTCncouq1xVVmj-pnB8eYaV6hp-SHuZHQBiX2LDuBwnIpFhp6TQXpkCrscx-Oqf3J5bVM2SW8cA9eKRyE3-7keWE9j_UxIpEgRj2SHYKaHgQ_BhanMyTraHcjja2Tv0TGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
کریستوف فرویند مدیر ورزشی بایرن مونیخ:
اولیسه به رئال مادرید؟ این موضوع اصلا برای ما مطرح نیست. او این فصل هم نقش مهمی در بایرن مونیخ ایفا خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101934" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101932">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T9bdtTFY5-uiY6ravHtJNG9MXTOZr_mZ8_2zz2sJj45JLAFecHhbQO-khF43rlkz5TLHhrwy-G371BGUi2CKlJnq_wTGFBLUJVsovyC4oqALv5VFwjJEJ5339H2PmFvOEci4ZpxcY0BM5cgYD8LNWItJamzLudxtMKVH9X_HbQFMv_F9zrvAfpYy_ApwrebmyYbjbDidZvmAg1rPuruNE-R8oaCY5yQZyNanGQWWVn1SNOh3XTrOQqamb7hPrxo-p4tZBEdOoaRm5r4HQyoPrT9dcQy_Lb_tMWFa6l1N49AFboITjHzvSBSL2QPmaWBZCLRmcTAJdJREogGPgJesDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t7jB5ZfBhHlojCCp9TKDGlWz-zxE4v3E-YQzALIwCGwMriSQCAif9GgZXLl7p4OBxWsQ4NWp9DWlBk4NYvDAYLvfJ6KxartBTMTTbdX5aSwXYGFvLyYoa32AeDbZnRiWq6q4r-OAyd4mYPOZIiiRJ34fLZlXc_YcQIGz3J6fRPgopfP7QBU8-joGLkrktmA8zr3ZsLrZUSPREtbFROohQbeofHELkb7bBzCSIjqyuDFftMj6EA5z9_YOoXuiAMtuc3hYHKVOdIXpkvTeIvdBOsT933XXKFFEnpc7BxdHbtnmuQIYw5VB-6Yj4gVtlUkL-Joslk-KOnsSrTEv1AfzNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
براهیم دیاز هم از پارتنرش لوز مندز خواستگاری کرد و رفت قاطی مرغا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101932" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101930">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmaJqs45fYoLwv3u0asZzthFAg9A5I5_a_ijnH8pJ13d3zOGb7qlLwqa-OxTePx01pcsPWiZKYvSST0dEEqDdCmWCiCo7C7HnGqGZZNHyV0qlim2Ce86FW2fEE8lXSaSC4aNG8v4_TFu-nyrP0Im1_FQbCKv1sqZtWsB6yUsv95_tw9mig6DBG13YbgYKZz2WFbHjeL3S-hYiWoa3PvbEHWKTi9zaRXm-QG7tF7HpOgHWOk0tEe_NDGhtuDcVWc_T_-iuHIX1wihbfmdIBl3NsDwrm18h_M18VgE5dvGdkywvFokcbxgwN1LC2yY09pKxZMuU6NQcfbLc-0KYqEucQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=p5_ZEVdXPq0Y8hjMr1mbw5ki6LjbeX4IjCShrKkj0aTsrH0NiyvOf0QFU6xZFsm4oHIlshdz4TUIqVo3LBflVkxbwajhMfPPbjuJNW15pVS-qO9Q72esnhwo1_akIIcjfHInpBcMOBo164KmMns70IfC_mOUPbj2yMCfyJsII58vYCEe92BVEfY2sMu2ZXLJ__Lvyrb2ExoAZQw0LLxolMSIM4CUN_5TagoTmtJPcJsV7VyfBxpO9udo9jVhiObMTgfZzOOi1yErEYUhnh0TFp8kRxephlzCftkzCXAk3giLYcrKWL7Cbem5QGf7P37CJKXHDhtAKA8vQA2zttTK_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=p5_ZEVdXPq0Y8hjMr1mbw5ki6LjbeX4IjCShrKkj0aTsrH0NiyvOf0QFU6xZFsm4oHIlshdz4TUIqVo3LBflVkxbwajhMfPPbjuJNW15pVS-qO9Q72esnhwo1_akIIcjfHInpBcMOBo164KmMns70IfC_mOUPbj2yMCfyJsII58vYCEe92BVEfY2sMu2ZXLJ__Lvyrb2ExoAZQw0LLxolMSIM4CUN_5TagoTmtJPcJsV7VyfBxpO9udo9jVhiObMTgfZzOOi1yErEYUhnh0TFp8kRxephlzCftkzCXAk3giLYcrKWL7Cbem5QGf7P37CJKXHDhtAKA8vQA2zttTK_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برگام عجب سلیطه‌ایه این! اینس گارسیا دوست‌دختر یامال، بعد از موج انتقادهایی که به خاطر جدایی از دوست‌پسر سابقش گرفت، یه ویدیو منتشر کرد و گفت:
من به خاطر پول یا شهرت لامین باهاش وارد رابطه نشدم. خودم درآمد دارم. از وقتی با لامین وارد رابطه شدم، بیشتر از چیزی که اون برای من خریده، براش هدیه گرفتم. کلی وسیله گرون‌قیمت براش خریدم، ولی اون فقط یه جفت دمپایی برام گرفته که حتی ۷۵ دلار هم ارزش نداره! بعد هم برای اثبات حرفش، کتونی‌های گرونی که برای لامین خریده بود رو نشون داد و در کنارش دمپایی‌ای که لامین براش خریده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101930" target="_blank">📅 20:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101929">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8-Kxh1L-419KVL4R5IaTIbROP8rDrRP-4cD5vlv99Ur9dxw_ycQ76L8tCNhDaBlseSy78rs3F5qskaGW12ztS0ymPiucULSJTkGUcv7BesBOzeI67kDX7l98h5R8b9Pn50oT5LVf9KjIK2D2Bz5cXr8CYnjfzGFbKHpzwEYbKKI-p6Cqf0uDw33E8UDGG7ZyUMeSG1XbMpsBrtkSH6Pv5esOi8ylizs93xmag0aFC_Na1Fcazi_EbnAB2ZlXgGjeIm6ozTE5bI6H-vFPZ2Deb_smnolGZzTW-cuWvnfl8y--90ALb5sSgk6Un9_MNbUnFsOAg82bFsKRW_0yvVB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پوریا لطیفی‌فر هافبک گل‌گهر با قراردادی ۴ ساله به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101929" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101928">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62941770b7.mp4?token=ZtuihivuuG-mg6GB3nQLR6rdEOP_nvQgvtSOBCiWu8dH_lFah_c6oSSPkGWm4AZcUhbPlecHSJ2u_gnHgh46-ThasedVTOwJxsmTS0zmV_OYboxGZe37VAJJNZ5VGZsSj44Sf5077LIOKX_oR-5vRS6euqbI-PJASLQMAe6A32R_eJu9wfgSCD96Xpi94YM2UFdN0ADgNK9I9OMykUWcRAxa_sWaftMaqBwhCRiWiSJaG_WGSy7feg_kfk9wGJvTI1w5m68-LfljjlZ_7cDisLrDRHoP_Wfh_j3P1Nt3_0NuLfRFJwe0h8TPEhNnQqXUUgE9hUSBigY9XDmxQLY-AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62941770b7.mp4?token=ZtuihivuuG-mg6GB3nQLR6rdEOP_nvQgvtSOBCiWu8dH_lFah_c6oSSPkGWm4AZcUhbPlecHSJ2u_gnHgh46-ThasedVTOwJxsmTS0zmV_OYboxGZe37VAJJNZ5VGZsSj44Sf5077LIOKX_oR-5vRS6euqbI-PJASLQMAe6A32R_eJu9wfgSCD96Xpi94YM2UFdN0ADgNK9I9OMykUWcRAxa_sWaftMaqBwhCRiWiSJaG_WGSy7feg_kfk9wGJvTI1w5m68-LfljjlZ_7cDisLrDRHoP_Wfh_j3P1Nt3_0NuLfRFJwe0h8TPEhNnQqXUUgE9hUSBigY9XDmxQLY-AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
استمرار، استمرار، استمرار تا رسیدن به هدف
این ذهنیت منحصربفرد ترین بازیکنیه که دنیای فوتبال به خودش دیده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101928" target="_blank">📅 20:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101923">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzhA_FifHgpBdLbanblqjNuuf7NRx6oXyxmGIVggZEzaoLBO_miJWAKLp4Ji5KDpvKXzmyN9pESfF58t9Exb1H7npXF5v9uNEMUI8tvPEiUZe8x42PHvJGv7HoGI0q6DdOAAQdXdlawgORWmaOVKp39pCZ3WuYR2l50Cxtfil2Q4klhbs5koHLThkgE27YNgB0G8s2ZlQNPO-3nCr6TIg6UwcL3UPSezOWSHJlsGJvuYoL5tk_UK59aAymMAmV03dMKI6MSdnOLS1wC5opOxd17V5VgCDAf8gSYhZXGQK5hhG1DHLBRBNTMvN1H7UtXBw-uMk99eRm5SaoUSwa69lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7S-pLpVneb8h6j4f-cw1J_LQkODWrvRRezVK4V6b7rzoxGgBloLTkRwlQ5In-OlEywM6XeIkyztToy8hjg1Gv2qTgJmt-ksFCMtyGnfxiWNGAG96i4rEXE8ban9z1-6s3Hm8rn3oZcK0Y4SxcW_mIvBGj_md2XDkA6HX8uSnnF70SjIcLp-mHIVBLu_x5Kxf80aLnVphQzNIcd9rGGPlW-fv9uzS5dVCG45b1_tTGiYnYM0jYyZmdBeP3d_adSBUg8Rdps2p4pt0haw853KX-h8TdEOvwVN-mjmP7A8ZKwfwhdXd2EoFI0zpgvazExW-myl3pq5HCWSDY24JGS03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZq8z_6JPSn5O2OqY0h371ISG-CjTxOkcZlYOk9luwGNRGn4k4CRT4C2TtF2VlhLeswML8t5yyaLSZ9EJQbrfruY2JvEA3C2DXtrhlf0-CSU7nTbGz_-c7pWEPuDVzLOT0oG_jRm5eonVxXi-eLatYxIIGrPnT94puODoBPnEY5Jc_tEsjaDew-lJbspzUFssqCUouYKBgIRI1c0eHJ0IuASTjZ2Nm4YbeS3pu458YHdPloNVOrMzozeiKrY85yHJFeccyUztsU_gP3PdTU2UOg6U96Jq8-9YCUyT1CxtHEORjAp0Bntl4p_LRRijmiTBYhcGvam_mSvXgCQzxSrjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=jje-TMbr4MZxHHzauMglMBPzBTMbFiOGV76ayw5QeMPczED4J8Yaf0m_7NKPFGXCl14S11lv3NDY3CoBqXxjubgFnjNfRU6NUNqi2GsKAo9D3PO3Ezp_nLRUIUEGDAjAzqur4yvmKJVQlyX-RPzs_Ct0QrgfmAzEzNT2qJZ83NHCcpWds1fsdHJC7sSvSAvvZ42xAoDMgbUQ6W1BjCNfy5NYkF7YcZ-L1KO3zM8auBMDWJewJ5tFQ1JpFrV3_R09-b7Lj9uUg6spHAC4HfKc_wbN5hEz5zGXo9DnwORVzOq9KENDYzKe26vuqhjAPOrKSR23gQ_Dkt8qlyT-G0EPCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=jje-TMbr4MZxHHzauMglMBPzBTMbFiOGV76ayw5QeMPczED4J8Yaf0m_7NKPFGXCl14S11lv3NDY3CoBqXxjubgFnjNfRU6NUNqi2GsKAo9D3PO3Ezp_nLRUIUEGDAjAzqur4yvmKJVQlyX-RPzs_Ct0QrgfmAzEzNT2qJZ83NHCcpWds1fsdHJC7sSvSAvvZ42xAoDMgbUQ6W1BjCNfy5NYkF7YcZ-L1KO3zM8auBMDWJewJ5tFQ1JpFrV3_R09-b7Lj9uUg6spHAC4HfKc_wbN5hEz5zGXo9DnwORVzOq9KENDYzKe26vuqhjAPOrKSR23gQ_Dkt8qlyT-G0EPCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدری تو تعطیلات در چین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101923" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101922">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbsfOJPVQo-txJ5vBGJnqTg_sZO9dT2Yh52cXprIensPfgR_gAyu8Ntfh1jqi4_BY9YL_lVFOGQOgvG7MQ7XVBgRQb5nv3Ylyr7f-LqMHflswIr2CdV6XNrxM_Mv9IOW8U-lVj0i4DY1O3zOBlE_FfEN0ruFt4rehMTUVGS2VsupRrhIKaQxun4SAn6JqVSoyd5d2qzPxaK4t5xugwaMgCLZQR48daSqcy5ucagNw2BUgibhHLI9G1pSsjP81eewIkgCViBtMX4fx76PSEoXN_37zW-TOvAOO7JhtdC_u9G4MyQGyHzdHTwp_IGZmyt00ICXUVLzGPtIIlPkSuRn1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101922" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101921">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=YcXJFDANFzkgnf5v2BZhA1Kh004xQN4LRhoG1ZcfgYsiMlaDnAyh45O7gZSeyybsTefQiGuAssL9iMgUCSds6B_v8mcB0ZEbWVoE6diQF6QwuGbd2jN3zgztGqwWfY-7Td7-b7Ga6OL25nd2StLBv5uT_nsW1VB8pz4JkCQtLryu8PHq_sAjPNWY7s1KEl4HULdOlSFR24o30XE5FfecdzCPFRMuvEo8-WQmDGSniVAi8SOR0-rYu_hEGzG3rDt2OlcQQpkUvuDN8kzZxip9ZQtufpd27H4rcL2hkXQj-84gUhNbOiTyZjDYasZQ7t5T1YRZ6LK6xp4aj8mecQiLPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=YcXJFDANFzkgnf5v2BZhA1Kh004xQN4LRhoG1ZcfgYsiMlaDnAyh45O7gZSeyybsTefQiGuAssL9iMgUCSds6B_v8mcB0ZEbWVoE6diQF6QwuGbd2jN3zgztGqwWfY-7Td7-b7Ga6OL25nd2StLBv5uT_nsW1VB8pz4JkCQtLryu8PHq_sAjPNWY7s1KEl4HULdOlSFR24o30XE5FfecdzCPFRMuvEo8-WQmDGSniVAi8SOR0-rYu_hEGzG3rDt2OlcQQpkUvuDN8kzZxip9ZQtufpd27H4rcL2hkXQj-84gUhNbOiTyZjDYasZQ7t5T1YRZ6LK6xp4aj8mecQiLPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
تو شیراز یه ایونت ورزشی برگزار کرده بودن که چهارتا کم عقل سر دختر دعواشون میشه و طوری همو میزننن که کم مونده بود بمیرن‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101921" target="_blank">📅 20:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101919">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQFa9wLOkfs8wq37dKxNmF_Aien_ak2jNQi4c5_e8zAgZAl__-fd8njjLwbdfMNqcoQyF8C3wylx9KlwvlrVUmnq3kotrV_Y0ljtQbAvJqFEd2tFujm058JkpKKWoKPR6UL3NL33xHjxFlK9lfajFtUGfolqTXIZ1xIyfrEBd5xceP3d6V9Ghp4uNs0Q4hnGSRQNH7mc8UjUItifTNLb7mJlTmduCtjMoLGjBVX8Za-ma6YO4tZRJsM0L89HBlLoG6nzNgXhvYKsoH62WyPDkEvJIWP_rt5APeTsh6emvBQm_xFNZTfxNsjc7XflWkGQFs6gdYEYzzUmqlJwQCklYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qtRbzXatvo2OPzA4glSFxv94xppIfqWIKZZH7apQG8R_2UnTXhilv5zKQ_SjvsYqh2R73nwGt-D_ErYMscsEwFeN8oxsAwGYn2OCdiNWzMOA82X0HWac0wVMCrNvNAaLpgJ1MP29p5JVPYcXBFcyZT-OK67Ot12-OS3sTQMk376tvPn3piWNq_Fw8wKwTkH3rjWrHhZ-cel6vdpMKB3nJBFRB209JEqjdQSf7CM_XnKJMJgBylMOxIr6Qcig50kjiKTEg-dMjcS8ayLpGooMkGxSNs0A8o_pin6bVnqNn4Gn8i9QYRneviEYxWtRFd29KMfXSHKbtOsXx0KTFUJSHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101919" target="_blank">📅 20:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101918">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJV-JIZmIHGxBIoWr-PeVjlTnUnHwIF0oe8PVGy5HLtLb2FLQD9qHX1SmyRv90kNG0KXmXGBrL7X1-0Zb2vRbE3V3yk7Hnxozt0jfjCYTefFOkHtxjdHJO_6LOw9Aux1K5LAnQsMEaSX9VCaiqYo82-E6zQMT_YJkfHca92cvPcILakWbWuuIOoWr-cjucYsg24uIUpH22vd9BIMpMccivPW1wCAF-yPhUvzhFbgrkf_6p5hjEIwo_pvfAANAlFiJDS5DUsvgPrW00nn-IipVumFBVvIK7g_rKluXrN3kwW1rBnJHUy9uy_zbH1fHhTP7LAZV_BbZlwAqsrOu9tBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اسکای اسپورت:
هری کین بلافاصله پس از پایان تعطیلات تابستانی خود مذاکرات را برای تمدید قرارداد با بایرن مونیخ آغاز خواهد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101918" target="_blank">📅 19:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101917">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/779a683584.mp4?token=CbI_mvJRxmAxTrnMkWaGWNBAk9m0PI11Cx4UlUBshLJJPmzO7Qy0jvcFwD2BX4Pd9yjyjXox3czy7Xms-4m73J4WnXzrjmD6Qs0oOQ1lQzBySMB5wwy_-lHs5cxIjQ15-ZX8aPqY5FACOmixokYZW-s8ri6bscFbHMDLRlEqv-46PQ9imGo5VEHeVXpBEich1c_fHDGwd7DpLyOpHsrFYW4__D2ykcW8q3cifJzm_48RnUs7FXK6FbiTYNuerpbY03Q77n0JvBtsC5CAcvCHVadDk1FV7nG5hJwEmcU_rrmwn0gJqtet-f45AZY1fUr8hrWptFGO29kThloCTW3bjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/779a683584.mp4?token=CbI_mvJRxmAxTrnMkWaGWNBAk9m0PI11Cx4UlUBshLJJPmzO7Qy0jvcFwD2BX4Pd9yjyjXox3czy7Xms-4m73J4WnXzrjmD6Qs0oOQ1lQzBySMB5wwy_-lHs5cxIjQ15-ZX8aPqY5FACOmixokYZW-s8ri6bscFbHMDLRlEqv-46PQ9imGo5VEHeVXpBEich1c_fHDGwd7DpLyOpHsrFYW4__D2ykcW8q3cifJzm_48RnUs7FXK6FbiTYNuerpbY03Q77n0JvBtsC5CAcvCHVadDk1FV7nG5hJwEmcU_rrmwn0gJqtet-f45AZY1fUr8hrWptFGO29kThloCTW3bjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3ffe3c02.mp4?token=BdNGc_UBPvUPO-98ocSUZ-6BEihpCaxdWJHFDhd_x7pYMdteLCfbseJHwkKau_Js_DlLbXB19JMestqtD2N8Yp1ZutuegTcYF_NPUHXn4HLGzmjqJmOnYE3L-eSBOF1GP14HMx9FIova-ZVuLJbFvtG0KwXk9xFTzxRr9_HmNjoO4mSAAPcJzOmsObRYWRyq5n5Sqa-32IVnljWDZJeIJnJp41s_GGuEpPpK_YIkhW66rxK2ZT6EJFdEmr8Zjxj2j3M6CE3ATt2mwP_a0dQPCa97IUwjLarT6ZogHKPWuw566rPCgJLZM87kUD8UD1FuDoBhQmemOZgAXNscScQhdFae-LXRbNbb0aGpcr93-yzgW32tq562O-3BFlat0nEnlQCwtMGozf3yaja7z_oKntqtdhir__uWQQk1-Wwm16L3hZcc-fDCqxo89kLN0igDazNmldYmN5FyDcpIFKw9RoBKfmVcX0fMZV4YLDBkCZ4KzQsRM7A0p2AyeOviWdQFcuelcchRlJYFvYOXLYrNjMW2jKSHROubGU7-Ugsg3eswM_gkoRGduV7nPh7iixlbII18Fe5I24gdDsTSi_AGvyQ011xyCkmALlxcv2-Lb5HZjFJztFpsQzKcSa_XP1LQYpLh862bu7EclPJ9foPcnWNB1VcbSdCqQ9rjg6wnsuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3ffe3c02.mp4?token=BdNGc_UBPvUPO-98ocSUZ-6BEihpCaxdWJHFDhd_x7pYMdteLCfbseJHwkKau_Js_DlLbXB19JMestqtD2N8Yp1ZutuegTcYF_NPUHXn4HLGzmjqJmOnYE3L-eSBOF1GP14HMx9FIova-ZVuLJbFvtG0KwXk9xFTzxRr9_HmNjoO4mSAAPcJzOmsObRYWRyq5n5Sqa-32IVnljWDZJeIJnJp41s_GGuEpPpK_YIkhW66rxK2ZT6EJFdEmr8Zjxj2j3M6CE3ATt2mwP_a0dQPCa97IUwjLarT6ZogHKPWuw566rPCgJLZM87kUD8UD1FuDoBhQmemOZgAXNscScQhdFae-LXRbNbb0aGpcr93-yzgW32tq562O-3BFlat0nEnlQCwtMGozf3yaja7z_oKntqtdhir__uWQQk1-Wwm16L3hZcc-fDCqxo89kLN0igDazNmldYmN5FyDcpIFKw9RoBKfmVcX0fMZV4YLDBkCZ4KzQsRM7A0p2AyeOviWdQFcuelcchRlJYFvYOXLYrNjMW2jKSHROubGU7-Ugsg3eswM_gkoRGduV7nPh7iixlbII18Fe5I24gdDsTSi_AGvyQ011xyCkmALlxcv2-Lb5HZjFJztFpsQzKcSa_XP1LQYpLh862bu7EclPJ9foPcnWNB1VcbSdCqQ9rjg6wnsuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یکی از مصاحبه‌های چندوقت پیش کریستیانو رونالدو که اون گفت او قصد نداره یک‌ روزی مربی بشه و بیشتر به مالکیت یک باشگاه فکر میکنه. او همچنین درباره اهمیت مراقبت از ستاره‌های جوانی مثل جود بلینگام و لامین یامال صحبت کرد و گفت باشگاه‌ها باید به رشد و آینده این بازیکنان توجه ویژه‌ای داشته باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101916" target="_blank">📅 19:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101914">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcbjdpSgsPoYmnla5oXQblR1bS-5ixyHqeerr3yYbl3QAxxuO97yRl94Jdmwpvomo6HJNYHDaUvGqdvKs6J7O0LvsVtYpAiG-FMn6u5hbQAF6YRM5ihKKudQbxtT6PLyKw9euoQU86jJoPqslpXdu1Vt_CY02BxSBNoDpzyQUFU8cpg7TjyNGeMu_Aw7S_s13FTFQNBSjEzeYVt-ESQ3dA0VQlB-PqRi3UtDPhTeJATIFoHNvsLDx7aFLBnlpKzDWYAI_wx4Bc4Fo5fRVZcD2lkUVeVr1feetDp2rxhLaoM2gD95z6Wuja94sZ2ymqXX4FZog-eToMo0wJv_jvDyvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9c742e9e0.mp4?token=tAXEqv4tlCxbBMVesUC6acR0D0GeSN8PzA9KiuzMPeFw9ShK6trZM6DqL-DQz8kHoAE3O4jQnFIqTCN26JfyhlltEUV7M9ABd8yFak7Bc0RVsJPmOQAjWfwg2UPmuE5ealkLpbCAGsl5geQC-ZBmjOiVKeNrsUZiqORNuO5P6oww70z8DpjKIw2vCGh8gOYrm5DiVy96qqMAkjN6JYI3MLX9lwmRRwWNRzPtJGMQ10Db-bYzMAS4NdDr_Mhi_iw3FOBkZWrLGX0KQQXGMT3W5wPdQPzOcgN2WKkLAYfTbQRZiOb6q1P5Sn50tJ1sHVt9FxYqHrCHoDZwmW3iqIKpOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9c742e9e0.mp4?token=tAXEqv4tlCxbBMVesUC6acR0D0GeSN8PzA9KiuzMPeFw9ShK6trZM6DqL-DQz8kHoAE3O4jQnFIqTCN26JfyhlltEUV7M9ABd8yFak7Bc0RVsJPmOQAjWfwg2UPmuE5ealkLpbCAGsl5geQC-ZBmjOiVKeNrsUZiqORNuO5P6oww70z8DpjKIw2vCGh8gOYrm5DiVy96qqMAkjN6JYI3MLX9lwmRRwWNRzPtJGMQ10Db-bYzMAS4NdDr_Mhi_iw3FOBkZWrLGX0KQQXGMT3W5wPdQPzOcgN2WKkLAYfTbQRZiOb6q1P5Sn50tJ1sHVt9FxYqHrCHoDZwmW3iqIKpOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
طبق گزارش‌ها، لائورا ایگلسیاس، دوست‌دختر رودریگو دی‌پائول، گفته او حتی ۱۰ درصد توجهی که به لیونل مسی دارد را به او نمیدهد. او مدعی شده بعد از شکست در فینال جام جهانی، دی‌پائول دیگر حتی کنار او نخوابیده و رابطه‌شان به جایی رسیده که به فکر پایان دادن به آن است. گفته می‌شود او معتقد است دیگر بازگشتی در کار نخواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101914" target="_blank">📅 19:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101913">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3ctxdWJPqLed0mZZv9hn4WsBovVrWnS7HrxvP7WBwXOjbq_w2G4nigpa9zt5BTKLEt8Ug3meEFaWj3Z_5hC4MTMSBPsNbRx1DXeS6MR2kRIL2nOPbVVN_s0M5-ylsdJ7fC8N4STGxnArl-VajM3A6YFMZMyRgvF8bIf5Bk6SXuSPwdCwSBbdS_JoGpVUb3-C916R5Da-R3tarj8viskYgiFTQnvgy4LHiyqwOxraiZpoT4ogN1icam71BJ2LIusSnzgwGk_s80RNYUZOKAp34VHfkCGR9eaoybUtQzTtZ1fgk02JLYKBYs_nQTRNH9zW5phb8OEE1T9JLg_xWMqsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
تلگراف: ژوزه مورینیو با انتقال وینیسیوس جونیور به آرسنال در این تابستون مخالفه.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101913" target="_blank">📅 18:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101911">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fpwn12_upR-tCBzEmVQkr7E-MOPL6rNPcrra3sm5lSDr9SKBMGEh6EgPjb6d0UhspOa2U3kv3yoCLoOdr2M691JgFqwCAauhYuZp4gyUYfXF1RSPM-UqijOqQu6_OoXkEzUtDcpI0lcJCuuBvGoyegZRwJ_7m8vc8Ra6-fBfSMiYm_nV0Jnrry8q7KDmH3YgPamctfEOU-My368T1KeJo30ycQqO03MBuwJOC7j7koEsUGhpLYiyHAaEs0e-xvC092XLVsXMqpqHnFL-ZxV4KLCTIuc1ojca-74-Fb-Vq-TbJxDhN7U0_64rDCV9rDnGvjGQ_57rDoYieiij5rIJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lWWQTBttMsKfgT2WJQlsSTwoi3ZOfVoxIeomOmfeipMlpReduz9d6jLjBySMk5EwQAxrM2RZweOaduB3ohoIEkpbHwPMTQeck9pSUnqbPAaO6sy3N0Lgr6lvQvanCLxTJnVnsLewc_aGbuzO79xiL5iyE6mVo_O93TbfO4h-eK3T9D2jYV8H77wTdhh4UDR0klRxDtZe-tK9sFoi5u3OCRi5ZW-U5T4miOQ0kG-kp9lDItO_dDoqZ6HSujgYQMrAPXyX7kwO4teDvu-oGO6tcpjSsXk2TIVodFGjE7PD63Xmpw-OWVfqZmerqCHVSc0Mt_jAgwF5xa3ptFeEgfN0Iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
رامون آلوارز:
اگر انتقال رودری و دیومانده نهایی شود، رئال مادرید ۲۶ بازیکن در فهرست خود خواهد داشت. در این صورت، باشگاه مجبور خواهد شد حداقل یک بازیکن را از فهرست خود حذف کند تا با محدودیت تعداد بازیکنان مطابقت داشته باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101911" target="_blank">📅 18:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101910">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7oOozMXh-75NxNJubgF5XjlHZdJ5UZcqJb8JfVRzgXyhmc88owgp1fpA6G3x9D_yo7XCR74vnaK8m4QQNE5jE7ZwB3wQMLDBGiSULePeCB-uYrL4OFQBGHiPp4wOtTMy13VwSJtCtEmDh-59mB4VF6GkjW8DtPTogyrd1K-bqhLJeSR-rT1mmqJhpuDzn7y4jQ34gEc29qmbixzuq9-60WD27IJ-X_o2DEz3UXJ3JYzfAqu2Ndo2p2qJfXb7ipsSfgLY2Y3wlNplzpG7-hmXt3bRz5V8NHwAXKhMnuFsqz-Nj22vWO_QO5BYzw_MLhjgvMkwjctZWkdou4bf1fNLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101910" target="_blank">📅 18:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101907">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jhVdTlJPigbv5O4zsCaqFTkyyGpFxutRGC19ScbMt0HaNEhtCqhEjxxPgtXR_QYLtMACrCSDwHSuS9y7q6EycY9TlMa9NXAIp_QmGJAPsynEPrWHw2n2WH9dpdPXYKQVqIkm7OlLfvlo3f4FZ4gSnLzhq0X3ocafxdEmWmDibhbgMxS_oKlUqP3TSs0Bzsh1G5Xg0UNO4xDY2pk-CRGST6hkjOmR3dEeN1CRE42a4zH3TWghrNKgYCqLaH80z95uKIQ8kiC7YJUZQDzKgYLgxQ27qBkobUS0cLzEPBybPZkfP3GBGgyGWTB8wdzmGNsr9UnR34P5ORVlXV4I5zmIzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQzFeuRNkJuX9KJyuKPHr60OZJPciS1HtlcTlTKseZUrwCTlYws-TODWuHXH0d_fgCoKq1D02LTWR18icm1ZiKJDelsQvkeHC_M4GaSwGgFj1yW-jK1qO1CKKGEEAWFDe449ASt0qafCw34jmhwpF8aACm-4Ag0Xx6jtE6vExJqbpTqRpVTAdCM_pbDjkbKoTSL4LSek0BDfw4JlP5NsG39jdMPRHVxE1o8xDN4dYp6PHaKix4KXPl1UFV_B5id3SAXjieJeEp4dIY5scJduLtKgqSiAzBRSIhoPLS-TFOFRbnJIoF9dCUEP-FLc3xR9PdBTGHHyJsHkbZUMAasjBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d05827d11.mp4?token=EiGWyk4wQFV1jIAxK7Os9y5lPQxro_luGZHRFDb6QqXuqlsLsSKE6ALi8rqsERcgW2v7zG1EqVXgiBm_Xsl5wtXlOS1iiWGMOmF9OPe_Iz9PhJwwMfk05zwO4kUEwxBUxtjCievpO6Eh6SQ1CGxIg01nXEL5bu1jidUb7u-yEpnw55hbpSaledSgw00R4bRYp53Bj4tWDUhl8iB2T35-zEmBa5rpvVn7HhN5aoWUP9P7eSf32yUS8KxNNbfDNY2v49gq8D-M131P9wcnzOO6Ftud_GnBmhSrdYJwDU47baYjwHQmHCq-kuuCG-n5nwGJI0lyJCa1P0QYl_CV5RstiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d05827d11.mp4?token=EiGWyk4wQFV1jIAxK7Os9y5lPQxro_luGZHRFDb6QqXuqlsLsSKE6ALi8rqsERcgW2v7zG1EqVXgiBm_Xsl5wtXlOS1iiWGMOmF9OPe_Iz9PhJwwMfk05zwO4kUEwxBUxtjCievpO6Eh6SQ1CGxIg01nXEL5bu1jidUb7u-yEpnw55hbpSaledSgw00R4bRYp53Bj4tWDUhl8iB2T35-zEmBa5rpvVn7HhN5aoWUP9P7eSf32yUS8KxNNbfDNY2v49gq8D-M131P9wcnzOO6Ftud_GnBmhSrdYJwDU47baYjwHQmHCq-kuuCG-n5nwGJI0lyJCa1P0QYl_CV5RstiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
رودری درباره جنجال‌های جوایز فردی‌اش:
فهمیدم مهم نیست چه چیزی به دست بیارم، همیشه یه عده هستن که میگن بازیکن دیگه‌ای شایسته‌تر بوده. وقتی توپ طلا رو بردم گفتن وینیسیوس باید می‌برد، حالا که توپ طلای جام جهانی رو گرفتم میگن باید به مسی می‌رسید. این بخشی از فوتباله. به نظرات مردم احترام میذارم؛ مسی و وینیسیوس بازیکنان بزرگی هستن و مقایسه شدن با اون‌ها خودش افتخاره. اما بابت جوایزی که با سال‌ها تلاش، فداکاری و ثبات به دست آوردم عذرخواهی نمیکنم. هیچ‌کس نمیتونه ارزش زحماتی که کشیدم رو زیر سوال ببره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101907" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
