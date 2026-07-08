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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 19:55:01</div>
<hr>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=PsPYqlvxWn3WNiH_ZG1O3erxgZxRHjSt91ypfNNq9AAYIU0OmOOIPcnWt3kbrQp4Z89aq5gXw1_nZVqhTW8TsTsjBRGn8ttzK2oXcB-BHksY4Af0JfW2LJAXH5SzH-qc1ceylOL60l4biafWTHu6SQmMIYjtbtUzOhthKcehJzXylkhcd7sIPPSPVTheYG61zqdZLe9tloc4gdW2bT6Pb4uOTj0_9QC912mMaq6kg0vItDXhu9Y-pmM7hChpm4PSoTI3zNqRX3VSryiYRxGcOC1aBVOH9kicLCDJnhHiGxmBlE3htlHIQENljTKNOyXSi_JMR_MkyUNMksqEiUoR4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=PsPYqlvxWn3WNiH_ZG1O3erxgZxRHjSt91ypfNNq9AAYIU0OmOOIPcnWt3kbrQp4Z89aq5gXw1_nZVqhTW8TsTsjBRGn8ttzK2oXcB-BHksY4Af0JfW2LJAXH5SzH-qc1ceylOL60l4biafWTHu6SQmMIYjtbtUzOhthKcehJzXylkhcd7sIPPSPVTheYG61zqdZLe9tloc4gdW2bT6Pb4uOTj0_9QC912mMaq6kg0vItDXhu9Y-pmM7hChpm4PSoTI3zNqRX3VSryiYRxGcOC1aBVOH9kicLCDJnhHiGxmBlE3htlHIQENljTKNOyXSi_JMR_MkyUNMksqEiUoR4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdUfZQkUbZn4PdoxFTVxLLC1_uh0pk_Svk5640gLN8azH07lx77hJEtleV78CRvp6Z_JKpk1-_8KmjB9UTsUSLYeoWcpCE5957aqSyJMQ_5BIqDmp-TH0m7ZDyf-FrXDdMCUqeIy2m3c-VmwCzD_GNxilrk1N9IF9d71qsK81cGd-WyPe0LehJS9HHy2h9vLs9Fjl8n88UE1EwFXrG3ONQkjmhXvPpZ9zoYiM7cynGUk5udht09N7zSMOMtnXavVqK5S6Dh_15r7eA7W9ZrkkdZ7eSfmgYwRD-IWBI4zZdX7GyzYebxleNPkr72Cx3_TmJCjbEjuip8uzyiy2xlHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=UM-4jBsmM2fSPhhatd6bMlVbQu4DH39d-uUUvsrbWXmPL1j8yncc3jOQDYeGue1N87B2hEiHhyL4oM3rWKpx-CgWwAlxzKywwK5Z_1be9mC3wCeU7nbbIN5vKVoc9DZkXrAtmCFWxMAjHe8AJQ_Fu6CyzcOEJgLpd0o_dwVYAhs_Z_Q7GT7fU3QAuReRn2V3pxRf1R8BLAvF183QLkyWPd1LrL-2qNHcAQpoH6o7HO2Wb9xp_qhkcb-h9TlM9bjj-Fvy7_Oh9VM2cTRZdJf51Y2Z1RoNHLdo2KX09BT1U77iW8SmwwoRqP7EMDSCSeXpgi_5lSN8ceiT2mEQXrtsmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=UM-4jBsmM2fSPhhatd6bMlVbQu4DH39d-uUUvsrbWXmPL1j8yncc3jOQDYeGue1N87B2hEiHhyL4oM3rWKpx-CgWwAlxzKywwK5Z_1be9mC3wCeU7nbbIN5vKVoc9DZkXrAtmCFWxMAjHe8AJQ_Fu6CyzcOEJgLpd0o_dwVYAhs_Z_Q7GT7fU3QAuReRn2V3pxRf1R8BLAvF183QLkyWPd1LrL-2qNHcAQpoH6o7HO2Wb9xp_qhkcb-h9TlM9bjj-Fvy7_Oh9VM2cTRZdJf51Y2Z1RoNHLdo2KX09BT1U77iW8SmwwoRqP7EMDSCSeXpgi_5lSN8ceiT2mEQXrtsmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=UOC4u3SGDeIPTJ-MzM5_IDOjqkVIdeQ3Oc7A6uIAkmrPuvtwZ0_QJGbYJa7HGGBjDTCR7DJyWt8ZdMBBYQ6D7gsm81q7aVMSHRQfWE0GTUQunRqIBulQrSp8NsBTLYSSpiHZFNJ5zpFrZsgqwW2C3rRyg5TDVT1EDb85KQGuBbeyf-_8cXNfGvyruxEomCRSt778bVBGrT26G4la6CKTNU7sG2d-1t7x5IjdYen9rLArwh4LOwT52tnn9R5J6XnQdXtiHlM9nIpSThFXieN2MbFVV7mLZqoxTBWGakFrFvWn-tND_oGZceWsn3qEs7c-IQe_ND61wslWqTBP7gEk8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=UOC4u3SGDeIPTJ-MzM5_IDOjqkVIdeQ3Oc7A6uIAkmrPuvtwZ0_QJGbYJa7HGGBjDTCR7DJyWt8ZdMBBYQ6D7gsm81q7aVMSHRQfWE0GTUQunRqIBulQrSp8NsBTLYSSpiHZFNJ5zpFrZsgqwW2C3rRyg5TDVT1EDb85KQGuBbeyf-_8cXNfGvyruxEomCRSt778bVBGrT26G4la6CKTNU7sG2d-1t7x5IjdYen9rLArwh4LOwT52tnn9R5J6XnQdXtiHlM9nIpSThFXieN2MbFVV7mLZqoxTBWGakFrFvWn-tND_oGZceWsn3qEs7c-IQe_ND61wslWqTBP7gEk8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=sIUCHYlduPx_HM4WvFX7f39c4BBRRln8kcipfwvCUJbe8HiGZ7vFsOs4ndas1ld7T1kgxs8lDmStQgFNYhsHwIN2aIxtxs4HEHq17V-gIMSWP6_oDxpLMhaV_qPGX9gxEEJjWTLWRE1CZFCIhRbnOS6dhbpmRXuGZp2N6dfExWgg4L9pjwoCQYkPabQlknjKTUtuB0nfgi3woWZgV6EUgH_JuJJrf208to4CSzyB2gU0Lvyoy_1scQUuuDd3ANlm709eF6xrwtImlEIb6D5ngSM9fQW3dQJ8TRso1LzSdYIoXQ8oUiORlzJo1P0Wn1rbD_3aEjTViE1VUcInC5Qc3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=sIUCHYlduPx_HM4WvFX7f39c4BBRRln8kcipfwvCUJbe8HiGZ7vFsOs4ndas1ld7T1kgxs8lDmStQgFNYhsHwIN2aIxtxs4HEHq17V-gIMSWP6_oDxpLMhaV_qPGX9gxEEJjWTLWRE1CZFCIhRbnOS6dhbpmRXuGZp2N6dfExWgg4L9pjwoCQYkPabQlknjKTUtuB0nfgi3woWZgV6EUgH_JuJJrf208to4CSzyB2gU0Lvyoy_1scQUuuDd3ANlm709eF6xrwtImlEIb6D5ngSM9fQW3dQJ8TRso1LzSdYIoXQ8oUiORlzJo1P0Wn1rbD_3aEjTViE1VUcInC5Qc3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هزاران نفر که اومده بودن توی خیابون‌ها رو کشتن!
صدها نفر رو اعدام کردن، هزاران نفر رو زندانی کردن. اومدن با وقاحت میگن ما اومدیم توی خیابون! طعنه هم میزنن!
شماها با وعده امنیت کامل رفتید
با پذیرایی و امکانات. حتی خیابون رو تخریب کردن برای تجمع‌تون، کولر گذاشتن براتون!
خود گدا گشنه صفت‌تون رو با جوانان شجاع ایرانی که جون شون رو گذاشتن دستشون
یکی می‌کنید؟؟ طعنه هم میزنید!
شما هنوز نه این یکی رو خاک کردید!!
نه اون یکی رو می‌دونید زنده است یا مرده!!
هست یا نیست! توی چند سوراخ قایم شده!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Am6u4Rrgu8xe47049HkbEe2GoLeGK-hOZx1km_XKP_cO5A_miICtDx6qpu8fTBH8KRnTnQu8UfsRbhd25HZTKsKBFMIA-CblIRkYcYhypdXrIDISH-w1l5s9QY563aUY4DThQUI2O1Dchy6cAVnvWz7rHw5CLFc34suckFckq1NkwD7U1y_E143cZCr5H-b-7TJxQksbK78-PiXS2vykxRns5SzXys-oSm9lPZFjXd_nH6oLKvyvcR89r3SjU04-M4-nqwYVCwwt-JOgqMHlJ5EPQ74vwNSdr-fYCXW6ztPtm1FQoYt3Vz-7cAhbq9GQnC7ZrdMeSGdcF6SyIY-eSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : «آتش بس با جمهوری اسلامی پایان یافت. مقام‌های جمهوری اسلامی شرور، بیمار و فریبکار هستند.
آنها مشتی آشغال هستند.
به آنها یک هفته فرصت دادیم برای مراسم خاکسپاری، ولی در عوض دیروز به ۳ کشتی  حمله کردند.
آمریکا زیاد از حد وقت خود را با اینها تلف کرده است. اینها شبیه به یک غده سرطانی هستند. غده سرطانی را باید سریعا جراحی کرد و دور انداخت. »</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7ovzrxVJ-I8dU0bHTsxaUMHAD9037YNq27Or5C6n6uHtLKXZA4tOfZOFO6RVEJYiKlh26CFYqkUf386ktr3AkL8mFXwCAwk31gZJHYl1hIUchBwk_mp6pbLnFfsQGHLXQxkVyIxQNGoRNJQTAQaeMVAp4_XLd2_KjsYWAAV635Fy3Xwsvq85AsoKMib1VxzOJ7QxQSvO-krfSpZbi9Av6321v_a6qyuq9UpEjQ0JpKXWxHzjjsdu2FSc_2sei0gVqQp5iUm3d-hEmmA5RoB8r0Wu9uiNMog_8NrotCtEyqGT4yjx164VMZtPhp--x5P0CMSZi9FnISzm37ofUkLEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-T3JbhS1OaSDLTuHP8ma-AYCeP5Fc9-eyx5cUpw9lrSV_DI_6R0u9h3QUKZKrnXmrbg3R0kHxW0c4rkfk7Vcr2E9TbO3ji1JyFOxJKnZEf3ag-MFJHYnNN8-Jb8mBWi2R6aCLI-E-EaFtE-Iv7JJrZb8t8zr3TnO10SoSD9IaDJz2KDOS33ZnZuShj45EbVFX9sXFiE_mEwOepM4km7XYt0xMBk5Im4FBJMxe86fKcVS8XsnOqYhtCCY68Ve6MtdfR9sQmX1W9jxMTAoOniybraXSauOMZFN5pw5SzhmQ_hpc9FvIdRBTya4uo8BSfTrJ61UX5UPAaxekq9dtZBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Rn_8WCUJbJutyPrrsbMZMeVklr871nCBWKrfT0m9f_uqL8UzQqnbVchV9RocoskvFLnM1rzw4iiNr0iISQPQR9vyPozccctXPIFjwtTBjK63QOoM0xPtuCCyWD7wMVHUZJen9tEGNBIqI5P4WKregQ06eb_O08JDarZZvevzknG8qaIZacMCgnxUytnh63z2c1e43687SiVbEblFIgNPsECUmc0QIPVUjmzLrPyV3VklTcdOIoyzEdiyPpzP_H-WCr_ob5AgrmEJxeZLp4Nxu6hP3pQWEyUH1XnuOMe_pJ6KaMwmc7a7UF-0SKvjokXa1aR1-T6SzIg0VfeBmUEEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Rn_8WCUJbJutyPrrsbMZMeVklr871nCBWKrfT0m9f_uqL8UzQqnbVchV9RocoskvFLnM1rzw4iiNr0iISQPQR9vyPozccctXPIFjwtTBjK63QOoM0xPtuCCyWD7wMVHUZJen9tEGNBIqI5P4WKregQ06eb_O08JDarZZvevzknG8qaIZacMCgnxUytnh63z2c1e43687SiVbEblFIgNPsECUmc0QIPVUjmzLrPyV3VklTcdOIoyzEdiyPpzP_H-WCr_ob5AgrmEJxeZLp4Nxu6hP3pQWEyUH1XnuOMe_pJ6KaMwmc7a7UF-0SKvjokXa1aR1-T6SzIg0VfeBmUEEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBKg-ty4IaIv55E92wHPrT0spbDqZHW6T-RHCr90Wgi75r8AOqLn4g8pa1ATiCDH-fd1K4j4cNX7vF-cyGm03IoAML0W9XwfBA-jb-l4ZTnCuZoFTxR9FgjI_ju-QfWtCcOx6FFSoPkgh0YSEnwQdtgeyEPL5eLZiSins-VnZ7FUj_snZxCScw80JQbewK9N17-Fsc_dFFyV7ZairGE4t4zOkEbuFqrcZJS5UeOp5BY2bZwM68S1IUxd_9OnoYiAuwstts-VKanRrLs2W8-1z6uG6I4ta_ZaC3T0JMCdRirqh6ig8JuyZo7y-3y5zrB6ynpCsnmrnnAkqKnV0dO5lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=TOf9vi73uQoTX-E3TAgt0KYxfBX2uwopboROUvR9lW-5h8zAU2oYOJAJ5GOAC4MFAYiODtEapqBEBop1t_xzIvQzfxN2x4Eiiis_Qz_-zxEJScWsbIJDAFEaVV_TbuWD_3nHeLUWSPbVKh6dUMFMmTN4aAb9vnFqSXAAAtMe7pbzuRvyr4HCl6XPVnV51ntxI04q364p0RoL19HzFNVhcDz6oohLK8aGBvs8jw0CFPa-hEKHj_orKah98Upj5i0EpRI7mkMG_2ZjL18Ba-WnrBgq29rynMmEsVq1j630b1ZhD5mX7hLrKqsKogTucMrJluaKM1pEvmQ4gX_eB_qlJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=TOf9vi73uQoTX-E3TAgt0KYxfBX2uwopboROUvR9lW-5h8zAU2oYOJAJ5GOAC4MFAYiODtEapqBEBop1t_xzIvQzfxN2x4Eiiis_Qz_-zxEJScWsbIJDAFEaVV_TbuWD_3nHeLUWSPbVKh6dUMFMmTN4aAb9vnFqSXAAAtMe7pbzuRvyr4HCl6XPVnV51ntxI04q364p0RoL19HzFNVhcDz6oohLK8aGBvs8jw0CFPa-hEKHj_orKah98Upj5i0EpRI7mkMG_2ZjL18Ba-WnrBgq29rynMmEsVq1j630b1ZhD5mX7hLrKqsKogTucMrJluaKM1pEvmQ4gX_eB_qlJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dl5147v52zgq7V-6SvRLDZOwhgAsF-M6ySej97lSthrUIuIMITEsenXrnUsvug4X-uU_ceN4hAWeSKFqybrWm90aypvb3jaYTHX4N6S7kA-NbktMwPEsrNuuWkTobwIfUuIxFuDMJL8fI1XlzGPfgqdYtiwmCVde2lTmKw_HPMNHGV3iUOKzf2g4ZyXzQktwGfouy3nwWm114BQYCuplc_-Fs-0BCvfdVhg6_H_UQx4mr-u8qQODHQWNcBX4EaHg6t0IP0ZPcHCNUFr-dy4TtFrXKHW50BfPX20sDB17fVaXaN3ORQdShuC2LfTe8XHGxDenjSfT6Ot6htm43uVvzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IboFU3QfYgGpXcSioiEW_DhlVM9x8mHY86IVdqEWempAJvB08Rbj9ncMe0fRklbWynUO4gfJfAvcmZabCb3LzLboIzGNRsLZqXtN5SdewlnAGtFd7YkqIgXW7Wr88YBWCX1Amy3uMBUwmSguVfVOsg0yjmnwiTu2unaK0ZNzllxOSIs1VtnYG33DZiomvOU9R5YsaU31lkhn94joaJB-GAoFtp359_92KNN6IRjtNnpPRYEtFik2Y84BImNO24dhoWaVjqcJS4TEpXTuIc-pAVOPS7MxRo_ibOBUOZBKryxbrjziK3Qj8lFuJBEPkpCxGqmmk-U7UQSyNGYUnFyfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=n-eJvZoAt_mchqF3o78aNLM4ilFHPYJWGRgeVSkGHOm__EMAp2T_bEQdWjTAsJE6xCalc3rlyTsZydhNkvkG13wnlzw3MVYj571XoibQq3OAD8O4Lu_axL0PHCKw8h8laOVBuFtACGkRVQqmCh_TJDMkFtxrUqfpi94dVTbyQXnbnic-zCg5GQrd8xAFU_Kuek_8dEzeR_i0sX-SzDlzs4iM6KSCWry8wi-JwUQ7SZGB3SOVtRHEHrXTOlSirM66vhqcEXXwaI5tRwmiu7XOhG06MRIfGst8sMd_RgXnvQwHmql6duU8M37A6SZViJ6W9pGv60qOLDal5ZeQq-pz2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=n-eJvZoAt_mchqF3o78aNLM4ilFHPYJWGRgeVSkGHOm__EMAp2T_bEQdWjTAsJE6xCalc3rlyTsZydhNkvkG13wnlzw3MVYj571XoibQq3OAD8O4Lu_axL0PHCKw8h8laOVBuFtACGkRVQqmCh_TJDMkFtxrUqfpi94dVTbyQXnbnic-zCg5GQrd8xAFU_Kuek_8dEzeR_i0sX-SzDlzs4iM6KSCWry8wi-JwUQ7SZGB3SOVtRHEHrXTOlSirM66vhqcEXXwaI5tRwmiu7XOhG06MRIfGst8sMd_RgXnvQwHmql6duU8M37A6SZViJ6W9pGv60qOLDal5ZeQq-pz2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xy3paN4MfD7MXSM5YFmE87SdGjtE0WySZ3LjIQD5-SwZVjqdc7Twk3aYJug3qWQCGqVU3WGthzfClOGSMUejOfBTPdB8J6rx1OvUJh8iDhWgptDtDzbJ-nb6uH4rxCdizaXFnLVGjQ_WqJNCQIjArPLahXh_nbnUWR3njhUokylsVNPbssUn35LNqSPyCB8J8HBSb3H-zl7cgZJiNkndip2mN6HkOhVxi4iK-U1AF9FJ2FKscaUoMZJfmc9OQBFZEPvYlkvrOImezpNXhGD_tWKlBHz_jw_TisqGd6eArHS8do9klASHwKQ1y1HjCssC5jFkbZb7rYlDr2_UbK52yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szD7uxwnFwF8BGvA5XCXlE5lKUe5OcRSQAwGIqDLzquW5lnX-D6bB4MaeiUqPtQ9igEDcK3EwdvUUSDpYU8WcgUuxyweio188UnMznoySed1c4QYtAN08YZ5Nb3FcutxL5MnjAcypY7ggghn_4gYfPN5BtX-GqSONwvxPy724FIbNwMKgzBaTs2N4-cohqXp8OkKT2VRmILsqn9mNWB6IGJBXLq4DmXxuJJUxAukpxpcX5hcezfIMZTjfePx8ApFSCpZNik1WVryyQ-pofhnmcfqzoe8vLY4OLmMnrcBf5lHCLPldOMLNH7r13_ZtiZdKOCeykUppKD_ls-TG31Lcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlBxJ4j_tfvhhMZzBzZm9efOJAPGdFOjbclmsx-nR0DiZ99fNVc8n2gOc6oXgXsErySER7W_HisaxeYfZYT2ipKCFPZDC0aTEWHC5_ySrOznlow-VKoTONPgJEIASaSuVZNDoGLOikVsbPz1tCUePDycwz6IY9SLqQCUTm7sJqtUlTOJTX28nKVJa7cppe35PKUnTRzPlUkjH24JOBijyYqh-i2PU9mT6ggBHSoAcq_LN2PWFCYQLEsUV9lMpdXCU6JNDd3VTt1HJNC44fZDeK0zKwDzaaJh0vE6pTsEP1jdkfC8kR1-GrCog60XjnwUojUwK8G_CQuR99-4_ajQ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jj81M9SJJ7DWS5ESy0gDmvGC1i2QzZqcTyTKWGCA4Boax2uABAqgcr8-Nxk260OuRiQnzF05JZ_3_6FM8s9yrQvBAkBLFeEws3v0b2UO5RxwDMegeDoHA5il7cCA8VJLqXDAakjso9XbAfhcZO2RdJ1kVmaxqZ2nq1qkZitA5dZuhxYEn3Gt3mtwuHMsPfLPvY-YofYBIV6fd7rzr3BLNhTldtTocFZ1SoEQNxBWU7eRcffDGjV7FIidjc5Vwbaw6_vHtfAqbu-qs6-9W-I8-kK_L3UogUsN9PU-MZjjfxyrBwxpNHugp4I-WJXiAr5MuL5IcJk_XRoEknKUFxKbRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QEc8VmlgImpX3OTfgB3sK-GnTj_sCjiRiTkQHMoe5byjQi_oC55uVMfO3R37O8Fez__Jya9H9kx92eTnN-l3rzL2LJIkt3fcXSFbebc_ngmI0UAW03ZXBa0PRUF-7OJg5S-3XbopmIbPJ604UZL24eSUmeQqSKsHsbFR998q8a0CNff__ZgApOIHWFn0xk-jrE1zKH4NUdxGpO-81hRi5fek0yhXsmYij105tYBUFPiDqW3J42taYFUHSmOGrjebEiugyjXUlf77Zu-JcktTDw4itSh8M8-ZOqBuS9nnVpWEkku_Pct-458YPavqOAsF9xQfELMAGSc0_wXrEERA6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJVpJ-nXDeW0kVoNVo1JF5WKLG31ylW6PsUAE9VJaWDHPIcbK3fuDetuyzU9q3g4x5BjlQ1LQxWByKebyqXJlp8Apwhwy7oK-sXHOQFxjYWByTzJMWzO_mwsYmNIrZyNAxEPIJd1PczaIotA_mRdXPYSke8jcTDdl2DyX3VL0i0xC-3zQ5UTcTJqafr8WMtOC2MntugBhfLI-5J15EtRoY-34rgWTvEjvV_jcd4snwG6mijdbYGxGsE0bMQ48BEmmZ0e1I4RNpjFU59ezXuQi8TMAVr53gvKaVEq56gCLBNtCOY6hS6fbhNQHwylYQu9P6308w1WWTvL2HQy_A3K9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=qfLb9J76t80Ca_g30D2m-bm5RKfq4dJ4nySvb5nmqazr611Ww27fMu6X-DAT9eCITqdCOlPWFOsLV8fO8eJTsCk-A7lHPZWmuox6tUTR-IcPCc-d2y7Skl9ynmZ4Wfcdxjh1y-08BLmnt_UdQOMuln1WXZU-bJH2tIO-y1RTfqUZFuW03cXoU87OiBNPUl1S0fpHjyGTs0BkwTezMMYMDHAVVh4BMurP3ZJrca7jKyLY0AFqYbikbFSlRxyaPCx6o-O6EbeM95Wf7KRXIKAzXK-dGNexvUuN7KdYefgXLt-4Z4MaOKOb0U2hVMDvFS78X6xF2EmIU45Ef_Y6YmpOSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=qfLb9J76t80Ca_g30D2m-bm5RKfq4dJ4nySvb5nmqazr611Ww27fMu6X-DAT9eCITqdCOlPWFOsLV8fO8eJTsCk-A7lHPZWmuox6tUTR-IcPCc-d2y7Skl9ynmZ4Wfcdxjh1y-08BLmnt_UdQOMuln1WXZU-bJH2tIO-y1RTfqUZFuW03cXoU87OiBNPUl1S0fpHjyGTs0BkwTezMMYMDHAVVh4BMurP3ZJrca7jKyLY0AFqYbikbFSlRxyaPCx6o-O6EbeM95Wf7KRXIKAzXK-dGNexvUuN7KdYefgXLt-4Z4MaOKOb0U2hVMDvFS78X6xF2EmIU45Ef_Y6YmpOSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbihdM7fzCb-Vf9y_56g4kcRID-J-Vrv0o1DcEZA07svXlsh7iDGqwf53C63v9qmgDA0B0BAmRO6eu368PVt8i9zmcGX1n9j8C0CV396S8nhXC8GGrjWMFVB7L5Iluc2y80pO78XHMYD5guUfAz2Fl648uHTInXo1fvgvjM8SCudoI5CmZy-lqGodOOfkFitpXuPbxxFX7ZNqu2sgTxjvTtB8j4FTmyea7nHqmpw_mb64mw2BLvDeW-byLQ3dazvENkq4VNuVBIrdjJzPAXUOHtecU7cvU2xMLAUU1jJKLO0s29Mv6uwD7qFK6KkQBtvM3DD7iNpjiaFYhxHuBf5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=tk_Gv4rdA8GPBhTry4Q6WcI8xZsKdbH9K7ULdqCIDjJMX3uOP4AYZbXkWEcRHvQ8DWh72KApGr8cbF9_g9whJ0qbsvDg6R0qVMbH5mx_UQ5a2YBeUZ8xwTDAzOTyQzGQffoq3-813aKfGhwUx1Wqsn38W9FsX1pRdD7OdHVgA8k5FZBUPewceMWmMqYOtMZ9jBca5ERMTSOLXXyzGUTr0wknUcgGckkIud6tJsh6X2NcPiGwOnXnex8AOmwVsMQKYPgi-oG9HvmS-rhfHfmoy38_7UCUd3-xRsUydsyRBAZh0bPzrkiF67R0opSIOMsPqBH_Fbx5ZCiOYwSWOmiilg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=tk_Gv4rdA8GPBhTry4Q6WcI8xZsKdbH9K7ULdqCIDjJMX3uOP4AYZbXkWEcRHvQ8DWh72KApGr8cbF9_g9whJ0qbsvDg6R0qVMbH5mx_UQ5a2YBeUZ8xwTDAzOTyQzGQffoq3-813aKfGhwUx1Wqsn38W9FsX1pRdD7OdHVgA8k5FZBUPewceMWmMqYOtMZ9jBca5ERMTSOLXXyzGUTr0wknUcgGckkIud6tJsh6X2NcPiGwOnXnex8AOmwVsMQKYPgi-oG9HvmS-rhfHfmoy38_7UCUd3-xRsUydsyRBAZh0bPzrkiF67R0opSIOMsPqBH_Fbx5ZCiOYwSWOmiilg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=MseYgFp9DynGfSXkiMCH51N5JM-_Ilc-7tHnUgf4mbCHl28TYQoERwW2-ejP9WGVFyh1U-ugjtn_ymLB4X0rR4OJvCURi7541ufEEV52mpHDnjtPM-noQX4WgpAzmET97e4_SzyXjGKwUOGESHqPTw__izuSoi3-m0_sV56GL0_Tg9npNOwTqeWcSj4_rDg1i89NovWF2-LM-hSMNgWylzYcC6YHNrugRM8EUyNYkd9TR5mwkzp7J0_d39dVVQFVC57AQIvvvL6hT7i4LnW2-S04P5gaN5ZAJ_VlHn5wzp6Iwhk_LcbdcJO9KypsmdAvae8L4HMlbgamW1r6dbB1GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=MseYgFp9DynGfSXkiMCH51N5JM-_Ilc-7tHnUgf4mbCHl28TYQoERwW2-ejP9WGVFyh1U-ugjtn_ymLB4X0rR4OJvCURi7541ufEEV52mpHDnjtPM-noQX4WgpAzmET97e4_SzyXjGKwUOGESHqPTw__izuSoi3-m0_sV56GL0_Tg9npNOwTqeWcSj4_rDg1i89NovWF2-LM-hSMNgWylzYcC6YHNrugRM8EUyNYkd9TR5mwkzp7J0_d39dVVQFVC57AQIvvvL6hT7i4LnW2-S04P5gaN5ZAJ_VlHn5wzp6Iwhk_LcbdcJO9KypsmdAvae8L4HMlbgamW1r6dbB1GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2Eb4uY_85H5qXFm3ou5gjw_eoqtz2nmwaAhgYcJ254y1XtTFP7Y1o1MRe8rWDT8Ce4Ljux4srYNBrT8M91YQVZd8Dc00SWJN0aWtO6K95o-CXc1A6XwJjkzhRsuICITdj-8VnvQ49dQsZS1uArm2eVLuSqoFo0xSlHOMfO2fj2OIzTITqroji8JvHaFwZVV7kfk6Tn6JpcWRmAcwS0VoqM4beNVWjlNGp5kKW5tpKf-nTykO5g69GhbToN8WD8QMOfeuEdB4eIt7WSjSKJSFbtXMoh1O-4mSV_mFz1Fl5ryZ982v9Yryg-21nKldEpR3G1jKp9l1jt5gcVN2gqcsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=JSY44-wQz82BXyGU2HW4n-TQfPGYqYR2rmIuzlAKoR_TARrTWm1h2jqxr7kNm09ZQyGjAxfBE6nZveiQMYXcuxkC1nTZbh2eUZCfbuis1k35lYwICkC87MteeWU0vT8GX98jz-fHOXxbwlMxF9JeI66hnNogFb21FKlPkGVN5G5TZKsv3T4lmk1dnFNW7nW7Oq5lnbLsKkGG0JlLv2LdHaYpFLj7YPKoqN8xaeEs7WDaxOUtbP1mVqldt9PUMiqZJIUyCLvVpfeHxCNrmG34M1Tf1RtDyCxidqy_3RDxfLIhK4oQbSBl3sWpDe3By20W7axydCMCjHAHL3BpNCNF_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=JSY44-wQz82BXyGU2HW4n-TQfPGYqYR2rmIuzlAKoR_TARrTWm1h2jqxr7kNm09ZQyGjAxfBE6nZveiQMYXcuxkC1nTZbh2eUZCfbuis1k35lYwICkC87MteeWU0vT8GX98jz-fHOXxbwlMxF9JeI66hnNogFb21FKlPkGVN5G5TZKsv3T4lmk1dnFNW7nW7Oq5lnbLsKkGG0JlLv2LdHaYpFLj7YPKoqN8xaeEs7WDaxOUtbP1mVqldt9PUMiqZJIUyCLvVpfeHxCNrmG34M1Tf1RtDyCxidqy_3RDxfLIhK4oQbSBl3sWpDe3By20W7axydCMCjHAHL3BpNCNF_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG-HHdnLxcaNwOOwY-qyoBWfAMSCdUFJxwE3wur6TIjPljxZYqdD-2zfxZ3wom799eN8ELOA8Zs6MOyY4qz9utVkBVJ5HXK-qrITAVhT5d_ZBSEQQRrJGwyAelH-KO8HubH36Rm2-NFHq4BQMGZPnt9MaItab110i5Ex37J9hgHBlz3wyS3fu9scyqZzPZodslZ4qmLsNH5GQAAF5I6tCZPnz688jsdL4Yfd_9myFNuJ66yjd794uPKaSaHXjVpaViXNZUVjtzIlRhfyzHHvbonIVlYi9yxT3zhBmfWlNO4UiOHZorTOn5t2ZkLS166RHYv0QyNWbzpOPQrTFI61sA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pETy4ZwXB02S-SzKO1zxR_1eXNOq95slxtcEBCUKqGtXDbhlvhS7uETX7o211MePMenGi59jfvuTf__tgerpbAv-bwrPVI-moOaUXPQGDj6D_QGqiRsb4IXGiaW-xx-cLhgSoPdPMTkXzZpoe0hWgc7d1lR-quWslTtMIxjc6GWf3yvaR-wxOSup89Bx_h_jn30vOGWBav0-gAxpZQrDMalegmxAZCYF8GSV8X9LKVt7-XSV10NIWfOJwEX4n_G2XO5Qepn2RbxjQF__nHW7lecniyOBgMnPh5gcH2MwYJX00xv9H_MG-Pp1uNDnASNdCNjwNhI68Rz5K3pJTli3DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acYd0eq0rMCo5vhWYPL44aolWJ5AVgGrVbLtRVLrHJ03N2NfzD6H2461GlbC4X4pvHk9LhB3wrgrqRf-oRxqzNamRX4knybaiNzZWATx2P69DNiOBkxnKn2NVXYOZejZJhwkzo-7d1WdvztzlRpFjQMFXgVnCDPNV-xYENB7X6OOV_2o827yKUqUe4FbSz7QjEYyLKL4o-_xkyDiVb5cVDLtTMx8dR4G2X5dh4Yd0af87sgB23lFAeU7PBNh8_Bi1E9FOJAKaOviJkrKMP12rl_C9HWo8OxSoUzo04nYs5WfhEf26q6HNe80akk-QPFWJRRR5uTcskah6BnJk3FXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcoA-ZfufKJQQPfTsHcgYowgE4-ziAcaWeatUqQCJenfjkvoLjQCp6F7aGplh58ESS_iVlarjmuk-MWFEmIknjiLWcz9HQBv1FEgaBx1MwgswL0pQZ4BnU64nrad7tQO_Wk3z56nEuFWylBmGl_kd1H-XHQyfNoHrVkbC9A1-iUAMQioOhRRO_PMoFaPENZ7FLhaP08YRYCIZ9D9FhFT2xZ9Rh1Ko5-hEaOEjXu8qPo6z9nADZ55H2AhEloU_7Ovu-ZVN5PxSfRPLOmUYkJO5UWcSKR0ya7-PASfC5rr1MJGEqH-f1RNqTSKV7U4fvfXFCkpt8XrW_bYIkN9qEWOHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEKJwjmOFYGC3PqIa8eFS54lwY89Xtqs0c-JTAMM9q5ElxJXNSSXvyL1BjE9PFj7_fhu9zCFQHlJahm5W7-wII9-RrBls7Xgv7ujgZoSY-aGpsuQvBXqKsiiDx-rNc8CXmLSbstmz9uMKJBH2di7_DSfo1WSPQ1rItnrrpVdpF5yeJTunoc_PPOLHLSz5_myhT39zuFVMh8u5Rn-aXfxxw8yDxG3u5v_DC2wKwqp3YNBYn2fL_0KUx3lxnd00OqBDNdR7gwE7hVcZag_9MGqQKo81EJ2__xWdnP3e_LBIt4RDIhFdIMu0F_P2VqR1_z-oJDezYcqviH3oCLLyP4uEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmgwBuXnucUVMrQuZgVd8u4bailRBIZwfjyzeN6nv3AYayiuRgYko1lIf9turAimMw_wHELF_v8JWqHb9cknaaDME7Jwh2LHBW7Ancrxaa4Q2Ow7yNkWit2r2UF0G12IqtGyGFU9Wv8wQSWd6kCPwT_yOU_C7hmOcUdWdoJpdrISxPLqACJ0zLMfrkyaudHW6io9HkAZTA3S1MYz0r5skBWMmyX74XRxl5v5WzY7zPkBZCNaBZS-BurfgeP8xONN60rIsn_mplUL-kcGeXluVusGTq2OsEA2_Ur87d-9EZ9jRTFrbvSG2IR9oAFv9VeDdq3dG9i_u8Si4hxaesw9Fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=ceqXAooSh1QaZbjkELsleW_Nmhpq0YwoVmS9AW44a8WiQFnMnRNM-4iLQQHDPhetgEKLhkk0AguKImbZcqo2mjkVGpw0AGGNvFr69R2Q178LBhePRtAZSSKVvMYOtPl2WPHHuJrrU6cS-X5XP-11BrvjvVE2xaNQjxFoXsrzOU5RAs76SGBDnlRcgqRMNk211NODZHerph9W_BXq8NEwn-THni4bl-y-1AoeNV-tJenI1iUocaL7g8xZxu1W3xooY-f8SBSfMPyartuuBrrVoBh7WZvKjpNfl3GgMx-1pb1UyMk_ZHHA_LC_bujQEGk9ThiTMqJc4c1D-LZwEIz3rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=ceqXAooSh1QaZbjkELsleW_Nmhpq0YwoVmS9AW44a8WiQFnMnRNM-4iLQQHDPhetgEKLhkk0AguKImbZcqo2mjkVGpw0AGGNvFr69R2Q178LBhePRtAZSSKVvMYOtPl2WPHHuJrrU6cS-X5XP-11BrvjvVE2xaNQjxFoXsrzOU5RAs76SGBDnlRcgqRMNk211NODZHerph9W_BXq8NEwn-THni4bl-y-1AoeNV-tJenI1iUocaL7g8xZxu1W3xooY-f8SBSfMPyartuuBrrVoBh7WZvKjpNfl3GgMx-1pb1UyMk_ZHHA_LC_bujQEGk9ThiTMqJc4c1D-LZwEIz3rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=TE9qSF-VT6d6wzwYZpgWpjVe-v7RXthkPdy00WAPt_iHojd_B4_ece_9cnabj9sPYNZXQb1D2ok59kHytUQCO0Hn1xalGwlURUe3fYBictGaULRXskYsfv6EEmvVNSf70ClxsfcpH9HlAnPwE4CK7DCTFZpjs54BvHY5jGA9VzoD0ui7RMi1ile1EUematUG_zuqQoRFAI62zkuOnRogHj7nlXlLgposLU6gaOcJL89OgUcRMy8c3IK9b5O4-udUeJ9wBZE3tmmjAzvGB--1qjGrTGeIwpJc566hGFF55WKaiZsvIZacaldv4zpF0iyvAjpRoY_JjEkkgj7lzsPD3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=TE9qSF-VT6d6wzwYZpgWpjVe-v7RXthkPdy00WAPt_iHojd_B4_ece_9cnabj9sPYNZXQb1D2ok59kHytUQCO0Hn1xalGwlURUe3fYBictGaULRXskYsfv6EEmvVNSf70ClxsfcpH9HlAnPwE4CK7DCTFZpjs54BvHY5jGA9VzoD0ui7RMi1ile1EUematUG_zuqQoRFAI62zkuOnRogHj7nlXlLgposLU6gaOcJL89OgUcRMy8c3IK9b5O4-udUeJ9wBZE3tmmjAzvGB--1qjGrTGeIwpJc566hGFF55WKaiZsvIZacaldv4zpF0iyvAjpRoY_JjEkkgj7lzsPD3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=TnTtNdvi7AhGzstIAr28xh8JEjdqjaGRxl-z0Os5Mo9PTGGXFAVV5WNC7AOLJhmkBGHj5VfNXDa9JH0ihEJ69RIQRAcaYydSIw5818RK-JUyss50ydhtK51YQcDULosfSzA5zUjCm0P50Mw0Hqe6oX4rgV_pHfh6NHYHXg10Jbrpd4nK_tmbuRZBnsdn_j_nKLV96NL-RcX1oi4aLW0t5HV9_5_9KHwmEm0fSgWFku434JlJrnFwA9RUyd8AZ0n2U3XX-xI_mMSSXSou8Tu10_hxBzpxldsYRS1eW8D4NHvcv2ZDS_F4aPyUBqF4h6hHuGSBtMx5_LLIvsYLJPUPFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=TnTtNdvi7AhGzstIAr28xh8JEjdqjaGRxl-z0Os5Mo9PTGGXFAVV5WNC7AOLJhmkBGHj5VfNXDa9JH0ihEJ69RIQRAcaYydSIw5818RK-JUyss50ydhtK51YQcDULosfSzA5zUjCm0P50Mw0Hqe6oX4rgV_pHfh6NHYHXg10Jbrpd4nK_tmbuRZBnsdn_j_nKLV96NL-RcX1oi4aLW0t5HV9_5_9KHwmEm0fSgWFku434JlJrnFwA9RUyd8AZ0n2U3XX-xI_mMSSXSou8Tu10_hxBzpxldsYRS1eW8D4NHvcv2ZDS_F4aPyUBqF4h6hHuGSBtMx5_LLIvsYLJPUPFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=fjsIm3TCi0lrAVa18LoORN7ee23nSn2xtyHR7rBulXYFaD2Vh_b9i9WGS-GUFc6-e0BcqhA8FRmMOQaedSckqQpMv8_VwFw9XMbUvbTZd88VBm2K28UUd3yi8AmN1zKxRUojnlov9-1a3IfTY_PkJbWJHXZgIlJhRZh05qfWeaqwlyI8Y-0HK2M76iDb_eXyEldko6Nm3-Cb6AaZL3Vr29uiKJqsmz4jaX0rbaCzTUHlAVhwFJr8MJH2MD7zw_wuiH7P041j78fP5u26BrZKRGq9dkcXryOK0eTxyeGXTgt3sAcidfukcsdDWoExMLZdRQ5FRUSPn1-YaBOZ_5Wlww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=fjsIm3TCi0lrAVa18LoORN7ee23nSn2xtyHR7rBulXYFaD2Vh_b9i9WGS-GUFc6-e0BcqhA8FRmMOQaedSckqQpMv8_VwFw9XMbUvbTZd88VBm2K28UUd3yi8AmN1zKxRUojnlov9-1a3IfTY_PkJbWJHXZgIlJhRZh05qfWeaqwlyI8Y-0HK2M76iDb_eXyEldko6Nm3-Cb6AaZL3Vr29uiKJqsmz4jaX0rbaCzTUHlAVhwFJr8MJH2MD7zw_wuiH7P041j78fP5u26BrZKRGq9dkcXryOK0eTxyeGXTgt3sAcidfukcsdDWoExMLZdRQ5FRUSPn1-YaBOZ_5Wlww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AofSPnB40GV2ZGT6wggjsrsPHahg74m7qk_D22bprDXsBy82evX1WupR5RYHIlDgOUIBp07kHGagKhDYShTwkSxPe-IXOo_LN_CwuT0PkVww5hD5-q8kffUc9wcyYCVktSxQBKl8BrJvhHXMyRXWuypP9XaWtBHdv2EAXap3qBQcq55zBhjkbVOn42rgj7honpecHqu85ynKeqrgLD02ID19mKCosIaux8as8S1GjavuZiyR-Q4V4g_ZvTZzzF-cBYjPfiZA3LYtWrj_4x3giHcQ6wU8pHI_wYIzErMlT0KuckruxeT1Gvhq09uaA5KFDyuEFvdh9LVx24PxniFasQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=N0TGpaZBh8fo4UHjs-xNleTwIGxV5N-0Z65z64Sb8984fDqf0aU1gmEfuKKGlCXHzvCGI95PATghLbmqt9MN-6ilY1DWLuO3boYOwu8n5lwPDv0sMbBw6ISVlNl_7jR-gDk67XoDhTYNM9IoixxkpR-GJXzVFdKi0dNi7VWJQ0yBLa9u-LokOa0pYFSQgyi2F58rR8qZ4PgHqN1BUyOsspzlpgjlGTFefYzjg7PPcKlUN9vk34Bu8llku2oidwFbcGXIrFvAt5zjVx3hpT-SoSuYI5zogdrm58EZQOeWT4Qurv8h8l0MqWMZCmlyrV0HuJFnQIyMT2dsRvBGcgF-sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=N0TGpaZBh8fo4UHjs-xNleTwIGxV5N-0Z65z64Sb8984fDqf0aU1gmEfuKKGlCXHzvCGI95PATghLbmqt9MN-6ilY1DWLuO3boYOwu8n5lwPDv0sMbBw6ISVlNl_7jR-gDk67XoDhTYNM9IoixxkpR-GJXzVFdKi0dNi7VWJQ0yBLa9u-LokOa0pYFSQgyi2F58rR8qZ4PgHqN1BUyOsspzlpgjlGTFefYzjg7PPcKlUN9vk34Bu8llku2oidwFbcGXIrFvAt5zjVx3hpT-SoSuYI5zogdrm58EZQOeWT4Qurv8h8l0MqWMZCmlyrV0HuJFnQIyMT2dsRvBGcgF-sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enAruS9cRpNV1Lm7Z-8o7Yy-bp3W-qdUlK1a0OryaChEdacKa3riiUzFWKTRUGxJ9ug55PTv3j174lD_sFYgAcht4PHZIVqI8bRdw-8gh4nCrwPxDU2Ayh3YK52ibe3W3EKUVkHpHCui94hX3Db1KNTQAvzYLNxifLoOPYORwdzz9QCkozoKnL4xZRYtFXGfYvsySITZ5HOzjZb-3YFtBg9vO4bk0AsWRLimB2lPK3kIbjg6veKkBkWTCmHU3hrySFSu3XQuHRO9w0W71jaz1nOjumD6fM3xuOg1Ms1l6l1KYQkBuQds1TS3f5hmnQSgkbduToZBreDRiLqWiiCL3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=AEpT7oS7PRMgVU3qt4g50H2NlpUsmSxHbGxk2jCWL3ocIQq-H3DK1tj7opt5QoXP7gGKJcvXhpKVxwYnM3g5jqIypfBy9d3D2Bfu6iR2WB1bES3I4V6_ntNV18STlkT1M5tGdiVzY2548YnlpTmTwEhkalgua8icQQCmJpiwGD7-NxzyZXOZz5OObLHlndzWjk-IWr0_8FWdI-hG1DkCqPUVVYLHbmjayeJgk36_LnwL_Va4jhQ-Gjqb-A6icP3mLHbsFh52IV-d6oXkKYdm0kWeBBDHdTFA3pu5UMqnCt3yA7r0E5Tlmez-MCNfKEXj_I1wyf4KYQhSE7K8NBT_2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=AEpT7oS7PRMgVU3qt4g50H2NlpUsmSxHbGxk2jCWL3ocIQq-H3DK1tj7opt5QoXP7gGKJcvXhpKVxwYnM3g5jqIypfBy9d3D2Bfu6iR2WB1bES3I4V6_ntNV18STlkT1M5tGdiVzY2548YnlpTmTwEhkalgua8icQQCmJpiwGD7-NxzyZXOZz5OObLHlndzWjk-IWr0_8FWdI-hG1DkCqPUVVYLHbmjayeJgk36_LnwL_Va4jhQ-Gjqb-A6icP3mLHbsFh52IV-d6oXkKYdm0kWeBBDHdTFA3pu5UMqnCt3yA7r0E5Tlmez-MCNfKEXj_I1wyf4KYQhSE7K8NBT_2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=KXE2V3iRfMPD8ol3v7l62TJmMnmg3xrc7VAyuGnyi-PqndzeaJzDNJbefnEssEXxezFefemzrJ-ByxmO9giAw4btnDEP1RNT556IeEaj8DwqYclfYRN12DmmTRuXd_ALaUBqtLOsf05_gkCpQ4l4GDHJdFVws2kMItanuUISM0rQjxHYoqLZmuLX3h4nQEGoulDxM-m5RgLYj8DDRpVcmoAbKpujUB_ZZeGBc3xxNog_r0xd07Rc10QnbV51R_JuHcwLsU8x05v7uWSJT4HJzACgKYirUIDammK0zJDyuAmj4bBnrPR4eDJTed3JRUrjKu01otVquGVujz8CqOLVlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=KXE2V3iRfMPD8ol3v7l62TJmMnmg3xrc7VAyuGnyi-PqndzeaJzDNJbefnEssEXxezFefemzrJ-ByxmO9giAw4btnDEP1RNT556IeEaj8DwqYclfYRN12DmmTRuXd_ALaUBqtLOsf05_gkCpQ4l4GDHJdFVws2kMItanuUISM0rQjxHYoqLZmuLX3h4nQEGoulDxM-m5RgLYj8DDRpVcmoAbKpujUB_ZZeGBc3xxNog_r0xd07Rc10QnbV51R_JuHcwLsU8x05v7uWSJT4HJzACgKYirUIDammK0zJDyuAmj4bBnrPR4eDJTed3JRUrjKu01otVquGVujz8CqOLVlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=cFk98CJqMrFwnBB-4lh1OStuXPy0zY4Z2pJERg12paozpXWtb3HQEO_oEmNeyHAADgUqsO67fzj0HlVwUTx8IjRZA3_2Qq8uyMQGJiI8IDJPQHW462ojQCX4YansE0qYu8IiUEYv19ZPZut3PcFHJs7hyivHuuxTbVFiR5BalHqaaBJTZFZ0vqQGMYhEGTuUsXb44EP0qrVOTLY2fnqSGG2lR4yLy6yPNixNRj5YzoF1wnz3bJQwRWOZ9t7uqL5SmHRlG4KvzBdhjoNpcDg256H92qBbJiObgXUXaJ_VzOO-EViO5E19UmLptxlYK7JsRbFYCeXisBgFg2CsPgjYSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=cFk98CJqMrFwnBB-4lh1OStuXPy0zY4Z2pJERg12paozpXWtb3HQEO_oEmNeyHAADgUqsO67fzj0HlVwUTx8IjRZA3_2Qq8uyMQGJiI8IDJPQHW462ojQCX4YansE0qYu8IiUEYv19ZPZut3PcFHJs7hyivHuuxTbVFiR5BalHqaaBJTZFZ0vqQGMYhEGTuUsXb44EP0qrVOTLY2fnqSGG2lR4yLy6yPNixNRj5YzoF1wnz3bJQwRWOZ9t7uqL5SmHRlG4KvzBdhjoNpcDg256H92qBbJiObgXUXaJ_VzOO-EViO5E19UmLptxlYK7JsRbFYCeXisBgFg2CsPgjYSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=Z-lDIWSA_GAIG767DB9_L2-GV2mjdTRYSSun-djmfdM1ZQ-oGxm6EeGHJc1UFjHy6nCHIEaFGuiz9hiOF970JaTcvCWQFTZ6I9qhSBKoayutWlxFmSgb71BlxchCPuXYGO3TkaOmUYEmIS1C6YmYykJMQBAkXof4221HIZ31hNyRgzLIzI-Um1HDPbRxL8HELzaZUYn2vjBqfxmQraUoZ4r24v2pcmqn95-cVrCQLA8-VImFCRW2qruoyCmgviHUoSa76G1gSavSTTa_xdHXnvqjjJV8VSyZ_CN9JU946-3aqxbVcMFbKKUNygC4tILtKkALlZeH51vML8nKgip0ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=Z-lDIWSA_GAIG767DB9_L2-GV2mjdTRYSSun-djmfdM1ZQ-oGxm6EeGHJc1UFjHy6nCHIEaFGuiz9hiOF970JaTcvCWQFTZ6I9qhSBKoayutWlxFmSgb71BlxchCPuXYGO3TkaOmUYEmIS1C6YmYykJMQBAkXof4221HIZ31hNyRgzLIzI-Um1HDPbRxL8HELzaZUYn2vjBqfxmQraUoZ4r24v2pcmqn95-cVrCQLA8-VImFCRW2qruoyCmgviHUoSa76G1gSavSTTa_xdHXnvqjjJV8VSyZ_CN9JU946-3aqxbVcMFbKKUNygC4tILtKkALlZeH51vML8nKgip0ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=NsGUQTtU57JRC_tDupMdHiSlMr0HsrcB1xxaKN3HCDWfroeoc4ETN8Ls7Fbv19kBQDhM3OJNQEacoPIglonmAY9iHSbpiREU9CCHJYhwVR2PYhJgYxkRasYTtqh_IocvMySYdsn5fqbtzVZuW9EAVBfSlPXiB-P9mkZKOuyS4erBnXUhg_XoVDmenua_KQfvcqKQf1I1hGQwkaAhmOwxSj7PJB08kWSJt11wtyzwrVgC6wmXbqc4Tv7wvhmepGBgoOub0Cw__qc7lu_WczRf2-7Y0tC2O9P6VmvAKm5Gfy5ZG6XKCePAJgOI3pmczsXwdJPfCS2NkMyWxiyD85oMeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=NsGUQTtU57JRC_tDupMdHiSlMr0HsrcB1xxaKN3HCDWfroeoc4ETN8Ls7Fbv19kBQDhM3OJNQEacoPIglonmAY9iHSbpiREU9CCHJYhwVR2PYhJgYxkRasYTtqh_IocvMySYdsn5fqbtzVZuW9EAVBfSlPXiB-P9mkZKOuyS4erBnXUhg_XoVDmenua_KQfvcqKQf1I1hGQwkaAhmOwxSj7PJB08kWSJt11wtyzwrVgC6wmXbqc4Tv7wvhmepGBgoOub0Cw__qc7lu_WczRf2-7Y0tC2O9P6VmvAKm5Gfy5ZG6XKCePAJgOI3pmczsXwdJPfCS2NkMyWxiyD85oMeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=SdkEM1t-dVAhUCBZkCLN-Vc9U3CfYsP_m_9lh1lrGFkEbpcOOW8CoyEtp2cYpPtsVsrdMZ2OOXWNclwlgPJIZ0X1Oz7BovWP9wEi021wBcdCC7dsXANRVSwKQpf5iC0fBfKfBKv1XF3d2dMxorcvW1WeKcoGpVpspl0jDJn506Cm91YaejzJNhXNZR55y9rMfzItBAJyYC-K-86HkcJpuZ1rZXjW4eIjBZtPOcOsK7fWppY_ATKhP0c72SOftnmWuuwdYAljvipkTwq_IJxe038pjtze9A_Xf7N0G8fJltcQ5m-pEBP-wPm384KgvCo9Df9kKyBOkVlpAeEQbjJHDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=SdkEM1t-dVAhUCBZkCLN-Vc9U3CfYsP_m_9lh1lrGFkEbpcOOW8CoyEtp2cYpPtsVsrdMZ2OOXWNclwlgPJIZ0X1Oz7BovWP9wEi021wBcdCC7dsXANRVSwKQpf5iC0fBfKfBKv1XF3d2dMxorcvW1WeKcoGpVpspl0jDJn506Cm91YaejzJNhXNZR55y9rMfzItBAJyYC-K-86HkcJpuZ1rZXjW4eIjBZtPOcOsK7fWppY_ATKhP0c72SOftnmWuuwdYAljvipkTwq_IJxe038pjtze9A_Xf7N0G8fJltcQ5m-pEBP-wPm384KgvCo9Df9kKyBOkVlpAeEQbjJHDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=ts8C00M5NvZSDmCyDjYuXyzwwjtkMQhz4Y1RRMihTJKXp6zjHHxq46319yodt9RQCJ2XY74_RgUv_7Rabwww55_5dqGY4aLWNAyCkKZi3wVzgdGVPv-qBKSQfgJGToOBXMb4eKrKHfUOEW1Qov4GJVC0UD6d-BctXNIeCD4bL5o7jN5LcNuhyA68xhPEL_FpZAvMn97MX5s3yS3s5ykfZUuC5QvmkJFlQRusufCWVXc4tEumhVfRTjuvsuwPXBHdlrMMHdAP-j7vHuUihaqUptY0Tru7fpeXqYgFLd37zHWx-7hNOb5VJsw4G7FnJEaSLRH0X1ewe_N529IeyiFC_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=ts8C00M5NvZSDmCyDjYuXyzwwjtkMQhz4Y1RRMihTJKXp6zjHHxq46319yodt9RQCJ2XY74_RgUv_7Rabwww55_5dqGY4aLWNAyCkKZi3wVzgdGVPv-qBKSQfgJGToOBXMb4eKrKHfUOEW1Qov4GJVC0UD6d-BctXNIeCD4bL5o7jN5LcNuhyA68xhPEL_FpZAvMn97MX5s3yS3s5ykfZUuC5QvmkJFlQRusufCWVXc4tEumhVfRTjuvsuwPXBHdlrMMHdAP-j7vHuUihaqUptY0Tru7fpeXqYgFLd37zHWx-7hNOb5VJsw4G7FnJEaSLRH0X1ewe_N529IeyiFC_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0H_cytAIcKTINKYBfqPvyQRPt8c7jDwykmFsPnEJed21lb7uo4ZaB-wn1Du2VDNVbIY9cOuu8m4X9uBgebiP8XvFefq42lW2URq8wgni7nb3ex5tKjQA5JEcVB5XVixCfrLZkHNCAuKnOs6n4t7bA9lv_MHv7oDj4CWbGeknu4AzXD-UGGITD7wmX37TkkwJLGJd7FxGzGDoyoeNOkiF1WGfChsC2ptiJ7Lgv_5GhtdTb8B-QUD2NdYanxeyor8HiA80_Djv0WlvvccH1WXERm44dEtRgIXUEUfoHwJVwfuMBs4nrigowsyvhGJg-XZVfPZJRJL8f2_0AtyCMbOQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbDMvJJEvL-U3nkOIJMYWJ82kYsRzCkcGO2DnxYmwsKn8wpZNc6GHn4Cxxpw-6ATGD5qCLQ88vSfAGDPKTHObyC8MVPiAP3nSgTJXjsunbCHw960p3JVMr5Od54LvshUkHGMVI35fk94ZzzHShntQInE-RbUlu2GAQH52H6MoTdlPmNHwyue1L-NNAg8NI297vJpqwrgo6BbNMk_y6AsbMC6t9Qpe2gcGttFGT2T0Z3UCAIWlASGTnyEqP_Fexbuqr7HWePn1Phdd7RbUCICc-JqCHIWuLWpvWDttFtqoMon7_ojs_e9dPwDELkJPDZ9xIE1wDFMyRxC3EZPjDdzhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=OunWEqk3bBuLUF8katTmSj2Wk_HKSfDc9Rclly-EnDoJTmTNgjUsP-vrLLlRo9aFanZ16lsHiqyDNvzE32BvzTAAo0Ort2kIW1ZNwYsslukve1EreeBO0xnyqEyaJvZtZdA4m5cKvvjcv_cnj-4_pU7Ln3AH4IlEQmvUAt0sp1qIALQnpn86DNdXCAJbn27VnZTt3Q72vrDzNBP_7uzKtPQGTo6XuAkUYXAZsEDxF8qEATrCDKyR_xyrYdcGCQsuPBKrCVf0WYqU4qL1GW2UIYZwvX8CV15wdILlU7yUQpypLC_ZFnWYqRVNfKplmJi3awSSLqas_IvrF8qauuwjJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=OunWEqk3bBuLUF8katTmSj2Wk_HKSfDc9Rclly-EnDoJTmTNgjUsP-vrLLlRo9aFanZ16lsHiqyDNvzE32BvzTAAo0Ort2kIW1ZNwYsslukve1EreeBO0xnyqEyaJvZtZdA4m5cKvvjcv_cnj-4_pU7Ln3AH4IlEQmvUAt0sp1qIALQnpn86DNdXCAJbn27VnZTt3Q72vrDzNBP_7uzKtPQGTo6XuAkUYXAZsEDxF8qEATrCDKyR_xyrYdcGCQsuPBKrCVf0WYqU4qL1GW2UIYZwvX8CV15wdILlU7yUQpypLC_ZFnWYqRVNfKplmJi3awSSLqas_IvrF8qauuwjJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8D6Etr-CvKEiFOVhYVTiyK2tpn-P2F0yKB37fl4MrD7prx5Lv02F-hC70Zq_So_fKvqT18OAnyeAI1VK3mOgwY78RYP0hQKIFNsdeGDSezMPcfQTSYMYf0EPce39a5iUL6sN32ygmab5c73UbETxsk7jSqfQBfvzanBJVIKlY8SETjs6Cytum1vtS28DePlc_skVPqb8ovQXgxiapuc0xs8h4Yd4IgqY6fYDvntAqXvP-xZUo6InwQySJFq2wTAc-dFOXBqimwLCCuOBoodjbxDJ-z8n_Z01gZEl1Cy-mKp1mtp8Zv9-yH-8bw4fM5BrEYJaVkPUHBL3DOOKY7DLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjQm8pkO_aAmUUpGT4k26bRIAdAQ3S9S6vL4nchcf1MU5rVb3vKDxXuX7FyBNHDunFj80i8OCGDQIV72RTcrIzIhLpPM6mVmyhIxYI0529nZvDG0i7XHj0YIca1xzk2tdTyOW0ID1PQch7lB9lO_Vx0KG2QO6EReYc9kpfrlPJOIqoC3LP70MScsBZ1VQGTOAsQJGdmRNv4uM3tRUuft1_2RGgkFsnHeZnV9pmSHDyy_h06IYdwGjOIJnk5QL79rDlE7p022M1pEJ6IWKzO1rBzfe0ziiI9VJ_jlwP6r6cNyTw0WRaObKsw24LdotVOeTpDVf-iYAADgcBBtDdi62w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=Inx6YF0HzvPOsWLLvHGut7N8N_HYUqcaHIJarsxpm8NRgzSctMDeRffiv_L535YI8qj23rn0Cyqi4MyLRSnksnjmaFRYysvuEhPdLMsmQdYGSS6LLBNAgq9pHi0-K4rJv8F0hHE6Acyf67E-4SykEzb7yHiAlb_g_sOBM-BF5P3WNvE1GzTnyco8NMKbxPnd2KCHMq2uWTvgA9Km78yQbhZEGoXoVbJvcitOJd2RcAgSdoDBVnqktdwxSxJhQc61U956dCZc8Dufa67I-zpk-3HbdvYkRd_r2LI6PnrGZZngFvAZICpK4vj2B5PVQ-O9fiSYFW9B-ZxIS324-REDZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=Inx6YF0HzvPOsWLLvHGut7N8N_HYUqcaHIJarsxpm8NRgzSctMDeRffiv_L535YI8qj23rn0Cyqi4MyLRSnksnjmaFRYysvuEhPdLMsmQdYGSS6LLBNAgq9pHi0-K4rJv8F0hHE6Acyf67E-4SykEzb7yHiAlb_g_sOBM-BF5P3WNvE1GzTnyco8NMKbxPnd2KCHMq2uWTvgA9Km78yQbhZEGoXoVbJvcitOJd2RcAgSdoDBVnqktdwxSxJhQc61U956dCZc8Dufa67I-zpk-3HbdvYkRd_r2LI6PnrGZZngFvAZICpK4vj2B5PVQ-O9fiSYFW9B-ZxIS324-REDZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=c1lPX_WHXt2TyC870eDNMO-HHE4wQXAmB3kzDM7CH2iyx1PTEsM8yrMt0Kwq2m0DYwC4Xv4DLMiO6hmj8jKvPBawONNayEIV6CZvIh1cp8w6wE-PUV3xHh-7vg_fwiXyzrOMDa0YKCrO6B5sSZ6SAi_bjKUlJJadbS1hvzzoB-6epjxQWSxWkyh4pSth8Yd0wGVRvyW320xa8TymsMYAfkndxGdjvbBat5BeCnpFmVivJ6Ye-NYQVOvH0qwS7OmOtBsCaG0c9dmMYJT1ycjJq96EKOqs5YSe5bCEdyowQMm_-qA3HasUqHB5mAtNhyG62tVHOVxFAGk-huljPVueyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=c1lPX_WHXt2TyC870eDNMO-HHE4wQXAmB3kzDM7CH2iyx1PTEsM8yrMt0Kwq2m0DYwC4Xv4DLMiO6hmj8jKvPBawONNayEIV6CZvIh1cp8w6wE-PUV3xHh-7vg_fwiXyzrOMDa0YKCrO6B5sSZ6SAi_bjKUlJJadbS1hvzzoB-6epjxQWSxWkyh4pSth8Yd0wGVRvyW320xa8TymsMYAfkndxGdjvbBat5BeCnpFmVivJ6Ye-NYQVOvH0qwS7OmOtBsCaG0c9dmMYJT1ycjJq96EKOqs5YSe5bCEdyowQMm_-qA3HasUqHB5mAtNhyG62tVHOVxFAGk-huljPVueyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=dfLTLP9AwB0YZXHIhvarKjF8e6c2TwoJ5cucu-50ZiiR338XQI8vLANNxII9lIyw-pz9beSIMBAkQ2vSp-CybU6NZk0ebbing72AdzhCnacQZu0Fc33sStD1VgqUEfhFJT6EkYovmNanrgj5oaX9w6n8pCU3VM87YZgRAtba7CVxjU_I_sFNzSYENobJWLptWOw43jPKtQ4_gzIHHSMIaTj78d5SiJAV7rTjCZfqETHA9RQbG4UnfOlCIiSR9wjLDfvB4ISFJjpQanwJgYpPprahjwSbPrqZ1ZhHgmqt1sm6fWcBuGRRJquNPdzUJmf_z0I9SKm3Z4DqFHc4C-htyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=dfLTLP9AwB0YZXHIhvarKjF8e6c2TwoJ5cucu-50ZiiR338XQI8vLANNxII9lIyw-pz9beSIMBAkQ2vSp-CybU6NZk0ebbing72AdzhCnacQZu0Fc33sStD1VgqUEfhFJT6EkYovmNanrgj5oaX9w6n8pCU3VM87YZgRAtba7CVxjU_I_sFNzSYENobJWLptWOw43jPKtQ4_gzIHHSMIaTj78d5SiJAV7rTjCZfqETHA9RQbG4UnfOlCIiSR9wjLDfvB4ISFJjpQanwJgYpPprahjwSbPrqZ1ZhHgmqt1sm6fWcBuGRRJquNPdzUJmf_z0I9SKm3Z4DqFHc4C-htyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSKh5WuGsjidJFCXmo5o_gfgrlr3srDzN23EOi0T-SW6vpMeMPFBnizgdSmBeeIacEi6B1lhnzdJ7ZBJkDepEHCzaD3pAdb5XQqC4spAOkknofbvpnES3wJWz_KrEnPKL3qKhnUUxFN0dakLzxNtGV1W-qE1h62m4Ol0OpKEmHEjdamx5CIY403EAv_KWdQzqqyUifEApN--S7Tn0ev4VeTz_5lUbz872uCN4E8NPXV_NylBk8M-sXocwJuOLLIhCOnl1zPCB2adlZ-IpL6k9buLlxRo62gbWEmUXy-PVJWyKgL3rE9IbXPA0diYHblE3UeLzA2Yvz01HFnvVDyDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nclJL9FAWKd23Dq5GflGLMx31_XdxQEVx_QGx0WrgUhb9BTP_KKfZhg8Vy_e96fwfknG8KwA1L7YtvIm7GAGR8Ip_GdjO_Aj15haCkDtKuDUPIjKaZX2DUi6qfj6ZxSSw8_kKkKiULH-Tp5cxWzawJN1dCDvm1qYss9XU68E2jACJ9HuA5CccZ2U4DZjB_cv3VRMnp5dKcvUpawc94Nng0kt7zMkJLCxqPaj9JQEeREByL3uCBMgbUvjaVcU1px7BUzTqqLedVcWOmaopRXAuHAJJWVA6BYGR6tWPoZH4PQ9DjnrLzLc0BMOBGl6_gEfdHTgGbYscnuC_v3sdPDwbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=YiZXVfHParTV1MK-pyBSxjmy7f6V8mpsyviVKwOcgvqBMbZwz6TRtO4rWkOU9nnvVZn--wtfkVR_3Vo9d-yGfk29pBQkaPHBpyRhLJThVlKjr0E4S8Bnd5qwHNcy1Ds5rVitCklRHijzVZhbt1Hy2TFFnAU77FaQgL55-PxgE1weWyqoGZ0mIhjWLp2nNZi7Hd93_bA7zc8uk9HjWR84Vckq1LblSXW3hb1r4TyEWnNd4WC17ab3jkkjewzLQdHuFxn5Lo2sxYBOvgc8eIHJkTZ_5s2m-6bcgvQpRVTBy_QVEd9FZ-28hEXZQwnkP_SFowTxsznHlvPUgFXqMsfIAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=YiZXVfHParTV1MK-pyBSxjmy7f6V8mpsyviVKwOcgvqBMbZwz6TRtO4rWkOU9nnvVZn--wtfkVR_3Vo9d-yGfk29pBQkaPHBpyRhLJThVlKjr0E4S8Bnd5qwHNcy1Ds5rVitCklRHijzVZhbt1Hy2TFFnAU77FaQgL55-PxgE1weWyqoGZ0mIhjWLp2nNZi7Hd93_bA7zc8uk9HjWR84Vckq1LblSXW3hb1r4TyEWnNd4WC17ab3jkkjewzLQdHuFxn5Lo2sxYBOvgc8eIHJkTZ_5s2m-6bcgvQpRVTBy_QVEd9FZ-28hEXZQwnkP_SFowTxsznHlvPUgFXqMsfIAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=YrhGA9vBTVIxvKawxLvIQWQEYxlslUZ1p1EhNxYsxJysdQwACKpa2CIJ96h8KVchMLeNqr7Lxqn6NJj-eySibfdtDvxdsHYfDEjsVCCO1frRYuHRigSV8fNYIPhL0FP_1Upt7ogo6OBp1UIknkDDo18Hgozv74l5jn5mA5iQE4SjtfLWFTp5S0YA9xZyrcX4sjwHkrPv_YrvlD1mq4lSk5LViypYFZJe39464RCaqcaAu704DkecjnRbODs_U7ICZ5aYTFeiPz582rU_uX_TFBWkQdaPcQdzfU1WEz9ZAG5F4QLjVIPfO5lZXcMBkydYUUfrogxBCLkCqGEZVphmUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=YrhGA9vBTVIxvKawxLvIQWQEYxlslUZ1p1EhNxYsxJysdQwACKpa2CIJ96h8KVchMLeNqr7Lxqn6NJj-eySibfdtDvxdsHYfDEjsVCCO1frRYuHRigSV8fNYIPhL0FP_1Upt7ogo6OBp1UIknkDDo18Hgozv74l5jn5mA5iQE4SjtfLWFTp5S0YA9xZyrcX4sjwHkrPv_YrvlD1mq4lSk5LViypYFZJe39464RCaqcaAu704DkecjnRbODs_U7ICZ5aYTFeiPz582rU_uX_TFBWkQdaPcQdzfU1WEz9ZAG5F4QLjVIPfO5lZXcMBkydYUUfrogxBCLkCqGEZVphmUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyiEA8J_lqiqAv5v8JV_CcNWn9yHzGpIZ6H_g67hqMUVuYzvJwxOjQhLUuuAAGKQR4sdBwt5_CIJQilFHtdvV6SjuqXiwpsryr-b4ieRPUhnHgUmP3e0zpLjOnySLMLlXsqdq5LQikrsM6TIpNR87IdyjMG7YRoeXNnU-6CWcOFbhVl9PGrO7rBO3FhtKV1tv5t8PZNCrcROZf-GO5qVlg8H4Jxrv0nCXlWhXPx5ToxHZfg7w0LG20RN7hmgANg6urQuWru8HOV-swW2NmPETNLLHmyb3AhtQJXIOIq3rVbxqd9KDdIUQnSOZQcGI_HBRDlz1xc-uRO8pu7pehSw4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhGosDgfvWePpuxLq9InE7odyM1wJWyEgdeYVL8oh8sDMxugcAwQaHFhtra_OnRqh4hm4xjlAIjVHYsRnjUNcsF2Q6sUeVjPhzb0-ehgHV8YX-JfZ05Hg5PBGmdFJEiWdj3QwK49a65z7_c2uA1uM-jp-o2tF17PoZgjiFDizJUl4grdhKvqkUQXub8SD42PzZxluEVPxucrd3GOYw19oZKObd6P6UDZ4UlZgUF4oD4zW_gdgQQJD7xGYn5DZrYx-IqKWu2hTZYNSCXizVM_QnOPOrCcv6cVv_1vDqbOR6zs0npy2WhpqaDFC6ofL43XbK6WLywEHy95-QCC7bJ3sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpT7cG8JTg-s9FEv5VgW-hTiICZb1kbos1u2vAMcXB4LQ-0MycRv_ZT-bVdi4n4rEByzROOEdrkLHQfJGIedI5zBQsN46W2-Lsvki6T_YK1NEtFHfkcZpQnOblUmVfrB-VfYAxEUr8vtSmvhOqnIdhM7T-1RTWJgqA0eSuYASvFId0XObiAKD3JT6d5FRKjPs4EAxsBCGd6BtPLUKqSy301nI0_NRELmigwYU0Sjg4MuAgA63K3-2C79ZlefGZM_VeXndRW3L5g5ymiQRKzVDPF1I-e4Kzq_nDGZcBA8ZxSAo_HeY0Xb4WGiNbvaxnsS9rfQD7kBCWIVp1zyIAEzBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pbkvpe0owXS2NL2oEecClqGLp7A1ndsbwGfj9S7WwMCeq-8ckBM_rIPnCm96E9QJVA1njkq3YqKPPsMOkiBHm3Ma5mE__zZsjVxJZeNGUP_nJ48mcqBxYKFGY7SKP0vNed8oUprTKOeGp5sE7hKTPrzGntsWoIb1eikYN_Wp75LY_2zh3qIxAqz8ct_neKhnlG5RZH7zYAISIJLd7EiWtKmh-hASEHE3U4cd9BXyAgW1FGfwHiQg-ZQFtj5OI3UJYaKeQTJzI6NHsHM0Ll-zUShpC3YSzjCESo_gaFmpE9qTNcUnZE0Waw0mdjgyp9B0rfknFQeodq5DNOYTrGmWUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFcT2DE6mHCDTpfdrv4x4AJV-Qo90ZSNZCax-HwGldzeUcpdnfUGNyJW_bdS45bY2Kj5_09yhXfIqOeiIq4OqIwz_24SdbqF-pfH1MGDJPpknTY1JvJW7fUr8moyp6ie2HO063U5kNCpXOJoyQf01beye29SSW9BAB0_hBW-TBfLdaoSuGHL9eosP5usQmEYBll7e9BQyLolffLUuXKEe7Td_6mvR67TsVJuKatofMyF2MoFDymlibgF0GYT25H6N8lioTQyr3cMiDAgWu27XWMdnZQ_PQ4I6Zertj0PLV-RjiipYNcw70LjqtFK9z5e22SPMHQfWSXVXlcQ9Gw2EQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/my_NnAhhWxaREPPTX5gJjn5dcEkfF45CKX1Brf27hwmAd1gJRdgUdS3ATgYySgeaJAE8P1LU3QpQSXJjJPNE9KDxM-2DdDmFEB5KWOVNVIC9ugGkzeeHr5eRHYMZXYkvmNHFQIz9A_BTQJhSTSxCcbHsWmV386SAM0xP35KIZCrG3iR8MgBX3d8hvKoGWhbD7vKiTj54JQF5yd_ScwxEuQUGqbH9tr2JXcYC6DHB8q7W2pnckpnaKShMSEqBZlt1ThwJKU6tu4J6eGYdC5Nh0m0rsde5KO54g8TPPQsxf6Ke1ciHdwmsnT5ef6tTM4gojBVwGzT9y4IktWw8RP7vwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=ohX1de8I81qznZzaQ1cVZKNCuMWWT0ay7vWdBkuy7_0RoaVbytf-PHrY2hrB0aa_BYNI4y7UN1hgBZ9_AwYwnOiRvJNXMZ8mNZUag1vYSDxt2LNvKLFIgj4WuV0_zxNenkXZIMJkufeIhhz81kjrVcx01F7oElpw2UUXajkNBshbj7N6zVAJ2o6bkRYasO4A-wUNRK4ggzQ0QJLajSv3T3mZIAn1Pnh8lUckikVcVqJXtEXjY4qLSYgygveXiiVOuEqhVcEmqun1g11B0eixiIT7NDwjcLk6eNb1e49dWxX6wAj6kLOAKyLdB617O9t8GFWv_7R_hev3mjesp3aGrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=ohX1de8I81qznZzaQ1cVZKNCuMWWT0ay7vWdBkuy7_0RoaVbytf-PHrY2hrB0aa_BYNI4y7UN1hgBZ9_AwYwnOiRvJNXMZ8mNZUag1vYSDxt2LNvKLFIgj4WuV0_zxNenkXZIMJkufeIhhz81kjrVcx01F7oElpw2UUXajkNBshbj7N6zVAJ2o6bkRYasO4A-wUNRK4ggzQ0QJLajSv3T3mZIAn1Pnh8lUckikVcVqJXtEXjY4qLSYgygveXiiVOuEqhVcEmqun1g11B0eixiIT7NDwjcLk6eNb1e49dWxX6wAj6kLOAKyLdB617O9t8GFWv_7R_hev3mjesp3aGrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=hlElrgvVfv-lPi1gFS3lEWK6spA8WOiHM6yritLTtv5eKJ-8xLpH_9iKh0RH-4Q5jXOpiwzP4uc8RptmuFBeXFhdm7mteqP5q16UPoN9L_6jgGfGkIxybZj9biQM5u-Sl0lhRGeylrfrN3wHf_-cCMQk9T8yWa2oJB94gRs5o4VbGXKxyE4OP8T0IDM8TMoHTEisw48b4I6llmvAbzJkOZ1dRNy_X8f7zx6xM2oQA2QdDHnvp4HuyVzboAPJwYU4Cr1Jc3d1tFV94oKwOWFrszHGN5YnP-MdEKLyY9UnBHNqU6mUuB6xBh246ZVlc-WZ7RAwEWaB0G9oV48q8E0mYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=hlElrgvVfv-lPi1gFS3lEWK6spA8WOiHM6yritLTtv5eKJ-8xLpH_9iKh0RH-4Q5jXOpiwzP4uc8RptmuFBeXFhdm7mteqP5q16UPoN9L_6jgGfGkIxybZj9biQM5u-Sl0lhRGeylrfrN3wHf_-cCMQk9T8yWa2oJB94gRs5o4VbGXKxyE4OP8T0IDM8TMoHTEisw48b4I6llmvAbzJkOZ1dRNy_X8f7zx6xM2oQA2QdDHnvp4HuyVzboAPJwYU4Cr1Jc3d1tFV94oKwOWFrszHGN5YnP-MdEKLyY9UnBHNqU6mUuB6xBh246ZVlc-WZ7RAwEWaB0G9oV48q8E0mYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=lYYuGfAxtmF8ncmrlBn0enPYz90lN62tgA2m-Xt3PjKf9mgZozriquP8rHKMx7JogViSjhVGBgcHK3mc-CIgvNPajIGFSce8qvGouiMGuyRORtWjZq3tuFn8ChYC7fvFp-WKs8vhEf47y5eVe7c4cBJitilPNzpVEYYR4Bbgtb4XFcoP4pKUdbf_kd7LxX3OKfRDNuKRh_0FFfU7CCZpn170F-imdzFH3KNIQYPtdBGwZO0NiKUA5uugMJMDJ1KrleuLlD9QJY86y0QdVLlAeKGYge4rmmkPxOOwoRfMzFi6qHZ_M_G807-AWfK2MQbWL1qrSyg_yDGDuvuBQGkG4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=lYYuGfAxtmF8ncmrlBn0enPYz90lN62tgA2m-Xt3PjKf9mgZozriquP8rHKMx7JogViSjhVGBgcHK3mc-CIgvNPajIGFSce8qvGouiMGuyRORtWjZq3tuFn8ChYC7fvFp-WKs8vhEf47y5eVe7c4cBJitilPNzpVEYYR4Bbgtb4XFcoP4pKUdbf_kd7LxX3OKfRDNuKRh_0FFfU7CCZpn170F-imdzFH3KNIQYPtdBGwZO0NiKUA5uugMJMDJ1KrleuLlD9QJY86y0QdVLlAeKGYge4rmmkPxOOwoRfMzFi6qHZ_M_G807-AWfK2MQbWL1qrSyg_yDGDuvuBQGkG4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=UOPZpiqg1BnhXcrUQ_YRVcoePzgasX2GZD8sT7f2mbOtvPlAXa0YLHku8_Wh_BGX2YgO30CL-MfH3okdnYj9w2xsP0o4uiyFVMqg-xMXOIErMu7O3WPhYjdO7-7Tp0vx8b6IkyT0bRzFFlVNuclBneZizif_rBOYW8tJQuY8ZZzF7tcBwSAAWqlEagrhf5s-PFSMKA9JZK4vO1ADGC6Wu2oCr3KYDoF1RnDPrQlEKo162JhwAwcaEQ6wfbWAe_aNNTl6HKx_1VqM2Dx8aLS3PvU0UbUjtNj6Dsmv3R_c2kJgx8hM7wB5Ozil7MS-OhTypmvyN9nJG8lAX5ACNaQPHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=UOPZpiqg1BnhXcrUQ_YRVcoePzgasX2GZD8sT7f2mbOtvPlAXa0YLHku8_Wh_BGX2YgO30CL-MfH3okdnYj9w2xsP0o4uiyFVMqg-xMXOIErMu7O3WPhYjdO7-7Tp0vx8b6IkyT0bRzFFlVNuclBneZizif_rBOYW8tJQuY8ZZzF7tcBwSAAWqlEagrhf5s-PFSMKA9JZK4vO1ADGC6Wu2oCr3KYDoF1RnDPrQlEKo162JhwAwcaEQ6wfbWAe_aNNTl6HKx_1VqM2Dx8aLS3PvU0UbUjtNj6Dsmv3R_c2kJgx8hM7wB5Ozil7MS-OhTypmvyN9nJG8lAX5ACNaQPHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=YJblMH0gnUKspAUoKS7YZZkKTqF4c4CHZdCZ-J1MU8aU_2cmN8TLnNBc5s7GOnVAqGnd3ZrNy6XU8X29VqwFyTJboGL1W_JOQme8ev-38Hl7OFrczrZip08KHVk0HPUsf3S2_hHhBPUKb6R7DdQKCYyZO5wQXCJIkbnM_uWvXUnwbmKq4NeRWVVgER_bTO1eENvRVeVWGYczAmPXZJ7an8oIOZuw8Q24nk5JtmDhY1ArMIyS89Za8WpjKsdqaYCjSEQJHNB1uVP3AFDpOsUWQdR3rLbp7zTd33MifDXZz0PzYlumOt7-h_Lred5Is0yBO1QvzcdpEXHjsVaKF-1TNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=YJblMH0gnUKspAUoKS7YZZkKTqF4c4CHZdCZ-J1MU8aU_2cmN8TLnNBc5s7GOnVAqGnd3ZrNy6XU8X29VqwFyTJboGL1W_JOQme8ev-38Hl7OFrczrZip08KHVk0HPUsf3S2_hHhBPUKb6R7DdQKCYyZO5wQXCJIkbnM_uWvXUnwbmKq4NeRWVVgER_bTO1eENvRVeVWGYczAmPXZJ7an8oIOZuw8Q24nk5JtmDhY1ArMIyS89Za8WpjKsdqaYCjSEQJHNB1uVP3AFDpOsUWQdR3rLbp7zTd33MifDXZz0PzYlumOt7-h_Lred5Is0yBO1QvzcdpEXHjsVaKF-1TNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=mvDK9GwYxeWWXWNs5BuTGo2ydbEGZh6-OhEot6vRruFd3_GM98KdWi0rZE9OhsyDHRWfiaAUtSFVi2h9IO7cPAbIRxO9PX7J8XFjoNWJ99WXUfhcQA_ZeBfSDg_ITWZO_StTc83f0CLWY4Wgb63OG2AbtTclSwt8RDV8-9t84rVjHSqqr3PW_1g1-nvT35ePYtNZA3OUg9nWq0H6J6_pCGdwNdIFDxjMrGKDqUpDyzBm2eXoAGoIfezpMytWPzjAAcJ0MpHA0-qrT_OvsdLEQ671gUPNNqhaapoG9nRK0LlQBypxlIJesgP8-MIRgNpUw_3EqNyRDedNPN9-lqGBBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=mvDK9GwYxeWWXWNs5BuTGo2ydbEGZh6-OhEot6vRruFd3_GM98KdWi0rZE9OhsyDHRWfiaAUtSFVi2h9IO7cPAbIRxO9PX7J8XFjoNWJ99WXUfhcQA_ZeBfSDg_ITWZO_StTc83f0CLWY4Wgb63OG2AbtTclSwt8RDV8-9t84rVjHSqqr3PW_1g1-nvT35ePYtNZA3OUg9nWq0H6J6_pCGdwNdIFDxjMrGKDqUpDyzBm2eXoAGoIfezpMytWPzjAAcJ0MpHA0-qrT_OvsdLEQ671gUPNNqhaapoG9nRK0LlQBypxlIJesgP8-MIRgNpUw_3EqNyRDedNPN9-lqGBBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUx09crewD6C_YF3SPmDLk_D67GvtGYSX3yzmSbaVbAbkWpStw8iqlJJmrEQamdYsgMuxo7hRefhD9EATNXXUIF-IQRzIPKAUaG34H6IK-K95kZDmvKP6G1npvfQrIDRwF1wsYfGFKrM-iYxqLEiqzQxdgDbQVNtAwfLpY77Rw8wRFg8lDgWX6WBXmCqgtQ4RC-FcGGUq3dksuWpiQBbyHcvy_4vA7fE6kwjRwQs9lTGD9Q5vspoOIym49e3oaFOMRzM4zxu_sS3aI26XOPQNe9YFX27cY_J2Sj5a5P0dr7Ynvukm_Ch9r-QQtFGs9TJzi7_EpSxq6BDnyBZFYhR5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=LEMFl7LZVLx9rMr6Z1k9gz5DZptTn_lmIIre2DScwHPCEEkdbEHoZVDWmse3UE1z03VL7DJgiI4r4pVy_JoUe4Bq2CH-zdI4_x2Hg90rQhL2hItnvu6K0O6m0B9y4O3KZR0lQVrNqUHoie0ks5DqJ2qKN9MfR2lhmxW-AJcZjfi-VIgTLT1rFjjtvazO2mU0LmMU4t-M9zDwvrP-LioGT-gl6-p71Jd086XetqTAvgFqnQpmyQ2on6DMz1ljQA9gbZhdc88wacsRXE0pM112xIBdE_zDRsfJ6fFKv2n_Jgj7RzU07LrUBZdQg6yRr7Hh-pb13oRld_Muz1xmUV4Bxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=LEMFl7LZVLx9rMr6Z1k9gz5DZptTn_lmIIre2DScwHPCEEkdbEHoZVDWmse3UE1z03VL7DJgiI4r4pVy_JoUe4Bq2CH-zdI4_x2Hg90rQhL2hItnvu6K0O6m0B9y4O3KZR0lQVrNqUHoie0ks5DqJ2qKN9MfR2lhmxW-AJcZjfi-VIgTLT1rFjjtvazO2mU0LmMU4t-M9zDwvrP-LioGT-gl6-p71Jd086XetqTAvgFqnQpmyQ2on6DMz1ljQA9gbZhdc88wacsRXE0pM112xIBdE_zDRsfJ6fFKv2n_Jgj7RzU07LrUBZdQg6yRr7Hh-pb13oRld_Muz1xmUV4Bxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=aEAyc4i5j_-CTaINIkwmhdxUgSoYhmSAM-6kq45od0EJbLMDzOlzwvF_Gs6zsRH4imbUpMNHSeYA5ItBlFtJibIlETI0HDqzaqSw_8_6T_WosaEF-Gd7pzxY_4G-CqqrS4hjzTpZp_XJsp_tjhTt_u-Vp3KEX2otv8o79jE0mlbh2tzQ-mVpbupU0VzOAh53oW7EvYx0JDTVS_D1XZgjrukS4QnWEGBQwa7YncyuHrSnM6rZ4ZTF5SInlJrHF1DNPFzf-SIYg3n_yPKdxyrEmGeiHC7KAeUxrrwUHsTr9ZHQIuqgT5T836mAibSbChr7NWZOw1WcBpGIVmKF3_sQ6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=aEAyc4i5j_-CTaINIkwmhdxUgSoYhmSAM-6kq45od0EJbLMDzOlzwvF_Gs6zsRH4imbUpMNHSeYA5ItBlFtJibIlETI0HDqzaqSw_8_6T_WosaEF-Gd7pzxY_4G-CqqrS4hjzTpZp_XJsp_tjhTt_u-Vp3KEX2otv8o79jE0mlbh2tzQ-mVpbupU0VzOAh53oW7EvYx0JDTVS_D1XZgjrukS4QnWEGBQwa7YncyuHrSnM6rZ4ZTF5SInlJrHF1DNPFzf-SIYg3n_yPKdxyrEmGeiHC7KAeUxrrwUHsTr9ZHQIuqgT5T836mAibSbChr7NWZOw1WcBpGIVmKF3_sQ6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac5A3Kp0QCe2j48-s17oMauNZM0XO17iNmKEzS_gFhnzNNZcD8txRvqekRdHtQUfv4pi2aAO9tNNL_e9EhkCx93eee3AkoQ833ql-Bj-KcaHdZihy-1qBxNmHLoOu-8BNcW0tRJrX4VyWmTWmDX9Qe8u7dWl5NKK2LEkmGESScoAua2T3Ueyg7VDA6yfA17wXJ6-0wvsozH5r7bZEfz8xo01veOz-aOuHocA_tbQnWN_Axn27-6fekf6nlantGHTx3ERED4CfSIjcCofvvacDuzKsz3-XTwHe-MGlvIUEEM1pEbZisM5BjpBA_SvANut47IjXkiAIFEGIG28Xoz6tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyOWaDZnbq7Br-mFUWw8bH016mb52wvYX_MLmKoX8Rhwx-ktHMWv_7-crNimaF9z8mN9_ofGlSOrAJbMJwPokf26TopQvHeocJNKINyCFjTHJQjnpE3b7fCxiSFQ6LGXLXUxEfnp2tnuXpGLYtXrrxW1OXE796r99E_B2OSdSo4pImoPZc2CjlZjmsnPpVZELHjKBN0e46XRzUDIrrVyTggq7hYXOAUXF01zGOvFO28XN8Ad8um6-Y1OqLC-nfQmjaS0nPS6CLB7ZkgW8q4V4pi3aNvCbAyBdJM4Aj9uY_i_-yGUrVUJRNTSUuid3VVHgOwuOUXkBPgfhtN4uljYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3g15UECY1jirpkzvYe5RC6uJ7UCk1EXq5rgS9F-7w6qqRIbvUE28KXQkC-PES-yVCZLdXuH0Fm2EbnEXddztfhofAHkiDNGLejzrirsNEeeXSU_73GfejMKKvIiu8wIKvACHC8SEOp1HJ3GKAthrKNx6GDdNhVUE1T4eGi9uxnZBekHxNzkgaiclaltls1Lm5cl3epsaJQhJ2c0XMEXb9LcgNwV4Tp5g1fHPP40yj4ElWLsIeKWZJ2McqcECQ3FHCmy7SIl4RDeVf5xP4rth3x0HquM6ddeFcs9AI9-JKHnkp9DGzWgYOfR2RvcgNCz3IJJv6uR-Rkdm97qgfssrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
