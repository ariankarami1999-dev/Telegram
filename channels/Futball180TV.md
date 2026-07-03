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
<p>@Futball180TV • 👥 652K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 13:09:54</div>
<hr>

<div class="tg-post" id="msg-97857">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afX0mGWbijTEGPl8QUFLXlSVaW2DXaXUxpxfwPY9ujdxIPB-LjbE4dLnDLgWSAnjQl_A-F9nt745v3FfM7FlfEMn21FPhDbhECx0my3-Og8lTPa5RRX0lrdwEPi32YKWdpDtTLI7SHivn8BoTUh_VHsZClo_JWTIiuNUqh3t_Wh7qAI4c-tBwws7I7QzsA3M_RRwxou08lyNaQu7aBk35KkdhfrbGVBnQYXX56XDDtd8esfwRZyvp8jFK4IVgygbTDGZBdVTPQ3YxruFiueSXUDqTRwbAwgwvHu7YPHQTB9fIIbuSYFbHvGVGQ42GKonR9KyrjPFgVC_yJ_ut0SAkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
جرمی مونگا با ۱۰ میلیون پوند از لسترسیتی به منچسترسیتی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/Futball180TV/97857" target="_blank">📅 13:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97856">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f201981e1.mp4?token=FK_BHj-VZl1JZSmYqp-_V2v0GCwfPSI8ArZBjjQwtCNdl9Od9iTikefW3ODzMk3oOXCugFVWj0QWwYEoRHtiOQEKJVLw1arKcGkfSGQnj2oNN0YfyjV-mKxgkFwL8rG9XKzPlOSzdfCmc43yS0NHFuJLnjNSPebLTiwIS3g-x6v_k2ziSX7LeT-hOIXgJqE_QgNtsHkY1t2Et34svLmqjvDHDPQ1dnTIKFFi1H2lxVLBHpFL9MliT0m7Ylr9IDgdt8vMCzcAKsbZD9xCCkHI96K1iAdKmYDNewsRCGQWowbq7dbPuJkJI8re68pt_dYCoj2_WCSP6esqkIIgIrOedQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f201981e1.mp4?token=FK_BHj-VZl1JZSmYqp-_V2v0GCwfPSI8ArZBjjQwtCNdl9Od9iTikefW3ODzMk3oOXCugFVWj0QWwYEoRHtiOQEKJVLw1arKcGkfSGQnj2oNN0YfyjV-mKxgkFwL8rG9XKzPlOSzdfCmc43yS0NHFuJLnjNSPebLTiwIS3g-x6v_k2ziSX7LeT-hOIXgJqE_QgNtsHkY1t2Et34svLmqjvDHDPQ1dnTIKFFi1H2lxVLBHpFL9MliT0m7Ylr9IDgdt8vMCzcAKsbZD9xCCkHI96K1iAdKmYDNewsRCGQWowbq7dbPuJkJI8re68pt_dYCoj2_WCSP6esqkIIgIrOedQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
تلفظ نام مسی اگر در کشور دیگر متولد میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/97856" target="_blank">📅 13:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97855">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51882d6736.mp4?token=bjgY8MHZhoh-saptBbYQTddGzLIjjxOVBV6GOIM5BMCggMELW0M1VKmiSBTL4z6FGese0iqv2_rFwpOcOGg6m-nLPgfx9iJA_GLyEFM0IR_ViKq_rc86K5fR5k94brKGqOuQUAmlp0UuQGCkbg0cEgk80IGngyt7v4XlnXJbiXQuvb6XWSwduoztdMftFoPdgsZ8GUCsexIu8aLJLFYRVwWeth0TkXOwBxE4jM9SOvMa10cEPdS-DjpMHfpXT2YaXnnJJAZ1-clH2q0h9w4QC5cjU2ZEeUUCi-RshlXN0h13DvwI6ECPpZ0-0bqXi8lWH7M3iGBLGjh9B3qkFw8_ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51882d6736.mp4?token=bjgY8MHZhoh-saptBbYQTddGzLIjjxOVBV6GOIM5BMCggMELW0M1VKmiSBTL4z6FGese0iqv2_rFwpOcOGg6m-nLPgfx9iJA_GLyEFM0IR_ViKq_rc86K5fR5k94brKGqOuQUAmlp0UuQGCkbg0cEgk80IGngyt7v4XlnXJbiXQuvb6XWSwduoztdMftFoPdgsZ8GUCsexIu8aLJLFYRVwWeth0TkXOwBxE4jM9SOvMa10cEPdS-DjpMHfpXT2YaXnnJJAZ1-clH2q0h9w4QC5cjU2ZEeUUCi-RshlXN0h13DvwI6ECPpZ0-0bqXi8lWH7M3iGBLGjh9B3qkFw8_ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صعود پرتغال به ⅛ نهایی جام‌جهانی 2026.
🔥
🇵🇹
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/Futball180TV/97855" target="_blank">📅 12:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97854">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ImoaQIR8-XiVjGl9T2dxXVFG1qMtU7i-5teohj8VjNmHoiGaAc6fepp5S6Og06tSlrkDcVLssU3GOgip43b0-ovcNnoCA2tHnfS8PBY7cxzhe3r6ez0aqHI9IxTGsHwJV8Iy3ndzF-0IPzAEwlyyRW2ajGoRZ9KyjFy4LVwrZ9tmV20bhGFtmo0278RalgVagLbhAnxocrqdghG3Rim1u0rq0mzE0JuVZgHnE5v4ZCazOhuWy-jpCas9zTSKb0ydWdtnpP2XedE-VSAVodWcCGpuWIbjsq9ZeD1IJABS2bel5fJORpUn-SmgSSDDwJ4qJEFROyM2-ytNaJ1l5ysXFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه لیورپول اعلام کرد که یک بنای یادبود دائمی در کنار استادیوم آنفیلد برای بزرگداشت دیوگو ژوتا احداث خواهد کرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/Futball180TV/97854" target="_blank">📅 12:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97853">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCxJ8X8wiFIaI4rdFVA4GMeQ9iMebtwbjuhJ52sgTI_fSM11i2ufHVirDSnzgXp9YxNEr2bQyG21MV9GfsjVn0y9gYmX9JagGzJtZFV3crNrelX6l-w-MmGBOo33E8YaMl5hPK-3Ou3-INjt4HWc6xvla_JIOH7JeR7lPKMKvTyx0J3W1DeP0mNl5g3Ksd9hdf5Km20MHBaHdFFukdxbMr27Y_cNZmzX2FrdjKPt-4Q3FbVrGgB1DY3yuakG-_rz9xkITGlBaTrkuWacTr5lnLLYVPSPCZY7uoLAqfDovk2DDs_6iTtZEl-4Ghfa3ORvA9l6A3_BRxGHMdraZRSfgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
👀
صرفاجهت‌اطلاع:
🇫🇷
فرانسه در سال 1998، کرواسی را از مسابقات حذف کرد و قهرمان شد.
🇫🇷
فرانسه در سال 2018، کرواسی را از مسابقات حذف کرد و قهرمان شد.
🇦🇷
آرژانتین در سال 2022، کرواسی را از مسابقات حذف کرد و قهرمان شد.
🇵🇹
پرتغال در سال 2026، کرواسی را از مسابقات حذف کرد.
🤔
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/Futball180TV/97853" target="_blank">📅 12:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97852">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XO9Xu77HybpoAO4xZ2nnawbDY9P2nSKGzAFq6ERnwvjI14SmWIuPiaRPM5eHBm9qB0cr6ShEUUqTzEdbge3yEd61GzBt854S_vnJTlq5mtXYEvhGZjbbMtu-t1yVIiiKGDvomDW6sn_CxW0f7mB3Ak06YH7GxfopzwD1CgA0eCgUX4GaT32Kh2dpQNW7fpJQgYVP_e3PoAhkNeuHArvBzVOQDjI3LfKoebIrXj-QOO0eVQjdCDIAEBSXDcKGUvvyGF3LF5AMDgik6AzUJggo3o0XLiC1Hbw8Bt89qwAjPyJdQ1FAhXArQDEoiiOwyNnQJifezfmdtuN0_Jq4Z1gMrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
‼️
جادوگر غنایی بعد اینکه‌پیش‌بینی کرده بود کنگو و ساحل‌عاج حذف میشن، حالا گفته که امشب نسخه آرژانتین هم پیچیده و مسی باید با گریه از جام‌جهانی خداحافظی کنه!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/97852" target="_blank">📅 11:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97851">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5nEYVqTRyOIlFwmkksm6qtcS11tIWPa72HIEed2yk2mK8PCiQv_RM0Ia3gFG_w5dSNJRAyoVK_H5OvitQGynM_tYqLAyXmcL0kpuK-PNA8bcNqKZs4UG0ZGCNEzU3_RfrRL6Ch9qvbGE3cChRepD2etX6GoKvtKWcs3csh29Yq6_6Dpm60iMGeGKXEVHgftYeOyeWz71EiCeOmpBSeTQJuXOYaH6nM699KbGi3EMJZR9Tpa-3iBpNYrooqVkBAQ7G8ggRDGkvv3LNB4P1IKGpS8F6EnzttFkFf3NCBkKOVXo3UrAUFVEjJIYizeaZAZPZcFkXOcO_oRcLU-WAhtcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/97851" target="_blank">📅 11:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97850">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyI72qIGbMZ9fvQ5V199o2Fd8BuWG05SBiA5ytQxjkGOByiLKr2lDvDhsecRfzzP_wS7mysTA62Qy8kwpNMM3F_X9YkRYdpZchExt1yzWVDKfxdIWmxWWxo20ltQpZZXfVk3eEi_6Adb5WupBneUyXQGbedCQtKsynzZ9P9dMgjnTJrjCPqCbbFgSy2LyXxTkZBs7I2sSDUM1ochCGXDiM1xuiYhCW3CH9FekeTcAn7nXwSeXAk52LQwX32zcGTdKODzfuSHMwBa4v3vjLDyisHwDnA6uMCELxEJhFh_aA6LmYfKmOM-iNDKF_URo1LmFxHBKbyt1f7VXgz1UDHYBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بازیکنانی که بیشترین بار جایزه بهترین بازیکن مسابقه را در جام جهانی کسب کرده‌اند:
🤩
لیونل مسی — 13 مسابقه.
🇵🇹
کریستیانو رونالدو — 9 مسابقه.
🇫🇷
کیلیان امباپه — 7 مسابقه.
🇳🇱
آرین روبن — 6 مسابقه.
🇭🇷
لوکا مودریچ — 5 مسابقه.
🇺🇾
لوئیس سوارز — 5 مسابقه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/97850" target="_blank">📅 11:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97849">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFx-9rrRbO-GJWzSoL4nL0_VGuqgVPK2OSpSzHjwzsMXR3wfVOeJwmPCVAF062VAurVlnoVDbtYFGdt3yEeQ6XtiTvXwWz4p5qQYPX0dPemU5Hv_qal9xDil4JaQhevFHUHQt0hS29Q4B5ktLMSLwQ8JuotHa8L_F9iymnELThxrK11D4wyGpwilSrYWjZC9vaTh-6sLjv__K786G8emtGFJYUbR7gQLbv7s1tI5yqJ5JsjIMXeqB1P_Yx_ZhxVphL0G7WYQA_yflSA9BDBK4fpcNBTZpWT5eYWDvF7hyETzAcVVW5EcxZOn2kr0-nGhMBPkKQ72ruQ-0FKFq_sZmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇵🇹
برای اولین بار از سال 1966، پرتغال موفق شد بازی که عقب افتاده است را در مرحله حذفی جام جهانی (در برابر کرواسی) به پیروزی برسد.
لحظه تاریخی قبلی، یک اتفاق افسانه‌ای بود: پیروزی با نتیجه 5-3 مقابل کره شمالی در مرحله یک‌چهارم نهایی سال 1966، زمانی که اوزیبیو با برتری، نتیجه 0-3 را تغییر داد.
و پس از 60 سال، "بازگشت معجزه‌آسا" دوباره تکرار شد.
🔥
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/97849" target="_blank">📅 11:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97848">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80ebb6451.mp4?token=qQUIfmOxNeb9ymkzXgOKlykRh8X_Mn9XpllJBMOIfB3gwzY3nm9h8w74rKGryw2FgYg6TQe6O9spbAwdEqDAl7102CDEyNtDcDy0q3MiqGLzAh7VqDeTjXoeHYjpIKw5YT5a1Kv-cUxjM3eF9QtJ9--Ftu5e7lDwkH-BT-G8Z9QGti07Bamfy4DuOu6mrRaSbusv_QTHT-PBW_0uLj4fOyZlwsQhM9NZRxNvzUQf-3VGxTGcFStdlBwRnSs-4VqoeqTrz704X94kYF6wwKO9AD_s-ZNlIfwaL9WGUQr4YY71aBO37QPvXoHfg8-qAmixHeXgiSQ_ZRXpRFubQd3B0oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80ebb6451.mp4?token=qQUIfmOxNeb9ymkzXgOKlykRh8X_Mn9XpllJBMOIfB3gwzY3nm9h8w74rKGryw2FgYg6TQe6O9spbAwdEqDAl7102CDEyNtDcDy0q3MiqGLzAh7VqDeTjXoeHYjpIKw5YT5a1Kv-cUxjM3eF9QtJ9--Ftu5e7lDwkH-BT-G8Z9QGti07Bamfy4DuOu6mrRaSbusv_QTHT-PBW_0uLj4fOyZlwsQhM9NZRxNvzUQf-3VGxTGcFStdlBwRnSs-4VqoeqTrz704X94kYF6wwKO9AD_s-ZNlIfwaL9WGUQr4YY71aBO37QPvXoHfg8-qAmixHeXgiSQ_ZRXpRFubQd3B0oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👍
یک حمایت کوچک از مردم مصیبت دیده ونزوئلا یا نادیده نگرفتن یک خبرنگار دارای معلولیت؛ هر کدام را در نظر بگیرید جود از این آزمون نیز سربلند عبور کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/97848" target="_blank">📅 11:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97847">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAUsOeTgNu5PjPtM9nctzoOO5BGOrr1WrfVK9j4LuPStNiOfvk4dwxvo5mKU8IaeGHy3V8FYpzUZqZG7AejfqJ5CEj5JKAo-iWcIrz5pCsvgzR2c0amcK5E8TgYDmc63V5uVpQRRMF48vDJZeW_SP-92h3rfzpYmyXlbbyK4NG7YClbugr6Exte0ruUmpczq2rfw-I1je4CeVKOM7DNf_eGrQJrRUiDvhdtddegKm_xuACz4-I9lrIffIbkHmOqN8U1Y7OGWRNfUr8WI6VFBCPZYHH9wXzrsgXbXyc1rgsZ1T9sf3lRZOkGGRAX8CfQ9paF2Juwf_JZxzRiE5_kLGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو : آلگری به ناپولی HERE WE GO
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/97847" target="_blank">📅 11:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97846">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVV0Y0uqI2mN58Prf8uKkbShCsWMfCrKfALlEpTCSKrd4g9NuAcFx4_6ZJLwoCaW_xbMQ-RSq5NtNFjIVhGprbjUQ_rmK0Xzyb3R-Y_3JCHA6g89rD7nOQIqjYw6wFr1doTKHsZJm26ozDx_qmkQJYGhEoYRfyhFC1-6_CzTQXn4KvtPfZ-ta05UYSXZ-YlZzWqN4PqIPW1OjYo_LC_nfRgekecwwlWa_xI13qAnSsd7gUuOUeiDxqfyQDRk_UCsS4EXbXJ5gyyKsiIihVh8rXiz2fAqJ02jlYt0DUYEZWGNMav0OXNLQt7CiZmgNnbM5n5fESzIdZEgCfgLehyJ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رئال مادرید علاقه خود به انزو فرناندز را تکذیب کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/97846" target="_blank">📅 11:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97845">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f386995eff.mp4?token=vL2gYrL0BfKLuJY0TC7fVswHUjZZRcDhq7uugBS771X9GDISHox9QIDKaFFrrzo4wvW7DsGqAZR5Rtmr8lF4JAMgDcfeMhDUYbNEd7_0Ir0I39qI3yaRSsgeUCs3rAzS7SjR0wlAkXw4DJB7GaAQ8R9d4Pm8HLFTEoYwqo6kBYdz9JznX3rJKej-O38LFcBA6ubqzb8cG3rkp3tuMHMifQNRpTBD8-CxCeS8JU_1tkJH2V-zSA0HQqhOgI13pLHpW6tmotoy3NOEeglEGhkBkyiCRr0QIuYCyOLAiL6aJZDifpztZ1tV1HfCRW2LWplKQ8fA9463Pp18WS9Qs4CWrYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f386995eff.mp4?token=vL2gYrL0BfKLuJY0TC7fVswHUjZZRcDhq7uugBS771X9GDISHox9QIDKaFFrrzo4wvW7DsGqAZR5Rtmr8lF4JAMgDcfeMhDUYbNEd7_0Ir0I39qI3yaRSsgeUCs3rAzS7SjR0wlAkXw4DJB7GaAQ8R9d4Pm8HLFTEoYwqo6kBYdz9JznX3rJKej-O38LFcBA6ubqzb8cG3rkp3tuMHMifQNRpTBD8-CxCeS8JU_1tkJH2V-zSA0HQqhOgI13pLHpW6tmotoy3NOEeglEGhkBkyiCRr0QIuYCyOLAiL6aJZDifpztZ1tV1HfCRW2LWplKQ8fA9463Pp18WS9Qs4CWrYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮‍💨
🏆
🇦🇹
ایستادگی برابر قسمت و سرنوشت
دوران فوتبال عجیب ساشا کالایجیچ، مهاجم اتریش مهاجمی که تا ۲۸ سالگی، ۳ مصدومیت ACL را از سر گذرانده
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/97845" target="_blank">📅 11:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97844">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05870783f5.mp4?token=h10vjsk4twjCPTPES-FcgxppvRiLinXXPPI9V8UDYSdr-a2dY1qR9D3YG0fPMTq7q7DHcWbcX9ogXEUR9Mlgk9QnLFinAreKVK1lp6QeAQdLaZ93EKzPk7vJLrDxCZS_ZpVqjMzlxMN73xvozt-SQnMnEa6CFf3PvULHWzwPYTgu_2wsYFEsGEpWdt45D-RjTfDzQwPIMuJbKHodlfc4mUCxkja4S-dajdMG4NrQ0VPgLUUUkZMPt5eKQQJMfBBMuKMTtPANxk0wDiJz1pCGD82xDBSsQmCXFLzhKkgB7TrZsZ2D6EymM3CI6jmELfNLpUL-dGuYFyBLkQDtCG7OwKOVrp3o6y_pB4O6jK5FqX5g6ofxnr9a35sxEXnLi_NAESb8Jv49GKvC_zeCz_2luAJVPHf7Ywtj8A3dwqmz_r-MjUvRqn8nGwpr-Dfc2gIYW3gLhFi0Gu6LxMjrBWhVP-f3iA0On-f5tMKn8fzR5dE8jIAsyntSOLqw-BHVIXua5eTXjw_yRlTyUzz-aObBFvlssTFzare9cqbl6htGEV4Ece262nsbnT50fmudTTSJ1tF_n4SBb7NWhpI6IM4Z07qYCkpe_25AQQPNCb5SM7G-KepeAy8nm6zW6bvd3UOcBDrZdEXBvy9_H_DLJswPH8iAHGvFRkF9dRmVwKRZsAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05870783f5.mp4?token=h10vjsk4twjCPTPES-FcgxppvRiLinXXPPI9V8UDYSdr-a2dY1qR9D3YG0fPMTq7q7DHcWbcX9ogXEUR9Mlgk9QnLFinAreKVK1lp6QeAQdLaZ93EKzPk7vJLrDxCZS_ZpVqjMzlxMN73xvozt-SQnMnEa6CFf3PvULHWzwPYTgu_2wsYFEsGEpWdt45D-RjTfDzQwPIMuJbKHodlfc4mUCxkja4S-dajdMG4NrQ0VPgLUUUkZMPt5eKQQJMfBBMuKMTtPANxk0wDiJz1pCGD82xDBSsQmCXFLzhKkgB7TrZsZ2D6EymM3CI6jmELfNLpUL-dGuYFyBLkQDtCG7OwKOVrp3o6y_pB4O6jK5FqX5g6ofxnr9a35sxEXnLi_NAESb8Jv49GKvC_zeCz_2luAJVPHf7Ywtj8A3dwqmz_r-MjUvRqn8nGwpr-Dfc2gIYW3gLhFi0Gu6LxMjrBWhVP-f3iA0On-f5tMKn8fzR5dE8jIAsyntSOLqw-BHVIXua5eTXjw_yRlTyUzz-aObBFvlssTFzare9cqbl6htGEV4Ece262nsbnT50fmudTTSJ1tF_n4SBb7NWhpI6IM4Z07qYCkpe_25AQQPNCb5SM7G-KepeAy8nm6zW6bvd3UOcBDrZdEXBvy9_H_DLJswPH8iAHGvFRkF9dRmVwKRZsAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
ریکشن‌های اسپید در بازی کرواسی و پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/97844" target="_blank">📅 11:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97843">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SomISN3GH-UG0uiNob9w8fHuOlw5OhddByx6CtryvPkWBUTYJ3D9JJIDla_Af09pop_nrUEOT7WBdPHIj6OwWVQaGtWLJMVIGl5cgyf_xJ_WLt82ih-gvoSgxis2NJo9DXEFDTbnNWJdyV3KDN6_yjf68h0a24FJ-GPH0OuK3-2UsAatc-At_ORo-4fMz5g90SomrttFsUiMr6txDceaS_iISeJx3AO4Znnw2UUO9a4NKFOVsmeUwu0GhLv1mR6obnT3lHHcxUCTZfBnTIb3ji3NSpKQT-iBExtufz1cZlxjLyKS0p2p5m6DAjwtgxl9j6wyCqqhTZg9GJSRPC030g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مارک کوکوریا اولین بازیکن اسپانیایی تاریخ است که در یک بازی حذفی جام جهانی دو پاس گل داده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/97843" target="_blank">📅 10:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97842">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/307bbcfb1e.mp4?token=teox4OSmP5xaWbYoWKkKI87d8agnOhH1sq3aR9X6tD-HLagvBqDPWblNe3o2cKY7ECsQ0uYH_ugVdsQW3rc4sb2OHS4KYWhLuXibS2s6G7t5Qar2Zr0uYZFNossp5VTAcDOu6FBctOInhbUyMVxI8B2Za4szrsGAe9Bz6FTovzfUnB1uJmK1AGpByvtCmozZpQE0MqlDH6gbeAn8W2cc8cwzPFuR7MZOAuzlx_jjeCFu7_4_1xKDYOHBwblxljO1P5IYBUtuSla3_gtw-Zjduq4dvA4VMYrIasuV2nRmN0hj91lRtzMmUAxUQg6LqIGZLLc8ZqJWEw330W0nkvw-iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/307bbcfb1e.mp4?token=teox4OSmP5xaWbYoWKkKI87d8agnOhH1sq3aR9X6tD-HLagvBqDPWblNe3o2cKY7ECsQ0uYH_ugVdsQW3rc4sb2OHS4KYWhLuXibS2s6G7t5Qar2Zr0uYZFNossp5VTAcDOu6FBctOInhbUyMVxI8B2Za4szrsGAe9Bz6FTovzfUnB1uJmK1AGpByvtCmozZpQE0MqlDH6gbeAn8W2cc8cwzPFuR7MZOAuzlx_jjeCFu7_4_1xKDYOHBwblxljO1P5IYBUtuSla3_gtw-Zjduq4dvA4VMYrIasuV2nRmN0hj91lRtzMmUAxUQg6LqIGZLLc8ZqJWEw330W0nkvw-iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🔥
🇵🇹
شادی رونالدو در هتل اقامت‌شان پس از شکست دادن کرواسی و صعود به مرحله بعدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97842" target="_blank">📅 10:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97841">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0MKU8gu2rRhvQXcPQOk2nsdV6472YrCtX9lCvTKcqf_IzAs17HVqGTOb0r1jD9vLeiOfSdIsp9drqY_R5ernFx5ETQGDgE657y_pU2RorbPcPV9TPGxDe0n4hwvfmaDea-dn55OtzPWJCQb39tiqVRHQx7vrpfNDneDnonUCmutO5ST3f8o6dHfrlSYeBgoC3k9fsqFmdGG1by6gajYlvuWWKv_NGnM4Pdgahav9vwBUt_ForwPKJ0HdtDoFanV1JJ4ykRKvo4clpYCBIPfEY0yhxd4cD4YdMh9VFEu4xzu12Qy_lzjcSp08B4sZS3Arsxzmo9crrAqxh5VgAjReg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
#فووووری؛ رومانو: ناگلزمان از هدایت تیم‌ملی آلمان استعفا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97841" target="_blank">📅 10:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97840">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fc4fcb346.mp4?token=qKt77yWDLJjuBurn3925SQk882b1n1CZ6W1XX86x5iyBO8q68LhyDEBWmT0W7EYWw6WQeHRrIJ8AEkq-7J4MeushR-dpu-wnYmefXHOWrULm1seeJcDGTs5dm-Zem3HM4n2UsUF0n-mb_PamWPsqXxnQKHtFbpixCaeExChDUNLyc88gi7hrWm1ffP0yWQt1_SDEIQdX7xIhmnBeiznk4cOd3zlkaXNhLlnC8EXBi2a-M0xd_dQNybvEBqBgOy_hyh3IoNGwG8fY9OWkH1ekAO4_KkPHTqBrQdgY9rCW_t4d9K-yLUxXptYgioK9upAwI3Qp7ISRd6Gf9rHh9jHxZwdkUbwOQJwkbI054jgK7adOPBTeSxl9PVUkq5P_9DKJirxlBiRnPwWAskhaK1uH2U6JlWYLz4pS4QuctyISPlJx6KP12YSLpECZ4xqdzw5BckacSGrtaV63-Zrg51MC8GwwiWxN1cc7HN4DekaaKc5qBUZ5_bFGrc2CHj9wnI_nwt181t1d_8b_kkNHcVHO38v7YpQDSRkQFuZPXFD8KU-5l7tbXo33z7mvbQGmJvouQ0UWkhzsb8_7J68-qg54_IVaCBQCd0bjs3MuddqLHqgDz6oaCKM58qcgzETVKFdkhosMmn--eDAA6-tpbjzrnc0BOeLmaFt-mpByQI4dSDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fc4fcb346.mp4?token=qKt77yWDLJjuBurn3925SQk882b1n1CZ6W1XX86x5iyBO8q68LhyDEBWmT0W7EYWw6WQeHRrIJ8AEkq-7J4MeushR-dpu-wnYmefXHOWrULm1seeJcDGTs5dm-Zem3HM4n2UsUF0n-mb_PamWPsqXxnQKHtFbpixCaeExChDUNLyc88gi7hrWm1ffP0yWQt1_SDEIQdX7xIhmnBeiznk4cOd3zlkaXNhLlnC8EXBi2a-M0xd_dQNybvEBqBgOy_hyh3IoNGwG8fY9OWkH1ekAO4_KkPHTqBrQdgY9rCW_t4d9K-yLUxXptYgioK9upAwI3Qp7ISRd6Gf9rHh9jHxZwdkUbwOQJwkbI054jgK7adOPBTeSxl9PVUkq5P_9DKJirxlBiRnPwWAskhaK1uH2U6JlWYLz4pS4QuctyISPlJx6KP12YSLpECZ4xqdzw5BckacSGrtaV63-Zrg51MC8GwwiWxN1cc7HN4DekaaKc5qBUZ5_bFGrc2CHj9wnI_nwt181t1d_8b_kkNHcVHO38v7YpQDSRkQFuZPXFD8KU-5l7tbXo33z7mvbQGmJvouQ0UWkhzsb8_7J68-qg54_IVaCBQCd0bjs3MuddqLHqgDz6oaCKM58qcgzETVKFdkhosMmn--eDAA6-tpbjzrnc0BOeLmaFt-mpByQI4dSDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
🇪🇬
مدیر تیم‌ملی مصر تو هتل محل اقامت این تیم پیش از بازی امشب با استرالیا با یک مامور پلیس شدیدا درگیر شد که شانس آورد پلیس کوتاه اومد وگرنه حکم بازداشت صادر میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/97840" target="_blank">📅 10:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97839">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=IswfO0TsA0kzXMW8XIEQtDXaqkDUFd3AdRHen69kp56L6u9549Sjpx6sKkO0mDUFbvAPNHiQkwpNfTPS4OgDm08AA3VyrZ8MO4HbhWWFEoo8spupszEbj-MAIx1qjx6JETdajXYN1N_BBELS8ee0lRoWVev4ZgkyrX5UiIhOzNl6FOQPl8G3QkOt84CXVSOtDMie4at0aDR_6swIeUFXc8SWQYjoEicTymL3jJckJABgY6xan6-bZH0wS-zxvzO9A66SYiMFYMhQafT6Wjofi1j8lw6TTYclmPoklVlJKXYDKE_Mrmrz-VqRnkRlSowqQm7M1-pXTp_Rbo1Rhwq28g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=IswfO0TsA0kzXMW8XIEQtDXaqkDUFd3AdRHen69kp56L6u9549Sjpx6sKkO0mDUFbvAPNHiQkwpNfTPS4OgDm08AA3VyrZ8MO4HbhWWFEoo8spupszEbj-MAIx1qjx6JETdajXYN1N_BBELS8ee0lRoWVev4ZgkyrX5UiIhOzNl6FOQPl8G3QkOt84CXVSOtDMie4at0aDR_6swIeUFXc8SWQYjoEicTymL3jJckJABgY6xan6-bZH0wS-zxvzO9A66SYiMFYMhQafT6Wjofi1j8lw6TTYclmPoklVlJKXYDKE_Mrmrz-VqRnkRlSowqQm7M1-pXTp_Rbo1Rhwq28g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بامداد امروز شوت رونالدو به جایی برخورد کرد که شبکه سه مجبور به سانسور شد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97839" target="_blank">📅 10:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97838">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b98b01a092.mp4?token=grcPkrFbYsuZW0KfldLLasWKReKgFW67XFISS4KxhIR8T-4G70VPwq3q0n2WI05F24oUJQxqsosAiStbdi_MtEPXNJstma49XAyiIYeqW3qL8W34kOCkzSlCK1FQF9kzgiTbXHLCx-yL4i51PSEcu6jWTjUYFhV0V2VgNoHeAbbwVBiapAESCEs2keITPzNe7UVcFxG1WMJlokbqXXVGnS2E80IzfZ7geQpn1moZuA7HiD1RWTODi8rl03QJHUsMGDii2nzndNqxa52xA0Yk9PEuHpM0X8ZMDqZT3qspx7LjFnI7K1onqpr_yvM7pHbRIxL9c9kYHapJsD9Tpsn2GIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b98b01a092.mp4?token=grcPkrFbYsuZW0KfldLLasWKReKgFW67XFISS4KxhIR8T-4G70VPwq3q0n2WI05F24oUJQxqsosAiStbdi_MtEPXNJstma49XAyiIYeqW3qL8W34kOCkzSlCK1FQF9kzgiTbXHLCx-yL4i51PSEcu6jWTjUYFhV0V2VgNoHeAbbwVBiapAESCEs2keITPzNe7UVcFxG1WMJlokbqXXVGnS2E80IzfZ7geQpn1moZuA7HiD1RWTODi8rl03QJHUsMGDii2nzndNqxa52xA0Yk9PEuHpM0X8ZMDqZT3qspx7LjFnI7K1onqpr_yvM7pHbRIxL9c9kYHapJsD9Tpsn2GIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇭🇷
🇵🇹
جیمی‌جامپ بازی دیشب پرتغال و کرواسی که با سرعت نور داشت سمت رونالدو میرفت ولی در نهایت پلیس به سرعت بازداشتش کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97838" target="_blank">📅 09:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97837">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/949a0e76b7.mp4?token=HiUUpbmHhX2aeBolq_vuTynZAgwRXJQ7cjj-l1VN-XXKDcZfMTX1w7mYZj7mGGy3egrTqOGODPqC_h5zlHqhpoLUHnyDWoN9X2Oua-tOMP5z4DWbjs_uNaEvKvPvg5b73Xn4Gl9YmWbD7U_fj0DTAWcHzuhEgHnVYDGurIgIK4EW08ic0XEgIHYxkhWaOWFJa19qACIHJKRtn_jsWdegUfEO8Fk-1wlgGKKsJgpeEkGdZsCGfI8gN6Mk9ulQS1TBBnF2aIAlUGcRfVIYw32JbniuKqqR_15iML5IjJcObatDMrt5GGvbtVG5JCiT96Ndt2c09zl5lV3w5qdnjGSFIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/949a0e76b7.mp4?token=HiUUpbmHhX2aeBolq_vuTynZAgwRXJQ7cjj-l1VN-XXKDcZfMTX1w7mYZj7mGGy3egrTqOGODPqC_h5zlHqhpoLUHnyDWoN9X2Oua-tOMP5z4DWbjs_uNaEvKvPvg5b73Xn4Gl9YmWbD7U_fj0DTAWcHzuhEgHnVYDGurIgIK4EW08ic0XEgIHYxkhWaOWFJa19qACIHJKRtn_jsWdegUfEO8Fk-1wlgGKKsJgpeEkGdZsCGfI8gN6Mk9ulQS1TBBnF2aIAlUGcRfVIYw32JbniuKqqR_15iML5IjJcObatDMrt5GGvbtVG5JCiT96Ndt2c09zl5lV3w5qdnjGSFIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
🚨
🇸🇳
سکته‌هوادار سنگال بعد گل‌سوم مقابل بلژیک که در نهایت فوت شد و به دیار باقی رفت
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97837" target="_blank">📅 09:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97836">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇲🇦
تو اردوی مراکش یه شعبده‌باز آوردن جلو یاسین بونو که از لیوان آب مار می‌سازه و گلر مراکش میرینه به خودش
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97836" target="_blank">📅 09:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97835">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🤣
داستان جام‌جهانی و پارتنر بالای سی‌سال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97835" target="_blank">📅 09:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97834">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnUIYphoMWgMb8_VZtAHqGgmQ6fgGlUrRMMpX9Hw-HRNRHcXEnjz-JIu7g_R3wp07G2lIOMMbMznxXoRUTDA2MPHa223gq5g5VFoGABpxw3Z_eaGVtP35TUp89FhFhE9Xjf3E9kHF6hxQDDlNbJqfL0OixYX2FiFCosKWFqlxt-a2qDaGd2wiE-hv_WUZC2cYWevVbvTWsYVEkENWTpwAh2m9UyQ1fLq8OF-1N55a-F1pN_R3zdV_6_4DcIvedoZRk_AKQjCpD4KDzMQGsCEJKAhNkh4-cOqLJJ-7d0oD4C_aj2vF4c_F6n2Nzao1PnePB0CIj3XknuAtKD5xvGwQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
#فووووری
؛ رومانو: ناگلزمان از هدایت تیم‌ملی آلمان استعفا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97834" target="_blank">📅 08:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97833">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🏆
مسابقه الجزایر و سوئیس، آخرین مسابقه‌ای است که ساعت 06:30 صبح در جام جهانی برگزار شد.
❌
❌
در دور بعدی مسابقات، فقط دو مسابقه در ساعت 03:30 صبح برگزار خواهند شد: مکزیک در برابر انگلیس و آمریکا در برابر بلژیک.
بقیه مسابقات در زمان‌های مناسب برای خاورمیانه برگزار می‌شوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97833" target="_blank">📅 08:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97832">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HT44HTuzQ0WnqdaQfKuiHFyJcS17oItfo4AltqG12rYzdYMZu5VzOmlNsENCthEEAwoHmXzYqXp3AwCNwjwwRc4QwFXNGweTFzNN0OUd0r4LYKVTI-dLAA-49Qbkg5RIfAyyE7R_y4TfVt61ZGiHhRsWclGSzrhJldcgZ_KkAM_OG2s-YqoIEKTyvYDI_wIYCHdHv4FklI__xW8eHMh-u7KUqvilA4YsYzVWc4_F5_z9Tu6_ZFkShDMo0YNOa4p33bLZ2M8apVpmi4FNyaAx39IgAA2bo66m3x96pPJqqhvrkmObsyRiS2Wkd5dsfVdGOapbbXIZUxhw5FHQuj-zrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇩🇿
با شکست مقابل سوئیس، ریاض محرز ستاره الجزایر از بازی‌های ملی خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97832" target="_blank">📅 08:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97831">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ms9mGZBO8aLBwFAN-RszmV_5Adq-NBKvgk4DAbeCdh9G0zUD3ol5Izr1r-lFG1RLL5hcSmiLZL_PNMCPm0row0wLjQSGO9fuYpjFcOQr0fr1nFrx5QsmeuVjuziXlz6dw46CMSRfpbeOeSkaiCjKrNAMAxfqg0Da7JslUIx9vICQAHa2Wq62ORP9j_elWykmwFQ5UQULGfQpwKip6iGPcg49D5UFOxA53AfmHOwkr-oaREIXz-sFMyIOjT_GraKcmwg3TvFK3RkuZ5e-MS4uKb23IF5EaWcnj8YB6FEswZu3but3J618T6G3wNaj_F7wPqrxg7ZiHXSeOWFTJq4qtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
آخرین آپدیت نمودار مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97831" target="_blank">📅 08:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97830">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezpvZnt5-_Zh735LxE6bU3ePYTkeIXXnJqQ4UrjjykYjcHHhRE_-slrI5S5snl_PNuO7Dx6RtUlTYdn7WnbUkoCpuYN0AY39Iye-2dz8gAOGLpdn3w11u9CiFAL50qL58JhqARasjUKVHRbqjRXa7xwThzqOLo-qBh1jau99dFAvTXapOBITP0C5k2PD2_yf6xe9aZb3P_x2eM_vmw-twMvwotNO0-e-zeL7BdHzyY99Z1ZidhHvZq1arjxoo9RQaFoiJC1mon3ULcHURWn4eCo24fqvKLgPcISFJFWZrjDBNPI7HWY8LyG7kEx-UiyvLIA9nv0qIMIOWQazw6x-Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهاجم سوئیس چجوری اینو گل نکرد؟
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97830" target="_blank">📅 08:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97829">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">الجزایر این همه زور زد که گل بخوره به اسپانیا نخوره که اینجوری جلو سوئیس تگری بزنه؟</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97829" target="_blank">📅 07:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97828">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d083e293.mp4?token=Of5moO1GyR5PwRZB9fVZIpTqMvTC2irOvYBEwvQcEJQEG-g8fQJqHfSBjHuM1Ap7mc3AK4hG5mQX06YdBPP5IVC9iklf9joLea8obbG8JaTZ66zEfEJ7knX9xbUmzil7lytfcceH6BpQhCaHLB3BksuChvuZr5u41Fc_g1WX6We1_kCSnLrqInye9GeaY7Iy11ubCpNdBUEhjusqvKEnozkzMusNX74MXnxqmFDRNmXrmDrATlKy6W3xm8JeXncXS7CW63oGljgYKO1W2pjKAh7XD98H9uv1gymHvanxwvqJB2RRchFpUgN1YEg7F31NSlhsu7sON1ukBF-Q276PiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d083e293.mp4?token=Of5moO1GyR5PwRZB9fVZIpTqMvTC2irOvYBEwvQcEJQEG-g8fQJqHfSBjHuM1Ap7mc3AK4hG5mQX06YdBPP5IVC9iklf9joLea8obbG8JaTZ66zEfEJ7knX9xbUmzil7lytfcceH6BpQhCaHLB3BksuChvuZr5u41Fc_g1WX6We1_kCSnLrqInye9GeaY7Iy11ubCpNdBUEhjusqvKEnozkzMusNX74MXnxqmFDRNmXrmDrATlKy6W3xm8JeXncXS7CW63oGljgYKO1W2pjKAh7XD98H9uv1gymHvanxwvqJB2RRchFpUgN1YEg7F31NSlhsu7sON1ukBF-Q276PiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
گل دوم سوئیس به الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97828" target="_blank">📅 07:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97827">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شروع نشده سوئیس زد</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97827" target="_blank">📅 07:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97826">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گللللللل دوم سوئیس</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97826" target="_blank">📅 07:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97825">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نیمه دوم شروع شد</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97825" target="_blank">📅 07:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97824">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjcbDDClnQXY0cx0f6N-VUgnSDJsPTp4QJAlb36XJuC3Gr75WRI5kAmceBQF-3pYzSpxJzt50DqwpvBSJ6jfyWA1TzV_qXpGYJS3KEVfhhl3rHokd3zy6VP7KTSQl2DEANLc6by_ZY6Zc169RQLVHe17XdwHChVrtBV4rbHsZdSIX2F24kq9Cfx0I-eFoLbYuNOCSkUut4uMjhmPK4QPM6zNL61CdsfaY3AIo6KSSVJj4-ccNXBAIREeO2hJvyZRiZMEPHoDySS-U0WMPdwPPJV8W9RotBQOQLND42Z5mCeVHlNEidN-Cn8kzUCh8_jO2faOhEOMVqIGPGe4S7nLWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
یوهان مانزامبی هستن پدیده 20 ساله جدید جام جهانی:
⚽️
3 گل
👟
2 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/97824" target="_blank">📅 07:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97823">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edce6034a5.mp4?token=vwjZ-JHZqriv1riFtN0TWoK-yt82VsEZU86sy5j7IIhPC6V7r6lDuqmFbb57b4gfggeDJ4XXScfVJ8FTLroORrwsmDQLg78QalyOFA1w5ZuyiRa4bM195A7nUzy1DiXUrT1cxjcwUWYLb_J6ryvgoxGtHY267tmiMy7wJW6MbWknKNIRmBRN3NSYLoFt50GOJ08mjYKOUyEIP47wINhxXCJyjMVasIhGubVsDVKH7GtCmG50BfXV1pQCFzZT99ExDTNx0COgpWIVP221jMslGo5YDPJhR0a_GFYS4htv1H2b27tyAPee5svAd_iRyrZLQyrjnK_1x0DKU5__6iPkOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edce6034a5.mp4?token=vwjZ-JHZqriv1riFtN0TWoK-yt82VsEZU86sy5j7IIhPC6V7r6lDuqmFbb57b4gfggeDJ4XXScfVJ8FTLroORrwsmDQLg78QalyOFA1w5ZuyiRa4bM195A7nUzy1DiXUrT1cxjcwUWYLb_J6ryvgoxGtHY267tmiMy7wJW6MbWknKNIRmBRN3NSYLoFt50GOJ08mjYKOUyEIP47wINhxXCJyjMVasIhGubVsDVKH7GtCmG50BfXV1pQCFzZT99ExDTNx0COgpWIVP221jMslGo5YDPJhR0a_GFYS4htv1H2b27tyAPee5svAd_iRyrZLQyrjnK_1x0DKU5__6iPkOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل امبولو به الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97823" target="_blank">📅 06:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97822">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">امبولو</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97822" target="_blank">📅 06:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97820">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گللللللللللللللللللل سوئیس</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97820" target="_blank">📅 06:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97819">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بریم برا بازی الجزایر - سوئیس</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/97819" target="_blank">📅 06:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97818">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fa9c63f9f.mp4?token=KsmknDi9qQgi58vD3QQISFCWrzBUxfuUDVCaWpdSOdYGeCU1JzalbJuAptOHjZhBJbdrc353nUB5NmUdu5x4dev4uB5l3JVaFSwk8n0Q0ymuGFEYAKGiee98mKydT6B0Ts3PHbOE_MN5xfVyIfr7kzmBBymxRFcKcJM2FE4Q7G4pwDw8Va--Y6eAoMR9s-JRfEjQLbtiRa7hbtzMvpXosjx9YchbuLttBFLCp6_IcDxAlFv_jpTJffi3I790DY_j0oR09cyklVuqdggqjtVs23H9bg_Iszu1uvBOztN362t1L-IRcuuqnYGnu9zQ4Wtj9LTkxP1A13DX6sEg0NBvcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fa9c63f9f.mp4?token=KsmknDi9qQgi58vD3QQISFCWrzBUxfuUDVCaWpdSOdYGeCU1JzalbJuAptOHjZhBJbdrc353nUB5NmUdu5x4dev4uB5l3JVaFSwk8n0Q0ymuGFEYAKGiee98mKydT6B0Ts3PHbOE_MN5xfVyIfr7kzmBBymxRFcKcJM2FE4Q7G4pwDw8Va--Y6eAoMR9s-JRfEjQLbtiRa7hbtzMvpXosjx9YchbuLttBFLCp6_IcDxAlFv_jpTJffi3I790DY_j0oR09cyklVuqdggqjtVs23H9bg_Iszu1uvBOztN362t1L-IRcuuqnYGnu9zQ4Wtj9LTkxP1A13DX6sEg0NBvcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زیدی ژائو نوس رو کاری ندارم ولی قطعا ترکیب استاد باقری و علی یاسینی یکی از دلایل صعود پرتغال به مرحله بعد بود
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97818" target="_blank">📅 06:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97817">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpBl61VXl52all_8jkCiJGkJyA9ztcKSMBLaG0vUeyzTX16WQPY8t64TcaNU8VD1F9dHI9sIXNIrwhCbM9bmLr6otftHJ7-OiWr6shQyMZ5_qXy7XRRMjkUh905J8aSaIkegptLX4AfxMxKL2c41lQ4qZcoVjO5e7_1lNnYzJsWFaI_2ubduRcjoOJ_BtCl5UlRT7DqYGBeaPcM-T2Ka4XtqSqUtXDFiiWTucmDQfLQYPYpI1BVYzV2rU4VwK16ktVCM5n-exhs0yWUQG4gNe-tM-wPlBZg3B7iqgSHmFo5kGJKVLDK5clFe_Obj37e9mbjRLlkxZB7IMx_qQHjAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"حواست باشه بعد بازی کامنتای اینستات رو ببندی"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/97817" target="_blank">📅 06:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97814">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMzx4ne8s92BFzy8KcCWDa2SI3E0GWyx6kt8BFY_0c7__U7rhoEIJ_swWa-AGyQH7pwVNl8rzK4J9iQzAHZHqVg8BMQHWUPdU-NF0UiTv2pA-AiUiA0rFBuCrLLifsaXC5fJ56Xp-gpLfRDvmZOYxThprjy-CaZsybgRywP7BmceyKg-gCesHWBI1QuFme0QbMo4RPaMdcWH5d5ZXXU7X0EMDG1Svsw8_SminSQQwVoSCxwvbr8us_G0W_FNIr-gYuvEh5QCYcPA3m3IsBtR-KHLRcuttqR-29DXC04ww4geqVmEsJmTi-MUcIK-mDNCyQNvw7IU3__stEuRLuvoZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JjhV2ItSD6y0OKTPZZB_i_SxkinPtgEpc5SlrYkbJVOF_yPd1Vfb3o9X8jIDOhRiIQOyLRbZKD4WbmT9sjlyOYeggoEnDtUoQxs36VREO0dFP7tx4e14FEPRCS7QtKWpQPL1enlG1iDd0IjQEhxa1FhgtoB_niPWsBL_oXmavcK-NPwYR0sGkHCICfqj2wFAvxEc4bZg_ZwUfqsADHYtZHuiIQWvXKSU51j0xrVAg8WNlfGOwYPjyyCr7goharcsbRkksXjKeS_UusZ8iUwT2W-TM4fGS-HQYEZEMeUIkDsuwfaTZ1XKulGZlCCjAICoYvtlrPk5go9WkDo2ESmqcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fOq42ZdqCi3FhaCcf8m6L22Z-GRdN6SYkDHU3S6dYYRFaxw7ryGEwZMJhWs0hvx1hJw0GOegoNJwZLuhL0F7yFsW65ihI1FUWTcJ6WypYps7r8Tq6FBSWqhGNBLMBhw5yMw_oAhfaExyPndPlaE4Cfc0Xa2SVM7vYcCKUl1d9Cl_0oh8ZnO2dIFWU3THrqlZjwRUAPZayZFpaIB4EZIEgZhY_K1TuydwWMVZs-mlDUEZhLGb_O6vcQcxMWEQx1A8AYBtoMt-TZdx0E5MBA7If4cpuXnDgwDbm2VY09cPGNhTDnNfTjUMcO3xHUL83ZE6mg7-H5p9iWPDUXGzmcB27w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
از دلایل صعود پرتغال در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97814" target="_blank">📅 05:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97813">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZsCUbXFgBZ2rsLwsN0NEQwjMj6YVcqZ9NSbW0wrPnE_tN9eMWY5wilRegcfAG6E9lvh8tTRvHWXhUHfmt8ZT7LSFgf8t3KKG1nAfms0oOywwl0pWhDZhI5SeIznRMZgoYJCR-UK6Ze0nRLDj2vBxxOV7GEKdEwe5mwkII0YQV3adHsFOqBJ9ucHJSVG_sPhbXFYnrsj2jVz8wjAg0iYEHjj7qbvVaL-4OfKJExUN_cr_JSZWhtrvJMNUvm1Gk-x4rOX-uOs3ODY-DLrE2aY3-oGIUZPc9iDR6nW8M9vChPnVH8MaKv0oNIbDIbG-zCV8aTq7nkxZk2C00hMR7zf-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مارتینز کسمغز امشب هم با هزارتا مکافات و کسکشی تونست ببره ولی در نهایت این سبک بازی محکوم به شکست مقابل تیم‌های قدرتمند تر از جمله اسپانیا و فرانسه و حتی مراکش خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97813" target="_blank">📅 05:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97812">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTEZ7ZqH-NKDHUI1GFJvkg5HT9PL-El0DpcbWU-iZPtWgs6Ry0rHY_nwz-Qm-7K65OxrnOzMm0zzZSgBQq-gBcX6KmpF0uzQybl9x_imRl4GF1Y02HJLH4GdM3R9PNf8YSB2aIHdmvtj0kTbJ7Ns9pqBjxlVvamc_CYQmvVd13lsH1A53FlO389AxJ7cuMu8jidQwikmkqQ2T3kcvncvMxC3RgENyawvZ9ljnFM4WeUdoASr4seKN2C39qcAsl9rf-NBBlM6t3ejIgds7It79LwIGhNvPi_HJ-g1-lm01_1907MT5O7cHUU91BQQrDCIRUIgpFhht0KhxoIzbli5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
قیافه لیائو قبل از پاس گلش به راموس:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97812" target="_blank">📅 05:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97811">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltOEwaBCCCQnx_uQFJDXp83MkZc7o1jHquKMS89o8J_BEgAuW14shYSGflogKYo8Q-nuZFG6-cZkeUqnMGDej3IfIDokSmijJCT5Nymwvh2P8T3n4LXP8QaumVR1Q2Z6bNQVvmooLbDmUr2PJfiqZ7mHFGR1OEhSVbkoS-6lk08vWuVbm7O6xwvVcL7-WF61tRI3mrUapnFzLSZUBJJF0gBGcCaEzJXUn2Y3VWZoZYxEew3U0y1khqxAlDSgNCIRy4Joq3slnZFI1UENU3JYSFlMjkAglmtNyK-IfDF-uBvKruwO380xh3hrru3q52ytDDOdDLVGoMZeCfWkFUu4ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد برونو فرناندز در مقابل کرواسی:
❌
0 گل
❌
0 پاس گل
❌
0 خلق موقعیت
❌
از دست دادن 2 فرصت مسلم گلزنی
❌
0 دریبل موفق
❌
10 بار از دست دادن توپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97811" target="_blank">📅 05:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97810">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCtR85y1taGb2absY64uT4Fr2IQK5XYEzpX5uWxBkL-ZgO7iG53iPGgYKLX2ch5tE1Fx_gQrUain-BEI5jk_ISvLvAaWKO5jS667FzPlajamAAzthCo-nVyeNmCtJd1ZMQ_iKT1T7ucwOC9cb3SxLPOfaJrCaLwLAQJ_KiB7aszqaq8VvrfFa_99kCkn4JJkMuLWpSDQR8Z3e0qQneZHaohb0cPMv6hiclm2OeiulnyXjBnX1O_6_d4GYdy_5Z02bBzvDOpi-qogTGYNFmTYBDXmyhyyx9CBw5iXNV_KqZ38NqStCVNjycsL-W9yrJMgHuu9CBiVjBezYl6FYL_iew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
| کریستیانو رونالدو مسن‌ترین بازیکنی است که در مراحل حذفی جام جهانی گلزنی کرده است.
🔴
کریستیانو رونالدو: ۴۱ سال و ۱۴۷ روز
🔴
په‌په: ۳۹ سال و ۲۸۳ روز
🔴
روژه میلا: ۳۸ سال و ۳۴ روز
🔴
گونار گرن: ۳۷ سال و ۲۳۶ روز
🔴
ایوان پریشیچ: ۳۷ سال و ۱۵۰ روز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97810" target="_blank">📅 05:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97809">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">از اون عکسا که دوس دارید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97809" target="_blank">📅 05:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97808">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxqsXP3aFPYm_NjsMJ_ZaYiXgxdvNSO_xiwmDyv28ZHi06-GXKtQguHvR6iVIdpaA_beX3twW_gddXQkk605U6Hz8QwSVhugRs-wBsaw-ct49g3_DpHKTEp0TeN3IgLj0zJebgARa9sV5VzHLl9_-56rgRPYhGWIhoCl7NOecxcN0_HLXjT0uuARrzTa09wZSin3qT94mFBCxrSnbSAJKAfHMOCIDFDpeU6Mo_OQuZDbuSC7S3ns2EkubvembJfpG2xGt3F7Bpci_Yt4KZVwm1sTU0cAWnxv8UcUy0EaRUntgqSfSDT2Gl_F74fGuEkSeIR47_4J3zu1zPWsunYVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خواهر رونالدو: رونالدو بعد جام جهانی از تیم ملی پرتغال خداحافظی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/97808" target="_blank">📅 05:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97807">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e979b7d1cc.mp4?token=r7eG5jhA-_EJIy3rxRSmnkCYIAEEwWAujJfx7oqnCIhC1pJRbXiMHzIlyBCvXCdqbeI12YNFoTQxCK1xmd6Pqf8yYcjE6YqNLlAhFlkVsWwR6LwG2-w-QLV1-5BZtcWbMdqoEOAfC02eOCeoHjyGHOIyYfveJ8g0A--bg4rVO1kmDlm0EnHv39Dxbs7YqD1a-XoTNM0yVR0gUqzmPLvuaEsSaGcMM27b7M6NV4AMevUNCDdtfkUArwqO6ATW6-5vDPhr--J5fOkSwob9W7EWw-2YnxE60sHpFVKqheJPO23WmVBE8D7hsLYamdSgdhoFTkOmGXLVZyikmGnjBXjmXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e979b7d1cc.mp4?token=r7eG5jhA-_EJIy3rxRSmnkCYIAEEwWAujJfx7oqnCIhC1pJRbXiMHzIlyBCvXCdqbeI12YNFoTQxCK1xmd6Pqf8yYcjE6YqNLlAhFlkVsWwR6LwG2-w-QLV1-5BZtcWbMdqoEOAfC02eOCeoHjyGHOIyYfveJ8g0A--bg4rVO1kmDlm0EnHv39Dxbs7YqD1a-XoTNM0yVR0gUqzmPLvuaEsSaGcMM27b7M6NV4AMevUNCDdtfkUArwqO6ATW6-5vDPhr--J5fOkSwob9W7EWw-2YnxE60sHpFVKqheJPO23WmVBE8D7hsLYamdSgdhoFTkOmGXLVZyikmGnjBXjmXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همینجا که دریک رو صعود کرواسی بت زد دیگه آخر داستان مشخص بود:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97807" target="_blank">📅 05:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97806">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏
🚨
🎙️
اسطوره کریستیانو
🇵🇹
:
🇧🇷
‏همیشه احساس خاصی دارم وقتی درباره برزیل صحبت می‌کنم. ‏من خانواده‌ای در برزیل دارم و مردم برزیل را خیلی دوست دارم. ‏چون آن‌ها همیشه در طول سال‌های حرفه‌ام از من حمایت کرده‌اند. ‏می‌خواهم به همه آن‌ها بوسه بفرستم
😘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97806" target="_blank">📅 05:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97805">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
📊
🚨
🇵🇹
#فکت؛ گونزالو راموس به طور متوسط هر 47 دقیقه یک گل به ثمر می‌رساند. او 4 گل در 187 دقیقه بازی در جام جهانی به ثمر رسانده است و این بهترین آمار گلزنی تاریخ پرتغال در این مسابقات است.
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97805" target="_blank">📅 05:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97804">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5L29lqBffXoRqfOhSQv3SXSWiSiLBOulnz93lx-kb0CcxdhFDOpcCa__4Wd7YzySwt1nemtoKFpy0xhc1odBjwbXaaPtsHnnhDglKQwErdtIAsHK8eaIwMeFFty4www8WaJbxFf40Kbv1gY3iNue4Mnb737PD8GX51EbCMvSKj6FAG9BitI2EKaOniTW5EfI_Jw7a7G_e_0Mk1gE0PCPIEA0KPQEZRH6Jcmv7Q24iq_NLB6tZ0Uk3sbF4gveUqUawrE1VXS7d33rKE1UaZX0UYAXnDtDus8r_1SwkdSKbiVZsLf7PpcAKsj3771YlPVRE9xDwA1rsQAumj-mtdjxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇿
🇨🇭
ترکیب رسمی الجزایر و سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/97804" target="_blank">📅 05:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97803">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0YPBYX1FonTxNTSXNfdpitKVE8CteIsj20bDJXDd99QYpTn4ZsgNic283REzRPzjI4ZqrkMKu5jyomKaJjcD6uDNIzAyLgGICZns7CIRmjliHOrmNIGyRdzhmApnM5mdH1Mi714JaqlvgnAyxb5Zq7HlRA97ZUc0VyPhrX_MgUcz26JCu1GN1usL4wkj1C841Gs8BHLGXDRYXyx8ptY_BEltFS2a8zQO1ylEAkV_I4YOJ1bGUUlujeWUhX4Y7OJSxPOhAN2aI4c4zXJqrHxrBzk8Tn1eR8IPXiAbf-AL-x83L4LfvmJPRaDm9gjdU-UAQO0ZSGNLCdtCEly8XWPEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🎙️
اسطوره کریستیانو
🇵🇹
:
🇧🇷
‏همیشه احساس خاصی دارم وقتی درباره برزیل صحبت می‌کنم. ‏من خانواده‌ای در برزیل دارم و مردم برزیل را خیلی دوست دارم. ‏چون آن‌ها همیشه در طول سال‌های حرفه‌ام از من حمایت کرده‌اند. ‏می‌خواهم به همه آن‌ها بوسه بفرستم
😘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97803" target="_blank">📅 05:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97802">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui1iGj0fu9m_jS4V6HzARphISD2vs2AdIKA0NW64h3xJzXFVDucW7D1dN8tLBkr_EgvPHtPfVY7qk2bNXqonA3WcMy-2hQ8aaQkVs8m7x8RX0FcDhy0wMc_xfhxeIGJf7mvw3KclIpYeThKOEsMcP3iTHTSmqpCjdEFsySH9rZh9kW3A8jVMyDGODbw0q6IZcGiIAJN4fVZxO8GUME8o5Gr41l8_aU8pk7Mw8x9I8CN8grnIm_jXuo5UFRO3icd2u-WXSd7ZXXQV3D2dukGnVSw74sgFAM7Pz70cN-pYXXpPr0VPfYLx7jQw3Cblng8jfccRuHgAXRkF3_FxjsJA0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🚨
🇵🇹
#فکت
؛
گونزالو راموس به طور متوسط هر 47 دقیقه یک گل به ثمر می‌رساند. او 4 گل در 187 دقیقه بازی در جام جهانی به ثمر رسانده است و این بهترین آمار گلزنی تاریخ پرتغال در این مسابقات است.
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97802" target="_blank">📅 05:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97801">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hz9sF7VhN7YxpNU7e05hUDHmp5MMmOlkCtWvWAvmnJiL28iEO_j2oxkaR4PJ3nEDab7JcZIuPOohdLZK8dmaxvvxxXyMnH3h4QsXQdwbYqS32L-Dlzv7kfj4gPRplcJaX64d4SRvIM-HJFMdtqRRtilXT6gBBM-DDbP39ypxX2f-cFBS4hRYMoZMW7JqqZzGWgVRaKsRiw6iw-6kf_h6oeYs_9nbBL0f7CNxgKkoS0baUSGtrm094lQ0c5KdxU6qy59-91giIWrK9OWrdHHpH5PcE0Lz0-ECH21msDMUXxP7b64xaLXh6Q-i-cmoN4DP24NPogvPV9m-bVWPujZhgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشک های کریستیانو رونالدو بعد دیدن تصاویری از ژوتا
♟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97801" target="_blank">📅 05:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97800">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👀
آخرین تقابل اسپانیا
🆚
پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97800" target="_blank">📅 05:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97797">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PElYiG7YAxl_v9Y8hg2gueMdnKOnFWYMPdYZ4JlIdkQ_OUimrK8b5E6aXpDpAEHYeBdVuF-F0tnI62Moan91V2XOeBywL-vhLr4-TYqlwMv1DHKxKgGyIDnb4hkpWJDdF3eRhakbsuqqfPJEwUvtPkBgS1c36E-hslLsA7DyLuuDF3nhmpxRfEXTAdh-zYJ6EdeaVzIxOstuo9_wFxiKCzd_lnWC_V2LgOy4qeHjwUcFNUyiUQ8TJh9cBoL4RbO0T69eSSqoWX1bv0Vu2thMrQJ4F61Xhi6xcpXCHP_C_AOwFG0yKdZVW46OXXfgv_Lo6A0j2PSADU373ZP0GmTWPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dmnTeTp6YG46TpMg3Hejat8JTB8zPejJM5zpHobeSYFaQV5Gf_hTkom9rJRowIALL_6eYuhshLvlfRGsiZZqdER_5eFIcyD9oZnD8YD5u06HAyccR_do8JQw__P6TwwiBymgCQde8cveiUe_ohUkdnTVAIkMIdoLdFHq14p2qV7h8n7dAt_V3elle9Zi3djg_PlzoNTP0D3Y9xmzkH9U6HJf6BY2A4CJ1TWLf3oL-5iS3rtIp9ORmEwUymlQoFNQ-foZDgJKhwj089MxqpLs84X1plsLIo5tBk43Q2aLdtog-dmn0fM9tKm0gcCf4idXD_MnrCJnckWUGb1XTt2PLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به افتخار دیگو ژوتا.
🇵🇹
🇵🇹
🇵🇹
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/97797" target="_blank">📅 05:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97795">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbyx3VRDowFEN2q-OInvD599cDISF370I44CeSxkDXZOQfndXYgGks3v-P2aC7Ll2oSki03UoevxCjxS_7P0S_XLACVVGIkCKd0lpPQ2j_CIj2QWQsFk8hdBdQ33Bsd86QpDCcr57GEMmbGVDJ_qn4JTnVQXXrtolj35_QCC9QLdugTU1o1IsT-1jXQwNbdBcp5kTQv1S8u3NCKlMxDpVNSQY51HYA3HQFuLO5jMx_yMBXW3I_o1lU0qj4fiOk_KfZ7YalsyzKoeIQD2Linf9q4Ux1mamRN05SPeFBk4uKeZYDcboz65bceL1n6xpiRqHIA2vuOZl47sOXws2Oj2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اون عکسا که دوس دارید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97795" target="_blank">📅 05:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97793">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZkQG6zbhkqB6-DpYcyvMNnbUYku4rjGn2sJc3R1vZCRu-RHaqoFze18ypPKVaKl65n8f24IXBU72zktJfWYF5fbpJ6tYg_yBcx_DbNEhsByC3w7QgCuEuvw0VNwSkdQ3xTSX_HVEkBplDX9zaus-K5dHBGEkDWj2I-qt9qfRKulqjyCA0cDF60SX3ilUNZIXDStfzq0R_o0WlVkHyATLGvjHVZQ6ov5Oq9mBIi8854BIpFO6wZkUi-WSyNijEJsigtHurs4tsTn8pzj8j_vjRI2FZEOl80-DGa70j7zt34fspkXOH6Zh4dwjixKZo_BgZ0tso4PuGgp-GH5Qxfjf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tK9jNFE66pKmwSPwigmtfCGQq9gAjLrVZZASLT41f5R_13OuD-ziyT5LbqgRSe_vNrmDh18bkLPH_3Fru8GIKabzbS0S5LjZBAxd5O-adTj_q2TutCDQWINPG1C9kgmj6PI8h3qI4n2PP3ISqjfSh_CnrhWG7mrs8YrPhuhvPyIBSYXk6DDb03uO5fVg18I2Rnvxxtn56FY4KCUPe3ITBAaYs9_NSk1bBpvPYL9ZXHJ8B1zjfQtaCqqEezy2P4xWVMLErXTY8S5NbMMiwBLAP5KonDYHcXHsvGMt6WgeuKTeb7XMYKgZ5ttU3VEbJ9TFBGT3Xx7B_J9-JHcB1VDHWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تقابل دوباره و این بار در جام جهانی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97793" target="_blank">📅 05:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97791">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKCi4aA3eBmP3SuCaqwKQqlLu_rN7NILCkTSMXK9gOqzOWJ8dQels9eEXREPmZ2qXEvYMt9Ts-VBrYBYWgn8Tc4wwittAYykmpgfWLAfkxW4OlQPCI7BdL357WqeabIA49-LrbX0vdNT4xLhrNOXKwWjc2RpRusHpQnFlZqls1ulF_0FcaGf6-jRfwu6dqV2s5e9hd9CE_loH4fIcECI_GYWqik6_r93oukOKwX2R7Db2YgbCtISpHbe2fLsV2S84yWwA63rVw5o9HidSiPnm7JaEVgjr3UB4crgi7wY-NXaJ64KwBIWusZ7te-R9rY88wuQrghZdGdCFsECSANrww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
آخرین تقابل اسپانیا
🆚
پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97791" target="_blank">📅 04:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97790">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y9uDNepAmw87MBz-3G9Ds9OKAMenovulxIsWJDYNoWT9WiDQ03F6k0nWqFmjkSaGoCs4C17djNtCtAOvTDpFdVoeMvNjp8PObP-ADPzC4hZos5dpkdiL79bSL4TDHHa1aPL0a1UAVqEB2yDTGMkoGDbV9gmNHLVh8hQo1LJQS89_2g_D_LbKp9UVjVi3saOQkhvg3Nv94AYsT7qS2fp7vagCADvDE3An0gp1ZAFVRyXCF048t_VhBdiZGWkWZ81o88sDWMHegIX_7bKgldy19DtVgu-PrQUmOoQoe5d3Tz63GcmS5yJw3_DtDQwro8RjYl1Z02zpTY3XrKqCViZMyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مارتینز کسمغز امشب هم با هزارتا مکافات و کسکشی تونست ببره ولی در نهایت این سبک بازی محکوم به شکست مقابل تیم‌های قدرتمند تر از جمله اسپانیا و فرانسه و حتی مراکش خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97790" target="_blank">📅 04:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97789">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2SV62Lprf3MsihLp6VYTBf3haaIqBnpcIjNINWx4_zHHF26fkYvWoDjE-P78Yn_wZ7kMe_AfsGmyfAN8dcJalWoli6RRGCBh7z-8I3Zzfvh1C9kH9BL5ATvKrtu0oIsj6tk4F721boIze9J8WFBVozw32qmUukXnzYZzzTTEYlUM-mkTpF2x4T0tlVuKdZEvMywZPcHScJNSB-yg0bVGUd7tRflO8ANw3qMf1j-gcqRFF6WlGbrsrx16EZerjgDMOPUTPol9MzdE_pdz_1uSep7RkXKwI_MOzw8AbrnXQUMMwGeIug44DoLgskZzkpvJJnpxL5bIbLQOqSXxJIdZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇵🇹
• کریستیانو، اسطوره فوتبال، اولین بازیکنی در تاریخ شد که در مجموع مسابقات جام جهانی و یورو، 25 گل یا بیشتر به ثمر رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97789" target="_blank">📅 04:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97788">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWh8ieVnQQhD6nRwqbVEXRJ9KUE4xwJ7twfzpXiufXboK25zVjbENl6d5oatZ9d2gmPWBEZPlIzYMiaxdHpNKAUTsZTWVuoiRwP_46ArBiVv1n9kYgH-BUpYNuuBEawvRuTcrfRYrcEDnXzEMdRT61k8PnDVSgaHTM_HXIa7-qoXS6YlEaYfguxgGuPiQxcLNHQ9xn0GyjN6fwR8CWpSR5IC21rXsqdHP6XwzU8732-6X2eql9iB7n_-P6szDzoe9FXxnINHEXif55Yy4YoHJCwIyT9iUcCBQfF4EvDExh647nv8XH5NEB5FHKNf9XFclgD6wI2N0dAM9BUHYiqjfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🇵🇹
پرتغال
🆚
اسپانیا
🇪🇸
🗓
دوشنبه 15 تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97788" target="_blank">📅 04:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97787">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/li1jy8Ypt5GglHuHu7EPV5v70BJFqK8O6wBpdHMf4ScMaSq1LKwMyuZ0zsRt3615kTXVFwaCKt4nbEkKGpW3secZj64RsXziD-16jOUDyzpHpWl8v3kxJgYA6-qWre7QEpTyGgVTusRrs9qU1HD8eW1KOH9qzCnOhQqANOac48-Byu7JUIeyfQJ3n8lZWf7kc57gBctYILr-gxs3x4VzdhQoVsmtQ9B4pq-g0yrsiUDsdW2bCh5Tgw9EngNGc82HxFHGFVLDQj9MIkd08zspnEQLZR3anr7fK54mBIQ3lbVZqGK_fI1yzQOKs79T8NsM-08-HMFB4A3hQ3B0RvRwaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ مهاجم جدید میلان نسخه مودریچ و دوران حضورش در جام‌جهانی را پیچید؛ فرشته نجات پرتغالی‌ها بازهم گونزالو راموس شد
🇵🇹
پرتغال
😀
😃
کرواسی
🇭🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97787" target="_blank">📅 04:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97786">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqwR9o31U6uWX0Nhcqq1dFvKHmV8Uhs5ax8iQ2I0tubaheZvp41jdD0MWH9FgaeaVt5-47IKbDEWy_-6ETIocsTY4PaaeKduPxcgAUI7DfZmoRR73JQOmrlslM8WcjPU0Bnytj1AMvSD9g_8OoG_MprwC-Qq9wQpElWVeo04Fre_xFSEbLv9057uJrvQjR9OVlfNo4M4XtIcmPpPJWOWCnvZ6G8PxlcZNi9-Eq3qQRrI-QhSiaKT3INILSI-HI_Cz6yMKnam8MuWdIo0bSQUD5OuerqI_8DZNtApW8NFQZBIYKM-C87_5FOomV_zjJj7DGAPYjwkVexTb4-8kNNZzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار مرحله حذفی جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97786" target="_blank">📅 04:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97785">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAS2XVSdqQ-6wXPTX_AcURP7xAeL3SJUbVTbhRi5D4JVQPz1kvgEoRFpXBoxqGOQnRDWUPOAevku7F0BbbOZavSVTjkgtuwwM5rmo0XVoYKeyp-GUjnpFh9xrRQjY3eGwYHi2Yz_QgeOwhG009hZvhfXJ3GhGvgNl8VAyrTQMM20SkRvmsqFw8JJ_e94xP4f07LpxeWpMMJX1qQw5CJ3q5dLzg7ooh_aHyfnObLKLemYoJO9Gf8CDcLZ8FdJpWH-QUQv6Iv_Mjop6peLO-sE8OEBPPwouTVUkpCY3aqmCbYZMX2kAb4rCIFV7Om5t6TMq-VWChZWoudrgMLIvmXBUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ مهاجم جدید میلان نسخه مودریچ و دوران حضورش در جام‌جهانی را پیچید؛ فرشته نجات پرتغالی‌ها بازهم گونزالو راموس شد
🇵🇹
پرتغال
😀
😃
کرواسی
🇭🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97785" target="_blank">📅 04:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97784">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHFseliwTbn_fsSq_fE6exdC5GgU8-ndg8dyhwuExsfIZXzvCc2KgWe1SXRCA1xFSCEEGJj4q8WuB4Ihdu-cQWVQAk4hDTTcS8vtcBaDrPGVlHmLlRol_BgYJk9LK5F_nBoE7qFPEqvgAaCqIREULX2x0grSp-nLuwx2sbCfTnaS1hpfGnobsXfJdxcTggvPNI6NOpRT8F20yX8HBtF9BBnVI-H2Td63rfL7Pk3UogL7Udv8RPp-MLIr7t90xLS9sD_eDGQmhZFq4pGTSOh1AV3X8iEmvmxy5br3g1iPv7jXTVeNLFlL9HFJr-HeDwYkLa3r3XCY3tnWk8wQcNLQmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ مهاجم جدید میلان نسخه مودریچ و دوران حضورش در جام‌جهانی را پیچید؛ فرشته نجات پرتغالی‌ها بازهم گونزالو راموس شد
🇵🇹
پرتغال
😀
😃
کرواسی
🇭🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97784" target="_blank">📅 04:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97783">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تبانی اصلی اییییینه
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/97783" target="_blank">📅 04:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97782">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تبانی اصلی اییییینه
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97782" target="_blank">📅 04:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97781">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCP6_MA2iEOHvN8-HjVOXS1vltmda3UGtXCn4koCRFmOaD8bmzYjcGU7ttysSgW6G10-9ldlf0fosvC0vtlo8uj6gRw52vfund0mvohTCWLTRUUVR8C0Q4QI3pQcJCPo9Q9n5K6ij6KcznV9VD6wg9-jJDlPIwfCsOCc1XQG6X5FZloJ8hhPp_SCg3qsjaCZsgiITZeQyOsNGlWxa0DmbOLoB6DmZANf-qwEeFN_Afifp6H5dPqhsPTjmQ56OHP_ChX_FA5ekiaTbKdjhvs51F2gXOmUvEwJ7njeEx83kNxBbb62SEFhfSu8gJjz6-vVIjYxfQTbapjv1AQpVcoLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ مهاجم جدید میلان نسخه مودریچ و دوران حضورش در جام‌جهانی را پیچید؛ فرشته نجات پرتغالی‌ها بازهم گونزالو راموس شد
🇵🇹
پرتغال
😀
😃
کرواسی
🇭🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/97781" target="_blank">📅 04:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97780">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2UJuVruQuslNGoyp6_ois-7phoxUmiR8vTbdV714V8mIEvk7mqdFgwIzpdOS7A_TSL5QCoNMtangXJlaZVedNU7cObdbPCPL6trXjtucozEiel_m-9QHBOT0-1qAnVBBnGjdUwMfH22N8dwNHEunhHLQYVKDWcKb4-aNDU5qu0KY87NZY8JMhiJvvTm942Z4f1h5XIZogQx3AanPiInoUlzBctxYy3Y7KGiWHXhpFXNcOVZib6UsUBvUSfGTM7j7Q_xCdTRdIvbdN7Ig2DRqqDbpA076ux6Q6wR8qGuv0Irn5cfhRdgMgoqYX96L-ZF6UcL4T90dYwC-6wNF6NbEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درد دل با کس نگفتم درد من گفتن نداشت
خنده بر لب میزنم، هرچند خندیدن نداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97780" target="_blank">📅 04:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97779">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رونالدو باز خندید
🤣
🤣</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97779" target="_blank">📅 04:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97778">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">از کووووون آوردددددد
😐
😐
😐</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/97778" target="_blank">📅 04:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97777">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گل ردددددد شددددددد</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97777" target="_blank">📅 04:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97776">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رفت خودش ببینه</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97776" target="_blank">📅 04:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97775">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOpNxRBkY6h5QHhN0rGyt956ITfdgbaiXOzW4IT6KsN8PIi9bmXNrj3PucYCfZxfNuzyXeHAcbXUA_X-2u00-7erlOT-X_sJ1L_28LXFYpRGlH0nW8hH00vtlMUK7vFkO3RuVJmlNb5TRt_j_WzX8EeJhJYu5C4_RwILGVF-v_9vRcjDUenHpZTbKg5Bq3WOh9EOjLEh_EuckOUSLbxdOEF2NHX9OG1kNwLHkxpHXii_GV-lhVcMOdgNcswPTIfRCFSp7SsKL9YbVbnIknNzV4goAjY3QIfagGhCgn7Pe5OOYSkQTlG3NruJYQE84fu3OPmmSKklGWWqcYGfBODi-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97775" target="_blank">📅 04:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97774">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">صحنه رفته واررررر</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/97774" target="_blank">📅 04:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97773">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رونالدو ریده به خودش کلش کیریه</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97773" target="_blank">📅 04:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97772">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">صحنه رفته وار</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97772" target="_blank">📅 04:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97771">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYAWToL-C011is3yb8wBNLdIKPnNphTuQhGaLVZm8ISEok5YfcP-u4b27IQ5F1SanuoL5qEkcaGY3XBAu6mAwxwp02_UyFDDO7LV73miXNMukozmuJ_KZrfwVhYK7kx7DxyvZnzVYECHU4YzPSlZDrzcRFDXB9lyIaXy6DjGuLMxmC2D0QLmnsrYig7uQOtty0B64k8rZKDdRcbKgXhuoQ2Xj6G5BGVbfyh4glWxVIpZt309h2jv9PfItcW4o_X4-KRu-jW8aU5G__V6ne_U-tndlOmsxve5nxafUm5ZnPXcQEhC3U436LByrHTcM7JuFBBfEKpCK9ZAv2Mnj6vHpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه رونالدو رو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97771" target="_blank">📅 04:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97770">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">احتمال آفسایدددددد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97770" target="_blank">📅 04:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97769">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وای وای وای چه بازی شددددددد
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/97769" target="_blank">📅 04:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97768">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">چیه این فوتبال</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97768" target="_blank">📅 04:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97767">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یا خدااااااا
😐
😐</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97767" target="_blank">📅 04:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97766">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کرواااااااسیییی
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97766" target="_blank">📅 04:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97765">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مساویووووووو زدددددددد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97765" target="_blank">📅 04:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97764">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گلگلگگلگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97764" target="_blank">📅 04:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97761">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/06d72aaac6.mp4?token=JFdcnSXGESsXCgDPm2zi-wAA3mY61ARXbhyY8-Ci2d5V-0z0LLfT7QfYOoF5bmnofTEjVGgRMm6tA0XqL1kS0q9DernmbePgZuz1ZVUEVJ53kZUyn5mv5UUUbepYvY6gbgHKw-O_27ACsStahJRpyPsGB4kJ79wYLJwlTtHnpafe3cIaNLHqMl8NZ8y-lOy4zsXX8IH-jXnU3we4km7wNthXVufEHbbKo2uryJEoHk_Tdpl9LLpEcTMl6ZND6EE7_7aUmSD2KVkCacqbv6aYz0xcM1agTlG49n0tf1610qlbcpVcE3OsvPC8qTGNM1s1P1zE6XLxX29-3vKJRjmpZIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/06d72aaac6.mp4?token=JFdcnSXGESsXCgDPm2zi-wAA3mY61ARXbhyY8-Ci2d5V-0z0LLfT7QfYOoF5bmnofTEjVGgRMm6tA0XqL1kS0q9DernmbePgZuz1ZVUEVJ53kZUyn5mv5UUUbepYvY6gbgHKw-O_27ACsStahJRpyPsGB4kJ79wYLJwlTtHnpafe3cIaNLHqMl8NZ8y-lOy4zsXX8IH-jXnU3we4km7wNthXVufEHbbKo2uryJEoHk_Tdpl9LLpEcTMl6ZND6EE7_7aUmSD2KVkCacqbv6aYz0xcM1agTlG49n0tf1610qlbcpVcE3OsvPC8qTGNM1s1P1zE6XLxX29-3vKJRjmpZIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌برتری پرتغال توسط گونزالو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97761" target="_blank">📅 04:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97760">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ay5mSSBe-NFC__tOng4DV9itBeiq1lYRdxHkQaKPKx97ZRlho7jF4WaOBKwN1eSnWTfT46Wrbbsh-RkeZ5DVKpNgNgCFbb4SSUHXGU1IdDOHtXl5lz3E4sr4TqZgfKekwboDIjvxx-FxdgkJ3a_EhgDT3ofhcf7WZFnlWbGvDft4Qm-h3jsh9gG7wD5iiU0_zoSU6K70uzxJFpAD78jgy3LO-erFCvwTh3QGa98mMcv5X8nObpAasD1z9l2cCYn7VLvZRDLz0W1Z16dB_W_BPQhI66kXbQ5kONeKYoR05n2iqSM3NAATXR4srFL0jUcdJCAQhD_gHmVBSV8trnaN_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/97760" target="_blank">📅 04:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97759">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">همکاری مهاجمان میلان
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97759" target="_blank">📅 04:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97758">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دقیقه 94</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97758" target="_blank">📅 04:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97757">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">چه دقیقه‌اییییییی اللللللللهههههههههه</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97757" target="_blank">📅 04:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97756">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پشمامممممممممممم</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97756" target="_blank">📅 04:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97755">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گونزالوووووووو رامو‌وووووووس
😐
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97755" target="_blank">📅 04:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97754">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پرتغااااااال</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97754" target="_blank">📅 04:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97753">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گلگلگلگلگلگلگاگاگگاگاگا</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97753" target="_blank">📅 04:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97752">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">داور کم لطفی نکرد ۱۰ دقیقه وقت اضافه گرفت</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/97752" target="_blank">📅 04:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97750">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/849a19bd98.mp4?token=HTVMdH6cl7ubJOunAiaWcpGBkgBuSHb1OUvN27njRfhCeHHNsYCeYcgoSHrLX99wtu4guSo-Q7_n9ERZKAsMivLv7Y1XtnR7MEdMwxbDpsg7AuRJRLRl8RzAlb0ThZAxS9MSomx8SrqkrMieJXS1D9XCu79kPlpuMM533Ns-U1bAnnxksY-DwhPIBfgbjHYZJh1e6xm7yDokRZxagA5OT0JaRAeQWZGc346J6cEeuyEcmQth9FzEAFvMKtQBrM9GqvAuqckgc3XQQZHEm-cfnAXSRUg9ii9oGSleoxsaT68VbDt4WUYRuSDkzEBYDMpCow_C0J_FNtA5BzJUwnqd_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/849a19bd98.mp4?token=HTVMdH6cl7ubJOunAiaWcpGBkgBuSHb1OUvN27njRfhCeHHNsYCeYcgoSHrLX99wtu4guSo-Q7_n9ERZKAsMivLv7Y1XtnR7MEdMwxbDpsg7AuRJRLRl8RzAlb0ThZAxS9MSomx8SrqkrMieJXS1D9XCu79kPlpuMM533Ns-U1bAnnxksY-DwhPIBfgbjHYZJh1e6xm7yDokRZxagA5OT0JaRAeQWZGc346J6cEeuyEcmQth9FzEAFvMKtQBrM9GqvAuqckgc3XQQZHEm-cfnAXSRUg9ii9oGSleoxsaT68VbDt4WUYRuSDkzEBYDMpCow_C0J_FNtA5BzJUwnqd_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسم الله گفتن رونالدو قبل از ضربه ایستگاهی و پنالتیش
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97750" target="_blank">📅 04:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97749">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VD-YP9Gtuk4UbD8Pj8ChzvZNkwkW3SkNbq-NGgKqcefgn0sKbQeaO54zieBU6VJW0fX5EvvqHo61XN4T0JwNKzNb6KWgo2VgGqIlk53j_rAReLx3YvANBvHsXZ4s_BXoevQ-2HjroFzk0RcwwPCCtbcPBUT5yHS9HVgrF5XUu7pzjA1mvlASYzP_pzZGDW_jNe5HBilCRaLQvJMTJ9kEn2TdDorwPEaXXWuh97f8UtVCYwunuiFpoj-KpfbjW2eF62SXbdj7V0oOYmSIZjI-PGy8gsJ6CBSTDySr2r370DFwGia15z9-bYoMOol9oPCdplNjBzQMIrbO1P_gXDbOnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین قاب از رونالدو تو جام جهانی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/97749" target="_blank">📅 04:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97748">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رونالدو حسابی کلش کیریه از تعویض</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97748" target="_blank">📅 04:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97747">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
رونالدو رو کشید بیرون</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97747" target="_blank">📅 04:11 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
