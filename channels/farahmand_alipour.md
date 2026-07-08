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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 22:46:24</div>
<hr>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=XkP7L4x5NF0tgJ3bBOG_ttkCSOfc8NZlLmIZi_yHMb1x-K1UP5Fj986yGJA4-b4YBkiOmNvVbFePkNVQOVESvOwm4k8JERhQyN0PQfsXGscCUCs9fkzn9cOFXT0KhYkfIweJ2k75JUdrHrnRiR6u23Uliwgx9daZOXexFZKIQSjANIkXnpkkGesRc5cXO6-jHdW4Ylb8DeLvJ1YSF-1yRwhqDF6U5XBXIXofuQ6969Y72MzG26lVmWyt35jVxPGt__wnv5MKKqShr0bnwCY8HyaQeVkOfDVtXd3IhmgEjPTCFl_zrqEeCgjyNFvJDIvYt8MlSe7xkf9AUWrP_Shwfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=XkP7L4x5NF0tgJ3bBOG_ttkCSOfc8NZlLmIZi_yHMb1x-K1UP5Fj986yGJA4-b4YBkiOmNvVbFePkNVQOVESvOwm4k8JERhQyN0PQfsXGscCUCs9fkzn9cOFXT0KhYkfIweJ2k75JUdrHrnRiR6u23Uliwgx9daZOXexFZKIQSjANIkXnpkkGesRc5cXO6-jHdW4Ylb8DeLvJ1YSF-1yRwhqDF6U5XBXIXofuQ6969Y72MzG26lVmWyt35jVxPGt__wnv5MKKqShr0bnwCY8HyaQeVkOfDVtXd3IhmgEjPTCFl_zrqEeCgjyNFvJDIvYt8MlSe7xkf9AUWrP_Shwfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگفتی سران فعلی ج‌ا آدم‌های باهوش
و منطقی هستن، چی شد امروز گفتی
که یه مشت بیمار روانی هستن؟
ترامپ : شناختمشون!
و لبخند رضایت مارکو روبیو
[معروف بود که روبیو ج‌ا رو می‌شناسه
و ونس اینها رو نمی‌شناسه،
ترامپ امور رو داده بود دست ونس،
که الان ظاهرا دوباره برگشته به مواضع روبیو]</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3Zqqio4D2q-qLws74KDCaiR09ijMCVB2Vp2Uc7zcICaOuSNA5BcjexN4v9UZiHU_dx8wzwOWvsYSuiQE6ktFNXMYdFMz2OyntzK7F0kX-OJpEs-H_qn-k3MKowsCgbbBrLFsy9OJsBpQtDlzf0wdgdTxuNtN1wophjMMMRAPf0lcWu9mGP_Ki1bv_vc_5ZUIWb3HUFaSX56m0msqIcvQ1Xg7Olu-vQSWdowYqiFgw_ejwD4Gl9F3POgo_N7ZZCDw21J2_4vck3seC8s3B5-uZVX8m-BeSRavHECVhE5e6SbkkQsdo_Bx5hZJ4gsN8Iqg-9v0P2sH1GDsuMxxa2E5oOOpg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3Zqqio4D2q-qLws74KDCaiR09ijMCVB2Vp2Uc7zcICaOuSNA5BcjexN4v9UZiHU_dx8wzwOWvsYSuiQE6ktFNXMYdFMz2OyntzK7F0kX-OJpEs-H_qn-k3MKowsCgbbBrLFsy9OJsBpQtDlzf0wdgdTxuNtN1wophjMMMRAPf0lcWu9mGP_Ki1bv_vc_5ZUIWb3HUFaSX56m0msqIcvQ1Xg7Olu-vQSWdowYqiFgw_ejwD4Gl9F3POgo_N7ZZCDw21J2_4vck3seC8s3B5-uZVX8m-BeSRavHECVhE5e6SbkkQsdo_Bx5hZJ4gsN8Iqg-9v0P2sH1GDsuMxxa2E5oOOpg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzzSsDYa8IXl7mXx7DOeEqP46ZcQdnBRUD64sU3JIY19s2RCYYLb_q3aDDtFOYzPCzNOncjWjzLGLfgb_Dqhqr989KFz42vbUMnRgQIeFX5NvkQp1L1eiQ3il-Gc4CiKOAprVvy_9OCHOLDWmGanGu4QRl_WYl9UdsRFepC6MSfeNnL-VtmrhDZE2IeX07dtUkvSA35ZHCwt-RbjEXs9oYxHaln930TAMkLQYmUJUc9SPfZOWe4We_oIGHg1EXT_yR4pn8exr_ZrpoukBvVRjI8rZ7rRQaIXvfuboDHX9MzWM0EygwAUgFF285h70DH_k1-CO2_lB9z3HkZpqh0XYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=Ki1alEeNcLwnOfBYCsOQxnFOSW-36GAObsluWfWob-aO9J9OQRJDHnsXNLD52g3OD4dXPUMdRFyapNPrHhpXswFdPruwvn3cR2Cl3-RX9zq5lUnXw6PXBkd2WjmWR0Rk77WGJN96trcxD4VhK7RnMLD3mJ9EnQFaSVr9XGR61Mx6XxLRnA43ZzWRrRR4N5K_2AU1ffSFMIqyDyXSiw7CK199XL6_Vi6PDSzr_ZCyjhm_LK_kbQTzgnborVhB6NEk6wabwt31vaBur3cqZ_gRGvgYZUxVH67J5VON-ZfCjhlf4ZLiB-HMH2tdubae9yJ-AwxXK_gTvplDSuYdc4HvhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=Ki1alEeNcLwnOfBYCsOQxnFOSW-36GAObsluWfWob-aO9J9OQRJDHnsXNLD52g3OD4dXPUMdRFyapNPrHhpXswFdPruwvn3cR2Cl3-RX9zq5lUnXw6PXBkd2WjmWR0Rk77WGJN96trcxD4VhK7RnMLD3mJ9EnQFaSVr9XGR61Mx6XxLRnA43ZzWRrRR4N5K_2AU1ffSFMIqyDyXSiw7CK199XL6_Vi6PDSzr_ZCyjhm_LK_kbQTzgnborVhB6NEk6wabwt31vaBur3cqZ_gRGvgYZUxVH67J5VON-ZfCjhlf4ZLiB-HMH2tdubae9yJ-AwxXK_gTvplDSuYdc4HvhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=PsPYqlvxWn3WNiH_ZG1O3erxgZxRHjSt91ypfNNq9AAYIU0OmOOIPcnWt3kbrQp4Z89aq5gXw1_nZVqhTW8TsTsjBRGn8ttzK2oXcB-BHksY4Af0JfW2LJAXH5SzH-qc1ceylOL60l4biafWTHu6SQmMIYjtbtUzOhthKcehJzXylkhcd7sIPPSPVTheYG61zqdZLe9tloc4gdW2bT6Pb4uOTj0_9QC912mMaq6kg0vItDXhu9Y-pmM7hChpm4PSoTI3zNqRX3VSryiYRxGcOC1aBVOH9kicLCDJnhHiGxmBlE3htlHIQENljTKNOyXSi_JMR_MkyUNMksqEiUoR4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=PsPYqlvxWn3WNiH_ZG1O3erxgZxRHjSt91ypfNNq9AAYIU0OmOOIPcnWt3kbrQp4Z89aq5gXw1_nZVqhTW8TsTsjBRGn8ttzK2oXcB-BHksY4Af0JfW2LJAXH5SzH-qc1ceylOL60l4biafWTHu6SQmMIYjtbtUzOhthKcehJzXylkhcd7sIPPSPVTheYG61zqdZLe9tloc4gdW2bT6Pb4uOTj0_9QC912mMaq6kg0vItDXhu9Y-pmM7hChpm4PSoTI3zNqRX3VSryiYRxGcOC1aBVOH9kicLCDJnhHiGxmBlE3htlHIQENljTKNOyXSi_JMR_MkyUNMksqEiUoR4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdUfZQkUbZn4PdoxFTVxLLC1_uh0pk_Svk5640gLN8azH07lx77hJEtleV78CRvp6Z_JKpk1-_8KmjB9UTsUSLYeoWcpCE5957aqSyJMQ_5BIqDmp-TH0m7ZDyf-FrXDdMCUqeIy2m3c-VmwCzD_GNxilrk1N9IF9d71qsK81cGd-WyPe0LehJS9HHy2h9vLs9Fjl8n88UE1EwFXrG3ONQkjmhXvPpZ9zoYiM7cynGUk5udht09N7zSMOMtnXavVqK5S6Dh_15r7eA7W9ZrkkdZ7eSfmgYwRD-IWBI4zZdX7GyzYebxleNPkr72Cx3_TmJCjbEjuip8uzyiy2xlHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=UM-4jBsmM2fSPhhatd6bMlVbQu4DH39d-uUUvsrbWXmPL1j8yncc3jOQDYeGue1N87B2hEiHhyL4oM3rWKpx-CgWwAlxzKywwK5Z_1be9mC3wCeU7nbbIN5vKVoc9DZkXrAtmCFWxMAjHe8AJQ_Fu6CyzcOEJgLpd0o_dwVYAhs_Z_Q7GT7fU3QAuReRn2V3pxRf1R8BLAvF183QLkyWPd1LrL-2qNHcAQpoH6o7HO2Wb9xp_qhkcb-h9TlM9bjj-Fvy7_Oh9VM2cTRZdJf51Y2Z1RoNHLdo2KX09BT1U77iW8SmwwoRqP7EMDSCSeXpgi_5lSN8ceiT2mEQXrtsmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=UM-4jBsmM2fSPhhatd6bMlVbQu4DH39d-uUUvsrbWXmPL1j8yncc3jOQDYeGue1N87B2hEiHhyL4oM3rWKpx-CgWwAlxzKywwK5Z_1be9mC3wCeU7nbbIN5vKVoc9DZkXrAtmCFWxMAjHe8AJQ_Fu6CyzcOEJgLpd0o_dwVYAhs_Z_Q7GT7fU3QAuReRn2V3pxRf1R8BLAvF183QLkyWPd1LrL-2qNHcAQpoH6o7HO2Wb9xp_qhkcb-h9TlM9bjj-Fvy7_Oh9VM2cTRZdJf51Y2Z1RoNHLdo2KX09BT1U77iW8SmwwoRqP7EMDSCSeXpgi_5lSN8ceiT2mEQXrtsmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=UOC4u3SGDeIPTJ-MzM5_IDOjqkVIdeQ3Oc7A6uIAkmrPuvtwZ0_QJGbYJa7HGGBjDTCR7DJyWt8ZdMBBYQ6D7gsm81q7aVMSHRQfWE0GTUQunRqIBulQrSp8NsBTLYSSpiHZFNJ5zpFrZsgqwW2C3rRyg5TDVT1EDb85KQGuBbeyf-_8cXNfGvyruxEomCRSt778bVBGrT26G4la6CKTNU7sG2d-1t7x5IjdYen9rLArwh4LOwT52tnn9R5J6XnQdXtiHlM9nIpSThFXieN2MbFVV7mLZqoxTBWGakFrFvWn-tND_oGZceWsn3qEs7c-IQe_ND61wslWqTBP7gEk8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=UOC4u3SGDeIPTJ-MzM5_IDOjqkVIdeQ3Oc7A6uIAkmrPuvtwZ0_QJGbYJa7HGGBjDTCR7DJyWt8ZdMBBYQ6D7gsm81q7aVMSHRQfWE0GTUQunRqIBulQrSp8NsBTLYSSpiHZFNJ5zpFrZsgqwW2C3rRyg5TDVT1EDb85KQGuBbeyf-_8cXNfGvyruxEomCRSt778bVBGrT26G4la6CKTNU7sG2d-1t7x5IjdYen9rLArwh4LOwT52tnn9R5J6XnQdXtiHlM9nIpSThFXieN2MbFVV7mLZqoxTBWGakFrFvWn-tND_oGZceWsn3qEs7c-IQe_ND61wslWqTBP7gEk8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=sIUCHYlduPx_HM4WvFX7f39c4BBRRln8kcipfwvCUJbe8HiGZ7vFsOs4ndas1ld7T1kgxs8lDmStQgFNYhsHwIN2aIxtxs4HEHq17V-gIMSWP6_oDxpLMhaV_qPGX9gxEEJjWTLWRE1CZFCIhRbnOS6dhbpmRXuGZp2N6dfExWgg4L9pjwoCQYkPabQlknjKTUtuB0nfgi3woWZgV6EUgH_JuJJrf208to4CSzyB2gU0Lvyoy_1scQUuuDd3ANlm709eF6xrwtImlEIb6D5ngSM9fQW3dQJ8TRso1LzSdYIoXQ8oUiORlzJo1P0Wn1rbD_3aEjTViE1VUcInC5Qc3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=sIUCHYlduPx_HM4WvFX7f39c4BBRRln8kcipfwvCUJbe8HiGZ7vFsOs4ndas1ld7T1kgxs8lDmStQgFNYhsHwIN2aIxtxs4HEHq17V-gIMSWP6_oDxpLMhaV_qPGX9gxEEJjWTLWRE1CZFCIhRbnOS6dhbpmRXuGZp2N6dfExWgg4L9pjwoCQYkPabQlknjKTUtuB0nfgi3woWZgV6EUgH_JuJJrf208to4CSzyB2gU0Lvyoy_1scQUuuDd3ANlm709eF6xrwtImlEIb6D5ngSM9fQW3dQJ8TRso1LzSdYIoXQ8oUiORlzJo1P0Wn1rbD_3aEjTViE1VUcInC5Qc3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">هزاران نفر که اومده بودن توی خیابون‌ها رو کشتن!
صدها نفر رو اعدام کردن، هزاران نفر رو زندانی کردن. اومدن با وقاحت میگن ما اومدیم توی خیابون! طعنه هم میزنن!
شماها با وعده امنیت کامل رفتید
با پذیرایی و امکانات. حتی خیابون رو تخریب کردن برای تجمع‌تون، کولر گذاشتن براتون!
خود گدا گشنه صفت‌تون رو با جوانان شجاع ایرانی که جون شون رو گذاشتن دستشون
یکی می‌کنید؟؟ طعنه هم میزنید!
شما هنوز نه این یکی رو خاک کردید!!
نه اون یکی رو می‌دونید زنده است یا مرده!!
هست یا نیست! توی چند سوراخ قایم شده!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Am6u4Rrgu8xe47049HkbEe2GoLeGK-hOZx1km_XKP_cO5A_miICtDx6qpu8fTBH8KRnTnQu8UfsRbhd25HZTKsKBFMIA-CblIRkYcYhypdXrIDISH-w1l5s9QY563aUY4DThQUI2O1Dchy6cAVnvWz7rHw5CLFc34suckFckq1NkwD7U1y_E143cZCr5H-b-7TJxQksbK78-PiXS2vykxRns5SzXys-oSm9lPZFjXd_nH6oLKvyvcR89r3SjU04-M4-nqwYVCwwt-JOgqMHlJ5EPQ74vwNSdr-fYCXW6ztPtm1FQoYt3Vz-7cAhbq9GQnC7ZrdMeSGdcF6SyIY-eSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : «آتش بس با جمهوری اسلامی پایان یافت. مقام‌های جمهوری اسلامی شرور، بیمار و فریبکار هستند.
آنها مشتی آشغال هستند.
به آنها یک هفته فرصت دادیم برای مراسم خاکسپاری، ولی در عوض دیروز به ۳ کشتی  حمله کردند.
آمریکا زیاد از حد وقت خود را با اینها تلف کرده است. اینها شبیه به یک غده سرطانی هستند. غده سرطانی را باید سریعا جراحی کرد و دور انداخت. »</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7ovzrxVJ-I8dU0bHTsxaUMHAD9037YNq27Or5C6n6uHtLKXZA4tOfZOFO6RVEJYiKlh26CFYqkUf386ktr3AkL8mFXwCAwk31gZJHYl1hIUchBwk_mp6pbLnFfsQGHLXQxkVyIxQNGoRNJQTAQaeMVAp4_XLd2_KjsYWAAV635Fy3Xwsvq85AsoKMib1VxzOJ7QxQSvO-krfSpZbi9Av6321v_a6qyuq9UpEjQ0JpKXWxHzjjsdu2FSc_2sei0gVqQp5iUm3d-hEmmA5RoB8r0Wu9uiNMog_8NrotCtEyqGT4yjx164VMZtPhp--x5P0CMSZi9FnISzm37ofUkLEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-T3JbhS1OaSDLTuHP8ma-AYCeP5Fc9-eyx5cUpw9lrSV_DI_6R0u9h3QUKZKrnXmrbg3R0kHxW0c4rkfk7Vcr2E9TbO3ji1JyFOxJKnZEf3ag-MFJHYnNN8-Jb8mBWi2R6aCLI-E-EaFtE-Iv7JJrZb8t8zr3TnO10SoSD9IaDJz2KDOS33ZnZuShj45EbVFX9sXFiE_mEwOepM4km7XYt0xMBk5Im4FBJMxe86fKcVS8XsnOqYhtCCY68Ve6MtdfR9sQmX1W9jxMTAoOniybraXSauOMZFN5pw5SzhmQ_hpc9FvIdRBTya4uo8BSfTrJ61UX5UPAaxekq9dtZBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Rn_8WCUJbJutyPrrsbMZMeVklr871nCBWKrfT0m9f_uqL8UzQqnbVchV9RocoskvFLnM1rzw4iiNr0iISQPQR9vyPozccctXPIFjwtTBjK63QOoM0xPtuCCyWD7wMVHUZJen9tEGNBIqI5P4WKregQ06eb_O08JDarZZvevzknG8qaIZacMCgnxUytnh63z2c1e43687SiVbEblFIgNPsECUmc0QIPVUjmzLrPyV3VklTcdOIoyzEdiyPpzP_H-WCr_ob5AgrmEJxeZLp4Nxu6hP3pQWEyUH1XnuOMe_pJ6KaMwmc7a7UF-0SKvjokXa1aR1-T6SzIg0VfeBmUEEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Rn_8WCUJbJutyPrrsbMZMeVklr871nCBWKrfT0m9f_uqL8UzQqnbVchV9RocoskvFLnM1rzw4iiNr0iISQPQR9vyPozccctXPIFjwtTBjK63QOoM0xPtuCCyWD7wMVHUZJen9tEGNBIqI5P4WKregQ06eb_O08JDarZZvevzknG8qaIZacMCgnxUytnh63z2c1e43687SiVbEblFIgNPsECUmc0QIPVUjmzLrPyV3VklTcdOIoyzEdiyPpzP_H-WCr_ob5AgrmEJxeZLp4Nxu6hP3pQWEyUH1XnuOMe_pJ6KaMwmc7a7UF-0SKvjokXa1aR1-T6SzIg0VfeBmUEEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZc_Vwhxfkh47zUVQhoGuIfSV38s0LjAnnkjB4zJqeEnRphn1r0OWGdkYplpgpObbgZ-IafyVuC90iMrDb_Jl810J9ku1FSRBxwWcDMmr7eB2eWp-nyKSUtLywniQmMKtYiVN7Zh7B5tCeEyqDFI00F52R4MY3Sro3IgipTEaZ9JvQOhLcAx6XhF0ilOnvgoQZfqY6dhDtr8PN1Zgteh-mi9SV6fM0UlWtUZg8qDv7oRdWLNsQ_9W3heaUiJSV5Dl3dR0j65Uy3RN9Dk6wcqYKh9zXovpGwjKH0ZPKmHIZQZaf4I6dejBLxKRs-bAc5i-pHjTwNpLj8gn0GXj41EWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=N_hR0SVgDvzVOHuZZJYR1-MNbpJ0WcuTYZQD1K4Ac_01qBdFOyIq106ay7-OBmMSiIvtS-feSsEhJbAG0Z_gQgY879-cVo79gUlmwIOCJVjOiKtZ1wdjFsbO0pqISUH1fFMxbLVmIvXQ7Q8R0VxRDA7SW-X4_cTgEYLySXgiT7LnLILPwC3eajYtotjuUxoJbl17whLxPhH_Sb0piolD10TsBwLmh5zW53ZJu9DiM5UbWeDntJNRlMRj5nNzClHf7tCeTFWAb72RYY2F-83XPvkBcdWn7iwm63HZUrsJDQlITaMB1928M-gaarBqCfwzYGmWHeTLxN2kqG-2syXnKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=N_hR0SVgDvzVOHuZZJYR1-MNbpJ0WcuTYZQD1K4Ac_01qBdFOyIq106ay7-OBmMSiIvtS-feSsEhJbAG0Z_gQgY879-cVo79gUlmwIOCJVjOiKtZ1wdjFsbO0pqISUH1fFMxbLVmIvXQ7Q8R0VxRDA7SW-X4_cTgEYLySXgiT7LnLILPwC3eajYtotjuUxoJbl17whLxPhH_Sb0piolD10TsBwLmh5zW53ZJu9DiM5UbWeDntJNRlMRj5nNzClHf7tCeTFWAb72RYY2F-83XPvkBcdWn7iwm63HZUrsJDQlITaMB1928M-gaarBqCfwzYGmWHeTLxN2kqG-2syXnKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmWB6oAHvUHb3DumrfxKqIuuP43XFJxs01Y4IZOYV6JvrmJWM41kjZ0YQGKlbBv3cH8SApgt6TZclcp7_JQHiiV951nhpF8jwTf3K6YR93PAzfMTzixMXZyy0j1S8ZWHWYwSpo8TNbvveLWlwP-NZOMaRNcuEGfZ_47umSS-4-jqg1g_4bU_cXRoVjNuMdSUFLmLlB-loIu3vhPTChASlYMiPreyqgpcQhapMoKdUywm9JJ1i6U6xSIY2goT0duIZ93z-9VGRCz258U0HpjQYJa-_GIA2DtD7NUfDP9ekt6W0srss4qMotWvbCQL7HXk5aVsqOmIvi6LoezyeFPI3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/autMnhtCwAKGxiCmwSet0GrrfZSKusfJyauLCVx9xaRHDDCa4ublfX3OHgU_nqFuJ1ANQncOpU0vY9MJguH71M62ZPkb2rMPNm_EXKqHKAyysnxgs1n-gg0C8vXkksu14BChOVd95yos_I_WAGh8YrZ3OXX3l2HgQ7UcTH1QZPyK8CVaeAKAMQSPoKtP9edt1slngtNvfP6ELWheFPOHorvUyxPHzvGKmRH6qDzGUEPIBDN2IS3ZSgdDdWUNlp_Z2OcgPSJDCmZerYo1ULgl0iBdTPEO-MHio3JG9630QzuHM_tsCA2ctAZJvmUi4YVRjYFXV8duBDVW7HNxES0-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=vbFzRgWDq6Akm9F3UEd1wpH73zQuTb5NsfPhMUZjgGFPVjBnDPAcnOOuwHIT3YCIud0abjXr3qqqrykZ8JL4QvSqZjeUh7AJ8ObmQ2da30Mg2EpK9LikrRp_Omrnl_EYRr-UdyslqTczN-yOMAeHqFd2Ombv4dcD4V-zv0tJHFE2CzPZvVYmrFwNU7Jhs87SPEsbUEVXk6qP0cBiOnjrR4FIKeJEj1_yLjOrh6J-DM1vG53zZg5-DoZmSWdfHMK5IS6mn1UU0_hsv-R28l8H774L9kz4UsStH3q2bRF2b6m3uqzsk_QDLXltJmsD1ercKdUOWfg7U44gWnESR-aBRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=vbFzRgWDq6Akm9F3UEd1wpH73zQuTb5NsfPhMUZjgGFPVjBnDPAcnOOuwHIT3YCIud0abjXr3qqqrykZ8JL4QvSqZjeUh7AJ8ObmQ2da30Mg2EpK9LikrRp_Omrnl_EYRr-UdyslqTczN-yOMAeHqFd2Ombv4dcD4V-zv0tJHFE2CzPZvVYmrFwNU7Jhs87SPEsbUEVXk6qP0cBiOnjrR4FIKeJEj1_yLjOrh6J-DM1vG53zZg5-DoZmSWdfHMK5IS6mn1UU0_hsv-R28l8H774L9kz4UsStH3q2bRF2b6m3uqzsk_QDLXltJmsD1ercKdUOWfg7U44gWnESR-aBRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWE6MPwRyNNG-mIFQ-WWzM_w5XtxayrkLwsLQjFxtEY0HfukAqnnhtEUkcErAsnkggXNiXppPMRzQbgl9hL3_AUtcJddVEVTETSKcJUpRTmFh0BNekWku4DcJHMMmAWt-5O1zuaNios4eKW0dVZXrroKI6lv9Ej1KQY83Ya3QB6DNlCAhDy56kkBRfUXKX6Y5ZAvSIvg3E4OK9EeE9FOg6zsaEJWNJQBXag-qDVFAkrYi7D3uGbNBT_HnfrQSnApo64ENEvvX3JZirMhBGP0r4RkTtygNt6iamYmDJqQfLtwaSGBSwggprXIZg3qRP4wSCOFZkou430L6Tt9H7jAVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ecls2FkJe824k4f5YU2SFE-EbXIvMU53n_s-k5cdcLemHW3AxNZdM8bZ_uiJCPrlkNiwMGkE_CcReYWJNa456amh1sICmJGBLQC9co3vAOtR2m7fhB5EUwodPdGUUzuwcK7I5JIhm3b81sLel8i1F2wqrOeH8P7Ln5IcbVgIvla4jzesKJtPbdXRwZFjrz8f-IE5FkOurn_Ai1HzwDTSC8MhDq2DuCpwumuoVSEfmiFjBEA1VP6nRWy_hH4A4O6n9gTTF5s2V3rCseU5Cpq3NeCU0UPS8tmrGxAjjm-WmpImZ8vKYWXtl3OeZ-bo2J_WeulXne3x8ck2m_pGDtgxlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8IAgDkOR9f7oSnyFSh23CraUgpd8GTJoFpYsoFKTdoYwyeoYR67NSso-wKjzkazpdZzZiiMk_eQ03DMdvTuBJ4L8Bic-WLd0dyUquWvypg8gvWYEkx8x-dz8p_Mz0TJzpK2otnaTkI4_GgTlLXQkKFQCNf-5nzmhW4zHvaitCSjbatfCgzXbM3XCK-ay34HwNMwbjgrXAJctr9EmuKl2R1rMb5lD-ej0MA6bhRedyCXfEOXMSmv4NnTuTFWGDXRTn8hd8YB_bRP2OqwiL33t5sRJzMz6ZcTFUF63BbcswQYQRck2gdxB374C2OW7ZJkOAFUEEdCHVnOAZDLW29PsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fPztkKsozJ3ofMR3Y50-1ugpTcOUw9bYtrewppArDJg_Gsf1_bBxlSNbsB8je196GBrXN9sp-QNaXjsOoPKZodymlHWTkJtfPPXiJlM85IbiTnifmMSdLv4daXUSlvyDXlqOee0lIVuOJUoMfaLKf8vVPX6x4GaH3uuX-0p3lUx2iXRVnmhtZIprQ9zNkTK6ycXZDwwRNjl7Fiywosqz4lMj7Qxy2EtDA9SeX6XL1oL0Yr5rEUFO5W5Yl9dtfQlOZpJ3jY-c11NE85gWBtV-6HKsQxMrK49K-Jh0CTTy6l8CQdlSlTU-gCTqmRMw3D7NdxtXWWKtGA0nksMq6ncJ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B92eEg0YdTHPtpONOdMJl3k8nJV9hUij1COf_USlbdLIu7MDFSkR4MdQ6XIX9j0miKNDXnjZAkqvsQxicR_g5Mz_bm1MtlziYc8wIod77yTGIdtSw1fA9vvPR7XQZA0sPM_bosd_qOZIOnNZx7Lv1Wy7W7D2UEYVYTaEZvvxTkdGuSGxrSh6CaDuuXKlGFmT-ZOgLWCX1Yn7jDm5baj_dWrjhq8iz_q2ksVIWN5_7scHV9_K2MfuRpFJYknMCMTUXyofQQa4KzeqEiFxrteVxk9xI1WS0tb-aX_oahn3XrP03hYSY7wTRt3ourpFeAcGXEKEC_a-ADPlMuS4FGgrow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=BZBX-RJ7KU_Gh_AuStsdDQuQn8UiW2Ito87RovkmA5-c42sGxDaJAkY5hVgkupN3BT8BEeSAK0K-kiXBwzyOTMPyENVQNvPRuxU9uZ-INev3nHXRulQfOWWHQi4fgTDwi3bT0SLdwnKsLvgiKVXKVBPKSoceU4h3zkOU9mpqIphCLbm4FwT1FWTH6MYxXIa0i6z4eWEN2MZkTHzGgV8zAgcUqXeK5s2z1vUNth8E7Kt0Mi7yCjIsIF5mTecnBoKoO19QlFCihmkqhGorN7epVuhwnLs0Nbqo4hoqlV-hgdiWMlSg_G_8B3lMS4yzfOHPRrndXUy_ZdaPFmaTvznNrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=BZBX-RJ7KU_Gh_AuStsdDQuQn8UiW2Ito87RovkmA5-c42sGxDaJAkY5hVgkupN3BT8BEeSAK0K-kiXBwzyOTMPyENVQNvPRuxU9uZ-INev3nHXRulQfOWWHQi4fgTDwi3bT0SLdwnKsLvgiKVXKVBPKSoceU4h3zkOU9mpqIphCLbm4FwT1FWTH6MYxXIa0i6z4eWEN2MZkTHzGgV8zAgcUqXeK5s2z1vUNth8E7Kt0Mi7yCjIsIF5mTecnBoKoO19QlFCihmkqhGorN7epVuhwnLs0Nbqo4hoqlV-hgdiWMlSg_G_8B3lMS4yzfOHPRrndXUy_ZdaPFmaTvznNrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJdFuzdLnwDmUlRpciVUaVbdKNOSrJ3NcglRj4YB1aqcmkNx7IapDB_3QH02cf1sf0FD2pfWYQVKVqcig_wf-RwUuo5rqiLpFE1wLXrcd3MBHAlSvjLR_dy5YkEhDY3TxLx3LhelLzE1EqwfwtzMQGqzeGZNGjfWRwQiEaKZOEivec5GHy29SMVYByaTpoP497WHuPF1xEJnYaXFaQMeilEcPYb0rhlScsgVZPVLBcVgpze8IK8mQ69MoBYdXYlVKKndHD7B2DL0zeu88Arb1KH84kWF36oPI_NMApTKIVCWPENaaEJ3sePE-k_82u1RNAzDjN5L1kvFONarhlGMtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=PRP0F79aPiWyVbo9Anauljnft2rqp4qXR0WoM2XbW_mZFKpW_BRQZit10RJHViSqLVpZnuRoHAxtkd7-bXTVGzGhm1CS4MMAkPmnfjGyTWl4NC85IwNQDH25od6LgQvJycfpGuI2gH-JEt1z8FTyXqILL3q6_iQzCt9onQNyBB_JsHrJ96VLUftsmkCE7EApPOb799UtiSmbwyYIpreX8N1qzHjecQjgMuR2N_xstfQHX9u2GkB8hIOKxnwVMalpIIdAavs2cRSy8wf52Gpj7hoX_jjbjlH1v8YikckvFAvhgqwwEEprsMUANQY-eh-ZS28jqGRmJRDAJ6b5SZM1bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=PRP0F79aPiWyVbo9Anauljnft2rqp4qXR0WoM2XbW_mZFKpW_BRQZit10RJHViSqLVpZnuRoHAxtkd7-bXTVGzGhm1CS4MMAkPmnfjGyTWl4NC85IwNQDH25od6LgQvJycfpGuI2gH-JEt1z8FTyXqILL3q6_iQzCt9onQNyBB_JsHrJ96VLUftsmkCE7EApPOb799UtiSmbwyYIpreX8N1qzHjecQjgMuR2N_xstfQHX9u2GkB8hIOKxnwVMalpIIdAavs2cRSy8wf52Gpj7hoX_jjbjlH1v8YikckvFAvhgqwwEEprsMUANQY-eh-ZS28jqGRmJRDAJ6b5SZM1bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBkhmD1-X57RjHQyQx2earoGoVu8RBQi-e_QbHmHOwdJ37g66kB9ylH37zZFmoXc7mWd6Yfttyq-nz0zVrS8Ej-TN8QwX_jSMfqkim3-d-OWDN8S6poQA7b3l3kwoYBW-25ARVn3NOnsM3SoRlY3hF94f60u3xCbgOrRUanVZdxJUz4W7Ho4Qz5jcuqhMFGKqfZVA6xLkzjzQ8uDX973uLXHrV9HQUVTLFUgGkCsNyAwIBE2uTcNWTAoMqfBbk5zBM-IJunzI5V8LpOeo83wVEHHxiHn-HNkFAFYWeeQy59ne1Vqv0b1x4c0v9pMjS9GMDOHigoqtYwBMbdoaSwPZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=BIXplzBrg4jq7RIjr2HbYz4J2XChMajHmAYGRB0s-p2bIhhaSF6ZNc1GBoWzr_jKECg5WarVYI3pfMPCBkFwU8Ksw7qhVJdPvW3xwUcVtfmTPqHAsf-AhQPqxcJH2vlsIcIvsvXVqQkddOf99pdLssn7JZYzh66-llYkXaei2mDAG1NqrexZfZjrtO2cqA_oNuTRtBNz_5PLWvh39Zizb2i5rUhRFj5tXgR6v67-667xh_u0-q6QEkFcocXo8oZtDHxDMUiBjlek6-3NRg3Q7uBaMayLUIsSBsfQQfDNXSGMPjdMCFDzXIKK9npXB_RQ4WwsQ_imZzCWx3etvSS5dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=BIXplzBrg4jq7RIjr2HbYz4J2XChMajHmAYGRB0s-p2bIhhaSF6ZNc1GBoWzr_jKECg5WarVYI3pfMPCBkFwU8Ksw7qhVJdPvW3xwUcVtfmTPqHAsf-AhQPqxcJH2vlsIcIvsvXVqQkddOf99pdLssn7JZYzh66-llYkXaei2mDAG1NqrexZfZjrtO2cqA_oNuTRtBNz_5PLWvh39Zizb2i5rUhRFj5tXgR6v67-667xh_u0-q6QEkFcocXo8oZtDHxDMUiBjlek6-3NRg3Q7uBaMayLUIsSBsfQQfDNXSGMPjdMCFDzXIKK9npXB_RQ4WwsQ_imZzCWx3etvSS5dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2PtEMwt-XW44khEtIoZquTb7hwLv46F7vlccrcUAT_jBRxT_dVRHkN29N8hk-XlzBF06MolFgCarzjX7BUnpXQ1VQA3Sca1TIOxnZHqTIZpCXab6rC1AOR_m1a4rgb-4DVj9oiCv0rG7J54ySbHxpBQeyOn6HpIMV5tMtMRhVil-XBa6vFXTr9Mg5osnKROC-KiuZ5DrokVPlx1bWJ7D8jxoolR7Gx5I9sAE78uBwx94avz8MfP8fYjx0CHo7z7oEXko3PLXStlvoFXpC1knXbf--2OuyFo2VFziv34x53VwA3VinXbO4Ek6Cg4Jmz1ZDO16BB7jl7InH80A1b4mQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_WBsCZ2cmISC3UKuNk8-N7YUzszHnydzJb3Fqcodf9_bcammQXRQW5VhtNYmK-TzwtZ7M38jksy7kf9ZmI1qPw3HceSawxO8Pcchl8nyv5jHjsiig1LgXxEHZbHsjnFjW74VcrtweHBADT22pcXIWGt4qJhLqBzweGA-spAYDR6qKmisxTHa3Ldcnr71BRRK2Jhh-KXIL7sByaAsKskyfHgMrwJTphYCqV070Fy1ohR8NIH7ZIA7TpjVzouGfkl8rQo19xEek3UqHFLUJphQnCUZ-9V5_As5vhj2YdzApeZEvN2yLf5ezUdLad95eONYDEBnhBWHEaEdekYd2Z7QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acYd0eq0rMCo5vhWYPL44aolWJ5AVgGrVbLtRVLrHJ03N2NfzD6H2461GlbC4X4pvHk9LhB3wrgrqRf-oRxqzNamRX4knybaiNzZWATx2P69DNiOBkxnKn2NVXYOZejZJhwkzo-7d1WdvztzlRpFjQMFXgVnCDPNV-xYENB7X6OOV_2o827yKUqUe4FbSz7QjEYyLKL4o-_xkyDiVb5cVDLtTMx8dR4G2X5dh4Yd0af87sgB23lFAeU7PBNh8_Bi1E9FOJAKaOviJkrKMP12rl_C9HWo8OxSoUzo04nYs5WfhEf26q6HNe80akk-QPFWJRRR5uTcskah6BnJk3FXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVPrvkDC4j7Wif_vjOCEDhuX2fksgh22Hbwl1BQ2QVWiuccvs23mdWX1gLGS9l4yWqUDPqvcVyvRgO4Ondume9WmoJNs2YQWyT9JcMHJgJnWceOmPVgTA2JiPZcjpYVi6IpqocNsZHdb6LsEreWDz6n9A0chS4gJ80EQ8mmM5rxhN8CEFqlo5YRg6InS9EkuCiyKu6CtRgQL-NP-EnWBuJYHWVsHXUTVW8g78PcVYLoO5W6qpC1eDZ6SLm4MfzlSBfA2dCNDSnsCEY_xC-piS3C0tx0R5o25Kq7fAn7QG8a_txZ6xryIlRTRj4Uj0Q_DdOzqXeug_IFCZ_GUrBRbMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDT7dvct6QkR3wlVcHFBk3KRgQ911vhRGKkN0OgC37Y5_m7c0Is2M53dxvAgB9WfEvYk_56qoJ8Joh75HFGDyD_XZ0FH2XnIocPV_QUTeJ8jFife1oTu4yNwL_xjVrncR-TpgDsVBtoZCdcZJIkarpPyjdKILSCQcHE7zvZwzrAxbgdtn3Wtd_YWvOw7CvKKtA4iwOL0cjG1n5Cn0Y7E5qryOKBnUPyMVrBk-itlzr-nmPcf0Ajgkf39g_MM3MKddrV5n473eEfbabCk12xVL-TWRccvLEmnf6IDRF3ed41_6G1hJWSdQSezpaPU0mUKgLv_6GrjXVxVixcf_xvIkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=JXM1Dxw1GBpjpV2q5pyBTPQCE9pGOvSQZrMoQlSwnYwjv-0bdNPEEdrLsZGX0xy-pRYxrHkUR5jrLDSvDNOR2VGQyFS_RBRjhJsZvN0dqjoPcTf_r7_oTgMp2lrY-Zix1JXzRl9hXFK8OZIV4RY8g4Tw_q0oMhWbh7aoCJdBUJ4ukrpZLDdfOobHS9UtMshGuVaDhVy2agAqLEy4sZZIoINWvpbkC9zzF9dy5fbM6nglSTugZhjYO7q9KiPaFfZh611LqfplXrReSk6hBinA-ZIX8soPaLoN8NkN43BnTawt1Y3knyXfLg5yDai_TfHTbEIvhJVNqClY6XZexQv0iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=JXM1Dxw1GBpjpV2q5pyBTPQCE9pGOvSQZrMoQlSwnYwjv-0bdNPEEdrLsZGX0xy-pRYxrHkUR5jrLDSvDNOR2VGQyFS_RBRjhJsZvN0dqjoPcTf_r7_oTgMp2lrY-Zix1JXzRl9hXFK8OZIV4RY8g4Tw_q0oMhWbh7aoCJdBUJ4ukrpZLDdfOobHS9UtMshGuVaDhVy2agAqLEy4sZZIoINWvpbkC9zzF9dy5fbM6nglSTugZhjYO7q9KiPaFfZh611LqfplXrReSk6hBinA-ZIX8soPaLoN8NkN43BnTawt1Y3knyXfLg5yDai_TfHTbEIvhJVNqClY6XZexQv0iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=MLcYxvP68noKbu-dm8xNZGG-_C90BJDrGXlueikq-YClvNeXAJy2Q0g76MZu0cTUqH6gaYTkqKH31iI0kOKMR-S1Y_-vij9IfbRIk9eVU_XwEMbdSTIYD6CHtETxVnzOfPITtjTTR9wy1Gx-0T40SugfNqJNZmtn1u-Z2zQe2nK6044rfig67rprtj4FpJUAGcGfFwI2yadIpqPDcWkPXoSUfmQaCkJrW-gtlYa40JM5JNNmguw-vHC0UUSW1rssWDgYoJ5Jj7-THmVnY9adAuoR4BppMmiETSnmOWHTcGYdgthHHE6SOvpS-IDZwaICujbU0WYwfm-u4PU_gleaUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=MLcYxvP68noKbu-dm8xNZGG-_C90BJDrGXlueikq-YClvNeXAJy2Q0g76MZu0cTUqH6gaYTkqKH31iI0kOKMR-S1Y_-vij9IfbRIk9eVU_XwEMbdSTIYD6CHtETxVnzOfPITtjTTR9wy1Gx-0T40SugfNqJNZmtn1u-Z2zQe2nK6044rfig67rprtj4FpJUAGcGfFwI2yadIpqPDcWkPXoSUfmQaCkJrW-gtlYa40JM5JNNmguw-vHC0UUSW1rssWDgYoJ5Jj7-THmVnY9adAuoR4BppMmiETSnmOWHTcGYdgthHHE6SOvpS-IDZwaICujbU0WYwfm-u4PU_gleaUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=YQBsaLzmOTv0faaV_CMDQNbio32zxbjGNQMCUWDq3ZkEVXwsoPcpuO2mQ-_dSYSoqyEhmOehidEQOijt_EQlR6uf1Dvl_3YhNNW_mVMT6ydcmdp8-no-w05iBgUm72cRQPmTqJ8z-Vchcox-86ZTg1O1FuJ_J17gLpN9Qon5jb9o3iuU_gRzNyzg9tJVN1WDqlto20PCmTEhlcRE5s6YnNtnvsWjTCuyPEQQEIYXoilehfYbIrQUNHlkGVbIH6KQZFqqZk0hk-8DhqL_0Z-yDy_Rx0qAhG3qkWu2KbgGq29fUNgW71we--VrVCnsg6EWc5EQTjjoNbjY04G9v_3SLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=YQBsaLzmOTv0faaV_CMDQNbio32zxbjGNQMCUWDq3ZkEVXwsoPcpuO2mQ-_dSYSoqyEhmOehidEQOijt_EQlR6uf1Dvl_3YhNNW_mVMT6ydcmdp8-no-w05iBgUm72cRQPmTqJ8z-Vchcox-86ZTg1O1FuJ_J17gLpN9Qon5jb9o3iuU_gRzNyzg9tJVN1WDqlto20PCmTEhlcRE5s6YnNtnvsWjTCuyPEQQEIYXoilehfYbIrQUNHlkGVbIH6KQZFqqZk0hk-8DhqL_0Z-yDy_Rx0qAhG3qkWu2KbgGq29fUNgW71we--VrVCnsg6EWc5EQTjjoNbjY04G9v_3SLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TER4S4_qQlIbC30s2OWkjgMFE9Zm1yMhOklp9eF5LmW4N6FuLATHJEXzq79kV4UmGpiA4oOAt2jnaa7p5yl3Jr2PVbEZtDH9BxcHRSldKX6W6TYbOB-Stsqk7pcOMMQu3Jo0nFia5tscCzaWafFuZSMJKcRJZ1RilwbiT6zqSf7WvJQsN8JQmFxgpyD-YayWZusfq546O6Qaui-pbbqynfGs5gAAeRONK0IhAqf9Y7oS_AgeEBBJ19sP_kWXt4pjyHVqwPwIRRFPwkwRLtHNahnFGThFSycrCTFsi97SZB7UIw1R9DykthumjGwtImSRkMuAHg5eKPOsnvc2bNYXgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=exUbfUrXVuiVNwWJrWr0B6p8ai_fwtZpIIzIGrqAxacEULqyV58W4UL-5dLOy5f_f4b1JG-ytXDfhLQxb84iQQ5QYWhxsL9JYBeOK182vhSfMa_wxB8hFS7VIpVxbgbJBsdS031wqCPzRdImWJ5EAEaPCnpjySwMg73z8GHqs3auJfOMwIKhkSxtI-3Sa3qm5r1_CEAgMoW17TklrtUDMwaBWFnuJRoSaN_uUAvUElEHVrdfqXMhRi7EKMnSV0ksRJDnFo442BJ6LXmaN6YZTWyoQJFvnw-MNu8X2A4pkZoZhmfcjWXuC-N7Qak9rauJx-1TsACKBm1KreEAvbT5SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=exUbfUrXVuiVNwWJrWr0B6p8ai_fwtZpIIzIGrqAxacEULqyV58W4UL-5dLOy5f_f4b1JG-ytXDfhLQxb84iQQ5QYWhxsL9JYBeOK182vhSfMa_wxB8hFS7VIpVxbgbJBsdS031wqCPzRdImWJ5EAEaPCnpjySwMg73z8GHqs3auJfOMwIKhkSxtI-3Sa3qm5r1_CEAgMoW17TklrtUDMwaBWFnuJRoSaN_uUAvUElEHVrdfqXMhRi7EKMnSV0ksRJDnFo442BJ6LXmaN6YZTWyoQJFvnw-MNu8X2A4pkZoZhmfcjWXuC-N7Qak9rauJx-1TsACKBm1KreEAvbT5SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EW05zEZVBlDXMknq0q7o8p3GHyWgQ64bHE0UKWGhQyahgu16OQj9dgSp7EBG4thoQY5XLe8GUd8Ipis35uXxN8kzIN74E1k0Coir9yadndSYNSsPWBEo0SYOV89tkD_hsWs5CiAQZ9ivEXGhy3YaLxN74jMmM8rz1eB1O4djdrzKAz36v9xcebL0xtjK5bsOybsBuiJ2c0JHiP9P1mSFlmUr21wp3wYd681nO5qlOQiEf5voCI5mZj4nl1FNtlp21_30aGOTiqmlV90s6Pyv74dcNbB7mbG8SZci6Lnk3YZubEZDUEfdj_6Z5ZOzKzgxXyXTIwrKnSE2MxXjULfZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=RuKqC5vlyd0d4QcvjBTnX0pDcy4bUiuFerNiiCPVTKunYGJPcyhHbLbmBzsRdQk67oLurgRtGR9f9EVAqqhPtsBepIFCC4dsMviTPRzSeeVZHqj6G0vjQQfb3N4HIPH96pG9SJ6ia8PRuRKjLGQ9LN6D_w85Ev9NIPKS-KkTVC_3H5wbAKfd6KRykf_xASV2LD79SX_sRE7tkl-5iMiTTFDxwwUg9uYEnbDkpau9CVb2zyOO0zY_I6Wt6dfuzO9_VlxnLh--yNXrdjt2Y4uczWItrNdsNG-9L5XiXnhORYvjXlOP8KSWnDQbcA_o2SjMnLYYFXCjA5--vaaCZAR4BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=RuKqC5vlyd0d4QcvjBTnX0pDcy4bUiuFerNiiCPVTKunYGJPcyhHbLbmBzsRdQk67oLurgRtGR9f9EVAqqhPtsBepIFCC4dsMviTPRzSeeVZHqj6G0vjQQfb3N4HIPH96pG9SJ6ia8PRuRKjLGQ9LN6D_w85Ev9NIPKS-KkTVC_3H5wbAKfd6KRykf_xASV2LD79SX_sRE7tkl-5iMiTTFDxwwUg9uYEnbDkpau9CVb2zyOO0zY_I6Wt6dfuzO9_VlxnLh--yNXrdjt2Y4uczWItrNdsNG-9L5XiXnhORYvjXlOP8KSWnDQbcA_o2SjMnLYYFXCjA5--vaaCZAR4BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=MuxcWvjHXREUy4ziglgwVgR0Z1iuRa7QegVAQqVXz8IUZ-W8lHCnmdigZQ45DQWVZ4_bIzhXlJW5pVqt6JD6xAmjwC1ZV1y3oFXcpdLbaubT4dzkCQMzsV80Af1AM4oXPVEyg0AAe2xfTVxQPyL-WLK_Ho9SiFBJyEVWsY08uD-US3JK2MwLosNcgTEQ-_t2-f3_JiOg1QSIIiUwDHyoS2lUNMQPSx5dAMFwYf84SwoPdBawRipzPB_Oc8tKG4mnUoQS2oz2Ni8b-j6_OKGqRYJgC_ghZNijvPg7rJcZiTZ8Uz-YJjF-NOXj21ma5XVyR7lPIThATJvWaJa2CPvJcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=MuxcWvjHXREUy4ziglgwVgR0Z1iuRa7QegVAQqVXz8IUZ-W8lHCnmdigZQ45DQWVZ4_bIzhXlJW5pVqt6JD6xAmjwC1ZV1y3oFXcpdLbaubT4dzkCQMzsV80Af1AM4oXPVEyg0AAe2xfTVxQPyL-WLK_Ho9SiFBJyEVWsY08uD-US3JK2MwLosNcgTEQ-_t2-f3_JiOg1QSIIiUwDHyoS2lUNMQPSx5dAMFwYf84SwoPdBawRipzPB_Oc8tKG4mnUoQS2oz2Ni8b-j6_OKGqRYJgC_ghZNijvPg7rJcZiTZ8Uz-YJjF-NOXj21ma5XVyR7lPIThATJvWaJa2CPvJcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=VinS0L5QRoU1V8OVjQd5xOCJBlNjlEZceZZ94fDTHR2Z7IYuR2dAPRdoygXr72fAhvwo9BiY-8-CSA8LY2j4dN1wo8OhKCCXqwDpNiaWGc-Jdbuz8bgqPK-fLbUsjd8Z0Na_yztgQrQMafujyXNyPV6OKva0qaHjdyhjeWa9cyUv6d32ppihUJ7-C5vM0CfeO2sN_EN9qRIg-ySvQ4PwmoD7wMTVOgYD8X6ot8fzk1_LqrHSo0uttbtx0qZ64N5213rdxf1lMEnQuEMU_WVA-9eel7CifNrHd1yT9dDFwhwqmfmq_l72NiPcXERifH16-x1FlfEvml_k4EjMygnuXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=VinS0L5QRoU1V8OVjQd5xOCJBlNjlEZceZZ94fDTHR2Z7IYuR2dAPRdoygXr72fAhvwo9BiY-8-CSA8LY2j4dN1wo8OhKCCXqwDpNiaWGc-Jdbuz8bgqPK-fLbUsjd8Z0Na_yztgQrQMafujyXNyPV6OKva0qaHjdyhjeWa9cyUv6d32ppihUJ7-C5vM0CfeO2sN_EN9qRIg-ySvQ4PwmoD7wMTVOgYD8X6ot8fzk1_LqrHSo0uttbtx0qZ64N5213rdxf1lMEnQuEMU_WVA-9eel7CifNrHd1yT9dDFwhwqmfmq_l72NiPcXERifH16-x1FlfEvml_k4EjMygnuXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=Jrmd4g1f5X73SYfWlhd12tcsgZTV_OgWj9zw8hkJzE64IfvOxeNF_yNkcj4mFlOnGr3koM8RkHMFxnQ5fT-B8W26MB0ea2ZOiMLzka336SjDnDGdtb6a5ex3hF8Sgfw2ZTm5hLL8pB3VhWUoOzY2779-J-qiTKFmXz4yQcgQAD6znrYv8oxad14wRHqR1Ib_3BBGCbHQrA6-r8BEJYXfDQLi0Efb8BuqtLFmXHf29bt6H1sscxDiOg6xCK8UDpv6_XglkHoTYmy0i3lmDZFw9YqZ4zm1oXrQGMuVU-4YlnoeL66hdPtHh4UTqN0hmlWxMGRRt_o1DhQEYQOioyaT8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=Jrmd4g1f5X73SYfWlhd12tcsgZTV_OgWj9zw8hkJzE64IfvOxeNF_yNkcj4mFlOnGr3koM8RkHMFxnQ5fT-B8W26MB0ea2ZOiMLzka336SjDnDGdtb6a5ex3hF8Sgfw2ZTm5hLL8pB3VhWUoOzY2779-J-qiTKFmXz4yQcgQAD6znrYv8oxad14wRHqR1Ib_3BBGCbHQrA6-r8BEJYXfDQLi0Efb8BuqtLFmXHf29bt6H1sscxDiOg6xCK8UDpv6_XglkHoTYmy0i3lmDZFw9YqZ4zm1oXrQGMuVU-4YlnoeL66hdPtHh4UTqN0hmlWxMGRRt_o1DhQEYQOioyaT8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=awlXaOLlPvggMSIpohdVQf7s0sgH7M3FzKZUXSWCl_fEKYsDJfBIUlntxq9tV5BV5oGvgAKzhP9cNuZOwwpv_d5CqjcN09HCJZ3giXX-J6tyQMV1HZH_hT1xNXpvmFmK3f89-fn1L4ihTf6GnB8aiSbFR3RztMZpAV1fERA3Y_vHCJsN0cmBuXzEehDWOciZp9y4KnnH8WAAfi51hUOe1Uy0qg5n_LRtI8VP9tZBmulx-M8qJdJapVeatyo2rBhfW3NHz8Z35cMXnKbCZx3E91Qitb2LvNAV71NKuazPJm1XgQeE7C46W_JrKpWUPSpoeASxJOrXaZ_ZDiuF-6ggSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=awlXaOLlPvggMSIpohdVQf7s0sgH7M3FzKZUXSWCl_fEKYsDJfBIUlntxq9tV5BV5oGvgAKzhP9cNuZOwwpv_d5CqjcN09HCJZ3giXX-J6tyQMV1HZH_hT1xNXpvmFmK3f89-fn1L4ihTf6GnB8aiSbFR3RztMZpAV1fERA3Y_vHCJsN0cmBuXzEehDWOciZp9y4KnnH8WAAfi51hUOe1Uy0qg5n_LRtI8VP9tZBmulx-M8qJdJapVeatyo2rBhfW3NHz8Z35cMXnKbCZx3E91Qitb2LvNAV71NKuazPJm1XgQeE7C46W_JrKpWUPSpoeASxJOrXaZ_ZDiuF-6ggSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=CjTyD9Lw_lHf4TG9s2nYp_9-rh6NM7LjPDUdp2pL-mEgzwUwCD5O6za4Ex1g425nsAeUFMQmI6-uMBvrvLJgkVHUAQPvMaQQJqvENVEMpeg5fJ61Rnm3BDGLO3XIVbNgjK_dRRDdHEqcqY95O9NSfsJKZ62IGZokn_zlHv7_NMMsBFiazoVf1YIPLHKLnCEl98Ubut7lgP5QjOW01FEqyTcFanTZkEauHRUqNzxGCWUtzDS0jVP6yuv8i5HddYqYBCDeRTXC_egcUYf6am9BMvzAtR-wE422HBq6W6APZbLDgV6Nq8ShWNKTpu5YTC-7anv0pi1uuP4ZV7GlhSxR5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=CjTyD9Lw_lHf4TG9s2nYp_9-rh6NM7LjPDUdp2pL-mEgzwUwCD5O6za4Ex1g425nsAeUFMQmI6-uMBvrvLJgkVHUAQPvMaQQJqvENVEMpeg5fJ61Rnm3BDGLO3XIVbNgjK_dRRDdHEqcqY95O9NSfsJKZ62IGZokn_zlHv7_NMMsBFiazoVf1YIPLHKLnCEl98Ubut7lgP5QjOW01FEqyTcFanTZkEauHRUqNzxGCWUtzDS0jVP6yuv8i5HddYqYBCDeRTXC_egcUYf6am9BMvzAtR-wE422HBq6W6APZbLDgV6Nq8ShWNKTpu5YTC-7anv0pi1uuP4ZV7GlhSxR5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=qjHpDL_dK3H6D1th_7ORYQ9Qg-in4k9lDEW3PTjz1ZEIVhLDVuU8Uc-GioMVH6FC5_M60fpMGd2zkzLwtxtP5eaN6qA2q5DVxH-7X3SpdokKOSntPCBIvXAyfd-iih78UfMSUfJBt98CdKMkJDH-MXbmoaonnPtzZhAxO_LB5Yrt2m9YIjbMbG0v9xUGtasgQ74VXkSx7rIHid_vNIRVacUgSm6-NE337r3YUvcI2O4M0-_FIr-4Y8V-kqy55xyYCTlURFfoSmfmHvHEcN_dY975iO5Mw-CUd9ipWskfIW9UV0inIZWn0TFF72VF9B5y5CoSh52hfHqWcfV24XSekw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=qjHpDL_dK3H6D1th_7ORYQ9Qg-in4k9lDEW3PTjz1ZEIVhLDVuU8Uc-GioMVH6FC5_M60fpMGd2zkzLwtxtP5eaN6qA2q5DVxH-7X3SpdokKOSntPCBIvXAyfd-iih78UfMSUfJBt98CdKMkJDH-MXbmoaonnPtzZhAxO_LB5Yrt2m9YIjbMbG0v9xUGtasgQ74VXkSx7rIHid_vNIRVacUgSm6-NE337r3YUvcI2O4M0-_FIr-4Y8V-kqy55xyYCTlURFfoSmfmHvHEcN_dY975iO5Mw-CUd9ipWskfIW9UV0inIZWn0TFF72VF9B5y5CoSh52hfHqWcfV24XSekw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIQ3sT269aABAYrEJwfJ2BJzvGCzC1wyZxv8_U74KrFKaTV_T8C5QrflNiRHo-QkVrtIIVCq8ixWFOWGHLxXJfgqcutOR8E53QAt0YhH69GLeUZ8Uh9Xd3hzvS_F9y1jxh59qi9Xu9T56WR_PHL7od9rftDaIt-5zIu59MtDUQr31jkDgIoSIkBjxdOLA1dNoNrzSgS9ZW2sM9DrjrqxbGCvHeCnCGnjZMWWJPHEHK4hd1p7w-eSOVdsaPoF9H3z13g-3V65-0QDtqit3dAPxnAlfmKFz2o1tYkwGP_aMlOdSSnPSyxWhuVqiTkVRwX_w2LD7sJYw-uixjsR1mqosA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqbEfSqHtFhUJj4Y0ADXhO-6N_WYwd8zZLifR3zt9owpQ57JjcqdJVZTvwvaBfXZS3QW5ayf_C8QNcnEQST14WrhLTJ3jrBdz67jHwaxsDO3ArEN_zIbsP996WRiKJVYHOvkqFCDtcb74fSdvAX8ej1sFAARHXwbpqtk3YhqRqcvT-BhQsuxLJv9_3U6x31waZk_1j8EKnUbUYSfoKXaCcgulw5bJdSnSjcF7zvT9xafCQ1WTCxreXzF-WZWCqs_I6KBHTZw00A0Ho2w_yMwd6Ww2kIOdRGByRwPFd2LGZiFunXjACccxomDMo9izh2uWwuZ5Sys_ICMzFh-XU--BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=RuuftW6JT4FdYsQwBgDLvjVhCuWwmdTRnHfUIVfFAyvD6tlKV3UE_UaVDkL7X41ID0-l6klNf1oOQuc7bir1OiCmB_MMCOIdUjnC81RJmuy011DqnPYa4Z34w_JliMcetB_VRe7As-2luEu8A3X0-Yf0FY4mMZZqeLn3cZk0AxirSDTxNvvg133Fx2XIe-2XTIN4dKYV1_ZxJw8jbb7NoJwggQBBh8HNxbbB9FZdgnc4DT4CRX0ZGPJpezrTnbYvmDiNwzMbTDCNXyXtb3DjZtExto1AxCIVMzukOeGPmGRkLk6wyLoSuLSEpWTEoUFAQ6F4v2uDK1Iqrbd4-wixFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=RuuftW6JT4FdYsQwBgDLvjVhCuWwmdTRnHfUIVfFAyvD6tlKV3UE_UaVDkL7X41ID0-l6klNf1oOQuc7bir1OiCmB_MMCOIdUjnC81RJmuy011DqnPYa4Z34w_JliMcetB_VRe7As-2luEu8A3X0-Yf0FY4mMZZqeLn3cZk0AxirSDTxNvvg133Fx2XIe-2XTIN4dKYV1_ZxJw8jbb7NoJwggQBBh8HNxbbB9FZdgnc4DT4CRX0ZGPJpezrTnbYvmDiNwzMbTDCNXyXtb3DjZtExto1AxCIVMzukOeGPmGRkLk6wyLoSuLSEpWTEoUFAQ6F4v2uDK1Iqrbd4-wixFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrJyB-hs7GwwnbtVfsquAuId_aZP9tpkMlZiWeLfZF5XPeOEspTf3Sy_Olpl3MnI9MFr-JX2ywO1Upb-xIbFccYyFuf-7KEItwgNtg25MpqVfAugrFyPGU0FIT-s48iENRhSW0YiG2KF1dRmf325P3NLxTZ-gygjQba9OwUQaiMbjyJEPZIfovbonpNz7ErBkK1zH9A71Xe3856O8hAmT43HTmzKOkDF18pCRfX5NWbgt5mpd8Rjh0SO5c-LK8c8NsR9ZmY8oBpyHuvybHgu9wHQp9OF0yqCBNvoJhZFr7ms0ToBuD7ribY864kDTbpcOMg7XLaK0i-ZPzBPCktgqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اگه توی یکی از کوچه خیابون‌های ایران
شنیدی  «خدا بیامرز» یا «خدا لعنتشون کنه»
حتی بدون اینکه اول
و آخر جمله رو هم شنیده باشی،
می‌دونی درباره کی دارند حرف میزنن!
و همین خودش خیلی چیزها رو
نشون میده.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSWqp-IRpsHbVfSixeV4SUbdE2YXo0bPrwVIZ3l9Hkp0lJwZYx7CJAGyHuuM7lxWsrPzemzifes7_QFxaRZsUIWjhLBm6uc7nht6XCZ3TspDEIWACnV7mHfvKMmb-cnjc-2yPyXaMpn95dJF94tVAkf8oEmSG-zSRSVWXTr54IFD_-h27hOgQeZ2ykt0XD8pdTKbNeCa39GZh0nvfPUNH8QyR9A_QqAk-Gbw5Rqxu5w363kS2OB9lySEAW0kP_e37yc99CzE5Ps-KmGKlFZb4tTsFjTsXRA6fTUq4mXhluhwB2M5fH6OjmDbfS7kfFavcswoqBngIpW41uuKidRh7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=icrsiDrxXxZDrs3ijYF21pGzJGp8j3lZvaIIQdOvvQAJY1uyiUC0YR7iq_v4bIhBcZzCRVnpMs6Dt8UcJ1v_G1RfFaatvo10wNy8a2chzoGjSsTZx1i6a4S6_d3rG87WvN9H4Xje2JChe0njIqutZwbMdHejcbJ2wUYgqEjsjTzgRgujuIye7f2A6FW-AMtC9_S461--E5RN-NsAzgLGp986A4gY2Ar7P4gq66IEO1JgyalPD15XyHBDBJaxxKF7dloscVPYjqlbvSomkKDZEKDPR0F7-memRdnHHvd-7ef-GCwNC_7lww0dukNfhh6lO_ilMIkuv6lUzS0ZragFRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=icrsiDrxXxZDrs3ijYF21pGzJGp8j3lZvaIIQdOvvQAJY1uyiUC0YR7iq_v4bIhBcZzCRVnpMs6Dt8UcJ1v_G1RfFaatvo10wNy8a2chzoGjSsTZx1i6a4S6_d3rG87WvN9H4Xje2JChe0njIqutZwbMdHejcbJ2wUYgqEjsjTzgRgujuIye7f2A6FW-AMtC9_S461--E5RN-NsAzgLGp986A4gY2Ar7P4gq66IEO1JgyalPD15XyHBDBJaxxKF7dloscVPYjqlbvSomkKDZEKDPR0F7-memRdnHHvd-7ef-GCwNC_7lww0dukNfhh6lO_ilMIkuv6lUzS0ZragFRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک گروهی در جمهوری اسلامی نشسته بودن و برای هر هیئتی که برای ادای احترام می‌رفت، یک آیه خاص قرآن انتخاب کرده بودن!
یک تئاتر و شوی آخوندی!
مثلا برای گروه‌های تروریستی حماس و حزب‌الله این آیه‌ها بود که آفرین به شما! کارتون عالیه! ادامه بدید!
برای عربستان این بود که مسلمین دو گروه شدن، خوب‌هاشون (جمهوری اسلامی) مبارزه میکنن و بدهاش (عربستان) کافر شدن!
برای حسن خمینی هم یک صحنه‌آرایی کرده بودن و یه آیه‌ای بود که مثلا تو به اندازه کافی جهاد نکردی! (خامنه‌ای خیلی جهاد کرده بود!)  و….
ولی از اونجایی که این خودش نوه خمینیه و خودشون این درس‌ها و مکرها رو به بقیه یاد داده بودن، وسط خوندن آیه ، احترامش رو جمع کرد و با خودش برد!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=GPtVJc2HU_niOQ3KTsLaXjNzHlm2gjXfCB2dFSjqTNJ4scf7cg3w4IA8pXSov7jUhijiS3-THFvZrJwl0fD46nH5LQPJAb14DI9K_BtIb3Wl_rG0oQTlLFmr5LVzxo7rP7VhCdSpyi1UM-p8WEmUj3mqAKKmqvAZhE0QD-wV2igULYc3sNZhMOt0YSr9Aee3WiE9f0C-ETX46gMeFquIx4Oabvkl2lePEH9Uf2VAX7ZirSNXm0eqaefwTkF3I8SezGXGCacD6gigacCXQPZvUcQ6jJ-9AxxVz96deCwEoGjgOcYyNUJqBhut_Tgd8nh-gWbTgUsepyCDSYE80vVuuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=GPtVJc2HU_niOQ3KTsLaXjNzHlm2gjXfCB2dFSjqTNJ4scf7cg3w4IA8pXSov7jUhijiS3-THFvZrJwl0fD46nH5LQPJAb14DI9K_BtIb3Wl_rG0oQTlLFmr5LVzxo7rP7VhCdSpyi1UM-p8WEmUj3mqAKKmqvAZhE0QD-wV2igULYc3sNZhMOt0YSr9Aee3WiE9f0C-ETX46gMeFquIx4Oabvkl2lePEH9Uf2VAX7ZirSNXm0eqaefwTkF3I8SezGXGCacD6gigacCXQPZvUcQ6jJ-9AxxVz96deCwEoGjgOcYyNUJqBhut_Tgd8nh-gWbTgUsepyCDSYE80vVuuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با امن شدن اوضاع، سه پسر خامنه‌ای هم پس از ۱۲۰ روز غیبت دوباره ظهور کردن،
اون یکی‌شون همچنان در غیبته.
رافضی‌های جمهوری اسلامی اینقدر کینه‌توزن
که برای مراسم خامنه‌ای، ۳ رئیس جمهور قبلی
(احمدی‌نژاد، روحانی و خاتمی) رو هم
دعوت نکردن!!
بعد در میانه جنگ میگفتن «علاج در وطن است»! حتی برای خاکسپاری رهبرتون هم روسای جمهور خودتون رو هم حذف می‌کنید و راه نمیدید!! تا این اندازه تمامیت خواه و کینه‌توز!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=mr1bH8BrehnHG5A_84S7-pJHrYXrwF33ztpTN_NNNabC-NZEJPbJdO4nkrOfAS6hNV5goylEuAGxOyEkQtfohaGJ77aKE5UOpgQ3EfLPgQ4fPHSwvWk8iY-uJC7ZnKe9yCLSqxAaVtzbGhjJH9-rxsHzitSNaBtiXCgcnIPGljHQq5F4Swdp0_DeLFn6VxgEQGjaJdGogXiA-srNahEIEI_x392_77JzyINecA4Jx78YJvP6N97YLGpVt6Xx21B3Df-TPOHvn43OUCtOru2EEbiN-lz581U-0BNB0E5MLkzUFIrlgPWZgm7VuYf-Uo2b6FwzBkEg_0lZzvvRVxb2pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=mr1bH8BrehnHG5A_84S7-pJHrYXrwF33ztpTN_NNNabC-NZEJPbJdO4nkrOfAS6hNV5goylEuAGxOyEkQtfohaGJ77aKE5UOpgQ3EfLPgQ4fPHSwvWk8iY-uJC7ZnKe9yCLSqxAaVtzbGhjJH9-rxsHzitSNaBtiXCgcnIPGljHQq5F4Swdp0_DeLFn6VxgEQGjaJdGogXiA-srNahEIEI_x392_77JzyINecA4Jx78YJvP6N97YLGpVt6Xx21B3Df-TPOHvn43OUCtOru2EEbiN-lz581U-0BNB0E5MLkzUFIrlgPWZgm7VuYf-Uo2b6FwzBkEg_0lZzvvRVxb2pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWpNe7PvoagCzz7yL4DVQ_xF9ydNZqsaIhx7PK8ItV4sHG14kdFrHAbITXMCFOjA7ezwbt05cFH_Vg1eIgQ-pOQ4dUzFkEdhhIqIISAjWCq6PgRZvo2a_EEh8aoPjIfEbw8gglIGjbAg0bxagAqIPQnnGX84H2xspOfcmhN4Vle7ZEbaH_Yko3CQgw_iWI9ZNWZF74nsxMDhd1brQ_XoaofHQgG0ox2dUvt7iH72TbsnRUiblVVw8KGraVMdv1gXHQj0WHjjnL-jbZ8mHiSaNT2FIJkOKvRaQdHaUs6MtpAp29uAT4yZOaf0aF7zTmHGU2P3ZWodYTNaw9JgHv7JQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDAQYgFMETMbIYV4sJfkkTtGTmaxgvSNNS-qTkQ4QFg8NVJsMsy6dvmV8e4ptcsfHOK2kIryJS3MsaF1Me6AukHwi1AeLVWyUOcL-uvXA9b4Sk1G_3hbGLhQZ3B5BIBF63y2gi8i81Q1iXRZXcjZN_qdzmTv_EF0ph_LKXeX0xbi6BHlmgRAs4HywsfHiKDhb03NehjoMD_MszgkmTkSAmab28RmjX4P8WDOsmpJqBruthSO57mTGm4aSbMG-tM6jfp5l6BvBOesMOS9i9b0cpkb76G31d6-UXZxIW5CHTPlnJMBibYIzFp17xdhV-6gJWc-e1QKGyE-p7OhySnodA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=DRQiaLu21LC5G98jn3NDK2Kw-XQJPbd7deXhU1R4lg0T9vRVGjual8HG2J4MyVKR7ZgniBrCYhEf4kmQZE7iV94xTm2VkU9a196mgckBSl-o_xA4go8jPUMZhll_VJlczCiMb9FlwXExae-tGGt6ufDwkQBqwrQUSOhC5bkJyAx2yDH0fosfVbpdMRYcn80TBmsdwMZmgkuoP872-8Em1KWdl1I1Qoc9RFwCmoAgq3dnJeFoyV_gU0DsXxmHV_A7-iQLDhYeC-y-Qqz-sLOtfFXbSheIhfWSxMPYtWLQqHqCLoDukuDxG2mVfUWueXlrhgJUXOahDlBjm4k4f8etlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=DRQiaLu21LC5G98jn3NDK2Kw-XQJPbd7deXhU1R4lg0T9vRVGjual8HG2J4MyVKR7ZgniBrCYhEf4kmQZE7iV94xTm2VkU9a196mgckBSl-o_xA4go8jPUMZhll_VJlczCiMb9FlwXExae-tGGt6ufDwkQBqwrQUSOhC5bkJyAx2yDH0fosfVbpdMRYcn80TBmsdwMZmgkuoP872-8Em1KWdl1I1Qoc9RFwCmoAgq3dnJeFoyV_gU0DsXxmHV_A7-iQLDhYeC-y-Qqz-sLOtfFXbSheIhfWSxMPYtWLQqHqCLoDukuDxG2mVfUWueXlrhgJUXOahDlBjm4k4f8etlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=XNR4ZrLgyeNvknNlh5B5SdRDs8oeXXnDReUjF9rBBqYARA85ldBCy8SJLxm5xhGdik9I9LWB0SDs2xSv-FJqMh7p4sLsvUEvhvkdslpJj-7oWNXCWpX-KhW8vYoh2j9CNtoliRwweAgth17maNsKm0GZG0CVEabvIEDPOS25HAXT51IlNJXRLXfcYoTN-BYGFzBMMqkbz69a4Ans0ug4Yf8ieDVwJXSs9v7qT-v53jTvSLtVat_jarFeb2hPQxl0qWSkUXegHT5g8GDjoFiq0A_WsDe15BiK_EgFxWxqLj3DgrgQyqS5PkYWmWUgay39B7Q_s88lExjgw8x3L0XaPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=XNR4ZrLgyeNvknNlh5B5SdRDs8oeXXnDReUjF9rBBqYARA85ldBCy8SJLxm5xhGdik9I9LWB0SDs2xSv-FJqMh7p4sLsvUEvhvkdslpJj-7oWNXCWpX-KhW8vYoh2j9CNtoliRwweAgth17maNsKm0GZG0CVEabvIEDPOS25HAXT51IlNJXRLXfcYoTN-BYGFzBMMqkbz69a4Ans0ug4Yf8ieDVwJXSs9v7qT-v53jTvSLtVat_jarFeb2hPQxl0qWSkUXegHT5g8GDjoFiq0A_WsDe15BiK_EgFxWxqLj3DgrgQyqS5PkYWmWUgay39B7Q_s88lExjgw8x3L0XaPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFpyltMW2-9jdrXe4B1dJo9Xq_Rxcx-I2yACFFZ91Nmgu4ebaPTgD_0WJPthlVwA2XMnEA3MPOSs8bU8hfyRrZhwvlqij3vYnBRMjkQmPFNjrgF145_WizWHnRQtTRtjUBF5FSrhHsKppoZc9lPfO5BNpkEqgx7YqjntNsL6ewelr1qjFpnpDeaTVJKVhBfPUjTWH4KzRG9e6oFArVPdRn8N0wfLKT1A9aLFqlhu_D_tVX7KOkWdkxV9BigxJ9H4wW3kZqVCOFMPZxxmbbRZQBnE9wXVS7K-wNIrd3MKucmW3vTeE7kMPK5qeS1vCS11kExxaDN7gMj2IrULMXiuOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBgwravvWXCxDIGIGKyOhfelsRih4PfTW8XQ86tzxth88IjoVLj-ymn3K9DWfpoC6SdoPjp1E0y6CbEuEfacPEu8G4Ns4ybfbmbzhhJ62jhvP-Ej5t7M_imCo-BZ6_HYGhsvXhf6gcOFxj_jyOn-R-K9XWAEbQioL6TsnaPO-1vhlerEZY92M7M8BBsgoUJnQOypj2sjJyWX_IWYOi8XHkRgKGITm9aKvvUtPNiFeH0yNYW-9yJNV7V5oeWrFqpuoNZGxHynKeSr_SbBsDddIVzZhVdQgIAO6jebE7_GnOh1QxOgB7WigR2j1fVIGNJm_-luHk95wWsnqvfNAMYHZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuS1MX_t3zHwpLkD9HnN8Meo5ulO75zUBTfaGMGNEMIP-SXzAryNxsysmupan6upmuT2mLO8n_NH1DZq_4gYGiy0P5WFpHmmPlTtm3YOa88BK3GrwC-t-JfIVarrKpthWdV84LuLK4P-UAmnWuviutdqMDgIUfZ109CnpxuqrNyHS0hNqnhfudMHqN9Bsh4zwsIF_iQchP1GkKCmMHUVxXd0iOsgA86COxj-SfE4pMSJyjkd3k95tYqKW2bOR_wIZw6QFzKs2T2C97LmS187yF3n5g8PPz7zVpbOirDpPbhtu9GdX8ULuB8YeFp2a4_rBwXjOqsWBDBSajTdniZBLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lF0_j5tfk2PUeis2ZWpr81q1MNL60fmjKeTV4h3xgsnWZzrg2EK2nwIoW-ylhOvhkHxyANWMOdFu5fSzmY8TKwPHE0UZCwxX_m8pS9fd-EKIZzxZUo3jlZpY7jVFNdm7g1zX8QaVQfkRMrdJYNsJg_KNp7JgSBOS7hD8j6KNL3g6M4r2QyP_8zTcVTY-1hVCjiuwH81cabs5pbKBvbC5py8X_1fE7wODSI9c3NVF5IH6av1Kyiv-ER7IsWwmrBqiVgOW9ilO9OspcHLf_VwxWNSaT0elFE66BLrZHGdJEc7BOsARMct-NHtl7KV_guSdP5lhDXJLgl647SlqU94A4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVrWh1GndPlWfvhn-nlW62mczkO3LInej71O41FZy44wr5r8vUPsTCqnsHa6Wj9mkTRszVLaU5FC1j30P6oJtiW6PFjKZeXGuWhamFe7GSb_X5rTA-eviD5vJY7mIMKauGWvgDoMYdrCWQqj-6uefgEzt4rAF3OHIeDAhGAzzqBDj6KjCUZDtCUCy5SCpNinwHve5VHu9p-dEuua75Ifb4eTOSSVkSKBybz7BiWQMos4kz93Sl0mfhQuI5MhSuyeMJ_VmwyYmpXzK2dgSlIw7et2tBVRhxOD8256brrKv5248OIaS-Jtv5moeR0k9_eH-gzXiQAwCe7u1XuXqUR3QA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzNauNcIFkZ9iAaw4QOC5IiacHNSrn87rTtE31GUj0qQ7RIFj81lBZ9Fk7h3oucnNjBDrP3XJ0xrTgufAAEIQxRvbPIOUYMTKOh-e9vW75veWD2Ng0pRCOUrLC-0c8tDyzhbh63W6GxDWoyzixg65mpRFJ-PObR73kJanSvngh2sLsZOr9RZropERcxXs7EgECsgYkJmFnZg91AitbSmYbhqyIS4nTA3D6FkMDGYdM662-8Kqi784-aQKbaeW5OXlqTjUV1fobpgwWRKcEVOPTayRs7zRbmQ-62rEIqgviPaH-R6SHHvC5UV4C5lUg-W6eTy1i3-wTi6TlxjFLdB7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=n2kor8Rbu27ZbGClz4OD1SgDlmjmiMsSDBWHnXTEOrTX_IKim4N66SAkdZLp3cIfD-gwip1W9yDGcxPcZdnM6G1J6YGKE4bWCTJTE3jAJ18EBZLib8HtKWXRSnOEvhaDz9G_SQwpAW4hHGwfgbrBp1_X_C-WzE4kXtQe6zYrAIlnu9jzEqkWSnJLqkXL_uyaZVILgz-Oz4GDt18N4y2ez0Zh3zq-PBjgoS0qG3xAeuiEdB99-ICAFf2BpEPPVCvwVC4yPyAgU0WvAyW5GmpzSsdWbnizk1frGfvkOBQgKJcMPxcw7c85Vhnnk_8jc51SOmpLRPBDEyVZRKUBh6ngJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=n2kor8Rbu27ZbGClz4OD1SgDlmjmiMsSDBWHnXTEOrTX_IKim4N66SAkdZLp3cIfD-gwip1W9yDGcxPcZdnM6G1J6YGKE4bWCTJTE3jAJ18EBZLib8HtKWXRSnOEvhaDz9G_SQwpAW4hHGwfgbrBp1_X_C-WzE4kXtQe6zYrAIlnu9jzEqkWSnJLqkXL_uyaZVILgz-Oz4GDt18N4y2ez0Zh3zq-PBjgoS0qG3xAeuiEdB99-ICAFf2BpEPPVCvwVC4yPyAgU0WvAyW5GmpzSsdWbnizk1frGfvkOBQgKJcMPxcw7c85Vhnnk_8jc51SOmpLRPBDEyVZRKUBh6ngJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=dlP7wBoWUA6KCZCk2n9JBt_jLfOWSuoWhMGrSvZHV1iL-Ef2fnBGo5HonzFiFgHLhKGlP2HtFkFVBv73q9e-u6h1RB9gP2ph_frTM7YLwAOqjBR3ixvZ1nXwgbzn9pu_1C_Ht7NWGIeh3jkE0GIGw_pinya0vWNU-F5F9aLLh32m3Nrbu1LTfOsKftaegEPjFqFGAjHj_nmnZRVTiVI63aB_MGLCL9hz5SZDdTfhjTMVaGyWezx60JFtSLf5xnb7ZnvDbNJE_OFcyJUnR2EdvP4dRsWIe7rezOldVVKeY1AYGXOp0CIKQA9-Sr9fAqwe9Xy4PrdLd2_c9oa3p7FMWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=dlP7wBoWUA6KCZCk2n9JBt_jLfOWSuoWhMGrSvZHV1iL-Ef2fnBGo5HonzFiFgHLhKGlP2HtFkFVBv73q9e-u6h1RB9gP2ph_frTM7YLwAOqjBR3ixvZ1nXwgbzn9pu_1C_Ht7NWGIeh3jkE0GIGw_pinya0vWNU-F5F9aLLh32m3Nrbu1LTfOsKftaegEPjFqFGAjHj_nmnZRVTiVI63aB_MGLCL9hz5SZDdTfhjTMVaGyWezx60JFtSLf5xnb7ZnvDbNJE_OFcyJUnR2EdvP4dRsWIe7rezOldVVKeY1AYGXOp0CIKQA9-Sr9fAqwe9Xy4PrdLd2_c9oa3p7FMWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=mrVLpVUsNwvUUzrNlZ1xz11eJ2j4pZ3XeiF4zdHPQlBEnRMcduVIvE1LeYSd0RpJh3Y5JoyGUh1mCODU2QFbooWmQVQHu-J8Dd07qW7mvW6QRLyYD50zjZGBBsYOqR08XSzAbULlC2m0z2EmXFDXdlv3GIM6fKiXcvmU7dA-Dhh_VYxqApcSDoAp0uNEybjS7fEhyJ5OwMLn29d3DolyOMSRzm0sdmpd4UZQhetIlZWR3eYDJVzDNuZQPZKhk2VuOzvlYS6j7H3iF8KCGXek_rIAtfI5TOLu241q7tHN_eYkPfjIaT_5rPscu3e4a10TPYjMdIKFyVVFapdwgrANDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=mrVLpVUsNwvUUzrNlZ1xz11eJ2j4pZ3XeiF4zdHPQlBEnRMcduVIvE1LeYSd0RpJh3Y5JoyGUh1mCODU2QFbooWmQVQHu-J8Dd07qW7mvW6QRLyYD50zjZGBBsYOqR08XSzAbULlC2m0z2EmXFDXdlv3GIM6fKiXcvmU7dA-Dhh_VYxqApcSDoAp0uNEybjS7fEhyJ5OwMLn29d3DolyOMSRzm0sdmpd4UZQhetIlZWR3eYDJVzDNuZQPZKhk2VuOzvlYS6j7H3iF8KCGXek_rIAtfI5TOLu241q7tHN_eYkPfjIaT_5rPscu3e4a10TPYjMdIKFyVVFapdwgrANDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=cEkdTCUaMl4pmCqG5arzDX61HYl2ccSoquL48tx_20F_xONVF2-Uu2T7YnT3tFUuQwFiun8NjQVznENijH8khh2R_wToWccpI8sMCmFFAJTP5257HuHjdjt9m4_meFudsHj1g9mZuRgo8-C-fh8X7J_qdi3gl0TRzqjXtYzsjXRQDkTMJN4kSe-hXm08dSpiWHrgrYoRxZzHPHEK2T9UJzyzpHq8BDj6LWJRJijWP-wG3hSRYAHDG8clDcF4pvc-obe1-YnkFiGyeNZ738WNvUqTaIGns5EDP8NX59xb4O1tt97Q66wiEqRF1SU-76r6yO18gACdLK2ZSPGgNKnAaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=cEkdTCUaMl4pmCqG5arzDX61HYl2ccSoquL48tx_20F_xONVF2-Uu2T7YnT3tFUuQwFiun8NjQVznENijH8khh2R_wToWccpI8sMCmFFAJTP5257HuHjdjt9m4_meFudsHj1g9mZuRgo8-C-fh8X7J_qdi3gl0TRzqjXtYzsjXRQDkTMJN4kSe-hXm08dSpiWHrgrYoRxZzHPHEK2T9UJzyzpHq8BDj6LWJRJijWP-wG3hSRYAHDG8clDcF4pvc-obe1-YnkFiGyeNZ738WNvUqTaIGns5EDP8NX59xb4O1tt97Q66wiEqRF1SU-76r6yO18gACdLK2ZSPGgNKnAaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=LjnEtAZ5b2L7NmReU1oiWVwMWzCEESiebA-SDL3CvD2jDxulbHnVphYdCft2UAtOYwg7PnHrLx8l6sfubuArRhtEl8c-k91Yzf0HAmWc7SrCLtdVDsGNfCnkF39FaqXqi9OMNrX-1UUE7o6ZYSMg4v4IxlYSCAgjgSGHX1hpvFdFkuN-vuTKm96wSKPHUsuUrqCvC6F9aNlHW-pDfbEw6b5YmGQ91oZ7wsJJzsbl7hTrphd-7fDDxsmo8ZG8pTZF5Sgr71BZ3ynugJFfK7ESOwDikuIXLg5V3NTqL-CIFSWXd654I3dAJ_SPIYIM06Rb-ODngKj0Zf76M5tqrrrLRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=LjnEtAZ5b2L7NmReU1oiWVwMWzCEESiebA-SDL3CvD2jDxulbHnVphYdCft2UAtOYwg7PnHrLx8l6sfubuArRhtEl8c-k91Yzf0HAmWc7SrCLtdVDsGNfCnkF39FaqXqi9OMNrX-1UUE7o6ZYSMg4v4IxlYSCAgjgSGHX1hpvFdFkuN-vuTKm96wSKPHUsuUrqCvC6F9aNlHW-pDfbEw6b5YmGQ91oZ7wsJJzsbl7hTrphd-7fDDxsmo8ZG8pTZF5Sgr71BZ3ynugJFfK7ESOwDikuIXLg5V3NTqL-CIFSWXd654I3dAJ_SPIYIM06Rb-ODngKj0Zf76M5tqrrrLRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=T-sO903VZi6Nwai_1QglnyZ7DybC-f4f-ra_AA5l1GdRoViCtAJ-XPsZgqdEsAxbn44fxwz-C_mSbUmrAY5b6VrUyt7XS_w-eusKRx-mzAhL_q63dJuBlzDPRh05noHq4LlpdU13OZ3fDhxufxGLerOWmWcZL8li-YjMZMfx8p9yt3QOMjzuyyVjdfnVNGTrOU1kG9sOqmUkwBWAQQFdjUfRVTQQncgO-xJY06zRlaF7URn3kra-q9KznK5ohdw_CxFn1hfDtraAblQspxm9RmeIQNIV3MLJzoJd6daSeA6F4BpIHrN08t0Zf33ix6xoTRGChe4k_gBz-76pvbXxRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=T-sO903VZi6Nwai_1QglnyZ7DybC-f4f-ra_AA5l1GdRoViCtAJ-XPsZgqdEsAxbn44fxwz-C_mSbUmrAY5b6VrUyt7XS_w-eusKRx-mzAhL_q63dJuBlzDPRh05noHq4LlpdU13OZ3fDhxufxGLerOWmWcZL8li-YjMZMfx8p9yt3QOMjzuyyVjdfnVNGTrOU1kG9sOqmUkwBWAQQFdjUfRVTQQncgO-xJY06zRlaF7URn3kra-q9KznK5ohdw_CxFn1hfDtraAblQspxm9RmeIQNIV3MLJzoJd6daSeA6F4BpIHrN08t0Zf33ix6xoTRGChe4k_gBz-76pvbXxRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4xDUbxKvhzJ2JIWYl9dy3NIN13TEXOqHBHQTOsCpjGRNhuxn5gAtBdV37ekugpOrJSRO2wIuOtCck8-rWMRuR19Hhm1NW2FoNcvU3xo66XgtEgVHZlye-cJQ4zJcskISYxgGD_aCz5qalKjj9ugK97LibKSnXPE5MFlYCys5Tx6ScB1LzjqWL2227dBJ670NV6qFF-Tvubzi3GfEhErJWVrOox6GjlnVAsflRrQVSxezRWHLiY7qi9srDnaYi0Sv47AgjEjfwjc6kP1MqnZu3izK7dHFfe_vom_IljinhcPWCUv3sQ0nVJP0zqemN-410ikzUi6MxeXaLY5KhttCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
