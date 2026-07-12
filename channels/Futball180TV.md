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
<img src="https://cdn5.telesco.pe/file/a6TQU73zpo7YSwFtau3smlKrkw8KjNq9ZO6rEtloE4-ELkmHJU859mNADUSa2RQLl0LYQD8H86HSqKqFlfxpEjNoHWYO4CtETlv3CIvcuGfXwDga7aykBMx-IPEExu--xBdkyz-FHXqBuwdoixSv-g2u7eYgPFX7PVNz31_jaSeYbRU1Qspi_MxrjsdMXz_JoncDCSdE5dUtoyuA_AB5SunzL6nJLD7dbzHoRO-z04t-ublL6CUdLjvntt7Th94_rG7qTv52GuWuaAzxpX9VcXgTUKJMyDmAK6RLnu5_hnecrgGIVcnLN2pfJj-ML3JrgmcaYeupBpzQUmWIAe1IGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 592K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 05:23:27</div>
<hr>

<div class="tg-post" id="msg-99711">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
پایان نیمه اول؛ آرژانتین 1 سوئیس 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 915 · <a href="https://t.me/Futball180TV/99711" target="_blank">📅 05:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99710">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/os5_H6ocK6EpPUPmiYmNZ_IQL3HW0f_x2CRX9KWl_BQvt3uI3PRYRa5d1AwuWi9E5lWum5s8am1wJiMtRWEWtcXr_HhxSMmZ7HeCRC9eG_OiB2lZuXZ0tD7skwsJgThvKPrI6o5GjZPs5mXvsLL-3BISbBUO3pg_f5Ne_fsgJTtfyaDDP7T_a2R58ABIfvJYooO4kVz1zHZMiEsAgQrxG3NbpIHqYaorHK-uICFZTTbAeADOFLpRvnnm8bxZrlVqPxV_xDANJq91CVYafOHL49ypcVGOS_CU_h_AyIg77mE1i75s7U_pgOvp-N_yAJaC3WSgAB_dasTAUA0cfwagyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقی نیست اما مسی با قد 170 سانتی‌متر روی سر آکانجی با قد 186 سانتی‌متر پرید و هد زد.
اینقدر بازی کصشر بوده که باید همچین چیزاییو پوشش بدیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/99710" target="_blank">📅 05:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99709">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دعوا شد</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/99709" target="_blank">📅 05:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99708">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">برید دینی بخونید از این بازی چیزی در نمیاد</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/99708" target="_blank">📅 05:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99707">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تنها نکته زیبای بازی به جز گل تا اینجا راه رفتنای مسی بوده.</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/Futball180TV/99707" target="_blank">📅 05:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99706">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUMv9inryafy9W5i2bTE17MkVUGffOEPHFe_Pu_bDzvgqAr5MvbaIOayxuf2zmd_FUqAdCH-_oUHBLpVZd16uGrQuDTrJIuK3YM5xooPLQR2zDzxAg-ATFriP2JO2UFIpIjczmlZSVLG1rSOWjC0a9y3NB-akN9kYjdSQhsw7hAjVgzB7-rwhxe6gNVo0jm1X0PfQ6g_J02ujUcZEuzRTeQMY_kIcKcooUx_tCnMF80tQAPvEE8Z4zmVNoNwfIkEprkq0iosoxZSByRIBmKf9heOI9Mq8rsjsYnMYrLtm3t47Ccqw_Po1LJKryeZFeRVWtfWoHaYALn2uQldek3l3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
عجب رفاقت قشنگی دارن بلینگهام و هالند
🥂
🎙
ارلینگ هالند: "رئال مادرید و انگلیس خوش شانسن که جوادو دارن چون همه میخوان بلینگهام تو تیمشون باشه. اون یکی از بهترین بازیکنای جهانه."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/99706" target="_blank">📅 05:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99705">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxwydmdraQ2QOCXPT12cgSbIgbop5k08kHyY4ynoKnhJht9fMu9iguHIO1UFX-pn_vKV0ClTvzHJ6xhzU3a5nl-r1fD8xc9Xo7kD4KqyHJPgZkrW_guaJwumgIE8rTHs-8rKHlzBsucvnhXcm7dpPhn6CwslBQkM3g-CQmGh66OCepyZEFsicuK0g8APF2vkfglrSVf8pVbq94twsSAEOFckG_WlCAhfin9Uh9XN0830cgS4VAkl-iH9vkwv5dhCczlko1fTlVIBapgF-DYsWN-4yDwbaDfdxOuSWdSL4SJMCqm3ihjdiMw1YHaRim0NH7Z_UM-_b4uYygERhbUE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب تک به تکی گرفت مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/99705" target="_blank">📅 05:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99704">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZbLx3OvlN5nHejFO7UXolnz06PLy5ZEpRoWW1IGzIv741G1p9N3ho9_VgxUjVI23k8Q6b7xYF0emb0kbhgYVuUSi010hM-rQM_JSrlnN2zk0NPLqzbqqIqJmiRwyWhmabPJ2neioIWp0gIr1fcW323zrHUrkGpbp2PEQk5NYR6Y9ITLb86f_QhAYko-iKlR9hPCPwFY6gJ4jib1aOVDEpch9Behod5HbgjMz6tCu-hk0NKRq7NXQ73PmtUDxMBY-SQLtNJsuaE6RKsUZCy1upr3nX2gmDnB0Umsqq0nvm39RAlOIlcYSgoIUkVQ24-57-5MEVk4nJNEiC07yadVlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط یکی از شورت هری کین تو بازی امشب همچین عکس شاهکاریو خلق کرده.
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/99704" target="_blank">📅 05:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99703">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYYCzf7w8HcUrZMkAbEw_eC5vzrY6d14UwpCYV7_IZ1Arqhf3HqxbG1mvhVBMdbmfONqKKGwLfV3Z6fwvyeZf_6YbQwCEyU3ivNUHYJpM2AnP8aWub-Ewv871t_3Sb2JpxzhCQDWYhapx7Dz9h9fnwrLFn8RjmzC75HM5nbp75bRluTugbr79QAeOCDhSId8Hvrzu-E8TNGkRz1W0PxjZhjAViLHWhl6t1JUUEZCL1vK-HGRhsS3wu3WxQJwiMRDBrR5gq-GurbzwU82MxgskA9Xwa3dZzibAgi7qqeUG9C9jvMy0I7k4Fud3v5EUb70yXwzmU02_FCIUlUdZdfL9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
اولین بازیکن تاریخ که 10 پاس گل در در جام جهانی به ثبت رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/99703" target="_blank">📅 04:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99701">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vqt0WMavkwK9va4Bg2AyaLS6WyXzK7MxcoB1ROUcGKk58gwrhT-vO-xNIwj_g7yo1n3t-7aBs92gKl_Z6qb7mVG0J-AT39RYvfwVpYDS9Tjn8-B_JZnz7fx6TMFtv70vRwMu2V-dszSMhrjxMcdJdhC_rnM05TsEmZeGgUUeyq2F0wvSKy75PywxAvMqObjH8jaYaDLDPaK4kjbziweT-m3BYkUVuyZpu5-BEBRTTKI36WbyCnhJLG-XuD6cBb2h_qVXIHsj0KEPdVJB92mnwBlzNk2gzPMKizQigUVo8cdJ4Ey116FGQva6IJoI-Y5B6aa_YCuO8shsr3bTenunXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TkJYDj30coxRJGq1pQpQuZ_mcJcLksutkEW-i0GS4pqYCfMuuVws1FVoQrym4GOLt6Nat2DbjRn_kCdDJzLQGrM0AnPZ9kci7GPF-arNgo3K60GcwLGUDASSJctNxwHodK3hsw-QTte_7XaXP1tRP3NSYGFR5ubndada6CMSrR6lSpT9YvpQ4XL1l-XMAVoeYN1uYviumv6mYbGrl9_jB--6Ye4Go44zTnJVtWRIrEIXSsWMGZ3Yxnx8NfmteMBfOXoiLrLhtisC5H5YGxiupfC5M8QZIvwI7ClTLgLeEH7-oKOqwRL4f3eK5pmyvTA_K49TphBjEb79hjCj3tL33Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه پاس گل زیبا از لیونل مسیییی
🥂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/99701" target="_blank">📅 04:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99700">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bf277a998.mp4?token=QrQdA2KxM9n0Lz8bdzGtxzYu37Jo0ju4vhRpxgNv44IkOtdKz5vKQtdQvvjbTZSN-4JKfaiS_tpLvfb_GhJYxiXpCBSLCWIyEkV-QwUsU_FAP8yy5LcX-Isg1i0hPMU-f3x9A9tBQDKURjXQ69Oqc2rh1hMcoSJjkUu9vvzE2zl2BafCHRRvY5UpHqbZH7drOBA13FnosFTp29gDMvd3kXuxBZJ1lowJzjPEZyI1cyrSsaH298j4RwpkDKDv65PjeOCQVCHs5KdW3By5I6qOHRZEYB9PLc4XJFTRP1ZgjkZC_30uR_JAXuJB68QtvbjnYJKTlTKbm_p40qMN9w977A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bf277a998.mp4?token=QrQdA2KxM9n0Lz8bdzGtxzYu37Jo0ju4vhRpxgNv44IkOtdKz5vKQtdQvvjbTZSN-4JKfaiS_tpLvfb_GhJYxiXpCBSLCWIyEkV-QwUsU_FAP8yy5LcX-Isg1i0hPMU-f3x9A9tBQDKURjXQ69Oqc2rh1hMcoSJjkUu9vvzE2zl2BafCHRRvY5UpHqbZH7drOBA13FnosFTp29gDMvd3kXuxBZJ1lowJzjPEZyI1cyrSsaH298j4RwpkDKDv65PjeOCQVCHs5KdW3By5I6qOHRZEYB9PLc4XJFTRP1ZgjkZC_30uR_JAXuJB68QtvbjnYJKTlTKbm_p40qMN9w977A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل اول آرژانتین به سوئیس با پاس گل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/Futball180TV/99700" target="_blank">📅 04:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99699">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پاس گل اسطوره
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/Futball180TV/99699" target="_blank">📅 04:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99698">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پشمام
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/Futball180TV/99698" target="_blank">📅 04:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99697">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مک آلیستررررررر</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/Futball180TV/99697" target="_blank">📅 04:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99696">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گلالللللللللللللللللللللب</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/Futball180TV/99696" target="_blank">📅 04:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99695">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2U37NoAB3qJvDQJ5Li7_z-T6T4kmk1GOVt0yyBBs9Dt8wEP622rhtdhwyzxAv_d37vYTvM-0UAiKp5dbyGQS-EbVWk_XIbTBXpS5hW0YckUYR4JVWsAHZzrgMjuzCzl87F2ZYPDy_LzTQ9_aICAFyYYA3CNRY7ZhhQ_4m25pEmQE8NCVreuxK5NOQbRoXSwTfvxjPciE7RnTrzjww2KUQjnRevMejSZ52E20iz_wiHAs4KNsqUa02SQXlr1evfTvvWOXtbn52S0FQDFIU-VJMbiQL4PzI6aT2ZTxOohRFDd8fzVoPZoygawHvNWRyfwA2cYDNz0llLwwqX4suorQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید نحس با کیت آرژانتین اومده استادیوم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/Futball180TV/99695" target="_blank">📅 04:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99694">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بریم برا بازی آرژانتین - سوئیس
🔥
🔥</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/Futball180TV/99694" target="_blank">📅 04:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99693">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYEPAJrDc-eyppcsN543OHyRqLc2gAzep-VZeyopmirs7paD5J5KZe_E5KbpQyKqHxx53GD7kmRrgrGW6hkcFVhO1kw-tyiMTCh37O_q3e1HGN6E_Tzih9y3raADFrxJEaVnp4X9d09TLxBoMuVTzh8R9DfxnDznxsErX55QPEQY4D-tPWHx_mjJJhVwqNxB_bpXbAgj_0hlFM_Ft5KdkNQ5t7XJd28HZio7oczu7rbWybLHra7heYhNqxOzYl8lPgPP71Eb1ltMbWr3uGXM_fhHMg7lOUynCCvPk8jALnVNETtq30IZCJLgwJppbombXwFuOqo488uVOkGdg2BQKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
تیم ملی انگلیس اولین تیمی است که توانسته از به ثمر رساندن گل توسط ارلینگ هالند در یک مسابقه بین‌المللی جلوگیری کند. آخرین بازی‌ملی که هالند گل نزد در تاریخ 13 اکتبر 2024 (636 روز پیش) بود
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/99693" target="_blank">📅 04:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99692">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7INmAIg8Z7kjlpwMWOn-Lp4CCPReXyMUEoBOj7t_g28iv2grHyyL-JK8TWFlzIgINK7kGwOegaaLlxTKcKjpp9YLijPrjq-lS7-bmq5uhFSfd4GQ9XDrI1q0Gk4JtqTWb70RTFo-EepRssIPATYu_eaOzzrMjJNWlD3XOwYPNoiltxfkByIzCDkKvab9SoaM9YWzc-6vDWaJkhvutcMM8F3GkXgDxFS6fCSznVhOPx1DlPlUih1FIoIWId2-3aCioooBVhieGkKtsw8M-LF1i3k5zGXqm_AavlFhtrv24KdRHjYLUD6ExvGpXVsGsMKnPRTwPhDPR09kLAgqzuflw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نروژ همینجا با ریدمان سورلوث بازیو جلوی انگلیس باخت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/Futball180TV/99692" target="_blank">📅 04:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99691">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1eK9h92X22_u0AWbYqETFRzYrigM05khbKDohnRhaxoGuN03Gy9kMuLBwnLuhFcpe19H0ge_Jz1RIdenhX4cvFmhy_v0D-Q5yM81AU03x-uzZj2QUk_5jypm17czmfL0nNVeE8_7V7zFcwYjey7uL4rumZWqE5NZShknIpZzNDphhtjjaMZPS9MSYArC8457lMJRw2uQuoz7rlKYVNCcGzNjD2GvwH6wHJ6-t9NMULKwDqsGFL7ATJea6NNfITsQt8Rfe05Q1V6iuArNDT79nYsH_wKjic9dn3dMts4g32O0XZ3nD-ANcNlnS3Vw6I5-ujLBMJyk3uTxoT5suqUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اراذل به خط
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/Futball180TV/99691" target="_blank">📅 04:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99690">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nea7yEzeT5T3OgAOWD5VoUjS1zJHBkhK6v1XIHK9rAS7EClN9ANDSxcA0pRueEPA-HGVIgCAgSpEkEwDG2BsHRNevF_LXWU8_yrgdRijRMXbCNRB4Cz4Luv-v9An5BNsGDUPx6oUp8X0Q3SyKOU8B_y6Gg0fUzpiJfV5zAVsqgB__LAefiXzwVd7gIzwZ0uK1P7ecQigUwpz8XR36kCC6yNIQdm00jX3heJoGGq1hij-kmbi-XdfldpkHHMNYIlrrMmw9FNDfAo7JjWRTsUGWFNqDC9GZKw6E4lhuKwfngeuQN7G004Z0nks_zKzkKClZihmyKAPmw8iVIwvceELpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐
ارلینگ هالند در اولین حضورش در جام جهانی :
⚽️
7 گل
🔥
یک دبل فوق‌العاده در برابر برزیل
🔺
صعود به مرحله یک‌چهارم نهایی
🔻
نروژ دوست‌داشتنی که برای اولین بار از سال 1998 به جام جهانی صعود کرده بود روی شونه‌های هالند به مرحله یک چهارم‌نهایی رسید و با حضورشون جام‌جهانی برای ما زیباتر از قبل شد
🥂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/Futball180TV/99690" target="_blank">📅 03:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99688">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_cDQHbGGKH75fqrwC8LKhswYsxEL_OCX5jm9XVn4hvmzm9RGfuJQfetTkoHBYE1k9hrvppLUNB0jHdm-1KepxF4I605ONUrDwsYW96gjZ4KmLSbA7pM_rNeFbiRlMYRbhy-rNdjYokIc91T2YkHklpTXPm8ChokbHq1MAMFoIr-wXzQGwXIgtaKHW_q6Gcxxe2HOq7cyWDTtz5vRUbuOyEXDUwMFnXG7rCaUIOzLz_IX5NsvbbI-PUdZWkFtrtS12cch1HUpLJ5U5lUTukrsn3j9hPIwUraFKmAJMt6j9ZbJDFVYHMR6hSotNI0tvg6VpYdQ9_4f944-AMcoskL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZBdL74x5Y_D0NST9ri9ul3da-wlPXl-EJR6RY6wasKD2GwKO7LGXYtfrLDYoi7eMolR3lKvitaQQZBbveIQeoJUVrV7SBEo0Tgnp82d3LcagZlhQhRCYvft4RatsDlHP_vLPGasQyUaXCTctGaJVYROom1DnSODr4s6HQS8eiz3NAA8JY50-U7Lon_pe7KTvPq4vQmnW9vR4LBuP6SAGjGPp2N6bqm_jr0RgKEyshZKnO0IQUyhVBq6qewKSv3oe26JPArElDWYKQLPztWU5Xa26BVbj9rxJHUVehso1nZlAsOlNi52vCCqG9an4ubZ_67309_9gedF_wRYuPpf_KQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👏
با اختلاف ایشون دلیل اصلی درخشش جواد در جام‌جهانی هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/Futball180TV/99688" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99687">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c68715520c.mp4?token=BCq2BkE5xxJjZ61OCjxHeaAc1ymR6ce4cMD8eh5dVp7IfgMcsxOSj02i09fISgVqUQSj8gNpPpbL-md46vO3OxJLEtsCTv1ca4Y3qHyd4LT_ALoJ04LZrRb9wXVTkgh-JPXnbE09OpkYGUDq5QWxKjD9FICeUQwDvCs6vX5062RNVd_keM8L5JGVpLgEdF2f4t6hrfSg-K4wKlk5aYn75T77KhDunwNN9ateT-G5sT37QB2vWbN7q0m1Os_cpAJYhRmNHVSWcZRk12flp0XASx_R_6dnb1xsPlDM3OcaZ3nj76rn_6pTvBk-uEt41wz2s71eMpWGpm-c3ICHAToYzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c68715520c.mp4?token=BCq2BkE5xxJjZ61OCjxHeaAc1ymR6ce4cMD8eh5dVp7IfgMcsxOSj02i09fISgVqUQSj8gNpPpbL-md46vO3OxJLEtsCTv1ca4Y3qHyd4LT_ALoJ04LZrRb9wXVTkgh-JPXnbE09OpkYGUDq5QWxKjD9FICeUQwDvCs6vX5062RNVd_keM8L5JGVpLgEdF2f4t6hrfSg-K4wKlk5aYn75T77KhDunwNN9ateT-G5sT37QB2vWbN7q0m1Os_cpAJYhRmNHVSWcZRk12flp0XASx_R_6dnb1xsPlDM3OcaZ3nj76rn_6pTvBk-uEt41wz2s71eMpWGpm-c3ICHAToYzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو منتسب به تهران؛ تایید یا تکذیب نمیشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/Futball180TV/99687" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99686">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXdD6ygahE6ooCpNOhfz2UmAQ602J3_N6tsHOsJ7ExCHT8LaElAT7ogdj72jKsOtX3wehJVg3og655oC_N1mVyvms-QDnvFVfV-LeKCBivPXJgBUhsj5FQHwq6J2VzHkh245NJiY7UFSFdDMp8AysaF9KTSbPqcwm8NwDgt0TWMhUnDrv3Ai2OwjrOg83YmZdw3Y8yOtEcPimA2E2LlUKyoJIrarq4tsVp5kCbhTPByVFG2qOVffv_SB3O6DU3yPmQPUByPAp5Od6QpzmMLPN3cspioLa9oqXlecD--PnT5muAm3-RM10ptxh1rAOlGtq3jDTJy390M-jlHrj_6Rmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✅
تیم ملی انگلیس در این جام جهانی 13 گل به ثمر رسانده است. 12 گل از این 13 گل توسط هری کین یا جود بلینگهام به ثمر رسیده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/Futball180TV/99686" target="_blank">📅 03:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99685">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nE7uYkPihGVgM64nz5EQ6NVxxfsdSctKkgWAoC3VYBQkSob6L9jzKvF03QjVlf8NBrG2D1-CjSuT6hGtnkR8lg3h4GDoLYvFgK1ngKIEnsuBVKgNj_9Hdczq2tQkOfd_WQhN17_KwOlhK4r2l1761o-9Mm1xl4gjfzv1biAg0GDx9mZIKCHx-mUVabaeLg48BKJ-xMICkat99Y9RrZTrCPYHGnW0ehUNlSlT49_PhM60rfy-_WQ9lbHuJZL1WyZdAPL-LN2dD8EursVdZANgZk5IVKLaw3KkJpe_9pNkiI4xFMfrh-xQsfuCxTQuKJLRYczpwgmRDa2KfNhnFpk3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
جود بلینگهام با تیم ملی انگلیس:
🔥
[54] مسابقه
؛
[12] گل
؛
[8] پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/Futball180TV/99685" target="_blank">📅 03:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99683">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0eDzObQtPGTaDJLY0s0f-CfcUUFZ59p7a-KTE_eZe7r90vCgv8XhppLgoq2w6W0_K6ZGNJ1d-pL1Oy6DLPq0Z7EM5-LjWAICsTu2uEb06mCR8C8XoUOwfWbNXoKZazS-TdGLA208kBTKXcX9jhKM0SXLruz1w8N7c22E52cVxDU3bntSVqab3xTsJgRR-gsaFIkqAhlCXq2rox3kexxY9JZFqAr6Pm8nkc104vtQElPcV9AZPCtvmvdQBDAJ4qzTYSy04ImAWlbyGEdHiVcA_1L7fhcLSK6tZHbITNjdlgUX2HxilKjnRLcRhPf3lxK8LBl5c6CLg7SqdcCU3mHGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام، اولین بازیکنی در تاریخ تیم ملی انگلیس است که در یک دوره از جام جهانی، 6 گل یا بیشتر به ثمر رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/Futball180TV/99683" target="_blank">📅 03:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99682">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U75JgW67AyYL7cltK7mKbqV0qmsjLzhliRtNVgjT1ZtlR_vuwd33CRvypc_YXMDJIXcFO4Lv_wDxsg0KPHfbLn3IVDK33sArJ0kseJ9YA96aWzdWAJrOLoRtTiEwEBi1jAhDNx3uZwWPIkT3ZvujSk2R6qk5ZeGg2dCFQExKUV4xW0MN3gUjUCRo4m9LZi1u2FyV9PxtPhJ2SX7-grPnCfkbI9X1vMZW-VdrX-kzlXSjK2QJn_06qlLDCvBa_ilDkPl3HM3BlMJkg-1siSrJynjh7P2yTHNB2mtE19yh7N2ptxr04MRvMIGv5i5dfibjdVUJn3nsw51lBcaiQdPJ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
📊
– تیم ملی انگلیس برای چهارمین بار در تاریخ خود به مرحله نیمه‌نهایی جام جهانی صعود
کرد.
🥇
آلمان: 12 حضور در نیمه‌نهایی
🥈
فرانسه: 8 حضور.
🥈
برزیل: 8 حضور.
4️⃣
ایتالیا: 7 حضور.
5️⃣
آرژانتین: 5 حضور.
6️⃣
اروگوئه: 4 حضور.
6️⃣
انگلیس: 4 حضور.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/99682" target="_blank">📅 03:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99681">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGXebY0hzzE2DHg1u3K_ci357c72dl-hfK70JQGtmHOKHeyEWHV6bCtlE8QtVIhJUlPt-sYI88Wf9O1DaAM9HUmK5Gm_PTi6scOfFQcKaxEyTKN9x6fpujgEUV-oMPqZNLaxcUzR8ppMlZY4-54Fa8etNadzNZ91y-wwp0-L2tZnRWvs23o1ZxxjZoee4yG784ZNhsRnKn9_huANPhcwzV8j7wIX4MgAn2a8zzyfCeSK6JQ-ole3SJ71Pt1u85A9V_2nyEs3gJFgqW8CY-16ByNJf9THdao_tzDPhMufa_X3dFlt9FQQ1We2iVi3JTBvZQJaDD2Tr7FIRW96pNVITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری؛ هگست وزیر جنگ آمریکا: ایران انتخاب نادرستی انجام داد. اکنون باید عواقب آن را بپردازد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/Futball180TV/99681" target="_blank">📅 03:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99680">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIUS5K5LWiyRaM-jiQU3MnjqvUlMgINR_xji9ou_vjNYc9it1pvdpoJ2kcXX0Lxg6bGoBJJmkLDkh3nOJrdE_xV0Qr6FCJj6ZHZT2ev9EmV2argJ86FCuLXRs7DSsYfP31yxL9gIQFFa8p4W7Cho5_nHLkssBWn_Qd3tVZ4S4H6jnLV-z_RV_H22skbmxl2jQoQoRZhtcrGhDgAEM4IGR_SfcyfmiR-vNQ-Fu8kvDiiMro44VgGGVOKVl-sg09JSAI6fwsZaa-gL3uMg8urrbKXLZQrtzDK3iOGxtCq60NPYNkSPOOH45DkP7zSaFkX3dnGjHHuIA3fhqL0yJ7glkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار حذفی؛ فقط مونده بازی آرژانتین و سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/99680" target="_blank">📅 03:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99679">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/op9tlAC3nN4dfQ5eiM0oe-7ksoWI2G83mrvoBXcfsX1Nfu_klFhtrHyfxOm8HjVTKT3Oo2c2wAZjbwtFGUGIk0RhUdvdH60UMckeBxxfHIowUCvpGQ1-kHO83H8UKxJDcFK79iyv9XjFwpFaE0YLmtGW9e3oxqHnYhAVWBz98m0S9Cemsfs2Evc20LZyFO6aKl2EmGj2AKz0YCTwCn5Dw6Dr0jRNpw62ufq28n1AiQDSg-WTmyrqKV8tYZG3S9o3jX2HiD22o5SG4dJL8Ara_ceO0MrplF9chlNn00riQEeOY4eEOl_TB32z4dUflBERZcCEcmPsNZhEHEnNglzyZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | غرش سه‌شیرها در شب نبرد شمال؛ انگلیس با نمایشی پرفشار، بلیت نیمه‌نهایی را گرفت!
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
😀
-
😃
نروژ
🇳🇴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/99679" target="_blank">📅 03:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99678">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بلینگهام تعویض شد</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/99678" target="_blank">📅 03:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99676">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VYuH_uTXwQRfOS3aREEw_vhE7ZtO_fqR9PPC2zCA9l1HLQs28Kk3PWtkekoneZ-GapePf4MPJVJRY1wK6kpJ2GnKOGwGhpSo_CFfiKR7lGjR8sUAwIlgB1RCO_px-7kId724ro9ZsKLuNX5oRseJfGqAQ7RIIKeLwHU8XJT43UP_jYUOO2cq47LSwtPS081qIZGWy_oQDs4oicXc8OcX9PTqHPn1PzWZLKgzKW9KudpwgBltxilZk5bIQiReq-_LmQ--4QXwVm8Lv44AcfBZ0uTtQC2nRdrCOD55q5V5ck5fOCaLw2j--xGk2Jd5EKjcmjiY9byVAdtt7v08nRzK3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cG5YGLMpg_sQbdV3LcCJUSViTc4bLeuUvznsCYykeexZhqUZd8kWDKoF4m2jRJ_Gcnkh19CovvNgqaK7s4lgftxd6sSVfyNL7l_X2Az5hzRs0BNmZBFznG79_AKwd-BeHFNckL4UJfJBcwb72vuf6VFuznA189ZkzcviA1N_BPvRaN9diQeEVeFxlUleA9R6JGuUyEnhbZhswjAPhMMBMoMAwIG-MDPzsZnX9eScWGUOfYa8jD4xeCX_I_opGZ5s-DMkgfE12tMGHHGx1J_FOjlDqD40gbWcjzMaJTi7k0rQSA2QDxGv56-AepVcOB3bXQqPJw_sC-u9oFszPAorIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇦🇷
🇨🇭
ترکیب رسمی آرژانتین و سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/99676" target="_blank">📅 03:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99675">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">هالند تعویض شد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/99675" target="_blank">📅 02:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99674">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
گزارش‌های غیر رسمی از انفجار در بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/99674" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99673">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
گزارش‌های غیر رسمی از انفجار در بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/99673" target="_blank">📅 02:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99672">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رد شد</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/99672" target="_blank">📅 02:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99671">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">میره وار چک‌ بشه</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/99671" target="_blank">📅 02:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99670">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پنالتییی برای انگلیس</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/99670" target="_blank">📅 02:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99669">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9f969f51ad.mp4?token=UQDQIdKBtZcDipAuHnPCmCWa3udIRvEy-2eBijRl9jcz4li1o6XPjiFEX8xlSCZ0i-LO2UOcEK1Fc3CN3LMOZDBd_kL6e3ZecXLemg9rwYicmBcpXjYriwOhOrHykMW8QaUojE1baUtu8BIyUW67A21WpwgmXptAt-fjt4XXxcc64Se83--yh3y0b6RqZWx4VwxPTHX38YNf20cZNNRDz3z6qA4U2_RPhSKAr30lvW-FU4StC5H2nuEPb7rouInOl52C2T4T9qjIGPCo9wGhKi3Ki_OrCYerqgk4_7dQ2d1OBy10tP_jO3ysIBDXPxR4oNHNzCCevCJkFiiu9uUNlQ-wdkoa1ud3dMImSQJkMmca8a0hh9rNlSreQqUKue4hexfHR2s1N57hkkKMsAdlJ0jqO-DjvrtYwcIVy8Z7vpL_WoAaX6Z6_VjZlv6takEXqH5slEMSqvT_jg58ATpbKySkQEALhYuD4RweayyFNqF08rvRTB94qGSDbgIUj7JS1P8wPDAN-XiOQZsvjIo28xFBf2EhvStvu4vZRYEsqZLQNrVPqmaJyicdX6vmpjHJX4LluB_fV5lFXjBIZXPlt6VevNEOIOd8BH99KSjq3nVIE3HRDKAzQl84CJgvKYHOu15MVLLlqVwqWkwzwUf7_soJ4w8PnzkQXFYz7cZwVmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9f969f51ad.mp4?token=UQDQIdKBtZcDipAuHnPCmCWa3udIRvEy-2eBijRl9jcz4li1o6XPjiFEX8xlSCZ0i-LO2UOcEK1Fc3CN3LMOZDBd_kL6e3ZecXLemg9rwYicmBcpXjYriwOhOrHykMW8QaUojE1baUtu8BIyUW67A21WpwgmXptAt-fjt4XXxcc64Se83--yh3y0b6RqZWx4VwxPTHX38YNf20cZNNRDz3z6qA4U2_RPhSKAr30lvW-FU4StC5H2nuEPb7rouInOl52C2T4T9qjIGPCo9wGhKi3Ki_OrCYerqgk4_7dQ2d1OBy10tP_jO3ysIBDXPxR4oNHNzCCevCJkFiiu9uUNlQ-wdkoa1ud3dMImSQJkMmca8a0hh9rNlSreQqUKue4hexfHR2s1N57hkkKMsAdlJ0jqO-DjvrtYwcIVy8Z7vpL_WoAaX6Z6_VjZlv6takEXqH5slEMSqvT_jg58ATpbKySkQEALhYuD4RweayyFNqF08rvRTB94qGSDbgIUj7JS1P8wPDAN-XiOQZsvjIo28xFBf2EhvStvu4vZRYEsqZLQNrVPqmaJyicdX6vmpjHJX4LluB_fV5lFXjBIZXPlt6VevNEOIOd8BH99KSjq3nVIE3HRDKAzQl84CJgvKYHOu15MVLLlqVwqWkwzwUf7_soJ4w8PnzkQXFYz7cZwVmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل دوم انگلیس دبل جود بلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/99669" target="_blank">📅 02:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99668">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آقا جوادددددد
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/99668" target="_blank">📅 02:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99667">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انگلیسسسسسس</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/99667" target="_blank">📅 02:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99666">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گلللللللللللل دوم</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/99666" target="_blank">📅 02:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99665">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
کاتز: ارتش اسرائیل توسط من و نخست‌وزیر نتانیاهو دستور دریافت کرده تا برای یک حمله مستقل به ایران آماده بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/99665" target="_blank">📅 02:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99664">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
پایان بازی در 90 دقیقه؛ نروژ 1 انگلیس 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/99664" target="_blank">📅 02:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99663">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">۷ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/99663" target="_blank">📅 02:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99662">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOtkRUA2kV7WWwLbp3VWn25smgYTSI2foRQD_s-4HPKTacssxY6plFptRYQbL4388B6yXVC-nyg5jzGLix7qK-rlK7untQ0NoC7ccREte4S34HFEZQKAM5QOpEUCdg3QJ5hEYWzstCP9HyuN1yJuPihOptK6IIZa8H2QMYSZPkfBBT09cqmeM7o6Hjacf9PhTE9fs6m4pcgMZ1PIvR4Eazpgx6bXZbJsLCCi_fFq6dF4M7iWfMa4Ogr2Y_z7lYTQdNkRxpjkp6NO1AZ5aCywaGKY6rs5TOm3yjPrg6_WVAEAzOy0XulmcVklw1UUkIzF4tzzHPd0rDidxZOlHiJ1YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووری؛ زیرنویس شبکه خبر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99662" target="_blank">📅 02:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99660">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
فووووری؛ با اعلام سپاه پاسداران تنگه هرمز به طور کامل بسته شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/99660" target="_blank">📅 01:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99659">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رفت وار</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99659" target="_blank">📅 01:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99658">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
فووووری؛ با اعلام سپاه پاسداران تنگه هرمز به طور کامل بسته شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/99658" target="_blank">📅 01:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99657">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رفت وار</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99657" target="_blank">📅 01:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99656">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نروووووووژ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/99656" target="_blank">📅 01:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99655">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گلللللللللللل دومممم</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/99655" target="_blank">📅 01:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99654">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0237e6ae5.mp4?token=ZXn7U6c_zvwoL_1S6WLPYxwY_OpzgiswtmFJi3f8kZHpvTZg7TldebLBN38L_2aPTDHbKkEuz4kiLB_2lMgIaTgYmAKYh4agvRgSq1Te9UYvIkbQr2LiPc0vn41Wa8rtzWwQz6igZDjGx2LaB146YYgsnr-0e2c7TPkxrasPFpDQdRGnKh3wNN5TGNNSZnWIUrAaeYNtjYitnHIyt4c93TOPTu8ue0IDwG1kVMES0z240hVT72IXSo_yo7cnRWSlBEQbn-ppUIQ--lo9tukhT8l-MXdIlqDYRUHJjTiuNPaqHdkbrh2kCoEsW9CCDG2o0-qnGY6Lm4x_bhfTmSn0uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0237e6ae5.mp4?token=ZXn7U6c_zvwoL_1S6WLPYxwY_OpzgiswtmFJi3f8kZHpvTZg7TldebLBN38L_2aPTDHbKkEuz4kiLB_2lMgIaTgYmAKYh4agvRgSq1Te9UYvIkbQr2LiPc0vn41Wa8rtzWwQz6igZDjGx2LaB146YYgsnr-0e2c7TPkxrasPFpDQdRGnKh3wNN5TGNNSZnWIUrAaeYNtjYitnHIyt4c93TOPTu8ue0IDwG1kVMES0z240hVT72IXSo_yo7cnRWSlBEQbn-ppUIQ--lo9tukhT8l-MXdIlqDYRUHJjTiuNPaqHdkbrh2kCoEsW9CCDG2o0-qnGY6Lm4x_bhfTmSn0uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چه حرکتی بود آقای بلینگهام
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/99654" target="_blank">📅 01:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99653">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بریییم سراغ نیمه دوم</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/99653" target="_blank">📅 01:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99652">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAsp12R3F2Jszz969MEGUHNgIGJHV7e9joplFA0a-CrmrTmPANfwwiYaG7BwRxfyRvGp63cfiOBqhL5BXevX97oEb1Qrp0-T29z_uPDXeqDrFWyg3IRNTpZZReTkrG_kCfdtDg2vUMBDmNvzdZcYMVZ0_ZT3IxhP-lk-200KQ_oohtEdbsDDGybzXa7qyt0dQ1Kk5-9DRGV7dX_ReAq7JR8BlbVp7mOV-oI9R2LXinGpAWZy3MNnYt7iuyaZ8C-IDLUQWtDgPZGV8dI6BKh5svvLb6nIQwDNdbjTy-6Q1ui2Uvx_YG0LOLAMGSJ4oMa8uqzHbm9bPY7gZyRaU4gE5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جود بلینگهام در جام جهانی 2026:
⚽️
یک گل مقابل نروژ.
⚽️
⚽️
دو گل مقابل مکزیک.
⚽️
⚽
یک گل و یک پاس گل مقابل پاناما.
⚽️
یک گل مقابل کرواسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/99652" target="_blank">📅 01:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99651">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnrOZpaWec1WTxythuuswuDP6gdyg13nAYSZoVyf3DLgpE7-IErwQU8T4OYZCr6VZe_4Xqc2E816EWIfn_Lsp6354VIA1q8dGiPDsY7yKeoseMCs6nZ86nkJes7YwZT7oydDdHKJ_WozdfiwNAkiaSvoo0-dEGsuKQ27lxvVPXiEOYszzbTfEcSAhUTSHewkWz3LwgkVkN1_N_mlwuRzA0HjKjeRXfgz2_pemlPPQnClTMBk9b-O7VDCmrIsCBX82mZiVsqp8L2fRgOgMOJfiii0UU8SaV3IDrRiHWnBrnaxF-PlLmF0DzafYD3_w-5gYifA9n2ZVAJ08XWR3VHsXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیکیو خیلی چیز خوبیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/99651" target="_blank">📅 01:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99650">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbRiphoXL3YBCcwVdlK7XfwYJ1rfVaHAr6Q8Hsb9HgFAZjTyHHxxsikl_U6AyDQ_0Kn0e0YOlS8YKeW0C15GYIF6I_AUkDUjGRnGKZ8cXaAziXThufF42_C8poPuYR1Nf8eyxoFtMFa992OgukjNsXWqVO4sB2C2C-vFqDxMpeuRGWlEIAX1KLkbP6WEIUUfSi3RpcAPyrHx5LNYvg0UV7lcT_AGclyqVanh0P2wVVev8w9PRqQKSx395oukik5ed1XCwfCj-tu-E5Y7cqgdy2Y_WZxOQ2iK98Le1KIquQ3bcwFnxuCKo032brXh7TRhZxD4XZ2sqoQvO9POU4Wn2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
آمار بازی انگلیس - نروژ در نیمه اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/99650" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99649">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye9CX38Ao-HogThpoo6pLJwdRsfy8hwhtECsG2SThOwB8lOOEF31152AlxCT5Bu7fiOLaXgthZ0tnrVJ-9NFKKJ1QMry0k19jJDdcC9Ncqx7yeeafypwHxm6qvBrr2Ko2WIoMwppog6yIOXQukc-ExfWxMmvlEhW66OGiYIIFlnmC00Emh5qbRXm9EJHlxbyCxI1c6C-KPNp_oJsGpOk9wHe9HgWnuP47VT9uNRpw6YRvsEtNGRvcVBpMpaUr5pmffZMPJ6CajJ4zYyfn7RJ3AgtUYIQnIGXLEDNWOdoB0oGUm8xK3e6o3OYGAyDdcNjyw7tCUHfW9n8h8W5XdOsXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفساید گرفتتتتت
😐
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/99649" target="_blank">📅 01:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99648">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvErHEWjb-uTYy-fz7rB6ktwz2IjyD0AxGYskodk65SEQJaCZnu_kFcCLELXLG__b9uHZI8LsXCXi_f1OcOGWKb6Dgr3iazF5pSISWiLcyVq7dGd0RJ0snJ0D3gJbKQZZCQ1ZHzvtZ2BvjOoap6wFgiYZcWUlsA81V66HbaSn143OSUQokWLPn7pL60xv6QDyVdJ3Hl4ehau8__4hzVTrAi595au59V136s23IaInmvB6_ZVVyfLkm-BB7n2peho7NelvMzI6T2Ma0MyhB50n4S8mm_5Iw20skJvTcgYZqKExyQma9XVU5oqRnNwpzm__Dqa0J0adgkncAqibQl73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔥
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/99648" target="_blank">📅 01:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99647">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
پایان نیمه‌اول با تساوی یک بر یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/99647" target="_blank">📅 01:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99646">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آفساید گرفتتتتت
😐
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/99646" target="_blank">📅 01:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99645">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چه بازییییییی شدددددددد</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/99645" target="_blank">📅 01:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99644">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پشماممممممممم</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/99644" target="_blank">📅 01:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99643">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کامبمکمکککککککککک</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/99643" target="_blank">📅 01:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99642">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هرررررری کینننننننن</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/99642" target="_blank">📅 01:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99641">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/99641" target="_blank">📅 01:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99640">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🔥
گل‌تساوی انگلیس توسط جود بلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/99640" target="_blank">📅 01:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99639">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بلییییینگهللللم</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/99639" target="_blank">📅 01:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99638">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انگلیسیسسسس</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/99638" target="_blank">📅 01:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99637">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گلللللللللللل</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/99637" target="_blank">📅 01:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99636">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBFtpg_RicGd0sgSxQg_cbEtSmZPka-2Wb7PprY4FxcW2DzOiLnAmpxsGBrxU6DWdM9gQDiv94S_Cs7fZIC3wzmyZ-qtTRVEaEP6Q1qYSs511rSXkj2vGh_rnJbD-OFR-IEVqa6g8ujecW89vVT9K_yDqwt-dL2zf5TNGL7bR9ASGcadjGebZth2A4vawBy8uU_3TvKHc7hzV1PeRnlWvBLPpV0R-_zw-nqH4C3xsNzL4zLZ8Pb6fxhVBGtXGtLKqmbqpqifdUdgyN6yFY_3ZWfV8YM5F7CACqJ48cS2Q80P9MHv0i_fwFsjQdsNH6f-GbWVtktmg0xq5IphZLNSig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حیف نون و پول بدن به این سورلوث دیلاق
😐
😐
😐</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/99636" target="_blank">📅 01:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99635">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سورلوث بیناموس چرا نزدی
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/99635" target="_blank">📅 01:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99634">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eeaaaab8c.mp4?token=LQAItvdNLowLRZZZqPwUHTz9jhWH19O66108prm6J0m8tErn_Xp9TJvMwreR9MabtWTXcyoDgo-ZT-JdzNbXEt1RBnncgUYxzvHQB_z81pMUZTCNBEke-KBuwel5L99niAT-dxQb-Sa-1jb3WgHx3fhIdycVgx9avity2p_5fOjFiixIFyZ2NmsdxeZMN5HamvUbYBgHBy8wiMlp6PtX3Z76IqcFvx7KEc-UUxiyvBy5VsgjePSG4dA6Q9V2vvZ0P3JBj6bXmNxbv_m9vt4WgUYdI3xNLQKHk5cpzu1PTLr8e5zZ48zJ-I04ObyiUKwBBp7QOS1qHE_H_iB1iR1C4Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eeaaaab8c.mp4?token=LQAItvdNLowLRZZZqPwUHTz9jhWH19O66108prm6J0m8tErn_Xp9TJvMwreR9MabtWTXcyoDgo-ZT-JdzNbXEt1RBnncgUYxzvHQB_z81pMUZTCNBEke-KBuwel5L99niAT-dxQb-Sa-1jb3WgHx3fhIdycVgx9avity2p_5fOjFiixIFyZ2NmsdxeZMN5HamvUbYBgHBy8wiMlp6PtX3Z76IqcFvx7KEc-UUxiyvBy5VsgjePSG4dA6Q9V2vvZ0P3JBj6bXmNxbv_m9vt4WgUYdI3xNLQKHk5cpzu1PTLr8e5zZ48zJ-I04ObyiUKwBBp7QOS1qHE_H_iB1iR1C4Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
گل‌اول نروژ به انگلیس توسط شلدروپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/99634" target="_blank">📅 01:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99633">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdaIj_cs-Bd1x1HnL9yZRKZkY-F5LEdiKhprW8WZXxXZwncF8EkP0T9MviF6SD_8AQYDvjkdMxcAHwR0ntT7P7VqglLRQINVvHm6RFiUnaff8efrNDT8Iue85Gs_pO3R5v9xopzHLGK18WfSMSu4RDZiIdbu4dopkvGwiMj51pgjCQbM13y5JwQMpqoakh4K4k4YBq6PWtglyUTdGDTvvVxkkp4cI3Fe_LDVhcp6fA6_QfkykndH62a2YKgCE_HKbCz95tNGDaya7PCUrMBsSVX7ykxa0C4BhLeXh7_QlplA3kNs5EY-kYnUVtGChLVmf3KZ0kPrmzd3yGyHpu29qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوشحالی گل شیلدروپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/99633" target="_blank">📅 01:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99632">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گل تاییده</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/99632" target="_blank">📅 01:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99631">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تاااااایید شد</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/99631" target="_blank">📅 01:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99630">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رفت وار</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/99630" target="_blank">📅 01:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99629">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">چه سوووووپرگلییییی</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/99629" target="_blank">📅 01:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99628">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نروووووووژ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/99628" target="_blank">📅 01:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99627">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گلللللللللللل</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/99627" target="_blank">📅 01:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99626">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کاشته خوش جا برای انگلیس</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/99626" target="_blank">📅 01:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99625">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کاشته خوش جا برای انگلیس</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/99625" target="_blank">📅 00:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99624">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1-9l-mpc9ATy3YBfaHwlMSKAAKZkJ71SHvb5azZukkfxOdDG8zWXFB4eYUjbwrsL1Wv9lgIOxTabzJkldN4bWYCrnH33pTLKkYuWkkQfE-eQBSg_B6sID3FyBObhLoV4ytOwpdwl1Usw4idp1lj9GxkVnRVUiKSfMxLLRH0f6sQ0Dxoc3C8xZ_sfzLr9SXwFBETxOsbDJ_tTpoNZuaFYZFUmAK19TmEiRz0SEYKQIL40nHgBM6pVm22p4VV7qKjoX3PnpDADodXkQGVxWBZAJjwTvtt1QNHmMt6RYGfjYPha3JQXiRXny8ymZVbRc-XYXUXL_9JVroOzuUl-7v69Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/99624" target="_blank">📅 00:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99623">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lymkMvBETWPQstQ-0JCyLQ9xVzYSepnSFCakvfIrf4oaiXE0SdWQ8gf8DJdOps-lZfwfXNNTjlr41NEUqfX1KKwirFkOK1aacKlehbJwjNQv0pq3qumGUw-BqVh0tmfP4HN2cFAlY3aiphhu5Uycfw0sOuwgISos_9EMTH5A4uAqUNI1spsa--si96NQsnYr8l79lXdvTfR5-wKYxKZWwqGel3zbpmQr64OqoWWkzIRwrRT6qhLdOt6WAgR4D3cqFA1AiHZmqkwVsHB_LWc6eKlzvuBBRJjuBHlij-dsVHwzbxrzEYxzwnVqmBkxfpnnDNOhaNCNxLIjr1Fo5r09zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی تا اینجا حرف نداشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/99623" target="_blank">📅 00:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99622">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6CCTz0_eFHDNt-dTfcA1SE9cVSitreYVPkMe1aeb56xpEPeaXMCybHBJr15EJ1lPE_36TjOxbgfDMzR2m7xS6Uc5PFA-hMI2VBWLnjuT0j5piX7gUfceUpeqUvNDbAiKoyZoiHxKuQPigcRDOxfOj2r8H9md9cA91r-vtBs-c6qM7wVk83X40217nsLRnoF8nRbFeBomtvC8SvW3OuLjcv5OX8b51pP0PgE1YJ3egmlyZk3PVgDufhX5eyc3CQMlKthfYl8oN3drYptqCVN5TbIb4eZj71lTnzx2sxNGZSkNWgQxrWOqc3_pxFpE0s8c3g-s1Q5lW0WoWIoRIAW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم که هستی بادوم زمینی
🗿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/99622" target="_blank">📅 00:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99621">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بازی از الان بوی ۱۲۰ دقیقه رو میده</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/99621" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99620">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">عجب بازی مزخرفی بوده تا اینجا</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/99620" target="_blank">📅 00:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99619">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شرررروع بازی جذاب نروژ و انگلیس
🔥</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/99619" target="_blank">📅 00:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99617">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPvQ26MeCUJfYlLxAWqQuGQFEKltwy0QpNWX3Srrjzz0qTAxjHFHQ1aPJjZ8Eoii01bMxe7ANrH-9xQ8ExkuO2I-TJCP2VZNJVd483oM_tL1KxCCWRFOXOs6GN8LApHKxzBLChgd6vElU-Vze77Gn9cS7agjCN_GnRUeJc87WydOUvrn9xjPejPQcsHprU5Slpy7NTmdt-eN9ArzFpLTRilRBIrb-lKGYfURM709x-VnZmW6nxcxYdrng0aXye9RI5pTgfoRV6iyr-JI8V95N9N46ZVQqwo3G296t_cYH0QE8nI2xdG02Wq7D59fqKivLsBrx1T89ncU7Gf0vxIxIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EYaiaw_7KRH6kvpVIE7LJQbtFZPd2NyGAO8xZ_M7xEiGBvc8MZ1a3gU-mSfTmujHT1ARyf880SmC6V4qcv2BBesCdDhYWHJoZuv8lmBUld-hYCQwCBIHV1SjU3-q8ggVAOnUMl3dd3qa3WCOw4zHlq9WwDr0Q0dTeuEdcRB4jsuMxnJOB1gZ0VSgwjUCBi1Q1RG6hYZ33UfYCFdkCo8BxCA8wieRmmfKxMRNluU4j0SLW4LkB4XPFHxgFWV2fgHKC-YQoHvsXxqFwGvwo3D8cgsbgHbdH0x4gVqQS7_nHm8wyATt09Lht0mqWMrxVikyhUQfRBKHDavGVWriFOj_rA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هوادارای نروژ و انگلیس تو استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99617" target="_blank">📅 00:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99616">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48060b8592.mp4?token=XmnqvaVfoTG_8SPk1kFNGgblc7XQtF6jSmIoB_2rZyjO2y-Ddc53JEKyEZR-rZBO_Ku5Xl2wQaDpU7EWet1eb-pEI6Kk1J7g-aIB6r6DGiSQ14BeXT8cPN1oD2ehDuv-DtBoZ__RHuSPFRL0qT8NYGHJS9hsecZCwadVhGKWyV4jKcjQrFcj9lx3u8mDfISu1TPwkc3gi0Wqp2KlNXB3AlWNXQ7-dkwDZN5uGuLXOJ1XE-MVnT95m1ifwjui9nNY_bmxJyJ4PvHsvdBG7M0tZTQ9RxdsTVoUjfvVxP12zXGkEPOAdHV1j8fL83uVDNdFmpm5nyP3dS4SJhD4Wp59TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48060b8592.mp4?token=XmnqvaVfoTG_8SPk1kFNGgblc7XQtF6jSmIoB_2rZyjO2y-Ddc53JEKyEZR-rZBO_Ku5Xl2wQaDpU7EWet1eb-pEI6Kk1J7g-aIB6r6DGiSQ14BeXT8cPN1oD2ehDuv-DtBoZ__RHuSPFRL0qT8NYGHJS9hsecZCwadVhGKWyV4jKcjQrFcj9lx3u8mDfISu1TPwkc3gi0Wqp2KlNXB3AlWNXQ7-dkwDZN5uGuLXOJ1XE-MVnT95m1ifwjui9nNY_bmxJyJ4PvHsvdBG7M0tZTQ9RxdsTVoUjfvVxP12zXGkEPOAdHV1j8fL83uVDNdFmpm5nyP3dS4SJhD4Wp59TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
امیرخان چه به‌به و چه‌چهی میکنی برادر
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/99616" target="_blank">📅 00:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99615">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtldyV4En7496hhFUgJUBwavSJBDolfo43qGUjyJGt2zoqlZFdqwSI3ud8JkgySyHvacU36sKD_0Ja-hpCza25t1YA4v7WXCj9nbQ1363syLfn74T0RPkHshSCVzQ9rGV7TjizMovwL72ldg4uUfmNnOJgxq8DY_DFbEgEGzPOlwVqAw3sNXD0DbiN9vANCCSDiesCgNs29jaCtrHrsE1kp88bhNi7qp1RuZjUcqfmU_8nXfq5TzuY1wfRCixseBxZYtuH2dlCJoFnvO83cdn-1dRDBucKCthvPaKh-N6QIJcps0u43BHVhZSvcsK2Yx_n_V62k6dux3I943AGfSOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🥶
رونالدو مهمان ویژه بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/99615" target="_blank">📅 00:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99614">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nb23tLGursXFv6y2SIVWgymPiPyrFFsq4dLCUIZuOxfEvDr3hT-y6Dhv3-py09ufjhay3gy5l-p7plipgGwrqJFb35zuPMDJwus1fvQ79ea4t6_JAivuaoA829bQ13t2xqI2rZQN4ybF30r8wMlWb6N9IVZbXKRzlXbjFt8P41u5Cdwn9pCkna9wS-MghK790z5NnFEb5dgKJPsMkE0DmYBPsERGS_EsBzBnLAqpytaZwgcG8S1EZzjgmTDvREdcjrV0LV4n1K8sJQ5YWEsk7N8CeQT2TzgKkvekLIXmQsQhnUZpDZoKZoDkL55VaUfFn466chyoJkV7VAbEg7pRSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاه میاد با لشکرش
🥶
🥶
🥶
🥶
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/99614" target="_blank">📅 23:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99613">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzGSqZhHR0CXYdmMhhDN_LvAmy0Nfsi5xVBLoiZvOX55spbIdnTOiE6joyLAYYlbPoXQz0LwWtYigMdyfyZrBEZ2fCDTxBMA1XsqLBN05eE7dVvbNAYblX8iJjUwt4AFHRXjwuqtzel4gu6X0B9IUoSFyrASI94dL8NSzuo1qj8qLJ0VhNnyjqVIM2wIWzljuJ0uaQBlrljj0dw-Vv4aydIBvICZVkPLrP89FWNkg4tdxkQigWhlx8wKia4zHSKlI3RrTAMcJOPRkw6gIm-luGbKmcax-1SJ-A6Nfd3ATmHDvxODfyLwnPwl-izf_a98m2Jo-5UkHPCxO4dML9xMQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابهت داشته‌باشید
🥶
🥶
🥶
🥶
🥶
🥶
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99613" target="_blank">📅 23:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99612">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cde4757921.mp4?token=G3GV2IwKSQF30jTFicJhnCKZge9AlzUXv-NqJGQJxlB5vjtubW3f5kqQSE7GpjInYra3MvlzXtulcgdsYqoz1rJyqgDkVQDn3Ffp9FAmpjg82TIOMObdQVXGVwzmz4_AfEsYTRe9t6rPlQhtGiSKzqq_HMW1SJD2j65TxFXtoG4xUd3H-Do6Z15E9-23QkPE33cz4KyAwtfHzOL8fxFo-TPLS4SONRjgz3l5-JzPuJ4hLkRPNsBGUbPsIfc1z_BWBRt2dawOjFh22eJk33qi8OCzOoLF0G2JSJrxEpotV1vnKT9BCKECxHoeTAOje0zrx_fRjJV7By2cI6nL_Ugk5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cde4757921.mp4?token=G3GV2IwKSQF30jTFicJhnCKZge9AlzUXv-NqJGQJxlB5vjtubW3f5kqQSE7GpjInYra3MvlzXtulcgdsYqoz1rJyqgDkVQDn3Ffp9FAmpjg82TIOMObdQVXGVwzmz4_AfEsYTRe9t6rPlQhtGiSKzqq_HMW1SJD2j65TxFXtoG4xUd3H-Do6Z15E9-23QkPE33cz4KyAwtfHzOL8fxFo-TPLS4SONRjgz3l5-JzPuJ4hLkRPNsBGUbPsIfc1z_BWBRt2dawOjFh22eJk33qi8OCzOoLF0G2JSJrxEpotV1vnKT9BCKECxHoeTAOje0zrx_fRjJV7By2cI6nL_Ugk5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🔥
نروژی‌ها فارسی‌زبان در حاشیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/99612" target="_blank">📅 23:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99611">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/99611" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1میلیون شارژ کن 1.200 میلیون تحویل بگیر با پشتیبانی آنلاین ۲۴ ساعته
😍
🔵
برداشت آنی
👌🏼
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی با
دسترسی راحت</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99611" target="_blank">📅 23:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99610">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYdZkY8rR_JkYALN0SKFh2utNI1lddD0CKhDVj30BtEW08BPVmS3h0ABcVgYOrpckNSw_V03hEmAYhigwBUbRuUwPWq1n8Ye8af-y-icrHyh5zYFGI0PbV11dsZbYml1sFoMP3DmDKJqmWrm_CwFThpbE8MvYKcnhYt2nxrH10Z_t8rThlJ2iTZsnHu6QQcPey_0XVcjnV3HM1LecfVLe8Og8c_F7FbsMSy6KeHFSXqnn6DTP7yXxYod3FgtgiT0y6yfWmb0r6ggKUEJYoMuCBLSP2M6QYzYz8F0hji_8PHzyjRCatiZFfrG4JA1ZXjYiQA7kaXTbGIVkE3fxFSI0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تنها سایتی که توی جام جهانی هوای مردم‌ رو‌داشته تا باخت سنگین ندن
⛔
📣
خودم بدون نگرانی از باخت شرط میبندم با کمترین استرس
🛍
از این لحظه 20% شارژ اضافی همیشگی یعنی به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان بدون قیدو شرط میده
💰
🤩
🤩
درصد هم برگشت وجه در  صورت باخت،دیگه چی میخوای؟!
🌐
betinja.bet
🌐
betinja.bet
کانال هدایا
a20
@betinjabet</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/99610" target="_blank">📅 23:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99609">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ffabc857.mp4?token=fN8Alv6b8eodCRPzjcfZlyDjEZ0sADgwGQlcJzXmvIFVI9BQUBM3Q6FnQ7Pqtk9pUcY5B9gpxRhXCaG1tKg3ozj5H7GF9AfrUB_U8Z2L4ik4FKQoJRXP1r-DNzB_sHNzrH44W17h7BlcXhh7B2iC7Z7MPOm9axYEM_ZfPweGB5UZKgP2ehtl-h5D2JWL79yn8JEOeIDF6XrphO8vrPI1KeEsNNPMi32cnyyy-W8Aq_9aekIYWTp_H9D5NLQJuZk7VfX0t9QNCqmbHdHLhM36JgsMJgJjTCOuVzQqAeEmi7ekYpbN7SddFyFlBJZqBB5RK8KTW1Zfm3XjyC51BeLtEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ffabc857.mp4?token=fN8Alv6b8eodCRPzjcfZlyDjEZ0sADgwGQlcJzXmvIFVI9BQUBM3Q6FnQ7Pqtk9pUcY5B9gpxRhXCaG1tKg3ozj5H7GF9AfrUB_U8Z2L4ik4FKQoJRXP1r-DNzB_sHNzrH44W17h7BlcXhh7B2iC7Z7MPOm9axYEM_ZfPweGB5UZKgP2ehtl-h5D2JWL79yn8JEOeIDF6XrphO8vrPI1KeEsNNPMi32cnyyy-W8Aq_9aekIYWTp_H9D5NLQJuZk7VfX0t9QNCqmbHdHLhM36JgsMJgJjTCOuVzQqAeEmi7ekYpbN7SddFyFlBJZqBB5RK8KTW1Zfm3XjyC51BeLtEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
این ویدیوهای ساخته شده با هوش مصنوعی از بازی امشب نروژ و انگلیس چقدر خفنن، استفاده درست از هوش مصنوعی یعنی این
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/99609" target="_blank">📅 23:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99608">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRx07MZaX97_GLKArnos4G0CfDR_ztSWV0eWQa6aHxUwu2MiDYlRnWY8giOgtHFBiy_VzYfs87xrAgmaUzNK7QNYQK32SzZ8CFlfy0d_xNvSn7YEfGpIUaZlEIzsF6j77bDwIEuf2CzkwB2w7xTeqZgNWRkHwiQrRF8NFwWBsvmvSeV4XeOnH-2Lz5iXbWFGkGO0RkD3o2yc5Hl-QrAWzZMjmVEnp0knHamGu6t16x4_0UGaPe8YGPE-YyYpZp5Ql3rUJZw2OE_d--kIkAxQEjMVF6o7R6BiJjAd3kWheT9ud8ktBitnYtdsGKPO-_e6qL20ODu3esbWKfPP-dHDBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تیم‌ملی اسپانیا در فینال یورو زیر ۱۹ سال با برتری مقابل آلمان قهرمان مسابقات شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/99608" target="_blank">📅 23:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99607">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjMVQOonpcLL3XfWdDYfN77gGV5GOXt8zHsoOPACgJDgHDVl3TflIJoHUGDDdX0aHRFZZfe-a8pbLbte81gXpGA7yRMO34aBxThjzKMYV706m7nlfxOb3r0D9mAiU0ZQ2a0hOIQigHw0P0HnK0zt0UBdjbEpvY6o_kPqKhuEjGUI-Fr8IdeL37Ol7iKy4fesqTfTzlA8nkiRA_y1k34O5H9ayImVjPLIGHeKLic2vFb7Fc-Dl0grpsB2cdoiba42p4yFpAlHklhKIT86kiaNcGk5gmJyplZUjP5vMc8P1XQJ39oTb8Zi8Rcrw4Yml8NXfdBJ0NGxYwonEDTMeGFYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جوردن پیکفورد
با حضورش به عنوان بازیکن اصلی در بازی مقابل نروژ، به بازیکن با بیشترین تعداد بازی در جام جهانی با تیم ملی انگلیس تبدیل خواهد شد و رکورد پیتر شیلتون (18 بازی) را خواهد شکست.
حضور او در جام جهانی:
2018: 7 بازی
2022: 5 بازی
2026: 6 بازی
⏳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/99607" target="_blank">📅 23:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99606">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1x_o_VXIwtvefMm3as6felqOEPgLW-wFPmkx5WpasWC6ZG5LEmFZqkQUepl82n5CsUEGaRSMaN87BHBQVS2CT2czu9euYA8Gcsua6aKLsdurwLk1tECI9da5fcI5P15BZ_2xTINqAds19CajcYpZeV_T-GF6vgkBnsYmAGJ1v6UijPPCHiareYfUiNM5AVNzYcDqq60NSOqp9S251ENNcFDV6_DVYIjOecw-KapTEDH7Scb_45DfUfoaBjPEMr3SsUGtxboDg7TY036Os2Qg_wldPxGTvvfiyQRvBQZ-HTYMvAW-k_1jfk5g8SIv9elskvlOfbrlexYj7p-e87JrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
ترکیب تیم‌ملی نروژ مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/99606" target="_blank">📅 22:58 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
