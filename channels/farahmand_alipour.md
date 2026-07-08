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
<img src="https://cdn4.telesco.pe/file/N4ARMjTvPSJ_uKgvLx1nkySQF9pTAHRU59lMqOi_eED1HRegE_aw4_fwxR5FfRWVabv23mCmB5VBTKwiSxLIEKfyAYn-fX3D01xJLzOSbecP4ms9Ax3xJ6uQ9dxfYdSl4O2zD21NQ0sK02ed5QDd90pDfN7HpV9hKrzkWsr4zV8AUQKWreWHOSF6yUs3zMyNLcc3rRco8eDSdxFdjif3s2dkYmJGJ4iqDLOO7-agT5tCez0N3sy6x6v5TLnK-3d3XTya4gn_uRGBqO4aBgHRW9Dk8J0ajwo7ixO3Psa52ZphEiPkjIyX2yiRwreqTKFNZvbfAlsttOVgvY__GAX3Gg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 21:26:16</div>
<hr>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzzSsDYa8IXl7mXx7DOeEqP46ZcQdnBRUD64sU3JIY19s2RCYYLb_q3aDDtFOYzPCzNOncjWjzLGLfgb_Dqhqr989KFz42vbUMnRgQIeFX5NvkQp1L1eiQ3il-Gc4CiKOAprVvy_9OCHOLDWmGanGu4QRl_WYl9UdsRFepC6MSfeNnL-VtmrhDZE2IeX07dtUkvSA35ZHCwt-RbjEXs9oYxHaln930TAMkLQYmUJUc9SPfZOWe4We_oIGHg1EXT_yR4pn8exr_ZrpoukBvVRjI8rZ7rRQaIXvfuboDHX9MzWM0EygwAUgFF285h70DH_k1-CO2_lB9z3HkZpqh0XYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=Ki1alEeNcLwnOfBYCsOQxnFOSW-36GAObsluWfWob-aO9J9OQRJDHnsXNLD52g3OD4dXPUMdRFyapNPrHhpXswFdPruwvn3cR2Cl3-RX9zq5lUnXw6PXBkd2WjmWR0Rk77WGJN96trcxD4VhK7RnMLD3mJ9EnQFaSVr9XGR61Mx6XxLRnA43ZzWRrRR4N5K_2AU1ffSFMIqyDyXSiw7CK199XL6_Vi6PDSzr_ZCyjhm_LK_kbQTzgnborVhB6NEk6wabwt31vaBur3cqZ_gRGvgYZUxVH67J5VON-ZfCjhlf4ZLiB-HMH2tdubae9yJ-AwxXK_gTvplDSuYdc4HvhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=Ki1alEeNcLwnOfBYCsOQxnFOSW-36GAObsluWfWob-aO9J9OQRJDHnsXNLD52g3OD4dXPUMdRFyapNPrHhpXswFdPruwvn3cR2Cl3-RX9zq5lUnXw6PXBkd2WjmWR0Rk77WGJN96trcxD4VhK7RnMLD3mJ9EnQFaSVr9XGR61Mx6XxLRnA43ZzWRrRR4N5K_2AU1ffSFMIqyDyXSiw7CK199XL6_Vi6PDSzr_ZCyjhm_LK_kbQTzgnborVhB6NEk6wabwt31vaBur3cqZ_gRGvgYZUxVH67J5VON-ZfCjhlf4ZLiB-HMH2tdubae9yJ-AwxXK_gTvplDSuYdc4HvhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=PsPYqlvxWn3WNiH_ZG1O3erxgZxRHjSt91ypfNNq9AAYIU0OmOOIPcnWt3kbrQp4Z89aq5gXw1_nZVqhTW8TsTsjBRGn8ttzK2oXcB-BHksY4Af0JfW2LJAXH5SzH-qc1ceylOL60l4biafWTHu6SQmMIYjtbtUzOhthKcehJzXylkhcd7sIPPSPVTheYG61zqdZLe9tloc4gdW2bT6Pb4uOTj0_9QC912mMaq6kg0vItDXhu9Y-pmM7hChpm4PSoTI3zNqRX3VSryiYRxGcOC1aBVOH9kicLCDJnhHiGxmBlE3htlHIQENljTKNOyXSi_JMR_MkyUNMksqEiUoR4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=PsPYqlvxWn3WNiH_ZG1O3erxgZxRHjSt91ypfNNq9AAYIU0OmOOIPcnWt3kbrQp4Z89aq5gXw1_nZVqhTW8TsTsjBRGn8ttzK2oXcB-BHksY4Af0JfW2LJAXH5SzH-qc1ceylOL60l4biafWTHu6SQmMIYjtbtUzOhthKcehJzXylkhcd7sIPPSPVTheYG61zqdZLe9tloc4gdW2bT6Pb4uOTj0_9QC912mMaq6kg0vItDXhu9Y-pmM7hChpm4PSoTI3zNqRX3VSryiYRxGcOC1aBVOH9kicLCDJnhHiGxmBlE3htlHIQENljTKNOyXSi_JMR_MkyUNMksqEiUoR4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdUfZQkUbZn4PdoxFTVxLLC1_uh0pk_Svk5640gLN8azH07lx77hJEtleV78CRvp6Z_JKpk1-_8KmjB9UTsUSLYeoWcpCE5957aqSyJMQ_5BIqDmp-TH0m7ZDyf-FrXDdMCUqeIy2m3c-VmwCzD_GNxilrk1N9IF9d71qsK81cGd-WyPe0LehJS9HHy2h9vLs9Fjl8n88UE1EwFXrG3ONQkjmhXvPpZ9zoYiM7cynGUk5udht09N7zSMOMtnXavVqK5S6Dh_15r7eA7W9ZrkkdZ7eSfmgYwRD-IWBI4zZdX7GyzYebxleNPkr72Cx3_TmJCjbEjuip8uzyiy2xlHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=UM-4jBsmM2fSPhhatd6bMlVbQu4DH39d-uUUvsrbWXmPL1j8yncc3jOQDYeGue1N87B2hEiHhyL4oM3rWKpx-CgWwAlxzKywwK5Z_1be9mC3wCeU7nbbIN5vKVoc9DZkXrAtmCFWxMAjHe8AJQ_Fu6CyzcOEJgLpd0o_dwVYAhs_Z_Q7GT7fU3QAuReRn2V3pxRf1R8BLAvF183QLkyWPd1LrL-2qNHcAQpoH6o7HO2Wb9xp_qhkcb-h9TlM9bjj-Fvy7_Oh9VM2cTRZdJf51Y2Z1RoNHLdo2KX09BT1U77iW8SmwwoRqP7EMDSCSeXpgi_5lSN8ceiT2mEQXrtsmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=UM-4jBsmM2fSPhhatd6bMlVbQu4DH39d-uUUvsrbWXmPL1j8yncc3jOQDYeGue1N87B2hEiHhyL4oM3rWKpx-CgWwAlxzKywwK5Z_1be9mC3wCeU7nbbIN5vKVoc9DZkXrAtmCFWxMAjHe8AJQ_Fu6CyzcOEJgLpd0o_dwVYAhs_Z_Q7GT7fU3QAuReRn2V3pxRf1R8BLAvF183QLkyWPd1LrL-2qNHcAQpoH6o7HO2Wb9xp_qhkcb-h9TlM9bjj-Fvy7_Oh9VM2cTRZdJf51Y2Z1RoNHLdo2KX09BT1U77iW8SmwwoRqP7EMDSCSeXpgi_5lSN8ceiT2mEQXrtsmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=lWSldFXcULycTu3WFD_3dNN4pS0Q4lmhUd8itfcvOwsG22UJGIy-W6A-vue_bANKACOxUlkdjMS6YcY1Dq5H4aMoyj3KVsk787lFKQLuBTk5eYUPyX5TvQab0xBUXhppvxpAGVwylJz1t0ye_18BQ-zPJIJ07SRIh9f54NbKBBTKwXuJpxbjKFwIGmnCOsw5qjhDcd9VnfXLdkcnYjgRwZNCmb-rlYgG8_knlCBJyo0WD07ihodMjys1LD8veB8BGQdxAMnpNVzlXA2Z0rgRvuzqDTracBD6ESaYpIG8MssrCmZmjh8UU1EUDyao2kt-DbK2fGYJ4VHOEKgIgziKLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=lWSldFXcULycTu3WFD_3dNN4pS0Q4lmhUd8itfcvOwsG22UJGIy-W6A-vue_bANKACOxUlkdjMS6YcY1Dq5H4aMoyj3KVsk787lFKQLuBTk5eYUPyX5TvQab0xBUXhppvxpAGVwylJz1t0ye_18BQ-zPJIJ07SRIh9f54NbKBBTKwXuJpxbjKFwIGmnCOsw5qjhDcd9VnfXLdkcnYjgRwZNCmb-rlYgG8_knlCBJyo0WD07ihodMjys1LD8veB8BGQdxAMnpNVzlXA2Z0rgRvuzqDTracBD6ESaYpIG8MssrCmZmjh8UU1EUDyao2kt-DbK2fGYJ4VHOEKgIgziKLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=UOC4u3SGDeIPTJ-MzM5_IDOjqkVIdeQ3Oc7A6uIAkmrPuvtwZ0_QJGbYJa7HGGBjDTCR7DJyWt8ZdMBBYQ6D7gsm81q7aVMSHRQfWE0GTUQunRqIBulQrSp8NsBTLYSSpiHZFNJ5zpFrZsgqwW2C3rRyg5TDVT1EDb85KQGuBbeyf-_8cXNfGvyruxEomCRSt778bVBGrT26G4la6CKTNU7sG2d-1t7x5IjdYen9rLArwh4LOwT52tnn9R5J6XnQdXtiHlM9nIpSThFXieN2MbFVV7mLZqoxTBWGakFrFvWn-tND_oGZceWsn3qEs7c-IQe_ND61wslWqTBP7gEk8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=UOC4u3SGDeIPTJ-MzM5_IDOjqkVIdeQ3Oc7A6uIAkmrPuvtwZ0_QJGbYJa7HGGBjDTCR7DJyWt8ZdMBBYQ6D7gsm81q7aVMSHRQfWE0GTUQunRqIBulQrSp8NsBTLYSSpiHZFNJ5zpFrZsgqwW2C3rRyg5TDVT1EDb85KQGuBbeyf-_8cXNfGvyruxEomCRSt778bVBGrT26G4la6CKTNU7sG2d-1t7x5IjdYen9rLArwh4LOwT52tnn9R5J6XnQdXtiHlM9nIpSThFXieN2MbFVV7mLZqoxTBWGakFrFvWn-tND_oGZceWsn3qEs7c-IQe_ND61wslWqTBP7gEk8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=mC23x16Mi3PzHAfd-idEYYSpqEnP-DQmUm2mYwHdl-sTpVz3OxgAEpgJH9g1v2b1izJPEOLAF-wr__jXR4LiCiI4fBA7L2OpjHp2gqnl8sGtWWIlpYXZzbxe-g20lnC3ANT-wl0edA1At24kmT7GR3WFQCQ7w4ZZvnmYmoTWCveeZMIog9jtiKe-t4n_MG17cPuF769CWEwo8M4gz4Hq7kLuGoqa9-g1JaoBQoq8J49rj3vconIqPc-9fNj-QRPyYYqlB-7bV9fK5kpqJh-NbCmCLJtHLJnpGAsxTwa3uOU9bZ5o8V2-7W6mwFrnw8nxmoC4yVjEogI7MKo6qShQIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=mC23x16Mi3PzHAfd-idEYYSpqEnP-DQmUm2mYwHdl-sTpVz3OxgAEpgJH9g1v2b1izJPEOLAF-wr__jXR4LiCiI4fBA7L2OpjHp2gqnl8sGtWWIlpYXZzbxe-g20lnC3ANT-wl0edA1At24kmT7GR3WFQCQ7w4ZZvnmYmoTWCveeZMIog9jtiKe-t4n_MG17cPuF769CWEwo8M4gz4Hq7kLuGoqa9-g1JaoBQoq8J49rj3vconIqPc-9fNj-QRPyYYqlB-7bV9fK5kpqJh-NbCmCLJtHLJnpGAsxTwa3uOU9bZ5o8V2-7W6mwFrnw8nxmoC4yVjEogI7MKo6qShQIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=sIUCHYlduPx_HM4WvFX7f39c4BBRRln8kcipfwvCUJbe8HiGZ7vFsOs4ndas1ld7T1kgxs8lDmStQgFNYhsHwIN2aIxtxs4HEHq17V-gIMSWP6_oDxpLMhaV_qPGX9gxEEJjWTLWRE1CZFCIhRbnOS6dhbpmRXuGZp2N6dfExWgg4L9pjwoCQYkPabQlknjKTUtuB0nfgi3woWZgV6EUgH_JuJJrf208to4CSzyB2gU0Lvyoy_1scQUuuDd3ANlm709eF6xrwtImlEIb6D5ngSM9fQW3dQJ8TRso1LzSdYIoXQ8oUiORlzJo1P0Wn1rbD_3aEjTViE1VUcInC5Qc3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=sIUCHYlduPx_HM4WvFX7f39c4BBRRln8kcipfwvCUJbe8HiGZ7vFsOs4ndas1ld7T1kgxs8lDmStQgFNYhsHwIN2aIxtxs4HEHq17V-gIMSWP6_oDxpLMhaV_qPGX9gxEEJjWTLWRE1CZFCIhRbnOS6dhbpmRXuGZp2N6dfExWgg4L9pjwoCQYkPabQlknjKTUtuB0nfgi3woWZgV6EUgH_JuJJrf208to4CSzyB2gU0Lvyoy_1scQUuuDd3ANlm709eF6xrwtImlEIb6D5ngSM9fQW3dQJ8TRso1LzSdYIoXQ8oUiORlzJo1P0Wn1rbD_3aEjTViE1VUcInC5Qc3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هزاران نفر که اومده بودن توی خیابون‌ها رو کشتن!
صدها نفر رو اعدام کردن، هزاران نفر رو زندانی کردن. اومدن با وقاحت میگن ما اومدیم توی خیابون! طعنه هم میزنن!
شماها با وعده امنیت کامل رفتید
با پذیرایی و امکانات. حتی خیابون رو تخریب کردن برای تجمع‌تون، کولر گذاشتن براتون!
خود گدا گشنه صفت‌تون رو با جوانان شجاع ایرانی که جون شون رو گذاشتن دستشون
یکی می‌کنید؟؟ طعنه هم میزنید!
شما هنوز نه این یکی رو خاک کردید!!
نه اون یکی رو می‌دونید زنده است یا مرده!!
هست یا نیست! توی چند سوراخ قایم شده!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Am6u4Rrgu8xe47049HkbEe2GoLeGK-hOZx1km_XKP_cO5A_miICtDx6qpu8fTBH8KRnTnQu8UfsRbhd25HZTKsKBFMIA-CblIRkYcYhypdXrIDISH-w1l5s9QY563aUY4DThQUI2O1Dchy6cAVnvWz7rHw5CLFc34suckFckq1NkwD7U1y_E143cZCr5H-b-7TJxQksbK78-PiXS2vykxRns5SzXys-oSm9lPZFjXd_nH6oLKvyvcR89r3SjU04-M4-nqwYVCwwt-JOgqMHlJ5EPQ74vwNSdr-fYCXW6ztPtm1FQoYt3Vz-7cAhbq9GQnC7ZrdMeSGdcF6SyIY-eSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : «آتش بس با جمهوری اسلامی پایان یافت. مقام‌های جمهوری اسلامی شرور، بیمار و فریبکار هستند.
آنها مشتی آشغال هستند.
به آنها یک هفته فرصت دادیم برای مراسم خاکسپاری، ولی در عوض دیروز به ۳ کشتی  حمله کردند.
آمریکا زیاد از حد وقت خود را با اینها تلف کرده است. اینها شبیه به یک غده سرطانی هستند. غده سرطانی را باید سریعا جراحی کرد و دور انداخت. »</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7ovzrxVJ-I8dU0bHTsxaUMHAD9037YNq27Or5C6n6uHtLKXZA4tOfZOFO6RVEJYiKlh26CFYqkUf386ktr3AkL8mFXwCAwk31gZJHYl1hIUchBwk_mp6pbLnFfsQGHLXQxkVyIxQNGoRNJQTAQaeMVAp4_XLd2_KjsYWAAV635Fy3Xwsvq85AsoKMib1VxzOJ7QxQSvO-krfSpZbi9Av6321v_a6qyuq9UpEjQ0JpKXWxHzjjsdu2FSc_2sei0gVqQp5iUm3d-hEmmA5RoB8r0Wu9uiNMog_8NrotCtEyqGT4yjx164VMZtPhp--x5P0CMSZi9FnISzm37ofUkLEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-T3JbhS1OaSDLTuHP8ma-AYCeP5Fc9-eyx5cUpw9lrSV_DI_6R0u9h3QUKZKrnXmrbg3R0kHxW0c4rkfk7Vcr2E9TbO3ji1JyFOxJKnZEf3ag-MFJHYnNN8-Jb8mBWi2R6aCLI-E-EaFtE-Iv7JJrZb8t8zr3TnO10SoSD9IaDJz2KDOS33ZnZuShj45EbVFX9sXFiE_mEwOepM4km7XYt0xMBk5Im4FBJMxe86fKcVS8XsnOqYhtCCY68Ve6MtdfR9sQmX1W9jxMTAoOniybraXSauOMZFN5pw5SzhmQ_hpc9FvIdRBTya4uo8BSfTrJ61UX5UPAaxekq9dtZBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Rn_8WCUJbJutyPrrsbMZMeVklr871nCBWKrfT0m9f_uqL8UzQqnbVchV9RocoskvFLnM1rzw4iiNr0iISQPQR9vyPozccctXPIFjwtTBjK63QOoM0xPtuCCyWD7wMVHUZJen9tEGNBIqI5P4WKregQ06eb_O08JDarZZvevzknG8qaIZacMCgnxUytnh63z2c1e43687SiVbEblFIgNPsECUmc0QIPVUjmzLrPyV3VklTcdOIoyzEdiyPpzP_H-WCr_ob5AgrmEJxeZLp4Nxu6hP3pQWEyUH1XnuOMe_pJ6KaMwmc7a7UF-0SKvjokXa1aR1-T6SzIg0VfeBmUEEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Rn_8WCUJbJutyPrrsbMZMeVklr871nCBWKrfT0m9f_uqL8UzQqnbVchV9RocoskvFLnM1rzw4iiNr0iISQPQR9vyPozccctXPIFjwtTBjK63QOoM0xPtuCCyWD7wMVHUZJen9tEGNBIqI5P4WKregQ06eb_O08JDarZZvevzknG8qaIZacMCgnxUytnh63z2c1e43687SiVbEblFIgNPsECUmc0QIPVUjmzLrPyV3VklTcdOIoyzEdiyPpzP_H-WCr_ob5AgrmEJxeZLp4Nxu6hP3pQWEyUH1XnuOMe_pJ6KaMwmc7a7UF-0SKvjokXa1aR1-T6SzIg0VfeBmUEEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZc_Vwhxfkh47zUVQhoGuIfSV38s0LjAnnkjB4zJqeEnRphn1r0OWGdkYplpgpObbgZ-IafyVuC90iMrDb_Jl810J9ku1FSRBxwWcDMmr7eB2eWp-nyKSUtLywniQmMKtYiVN7Zh7B5tCeEyqDFI00F52R4MY3Sro3IgipTEaZ9JvQOhLcAx6XhF0ilOnvgoQZfqY6dhDtr8PN1Zgteh-mi9SV6fM0UlWtUZg8qDv7oRdWLNsQ_9W3heaUiJSV5Dl3dR0j65Uy3RN9Dk6wcqYKh9zXovpGwjKH0ZPKmHIZQZaf4I6dejBLxKRs-bAc5i-pHjTwNpLj8gn0GXj41EWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=N_hR0SVgDvzVOHuZZJYR1-MNbpJ0WcuTYZQD1K4Ac_01qBdFOyIq106ay7-OBmMSiIvtS-feSsEhJbAG0Z_gQgY879-cVo79gUlmwIOCJVjOiKtZ1wdjFsbO0pqISUH1fFMxbLVmIvXQ7Q8R0VxRDA7SW-X4_cTgEYLySXgiT7LnLILPwC3eajYtotjuUxoJbl17whLxPhH_Sb0piolD10TsBwLmh5zW53ZJu9DiM5UbWeDntJNRlMRj5nNzClHf7tCeTFWAb72RYY2F-83XPvkBcdWn7iwm63HZUrsJDQlITaMB1928M-gaarBqCfwzYGmWHeTLxN2kqG-2syXnKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=N_hR0SVgDvzVOHuZZJYR1-MNbpJ0WcuTYZQD1K4Ac_01qBdFOyIq106ay7-OBmMSiIvtS-feSsEhJbAG0Z_gQgY879-cVo79gUlmwIOCJVjOiKtZ1wdjFsbO0pqISUH1fFMxbLVmIvXQ7Q8R0VxRDA7SW-X4_cTgEYLySXgiT7LnLILPwC3eajYtotjuUxoJbl17whLxPhH_Sb0piolD10TsBwLmh5zW53ZJu9DiM5UbWeDntJNRlMRj5nNzClHf7tCeTFWAb72RYY2F-83XPvkBcdWn7iwm63HZUrsJDQlITaMB1928M-gaarBqCfwzYGmWHeTLxN2kqG-2syXnKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmWB6oAHvUHb3DumrfxKqIuuP43XFJxs01Y4IZOYV6JvrmJWM41kjZ0YQGKlbBv3cH8SApgt6TZclcp7_JQHiiV951nhpF8jwTf3K6YR93PAzfMTzixMXZyy0j1S8ZWHWYwSpo8TNbvveLWlwP-NZOMaRNcuEGfZ_47umSS-4-jqg1g_4bU_cXRoVjNuMdSUFLmLlB-loIu3vhPTChASlYMiPreyqgpcQhapMoKdUywm9JJ1i6U6xSIY2goT0duIZ93z-9VGRCz258U0HpjQYJa-_GIA2DtD7NUfDP9ekt6W0srss4qMotWvbCQL7HXk5aVsqOmIvi6LoezyeFPI3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/autMnhtCwAKGxiCmwSet0GrrfZSKusfJyauLCVx9xaRHDDCa4ublfX3OHgU_nqFuJ1ANQncOpU0vY9MJguH71M62ZPkb2rMPNm_EXKqHKAyysnxgs1n-gg0C8vXkksu14BChOVd95yos_I_WAGh8YrZ3OXX3l2HgQ7UcTH1QZPyK8CVaeAKAMQSPoKtP9edt1slngtNvfP6ELWheFPOHorvUyxPHzvGKmRH6qDzGUEPIBDN2IS3ZSgdDdWUNlp_Z2OcgPSJDCmZerYo1ULgl0iBdTPEO-MHio3JG9630QzuHM_tsCA2ctAZJvmUi4YVRjYFXV8duBDVW7HNxES0-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=vbFzRgWDq6Akm9F3UEd1wpH73zQuTb5NsfPhMUZjgGFPVjBnDPAcnOOuwHIT3YCIud0abjXr3qqqrykZ8JL4QvSqZjeUh7AJ8ObmQ2da30Mg2EpK9LikrRp_Omrnl_EYRr-UdyslqTczN-yOMAeHqFd2Ombv4dcD4V-zv0tJHFE2CzPZvVYmrFwNU7Jhs87SPEsbUEVXk6qP0cBiOnjrR4FIKeJEj1_yLjOrh6J-DM1vG53zZg5-DoZmSWdfHMK5IS6mn1UU0_hsv-R28l8H774L9kz4UsStH3q2bRF2b6m3uqzsk_QDLXltJmsD1ercKdUOWfg7U44gWnESR-aBRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=vbFzRgWDq6Akm9F3UEd1wpH73zQuTb5NsfPhMUZjgGFPVjBnDPAcnOOuwHIT3YCIud0abjXr3qqqrykZ8JL4QvSqZjeUh7AJ8ObmQ2da30Mg2EpK9LikrRp_Omrnl_EYRr-UdyslqTczN-yOMAeHqFd2Ombv4dcD4V-zv0tJHFE2CzPZvVYmrFwNU7Jhs87SPEsbUEVXk6qP0cBiOnjrR4FIKeJEj1_yLjOrh6J-DM1vG53zZg5-DoZmSWdfHMK5IS6mn1UU0_hsv-R28l8H774L9kz4UsStH3q2bRF2b6m3uqzsk_QDLXltJmsD1ercKdUOWfg7U44gWnESR-aBRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWE6MPwRyNNG-mIFQ-WWzM_w5XtxayrkLwsLQjFxtEY0HfukAqnnhtEUkcErAsnkggXNiXppPMRzQbgl9hL3_AUtcJddVEVTETSKcJUpRTmFh0BNekWku4DcJHMMmAWt-5O1zuaNios4eKW0dVZXrroKI6lv9Ej1KQY83Ya3QB6DNlCAhDy56kkBRfUXKX6Y5ZAvSIvg3E4OK9EeE9FOg6zsaEJWNJQBXag-qDVFAkrYi7D3uGbNBT_HnfrQSnApo64ENEvvX3JZirMhBGP0r4RkTtygNt6iamYmDJqQfLtwaSGBSwggprXIZg3qRP4wSCOFZkou430L6Tt9H7jAVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ecls2FkJe824k4f5YU2SFE-EbXIvMU53n_s-k5cdcLemHW3AxNZdM8bZ_uiJCPrlkNiwMGkE_CcReYWJNa456amh1sICmJGBLQC9co3vAOtR2m7fhB5EUwodPdGUUzuwcK7I5JIhm3b81sLel8i1F2wqrOeH8P7Ln5IcbVgIvla4jzesKJtPbdXRwZFjrz8f-IE5FkOurn_Ai1HzwDTSC8MhDq2DuCpwumuoVSEfmiFjBEA1VP6nRWy_hH4A4O6n9gTTF5s2V3rCseU5Cpq3NeCU0UPS8tmrGxAjjm-WmpImZ8vKYWXtl3OeZ-bo2J_WeulXne3x8ck2m_pGDtgxlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8IAgDkOR9f7oSnyFSh23CraUgpd8GTJoFpYsoFKTdoYwyeoYR67NSso-wKjzkazpdZzZiiMk_eQ03DMdvTuBJ4L8Bic-WLd0dyUquWvypg8gvWYEkx8x-dz8p_Mz0TJzpK2otnaTkI4_GgTlLXQkKFQCNf-5nzmhW4zHvaitCSjbatfCgzXbM3XCK-ay34HwNMwbjgrXAJctr9EmuKl2R1rMb5lD-ej0MA6bhRedyCXfEOXMSmv4NnTuTFWGDXRTn8hd8YB_bRP2OqwiL33t5sRJzMz6ZcTFUF63BbcswQYQRck2gdxB374C2OW7ZJkOAFUEEdCHVnOAZDLW29PsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fPztkKsozJ3ofMR3Y50-1ugpTcOUw9bYtrewppArDJg_Gsf1_bBxlSNbsB8je196GBrXN9sp-QNaXjsOoPKZodymlHWTkJtfPPXiJlM85IbiTnifmMSdLv4daXUSlvyDXlqOee0lIVuOJUoMfaLKf8vVPX6x4GaH3uuX-0p3lUx2iXRVnmhtZIprQ9zNkTK6ycXZDwwRNjl7Fiywosqz4lMj7Qxy2EtDA9SeX6XL1oL0Yr5rEUFO5W5Yl9dtfQlOZpJ3jY-c11NE85gWBtV-6HKsQxMrK49K-Jh0CTTy6l8CQdlSlTU-gCTqmRMw3D7NdxtXWWKtGA0nksMq6ncJ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B92eEg0YdTHPtpONOdMJl3k8nJV9hUij1COf_USlbdLIu7MDFSkR4MdQ6XIX9j0miKNDXnjZAkqvsQxicR_g5Mz_bm1MtlziYc8wIod77yTGIdtSw1fA9vvPR7XQZA0sPM_bosd_qOZIOnNZx7Lv1Wy7W7D2UEYVYTaEZvvxTkdGuSGxrSh6CaDuuXKlGFmT-ZOgLWCX1Yn7jDm5baj_dWrjhq8iz_q2ksVIWN5_7scHV9_K2MfuRpFJYknMCMTUXyofQQa4KzeqEiFxrteVxk9xI1WS0tb-aX_oahn3XrP03hYSY7wTRt3ourpFeAcGXEKEC_a-ADPlMuS4FGgrow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_l0VikWBfxV5Y_TTUnUHi9NSU0PhlIhUygHNmM4Ev2IZIyVg33tkPukuUX3kGSImwi6Fr2fb9SxvUrENktHnQCFF-hriBOb-ghzTQCjtUxrB8uu-jo78hUo84ekjxqE0TtzS8Nq3BTAfmg2U7yl8sNgHQhv1hbdTrKJFI2TangdpoDMizwYnf6UEdtXofIZl2ZMgcRV67ePtj4d5rHaMMdcKVgFwH_V4YNvR_CTKlhcPzCoDZQWSC9YFOPy95lbwrmvuFVLvSE90s1mWNa_2LppZceSxIBa-SZ_fK3SjQj0yoegH-NT9_O_B4yn77YyLmX-lLCY6zOJHNI61uauBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم پاپ فرانچسکو
رهبر مسیحیان، روسای ۶۴ کشور
شرکت کردند.
برای ولی امر مسلمین جهان
رهبران ۴ کشورِ اونهم داغون!
خامنه‌ای سخنرانی کرده بود و میگفت
سرود «سلام فرمانده» در سراسر دنیا میخونن
و گفته بود :« اینها عواملی است که می‌تواند
به قدرت کشور کمک کند»
که منظورش نفوذ جمهوری اسلامی بود…..
دیدیم نفوذ و جایگاه رو!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=BZBX-RJ7KU_Gh_AuStsdDQuQn8UiW2Ito87RovkmA5-c42sGxDaJAkY5hVgkupN3BT8BEeSAK0K-kiXBwzyOTMPyENVQNvPRuxU9uZ-INev3nHXRulQfOWWHQi4fgTDwi3bT0SLdwnKsLvgiKVXKVBPKSoceU4h3zkOU9mpqIphCLbm4FwT1FWTH6MYxXIa0i6z4eWEN2MZkTHzGgV8zAgcUqXeK5s2z1vUNth8E7Kt0Mi7yCjIsIF5mTecnBoKoO19QlFCihmkqhGorN7epVuhwnLs0Nbqo4hoqlV-hgdiWMlSg_G_8B3lMS4yzfOHPRrndXUy_ZdaPFmaTvznNrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=BZBX-RJ7KU_Gh_AuStsdDQuQn8UiW2Ito87RovkmA5-c42sGxDaJAkY5hVgkupN3BT8BEeSAK0K-kiXBwzyOTMPyENVQNvPRuxU9uZ-INev3nHXRulQfOWWHQi4fgTDwi3bT0SLdwnKsLvgiKVXKVBPKSoceU4h3zkOU9mpqIphCLbm4FwT1FWTH6MYxXIa0i6z4eWEN2MZkTHzGgV8zAgcUqXeK5s2z1vUNth8E7Kt0Mi7yCjIsIF5mTecnBoKoO19QlFCihmkqhGorN7epVuhwnLs0Nbqo4hoqlV-hgdiWMlSg_G_8B3lMS4yzfOHPRrndXUy_ZdaPFmaTvznNrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJdFuzdLnwDmUlRpciVUaVbdKNOSrJ3NcglRj4YB1aqcmkNx7IapDB_3QH02cf1sf0FD2pfWYQVKVqcig_wf-RwUuo5rqiLpFE1wLXrcd3MBHAlSvjLR_dy5YkEhDY3TxLx3LhelLzE1EqwfwtzMQGqzeGZNGjfWRwQiEaKZOEivec5GHy29SMVYByaTpoP497WHuPF1xEJnYaXFaQMeilEcPYb0rhlScsgVZPVLBcVgpze8IK8mQ69MoBYdXYlVKKndHD7B2DL0zeu88Arb1KH84kWF36oPI_NMApTKIVCWPENaaEJ3sePE-k_82u1RNAzDjN5L1kvFONarhlGMtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=PRP0F79aPiWyVbo9Anauljnft2rqp4qXR0WoM2XbW_mZFKpW_BRQZit10RJHViSqLVpZnuRoHAxtkd7-bXTVGzGhm1CS4MMAkPmnfjGyTWl4NC85IwNQDH25od6LgQvJycfpGuI2gH-JEt1z8FTyXqILL3q6_iQzCt9onQNyBB_JsHrJ96VLUftsmkCE7EApPOb799UtiSmbwyYIpreX8N1qzHjecQjgMuR2N_xstfQHX9u2GkB8hIOKxnwVMalpIIdAavs2cRSy8wf52Gpj7hoX_jjbjlH1v8YikckvFAvhgqwwEEprsMUANQY-eh-ZS28jqGRmJRDAJ6b5SZM1bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=PRP0F79aPiWyVbo9Anauljnft2rqp4qXR0WoM2XbW_mZFKpW_BRQZit10RJHViSqLVpZnuRoHAxtkd7-bXTVGzGhm1CS4MMAkPmnfjGyTWl4NC85IwNQDH25od6LgQvJycfpGuI2gH-JEt1z8FTyXqILL3q6_iQzCt9onQNyBB_JsHrJ96VLUftsmkCE7EApPOb799UtiSmbwyYIpreX8N1qzHjecQjgMuR2N_xstfQHX9u2GkB8hIOKxnwVMalpIIdAavs2cRSy8wf52Gpj7hoX_jjbjlH1v8YikckvFAvhgqwwEEprsMUANQY-eh-ZS28jqGRmJRDAJ6b5SZM1bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=BpSfBCth5HmmjWtIjkJZ5WfRwghRqwtu-vFWN9CFwCnqoz14vci4XVu6gMExfhLqFwhOz1es0c-ywitkkgygzAh4VQG88sS2A3slpyUuJjdn_5BoIq75KbNHzilHMyG3_iwAO62aa8vclE1oVNc3-s_Iy1co-Cjh9R5o2fpCalWqULcAhIdw7dZD5Z6lNS5_ppnZulk4cfCaGkFNCFhIcgo4IrMi2mGrJuGfr1PBLxlmxI526Ub9HNeJVKhDRl1pQ9eQ3u3cc7oZ8enBcwo42uJ82J0CfP9DVX8vGdxPwgk5Il_B_e4dv5XM3mavMs0a_Y3HKPmYuP0Fxqi_lF2i2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=BpSfBCth5HmmjWtIjkJZ5WfRwghRqwtu-vFWN9CFwCnqoz14vci4XVu6gMExfhLqFwhOz1es0c-ywitkkgygzAh4VQG88sS2A3slpyUuJjdn_5BoIq75KbNHzilHMyG3_iwAO62aa8vclE1oVNc3-s_Iy1co-Cjh9R5o2fpCalWqULcAhIdw7dZD5Z6lNS5_ppnZulk4cfCaGkFNCFhIcgo4IrMi2mGrJuGfr1PBLxlmxI526Ub9HNeJVKhDRl1pQ9eQ3u3cc7oZ8enBcwo42uJ82J0CfP9DVX8vGdxPwgk5Il_B_e4dv5XM3mavMs0a_Y3HKPmYuP0Fxqi_lF2i2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNNDvQtrrJFLt-OgeMrviEJD9C37DZwtP_1LVz1FbFcTMwK6bt2Qfc6EkRf3flIvh_KeAb7IOKMcbYH6_lR_faxgcwoyb_WMwN5EDPwt3kRFXz1ihDa8x2K0kGoAxiwjKAYhsm3eEODqM3c_TQMBFhejugaHwcmVEQsSmTeVTKWGXzN5uJxI7aJDxPw25pRPCBEFWhZ0NAsJQIC_sGM2FQ8__vvK0lXJnAgBQAzsNhvK_702OT7mqMIfexN1ImmGgGYMfB_m996_9Qjfm3oOUmvRquOgnVml7MdkjPUL4iQ8bcwrBrqO9sK1Zr7-wzMfuhn7bc2Tf-8UQ5ruI2VRtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=r3yS1aAkEJbH-Du0UctOn9fDWC91MyqM5Qp_8sOX8qaKp6O7mKVBYWmfHTmDFKRcuEGTNne07edE1m8dcNWsvUWDwG-CFiHZpdhuAuapVlIB_LOLtYQTLc53uda-rCjzE0-0qHC9Bp-lWcjem1aJiugCZgK5iPSDXuL1d015gT13W1jV109eXBAWkz0-rinjZK2-CSbwSa6AxWahNEc60JlL1eC1A6zKEAg-dHXqUfwfD0ilAOWw6zx53s8NCNQwEKHDcOA7x_g26lzl2XFEB2bNM1UCVASgwM7vVBN6lhF_Q2_4rt9r45w8ArPjnseg8EMGlUVnselV61xX0y1czA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=r3yS1aAkEJbH-Du0UctOn9fDWC91MyqM5Qp_8sOX8qaKp6O7mKVBYWmfHTmDFKRcuEGTNne07edE1m8dcNWsvUWDwG-CFiHZpdhuAuapVlIB_LOLtYQTLc53uda-rCjzE0-0qHC9Bp-lWcjem1aJiugCZgK5iPSDXuL1d015gT13W1jV109eXBAWkz0-rinjZK2-CSbwSa6AxWahNEc60JlL1eC1A6zKEAg-dHXqUfwfD0ilAOWw6zx53s8NCNQwEKHDcOA7x_g26lzl2XFEB2bNM1UCVASgwM7vVBN6lhF_Q2_4rt9r45w8ArPjnseg8EMGlUVnselV61xX0y1czA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A15EZ_FKX_D2tdFotnSwTBB6Sx6DQKdLU8-qyPwlBj5Tt1ZEEVH9YDEFnfKQSLjeJoqeqR4Cbkxlirf-JcjTpA1tRLywsdeVZZPM0UXXOEznMAPnJX2g763ibhIvL4vdEsxT4QzjumKf3mjaBxGlJ3LdBY39GQHX0SfwIBVNNG-Q6HwkL1NQb_1FCfGht8pTdG9wqMGnZ9NnIho9Oqib0kSrxpoJnwuc0a_crrq-hdUTDeGXQVTroPCie1JmhyeG-oUEIPXemVg5UOLrG_HlbyqGERta2jdn9gsa3QXsIaV2_TQ7MusrX--lt1k4QffPQR964Qt8nrMMfZCPwupPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اما چون نوشتم «قطر رو بزنید» و…..
ج‌ا، حتی اگر قطر رو به سختی بزنه،
بازهم قطر همین مسیر رو ادامه خواهد داد،
چون قطر به خاطر جمهوری اسلامی
این کارها رو نمیکنه! برای خودشه!
میخواد میانجی بین آمریکا باشه و گروه‌های اسلامگرای افراطی مثل طالبان، حماس، جمهوری اسلامی و….. برای همین دفتر اصلی گروه تروریستی طالبان و مقر اقامت گروه تروریستی حماس،
در قطر قرار داره.
نکته بعد هم اینه که ۸۵ درصد درآمد این کشور بسیار ثروتمند از میدان مشترک گازی با ایرانه! و تا زمانی که ایران منزوی باشه و زیر کنترل جمهوری اسلامی،
قطر همیشه ثروتمند باقی خواهد ماند
و اطمینان خواهد داشت که در استخراج گاز از میدان مشترک، رقیبی نخواهد داشت.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_WBsCZ2cmISC3UKuNk8-N7YUzszHnydzJb3Fqcodf9_bcammQXRQW5VhtNYmK-TzwtZ7M38jksy7kf9ZmI1qPw3HceSawxO8Pcchl8nyv5jHjsiig1LgXxEHZbHsjnFjW74VcrtweHBADT22pcXIWGt4qJhLqBzweGA-spAYDR6qKmisxTHa3Ldcnr71BRRK2Jhh-KXIL7sByaAsKskyfHgMrwJTphYCqV070Fy1ohR8NIH7ZIA7TpjVzouGfkl8rQo19xEek3UqHFLUJphQnCUZ-9V5_As5vhj2YdzApeZEvN2yLf5ezUdLad95eONYDEBnhBWHEaEdekYd2Z7QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acYd0eq0rMCo5vhWYPL44aolWJ5AVgGrVbLtRVLrHJ03N2NfzD6H2461GlbC4X4pvHk9LhB3wrgrqRf-oRxqzNamRX4knybaiNzZWATx2P69DNiOBkxnKn2NVXYOZejZJhwkzo-7d1WdvztzlRpFjQMFXgVnCDPNV-xYENB7X6OOV_2o827yKUqUe4FbSz7QjEYyLKL4o-_xkyDiVb5cVDLtTMx8dR4G2X5dh4Yd0af87sgB23lFAeU7PBNh8_Bi1E9FOJAKaOviJkrKMP12rl_C9HWo8OxSoUzo04nYs5WfhEf26q6HNe80akk-QPFWJRRR5uTcskah6BnJk3FXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVPrvkDC4j7Wif_vjOCEDhuX2fksgh22Hbwl1BQ2QVWiuccvs23mdWX1gLGS9l4yWqUDPqvcVyvRgO4Ondume9WmoJNs2YQWyT9JcMHJgJnWceOmPVgTA2JiPZcjpYVi6IpqocNsZHdb6LsEreWDz6n9A0chS4gJ80EQ8mmM5rxhN8CEFqlo5YRg6InS9EkuCiyKu6CtRgQL-NP-EnWBuJYHWVsHXUTVW8g78PcVYLoO5W6qpC1eDZ6SLm4MfzlSBfA2dCNDSnsCEY_xC-piS3C0tx0R5o25Kq7fAn7QG8a_txZ6xryIlRTRj4Uj0Q_DdOzqXeug_IFCZ_GUrBRbMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyOMtJ19t5VsUI6rnlArFwZ-3G3FppWI3i8Y2chSqwjJ1TrwP7A__03UEcBqwXlokrKTmE6OgLLCViC35NsLiYjzedSTqDoGXWY27BqcklkeHw6BUOtHm3FpALaJlerTLQ7sp7y1hp-1GcPyE13NEVhsBGYwlnoI56MyspVg0RqSoKvYPdyFsr2gYfGB7qzVRkIds9LFuSCPabAy9yico-6C7E9bmhm04u3aKcl92FZJwpzHkgsYfMxsovDRpSUAEvqwmgGsveiIrWgTbuNxFTOvSa2AY5jebV6B8t1Zk0s6VURB_InwiM3iWKqqXqkhz6oM15_sxpfxv4_QjKYp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7QytdSRuVivXZsZGnJhZfWBaKYQIFQ5Qpy-q3mxKpmcTmyD1CirNP-q4HBtxTcztCOCRsjG7QT6zWO3_j5cs09TWNoV54E6Pz1E4Wixmbogx5K9x7FMFM5dnKet4FwzYRNXHjamgLfPLboHOiFa0DkEbyep1eBohYnkfti83xMKpkB5NCtigDx0Zh6EKsqWhVF0Y2wLHg-uS6XJSvRsSyrwBIGL16GWvgLInPisJDw-kNQ749Yn6FmC9Jnzd87jjTeiP6PMOo2NPQKBqtRdNTYuN-UIt3kjb5DxjR-_xYCf3uh50LSfn87IuoAYBXDcCAWKWF8OFgv5C6lVsW2fqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم
خدمت شما داشته باشم. به عنوان کسی که
با جمعیت زیادی از مردم هر روز در ارتباطه
و یکی از کارهای مهم خودم سرچ کردنه.
گوگل به نظر خیلی خیلی ساده میاد،
و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،
و اون چیزی که میخوام بگم :
دقیقا هوش مصنوعی هم همینه.
خیلی‌ها فکر میکنن اگه توی کادر چیزی بنویسن و سوالی بپرسن و جوابی بگیرن، به «جواب درست» رسیدن. در حالی که پاسخ هوش مصنوعی،
می‌تونه به دو کاربر
دو ‌نتیجه متفاوت بده!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=Ol03-fb5i3gpg18FWO4Jn-jZ7YidD2EWbVnB2IkLbvCHdSNtNAY7_6EU18MixZw6jzOByobarkubNVu0zD9CJWA9fTXMpSSKIq1RN9tZ3GPH-7iL9s3trlf_J0zkyUIC6rHtN33zbZWfxRd35-091i_b0CUSz8uX4lKccntH_y-fPXXrQQVUuSs_mokMuegd4Xeb3z8CIHW6ge5M8gNn9QlZQwJZs5UeRTq1I2HGFWDu3d-u7FZNQIQa9NRiPue-rZPrHrKTS2VPkahUSqhBb1xRaJjA-9lmCxL5PaxeV2RbHTYIxQMK-_sTqtp8h_sYkxeYrtdO_zs_efA_NhA7Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=Ol03-fb5i3gpg18FWO4Jn-jZ7YidD2EWbVnB2IkLbvCHdSNtNAY7_6EU18MixZw6jzOByobarkubNVu0zD9CJWA9fTXMpSSKIq1RN9tZ3GPH-7iL9s3trlf_J0zkyUIC6rHtN33zbZWfxRd35-091i_b0CUSz8uX4lKccntH_y-fPXXrQQVUuSs_mokMuegd4Xeb3z8CIHW6ge5M8gNn9QlZQwJZs5UeRTq1I2HGFWDu3d-u7FZNQIQa9NRiPue-rZPrHrKTS2VPkahUSqhBb1xRaJjA-9lmCxL5PaxeV2RbHTYIxQMK-_sTqtp8h_sYkxeYrtdO_zs_efA_NhA7Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=k7vDDtlC3uhTPvzcCBiaAytsZ3DOAQxw0CokL8XqPRvLiISZrKGzRuLWJfxe6UMkn5ABIWvDb0xaAPpHL2tC1ChnS2_q3y4ydVb3csht4Qf45oilKXHu9fcmjl7QsPurFr_kOd4qvjI2nqfNVA2c9yZYjn9uLXDv3EisY-rAQGsrte6eacNxqejeXG_19d78Ogmv1PBJlCdmkLRMMfsKXC8y2DCpdHiAchbp2yG0fefgCC1MJjsgWA8niGT_ObiKpVUWpuKEqCkFliZSQqJ9PmBxgjRmnzKY-4RknbuoC28MV_7uH7QH3TUjMFdKmQLqndfRvpMLvkxbPQFup-6l8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=k7vDDtlC3uhTPvzcCBiaAytsZ3DOAQxw0CokL8XqPRvLiISZrKGzRuLWJfxe6UMkn5ABIWvDb0xaAPpHL2tC1ChnS2_q3y4ydVb3csht4Qf45oilKXHu9fcmjl7QsPurFr_kOd4qvjI2nqfNVA2c9yZYjn9uLXDv3EisY-rAQGsrte6eacNxqejeXG_19d78Ogmv1PBJlCdmkLRMMfsKXC8y2DCpdHiAchbp2yG0fefgCC1MJjsgWA8niGT_ObiKpVUWpuKEqCkFliZSQqJ9PmBxgjRmnzKY-4RknbuoC28MV_7uH7QH3TUjMFdKmQLqndfRvpMLvkxbPQFup-6l8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=MLcYxvP68noKbu-dm8xNZGG-_C90BJDrGXlueikq-YClvNeXAJy2Q0g76MZu0cTUqH6gaYTkqKH31iI0kOKMR-S1Y_-vij9IfbRIk9eVU_XwEMbdSTIYD6CHtETxVnzOfPITtjTTR9wy1Gx-0T40SugfNqJNZmtn1u-Z2zQe2nK6044rfig67rprtj4FpJUAGcGfFwI2yadIpqPDcWkPXoSUfmQaCkJrW-gtlYa40JM5JNNmguw-vHC0UUSW1rssWDgYoJ5Jj7-THmVnY9adAuoR4BppMmiETSnmOWHTcGYdgthHHE6SOvpS-IDZwaICujbU0WYwfm-u4PU_gleaUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=MLcYxvP68noKbu-dm8xNZGG-_C90BJDrGXlueikq-YClvNeXAJy2Q0g76MZu0cTUqH6gaYTkqKH31iI0kOKMR-S1Y_-vij9IfbRIk9eVU_XwEMbdSTIYD6CHtETxVnzOfPITtjTTR9wy1Gx-0T40SugfNqJNZmtn1u-Z2zQe2nK6044rfig67rprtj4FpJUAGcGfFwI2yadIpqPDcWkPXoSUfmQaCkJrW-gtlYa40JM5JNNmguw-vHC0UUSW1rssWDgYoJ5Jj7-THmVnY9adAuoR4BppMmiETSnmOWHTcGYdgthHHE6SOvpS-IDZwaICujbU0WYwfm-u4PU_gleaUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=YQBsaLzmOTv0faaV_CMDQNbio32zxbjGNQMCUWDq3ZkEVXwsoPcpuO2mQ-_dSYSoqyEhmOehidEQOijt_EQlR6uf1Dvl_3YhNNW_mVMT6ydcmdp8-no-w05iBgUm72cRQPmTqJ8z-Vchcox-86ZTg1O1FuJ_J17gLpN9Qon5jb9o3iuU_gRzNyzg9tJVN1WDqlto20PCmTEhlcRE5s6YnNtnvsWjTCuyPEQQEIYXoilehfYbIrQUNHlkGVbIH6KQZFqqZk0hk-8DhqL_0Z-yDy_Rx0qAhG3qkWu2KbgGq29fUNgW71we--VrVCnsg6EWc5EQTjjoNbjY04G9v_3SLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=YQBsaLzmOTv0faaV_CMDQNbio32zxbjGNQMCUWDq3ZkEVXwsoPcpuO2mQ-_dSYSoqyEhmOehidEQOijt_EQlR6uf1Dvl_3YhNNW_mVMT6ydcmdp8-no-w05iBgUm72cRQPmTqJ8z-Vchcox-86ZTg1O1FuJ_J17gLpN9Qon5jb9o3iuU_gRzNyzg9tJVN1WDqlto20PCmTEhlcRE5s6YnNtnvsWjTCuyPEQQEIYXoilehfYbIrQUNHlkGVbIH6KQZFqqZk0hk-8DhqL_0Z-yDy_Rx0qAhG3qkWu2KbgGq29fUNgW71we--VrVCnsg6EWc5EQTjjoNbjY04G9v_3SLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iofFmONIOxp__Koz0HYH__QwZlq2hzC4nNCGAaGaC7qP3wM4tb68BMw-2cAz1Usl5gG8weI9ZxeuNIJSlw0zvUBGuoLMP0Jti4pcmWK6_OXkcaN5iiSgtPBr9vdp5BzInk1mIR82hEFiyETq2_iHA1q08s4BcjjLPJBdTjAoSLcvdgjADOlqV-8af9_W9ZJ9XHkzVknBjW2EtG93ILu8Rgtpj8zHqFftnhVcfms1AGjAa5mBK5iCqhbP-rWnhFP7fg6iyL3SHiJ2g0W7vjFdkLYM7GEsdDaMGu5nc_K8vdETi7oPWw4H87E7nvoV6wB-C84Pi7qTBmww8_fN4rymtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=DoEjvu1-kEpAvf_8gxDEDqVpRFg_9yPxOrhRaL2qUXIlBvtfPmC4t3f7k50nFRre60bEHjl4WFqnz-VyKbUqHXbTkFtCvqfCyGQBWnnZa5_bNKVVmXg-womVPtSltIBJhVEPmuQUPPrGPdrCCM7ZPM4HpFChxuKJQfrs0ZAtm06J7wFQnNujNTkWwLQqAmB3TmGXH2aU0DDHwaa20bBoYMbNfxqvLS2UbJLK-R2-oCPOht3iPJzK75R5uCut2I0D1_c6Ac7GDiKED2oetXHrd6ThJuTvFxwmhXUnnx09-Cb51uv6dgmsFVgPntYGIryufbjuylPS3spljNoOaC6szw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=DoEjvu1-kEpAvf_8gxDEDqVpRFg_9yPxOrhRaL2qUXIlBvtfPmC4t3f7k50nFRre60bEHjl4WFqnz-VyKbUqHXbTkFtCvqfCyGQBWnnZa5_bNKVVmXg-womVPtSltIBJhVEPmuQUPPrGPdrCCM7ZPM4HpFChxuKJQfrs0ZAtm06J7wFQnNujNTkWwLQqAmB3TmGXH2aU0DDHwaa20bBoYMbNfxqvLS2UbJLK-R2-oCPOht3iPJzK75R5uCut2I0D1_c6Ac7GDiKED2oetXHrd6ThJuTvFxwmhXUnnx09-Cb51uv6dgmsFVgPntYGIryufbjuylPS3spljNoOaC6szw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_jBadcUvu0FkgjqilEgITrvI0noFY3_M9_Ix591GO20UFbC1WIMEo8RFDVut1DwKRyIDLdHtw5fRb6_FPHpRebgYoeVAgfnBmAjw89bL-wGReI8oXPtVus5sseD6rJmAALlq2-7eT88J4kbzXc2bRAs7lNkgwcyc6JtmVnX05CPc97LTfr_uvFEi690q8KYQX8OUiBxpueq1QPGG2viUu5-8fb2VwI88o7dfpaaq126r9_2v2UEBc1cbsXCVt87vltxz6YY0zdcwnJBzxjTPKhKgH_nNswXvyS9AG7RqxsfMiz5dpb5c84ozxAYnhKTkoo5AFI5veC1wbEWSDCJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=mjbj7F0-eErbAomym6eJ2V7nMLO-NuhsY2AxLkoLxCeeaf8C33-RLXocswhm3mCAkEkE8yoVjpKOZqLkW1KBbu6GkvAh68yWJ_7xn3e_aZsMbjLVFJ3V58e2G5_v0SgXrdnyatNAlTteiXGWopPKWUZoOoQq1Mh-6TXHUYOaOoFVxCJotlgd7WjhtIYNNVVQEGU5jhybIEsE03iT1bKl3m6rSiMsUD1alghiv5L_kWVJpVLLA072f5pPRPATxK8UVJHcmD3h5RLvXJEpRiZ76ZD3JiGuI6D2lBd0XT1E3DBQFzUWbcYMynVlnZfLEtcXZ5mxGg_Hfl1kSirKsP9Qjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=mjbj7F0-eErbAomym6eJ2V7nMLO-NuhsY2AxLkoLxCeeaf8C33-RLXocswhm3mCAkEkE8yoVjpKOZqLkW1KBbu6GkvAh68yWJ_7xn3e_aZsMbjLVFJ3V58e2G5_v0SgXrdnyatNAlTteiXGWopPKWUZoOoQq1Mh-6TXHUYOaOoFVxCJotlgd7WjhtIYNNVVQEGU5jhybIEsE03iT1bKl3m6rSiMsUD1alghiv5L_kWVJpVLLA072f5pPRPATxK8UVJHcmD3h5RLvXJEpRiZ76ZD3JiGuI6D2lBd0XT1E3DBQFzUWbcYMynVlnZfLEtcXZ5mxGg_Hfl1kSirKsP9Qjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=I0k4jo_LdRFlZauZ_fGD-jicf7CXXkA8RE6Gdo8TC7uaDqdaDVQ5UAi_nlADP3zl3HqgMsIr5X3DxdSEEVhhMcKOtxIGTtcJ-dwdLRzhX7Mv6KqM58Tek51E0h5PnNJZDvO5fiUKr_NDgIdG46Vs6cumrg77GKlFhwEm8jvNAe1Eg2t_yaaSRuuGm69KoNAj9qn44_dAOoGD54C2hBNEX_ZhY7kHQ8RYBlwEvJuO4KTjTCAW9hIwiLRBfVScOLTeB8mOHtEArfOTYDqV2L2ScITNavPYf1uTMhWEjWTv-R4f4_3s_2_CM3fJb5jntulu7EAztWHVxb-N3OthmvazRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=I0k4jo_LdRFlZauZ_fGD-jicf7CXXkA8RE6Gdo8TC7uaDqdaDVQ5UAi_nlADP3zl3HqgMsIr5X3DxdSEEVhhMcKOtxIGTtcJ-dwdLRzhX7Mv6KqM58Tek51E0h5PnNJZDvO5fiUKr_NDgIdG46Vs6cumrg77GKlFhwEm8jvNAe1Eg2t_yaaSRuuGm69KoNAj9qn44_dAOoGD54C2hBNEX_ZhY7kHQ8RYBlwEvJuO4KTjTCAW9hIwiLRBfVScOLTeB8mOHtEArfOTYDqV2L2ScITNavPYf1uTMhWEjWTv-R4f4_3s_2_CM3fJb5jntulu7EAztWHVxb-N3OthmvazRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=ACpik9tLJ1lkHmpsmizyfYcdITNHM5siZjX_JnWw2gZ92fkNk4dp2uVstLrDI-ugYwutjo4V9slGzVOBgAFeciT2d0CXChUVUEzvoKntXCsN43FqgrNXF2OAKeQBpSbWD2cUK2-eZ-Wy-IrHnokPK8Ju1oj5ek36LOrELHSw14yk1xQ5WwOU3TpUudJ7KZbiHN3QsHlWIOuRK8qSFfCMKRjT0VExgiF0ydo7bUwv3dlG2bR1KJYxPF-1kXj5T8V92pssJAT7GXu7SxPP9OD3z0Yhmznno9YWuFPsD_THBojQmp4u2p-kzX7PaZQxPW09CsY8qfj4Rhm2yj9JqG8Lyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=ACpik9tLJ1lkHmpsmizyfYcdITNHM5siZjX_JnWw2gZ92fkNk4dp2uVstLrDI-ugYwutjo4V9slGzVOBgAFeciT2d0CXChUVUEzvoKntXCsN43FqgrNXF2OAKeQBpSbWD2cUK2-eZ-Wy-IrHnokPK8Ju1oj5ek36LOrELHSw14yk1xQ5WwOU3TpUudJ7KZbiHN3QsHlWIOuRK8qSFfCMKRjT0VExgiF0ydo7bUwv3dlG2bR1KJYxPF-1kXj5T8V92pssJAT7GXu7SxPP9OD3z0Yhmznno9YWuFPsD_THBojQmp4u2p-kzX7PaZQxPW09CsY8qfj4Rhm2yj9JqG8Lyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=DoznEjoCNCsgK9WXtsuCOzLdJVSZCSFKSCqVdq0JRPLgscDIwSmfBvmGbQKb1PDPHkael_hh1iqoVP0zchXvw1zUsm8sol7FYS6ho6phT9LJLyzMBHx1YHYQL6FMJxy_W10PluWFc8njPekv3NJF-3uz6tHh1whujTetfeV9bRbBFtqH_JQEjny6gPNDAZSFoBk_v8egXTRpgoiL7Pp-wqPk0pAnfxnoAjgCOCE0mlQV9KNasYQvug_xPtfsXaShwPGyL3uYisafUr1pl0P57PeicMBRT_bAakclYRkuWslG5VCH3MkSsWro6mu9jbank-GwHYCUP3F4oykNuGy9Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=DoznEjoCNCsgK9WXtsuCOzLdJVSZCSFKSCqVdq0JRPLgscDIwSmfBvmGbQKb1PDPHkael_hh1iqoVP0zchXvw1zUsm8sol7FYS6ho6phT9LJLyzMBHx1YHYQL6FMJxy_W10PluWFc8njPekv3NJF-3uz6tHh1whujTetfeV9bRbBFtqH_JQEjny6gPNDAZSFoBk_v8egXTRpgoiL7Pp-wqPk0pAnfxnoAjgCOCE0mlQV9KNasYQvug_xPtfsXaShwPGyL3uYisafUr1pl0P57PeicMBRT_bAakclYRkuWslG5VCH3MkSsWro6mu9jbank-GwHYCUP3F4oykNuGy9Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=ckf5jr7IeLK2BNR2j-vQ3PnrcEnYKb4ZqbJatxacKExdV4afarmHkFJ8HlQxY1qC9RBmluYPWJ_y_9iGwHIDQEIKMZvRw0JrikpMazXFuNYiOU0TkWEdo_waQaj9vouyAtYin8AiKUKLwXhL4ZX1fMXHzBg6O3j7RuwWI3xsK0MLeGDatj66Z5hkR0WeQ_0Z1RqVOZSkoIo5XO45yDmPek4dv6WexTsF3qLFJ_xLI21G7kyg6HZHTzHmsPl5H4xRgU8uD5uIL0Kdu5Www_oJit5TeIelFwEC-DFms1FBtHik-xEAzujHjcHkhEA-sEWZy8wv8Rv4tH9BbZTkiJCE7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=ckf5jr7IeLK2BNR2j-vQ3PnrcEnYKb4ZqbJatxacKExdV4afarmHkFJ8HlQxY1qC9RBmluYPWJ_y_9iGwHIDQEIKMZvRw0JrikpMazXFuNYiOU0TkWEdo_waQaj9vouyAtYin8AiKUKLwXhL4ZX1fMXHzBg6O3j7RuwWI3xsK0MLeGDatj66Z5hkR0WeQ_0Z1RqVOZSkoIo5XO45yDmPek4dv6WexTsF3qLFJ_xLI21G7kyg6HZHTzHmsPl5H4xRgU8uD5uIL0Kdu5Www_oJit5TeIelFwEC-DFms1FBtHik-xEAzujHjcHkhEA-sEWZy8wv8Rv4tH9BbZTkiJCE7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=qro3K5DRfT1RzJHjvW5PMTIPRfUK_ntA49L-RroT_JVhx2Dob7YcT6R0rBmkagfk9xMHUQ4XnqiX3OmucKRiExR14GBn5AMFTECbvfdse0rXJrgjGGX8r1smlS7y6LhuToHiyMee6k99_eJGBVC8SCjT2YykPcsx0hX-52AqPaQdygFLG5B4HT1K72D7qWr8pK5WZ6crRiV4JhMPHk0GX26mip7mW5GLso8-X7Mk06ZvPCI3b1Nv0yZWsTI9p6Sg9AA1M-wwiy2y62qtCHN1OW2uxztD0d8IJ9U055hROD2NuYr_F3znLAH9sTmA0TLkB83IbCaTT6s5uuJVlcwZUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=qro3K5DRfT1RzJHjvW5PMTIPRfUK_ntA49L-RroT_JVhx2Dob7YcT6R0rBmkagfk9xMHUQ4XnqiX3OmucKRiExR14GBn5AMFTECbvfdse0rXJrgjGGX8r1smlS7y6LhuToHiyMee6k99_eJGBVC8SCjT2YykPcsx0hX-52AqPaQdygFLG5B4HT1K72D7qWr8pK5WZ6crRiV4JhMPHk0GX26mip7mW5GLso8-X7Mk06ZvPCI3b1Nv0yZWsTI9p6Sg9AA1M-wwiy2y62qtCHN1OW2uxztD0d8IJ9U055hROD2NuYr_F3znLAH9sTmA0TLkB83IbCaTT6s5uuJVlcwZUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=YoetVc8Jb5i2j8_9GLx95JiNaxOQ67jiXGJfUYTt1fQCxQ0bZPd08uZfvxgL_oXtpAwflRAlD335LyZ1Pzarxes_E-Kzxr_KDjNeV7VZKxqiPB7Ww-YdvBzLNsHLhJGuCxWFn4UeirBM4S5WF5D6DhX7nl4c4dHrO5cgvs7ET_Im9Tn2I4FsoUFN-72MURH7KnjVXHyu3zAyVsn18iWD5hLXcbWfw0eeJcVDf4E2BSUFXTqr4rBOHwPl6WueVKrMEk4A9cnad38Qf9YebUmvsYqJXA8Z3GjeOGz5lMrHufCYuWPGwfKsnKPSI9WPwkQHn_DEMjShUR--ejLKINNuIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=YoetVc8Jb5i2j8_9GLx95JiNaxOQ67jiXGJfUYTt1fQCxQ0bZPd08uZfvxgL_oXtpAwflRAlD335LyZ1Pzarxes_E-Kzxr_KDjNeV7VZKxqiPB7Ww-YdvBzLNsHLhJGuCxWFn4UeirBM4S5WF5D6DhX7nl4c4dHrO5cgvs7ET_Im9Tn2I4FsoUFN-72MURH7KnjVXHyu3zAyVsn18iWD5hLXcbWfw0eeJcVDf4E2BSUFXTqr4rBOHwPl6WueVKrMEk4A9cnad38Qf9YebUmvsYqJXA8Z3GjeOGz5lMrHufCYuWPGwfKsnKPSI9WPwkQHn_DEMjShUR--ejLKINNuIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfOJM-PKHXFf1QGvwqRbKI9jWA6aodk0jIfxaQGdO4rp_Wb5fwIKKz5HBBGafHMyxwclK3E0HItItbVWiA91BALzL8XAtnTASqv09AYVnGsQrcFqlrFgCwAcmzwYPdqarNUyER81J24PghCLE3T9NyLC_o8Qo0UXxduY9KdS6RdB9jgAFdOo1AsdMXL4FxW7MwpO0fZK4L4CzaBZUKrMziQ7YARG6l7NT0T0nmBAK316N8mdEaBjdfxalcLjdIZ2SXnPTDDpaeDyHdFnXRwHg24c8PMY1pvBz0CWsHOK4SzG9_8llvrYZ-vjAIrP6nRs8qybyIMtvrYkJ-cZiUepVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEToxe0Sj2RPbf4zhNWwTEIZny8dyVexGGq1Dwff0_7_OMycdBtGN0b2tov4VqqlACi-wggvuPpPdAiRcCebucRnKpuDIfVa4H7Ybf0A0xZYjCAH0laBto9H9A9tF_zyGSehdU3CUAJ0LTDXhtXi8DXbDIH7dH3q2QrOkM8u-bN-28kSueyodr-PSsAglnbv0UuHkAnGwvsGQd3URKiSUWphn9q6rBjZym3Ga1ve72ntmNmQzDLlm16JbZgDyKcVnS8zNS7STO7s9Mo6IdtNqXPeTdQ2bpm_WbMvXz9tbsxaPzQDgoZkk84dEfhx8VavoUJRCvBjPPwGrTr-BGaJzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=eltbn5I9vXUDL29Oiw4kMyWfvQ1JzhmqmfRjuEzQ6JyWUVCRKgOZUNanUGbtOOfUNKeNSI9l_Pki0U7xwwINbk74pStrhF1ULQi29cmU_lhXDEfXzJ_j1wfwV6MpipocnRvcvI2HQhVhyA0ZkzTU9EEJf8yVdRcB0MTiOLbq00lpjzOmbZ6ONCAMHWV8CJsonhxeuIjODx-sK51h81MA_AjAdq7-zxQJeyYZ7-d7LDsa8jkhTLCWyeTFNB24XKuAD8iAs_XLgB2e9jVL7BXpCzNGP0egzAlS8k85YVYOtitCuxCRstIHY_dQMAo7281_i6JNQ5EaDn08UeJ6CoKY3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=eltbn5I9vXUDL29Oiw4kMyWfvQ1JzhmqmfRjuEzQ6JyWUVCRKgOZUNanUGbtOOfUNKeNSI9l_Pki0U7xwwINbk74pStrhF1ULQi29cmU_lhXDEfXzJ_j1wfwV6MpipocnRvcvI2HQhVhyA0ZkzTU9EEJf8yVdRcB0MTiOLbq00lpjzOmbZ6ONCAMHWV8CJsonhxeuIjODx-sK51h81MA_AjAdq7-zxQJeyYZ7-d7LDsa8jkhTLCWyeTFNB24XKuAD8iAs_XLgB2e9jVL7BXpCzNGP0egzAlS8k85YVYOtitCuxCRstIHY_dQMAo7281_i6JNQ5EaDn08UeJ6CoKY3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقام انتقام!
بسیار به جاست که یادآوری کنم
اولین گروهی که رفت دنبال انتقام و خونخواهی
خامنه‌ای، گروه تروریستی حزب‌الله لبنان بود!
و پاسخ نتانیاهو چنان بود که جمهوری اسلامی برای نجات حزب‌الله و بیرون کشیدنش
از زیر دست و‌‌ پای اسرائیل،
به آب و آتش زد و  پایان جنگ در لبنان رو به عنوان شرط اول مذاکراتش با آمریکا عنوان کرد! در انتها هم بخش زیادی از خاک لبنان دست اسرائیل موند و یک میلیون شیعه حدود ۴ ماهه که آواره‌اند!!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNbotPyKpQ_YKQBvmGRZolCyY4VqI8fDTdb-2Rg-rKra-ZazUi9E1btqLMQtRiBXIObn63zlxmkLpxqNMs5LvjHhxFKcCaPpbTO6OEmqtUNlEfxckFswJvwzNQV0171tli5X2m0O4jy3UP9sDDlF0Bnbjs8xAa0Hwt9M7EzEvvhyYuiuPzPIgZrWR6gEFBrpgg1LCrksGpVU5NAxnrIjs8JAo39cxCJgywZMl_OdGCsZ_8PlYskbhOJwXzT4kqL5N9lXfi3apfWBbUSRX5-UQPvE2GeorLD0-cUqCgz5i-69nOINIads6dvqNJJytaVrRM0GNNntNGBQObjERydyog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه تروریست‌ها
الجزیره از دیروز شیون و زاری میکنه!
زمان جنگ هم، در حالی که جمهوری اسلامی به قطر موشک میزد،
الجزیره به سود آخوندهای جمهوری اسلامی گزارش میداد.
وجود جمهوری اسلامی سود هنگفتی به قطر میده.
قطر و ایران یک میدان مشترک گازی دارند، بزرگ‌ترین جهان.
۸۳ درصد درآمد قطر از همین میدانه!
راز ثروت و جایگاه قطر از همین میدانه.
سالی بیش از ۸۰ میلیارد دلار به جیب خاندان حاکم بر قطر واریز میشه. کشوری که جمعیتش (بومیانش) کمتر از ۳۰۰ هزار نفره. چیزی که باعث شدت قطر ثروتمندترین کشور جهان باشه بر اساس درآمد سرانه!
جمهوری اسلامی اما به خاطر تحریم‌ها قادر به صادرات گسترده و رقابت با قطر نیست!
تداوم جمهوری اسلامی، یعنی تضمین اینکه قطر همیشه بدون رقیب می‌تونه از این میدان برداشت کنه و درآمد هنگفت داشته باشه.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اگه توی یکی از کوچه خیابون‌های ایران
شنیدی  «خدا بیامرز» یا «خدا لعنتشون کنه»
حتی بدون اینکه اول
و آخر جمله رو هم شنیده باشی،
می‌دونی درباره کی دارند حرف میزنن!
و همین خودش خیلی چیزها رو
نشون میده.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPYH7wliqbH3O9XX2_5TcppHCF0SSvBAMmiKXOxC9rnMOf6Gjgf-mbCE3zyyKUGYN_sL6QwRYltyAP741ROl7umDjMPPx2cGHnavo7PQIIObLtywAetSVQssFglFUCXbpn9ILtypqsWtVXxcrk1iv0TnOVz3nIncZGWNu9p87DAplMzmB_SdzCpceNfENWnAUcxiYzzQzXEJlQXCLpzydtr1fJk9hgdDdWSAI2t9E2AWE671ERoJicFHTkhDhwCqGMoSsHd-DPAcrg8uGzrOh20g_R4MTr8C-Ed4vGjZ8U3EA--k7prDyTnadJKPzXkNFboQkB7iXDDdt1_mH4SQ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=kfEksEVfypID0tyQh9FfybW83htIHkGotOKBjV0fcNSvxn1ur9u8bvn5NAXAWR0Bu0HRGGQRtRwZMcRilnIUfRcL14ij5lNmkTGWd04t7YZYQ4kXVcvgXC1EM9sqRpV2OFqePkcqguYZ9FFBcT_RibiA11yCd67mhnkF3hxKyIhMme3Vm2fskNJKPFyQkztIMFC6f1eqn08ajkWtUR3KrUqccpKoqt9BMeMANFhTzikoBCPfQxRwc5NsCQIwLygiAXPuMnnrRKoQ8uBlyOHPWF7QR4WtApUaikK15ESuSZBnb1vykdbf0G41fhiHzNYnI8GyYlt2l-RwmjrKTFR6xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=kfEksEVfypID0tyQh9FfybW83htIHkGotOKBjV0fcNSvxn1ur9u8bvn5NAXAWR0Bu0HRGGQRtRwZMcRilnIUfRcL14ij5lNmkTGWd04t7YZYQ4kXVcvgXC1EM9sqRpV2OFqePkcqguYZ9FFBcT_RibiA11yCd67mhnkF3hxKyIhMme3Vm2fskNJKPFyQkztIMFC6f1eqn08ajkWtUR3KrUqccpKoqt9BMeMANFhTzikoBCPfQxRwc5NsCQIwLygiAXPuMnnrRKoQ8uBlyOHPWF7QR4WtApUaikK15ESuSZBnb1vykdbf0G41fhiHzNYnI8GyYlt2l-RwmjrKTFR6xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک گروهی در جمهوری اسلامی نشسته بودن و برای هر هیئتی که برای ادای احترام می‌رفت، یک آیه خاص قرآن انتخاب کرده بودن!
یک تئاتر و شوی آخوندی!
مثلا برای گروه‌های تروریستی حماس و حزب‌الله این آیه‌ها بود که آفرین به شما! کارتون عالیه! ادامه بدید!
برای عربستان این بود که مسلمین دو گروه شدن، خوب‌هاشون (جمهوری اسلامی) مبارزه میکنن و بدهاش (عربستان) کافر شدن!
برای حسن خمینی هم یک صحنه‌آرایی کرده بودن و یه آیه‌ای بود که مثلا تو به اندازه کافی جهاد نکردی! (خامنه‌ای خیلی جهاد کرده بود!)  و….
ولی از اونجایی که این خودش نوه خمینیه و خودشون این درس‌ها و مکرها رو به بقیه یاد داده بودن، وسط خوندن آیه ، احترامش رو جمع کرد و با خودش برد!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=N9VMZld2nobQwof1m7usKxJ99iqHq9tI_gebJXTBGuXdSD8q__jPohF7Ix_tDafXqMDzTHZxCaa7j9kpNds6wW6H00n3oMYxH0Zhjum3Z4-sEmLviCx7HlcuadMiYkb5qEWBcgsR7u19sL9x0e9P4WeLdEwoUHxSTUlIoq_1QwK7qrjXr6_4FiNgWhqT47EkDkqN9i-uEQqdZZC7jyb29maNw5grtU6ZVzDlcoFshfwvqkSUMfUJbAPUY99jJ9kXRKLSvNCU1UTQUlROQGFTFvPqn7xn44PruLxopMJxflLswp7usjYdxDPWct67hq-yDQWe6QQP8uvwvmzGrHcZew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=N9VMZld2nobQwof1m7usKxJ99iqHq9tI_gebJXTBGuXdSD8q__jPohF7Ix_tDafXqMDzTHZxCaa7j9kpNds6wW6H00n3oMYxH0Zhjum3Z4-sEmLviCx7HlcuadMiYkb5qEWBcgsR7u19sL9x0e9P4WeLdEwoUHxSTUlIoq_1QwK7qrjXr6_4FiNgWhqT47EkDkqN9i-uEQqdZZC7jyb29maNw5grtU6ZVzDlcoFshfwvqkSUMfUJbAPUY99jJ9kXRKLSvNCU1UTQUlROQGFTFvPqn7xn44PruLxopMJxflLswp7usjYdxDPWct67hq-yDQWe6QQP8uvwvmzGrHcZew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با امن شدن اوضاع، سه پسر خامنه‌ای هم پس از ۱۲۰ روز غیبت دوباره ظهور کردن،
اون یکی‌شون همچنان در غیبته.
رافضی‌های جمهوری اسلامی اینقدر کینه‌توزن
که برای مراسم خامنه‌ای، ۳ رئیس جمهور قبلی
(احمدی‌نژاد، روحانی و خاتمی) رو هم
دعوت نکردن!!
بعد در میانه جنگ میگفتن «علاج در وطن است»! حتی برای خاکسپاری رهبرتون هم روسای جمهور خودتون رو هم حذف می‌کنید و راه نمیدید!! تا این اندازه تمامیت خواه و کینه‌توز!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=DMSYuZr5jm9OoSvQKyUz6YGh0iXAEaDAtCMbovlRwZpJ51TjgIXzMLnlMLm8dlAxnF28uaJc2wGSromH8NLn4MnIL2HOBoEyzrfBCFXS9-Pct_1FlgJahuN-3MKQu7Vvaf4A5OkaGQT5Lj1oQj8AZOIrkyEfd46TpFeCTcTFSMrSodw4Yz70JGveGoL-EzuHuLN7wBAXPx3kgp2YcY6H5Br1hIyrODoKsCUhlGVF208D20swx3LKCoJgUhudZnSyKiN5ct9KDYTwb9upO-257EoyHfBy65FR-Ca9C5o1XsDFOXfRdMGsGQaEiphoeLErkE_m7g06y-S8kA1wBTAPvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=DMSYuZr5jm9OoSvQKyUz6YGh0iXAEaDAtCMbovlRwZpJ51TjgIXzMLnlMLm8dlAxnF28uaJc2wGSromH8NLn4MnIL2HOBoEyzrfBCFXS9-Pct_1FlgJahuN-3MKQu7Vvaf4A5OkaGQT5Lj1oQj8AZOIrkyEfd46TpFeCTcTFSMrSodw4Yz70JGveGoL-EzuHuLN7wBAXPx3kgp2YcY6H5Br1hIyrODoKsCUhlGVF208D20swx3LKCoJgUhudZnSyKiN5ct9KDYTwb9upO-257EoyHfBy65FR-Ca9C5o1XsDFOXfRdMGsGQaEiphoeLErkE_m7g06y-S8kA1wBTAPvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aV6o9onXSv2zWEo9GxsodB87X_sgn3LT2gSfNeqLi8B0Jrvk2z-KpgmpB9jkWkIK4XfaCRI0UeXJHy26njNbb6csNLM1i_sg2FmKFjSEHZBSeiWyl5S6ukW7dBpSHVAIZ1wk-4hSs4ermjc2Dqqz_sNRNO2DaMZQCzwmoGdgyZL01guSKEJhQMTxrxWtueqagqCBGP24g7XLID_Zip_8HODVVsZCxLyinui0qa15dxNaim91asbQ2JCmYvwh6cEZWP12MFaGdZRGX9YQcj6TPw9E3RXtSRJaFPBy9axIOFJJ391p0vBIDMXqdf46WbAm1uF4qTWJm5QnOZB-CEdhSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iegAEbmqeQQTT5AQvfzXO4ZIUt6N95QPdtNTBw0m51t4HK8SIpXFcLtP1yEiNPRSHR_5qUvG-HvgjEglxacViMlqqfEhwY2HHsNDq2M6Ni8XzhSq91RBhtLI6jlf237BS-z4Ogb1BdlZA4_YlKfQWIy_zkPJ97Yg6EfN3TDjXtwXi2H5wwpsyjAUJR1YoBksWDygK_AeLmIp6l0aibmWXvD1Em8UBDciL9BPwfEDTK7_EEfSjUCl-DaE2Lt9rQV5QJh2js6JLM6UpzefbjmDYo3OAmuQqd7jYVlUxPaGoYepghPIjzX9W6HwMRw8eDMOsE04pGOzY8SWn8N1EOIPjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=qmJJO0P8laY-BUc-m1j9DCivRN26sMMnq8NPjfnuouEH4s1PMxvtAJ6cDftk41E0-KlHjaALZnVIrgQEwB3uj6m-iLpdf_-4ERu-Bmkea2H00TUeLC1yScvDBt2R7B4yR_5dtpyA1dLMa08riqzCejGb22njrrn8cLnLcRbkBZ7UeUZtZROhzQEpmh0csEpvB__gxxFOqvPenYyR98fHJcYjuhRE_eNeOQoanlpLPfkf6CdUUkkJ6i1nZ5raqgZR0QXnqTbJeA7tgP5XgyY-TKAuqbTuKie6CUASOjFiQWambLZ0rSoHI65Lrir0LmvTuXq-LkdDs4CMD9EctB59GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=qmJJO0P8laY-BUc-m1j9DCivRN26sMMnq8NPjfnuouEH4s1PMxvtAJ6cDftk41E0-KlHjaALZnVIrgQEwB3uj6m-iLpdf_-4ERu-Bmkea2H00TUeLC1yScvDBt2R7B4yR_5dtpyA1dLMa08riqzCejGb22njrrn8cLnLcRbkBZ7UeUZtZROhzQEpmh0csEpvB__gxxFOqvPenYyR98fHJcYjuhRE_eNeOQoanlpLPfkf6CdUUkkJ6i1nZ5raqgZR0QXnqTbJeA7tgP5XgyY-TKAuqbTuKie6CUASOjFiQWambLZ0rSoHI65Lrir0LmvTuXq-LkdDs4CMD9EctB59GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها رو!
آقامون چقدر قشنگ رفت :)
چقدر دنیا رو زیر و رو کرد :)
در نحوه رفتن آقاتون، چشاتون قشنگ می‌بینه، ولی انصافا کار خودش نبود،
کار اسرائیل بود!
ولی بله همون زیر و رو شدن دنیا بود که
باعث شد که یه مدل قشنگی بره!
برکات رفتنش هم خیلی زیاد بود!
طوری که رهبر جانشینش ۱۲۰ روزه
که معلوم نیست  اصلا هست! نیست!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=tYdI6cns-BpMrSXGLp7HcLua-yNJUOmzDEYZJ8R1k_OKqM9qMcifUgUFknebGw3peFew4guoKtcrs6cunIGoN-dyjAl4Qh9Jk6SEoyvoZV292yICyuLKqCcDptpq2-wkrzOjPSQRC8r22ENwqOF6_zH54imQFLj1BYFSsmzYIgVygSCaz34H6Y77CNaYqasLhZthOILIbDeLQ2nSJvIBUOAYtn_m4Z27qruvmZy8_BTG6Rpxam-xKkWpxzSuIMk9ZJGwNqjdO6nuniP2FEZx__fXleVoUAnqNZaTVuFJJLIuie-B1N3pbYKKhs9FZ3xAbxU271po1D9rgXqaoUoDBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=tYdI6cns-BpMrSXGLp7HcLua-yNJUOmzDEYZJ8R1k_OKqM9qMcifUgUFknebGw3peFew4guoKtcrs6cunIGoN-dyjAl4Qh9Jk6SEoyvoZV292yICyuLKqCcDptpq2-wkrzOjPSQRC8r22ENwqOF6_zH54imQFLj1BYFSsmzYIgVygSCaz34H6Y77CNaYqasLhZthOILIbDeLQ2nSJvIBUOAYtn_m4Z27qruvmZy8_BTG6Rpxam-xKkWpxzSuIMk9ZJGwNqjdO6nuniP2FEZx__fXleVoUAnqNZaTVuFJJLIuie-B1N3pbYKKhs9FZ3xAbxU271po1D9rgXqaoUoDBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vore01CzLHEap85GMpUv9_Wt62AZKPba9tu2BQnKtNAnT-amO8sLsLUEASpJhpksCq7XO7tP_noiOqfki08Z7XTa5pJr_6dFfmnuLM1NqcFxnCznZDF1O7CyoNyRJ9Otw5O5tCsH8hluX7hYJLW5ieESYo8-T6lOMWTe5V9i2Gl8cX1zsZncjjc8bTMNshMJZ0yfCajdrEVEpHe8EEvVFu7U0c-gtf13lLd8mv_iF-jnhcCQrY2JnvoAVxewUzR3iAGyqlt9bd1ctENi2FJTAFBYkJd7Qs4ONtj0GKx--KugAbgMGaunfYmK_3bp61aHNmCJf3krBWl7cNlaUDbIaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkxbGwE2sf-KoUH1QwOFVlWtfHsyvTJULZFB9c2R9RLXOwQQQFzOV_-3OWUITvHguoXJBOFS8QCnGOpsCHXYRjq18lbplyT17OKezLlQiqf5V4xxseizoLDXPfE7VayccEJTZmbhzYLuYRJU0n2HnOBaEi7T4706AapMY1S9_tRRQmrjVL9xkaBxm5B3L9SfO19xNkbVD89teVOrykwlVCxFlWsi8dKdROMyXQjtpDLc729NrPwpLO6vZjdaiGGBKly2b0BnljniGFIsguYBkEzTk0yTVEzcWOaxZ8VOenoneNuUL-1wsnkw7zujM5rxMAiBRHLeaLW1UNUaFcIT-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWIu3HwTlCWQcLjRHavlFb2McJYofXrnbaLwT3LxEK8UDlnTVpHvwzre6ofI4ssOjE46dP-XTqULAOR5iq_qPhPZYgokpUT-_NqXEntEbJhQwXsTIbYndPwFAegMJSnJbod-XaI4omPTmQZHwyLTdxDZpubdlLt1KgE-lczHAzjYXpEYloePTAyhzla6wdR2hQA4DBnoPhfZp7-IbDA-dIlKxq2bv8HXhkEL92tY3SfweMYYLeHGo6MN6AGbY0gxKt3yyFo9kpyKfOWyCRt8qIh_CtzJVrKk0LY6yBT0yodQqdJObKiGPixb8cvQvykaXkWRsfEdSsBjxbRPjrNJvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8QHevx76QLBni8t5H5RPRa8ZcDaCYWxwgHNxezy255yGa7BAbldL54NOcTaXjLJJi3qsd5vIFcyGCDVUVl8s7PKTLtDtujTUuqlQEK77hxSdymzQewYBFDEKSg8dTmr56sWSyuHnuls8to98l0LOcnBFJAZJtsw3jIHCxX6NfYpaE5Y0Vt3QiBAUtxcl59PEdtAZ7bAQS0DpeiVoIOKwdl0qK5WhwYhRiq5naxODvMOEDG3lv5wNCH6vTGOYSN_hz6PVG4uKrCCqRigUS9H1kzvLAaIH0VRoLfDQtN4jp2m3glAfLECcP0mwnDlz_PyjL8cORdlSIPuI4dtagNotw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBYPjwYLqdKMpVv-zc-0omF_PVHn8QrRBSSr_lvpAc807RPfhYLeAoNYJh0xeZ6IuMAgxcO64TccWqZ4uzx3Zb4bE3_LjUJophirOAR45EOYtRvoi0c3ictjDVRvB5m4n1YtDPYXbXMqaVmGeTB-8vIHXJjr77SpCGE10ID6G-QX8vJCkVhmd3akNkpUSFaBvYSlHpr7p-2lFBflcVSn2RpRnBKapx7V4guEk9OPh-qj3x8WmysWtjl3WU2CPoTW5yozQ7Jcyg9w6qyAkyNA19TKxRC5yBLy2qLJwmYYY1oYxeso0dmwdV18dIZFpNecSgIFuBmyy6ltfyf3Kc3yFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان «معاون وزیر خارجه» فرستاد
اندونزی سفیرش در تهران رو!
ترکیه معاون وزیر خارجه و معاون رییس جمهور
دولت لبنان «هیچ نماینده‌ای»
در هیچ سطحی نفرستاد!
تشکیلات خودگردان [دولت] فلسطین «هیچ»!
امارات «هیچ»!
سوریه «هیچ»!
مصر «هیچ»!
تونس «هیچ»
کویت «هیچ»!
بحرین «هیچ»!
مراکش «هیچ»
اردن «هیچ»
لیبی «هیچ»
جیبوتی «هیچ»
سودان «هیچ»
ولی امر مسلمین جهان :)</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaIAuFP0XUfDSxL7II2JjtznSk7BhVtibik6x_W0irXKeN7bq92_Glr4r7Kdob2hcZexGwhvJPU_e-tP-Ef3L2UA3l5wxpXqKZC0V-FZWPFPFwAkbz7ARlPNcsC5esFt4oDukBUxBZGjvwjk_DgtZ_v58FCpQop--MqdeVzIh1oba5VsdtCpeULQReopprhFOZpzZ2sGaAb7F4gWD5HDWAzc3-gMcB4LkUKeYtMC3wsULwIVphxfZqrGurjoSbgAqI_O99IOUkq-tf8GAWHMD9di23WXsV--ugQ2BgoMxnef67IwgwGq4dX77u73X3IOINaCh4MSsbC181wxzEGCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=BOwZKJYjV0QglKnPhtvIV8EJZkDIGuyGxB9IbuyVY8J1X9zI9A7pc9J0B3V5O2GirlGw3tHWWaCLfCQJFrd7zy5pH_-asH4wMXr0uQZg10uLzM_qyWrr2_7mqL8bts_8TNUJ1mgsdteTxF4qp_seNkAE4m6rjnWPeEwqWXxf0YxuT5VD_Tx0_dvQ7Xy7Oijaa3tDI1i4O-MotUE-x9lND2gg2cI6ief6QQOB0VWPoSA_k5FTt6Mx-SynwmCmY9WLxI4655nBUBIqyrOlx0OIbq0T9y5mXeNCUxV5gZdYuZwkLVOQlF2fmiJLHjQWwj7aT0DIozojEgibc5Oe6KL_uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=BOwZKJYjV0QglKnPhtvIV8EJZkDIGuyGxB9IbuyVY8J1X9zI9A7pc9J0B3V5O2GirlGw3tHWWaCLfCQJFrd7zy5pH_-asH4wMXr0uQZg10uLzM_qyWrr2_7mqL8bts_8TNUJ1mgsdteTxF4qp_seNkAE4m6rjnWPeEwqWXxf0YxuT5VD_Tx0_dvQ7Xy7Oijaa3tDI1i4O-MotUE-x9lND2gg2cI6ief6QQOB0VWPoSA_k5FTt6Mx-SynwmCmY9WLxI4655nBUBIqyrOlx0OIbq0T9y5mXeNCUxV5gZdYuZwkLVOQlF2fmiJLHjQWwj7aT0DIozojEgibc5Oe6KL_uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=C-vLuvgJVPSLgcZ_KnhOzD--7h3E79_k_ljiUJIi6bq5xp6RWarBaFcRbJ-9k3JstJ3GfeMvY4FLHI2Nlm0s2M6-MeWABjqi3KU_2N0aOc2j7lD7GU76vZm1BkNg-KnI1Kn3dm4CaUxJpCaeBtMG4n23WZTo_cj8vUTWkkRC38ezmN-YuVpSz5HY3Clz5EPlaj_1WNQu0UbUN_2lD7x1rs4BB5f6vGqlhAC2L55kqMgBei2Tfx84VEtMYMxOMpwRiK8G50tLNlUWlRtrhj1z8lcyjMxuRHhdWJe-0DDnkE_JiB7oNACI0LHelBGYWJ9Vfew3TFH_DdrzJkCvn9TPew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=C-vLuvgJVPSLgcZ_KnhOzD--7h3E79_k_ljiUJIi6bq5xp6RWarBaFcRbJ-9k3JstJ3GfeMvY4FLHI2Nlm0s2M6-MeWABjqi3KU_2N0aOc2j7lD7GU76vZm1BkNg-KnI1Kn3dm4CaUxJpCaeBtMG4n23WZTo_cj8vUTWkkRC38ezmN-YuVpSz5HY3Clz5EPlaj_1WNQu0UbUN_2lD7x1rs4BB5f6vGqlhAC2L55kqMgBei2Tfx84VEtMYMxOMpwRiK8G50tLNlUWlRtrhj1z8lcyjMxuRHhdWJe-0DDnkE_JiB7oNACI0LHelBGYWJ9Vfew3TFH_DdrzJkCvn9TPew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=LL7UkH3t0LvuMPoGL2sPfHQi7DglF8IKRy9z0C1HkwnEWdB0l5_CnqJFkYCQr2yAFVvtmhurH-tgIrrKqJb-M1PBEK0t4YxtAYCJbhn4q4gu1FgJ-MrU-tFrt0xeGlc4IIL5zVCqkHgHH_OvfNjhWFdFDPHGt9Hj7cPQV6msGYMpdXaS-F0ikZ0O44WqrmVWvLPZCmaCaXypwx4dIWmXcfjUntk-Jn9s8LhW7pYmlSazRstUdb1oYCig0FwPSd6iVb4J8_u2AE6upZVeyHKx6CA5-kZ8GrqLIpDzPXkZtt2Urfz87Z9nwSqVw4ldakkmWFHPVQprT6Jwr6K3aRG28w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=LL7UkH3t0LvuMPoGL2sPfHQi7DglF8IKRy9z0C1HkwnEWdB0l5_CnqJFkYCQr2yAFVvtmhurH-tgIrrKqJb-M1PBEK0t4YxtAYCJbhn4q4gu1FgJ-MrU-tFrt0xeGlc4IIL5zVCqkHgHH_OvfNjhWFdFDPHGt9Hj7cPQV6msGYMpdXaS-F0ikZ0O44WqrmVWvLPZCmaCaXypwx4dIWmXcfjUntk-Jn9s8LhW7pYmlSazRstUdb1oYCig0FwPSd6iVb4J8_u2AE6upZVeyHKx6CA5-kZ8GrqLIpDzPXkZtt2Urfz87Z9nwSqVw4ldakkmWFHPVQprT6Jwr6K3aRG28w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=CRjgXHD8sE3Kak8H9efBJJFxoe6_JnAc_BCgyz7wKHrbvEG1hyOYRsJQ4u8VoZSDYLY1jj9Q5NksX4F5B4HZi9Q6r4msUni7obt2O8ALG0JySrrB93rdGT87JPuVVGhGk3fwZ2IbRyyErXc-IBEVRliWGb67C-l1YA9Beq4WVqc0xZUi7tQVDMW6l2iDn1jHcf7772gFsaHrXAp7QoO52bkglEUMkcet38ywbG4cTIqMGbMq0WV-CxYDreqTBnaUGH8N-SikoqLTh8hvx7o9NsppYmWR2luq_KmaHr19vgjdx3Yv4zEG084GzHPgJ5DrSDlnbpo9ot13M4C58SAxlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=CRjgXHD8sE3Kak8H9efBJJFxoe6_JnAc_BCgyz7wKHrbvEG1hyOYRsJQ4u8VoZSDYLY1jj9Q5NksX4F5B4HZi9Q6r4msUni7obt2O8ALG0JySrrB93rdGT87JPuVVGhGk3fwZ2IbRyyErXc-IBEVRliWGb67C-l1YA9Beq4WVqc0xZUi7tQVDMW6l2iDn1jHcf7772gFsaHrXAp7QoO52bkglEUMkcet38ywbG4cTIqMGbMq0WV-CxYDreqTBnaUGH8N-SikoqLTh8hvx7o9NsppYmWR2luq_KmaHr19vgjdx3Yv4zEG084GzHPgJ5DrSDlnbpo9ot13M4C58SAxlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=F63sxSGqM3jqU7xnElQnlEx8U6B2n8urz-sJKe_DIo7rsuTYVjdJMQmiiVcgL-e0bLqYa-mFenuQPqsviqiVGHNDELjpmI9QL8Y7WOSLrhrfhgwDNZIDtbmLROPvADbrrBV2pZAlD7gwA9rp8DYEWjsm76gOVV2Z0hUvbqrQzd3dicKPXhGqBoUvsK2tgBV9h_NumWNICu3LMuc_AoqVmqp97NyuqfMcNkoNwk34eSSW7oqR9s_18VjsO5F247QaBdzUqU_fDQZxDwIdApkRQUjjKck04nxPkgqUxQFbtbC_gZvuzu5Qc5bgqNij0Jjm2QiHz5aOn3mf74MxmmjFmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=F63sxSGqM3jqU7xnElQnlEx8U6B2n8urz-sJKe_DIo7rsuTYVjdJMQmiiVcgL-e0bLqYa-mFenuQPqsviqiVGHNDELjpmI9QL8Y7WOSLrhrfhgwDNZIDtbmLROPvADbrrBV2pZAlD7gwA9rp8DYEWjsm76gOVV2Z0hUvbqrQzd3dicKPXhGqBoUvsK2tgBV9h_NumWNICu3LMuc_AoqVmqp97NyuqfMcNkoNwk34eSSW7oqR9s_18VjsO5F247QaBdzUqU_fDQZxDwIdApkRQUjjKck04nxPkgqUxQFbtbC_gZvuzu5Qc5bgqNij0Jjm2QiHz5aOn3mf74MxmmjFmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=KOL8DIVxaDvcDWsOfnbO63_ntfa33R0VIY82VCCL9GPnVuTk1gXWjsxZ2PkCAGPnnLhrbcGbi20GjmD9_Gv-GNxqT2jn3Ct8C-sftVqWhGkSQa9QX-oePr-KBC-KQvRcDxcwl4ZkSgVwjcvUoF_w6tk_u_ceNAv2JbkLDjZM53yC1SfkI6FQSf32NDNZxEbMkyCdZW-JKPGx_DbFxmHc_jO0ptH9Pf-tNwQxq9TvpgsgDAcgJp76S5Uz4_xBe-PnD8E_O0FBGGkde-TO6mUHOm7svGe3eHywsNcqzwPmrSmnkN2Ltwnxdj-avg6p12_eVnm3N_Pj1d6Qaarkff-OBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=KOL8DIVxaDvcDWsOfnbO63_ntfa33R0VIY82VCCL9GPnVuTk1gXWjsxZ2PkCAGPnnLhrbcGbi20GjmD9_Gv-GNxqT2jn3Ct8C-sftVqWhGkSQa9QX-oePr-KBC-KQvRcDxcwl4ZkSgVwjcvUoF_w6tk_u_ceNAv2JbkLDjZM53yC1SfkI6FQSf32NDNZxEbMkyCdZW-JKPGx_DbFxmHc_jO0ptH9Pf-tNwQxq9TvpgsgDAcgJp76S5Uz4_xBe-PnD8E_O0FBGGkde-TO6mUHOm7svGe3eHywsNcqzwPmrSmnkN2Ltwnxdj-avg6p12_eVnm3N_Pj1d6Qaarkff-OBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟
با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟
چون مبارزه آنها برای “ایران” نیست!
ایران اصلاً موضوع دعواشون نیست!
آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند
(دشمنی‌شون با اسرائیل هم فقط به خاطر اینه که مورد حمایت آمریکاست، و الا سال‌های اول تأسیس اسرائیل، شیفته اسرائیل بودن، شوروی خیلی زودتر از آمریکا، اسرائیل رو به رسمیت شناخت.)
شاه به درستی به اینها گفته بود: بی‌وطن!
خودشون هم میگن که مبارزه‌شون “جهانیه”!
“انترناسیونالیسم” (که بنی‌صدر میشد، “انترش” ماییم!)
به همین دلیله بهترین دوستان جمهوری اسلامی در جهان یا کمونیست‌های سابق هستن (مثل پوتین و چین و ونزوئلا و…)
یا کمونیست‌های فعلی: کوبا، کره شمالی و …</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYnYqszbotzi9PNQCKTbPSTEXlavYIClFIxfXFFVihHxdEm26TZ3zavglJpGGQKHvOsPsVEqXAKTvyXwhqzN_hO_qLPpNq7Ohb_oJ92h4bu4pCkIZudIiBRwjeNyrWJOLDQeUqbQY00hnfqxi1GvQ1IT244pY-HX2sHCJvO9pxLFAjuYQv5q4KdSTqJCsBcL5Pr-U-k5w1oShBttTgnXJA7uR4zHGLbPpwSEsNddFXC4gaIe7a_FmbZxvZDlZZofaSXNU_bDO32D9BmePevPtSAKNZXF0yHGvmw1vakSFeNdAEBAsxIozzkXwVD8BxapMYppHc69QbWlcJHx-03Dxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=Q3m7o14M5vFqH7WMbEYarYn50c1nsaai0bFHlu_u5LzCcDT5dP7cHMNsoVip__YqKiKjVgtKKlcLWdS1A65EjmZN554F33IqHPFN_lSPYSJiK9Na22Ag0h3u6ZJhW_tRmRf6En-83suQdr9MTCNsA9BeeGFXiI6nIDg4vAAzsr3uWhbnVgXKwMbBpBzVq2bQtevH2bBtqtauQ-ENhM75f-zAAuZtZtRpGkcTji6RAbTSGReW1CtFpq5QwuzzVdbkoUsUr9nbq0crC8Off1LThfPONoZxKbaGdagnuSNZOoQClVIEtMVXuvD1MjaD3ua1E2i2-HrS1w7eK3xetGQoBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=Q3m7o14M5vFqH7WMbEYarYn50c1nsaai0bFHlu_u5LzCcDT5dP7cHMNsoVip__YqKiKjVgtKKlcLWdS1A65EjmZN554F33IqHPFN_lSPYSJiK9Na22Ag0h3u6ZJhW_tRmRf6En-83suQdr9MTCNsA9BeeGFXiI6nIDg4vAAzsr3uWhbnVgXKwMbBpBzVq2bQtevH2bBtqtauQ-ENhM75f-zAAuZtZtRpGkcTji6RAbTSGReW1CtFpq5QwuzzVdbkoUsUr9nbq0crC8Off1LThfPONoZxKbaGdagnuSNZOoQClVIEtMVXuvD1MjaD3ua1E2i2-HrS1w7eK3xetGQoBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=US1h7M92VkKSieuh3fbJeR6J4vKik07aC4X1TsTWEF4T3khrqbcwVHJg1q9PwWaprXer9qLlHt4qrkiUhxNtxfUtO04NXXkG6qtzAsgB8DmxQDyUf8j3N4K0JvTmXFnSrLS7p9hVgf6IpgyFld1l56kWB5iYIYQox8VSSe4qTapiadIc7Ycq6m7rJNov1EzmzOe94m1fZI0Y7bh3fexnqakQ7lXzl7yHbEP_u0hsCTGNTQQvDgCe8yRsF7SKqPE7h8mxQGJEHm6t4WLWg9k2Ezav7PoH99TYnnXV5hPpe_HcKNvGmaRHlq69LU2aXjn_yhErZLpok09SA3oKXpjoNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=US1h7M92VkKSieuh3fbJeR6J4vKik07aC4X1TsTWEF4T3khrqbcwVHJg1q9PwWaprXer9qLlHt4qrkiUhxNtxfUtO04NXXkG6qtzAsgB8DmxQDyUf8j3N4K0JvTmXFnSrLS7p9hVgf6IpgyFld1l56kWB5iYIYQox8VSSe4qTapiadIc7Ycq6m7rJNov1EzmzOe94m1fZI0Y7bh3fexnqakQ7lXzl7yHbEP_u0hsCTGNTQQvDgCe8yRsF7SKqPE7h8mxQGJEHm6t4WLWg9k2Ezav7PoH99TYnnXV5hPpe_HcKNvGmaRHlq69LU2aXjn_yhErZLpok09SA3oKXpjoNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_tdoykv5FdLpwubdeF09bA048Oj2fVBzLE6eAWM-LSAWz187xN9935XyOmZsic2mHUy1p6WRZKXKobEcsO9ZY7y252qDoFsQNsjdE1Npul42Kw293zNIJKarOeiX9eHG2c4fYDvA5dDLal3w6AuJmVqnLqbO6ouDCDIUMfNtRRokq3dB2dN82HUJ2Xox3WU3Kzc6RZEnwjNeCPSo6t5koEvJgcJHmlf1g3OnEc1mwd5BMOtS2lKvLepUSpCwolGHl7I5HETGBNycSZLZ1JPUVrhP_yOpyoQWLjV6Y5CTYx_CsxTR1-0PDEWuPA1oUGILJyb6Uu8ky_7OBK-maPX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
