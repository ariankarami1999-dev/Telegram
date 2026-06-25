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
<img src="https://cdn4.telesco.pe/file/c6bgWZKLl8jSUnsCo1oVwaH0It2mO_wYOtbpjQBQzZWTcvoZje5QbHoFDobzhJirjwNBITW5vtRkXF2_1ev7cZJ4CnUmx_Drx414jlRSr4tYVfB-3E6KhsrvmF-IFDNvx28wnWMy6XGipsTusLcSqI4aiV-Fqe4M3e6_fVVGDoJWy2dpNOPPNlWY2Jd_QfmlZpSpxVkua2YQj49SK8xHArCm0STzIdbqBc7cjRUBR9RByeh4N5RlMQmpYg3YF8FKCUO4hw6k5HLtGkLO1HWFUJX719xEd9Jxt0ovzlNujDdJroLjlaGUs4ho5XTjPibBEOzZA5qsurlD05_1N-Zr4w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 11:10:51</div>
<hr>

<div class="tg-post" id="msg-79830">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇶
📰
رويترز عن مسؤول كبير بقطاع النفط: العراق يمر بأزمة مالية حادة ناجمة عن الانخفاض الكبير في صادرات النفط بسبب حرب إيران ويجب النظر في زيادة حصته في أوبك بمنتهى الجدية
🔻
العراق ناقش داخلياً احتمال خروجه من منظمة أوبك، لكنه يعتزم البقاء في المجموعة والضغط من أجل الحصول على حصة إنتاج أكبر.</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/naya_foriraq/79830" target="_blank">📅 11:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79829">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2hzAhcmnkCwca0_2YNdboqUnHIz96cYNjScjyIsRlLwIeX9lGiMSnBiNjHCRSyUKLIYBJwG53qqq_t5aJVuPjxLQUlqTxYKmMNJ7Q1lHep0KEYs2k5fVw60tVeqw4cEQnFyzhOT8mVdQrbweGdOQdmUJQqF2IXubHLVmfOnZUXtd9G230gVr5LS-NxfY8bFzSsxZfyETRRlUUlzWaT_MM0CVJcIzkmA5niUa0gYXSqMFEATNTA2pHiSY8hNYAnPlCgq9-rpLOjPWQ1vIPqgesJoDqECIYDp7PxdFCESZc9xtnKkdu_X2L9tf-KNTxlAKM3RLiR2UgbPo31YZYRNXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
أفلس العراق رسميا ؟!
مجلس الوزراء العراقي يقرر إيقاف التعاقدات للمشروعات الجديدة الاستثمارية وما يخص العقود السابقة يبلغ الشركات " اصبروا ان الله مع الصابرين " يبدو انها آثار عواقب الحرب بين امريكا وايران على المنطقة ..</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/naya_foriraq/79829" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79828">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0395c35c88.mp4?token=PDcC1CLWyiGCcc6vfyn5WerrDz3RvnumHzn7dyCwEzloizTWI81VRssdUA06SEiFkVJy0pIWQg4sOWd-C4udi2Tk2Vrv0m-7UUNKsw_E6WVyGsHdnR1O9vv3DBvBCAAN2W72zdTxM5hxi0Kisnxf7oLIy6oJsTxsUmIMsxF48dWL4yrmxmAxKmwxKo6FrIg7zgMwmTzpKPlIjtAhx4LBD8T-HffJelzUVxK5YROHgJDI-P4eIcUmR8A6qtGN1knO01C5OC5JcklQW8S7wBGfnmglWopMYdMeF9ZLECXT63GTxp2TvS2J1N7fCv7DtLPP94U7YyMzAqKdxYKFKY_ZcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0395c35c88.mp4?token=PDcC1CLWyiGCcc6vfyn5WerrDz3RvnumHzn7dyCwEzloizTWI81VRssdUA06SEiFkVJy0pIWQg4sOWd-C4udi2Tk2Vrv0m-7UUNKsw_E6WVyGsHdnR1O9vv3DBvBCAAN2W72zdTxM5hxi0Kisnxf7oLIy6oJsTxsUmIMsxF48dWL4yrmxmAxKmwxKo6FrIg7zgMwmTzpKPlIjtAhx4LBD8T-HffJelzUVxK5YROHgJDI-P4eIcUmR8A6qtGN1knO01C5OC5JcklQW8S7wBGfnmglWopMYdMeF9ZLECXT63GTxp2TvS2J1N7fCv7DtLPP94U7YyMzAqKdxYKFKY_ZcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
تاكر كارلسون: كان ترامب مقتنعًا بأن قتل آية الله سيؤدي بطريقة ما إلى انهيار إيران. لكنه وقع في فخ الحرب مع إيران بعد وفاة آية الله علي خامنئي.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/naya_foriraq/79828" target="_blank">📅 09:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79827">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36962cfb3a.mp4?token=vg_v2BeUAX7m-c174U05zLAx9p1nVmKxIAhzv3a5yzLFrKrTg9Gp24AtZOjNXAD59J6VYoywSbzzaRn1ydj6e_g04XV2Uf7mt0njifIg40qC1zUix_cyKNY7Q3qEb0CkUdWVeaWiCfIzT6DOHqULaNJNBCVXbJR1gSvo-uk5Dqm6SZmpPogPfTdXlPIMrRiHGOtI0XlwDKqLFSjtsuuH9mibR0mr5v4nYKX87eAHzHVq4R7F7akNz7jHFkQ8u4KZDWWOpqXn5GvSZ1_WLzw7jxRuvyXQDwFCxJD-hL5mIt6KjSoCxW0C20hulVpP6LCo3Z44hcvsjayQ1n4mxm4gVEop8V8wPYdiNCIv7zC846brv6H0wrDCUAKtAWxpHSYtk8HiexEUiUU6jhm8kHgJwa64k5VhkhbAH74gutbIW0jaP9h-LGnt8VNyXiWOSXp5KYLKjwMh1MG7nu3CY-CLfur_Gc1sPYXPkYMtYEPdNuk88FSC_M8Lvv3u9Hmwt7GhvHL18tgxcnwp_OiNtFQfYV47RT18jVZxcnVfgafOIBV7FbmtshqGZ0EZhJ6WMbX67DwIY42LgqBIUtJ7iig3UidyMhi-zw_1BTqK9DX0lxp9psSz06QwYQOzkiP-XwdPfW8rhNbNgkPAE8bESJm-KVUFFFfQlte6cNdJ4eGGfs8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36962cfb3a.mp4?token=vg_v2BeUAX7m-c174U05zLAx9p1nVmKxIAhzv3a5yzLFrKrTg9Gp24AtZOjNXAD59J6VYoywSbzzaRn1ydj6e_g04XV2Uf7mt0njifIg40qC1zUix_cyKNY7Q3qEb0CkUdWVeaWiCfIzT6DOHqULaNJNBCVXbJR1gSvo-uk5Dqm6SZmpPogPfTdXlPIMrRiHGOtI0XlwDKqLFSjtsuuH9mibR0mr5v4nYKX87eAHzHVq4R7F7akNz7jHFkQ8u4KZDWWOpqXn5GvSZ1_WLzw7jxRuvyXQDwFCxJD-hL5mIt6KjSoCxW0C20hulVpP6LCo3Z44hcvsjayQ1n4mxm4gVEop8V8wPYdiNCIv7zC846brv6H0wrDCUAKtAWxpHSYtk8HiexEUiUU6jhm8kHgJwa64k5VhkhbAH74gutbIW0jaP9h-LGnt8VNyXiWOSXp5KYLKjwMh1MG7nu3CY-CLfur_Gc1sPYXPkYMtYEPdNuk88FSC_M8Lvv3u9Hmwt7GhvHL18tgxcnwp_OiNtFQfYV47RT18jVZxcnVfgafOIBV7FbmtshqGZ0EZhJ6WMbX67DwIY42LgqBIUtJ7iig3UidyMhi-zw_1BTqK9DX0lxp9psSz06QwYQOzkiP-XwdPfW8rhNbNgkPAE8bESJm-KVUFFFfQlte6cNdJ4eGGfs8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: إيران لا تمتلك منصات إطلاق صواريخ. للمرة الأولى منذ 3000 عام، سنحظى أخيرًا بالسلام في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/naya_foriraq/79827" target="_blank">📅 09:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79826">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039cf77145.mp4?token=Awf3GKX_0nNguFpgWpvTsc_VRPn2K6apwrgEMvgJ79jrgAeLsfzu_CK5GsIjU-UiY3G4fE332G7pkBh-fWH-WElMoX5N4QNLzq3tvLTM2YJNZyqgnz6cWd_dMWxNWO3l9lDwG2vwDa-RizSA5NhwAe0hMMXQJ3-mp-3dXoQ0E2ei3c551WxkvM06193nZWLh2gUDaU8XKv7OX5XODCpiqhZaY_8P8R5exoAcQwtJCT-nmbFLjreQ5CHPFq5FVWVc4gHDCFolJYFZPWHSGCYR-VIgVzud38z9yOCxeSU4fFwJ7WG74bFzcuDQ8jKzO4mBDmlnOtJZcgIxo6iqDDDXgC-UGH7fAIW3p0fX4gt6CaLEXnOTUo3_tHzCJZ1tp_5YpBxpBO-Za0xSndxUWcR4GsXQV3yQJm-WwmfAHX3BkkGPqAllBDaWf_oYiOtCo97sDix8PEN8NHLcOsq6KTN-1z78RRiFFbW6xy_C10G6PkZm4xAYAen7QJFQBlg8-bJtD8Hm0LSg3YlLqZqq5XxIgwdGbtk2_lyiqJASoOu5sy0vm7AdfrAW-SEwLX1JlGdBLcW7WJoWBN6PSzyy1cc8K8pzve7N3RG4Ao-JhfmOggRTRxiRRJkIMhPD41PkbgvY24BhqkKb1kN6f12AXCQaHN_WvAnCsW90HY95iwYJ7vI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039cf77145.mp4?token=Awf3GKX_0nNguFpgWpvTsc_VRPn2K6apwrgEMvgJ79jrgAeLsfzu_CK5GsIjU-UiY3G4fE332G7pkBh-fWH-WElMoX5N4QNLzq3tvLTM2YJNZyqgnz6cWd_dMWxNWO3l9lDwG2vwDa-RizSA5NhwAe0hMMXQJ3-mp-3dXoQ0E2ei3c551WxkvM06193nZWLh2gUDaU8XKv7OX5XODCpiqhZaY_8P8R5exoAcQwtJCT-nmbFLjreQ5CHPFq5FVWVc4gHDCFolJYFZPWHSGCYR-VIgVzud38z9yOCxeSU4fFwJ7WG74bFzcuDQ8jKzO4mBDmlnOtJZcgIxo6iqDDDXgC-UGH7fAIW3p0fX4gt6CaLEXnOTUo3_tHzCJZ1tp_5YpBxpBO-Za0xSndxUWcR4GsXQV3yQJm-WwmfAHX3BkkGPqAllBDaWf_oYiOtCo97sDix8PEN8NHLcOsq6KTN-1z78RRiFFbW6xy_C10G6PkZm4xAYAen7QJFQBlg8-bJtD8Hm0LSg3YlLqZqq5XxIgwdGbtk2_lyiqJASoOu5sy0vm7AdfrAW-SEwLX1JlGdBLcW7WJoWBN6PSzyy1cc8K8pzve7N3RG4Ao-JhfmOggRTRxiRRJkIMhPD41PkbgvY24BhqkKb1kN6f12AXCQaHN_WvAnCsW90HY95iwYJ7vI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: إيران لا تمتلك منصات إطلاق صواريخ. للمرة الأولى منذ 3000 عام، سنحظى أخيرًا بالسلام في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/naya_foriraq/79826" target="_blank">📅 09:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79825">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇷
هزة أرضية بقوة 3.5 تضرب خراسان شمال شرق إيران</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/naya_foriraq/79825" target="_blank">📅 09:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79824">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAIsz0m6kZHStgGxxFTsCVpJCJNH7LNMGOrjNl0dzAY3wd2u_KmjDe5GDSfCxXNDL-B5RQJi0tqxY-WwK03t1tk3-ESBvzCR7TWPMzm28IzZfRm1bpVl-ppCmYGrap6u_1qvMu0Jp31tBO7usZgwBihAX_hQyxRCZby26TptMaUzNRPHkpTK1f8ksqyV_v_Ob2IY6-KDmSmNXF6L9XD4xMgO-Rfyv8U6MN1bHG_FCXsy3csxePYnpOivFssyeCcXNS_sU4ukdnzDNCLnWvrl_Z3i8Tv7CWvWRPiW346TNOR5Fk5jhjVcP4x_Ytn6ZBOwtlYyCGJrjSU8cCdomjKokA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
الزلزالان الكبيران اللذان ضربا فنزويلا مؤخراً كانا هائلين، وقد خلّفا عدداً هائلاً من الضحايا. الولايات المتحدة الأمريكية على أهبة الاستعداد لتقديم المساعدة!
‏لقد أصدرتُ تعليماتي لجميع أجهزة حكومتنا بالاستعداد للتحرك بسرعة. سنكون حاضرين لدعم أصدقائنا الجدد والرائعين. التقارير الأولية ليست مبشرة!</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/naya_foriraq/79824" target="_blank">📅 08:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79823">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZglEdR4uUbmizEypG4VWJAZpxzBdY9BPBhtMI9S9bDixAO6WMFdvVwf7-zr2E2oF2pUs4VumNmYL7Z6AWkX__JrFEwamf6weZfTvizqEcqpBKibAFDqxRRlu8EJydx7Y1C8ZHYfrEp6fS5aKAesLJp3y62vEf-zIBlUhZjixhtsndSYts1b8TmJe-PeavdZhvcLcHsbvdv4uXDkLg4HWb6K1gPezqHjO7snt1iajxuAEJBCu2SwdJqdPlF5CmNXG8o2cyqBzYl19_XCJNOOCnZk3MV6qt-x4WLY7KDAEk_fgqdVj9tjokgKZ8RIovkXXMAfC_WtCMMue-gOl6dd1aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الزيدي للصحافة العالمية :
سيتم تخصيص 500 ألف برميل يومياً من النفط العراقي لتجديد الاحتياطي النفطي الاستراتيجي الأمريكي ؛ سيدرس العراق "تعليق" عضويته في منظمة أوبك إذا مُنع من الإنتاج بما يتناسب مع قدراته
‏سيتم "خنق" الفساد
‏سيتم نزع سلاح الميليشيات بحلول 30 سبتمبر مع مغادرة آخر القوات الأمريكية</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79823" target="_blank">📅 01:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79822">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">امين عام النيتو في البيت الأبيض يحاول إقناع ترامب بأن الحلفاء الأوروبيين ساعدوا الولايات المتحدة فعليًا خلال حرب إيران. ليرد ترامب خاب أملي من إيطاليا وبريطانيا وألمانيا وفرنسا وإسبانيا وكان من اللطيف أن يعرضوا مساعدتنا في حرب إيران</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79822" target="_blank">📅 00:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79821">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05f1c85d25.mp4?token=bnhS4XKTJCfRBkXQXrgVFJyRSiUKAlej3Y7HRYIkaBePGYHjU3_eoSQTMFXxIliG7pvqDVdMKGD9D1O_2w2QvecNTn8aKEH-aO56lx8WSMsLFiuP5wVAWIDzuQVwf24fflHmVtlCisD6pd0UTx-YoOUqg2ymg0ngsZcFXx3BJWvUzGZHgokmWyTtBUi5-wuihpsnGkykbuboUwsgH31KeLjo_vpuTG-AE3OnCswfmpqyPOzttC15nI4MjCBf1mQNVueh6ChXroKu62nhJm4eQqiMqujua7V8oRUENzthYRhbGSeJQ94ve_UIxb1mcIiBeblhsxQCQ2yj-3d2_W-O8S57oB1DAd6qmxXJkQ5uyjXZLC_jPZlFn8plNzwai7Juupk4L3LDYSf4pQP6MQZlR4qqFTBE2QyO5cgrSXRGbH6Cy5OHEX4RRaGhfIDKFaZ1G3X8Cn7A2rlWEqdQLvN26kDAj_4kdM1gcEJu-CI-kLLj8w8eKCmq95ovVKDzzXGJI5nmuMMeH9Vrr7Ls_wT8688rsG2NcLT_pFaW5r8TUJAv7HKlIgHm9Yzvv6lSqA_FKuTm5-Ep4ntriUWx-HOtGs7ONFW8TjbcYLRWLpM9Mk7zEPB2L0hM2bdHTYQqJfRcvqitUbUN4QLSBJx4AXv7uRB6_sabyiJmTSw8lY1InWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05f1c85d25.mp4?token=bnhS4XKTJCfRBkXQXrgVFJyRSiUKAlej3Y7HRYIkaBePGYHjU3_eoSQTMFXxIliG7pvqDVdMKGD9D1O_2w2QvecNTn8aKEH-aO56lx8WSMsLFiuP5wVAWIDzuQVwf24fflHmVtlCisD6pd0UTx-YoOUqg2ymg0ngsZcFXx3BJWvUzGZHgokmWyTtBUi5-wuihpsnGkykbuboUwsgH31KeLjo_vpuTG-AE3OnCswfmpqyPOzttC15nI4MjCBf1mQNVueh6ChXroKu62nhJm4eQqiMqujua7V8oRUENzthYRhbGSeJQ94ve_UIxb1mcIiBeblhsxQCQ2yj-3d2_W-O8S57oB1DAd6qmxXJkQ5uyjXZLC_jPZlFn8plNzwai7Juupk4L3LDYSf4pQP6MQZlR4qqFTBE2QyO5cgrSXRGbH6Cy5OHEX4RRaGhfIDKFaZ1G3X8Cn7A2rlWEqdQLvN26kDAj_4kdM1gcEJu-CI-kLLj8w8eKCmq95ovVKDzzXGJI5nmuMMeH9Vrr7Ls_wT8688rsG2NcLT_pFaW5r8TUJAv7HKlIgHm9Yzvv6lSqA_FKuTm5-Ep4ntriUWx-HOtGs7ONFW8TjbcYLRWLpM9Mk7zEPB2L0hM2bdHTYQqJfRcvqitUbUN4QLSBJx4AXv7uRB6_sabyiJmTSw8lY1InWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امين عام النيتو في البيت الأبيض يحاول إقناع ترامب بأن الحلفاء الأوروبيين ساعدوا الولايات المتحدة فعليًا خلال حرب إيران.
ليرد ترامب خاب أملي من إيطاليا وبريطانيا وألمانيا وفرنسا وإسبانيا وكان من اللطيف أن يعرضوا مساعدتنا في حرب إيران</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79821" target="_blank">📅 23:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79820">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🌟
جيش الاحتلال الصهيوني:
أصيب مقاتل من جيش الإسرائيلي بجروح خطيرة نتيجة انفجار عبوة ناسفة في جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79820" target="_blank">📅 23:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79819">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c6939043.mp4?token=FfZ6SRj0_X5NYIwSTH5J1pNTpszTchFqpQBtcE7xPuCstM6fAIZpPj7qG8ksFjqihyL7IVORiUemmEp5VdH32e5XzyhRT09LyFcpeTZzo7FK-NOVbB0LTBLD4or88VelY9BYkzn8P-xfipm8NGj3e0X5c7YahP31F25Dp3L4XP4Osq4B2JA4d4AY7YDrACMIX9KpysSZMZjV6KAToOOb4A-0Fpw9v3ByYoN5i9jbr3q9XB876v2FijCQvjYanMocXIzKg7ZLSUgugVb7u5OAGiT2X75c2dqbJAuVKaC3VrbGb28mQMYbbW4KDVGhNRNAfVbiXoMKBaofoqzLb6liiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c6939043.mp4?token=FfZ6SRj0_X5NYIwSTH5J1pNTpszTchFqpQBtcE7xPuCstM6fAIZpPj7qG8ksFjqihyL7IVORiUemmEp5VdH32e5XzyhRT09LyFcpeTZzo7FK-NOVbB0LTBLD4or88VelY9BYkzn8P-xfipm8NGj3e0X5c7YahP31F25Dp3L4XP4Osq4B2JA4d4AY7YDrACMIX9KpysSZMZjV6KAToOOb4A-0Fpw9v3ByYoN5i9jbr3q9XB876v2FijCQvjYanMocXIzKg7ZLSUgugVb7u5OAGiT2X75c2dqbJAuVKaC3VrbGb28mQMYbbW4KDVGhNRNAfVbiXoMKBaofoqzLb6liiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
رغم التضييق، يواصل أبناء البحرين إحياء الشعائر الحسينية، مؤكدين تمسكهم بممارسة الحريات الدينية التي تُعد من الحقوق الأساسية للمواطنة في الدولة الحديثة.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79819" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79818">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09002baed0.mp4?token=iiOLYsXFxjGG1sRsY6KcEkGmu-OrntMlJ6xR0A1w6t70b1L7g8hcwCg-L5s5Jjb5OxTBJesjKvtiirG6BGrT60y9goAf54ud-octybfe8wnzCMyiga4Pj7kRnJ1KeneKZbNnEkjxlaq2BfKzYwR_-W9uAlqTKL315zc1wVzgSrYcbu2Fp6JbkOj7XkZj2OyD9IUI-c6LbDqyiXHrR1WGKHCOAtYVYGVxGrTts8R1Yv_5vQ3SLmf8NVkHth1rgR88rHS1mVDV_Ngt_j19kdt4vLn1-ImFW5Jm0Z1sVI-cmmGVjwUWqoX_88nRJBwkgbxeY40CxAeB_fHjj_7xU0qyNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09002baed0.mp4?token=iiOLYsXFxjGG1sRsY6KcEkGmu-OrntMlJ6xR0A1w6t70b1L7g8hcwCg-L5s5Jjb5OxTBJesjKvtiirG6BGrT60y9goAf54ud-octybfe8wnzCMyiga4Pj7kRnJ1KeneKZbNnEkjxlaq2BfKzYwR_-W9uAlqTKL315zc1wVzgSrYcbu2Fp6JbkOj7XkZj2OyD9IUI-c6LbDqyiXHrR1WGKHCOAtYVYGVxGrTts8R1Yv_5vQ3SLmf8NVkHth1rgR88rHS1mVDV_Ngt_j19kdt4vLn1-ImFW5Jm0Z1sVI-cmmGVjwUWqoX_88nRJBwkgbxeY40CxAeB_fHjj_7xU0qyNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏ترامب: الحرب تسير على ما يرام. كما تعلمون، نحن نحقق انتصارات كبيرة. إيران تقدم تنازلات كبيرة للغاية. سنرى ما سيحدث ،لكنها كانت قوية للغاية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79818" target="_blank">📅 21:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79817">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🌟
🇮🇷
استكمالاً للتنظيم الأمريكي الفاشل في كأس العالم..
أفاد الاتحاد الإيراني لكرة القدم أنه خلال الزيارة الثالثة للمنتخب الوطني إلى الولايات المتحدة، قام مسؤولون أمريكيون بمضايقة سعيد الهاوي ومهدي طارمي، مما أدى إلى تأخير مغادرة الموكب إلى سياتل لخوض المباراة ضد مصر. وينتظر أعضاء المنتخب انضمام اللاعبين إليهم.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79817" target="_blank">📅 20:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79816">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3d12ba221.mp4?token=Ae9l0t0fcSo5WwGWEpAavNnhYPWN1EzCjcBBlUS6njJ68v7JTVhF-_vZNeWbeq_9UOkSZfCrNey-_wJ5ueox7Nh1UOCK0LxO9pKup-UFybjtZtLZTXXYYxWSRomNuueXx92F9qbeCxK8VXB3J0rNATOcpU70JQ_BU9ygiF06fBfSEUIw6HHqs-RX9sTMzlGQhrCbshGLuSt_JmVRDTwQv6iffI3FKFirI85tEyvb6TfLb9M9sSooyPQl1BSWHhRgb4FQP9lKILRIa1VS8rJ3HoUoB-V-G7nMc3KJ4OboVyMI6TX2l9Isy_yOA596wEZmlpJJMg-UWnjxxL9-67F_ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3d12ba221.mp4?token=Ae9l0t0fcSo5WwGWEpAavNnhYPWN1EzCjcBBlUS6njJ68v7JTVhF-_vZNeWbeq_9UOkSZfCrNey-_wJ5ueox7Nh1UOCK0LxO9pKup-UFybjtZtLZTXXYYxWSRomNuueXx92F9qbeCxK8VXB3J0rNATOcpU70JQ_BU9ygiF06fBfSEUIw6HHqs-RX9sTMzlGQhrCbshGLuSt_JmVRDTwQv6iffI3FKFirI85tEyvb6TfLb9M9sSooyPQl1BSWHhRgb4FQP9lKILRIa1VS8rJ3HoUoB-V-G7nMc3KJ4OboVyMI6TX2l9Isy_yOA596wEZmlpJJMg-UWnjxxL9-67F_ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
جيش الإحتلال الإسرائيلي يعلن عن خرقه لوقف إطلاق النار: شنّ الجيش الإسرائيلي هجومًا على شخصين مشتبه بهما عبرا المنطقة الأمنية في جنوب لبنان، وشكّلا تهديدًا لقواتنا.  قبل قليل، تم رصد مركبة تقلّ مشتبهين عبرا المنطقة الأمنية في منطقة مرتفعات علي طاهر، وشكّلا…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79816" target="_blank">📅 20:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79815">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fed3ef8188.mp4?token=LNYmC5kA4PfqHjHuATa5EUYj6wDgW39boOsc86MXYlKy1Ga2CCAxpx_8ToI1pX9DlIjTDcTK8RcW26e8Em9ldwx7oh4-Zx2LR_xg90qsmg-u1_nQjWrc9j7fr_lLDwTZwhhFM7Fmz8S-fZle7OvLCptan3BE6itapOKQC1HJiSvYW6Bai7relHWgF5ox7gsf6bKCXVooptH4lmdH9qk3gUoC5b6qcoUmSHublVM7ok9PoFdDLz_ICBwCwQ_92z10HKA7jSOkH31lyAlLkYCAca2BgX_uD2XJwQktRdBneO3sQR5z_gmOvo5I3yFKdZF5PYvQQm_fr1BrpWhIafjGXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fed3ef8188.mp4?token=LNYmC5kA4PfqHjHuATa5EUYj6wDgW39boOsc86MXYlKy1Ga2CCAxpx_8ToI1pX9DlIjTDcTK8RcW26e8Em9ldwx7oh4-Zx2LR_xg90qsmg-u1_nQjWrc9j7fr_lLDwTZwhhFM7Fmz8S-fZle7OvLCptan3BE6itapOKQC1HJiSvYW6Bai7relHWgF5ox7gsf6bKCXVooptH4lmdH9qk3gUoC5b6qcoUmSHublVM7ok9PoFdDLz_ICBwCwQ_92z10HKA7jSOkH31lyAlLkYCAca2BgX_uD2XJwQktRdBneO3sQR5z_gmOvo5I3yFKdZF5PYvQQm_fr1BrpWhIafjGXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏
ترامب:
الحرب تسير على ما يرام. كما تعلمون، نحن نحقق انتصارات كبيرة. إيران تقدم تنازلات كبيرة للغاية. سنرى ما سيحدث ،لكنها كانت قوية للغاية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79815" target="_blank">📅 20:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79814">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
🇮🇷
‏
وزير الطاقة الأميركي:
إيران لن تكون قادرة على إغلاق مضيق هرمز بعد الآن.
‏الألغام الإيرانية أخرت عودة تدفقات النفط إلى طبيعتها  في مضيق هرمز.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79814" target="_blank">📅 20:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79813">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🌟
🌟
خروقات مستمرة لوقف إطلاق النار.. غارة معادية على النبطية فوقا وقصف مدفعي صهيوني على بلدة ياطر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79813" target="_blank">📅 20:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79812">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhSPSI7-NWLTGKGc2TqJlgQy_YhA8ta_n4dAd2eRvsEnG163EPxmlTGDBlttNZjqv_Q8yDm470a5XQO9G5ymD-4QmH8qZJqMJfvY1_tKOAbFHAfykm3b4SXOIOVxYghwZCieIkQublkpwny8e1QTf5PBQnLb53mp7bkctG2g1vesu8YnbuTYySzqRWzdIyoPJx9Xfn9rFbeG7fwKFZrdFykUWUOK1WzyiGignqnXAGM3r5RDbhTn9sak0HSXS9nufR6ALiiIlwoY974rzLuZqPtMqkSB_d7R0eCA-aikItf27dJ42FK61mnQid0hXDsw_qnDFjOjIP-UdsuGjExXmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث بإسم الخارجية الإيرانية:
لن ينخدع أحد؛ لا يمكننا أن ننعم بمنطقة مسالمة طالما استمرت النزعة العسكرية والتدخلية الأمريكية، واستمر وكيل الاحتلال التابع لها، مع الإفلات التام من العقاب، في شن حروب لا نهاية لها في جميع أنحاء المنطقة وارتكاب الإبادة الجماعية والعنف الإرهابي وكل أنواع الفظائع.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79812" target="_blank">📅 19:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79811">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiqhMoTHEO0tGvFUcf091xMs6ow4nDyrGI62aksAeIot73ImO0Wefmns126N9_25Fn0spZ4kuntMLjm8Vy712OqWFMarlWgFXHkwOF_LlRuMa3tclNCTAz9FY6qSanLpSc_je8JpsCJ5aaN2hgf4hikcr2d-4cIKNySPQZA1xhO4QEto_3Ld2P5gUPiK90JrANzSkRH8ypFGjRDCttXiJI1W6ymkudOrUAna3ZZpfhVu-KgmowBOTDrgYkHss5FcP53B7RSd4poknyH1gXaJy8rtWAwxTcsjRpkjbR4rtButFBZXJEpHZQnJdRw3cZxOme_G5eAFa2U5nLygPvaX4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
طائرة أمريكية تطلق إنذار الإستغاثة (7700) فوق الأراضي الفلسطينية المحتلة بعد عودتها من أجواء غرب العراق.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79811" target="_blank">📅 19:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79810">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⭐️
علي الزيدي:
العلاقة مع الولايات المتحدة ستتحوّل من عسكرية إلى شراكة اقتصادية.
معظم الفصائل بدأت بالفعل بتسليم سلاحها للدولة.
بعد انسحاب كل القوات الأميركية لن يكون هناك أي مبرر أو حاجة لأي مقاومة في العراق.
نريد من "أوبك" زيادة إنتاجنا النفطي بما يتناسب  وقدرات العراق النفطية وعدد سكانه.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79810" target="_blank">📅 19:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79809">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🌟
روبيو:
الرئيس ترامب يريد أن تلتزم إيران بمذكرة التفاهم وإلا فلديه العديد من الخيارات بينها العودة لفرض عقوبات.
اللجنة الفنية ستعود إلى سويسرا يوم 29 الشهر الجاري لاستئناف المحادثات مع إيران.
المحادثات الفنية مع إيران تتعلق بالملف النووي والعقوبات.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79809" target="_blank">📅 19:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79807">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u_udraJMKjnmwprQCOxv5wK5VMTd50qjMBvdkczHyFUdccFjl2KAgY1jaSJwy0Kk4Fbcnoxk9XdJtMzlr-FwUeGUiNZA1TeHMqb1_MlZJF5runusW-nfqbqNsKErCWukOizDesF9dO8figHtAKJOz_g25Q8qmbh03Keo41q2gGEi-VDGg7b3qmOqMB3nSU_JnmWltGDRR4FncRKZE9taEn2C2J6hIUTHPFKfCn4527AOcTujXfswkGjlHvX1JXz3YEnZ0U-TFRofxdAKPSLOEc5Ob3hMvmf4wBkWTTiWjNG1ThOTWuMq_HlFYNJKH0jmO20vrmkrBWHCo_xwgrRFkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IskTrDw08oWR7PyjmWhVpHWjhfvHFfE4XO_lbbcSnVy7iDWQTSJ4r7vzEtLPXDyZ1M8OpO8v3fKSV0vzRFNci_yrf6s2zE6Y9L_EgWgOYhDNiTpGH2JL5LkOsQdO7d6mihzAOpOXLjFjaog9olvLZfuh4o3Bp57nKetVS21t8kuBUNeJpB9A5snZ2T4veCJnZ4G1pn9LCai8DeDXVTyaqOKxldCc230J6FrflL3TencL_HSdTbXC8LH52_9ugpP7SPhTn4BXIoTMcP32vRYLUE5xxRhwt8jkvc1p1fsJMX8EXOJNDqSjEeJKYVGBtzNPjojyJzRDNTT72_4Y6P4pjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
صورة خالدة لإرادة قوية..
طهران، تقاطع ولي العصر؛ رجل مسن منحني الظهر، وعلمٌ ظلّ مرفوعًا.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79807" target="_blank">📅 19:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79806">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
🔳
🌟
سي بي إس نيوز حول هجوم إيراني على قاعدة أمريكية في الكويت:
يشكك عدد من الجنود الأمريكيين الذين أصيبوا في هجوم إيراني بطائرة مسيرة على موقع عسكري أمريكي في ميناء الشعيبة الكويتي في الأول من مارس/آذار، في مزاعم البنتاغون بأن معظم المصابين تعرضوا لإصابات طفيفة وعادوا سريعًا إلى الخدمة. في مارس/آذار، صرّح وزير الحرب بيت هيغسيث بأن "ما يقرب من 90%" من نحو 400 جندي أمريكي أصيبوا خلال الحرب الإيرانية، تعرضوا لإصابات طفيفة وعادوا إلى الخدمة. إلا أن بعض الجرحى وعائلاتهم أبلغوا أن الإصابات كانت أشد بكثير مما تشير إليه التصنيفات العسكرية الرسمية. من بين هؤلاء، رئيس ضباط الصف رودني بيرمان، الذي امتلأ جسده بشظايا عندما أصابت طائرة مسيرة إيرانية موقع عمله في هجوم الأول من مارس/آذار. تُظهر السجلات الطبية أنه عانى من ارتجاج في المخ، وفقدان للسمع والبصر، وتلف في الرئتين، وجروح متعددة بشظايا، ومع ذلك صنّفه الجيش على أنه "غير مصاب بجروح خطيرة". وصفت زوجته، إيمي بيرمان، هذا التصنيف بأنه "غير مقبول"، إذ أُبلغت في البداية بأنه سيعود إلى الخدمة. كما أصيب الرقيب أول كوري هيكس بجروح بالغة جراء الشظايا، وخضع لعدة عمليات جراحية طارئة في مستشفى كويتي، ويتعافى حاليًا من إصابة دماغية رضية. وقال إن عائلته أُبلغت في البداية بأن إصاباته طفيفة. أسفر الهجوم على ميناء الشعيبة الكويتي عن مقتل ستة عسكريين أمريكيين وإصابة أكثر من عشرين آخرين في الموقع العسكري الأمريكي. وأفاد ناجون وأقارب أنهم يعتقدون أن الجيش قلل من شأن خطورة الخسائر، بينما يرفض الجيش هذا الاتهام، مؤكدًا أن تصنيف "مصاب بجروح خطيرة" مخصص للأفراد المعرضين لخطر الموت خلال 72 ساعة، ولا يعكس بالضرورة العواقب الطبية طويلة الأمد.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79806" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79805">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c62883e3.mp4?token=h1HMCopcbRVE3zNzIRcwSePb-z6ubmjSEX4CUSLNoi0mnmvJ4JezBAixyQnWixMhhHcU7m23fN4ST3px4QtacdlwgttFhJCV9cwTJ8zZ3HWYvDk2tK2G5DqdxDmVHU3erXc6uBvz8g3Pe5vayS9RTMJHW19TXksXrG4AbPpvX9662pPWfezTEV9N6vbFRLhSIQEKBGidVzqTdsEYLRIeuRRJXouK_p1sK6FF3crSZNpTlzZuqZCgeDB2dAKQwfOG-G1dH4j0QMApk5tJVXeIXsa3n7d2esD80lRzUa8i052bx9bp-oG9FVcVu0nhZcuHs6cwIXzPhN8kveOAsWRduALOv3KGoNoXW6RMvxHbF6tTuK2f-2qdIoc61-2bNeliTR-q7gprmyqdxJHgqEweip7rQrYbBQktyw5WAAMHFkD-dq7Tqsgjdl2ETxsKSGg58XrsCbljh4AijbxQfxUfO5UFOZM55j1N1l3anua4NNDVQp8t_KbpBPQx5mKKnN4trqqMuzrKuaB9H6oMiV6FKyiU2oorB4gKV6FkEzczcwvaHLfyAwRajlL8SwqfuPC6wHXCCGOSqoR2NJ0BqKl-o29LCEIlUHu4nR5OQW0iZlgNXr0O9u8aUfF5Qam3ir-PVZyyBdLL9haFMWCWecrM2GcfF2jF-lziEojKlDTAjzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c62883e3.mp4?token=h1HMCopcbRVE3zNzIRcwSePb-z6ubmjSEX4CUSLNoi0mnmvJ4JezBAixyQnWixMhhHcU7m23fN4ST3px4QtacdlwgttFhJCV9cwTJ8zZ3HWYvDk2tK2G5DqdxDmVHU3erXc6uBvz8g3Pe5vayS9RTMJHW19TXksXrG4AbPpvX9662pPWfezTEV9N6vbFRLhSIQEKBGidVzqTdsEYLRIeuRRJXouK_p1sK6FF3crSZNpTlzZuqZCgeDB2dAKQwfOG-G1dH4j0QMApk5tJVXeIXsa3n7d2esD80lRzUa8i052bx9bp-oG9FVcVu0nhZcuHs6cwIXzPhN8kveOAsWRduALOv3KGoNoXW6RMvxHbF6tTuK2f-2qdIoc61-2bNeliTR-q7gprmyqdxJHgqEweip7rQrYbBQktyw5WAAMHFkD-dq7Tqsgjdl2ETxsKSGg58XrsCbljh4AijbxQfxUfO5UFOZM55j1N1l3anua4NNDVQp8t_KbpBPQx5mKKnN4trqqMuzrKuaB9H6oMiV6FKyiU2oorB4gKV6FkEzczcwvaHLfyAwRajlL8SwqfuPC6wHXCCGOSqoR2NJ0BqKl-o29LCEIlUHu4nR5OQW0iZlgNXr0O9u8aUfF5Qam3ir-PVZyyBdLL9haFMWCWecrM2GcfF2jF-lziEojKlDTAjzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
11-06-2026
جنود جيش العدو الإسرائيلي في بلدة العديسة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79805" target="_blank">📅 18:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79804">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW4kOWzqbRpVl-hkHxGQ6gLGPlW3FytLnHoJ7XTYf5aN9OuQdbUi_6EncyBg5uiP2bL-tEtXH5l7phRfUVSh6wrb9uMHA8ivHXl3wrjZJqOgpfdA6tJ4z2ovB8G_XtbHtjnVtJUu6AdlycY6hfpDnEbHcaChuuOdylQ4WkR7ZbwNbOoUTtAU6Uh_6uuFQApxfYIHXapvUndsLEomjKSKDxZhxfOlYUXzjrgnxkzYyD815ZFmTF_NjEENFhKsZkRss9IMqFh7IGsK_7oC1vSWPYeNOY8aFDAppbxdAiPpkBuQCiKzK3bFx20mhWSPg5FpbvTAYhauWe0fgI7g-lxkig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
خروقات مستمرة لوقف إطلاق النار..
غارة معادية على النبطية فوقا وقصف مدفعي صهيوني على بلدة ياطر بجنوب لبنان.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79804" target="_blank">📅 18:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79803">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6yqIdGJshm-7S8CVzMkSv705COYBhE8rTF9vaGkNjj2OYcJGbVlA0kJU4KriEYkmxfoImv3e2N6eYYdIUmuiWalBeORteLWfB4vVDeY-uflpQe4Re4gEMof03BcT8Jp0MWx0Wf5kLSiq2RGGl9uLQmbADKi4z0CNMVwDh51QPlJxw1LFYe5KGr34mM6JOZvdKaEZOnOfap0AawgMG7bSgEEyp_DoCAjqLF2iArV-hC2F_i9WJyIdqxeRYNkrycLBaf5aV0ki53ZX4chlfe2p2670OAkThY4l0X0fuTB67EtkYVg3_PLyA78hWRP0Kr0yECgvtqwGzSWClJ0_OluIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
شركة نفط البصرة توجه حقل الزبير: لمتطلبات العمل ولأستمرار حالة الظروف القاهرة في المنطقة وعدم توفر ناقلات يرجى تقليص الأنتاج والضخ ليكون الأنتاج بمقدار (300) الف برميل في اليوم اعتباراً من الساعة 12:00 مساءاً ليوم 2026 / 06 /23</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/79803" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79801">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8401d06eab.mp4?token=Th-y1DWpMRSkhlHLzOeszAuhY2PhrOyQwyXccVkw0gl-NtU13IbCcbAA09W_iBppVY8xdf5BdlmBUj9QWw9jw0v2m3v7sTMUgy2g1VfTUkbonBKusp7mneAcPXqgfyQygaPz1-NAV1AIyjec4ztT0odx9t4kvqxwD39gfJSFTnr4Q-uYrHX7Ap0OBbZDVeicumkUd6AF8My5ROxv1B_oFeFIUgLjBzyEUmd3J4uL6nRZn3kC6Tq4ptCc_XgjVESajEsBXqgfCc5tkEJE2RbmEgyo84vhb5vul1xGOUBq-LuuQJDV7I4HkQBvImJznqFEm1k3UtCdCZoJKrstP2xDIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8401d06eab.mp4?token=Th-y1DWpMRSkhlHLzOeszAuhY2PhrOyQwyXccVkw0gl-NtU13IbCcbAA09W_iBppVY8xdf5BdlmBUj9QWw9jw0v2m3v7sTMUgy2g1VfTUkbonBKusp7mneAcPXqgfyQygaPz1-NAV1AIyjec4ztT0odx9t4kvqxwD39gfJSFTnr4Q-uYrHX7Ap0OBbZDVeicumkUd6AF8My5ROxv1B_oFeFIUgLjBzyEUmd3J4uL6nRZn3kC6Tq4ptCc_XgjVESajEsBXqgfCc5tkEJE2RbmEgyo84vhb5vul1xGOUBq-LuuQJDV7I4HkQBvImJznqFEm1k3UtCdCZoJKrstP2xDIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران مروحي تركي يجوب أجواء مدينة الباب بريف محافظة حلب السورية، وأنباء عن نقل جرحى إلى مشفى المدينة.</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/naya_foriraq/79801" target="_blank">📅 18:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79800">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d073efb9.mp4?token=hWsFsBUd7T6QPRJlcBBqww32rcFYBUGhlugPoX8bwCfJIsclzRXTuIDNq5jghpZo_x4t2ylxLQtbOENdOPthioZ_JP_Gq8OoKaGGuucYdSXQ4CpDx22StJqpgiseRm1O42fNv0SdKCkCpLTgK428Xz3ovb7oVtUS3bzplhtx4SZJ7rJeiSnsrEyeyutgrU-pIK1A9qnWuDoSht8gLUWP5Ekfszr2FivqIr2bx2kMUAcxojfsNpewe_BeIt8Jjb8ke_upOUr6JfUFhkhxO3HNFbHCpA4-j1zHJB9wSN-SKwBA9aa_HLThjIUn2C5ae_T9f3kveQ7Kh6B6VIRbfvVJbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d073efb9.mp4?token=hWsFsBUd7T6QPRJlcBBqww32rcFYBUGhlugPoX8bwCfJIsclzRXTuIDNq5jghpZo_x4t2ylxLQtbOENdOPthioZ_JP_Gq8OoKaGGuucYdSXQ4CpDx22StJqpgiseRm1O42fNv0SdKCkCpLTgK428Xz3ovb7oVtUS3bzplhtx4SZJ7rJeiSnsrEyeyutgrU-pIK1A9qnWuDoSht8gLUWP5Ekfszr2FivqIr2bx2kMUAcxojfsNpewe_BeIt8Jjb8ke_upOUr6JfUFhkhxO3HNFbHCpA4-j1zHJB9wSN-SKwBA9aa_HLThjIUn2C5ae_T9f3kveQ7Kh6B6VIRbfvVJbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
الكيان الصهيوني ينهار من الداخل..
استمرار المعارك الداخلية بين الحريديم والمستوطنين في عدة مناطق بفلسطين المحتلة.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/79800" target="_blank">📅 17:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79799">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E313v4noaa6susFSmI0jwcfWWQX_o_OBwrUA18HdGSG4JEJsFVELXIPr5DqPPxygTa4qwlaMfeoTDlmHfAqZVvpdcKZySOCKWQQZ2Jm3RMvvtUEWi9NtueI7_KT4zPPkbPcM0oEuIFHLHfw7bt3-yPoYooUFdsKhLWNsSsZfb7xFgs90p7aQqlzXViwWkXYa5gcht6SdUkJAubFEFFVElltGQxJt3aqUy5P9e76MvE8RZ89FvlI_yYUH6VkR492YEYD3bTBIRz2I6rgpEdpQHoS4gyexMcMJB5B1IrqxUfucwGW9aTMzPd-CFxSLxQLVBDvzc2p4JKmh1oYEMdJcJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
يُلغى بموجب هذا المؤتمر الصحفي والتوقيع على قانون الإسكان المقرر عقده اليوم إلى حين إقرار قانون إنقاذ أمريكا الذي نحن في أمس الحاجة إليه.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79799" target="_blank">📅 17:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79798">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🌟
نتنياهو:
نقيم حزاما أمنيا عازلا في جنوب لبنان لمنع حزب الله من شن هجمات علينا.
لا يزال هناك ما يجب علينا فعله في لبنان.
سوف نحمي إخواننا الدروز.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/79798" target="_blank">📅 17:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79797">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🌟
إعلام العدو:
إصابة جندي إسرائيلي بجروح إثر انفجار وقع ليلاً في لبنان ويجري التحقيق في ظروف الحادث.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/79797" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79796">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmLfttUISmJnIAb_1EGcnjdj1GdNoB5o39F0QCnoY_YCtxBTLp4Uziv-kBnogVkD-Dk4MdJUZzoO7RnTGOLVf3hzwAYlpx9mQEH8ZzJh9QiU_7-ewOgxfThf0GvnLJWuNvxEcCBk3d-Zokuo2S0q20ZY4I5Q4RtcxuBZoGJpOl2orgb9Tum6Nlsz00hgcyorxcsDd4oGEyrw1qwWItRzbD_6EGYkSRUsaXADAUW9TcudiPDHH-DaY1XAtSGcaF62iqtfGthHEBXHyteU7rkUcM6ExW7qZwkBTtn8N3WwcbndmH_CBuM2_1feOQk7NFPXqY9YmVH9s6bgH5REezjhug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:
سحب العمدة مامداني ثلاثة شيوعيين قويين، وتلقى تصفيقًا عاليًا وشاملًا من وسائل الإعلام الإخبارية المزيفة. تهانينا سيد العمدة!
حققت ليلة أمس رقمًا قياسيًا بلا خسائر، حيث ساعدت في انتخاب وطنيين أمريكيين رائعين، ووسائل الإعلام لا تقول كلمة واحدة.
على مدى العامين الماضيين، أدى دعمي إلى فوز 259 انتخابًا تكميليًا، ولم تكن هناك خسائر تقريبًا، مع عدم تلقي أي اهتمام من وسائل الإعلام؛ أخبار مزيفة.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79796" target="_blank">📅 17:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79795">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMesIc_IS4hcpNay81nNPMp6eWo0-ry5rbrNQY5vPoSvLI5mK92Raqdf8wCfwbTf4fOUmjNFKcE4vcQd8EMyhm_GTfjqW-nQSp4BvpSg9XgpI8PDHjv81Y9HW1p8SjQ-vEM4npC06ytbBBc2ltB_Ng0h5OZ8N137qsfHa4po44jHRR5Klmq_H1HN5GFySKuRujsLHABJAPQ1-njWugrb_oUjtxIaYp8wW5Au8V7gS8V9dCofq_Ssnjsc_xXTUZlYlb2XbwWnm8qaGU6GgF_09TNjtNy-1bcWBw_6OWXJmuJdB6X6a2ZiAm8GWEQQyZCH0Raj2dcndEiJv3OjQ6NhKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
شركة نفط البصرة توجه حقل الزبير:
لمتطلبات العمل ولأستمرار حالة الظروف القاهرة في المنطقة وعدم توفر ناقلات يرجى تقليص الأنتاج والضخ ليكون الأنتاج بمقدار (300) الف برميل في اليوم اعتباراً من الساعة 12:00 مساءاً ليوم 2026 / 06 /23</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79795" target="_blank">📅 16:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79794">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🌟
سلطة الطيران المدني العراقي:
منح ترخيص التشغيل لمطار النجف الأشرف.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/79794" target="_blank">📅 16:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79793">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🏴‍☠️
‏إير فرانس تمدد تعليق الرحلات من
تل أبيب
وإليها حتى 30 يونيو.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79793" target="_blank">📅 16:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79792">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الذهب يسجل خسائر غير مسبوقة منذ نوفمبر 2025 وسعر الأونصة يتراجع إلى أقل من 4000 دولار</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79792" target="_blank">📅 16:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79791">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64062428bd.mp4?token=MrA5IbTuBeEtIKCSr1Fb_nhyPpeqPDzv76JARDzjywJNO8687blFiT3vagXuvQYxddWpbG0JgaLjh5Cf8AVO8Ia8Yze8pKcj83lk-3M-agz5NtkhnT7ZrOVGWs4AFkVEe_VFvS_qUWui-Bz9wRdLP-n6kchfRv5u4w-sCpupIh8SqHtIGht9qWuLQ0BNV0xECaqcVophkFbQjK-T6uWHaxg7AMSxK4LpkppPU095OHQO5JMlyvZ1XK4PI2NW0n8ifglyShCXKjaFK9Z0-y7H-JZsooSqd38PeBEjIkYvvT2JZHmhGg2w2AY_k0HhqMHPYzXjzHcISphW8mUnns5MiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64062428bd.mp4?token=MrA5IbTuBeEtIKCSr1Fb_nhyPpeqPDzv76JARDzjywJNO8687blFiT3vagXuvQYxddWpbG0JgaLjh5Cf8AVO8Ia8Yze8pKcj83lk-3M-agz5NtkhnT7ZrOVGWs4AFkVEe_VFvS_qUWui-Bz9wRdLP-n6kchfRv5u4w-sCpupIh8SqHtIGht9qWuLQ0BNV0xECaqcVophkFbQjK-T6uWHaxg7AMSxK4LpkppPU095OHQO5JMlyvZ1XK4PI2NW0n8ifglyShCXKjaFK9Z0-y7H-JZsooSqd38PeBEjIkYvvT2JZHmhGg2w2AY_k0HhqMHPYzXjzHcISphW8mUnns5MiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
مشاهد من احياء ليالي شهر محرم الحرام وذكرى استشهاد الامام الحسين (عليه السلام) في مدينة ديربينت الروسية.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79791" target="_blank">📅 16:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79790">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">امريكا تزعم قتل قيادي من داعش في غرب سوريا</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79790" target="_blank">📅 16:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79789">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHMPaAYC3U51-8p9FxBDJfNNfIkm0iUapt2LulYrNGkea1usxww3KxI8RVoID_J83EdPBTkOU2cykSHcc0COSIZ0FKPG2Jx4L-crhse-ylgDcI9rBV7l90YArt8X6YPs8VenirDKMOuNhy6EMzPNlcfPFtYUPFBWL2dcXTsFAAFvxjoQLqXxlgkfYYg0xpmF_bBB0vtyUn5nmIKUuLZpcTxaPkf30YWIi5Y-kfBRfIizSvaljeCNDI7lee6BhryRuD8nagdjhdSp8n-C6s2aDPps8-Vnh5j1CmSvRNYEEnUuAjmaZTV2bUdC5YJNThbT8TTrGYBi47vZd_BdCu0tJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
السفارة الامريكية في بغداد تشارك تصريحات ‏وزير الخارجية الامريكي ماركو روبيو:
"لا يمكن إنهاء الأعمال العدائية والصراعات في المنطقة ما دامت الميليشيات المدعومة من إيران تواصل إطلاق الصواريخ والمسيرات من العراق، وتشارك في الإرهاب كما فعلت حركة حماس وحزب الله".</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/79789" target="_blank">📅 15:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79788">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
بعد الرفض الايراني.. ‏ترامب: لا داعي للعجلة في إرسال مفتشين إلى المواقع الإيرانية.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79788" target="_blank">📅 15:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79787">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🌟
‏ترامب: سيُسمح للمفتشين بالوصول إلى مواقع اليورانيوم الإيراني.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/79787" target="_blank">📅 15:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79786">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🌟
‏
ترامب:
سيُسمح للمفتشين بالوصول إلى مواقع اليورانيوم الإيراني.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79786" target="_blank">📅 15:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79785">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تراجع سعر برميل خام برنت إلى ما دون 75 دولارا لأول مرة منذ 27 فبراير.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/79785" target="_blank">📅 15:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79784">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وزير الخزانة الأمريكي: أي أموال يتلقاها الإيرانيون هي للإيرانيين، نسبة كبيرة جداً ستُخصص للأغذية والأدوية الأمريكية تحت إشراف وزارة الخزانة.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79784" target="_blank">📅 15:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79783">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuvrXClKnG5jlyuM-XmRzScRBsreXNXvXQDFiltir4975I7UAr3rcProXNcVJusz_n_lE8B3XPshHUm_1AWXjKIyHo9N1as4ItGN2I_k31WdRXhf7Qnaa3X_nAMMoo51Dj0Dcq5TEbiR6rhDqUCLmgdxm-VffykC6hHJKYuhqmEl-yskazSZt82F1UP0Y14XDOif6aDPjomBhhXXkEkD9B_Zwq2-fgaUDx8FfBwh5dbhjcjehRYMa32VXq3962NOKsVsrx-yqML5hAlKM2HgfrWPV41-YqEwHsb6qjmA5mbTl7-Q457CuM2JX3NKsSdc0IR2eDSfAlnWymeEdIw6xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
أبلغت إيران الولايات المتحدة أنه على الرغم من التقارير الإخبارية الكاذبة المثيرة للمشاكل التي تفيد بخلاف ذلك، "لا توجد رسوم عبور، ولا تكاليف تأمين، ولا أي رسوم أخرى من أي نوع تطلبها أو تتلقاها إيران على السفن التي تسافر عبر مضيق هرمز. إذا كانت هذه معلومات خاطئة، فستنتهي المفاوضات على الفور! بالإضافة إلى ذلك، لم تُقدم الولايات المتحدة أي أموال لإيران، أو تُفرج عن أي أموال منها لصالحها. سنُفرج عن بعض أموالها، التي نتحكم بها بالكامل، لمزارعينا ومربي الماشية لدينا، لشراء الذرة والقمح وفول الصويا والمزيد. هناك حاجة ماسة إلى الغذاء في إيران، وسنشتريه لهم حصريًا من الولايات المتحدة. شكرًا لاهتمامكم بهذا الأمر!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79783" target="_blank">📅 15:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79782">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🏴‍☠️
‏
وزير ما يسمى بـ"الحكم المحلي" الصهيوني:
قادرون على منع إيران من امتلاك أسلحة نووية ولكن واشنطن لم تسمح.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79782" target="_blank">📅 14:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79781">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇷
🌟
السلطات الايرانية:
أكثر من 3 ملايين زائر ايراني وصلوا إلى كربلاء المقدسة للمشاركة في مراسم عاشوراء. اليوم عبر 400 ألف زائر إيراني الحدود البرية إلى العراق.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79781" target="_blank">📅 14:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79780">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49e10fb40c.mp4?token=YQXxI2GO9XjelnUJ-WaIjD9lLESLKPsSWM_H9jheyt1KOjlVlCtcXptkrxpC1nZTLx-BIwXXFu6kUiZo6Hjaj8PdR-s1R8wtjpRl0l32hkQ_yHSmsjVD309__U1pON6Xijo5H33Of5Ukv8PDKImI92W0OJHKXBn3Y0xyAbPCx2Dz-0Sgw-tHLO_ntmTG-wiyq8BORTNTJ7-juRTHaDBneatPU611mQrvtxmRGw5yjaD0dBvytMrMCL1My_cEF8FAXqSJJ1wFGFln_GffuRxHfMf2JfsiZPXhKrzLnh6oUrvGMXmUYFTlqHGqlPweQ7lgtoQrar_zkmvvidwQk5-1QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49e10fb40c.mp4?token=YQXxI2GO9XjelnUJ-WaIjD9lLESLKPsSWM_H9jheyt1KOjlVlCtcXptkrxpC1nZTLx-BIwXXFu6kUiZo6Hjaj8PdR-s1R8wtjpRl0l32hkQ_yHSmsjVD309__U1pON6Xijo5H33Of5Ukv8PDKImI92W0OJHKXBn3Y0xyAbPCx2Dz-0Sgw-tHLO_ntmTG-wiyq8BORTNTJ7-juRTHaDBneatPU611mQrvtxmRGw5yjaD0dBvytMrMCL1My_cEF8FAXqSJJ1wFGFln_GffuRxHfMf2JfsiZPXhKrzLnh6oUrvGMXmUYFTlqHGqlPweQ7lgtoQrar_zkmvvidwQk5-1QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حريق هائل يلتهم مصنع في قضاء الشيخان التابع اداريا لمحافظة نينوى وتحتله ميليشيات البرزاني وضمته لمحافظة دهوك.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79780" target="_blank">📅 14:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79779">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇷
‏
نائب وزير الخارجية الإيراني:
لم يُعقد أي اجتماع مع غروسي في سويسرا، رغم طلبه. كما لا يوجد برنامج للوصول إلى المنشآت والمواد النووية التي تعرضت للهجوم. ستُدرس هذه القضايا وتُحل فقط في إطار الاتفاق النهائي ونتيجةً لإجراءات الطرف الآخر العملية برفع جميع العقوبات.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/79779" target="_blank">📅 14:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79778">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🌟
وكالة الاستخبارات والتحقيقات الاتحادية العراقية تلقي القبض على(25) شخصاً أجنبياً أثاروا مشاجرة في محافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/79778" target="_blank">📅 14:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79777">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🏴‍☠️
‏
وزير الحرب الصهيوني:
حتى لو كان هناك طلب أمريكي، فلن ننسحب من جنوب لبنان.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/79777" target="_blank">📅 14:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79776">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇶🇦
وكالة ‏رويترز: رئيس وزراء قطر يبحث في مسقط عقد محادثات بين إيران ومجلس التعاون والعراق حول هرمز.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79776" target="_blank">📅 13:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79775">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇶🇦
وكالة ‏رويترز:
رئيس وزراء قطر يبحث في مسقط عقد محادثات بين إيران ومجلس التعاون والعراق حول هرمز.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79775" target="_blank">📅 13:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79774">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇷🇺
‏
الكرملين:
الأسلحة النووية هي الضامن الوحيد لمنع حرب عالمية ثالثة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79774" target="_blank">📅 13:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79773">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🌟
وزير الخارجية الباكستاني:
التفاوض بين واشنطن وطهران يدور حاليا بشأن البرنامج النووي والأرصدة الإيرانية ولبنان ولن تكون هناك رسوم عبور لمضيق هرمز أو أذونات وتصاريح.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79773" target="_blank">📅 13:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79772">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حدث أمني في أنقرة</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79772" target="_blank">📅 12:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79771">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حدث أمني في أنقرة</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/79771" target="_blank">📅 12:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79770">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇫🇷
أ ف ب: رصد إصابة أولى بفيروس إيبولا في فرنسا.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/79770" target="_blank">📅 12:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79769">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5943b6171.mp4?token=FNGvHXoNUnlHyycwX3fgNalVJ6UbWkYPFl2Yk6FOCK79zHrgdfCzLTSY_b8n17EWPWzx2_NI3U2U1tiE-SxUlPXqbTGHvj-jECSEZv7zwN_0fMdV-7WzHk-M2-48bYXLGWPLqh0BkptgKnDtdDu1rxQ03yalo2olpxn6qPmYVba2y0mvCfiDc-DitULOjnma1YfJUXdBIGamGIRC-vtFScCyxvy8Gm7r3PLjnIY_xdxrrGmTCh6jJ6RnCu_q8mCcbmRVTt5tjoBQaI3fKNKM9r70x0C_GYmbx1h6tsaLaFafblJKQ4DhsUt9UZIVIIS2gycrPuCG896AU3t-T-0nUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5943b6171.mp4?token=FNGvHXoNUnlHyycwX3fgNalVJ6UbWkYPFl2Yk6FOCK79zHrgdfCzLTSY_b8n17EWPWzx2_NI3U2U1tiE-SxUlPXqbTGHvj-jECSEZv7zwN_0fMdV-7WzHk-M2-48bYXLGWPLqh0BkptgKnDtdDu1rxQ03yalo2olpxn6qPmYVba2y0mvCfiDc-DitULOjnma1YfJUXdBIGamGIRC-vtFScCyxvy8Gm7r3PLjnIY_xdxrrGmTCh6jJ6RnCu_q8mCcbmRVTt5tjoBQaI3fKNKM9r70x0C_GYmbx1h6tsaLaFafblJKQ4DhsUt9UZIVIIS2gycrPuCG896AU3t-T-0nUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
قصف أوكراني يستهدف مواقع في شبه جزيرة القرم الروسية
أوكرانيا تتلقى دعم من بريطانيا وفرنسا وألمانيا وباقي دول الناتو</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79769" target="_blank">📅 12:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79768">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇹🇷
هزة أرضية بقوة 4.9 ريختر تضرب سواحل ولاية موغلا التركية.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/79768" target="_blank">📅 12:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79767">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇸🇾
خلف البدلات الأنيقة والخطابات المنمقة والصور اللامعة التي جسدها الجولاني تقف حكومة لا تتردد في إرسال أبنائها إلى نبش القبور وارتكاب افدح صنوف الظلم ثم تتحدث عن القيم والأخلاق بوجه لا يعرف الخجل ؛ حيث يظهر الفيديو لحظة نبش أحد القبور واستخراج جثة أحد الأشخاص بحجة انتمائه للشبيحة في قرية عربين بريف دمشق.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/79767" target="_blank">📅 12:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79766">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🛫
الاتحاد الأوروبي بشأن الطيران: نصحت شركات الطيران بتجنب التحليق فوق إيران والعراق ولبنان، وتوخي الحذر في بقية أنحاء المنطقة.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79766" target="_blank">📅 11:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79765">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8n062vlMbTEF4Sjq1fXhx0ltLK8iwl4w54ACTNOe4KFTDKDYpLx0bzuhEEsgKT4Xjb9L4rKZowTEbr-exyeZ9K893f62bdET3kmBh7CusVk9_9ZXJUC_npFOmMrZvZF16DO3sM_v9bsaxXLHZTwXQUt1dd18sAS6iTecEoBcNPC0uPVjPbfRK3x3F2JouOa2zqlVduF5b8CZl6_FSZAjRaBk-t9htKgNB8CPPKBSg3GDf_s688tQZWrVNTf9BKyAbpTgx749NAd-D-35EGxvfGaztXIBCl5wuwWmlrRXv8USP1EpHzWc4SfwM_jU_Qlota1E3WfKE89Gc-pZzhkwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
غضب واستياء شعبي واسع في شارع الكفاح كعبة المواكب الحسينية في بغداد بعد صدور توجيهات تقضي بتضييق ومنع نزول المعزّين إلى الشارع حيث يُعد هذا الشارع أكبر وأهم حاضنة للمواكب الحسينية في العاصمة وشاهداً على أضخم التجمعات العزائية ؛ الأمر الذي أثار موجة من التساؤلات حول القرار الغير مألوف بحق شارع ارتبط اسمه بالشعائر الحسينية لعقود طويلة ؛ متسائلين عن أسباب هذا الإجراء وما إذا كان يمثل بداية لسياسة التضييق على المواكب الحسينية والشعائر الدينية.
🔻
نسخة منه إلى القائد العام للقوات المسلحة</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79765" target="_blank">📅 10:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79764">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔻
🇰🇵
مشاهد بثها الإعلام الكوري للزعيم كيم جونغ أون أثناء حضوره حفل تدشين السفينة الحربية تشوي هيون في مدينة نامبو الساحلية، وهي إحدى السفينتين الحربيتين من فئة 5000 طن ؛ حيث أكد أن البحرية ستمتلك أسلحة نووية وستُكلف هذه المدمرة بمهمة الدفاع عن الساحل الغربي للبلاد.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79764" target="_blank">📅 10:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79763">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFuTUrPIz1WbZaCzKyb_vusYQckXo3-wQ24ymmRrf3qDwryk7G3t8tYiRHUJAM6rM9ofqyg7G7C6JnFCViIXdHS7y9NkryMVEPYSnhTTene-mJ1bFoBtRYcWAwDdXSNgBAIanAx3bKZyn2dXV7M_DSXQk0-NiJ-0J8_M_QEdIdJkPdzVfo5N29e5vCm62-0-X1gBSKj_E-sMfTJ2x_wQ_VvD1UE28L2dWswFp4xdYdN6hDw31WJQSXBPiGR0ba6NDiNaqwEVpAebYS4iwwkKqUIiDK9rjA5X3UvMzpZv7Uw_-qp9ZB_cNM4a3lVjY235YDjIrkjLySjhRjRKoPBZYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
شركات النفط الكبرى لا تخفض أسعارها في محطات الوقود بما يتماشى مع الأسعار المنخفضة بشكل حاد التي تدفعها مقابل النفط.
هذه الأسعار تنخفض بسرعة كبيرة! بمعنى آخر، يتم "ابتزاز" العملاء.
لقد أوعزت إلى وزارة العدل أن تبدأ فورًا في التحقيق في هذا الأمر. يجب أن تبدأ أسعار البنزين في الانخفاض بسرعة أكبر بكثير مما أراه!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79763" target="_blank">📅 09:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79762">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9gWGDiTWsDor3CbqdsEJ6KZ56Qt_u20mu5fp-TofF2vr32Lr5cvvOAirhgsAs7JWMKkenVEyM9ut_4KAszX6wllBbrBTqgP4YfO-FNV9NDfKR7IGE8xqHX6643CUT2CpWka1-7rR63Jh4GrOEXPhw7hvD55xTJsk24CMV6OX5-BPJXh47N7aHkPD8p9khlR0rBrBo0dXdtd6LxcdlZQjQ3Ri3nrmXdTTwpNSOI9J0Yw7gV5aM38uO4oR6sRUy0jg8rZ9diO-ONfk_sLvgKfG_pK4D2vdq4EXWlridipII-GB1sDQ7UbVyniuZLFpqpbavfCOsgzYHXPjK9UfrR0-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
إذن، إيران على وشك السقوط، مستعدة للهزيمة، مستعدة لتقديم أي شيء تقريبًا، ولأول مرة منذ عقود، تحترم الولايات المتحدة ورئيسها، أنا، ويقرر مجلس الشيوخ الأمريكي التصويت على قانون صلاحيات الحرب في توقيت سيئ وبلا معنى، ليخبروا الراعي الأول للإرهاب في العالم أن الولايات المتحدة لا تحب ما أفعله بها، ويجب أن أتوقف، وبذلك يكونون قد قدموا العون والدعم للعدو. أربعة جمهوريين خاسرين صوتوا مع الديمقراطيين، وسألت إيران شعبي: "ماذا يعني كل هذا؟" لقد جعل هؤلاء السيناتورات مهمتي أكثر صعوبة، لكنني سأنجزها، بطريقة أو بأخرى، لأنني دائمًا ما أنجزها!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/79762" target="_blank">📅 06:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79761">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9319476213.mp4?token=dTV_sn-n4wBmDaX7b4CQg5l5NdFFE_-LZNuaa2V8JOkd-BQzbYX3kmLZ5oNOxE3QPBUy4jQJUYoRx-BBiDy2Pjs63Akxt1uVDSXAVZ5sYUapYEWZginlSSA76-FoF4okPmrcT8ED3nWSbT3CpZO2zdeOM9Pcla5jv4l1t1PUV5jrD9gzC_e_YuXmqgbNU6W4ltxwO2paxn0lEekBMFZJmzGGF-3iChsgR0uJZ8zZwwdZI2o7dwI0auzzQE1mq8F-DSsZp9U1upC2w5FIxcIgbK0bY200ZFoJ07qkKNVQdJFfFXAfzHfValz58e6mU0hwsqtEY0ym4k8go3MB81Atx5VIxrbP44qUHhl9ajZZjxctQJagEZd1mFI17F8S-LnPCrdwf4NkuLJGOd8axCXlQtnmREQsB5gAhrBOyt6IK1qhObMLM7l_zdmCFPm7MGTR77mJ18SqRrOU3pOaKLXqgG640EHMFL-9Pfqp0E_nZKV_jEm10rUJHvsDJLc0XjehpCkiy_ELLOXPC9J9wN63zRuMPESmcwL5Q_lG82CJiezVxw9_OrFqbOX22Dpej80jCcQkIqSjK7Xad4UU7mFjU29Bqq9uW6qyNgTvDwRYlhO81OYa_aCk5ruCgK1gHP_29_xoTNO43jmMyCiBZg780QFNm4pc12GAF6W7awJRFZ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9319476213.mp4?token=dTV_sn-n4wBmDaX7b4CQg5l5NdFFE_-LZNuaa2V8JOkd-BQzbYX3kmLZ5oNOxE3QPBUy4jQJUYoRx-BBiDy2Pjs63Akxt1uVDSXAVZ5sYUapYEWZginlSSA76-FoF4okPmrcT8ED3nWSbT3CpZO2zdeOM9Pcla5jv4l1t1PUV5jrD9gzC_e_YuXmqgbNU6W4ltxwO2paxn0lEekBMFZJmzGGF-3iChsgR0uJZ8zZwwdZI2o7dwI0auzzQE1mq8F-DSsZp9U1upC2w5FIxcIgbK0bY200ZFoJ07qkKNVQdJFfFXAfzHfValz58e6mU0hwsqtEY0ym4k8go3MB81Atx5VIxrbP44qUHhl9ajZZjxctQJagEZd1mFI17F8S-LnPCrdwf4NkuLJGOd8axCXlQtnmREQsB5gAhrBOyt6IK1qhObMLM7l_zdmCFPm7MGTR77mJ18SqRrOU3pOaKLXqgG640EHMFL-9Pfqp0E_nZKV_jEm10rUJHvsDJLc0XjehpCkiy_ELLOXPC9J9wN63zRuMPESmcwL5Q_lG82CJiezVxw9_OrFqbOX22Dpej80jCcQkIqSjK7Xad4UU7mFjU29Bqq9uW6qyNgTvDwRYlhO81OYa_aCk5ruCgK1gHP_29_xoTNO43jmMyCiBZg780QFNm4pc12GAF6W7awJRFZ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجارة البحرية البريطانية: وردت أنباء عن سيطرة أشخاص غير مصرح لهم في السواحل الصومالية على سفينة شحن تم تحويل مسارها إلى داخل المياه الإقليمية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/79761" target="_blank">📅 03:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79760">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">توقف سكك الحديد في عموم المانيا بسبب اضطرابات في الراديو الرقمي للسكك الحديدية</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/79760" target="_blank">📅 01:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79758">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">عاشوراء عهدٌ متجدّد؛ أن نبقى ثابتين على الحق، أقوياء في الموقف، أوفياء للمبدأ، ما بقينا
عاشورا پیمانی همواره استوار است؛ اینکه تا زمانی که زنده‌ایم، بر حق استوار بمانیم، در موضع خود نیرومند باشیم و به آرمان و اصول خویش وفادار بمانیم
Ashura is a renewed covenant: to remain steadfast upon the truth, strong in our stance, and faithful to our principles for as long as we live</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/79758" target="_blank">📅 00:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79757">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🌟
مجلس محافظة ذي قار يعلن تعطيل الدوام الرسمي يوم غد الأربعاء .</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/79757" target="_blank">📅 00:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79756">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🌟
العتبة الحسينية المقدسة:
لن نسمح بأي شكل من أشكال الاعتداء أو التجاوز على كرامة الزائرين مهما كانت الأسباب.
وفيما يتعلق بالحادثة  التي شهدتها مدينة كربلاء المقدسة مؤخراً والمتضمنة تجاوز عدد من الأشخاص على مجموعة من الزائرين، فإن الجهات المختصة سارعت إلى إحتواء الموقف بشكل فوري واتخاذ الإجراءات اللازمة لمنع تفاقمه، كما تؤكد العتبة الحسينية المقدسة أنها لا تسمح بأي شكل من أشكال الاعتداء أو التجاوز على كرامة الزائرين مهما كانت الأسباب.
﻿</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/79756" target="_blank">📅 23:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79755">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⭐️
على غرار سياسة آل خليفة المتصهينة في محاربة الشعائر الحسينية..
حكومة آل صباح في الكويت تجبر مؤسسي "حسينية آل ياسين" على إيقاف جميع فعالياتها الحسينية وإغلاقها حتى إشعار أخر.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/79755" target="_blank">📅 22:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79754">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">المتحدث باسم وزارة الأمن الداخلي الأمريكية:  الولايات المتحدة تخفف القيود المفروضة على المنتخب الإيراني المشارك في كأس العالم، مما يسمح للفريق بالسفر قبل يومين من مباراته القادمة.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/79754" target="_blank">📅 22:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79753">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🏴‍☠️
خرق صهيوني جديد لوقف إطلاق النار..
مسيرة إسرائيلية استهدفت سيارة على طريق الخردلي بجنوب لبنان من دون أن تصيبها.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/79753" target="_blank">📅 21:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79752">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5161524b76.mp4?token=m9vbDlDLvTFz4B3pCmPYjfNWT08TJ4lbZg2kKCO5Yv6yKYFixJzQjSSw1J6SCD2KU_otIfd4o1raqsERY7J--N_LyhMBon3DGR8DhwlSI6jdmBP-iUDSqwnnAFkh8ftt5KxJlWWjB0RE0NsX9BDS8ltpjYRG7C0WRk0JjSMENH8V_Hj0Xh5pnovh7QqHXfA0t4i4cPLN01T3xpZM6GG4zHBXZnVszNjsoS8hq6YAhygFYSL4rGEnXs-IfRGFQbyvgdKQwxXape97fU1zkFiKMibDsDBvwWmC5O53zVtyIF1pl4Y46y1jsjPXeHb9E-cf1YFe_DrgnPfMd3IjWeT63w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5161524b76.mp4?token=m9vbDlDLvTFz4B3pCmPYjfNWT08TJ4lbZg2kKCO5Yv6yKYFixJzQjSSw1J6SCD2KU_otIfd4o1raqsERY7J--N_LyhMBon3DGR8DhwlSI6jdmBP-iUDSqwnnAFkh8ftt5KxJlWWjB0RE0NsX9BDS8ltpjYRG7C0WRk0JjSMENH8V_Hj0Xh5pnovh7QqHXfA0t4i4cPLN01T3xpZM6GG4zHBXZnVszNjsoS8hq6YAhygFYSL4rGEnXs-IfRGFQbyvgdKQwxXape97fU1zkFiKMibDsDBvwWmC5O53zVtyIF1pl4Y46y1jsjPXeHb9E-cf1YFe_DrgnPfMd3IjWeT63w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترامب: نعمل على اتفاق رائع بعد أن تم القضاء على كل شيء في إيران وهي ليست في موقف تفاوضي جيد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/79752" target="_blank">📅 20:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79751">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏ترامب:  لن يُسمح لإيران بامتلاك السلاح النووي.  ‏في حال اختارت إيران المتاعب فعليها السعي لامتلاك السلاح النووي.  ‏هناك تراجع في أسعار النفط.  المفتشون سيكونون على الأرض في إيران في الوقت المناسب.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/79751" target="_blank">📅 20:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79750">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/236a2e1e8d.mp4?token=ZboWzYB_SQexfVCujlkCswyCZ9sGBOzcnt_DELvB074st60bSEIADCWuyT5_2590ffAz5F2ZG76-ODRFHNkzJIDY9lDea1Cgp6rERtR7WbMc-Kc76uJzcg819y2oROWvOb6BhX8nMMI1qvowQQytEubTqwBFllpGssOFp_aAXNGX5D6pMsGE11defPLdTOtTreCuzjjYOMiPDXBaIB6Rmv7oxvj4wayTbpLGm8yekoKJfrOzoOpfWnMawXfTtwY1iLxHtIncixb39jOIlf-rLlFmtt9UxmRX3EHRmgF8WtnFlAr4m-v_WUl2KrQCzLKztAgldtd4MXMLnxY6OYn-xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/236a2e1e8d.mp4?token=ZboWzYB_SQexfVCujlkCswyCZ9sGBOzcnt_DELvB074st60bSEIADCWuyT5_2590ffAz5F2ZG76-ODRFHNkzJIDY9lDea1Cgp6rERtR7WbMc-Kc76uJzcg819y2oROWvOb6BhX8nMMI1qvowQQytEubTqwBFllpGssOFp_aAXNGX5D6pMsGE11defPLdTOtTreCuzjjYOMiPDXBaIB6Rmv7oxvj4wayTbpLGm8yekoKJfrOzoOpfWnMawXfTtwY1iLxHtIncixb39jOIlf-rLlFmtt9UxmRX3EHRmgF8WtnFlAr4m-v_WUl2KrQCzLKztAgldtd4MXMLnxY6OYn-xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
المراسل: يقول الإيرانيون إنه لا توجد زيارة مقررة للمفتشين. هل هذا جزء من اتفاقكم؟  ‏
🌟
ترامب: إنهم مخطئون. إنهم مخطئون. وهم يعلمون أنهم مخطئون. لو كانوا على صواب، لكنت ألغيت الاجتماعات فوراً.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/79750" target="_blank">📅 20:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79749">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d953889d0d.mp4?token=C_GXJJs_EEsP7WSmqz0bhgIBc1Myge2nVYo0LSkz-cSINo2aQbmoc2jcYIN0eQ2nbcCg2HGwm1kmaDVl_QOW-NFa2zUW90TSFn1FBqaeZI4IwJG_VkBCt6SIxlbv9SV6ynLVRojEeqfh7BgZiS8HzlYTq1xwcChTSn1KFKipF_0FH__ku9oeuoB1_r9_oW-cretborc9RneG_m_jl1Pf2ILs2nr9nb0Jm_DQ8TRQyTkPoCJC9RsCj3HeysvDmLKRmjq8s844TrDBeJPIZkEd8CUrCN2m4054bf-CFsT0_a0gxpEDHyqznsyW_xlRTmQrSWGL7dqp2dDW80mXz5blVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d953889d0d.mp4?token=C_GXJJs_EEsP7WSmqz0bhgIBc1Myge2nVYo0LSkz-cSINo2aQbmoc2jcYIN0eQ2nbcCg2HGwm1kmaDVl_QOW-NFa2zUW90TSFn1FBqaeZI4IwJG_VkBCt6SIxlbv9SV6ynLVRojEeqfh7BgZiS8HzlYTq1xwcChTSn1KFKipF_0FH__ku9oeuoB1_r9_oW-cretborc9RneG_m_jl1Pf2ILs2nr9nb0Jm_DQ8TRQyTkPoCJC9RsCj3HeysvDmLKRmjq8s844TrDBeJPIZkEd8CUrCN2m4054bf-CFsT0_a0gxpEDHyqznsyW_xlRTmQrSWGL7dqp2dDW80mXz5blVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب:  لن يُسمح لإيران بامتلاك السلاح النووي.  ‏في حال اختارت إيران المتاعب فعليها السعي لامتلاك السلاح النووي.  ‏هناك تراجع في أسعار النفط.  المفتشون سيكونون على الأرض في إيران في الوقت المناسب.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/79749" target="_blank">📅 20:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79748">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏ترامب:
لن يُسمح لإيران بامتلاك السلاح النووي.
‏في حال اختارت إيران المتاعب فعليها السعي لامتلاك السلاح النووي.
‏هناك تراجع في أسعار النفط.
المفتشون سيكونون على الأرض في إيران في الوقت المناسب.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79748" target="_blank">📅 20:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79747">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13c3f6bff2.mp4?token=rt8HrvF-xumz-cHcp4t_j3p1g_LnpJ4BQZz_7Ran90XlWKiEEtJBJ0Z5587uhoHnmg91vLEL5ImhbD9YVdVAtLPNxlW0EOhkcSr101ooBjZlpaodVmTFOim6bULDLBMSf7BlkL-j2lShASTnvFScfrcUQbIRx5RP59LUqcZz3nQgrcqRe2e3CrbeioK3zs0mfczuFtY9EPcfULWY4h_p-DZ4XG3mtChxnUVxQspQBe8pWjyDm8-Iid09VwYYnxO3TBik2L6jILLZxrBnRAyudU0xX31udg6v16Tf5foIFbeRW1ACqBIVFvEUKzS5Y9dXMEKf0HQz6bgq5zndrVXCMR4NYOHRPpsDTIGjPWLiWPB3wSbOd-C2uJSkh_v45G3pFbnOlDe1HF5_hpaDG-rM_Z9ae122fN4y-K201ztGe-Ymm7eBn1TRCYLQ5zMylzfMiaX2nk1dVbpUiVS6CBrcGwYqJM6aP5ieAt52GyxvcFtdMn5xBulDhxTH7-itKeezymiJQjK-HtRypcD6DlK3ZyLel0683XZvEb9j3IwCsuBlKS2loEVwAhQ8M1s3SHEir_13RIvfl5IoTOs9zp4bgNE__jgj6PLExLo-C_uqpqpRHHAqQXQBkWdATfLv9XS4Nh0epKpWWw0Kp-3AeJVauETX-sqJY51DABFIa9YKwQE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13c3f6bff2.mp4?token=rt8HrvF-xumz-cHcp4t_j3p1g_LnpJ4BQZz_7Ran90XlWKiEEtJBJ0Z5587uhoHnmg91vLEL5ImhbD9YVdVAtLPNxlW0EOhkcSr101ooBjZlpaodVmTFOim6bULDLBMSf7BlkL-j2lShASTnvFScfrcUQbIRx5RP59LUqcZz3nQgrcqRe2e3CrbeioK3zs0mfczuFtY9EPcfULWY4h_p-DZ4XG3mtChxnUVxQspQBe8pWjyDm8-Iid09VwYYnxO3TBik2L6jILLZxrBnRAyudU0xX31udg6v16Tf5foIFbeRW1ACqBIVFvEUKzS5Y9dXMEKf0HQz6bgq5zndrVXCMR4NYOHRPpsDTIGjPWLiWPB3wSbOd-C2uJSkh_v45G3pFbnOlDe1HF5_hpaDG-rM_Z9ae122fN4y-K201ztGe-Ymm7eBn1TRCYLQ5zMylzfMiaX2nk1dVbpUiVS6CBrcGwYqJM6aP5ieAt52GyxvcFtdMn5xBulDhxTH7-itKeezymiJQjK-HtRypcD6DlK3ZyLel0683XZvEb9j3IwCsuBlKS2loEVwAhQ8M1s3SHEir_13RIvfl5IoTOs9zp4bgNE__jgj6PLExLo-C_uqpqpRHHAqQXQBkWdATfLv9XS4Nh0epKpWWw0Kp-3AeJVauETX-sqJY51DABFIa9YKwQE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-06-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79747" target="_blank">📅 20:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79746">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bd43a7e5.mp4?token=I1dZkERBq4IVtwD5VW9LqAhMOipYd-Zkcsy6X3N2pnAMOlFvGG-VFvDVRFGuf2dshJRTK0SxqaCjY4Jbfj3lQpLgvss0xblpmsV7jKjKKBSTPc-BjLLptuXHsvJ8vluWnAARRodEGGxKSiFBifoC2vHUYjhdHNQWyHa_gXXWFsydRO2Hn_rrYWPpOtXkQiNt4BqiDLax8ZDWUl9EuWPW73aLnMkJ3fG-pGKAyxkS1vQvwzD5yeZcTC1IklDAwWmZxgCkcy4NbBPDBUgIS8I17O0M5vpr0gnwXBkmYt5JFXT0mXwH3ipkYdDhjYii3FLhJbVajQZTjpZJUriY5c33UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bd43a7e5.mp4?token=I1dZkERBq4IVtwD5VW9LqAhMOipYd-Zkcsy6X3N2pnAMOlFvGG-VFvDVRFGuf2dshJRTK0SxqaCjY4Jbfj3lQpLgvss0xblpmsV7jKjKKBSTPc-BjLLptuXHsvJ8vluWnAARRodEGGxKSiFBifoC2vHUYjhdHNQWyHa_gXXWFsydRO2Hn_rrYWPpOtXkQiNt4BqiDLax8ZDWUl9EuWPW73aLnMkJ3fG-pGKAyxkS1vQvwzD5yeZcTC1IklDAwWmZxgCkcy4NbBPDBUgIS8I17O0M5vpr0gnwXBkmYt5JFXT0mXwH3ipkYdDhjYii3FLhJbVajQZTjpZJUriY5c33UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇮🇷
‏رئيس الوزراء الباكستاني شريف:  أبلغوا رسالتي إلى القائد الأعلى بأن إيران تمكنت من تحقيق وقف إطلاق النار ومذكرة التفاهم بكرامة.  ‏أعتقد أن إيران ستتحول قريباً إلى واحدة من أسرع الاقتصادات نمواً في العالم.  ‏لا تتضمن مذكرة التفاهم هذه أي ذكر للصواريخ الباليستية،…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79746" target="_blank">📅 20:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79745">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKMVOQLRwrDHoXn6UB4KwXR062706lEs1ck7NTQ7Dzitu7mL0NX5izgq7kPxIXlTODjGX7j6O3aERsFqP3veHFX42U4zR02yK0O0wTs-sHrXwzFtRUyhoIGaNFs6Yckp5xJpSVdc6fc8aWyJDweL35FVyJksVM-wkbe-7MD6t5XMXfDPX0zPbfFsQIYtDe_InvM5U7ZL12GgiwIa8FAf4BCesNs4gAiDDa2TQgE5R1wJJwdA_0XHqPoCyWU9pfxeSX9TkkMro5k9vlgfhkQEj1u2yExdUcFT21WUY2xBUQoOeHLLrJo6PrO4_qWxCBQ3gSsqWy4Gu4dIDKH9zMe57A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد زلزال هيكلة وزارة النقل العراقية ؛ هل انتهت أيام شاكر الزبيدي في الوزارة ؟!</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/79745" target="_blank">📅 19:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79744">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/680209a07d.mp4?token=n2zGA1ninyA0Jw08n1KqBmwIwK85YVd3zNMB1GDovuBA8vVRslaMJy1S-DcJ4zqD5dgQ974InHov5YQuAlFuVk5ohK-3Q-AcUCQlTObGF70lDwDeNgK-aKA3SkhcuOL1lR-01xg2BLPhuqBlH4oCUde3tMOmqjtfF7qjHxKWvaQJ9vZobnZN01w9JYfAtil6AxKcx0yHQz7zx3KyeUJv8wgOAfU496akkzJCVuoXTClS-0zaSbxnpHGbnYdS6OJlXiuya___i_SHaHcvEMz-foMsZYSv3uNyi1m_7vrkWuDa6TuhUY0gbV8chhjkxI5dz88VlytVqlJVJbYB_whhY7Tl87drv9ft1eOJpEAyS4poHg-0D1Kq_Fk3ElrmB5_rClma6xZpBzJ3U4gs5OF2sNwT1GTNo_mgT2l_stnGlHmPpk0fv9o0ZJ_w3G3SJD1yv44a6TTCANrTcYY5RvGiFY3uLG7sM-FS8-R7xUhO8rxWrE-L9Eex3XL34y_jSBAMv0RrI30fKOsuhka4PFmCPfitb9M0ORUPkjBG26IVby0F5ciJ9MePeD-WViO0dULvqNYnTLKQw7Q8qAxNuusQh6TJpkrblaxueOOAvDz6c4IAwzvmUZ2RwYp-9DWQ-yfBRN6t1g031-d6cC_pIUrvJ6PILevzyODQUXpGHFjHhXs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/680209a07d.mp4?token=n2zGA1ninyA0Jw08n1KqBmwIwK85YVd3zNMB1GDovuBA8vVRslaMJy1S-DcJ4zqD5dgQ974InHov5YQuAlFuVk5ohK-3Q-AcUCQlTObGF70lDwDeNgK-aKA3SkhcuOL1lR-01xg2BLPhuqBlH4oCUde3tMOmqjtfF7qjHxKWvaQJ9vZobnZN01w9JYfAtil6AxKcx0yHQz7zx3KyeUJv8wgOAfU496akkzJCVuoXTClS-0zaSbxnpHGbnYdS6OJlXiuya___i_SHaHcvEMz-foMsZYSv3uNyi1m_7vrkWuDa6TuhUY0gbV8chhjkxI5dz88VlytVqlJVJbYB_whhY7Tl87drv9ft1eOJpEAyS4poHg-0D1Kq_Fk3ElrmB5_rClma6xZpBzJ3U4gs5OF2sNwT1GTNo_mgT2l_stnGlHmPpk0fv9o0ZJ_w3G3SJD1yv44a6TTCANrTcYY5RvGiFY3uLG7sM-FS8-R7xUhO8rxWrE-L9Eex3XL34y_jSBAMv0RrI30fKOsuhka4PFmCPfitb9M0ORUPkjBG26IVby0F5ciJ9MePeD-WViO0dULvqNYnTLKQw7Q8qAxNuusQh6TJpkrblaxueOOAvDz6c4IAwzvmUZ2RwYp-9DWQ-yfBRN6t1g031-d6cC_pIUrvJ6PILevzyODQUXpGHFjHhXs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
🌟
من جرائم العدو الصهيوأمريكي في حرب رمضان..
توثيق جديد يظهر لحظة تنفيذ غارة على مدينة لامرد في محافظة فارس الإيرانية؛ ماأدى إلى إستشهاد عدد من المدنيين أثناء مرورهم بالقرب من مكان القصف.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/79744" target="_blank">📅 19:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79743">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd98c729d.mp4?token=aJwlVas5Lzc2iSEq3ejyLifjMfm3AjUu9rm3sw8BqhCcXKJ_el5i23iHT3Q6FJpmYhnEKK7dOUCgqKGrpn_D9uXj4kagTNHWiNvuzobh9HXiAfEz-tAu6N3dSl5F1v7c79MJpq7YsO7bLXIoJNwZrXAuPRHScJP20pZWMRiwgO4uz0keGU_BbF8mTQGUjxFeC1maEdNAADgt7UoHSD9hGkw09CIFnhhsNftxHCMQ0ntJOJEZy0Utn2ZFD0k62SY76Z6U-1xwgq0R0yFEXWhHX1D1A9hTX-qP1j2heTd-w02We7yMYHrbMx48m5aotQgwYl4edwN6sPuH0hMvK-eH0Fxkk_4qTqxcanS1M570_hwgMQ-N67cMPtNsi_5BZPJuAjlbmjs3S1fPLLSUKaVrlWQrSueh0XDhsDACdjscexaRVFjfOVPLTs_6r_hvmuuaUWtQ3tMgT7kSw7pX8Ooqe7NKVS1pjR431KLpXwQckU7ydkK1eXNrzV2auo-bJb8gzWoaNhqnPbdDDCupVMaUrM4w_6xkBY-R_Y_09SXDRLvxP0dbnr7VIEqedNLrq3V-cTXzvzPlQSaSVNIEHTxFwSNhhOUqbq-hGzkVJT936lhNwljL1Z8A73EgJMnpdgLi43hUqmVQIlsuE00nd-F62ZPCowdfaajWqSuPeFFV8IY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd98c729d.mp4?token=aJwlVas5Lzc2iSEq3ejyLifjMfm3AjUu9rm3sw8BqhCcXKJ_el5i23iHT3Q6FJpmYhnEKK7dOUCgqKGrpn_D9uXj4kagTNHWiNvuzobh9HXiAfEz-tAu6N3dSl5F1v7c79MJpq7YsO7bLXIoJNwZrXAuPRHScJP20pZWMRiwgO4uz0keGU_BbF8mTQGUjxFeC1maEdNAADgt7UoHSD9hGkw09CIFnhhsNftxHCMQ0ntJOJEZy0Utn2ZFD0k62SY76Z6U-1xwgq0R0yFEXWhHX1D1A9hTX-qP1j2heTd-w02We7yMYHrbMx48m5aotQgwYl4edwN6sPuH0hMvK-eH0Fxkk_4qTqxcanS1M570_hwgMQ-N67cMPtNsi_5BZPJuAjlbmjs3S1fPLLSUKaVrlWQrSueh0XDhsDACdjscexaRVFjfOVPLTs_6r_hvmuuaUWtQ3tMgT7kSw7pX8Ooqe7NKVS1pjR431KLpXwQckU7ydkK1eXNrzV2auo-bJb8gzWoaNhqnPbdDDCupVMaUrM4w_6xkBY-R_Y_09SXDRLvxP0dbnr7VIEqedNLrq3V-cTXzvzPlQSaSVNIEHTxFwSNhhOUqbq-hGzkVJT936lhNwljL1Z8A73EgJMnpdgLi43hUqmVQIlsuE00nd-F62ZPCowdfaajWqSuPeFFV8IY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇮🇷
‏
رئيس الوزراء الباكستاني شريف:
أبلغوا رسالتي إلى القائد الأعلى بأن إيران تمكنت من تحقيق وقف إطلاق النار ومذكرة التفاهم بكرامة.
‏أعتقد أن إيران ستتحول قريباً إلى واحدة من أسرع الاقتصادات نمواً في العالم.
‏لا تتضمن مذكرة التفاهم هذه أي ذكر للصواريخ الباليستية، ولم تكن مطروحة على الطاولة أو جدول الأعمال مطلقاً. الجانب الإيراني لم يرغب في مناقشتها.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79743" target="_blank">📅 19:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79740">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2660a35f99.mp4?token=XdHXwuA9czBjat7WI8I8CmMa59z_9UaJf-2gOR0JkMl2cSbp-phY6Zw4aPm3zaZAiOURXSQozqZkWVvCNo63e0Hqg-jgPW9dp4TvETmrUXpdM3r4wVVJDtKJ-zN4iCikfE6-C_akrvv-G89Q1Fpc2gOhLc91tXsXn8wXt5o-01i7aOsUiGGmlU660Y4l4khOmGQx4pbmHGqONg8XYd1uRafbx03F5VZ8S4Zvxk_0AirZN5hm5n4p2eGEG9FN09duF589dwQ5uzORtav9U6x5Y18p8dVG7l1d2XD8M5YUYA_hy7-BpYoNz7hDSAV21h9qxGLpT1yXdev4ZCnCTbNuGwEQMjWBhV2OFjbeKpetWm_6xOlbo_US-zUvthv4HREuxER9kS3HQgACoPZzRouOaXyvo9_zB1e0I8QngZOeTO2TJ5bf2MDiOYYF4MffPIwvQdPGacsNK9o4Cbtm5q0qRwAVzd_Amva-kKvy1zfxM8J3wHwcGcbycte6BCMQsHqYv5M7PIxYv9odnsRxVf5SnB7y6aeY0B_kgZPNsmZMIgU-K9t8rwfQNpAyuDWq0asZ4eWvGot9PEM5X_rCGWu06s5rKNQGFP73KaUkCqe1qVKjCkBICWAsoQu3xa_jAmMo89Ml_C3MbX71C1Vtp-SZ47xW9gLKFgEUyosKQ1bFDBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2660a35f99.mp4?token=XdHXwuA9czBjat7WI8I8CmMa59z_9UaJf-2gOR0JkMl2cSbp-phY6Zw4aPm3zaZAiOURXSQozqZkWVvCNo63e0Hqg-jgPW9dp4TvETmrUXpdM3r4wVVJDtKJ-zN4iCikfE6-C_akrvv-G89Q1Fpc2gOhLc91tXsXn8wXt5o-01i7aOsUiGGmlU660Y4l4khOmGQx4pbmHGqONg8XYd1uRafbx03F5VZ8S4Zvxk_0AirZN5hm5n4p2eGEG9FN09duF589dwQ5uzORtav9U6x5Y18p8dVG7l1d2XD8M5YUYA_hy7-BpYoNz7hDSAV21h9qxGLpT1yXdev4ZCnCTbNuGwEQMjWBhV2OFjbeKpetWm_6xOlbo_US-zUvthv4HREuxER9kS3HQgACoPZzRouOaXyvo9_zB1e0I8QngZOeTO2TJ5bf2MDiOYYF4MffPIwvQdPGacsNK9o4Cbtm5q0qRwAVzd_Amva-kKvy1zfxM8J3wHwcGcbycte6BCMQsHqYv5M7PIxYv9odnsRxVf5SnB7y6aeY0B_kgZPNsmZMIgU-K9t8rwfQNpAyuDWq0asZ4eWvGot9PEM5X_rCGWu06s5rKNQGFP73KaUkCqe1qVKjCkBICWAsoQu3xa_jAmMo89Ml_C3MbX71C1Vtp-SZ47xW9gLKFgEUyosKQ1bFDBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
محافظة السماوة جنوبي العراق تخرج عن بكرة أبيها في عزاء الإمام العباس (عليه السلام) باليوم السابع من شهر محرم الحرام.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/79740" target="_blank">📅 19:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79739">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a83af36368.mp4?token=luevC_sH8DcDWTBdcVDs0IoNpFT8u4EjuJEC6maRS1Y3FOyVUWFd36YsumFHO2YjGdYqUCcPQGQX048XSrtDqY0qICIE3kkn1XRmhXckaN8oMUfZ6LaKJeel2JHXmUmo93GTxeKz7raCqEESPbH13NpfksA5_Dz-BJ_oHTp3k_mo1vfjII8CJDnddSTGfaZNbYa2rL3OSkxBAC0_nR73X3DEkaEzwoE0WWRLk5C2AS5U0F9OLC4gGgDAa3CZx0OoWghAZJKFlGzNEM4A9CSUFSogRZnkRud3Us1bVWTqS_cbmgP_6lwxveLZZFVhzaKcM2n1HNNDmTagNIi8LjpdeoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a83af36368.mp4?token=luevC_sH8DcDWTBdcVDs0IoNpFT8u4EjuJEC6maRS1Y3FOyVUWFd36YsumFHO2YjGdYqUCcPQGQX048XSrtDqY0qICIE3kkn1XRmhXckaN8oMUfZ6LaKJeel2JHXmUmo93GTxeKz7raCqEESPbH13NpfksA5_Dz-BJ_oHTp3k_mo1vfjII8CJDnddSTGfaZNbYa2rL3OSkxBAC0_nR73X3DEkaEzwoE0WWRLk5C2AS5U0F9OLC4gGgDAa3CZx0OoWghAZJKFlGzNEM4A9CSUFSogRZnkRud3Us1bVWTqS_cbmgP_6lwxveLZZFVhzaKcM2n1HNNDmTagNIi8LjpdeoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
طيران حربي أمريكي يحلق بكثافة وإرتفاع منخفض في سماء محافظة ديرالزور السورية بالقرب من الحدود العراقية.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79739" target="_blank">📅 18:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79738">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-utaPP_XhKvudarFU5iiyQlDYTldXrGZDjkboisW4YF5qx-lGshsi_9Z00tWTYO-Z3mxyHzrYg2MWPqIoIIBXkk3NvKentKeaCbACSvHu98MtyLMgRvy_k5_2Z53bBQ8eamUxSvob9tf7PyulCQzonXqzkJGIgxNGwjaqrJ9pG2usKrFV7Ha1PCBcVAWHTOKpw1ivd1puGXQBOOER9yJ5O7ng-aXsmOh380fFvrJn_s0qvNElrZYCJ6zNAWD9n6InS5_8C_6-GYuhlL6akZ1EDWPKE_CUAdQHUiLJafeqgT8DHZeU9kzCLqfW_qAfO3_qFvTIDK_61o8z15q16ZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب:
أُلقي القبض على ستة أشخاص، ووُجّهت اتهامات لسبعة آخرين، بسبب الأضرار التي ألحقوها ببركة المياه العاكسة الجميلة في بلادنا. الشقّ الذي يبلغ طوله 350 قدمًا، والذي أحدثه سكين حاد جدًا أو شفرات حلاقة، هو في الواقع عبارة عن جروح عديدة على امتداد 350 قدمًا. لقد كان عملًا متعمدًا وإجراميًا، ولا بدّ أن يكون أحدهم قد بذل جهدًا كبيرًا، ربما في جنح الظلام، لإحداث هذه الحالة. كذلك، قُطعت المنطقة الصغيرة في قاع البركة ورُفعت بقوة عن السطح، تاركةً حوافًا خشنة وغير مستوية. ويجري استبدال المساحات الكبيرة من العشب. على أي حال، حتى قبل إصلاح تلك المناطق، فإن بركة المياه العاكسة في أبهى صورها. سنقوم بتفريغ بعض المياه، إما قبل أو بعد الرابع من يوليو مباشرةً، لإجراء الإصلاح الدائم.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79738" target="_blank">📅 18:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79737">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSJc_x2X-1trdBSeKWbbHbvpZ9lbtdkLu87927pFAgUt4sOA4lCklNtpltq0SirMAciSQ7DJI-OtqVdyUIQKNLIhCRruvi0LPCVhlbg5ocgr5iXC5Kbo9GCghNMfxYqX3R1jzPtzQq7iXrbt5hkvG2DFjBbcd7nQokvl92cSy8tR_tju3o7ohIvTIP91g_5d3cp0lyY4y35AEzQNUK8wmcYatlvYYXjKs9wnUJnVcx7uBDVvOqwybsdIAA0yHVOLAKwol0i-zDLVbWkQ2Bwpiqe88l9UZq9iyVslQiqurvdoen5cIOed60yHFGytNZxHkpYQkIM_Y_kUK5KJ9U8Ndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
طائرة أمريكية تطلق إنذار الإستغاثة (7700) فوق الأراضي الفلسطينية المحتلة بعد عودتها من أجواء غرب العراق.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79737" target="_blank">📅 18:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79736">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇷🇺
‏
بوتين:
روسيا مستعدة لمحادثات السلام مع أوكرانيا على أساس مؤتمر إسطنبول 2022.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79736" target="_blank">📅 18:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79735">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBfvonjTrL-FmErYpnOxXZuS5SJOU5JUQXXcj3oIKv9DJ7gDeGMkcGuGuc_86HWY8b6Ge8FuS7Zv7TzlJlbigPSa4R8HE1ytkXATrUQuONWWuf5sUXHkKgC3i_VlHE6m1bZsz4TtZKZtv81QsqkQOSC71bfIoG6cwleQQNEhkn2HSRPPJcalzwF0NyZypu_uwucWEgQz-C1fAWGjvIbma2vEW7KUGWrt-MGjuTcahF6WESjg1yPrylszGASqsZr93ZR3dkidE1W0TWdy9e9KzqfoXsxRj-x5tlzZwDJbOdLlo1h6umNBo3wOOehdoNwF1kXla4g6ivI5Jldq1nFgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
نجل الشهيد تنكسيري قائد البحرية في الحرس الثوري، ينشر صورة لقبضة والده المشدودة بعد إستشهاده؛ مع عبارة "
قسماً بهذه القبضة المشدودة، لن تسقط الراية على الأرض
".</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79735" target="_blank">📅 17:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79734">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكتائب سيد الشهداء</strong></div>
<div class="tg-text">في الذكرى السنوية الأولى لاستشهاد القائد الشجاع السيد حيدر الموسوي (رضوان الله عليه)، أحيت المقاومة الإسلامية كتائب سيد الشهداء هذه المناسبة الوفائية، استذكارًا لمسيرته الجهادية الحافلة بالعطاء والتضحية، واستحضارًا لمواقفه البطولية التي سطّرها في ميادين الدفاع والجهاد.
وقد شهدت مراسم الإحياء حضورًا شعبيًا كبيرًا، تجديدًا للعهد مع الشهداء الأبرار، وتأكيدًا على أن دماءهم الزكية ستبقى نبراسًا للأحرار ومنارةً للأجيال في طريق العزة والكرامة.
المجد والخلود لشهدائنا الأبرار، والرحمة والرضوان للقائد الشهيد السيد حيدر الموسوي، ولجميع شهداء طريق الحق.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/79734" target="_blank">📅 17:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79733">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0TFkAXeKhJBtrMNYoveYEsLkuiS7ZkzBAnzhDddwak2e-_NEsVXSiE0ZSYXeEF_CRdb2-ckjrWmI0f7KUh7zTSRUGQC9c3WGk1oA1vu8lw8ArCkT_jDUEoXhEUrl4xBd_JNf3eUuTq27S4G-araISns4R1AoDXHmuXQ7udF350uIdZg8hlP1ezL3UtbQaxpesLOqcg7bCkKCaFzg30-3vdDgEt4FKCZVUwA-A4d0HTkS8iQ3HQ4vwg20j5LcR9NaaTyRNKKcKmG29UTfBs9PkF3ysTCT4jPTCqqtTnTuvS-bybC7K6Y9RR_e8-Em5Gipx2luTr4T19bGzrRtDjlTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر لنايا: هبوط طائرتان من طراز AH-64 مروحية في مطار واشنطن داخل قاعدة التوحيد الثالثة في العاصمة العراقية بغداد ولأول مرة قوات الـ FBI الأمريكية تنتشر على جسر المقابل قيادة العمليات المشتركة لتأمين القوة التي هبطت قبل قليل.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/79733" target="_blank">📅 17:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79731">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🌟
ناقلة تحمل اسم (Kiara M) ترسو في ميناء البصرة النفطي العراقي لتحميل 2 مليون برميل بعد عبورها مضيق هرمز.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79731" target="_blank">📅 16:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79730">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مصدر لنايا:
هبوط طائرتان من طراز AH-64 مروحية في مطار واشنطن داخل قاعدة التوحيد الثالثة في العاصمة العراقية بغداد ولأول مرة قوات الـ FBI الأمريكية تنتشر على جسر المقابل قيادة العمليات المشتركة لتأمين القوة التي هبطت قبل قليل.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79730" target="_blank">📅 16:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79729">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🌟
🇸🇾
محادثة بين عنصر من عصابات الجولاني وعنصر في قوات حرس الحدود العراقية.
ابو زهراء يروح يمين يخاف لا يفجر نفسه ويلحكه، يروح يسار ويلحكه، كافي يا اخي اعتقني
😄</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/79729" target="_blank">📅 16:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79728">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc0KGnTbZ5sPU0Yzj03Yg6TqpsypVvZ6vAkTJnnxuWKMQT75PYrXOMi5R5FATRygF781laRiqtwYadWwBgZt774mi4E6AsX2uOWxHrIudw5qZ8Ib928VRbYrBfcIsjHU7djEWgGHQoO8wq8PTP4L2mnVf3N6iKycjuNh56QV5iinrhJBRHZN6M-Im-SMlUlY5wfZ-ssYqzaWUDwMoP2qNKbH1v2_UGjgbTt9BAK7qNEr6Yz90S02CP45tXwdf6KpCk3sfLlFHSxKQFQW4vHwAD0mC47unnjuBuJIAL-PT2Zm85S51Xyzx-LbHVjp-PEIfjgaxd1S7OEgQjuX-p70yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
القضاء العراقي:
اعترافات وكيل وزير النفط لشؤون التصفية تطيح بمحافظ صلاح الدين الأسبق وارتفاع حصيلة الأموال المضبوطة في القضية إلى (98) مليار دينار و(11) مليون دولار</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/79728" target="_blank">📅 16:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79727">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvnJGVkgzbNYCygv195CP3chO53yvFEQN8sYGsGezzsy8Sv1yzifsse5W3OYx8MqyEs7fIbk5Ry3d2pkO9b8yBa6Ld9aMi6XxV14XOJa7Ghr4zLzvWh4qlNNk4FNEGGJFBDTfWkFnHupa1hpA4A6vuRCcTVJWNgyMGeQLql0iKD6FRL4KE_26j0ZG-kzyNclsH4GIMDzt5YZ_rCPKASdYdQr16iDjjLLdkHwydE5ryrzVKOhf6DhQEU4sVkWGeaqhP92E_tJTy-hELn-zcWJQxJoS3CixB1qd4PML--zQ-KzJi7_qsNWVrx2jgXkcEmpfziLz7viGPB7TVkQqI--nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
إلى أمة المقاومة أمة الشجعان والشرفاء، وإلى أبناء العراق كافة
ندعوكم للمشاركة في تشييع الشهيد علي (محمد عبد الرحمن) ابن لبنان الأبي، لبنان التضحية والصمود الذي ستتشرف أرض العراق باستقباله واحتضان مراسم تشييعه اليوم الثلاثاء في محافظتي النجف الاشرف وكربلاء المقدسة
النجف الأشرف - شارع الطوسي
الساعة العاشرة مساءً
كربلاء المقدسة - باب قبلة أبي الفضل العباس (ع)
الساعة الواحدة ليلاً</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79727" target="_blank">📅 16:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79726">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 17-06-2026 تموضع قوة تابعة لجيش العدو الإسرائيلي في أطراف بلدة كفرتبنيت جنوبيّ لبنان بمحلّقة
أبابيل
الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79726" target="_blank">📅 16:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79725">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r93GveVMZFrkgpUQT6vjRfdUDFNvsPgZQGYTUmUcq1DArMB6WeLtNGRDYl-ZvG3DlBphLPY2mQZxtrTOPLLvv3PSX4s_2EF0psDpOjmhaAfRcCFy4jSYhNOgq0VCxDYuvlb65X0qj-1RZW2OS7rAwiIZ2L9aTjyUNPxaAcWaSTIrGIui-DBcZgWaJnocV7DsRHTupuEx4v6A05pdy5gkPX-l8EKk4E36r-1pVpBRJn6le-EOZ1lhPMkILJ9TJ9-d0jjZfJ8BMjmY6Okwrs5uj6lhjlICZrrBpV8xEoB-orxLbXodJSssOdd7NxhfphZPDyIRLToC_Nn446bygAeWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لجنة المحتوى الهابط تتخذ إجراءات قانونية بحق زينة العبيدي لنشر محتوى مسيء للآداب العامة</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79725" target="_blank">📅 15:43 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
