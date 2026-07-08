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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 18:23:08</div>
<hr>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=UM-4jBsmM2fSPhhatd6bMlVbQu4DH39d-uUUvsrbWXmPL1j8yncc3jOQDYeGue1N87B2hEiHhyL4oM3rWKpx-CgWwAlxzKywwK5Z_1be9mC3wCeU7nbbIN5vKVoc9DZkXrAtmCFWxMAjHe8AJQ_Fu6CyzcOEJgLpd0o_dwVYAhs_Z_Q7GT7fU3QAuReRn2V3pxRf1R8BLAvF183QLkyWPd1LrL-2qNHcAQpoH6o7HO2Wb9xp_qhkcb-h9TlM9bjj-Fvy7_Oh9VM2cTRZdJf51Y2Z1RoNHLdo2KX09BT1U77iW8SmwwoRqP7EMDSCSeXpgi_5lSN8ceiT2mEQXrtsmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=UM-4jBsmM2fSPhhatd6bMlVbQu4DH39d-uUUvsrbWXmPL1j8yncc3jOQDYeGue1N87B2hEiHhyL4oM3rWKpx-CgWwAlxzKywwK5Z_1be9mC3wCeU7nbbIN5vKVoc9DZkXrAtmCFWxMAjHe8AJQ_Fu6CyzcOEJgLpd0o_dwVYAhs_Z_Q7GT7fU3QAuReRn2V3pxRf1R8BLAvF183QLkyWPd1LrL-2qNHcAQpoH6o7HO2Wb9xp_qhkcb-h9TlM9bjj-Fvy7_Oh9VM2cTRZdJf51Y2Z1RoNHLdo2KX09BT1U77iW8SmwwoRqP7EMDSCSeXpgi_5lSN8ceiT2mEQXrtsmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=UOC4u3SGDeIPTJ-MzM5_IDOjqkVIdeQ3Oc7A6uIAkmrPuvtwZ0_QJGbYJa7HGGBjDTCR7DJyWt8ZdMBBYQ6D7gsm81q7aVMSHRQfWE0GTUQunRqIBulQrSp8NsBTLYSSpiHZFNJ5zpFrZsgqwW2C3rRyg5TDVT1EDb85KQGuBbeyf-_8cXNfGvyruxEomCRSt778bVBGrT26G4la6CKTNU7sG2d-1t7x5IjdYen9rLArwh4LOwT52tnn9R5J6XnQdXtiHlM9nIpSThFXieN2MbFVV7mLZqoxTBWGakFrFvWn-tND_oGZceWsn3qEs7c-IQe_ND61wslWqTBP7gEk8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=UOC4u3SGDeIPTJ-MzM5_IDOjqkVIdeQ3Oc7A6uIAkmrPuvtwZ0_QJGbYJa7HGGBjDTCR7DJyWt8ZdMBBYQ6D7gsm81q7aVMSHRQfWE0GTUQunRqIBulQrSp8NsBTLYSSpiHZFNJ5zpFrZsgqwW2C3rRyg5TDVT1EDb85KQGuBbeyf-_8cXNfGvyruxEomCRSt778bVBGrT26G4la6CKTNU7sG2d-1t7x5IjdYen9rLArwh4LOwT52tnn9R5J6XnQdXtiHlM9nIpSThFXieN2MbFVV7mLZqoxTBWGakFrFvWn-tND_oGZceWsn3qEs7c-IQe_ND61wslWqTBP7gEk8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=sIUCHYlduPx_HM4WvFX7f39c4BBRRln8kcipfwvCUJbe8HiGZ7vFsOs4ndas1ld7T1kgxs8lDmStQgFNYhsHwIN2aIxtxs4HEHq17V-gIMSWP6_oDxpLMhaV_qPGX9gxEEJjWTLWRE1CZFCIhRbnOS6dhbpmRXuGZp2N6dfExWgg4L9pjwoCQYkPabQlknjKTUtuB0nfgi3woWZgV6EUgH_JuJJrf208to4CSzyB2gU0Lvyoy_1scQUuuDd3ANlm709eF6xrwtImlEIb6D5ngSM9fQW3dQJ8TRso1LzSdYIoXQ8oUiORlzJo1P0Wn1rbD_3aEjTViE1VUcInC5Qc3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=sIUCHYlduPx_HM4WvFX7f39c4BBRRln8kcipfwvCUJbe8HiGZ7vFsOs4ndas1ld7T1kgxs8lDmStQgFNYhsHwIN2aIxtxs4HEHq17V-gIMSWP6_oDxpLMhaV_qPGX9gxEEJjWTLWRE1CZFCIhRbnOS6dhbpmRXuGZp2N6dfExWgg4L9pjwoCQYkPabQlknjKTUtuB0nfgi3woWZgV6EUgH_JuJJrf208to4CSzyB2gU0Lvyoy_1scQUuuDd3ANlm709eF6xrwtImlEIb6D5ngSM9fQW3dQJ8TRso1LzSdYIoXQ8oUiORlzJo1P0Wn1rbD_3aEjTViE1VUcInC5Qc3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هزاران نفر که اومده بودن توی خیابون‌ها رو کشتن!
صدها نفر رو اعدام کردن، هزاران نفر رو زندانی کردن. اومدن با وقاحت میگن ما اومدیم توی خیابون! طعنه هم میزنن!
شماها با وعده امنیت کامل رفتید
با پذیرایی و امکانات. حتی خیابون رو تخریب کردن برای تجمع‌تون، کولر گذاشتن براتون!
خود گدا گشنه صفت‌تون رو با جوانان شجاع ایرانی که جون شون رو گذاشتن دستشون
یکی می‌کنید؟؟ طعنه هم میزنید!
شما هنوز نه این یکی رو خاک کردید!!
نه اون یکی رو می‌دونید زنده است یا مرده!!
هست یا نیست! توی چند سوراخ قایم شده!</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Am6u4Rrgu8xe47049HkbEe2GoLeGK-hOZx1km_XKP_cO5A_miICtDx6qpu8fTBH8KRnTnQu8UfsRbhd25HZTKsKBFMIA-CblIRkYcYhypdXrIDISH-w1l5s9QY563aUY4DThQUI2O1Dchy6cAVnvWz7rHw5CLFc34suckFckq1NkwD7U1y_E143cZCr5H-b-7TJxQksbK78-PiXS2vykxRns5SzXys-oSm9lPZFjXd_nH6oLKvyvcR89r3SjU04-M4-nqwYVCwwt-JOgqMHlJ5EPQ74vwNSdr-fYCXW6ztPtm1FQoYt3Vz-7cAhbq9GQnC7ZrdMeSGdcF6SyIY-eSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : «آتش بس با جمهوری اسلامی پایان یافت. مقام‌های جمهوری اسلامی شرور، بیمار و فریبکار هستند.
آنها مشتی آشغال هستند.
به آنها یک هفته فرصت دادیم برای مراسم خاکسپاری، ولی در عوض دیروز به ۳ کشتی  حمله کردند.
آمریکا زیاد از حد وقت خود را با اینها تلف کرده است. اینها شبیه به یک غده سرطانی هستند. غده سرطانی را باید سریعا جراحی کرد و دور انداخت. »</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7ovzrxVJ-I8dU0bHTsxaUMHAD9037YNq27Or5C6n6uHtLKXZA4tOfZOFO6RVEJYiKlh26CFYqkUf386ktr3AkL8mFXwCAwk31gZJHYl1hIUchBwk_mp6pbLnFfsQGHLXQxkVyIxQNGoRNJQTAQaeMVAp4_XLd2_KjsYWAAV635Fy3Xwsvq85AsoKMib1VxzOJ7QxQSvO-krfSpZbi9Av6321v_a6qyuq9UpEjQ0JpKXWxHzjjsdu2FSc_2sei0gVqQp5iUm3d-hEmmA5RoB8r0Wu9uiNMog_8NrotCtEyqGT4yjx164VMZtPhp--x5P0CMSZi9FnISzm37ofUkLEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-T3JbhS1OaSDLTuHP8ma-AYCeP5Fc9-eyx5cUpw9lrSV_DI_6R0u9h3QUKZKrnXmrbg3R0kHxW0c4rkfk7Vcr2E9TbO3ji1JyFOxJKnZEf3ag-MFJHYnNN8-Jb8mBWi2R6aCLI-E-EaFtE-Iv7JJrZb8t8zr3TnO10SoSD9IaDJz2KDOS33ZnZuShj45EbVFX9sXFiE_mEwOepM4km7XYt0xMBk5Im4FBJMxe86fKcVS8XsnOqYhtCCY68Ve6MtdfR9sQmX1W9jxMTAoOniybraXSauOMZFN5pw5SzhmQ_hpc9FvIdRBTya4uo8BSfTrJ61UX5UPAaxekq9dtZBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Rn_8WCUJbJutyPrrsbMZMeVklr871nCBWKrfT0m9f_uqL8UzQqnbVchV9RocoskvFLnM1rzw4iiNr0iISQPQR9vyPozccctXPIFjwtTBjK63QOoM0xPtuCCyWD7wMVHUZJen9tEGNBIqI5P4WKregQ06eb_O08JDarZZvevzknG8qaIZacMCgnxUytnh63z2c1e43687SiVbEblFIgNPsECUmc0QIPVUjmzLrPyV3VklTcdOIoyzEdiyPpzP_H-WCr_ob5AgrmEJxeZLp4Nxu6hP3pQWEyUH1XnuOMe_pJ6KaMwmc7a7UF-0SKvjokXa1aR1-T6SzIg0VfeBmUEEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Rn_8WCUJbJutyPrrsbMZMeVklr871nCBWKrfT0m9f_uqL8UzQqnbVchV9RocoskvFLnM1rzw4iiNr0iISQPQR9vyPozccctXPIFjwtTBjK63QOoM0xPtuCCyWD7wMVHUZJen9tEGNBIqI5P4WKregQ06eb_O08JDarZZvevzknG8qaIZacMCgnxUytnh63z2c1e43687SiVbEblFIgNPsECUmc0QIPVUjmzLrPyV3VklTcdOIoyzEdiyPpzP_H-WCr_ob5AgrmEJxeZLp4Nxu6hP3pQWEyUH1XnuOMe_pJ6KaMwmc7a7UF-0SKvjokXa1aR1-T6SzIg0VfeBmUEEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBKg-ty4IaIv55E92wHPrT0spbDqZHW6T-RHCr90Wgi75r8AOqLn4g8pa1ATiCDH-fd1K4j4cNX7vF-cyGm03IoAML0W9XwfBA-jb-l4ZTnCuZoFTxR9FgjI_ju-QfWtCcOx6FFSoPkgh0YSEnwQdtgeyEPL5eLZiSins-VnZ7FUj_snZxCScw80JQbewK9N17-Fsc_dFFyV7ZairGE4t4zOkEbuFqrcZJS5UeOp5BY2bZwM68S1IUxd_9OnoYiAuwstts-VKanRrLs2W8-1z6uG6I4ta_ZaC3T0JMCdRirqh6ig8JuyZo7y-3y5zrB6ynpCsnmrnnAkqKnV0dO5lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=TOf9vi73uQoTX-E3TAgt0KYxfBX2uwopboROUvR9lW-5h8zAU2oYOJAJ5GOAC4MFAYiODtEapqBEBop1t_xzIvQzfxN2x4Eiiis_Qz_-zxEJScWsbIJDAFEaVV_TbuWD_3nHeLUWSPbVKh6dUMFMmTN4aAb9vnFqSXAAAtMe7pbzuRvyr4HCl6XPVnV51ntxI04q364p0RoL19HzFNVhcDz6oohLK8aGBvs8jw0CFPa-hEKHj_orKah98Upj5i0EpRI7mkMG_2ZjL18Ba-WnrBgq29rynMmEsVq1j630b1ZhD5mX7hLrKqsKogTucMrJluaKM1pEvmQ4gX_eB_qlJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=TOf9vi73uQoTX-E3TAgt0KYxfBX2uwopboROUvR9lW-5h8zAU2oYOJAJ5GOAC4MFAYiODtEapqBEBop1t_xzIvQzfxN2x4Eiiis_Qz_-zxEJScWsbIJDAFEaVV_TbuWD_3nHeLUWSPbVKh6dUMFMmTN4aAb9vnFqSXAAAtMe7pbzuRvyr4HCl6XPVnV51ntxI04q364p0RoL19HzFNVhcDz6oohLK8aGBvs8jw0CFPa-hEKHj_orKah98Upj5i0EpRI7mkMG_2ZjL18Ba-WnrBgq29rynMmEsVq1j630b1ZhD5mX7hLrKqsKogTucMrJluaKM1pEvmQ4gX_eB_qlJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdPbQyU29iMFSPN0LnUcVR6V7MCBVUAe7RHXePg_G3-B89XIjCMShFiJJKcagRQpoc_UPQn8ucirH0jnyq4Sm0XLA_x0Yq1JDrpKT0L1SnpWTTfYZwuF_u2D-KcJiITCrs9XlmaGi3JEzi08qs4GaoCFqTwp2wU4mFNm5_GQlOL8E2TqWKf9P4UnhQWOcXK2OaXFHXWf9tpE6zD50x9i7Su3LjbV0I2llN19Bt1gD96kaMYdUYP8RZveq0uEUfPTCl_Zj2GHf8N-wRd-N54qtGGBDoPI8gF0exR2yq7zISToGIYVjh6ytaJx8zuC-QpFhh74sWmSXNbzFQBdpQCSWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IboFU3QfYgGpXcSioiEW_DhlVM9x8mHY86IVdqEWempAJvB08Rbj9ncMe0fRklbWynUO4gfJfAvcmZabCb3LzLboIzGNRsLZqXtN5SdewlnAGtFd7YkqIgXW7Wr88YBWCX1Amy3uMBUwmSguVfVOsg0yjmnwiTu2unaK0ZNzllxOSIs1VtnYG33DZiomvOU9R5YsaU31lkhn94joaJB-GAoFtp359_92KNN6IRjtNnpPRYEtFik2Y84BImNO24dhoWaVjqcJS4TEpXTuIc-pAVOPS7MxRo_ibOBUOZBKryxbrjziK3Qj8lFuJBEPkpCxGqmmk-U7UQSyNGYUnFyfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=GimCSjU_DrgvXaQkU-Po-UGlpVHUGH-6cVrlHsG772zgy5IxKrF6gKYepYmZQGYXn2R3heZfiRllyMcuQHM5ONRxG8PaoUPYzbCPCmRawAMdRmPzEdOVZIwuPMCh9j80mjn3G8EwvQMECH1z-EKqDtc6Ca5aTTd4Px4vicgJwiP58W12W2OgGs1R-GjP7zK9bEtYZOLuC2garzxR0Bhjz51ZSCN7Z3BYn5hLG95moJqod4VOnUu5etWWyYQ840pgWwe2OEEUT-3-CT2Pa-kVDBDTEpmv1pglVTvxvv8ocOFAlpRTAdTr-0733QoLU6Pb1_mFgoLxVLKAZ7MF7qbV0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=GimCSjU_DrgvXaQkU-Po-UGlpVHUGH-6cVrlHsG772zgy5IxKrF6gKYepYmZQGYXn2R3heZfiRllyMcuQHM5ONRxG8PaoUPYzbCPCmRawAMdRmPzEdOVZIwuPMCh9j80mjn3G8EwvQMECH1z-EKqDtc6Ca5aTTd4Px4vicgJwiP58W12W2OgGs1R-GjP7zK9bEtYZOLuC2garzxR0Bhjz51ZSCN7Z3BYn5hLG95moJqod4VOnUu5etWWyYQ840pgWwe2OEEUT-3-CT2Pa-kVDBDTEpmv1pglVTvxvv8ocOFAlpRTAdTr-0733QoLU6Pb1_mFgoLxVLKAZ7MF7qbV0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xy3paN4MfD7MXSM5YFmE87SdGjtE0WySZ3LjIQD5-SwZVjqdc7Twk3aYJug3qWQCGqVU3WGthzfClOGSMUejOfBTPdB8J6rx1OvUJh8iDhWgptDtDzbJ-nb6uH4rxCdizaXFnLVGjQ_WqJNCQIjArPLahXh_nbnUWR3njhUokylsVNPbssUn35LNqSPyCB8J8HBSb3H-zl7cgZJiNkndip2mN6HkOhVxi4iK-U1AF9FJ2FKscaUoMZJfmc9OQBFZEPvYlkvrOImezpNXhGD_tWKlBHz_jw_TisqGd6eArHS8do9klASHwKQ1y1HjCssC5jFkbZb7rYlDr2_UbK52yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szD7uxwnFwF8BGvA5XCXlE5lKUe5OcRSQAwGIqDLzquW5lnX-D6bB4MaeiUqPtQ9igEDcK3EwdvUUSDpYU8WcgUuxyweio188UnMznoySed1c4QYtAN08YZ5Nb3FcutxL5MnjAcypY7ggghn_4gYfPN5BtX-GqSONwvxPy724FIbNwMKgzBaTs2N4-cohqXp8OkKT2VRmILsqn9mNWB6IGJBXLq4DmXxuJJUxAukpxpcX5hcezfIMZTjfePx8ApFSCpZNik1WVryyQ-pofhnmcfqzoe8vLY4OLmMnrcBf5lHCLPldOMLNH7r13_ZtiZdKOCeykUppKD_ls-TG31Lcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-hIZc8nApXH_E5IEZGhfZQUbn-IMhDHepL8qE8GErsAozf-FCnHYE4jh_k6zQM0n2YYUJ96zJXh3BTNhwbINYdkq21c9S97uQrJp3a86SVXFwpxANnZL_wB3zxCEbsAbi9u-uQrGHG3uhvtoOoarQpeB9FjzVMNKjqsD4-WqvtGNTtMR5qAdP3XAEGol1lrbmTbDw89e_9PKcw5FIeiRlsaK2aBrL4--YAwy27jIC2c4dyfLbxW7vR2IpFmx0IjsZc6w2pBzh82u-1lS9OaF190-07F-6oA1tt1SHgNqf08jCabuLAMkcSZtDVRRp7mRxkNlvfB7pMFlwr-AO2aSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jj81M9SJJ7DWS5ESy0gDmvGC1i2QzZqcTyTKWGCA4Boax2uABAqgcr8-Nxk260OuRiQnzF05JZ_3_6FM8s9yrQvBAkBLFeEws3v0b2UO5RxwDMegeDoHA5il7cCA8VJLqXDAakjso9XbAfhcZO2RdJ1kVmaxqZ2nq1qkZitA5dZuhxYEn3Gt3mtwuHMsPfLPvY-YofYBIV6fd7rzr3BLNhTldtTocFZ1SoEQNxBWU7eRcffDGjV7FIidjc5Vwbaw6_vHtfAqbu-qs6-9W-I8-kK_L3UogUsN9PU-MZjjfxyrBwxpNHugp4I-WJXiAr5MuL5IcJk_XRoEknKUFxKbRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QEc8VmlgImpX3OTfgB3sK-GnTj_sCjiRiTkQHMoe5byjQi_oC55uVMfO3R37O8Fez__Jya9H9kx92eTnN-l3rzL2LJIkt3fcXSFbebc_ngmI0UAW03ZXBa0PRUF-7OJg5S-3XbopmIbPJ604UZL24eSUmeQqSKsHsbFR998q8a0CNff__ZgApOIHWFn0xk-jrE1zKH4NUdxGpO-81hRi5fek0yhXsmYij105tYBUFPiDqW3J42taYFUHSmOGrjebEiugyjXUlf77Zu-JcktTDw4itSh8M8-ZOqBuS9nnVpWEkku_Pct-458YPavqOAsF9xQfELMAGSc0_wXrEERA6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=qfLb9J76t80Ca_g30D2m-bm5RKfq4dJ4nySvb5nmqazr611Ww27fMu6X-DAT9eCITqdCOlPWFOsLV8fO8eJTsCk-A7lHPZWmuox6tUTR-IcPCc-d2y7Skl9ynmZ4Wfcdxjh1y-08BLmnt_UdQOMuln1WXZU-bJH2tIO-y1RTfqUZFuW03cXoU87OiBNPUl1S0fpHjyGTs0BkwTezMMYMDHAVVh4BMurP3ZJrca7jKyLY0AFqYbikbFSlRxyaPCx6o-O6EbeM95Wf7KRXIKAzXK-dGNexvUuN7KdYefgXLt-4Z4MaOKOb0U2hVMDvFS78X6xF2EmIU45Ef_Y6YmpOSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=qfLb9J76t80Ca_g30D2m-bm5RKfq4dJ4nySvb5nmqazr611Ww27fMu6X-DAT9eCITqdCOlPWFOsLV8fO8eJTsCk-A7lHPZWmuox6tUTR-IcPCc-d2y7Skl9ynmZ4Wfcdxjh1y-08BLmnt_UdQOMuln1WXZU-bJH2tIO-y1RTfqUZFuW03cXoU87OiBNPUl1S0fpHjyGTs0BkwTezMMYMDHAVVh4BMurP3ZJrca7jKyLY0AFqYbikbFSlRxyaPCx6o-O6EbeM95Wf7KRXIKAzXK-dGNexvUuN7KdYefgXLt-4Z4MaOKOb0U2hVMDvFS78X6xF2EmIU45Ef_Y6YmpOSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbihdM7fzCb-Vf9y_56g4kcRID-J-Vrv0o1DcEZA07svXlsh7iDGqwf53C63v9qmgDA0B0BAmRO6eu368PVt8i9zmcGX1n9j8C0CV396S8nhXC8GGrjWMFVB7L5Iluc2y80pO78XHMYD5guUfAz2Fl648uHTInXo1fvgvjM8SCudoI5CmZy-lqGodOOfkFitpXuPbxxFX7ZNqu2sgTxjvTtB8j4FTmyea7nHqmpw_mb64mw2BLvDeW-byLQ3dazvENkq4VNuVBIrdjJzPAXUOHtecU7cvU2xMLAUU1jJKLO0s29Mv6uwD7qFK6KkQBtvM3DD7iNpjiaFYhxHuBf5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=tk_Gv4rdA8GPBhTry4Q6WcI8xZsKdbH9K7ULdqCIDjJMX3uOP4AYZbXkWEcRHvQ8DWh72KApGr8cbF9_g9whJ0qbsvDg6R0qVMbH5mx_UQ5a2YBeUZ8xwTDAzOTyQzGQffoq3-813aKfGhwUx1Wqsn38W9FsX1pRdD7OdHVgA8k5FZBUPewceMWmMqYOtMZ9jBca5ERMTSOLXXyzGUTr0wknUcgGckkIud6tJsh6X2NcPiGwOnXnex8AOmwVsMQKYPgi-oG9HvmS-rhfHfmoy38_7UCUd3-xRsUydsyRBAZh0bPzrkiF67R0opSIOMsPqBH_Fbx5ZCiOYwSWOmiilg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=tk_Gv4rdA8GPBhTry4Q6WcI8xZsKdbH9K7ULdqCIDjJMX3uOP4AYZbXkWEcRHvQ8DWh72KApGr8cbF9_g9whJ0qbsvDg6R0qVMbH5mx_UQ5a2YBeUZ8xwTDAzOTyQzGQffoq3-813aKfGhwUx1Wqsn38W9FsX1pRdD7OdHVgA8k5FZBUPewceMWmMqYOtMZ9jBca5ERMTSOLXXyzGUTr0wknUcgGckkIud6tJsh6X2NcPiGwOnXnex8AOmwVsMQKYPgi-oG9HvmS-rhfHfmoy38_7UCUd3-xRsUydsyRBAZh0bPzrkiF67R0opSIOMsPqBH_Fbx5ZCiOYwSWOmiilg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=MseYgFp9DynGfSXkiMCH51N5JM-_Ilc-7tHnUgf4mbCHl28TYQoERwW2-ejP9WGVFyh1U-ugjtn_ymLB4X0rR4OJvCURi7541ufEEV52mpHDnjtPM-noQX4WgpAzmET97e4_SzyXjGKwUOGESHqPTw__izuSoi3-m0_sV56GL0_Tg9npNOwTqeWcSj4_rDg1i89NovWF2-LM-hSMNgWylzYcC6YHNrugRM8EUyNYkd9TR5mwkzp7J0_d39dVVQFVC57AQIvvvL6hT7i4LnW2-S04P5gaN5ZAJ_VlHn5wzp6Iwhk_LcbdcJO9KypsmdAvae8L4HMlbgamW1r6dbB1GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=MseYgFp9DynGfSXkiMCH51N5JM-_Ilc-7tHnUgf4mbCHl28TYQoERwW2-ejP9WGVFyh1U-ugjtn_ymLB4X0rR4OJvCURi7541ufEEV52mpHDnjtPM-noQX4WgpAzmET97e4_SzyXjGKwUOGESHqPTw__izuSoi3-m0_sV56GL0_Tg9npNOwTqeWcSj4_rDg1i89NovWF2-LM-hSMNgWylzYcC6YHNrugRM8EUyNYkd9TR5mwkzp7J0_d39dVVQFVC57AQIvvvL6hT7i4LnW2-S04P5gaN5ZAJ_VlHn5wzp6Iwhk_LcbdcJO9KypsmdAvae8L4HMlbgamW1r6dbB1GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Io-UL_N97Lf6EcsTCz2NQ_INZnG7yZRkBFFEV8RA5q48JDNssA_i9hLLLE7osGX0DfxyuHOkcrbVrbbPLWQ4TWOOA3IGFrjuJC-vN-3pyG4NgL4irUqLJ6Ew1s32CkGF51Dm89Ful50O-GoY70foK2lBqxBZj_LMidxILrX100uMwIsbF-QDSpwm7kJJPPWUg-cSJFxGaeLxLqkHDZZ0x2poeBMWEmm7Y1q0-WJxAOwzuwhnG7mEIdbPfI-Efg_NvVgtTWZUSRvYnTOdyH5STNl-2b0Z2ks5JHMjUa8cw0COD1Gn7IyZ2nohKkRmqDVu4FzYevhiLW1NvXIw4xP6AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=Wj14YfWrTfnm9h8TaS58ougn2EhhGz0boTUkYG-QRRrPthSbdPouupow2mCXs0QKNuo5sUIMW3HCpFDmZtDKQgyatc7SsUUsJjthX48p7TndeAUYBh_bF1caJ1s7PtC6jQaWP2TU-qPdApMzjipKfX-t8HABxCa4NS2MkQ11U_Z82uhaPlf1q7z4iGmdq5zjx3JLW9VQfQo7RXOVM9doiInHLIwCtOU_hlbH-SrIgQ6v5SDQOGEzok6obtFSA5Q9A5-0SzD7f986nIoemUa5iQgTnCIuR7m-EW40fOBpvtadp9u6J0jKopDfIQt7jZwaHrbYiLdwwpE3uYViDPMBww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=Wj14YfWrTfnm9h8TaS58ougn2EhhGz0boTUkYG-QRRrPthSbdPouupow2mCXs0QKNuo5sUIMW3HCpFDmZtDKQgyatc7SsUUsJjthX48p7TndeAUYBh_bF1caJ1s7PtC6jQaWP2TU-qPdApMzjipKfX-t8HABxCa4NS2MkQ11U_Z82uhaPlf1q7z4iGmdq5zjx3JLW9VQfQo7RXOVM9doiInHLIwCtOU_hlbH-SrIgQ6v5SDQOGEzok6obtFSA5Q9A5-0SzD7f986nIoemUa5iQgTnCIuR7m-EW40fOBpvtadp9u6J0jKopDfIQt7jZwaHrbYiLdwwpE3uYViDPMBww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I47yRGb7XA0On--mWFDtprW4_9fyFTjbkZdzbgZvr_O7xQR0aSh6N1A2hiU7BSh8wk67Lq29IoktOt9PhfYkf1nFMnIpEigHi1k8-iESsG6nBCpOOg8P6U7QL3tXwmPM2wi5lkTAvnPXNny3zVumc5zljbm8O3euOo7l8D_v7oQ6fouvoprp2nv2eJR65s-czhUxnXw3_jGPcr6csxi-G1V5UT-NPSQFM-WLsOclFCr33bJ_N1jgbXsn3qNbiCDAeoG5qr31atBHp5K0gvyFiOo8LmxAS41MtWppD5YLm_Ws8t9HJTVeDh7xoq3cKYx-ks4SQdrB2jqcU_Li8yrR9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pETy4ZwXB02S-SzKO1zxR_1eXNOq95slxtcEBCUKqGtXDbhlvhS7uETX7o211MePMenGi59jfvuTf__tgerpbAv-bwrPVI-moOaUXPQGDj6D_QGqiRsb4IXGiaW-xx-cLhgSoPdPMTkXzZpoe0hWgc7d1lR-quWslTtMIxjc6GWf3yvaR-wxOSup89Bx_h_jn30vOGWBav0-gAxpZQrDMalegmxAZCYF8GSV8X9LKVt7-XSV10NIWfOJwEX4n_G2XO5Qepn2RbxjQF__nHW7lecniyOBgMnPh5gcH2MwYJX00xv9H_MG-Pp1uNDnASNdCNjwNhI68Rz5K3pJTli3DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acYd0eq0rMCo5vhWYPL44aolWJ5AVgGrVbLtRVLrHJ03N2NfzD6H2461GlbC4X4pvHk9LhB3wrgrqRf-oRxqzNamRX4knybaiNzZWATx2P69DNiOBkxnKn2NVXYOZejZJhwkzo-7d1WdvztzlRpFjQMFXgVnCDPNV-xYENB7X6OOV_2o827yKUqUe4FbSz7QjEYyLKL4o-_xkyDiVb5cVDLtTMx8dR4G2X5dh4Yd0af87sgB23lFAeU7PBNh8_Bi1E9FOJAKaOviJkrKMP12rl_C9HWo8OxSoUzo04nYs5WfhEf26q6HNe80akk-QPFWJRRR5uTcskah6BnJk3FXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcoA-ZfufKJQQPfTsHcgYowgE4-ziAcaWeatUqQCJenfjkvoLjQCp6F7aGplh58ESS_iVlarjmuk-MWFEmIknjiLWcz9HQBv1FEgaBx1MwgswL0pQZ4BnU64nrad7tQO_Wk3z56nEuFWylBmGl_kd1H-XHQyfNoHrVkbC9A1-iUAMQioOhRRO_PMoFaPENZ7FLhaP08YRYCIZ9D9FhFT2xZ9Rh1Ko5-hEaOEjXu8qPo6z9nADZ55H2AhEloU_7Ovu-ZVN5PxSfRPLOmUYkJO5UWcSKR0ya7-PASfC5rr1MJGEqH-f1RNqTSKV7U4fvfXFCkpt8XrW_bYIkN9qEWOHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCwHU-meMmzsAetyrQJENZGX5VtXKC3ND2R0Z0HB_D_WLWqCtq6jRKugy48Qz-7Sy1gz_zmXqhdjpMhPR_uP5DO-zbreiyWx4_SGizDhB7tXwFlTwMbN6666vsx2CYOsIGl3l57dcYi3SkljYf12RZhn7jdtX1PLnSG3eWOGTFASATKntSabTFcifo-j1cLk8_bNFl3tK4uUhNq4F0IAg5d3uEE4jy1hiwrpQw0T0maYRGwhuM1C1mRJ4DMrcmFozNyn6D9niXLQ7VnPN5WlGr7VNniSxoVKK2e9X0gQbvrMZmEFu8mNapuHfiw--GCpD6fFA_TsuaD0FwiEu-zRVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-wrN9nGui9RJJOtiDx5J5Svl3H84CjbOKctf5vtlQ6jR48mVxANkuHxkTRSviM29SKzdmf60l40OPloRIsoFPHdk8xWWqmVTxKjC-6X5AAhV7V9CEouo_zp8fZQKrUqWTzS_Og1_y4iFBi7TknF1ygXaZ3i3625gw5j0zahYsab6UxNlk8rDdKXPbQGgkGI6FgyyTe7gB1xxPp2wrJgv2uwvEPIAeurEcrGjv6aKxbTIhiYip1OsmOxNApLsIYvj6lYdvb-U8ZVr48J__5MVaw7o0QMG7xxRtC2lnpiacv0IsJy6M4c4P_lFk_00sp7vXq2XVEm3uOkWY5-BMfz5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=vFQEUr9CqqRofLNkMhVqQiD3xrZHIXCVw1YKlcGjxPtfib0rRvSrduKQ_pTc65OL4dejx1SyiIXoYhEVW0toH9tnx-Cro1oCBEKRs5WRkcadAyQSxaKABCedwoUT318kO-LC5vKUFwmPoqob2JYwXCqIkLfpLLKabcG4fNDnrImRdNIMTcWZrRpz2HntY6lFNAS2w8KdBj8_fK5IHLQozQ3aLCZpGKGVmh6lygZv--2VZl9WxSOBuQ7KQ9T2NXKUqNFxYcJeVP-CgiC7_lc21WqkPq5_rq7LTTY0rKavJ5SJluMbB5xMztAvFlV9OZ1YuX-sJi9pLhR6QdkwZnW3gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=vFQEUr9CqqRofLNkMhVqQiD3xrZHIXCVw1YKlcGjxPtfib0rRvSrduKQ_pTc65OL4dejx1SyiIXoYhEVW0toH9tnx-Cro1oCBEKRs5WRkcadAyQSxaKABCedwoUT318kO-LC5vKUFwmPoqob2JYwXCqIkLfpLLKabcG4fNDnrImRdNIMTcWZrRpz2HntY6lFNAS2w8KdBj8_fK5IHLQozQ3aLCZpGKGVmh6lygZv--2VZl9WxSOBuQ7KQ9T2NXKUqNFxYcJeVP-CgiC7_lc21WqkPq5_rq7LTTY0rKavJ5SJluMbB5xMztAvFlV9OZ1YuX-sJi9pLhR6QdkwZnW3gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=icOsCa-0bbN5lZXOHEjrTVpiVxvY-g7VCkejb0k8VfCu8JxhifxtcYjq32H31dwxnuuZMxm8jc8FngvODgFJ1MKwmEFqTd7d6xUBESRVhyhJnxC9-HT9OxiGXj9_RyC-uyAzanhVMz52SLZIbIWhnASFZeM7Ofelywm1iPXheDmUXmepRq6QJnW_7MhkaMZ7chTD6aqG5TVnkO7jqhtln7bFZpjnuIojeivUWH6wDXAyGr9DVl4wUwFELA1VUntEQv1Z-o3nYU8VErp21lpxtNLw63NNvk6cVNFBDvOShg5X_kgISgEb_VH9fyh10yicJyVUSQQ0H7dYr8-OIgQCQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=icOsCa-0bbN5lZXOHEjrTVpiVxvY-g7VCkejb0k8VfCu8JxhifxtcYjq32H31dwxnuuZMxm8jc8FngvODgFJ1MKwmEFqTd7d6xUBESRVhyhJnxC9-HT9OxiGXj9_RyC-uyAzanhVMz52SLZIbIWhnASFZeM7Ofelywm1iPXheDmUXmepRq6QJnW_7MhkaMZ7chTD6aqG5TVnkO7jqhtln7bFZpjnuIojeivUWH6wDXAyGr9DVl4wUwFELA1VUntEQv1Z-o3nYU8VErp21lpxtNLw63NNvk6cVNFBDvOShg5X_kgISgEb_VH9fyh10yicJyVUSQQ0H7dYr8-OIgQCQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=TnTtNdvi7AhGzstIAr28xh8JEjdqjaGRxl-z0Os5Mo9PTGGXFAVV5WNC7AOLJhmkBGHj5VfNXDa9JH0ihEJ69RIQRAcaYydSIw5818RK-JUyss50ydhtK51YQcDULosfSzA5zUjCm0P50Mw0Hqe6oX4rgV_pHfh6NHYHXg10Jbrpd4nK_tmbuRZBnsdn_j_nKLV96NL-RcX1oi4aLW0t5HV9_5_9KHwmEm0fSgWFku434JlJrnFwA9RUyd8AZ0n2U3XX-xI_mMSSXSou8Tu10_hxBzpxldsYRS1eW8D4NHvcv2ZDS_F4aPyUBqF4h6hHuGSBtMx5_LLIvsYLJPUPFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=TnTtNdvi7AhGzstIAr28xh8JEjdqjaGRxl-z0Os5Mo9PTGGXFAVV5WNC7AOLJhmkBGHj5VfNXDa9JH0ihEJ69RIQRAcaYydSIw5818RK-JUyss50ydhtK51YQcDULosfSzA5zUjCm0P50Mw0Hqe6oX4rgV_pHfh6NHYHXg10Jbrpd4nK_tmbuRZBnsdn_j_nKLV96NL-RcX1oi4aLW0t5HV9_5_9KHwmEm0fSgWFku434JlJrnFwA9RUyd8AZ0n2U3XX-xI_mMSSXSou8Tu10_hxBzpxldsYRS1eW8D4NHvcv2ZDS_F4aPyUBqF4h6hHuGSBtMx5_LLIvsYLJPUPFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=R6fc7KJi5URjkuMWc08qK8ZU52NSjqwvJuw5GvwD9RlxHAg7cQ43hv6dg874IYwXXst3mAM5HBNU4uidW2vR4jrodAMfwixpBXwjcL5og_UbDnc2YxLoNfjd9MCNZMnBtLUA5moCK27jsPOBrt6spYcbOz3Foizb_Dk2zeLMh8muCNEk1EnEwjSs7ylQfsJqxgh08oRvd-8-EK07FQphIOoK0nK8ejU_-A1Ui7H6AvUhmevEikKwWf1tqEd3TDnFo1IqMC4mbt7eHKQnqz2uiHhFdcsBZcuvq_O2lyarQ7FYL9JZkhvkwHca41hcwMOjSShJ3rOC5XkniyixlzojKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=R6fc7KJi5URjkuMWc08qK8ZU52NSjqwvJuw5GvwD9RlxHAg7cQ43hv6dg874IYwXXst3mAM5HBNU4uidW2vR4jrodAMfwixpBXwjcL5og_UbDnc2YxLoNfjd9MCNZMnBtLUA5moCK27jsPOBrt6spYcbOz3Foizb_Dk2zeLMh8muCNEk1EnEwjSs7ylQfsJqxgh08oRvd-8-EK07FQphIOoK0nK8ejU_-A1Ui7H6AvUhmevEikKwWf1tqEd3TDnFo1IqMC4mbt7eHKQnqz2uiHhFdcsBZcuvq_O2lyarQ7FYL9JZkhvkwHca41hcwMOjSShJ3rOC5XkniyixlzojKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNtXB56QBucXso9-sfyEd3qD0wOoy7OeuVUglsx_ZGnSwsCGLZvMCuvXaCusr6W_pVb4WLzMyMR5R08sBix0GN_ldZjP5yqsBZFX-cI0UL2ZOd5XNlt8Nw5jcbRBxyV6wSO4TDGeXb1kQHxDAabBVaG2h_2G6vY55oFqRRozVQM3Gc8-MWVZOtsODfAQ-WXlkRY3cIsRMZu3C25t6Wda2tXoRQP9sQvC53ByW1SX0Rq0RiVI8okkgxxLLkUvB_kgMQ1SttrNs7TRJOSsbwZEQRoqFyvlif1vRQfm1YWdbp2ybDOlmMafxwYhkojilvUkwK-B2DA0Zr9ouppVpMmzmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=HaeZUePJ1lojoSm8GF51azkom_MmL4t8iNL81a-iJ-rWB5b64CubzUze7f2LVhKumtOzBhJDwg6CBOxznribK4BnP6a-9cd5IxhWWPK_kpt2EYqRFqGt2zS_w2jAyo7P-1plKwDFeJZrGx7WsCMHaRMB-nO97ne7LFd4qqB2fNaU0iHwm7463spsRBrhY8r-O5Kl2SLTulpgK97Y0Nv34wsSTFOxBaukl9LjsTcJ-J7DtbMfmXNA38XNVGp6642ma-KXv8cl0eS5XqHVniPQ46bZMePeAEYNW3pp4LGTv8I7Njyz7YRkc8Hx6NcvShbu9PDckaisTJ6s8epoMGLAfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=HaeZUePJ1lojoSm8GF51azkom_MmL4t8iNL81a-iJ-rWB5b64CubzUze7f2LVhKumtOzBhJDwg6CBOxznribK4BnP6a-9cd5IxhWWPK_kpt2EYqRFqGt2zS_w2jAyo7P-1plKwDFeJZrGx7WsCMHaRMB-nO97ne7LFd4qqB2fNaU0iHwm7463spsRBrhY8r-O5Kl2SLTulpgK97Y0Nv34wsSTFOxBaukl9LjsTcJ-J7DtbMfmXNA38XNVGp6642ma-KXv8cl0eS5XqHVniPQ46bZMePeAEYNW3pp4LGTv8I7Njyz7YRkc8Hx6NcvShbu9PDckaisTJ6s8epoMGLAfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enAruS9cRpNV1Lm7Z-8o7Yy-bp3W-qdUlK1a0OryaChEdacKa3riiUzFWKTRUGxJ9ug55PTv3j174lD_sFYgAcht4PHZIVqI8bRdw-8gh4nCrwPxDU2Ayh3YK52ibe3W3EKUVkHpHCui94hX3Db1KNTQAvzYLNxifLoOPYORwdzz9QCkozoKnL4xZRYtFXGfYvsySITZ5HOzjZb-3YFtBg9vO4bk0AsWRLimB2lPK3kIbjg6veKkBkWTCmHU3hrySFSu3XQuHRO9w0W71jaz1nOjumD6fM3xuOg1Ms1l6l1KYQkBuQds1TS3f5hmnQSgkbduToZBreDRiLqWiiCL3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=Tp11BHqYtfURjHr_n1WaL1F_lMDsWkz6Ye5xObmqyZZ7_JMssbB7kwQGt88PNl6z2sOtzEe0Zu8fQLbA7axRJODUFOyXgkZrVb_Kn9nK6H5C1wIBUzF56aORC1n4BSvUzTp0w5CujTqBMlWPb8AepC9DBxhujIeE-vF9JchVq0bKnbmVpOmvqXJeb8Pf_5HdBB7iVMvWfkjfAyViH0YTbDyomCAXOKPiqI4g0X_poxXx43cLXRRvILgrhjZZKzsiPho--PnZ8nhScuU3sFjhrVW0tGlP1KUErh5pb8qMFQS5yQu5NSxss5VrwMb-zAjORGS7M0_FH37tO8WRQ5IZtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=Tp11BHqYtfURjHr_n1WaL1F_lMDsWkz6Ye5xObmqyZZ7_JMssbB7kwQGt88PNl6z2sOtzEe0Zu8fQLbA7axRJODUFOyXgkZrVb_Kn9nK6H5C1wIBUzF56aORC1n4BSvUzTp0w5CujTqBMlWPb8AepC9DBxhujIeE-vF9JchVq0bKnbmVpOmvqXJeb8Pf_5HdBB7iVMvWfkjfAyViH0YTbDyomCAXOKPiqI4g0X_poxXx43cLXRRvILgrhjZZKzsiPho--PnZ8nhScuU3sFjhrVW0tGlP1KUErh5pb8qMFQS5yQu5NSxss5VrwMb-zAjORGS7M0_FH37tO8WRQ5IZtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=QWsr8rK29xyG5GxV5iHVBF-SJ5DNfWEFWVsojfKfDb-R-XnFP0WIIPJW15AXChlQ3y4p7FG671_V7pWin_rMFGP_nhwIWq1XOhnA2sqYuL_MBPFUAvLxW8u9HSHMrrOKtrsA27w-cTWLDdOEbSpaVtMPt50mv8Ji5cKG02LZNTc6e-GqyLnCtORJpbxCsndiOVlSNJyF_xDds_T3ecSM0c-pjOAc4oKDvzHs6fvcgFnxEY5jy6Qp-Vp7vYA4b4uKzOPOnpODrzPQYvQ4fM_cDhPbx5gw0zvNxOd6KCDa4dSdWXbHSOWa4A4tWsoWCJChPCyEVGi0Omes7PwADq9RYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=QWsr8rK29xyG5GxV5iHVBF-SJ5DNfWEFWVsojfKfDb-R-XnFP0WIIPJW15AXChlQ3y4p7FG671_V7pWin_rMFGP_nhwIWq1XOhnA2sqYuL_MBPFUAvLxW8u9HSHMrrOKtrsA27w-cTWLDdOEbSpaVtMPt50mv8Ji5cKG02LZNTc6e-GqyLnCtORJpbxCsndiOVlSNJyF_xDds_T3ecSM0c-pjOAc4oKDvzHs6fvcgFnxEY5jy6Qp-Vp7vYA4b4uKzOPOnpODrzPQYvQ4fM_cDhPbx5gw0zvNxOd6KCDa4dSdWXbHSOWa4A4tWsoWCJChPCyEVGi0Omes7PwADq9RYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=WsZt3Sh8bDH-j2dpBs8RW28Zhnk9Qx4AF9yNNnReR7us5PEDmDe07amw8eujJMhytcDkVSyWe4SXoK8Wre6CRyxiY78v0C2uVpcfMzO6Q9g1_LxbWnyu-iJmrdSPnZ6Uj0WdU8OYrNe_c6vekXJUbjAn8zfkeYftCqOF1kC2RKfedy4-IK3JqPCyJPz7YlSZs_SLwh3h5nG1p490L6g9G0Tw2ckxEi4lTjLHFmfFnl7ZJFBvmPOqsfOMu_Rzrb99m8C5pvtZhxeYE0BA2u6s9fYnY6mEgYWCs51Av4ixyrDKfKJw3Wt8T5rTPyI76kAhGKOyQlMWbNTcearyJ4ApKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=WsZt3Sh8bDH-j2dpBs8RW28Zhnk9Qx4AF9yNNnReR7us5PEDmDe07amw8eujJMhytcDkVSyWe4SXoK8Wre6CRyxiY78v0C2uVpcfMzO6Q9g1_LxbWnyu-iJmrdSPnZ6Uj0WdU8OYrNe_c6vekXJUbjAn8zfkeYftCqOF1kC2RKfedy4-IK3JqPCyJPz7YlSZs_SLwh3h5nG1p490L6g9G0Tw2ckxEi4lTjLHFmfFnl7ZJFBvmPOqsfOMu_Rzrb99m8C5pvtZhxeYE0BA2u6s9fYnY6mEgYWCs51Av4ixyrDKfKJw3Wt8T5rTPyI76kAhGKOyQlMWbNTcearyJ4ApKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=jKM-ueIs8FhtxLGIeiKf5Vqat4cEcfqOZvWiT-qtypQtaknzhcSMMu3FpMzL95lA0O5hDNZ-6OGJspn9ob3SVEcBS35Tp8JqVQLXK3A_fxW5fi9WJBZzmahw0GQQx2biMZ9KRjYefzKLnRByYZkBR2HoUBjc1BNck8piVBa9rUO9TVwK9sIMnO7h3rm0SnRYjmc4c7023WUIgFzLcBCsunLu_SkIcwjkCEacAVqrzyvLqwqMAPWTzoTRqsp3vCJ5w53dPOi0ajTH0eCecaJumwsUdpalh22EYU6a25LMmmuNZBQHMp7l9gAAP1tV3RHHUALFpFwAbD1fnoN76xQpMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=jKM-ueIs8FhtxLGIeiKf5Vqat4cEcfqOZvWiT-qtypQtaknzhcSMMu3FpMzL95lA0O5hDNZ-6OGJspn9ob3SVEcBS35Tp8JqVQLXK3A_fxW5fi9WJBZzmahw0GQQx2biMZ9KRjYefzKLnRByYZkBR2HoUBjc1BNck8piVBa9rUO9TVwK9sIMnO7h3rm0SnRYjmc4c7023WUIgFzLcBCsunLu_SkIcwjkCEacAVqrzyvLqwqMAPWTzoTRqsp3vCJ5w53dPOi0ajTH0eCecaJumwsUdpalh22EYU6a25LMmmuNZBQHMp7l9gAAP1tV3RHHUALFpFwAbD1fnoN76xQpMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn4XJB30G9eVUXZppPV_Yg0i40qDG_wJ7iwiDWd_z2A9owlY-8FXqI9zUGExHGgKL5XBZJR4fytG6FeTdXe5QbOKhrnqrUZUAvjgFCpxI6707sPDa5IRXs0tilTrS3s0Gsk97LCzrTEPxFEfU2DBTC9nxvZxGb9BvtV-wftInCWKM-SHDCXJMBszNA7Ix3EY7iybz1I7AbITZJgUdZ5rNJiVq0sv7dy2B_95Apyma3OUsm_RlnUKhkZFHkcJBxl7NbthpmKEmGUbrRrjCcD6YaZxeTAz_WxGvRYYIK_06qGCYFqJIW2AkUewWVwQjtapwaQFpPwNk8q-cdyJ55856g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGwjqPOH-hw5Z_PIEFp-Avc_iqQemNJNlNVDm1yQg6QgcBgf29iG1dHx6xPKIBfRdfqcRM-uCB2BWdDcM9scJ6NdFDs1_1uu9bhOD2Kueu9GV_3Gb-R8J778UnA4u_F9uX9re99dpM99LXNiKDDpiYV_RgzhDaVZ6wiLyE1oVde8YtRF9qbenkxN-A277lutQvvMWCtACdOnKT_WHsl5FzzKHjfI4QmoAqFB9vEcPG7PS0KWH1ctWl3VHTqotScv8GGPLksMkLJFGeXxw5aTf5hC2a7r0I8rtD1TPw1k7UhOuuNRJ3rY9d7bZK4r8O8H_91mwMazi8Xshf62yMvSAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=P3VZRbneJA5i68-mdUURmTbdV54i2S28hEMYvX1IE00kczkeXO1SrXht-MiF3NSjymbplC996XZLtfrhIfrF11NlAQXBpgPlUp5xyDMuCBkwWPwKeC9YTaX8J_SXmoWD52H1TYHjun9a2uHR8YmUqzPjjFuhpq-NVMebYl6zqTEKivdCDvSglyKDlUi7qZenuYFROzcJqgCu8O-0qeQO8Y4cKndl1b_v8Gmr5kolGL-HfxeLsmlGjzwVW6wN_xgsURzoBVEp3q8xiq-lEHk8GU-ZsnfO0Jj3CeDq3U_uZkWXi2vM2WwhcHkp1KcSw1ov0MsM5gTc34T7UjdtRoPkzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=P3VZRbneJA5i68-mdUURmTbdV54i2S28hEMYvX1IE00kczkeXO1SrXht-MiF3NSjymbplC996XZLtfrhIfrF11NlAQXBpgPlUp5xyDMuCBkwWPwKeC9YTaX8J_SXmoWD52H1TYHjun9a2uHR8YmUqzPjjFuhpq-NVMebYl6zqTEKivdCDvSglyKDlUi7qZenuYFROzcJqgCu8O-0qeQO8Y4cKndl1b_v8Gmr5kolGL-HfxeLsmlGjzwVW6wN_xgsURzoBVEp3q8xiq-lEHk8GU-ZsnfO0Jj3CeDq3U_uZkWXi2vM2WwhcHkp1KcSw1ov0MsM5gTc34T7UjdtRoPkzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCOjb2GJji9CyztIEaKrhTCngqpyk0hoJc252sNJ9laglfyracsyecoXBC1jGux2rnjqmMhCa-NH6NyYXplvdICqIPHw8Nh70-eZ89CGqFY9LBSTx37QzbLaN0-pjLLphQsUc4hfRqHQKDOmvDe9COjHa2bV0tenXWv3lX6bLXMD7zTwIIa2GWBkCmQmpgtb8RhuV47S4D4sZGzEuPdQ_eroXSNNsSbKf6xHCTAxsXOhG5KXQ1ewl3S4-Ot1zWI_WLFwXkbfz67aV4ne1krpf_yU5WtSYz9ZUKCU309zb8r4O0m9irlZM_nvPwviOH856sbBIYajDYlYtWq0fzdCTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtSvGKaf-J-Y_lfFDqz0xGy7SXraul_nWwZSwlPoOgI60NhRpyVNpnxLx2aZuqp3cgn8dyWNPT958bCQKdSRynubDGlloN3PXZ5e4YwAVWy2MPS-wh9skRkDBxspOjaHAOExlzK_DniORSIbQ6QNyrRNVwlb8e8eIRHbUaJ9PAdO3wjnMyrUTuJw-tPpS_fCkpAD2Pg6wXwmrtroe9TTMH0tn_DNw1qSV4XaJlnPPveRoGjgEKgUIy1xEM4SZ2Ct-CC29QcPFE6uMjyt_-OrKdLM3s_PHaif6XuZIix6M6g8px8kDL_vHIpFeHtsa1zEAUXTI91i2mdNNnSpFoj3AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=aQFHZ_aP4Z-9TF_oxGBO-OMRKyXLfnYKqhfiTjGFcGd7s-32RjQ9BuExEALEeIamvhqJdHpbQ5rkJViEJISbee9DNA9b1DDaxuOqUzJ2aUXYKfXnmW1SvB7T83fl_Y84NI2YcNEBZK9jCvDqBVgElUZRFdeVA4S8x1OqzleLqY_3dH8OvWe8lOQ5SfKB3eQv1Ow4fDv-G5YMAG8xFXJWnX8vAZg2M113LqJjWRZPauh8o9C4tbO0vpT51QcVjHDaefyxxeU638IT8I9OADpktrZtBoA1VaSTEucIAiFpY3Vmw0DOClY_npefkz8-RFAlInIfKFVCY0hG-HBzQy2Atw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=aQFHZ_aP4Z-9TF_oxGBO-OMRKyXLfnYKqhfiTjGFcGd7s-32RjQ9BuExEALEeIamvhqJdHpbQ5rkJViEJISbee9DNA9b1DDaxuOqUzJ2aUXYKfXnmW1SvB7T83fl_Y84NI2YcNEBZK9jCvDqBVgElUZRFdeVA4S8x1OqzleLqY_3dH8OvWe8lOQ5SfKB3eQv1Ow4fDv-G5YMAG8xFXJWnX8vAZg2M113LqJjWRZPauh8o9C4tbO0vpT51QcVjHDaefyxxeU638IT8I9OADpktrZtBoA1VaSTEucIAiFpY3Vmw0DOClY_npefkz8-RFAlInIfKFVCY0hG-HBzQy2Atw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک گروهی در جمهوری اسلامی نشسته بودن و برای هر هیئتی که برای ادای احترام می‌رفت، یک آیه خاص قرآن انتخاب کرده بودن!
یک تئاتر و شوی آخوندی!
مثلا برای گروه‌های تروریستی حماس و حزب‌الله این آیه‌ها بود که آفرین به شما! کارتون عالیه! ادامه بدید!
برای عربستان این بود که مسلمین دو گروه شدن، خوب‌هاشون (جمهوری اسلامی) مبارزه میکنن و بدهاش (عربستان) کافر شدن!
برای حسن خمینی هم یک صحنه‌آرایی کرده بودن و یه آیه‌ای بود که مثلا تو به اندازه کافی جهاد نکردی! (خامنه‌ای خیلی جهاد کرده بود!)  و….
ولی از اونجایی که این خودش نوه خمینیه و خودشون این درس‌ها و مکرها رو به بقیه یاد داده بودن، وسط خوندن آیه ، احترامش رو جمع کرد و با خودش برد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=IXKy0Y8wH53i3v5xa7lypfgjiTs3nBKzFwbvBF45p6lZEGDkuCwq5OLdXNu0gv8bGtTIMz8lJVVCO2BjJkkLr5XR6P8IeHsQx3Lz8pLN5rfykFoOPici91ud9nhBruYy164D_UkdbX2FHjJ-dZe2WchetifTGPmM9AiPsy5XJRQsZ-URLMcah40l6EGDetAaTHILJU9hQEpL7EGQTbIUe_TnHD0mwU-JoA8LrFtK2uwETXzyAEYYz3u78hT0OMnH82JxeV8S9CmDbFvYQZY8Q-5907ZgfI7iqdWUYqFOW8t0zFjBIUzgfGqiveQ5eQ40j9otpeTyL8TKR4oIlWqZRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=IXKy0Y8wH53i3v5xa7lypfgjiTs3nBKzFwbvBF45p6lZEGDkuCwq5OLdXNu0gv8bGtTIMz8lJVVCO2BjJkkLr5XR6P8IeHsQx3Lz8pLN5rfykFoOPici91ud9nhBruYy164D_UkdbX2FHjJ-dZe2WchetifTGPmM9AiPsy5XJRQsZ-URLMcah40l6EGDetAaTHILJU9hQEpL7EGQTbIUe_TnHD0mwU-JoA8LrFtK2uwETXzyAEYYz3u78hT0OMnH82JxeV8S9CmDbFvYQZY8Q-5907ZgfI7iqdWUYqFOW8t0zFjBIUzgfGqiveQ5eQ40j9otpeTyL8TKR4oIlWqZRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=NtM9PsYFfcB2r-hXSMR3_1_pOf0rFOzz2IVymJ9la3jj_fdxDQetdN6hGD4GoGOGa6AAhxwCjHDEKn4ago7v2AahrRa2FmA7qd92klGkYwmY68TakPoXyOc_KxZ_gDLQ66xs2KALjX87Jj5g82IxlU7W1hfvCjs9btCF7QQId7OJ2xhfO4H1vHezUKluASysZycx3wD5GBPqaPZ47BhTVfvA_YZMfPbDoIH6giSRxDv4Uuo6BI9qSeEOI4QgblU58I9juqh--yRy338zZ1Qyl3AZSv47RRAIrjQg5PPDMBiXoZbv03QtRlbNEZofqnLQg3fsbJVJ4qNzfbKFAABxng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=NtM9PsYFfcB2r-hXSMR3_1_pOf0rFOzz2IVymJ9la3jj_fdxDQetdN6hGD4GoGOGa6AAhxwCjHDEKn4ago7v2AahrRa2FmA7qd92klGkYwmY68TakPoXyOc_KxZ_gDLQ66xs2KALjX87Jj5g82IxlU7W1hfvCjs9btCF7QQId7OJ2xhfO4H1vHezUKluASysZycx3wD5GBPqaPZ47BhTVfvA_YZMfPbDoIH6giSRxDv4Uuo6BI9qSeEOI4QgblU58I9juqh--yRy338zZ1Qyl3AZSv47RRAIrjQg5PPDMBiXoZbv03QtRlbNEZofqnLQg3fsbJVJ4qNzfbKFAABxng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSDwcyOnWePHKHWXeJ6mkkDAEZPuQvU4dErS-l2-2TK2vJsVZJFcOqJKJluRF2M-UyURO9dkYmkTkJ2k9N6DvfnPEH75BAXzJo59B-9GI5yQOdNUSg-AYEBnHq6JjXMzzEB4BNzbnw9PvQ0LFRYsSQGwM6jLiFwfr62sb9JOfKc9jXwJS2_Y1tNd2RExsFfbgAyxbUuJ1dxGaLlkDm-HA4iNu8ItJ0mnn_LxIcg2GNhs4S5vjE3iqOV2oiv0Gim3zVmRPvp4xUcwGD46zp2MRiuiYHKOtH7EBAak2514XVt7JPWY31ofoBAD7ttkdopO8tE9qMM0rzZXdt5utLhfZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtMyzALcvcsK8SVb1ok0qVs4bcUTXOJc-Nx7nEYQ3DF24xKASBZea4Nwp71Kcv1OQCG2Tu17VosLwMcNmXt8SyIop2xbVG0Hv9OSpy5a79CxuxyYjiuAhiKsQmb4hSO6tgiUGVtdb7Wy-NDoJ6YwS37Lmxt3R4gR9aMgWx_Dx_ZCAamPMGzw7XU5PFgtY8Du2B75Sau4b1LKYWZEG-TxiH6tnDcRNM9vMmoIeF6nD0DUymEmLbfNySqJHyz9k4UnkNtmRqjk29bJGj6eW04Q7X8s7IVPttIkabGyrWkc2lXCNobOudM90vn2KRgD9uOfLTkdIrEgzo73qLeJfDyoxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=Tq2DXu14iPk50lt1-6XewhnzWFbSjInWQIQQ9aL8j99S-nYRgNY2qex-_XANwO84yLmiPd4FLSyf3aA5aVovHtOi_rzYyAmdsZXgXJn8AZ8PXI2WPHPIFCwU7Cl2LW9siDGC-1OCr2ZHbBI3lVpppMEwfkORL5kZF3UbBIf3YF9_Uw2ZjSFLUqV-AEWG8aFd6RDCjpNArPjSP4OZM3I-CQQ2mdaetWKq8I1jDRpLIT24cmm3wHotDhUXklpsERupbNAPMKoqKwA4e5s9QMcEhkNsq98NdGhbJcZfC7tRxO7x33kKsF2T-qAFkbq5kK1K_wDJxyUWprkrRE1Skb1BJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=Tq2DXu14iPk50lt1-6XewhnzWFbSjInWQIQQ9aL8j99S-nYRgNY2qex-_XANwO84yLmiPd4FLSyf3aA5aVovHtOi_rzYyAmdsZXgXJn8AZ8PXI2WPHPIFCwU7Cl2LW9siDGC-1OCr2ZHbBI3lVpppMEwfkORL5kZF3UbBIf3YF9_Uw2ZjSFLUqV-AEWG8aFd6RDCjpNArPjSP4OZM3I-CQQ2mdaetWKq8I1jDRpLIT24cmm3wHotDhUXklpsERupbNAPMKoqKwA4e5s9QMcEhkNsq98NdGhbJcZfC7tRxO7x33kKsF2T-qAFkbq5kK1K_wDJxyUWprkrRE1Skb1BJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=NVSb3TWZyCLJMopauq_BgKjZr_eTUtLQfMo2dDUNl3JsT-607E0XocuObo3B9zsbPg08rK_PMnbOUgxT41dioUxkuUVTxevrd1omujm32I_M5O3ewVHyXDf1UzzasxcT0LzGv2wxc318W2if2vwhqjdswsUDb4DWEd1DdObk5Iik9nmL11fVKPlVbyGonigrbml9CIPHW0NBKRCW8UCojbJjjgmaooSk-Dg-RbHmnp5pfH8lyiBX-YIKgv00AV-AZSPL_utvBW_nX6bXFcPWfI4URPwSRjLWC9-gXCJvjIMMKfmSmEoVU9bX0EMWCCZbgiRBL17fzy-DQEohKtOT6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=NVSb3TWZyCLJMopauq_BgKjZr_eTUtLQfMo2dDUNl3JsT-607E0XocuObo3B9zsbPg08rK_PMnbOUgxT41dioUxkuUVTxevrd1omujm32I_M5O3ewVHyXDf1UzzasxcT0LzGv2wxc318W2if2vwhqjdswsUDb4DWEd1DdObk5Iik9nmL11fVKPlVbyGonigrbml9CIPHW0NBKRCW8UCojbJjjgmaooSk-Dg-RbHmnp5pfH8lyiBX-YIKgv00AV-AZSPL_utvBW_nX6bXFcPWfI4URPwSRjLWC9-gXCJvjIMMKfmSmEoVU9bX0EMWCCZbgiRBL17fzy-DQEohKtOT6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvrWF_RauU_WH6UhvCCmFkU724WECpXBrbfkXLNTGwHYivZXZF4Q9M6rHEA03Yr4Xfr9wO47LmTt3nNp4dDAzKnRnDlP2B8OPVJylw478O_uzTtZ9CjEXB3JXBQMl3vBACo7VwSaQuBLpPeEwaXX5SJRKdHKdc0c37usmnkwDEtIhr1c_n4LicuxuQcIwSjbyWrUGZwuj1C2KW81ef4IfZACHggn6ZUdKGZyINGfgcLiofYcE5kg-eMuERY-9YlZJ5E4zOaQUblYRoUXnTHXRao8GG6gFNynAVGQKnvgFVUV1TQQqOWg9qoqChBAE34ja1XYXZJEW-6kLZiKJY7cEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVVCynvtsxMtbEIojwhVF9rxLDMczeX9947uarnJZDWYqxOGJP3v3uzuMDZTbsWgvVLhJguJltP7m6hheO1p1jOltwKRC-XWfRLUt07IgPwF0EHNjvGFCOZEfPCvtHxlhh2aIo1LImMcSP2BXZAgU_z4j9P0tkJgRox7jPe1dlTItHGeQr-57GS9JLhEZEQi2mg-QyjLTpvg1vjuHgmxfyjJB8-PXzDHinoc5riZ8kU3PxrDjA0Rb28LeWvFoO_k9UmTejxbH3bnMXDAdepndCsbQPpCBy4ujtYD7LPsrdVVuLPRm1sttnc-FmL2MBDBlcx8Mey4daPau1k9bP0UEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9ffVpV4ZgctnGAQ42pD-_0QcnF2HX1cLjHMi6eOUL9JdKb5NA-jBEwrjxZ57Z9-B4yeA5_JK6DvEqz9m0VPfBG-M6AqYGsu0xHYTaZJs7D9NOcOQgNBaBG-GXt0otrKMu15DwISru589evLVp-sTsDlZb8zk-kBKIAFtFXfzCme-G_JxTuroipzn7aYeSLo7zKglMjcGwbHpvQSjwLRTwnfmTJI1S-fP309rMz5tFFUVjOhBiFrJBQsrUTDVPBwXPlLA_Kxd6r3GQPZGipoXE_K_1oUmal_y4FO8lWAyrfuaUWvNGhhJuUkZSaOrLXon8iKS5JLb0XyhTH4CXzYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVcYCxvdvpiDMkCWFXOqYWovWcXvpFAovWCUxyD8IOPs3rQsm8CItVBn_wdXYu3lpu-PIUktyGVAPIsd9uHoyXir_kv6oJzWgxhy4NAWcnnIhYuakHSkkin3_vtaYaA-I4rlENEhcj9JevDVz8VGr0_aKHiDM6k0rPfBR0rDyHlxGiAIzLOsBzb1PJM5XtVckqEYCF-PzqOCtvuO5FmE7nD10LsBWmwBT1BrMbkwmyc6sH0KoJ-F1QQJcktsIYqJstIuwiwEPk5JzbVKrxTWV2Z8VcAfU2mrUsgTBJ5wq7gvRi4DLFITYa1fssp9B5JkOhIFjaNL80z0_pfU6XiNPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/un2zoIjb0fA8vzD436ZYZHBooVE9mdjgiestW4OldzpbrhJxIgdyc_ooyVA9NNNflwsYm6jPhU8zO1TkOPGwI3Ka5AduAxIIEfQ3DmwiBQ15HhSXIr2biXJEtO6RkS3Qq_8Zj-wK9h7Yqh6EdL2BKvAf4Ru_LVXSgUAc1X16P3cB1GZ8bL3zp_uzifcZsSN03SWZk6fSo5nxcm-04Rhyv3imcDDYGZ-i7XN32KbRgeMXjd-MfFkbecH0nM-Nz9MoVJSVdvS2C33719WpLcSqY2feBsoSI_R1SjMlQ6rzDpHGFvyYxyP9Ni72AkMZGlYAeVTuQkFuB01kCt4irDUZpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2sLt1RRSBmMwWHOR6T6dZIq_D7fHD7tMZiXsBX1ZF2qsb0YAogFTXJIJep4ySjSQCrEVMUtHs92ghn4P7gjZS8LFbCxJ6x6i7Qb9FSRI1f9Uz8-JQU0_TdYtt5kcqYC0suqOOINl8UircblpMOp2KXGWv8yKhc_pWso6BnhC5c67nig2mYQGrB21YlvTAt8nde8hT9cgEZ8zOmeirk4-49Dy-Ix8rsmA1N9ezYQ3N_r9Hw0CehsOILbW7jdo6brE9gOGtbqpTicIOE_K5VyonB2aSPauSwTwZd4eX7aqfzNYpINr2NKZiMWxSgPtQ0L5i1UUO5uqhlcyiMGcFPZGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=UCMO57k5HWf3M3XgSC8VB2SJck-89dtg1T9fDi0rKijQCF6hbOUUMTUnsfa_tM7AFxgM0MZUObkbNyG8K36IO3ppm_XZiW_Ak4VF_RXyF96-t8uJI5OOgi2Z7xkWMluik6fFw5pep-RSKEYTHHfQ94NO9VOk1yHMyP1i5Q5iIH_aPen7sYHzS6d3_XftSqaOS6Ldx-M7M9HI5uyTsqvZ7AzOlatuML7WE95iHZzRdK1-3CO8uYnwDm2Py5KzpOWKe_WnVmIUaa_IihC82GBeq3XDsTLRCDF7qUV-Xtf6co6PRmxbyfxZ-4JQrhP6iK4EBnInQWJxxcoemW80cpM1LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=UCMO57k5HWf3M3XgSC8VB2SJck-89dtg1T9fDi0rKijQCF6hbOUUMTUnsfa_tM7AFxgM0MZUObkbNyG8K36IO3ppm_XZiW_Ak4VF_RXyF96-t8uJI5OOgi2Z7xkWMluik6fFw5pep-RSKEYTHHfQ94NO9VOk1yHMyP1i5Q5iIH_aPen7sYHzS6d3_XftSqaOS6Ldx-M7M9HI5uyTsqvZ7AzOlatuML7WE95iHZzRdK1-3CO8uYnwDm2Py5KzpOWKe_WnVmIUaa_IihC82GBeq3XDsTLRCDF7qUV-Xtf6co6PRmxbyfxZ-4JQrhP6iK4EBnInQWJxxcoemW80cpM1LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=pZ0REivfFs3CSYZ01XVR83iqkB1GVsZrjaCKZjx-xn-J9_xTI0qpKlaqc9GL604d1tdiQ7kut1a8btC_sD5-IxGLkAMFqWdpmaNtlf_wSZ84gtLjTrYOXxvA_A2ExnRmlp-UHVtwHkSSsvf9MF26CLnd2bmDK_w-ky8yT0z3DjODLiZMXaMdBnbWCYTd1UAtjSFrUo_tkzppoExE50YiK9GMzXgMBHAstdSYezPNojhGGoRlXk6TaAGmzy2QGR-VfJIn7jC-AGV4i65TU5B_JBEymeh2ekUYCogDLwlTgDm0WOf78FcPJ2tIpCK8-ZFxTNk6WiF-Yb82bNa3__iB8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=pZ0REivfFs3CSYZ01XVR83iqkB1GVsZrjaCKZjx-xn-J9_xTI0qpKlaqc9GL604d1tdiQ7kut1a8btC_sD5-IxGLkAMFqWdpmaNtlf_wSZ84gtLjTrYOXxvA_A2ExnRmlp-UHVtwHkSSsvf9MF26CLnd2bmDK_w-ky8yT0z3DjODLiZMXaMdBnbWCYTd1UAtjSFrUo_tkzppoExE50YiK9GMzXgMBHAstdSYezPNojhGGoRlXk6TaAGmzy2QGR-VfJIn7jC-AGV4i65TU5B_JBEymeh2ekUYCogDLwlTgDm0WOf78FcPJ2tIpCK8-ZFxTNk6WiF-Yb82bNa3__iB8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=MvxKEkJtvSLf4xh6-pHFnXy-0jGei4XzEMEUosOMDfyIP3oK73Cx0IX_Gk74ufPFEaTGMauH74SP1njQv8OHCkG4bjft3BBOChipIFkqraAzDIOZm-EHk5EORRw_oXkc7BPxZ-X6YSbIY3He0b9MxBnDT7LkQ44YQiBxEARKQA0dwa2iyR4gpVRlXkPZtPO8phq9e_ZHN4ZV-poVWCNYj4L_a-TWeQ7QQwlexYOHKnOVWZ2FxTdNA0ypQhYu-3J9_GStWhM5N0MS7_qtWkEq5Nd4KBGhvW3S_jxP4OvWpyljAi41r7HSec0cSwaPVLEOTIx2hmm2L0ch1b0arPUGfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=MvxKEkJtvSLf4xh6-pHFnXy-0jGei4XzEMEUosOMDfyIP3oK73Cx0IX_Gk74ufPFEaTGMauH74SP1njQv8OHCkG4bjft3BBOChipIFkqraAzDIOZm-EHk5EORRw_oXkc7BPxZ-X6YSbIY3He0b9MxBnDT7LkQ44YQiBxEARKQA0dwa2iyR4gpVRlXkPZtPO8phq9e_ZHN4ZV-poVWCNYj4L_a-TWeQ7QQwlexYOHKnOVWZ2FxTdNA0ypQhYu-3J9_GStWhM5N0MS7_qtWkEq5Nd4KBGhvW3S_jxP4OvWpyljAi41r7HSec0cSwaPVLEOTIx2hmm2L0ch1b0arPUGfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=ZHirCieiRyIgkFL6bNtnAShyu1wjgRnTDrrQ8D3Iuw9oZwWyH_i8dxQ_tqH83IM9ax-drhkDlXvS-lA4aFNVSnVFx_0A-H6e7PFIv0u7JneN9eLv3vxlEgnU4DHcE0ypoZfdSW9DM1y3WKVDbr6IiGF9PpEnh_hnEDFX7aEWNGSv1nBcqvLHvsiny6gJhLPrDf4SLmD7qMe3wSFyvkJzUsNnzvHXtotojlNHKkojtzlWFjInpZXiXR9tT1lUtivJ94AoJN04JehlusYxo-evMfWE0SbHqrEICyvzypuSkxKfM3KIfMgfaXu982vSDY8ot5TdniMduWz2PXaw5sAtRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=ZHirCieiRyIgkFL6bNtnAShyu1wjgRnTDrrQ8D3Iuw9oZwWyH_i8dxQ_tqH83IM9ax-drhkDlXvS-lA4aFNVSnVFx_0A-H6e7PFIv0u7JneN9eLv3vxlEgnU4DHcE0ypoZfdSW9DM1y3WKVDbr6IiGF9PpEnh_hnEDFX7aEWNGSv1nBcqvLHvsiny6gJhLPrDf4SLmD7qMe3wSFyvkJzUsNnzvHXtotojlNHKkojtzlWFjInpZXiXR9tT1lUtivJ94AoJN04JehlusYxo-evMfWE0SbHqrEICyvzypuSkxKfM3KIfMgfaXu982vSDY8ot5TdniMduWz2PXaw5sAtRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=mpD2glPKT0s3z4TISro9eADxYZ5WR5NH02vV8a9n9y2bUa1_kKWN_DrCzxCM7kYFzUIdGUbwjNUoEXgrS18g5ZWsAneFBVG4TjJYxErtx94RjnS5yfSK-6kzdj5eQo2SnY8v1nf9t0EGHa9i9KyfMRFXjFXlhwYlmWLekBiguv5wrG8e_ogRopJcmzgX8DAC2eeIJeHhUX6JVqNJCIfKE3qoeo8qfzSbVPe-c1SR12UyGI8zadvDzc-Npfl00fxv0guwoNZ-ixbW-SxGJxbrJMLEvf5QsW3hKH76_67muJWh2IkFM5dRu2LhBr5_ZGADyLd15ssQCanSFGjyKtHJtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=mpD2glPKT0s3z4TISro9eADxYZ5WR5NH02vV8a9n9y2bUa1_kKWN_DrCzxCM7kYFzUIdGUbwjNUoEXgrS18g5ZWsAneFBVG4TjJYxErtx94RjnS5yfSK-6kzdj5eQo2SnY8v1nf9t0EGHa9i9KyfMRFXjFXlhwYlmWLekBiguv5wrG8e_ogRopJcmzgX8DAC2eeIJeHhUX6JVqNJCIfKE3qoeo8qfzSbVPe-c1SR12UyGI8zadvDzc-Npfl00fxv0guwoNZ-ixbW-SxGJxbrJMLEvf5QsW3hKH76_67muJWh2IkFM5dRu2LhBr5_ZGADyLd15ssQCanSFGjyKtHJtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=Re1AHzL30wSzckjPqpquUoo3GZk_hqah--vLOg6wjf25-xFNNDtAQdYJTFLgYHa7EnT7kpyx6NwOOqN6C7dDnq-biAobfJHJu70AvxLrAwafkq6wiFz2HzAfGQKyIRFCQUZeDy4FZPsVlzzWNlhTG5swcDTFzdHI_uOhNiZGF4etQOHsHtPXy9I1-fL5tTGaIK8x6JgKIGWy3W6M-WcuCaNL3PKyI8qaWr3aya3kh7eJdri6GpCP5ooHsksmmmOFlc-GBjiIbsGIIta_VnTL_urfP9CwDuWt9040yzX3Oanbc5rI-5nl7z_41xCgKKGX7tKKJYe4X4y9YZP7KOzPSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=Re1AHzL30wSzckjPqpquUoo3GZk_hqah--vLOg6wjf25-xFNNDtAQdYJTFLgYHa7EnT7kpyx6NwOOqN6C7dDnq-biAobfJHJu70AvxLrAwafkq6wiFz2HzAfGQKyIRFCQUZeDy4FZPsVlzzWNlhTG5swcDTFzdHI_uOhNiZGF4etQOHsHtPXy9I1-fL5tTGaIK8x6JgKIGWy3W6M-WcuCaNL3PKyI8qaWr3aya3kh7eJdri6GpCP5ooHsksmmmOFlc-GBjiIbsGIIta_VnTL_urfP9CwDuWt9040yzX3Oanbc5rI-5nl7z_41xCgKKGX7tKKJYe4X4y9YZP7KOzPSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tz0hCamljfTO5CWWusmh-hAVZixf-JPBwFeZMQyaeTMRb__7AS6aoXcMx-WFus6RQDZjr6CwLW7dgY7EDElHtO_wjOn27tA36ofEU4o66LRvP8_GNoQHY6v0dcNrBuKbg4b-jD-CBhQDUqvJSSASkqsZfuFqveKTRgSXB1PiWY2aEZ2ta5JI-4R4_QqJLWXY9A12HhCT0eeO1XBjcLf0MP3VUBr58FmF4ZFlBDxvG0Qryun5_cB3YyANd0W-qP9NQD8PhBbkopd3s4MqYR34MILG9iNtJLwAV1DDPnGXD3iM13V2uO6OherasMtMrRXN1zgZilf6wRHshk0mEri_pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=F5MQieKRnHnTsUmnPpH5lLHjOcof92JhwI7FDVdoJ7VO7oT7d0nu0NjwPGcJeYi8p5tb2_5QDV3ywzCFngM-YD5t-hFL3qo5oRWsEM2xNZ6mDj-wHiAs7qJqKtMvPt-D48qSV-Tw5v4wWRsofQJ7qAKdxNko0_9M6fY6f555Gl-l61kBvLJrnLao6hxLGxWXB2MUU46d9t2a3aKcRyE_JLcy7X6rR-ayHnDyQuOyaMFt0xrxfeK7wo9CcuD-bY0oiFEla3ut_lY3diM8ltPpZF_86MdT_ys2a5SFGuZIKY4Wa3WVswCyCY5yz4ra-LMge4hHHNBuEWxuEjSILdvHXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=F5MQieKRnHnTsUmnPpH5lLHjOcof92JhwI7FDVdoJ7VO7oT7d0nu0NjwPGcJeYi8p5tb2_5QDV3ywzCFngM-YD5t-hFL3qo5oRWsEM2xNZ6mDj-wHiAs7qJqKtMvPt-D48qSV-Tw5v4wWRsofQJ7qAKdxNko0_9M6fY6f555Gl-l61kBvLJrnLao6hxLGxWXB2MUU46d9t2a3aKcRyE_JLcy7X6rR-ayHnDyQuOyaMFt0xrxfeK7wo9CcuD-bY0oiFEla3ut_lY3diM8ltPpZF_86MdT_ys2a5SFGuZIKY4Wa3WVswCyCY5yz4ra-LMge4hHHNBuEWxuEjSILdvHXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=sY1GjZNOi3_IyhAVVyaiSnsCVku3rJIpPGYWZtYiLFnGXK92l3c3Ny0bV4KM9l568nS_aKvNPVPKTwi-lMwsLN-keJSSDQcji10jqrAUDztPK91neUeU-vYhmig6VEflG_XHJOOYZRdhNfzOZ4EtPPSZCYurOhxpb8Qs8eFHty87XOSjGrDSZHP8GfTVkOYpLyMZMIZ6Tulpc8__B6zkhEk3aBalyC5Ti33CMzecPxkG3ADged4csR7y7IK8RuWldyTJkf3xVAvZGU2pThk6Nit77HHObMGKf2SgFWBzFhvY4mUJqshAVlb-ruQ91oImL72sGlsGOSu83UsitXdrbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=sY1GjZNOi3_IyhAVVyaiSnsCVku3rJIpPGYWZtYiLFnGXK92l3c3Ny0bV4KM9l568nS_aKvNPVPKTwi-lMwsLN-keJSSDQcji10jqrAUDztPK91neUeU-vYhmig6VEflG_XHJOOYZRdhNfzOZ4EtPPSZCYurOhxpb8Qs8eFHty87XOSjGrDSZHP8GfTVkOYpLyMZMIZ6Tulpc8__B6zkhEk3aBalyC5Ti33CMzecPxkG3ADged4csR7y7IK8RuWldyTJkf3xVAvZGU2pThk6Nit77HHObMGKf2SgFWBzFhvY4mUJqshAVlb-ruQ91oImL72sGlsGOSu83UsitXdrbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifjR2liDUUVj782QFrnqIw1gyy0mRqet7rWV7VS3AJ7zWjF8CTtKoROebpCteD5oYzRRmdkDM88JLyCVgHWa6C6wofXIPINxhvCOS-htDTrAzdpeD2X1IqRhbb7GT8HHLLDb2BpdPJubAEKC2WZByffh3FaB-Tt6zUVUU6FHMc6MwWSYSTkUSOYTgq91uTMwOKCnFzd9DWtHlU7-KS2ns7Ql-k5i9yLZZ8kZIlR9dVBVCMQUqmxhyn3ElKpEhYEPre-akVt15RlRhbfeEzHxQVBwR5BiiEnCACkMQOEPv9k6AUbefNVw0noyKdRTyyDQ2IaPuTeBOUePvLQ-WVDZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLYgwt0O6lmtrjxb7aT5mWbozrBsLbAXgouhN5nIZRCX4mGP5SFCWIn7aDyf8XSSmLCNfXgTwWUTcDRRs7GFHAxeyL0GjzotCnjxpeMTsrY9YdkTiN5PDD1wm88HEnGdkvfMYEAZZYUqyJxm_YlPuOMR9jl08bAXGSJBfs97hq2F6AeanV50pDQjBBubJU4A__25lQ0l6HahfX9sYD7LeNUQQC1y2zsZ0ZwHltuxeW7sZHGHKxstJ_HXyLLiLkuMDH83oqEW_0Rr_r5_wM_JyHLSmEJ9CC8R4awrqsvVgQOZ0FeevI9vdVQmL6QVfwX9V6N3-eUjR5WRGeEiEdnxNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpz8ybncYSl9FzvGri39xlY_Yw3dMEbiRimDbMIth0A5l5wGZYtHD6jDr_clCzc-wcMivX1caKYp3Fiu9ZLRPZ1dpRKxbyH4ebvqTJSBTYOaCuikkaAosJToIA7P5SkPUVntwJexPvTdJ3mNbZcYpCUaDOZQfF4kZUneCMtNWD558msXlsgB_dZLGQj-z3_RoaSS_gLSikUvXArAbp_4os_X_XFEqZtXZjNzto4tCsmUt9H67b-C5eUlE5UZlh4VszRwxuEUPCcYz_QzXgNenOimv5lpUau2bWNnR0XjxfnnMzpKBr7fRALSwNHyHAk32USyKARa99l1I4aiPmraJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ak9VGZy-k3bepBPMbprnbGUYDat5lcwxgQu6J-lFtjT-AThiHMnlYt-XYqWzzdc_gOrobE_kWC9M7xf11AUe5_pURVbr9rITdZxKnY32OtM_eNmIIW0aUffSjBlGEk_OfIi-D_y19_gb0JnYZx2UvjvJJxXnb51E1Z6UPM2cWvpFFNR_cYU5b8a7QFjo5ERosUwtbcGiVvjZ11HOnrLCCLlkj42lv36ogz8aTqnjNhp9M1oh6a_MP9tUeDmQL_pICcVu4-Y7mi0SELlC1UmeoPoP_DdwTUqJio3aB7OdBRl-av3u_FfmqMrJZE_h7JmDUjjfO_6I2EJUq-cxjBXH7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVR6mOMazCRvNdPoIRscnBHXE5GNz7BYqvZmfQ8WfGrGCJkWOnXy1UHnxxClmtGp74SQyr-CjgvTVoeXvqlJKC2mOxXQWLQ5aH4X6_0SD_cVwV8qu7JYMtbkUMlvmU0AL0KNUrV6Rzdm8EeGTIeeWw-yo_MJOKWe-0_JdtCBdwYjnFrjaZQgG3MYlr3TbIwAc0yfJoFfQjNntTTB8xtr7Z0wZYCfBsbW0zZPGfPFrcCMkOnUDZi4sNTLalN9Y8ofC5EMXCZhi3qaB8OgmU03pMXlH-GfQqllwL6greOz7FomWRXQt5QdMmFccGSV7sS03THNX6ZRD3MGZ0deIBYkvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
