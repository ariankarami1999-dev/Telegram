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
<img src="https://cdn4.telesco.pe/file/RWfWfb1S_AxWny7SMXdS8xIzVhAdvqceyAnEkfmKSY_B4lRr16z7cBpoAGWaZL6FMk98EiDsWZaLKs33w7NSNEZKwOruzvmRgU-g3Lkefd3jz6SLYVE0N7tUaNL6JTXfeAmsY9PZAFvQ5vxkTqPj5g6XSx3l0Ev49k-Emk94Jayd_XUBKAtyMRbv3_INgVJ0CQt7AaroT3XYRIWZixdXxDyJ6ZUqE4VHX6zmRerIK80dUdDVXZxar7J2eNex4tedoHVlq_g06wl2tmzjwhG8oeZnvCugfomFxChUWfzr1PTUn_XQnVvnY-rIZQPRBzd1usBsYGYLBCVYXEaBNSLN_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 271K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 00:04:08</div>
<hr>

<div class="tg-post" id="msg-85185">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
‏يوم الأربعاء تمكن هجوم إيراني آخر من اختراق الدفاعات الجوية الأمريكية وضرب مستودع أسلحة بالقرب من القاعدة نفسها التي قُتل فيها ثلاثة جنود أمريكيين في الأردن، مما تسبب في تشكل "سحابة فطرية بعد أن أدى الهجوم إلى انفجار.</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/naya_foriraq/85185" target="_blank">📅 23:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85184">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
تم نقل ما يقرب من عشرة جنود أمريكيين أصيبوا إصابات خطيرة في الهجمات الإيرانية الأخيرة إلى مستشفى عسكري أمريكي في ألمانيا.
هم من بين حوالي 100 جندي أمريكي أصيبوا منذ أوائل شهر يوليو، على الرغم من أن وزارة الدفاع الأمريكية ذكرت أن معظمهم عانوا من إصابات خفيفة في الرأس وقد عادوا بالفعل إلى العمل.</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/naya_foriraq/85184" target="_blank">📅 23:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85183">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1XFOHBkppMyyYzBoYaMunOkpNO2l7L5qNnGBySZ7S4klKdA-kUkOj7LfLpfkuErV2oJWGNUqNI6BNlP5hcj2UYBCmFKcykEfS8ejJRLS4EaDByBmTvO1lNBUDE8c7gXRnQKs_npgAk6083qlSCGsypsNFVsqvZoUdQH_yEdMsDI9nOwYDznA2AnANF0PSvct1E-eozA52JlKcQSTEpIGO3Yq0mPUXxuG3yFoL1-XcJ2xzGZaqiQMOyz76qUVvd3DrO25qc9JaZwc2NHjGqwx5iP5uWQkbMvGyh2UsIb-4PYwK4k_bPk7mw6PimcNEYQOhE7a77GF63c_eklru2ZHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
توثيق من جانب العراقي يضهر محاولات الكويت بالتصدي للصواريخ الايرانية عن طريق اطلاق عشرات صواريخ الباتريوت.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/85183" target="_blank">📅 23:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85182">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الصواريخ الايرانية تنهل ‏على معسكر بيورينغ الاميركي في الكويت</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/85182" target="_blank">📅 23:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85181">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انتشار قوات الخاصة مع قوة مدرعة في مداخل مدينة الصدر شرقي العاصمة بغداد</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/85181" target="_blank">📅 23:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85179">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a99a0a78.mp4?token=qfuu3tYrzec6lU55XszEpWxXiANv__6iVpyDubZZSnyMClfJ5ad8WUwnXKqpUui6Cje-2n_dx16QPskjKTqhCIkXqUXsUT8pBS-05YR-eUU-I5ozFMFLgRXc7u5a0UWhb4sYwPMlIsbr3kQOD79JlADL7U2WSqEOHXBHEqPm9hRGhdLqisEAKGxJFwLrOLS7ESxaVLPu1SeEX28UNeB93yGR5c5JFbahtJwH5vClJIdxJKQbh2taoHeWfCvUzyw-5cQ1rwl_AW69hN37pSNdWHn-B2FqnpkDa__H-6_BcCxKRx8KwRV5saXYiXpc3ke8p4AGBkuOjlbxPn5t_Pe84w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a99a0a78.mp4?token=qfuu3tYrzec6lU55XszEpWxXiANv__6iVpyDubZZSnyMClfJ5ad8WUwnXKqpUui6Cje-2n_dx16QPskjKTqhCIkXqUXsUT8pBS-05YR-eUU-I5ozFMFLgRXc7u5a0UWhb4sYwPMlIsbr3kQOD79JlADL7U2WSqEOHXBHEqPm9hRGhdLqisEAKGxJFwLrOLS7ESxaVLPu1SeEX28UNeB93yGR5c5JFbahtJwH5vClJIdxJKQbh2taoHeWfCvUzyw-5cQ1rwl_AW69hN37pSNdWHn-B2FqnpkDa__H-6_BcCxKRx8KwRV5saXYiXpc3ke8p4AGBkuOjlbxPn5t_Pe84w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار دوي صفارات الانذار داخل الكويت</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/85179" target="_blank">📅 23:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85178">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae28f96254.mp4?token=acX5M-_OrqLkExpwSSW4fjjeO9STF4-1CdzMsvf-Cna60teyeLFXYJTTbhb1fq1kC9K2e9-Nqpf0YacUJJckBMWnH3MPcM5cMNmP6jazbQa3j3qxIp5zycKpNgzO4XEB2fds33Z6wOW4fCIJ-IpwQrI_nSx2xPzRtgWBgJyJD5CojfHtpRIhwqPkCEjI439ieR75gguepBcMY4hBjAZdAaDh2zkQ2Qn3tUsqJf6TKZ_cRR7Cy9R5hCJOt9HojuNzfz5vM-AC1F-uFElKCpMPnkRpef1YrY1nzFcfmBOToOiQdRdg7Q9AElrYUl0aHF3GM46HkVJM0q0H0hxbPTU_GI0wjuSuWrE9sA_NR2S1vk2Cc1Vfott1wrAecD4nHBtuZKchI5DXWS9W_o-HsWg4O_pIxUYcMWao2lPgVN3fNuqDmMjCdnFsonF-PQg5-yLTt0CWwX13yH8fiseOGbndLhHp4_Qf_r1SUIHNi2qPigIEzdX4-FznEB4GdacFgS8GHk3wH7nLfPrLaNoDnXE8FkLWhktQGvlnyzDAhE1LIRIKTi187J-raiI75z1jm37q5-2RomiIPZub75rZ5pVvvPIzeMN7fu04ix2R2P07nlylLwrwbJA9_MVoLPKEcWw0ORYDnTCTGgBrAOwClGeqcCor-st3dQIcpmh1opdDtBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae28f96254.mp4?token=acX5M-_OrqLkExpwSSW4fjjeO9STF4-1CdzMsvf-Cna60teyeLFXYJTTbhb1fq1kC9K2e9-Nqpf0YacUJJckBMWnH3MPcM5cMNmP6jazbQa3j3qxIp5zycKpNgzO4XEB2fds33Z6wOW4fCIJ-IpwQrI_nSx2xPzRtgWBgJyJD5CojfHtpRIhwqPkCEjI439ieR75gguepBcMY4hBjAZdAaDh2zkQ2Qn3tUsqJf6TKZ_cRR7Cy9R5hCJOt9HojuNzfz5vM-AC1F-uFElKCpMPnkRpef1YrY1nzFcfmBOToOiQdRdg7Q9AElrYUl0aHF3GM46HkVJM0q0H0hxbPTU_GI0wjuSuWrE9sA_NR2S1vk2Cc1Vfott1wrAecD4nHBtuZKchI5DXWS9W_o-HsWg4O_pIxUYcMWao2lPgVN3fNuqDmMjCdnFsonF-PQg5-yLTt0CWwX13yH8fiseOGbndLhHp4_Qf_r1SUIHNi2qPigIEzdX4-FznEB4GdacFgS8GHk3wH7nLfPrLaNoDnXE8FkLWhktQGvlnyzDAhE1LIRIKTi187J-raiI75z1jm37q5-2RomiIPZub75rZ5pVvvPIzeMN7fu04ix2R2P07nlylLwrwbJA9_MVoLPKEcWw0ORYDnTCTGgBrAOwClGeqcCor-st3dQIcpmh1opdDtBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار دوي صفارات الانذار داخل الكويت</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/85178" target="_blank">📅 23:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85177">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏
🇺🇸
الحكومة الأمريكية تسحب مذكرات الاستدعاء الخاصة بمراسلي صحيفة نيويورك تايمز في تحقيقها بشأن مصادر تتعلق بطائرة الرئاسة الأمريكية الجديدة.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/85177" target="_blank">📅 23:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85176">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7986b0253e.mp4?token=NXbOAAsAvgPjgm-or0hzJJ0JNi_8YpjJ7JDG1cnETnZ5JeimHirKmpcSo3deJncEIpEJo3kXHLwI1-XT2qfRTd93PvG3UoTdRW7Aq-7g8g9Mm4avVTVhTEcjt3gi5I_ugETdYlb-sCfQ73Jd_dX8cLGvXLk217tXGKDnpP2ZpfbNUc-BMMHTK8BkO8BUVkppxEPLwx6m9DXPPM5hvX-ZxxTm1g0Ul2e3il5P3oyM-RGN65UfyCFDOlZ8VtuZ8SRqZrGCElWJ9PcW5nics2hQD-QF6BH2_0C8uVDP2i2gKAbJM_g6iF88SznRQ_dcwoqg1VGHM0BLlfpIiEKZZkLjqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7986b0253e.mp4?token=NXbOAAsAvgPjgm-or0hzJJ0JNi_8YpjJ7JDG1cnETnZ5JeimHirKmpcSo3deJncEIpEJo3kXHLwI1-XT2qfRTd93PvG3UoTdRW7Aq-7g8g9Mm4avVTVhTEcjt3gi5I_ugETdYlb-sCfQ73Jd_dX8cLGvXLk217tXGKDnpP2ZpfbNUc-BMMHTK8BkO8BUVkppxEPLwx6m9DXPPM5hvX-ZxxTm1g0Ul2e3il5P3oyM-RGN65UfyCFDOlZ8VtuZ8SRqZrGCElWJ9PcW5nics2hQD-QF6BH2_0C8uVDP2i2gKAbJM_g6iF88SznRQ_dcwoqg1VGHM0BLlfpIiEKZZkLjqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار الانفجارات داخل قاعدة علي سالم الجوية</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/85176" target="_blank">📅 23:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85175">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انفجارات قوية في الكويت</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/85175" target="_blank">📅 23:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85174">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/85174" target="_blank">📅 23:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85173">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انفجارات قوية في الكويت</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/85173" target="_blank">📅 23:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85172">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انفجارات قوية في الكويت</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/85172" target="_blank">📅 23:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85171">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇷
اسماعيل بقائي:
لقد صرّح قائد القيادة المركزية الأمريكية (CENTCOM) براد کوبر صراحةً بمشاركة عدد من الدول الأعضاء في مجلس التعاون والأردن في العدوان العسكري الأمريكي ضد إيران. وإذا كان هذا الادعاء الأمريكي مجرد كذب، فإن ذلك يستدعي من هذه الدول أن تدحضه بشكل رسمي وشفاف.
‏وفي ظل هذه المعطيات، وحينما تمارس إيران حقها الأصيل والمشروع في الدفاع عن النفس بضرب القواعد والأصول العسكرية الأمريكية القابعة على أراضي هذه الدول، فإن التساؤل عن "دوافع إيران" لا يعدو كونه استغفالاً للمنطق ومحاولة تضليلية لا أساس لها.
‏لنكن واضحين: إن حالة انعدام الأمن والحرائق المشتعلة في المنطقة هي نتاج حصري للعدوان الأمريكي الإسرائيلي المستمر ضد إيران.
‏إن توفير هذه الدول لأراضيها كمنطلقٍ لتسهيل العدوان الأمريكي، يجعلها شريكةً فيه بحد ذاته بموجب قرار الجمعية العامة للأمم المتحدة رقم 3314 (المتعلق بتعريف العدوان)، كما يمثل انتهاكاً صارخاً لمبدأ حسن الجوار والمادة 2 (الفقرة 4) من ميثاق الأمم المتحدة.
‏إن ممارسة إيران لحقها المشروع في الدفاع عن النفس ليست إلا خطوة ضرورية لاستعادة الأمن والاستقرار في المنطقة بأسرها.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/85171" target="_blank">📅 22:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85170">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0960660f1a.mp4?token=RSRIbXKSm82W6Eb7Y6Su_8C4_ALvwiNCAnICXX77GDk00MV7EsWDjwZA57mwXSBD9k7rJp4VLiY3UTwkxwgQ4jhFrUS28pvnNoCPdN4NAQ2wOLXiv9Ld29LEiiwASP_Q9xMJvIF3sNJx84wyZ6d84NT9hzYJbnd7UBBz73kkBmNsduqQ89eZpvN_T8rsBW3nxuBsuctwl1Ef6WY9hh58XlUuYMxfc9aXGZydufxAAbTyEsKPqcytjt8Yr4DJjTReHWFoxSPkqxVU5zzXg5nktM4PlzhNDFDPYhl1_4IZ_NhbsIbRanLQwZN8iA1EScasUWPubO7WEKok2QERawfvAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0960660f1a.mp4?token=RSRIbXKSm82W6Eb7Y6Su_8C4_ALvwiNCAnICXX77GDk00MV7EsWDjwZA57mwXSBD9k7rJp4VLiY3UTwkxwgQ4jhFrUS28pvnNoCPdN4NAQ2wOLXiv9Ld29LEiiwASP_Q9xMJvIF3sNJx84wyZ6d84NT9hzYJbnd7UBBz73kkBmNsduqQ89eZpvN_T8rsBW3nxuBsuctwl1Ef6WY9hh58XlUuYMxfc9aXGZydufxAAbTyEsKPqcytjt8Yr4DJjTReHWFoxSPkqxVU5zzXg5nktM4PlzhNDFDPYhl1_4IZ_NhbsIbRanLQwZN8iA1EScasUWPubO7WEKok2QERawfvAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
تضهر صور الاقمار الاصناعية تدمير مركز البيانات التابع لشركة امزون بالبحرين على اثر قصفها بالصواريخ الايرانية.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/85170" target="_blank">📅 22:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85169">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇱
اعلام العدو: جاري تحقيق بوجود حادث امني عند الحدود مع الاردن.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/85169" target="_blank">📅 22:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85168">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHynhznJR91RjQKTdmWa3M4jF-tgH4T0BYroqHGtZ-D6Bw5aKa6Bhq6SzjClvSR6Se-gECBhFRjpY2wj6SuAucJY__kGuiVCvFx-1RSF9UpJCIZVdFbrBTRUumvir72LLFiM7PAu21Hr4DQKx_Y0TuV6lZP4wAPpGDTT-WesHbFnuX0NT_vz0YBecgOSedXUXIbpozqvU7xn4MS6_KSY3bIpGYhS5adSu4BhGUheAr2-HRfEb9uUthUnVGPsNIRZ5cAwzoEQuLOE5Zyi83bCXSrivol-3IdBt2c9y19aEOc-JgeWiwr0F-HOgSvI7IDKJFv2X0j4ajfH-3KHGP5xEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇪
مواطنة كويتية تهاجم ترامب ان تهاجم ايران وأحنه نأكلها
اتركوا لها تعليق جميل
https://x.com/q8mahaal/status/2080319421759819938?s=46</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/85168" target="_blank">📅 22:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85167">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇱
‏
جيش الصهيوني:
سنرد بحزم على أي هجوم إيراني علينا.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/85167" target="_blank">📅 22:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85166">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇱
اعلام العدو:
جاري تحقيق بوجود حادث امني عند الحدود مع الاردن.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/85166" target="_blank">📅 22:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85165">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇶
🇮🇷
حركة الزائرين الان في منفذ الشلامجة الحدودي بين العراق وايران ..</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/85165" target="_blank">📅 22:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85164">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbc6b9e32f.mp4?token=snMvxTZCcEhfy1_KmzH1W5AOjqf3376FBlQyezMDsIxVp3FJy93dPs-oSJgyTrSGGC7hREMypn5lMKtpHyE73GQTHGQXwskX4_PlSd1SQUFgkXwCErmHCf4pGqj_s80WcXjUcLL7PjUApOT0cYwgO1JZMsollBI4_Q_RaJkhrVV7NnVJfCOf44CLSdvPMialn1act52O2d5Qttw_WWxHCcO1xKAPryZwxWVUjytzHV7nlz9IGSaIF8kfpk6UyuTJRFGXGAaV2XLZVWO2y36vBFY9Mtc_KO9uQimQKZg06xL7ipgVg6qFgUHx049zRLfZxkM6xg_d0_de6MfRMWJVCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbc6b9e32f.mp4?token=snMvxTZCcEhfy1_KmzH1W5AOjqf3376FBlQyezMDsIxVp3FJy93dPs-oSJgyTrSGGC7hREMypn5lMKtpHyE73GQTHGQXwskX4_PlSd1SQUFgkXwCErmHCf4pGqj_s80WcXjUcLL7PjUApOT0cYwgO1JZMsollBI4_Q_RaJkhrVV7NnVJfCOf44CLSdvPMialn1act52O2d5Qttw_WWxHCcO1xKAPryZwxWVUjytzHV7nlz9IGSaIF8kfpk6UyuTJRFGXGAaV2XLZVWO2y36vBFY9Mtc_KO9uQimQKZg06xL7ipgVg6qFgUHx049zRLfZxkM6xg_d0_de6MfRMWJVCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: إيران ليس لديها جيش، ‏ليس لديهم شيء سوى أنهم لئيمون وأذكياء، ولا يزال لديهم بعض القدرات.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/85164" target="_blank">📅 22:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85163">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇸
ترامب: ‏كنا في فيتنام لمدة عشرين عاماً، وخسرنا آلافاً ومئات الآلاف من الأرواح. كنا في أفغانستان لسنوات. ذهبتُ إلى دوفر. قُتل أربعة من الوطنيين الأمريكيين العظماء. هذا يعني 18 قتيلاً في حربين. 18 قتيلاً فقط، بينما خسرنا في فيتنام 200 ألف قتيل، ‏استقبال الجنود…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/85163" target="_blank">📅 22:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85162">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70fe84e6b1.mp4?token=nA58VFUfAJWeJUUJOFv5GPOVJzMpCD9PmBg1hHFszA1cFgEjf7SUbLuzVCstSPNLMSRtPqHfYKkktrC8xevuH1_0peUoikzCew4WfZnKtr5IMddI-vRnHf0u1eZguZcJtn5hcDJBuxlqeb6nhboI1mRTekhvEmbG06HX1m9DpD5fXxyCCWTLCa2Jq0XF9IecJMypX4YCpePEUYM833aNQqMWk2J7tW2QaY5hAQI_NYwelO2qpcBjaxyF_mis6IBUeGORJB5vqJ02J5dkjwGwrhDAXzHyy1tN94V_WcvCDXztCrmeWVTPjviXHRwBMWeu8KzirKuigOZW5wH_7TNYxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70fe84e6b1.mp4?token=nA58VFUfAJWeJUUJOFv5GPOVJzMpCD9PmBg1hHFszA1cFgEjf7SUbLuzVCstSPNLMSRtPqHfYKkktrC8xevuH1_0peUoikzCew4WfZnKtr5IMddI-vRnHf0u1eZguZcJtn5hcDJBuxlqeb6nhboI1mRTekhvEmbG06HX1m9DpD5fXxyCCWTLCa2Jq0XF9IecJMypX4YCpePEUYM833aNQqMWk2J7tW2QaY5hAQI_NYwelO2qpcBjaxyF_mis6IBUeGORJB5vqJ02J5dkjwGwrhDAXzHyy1tN94V_WcvCDXztCrmeWVTPjviXHRwBMWeu8KzirKuigOZW5wH_7TNYxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب يعلن عن مناقشة قادمة حول الحرب مع إيران.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/85162" target="_blank">📅 22:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85161">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4D3X0VUSAZpmdqcLfMLWpwquJSKAOSyFKmUVkoyihzYM30ixFtYylSNOWy3c48GWFL99CIujBOJ90WPA9otxGuArN-2cVrFclHIVFaKIaZ6o6Li38KWzeeFuHewe4GG9aCcfI5oZPwxCzA-CylWRBcvOs5SPq3-jmd8WzistcWDPky5g4idnt7En6lvJI8BuWxHfLJj_rgAOQ98bUq4wJDnP1o-I586QtQWdu5NWEoUJIO2gbDRCoUPL6qaiJHdDjjQENMcLc2plDaIalHeWn4_9JDBlfyF3GIEL9wrwxh4qBZyD5GkQwPfUOqQaYaZ38F4rSt0cUehBzH2OcrgKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاول مرة
الجيش الأمريكي يشتري صواريخ باتريوت PAC-2 القديمة لأول مرة منذ عقود
‏صواريخ PAC-2 GEM-T ليست عموماً بنفس كفاءة نظيراتها من طراز PAC-3، لكن الجيش يحتاج إلى كل صواريخ باتريوت التي يمكنه الحصول عليها.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/85161" target="_blank">📅 22:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85160">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/85160" target="_blank">📅 22:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85159">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
مصادر ايراني توضح انه لم يحدث اي انفجار في شيراز</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/85159" target="_blank">📅 22:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85158">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامب يعلن عن مناقشة قادمة حول الحرب مع إيران.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/85158" target="_blank">📅 22:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85157">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">يا قائم الـ محمد</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/85157" target="_blank">📅 22:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85156">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/85156" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/85156" target="_blank">📅 22:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85155">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔻
مصدر خاص من فصائل المقاومة لنايا   بسم الله الرحمن الرحيم  العملية الأولى  تقرير عن عملية مسیرة بتاريخ ۲۳ یولیو ٢٠٢٦ الساعة ١٤:٠٠ استهداف معبر الحدود الكويتي ردًا على الاعتداء على معبر حدود شلامجة  إحداثيات الهدف: 38R PU 60460 31042</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/85155" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85154">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔻
مصدر خاص من فصائل المقاومة لنايا
بسم الله الرحمن الرحيم
العملية الثانية
تقرير عن العملية الجوية الثانية بتاريخ ٢٣ يوليو ٢٠٢٦ الساعة ١٩:٠٠
الهدف: مبنى قيادة الحدود الكويتية ردًا على الهجوم على معبر شلامجة الحدودي
تفاصيل الهدف:
38R PU 61239 32037</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/85154" target="_blank">📅 22:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85153">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔻
مصدر خاص من فصائل المقاومة لنايا
بسم الله الرحمن الرحيم
العملية الأولى
تقرير عن عملية مسیرة بتاريخ ۲۳ یولیو ٢٠٢٦ الساعة ١٤:٠٠
استهداف معبر الحدود الكويتي ردًا على الاعتداء على معبر حدود شلامجة
إحداثيات الهدف:
38R PU 60460 31042</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85153" target="_blank">📅 22:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85152">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ربما يسمح بالنشر بعد قليل</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/85152" target="_blank">📅 22:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85151">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔻
تواصل أسعار النفط العالمية ارتفاعها عقب التطورات الأخيرة وإغلاق مضيقي هرمز وباب المندب ليتجاوز سعر برميل النفط حاجز 101 دولار.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85151" target="_blank">📅 22:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85150">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a796ffbbb1.mp4?token=JfUgA3cX_IJIsP5Z7qnbHVYuI4pCu8IU1bXpuHRJjgQ1QHhqA_8qmJkv0RMPnMv4Y254bYdYwb2mauQhLp1NA36-c9bLuAfSQRvlNgJkkn9ld-SBTt9UzEUCx1EYxTn2yrYmdXEd4JYmoiT4vdm1I65CTvD_aQjU0320wQclgzteSDkKt-SK-1K5qjZDWoorFbnfby2-Xh8C32QXa3KfTDHZXHJoAU2oW8TfC72iIyO3EBsNveCK0Ky60eGi-d92_F16rHepME50HY5SY8m761E_MrIGKsi8FZAls3A8AtoDahbHQgnI4mO-wR2bG7og-y3N8VoxESfQCRSrDh0CGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a796ffbbb1.mp4?token=JfUgA3cX_IJIsP5Z7qnbHVYuI4pCu8IU1bXpuHRJjgQ1QHhqA_8qmJkv0RMPnMv4Y254bYdYwb2mauQhLp1NA36-c9bLuAfSQRvlNgJkkn9ld-SBTt9UzEUCx1EYxTn2yrYmdXEd4JYmoiT4vdm1I65CTvD_aQjU0320wQclgzteSDkKt-SK-1K5qjZDWoorFbnfby2-Xh8C32QXa3KfTDHZXHJoAU2oW8TfC72iIyO3EBsNveCK0Ky60eGi-d92_F16rHepME50HY5SY8m761E_MrIGKsi8FZAls3A8AtoDahbHQgnI4mO-wR2bG7og-y3N8VoxESfQCRSrDh0CGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الآن، صاروخ «ذو الفقار» في ساحة آزادي (الحرية) بطهران.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/85150" target="_blank">📅 21:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85149">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZcSQcs45zDwNY1RXoX6cO-mIjyIEcyDWWrahjAFxTlU-6htuhmRZRY35DTpdyTZ6F4x-bhgw7U78PYlpiQErCij_mCqy_kwG9v_OaSKthuQAfrze3q7AXuhUxgHQyzNedkgUl-Sm9MQoWlQaiqlKlG20Ohw2CS6_D-0ZUIqic3NMwumqZTDzhnCF4oENk9C3nzbWu18bOQAj3BBRWZ0UBeyoWlpw0EjOoEv82WgRztr2Tuy-F2xaN4arj4EppkDpdVrMgoSTdBggYfw2VaVqKRbsVm2Q4gXDrTavW3lmiyLQ9IjvORoSOHbOaTT1-yvBGkPrmu933VZUhUSi2QwJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
يتقدم أهالي العراق وحركات المقاومة الشعبية حول العالم بأحر التعازي والمواساة بوفاة المناضل الياباني
كوزو أوكوموتو
أول وآخر لاجئ ياباني في لبنان المعروف باسم
"أحمد الياباني"
.
لقد جسّد الحاج أحمد نموذجا نادرا في الإيمان بالمبدأ والالتزام بالقضية مؤكدًا أن طريق المقاومة والحق لا يعترف بالحدود التي يرسمها الاحتلال ولا تحده جنسية أو لغة أو عرق. وستبقى سيرته شاهدا على أن الانتماء الحقيقي هو للموقف والقيم وأن نصرة القضايا العادلة تتجاوز كل الفوارق.
الرحمة لروحه، والعزاء لكل الأحرار الذين عرفوا فيه مثالًا للثبات والإخلاص.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/85149" target="_blank">📅 21:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85148">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe18daab7f.mp4?token=Qnh-j_aWFUYEc3sk807S9n6voxZVsVFIiLT5quzzvJANgnBydtRlCRjlJhrjTHDcCqYYgv1VQXvun1ZEsJK5mumGNlbZBBizg3zgUiGO7iaKUkaCpQjzKx2DdSbFqwJjhSlgWBXDCuGRjQuvdpUAWwq_akbGHsm7dpRqvyp_YP1K_L2KZfsr_-lh0VvJfQzoCNXACu3nyEDAMEJl39HuA3-Uy3wn--U0L2QWsJ2aXLSOCz0_Clvk9TQsQWL5t8weyFutHj7DNG8wC3LOXyTUJpuyLRk2rFyKPGCSKRACb08ARNQ_T3-cY_B4gy5fSqk1CItBPqBMnIbyJynnYFWuHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe18daab7f.mp4?token=Qnh-j_aWFUYEc3sk807S9n6voxZVsVFIiLT5quzzvJANgnBydtRlCRjlJhrjTHDcCqYYgv1VQXvun1ZEsJK5mumGNlbZBBizg3zgUiGO7iaKUkaCpQjzKx2DdSbFqwJjhSlgWBXDCuGRjQuvdpUAWwq_akbGHsm7dpRqvyp_YP1K_L2KZfsr_-lh0VvJfQzoCNXACu3nyEDAMEJl39HuA3-Uy3wn--U0L2QWsJ2aXLSOCz0_Clvk9TQsQWL5t8weyFutHj7DNG8wC3LOXyTUJpuyLRk2rFyKPGCSKRACb08ARNQ_T3-cY_B4gy5fSqk1CItBPqBMnIbyJynnYFWuHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مسلحي العشائر التابعين لحكومة الجولاني وعصابته يعلنون بدء الحرب ضد ميليشيا قسد في مدينة الشدادي بمحافظة الحسكة السورية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/85148" target="_blank">📅 21:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85147">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04132ae88a.mp4?token=l864y5Gxu5oqZ2PWQCPUcc4UnyjPI2ghzq2wUXG6-tHwlODBRe8Vgv3G-SL-vz29VIQ4194AVPWTC8tOjf1E8fNoFapekvF9wtbQzG96TihfxtyhmZnY907cksYvWT6k0LAJdWxyiwLwVoVGi1Od-I1EQDIbVBw4J5ky5ZRxS8661ZacKx_EgcAJ1cz9hOxRGMnpdeWQmDGVr19YT50JlRYI79RJ5f01csY_iXxHWysBr6FisZ9jOP28Q3VJ0Ngvz7whyHXWUP_UCW2-eSre9p5-pbbkYMcDf0-L43PQWS8yQ55E6_EUwOCK6Fk6Z0ul2v6d3F9i4UZnraKHMB9VcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04132ae88a.mp4?token=l864y5Gxu5oqZ2PWQCPUcc4UnyjPI2ghzq2wUXG6-tHwlODBRe8Vgv3G-SL-vz29VIQ4194AVPWTC8tOjf1E8fNoFapekvF9wtbQzG96TihfxtyhmZnY907cksYvWT6k0LAJdWxyiwLwVoVGi1Od-I1EQDIbVBw4J5ky5ZRxS8661ZacKx_EgcAJ1cz9hOxRGMnpdeWQmDGVr19YT50JlRYI79RJ5f01csY_iXxHWysBr6FisZ9jOP28Q3VJ0Ngvz7whyHXWUP_UCW2-eSre9p5-pbbkYMcDf0-L43PQWS8yQ55E6_EUwOCK6Fk6Z0ul2v6d3F9i4UZnraKHMB9VcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
مسلحي العشائر التابعين لحكومة الجولاني وعصابته يعلنون بدء الحرب ضد ميليشيا قسد في مدينة الشدادي بمحافظة الحسكة السورية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85147" target="_blank">📅 21:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85146">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzLZD78xymQc58MVHsh3zme_YV__4wEIVXDnCoPlJzRryAq_TFFs_Jg-a4QqLaI5zqvzZWEynwPQ0Pu1C-hO4n7_5HNoqWh-W_oFdaAhdoLTVYAfDvhcVNE5yuUHV9UHwIIIAAq4IPDRpLCtMF-2wOfSyczoQkxE0TJBFB954att9RZui-4hw_jS9F9kJrxeqdgeK4FofXaVhCE0Iitf7eaWZ39hmFTJQXQYJaDqx4j1Nn2BxzjOPVHsfG7asC-yCCJ4_qCzVmwvFxWui1EakL9-6z9czoMbh-rKIU2gLdTtI57eJt5HrZUDXx_8Bz1D3GjmLqWmYaaP8p86-kYNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الآن، صاروخ «ذو الفقار» في ساحة آزادي (الحرية) بطهران.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/85146" target="_blank">📅 21:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85145">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇶
اشتباكات داخل احد مقرات الاحزاب المعارضة الايرانية ومقتل العديد من افراد المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/85145" target="_blank">📅 21:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85144">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcFTlpH8ALwGCD_LUsRjgcKCEaaY9mPAXcLFQFaEI711qIwpkAUBnpnShOOI1hgaMu1PfohIeHKD2F0keTRmCgsmXJPDbXWGLqo-5E2r1FjvlH9-4N1F9SXPqk-dt5E3_KYpmfTRwCLvXP4hueo4qG_XhjJa_Sy7iiH2-gLqWQUwd803jSVKNvGgZ895Rc7igVTaZJ_0_KtHC99rgqWyK70bBA3oby6G6mOcXlKl3m2vryRIPys7qCnwMhXjMsCXTMfl2vkf1ifBQ1VNp_0UlVkQxHPvxj4bTFZ4Mqq7uR3vcA93GRPkI71JIT1BK3pvCK_YBxUiaHAYN1gqRMklrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
خريطة للعمليات التي نفذتها إيران منذ ٢٣ من شهر الحالي بناءً على البيانات الرسمية.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/85144" target="_blank">📅 21:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85142">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رويترز
": سفينة تجارية خُطفت الأسبوع الماضي قبالة خليج عدن في اليمن باتت في قبضة قراصنة صوماليين.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/85142" target="_blank">📅 21:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85141">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d399ccf44.mp4?token=BmSoaDL9LSFShJpdymks5fU2zMq5xdfV-XtcDN9kKdJYXrtUvZlHFr5WNIQeQtqeD3ho2ClyX62qmqtCvyxUr-t2hr6VUxDFUzR7jjRZ8rc0jMnFRLOczNTZMM9N60QTLRMIaxo5ATCfYE7hVHseJAusdIp0cLZ-m84P4Gkals_1d2pmTHjH-c5ZjrYfZA_AsYoV3Ji_U8cyjEmR9FXa8sCcEjzhOOwuGPmHGtquwJ8DjLXh6q5QnXNqlAjnH3TvafUkKW484zNOu5_sEUJeabJlbmubKN15vV-9lqd-IeLhOOJTBE3Hd-vU_Ylxvu-_jaf87CrzZE1bxRAxPz9HDKnQC3bcbi7dBUMpJ9zPjLXnKkxN2CWBC5H_Pjj_upgUL49DP1GbdyFzd1BsE9D6GlbcOx8D7FImrnV8aArzbKa5IwHNLknZorK9R44h7gde9t-T0x6rLlf3Im3khOA7oCs22Pfv7Nj9tyOiDPUmapOKG5GI8t5mxbiMcDwM5EtfyvPZngsskhGNOjUW1FsLnVYsm2vGjKWuQ2sR2MHYwq0J4VpjEQXCd9wimmFwRXHlwuwWSFiVCmcJYS9N4PjoeA-febMypR5SEEGZNmAA29g8rzB9JcOCBl16b5396KVM_SRqK4iJX7rJGsNo_m9OVTYDSFrkhxbhgnTXnKssmHs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d399ccf44.mp4?token=BmSoaDL9LSFShJpdymks5fU2zMq5xdfV-XtcDN9kKdJYXrtUvZlHFr5WNIQeQtqeD3ho2ClyX62qmqtCvyxUr-t2hr6VUxDFUzR7jjRZ8rc0jMnFRLOczNTZMM9N60QTLRMIaxo5ATCfYE7hVHseJAusdIp0cLZ-m84P4Gkals_1d2pmTHjH-c5ZjrYfZA_AsYoV3Ji_U8cyjEmR9FXa8sCcEjzhOOwuGPmHGtquwJ8DjLXh6q5QnXNqlAjnH3TvafUkKW484zNOu5_sEUJeabJlbmubKN15vV-9lqd-IeLhOOJTBE3Hd-vU_Ylxvu-_jaf87CrzZE1bxRAxPz9HDKnQC3bcbi7dBUMpJ9zPjLXnKkxN2CWBC5H_Pjj_upgUL49DP1GbdyFzd1BsE9D6GlbcOx8D7FImrnV8aArzbKa5IwHNLknZorK9R44h7gde9t-T0x6rLlf3Im3khOA7oCs22Pfv7Nj9tyOiDPUmapOKG5GI8t5mxbiMcDwM5EtfyvPZngsskhGNOjUW1FsLnVYsm2vGjKWuQ2sR2MHYwq0J4VpjEQXCd9wimmFwRXHlwuwWSFiVCmcJYS9N4PjoeA-febMypR5SEEGZNmAA29g8rzB9JcOCBl16b5396KVM_SRqK4iJX7rJGsNo_m9OVTYDSFrkhxbhgnTXnKssmHs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العوائل الكويتية الكريمة تناشد عبر نايا العراقيين بالسماح لهم بفتح المنفذ الحدودي مع العراق بسبب النقص الحاصل بالباميا والقيمر العراقي والنومي بصرة والخريط الذي سوف يتسبب بمجاعة كبيرة لا سامح الله إذا ما استمرّ الوضع</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/85141" target="_blank">📅 20:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85140">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇷
بحرية الحرس الثوري تستمر باطلاق طلقات تحذيرية للسفن المخالفة لقوانين عبور مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/85140" target="_blank">📅 20:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85139">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErKFOoGDytsdNj3wLFm93EG0e4b4xgWETTvejuUQ46tz53DQsrM23LQe33tjDn0x39iUu-VmRNiFmehCAGqfiyDfwHKiGU523yStOYvG1yREuFCVA08N9Okmi7VJzyruOJYACI4ilMZ4BbRnwPQd4qBfG3zuogg6I28y9A8k1y93hvLEeQGkGEAXAXW7Pcb9UZEfs46LosSRWlzxGecK-HGo-eGfB1uoW901gNrQr1gB0Y212XqtrGVqBzllE1YZm7m0tWn_pCdLvVnSEPpXZLb2AvM_3s_ihaL4s1LsQ1Y9u_T7l_0JO8mPvtXzTJAVl8kWKIhgOUqjMVna6_xAjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسعار النفط تتجاوز الـ100 دولار للبرميل</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/85139" target="_blank">📅 20:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85138">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5kAqIcn8Eyf0SIXAe0cfoDH_Earl3TilflsEvslt7xhaA-Ki7BY69RI7flAdG2aRAEgV8URYWROXHZsx81BMzY4pVd6MLI5IwWg_K_IooR2kNwcqYJM7bRJJnXMfGXhd8k9KacQZZOFONehMBHQk8xYkfFHQ-F3f2oYs7B-UQzys20Bs6oFUyEn44pY9PogJiHf9L-lJE1TnthXUYcTXWYGAfOZULIxkEL28quJ-HowkwOnG0wyMj26GpCnAM9KUqK5K_knbG_agEPyCZG-IUEMQKPsHQYo3lzU5owGiKub0e-5UXfqFD2c_okxq5mkmQwLt9kWFhqaANPZOedCaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇮🇶
هل ستحاسب هيئة الإعلام والاتصالات العربية السعودية ؟!
تحاول دولة السعودية عبر إعلامها قناة العربية تخريب العلاقات بين الكويت والعراق علما ان ولا جهة حتى اللحظة تبنت الهجوم والعراقيون يمتلكون من الشجاعة والإقدام ان يعلنون ما يقومون به بلا خوف ولا تردد ! هل سيحاسب بليغ ابو كلل العربية !</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/85138" target="_blank">📅 20:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85137">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏
بريطانيا
: قواتنا جاهزة للتصدي لأي هجوم بعد تهديدات إيرانية</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/85137" target="_blank">📅 20:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85136">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
ترامب: أنا بصدد التفكير في هجوم ضخم - أكبر من أي شيء حدث من قبل، وأنا على وشك اتخاذ قرار، وانضمام إسرائيل إلى الضربات ضد إيران سيترتب عليه "عواقب".</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/85136" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85135">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇺🇸
امريكا مخترقة من الداخل
أخبار عاجلة  سحبت خدمة الأسرار أحد العملاء من فريق الحراسة الشخصية الخاص بـ "فانس" بينما يقوم المحققون بفحص ما إذا كانت معلومات أمنية قد تم اختراقها.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/85135" target="_blank">📅 20:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85134">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8KaJTDaYpkwYhtAxK-ygpK1UaN0b3etYDxwC2VBoE3-XceYJMQ3HBwq1phSKeZAvaWEg8n2AfxAlXUaev0j_snDICXUVcKbK8m5R5Aqt-iqJ_X9X5Ekkdc8kOA0g_5DqWMmi7DI8FXGZilI5C_omB6R9nTix8gYlI_PoGSVh_KjAxWslvFAH6jSkZa6rct2uAP1YNDYvQrM7-GLg3_sQzzgjvUedChEL5RH417h0kZtcHja7FlXo139wu-VCt-Ei2V_y0Yf07O66buituoh96YXwCQND8Owy3Nk3DIYewf_6-hjtDIz8GxMUzJzcAhyNveLyt70lEdER8ANjqaWLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
تنويه لم يصدر اي تبني من اي جهة عراقية حتى اللحظة حول عملية استهداف منفذ العبدلي الكويتي ؛ وما نشر وقبله قناة العربية الكويت التي اتهمت اولياء الدم هي اخبار تندرج من ناحية الاخبار الكاذبة والتحريضية من جهة الإعلام الخليجي المطبع مع الكيان الصهيوني لذلك اقتضى التنويه ..</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/85134" target="_blank">📅 20:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85133">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
مصادر ايرانية تنوه:
الانفجارات في لارك ناتجة عن اطلاقات تحذيرية للحرس الثوري للسفن التي تنوي عبور مضيق هرمز.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/85133" target="_blank">📅 20:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85132">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مصادر غربية : بعثة المانيا في ايران غادرت</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/85132" target="_blank">📅 20:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85131">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مغلق لاشعار آخر   منفذ العبدلي قبل قليل بعد تعرضه لمسيرات هجومية جديدة</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/85131" target="_blank">📅 20:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85130">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">😎
زيلينسكي
: يستعد بوتين لشن ضربات جديدة ضد أوكرانيا، ويستعد، في رأينا، لتعبئة إضافية في روسيا، ويستعد لتوسيع نطاق الحرب.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/85130" target="_blank">📅 20:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85129">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
‏مجلس الشيوخ الأميركي يعطل قراراً يقيّد صلاحيات ترامب بشأن الحرب على إيران.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/85129" target="_blank">📅 20:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85128">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4f8070a5.mp4?token=L0V_YxvjjubvJABAfIpKWvjlMzZ8ULSG8Riw3AC4iVJM7LPxM_ahxGhkB3Rerme1j-N6L3BH3iTcohli2Y5pgadhVwGBPVWMWeAnwZT49wAWbUjdzdD3auP-Vq6HCxn-dryOa5nMdCFe317SbKzmOg1lx40aMqgAVV3bFUnqs-BnZOq3Cj1ardml_iP3Rn8ZSoP5WMfVd9IdCMEB5oTajzKPPW6b71wA4TqgNawPvigz7XoPlquif-7ykCYwy973L1QLjM1cKhUE8LkvAXoIOU5yxTPuG_vI688yfNvqrGzuIjNCHJ-5KXuFn1WVJi_u3tm-FxiRNnOkTSHsZ5rMMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4f8070a5.mp4?token=L0V_YxvjjubvJABAfIpKWvjlMzZ8ULSG8Riw3AC4iVJM7LPxM_ahxGhkB3Rerme1j-N6L3BH3iTcohli2Y5pgadhVwGBPVWMWeAnwZT49wAWbUjdzdD3auP-Vq6HCxn-dryOa5nMdCFe317SbKzmOg1lx40aMqgAVV3bFUnqs-BnZOq3Cj1ardml_iP3Rn8ZSoP5WMfVd9IdCMEB5oTajzKPPW6b71wA4TqgNawPvigz7XoPlquif-7ykCYwy973L1QLjM1cKhUE8LkvAXoIOU5yxTPuG_vI688yfNvqrGzuIjNCHJ-5KXuFn1WVJi_u3tm-FxiRNnOkTSHsZ5rMMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أنا نايا عندي كل الخفايا  الجيش الكويتي تعرضنا لهجوم مجددا بالعبدلي</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/85128" target="_blank">📅 20:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85127">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ارتفاع اعمدة الدخان من منفذ العبدلي الكويتي</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/85127" target="_blank">📅 20:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85126">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اصابة مباشرة في قاعدة علي السالم الان</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/85126" target="_blank">📅 19:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85125">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اصابة مباشرة في قاعدة علي السالم الان</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/85125" target="_blank">📅 19:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85124">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/85124" target="_blank">📅 19:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85123">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">موجة اخرى من الغضب الحيدري</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/85123" target="_blank">📅 19:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85122">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏
وزارة الدفاع الألمانية
تعلن أنها تعتزم سحب سفينتين حربيتين من منطقة البحر الأحمر</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/85122" target="_blank">📅 19:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85121">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">موجة اخرى من الغضب الحيدري</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/85121" target="_blank">📅 19:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85120">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇸
مرة اخرى تنوه الخارجية الأمريكية
😆
:
على الأمريكيين في الشرق الأوسط الاستعداد لاحتمال إلغاء الرحلات وإغلاق مجالات جوية في المنطقة.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/85120" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85119">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔻
Here's what the Iranians would say to the U.S. ...
🔻
Naya team on telegram</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/85119" target="_blank">📅 19:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85118">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juNwuRPZByrkQslMArHLiKwzLXIasazyNf4895W7HgKfu4afrr25QtTPlW0iu8D3V04j4WdHvGCOnqSk4X8kobE90T-B9eU4owqkUWUmRD666aS0ALRmpHC1ZouUqYCz9fAvwrxIOgraagZndIT2sxONhKMx4JcVRsRB5zU6xnwW1x76dqJvCIxabd3X3rj3dcE9fe8aYHD264IMdEp6F0PIY4sxNjUWakiMGcw7seY9dc2X6-ggWq7dWAHMYP8mLRU3zZ2i8s9dotZ6MM_OuZI3XG4FguiqzjMpYptHKPlKd3lwPgea_wADwy4rVSOXlbkbgv1rI4s6mOvk0FApZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب الإيرانيين لم يتلقوا بعد الألم</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/85118" target="_blank">📅 19:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85117">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شبه لهم يا حسين
ما طحت انت من ميمونك</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/85117" target="_blank">📅 19:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85116">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">موجة اخرى من الغضب الحيدري</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/85116" target="_blank">📅 19:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85115">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/85115" target="_blank">📅 19:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85114">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/85114" target="_blank">📅 19:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85113">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تفعيل الدفاعات الجوية الإيرانية في سماء قشم</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/85113" target="_blank">📅 19:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85112">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ارتفاع اعمدة الدخان من منفذ العبدلي الكويتي</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/85112" target="_blank">📅 19:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85111">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/85111" target="_blank">📅 19:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85110">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/85110" target="_blank">📅 19:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85109">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/778c692cfe.mp4?token=QUTqQl80eg9fcmM5JZSjuy6RLtCDHpahEfdJAJ0hgtUk_K2gn9npj8Y2jaBPfMXJTDIgeQr0jetimme9cmDTV-oOat2acfUgntGsJNU16WZ4dMVidqaZI-MEcSl0XHePS2ykm3iet6FeRgPRuu1GvW6g1xAYbVAyA4vW_LmMr67wcpXpwrvEOCrdFOIxpr9n7jz5BeBx5vhzEGSLOXTxN4Qw7Gydgd7e02NRt-ojWVxDNzwNCdESwetZyeb5JdTSheTM92Ox6hqGyLGmbMNOE-HWvq7FpMx6UqLDMKFQD6y9M0pUOyQHS9c-f2iCnQEia5guRpIFOIyRXGYUjgNyIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/778c692cfe.mp4?token=QUTqQl80eg9fcmM5JZSjuy6RLtCDHpahEfdJAJ0hgtUk_K2gn9npj8Y2jaBPfMXJTDIgeQr0jetimme9cmDTV-oOat2acfUgntGsJNU16WZ4dMVidqaZI-MEcSl0XHePS2ykm3iet6FeRgPRuu1GvW6g1xAYbVAyA4vW_LmMr67wcpXpwrvEOCrdFOIxpr9n7jz5BeBx5vhzEGSLOXTxN4Qw7Gydgd7e02NRt-ojWVxDNzwNCdESwetZyeb5JdTSheTM92Ox6hqGyLGmbMNOE-HWvq7FpMx6UqLDMKFQD6y9M0pUOyQHS9c-f2iCnQEia5guRpIFOIyRXGYUjgNyIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع اعمدة الدخان من منفذ العبدلي الكويتي</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/85109" target="_blank">📅 19:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85108">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=sdN8Hx1V9lqVH8PeAHQULQY8grqynUPjUldQU0xeDv2wdENDDkMeWjf56m45LwiwIsArifbPfMJsQ3z_WJE60y97NxDN1XJjprhO1wxNC2JuJuMC4mWls3pmyEeEAsZBzC9_lXdoDWREXsgH7zFiHGiYtOhC5dZMxMWnEyh73a6vC9HV7lZn1BKThKZACdwws3HQuXXVb1Jf1rpxVmfUkXFmsybTZ2u_nJ-X_SgpzjQwbOLyIu-zvI6l2RKhwpBJg6HxHxRGGR1qeniUMCVGeDH3GGmE-hvN-zuDj_wlGZytuy_JyLeaqftVZY4dAFEE-JxE13FoMHpVAL0vDYQoJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=sdN8Hx1V9lqVH8PeAHQULQY8grqynUPjUldQU0xeDv2wdENDDkMeWjf56m45LwiwIsArifbPfMJsQ3z_WJE60y97NxDN1XJjprhO1wxNC2JuJuMC4mWls3pmyEeEAsZBzC9_lXdoDWREXsgH7zFiHGiYtOhC5dZMxMWnEyh73a6vC9HV7lZn1BKThKZACdwws3HQuXXVb1Jf1rpxVmfUkXFmsybTZ2u_nJ-X_SgpzjQwbOLyIu-zvI6l2RKhwpBJg6HxHxRGGR1qeniUMCVGeDH3GGmE-hvN-zuDj_wlGZytuy_JyLeaqftVZY4dAFEE-JxE13FoMHpVAL0vDYQoJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لا عزاء لنتنياهو و ترامب... إسبانيا تتغلب على الأرجنتين</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/85108" target="_blank">📅 19:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85107">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇸
ترامب
: أنا بصدد التفكير في هجوم ضخم - أكبر من أي شيء حدث من قبل، وأنا على وشك اتخاذ قرار، وانضمام إسرائيل إلى الضربات ضد إيران سيترتب عليه "عواقب".</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/85107" target="_blank">📅 18:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85106">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">▫️
المفتي العام لليبيا
: الأردن يتستر على وجود القواعد العسكرية الأمريكية فيه وأمريكا تفضح ذلك.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/85106" target="_blank">📅 18:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85105">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">▫️
بيان لدول الخليج والأردن:
نرحب بقرار رئيس وزراء العراق حصر السلاح في يد الدولة ونؤكد دعمنا لإجراءات حكومته.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/85105" target="_blank">📅 18:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85103">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇱
بلدية يفنيه تفتح ملاجئها وسط الكيان الاسرائيلي.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/85103" target="_blank">📅 18:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85102">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
🇸🇦
🇾🇪
التلفزيون الرسمي الايراني :
الاهميه الحقيقية لحصار الحوثيين للسعودية ستكون عندما يتم إغلاق قناة السويس عبر اغلاق باب المندب
حينها ستحدث الصدمة الكبرى لسوق الطاقة في العالم.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/85102" target="_blank">📅 18:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85101">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇱
🇮🇷
اعلام العدو يتحدث عن إحباط خطة إيرانية للتسلل إلى إسرائيل واستهداف كبار المسؤولين.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/85101" target="_blank">📅 18:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85100">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سرينا يا رجال الله</div>
  <div class="tg-doc-extra">عيسى الليث - علي الديلمي</div>
