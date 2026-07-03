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
<img src="https://cdn4.telesco.pe/file/P7nTMMYZW1uopl_LxhZtKZgHZpDaQ6rLs8PMneULNQ5ZkNWAMBJyePT2jv6Vx8xuFN3xTdc98P-GWwnWwmCzS2CugbgpEVkt9CUztCa0AWA1SooBI96HMX2MwS4I3WxHzuHkAUeas98vWhLiyHEb5GQAk4PMNF4QHQTU62TEerC53U_9sJq3rD0CbGgbYdUQ0VjjeDs9r_5qMF-wLKnk1SxVl-TAC0zBdVToHklHNpmuZauCXT63mQa0f0uZjx4ipF90BOtzxgDQ_zW1boo2ZVPPbCSXMT9IIC6gq_srQWqmx_nsvhpW-w0yxTvKHv9-Okdbtp6ppLRfsGeqH7-nDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 15:31:33</div>
<hr>

<div class="tg-post" id="msg-80771">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اعلام غربي: مشترين يابانيين يجريون محادثات أولية مع إيران لشراء النفط الخام.</div>
<div class="tg-footer">👁️ 605 · <a href="https://t.me/naya_foriraq/80771" target="_blank">📅 15:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80770">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7de078a47.mp4?token=pCvpA1D1G-cdwtKRxu6PCulSFRZ3gL_vX71UdSLQZ4oabuxZ8_6gs9bQp5RGKHPN1RfvF2zQhmAftJPiK21APNxMtrESVcksFYJtePCLnz315SU-Sym0E_BIKLlbmzrqDnhAkfg8y5LreynTx-AV2S8JqUDPKofy1-upTQhLly_lWHeihLWM42MnGRzpixPgQbjXCuJ68jckc4Ob5FW5MJBC8sye78-KfDsCOolC4x8ii2gcHlSj7lyYZPwh_ZM9UJq1YkPYGN3YhJ9MJiTUY64Lr10e98CroLqipJjzOeUgu_R6cSi0LWeb2rX9ct_RBqVdfUuYIhSQ9GbkAudx7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7de078a47.mp4?token=pCvpA1D1G-cdwtKRxu6PCulSFRZ3gL_vX71UdSLQZ4oabuxZ8_6gs9bQp5RGKHPN1RfvF2zQhmAftJPiK21APNxMtrESVcksFYJtePCLnz315SU-Sym0E_BIKLlbmzrqDnhAkfg8y5LreynTx-AV2S8JqUDPKofy1-upTQhLly_lWHeihLWM42MnGRzpixPgQbjXCuJ68jckc4Ob5FW5MJBC8sye78-KfDsCOolC4x8ii2gcHlSj7lyYZPwh_ZM9UJq1YkPYGN3YhJ9MJiTUY64Lr10e98CroLqipJjzOeUgu_R6cSi0LWeb2rX9ct_RBqVdfUuYIhSQ9GbkAudx7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد قرغيزستان يشارك في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/naya_foriraq/80770" target="_blank">📅 15:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80766">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qo5EHO9n3dnk-9ngpio9C3wuiZ6BqNWpxTFxQ14rvSQtMug9dTZ9lpOLlzwDIdvKK0kOJOyDOs-AUwh62IxiuJjYHodoTQMBcvOALFeYBRa6eOWgrD6s2ecKNtvQ0G2bCQTotEFlZXI_WSW4LaIhEJe6C2C0MFCsAg-irTd9LV4LC-vP5ZC7oSFCcp6KGAxwiGGWOjetWmOInqyhVjaTU2oCbOPbwNYUg7zFnyRFKjUMuykcmGkRVJHjFuMe0bR55xmOq9wyr_fbLGBwtpw8YjbZcBkluHKT115k2WBQab19xXepz1qSG0szefsa1RIEwN-jhHtQyW4gIo2j0586rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m6E4XySn8G_HuE1dsrwfCK74QG3L_bUvY9pS9L04nDKObf0P3TZXueRzlhsmQHt4Jg5YNxrtt0qyC8udt9g421mIFBJ-bXg5Mc4S1QPwbjjCqwgAevTV7bJih9NNLLc6vXRNBLxaZBnIq2k1fYju971S8QL-0h_Or3LVR0IJ5ygJN3mGR0UEFkjkz4keet9ZiXGBw9vqNYLq5gyIag-0NVVzKrVaDJzBDC4poIBHjEPem_-UYKQf1UPiFfVGW_NX7TKCKf38eNwkZYFIgx6h88ipiO1ETCDsxvnfdVSwXaCuLEytEsChvDrzFv3iEnOct8QtCqZtH6PiAkeLwnRkbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_eCH6Traf04675Bx--B9a9fYLWl2mrxURDeShVPAAKn_NUbeMFuLxs0OQNwpcmr27Ev33_7pdN_XgenxjgPWt-Ve8WxGWXTyCF5Ck0gTeVW596E7MIlsevTMJMqBR07qh-iYmjpY-69gx97nlwe1j0SLft41fLOFJN0y0zEPZOxDiLKNh3dSbYWx38yOwc__8ozYSub8DoHHarK-TnXhJmS_jyqyytoNhh4VUWQ3GThLDM0NiZmFPr9LgejV0SMiG0tLsQFd0-70pdf--DeM-IlrvMV5hXxLaD_UrH3atllA-LLBgpsMy3fCQeeQMG5iCI13rDHu4XThvRZNxqBLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G08AhgpPJ0YMLZKqfaYx1QpMpUSm9IG0oQKRcp4kQpRj8DXjHSFBaL9s7Yd6xSPYuKXV9Sv3KEivg69wh3--GgAaKaMaKbhTGEgPDjHKrKFhmoQOk0gueAhMi8WjEL6P0ianFeT5iX3Otiu6rml70sTXjjNvAErAajzBv8N5V3YRN0A9dQJLjjKg723nX4eenvs9YhAUM9ylkPK5fF1zj-IbcW7WpcVl1TLKbngGZWHzjzMjP2UUPwvbSwsxE09QJQH80RX_UUC4zWcswGFCmt89uvRAyunSf8JMxJvzE10izZKa0Og8Yif0R6YSdfJ24XQxfzhyQwOoKAOSBKR1uA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الخطوط الجوية السعودية تمنح شركة ماهان للطيران الإيرانية خمس طائرات بوينغ 777-268ER عريضة البدن مستعملة ووصلت اثنتين منها إلى مطار مهرآباد في طهران  ادفع يا طويل العمر</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/naya_foriraq/80766" target="_blank">📅 15:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80765">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الخطوط الجوية السعودية تمنح شركة ماهان للطيران الإيرانية خمس طائرات بوينغ 777-268ER عريضة البدن مستعملة ووصلت اثنتين منها إلى مطار مهرآباد في طهران
ادفع يا طويل العمر</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/naya_foriraq/80765" target="_blank">📅 15:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80764">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64825aa740.mp4?token=D3AYgBilgHu1C6EKXfx9hXvzIIDqqeZjLlVdydpjVdG0PZ6sbUNvItn_YBCMHxzJJas67pHyx01LyNYlzaiY6CsnkLk5tJl3WlzFkCLYh3jP0_cnJliGWwXwyXi3ddcYyFKASRMiegcqeHXnV9wHUs3hOri5bfIBPlJ9i5cQYUjkhtq2af_95JuA3_fsRfrtxMhL88aoYzn62xJvYAKTsr9B-FCPvyZ6khiWMHuWRjdThsljVNSG52GZ6rEmH8Ih_l0kiMEo1OboDvN3im2KFhBN6jSnrbrWa_E3RMbTGcFl7N1bbZNfgt-CrJwLR3tLlnVjUi9e_9gdtyd2Ymhevw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64825aa740.mp4?token=D3AYgBilgHu1C6EKXfx9hXvzIIDqqeZjLlVdydpjVdG0PZ6sbUNvItn_YBCMHxzJJas67pHyx01LyNYlzaiY6CsnkLk5tJl3WlzFkCLYh3jP0_cnJliGWwXwyXi3ddcYyFKASRMiegcqeHXnV9wHUs3hOri5bfIBPlJ9i5cQYUjkhtq2af_95JuA3_fsRfrtxMhL88aoYzn62xJvYAKTsr9B-FCPvyZ6khiWMHuWRjdThsljVNSG52GZ6rEmH8Ih_l0kiMEo1OboDvN3im2KFhBN6jSnrbrWa_E3RMbTGcFl7N1bbZNfgt-CrJwLR3tLlnVjUi9e_9gdtyd2Ymhevw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس اقليم كردستان العراق يشارك في مراسم وداع القائد الشهيد للثورة الاسلامية</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/naya_foriraq/80764" target="_blank">📅 15:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80763">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14db9faf02.mp4?token=n7f0gt8u7bKlvqOTUxHJVdzs08VWCqtO9-5ord20pK8PugsOx6vgIZ9BipxImgCfBwM7_AVsfAAknvw2CcwGZ0jfFx1UhOMWf51DstSq_NDXKf_uHtYzePELR6p-IrFnUBFosEFAqnvDaIa53iKAWaZrIGaOlmGnPx90Yus92SL7sdVUzeCNtLlBWexs5_RDpgDt-n6Ksc9fqMr67m1G2_gktPU0mGTP0UX9iACjK90PeOVJM7NUsx1j-K5NTCi7UeKN4ofIJO6jes90qhZ4__X9qMhgVmToBSfPmEvhyGVVJjxMB7TTGAtxrlok8BvFMhUrSlMCGFunNqAjni1nDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14db9faf02.mp4?token=n7f0gt8u7bKlvqOTUxHJVdzs08VWCqtO9-5ord20pK8PugsOx6vgIZ9BipxImgCfBwM7_AVsfAAknvw2CcwGZ0jfFx1UhOMWf51DstSq_NDXKf_uHtYzePELR6p-IrFnUBFosEFAqnvDaIa53iKAWaZrIGaOlmGnPx90Yus92SL7sdVUzeCNtLlBWexs5_RDpgDt-n6Ksc9fqMr67m1G2_gktPU0mGTP0UX9iACjK90PeOVJM7NUsx1j-K5NTCi7UeKN4ofIJO6jes90qhZ4__X9qMhgVmToBSfPmEvhyGVVJjxMB7TTGAtxrlok8BvFMhUrSlMCGFunNqAjni1nDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السيد هادي خامنئي، شقيق القائد الشهيد للثورة: الشهادة كانت الأجر الأمثل له.</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/naya_foriraq/80763" target="_blank">📅 15:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80762">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ab2eecaf.mp4?token=Ydrn1Wah5UC4hgYsOpla82BrkwPcJu2aAOA62V8m1TBvXcC-j9RT7fleT11ESoSnA0Qmxmmuo0xstej1clXIPLZa0DUUfqVLQtIbKWPbCPAl-S6Vn23gPnBJR_xe7mryxzTB5waD_LGvhuRM4Ne0wc2sLaTCEuS5pqoFzL5iWJtxh7QPq59Uv9rzKE_UlU4KglVJBmZLV5T-qAcrvfVxuAZc874-AjSZhcOtrDcdDmIxFEKcIuKT9SXyNVDGHuV-bEhFrqDKl854_SmrKYorMrkcsFCFjpdvtSgErNzFkeeIc4oyRJymWdwMx482rrs0TyEO_FStMDr4AAAf9pwukw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ab2eecaf.mp4?token=Ydrn1Wah5UC4hgYsOpla82BrkwPcJu2aAOA62V8m1TBvXcC-j9RT7fleT11ESoSnA0Qmxmmuo0xstej1clXIPLZa0DUUfqVLQtIbKWPbCPAl-S6Vn23gPnBJR_xe7mryxzTB5waD_LGvhuRM4Ne0wc2sLaTCEuS5pqoFzL5iWJtxh7QPq59Uv9rzKE_UlU4KglVJBmZLV5T-qAcrvfVxuAZc874-AjSZhcOtrDcdDmIxFEKcIuKT9SXyNVDGHuV-bEhFrqDKl854_SmrKYorMrkcsFCFjpdvtSgErNzFkeeIc4oyRJymWdwMx482rrs0TyEO_FStMDr4AAAf9pwukw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الباكستاني بقيادة رئيس الوزراء وقائد الجيش يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/naya_foriraq/80762" target="_blank">📅 15:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80761">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPm85U35oVYFmwa20SWbx6I54WGhFi2hBUP8KoFouEcL1tNc6fA7N38_cMB_MP5Zk4H-RuwVtfOGbMPzk2gvpku12p2PRmd90pCS0cBF7QoVd_5XO2peg7rkNeGcGdqLIFTcy8NmzPuwOH7r6YicTjYrRZJn3LAO5ZWecOm0ghcxb1n9iPNbeXk6ybPhHHU-L1YDEgmvDF850BMjzFXXzZqT5NI-ir0Nfk1jiq70IawMvOKmi9AWVtW7nHaPuFFVBuEBZaqt0WiN4S2QeEN7OUIVp5gN08A7bGruht3DEiQjgF8w0K3T2lSYfjPYIRXc5ZEII1dTIgsMr_p-VcJJ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئيس السلطة القضائية الايرانية يوجه رسالة إلى القادة السياسيين الغربيين:
افتحوا كتب التاريخ، الأيام القادمة ليست مجرد مراسم تأبين؛ بل التاريخ في طور التشكّل. عندما يملأ الإيرانيون الشوارع لتكريم قائدهم الشهيد، لا يمكن لأي إطار أن يحتوي على حجم التعلق والولاء الذي يكنونه لقائد الثورة الإسلامية.</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/naya_foriraq/80761" target="_blank">📅 15:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80760">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrDERSv3NuP0g1xGozIMjpH89Aioi3CM7rLoNqDaGUsXlMQatAFhmZnzv30qU6X3NufFWhRDLAI72Q0tZ1AMM19eKGDy7dOJ5KxgpQ5qHuWBQmxge-Hx2BjxJof87AckYLyK8VUajO4KR-gmTkF6XUvLz_mSRx6diqxBWoIp5buX76f1Py7kT0_lYLg67T0obckwELxkmz_lxz2xttZ7Ih8GZWQB-rrtxRRBe5o0ofPoDqHanw-4gpoZ812z_ROxtVn99VPaJEgHcJtao1j-Fg9DU8C5PmKW075u9DHX7ZyRGYrBqf2ExM6X_9KgFStXfGptL71t4GJ1vYwS5Kpusg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرتين روسيتين من طراز إليوشن Il-96 Il-96-300 تتجه الى طهران.</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/naya_foriraq/80760" target="_blank">📅 15:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80758">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LaRxvMGd0cd7_Z8TyZY-tXYwOrJky7BueWnEEfTW5BT15LWy0xJ9t1bdS6pcVyyFeOvM7LF6Jln1dZD7WWtnOj8WRnkwNaPMw98xuVARhy-WACwUaPCR0ryC7tll_zE42Xr3ppZ_gAX3NgvHxNVWy1P-z_L2ooJtWh3w-CfzvlPVFngBQ_W9AFMOcLeFws4cL9enoJMo7TEV35Sj4JUu-HhEwoF-vLtHl-FIp2riIFr2h2bEM6PYrUuMd9fyJzdOKqtLRU5y1Shdn8smoYyFOX08SX4rG5VyTJyZSkA0EDjMAX07ym68hTzFkCozGli2A--W2yW4aa3TRQ9kyWVmrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mG17GXvvxLU5IoACp2OjFAmzqOcl19gEY_P7Lqp5s24ONDtuebtURYKeiBLIlbMiprYbnCQCCtCFJcoskoj0OykTuQ0Vkqd-jWkfu7CzMAePmRAfjy6cfv7o1c5F6qiLE6HWE1KastJ1lhe-7HT_x1HfyrQHFWz2XoFwUKerrmZhAt1hbXkUW4N31QFDhVrxKRU18QkCsdbqFqPFw7ue3ZNfMOcSZSm-MdGzZ_Jdokyxzgo12Z0h6xMbYYIAr_-ctUDxUVhr8fmWNwsW2ucLSOt6vH-YaCSWy8CyJYD_Qfo4EehDQ0r64-Evep1sbfIPTeTLml32OtaUbiiug-mJ-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حضور علماء أهل السنة في مراسم وداع القائد الشهيد للثورة.</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/naya_foriraq/80758" target="_blank">📅 14:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80757">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3391779aa6.mp4?token=mCXnx6JUuItO0jqBl4cRS4klE9rutloBCOzlLB6CRk-itH_NULdXMX3oxGkl_2eCQ017PjNsaJ01EqgWiAc2uM24tuvyf47E_dyiUb6doaUO3yfdLRhwVtmCEIMIiB8x9pmxZk8LUr7hWmwRh8ZTMRvZCgv9MBwKA8R9GrNtl_FsDTF6bmIp-bJe9QqR0RRNOdR1wbiGQTCtnX0CgxdkPN4kL4vweIGyflmdT3oByTrBOG_t0hJyRLxZ2oBLFG5N3eCeRzwySgXyLWiXvoA4iutxvMSZveQgoXfn3VlqOEpKKE2D5-QoMd3eRpQQIFxPrEWSICd7XFMiqGhguiQ6MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3391779aa6.mp4?token=mCXnx6JUuItO0jqBl4cRS4klE9rutloBCOzlLB6CRk-itH_NULdXMX3oxGkl_2eCQ017PjNsaJ01EqgWiAc2uM24tuvyf47E_dyiUb6doaUO3yfdLRhwVtmCEIMIiB8x9pmxZk8LUr7hWmwRh8ZTMRvZCgv9MBwKA8R9GrNtl_FsDTF6bmIp-bJe9QqR0RRNOdR1wbiGQTCtnX0CgxdkPN4kL4vweIGyflmdT3oByTrBOG_t0hJyRLxZ2oBLFG5N3eCeRzwySgXyLWiXvoA4iutxvMSZveQgoXfn3VlqOEpKKE2D5-QoMd3eRpQQIFxPrEWSICd7XFMiqGhguiQ6MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الطاجيكي بقيادة رئيس الجمهورية يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/naya_foriraq/80757" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80756">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZwW7TjJTcYCWBc2vJOw_-hr-mXg_5p-obrsFdCbY8LNagLk2FOxF_daQruiM-zGHO4hJCkNd4blBNrF9emUqScw_FjY0awk9JKSzr3SyZuv6-xuDddkwtiT2zB1fYZKyZLSBWZV9Q9p03mbqLYeT6YEAq4au_dgGHz3tgKJpv2x_wj8oNetfI2MFjaWOkbAMxGoWqCItuS31ziL_JZnArFLIg-vWTxmGrukb1z6Bx0jf1sLY7X8dpec7zFp_S1XirTdyYPkq_ft266gMGgjQAq41hyfgCCtt1vg8oeI--6FkcXmfW8GM-v4-dDfVrYVuHPduCV0GiedYoqu6OPubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجمهورية الاسلامية تضع صور شهداء مدرسة ميناب عند مدخل القاعة التي أدى فيها المسؤولون من الدول الأجنبية احترامهم لجثمان القائد الشهيد، في مصلى طهران.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/naya_foriraq/80756" target="_blank">📅 14:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80755">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5996e691.mp4?token=LYU-8GusugkaqYBKJeECBxvRYtXPkCUCOLyWIHBngmYVt7hgUM383JuEGsjBdv1Li64WJMxPFfbqefc7ZTAMNbWuK4RuFK3N9bfs62Iid94SE5op48M79o2CifBrUZJ2bzneOMAuXKihZoXzuMTIB-BmOwhA47YlKkXfxdJn82r6hruU1RJTgrceXEc6EN7QPttg6ZS3hbl9clKcpyqnDD8DL8BM0WNyOLouxJWzMnsrvnKzmEdtONnaWIfxZhVIf5ZibvTz8FYpzXPDaqlQiZiDjPlGPakTVIwSOFYWPdYLTqVXvWv59qNKF2-hz8DSCerw0NfmeTSszOkdWTEPmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5996e691.mp4?token=LYU-8GusugkaqYBKJeECBxvRYtXPkCUCOLyWIHBngmYVt7hgUM383JuEGsjBdv1Li64WJMxPFfbqefc7ZTAMNbWuK4RuFK3N9bfs62Iid94SE5op48M79o2CifBrUZJ2bzneOMAuXKihZoXzuMTIB-BmOwhA47YlKkXfxdJn82r6hruU1RJTgrceXEc6EN7QPttg6ZS3hbl9clKcpyqnDD8DL8BM0WNyOLouxJWzMnsrvnKzmEdtONnaWIfxZhVIf5ZibvTz8FYpzXPDaqlQiZiDjPlGPakTVIwSOFYWPdYLTqVXvWv59qNKF2-hz8DSCerw0NfmeTSszOkdWTEPmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد البيلاروسي يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/naya_foriraq/80755" target="_blank">📅 14:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80754">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a80961d7a.mp4?token=KV7GIxwkdZ6neWhcW1_G6lANi00gmD3sVf-a-TQVFhFPBiAm7udYEg5iFjimSGeIoxX23gAd8LjKf1rRBQFmFxiKAPIwNGoIbT1ypTXnKmYybIrOqCA_nYWtP5U0VSflqWX1ibXU67frBScJ01lqQcx6LrwSsMZZy8sjeaL-1t8_ZMUy3N7W23w0n7q-vfLqg96mW94GcCPufokkLcgZIh-kmAkKsoiVELlyvxBxbtUikCPbc7L8b_9U7mgRLYYxFMvw-ByAIp-khoiKWHB304vzUPItpXAa04V2bcMeb8YLGmw4LCK2Zf0IWpEv31FdSHDpWel3oEr0brhbLpzW6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a80961d7a.mp4?token=KV7GIxwkdZ6neWhcW1_G6lANi00gmD3sVf-a-TQVFhFPBiAm7udYEg5iFjimSGeIoxX23gAd8LjKf1rRBQFmFxiKAPIwNGoIbT1ypTXnKmYybIrOqCA_nYWtP5U0VSflqWX1ibXU67frBScJ01lqQcx6LrwSsMZZy8sjeaL-1t8_ZMUy3N7W23w0n7q-vfLqg96mW94GcCPufokkLcgZIh-kmAkKsoiVELlyvxBxbtUikCPbc7L8b_9U7mgRLYYxFMvw-ByAIp-khoiKWHB304vzUPItpXAa04V2bcMeb8YLGmw4LCK2Zf0IWpEv31FdSHDpWel3oEr0brhbLpzW6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الارمني بقيادة رئيس الوزراء الارمني يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/naya_foriraq/80754" target="_blank">📅 14:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80753">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0a7346f1.mp4?token=INSTT7qSrMGFBi9KsYVcvKmHFgaMCq1SoUvb14hcqiRbNeg_OJYIH5oX0rpUWtHhmT2HOstNZw7CSpEExYWTrCU_R9nBKLQZVHApdsqHafNZDex0eBfT02pLq1JbqG1CiSuIRAMs1A9zozk6p6kZgbHoJjsVwfGk2xvmmA4D3YMNzM5BALKiEogM8Nb7Ag8PBkAJfnofEyX1C6B5zjwil2UfY8bxAkIVC5McMHD2nCKMCSoUvE8THeVkKx5uLoBIYy5cX7RWg70XHAzJAz7B7dLKEtHuPBx_RWQ2e9qZZKrLzs8_nWI06d5XpK94lZSFl9WXUKh8-KQ42YvPdyco2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0a7346f1.mp4?token=INSTT7qSrMGFBi9KsYVcvKmHFgaMCq1SoUvb14hcqiRbNeg_OJYIH5oX0rpUWtHhmT2HOstNZw7CSpEExYWTrCU_R9nBKLQZVHApdsqHafNZDex0eBfT02pLq1JbqG1CiSuIRAMs1A9zozk6p6kZgbHoJjsVwfGk2xvmmA4D3YMNzM5BALKiEogM8Nb7Ag8PBkAJfnofEyX1C6B5zjwil2UfY8bxAkIVC5McMHD2nCKMCSoUvE8THeVkKx5uLoBIYy5cX7RWg70XHAzJAz7B7dLKEtHuPBx_RWQ2e9qZZKrLzs8_nWI06d5XpK94lZSFl9WXUKh8-KQ42YvPdyco2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سائحة امريكية تتعرض للضرب على يد عصابات الجولاني في محافظة حمص السورية</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/naya_foriraq/80753" target="_blank">📅 14:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80752">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e8c7e0e1.mp4?token=jKPrCoXgMplS-YDCejh4qZBArzVxtffZTtFHVltPVkAmM1JUZTWUQNWvCfQu15-6ABDAbJ3-l0HRPPzc4QHTHHw3sc8qv5EopPoyLj97D2fbXch5ngtxd7fNO3wd2Ko13Wd7tIevcdF8_-4Bk8c_moWzApgU_ShAsLnMliDCYfTpinAMBAeXWzPCDZpqUSyAqZCh8p9AbSkSItbDouMAGUORjQ55gNBmBiQUAbM8snC-DmUPqzWdHPGiMHbZOQWjDLqapLe5EaviZ4jPjI0QjccRkusUN0kgIBGoUW8JzCfwf3j8ShEvi73ri81cz1JCss63Dsk7_HqOJVpMFCGFUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e8c7e0e1.mp4?token=jKPrCoXgMplS-YDCejh4qZBArzVxtffZTtFHVltPVkAmM1JUZTWUQNWvCfQu15-6ABDAbJ3-l0HRPPzc4QHTHHw3sc8qv5EopPoyLj97D2fbXch5ngtxd7fNO3wd2Ko13Wd7tIevcdF8_-4Bk8c_moWzApgU_ShAsLnMliDCYfTpinAMBAeXWzPCDZpqUSyAqZCh8p9AbSkSItbDouMAGUORjQ55gNBmBiQUAbM8snC-DmUPqzWdHPGiMHbZOQWjDLqapLe5EaviZ4jPjI0QjccRkusUN0kgIBGoUW8JzCfwf3j8ShEvi73ri81cz1JCss63Dsk7_HqOJVpMFCGFUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الاذربيجاني يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/naya_foriraq/80752" target="_blank">📅 14:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80751">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">لجنة مراسم تشييع وتأبين قائد الثورة الشهيد: سيتم فتح أبواب مسجد طهران الكبير أمام المواطنين غدًا ابتداءً من الساعة 6 صباحًا.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/naya_foriraq/80751" target="_blank">📅 14:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80750">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">لجنة مراسم تشييع وتأبين قائد الثورة الشهيد: سيتم فتح أبواب مسجد طهران الكبير أمام المواطنين غدًا ابتداءً من الساعة 6 صباحًا.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/naya_foriraq/80750" target="_blank">📅 14:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80749">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رئيس البرلمان العراقي يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/naya_foriraq/80749" target="_blank">📅 14:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80748">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dbbcf836c.mp4?token=p12dCtJMkwnu3-09cBedid0kvtxjZMIIvQ3J14ZPr3ftctQrS_be4IIyVTI5z9PyoTH-qKXeobeIjniXnTjTiK31RUdR83caS-CAmV7nZ-JSELfsCv23lJejwcHL0UiIsFygzKBv6DWI8ukoIa7-o6qmA1lIJym0OZ__Oa41P-vLwfNHvvZrRBuu8Lhw6wiGPVWNtJSh-Q6ANj4_8AGeO_nDJ8LGFEqwzMFzDntaoCMhsNzeo1Q74tmzpBcoikUpkmQ7Re59WzJ2ATps3Mk61fCdG_7oVlrgIbDbV-RG78DMzrdrgHUTRbpwXjll1SApbZFRWnlTixuGNBasgxaN4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dbbcf836c.mp4?token=p12dCtJMkwnu3-09cBedid0kvtxjZMIIvQ3J14ZPr3ftctQrS_be4IIyVTI5z9PyoTH-qKXeobeIjniXnTjTiK31RUdR83caS-CAmV7nZ-JSELfsCv23lJejwcHL0UiIsFygzKBv6DWI8ukoIa7-o6qmA1lIJym0OZ__Oa41P-vLwfNHvvZrRBuu8Lhw6wiGPVWNtJSh-Q6ANj4_8AGeO_nDJ8LGFEqwzMFzDntaoCMhsNzeo1Q74tmzpBcoikUpkmQ7Re59WzJ2ATps3Mk61fCdG_7oVlrgIbDbV-RG78DMzrdrgHUTRbpwXjll1SApbZFRWnlTixuGNBasgxaN4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس البرلمان العراقي يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/naya_foriraq/80748" target="_blank">📅 14:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80747">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇷
المتحدث باسم لجنة مراسم تشييع القائد الشهيد:
هناك احتمال لتغيير المواعيد؛ فمع أنه أُعلن رسمياً أن مراسم الوداع الرئيسية ستبدأ صباح السبت، إلا أن أبواب "المصلى" قد تُفتح أمام عامة الناس الليلة إذا كان ذلك ممكناً.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/naya_foriraq/80747" target="_blank">📅 14:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80746">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo71ZhiU6V5afsFifru_NapO_y4Gfx4h_gNaEOPHbfre_V2Qq-w3qCKEyGsvMjuT282pOr06RT-V4_2o3D0bHXtkKnJrK_u_ZiwJzE8Lupj6_C2fzV13cYNijRWY8BnL4Rc8sDxmtawANjHmOvsLlh7aFOWL-VvfwA8y_sfdhO_3EzCYxUzooMamIBL-XPUOY8QOzsa4X-AU5Wo8idA8tXE-XCKUh8XiINr7pvHa8kyBTpOwX54YIJdWKmQ5Fbk0wG6At7rdmVSUHkDFHF3IF-AUFVMIgZQzF6YdQL-mBCvN2oav_iSXvhgjBYsYBqrW9xga2yaNOHhCKeJeTl2V6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
نسأل الله الصبر لكل المحبين
يوم الأربعاء
النجف الأشرف ٦:٠٠ صباحاً
كربلاء المقدسة ٤:٠٠ مساءً
#قوموا_لله
|
#باید_برخاست
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/naya_foriraq/80746" target="_blank">📅 14:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80745">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌟
الاتحاد العراقي لكرة القدم:
تشكيلُ لجنةٍ للتفاوضِ مع مدربِ المنتخب الوطنيّ الأستراليّ آرنولد مؤلفة من رئيسِ الاتحادِ يونس محمود ونائبيه من أجلِ ترتيبِ الأوراق، وإكمالِ عمليةِ التفاوض بغية استمرارِ المدرب مع المنتخبِ الوطنيّ
المكتبُ التنفيذيُّ للاتحاد يوافق على حلِ جميع الملاكاتِ العاملة مع المنتخبِ الوطني
العمل على الإعدادِ لمؤتمرٍ خاصٍ بالمتخصصين في كرةِ القدم والأنديةِ وأهل الشأن للخروجِ بتوصياتٍ ومقترحاتٍ تهدفُ إلى تطويرِ الكرة العراقية
تشكيلُ لجنةٍ لاستضافةِ بطولةِ غرب آسيا للناشئين التي تقام في 24 اب المقبل في العراق ورفعها الى المكتبِ التنفيذيّ لغرضِ توفيرِ جميع مستلزمات نجاح البطولة
السَعي إلى استقدامِ مديرٍ فنيٍّ أجنبي يتمتعُ بخبرةٍ وقدرةٍ عالميةٍ لتطويرِ ووضع البرامج الكرويّة الهادفة إلى تعزيزِ قوةِ الكرة العراقية من الجوانبِ كافة</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/naya_foriraq/80745" target="_blank">📅 14:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80744">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مصدر روسي لنايا : المجاهد الكبير ولعنة الناتو دمتري مدفيدف سوف يشارك في عزاء السيد القائد في طهران</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/naya_foriraq/80744" target="_blank">📅 14:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80743">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd34ffceb.mp4?token=huK0_tb_xk8_x6DcejHhZaYEo7NezKQS7gVBgga7z350c8a3_NFOZl4YBv0AJU5oFZBLD2Ng1LXPN2z21WJFs_7fpBGSbjH2K5cjZmpcHWo45LOoMLlmftf1GrgO6pHSQJH8sO7A16LRetsDq4MqEBFvA1iEXO4fmR5IoEqukWQofqhv8kTSXJoiDIT3ao64p-tVb6gVI-LgOLenTv9JTB8bDaKlOU_o2OFrp8DS2g31fafHrBq8Getd9vpjMIlLs7F74qj0KqGngfS_W3jKjUQNYKOZ4nc4mHSicO4lc5tP7_h1qXhQK5ylmUR0IIJC8T8uQzR1RmxEP0pgkpnlpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd34ffceb.mp4?token=huK0_tb_xk8_x6DcejHhZaYEo7NezKQS7gVBgga7z350c8a3_NFOZl4YBv0AJU5oFZBLD2Ng1LXPN2z21WJFs_7fpBGSbjH2K5cjZmpcHWo45LOoMLlmftf1GrgO6pHSQJH8sO7A16LRetsDq4MqEBFvA1iEXO4fmR5IoEqukWQofqhv8kTSXJoiDIT3ao64p-tVb6gVI-LgOLenTv9JTB8bDaKlOU_o2OFrp8DS2g31fafHrBq8Getd9vpjMIlLs7F74qj0KqGngfS_W3jKjUQNYKOZ4nc4mHSicO4lc5tP7_h1qXhQK5ylmUR0IIJC8T8uQzR1RmxEP0pgkpnlpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد التركمانستاني يودع قائد الثورة</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/naya_foriraq/80743" target="_blank">📅 14:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80742">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXCzXYm7SysS-R9UaEYtJIkIVmd6hrozWUe8LCawihjzl7b1culBm1kX6M3Zr8z5X9xRyeVD3groChhWa_J4L7M-bn6rWrW8TDShGPE2oYoce_bDVJc0BDqdq3wio53c2njGBDvAPsjbtvYRjON3BO68Zka_EHkQTQGMQ_1kuryS_qHFjUN0OGBV6H40HY4alXwXnAWU8s154SgJZhTw_auZHPZrblLhYMXq2n9PmgqPomWyxLGY5_-2wn-SO0VpSRnmcNqB5Es0cPExr2Sb8Lscvhi0sIHOAGyEl9YWsABo8ZymqIvbXfSoLXCCZQTF-ElHICxgCNQRl_BCKcSA8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشيخ اكرم الكعبي: المشاركة بتشيع الجثمان الطاهر للسيد الشهيد القائد الخامنئي (قدس سره) لا تقل عن المشاركة في محاربة هؤلاء الصهاينة الأرجاس في ميادين الجهاد.</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/naya_foriraq/80742" target="_blank">📅 14:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80741">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5587a3fe4a.mp4?token=C0oUvGk4CPZNZfjRS2V9eqZNPke_uxQssmXLVc0jbbgCwr0LBjYvvr8xtI-SrB_sceA4ubHeCD9y77d3v_wnKIsHh8uFH59jLBl6MdMMkBVxmiE9Dah26AYJaylq6E4HVFn5cIqFr_l8WWkXLylml_kcgsbS83FhKg95PCxShMg1s3qpZayHc-Bl3fddUo1zUtTdCsYGc__8jSYg5urQoJ0hw3ZeOBS05qpkrnj2SlBRb0mY549BCqaKeZ5hAZ4qLf2bVjhJ8cgzO3tNpdwFpDEL5-9aFyCdc3Htj1WEqbIZM5aozvRnJ8R3RHt3FjATxVkIc57Atb9ckgBN1EKOMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5587a3fe4a.mp4?token=C0oUvGk4CPZNZfjRS2V9eqZNPke_uxQssmXLVc0jbbgCwr0LBjYvvr8xtI-SrB_sceA4ubHeCD9y77d3v_wnKIsHh8uFH59jLBl6MdMMkBVxmiE9Dah26AYJaylq6E4HVFn5cIqFr_l8WWkXLylml_kcgsbS83FhKg95PCxShMg1s3qpZayHc-Bl3fddUo1zUtTdCsYGc__8jSYg5urQoJ0hw3ZeOBS05qpkrnj2SlBRb0mY549BCqaKeZ5hAZ4qLf2bVjhJ8cgzO3tNpdwFpDEL5-9aFyCdc3Htj1WEqbIZM5aozvRnJ8R3RHt3FjATxVkIc57Atb9ckgBN1EKOMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول رئيس الوزراء الباكستاني الى طهران</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/naya_foriraq/80741" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80740">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6906509da4.mp4?token=QL_PTa7KWyzDYoQYaleR7XXNOEN-2gpcoQ9_uKJvQlW8qdIyVOwI_QFa0j12VDeMBvmrecB-79BmAegHwoXVawQzo7MYwJ--unEAciriHJciBWJW3-pCU5wRZUiyV_J5XLFDwbMn2MGcEA6miZt4EGPl_ewDNhY9atU7DqbvhcJS4ihDKEEe8XIQTv8qGP7DEqfxv_1Xe0MEA48CHPWCE1yakp4YCEQdMq5PP_RAlwg98a6CbuSX_W1R3UWeCBrwC5cYPI3P0l9THK-Iyp2KHNpA06xnb1zczz_2CiP9lXzWjuoIguag08i33KOYlHB7NshpUaz1GdCd72CVWpf_GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6906509da4.mp4?token=QL_PTa7KWyzDYoQYaleR7XXNOEN-2gpcoQ9_uKJvQlW8qdIyVOwI_QFa0j12VDeMBvmrecB-79BmAegHwoXVawQzo7MYwJ--unEAciriHJciBWJW3-pCU5wRZUiyV_J5XLFDwbMn2MGcEA6miZt4EGPl_ewDNhY9atU7DqbvhcJS4ihDKEEe8XIQTv8qGP7DEqfxv_1Xe0MEA48CHPWCE1yakp4YCEQdMq5PP_RAlwg98a6CbuSX_W1R3UWeCBrwC5cYPI3P0l9THK-Iyp2KHNpA06xnb1zczz_2CiP9lXzWjuoIguag08i33KOYlHB7NshpUaz1GdCd72CVWpf_GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس البرلمان الإيراني السابق غلام علي حداد عادل يودع قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/naya_foriraq/80740" target="_blank">📅 13:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80739">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYne25Fq3ACaWf3XcTEbbGT-N-hjz2_sK9uWIrdUNcnBsHQce2xA9E2yp4Ye1kHIWY79EYAi8jDl91FKpv7uf-tjuYCG9lO-uU5UOoL9CwVDXDWqz1WXYcrCPsq-ig1xLqULxcM0pkyn9mOSoXwYQeUGQqosstDF93Apls7gmzfzkJLwNT-NpWaViqo5t3WHlwQ8ilhmWgXIf1Ns5VciGjr4PIkgXaTh5cs6uddlaf1zl5ou2cGj0Kwk25vte2A8GZeqwctFw9VXGSlO2CeH310zEa7pLXaSqQI3O50vXOkrExc6YUpynQ1vY9QyzhUfW8epMbNGTJ4aOfHgy3xUlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من وصول احد اعضاء الوفد الباكستاني</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/naya_foriraq/80739" target="_blank">📅 13:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80738">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b419c1671.mp4?token=oXIaMKDmPS-cvhhW0qVltUWpraV4gphWFZlExeMpy6ESij5gPk6InJEsdoGv5fRAXjRWiNWtWl6ukbqSD1fwOLGPbuw4qAR4RsPAljLY0kDNnWfR7Lg7XLYhq5mo2Vv4vHMReENNe2-fyFsGkdQPCWnt5dU9rCM5jrd3vEKQTgt1f8e4PuGHMzZcNnY-2JAgSZepioaUOMP7JPec1GIYKMWOvoIfI38IkAr-9WQCdsnoAAcbg9i2AKtoy60EHRP36YXgugAjTVFJ-YBcBo1Ypf3AGp6osMjlF2ZHVNW5Z-IR9qe5OFIIx9ZE9Lk-VsJBxlrBjfQ2K0kAAap14c7MBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b419c1671.mp4?token=oXIaMKDmPS-cvhhW0qVltUWpraV4gphWFZlExeMpy6ESij5gPk6InJEsdoGv5fRAXjRWiNWtWl6ukbqSD1fwOLGPbuw4qAR4RsPAljLY0kDNnWfR7Lg7XLYhq5mo2Vv4vHMReENNe2-fyFsGkdQPCWnt5dU9rCM5jrd3vEKQTgt1f8e4PuGHMzZcNnY-2JAgSZepioaUOMP7JPec1GIYKMWOvoIfI38IkAr-9WQCdsnoAAcbg9i2AKtoy60EHRP36YXgugAjTVFJ-YBcBo1Ypf3AGp6osMjlF2ZHVNW5Z-IR9qe5OFIIx9ZE9Lk-VsJBxlrBjfQ2K0kAAap14c7MBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عائلة الامام الخميني تشارك في مراسم وداع قائد الثورة الاسلامية السيد الخامنئي</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/naya_foriraq/80738" target="_blank">📅 13:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80737">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خلية الإعلام الأمني في العراق: لا حظر للتجوال أثناء مراسيم تشييع الشهيد السيد الخامنئي في العراق.</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/naya_foriraq/80737" target="_blank">📅 13:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80736">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خلية الإعلام الأمني في العراق:
لا حظر للتجوال أثناء مراسيم تشييع الشهيد السيد الخامنئي في العراق.</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/naya_foriraq/80736" target="_blank">📅 13:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80735">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d66cfc76b5.mp4?token=L1gS8lCBsm7Ao0epGzqe3zJhgDfRuT8FwWHPyPr1IJGOeaIxdX4Etq4uqC610qMfeyD56KrtQGzmpUvD1Lq8WaOJwRyFRetgz7IjM6hPZeQKhxqBwE0MBVdMEKxxHkE5Cx-xd8vi_iqhBYb6obT3NqLry2x18APOauEogqe08iPKOljuhrSyOXpN0HcBAItsK_pOr7e6wP9l34V6pGTfX7FrjkOEw4f2nMXNU738imIY5UzR25afZgZVsSMS-mxx-Blp-pIWuW_zk4hsiSSm5S97j7a5jWqJ1rM36sELuqxKkrGnFnjmWcyBf_gaa1woUaFLVu7C-cD7XEWudOuJ4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d66cfc76b5.mp4?token=L1gS8lCBsm7Ao0epGzqe3zJhgDfRuT8FwWHPyPr1IJGOeaIxdX4Etq4uqC610qMfeyD56KrtQGzmpUvD1Lq8WaOJwRyFRetgz7IjM6hPZeQKhxqBwE0MBVdMEKxxHkE5Cx-xd8vi_iqhBYb6obT3NqLry2x18APOauEogqe08iPKOljuhrSyOXpN0HcBAItsK_pOr7e6wP9l34V6pGTfX7FrjkOEw4f2nMXNU738imIY5UzR25afZgZVsSMS-mxx-Blp-pIWuW_zk4hsiSSm5S97j7a5jWqJ1rM36sELuqxKkrGnFnjmWcyBf_gaa1woUaFLVu7C-cD7XEWudOuJ4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تركيب تمثال "قبضة يد مشدودة" في ميدان انقلاب في طهران تجسد وضعية يد الامام الخامنئي في لحظة شهادته المباركة</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/naya_foriraq/80735" target="_blank">📅 13:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80734">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87b6d075f.mp4?token=UpFqBrACMbRQcgE65IGFfIXGWgUqqEH8Tr8_khWBC1siplddGCvCpT3JuH9axD4t4b-dZxazIkhy66ZeyEhdR5bC2VYIDVxRpaFlDHuxBZdeIVPimz40VpagupKG07lxM_FOQU8TDRHT3laoQkrk2a0dbQQcD3atEdiJ-qGCdBExzFLCkygmgra8Imzck3nUupXrz79zaZ0P3NhZk1X45O0XaPe_mdoP63Hj7B-9IuC1blhZx9tUUVcnw--9X7_cW5ynb7Y9_Un21PwDQYCTCslAKofWJ_Enxt7jyVmlLwYc2-2sWupjpt7MzrYLESUYNMMQpyrGWnQWo03n1GqZvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87b6d075f.mp4?token=UpFqBrACMbRQcgE65IGFfIXGWgUqqEH8Tr8_khWBC1siplddGCvCpT3JuH9axD4t4b-dZxazIkhy66ZeyEhdR5bC2VYIDVxRpaFlDHuxBZdeIVPimz40VpagupKG07lxM_FOQU8TDRHT3laoQkrk2a0dbQQcD3atEdiJ-qGCdBExzFLCkygmgra8Imzck3nUupXrz79zaZ0P3NhZk1X45O0XaPe_mdoP63Hj7B-9IuC1blhZx9tUUVcnw--9X7_cW5ynb7Y9_Un21PwDQYCTCslAKofWJ_Enxt7jyVmlLwYc2-2sWupjpt7MzrYLESUYNMMQpyrGWnQWo03n1GqZvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرئاسات الايرانية تودع قائد الثورة</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/naya_foriraq/80734" target="_blank">📅 13:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80733">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff15d4aac9.mp4?token=ZscPMoULahwfkzqBcm_1N30mMck-PvoA45IxcItBNCs-7MsQvDKaZxEk5A-BK7G7KF5hvzLevYr8Z77NswJwu480ihdoGiVNg_3AuOln9luw5KcbQQfp_YWSvVyZeRab-VYvKG6d1IEhXWscNiHCF-uLKj74CJdfXei585nVcAY9aPZw3z3xULL_e86EbdqqS5NtLN_NonlAEA9yAPIltDFSNJxf3-RbnwnhqaFOxhiCwtLA8bojG6VCYNiNdGPyEqUvgcms2DC0xBdGJo-XG2d1iJRvtkhXJDrUJSY0_vlwkwzu9bgnZD_4mHUlw8OVSelkRIS8qf1gSuhsoUQHCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff15d4aac9.mp4?token=ZscPMoULahwfkzqBcm_1N30mMck-PvoA45IxcItBNCs-7MsQvDKaZxEk5A-BK7G7KF5hvzLevYr8Z77NswJwu480ihdoGiVNg_3AuOln9luw5KcbQQfp_YWSvVyZeRab-VYvKG6d1IEhXWscNiHCF-uLKj74CJdfXei585nVcAY9aPZw3z3xULL_e86EbdqqS5NtLN_NonlAEA9yAPIltDFSNJxf3-RbnwnhqaFOxhiCwtLA8bojG6VCYNiNdGPyEqUvgcms2DC0xBdGJo-XG2d1iJRvtkhXJDrUJSY0_vlwkwzu9bgnZD_4mHUlw8OVSelkRIS8qf1gSuhsoUQHCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرئاسات الايرانية تودع قائد الثورة</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/naya_foriraq/80733" target="_blank">📅 13:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80732">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef3133b31.mp4?token=MdxpzNV1uu9UCKAdyiyMbAH8MMyXGNAIPYYkeWL563yvM8zcO4Uz_5DcPPJyW2PMyubIJe8P9xJJDp94zPBEuwcAlto-gyGLodfpNI4oTFcJzmNlCw2quYWt1K9AYah-teSqkoR7mdqZv8YgCZbx1UJP7CXekONeVh6a0LSTEHPpoVZVPUZDDxwK6oGhEi6YWw2KGoMKZwe3jmpUnDl0KSgeqBfk2p9I-4ZvCGJAPVi4P8c6ZUqAW2PcMPbK_7-8FD_dmWgDeK6KOZuMH_ZOJOyFqRzrYFu1J3_opfNTNATD2xtEu4zasoHVXqjKij3r2XUmQP7ax9w4GMnR-eJTDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef3133b31.mp4?token=MdxpzNV1uu9UCKAdyiyMbAH8MMyXGNAIPYYkeWL563yvM8zcO4Uz_5DcPPJyW2PMyubIJe8P9xJJDp94zPBEuwcAlto-gyGLodfpNI4oTFcJzmNlCw2quYWt1K9AYah-teSqkoR7mdqZv8YgCZbx1UJP7CXekONeVh6a0LSTEHPpoVZVPUZDDxwK6oGhEi6YWw2KGoMKZwe3jmpUnDl0KSgeqBfk2p9I-4ZvCGJAPVi4P8c6ZUqAW2PcMPbK_7-8FD_dmWgDeK6KOZuMH_ZOJOyFqRzrYFu1J3_opfNTNATD2xtEu4zasoHVXqjKij3r2XUmQP7ax9w4GMnR-eJTDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول الوفد الاذربيجاني الى طهران للمشاركة في مراسم وداع قائد الثورة</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/naya_foriraq/80732" target="_blank">📅 13:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80731">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dce186c99e.mp4?token=Vzb9AdywMUsNki0HEf_MEm2e5_hlDXru7SBmPK2dHU5rF8kvjOu12tPK3RZmUB6uGI7kz6sd5EyBpjQgOSgTFCmf41ypsbLlQBzJD4ztW5b-8Y3rTDJL5kUtnghn0bRIee5RCPiUfXjpFB3DxtXoMCf-EjOzR99X_hFlQWaNjWU-NSGgFEVgbYpUA8Vs1VrrmZoG2DlDO_lp0McCdzQ9wkxig5kgynFdYb4UNZdIM7TpX66m8IwxXoLuO_iNUxQQPiO1Mru0Ml_6neJ4_LHxLfCgztC-3ru2zFcEUxFgc_TvBt_n2noF_kZM6A128gMmIXz-eVcgfQyGPVjfFY35nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dce186c99e.mp4?token=Vzb9AdywMUsNki0HEf_MEm2e5_hlDXru7SBmPK2dHU5rF8kvjOu12tPK3RZmUB6uGI7kz6sd5EyBpjQgOSgTFCmf41ypsbLlQBzJD4ztW5b-8Y3rTDJL5kUtnghn0bRIee5RCPiUfXjpFB3DxtXoMCf-EjOzR99X_hFlQWaNjWU-NSGgFEVgbYpUA8Vs1VrrmZoG2DlDO_lp0McCdzQ9wkxig5kgynFdYb4UNZdIM7TpX66m8IwxXoLuO_iNUxQQPiO1Mru0Ml_6neJ4_LHxLfCgztC-3ru2zFcEUxFgc_TvBt_n2noF_kZM6A128gMmIXz-eVcgfQyGPVjfFY35nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد قطري يصل طهران للمشاركة في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/naya_foriraq/80731" target="_blank">📅 13:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80730">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وصول وفد من دولة جمهورية كوريا الديمقراطية العظمى لطهران للمشاركة بعزاء السيد القائد</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/naya_foriraq/80730" target="_blank">📅 13:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80729">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e2423c7e3.mp4?token=ATEv3VSkpySYpSymQls5BZi2W2hVeBpaJ2s1fJoLXTeebD7eN_vegyZuuKbXMNjW14LP3WvwyGniFDIgEBx8H3AgHm4lQSl3bM8nppvPy8MzgtcpWofcKObZSRyx-K6z0bdlA6nbCo-g0UaHtTkKtmmUclb-1s1Wt5RiH3qWr7O03CxBvynj46Ibx1ZxtODPPu7aGk-y4N8TVKZIuGall3dA7nq9HdlYjr4Ao6DNaJN7HZIDgI5B9FSD8q2EJODnjkzVauLKfxftS6Ue-RA3oLhlwYH5iZc9IGGQCmeGO2E7vaSUtxnxhWKjHBteI7otJIry-K0dt610XHMC73xwug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e2423c7e3.mp4?token=ATEv3VSkpySYpSymQls5BZi2W2hVeBpaJ2s1fJoLXTeebD7eN_vegyZuuKbXMNjW14LP3WvwyGniFDIgEBx8H3AgHm4lQSl3bM8nppvPy8MzgtcpWofcKObZSRyx-K6z0bdlA6nbCo-g0UaHtTkKtmmUclb-1s1Wt5RiH3qWr7O03CxBvynj46Ibx1ZxtODPPu7aGk-y4N8TVKZIuGall3dA7nq9HdlYjr4Ao6DNaJN7HZIDgI5B9FSD8q2EJODnjkzVauLKfxftS6Ue-RA3oLhlwYH5iZc9IGGQCmeGO2E7vaSUtxnxhWKjHBteI7otJIry-K0dt610XHMC73xwug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط قتلى وجرحى من عصابات الجولاني جراء هجوم مسلح بواسطة القنابل وانباء عن انتحاري استهدف حاجزاً عسكريا لهم في منطقة الدويلعة في دمشق</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/naya_foriraq/80729" target="_blank">📅 13:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80727">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06facee14e.mp4?token=N8WZHVAz0ZRK9qVpFmWgsoJOx1afIlQ4hhSy-z3wlHQ3auOP0wQYERVhwNtr23RNc8HDJc4n0U0gCZxViqmyXmhRjYU6GYWa01U0fqaJOvoOOZY9YxzF-40FSplcVyfXX6g4gRXXp1e-d8uDLJqRCcV2xrzFGPCojozJJtFGS9wTS6bdodMIExk1jg3jyvySqOb8ADl26u6GSI2j0NjTp7k9bnitx2soAH7dvrUhNjAE8Xfp_KjZW4k1VWzLz84hztIM5eMHjo1e_1txeqnvmrZY1S6Pja7pqrosigXUM8bypgQY_WOdDXCQHr7jclW3hueJYHniJYNRWv1BiFrn2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06facee14e.mp4?token=N8WZHVAz0ZRK9qVpFmWgsoJOx1afIlQ4hhSy-z3wlHQ3auOP0wQYERVhwNtr23RNc8HDJc4n0U0gCZxViqmyXmhRjYU6GYWa01U0fqaJOvoOOZY9YxzF-40FSplcVyfXX6g4gRXXp1e-d8uDLJqRCcV2xrzFGPCojozJJtFGS9wTS6bdodMIExk1jg3jyvySqOb8ADl26u6GSI2j0NjTp7k9bnitx2soAH7dvrUhNjAE8Xfp_KjZW4k1VWzLz84hztIM5eMHjo1e_1txeqnvmrZY1S6Pja7pqrosigXUM8bypgQY_WOdDXCQHr7jclW3hueJYHniJYNRWv1BiFrn2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائد قوات الامن الايرانية على هامش مراسم وداع قائد الثورة: إذا كانت القوات المسلحة اليوم قوية وتواجه أقوى الجيوش في العالم، فذلك بفضل جهود القائد الشهيد.</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/naya_foriraq/80727" target="_blank">📅 13:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80726">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUW8AEJJaiw43ApZ3UnMkt2qWL1hssGGtdDpCo22CTEAw9Ea06zfocZfYNOEjBoyXOvo0ym-lZQ4HgAwwb0atK6hwu2N45cv5Lrz6_pMNL1nKmAvXOEl8aGwG_zFrF_1l3Wdbj_w_CRiEjUZaTx1Hnd5hMJwzQ7D7asFjZGfopIDV7uDp1qvWAhUTyYHMyX2DA1j23GKtn7sHQTEtuVvgfKLWZEitt5E2C83AynFmbdiIeP2CvUJAVr6LAp_d5mhjwj8kq-77GWiv38A4aLBDtRWNUX6wNxT_ZCbvW93h96ASxvHDRePtLbp0OWFVySOe5N3UORRTI2kS_K4AlLaKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الرئيس الايراني مسعود بزشكيان يستقبل وفود من الصين وناميبيا وأفغانستان ضمن مراسم وداع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/naya_foriraq/80726" target="_blank">📅 13:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80725">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADl-tqetjIGIsMhcb7OWDpEMMroymk6ydDyv8c0JX3LsT3wEcuCShO9ZoK6q_pWUDm34kv22K-vDGOKM19RAUwQaFj7fGvXG0Hs-npsEw_DmjnoC7PimMEqskFhrWQ2dxMogKmKzECMHTuSFxmITKj6zhVCMDDZLijQvvoh6JXGZVeKW5Q3161La8pwENv2z7HlHgjZ0xMaBm4Bl8pRwr-DsjM4RHr8CR8jel4Na__k70itwP0e_nXXCWc6ZesXPhyxu65Cu81A3hr1EezrN5YtsImsM0kXglKnvT8daWdct9JlYmxBbwydIV0pBFy08otS3ch8ZnB99W0ve__R4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يا سيدنا القائد؛ أفتخر بوجودكم المليء بالمحبة والطهر
رسالة من الشهيد مصباح الهدى باقري إلى السيد الشهيد، الدكتور مصباح الهدى باقري هو صهر القائد الشهيد للثورة الإسلامية واستشهد في بداية الحرب المفروضة الأخيرة برفقة آية الله العظمى السيد علي خامنئي</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/naya_foriraq/80725" target="_blank">📅 13:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80724">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بدأ جمع تواقيع نيابية في العراق لاعلان يومي 7 و8 تموز عطلة رسمية لاتاحة الفرصة للشعب العراقي للمشاركة في تشييع قائد الثورة</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/naya_foriraq/80724" target="_blank">📅 13:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80723">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB2Gku5GCQ7qvHr--elo9hawIyLDnRFTDNqSg000Vy3Fce77mD7-Dl6r_Gk-WcTh2QnhBHkdzz_5lSosLjwE4nOnwbwPNjMyMRwWaBlTHbBUpkqiNaOV2kOfIHAcBSw8DDaxrD3C2ZHBqKvqhLgaVfezybAvdO9AesASy214DEeZB6XfnGXOVAr5-FxCcR3DtqRkpmdbDFxQ7tR6cNt6FQcZ4_d1AY2421MdrYT6ITVutregPwZBKVJJFlmWS5wKYU6g8eRp5hIOCrFs2WZKiPL53HLspSvIjTbtF0x5fr_oEHC765LpU3mZz9li-MYOD4zJw1YtHkyL0fTiQHVkpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/naya_foriraq/80723" target="_blank">📅 13:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80722">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e686e795f.mp4?token=IIcWWM6O1gg5jUKiVdeIlz-iKi7xWY7sV6rCzCsd2yBDrHDPeWciatzYZqNyqBM2UgUxxTMkRaNp77_Y9_MeXXw85rXxghQbcwoSubMYcQvaYrUJTjvsqOsm-0Kl2wlWOuk2ZLHgpjOZqYFNhIW8az0xj8dgQjVZCICcv_uXVTODkiFKdRKtQYt_1CqsZdJc97NE_Nngc68-aR5XUL-HE17t0Dn8YO_to5qxZWKeGC9BJ7N_Tr3HBfnruHJAIDNHJDhLsJ14kWpUn1cTD9KdQBZ_hV_ImS4PJSJTr-B_pV0Xnekj8tuZnbUxCgYKWOYbeosDKE45S2CJEq5CF5JfQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e686e795f.mp4?token=IIcWWM6O1gg5jUKiVdeIlz-iKi7xWY7sV6rCzCsd2yBDrHDPeWciatzYZqNyqBM2UgUxxTMkRaNp77_Y9_MeXXw85rXxghQbcwoSubMYcQvaYrUJTjvsqOsm-0Kl2wlWOuk2ZLHgpjOZqYFNhIW8az0xj8dgQjVZCICcv_uXVTODkiFKdRKtQYt_1CqsZdJc97NE_Nngc68-aR5XUL-HE17t0Dn8YO_to5qxZWKeGC9BJ7N_Tr3HBfnruHJAIDNHJDhLsJ14kWpUn1cTD9KdQBZ_hV_ImS4PJSJTr-B_pV0Xnekj8tuZnbUxCgYKWOYbeosDKE45S2CJEq5CF5JfQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد باكستاني يصل طهران للمشاركة في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/naya_foriraq/80722" target="_blank">📅 13:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80714">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qTi9XoW869kTFUeDmlInSZy-dXNxq-SeQedccFuXPJ8fjUH7PxMc5yuIb1cwVQRIIvcqTRq4XU1yRMkTmebp3by706Ce6VbaFfU_g_nRZQE9A-EfjTSLl782Yi4vpVSWpS9p4ygTEwsn784m2zzGMWZJrA9lFLlCVJwAgM4b-dqte6s2x5qur8lqAx25hjPMqW8P996wwo1gKeCfMx4f8BHB4e_29rxxcOeKkEnli5pYMPOpfz3pimFjetgi1JMpYFzPwB80nZaayRLQmUJZgtPnGrOXO7hyuNKXAh-AH1eofvlGlHK5ltzKues4MDx-aG1IqMHSriSeuNZRAS6ZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/patIZyPr4oByQz3EjRBpQmQzdijPn_TeHSoy6Xhb3gk9X4hktMPocTlG-s3ASQz0tkaOqsMkowxDB6Zd4sqRUjtBqNqAcIuzaZMIQ0JA6IW-3ZaBM0ysE0vOsefZO6ggMvaxj9rS4NM3-JXyBLBYbY078JKirPDL4rlzb8ZDIXGLfJ_A2Jm28ZlQn6GqnWwORIKzv4Y4QnB13hKzhcGIhFQFvWkvwrnVyPrOz3wDPbtNHzONu3532m-S6pKQgaotOgrSa_2DU9InK8fcXW2tcIOiA5lCqkkuE7u2ncScRUcCwTu_YeYLzI498QZrjYCtiq03_C-U7uy3GZ3XXRKMrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lGO_poCRiyGLBxo2ROgwTNMYqciS-QWBu-1QEwpsOP9dQ9h6Zpx1W0NdOBjDEnJHq_Srt4AgMTnrnIR-VVvYhTKHu-4XKzCsJTapLwyW8WJ6J8fUVSlO3p2KQgYnJ4N8jwgi1NXv_qeo_ZjjN3hKVOTIwcfB6C00YPmXB_0dj24RS5z9O6T_kIj_EKoZRxiPIZPzjkB-f0GmShAGfQDuLrmSEhJKZD-XzhMkGFP5HRU0bDkJVdA3sTRD0x31FrwnhNXJBBCYyw8N0ulqEX_KhZ5Fw4oK8uYgW6F8KpAVb742jtP6nMfEbfwZ-YXa9BmjayErpfCmLsoS2pL0H7Dr1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qBZ50L2nCTDmOGPDTS0-UQ7zoaf0_0-mHypArdc12olSZgE-zRkzB50d1KTm1DV6gYL4OwLvaUsIvJbhv16bs-eitj607pq81qWoFAN5Hl3PF4-7gwi4lxGpdDENRaX9DEK2jXmnw8J2EwPtzN333u-8gkzLZWphMOxI_p8mFh6UHqdydCC1H-ExeyQooNsDTHADSsEgiaYAlNNpvZFdEwFYxDyaWfRSgBU1sriCiow3qJiSCBIrrUf9ths0HdqPyc04JYkT0aRQsTUSYMAyQ9hDS4vtlSdmEmO1FfFyRMLJsMcKTd0N2gq0Pst5dd4oQndUqOh-j9CfvIQJL4CQLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2xh6-dioY2AFAuq0KFCChRcuqZEGGX05kMMkGms2eTNiRxcfFjyEjzbaU5EkEnGEvAOPsk06r8dF5Q5vLe7GetZuMZI7iSFEt0fBALUUT2xFXSWbNnifmUxA8yL-HZBM3Pw4Fy_mtIGfgYrpBJ3W0OCUQHu1j3DdpAHCpg_TBaHiL6nAPSSxD_hkbPXcZL_21UTuCkm8maB55ItD5bfnJ9ELtLoCLIaknse6U8XftEXmiogwDpnZ3YWZMWOST7rbgqQzMMiwhPtW2YtTnjCif8ZlqXZwFvHyEzXZrKUuVZBj2Un1iuOclNYFozJR-3grtQTWEKFAzr7l1xopvt-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dEtmoZ66sENNWBWjafY9Z9jaZrEaWsWO7oDmUe3B2H9yPib5prtD77M1jJLgDZLMnyzrUONajrvongAHz_cd-N930ATzOk8Oawd4dR0CMToOx9GmdRINK4YntppETXnnWF73ze-yHDsFDAbJQcDccKR-ZUx_47pzlpbjtsvuRcWHGjVRgkXmpRvczK4YDkOSRNxXYt2FyJuFZ9OjrNCfm7ZLrR71PWtYNDlZMGMDQxEeIPXMYCAHz_vVMK4cV3MTXtTqGYbK7bJ2eNgRJfAEVEzDhtRcgMRbRdT5BlUS_HYXxP5DlNs7iB5YhkjOkKfm0jcv5iHBCNFr0SRjMUCGbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoiY-EAi5AimwryokBeFYrd_jQSNpvddv06sgoCCuv1QRKuvsOCARD64Xqz3P99rcK0huQTwJfP0-N1mpjropHgjD2hU4Si5nGju0uurhtANJGrhNX9U7LNyLLmqGTUy5Iceu3dkC2HrUo-c193eDqmVQbAB6KRQwG_gK5GCu8AKnOH1mbWdWWDqIJBQDeUx_qquQaF5fzn8NTbDFRJnoGRLlMx8w9WygnYPgrw7l7ccU4QWflRXaw6-3Accp5GWmKfA8sudzZduND0cerGt3Kubr1fCzyCwG-daG6fVa5kPpTQ353AoYa4WaFVaDJ5wmL2IN8ypG8GXJh2khC8Eeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/elZbAcAaXDDJXyGALxlePAPNfnbwNHOy3e3_g3Znh_2vIXFNbGlaGfMpMNZyzftnHq_HCot2KbtCm1gO83Ace_kEl0tvcPXfAzH7GteBAQT-a8dnbnzsiQx9Rn9HSwEA4u9Pfb1hY_3Z5JCvEFNhn1TGa7si9yYtaXIapEhtdQrykkqFHHyMcGhlnc0ZT76ULHLaSNFhoVTP-lxJ1NWZr_vRJMG3kYHydfxuSK6tj5CkxydkRiC6QXRtcpNxX3Y1bck2cw3-OHZNQq0ZSpLfxspmL3hfWa5w3mL88oB3KsZXm4gCYXQzRuiSAx2DMAlKJQeaFrA5Xt986Yke4x0YuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وفد هيئة الحشد الشعبي برئاسة الفياض يصل إلى طهران للمشاركة في مراسم توديع آية الله العظمى الشهيد السيد علي الخامنئي (قدس سره)
وصل وفد هيئة الحشد الشعبي، برئاسة رئيس الهيئة السيد فالح الفياض، يرافقه رئيس الأركان السيد عبد العزيز المحمداوي، وعدد من القيادات ومديري الهيئة، إلى العاصمة الإيرانية طهران، للمشاركة في مراسم توديع قائد الثورة الإسلامية، آية الله العظمى الشهيد السيد علي الخامنئي (قدس سره).
وتأتي مشاركة وفد الهيئة في إطار حضور مراسم التوديع الرسمية التي تُقام في العاصمة الإيرانية طهران، بمشاركة شخصيات ووفود رسمية من داخل إيران وخارجها.</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/naya_foriraq/80714" target="_blank">📅 13:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80713">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940ab08d64.mp4?token=Jk79Dr0rvk9hocoOiXSSUf5Kg48DQ_8ybW84BSvy4nWcvHhSDd1gf76k9xa-Zeq0-OQZO-A5MpJGe5luOR5I1fTVTIwM9Q7HTF7fLgrW2PRp0wKpO-GtVbZ7Kw7SmJVBf6Q4sWFD5Ds8rc7O2ODqRDIwT4-zPuNEKkIlR-zCxOuKwBaT9ZzxCiuQ68X4KmG2tO1dvdNVrhTCgosEwJO8k098xvVP_zceeQfuMMEOY6JmrmWk3owNPjVZCRJdhFmavt33tuhrPtCaOcpKxGTa8IFF0-dDd5927fhVX1cwVu_WrZvN-Po0PooZyf1Br1jMxzd2rl7z7qJOMfI3VOtS9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940ab08d64.mp4?token=Jk79Dr0rvk9hocoOiXSSUf5Kg48DQ_8ybW84BSvy4nWcvHhSDd1gf76k9xa-Zeq0-OQZO-A5MpJGe5luOR5I1fTVTIwM9Q7HTF7fLgrW2PRp0wKpO-GtVbZ7Kw7SmJVBf6Q4sWFD5Ds8rc7O2ODqRDIwT4-zPuNEKkIlR-zCxOuKwBaT9ZzxCiuQ68X4KmG2tO1dvdNVrhTCgosEwJO8k098xvVP_zceeQfuMMEOY6JmrmWk3owNPjVZCRJdhFmavt33tuhrPtCaOcpKxGTa8IFF0-dDd5927fhVX1cwVu_WrZvN-Po0PooZyf1Br1jMxzd2rl7z7qJOMfI3VOtS9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد هندي يصل طهران للمشاركة في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/naya_foriraq/80713" target="_blank">📅 13:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80712">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35aac3f0f7.mp4?token=lZkbzbosYg153rT-Lm7sZfB3C_F-DXllWJL_RDHYzTrGJKyO0YMs4Fy8IcPn4hmrPlXxDtQTShbzQE3ROPx7lhIHfip6BIroXhWKs5YVXpBrOSI1fZIcfARukiU86D6OBMC9jo7r-SvITPlC-a7LMjSQlQ-k39KtCd_lhxepDp-A_fgG4e5rTQAUdmWpwcC6vnlJQk2fAa2ukL3nc-7ABODxLGEEdv1AXMw4k6QYYFaTiuMtZ3obBEAUQpeNkexFqEQdglU3CLRiWh25ClVBKubd5UaJbzJ7VeOtGH7LU3lyBOIB0YUJebdQOdMKlCSDvqqyk7oraCBPtUoo8ndTdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35aac3f0f7.mp4?token=lZkbzbosYg153rT-Lm7sZfB3C_F-DXllWJL_RDHYzTrGJKyO0YMs4Fy8IcPn4hmrPlXxDtQTShbzQE3ROPx7lhIHfip6BIroXhWKs5YVXpBrOSI1fZIcfARukiU86D6OBMC9jo7r-SvITPlC-a7LMjSQlQ-k39KtCd_lhxepDp-A_fgG4e5rTQAUdmWpwcC6vnlJQk2fAa2ukL3nc-7ABODxLGEEdv1AXMw4k6QYYFaTiuMtZ3obBEAUQpeNkexFqEQdglU3CLRiWh25ClVBKubd5UaJbzJ7VeOtGH7LU3lyBOIB0YUJebdQOdMKlCSDvqqyk7oraCBPtUoo8ndTdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائد الجيش الايراني على هامش المراسم: نعلن للأعداء، بإرادة أقوى، أننا سأخذ ثأر الإمام الشهيد والشهداء.</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/naya_foriraq/80712" target="_blank">📅 13:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80710">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🌟
السيد مقتدى الصدر:
بسمه تعالى
قال تعالى: وَنُرِيدُ أَنْ نَمُنَّ عَلَى الَّذِينَ اسْتُضْعِفُوا فِي الْأَرْضِ وَنَجْعَلَهُمْ أَئِمَّةً وَنَجْعَلَهُمُ الْوارِثِينَ
كنا وما زلنا دعاة إصلاح لا يجمعنا مع الفاسدين حتى حب الحسين ، وقد كنتم وما زلتم معي في السراء والضراء، فلنكمل طريقنا لدعم الإصلاح وحملة الإصلاح الجديدة التي بدأ نورها يشع في ثنايا عراقنا الحبيب.
فهبوا لوقفة سلمية تدعم الإصلاح وجندي الإصلاح الأخ الزيدي رعاه الله.. لنقوي من عزيمته ولنثبط من عزيمة الفاسدين الذين يحاولون الضغط عليه وثنيه عن المداهمات الشجاعة والمثمرة التي أرعبت وأزعجت الكثيرين من الداخل والخارج.
فنعم نعم للإصلاح
وكلا كلا للفساد
وشكراً لكل من أعان الأخ الزيدي كالقضاء العراقي ورئيس البرلمان العراقي والقوات الأمنية البطلة ،
وأحمّل الفاسدين المسؤولية الكاملة عن حياة المصلحين وجندي الإصلاح وكل دعاة الإصلاح الذين يرومون إعادة هيبة الوطن والدين والمذهب
والسلام ختام</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/naya_foriraq/80710" target="_blank">📅 12:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80709">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95caa026c0.mp4?token=njX3KLiRAwduP04Loq4JOCnpzqvL6wCHsB50kJzbWDI4wtkckCwSZOyFLRYTsUfI-tLCxEHby5Y-Jcg1YV94F3tpP6Aq9_Ethg8BZ5VeFvfRanNArWRaTgOT1YgbjfR1D3MKTeR5kukW3PWTQ8zAyKLuRQM2M2jSf77ZBAH1bl6e742DKEEc6UHmrJVchrKRCA3qtNM8y7jSnD-DgKwYHVPvNY9e_KBkkZuoBv5XIkDUmic-0vPa_UdT-JH9XT5JQ0PWfH8CQNZo9hAc2XhsDtp347i-9BdyXpe_KwKhmrGpUeIRRb5VThoyb5zY1TSP_cJKm5odf_ma48nx3KwPWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95caa026c0.mp4?token=njX3KLiRAwduP04Loq4JOCnpzqvL6wCHsB50kJzbWDI4wtkckCwSZOyFLRYTsUfI-tLCxEHby5Y-Jcg1YV94F3tpP6Aq9_Ethg8BZ5VeFvfRanNArWRaTgOT1YgbjfR1D3MKTeR5kukW3PWTQ8zAyKLuRQM2M2jSf77ZBAH1bl6e742DKEEc6UHmrJVchrKRCA3qtNM8y7jSnD-DgKwYHVPvNY9e_KBkkZuoBv5XIkDUmic-0vPa_UdT-JH9XT5JQ0PWfH8CQNZo9hAc2XhsDtp347i-9BdyXpe_KwKhmrGpUeIRRb5VThoyb5zY1TSP_cJKm5odf_ma48nx3KwPWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائد مقر خاتم الانبياء المركزي على هامش المراسم: لقد فتحت تلك الأولويات الدفاعية التي حددها القائد الشهيد للأمة، خلال الحربين المفروضتين الأولى والثانية، الطريق أمام القوات المسلحة للرد على العدو. لقد حققنا النصر في ساحة المعركة بفضل جهود المقاتلين وتوجيهات…</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/naya_foriraq/80709" target="_blank">📅 12:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80708">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🌟
🇮🇷
قاليباف:
لقد وقفت إيران والعراق معًا في الأيام الصعبة والجميلة. ورغم أننا تجاوزنا فترة نظام صدام البعثي المريرة، إلا أن الشعبين، كبلدين شقيقين، وقفا معًا للحفاظ على سيادة بلديهما، وساند كل منهما الآخر، وقاتلا، وسفكا الدماء.</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/naya_foriraq/80708" target="_blank">📅 12:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80707">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3f19945.mp4?token=E5BWfHaZu02F-xPwNNAy2CAk_1RorxzJnzIbRMRpxvahuXtj0EtqjkdCsDEpptK3-wfG0BLafSIJfBvuohjOhcOlPVt6cJ3dDttJZ5d_02YlmyQ6ItgXrbcvrr4PxG7te9BpIofYsxxmIKaoV4Yk_zPzE5_FM7ymIpyLIrayt7YnBlq7XeLpk9p6CV5Zab4eF_EuM9qKCgDIz52OL2wXsjXzsiDofBsxD1RUn_z9hZzvgTEhOYrWB6hGLFppHSZ0fL5L5P11TxdZvD15Z4PUMC8kvc_CzefGFSZ2OfTcxeslvqH0W_DlDil8ZYEQGHXExtOO_VTbrsnV98dizcRwLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3f19945.mp4?token=E5BWfHaZu02F-xPwNNAy2CAk_1RorxzJnzIbRMRpxvahuXtj0EtqjkdCsDEpptK3-wfG0BLafSIJfBvuohjOhcOlPVt6cJ3dDttJZ5d_02YlmyQ6ItgXrbcvrr4PxG7te9BpIofYsxxmIKaoV4Yk_zPzE5_FM7ymIpyLIrayt7YnBlq7XeLpk9p6CV5Zab4eF_EuM9qKCgDIz52OL2wXsjXzsiDofBsxD1RUn_z9hZzvgTEhOYrWB6hGLFppHSZ0fL5L5P11TxdZvD15Z4PUMC8kvc_CzefGFSZ2OfTcxeslvqH0W_DlDil8ZYEQGHXExtOO_VTbrsnV98dizcRwLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">كبار قادة القوات المسلحة الايرانية يشاركون في مراسم وداع قائد الثورة</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/naya_foriraq/80707" target="_blank">📅 12:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80706">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=c3n2r3NJjcSMH1l_qnrJzua3xVQxbGZO1at0BL9A7UdUPTpfwPfhtW4VIve18GNBN_Zi3Rnx0GYrgyK6afNCQm2dT1FMTYaRqQXfp497gT-NxPIJYQneDQwY7Uer-Ahg4MMmCjUbfsYuiBJ1AImymmrLvo3bQN3OcwIaB3QuGlmF4kG8nDUMpLBokb7XVBLZXxD23v2VJRzdzQv-gVkp5FFHTE2-dFXFDthwOuBfl0-m4dy_sXuDyFI_4IdhNCv58Cl6yBCeFzoT6kqfNxGfCL0sM0o5kVHRzPl4btEJuvARwjaZVwdudPfW8tBTDI8vBO0Z2MUEoh-csM0FxHaipw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=c3n2r3NJjcSMH1l_qnrJzua3xVQxbGZO1at0BL9A7UdUPTpfwPfhtW4VIve18GNBN_Zi3Rnx0GYrgyK6afNCQm2dT1FMTYaRqQXfp497gT-NxPIJYQneDQwY7Uer-Ahg4MMmCjUbfsYuiBJ1AImymmrLvo3bQN3OcwIaB3QuGlmF4kG8nDUMpLBokb7XVBLZXxD23v2VJRzdzQv-gVkp5FFHTE2-dFXFDthwOuBfl0-m4dy_sXuDyFI_4IdhNCv58Cl6yBCeFzoT6kqfNxGfCL0sM0o5kVHRzPl4btEJuvARwjaZVwdudPfW8tBTDI8vBO0Z2MUEoh-csM0FxHaipw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">كبار قادة القوات المسلحة الايرانية يشاركون في مراسم وداع قائد الثورة</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/naya_foriraq/80706" target="_blank">📅 12:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80705">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8e6eaa98.mp4?token=q60A_DMv2SSSe236sRLBFhBgO7Ta-EL3BcnJKLs2kBzUIxKF68fH6xWnT66RQ9526BfuiPnNkw3SLh_BOO__9Ey-TBdkRjOXYbL9WW2yIaZg5DFYsZElHXhTscc8HPh1m4SVDsZ8F3yDUmyE1687TZO56bnj_rJogJYPaufZjpPaEmdi1DZE-w2EmvKh0JtgZVB3jyteuyNpf1kfABXtphovSA-0HqU_VsGjpBAab5h4U5TTqcBadIgosS2GLIBODx0mNXuVvISsPOjJ8YjZHL40ia5enhrJVD5fWwRQMd4vNgu1cd9qZBhoaHcstX7OOIJtaUu6hBDPCViT99tk6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8e6eaa98.mp4?token=q60A_DMv2SSSe236sRLBFhBgO7Ta-EL3BcnJKLs2kBzUIxKF68fH6xWnT66RQ9526BfuiPnNkw3SLh_BOO__9Ey-TBdkRjOXYbL9WW2yIaZg5DFYsZElHXhTscc8HPh1m4SVDsZ8F3yDUmyE1687TZO56bnj_rJogJYPaufZjpPaEmdi1DZE-w2EmvKh0JtgZVB3jyteuyNpf1kfABXtphovSA-0HqU_VsGjpBAab5h4U5TTqcBadIgosS2GLIBODx0mNXuVvISsPOjJ8YjZHL40ia5enhrJVD5fWwRQMd4vNgu1cd9qZBhoaHcstX7OOIJtaUu6hBDPCViT99tk6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرئيس الايراني مسعود بزشكيان يستقبل نائب الرئيس التركي والوفد المرافق له ضمن مراسم تشييع قائد الثورة</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/naya_foriraq/80705" target="_blank">📅 12:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80704">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وصول وفد سلطنة عمان الى طهران للمشاركة في مراسم توديع قائد الثورة</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/naya_foriraq/80704" target="_blank">📅 12:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80703">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P555MEEgjnpvFd7CH5F89YYSCS2dzlOLy70Gpb1x5huRJyc2geXCYkgMdoa4OW-yO-Ce15mbZa_mmjnQD_2GR9yr9eyVPiF2yf5YtVh9lCGSkoqIuPrbTTM2GPjlX4hY1-8ZET2L1dhLezvN3n944e3y1jdfkfGF2WN1ciBe-rYzKgNVV8andY5WFwtT_jy0ryUqfKcJhBPUhpNNM4kKyECIu_CCih3zKjzZgizuVuol3GW2TB6D7P71LSF3IH4_vB09ukMXvHegECrkSQm7OZnBAn4eMBmjOO-8bAjICBOcjjIH05bxANnnFGFBLdegTnoKdanaJVpZmRx0KF7HlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أكرم الكعبي الشجاع</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/naya_foriraq/80703" target="_blank">📅 12:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80702">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مشاهد جديدة من دخول نعش قائد الثورة الشهيد الى مصلى طهران</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/naya_foriraq/80702" target="_blank">📅 12:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80701">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9252cf910.mp4?token=LnZb_fIHM3JTPu2oAywi7XGaVuUlhrjNcmbNNQXajIU5j_D0Y6ugcce0rSdceNICv5HQv2pqph-nwuJwOdqH0qkhVvgZWuKwanuoExwVgGGRMKK8OG032JpBI3lY50VkYX_TvSMxWLw-di6J0Qni7iJ2-TreSFDrX9HmVXuBHZYIv060QVKzNltRlecZx7kZk9L6r08XwgCTO9m2kVoZyvQYIskWM6qW9xfK-SYDOS82i0VXXKnqCLuQO7OQT6YNJQjN5aNzw7uxiuFOKKWRI_tHGINeeLkVw-FwRKwmuFykfWGcdA63B88yrzFO6Ky1J1rH2a8tbEQ93DHszFm3jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9252cf910.mp4?token=LnZb_fIHM3JTPu2oAywi7XGaVuUlhrjNcmbNNQXajIU5j_D0Y6ugcce0rSdceNICv5HQv2pqph-nwuJwOdqH0qkhVvgZWuKwanuoExwVgGGRMKK8OG032JpBI3lY50VkYX_TvSMxWLw-di6J0Qni7iJ2-TreSFDrX9HmVXuBHZYIv060QVKzNltRlecZx7kZk9L6r08XwgCTO9m2kVoZyvQYIskWM6qW9xfK-SYDOS82i0VXXKnqCLuQO7OQT6YNJQjN5aNzw7uxiuFOKKWRI_tHGINeeLkVw-FwRKwmuFykfWGcdA63B88yrzFO6Ky1J1rH2a8tbEQ93DHszFm3jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرئيس الايراني مسعود بزشكيان يستقبل الرئيس الطاجيكستاني والوفد المرافق له ضمن مراسم تشييع قائد الثورة</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/naya_foriraq/80701" target="_blank">📅 12:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80700">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2919107021.mp4?token=cL47DVImh0I0drqrcfqXOXfLwDlCCecGckq0cc7ZtqQkl1vXy74v6JOrMbJ4axtq2WLi48suabI5SzdmTtyWloIGriyFJ5PALTXet8GlgxanRbWfWBoVKCH0Sn-X7zRdcD7UHew6kzoRvdOpdVMCMLyX6REDlpChZ2gQF5t1FYquv-6Tspdf2yGlHdXiGCuNz2HhSLRemx7eFaN-mkvFox1xeiYAuubdH-oi7Ms5QXEFK137mPQX1RAejVb9dHSgEQ-aZfALbT1yI1idGNvTYhCUPdOTe6AHqd6x6XlK8PRbkZNjlG90J8oP4aPicMXD1a275tc-2ntU1CDNi294GzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2919107021.mp4?token=cL47DVImh0I0drqrcfqXOXfLwDlCCecGckq0cc7ZtqQkl1vXy74v6JOrMbJ4axtq2WLi48suabI5SzdmTtyWloIGriyFJ5PALTXet8GlgxanRbWfWBoVKCH0Sn-X7zRdcD7UHew6kzoRvdOpdVMCMLyX6REDlpChZ2gQF5t1FYquv-6Tspdf2yGlHdXiGCuNz2HhSLRemx7eFaN-mkvFox1xeiYAuubdH-oi7Ms5QXEFK137mPQX1RAejVb9dHSgEQ-aZfALbT1yI1idGNvTYhCUPdOTe6AHqd6x6XlK8PRbkZNjlG90J8oP4aPicMXD1a275tc-2ntU1CDNi294GzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرئيس الايراني مسعود بزشكيان يستقبل الرئيس العراقي والوفد المرافق له</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/naya_foriraq/80700" target="_blank">📅 12:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80699">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUqcF8PqDw56Mg8ETH5geEmFS5cBPNXA3742_aMxkonEuzM-wLsy8yA99p63a7TN6wWJWYgpIEvHjjUzaI8goB72pGFOOz4wc9Q_fwQGVJIyNVxXGt_TzZJZBazMLMkUX9HXr8cWjrEJd3fHdI38Cq2ZaVVaELrrhlDCkD-KcNO0gDex3Z2C6VeQKA_EUSgCZRK5AotahE2L2LbCnhx9hXWyWFURYarSC2jTkQCDnY3C0z-01rcei_5IeiHPrpmpAM2sUtTSG7xKix16xwv1JjSqDtc4xb4uB0ghtXC2DzB--t22d6HkEriG39ecZCW3WWZjf8icGTCct5a_K_pdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
من المبادرات الشعبية العراقية الساندة لبرنامج تشييع السيد الخامنئي..
فرق تطوعية ومواكب حسينية عراقية تعلن تأمينها 450 الف وجبة طعام للمشاركين في تسّٰييع السيد بالإضافة الى توفير عدد من سيارات النقل المجاني</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/naya_foriraq/80699" target="_blank">📅 12:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80698">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d928237333.mp4?token=UW86wHgkzWoT_wF0qStoRkNfkqq4B9germmoGeJjWrMl54KBHlQk7yMxtogvTJKWgveNBYQ_tlE__L107tMZJZZ4scmiyAnbLhPMnVp234PJSX5DIAS_YPXpbtn6IKrnVMWvZ4IzphUGalFe2oXRXXq_0FplP6wDZQHuoHr8wERDGhBJzMfhJ3O0GEeUJpolT0HREDsBXgF0Vttcj_qb9SNMiqTJyEeB3XtF5H0g_Vl0UGMoiKqlq5ddwcOmyahbUIfyjEm_83MGz-CDfNcpZ53kiGBoXuFlbwBODVlZ2AbZh-DxoE3f1uGg1a6P6VNgWLeV35fyZl1faTZS9keEfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d928237333.mp4?token=UW86wHgkzWoT_wF0qStoRkNfkqq4B9germmoGeJjWrMl54KBHlQk7yMxtogvTJKWgveNBYQ_tlE__L107tMZJZZ4scmiyAnbLhPMnVp234PJSX5DIAS_YPXpbtn6IKrnVMWvZ4IzphUGalFe2oXRXXq_0FplP6wDZQHuoHr8wERDGhBJzMfhJ3O0GEeUJpolT0HREDsBXgF0Vttcj_qb9SNMiqTJyEeB3XtF5H0g_Vl0UGMoiKqlq5ddwcOmyahbUIfyjEm_83MGz-CDfNcpZ53kiGBoXuFlbwBODVlZ2AbZh-DxoE3f1uGg1a6P6VNgWLeV35fyZl1faTZS9keEfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رفع راية عصابات داعsh الإرهابية في محافظة ديرالزور بالقرب من الحدود السورية العراقية.</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/naya_foriraq/80698" target="_blank">📅 12:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80697">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMwR7-m3jvQZTajwGyOGLQLB2munHPb_CMQyKZy-KE-UwDqOd597JiJWHZkeOBc3Q8J_8ATWUT1xPwzRovQ8xtnhwMUByGp5I_FtdAV7nla7FdBxLN5JteqQwsD7exyaXsLoZiLkBt9Hw_qTfU3mi0-SEXbbEPW0z6LFIJ8-myL4Yjg3XkRfKgvvDo85tmpbHjSQF0sBAH-pycvIjYxdR05TkReJ8WEUSNW-3lVtiSaXBEbQBEZXsELhVFrEfGBIXScC00tLaOpSrPP1KiFKeLWCLlqO4DYRkifYEzcMLqfAWbhKeN4_v0zja2_5FL4W_8Bf5ImdvmTV2uok3ML2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعيل بقائي:
يصادف اليوم ذكرى واحدة من أبشع الجرائم التي ارتكبتها الولايات المتحدة ضد الشعب الإيراني. ففي الأول من يوليو/تموز عام ١٩٨٨، استُهدفت طائرة الخطوط الجوية الإيرانية الرحلة ٦٥٥، المتجهة من طهران إلى دبي، بصاروخين من المدمرة الأمريكية "يو إس إس فينسينس" فوق الخليج الفارسي، ما أسفر عن مقتل جميع ركابها البالغ عددهم ٢٩٠ شخصاً، بينهم ٦٦ طفلاً بريئاً. ومن المفارقات المؤلمة أن قائد هذه السفينة نال وسام الاستحقاق من الحكومة الأمريكية لارتكابه هذه الجريمة.
إننا نكرم ذكرى شهداء الطائرة الإيرانية ولن ننسى أبداً الجريمة التي لا تغتفر التي ارتكبها الحزب الحاكم الأمريكي آنذاك.</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/naya_foriraq/80697" target="_blank">📅 11:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80696">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28885a59f4.mp4?token=f-2zKA3nhEFGdE0akByMPGkiiz2dTm7kuXPXU0c0GSn0l0ser7-5rBxq5guCBkhNx4Wclf7UXnCYgVOkNtSkBUWLisoKNfDCc6f1JBOXDBpg7Le2uk4YTJNynY29KpWjAa-N3QobR9FklH1UvkOmcbPoLhhuyAWc3nAOHLNt333Paq3LRPleChE1UgDoh3DUm_H6NzkifgjBiQRHy6PP2ZGny7WCdVtFMzq0ASJsRjT7OvD6QriHCPl605axU-gTsllsP4KZhaK7AqnFnCmSdQBh-NKnoVJVoOlUCM3vPy4AtarQ5MGYLM8Wyo37SF0ZjmI0NoSloPRjOe5jQ6MOiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28885a59f4.mp4?token=f-2zKA3nhEFGdE0akByMPGkiiz2dTm7kuXPXU0c0GSn0l0ser7-5rBxq5guCBkhNx4Wclf7UXnCYgVOkNtSkBUWLisoKNfDCc6f1JBOXDBpg7Le2uk4YTJNynY29KpWjAa-N3QobR9FklH1UvkOmcbPoLhhuyAWc3nAOHLNt333Paq3LRPleChE1UgDoh3DUm_H6NzkifgjBiQRHy6PP2ZGny7WCdVtFMzq0ASJsRjT7OvD6QriHCPl605axU-gTsllsP4KZhaK7AqnFnCmSdQBh-NKnoVJVoOlUCM3vPy4AtarQ5MGYLM8Wyo37SF0ZjmI0NoSloPRjOe5jQ6MOiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد لنعش الشهيدة الطفلة حفيدة السيد الشهيد علي الخامنئي</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/naya_foriraq/80696" target="_blank">📅 11:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80695">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حزب الله اللبناني يدعو للمشاركة في التجمعات الشعبية اللبنانية والدولية المتزامنة مع مراسم التشييع المهيب
الزمان: الأربعاء ٨ تموز ٢٠٢٦؛ الساعة ٩:٠٠ مساءً.
المكان: بيروت؛ باحة عاشوراء- الضاحية الجنوبية</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/80695" target="_blank">📅 11:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80694">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b30b0001f.mp4?token=RwNxSVL28ujthX_fMie3w4CrGs4ESrzRBRDHafeoIzi17jigMUwVXNRMFt1xENG159vjfgTa4TV7hmQk4cXsDYAJrZ6yrCkJeDwjDKYtrFKZg-TCLlvEXLFBJISRtEoMQCj2fdv3Gp-k2DqcrJ3JKwWcLN2pATHae-gpiYRzL5n002owSN4RaCimiFo_a2eQuHbvh9tNmFqx2HYo3BqhbS9zPqSFjqj-5ZDNnds6x7RUOIuIHNqNiCbKKMd70_MRAcFWglMuD-rQN-PLhTtxVVxyXD38TT-piuASyMhfkdKGvoGK5bLz4DA-HLrO1HGPu86lbLyPgxNelmtInHG8P4yXOP5iW6C88q_FOPzM_405CDdm4WkhxHcugt35JfGKPw4fvONG5JxYmtwvutKm2MYRM8W0p-PmD9jwDENfa5FQ8c0l2Gm6tHOd456Fmf-wuJ5rIO8dpVHdh1szWoWhc67qm51rrWsyvnqzaMP7EBj5Hczpr9q-PN2wBU1Jp8Kp4gSiIwMKCY9sWnPx62K0IJUfwqFMdT18B0baC_yNBBRWikO3kfs7wqANFILz35gomJdtQqUthMOMAzTIGoNl18zANNNG0rdJ0h3sDiRvVfNg2DIOYrNKuDgeV0juk2Ayf1wepDXf6gxaGlTLOpSojEy7IMXenf45x8NUlxf59ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b30b0001f.mp4?token=RwNxSVL28ujthX_fMie3w4CrGs4ESrzRBRDHafeoIzi17jigMUwVXNRMFt1xENG159vjfgTa4TV7hmQk4cXsDYAJrZ6yrCkJeDwjDKYtrFKZg-TCLlvEXLFBJISRtEoMQCj2fdv3Gp-k2DqcrJ3JKwWcLN2pATHae-gpiYRzL5n002owSN4RaCimiFo_a2eQuHbvh9tNmFqx2HYo3BqhbS9zPqSFjqj-5ZDNnds6x7RUOIuIHNqNiCbKKMd70_MRAcFWglMuD-rQN-PLhTtxVVxyXD38TT-piuASyMhfkdKGvoGK5bLz4DA-HLrO1HGPu86lbLyPgxNelmtInHG8P4yXOP5iW6C88q_FOPzM_405CDdm4WkhxHcugt35JfGKPw4fvONG5JxYmtwvutKm2MYRM8W0p-PmD9jwDENfa5FQ8c0l2Gm6tHOd456Fmf-wuJ5rIO8dpVHdh1szWoWhc67qm51rrWsyvnqzaMP7EBj5Hczpr9q-PN2wBU1Jp8Kp4gSiIwMKCY9sWnPx62K0IJUfwqFMdT18B0baC_yNBBRWikO3kfs7wqANFILz35gomJdtQqUthMOMAzTIGoNl18zANNNG0rdJ0h3sDiRvVfNg2DIOYrNKuDgeV0juk2Ayf1wepDXf6gxaGlTLOpSojEy7IMXenf45x8NUlxf59ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد من قادة محور المقاومة يودعون قائدهم الشهيد دون الظهور أمام الكامرات.</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/naya_foriraq/80694" target="_blank">📅 11:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80693">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb23b13f3c.mp4?token=YC8ohGfEpvnLgSjZ3-jQyooPgf2XaF_MZPMo5jnUYlaKkSx0HSetM6kvvgYfobMBrVX-jZXNHNekFG2zinuI8FTOebZTy7VRDz2kmYrA4NcuXGoSBT5wCOUIssfrDYmiQTjH3qaWyEX1u0ofC5xZBIyG9RqzU8NIq_5Tzb5RRyjqw87-dMsGAw9yuTlvxZ7eGPT4pUxk-xZYATlNWVctpmtD6MSI8MosS_RkCZEkmxdhNmdULa0MMaUx8UcDf85Eh8FajQDacDiyqTpl5NDqcTNetVKQQADnB5Lg8SpW9Xk7FKSm8O-Jd7grvyKhhA7DrCHFfexwlkeGrfrbk9Sk-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb23b13f3c.mp4?token=YC8ohGfEpvnLgSjZ3-jQyooPgf2XaF_MZPMo5jnUYlaKkSx0HSetM6kvvgYfobMBrVX-jZXNHNekFG2zinuI8FTOebZTy7VRDz2kmYrA4NcuXGoSBT5wCOUIssfrDYmiQTjH3qaWyEX1u0ofC5xZBIyG9RqzU8NIq_5Tzb5RRyjqw87-dMsGAw9yuTlvxZ7eGPT4pUxk-xZYATlNWVctpmtD6MSI8MosS_RkCZEkmxdhNmdULa0MMaUx8UcDf85Eh8FajQDacDiyqTpl5NDqcTNetVKQQADnB5Lg8SpW9Xk7FKSm8O-Jd7grvyKhhA7DrCHFfexwlkeGrfrbk9Sk-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طالبات الشيعة من مختلف أنحاء العالم يودعن جثمان الإمام الشهيد</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/naya_foriraq/80693" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80690">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gjFFao67M8xMGiqyj0AiwWX-xTnJgcojt3t1bwgKFa5vOcBHOkdx7G28lzJWkzZWlRqJwwuMTqkiDAwBS7wMOle6LNpBl-MF-al7G5ljc3G01KWotemjliToWY1sQFheNPGAuv-8hqp5uY9Lu8vx1LD8AsCa7fyNbXWBb_1eTlx7kNWJkZ8evNn0AjzIG0gU1zQPUxDxZCoaU5EjgIfRqHyaQfT4TI7gBac1UJjt4Sf31f0gHTOpxrXBpwSogmqaKp3sqFyCJ7EeWRcpbzKNv2gpfY6-9cT1yZRPKp78IVkzLAqhwqnMfVfy7l_vEWQmvwrMvzVxQrYZTceAq7QITg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BpBbyw-aD10hdRWfUtDLohrdAtr08IGJ7cFIx69vBEfQPe0oCbXq6C14B_Yh8vXR7396qtmJMRnG_eY5eux-ZyoVwHfO3YnSHEH8tR1pgrWW_kxnfQuTojgc38ntGTF8Q1ADgV3KJt5DDviTKkF_qf0XsuESVf1d3yUnaV0K8ru3orpCOmb9QSNW0b_kGHL0ivWAJVPS-s78ZnVwWfFmmAEySO31tNFbRRzlm--liQwEgQpfzNAkegEr1LJl9qbQolcMJFy8MSq0JzxzNEnMml02QdRlbWh2OH_ohSByasgctjRQp20aAwpIt_VH3tiLHPzEuTiudWDoa7IdD9ELPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jMnl_cH9cYGEeqpg06_1mfghiGdLK2PP-MdSI1hRBRdxQw-HgRgbmzItvqYW5NXMNIxeCuPQr6gOHdqov50iTdOAxitBB2JTyWd8PqMxAMyBP6P9fcq0wcpKbsJ0Argic2jKq8y15gxXeaexXqDO1h5keh7BO0Gq9axS1KuIQSa7ss8_hviM0VZRx0qFsS4wgHscq9Q31j-SWeLbm28FqQQjLV89VUxrkYMObZGRDjuWk8PDaDv_UluUWS6DrdAj-sdDGBM14C58ju9znQvl4YJzD_Lb8cg79EHc9k3Abup9ch406AVWHQkEDkAugLUNX-22kmvZxIFhfvYpDLdQvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لحظة وصول وفد هيئة الحشد الشعبي برئاسة الفياض إلى طهران للمشاركة في مراسم توديع آية الله العظمى الشهيد السيد علي الخامنئي (قدس سره).</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/naya_foriraq/80690" target="_blank">📅 10:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80686">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TqgCbK9F4rJuop3W2b-3sMoBD_YNImC-fnbeqzbKMqd_W5VrB7pw470DmMb5a8WInl6OhZEJshBdmsMMfyuDLyAHwRDRz_wkpZ5j86kPh0VbJCPIXVs4cNNWlQRdRY6ebV0TxrJ7XjoHuW0NvwB6o6rfeYYfkkMzV8p3QOIRvWvPcDMVd4k9FeAl1DrTbNR0D5TSws-qSGRGyR0lzOk5etX0phHj-vgCIRhPF4kfuuphSQAl8MM-LiUjlSmGdTaV9El2uqywiZyzjMEFHOjRrKQu4zsRLCjsABmJiqM5HpdDCK9gdUCCmCGjuTnSZqnK7mM5gPo6-DjcKreE1G9gfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTaCE7o9Zk3r43iBQkkLtLxIXeyABB_OBZusxGBJWRmdU_oJKhO19CjSy3SCUO-EIMrNyla5e6v6qPemRMXg6Xj39YIAK_sXK0IY4EGGLDa6G-25bghbqBBEtvKaPb5i_HILUHpQOqZGwAO4P1Dhq_8TVX1FtcXejCMr2CaTUP8fwSY3nzfReJcChObQcLxurTDnbUXa2wzaXBqx-u7YhzD67MCbUl9sFk1drUeDsTQa8FxrBn1Rl4knBZYKSdiv-Umfk2PVkL7e-PPdCzEM3Ay97s-q5_20sX1-wQwzwUotjt0oHewyD46PM7_VkD3ckPmU2imtN_90RKA27CrxVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/skUa_EbQLN4tdQfhFoWUsp67lsNv3-FbMX90vZ9tKtxf3pXmEPDuZjqiqf58lIC9ku85Nyj7n_hGlDKc9sg-t2TgGrb67LQE42KvMnHtvkob-o1J_aAa1UmYRInoq6lIV2HSXwKfbqOVg4t1CJrb12ZdqvzRf9oUDkK5PMpz7ib7S-jNdQ0iXwVqaL2zoW-d6mTOYIzbQBBzqWjTKyD3ZiQQkKj7Mh9o6F-ov6D-MIDex6AcIYvBUDKW85hI2cxM67Z92_zzznoLmD1fsTL0BLGuE6k9mdd-wJS5nlGU1zcmk2kW_pqevruvVEZtz_-WXm8Si4eEhcFyhfyMK-JrJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rk6A_8d_V30PrR7WMZpoX_EmWHUcb_ntKDXYuveEx_fyrjKOkL_10kA3tgzWFxytGbvTmnjPvJo01DMMnt8lzwxDs5ocUbu8Css5DToKKuaECjysGXWgjHZdZG3KAfpZbDlovmF9sMJ1weRN4CybZ_HIJlXhF8fB0ziiPki7-k96MCRBOEBAVuW5V53WA7pyuIbaXyGN2Mtxwl5oVMRirXV6T8PkfcCbPdGlGGbWAq8B8vdIE9vZ8XD4WhucVKFtNuRyen7oPSGcwloViFYmzbc1jAI_HvBbXOoNiyisjEbmGC8SF6N36uqnGl4Pq1zpuL5zD8iFIivoFzB6XajZug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قاليباف يلتقي برئيس مجلس النواب العراقي هيبت الحلبوسي في طهران</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/naya_foriraq/80686" target="_blank">📅 10:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80685">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b9b81b411.mp4?token=VFks9gBkyd_vhXowtDd44LRG7o0S4sr7LwvST3kT7aomWtg2g9O5MEPicum3Ltck3UuCXXFiA_AM3UhtS7XGSG-Tei9NKsZLhdJgkJOCcAD0R6cqVZnVS0br4ZDQ0nkQ7aGv47WIn-datdVjeryCK976oWRa9cxP4AgmZ8O7SYPLYwAYuthgq4zADz0u5qCG6KBpuaFott2xJ6XUofE4Wib5jYLu2xxTVIy4XIRlH2uPbsROwocz1mt9690KURxc12vqn2GJv-LlKU41p8aLuLlgEqzn4tj9Ow1GYEahtfZxXXL-6ZPFHXv3upZ7ZXpw_UnSbNYl8ymkbpUfUpcmKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b9b81b411.mp4?token=VFks9gBkyd_vhXowtDd44LRG7o0S4sr7LwvST3kT7aomWtg2g9O5MEPicum3Ltck3UuCXXFiA_AM3UhtS7XGSG-Tei9NKsZLhdJgkJOCcAD0R6cqVZnVS0br4ZDQ0nkQ7aGv47WIn-datdVjeryCK976oWRa9cxP4AgmZ8O7SYPLYwAYuthgq4zADz0u5qCG6KBpuaFott2xJ6XUofE4Wib5jYLu2xxTVIy4XIRlH2uPbsROwocz1mt9690KURxc12vqn2GJv-LlKU41p8aLuLlgEqzn4tj9Ow1GYEahtfZxXXL-6ZPFHXv3upZ7ZXpw_UnSbNYl8ymkbpUfUpcmKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود من البرلمان العراقي واقليم كردستان العراق في حضرة السيد الشهيد القائد علي الخامنئي.</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/naya_foriraq/80685" target="_blank">📅 10:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80683">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735bf69606.mp4?token=Ew7ZYHvEifiHlByBkp2Qxy96d0U5zEmwIXFDlH7H3lEYcXvnu9vkaHBZvegSzdJh7zv5kJ-p6odTALfKRby0iLKhRxppE9OOz8BUeJcOBI5Vw0KEj3BUicCZna-Se7xJaLVIXrmeR1eBKXSitYfLULqALvOCkj_W3Ka223VdFrFb1Rhzw47gxuibkOmvvv2eJWq8E4O154hYflq0pMECo3-wnyf_7Hs0H_f7gnPsrSlXv8jYSDXMwZiH_SLM_Gnbz8qJvJAYztW4Bu9zt6VcEdyqQ_gRHFPyzGD08oAGFgQglRAW_wEgxD4t8xgcIPf6waqCuAlkr2npPEpV6W-oPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735bf69606.mp4?token=Ew7ZYHvEifiHlByBkp2Qxy96d0U5zEmwIXFDlH7H3lEYcXvnu9vkaHBZvegSzdJh7zv5kJ-p6odTALfKRby0iLKhRxppE9OOz8BUeJcOBI5Vw0KEj3BUicCZna-Se7xJaLVIXrmeR1eBKXSitYfLULqALvOCkj_W3Ka223VdFrFb1Rhzw47gxuibkOmvvv2eJWq8E4O154hYflq0pMECo3-wnyf_7Hs0H_f7gnPsrSlXv8jYSDXMwZiH_SLM_Gnbz8qJvJAYztW4Bu9zt6VcEdyqQ_gRHFPyzGD08oAGFgQglRAW_wEgxD4t8xgcIPf6waqCuAlkr2npPEpV6W-oPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود من الاحزاب السياسية اللبنانية تودع الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/naya_foriraq/80683" target="_blank">📅 10:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80682">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a31886a48.mp4?token=awldgQv6aQPyUcra4IQyMklWL0KZsCTam6u5YTrF8Vsry8LEwvtthl3o4fwo7RpZcaoe3gQAE9vUN0HvU3xpmqd9fo1RKDdF62NEVG-LAslMs0IV4eK9H_8-k38RB5MhWCqCKtZXsDBarkQ4VqlrBLP02LeVat1o6R1X1FniSVuPoxibTkRCucar135mOppjtEIWcooMh0Qau8d5_CGkBYx-i3xuo3IAz5d5z5iDcUfLQrzDgPP32KA7qVp5uLoNRxT_vBN38Ru9FMF_rAHBH5bZOHaB6hvdMNhZehJx2sYj8-x1WPE2vKohrdUXRDuqnzf1kRJe9-0vjYP2MYTsug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a31886a48.mp4?token=awldgQv6aQPyUcra4IQyMklWL0KZsCTam6u5YTrF8Vsry8LEwvtthl3o4fwo7RpZcaoe3gQAE9vUN0HvU3xpmqd9fo1RKDdF62NEVG-LAslMs0IV4eK9H_8-k38RB5MhWCqCKtZXsDBarkQ4VqlrBLP02LeVat1o6R1X1FniSVuPoxibTkRCucar135mOppjtEIWcooMh0Qau8d5_CGkBYx-i3xuo3IAz5d5z5iDcUfLQrzDgPP32KA7qVp5uLoNRxT_vBN38Ru9FMF_rAHBH5bZOHaB6hvdMNhZehJx2sYj8-x1WPE2vKohrdUXRDuqnzf1kRJe9-0vjYP2MYTsug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عائلة السيد حسن نصرالله والشهيد القائد عماد مغنية وقيادات المقاومة في لبنان تودع إمام الأمة السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/naya_foriraq/80682" target="_blank">📅 10:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80681">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c36e33cf4.mp4?token=ci-zYOS_s1_fwtTf_u3El0LHQ_H6MUZTG3pVkqa8TBZQMguWC97aG00iXSif80xhyhPxmK0MVF7pau1_BRXmecZei9SmvaFExD80VRSTPbBO8VFblQTrLdm1GA4xD1_Db6OA3ovHd-ex-yF7IDZIuEk_oqOCB5UsikUkT59B0uBVRSuLmjVCZvvpbCuTtydMnLf8JxNiS8DOuYi3jcLSmPLzBbgFoHIzC_8YQ9u7BChx3PlDH-EwVXZiIaB3GOhfNLGRN-k93mf3mSjBYJ91BeNdwQvVH_8zBnoqNdiAw4p3k9P-NwblDp1ht0LUf4_Cm4A8bEjdpURr6e3C2QI7z0eAl3oPicw6Kcl4SO2zobEW4Yr1TV5d1gmMRIBvMB_Qr2kSXQUrDydtKidioabTotvrWKRplSeJ5LMOEj5fHSLYzFas-C0_j4ylre7FK8N5QGZ7Cg0o65crF1tOHWgxnI8Vs530i_v6ms2zhxo6JpT_FxaTnotmqQuiotZunUw6_0An8lmweTdyziX7nBeGbvukgVSx1gjKpajw5veocFonNB1rQwmi4v2bO6MMrZb3odgUDOLYQlYrqYoMwtZw9dU9rz7pmZb8HAA1BUankzv8ju2L1blJo1fri6mkTHTFa-k0v5AVYUmF0fRpSnaIIIOwzj_TMg3A8atIJazwpMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c36e33cf4.mp4?token=ci-zYOS_s1_fwtTf_u3El0LHQ_H6MUZTG3pVkqa8TBZQMguWC97aG00iXSif80xhyhPxmK0MVF7pau1_BRXmecZei9SmvaFExD80VRSTPbBO8VFblQTrLdm1GA4xD1_Db6OA3ovHd-ex-yF7IDZIuEk_oqOCB5UsikUkT59B0uBVRSuLmjVCZvvpbCuTtydMnLf8JxNiS8DOuYi3jcLSmPLzBbgFoHIzC_8YQ9u7BChx3PlDH-EwVXZiIaB3GOhfNLGRN-k93mf3mSjBYJ91BeNdwQvVH_8zBnoqNdiAw4p3k9P-NwblDp1ht0LUf4_Cm4A8bEjdpURr6e3C2QI7z0eAl3oPicw6Kcl4SO2zobEW4Yr1TV5d1gmMRIBvMB_Qr2kSXQUrDydtKidioabTotvrWKRplSeJ5LMOEj5fHSLYzFas-C0_j4ylre7FK8N5QGZ7Cg0o65crF1tOHWgxnI8Vs530i_v6ms2zhxo6JpT_FxaTnotmqQuiotZunUw6_0An8lmweTdyziX7nBeGbvukgVSx1gjKpajw5veocFonNB1rQwmi4v2bO6MMrZb3odgUDOLYQlYrqYoMwtZw9dU9rz7pmZb8HAA1BUankzv8ju2L1blJo1fri6mkTHTFa-k0v5AVYUmF0fRpSnaIIIOwzj_TMg3A8atIJazwpMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود إعلامية من العراق ولبنان يؤدون التحية إلى الجثمان الطاهر للشهيد القائد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/naya_foriraq/80681" target="_blank">📅 10:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80680">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkDsxYHn1EvH-n_A2V1nsjTd7vwSgPyIIM3QE1jCTbgQ4-2OaIZW3C-yuzQ9bzF8NJOUbfI067tdUaphHpxTSJtMjue5Tdx8FStjG40G9jzJ1DsEfmb1PTDkpuH7LmhG2rbpQDu00UAaa73PDNpF9qplw5UPBKUERZTzCe-FFaYQJeYIRQluRCxX6BgIl2M8qQTveVekWCZFm9JGr-DI34Qwx7Pk0UaKOQKSzzQS4B9BbNjBk27S3Tmd5ZW6IFnHjguVxMGbmuEnGAdqVLOuzd5wGLFuCITtoqVm8zX2qHHGzuru445um6GWYC08D1GoLp7EGUn4ZfUiV8woTAYMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف يلتقي وفداً من حركة أمل اللبنانية الواصلة لوداع السيد الشهيد على الخامنئي نيابة عن الرئيس نبيه بري</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/naya_foriraq/80680" target="_blank">📅 10:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80678">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a61c2f6831.mp4?token=RW7iQmJdd2U9PcZEg-UDZ2xg9yijX5d05xZsHJzCudUEnpMBLN7gsCdbDwxJdRpVa6HPBrxCTNog73KTIqMRG52IGip0P5p3dJSzDPNTztuM49hTsw1K-its6pFoYF1yN384sVoGiAPzw-WnRYbKevHL_H8yvl4G3VGnGg9E7J_yVv6_PlUHvMQ6lsEWPJI5P9KCqMXMk71AOvfzLpZHU7cwW7uHFDxYUWvS0qwymwQzPXDxe4dknXUWDaCKzmYjocdFVdk125_Jm6-mYY1mRmq3MAj73PN3ObePQ10Pnz6IlgnI_6tbYKD5-eU7AckOGwXK87YaUhnlYhIe021VAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a61c2f6831.mp4?token=RW7iQmJdd2U9PcZEg-UDZ2xg9yijX5d05xZsHJzCudUEnpMBLN7gsCdbDwxJdRpVa6HPBrxCTNog73KTIqMRG52IGip0P5p3dJSzDPNTztuM49hTsw1K-its6pFoYF1yN384sVoGiAPzw-WnRYbKevHL_H8yvl4G3VGnGg9E7J_yVv6_PlUHvMQ6lsEWPJI5P9KCqMXMk71AOvfzLpZHU7cwW7uHFDxYUWvS0qwymwQzPXDxe4dknXUWDaCKzmYjocdFVdk125_Jm6-mYY1mRmq3MAj73PN3ObePQ10Pnz6IlgnI_6tbYKD5-eU7AckOGwXK87YaUhnlYhIe021VAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود كبيرة فلسطينية تصل لوداع السيد الشهيد علي الخامنئي</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/naya_foriraq/80678" target="_blank">📅 10:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80677">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c971af3f.mp4?token=sUek6XXjlqVDFAroeyjS4pMGOv4fY-O8imcPYvea-bbLu0zbyIiQZd7uN_QKGUQ0-oKZj8m8STnX2qIc0ruHBU6tePud_P59O5RopHIjL8VuRHKxKaRlETtuR7rUhvvWKuu6LTGzJkiPEAVc6yjWXzXqVFw70NWcbPNu_imBr5P-09hA5ItADPHgvlMq4s_vot6OyCJVLB5h4iTerozPzZUsOt6b20Mj4CpeLcXYO8rW0DAIhHRkhaWlhsF-QIYCr9nbbgXL3ndIyfH-R_VMAaxRwoL4XdHyoseX_6Bd1_x_XFptMuexV0-xOi-QL3e_OMyVT83S-jm1BQ2dm7MKNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c971af3f.mp4?token=sUek6XXjlqVDFAroeyjS4pMGOv4fY-O8imcPYvea-bbLu0zbyIiQZd7uN_QKGUQ0-oKZj8m8STnX2qIc0ruHBU6tePud_P59O5RopHIjL8VuRHKxKaRlETtuR7rUhvvWKuu6LTGzJkiPEAVc6yjWXzXqVFw70NWcbPNu_imBr5P-09hA5ItADPHgvlMq4s_vot6OyCJVLB5h4iTerozPzZUsOt6b20Mj4CpeLcXYO8rW0DAIhHRkhaWlhsF-QIYCr9nbbgXL3ndIyfH-R_VMAaxRwoL4XdHyoseX_6Bd1_x_XFptMuexV0-xOi-QL3e_OMyVT83S-jm1BQ2dm7MKNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جبهة تحرير فلسطين في حضرة الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/naya_foriraq/80677" target="_blank">📅 10:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80676">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906f02df65.mp4?token=nhvJeLijqtEwfpr4CuSdpPK6iGmhx4AafrurHJSq0MkEd5J3BqXIEDnCPgcs3EPUhevneyoh-BGB9BawS6q3TI0vaLq0h95zPwyYeOVpCqE9Ic_PtgeclmnOL8VDUsrg4XZ48tOH9yIAIGHFWf9NEp1e9gtQNisUeOvC_5aVxrL7piC7SAnCNubzo_ak1ZyZa-p2tCiN_WLTtPGuuISIjIfHP9sHNd1vCuyQzCSk15vWZ12a4iirOcTlJr7hHbTD40B43c-EwL_EuOyRfwN1IiXXy3tFQmasAtdd8PB2DdiMyGMRnf7Cq3UH9qnZSsYq6ppEhYCQ4yiYAqlPqg9rVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906f02df65.mp4?token=nhvJeLijqtEwfpr4CuSdpPK6iGmhx4AafrurHJSq0MkEd5J3BqXIEDnCPgcs3EPUhevneyoh-BGB9BawS6q3TI0vaLq0h95zPwyYeOVpCqE9Ic_PtgeclmnOL8VDUsrg4XZ48tOH9yIAIGHFWf9NEp1e9gtQNisUeOvC_5aVxrL7piC7SAnCNubzo_ak1ZyZa-p2tCiN_WLTtPGuuISIjIfHP9sHNd1vCuyQzCSk15vWZ12a4iirOcTlJr7hHbTD40B43c-EwL_EuOyRfwN1IiXXy3tFQmasAtdd8PB2DdiMyGMRnf7Cq3UH9qnZSsYq6ppEhYCQ4yiYAqlPqg9rVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الناس الشجعان تتهافت عليهم الكاميرات والجماهير
نحن نحترم الابطال الشجعان</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/naya_foriraq/80676" target="_blank">📅 10:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80675">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9716e3e815.mp4?token=FDScCs8Kze98r3jq6qPOKih2z8PDyzF_PSRmNnsZuWp22VCzRb8cBuXn0nKYIVfHsGFhH1HYEcM5NRVp8NwrFy3ZrkyUHGBgS7eTlPjSD6DfHNFpdI9qOeY0Sx75uP6k5kGmhWeWZDBERatN5HmHEI9iD2oNciZH5kdieNtfisIvEikFHdjH8SuWHWbQPfnxL_UoOyeV6pt7Yi8aUWsPxWC9HTNn0dLXXP1Ix0wQU-OBlnfft3u32SuHZkFp1bKf3Ih_vQCdZJwGvLDSRuok9-09LCLyMws4YPhevQ6r_aj-KWG_QOTbcq957CtngDpxWVly20YzrAsPC6XQrMtLxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9716e3e815.mp4?token=FDScCs8Kze98r3jq6qPOKih2z8PDyzF_PSRmNnsZuWp22VCzRb8cBuXn0nKYIVfHsGFhH1HYEcM5NRVp8NwrFy3ZrkyUHGBgS7eTlPjSD6DfHNFpdI9qOeY0Sx75uP6k5kGmhWeWZDBERatN5HmHEI9iD2oNciZH5kdieNtfisIvEikFHdjH8SuWHWbQPfnxL_UoOyeV6pt7Yi8aUWsPxWC9HTNn0dLXXP1Ix0wQU-OBlnfft3u32SuHZkFp1bKf3Ih_vQCdZJwGvLDSRuok9-09LCLyMws4YPhevQ6r_aj-KWG_QOTbcq957CtngDpxWVly20YzrAsPC6XQrMtLxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس الجمهورية العراقي يصل إلى مطار العاصمة طهران</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/naya_foriraq/80675" target="_blank">📅 10:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80674">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cb65272d.mp4?token=BxuQ2AJn0Wn1067bg4sa3f5d8Z0jA6JgHAHORv6EqHuM45zr-s5h-Q6303s-lubKZWQrWI6I7kk_1xQNM3qJMklx_ZZLqA4WOSo302jS4OA65XYGWvwSeKOcx5sQ7-cYeOtKvm9g4ztg0CJz4nkrpVvjA4yz8S1XPWFjtKZRyu1jtiYCkZboM2e1vpMxPOEDTkMdIPVs7OYuwevBscDdN7BshyJkphn5KPlrqlqDlmh6WVs9z6-DU3VNpQ6eLoozp-WESU4f-StrR1HZji4oAiprUGTAue9zby7xnYSFdYA_2ZIKPlZecWUNZjyDNUqTKihchxtHl8UUfsJC5CULJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cb65272d.mp4?token=BxuQ2AJn0Wn1067bg4sa3f5d8Z0jA6JgHAHORv6EqHuM45zr-s5h-Q6303s-lubKZWQrWI6I7kk_1xQNM3qJMklx_ZZLqA4WOSo302jS4OA65XYGWvwSeKOcx5sQ7-cYeOtKvm9g4ztg0CJz4nkrpVvjA4yz8S1XPWFjtKZRyu1jtiYCkZboM2e1vpMxPOEDTkMdIPVs7OYuwevBscDdN7BshyJkphn5KPlrqlqDlmh6WVs9z6-DU3VNpQ6eLoozp-WESU4f-StrR1HZji4oAiprUGTAue9zby7xnYSFdYA_2ZIKPlZecWUNZjyDNUqTKihchxtHl8UUfsJC5CULJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شيعة الهند وتايلاند وألمانيا يقدمون تعازيهم في حضرة الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/naya_foriraq/80674" target="_blank">📅 10:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80672">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007756c400.mp4?token=D8KO4DTeEsYoPRs0kKzyXQhAjbb54t1cxMGP3WADh3-9u8qVDRcBDZfMDg27Z1Aj1qnuvkIjb4umcyvBTZG5qR0xHDulz1xAoUgA4XZZ9p0vvefZ0WR159tgibJRl--kQxZ5sUSxD_Ut_di7Z0d7jTPjmAZng2fpSPzkBDeM_WK19_vpjXJgIIY34Tttjmxfhi1sA0a8aExJT635TtGT-GVNmLFNCEnl1yBXF1rfZ4sNSc1k7lF2qN3-81ong5URTNC8VcqddWmB1YGcRWKY_hEB-c4M1nKzhK_9iey1KkGa6cVIbTY-CuDFKsUIat36mNHfezBseVITCEPH4YnOxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007756c400.mp4?token=D8KO4DTeEsYoPRs0kKzyXQhAjbb54t1cxMGP3WADh3-9u8qVDRcBDZfMDg27Z1Aj1qnuvkIjb4umcyvBTZG5qR0xHDulz1xAoUgA4XZZ9p0vvefZ0WR159tgibJRl--kQxZ5sUSxD_Ut_di7Z0d7jTPjmAZng2fpSPzkBDeM_WK19_vpjXJgIIY34Tttjmxfhi1sA0a8aExJT635TtGT-GVNmLFNCEnl1yBXF1rfZ4sNSc1k7lF2qN3-81ong5URTNC8VcqddWmB1YGcRWKY_hEB-c4M1nKzhK_9iey1KkGa6cVIbTY-CuDFKsUIat36mNHfezBseVITCEPH4YnOxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد من علماء روسيا في حضرة الإمام الشهيد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/naya_foriraq/80672" target="_blank">📅 10:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80671">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204fb36bdd.mp4?token=LefZ66EW_zt0rs_VknBeNz2N2gtaviSUnaFvTl0BIDl48FTsvKHZg8_jQEo9OPc6545K5habMxa5x-lBUqFvrS7dw_Rmfuk8h2lm9MMsuW7cpaWQRv77OOhJ-UXcE28kJWrsi6fI8_GqWfVBuf44i8ZB3NqLxo_673Uz9oCwDHrEl85JwnLFnUEFL0uq0dH-dTNQxcLfxzOyUrR8hlmD_l8NMtmqSKwB0eWcXAXBh4_DG-MaXiH4BtvasMIORiQS-_02VJJQNAabdOn9l1AVB-8bOBInPf5cF6lHu71k50i3vWAIhqo4xTl8CqFCcMPaHlZwRcLjG5NeFj0eoeW2uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204fb36bdd.mp4?token=LefZ66EW_zt0rs_VknBeNz2N2gtaviSUnaFvTl0BIDl48FTsvKHZg8_jQEo9OPc6545K5habMxa5x-lBUqFvrS7dw_Rmfuk8h2lm9MMsuW7cpaWQRv77OOhJ-UXcE28kJWrsi6fI8_GqWfVBuf44i8ZB3NqLxo_673Uz9oCwDHrEl85JwnLFnUEFL0uq0dH-dTNQxcLfxzOyUrR8hlmD_l8NMtmqSKwB0eWcXAXBh4_DG-MaXiH4BtvasMIORiQS-_02VJJQNAabdOn9l1AVB-8bOBInPf5cF6lHu71k50i3vWAIhqo4xTl8CqFCcMPaHlZwRcLjG5NeFj0eoeW2uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نيجرفان بارزاني يلتقي الرئيس الإيراني بزشكيان في العاصمة طهران.</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/naya_foriraq/80671" target="_blank">📅 10:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80670">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79d0a2771d.mp4?token=NtORTpVCPowoewszSVZBS-hcWjbEWb1xqSZe6oLPnzZ3Y78PndUJnp-EqCi3vnUBlm9kVIw7ZUsIDf84sDCBg-pMNPo8Crmgo-IMph-oxcxEZMR_zcSXh7fwgnlYl9pnnW43APOMWi6BLNZY8IGoYGm_oq1e_pO2d_tmxByfjSEyR3RlRyhfb56a9ggg36QW8IXXI5cXOxiMacJce9eoPHckaVp85FDSwyhTzQ0cBhaeSR50_dvvO8jOJFW8WNJ_f3EBS88n2WszsNXEyrr-1hlQ4FJUAqrZ_l3H-9NJBsxxygRcZQ2FcHrQhEHB3lVLAeWaq9KjTSRo4DA3aLFs0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79d0a2771d.mp4?token=NtORTpVCPowoewszSVZBS-hcWjbEWb1xqSZe6oLPnzZ3Y78PndUJnp-EqCi3vnUBlm9kVIw7ZUsIDf84sDCBg-pMNPo8Crmgo-IMph-oxcxEZMR_zcSXh7fwgnlYl9pnnW43APOMWi6BLNZY8IGoYGm_oq1e_pO2d_tmxByfjSEyR3RlRyhfb56a9ggg36QW8IXXI5cXOxiMacJce9eoPHckaVp85FDSwyhTzQ0cBhaeSR50_dvvO8jOJFW8WNJ_f3EBS88n2WszsNXEyrr-1hlQ4FJUAqrZ_l3H-9NJBsxxygRcZQ2FcHrQhEHB3lVLAeWaq9KjTSRo4DA3aLFs0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود من جبهة المقاومة من سوريا ولبنان والعراق والمغرب وتركيا يصلون لوداع السيد الشهيد</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/naya_foriraq/80670" target="_blank">📅 10:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80669">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c74abecf.mp4?token=CPDwroqZqQbE9skcz4y768_btWYbZTptQZw-UUcrcyD5hgv7YGJV8rvpCvttroJxML4-wyhaVzK433iaXM20_2kltmZItoKlp7vsx5ELY5ah0tPVFrcNTDLMAzeuDCm42WFyCVz0BxU_Lfd8bHcEh5yiNbPZiYtDCK-iAAbA5jOwc_H93q8MROYivyq8ihzL0pXRr3FMq4EOO_jz-hhY8_9CLuoCUiDJszsUgGtKAkxU6J87qU-1bxWToNUxJRk8TUUKyz2U3OA0ome6OvpsnvSpb5kSbcDVTXwgM954Qdh58DdCrgq7yQYgLSbTaWDCl9eb7mAat95VpwRrXNdEXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c74abecf.mp4?token=CPDwroqZqQbE9skcz4y768_btWYbZTptQZw-UUcrcyD5hgv7YGJV8rvpCvttroJxML4-wyhaVzK433iaXM20_2kltmZItoKlp7vsx5ELY5ah0tPVFrcNTDLMAzeuDCm42WFyCVz0BxU_Lfd8bHcEh5yiNbPZiYtDCK-iAAbA5jOwc_H93q8MROYivyq8ihzL0pXRr3FMq4EOO_jz-hhY8_9CLuoCUiDJszsUgGtKAkxU6J87qU-1bxWToNUxJRk8TUUKyz2U3OA0ome6OvpsnvSpb5kSbcDVTXwgM954Qdh58DdCrgq7yQYgLSbTaWDCl9eb7mAat95VpwRrXNdEXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الفاطميون من المقاومة الأفغانية في حضرة الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/naya_foriraq/80669" target="_blank">📅 10:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80668">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCxOdRGet-mnEZ2VkFiMOZn9NgoDUb1hWEL59iDHg-UxbxnjTtyInjWtlGZh4HB29Fl2qJjp4JIpPaqJXLgXTKUSbFdztRHb3APiJsHTT_NR8SRt-DsiKAIFLz7r3O8xuwfnpFszV0StGybx6PeeZl-Qgc6--NqrfDZjwn77ShteEhhO66iPaX5Fl0mFBBxHz46K5iZHPEfvwXsrK2VifGQB-dkBQqP4RRhUUW_7bEeN1T2Qqqvs-9p9nmue1aHd2Dy448pCT_8YW1iPRa4HYazz1kpy2N76e6fRKSg85ZoAeKXGm0Pt9QjAqrx8BUVYQYWVxKRIwo-fKuOZGgHupw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الوفود العراقية برفقة نجل الشهيد السيد حسن نصر الله في طهران.</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/naya_foriraq/80668" target="_blank">📅 10:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80666">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jm_QJc7vJvYF6_e_GGJgxJrF043numJvZSxT0UhlKA3ulmr-QQMBbD4TVDhjI2r1H_UkQczePU12Ghp0RM-z0W7haVWDvSyHtCt2zsYImn_sJ0m63nIoR_bYdEEQSgVyqylVRlh9PqcYG1neyZ_cqgt1B7r9Bl71VEt_m6HT0arz25rum2_U2YIxSRqlq8cok6zBD6N-ldNl-GUqYkMWXgllrhheZQzDFsCJv2XAliMft3fVneBFMr_PizYTWG1mBPuadTm42qflAebc3KwP8__sbI_OwsxzPjjYUOQBJhejle1tJdxC_owjNaw0yqoLRLBkzCK1axwtRGEHmGm6Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QZtXncATIbDqsDD-TjTzmI_yQOFIFNdIG5JLrafj9S6dMXCs3lEJE_90rf9JRurrHwyT45T03sGfxmbDjX6LWVFrhF5NIS0yYLHJwqcD2bgHRYy_-gQCyUVisYErd5wV2OCRovskCOlctZQw19X4G-J3fEg1djftIPnQ9-ddmWqtxC3PY09IaBW-ztYve6XfoCY6ZBaF5Z0qjG9erQZySLIVrhZnmvjRB2pdcPE7oo8gVqLxlSOWemg-vEQMd7d2KdyWbUIsNYZGowKYBM3clKG5RFfm1Bn1jO9HJrBKggLdWVYUoldRy7qEYImepX7LZT2BzKzK5wTsDhZd9yPxkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الشيخ اكرم الكعبي وأبو الاء الولائي من طهران خلال مراسم توديع السيد الشهيد علي الخامنئي</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/naya_foriraq/80666" target="_blank">📅 10:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80665">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/846eb2bb69.mp4?token=DNhbEfZUmQPZA-nwRgcSYh-UxTmOeoqYrwcfjG7V_yvoChRge5AC6afMNTmsKJXiDCX-srpdtyZemKb-9A6lRzYWe7G3Mjyb8MU78nPDyjwDIMIeNG39lKKQZTflrxlnb8hfAxFQ4PKId5H3VD4Vkmhy2fPFFAVt3wIBFJersso02xIHRYUHgvww-ESIEDQC3cGjwcqqhxZ3mcCSVQIsBooBJNhBHj_uq-jkxoOjCfxA7FBGMSYRXTOd-LQPjeNDM4qtvgAEjrPCJCwjGvuQSOBYWg-BceDeMHqNRl86VlxNh6mRbz0N4jG_x3evflSuUa6C7QOQHTyrO7n8H2j0PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/846eb2bb69.mp4?token=DNhbEfZUmQPZA-nwRgcSYh-UxTmOeoqYrwcfjG7V_yvoChRge5AC6afMNTmsKJXiDCX-srpdtyZemKb-9A6lRzYWe7G3Mjyb8MU78nPDyjwDIMIeNG39lKKQZTflrxlnb8hfAxFQ4PKId5H3VD4Vkmhy2fPFFAVt3wIBFJersso02xIHRYUHgvww-ESIEDQC3cGjwcqqhxZ3mcCSVQIsBooBJNhBHj_uq-jkxoOjCfxA7FBGMSYRXTOd-LQPjeNDM4qtvgAEjrPCJCwjGvuQSOBYWg-BceDeMHqNRl86VlxNh6mRbz0N4jG_x3evflSuUa6C7QOQHTyrO7n8H2j0PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من وداع الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/naya_foriraq/80665" target="_blank">📅 09:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80664">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4990178830.mp4?token=Hep28oXnOerBNnrBrlpT6ISebF6zdr7erLqyYGiwhBCzYWFXwPinAjnZ4DT5xBsXUtXghV0mlQjWupyBiInZp7Pv_C7U0WJSiY8BQsnaYTA22pHwhXnYWKSUyz9Mvz4qfFYElbKBTGD58DoJjbQ2LM7LWyGEsOQp4GEByB72QUl25lA6A4ogqTiEuGq2BtgWmdNiqrEeIE1VF31MuoXpx4v2ZWpd3DNgdqj7tAl2rKPldZWq5MS_DS6z0M_NEJ8zgdYJXn8o_9YjsduDH91HvDUhXF172_Utt6nwCqAly4JrtomwdVcTEZrgFtGDz7s8jNZ3_kUvZt7VuQL5Hta3xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4990178830.mp4?token=Hep28oXnOerBNnrBrlpT6ISebF6zdr7erLqyYGiwhBCzYWFXwPinAjnZ4DT5xBsXUtXghV0mlQjWupyBiInZp7Pv_C7U0WJSiY8BQsnaYTA22pHwhXnYWKSUyz9Mvz4qfFYElbKBTGD58DoJjbQ2LM7LWyGEsOQp4GEByB72QUl25lA6A4ogqTiEuGq2BtgWmdNiqrEeIE1VF31MuoXpx4v2ZWpd3DNgdqj7tAl2rKPldZWq5MS_DS6z0M_NEJ8zgdYJXn8o_9YjsduDH91HvDUhXF172_Utt6nwCqAly4JrtomwdVcTEZrgFtGDz7s8jNZ3_kUvZt7VuQL5Hta3xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول الرئيس الطاجيكي إلى إيران لوداع السيد الشهيد علي الخامنئي</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/naya_foriraq/80664" target="_blank">📅 09:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80661">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hNMbGTQ7rgLr_OJoSMpgLoRa5j6WpbCslmjoXOSZe6-ife5MfyCFO2HUBLimg8-3YxwVPxL5zWQ999jmjfhgo7ed6RsWgpDV1EFi7L4qvPpd4y7TtkCcTroUZ29H-i11DCmXVKe3bGYejrJZYKQx5yKos1q1qMCfKPKD2-naYjOEcbg5S7qIVo2_UtFd21Yag53RxYaWhWm0RkukhOkfNzD_bhzMmykKQ-vJuHjde5-gnlBeodukVcJkvkxWkPUlBT1HQ5KcySxaDiDizp8XO4Ai2aTKKhmPF-Kaa9zFm4hpK3aj7YPlQWQJqPC2ASUEEdum4VyGu6azkpT9r0J7MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9ks2X7PJSCVBs83beIi2-KN1szOkACqOrZBxycibZshtU6BLmXWEImUVdb2vJQwq97Hlb4DbbGi3AS0eLvT5RjflntdBTBilqzu1-QLb1-8oGLxn_r-8ovMyu9wffwxApG3gVhKJmZDI4eFIB8hc1ePEVfw4M-bBek4RKA4MmqXZZAMH1WUngn5nxaz3XdRrk_HIInYQz5yuhYfH_CHajAkzH0OjB3baz1LUvhqx2KjJhlCxY3dhoMuXxa5OusBAEdAeY9evWFqBo_YIw9xUOZzQWGglIpCBAemvqqllPkqY6bWmQAIqoX3yv8F7-5n4Hx3_ZZJUQpMFRt8npoH-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d006a5066e.mp4?token=v1T4NyO9irq41nM1zcYNXyCRN7kI-7LtGBRMW_kBejnwUJqq735Fed1kGG5JGVA6QZgIhZMSJR7wCoosqQ9N3frehKE0io545JIZii5eb8NYC3mOA0pj11USD8DZzzcYIK3lQWpI_EkpWBduMBMDQ1QrwA9WkGRdK14kiIVNW3wXHqFyIktmE04rs3nEycv6wXcFNJEuwp_P8FJ2oYCih4tXR3MNnJ4m6gKaLenrysx-2kLziyoVtblAwYaDLMP1dDnEVILiDwe3FJAZeM4f_bFNOx94HQdMlWcSBVRlfjCvyg5ulmdWOt1Df2h9H3QguXnanlhnDwRxtjnsCYyDHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d006a5066e.mp4?token=v1T4NyO9irq41nM1zcYNXyCRN7kI-7LtGBRMW_kBejnwUJqq735Fed1kGG5JGVA6QZgIhZMSJR7wCoosqQ9N3frehKE0io545JIZii5eb8NYC3mOA0pj11USD8DZzzcYIK3lQWpI_EkpWBduMBMDQ1QrwA9WkGRdK14kiIVNW3wXHqFyIktmE04rs3nEycv6wXcFNJEuwp_P8FJ2oYCih4tXR3MNnJ4m6gKaLenrysx-2kLziyoVtblAwYaDLMP1dDnEVILiDwe3FJAZeM4f_bFNOx94HQdMlWcSBVRlfjCvyg5ulmdWOt1Df2h9H3QguXnanlhnDwRxtjnsCYyDHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لقاء وزير الخارجية الإيراني عراقجي برئيس إقليم كردستان العراق</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/naya_foriraq/80661" target="_blank">📅 09:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80660">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/292c198e71.mp4?token=Hbz31hyepoOjKxI-NhGr66CG-VZJ8DP3okp5D77jKdZlBL2mc67ifuQz3dTTjmFjKqZCuUU8tDJKY2Nm4Fh_TxhRKUvnRhtaJdZrOjWEg5kPGMgAGtQi5ribQ9qWFQw6Ax3MdkYa6pXncaFxMyiHIK1fFprtFXGpSP_XUdCo0e3bPRD1jE7FG3I9KIZZpDYRV1M05HnTwCa1YC_mod-BGILE3XIOBmhAeIdbtuIR0pDtOqE9Era_SkTnOEzj6TIA3CFGtOT8VKIYA9SCOEqTVgS4hwR6EnaAZK6jL3quv2jZDnZQNMEfpHTeIRh3x-lQWLRyy8SB6XxSb0dX669zrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/292c198e71.mp4?token=Hbz31hyepoOjKxI-NhGr66CG-VZJ8DP3okp5D77jKdZlBL2mc67ifuQz3dTTjmFjKqZCuUU8tDJKY2Nm4Fh_TxhRKUvnRhtaJdZrOjWEg5kPGMgAGtQi5ribQ9qWFQw6Ax3MdkYa6pXncaFxMyiHIK1fFprtFXGpSP_XUdCo0e3bPRD1jE7FG3I9KIZZpDYRV1M05HnTwCa1YC_mod-BGILE3XIOBmhAeIdbtuIR0pDtOqE9Era_SkTnOEzj6TIA3CFGtOT8VKIYA9SCOEqTVgS4hwR6EnaAZK6jL3quv2jZDnZQNMEfpHTeIRh3x-lQWLRyy8SB6XxSb0dX669zrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائد المقاومة الأفغانية أحمد مسعود يودع جثمان القائد الشهيد</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/naya_foriraq/80660" target="_blank">📅 09:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80659">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإمام الشهيد السيد علي الخامنئي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af5a33e00.mp4?token=GYCVkyXs2IpaB8MEM6jlAFE8cMVJibLMi02kSHELiURuTUhVQUWfbuiJLsTFhEH-rQF6mxiUwAoqZrUJqED1vyjVl1GPpK6nLGBbgOKeogVkr-r5VFJuaz8LTEqibglcjjK7Of3be0oLq4atMfRTPkv55IenkgGhWbVDf9w_V8aoA44wBWmZypqf5UGFUiGCrghkNRHpaKONgzAnI7hnjNXMtZSgkXQGOVan4RcdfhtHUY04pw0V5AiDH0phP7mM0yxx2aTSGQebWJWR5ONSbr9_a2ZswXX26pycFT1m6OAdIExjteqD_TxBQWxK0CF1Zbu9izkaJ6pcUNTxUZ5tGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af5a33e00.mp4?token=GYCVkyXs2IpaB8MEM6jlAFE8cMVJibLMi02kSHELiURuTUhVQUWfbuiJLsTFhEH-rQF6mxiUwAoqZrUJqED1vyjVl1GPpK6nLGBbgOKeogVkr-r5VFJuaz8LTEqibglcjjK7Of3be0oLq4atMfRTPkv55IenkgGhWbVDf9w_V8aoA44wBWmZypqf5UGFUiGCrghkNRHpaKONgzAnI7hnjNXMtZSgkXQGOVan4RcdfhtHUY04pw0V5AiDH0phP7mM0yxx2aTSGQebWJWR5ONSbr9_a2ZswXX26pycFT1m6OAdIExjteqD_TxBQWxK0CF1Zbu9izkaJ6pcUNTxUZ5tGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
|
وفد حركة المقاومة «كتائب حزب الله» العراقية يؤدي الاحترام للجثمان الطاهر لقائد الثورة الإسلامية الشهيد. | 3/07/2026
🏴
#قوموا_لله
#تشييع_إمام_المستضعفين
➕
t.me/Khamenei_arabi</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/naya_foriraq/80659" target="_blank">📅 09:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80658">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رئيس الجمهورية العراقي يغادر إلى طهران الان</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/naya_foriraq/80658" target="_blank">📅 09:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80657">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d463bb3a6.mp4?token=lCNTQjqnUeHzlaIuX4Y5sUZZFioiGXPnZ0YsddvVYsz75eYQDANyOegPG6ub5AFyXlrMWQESUGr_InRcVN2AYa1_YpFFil-E9N04aCyUnN-05XuP1Ptsmzrd_maS9TyTOpD1KGiT7gGKaj0cPVBhni6wzq_r-OuH0Chp1Cm4VFRyTW6Z-D3jUB6ssgMDpd6dTzvjydgOAZ2vVyu4e_hv3ZfMqj-QoZ5wGfTs5qAyLAQaghsPFzMgfxUDgjfPx4wgYLjh20ErWxandpOG8r4iYIeRjyMMtR7ZB9biUlpJEdwXHK-PHGCL8UwnWpdKh2U5DKye-5cW-erGNBIO1dghGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d463bb3a6.mp4?token=lCNTQjqnUeHzlaIuX4Y5sUZZFioiGXPnZ0YsddvVYsz75eYQDANyOegPG6ub5AFyXlrMWQESUGr_InRcVN2AYa1_YpFFil-E9N04aCyUnN-05XuP1Ptsmzrd_maS9TyTOpD1KGiT7gGKaj0cPVBhni6wzq_r-OuH0Chp1Cm4VFRyTW6Z-D3jUB6ssgMDpd6dTzvjydgOAZ2vVyu4e_hv3ZfMqj-QoZ5wGfTs5qAyLAQaghsPFzMgfxUDgjfPx4wgYLjh20ErWxandpOG8r4iYIeRjyMMtR7ZB9biUlpJEdwXHK-PHGCL8UwnWpdKh2U5DKye-5cW-erGNBIO1dghGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حركة أمل اللبنانية تصل لتوديع النعش الطاهر</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/naya_foriraq/80657" target="_blank">📅 09:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80656">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77e9cb4668.mp4?token=gczQ-HbkVoaDx96OzlYBZ0LSc6q-EWSGFOdTHxfTAiSI13Hefwd2wiaAWLtj-02-vKUiwRYbnmE_2skoho4jvpsLr1TlvQ6yyqUatkkQ57roMgywEKIVV7b3cLVd6prrZQgzW8AK-B8OiskBPcW9pqFJ8DrhgEKPggfP_rjwLjz_Fbjhzm7rE1US1oLoI-zOX4h5IE66xA-RYShEI0OOOdqEARKwyKSQrKoX2iL6p3SDSd8iMuyCeJJSLYAh-WxbN_1wt61pRFED7wwW8MsV9FHwDZNYiHvqbIYuSo_0KhT8kDRzznpsO6Wt0JqXh-c3bir3P978ixSriA4-9OgNqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77e9cb4668.mp4?token=gczQ-HbkVoaDx96OzlYBZ0LSc6q-EWSGFOdTHxfTAiSI13Hefwd2wiaAWLtj-02-vKUiwRYbnmE_2skoho4jvpsLr1TlvQ6yyqUatkkQ57roMgywEKIVV7b3cLVd6prrZQgzW8AK-B8OiskBPcW9pqFJ8DrhgEKPggfP_rjwLjz_Fbjhzm7rE1US1oLoI-zOX4h5IE66xA-RYShEI0OOOdqEARKwyKSQrKoX2iL6p3SDSd8iMuyCeJJSLYAh-WxbN_1wt61pRFED7wwW8MsV9FHwDZNYiHvqbIYuSo_0KhT8kDRzznpsO6Wt0JqXh-c3bir3P978ixSriA4-9OgNqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفود العراقية ضخمة جدا ومستمرة بالتوافد</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/naya_foriraq/80656" target="_blank">📅 09:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80655">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وفود كبيرة جداً من المقاومة العراقية منهم السيد صلاح يصلون لتوديع الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/naya_foriraq/80655" target="_blank">📅 09:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80654">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/253b6da29e.mp4?token=XRNOCqpjJd3D-fFQPZv_9JMUnIixllS5phI0pWsNhCAkmdv7f6NLLh_MdByYIhzuqlahbeEN6Mi2IiUFNXotFX4p_q5u25I6s8uDPKTf9Zl8RPDVxGGyKxdE8efRX5CIb9sbPHoaTfSMlsTZ6WljCAPpHZ6ijJGTrMH4ipqUn2GkvHLntJFPqaJGt7RGW4mN6U-xZSel_l-fEVkS6R7KNK0T3hPNL96TKT9hNiMplPZICpM971kCcMPWkEw4iJcDybSIxuYUnA_DO2luTdbI8U2wh8Jr000BnM6Zk2CZlk26-5a7XZMhrQbA44rD_3RcnX8EhuxD0V2dEsdMH1Uj3Y2ItbUjf0cPYWT8JH8v9VagBeYciY5VuT4hyDmS0FrSuH8G1JqX76t2C_fGMHJvKjq2jsKU-LwGhU8PvX5WrUlDVSPWsYCSJ857bWtoPcjuijmK5H8x5DUnZv6aPed9oJ7yoKKtubjP9qoRjIvk0X54OpIMWq2INEwi0rUU77uGd7gKDczV_AYDGUCJTGQGnFoI8JAsAyIZdcN2u2wERHa2cNuspAd76pTGxx85t2DfQaq4I-DX_XDQTzi-2fLqEZytBebqQUdSYAiSqzk8E4l6U0Rz2k4qecHxlkFIYyvKEjhnmxYck_kXO8OONJXJ7TENJgmkqHv0C8tFPD7wqF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/253b6da29e.mp4?token=XRNOCqpjJd3D-fFQPZv_9JMUnIixllS5phI0pWsNhCAkmdv7f6NLLh_MdByYIhzuqlahbeEN6Mi2IiUFNXotFX4p_q5u25I6s8uDPKTf9Zl8RPDVxGGyKxdE8efRX5CIb9sbPHoaTfSMlsTZ6WljCAPpHZ6ijJGTrMH4ipqUn2GkvHLntJFPqaJGt7RGW4mN6U-xZSel_l-fEVkS6R7KNK0T3hPNL96TKT9hNiMplPZICpM971kCcMPWkEw4iJcDybSIxuYUnA_DO2luTdbI8U2wh8Jr000BnM6Zk2CZlk26-5a7XZMhrQbA44rD_3RcnX8EhuxD0V2dEsdMH1Uj3Y2ItbUjf0cPYWT8JH8v9VagBeYciY5VuT4hyDmS0FrSuH8G1JqX76t2C_fGMHJvKjq2jsKU-LwGhU8PvX5WrUlDVSPWsYCSJ857bWtoPcjuijmK5H8x5DUnZv6aPed9oJ7yoKKtubjP9qoRjIvk0X54OpIMWq2INEwi0rUU77uGd7gKDczV_AYDGUCJTGQGnFoI8JAsAyIZdcN2u2wERHa2cNuspAd76pTGxx85t2DfQaq4I-DX_XDQTzi-2fLqEZytBebqQUdSYAiSqzk8E4l6U0Rz2k4qecHxlkFIYyvKEjhnmxYck_kXO8OONJXJ7TENJgmkqHv0C8tFPD7wqF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود كبيرة جداً من المقاومة العراقية منهم السيد صلاح يصلون لتوديع الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/naya_foriraq/80654" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80653">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8eea18a41.mp4?token=S8TLP8hlmQaLom4xANmTxgKjEFhH7b-8ExlBafxm3HfrnnEKHG-_Ghz0koYTxqH1yIO47JNE03WvZTsqMoEa5Um3GMTRACW0jZGJmejhLfIIj_pBE0RyuCqDmBFTwM6VWBZ875Domu8nChkcx954hVWxs6I8RUpTM17KR17vvASGYVpfwtbR9WLAl-fhohMjq7L8hj0aNFV3lFmSyGp2gpXNkxA6ryAqcKVDgO8HjsH5cZanHrBdpvVPwwEIyPKju7T3aBlSWpcbvqlwB_QXdeIFXxnhzmRh2pvEtfJYxdeu7u9eQwVneSa3RuRMaulixpMut8oQc65HEd_6YaPDyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8eea18a41.mp4?token=S8TLP8hlmQaLom4xANmTxgKjEFhH7b-8ExlBafxm3HfrnnEKHG-_Ghz0koYTxqH1yIO47JNE03WvZTsqMoEa5Um3GMTRACW0jZGJmejhLfIIj_pBE0RyuCqDmBFTwM6VWBZ875Domu8nChkcx954hVWxs6I8RUpTM17KR17vvASGYVpfwtbR9WLAl-fhohMjq7L8hj0aNFV3lFmSyGp2gpXNkxA6ryAqcKVDgO8HjsH5cZanHrBdpvVPwwEIyPKju7T3aBlSWpcbvqlwB_QXdeIFXxnhzmRh2pvEtfJYxdeu7u9eQwVneSa3RuRMaulixpMut8oQc65HEd_6YaPDyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">يستمر الوفد العراقي الأكبر من قيادات الحشد الشعبي المقدس بالتوافد ؛</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/naya_foriraq/80653" target="_blank">📅 09:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80652">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08c2840f4a.mp4?token=aPNiSD1egQ8svhbxygfVqVNtuda79G0Dyd1rTFDtPO2upjVQJyjnkce-_9rMnQ8aa2QdvX0FEpzl7MJNJWEV5A40o8pSkPPOjYeD26yKtrftcvisXv6HVJUPjoTtBSfAky1FGiPGawB8_232vS19mvAZ30JQmMnS_eplRuEcat0AcMMtZNiyX55vhuJxoEYMLxTIQUaMkM42jmtdWbG7wsdbB8ptUxKGMs0rPID02vKmi0T2YKAJ_iU8Zqb-f1n0-JDSkxRuhsqCpVSlOukuT9iW-nS1ItMhVdAr4wqvR89EJT-lIOKW14711IPeD23HpDsF004tytxyJQV8XJ04aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08c2840f4a.mp4?token=aPNiSD1egQ8svhbxygfVqVNtuda79G0Dyd1rTFDtPO2upjVQJyjnkce-_9rMnQ8aa2QdvX0FEpzl7MJNJWEV5A40o8pSkPPOjYeD26yKtrftcvisXv6HVJUPjoTtBSfAky1FGiPGawB8_232vS19mvAZ30JQmMnS_eplRuEcat0AcMMtZNiyX55vhuJxoEYMLxTIQUaMkM42jmtdWbG7wsdbB8ptUxKGMs0rPID02vKmi0T2YKAJ_iU8Zqb-f1n0-JDSkxRuhsqCpVSlOukuT9iW-nS1ItMhVdAr4wqvR89EJT-lIOKW14711IPeD23HpDsF004tytxyJQV8XJ04aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد العراقي هو الأكبر</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/naya_foriraq/80652" target="_blank">📅 09:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80651">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdbIJSWp5WogQ55REvVn6kpbTSmS2amUFIUpIlu_y4Af8if3SnLxWNa20yBMvie6XNNA8gsXO8xUSYCiBbVIWS_VeidEwSr2_iWLQvpfaIgv75D49TGqOE9iXu2bwu4P3f6pCVuLcEYecA-U3ge1eVukCROlhnbNacpf3Mq-hQJRd3MpHM0ddzUD_e5HiOT0hv6SPTZtcRQ45B7GlWGEK-0ixymilr0-fA3JXumAA0TL7Yl5KLToKHxro_CW4kHffNmJd9MXaS-aXiSVPDDDr6b_O413na8g7ZZouoi3RAkRCIhPeQrG3jZHWW0eELdNU5crDjr9fJOByqh1OEENAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف يستقبل رئيس برلمان بلا روسيا اثناء مشاركتهم بالعزاء</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/naya_foriraq/80651" target="_blank">📅 09:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80650">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf31476a75.mp4?token=tbWhE1aNki0-yB8lMCsx87aZ6zrH9h9rs0aq0HhfxJPBrdFQNCTZjeLCGETj4UT96nzRNrdK2Zk-EJQ-RBIO308qi8AvMHr4mOK6yeXJkD4fq5sM4rXpgLCF8cO8Vhf2OqPXSFGtSq3t4CCPWmD979nx-0WrJ35d-R_z8NlnvKCE09GwtuON-gvNHQsOkxZryiDeo45_xaPZU0ij8eIWrcanj4IhncjuUoAhO3jraRXODE2wn7sV2WaQpJFERoiBoUmYaxhMreRWo29Btnpt4l7GiDZ1tDZNm8h06fct-xD_YrfGTfeNaln9nZPkp8MVwsGhC1RCcdYm-e-akDxN_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf31476a75.mp4?token=tbWhE1aNki0-yB8lMCsx87aZ6zrH9h9rs0aq0HhfxJPBrdFQNCTZjeLCGETj4UT96nzRNrdK2Zk-EJQ-RBIO308qi8AvMHr4mOK6yeXJkD4fq5sM4rXpgLCF8cO8Vhf2OqPXSFGtSq3t4CCPWmD979nx-0WrJ35d-R_z8NlnvKCE09GwtuON-gvNHQsOkxZryiDeo45_xaPZU0ij8eIWrcanj4IhncjuUoAhO3jraRXODE2wn7sV2WaQpJFERoiBoUmYaxhMreRWo29Btnpt4l7GiDZ1tDZNm8h06fct-xD_YrfGTfeNaln9nZPkp8MVwsGhC1RCcdYm-e-akDxN_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود أخرى من الحشد الشعبي العراقي تودع الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/naya_foriraq/80650" target="_blank">📅 09:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80649">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65354c2ec7.mp4?token=dBXiJTw7kPI5bzTW1cOTnOKEcu9h3sTDceWpdbW1iXbLG5MZIATLK1ZIDIHoQJjtTp9-O56TSII-FQQmzVJscuH5b1P4kFH6Csa72hvQM1HT75HBBCLU849iesL9XL9DpZbEA9n7yFDPmteTPfKu4s6NntBgLNrmitKBN5kW_DQIb5K-G1vavYxyIAvcdL-biXCfcQJhCk7ddcvajHTFnR1Un4V5s6YzSejySwGb4EjMD0fgkeqbOcPiGXFinX30bqzdXBcYZQmc9TWyQ15Dfv_1M28VugqYudFBfYgfCToF9ey-uoN7VxzHspnZ7vVKYMy7-qGp4T4burvgW9yD_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65354c2ec7.mp4?token=dBXiJTw7kPI5bzTW1cOTnOKEcu9h3sTDceWpdbW1iXbLG5MZIATLK1ZIDIHoQJjtTp9-O56TSII-FQQmzVJscuH5b1P4kFH6Csa72hvQM1HT75HBBCLU849iesL9XL9DpZbEA9n7yFDPmteTPfKu4s6NntBgLNrmitKBN5kW_DQIb5K-G1vavYxyIAvcdL-biXCfcQJhCk7ddcvajHTFnR1Un4V5s6YzSejySwGb4EjMD0fgkeqbOcPiGXFinX30bqzdXBcYZQmc9TWyQ15Dfv_1M28VugqYudFBfYgfCToF9ey-uoN7VxzHspnZ7vVKYMy7-qGp4T4burvgW9yD_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة وصول قادة الحشد الشعبي المقدس العراقي إلى توديع النعش الطاهر للسيد الشهيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/naya_foriraq/80649" target="_blank">📅 09:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80648">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حشدنا المقدس</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/naya_foriraq/80648" target="_blank">📅 09:08 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
