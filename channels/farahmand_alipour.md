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
<p>@farahmand_alipour • 👥 63K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 00:11:03</div>
<hr>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=rJF7EeTRC4n8QscbBSwyywBYgLGNt_bxCZ0ukHDzFEOaFdoWqCR3janNRcHjRNXdMn0tW6WPCzJ0aRdJyp5JNdS6r7UmFfyWL8Q2Vllol5CaQzACk3YVplRsOtgd4WmgQgjBikTIEf2L_6CtcW1K5DojKXIWfBXuUPt9hT3kR8YW5jF8ymuY95iVZ_fmJVj-36bt1q3_NSVcxbTDuSSsWKMyyJNhB7bJFPzL6bSEB4DwDfQ5dfmzo5U6pUVPfAW_tYeta4dbewV5HPCtJkXi1slJ4GVjWneuhz8Dufq9715gD8tLdOSsy2gOxIUqT3O-HzNdeKucU7zgKpYknGNO-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=rJF7EeTRC4n8QscbBSwyywBYgLGNt_bxCZ0ukHDzFEOaFdoWqCR3janNRcHjRNXdMn0tW6WPCzJ0aRdJyp5JNdS6r7UmFfyWL8Q2Vllol5CaQzACk3YVplRsOtgd4WmgQgjBikTIEf2L_6CtcW1K5DojKXIWfBXuUPt9hT3kR8YW5jF8ymuY95iVZ_fmJVj-36bt1q3_NSVcxbTDuSSsWKMyyJNhB7bJFPzL6bSEB4DwDfQ5dfmzo5U6pUVPfAW_tYeta4dbewV5HPCtJkXi1slJ4GVjWneuhz8Dufq9715gD8tLdOSsy2gOxIUqT3O-HzNdeKucU7zgKpYknGNO-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxKSWjSmIZRGZCkiIdztiiXPmw7MI6TsWnzLxX_AJEyaXn6s1X9kzMjbMn30_ayUlpX43jgOi2hKsaylIDAERPdR9wiSz5wIZY5ruhOBz29lqEnvQ8OJA3QE3xoOOn07hJ7aPaXAstfulhyboeoyMGoOar8LOWvMcfcxoR66Axqafd-J0EBZkLg8Tgqglw7jCnAyFzoOgDi0j_ZqkFDps8E3JXU0zNqWCiK4fh1l6htJhQKhgNfpm6bWuusQnRQwpD1aIG4rIAakmimFuyal57AGRH7BjzW98Pm2p6etv_0cHru_OKew9GdlilnK61ISD1nMQic1SZi4rPobpk4Usw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3Zqqio4D2q-qLws74KDCaiR09ijMCVB2Vp2Uc7zcICaOuSNA5BcjexN4v9UZiHU_dx8wzwOWvsYSuiQE6ktFNXMYdFMz2OyntzK7F0kX-OJpEs-H_qn-k3MKowsCgbbBrLFsy9OJsBpQtDlzf0wdgdTxuNtN1wophjMMMRAPf0lcWu9mGP_Ki1bv_vc_5ZUIWb3HUFaSX56m0msqIcvQ1Xg7Olu-vQSWdowYqiFgw_ejwD4Gl9F3POgo_N7ZZCDw21J2_4vck3seC8s3B5-uZVX8m-BeSRavHECVhE5e6SbkkQsdo_Bx5hZJ4gsN8Iqg-9v0P2sH1GDsuMxxa2E5oOOpg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3Zqqio4D2q-qLws74KDCaiR09ijMCVB2Vp2Uc7zcICaOuSNA5BcjexN4v9UZiHU_dx8wzwOWvsYSuiQE6ktFNXMYdFMz2OyntzK7F0kX-OJpEs-H_qn-k3MKowsCgbbBrLFsy9OJsBpQtDlzf0wdgdTxuNtN1wophjMMMRAPf0lcWu9mGP_Ki1bv_vc_5ZUIWb3HUFaSX56m0msqIcvQ1Xg7Olu-vQSWdowYqiFgw_ejwD4Gl9F3POgo_N7ZZCDw21J2_4vck3seC8s3B5-uZVX8m-BeSRavHECVhE5e6SbkkQsdo_Bx5hZJ4gsN8Iqg-9v0P2sH1GDsuMxxa2E5oOOpg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzzSsDYa8IXl7mXx7DOeEqP46ZcQdnBRUD64sU3JIY19s2RCYYLb_q3aDDtFOYzPCzNOncjWjzLGLfgb_Dqhqr989KFz42vbUMnRgQIeFX5NvkQp1L1eiQ3il-Gc4CiKOAprVvy_9OCHOLDWmGanGu4QRl_WYl9UdsRFepC6MSfeNnL-VtmrhDZE2IeX07dtUkvSA35ZHCwt-RbjEXs9oYxHaln930TAMkLQYmUJUc9SPfZOWe4We_oIGHg1EXT_yR4pn8exr_ZrpoukBvVRjI8rZ7rRQaIXvfuboDHX9MzWM0EygwAUgFF285h70DH_k1-CO2_lB9z3HkZpqh0XYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=Ki1alEeNcLwnOfBYCsOQxnFOSW-36GAObsluWfWob-aO9J9OQRJDHnsXNLD52g3OD4dXPUMdRFyapNPrHhpXswFdPruwvn3cR2Cl3-RX9zq5lUnXw6PXBkd2WjmWR0Rk77WGJN96trcxD4VhK7RnMLD3mJ9EnQFaSVr9XGR61Mx6XxLRnA43ZzWRrRR4N5K_2AU1ffSFMIqyDyXSiw7CK199XL6_Vi6PDSzr_ZCyjhm_LK_kbQTzgnborVhB6NEk6wabwt31vaBur3cqZ_gRGvgYZUxVH67J5VON-ZfCjhlf4ZLiB-HMH2tdubae9yJ-AwxXK_gTvplDSuYdc4HvhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=Ki1alEeNcLwnOfBYCsOQxnFOSW-36GAObsluWfWob-aO9J9OQRJDHnsXNLD52g3OD4dXPUMdRFyapNPrHhpXswFdPruwvn3cR2Cl3-RX9zq5lUnXw6PXBkd2WjmWR0Rk77WGJN96trcxD4VhK7RnMLD3mJ9EnQFaSVr9XGR61Mx6XxLRnA43ZzWRrRR4N5K_2AU1ffSFMIqyDyXSiw7CK199XL6_Vi6PDSzr_ZCyjhm_LK_kbQTzgnborVhB6NEk6wabwt31vaBur3cqZ_gRGvgYZUxVH67J5VON-ZfCjhlf4ZLiB-HMH2tdubae9yJ-AwxXK_gTvplDSuYdc4HvhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=PsPYqlvxWn3WNiH_ZG1O3erxgZxRHjSt91ypfNNq9AAYIU0OmOOIPcnWt3kbrQp4Z89aq5gXw1_nZVqhTW8TsTsjBRGn8ttzK2oXcB-BHksY4Af0JfW2LJAXH5SzH-qc1ceylOL60l4biafWTHu6SQmMIYjtbtUzOhthKcehJzXylkhcd7sIPPSPVTheYG61zqdZLe9tloc4gdW2bT6Pb4uOTj0_9QC912mMaq6kg0vItDXhu9Y-pmM7hChpm4PSoTI3zNqRX3VSryiYRxGcOC1aBVOH9kicLCDJnhHiGxmBlE3htlHIQENljTKNOyXSi_JMR_MkyUNMksqEiUoR4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=PsPYqlvxWn3WNiH_ZG1O3erxgZxRHjSt91ypfNNq9AAYIU0OmOOIPcnWt3kbrQp4Z89aq5gXw1_nZVqhTW8TsTsjBRGn8ttzK2oXcB-BHksY4Af0JfW2LJAXH5SzH-qc1ceylOL60l4biafWTHu6SQmMIYjtbtUzOhthKcehJzXylkhcd7sIPPSPVTheYG61zqdZLe9tloc4gdW2bT6Pb4uOTj0_9QC912mMaq6kg0vItDXhu9Y-pmM7hChpm4PSoTI3zNqRX3VSryiYRxGcOC1aBVOH9kicLCDJnhHiGxmBlE3htlHIQENljTKNOyXSi_JMR_MkyUNMksqEiUoR4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdUfZQkUbZn4PdoxFTVxLLC1_uh0pk_Svk5640gLN8azH07lx77hJEtleV78CRvp6Z_JKpk1-_8KmjB9UTsUSLYeoWcpCE5957aqSyJMQ_5BIqDmp-TH0m7ZDyf-FrXDdMCUqeIy2m3c-VmwCzD_GNxilrk1N9IF9d71qsK81cGd-WyPe0LehJS9HHy2h9vLs9Fjl8n88UE1EwFXrG3ONQkjmhXvPpZ9zoYiM7cynGUk5udht09N7zSMOMtnXavVqK5S6Dh_15r7eA7W9ZrkkdZ7eSfmgYwRD-IWBI4zZdX7GyzYebxleNPkr72Cx3_TmJCjbEjuip8uzyiy2xlHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=UM-4jBsmM2fSPhhatd6bMlVbQu4DH39d-uUUvsrbWXmPL1j8yncc3jOQDYeGue1N87B2hEiHhyL4oM3rWKpx-CgWwAlxzKywwK5Z_1be9mC3wCeU7nbbIN5vKVoc9DZkXrAtmCFWxMAjHe8AJQ_Fu6CyzcOEJgLpd0o_dwVYAhs_Z_Q7GT7fU3QAuReRn2V3pxRf1R8BLAvF183QLkyWPd1LrL-2qNHcAQpoH6o7HO2Wb9xp_qhkcb-h9TlM9bjj-Fvy7_Oh9VM2cTRZdJf51Y2Z1RoNHLdo2KX09BT1U77iW8SmwwoRqP7EMDSCSeXpgi_5lSN8ceiT2mEQXrtsmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=UM-4jBsmM2fSPhhatd6bMlVbQu4DH39d-uUUvsrbWXmPL1j8yncc3jOQDYeGue1N87B2hEiHhyL4oM3rWKpx-CgWwAlxzKywwK5Z_1be9mC3wCeU7nbbIN5vKVoc9DZkXrAtmCFWxMAjHe8AJQ_Fu6CyzcOEJgLpd0o_dwVYAhs_Z_Q7GT7fU3QAuReRn2V3pxRf1R8BLAvF183QLkyWPd1LrL-2qNHcAQpoH6o7HO2Wb9xp_qhkcb-h9TlM9bjj-Fvy7_Oh9VM2cTRZdJf51Y2Z1RoNHLdo2KX09BT1U77iW8SmwwoRqP7EMDSCSeXpgi_5lSN8ceiT2mEQXrtsmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=UOC4u3SGDeIPTJ-MzM5_IDOjqkVIdeQ3Oc7A6uIAkmrPuvtwZ0_QJGbYJa7HGGBjDTCR7DJyWt8ZdMBBYQ6D7gsm81q7aVMSHRQfWE0GTUQunRqIBulQrSp8NsBTLYSSpiHZFNJ5zpFrZsgqwW2C3rRyg5TDVT1EDb85KQGuBbeyf-_8cXNfGvyruxEomCRSt778bVBGrT26G4la6CKTNU7sG2d-1t7x5IjdYen9rLArwh4LOwT52tnn9R5J6XnQdXtiHlM9nIpSThFXieN2MbFVV7mLZqoxTBWGakFrFvWn-tND_oGZceWsn3qEs7c-IQe_ND61wslWqTBP7gEk8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=UOC4u3SGDeIPTJ-MzM5_IDOjqkVIdeQ3Oc7A6uIAkmrPuvtwZ0_QJGbYJa7HGGBjDTCR7DJyWt8ZdMBBYQ6D7gsm81q7aVMSHRQfWE0GTUQunRqIBulQrSp8NsBTLYSSpiHZFNJ5zpFrZsgqwW2C3rRyg5TDVT1EDb85KQGuBbeyf-_8cXNfGvyruxEomCRSt778bVBGrT26G4la6CKTNU7sG2d-1t7x5IjdYen9rLArwh4LOwT52tnn9R5J6XnQdXtiHlM9nIpSThFXieN2MbFVV7mLZqoxTBWGakFrFvWn-tND_oGZceWsn3qEs7c-IQe_ND61wslWqTBP7gEk8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=sIUCHYlduPx_HM4WvFX7f39c4BBRRln8kcipfwvCUJbe8HiGZ7vFsOs4ndas1ld7T1kgxs8lDmStQgFNYhsHwIN2aIxtxs4HEHq17V-gIMSWP6_oDxpLMhaV_qPGX9gxEEJjWTLWRE1CZFCIhRbnOS6dhbpmRXuGZp2N6dfExWgg4L9pjwoCQYkPabQlknjKTUtuB0nfgi3woWZgV6EUgH_JuJJrf208to4CSzyB2gU0Lvyoy_1scQUuuDd3ANlm709eF6xrwtImlEIb6D5ngSM9fQW3dQJ8TRso1LzSdYIoXQ8oUiORlzJo1P0Wn1rbD_3aEjTViE1VUcInC5Qc3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=sIUCHYlduPx_HM4WvFX7f39c4BBRRln8kcipfwvCUJbe8HiGZ7vFsOs4ndas1ld7T1kgxs8lDmStQgFNYhsHwIN2aIxtxs4HEHq17V-gIMSWP6_oDxpLMhaV_qPGX9gxEEJjWTLWRE1CZFCIhRbnOS6dhbpmRXuGZp2N6dfExWgg4L9pjwoCQYkPabQlknjKTUtuB0nfgi3woWZgV6EUgH_JuJJrf208to4CSzyB2gU0Lvyoy_1scQUuuDd3ANlm709eF6xrwtImlEIb6D5ngSM9fQW3dQJ8TRso1LzSdYIoXQ8oUiORlzJo1P0Wn1rbD_3aEjTViE1VUcInC5Qc3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">هزاران نفر که اومده بودن توی خیابون‌ها رو کشتن!
صدها نفر رو اعدام کردن، هزاران نفر رو زندانی کردن. اومدن با وقاحت میگن ما اومدیم توی خیابون! طعنه هم میزنن!
شماها با وعده امنیت کامل رفتید
با پذیرایی و امکانات. حتی خیابون رو تخریب کردن برای تجمع‌تون، کولر گذاشتن براتون!
خود گدا گشنه صفت‌تون رو با جوانان شجاع ایرانی که جون شون رو گذاشتن دستشون
یکی می‌کنید؟؟ طعنه هم میزنید!
شما هنوز نه این یکی رو خاک کردید!!
نه اون یکی رو می‌دونید زنده است یا مرده!!
هست یا نیست! توی چند سوراخ قایم شده!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Am6u4Rrgu8xe47049HkbEe2GoLeGK-hOZx1km_XKP_cO5A_miICtDx6qpu8fTBH8KRnTnQu8UfsRbhd25HZTKsKBFMIA-CblIRkYcYhypdXrIDISH-w1l5s9QY563aUY4DThQUI2O1Dchy6cAVnvWz7rHw5CLFc34suckFckq1NkwD7U1y_E143cZCr5H-b-7TJxQksbK78-PiXS2vykxRns5SzXys-oSm9lPZFjXd_nH6oLKvyvcR89r3SjU04-M4-nqwYVCwwt-JOgqMHlJ5EPQ74vwNSdr-fYCXW6ztPtm1FQoYt3Vz-7cAhbq9GQnC7ZrdMeSGdcF6SyIY-eSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : «آتش بس با جمهوری اسلامی پایان یافت. مقام‌های جمهوری اسلامی شرور، بیمار و فریبکار هستند.
آنها مشتی آشغال هستند.
به آنها یک هفته فرصت دادیم برای مراسم خاکسپاری، ولی در عوض دیروز به ۳ کشتی  حمله کردند.
آمریکا زیاد از حد وقت خود را با اینها تلف کرده است. اینها شبیه به یک غده سرطانی هستند. غده سرطانی را باید سریعا جراحی کرد و دور انداخت. »</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7ovzrxVJ-I8dU0bHTsxaUMHAD9037YNq27Or5C6n6uHtLKXZA4tOfZOFO6RVEJYiKlh26CFYqkUf386ktr3AkL8mFXwCAwk31gZJHYl1hIUchBwk_mp6pbLnFfsQGHLXQxkVyIxQNGoRNJQTAQaeMVAp4_XLd2_KjsYWAAV635Fy3Xwsvq85AsoKMib1VxzOJ7QxQSvO-krfSpZbi9Av6321v_a6qyuq9UpEjQ0JpKXWxHzjjsdu2FSc_2sei0gVqQp5iUm3d-hEmmA5RoB8r0Wu9uiNMog_8NrotCtEyqGT4yjx164VMZtPhp--x5P0CMSZi9FnISzm37ofUkLEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLTAkiyyGNWlhbVQ2nrqLIjN41U5ZvJZezsHRVicPJ5GjQacvQQa6zPRnyeEK24wU3Yv_V7a_w24YLDPnu5FBhCa4Dz3tiMiLt4cUVEXH15-N_Y6046KzKMGd0Aj9xZGRFwwQ6q2aH8nSolXrxWUf9m7l5waP8kG5t1DELeo--EFCgs2XaV-GXasMDv_ngG-71hjJujQw912CoTZKZvsaXemWZ1vpqoghzVriFQeJ3Tw05cTNPHjHmdZIZGj_8nwtmad7LMNk1N3oZN9z2Xa2QTyq2Aa3GJIgQDXVBHKIVVr6TZOP0c57QQ7S8z6pKi5enBgDUi5SM-_y0NC0BG4hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Rn_8WCUJbJutyPrrsbMZMeVklr871nCBWKrfT0m9f_uqL8UzQqnbVchV9RocoskvFLnM1rzw4iiNr0iISQPQR9vyPozccctXPIFjwtTBjK63QOoM0xPtuCCyWD7wMVHUZJen9tEGNBIqI5P4WKregQ06eb_O08JDarZZvevzknG8qaIZacMCgnxUytnh63z2c1e43687SiVbEblFIgNPsECUmc0QIPVUjmzLrPyV3VklTcdOIoyzEdiyPpzP_H-WCr_ob5AgrmEJxeZLp4Nxu6hP3pQWEyUH1XnuOMe_pJ6KaMwmc7a7UF-0SKvjokXa1aR1-T6SzIg0VfeBmUEEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Rn_8WCUJbJutyPrrsbMZMeVklr871nCBWKrfT0m9f_uqL8UzQqnbVchV9RocoskvFLnM1rzw4iiNr0iISQPQR9vyPozccctXPIFjwtTBjK63QOoM0xPtuCCyWD7wMVHUZJen9tEGNBIqI5P4WKregQ06eb_O08JDarZZvevzknG8qaIZacMCgnxUytnh63z2c1e43687SiVbEblFIgNPsECUmc0QIPVUjmzLrPyV3VklTcdOIoyzEdiyPpzP_H-WCr_ob5AgrmEJxeZLp4Nxu6hP3pQWEyUH1XnuOMe_pJ6KaMwmc7a7UF-0SKvjokXa1aR1-T6SzIg0VfeBmUEEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZc_Vwhxfkh47zUVQhoGuIfSV38s0LjAnnkjB4zJqeEnRphn1r0OWGdkYplpgpObbgZ-IafyVuC90iMrDb_Jl810J9ku1FSRBxwWcDMmr7eB2eWp-nyKSUtLywniQmMKtYiVN7Zh7B5tCeEyqDFI00F52R4MY3Sro3IgipTEaZ9JvQOhLcAx6XhF0ilOnvgoQZfqY6dhDtr8PN1Zgteh-mi9SV6fM0UlWtUZg8qDv7oRdWLNsQ_9W3heaUiJSV5Dl3dR0j65Uy3RN9Dk6wcqYKh9zXovpGwjKH0ZPKmHIZQZaf4I6dejBLxKRs-bAc5i-pHjTwNpLj8gn0GXj41EWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=Hlq_2rB51YY97hX9EPrjWSPGhShdz7n0QFoaOQeuaQbdFACBgrGym2bLn1l2xSeS2VqnFFDYimahJHtQcug7UBN0FJz8v0CjaHl2avEUeb2hXbOvW1OsJKVqRyqN5w4DROQRznRsGfv7v1gnzjtPf_-UqcKQX_dHElADTNSfc4cpeDJ0JQOpXHIG6kEdPZ5C3bwJW8qAezFsAkjCFd6uG37jpNolvb55YLfYjtIlVohPSe3ZYaBhu0X3KC8T5FM9iVWo3OClCl3W-9WtmcNVEzumugxEHvue6Lb9G-g3kclf_TIAhljs4oTS-osmDJ_yfrHU4KlmGv0YkbbOQFLq-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=Hlq_2rB51YY97hX9EPrjWSPGhShdz7n0QFoaOQeuaQbdFACBgrGym2bLn1l2xSeS2VqnFFDYimahJHtQcug7UBN0FJz8v0CjaHl2avEUeb2hXbOvW1OsJKVqRyqN5w4DROQRznRsGfv7v1gnzjtPf_-UqcKQX_dHElADTNSfc4cpeDJ0JQOpXHIG6kEdPZ5C3bwJW8qAezFsAkjCFd6uG37jpNolvb55YLfYjtIlVohPSe3ZYaBhu0X3KC8T5FM9iVWo3OClCl3W-9WtmcNVEzumugxEHvue6Lb9G-g3kclf_TIAhljs4oTS-osmDJ_yfrHU4KlmGv0YkbbOQFLq-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYlWE-T9ee_SQawtgsguqRyjRdTF0b7U5rT308SZm0BKvJTK5UNj7I3NuHu0CMwNGLwGFMV4zTqL1FOdIpIdm7jb4e-QLI40f8Z1DI_yQik6nUJON73BL7z27VlOTXZ2ukQVXueGg6lNWuGpcXE4XaszGOMB_q4BvXDesaYoHcvnc1sAK-gyRQWCqHoNeKh7LJwnE6IFZ6kvwSgqHZ340EEu28GCiHoKCaPPditL-I-RsUDAfICOyHtzshaw0ifWr8xvydG2EmzI78S3oVoStwgdrgKzPTQQbaJf1VDBFuaK9Gbe83t3nbijiZPTfRQZXdcfPZ9pSZuTkH226ZTkGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EigSPC6Wgcv0NoTO5CF8EkrZEf3WryXdUvVdcqNuCxuDxu2Ckqpt2oY9FQhplluZfqdCvSVyDlhRckbEdzOXBMFPbyxYbYEkLTzc3a_QCAlfQPV99nXGN226Qd2_gR9ohex_YG6iG0rFx4Ybm3JLf8ORXmbbiT8jjNJlQGGnsy0xkgcbw6sjJGjwWHFA0VugfIuPxCjYlFhk2CTUrjLNtpp4N2yvDgnWx9bNvZ0KXyq6dgWAUDdaXufcScTiu7ij6g3eQRXFWyO1OU7YbbQOtmk6yR5PmMUvliaqyHMR41ReeWbJgAPhm9iXWVX66ypxweQMc7XpycSGBvlo_Apmtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=eP8kUx-E0pBJgGQcAQUUO-GQa9KImHMn1ArHrIidT54Fhc6_zWrxfWtZDopf-39IrHIOSLFK8OlXgGt115vWRriJnyBpvZLYQ58dNc8bNPQhNEkgLYmCWi5YQfqLBIs9QdqzrRtGQEy-0VPIrE-scv0Ut48SDsZ-VUX7GaqI2f1doAuSuGa5OAhyEVuDumCVz1N-woN_Q4rLr61XpncOtqm65TDkCubwVcOCQ9dLXWEqwcFNix0PkXy6k_j4zrrLELI3jJrAkwu_henWO2DMCOcnlmvH-5nlzT1q1N5-n-sm0b3Z3llKzkhSSHPUE5w4csWKAxIV5u9xZ7xadDYhwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=eP8kUx-E0pBJgGQcAQUUO-GQa9KImHMn1ArHrIidT54Fhc6_zWrxfWtZDopf-39IrHIOSLFK8OlXgGt115vWRriJnyBpvZLYQ58dNc8bNPQhNEkgLYmCWi5YQfqLBIs9QdqzrRtGQEy-0VPIrE-scv0Ut48SDsZ-VUX7GaqI2f1doAuSuGa5OAhyEVuDumCVz1N-woN_Q4rLr61XpncOtqm65TDkCubwVcOCQ9dLXWEqwcFNix0PkXy6k_j4zrrLELI3jJrAkwu_henWO2DMCOcnlmvH-5nlzT1q1N5-n-sm0b3Z3llKzkhSSHPUE5w4csWKAxIV5u9xZ7xadDYhwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zc95jTNElqZhTHlZQHU5Og8f_Y_kDHDgpBiblOmGFxCpFU6n7jv7Uz0YAL_X8barq7VFsclQHTBeAT8sk_5NTMgzp2vCi12l6ZegV0DbYj8lA-I7jvNAvf6mLW_YW0zIdmLReoN2dYFA_L0R_k8lN5tz3puxd6Orgquoa9CzzcNbcPP31aGOaiRqIDJ6_lj1rgmMdNFUS_zWSc0tEFTQLRYvuEhdCFI61_Ggr-7TdRn03OL_WJg0iZdV5DAQx6GDvZuRBafwAgzOrm67NtKSJoRkfk8kUxcfZf5apkGnnW2HVMQAUsrNFEB9Srfx8_IV9lXvIZa6_dZwAX1vHxXP7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_rz8SAQBCeOSqbBudxTznkNGmicDSj3KVs-cvcxVy_eVslgZBZgvv41kyfGhS3LfdwjwtdEX14tPDY9eAaUDycBYqlfLMqFhtCVMLlrvEFWafqvmdmOhi1-OyaLv0q3hBoNMVtL6gxI8PMvObal8dcNMa3YptQ21OgwS3FNb81J1uTXJ-20quGi8En1JywXDnD2PWNClOGn44mZNQSqfttTdF8QOdXTB3Kh83i_wr-ouBhIKIuHNMHCMknT1ga8ytVo1-A8sfxoaOFQGlpXz6L3fwe42nJJYIi9w8AE4vAk__vRoXO7PuGmDsK0gb9kB1VbrYAZGJn44TzmGHwuLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmdAFvF7tspfH_iAySn_6TNWcstJ8KA63rr9Mr5LS3E1s23q5Mv3gYbdvUyouOxNDNvKycVFXk7mHk5rSBbYsKPlfKRZp6NRi6seD8Yx4pYlw0LH2nNtxVpijXVoPmdAmO8TcqT2yizKKvv0iKf15EUgFP5l4EunGrmyKii-oTfFp7CeKPo4wnrmczjgtrmEsy1xtRinrj8XAU_KEZkl8oONzWTO6m21TyKKwiFxCa0dFp1np49g4o_F81YXL09903cx55cSYmEYPLL0XhX6thyFBfK3K1-6ULOo8hbdU-ymxgbLyQZ12iGPzETrQmyybUEOKG0aoLmU5-tv-Tptmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fPztkKsozJ3ofMR3Y50-1ugpTcOUw9bYtrewppArDJg_Gsf1_bBxlSNbsB8je196GBrXN9sp-QNaXjsOoPKZodymlHWTkJtfPPXiJlM85IbiTnifmMSdLv4daXUSlvyDXlqOee0lIVuOJUoMfaLKf8vVPX6x4GaH3uuX-0p3lUx2iXRVnmhtZIprQ9zNkTK6ycXZDwwRNjl7Fiywosqz4lMj7Qxy2EtDA9SeX6XL1oL0Yr5rEUFO5W5Yl9dtfQlOZpJ3jY-c11NE85gWBtV-6HKsQxMrK49K-Jh0CTTy6l8CQdlSlTU-gCTqmRMw3D7NdxtXWWKtGA0nksMq6ncJ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B92eEg0YdTHPtpONOdMJl3k8nJV9hUij1COf_USlbdLIu7MDFSkR4MdQ6XIX9j0miKNDXnjZAkqvsQxicR_g5Mz_bm1MtlziYc8wIod77yTGIdtSw1fA9vvPR7XQZA0sPM_bosd_qOZIOnNZx7Lv1Wy7W7D2UEYVYTaEZvvxTkdGuSGxrSh6CaDuuXKlGFmT-ZOgLWCX1Yn7jDm5baj_dWrjhq8iz_q2ksVIWN5_7scHV9_K2MfuRpFJYknMCMTUXyofQQa4KzeqEiFxrteVxk9xI1WS0tb-aX_oahn3XrP03hYSY7wTRt3ourpFeAcGXEKEC_a-ADPlMuS4FGgrow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QF2d7iwWz4NtP_BpOjWMgZR0xdFhS4LWGdO4OwKwFTqNhz7620TnYjQDMZjSAcnNI3FG3iHorVPPTTQOc-v2byySu6O7_s2a6zVLacB3iouDSR_kwlEObRT_r2qqTZIyHI6CoCisR0R_kZ7C08fyjjKxcBQPDsr6iRGex1HqmcdFYeb6qsYKuuxRIqNvoc-CtA_nGPBS253AlOJ6ABlVOO5ZUHtwKmzXy3ae6SDpw4W9p-K2_xO5i5VN94GKBYLGHUmaSOHyVPjP1n2Cn2TX6qcxq7lYTIUzBZLk7IUe2Y55wyoP8kID4TZ_PoDBVeBsL6G35f3wo74iJLtKcJBssQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=i-0h5FN-HhRshSA0gnEmu0YhF-Xav3dIlJm9Lzx1KQu7i9AlJtPArJjzUrT50s3gqXfs9zR7c6gw8Yd1xg-vLMrjo604PbzRUOpoI_j6UpTkqJar7PwxtkJr9AQYkslkd6a8eSdDt990qh-fU8krRnuh3YKMrDglIioCgd-DsdRfN2Nu1u7Pl7gpr7VGdhTU_ADhhptq7h1cfuulwANmqguF4Lh36hj3qIM9JbiaYkmkznBEsrBnJmDdoiP2Cm_KfMKQ5YCa16jHdWx0esWxI_LQaJjUlIoRBt8glZ85Aal5igZyrQ-uyEFVOvDYicUvw9hNVddNSt3PCv9ggrC_MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=i-0h5FN-HhRshSA0gnEmu0YhF-Xav3dIlJm9Lzx1KQu7i9AlJtPArJjzUrT50s3gqXfs9zR7c6gw8Yd1xg-vLMrjo604PbzRUOpoI_j6UpTkqJar7PwxtkJr9AQYkslkd6a8eSdDt990qh-fU8krRnuh3YKMrDglIioCgd-DsdRfN2Nu1u7Pl7gpr7VGdhTU_ADhhptq7h1cfuulwANmqguF4Lh36hj3qIM9JbiaYkmkznBEsrBnJmDdoiP2Cm_KfMKQ5YCa16jHdWx0esWxI_LQaJjUlIoRBt8glZ85Aal5igZyrQ-uyEFVOvDYicUvw9hNVddNSt3PCv9ggrC_MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1xZ3i6Z1beJBp0oAlTzBQWu_x_P1iNqZqAvICegA5JOfIB6OoHTPwYs7aJ74qry6yg15AGqBz72xlHGdTuZ4Esq3d1edvEkCepRom42ma--K-r72z_fjHWT1RFt34ydjLItP35rGkgA5yQPh1b1aA73SnAwhfUcArZxlyJnli60-6bIpJQ686FV1lXSzFHhrgb52ooL5dIOkRlufIXavjLZ2M_AxXtvUbn8ViDVozZIaZ2zNlSq03qg1zcOjUBIB5Q0gN-bB9F-1KXvvDIjYQ-3l93eAdaIpLDnE87XkF6Er4Dd1ZLsbkF9HsSU3fh-ZK_QKc0KeonYLihHEatbRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=s-bbHLsQuLhGgniGfx9VD5lHrC50-lZXXsuk995Fr_iv1XN-7ujY8nNYvx6QFBi_vhOEGFCez6_cepRsVbQeAQ_EeWYKutSGuPX6DRQHzXFuQUAU7kqGuXhkhdhugPtG0K8jo4RLi5g0IoIWUYgBcZPG7XVAxbNK1MxmZjkysQVmNBaI69KqvonGQdLeZ_Ro0-Gyl-gE34sSb8j6nqMqaV6TsxqmpBZ9Yfrd0_2-8ZavgoGk7TmkZEfcVZaym2YQgIHTXW--3vc83u4Kl1-HkVykeM1CerVlOC5a-TqVDK-A50gHVvgDAKPXEagKqVbEzQd41mcZ9L4L5FIUpvwwOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=s-bbHLsQuLhGgniGfx9VD5lHrC50-lZXXsuk995Fr_iv1XN-7ujY8nNYvx6QFBi_vhOEGFCez6_cepRsVbQeAQ_EeWYKutSGuPX6DRQHzXFuQUAU7kqGuXhkhdhugPtG0K8jo4RLi5g0IoIWUYgBcZPG7XVAxbNK1MxmZjkysQVmNBaI69KqvonGQdLeZ_Ro0-Gyl-gE34sSb8j6nqMqaV6TsxqmpBZ9Yfrd0_2-8ZavgoGk7TmkZEfcVZaym2YQgIHTXW--3vc83u4Kl1-HkVykeM1CerVlOC5a-TqVDK-A50gHVvgDAKPXEagKqVbEzQd41mcZ9L4L5FIUpvwwOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=paURd7bU0AfY1TK3SOxHZ2AhLZE74lMt4Nc5mm91YefqcrvOrh7Z2EA5oxhxBCidXDpfjFCAbVbSiTCTiLfCODVd5gaeQ0DT7e-B0Rkf8Nd0Jx14PEx1z6zlHqBbDWuJTYyByqBBt58iQBghu_KOFsuzyM42uiQLthZy9iLO0ek1rB-qww9h32s14yfC9A6qb24HcGae7XXY40kc5aSGl7HvHm84Hyc_TR-8-NMo4cdB5l9z9v_j58pcrtM4Q_5HTVQe3dn4LT8KeV_QfLTr2AL3yKxza1_DvvrikpHDG3mGbd2rQklPKl1tJEQQb-yzSydXIRQqKmjTdoK2BCAcrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=paURd7bU0AfY1TK3SOxHZ2AhLZE74lMt4Nc5mm91YefqcrvOrh7Z2EA5oxhxBCidXDpfjFCAbVbSiTCTiLfCODVd5gaeQ0DT7e-B0Rkf8Nd0Jx14PEx1z6zlHqBbDWuJTYyByqBBt58iQBghu_KOFsuzyM42uiQLthZy9iLO0ek1rB-qww9h32s14yfC9A6qb24HcGae7XXY40kc5aSGl7HvHm84Hyc_TR-8-NMo4cdB5l9z9v_j58pcrtM4Q_5HTVQe3dn4LT8KeV_QfLTr2AL3yKxza1_DvvrikpHDG3mGbd2rQklPKl1tJEQQb-yzSydXIRQqKmjTdoK2BCAcrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVhMovaqy4k6X-kg-tWevAEoMYzKgbRr07mFz11bEwqABeFM2SsoYjauftJ6rsRPOM0c3tav1sxrU5XZH3lS69jfKJ29H-LY9hmBdXGTaqN-n0Uhb4IiOMzb5aALslqvh6afoIOqc5lSmMpH0WJajOySc-79GjGjqF9VKb5TdAcsiUx1-xW1ksXnNYEebGBHf5JeTZjQaBHl-gMzLomS9KiwpG_TGPFJrK8dgZB_8bb-thnlgjjUk1opspol7MeIanFd8a2KB7u8XkAXcLTfHQGGOYhmpsXF5v2cU4C0i9jUXuyoGcs0HgOg3PKwbQhB9nBJXfdw4WJ7XCO03mnGXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=nsVVYZ63mJvZJvxOLKy3dkJbpDQ44OTmE6NsSsC5Xk-yxDO3d4maJzbb8g8qE5zDqxaKUwAGho6jBwQlsvyPZjE5OIYlDO3MNoCXrlqGaAK1OG23LqPL_slEqU7IOYXgMUEo_35yi7emogkEuDmHj-FARsNA7_mpzi3RN0hSkFc7SSbYFgkINrqV_tA3Y4jqs2DASbsshTgj4f0VHNdvQl3ig9RsHbaFjiYNtJ1nJsSlXK7DLHU7GsLOyWG42sTKlwrJDid26cZJ4B418KtGXBw1khDz4MPlNaOFaTWZS1QzdEUQzo4s3zeuZ4d0Ih8E3YE9DIl7GxPJDi2ENUlNbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=nsVVYZ63mJvZJvxOLKy3dkJbpDQ44OTmE6NsSsC5Xk-yxDO3d4maJzbb8g8qE5zDqxaKUwAGho6jBwQlsvyPZjE5OIYlDO3MNoCXrlqGaAK1OG23LqPL_slEqU7IOYXgMUEo_35yi7emogkEuDmHj-FARsNA7_mpzi3RN0hSkFc7SSbYFgkINrqV_tA3Y4jqs2DASbsshTgj4f0VHNdvQl3ig9RsHbaFjiYNtJ1nJsSlXK7DLHU7GsLOyWG42sTKlwrJDid26cZJ4B418KtGXBw1khDz4MPlNaOFaTWZS1QzdEUQzo4s3zeuZ4d0Ih8E3YE9DIl7GxPJDi2ENUlNbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNuQrkA3JUVYiZQ8xSGZsgJOdSXWPdQulN5wkIEp3JF6zM07dOmNLUuxJdjy51DLe8UkbVCs6OoUy3j7kP99ryZ8_M7M5ZMkYMAfgpWGEAltkkcAr4q_6R8l678FyYTkp3H5x6e2wLCc0tb0IgT35gXKwsL7DPhUqe_3LyEcij4d-oN7ObvR8QlhFdrQUYgiYjEVR0LGgqWhJVSpi78i1VVoOMlzwg19FHlAhdZia4SQvqoIsEXQz3LGsT3KzLJLerwhucDekqtKH5YHVsr-n8NaIwPnzmLOr0PUNTpaAUlO18TOxo2E0uGa8_m547CZ8KutF80I941vPIM9VbAc1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1_JIAyPmLeJLFghOg-2tEGLXNU7F0Naqy2YmvXV5ILJPH4eTEvaU-yUX0MvYwmUU7AUlnnCEydGltBrSsWCkDPhP6bweHLMoB_UjL7BYH1iq15gJNA_fg74jCtZ35sHu7FaTIY6aJLubFwy0lqEdy6gsFPFo2g6U3QwTw6VbyrGlVbp_LjUVK2ut_oO4nNVQqW84AttaTTWzvqgzemDd6Ly_25CCdYXplkDZYuKXGDKJd6wcaEk7gpmWU8sylVRfmnS15X4DYnvpXpgI15U_slTGmkkCr2c-j7HFWU-EvHhmIsH--wviQ5UB99c6GRodGqumzFMqCSVqO3t3ES1nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acYd0eq0rMCo5vhWYPL44aolWJ5AVgGrVbLtRVLrHJ03N2NfzD6H2461GlbC4X4pvHk9LhB3wrgrqRf-oRxqzNamRX4knybaiNzZWATx2P69DNiOBkxnKn2NVXYOZejZJhwkzo-7d1WdvztzlRpFjQMFXgVnCDPNV-xYENB7X6OOV_2o827yKUqUe4FbSz7QjEYyLKL4o-_xkyDiVb5cVDLtTMx8dR4G2X5dh4Yd0af87sgB23lFAeU7PBNh8_Bi1E9FOJAKaOviJkrKMP12rl_C9HWo8OxSoUzo04nYs5WfhEf26q6HNe80akk-QPFWJRRR5uTcskah6BnJk3FXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgHzRW4mTOMLaFnF7K-MVKuW1X5VuSHW54fi3L-9VP9RgBZ5gX9QmoSCgDbxT04nxv-3nu0UyNme0IDp-XtrWaZ_Fvy0Hw5GKf_a2YcEhMJQYBxfKkSxrsMIwldiBz-lcU1x_5vE4Dgi02rh9olBPvsB6JfU2heEKJxzUXlLJ6iV0xlU-5nQC3Mwyt3fTusxmh6Le1JgHl43aikp4KG9Rg5C5c9HJSXl4GCFdDIsf2pKmWCOdpYO_6GQSGlaPIPHsfz40rWifqJ1qeQqwZZXRztvI3ZRhuC4NTcJWPUI6rlG0ThVA3fTkMittjh7VPMJT3sTuyb9GlHPqkv7J5UIHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNWfmuYH6nFTxMLTlJBLUeV4i5Uh-tauaNJz3Kyvwvp6QmcBgJTq0J6WvBGMQJADIHeAHCWqZdb4994szr57F1DXaUKRq5tNlnoK6c9H_BPAEO-Op_pM5A8gwB10mG3pWLtZGSToC908LYK6H4AbGyQy63GWOtjG4ZjlBiNzzSYHUtriK95zo2sTkqgGxixt-xJI3L-2mFJZN2ihlU6ER-EgiyiMZDSEvG_7SO-Kaq5oSa0MTRxvSvxWrOLwzOKwRIdC3gU75TdgXzr0nTjHLOpVO5S73UO-Sxls1lHstmkPV_0KDXC2RpFtI5POy1zLGFEb3CzZLQaBtnKgAtcUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGedrTABeoz42nl2qJrkaxRIKYacEa61fqdHF2WKV90rgSBww6-PtPdRaGGNejarYSRiGj0r2kGphAwgiEm7ektnysZG_JILL_0fPcRJ6ZLnXYf57mCdDUbOMavojVeaIcivQtmbowEYolUuKQhJYCwggv0oR2zOVZwQFiOYrWVWSpj8mj8TCRiYqNrpWUie3eWbiigQbTLz7LVL22AasmT7ljy75mjiOkXYDJb4T1wS0I0Bu0OTbn2jy2fM79-r8pkAU-9P_zNKdT5FMOkwlSfODvrzf6VA63NVyv1mPmTrqjpgWIKkXkQrplFeCuc8hem6XFnYsPJxd6IC0sCcfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=F5F09iPVupw8exhPL5qWa2mA4nwjv3VHvYqtzbCaPSFQJzuMKAWDVcxt7hb0x8oCUpLHGgVTrecTgiROJNKO9hcLBWkSXqnYPElqonBJCYAfsWfhc-6GS7zMmAVi_BcZ73vfHrb-0GzOa8rISl6zssGKpuANBumZIAjSQC31tDyR4NiTFFKNz5xmCs5z5qA4U_LYiDbDfJd-2R_bsEWOmxeRacap4MdNAQD7SIst8z3-dTVF2ZGXPzJ_k4xCrg9xrGKKViJay9upf7ElS8hzxEhH_E9khf8-F4_zbVIkLUnItLS3LgiLv_soHoBTapsXok_SPRvuKD2kr6Ipx-fJkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=F5F09iPVupw8exhPL5qWa2mA4nwjv3VHvYqtzbCaPSFQJzuMKAWDVcxt7hb0x8oCUpLHGgVTrecTgiROJNKO9hcLBWkSXqnYPElqonBJCYAfsWfhc-6GS7zMmAVi_BcZ73vfHrb-0GzOa8rISl6zssGKpuANBumZIAjSQC31tDyR4NiTFFKNz5xmCs5z5qA4U_LYiDbDfJd-2R_bsEWOmxeRacap4MdNAQD7SIst8z3-dTVF2ZGXPzJ_k4xCrg9xrGKKViJay9upf7ElS8hzxEhH_E9khf8-F4_zbVIkLUnItLS3LgiLv_soHoBTapsXok_SPRvuKD2kr6Ipx-fJkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=N7tkYxVLTcA2lwxLn9FSxT56B0uPpIX0-kIcADNbM4QADXiMiDcLcC2RkRkSUEhxqQWg9rec55klCTTqeDZoUWf4mvoTIKIThwqqMd5H2Iv1mAhnEPpXyMAWxfcPM-Q4O0pFYwx48861pCjuTFBQ8zTaAe8eYtt0piWFn2SAspSX1121dHUZnKOvd-fHFD_QOU450Fmd5HClqg92S06o3MxF4mfl-zCo3x1gObQKO4JRTrhkMQ_MGU8sL-rjmG4TETk2yUbvA42EgNxgE4wIm4EnyR9HloUhNFSXv5488JApPQBZwGxZdnNxwPEVvjDUfqn3dxYtwU4xcM-9QGKZGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=N7tkYxVLTcA2lwxLn9FSxT56B0uPpIX0-kIcADNbM4QADXiMiDcLcC2RkRkSUEhxqQWg9rec55klCTTqeDZoUWf4mvoTIKIThwqqMd5H2Iv1mAhnEPpXyMAWxfcPM-Q4O0pFYwx48861pCjuTFBQ8zTaAe8eYtt0piWFn2SAspSX1121dHUZnKOvd-fHFD_QOU450Fmd5HClqg92S06o3MxF4mfl-zCo3x1gObQKO4JRTrhkMQ_MGU8sL-rjmG4TETk2yUbvA42EgNxgE4wIm4EnyR9HloUhNFSXv5488JApPQBZwGxZdnNxwPEVvjDUfqn3dxYtwU4xcM-9QGKZGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=e53UlB0-U8NOWV-LoyL0-Y8DkLLmA9yZqXHP5NDPtR323s21yqtRJ_ck0CPvTFj9M4og5H3drQqltDhm5cyN4LnGt1salY3f5wPmMFIZ2j0-6i0NDszMkv0CyMGevw_DBx5-UlfQobG6Z7jUQffPzD3batlHne8J-90t82AjDUqpytR8Az0kOfjRHUgxFwsXiUzkiF20bZHslHypYRnwaYDbP0QZeJeyd_LimawzuC04XHtiWjQvBsDTcc_NQejV0LdS-VEwJIVA-yjSo4_pXcATVyx7SgKR2RW1XwaG_gOlVxZ_y4UstNaNJpmPC96qOTJaqu_DCRWTQWxnJRm4Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=e53UlB0-U8NOWV-LoyL0-Y8DkLLmA9yZqXHP5NDPtR323s21yqtRJ_ck0CPvTFj9M4og5H3drQqltDhm5cyN4LnGt1salY3f5wPmMFIZ2j0-6i0NDszMkv0CyMGevw_DBx5-UlfQobG6Z7jUQffPzD3batlHne8J-90t82AjDUqpytR8Az0kOfjRHUgxFwsXiUzkiF20bZHslHypYRnwaYDbP0QZeJeyd_LimawzuC04XHtiWjQvBsDTcc_NQejV0LdS-VEwJIVA-yjSo4_pXcATVyx7SgKR2RW1XwaG_gOlVxZ_y4UstNaNJpmPC96qOTJaqu_DCRWTQWxnJRm4Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=e4IRu5WyMC-9TiP2HJyhQYuZaz75pupmZJ5peU1dQy7vPhdEnqD9f3RvIIlpKV9z4pafp2T0DeaZq_D-NTUDDU-Lc3MwOpsp_E0nTbERVtV_REwG9AgOXs86vtKTlm0-iRcZ7Zsea2I69OBXRnGevQUQSwyrMSM52SdyBpH4X2RUSsm653WUPTX87R8sJ04r2GiehniFoKgIl0k6NnuEAr_UsGPVZs_oDV6IFToCrLj-qInhwDuczPwPUTGvdBS2mSJgWWvU_9mKj6UyIGbVVZPzvCF-gQdP-DnEvmSUsaiNolRTVGq3S3YiPgEW585iqDnETL0RTk16WIENI_6ryA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=e4IRu5WyMC-9TiP2HJyhQYuZaz75pupmZJ5peU1dQy7vPhdEnqD9f3RvIIlpKV9z4pafp2T0DeaZq_D-NTUDDU-Lc3MwOpsp_E0nTbERVtV_REwG9AgOXs86vtKTlm0-iRcZ7Zsea2I69OBXRnGevQUQSwyrMSM52SdyBpH4X2RUSsm653WUPTX87R8sJ04r2GiehniFoKgIl0k6NnuEAr_UsGPVZs_oDV6IFToCrLj-qInhwDuczPwPUTGvdBS2mSJgWWvU_9mKj6UyIGbVVZPzvCF-gQdP-DnEvmSUsaiNolRTVGq3S3YiPgEW585iqDnETL0RTk16WIENI_6ryA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBKAgf5njtDv5hN8wF8oLAakcZ10SCih705l-S7BNfYVrpgd6gmmLPixSUvDnbBcE94CHJtfHrO41bCAVL0qi43ZB1l2aGBgGBWbXw-stqvXJgLfGHQMABBxlQ9AOpAi-cL42QYczVzBf4KWCVEUdWVmA2I6_7BaVJX-YoKPh3voMzRIJBAyZz4EVJXB51Z73mWRr62X2VzxqbyqTfS7UxF4KSqgDcKFjgcORkT0rpOYEM89Hsvqa1_AD_X-uYEcPjCpAzicyczNsPdPlvaczxihG5C9BAk2mq6zQqpAYzHBLGkC5qZUejB1RoEGZiu9hFzHfgnDiqHuW2VVTc1vGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=Ytzk-39tn_eu95tHZBzluE76bzvmdL2yy3HFb8qBl28UdP5MV0rIp2KTBKh7sFQ2DniShc-d7-BmUPIabu5aw681MsUI9EZwB9Kd6SMihdU6N9DKeXpA0MZoF3BoMVk93eR8H49RRNQzOv9R2zgAfjgXyTWjh-9QvFECTMds2SMML-lpSb5fDvB69VRQdu-i9vggqlf0RixkhgubUZPMw-JRm-UNtCD9BJ2P2kgoKGCId9o7b-VWo9qjzODe7ZclnNKLvGPmh9RvhMrlG3P3Qpcaw6hRHXsnuyF7eN3YvKb0Co8g1petCrxlDwHchbl-WR0owwCnJkORz-BOy_mysA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=Ytzk-39tn_eu95tHZBzluE76bzvmdL2yy3HFb8qBl28UdP5MV0rIp2KTBKh7sFQ2DniShc-d7-BmUPIabu5aw681MsUI9EZwB9Kd6SMihdU6N9DKeXpA0MZoF3BoMVk93eR8H49RRNQzOv9R2zgAfjgXyTWjh-9QvFECTMds2SMML-lpSb5fDvB69VRQdu-i9vggqlf0RixkhgubUZPMw-JRm-UNtCD9BJ2P2kgoKGCId9o7b-VWo9qjzODe7ZclnNKLvGPmh9RvhMrlG3P3Qpcaw6hRHXsnuyF7eN3YvKb0Co8g1petCrxlDwHchbl-WR0owwCnJkORz-BOy_mysA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYMZRuZF2kwGVmreRZHQ_6J2MfYqC2WSbHXCt6X48HOqGgoNR5d_JOp-0OJHJsKfvrPEdD0OncASTieY5UpATDAeuzCu2yRUjEcpY7zCjlwFcacF-Hf78-LCyNd9ok2chcavKa-4smueOcWXYZAIqRB2t-wEToXa5vpAvS5eldmZwkdQNpZ7vDbsMhnPECRuwJODSiCPqKPqXUYnOIeA67aXtSTye5fjSTgGEeTtwio2JvSeDIRHyRfgY4ZH2ocLUp254XosCaJCrAOmcBFSHjTJ_3PF9_KP0XKSyVmCUD8H3ks0-1qDLyhuOAcy6JJdPR5yfeYomax8CZEw0e3ynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=Fv91XwL2827KZWNOZBVKu1VD2khZhURpsRjf3F1ZjEhqZUZ99cAjDjD4CZCDaM2EMogYxdtBxisZaqe5-4emrBq-aePYf72CYOctRe0mV1mD6vSAOn80qBNW0WrS-VaefHTJ3AsmdixmyIuhUFxyIvDJPXkBVZyOCfp1zVMzXw5vy7X8cg-4rG9Ax1-zpbt2o1nOWjSAt8s4hETEGNUEUPjboMwQARc6Pubq-R3Bvb1Gw8J6dyd1wueTi8IYOB3tVgTlEwRLRtDh0sL1y0sm7IR5l6MOnEc2yVaQO7qN5bVOlxGuaorAN2RcBkbabgauHSuAM8M0589yBBi2_K2yYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=Fv91XwL2827KZWNOZBVKu1VD2khZhURpsRjf3F1ZjEhqZUZ99cAjDjD4CZCDaM2EMogYxdtBxisZaqe5-4emrBq-aePYf72CYOctRe0mV1mD6vSAOn80qBNW0WrS-VaefHTJ3AsmdixmyIuhUFxyIvDJPXkBVZyOCfp1zVMzXw5vy7X8cg-4rG9Ax1-zpbt2o1nOWjSAt8s4hETEGNUEUPjboMwQARc6Pubq-R3Bvb1Gw8J6dyd1wueTi8IYOB3tVgTlEwRLRtDh0sL1y0sm7IR5l6MOnEc2yVaQO7qN5bVOlxGuaorAN2RcBkbabgauHSuAM8M0589yBBi2_K2yYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=XLowoOeg51AmZVPsRkJ5SwRRp81TrKAWS13MqdwYKBbiV_LDR-xzQzQqGMFgrsv8Lp8C48oUTZuCHHjwsoLA7IeG2Qn1lcTQ74-lBm1LlEA2exoitfOMksmXFjZ_W6z2eY29DMLvSHJ-HK9pJOTyWCaTAxrtHFeWRQya0iAMbZs1_ZMj2N-pQ4lz0vQIXPu87GII6FfJ0P6pKn7j2HiaIVFPwwPPbIde1-UK5sUJyjyTRE7Hjwfz8hRqF7p9Z2QUKbB-OJxEBeUmIZZBblG-7vtIGbDEObDksrZ3ixQH3QY3MqXLtWobPXZsaGCFO2E8fTYAA7VwvEK2h2ydHACIYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=XLowoOeg51AmZVPsRkJ5SwRRp81TrKAWS13MqdwYKBbiV_LDR-xzQzQqGMFgrsv8Lp8C48oUTZuCHHjwsoLA7IeG2Qn1lcTQ74-lBm1LlEA2exoitfOMksmXFjZ_W6z2eY29DMLvSHJ-HK9pJOTyWCaTAxrtHFeWRQya0iAMbZs1_ZMj2N-pQ4lz0vQIXPu87GII6FfJ0P6pKn7j2HiaIVFPwwPPbIde1-UK5sUJyjyTRE7Hjwfz8hRqF7p9Z2QUKbB-OJxEBeUmIZZBblG-7vtIGbDEObDksrZ3ixQH3QY3MqXLtWobPXZsaGCFO2E8fTYAA7VwvEK2h2ydHACIYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=RuSEy5lLM9HFgAPwfS7unhjW8VohmzUYCd2EGu20w53iy_PbasrQjeCkI-aYqPwmVDZfQBH0NFG4RdtfLnVDgj9Vaud6ukdp3gd9tNG6uZNJDPlYmrWb0ZHqjPvbi2vyOKpf53Pb6-ABIVuPyCFOiSXmEicQLtj1q0W9YhZv4NEg_3x8Qg95jrpysoJdmKSLRlG6YFEf4tSn2ek3iawvcsHjWl55zFz4iaiSomeduEcDc6zP0Y0ftFtGmPKVfEVn_xQ3IiPcNrMHSA5Obtf_W05LS6iSu6arlv6ybvn4fG0KcxrE4IioUJUfAkqaIl7oMz5jhcB8vO-66d3YXecSfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=RuSEy5lLM9HFgAPwfS7unhjW8VohmzUYCd2EGu20w53iy_PbasrQjeCkI-aYqPwmVDZfQBH0NFG4RdtfLnVDgj9Vaud6ukdp3gd9tNG6uZNJDPlYmrWb0ZHqjPvbi2vyOKpf53Pb6-ABIVuPyCFOiSXmEicQLtj1q0W9YhZv4NEg_3x8Qg95jrpysoJdmKSLRlG6YFEf4tSn2ek3iawvcsHjWl55zFz4iaiSomeduEcDc6zP0Y0ftFtGmPKVfEVn_xQ3IiPcNrMHSA5Obtf_W05LS6iSu6arlv6ybvn4fG0KcxrE4IioUJUfAkqaIl7oMz5jhcB8vO-66d3YXecSfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=u58-WZDJOTXM1sxpLipa62-4Y9ZfSIKlrTOwBIKF-yn4LD0oAPxH_vnGtJ06R6lJRK_JDZqLDwSlWpWY-RSSwrFM8Z6Ow66lAKzpy4uPQRCE8L5YqR9IaPQCtd1wfvtEMFnEEJfxMe9zwYRFQKWtAI7ID75nFDpoxKLTUc6nhEMFjQUco_4ZkxRo1inlCJo_Eh_VUW0JG8ZrGPut13KBTZdxO2zkgrbTN0QLmuOluc3KchDeYtrXfDC4zoiPX9Mq2wtSOw3gG_dfm6r5oG3FsvosO2TPCZdiLhXmr_PKK8HAtrPIjgWXO99S4kXWDENJGHMDKkkhXRB2LJ3w8T5iOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=u58-WZDJOTXM1sxpLipa62-4Y9ZfSIKlrTOwBIKF-yn4LD0oAPxH_vnGtJ06R6lJRK_JDZqLDwSlWpWY-RSSwrFM8Z6Ow66lAKzpy4uPQRCE8L5YqR9IaPQCtd1wfvtEMFnEEJfxMe9zwYRFQKWtAI7ID75nFDpoxKLTUc6nhEMFjQUco_4ZkxRo1inlCJo_Eh_VUW0JG8ZrGPut13KBTZdxO2zkgrbTN0QLmuOluc3KchDeYtrXfDC4zoiPX9Mq2wtSOw3gG_dfm6r5oG3FsvosO2TPCZdiLhXmr_PKK8HAtrPIjgWXO99S4kXWDENJGHMDKkkhXRB2LJ3w8T5iOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=Zp40fT7GxnMvYcqJvNsGpkmqvC_P73sV_NpmK36NOl0ppGId5vuHzgqKA_2WtKlqK5dh5zowtWQBjECmC2jEVAt_z04AP84Bdzg28-4OplTk1VAu21CRcSr-gZyfM0PmB2D_Gay4cy_hvku7IGFEWzOa4rY7TmZWdKldqcrvz6lTX7cLw-iQUqhW94-Vz5jXcyo9WhzgkovJWFVAreQ3xsxK8szgMI5df5QuijkA3rSFcm6pM5G-bSzZFplIvsEQ_IC-TNV3smXC0yN_uCnlAZGW2XO5tkPLQrUXBW6k2zzTz2QVUM4MhgP1QEtO4q4U1iggiAK34q_zmrlV2hNLUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=Zp40fT7GxnMvYcqJvNsGpkmqvC_P73sV_NpmK36NOl0ppGId5vuHzgqKA_2WtKlqK5dh5zowtWQBjECmC2jEVAt_z04AP84Bdzg28-4OplTk1VAu21CRcSr-gZyfM0PmB2D_Gay4cy_hvku7IGFEWzOa4rY7TmZWdKldqcrvz6lTX7cLw-iQUqhW94-Vz5jXcyo9WhzgkovJWFVAreQ3xsxK8szgMI5df5QuijkA3rSFcm6pM5G-bSzZFplIvsEQ_IC-TNV3smXC0yN_uCnlAZGW2XO5tkPLQrUXBW6k2zzTz2QVUM4MhgP1QEtO4q4U1iggiAK34q_zmrlV2hNLUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=ZvbUmgWKK1w-I7vzV4DjsUXOWDEzxbxGB97mUQeDvx4Xxhpk1fz3PdrT1YZSznyeLus1GTX6_Z1lkK2Kj-gLl-ktFF66k0TD_Pp9nhFwwJodDH50yrm02ZA0JV1LrIVXGrTtN72L8MtNOVxVDkfnuRv-HCSSxLqEi9T2igngHx1IP54FLNEo2xXkMm-DKVez6UjILzvjo6WcG7yR9IRFvaiBFji1MSWuyz5nrovR2ML2V4SWfV5u5rcCQJpzIHZnTpSlgu-RawiFCefGJQ6E9nhL8TgGQ6e0aD2Kl4ZtvrFjpwpbchM3MrLEt890vYUv4Ly9Z3dj43pt-rT58kHdhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=ZvbUmgWKK1w-I7vzV4DjsUXOWDEzxbxGB97mUQeDvx4Xxhpk1fz3PdrT1YZSznyeLus1GTX6_Z1lkK2Kj-gLl-ktFF66k0TD_Pp9nhFwwJodDH50yrm02ZA0JV1LrIVXGrTtN72L8MtNOVxVDkfnuRv-HCSSxLqEi9T2igngHx1IP54FLNEo2xXkMm-DKVez6UjILzvjo6WcG7yR9IRFvaiBFji1MSWuyz5nrovR2ML2V4SWfV5u5rcCQJpzIHZnTpSlgu-RawiFCefGJQ6E9nhL8TgGQ6e0aD2Kl4ZtvrFjpwpbchM3MrLEt890vYUv4Ly9Z3dj43pt-rT58kHdhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=gxUfXUJMlafgFJh_ArB_xnzBoG1RkD1B9njCjndCSBtmOzDgGqrX7ACQqa1-LBFOzFnF6167Z9sMkxCjqweIiW4rSBeVpaVYny45JVWPBVubnpqyApTkN35mMsyi__6AtU-kVG5t4EtEyzCFm1AwoOtXdiBgrmUKEtDgs6-Q-MUYmaY1cqIAP1VTFnnHrLK8i5Pha1JtjjzWmwWBKctoAu0MBJSj3gVs9aXiSPv-oWE-L-DieckBftF7tqSaLBGeYbo-iAe5ZVBdK0K2uY7ww0OpKpzF17baGA2L3wfI_MsIjlpihBc1agu6Kh287IXTsSX2Mo_JeKKtXXtqvbtZAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=gxUfXUJMlafgFJh_ArB_xnzBoG1RkD1B9njCjndCSBtmOzDgGqrX7ACQqa1-LBFOzFnF6167Z9sMkxCjqweIiW4rSBeVpaVYny45JVWPBVubnpqyApTkN35mMsyi__6AtU-kVG5t4EtEyzCFm1AwoOtXdiBgrmUKEtDgs6-Q-MUYmaY1cqIAP1VTFnnHrLK8i5Pha1JtjjzWmwWBKctoAu0MBJSj3gVs9aXiSPv-oWE-L-DieckBftF7tqSaLBGeYbo-iAe5ZVBdK0K2uY7ww0OpKpzF17baGA2L3wfI_MsIjlpihBc1agu6Kh287IXTsSX2Mo_JeKKtXXtqvbtZAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efOzEdDQ1ymyOtVU3SdAlj-z0DFP5GgNH5OURYj7ALhtQ0mR7TGp-IdnNyk_TCbFbp64z11COMw6K-RE95OF7pdCw5ME2IwQt267_xGTiNt6PoTkFel-6KMit9ct27cO-kj_R_tFUG_Y55mlCfkKp6gmAJq6TIz5pQ_fIRWgfKZa_JB6bdgtwaMkMlCe-u4kOe2E3A3x7OG56IeMWHDmeClZ0m8ESfR92WOm3OpU5uBnJ5vbJ5JVpTmaJ9V6uOlPkrXkObBw6pxw9P96ZfUXCw5Y6Ydfdpo5hN9CsidFf4MYNDw8LzEb9v1P8IFNJss8acLwQX_NzvD7ldyQmMazkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBO774ynIaX1TlhAKc2Zpj0uiaAEW-97TTELz2Z6AGNL7PdxZPBAerqmxjCX7k3F-IJKFnr_3PnTBMHwmHW-m7PtBk2qnvFJoufMu_7VmYCwtQKhDoNAgQBLKDvjWUogb9ZJE3TE-o2T7PWJEtfd6-biw2nsoRLgtU00Jl15dAtaV7kwzgMOMTa5F6vsbY0KdW8FgwAdylfKQZz21V6em6vTMlxdod7GtGAPe8BhPDRBfjH3NbJtWA4DQDI0_1N67a4S53SUdDrnP4nOY_QS3Cg1XMYmTV3EELiYUsG9ktiqa6SptL5YdS6Ep_N5a6f1rlr7xUmMkiSGiAZ4KwY67w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=k87A7K9GNFVD-iQeemtHjNycf7LpgGKyIAM4amdL5fFMNp3Cbf8D2mZgbTT5XdxkoU1n-E4CjBLc6CymiUb7Dsv2cxub--mMwqZv4oIBwhufpG7kLVDkMxyp8G2lunzpxrXk7hdn8rTnw7Td0fpgGTlUojjEblUJayUO1RLQ20C6MSwLrqk142bV34tPzaeoLCsAioAZFta5V86VLc36Z_AlD5eWKhcLlZVn8dmO0fwmEIYEkZxIxOE3LDPhvwYlITTatqe2rwhDRi3k94TA7BGpPB38TDFnNlHo5JqbFHm98CpNS0u5o7JHjmpbj-I60rbPMP7WnjCXY9DCab2OCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=k87A7K9GNFVD-iQeemtHjNycf7LpgGKyIAM4amdL5fFMNp3Cbf8D2mZgbTT5XdxkoU1n-E4CjBLc6CymiUb7Dsv2cxub--mMwqZv4oIBwhufpG7kLVDkMxyp8G2lunzpxrXk7hdn8rTnw7Td0fpgGTlUojjEblUJayUO1RLQ20C6MSwLrqk142bV34tPzaeoLCsAioAZFta5V86VLc36Z_AlD5eWKhcLlZVn8dmO0fwmEIYEkZxIxOE3LDPhvwYlITTatqe2rwhDRi3k94TA7BGpPB38TDFnNlHo5JqbFHm98CpNS0u5o7JHjmpbj-I60rbPMP7WnjCXY9DCab2OCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقام انتقام!
بسیار به جاست که یادآوری کنم
اولین گروهی که رفت دنبال انتقام و خونخواهی
خامنه‌ای، گروه تروریستی حزب‌الله لبنان بود!
و پاسخ نتانیاهو چنان بود که جمهوری اسلامی برای نجات حزب‌الله و بیرون کشیدنش
از زیر دست و‌‌ پای اسرائیل،
به آب و آتش زد و  پایان جنگ در لبنان رو به عنوان شرط اول مذاکراتش با آمریکا عنوان کرد! در انتها هم بخش زیادی از خاک لبنان دست اسرائیل موند و یک میلیون شیعه حدود ۴ ماهه که آواره‌اند!!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAxKpnSfY-flWn6B9lM2Wgq3Cku64yrK9zs8znzCY-iLaK99u0l2D3KQwFB0ontpZ8boEU_7GLY_DAXq2zIHAaHbx4ZolQMWVQc4KhAJUrU4G8l1iPjmijOyfYnnRqWzvy9nci5e7swoIiII9oG90Gl8-qh8PLQ2TZHhgT2eXbMlGyL4EBMYNS4Ug3gXRJQqo_D56jodlzqquEfQsppyro9xtXb7F6bkdqsPG44t79ThEiJNuG7W0W0rLGl6iw52pS0Yw93CXNnXisutmNmWjrEEfYIvnqfesgbg9KC-nivtkFiaJjXhMOwdrIGn6QPzVzSy1BLPe9FlT_ERC5tZtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ayb8SswA0xns9awyq2Mp3jezSGO5VQCA4Qq2AxYqtQBgDDyK4mtafFgZ6mbIKeO1bLlzTj3HWbhbftrloDiaqZhv5uIYYM7ZN9IczMVtu4yQ8rsGxms2QjGWOfIxc2-_dfUOl9dmF56f9hsUKqaabnyN5_L9oEaauTD3lTZKwNUR6GOnWyJItoudmEyLIOhAGNO7zcKmyPxpqwo3oXvShbzlrO-wqAoCp3QkNRPNWaG4mjka49Ew8b1HzrrpjK8SNlu9Cqs1skbdYb7neJk36kVi3usoUyS9Gnmvzyo1Fi4KG1xbzIDT2V29ZNgEx2veI6_BqCZB2zSilBvTtvK14w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=Ls-vSLfUM0hzvS8ah4EMtzmQc_P9IJdNOJXB0LyimO1WL9qFVxrYKAJslwNBLWbdBE5_5_SMP2pmd39NKhVFZ7BOwQtXcTBOpFRvdQbIMXWIFUNlPYoLsBg7yXFi6OHt4bC7Pwl6YxWP4v1i9q4g4K5z8XPxawVil9VKDhrNjSDgGUZygypNsngeU6V1OSYDkBbnwFvEIkZhVwUY3PWQu3nAcY6LmJaPDOvpnfCJTI6nr7sIqpD66jm06B5oMojUOdYSa9bFBcDv1wyl_14kqlCwCi3EAJaUSyAbRGF1uaiV5rZsX8KSb_qPn-6Ph9bqDxhwRYG9vhP2_jiDgrxrvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=Ls-vSLfUM0hzvS8ah4EMtzmQc_P9IJdNOJXB0LyimO1WL9qFVxrYKAJslwNBLWbdBE5_5_SMP2pmd39NKhVFZ7BOwQtXcTBOpFRvdQbIMXWIFUNlPYoLsBg7yXFi6OHt4bC7Pwl6YxWP4v1i9q4g4K5z8XPxawVil9VKDhrNjSDgGUZygypNsngeU6V1OSYDkBbnwFvEIkZhVwUY3PWQu3nAcY6LmJaPDOvpnfCJTI6nr7sIqpD66jm06B5oMojUOdYSa9bFBcDv1wyl_14kqlCwCi3EAJaUSyAbRGF1uaiV5rZsX8KSb_qPn-6Ph9bqDxhwRYG9vhP2_jiDgrxrvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=rRY-73jMxmUoH8WAUnzroYNh5_-yyHj9_P6J7ObWwYgFXgnPvmWpozPRp4xZG3I08j8aOjPj01CO83FI8a4sMlu07SgRH0jA-kbccvguuTyF3B0yLPNMjI_X7mYXy9RR4mSPMFTjZSdtRvft7slx54HXmOGWlZbGF-5R8CUjW6nDeIybQBz44w1TnYMV5yi7yQ0l2Zwg5t5n5ZRyg-o0svewdkO0vALaMxTEe2lU8SEhWO3R74SREz6hSRhmkSy0PCQsNjPfB4okC9f6pOkcShVlH7feWnugTG2mc3YZ9gYAc6ukwZrvlg29ve-53bo-QIZ9oOOfa1XBMnhaRik3Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=rRY-73jMxmUoH8WAUnzroYNh5_-yyHj9_P6J7ObWwYgFXgnPvmWpozPRp4xZG3I08j8aOjPj01CO83FI8a4sMlu07SgRH0jA-kbccvguuTyF3B0yLPNMjI_X7mYXy9RR4mSPMFTjZSdtRvft7slx54HXmOGWlZbGF-5R8CUjW6nDeIybQBz44w1TnYMV5yi7yQ0l2Zwg5t5n5ZRyg-o0svewdkO0vALaMxTEe2lU8SEhWO3R74SREz6hSRhmkSy0PCQsNjPfB4okC9f6pOkcShVlH7feWnugTG2mc3YZ9gYAc6ukwZrvlg29ve-53bo-QIZ9oOOfa1XBMnhaRik3Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=wAnIDI0XZSQqfI7Bhg7D8MZKyX3nAsDy_bgqJBRlv8I_Zo6lR-B4DjQWq8Wa9066LV47QGqrNNv_RjN4b0Pjb1fThydh4nFkWB0r6T23de5WscmUVfdh8Uoy5AeZwOmV8gQ024sluIsMsl6cjT1Tnurv6hp-JIGXvZDn7uDC-W5nwvCB6ugFvDv61HMlndRysZe-ZtyRvDAE67-vIZVNLw3bqVfLDMmBA01Mf20q6T1IYqI9l_XEuq9KuDhFvVyctLD35hxrr9hM5nM6L3-tAlD6RK2oBwODeHDaEwYbBul_uGXfBTasvqm45WlisItWomz4kec5Jk7hlnp4IbRKnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=wAnIDI0XZSQqfI7Bhg7D8MZKyX3nAsDy_bgqJBRlv8I_Zo6lR-B4DjQWq8Wa9066LV47QGqrNNv_RjN4b0Pjb1fThydh4nFkWB0r6T23de5WscmUVfdh8Uoy5AeZwOmV8gQ024sluIsMsl6cjT1Tnurv6hp-JIGXvZDn7uDC-W5nwvCB6ugFvDv61HMlndRysZe-ZtyRvDAE67-vIZVNLw3bqVfLDMmBA01Mf20q6T1IYqI9l_XEuq9KuDhFvVyctLD35hxrr9hM5nM6L3-tAlD6RK2oBwODeHDaEwYbBul_uGXfBTasvqm45WlisItWomz4kec5Jk7hlnp4IbRKnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7VqwZaX0zJdK1O-RShN69IkacqWOcc5nzkV6w-9EPDwnfwmMc0i0NAG0JP4iMEgvwBIA12p6rUNR2Bty1pKqrfhZbz0Wo2mskkb9Nihz1Ds0PoP9uZ1OSvHlnwYdti_YvbcP8xYIJNkHbSeSd9e_TS5qK_xFX27RXJFKvm4mFQGEXFNJvVMJeSv5kkTOHCyesHj22UoKbekZul7hVgcaFPj7mLWiNuZZuRWVtbSLL5PkRHPCOLWAC9yjL0B8h-pk-HeLJ51gS8piP1F3bE4c75GX3gFCSr7l1m_SPLnwUSm3w2yYDZBlzaNPg2FoBCXpmvK-2klCfPMMtSx0pwt7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juTs2PSSlA-FUa9FUhHd8MAJJN_aGm4NN3OYqTzx6szTjekXAajR_96qo7dH45whWiv9Vd2p_ljRDSvg6O5FkjHx5Rgc6c8h0rczS7VVJ9uimpeF07q-BjpfRhozXZ0IoBDxzfavpf0WzuNPqaVIP0MBM7bfRduzU1gcexMwsWNR2ae9KbKAY7vVlLOHF7IgvjOSGUPBM45Og0WQn77OIOkiQzMjPAtGncTG4lo7nI30Xuk5b2PZgTkhDvaBScaHyGM-AGmMso51r-PApP3dHB42YXeOd2d1g1sXdX8_ji6uHMQkEqXOA-EhvmCz4pQLQoNbUDKVI4p9xr5cKBHlow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=tEe8IvLivIyAld35obrMLenCcvrV1CoSHboM89D4N2_faVliiLzF1af8BMcE65xZTvNCS55k3fQ-w2p7jlMPizVRpHCV39AXR0DhLFgpaYU4WFcsRmIenzZ2FIpxYjNUW1dIu9Bs0ddhyNKZ7gOM2N_GdvmiC5JMDl1hM6dnNSUGOL179eui0etijRzFKg47nJjaz2lxiIADQto5o_V2slNhIgHhiC-vGe3I3AlnpFWc3LKmpftlBMW_wzW0q6Xk9ruoY_cl1fy0BCIKc5maa8OhSBiLwLbR0TSBYW-qePEgkqtHPNLn_KgJCHoO4qVicaPLjIOpHZqqymcdohFDFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=tEe8IvLivIyAld35obrMLenCcvrV1CoSHboM89D4N2_faVliiLzF1af8BMcE65xZTvNCS55k3fQ-w2p7jlMPizVRpHCV39AXR0DhLFgpaYU4WFcsRmIenzZ2FIpxYjNUW1dIu9Bs0ddhyNKZ7gOM2N_GdvmiC5JMDl1hM6dnNSUGOL179eui0etijRzFKg47nJjaz2lxiIADQto5o_V2slNhIgHhiC-vGe3I3AlnpFWc3LKmpftlBMW_wzW0q6Xk9ruoY_cl1fy0BCIKc5maa8OhSBiLwLbR0TSBYW-qePEgkqtHPNLn_KgJCHoO4qVicaPLjIOpHZqqymcdohFDFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=D_VCxp9UTdnDBEsAlvjIO7ThRidSw_q2UU8fT84g1jTvT5ufJt0CLdL3L-ttDJ4NCD4dVuCqp93e6-B2ZQQETL0TaZWO2tPVuXhCTxWoG7nUZW883xl_jLLD8rSucdclU-djgGP195b9bV0J-OuSEMdYr6HRX9Mhp9Dv6Q5xOs6-2PtufxvlJudY6kjg6CeIJoaablzSFSskXXG2-HhLc_fhu6cdDCmMLGqoFebdasGDWlNQcDtWDSUVJMJy3JAzv8r8PKL5gFefzkvkC3X2bl0RditUXmVhKtAo_qU2Uz9HDmzT2zI9A9Aa_Jf2L6vxrRFtI5YWtWxC49Zn9EpiNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=D_VCxp9UTdnDBEsAlvjIO7ThRidSw_q2UU8fT84g1jTvT5ufJt0CLdL3L-ttDJ4NCD4dVuCqp93e6-B2ZQQETL0TaZWO2tPVuXhCTxWoG7nUZW883xl_jLLD8rSucdclU-djgGP195b9bV0J-OuSEMdYr6HRX9Mhp9Dv6Q5xOs6-2PtufxvlJudY6kjg6CeIJoaablzSFSskXXG2-HhLc_fhu6cdDCmMLGqoFebdasGDWlNQcDtWDSUVJMJy3JAzv8r8PKL5gFefzkvkC3X2bl0RditUXmVhKtAo_qU2Uz9HDmzT2zI9A9Aa_Jf2L6vxrRFtI5YWtWxC49Zn9EpiNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK4MERof0SUVMc-7mDFqlK6M99sElz1vX5nvMCz6P6bgKqtDBI_0HKk7FAEIy3oLjmAfTQjRsVotuocwDTmDdIC1FxYe5YHmdS-RRw6rljyL-Yg5xJ6ZV1enHIJUMj3XrRPfL2ipudOe7pBDCZJwyeX0tgdcyZkFzAtA_iK-uAHTN9ehedgvzd_RL25wq1HAkTxl7LzynIhmS32U3z9Jo-XBMvxGK33t7nEcFCK8wOoh3AGQUT2ZnU-jqyRdiF4qa4pQiCtUuuFaOZ61T4NY17TslZAZq3dH5BXvPLnFi74Ir1bc_EwH-eCPMg2SHAfOAUJyP2ov2QN2kOFmTMIzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3qfJrp4lSn5FCxmPSJBYYqD4B7x9hR1oZsEYKX7Qko2wIE-fWS-BLVwKlWO2Yd7msC_Gk8NLPuRw1f9y8vWx-sB8y_B-Hd_1yC0ggo0WaPA0l7mkmHtF1VtIqHw8EIi7BlB-EErRu-zAPK4RFY8_ql0BFco1_Jp94BY4vuvhaofG4p8hNFyTTxYdvMdgtqejSqF59ECxtZ_UoeD_ZNDjNIaNMUlI2kvhlFLmSDciaJGzSnpm1HP1M1urgHVml5CmH4JKcTYudYsRZdt4IUCg6BmEq2rl7uoweo4AHCnEypaXbbMu6u89wJ4_z-K4k6sly089VZgi87EYPkl7ogOxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXX7YuXU-qqDQ4zfIrq11otPlWr1PCE0uGuuAlbOT9EaD1SZk9iskxjAQTyR2qI-brCharT4yzQ4oh-MRLEj8pwYGAZfgtiTjvxmmY4UNbNJqBE8hDXNuozwQnM9S1TcuhAlAsTznqOnNI_I77_UyQaI5QrgCkzGDjHPWFljgtNYhBRzZAsarc95sei7FIf6CrypHAv1nqkUOc8-gRocbEcW2Be8vZ6FWPmCJEMAI74cVwl7R34kgT7jHfY4CHmiKpekjBIXfVE-0ViHXla18Qgio1cJcVAVD7nGWLl0kFg1tvwxXN-Lkj28JSD6Xf8EbRe4JrjMe_lW_enZA54vUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVHX-oxfis5Ss0TaJUV8ITn1UyYzlV_W7oEFa2rwp8WBiUmolAAbDfkCJQBcYVd73ybuzrYnHW8TGwlIJQv0Os-nH7zvzizVLbzk8iTWFC172V2t-_bzb4EtmDYSBNSrIdSV82t6z6OTiP9-s5tpQ6Vb9DdCc_cPatzB9BoF9rH3YcxcFXp6NRry8YnACqt69zv8UIWrSKgYn84US65xN2k5M6asjkZHMZ3iYA_AiAdQTgihdONGpmHnPxeu5qZQKmamPPu1C0hF4y1uue5TrvSbvj6Kbu3B4mZwuWeaWsrRxSUU1neirXLCDh11q05Ko1D8BbewUb14uj7OTtN2mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnI2ldyBHw2kRrjQ6Fq5dgBLwQof2hmYmqxLVy1WLjUPGYI1YpBbzFcrwMecIGYDxLYXKl3V3DVlC-AFNa0P_sc1dN6TTyrATQxLYHaTRJXKVK5uhIDicDevKt_lWAbHDis-FnHBEm7Jd_QVQ8-uop-zIuOzGMX8s3q0i2RvTj91Tz0LV2Nk9raRIAhytkmNt_mxlD1kdPKHg9a-fdiVSNkzPcZcHcnOySxZk6G5Jy3zrphLP6kDWchImBUDUhvSQN-5py1rX-GgSkNxXcJ909c08IiQecf3sB2rrPad-gDvh7SBf3MBh--xExRkSBMBHB_AgpwY5ICR-R9olzQJsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScJZCeHhuf0PqXKHwosbWdzKCJB5njrlWqLZ9dAUZ6wz9XgXkNgeUrmr0xgoInwB2SoKMrKmSV1grlB25IL9N6N2hM_76WyvuGxlB0E95QPERj8feWCt12Rofvevj7OXCuh_Aokn_m9zosYf9-n8jo09UNYsCrCtcETWnH726Tw5xOvdNUDcGrt7YnVXg9rZnjxwKAst1E3P1SXMfCw4LcZBjnAnZoCrOmETb2WwpAdFcQdXus0mmrvm2q96vsyhSrYvj9l0zAgSjHjx2ApKc0xNlCoZWAYKSJQDaHaYSte6dCzFbwO-hwrzrTvWYb744ZXuAdnU1_lro6CzM7Dd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