</div>
<a href="https://t.me/naya_foriraq/85100" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇾🇪
ورسالتنا لعشائر اليمن الكريمة
#شاركها</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/85100" target="_blank">📅 18:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85099">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇾🇪
الرئاسة اليمنية في صنعاء:
لن نتردد في استهداف أي دولة تتعاون مع السعودية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/85099" target="_blank">📅 18:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85098">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الموساد: خلية ايرانية كانت مكلفة بتنفيذ هجمات ضد مسؤولين كبار.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/85098" target="_blank">📅 18:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85097">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇱
🇮🇷
اعلام العدو يتحدث عن إحباط خطة إيرانية للتسلل إلى إسرائيل واستهداف كبار المسؤولين.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/85097" target="_blank">📅 18:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85096">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇱
🇮🇷
اعلام العدو يتحدث عن
إحباط خطة إيرانية للتسلل إلى إسرائيل واستهداف كبار المسؤولين.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/85096" target="_blank">📅 18:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85095">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/103d326f00.mp4?token=T28iGbQSE-cfaXug04DignQcdTQkAKXICFtt9l7gdOcrWsEYyzyeHBohc4FA1wwfl0OdvMMUgB0sb5LsIkN0WIA5lQolA8FnAHwWN9sQGDl9wJb7Tp6GGtADe6CiQGN8CprHjgVkTSPv7e26kKkKSHK35HkLxCEdLKi9Ix_g0h951yaiHT9OMI8UlLiTu_ojDBndag1uC-38wrLt9VO65TwEx1vIPg8vAzzh1XbYcEwz3eFkVL9a6SJi5RCOWOIdcC2g2_rRBwUokgu1JpwyXhtxnA4UlBmASbD1V7Zcki4VEA1ow6ZPQ3wP4IfAzmGTYvea-clF6iaeeR1ZVKOqpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/103d326f00.mp4?token=T28iGbQSE-cfaXug04DignQcdTQkAKXICFtt9l7gdOcrWsEYyzyeHBohc4FA1wwfl0OdvMMUgB0sb5LsIkN0WIA5lQolA8FnAHwWN9sQGDl9wJb7Tp6GGtADe6CiQGN8CprHjgVkTSPv7e26kKkKSHK35HkLxCEdLKi9Ix_g0h951yaiHT9OMI8UlLiTu_ojDBndag1uC-38wrLt9VO65TwEx1vIPg8vAzzh1XbYcEwz3eFkVL9a6SJi5RCOWOIdcC2g2_rRBwUokgu1JpwyXhtxnA4UlBmASbD1V7Zcki4VEA1ow6ZPQ3wP4IfAzmGTYvea-clF6iaeeR1ZVKOqpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
استهداف سيارة للدفاع المدني اللبناني من قبل طيران العدو الصهيوني على طريق عام النبطية الفوقا - دار المعلمين وانباء عن شهداء وجرحى بالتزامن مع حديث جوزيف عون في واشنطن عن اتفاقيات مع كيان الاحتلال.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/85095" target="_blank">📅 18:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85094">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📰
وكالة رويترز تزعم:
أرسلت إيران قادة الحرس الثوري ومعدات متعلقة بالصواريخ إلى الحوثيين اليمنيين هذا الشهر.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/85094" target="_blank">📅 17:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85093">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icBJE2HDN2TuqOeSCqUh7x-bw_THVPRhB5xQ86ZJnbn4Ry4iEeSQoQKpguQtVV-wMDo8x8iwFzElUycMbAIhnv7TYuVc6WR71xn81Z2LSW-yvmLvThVm3wBTFcMDlO7fl4eC2zKLxW3cFWRvJmimbkS0Xj20T72ZZmjrXO8-Cl4FhEpVbEmIoPHypYdZPfOi2XLSst9TLNX6-2SfJqVPQosbsFdjMTx5rYPTpti3mpzuVHxsKhPBtA77fAPMEqWvJkDjh5zvfALZ-_jrV_y1KP3L6dlgTNyC_IoeEM1QAcczjna9WXvsHiSQ1h8Zc6Y0H5TnEWLFOsOcJlb4rfijHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هيئة الاعلام والاتصالات العراقية توجه تحذيرا لقناة سكاي نيوز الاماراتية بسبب استضافتها غيث التميمي وتدعوها لحذف اللقاء وتقديم اعتذار رسمي خلال (3) ايام</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/85093" target="_blank">📅 17:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85092">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇺🇸
البنتاغون يقوم بتحديث قائمة المؤسسات التي لديها أنشطة مثيرة للقلق؛ وتتضمن القائمة مراكز أكاديمية في الصين وروسيا وإيران.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/85092" target="_blank">📅 17:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85091">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
🇮🇶
توقيع مذكرة تفاهم بين العراق وايران لمدّ سكك الحديد من كرمنشاه - خسروي - خانقين - بغداد</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/85091" target="_blank">📅 17:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85090">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc04871c7.mp4?token=B9oOmiMi6tAirpg5kPRF9X8VhcXEoqYiTS5W6D-SrXhomdI1AN-L4dhtnE82U89k5T_aehy1nPEsyBK2_e7hHtY0ej7nBxbUetxlBcZGQsFhiG_prkDrO4fgIocM6NlDEoOKlwFG1Sem2wFZvX3ak1mJ3TpYOuz8rpVkdIKH3SS-iL6B0ZmLoKFoNhpFh1JX-cCpLGzM5XJKk6KSBvbqg8Cu7Xb_W5wcb_nVMqyTG3dwECXUyMsKK1UuuSrqnWcLdPI3W87hxNnEZI-LBcgiNTjK9tbL4fJLQ0C0m8hPvnD_v7CMV_tDb_rPkX5276nXC3NH13bDizGw_iyJw6idDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc04871c7.mp4?token=B9oOmiMi6tAirpg5kPRF9X8VhcXEoqYiTS5W6D-SrXhomdI1AN-L4dhtnE82U89k5T_aehy1nPEsyBK2_e7hHtY0ej7nBxbUetxlBcZGQsFhiG_prkDrO4fgIocM6NlDEoOKlwFG1Sem2wFZvX3ak1mJ3TpYOuz8rpVkdIKH3SS-iL6B0ZmLoKFoNhpFh1JX-cCpLGzM5XJKk6KSBvbqg8Cu7Xb_W5wcb_nVMqyTG3dwECXUyMsKK1UuuSrqnWcLdPI3W87hxNnEZI-LBcgiNTjK9tbL4fJLQ0C0m8hPvnD_v7CMV_tDb_rPkX5276nXC3NH13bDizGw_iyJw6idDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
صور تظهر هجمات الصواريخ والطائرات المسيرة التي نفذتها الحرس الثوري تحت اسم "يا أبا عبد الله الحسين" وهي مقدمة لزوار زيارة الأربعين.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/85090" target="_blank">📅 17:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85089">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇰🇼
‏الإطفاء الكويتية تعلن السيطرة على حريق منفذ العبدلي بعد عدة ساعات من الهجوم.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/85089" target="_blank">📅 17:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85088">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔻
حرس الثوري الإسلامية:
في إطار مواصلة معاقبة المعتدي والرد على ما وصفه البيان بجرائم الجيش الأمريكي، الذي قال إنه هاجم فجر اليوم طريق زوّار الإمام أبي عبد الله الحسين (عليه السلام)، مما كشف - بحسب البيان - عن حقيقته وأظهر للعالم وحشيته وقسوة قادته، نفّذ مقاتلو الحرس الثوري صباح اليوم، في الموجة السادسة والعشرين من عملية «نصر 2»، وبشعار «يا أبا عبد الله الحسين (ع)» وإهداءً إلى زوّار الأربعين الحسيني، هجمات مركبة أدّت - بحسب البيان - إلى تدمير وحدة الحرب الإلكترونية الخاصة الأمريكية في قاعدة العديري، كما استُهدفت أماكن إقامة أفراد هذه الوحدة، ما أسفر عن مقتل وإصابة عدد منهم.
وأضاف البيان أن برج المراقبة الجوية في القاعدة تعرّض أيضًا للقصف، مما ألحق به أضرارًا، مؤكدًا أن العمليات العقابية للقوات مستمرة.
ذكر البيان أن الولايات المتحدة، بعد فشلها في ساحة المعركة، تحاول مجددًا - بحسب وصفه - استخدام الخداع للحصول على فرصة لالتقاط الأنفاس وإعادة التسلح، مشيرًا إلى أن المسؤولين الأمريكيين يكررون الحديث في الأيام الأخيرة عن العودة إلى المفاوضات.
وأضاف أن العدو يجب أن يدفع ثمن نقضه للعهود، وأنه لن يُسمح هذه المرة - وفق البيان - للولايات المتحدة باستغلال أي وقف لإطلاق النار لإعادة ملء مخزونها من النفط والذخائر ثم استئناف الهجمات.
كما جاء في البيان أن الجيش الأمريكي، الذي كان يستخدم صواريخ كروز تُطلق من سفنه في المحيط الهندي بعد استئناف الحرب، لجأ أمس إلى استخدام قاذفات B-1 المنطلقة من قاعدة فيرفورد الجوية في المملكة المتحدة، بعد نفاد مخزون الصواريخ على تلك السفن.
وأكد البيان، مستشهدًا بتصريحات مسؤولي وزارة الخارجية، أن أي قاعدة تُستخدم لشن هجوم على الأراضي الإيرانية تُعد هدفًا مشروعًا.
كما وجّه البيان تحذيرًا إلى المملكة المتحدة، متهمًا إياها بأنها كانت السبب الرئيس في معاناة شعوب المنطقة، وبأن سجلها يتضمن - بحسب البيان - تقسيم الدول الإسلامية، وارتكاب مذابح واسعة، وفرض حكومات استبدادية، إضافة إلى تنظيم وقيادة احتلال فلسطين وإقامة إسرائيل، واتهمها أيضًا بالمشاركة في الهجمات الأمريكية والإسرائيلية الأخيرة على إيران، محذرًا إياها من الاستمرار في ذلك</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/85088" target="_blank">📅 17:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85086">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇱
مكتب نتن ياهو: انضمام المملكة العربية السعودية إلى اتفاقيات أبراهام سيكون قفزة تاريخية إلى الأمام نحو تحقيق السلام في منطقة الشرق الأوسط.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/85086" target="_blank">📅 16:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85085">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامب يقول ان الموافقة على النووي المدني السعودي كان بشرط تطبيع السعودية مع الكيان.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/85085" target="_blank">📅 16:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85084">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رئيس الوزراء العراقي: أمن العراق وإيران مشترك ولن نسمح بوجود أي تهديد لإيران ينطلق من الأراضي العراقية</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/85084" target="_blank">📅 16:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85083">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHCImkytt4A5yr5YqKjSUGHtzf4EAG7eSQqRuBpIkukTiY859o0kPfnk3Nsn6oe0iRZSALiITPj5VJMFY8M_OJ_w_aTVbx7jhNCmBkbJ1y4FBdGYbsCHPDUFYNlEIIE5pB3CspmMw5eLQy6KRG6lWW93AQCta23Gsw1tVlmkVBjtXhbNL5mxA2CipeDi3vpIhGPyGrlwp3GUOLhvv-V6cjdsa_pfiYTngflzICgy0Dx8bgV-mpUOFuyMN9957DX5vFPSA747Vrk0uLK3tjCO2QkKUDsgSfDpSwoRweDlcZnGG5gdmngks87ZB_e3pviVRXqcDVM8cYaRPxyD2nzZEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسعار النفط تتجاوز الـ100 دولار للبرميل</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/85083" target="_blank">📅 16:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85082">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الصين تصدر تحذيرًا أمنيًا لمواطنيها في السعودية.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/85082" target="_blank">📅 16:37 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
