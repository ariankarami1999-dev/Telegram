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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 01:57:18</div>
<hr>

<div class="tg-post" id="msg-102037">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZL6-zjqfe1m7RIDVYmiolp6PzjPyucY0xcTbQvTuJjNOOWuaanCTyTScKZ1J1OpMBXoMulXfGe0z9OLHSO_xzKRXm95YdMyP3a9wbMOSPAUK3OSr2ft-twp8ERkmcCl3zTVXllCcyJtgC9JAF9O7jTVTnxtVHVOaTgEIzQ2_4YixrvhOao2LTfEAEcQzIGO5wIWrROlVOZvBiR3lUIZEqG0KOZmoNuQVOQL_z-PTIiCnfZoSpdFxQZRoj4KzDpi3Od0w-g-vn49o1nhwXjMs1lf3okR5NoP3EjjSXu-hzjteYuKZU2rfCZLCHlioeYzOPxk5K3cDO90Cx-VcA2HHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
جنگ بین خبرنگاران مطرح فوتبال اروپا بالا گرفته به طوری که دیوید اورنشتین گفته پیشنهاد رئال‌مادرید هنوز مورد موافقت لایپزیگ قرار نگرفته و نیاز به زمان داره و به نوعی گفته رومانو فعلا زر مفت زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/Futball180TV/102037" target="_blank">📅 01:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102036">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/frQ_pnVqbi2FJYon_dYsXMEhASOhR2pKWD-9-KBNFxJmqDj8w_hBHpjrtdDPYtvxbXTRRxmmbBn4AeubpX7h1u59eCGOMxSZy1U4K8wEOcJEVzR3CCTLa8nfquT5Oas85X87rTUfocB-yS53FKy3WU_7_7BlkuEJI7ej9cEDUgrliRyVSDqXfkGV_ZiF-pZ_hjtjwe3VNWjzen5jB22n2Ypb5nMf3DJH3QyQuf_D-xzsbAZV5D90QoXLIQM897o5M_vpNcOc-GMSgWnTcsdwpdJ9yRWUM7lgSdmg0AxT4ztThP0arYZY0Hy3pQmZCfKWjALfN-z3zRF5n3Nt89D6Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو والنتین خبرنگار فوتبال اروپا: ژوزه مورینیو به کاماوینگا گفته که فرصت بازی زیادی در فصل‌آینده نداره و بهتره به فکر تیم دیگه‌ای باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/Futball180TV/102036" target="_blank">📅 01:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102035">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNjiOmWmadARLrE-reDA1udY3A0Y7EYxLnf271ANuu9ScwQ2pPSFJ-weLmRGES_L9E04_Fw0EfXLUOaWYzOCEGCPQqInSp1oHfl5WJi8yyFywWBh4Gw4DWhNX6jG6mjPI_cDt2yI5MEYY0XJCoKmIYaZ_KfxSh4UDmALIqEANGD4qBblJAPZmElyCcqfLeozypZqTLoj2obOm2fqGDUNBRnIDo0ENvyIFZ4dW017jLu6U9koToLV-r9A3V5r7VxE-X2LLa_OEuIuhsRo14vT24XlvXUQeZVlkIuP8ccU939eeGY1jnvk-xr5W46jd3rtBvCljfuUCjj2TLpb3esqsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/Futball180TV/102035" target="_blank">📅 01:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102034">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1wfxSpDixJNz0fbYTrnmQjgqieMonMXvEG18_i_Gwrtd0el2SGREgA8r3kj3LxnDhB4WIANch1vTSisVs1i8V3e5FLcxBJV4f5Q1oNH2NgvG0XCbEjUvLBMMYU1eCvSM12yYpK243vyGbX_Tc57_zLYBjCJw5sd5fVPgS1Bj_Dx1NR8U-XXqd_g1-k2gzWL4ZNG1T0lNEKnnqRX5i24YlDefhy502c3oT_sSgngM-8GAooSSAm01U_geD5X9xY3L8tNvLplg9dmXd7-iPIpKZEcalApo15x32rluUWYWOH_VALh-aSr-wH-rF53IavoJyIKP2FS7g5VY5OBenCCPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تلگراف:
مدیرای آرسنال معتقدن وینیسیوس جونیور همون بازیکنیه که میتونن باهاش چمپیونزلیگ بگیرن و هرچی واسش خرج کنن ارزش داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/102034" target="_blank">📅 00:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102033">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/102033" target="_blank">📅 23:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102032">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0SzL98f-p1xRc9J3ivfPtYtQiv53Depu0QX44KBvUb3UcsQUoN_M6s3LqXmssimPK7Mtou9mjDza-LHUHAHEEBHughAvZY0uVWeB1xiaem-wspzuJ3YmsO9W4Gkb_tIO2iYSu9zxvOLFZQ0WkG2ZO4zbhbNy20XvS6QIcX_L_MIq0rqzu5nf8bjNLO6CNvDBuI-6CwFdywjKk5__i5rTaS55dakYgI5s8rSsd82-f9jKY6NwPqp0BU2BR7uuU6AUQmGEyDpopvhNNnpFfzPDgHPnDcEte6yT_4oFHCohSvzcvb1Z6X7Hz4JMXRe5EPoqk-h6coyIOJroCuLKJyX3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📮
🇮🇹
دیس فلوریان پلتنبرگ به رومانو: بعضیا همیشه میخوان اول باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/102032" target="_blank">📅 23:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102031">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUxIlRX8zuSMpcS1Ajlm6MLt3Q9Pl4QgU30JfZBLev4xpHQzTZWdcMg1x429Si6trJTywi_u-gybyO2kgICr6fexMdYVHQItv8JaXJgRp8smcKy1Y1sLj4UA1Uydvr3jMyaQ7_zhT6iXMhx6o_EMttg6Ujug_VH3kKtPqSZso5Zml1ocN965qQ1gIaHEG-tI1JLCHuR94V1ZAsVT9JNCS_QCiGDGaotTW9zYDFgidFhqx0ZhL3UmMwS6sGNniJTeWLYUzbSf0gTJA_5y9Gx3JNd0glPZK8d-3DXNO9VeYbrwQEquO3HcP8MnoA2hlQsucadjuRC3c5vEqICi70xGsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
فلوریان پلتنبرگ اصرار داره که هنوز هیچ توافقی (حتی توافقی اولیه) بین لایپزیگ و رئال مادرید حاصل نشده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/102031" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102030">
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102030" target="_blank">📅 23:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102029">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/102029" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102028">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102028" target="_blank">📅 22:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102027">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xt_XajTURcDUD5hbNel_ZBCYMlP-EwDCo5PRi3h1LGZ3GtIUQs76eHvaHOFfqim5DExA8NidvudbtcgSK-2r5Uz2Ys3i1XAjihA-4vdunSOZm-WtM5bO8ItpMabUim870jPYACMWDzOa441nMN7vs4fNUdSTiwaQDQsSAC1r5Wgwd0rON_CQktnqL3ntYR5zh96Go0Cx_bze5cpU9DufD33szDjIL74Bkr631d2hY2wYZXooIKcmdBz8r-jIjw8QH5k7g3wNcBKR8eqKJFXfAzWJdIR0NzjRfYYtR8ZFOcknfPansDoEAa3i6t9WPBvwinwPs6riNn05RKyNspTtHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار پرز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102027" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102026">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102026" target="_blank">📅 22:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102025">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tofSIsTrqfLcoSC9EJsV_ErDB-Niej7QCFYN197iX-b_UDhbQ_0GaEyHTfGdXmspPhuqfBVSjzXtOAcpQ3tvSgxsHV_9gmSxH4KMbEgc45Y0ORLL961rswsPb7rabGOBhU7Au8O6xiqAo2pJi42ohX8x1JHQToJwuvS0aZVooVZ1kAiQf5Ntd5bkvjXj5xC8f0Y1yZckWu-aeQTkWhTZapCe1m0a68k1kqJXRp3Gfa1RbYWQ9U3_hzaMXVz3_ePiWb7XERiMgI7NP4uEkWv0JCJd7cihRb8QIDKjB0V-DAUCcKF4-_MS0iT0aBt8DDmbp2MyTxJ3jnnXbz8k65_3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
اسپورت: خولیان الوارز گفته میخواد یه قدم دیگه برای پیوستن به بارسا برداره و بزودی انجامش میده . نهایت تا ۱۰ روز اینده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102025" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102024">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102024" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102023">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102022">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_ita4ixEJYZOJq6yoLCs--evlJZ_dMw23E7cT2kcRVbaeC5U2EtQHUlmSIOkE57bbkwvdBn8wtEaOdkuO2C88fSJHN4AsqTQq2MElKTinqm3R5-AQyWXiwH0eEc-D7DkiX8444cB-0qBTW-PVkxE7w43-FOjgE3RNa33oxn0lAgeBib_FWyRvqp7KgFAtrqiE7VIBCNUUUJqYvTmEe0RG6jPH1kiPGr4JM0c2sDZechUq6IZ9locLS8T_TQ4TlMKQJzXAcbyJ2V0_6cEcXCVfQf5ButoCwHRXB44SGisQqvcHOJvFt2igOvtT55pRdZj4iOXaWdzEnDgn8ueVSAnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚪️
عمق اسکواد رئال مادرید برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102022" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102021">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102021" target="_blank">📅 21:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102020">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZD3ijjJ1aTS24mY_Rygmr4WOXMKvks_TS8LiZB1HPwvMrUGGCAIRcE4dK_LydXoB9vqP9JYK0PHYDsBU-FuYI_DVyy06rQVHvkq4EQmeru2oNqjH_jm9fdWfVVKqiFMgGmiQxT7NW0HDrCBwDd7CuoK1jCHGup2wMGjpWlSMuyryOLj4WzhKrybr3oWdz-jXRD4oqH5MWvgizyh5v4JSg58CbLXZRpb-6j6tZj5ZA4wjMRrNKzuU5YLbTWedS9NUeUOtY543W6Dw5YDJrztmpnnEigaO9wFMGUOPhQEM4WRjA-eBFaqq59CTX_r0apZlS5GEPdqwq4Der2bocmcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🚨
پژمان جمشیدی که به تجاوز متهم شده بود، در رای نهایی دادگاه از این اتهام تبرئه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102020" target="_blank">📅 20:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102019">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPw1aOMjox-UMnzZshTqh9WMW_7YcLHigq86U-jGYCeJuwmqGBzEhcB8DmhQhMQJAlOZOyRAJSDg7y-6N-zHA5fwa8hm8UVHZTsPljXGilaqkkDPCdXgAovtxUeu1Br3ZqXJqF35bVBG7OZqp7CFvVIw62JuwkvQPF9MYK9zTEQjNDvFguJ1jtVNkvbNAXu2pUrSQfB37nEaUET-TL9BDGRJeYZNsT9kfV9P3pjeseHQD4Uny-MTEcBGFKrlx5tdbWtGNl4P9CDnzNpym1mKUDLuZT9v2YcZALJV0xX1Il3cSgYidJ0PmmbDSrQO5lncA7f4ZtH32PAvVGTCFF4r1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
آرانچا رودریگز: انتظار میرود که یان دیوماندی این هفته به تمرینات رئال مادرید بپیوندد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102019" target="_blank">📅 20:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102018">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102018" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102016">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102016" target="_blank">📅 19:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102015">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102015" target="_blank">📅 19:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102014">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102014" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102013">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102013" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102012">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102012" target="_blank">📅 19:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102011">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCUjXKE_6QSCWDkO5tZ_u1_scJEimc7zdcjulMuLpXlFqhUvxaxyoNiJfFCZob7uJg7qK4LGYIBCAVmpSa3GwpuHnwhzBVCdnHFVYv6F_A5_uiN5ZOG8VrCscwq-QEX330_UiBPKJanuO8AobDNUlSIkVvPDdxakwGYKBRKzIH4rCvL-4KlFvGDxBhpylUJusIfiXacSjiQuskwOmxJExlZmZI_z3bp1iSTpfU6ZMt0WZ6lRYU4KBWXNMKPmn-eQHaYSR-q7u3AUnDAA-akMQfL1ThJyjGMAJbEfqx44FpWYLecCIRXYD8E9rDg1alqiZFN10zrI-U-Xa6t5F1rgog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102011" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102010">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102010" target="_blank">📅 19:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102009">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIJgcZvLa0gMwKEiZAkvr1tMRnw1Ltcr_u4hwmDGtYL65hCHatdAshi1vS5X4ttHwW4I7nkuPZ2wMR6VDipfn3x-S4F-Ynv3Sp4O3WJbHCclm_7_VFXuCa8AQENUmSOSHqH8IILfBh5bGveaa1E6ItjE1iNhRQo-9M-9k-fKjsqEC7qO0UlPEKn1gihBHdOq7X91s-LJ77QEw68WvWfdjTui3aZw3XVMcz0YIdoIgDC7bKddCXUX_OAxvGoOBdNLlupsQD2Ervj9FScK4eBO2UDJZJId9lxTB1xndfXX5sOvS0gr0L0QGFKbMn-HGV_YDcEu1F83iZPXCTaMvRhCyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
اشرف بن عیاد:
کار تمامه، مدیرای بارسا متوجه شدن که موضع اتلتیکو برای فروش آلوارز تغییر نمیکنه و نمیفروشنش، حالا بارسا منتظر واکنش آلوارزه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102009" target="_blank">📅 18:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102007">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102007" target="_blank">📅 18:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102006">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102006" target="_blank">📅 18:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102005">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102005" target="_blank">📅 17:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102004">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iw6A3W5ftWWNPz0w47eaJqUR05u71KxD8-FJSyOcxOzK-K_uq-aEtica3m_vclMXzJ7USRv5cS-71n27pWdAACFajSDh_8FIHgt0r655zFjZhs1iAlb_NBHKffFfzIE19Zc7N3Smk05vVQ-bszcQSs3qOGf3OcMt3U9NbTSZGHN-epDpYMFJiE0tPU082ygwkGnhdZq7DPIn5eHV431GljCc3AlilyU9cj0MaBJFOfCTx-fjA90z0U_1wHr4jjlU9Jn8NyhkYtvgBUNe105X-Oax273MEC-zWOU94x7j126PYvxKXk7UGwF68KJn_LCkuewcyk9GD7SYLmn2aPmNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
فولام قصد دارد یک پیشنهاد بزرگ به رئال مادرید برای جذب گونزالو گارسیا ارائه دهد. آربلوا می‌خواهد او را به تیم خود بیاورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102004" target="_blank">📅 17:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102003">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmNT9Hn7o_yCZrqnFxvXqhteA92zCHf5r13mndhaBkC_y-xqbuuKVbkrVWSzd4K-ivt2Tl9IvqjxNXJbmpX4C14yrQdxPley-9hp7xZ0Ps0BUy-XkP0Y-gqdguuhtyHSX5vq1LvG4cX13x3pDBcfXnBZGZZ4YGQ-cmP5P4gjmJ1SuF6Le45XUeX2QZXgCfjmj6qYZobw5G3YND4XUFaWONHoWGXeH1cylAiUQCH4uWYJhXZo6kCnzZ9hdFNBiYNm7i1GfQhPtgVxFC5YYQaGASF0ozNwr9ttCj0m6qsRvpApFKBYsk_GzXeptE1uJn7RLMNXXgv_WVdxnYD4jo_WYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی اونا:
باشگاه الریان قطر پیشنهاد خود برای جذب جیدون سانچو ارائه کرد
باشگاه قطری در تلاش است تا وینگر انگلیسی را متقاعد کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102003" target="_blank">📅 17:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102001">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🏅
فوری؛ لینک پخش زنده بازی پرسپولیس و پیرامیدز مصر گذاشته شد
💬
@squadify_ir</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102001" target="_blank">📅 17:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102000">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102000" target="_blank">📅 17:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101999">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101999" target="_blank">📅 16:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101998">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101998" target="_blank">📅 16:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101997">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101997" target="_blank">📅 16:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101996">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101996" target="_blank">📅 15:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101995">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101995" target="_blank">📅 15:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101994">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🔴
فوری از رومانو: لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101994" target="_blank">📅 15:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101993">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZnE2pk8xWfK8kaX1EUhJxXjaFdzzCvaXZhWlo7UrULxUEoPd3XMxlMYXw7DPjqH0yryv1HPIsJY8DTbzJ4eH4VLz8tSZVjIbcFFswFIEW5ngY_44KuS45pz9qkPCPjfiU-V292VaxQL_qqT5yP7WnjONzyJWtqlaH0o_Emtf5Hk-wXGYj__oTVbdq3ufOzBm8r_mFsOvEtSvgsexVmoRFEBi2EW-f-NNIzQqRSwRkV751EQsDG_cZK9aIWD2sY-jI_BQNmxzqxmmEMmV4qoFnRK_Mo8IOiLS-TaHV9-BnqlGWa2PmShTBULP-ruFNiGkBE-dSesgKnLQ3I6k7jLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فوری از رومانو:
لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101993" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101992">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=nOt9HE8_j-dCfA7-t6XFGNN3YqhfReK_0uYWCuGShgrnRSblzaWRlrA0Jb9l_bvyKBJ5i-ssyN14m48gLPjV39O6nCmzW-k5jFcTGGNYFVcR2Zx7qpREGpz-kWE4nh_BdBXpAkdZzhgEzgzrHxcaOg4JwD9fUzLwZ0e4Mew9Ytw1k3nKWKXBbrgVtAGTiizO91b6za0ikzTkL00NRrlJftHn6DsrCt3DaPhfJP6ZDUfSrAjYQ5Oi-KFScQ-X4sb7HZjIMuRE8PxXOhlDKpGkw1XzgCN7C0v2IUJ3UdG-RFjsdfnA3GRJcZMAUUV4mGi5-W7agGLV9RMuyU_LhDjs57aPEVqATYOzz0rFZm4eQV7Viw9fNA8rBCPou3bfTpYDlJu8OaKACQ_O8eUKiY4ptik_Glq2ZcwloTPcDIGJ-cgvimUZDXAarKb3664XR3u5UX2__eeBEFMLwcdTEHM6lYi8JB_tBw0FpC7tBDnefcCGQQ6rX47V1m4e0Ybkk-irXzKzorB76Zk7h4p-R7F3j8T8JMPbC6dmfOMhXVMnQYXE5PO9tAVJWpBgbQkkBSeqDdbaaWa2CpN10NJNOfskIb7ayW5_DPxgyKAypxcsreI0EHeXbsG9G6eG8It2Lg28-xH-MTbQFJye3Wv6buSHGhuBkJ2R064u_qnPUPkP0ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=nOt9HE8_j-dCfA7-t6XFGNN3YqhfReK_0uYWCuGShgrnRSblzaWRlrA0Jb9l_bvyKBJ5i-ssyN14m48gLPjV39O6nCmzW-k5jFcTGGNYFVcR2Zx7qpREGpz-kWE4nh_BdBXpAkdZzhgEzgzrHxcaOg4JwD9fUzLwZ0e4Mew9Ytw1k3nKWKXBbrgVtAGTiizO91b6za0ikzTkL00NRrlJftHn6DsrCt3DaPhfJP6ZDUfSrAjYQ5Oi-KFScQ-X4sb7HZjIMuRE8PxXOhlDKpGkw1XzgCN7C0v2IUJ3UdG-RFjsdfnA3GRJcZMAUUV4mGi5-W7agGLV9RMuyU_LhDjs57aPEVqATYOzz0rFZm4eQV7Viw9fNA8rBCPou3bfTpYDlJu8OaKACQ_O8eUKiY4ptik_Glq2ZcwloTPcDIGJ-cgvimUZDXAarKb3664XR3u5UX2__eeBEFMLwcdTEHM6lYi8JB_tBw0FpC7tBDnefcCGQQ6rX47V1m4e0Ybkk-irXzKzorB76Zk7h4p-R7F3j8T8JMPbC6dmfOMhXVMnQYXE5PO9tAVJWpBgbQkkBSeqDdbaaWa2CpN10NJNOfskIb7ayW5_DPxgyKAypxcsreI0EHeXbsG9G6eG8It2Lg28-xH-MTbQFJye3Wv6buSHGhuBkJ2R064u_qnPUPkP0ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظات خنده‌دار از زنده‌یاد اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101992" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101991">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=dhDF_AZjMEkmJBF61Sl4a2mmCXsIDNSRFoYqWOsqo_MzGAC6jGn4rBeRLfvT-2ko51x96-2-3yamtFk_gR9zZSnz2GRxoQyEnEXuGLZAVB2sKnLeDchdySr6i3dR3eTmZrPlAh6XHOUyp2OctubjF0E0qwmaOvxBcaxNXq2WytJKhTtp3LD6fBbHTNE7tlTFR2B_k5aBzU80t-b_U9CwPgxxIwjlfzpGL58BGdHWhEmqDH4hnO0tDAYBT7B_3M-PhcLgXqn_wzpRxmb-vj6UjQfaHUDV8dzPRbZLqoe9ESjlf1wcOGuoRt42-5wtZmX_9now__7uFkiNMCO10pu0fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=dhDF_AZjMEkmJBF61Sl4a2mmCXsIDNSRFoYqWOsqo_MzGAC6jGn4rBeRLfvT-2ko51x96-2-3yamtFk_gR9zZSnz2GRxoQyEnEXuGLZAVB2sKnLeDchdySr6i3dR3eTmZrPlAh6XHOUyp2OctubjF0E0qwmaOvxBcaxNXq2WytJKhTtp3LD6fBbHTNE7tlTFR2B_k5aBzU80t-b_U9CwPgxxIwjlfzpGL58BGdHWhEmqDH4hnO0tDAYBT7B_3M-PhcLgXqn_wzpRxmb-vj6UjQfaHUDV8dzPRbZLqoe9ESjlf1wcOGuoRt42-5wtZmX_9now__7uFkiNMCO10pu0fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
دستاورد دیگه تیم‌ملی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101991" target="_blank">📅 14:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101989">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BYPsTzv9pUspq4uDdlX-E8GxCDbzLGA8mwUHQLnQ1XsjKSNaReAJoGA3luUtY3d2Q87j7C5qgJARBLnC1ikBka9MEVtr4bcedTI-ckmquimZuBDJIFNQM-jnDSqdT0QqqIaHjVtR30GYcxK5zEoqfkbOZmrc3FM1Jo59dMg7y8CKJIeDOR_n6LTwWi4P20FyB18MP2DciTlRh1YRDAY-pUsErWYFt85unPQvPmO32LJ_zHB8Lp-2LQ7DrRk8UicUluOc_4qzTiopys2QQGrb3eZaFRujIbheQgpF1DiAXTccVFSDrUCYbG_PyynYpKEPereQLAiarHWJaaObAnLE1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGA_jezv4vipmckUzCKPoZPRMIlaggerESym9tsewcirkp-pxL4-YIkkcD2aFl2vNDFniF_owAa9IjRMXSr6NTQlDc5T2tXc7-9tDTcn6cmoy3QRnWBUmsVJ1fKnCjUsm7xUIY5rBboN6UFhoLrRT5FUD3QjnGb7rvBRHwU2zg5A6_njwO0vWdX7QQ-ut9-TMMKGNOmWvIW5hyRXF_pxRpmNz6PWaV5k-j94i382AKiHq4N8Le9JdHPe728ZC4MgGISEMSJKYlN46-nxXTy_oka208JhUzitHbGoiJAJY1nukIcEAOn1h6j8SMWp7ne8-KUdW61kfc2wixO_VfpUBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اینس گارسیا، دوست‌دختر جدید لامین یامال به این موضوع که گفته میشد باعث جدایی او و نیکی نیکول شده، واکنش نشون داد:
من به کسی آسیب نمیزنم، چیزی رو از دست کسی نگرفته‌ام؛ فقط دارم زندگی خودمو میکنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101989" target="_blank">📅 14:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101988">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=Vk-TURdFlcyT6xBa2KWea3FS61zN46UnqoWUCjsHGcxklx605MfFOe3gYUDmYUofdMM6iUnwMRGpTWHhofNrR-Jq4wgmJDgqQO3NeMVMS_XGTiCfWJpwoL83mLulZc9tt1kIY9JP47DR7jUEVo7NTJnrgYu2WeBBfcJnHVUclXoJLTi7g5yqrUW8YJNEjsTOtBUqt6LwjrnVJadICO58TQTe8ty533ZAWlrSZsl3d4Y5wX5AgiEbL_brkKW9hrz8JOlD0Um6hrxI4FGRUHR9NTRP1Dj7L2rXDJNeaJEyB1R9urO3C2e6a7Kcl7ZPiCu0Ik9wfTzZcowdfsmn_YFs_iXSsh34EhL1tXbBhbrnNurC-HYKYisSHp74gWZrx61ownx1q2iuFkA6bCmyFhpZLVtG8WwzUOUEK2pJybQckNuWvFpLnXCQDjsiaEvOYGnwdKXfEzdVpBW4myys7n9zWGiQI9B8BMO4M-xY5OoqCV7f-PGiuVbfmpZNdGSd2M-GHjGKtVE0irvpJcwUPhWnVFNiUypShy5rRvjll7K3hAelVL5HB5PcOK2VVrZH7w4fdaQqgUGztM8HdILr19mkGKpXIT37M7M1IuciDzD0nO2unX8tPy4R_VTLuFMUDu0mHLs_RG7s1dZXqNYpkNUe9J3ipcNVv98nmMahuLJmkUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=Vk-TURdFlcyT6xBa2KWea3FS61zN46UnqoWUCjsHGcxklx605MfFOe3gYUDmYUofdMM6iUnwMRGpTWHhofNrR-Jq4wgmJDgqQO3NeMVMS_XGTiCfWJpwoL83mLulZc9tt1kIY9JP47DR7jUEVo7NTJnrgYu2WeBBfcJnHVUclXoJLTi7g5yqrUW8YJNEjsTOtBUqt6LwjrnVJadICO58TQTe8ty533ZAWlrSZsl3d4Y5wX5AgiEbL_brkKW9hrz8JOlD0Um6hrxI4FGRUHR9NTRP1Dj7L2rXDJNeaJEyB1R9urO3C2e6a7Kcl7ZPiCu0Ik9wfTzZcowdfsmn_YFs_iXSsh34EhL1tXbBhbrnNurC-HYKYisSHp74gWZrx61ownx1q2iuFkA6bCmyFhpZLVtG8WwzUOUEK2pJybQckNuWvFpLnXCQDjsiaEvOYGnwdKXfEzdVpBW4myys7n9zWGiQI9B8BMO4M-xY5OoqCV7f-PGiuVbfmpZNdGSd2M-GHjGKtVE0irvpJcwUPhWnVFNiUypShy5rRvjll7K3hAelVL5HB5PcOK2VVrZH7w4fdaQqgUGztM8HdILr19mkGKpXIT37M7M1IuciDzD0nO2unX8tPy4R_VTLuFMUDu0mHLs_RG7s1dZXqNYpkNUe9J3ipcNVv98nmMahuLJmkUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
چنتا سوپرگل نامزد پوشکاش ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101988" target="_blank">📅 14:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101986">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KrHqV0Tg68Un3shsf_WJkWdaM9zgKeJrcGgWQggleuV6pSWHZc4yFHBnSSEIlVAuNawgRCXCRxjb89MkcJhf0qdqdQxDtJ-gLZLNK4E0GISkD-yMmwYgYRxQiwabAPAEOc3kO99VFfa-A76XenDHTfIUGHBf5ZjOtJWAYUXvNrFaSi8ToPOwHMq3uz9fBkprwoGGeM4SQZluWMe03pLWfmsEgJCwsiggBnjYV1gG11W5GznhRnmRJ6JmBEgVu5HgtHHUvaxoUg2F27TpdI8BIZNSbp13Lm_Y1p6MSwUm67urw9ddU5hGJpMkekm466aNl_GFzv1Ytv3F5mgaCfH5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxwVUGi92MftRROd05VyLIuPgGt68TBypncOMKs4DXtoTFIMB7upKD7KfUrpdtisRHmB9J7577LZ1CBpyfKc8glePm3RHCp5F7wu1JGkR08YJx7rHw8MAmrut7q3vcHwnHNpCqIGxPXJlnXvkFSAJ6ysPhlJU_vEnUtM_0sOm4VfehOrXeqmzJ0JLWbqEomNcuAe-JpHl61gwBDvDx3-DftkHvqBX2i0_ABIOr9jw8jfwHM9pk3jz4UEmXltKJGnf5Ewhx-JpimeguXft6VIJesoGd-8jVvCW4uj7AKYcsVFJIYTGV9gJkvRsFEf-Ym2UlkGqGEoUH1PnAD9CawxLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101986" target="_blank">📅 13:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101984">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjzplorUJdOOeL3o-seugnWW1WsTP83233W5YuDO2P43MSRE_n1r_r-0tAou42RE2m0KRLtX4N1HPeGF-vMls6RBP_qETS_nrpJ0lTqbtTdQOlEjYNE086Gbsfs5zzmd_ylaG3MqPIvSR9hXC6xoD7XDf9a4d6QgvRYNb5vqIENEJV3BQzg9gx2QoO5GyoeRgr2CXyToIWy5kWZqG5wFyyiVgCv_qrEUbrBwFQdPPhLqBJRFgfl0eZ6YLhybA5PM8hh2eR0D1a6VnDTRcyPKqkta7wniK1zx-dhqIyzSKZmtWrs3xN8daN_YARHyq7JQYk5M4eTNnKKfjBZTkgGFGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bc7wSSPBA84s58pP7DzXuRP8I3Sz2ZxDT2MHkIJOKZ86iz-w-ehvrGafZkzBnh9blPgNkiP1R7sZl19pslTnm7gJ6HbiqCPtrzWjaGmWYBjpj-HVMZ7utOJhTv40jEv56ha-XRSz6itG_6X7vGrd8CBEOH2cmA2Y8JFpPe87aHqICNd7mTArJN19fRH3ieUAKwdWLjnhQdcQ-9mAMz0GBc1M-WYcX5vuS4FPfrMB0ZftxYbYfbKfP_3kWQkWZuuIIPgNzVsgKwGMMETCf7kW6Yz0YvG989yG4-0COKlE3MKlItIites_USMgxo_ownuK1zmn3OCvzldgXQ5h4d1RKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
جسیکا توگا دوست‌دختر سابق وینیسیوس جونیور:
این فوتبالیست‌های سیاه‌پوست فقط از نژادپرستی شکایت میکنن ولی همیشه با زنان سفیدپوست و بلوند وارد رابطه میشن. اونا هیچ‌وقت با یک زن سیاه‌پوست وارد رابطه نمیشن یا چنین رابطه‌ای رو علنی نمیکنن دلیلش چیه؟ جوابش واضح و مشخصه! خواهشا این سیاه‌پوستا فاز آدمای اخلاق‌مدار رو برندارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101984" target="_blank">📅 13:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101983">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101983" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101982">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAOuHZltIMtVA6DTPkt-8ZD2tRRQoFLiBaKtGCRBLw-_uCZb7OYhaGgTV9Ujprgvm3nWx5XCSLs3crL8Jmbn1GNK3Bz8kpnNz906P6ZK7Is9gekkpsBRfwpx3n5damlz0Eg4BOMYI1PZrV3STx2SkxDpvhAOTwrlofmviVaaVE7lnVbricJG5P1Vn4K-M2fZje2pG7jA5gmabCbaJJ_FVXPNpudeunFqWN2YxMoLvSgfva97DnQdbZ0kTaAWP4IHXEAs9h-6TEvH10-DVYfBmjZ3ITX0-qdRnoImR_24PMzRvpHpSF7sB7J061u8m67kGJO6fmSv4X6JGpAh_HXIwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101982" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101980">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBQM_RB5nafEv0I2pJAPXoOPL8dVxJk1nifr7vTP5G7FaEOVkBsiQpGKu-_JjAKZOawdPGDyUjLTSuFYM8W5ByNIaTSkoWCi4FrXq7tqhZSnA93i7qd8oElu7th3X0gHf1C-6ZTfh7DYcfZWGJ_5dldTl008WhqN5ZSFqeUYnyGRgurKrfnS33e7bnqL0yD7vSlYx2eVeRFxulRsQzUIQ8jhFXAvsrHu85kLluz_K8PI-utsoEoVdHo_bZBS_OeUp8GLUNoUPbT1AI9BsMnRwyrNygBm6iNSVkQVJ4ZVHiKJnNeiyKl-92Zc0u5dF5s-8bEofXWMwWGfw-TugS3eHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNdTpot5dGu1FiNNte5DExtkKbo42g5dYqaJFf4C7Zt_qYgUkPsh-EEvXn4GsKJDQsyXGam6kRznJXereuf5plsLvDYxOXHj4D9fbWiQzPedw6ZiAY1yuW8RB0vewjzFjXrEjenVx9RWCRjq8cb_G5LLh5wDmneP6BVRtl4y9mqCnfVY53Aix2hWpmXncWNa8aMt9Jr7ZusceugIEC4nd-jMqlVrNHbrg_4so6MMvXab3Ju3UDpYmKaKyB5BKiKYhpYv4KK5sB6hQXH4hsOg6EchIE1G1c9bZwfaq9CKU58ECrQi4CqGe0t6lAjJ4rHLMvBBk3E6mFrcAsbua96uOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101980" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101978">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUG93exJbxkA6NRwZ3XPvYYqCWLINxcjO_5WLdTierkpOsl44rIEuA9Ib9qjs1McwiADMLXvf2kyAIoeH34ev4yN0ZNGuce5yiEA10pkZkjicJ95A7Fu84rj0nAlrKZ6qNW0SWbEhtg2qoy-Ge7HNSn75ykBjphN2wcutu-9vv5PQEwNcV5QPVnyYJmmJbXcAbSLsLm-vHmKprSjLKAYlihFVLBgbvTgU3PQ0B79Ray6jcfAAvv1U64Wu6qrS6UQEqe3kIBQK0ZWtefHVZCZQ7AfyKGE3a7mzQePAwmwxlImpjVb4KiUKcDHUmfjLCrjSG4NhtLqkuvG-PJEhBH-Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a7oUcri3Ne8VTg4BiLI8TGzoUDm1zQVVt4b0EB_eCS3NBqxOMgOKYy2i4vG-6JwCutFc94lLVO0vnAT4DhXhYZ7Mykz-OYxt7fXfc9-5wzSaA7CCItT-r5FW30JMbE_XT9Yl8fHEJPvzZqPO3zpetWd-lI25QUv1ZMjflqbhc5JPk4tk7Vy5RR6g4RyOid0nYqxoFcGybo7G2FCI5tJ7xIUh68rFb7Uue0FU1GOenGVE4pN5puu-7u5Hf47oTQFznvDBhbU3W9c9hlCgfH2-VfIVyv5B0HXRnh-PQubsS9JRusiKPX4eFOizJrsHmt-IxG5Ex-ZZbFO1T0KCB4aI-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
الساندرو نستا درباره غیبت ایتالیا در سه جام جهانی متوالی:
باورنکردنیه! پسرم تقریبا ۱۸ سالشه و هیچ‌وقت ندیده ایتالیا توی جام جهانی بازی کنه. وقتی بهش میگم ما واقعا جام جهانی رو بردیم، تقریبا باورش نمیشه. میگه: واقعا؟ برای نسل بچه‌های امروز، دیدن ایتالیا در جام جهانی انگار داستانی از یک دوران خیلی دور و گذشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101978" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101977">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSt2ODt8BCJbSDrp7v3SqIpysdl1tuy85QiGkhRw5DnFjVqtBZQw1TRrVLS0waGyeCFz-XySss2_qrwMPt2GK61pA32M-TunA-QrHj0n_vGEPtlJUW_cGA7GbmJtm9dRJ-o_p97Ot1qMUWXdnpBBmckNogWdpI0bqIPJT9v6h2X40l3APwZBD6UjrwizCueYSZvnbP4KAR1uf2c2jyNSMnm25JehKrra8oX4QPXp7qIYAv04wWCXSfEEn3q2-uDi7xr3mN3YLx7yfHTkxdL4n3DCNjr2GhRQ7PNz8X-b3KHxc0QxHcXPAKIxIHl-Y9tMHE960pkNXq8vYRDNQAc_ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
ترکیب آرسنال اگه همه شایعات نقل و انتقالاتی به واقعیت تبدیل بشن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101977" target="_blank">📅 12:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101976">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKgkDaKvEYeRHrCTmvFXpUUakjUge5VkcxevSTvVoZmvYJTgCb9Bu7Hs2XpN3UKldu5TTYfHRuhM4bjpmVl4hZ_zwpHKmGMm6JHNw8pjmb60iMdQU2WrNkFFgvOuNFHNLmlUceuPxiiOJ6S8bc-8yNDqCGbS_qD51uFRvRPWRLIEIJkVv_qFSw9JbksFDCg5jIgz8h6viISWVgoW-vkt8rz1kbBidI1vY3VE1SAWXwPMaoStR9NnI6yOz68ulG8xTQbJT4s-Q4kQ0UJXHg9G49HVLEGQdK2R6WI4vs92pMaR4smSpwsnqk1Rn0c-fAki2m0M8AQf_g6S8WlxsGKp7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
طبق گزارش‌ها، بدهی‌های النصر عربستان به حدود ۱ میلیارد دلار نزدیک شده و همین موضوع توانایی این باشگاه برای جذب بازیکنان جدید را محدود کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101976" target="_blank">📅 12:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101975">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=v-ENM2Z96ndGVyZEDqlvzV1JXmsJxJRCxYOCjsViHEanoqU8AMJWMvhOv5ZUUfUScJbheR6XrHtuAeNEzU7YpsYFCR8FAUZXESl4MqLeWcOnvp3cj8qKg_C4xxeml_xA9P3TNf8rIdfbRR_QYP8Lp1nGwn39dUnqVfCHEwjHXX9bUjfIw95hz0CIfX5tawbMB-GFeblO0gHt2gF2tqw7lv93wY8GNovKXeOjQnOi8E5FxDzUEAhiDl-GK08tbobIZKxDqv4l5PzXumqveWyPOOqgT2DiGSTLKalInC_x8AC2O7CWS4rpoplWC7yjORwyi_Fs_9ufQXkUDizHpnZ6YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=v-ENM2Z96ndGVyZEDqlvzV1JXmsJxJRCxYOCjsViHEanoqU8AMJWMvhOv5ZUUfUScJbheR6XrHtuAeNEzU7YpsYFCR8FAUZXESl4MqLeWcOnvp3cj8qKg_C4xxeml_xA9P3TNf8rIdfbRR_QYP8Lp1nGwn39dUnqVfCHEwjHXX9bUjfIw95hz0CIfX5tawbMB-GFeblO0gHt2gF2tqw7lv93wY8GNovKXeOjQnOi8E5FxDzUEAhiDl-GK08tbobIZKxDqv4l5PzXumqveWyPOOqgT2DiGSTLKalInC_x8AC2O7CWS4rpoplWC7yjORwyi_Fs_9ufQXkUDizHpnZ6YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خارکسده جزیره برا ایرانه
✔️
خارک و سه‌جزیره برا ایرانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101975" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101974">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2mV_9QhXFdwEIgJfAzZioqbZuKQnR7Toukn0PHXzEEtc2HivFbLh8acj7BMYkpfWMf9Ttuv1tLUxIKGlnw2EmXlP3jEXs8AE27gouimJ-rC0b5v-W3HScL4NGSRumcrG4YVvolKG2YOZ_xNhadMwXCSBHjbki6cC-Ly2rSh7cUUPusLA0HMLNZa5U-QJC86Ui092hAgbCBz7OA5_3jnhKi4UF-C7iTwYLoII7CgJiUXtMvjwkZIOCBT8hNz5Fcbf8nDOt7f38uJPAmtI8cjUv2FHyirlIUsve8LkAhfKkMShJSVZqDIxfsGREFvqfr7vpXcf47QqeJluDPXEZGj-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انزو و خانواده تو تعطیلات
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101974" target="_blank">📅 11:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101973">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101973" target="_blank">📅 11:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101972">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=J3Tnx16D30TRHSblyscFyPEHUn_qtRLIl_h50ZTIQJYZTUoFyGRlyM-5hkuE7s-aF1WL2cQOxneEMSIe-9IzmbbpdeeRTV_zZuEzldDmFcLVNKIDuplZJO3DXMIwwy2E5YDnFBb8RksaJCiJFhWn_cvOhKPzACKHpWmmVGJcfUXRGa7OXkrQKVzbHKfgJyhmKXDMDsbwScZXpr8E9Q2zmxBkO_Bestrd0OTmhHbR8dsrcUg-hf8sU1-K9XOZjGNzzZsAOgcBDHVWnXtSqAy2fs5rJXCPRbJPyvdUFbK61lPGghe4OfeAPK3NJzBfCyJFW-tQELszJRd8YX1kxWDrHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=J3Tnx16D30TRHSblyscFyPEHUn_qtRLIl_h50ZTIQJYZTUoFyGRlyM-5hkuE7s-aF1WL2cQOxneEMSIe-9IzmbbpdeeRTV_zZuEzldDmFcLVNKIDuplZJO3DXMIwwy2E5YDnFBb8RksaJCiJFhWn_cvOhKPzACKHpWmmVGJcfUXRGa7OXkrQKVzbHKfgJyhmKXDMDsbwScZXpr8E9Q2zmxBkO_Bestrd0OTmhHbR8dsrcUg-hf8sU1-K9XOZjGNzzZsAOgcBDHVWnXtSqAy2fs5rJXCPRbJPyvdUFbK61lPGghe4OfeAPK3NJzBfCyJFW-tQELszJRd8YX1kxWDrHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیوزلندیا اینطوری از بازیکنای تاتنهام استقبال کردن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101972" target="_blank">📅 10:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101970">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vK6BYztSxmEvk8vyCGmNLyLuYPP_R1HmVQwISWSURAlENaWgVWAWx-1nAHhJnP2CqRRwGNSXsDA_EcNsgxLkMR0hbVkq05DD3cVntWTbv9nBpnOtYgUlIwKvARPwOYOb4hPG5TyF7-lUBzHwpM_mZ0nihI6vLLfZv7MuNhUiBI8Bkv5hmrHrfllm1enRWYdS4F_oxHLna2hgIXBaocfPFMdvRZAz0mbnejLEpolfx37G9unCtrcjSjX1ZHBDahonlgk3r8GY3Z4Z93XZ7dpKiWv_4NQZ5ixKFgDcRrs5pAe8hD4j7cNQV6okQG6WNcTbEGhGycQ1IkCruFhWlJue8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOGjvGu2-HeAYqz0epZ2oNoDYiugMLGodJA5DPqWQJZGyKx0KJjPb_kFvv6Exz9n_uvCeRM0_AjikataL7Vbw84QuBg8ysfRELJkpTIGiPmk3ED0eknp6xsOVgxQ9-fKSJx7XZ4VcCCfFCgt8fmZib8SsoxCxAK2eWEDSpRQI5C60WuRILbNXqJnSHVfGwKRyYFakdSOE-aImjB54tnwV0MTMg9WTVaqcgQyvaFK_Oxu5mW_oCCk8CzI7qG98Gdnqya8wOQjM5Rxt5MvcTrM7DYhyobRTenLt7aa9MBfnox-c-xWQ5OQx4Bp-sFVaqvq4Ps54rECm1oQ5nND93gvqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پدری داره تعطیلاتش رو اینجوری تو اسنپ چت میگذرونه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101970" target="_blank">📅 10:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101968">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HHKaGrhfDsImCv_txES-ImUTUHn6hvsITafd0-3TbCcymqfgfS4SJCq6711B-AKxWg9rFxw9l04Wn8QvsBuPX394z7FWlUWXcbvDHN19TY3mFGsSBJLpER8PG0GSgkj87G474eo7G1ro6AWzeeIvqSx0ToB37yNKGORDbBDzEEbDhPWkrGMFupnX9UvySuV3AB55wn2W92yjvdrLdjmfsXJZW0EUlOm85sUTboH_-WDr_QmbgHMGe7pOqAkBsNmWt1V-wvFE8iNF7r3BAmrG06vsgs4MGAfBs291Bu-oHZr-JQRIAtgNeYxQi_bvvJKs1YKjvJyXfq1GKfwuw2BwHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s5h-YJlk8kFRTi3dZR9ONgXYlw2OLLs5aXDsHnWn0LP5PKLzbKLd4RQOr5HuLGhTShAmUACbRJHpDmhPTeWXbrMhvWs92UpAPa06exTjphoNNCIsw4O6c_rfQjfe0iKSK1mmcI-a-9PDHB3nB-P9jeegKTn2_imV8mzRsGWXyh63LW_pGbxWFzch5fNOzS4VoCOD_zvxOpTTpb-iMf_Zz2JJ-2d-Hmt35yOO2xf3EWxRYr-hD1HFSk13In8tmLb4meUArwyUUrWEgAL8Gj24zinf42aQ64pwqIYWKiMWMofNHWzYxRyVTdrhlfBESJopN-XM44qCZA0SWKEnQMGX9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
😞
میگن نیکولاس پپه بعد کات کردن با اکسش تیانا ترامپ ( پ.ورن استار ) الانم داره با لانا رودز وارد رابطه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101968" target="_blank">📅 10:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101967">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3EQi_YKrkBl8ZhqutqMMbj2CcfzxpI6n8pmdl0w0yDf5jWHuUzZGSIey6X8pAlP3BVD5dtlu9y83yJXD5N_usC9zmPHIq3oXkAx7ZmNvlCUq8xrktvLRCKLkn3AUeqPV0cX4XpKLetOCbZrwqIYT1SIg_4xfpcdl_Qb6ywckciIfzwiorFtQxmJJ93BNmdVZ14Xy1HUZghPZN-S9-OlPmWfJ--7xEL7UrzwPvCTB9VeusWnkAikpeyBMvmM2wMubQpaTY5buYxelzCrOLWF53gXbhdyU7z7uuCj5sT3KvpU2uF6G9gToR74JMJ_Ipq23nJeDzUte4yVHqrd_h18ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
موندودپورتیوو:
اگر بارسلونا نتواند خولیان آلوارز را جذب کند، دیگر هیچ مهاجم نوکی هم نخواهد خرید. بعد از جذب آنتونی گوردون و کریم آدیمی، مدیران باشگاه احساس نمیکنند نیازی فوری به خرید مهاجم داشته باشند و معتقدند فصل آینده فران تورس، دنی اولمو و رافینیا هم می‌توانند در نوک خط حمله بازی کنند.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101967" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101966">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwLhLA-FMQ13Ai5u5vQvX4aehsponf3ds2eHdTox4BY870ydMEMBvhr_g_L4PEXtdM6EKGtyOqRTKmWqhRMDFOOJ3_9cRWWj6d0o60MmnKOWY85pQN1bhZftquHbvvl_w7QwG0gDXLUEfcB-2xeqaKkYxpz6rNyOQT9LxnoZKKuc4F4F0b8i6IronumB-NLDhyc1omIXQavcIVrqjf78lD81nD2cHZSOj1Z5UTnBAWQCN8pxW76tuokCkMIXk7adjTxlqyTJF9FBPpUg9-Obv1-7EMFI7hWoHCPqRtMpVEltB5N7HQOBGt2bOXog5zYkS3LQJ7ZYRoMyK0RvCof-MA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101966" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101964">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hA-CJpu7-sRnP5xKn6PwNC99sO4oO_c76pM-NopM6qar7l3ORfaZB5x5s23TLniGU178Ixke_4ls56TT9h2TrVRFVG-TFzzebA4uxb4tvPP0ByHQgrsrrcpnllvCo19aY6523sxsd0kiN4D9xPopJwxHvlZCw6binlH64haO4fW_1S15GSyxOqp4YOZgruD7RxWJLLJ9bbWaFRVic5TQu8HiCmTk7qNjSAwS-ZCUEmxT3xGdJCzcidm9xMroj7My75bWLR44SKD_Xag3SvN97pC0Y0djBKaqVUgo8N7123Btmo7yhJg0bbZVAteg3Tc-7Ed7fJxMtZzfaqHkd2nrVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s-nHJg1f2O81eYYtBI8w0G5VSRSa1_aZ19AiwN5iBAwmIhR4yWJVgR_lbb-22kdSjvKO9wtW8pxD7qEpakSf4d4r45VuqhyMi6CLYMylER40g-cmZfmlK9Zus47RSDM8eEy3uxDilkTG-6cERo1iTxjHgqBC4fqj7U9ceHlNBMDsNnl-0OQPZgsmpgH1sd647-PM5UHhRZDc-EXmgHj11lZJ7ZfGrPLpBIexQUCIfQUDYubXVOFZa4jjbHxqGsmndGY_Qc-lqQPa6nOFVns-pKwKL3_qsJJ6xQxbcS3bQ89K0oLtLE3k5TlyLwhVJCewDvskyNUcKWffc58133QqUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سوفیا رین شایعه‌ای مبنی بر اینکه حاضره شبی رو با کیلیان امباپه، آقای گل جام جهانی، بگذرونه رد کرد: من هیچ‌وقت با امباپه شب رو نمی‌گذرونم. هنوز باکره‌ام و خودم رو برای همسر آینده‌ام نگه داشته‌ام!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101964" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101963">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hW5KO4HHlm4B7GnFYUHPyo3IMjSwOYktzPiFr8un4CC6QUq-J8RypCLI0lIY7BRFccMXCRuQ48SAFVu4QzKRFzG7mm3BqhfjM_Tg0W2pTojOQKDGBBXB9y908nJh9UaCVL8PdMZPfiKONfpHd8n6qLvctg0IfDWUwWykpbAebxS_HI4wQ1H4aEatYZlkNUs7r-H5L2oBb8svW8nTfimacPsOUnNzdXnYU1JzO9aCRlbsy4KA13O0eLLIlUsc1iCBApEAc1Er7Zm3J_RUSOxvubOGgMwd3OMxjYzxWjkGWCCfJVKS6arN4xDD2kXt3jcW-sTUuAilrZtnA0vr3cXt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رونالدوی برزیلی درباره کریستیانو رونالدو:
فکر میکنم بازیکن‌های خیلی کمی مثل او از بدنشان مراقبت می‌کنند و این‌قدر اشتیاق پیشرفت دارند. من تمرین میکردم چون مجبور بودم، اما او تمرین میکند چون عاشقش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101963" target="_blank">📅 09:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101962">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=ZljSEjEgJj6LQHm-dZT55X1eoT33Qvat9XWwIv4gEbQY8jXdh71DA0TAzpjFAm0aVEbe16Iu3z6VqfNSab_gygpOSyuIJVyDx3FaAD72qbQtzHJKGHTIPkW2MfFiWXH-KbZzAaJLs8BMai8RtswFq_4WFblejMTQFIiAMcIdZmw7VvF93sQlGRUuv0y5f6d7JwPDVOYY0o7hUB9dbDELuykRJ20wuYACh-16itc-y3TpfLrxH82qggfqeYQxO8f82Q5P6JgrW8TXqunSPGgju7OhtjrUYXebs6xl5n1LlS9c4zEFpK1D045gmkm2VbZitvlEpjrN52zF9ob4bjYNGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=ZljSEjEgJj6LQHm-dZT55X1eoT33Qvat9XWwIv4gEbQY8jXdh71DA0TAzpjFAm0aVEbe16Iu3z6VqfNSab_gygpOSyuIJVyDx3FaAD72qbQtzHJKGHTIPkW2MfFiWXH-KbZzAaJLs8BMai8RtswFq_4WFblejMTQFIiAMcIdZmw7VvF93sQlGRUuv0y5f6d7JwPDVOYY0o7hUB9dbDELuykRJ20wuYACh-16itc-y3TpfLrxH82qggfqeYQxO8f82Q5P6JgrW8TXqunSPGgju7OhtjrUYXebs6xl5n1LlS9c4zEFpK1D045gmkm2VbZitvlEpjrN52zF9ob4bjYNGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚡️
بخشی از گفتگوی جذاب بکهام، زیدان و زلاتان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101962" target="_blank">📅 09:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101960">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LOV0xAk4TMRmkelH85EWZ-oL0mUX7uTU-ynUgcuE7gstfZoDssuwU1YbOOnN3UHR1boEfqvOpuUM7KjplSTIPGX0OeAqbq-TX6u8jFKb63ycGipEwvytolJ8f3r3AAnYkwu17tI44WNBmDzCT-TneWK4_78PwGh4PvQVcjrid04_CslQCwq0dhWd03Vhq5gy2pz3-cC3JO8gO_CkUfYh_4eUHbhIAoNe3xwOoI50cbUnjygiDYD5KruX2QgRb_kTYJsrN5pvdo7Wn3eYkFObPSOPvneIWgLeYfuMmNFSmMP6Z6vx7GWwSKq3WYR0ZGzedr0IJ2yTd36QLLQbbxymJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bkmc7jjPDanTisgffv_YVzZrNuuHFaJCyfHrWMTZV_gnIJu2zDgo2VLVEz9awqdli0yGY76alv6x5aQj2WtwWl_fa5AHwnvKvHSDIe1re_8kv9L4ZvqTsOliNFdQqgqHyk7ME-Ic7qrAJkv6rHUDJIAt4uHlLg3OrCZeSgkBc__2kIFfdID_wjHyWKEc-G1sezDjdl7e_uojVKFvDhYBnqboqhflSIhoTfODcAg_l8aq6hgy2TfBfLKY2hKFAsJou30cbcAXY4AqfMLMfnllfjy41xXxj8HR8zmhsa3w3YRNc3B1XU0V60hB8beD2GKXSp1mnO-0k1XuWrnVaWegRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریستیانو و جورجینا قراره ۱ آگوست با هم ازدواج کنن بالاخره. تبریک به این دو نوگل دیرشکفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101960" target="_blank">📅 07:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101959">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L92RKmgeZU4PKMwihA7yL2qUYjT1YFLU8P6Wf3qvZdMYpJmQxoXLTRk6IRW_an1Wz7vdvONckwjtuVgCipqE2d0pdOWxjA_b74Ek9BskmhtQ3Sy8r81zIQJy53Eup3eV3xzLoy5uvhHT-9BjSyxzbzesb0xjyQGVgba5H1OEYK04QAlLOunwSGJhSyCWR6DKxn41IPgIVHiMtzPxS5nZ7H1p2BprGKCFAwCYBDv6WJdkSXJ2cWhjEvXRhdCKyUlr0UKSrNcuPDHXJem7vFZHS7UZh5GJyw4E1zykZhredwBDtUBZOpnQQxv7iuq6Won0ZfecEZw1BFMs5OE5ZZuHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👑
موندو:
تعجب نکنید ولی احتمالش زیاده که لاپورتا پرونده نقل و انتقالات بارسلونا رو بدون جذب مهاجم ببنده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101959" target="_blank">📅 06:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101958">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=V7EEmvOiTqPR0a2Zh0AmTzCjHOJEUkxTZ350yiz5E7Vw2Ca9j7CekwJPTQ0DyQgBFtaKK9RsyS2Ksgx3wgFH-FFlZqCwHa3RbxtGjy06FmHXp5NFfgCE_NEfQS6r7q1jemNuLU0relcYLDNrIhv68aZCzN4YuxnsVBRY3d3uRn7pLd4zp39olKBcAqDVhwqFddvCSBNXFRe_t5WNuCJ0Bi6FsUvNwNCjdr5AgiRi-14B7HXpfrzedbmuwe8slGV7iLECkPPjRR5PPQCYRZNncdRtPb2g_sImU-lKD8dHiHi-f1SNyGe3WG1rNdOXeb5Vfev7FJYeFk1ZWYaKppncww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=V7EEmvOiTqPR0a2Zh0AmTzCjHOJEUkxTZ350yiz5E7Vw2Ca9j7CekwJPTQ0DyQgBFtaKK9RsyS2Ksgx3wgFH-FFlZqCwHa3RbxtGjy06FmHXp5NFfgCE_NEfQS6r7q1jemNuLU0relcYLDNrIhv68aZCzN4YuxnsVBRY3d3uRn7pLd4zp39olKBcAqDVhwqFddvCSBNXFRe_t5WNuCJ0Bi6FsUvNwNCjdr5AgiRi-14B7HXpfrzedbmuwe8slGV7iLECkPPjRR5PPQCYRZNncdRtPb2g_sImU-lKD8dHiHi-f1SNyGe3WG1rNdOXeb5Vfev7FJYeFk1ZWYaKppncww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101958" target="_blank">📅 06:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101955">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qObZnavmKtWd-8ArwcFDsPd-p86y6nhE7OkImcwMyJWOCwzJ6nPY1IxlUT5izePdwPXgd_keZq9VULWy3xaxV6oy10sHB29PH8PmbmyIiu8X6368igTULykDsl2Y8SJP64_rduR_2MqE0JBKnnB2-EJRo6F_BekH0Oo6u6WAspODLWuuegFN9XfvTJpq9y6iGxibFf4enmPYBWi5cwT1bI1njbz9rwjaknLBvbKEvzi0bRJRX0wiX09YfwSctsI16VCPQ66fqQ1OqCbixfZAmeF8XSr1kwF3r696Y3LCk0fXQ2OpIhoe6I1Sy6777sYXniFC_bbCExRADLl31kYOCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PkNxrMEw4y0FLZzSKU_c8AAxTL1MTbRyIZepaJf25AL9g8-HNMlUiFZtDSlDarSYUwg_YGJpPI4s2h0tfn5G8UeZau0psRTJrwm35R6NKAAjPMUoAQuRyenc_BZcdbHkxHKwozut24EYT63zsZnTRd7--0S02Gj4wjpT52WO4nfOMaFRQAZkRo8zBsk1Z3MY-iN7GqKrn4qT_4YhY9amGYVJLVeeIO91dMQwc14ZWN_eXX96kvKzKrRqISaNoEvChrc2w-479JKIWnL6mwbSQ0VAB8lgfZTGfGp94AWwf_zG7g9tihmEzgTYEPGY20HwG6sVM_QOCpSBd5IJEDGkFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=L4tYPbGiqlF0cBU1J_xXmY_pl813guVt6e94GahAjIEDam9bjxyatnFG-qWRAZn9oZsgpmVSar_6r5F_Y41apR-zfPKZKyKYr5RQrjhzCgEWps4C2BTvmycHK7sVdPzyhux0T8LJ-WgT1e5mSAlKiPyeaF-lifZTVSrkDwpbNsgmnGVscAAQieO7UDaCN946OYmOQubZXifBl3ftbLkoa7rUtDbAenw8d94ZD49FufYbAuQ4lnwlQs9HftMwRrC_yhjEkYsm7YghnMcGo-P6kFR4UF3RuK2kW3UnexqrmQLr0wF-pCWtav8L02Zu3stIRn9hK_af-Nn-Kp_0t_8p1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=L4tYPbGiqlF0cBU1J_xXmY_pl813guVt6e94GahAjIEDam9bjxyatnFG-qWRAZn9oZsgpmVSar_6r5F_Y41apR-zfPKZKyKYr5RQrjhzCgEWps4C2BTvmycHK7sVdPzyhux0T8LJ-WgT1e5mSAlKiPyeaF-lifZTVSrkDwpbNsgmnGVscAAQieO7UDaCN946OYmOQubZXifBl3ftbLkoa7rUtDbAenw8d94ZD49FufYbAuQ4lnwlQs9HftMwRrC_yhjEkYsm7YghnMcGo-P6kFR4UF3RuK2kW3UnexqrmQLr0wF-pCWtav8L02Zu3stIRn9hK_af-Nn-Kp_0t_8p1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101955" target="_blank">📅 06:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101954">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcJc2ZaGIn73mQYPWdD8iNKDUjKs5vfdRkE9wXe7vQ6d_HOvu54aRH9AXPq38lFV5oevaaWLnhqvGoMJMO6dPkjXOAfWDzcrJRcIv-m_fz-oujtvEbq6iHbDKFm1DVfMPkVNsRG7cOC6Zsc8O0zzXcdGatyWJL_vhwgk-Q4dxioG_cgB5nQ3-SF2vDfp4uAoQuNoPLdrEEJJAI6ERQtvAfN9en06myxKAC0ZS04AQfYHznjQGGicSSHWQE6a97D2goumlZfvn0RMoWdI7WHFxfBIKay9azZeuPV5pY6Ncvz3Emcv18inHx8ePCL2vGrpzupVFZLgKyH3cioW7ZKWpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
مسی امروز اینجوری تو روزاریو شکار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/101954" target="_blank">📅 01:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101953">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu326_807Ta1PaSi7qqDXVGk5LKHwZIbYY85tDJSXx4Yly-L7M6fvCMDtpPGygbXJqMzWo3pJvA5A0XSEX4adNu9pryLxNQZdYiYiadNsIgY0uHULYioDNKOr_N0T0oHmlex0a7dm9795v6c4aeOuDkMoukBA5ruR8bLjVipEyOTQhCnacGMFMmJpqMO1tZxJdnc-W7xCzjJGkNYmwQfWP3532JtyHzdH8wmNM1M7rVd-rYygjuC5OY2QxT-pvM-ihQgwYEetHZXT5KmzHRXGSR4wzTH-bB6ZHLWhQTSqQ3Snb1Qcvl-Xy7RldmuurRvU2xLA4qosRqveWpZikiA-m-jY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu326_807Ta1PaSi7qqDXVGk5LKHwZIbYY85tDJSXx4Yly-L7M6fvCMDtpPGygbXJqMzWo3pJvA5A0XSEX4adNu9pryLxNQZdYiYiadNsIgY0uHULYioDNKOr_N0T0oHmlex0a7dm9795v6c4aeOuDkMoukBA5ruR8bLjVipEyOTQhCnacGMFMmJpqMO1tZxJdnc-W7xCzjJGkNYmwQfWP3532JtyHzdH8wmNM1M7rVd-rYygjuC5OY2QxT-pvM-ihQgwYEetHZXT5KmzHRXGSR4wzTH-bB6ZHLWhQTSqQ3Snb1Qcvl-Xy7RldmuurRvU2xLA4qosRqveWpZikiA-m-jY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوکاس هرناندز: «کیلیان، اگه قرار بود یه تتو بزنی، چی انتخاب می‌کردی؟
🔺
کیلیان امباپه:
فکر نمیکنم هیچ‌وقت تتو بزنم. دوست دارم مردم من رو به خاطر کاری که توی زمین انجام دادم به یاد بیارن، نه به خاطر تتوهایی که روی بدنم دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/101953" target="_blank">📅 01:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101952">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYv1zl5WHkyn8Ayu369ttvIL1BiqZ5pD2aUB6UBvyd2GRaV89v3aAIMuXl1YPE34MlZp7IapA1cP6qHGPWg-4-ur1Q-UDtLVXkHh_MRuTkxcZajXLKM4N9bU73izKaqgBohz4KuwxNAjgrzMs-Sw4s9b-v63F2G-lQnmD5IHsABe6wgk7upEFFIefE2UuP2Bcr9_GBeYInJD6G3acRh_r676pyVPUdQkE1dq7M80X7o1W-aofNhi2trdgugL8vlsxzcWZZrNZhiLDQ8c4Mi_qbVQO5PAENwpSeSiZ2BLDR6WWGsUKhKdCVF9u6Ri-P1TgSS8WHwUSiy1PgQY1ShywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
امباپه و پارتنرش بانو اکسپوزیتو‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/101952" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101951">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNZtEvEG67y_r61Eu11l5JXWmhRuEhOeZ60gKO8SuHwqpnGpYPQlNVw2A2pRcXCO0vmNvjHREMsfX3dd3cVWdYvExfvtLE_8fKm0q19T9c_YoTGWx2YpT2sz4fO4IBEbOCQdxWfz3CwC2-1op9fyxaoJPOHjvZj3OFaYzwgUZ8OWPZXo8UrVryyHEvDMFLMP0brXLS71_0dGxRNP3p99UUQEd2N_FkOeQoIuYi2Z5vPTfs6GJePrYdFkc0QXxi-U-p6wz1U70bSt4H11tiSTX8arJkNfIz3x6zFwM3ev9yheeU2TXabAbZzZYlU8f1oochQ-5nbtRpGKtiSz0UWSfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی خوشتیپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/101951" target="_blank">📅 00:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101950">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/101950" target="_blank">📅 00:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101949">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-rttT-rx7qza-lMXoAHZJWDi0Cc47mNPfvMo-LwH-cDxu0f3vrsUh4l-3pjZGjVevgjz7u36e1drwUAUx8ThlAubU_0VI2dOWNigPgeO9Ch6nseG-bbWp4qxJNz00jIyBseHjNW5CxfXKgHmAy9Wq0i5PIOl-dP6hRODYr0S3Rhm_50Ou_LDXVyEYE8kUeaNGDAChVFQNY71ASrvpOQkm-CBj-_xAssW-fzw_62z3cwWOC26p2yCghQqGULoJZMp-7oVnlvgCiyWBbdlIOnHPghxWmb2bH4bz4xHUrAbbTSW2YQzogGo_a0DPfQZMgDZwj53GVdL_XrWKaEAFnhbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/101949" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101948">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1g4yGawof9j3QGozj_aii6t4zsm0ckDey5zCWoItFg3hbohOolYzRVOXwUW_7Xk9Oaq9HbhMehmhwm-ntxf7ZHXRB_WI7cdzKeHcOfuhIClLJ_M18Vew7LN8iKIdCtAt62LrEYSe9f2DU5AsK0EjrLC7sGFfzOi1dkfYSaEK2_Cz8VyfgrGxlR_7jUd2YvqnOvuwd3N-7ikbB5tvlh3jDinPm94YzsL6ntlm3xU25mRS04ffeYZZpI9DxpRbn57skraqZC7Ht9Ld3Q4KG8nBR-bUW20VGedW2XB5NxaSlRP2L-wHmDlEqF7K_U6-AYLUQoK20mIAOyAWteyJfX5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔹
ساشا تاوليری: باشگاه الهلال میخواد مبلغی در حدود 120 الی 150 میلیون دلار برای جذب لوئیز دیاز هزینه کنه! اونا بودجه 350 میلیون دلاری برای نقل و انتقالات کنار گذاشتن و این تازه آغاز کار اوناست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/101948" target="_blank">📅 23:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101946">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NnZF6K8LEqBsg_yRU_MNpvjnQZVuS47zKpiJHHbzDPrf8Q0TYuZSy6HbY-CT_6m6zVqsIKtiyForxwzBYV1z8sDw7mL2EQ5X_4aPFJgnxlozpuiDxGulU-ccWror07ebwewaDs47v6hPzH-hn9ftK4ZYAFo-FvTrCzI4VHW8s25P4hYovAY2Z4LXVwQ5IvXD7HFGm3hLUjKDpeUXnbVWUvXurDp43CnfK0u-EHhPAdjJTdzZg9cVNJXjaSY7HcthBtwjHMPWyb-DvvUr3Ylx19z4fDIQDiZJ759k_RAP3TGnpmuUM9ob7GPLQSdCUXkZxgefcg33DIM5PlR4ThSDHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRfpmKzNBXMdGq15RcSCtfujpjIAQhBcACh4AA5KNL7WrCdMtuoMsT_Y9XsZy1xkjdxn6VwlJslOE1gmywcfRn6fbjzWbAHy4wbneF_vRXDjUbXQuoTA7JOgo2J6SBIpYAuLgiWEsF6_kvxd1pUlktDukr9SiPiExSu9PLUiwSA7tTFGQxKC3_dcNfiv-gVYlD1WdDEjPgLWfKtqt1ealW7pR5qXtrLJN4q7Mupxl5p8BXVCNZ5NErcXYTPZcLpFNlfTLylvfC_5u7ZAEF1xIHY6icl0vGSx0AXYn7LgVQjnEq68_sJaWAIS_Vc66sOuzqC_OkRs_Pdi8bCKm8IR3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سرخیو راموس درباره اینکه بین کریستیانو رونالدو و لیونل مسی کدام را انتخاب میکند:
برای من جواب این بحث خیلی ساده است؛ اگر فردا فینال داشته باشم و فقط بتوانم یکی را انتخاب کنم، کریستیانو رونالدو را برمی‌دارم. مسی لحظات جادویی خلق میکند که کمتر کسی قادر به انجامش است، اما کریستیانو این حس را به تو می‌دهد که فرقی نمیکند بازی چطور پیش برود، بالاخره راهی برای بردن پیدا میکند. چیزی که بیشتر از همه تحسینش می‌کنم همین است. استعداد یک چیز است، اما در اوج فشار درخشیدن چیز دیگری. وقتی کریستیانو در تیم تو باشد، همه تا سوت آخر به برد ایمان دارند، چون او بارها این را ثابت کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/101946" target="_blank">📅 23:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101945">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8jf5Zz0hfdo_JtN5rhlMdm-tpx5XoJKqG6o5c9GbhRiJJe4wkDydIzsWFqtJ8kDG9QWRSMY7GS6cgBdk3t-DISRPzgGx4NIaNxetQdj2X_6AJDrop_654fSJVf7Y6kxBU6aJDdz5TSoKsKveEDt19IVz0Xv7e80PNe-KGwye6mzQj362ZY-h7qjCrcscjwNfaDCUITFERy2MUy-Fc-3S0sUEHykWiY2RUFc59TyJuRKEhOJuM4RIJTiAwdz8Qd_RnEcLrVE_RUAMnN-1l3i634KiC_m16RNGid_xKgbpFRt13A0T4IE-uz2TDRh3N3jQwJyUv1zYSj4iMxXDrFVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
به نقل از فابریس هاوکینز:
مایکل اولیسه تمایل دارد به رئال مادرید بپیوندد، اما بایرن مونیخ درخواست او را رد کرده است. رئال مادرید تمایلی به درگیری با بایرن ندارد، زیرا رابطه بسیار خوبی بین این دو باشگاه وجود دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101945" target="_blank">📅 23:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101944">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHmRt1OJdSOZHDKpIgCJnMvW2lhQUoTbyUWJ2i0sU1EZcGL6orlXn976QS34jNLaztGXHvo2HvUtGzJOif9koQsKEMg1ZrABPKROwlO32rAv2auHidBbpsyF3R3st5yjvl7k_6VDbL5b9l2CSC2gnPs3M9NyhMP7S950O6Jk_RcMifZZ-fsZTW6dALO7EMJeguLcQWgXEnpjvsICGp0zcigvE2Y37QCwj2Fxlu4aZQroc5IH_nqneIQMIjoCrlWBLA9vhvGRo4lNqPC6H4OO_ugBa1_vSHukja1lei5HKElZUMT0x6u7Uvx00kzIWE2reJTiDSXQAqRaLM7EBOs8rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101944" target="_blank">📅 22:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101943">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUJ6deeNT57wf3Jn0gSfkBpQIyKCB2r5D16NB0uraopc1bjRVY3mYq8NInnQSF0jTUkUuGO3jkBMSkrenGOXBSfe9ghnfXTWq5SVDt9Jf128B0HQtlPpqNvJwyi1QsgC-8dw3j8joxIPuMRwBPbJMEma4bFb6vyZD8AuwS-pYcLNYysdDV_NA85wRFn72BtbzUnWhdWhngtOSD548FNk7rLANSnuN2WV2LIy35AYf5tvs-B1qjLWCHfb2beK25mXgQPwYmjNtkfB1mV5PzrxAcut4rwbIEdk6Qy2tvMurZoRYJMDNmZk21Z244ZAD1rX_5UdPhuG7grtoMpDsVw_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
رئال مادرید و یان دیومانده به‌ صورت رسمی بر سر شرایط شخصی قرارداد به توافق رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101943" target="_blank">📅 22:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101942">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwpZyfNeF3JSVVMxNcsfdNo7e3dESmAXvcgJO3ctuNa4mf1_XGWOJH0_C6_NhChtMrtj52NFPmUgEiu8lnfr2QqHp4QX17EqAKrxIl-PBQ1M4p5q1joIMMIBY_FWnI9lpkSkLeXd3WCq7o9MQNdQdXnD7vZlPgbSB9vrHwP7RLDm8VoPDe_8T9D3z5luwyTOYF326qpYT2LhvZadmHDHvlpGCQAQlBCMNz3lf1mUyuifLumqnd8U_B2SFiC0akD2eavIQoo69mZsFcx7Osm8VmyOhyWPSJM3x1qZqF68ghnI8sZCQGK0ok2ZGRGnDqAEPe5_fvz9tKGGoItRC0gEzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
ترکیب احتمالی رئال مادرید برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101942" target="_blank">📅 22:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101941">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cc_TSNciAmKOTEfzvwXXk9QTCL-ulY2bzm0MxoP5_ul85YMSJZZdZQ27ogdf_5mUqwhS7_nV3FuqvF9DD1DGNGtHPXmdZjvrpV59TW0eSjVOHrwSBiJcLqhyB52tCmcBqOxhIcUeCM-uC9kD13aW8_7xAD-RsHzEeF8yowtkFygmQ8RaK64ntDBP3b_KaLh4U71r2sMLaCTkNdR49MjJUs3A4m_3St31i0VRQ1hRz-aIERkIef82DbXJu-30RREQhDh8KfjSJSGy6uxnT-2zusDdN0405uzWmDbtcyRNIZOmF3vSiWdHisUTR2FWCKnWeVJi0izcA8O8ThXVbnU_8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از قشنگترین تصاویر جام جهانی؛ مارک کوکوریا قهرمانی رو در کنار پسرش متئو که مبتلا به اوتیسمه جشن میگیره.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101941" target="_blank">📅 22:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101938">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mIO0AeePB33GQvBuLQW9V4sTdaBpXuxINlBusYQK09SVw1lepy3ElkWcY9h7W5lwY_NhfTYkvtDSci53K95p57aOqNyaVp0VZHlPfoAsNFNsNQVYJ-VGGvvX0vBrslkAnRLQ1mHbxd0zL-QBUf50ZnqDexJli6FtFTxrT5jSmF7EWvsrmWATzLFV3j-aAIxw_B9WSd_-l1jqG8EGr7z5EBYI0AgyB5Yrz9sje6zj_rs2nKJ9uDwsaWBFMNIz_obColMoxRmudh7fRrjf06MSjpH-gho_ry0u3dfi8ahvcOgHPTy3nhJEUhJD0h9SS2wU5Wg6e6kYneSSzXQ7byrqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPRaRKx6M3c5Vx6GukW81Q9W-bM1d6rM659Lrr57YlKsQg3ibRnqWUf5XZc7gKgZpJyr0_PXUml0N8hkPLnwsg7fHnoc2mg7SFAYSPWSNt72VjBAfFyiJ7y0jnBvKSLC9w64TYVoCMVAvy8yFYrNO01qOSB8vOJN6wl4PsXsBaD67GEbM4uD0tbzSyuq_6TV5ZLNuMiQ9oUAbbxSWNjybbCRg8aE8tdv78JbycL1Xza6A2q1yxs6jMzQpM07psvTmqRmplGR7u5xCMmBdAtdWmBd8PSjSjzEeRc-__8i1WOiv9xym6jXWkuvdVuZxbqZf9eUK7OBJq6rZOGpnL3RIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVXVCs6fwr0PsDJG-QABp9cjVJR1xkrqSlFRXwC6hnCZ7NgSa6Zy_6TOA5sFxTrR9pDMpBuY9dmxhz2YStECvdW55kuucfojSaWzhdpMo1GdA7EaAvMNkF0z4MR5gLfy9PzUS8ouWVqFNPIV9jW6FjaNqwMafT9-Gkwe27X7gXHv04wgvuN--QSQIrqphWvSaoEWZTPHWd_IVDOQUGqB9AIZl9UK32sVPejbnF6NDAUgxD357SnSRbMukZf1YeYQj4tykRKdpQEoW5COLFtf0WpCbab1HukEtnnYJfBg8KgN6enitmfgaHkL33GGbT68CZXYNmrl8I-VDKYkbl37kA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇳
😆
امروز تو یه حرکت پشم‌ریزون دانشجوهای هندی تو اعتراضاتشون ضد نخست‌وزیر هند، عکس امباپه رو هم آوردن و محتوای بنراشون هم اینا بوده:
«دیکتاتور امباپه شکستِ سیستماتیک را تحمل نمی‌کند. همین حالا استعفا بده!»
«۱۲ سال در قدرت، و تمام چیزی که از مودی(نخست‌وزیر هند) نصیبمان شد، نسخهٔ پرمیوم امباپه بود.»
«دیکتاتور را پیدا کن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101938" target="_blank">📅 21:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101937">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWemb-S3gFQKVsA7v-qDk7ub5rTyY-fpi28-oFXIW1VKsiQE3eju_Eu7tUPbd9-Dm5piTF1F1n0Lj93zyJYWl0I8vyWK4v1NrsRgf0AID5c7B2BCBFGQSmK5AKJbIrWX8Uvu7cw4GXW7jFXjsBjsr9Wmt67Dz4UWNNqGngvP8DhGmrbMQi-claF0A3fllcchoXpnNTDEtjDzYZjbUjo40n5ejg9ewx8J-rTSGYyQCHYiAcAZkUVHTKLTik8YIOF3AgzAvJaJ3vgE8S9h63x-IG3RDpL5Grr6v5yB6XJkffmqXbQZ3A81an5S7cOEK-5q915YUN5VgTbClgeOe4KTiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلاتان ابراهیموویچ: "بین این دو باشگاه، این سوال پیش میاد که کدوم یکی احمق‌تره؟ لایپزیگ که پیشنهاد 100 میلیون پوندی رو رد کرد، یا رئال مادرید که 100 میلیون پوند برای این بازیکن معمولی پیشنهاد داد؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101937" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101936">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEpSm1tlicjSesxsSRMaWAaHDEF7T5TE-gsSyEK-1hz5_hHjTnvEaTv6Cxklv2mL5XYhgmQEcphf_p8kedLNyAQ2ePbIoySD-y6z35l6iFAskMyyQ_j8f5GgPsnol1NS8zJpr1CTcUkBP-jh4PDXV1THxFGXRcgHO9njdc4IaSW0VFt1AdX673fNPeNR5LhK2lNbmr9IZcyGQr-ROXu3pqiffS8LlrgYtMVsAzzJEFe39loWTFU637EnbVyS3G4ebv-Jhe2ZZQwc6Eu2X_yOXQIvbVoR6CXx5U0Q57VK4eFO7lmuLaHKQPUbEM7llsmZBFQOdmslGD7KZ3QWoTI59A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
محمد خلیفه، گلر جوان و ملی‌پوش آلومینیوم به استقلال
پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101936" target="_blank">📅 21:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101935">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVLNh9Y4vjCgOICL_gQtTBjnKS7E1pMW-iN2oY7D65Rg2goR_Ba6VSd657iA8AbjcM8BtWRk2ZyNMegynFbFGSMQw_LLpL33caJrBEyQi-pjwbG1Y274-Y_45JbQN7eHh9yGJCDZpDsVjjgIZS5khXI4mkEPpp_Yy_1uMdG0p2QqUc4_7PNlNliJZS9Y0QBsg96ZldS0W-cQHbYFXNRBQ7RlE8VDrPLRgo6gG1eIgaWTKsSLG-ImKOO-EEZrt3si7PI5gTPZe_GIxErEvFuNDMU2e76_CSvAkogyi5CJ_obp7fhQzbOis-q1lLM6-TsCw-3P_o0xRhCzXDcup-NIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ماریو بالوتلی:
یه بار زلاتان ابراهیموویچ منو با رافائل لیائو مقایسه کرد، ولی جوری حرف زد که انگار می‌خواست بگه بالوتلی بازیکن خوبی نیست.! منم فقط یه عکس از جام قهرمانی لیگ قهرمانان اروپا استوری کردم و زلاتان رو تگ کردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101935" target="_blank">📅 21:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101934">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T9bdtTFY5-uiY6ravHtJNG9MXTOZr_mZ8_2zz2sJj45JLAFecHhbQO-khF43rlkz5TLHhrwy-G371BGUi2CKlJnq_wTGFBLUJVsovyC4oqALv5VFwjJEJ5339H2PmFvOEci4ZpxcY0BM5cgYD8LNWItJamzLudxtMKVH9X_HbQFMv_F9zrvAfpYy_ApwrebmyYbjbDidZvmAg1rPuruNE-R8oaCY5yQZyNanGQWWVn1SNOh3XTrOQqamb7hPrxo-p4tZBEdOoaRm5r4HQyoPrT9dcQy_Lb_tMWFa6l1N49AFboITjHzvSBSL2QPmaWBZCLRmcTAJdJREogGPgJesDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t7jB5ZfBhHlojCCp9TKDGlWz-zxE4v3E-YQzALIwCGwMriSQCAif9GgZXLl7p4OBxWsQ4NWp9DWlBk4NYvDAYLvfJ6KxartBTMTTbdX5aSwXYGFvLyYoa32AeDbZnRiWq6q4r-OAyd4mYPOZIiiRJ34fLZlXc_YcQIGz3J6fRPgopfP7QBU8-joGLkrktmA8zr3ZsLrZUSPREtbFROohQbeofHELkb7bBzCSIjqyuDFftMj6EA5z9_YOoXuiAMtuc3hYHKVOdIXpkvTeIvdBOsT933XXKFFEnpc7BxdHbtnmuQIYw5VB-6Yj4gVtlUkL-Joslk-KOnsSrTEv1AfzNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
براهیم دیاز هم از پارتنرش لوز مندز خواستگاری کرد و رفت قاطی مرغا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101932" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101930">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101930" target="_blank">📅 20:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101929">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8-Kxh1L-419KVL4R5IaTIbROP8rDrRP-4cD5vlv99Ur9dxw_ycQ76L8tCNhDaBlseSy78rs3F5qskaGW12ztS0ymPiucULSJTkGUcv7BesBOzeI67kDX7l98h5R8b9Pn50oT5LVf9KjIK2D2Bz5cXr8CYnjfzGFbKHpzwEYbKKI-p6Cqf0uDw33E8UDGG7ZyUMeSG1XbMpsBrtkSH6Pv5esOi8ylizs93xmag0aFC_Na1Fcazi_EbnAB2ZlXgGjeIm6ozTE5bI6H-vFPZ2Deb_smnolGZzTW-cuWvnfl8y--90ALb5sSgk6Un9_MNbUnFsOAg82bFsKRW_0yvVB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پوریا لطیفی‌فر هافبک گل‌گهر با قراردادی ۴ ساله به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101929" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101928">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101923" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101922">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101922" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101921">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101919" target="_blank">📅 20:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101918">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101917" target="_blank">📅 19:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101916">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101916" target="_blank">📅 19:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101914">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3ctxdWJPqLed0mZZv9hn4WsBovVrWnS7HrxvP7WBwXOjbq_w2G4nigpa9zt5BTKLEt8Ug3meEFaWj3Z_5hC4MTMSBPsNbRx1DXeS6MR2kRIL2nOPbVVN_s0M5-ylsdJ7fC8N4STGxnArl-VajM3A6YFMZMyRgvF8bIf5Bk6SXuSPwdCwSBbdS_JoGpVUb3-C916R5Da-R3tarj8viskYgiFTQnvgy4LHiyqwOxraiZpoT4ogN1icam71BJ2LIusSnzgwGk_s80RNYUZOKAp34VHfkCGR9eaoybUtQzTtZ1fgk02JLYKBYs_nQTRNH9zW5phb8OEE1T9JLg_xWMqsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
تلگراف: ژوزه مورینیو با انتقال وینیسیوس جونیور به آرسنال در این تابستون مخالفه.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101913" target="_blank">📅 18:44 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
