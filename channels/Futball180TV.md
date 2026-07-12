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
<img src="https://cdn5.telesco.pe/file/ATROMVnxPMC5NtpmvHo4fvTSBY27R_jgdJyJxdRwHbjyGUIcdzJTyQS2d8yfyU5wdgM-ur0Ny5X4w9Oa_xzB79xZTE1umRa3Mezmo5wJo-9q-cLWkXr9pG8RtAAWtUVrnSDwye1D7tTFz0qS2LxQ6Q49d2AqYCNS0Lgn6vDGhje3vY6AsbnWTrMTvquWbMwCn5_XDQgleoZy1P04-3YTsFZZnJQkybScxHjrRLTju098meOPOQo7clwLBU5j9p-g5u7MLpr22ltQfydPUUcwvzjVWdgNMfOJOK9KCJE2DL2vii1G_dvBZ_WZHnV7Nf1jny7uP3lDrkokqL5QPMG0RQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 590K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 15:41:54</div>
<hr>

<div class="tg-post" id="msg-99822">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3eeeaa3f.mp4?token=n61LwevsqWeyCpoxpg2h0bc9WSCMEgmfd-f4mv8-CPKXb5kXlfWsSUFAm98RlW5WQ2EKfYGHsBkC8uEjCNrouvsrmFLqUC6Ze__wo-J71VsPvSE174SwvxU4KizoltSYqbBtu3m7N0x_licCMKV9Q3-WVQti3yG-f4OveY3c_VeWZXFH2lLuk0PpV3SsgUHK4HPCMhufqk4fXblpUKoxDHAU1BdOqUylYc28RIwPEAz9U06z8NBUmBnJQOpAp9HGoqUmeip1usIKXylh7awF5n7HqFgZYuS7zr_4FSI1fU2OhkBqkIaZ1pil8QDZdytOjA2KoKGYJB1xYT8LSxSakQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3eeeaa3f.mp4?token=n61LwevsqWeyCpoxpg2h0bc9WSCMEgmfd-f4mv8-CPKXb5kXlfWsSUFAm98RlW5WQ2EKfYGHsBkC8uEjCNrouvsrmFLqUC6Ze__wo-J71VsPvSE174SwvxU4KizoltSYqbBtu3m7N0x_licCMKV9Q3-WVQti3yG-f4OveY3c_VeWZXFH2lLuk0PpV3SsgUHK4HPCMhufqk4fXblpUKoxDHAU1BdOqUylYc28RIwPEAz9U06z8NBUmBnJQOpAp9HGoqUmeip1usIKXylh7awF5n7HqFgZYuS7zr_4FSI1fU2OhkBqkIaZ1pil8QDZdytOjA2KoKGYJB1xYT8LSxSakQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عیش‌و‌نوش محمدصلاح در کشور مصر بعد حذف شدن مقابل آرژانتین در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/99822" target="_blank">📅 15:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99818">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDi_0JQGS79_z2FiGdqQ_phmaccs0IF4nS_98vpGBBJDpZ9r33ReIvZr0eGXVKRt6x-FqM5WrC9m5259jW_hIqhKkgr_Oa6rkurU5Uh4R55qcUksQSGfUPxVFAbhdg9L27ujenG7WU9ADKGR3Ny0_GGhv3EN-wzor9HwXhqb8zxQgWiaBu7domZEUuyPh34_PS1yDSsmX-GAPISiGj5MhTcYN3ueQTZdYvacFD4qoguFwrlR8NRtxsPSMYWJyHqZdOVXhK5SeF25ZB_gORs5cNJ_epMf3zYmpHdR-uGv72PwXlLbzNcENVAB3m02tYBORwUeiu7pHFthhvzvfgGXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJoqnVx_5jImmAN-aMNMsDpcENshYtppQE_195ssOEDU4x1lg-i8DrHdMVY8X4YUHSkpyEr1qoDWAmblUllblCRjwl5MVLO9D34LxU2k06z_sq2MT8uaLUGT9Vkofu8ZeXW9B6bJoG_3ww_3LdI5_pgRfH2iF07rg-O1aPjFIEjyu51s__xX5-oYFnESz4GpPGwrsQfLAJtJFf5ulWY7t_AKInkpvjtCf4m0H-OhzAbhtTUkwW0sDrpffy-LPA7vBAtaP2tjPz0xy5M5NqFbGWpQAZv2l1N-PWXuvKWpBL0Kt4eYTIgXVg2ar93ePugb5acq_sAFVaQcecNsoSNzrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qtV3xZJvbMvcmnQjAM6s470-fYJ9DInPelOTd6haOflfZa1KzZ5_xCKakqh3lAnR2-82p2E_MFGrJ12PdDaTOWQgrp8RkDuzGMK2vniq8Q6-Df-Hr7yDWRkyKPihNwhJKq0YNex5-WUfWgZKnVvO2XmTnkzAqe3FluPk51TEec4LLCyLljEwt6FbJivDswibKb4mu3-Ct2p4dT5jU0rYuaIxEdDVylOQRhH2DGZKm2tBWqO8mhffs8DvGJgeTnyM76e3ciUe6lsR4y4smFySSz8HO4KFnAvF2GX73drx9zl0btadkLZz12HYg2r5CHdkA_FMm3XfmXCujvnIYe7yyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJ3TMRGBVQMC_BtMF1bvtXU2RE2kYfsqc9rYDtsmComik4oXrj-jJnKFwN7ve-T0OTgGzMXchXklQI1JApf-C_J5UvoJvhNmA7Za5H4ebwMV5sU95a4vCeoOR6OVxnAF_oB3dVahwz4WhXC66ZQqVIi9-46booNAk-GzTUiZgoK_8_J4b31WtkE-TtGzpwNcEineHx69FZn6rwPbxIiGp1D2eUK8gcEruXxeZz3DbA__x5urs_c6p6C5uqWf4vPwIOtfgRBiBNwoJbgoTL85ZIOschshdrNyglLy7Ycp2qsNAh6kzYHgFzqIbPlET5StTqnMS_368ChQj7e4F4JqnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
استادیوم‌هایی که میزبان ۴ بازی باقی‌مانده جام جهانی ۲۰۲۶ خواهند بود:
🏟
• استادیوم AT&T [
🇫🇷
🇪🇸
]
🏟
• استادیوم مرسدس بنز [
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
]
🏟
• استادیوم هارد راک [بازی رده‌بندی].
🏟
• استادیوم مت‌لایف [فینال جام جهانی].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/99818" target="_blank">📅 15:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99817">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgEoahr21yMnRcBKhweHlkLqgcm1WAC_DlhP8mMvOJRuWvlExrmSTJweZo0i3NLfay-1Q3qwYlxVQyi_5ouD_d820bopJNSAv1u4s5KGeQ31wRlZ7taau1QLchikGjj5aMGIt0tTyQEtJ_swduI6D-cfxwW9l84_BmA-Y9ZcZVxCdboCCTvBWCL4bKGs4ygLUsIIDiYul8KiZKaQqP4VPlsyhD68aFMtwAqNtOUlT-aVWRKDbgSi-EEvNJt-9VhtTyo8oxPqgcxGNzwpSXMRPuQXjw07MIQ_HQh3yZ8SE9sBMyILLUibfdEITuRQWJXTVzxdB_s7I38j12gSNe_8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد تیم ملی انگلیس در آخرین تورنمنت‌های رسمی و بزرگ:
🏆
جام جهانی 2018 — نیمه‌نهایی
🏆
یورو 2020 — فینال
🇶🇦
جام جهانی 2022 — یک‌چهارم نهایی
🏆
یورو 2024 — فینال
🏆
جام جهانی 2026 — نیمه‌نهایی
🤔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/99817" target="_blank">📅 15:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99816">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41a3c293c.mp4?token=kqALw6-0FO0Bt8BBMzNi-OkZmKTjvGDfiR3BvtC9_R4LADR8YzK-s6IRcj6uU6TK8ipP9jZaHSby2yg2aNQCz3D04O84JkTRbhuzXvDj84PmfH0mfyZ9QArCjO_qEWSm5Rc76rsbZbq0jLNn6gXLqQE5HRDUekDL-StEKOcaJYhj1s0n9Luuwner2HuePHtrO8kaleE7uUGixJcaLbFhI4pe_yArxuCp4sviiBiRBWUSyxBk7NOIEOdQdG5FgI4aBoSxEt6lGJy4Fkr3A7TtHp6uliA0F3IG3ttN6ScqgjFys4aUF_tkUzbMvoWp9x9LykfEDwHKZ9EF_U1qTbTepyAmZj4nnWhzQPWpJalsR26cfPPuGnFPBp1j0tGQL5NWqwLRkYypE3dN82qX-xO7ilDaBFy-HsVk1KuXdgoC7xUQumn3l2zQv5XFaNR_yz9kk02QKFC6siY4jiimS-x0hM48dKHYbv6SHNt0SOEWMT9e2TbORkwZ917rjrh-MpET2ga_4149zd5l_OwzsfYKM_2G2oZYwUh3vwvXfe5eUrSvIuN0Ar-9qWw3Rq4di_r_-C4lhUaQ-KzObfCpQ6lpZWb79VEFeuS7NOnBJifgWAVSamPCr9aW8ATvzOwVqQFqyaqb9Xsyx2vLSWkhaXDyiLo5mhQo6ofPJVUcmP52tmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41a3c293c.mp4?token=kqALw6-0FO0Bt8BBMzNi-OkZmKTjvGDfiR3BvtC9_R4LADR8YzK-s6IRcj6uU6TK8ipP9jZaHSby2yg2aNQCz3D04O84JkTRbhuzXvDj84PmfH0mfyZ9QArCjO_qEWSm5Rc76rsbZbq0jLNn6gXLqQE5HRDUekDL-StEKOcaJYhj1s0n9Luuwner2HuePHtrO8kaleE7uUGixJcaLbFhI4pe_yArxuCp4sviiBiRBWUSyxBk7NOIEOdQdG5FgI4aBoSxEt6lGJy4Fkr3A7TtHp6uliA0F3IG3ttN6ScqgjFys4aUF_tkUzbMvoWp9x9LykfEDwHKZ9EF_U1qTbTepyAmZj4nnWhzQPWpJalsR26cfPPuGnFPBp1j0tGQL5NWqwLRkYypE3dN82qX-xO7ilDaBFy-HsVk1KuXdgoC7xUQumn3l2zQv5XFaNR_yz9kk02QKFC6siY4jiimS-x0hM48dKHYbv6SHNt0SOEWMT9e2TbORkwZ917rjrh-MpET2ga_4149zd5l_OwzsfYKM_2G2oZYwUh3vwvXfe5eUrSvIuN0Ar-9qWw3Rq4di_r_-C4lhUaQ-KzObfCpQ6lpZWb79VEFeuS7NOnBJifgWAVSamPCr9aW8ATvzOwVqQFqyaqb9Xsyx2vLSWkhaXDyiLo5mhQo6ofPJVUcmP52tmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خوش‌شانسی یک‌آرایشگر در حاشیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/Futball180TV/99816" target="_blank">📅 15:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99815">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44c1f00871.mp4?token=jH_sZxAUsTHUmlRF56YMeXne34xvYR-mzjuorhht6rTUaI2v5EkF_9cRy-MGM7O0ytTjqbVBGrUV7uSMFZJs795IV1Mb4JdUcorWD9Y2dkJiYXQ9HIwUCq3_HDMBdrirtJk4zc-1Ep_UkvkSiI6wpCyfVcX5anoaOa9lUP3oqriIWWogSIv0FRF7Kh9RHDbZHCP_D_z9a0u2aGwbNvA8c54rnQoDgUaw8iFFrUVD9MN9Gu-58CTEXN6zUv6cKsA926KACVn-zGp5hGnqn_PqLTL90bSS6eeEoZ6v5bQ-4mxzJcTGc8GR24ETtOdWJwmiN5H2HhkbkSRtlsAY_L1jiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44c1f00871.mp4?token=jH_sZxAUsTHUmlRF56YMeXne34xvYR-mzjuorhht6rTUaI2v5EkF_9cRy-MGM7O0ytTjqbVBGrUV7uSMFZJs795IV1Mb4JdUcorWD9Y2dkJiYXQ9HIwUCq3_HDMBdrirtJk4zc-1Ep_UkvkSiI6wpCyfVcX5anoaOa9lUP3oqriIWWogSIv0FRF7Kh9RHDbZHCP_D_z9a0u2aGwbNvA8c54rnQoDgUaw8iFFrUVD9MN9Gu-58CTEXN6zUv6cKsA926KACVn-zGp5hGnqn_PqLTL90bSS6eeEoZ6v5bQ-4mxzJcTGc8GR24ETtOdWJwmiN5H2HhkbkSRtlsAY_L1jiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حذف نروژ از جام جهانی به دستِ جود بلینگام.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🦁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/99815" target="_blank">📅 14:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99814">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpYBYO4VVUnOJsj5sKabYxcn4TFBW3TlbgqQdSrgFT1zkRkVNDkjCCoQJ_qOf3JxuXrOvOhthHtAIPz8p_vS6ybdWA0qObxlivMW43km9kWhXPp9aLuRnfL6TtbC46-0tZkskPjBBvhGT55bmcJfolYsg02W94GFCag7ayEWy91B3cQm0lcY3uuuJ7cz00CJ31eXGLOYn-KMOW3tsy8qBUWy8qHUKCj5VY5K7uVRGGOrbQvSaiCKo-ySLU7zgfpI0EkTVXtShMB353CHNXNVlMByu-Drrv_ncJWdm8hNXYXwQvHSB68WWVlQQuPfljqgwFjgIPW2HHfx9dfvub5RmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از حواشی زیبای بازی انگلیس و نروژ
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/99814" target="_blank">📅 14:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99813">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3480a720.mp4?token=a9hhWWQWYsq1REAi-mcJDdKA-McSyoy6ut6fWQURfMACR7vKX4W4AIn8olN6QHHkUbLwrhTBtnHvTrmLjpVT-MWR2dzJvFui4dq-FO6nt0YuvN_anKWvG_NDvH263xxY88VU_1VAYmqoMqfAf-mAKtwaJW67GQrSQIDhwy8MTvfpGHXOn7AyZbF7n1KsmIP9c9R_gm6snGyOCpr3WNPivB2P84Qm4e4Tu_oy9Fy-bsfiqRGeiv7mLXwQTXLrFqg8pTDuIvpY_YTj34fU-jLVlgZ9t0hmrjYURoTV8eoGBNJEAPLXKrmPkPXUUZnlqpMpcDjg6pjSMcOpPCyREdiUXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3480a720.mp4?token=a9hhWWQWYsq1REAi-mcJDdKA-McSyoy6ut6fWQURfMACR7vKX4W4AIn8olN6QHHkUbLwrhTBtnHvTrmLjpVT-MWR2dzJvFui4dq-FO6nt0YuvN_anKWvG_NDvH263xxY88VU_1VAYmqoMqfAf-mAKtwaJW67GQrSQIDhwy8MTvfpGHXOn7AyZbF7n1KsmIP9c9R_gm6snGyOCpr3WNPivB2P84Qm4e4Tu_oy9Fy-bsfiqRGeiv7mLXwQTXLrFqg8pTDuIvpY_YTj34fU-jLVlgZ9t0hmrjYURoTV8eoGBNJEAPLXKrmPkPXUUZnlqpMpcDjg6pjSMcOpPCyREdiUXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
کنایه عادل فردوسی‌پور به عادی جلوه دادن شهید شدن مردم هرمزگان توسط صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/99813" target="_blank">📅 14:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99812">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🙂
اگه جام جهانی توی ایران برگزار میشد
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/99812" target="_blank">📅 14:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99811">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2495db55b9.mp4?token=armBEa9MG8f89eDSzsTSe2O1uRvS2e-k1aZbB6pVyhcAsgC_7HKJnCtOKdqSrQXFDGUXTUdPvnqJxRSEf3SiNBdAfhelY3CszQjZOTa_oBB1xH1iuNV5dK9CxlX5nohLyUBivpgKNbJLu4GXit9gpflPrVwY6uO_hnLLiQ7ZngtYGshF_u_xAP1-Tb0ZbnX83DMNatTnQte_GtebAYQTqcHp3HTslA-Vxvy9NZAYPoqG0FD8R8bsemoT8bD9y_HuBZQx4orTgQ__NMBmfzozEkH9jh3x6S3vbtk7lBAX9u5LPlKTOlKkvDogBr-XSRhz7dP-V1avnIQcDpBV5XduFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2495db55b9.mp4?token=armBEa9MG8f89eDSzsTSe2O1uRvS2e-k1aZbB6pVyhcAsgC_7HKJnCtOKdqSrQXFDGUXTUdPvnqJxRSEf3SiNBdAfhelY3CszQjZOTa_oBB1xH1iuNV5dK9CxlX5nohLyUBivpgKNbJLu4GXit9gpflPrVwY6uO_hnLLiQ7ZngtYGshF_u_xAP1-Tb0ZbnX83DMNatTnQte_GtebAYQTqcHp3HTslA-Vxvy9NZAYPoqG0FD8R8bsemoT8bD9y_HuBZQx4orTgQ__NMBmfzozEkH9jh3x6S3vbtk7lBAX9u5LPlKTOlKkvDogBr-XSRhz7dP-V1avnIQcDpBV5XduFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
🇫🇷
حمید محمدی: اینکه کادرفنی فرانسه بعد از این نتایج درخشان و رسیدن به نیمه نهایی جام جهانی بگویند بس است و این سکان را به افرادی دیگر بدهیم بسیار آموزنده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/99811" target="_blank">📅 13:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99810">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8bf3f6a7.mp4?token=uyouTozlEr4kUZ-tVs0zhinuT7kot33yMEynDQMlY9NT2gN8YcB5mheJx3-2T5YbIcVimeLB3GKbcvpI8YOkGEFuMTd0v5J1sKQE6E8jgToauJGGXlyrJhoTaM-ddtPagR_jBxpkUt2D6WLTEAYPPYhwRKgNkqM3fqyuWa-To19mSJ-puZA3uS6pzHq_-U5_gC6zTDlt-UujPGGRdYkkl7-uUhwws-TkjJF25ZGXUItNzH5VT4TIusqvrlBm898lTGPcjqQEafd6yorXWYB-6Qw6tF9vlZDmtPHEq7Vo3gLsSFdZdAHYlpCpgHecDtF09MFyKm6mhirt6Evkjxvq2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8bf3f6a7.mp4?token=uyouTozlEr4kUZ-tVs0zhinuT7kot33yMEynDQMlY9NT2gN8YcB5mheJx3-2T5YbIcVimeLB3GKbcvpI8YOkGEFuMTd0v5J1sKQE6E8jgToauJGGXlyrJhoTaM-ddtPagR_jBxpkUt2D6WLTEAYPPYhwRKgNkqM3fqyuWa-To19mSJ-puZA3uS6pzHq_-U5_gC6zTDlt-UujPGGRdYkkl7-uUhwws-TkjJF25ZGXUItNzH5VT4TIusqvrlBm898lTGPcjqQEafd6yorXWYB-6Qw6tF9vlZDmtPHEq7Vo3gLsSFdZdAHYlpCpgHecDtF09MFyKm6mhirt6Evkjxvq2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکثیر ارلینگ‌هالند در سطح بین‌المللی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/99810" target="_blank">📅 13:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99809">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5445db9621.mp4?token=GBY13G4VY2YWPZqakkkoiOw7-7tdU7GFWDsmgyaOYPxMOX3P-skj4nJakOMDL3dHACSABcsIHqdzhgJeXdmIKqybzuYd8XPSUiB2cPbTHa0cWfuPwefjIYhDXNjuR3m7lhxIF4T4IWB-UGDQjZ2-Z_6ohz5Wckfv8QCMlihmxTzbumr7xfbbc-FDSzy1MKAXW60cbrM-CgWKrb0aGV3wL2hX6HvfQjC8JThHV--Pzu6dKZ-rjx1b7ob-0S_K0jqg23uJ-Q_ytNiHixVe6-LJ-usa0k-HwJIGgYJnljfezupDmJlkBBbyOa3BdHP3btZs1ohyLTf_gw_rCng_XswLvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5445db9621.mp4?token=GBY13G4VY2YWPZqakkkoiOw7-7tdU7GFWDsmgyaOYPxMOX3P-skj4nJakOMDL3dHACSABcsIHqdzhgJeXdmIKqybzuYd8XPSUiB2cPbTHa0cWfuPwefjIYhDXNjuR3m7lhxIF4T4IWB-UGDQjZ2-Z_6ohz5Wckfv8QCMlihmxTzbumr7xfbbc-FDSzy1MKAXW60cbrM-CgWKrb0aGV3wL2hX6HvfQjC8JThHV--Pzu6dKZ-rjx1b7ob-0S_K0jqg23uJ-Q_ytNiHixVe6-LJ-usa0k-HwJIGgYJnljfezupDmJlkBBbyOa3BdHP3btZs1ohyLTf_gw_rCng_XswLvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
راز جلیقه‌های هوشمند بازیکنان در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99809" target="_blank">📅 13:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99808">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmkrcCbbNXMOs892CHpxvyNqxDRKLf_FPo_fonItp4YKudYtByDBCBjsfK9y02tXevONwvNRx8kPx1IDxqTeTDlg6XXiemtOoGzii6TT0E8DOk2DvMVjxJKsoZ4BAYmo6DT7n7UKUmoDXgiA6q9hCeD8zDAF9r8h_U1AqghKwWjhBSjML_mhA41M6AFSWu0VUzQDDtlBxc3HS_gUp3KVXz_RuboDKM14v65XrxIYl777KifBzHQREBJXqpjw2s0rRdSv6EZ6D7surnpbLisRc8Q7qCyqVVQo9g7-wi7IskxTiYgSKuSF5zZik6X30grqtJDTUp1pUsuSZot-p_cwaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
• درصد احتمال صعود تیم‌های راه یافته به فینال جام جهانی (بر اساس مدل‌های پیش‌بینی):
🇫🇷
فرانسه
- 58%
🇪🇸
اسپانیا
- 42%
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
- 51%
🇦🇷
آرژانتین
- 49%
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/99808" target="_blank">📅 12:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99807">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/99807" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">❌
با هر 1 میلیون شارژ ،
🅰️
🅰️
🅰️
هزارتومان شارژ اضافی بگیر
🅰️
بدون‌قیدو‌شرط
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی بدون فیلتر</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/99807" target="_blank">📅 12:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99806">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYcvpu6iZobzPXiCrb0RvKxAWxQNBQKLGip2zT2nIT2B_2PR5HTw3bw6rH-m23JnKEd0hVQaY5W0junrVKIDTJEVRcDP5z2k1knOlmUnjG7y9U-5Gia8co1iDvp_v887Nnno83Je3I3HlgCEYO-Gu2OMrMfOBr9SQ4mUE-iZt-kcI0lurt30fOXhnw4ADzSWsBAArlHdW1Vc14aey9nf4ijmYg0tsVe4lMYmi8XhCXD9ykhqbmowvAu6K5QyIZZ6W-V1pyzDRFBkMqlOKSE_PvSVxg7Msds79eNCGi3xAAejZ940706Jcd4uIDU43NUeinkaMcBvHd2xRRrfGLYX3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تنها سایتی که ریسک شرطبندی
🅰️
🅰️
🅰️
آورده پایین#بت_اینجا هست،بخاطر اینکه :
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی میده
+
🤩
🤩
🅰️
کش بک بابت هر باخت
🏅
بهترین فرصت سرمایه گذاری و چند برابر کردن سرمایه :
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r21
@betinjabet</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/99806" target="_blank">📅 12:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99805">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22252f139a.mp4?token=O9lx6CsmyFFwImgIwWPz_XGCm7ONdJCZo_CJcMcbzdU3UeQArhzFkTqr9ucmGz_bh-F72a1wAfzHuDLC6rstPaCxiVY9Ub4hDSxpPf2HM5OV12ee2qFiMI_jStxEYN9tEQIaJNFEaXsWunyNn-IbmqbDhRQr3TnjbilYoHt2ma3DHOrzi_aHPswh5AxnKTk9IxkBmVSGo-_tq5KqUssPnb5LBKT2MjpW-6iebBT1J-lHPPJCQeBSEcaID8JyKQsdgXnfru-EI-YIyQnuK_GgYrw7CfhiXXGD93ZKP89zpnXuukabmrbmPvjGMhtP1mwlSHjS88s3srrim9OtvL3Lt4NSfSiHPPxELjY9rBgklTAb2zu24RJNHeanze1xAyui3v3UtUQruJPEUldh4Ptx8p_pf4FHmPvTUL0uBSHlvb48_9ooIQssM954vRw3OkxMvyKJdXlGrEAVrS8Y6RHwCMJyY5I0p8dwL2BdzTloFb0dsdld9XzcwA-l4Q9Hz8T_qcT8SHOd7_BsI3AbKJH2g0pGstk8rPkSWJfV0-Z3hLfIUo8MicvvL09WxeX541mz_h14lzTD44IPUU9tlfa76NJknH6RPb9rlUAhuPiGxHb3URYtAwoR2HeCQppma_NB_5kck1ZxNAN6SzCgbCbVrqCIx2lLI14cu2thEH42LSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22252f139a.mp4?token=O9lx6CsmyFFwImgIwWPz_XGCm7ONdJCZo_CJcMcbzdU3UeQArhzFkTqr9ucmGz_bh-F72a1wAfzHuDLC6rstPaCxiVY9Ub4hDSxpPf2HM5OV12ee2qFiMI_jStxEYN9tEQIaJNFEaXsWunyNn-IbmqbDhRQr3TnjbilYoHt2ma3DHOrzi_aHPswh5AxnKTk9IxkBmVSGo-_tq5KqUssPnb5LBKT2MjpW-6iebBT1J-lHPPJCQeBSEcaID8JyKQsdgXnfru-EI-YIyQnuK_GgYrw7CfhiXXGD93ZKP89zpnXuukabmrbmPvjGMhtP1mwlSHjS88s3srrim9OtvL3Lt4NSfSiHPPxELjY9rBgklTAb2zu24RJNHeanze1xAyui3v3UtUQruJPEUldh4Ptx8p_pf4FHmPvTUL0uBSHlvb48_9ooIQssM954vRw3OkxMvyKJdXlGrEAVrS8Y6RHwCMJyY5I0p8dwL2BdzTloFb0dsdld9XzcwA-l4Q9Hz8T_qcT8SHOd7_BsI3AbKJH2g0pGstk8rPkSWJfV0-Z3hLfIUo8MicvvL09WxeX541mz_h14lzTD44IPUU9tlfa76NJknH6RPb9rlUAhuPiGxHb3URYtAwoR2HeCQppma_NB_5kck1ZxNAN6SzCgbCbVrqCIx2lLI14cu2thEH42LSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انشالله برادر عزیز آقای عباس‌قانع با اون صدای گوشخراش خودش گزارشگر فینال جام‌جهانی نباشه
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/99805" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99804">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1d299a804.mp4?token=mAGWvGBJxXZ5ZdHzDAZOtYFfh77pipt-z9sv8bP6raldVPL1cOhqONmEt75tJf6qWcmDMpZFk5HAWVlEB_NLpLbhtp2h5jdUGoi7sy1sO9zbTSeK9gyQH2PYc0Gvpi1K6WXG4HwgRn-nRrWJjs3TThe0qqIAOIqz7la2C7woqWvQ_wbAZwDVgudSf3E5cFQscZycdcvWw2syE4sHyeunr4MzsI-VnZEdo0n9b51Qb7jnoEDEFMV0oezjhiXbUjOX4l_DbSgfYaQ8zGFTSkXmbQ2jz_kWPSIUFDqYFHz1jaVEelNoCZDoB-KR1aAv8Cfhh9RQJBb-IbLr5-WRyD-tng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1d299a804.mp4?token=mAGWvGBJxXZ5ZdHzDAZOtYFfh77pipt-z9sv8bP6raldVPL1cOhqONmEt75tJf6qWcmDMpZFk5HAWVlEB_NLpLbhtp2h5jdUGoi7sy1sO9zbTSeK9gyQH2PYc0Gvpi1K6WXG4HwgRn-nRrWJjs3TThe0qqIAOIqz7la2C7woqWvQ_wbAZwDVgudSf3E5cFQscZycdcvWw2syE4sHyeunr4MzsI-VnZEdo0n9b51Qb7jnoEDEFMV0oezjhiXbUjOX4l_DbSgfYaQ8zGFTSkXmbQ2jz_kWPSIUFDqYFHz1jaVEelNoCZDoB-KR1aAv8Cfhh9RQJBb-IbLr5-WRyD-tng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😔
جوری که پیمان حدادی مدیرعامل پرسپولیس دیشب از حقوق ۲۰۰ میلیونی صحبت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/99804" target="_blank">📅 12:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99801">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cS25UgLbNq2FVs7UckUvipFuwW1f2XQYk8a2rfa1pcp2GODBqK_stor4qlqa3lx9hw08C7itTrSyory3UVnJ5UpyKECFEXqorpnVOTyUQbviZravkd_4dhSSxwS4Or-P44vfoQmanEYjEheuXWnXGatXm1sNWgWlGBMqFFmnJ58US9qvTHUgklqz7YR-K8mkC_n0eS1EJcl9ZiNCpvXCsLgAiQRpL2mzczcdfd4TdqoLcPL5XwWKgKXU95Sj6Zh0nh1451RZjVTMv4fH-ZjmJ8fzKbKhGjZyndKgewvrTg2Jk__3iNtUgUAR5faTNn7dJ8ZBkZNIGjLw3pRldZaTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JXg1yk9LG6zwXW1WC5QKQZCEiwaiKfYuPedNZgltoHQCzEAjFdnvp1QwF43mNAnPHL3965mdv3SQRitegO1qw1YXD5ivBsMFmEDjSptFBoiAW3nmMRgbG2YG1v613GxmIadVzKCJunDMGX-g0rjLSy1sTT9qmeM-_F_ZBwbiFjXT8xPsXyUkUxNPoEydb5sXNNuoDwu9dgvXDpkE66Fd4UrE4KoSgHZpdEHtlyDUDBmvM76OMrz7gXW6mUX7Aplh6MdG88QwuPy6KjLzgOGI9tpoRc40Q0AjFPckLMXJkYKG1xy4qIo_DigxyVo2pOHvXENzifvDbAcKyEmDunWMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VFL9cHYcSXZkPjty6TCnlNxV-I2Etq-U72XE9aZ182FBUN9ZiCxYCEBmwGw0OAEoXF0pMCyYfefH7mIFsA4uVfarT6YrLCS-7Q_Ev8lmgUlGaMvnShkg1eHjFQMpknDF2610xlzUe6Q0y1o9r8auVhNjpcsAj75WZgNIfTvhqDfu95HPbLo_mBwSk2Pfz2XWYbAesdDoJRnL2VHMClLG6mwKWyVgaIJjOD04motvtdvQZBoNaaDmRWBEXLvE1u8XZv7Hp9sSKLAIr7rppBtmLfUbMSEukadHOYTnXn_eCYvJuLhjWOZG7mIYsnjLlj3MJOUu7TNIgOkivAl18JcezA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوس‌دختر بلینگهام در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/99801" target="_blank">📅 11:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99800">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007eae865e.mp4?token=qt-W971kzUuOvccYpUjSobqNSfvW8TMmbonF09Uh6Pouj27tp73KdVCFlNRa0EiGJZ5-O77lWrgKPVGc-KeNXe-Zs_mT2oLQM2CCDP6KyCa7FvRk45-_zs0McHEljoDk1EDXFxJN563Ws6tl8gKb5k6Iu5ZEdL5JDem7eIxKk8BpM1dd8IOk_mS4T3IDMuscjfJ-xzdm-BhnnJg3mMvuSI1UjEGMVewhNfc0tkGH85JDXLNU9CERZ6cgEOrGpbL52RrVcjchOVnIGeAo6bWN-Uq2LPbguiBU7Z60X3gRYGIRA5jVo8Mlqke-qykjfcHIoChgAcfVNDzRFPakpWDkLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007eae865e.mp4?token=qt-W971kzUuOvccYpUjSobqNSfvW8TMmbonF09Uh6Pouj27tp73KdVCFlNRa0EiGJZ5-O77lWrgKPVGc-KeNXe-Zs_mT2oLQM2CCDP6KyCa7FvRk45-_zs0McHEljoDk1EDXFxJN563Ws6tl8gKb5k6Iu5ZEdL5JDem7eIxKk8BpM1dd8IOk_mS4T3IDMuscjfJ-xzdm-BhnnJg3mMvuSI1UjEGMVewhNfc0tkGH85JDXLNU9CERZ6cgEOrGpbL52RrVcjchOVnIGeAo6bWN-Uq2LPbguiBU7Z60X3gRYGIRA5jVo8Mlqke-qykjfcHIoChgAcfVNDzRFPakpWDkLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇦🇷
مود طرفداران آرژانتین در روزهای اخیر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99800" target="_blank">📅 11:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99796">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FXX0Z8I46-5GUnDGZcp2DPeVH7zXg6PmFxvmz90-JcQ7bxM5h4xj4OoIZeXkWiiogEwg3YNfvulo04peldKwLfOxtPzxp7U6MqyuzWUQA1Yw_SsDfKOdmSQFhBXKPKsVUU3RqKM8MZudUBkMxgwJu29JP2YGJcOj8_CW7w9BuyDEl8J54Uvx6CvTo2HIuwbc0XMePqHR3n3zWsLC1SJyXuWNbDT5Iwqd3CwDhwWcZ8oBHn0AQSJxnsdZ7gSTvaGt8Vpyn1irphLgwTDUH7GwizDOHJjxfftwF3yoIsferV7o4nHj1BNWWnQpG13lTeL4HL0jfD_nRwSEmni22K270w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hdepc5GgDhMXTQU19qh4JtWIH-q0CVtsPxdP-KOoMH7dFEc-mEy7EBiA0ZaZrpbFUtwFcCIb5zJIkVNI8kXVCo4cwrXaT21VWmun-DnDxjh-c8o2WUYUA1MtwTz68Vns3yhgs8QjA4s9C1dv9DEabDZoyt5fZU-gtQbHNu70vEdNlaRNwLGK2o442fEsVgV9jRA2HHfQTcKpyUppwcWptoecYtfaYFd79ZK8xp3HawnG6vIIgM8Dr7cJAnKhcgX_UoYHqH7xDiCew5TkbRQrhWjIXUOLcM6g3th4KAa8tbaBcdSTp5rTcIc9Ag5QK0EGBdiqCQVjnl5AzNVicBkg6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFVjOqkdSVVxh3Si4WZB75a0pdhZkWOuT5dozPH1khU05M2_cXkKGvV0lWF_c0vF4RGyBBFSjN9KHhuRBvsGpV-E2HYCz1zjU3-O-fwDqglGfFtbJklMZ5UEZUaf65I3JJ1oisQ0s412fXP3U7f2DzNDIuy-55wVnwGnNOTfowcAz-JSkVDahvSGbwrEAy0TeiOMzh2ipCU4a980Y6VBLw7zuXjNe8WeXLIh2e4UI4QFj9xAcpjsx0r-2JDarnZkflzYjofAvthQw2iP1_EStTHVcDoF6FpYlDX3sSrU8AUsCwVw0gKhxFbHiDByz17FDBDXwJaBr2zvZEUMqKfTVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IPOSodF3355N1-AyK_8cPgW8-GVhpAH0GDreoRK0Amn94xUt8BaZn5xb95zDLK-T2shMfq9eOlzmD48F6sdRkzKLfOWtDLgnEVzAiJU4nLT41GlybjnuTxEVonfoDtckFwo4rOA0g-22RRaFpruBH6_amvcg6LvsqHQYfhpyo9DmzedAdLSplsg-I3-9Vc2H24302l6PIRcX_-dDHtT1GMfJgRmqLqg311jMX1dUG7MELJJjrAq_Gmjz3ZZENCwDS_L8AIEz1_C4clercDPYOWp9vme9H7DZyNAi43TP4uu0LH3kJGqm5KNVrTW_Noc2Mnh7t1CUhXOiYUFwG7gsAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇦🇷
خانواده لیونل‌مسی در بازی با سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/99796" target="_blank">📅 11:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99795">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aaab4e8ef.mp4?token=i-Ur3SWoALiK_imXTCvxlQMCEGvBRTUmha3KtR1O2KC3asuZXGN2o2es5qMKKGNDp7qxmE7CnfmZmMlhZQHPxBwiPAcPt2MiEpubKotTb5303MqSt5CdlOwa8h9aeQJn5ANrKhULeYUL3yPWKPGuhG5YVLZC_1nbKL6_6_OEA-t_WjOuZf3gOfVN0KYg4iV4nBy7cN442ztGGvcWPW1TtOF4WWL80RupNY5dbWrOnIso1FOBy00WfYczo_qWhz9-2mcPc4iFBMNG_K5Wj2e0ihgi7cAL4oeQyoNAbST5j8Ajp84BYnJ8jAxjCb-8H7TCqUUsGVWzwAUwqFU-Tonr0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aaab4e8ef.mp4?token=i-Ur3SWoALiK_imXTCvxlQMCEGvBRTUmha3KtR1O2KC3asuZXGN2o2es5qMKKGNDp7qxmE7CnfmZmMlhZQHPxBwiPAcPt2MiEpubKotTb5303MqSt5CdlOwa8h9aeQJn5ANrKhULeYUL3yPWKPGuhG5YVLZC_1nbKL6_6_OEA-t_WjOuZf3gOfVN0KYg4iV4nBy7cN442ztGGvcWPW1TtOF4WWL80RupNY5dbWrOnIso1FOBy00WfYczo_qWhz9-2mcPc4iFBMNG_K5Wj2e0ihgi7cAL4oeQyoNAbST5j8Ajp84BYnJ8jAxjCb-8H7TCqUUsGVWzwAUwqFU-Tonr0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
روایت حمید مطهری سرمربی فولاد از بازی در آوردن علی‌نعمتی تازه به دوران رسیده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99795" target="_blank">📅 11:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99791">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ei5sRl1oX9hE6h69D_Xh_IwK4umSlaNoxkk6qkIPiF0TsMKfa0TQ5yzaXU6DR8pLb_ejTl4V41Au-heJKYsL8qP9bpjoDB9NCoQVfUKfNdk_oISvnVyGnuOcwnaYk5BAQ-yRW5leBdhJYILWyAhvQFAMdNeevefDetrjhFo9ziajy06jkkRlvnKRKfvx6Adoj1q1cTJ5oJDwMMlB8CyM0W4LUNZaQiIqxYFbymH6LTo96VKmsbSiNxxjPQK3dvpua8HO6pLvAj-nhK3jhRkvuBPXd29NLEX-ay3BmLU0yxW82UNFFoE_niouj9tH0TEIWCNKc6OUVa_NSAjOnXzRJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQafz9CIjMBihYMLh4nd20Cf2VptQQQAL1BX2mFuD8DJupgraS66IeXwhYj6WoEsE5kUMwuPtWo7oGKorVHt3xeZ_gCOZAG8TtiFZGzZ1cTbXZp_edQFnjHmbqtQUjDtOKs_6h446IRy41iAlCoc-I82_Kv8ZAlRqHESWSRXw2C-ZgQWGM_Rdlc7LgSnma8keurqE9xkpEDXOtepvZTX7qazkiql0xJjmSizwLrenJOTbtFjugRBL2MRrUAZjsqbhF7YO-LQ_YGQZKNdnhuTjZIaPQedE30ZJ0uClAkyn66HqwRAUCFECXsF2k9Fj6rlkA-1tZjuUhHs3NCOyYGDDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
فیفا شروع کرده به فروش چمن های جام جهانی 2026 با قیمت 450 دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99791" target="_blank">📅 11:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99790">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHvIz9ceLIh2I9U8lqy4zHWIbY6cjIkR6Wl0jMLGWcu3v-bSFWTax22Y76QJWXtKc5FEizG5dqZg5_sofQdbS4iSg6YOaCeukOxiuv0u7WYBxFKndfpHIVYsKDp8AwIuOi-IbrYdsj_Pwa7yAAKIyuIUp_YhACL0W89X51r6aqXdazQqhmD9brxV25akAzGElrJ8PmCk35195Lww5IV3t8TnGjG7zQBJIj58vR9ZpjACdyL5Mww1uv3LU35LjfvOQA0s5npYh8B7wqEuTiKs7ziK9qoqib2uCwNXNDtWBzhGu11QevbEESJBKuhrFXfFKq5wYPl85dCqhADFW8Xa0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">� بعضی‌ها فقط پیش‌بینی می‌کنن…
بعضی‌ها از همون پیش‌بینی‌ها درآمد هم کسب می‌کنن!
داخل
@betegram_bot
می‌تونی شرط‌های برنده رو ببینی، از بقیه ایده بگیری، شرط خودت رو بفروشی، امتیاز جمع کنی و جایزه‌هایی مثل VPN، گیفت‌کارت، Steam، PlayStation و کارت‌های مجازی Visa و MasterCard بگیری.
⏳
هر مسابقه‌ای که از دست بدی، شاید فرصت بعدی درآمدت باشه.
👇
@betegram_bot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/99790" target="_blank">📅 11:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99789">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e4fb76e4.mp4?token=Nu79AObJmEXgnLx9aQHGzLzeZfz7Oq2yh-rGRtXxgfnVP930-mUKdNCwzVl7yKdHCkchci6oPWoql1CV-D7O4InKSwW1PaDb3ChtErakXRTRgZu8vtL2LbrSEhF01BOKcEyo9ojGrmBmZNXTQeRYXG4uGP42eTaBoez_VFBtcrCHcDAuw1xAdTLRVxQ7nqxprGdjGtw2l9YoW2TOs89N-VByDW6shfbcfo7AVJCtACLqxBnevq4gNZNKwXVm7VZaZT7riwXIeZ-aH2S2fXvXHBpuvdq20GwvuwiVEfDvCRba7lGy52buqpkS39lyXWVdh74N5or5A8SStO4y93Zalg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e4fb76e4.mp4?token=Nu79AObJmEXgnLx9aQHGzLzeZfz7Oq2yh-rGRtXxgfnVP930-mUKdNCwzVl7yKdHCkchci6oPWoql1CV-D7O4InKSwW1PaDb3ChtErakXRTRgZu8vtL2LbrSEhF01BOKcEyo9ojGrmBmZNXTQeRYXG4uGP42eTaBoez_VFBtcrCHcDAuw1xAdTLRVxQ7nqxprGdjGtw2l9YoW2TOs89N-VByDW6shfbcfo7AVJCtACLqxBnevq4gNZNKwXVm7VZaZT7riwXIeZ-aH2S2fXvXHBpuvdq20GwvuwiVEfDvCRba7lGy52buqpkS39lyXWVdh74N5or5A8SStO4y93Zalg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
لحظه اعلام خبر درگذشت گراهام توسط صداوسیما و تیتر: به درک واصل شدن گراهام رو به ملت ایران شادباش اعلام می‌کنیم
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99789" target="_blank">📅 11:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99788">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f1adb911.mp4?token=kkvrAPyCYmp3f6A3_9xWrXs7aqjwZHh15tlt1YvvAB-heYbuk8w4hgxIz9K9HU3ODV7yc2SaDLSw9lT-nGMoOLJzQZUy3ZhnqW6Vola-1FxZzg6QXp90Uw2YhI4ND2a7dl3gweZu521nErLP9lIShQbaEITvjWJuNC1N6NklLyf_XrvkKLhCIpc0kQpfQDif1CsCp1gJIXB0flw0fHQsy3-WBo8IUA316dBdT-2Boxz9MjttWs-ptE2F_sZq9joV3sEhXS0xqGfIrGgQrTA0GsfEDYaKbMZCCijvB62yTN_vLTPFfHErnTIZ1yg-nSEahXN1gMT3XQUMnHLk8PlWjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f1adb911.mp4?token=kkvrAPyCYmp3f6A3_9xWrXs7aqjwZHh15tlt1YvvAB-heYbuk8w4hgxIz9K9HU3ODV7yc2SaDLSw9lT-nGMoOLJzQZUy3ZhnqW6Vola-1FxZzg6QXp90Uw2YhI4ND2a7dl3gweZu521nErLP9lIShQbaEITvjWJuNC1N6NklLyf_XrvkKLhCIpc0kQpfQDif1CsCp1gJIXB0flw0fHQsy3-WBo8IUA316dBdT-2Boxz9MjttWs-ptE2F_sZq9joV3sEhXS0xqGfIrGgQrTA0GsfEDYaKbMZCCijvB62yTN_vLTPFfHErnTIZ1yg-nSEahXN1gMT3XQUMnHLk8PlWjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرمهدی ژوله: به پژمان جمشیدی با تاکید خیلی زیاد گفتم به تیم پاس نرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/99788" target="_blank">📅 11:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99787">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e66e95548.mp4?token=BgYBQdExaGgF-zT61CEfVPiw8NXWqWv8OHC_GZEEXor2vIEfUviwUqeKLHxSKOPl1GRGjGurm7e5obAvAc-S-TJhX7h7JRQ9JisUH5kZdqa2tYOavL90NHqJLgZkV1mzt0jN21RhnuXj5HAXhguKnvTNxJ2WNPkXJBkP9gQzMnfdK3fuz6O7lr16MDCVfQU_0oQoqGlU2ZCChiih1gY7qH0j45a2IpI9x-6wlfsp1-E1xmLibKaLL2LyqS8OmyL8oaQK3U3tXElqTBdeOhk1YlU9AP8vnCrpzh3WNtFnFACBs6iFuA8CMOOTXwBvdX6AnKx3pv10ZOZhQU111W8nuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e66e95548.mp4?token=BgYBQdExaGgF-zT61CEfVPiw8NXWqWv8OHC_GZEEXor2vIEfUviwUqeKLHxSKOPl1GRGjGurm7e5obAvAc-S-TJhX7h7JRQ9JisUH5kZdqa2tYOavL90NHqJLgZkV1mzt0jN21RhnuXj5HAXhguKnvTNxJ2WNPkXJBkP9gQzMnfdK3fuz6O7lr16MDCVfQU_0oQoqGlU2ZCChiih1gY7qH0j45a2IpI9x-6wlfsp1-E1xmLibKaLL2LyqS8OmyL8oaQK3U3tXElqTBdeOhk1YlU9AP8vnCrpzh3WNtFnFACBs6iFuA8CMOOTXwBvdX6AnKx3pv10ZOZhQU111W8nuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
میکل‌مرینو فرشته نجات تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99787" target="_blank">📅 10:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99786">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e18c3ee23c.mp4?token=QIgypOu8EopJ0xFCIJ6YcUdONCBFnbfMeWxMbriuXB2vgrwtTmHRNknGPIPoSdv7LPK9wpwWBOtbEnnSlwXiE-KniETUUCuNag0UXPb3cszeXepeB2NC8qE-riEeA2vU6Hvcr6MGG0UT2mjBU-ZAk69K4dyWHceToGU1-vkCvSuCQyucgMrpCHn3gKGHep1Ngb5LAsF7UY1-qab3VIvGr38IQSvG-n9kTyTw8p3Q57UegUB3b07-17_u1QZ1JFD38RuBCjdeAxLBWgp4CdNsnoNFnJcGok81U1P00MjuwXYpJ8cbhcd3JIhd_qKK0agcYFxRl6KxX9z3aefHXK1q9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e18c3ee23c.mp4?token=QIgypOu8EopJ0xFCIJ6YcUdONCBFnbfMeWxMbriuXB2vgrwtTmHRNknGPIPoSdv7LPK9wpwWBOtbEnnSlwXiE-KniETUUCuNag0UXPb3cszeXepeB2NC8qE-riEeA2vU6Hvcr6MGG0UT2mjBU-ZAk69K4dyWHceToGU1-vkCvSuCQyucgMrpCHn3gKGHep1Ngb5LAsF7UY1-qab3VIvGr38IQSvG-n9kTyTw8p3Q57UegUB3b07-17_u1QZ1JFD38RuBCjdeAxLBWgp4CdNsnoNFnJcGok81U1P00MjuwXYpJ8cbhcd3JIhd_qKK0agcYFxRl6KxX9z3aefHXK1q9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
🏆
جوری که جام‌جهانی قراره به پایان برسه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/99786" target="_blank">📅 10:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99784">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dg9VKKLPATwEn1zmyI-eMVZue-cynrZyOSsM5bW97wIX0wT__rOU8hO4TRf3IyQtUm7SUe_xE7Ghvn4BaAEeXFHHFditp2JY1SZgEijJ6suMfr9Gky3NelLKXzmBoPGx9YnvLLKPGdeVI3ggLABuu90YJqTiIhV2DNI1VFPkqPQLrhAUP-CmuZ62vtLOlrKSCvejRMhv__VK3uliKHyKR9lbP1DdLVX1chwsaoQ8-tQkgyF1utDLwrrr9ZSdsC9j-_Jxj3TKBAi5kV4tZdOLLeFAkpkH4NOane0n8jaZnMn-9LGw0SoWk39DKPZtG3r27b5mAIC-ReaNK127baf_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ulEqZo3ODmo7nbSfda2xlqp0Iv79atwd62zoYpEKVkVSioMj-YoxTV2_KmaHgB8wE5u3OAsBHdfymAt7R6FblteSWRGdoEfd0rmWUxmNp8G9lY8sMx2C6lzmf1kPz5an9mS73G0xDhtyKIUr4_00hVkdpRfmtCXrF8yKXCy8jd3BkCDB0te0qoMC-X4-Ejwg_RJKb6dEhsUQmNMSUUxDU0bOBZzYxBjuIgqlJEUHLQThHltYBhpCaBuB92B_L0GAcTpqmuplGBEsBVO-8JH3D_4yE1LCrBEZ0EWd1yL1Hv-cKvKWkNJM3Et6FXpqeBApDAo64MWKh6meVqXS7MEwgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر چقدر به دروازه نزدیک‌تر بازی میکنه مهارنشدنی‌تر میشه. انگار بیشتر یه مهاجمه با قابلیت‌های یه هافبک نه برعکس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99784" target="_blank">📅 10:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99783">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f570ead6a7.mp4?token=CZ-0i-blSRaZUNhnHgTZItzQTKvnaF16skMkZnmZ8yp6RcqRhtvjQgV6K2nOnRz_32CAwqaRoH5sia5Ke_--bxOYe-Wtzog5tiFDEpa7tT3btlajjbjer5TepZUV_49IsWlUN3L7eC5aVn194KklA-H4h60GG_PgZ4dmbIOhlbidn262kqyiudADqGeIqTMjZukarqsrtfvJc1kWl4SrBVv8EULxmb93DG-O031C6rrNRTvMUIbFeKBP4lVxooSdZDvp0sEnnPpuaT9v-7sP7JGOsowG7v1dlkdq5dBlkyhtucHVQb4ndaM6a-EteqB3eW-jD_ZFebAkPwJmqi3_rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f570ead6a7.mp4?token=CZ-0i-blSRaZUNhnHgTZItzQTKvnaF16skMkZnmZ8yp6RcqRhtvjQgV6K2nOnRz_32CAwqaRoH5sia5Ke_--bxOYe-Wtzog5tiFDEpa7tT3btlajjbjer5TepZUV_49IsWlUN3L7eC5aVn194KklA-H4h60GG_PgZ4dmbIOhlbidn262kqyiudADqGeIqTMjZukarqsrtfvJc1kWl4SrBVv8EULxmb93DG-O031C6rrNRTvMUIbFeKBP4lVxooSdZDvp0sEnnPpuaT9v-7sP7JGOsowG7v1dlkdq5dBlkyhtucHVQb4ndaM6a-EteqB3eW-jD_ZFebAkPwJmqi3_rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو هند اینقدر حوصله‌شون سر میره دست به همچین کارای کسشر و احمقانه‌ای میزنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/99783" target="_blank">📅 10:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99782">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUK6SLFNlz8bBvcp8SyORv0YD1e6p1BptCct6Hx1y5hFqn2hb0i0WoTZJJl20ZoWqBJiwy9DQZAmJO7kt3I3sl9DS1IMIg3Joi_fLY7V1A8NyW-0BQtRo3TYPtUZDubY3N_6KXdBmqebs5JI_JvkTsReumhOkYZUtgaw-MIwtqo5Dz8EZRUel6YPIZkPCW2uwGjfZ8-2mzQYCw7dXEMKEBRtoldIkulXWBijIQUdqH-r5A0KlsjopkrejYX068uHoNiGTBu9MfLvVUy-FyB9eDqOw5H8T92niNfEsGiV4SpO82eNvjY50JFtcu-NTM_271y2GiPW50Vc6KY9OaXkhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام سناتور جمهوری خواه و از حامیان ترامپ بر اثر بیماری درگذشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99782" target="_blank">📅 09:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99781">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56cccb9946.mp4?token=MuNX3ySVfFG5r5VfQK8WDGd9WTQIXyDiL-uYVnzxb2SE5aKJHuKNzz0sHkagEFPckbatv5z7RkP3HHJ1BR_lusiFXfd9j-ZApKLGItF7MxwfpDCRLQP5-g8-mkHV3wjW4VrVsTPw0e-91M0GC8gz3SNkxvF2XzJXrsByAbjL7MxWTRAweSGtZlQ8rb0trbAnNWlRLEhwO2CY8rOdBht3MFqstn2rn9DXvyHhtaBtPutTXhRfr22KD1kq9wsIihrEuYIiZSIn0qBd4hrFMtDqiVL8C1X0BYD5j2rf5dbRkZt_PbZm3e9UC41DKXRXQAp6AREcW-caKn9CwLwNXUE3aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56cccb9946.mp4?token=MuNX3ySVfFG5r5VfQK8WDGd9WTQIXyDiL-uYVnzxb2SE5aKJHuKNzz0sHkagEFPckbatv5z7RkP3HHJ1BR_lusiFXfd9j-ZApKLGItF7MxwfpDCRLQP5-g8-mkHV3wjW4VrVsTPw0e-91M0GC8gz3SNkxvF2XzJXrsByAbjL7MxWTRAweSGtZlQ8rb0trbAnNWlRLEhwO2CY8rOdBht3MFqstn2rn9DXvyHhtaBtPutTXhRfr22KD1kq9wsIihrEuYIiZSIn0qBd4hrFMtDqiVL8C1X0BYD5j2rf5dbRkZt_PbZm3e9UC41DKXRXQAp6AREcW-caKn9CwLwNXUE3aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
صحنه زیبا در حاشیه بازی نروژ و انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99781" target="_blank">📅 09:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99780">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5675db48a.mp4?token=iu09V4LnCM-6_JAy2pX2AXmSgnMkAyR0d-Dqx62RMdJ5cvT6rPieI_bShj_i0BFNxS6oiQlIfM2lsC9QfFO5nw1w6f5R4L9f2TqNdcktTxs1pzPbbsexvpRv55T59GGCcK5kd2CmcaVnPvdYiIiMVu0HAXIR-smRluJRfcBfNPCC5r4kj0-ROgGL_Y1j202wJrhHbgyFfl_1o16sIZCs3ij6BO3XB6N4P6doQs4DdP7MQFyKM3UrP_aJ3swPuHVkGQTkNKb8WROPlbz5Kq-LTNwgOXrtffxG6whipaJy-UmiLDMQqXEwYfHlHUcDauiG7KAfIONA1rUgRR9lSqSwuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5675db48a.mp4?token=iu09V4LnCM-6_JAy2pX2AXmSgnMkAyR0d-Dqx62RMdJ5cvT6rPieI_bShj_i0BFNxS6oiQlIfM2lsC9QfFO5nw1w6f5R4L9f2TqNdcktTxs1pzPbbsexvpRv55T59GGCcK5kd2CmcaVnPvdYiIiMVu0HAXIR-smRluJRfcBfNPCC5r4kj0-ROgGL_Y1j202wJrhHbgyFfl_1o16sIZCs3ij6BO3XB6N4P6doQs4DdP7MQFyKM3UrP_aJ3swPuHVkGQTkNKb8WROPlbz5Kq-LTNwgOXrtffxG6whipaJy-UmiLDMQqXEwYfHlHUcDauiG7KAfIONA1rUgRR9lSqSwuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
واکنش تند فیروز کریمی به عملکرد بازیکنان نروژ!
فیروز کریمی با انتقاد از تصمیم عجیب این بازیکن گفت:
«اگر دسته سه تهران هم بود، پاس می‌داد!»
😅
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99780" target="_blank">📅 09:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99779">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhV3PcdchCS7tpvcv0IgPAZi1YpLiYKFGvfFrdUpZNZjBj5e1bcQOHjK826XvmZKZyfu2KcKGZSpvFC-TuVwybio6uDbz6LaTBfznJ_wckAWFCy8yWGwrlqQVKyIVUQy6IWS24Z1pKkxM5uqgA69bUA7Z_XddKcsvRdjg6fV38Z_sS3hPr_PNxM-vZz2xN6zgx6I4KjOU6Xei4jsFnqL7o3_gYz_R1TJNqrRWjgR2p-8vv4zrbsB5r_uq_oiH3Wfd8h5ZWqSBSPH6MjN1uKsSUSS2Mo_yPVy28BcvHo_pG5fYKvwVFkGoi6Tm2YslJtUUmlhqOifBnZzl8YWMW2Bug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریک امروز 1 میلیون دلار رو کانر بت زده بود، که تو 30 ثانیه اول باخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99779" target="_blank">📅 09:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99778">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9322a318fc.mp4?token=qOiBaHffGGC8PuZiG5Yry-NXBTz6MWbl3D2LKJ4QmpY_-8pcByYF8NIswU4avyDPXMKZ4uwu7_XATIIb0v7F8qci5afGP01hdDqyLKDMvAHzLUAekoy9yO46p8fJ9pgySQNTAQNwCO6QOEH5ZeRO-lfCqwLR8NebuKXoYY1O6lpGP-EAGG0V7QiVtLGJGCythvFlmtKOaye9AUwCSMfH10BDQ99QZlJyx-YIEmT9HTfMz4IGHNIevJBueO2XCaVOoL4YkXNvWPo18zcgvXigJw7sUbylUyLHwXU7exFTYH5colMSGqIw4kKlc9ExTGux81_rwEQ5pnVVK8U1yEBQLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9322a318fc.mp4?token=qOiBaHffGGC8PuZiG5Yry-NXBTz6MWbl3D2LKJ4QmpY_-8pcByYF8NIswU4avyDPXMKZ4uwu7_XATIIb0v7F8qci5afGP01hdDqyLKDMvAHzLUAekoy9yO46p8fJ9pgySQNTAQNwCO6QOEH5ZeRO-lfCqwLR8NebuKXoYY1O6lpGP-EAGG0V7QiVtLGJGCythvFlmtKOaye9AUwCSMfH10BDQ99QZlJyx-YIEmT9HTfMz4IGHNIevJBueO2XCaVOoL4YkXNvWPo18zcgvXigJw7sUbylUyLHwXU7exFTYH5colMSGqIw4kKlc9ExTGux81_rwEQ5pnVVK8U1yEBQLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انگلیس در نیمه نهایی به آرژانتین رسید!
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🥶
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99778" target="_blank">📅 09:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99777">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd2c616406.mp4?token=dCcpVeNlq5RgfV4Td0piGIPP05bT2xKW9Zs9Cb83QcIia0AMFPb8duL0l2XuT8qHft5MJko27WlM0fNTuo3BF1OFsdzMNKJRw5OCTR2qTo6W_3QPZs-ueM51YmYh7276HAKWrFz4q_rU_9VVrCfpKKSThN1OLQi87Wx5_Hzx4xFSGJQezaT_ma6Hf-F7m-Njg9cErsoCTCJAiO1LnoEVgqMKN-98_hZJk4tAI1TWiSX47gTIWBtcBuWf1KEiBS4PZ77Yxw9qZ2m96Xh-hMWPPGaof75NCK-fEEzFjMC3UVYRnP1ncc2Bud3_Q8KLNUm4rZDGqmE2ZN98gp0p2o8nZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd2c616406.mp4?token=dCcpVeNlq5RgfV4Td0piGIPP05bT2xKW9Zs9Cb83QcIia0AMFPb8duL0l2XuT8qHft5MJko27WlM0fNTuo3BF1OFsdzMNKJRw5OCTR2qTo6W_3QPZs-ueM51YmYh7276HAKWrFz4q_rU_9VVrCfpKKSThN1OLQi87Wx5_Hzx4xFSGJQezaT_ma6Hf-F7m-Njg9cErsoCTCJAiO1LnoEVgqMKN-98_hZJk4tAI1TWiSX47gTIWBtcBuWf1KEiBS4PZ77Yxw9qZ2m96Xh-hMWPPGaof75NCK-fEEzFjMC3UVYRnP1ncc2Bud3_Q8KLNUm4rZDGqmE2ZN98gp0p2o8nZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😆
😆
😆
مکالمه پاره‌کننده دیشب هومن افاضلی و خداداد عزیزی. کپشن اصل داستانه⁩
من از شجاع پرسیدم!⁩ شجاع بهم گفت! گفت که بدنامون خسته بوده! خواب بوده
😂
⁩⁩ ولی هومن
💀
⁩⁩⁩ بعد همون شجاع
😂
😂
⁩ گفت غضلاتم همه گرفته، عضله رو ولشن!!!⁩پاهاش اینجوریه دیدی که
👐🏽
😂
، اگه پاش اینطوری بود
🦵🏻
آفساید نمیشد ما الان بالا بودیم
😂
😂
⁩⁩⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99777" target="_blank">📅 08:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99776">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0WW-fZTWPCJ8KecTEw4KuRGEjdkqr10JZJV5Y55kL3GzE9TphHyHed-O3Ei9HkcVCvXltYLD3-VMeiu43bJMvzA2FAXGoCC8FahMIzMAkfl9GsBvu_0-nYCttV9kLrmWlkFKIeIU7TmYdwLmkUKt8dHksn-8U2eJhD1JNM7M42jh0H4Sh6WgEp_kUoRjQV24bVtQ_FkC1tctwfrHp0aEDay4xNiHF9M2K4KaEjXKnSQ3JQz2jApGaBZWVKpzMhNCcrkp-2LMtf0LbxT6iejm9wcHueXqt_HbavhbJMjYDplYLTUDqPCvNzXsDsu1UvIugCyq68wdmSBESWwiL1Eig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی اولین بازیکن تاریخ شد که 15 بازی در دور حذفی جام جهانی انجام داده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99776" target="_blank">📅 08:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99775">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPp0gOm9Iehanw7u19b1EAIlafqTEbdTBy0rJuLFUbEQyjqDOEnlMpMGDLp5raY3TbDQ2Nf2TRdLFCtQ5qlY4EC7D7C5OD2pT0XOJWgf9nMxfs6OizF861LBVVMHk4ydRgOKIDBWDEv_9czwND-C6a6v10qh9Qi5ehy3-ljtzKcAEkHG1v-JIcNZmFVlXq1PChZMoXIX3aTtX5L341lvbi3COr4Ny9zJ2rRKximP62Y8lb9-GdwoZRF_BKqx5SbT-JdxVJ36geutikcCppefFLa-dmGdafja3bE64y_qYRMW4iYe_NeBSre3x3eY7S1-KsKOkOZyEjxwKjqAz5Snkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🎙
🇦🇷
خولیان آلوارز: مثل یک ارتش پشت‌سر رهبر خود لیونل‌مسی هستیم و هرکاری برای قهرمان شدن مجدد وی در جام‌جهانی خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99775" target="_blank">📅 07:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99774">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFdaxjjvYLzN4eYXQ0FZ_jyU-2KeFVflJ2085mw-nPviwVvyE9f9w1MPcH_vDtazvcq6V4W2ogcrl04AKRuBeotrHpXEOrcXVyuLxN_e1gNS_Ygtm7nNbwthMhCb0PKdXgJcIk8l0O0i-YmaFJMTXmiC3_Det2xPt2-9dvtbgq7ID2eXYv8L1no-SqRTCVXy2fPSQRFPCE7brTVHAbNkFs0BTrbqcul6dbiYM9GZ_TQu90NDS3coBwYNfKcXdwWh22rc3kVjzLhNU3b9qkDBkXP4Vk3KvWv4zz8c33x88-Okv2klTDy4axDFFgLuI1OyXX299Jmf46oB67SE4ouDUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
تیم‌هایی که در طول تاریخ بیشترین تعداد به نیمه‌نهایی جام جهانی رسیده‌اند:
‏12 بار —
🇩🇪
آلمان
‏8 بار —
🇧🇷
برزیل
‏8 بار —
🇫🇷
فرانسه
‏7 بار —
🇮🇹
ایتالیا
‏6 بار —
🇦🇷
آرژانتین
‏4 بار —
🇺🇾
اروگوئه
‏4 بار —
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99774" target="_blank">📅 07:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99773">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTiUmXrG1tUYBQzTXjuoAR1FqM0vZljsSOqrIxneQRrHBuqYc1PHWIqFtqGO3Uabe_Hpj2ZUOmTCz3wJtQPDSVWGD1pmS6bjc0AWzB6n6QtIG7Zd_1Q2gEpuGcE-VowINHNQlyQrdF0nzXHDNAKK7lKkE7jZD38B9kVyjh2L3IFqYooXFV_mQQ3pI-7dJyBak8eLadtJ_C2SA26-QieBbRIOLo069s3o0fDqttgLzdbR87lw6ntQmOhBJYvA2Sj4w1iSqJEKXfT1VxTZw5-bJRG9yqIwjSGiDHloVtn8wCVvXg50MHuLYHEJBO5Y5-gF3DPhSO9hOE68ALQ6hthWsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇦🇷
خولیان آلوارز رکورد مارادونا با ۵ گل در مراحل حذفی جام‌جهانی رو شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99773" target="_blank">📅 07:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99772">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHu-O84uyAylojN4Z4YszezwNbD16Cp8Rc97otxmwMJOcuou-XYjz0mcxaf2j4EfC0u7p2F9T1TJSEPJ_NJhu6L5GqIUs9L7cYWePlsyLpoBRY0KkO7Wq80_jZPLHNLu6BDFWiE8Bc6fWirC29kuadXG9bjTq9MyCFVNAxd8i_8ILwTV7yjTs8lIFXrghKOt6BO4vtH2aIf7YpH2tzLNyPU7MN0-0QMxQ4IpytE5xAuhrN_fNEfgXI-GeA1TSgVnRPgVuPvEUgcQJ-sH9-MF8KDC-umupKc3m65oZX7qd66CyZwlJflAYdzFTJ2O5yVavq90JHanrLbCgUp2XPLGRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی آرژانتین نخستین تیمی در تاریخ جام جهانی شد که بدون مصاف با ده تیم برتر رنکینگ فیفا به نیمه‌نهایی صعود کرده است
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99772" target="_blank">📅 07:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99771">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIvArxtDIc6XuJlaQYmHsuC84HeOHYccE5h4_FrGfTm3kqINA97Ihy48JLIvfsZfURLxnRwPRrEizvvsopcs9maHUQRF4rnjFCYVWjqTF_8ZqqjuwCZAmjhX0bTiGmueJsR0-2t95f5WvPQyeA8ya-WjCPoLARO2jKxiziYGwNuRiBV_4ig3Vqi-GGFzAR0EpPq2v5hHMvT1F7FcqY53PgCIKezerARWGUTQ9hM7TZ7atqJf9yxV9DG8YF7V8LaEBPskeBLyPWCTTWDp0Zi-p1Tv2MsMztqKp_f0Cf2jhZbHcX7M9cwUqIqZmepY1cyHcIHj1-wO1XjAav0hSKEM0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🌎
| برای اولین بار در تاریخ جام جهانی، چهار تیم برتر رنکینگ فیفا در مرحله نیمه‌نهایی با یکدیگر رقابت خواهند کرد:
🇫🇷
- فرانسه (رتبه ۱).
🇦🇷
- آرژانتین (رتبه ۲).
🇪🇸
- اسپانیا (رتبه ۳).
🏴󠁧󠁢󠁥󠁮󠁧󠁿
- انگلیس (رتبه ۴).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99771" target="_blank">📅 07:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99770">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61b30f5ad6.mp4?token=HEpZI8rsx_hMzH_WRYvoJYwk9GV1YKxo1BYMTmLf6Yfe1YAlJBciFrRIsW52aBonV7RWE6Ykdm599p4_ZG5ji3Ngu9drnk_EhQ1LyGN52hs1I9C5RbX3xCMpyQ6PPr8Cn4cjNnDM5w1RO_d-_wFw8qw8-A6KUIzHSYJACRVHkMfEs7yz-MkBtsXFIYbAtlxj1e_AyhMpzszd__MriiVvJ4FaKHAHZb21m7K8g7Cjams36V2juiCu_YC0zUsKSmh8g_6waYl9MS1VMQBqR9V047uCIyGUVDyCOBj_fYTYm0QUuxzhjti25sZQTv_qRBkQwmISuxNdfUKUlhZdtrHD0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61b30f5ad6.mp4?token=HEpZI8rsx_hMzH_WRYvoJYwk9GV1YKxo1BYMTmLf6Yfe1YAlJBciFrRIsW52aBonV7RWE6Ykdm599p4_ZG5ji3Ngu9drnk_EhQ1LyGN52hs1I9C5RbX3xCMpyQ6PPr8Cn4cjNnDM5w1RO_d-_wFw8qw8-A6KUIzHSYJACRVHkMfEs7yz-MkBtsXFIYbAtlxj1e_AyhMpzszd__MriiVvJ4FaKHAHZb21m7K8g7Cjams36V2juiCu_YC0zUsKSmh8g_6waYl9MS1VMQBqR9V047uCIyGUVDyCOBj_fYTYm0QUuxzhjti25sZQTv_qRBkQwmISuxNdfUKUlhZdtrHD0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولی عجب کیری خورد تو این جام جهانی اسپید طفلک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99770" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99769">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2b50xeXXX25DxxeAJ4NlBLlMvmXl_4K7ZHHYRCHL6I4Z7mWbUWrLEHN_RdnJ_5USyQzSoZGogH4k6jXKphxt0IA6JDnMxG9t1zM9fhtCGcoS0TFsV90_-tmkbLzJJ5Rjs4o0SFUq3dZh2ubMChEBLUobPBSPAyPSzqiUFuts3HBmvsGwl3vOK7eF0cnWdbtgUMLVEOZlextAM23me8mEqXQqbVU43ZFTV5_GlIC8fZ0KPyQbA6fksmm_ukYCarQybfGjkWY7a2CPvhuZ3drHJKX9gH2oKdvtz8yY9wfrdI5FCb65UIp1-PvL9_Iyr-pDycdEcVGfkfu-9ADONfDCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🥶
🥶
قهرمان رو با ریکشن نشون بدید
🔥
فرانسه
❤️
آرژانتین
👍
اسپانیا
🤯
انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/99769" target="_blank">📅 07:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99768">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🔥
🏆
برنامه نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
🇦🇷
آرژانتین
🆚
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗓
چهارشنبه ۲۴ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99768" target="_blank">📅 07:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99767">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpyr4SH4-R469jav-fycJK38RigEITIeWbdbNfIzaIFh28H4-HNC1SwtekuhGugQEdku0b0UP1ZNd5CbbbFyoc3y-GrDRMz5xDEVGP-LA5jxFcfugQiNQ4Kg_HsMwH8iNPrjtHkir4tLOVvaaf_nBI3Zahmoh3zu2HBxeu2ds0hJFQnhG8YDofCkbdo_cyGqhelXWAFUN1YysG9j7Jr-hj_pJi_VAnkM8mPndTOeQMHpj4mVntnoazrH9p36eUU-DZirJD0NIxj1yQHlB2eRI74K64HanVXfgYfXKsmlqb5zC6OC11o1hncaVA8Bc3G6W5ydOAYDPPsN3beU4w4bpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
برای سومین‌بار پس از دوره ۱۹۷۰ و ۱۹۹۰، هر چهار تیم حاضر در مرحله نیمه‌نهایی جام‌جهانی سابقه قهرمانی در این مسابقات رو دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99767" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99766">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGbcBRl_up9aDPyWieHubaYBrx9yzqRn4tmI1TRVF4_Th9rBxfpzTJLSb9MHhMgAEiz2hp-4pi_mMYpEouzGyzpyh-KxhBij3nO0cfbUGy03bxyt7XYZy1owT1qRyvm-7_P0T0O0UHFM1mMY6yPhu1hlM7bOJYBWRm8fO1U0ajafZdDKPeCQDKkpJQZ_e8f2LaXGB1sGFRRxb6di5pzWo9mZKTkGhFkNQSvKWXUcrr7K3JSV8V2tw99-dNFUgQJTpjdcF2V5TimK5vDst4fHUkPtnK23lEi32Tfwjo45LdkKCJwEEwJMA5c4xHyvsn__RcvKXDA3PMP8pNBEWQoWrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسو ببین یا خداااا
🥶
🥶
🥶
🐍
🐍
🐍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99766" target="_blank">📅 07:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99765">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XBP4bvrj6z6mo-ul_uFDHERlmYPKa9lV6aRcNvek9CaBD6xutDSLpd6rZoVAhRKI-neeULFypY9R_bGLL1CXK3BKTikwsLPtOzIHuhkkbaFaN1pHSj-lc3XVYv-120olRUZXB7tHllhwHXT8vUrR_O-zP76Iz6aYRGu8K99kqiKbvWxEP7eOHLRs9WGsChyOypH72egemyZ3n2TYLxD-vPH33aeSQ1XFvpmlulQ6VbneZoZG-4I7vfVmOpQbX2XZE8Soyie08OuzobZz-S8wHoc_AdlVaK1D3npACG-hvAXl_zz3U56MoqCB8j5lKZyD9X6TBQcc1DE6mNTJUW2gXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
لیونل مسی برای اولین بار در دوران فوتبالش، مقابل تیم ملی انگلیس قرار خواهد گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99765" target="_blank">📅 07:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99764">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eecRMQBnSqVmK7pi-R_VVRfEoT1KEhneS5k7vxUnIxbP9lZmibgWt0XI4edJBugzaMjc0ngli3yLhvlZ0BRF7QTDTsKDs4UVTqS_cwcZPr_Mhp-FNuqwxj-5e9Y5Urr9FOk6LGqpZfg4qMWVvwbPGNja0yVvukQl3o3OqLIIbjLTBxOTVh62PRj7kU1LPOm1Y3XXwfdpS7sa4Nhv7Cwl4613KfbjDcF8jg8zGAJXzTRvw4fvab6lj4l5xuRUeoYLyj10rxIRjz69hA5tRHG3WOi_08SgHXvKCW0-ATNHzrAskzonfwkPT5neHetqKxXzBfqPPxZM9Xm-jXhfEiu9mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
سوپرگل تماشایی خولیان آلوارز مقابل سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99764" target="_blank">📅 07:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99763">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYKPdzA4LiXPDVDaTtR_prI0AIW0SkLhHGDDkNvMMPmDP2GyXp3eKhP67sH7AByXa_gLueEV5XlK-PGINhOIRLjNEqBhZGh_pI8Fmcbm1ahbxKLakdsSYfxNq66jZeCZRcenm4WGVBEGA2c3EEMdgl7o92Tnc6GXYS396Ser4wZIv1eC92bOo-fcTYjxl1npmAvyE_L7phQHJR832QLKAl8V16i0XV2INtySD-j4AoNR9AZMSJeoLsF2rWbgyeF4sKwMh4yZ0iJ5VcNBQcsDAMFUH6bQHzYZjadnHIOKTIobp7qHP8jGp0i8Z4AbjLy5A4jMh56iswWiV74TnAN7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
برنامه نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
🇦🇷
آرژانتین
🆚
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗓
چهارشنبه ۲۴ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99763" target="_blank">📅 07:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99760">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9t7VH9oZOUbnkDP4NQ5zwr9b3mpgZ2krk5bIzDy8niRmmKmOFicOKrcd1R-3F4KgXtgQvP-gwigL7usiS9i9cNR-Iw19-1StqgEDVpzMhUfLkCnY9R_Z9dVY6jMLP_KP0KfAoTGh9qmmhtCzw-b_LT-p-Nel51PiQTWFrV1sV5gBa_QblXDN7c88WrU1IEAr1X--sj2mx5eRjweUNAYnXcVAFeCe2-TPo8jbfOa1gP-JdGlc8J75e7SRBVxoPsGBb7TF2NVbQWaWf8bEjG7kp3ZYK7qxizbdZIHKolU4gQT0kzSCobLjKAoo2sa-emSUwAxLmR2OpRcXUp384FXDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
برنامه نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
🇦🇷
آرژانتین
🆚
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗓
چهارشنبه ۲۴ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99760" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99759">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSwOwD9P-wAg_Yw4JifPcCB1Xw1r72I_3nOBmhkZCexWtR6ndwxyxZ6o_J6jaA0nZNXxQOJsFUwkElQskXXUvIsQZdrPks2yZ33FdhZKvP4EDPLUGJJZ3f-_TO1FiVSpacD4TYjYlZbfsiaTcPZRUONSkCuMONywkK5IJ9Vjs0Xyo3_SteHK-NX1dtwI9RBMNgSMFkT2q_LiKUlhlHo-Vp-Zq5M16UYMVJaTtyV2hdiuO6MKwq-1KwOZ5y8DBQgy_zDXRzaCBMUNO69dbIv4pbeLw80XEVpoIj80-nc_QiCPiSEHAz5KrLKYF9ongnQ1GNkGyYxlwcJnpJetNpuaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
🏆
تیم‌ملی آرژانتین با برد مقابل سوئیس حریف انگلستان در نیمه‌نهایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/99759" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99758">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TawV9NDvimXOSjzmqq2Wy2Tb0sjd5QeXbKRNirME3IsXa_mmyZemNLPLW8hHR2Ef-jp4capF3HRnEjK4uQKpOvGHeTA3nohKuHCxfxjjXVvh8tfDyXUes6p-gxihtVhUTWs4InT-q77gnLfJimBVbfiYLVSISJtDKi5Qep58Z71JH2V1ord_PzvXNLQAi9RV5xXEUv8Ca0OZaYullO2OPK0Qci4Eq9gUQMUwicDgpHVoH2x5PQsiFSLKkLvPehG0S7U9aAdE3y6uq_dzSl12lI846R2z6pO0FnFJnxXWsW24F5fSwmYaY7L7ABx1ZMQy4f8ZlkyC9Pl6uitDGcc2Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|جام‌جهانی برای کشور آرژانتین به نیمه‌نهایی رسید؛ تقابل با سوئیس هم به ۱۲۰ دقیقه رفت. پسران اسکالونی با نهایت تزلزل مقابل سه‌شیرهای وحشی قرار می‌گیرند
🇦🇷
آرژانتین
😆
-
😃
سوئیس
🇨🇭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/99758" target="_blank">📅 07:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99757">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مارتینززززززززز</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99757" target="_blank">📅 07:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99756">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">لائوتاروووووووووووو</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/99756" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99755">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">و تمامممممممممم</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99755" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99754">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلگلگگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/99754" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99753">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دقیقه 118</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/99753" target="_blank">📅 07:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99752">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqeLsO2yZpkRSAsCT-ykb9gFKCQZvPDfLlRsAzY9QLPib0m73SOolrk9Eycs43S3afFOj5Z9eJVha_uOwrk7gszakUBJz6AWsLlla19NLKRhy4Bz1xe9uEs8Hrd5Ho-eDO1L_5v57lm8Njw6eyKPR8oH-cO56CegHsycTL-wvopi8RdPblhXy9XCKsBMklSGTwTNsJTkl7TaoGPE3YPF_J8b8xFtqNZwFZEE7_8-p6foE_1h9iXQFjkNS0da0n2J9hP-CYmuOf-sObjUf3iQj4Fyy1H2s_ZPhdHWn_u1x7D7e1wOtjAr-U82_53U8bTMeXDeGfpSbOSgxwJd4Bqntw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلوارز توپ رو فرستاد جایی که غم نباشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99752" target="_blank">📅 07:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99751">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlxzTuICsznQDbfHS-xCRtlXvXRntN3000AoTNtVyRW27Vihsnjz5bXOAbBOimCGBqQyBW4bDPtugWwXtCTaBGx7GWLrZ0OTtQVLyEkmn_aizekUgUd4XF1IR_FEyXpwmejfmBpX2lbcrFAZq3yYPpJho6WOif5YqA8z7ne7--QnFMlhYVo9rtClh4BraGSQmNSXmRmV90wrXNLiMgc4zxshm-PRxFJccrOBJtFZwbN2ypFwPXoJLLXGLF9YtyG4l-s_GWMh6gz8YItna-e_2TTrM81mTWjNfD0qcIpkreqOVCiljoEtH2T3vsDLb6RVWR5oRmtbFAAaYhFMNDcRjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب جوی
عجب جنونی
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99751" target="_blank">📅 07:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99750">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🔥
سوپرگل تماشایی خولیان آلوارز مقابل سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99750" target="_blank">📅 07:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99749">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آلوارز از اول جام جهانی نزد نزد
چه موقعی زد</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99749" target="_blank">📅 07:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99748">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آلواااااارززززززز</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99748" target="_blank">📅 07:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99746">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خولیاااااااان</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99746" target="_blank">📅 07:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99745">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مگه میشه مگه داریم</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99745" target="_blank">📅 07:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99744">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آرژاااااااانیتنی</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99744" target="_blank">📅 07:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99743">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گلگلگاگلگلگلگاگاگاگ دودووووم</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99743" target="_blank">📅 07:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99742">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پشماممممممم</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99742" target="_blank">📅 07:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99741">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یا خداااااااا</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99741" target="_blank">📅 07:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99740">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99740" target="_blank">📅 07:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99739">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گلگلگاگگلگلگلگاگگاگا</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99739" target="_blank">📅 07:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99738">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اسکالونی با این تاکتیکت ریدی برادر من</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99738" target="_blank">📅 07:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99737">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نیمه اول وقتای اضافیم تموم شد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99737" target="_blank">📅 06:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99736">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">از اون بازیاس که مسی با یه شوت پشت محوطه قراره بازیو در بیاره.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99736" target="_blank">📅 06:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99735">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">عجب اتوبوسی چیده سوئیس</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99735" target="_blank">📅 06:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99734">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پایان بازی آرژانتین و سوئیس در ۹۰ دقیقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99734" target="_blank">📅 06:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99733">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">9 دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99733" target="_blank">📅 06:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99732">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آرژانتین داره فشار میاره.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/99732" target="_blank">📅 06:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99731">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb5d00cec.mp4?token=YGkK_R5ynrvBdtV5hAR6wvW3_JCpTNQQI8LSZi2zL4Y9Ic3GHOx_Ie0EWlaZOm3EjOZNmcGcKXYTTtJyiUs3IjIoiPVwsbI_wFRP27bd3-P_RYKHbaLUtEtAXaiiyrgWvpeh429NZh2myQK-WF6IIZFi2rSl0vQsIfyLs3xJ8GSiTvYDHs17_ft6j8oRvhG5GKR_8nDs0XLqwHnCZ9SfPLST294qY31tqH-WKVyQwcgrqCGDRVa3-Vq0dDYQ3UBUrqy0lw8aUOLKLWWBsuAdgTK342PAQakHULT6EAvo9cDHiA1TSzyE76bWTranRC1qr7p9vY5i1nD5WJwG9CvMEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb5d00cec.mp4?token=YGkK_R5ynrvBdtV5hAR6wvW3_JCpTNQQI8LSZi2zL4Y9Ic3GHOx_Ie0EWlaZOm3EjOZNmcGcKXYTTtJyiUs3IjIoiPVwsbI_wFRP27bd3-P_RYKHbaLUtEtAXaiiyrgWvpeh429NZh2myQK-WF6IIZFi2rSl0vQsIfyLs3xJ8GSiTvYDHs17_ft6j8oRvhG5GKR_8nDs0XLqwHnCZ9SfPLST294qY31tqH-WKVyQwcgrqCGDRVa3-Vq0dDYQ3UBUrqy0lw8aUOLKLWWBsuAdgTK342PAQakHULT6EAvo9cDHiA1TSzyE76bWTranRC1qr7p9vY5i1nD5WJwG9CvMEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخه مرد مومن وسط زمین چرا باید اینجوری دایو بزنی؟
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99731" target="_blank">📅 06:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99730">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بخاطر تمارض تو وسط زمین کارت زرد دوم رو داد و اخراج کرد.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99730" target="_blank">📅 06:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99729">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">امبولو اخراج شد
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99729" target="_blank">📅 06:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99728">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b4b3a32c.mp4?token=P4nr43a0-pShxo77lCPL15BjDb_7qmyISzaTa9y2J46eNSwdJCGsVvsoBMxOh-pV9j3Q16jrThfidkvcoaCGZ9Ik297oF22BMHhKWffv_H5WfDZ8zJEEHdJIKKaqEHL_3iYa1wY3_k1muIyoE9lBXFGmfFl3NsNEZ094S77AtfyijgTToc21_P-z-clexlc8_UkPJBTleUySPEu4Aa5VanGP1PY9VOUuM78QdnwnjnW32SsJQygfO3NIkqdbRnEDewksLq-fcgioWoeTiLSbWyPY7lzP8FWkPJVbxBJjk-2JyMRGpocXBA9uF8fRW2xEFsKPT7DhGet1rQ_qAXzorg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b4b3a32c.mp4?token=P4nr43a0-pShxo77lCPL15BjDb_7qmyISzaTa9y2J46eNSwdJCGsVvsoBMxOh-pV9j3Q16jrThfidkvcoaCGZ9Ik297oF22BMHhKWffv_H5WfDZ8zJEEHdJIKKaqEHL_3iYa1wY3_k1muIyoE9lBXFGmfFl3NsNEZ094S77AtfyijgTToc21_P-z-clexlc8_UkPJBTleUySPEu4Aa5VanGP1PY9VOUuM78QdnwnjnW32SsJQygfO3NIkqdbRnEDewksLq-fcgioWoeTiLSbWyPY7lzP8FWkPJVbxBJjk-2JyMRGpocXBA9uF8fRW2xEFsKPT7DhGet1rQ_qAXzorg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل مساوی سوئیس به آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99728" target="_blank">📅 06:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99727">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">همه چی بر عکس شد</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/99727" target="_blank">📅 06:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99726">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پشمامممممممم</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/99726" target="_blank">📅 06:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99725">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دایو زد کنسله</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/99725" target="_blank">📅 06:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99724">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آرژانتین داره بگا میره</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99724" target="_blank">📅 06:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99723">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پارادس شاید اخراج بشه</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99723" target="_blank">📅 06:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99722">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اوه اوه رفت وار
😐
😐</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99722" target="_blank">📅 06:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99721">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUjxM7e2JGPRRy6ekOIQqoHNOxg_x46z6-o9AmsAoAfvssM6rokhIV_7tdnc5KVlzqAqVpcHfTIzYUmuRzWAsnTnR9xvLkqTEzUttUdACshYhKxL6zAgvt1LlwU1FOY2stL_WHeuXxbDb6_VSinGXop6FP8bE3TICdmcDrlC5tRzsjBGMfwA_n2DQzMjiyrUbJjPLSIlVuNK2WrQZslbT-k9QXgmwChveNUMKsP4VCXd7CV89EDexm1TU1W4OSb2FAYOpZIDEoS8o8V9pj_0UTWNJWGPERSjEEqRk162xPb7K6upeM530Zo2FCiaeXywmZLfefpVBh4S-pGcQyoaqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99721" target="_blank">📅 06:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99720">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حالا بازی جذاب میشه</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/99720" target="_blank">📅 05:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99719">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گلگلگلگل مساوی</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/99719" target="_blank">📅 05:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99718">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پشمام سوئیس زددددددد</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/99718" target="_blank">📅 05:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99717">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گللللللللللللللللللللللللل</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/99717" target="_blank">📅 05:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99716">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNP3Z5Ek7_zZGimv9VHNsA-e5ty-QNErEVtCe74BXN8-_a-zjDuF8beW4QaZnDgb3Rylf7R0asQwFAgcRlz6iPYSTNTMQ08hrnlL1f_6uLUYjUkSW1dIkXAOzjWL0pBa6VNkhnEjRQNOq5qHD4mjut079g19xLitgVByb0ZHHnzqNWCMZl7T5O5R7MSIcFzAL6l-0RgjsFrHAYLbyZ4Ey3Ja61kUs5-1rsuhWxMsSoqhfQYMjeJvOk9vu4bveaixGBN_lGS-JGCDWpUdoSB8Z0ugxKYbMGU2bhPNizZSHO3cDewVxuktG5qeETEdWq8Vn4r0gx7-os09vk4jIUShrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
صحبتای مسی خطاب به داور بازی با سوئیس: با من درست صحبت کن و بهم بی احترامی نکن چون منم دارم بهت احترام میذارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/99716" target="_blank">📅 05:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99715">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">لیساندرو کون آرژانتینو خرید</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/99715" target="_blank">📅 05:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99714">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بریم برا نیمه دوم</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/99714" target="_blank">📅 05:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99713">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3BwW9hT0ytNgNiz4vVJAx7kWeVY0naxIbo8Bbo20JIU2jJ94u9wDAfhbaVgHi4Zz1rSymA9F0Sbt4vXIjB8tdQRU3JK8Vu_0X42TFZms6s76d9gnMpkj2OsA7o7Tw5WNCIB9_l4C04heKzeSnlQ1pD-nHLKusG0Kr9ThCPtzFl8rjzRHCAXhOq3GkqbXwXJIsAO9JjSDTCX7RfSQc75cio9XFUJsL-mKXX2wHlZBU5y5IyQ_QakK_Dbp1vCnRxzZpivlC9fhA_B2EeN50-gd6e_mbn2tftNFZrkA5LOyIN8HDBRHcbNg0PoAuaey2J3d44EAcPYfg2zA-2tVG3EeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر عکس جوون ایرانی که با کلی دغدغه و مشغله فکری و هزار تا استرس میشینه پای بازیای جام‌جهانی تا شاید چند دقیقه بگاییاش رو فراموش کنه یه عده چند هزار دلار خرج میکنن و بدون دغدغه تو همچین ویویی بازی مسی و رفقا رو تماشا میکنن
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99713" target="_blank">📅 05:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99712">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wA3CKOQUf3p4LiUU0eqa5Ji5J-UzEMvdrPZzXKmrA-SwCclD1BJM7aklnZa1SruYdHDC8XhQUN-gaMdD4uico6z0wq34U2117kaz7jA459Y7mGTJmPB0MbQnOFD51n68AOXn_HAMZN_DlDl6zs89bLQULf9qtZT5yPBEn36_NAhB0_Qbsiwske_3xCY0FoCAA9NrsU3XOzawREx7xkDipDISYjkJMp3w0Rys7zmLey444kasDYkEdS9ESzF718C4s7psKKaD7y8krxOMqHE0CTrfuJB5-VUQD5UG9nDOJhZrBmkqB76jgtuPFRinFzS2FE2g2cVjn8qmWdtHANLuDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇨🇭
آمار نیمه اول بازی آرژانتین - سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/99712" target="_blank">📅 05:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99711">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
پایان نیمه اول؛ آرژانتین 1 سوئیس 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/99711" target="_blank">📅 05:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99710">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKZ1IxNYpoTkEWrc02qVrlrIJsMV_ywbhPMIBZoaHHe0NEK7WtErA1n2CU32w_cd5A8hEVU0ZDPyzFH5o7X4fmWZzPIIkRKv2Z8xkgAxKaTNAWVgk9FJIcIN9XYL4vLVMiyeQchKYz0l14tHA0jbuKZlKKO1Jl46no8RerDn36t0TmwADwMOjNVHl0evyoxV3Dm80FIZaGOxOtW1oeNodOQ1IKV-OHiIAJ6jO3825rEec6TVQsvN4LfJsVucLqzwD3Hg6oJ8EKuYlaiHo2ezrwqb0C5kGfr-4d3datj7VA3xjHtgzdIR7ZUsZdA6TF4CTppiTsnLHnv_ff-G9ovvhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقی نیست اما مسی با قد 170 سانتی‌متر روی سر آکانجی با قد 186 سانتی‌متر پرید و هد زد.
اینقدر بازی کصشر بوده که باید همچین چیزاییو پوشش بدیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/99710" target="_blank">📅 05:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99709">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دعوا شد</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/99709" target="_blank">📅 05:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99708">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">برید دینی بخونید از این بازی چیزی در نمیاد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99708" target="_blank">📅 05:13 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
