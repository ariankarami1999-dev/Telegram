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
<img src="https://cdn4.telesco.pe/file/i871apWkffRI_T15boix7iBelk-uQC8wQk7xfuk8hbA06nZiHpYC5eBI391lrpgdQtRMcsfmSdjrLHUu3DPzlPMxdgEkOlCH8wOSpBXoORbcCNEEzQkuEYSef0fQp-rUeazATDWCCnEkEUYDbX_mnurg2AqhOd8vnVbSyuMkAl51LRxZPbKLE_ECK3aLzpIN4kROSNeKqFy_bV-fwxph1yvMwdnS0TAMAnhpsV22V-X9qEiTcURTpAa9Th3cBc9mWYLAojALwsIReDNDEdaKfq41WHc74x4jN--zgqU4aU7vCFobrRDUogv361juSaq40T4JcskFZ_wV12ObN0yGuw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 169K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 15:44:21</div>
<hr>

<div class="tg-post" id="msg-68258">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">💢
مرد پاکستانی ، عاشق محمدرضاشاه
@News_Hut</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/news_hut/68258" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68257">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQAQu4QGRgmmrmAx1TiISUP4MZ8RJw7k60uNrrH_FiumPmJjycEIe7yjJld9T4g_atTXEtiP1zm59MYe2lQuSFPIrqySiRXjVh63tAAC98jS20_MrnvWQMaUVhMfziSWR63HvLCIDUftSZO9LM-raoQa1vahjUTrfz6YPEDPx35XyEKpWJ1_SLtjWUejfMTSbfsetKH8vP0eibqT8LNcMWLSOfYAO7q_rK3gYxujcw3-teqG_pkxmiuwChiRF9hk6iOziYmtMGfGHJ5E57gG8Z9l5OoqjeDV_gN6UfIDpxp3yp_k-xCL4nky1cITLh1jTVzIothHA-wf-VJC6-T4uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نتانیاهو سفر برنامه‌ریزی‌شده خود به ایالات متحده را به تعویق انداخت؛ این تصمیم پس از آن اتخاذ شد که مراسم خاکسپاری سناتور سابق، لیندزی گراهام، به زمانی دیگر در اواخر ماه جاری موکول گردید.
@News_Hut</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/news_hut/68257" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68256">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=Oseok4iiALXD89GC5wg8kt2dhu00nrgQt8qkm8RoWrZAG50P5RuJZHNW608m_A4xeW4Q6HvaNxqzPfQ0poqUrUUy033HveKEna9ir2Mvlnrmpy362j1Vu8telMoZONPdJ1_YsFf6S8JrTmsS2QN233NPZ58sLJcBFR-mz2nMB3--M6GY7NtJyupzPCmloxziddEp13c7PX6lANSJC5Dpqye9qsLTe2PqhaObQ4c7Wc4zr5zwBIzwfwldfljIjav5LeEwr_EuIWZ9JVxG_vtJyWRx2OcAsgKyCfJ_XumKvaByCovtG_dhL3fLLUf8TbpAMBmgMXTJwd7fIp0Nif1y_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=Oseok4iiALXD89GC5wg8kt2dhu00nrgQt8qkm8RoWrZAG50P5RuJZHNW608m_A4xeW4Q6HvaNxqzPfQ0poqUrUUy033HveKEna9ir2Mvlnrmpy362j1Vu8telMoZONPdJ1_YsFf6S8JrTmsS2QN233NPZ58sLJcBFR-mz2nMB3--M6GY7NtJyupzPCmloxziddEp13c7PX6lANSJC5Dpqye9qsLTe2PqhaObQ4c7Wc4zr5zwBIzwfwldfljIjav5LeEwr_EuIWZ9JVxG_vtJyWRx2OcAsgKyCfJ_XumKvaByCovtG_dhL3fLLUf8TbpAMBmgMXTJwd7fIp0Nif1y_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش مجری‌ها وقتی یارو میگه تشییع خامنه‌ای ۴۰ میلیون نفر حضور داشتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/68256" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68255">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBUImbbH47PBsBuzbROs_rCZR6MuveW8wPebRjITDIs8mt3IdTAl5KOPLYPFw_lUCT_jozJeHygH23A_Rt5e7DNz8HfzhcF5eaBTCiq2-mlvCelFi3dh9VGYYg8t_1BESNimim7Gaa-pGsZhwQoBTLBhJu9gT-fJyigglcSYmcfgW95wkC33cyAuQHaSXlu61-jogs4Hrlg8JDreQ_l1vXfem2Zp79kJ1yQTaDISuf9Nfj3XTp3ALkrQld4eIchxonPfYji4GFp449m7zfqMHGf_SWqRsDGMr_xb7n7W9tlGk-8uPzBs20MSbDlJot9Ps0mDjMgu6sBZUi55d6poNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فینال جام جهانی 28 تیر (یکشنبه) ساعت ده و نیم شبه؛
- یازدهمی‌ها فرداش عربی نهایی دارن
- دوازدهمی‌ها هم دو روز بعدش عربی نهایی دارن
بهترین راه اینه که فینال رو با گزارش عربی نگاه کنید
دیگه عذاب وجدان نمی‌گیرید
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/68255" target="_blank">📅 13:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68254">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAYYGzolDVf-pU7j2k1wg2DzFBp2rHWkRBk4Q4_58StwiRi1g5M1sNF-cTWZvUJtuM8yCvSl03KNAW0PGCmPIxg2vnaqlZFzDrwd2m_7eFOQM-bIfCajeMSDRAOsbWonYMNv3Yj4UgNgOHSd-xsCFYIpbZ9LB2c_fG9hZFij4-objtwUtTQdv7FtQQdGiZs0UufGZ_LGpkzp55dt7f91ru67bTj5vYR9ojzCbMTA1T_S3puszBY0KI_mTZY90F8jQxOe_X3BSAtSAMcR43n3sPG2WPrRPEr2Ab4sVAhdGTXLZiG77jL31zOnfLn7f_zc3gXTt9yWV9Pf5oiTSudqxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:  کارگاه قیرسازی حرم آتیش گرفته!  @News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/68254" target="_blank">📅 13:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68253">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=KyQLTae1nmQEVeW38HABCxud_WkMPPbew_SKjYTX846wz7NQYVGDxY0uw1nB_p2y88ZJFXsfSk7J5hyilADCRL_8gn7mfsx50lwxwAzrLV0HM3lNCgq3T-YQGrNvc60LwWWCo42a3RK1Ue2kQYzV0WfAcKZaTy9pS8Q9S6TLOZslHTGgDTBiH4h7iuiRp2XVcVm52tZ0bglu_5XzmGaL0XAV9KnwPMReaVrpJi7yPGUYXg3LXUQ-2EDZH8C42yLrpxlyDG-SEMK2wx8pO80-maeJBkCNUCTRHaHlV6ZnqtyvnUowKKAmdHXd9yq20bUg_q6_2JdK6iALRMedhp3AJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=KyQLTae1nmQEVeW38HABCxud_WkMPPbew_SKjYTX846wz7NQYVGDxY0uw1nB_p2y88ZJFXsfSk7J5hyilADCRL_8gn7mfsx50lwxwAzrLV0HM3lNCgq3T-YQGrNvc60LwWWCo42a3RK1Ue2kQYzV0WfAcKZaTy9pS8Q9S6TLOZslHTGgDTBiH4h7iuiRp2XVcVm52tZ0bglu_5XzmGaL0XAV9KnwPMReaVrpJi7yPGUYXg3LXUQ-2EDZH8C42yLrpxlyDG-SEMK2wx8pO80-maeJBkCNUCTRHaHlV6ZnqtyvnUowKKAmdHXd9yq20bUg_q6_2JdK6iALRMedhp3AJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تسنیم:
کارگاه قیرسازی حرم آتیش گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/68253" target="_blank">📅 12:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68252">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVaCSL5XtNsXqbHm2kH6a6Q9Wg8OlXq9S6wURjxJYxxTTEly5YlRYruV-8iinUOcmqBkecFMED7WfLubedV7GG8dKqc6OW-jk9-gYJFAVmOkaiD4ch1CBVttx2_NBL4l-qGUTKFAcP-Jkb3IIWHGNLHkbXhybrKOQlO0SgbPMgIHx7aFdqzCFsZaSz5QUVtYOWwPI0mgo-ZXg_JMjcE89AMxh8DP1SK0vcceHb9rIHgwaCUd-8Tl6k9pNjUzWpfwpeM1xo_qLvxrxlt391gNF9FQQsUkkRL09KaVv2_MvF0kAx0tO9ysUrwX2ftyS6MvTJIdk3ViyPJKX2cVASEHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتش‌سوزی در حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/68252" target="_blank">📅 12:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68251">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/314324694e.mp4?token=W6BvFi11QIA_YFtSL87B0voeKMIzqAIUU5-QePjIbZKDbx4INGeeM1_4HnBw7rCjgC4upCEl8EMr-Y3PVgncRFKQVufjZGIjI9z-nFywN6XRgLrXx_lfQmRTFhwE47hNCLzJddNBzJEypBkzbg0LKhi2QviC15Kx1D0e6LAfRpzn_9CceH90TOF1Z4sjZ60ESQy74GackiBnvL9RMgac09TJ_cFmq5JcvL3I49EFjpCSyDV7f7ubI9Qa278G_Kn5sx7ZRfR0Fi_FlbEnhR7QHvCZ6zJU0VWG9YthXCzv85zBL4pWOdUdjj0cWxI94OvRtIaa7xCLzxviTvczAsz_76G0DqxQyDAqW1G_FNmO1GUpgCOu-Bi7ZLoN3ZovuzU9HnEO5E_uN5OfcVVr2ignhUpfB2jRMQOkz_V7OMO2CD9VpgYcliMsDzZwMmaRk1Y3v3gaFjKzd4uCPkajxFe2eCs1YixdsPAorD-9F4CPGbkiZJXw-UWJXjZ5y56M0V55Alsu2rhEO1ER0NfV-5PLkwFHXtQN_GlzqfhRNdIwlclDKVaVxUMit34L1kQ4siM-8F9BX6u8qx8BFnq6n17cq7NcnxmGE45Pz2UzrsWumkG0u0u7XSVYMMkWvdr_vLaB4b35QYrNLq1Pi2bTkO_Ur7E4x_WqMt5yg6Go4JbFGpI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/314324694e.mp4?token=W6BvFi11QIA_YFtSL87B0voeKMIzqAIUU5-QePjIbZKDbx4INGeeM1_4HnBw7rCjgC4upCEl8EMr-Y3PVgncRFKQVufjZGIjI9z-nFywN6XRgLrXx_lfQmRTFhwE47hNCLzJddNBzJEypBkzbg0LKhi2QviC15Kx1D0e6LAfRpzn_9CceH90TOF1Z4sjZ60ESQy74GackiBnvL9RMgac09TJ_cFmq5JcvL3I49EFjpCSyDV7f7ubI9Qa278G_Kn5sx7ZRfR0Fi_FlbEnhR7QHvCZ6zJU0VWG9YthXCzv85zBL4pWOdUdjj0cWxI94OvRtIaa7xCLzxviTvczAsz_76G0DqxQyDAqW1G_FNmO1GUpgCOu-Bi7ZLoN3ZovuzU9HnEO5E_uN5OfcVVr2ignhUpfB2jRMQOkz_V7OMO2CD9VpgYcliMsDzZwMmaRk1Y3v3gaFjKzd4uCPkajxFe2eCs1YixdsPAorD-9F4CPGbkiZJXw-UWJXjZ5y56M0V55Alsu2rhEO1ER0NfV-5PLkwFHXtQN_GlzqfhRNdIwlclDKVaVxUMit34L1kQ4siM-8F9BX6u8qx8BFnq6n17cq7NcnxmGE45Pz2UzrsWumkG0u0u7XSVYMMkWvdr_vLaB4b35QYrNLq1Pi2bTkO_Ur7E4x_WqMt5yg6Go4JbFGpI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام تصاویری از حملات به ایران منتشر کرده است.
این تصاویر شامل برخاستن جنگنده‌های «اف/ای-۱۸ئی سوپر هورنت» نیروی دریایی ایالات متحده از ناو هواپیمابر کلاس نیمیتز «یو‌اس‌اس آبراهام لینکلن» و شلیک موشک‌های کروز «بی‌جی‌ام-۱۰۹ تاماهاوک» از ناوشکن‌های موشک‌انداز کلاس «آرلی برک» است.
اهداف مورد حمله شامل پرتابگرهای متحرک موشک (TEL)، سایت‌های پرتاب پهپاد، هواپیماهایی که پیش‌تر قطعاتشان جدا و از رده خارج شده بودند، و یک دکل مخابراتی بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68251" target="_blank">📅 12:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68250">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlO0y1BmTZlmKQHlE1PGh47EtMZTwinyZEpmWw_aCDqNEv2Z0EsOIdfkNg6nIrmBp8B80xwcus7a5SmE8Za33zu9hFVO6XcdVLRORTLfeqkX21yaRe2Pp3IaxEAOOy3tcm4WC5-JJOVV797hTm9DsTZkW-LSX4SiDnbbJ2aFyLpvAk5RxTQ3tMVxcxd7Q2kWJwbo6rU99HVuHf3F8ITQWhcG4mI2zHrU2Tj8yZm7QEYw0MU9bME5t8qs7265MS66i-rcvL_DL9NAnaTDZBuzjaLiZTLvSOlaQWak1m14jYjMdBDRCm5LAXdcj1y1fgftEePnjDW7nXK385rjiv6CVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ:
ایران اجازه داده یک شهروند آمریکایی که در دسامبر ۲۰۲۴ و در دوران ریاست‌جمهوری جو بایدن بازداشت شده بود، از کشور خارج شود.
این زن اکنون در سلامت کامل و شرایطی مناسب خارج از ایران قرار دارد. آمریکا از این اقدام مبتنی بر حسن نیت ایران قدردانی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/68250" target="_blank">📅 11:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68249">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=nTjCUxwO1M8kkDwqZCkbouyunaNn_-U9PfFj8jeumDxXwMzwTwSCo48YnFSOAMZUrmnIECCNw83-kGCEoSIZU5H_7gsdjJR9gfmsyY-aRczK4O140OgBd0r9zJ212rW9I3oA3kLqYm0MqItUvo7gSH9YCd9vkijJsoJMXYhjJsEfWy_2uiwTq1R0gDgsdY78TGRn4ivXkIAyb1DtlofHCD7m0znjT_DpGXm1GbmPmRst7dwCy4MzyYhzQPfHbNgakTQfCjwGaTBgwOgGz14mxhok3KfDcATiqmLwJAwOMrW0RUJTwPKbEVu4GGb-GJ9efS8fwPAnJZbz-RSui_q4qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=nTjCUxwO1M8kkDwqZCkbouyunaNn_-U9PfFj8jeumDxXwMzwTwSCo48YnFSOAMZUrmnIECCNw83-kGCEoSIZU5H_7gsdjJR9gfmsyY-aRczK4O140OgBd0r9zJ212rW9I3oA3kLqYm0MqItUvo7gSH9YCd9vkijJsoJMXYhjJsEfWy_2uiwTq1R0gDgsdY78TGRn4ivXkIAyb1DtlofHCD7m0znjT_DpGXm1GbmPmRst7dwCy4MzyYhzQPfHbNgakTQfCjwGaTBgwOgGz14mxhok3KfDcATiqmLwJAwOMrW0RUJTwPKbEVu4GGb-GJ9efS8fwPAnJZbz-RSui_q4qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پهباد شاهد در حال رفتن به سمت پایگاه های آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68249" target="_blank">📅 11:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68248">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b8221101a.mp4?token=USAzWNXmfW-Tg4_-aAqTAEyeo2Z9tQycbXDBDoVN9PLvKaf5dngueVmva82FhMvr7NnCs8DDpo8cMsKaedfnop03ANZyrszP2O8qP6CxEINm0D3Dct2sRnufrZgQ6u9XXCZVxnwiIx11Pqna6R4fug1dg2OmUuuxc-AGP-xXtlo0tBausAPNe3nPe3XQMU9eWE0rj_Nak082iYjezpSqEIK8Kh3ppXqnXqIYhwM1VFLnhcpsc3sFt20-F9NnvO8e7YfIc6JioIEKGI0fo2fK6ewJO0kAbx-9Nm_CyxzIXXHDV4XnxCqrzk17VwT1VUq5IoQwwfCZzC_ZfFAeQNmKtqnfHO3hotQ8GhgdCOpLmxVpBxGvndqf2LX2MeaooaZPvxwT2npRh4xmjEMyOorgf2yW02YVgrOczx5AemWgWg9lBf8WQDxATCWp6rtRRnfxDxGmn-fA08gnhrZ-IXA7DOiBmHoqEFEb30tFhdw_DMVSplL2LUvu4ijj_r55xznqXITXUENpWaeiFWJdTsgxJMEm6lj-EOE3_xlFlovk2I7AyuzxT_N19-0jTLBnNMcTnx_c2fKuXGPKuUQ88tttJOi-cn6hpCz1f1B12L4eL9avmIxm-p2eC8wJ7Th21djIwRMl2u2otnZWutbtLif7JpwzfZgQEYtzUxEFYnxiiL8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b8221101a.mp4?token=USAzWNXmfW-Tg4_-aAqTAEyeo2Z9tQycbXDBDoVN9PLvKaf5dngueVmva82FhMvr7NnCs8DDpo8cMsKaedfnop03ANZyrszP2O8qP6CxEINm0D3Dct2sRnufrZgQ6u9XXCZVxnwiIx11Pqna6R4fug1dg2OmUuuxc-AGP-xXtlo0tBausAPNe3nPe3XQMU9eWE0rj_Nak082iYjezpSqEIK8Kh3ppXqnXqIYhwM1VFLnhcpsc3sFt20-F9NnvO8e7YfIc6JioIEKGI0fo2fK6ewJO0kAbx-9Nm_CyxzIXXHDV4XnxCqrzk17VwT1VUq5IoQwwfCZzC_ZfFAeQNmKtqnfHO3hotQ8GhgdCOpLmxVpBxGvndqf2LX2MeaooaZPvxwT2npRh4xmjEMyOorgf2yW02YVgrOczx5AemWgWg9lBf8WQDxATCWp6rtRRnfxDxGmn-fA08gnhrZ-IXA7DOiBmHoqEFEb30tFhdw_DMVSplL2LUvu4ijj_r55xznqXITXUENpWaeiFWJdTsgxJMEm6lj-EOE3_xlFlovk2I7AyuzxT_N19-0jTLBnNMcTnx_c2fKuXGPKuUQ88tttJOi-cn6hpCz1f1B12L4eL9avmIxm-p2eC8wJ7Th21djIwRMl2u2otnZWutbtLif7JpwzfZgQEYtzUxEFYnxiiL8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو وایرال شده از یک جوون طرفدار حکومت:
من الان شرایط ازدواج ندارم چون نه خونه دارم نه ماشین
بدیهی ترین چیز برای ازدواج اینه حداقل ماشین و خونه داشته باشی اما خب من ندارم و پدرمم پول نداره که بخره
دلیل وضعیت الان بخوام کوتاه توضیح بدم ؛ سخنان حضرت اقا یک طرف ، وضعیتی که مسئولین درست کردن یک طرف
الان ما باید تا30 سالگی بدوویم تا بتونیم یک زندگی متوسط درست کنیم
الان یک میلیارد طوریه ک ما شما با هفت الی هشت سال کار هم نمیتونی بهش برسی و انقدر هم پول کمیه که شما باهاش نمیتونی یک واحد اپارتمان بخری
با این اوضاع 50 شبه کف خیابونم و هیچ ربطی بهم ندارن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68248" target="_blank">📅 10:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68247">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⏺
صحبت های روح‌الله زم درباره حلقه نارمک و جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68247" target="_blank">📅 10:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68246">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYp0b4gh2gqoRfL4EZJ4w83Wo6HR2FSR6N_CWh93-_x0xmKCjvCLGNkRRbCNPGp9l4_-RBU8v654nIZbKtg3Wj8khi_HbEIJTVNyO7D6Gujjl7ob3jAhXZTVuCCK7QXTBRyYJydz-VftSUzp-vWEO5la7FhlTFHDYYOFVUQPKW0mhvO-cL_PLxbuNDpHnSZMg_nePjojVXYhLLeZ2Gdu1Li7Hos9VQgcgYmEwmPsQWfX9uGz_pxsXh3kNx22gQlEclPrOtYaVbnD8BUEbzwk8XRR_bO-YQDAobLcTlWCN-H6aeCxMvZEvy6NFFPvYLHnO9Yfx_3MuQiv30ylMQZl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سی‌ان‌ان به نقل از دو منبع آگاه:
دونالد ترامپ، رییس‌جمهوری آمریکا، در حال بررسی گزینه‌های گسترش عملیات نظامی علیه جمهوری اسلامی است. به گفته این منابع، در نشست سه‌شنبه اتاق وضعیت کاخ سفید، راه‌های تشدید فشار بر حکومت ایران برای کاهش کنترل آن بر تنگه هرمز بررسی شد.
بر اساس این گزارش، ترامپ احتمال عملیات برای تصرف جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، و حمله به تاسیسات زیرزمینی کوه «پیک‌اکس» که گفته می‌شود با برنامه هسته‌ای جمهوری اسلامی مرتبط است را بررسی می‌کند. با این حال، او گفته است ممکن است عملیات زمینی برای تصرف جزیره خارک را کشور دیگری انجام دهد.
سی‌ان‌ان همچنین گزارش داد جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگویی تاکید کرده است که جنگ تنها با ابزار نظامی به نتیجه نمی‌رسد و در کنار فشار نظامی، گفت‌وگو برای حل بحران نیز ضروری است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68246" target="_blank">📅 09:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68245">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68245" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68244">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sh2c7CiExExDZH_6VF5C6tdVG9rMUcQGnyFGy0YG7fkVv3rn24zEBONEuOkVky__U2AwTVIl1V61XIi8mVoThO6LluGLhJ1_4gJmhR3v_I5fxTpXnEpIPNLcP9cOOjNzPoQyGVWIp7eU-3_x8m0hUUMY-H4QgroNE9B4eCmaYDS0EZw8QJI68S7Fad7iCMpkYM0MtQrAk-ekT4BQbhKGipAWZL8jx4YhG9ts85QvYURc-ny17Yig0amG5SznsBvdh1IoObbxCkjpseh2ytTZiQ9eXJV7pPMRNvE6YvpXC2lGT38tjBPnb7Aj-5LITqBLdIy8YkKIKXtM7dHMGB9LIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68244" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68243">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4873db94b.mp4?token=Lo6AKHUP9Fk5clS3OJv7rfYNKvB54WW8jUMgCw6mOEWR93gtkwZoH-K26lV2Y-R4qg-tw9LA0oive37t8nvjQm_XCAL9k_6I_ALK5lyxXFGyLoAaKVK1F5o3b62awdb1gSdF0OokYztiQ3EMXeIIfe4AHUb1fF09Uv4uGUvy0fc2ndPT01cMyYzeEeYJb1vUdMupmXPEC2_NlZ9l71K3McweZbSXPDPCH4M8StvJYKA7RGBzAKNSVcGS4i-IFi8h52cbEuUQRIeEvDC1Xt_fdo8ycQh-Fqk2T_JK8RfHdmbUdmROJxer136IgwR15hqCYaUOd3hqwwQ9fESQmsmcbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4873db94b.mp4?token=Lo6AKHUP9Fk5clS3OJv7rfYNKvB54WW8jUMgCw6mOEWR93gtkwZoH-K26lV2Y-R4qg-tw9LA0oive37t8nvjQm_XCAL9k_6I_ALK5lyxXFGyLoAaKVK1F5o3b62awdb1gSdF0OokYztiQ3EMXeIIfe4AHUb1fF09Uv4uGUvy0fc2ndPT01cMyYzeEeYJb1vUdMupmXPEC2_NlZ9l71K3McweZbSXPDPCH4M8StvJYKA7RGBzAKNSVcGS4i-IFi8h52cbEuUQRIeEvDC1Xt_fdo8ycQh-Fqk2T_JK8RfHdmbUdmROJxer136IgwR15hqCYaUOd3hqwwQ9fESQmsmcbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پرتاب‌های متعدد موشک‌های پدافندی پاتریوت به سمت پهپادهای ایرانی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68243" target="_blank">📅 02:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68242">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1519c2ac09.mp4?token=TMRPmpKlyVsYXg-F9UvJ2nAeu9ISU2Ev4nxt0pKftAWGPLuh2e5U2E3MASDMqDzdOVaDfao_CwWHhgDpQy1CLURjBqOFowxit0AJTpooBkoy7ewXoXsWsjhXgkKAmnLaETr4jpx-FQnTMMWE0xNTxG5ycuM5w7noeeutC6iJYXb1pMUBZCFE01SUKcFBSosBysya_uPPOVEVpa-WmaM1xO5sj0sUnxta1KRydC-iBhu9ZeKjojspLdCnwK2PXSsL24zF6jBAhy4nE0S2ceKaWREPKUo5LSMYAAX6ZY0EUovpCS7uDYBiZmTjKW5OfQwH5C0zuz5NRT3egFQ1uCzezw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1519c2ac09.mp4?token=TMRPmpKlyVsYXg-F9UvJ2nAeu9ISU2Ev4nxt0pKftAWGPLuh2e5U2E3MASDMqDzdOVaDfao_CwWHhgDpQy1CLURjBqOFowxit0AJTpooBkoy7ewXoXsWsjhXgkKAmnLaETr4jpx-FQnTMMWE0xNTxG5ycuM5w7noeeutC6iJYXb1pMUBZCFE01SUKcFBSosBysya_uPPOVEVpa-WmaM1xO5sj0sUnxta1KRydC-iBhu9ZeKjojspLdCnwK2PXSsL24zF6jBAhy4nE0S2ceKaWREPKUo5LSMYAAX6ZY0EUovpCS7uDYBiZmTjKW5OfQwH5C0zuz5NRT3egFQ1uCzezw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68242" target="_blank">📅 02:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68241">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aci8UzDiFtULbTKoiiPmNABF4E7oT1bYeFeHu5xYqiVw4LJPP2wLWEigl66C5kd_5qTCQfRIqF1uz3UR3wDlU0vtm9J7_bABcbMYqQF9l01oCvBtodrTD95asWZTpwJQq6ZrbSGfmWSzOtfW9kFgiFKZLg3-JVtN_AuqURNh8T5WAz-EbL0knrnwuCeErC4DQiByKAMh7vVBdGWr_wgKdq2aj3wJTIa3lKWtmfodE87p2-2GRc5OIhn3KG_LOFftsgzsgLGySd_cbQMlkfbjS0eNKHyteMOaqgAytJ479LsYQOmfJ0fxR5N0AYfi0z9hhOaXe7xRY3eYvnm7gqSWiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68241" target="_blank">📅 01:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68240">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68240" target="_blank">📅 01:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68239">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd7e59689.mp4?token=hdLmN7Z-ORDhQkK4cjxM2_hD5gLaaCFqETPgjdH12DoQVPKsom2OzhKmz_PP4xSrhKFGG5XCICrxQ5vwzGV-qyzcnZHp9mYuIafnJZ8u8ea18r6Xc3O_QDE1Fu02-rakOc8tuuiYiKUTBnNUlHJwk21iRm-OJqly_Q_DanuZtxPRo9kYXOvgO-ZE0WwHZRRve0ZgWJIPbKYMnIEI35sdOlGjJOcajffPg5VSCMphEb-johMvtagfiGJvf6MTClMaydQyKU10mTMscVGvXbLQP-KGZYS3NRscH4w7fghR50yIWo_90IvpxgF45yPtxltS6FWzlcbPWwNeaAbj67xm1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd7e59689.mp4?token=hdLmN7Z-ORDhQkK4cjxM2_hD5gLaaCFqETPgjdH12DoQVPKsom2OzhKmz_PP4xSrhKFGG5XCICrxQ5vwzGV-qyzcnZHp9mYuIafnJZ8u8ea18r6Xc3O_QDE1Fu02-rakOc8tuuiYiKUTBnNUlHJwk21iRm-OJqly_Q_DanuZtxPRo9kYXOvgO-ZE0WwHZRRve0ZgWJIPbKYMnIEI35sdOlGjJOcajffPg5VSCMphEb-johMvtagfiGJvf6MTClMaydQyKU10mTMscVGvXbLQP-KGZYS3NRscH4w7fghR50yIWo_90IvpxgF45yPtxltS6FWzlcbPWwNeaAbj67xm1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سنتکام تصاویری از اصابت چندین موشک هلفایر به موتورخانه نفتکش M/T Belma که در خلیج فارس در حال حرکت به سمت جزیره خارگ بود را منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68239" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68238">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
بندرعباس بوووم
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68238" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68237">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiZrourKo8VTzQNd10XtY2wz1mVW1tuTmzH8YP9PiLABLBJ-ap_5H9F6WwAQgVL4Y___uPq57exGqIw3dzUZh6CsblSNrqJPOV09VIHDgns9l3CtGq7-7Fx9eDV9NDmXtL1Fa0mDlI9h6MnUhnc4YGnkQFxwL7SZGL9j7VcfnfMKjSDjgg1CGMLIcehLdc6VmkMGXhxlHzpOBH-73M7tp8_trj8ti3q6HlTfXziBkGYVQy7Eo-D0Yq3069M278MxZKDUo3L48CbFQNaJCMKkgCkZiWjX5sYy1_d-1yCvikpDU0GYZqKLRqyITq_IGYvWt-dTz12NbmrycoVsBMsNXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی| امشب روح فوتبال ارضا شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68237" target="_blank">📅 01:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68236">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68236" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68235">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uEQYYWgOAdUAGDHWSJyG01ge7Ol6bl7MfCiPCiPtdm9IRq1x4uMQKXyhOHX8-H_gqyXI-2HUfQ7d2yvPhHO8Okx1WA-_hquLua6zyzlF7Iu1dFRKDQjcj8yFURBp9P05JgQvPPOk-FRpMz8Kw675ExoBDcbPodma0N_rGg_ELnFbX1MTfWm5dR35BHRe4N1G3trohBFhNHT6zLkEaoQ-c2i6rJpKpuZ-j7ZIaBTsSMl_QWmN_RybHlKPp5uW3z6Mr3xSvpP27gSjVLhpmtH9CtbHy3SUodullvtYbprnrONP2WF6PiVsCuL8aVW9aZoSnx_P9Pq4X251B4p43JGuhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی| امشب روح فوتبال ارضا شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68235" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68234">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">من خودم رئالیم ولی برای مسی باید ایستاده دست زد
😑
#hjAly‌</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68234" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68233">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=EdUDwJbx7As6NyBqfp-H2Bai-v3qIKUK4cDVWuzhIR6fJPc4FQ85wjhxYgoFx1lToPqoTp-7Ls4HnCHf3iFLF3ajOIFt5bVLxEa_n5cTqX-rejkDS0PmV9M5L0ZcLx4LmoX9Z7mZP21EjOhL34nn8GAy-eZUnKAzyhywLzolqL44HX747uFy9ujZHz2eljZICAsjr2GnXtJjDIC-tlNQIXEYtRRlFWjfeTJ-m5iPySwnKlRCPz1KejoB1BdDWvDZ9ie3MsskDoVN4md6Dtn6vSh7hjuqVDYNtYV-Quj26t77uRuXVjX2_o9LMBA0dejFKzG_iGo_tOIWh_w45sKPSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=EdUDwJbx7As6NyBqfp-H2Bai-v3qIKUK4cDVWuzhIR6fJPc4FQ85wjhxYgoFx1lToPqoTp-7Ls4HnCHf3iFLF3ajOIFt5bVLxEa_n5cTqX-rejkDS0PmV9M5L0ZcLx4LmoX9Z7mZP21EjOhL34nn8GAy-eZUnKAzyhywLzolqL44HX747uFy9ujZHz2eljZICAsjr2GnXtJjDIC-tlNQIXEYtRRlFWjfeTJ-m5iPySwnKlRCPz1KejoB1BdDWvDZ9ie3MsskDoVN4md6Dtn6vSh7hjuqVDYNtYV-Quj26t77uRuXVjX2_o9LMBA0dejFKzG_iGo_tOIWh_w45sKPSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#hjAly‌</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68233" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68232">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گللل دومممم آرژانتین
💢
💢
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68232" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68231">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گگیایایتیلیاایایاااللل دوممممم</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68231" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68230">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گلللللل تساوی آرژانتین به انگلیسِ کثیف
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68230" target="_blank">📅 00:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68229">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گلللللل تساوی آرژانتین به انگلیسِ کثیف
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68229" target="_blank">📅 00:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68228">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">درووود بر روح پاک مارادونااااااا درود بر بیبییی</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68228" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68227">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کلم کیریه، کیر تو انگلیس کیر تو کیراستارمر #hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68227" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68226">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379978a151.mp4?token=BLeV2XQUn54Oj9majlbV0RPCtuQHoMaylAUOjEO7COFxFBbdjUk2ULelWJrAX7BJXZnC5dY71fJrdrXrAM2_s71f1QkCCweHk2f-dwSV_LEJgPoU2KoOvJnB5gEwbhSJ95YolwbqYFHjyAMQxy5qAcXWwWeKuTL_5LWm9Vr1ddg9PoonSxKQF8R6O-blf0uSH9YtDawZvDfCxoj410DnLnIsmsebZXVtOKKPcaIECVw0uWu6cU2TxqFfu2-mzxmJC0_XLBG-XZfrCA-O8HO47LxfNcKm3xA2C0sPQXAGm3x3ExE-HTmf9GIo_bcBpnQv6wmyjCYtyWv39N4MbSzl2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379978a151.mp4?token=BLeV2XQUn54Oj9majlbV0RPCtuQHoMaylAUOjEO7COFxFBbdjUk2ULelWJrAX7BJXZnC5dY71fJrdrXrAM2_s71f1QkCCweHk2f-dwSV_LEJgPoU2KoOvJnB5gEwbhSJ95YolwbqYFHjyAMQxy5qAcXWwWeKuTL_5LWm9Vr1ddg9PoonSxKQF8R6O-blf0uSH9YtDawZvDfCxoj410DnLnIsmsebZXVtOKKPcaIECVw0uWu6cU2TxqFfu2-mzxmJC0_XLBG-XZfrCA-O8HO47LxfNcKm3xA2C0sPQXAGm3x3ExE-HTmf9GIo_bcBpnQv6wmyjCYtyWv39N4MbSzl2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
جمهوری اسلامی به زودی شکست خواهد خورد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68226" target="_blank">📅 00:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68225">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94485380c.mp4?token=XWgbUwrv_Lm9NcPsfZfJSVl1twj-nFhCiKkHjzWnDt1ieaV6vLt-ShlnoILF9fUJS6CaFmlvCh6EKWdaEfelY449oZhylPEmZG5XDEGuOlVwf76pZuelbMb3D9P3ggfFMYbdYA69bD7XwUrqZVbYE3K5PJHlpOCXe5CEgTGZCoLL1VgaaIIWGDWmM5ZDLNPUenZrmjCwgEl8EfY6gjbNsGNAMJ-SgqrxclnvuTxHSsf5MpC050_L4GcIfmdC0PEpeexpzwGGNzVo93hGt6UQjIqg6S-pV3Cfb873lDwm5TUllqElHtXkKzDPxTkkAmZ8QSKEUCR18vQbew3lTqv3DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94485380c.mp4?token=XWgbUwrv_Lm9NcPsfZfJSVl1twj-nFhCiKkHjzWnDt1ieaV6vLt-ShlnoILF9fUJS6CaFmlvCh6EKWdaEfelY449oZhylPEmZG5XDEGuOlVwf76pZuelbMb3D9P3ggfFMYbdYA69bD7XwUrqZVbYE3K5PJHlpOCXe5CEgTGZCoLL1VgaaIIWGDWmM5ZDLNPUenZrmjCwgEl8EfY6gjbNsGNAMJ-SgqrxclnvuTxHSsf5MpC050_L4GcIfmdC0PEpeexpzwGGNzVo93hGt6UQjIqg6S-pV3Cfb873lDwm5TUllqElHtXkKzDPxTkkAmZ8QSKEUCR18vQbew3lTqv3DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه حمله آمریکا به سپاه راسک سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68225" target="_blank">📅 00:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68224">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول انگلیس به آرژانتین توسط گوردون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68224" target="_blank">📅 23:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68223">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
انگلیس اولیو زد به آرژانتین
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68223" target="_blank">📅 23:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68222">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=FkSdoEl1ARgYJLPoxAIFuhZu5SNtgMmJwulrGaH06EOnb34h1ppukhePsoZom2nBdPxhQ-sY9T2pFNfIOf-hFxi30fIDpfL0nkdZqEhP59rBzvkHSRF-fZFeFIijKlN179moLtNpTHUAoDXkFoS467DfmCKj29urAMJYSUFovaXq_hI9-J3F4XJkuqjmIlwqBaDMsPOmtKud3ZskKlwKmJ_Wd_jUhpunKWOePU3gMy95LBMesWkOAirUkyr0_vP58FTpAWTJsB3-jLk7yGmllobiFvYuZc6texEVkJxrFvfw-_1hg2T2Tbdcnk7Z0h8kV7ukHym3UWyg7dfjwSflzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=FkSdoEl1ARgYJLPoxAIFuhZu5SNtgMmJwulrGaH06EOnb34h1ppukhePsoZom2nBdPxhQ-sY9T2pFNfIOf-hFxi30fIDpfL0nkdZqEhP59rBzvkHSRF-fZFeFIijKlN179moLtNpTHUAoDXkFoS467DfmCKj29urAMJYSUFovaXq_hI9-J3F4XJkuqjmIlwqBaDMsPOmtKud3ZskKlwKmJ_Wd_jUhpunKWOePU3gMy95LBMesWkOAirUkyr0_vP58FTpAWTJsB3-jLk7yGmllobiFvYuZc6texEVkJxrFvfw-_1hg2T2Tbdcnk7Z0h8kV7ukHym3UWyg7dfjwSflzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما به این نتیجه رسیدید که نمی‌توانید با سپاه پاسداران مذاکره کنید، آیا این به این معنی است که ممکن است آنها را مانند داعش از بین ببرید؟
🇺🇸
ترامپ:
بله. همینطور است. درست زمانی که داشتم به اینجا می‌آمدم، تماسی دریافت کردیم و آنها (ایرانی‌ها) می‌خواهند ملاقات کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68222" target="_blank">📅 23:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68221">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48590994cc.mp4?token=G4xBeeuB1Vo7YKzSkcyVHp0Kdb7NTRCJKKIPqVKZiAtM4GyV6KZZz39IsZwS2NQCbv8icawaT4MrvxcCWyeRAX42VmC6ZG5v0XwBrEOkg1zkpcu4zeN5l7aKMSNRWg6xblgharRHkXhr4XeVIbWthLH0CI6IKHSgl1uDkKcByx9gKiP5_oi9Ij5hyrq2hp6_G8PuRN7nOlV3snsasfINNj_OlYVM-259N31xKBSHx945McK26ES8VDrAWcVGgi2BHCUp3fRxlKMJTrbCssUl__kbv0ZadmGY-dPhVHPVBdtab1Bv2HFf2KJN_zQpsP1CCy1LMfPvOmQ1XQ-n54glhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48590994cc.mp4?token=G4xBeeuB1Vo7YKzSkcyVHp0Kdb7NTRCJKKIPqVKZiAtM4GyV6KZZz39IsZwS2NQCbv8icawaT4MrvxcCWyeRAX42VmC6ZG5v0XwBrEOkg1zkpcu4zeN5l7aKMSNRWg6xblgharRHkXhr4XeVIbWthLH0CI6IKHSgl1uDkKcByx9gKiP5_oi9Ij5hyrq2hp6_G8PuRN7nOlV3snsasfINNj_OlYVM-259N31xKBSHx945McK26ES8VDrAWcVGgi2BHCUp3fRxlKMJTrbCssUl__kbv0ZadmGY-dPhVHPVBdtab1Bv2HFf2KJN_zQpsP1CCy1LMfPvOmQ1XQ-n54glhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68221" target="_blank">📅 23:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68220">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">برق بعضی از مناطق اهواز قطع شده، خونه ها دارن می‌لرزن
😑
#hjAly‌</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68220" target="_blank">📅 23:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68219">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ
مادرقحبه‌ی هزارپدر
: ایرانیا خیلی دنبال توافقن می‌خوان جلسه بزارن
#hjAly‌</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68219" target="_blank">📅 23:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68218">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
گزارش ممبرا از اهواز:
اهواز قطع برق منطقه احداثی
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68218" target="_blank">📅 23:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68217">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ممبرا از اهواز گزارش لحظه‌ای می‌دن، حداقل تا الان ۱۲ بار صدای انفجار شدید شنیده شده #hjAly‌</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68217" target="_blank">📅 23:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68216">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ead41427.mp4?token=cFqdEr1yFfqzrzzTwblV6kdErSE3QblhsBIQnObgC6mj73i824TxnUP2tfFymudgb0NU_g3LIFKdZIJAshukFjtmnKP1FZG4OJ0GE-pMB3NTd00KGeSoWDih4NxSr1YjNLbHGAA7UbBSXgZXndXRyjClyDiqZK2AC35R0YTNUCBdPN6ns7RJxuSSUeSmAkwFpKgzmodp5qj7d6sW5WkUETpjAnFhFmWd4NddI62fTe5Ay1OJOessmwV0YerQoQz-4dvmFG5j3pox7eLOrm-T8wBsZfhFZC2fvoJLa2PX8C62YPQyHhgphVX5Da4lfcHaQQo7QcY_bSMbyHOHgbNMyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ead41427.mp4?token=cFqdEr1yFfqzrzzTwblV6kdErSE3QblhsBIQnObgC6mj73i824TxnUP2tfFymudgb0NU_g3LIFKdZIJAshukFjtmnKP1FZG4OJ0GE-pMB3NTd00KGeSoWDih4NxSr1YjNLbHGAA7UbBSXgZXndXRyjClyDiqZK2AC35R0YTNUCBdPN6ns7RJxuSSUeSmAkwFpKgzmodp5qj7d6sW5WkUETpjAnFhFmWd4NddI62fTe5Ay1OJOessmwV0YerQoQz-4dvmFG5j3pox7eLOrm-T8wBsZfhFZC2fvoJLa2PX8C62YPQyHhgphVX5Da4lfcHaQQo7QcY_bSMbyHOHgbNMyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اهواز رو وحشتناک دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68216" target="_blank">📅 23:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68215">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ممبرا از اهواز گزارش لحظه‌ای می‌دن، حداقل تا الان ۱۲ بار صدای انفجار شدید شنیده شده
#hjAly‌</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68215" target="_blank">📅 23:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68214">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
اهواز رو دارن میزنن همچنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68214" target="_blank">📅 22:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68213">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
گزارش ممبرا:
مجدد انفجار در اهواز خیلییی شدید بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68213" target="_blank">📅 22:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68212">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuNlz9JoFGV16ojlrUBLMih6UUYa-igFsf2CLOyEB_0vmAxxyxrDzfCGpaUIyEhRc98Z_V2TXUWlGqHvyAteLTbrxG7Ue5RwCoXF8vwq_K9O-uooRcjoyfZw7Str2jr7RMUz_W8VTSRGJ1bGcBvbIC1_5R0Yb01y9IbYp5vTkqN5c1rWiWI6qZqrAgaNy6CSuDN7JA8TdzLnJ0urR78s3wVwsagLZlsjjgod3eSYeXb2jG1iWsRqaIlta-ABGjsz9oEQPzlUpbKpjk8FaHACKCeNusiChjp2slPdNSgdW1gVPcHaWtAfREmCBf7SNPoFwA8jVPyPkWbY3ODFo23LEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ساعت ۳ بعدازظهر به وقت شرقی، نیروهای ایالات متحده امروز موج دوم حملات را علیه ایران آغاز کردند.
این حملات به توانایی‌های نظامی ایران که برای تهدید کشتی‌هایی که آزادانه از تنگه هرمز عبور می‌کنند، استفاده می‌شوند، هدف قرار گرفته‌اند؛ تنگه‌ای بین‌المللی که برای تجارت جهانی حیاتی است.
ارتش ایالات متحده در پی دستور فرمانده کل قوا، ایران را پاسخگو می‌داند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68212" target="_blank">📅 22:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68211">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68211" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68210">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
گویا انفجار ها خیلییی شدید بوده
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68210" target="_blank">📅 22:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68209">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68209" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68208">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c19ec2f58.mp4?token=p6VXJ4-zzrVY-zm0ICLtxTQYSSorhkUWQDi7uGCIvYF_mVi1hJ7ScTzf8yZzu7BB1rH_SO5wRUSzKWWGchHP01YSUMQuC1LD6BAY1JdP8WEzJ4ChFD9NwAFC6vS528b7gu-hdu7jGTHIcFUkr5cZT50_NBIItCXO9x4ZRakji26FYRY0QdOeK9APj72nEunDFvI9p18ZGwdw4R56OmErwYO9BX8mU1Kx9NoiMAxDY7yQUu7LNDvwuXRt783e5JNtCHjbbP-BbGywaXlT4ADBWtHd5oQaVJq_7gUhQP_a1qvsEC19iFs4Snl4igHPUX7rwr7cbSWpfVA68O_yXf1Zbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c19ec2f58.mp4?token=p6VXJ4-zzrVY-zm0ICLtxTQYSSorhkUWQDi7uGCIvYF_mVi1hJ7ScTzf8yZzu7BB1rH_SO5wRUSzKWWGchHP01YSUMQuC1LD6BAY1JdP8WEzJ4ChFD9NwAFC6vS528b7gu-hdu7jGTHIcFUkr5cZT50_NBIItCXO9x4ZRakji26FYRY0QdOeK9APj72nEunDFvI9p18ZGwdw4R56OmErwYO9BX8mU1Kx9NoiMAxDY7yQUu7LNDvwuXRt783e5JNtCHjbbP-BbGywaXlT4ADBWtHd5oQaVJq_7gUhQP_a1qvsEC19iFs4Snl4igHPUX7rwr7cbSWpfVA68O_yXf1Zbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شلیک موشک از کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68208" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68207">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
سه انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68207" target="_blank">📅 22:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68206">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66f6a0a0f4.mp4?token=RK9f5qkDs5zvETEiMeuE7TZW6UEXdx4P6gWuatXOucuHF1qaeRX8z2sP8y91rFvPKNbrY1Yt7tn2j9BfKvxjd8YssgYSqEVtBKdPRWjz-W8M9aw_VzCrCFJmCjHUaUKS7f3ouzddT4UAnJ5Ird5wqNyjkYM4Sv_S11W9cgYOXyAsJTtJOPPhpDgiHny-lvcJ957JCrHk-ZfT2ZrD2_qSKHQnD1kAg-KiSnmR2NFnGOA41ZDV5GoxlxaliXYKFCDkDK0pAnG_GmMWHA6R-TbK4YTq7qIt6oQge0yBiMgXYv9TcsRZlkPXO3dYvfWOfSIfT6nG5r9gJoMg_skY0hmjtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66f6a0a0f4.mp4?token=RK9f5qkDs5zvETEiMeuE7TZW6UEXdx4P6gWuatXOucuHF1qaeRX8z2sP8y91rFvPKNbrY1Yt7tn2j9BfKvxjd8YssgYSqEVtBKdPRWjz-W8M9aw_VzCrCFJmCjHUaUKS7f3ouzddT4UAnJ5Ird5wqNyjkYM4Sv_S11W9cgYOXyAsJTtJOPPhpDgiHny-lvcJ957JCrHk-ZfT2ZrD2_qSKHQnD1kAg-KiSnmR2NFnGOA41ZDV5GoxlxaliXYKFCDkDK0pAnG_GmMWHA6R-TbK4YTq7qIt6oQge0yBiMgXYv9TcsRZlkPXO3dYvfWOfSIfT6nG5r9gJoMg_skY0hmjtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از کسی که در برنامه زنده می‌خواست شب‌پره بگیره چه انتظاری داشتید آخه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68206" target="_blank">📅 22:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68205">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
یه هموطن داشت از محل برخورد موشک ها به چابهار فیلمبرداری میکرد که یهو برج مراقبت دریایی رو زدن
‌
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68205" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68204">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nksqSjg8n6CLwx8xkpnWZjJCmU5GubEPqEj1Ko3iL3Beu8RYmte7Ll_5GrNsqT7peMC9hPqqUV6QGw1Z5Ld1sn0MARHfqoxIlKXWvMYf3NwwqoKbn6rHHTlTYqXgnaHM9DXDbe6cYXG_vpSOnArZZvTacXaW7wIcCkkBz4O_3e95KiKaT1vqOSZBiMklSDXfKZGoidPmyZ-jLuED6UNK55tD-5Sbe93eYGur7JdD_3oYlcxQMOlygwA_Ixj6g0xah3MGjt7QdsuO-rEG0A7X970ydgQMEdFwmGr5D9OEUne0vHWqvoPE2nzbDS_k1FU-_3Ot86Zak4nnpeZxBEhhOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
امور کنسولی وزارت خارجه آمریکا تو ایکس، یه بار دیگه به شهروندانش یادآوری کرد که هشدار سطح 4 برای چند کشور از جمله ایران
🇮🇷
، عراق
🇮🇶
، لبنان
🇱🇧
و یمن
🇾🇪
صادر شده.
+هشدار سطح 4 به این معنیه که آمریکا از شهروندانش میخواد که به دلیل خطرناک بودن اوضاع، به این کشورها اصلا سفر نکنن و یا اگر اونجا هستن فورا ترک کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68204" target="_blank">📅 21:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68203">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🇺🇸
فاکس نیوز به نقل از ترامپ:
حملات علیه ایران هفته آینده گسترش خواهد یافت، و خاورمیانه خود را برای اتفاقاتی که بعداً رخ خواهد داد، آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68203" target="_blank">📅 21:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68201">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/adRAmEa2AuynZr910rGddIiDKI4dvdJeziDORL5pLdFCchXrUbCWPKPjGU6_wwDsFt8XBpqi_iPSyem6Ge9QKUNK-7n6SJYL79vp9YaiguUWzzEHP5vk_Dlxkhnt5EQ-PdoD63SmReQHKgqyvAekqt_P0U8H1IYExzjWTozfpptiV5s74P9QfT1xJZ2N6JDuAuZ606lkPqqs3c7wuA6GyYYk_wFW97lnrDLj16zu2Hf0i91FUDTokswZ7twok9B7U6lK3D1pBiTPrTvjO24BsiR6FOJ0-2axHiUxd0GiQV-0zOL3xZfzJTB_1K_BnXwRh7w_2AW2FS0VFubZgK_NDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GPZSYaTN-Rh-BT-W3syor8mQL6dF9yZxmQu4uxzBt-6cqBuP0dLqz6gD_7FXcrlK9tehmqrEDviTDWuW890NKJpuY1Srn1UmFPuuCyjt8bxvpMSzJSi9bz6N0rjavtvtCEcvuidfJhLb9HSCGInRIApSYTHgDibVZ8oUMwCbuSxxQjDaRdgm0v9ZwCsCljqiYl0oyXPKg5KXeULQGWB3JZgqrweXaScRibVPtB_BmTS4j5Ix7VfDO7a_t5oWIS6qsaNkMoY3Mjc0R2qvWEdcPRlilwfN_VaDUOOpHEmspwSlvtbPOq2CzDyhn4SWsKpsdHi_EA47A8om4xX5rFwjfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ترکیب انگلیس و آرژانتین برای بازی امشب
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68201" target="_blank">📅 21:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68200">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
قالیباف:
همزمان با درگیری‌ها، باید از ابزارهای دیپلماسی و مذاکره نیز استفاده کنیم، به گونه‌ای که منافع ملی را تأمین و تقویت کند.
همانطور که بارها تاکید کرده‌ام، مذاکره در این مرحله به معنای تسلیم یا ارائه امتیازات نیست، بلکه در کنار جنگ، بخشی از استراتژی مقاومت و حفظ منافع ملی است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68200" target="_blank">📅 21:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68199">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
قالیباف:
برای ما مسجل است که انتقام خون آقای شهیدمان را به ثمر خواهیم نشاند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68199" target="_blank">📅 21:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68198">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
محمدباقر قالیباف:
تفاهم‌نامه وقتی معنا دارد که مفادش معتبر و در حال اجرا باشد. اگر ایران از آن سودی نبرد، دلیلی برای پایبندی وجود ندارد. ما بر اساس اصل «چشم در برابر چشم» عمل می‌کنیم و در برابر بدعهدی، متقابلاً واکنش نشان می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68198" target="_blank">📅 21:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68197">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
قراره تا ساعات آینده ممدباقر بیانیه‌ای درباره جنگ و تحولات روز کشور منتشر کنه.  @News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68197" target="_blank">📅 21:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68196">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5u5k-f70Kayg3FtWMkvNhBmXavPxX42hcUCPCoQJCcRINI6VtZhK2FqHbST3E4YElRHPgKBoQRkrEht6Xr3R2BsyLCc-GjnQrGESKNnuxHFH_q9WmsuB8tjcYXNAJv79f_hPh0_1hrp7zBlBeBPfTaslA_A7hFIDDBrQNB8F6kez7621ptxK2DjlnYRGPU2YbMtNZcmF9aFIeQZMv-Y00tql9lht7i-2YlI1cmWQIJ4KrSSzbSkcwJjenpJV7GX29kVWy3gPbDfNCiMQr0K-xsqRKmQUrgVyo5ZmSc22SJjWIN4xsXe2bfcKtMWUjnNDmRgOZjHznuh9XLsm5PFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر شهدای حمله آمریکا به پادگان ارتش در ‎بمپور.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68196" target="_blank">📅 20:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68195">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKSPKEC6mZjbHdmghtj2F9263_Ng0Kc4REMPHto7kM0dherxA3ts_FjjWN0oewdfMQ4DftVpSUcLB29i24OjjBjn0vRwX7VjM1GW5UDQEhfUgHESJCrFMMqq_wIMjFZoKR3P1CNDM4iojQPac0J9TVuI3woUDojSfVXObeeEdT4L1C8tTLmxmH2pULiVlQRES3ysxDZuREpZX4OQg3jwPwl_W1McEMANEWO6gOTeiFU_Lwwo70aPS2ydPQTuZSMOSlyrebZPJmSTSdtsB1NI_Kg9TEUscO0ZlS9UxEDKpzjDuRnyF2nJsiPFfcFC6njqDQa78-o0TMcJCPwnG632NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب عادل دو تا اسطوره‌ی تکرار نشدنی رو آورده، فوتبال ۳۶۰ رو از دست ندین،
کص‌خار میثاقی
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68195" target="_blank">📅 20:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68193">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMreza</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfnV5M1R7OiDNzm2TIS_SjJxqqIP8Vsx_-xrMk-tLXwau2GUWgEEPxh0xhlOdXhfHVGFWe4jOqHYwnh4rOpRtsY_9uarlKkV8PxLTsUzm_oZkrwresOOb4mDtRKP-VCoEM4ohW9zXrtcjC-XYb3ZgmHPGuGj8MM21spUJKIHapywcLkq1KCxcVi4Uf-iWIjE4LLPzHlKu4XYoEqnmqRbyUUjP31vtXBmtmKwPP-h1Z4vivt95KVQ-osDyx8Ih8t57vClyblmCS8Y96MMeXCIj_5sNpdvBUBHgeamRUapbOBzL_BcgnrisirurkB6rz9UPumfz5raVE0v1GIo-ABeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-jG4Prc97qHBdUWlMGFp9vtZ5JDkuPtCPhy4vHQ6sQtDKBFNQ4wVxL--pmKTcrL3gU7M9lYjKNuJDbs0ZprhSs-fAh9qwVpYfot0hFCKTruWN4Ev79pMeWwuTYMvficgUzKPj4QUnJ2GVhJRDwUK0Bm8o2nwBOaVZuLOVTj-DHGe-m50P_dILz3T7FkBq7wMh3WFlXDcRLNeDogWNfu7GzfjIEcjkZiBd6e9gNlEhifhRqV753_NgbODj-oRH4R1pELOmAqU3RzwomGscWHz257BuCfHi1aR1ZPN7wp2EjuI-yzAIPURG1mHvaWhnfCBdz_DJKBsPQ7rqR18I3mcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Siuuuuuuu
❌
Zhiuuuuuu
✅</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68193" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68192">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e6c5a6cd.mp4?token=jClrN_QRFuyXw2rZzHSsyd571yV5VV5Oib_oJcwlOhxBOrMiux18cWKwnGDc_fdN07h353-6XQ5Ah979gX5Z0xrmzdHR3VboBkbpkbC5eJ2laYzxzxnmAPEAKJwDIYS9mPMa5LrxN0eYQvNLzIv4c4veuEb7uRTBollWuPFAoV9y8IgAav1SEjRQeKeb2DbGaYuhffJcQrgWU1a8d2fHGaliWkY5EgGP-9MMYz4ymTd7d9rAuWT8WJSwA37MclhQfeVQPNfBzr3mBdXdjnl4K-TmDkSC-7-gqXMT_kjtyDhPvCml78vfF5WKlHAESPhaYaVd0B_Gs7ffWx39Qy7VuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e6c5a6cd.mp4?token=jClrN_QRFuyXw2rZzHSsyd571yV5VV5Oib_oJcwlOhxBOrMiux18cWKwnGDc_fdN07h353-6XQ5Ah979gX5Z0xrmzdHR3VboBkbpkbC5eJ2laYzxzxnmAPEAKJwDIYS9mPMa5LrxN0eYQvNLzIv4c4veuEb7uRTBollWuPFAoV9y8IgAav1SEjRQeKeb2DbGaYuhffJcQrgWU1a8d2fHGaliWkY5EgGP-9MMYz4ymTd7d9rAuWT8WJSwA37MclhQfeVQPNfBzr3mBdXdjnl4K-TmDkSC-7-gqXMT_kjtyDhPvCml78vfF5WKlHAESPhaYaVd0B_Gs7ffWx39Qy7VuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا صبح می‌شه به کریستیانو خامنه‌ای خندید ولی کانال زشت می‌شه پس بسه، فک می‌کنه کریس آمریکاییه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68192" target="_blank">📅 20:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68191">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdFiyLCqPanTqBYdUZRQPedGpwsNkyI0Y-RWpJmToPHej842HKNPnkisQ-P1_fAz6wB1bhOZnPhrkfKurjomlxgvF5ijFXIHYEbnQD99SSLtS-7sL58UPzMAqGe0q-vMvga65ykC40zQjcMv0UUwLrlK_Lz8dQ4vo_w6HnOt61OpV2Fu5ZCxO8ml0aMpO5iUOGbUWT423NkK6s9SjIgGzbS9i2pLaYI-peihGXE1y-utYuMycSmyOz-K0K5h4X6n8evkzcvgmMqAEi0Awqejmk89gendloE1HQdc2LLrlhHEkxIluLGIa5wetG3KefO4UbDP-0CDG8xLA-1fj1P8rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو خامنه‌ای کرایه اسنپ نداشت بره سازمان؟
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68191" target="_blank">📅 20:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68190">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرونالدو</strong></div>
<div class="tg-text">اخه من چکارم؟</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68190" target="_blank">📅 20:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68189">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hj8F3cHXxWjoXcEGD1Mo6o6mUOtjQGVDRs9OO5cHhBq0ntbwH94feRL6lmOTQGUcA5vOFfIY0fGkciIrK8PUdDVU2Jm73_zNb18n80qq8XnuzoFvIGaFZCQTrEIqshttzR7CfkH-h6sLjtOXVjhkmYjptKSBT4VqtduMU_kmxZ-e1xTx406pSHy8qw4VIzywtnyGsFaXwKC9XwkZzrIC60bEy9F-JZ6CccpOI1jBr_1bpnVhU1E2-l8G4jqrejCOrKudEmuy681Nt0t8uJGlHLHjVq0nNTwjf9BRYt4iOFuDb8mYwkD7f9zTBY3CNgGzuKYOq2vRMXZ_TEaJW4mqSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل بچه‌ شیعه‌ی آخوندپرست
🤯
🤯
🤯
🤯
:  #hjAly‌</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68189" target="_blank">📅 19:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68188">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b2e5150b.mp4?token=nUYEKqBwl-2Es6yWUE8qPDdv0pF53gUzBmns0Tv59dtpmznai9QmnB5YQzJ84_UbUCEaliHlwvWit92cy3fQzA5HHOS5qldLjIaz6oU_NwpcNWVwzO1KdK0a_H3ZWn9PFD9bF21fKV3DiTF2oPDTVUrUh4VG6FVa-4q6Yg0K7ycn5x3BIAIfxyNksB2SgRrn1AQN_AiXRrl3XeH-tEfSX_hVglNr3lEAWzkG-TH1mg6iOpqKY4pfK6b_xsDAm3_SxT1sYIiZSJHW9GmorltHKYbTLeIiNA-vS-esOBPhj8kst6R4W7pTWUHGtNWHn2z9Aof-eTXeNZ4RIqWngWBozQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b2e5150b.mp4?token=nUYEKqBwl-2Es6yWUE8qPDdv0pF53gUzBmns0Tv59dtpmznai9QmnB5YQzJ84_UbUCEaliHlwvWit92cy3fQzA5HHOS5qldLjIaz6oU_NwpcNWVwzO1KdK0a_H3ZWn9PFD9bF21fKV3DiTF2oPDTVUrUh4VG6FVa-4q6Yg0K7ycn5x3BIAIfxyNksB2SgRrn1AQN_AiXRrl3XeH-tEfSX_hVglNr3lEAWzkG-TH1mg6iOpqKY4pfK6b_xsDAm3_SxT1sYIiZSJHW9GmorltHKYbTLeIiNA-vS-esOBPhj8kst6R4W7pTWUHGtNWHn2z9Aof-eTXeNZ4RIqWngWBozQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به یاد سربازان تیپ ۳۸۸ بمپور
💔
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68188" target="_blank">📅 19:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68187">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پاساز علاءالدین خبری نیست، ویدیو های منتشر شده مربوط به‌ گذشته‌ست
#hjAly‌</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68187" target="_blank">📅 19:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68186">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKAb3ZsEvyPF7G13_hfKTEEAHCeORsCBjcI4G2eNcwSlOmBL9pf0wiRi7X8VIE74rsdXuPc8f5Apmkp-JDF8N6ySAUXkiQVtTw7oO73WzeI-B8mJvo2CylV8E0FWQCZo1GHFtEGpLMQwBs5UQRLy9u2h-gCMVk-kDG5t4fnOyYeoj50ky_RVlewl9aLOcgTSNrRl6oOropOHDO0TbZWxCdDnFW0IV9MglGhM0TGEHgvChYfMl0rKybOZZAOmXWLHNQSFZCiyghblslt51nMXqUx1bgq2urShVgMR-CvYG9CI8OG5bzLmDVAlVxenNccgj3knaDwt6qO1ArbId3OCdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:
❌
ادعا: رسانه‌های دولتی ایران مدعی هستند که نیروهای آمریکایی در تاریخ ۱۴ ژوئیه به یک انبار غیرنظامی گندم در هویزه حمله کرده‌اند. این ادعا نادرست است.
✔️
واقعیت: در تاریخ ۱۴ ژوئیه، نیروهای آمریکایی اهداف نظامی ایران را در بندرعباس، خورموج، اهواز، قشم، تنب، بوشهر و کوه استک هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را تضعیف کنند. در همین حال، ایران غیرنظامیان بی‌گناهی را که از این تنگه عبور می‌کنند و همچنین در کشورهای همسایه حوزه خلیج [فارس] حضور دارند، هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68186" target="_blank">📅 19:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68185">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDuAhXhGhQrUT17senNuwIk882THW60Gr31VzI7jkR7zaJGLFtjV3nrEPhk5ymkaL3xbCmTcSh7mgBXoCGL41QvXoI_op4R30hncpn0udMDFfO4KQpUVAvP6S4JE6N8sa5DYUbmWCO0Wo8_8q1ZhwRQnBmw50XxyQKdZ1LTJm7GrTc0DtzOTe-3uVVIweYUzleMvS5JQObm_R1OU0T5ItsGaNwEeYWoNki__RmKBpVKnFFq5GFwZ3rzuzbOh7y9vgH8VqOg0yD41oYx3nLhkw3zWbdd5Vzqd4B_vcwZr6tbXpwIzKEKCNw0qfFNv2RWINRgC6czLWuP_BpZjDFzSXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قراره تا ساعات آینده ممدباقر بیانیه‌ای درباره جنگ و تحولات روز کشور منتشر کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68185" target="_blank">📅 18:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68184">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCCnCM3SYSVux4lXF7qC4MROGQ2JBgKGDEgNbVF5xmShfCXQbQei6v7vch-EFq2qdapjO8Ao_JEQcEOMKoYMIu8mQ8pj5qXiVuTto0Bzhae9P9gxEV1zMsI2lgqSj-5Vov0Z58ObdP3DpqYYKPkyAcT4UhJJQ1MUR8qAeRzLEwweqAMRzb2wUmvFv4mCxPzw664dbRSxdLGV-r6ar0Gv_6VRWRTzUTIV4f2iYHA1JewOAUVuaT38IiDf9l4oqLhRjeeC5uafeSTaIaHHbWndBg43_4pCOeeMWSr0rHP7xqt1W83b_bjUfRf4Opdbp-Hl1h-FbGXzW3u0E2_jzfpURg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
از زمان ازسرگیری محاصره دریایی بنادر ایران در ۱۷ ساعت گذشته، نیروهای آمریکایی مسیر دو کشتی تجاری را که قصد عبور از این محاصره را داشتند، تغییر داده‌اند. ارتش ایالات متحده همچنان هوشیار و آماده است تا از رعایت کامل مقررات اطمینان حاصل کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68184" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68183">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/68183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68183" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68182">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7n682HwU2mSZJ7gbdHKBjqUrkM6jYM_h47EEN9CfOar6Qxf8vrDdOeOBTh54m8SyYi16X_PkVTYI4EPjoNm9Q0Q_9Carj3rE8Q4ytf4kMVP8RYTOqe3H7eVMRmCKNr6SaS5E0kcD85o2YXEaKcGP6TNbXhI0RUu0jsuianGI5yoyNZc6-WAz1NBPSTLrVaNp-4BZK0SzgEs1-ohIcBkxAM5ReFIBUA2fk7VGr0_md_ylgp2JWVl4st-t1LCeLoKcLG2c5rgpFcn1cJkxsBfyxqPbEG4iz2QYxulfqcfTZrCM7f3LZEGFn0RzcSMwXCCLt8H2VH20zDzQrNLB3AZNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
Stand for Victory |
مجموع کل جایزه  250,000€
🎁
جوایز برتر:
🥈
جای دوم — 33,000€
🥉
جای سوم — 20,000€
4️⃣
جای چهارم — 10,500€
5️⃣
جای پنجم — 8,000€
🏅
جایگاه 6 تا 10 — 4,000€ هر نفر
🎖
تا جایگاه 450 جایزه دریافت می‌کنند
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68182" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68181">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
انفجار در جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68181" target="_blank">📅 18:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68180">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415d2aa12e.mp4?token=Gn3biHC6Fgpucjzi2It9nuyAYBuaYK6-KxV_Lp9D47rKxj4HpRlIVQH2jilitHdsbsZ3gaxBgrPktAw19mvJkrV5qsMe4ihomqou8OTUZGkx3hTVwseedEU0OkD967ALv7GrY5GfA5zArz_jJX6hSY0vnNJ1UC8Kvup9f6SuRughDSrEXQGZJ3yYnfT7fOvhigihuVBdS9GAUVN4_gF9G8CKuAPwfMaEFaOoXhvssycUQZ8eJL-ndVY2YtGnZSrG527dSn31yGPnIJuo8adF8culdPFvRghBW27h27E8roqzryHS94s-6l05fo_6BNo1cCEYIav-Shzm3NgVYMx--A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415d2aa12e.mp4?token=Gn3biHC6Fgpucjzi2It9nuyAYBuaYK6-KxV_Lp9D47rKxj4HpRlIVQH2jilitHdsbsZ3gaxBgrPktAw19mvJkrV5qsMe4ihomqou8OTUZGkx3hTVwseedEU0OkD967ALv7GrY5GfA5zArz_jJX6hSY0vnNJ1UC8Kvup9f6SuRughDSrEXQGZJ3yYnfT7fOvhigihuVBdS9GAUVN4_gF9G8CKuAPwfMaEFaOoXhvssycUQZ8eJL-ndVY2YtGnZSrG527dSn31yGPnIJuo8adF8culdPFvRghBW27h27E8roqzryHS94s-6l05fo_6BNo1cCEYIav-Shzm3NgVYMx--A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
منوچهر متکی وزیر خارجه اسبق جمهوری اسلامی کاملا جدی اومده گفته:
باید به پایگاه های آمریکا در منطقه حمله زمینی کنیم و صدتا اسیر بگیریم ازشون و بیاریم ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68180" target="_blank">📅 18:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68179">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1331c1b8f5.mp4?token=TPmnzH0NiN4MMU5cURTFM2Q_DyHZwoSkDtGHhAAsG1HebwZdYHR3bcGOasdGU9ZrdzkRsN8jkcVYi3ykY54-qb69-gcs5pMnI9UHkogYoNhaD4_AeHjddT3FM_ggJJnz3eiZ2GBgRm72yZtQld7LUW1YCTHPH1lUmOdUMnuQJ8c1TS-KEClqNXXfputpXj7bK2lVUngrrFz9wHkIJFJEK39dO4MlhENVP8d4fBrLzBWYYRVQ7vzXTjdN6uvN_3YA-JM66D_y7rHSK-jLlN0Zns78jHAzs5URsikVVm5_dAf_LRKqWXiLyf8Xz7Xhl5j8z3owqIWTRWjTQEiSv3o2Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1331c1b8f5.mp4?token=TPmnzH0NiN4MMU5cURTFM2Q_DyHZwoSkDtGHhAAsG1HebwZdYHR3bcGOasdGU9ZrdzkRsN8jkcVYi3ykY54-qb69-gcs5pMnI9UHkogYoNhaD4_AeHjddT3FM_ggJJnz3eiZ2GBgRm72yZtQld7LUW1YCTHPH1lUmOdUMnuQJ8c1TS-KEClqNXXfputpXj7bK2lVUngrrFz9wHkIJFJEK39dO4MlhENVP8d4fBrLzBWYYRVQ7vzXTjdN6uvN_3YA-JM66D_y7rHSK-jLlN0Zns78jHAzs5URsikVVm5_dAf_LRKqWXiLyf8Xz7Xhl5j8z3owqIWTRWjTQEiSv3o2Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمسخر لهستان و شوروی توسط چپ‌کش اعظم رونالد ریگان فقید:
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68179" target="_blank">📅 17:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68178">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f97b887b.mp4?token=uu59ssBrPf2z9NTodXnKDJ1T5oT0JuhYAmMrhJexN9_iQjOqn7zPr5B3LduuxUecLerZs7NgXRe0ZY8wtzgvkr4GePCOTz5LXTquaz6fpk4k7e-VOf-FyplHPQw2tNdI1FXhxJNeUqbvy4exYRjAPc_ZucWJY71jNPO5xY3ScLqoWOxI5-l4ItsMe84UoyJY492mSu7Nj0TKwdcFC3UCddeqhKqeEaT65R7P2KVId9JyX_2SpP9nmPIf5yn3J8DysLkP9WFYJE5mhFrK4BEAZhlPxk67kyMnZNSMco4J2jA6JMDgwCymIzwW5UJ7gaqIQwRQZK9Kma95kDMZIgRTjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f97b887b.mp4?token=uu59ssBrPf2z9NTodXnKDJ1T5oT0JuhYAmMrhJexN9_iQjOqn7zPr5B3LduuxUecLerZs7NgXRe0ZY8wtzgvkr4GePCOTz5LXTquaz6fpk4k7e-VOf-FyplHPQw2tNdI1FXhxJNeUqbvy4exYRjAPc_ZucWJY71jNPO5xY3ScLqoWOxI5-l4ItsMe84UoyJY492mSu7Nj0TKwdcFC3UCddeqhKqeEaT65R7P2KVId9JyX_2SpP9nmPIf5yn3J8DysLkP9WFYJE5mhFrK4BEAZhlPxk67kyMnZNSMco4J2jA6JMDgwCymIzwW5UJ7gaqIQwRQZK9Kma95kDMZIgRTjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از وایرال‌ترین ویدیو ها در 24ساعت اخیر در توییتر فارسی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68178" target="_blank">📅 17:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68174">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVWiKbOxC1eLduZNtWHnu-PW6VP9wYx97y2TYqG5DVJaUkXZ3MWWqeS9mDYCbgwDGcBtNHAOVxfbOZWaI3CjI6hhXSKgSWtuzdgQ9gF6X5BONV0gAxC_mw60_8RfgTwzp9a9J4Uf9g8TWOGv8fJ-7uSODq_QsbYZHwgBTT7Ls8lkpPW4xiOwDz0TL4BrzvsvENHAjRD2OWmRZLB1rJn2JECyhyAq0EmNjLzCjTygiTrRH-IX87mLdDDXcqEGTTpqSzm_BnKjUhpLuNqL-U2gZFQ_-QJZUpG4rFbt6mh9ZJoQjqL7ojrOa2ruczfVLVKS8XcMHVCnqc3sBXDZXQGsvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=UKbapHgDgQe3U4X1nmGEdbJwT3dOKZ_TwIGh9tnXGkCyF3GaJodDzMNbs6Th4_05CJVyAtkGgCllkCj1REyhPLR8t1B-b2bVX07e-_Y3DO5ntHF5i1PLOuL_XCR36OXWDYJqENAWO7QcmfHBDrRBVnH-sfgOQtl8D2obA2dv6mfMwi4xJXqq1-iqoo-KLeU50crtcSB7jnt7vYaINdqOOm99d7qsb3P3v4gij4_LX1_aJvPWdog6RFTuhmS4MXLXXqUpYMpKkqHWbRnm4tHQmwIifRa40iahIbhf6p32AG6ctR_z9w1Bqf4nEnNDIovHl0o2ZxPbM9o8hy4ly_TvIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=UKbapHgDgQe3U4X1nmGEdbJwT3dOKZ_TwIGh9tnXGkCyF3GaJodDzMNbs6Th4_05CJVyAtkGgCllkCj1REyhPLR8t1B-b2bVX07e-_Y3DO5ntHF5i1PLOuL_XCR36OXWDYJqENAWO7QcmfHBDrRBVnH-sfgOQtl8D2obA2dv6mfMwi4xJXqq1-iqoo-KLeU50crtcSB7jnt7vYaINdqOOm99d7qsb3P3v4gij4_LX1_aJvPWdog6RFTuhmS4MXLXXqUpYMpKkqHWbRnm4tHQmwIifRa40iahIbhf6p32AG6ctR_z9w1Bqf4nEnNDIovHl0o2ZxPbM9o8hy4ly_TvIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیوی منتشر شده از انفجار در چابهار صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68174" target="_blank">📅 16:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68173">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=diqk0taOti9A_GxDFBaqCgGmtyWRnQsfE1jwXjDtPALZYfox6DsfwCGynhwJsoyTFKKH3IEKkVO0rYfYDusokDwF401eMASU239xosyo_RoM5AuZLNMM08gV5UMXN0KaH0fAeGtuHUWTgeoHMXYreyaV16fv2Gd5V7tNYs55DK7DjLiu7p5-3vfDgHo7XVr18_uS3MJJXqFDEzhDpGNZbySZbLeoFNx79DoLY9WUpesQNEXrQOhSuknIdz6zdM0exS21Kie6RngdzE_YATsHSGfqZAP-qiQZIeNwA7Sg0oLIAco2DC4ioP2PqgVP-W2r040dT1IE7I1YlyfkgFi9KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=diqk0taOti9A_GxDFBaqCgGmtyWRnQsfE1jwXjDtPALZYfox6DsfwCGynhwJsoyTFKKH3IEKkVO0rYfYDusokDwF401eMASU239xosyo_RoM5AuZLNMM08gV5UMXN0KaH0fAeGtuHUWTgeoHMXYreyaV16fv2Gd5V7tNYs55DK7DjLiu7p5-3vfDgHo7XVr18_uS3MJJXqFDEzhDpGNZbySZbLeoFNx79DoLY9WUpesQNEXrQOhSuknIdz6zdM0exS21Kie6RngdzE_YATsHSGfqZAP-qiQZIeNwA7Sg0oLIAco2DC4ioP2PqgVP-W2r040dT1IE7I1YlyfkgFi9KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۷:۳۰ صبح به وقت شرقی روز ۱۵ ژوئیه، دور دیگری از حملات علیه ایران را به انجام رساند.
سنتکام در جریان این موج عملیاتی ۹۰ دقیقه‌ای، با استفاده از مهمات دقیق‌زن، سامانه‌های پدافند ساحلی و همچنین محل‌های نگهداری و سکوهای پرتاب موشک‌های کروز در جزیره تنب بزرگ را هدف قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68173" target="_blank">📅 15:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68172">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=ADBg4KRO-tGLls8JfJUkbEn-IiAhAFkKamTCOrHuW0rSjisUUraMB7UM61cwUMK_vbbSb9XlbahR4TpV8IiWNQoOrITlmhjVGNW9451MUANlME_ZhPB0XOytLfInfRcqtvsPVpwQYwOCaLk4MmTckmlCUxqna6DfLd1Az49ctDrb3AHO7EtQ0Yy6yIdYjuzHgBpHC0mlFxgTNzicJRBqj_5lwknFzlKtqf6Xbw8GKDSeZSBUZEUUbl0nNSbCEPn9fjHDFa9xEnlSn-9X3UDS-zjs4pV5WNvpE48aAMNnCQHYXCBdETh3k0AsjsxgkimnsSm9ADLtuu4pEXu7f0Qv5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=ADBg4KRO-tGLls8JfJUkbEn-IiAhAFkKamTCOrHuW0rSjisUUraMB7UM61cwUMK_vbbSb9XlbahR4TpV8IiWNQoOrITlmhjVGNW9451MUANlME_ZhPB0XOytLfInfRcqtvsPVpwQYwOCaLk4MmTckmlCUxqna6DfLd1Az49ctDrb3AHO7EtQ0Yy6yIdYjuzHgBpHC0mlFxgTNzicJRBqj_5lwknFzlKtqf6Xbw8GKDSeZSBUZEUUbl0nNSbCEPn9fjHDFa9xEnlSn-9X3UDS-zjs4pV5WNvpE48aAMNnCQHYXCBdETh3k0AsjsxgkimnsSm9ADLtuu4pEXu7f0Qv5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از جنایت ۱۸ و ۱۹ دی ماه؛
تا مدرسه میناب و پادگان بمپور؛
نام‌ها عوض می‌شوند
اما قاتل یکی‌ست:
جمهوری اسلامی؛
حکومتی که برای ماندن؛
ایران را می‌سوزاند
و جوانانش را قربانی می‌کند.
#hjAly‌
@News_Hut
|
@HutNewsPlus</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68172" target="_blank">📅 15:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68171">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehiPXzzoWXO_o2sKi7fI2zRkyptzZ9PUryF7QofCHNM-dyymfemJe2tSsDuqsztHW3MZ6aAWSpYB1gsXA0YE8YGSBuY87fsilR7X_S46f3-Ww2UjCDFuDmAL6l448cDu7igpUDximazfRtUt7mCCbatbJSBYkZE2_rGKQE9iJTbr7xfM7YQ3vpXrKhvAFeRXT78KpkVkZw9DdP9X6oD-0_qRkaw2C__XqdRmfgfDE4q_e9bXqcW7ZJwPzDxxqBE2WJoZtF3MpvXtFe0L5C5pliqrO9ZginMCih8GTER0ealsoyhEuNp4luhJXakbcfPAEAqw9O8j8dIi_h2MN17NTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری حامد‌لک:
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68171" target="_blank">📅 15:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68170">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijQe6-1mmxDIF_2ICEil4IG7o10ddR4OcqgXECMfb-TZhXUCrBVEzUtsmO9hOB69ABZkOM5jC6k0DCMrOF64eBgy-1AQ_wUMqH6aKAVDog9FZcMYqiY4zEDx4OgTc5s2S9Mc5GPCnD76NTpIqgozOS5v9NR4vKJEK4AAXh55jxTMmBJcv2nP9qICTU-257gl8ZcWmmRxdjJTjakd1GZ_8m9fuYnLCg5DVYoyszcKlwm3FCPf3zAXxjAmu5hXTw0xJJzu-34klJtHoBIlR5Jpq0H1oSYummTmSLXHdBNhEb6OST3QKGgUrqhkp1ISqIvgfH1WTTLULPbqFgxJ6zRniA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
چهارشنبه ۲۴ تیر ۱۴۰۵ جام جهانی ۲۰۲۶ مرحله نیمه‌نهایی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
- انگلیس - آرژانتین
🇦🇷
ساعت ۲۲:۳۰
ورزشگاه؛ مرسدس بنز آتلانتا
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68170" target="_blank">📅 14:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68169">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
پنج انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68169" target="_blank">📅 14:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68168">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">علاوه بر اینکه سوالات یکیه و باید همزمان امتحات گرفته شه، تسنیم اومده گفته فقط نهایی دوازدهمیا تو روز ۲۵ و ۲۷ لغو شده، این درحالیه که دوازدهمیا اصلا ۲۷‌ام امتحان ندارند و یازدهمیا دارن!  باید منتظر واکنش رسمی اموزش و پرورش باشید @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68168" target="_blank">📅 14:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68167">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HniRrE-qBUKx1Q4fCWRf6f4fgLyL4HZds0CJvEMEmMaaHiRSIZ-WrGABk4YfEni83V5s6rcCB7LhLiqiwjcH4oPKA6X36c9VlSHhrBOx_aR2Se1qFdjVZUakyQWw1g1hkBGbVoPo0FHJMggkkNkmATFQcrdkrzEafqndpkcjVedBmvY7mODVmJOGe_wGML7vIckAdivL5IfYXR8ECxlFmP0d-xkJ8yzTzJZUxV1hAFDUifQcujh6ZLJgB2kp3FH_rXRhULnrHx6GLxwpRdGWnvAqZrpJfqxXl0sbqsIJ3R9EZiFt0b321DofnjknhmBCeXtUudWfllfJrmipp7oGFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطوری نهایی رو فقط برا چند منطقه لغو کردین، کاش این دو روز کل ایران رو لغو می‌کردین تا فاجعه‌ای دوباره مثل میناب رخ نده... #hjAly‌</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68167" target="_blank">📅 14:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68166">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=o1IAmuJ9YaUEM6J8yFtdgw1rNfprPAiiYYrx0b6PtpzR5EdmcStvfPiskzrzex9B7c_ifqgbAK9qd2DcQdwkCvhGr43JATynwThJKbwHGmANeI0Zm9qQn5KcN7G-XlaOgP3L1A8c02FtPiDTbVBZDFzFKVmqjevvIE3-mMub-iRALUyrSgNbqQfJPM6EIy97U8p032_ydwK8eihdXLEPi05s3aP-pKmN7nK0c7JjS4DmGD9Hq6wjuk8g2QR-L2xmNWRmVysBTQY9u1m8Znt6mY3w5P4L7_-isNd0i_kMQUOOMMPCJEPnVBODjgCjkblnHDegUjK461oY2EvLY_dGgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=o1IAmuJ9YaUEM6J8yFtdgw1rNfprPAiiYYrx0b6PtpzR5EdmcStvfPiskzrzex9B7c_ifqgbAK9qd2DcQdwkCvhGr43JATynwThJKbwHGmANeI0Zm9qQn5KcN7G-XlaOgP3L1A8c02FtPiDTbVBZDFzFKVmqjevvIE3-mMub-iRALUyrSgNbqQfJPM6EIy97U8p032_ydwK8eihdXLEPi05s3aP-pKmN7nK0c7JjS4DmGD9Hq6wjuk8g2QR-L2xmNWRmVysBTQY9u1m8Znt6mY3w5P4L7_-isNd0i_kMQUOOMMPCJEPnVBODjgCjkblnHDegUjK461oY2EvLY_dGgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خسارت وارد شده به یک دکل مخابراتی در بندرعباس پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68166" target="_blank">📅 14:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68165">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
#فوری؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.  وزارت آموزش و پرورش:  بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68165" target="_blank">📅 14:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68164">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
#فوری
؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.
وزارت آموزش و پرورش:
بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های تحصیلی پایه دوازدهم در روز پنجشنبه 25 تیر و شنبه 27 تیر لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68164" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68163">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zp3npOm8aD9LLpThpAAqPl02jkaHw_aZP4QR0kwle8_C1ysqg_tYk51QdQ6kuJsFUQ9Up_F--MfcIN3GG60UqZtPtlnon_p-oWwo9SUi4SDvZtLadigrL4oppNvEHQtevV5LR8BSQHt3FF2ppxFuowroDdW1VmIRvQkjz9uB_p2PHjWQsKd_exGPFYpnnqBEZOr5WjswtllvpN7cw6JAaZA1Dm96ExG5TlRdH4fbP3MHBcuTjXa6GDANRlGNEy_KaDVX252iYP_YoncHp493nfSCcgKFuR6Yov1vmSoXLbDqlE5x3s3-oUh0GsXSg6bQWItWhT8zA2uZZyUK89nDnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۶ صبح به وقت شرقی، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) موجی از حملات را علیه ایران آغاز کردند. هدف از این حملات، تضعیف هرچه بیشتر توانمندی‌های نظامی‌ای است که نیروهای ایرانی برای حمله به کشتی‌های تجاری در تنگه هرمز به کار گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68163" target="_blank">📅 14:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68160">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lT0e_mFOTgrsWHtxFXb6x42BHZJbojP-2SMwFPFtkJaKh5E1jQVaKZsfU7F-_Pncozn04RGPyEfYo3IhIF6R5AovMbjJ-yz2GIv0tFvBQc7qpCrftCnBbInwyJqGoDrzXyyNu4k4FCnwhHF9HVfOmFFDWzuGU1Ni1485AvkJnNkoo_ifkQ8uYtwgYtWL7UlD6TAERLLo-D6WOyb5e7FBx518_SDPDDYAOzn6lmdHB2mED1HNCBFxV4Ix-LOOezuXPBGrkBNcG7Yzr-jmp4b56BB3BJdiRkhs-VKXy_OidDaxE5zq3AUw3YSQitIYrUwMy7eoXE_LrFGno2OiE9kiSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gF_mo9HLC0Yn1N5SUQu01vfG76pHTX0E1ovEApRIYSlzI3Pv1lnzq6qnbd7hTKJzM1JKRn6qArt_TPcfkzNQkman4JDmHs7AJPSEwF9eeCfB43Oh9sdDYng8SxP4rdU4NW_vD85qcsLPoT8SCB2RHWJyHhwo7GJ_KRf7qNuwHKLml0qv6lcMkMDoPTqW-0udSu5CCGsB5tGPMBBLha_xjC_q_eLNMPIhJYP4jKa2DuaDUbh2TEftjed8MAX9_wZG6lnemQioJ-TYyF-erH2voWPX2pnPuN44ryiGZwy1stpXqKsAh0i6MNnuWv9LjYeRI3XLbjjqxmuyoanlfOKdHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=Svy3LrXDVg91bhjCV4wdLpvMWEmTwlg7iTvXIFZjZcnvfwkU-fHP0tI_ja0JB-JkLHDLZxHiK2h35jqxqeKHlFIuH8CHLaJispWtHa8oV9X4X5fsM55fWkC79VviLFu-9E9aMwNvDqNP00uUedxwQj1qeSBFIR8ThrmRErEQL5i2JOyqcgI425sGEDhD35hEOnz6i2cejG3ANIcZyr4uN_YhbKKgWNexzPv1dG6OOXd9G5_zzyRlDAKYVYsNDrhB-2lIn3-5lTVeQL19B7Yk4eHdKSsBs1Iwj1d-QfB7Gn9kwP_tH-AnlJDlgxl8pQqxIneev-zxP7kSlQmuOrJUFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=Svy3LrXDVg91bhjCV4wdLpvMWEmTwlg7iTvXIFZjZcnvfwkU-fHP0tI_ja0JB-JkLHDLZxHiK2h35jqxqeKHlFIuH8CHLaJispWtHa8oV9X4X5fsM55fWkC79VviLFu-9E9aMwNvDqNP00uUedxwQj1qeSBFIR8ThrmRErEQL5i2JOyqcgI425sGEDhD35hEOnz6i2cejG3ANIcZyr4uN_YhbKKgWNexzPv1dG6OOXd9G5_zzyRlDAKYVYsNDrhB-2lIn3-5lTVeQL19B7Yk4eHdKSsBs1Iwj1d-QfB7Gn9kwP_tH-AnlJDlgxl8pQqxIneev-zxP7kSlQmuOrJUFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68160" target="_blank">📅 13:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68159">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgwDochSO-8SMj-8zB6i7ZY9PTmAsnPurJNasXienOuklP9C0tyfQHFhyQpE5wxoz3PJggTaDWkSDz8PI3TqOPZ_4AKRY82eIoN-Dlc0dOATAEH63n4YCfYFVe8xSYMcAvrINF6yZm7jK51hmResSnuZc-VortkNf427IhGJNSTw9QVSagEKJ4u5r21jQ4i9qAAGiuseGDlLlJGXgtRMBmGaz1GbSgwq7cmwPFkxjnA1K5mURDk1ieJAqyZ6orjKgRkPlbI81nbjby8fRQY_McDC5lvIhw085BSgK7v9n50pJ4iF5hrmmOmAXajS8PvqMfLoyBfWqvAQtjkF6Lt36A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68159" target="_blank">📅 13:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68158">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNo-7CG4zHaSVV-b9vPLQ3rLL93oTdgZn9d7Y5Fp5qJaKDea6Kmfs7uNNLe8Vp3lWzu4XLCG0h2AeJZAidYviDW9UxQGRRhMVoOfOhIfINJ52GASbe2awqPNK8dX_En-SiRARGhqq_HGuqyZbpl_YB2bhbdemYGCkADJMXpndkKYwNF1gYUUe_5fBf8IFwLDYNLTHXWMU97qYe74YYxfenLwQay5nZl1qj3IzYbYsoAVg8Dz8dqVbkUsb0qvKwYB5jxIeuKXZNKM7CreVm_w04y35ivMadLEoWd5fqnMyahefwYsWfPJHnhq1czZB2QVMuqYBu1nI0NCn9Xs06w0xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرِ داریوش فرضیایی (عمو پورنگ)، بعد از تحمل یه دوره بیماری، تو سن 90 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68158" target="_blank">📅 13:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68157">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‼️
امریکن گات تلنت یا همون عصر جدید آمریکایی ها
یک شعبده بازی توش انجام شده که حسابی وایرال ‌شده
👀
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68157" target="_blank">📅 12:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68156">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfZOxhv8K7rJ7KD100xzZt184JibKmQet8u2MPXAuf4XaV1DvAs3GbCkusPS_N0aFWc0CFX9CgNZVwdO_XF2KakkG_fIXg5gGhd56ATzfQMKqpdBO8R2mviaPPYufE3omXwyIv3Vth9lvqBdjx2_oHuRvy7ewsW3VgAwYvEXpu21xuCKGtG2QjoaZWhwht_0uifYCGp3Z-GCtYd0OFVnmkSQzCAf_tuOqLnj9cQU_rr-pXtQE8i8r2kAUZKRtRWSC7Zp2YBPgEoIOlsqfKc-BOjGL_SkSzlLUlfPU9YUX6iM20DME3lo3mDDroyMzn6NDhPSNb2JWG6hd1HAHqB-qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ا
کسیوس:ترامپ در «اتاق وضعیت» جلسه‌ای درباره حملات جدید و گسترده علیه ایران برگزار کرد.
به گفته سه منبع آگاه، رئیس‌جمهور ترامپ روز سه‌شنبه جلسه‌ای را در «اتاق وضعیت» (Situation Room) برگزار کرد تا درباره یک عملیات تهاجمی گسترده علیه ایران گفتگو کند؛ عملیاتی که دامنه آن وسیع‌تر از حملات کنونی در اطراف تنگه هرمز خواهد بود.
به نظر می‌رسد ترامپ مایل است جنگ را تا حدی تشدید کند که خسارات کافی به بار آید و در نتیجه، حکومت ایران تنگه هرمز را باز کرده و خواسته‌های هسته‌ای ترامپ را بپذیرد.
ترامپ این نشست را در حالی برگزار کرد که ارتش آمریکا برای چهارمین روز پیاپی، حملاتی را در منطقه تنگه هرمز و در امتداد سواحل جنوبی ایران انجام می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68156" target="_blank">📅 11:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68154">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5c420396.mp4?token=DWDE7bRG3HhakkvC-KF30myhAMm1hCNG6iEaWxMLg8zZB259nJX2DhduSbaB88Ph0KVS0Xf-sSAgmmOauna-WHKT4RHB5fRZlRCdME3BIpoWopQZOpf1e0GIWZ2XwDqVMalQp3TqfoNgtIV6u8D7jbdLO5RacUoBm-kWzT-Hvu_oLTtsEY-4oo6EMbxLagLWiqOitzr5yAgP5UZu9KRIM5VYJ5dwyrx5utY8lioRcpzMWdsg2lk019Xd4LTkA08CTa-o4DdZ-kyVUdI8ckl-hwQkv2NubIuxercMh8FmHrRW8rCJa0mudc00gysCKBsHyYmN9EViI48eWtehV2Nk-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5c420396.mp4?token=DWDE7bRG3HhakkvC-KF30myhAMm1hCNG6iEaWxMLg8zZB259nJX2DhduSbaB88Ph0KVS0Xf-sSAgmmOauna-WHKT4RHB5fRZlRCdME3BIpoWopQZOpf1e0GIWZ2XwDqVMalQp3TqfoNgtIV6u8D7jbdLO5RacUoBm-kWzT-Hvu_oLTtsEY-4oo6EMbxLagLWiqOitzr5yAgP5UZu9KRIM5VYJ5dwyrx5utY8lioRcpzMWdsg2lk019Xd4LTkA08CTa-o4DdZ-kyVUdI8ckl-hwQkv2NubIuxercMh8FmHrRW8rCJa0mudc00gysCKBsHyYmN9EViI48eWtehV2Nk-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه برخورد پهپادشاهد ، به طور مستقیم به یک انبار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68154" target="_blank">📅 11:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68153">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fsuw8VATZUpV4dhFMykbQgnhbcE3tQSpBAuN5Y_jMTKPSkcaHnEYJPR3S9jfIm8KM8UDNJ52mD53sVDRvvsfhmnPxco59vF1BNaoXvZqlg_CUfmS_DEr05_hVa8_8tcLfnIgATyi21QZXUdH9HUzUsplI4nC6KCva5AMQ5ZMgK11k8-605RQqLLLyairAQQAdT3xm5gVS3FcpRYzxUINdsCVvK6QzlZK1mm_zG5FB1v47lH6qxeprq49VzhldnYTihcjtOUh0zTozUejKwDFGw3rU_5HBn7IR4-zxQH2CPpNtTt0MMFA_RlDBYV3yh_GtYjlK-3ymtbkLkDSQ_75_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل بچه‌ شیعه‌ی آخوندپرست
🤯
🤯
🤯
🤯
:
#hjAly‌</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68153" target="_blank">📅 10:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68152">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c4cf4b27.mp4?token=GA3Olbsvko7qX39GGI_2Qd63URDqO1lOu7vUvHZK19Okk51Vcb1w7p-725BtA5YQAWdQRKJ_tHT89ATvQEMjgvVvO6RAr-1KWN5E1N2zig6K0hjTO0HbDm-iS2LydK6SK_CaLMmcC1NnDGftZV2BGiY1JeGL99GlCHD_DOXykYT4LPVm0DcLx3oVCReeqSEbZ0Mg1P3xQrA6zmaV4sboKAbARtRZDN7v84EDuey3Sd3Ei_-il5PiXcyUfj86EV5FqBWKy6GOw_oC_NQOWqBFeo9vRtXOrrSUj-8VXJyDZeLSRYkaAnAZqToT2S2T2eidPri38cZ0JlOcjD00U_s9kDQGllpPMCF7MgyKcb9HuTqRYSS7AWEsB4jy28y_Z6Td_Kt6yN3dwJUZnCgXDTqBPEL-NI-N8oDOpfxJYIK6hEozxtbJRV5dKVJfRNE45DYKbiU3XBWpdboi6WySvSIskiGc5qnQzHMYbIGfH_8JPlaiMuy1dvcTHWlPxTI6QyGTNp4hpOnuw2oT_SeVivvFQolfGXcEc4PHIj-DQp2LJjV00owmW3cIiDbABOW-rmvIxYCrylelogURPF9P3zLCNQAzsH6HE6_Wju7TZ6XhX-EOAdaiGMZtRXVci1ldBzMKmc-CHmm6R4lrhvyyZoablJlthOIp3Q6FZ5JVnyCaKrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c4cf4b27.mp4?token=GA3Olbsvko7qX39GGI_2Qd63URDqO1lOu7vUvHZK19Okk51Vcb1w7p-725BtA5YQAWdQRKJ_tHT89ATvQEMjgvVvO6RAr-1KWN5E1N2zig6K0hjTO0HbDm-iS2LydK6SK_CaLMmcC1NnDGftZV2BGiY1JeGL99GlCHD_DOXykYT4LPVm0DcLx3oVCReeqSEbZ0Mg1P3xQrA6zmaV4sboKAbARtRZDN7v84EDuey3Sd3Ei_-il5PiXcyUfj86EV5FqBWKy6GOw_oC_NQOWqBFeo9vRtXOrrSUj-8VXJyDZeLSRYkaAnAZqToT2S2T2eidPri38cZ0JlOcjD00U_s9kDQGllpPMCF7MgyKcb9HuTqRYSS7AWEsB4jy28y_Z6Td_Kt6yN3dwJUZnCgXDTqBPEL-NI-N8oDOpfxJYIK6hEozxtbJRV5dKVJfRNE45DYKbiU3XBWpdboi6WySvSIskiGc5qnQzHMYbIGfH_8JPlaiMuy1dvcTHWlPxTI6QyGTNp4hpOnuw2oT_SeVivvFQolfGXcEc4PHIj-DQp2LJjV00owmW3cIiDbABOW-rmvIxYCrylelogURPF9P3zLCNQAzsH6HE6_Wju7TZ6XhX-EOAdaiGMZtRXVci1ldBzMKmc-CHmm6R4lrhvyyZoablJlthOIp3Q6FZ5JVnyCaKrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوندها عُمر طولانی دارند و بیشتر از عمر متوسط ایرانیان زندگی می‌کنند:
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68152" target="_blank">📅 10:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68151">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1084df804.mp4?token=iQxrp2WjWuVQjZcX_un165lkun8DJLRtVVIgq8viE922epyrXvrKva1EF_HTazu1BjiHwTK-tnKbkzkF4Rz8vhBn71iVu72sp79zqA9hdbnrTj1aCOAeoRyxrpv97uMBTT_LDgC-xa0CLxiweKtaPqNX6YwfNJU_wkmCiHGFlJqJIjseAfTbR470pbLf8dinkrOcg9-xE7Sy2q2VCuwzzDXxU8WBsQzaSiaFojwVZMBlzNZ7ZigSd1vV2DpRkR_C_o931vKi330pHU6-b4sqAq0SXEovm6LBsyp9ZsK--aa4zwRP4ZqWlYV8xdmiz5H3yWvyky9-njXRLssrUAYjSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1084df804.mp4?token=iQxrp2WjWuVQjZcX_un165lkun8DJLRtVVIgq8viE922epyrXvrKva1EF_HTazu1BjiHwTK-tnKbkzkF4Rz8vhBn71iVu72sp79zqA9hdbnrTj1aCOAeoRyxrpv97uMBTT_LDgC-xa0CLxiweKtaPqNX6YwfNJU_wkmCiHGFlJqJIjseAfTbR470pbLf8dinkrOcg9-xE7Sy2q2VCuwzzDXxU8WBsQzaSiaFojwVZMBlzNZ7ZigSd1vV2DpRkR_C_o931vKi330pHU6-b4sqAq0SXEovm6LBsyp9ZsK--aa4zwRP4ZqWlYV8xdmiz5H3yWvyky9-njXRLssrUAYjSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیش‌بینی پروفسور جیانگ از تهاجم زمینی به ایران
:
پروفسور «جیانگ» تحلیل‌گر سیاسی مشهور در گفتگو با «پیرز مورگان»، مجری معروف انگلیسی، پیش‌بینی می‌کند که «نیروهای زمینی» آمریکایی از اوایل ماه دسامبر در ایران مستقر خواهند شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68151" target="_blank">📅 10:02 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
