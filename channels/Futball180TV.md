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
<img src="https://cdn5.telesco.pe/file/YfNe7Y_zVizrPqEDXkZycNBgkE3LiO7l9EPxIE7aNqpm5CEWUpNr1D3FYcjwPKQxk472br2xLXqrvaz__Bc7SoqqXiL9SyzImP3Z9jfTLaS0cNe1YGrUbV43S61dk_uxn-gN9ZyHZRDh51xh5mT8R65AxhBu3fel77cEJoVnsOaB0gdUXCklNvsqvwUMQjVRQi_7BxFXwbooOe3shfIOQ6wi2gx7Mza0nt_pcL3OMStLM6Aysvdjll_kUh9eTL_COQmad7Gsuc_oSBoREM6fxfRVcLbzGRIG995Jc3woi07kvvHV1dWIPsboNNWKAso7zWF1vT9j8bH0X0a3O_dyqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 454K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 17:37:05</div>
<hr>

<div class="tg-post" id="msg-104235">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
آخرین وضعیت استادیوم آزادی: آذرماه جدیدترین تاریخ اعلامی برای بازگشایی این استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/Futball180TV/104235" target="_blank">📅 17:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104234">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1b80d7014.mp4?token=hkLhgd7xI07RklFT_0B8et8OT6oFTE2qFTV9I_Su_JwZO4LPD13u8XhrYbyZ9DhNgtzuzSZY5z42RX_Vc2372LZ6KekSfaW7T7RK0P1qJtds3QwVTaWKSLPaUJUCji_GE4eUMgRGta9sfCZquL1faEQDsqubAcjFsaFfW2W-dz_SrGY_nYV8_aIFNvhsg1dHmS61eWhxWVXy0QOdEdWeo5oRAQRsavMj35ZGcCgzEz3NLK_cZgt2veKSCVN59dsoEdrlpUuoU1gvVmEZfKXK14eCD-MeG_piEeRwF5U_CWuarQddzsXOQCrQsFEe-n7INzbVu3bWG19ZCJzI1z5hWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1b80d7014.mp4?token=hkLhgd7xI07RklFT_0B8et8OT6oFTE2qFTV9I_Su_JwZO4LPD13u8XhrYbyZ9DhNgtzuzSZY5z42RX_Vc2372LZ6KekSfaW7T7RK0P1qJtds3QwVTaWKSLPaUJUCji_GE4eUMgRGta9sfCZquL1faEQDsqubAcjFsaFfW2W-dz_SrGY_nYV8_aIFNvhsg1dHmS61eWhxWVXy0QOdEdWeo5oRAQRsavMj35ZGcCgzEz3NLK_cZgt2veKSCVN59dsoEdrlpUuoU1gvVmEZfKXK14eCD-MeG_piEeRwF5U_CWuarQddzsXOQCrQsFEe-n7INzbVu3bWG19ZCJzI1z5hWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
مراسم خواستگاری دیشب کف نیوکمپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/Futball180TV/104234" target="_blank">📅 16:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104233">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f3ef3446.mp4?token=uaCUIqBrYdanEdDFDK9ptx1CVYlqgzZP_8BzC04H9WbJMqi2-g6RSoCcK36oX6Kpaosk9JNeWFtnucv9rtSzZi4bj8lHYi0fnAICgWiClxNc-JQkNaPsNcahylFwBHbNFa5BpjKk-FUgjgGjh0TxOlJYJC1nx7Ndaf_5h9xZeUYGvenbetH-JhaWJ2WMgGvSoI4VDP5fyjNRouyc7d_Pg-FhGRwZU7fkasOO9eXKJnhLDLWhbMu1Mjhz05a_E3Hj8IOa0MfMBEsi0eqHoMeWj1AhgZnMXNh1D0bGmJpkI3spcY55l9XlYxxGabK0csm45otcl8-aAZEqVPEwM5wuuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f3ef3446.mp4?token=uaCUIqBrYdanEdDFDK9ptx1CVYlqgzZP_8BzC04H9WbJMqi2-g6RSoCcK36oX6Kpaosk9JNeWFtnucv9rtSzZi4bj8lHYi0fnAICgWiClxNc-JQkNaPsNcahylFwBHbNFa5BpjKk-FUgjgGjh0TxOlJYJC1nx7Ndaf_5h9xZeUYGvenbetH-JhaWJ2WMgGvSoI4VDP5fyjNRouyc7d_Pg-FhGRwZU7fkasOO9eXKJnhLDLWhbMu1Mjhz05a_E3Hj8IOa0MfMBEsi0eqHoMeWj1AhgZnMXNh1D0bGmJpkI3spcY55l9XlYxxGabK0csm45otcl8-aAZEqVPEwM5wuuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
نحوه استقبال از تیجانی‌ریندرز توسط القادسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/Futball180TV/104233" target="_blank">📅 16:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104232">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e04b7c878.mp4?token=CdEaP2Rtf1l_QBtPdF7GKJ-AeGjw_k8sqB7UOVK8UIES_mR4clmCqQzyZzLgPy7QFCnLyVbnVnj5xCHckm3_lw_saUAoVeWxxRq1f9c2RlmRdDKMR1QPTbYHy4eYukRz7IKMjar3CJKBD5IHtHc38fkUiZl73-vCcff2Ca4MC5oWNJswGngPScRLdrIIw8gXZuVeI75iCTviz1G5YGIt3HuYSQg5yaav37HUMW_RP2aXe6nD-McRv07LcvAkUM006e3wxwaFUQCapHmgOekDOSpxaXHKfKSdqcF2w3YGuVtjKBtI1GrBv4eirwFS86ITK9na2UtnpZyClaLee4kfzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e04b7c878.mp4?token=CdEaP2Rtf1l_QBtPdF7GKJ-AeGjw_k8sqB7UOVK8UIES_mR4clmCqQzyZzLgPy7QFCnLyVbnVnj5xCHckm3_lw_saUAoVeWxxRq1f9c2RlmRdDKMR1QPTbYHy4eYukRz7IKMjar3CJKBD5IHtHc38fkUiZl73-vCcff2Ca4MC5oWNJswGngPScRLdrIIw8gXZuVeI75iCTviz1G5YGIt3HuYSQg5yaav37HUMW_RP2aXe6nD-McRv07LcvAkUM006e3wxwaFUQCapHmgOekDOSpxaXHKfKSdqcF2w3YGuVtjKBtI1GrBv4eirwFS86ITK9na2UtnpZyClaLee4kfzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
خاطره بامزه امیرحسین اصلانیان از اسطوره فوتبال ایران احمدرضا عابدزاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/Futball180TV/104232" target="_blank">📅 16:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104231">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea3bf7fa1.mp4?token=HDIsqZyS02cVjV-fvXmL2qzmDkM_WLmlKuhmfDlB2jVipd1qLapv6BkMDvGEpAqYcYkg8-1f-8MwIJguHN_JFBQmQjlWShdnF0foc_mJ1XXOa9NKr_Bq3HyxRYxNr7eUUMkwwm86np3xBeO4kMsIIBFWj_Q7bd_AWz-ihE7m3NdwIO8DHJ9Tm9CxsFCoJuDep7-mE0CGV6ReYo0LW31PRtZ7aAelEfgL8zqv0tOensICmLDimxBVnCc6ILR_qdTUvBvnNW9FrdGMgUWw99EnQ98kZ4Ecuq8jRaK9TotdBoVI29zcbs07Lm8bQAS6sX4ghpsVAJmzfbYFqIwVz0DGIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea3bf7fa1.mp4?token=HDIsqZyS02cVjV-fvXmL2qzmDkM_WLmlKuhmfDlB2jVipd1qLapv6BkMDvGEpAqYcYkg8-1f-8MwIJguHN_JFBQmQjlWShdnF0foc_mJ1XXOa9NKr_Bq3HyxRYxNr7eUUMkwwm86np3xBeO4kMsIIBFWj_Q7bd_AWz-ihE7m3NdwIO8DHJ9Tm9CxsFCoJuDep7-mE0CGV6ReYo0LW31PRtZ7aAelEfgL8zqv0tOensICmLDimxBVnCc6ILR_qdTUvBvnNW9FrdGMgUWw99EnQ98kZ4Ecuq8jRaK9TotdBoVI29zcbs07Lm8bQAS6sX4ghpsVAJmzfbYFqIwVz0DGIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
وقتی میخوای بیانیه یک باشگاه را یک نفس در ۳۰ ثانیه بخونی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/Futball180TV/104231" target="_blank">📅 15:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104230">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af4cdf7dc.mp4?token=EPvQFRwCmp4DIUKBwcND60h6XTxAVlrdfkr2GRc0kVeyN15hR3k-BdHsbFcIFiqlZmYNGiPv3BFdsH8l7NQXfC3QMWCF7ARarVrPAux0GD4SP34GzLht5Ep2KvUZayBXHt365WxUoSQTZHz3PaGW5aGLSaFx0C4T7Kil6uEUlfWWgmFU8usFWT1pR4MrDAmddvd9se4amoQuXSrCFrX-6ox8U0B1Pmih_R7_KDj3yplvq1_vT7UBCs1C5oSP7U3jYqZJXAHM6zYxSABw5QXHF-Sco-hrnIxl1NdXxHHpN4K6RiiK4E8rmwd-uMUc76VJzprlwJIsBzIfaFolVX56aA8wX5hbonpjFwmbSsUUJMFDj3oNojs9e03cQCBdm3q0NKV5TsbH-bsrbCxclJaNemXQPCdFN4MglDtDlrjIb6XlhRZjrpg6oaT5ugxaxAk8xNAFmbkguBQfw3zWL2_lPI7dXG2J58lNqCMEsFHulBamGS-jH6NWgdojz2Sp-GcS1EygPpYhVj7CH0wACMnY2MvEBVh4yCZZLSQ9feFQmMNZR6tL-zhIJqShZUJPkuiN6_nkoFVwkvvnDWsUjC1eFnYqLbd6FLD3K1HjnuNq0yiRG-U4rQp6cNqY-nAgoDXxzlA6DsTT-LDkidb6oxeMPSFVeNh2LvZ36xtzbfrxTZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af4cdf7dc.mp4?token=EPvQFRwCmp4DIUKBwcND60h6XTxAVlrdfkr2GRc0kVeyN15hR3k-BdHsbFcIFiqlZmYNGiPv3BFdsH8l7NQXfC3QMWCF7ARarVrPAux0GD4SP34GzLht5Ep2KvUZayBXHt365WxUoSQTZHz3PaGW5aGLSaFx0C4T7Kil6uEUlfWWgmFU8usFWT1pR4MrDAmddvd9se4amoQuXSrCFrX-6ox8U0B1Pmih_R7_KDj3yplvq1_vT7UBCs1C5oSP7U3jYqZJXAHM6zYxSABw5QXHF-Sco-hrnIxl1NdXxHHpN4K6RiiK4E8rmwd-uMUc76VJzprlwJIsBzIfaFolVX56aA8wX5hbonpjFwmbSsUUJMFDj3oNojs9e03cQCBdm3q0NKV5TsbH-bsrbCxclJaNemXQPCdFN4MglDtDlrjIb6XlhRZjrpg6oaT5ugxaxAk8xNAFmbkguBQfw3zWL2_lPI7dXG2J58lNqCMEsFHulBamGS-jH6NWgdojz2Sp-GcS1EygPpYhVj7CH0wACMnY2MvEBVh4yCZZLSQ9feFQmMNZR6tL-zhIJqShZUJPkuiN6_nkoFVwkvvnDWsUjC1eFnYqLbd6FLD3K1HjnuNq0yiRG-U4rQp6cNqY-nAgoDXxzlA6DsTT-LDkidb6oxeMPSFVeNh2LvZ36xtzbfrxTZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
کیفیت دو چیز در استادیوم‌های فوتبال ایران تغییر نمی‌کنه؛ اول چمن‌های بازی، دوم ساندویچ‌هاش!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/Futball180TV/104230" target="_blank">📅 15:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104229">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af1fb314e.mp4?token=P0QGGSNGUbBSxcxRnOqxjiEG0yoWj8oa3atRjLp2gN6ICInqehlmC4wGwpCwrjGbgvMCc3ognDjJ4NGlQbsJk3kdyPLBczs8jwkL6xTxxkqOFNwvz4lwWNWRvUk56u5HWBbjRuPBry2uUJ0MuoNkMZYevYFOKayFxgaJNPH2J0_XigYwMSe210AbyBmT2uJ24oHSgywF6k_m4oA0li22PAdvntNJpkMKyRJgVsonxzrlzUnU2YIiuxi-Zk1shRrZQSEVGdfM4kfvBQPX2PitDg515oT70iST7pc82QyDls7LynEePbrzHefrlblvKFzGAldAlyCHSU43EyKltHpNEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af1fb314e.mp4?token=P0QGGSNGUbBSxcxRnOqxjiEG0yoWj8oa3atRjLp2gN6ICInqehlmC4wGwpCwrjGbgvMCc3ognDjJ4NGlQbsJk3kdyPLBczs8jwkL6xTxxkqOFNwvz4lwWNWRvUk56u5HWBbjRuPBry2uUJ0MuoNkMZYevYFOKayFxgaJNPH2J0_XigYwMSe210AbyBmT2uJ24oHSgywF6k_m4oA0li22PAdvntNJpkMKyRJgVsonxzrlzUnU2YIiuxi-Zk1shRrZQSEVGdfM4kfvBQPX2PitDg515oT70iST7pc82QyDls7LynEePbrzHefrlblvKFzGAldAlyCHSU43EyKltHpNEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇪🇸
🇪🇸
وضعیت خط میانی بارسلونا و رئال مادرید در ال کلاسیکوهای این فصل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/104229" target="_blank">📅 14:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104228">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8411590ba1.mp4?token=rDLHHdzKMUc-_enRzkgzE2Mq-vkbeHtCjcO7DZ72lh6sry7mW_u8XtsOhydp_pH-mjC5qOwKkTJ_dTGepee6vWIw3TWdQv2n-VBiJl5bJqbrdBizrj7Lqqbvwsi7eFLgQHvbiSpZq9iBI96ZEvDxR0yRvWgzJ1TPngyKlB71BMAc-TkUmGZuDIBIggX03CIuyyQI5tnnpHYShs8kdJzvwMdY9PB4t-4tPNoZVzsqbb_E_K7Rr-u_Nae6f1Wc-fK6gqyM4j8KzP4Zr-biEeMIP7ObkNhk1NzwQWZqZOh1Ic2_E10YTL_5SF1U1u2JSp-Q7F4StDVVqpb2iE58jFObag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8411590ba1.mp4?token=rDLHHdzKMUc-_enRzkgzE2Mq-vkbeHtCjcO7DZ72lh6sry7mW_u8XtsOhydp_pH-mjC5qOwKkTJ_dTGepee6vWIw3TWdQv2n-VBiJl5bJqbrdBizrj7Lqqbvwsi7eFLgQHvbiSpZq9iBI96ZEvDxR0yRvWgzJ1TPngyKlB71BMAc-TkUmGZuDIBIggX03CIuyyQI5tnnpHYShs8kdJzvwMdY9PB4t-4tPNoZVzsqbb_E_K7Rr-u_Nae6f1Wc-fK6gqyM4j8KzP4Zr-biEeMIP7ObkNhk1NzwQWZqZOh1Ic2_E10YTL_5SF1U1u2JSp-Q7F4StDVVqpb2iE58jFObag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
هواداران فجرسپاسی در بازی دیشب
💛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/104228" target="_blank">📅 14:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104227">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15540c4079.mp4?token=VlsxX-ffRIhPRqsxtkj_TDVIC-CKkpmpebpS2PDCRNqUSH7IBkCkGCr_UQ3CnlbVhOsBtF-CAkzg0aFRuvzgi5C8nGaawZ2aGSbjYBVmmC8tCasEZ_gXUerot4jnhwjgUesOM3I-Y1d9_SPcGelPWwtsy7akMAiCBF2b6RY2vLHceBgzMEA48B0K506r17T-E40BL1FU4GS_aY8g1r-2RhttVzqp5ybrcWjEJ3HYbaj7KoNymbPWSd-hqciqTUCBXkzF_4gA2JSRqpG1KL_ewjVKJuB4446rcsH9zbv2aNHfgpZMWr92eQu-2GO-LC8ceLETUyr2FJir98bkfiTUsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15540c4079.mp4?token=VlsxX-ffRIhPRqsxtkj_TDVIC-CKkpmpebpS2PDCRNqUSH7IBkCkGCr_UQ3CnlbVhOsBtF-CAkzg0aFRuvzgi5C8nGaawZ2aGSbjYBVmmC8tCasEZ_gXUerot4jnhwjgUesOM3I-Y1d9_SPcGelPWwtsy7akMAiCBF2b6RY2vLHceBgzMEA48B0K506r17T-E40BL1FU4GS_aY8g1r-2RhttVzqp5ybrcWjEJ3HYbaj7KoNymbPWSd-hqciqTUCBXkzF_4gA2JSRqpG1KL_ewjVKJuB4446rcsH9zbv2aNHfgpZMWr92eQu-2GO-LC8ceLETUyr2FJir98bkfiTUsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
متفاوت‌ترین جشن ممکن؛ یک کیسه پول پاداش برای بازیکنان؛ جشن متفاوت در رختکن دینامو تیرانا؛ رئیس باشگاه پس از صعود به پلی‌آف لیگ کنفرانس اروپا، با یک کیسه پر از پول وارد رختکن شد و میان بازیکنان توزیع کرد.
آردین بارزی با این حرکت غیرمنتظره، پاداش صعود تیمش را به بازیکنان پرداخت کرد و جشن رختکن را به صحنه‌ای متفاوت تبدیل کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/104227" target="_blank">📅 14:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104226">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqfCMx4yCNuAwNj8YLguAGJfAcXdeIWuNZnoBrQcC-ZtNN2n7joXWuYrcrW_HDV72ulxaaf11csCIiZ1rRlRwz_Brt2ml8oGJAL-0IgJoalJZLbsemuOv6IADamuxSXZ5JOxdCL7XlaPjjHWHeT7aCEoZy6AQlRA4jSP3WjzOIyMA2AXg46N68U-rxckDnzHiuV4wcK-2ei1coP7bOUX4mfkAviamryP-x7i1wIRt5OLtKDNMcSBJ2CFYIiYT4QdtmgUVo615w-T1vvCtF0ZZNPr5qQ6xoJIy0ay2gohhLIwpXvZw09ejcI8u0HeX6IkbeZVjg5Fj3vyw_6N1Uy4lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه‌فلیکس‌دیاز: بارسلونا از جذب آلوارز ناامید نشده و دنبال راهی هست تا در ۱۱ روز پایانی نقل‌وانتقالات بتونه این‌انتقال رو انجام بده
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/104226" target="_blank">📅 13:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104225">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab172d319.mp4?token=qg_28GfkA0ZVIwqEJH-_9zyDZ4eJWLppBZBdwaeZFgNPGIZD1p82fZ6lIjBI7mpF7VZWd2RF-LgWYmlvQdVkOlADdPIllZNWX-T2dcqhcbtuhKI69eWqtCgEya9Yq66hLEafScdtrIOBQ4FakOI5P7HvMNgyMkOzgTmkwm_0RDdWV48d4e6CvAG8LolPEhw__m8OvZOhD_Yglit_gau5fg0mmTYHdS_CmH6ZfL6aZT61993SCanG9CCHdks7sizhJfiAeFoBd2btxpXLfpvRzFlGJq5I99z4R51ODiaAHFZi9_eEqIZEaiy49JasCPZT_oXGO4dHUcAiR78zz0Qs7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab172d319.mp4?token=qg_28GfkA0ZVIwqEJH-_9zyDZ4eJWLppBZBdwaeZFgNPGIZD1p82fZ6lIjBI7mpF7VZWd2RF-LgWYmlvQdVkOlADdPIllZNWX-T2dcqhcbtuhKI69eWqtCgEya9Yq66hLEafScdtrIOBQ4FakOI5P7HvMNgyMkOzgTmkwm_0RDdWV48d4e6CvAG8LolPEhw__m8OvZOhD_Yglit_gau5fg0mmTYHdS_CmH6ZfL6aZT61993SCanG9CCHdks7sizhJfiAeFoBd2btxpXLfpvRzFlGJq5I99z4R51ODiaAHFZi9_eEqIZEaiy49JasCPZT_oXGO4dHUcAiR78zz0Qs7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
خروج صداوسیما از ماتریکس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/104225" target="_blank">📅 13:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104224">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">▶️
🇪🇸
هایلایت بازی شب گذشته بارسلونا 2-1 الاهلی مصر با گزارش هوتن خداپرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/104224" target="_blank">📅 13:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104223">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ccac38661.mp4?token=uNmo0NNwWQW4ib_V5bEQ_Rxgc9V7HVUKrgCoOK9u-1DFRHYx56DkkJlOMDvOq59Ydn2VtWiXRni4g-7QEIhUoe9pCNr8litw_zI0EoGde3miDssXEAaBixgnipRbyTcLVfCaeHn5eyVzCNF65vRks1Xn8IZBKsOUANREi5ofL2Sqo651ixOxzcjo1AkxQZQ2MIFQ8OANgLKcBWM9joBJdEIF_8xFv--GpwnMb2tbowRekZyUzG5XPVJVLl1XoHdfhMBLq9VjRrlAdAhgHSvOyci4GG1gTv7pXhcthKPx42f1NaOUvZvUpYvJQzVUe-ydtYNHGsIHLc6nqdAmQ1ozLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ccac38661.mp4?token=uNmo0NNwWQW4ib_V5bEQ_Rxgc9V7HVUKrgCoOK9u-1DFRHYx56DkkJlOMDvOq59Ydn2VtWiXRni4g-7QEIhUoe9pCNr8litw_zI0EoGde3miDssXEAaBixgnipRbyTcLVfCaeHn5eyVzCNF65vRks1Xn8IZBKsOUANREi5ofL2Sqo651ixOxzcjo1AkxQZQ2MIFQ8OANgLKcBWM9joBJdEIF_8xFv--GpwnMb2tbowRekZyUzG5XPVJVLl1XoHdfhMBLq9VjRrlAdAhgHSvOyci4GG1gTv7pXhcthKPx42f1NaOUvZvUpYvJQzVUe-ydtYNHGsIHLc6nqdAmQ1ozLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇩🇪
قوی بمون، جمال موسیالا.
❤️
💪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/104223" target="_blank">📅 13:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104222">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNr4_ZVUCGqJjROOMza_YAGYuHoyqyCKVjr93AhZxV2NCzXl_AYrEVZaZqPWrrFzQSl7vAQ8ttStbnMMVO33cK2WeubXWTZe574nBnGw6SGxzw-uh5Xs7SdKhj0dGkZ7IodVfC2mtOJjoSmZVGH8Nfp1pjkpcss55BtjucZ0VUXtwpdDRmuAyeXMNu42vgnbd2cAam1f3aDbsukABN7IvSM2JDawSP8kaDzgQpZDCvMhpebzBiZAAqK33LtRnEg_s-avoWBw_CpQZw5oM3cZu-wr9cAIEXDDxSl5pcNZ78AnNTIZMODrwxeSqppBJcx5r_1F71KMN8SVgl0RbTLfUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تمامی ورزشگاه‌های فصل‌جدید پریمیرلیگ انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/104222" target="_blank">📅 12:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104221">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d1d403113.mp4?token=taCGp1mZJ_zRhUoysne0VjFpZvdRE9nJ8mk-3DagBoYXmjHDHhDo-_pZel4CZvE9r0GdjZdRVGSUwieugqBT2tKhjimeAn30ibF_bv1pJAaEkJV-SPfC9Bfz8c3vXjM1K8sguLM6bkX28C8pNYy0M00MQZLG3lXdFZ6QxqVKEUpbzfSdzCEwrOIn5B0ALqfahZIYB7dYopejvHZTucXvSZMfcWRO0mZV8q1e-36C8x-zsp1DdWI_UyUAagcGp0kdPdqGpS4ZMoulc08HSbSGpoHgUPvT6TRK55BzOYzHFGCreONCDSad3tkidjJZJyDxko7t8xaYwU7Zh0sHEdrSgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d1d403113.mp4?token=taCGp1mZJ_zRhUoysne0VjFpZvdRE9nJ8mk-3DagBoYXmjHDHhDo-_pZel4CZvE9r0GdjZdRVGSUwieugqBT2tKhjimeAn30ibF_bv1pJAaEkJV-SPfC9Bfz8c3vXjM1K8sguLM6bkX28C8pNYy0M00MQZLG3lXdFZ6QxqVKEUpbzfSdzCEwrOIn5B0ALqfahZIYB7dYopejvHZTucXvSZMfcWRO0mZV8q1e-36C8x-zsp1DdWI_UyUAagcGp0kdPdqGpS4ZMoulc08HSbSGpoHgUPvT6TRK55BzOYzHFGCreONCDSad3tkidjJZJyDxko7t8xaYwU7Zh0sHEdrSgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
برگردیم به زمانی که گرت بیل به رئال مادرید پیوست و EA تصمیم گرفت به این شکل تو FIFA 14 پیوستنش به رئالو اعلام کنه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/104221" target="_blank">📅 12:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104220">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
‼️
🎙
افشاگری داوود سید عباسی از شب‌گردی‌های دردسرساز ستاره‌های تیم ملی در لبنان برای دیدن داف‌های بیروت در سال 2000: زور هیچکس بهشون نمی‌رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104220" target="_blank">📅 11:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104219">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0abb8b5a2b.mp4?token=v7Mbqu3b_i6zpvFsChe-csD6zC3I7rzF0OUwQ7yeC8C1UqFxapxC5Z48yGK5J63BH80tocnHCMSId9BRDwgasXdrr2oJUzMQs28kefzUH9L0i0B0MSe8AXpvzT7ILBu3FHlceG9vcj-A1sm8mKMvnWaAEPTAcg0nsVvHRCc3xGHdinDQAdY9Rfw7URKyEsJxFCvnNBXTc5VKzBr_92XIpZP5IoXwc7gHsBvDs80NczbpMoidPrwY2AvJoJEBjFt-BeWBzIsdCPoSByRmDRoKVgRXgudR7OjMPrsUSFkmm2ehr86z_i4zG-sTDL7kr7RRE4zxm9c2Z3WlgA1xN3SuVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0abb8b5a2b.mp4?token=v7Mbqu3b_i6zpvFsChe-csD6zC3I7rzF0OUwQ7yeC8C1UqFxapxC5Z48yGK5J63BH80tocnHCMSId9BRDwgasXdrr2oJUzMQs28kefzUH9L0i0B0MSe8AXpvzT7ILBu3FHlceG9vcj-A1sm8mKMvnWaAEPTAcg0nsVvHRCc3xGHdinDQAdY9Rfw7URKyEsJxFCvnNBXTc5VKzBr_92XIpZP5IoXwc7gHsBvDs80NczbpMoidPrwY2AvJoJEBjFt-BeWBzIsdCPoSByRmDRoKVgRXgudR7OjMPrsUSFkmm2ehr86z_i4zG-sTDL7kr7RRE4zxm9c2Z3WlgA1xN3SuVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
کنایه تند هومن افاضلی به نکونام: کاری که با محمد ربیعی شد بعدها با خود نکونام می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104219" target="_blank">📅 11:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104218">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/813ecb9de7.mp4?token=mtbcl7y45bNyp-pjKDb-baffNhvcC8sXuPYfn166p-9XBFzXmLlBSRPb67aEclTatp-WD0sodMKZbyhaAOREP-3pFT3oX9ImZ2j8185AkMu4C90zxChZNetWjvagLnnzkazHc4RfaNZfgfmQRyjqxJ9aLbWmZfwnwJbZU6C9pObogTXJz530coG20rqx4k2ZrUCvSEQYFmZ6sIH77Rj7YoHXrrjp_EswiHJNsv6AhGvF8izMrGgQLvhTzs98aqOxO35FqW_hdtgMqn0vtKJsG3iLi9aLcKejqmR93m0R4GrfIrRE-uWFdUOhc9cO1UjWUScZrxRLY6pt--zT3b7jvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/813ecb9de7.mp4?token=mtbcl7y45bNyp-pjKDb-baffNhvcC8sXuPYfn166p-9XBFzXmLlBSRPb67aEclTatp-WD0sodMKZbyhaAOREP-3pFT3oX9ImZ2j8185AkMu4C90zxChZNetWjvagLnnzkazHc4RfaNZfgfmQRyjqxJ9aLbWmZfwnwJbZU6C9pObogTXJz530coG20rqx4k2ZrUCvSEQYFmZ6sIH77Rj7YoHXrrjp_EswiHJNsv6AhGvF8izMrGgQLvhTzs98aqOxO35FqW_hdtgMqn0vtKJsG3iLi9aLcKejqmR93m0R4GrfIrRE-uWFdUOhc9cO1UjWUScZrxRLY6pt--zT3b7jvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
‼️
حمایت ترانه علیدوستی از ملیکا پارسا شاکی پرونده پژمان جمشیدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104218" target="_blank">📅 11:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104217">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452261b723.mp4?token=e1AeEU1J9Ri4_aPxX7L7m6zv2a7D8d5V7VrQkxryoeazUMEVdTUof9EGwTknDe2Lc1pSWYW5h90hPjMxcbqs_qRCDBwxfdMlDt6z-OsdY04aYvJ_V-fWJS6CX7U1mXyvhupblPRxC--vbhwcf7ykTtzOqXdQ1pA4A6Hg0z023kVbxASkAG0MCIhCrkLwamYJmrks2ilX6ZSO4jRGKkQaZj8ZwV3b8Vv6xpZBC5CPoEyzNiKzsksm3z36wfi3lWClkc1gyIzuNQ2KYMng_5Q3kvzUadPW3paqvPdhb58R8guzki4VMbGOzlxDMMAongf3iUOhvsZezmR607Do1Ft-K4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452261b723.mp4?token=e1AeEU1J9Ri4_aPxX7L7m6zv2a7D8d5V7VrQkxryoeazUMEVdTUof9EGwTknDe2Lc1pSWYW5h90hPjMxcbqs_qRCDBwxfdMlDt6z-OsdY04aYvJ_V-fWJS6CX7U1mXyvhupblPRxC--vbhwcf7ykTtzOqXdQ1pA4A6Hg0z023kVbxASkAG0MCIhCrkLwamYJmrks2ilX6ZSO4jRGKkQaZj8ZwV3b8Vv6xpZBC5CPoEyzNiKzsksm3z36wfi3lWClkc1gyIzuNQ2KYMng_5Q3kvzUadPW3paqvPdhb58R8guzki4VMbGOzlxDMMAongf3iUOhvsZezmR607Do1Ft-K4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسل‌جدید هواداران در استادیوم‌های ایران
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104217" target="_blank">📅 10:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104216">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/104216" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/104216" target="_blank">📅 10:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104215">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMkftkE-pQSfDitEbKu5r_35lhvayhXHb6gsWeXRhvpYLLuUiacRAEFbv7ovUHTbB961QGnx439A9ILKhwWn8uXNXUHCBC755sLESBn-mOAEMkQtbZosvgQkhFfaNITL81s_DsC72algJZ_9dkaxtfWiwBRnkW_lHKiSmBBnqKQ_tc4mb2NAXiZOnbrRfrEODZdDd06Q06pdkzcGlWuhdzBtuJpt5bQLV89zB7n4pCAMEikfJkZgQ0IKZ3hty1AA9jaXWz-sdwJEbhhaxBBi2N9yzJ0kEwTh3Bq_RAufrbdZTZ1Dkv9i-1G9orBczdWZZsu9zwonQ1C3L5G0zpeg-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r29
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104215" target="_blank">📅 10:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104214">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f95dab32c4.mp4?token=RVn3stWizLCLlMcNVepHUVOIXYvwb3K7RcReREVEUhmtvVaPukgndELpYhFAENyNDkdcLE058b7wE1qxfjREiGN6VQvN-JRTOPDQn4cLEDRzf7zZQTLFfroOFWWHr9QAnqFArk-_htRdi86LKiXEloMFPg_m1SSaJZC1pUpz91BMcmJPfwbvN_tRANFsy4WYMLndkyRWk-mS7HrzGeezXKv276SsQQc_18LFv8krfAWZke1Y9m1mLYrMSQeB7qOeBlVWaixNz7cRUDwj40t2NiqwdddfbIj1xMpZu9ffPC-QuOj_230A8eQ27Tzweg04gzYo5pih0tUhUHl9tJj1YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f95dab32c4.mp4?token=RVn3stWizLCLlMcNVepHUVOIXYvwb3K7RcReREVEUhmtvVaPukgndELpYhFAENyNDkdcLE058b7wE1qxfjREiGN6VQvN-JRTOPDQn4cLEDRzf7zZQTLFfroOFWWHr9QAnqFArk-_htRdi86LKiXEloMFPg_m1SSaJZC1pUpz91BMcmJPfwbvN_tRANFsy4WYMLndkyRWk-mS7HrzGeezXKv276SsQQc_18LFv8krfAWZke1Y9m1mLYrMSQeB7qOeBlVWaixNz7cRUDwj40t2NiqwdddfbIj1xMpZu9ffPC-QuOj_230A8eQ27Tzweg04gzYo5pih0tUhUHl9tJj1YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
تمرینات نفس‌گیر وینیسیوس برای دلبری از ژوزه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104214" target="_blank">📅 10:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104211">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DuEXkPS39CFEQMZMnrlEktacUoHxKx0VFU59W-Zzo_dkXa4L6eAgKfzWfJ561ESGf73FilFmihc1HntyPgW3Jqad4G8nGcxl7YzeZzbWXrLJlDVaBzAluanMzs5MRbgO2KehXyGDBIDD92TvKBQQ-S0vO6iBENkkOs4JgH6cLfBPZZ9qOAXqSo5dgTWUdyfiemywp8dz4rsQ0I7g0owTkdyjtgXhF4l-mvceQF1htXSrKoVKvYzhItpyzU0e9bKFP0fPdd0lfpQmHp0MCMaLgCLIIFWD8_EQ-Mil-B_AYRr4XWWhd5ntFPB1ODlWhCiDOP1ZsUzpBj1OfEF1V-tHKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oe8rAzkKQ7GZpZizZDLLuUZXGdBOWWOgCyl3e3UEnN5GlECAZh4yDc6Jq_SdxMha5uEaAtOAGe2-EJ9VYiQ2G-bWFkeriuBDeQFSASN-2pwRVwNmB-upbjtmDzswlGCMC6hRKAWow0r6ZjGX2_O6y0IGIJA5Lpq5ltoUrSEYJi4RNJFTaCx8Nt4vX8TemRYV37TexKJ8I3CPiuKnov_ZADZxdwoechzDnRvQtjpEGjL1_DLfhOKNvPjFsvEUIN3z7N5LmCAa2AdR_VFh_Auw3fp-KAdEmeH-PGas3bPrDSdtM9gN0_yGTPkU5dEHqywLNe0ybwDqJV_5-7ih4XOvlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gy09337AQftdV2pDWiX9-IJ5-q3cQhu42DxFZhdxx6d8TO90lVmQkgLm5wFq_XCM5pyX9BU3nx-n9GV5NMdoULyr6iiJvMtd5Zg_0FLTILW8Rq7OLnZyq_YEH4QgzT3hzcGdPSAeY4kCJO23af8h9yWBjutbCehzmZ239dwSg8Zlr11RGrCBW2z7CDrIqv0rqQIN7Uy2I5iTEbi_rvJ1HTcEcF86fjqq-b1qf4iXRidbZ-QFSU3t2otEKM0JxKNsj9A4o1uJPwm114Xb4G9sPzhB0lCdjKK_u_t44aOSDZL5K57wvGhhJKPcWUn-MafKioSqCC2eAArdLjjNFRDISQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
هوادار فجرسپاسی در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104211" target="_blank">📅 10:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104210">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268128aa94.mp4?token=h9Vk7IAAqr5T4CaCjOmMDTCF27xdAiR-uBDH5yfCXrkL73gkmi5qNSMxW8ZkTGNYSx1i_NvCnrqgTEcps-GZ22NS-cdnFdvQUcmvI5cSAjXi8XrVXKSn_GZX8DDkg9m_pPN5kCATOYGN5aK55934lQtA7Ernd-ISKUXy8ZVYDYfx19UGxhm5jTE7H29h978j8Y1gkRU8lfiAdp2qYYx_7uLXqBHqi9JsRcHPCaNYUQsOfirCbmtm91foBlqiRusPMmqH5PynnstysMO3tFVoojHw_lGxjG5VJeyCT7eb3gNLfof4z0wpSt5Jf5HNscjdFbqlotI8zBDVCgzBKBx_24V_qyQBCNHvG8D6HYLSh2IvUaqYCb3-9gGPpKPlyacKjghfRCD9pzCz_bK-oFrvn4PX0fgrOdYK_KQELxU9XbzHOYioZDaY_yDzVwN3zpdn2f1b-T4xDbVITFNviGPsKCVt3naNRhv66EjULUTI7Fwef9NnCbq7jk5sXzCzkDcviizUreHdVgOMHCO9N98wyx85BVbjNTBkLtQcjcYZcT2kzywtT08U4bUiQ06Vk7Rn3AfxLOqT6QwqmKo5qh4I3B4s3D5I6Pgo8VpNRWaAu9yYr09Yrhw3chtsFCEwEssGsqs8Ifc3fhHVhK1j196zBuV0OTZwXKT3tdAUDKgmrUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268128aa94.mp4?token=h9Vk7IAAqr5T4CaCjOmMDTCF27xdAiR-uBDH5yfCXrkL73gkmi5qNSMxW8ZkTGNYSx1i_NvCnrqgTEcps-GZ22NS-cdnFdvQUcmvI5cSAjXi8XrVXKSn_GZX8DDkg9m_pPN5kCATOYGN5aK55934lQtA7Ernd-ISKUXy8ZVYDYfx19UGxhm5jTE7H29h978j8Y1gkRU8lfiAdp2qYYx_7uLXqBHqi9JsRcHPCaNYUQsOfirCbmtm91foBlqiRusPMmqH5PynnstysMO3tFVoojHw_lGxjG5VJeyCT7eb3gNLfof4z0wpSt5Jf5HNscjdFbqlotI8zBDVCgzBKBx_24V_qyQBCNHvG8D6HYLSh2IvUaqYCb3-9gGPpKPlyacKjghfRCD9pzCz_bK-oFrvn4PX0fgrOdYK_KQELxU9XbzHOYioZDaY_yDzVwN3zpdn2f1b-T4xDbVITFNviGPsKCVt3naNRhv66EjULUTI7Fwef9NnCbq7jk5sXzCzkDcviizUreHdVgOMHCO9N98wyx85BVbjNTBkLtQcjcYZcT2kzywtT08U4bUiQ06Vk7Rn3AfxLOqT6QwqmKo5qh4I3B4s3D5I6Pgo8VpNRWaAu9yYr09Yrhw3chtsFCEwEssGsqs8Ifc3fhHVhK1j196zBuV0OTZwXKT3tdAUDKgmrUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
فن‌کشتی بازی دیشب اینترمیامی و فیلادلفیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104210" target="_blank">📅 09:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104209">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08de822050.mp4?token=Mzz7odM9hDstZUeF4Ik26L0lSZWv1BBEKk4GG85MWRNsTP8BPNJd3vXZpJGhuUV97VbYURytS2BZeZM7ITxvQS5vsHuCUVH04Wtp-30bcOjo_aDG-isYAegJgXeMEbR9aB9IqNBFZu0cB5DGQKhwBXZ1UUqPHjC_ShJLZT4rLB7Ey9Fw1rUwUbuLgWog8VcvsShbgHWa8lHQ9ddjQ6FKGFyekz-mTFlLWXa4t5xAlEFcBL_YgZH1c4l-kijJa7KfI3v1XRCyH8F7CIyYjn_5WsKtird1rqYI9hM5qW3Rl8anPG7eNs7WfaBRowofLie6vNoOmp-R55_HYZCgtl48Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08de822050.mp4?token=Mzz7odM9hDstZUeF4Ik26L0lSZWv1BBEKk4GG85MWRNsTP8BPNJd3vXZpJGhuUV97VbYURytS2BZeZM7ITxvQS5vsHuCUVH04Wtp-30bcOjo_aDG-isYAegJgXeMEbR9aB9IqNBFZu0cB5DGQKhwBXZ1UUqPHjC_ShJLZT4rLB7Ey9Fw1rUwUbuLgWog8VcvsShbgHWa8lHQ9ddjQ6FKGFyekz-mTFlLWXa4t5xAlEFcBL_YgZH1c4l-kijJa7KfI3v1XRCyH8F7CIyYjn_5WsKtird1rqYI9hM5qW3Rl8anPG7eNs7WfaBRowofLie6vNoOmp-R55_HYZCgtl48Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
گلزنی لیونل‌مسی در بازی بامداد امروز اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104209" target="_blank">📅 09:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104208">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiDE2VwIYdRTHX_Eqbiq7RLlw5m8qTtutwzbuK1TEkplkeSOsaEe0z8yeSoTv0Uu3Bs72E5IqZyJ77uxnn3E2CT_st23W5sJakXuwaxWA97DTaq26wONhy2CnJNFktcK3F-N4r2aNXB-btTuTFjPTdgrTJMts0t5kTJQj7DNV2jGSZ2JPw-46ZKWzdKNEbteaoMhUqTFrtKsnc644Q91RHVEI4FQBdY2W2pMNnCel-j-M_VIxYBJGufmLPb4U2TiY58fqxCELzfgQOiYo8y-keTT_2FAK2eYWCcOSTla5GkVHjKyu5QBi_c84ndb4cXIgQjL69KzmbCoP_K1iB-kOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇺🇸
ترامپ: از این لحظه شدیدترین فشار اقتصادی تاریخ که تا به حال علیه یک کشور بوده، علیه جمهوری اسلامی اجرا می‌شود و‌ «هر کشوری» هرگونه کمکی از جمله اقتصادی، نفتی، صرافی و بیزنسی به ایران بکند را شدید‌ا مجازات می‌کنیم. این دیوانه‌ها گرفتار شدند و به آخر…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/104208" target="_blank">📅 09:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104207">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d04c58120.mp4?token=NAK9aEBwLQyH4pcZOYevsA0gWFVAZZ27X2dkomRlBr4WSiuN7raakPUdfOb8uo0la9OjdHk49ep3oqg8ggc1j0jZjnQRrOSHpwDQSNSp3wxFOBoCgDxBe9PmS4IeMHt-TUJr74A1jdkeS_4FQxkdudQNBToMQ8KR-_wG2aJQGchkQTexaPdliHJNAWw8Rh0kpKk2VnA-HpCZBAl0DmKYJIxWWtuc7wofZtiKGxC4hTg6w4r_axYCjXX_OC6OS22svIOVb7EBh8-H5_GCXs61hxD98CQYJknvOxkutt40BygZZpGbCSh65mJG8NPpynJxkNwugjdEwxYmRHVG1pHvew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d04c58120.mp4?token=NAK9aEBwLQyH4pcZOYevsA0gWFVAZZ27X2dkomRlBr4WSiuN7raakPUdfOb8uo0la9OjdHk49ep3oqg8ggc1j0jZjnQRrOSHpwDQSNSp3wxFOBoCgDxBe9PmS4IeMHt-TUJr74A1jdkeS_4FQxkdudQNBToMQ8KR-_wG2aJQGchkQTexaPdliHJNAWw8Rh0kpKk2VnA-HpCZBAl0DmKYJIxWWtuc7wofZtiKGxC4hTg6w4r_axYCjXX_OC6OS22svIOVb7EBh8-H5_GCXs61hxD98CQYJknvOxkutt40BygZZpGbCSh65mJG8NPpynJxkNwugjdEwxYmRHVG1pHvew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
آرزوی دیدن دوباره آزادی برای هواداران!
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/104207" target="_blank">📅 09:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104206">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9be7548134.mp4?token=VXFb4rvmCAO_vpkSXCdc1Oj1MVIC9VDqWuWVSINP2HS1rAOda43sftI7G1_KH36FISNiBrnMyCQkCr78bCq0DPLxrkU3Ri1PThvEajWCmV7ZELrYnFrRyGklTY41qadY8sFGbOwMNJq7v3RLQRlai7uxiKcELZ8oFRtwuinkeup3GD1kbIL0piqisRSgPmHwTzmIRK_2r4kCmPXCsWB19Lm6OmZ7G1cUBByNacxNoFLzI7obNJpYnXAfr1l5J0terjbVrc13IHkd4mu3R9EnaCEj0isZ50TxOg1xC9v9IRwu8DS0JmHhI18OzxfW1Sh7tOTo4yp6ZbVb_GDwGJ4n0GbbzbuH-TrvBA-sLkxqDS_Y6Fgr5BQDlxGujpRJhBQR8VcXvOTFXSXg5M4ksoK05BkzZMCJj5TkhRaK9Nz63_jAqcr_vWOr3V5A3Fx0bPhdN3iUO9cr_sRuae5_2YM5qQuWtBzaiM-NMTQ1Ergea7GY6kLTqU5Q8oE-lFlvw-q0JYWdBlRQJk6-OjzX0QRlznFy8jfshihdSDy68EpwgYOpfWLya4wzDe1sndAj9I6IjjkSKGX5KFVJke4h_8PX1YVWvLLcwvUVzOpb38izeEaA4n4znwQsvQ10K4RerHuaG8XMBx0kwnzw8EzkaU9l9JW426AjCu80wWfWiK7AhuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9be7548134.mp4?token=VXFb4rvmCAO_vpkSXCdc1Oj1MVIC9VDqWuWVSINP2HS1rAOda43sftI7G1_KH36FISNiBrnMyCQkCr78bCq0DPLxrkU3Ri1PThvEajWCmV7ZELrYnFrRyGklTY41qadY8sFGbOwMNJq7v3RLQRlai7uxiKcELZ8oFRtwuinkeup3GD1kbIL0piqisRSgPmHwTzmIRK_2r4kCmPXCsWB19Lm6OmZ7G1cUBByNacxNoFLzI7obNJpYnXAfr1l5J0terjbVrc13IHkd4mu3R9EnaCEj0isZ50TxOg1xC9v9IRwu8DS0JmHhI18OzxfW1Sh7tOTo4yp6ZbVb_GDwGJ4n0GbbzbuH-TrvBA-sLkxqDS_Y6Fgr5BQDlxGujpRJhBQR8VcXvOTFXSXg5M4ksoK05BkzZMCJj5TkhRaK9Nz63_jAqcr_vWOr3V5A3Fx0bPhdN3iUO9cr_sRuae5_2YM5qQuWtBzaiM-NMTQ1Ergea7GY6kLTqU5Q8oE-lFlvw-q0JYWdBlRQJk6-OjzX0QRlznFy8jfshihdSDy68EpwgYOpfWLya4wzDe1sndAj9I6IjjkSKGX5KFVJke4h_8PX1YVWvLLcwvUVzOpb38izeEaA4n4znwQsvQ10K4RerHuaG8XMBx0kwnzw8EzkaU9l9JW426AjCu80wWfWiK7AhuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
زادگاه‌زیبای اسطوره رونالدو در پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/104206" target="_blank">📅 09:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104205">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZaISrCIc7KNdETrM-F3RFLGXe7k-aidfPWq7NlCztMXDm8w6xJjzjbhg94xWHbIzV3pBkXiPED7q4gCqZYGq8goN9W4HT0LYGW9FaphFGIpY9rR7EOh8vAoRC9XSvspt-9Jfzw2HCIrfY9nDgRXLguEyJmS5HPAscd5gADd4kVLJzPTmJtArDyAHm_538Y0MSCVU4Uz12HwH6lVJ898znGY46F59-YbG2Dd4XLN8xe4ADkhJE0q3SVbtVJDz4KjCPxaqpgylMSvH2L-mqDoGlE1CfnwXzGAN2FV5Wo-YN8aXH58hC1lVK1ADDtG5Ak0sLf2vjJF5sQeofe8qKb1ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇺🇸
ترامپ
: از این لحظه شدیدترین فشار اقتصادی تاریخ که تا به حال علیه یک کشور بوده، علیه جمهوری اسلامی اجرا می‌شود و‌ «هر کشوری» هرگونه کمکی از جمله اقتصادی، نفتی، صرافی و بیزنسی به ایران بکند را شدید‌ا مجازات می‌کنیم. این دیوانه‌ها گرفتار شدند و به آخر خط رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104205" target="_blank">📅 08:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104204">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctLSOAQpeRw5_XAEj7lbN_weyZfQyN5aezxG7rSp3OKyZ9bU4KxrxwXlOraZJGlb4hw29g12xX95t9lee34zOSbx_PA0n4KsHBnbQW35M7uQF3T0kvm0AB8zSWRPdwfJ7pmNNqcyuZZ6GTTd6UNmVaaDrRvns26_OFnc2vQPgacREx7UJdAIBXl5RS1Qu1zhpk1PPkc3-WMaMFNLAexjgfX9pkwqSFgLdxA2328rLb4JxZuIfSvgqeQ-qN7bJUo6l0qpnNHbKmb_JOEkiclv5LyqHN3zjE9QL2_nIVVmppz8K98jelzIJKeEGaurorJTBUgqwRqtHKchFC-2NYC1NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
افشاگری یک‌خبرنگار از دلایل عجیب و خنده دار عدم صدور کارتش برای ورود به استادیوم برای پوشش مسابقات لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/104204" target="_blank">📅 01:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104203">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/185cc08019.mp4?token=RihpowSHuBkyQ_HEHuejb0iewObSanAaRBYtoIgnbnFkecTT9hMQwZmfhd25uM0z-WaauJ84jOwOvoQaxM_Htc4m3DJeobFgmdsmXwJa_Cad6_HuznmUr5MYY1FY6bGbYUQWOm6LGqiW0pB84cuZV4QPgfiPN-5Yhf8Ca0zQ1rPK4lOKdVvK9JswS8q9r-8ppMb4Sy6qSDRQHWUzPEayyi3gGQNLrIex5ulRGGLhv_3O4OYXhp4XxSAazuCy37C6WyD_k5fFvMqjR6fxU-2Oi7DOY_-NgHy3aEnntj77hkn_E-JkmSg7wX2wGxpC6GuZLiSE2x6-HVW4VlBODMQwyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/185cc08019.mp4?token=RihpowSHuBkyQ_HEHuejb0iewObSanAaRBYtoIgnbnFkecTT9hMQwZmfhd25uM0z-WaauJ84jOwOvoQaxM_Htc4m3DJeobFgmdsmXwJa_Cad6_HuznmUr5MYY1FY6bGbYUQWOm6LGqiW0pB84cuZV4QPgfiPN-5Yhf8Ca0zQ1rPK4lOKdVvK9JswS8q9r-8ppMb4Sy6qSDRQHWUzPEayyi3gGQNLrIex5ulRGGLhv_3O4OYXhp4XxSAazuCy37C6WyD_k5fFvMqjR6fxU-2Oi7DOY_-NgHy3aEnntj77hkn_E-JkmSg7wX2wGxpC6GuZLiSE2x6-HVW4VlBODMQwyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚠️
یادآوری خاطرات تلخ برای پرسپولیسی‌ها توسط حامدلک در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/104203" target="_blank">📅 01:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104202">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
جدیدترین پیام هوادار روشن‌دل پرسپولیس: راضی از رفتن خیلی‌ها با چاشنی پیام برای یکی از مدیران پرسپولیس!
فقط هوادارای پشت‌سرش که هی سر به سرش میذارن بهش میگن علی‌پروین مادر...
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/104202" target="_blank">📅 01:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104201">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnJFXQy85gmyihpKc9-GSKht-OyTE625dh0N-pkBO6iorksZE1YBIBbO5A-Jcb_cjCPcMbzsrWOz2r3xiVO5WNsBIhufYTmsadlyoQtlhCM1EKkSkq34bKspInnIM_ScDICuntPxEocppA4frNTQ_0QOyxBjyjPe4CDgLDpMmnTVWnibCHTYV-gSRDqKyVQY1K6ZFj49DCaPdf2O7SnpSKJsUU798ts6RBbJrm2sGL5GPHZz_5j6hq_U6QejXsl7OPbcPHJgDRwG7JneZDBP3-h_gxwub59my-LIImcekzG7DlLyvBBBJKEMD86E38TuiEQnjgQYLvDmrXgQnRn5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اورایلی درباره جدایی رودری از منچسترسیتی:
🔺
‏"همه می‌دانند که رودری چقدر بااستعداد است
‏و اینکه حضور او چقدر به عملکرد همه بازیکنان اطرافش کمک می‌کرد. حضور او، جریان بازی را تحت کنترل در می‌آورد
🔺
‏بنابراین، جدایی او یک ضرر بزرگ است، اما زمان سازگاری فرا رسیده است.
🔺
‏ما چند بازیکن جدید جذب کرده‌ایم و نمی‌دانیم آیا بازیکنان دیگری هم به ما خواهند پیوست یا خیر، بنابراین باید صبور باشیم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/104201" target="_blank">📅 00:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104200">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJA_s3_d51ypl8czh5U5WGG4y2lNv1cp0Dnk_wbnF8mw0LVUPskxxflO_fHwwYaKVCgMPlX4rHUEO6T0yjZLdAhmkscmsE22N6VprlqmnqGkLg521vFb8yQ-KPyrOWJ-2FOa0VCBUkpU0IMSnNyHHvGGMGFLIKysj2osuZR9gq2Nnm9oBcAEoEzYobZ_dwkocoTDg8JHfKuzD11VFenP8skt97-PBm9CO8H3WWNeAzYCyk0WgQpjs0ZvItb8IlOEq8srI_0O2wkJ38ZtmJHgQxCfwu0tZi59AyCTjP9i007c7Xb6ImAK4xLK0iCoU_nZWc3RixHGeL5FUph1eTrG-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: انزو مارسکا سرمربی سیتی شدیدا خواهان جذب انزو فرناندز شده. سیتیزن‌ها در روزهای پایانی نقل‌وانتقالات تمام تلاش خودشون رو برای جذب این بازیکن بکار میبرن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104200" target="_blank">📅 00:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104199">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔥
امشب چه تیمی می‌درخشه؟
⚽
کدوم بازی گل‌دار می‌شه؟
📊
کدوم تیم ارزش اعتماد بیشتری داره؟  ما بازی‌ها رو قبل از شروع، با آمار و تحلیل بررسی می‌کنیم؛ نه با شانس و حدس!
📌
برای دنبال‌کردن تحلیل‌های روزانه فوتبال عضو شو:
🔗
https://t.me/+nbm7Tb2pz8VjMDlk</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/104199" target="_blank">📅 00:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104198">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=Ag_KXXNL5snTos9iZ9HipcAfcLqjdRgxPYGl9k3QU5p5k71ybVeVlqb6MANqJJ8HzcZCTb2qzfsVCmR5Tj9Snsg0mYTDUQFhP65NjMeHjnkQfD7xHNkRHmLX3gug2HI-Ty1MIKrGX9YG-fV7phd_DigqlJCaZYk-pofuUhsOY7p5cb1l0iu4JnN15adf8_iVnInfiJ45XDxzKuNUv_z6WcrkzJQwl1aqYpUjA2A8qYqJAhSQzyO9Z57ZtSqSyS26e5v_Lk_cvB2Mqz1CzpdyUhHhOiqAB3IYuc9ViGPgXkwdkwgYWBMMe1ut4szAFfAixFLzqPq1S1DzhvVLsWF0Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=Ag_KXXNL5snTos9iZ9HipcAfcLqjdRgxPYGl9k3QU5p5k71ybVeVlqb6MANqJJ8HzcZCTb2qzfsVCmR5Tj9Snsg0mYTDUQFhP65NjMeHjnkQfD7xHNkRHmLX3gug2HI-Ty1MIKrGX9YG-fV7phd_DigqlJCaZYk-pofuUhsOY7p5cb1l0iu4JnN15adf8_iVnInfiJ45XDxzKuNUv_z6WcrkzJQwl1aqYpUjA2A8qYqJAhSQzyO9Z57ZtSqSyS26e5v_Lk_cvB2Mqz1CzpdyUhHhOiqAB3IYuc9ViGPgXkwdkwgYWBMMe1ut4szAFfAixFLzqPq1S1DzhvVLsWF0Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
امشب چه تیمی می‌درخشه؟
⚽
کدوم بازی گل‌دار می‌شه؟
📊
کدوم تیم ارزش اعتماد بیشتری داره؟
ما بازی‌ها رو قبل از شروع، با آمار و تحلیل بررسی می‌کنیم؛ نه با شانس و حدس!
📌
برای دنبال‌کردن تحلیل‌های روزانه فوتبال عضو شو:
🔗
https://t.me/+nbm7Tb2pz8VjMDlk</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/104198" target="_blank">📅 00:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104197">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7QF_k8oQO8XVyl5R0V5ZA8hLK3N8aU949YAv1k6vJrW_IAjtv3f6yNZif5OEIBBGWoCefwS7q6uL0j2m4f06KQ3nRfQ9qX9FazcdXD37d7dupUObhlfTa6lhVR8Efh30Ze7bdwGOe2BOP8UVjIykgu3ms2k9BYkiflfWp53sPyy2EJ4RlcfT3hOR7iDnRR3hbgRFPRKUvQO2Y8uUtlpH6FOm9QCQv-aEOdTuBmGwxZQ8s0xgOT9cqpBHe3JisJKYTrFhSF82ziFk16WmTXvSHoYWKnEQyT13zXbRIbNgSfxkXZZkTBqWj63Omz34tqL2HogMNdPu6gpk8q5PTTp7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇸
هفته‌اول لالیگا؛ برتری اتلتیکو در گام‌ نخست؛ جانشین کره‌ای آلوارز گل‌کاشت!
⚽️
اتلتیکومادرید
2️⃣
-
0️⃣
مالاگا
⚽️
⚽️
کانگ‌لی - الکس بائنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104197" target="_blank">📅 00:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104196">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCOuZzSEO4VTDUUHonZZf1Kz62ayosgVTI4FsTOZG-8HhQgo2fNBEVWlIaXhfAftUsB7e9CNXOz2iASxS3TaoG0JNp4_A_juj5cvS7fyOz6pNUfkSLf1L6wRI9Vp7WfThKpUdEXhT5RtVMM7csWT1zfygSL4H5kOWxduYoV2ig0-g3qVWfioSLWUogh_EV9DX6yWiGOOWk9M7NErcg78oqL_c381X6x_-ctu52KYW36Cna0bitK1fMHQC69COFQI7CtBzwlT4wFZW6BCWiyTCYScPNyMAQiBd5jJ3VpXax-AahAET8Y1gziAv9NDSRlJT95moeR8thqPP6fW7PzmDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
دکو مدیر بارسلونا: قبل بسته شدن پنجره چندتا انتقال دیگه خواهیم داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/104196" target="_blank">📅 00:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104195">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cT5Gf7MbmBOBb7eaCzE_KsBACk0I0FlQRhy17h_y_5GRLW3AYDgDJOdJUHFP8q5Yfuh5Kkxxg5KIaqFdz1wTIZTu_HG_1kjHVi_zMuZvrWAIDm_P2jcFcZQxY3HbmL0M6apWqIePpxc_jxZQGv_oYIaS7t8D4pVvRKRVO7lq8o4NBBjJA3AbtApRVaLL0Q4tzJ2N9ErHjwmuwHHthTcGzYk-xFPanaqd5wQYJzOF-g67VUHoJalFLUmGWtM2e0rE3XSITueZt9CHKyhuTV6O8aZZc7jM1RPS1s-njes-34gHYZlKlD__CwEfoCnQIHenvFnzkaTAp3hHKqLKjl5U5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هانسی فلیک :
«ما به دنبال جذب مهاجم هستیم. دکو تا اینجا کار فوق‌العاده‌ای انجام داده. امیدوارم و کاملا فکر می‌کنم که این موضوع نهایی شده باشه. من به دکو اعتماد دارم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/104195" target="_blank">📅 00:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104192">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmcaCks1gIn22awbAwBCa_N9IIUexS4Nl4l4mwTBjgQMgBQGPVkSgCZp9nFnxtpwL-VETSvgiArFoRfhxD-d7zgdjpm8k4ZF8J87ix-5GZ9YiD5DHL9AAYeehACyx9YRxxTTsLdpgK0aDOB9bll8F7WtSEqQskrbTEkArwmX8UQVcbQO3MQTuki4bL-rZItqsH_QYqdup6I-A9_cuKUapsGUMIHL5DUrtgc939Gs2lvQd0MSLu0z6EglTTJcGMTQGgxXZdNOb9GwFcj8NwKSn4W0FACsJkG37hKTd965yXL1UHBf7iE8blAjo1vF0no7l3waqOKaAvdfLlFrrWvscA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هم قیمت بنزین تا ماه بعد و هم قیمت دلار و ماشین ایرانی رو تا اخر شهریور ماه گفته؛ این کانال تمام پیشبینی ها همراه تاریخ وقوع رو میگه:
👈
مشاهده بدون سانسور</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104192" target="_blank">📅 00:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104191">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b7fd471b8.mp4?token=QxFuGYgIE5PM_c4VUuFvYxe7FL_GbMm9AQZtDPFS_nhLxExEuK2DfofghwkrLaJbt4J3kFkepq81VLWcOLu5_0jr-B-dq1whwLP3hPxl3qe0i8lRne9Zc3-fkDPETYFVq-1dW27a8x9AfwwcNnai0EiNHAxuFU9Z51VAQOQx0dhWw_UmlyZD7sUZ76f7R9j6hCHQUvsvBIpDqmiy0H7AY416bwyzP8G2nMgHxrgRQvL_vGrnMrD_gdRd0xle5vaUXteDtG7o1dM0Tyr45xV4z1DuPHrckEY7xtDiZWwnrV0KJAsMEIaCOXes-lqVxuKGnKBguTXGKYVvM_Z8ShueOaaeFIM3btbsGlWYhAyPBQ4Dehd5Hh8OVR-QvVDQAHT4OYYs3HmcnrqUZdGLHQ17z_P-1v4wUj69kYCYMFGVlboz9YlyFOII8sTqt8sL-a_BcSFwwMF7ErBYrB9CYCWNjdtiwZHOTbKaOBUDcCvpQdZQ6rVtn0XvtVb3Av_Zq5QJcUPWZY9yDXShGd_ynDTzLYIu_Ah6IxClPKcsbNH4pE87DiyW1C3SCUDodLnwX01xOQO3e5gp8bqZs6afPOBS3dfQ3EZv3bi5f68a0_I-xaZZf92txmbtrLf_1YP-Q8K9D290LhYRHaIPy7CKpyr09wHz8e5YgB_rLQJh6gR5iy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b7fd471b8.mp4?token=QxFuGYgIE5PM_c4VUuFvYxe7FL_GbMm9AQZtDPFS_nhLxExEuK2DfofghwkrLaJbt4J3kFkepq81VLWcOLu5_0jr-B-dq1whwLP3hPxl3qe0i8lRne9Zc3-fkDPETYFVq-1dW27a8x9AfwwcNnai0EiNHAxuFU9Z51VAQOQx0dhWw_UmlyZD7sUZ76f7R9j6hCHQUvsvBIpDqmiy0H7AY416bwyzP8G2nMgHxrgRQvL_vGrnMrD_gdRd0xle5vaUXteDtG7o1dM0Tyr45xV4z1DuPHrckEY7xtDiZWwnrV0KJAsMEIaCOXes-lqVxuKGnKBguTXGKYVvM_Z8ShueOaaeFIM3btbsGlWYhAyPBQ4Dehd5Hh8OVR-QvVDQAHT4OYYs3HmcnrqUZdGLHQ17z_P-1v4wUj69kYCYMFGVlboz9YlyFOII8sTqt8sL-a_BcSFwwMF7ErBYrB9CYCWNjdtiwZHOTbKaOBUDcCvpQdZQ6rVtn0XvtVb3Av_Zq5QJcUPWZY9yDXShGd_ynDTzLYIu_Ah6IxClPKcsbNH4pE87DiyW1C3SCUDodLnwX01xOQO3e5gp8bqZs6afPOBS3dfQ3EZv3bi5f68a0_I-xaZZf92txmbtrLf_1YP-Q8K9D290LhYRHaIPy7CKpyr09wHz8e5YgB_rLQJh6gR5iy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌های بازی بارسلونا ۲-۱ الاهلی مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/104191" target="_blank">📅 23:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104190">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/065326b085.mp4?token=hbaqJmX2Qcv5JeFjmOpZKJV6zf6QJpzLVQ8bBpxYUuDx_vI_qKqtVLG360RO5Env7zJwfIHleo_gXKEln5M9z_bW9n4mw4bMLWkFgNzonN9rlSwRtZJ6ckYw-fzaMEEMW5bj_g2J3ITjc8WVs6picKbDVVCQHqHlXr7gICPq5J_97SJUsLUv8TQTkRYqg5A6BX_9qUMk3q9QpRohm5HCoUuqNFAvb6uEzMPlHSC8OEBs1DJcCFcREONmnSo0Fm82trl07UdHYQJR4rPs0RR5J_LuJdm7-RGPNcCz_TLNY_FXdXWglUhs_uPJfh8K4ZrbHxw_VnfYnXl4pMo2SfOZSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/065326b085.mp4?token=hbaqJmX2Qcv5JeFjmOpZKJV6zf6QJpzLVQ8bBpxYUuDx_vI_qKqtVLG360RO5Env7zJwfIHleo_gXKEln5M9z_bW9n4mw4bMLWkFgNzonN9rlSwRtZJ6ckYw-fzaMEEMW5bj_g2J3ITjc8WVs6picKbDVVCQHqHlXr7gICPq5J_97SJUsLUv8TQTkRYqg5A6BX_9qUMk3q9QpRohm5HCoUuqNFAvb6uEzMPlHSC8OEBs1DJcCFcREONmnSo0Fm82trl07UdHYQJR4rPs0RR5J_LuJdm7-RGPNcCz_TLNY_FXdXWglUhs_uPJfh8K4ZrbHxw_VnfYnXl4pMo2SfOZSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
محسن خلیلی: اگر استقلال تصمیم بگیرد دربی رفت 90-10 باشد چرا که نه، ‌اتفاق بدی نیست که این قانون یکبار اجرا شود/ من الان «مهرزاد معدنچی» پرسپولیسم؛ ‌این هجمه‌ها کار دشمنان قدیمی است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/104190" target="_blank">📅 23:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104189">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae9b74973.mp4?token=GFLtzWLg847hn591ti6IUkIVW4N6JWlPXU4kFchHVWoVl5CXxNRLycSWlHgSmNfTlYQIjnqNhObs44sscpru8COCCo5IaYEEw5AaT5_RjPE49kPljWJGB49YPZ7CPycOSQKN8TnaVjpBPivmIT5ZUg0wTFJ6lWDT4g060eQrAVs3mfY8E_udMA7uE3gPVBetlP0KfEJm5lraeealgHXjWQMmkOVerxe9LUwjnJ380f7bZI22w_PzH8mYswdFpcGMTfK4g4WMaalWJvBv0knWvTmD1ZA7eZSYFArCeFVjZPBtu2SJhgxSwVV7bhwJiXAo8AbbnvFfBWq2WrX4-_6W5HZLl7i37H7dQlXukDRijsdR7w2av4feJ0o6fA7yNfu5wyB5S85vsrlP04Y-aIXhx-l23z5r696vJSkB-BefBpjHBi4OG2W_Sul6a1gHKwjR7_tbFCc_TTOl0R34EKmnrvgxafBjJUx0jf6ywevNegEKrE_yzOwaVp8lrxle9n6yj2BJBQRZqp5KlAPRhWpxBAf4PqZy67deZp1GRF3cpUD3W9FMc8ame2DNgs9nBmF5EDS6Yuj8ck5howHU1EGXGXz63k9R3YWbJIEIs0ZQxQOloF25JrAgy0Q8JaXtPUnKA0EYaq2XKmu4uBR7bGsMJb7r4skW641gxcsdhd378fU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae9b74973.mp4?token=GFLtzWLg847hn591ti6IUkIVW4N6JWlPXU4kFchHVWoVl5CXxNRLycSWlHgSmNfTlYQIjnqNhObs44sscpru8COCCo5IaYEEw5AaT5_RjPE49kPljWJGB49YPZ7CPycOSQKN8TnaVjpBPivmIT5ZUg0wTFJ6lWDT4g060eQrAVs3mfY8E_udMA7uE3gPVBetlP0KfEJm5lraeealgHXjWQMmkOVerxe9LUwjnJ380f7bZI22w_PzH8mYswdFpcGMTfK4g4WMaalWJvBv0knWvTmD1ZA7eZSYFArCeFVjZPBtu2SJhgxSwVV7bhwJiXAo8AbbnvFfBWq2WrX4-_6W5HZLl7i37H7dQlXukDRijsdR7w2av4feJ0o6fA7yNfu5wyB5S85vsrlP04Y-aIXhx-l23z5r696vJSkB-BefBpjHBi4OG2W_Sul6a1gHKwjR7_tbFCc_TTOl0R34EKmnrvgxafBjJUx0jf6ywevNegEKrE_yzOwaVp8lrxle9n6yj2BJBQRZqp5KlAPRhWpxBAf4PqZy67deZp1GRF3cpUD3W9FMc8ame2DNgs9nBmF5EDS6Yuj8ck5howHU1EGXGXz63k9R3YWbJIEIs0ZQxQOloF25JrAgy0Q8JaXtPUnKA0EYaq2XKmu4uBR7bGsMJb7r4skW641gxcsdhd378fU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
نمی‌دانم شیر استقلال از کجا آمده!؟
🔴
مدیر روابط عمومی پرسپولیس: شیر به حق به پرسپولیس می‌رسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/104189" target="_blank">📅 22:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104188">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/702ffd5ee9.mp4?token=ORVXo7J-_6zZda5O6QevJ_LyGxrBb9FpfqhZAoPCwVkfiEnWaNVOBeIM52abuTqwZwJwkiX6ABhLgiON4ONo5qy2t9kY7FsKIpTsNrhfHmifqaRzerw02r1O_8Ta-oqBsic_-yYZw2vspKa7QkKdOyGVccVBAX8cy7UVL9Znac275noWbpppf01qkInZ37BEkXPHXJKc1Mxdu7rI0qEZy6Wa61Td6M6ARKWipAp7l-6n0kiTv2B_aB4FMWiHXJu1r-5V13P7feWpQTWen1xR1y85IWf6fK_iNsvZjWqRJeh4FnvxYMNfzQU7KufEJWhlI5EsC6qTwpk3lg7fJ2901Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/702ffd5ee9.mp4?token=ORVXo7J-_6zZda5O6QevJ_LyGxrBb9FpfqhZAoPCwVkfiEnWaNVOBeIM52abuTqwZwJwkiX6ABhLgiON4ONo5qy2t9kY7FsKIpTsNrhfHmifqaRzerw02r1O_8Ta-oqBsic_-yYZw2vspKa7QkKdOyGVccVBAX8cy7UVL9Znac275noWbpppf01qkInZ37BEkXPHXJKc1Mxdu7rI0qEZy6Wa61Td6M6ARKWipAp7l-6n0kiTv2B_aB4FMWiHXJu1r-5V13P7feWpQTWen1xR1y85IWf6fK_iNsvZjWqRJeh4FnvxYMNfzQU7KufEJWhlI5EsC6qTwpk3lg7fJ2901Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
کنعانی‌زادگان: ناراحتی اورنوف طبیعی است ولی همگی تابع تارتار هستیم/ دوست دارم یک گل هم نزنم ولی قهرمان شویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/104188" target="_blank">📅 22:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104187">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuFsk5qb8zDy7vEJMCvj4v9zklZcCELfQreiEatzKhvhDhgGmYNok6QuDwGmGxtk4zAjC5IXPQy1EIECi2m1EGz7mGAuN1E7gHykU3nLWNYD6zvxnvsub_5hNI5eL91bIexawxBfa2Ael_ZrNvwPUq0iriXrw4jT-cqeQEHLPpEpfEtv4NIqB6_iRMXb8jgo7CZYeWRt3eWPvaIFKlh8oxO62SWp0KwTrvv7ufgd7LVe1owxJ2bIUTAXO_0xRnmlY1toOhl97THPJ0hVX_tK0wd6OQtmo9ylMuNt5esuVGyKc1oc3CPeJjo3D0umMGPZZNmX-puEJDGAihiE4aloLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
📊
جدول لیگ برتر پس از پایان هفته دوم با صدرنشینی پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/104187" target="_blank">📅 22:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104186">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a4eaad83a.mp4?token=TXXxS3Wu7RjCnJDyOvpAVXM3cl1XpFBqGUh3v72BcjZpNm7SUltOgyh957R_wqa1NMeT0B1gqTEQ5sF87QyaLVNYcrhFouqvWAFC9hisXo2Qdz2d8oysEQuIUm_r2enEgKiO3NDQGH0Bb6MlbiWlhib8eDjQy6liHuzUHHy0c9Y0xFpFnULMQ8U8KFCz6gxlKHz-OoSeysfEwuSkzDZH6dXc6N0UAtYuDBDLk_PxYx3OJwo1yrnDPvQIzBFf2utFhfYRynqNZSCAJ8QSkxQY_orgQO-Aq43UzGJmcGsO0hh405judpr5eAHi5Jv92W0lF57oIaFYDzEIifUbTmf8Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a4eaad83a.mp4?token=TXXxS3Wu7RjCnJDyOvpAVXM3cl1XpFBqGUh3v72BcjZpNm7SUltOgyh957R_wqa1NMeT0B1gqTEQ5sF87QyaLVNYcrhFouqvWAFC9hisXo2Qdz2d8oysEQuIUm_r2enEgKiO3NDQGH0Bb6MlbiWlhib8eDjQy6liHuzUHHy0c9Y0xFpFnULMQ8U8KFCz6gxlKHz-OoSeysfEwuSkzDZH6dXc6N0UAtYuDBDLk_PxYx3OJwo1yrnDPvQIzBFf2utFhfYRynqNZSCAJ8QSkxQY_orgQO-Aq43UzGJmcGsO0hh405judpr5eAHi5Jv92W0lF57oIaFYDzEIifUbTmf8Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
علی بازگشا، سخنگوی باشگاه پرسپولیس: اگر تضمین بدهند در بازی برگشت با تراکتور هواداران حضور داشته باشند، آنوقت می‌توانیم تصمیم بگیریم که بازی رفت با تماشاگر باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/104186" target="_blank">📅 22:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104185">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85bc3fae83.mp4?token=Iv-4X5QqyGclTTNVbYPh_wgjEZEs9lxYtAqdJodrUQONVVJ-l5MG2sCmp6DX09OVNKR_aMr-1nA90sR2hjGGwnNlfq2AxeO6U40pnKJUhaKq5iME1z89k-AsLrYge5C28byMO3RNK_u1j_L0_TibNJX4eL5IXrq6vFKwV2sEi-XApxzrDqBrMj3f_yK2Un0QMXTpRxQtX9bWhZVoSehMvGfzpGC21kZezh1nqazfNV-7KJmBNkfgPRYDeEmqi7vgQPWznMnP7jNQvHDUhXn-Gfj96OQyxvpH7Qw54dOq1_H0IBUAn0Sm6lcOyJZerMVzG4Dr4GAkDLTHPz1lVEa8kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85bc3fae83.mp4?token=Iv-4X5QqyGclTTNVbYPh_wgjEZEs9lxYtAqdJodrUQONVVJ-l5MG2sCmp6DX09OVNKR_aMr-1nA90sR2hjGGwnNlfq2AxeO6U40pnKJUhaKq5iME1z89k-AsLrYge5C28byMO3RNK_u1j_L0_TibNJX4eL5IXrq6vFKwV2sEi-XApxzrDqBrMj3f_yK2Un0QMXTpRxQtX9bWhZVoSehMvGfzpGC21kZezh1nqazfNV-7KJmBNkfgPRYDeEmqi7vgQPWznMnP7jNQvHDUhXn-Gfj96OQyxvpH7Qw54dOq1_H0IBUAn0Sm6lcOyJZerMVzG4Dr4GAkDLTHPz1lVEa8kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
شهرآبادی، بازیکن پرسپولیس: امسال هدفمان قهرمانی است/ سال قبل تر از حضورم در استقلال به پرسپولیس رفتم اما قسمتم نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/104185" target="_blank">📅 22:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104184">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43972e9198.mp4?token=WvANpy0bRkqSUYONNGZv--6CN2eceN1TT4YKgsG8j1SH50VfH1svEOzpRHP9F1oAF2yoPjdJGidJsq2_h_q3WkOuSDuLwPpIHC8-rU6YQ5h06fFHi4YZIPMXynAGypEdK_5ALZEU29tSw6s-thmoqQY0j7wtMpZ62mkG9NvhX46blrDf5vaqtgd4kLWesKpsmG_SdOr6ZOQSm2MsB02hdj1jzzwye5KZXtr3LQg4FxHzXdEyLZHRm544SUnUC-hMc_dhFxyMxO81nm1395rRnXUpIUxTQs46RECZXP2EwfCXN6LdXeS4BNXOAr5YmnMuCHSso5X31_jb_80QLFd2Lm4tDPzhPxYvPZsIg_OvmZz1JxnX5t5biP8pAUPA_CnjLCd9o_E30Iq29zQS2K4psNpyS1Ff6XkwE9Tf-MJoVpyZswzzm6kB3mcN_pQ55Qxou8IOJxygGY4r549RsphrkcqZhX4gGAqlqXyimqvXHTZvRk5zF1kTIQY4j1ShBC-DNA92nquXo-4Ls2dwOVFNuKeo5CWnNKjMqfqku5P834c8x5TaxKeChjFlijSVA86MSERxGfhttdEUoQCa-oTbdZc_WHxRC7CdxPDpAdgQBZegCha84zToTVhYpoHclUrZwYe47Nhes3qX42nMk3UlRs5IiOozGE2uuAQzZG6teXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43972e9198.mp4?token=WvANpy0bRkqSUYONNGZv--6CN2eceN1TT4YKgsG8j1SH50VfH1svEOzpRHP9F1oAF2yoPjdJGidJsq2_h_q3WkOuSDuLwPpIHC8-rU6YQ5h06fFHi4YZIPMXynAGypEdK_5ALZEU29tSw6s-thmoqQY0j7wtMpZ62mkG9NvhX46blrDf5vaqtgd4kLWesKpsmG_SdOr6ZOQSm2MsB02hdj1jzzwye5KZXtr3LQg4FxHzXdEyLZHRm544SUnUC-hMc_dhFxyMxO81nm1395rRnXUpIUxTQs46RECZXP2EwfCXN6LdXeS4BNXOAr5YmnMuCHSso5X31_jb_80QLFd2Lm4tDPzhPxYvPZsIg_OvmZz1JxnX5t5biP8pAUPA_CnjLCd9o_E30Iq29zQS2K4psNpyS1Ff6XkwE9Tf-MJoVpyZswzzm6kB3mcN_pQ55Qxou8IOJxygGY4r549RsphrkcqZhX4gGAqlqXyimqvXHTZvRk5zF1kTIQY4j1ShBC-DNA92nquXo-4Ls2dwOVFNuKeo5CWnNKjMqfqku5P834c8x5TaxKeChjFlijSVA86MSERxGfhttdEUoQCa-oTbdZc_WHxRC7CdxPDpAdgQBZegCha84zToTVhYpoHclUrZwYe47Nhes3qX42nMk3UlRs5IiOozGE2uuAQzZG6teXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🇮🇷
سوپرگل‌فولاد خوزستان مقابل شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/104184" target="_blank">📅 21:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104183">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">▶️
🚨
🚨
🇮🇷
🇮🇷
خلاصه بازی پرگل و جذاب و دیدنی پرسپولیس و استقلال خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/104183" target="_blank">📅 21:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104182">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMa-mRIiopuMJF9ZOnebBh3dGnO_i0H2jatBHIT7UO1XUnU4AYByLcTO4d0tpPO3mDhhhCB1Fr81TKfTAuPWq56SulfX2R1zdEmMJR3icLPJNnyAsh_lZw-gMW51BNpmPyR_MOUs1Bbqzo9Be-WRR31QRrqQmAmGJbIuD3Ri7wftGwCSaOmX3z9lAnW6Vj2beEYicom07VTgWUIK8TCpU3qaoH3hX6nmMUxoMwBWKD99Prt6yxy3H8F-oz3HE77EBeXBh_Bu1KfEe75_7iBJiXJGCHpjg_m0CeOir-q7-Km9e_KqWuKwFxqApL9JIEiBj_x2H6aJ8IyYijZ6GMPgqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
پایان‌بازی‌هفته‌دوم لیگ‌برتر ایران؛ بازی چشم‌نواز در شهر قدس؛ تیم تارتار برای رقبایش خط و نشان کشید
🇮🇷
پرسپولیس
😀
-
😃
استقلال خوزستان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/104182" target="_blank">📅 21:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104181">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a62ef1f46.mp4?token=NePGekeNuzoVID_TksyM1pDiFa9RN9SkN1l8FPHchJE6FBAgrgt2UPfX25WwZMmqNwAyp6EkS0tksymvAeLpYEjg6qvVdaOgXLHciKWxNmdU_j4f5L9vFN4gA3BynFP7FQQNSdT_KMOb4bGYr0jViSIW0Xwsziz5hXtpwAmh1SK85vgeuzpLv0ZKeXdK_sH_8UQ9PNglR6CQgC2K54ZNOsXYlZOUdZdeCi0mzOjWwCFVTUy38cR3QhRPLj8dyeWF9JZnRGGTreATFMRBcVJFKGfaZgmsnCuFY0f6B4RyyEv-wW6cjZrc3Ho5pqCc9KoJ0HOz4Ab5gXyWFsd__0GfLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a62ef1f46.mp4?token=NePGekeNuzoVID_TksyM1pDiFa9RN9SkN1l8FPHchJE6FBAgrgt2UPfX25WwZMmqNwAyp6EkS0tksymvAeLpYEjg6qvVdaOgXLHciKWxNmdU_j4f5L9vFN4gA3BynFP7FQQNSdT_KMOb4bGYr0jViSIW0Xwsziz5hXtpwAmh1SK85vgeuzpLv0ZKeXdK_sH_8UQ9PNglR6CQgC2K54ZNOsXYlZOUdZdeCi0mzOjWwCFVTUy38cR3QhRPLj8dyeWF9JZnRGGTreATFMRBcVJFKGfaZgmsnCuFY0f6B4RyyEv-wW6cjZrc3Ho5pqCc9KoJ0HOz4Ab5gXyWFsd__0GfLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
گل چهارم پرسپولیس به استقلال خوزستان توسط شهرآبادی(90+3)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/104181" target="_blank">📅 21:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104180">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b2857b1d.mp4?token=jYvewFgpk2pBXPHgDOejLRYOCttjLza-IyV96CH0u7JLM_U9xZ_XDG-aX00LCsoA3P25QhPKlBbG5N34FVTL1wUwJ-V9JX9v9iYzvZiPjfFZR2RLvwZpNJs4kmbE1-VuB1ZX3BVk7zUW7f6TDVRqIRgRn8u3j_04hVUclurcxAYM3aNfxeaoe1j4TstezyE4eJxFZI6PUmWIBiSZN4aDjtphWguSNAcNdVXTJDaLRcbSmoP1HZpZOckYkz-2P6uJVPrWu7GOHmu672LTJ4Lsq2GCQpbSfJB3D8_MatW5Fuq4G-Fx5hIVElZvsfe3TPpj3pNPpccxIcPE1hBLUn3iCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b2857b1d.mp4?token=jYvewFgpk2pBXPHgDOejLRYOCttjLza-IyV96CH0u7JLM_U9xZ_XDG-aX00LCsoA3P25QhPKlBbG5N34FVTL1wUwJ-V9JX9v9iYzvZiPjfFZR2RLvwZpNJs4kmbE1-VuB1ZX3BVk7zUW7f6TDVRqIRgRn8u3j_04hVUclurcxAYM3aNfxeaoe1j4TstezyE4eJxFZI6PUmWIBiSZN4aDjtphWguSNAcNdVXTJDaLRcbSmoP1HZpZOckYkz-2P6uJVPrWu7GOHmu672LTJ4Lsq2GCQpbSfJB3D8_MatW5Fuq4G-Fx5hIVElZvsfe3TPpj3pNPpccxIcPE1hBLUn3iCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇮🇷
گل‌زیبای ملوان مقابل ذوب‌آهن دقیقه ۸۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/104180" target="_blank">📅 21:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104179">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohWzDp8dxcl1ismcGc10GSLYCjS2A6gegFAAcvcXAiYpLOK5wf9h79FVsspAkq7Wyz0RWkDidgOIU4aZ_YutG5MeqpomEeTd04eKCjEshfYYJEPQ9cTPShhGpViTEQZa8cWaUFj1U80l5hEbm9WS6gc7S4cDrfrlzkucHjwiRZmbvT0PdDj7W0FKj1JxlA8zWpNwzTW6DxGJkDHqM_IwEuLt9POLWibzxVHVJCU054zHDyOFaUHtnjjpunxWuhdzjppkE-CZune7v5_vjoHXL00aV3cbxqXpop7dDLopDFiNMw3HtBTeAJkO87sFKJ_DkiTF2DHYiRPdRQA9QpN2_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته‌اول لالیگا؛ ترکیب اتلتیکومادرید مقابل مالاگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/104179" target="_blank">📅 21:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104178">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543b2ef6fe.mp4?token=rzs6qp5Dwfx_d79oLdtrpXBcYgZEiTmUEmEpZS3xZiacUDbP1PzjIJIkIwKrFck8blhzYkzmqx64vLicCzuNBD84IKb85Imme6IoIdOi02Tyix9iIPAHuObNOo-du8wiTq7ciVR7pPQ7T7QfKHiyz2H0VpZu_WmYc2saGA3tFhnxMnRO3ZuDkYoBvELsPlyJ3mGxVCVNbSQwWJ0aTmXTF0IVxtTsQw15K3vIj341Y97hk0tDud2yZ-A3boXbNzm5i4gZQ7LFFJJhXJOTY-zax-iTt5BFC3tQgpuBPeqRc2klkT60h4XA1lGbwQBjflRXc6F4uJVo_zW89w2B6eNLfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543b2ef6fe.mp4?token=rzs6qp5Dwfx_d79oLdtrpXBcYgZEiTmUEmEpZS3xZiacUDbP1PzjIJIkIwKrFck8blhzYkzmqx64vLicCzuNBD84IKb85Imme6IoIdOi02Tyix9iIPAHuObNOo-du8wiTq7ciVR7pPQ7T7QfKHiyz2H0VpZu_WmYc2saGA3tFhnxMnRO3ZuDkYoBvELsPlyJ3mGxVCVNbSQwWJ0aTmXTF0IVxtTsQw15K3vIj341Y97hk0tDud2yZ-A3boXbNzm5i4gZQ7LFFJJhXJOTY-zax-iTt5BFC3tQgpuBPeqRc2klkT60h4XA1lGbwQBjflRXc6F4uJVo_zW89w2B6eNLfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🔥
🔥
🔥
🔥
سوپرگل پشم‌ریزون زبیر نیک‌نفس در بازی امشب مس‌شهربابک؛ یه لحظه روح مسی درون نیک‌نفس ظهور کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104178" target="_blank">📅 21:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104177">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58ba1302f.mp4?token=O52MRBtHJgQkK1ZkFNU9geW6bPK-fVq-Hkwv_N3l-oBRIQ1sii_Vv80wwfcCf05vRid5TnfR0dMKcAMiw3X5LJ5uQ69kUP9c3G_BHKPJSMJOt_BraoOA9dnn5BZmMDoEGWIxAO7DwN40al4SweCxe9-7O4nj9Z7jsvXOtSTQNawuVGUjW76QkfYCFzsvrr93X-SbNW4QHlfNpEKkJhcKXVDNk07aBYfVvamGqKgqqdqS0xljhZB3r7ZRTZP9oagpbGeUvDABigXPmWw2fxZ8pRR-d28bDYnE7vQOPUXLzo-ze9dmXgdVgfgYOZtLPGYgDUwrJiMC7MMMcl003q573Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58ba1302f.mp4?token=O52MRBtHJgQkK1ZkFNU9geW6bPK-fVq-Hkwv_N3l-oBRIQ1sii_Vv80wwfcCf05vRid5TnfR0dMKcAMiw3X5LJ5uQ69kUP9c3G_BHKPJSMJOt_BraoOA9dnn5BZmMDoEGWIxAO7DwN40al4SweCxe9-7O4nj9Z7jsvXOtSTQNawuVGUjW76QkfYCFzsvrr93X-SbNW4QHlfNpEKkJhcKXVDNk07aBYfVvamGqKgqqdqS0xljhZB3r7ZRTZP9oagpbGeUvDABigXPmWw2fxZ8pRR-d28bDYnE7vQOPUXLzo-ze9dmXgdVgfgYOZtLPGYgDUwrJiMC7MMMcl003q573Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل اول استقلال خوزستان به پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104177" target="_blank">📅 20:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104176">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvvqeTFCQVxcHmpx9Az8LY_jjXYfqDsvTAI_AgToGKHfzGSfU1ld_cjgeyWA9COkrr9pht3dmDCivjK6YXV96bprt21wa_Pabot0CPyXY-syDoT62dQtNKMm83NbmRTFwGzYNw7J9ZHdBtw5b8ZRpVxJ6eTgLb4u0G96sOO4U3u0nZKJLVry8CcbhaG4KKzsIuPiNnbrxKnuZZW8s4VfukJkNlHT1qsnALBDvfdRXLdT8XxqdEAlEAVBLR5D7m8nQVyNQn7g8nI6dP1tV4YWk_E4JqoZDeKkzsT2JVGY1PnFrqk9OQq4m3AMqNB0xTyfUSEqiQexbcF4Lz3NMpVtbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
استایل ساده‌زیست بالنسیاگا رامین‌رضاییان در ورزشگاه فولاد آره‌نا پیش از بازی فولاد
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/104176" target="_blank">📅 20:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104175">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔥
🇪🇸
انفجار نیوکمپ پس از اعلام نام رودری و ورود این بازیکن به زمین چمن ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104175" target="_blank">📅 20:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104174">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_2Zf9gXICr2-_qBGliotzqtugqZ8fyoUWXrsvMLlUFlsW0KA4LZHVBYWSKEYp3d_tDEGlw5RcG0sIzibdqqjYnOO9-YCmp-H5hLQawlh6yNWiojpqFG6pGZBJ9HSdIkL1akzrt7EY-ak5EvOsKsE_Q7dbPL5-IwUBggiG3rLonqp5PN5BNqNR6vMkWqXfWjBIUQy0LJndv9JawWQJ5pOcCnj3-BzRBRLwUJKWemSurhGDP32TLCoe0bNtDyprAMoi6m7UTPOSdy-vqR5Vg42ssMFQHBMHnGMqwqoWFnqhrB68GDez4tzvFwiuAURNvy3dt4_7hvQyI-i_xvIexM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
😳
🚨
🚨
🚨
تفاوت آلوارز تو عکس‌های رسمی فصل های قبلی و این فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/104174" target="_blank">📅 20:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104173">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41445f46c8.mp4?token=ePr2231flg_rgt-ZO3G4BDPqujL5srrG1gcqLsmj5lZSRwy9uzC_huatsNYEuijYVErtf_sBNCneHgcCifXXbUfqfJbVp2vLIlSwOu8LgmFi82lYB-twaoRCI_bSQn_vJOBgC7ytWSMsoi_byTYp35e9wpD4MO2bfjRGVGdjdT1ArOVpgAZX-UgH_KCo9x9ICy0MK7mxXdf2Pl-wUvusCofxyJuhngMrRPCRja84NERCyKcT0px__8SjS_-r39al7if4utzpaxkujv_1P--THjZonL9dAfjD7YRfWBynPkEMEzLD2jZipcMMJzvSKGPW-hYR8Vt2wW2DfVl1r8aCRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41445f46c8.mp4?token=ePr2231flg_rgt-ZO3G4BDPqujL5srrG1gcqLsmj5lZSRwy9uzC_huatsNYEuijYVErtf_sBNCneHgcCifXXbUfqfJbVp2vLIlSwOu8LgmFi82lYB-twaoRCI_bSQn_vJOBgC7ytWSMsoi_byTYp35e9wpD4MO2bfjRGVGdjdT1ArOVpgAZX-UgH_KCo9x9ICy0MK7mxXdf2Pl-wUvusCofxyJuhngMrRPCRja84NERCyKcT0px__8SjS_-r39al7if4utzpaxkujv_1P--THjZonL9dAfjD7YRfWBynPkEMEzLD2jZipcMMJzvSKGPW-hYR8Vt2wW2DfVl1r8aCRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
سیاوش یزدانی، مدافع پیشین گل‌گهر سیرجان به الطلبه عراق پیوست و‌ شاگرد علیرضا منصوریان شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104173" target="_blank">📅 20:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104172">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d92806f40.mp4?token=FGETWwt0z2vLMJT-TXMC0fM4pmOOVN9AeFkx2bLdZeuulCj0u4N3OjFFEZqIPxVvNYcc5uH8jMgdP8VCTuWRfP066QAA7htM0M5hDlzOJGZ_KNw3QO5PF0YeUPNjOiYLM3xtnTt9LOdKj7tdF-1Mw7Nja7SoQvBCdj0ne--mvO0vCHqoBDzia5HyitSbteD6S93JNpv9JorGuF3wWy244-2In5kMp20e99uV6rwjg5nGFIP0nni6XTMc27zp7Slub9UOM0LUlVZ5TsGVDcZv5LpT8uzXxW6j61NH9DAIexPugDOHy3PU8MRVjawRU7T3MWHG16p8QYG0SBk-JCYX5L9ab9AY5URJDucFXL3LPxPECFIAceIdQZMrb3OzoU-YSnUbLqP9IbFr7KdFjUBQR5QRKcN65Zdc7qjY7m5MR8pV5q0-Gb2v9mO-_sunIveasAgWrCSzxy8clkSr_XH2k1ndmxMgSgb-447gU4U4JtTbNX71VWZXplKDF8KHHd0Wwz72MpDobsJ71E7lHXupTUBYgR-BEH8I70yYkJknR0AZe6673zfFmDbWX61iBjuPo538tyeVc2znsSCnFl5-WXEUMmVHQVREs7mz8173TOHGQWrS5ipVCpBfQFuey1dDuC2YpX1-zqhun2R9yV2QFumwd8cUkOlknlOeenF2kAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d92806f40.mp4?token=FGETWwt0z2vLMJT-TXMC0fM4pmOOVN9AeFkx2bLdZeuulCj0u4N3OjFFEZqIPxVvNYcc5uH8jMgdP8VCTuWRfP066QAA7htM0M5hDlzOJGZ_KNw3QO5PF0YeUPNjOiYLM3xtnTt9LOdKj7tdF-1Mw7Nja7SoQvBCdj0ne--mvO0vCHqoBDzia5HyitSbteD6S93JNpv9JorGuF3wWy244-2In5kMp20e99uV6rwjg5nGFIP0nni6XTMc27zp7Slub9UOM0LUlVZ5TsGVDcZv5LpT8uzXxW6j61NH9DAIexPugDOHy3PU8MRVjawRU7T3MWHG16p8QYG0SBk-JCYX5L9ab9AY5URJDucFXL3LPxPECFIAceIdQZMrb3OzoU-YSnUbLqP9IbFr7KdFjUBQR5QRKcN65Zdc7qjY7m5MR8pV5q0-Gb2v9mO-_sunIveasAgWrCSzxy8clkSr_XH2k1ndmxMgSgb-447gU4U4JtTbNX71VWZXplKDF8KHHd0Wwz72MpDobsJ71E7lHXupTUBYgR-BEH8I70yYkJknR0AZe6673zfFmDbWX61iBjuPo538tyeVc2znsSCnFl5-WXEUMmVHQVREs7mz8173TOHGQWrS5ipVCpBfQFuey1dDuC2YpX1-zqhun2R9yV2QFumwd8cUkOlknlOeenF2kAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
گل سوم پرسپولیس توسط ایگور سرگیف در دقیقه (48)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/104172" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104171">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnRpzMJkmsvMJIMfuBMgajzNa9FUQgClCq-yQCkrX-aTt-eyfjNMgYkUw5h0yX6nz1apsHCdDNfeoRuAAGLNuY_nktzoTKbeNZZxa6bxdk6D-WTpBKOx1pCWJEErOFHkUnFSfFVk9EPcDMefy9c2Apd6Y8x-Tq0rNqUiaywZEKqymj5KFmSoAWJYXbm0ub05N6yOXgOcyDtPF1u1O8izYLkwb4_9JagowxPB-C_9ppDQ-0vP9vtti3qU3LXFWTNFVRD6HIBabv6lPXWRyuvB7Rfjw-5ZBFTfvPC3whHNu4EPmeUXBrwGGQ55QwLIE_mrYPGIwPRzBqgYegkJ3ZxBRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمق خط هافبک بارسا
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/104171" target="_blank">📅 20:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104170">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeAi3Ij0FIV98HgYURiZxG2Sl0q9xciUDgAzO9ln-xtz5N3Hd4OR-1Pfs9SKJf-s1-fRjeZFqn3DBQqeu4NXxJNjhP1CmcVmEu518zrGV50TC6q4ncRP5B9yQ5gI22ZbC9tiditHYti_o9grC4knbJKE736LnhE5cZnFYiIFFRSW59ihvLa6RDr6hr426IsZ0GdEAfaePCXnLWU_gVWQAhyKSr05UfyntVeJ2j23i3fA3wbbZTjqjhxcSCWySWymHZMotKZt9HTrMnjsDPUZ2XJ5k7qpnjBBT-4OD_DN59fKBdWgyGfyiWsQ-8gOdUDVHrB6Bd2PgMC54EkFgC_dEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جام خوان گمپر
🇪🇸
بارسلونا
🆚
الاهلی مصر
🍗
🗓
ساعت ۲۱:۳۰
🔴
انواع آپشن پیش‌بینی برای این بازی در بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104170" target="_blank">📅 20:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104169">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd2bcc49ca.mp4?token=rDdHCGF6kumg0PYJ1c-ukxflMaq4M5WebiKD6f_4SneE8ZUUyxn0Jlx_E2bQ8ot622s1bWK0IxS5uAWIlFJB1TL_yFBu5VcotUpUlhxqUVV6DbbYgvT_xG5H24fYQ1oZdDkXJldjda9fvC6b8nBkeIrWIbmxjGyr42oAlMRpLhQb_NZ7sY31gb2fcIrlHdJsfsGyVukgz_HcP5l_H8rUI4MMHJxLaekhhpFjLgBAQSO1QuItBsNFnXyfZ9wocbtc3S1Y_VNULqTweb6M4qxCrYsTZXlxEVvP72CZc__z9uMpuW4gLiD9rumoYNafec6coNY_L8QGVuaLbbTqCnkd1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd2bcc49ca.mp4?token=rDdHCGF6kumg0PYJ1c-ukxflMaq4M5WebiKD6f_4SneE8ZUUyxn0Jlx_E2bQ8ot622s1bWK0IxS5uAWIlFJB1TL_yFBu5VcotUpUlhxqUVV6DbbYgvT_xG5H24fYQ1oZdDkXJldjda9fvC6b8nBkeIrWIbmxjGyr42oAlMRpLhQb_NZ7sY31gb2fcIrlHdJsfsGyVukgz_HcP5l_H8rUI4MMHJxLaekhhpFjLgBAQSO1QuItBsNFnXyfZ9wocbtc3S1Y_VNULqTweb6M4qxCrYsTZXlxEVvP72CZc__z9uMpuW4gLiD9rumoYNafec6coNY_L8QGVuaLbbTqCnkd1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🤕
ابوالفضل جلالی در دقیقه 26 مصدوم شد و از زمین بیرون رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104169" target="_blank">📅 19:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104168">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXZBhTIBCrfFuGrNwPz9fdGrn8qFggfbS5JBGiODaeiLYs0ISwWJoTaTfNUn0SywbO5fhWxzFH9S_GJN0K5m3XQJTLbDmqfgVyF-q660GQdD3jUf4rx3z52uQRYz43vi2ccPLsBrk9zLfOQnD_BpDASS03nbCy1MH0bHdb6VX2yR-oNH588CbaCKVpKo_GRu--fTAZK_8Jn-fA9xv-q9OBoJaaRc_aYDU1H3oTLArynki1bCq_VBWImqTwoVcCK6whre-HVx856tavSeh9vLVynh72FfSC0bVCJ9AH1riLfSUDCIzPC_FTk3zRzlIZhqoXx0JXkh_bqePKKEFwSiLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
ترکیب رسمی بارسا مقابل الاهلی؛ ساعت ۲۱:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104168" target="_blank">📅 19:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104167">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b73b9b3bf6.mp4?token=hTJZZF4jDdPqnejAdia2irun5lxZTIFdF5gLISXZwaXVKmPq1fovfH7t1qw3UUFurbWBxykmNcmEdUM6x6YzTF934bvsQSb5y4sYgOgkKwZXaX21-37rHaca-hJYRLTHVQdXrvfR6-0CXA3fxxK20dYRUlxdP5-l409gS_KB5cjjWS5_nVEEXK_nBU26Wj-qeiR7VaNOexjtjyDaJ1pPCh_jDFjsd5b3gI0-ZiAixsP8w2sNncCQAfooy4ZKWpACzuo_ukZpomUHatFeTwtd0OrfclOUj7FDImFGrmh_VuE7f0J2P3aJMckfyYrWJcaYWYQQ2l70rP2y9p04B_seiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b73b9b3bf6.mp4?token=hTJZZF4jDdPqnejAdia2irun5lxZTIFdF5gLISXZwaXVKmPq1fovfH7t1qw3UUFurbWBxykmNcmEdUM6x6YzTF934bvsQSb5y4sYgOgkKwZXaX21-37rHaca-hJYRLTHVQdXrvfR6-0CXA3fxxK20dYRUlxdP5-l409gS_KB5cjjWS5_nVEEXK_nBU26Wj-qeiR7VaNOexjtjyDaJ1pPCh_jDFjsd5b3gI0-ZiAixsP8w2sNncCQAfooy4ZKWpACzuo_ukZpomUHatFeTwtd0OrfclOUj7FDImFGrmh_VuE7f0J2P3aJMckfyYrWJcaYWYQQ2l70rP2y9p04B_seiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
گل دوم پرسپولیس به استقلال خوزستان توسط علی علیپور 20
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104167" target="_blank">📅 19:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104166">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtXk5qmdpMTYlWnhVldEIhqsnn2WWYwFzeNilih8R3CdthqE_hV0tyRiieaQ2jK6gBMjBD6mqEnkrIOiF-COkdUDj88PXGsOipPFx555wV-_ZsKQqJ0cFDEhCUjvtGIoow3TBGn7ojtFSBCd4KUJOsSjDfn2CZ3jbdixLAf1f0jnIFEqQLjkd6mQb0ABZbZ3dd9tXH2RBWFVwa-V-D9wKwnd2yg0ihEBiERnrXONvfOCg6zPLh6twB5KoLaMPf85MxOelivUy4vi4VPTMw77olKVZiEDjeE-Hu9HEscFu0ASX250cCMV4lIhPkYqRJvj2B6Ca-7VH31yKDrnDEMqLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
جرارد رومرو:
لائوتارو گزینه ای که بارسا انتخاب کرده و تا پایان نقل انتقالات برای جذبش تلاش میکنه
✅
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104166" target="_blank">📅 19:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104165">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6842cf509a.mp4?token=Cje-vgDOe3W-Xq1e8eNi5IjxoG0HTx4XBmJFTAIJWncat82m--U-UVl8RY7amius7_P2h2kPEUjZJJArbmmAYlnt0NvjGkFWiKCuDOnO9E9VyQWLqrs86nybVPXiRacue22cckUKHojMJxegEJD_R8RYOV0LoMEaGEKE_5eC5OyaXLOB75cjCCWgDClCDwG_38KYDIsc8beHD-KSQJwH1GNUAbIaAUFa5yZUGNs1clHLBg34i8oNC89IMhTBHsP-U12MK0cRYUkSrEHLySN1ZvD4i9yxHh4l1oTd2UHkI9UMz_mIq3BoGe7z8Nwu0k1uOrRKpfQaeXYekOSrqTRnoUnmkp4TkEmaPwMhPLuUyzbD8h-_uQbKtTCMZmqNDh8YFqAf86VJ29oJZV_H8L-7DvJSrlnQyjhuMovy62kTVg1Zy63MN5uHThxcgCn8NMH6ElyOqZiDQuSsQHGmYOEqVeOoO8p5jRAUYKVESHfpUFMXZKHQD041tEh2USUZ0Wh_hi-2hP7OArdm2uE5NN4muTmPLLsdBVqiTOPElrhaUhwtJKi0dnFX0LaOFM06NC5O2ZLErCs1Y6ZwOkaeEflwR9h9v9BBLg1h1L_mbWOw8Wg83LpzQuCndXQurYNApXrFDQ5nTD3vLzdwcHJyelxdM24-ROZLoJK0n2OWIXmiQ74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6842cf509a.mp4?token=Cje-vgDOe3W-Xq1e8eNi5IjxoG0HTx4XBmJFTAIJWncat82m--U-UVl8RY7amius7_P2h2kPEUjZJJArbmmAYlnt0NvjGkFWiKCuDOnO9E9VyQWLqrs86nybVPXiRacue22cckUKHojMJxegEJD_R8RYOV0LoMEaGEKE_5eC5OyaXLOB75cjCCWgDClCDwG_38KYDIsc8beHD-KSQJwH1GNUAbIaAUFa5yZUGNs1clHLBg34i8oNC89IMhTBHsP-U12MK0cRYUkSrEHLySN1ZvD4i9yxHh4l1oTd2UHkI9UMz_mIq3BoGe7z8Nwu0k1uOrRKpfQaeXYekOSrqTRnoUnmkp4TkEmaPwMhPLuUyzbD8h-_uQbKtTCMZmqNDh8YFqAf86VJ29oJZV_H8L-7DvJSrlnQyjhuMovy62kTVg1Zy63MN5uHThxcgCn8NMH6ElyOqZiDQuSsQHGmYOEqVeOoO8p5jRAUYKVESHfpUFMXZKHQD041tEh2USUZ0Wh_hi-2hP7OArdm2uE5NN4muTmPLLsdBVqiTOPElrhaUhwtJKi0dnFX0LaOFM06NC5O2ZLErCs1Y6ZwOkaeEflwR9h9v9BBLg1h1L_mbWOw8Wg83LpzQuCndXQurYNApXrFDQ5nTD3vLzdwcHJyelxdM24-ROZLoJK0n2OWIXmiQ74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
گل اول پرسپولیس توسط خدابنده‌لو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104165" target="_blank">📅 19:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104164">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
رومانو خبر جدیدی راجب آلوارز نذاشته و اخبار منتشر شده دقایق اخیر فیکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104164" target="_blank">📅 19:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104161">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e03b3c710.mp4?token=aLHydTjihNiJPXRTciyymVvtDSAci2TqzIzkGi3IkON2vQk_IZhuG9CIdGWXzDuqUog5_gxmhsKUj3x-sQVLNNqc8lvDL19oPiGyYn-aLML6Yhwz_3BzEUHQFWy-JqfBrC4Oaej6N4kVpMksH--71VwN6ROeydb_imlD23n8obvb3KCxlFax4l0ZnG_DJGXC1naOhwOeQp_Xs_cfeInK1gUfQT-5QhAA_JArgiyzYdi2joSwritoNhTr8-Kgdok73k_1XoSOtP9DC9Ne8_0Je2q06ycD6Km5sHAiHKOH_9ZLiKU7RTwyw93ciZi7XFsiG_Ca8_fzn4z0mvHuqS1wvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e03b3c710.mp4?token=aLHydTjihNiJPXRTciyymVvtDSAci2TqzIzkGi3IkON2vQk_IZhuG9CIdGWXzDuqUog5_gxmhsKUj3x-sQVLNNqc8lvDL19oPiGyYn-aLML6Yhwz_3BzEUHQFWy-JqfBrC4Oaej6N4kVpMksH--71VwN6ROeydb_imlD23n8obvb3KCxlFax4l0ZnG_DJGXC1naOhwOeQp_Xs_cfeInK1gUfQT-5QhAA_JArgiyzYdi2joSwritoNhTr8-Kgdok73k_1XoSOtP9DC9Ne8_0Je2q06ycD6Km5sHAiHKOH_9ZLiKU7RTwyw93ciZi7XFsiG_Ca8_fzn4z0mvHuqS1wvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
تیجانی ریندرز، هافبک 28 ساله منچستر سیتی با قراردادی به ارزش 61 میلیون یورو به القادسیه عربستان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104161" target="_blank">📅 18:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104160">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUkBL4LABJy9wJRpb2G9LqjtQIu1RtZhJA8lOCP3jcJQbUfNwOe_7yFyWwxow7Jbd_rnK1t8dT7jDdiInVSZ4a4OMsWtcR80mQytcftDtWnsW3zqz_HATynf29LwAWMH1edz-qit678iizdeKvesgfptk-5TQEBuLin-bmWN4yxS_i3ljMssF4NJ-z_aUDoyoAqOATI-wuMqktBQc9lnG_39rIWwXjJerqlrYUkehn3qD6wF-_uoZ8wvQFuhQwlhKdtUHlnVMlys9WTjuFnaDpCidWXdbv5Ng48KBEcQwvoMsysMYtSKMRdA2vD3baqjArZt4j7xEy-ZZ85Dz2XBiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
✅
شماتیک ترکیب امروز پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104160" target="_blank">📅 18:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104159">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5pMCg-jXVPJM24L8Zdl1o7JrtvoWkcQU07xEKZaj4uw4OOzqZiuzAG4zPbWwNkYeoaR_B6yaXD-PHEWPHhxIngnmbfLwgpHxHtPa5UI9UDfhvReYW7f1QmcbgDeWbhin4fiuQUOu8y_CQGR32jz58BVRBv0HGxBnETWS6b6m1Ji1WCTXBqTwLNF-IfviFbaaeoQQoVMrDfSMWUJZgFhSkIxXM3oIfUzAld7Von2ufmMIf3rbv1cMDJVffL9xT8uWhGkJ8O5N3skL2pnZf5Kh25KDz43VVzjJS_gmEfDWI2M7hQx6VVJ01Fug6gD2c_D5-IdElwoEOMeRsvBsDP-MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🇮🇷
🇮🇷
لیست بازیکنان اصلی و ذخیره پرسپولیس و استقلال خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104159" target="_blank">📅 18:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104158">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d63f7a79.mp4?token=YFRMYE39Y1JMh8XmNeFEi_HTC_BHBoCEifkD6f8qu3XeUwYVig1XcJNVFCgXuxz5hzZWXTZ_8hDiaCdNlCZWRPYpidK7XiButkOctLnJVR2my4jWtqCOzpN6h6gjTtlXwdZi46fterazrLzjxtR04EQH_a8CHCH5uLU6c3_iygfgJXvQC_J3dV11T7pbw100rvmAEV_fvD6AtToiAOY4lF28dlXJljrCEamW--WVc6EqB15jzJtgNh1-Dw_ccLTQqnd6OcwbyAZkMJnLtz31tdRDtkOBVs30z6UVfMrrMT0PSht7Va29GEcMCNOsAX6Wc1U2gNcDrxMkoiJsWs8HYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d63f7a79.mp4?token=YFRMYE39Y1JMh8XmNeFEi_HTC_BHBoCEifkD6f8qu3XeUwYVig1XcJNVFCgXuxz5hzZWXTZ_8hDiaCdNlCZWRPYpidK7XiButkOctLnJVR2my4jWtqCOzpN6h6gjTtlXwdZi46fterazrLzjxtR04EQH_a8CHCH5uLU6c3_iygfgJXvQC_J3dV11T7pbw100rvmAEV_fvD6AtToiAOY4lF28dlXJljrCEamW--WVc6EqB15jzJtgNh1-Dw_ccLTQqnd6OcwbyAZkMJnLtz31tdRDtkOBVs30z6UVfMrrMT0PSht7Va29GEcMCNOsAX6Wc1U2gNcDrxMkoiJsWs8HYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
🇮🇷
بانوی هوادار پرسپولیس: یاغی خوبی گیرمون اومد، استقلالیا قدر جلالی رو ندونستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104158" target="_blank">📅 18:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104157">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-PpH8g-e9H0nTPha-0yW9zedjjBpVSB2tSWair8AubpoUWgWLwjcapLv02LTljv9uBWDBsnLwuf2Liuw6Q0Lqu_2Jusd98-YXKXv3kV3oV5khKCtO78woia8MbA3XDKgSh5HbZ291GXGyNa0dIAe6EKvcaJE-iiHU3jjHTJpan0EgssDrsCO8X-BSjlsktyhvZSOO5HfMva-2eHlGSXh8_suZuxiq7AYW0MAvXjxxzPtR-WKQrdJ4ayLvrqggUhPGxZhFfo_8Mn9rz-7_1twd9t89g4myzICxyE_4nlmio0KLUR79dzw_n6mabiA_rbrx8-3ACa3tMWa3dMowSgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
روزنامه‌اسپورت: منچستریونایتد پیشنهاد ۴۰ میلیون یورویی برای جذب گاوی به بارسلونا ارسال کرده که هم باشگاه و هم بازیکن این پیشنهاد رو فورا رد کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104157" target="_blank">📅 18:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104156">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d137678386.mp4?token=W3QkPL8_CvP0SGMvSZNeMjAv4sEEyMPsohPIASR7YsfJ9DfapUijW6egVrAMYSxdTJ-_JH46rbOwhtCuDS9VwScmEtQfh6aUQAFdDwHeNRERzm3MudeWn0EA1DXijfCw3HdG1cvfJXO--JahCqLVt17-RGckZBCMKD0u0_oLFthw7jfYb8jHTWN7nqLiIE_7H0ZfSbChANleOlSEPZyTaPBbpUdGZqv2E7DYD_ct437P3e8U0fWPGo5--pIq8850u3MXwJw7j1uWhU2I6cs6XAWWvTRwKIuMhXHlDI54i9yyWUw1FgngSWoKZ6s-1JfPlqdFI88qv6E7OF9jWgMfwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d137678386.mp4?token=W3QkPL8_CvP0SGMvSZNeMjAv4sEEyMPsohPIASR7YsfJ9DfapUijW6egVrAMYSxdTJ-_JH46rbOwhtCuDS9VwScmEtQfh6aUQAFdDwHeNRERzm3MudeWn0EA1DXijfCw3HdG1cvfJXO--JahCqLVt17-RGckZBCMKD0u0_oLFthw7jfYb8jHTWN7nqLiIE_7H0ZfSbChANleOlSEPZyTaPBbpUdGZqv2E7DYD_ct437P3e8U0fWPGo5--pIq8850u3MXwJw7j1uWhU2I6cs6XAWWvTRwKIuMhXHlDI54i9yyWUw1FgngSWoKZ6s-1JfPlqdFI88qv6E7OF9jWgMfwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
هوادار پرسپولیس: تیمی که ۷ گل خورده و دسته سه رفته، به ما نمی‌خوره! فینال آسیا واقعی رو ما دیدیم. استقلال بره آسیا ۷ تا بخوره، خوشحال میشیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104156" target="_blank">📅 18:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104155">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxjIxIewqys96OXftZ7TtAWPHcFZOY7ahT70ljH_egx6JhQILDd-yiccUW9PnL26Zqa5pwCDsifTGfVoRLJihNrkj-gcCOWZEft4wHMLweN8PBG_zmg0b1NFZI2XotNoM4bnSEKzqEaCeB4MkwSPPp0lO8xUds3HoGr6I-5btTYR2VaC6EjfsjdDRV1ViuWJTaXl203JNIMrZ_KQSuvKNTriG0YhVDb7C-5eriAyQt3dMoyjkw9dLyIFx_5yr2KzxAiknoZ7uBkRk0MSDyk-Vfp1m4VJDo4scaGWKuIfDZx6LhcJGxCLzWi2Ri-L1gc9SOCcbKFbX-XCS1VDMcRvtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
بارسلونا بزودی با عقد قراردادی لیواکوویچ سنگربان تیم‌ملی کرواسی رو جذب میکنه و یک فصل قرضی به تیم دیگه‌ای میده تا از تابستان ۲۰۲۷ جانشین شزنی در کاتالان‌ها بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/104155" target="_blank">📅 18:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104154">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NitVS53nRMdOdM4BKUIgEIE0H8DglZ5sDVQtuRsgOZJCESozZA-NZifz5wpTWEFd8AzVQTDWse-2Ud6JXHGag2ABCt5kG73OH2FcOsYuupUi6oFnLt-_Uul9FbYX-VtPHYci0tqJ17IpO3Gys9KmRs4NgOoWmJsHxJLqTZTFbZ02pTt4NbQCB-DjBsy2nK8_mhGwr3wdEt30EuGlLTqBhnmaGPRWxkJdgG0WkZAL0cAuo2X_ndDZiWMRD18QMd10Bf_MtEiBS97c7WRk8G6Hlmfe-ZGuXAgnbGfI0D5WWp3E_dYX7KT02d86gej8OgUaIJsm82CkJMclRYOgfkhC7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
خولیان آلوارز باید یه سالی بره تراپی تا به وضعیت نرمال برگرده
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104154" target="_blank">📅 18:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104153">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPVMfu9weTxBB4a84gtxwO_hA5zk9gozyWBWBKZHXlnGVAGrr2KDNV31qq2PTLYrRtS0UDpIVdEI94kuiabY-2chl4LQsZhsunI1IdSq8OE_sX2Abj4xp8oCtF4_9cTQG7yswBKlg6-Nlf8vuI4lxcsw7jxj-ia0nds5-buwh2mxkvf70J4tosC6r6YgUjFBq1Q0GcrX_JvWFLc8rPH_h747wb4DJHS-cwc9NuWHETKNYXUcaFchW6OghGLYjs24zodkkzAkJGp-QuGO_sTGJ7CS7dPYiSxKu3Aet5zYxSkcbMKNVBJu4dYaM5JcorQFXysx15fb-ZvhVINNLRVdXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
هری‌کین ستاره تیم‌فوتبال بایرن‌مونیخ جایزه کفش‌طلای فصل‌گذشته اروپا رو دریافت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104153" target="_blank">📅 18:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104152">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82988d8dce.mp4?token=ON-nKQ-2xa92jK0J7m___dvEGSWuS3Q672cfOfZlman-LJ0kL_OFDzaQ2iYDy3__m4c3fUCOwulZotwJyEMPoUN22tk6o1b3qmGAAIn7-rrJKGzUfi2l04c4ILWtMwT-QMBEPe5cxMhJlXRK_qX6Aq-w58VvGftzdPFKxRVgtQxMKCht7XOjUeTcR2mA10jspEbDQot777ByAlZEAxhA-LMDLfSo96J2xfdopNHLmI4TgMgqJYj9wdR9n22u1VoFQ8igrXRq08PwFSSkri7Ao3A58-3Isd-KRYfR8GrbJiJ8CRROvnqocvtqsfCAGaCWRgUgVKkodLHFZMUWP36mDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82988d8dce.mp4?token=ON-nKQ-2xa92jK0J7m___dvEGSWuS3Q672cfOfZlman-LJ0kL_OFDzaQ2iYDy3__m4c3fUCOwulZotwJyEMPoUN22tk6o1b3qmGAAIn7-rrJKGzUfi2l04c4ILWtMwT-QMBEPe5cxMhJlXRK_qX6Aq-w58VvGftzdPFKxRVgtQxMKCht7XOjUeTcR2mA10jspEbDQot777ByAlZEAxhA-LMDLfSo96J2xfdopNHLmI4TgMgqJYj9wdR9n22u1VoFQ8igrXRq08PwFSSkri7Ao3A58-3Isd-KRYfR8GrbJiJ8CRROvnqocvtqsfCAGaCWRgUgVKkodLHFZMUWP36mDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🇮🇷
کری خوانی جنجالی هواداران پرسپولیس برای تراکتور
: همون تیمی که 10 سال اومده لیگ؟! به خدا کری با آنها نداریم. ما برابر بایرن مونیخ هم برای برد رفتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104152" target="_blank">📅 18:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104151">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e37442fd.mp4?token=Fj8rv0Zuk8Eu_XcirF0cgtgSRymKvlR9iNz-OaoJTXEhO2yQEFYE9ft-zMk-_vY2lZomEEKJ38q15pkKnwQsit06cNS7NsflspO_1WY28OCD_Xx7INDoCg_ip5dTz0ekzg_1EEXkUky_XWH2YGwaTdz6lost4bDTqDGcq1dr0GDGkqP_Ao7bjOncfWg07RSvsQpI9O92cuC5QtnSURqBsfphh21zdr1k0ooQ0lu__YrJEvNNiX_MBTQ01c-zSmeSkIa4QNzmmiP_3DZyPlXhBLjjBria3Fek8YKRwW5Dc-DC8gux5OidZ6mAIHJOgU_LAEqxRJ1IyTwIE9TIOsQCdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e37442fd.mp4?token=Fj8rv0Zuk8Eu_XcirF0cgtgSRymKvlR9iNz-OaoJTXEhO2yQEFYE9ft-zMk-_vY2lZomEEKJ38q15pkKnwQsit06cNS7NsflspO_1WY28OCD_Xx7INDoCg_ip5dTz0ekzg_1EEXkUky_XWH2YGwaTdz6lost4bDTqDGcq1dr0GDGkqP_Ao7bjOncfWg07RSvsQpI9O92cuC5QtnSURqBsfphh21zdr1k0ooQ0lu__YrJEvNNiX_MBTQ01c-zSmeSkIa4QNzmmiP_3DZyPlXhBLjjBria3Fek8YKRwW5Dc-DC8gux5OidZ6mAIHJOgU_LAEqxRJ1IyTwIE9TIOsQCdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇩🇪
جمال موسیالا: یک اختلال عصبی دارم و اتفاقی که در دوبازی اخیر برام رخ داده کاملا طبیعیه. امیدوارم هرچه سریعتر بهبود پیدا کنم و‌ نگرانی خاصی وجود نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/104151" target="_blank">📅 18:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104150">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">💎
برداشت بدون محدودیت داره حتی ۱۰ میلیارد تومان هم برنده بشی بدون دردسر برداشت میکنی.
✅
🎁
برای مبالغ بالا ۱۰۰۰۰ دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ ۱۰۰۰ دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104150" target="_blank">📅 18:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104149">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari (3).apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/104149" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر WEPARI
😀
😃
😄
😁
🔥
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 120% اولین واریز
‼️
🔥
بونوس برای 4 واریز اول
‼️
⚽️
بونوس ورزشی هر دوشنبه و چهار شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🔥
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
📌
آموزش نصب برای IOS
g28
✔
https://t.me/WePariFarsi</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/104149" target="_blank">📅 18:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104148">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13852c35e9.mp4?token=b0rRGdhOGxD-GrZ4ZRkfsLiJI30L6Csp6-4amptjJsphqDZE0e86ifQ7hvhkrznWvds2WEr0GHvLQ96v5IzcI_9ANns2Azq65zTEm40_0mHSSgOAWpgvy2VqtIWdBb_aj5Df7a4iCXwKtqWxworPStKW2-CyVPVg1_EFuptzjKfcyUeY1R_qAuib1bBbT2hI8Yt-1N493ZCnmQZ4epRmsLjuBWS5GioqCbacrBI4OVzMMdlvZQXCfhMP0qrMRLSq-6Uu-A8e0cQ3i65SyVvjncbBgOSSRIQu75GTdLoqcL8Y_q9joK4gSC9-8wO6-aZ-trngcNXpK1e8YglyfAdrNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13852c35e9.mp4?token=b0rRGdhOGxD-GrZ4ZRkfsLiJI30L6Csp6-4amptjJsphqDZE0e86ifQ7hvhkrznWvds2WEr0GHvLQ96v5IzcI_9ANns2Azq65zTEm40_0mHSSgOAWpgvy2VqtIWdBb_aj5Df7a4iCXwKtqWxworPStKW2-CyVPVg1_EFuptzjKfcyUeY1R_qAuib1bBbT2hI8Yt-1N493ZCnmQZ4epRmsLjuBWS5GioqCbacrBI4OVzMMdlvZQXCfhMP0qrMRLSq-6Uu-A8e0cQ3i65SyVvjncbBgOSSRIQu75GTdLoqcL8Y_q9joK4gSC9-8wO6-aZ-trngcNXpK1e8YglyfAdrNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جی-جی اوکوچا در پاسخ به سوال مسی یا رونالدو: "رونالدو یه بازیکن خاصه. اما برای من، اون فقط یه گلزنه. اون یه گلزنه؛ درست مثل هالند."
👀
"مسی تو یه سیاره دیگه‌ست. مسی اصلاً به دنیا اومده که فوتبال بازی کنه. فکر کنم مسی اگه فوتبال بازی نکنه مریض میشه! اون یه نابغه‌ست."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104148" target="_blank">📅 17:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104147">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bc9togHwIrbxzTIKLzilHhR7ip_Uat7eMHJGpnCXsklVlSpf4xIU7DiNEnx_VOlzH80DA8TfpfDruapjQFHIc1Cm1OHfnC5jFl3saswgPYGGch55BkSApmVHopE4OVJrWBN29O8ZCz0dMLbUSgDjz5jwfYHcwhsvY5y3UxUoOahrY14e6q_dZYlvipIb6-qwSDoC09Lpev_y7-IKGaWPH3iIqkorR7HPnjkZ9rvDoJfd4KhtZD_8deb5iIT-BCSTP921gvS9Ei6SNndcJDeFWRxS05ywNDwroWlodhY9v3oEHkN0GV8MTBw62wv3oa_8YapvA-1ZC_ER0Hnu0o4ibw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
جرارد رومرو: بعد منتفی شدن خولیان آلوارز، بارسلونا به صورت جدی درحال بررسی گزینه خرید نیکولو تریسولدی مهاجم نوک کلوب بروژ بلژیک هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104147" target="_blank">📅 17:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104146">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9md1BO7oj821FAFi3oiBCtlesV2umwAGJSiX5jnu80yLP4ukvQrnE76u8ySfOfTZEx9wX8RLsl2nUPzOTPGe7tpPDsW8beFmeP5gRatLPQoGmyN5NR-8QyFurwVF6LWJSTbiMW5o8GXszC69pVR1vXFXxMLaFvFfoFqP9yTgzWiXP_v5zT7h-619xavaeThoxnKPc7lbGsPgq1lA6W6iyaD_ZKw85TbkrdFwo_mRQaah4TLGaxL8Ky2FIqGz5lS_6EI9IuUltYT1XIhNEhseC3ZqVUVGeOwHJiIhYmSj1rmu4qwZCp-sJjI4HmescnXllJSAylcJdcEswEOGbMeig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از دیوید اورنشتین: دو باشگاه آرسنال و استون‌ویلا برای کونسا به توافق ۵۰ میلیون یورویی رسیدن و بزودی تست‌های‌پزشکی خرید جدید آرسنال انجام میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104146" target="_blank">📅 17:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104145">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ue9Gz4AMwof3RO6IMvMywP3SK17InHei8XE0n5LcNZOlrssA48Z6d8l8vK4HB7nNHvsw5Q5JuMKE2c3nVql3Idq-lIH2OUnzV3w99K_no0FlZf2OmjNfJrSewkvu2X2sp9tvpnR-rpo6-FeBbBl5kUagdCKwQUSeVs1u0dsoBTwdgt-GZhvHoP8JglEJGGRTwcBdtsty8HIo1pdfT0sFPcGy8ohHW137OztpPH0t6s_pZ0mElqH2wfCwRhbpqvat_iDHn2NuqlsXZ3M0riNhbQFssVUdUDww5xKbaLB8wFUHLZyeJwNS3pZXeHV9Qh_OWcrBMQqTk5QUzG3K7N-TnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از دیوید اورنشتین: دو باشگاه آرسنال و استون‌ویلا برای کونسا به توافق ۵۰ میلیون یورویی رسیدن و بزودی تست‌های‌پزشکی خرید جدید آرسنال انجام میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104145" target="_blank">📅 17:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104144">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇪🇸
انریکه سرز‌و (رئیس اتلتیکو مادرید):
«نمی‌دانم خولیان عذرخواهی خواهد کرد یا نه، اما فقط با دو بازی می‌تواند دوباره دل هواداران را به دست بیاورد. ما از همان ابتدا به بارسلونا گفتیم که می‌خواهیم خولیان را حفظ کنیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/104144" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104143">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0844b0d9d0.mp4?token=fQvDwUQfLwfC_gxKT9mcRhsVPst7ZoIj4JVZ--O1WaZ4wvJPQqMDsJTNhIR25uDLQDhgkTCD7S9Q1YNi4kDfliAPExZR8DYPaqhcxD4AY8XwuT8D08nzUW5c01GlU_Jc2L8ybEkNS6XOTO_VkE_OFQC2j_YFCwgnh6Uz8ItFe2cNdIZJm-d75N6KosTjC9B2Hx_7ySKGWCXFzDYVEiYPFKtC7Vf3uxG4SMWsc1A-6D_-bMkiQO0hNb0rHUYfRECQhhZ2kBq5tDE80AzwbrAoZwyRYooRT8tEjDUQudKwZJdwfQ_fB5t1lHOa-HDrc3pdBGvwpp8RP3RnQwCiYu-HWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0844b0d9d0.mp4?token=fQvDwUQfLwfC_gxKT9mcRhsVPst7ZoIj4JVZ--O1WaZ4wvJPQqMDsJTNhIR25uDLQDhgkTCD7S9Q1YNi4kDfliAPExZR8DYPaqhcxD4AY8XwuT8D08nzUW5c01GlU_Jc2L8ybEkNS6XOTO_VkE_OFQC2j_YFCwgnh6Uz8ItFe2cNdIZJm-d75N6KosTjC9B2Hx_7ySKGWCXFzDYVEiYPFKtC7Vf3uxG4SMWsc1A-6D_-bMkiQO0hNb0rHUYfRECQhhZ2kBq5tDE80AzwbrAoZwyRYooRT8tEjDUQudKwZJdwfQ_fB5t1lHOa-HDrc3pdBGvwpp8RP3RnQwCiYu-HWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇪🇸
مراسم معارفه رسمی ژوزه مورینیو به‌عنوان سرمربی جدید رئال مادرید برگزار شد؛ بازگشتی که خودش آن را «بازگشت به خانه» توصیف کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/104143" target="_blank">📅 16:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104142">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ad88532c.mp4?token=nFNXIT3cP82XYCL4ENpzp3NYOp1cn5eTNq8ioImxhEPQdsiCFKBe3OIHKNOB2EDfRuCS107Xcn_zfgsq4dk2ecRxpOQhrhZbomxswKB_4Egw9W4kXZByR_n2pyF0ZM1XQdjb6rEepcKnJdL_Q_gz-5x_QOD26t5rgB1D02V0ODlitzp7jg691mJGeHYgf0ja88bnNujUu7B9vq347ouJSSK7QI_xQCumvL5q0tQM0OCq3QYh7URULFXSKxvm2tF0DmUAnzhkKaczr8Mx57MzOUFB6FxFkasXWEbYaehwgITu4Vw4DSH6jVxKKkkXrn1rOCp8jgYUpeDu-KywkAZRig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ad88532c.mp4?token=nFNXIT3cP82XYCL4ENpzp3NYOp1cn5eTNq8ioImxhEPQdsiCFKBe3OIHKNOB2EDfRuCS107Xcn_zfgsq4dk2ecRxpOQhrhZbomxswKB_4Egw9W4kXZByR_n2pyF0ZM1XQdjb6rEepcKnJdL_Q_gz-5x_QOD26t5rgB1D02V0ODlitzp7jg691mJGeHYgf0ja88bnNujUu7B9vq347ouJSSK7QI_xQCumvL5q0tQM0OCq3QYh7URULFXSKxvm2tF0DmUAnzhkKaczr8Mx57MzOUFB6FxFkasXWEbYaehwgITu4Vw4DSH6jVxKKkkXrn1rOCp8jgYUpeDu-KywkAZRig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
شعار «وقتی بقیه خوابن تمرین کن» احتمالاً بزرگ‌ترین اشتباهی است که به ورزشکاران آموزش داده شده!
✔️
علم روز پزشکی ورزشی ثابت کرده که خواب، مؤثرترین و در عین حال قانونی‌ترین دوپینگ جهان است. اگر خواب باکیفیت نداشته باشید، سخت‌ترین تمرینات و گران‌ترین مکمل‌ها هم نمی‌توانند جلوی افت عملکرد یا آسیب‌دیدگی شما را بگیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104142" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104141">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e19dd4c082.mp4?token=JJtcnvXKp3w6kJcnmajuR4J9aGwoSLdceZfZXBQuq4YTQWhZFJ_ow5z8JY4eVywxU_0MGbGdNifH8aEV1J2BkiOhSQLpdjn76JUkVQHbA7SkotSXMroX6cw37e3cu46xcdF2oeN1buyC4r8afz_31Ny8YgFgAAeOh8bV7FKCok4Fn9FzdqxJie-WhnCy0rTmASuFmyVuDR-9IFhTK1xhhVun2H0h8KLKJc6ossT4TirUt5mLxJf1rXqiHVtvbA0oZ0fGyqEeDfSsnv1yVH6cUVZ5x5jhcZl8YtKFNg2NgGO8e-g3Kni7DD4r70ZD1YFou8LPPsiUfP3xN0Zf_UKNxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e19dd4c082.mp4?token=JJtcnvXKp3w6kJcnmajuR4J9aGwoSLdceZfZXBQuq4YTQWhZFJ_ow5z8JY4eVywxU_0MGbGdNifH8aEV1J2BkiOhSQLpdjn76JUkVQHbA7SkotSXMroX6cw37e3cu46xcdF2oeN1buyC4r8afz_31Ny8YgFgAAeOh8bV7FKCok4Fn9FzdqxJie-WhnCy0rTmASuFmyVuDR-9IFhTK1xhhVun2H0h8KLKJc6ossT4TirUt5mLxJf1rXqiHVtvbA0oZ0fGyqEeDfSsnv1yVH6cUVZ5x5jhcZl8YtKFNg2NgGO8e-g3Kni7DD4r70ZD1YFou8LPPsiUfP3xN0Zf_UKNxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
‼️
🎙
رحمتی: کیفیت بازی‌ها در کشور ما مهم نیست؛ مهم نیست کشته می‌دهد یا جانباز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104141" target="_blank">📅 16:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104140">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b52b455aa.mp4?token=VOxcJBUCyrXI3XXzCqsazeFvkKDuMO-_n0LCYu9xBKWHv4DXvwe6W0s9fBEwBech7c0JI5GNg4A8o9aFb4eIBwxLprzDTAIAOAdVMHXqXM-NABeOllkvr2w2yO4mk8dLQw-mttYZgDC4bg8X2uTqhuq1OqyfI8P1ojVVseFmCQIukeOnKEYBsSawNP4VDCRcT5dSrbPHaz9Ef5ob5dGCKMUiwVV8vxbc9vLsOq7xcQGGNUgW415QCiWkq3KTp9iGM8SxGb7cAh8rI09EtBbWYZzSJJ-p6iIfF6DKaQN9bLKpBOo1UX7AKGvTakyjeLMR-KGTMY6JmQLJOCBuRp6G7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b52b455aa.mp4?token=VOxcJBUCyrXI3XXzCqsazeFvkKDuMO-_n0LCYu9xBKWHv4DXvwe6W0s9fBEwBech7c0JI5GNg4A8o9aFb4eIBwxLprzDTAIAOAdVMHXqXM-NABeOllkvr2w2yO4mk8dLQw-mttYZgDC4bg8X2uTqhuq1OqyfI8P1ojVVseFmCQIukeOnKEYBsSawNP4VDCRcT5dSrbPHaz9Ef5ob5dGCKMUiwVV8vxbc9vLsOq7xcQGGNUgW415QCiWkq3KTp9iGM8SxGb7cAh8rI09EtBbWYZzSJJ-p6iIfF6DKaQN9bLKpBOo1UX7AKGvTakyjeLMR-KGTMY6JmQLJOCBuRp6G7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
واکنش شجاع به خوشحالی جنجالی بعد از گل دوم تراکتور: طبیعیه؛ خیلی خوشحال می‌شم اینطوری می‌شه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104140" target="_blank">📅 15:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104139">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e36fbbeae0.mp4?token=XImNlDao4YnFZN-g_cFhYjyzV84IWqLMOa7aFY1zJc9ZaONljw_H1twc71_tTxcbeGz9cHKCZPBYIItNsba0QAozh6-N_xBfoEubmJ6f9I2RBQy5jSlGFJpJZNNS-pII9iWrvwLQSrT6-PvIb7YvOIvhMJmmi4m-ZybSu4uwozcakj9t0Ij3FAwOnnUKLlMaRI6qQeda6d5j4LmPJmAut0ihB-xFk1Me5FTW-8zQBW_OeRfTWbaokc3yDd4x0QJgApaOnZCV197aswwU5wrwoGPKlbGWtHbnqWW4vHocuXf957_mU5XUJR7J0QfvCF1vVygmKiaZiSDLfnSh9UyjPVRl0s0fNGXOWoYkJ3A4YdyAAtk1wC5IzyzXyC6Axc1kT9Sw5whPXUkO1N96DwohwNMwC8sXp5_wTAUu6Y-ajY0QZx-dqATBh0MoiY9jKCszzGLahgws8jHf9COtGVPcW9lYY0Q5aMLLT6Z0w-xXu46w5KJY6utIsRwXC-1svtudJPX23cX7mzIRgZrViRNhqrl4qpOuAajeKaPeXunp44Bt8HRq31tM1k_qX01LcryK9gJSoPZhnPRro69LqBxnNaL3v5ONHgc_iJ1vejXWLhShQU4nqS6F4fjNqOSX2Br9qzfrX0CIQpuz1vlqjrCX6ODJZ1bRC9ubbPwMAvY9wuk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e36fbbeae0.mp4?token=XImNlDao4YnFZN-g_cFhYjyzV84IWqLMOa7aFY1zJc9ZaONljw_H1twc71_tTxcbeGz9cHKCZPBYIItNsba0QAozh6-N_xBfoEubmJ6f9I2RBQy5jSlGFJpJZNNS-pII9iWrvwLQSrT6-PvIb7YvOIvhMJmmi4m-ZybSu4uwozcakj9t0Ij3FAwOnnUKLlMaRI6qQeda6d5j4LmPJmAut0ihB-xFk1Me5FTW-8zQBW_OeRfTWbaokc3yDd4x0QJgApaOnZCV197aswwU5wrwoGPKlbGWtHbnqWW4vHocuXf957_mU5XUJR7J0QfvCF1vVygmKiaZiSDLfnSh9UyjPVRl0s0fNGXOWoYkJ3A4YdyAAtk1wC5IzyzXyC6Axc1kT9Sw5whPXUkO1N96DwohwNMwC8sXp5_wTAUu6Y-ajY0QZx-dqATBh0MoiY9jKCszzGLahgws8jHf9COtGVPcW9lYY0Q5aMLLT6Z0w-xXu46w5KJY6utIsRwXC-1svtudJPX23cX7mzIRgZrViRNhqrl4qpOuAajeKaPeXunp44Bt8HRq31tM1k_qX01LcryK9gJSoPZhnPRro69LqBxnNaL3v5ONHgc_iJ1vejXWLhShQU4nqS6F4fjNqOSX2Br9qzfrX0CIQpuz1vlqjrCX6ODJZ1bRC9ubbPwMAvY9wuk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😞
وضعیت فوق‌کیری نیکولاس‌زوله ستاره همین چند ماه پیش دورتمند و سابق بایرن‌مونیخ که از فوتبال خداحافظی کرده و اینجوری وزن اضافه کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104139" target="_blank">📅 15:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104138">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0708d4aa6.mp4?token=gpb8QNwzBKtoEgq6-Mqe-7KAwl1qibMipVGIQGJMAaZAI6xInjy358CII9umTBVqcJjKxkLYzfqnKFCkYzEMhl4PdvammfD0SHniODxyaKnQ73Nzb1zkOy0xJ6z3HLXYPFhNntyFw07V5Fvkz7BxmikZISDCQlHN90NUjietp7_U2PVZ8ya5pQhb8YW4H9TbTgLhHMRaYzwZVVjX3Zayc7mIyPtrAiJHKBS3YShCTsJedkV2F5yQzDWEMUo9Fcw11Gt0wQFnsrW_33aKa1BeRSWJrPcdHW4aWH0pwfVZjF_-Sjm-2cFjJsptYmom2hLteeRkhGHZT2sQuGMydOrNbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0708d4aa6.mp4?token=gpb8QNwzBKtoEgq6-Mqe-7KAwl1qibMipVGIQGJMAaZAI6xInjy358CII9umTBVqcJjKxkLYzfqnKFCkYzEMhl4PdvammfD0SHniODxyaKnQ73Nzb1zkOy0xJ6z3HLXYPFhNntyFw07V5Fvkz7BxmikZISDCQlHN90NUjietp7_U2PVZ8ya5pQhb8YW4H9TbTgLhHMRaYzwZVVjX3Zayc7mIyPtrAiJHKBS3YShCTsJedkV2F5yQzDWEMUo9Fcw11Gt0wQFnsrW_33aKa1BeRSWJrPcdHW4aWH0pwfVZjF_-Sjm-2cFjJsptYmom2hLteeRkhGHZT2sQuGMydOrNbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇮🇷
😢
مهدی‌تارتار: بازی مالکانه را از پپ، بازی دفاعی را از سیمئونه یاد میگیرم. ضربات ایستگاهی را از آرتتا و پرس را از کلوپ یاد میگیرم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104138" target="_blank">📅 14:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104137">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f2ef998c3.mp4?token=XwQYbt2t5ersL-1HUJG4pFxiZUy39snw0lgx1GRBy2xdpHjNkhtxD82-VkDM0Zw_LrWW66ZEjdbGcwKjJ0-lFKnOeWWIYosB1Kk5BWXsCaHCyaSAFfWC_PPBf-85LTZ4V0RH3-Y5sXG0fmZy-DT4Pqr-M0obI9z9IISjlmVFONSPLZQOG96WIrSaOLDJ8b7iLv2T7ANgdybcMEYmL7eW11yGqteBylSZC4L7GzQHsWhIoUdPL6WPftzO6U_6AJibXU6EHKD0259Bcn7P5NwtZwDqOrKKVTrpjVqCt09SCwge_pu9nYBisHRO9c_WwWByBnykX7mayCYr7cE8iOuGfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f2ef998c3.mp4?token=XwQYbt2t5ersL-1HUJG4pFxiZUy39snw0lgx1GRBy2xdpHjNkhtxD82-VkDM0Zw_LrWW66ZEjdbGcwKjJ0-lFKnOeWWIYosB1Kk5BWXsCaHCyaSAFfWC_PPBf-85LTZ4V0RH3-Y5sXG0fmZy-DT4Pqr-M0obI9z9IISjlmVFONSPLZQOG96WIrSaOLDJ8b7iLv2T7ANgdybcMEYmL7eW11yGqteBylSZC4L7GzQHsWhIoUdPL6WPftzO6U_6AJibXU6EHKD0259Bcn7P5NwtZwDqOrKKVTrpjVqCt09SCwge_pu9nYBisHRO9c_WwWByBnykX7mayCYr7cE8iOuGfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نمایی دیگر از حرکت جنجالی شجاع خلیل‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/104137" target="_blank">📅 14:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104136">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34bfc2ef34.mp4?token=iB7J2FP1MAFQJAwLHHAl6LdNZFVfIZk9n62jtZKzTUUIn0Fbg38yOPtD32odPe6R-BgBDicF79wWEsCkgL9b79LWF2TJA2KqDUCRpMi5T_eu12xOzHBGTTA77CALjRb42Y57fZcq1l1xSy1a-kpVNtPtV0fH1nDnvBCRxl9CHEFLsDNBcn4LxEERf1QBP8eM-WfGas338ryha5n-e7xthuv0ENcjt3s-z5wXqBd5H4ktvI5zOCXa51dkXib4cI4nmz_9flcN6V1Wc4rHUIZBN8Q-ju-OvGy-ifBj8-Xmq2Zc_tmJQJw507nDgCD8vGe9jq1PPtH-Y5yT8LoH2VHkkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34bfc2ef34.mp4?token=iB7J2FP1MAFQJAwLHHAl6LdNZFVfIZk9n62jtZKzTUUIn0Fbg38yOPtD32odPe6R-BgBDicF79wWEsCkgL9b79LWF2TJA2KqDUCRpMi5T_eu12xOzHBGTTA77CALjRb42Y57fZcq1l1xSy1a-kpVNtPtV0fH1nDnvBCRxl9CHEFLsDNBcn4LxEERf1QBP8eM-WfGas338ryha5n-e7xthuv0ENcjt3s-z5wXqBd5H4ktvI5zOCXa51dkXib4cI4nmz_9flcN6V1Wc4rHUIZBN8Q-ju-OvGy-ifBj8-Xmq2Zc_tmJQJw507nDgCD8vGe9jq1PPtH-Y5yT8LoH2VHkkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ممیزی متهم گریخت، ۲۱ سال پس از اولین پخش  که هم‌اکنون در شبکه آی‌فیلم پخش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/104136" target="_blank">📅 14:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104135">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbee7be849.mp4?token=fyppqXYyCrUCmRohWtnG4M_BpWzZuscKeCb2-nBY-NufOiyXD36a1rN_vg_PVcwGfp81wotvg_7dqueJW1o0Q1oP29g3qKwIJTv3sezIjdZOVOJbzC86fpzsZxPutVnHo9E_Pu--UkESckR_hDb_qqtaRJzEYpM60njwjwq0XkLcnpxGkLJ1pe9tXp7I43KglwS75QiZzIb5WOZz57WX3_VduLKQsJFQO5pCE81TOT3aD-uiCO2yQlqs_7Ab2TK5-uvmizMQ31y8ZVw1SckBGmpS_GNeFCA4O9k8iIuO-F6-h6IiHYopDc5Brx46RVAjqLrxhhSBh8KWs6qS8TLdJmOqWlyM5Mhe8cJh_ja5nRe8INJmUJvb54DMsUZ9QQtjjsyYCqtndWC5ttQwnsFLOiRc03TSWRpevAXVcAvumZwb5P_q-WsdUXd5Ji8afN2knr3Mm5cZl7jyWZIzY-a4vLSRsZ1rxdx49lEkJ9Ai2M-Dwk6B3l73PjrCWTQIQNB2pgadFDG42qYYUhUu9u05DLEiOJHU7LAtSfyxLpfDAjE9qqcv2etQcD26FNLsOUkZ1hx96w_KYHWPkPskyuYFwk1-e_3MsDeo2klJQA7ECVK1-9qveG7HJfdxnIpZflOKLoYVqr4WOpR2HfWOQNQ4pK-8RfKV7nANnUo5OFrp7As" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbee7be849.mp4?token=fyppqXYyCrUCmRohWtnG4M_BpWzZuscKeCb2-nBY-NufOiyXD36a1rN_vg_PVcwGfp81wotvg_7dqueJW1o0Q1oP29g3qKwIJTv3sezIjdZOVOJbzC86fpzsZxPutVnHo9E_Pu--UkESckR_hDb_qqtaRJzEYpM60njwjwq0XkLcnpxGkLJ1pe9tXp7I43KglwS75QiZzIb5WOZz57WX3_VduLKQsJFQO5pCE81TOT3aD-uiCO2yQlqs_7Ab2TK5-uvmizMQ31y8ZVw1SckBGmpS_GNeFCA4O9k8iIuO-F6-h6IiHYopDc5Brx46RVAjqLrxhhSBh8KWs6qS8TLdJmOqWlyM5Mhe8cJh_ja5nRe8INJmUJvb54DMsUZ9QQtjjsyYCqtndWC5ttQwnsFLOiRc03TSWRpevAXVcAvumZwb5P_q-WsdUXd5Ji8afN2knr3Mm5cZl7jyWZIzY-a4vLSRsZ1rxdx49lEkJ9Ai2M-Dwk6B3l73PjrCWTQIQNB2pgadFDG42qYYUhUu9u05DLEiOJHU7LAtSfyxLpfDAjE9qqcv2etQcD26FNLsOUkZ1hx96w_KYHWPkPskyuYFwk1-e_3MsDeo2klJQA7ECVK1-9qveG7HJfdxnIpZflOKLoYVqr4WOpR2HfWOQNQ4pK-8RfKV7nANnUo5OFrp7As" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
اخباری، سرمربی چادرملو: نه تنها از ما عذرخواهی نکردند، تهدید هم شدیم. از این‌که جای تیم ما به آسیا می‌روند از خودشان بدشان نمی‌آید؟ امیدوارم باعث‌و‌بانی شرایط روحی تیم من شب راحت بخوابد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/104135" target="_blank">📅 13:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104133">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJtOwYAVWUuBCMFr0WggwHoKAS2oIRC3idbMpVv3fWvtOi1tUS8_gOt5yFa76NT47KPPeUQ6aGUR_WFY0SB9CTfyFRxlqCc6iaIwb3YR8GlW6UUonsz1qaEZYMnH31kblvOxAVpgApx4Cy1f3HZjmDf-s41vA4T_RRbKqVmPACpZBjmbKztPX8KVblEA7lMCLBu9v2AvEcBtKCb4O7cHtbzwJUgNQAizb2VxcyVQ-fzS2YRAVUsFmPjw0KPhGruWDguTSiDMtJaIzRbpB1kg5V-NrjqYhopKD1U7FYqjFsDVBI2IOeZp3NNEOzgeJuzjlnG8jPZI9b4qE3Qzcjf64Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
استوری جدید رضا علیپور : جنوب لبنان که چیزی نیست تمام دنیا فدای یک وجب از خاک ایران.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/104133" target="_blank">📅 13:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104132">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947d3a1948.mp4?token=UHZqoS-Kwn5vTQnDrYF2o2n4TL69G_Xq91i9KsY6iaSnNBpGSBRluMuVgTh6zTC5CgbstAUnaIBGdRGsNJxFvXg-q0BPdkDScVC4MLGp4jPPPmnpSO6JMBdJgIEa30wO0CIt9tg0X8U5xPpLhuQONfLyT2xtu5Id2DgQz1CN0Lo5B50ixY7mINfevQS4O9BxFvjRWLohCqmhQuj0pU2UlMzkIju7jCFGzeV9M_lgcCskjoeBcCk48ygBHmtEwDgaAOa21IB_nuopD1pa_yczAGqebQAW2U6_fks1BEAdpBAG2X_59oQCEXRKBQekSwvl9pNi_SHW1IGLpvVji-TK3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947d3a1948.mp4?token=UHZqoS-Kwn5vTQnDrYF2o2n4TL69G_Xq91i9KsY6iaSnNBpGSBRluMuVgTh6zTC5CgbstAUnaIBGdRGsNJxFvXg-q0BPdkDScVC4MLGp4jPPPmnpSO6JMBdJgIEa30wO0CIt9tg0X8U5xPpLhuQONfLyT2xtu5Id2DgQz1CN0Lo5B50ixY7mINfevQS4O9BxFvjRWLohCqmhQuj0pU2UlMzkIju7jCFGzeV9M_lgcCskjoeBcCk48ygBHmtEwDgaAOa21IB_nuopD1pa_yczAGqebQAW2U6_fks1BEAdpBAG2X_59oQCEXRKBQekSwvl9pNi_SHW1IGLpvVji-TK3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❗️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تصاویر تازه منتشر شده از صحبت‌های پپ گواردیولا در رختکن منچسترسیتی، پس از باخت ۲ بر ۰ برابر دورتموند در چمپیونزلیگ⁣
پپ: احساس حماقت می‌کنم. می‌دونید قراره چی بشه؟ قراره یه مربی جدید داشته باشید. از این عملکردتون خسته‌ام و احساس تنهایی می‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/104132" target="_blank">📅 13:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104131">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🇮🇷
❌
سرپرست باشگاه نساجی: تا این لحظه مدیریت باشگاه تصمیمی برای شکایت از استقلال بابت بازی دادن به یاسر‌آسانی نگرفته است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/104131" target="_blank">📅 12:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104130">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHQDbgNgIe8n8QGNg-CAJi_IqzZaHPaZ0dGNLaTr5TMIcz3rkpksIi9FWnyhgTJhyYPDZ9mUdtBUVDafSLzFrh2LCg9HGm9cu-YjatgCIIAeAQesA-k1qGHxuLXKSeUtp92mkegGJ1Uzmr8yqvaLTdRpB5gitU66J6uloeaDkb4iBSBtwdWnjsjP8DIymsbnNnfrw1VyB1F6XIjw-e0pT1RA4P3A9xh6gUA4GRu3pUgZIHxiMBTGntpqu51T207I6hwqTGvy1u1Ya0hY8WgYadhlNJ_eb5BgQIptb8-GdbzRWydgqNODHfpXwkIH66SQEXtxluczhMLpXn65XUZ_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتین: یونایتد برای جذب کارلوس بالبا از برایتون با رقم ۶۵ میلیون پوند به توافق نهایی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/104130" target="_blank">📅 12:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104129">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFVJesPc0u1gDGX5NkXO81V_Kc9TZLNdl12fjrGZ7mcQVKoUKHCgyrKcpUntBnby7H6I1sPk7IZedvAvby5VrvR61yYEc2Dqzp5IdVu96pnPKUvpogmqHLyKFkcuqN3tNbr7OxqdXoxP2eF-A9Vcf_J4zTpeuwzdqbtuCT6LUaNmP6ydEpVi1N-NnECb4NpTX5ovhvpk2pbKFqfnvl0S2tu8fpjxnIWNVArboUWqy2EvKcixP6RDYiyaNPLx_wmkNuTVlKjdpcOxbykeaqUQD0pzn4Y3Ga4Ub3EZo041qSsXs_rPKo2TQlHLRIkQq3lCJMw15ao2K3hKAq7fWsJnUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: ژائو پدرو قرارداد خودشو تا سال 2032 با چلسی تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/104129" target="_blank">📅 12:15 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
