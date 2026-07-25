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
<img src="https://cdn5.telesco.pe/file/lPPj3Uz1NJAeVo7XfA9_dQ324LgY4skblKOo0iZHnkptENAGm9d90488XHip2pe6ZYtTSYVwO3IDZ4V_DwuR8NqrokR_Aug7WD-9lItvseMj42ahsSfhmQDEFnu7n8YIpxBJ-U7_GQj66FmBXMsrEgBPGqLQyuv1V3JxzmGZA6WHuGDYh3AcJW6gRnzzdToXnx0XOh3xk0EvDqOWlpgqDoTSG3SlTyLCn6GK32w53xBxdUzG42aPmEjIdIdD2TeALBOcRYKzBIN_tnS92CQirfuThXcZy9QZ2xULJjaZx-ILIkpY2jNMz0VK1HJ-Ff980GBezI7WabqgB0TXm-tJEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 532K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 11:01:25</div>
<hr>

<div class="tg-post" id="msg-101867">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f4c9480c3.mp4?token=b2PxyLBpzdRPMtPK1GKkH7LAtPkDog-Vy0LLYt0trrweeZ4lSRg8fjOHg3gw2oRGBDtEJ0RAKVe4-WCgT3edPvifwsagUu4YIsRMRdX_zkWjhmOE753xe2gol2pJxYHfuWRTnhUorYqX4NJEprE3jLW9RYlMix7JQE5QA0rLas0MuZ3i-MgHz2vIF46BRmOwAMwE0M3bVNwLN2PHNJ6dtF-ddrdMpjW8RLm74nFyPQhWnkZhvmGuECXLd6de_OQak52MwutHLL4wSJQLht3ai_zL6I8lztbBk-iTv26NAnxiUNSYSezGWwLUn28JDx2p2_vXNMwDLDyyc4a6hTc4iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f4c9480c3.mp4?token=b2PxyLBpzdRPMtPK1GKkH7LAtPkDog-Vy0LLYt0trrweeZ4lSRg8fjOHg3gw2oRGBDtEJ0RAKVe4-WCgT3edPvifwsagUu4YIsRMRdX_zkWjhmOE753xe2gol2pJxYHfuWRTnhUorYqX4NJEprE3jLW9RYlMix7JQE5QA0rLas0MuZ3i-MgHz2vIF46BRmOwAMwE0M3bVNwLN2PHNJ6dtF-ddrdMpjW8RLm74nFyPQhWnkZhvmGuECXLd6de_OQak52MwutHLL4wSJQLht3ai_zL6I8lztbBk-iTv26NAnxiUNSYSezGWwLUn28JDx2p2_vXNMwDLDyyc4a6hTc4iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
🏆
رقابت‌نفس‌گیر توپ‌طلا ۲۰۲۶ در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/Futball180TV/101867" target="_blank">📅 10:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101862">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZf7ji4P2elSKJ1k122n-MKoatVIuxprC9Q4ZtHeTx6YwbrEYjav_OKwxzAYsBVm0tqtAFr-UaVoYI5K_nYwCMFH9mOZiisAnbOwu3LOLpzBYDaJi3eHuTWQLDd9CICPySm8KuX2IJhOrzSXFsiWLN8kl7FFJE87R-Lvr9yR-eFBdNi0LQwPCxEWoshRwE8xb2pD8JjcbwfL-97t9sdmqoB7s6x_BM-2h6bVaLSCwsIzsFrT4FwoL-ZJEB5nJ1l3p0O8qf4gUxbPvrb88mnoCUPh3lV2bxrOzr0TPSWguwiLDmOCgXNe0kBfaA2E_mlnY9LrjAfT8vmVmr8QwEeZGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMi0dRIBdto8lbnFO1uS1i1XM-53CMrTjlFftfYI01OeOiR9-i3_OTE6YxObH1ta6twoAm6WTwdltksBIrxtuvh0ehV7IPDGFNxqqZIlkQD69F8RIeK3Ksi6Vok4jzSa3S5ku0gXoSmIA4ClJpD2_Tad5OVvrotloKMo0Y-eISLpDsCvW5_9jtkoHkB5r_fOI_Y9vZ9NHEifZtrWkNMysxhV9x3G2H5CBQnUoCjMnt-1H8j9E3OgV75wg8YWO6sp9aw6yL9xyy4pzyfEg8OoqcFcvkWp8yuLmCtoSZ1idul54jIs1cNW6mmvAVicY-JDnnBhfZTYKJ9YSBNn88Z3rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNyOoveo_Ju7CFdcYUN6Lb_trva6yFar8WRg3V_hdnWHXegThlw4N1ohoRkkoSams-V9mGDQj-gJgwGi_yArEeWAIH25KQ0qEKJ1Xicx78heHpiAgsBDDMc0cfYLyUYFcLiMEnIXnMD9_Y8ep3uY4MxFsmSB7AfpyWG6a1r3SNTyAooAHq6qB5JE-Bhn_scr6_uK5LOO9qTlfuWevpSsk_mwS_f7oWfVZIBiuKDvQOWk69qsw6lf7BYVzRc7bG3b1tKn59dFdn2lVP_Rj1Mf_d6oXvrJGvO4vlqzC4ev_LfcUxfqIgZt4uhGs1Loz2mcahbc11GLf-QwxX582CYEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TS2eWv3ucHYmQKyjUxMGzdv7FknQG5NujEhUIhg5dnncwR3WRcaIwtuDu-wKkSp1u9ulslk-RqNRp1Rc_zbIHfZjv3H9V3hfHZrHfFG0SlqOltuELSla5VfUgl3n49oDaacZHIQw4ov07NdfClcBf9CTnck1Fx8HM3B6ZxuuQXX9C599NHYHoEHL0aFoOSCMploCHCXd6pzuhqr6aW41apisZgnzKUvkEcJsq8_j0Kzh_wRR5OVBynxTzcJyNfYf0YguQ7DrTTZdlgd5b9AG8F0-qgf-29osBvSv5BwqYS-8VIUcsAcgSd6KgGaV3Lpps3yy5uy48lfpuiUSvn0Jmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GcWzRMG2s3sr0-zQE9dxEcv544LE4h0AjqX3Nxo7CyMRoMFTM_LrVQLR528MPRV19JWy9fKGK0hGvccugGjnuf7qpGLFHuCH--xVKVe8V8ReJjT1lSXpjz4UvJs7T8wQXKmAYl5RYnj80yOv3ETVFaE4Rj8F8qtXumgVqW_uykUNlJoRawRK5Vc1RhSTLuPew8UR-gjCOUzMjhdRJjCqIne4mLCmC83PFv1H0WdY-ZSN2o0jVQsIlyT_jqNwPvVZJ-mMyGbAW-HOpzzePKZ-FHJAekNiv11g7kSbJ57KwjN6F23Z-aUtyJXXMtgUAHkMomddCcyOnJxuOr_NtONfqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">+ قدرت تورم :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/Futball180TV/101862" target="_blank">📅 10:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101861">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d7ccd208.mp4?token=ih9kN0VwiJtXQ-NCNyv9C1aBPSckVmMHhuK875Mps01WWzKwp2u4ql_5CQKF1nLmikp5XID63ga9PeIkIGAAhvvc4H5oH50Rpb5SVoJduW6ISEZzIt7oVGI7eklzjCeRJ5zSHjG0HfkegH89twjEsu5XNp48tmXEeBEoZV4mjl8rL3rS0Am1i9V6Z8mfSxy0DGcLWGKZpYIZZJzpRm15QHoEYdKXX41tPWlzBun9XZ7pM5KlIa1iNbT6NVJK195O_85OyJceaLLgDQITVU7YrAD9MEmjlu1LYwdUnllVVvl9DBrLQ1v57Gr4J3Xmnn2peRBkf7YlP7X6LN8Bc2xZtg--ZedjP3D0FijTDUS8J3cV5sztOx7vv6GvGbK394PI_GD9oOkbEMMpF6iIfKN2jUgMdjahA3-pkP48UmvmYtYpvua3nqXxMe-biOm_4aKLvndKLKjSpkTh_vS7pQEkGAD2AMbnWW8huOik4uTf3aXHzSg9nix1GDWB0Bc2TkWaaBoYaq5nDAnIra4LqnFhbGK78IpfilLgVgY0NKq0UZnU3raVwRNH_vB5IuDSKhOllAqG_iCXgyKvGYM1NDrI9fzAjhyr5mldcls01i67MxVdVx5jBi8AuhJronyKMVS90J_Cd1FYglvRKMqY_kekgCaUVS0J4UcSyNK0rXifIIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d7ccd208.mp4?token=ih9kN0VwiJtXQ-NCNyv9C1aBPSckVmMHhuK875Mps01WWzKwp2u4ql_5CQKF1nLmikp5XID63ga9PeIkIGAAhvvc4H5oH50Rpb5SVoJduW6ISEZzIt7oVGI7eklzjCeRJ5zSHjG0HfkegH89twjEsu5XNp48tmXEeBEoZV4mjl8rL3rS0Am1i9V6Z8mfSxy0DGcLWGKZpYIZZJzpRm15QHoEYdKXX41tPWlzBun9XZ7pM5KlIa1iNbT6NVJK195O_85OyJceaLLgDQITVU7YrAD9MEmjlu1LYwdUnllVVvl9DBrLQ1v57Gr4J3Xmnn2peRBkf7YlP7X6LN8Bc2xZtg--ZedjP3D0FijTDUS8J3cV5sztOx7vv6GvGbK394PI_GD9oOkbEMMpF6iIfKN2jUgMdjahA3-pkP48UmvmYtYpvua3nqXxMe-biOm_4aKLvndKLKjSpkTh_vS7pQEkGAD2AMbnWW8huOik4uTf3aXHzSg9nix1GDWB0Bc2TkWaaBoYaq5nDAnIra4LqnFhbGK78IpfilLgVgY0NKq0UZnU3raVwRNH_vB5IuDSKhOllAqG_iCXgyKvGYM1NDrI9fzAjhyr5mldcls01i67MxVdVx5jBi8AuhJronyKMVS90J_Cd1FYglvRKMqY_kekgCaUVS0J4UcSyNK0rXifIIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
روتین تمرینی لوئیس دلافوئنته‌ی ۶۵ ساله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/101861" target="_blank">📅 10:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101860">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025979a7c1.mp4?token=rGSzJa3v03gi9yQNVeWV0mR1KSkYHY-ygg1drETNWPjhYWs2vszd_Lutc7NGP-21Wf8FPm7WTNMcqpDKwv5Cuhzq_ogTr3GB-vvC65HxByIJuLsDotg--I_smFw81mnsmQJzw5vp_bhhHpxk_47h53KCkddiBDzuN3W2hKp4RjnfiEl3E3e8H9hmt3QyyPA36MKG68eUSFE66E0m-MVBZtIdVMf63t85tf2Th444yLktWrJO2zXfNjzHD4cXfAjL57AGDFVnamlZ-_2meh7KPo-DAi5ZEqUKOhq1Ce9n214LY6u39mqxy3rltUoL-thJs7CYLm-Hsf7qOewcuPzJ3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025979a7c1.mp4?token=rGSzJa3v03gi9yQNVeWV0mR1KSkYHY-ygg1drETNWPjhYWs2vszd_Lutc7NGP-21Wf8FPm7WTNMcqpDKwv5Cuhzq_ogTr3GB-vvC65HxByIJuLsDotg--I_smFw81mnsmQJzw5vp_bhhHpxk_47h53KCkddiBDzuN3W2hKp4RjnfiEl3E3e8H9hmt3QyyPA36MKG68eUSFE66E0m-MVBZtIdVMf63t85tf2Th444yLktWrJO2zXfNjzHD4cXfAjL57AGDFVnamlZ-_2meh7KPo-DAi5ZEqUKOhq1Ce9n214LY6u39mqxy3rltUoL-thJs7CYLm-Hsf7qOewcuPzJ3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
دلبری‌های لامین‌یامال و‌ زیدش بعد جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/Futball180TV/101860" target="_blank">📅 10:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101859">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/552820f16b.mp4?token=g-WFp1-UEIZJPowMEvkRjoUf5U4Ao0zuIoPIoRiPnEGUqxgPZiScZHstsXAAdzcWCFJZH2mpUDIAz3dWvHVgW55EtCBG5RVE0JEgtIfJjW0-Yjdld4_h5gui2kWOOZr4sMeEDo6Vm4ukYhlNonyrzeWovUAucAgED7mbLvBVivYCvHue0zzHo90EPNiK0wZUfEu-3fsHvzvdo0DBMObXnh4dA41M57sKxE0M2UjK6TKjtnXMGcpNq446FKsBTfvML6u27ID_Xs-L6S1MW7gBfeU50BPqjy6-xmBIY4Rp5Gnw7d_EOe-2PX6OnN2eSDrCK_yrd9m4VVcEqWlHi2xNOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/552820f16b.mp4?token=g-WFp1-UEIZJPowMEvkRjoUf5U4Ao0zuIoPIoRiPnEGUqxgPZiScZHstsXAAdzcWCFJZH2mpUDIAz3dWvHVgW55EtCBG5RVE0JEgtIfJjW0-Yjdld4_h5gui2kWOOZr4sMeEDo6Vm4ukYhlNonyrzeWovUAucAgED7mbLvBVivYCvHue0zzHo90EPNiK0wZUfEu-3fsHvzvdo0DBMObXnh4dA41M57sKxE0M2UjK6TKjtnXMGcpNq446FKsBTfvML6u27ID_Xs-L6S1MW7gBfeU50BPqjy6-xmBIY4Rp5Gnw7d_EOe-2PX6OnN2eSDrCK_yrd9m4VVcEqWlHi2xNOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
⚠️
بی‌توجهی یامال به دختر پادشاه اسپانیا که در فضای مجازی حسابی وایرال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/Futball180TV/101859" target="_blank">📅 09:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101858">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5533cc045.mp4?token=c0dLlbfsqPlPe_O4M_XRAo7VV-MryIJfKhiDbBT6EQip_arE_k2cLY1e-KVpfstchsuLrgNJs82SnEBnRlc3Rd4vaAqKGWHPPYY33sQhUPgiLziiUhKkKxnwNBXHVNNYt2WMfozdshEp0wf-nYAau5I63gzYsvLmnPNx-e4fYim1AuA3yteCu3dpFFfxcdeAwDLGBYTir5C-n0elZX23Pm6t4j6lFl2-TsllseEEtceH2XE7_8kYFiDOD1_NfnUU7TFDh6VnL3zYH6_3ekrrtQ90gMIykFW-__YPnsO1kZPXfghGm_IgpWdClsGbcC9rscBNcbmRnij441ugDWBVdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5533cc045.mp4?token=c0dLlbfsqPlPe_O4M_XRAo7VV-MryIJfKhiDbBT6EQip_arE_k2cLY1e-KVpfstchsuLrgNJs82SnEBnRlc3Rd4vaAqKGWHPPYY33sQhUPgiLziiUhKkKxnwNBXHVNNYt2WMfozdshEp0wf-nYAau5I63gzYsvLmnPNx-e4fYim1AuA3yteCu3dpFFfxcdeAwDLGBYTir5C-n0elZX23Pm6t4j6lFl2-TsllseEEtceH2XE7_8kYFiDOD1_NfnUU7TFDh6VnL3zYH6_3ekrrtQ90gMIykFW-__YPnsO1kZPXfghGm_IgpWdClsGbcC9rscBNcbmRnij441ugDWBVdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
امباپه‌هم دیروز اکسپوزیتو رو برده یه جواهر فروشی معروف کف پاریس و براش هدیه گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101858" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101857">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiLXc6rUIUimaBPiSQNYThVloEpIdBbZKt2YZFKCkXjW1jnvLiEcleh4ABCJ0fZz7Al3uzkTkxe-OQlUfYs4gNrlG0lyKckUwbpjSGM4WE3Q58jvkRA2EQ_S2js19ZZCp-Bfl-mHHpwInaLo1FH4D-cRIzHL2MEZAJOe1a2lcL9PLIGCT7gKV5r96oIPVjPCA8zZRpezsGvtJUk9q0jbV-VVuBzkjjpWfmjghMR0mfiABmOtnKefXpbL-g4S8f0VDKlzH6JsolxsL16CZyrU_rm79GDaEJ3pvf9PJT5IXQPNDxtWm17KKKpPzyAexzbp0wDd-N4piACFizUDEBnDRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
✔️
تمامی کاورهای بازی FC در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/Futball180TV/101857" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101856">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحامیان_جبهه_پایداری</strong></div>
<div class="tg-text">این یکی واقعا معرکس و حسابی زده توخال!
#من_نمیتونم
@hamiyanpaydari</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/Futball180TV/101856" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101855">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❗️
▶️
کلیپ‌فوق‌العاده دیدنی از پایان برخی از اساطیر معروف تاریخ فوتبال در جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/Futball180TV/101855" target="_blank">📅 09:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101854">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2e5fe7985.mp4?token=NqtLqXHrpP0QYXGZRoIUqUW24T2fWt63uu4h6BCeK5UA3qPDjXd3X4sboqFyqAjTHip_Dhr-qgDedkHmPiFlHxBZq7KTlUhyVENcxqehuT0T4PDMlcx15kiVCwv4STnYqp489jPiyiMURuTELCNl_Jbx1WNb-tOCvzUzUgDI5ZSrJTk3PSwII2WXMuMonbKD3Nz4Sd9bCEmUTf-c_jfHf3zsYJ7ZumeX-AhaGVQ1WctlA9dYg6urjFj1Af0MSRqTQUkedqXbocfj8nD36xJYsAJfQeA2t2BEVQTPZ5PNP2MXsNF2coaCPe5xuEEgdhuRmU-L4oqCL92YbyyQGVb0vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2e5fe7985.mp4?token=NqtLqXHrpP0QYXGZRoIUqUW24T2fWt63uu4h6BCeK5UA3qPDjXd3X4sboqFyqAjTHip_Dhr-qgDedkHmPiFlHxBZq7KTlUhyVENcxqehuT0T4PDMlcx15kiVCwv4STnYqp489jPiyiMURuTELCNl_Jbx1WNb-tOCvzUzUgDI5ZSrJTk3PSwII2WXMuMonbKD3Nz4Sd9bCEmUTf-c_jfHf3zsYJ7ZumeX-AhaGVQ1WctlA9dYg6urjFj1Af0MSRqTQUkedqXbocfj8nD36xJYsAJfQeA2t2BEVQTPZ5PNP2MXsNF2coaCPe5xuEEgdhuRmU-L4oqCL92YbyyQGVb0vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
✅
علیرضا فغانی: هميشه خود را كنار مردم ايران مي دانم و از حقوقشان دفاع مي كنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/101854" target="_blank">📅 09:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101853">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBGnU8aI1UzQNWMJdCutdv1PMI3AvHph5xn9tpD6EcaTJ7gB3ORsun1h4b2ApnFLhz0HcvVwBc0fszMbAK9vpyYDFvj7Z7rFnLm8vgv3Ar4YXvXWG3kGJtKpNz5UffOFNAFitBTJiRVMRLrHQTEwyWpzU7hHwetmp85slhYdj2y7mBr4X7tnTcRCeYJbgJxSdFf9bJB3elQgwLlrG6rQoEaJXh3XtPJw-ugqdCWds3ai9gvPITUZo6sfqd6gqM4Ik5cy6grZLbGEbAYCU0j05s_wtktnnb8EdcD27fNC8ZIK7W1ROVqL9A2Czz4lp6JeRmNSjCjYZnSkYcr27chnhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رسانه ESPN: رئال‌مادرید تصمیم گرفته که به سبک بارسلونا، شاکله اصلی تیمش رو حول محور بازیکنان اسپانیایی بنا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101853" target="_blank">📅 02:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101852">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7211acfa.mp4?token=gha5Gup9AWk28a96mlAumZ2LinbP02xa_qVmhvlteLn14RoL9o2Lbb-w1CbNHB1k6O5-9CbjSWnZhXZ2ZGFAeJFSthNrSfZYHAkFek6xHySfjoganF4K7j2uDR4GxxvElvWEECYXxc8S2wXw8k6tYYnQJf7eT9CKXpE1EA65jcF0v6tcT-QawyxAte_zpVYV46IEMZcbXSetp8g6eFpOo79Nt8-1XaN13Rc9PVaCMKvmV1iOgm0eD5fvh4gjaXuWfT-Z-9egOxV256vuI-O_om4acX9sSbt92KCDgymAnWnNSzRxCTXTgGTFNSn576x9E5910p2i83b9h8oRRUca5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7211acfa.mp4?token=gha5Gup9AWk28a96mlAumZ2LinbP02xa_qVmhvlteLn14RoL9o2Lbb-w1CbNHB1k6O5-9CbjSWnZhXZ2ZGFAeJFSthNrSfZYHAkFek6xHySfjoganF4K7j2uDR4GxxvElvWEECYXxc8S2wXw8k6tYYnQJf7eT9CKXpE1EA65jcF0v6tcT-QawyxAte_zpVYV46IEMZcbXSetp8g6eFpOo79Nt8-1XaN13Rc9PVaCMKvmV1iOgm0eD5fvh4gjaXuWfT-Z-9egOxV256vuI-O_om4acX9sSbt92KCDgymAnWnNSzRxCTXTgGTFNSn576x9E5910p2i83b9h8oRRUca5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
‼️
🇪🇸
شروع‌قدرتمند آردا گولر در ترکیب رئال‌مادرید برای فصل‌جدید با خراب کردن‌پنالتی امروزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101852" target="_blank">📅 02:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101851">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqBfL5eXffk83RIOptdjjsekAKpKqqa_WKRHvwWvf21h_CHcAU6DFE8-IwT5_8QHh-H2rdRrbu8SIAKmMM21aRwRVm9Dk3XGKPyGlXbfJdOH3e8hMdIhtcmjjJ5whEE4i2bwiYTZGif5ZDIsJut2vbhKTM1HIVwOLOEW48_iFeRHOWfSNfGNTLtvOd2nPeU36w3KAqP0ma89nAGs7D9Ll_wiJx4qoU6H3E4B8qgj2jz3Cyp7xRe6p0XPUgidcFdxZ5C0psFTu416pMftcnmI2C_oO2eXe0CQ-VSvUEqYC4YSavV3AEG_I7eugiaea4gLPIPAL78FzzRlbzgl3lf4YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇻
بر اساس شایعات منتشر شده از منابع خبری آمریکای جنوبی، ووزینیا گلر شگفتی‌ساز کیپ‌ورد فصل‌آینده به لیگ‌شیلی خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101851" target="_blank">📅 02:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101850">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c-dxPaReRuS_mY1ZdYhm7r1tGjq6MWqQcB7KFQY49ipWzZ35Bvw89p1JgxaN4oyCR2sJqcsE9yUhclbHfL0-4mtwfXntsCJDYGPwsFiH0b4L0Z8XswqlsYxqsZcxM1hgxr3TELR9IlnHZAtUwhHbnUVEKK-baVhIUXNJ1ZGAn3DZdkKHOixN7yJZFpBuIsE6deUiYsVgVmZ-9n-9nORboljarC3jbv3vBFbURaqWNW5XZheKDnXu0XPBnv-gVvGaxQX9bao6EUmV7kBiNxnsp9f5AJ9V0tFpRBSUWUZHyFirtZbJklowJWh0zrliGICWh98OgPTa_dZ5V9n1IYC1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101850" target="_blank">📅 01:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101849">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pO_irJUtT2rhxfqpKf7PyD-gSlt8-7YlalRilBltYgkKs-leVbRM6aHH2lj9GZxO9mnE-wkgw81NDwORIXC6U_V5pZbDpe9-tI-deedBf3dXzjy5A4XjxWeh5aCKQ-gKg2nFDHwxihohDNE6KlLikVXgEirRKakIWUmyQxeVpC9uJOLtTOp2SG7qnhQrDnFYZImr-lEXd22iy1xLQjY4wzC5pIEyP7osclBnKCqXQMRDyqrBJS3xjLKbbNksV_ayhaArZEXhDI61CAgLMRkjdE7Ofts70NtIzEZE2mjfHHT_athypEJ9DCXeB-64Pcy_nEmYQ6GZVSjFrRZ-Fi_zWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🔥
🔥
🔥
مارکا: دیومانده تایید نهایی برای حضور در مادرید رو داده. این بازیکن به پیشنهاد نجومی پاری‌سن‌ژرمن دست رد زده و گفته که فقط به مادرید میره. مذاکرات فشرده برای توافق نهایی با لایپزیگ درحال انجامه و بزودی خبر رسمی میاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101849" target="_blank">📅 01:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101848">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eiy0tLkafz6e5NlgE8OZSAEMIPYxqD3yByegkuWZSDo8mrUrf8iDW4CGXfHaBbj-cauNwaN9W-zLc0OSHIXtnQMp3rWYH6J0fmiNKXZF1YV4PyA5F3yuQP4O-XAWDFfU8nyHW7TQu-ncso0vkTT2avCyTdygfRuLxA7e8GU1m9G4oyInNQJYgcjbEnH6TFijjtw4-SArep7PATKU7ys8_NYS-34GI8mEge94dy3bnVS6mmcdRUb4k-UON7AGJMvDygYK-07hML9nT78MErKUswbpDrfXzI8dK8EadpM4hmXONJTNezO12LUf3FOv7DPKu_fzOfffJhZfuLFvA7bepA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز: رئال‌مادرید و ژوزه‌مورینیو دیوانه‌وار عاشق دیوماند شده‌اند. این تلاش پس از ناامیدی از جذب اولیسه صورت گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101848" target="_blank">📅 01:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101845">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EAI7ucwi1x_gDmhKAbBnyUzCpOS5JSH7SoJ-79ghUx2VQ8idGPdg1r_erIIsXszmr9JMPRTHXdJbpb0H9k9EMPiNCucEvuCo3ZJAxDCJiw9HIKqnqEsTcNIDBFnKULWDCP1Zg0NumoVt2ZpFEywflFpw6EqCZMDtCve0rrSdxRjKokg8ZWbUn-PXCkDqlgUhDis10n91XTbKjiMQJ6ftbwacTgZot9teSupp6IDb4luOe-3maPdqJMBHavVqrNoUg2XKYSznaNZ1nWjEfiCgIv5J9RfGlDs0Deuue_Yjk-prr0gWSlyWhpKhTxQDanTD1quWmJczWytCzpb2IBzDNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oCTN1H3XHJjlyofiJBerARkC7Nb5pr1xfINQZaiqLJRMGFghJhSs3TE59yYVyHUhoJZFo9YdcKhKZnLJFQw30wbLplUyHDgsqyCCrwVz6t_HM6PD46JbczzaaRbjKZx9e1KC2VKNadM-tuos0kSHYZhJAL6y_jNg2XJ0RafKY5YUGoSZkJV6wm2IlTx7DdQdgG3FY06xOvZpzd3smo3-cFhbqwT3g4hcVZR1RrY8-rSO7WHKdJBrxurxY6c8qeJ69vexJcYTzJaJoCyeya3zab1dPLOB_S70smHkWld3YJ0zpltLyQyETmwLtEsEXSrDryn6Iw4yqq-U9IdDxWdC0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز: رئال‌مادرید و ژوزه‌مورینیو دیوانه‌وار عاشق دیوماند شده‌اند. این تلاش پس از ناامیدی از جذب اولیسه صورت گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101845" target="_blank">📅 01:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101844">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkGT1Uf4vJHT7WW5fKhCHEH1noxAngcVWG8bIm1J3ZJR1xR2gs3orFjdEG_jKvTQFo-GV9lLQe3eZkKX6WQ79lj8Egesr7UwlyUhiqvM8OkZFvb_5Ik3pBp-Rx4s48eEoSCBDsxTBXtDYv5DZMT-_aKkvgu1L8bCIPerLUrkNstqASx_pI1F2oeH_P7OP7mEp6oZ5j7oJHkCkyKMQn4WevVArDMPF8mSMn1v8osVXiDo2F2iIH7uK6MXzdEq7g--4ezuWA0L_GI2gRx47XjLZwBY3deRhKqITb0CmGkebIFt7q56CTsEkzrm_9mGmtCc3QSKRU5CYVSKcD31MgjCXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
په‌په‌آلوارز خبرنگار مطرح مادریدی: در رئال‌مادرید برای یک‌فروش دردناک و غیرمنتظره آماده میشن. بزودی نام این بازیکن فاش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101844" target="_blank">📅 01:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101843">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ko-UK5yeLKP53oFX3c0Ll5uE0HHhFXCW0p2xQsCyDS7J98ckUzTa0wz8l_X3hFuoxpsFvyKvGHKQI4QZWGUUcGjqB4muYwKDeKkK1gt2cT1tnvLudSOcipwBs-WCMEc15GPIlp1iNTV_gA7JMpLCYJRkhe3VF1eW_hCjzqEW9sgHXBE3J_JWFLXh6vsCb2ZSR_pX217eET_p6NzAx3KbHvBa6C7fsr-b9LgnH7SQQUmlASZ2wwoHmGOErO-oZM_UJAM4AKtRN9SkMKVtvQZie-xwghEx5H5BFozmy4t2ESgTnzgiOtvwipGpWLmS-QpzvHE_yDigwOnEzMmWOhvr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
په‌په‌آلوارز خبرنگار مطرح مادریدی: در رئال‌مادرید برای یک‌فروش دردناک و غیرمنتظره آماده میشن. بزودی نام این بازیکن فاش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101843" target="_blank">📅 01:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101842">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
⚪️
رومانو: رئال مادرید پیشنهاد اولیه ای را برای جذب دیوماند به لایپزیگ ارسال کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101842" target="_blank">📅 01:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101841">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dkl-bjDqFmLy0NWGgzqKJ8KSOr5KrpZUENoUv7uG4BgPHz47CIdCSeFDJ49Axlfguvg0dxUUUfcN23RQ3G_OuNubAaBBchgut_48afv6iKwfBq-ITQ5QW9eT65RtyrLTF0auxu4vrHkFu8cGrOoE03bodAcSynig0QBXOpQEk9wYxaEBWr2GyXNJ-riQB8OJQ3rOGS2GHzinSPpsDP5-zs2EBQ1Xb4VL04mNaIhBcyhDtTFqsKSDzMeRN50xVe2ANP2r4cvDRwB3z_E_3Fk2PeClSfzs8qB45QGHFOyN6m1tzUmSsOmg6jrtW_wnYDzKZgCt2Fsk4Axmzm-U8is5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیژن مرتضوی و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101841" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101840">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOgmW3Zndc8PHocJU0jk_b1guPew-Wwz8_LlI1CnLdVAWqIa124lLWQjsm-aS9_pVAz46D9I77DDhpHLLp5PeMzt4w5G46p9pAtF3Xq6YDGwJKwXLjKHWwHjJQ-sp0Kn78kdeAbnZLEw3yhA38bu7lHyIjgpof94M9ACV86pg2PTOWbNcDtv37Wr33zbqmRiJPt3PWSqgGrxz_EBkP0dPY7kq7-cQ-fxilb3gLOj3uwpJHcUSrOAqbYdxEwXQVLheg1yogr7LusfKwSEhDRucI-J-vsyn2A-s99Ahu5E2TidbcKfUymxBNHTVWtqhkQXiXxsXYtEVuy5ObG2lRWxxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
رقابت دو اسطوره برای رسیدن به ۱۰۰۰ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101840" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101839">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8hS5nyq9ZDtekpSKWSLar57xy8jXakgHmZVnxvPscClK-T_aAEP1qQuCn9gMM1NHn-s3T9q0IYgy9Mx5i4meZBuAyggVbBD0gpzJ0vAs62eTSpxUnyF7wSytTAicgQ7hXIByx44okJRDiqk6ZiqTm-gGIEIw4iwa1sslgKla2uv2tvBaxYgKr8sn1S5xHTj3rtMJrmo4C2FS6Z6O42mLGBmmPGPlxJfxI2NPiTSiT1S1825OJ_YvR76BFy4UqaQNYsOagBshacayxw77MR4z9OorZkrMVngQBpF3FN5ID2-3Ar6pp9o5cRAp6EqKHaekr9DEuPODbsy8XR8Dl5uhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رومانو:
رئال مادرید پیشنهاد اولیه ای را برای جذب دیوماند به لایپزیگ ارسال کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101839" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101838">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxzpsXHbwHHrLVWtztRRB6Abzj5eJ7VrWEq2tkvGTJAvpe2q7awCsudnWNv1ceSkcntfsOcDCdZs-Oez5F8w_-248UwRWkTiV-TWGgg2X8yZIbNqIM8S_bL9O-r7JAo3xGg6WrvjW-RWAJCebuiftIEnwHZ7zknOFpvgr5ONG0bZfpohpOB1TSFb-qrku2TZDcSLgwmBzXaPC1mHCvLxNA4zcry86xpNfHiGZW366lD2zHSjoRZfVLW_MwSIqZxDRXSqBuMy5yTHFAvCNNfToSrBsl8YkBtjnpfipdWP7jegLsEl_ORYwekJIn7oJSun9WDQ8KFkuN4cnjHP472mgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
بهترین بازیکن جام جهانی ۲۰۲۶ از نگاه فیفا و برخی رسانه های فوتبالی جهان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101838" target="_blank">📅 00:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101836">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCa8kN7cB-y_X-JVn6Y0j5VLR5Oqp5JYMRhwAM9-x_54nhgvaBRFfxpt_bcLGifmsMffBaLBDbiRp2PtMXkaicgaBkuH1gYlcv1-6xw7ZWDc1ZBeLM4fpERnIO2WVWJWQO--__BbXWtSVxxkUYuXV6G3-qB4Svm6CwwrMRsDI8D1KJohjuE3G0c63NRr3GlP5ohLNiaHrO95MHHzt9Cl120gGLdEe7kyUwvJhxxC4RhuR60CHY-iPyaXwxvVO5r0TqbwOQFfCBWWXtFEdF7uK6OkZ0Od7X5xVAe6fhJaCn1BddHygnqPRJWOXohhIez4r46iCLXY4myzGFrLglSrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تیم ملی آرژانتین اعلام کرد که لیونل اسکالونی به عنوان سرمربی این تیم به کار خود ادامه خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101836" target="_blank">📅 23:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101835">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQssKl4K0sbjOY-93pUKzjemIUDfr7dn-UnhSh1sl8PWoy-2OiS_yQBf3DNpiE-7IJ6q-Aut227cidbgGswHI2s_hw3YPrpk9eH8aEeVkIzaV4eznWE9wdOsCGz6DYlqH69oBY-bG61CmYBA5swII8Zs27mQm4jOlFKgm-yWf2AtMGglfyu1aAOm8yU0RWsTolta3mZ8O_MrVzXbQAXHXvYkQi2mmwHodmx-rr8fvUFYl62Mdkm8JsXRyzG7hoNiSVkRvJKUU_I861VswUOb6-g7QApIk1qFDdYmzDBH9Vrxow_UKjnDRFAvkb7FTjg5lg6gcC-YPzpcbMc-Ju4bwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
فهرست بازیکنان سانتوس برای بازی بعدیشون مشخص شد و نیمار به لیست برگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101835" target="_blank">📅 23:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101834">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-CEXRC4nNi_EY7zJWzkogVfcK6QZHqZZCxpE0fkwU805e26DOxvZajlGWoMBkOenZQcPJk4-Jom-7E0Tu84RY13yPzKbA8KYlVXlCfN6CNZKFF94uVS3QCA5LylEu8rZFwnKHBJRhmCW67y2c2DtSzKixRgMRRKZHg_3ugwqzBmL-QQKo5WBlxz6a7CzIpOoNFV33YpVhHJH-hA8XvNV-MtoBvhRlydZVZ80MBPJmWlPaa4W-vzt73BkotjSUZ3iJQQQ43kOAAbDQixT47d7gB0ypWOU4DYiosn073lLg86ujESHPeen1IWmhTGHz0LC81LTZ5UMBndc3NvO_HyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لبرون جیمز ۴۱ ساله با فیلادلفیا سونی‌سیکسرز، یکی از مدعیان قهرمانی NBA در فصل آینده، قرارداد امضا کرده. این انتقال مثل این میمونه که لیونل مسی ۳۹ ساله برای فصل آینده با آرسنال قرارداد امضا کنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101834" target="_blank">📅 23:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101833">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
دونالد ترامپ: با وجود اینکه درحال گفتگو با ایران هستیم اما باید بگویم که مهمات ما برای یک حمله وحشتناک به ایران تکمیل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101833" target="_blank">📅 23:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101831">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFxco8IjE66VR-rE4X6E0ZSGhrxZmFXWUvSqtrKdBkPf_wukH8hQQy2JsBZ9Av6OzhmSEMa-_aczT6M0oqAa4f52fG1Aeac-c7aMObLxTchl3PG0_BRBhii1iCnaqDy3iYaFUhF5y1elG4Z90Epd_aUICkGGsvWvJl3sThoP1SopLXylt6h45NsPtcIqJPvyYFRAFxIsgMJqpaydFeJEwaSfSthlRFiY7iwHctYhjnOMc2wRFngWFuC34cF6mQdRcNHZfCLdd4fAmihe-_tJsNh6Pxwy8ZlBteiPopK1Vp-7hsGEQz008swN_g_vcUW3VKM8L3mSdkkeKBlPQrmdAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V3oSbscJ_ZCHVjkr8oXJZR-fsZG54ZMpEQ59P_uFw98XjA7-jYU5T_N5zW18mgcEJUaKbItVe_yX5wjBzVgOkxOLOgnVM5lLsRc2Hec56Dxx5r-7Ye7FXxdMxBJ2hq1fgiXntPosv57rQliYucMjQ6PSqEIAG0wzZUCKkqL065V5XxeOlUKxRlKwcnbHxjVZhwn17JbXor6F9K_zCvFtTiuPEWXHS67pWH3giNctz4l3uDqN505woaz9RHZLJQtxmnZKxtT6nZcGERDI5jx8NK5cxNGEHvubB0tyHuLZw8ejd1Wz2uf96j0aef92Srt0m-y41DDsyRWoxPZVF0wkDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
نیکی نیکول گفته دلیل جداییش از لامین یامال، دخالت‌های زیاد مادر یامال بوده؛ از تماس‌های روزانه گرفته تا کنجکاوی درباره جزئیات رابطه و کلا مادر یامال علاقه خاصی داشته بدونه یامال تو رابطه با دوست دخترش چیکار میکنه! او مدعی شده این دخالت‌ها باعث خراب شدن رابطه شده و همین رفتارو در رابطه فعلی یامال با اینس گارسیا هم میبینه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101831" target="_blank">📅 23:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101829">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAt5iPLj__t7lMIrQ6cs4d0XSal9EUzZ0hnGzxpWBseSUwKIiDfDk0j3Rsg1KbtzGJxGWjUuTruvkQzjYs0q5XQVoUgzaAkez3N1z0P_zxnnLsMlJqQrKov1aFuyvtoHXfcnJOgF_7XprNMfHZwKJTgMyLZ2nHqy6gHv2H2KC1SRCjvANsktpXdD-5MyB3vN2R4aYlJzoPZt16IkmduFmwDhd8Cm420ue9jWpfHTrxkoSYmq95U6GAOyNx307tPenF_OTGXiFz7ePxSjS1faK5CBBp6roM4u3gUCb3oidcIQlsrV4NL_3OzI--XXC1EEnqsapjZzka4wcGnY_cLH9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dg9ko3xT0_2JsoswkBJovv0oDTGFU5sVU6aOqsY7PyNlm1bqlJs4YSfzjq9hMAJuWGHPrMKIgzD6TJYGYvpuGus1XIsfB3FS0JJfKqe_Uo7kKUPzbpspdtr-ONQntNB4XbSQQYZVHhCOj43BGRIToUXW0ZGZ_FynQbo2QK9n0NBSScRwljIAPRkmfvDQVt-EnVnfR0OGVITNswD6HKJ404KD-iqhQoo_zewAwp8oij00xtuOAz6jstun_ZP2VJ1fKx0z7tEI0-K0YPqt3j3y_Yo2p2rYMB0StRH36J-GdxaF5Q-1NonmuGyhKFuZjLz9_ubGumaS3B3ZWulDsjI1EA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔴
زمانی که رافائل لیائو تو میلان بود دوست‌دختر سابقش با استفاده از مدارک جعلی تلاش کرد ۲ میلیون دلار از حساب‌هاش منتقل کنه، اما ایجنت لیائو این اقدام رو کشف کرد. تحقیقات پلیس میلان جعل اسناد رو تأیید کرد و در نهایت دادگاه این دختره تیغ زن رو به پرداخت ۵ میلیون دلار غرامت محکوم کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101829" target="_blank">📅 22:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101828">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBELRp1JN_dytesghmoDqUaUmUXf-itP2FefrljwWo9ooqAfKaZ36Xo33M8q0QeKrAbfhC0q66RcYmrdL1fdLbiAiHcvkc-XGg_Ni5kzAGFP2KsHcLhU8it_VHLz9RdZd27Hm7fHK60acL3Rtbwxe4X6IDNiSbCItc21D2Ad0HYfTeBy3Sr5jGMx7Vel7vh4eYFOEyc-lSaVVPe-s8I2p-bXN-QOVJlHZsWC04_tQi1SgacyQpF64Okhoc4OGtiFc04iphOdBP4B5FWuGeJYgUl3TC6CpIL_ZrOqnHqFIoRu72Sy38h0gNlxDXS2TdodrURzbaI4w7lHf9aX07n2ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
توماس مولر در مورد ادعاهایی مبنی بر اینکه داوران به لیونل مسی در زمین امتیاز می‌دهند:
🔺
"در مرحله یک‌چهارم نهایی جام جهانی 2010، ما مقابل آرژانتین پیش بودیم و مسی دقیقاً کنار من ایستاده بود.
🔺
توپ به سمت بالا پرتاب شد و به دست من برخورد کرد. داور بلافاصله…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101828" target="_blank">📅 22:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101827">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpNkFkSeBqTrI0wpaRgGOMgIPQB1_VqmgWmf9TtgTcIfCgCu-OUtv473buM0XzzHa43N96xNr0Wm40qHvminLO8OtCgrZHREvR7gnA5F7xQkDR-fx9vbo8Qv1XrbGo2-pVhFw1Wa3g3YF0MD316A0-bziH_47N2tSa78TbIMMbyLDgjOQG5u0Sax4yHRJKKVILXsVw-pinV9eYlvZpRLr1WgObl26FWiAi9AqdDF61BSLAQ1Jfzu0F0ooFB1Trrk1p-n5O1aRdCIYdkp3qV9tYKEbUh9yBCkprBs_6pbFvtFiFoCgfLpH2ymGn7bXhsDkeJQUQmU2G7VP5Dc5YwvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇸🇦
•
الهلال رسماً سامرویل رو با مبلغ 70 میلیون یورو از وستهام جذب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101827" target="_blank">📅 22:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101826">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDtiSQ3T5kayivVpv2UbUwAsQGriPWhUh6QCJIKDLYQcBPWRdWLKVFlUtQxTQVwyoksuRk4Q_0E5GBcDdWBM1MjLcGwmw4uF-j52YiSzPuoQN1AVhWEhD3HbU6OqSJdV1mcwIs8yPGiAyIU8M7Y_aF5qEqXpr-uptHRTgVLuyihg3uxU2LoUh-OZz-uLql0ii1D6Xg6U5tnAzbJQX95SZcCQuCJjzaqL4kF3syAEwvGj4kPxDyQFwuJ3qI-jHEpKwBDi2oMlXUyw9REYgLakS5vl5XHKXrfiZNf_JrmhTv-RyPUW0B-DDA3cvVEg0A6u2h023xuJYfaZEzZH8L5ZNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
دیوید اورنشتین: رئال مادرید قصد داره که رودری رو حتما این تابستون به خدمت بگیره.عملکرد رودری در جام جهانی یکی از عواملی بود که باعث شد باشگاه رئال مادرید تصمیم به تلاش برای جذب او بگیرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101826" target="_blank">📅 22:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101823">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k50o01M4o1plzV76Y0Ixp5_QzbF4BP9nI49McDk4l3jgJe8GprtqBhy8YuTx34omZKhVjmssYJfWdrPjn80g-gCjFLEA33ivEjWO9w1xnxsqf3Su5YJqBEgAYthkyXlY8OXH1Z0JZMcxLESH0HIgnSOeim_L6OI3P1ODUKY_kz51Bo6LZINXtgpV0QGh4j7U6pkUAMLsyY_kqpH_e18i9ZIDuQ2rFYTEtYbGsu3XB12G0ZkNnSpit6Lpsawf2WGr0Cz70eAibiGfhb_cmUViNTPqIqaPqWUKDElTzQURvYwOtOWULRQS6twV_nJPkq55s-aIHcuSRBQnN2Mi9NGhDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
🎙
ووزينيا درباره شایعات پیوستن به اینتر میامی و بازی کنار لیونل مسی:
من عاشق فوتبال هستم. اینکه در ۴۰ سالگی هنوز اینجا هستم، به خاطر علاقه واقعی‌ام به این ورزش است. میخواهم حداقل یک یا دو سال دیگر بازی کنم. امیدوارم باشگاهی را پیدا کنم که واقعا من را به‌عنوان یک فوتبالیست بخواهد، نه فقط برای اهداف تبلیغاتی.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101823" target="_blank">📅 22:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101822">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XB9HU5ZK1y_pES4u6u2TlDRba_hyod27-NgTMHFx0oP92ZfocS-qG5dAHlXUgIPM69ryZlPIOqiSyv78xWbpokeNHP-7cb9bQYxlYR_HzfzGiM1cnqO9Z-EGEWR7q00njUyZ-Z_onyqOF9aopNSbSdMd8P8PnWkYFQ2Qv_Xyofll_FsrISJwJCvgdpjPAN2B8vZ7IW1lJFMcCw77ggL-q3jbXXW5lG3GiQRutVGs2Ngp2D1R7FnDbdiSXZLUlyoj7ogZ5clDiBCEb_YZsclE9Yk_HLhdQJnpojYw3uf0X1nemvqlSRklaxOPEY4qrDYjZDGAa0eUW9i19LtlAv0g_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
دیوید اورنشتین:
رئال مادرید قصد داره که رودری رو حتما این تابستون به خدمت بگیره.عملکرد رودری در جام جهانی یکی از عواملی بود که باعث شد باشگاه رئال مادرید تصمیم به تلاش برای جذب او بگیرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101822" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101821">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLOjewV3Gr_9ahfS_suOPBg73gCyBlbRqhpgwy22yZlTAnAxkEVzYzwIyOzLBkueCqqrEbHSIXy1394fSim0lDSXmZ3uuuN5uVubSAkCoud2hnoAjIcCV1RszoYxkAq-i2AgO6vllxDSk0KA4QzYnRq8fztI51RUphqkOtEX_YRaLFnUHOxQm8wOO6Ok5Gwh6z00RnptiMsqkCEmstx5oBZlAdt4ID3vg7IaGtfzNvnRQHnIC686JY999cxVORwF9lDqBdXHzoWlACm4Rc_hzviGvdIoMAMk4AFrxDp3i0_mx0HtrQ6kwTCabKj8q6pOhIsJpjWK7Or3BuMa7RycoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
رده بندی ۱۰ بازیکن برتر جام جهانی از نگاه اسکای اسپورت:
🥇
🇦🇷
لیونل مسی
🥈
🇫🇷
کیلیان امباپه
🥉
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگام
4️⃣
🇫🇷
عثمان دمبله
5️⃣
🇪🇸
اونای سیمون
6️⃣
🇳🇴
ارلینگ هالند
7️⃣
🇪🇸
پدرو پورو
8️⃣
🇪🇸
میکل اویارزابال
9️⃣
🇪🇸
آیمریک لاپورته
🔟
🇪🇸
پائو کوبارسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101821" target="_blank">📅 22:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101816">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7xcj1BPSTC4zKjjtvBWx3p2iZVUdapcmZ_QCKhh2nEmdvFYbAGPsRuZE3RDecyFs08SCBotb0_TxWeSfj4zc4dk7YgYwViQZvaPu8GgYax7Jz-fFIzIhnUwOJbLH45S5tHbJO1IQ_g7ZcSJ4u0oMW7wzh2t4f3gpkretcU93n4DCYrbq_gpKb-uosH65kphijOZ0Jbhjyhw8egUPstGJT9nz2JjeL7MiiUTleFW3n8ed3Q6xuNOxPR76k-lU1OZpcec-ZNRq7euSIWQKMDEdmnszL6G9_hxBEgj5ZMm6P4nUuzzUCAwgBG1adFr8qYhKd4157ivekb-ElDtZbb_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxCLummXBRR0V8rQFq203bbTBfwxvOHnxGvh6IncwbAn2T3RF6RFaT5hNi8_Nlu1Q7yFA4wCQ3Ql-t6yX1cJOGHFrF6tQsSKz1amWbo0KAf6N3feXmVzwUCJVsMKXiE_zZODB-6dfL0L5_StTMd7VP0I0p5N1aHZEzhkOZ4EkvsGK5dlsK8JQHKiHsSn6QEmA56TKrDFp65ya1wdD2Jz9JxvZTgRFkcLzD8iiIhD38HG4pvRemf6JpZKOaQtbJQjELiFzccaoKuMQ3ReulN6GDjzWC-g-_o5iMVqLYbqRffT3OD1W4lok8lBscrvNOSPdGvMlQKui0f9r3fPpRWMVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/goKFsU_9TRN-ta3XCsY2vO_nFKzN-I6ZYRMLXxBB1CBMq5u_HTrwqK-cf_guu5WJ2EqVSUqktWAaz6sYxJm5EKqay97V3fQ3OH2mLTxwLZK5YMh1j9LyVKrs0S9RbMiTtcH070chnmr5Mxk8rjcOu7CJeldOMZqeRnwuUx0maJinlKGoaDDWZvrrebQh0cgn1oxMiDao9rqs4Kd84JxmIwJPvwTUKQ3Gh6bS1xFF-wL2LFG9MolQ2QhRhP0i4HSxZtKuJNEJOV_e3PVIVAGxvkzHe9JyjsfrjBMup3btJbxqW8UxFQYz8J8Nz0fJUCItJGg9lIMbCNdhhqyMn-4poQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vKXB16wxGTL80Qr6VJzPhHpJ7A67Vhrkfsq7M7fwegkz6EXxQgbWMWkWxF-0ESVBCsjXk7oixamS3qI0iiZpzYdv01G08aurwuzQ_FbfQKBeVT1qqh6jg57zUdlk1e9Jw-KtPJRpRNoxCCg5Q-9dfrXShYw7Z_jnlFgOc0Q2SPy9kfXHC61Rw9DILrNnjgtma4U6b5RplIBaHIfwQ8DxsVJO1nQQBvtnRo3It0w4Zt5FWqeY6GQ19liYxXyUaRcdSh1IYO5AsSSS2Pfv8WIjceHapWQvpdfnu1T3CmHV3HMFrwWXN8GR6KYKmrmU3wA39-O8FwQXMoJzLpv304IEMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJsqek0flmiukt4Z9w86SwvdsQoPf0wHxDBrmZSuiBGGk2uKbia1uH0R2WlgdyaBgOlsW2UQz8b68KyKDpnIczQ_Q0xMW18-2-sbAPM92FSdPXR1UZiqKgWnFb1Q2dQ9S9uanwwozZBoIwUk3TASLxKyYHP3V-6L10HE2PzuRDW8COAcX5IhQXPNMmhTShEvCJ8Lau1NGAjvi-XTYi5bkaxR2uO-Wc9SPQ9hzuxgL-cSKZaQPmWWdq4-osRT69uk2e1vCruZHoGajKh_FSFR_YKAe28JZvaE6d6Izzf8hxqvHlx6l2ZBj8TatxWQEwr-HBWZLY4E7QdTQP0CsHBDzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌈
🏳️‍🌈
فران تورس با مارکوس یورنته رفته تعطیلات
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101816" target="_blank">📅 21:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101815">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEux3hSr_EyLFEDL3A8Z_Cekj9EORJmiIH7nUkmpeh84ChE7GYx8Vt0UbIrnkP7UETzBg36TKT49RxW9Dj2aGwi0CDgvphIL-1diMlwNWMkvn2WLdB6jDRCqgdLErTFFBF5Ya6ph_DMNA37m5olyy9BdLu71LiW8Tl_OSZLLO4GONKPgcGMtCUc8JILJv6JtzJTljV1_7qYe_1Zi8RIXewbc53DyNIv1Fq7qMm8qEGZRq9QKIwJirpchaWIIi2TTOX8GieaE6JxFeqOC11yWxiPoGC4x3cv8jU9H0FCeTp9JejoDklzlbO9ajOTMjNYT1sqoukY96cHQAbDYAgJrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال ۲۰۲۶ معرفی شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101815" target="_blank">📅 21:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101814">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbhFBmq260arm3fEGDVcE0ASX5xKIVgqwTh9b4zcI2WjZAr8YKYqlD0ce_cF9Q9SpmLO8Nka7tPhWBlrN0Myn49mK-OS9cMRjXqHxxtqboll8ttCSX9BdhXfUY33H1QDvFdpD1uaYa41PsJiuBU8ES_AvKviigh9h0wVs-RLX8Pc_w1CsYnNrNNotLC0YiCtgFJpIUuvp08iKUXm0TFRlJuqVGmaKffoN2wgJdTmfgQQn0GGb5t5zl511JpxYsayWX3mlaCiHm35p-VSl5VyQgvGP-fc_F21XpM9yT8dWxZlIb1DMneABWmDKPx0rOU_PZsJN6GrZG_KHJW9THxa1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101814" target="_blank">📅 21:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101813">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3wsmScmC8GSoOd1umJuMyXs_IAoFkgVN2a8KvxZbPpjtwbaHM-_9Xa4ImnKUqRSEfFQoUfgRHBbTcImQG-7FZMqMJKZ7hXMPXG4dzEzpSVrUWwgSfth7ZPeqPmr0G9EHWxlWR8zNSkY_Vvrh7sQ1-DIwnNa3RiTEQsWtD3DEoLEBJS2xDgO9W-7NfIskcXe8wiYND7RyvO2b2pk7JLJGOoVUXh_yuvuoGL_MlNlAL4wiNO8CPNgmkDwPK1rexZnCsN7eCLM7d087a2M79Lc4KzWyngJu1VKJPNi-4x8Epi5JW2KiLUqW1q3xLTGwDnZY4QFXAJrN9lbxHYP3dZtQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
کریستین فالک:
‼️
بایرن مونیخ تابستون امسال مایکل اولیسه رو نمی‌فروشه و بررسی احتمال جدایی او به تابستون سال آینده موکول شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101813" target="_blank">📅 21:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101811">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWN96zd9e-f4EDj-eq2KcxFj3S8VRosoActk10afebmAJHJi4dboBDktd7Yd89dFZPcHX3w0daS9q7KwmjyewzULnDug4HSm-0ueJG1bl2meA1aPZ-GT-BKZhEpAQjdvGIPEpf1UdLrGHoROmiP_wFmZQ7CteZ71cenomBp18pJQmF4rhpPmXhVWfL5xe03q-ScPK_iVrWPg46_bGox-T6idbauZYJcp3fpY7z4diUnWGIJO77JKC_u2dsLBuO-AOAMhSw5ylSX15tln1gJ26dytJ2H05j-2sm0o2ZjOKvpQq5C_dB9W8oXctajtz8_Z5bUxsOD3qQrBJG5IvyyDLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X4jUlj0SQCda3FQNcScC1W-xtJxYpNv3Rss0Lz3Wyw_Y2DXX7qMEVkUjCMYHYRo3q_SY0f0zaiZY4Oy19ognjlwVzYkam2QSODUR2dp4gaPjFZ_RKB-q4RneVnGnk7wFBhNQkbhkH44Oa3WXU-lzRumc9KpvMkhro2kHahmxycwPAXdWXjqYiRLynB-K1X1bjoZW3OHdIbGeyU8QxiZro6SC9YzhdVXEgB1n73EsSvAXa2hW_WSjRQtbXaLdBGuPKYFXhcJpXL2H4u6-2N-65L3ahsWR5KXzN7NmEZ1kfN6r7mqo5itubLLVAKLBxzC6J1ZchncTI6te-fO6aldR2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
💎
۹۱۵ روز پیش، پائو کوبارسی اولین بازی خود را برای بارسلونا انجام داد؛ در حالی که تنها ۱۶ سال داشت. حالا او قهرمان جهان است و ۵ جام با بارسلونا کسب کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101811" target="_blank">📅 21:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101810">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142d4e6b9.mp4?token=H3CthBqaGswDpp9FkooNarwxMHd1P_iOVzwo7odUKn0I5TMQenNtkq52IVlw3zrHnKok6spXh6zavF0mW-L__TVWegJgtDfBbqgSGqFIM42eK5Z46nyq9N7V13ALyGyMusE--F_WfckgTddFjewj65Y_BNFS2vAvk5L9j59360Hv35nGlwpfhoXaqLG60wN2etOBqog18pWrDLBKTuV8NE6USO8PuW28X3H-bx3EZQxsHDO6SQ7ZheeCaawfGSYq41uNwqBPCrX57zoexxYUSbXs9H5u5wexbzmGF3yFx38Y6r0C_QcHLHJgBaF8Jta-AnHAFK9NDjhxM_qDwim1_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142d4e6b9.mp4?token=H3CthBqaGswDpp9FkooNarwxMHd1P_iOVzwo7odUKn0I5TMQenNtkq52IVlw3zrHnKok6spXh6zavF0mW-L__TVWegJgtDfBbqgSGqFIM42eK5Z46nyq9N7V13ALyGyMusE--F_WfckgTddFjewj65Y_BNFS2vAvk5L9j59360Hv35nGlwpfhoXaqLG60wN2etOBqog18pWrDLBKTuV8NE6USO8PuW28X3H-bx3EZQxsHDO6SQ7ZheeCaawfGSYq41uNwqBPCrX57zoexxYUSbXs9H5u5wexbzmGF3yFx38Y6r0C_QcHLHJgBaF8Jta-AnHAFK9NDjhxM_qDwim1_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیرس مورگان:
چرا نمیخوای ازدواج کنی؟
❌
🔻
زلاتان ابراهیموویچ:
چون دوست ندارم 50 درصد از ثروتم رو از دست بدم.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101810" target="_blank">📅 21:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101809">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euCNY-lNNS7xn0eljc7imZXE-w2NH26cWJbGEi-QnDjRvuhImtBp-AVtPVTJVhdE4kfntyYmXxkUmc-1CkaVc5eEoB9inw02dD6ZhPi2pj-2B4QbesUaZP8Z1K0t1CW-NPseaYEq3cepU1elpjXcV-T7k0Kix5aEvbrkwJJNTpF6J3fyXZPHalV_cfDpJwRMs-oXiZSea8stsUN1xGt9YW_hcNNthLVxMQ_sfZZ8er5XVO_FthTjZVfSNXvmfTA4sSs2utOC2zro0kRCi-7h2rhjytXyrviF218afFX8osAQyB5jjcgGi7OescU3oYGjxg6dkbJkvs--1X2d_jgmjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🚨
فوووووری اکبر عبدی بازیگر سال‌های متمادی ایران به دلیل بیماری قلبی در سال ۶۶ سالگی درگذشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101809" target="_blank">📅 21:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101808">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwxgWjgkgr9xuw87OzQxUMfadcga7UksRFgaXu60ZW-_-YWDngYr2ze3g_dBhR4aDUR1RhXyAlrz38m7wM4QjvF7cH49Jb25g-gOtjhFTUaCLXBqwSWjUDB3EvYYAVaehi9cqD77wAM1gc3RW-bBd5tplfQL8pDNpnRyt_-ZsOw1gjJegf5L6yvNhwAh04WaQuf0lmzN2dhb3ynj40Lgy4w6cgGSsv5nn6-YI2GuYYPToQllAgqhF67TBFfGlq_GAsgzKvQSmnKnXwf4d3YCOA0lRBIOucmo0Kgw2jbX68DkEQzNhErwpCYRBrWGpnQatTycZcxGIR4UkuMyAbGvug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
کریستیانو رونالدو تنها بازیکن تاریخ فوتبال است که در ۴ سال تقویمی مختلف، میانگین بیش از ۱ گل در هر بازی را ثبت کرده است.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101808" target="_blank">📅 21:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101806">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZXiJ7ZJiS2KhB3shdLUZ3FxeTbHfU61clTwrxOgzXYggTCCdSuwiVnuF05cuNfp9M1Tb89FJ6qfbyZhLg4VIbchUgZyx4Hfs51E71p6vddVD5RMKzH18szM5vSxhkE52FeHzUDnwr5qTWUd4BLTYmWzsS8aWDmG2PPdCn4ouiX5bgEZlTyE_wQp7ednZHNv4ZcA1rnhcyxxODeTvYqfaDID2j_0WbjSkrMYC2KkK0ROYbCoZdMPlzyFOe1MPPFdbOu7_oiLBawCJin2bXCCsy84I1Xm189JzaYHwx1CdZ9T2H0EkOnTkCChadBY_wTF8fYhFoREY5sHkjkcCnbuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a81621b4.mp4?token=Bkoi2REqCarFi0ztyHccuCTC4ENq3dmW-1hA0VGUY11JQF50muD3koDnDeOZRy2O1TNbl-BVFJk2mF5tqeFK6eMK6lRtYLux8a1JJlYzlraKlpuDJb2Z1WDc8faD-LEdG6D91kfUjOOA8_JyjYxKecFAkKe5EWoY7FjW-sATH3sc3eUljN-dDMtvRgRQxK2BeZHvXP0NQCVJDoGxO2OffeQ4QsghWybZ_LzhEBIR6_UQ98MfxzqX3PhIuLNMFkYSaR3BiaHrCILr7bYt-0amlL-C8Dc2xOXDklS39CQSndYDgqpsKAC4wy2S-5XzxZe5kvLGUasBb_dr4-iQVCXqHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a81621b4.mp4?token=Bkoi2REqCarFi0ztyHccuCTC4ENq3dmW-1hA0VGUY11JQF50muD3koDnDeOZRy2O1TNbl-BVFJk2mF5tqeFK6eMK6lRtYLux8a1JJlYzlraKlpuDJb2Z1WDc8faD-LEdG6D91kfUjOOA8_JyjYxKecFAkKe5EWoY7FjW-sATH3sc3eUljN-dDMtvRgRQxK2BeZHvXP0NQCVJDoGxO2OffeQ4QsghWybZ_LzhEBIR6_UQ98MfxzqX3PhIuLNMFkYSaR3BiaHrCILr7bYt-0amlL-C8Dc2xOXDklS39CQSndYDgqpsKAC4wy2S-5XzxZe5kvLGUasBb_dr4-iQVCXqHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تونی کروس، هافبک سابق رئال مادرید، بالاخره درباره توییت «فوتبال برنده شد» که پس از قهرمانی اسپانیا مقابل آرژانتین در فینال جام جهانی منتشر کرده بود، توضیح داد
.
🔺
دیدم که خیلی‌ها از آن توییت خوششان نیامد، اما همچنان پای حرفم هستم. به نظر من، یک تیم واقعی فوتبال روز یکشنبه برنده شد. همچنین معتقدم هر کسی جام جهانی را تماشا کرده باشد، دیده که اسپانیا بهترین تیم تورنمنت بود و آرژانتین نه‌تنها شایسته قهرمانی، بلکه حتی شایسته رسیدن به فینال هم نبود.
🔺
به‌خصوص مقابل انگلیس، بازی خوبی ارائه ندادند. آن‌ها بیشتر مسابقاتشان را به‌خاطر قضاوت‌های جانبدارانه داوران و فوتبالی که مدام با خطا روی حریف همراه بود، بردند. به همین دلیل از قهرمانی اسپانیا در فینال خوشحال شدم و همان باعث شد آن توییت را منتشر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101806" target="_blank">📅 20:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101805">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdetRpkX-IaULYBaMFuhqaCQrzGyOgx71P8vAF564fuB2P9kHWikff9Sg9L0TKiSQHHnrsFgAqjoPFRT8oGo2qoubM8qIFXhQnSOUFrkJs-iKvrfwSmbvYOWz6OSequ19uwYdzkWUBG6dYRuZZIwa3Qs_tSLbKzKOMXap3NDFEDrRApzapZ5r7H1rM8ZZt-M1lSc08axc_gC7pDJ_1Xd-DYw8jILdR_kwYNp7cdD4UpPZ4KLUgrvQknfjE8-4c0RU7rKFI-gbbWSInSmO3iac4e7jEwkr20AUI3b6lKd6dwYn-gNn0CVyl29zT2--K7K0whweV-fpjaKgz-IG9Z0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لیساندرو مارتینز درباره کسایی که از شکست آرژانتین خوشحال شدن:
سقوط بزرگان همیشه باعث خوشحالی افراد معمولی بوده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101805" target="_blank">📅 20:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101804">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpImD531ym9jpkB9QMNCA9CfFX3SUQS1ZvvvzQPPNragmer-tZbz4OstlRfP__thLUc6qr7OpcKTLMEvWkHzQ_fJJ47VzbW-LuoM2Ih6GELHn9gGOe6dJxcZCv2voW7eRvjOA_A39vry8ZrEvPCtz9lRrDttFO5RkB_ptQskb_4lEziyPjZMTf-HUIlcvvle7C1S9PtuI_5SrzVaLpICb6SfgHvG0_AVPFT9d1zt6BUbFVx1eAcv6fYrf8BiHI1wsXh_KQnrIQjwcUjnpTbudAt4Y_XZXXpCsOxlT4viu_onxYb6OGsNonUTKSVUUxcWW9nuFJ97dt-q8ncYKK2A8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اسپورت:
فِران تورس از شرایطش در بارسلونا ناراضی است و تردیدها درباره آینده‌اش، احتمال جدایی او را بیشتر کرده. او احساس میکند هیچ‌وقت گزینه اول تیم نبوده و باشگاه ارزش واقعی‌اش را ندانسته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101804" target="_blank">📅 20:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101802">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RkcUSJPywdAajBVBt0LBGKpnOslQw3d2gWhJm3y92NN-9-PTTkeknTkfoVfWgLKU1SquYO6OsiL8LxzU5T4xxBx3I5CMVixtAr8it2UDFP5KWoXEJ7XIbv4kpIYp72JgIMr3MzhJF63SyeCeOJlVdpyibrzXN_upGHIAgSDrDvXyneHnd97owWuVIaZ5epd01EBWUP3cMpzhqUIcF59fj2DRg1CaTnnRewWk2lfJkl21-ZqZ07r_4uLCr3u8TdzgZTTJ79NB5ZcvaAKN5O5AjxiT0YCOItkk5YFdCxLvoZf1qRgdGeL0v3IKKN4T6cwl9OyDrRGdN34Ymsm-_tmFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9SLn0myP8JiKbG_qF6fA2GYEhc8tbKS6tsQUyjwYIR5cyc-haf34YY2vJ4UqetMP--abVcZenk9WKMKVVLPsuREAGoR59WCpWpsGFsf23ZJpkBxcZgX1c-5qL6_gzqiC-s6WL5AM4-wfD09mJSjnjNZUOsbZ_bsYfrFIJe3brTe7r-tCcfND0Fp6qeNPitR9zEXQkUjE1lejdRMNvWJ3NTagb0qXNLwBxH508Ilt9dDqAJbTD0hWwoIqygFXb2giPWc5e2W9OD1Jrm6KD7NCWuhgNRcTAAYwoMhER7VfUxZUDaCz9MVQNa1n-lsURc8E_D3WbNav39ROEm_MrJnfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدن سکسی‌ای که فرناندو تورس ساخته.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101802" target="_blank">📅 20:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101801">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FajfY-5QDaz6m6yY6s06MIWWPtxh5fFdI_FC0dnRIDusHz8tvIx-N3DEdi4bU6kqhqkGd8i07j9bLFjVkvrHa0QvUJgfE-sS6dzqOSIA0-GbE48EvZwPWWErd-dj8XseV5Y7dy1hnGFEq45m0R5cEaat1_9AjPFZWJLoIXSvpfoDbVijCXt9dB0rXajzQ901hapfpwfRCXlB5cb4hK-w91Zss0sMjUkvvq9698ZyLMSJjF-Sgouu41l2JStXBY7dGK7UcCTeLc2j8jrhemTDRXseJY6c0us99sHeSteQqHQJUUEipBPFXo7vnRTfMvMbpOHVE_HonfjD-zjMS8M06Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
لیونل مسی در چندین بخش آماری بهترین بازیکن جام جهانی بود:
⚔️
بیشترین دوئل موفق: 60
🎯
بیشترین دریبل موفق: 28
🅰️
بیشترین موقعیت‌سازی: 25
🎯
بیشترین سانتر دقیق: 20
🥵
بیشترین خطای گرفته‌شده: 20
🚀
بیشترین شوت از خارج محوطه: 18
همه این آمارها در ۳۹ سالگی!
🐐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101801" target="_blank">📅 20:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101800">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tM7u1yDhlOSZZJ-pC9XAVmJdpd0U_VNSYg_wl1HHXABH3z5W0JP8CF9JgjmmrQIIjWzxRaGhxdkng7bsOr0Qk8Y4-xCN4a1Y_HkTl7S7oujbOkZ0RGONol030IUcc50Ave_10Uv7__cftZ3kX-dNuzL7RKucCafQ1zlcPAgDXfaCo-VBaex3UFUc1akfPsp4aJ0AVWTB-d3tcVxmMh-pQzHdIAkdlWZRKw5jdSLDbUPLvqmpTk0iOloosALmKzjxTkhx5-m0RROQgZHIxcCETuNFwP7q6zgOmpDgyaWscWOv04428lvQf3JDCfgyIPx7sOH_U01BZ6ifbjcRCHCyww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
الاهلی مصر اعلام کرد که روز ۱۹ آگوست در جام خوان‌گمپر به مصاف بارسلونا میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101800" target="_blank">📅 19:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101799">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hO-5ksOPmqMvRBZW467m2mENJVG8pCVZBzXBA0K2989Nm4XZvhWCQS1QLBjbAlv3lxTOEyNqVzEJ3o70uuFi9_n3ciFnYwRm0L1oY8m6ihuEiUot3o7gdsznZVQkfBQvZHqYiHhvxMdvEWmTKR9lUVvBq_GYViD43pTT9F3VKPux2yOkxiYcLQjhbGWhMz3AVnXwrGgXrRqsbkX9uTXcRYg8nJvNotelM7acTxoe1LmuMXZPByVAACl85ZCYT8pMbVsZ9f7RSDbSdT5XTTwowzVFNRd4Jk0_C1nE9prZAqIhQtF4azaPDEW8L3rDjx8xX5O5tPZQaItHoEPSwhF0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
لئاندرو پاردس فقط ۵ روز بعد از بازی در فینال جام جهانی، با بازوبند کاپیتانی بوکا جونیورز در کوپا سودآمریکانا به میدان رفت! هافبک آرژانتینی از ابتدا بازی کرد، ۹۰ دقیقه کامل در زمین بود و حتی پاس گل پیروزی‌بخش تیمش را هم ثبت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101799" target="_blank">📅 19:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101798">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrlbOsNRnZk3bi290eWe_aWobsNljlhMoE8G_QD4ycPCj8gXyMdF_KKIJl7i-oSx2SBIJdFh5poM9AL5q6b_wZScp2ATwigxaACaaANPCsdiMSdq7CecZSfaW4VRf5P_VNkJKVX5SdXgh569jTmdxYqUCqeF7rJqYrMebJFsl4mIX1QnbccxxiBZetoO5yDvtP693qDf29biYii7XN3b06UDXgcjrA6x8feFuTeFSRRYDQJP4ZTc8R1EHRMv5rFb6fUmseenWq4zinhAdWX4s3RsMLchtIxYT7FrIrE9u4OxgS3WiYEbIdpaJX0ElpHMCRSWmuZNwoAYPR1ierBKYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
فابريزيو رومانو: پیرلو به تیم ملی ایتالیا 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101798" target="_blank">📅 19:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101797">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDe8eTknsxxDfiXXft90x5sZv-0NyMR9YkZf4hu0k5uiUSp-a9mBayaZDf_4eKLF_S8op12Lltqcj4aNEC5-WriYMCGfmL2UMhTmwsojAOz4orXNoa2Js4e6rlOdGRTamlCgBw4J50wN-i3UIrutwe1fwcOO27Y9PkJLbvkOXNW8kmF98L9JrdaY57UssjTCbjhbSVIuks3vI9isyWpWmOw-3C4BSQXIjWneltXvswbNg-1P-ddaLgB1yitW_mWpDVAD49HV4A8F8Y86gsy-VDuUZHPVH6s4iIXTMedwzjqi-7i974vdkstIN9EbXOOsta1Y2oSCoaDEaB-v6zUrfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بالاترین امتیاز ثبت‌شده توسط بازیکنان لالیگا در هر فصل از ۲۰۰۹/۱۰ تا امروز (با حداقل ۳۰ بازی):
2025/26
🇪🇸
لامین یامال — 8.23
2024/25
🇪🇸
لامین یامال — 8.01
2023/24
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگام — 7.81
2022/23
🇫🇷
آنتوان گریزمان — 7.69
2021/22
🇫🇷
کریم بنزما — 7.69
2020/21
🇦🇷
لیونل مسی — 8.52
2019/20
🇦🇷
لیونل مسی — 8.71
2018/19
🇦🇷
لیونل مسی — 8.48
2017/18
🇦🇷
لیونل مسی — 8.68
2016/17
🇧🇷
نیمار — 8.52
2015/16
🇦🇷
لیونل مسی — 8.46
2014/15
🇦🇷
لیونل مسی — 8.84
2013/14
🇦🇷
لیونل مسی — 8.34
2012/13
🇦🇷
لیونل مسی — 8.83
2011/12
🇦🇷
لیونل مسی — 8.88
2010/11
🇦🇷
لیونل مسی — 8.76
2009/10
🇦🇷
لیونل مسی — 8.65
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101797" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101796">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iN--Glso5G4uLLGVFR6OwOWWp5_cZeG0-lGr47LjUIyWF0lTqP3whBe4M6B_kv1nKqjDTFR61p9SZFeqXEzI-RQeq0xTy_Yxp9S_tEkAakxrAl6rOHH_eYrMP_ve8z0orswYmQGgkaQ4ceue1HKdDfxDsn1a48ffateUHqCmHwC8sVPDYcY0UBKiImfM6FPF4fW7djOKDE5TLkbh5Lrt2IOdrjrKn3i-sfBYPtzWnBJ7Tp1t9uzhaZc8oDMM_grMfREkaRL5mU_eLKqHxQLHux3NlV-Ru7mRofdJxw_M1_Tdtz28v8fo2AH1aQaiVOwz-g6MENireGwSjn0xHID7XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💀
مثلث‌خط حمله فصل بعد بارسلونا: GAY
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101796" target="_blank">📅 19:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101795">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXBwddTGgDIPrDwMrS9JeLkNtqeApwitPlkCEoE0Js5jFdTag5wgpiNFLOdCqeSV5xW2Ism7UI41A01tgumDt_uzmE1doEikmb7tQ3wP8ospaqQgymVO0w_3oLKXSlWlpBvwyD0863WTCQUCrqYey0HAniuUqUE9rvAScoQYkAKNEQfcHSSsnsmu7zpZ9VSgWQXhEDGYkqSA0qYz8ZWT9cXgWqpa-OAFIS_IOGP9Cp6Rs9PO_rl5JNwD62IJTWn-5YWrjjieIps3F9zlngJhywhm88wzy5beQYs3d1CEUQ2gzNkL3msjB5GJnz8mUx2DY7g1WlTuUou1-_0mIHEVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
⚽️
بیشترین دستمزد هفتگی در سیتیزن‌ها.
💰
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101795" target="_blank">📅 18:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101794">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1da4d2bb8.mp4?token=CppnEG3rmREkEPa245rXu2g66Ai85XqJJp8qSLGryly2VcwI5c_6RsBcjXwHHIsyXG2c9p9cT7VZQKe6sndnyydFm3-cTwt1nKRFrBQSKTMZgqgshievVys7kaqlDTrmWO9Rc48pFE_HRxz5y3WJkjZqzNSeadXf-3VajcvofEoooKutoaMHWYisu3SmfTALOGzPDsXRJ9O8gsIT9iv3qUijAw6BmpR6hc_toNZ3PrtlBa5EvqKmo8WoAYc00flVWU5_9ACSqMPE39BXHy5_fIFRzvzu_l0TpGHZXpDjpC3g3KzfyQrqdiYvHnhWjySN-iJDIAKoXjWrnarAy8RMR4JAn8cAvtDeL4-SxqAyQ9iHd8sbLu9sjABn9UknAVcv9TZftqDPdqslZbn-YAKwOGy_L4ffNMes8h3vhVyczBZfqW0xzReWpSbs5qQGTQtpmvi3NSBFfD1inDOfK3iOXtZwod7j878sT_Rh8XXGjdwGtHlzDEA-3ubF3YG2tkIZvtRzCoEkXjljUe-XRXvw_HbZ5MQZPs3tpRK4iZWS8FvLgj-b6m8C4zyaoGSWxII0Cd1N6YHH4P8Po5Xsgcq8hbrbEAG7XT_HNvmD9ybJRyUijUGcaIS4WrS3ehUJ7bHUNlyKCnNlwbhgD3CuKnSdgTZ2Qa8jTMRM-ZlqTBuDBSo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1da4d2bb8.mp4?token=CppnEG3rmREkEPa245rXu2g66Ai85XqJJp8qSLGryly2VcwI5c_6RsBcjXwHHIsyXG2c9p9cT7VZQKe6sndnyydFm3-cTwt1nKRFrBQSKTMZgqgshievVys7kaqlDTrmWO9Rc48pFE_HRxz5y3WJkjZqzNSeadXf-3VajcvofEoooKutoaMHWYisu3SmfTALOGzPDsXRJ9O8gsIT9iv3qUijAw6BmpR6hc_toNZ3PrtlBa5EvqKmo8WoAYc00flVWU5_9ACSqMPE39BXHy5_fIFRzvzu_l0TpGHZXpDjpC3g3KzfyQrqdiYvHnhWjySN-iJDIAKoXjWrnarAy8RMR4JAn8cAvtDeL4-SxqAyQ9iHd8sbLu9sjABn9UknAVcv9TZftqDPdqslZbn-YAKwOGy_L4ffNMes8h3vhVyczBZfqW0xzReWpSbs5qQGTQtpmvi3NSBFfD1inDOfK3iOXtZwod7j878sT_Rh8XXGjdwGtHlzDEA-3ubF3YG2tkIZvtRzCoEkXjljUe-XRXvw_HbZ5MQZPs3tpRK4iZWS8FvLgj-b6m8C4zyaoGSWxII0Cd1N6YHH4P8Po5Xsgcq8hbrbEAG7XT_HNvmD9ybJRyUijUGcaIS4WrS3ehUJ7bHUNlyKCnNlwbhgD3CuKnSdgTZ2Qa8jTMRM-ZlqTBuDBSo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
اشرف‌حکیمی و امباپه در کنسرت بد‌بانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101794" target="_blank">📅 18:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101793">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b632e2b27.mp4?token=covjcsGBfiFdsHI8g5YM_6jgCmpaWcgvkbO21uePrsCqcFDgU2ZBb5K3VAOR2CiTUaH8VzMaSYMr9Cup9akuon94w69VVEm7ewgQN07VfFj021egHsnmJSRlpA2cXbL6Oy_UVocwPAOlsdcCvW8fOKn1IRDoS2msJ0EJtGns1XYrqVtTkmZdhr4ilA4qyod3CVvEcjcYUa6Tka5KS4yNh-qworohcrgYHCqxuo_iB0skvxPcxx9jQczhtGNjZQ7xo-kIY8NgZI4XiwAOMpCbk-bftqD3kgrjSlifKygNR8OGej4e3w60KBruM1VKCQ_qNxJjeiBUIUep41f_5da12g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b632e2b27.mp4?token=covjcsGBfiFdsHI8g5YM_6jgCmpaWcgvkbO21uePrsCqcFDgU2ZBb5K3VAOR2CiTUaH8VzMaSYMr9Cup9akuon94w69VVEm7ewgQN07VfFj021egHsnmJSRlpA2cXbL6Oy_UVocwPAOlsdcCvW8fOKn1IRDoS2msJ0EJtGns1XYrqVtTkmZdhr4ilA4qyod3CVvEcjcYUa6Tka5KS4yNh-qworohcrgYHCqxuo_iB0skvxPcxx9jQczhtGNjZQ7xo-kIY8NgZI4XiwAOMpCbk-bftqD3kgrjSlifKygNR8OGej4e3w60KBruM1VKCQ_qNxJjeiBUIUep41f_5da12g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی همه چیش بهترینه، حتی میم‌ شدنش.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101793" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101792">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e74ccace70.mp4?token=jB8sPAJrjpmOGNuLB6vBCKlPNgrLAOJot-LByTc6NQlMS1SW22aCxiLQpLXObuZUhaZbH155C-08u2T4Zmyc7Wb9y5fu8rZrftuLnK2aELNhGOVHMz_VkeGN_7TMjiihF7idzDeSEtAAqzWhZQeTF0N8QKYYylgm5sgKaPT3V9bdhr-ZYdDW9g-bOw-RmDFFwMGjGCCV6nsSGbFaZFF1Mxv-UOXCf-szosPvVqEdUFx9pvcIzOU6aPUrtzq6dBVu7KqNaphAPA3EY-bOW5b5RD7zn7I6f34DlYMlI9L9w_glkcu3Es4-G7aJ_J5t-P9Xh7q4L36DeZFneXPYLygeUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e74ccace70.mp4?token=jB8sPAJrjpmOGNuLB6vBCKlPNgrLAOJot-LByTc6NQlMS1SW22aCxiLQpLXObuZUhaZbH155C-08u2T4Zmyc7Wb9y5fu8rZrftuLnK2aELNhGOVHMz_VkeGN_7TMjiihF7idzDeSEtAAqzWhZQeTF0N8QKYYylgm5sgKaPT3V9bdhr-ZYdDW9g-bOw-RmDFFwMGjGCCV6nsSGbFaZFF1Mxv-UOXCf-szosPvVqEdUFx9pvcIzOU6aPUrtzq6dBVu7KqNaphAPA3EY-bOW5b5RD7zn7I6f34DlYMlI9L9w_glkcu3Es4-G7aJ_J5t-P9Xh7q4L36DeZFneXPYLygeUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
عباس‌عراقچی وزیر خارجه پزشکیان: توافق با آمریکا بهترین توافق ممکن بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101792" target="_blank">📅 18:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101791">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dpu0iJIiKpp8Tjh0N2YzQ-2eXqwQqXQMxkgLl8pCgEJ3kM7KsShejh7ySRNkNFJPv6Co5R0n7UwtkrRcRz6HWGklfzbRCuKfCQ_IH4vEDoYLoAixbpOFcitT47_t0JHlKlTOHzpwr1IiYB0FcxebtgtpZdfOoQMiv7g2k0etnp3ppdHSAa_ZOdKK0T1x2mvGOg3iTdKS9zsR8TMg2bM66Ivb8ml6ee3OxhYx-yJRVmIWLeUGwmpycLY6jDeivIrOfhC1oIFNjoKf0OM8T7qTeao3LOfNlNUG7orF4KBqB_aPQ2QZWsKz6GDUGelM4YSafEQLyY-0hQvY-Ogmy16q5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
💣
💣
💣
💣
💣
🇪🇸
خبر فوری: فلوریان پلتنبرگ: رودری اکنون به طور رسمی یکی از مهم‌ترین اهداف فلورنتینو پِرز در بازار نقل و انتقالات است. مذاکرات با نمایندگان این بازیکن آغاز شده و پِرز با این انتقال موافقت کرده است.
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101791" target="_blank">📅 17:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101790">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👀
یک استعداد دیگه در کارخانه لاماسیا درحال ساخته شدنه؛ سال‌ها بعد اسمشو قراره زیاد بشنوید..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101790" target="_blank">📅 17:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101789">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhVCdV8PWPdGqlHsJgYL93J6UJ06zF6ARScRTDisLzlBVsXP57L94bVOI0nczyTvDBRdKJLbjjvTGM9aECp5wVd5Fmxe8XlZ8RiKuV867JbZkdBJ7YXXomYyU1Wnsno-10ZWQKI1xF0MQ5Q2bq2UAA6ihXRq_sX0BroYcGgDgc-P4WtRMZYqyGca9g9Rqn48SNSbOSF-MCFnF8eXTuNIeSedLGq3WQSGd6sShm8w9o4qCgPcn-KRBToR5plHGOqHmhRbILnizpmz2kgjOZAP43LpRyHiuoAqTvCQcQlFAYUmk8ETyIk_TPgkcyd15pgv7Ipi9gNpLYxpydn7rerpqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
✅
رئال‌مادرید به رودری اعلام کرده که مشکلی با عمل جراحی مربوط به مصدومیت غضروفی این بازیکن و غیبت برای چند هفته ندارد و تصمیم نهایی برای عقد قرارداد به این بازیکن واگذار شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101789" target="_blank">📅 17:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101787">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m_Go7M_jWU1DQJghOcwzSaL2ItwnOTJHQn7u-iQaCD7r79Q2Tax4GxguANewqsFY2eibfNcE6wsMjknisMK1Hd1HbrDdehJ9DyYQqPV2eqxyl9G3C3VTTlwl2SianIydyhLM2wk2_vyld_6Co0ElizSzW4dqj3DbPxTw0aRWhmLn5v95qUfadPb6Wuy30wG2_NZNG2OHXJDxGVCxjdwy0QOKpc3OEFxeHdnwd2btIYBeyrt_u7FAQ900DRWTbWMyR8KRKZoBHQ5Em2Y8YUK66XDq0qz-E5SzSZkKw1mGn-zywsseO1H603EoFhdaIeDkltKTzmZKXLtln0e5AjUQjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hNjrQ4tRAQ3SrW3jSAc3t4s8TzPByQhVw_-bMYjcoBQ98mybXuYb-Xzg-y565fmqV72iAFcZ0DG51FPO9l36yySySwlgH5q4FRbjnZl_x_LHFkD0ZKp27iE6a5LOlthG9VBoHYWv_M4CyNqSRQ62pO_EZYLvtxwSA1X9tIsOoZAoQfVgtAStunO7IVin5HMBN5REYo8ndOZxmZfNXk_9oerI8VFkvNyq1XzscO9VrQrn4zU_AzJc0VcRLqnATT8cVrvSDmRy9PZZwQ6_krWtNvzKaKyFw77oVR2Ks3PywoE_Hp5VU4Q69lGdirOdmXVHoXgewMwJ-JVqbPONChlvIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
مشکوک به نظر میرسی هالندعلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101787" target="_blank">📅 17:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101786">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpRJw6B4M0EBkUjCD9IqjPeVqfZqFjI16HvvYdPVuSWTdpOT9KJWhwZyZHN2n9rUSvrwVJtckt2XxMn2kW6PyUgQlSkvCuz54X5fdePQS-VhinjRejRbRixUIZHizq53fHLQgjEhCXLqueKWwEr5bIPCMoQ52BWrz-NzFZATd50Ei7bSbpTBfQLQ_VOGozyv_t-JTxK5LpODhswjZl1sa_Rnnq-2Yc2ruL_iLirKx-YgYmaG7c4RBWoIlegq4KkAtfCv46IwpbdLfIrv_VTPPkgNiel3z5P8XBdfhGDeH9Qvn314uautBv60L7OyKOyp1U1corwlo-fv2zZI_60Pog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اسپورت: منچسترسیتی با توجه به شایعات جدایی رودری، مارک‌برنال ستاره جوان بارسلونا رو زیر نظر گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101786" target="_blank">📅 17:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101785">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101785" target="_blank">📅 17:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101784">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJOmmBqCLpJ710TVZqsMzpcB3Nyin_vcSWDCsPNWNsNeIqKtrrAfGkHm3MGgQqt4q5jWa1kgwz-Ci7KsNHc3Sroiy4rRzFJGBzZz3T-8GW1D04h7oKGg5op8IJ8j8lngp8lwx_VDiZ9FKhpVoZiWW3uROuB3OMZ4xsNCB5I0FFfwXS8ljpaXiQVVxk2332y-2FfQwHeAEIZBro0ZMisfWtKJb1nhk-UF_gHrg8ahGj22mNsW6jn0GzGQ97aRDP718mVIX7GFFYKdOgkxP9VKw8P82vMV3M3O3cq901HwG7WDdUQflWV_ejX6aoQfepryVEtsjBYWVlido_LEiyTc7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇹
✔️
به نقل از گاتزتا دلواسپورت، آندره‌آ پیرلو سرمربی جدید تیم ملی ایتالیا خواهد بود و این قرارداد به زودی نهایی می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101784" target="_blank">📅 17:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101783">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1ed1b860.mp4?token=rGqyxTSNAUuaIyrYNAQnzeSfZLVarSO80hseR36tNTCBNzfGoqaRlk6Pa64jAT7xGndiDGVy3z7x-Eb-_BpWZyrr3MT58iEc5LHa495i5pWaAVXLnTz0O1PLUiLt_btCrCtJCwyt3V7yv5v2ZiD4aFRawgWVC3dGNX6zQOlK9rPtKR1DxxiWjdVStHoYj3U2gMLB8NXl9XAZOyfUUXHhmMOVq9ZzN1sd89oxw0KPUjf_5LJtShGfxRqjnIIRSU90nGkGy5Mg7cpieBsGImgiqj8ged0kxviKfcI_4QP9D3LzJmcOGMpjC_nkfxFQQJFsP31_SLWeQ36m-aKrPNF5SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1ed1b860.mp4?token=rGqyxTSNAUuaIyrYNAQnzeSfZLVarSO80hseR36tNTCBNzfGoqaRlk6Pa64jAT7xGndiDGVy3z7x-Eb-_BpWZyrr3MT58iEc5LHa495i5pWaAVXLnTz0O1PLUiLt_btCrCtJCwyt3V7yv5v2ZiD4aFRawgWVC3dGNX6zQOlK9rPtKR1DxxiWjdVStHoYj3U2gMLB8NXl9XAZOyfUUXHhmMOVq9ZzN1sd89oxw0KPUjf_5LJtShGfxRqjnIIRSU90nGkGy5Mg7cpieBsGImgiqj8ged0kxviKfcI_4QP9D3LzJmcOGMpjC_nkfxFQQJFsP31_SLWeQ36m-aKrPNF5SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدی‌قایدی ستاره تیم‌ملی ایران: اگر میخواید عاقبت بخیر بشید، بچه‌دار بشید
😔
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101783" target="_blank">📅 16:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101781">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kgXcS4pIVeAvkyENBzXHzBr6sNgEgyI5qNgTfW4H16hoAkZoQa5uH3X5LWhn4NhtRCmSi6aOwgi1g5RcuQZqhxFRnPeSB_M6lXL91B9hNARQpvq1_8F13V5Iwm9AUw-_4E1y5WRudT4bfJMxaVDtEwkgQAeGmFDF1p2euwtL0IdnnSPyb82jECKz8PIuB-GtZve1Xon9eRdCPvKnrsMm_LiJ02V4CZ7QKIQNU3Tl7gVAupOAAllObPkX9T1PrG4o2GwRDpDwjfZA4rpBFt7mHP0CB8LLAHdbla5SodeLfu9GeGNxAuYvQ7MyJ76zFE4202rT84lSpVRBp03BMpOKQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sW_z9hkKUqwrnJ-MGOU9tvFrEU_6uLD4ZkWg_BTEqaN2venw2MIufyjDZEvBxmGGtaktJDrfEJO4E8sILqT90zyvG-xvatFgvoF0ghIag2oBUM5kHVy30S4waQ-9NAm_1YdsOMCHMZVvRBxKzRTMc78D7QUysoyjLh4dGBoOTx4OTh23ML2Ky46FlYKOILqGb56OMJwhMHWsJtbbiY4sxvUtiMY2mlxef6sZhrxX6qIM1jo2A9zNj4EWOgzX0DxYkYTzwYLLTepKMYG2L3Qeyj6vanAK93jZwAoaw5DyUjoH7ooiOJK_IXFtAVIoAKPSDa41_rQ-XE_Nd0oEXCyjwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
امروز، ۲۶ سال از جنجالی‌ترین انتقال تاریخ فوتبال می‌گذرد؛ لوئیس فیگو، کاپیتان و ستاره بارسلونا، با فعال شدن بند فسخ ۶۲ میلیون یورویی‌اش توسط فلورنتینو پرز راهی رئال مادرید شد. این انتقال رکورد جهان را شکست و بازگشت او به نیوکمپ با استقبال شدید هواداران بارسا، از جمله پرتاب سرِ خوک به سمتش، همراه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101781" target="_blank">📅 16:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101780">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQ3tsBiDYeVxA6-9pe63uNa6kHMaYahDXcc5Kj6RBXYC9hL5T9v9HR0ESEZB85uTv1oZLFs63w4TktBfuuzacDgYGH1z-lawhK5BjCL2z-U2qjCusxFrroz76TVTAuWIsdSuJOJb7lxQpKuA2prj2uzTdup6oEbS5A74UVAnOlj_A3e9Ock1QA8-1aFW9MOQhTXtJLFvI3pBw6zE2NslqS-T6IjjJpMZYlhswcOvOyIzPR1YjQbhestolQBDnyuk1I_FxzlAE2Iz-boLBTE3tPQk0ZZ32jBdO0CPJosMUw-BYSx0CQrhhRvOIoH0iwVRPUeyc131G0s24F-a3Q6oPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینتر دید کسی حواسش نیست رفت به یه تیم از دسته 5 آلمان 16 تا گل زد. دوستانه نیست این دشمنانه‌ست بیشتر.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101780" target="_blank">📅 16:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101779">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f574b376.mp4?token=CTMK8B461SiLd6mILheXNZ05Z3PsRyIe2DLBUROfwH9vVeHCws9_aFvk43O9Ny4_5gFWzHyqRFTJoQ3uFBGEyWIBrm3HUYYNf6jW0dDelVkKiWuwr3YFMwbW-NGNj7NEBvu8zpD7id4QVdTpbdJjNBAkkojf6l6JKx3OxukRIEBWzxvbYI_FGhvLATdl_odoEGMtfGvu7NHEOToKAkg5_rjgcNcdSPvSEXodu3We3_1w54O3tIr50ixHRzHRBXOkVVZSqv80F_ke0VPkbMdU9FgB6JDmJG3JdBKXcAn7g1_PaBkW2nwbGndSh3iJStmM9ulHBDUk3SGniK9OgKfRZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f574b376.mp4?token=CTMK8B461SiLd6mILheXNZ05Z3PsRyIe2DLBUROfwH9vVeHCws9_aFvk43O9Ny4_5gFWzHyqRFTJoQ3uFBGEyWIBrm3HUYYNf6jW0dDelVkKiWuwr3YFMwbW-NGNj7NEBvu8zpD7id4QVdTpbdJjNBAkkojf6l6JKx3OxukRIEBWzxvbYI_FGhvLATdl_odoEGMtfGvu7NHEOToKAkg5_rjgcNcdSPvSEXodu3We3_1w54O3tIr50ixHRzHRBXOkVVZSqv80F_ke0VPkbMdU9FgB6JDmJG3JdBKXcAn7g1_PaBkW2nwbGndSh3iJStmM9ulHBDUk3SGniK9OgKfRZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
برخی از سوپرگل‌های لوئیز سوارز در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101779" target="_blank">📅 16:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101778">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3068c762cc.mp4?token=fP8Qq9bhC6f-1FmVhe4IEDOCX_dwA6KnTQOHWS37mqM67X3ZQAog8OyIZJ0BEm5KPEROUcIZkDXjsC3noKO9q64L_AQ4ofXM4UxW_ZdxYfzS0nqJzj-LsHxFj_68wYa4OI_RPaBNCdkXoRQt71s1gVPEGZvaVj2E_qu73cjWG1UW-bH09-G564AA_cX4d53qtzikkf0zNYtACPUA0Kdl3V7pCXFOGPAc3apo6k7a60PB0sKj9-5M8aPlOAPfkN41ed0Xvv_mf1ZMwhbNeJD880SG7Oh0s9Pgz6EDK5kTj10hYbHkJqLi-kIQ2Y2nNsiWga6Ldf84DGR0khzPKEtSE0dHHgWvySZZJuYvGWaVptTcqRA9pdrKtaRPd0PK9W25eBvYyclWuVnqf-uJqupQQ1U69afUmz4seXVy7dRk60hpgfd2Np8A4yopjN4AgQ7F1u5vbs_98U8Mk4ij1wsxJzFL5-bsARTmxCC4npI6KMG_-1USl3qCor_lLJp01D228xXt5nwFFXXo5OFRKYo3xncu3BDbkbm-W_lM3zrXZeFoL9ceMEU6DocFaWKwRm5BbYPYELkGxxgehIw-BcvTacSx5nV7UnJ4hL1HS2c888xxE_42B6FZqIOU5itAv69Ho2K1ebScTDhWEV0NeMjB2OAUxwyOchCmh07QXk5iFFU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3068c762cc.mp4?token=fP8Qq9bhC6f-1FmVhe4IEDOCX_dwA6KnTQOHWS37mqM67X3ZQAog8OyIZJ0BEm5KPEROUcIZkDXjsC3noKO9q64L_AQ4ofXM4UxW_ZdxYfzS0nqJzj-LsHxFj_68wYa4OI_RPaBNCdkXoRQt71s1gVPEGZvaVj2E_qu73cjWG1UW-bH09-G564AA_cX4d53qtzikkf0zNYtACPUA0Kdl3V7pCXFOGPAc3apo6k7a60PB0sKj9-5M8aPlOAPfkN41ed0Xvv_mf1ZMwhbNeJD880SG7Oh0s9Pgz6EDK5kTj10hYbHkJqLi-kIQ2Y2nNsiWga6Ldf84DGR0khzPKEtSE0dHHgWvySZZJuYvGWaVptTcqRA9pdrKtaRPd0PK9W25eBvYyclWuVnqf-uJqupQQ1U69afUmz4seXVy7dRk60hpgfd2Np8A4yopjN4AgQ7F1u5vbs_98U8Mk4ij1wsxJzFL5-bsARTmxCC4npI6KMG_-1USl3qCor_lLJp01D228xXt5nwFFXXo5OFRKYo3xncu3BDbkbm-W_lM3zrXZeFoL9ceMEU6DocFaWKwRm5BbYPYELkGxxgehIw-BcvTacSx5nV7UnJ4hL1HS2c888xxE_42B6FZqIOU5itAv69Ho2K1ebScTDhWEV0NeMjB2OAUxwyOchCmh07QXk5iFFU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چطور در لاماسیا، مسی و اینیستا می‌سازند؟  اینیستا و تشریح سازوکار خاص‌ترین آکادمی فوتبال جهان؛ استعدادیابی در سرتاسر دنیا، مطابق با استانداردهای بارسا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101778" target="_blank">📅 15:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101777">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">▶️
👤
به بهانه تولد 49 سالگی مهدی مهدوی‌کیا ستاره سابق پرسپولیس؛ تمام گلهایی که در در تیم ملی به ثمر رسانده را در این ویدیو می‌توانید ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101777" target="_blank">📅 15:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101776">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKEFs3h6UA47HDJYhPAU_0qvHlwYbK35MxPawUub04-t_PgOCNswSMMj8PYbPnQ4F6blVIThv4yBHH35H3PkLLXlup0I2Ix8usaG8BSjaRcJAwNjDUEH0Ii3NxPEZXv2aaB92Nz_uQc2mfI7gCzeaI79IcHeje53lBx5b26fQIodQwtP6efSdWAIl-l-ALgYLpEWkMKTAD76RfQOX-mKQXO97IYfh7WryCPo0ZZIHL8z2WdKGI4RviXgYM-Osr_H2FasMAH4slZxfgckk6i3p7vo-tz_ZwmTUS_aTjbMz_8zWKeBQUPSwGxwp9pcjTfnCfTeqiAu-r2WI1QfXnIYAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇩🇪
یورگن کلوپ:
با چیزی که خیلی مخالفم فحش به خانوادست! اگر به خانواده‌ام توهین کنید، من می‌روم. اگر روزی فکر کردید من مربی بدی هستم، مستقیم به خودم بگویید؛ همان لحظه بدون اینکه حتی غرامتی بخواهم، کنار می‌روم. من این کار را برای خودم انجام نمی‌دهم، برای شما انجام می‌دهم. با وجود اینکه دیدم با ناگلزمان و توخل چه رفتاری شد، این مسئولیت را پذیرفتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101776" target="_blank">📅 15:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101775">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcNTrspHIHUHCq1KivZrucfuzLXnjNnM8Yv4pUz4cK77PBrCKR8IvcjBjerLVJJDuvXm4NmD9WTAelt4E5d54Ee1PMv7p5WpxBDh75SaPijRqD0bRPN059J3Ws2029OHP0YU6XT-7L_eb2VdESE5u5_c2RJXj5WBqvx8RmZ0Ip5yyhNFEfUgJVTUjQm3E7WqZUYgdr-8JsVCWrdqGbTR33o-kucQZYsG-YtYTpwZpNSvX3J-k6qkxXHHwISdS81i9hPX50J2VGG6Ra0AYtdN4Awqbzh1aLAUfTmFv-fMaeSS1sRh3FcZIFh_sBt7T6CyAvWdL3eHbigbh29e2EK38g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
دنیله دروسی:
عشق من فوتبال و رمه! اگه بازیکن رم نبودم، حاضر بودم همیشه 10 ساعت با ماشینم سفر کنم تا برم استادیوم و تشویقشون کنم. هیچکسی هیچوقت نمیتونه رم رو بیشتر از من دوست داشته باشه.
تولدت مبارک آخرین گلادیاتور رم
🎉
🎊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101775" target="_blank">📅 15:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101774">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qd3VB9faGpl-g2z5kgKQMKJbmTvLnRu4YIMknUpry_SrDYV1kLkFl6tbJg5YjtAvN8DUkq36X4f1Vz8rtJSyCjFkE3--VcyaSAFBdMyrNANv2h16GiexVWrA_YYHrWIlfcsV8eODKhmGi8FIfXNFlIwgIzKDcW5NfpOI17n3-RlooglEmnTtEzMrc6NDgUmdAOEgl55tTo77YWHMbtoWK-IF1Sx94rJmDBO3mcaN24IzS4nqOuOKJ3R-qxQQJDXb1ST0UC4VkRJR_SXkQUNMmaLIGdVi9ADIFkPVO1W-aAnlp2p3xpk-X5s_P5vEWWSS1nvFWVfNuEecV5daEX3FRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
قرعه کشی مرحله گروهی لیگ قهرمانان اروپا 27 مرداد ماه برگزار میشود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101774" target="_blank">📅 15:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101773">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joKHYCivg5cVoZCZma7x9RRI_9HaxcqLXE9srwMuiogo28W9L8GoGqsuN6JMR7gT9lRkOVPwSxYXIVkpzMhEAAaHGQBanHVMRGUKc06kdhmQHur6WG8uKyJg0ZYQK5nr0kxiGBDb6fqEV05qFUqRqP3A2sk6U3vrCtEZwRAU29dcS8ADKr2MFN-bx6eQ8QMxWbv1zLxnlE3znYr4lO8H58aMqS_daszRKM1jGkEn6o6R-9BIaNH-4qjW06nA0vFxlqLe9z8BXWB9ngKDhqJp6662VIZsxVQG_Ha85pw46fUXIe-xntpnmWwvEswqlB2ykuKxVRXR4ZwCj_BcYScBEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
📊
مقایسه عملکرد نیمار‌‌ و امباپه برای پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101773" target="_blank">📅 15:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101772">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmt428Rf-BwYqMu2mw2RCywkIY6vRvSofzZobFxv1oeXW2PrjPkqOuHZQ8fTARjuWQyG3n7P2m2BF0mUazQ9g7CiyPnJkwn2nH4rW4smrJbtMpBZi1YqN09uIXiMrZmnZPzwgD0B5vpGP0VLs7nm7iD-2pOdh2T5gCLko1fMT_YAVps6ONppNl4RraSSCZIazOi8EmJRJKCZKKBh5nqDcsSBeHVoV0NwptMq4NOQMgoRZm9glTFiXVnmWB3Q1I6d9vvLZOQ6jZgLv1ioXFzZ2QYZ2TUoFis8hqO9eaKDSpUH1b5uq2vK8xMKvcuFVp7a0mBRAXWrwFrirpfXrFNoMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییییی از فابريزيو رومانو
🚨
🚨
🇮🇹
🔺
پپ گواردیولا پیشنهاد سرمربیگری تیم‌ملی ایتالیا رو رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101772" target="_blank">📅 15:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101771">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrIeqzAIVCCIt5EPsjEG3icLcS6HEzBqO5DAyfd22-6SJh0McE7kp7nSHnxUrp93g2wdiCnD7EZSYbPFwRJCK53JYpzgiyGiGYFNDz5MRYaC0F1k8kvMD3BG1W-2p4dllPMD7vqsG58O-LH9DEHxoFs9RGRfLIkSaYhSMHf9WAjgj6k-fRHPTMzUMjI7zM59wO8sWuhDr2bHEPov7NVmW0h6Xpj5UC4JA3aSZevGY45PHpQUJhiuI24lb1d2FPvkSWYptG6B3N4Gpoajjrh21Zt0KhvnCbmCx0fEObBOJOj1T12HPSbrEJreFZaukx8xed5jdCaslCJf7m3wmN71mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اندریک و خانومش و بچه‌ای که خانومش بارداره به اسم کندریک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101771" target="_blank">📅 14:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101770">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saD1P7GegXcxnBAYev8L-DgtzIM71OUiJcIY_TdKpMxrdEDdqROqTPUBhBwcUDmO63WflCjRabEvNYkRFcivSp6wmH3aYrWy3w4ya8pvTbsisHmNhAAYvwk9XzWO-W1rjkJ-7TSIYrVyzmfkaIvhzAq1tOoBEeVIyAO2h0X9lqPS-PZghovhjr-4hoqiardUEkLqkJZ5_r13wB_E1JUyub7h7-iT3Nm58wZQhiqMFKEMD_rmnSAprxrKThJPvXbkjzWLZnlYSEBM44ovyJxsTBArQfd__ijW2rxEV1ARCAbtGcSHk_0IoBoHDuPcOeiV2HUQGQueqgDM7iSFobhFDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚑
🔴
از زمان پیوستن به بارسلونا، فرنکی دی‌یونگ 416 روز رو به علت مصدومیت از دست داده که با این مصدومیت جدیدش احتمالا به 566 روز هم برسه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101770" target="_blank">📅 14:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101769">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/accd9e1667.mp4?token=RFsmCP2SwT8lF1giaNRU62B-VM6PdNLr5dH55JbfRxdL47zPeK6qhbDH_vyHzm2dpPKVbq_Qnb3mi6-ZtdH-B2jz3ECWcS27nRt2KUwpSJTQhUDkkceqmnfpnOK8M0nKGFKU9Q2B6S5Jwon3GxRvow8ChAivf76rdlyhSle7N01hAtUz2liXfLjZwtgTsbUrcZ-2EVYt2DruRR4j4bFV_fm0VjvgF_TXoHRbKkBn6UbzkUj7XXPtt7XREyKYsovaPMKPwvtSbWaS5dAG3w_djFaylCHQrOqiJ9tfr_BVdpbxxRavd8sUX9j87zDoXTWRa-59yVJIrXI2BUQfO4k0YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/accd9e1667.mp4?token=RFsmCP2SwT8lF1giaNRU62B-VM6PdNLr5dH55JbfRxdL47zPeK6qhbDH_vyHzm2dpPKVbq_Qnb3mi6-ZtdH-B2jz3ECWcS27nRt2KUwpSJTQhUDkkceqmnfpnOK8M0nKGFKU9Q2B6S5Jwon3GxRvow8ChAivf76rdlyhSle7N01hAtUz2liXfLjZwtgTsbUrcZ-2EVYt2DruRR4j4bFV_fm0VjvgF_TXoHRbKkBn6UbzkUj7XXPtt7XREyKYsovaPMKPwvtSbWaS5dAG3w_djFaylCHQrOqiJ9tfr_BVdpbxxRavd8sUX9j87zDoXTWRa-59yVJIrXI2BUQfO4k0YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
در چنین روزی، ۱۶ سال پیش، ماریو بالوتلی در جریان یکی از بازی‌های دوستانه پیش‌فصل منچسترسیتی این حرکت عجیب را انجام داد. روبرتو مانچینی آن‌قدر از این اتفاق عصبانی شد که بلافاصله بالوتلی را تعویض کرد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101769" target="_blank">📅 14:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101768">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=hSmwjvorogRV9skl5GCiWOMsCroFKVbYLnQOriHuIs1AXL8_uN3Sselzkb_LAYg0jZ9bCD1jyQFRoIUt_5cvl35_zijGTANh0I3362d1efiiqfHkMekAdSOJpbIMsfhZK_P79acXn44vstVGWik2H_rKXXD3F9KVA23kCT-FO2KxpJNyqzI1PB6j_VgGpb7_GJLOL9FntYKux2moL3XoUyYgtblNogKn1xcnTx0bVsuiSkr6VqD1ycd8uaNdTIYyj5n3mOHlq0dnUPcCSBMjic5H69n0OF3mzO5bibIxtfETsuntdRJ3IURmHx5kDuUr3fW8tisfdLAfRSF0-vOrdTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=hSmwjvorogRV9skl5GCiWOMsCroFKVbYLnQOriHuIs1AXL8_uN3Sselzkb_LAYg0jZ9bCD1jyQFRoIUt_5cvl35_zijGTANh0I3362d1efiiqfHkMekAdSOJpbIMsfhZK_P79acXn44vstVGWik2H_rKXXD3F9KVA23kCT-FO2KxpJNyqzI1PB6j_VgGpb7_GJLOL9FntYKux2moL3XoUyYgtblNogKn1xcnTx0bVsuiSkr6VqD1ycd8uaNdTIYyj5n3mOHlq0dnUPcCSBMjic5H69n0OF3mzO5bibIxtfETsuntdRJ3IURmHx5kDuUr3fW8tisfdLAfRSF0-vOrdTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
کدگذاری به سبک قلعه‌نویی؛ واکنش قائدی به حرکات عجیب قلعه‌نویی کنار زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101768" target="_blank">📅 14:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101767">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUBk5UW53Bu85OZWIKURA7RGv6fnh7hm559uLKeg3zG5WYdv5JjFwPVagE1vw2NUAMIir-a1NsoXSRC3tmjbfgwboT7GTb76MGhzjDH1-KLEMNrcSD0m8FQftfiMedIka0GUnrxdUHO6IEDygGGApz3hd22hcsrSNO23EUs77j2WCz5KdJrhQ0GWaRPDZMUDiXwkSlwX6ITdZ104WoB5CdaCzl8PLQFsYz0iNfUl7HxvmrFLFv5lr9Dnovfrw-D_eY3RhzmKaL_uHQAnfJukLZsxrC9VZYNsooIe33OtLmDV0zfDWFNLqIKQPGrd6d9Ix9vxIcpXhRQkHHRPxj6vMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نفرات چلسی برای اردوی استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101767" target="_blank">📅 14:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101766">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f65adaacf.mp4?token=iEvym2wVQoTscqP-KlBs2oHNb6CuQjgaEclT3hCNowlwh8PyxEKhu-xdBCK_jBbIhpazLdI_8peU5m9H82vW7_1xsqAPmc3uBXvVKdvB_cgMxILdhYPwpLoT4ex8ks34E4vk8vZRhKxbKdEQoHdGt3hm_nLEE2RxeR9lhOuioSY1k7ASDLt0lgcruwLXyek61qropHKFTiK4n-lfu6NOrm-AzafeQ1qM3lkAsgJu2EpyfOSpUjR1fPTyMND4FvjrCMBMQgHN3BkTANVdPGTiT_jOaivzBUkMtX1BxvOOPp-bTj_f_kJgnY5ljowMPsF9u-LegDHdxtvMKnD4KbNTcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f65adaacf.mp4?token=iEvym2wVQoTscqP-KlBs2oHNb6CuQjgaEclT3hCNowlwh8PyxEKhu-xdBCK_jBbIhpazLdI_8peU5m9H82vW7_1xsqAPmc3uBXvVKdvB_cgMxILdhYPwpLoT4ex8ks34E4vk8vZRhKxbKdEQoHdGt3hm_nLEE2RxeR9lhOuioSY1k7ASDLt0lgcruwLXyek61qropHKFTiK4n-lfu6NOrm-AzafeQ1qM3lkAsgJu2EpyfOSpUjR1fPTyMND4FvjrCMBMQgHN3BkTANVdPGTiT_jOaivzBUkMtX1BxvOOPp-bTj_f_kJgnY5ljowMPsF9u-LegDHdxtvMKnD4KbNTcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
مصدومیت شدید یک ورزشکار در جریان مسابقات مردان‌آهنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101766" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101765">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ea14c8f5.mp4?token=Mxqw0bgCYhE8Z53de7useu9RwDml3YQsvZ-4VRNd7_g842gvPa0WOmY0jV5KLDgG1QRvglcg7-p0RpvNkh2T5rTy-Kk8UL1My5UYotLedJgTZEM19TxlEdB1hL9S32SIV22LANWCk053PDO3ybkHtzO5luU1cFnSE1avQRmjUrSTFadZ2Xcy9xvNV_URL4W5XNdjgbesfTs14mf3JdCywPg27bR9O-8etCwYCw-n9bO12VXuGhB9Ss_GWRoqjX9y9rG3co0l5PWPpthy2d63IUyJZbhFHrVdhQ_4uhSGoe2z0NP2W6RlVHRhuz3_88PWqd_4QYm_S075WUCorswP1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ea14c8f5.mp4?token=Mxqw0bgCYhE8Z53de7useu9RwDml3YQsvZ-4VRNd7_g842gvPa0WOmY0jV5KLDgG1QRvglcg7-p0RpvNkh2T5rTy-Kk8UL1My5UYotLedJgTZEM19TxlEdB1hL9S32SIV22LANWCk053PDO3ybkHtzO5luU1cFnSE1avQRmjUrSTFadZ2Xcy9xvNV_URL4W5XNdjgbesfTs14mf3JdCywPg27bR9O-8etCwYCw-n9bO12VXuGhB9Ss_GWRoqjX9y9rG3co0l5PWPpthy2d63IUyJZbhFHrVdhQ_4uhSGoe2z0NP2W6RlVHRhuz3_88PWqd_4QYm_S075WUCorswP1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😐
افشاگری پشم‌ریزون اوجی وزیرنفت‌ دولت ابراهیم رئیسی: موساد به من زنگ زد گفت ۳+۵ چند می شود و سپس خط لوله هشتم انتقال گاز به شمال کشور را منفجر کرد!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101765" target="_blank">📅 13:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101764">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a128d814cf.mp4?token=XKreureC30lDTHbNFVdxgS446vWZTqebdlE1Tf10KrwHDT5u57hrNoh1ZRgtwybDwnFPv7UwmuIKQb9nht_TvTJF1rtDuMfnvj0IXsSP43hngqFBAq0LPGLAaM_u-DQV-aJxgJJVUKlIp26lBVYlcr4LwGHp5wQ1zddIV7EYbvStC6GbC-MsOtClijqC2D5DDgYrBhvrytn-MjfVWtJIPVGyMfjJ2lRAzKKYkb2odLlMdc_lHjT_ekMwxYou1YxLnDH9dqgrZrvfXFCojzot79-ERnnACo2v4upuYFnsSQldkc7Ge3nk2j-b6qGm_sIXfVz7b-qliGeL-NtJCYUeBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a128d814cf.mp4?token=XKreureC30lDTHbNFVdxgS446vWZTqebdlE1Tf10KrwHDT5u57hrNoh1ZRgtwybDwnFPv7UwmuIKQb9nht_TvTJF1rtDuMfnvj0IXsSP43hngqFBAq0LPGLAaM_u-DQV-aJxgJJVUKlIp26lBVYlcr4LwGHp5wQ1zddIV7EYbvStC6GbC-MsOtClijqC2D5DDgYrBhvrytn-MjfVWtJIPVGyMfjJ2lRAzKKYkb2odLlMdc_lHjT_ekMwxYou1YxLnDH9dqgrZrvfXFCojzot79-ERnnACo2v4upuYFnsSQldkc7Ge3nk2j-b6qGm_sIXfVz7b-qliGeL-NtJCYUeBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
پیرس مورگان، مجری معروف تلویزیونی انگلیس، بعد از باخت آرژانتین به اسپانیا تو فینال جام جهانی ۲۰۲۶، دوباره رفت سراغ انتقاد از لیونل مسی.
گفت: مسی فوراً دوید سمت داور، مثل یه بچه مدرسه‌ای که می‌خواد یکی رو لو بده، تا باعث اخراجش بشه. به نظرم این واقعاً چندش‌آور بود.
این‌همه از «سن‌لئو» حرف می‌زنن؛ همون کسی که می‌گن قراره بهترین بازیکن تاریخ فوتبال باشه. ولی توی فینال کاملاً محو شده بود؛ انقدر که اصلاً حس نکردم توی زمین حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101764" target="_blank">📅 13:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101763">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eC4AsgZ2GrX23F7SmMCj2gRPMMk1QsOxuVbF4ggfJ1NN6AwrMRT8iqRggM7QNVbDilwEfK15tjnCM0ujBrspC13ew_p0KUqX4u3ZosYcAWsQU5osJpuCPTVrCUcdivjdbPQbNbV3J7LYxgQLD7YIvn-6sAXQ8SpAPqMeh-iiHWZi0U8iSvQ2W8zEovxxKCoeMOSDVcC8RhJ-yOqvLC3mHDnQVPM1Zu-NaEVwOrTAeL3kwMAWrv43APPCn-qgo0jJF_DMYMvVNhG_de9AKjq1MVMakI3_4eT5FOB67x8CaB5OJgHW8RqPdf8jLFu9XXKacoUCWCwx8WKlZs26EE01vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101763" target="_blank">📅 13:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101762">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632f699042.mp4?token=lrxbyJQ5xYzfZHSgex6yab3KJyv1iacTGtgqRnF1QwvwQzF5J9Dxg4crT9yuGp9ljUKJD_u_oTW7bUFN15woCwjkeBpklJzphwEF0HHhiQTB_mRd_Br0-e5d12S7PBc5-xIlayEWrGY5fZVYJlJPTG5lkeAlxIjWe6pW6I6gmre8b7stznwOCPAZr-h6FRZkF7jpriSwyksDcnga8N-1gGgRvIOaUVzcHh0ZRyw8d4AdnHH5m8J6LfYzvs6EqbDDnLTD5XcLS6tpHwWBzrky6plbB-U1rt8bxnOct-yQPP5wZOe6JSamdcnmQJWWuFlQdpg9WVuvw7oQWqMml8y96Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632f699042.mp4?token=lrxbyJQ5xYzfZHSgex6yab3KJyv1iacTGtgqRnF1QwvwQzF5J9Dxg4crT9yuGp9ljUKJD_u_oTW7bUFN15woCwjkeBpklJzphwEF0HHhiQTB_mRd_Br0-e5d12S7PBc5-xIlayEWrGY5fZVYJlJPTG5lkeAlxIjWe6pW6I6gmre8b7stznwOCPAZr-h6FRZkF7jpriSwyksDcnga8N-1gGgRvIOaUVzcHh0ZRyw8d4AdnHH5m8J6LfYzvs6EqbDDnLTD5XcLS6tpHwWBzrky6plbB-U1rt8bxnOct-yQPP5wZOe6JSamdcnmQJWWuFlQdpg9WVuvw7oQWqMml8y96Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
خبرنگار: ارزیابیت از عملکرد مسی در جام‌جهانی؟⁣
🎙
لوئیس سوارر: با سنی که اون داره، میتونست بشینه توی خونه، اما با انگیزه تمام رفت تا دومین جام‌جهانی رو برای کشورش کسب کنه و تیم ملیش رو هم تا بالاترین سطح بالا آورد اما نشد. فکر نکنم کسی گله و انتقادی ازش داشته باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101762" target="_blank">📅 13:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101761">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=bFxBthm6eKQnUwU4PTkZl2oQveWrIsYwExylBsnthVz0kNaUDfI4F3ct9FTzX4WwKhtGLhBjTbLqG4dz1mTBszdnvdCJdC8Fr94VkUokb_5RqJlOMAooEiC5ahQAISxCB08PRbrQGmhb3YiHtwFPd1hv7UWvt5KtLam4X25dS_2H3j78ak7NU5UvC5RxN0rlJyO55QAgN5svmUdBNt8e95rlQek0I0_-020RoIDQYkoX5Fu-IrBRyS2Q1KY-2DvXbdzvQ-mtmFXEg45Bpmt_LSgRLI4eH2vuynaR6BdajHDBHVpFcZOhpN5suh3Y7drqgiZPMG03viLYU8NyhqEWlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=bFxBthm6eKQnUwU4PTkZl2oQveWrIsYwExylBsnthVz0kNaUDfI4F3ct9FTzX4WwKhtGLhBjTbLqG4dz1mTBszdnvdCJdC8Fr94VkUokb_5RqJlOMAooEiC5ahQAISxCB08PRbrQGmhb3YiHtwFPd1hv7UWvt5KtLam4X25dS_2H3j78ak7NU5UvC5RxN0rlJyO55QAgN5svmUdBNt8e95rlQek0I0_-020RoIDQYkoX5Fu-IrBRyS2Q1KY-2DvXbdzvQ-mtmFXEg45Bpmt_LSgRLI4eH2vuynaR6BdajHDBHVpFcZOhpN5suh3Y7drqgiZPMG03viLYU8NyhqEWlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇫🇷
هوگو لوریس درباره برنامه فرانسه برای مهار مسی: "یه دستور ویژه از طرف دشان به انگولو کانته داده شده بود. کانته همیشه باید سایه‌به‌سایه و تو شعاع حرکتیِ لئو مسی میموند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101761" target="_blank">📅 13:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101760">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=s9NUSf3w-MbYhp-EDj16wQDLSRSKt08nG4cFHrdKXxemtoEh0Xq8Sd4WTIkIALApzTGn0RIKg6xX35-nEaFiik4x07hBrWBsQEm5arXREAUpat2Uwf3venqV12-05WOUFQ6o7lt-otHMcv7HoRA87dxM1dPMjGKZxVbCuBrqOHr7xRMSJwpTRCj7SEKF8Tt2kRBGmTwXv7GnyRWaWPsjU3OIh4zc8ABn_AwxWfHQrDLIZqkyQA85tKOQH6Sxsj8fxfhfuhB_jnWRqVIv-3NPX_-RyyyDRvGyYFPRWR_T1TDF8Wh1g3adx3XHESHPAWoma4qur063PZR46c9hiEB7sIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=s9NUSf3w-MbYhp-EDj16wQDLSRSKt08nG4cFHrdKXxemtoEh0Xq8Sd4WTIkIALApzTGn0RIKg6xX35-nEaFiik4x07hBrWBsQEm5arXREAUpat2Uwf3venqV12-05WOUFQ6o7lt-otHMcv7HoRA87dxM1dPMjGKZxVbCuBrqOHr7xRMSJwpTRCj7SEKF8Tt2kRBGmTwXv7GnyRWaWPsjU3OIh4zc8ABn_AwxWfHQrDLIZqkyQA85tKOQH6Sxsj8fxfhfuhB_jnWRqVIv-3NPX_-RyyyDRvGyYFPRWR_T1TDF8Wh1g3adx3XHESHPAWoma4qur063PZR46c9hiEB7sIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
وضعیت استادیوم فینال جام‌جهانی که درحال کندن چمن و بازسازی برای مسابقات فوتبال آمریکایی هست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101760" target="_blank">📅 12:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101759">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQKU9lYqP-ipyWRnQs6KL9H1vgZdTi-1J5nsQ8W5JI6Ss1NC0n3OpKt-pbEdi2_VBtaafpppEaAVqJ1ulH2P6cwdMIcEkJeVk2xjLDZRzzHdYYEgJqBU9wCuZh70GcQOV66InXNGGmwViA8QB8Y9gLM6faGj9hfImKL5fRO79WhhCrCTZJVJUs27npPEF3HKYTMKcGo4hT9mHmLbmk1_bWYnTZJk-FJwUBDpQsD_fQvgc1n1rW8dYLKmlZ7ezWwK_CqfPh0dfyJ4DGY3mVjSSfgAU8zbQ1LwAv-ioc76XEubIKlvZNKaYNDJTxAlYMlTMp4ZhdBszGLf6HaF7C0RIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فدراسیون فوتبال آلمان از انتصاب یورگن کلوپ به عنوان سرمربی تیم ملی با قراردادی تا سال 2030 خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101759" target="_blank">📅 12:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101758">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IftOAMbyareRX2LpnuA-8Fih_IzfMuDbCwogb319hynRxJsx6dp-e-q5RrWs8LtWDuMZjTnCu9Fj189sKN4fnql-Esc96dx9AaUy22zguCnRsdoAsW-5K42t9CjY7Af2DCY5nYBa18NLX2LYiWgu_tE2wPDAwvaFWGwfutZtn3z5bxpkNzUFCO_hNiUm8eBFiMPJHaDr8ykOOPvC1sv4s3wCNBRj76ICL0K97nsvtIYZqDCITTy-LF6O1C-1pkE-dwAfcgDRpKdk2M_5E3kDUlmiw3AihG4IHsVxNxx0zn-wxwY6jo8RGNROZXvlTfc_aj1J3JVLhgS6kE7nb0BOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییییی از فابريزيو رومانو
🚨
🚨
🇮🇹
🔺
پپ گواردیولا پیشنهاد سرمربیگری تیم‌ملی ایتالیا رو رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101758" target="_blank">📅 12:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101757">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d513714e20.mp4?token=ZLMH1T3vZowHi_Lmzl1oHDqlwu4wIdFLt4ZhDLFR53lxmqiwsnIgcdShLjx2vEEh4K20CDxgflXrhSpKiC14KWMk6QzZm2raizM9SXk7KcvMO8Qp3dMDFU2f9nBTCT7LUxFTlOKxxiVRbQiE6l3zfLNOB8vOttDiX25qseBaFcLnKYbN7VFAdGmQHTNTjaWPT6rel4zawAofuy0kPO6PoNFLE4bpQyFjy8p8hbKmkUKQl8t6Vo__seB4a5FK1eEiiUYs0vw7IblgFuH9LLU-nG-HAMI6Lx5ACBDCATFNqYzEdaJSV-eLVRrPdN3M9JtQX9TFPHpzjH6PKHtFdmclrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d513714e20.mp4?token=ZLMH1T3vZowHi_Lmzl1oHDqlwu4wIdFLt4ZhDLFR53lxmqiwsnIgcdShLjx2vEEh4K20CDxgflXrhSpKiC14KWMk6QzZm2raizM9SXk7KcvMO8Qp3dMDFU2f9nBTCT7LUxFTlOKxxiVRbQiE6l3zfLNOB8vOttDiX25qseBaFcLnKYbN7VFAdGmQHTNTjaWPT6rel4zawAofuy0kPO6PoNFLE4bpQyFjy8p8hbKmkUKQl8t6Vo__seB4a5FK1eEiiUYs0vw7IblgFuH9LLU-nG-HAMI6Lx5ACBDCATFNqYzEdaJSV-eLVRrPdN3M9JtQX9TFPHpzjH6PKHtFdmclrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
⭐
فوری از فابریزیو رومانو:
⚽️
ماکسین لاکرو از کریستال پالاس به چلسی پیوست. 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101757" target="_blank">📅 12:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101756">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=bpxsDclMZshllyxz12WviUJ9VX9zFOcDdAJqn8kY2h7yQ9lF1kkgKPelSoz4Ar4la0DLDsKxH95wzXcNKaqojv5k_fpMX0LwIKaxnwugejh8Ssqj9M2L4T6tvzwMSzOizJsAiW9XKtxARjS8ofPLqm8sQJyxOwxka68GgLZhGmT9iaVyLUMesiVlEQ309HR5WCwGDnlHxnSieDaOY-ee9UaXjE9nmT9j2JyJJfdGc-WFVvwEJhyN7pjlgflFvsX-wMXa2c_HlU67hXMHOARGEzO8gXyRATt4jcE_pvW28OvOzM5m5Q51CbXg9_CUgjDdcTzR7e0BFiXLh0siX1ITZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=bpxsDclMZshllyxz12WviUJ9VX9zFOcDdAJqn8kY2h7yQ9lF1kkgKPelSoz4Ar4la0DLDsKxH95wzXcNKaqojv5k_fpMX0LwIKaxnwugejh8Ssqj9M2L4T6tvzwMSzOizJsAiW9XKtxARjS8ofPLqm8sQJyxOwxka68GgLZhGmT9iaVyLUMesiVlEQ309HR5WCwGDnlHxnSieDaOY-ee9UaXjE9nmT9j2JyJJfdGc-WFVvwEJhyN7pjlgflFvsX-wMXa2c_HlU67hXMHOARGEzO8gXyRATt4jcE_pvW28OvOzM5m5Q51CbXg9_CUgjDdcTzR7e0BFiXLh0siX1ITZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
🤯
«لی میژن»، دونده ۲۵ ساله چینی، در حالی که تنها ۸ کیلومتر تا خط پایان ماراتن دریاچه هنگ‌شویی فاصله داشت، دچار قاعدگی شد. با وجود خونریزی و شرایط دشوار، از مسابقه انصراف نداد و با اراده‌ای مثال‌زدنی به دویدن ادامه داد. او سرانجام مسابقه را در زمان ۲ ساعت و ۳۵ دقیقه به پایان رساند و موفق شد حدنصاب لازم برای حضور در رقابت‌های قهرمانی را کسب کند؛ عملکردی که تحسین گسترده کاربران فضای مجازی را به دنبال داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101756" target="_blank">📅 12:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101754">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrxLbX-H7f686LyPGvDUP4ehDEgSHwgsz5d_IVIOYW1i4axA9Kvbv0ahUCsnR8c8t_-yjSAq8iBegkPL7osLjIuLeiGwKNQatEtXzJtdmh2vCFzQoO4lCsDotzvjYrbSQ80M-j_8Yq79IZHDhS0fl-pvRMJ9QBibCZie6HdaS7ft2_BgvmmAzDeVti1Gdpys6s7DVM5Dht3BRgPl3UJAnMzvq1k2AMZHemuExb25xLSNqnKn1y3TVYMG-CtfNic_44avWRjuu5_rnja93JkpU6eZ2wR2xP6rwo4hO_f5ghvSpTYcUsPxlxBWQ6idRE0Vruz-kNN7EN9efknutIdP7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بن جیکوبز:
🔺
چلسی به احتمال زیاد قرارداد با ماکسین لاکرو مدافع تیم کریستال پالاس را با مبلغی در حدود 52 میلیون دلار نهایی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101754" target="_blank">📅 12:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101753">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=QDz-apJ8qgQ-p3NdTtyQcab5HI2B-OiB0IBUyckfJT09tqsfO0AbQ6RTIvshxbzpTXaSap8xNFiRAy06rGAxc71iptSuRZOCwdqPsONt4ljWECP2aTdN0e6sfvUJtP2l7-c9Y3YS34XYeDGpuipyIS3KA1-X7LAgzGGL_HEExaU8xtCMepjVfer3S8TzDGIbXByBFhPLM6vXFBI17fA54OPzNv6mNtvy5qstxpZKdmmB66fh2jTTahOQitp86adl5VyShcsJlM6n-bhAA2GZHBa62CYmrgcfsfLgB2leHEs2xJ72MCEaueNQaW1Qw44bJkt5NOpGCTQychTI4gqRJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=QDz-apJ8qgQ-p3NdTtyQcab5HI2B-OiB0IBUyckfJT09tqsfO0AbQ6RTIvshxbzpTXaSap8xNFiRAy06rGAxc71iptSuRZOCwdqPsONt4ljWECP2aTdN0e6sfvUJtP2l7-c9Y3YS34XYeDGpuipyIS3KA1-X7LAgzGGL_HEExaU8xtCMepjVfer3S8TzDGIbXByBFhPLM6vXFBI17fA54OPzNv6mNtvy5qstxpZKdmmB66fh2jTTahOQitp86adl5VyShcsJlM6n-bhAA2GZHBa62CYmrgcfsfLgB2leHEs2xJ72MCEaueNQaW1Qw44bJkt5NOpGCTQychTI4gqRJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
انتقاد شدید عباس عراقچی از صداوسیما: صداوسیما مصاحبه‌های بین‌المللی من و استقبال مردم عراق را پخش نمی‌کند، اما شعار «مرگ بر سازشگر» و روایت‌های منفی را برجسته می‌کند؛ گاهی با خود می‌گویم شاید اسرائیلی‌ها در این روند نفوذ کرده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101753" target="_blank">📅 12:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101752">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGJMsznCL54cPwDtrvn7bIUXNeEwVeA19AlnHcpOc_TXiBEaa0CbjhQamg8qywOdL9kuaPl002oEf_tTK6NpT_tAFbRP5L-pCgXNz9OfFWBDzpCsDVzWZXH9yBI7H2G9J6cdX1bwn72X_atO8o9_9uUiUJsZwjPPifXORmfeDnqr3gnE6ICvEP9kzil_D_KeROi0Bo39uMFmZFKvRhAllT8GUcqFZr3twUhQeuD6erkD-W-j_i6UG6PxhZWiHWrYtjffm6Xp0dQ_-O2o6GWTw609UN8hWd0V0K7f8lkGYSv1ZUvPuE77vAiC7jbs3UJ4i3_ximc4xmdH_k36DCpoPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
اینترمیلان تماس اولیه با نمایندگان کریستین رومرو برقرار کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101752" target="_blank">📅 12:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101749">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjulrHYsZlXYhj6WSfnceD-Mg_JamFmTSitI0zDqe9rdio0arXh97GpM8X-bmMLQGXgdFKRFdL1l01pi6To-KEH8CmWUaNhZrhG0VF28IlNv5H2wlsxcECZ-8cRZ5YGnx-zZF3yeDUdKxhCDKSz8PLTxPA8QVaFhYWh1nQMdu4cyKCB4EAosCCpBSOA6Kdu8Wzpm2KfOcjbyd-U5n3NPPd6cxtLJ_wWxwxjF3oRwN9V8Xq4W0Eo68w-cNTMOWlm98mMIJA8VJQhDka6g7j3Ap5J61PWtqQUTcTF-bwnF5TUsULZVUEB386VEB-DxSmyxgBcmtcaiBiQ3mfr8DFsIOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DkecjFBRQUFcCygpkhmJA7jFIkRIjEt16W2WCaMu_wvwvDUQD8jGx75-jUYGEvzRDExv-bQaUHTi-ZK3P4rCYSdw4sLGxx5F_WiaD8hwkTafCtEGyJkdnWsHotB6_sVHpgUS4RjFCpWu_wrTB0QOV3y2TwRgfU2uhTQ4oSdkX50-hEUOiMfgrD_PBTtRTgykz2qWNqjFlgF4Sg5K-K1D2lD_P5Vln_h32VncswlkCXeW-Zit1g22mAvWiOHJqpIRxKayh5ScxGs93J_M9fDV_ZnLktyjq6TGD909ViXWEsQ_fgC0_U3ZTNp1hZH07klPTXGJnJdGUcIwmrSs7HscAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVUuGSKFZrw4KHgyI1RN7gmb873eXLfcSsm7nNh-KwJxdJRQLWO5FBm9pE_moudPquAhNDP8yZvGLg5KAXwa0UoEQMz3bRfhTpPEA22Q6cemuvP93lVR73kDw_tDG1nJ_hdFa_2hca_Xt1F-fsEXymuieKThkCpcheCcIhRp9MCBD77O_eq58exxj4mSvS7kD8Tn6_s85xtUq9uoIbLkVaFkKEiZIahpfgaGM6SibUZIqvdfl-KLZ5__xiH_lTvwjza9HL3YUmx-EWG6QdQ1g1Wj3isc64-1CiUUwJbi5AAfx876pFn1Ij1mB5uTyvy1Qyng7roABwQxJRkH2wxIIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚫️
کیت‌دوم فصل‌آینده باشگاه نیوکاسل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101749" target="_blank">📅 12:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101748">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sC6tK5FIh9qNNHX8x0iLUHsSUaSvDWQQnqRGn_egFQGuSsHl0MDyzltpZx51w_rvMFow94dxP3cetxwiljaj7pojkQgKPVZDB_BPUFddcOtnJAqCIJQsGhrgHinsjBMIc6ya7LYWG3aI9ke1NgEn3htUx7OKc7489AJvVrZoJLMXw4tmNGJtH6xCh0Xv40iw-_5xhwEcszM4OppiIbxsroqsjGT3Hx-Gih3ZkVD_JsYcYqlB_xQvRcONlBJK-lzH8UZOqi4gf_IwGVfa3sP7_thI3y41tKluSpxMLsY6q4MmdOnUBrDlhl-3XrpYK76c0o-cFrMfVsw1W9hZztDM8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
لاگاتزتا: فنرباغچه ترکیه با ارائه پیشنهادی به ارزش ۴۰ میلیون یورو بدنبال جذب رافائل‌لیائو ستاره میلان است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101748" target="_blank">📅 11:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101744">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HcNty4irAOlppKHojyjCzz9UaxgcMexAUI4BFFvxGejCKmHsHo4FARUKI3SJah6zyspsr8EGPbfceQGktYtrC6c86yxX47-9jAMMXKjERo93hVP0xK_78du4VoW14VH0k9ozo0R65j-sHTb6DwAb0oWsnQ10ahR6bwRXQr8Gba1DayYdYMdb_e9c11OUhuLeDND7tcGcBphfrI_ZDIkVAO3voQ5VGFOVwAsxJb79PHNwPR9ERCiTi1EMkuxi7wNRjO2b6HVRhjivuBcv0oKUtBjPydc4yatpyRhYGKX903HbuOprsCXhzCKJqkCiFaC7HurXnuMCySHpxvyJel-lNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQZW2QmKIqwalbPYSClqsyQT_hAoTvpElm2mx1Dqg25oSLdcSFcQoxlbl7R4VMe3OfJaiJyJohrSZhTXrex9lK4Fe9cINSnvth6ER0vXVYXLNvV-pk-dd7RikS3CrigdcGoNv-xQg8LNdUYOQiOHjmMkRRT2NcMYND8FYYbwo58nGratbVpe022Ff2TdK7bSgbuueimShdntW9ym-ltvLj2bz9s86acpSlxxy2F-zp6nXkXNGqtq9K7c0g3n0PceBogCjR3cTKtqTw2OJKnWcvGxegdlf26jlckjkt1Us-RL79IQfutg6AL1s7KKpzi7q30JCaL2L4NqSXy1Y5bPIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-HMydHoJOVNY6B0FRolT6oNyjTvSdUn_gD7Rc6YZyikolNOSIIx1ijzNEjiF6xzNdyLeN-tXiATC-4-CgCjfte8MXJf_Hs-0WP5xCI4Z_pF37tQ-LHWPqVxjUBklbyLZqxzedToLqgPdhp6PgY8ulhYMD5PAF2XkVPsn7poIxkLQRngT4Zz7rLE4tpM2swP0Gq0Kx2gekL19b068BmBU2TQsSEgZarU-87KQA-x9tz5Kmd_8111Fp3t2fTgd-q0IHpSdb1KygUyACuMLJXP1ju2-zzhkMJbHFGq5R9VvHMlvyhx8hfF1EYiJPNiCefH59bt9UxTh3xXIiwH-nwIGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم فصل‌آینده باشگاه آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101744" target="_blank">📅 11:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101743">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=rvac2xz7_G8ukxZAE4oYvkrUzCKY6-SAtRBmw0sTVVwVsfKiPXvt5mEkKIDWXKcJFio7FUjhh2WJXCDovPgBcSWkhq9jYno-8GpS1qtZRght75p4AsIbQPTTtbqgg4-juSbSiJ6ubIEL0EePg9aGY7-x5U9cnTX9HENa2ySXpQEQUD_rEh0pZ2tpxZ56wvvWehYoJq4y7QZAbbn1B9E3tw9MC2mCzGJWGL3gJko2c375kS9KBA3tgW8P7ld1I8VxIasWjYj8YY9Uri4wYMd2Gxfj11InRdeDYTdcvejMIugldwywY88NCr5uF_WvP86pA9tyTegcq_kOFaNCMEv8XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=rvac2xz7_G8ukxZAE4oYvkrUzCKY6-SAtRBmw0sTVVwVsfKiPXvt5mEkKIDWXKcJFio7FUjhh2WJXCDovPgBcSWkhq9jYno-8GpS1qtZRght75p4AsIbQPTTtbqgg4-juSbSiJ6ubIEL0EePg9aGY7-x5U9cnTX9HENa2ySXpQEQUD_rEh0pZ2tpxZ56wvvWehYoJq4y7QZAbbn1B9E3tw9MC2mCzGJWGL3gJko2c375kS9KBA3tgW8P7ld1I8VxIasWjYj8YY9Uri4wYMd2Gxfj11InRdeDYTdcvejMIugldwywY88NCr5uF_WvP86pA9tyTegcq_kOFaNCMEv8XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
کاپیتانِ اسپانیا در رویای پیوستن به رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101743" target="_blank">📅 11:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101742">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=iPbDNO07mKJCzUbc3NSXoC-WIK24SIAhEx1vTtVpW5X-xlZzDayZAqKNkd_UnNKw9IaZU3jRflJBU_ruHMoctRSVGcLJOrWjJQkxlfcOsm6G0bJ_h4gCXZpPU_ahijfNE1HLNB7hyyIQQmWuG6-Sw5vuppw_TgM-Mr2aCqHXquOwigmnxP4S5bEcWMwyTiHe27oXF-Qs9u_RMGPhxCVlqD_eC-cc4Ksw0_HCqmtlE6SB7BPYrmSo4BXkS0gVmITLG8AJwDF0zdmpvxptotJb0XovUqP7rFwGNONF8pbDDjtcVolRYbADw-EoacBBcikFry-DHJLuROqg_gyJ1h8H4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=iPbDNO07mKJCzUbc3NSXoC-WIK24SIAhEx1vTtVpW5X-xlZzDayZAqKNkd_UnNKw9IaZU3jRflJBU_ruHMoctRSVGcLJOrWjJQkxlfcOsm6G0bJ_h4gCXZpPU_ahijfNE1HLNB7hyyIQQmWuG6-Sw5vuppw_TgM-Mr2aCqHXquOwigmnxP4S5bEcWMwyTiHe27oXF-Qs9u_RMGPhxCVlqD_eC-cc4Ksw0_HCqmtlE6SB7BPYrmSo4BXkS0gVmITLG8AJwDF0zdmpvxptotJb0XovUqP7rFwGNONF8pbDDjtcVolRYbADw-EoacBBcikFry-DHJLuROqg_gyJ1h8H4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⭐️
🇪🇸
زوج طلایی اینیستا و لیونل‌مسی که از بهترین ترکیب‌های تاریخ فوتبال یاد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101742" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
