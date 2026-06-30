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
<img src="https://cdn4.telesco.pe/file/uQhk-sN4BYEX2u-XZQCdiJTOwlohhS5TRWvkaDwWKKRR49SEu-Gj0BKi_kM2efxvizIdexUN2xtbsgIJAjSbZ3eBq8TtPqNizxI10tTxJhHB8ihTP1QcJWQ_4WuzQ4LCSGS8CB1SC9ZI993XWs-7i5SYI0GeyfZMV6Ac380EhaEeJdWbgtr1WZYKOuzyUwkafw6z_Bi1hILqGJZRfZKvI1FmG6T62hfdF_YrWaRLlD5QigJg57owXM6Ta1ZvCpmry3O4c1IWMwxO0XmcOvZMy9pWwjGaMeE5_q1_ojZZ2mFS-if6vlpg7DazDDyTWhHujA3NNCPAVx0mpxEUM1EyOQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 349K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 10:19:16</div>
<hr>

<div class="tg-post" id="msg-24661">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572d6647db.mp4?token=quURlYGZXfx-riwm3hzGbW-XiO36iqTMqFCbGROMIrsu4EFSuEqU8QLoN8wIwm38_feo25el1f43bfCoAcfP2Jb_oNGZoGaZeDXjg5uedZfJXyQN5FySHgwbajwjRAhRpAsRJKZH_eM_wwqX3EYV65y7Nw5H2L9ZnEGsT3NymC8Az2ruW6JfKiZdEEm-OPVRIxfkWWboj5xNm_NEmWqy1HkaEaCk3FfQXSFiIms32tbouMGreiZciZamPNbJD3IKPuwuZmmuC4cCOFyNLjL2zL04HsDk4kVyF1R8bPamvwZhnI1VQ4XoCLBuTOg4l8Al6HZmGQvZsR9p1CiE_m0asg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572d6647db.mp4?token=quURlYGZXfx-riwm3hzGbW-XiO36iqTMqFCbGROMIrsu4EFSuEqU8QLoN8wIwm38_feo25el1f43bfCoAcfP2Jb_oNGZoGaZeDXjg5uedZfJXyQN5FySHgwbajwjRAhRpAsRJKZH_eM_wwqX3EYV65y7Nw5H2L9ZnEGsT3NymC8Az2ruW6JfKiZdEEm-OPVRIxfkWWboj5xNm_NEmWqy1HkaEaCk3FfQXSFiIms32tbouMGreiZciZamPNbJD3IKPuwuZmmuC4cCOFyNLjL2zL04HsDk4kVyF1R8bPamvwZhnI1VQ4XoCLBuTOg4l8Al6HZmGQvZsR9p1CiE_m0asg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
صحبت‌ها و عذرخواهی هاجیمه موریاسو پس از حذف ژاپن مقابل برزیل بدون بهونه اوردن و گیر دادن به زمین و زمان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/persiana_Soccer/24661" target="_blank">📅 09:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24660">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4Uf0xiSpGiLDTVG2kp_FQRqspEMSzmZieT4dOGJQZdqwAqtSKXx0NLscPEAwgKiQHAQpT-BPgHumg5cCG5Hxi8YoEhrK0vmr8spr-yKSKFhBQ6ETyeBNJCyaTOCSUpj44cu8OZhwVxpS7GU1mUOUvtPdc-NYpyZjuxqNnn_q-caBBqcX77Q7LFZq_N8kBVCfYmzo_R86iigJIAWj4sIYWE114iPVCqJqv6Wdp98dPh_qfyO2O-J5S6eHUXcLVr79VFPXLFGVaGpG8UbSAM23KLPDSs0QE0iLA5AaAgI289Cbn762fbYaKFsv4nXGGQD8FJk_13iPIPWBGO0qNV7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سه‌فینال‌آینده‌جام‌جهانی فوتبال در این ورزشگاه ها برگزار خواهد شد؛ کدام ورزشگاه باشکوه‌تره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/24660" target="_blank">📅 09:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24659">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/24659" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24658">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8sp1iX0ftyqojAa7_cnR0d8U350fCP-z-DLIQZTeyo-ynMjHnftlv3h0D2SzwiEsojxoIzQu5sFR5ZugkrxVar3x_kxs86kDXGGODxjsJlr9wQjzXPDA8lqTx_20NP38-qahoZH0eUHd9wsCnTgs3ab6Zc40mdqTeU8PEJDdnbIN4Ljg2ULIdKeX8ftJXvbUAVrpu0eZWF09NUoX9tAT6ewsgvI3eXj202A-jGgyy8ZgViayLc4g2SEQEENsUt5VVNg87xsO10OdkEOQGc-wt1BZdE4-ILVyxiKQbcbHfBWysZDAe1Sh7C0zlddu1fnkkj2gbpi6x4TcwYiISj8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/24658" target="_blank">📅 08:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24657">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMwDJQA1lFhNa8nYd-GzfXduI2RB-X_q0oKP1lhlFQfQArfYsgvRBR-TiY489BH_ASysGsojYKdOsRayCeZ4vImWo1mxN4t9XZ0ojd5ZhEXdhKsBSHSLeTcL88UsmtnhU-WtzKhcFAaqoW604mBjUj9tAcWb2hBVp_jYpdWiHU8yXThE8NqTaj30f_4dRmZQzzg4W1XCFOp1VulqMppk9OKyUOpJ3DJllDbIQn-Mr9BG9-_13A2La73eTZ25_kLVNSqihqSPIGk0MdgX8LWKn-Uinu7ch674omMOiJ45cDCLPW24PdCunO7C50GuOKlJ67iCeEs-4cm7HV-xzn2dMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی بعد از صعود برزیل و پاراگوئه به مرحله یک هشتم نهایی جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/24657" target="_blank">📅 08:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24656">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V80AHv8d98DwgNlZv9a1nKrgUi-QLOxiC6dFhdOb43ulZTxnsXrk0-ofxoRQgCLpXvH8jvmT62sxt8_IuwZtwX6xsex42D0rO98Wa7eJR-3U-bwFZjsA-ys_hwffp3IlkHzghGbB6DSaiS-KZz5_frDtQQrkMKFJn1v79ckRus8MSPxuNRCisY8nLHRiN69cOFwiQyGwzBLDDq7ihLzmvSt5_hXHwOeDROIKgAAxFCSY-CwN8DIY_hdASC3OfHqV92a-iPsaqxQASHq_-w8s0NX25F2nQT0bTeYG8Z0v756wtgmIQhFeRphjvbHCZ-HvmkpXY4Ur925GSmxL9qTLvb3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V80AHv8d98DwgNlZv9a1nKrgUi-QLOxiC6dFhdOb43ulZTxnsXrk0-ofxoRQgCLpXvH8jvmT62sxt8_IuwZtwX6xsex42D0rO98Wa7eJR-3U-bwFZjsA-ys_hwffp3IlkHzghGbB6DSaiS-KZz5_frDtQQrkMKFJn1v79ckRus8MSPxuNRCisY8nLHRiN69cOFwiQyGwzBLDDq7ihLzmvSt5_hXHwOeDROIKgAAxFCSY-CwN8DIY_hdASC3OfHqV92a-iPsaqxQASHq_-w8s0NX25F2nQT0bTeYG8Z0v756wtgmIQhFeRphjvbHCZ-HvmkpXY4Ur925GSmxL9qTLvb3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/24656" target="_blank">📅 03:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24655">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=Q3OVpk2RLHuebs59eZqewQL03-8-bi9GZH_jY6e2jpNnYC5DVO-Q23K96wOjmJ-PCmJWxN1M4Xr6xzYvQ7LBxllWoIcQdqSOBglsq7e1F3AXRubA1YBPa6xw3aku9W2GyNrrXIdJIlJMqf3rgDD_9ahmw8btdUKte1wSO2skED_35nZuMaP-_mUGAiShq-arpkrmKdQQeG5MEZF-7K_9zutPpNw2l809GSD9ImW9dK1cQ-omB4RDKj195vgiUXI4vMRsP36xPB-SMmZivK0XbryBoErJst-0Y_a6M6EO1cBn5QxDuhj9iGzQ7_2wBhC8ycOVpBn_L0bZrOZ8yldbyJnn8qJRy180qRiiZ5PzYGvoIsxJAJjN054x8HAM1ov6eTRl3mF25SeOG8gGtJEfW6zoSqbKycv-aToQUiCDyw7BVE1vfEAKDhw5OCm7tqjQ_ShpOK5o3fJpO20fuYbb2TGTb3XjG_Sl-Er1HfTwTJrqkfH9uN3Qrg2BhEIyZz_yueXFlGjNF2i_H8lYpkW6uMhdic1hDK10E3va1JuUMO9B6VU-ENT51k_vOj8Woh4J04rKadM1C-WC8gHAV6ricaC34kB-rRcue51D131Msh_Jx-QlC0k8YJghh317D3Djc7JrE5h-3BJ-nDlVeIDh4MD_izG7_i-w1Fs6kLu9-18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=Q3OVpk2RLHuebs59eZqewQL03-8-bi9GZH_jY6e2jpNnYC5DVO-Q23K96wOjmJ-PCmJWxN1M4Xr6xzYvQ7LBxllWoIcQdqSOBglsq7e1F3AXRubA1YBPa6xw3aku9W2GyNrrXIdJIlJMqf3rgDD_9ahmw8btdUKte1wSO2skED_35nZuMaP-_mUGAiShq-arpkrmKdQQeG5MEZF-7K_9zutPpNw2l809GSD9ImW9dK1cQ-omB4RDKj195vgiUXI4vMRsP36xPB-SMmZivK0XbryBoErJst-0Y_a6M6EO1cBn5QxDuhj9iGzQ7_2wBhC8ycOVpBn_L0bZrOZ8yldbyJnn8qJRy180qRiiZ5PzYGvoIsxJAJjN054x8HAM1ov6eTRl3mF25SeOG8gGtJEfW6zoSqbKycv-aToQUiCDyw7BVE1vfEAKDhw5OCm7tqjQ_ShpOK5o3fJpO20fuYbb2TGTb3XjG_Sl-Er1HfTwTJrqkfH9uN3Qrg2BhEIyZz_yueXFlGjNF2i_H8lYpkW6uMhdic1hDK10E3va1JuUMO9B6VU-ENT51k_vOj8Woh4J04rKadM1C-WC8gHAV6ricaC34kB-rRcue51D131Msh_Jx-QlC0k8YJghh317D3Djc7JrE5h-3BJ-nDlVeIDh4MD_izG7_i-w1Fs6kLu9-18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/24655" target="_blank">📅 03:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24654">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMrruJ3y8tnDhHhK1LmgIVokqaulelkQWE101QhQRYCR0p_ak8ULgPr94HHHnjMWY5OiaqwrsZ4eRxOYE0Z3E6JQHNIgoKSexDrPHMYhhSMYhsl98b2eoBft3iX44MqX9TFJVvYHQFJI2Ky8c_jcfhn2pyuLSDfLAE07_T5qh7RZz-tDKlKX8sLhM91e_h35Ql8s-T-PfO4RCwP6gBRyEGi4E185WynbGy_Hs8h6BQ6edvXQ0jp5BQ4jJjoZDQAxrjXiVGgQm97SCOPLp5BL39EFyJz5Z1pRf2_exXNVdU_yp6rVsTp_kfe-kiAXmiXvTDJk9JECv1a5QMf3x2uw2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/24654" target="_blank">📅 03:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24653">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=ri0Xe9GWRnpYgkw0ZnEUzUZoS8AP2b4BRSyH__99AbAllduUvsXWfjwAZ8KYvMMn124qsaIWnQuz45CyD3OCDkRK2kINx2ksYYw95ibJJDQynfgqxtTqHf09zqPvkjv0z4Lca9IMahd1EajKxJh_hBccQagvAUXbpoajgB6iEHRbo_RAoKyhO7L3m9ihaJgrpro4FOdfFPo_XYV4j6JcBLKg4um6bmwAA0VG7XeTS_SSS39TDIt3HnqO6Mg3QDdUfLBQn1e9nfDNVImHS9bxDjHMgsJtFNhz39wiGViILQpr_xzj7jeC8ooBLKtvm3J6ZRjk-3SHYbJCy6aB9CqkzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=ri0Xe9GWRnpYgkw0ZnEUzUZoS8AP2b4BRSyH__99AbAllduUvsXWfjwAZ8KYvMMn124qsaIWnQuz45CyD3OCDkRK2kINx2ksYYw95ibJJDQynfgqxtTqHf09zqPvkjv0z4Lca9IMahd1EajKxJh_hBccQagvAUXbpoajgB6iEHRbo_RAoKyhO7L3m9ihaJgrpro4FOdfFPo_XYV4j6JcBLKg4um6bmwAA0VG7XeTS_SSS39TDIt3HnqO6Mg3QDdUfLBQn1e9nfDNVImHS9bxDjHMgsJtFNhz39wiGViILQpr_xzj7jeC8ooBLKtvm3J6ZRjk-3SHYbJCy6aB9CqkzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هالک‌ایرانی‌درگفتگوباابوطالب‌حسینی:
شمشیر خوردم و مانع کشته شدن یه بنده خدایی شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/24653" target="_blank">📅 03:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24652">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g17cI34tjTAAtNg6LEtO3QZLEZdXBQmrfu_DeAnNIYqdppPtACzEZqE--ITpzBchh9hSLwVu7UD_Q1989U_QVLYP0fi3GQDl8WaccJUS0ajZC3ew-J03FppwNNhlzvibaYeOpaD1BdY2YxHQljHSvdgJ1DDl7i58C5VgwwtlZAjXymSCAYABa7Th55aD9Y5TTQpDMs8OfNcx8rsq8z-TVpB2ECTSQSjT-4fl0wgvjfVKraBsuvNIUqCafOvTldLEiXByE-OfzNNC-1mlKOyMzj4iAOiqicRVhlcU_flQDeyqNQlnYhbyQQfSQXM4uyLAnjijcpdlVegvt_iHfw0rCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/24652" target="_blank">📅 03:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24651">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8hUeG7o9cR16ZJkJzoEhMYim1wKCX1bwEujsSN1t9RAxnK4Ixi4ARlGq1hHehZF8hibSinz_XNZ9y-3DHVPjmErX0tYGkPHjtSEvNnR9uIYU1ob0LMxnbemW3BD47XvhjQX6c2jIU2TjPh7wlN6Yco-fE_aJGGhjliwLIK8szJxhLZVhuji_iMjp82xVmygsk4xWBl-CE5p5ppdQ2gQtvMvgbLrLKw3Qo1DaaFQ5J7VCn3360bf3kvXNrok-qrHLRFoo0RjzZxABieG35kdK5nD2c_FJFACyJGCBRI2Zdd7DQcMZl4xy0mR_AEQDrdpNdenPQLmJVOuBF3fq9Cu4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلمان‌امشب‌از پاراگوئه‌گل‌خورد؛ آخرین کلین‌شیت نویر و آلمان توجام‌جهانی‌برمیگرده به فینال 2014:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/24651" target="_blank">📅 02:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24650">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=dvvyFxE_M7QZTzcdHX1Ppv73J3mo3Oxg0kLRg9MiFd7n7EgdXmuDqHPU5dyFHk_fTOzZZeEgZeQFfTZvJFxw8IFF9p96NrC9Yj3iUhQj_FppiD8UWN_zkEHm034cXm_8QlYk5qynZ2Iq4Tr8t_b3pnhtQXlDrM2a9f_eJ17jYIsKUkuBwABSQbmqd4Wp_lwJpV0ud8TIkKC-26BFw8ciVUWuxJo8Hs__gbgOE5_EozPW0OhNR1Pq3LprfLhlkRs6kiKq5SjIsuki8ZEIiAUuI6LAWzKphNLsgFtAdSM1MyKLdIIcRQxB9MTrJyTYxoHDerSrdfLLHhQH2Awpcfa6YaZ5cxuTK4mWJOJLwWkyWPxXh0EiidZ0bqApIgrCwXbqC0lWG8TefP8AlExGQWtkDwCV8XKnRvQrT7PuDvpnHMVfadfo2u4VyN5cHNPI-gVpP4eYKbJ4Ium-JhX3UwsDNLsK5mzwWicrqcvp10b8QxNFvh4VpYRmZxdDA3-SoJpoqN-hILGzq8LsTcUN4W4kavN0pryvY1tJNyOpmQeOSPN6TTMuWkCjaKiID13dgM1xIpsKz8pl--QHg3vz2-yGPHV6L9GhWWWLI7pYswFaG76xp1Gwx9s7i7tSYzB8LmhIdRRB-gKsqOyADxmtt5Dx04oFr0pyS_EUbFu6sWWSc5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=dvvyFxE_M7QZTzcdHX1Ppv73J3mo3Oxg0kLRg9MiFd7n7EgdXmuDqHPU5dyFHk_fTOzZZeEgZeQFfTZvJFxw8IFF9p96NrC9Yj3iUhQj_FppiD8UWN_zkEHm034cXm_8QlYk5qynZ2Iq4Tr8t_b3pnhtQXlDrM2a9f_eJ17jYIsKUkuBwABSQbmqd4Wp_lwJpV0ud8TIkKC-26BFw8ciVUWuxJo8Hs__gbgOE5_EozPW0OhNR1Pq3LprfLhlkRs6kiKq5SjIsuki8ZEIiAUuI6LAWzKphNLsgFtAdSM1MyKLdIIcRQxB9MTrJyTYxoHDerSrdfLLHhQH2Awpcfa6YaZ5cxuTK4mWJOJLwWkyWPxXh0EiidZ0bqApIgrCwXbqC0lWG8TefP8AlExGQWtkDwCV8XKnRvQrT7PuDvpnHMVfadfo2u4VyN5cHNPI-gVpP4eYKbJ4Ium-JhX3UwsDNLsK5mzwWicrqcvp10b8QxNFvh4VpYRmZxdDA3-SoJpoqN-hILGzq8LsTcUN4W4kavN0pryvY1tJNyOpmQeOSPN6TTMuWkCjaKiID13dgM1xIpsKz8pl--QHg3vz2-yGPHV6L9GhWWWLI7pYswFaG76xp1Gwx9s7i7tSYzB8LmhIdRRB-gKsqOyADxmtt5Dx04oFr0pyS_EUbFu6sWWSc5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
صحبت های عادل فردوسی پور در تعریف و تمجیداز رامین‌رضاییان‌ ستاره36ساله فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/24650" target="_blank">📅 02:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24648">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=qINYjApyvnGJRv5AifbrAQ8k7AqelHUqsRyppJPpjZVQ3qZtGxJxMIcgymh5Yb3pFmjXtw_gVF9_ZlJzql4A8pQiYx17dMoCRab5PZJYXD1nKaXKSJkQ63j37NrbSk8rOdtXXz46o-vQj2Z61VSMU5yLUx3i13zOv6IUR9Md4KF9A-KuShpb0MGF1fA34x84JVLg9JcXY6RPBiAcjKt47tMaRYFtLUwtWq1kY_UEtVY79OSkfwAXZPXkMFZktF0hLu-S8G1JmiciaT5rLmW7N6GaB00k5JoTYYcu8t4OgUGUeot-Nq0A15uuNjwici_XaXSpV2atGcyxsm3WjqWyig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=qINYjApyvnGJRv5AifbrAQ8k7AqelHUqsRyppJPpjZVQ3qZtGxJxMIcgymh5Yb3pFmjXtw_gVF9_ZlJzql4A8pQiYx17dMoCRab5PZJYXD1nKaXKSJkQ63j37NrbSk8rOdtXXz46o-vQj2Z61VSMU5yLUx3i13zOv6IUR9Md4KF9A-KuShpb0MGF1fA34x84JVLg9JcXY6RPBiAcjKt47tMaRYFtLUwtWq1kY_UEtVY79OSkfwAXZPXkMFZktF0hLu-S8G1JmiciaT5rLmW7N6GaB00k5JoTYYcu8t4OgUGUeot-Nq0A15uuNjwici_XaXSpV2atGcyxsm3WjqWyig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/24648" target="_blank">📅 02:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24647">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRQKdV2g2cOV70qZaJN_G31Ji5s__0MxMDoXgRZ5FI6hOdb0DF-OfvYe_rPuR-S5xATjBI3uwcHDA12_XGQQHwsB5zo93dq7rAbUXlRJf1TG1vS6IA-MOaYPwdnefhnnh4DrKOIhug9QIaSXAVc5Fml9PONn1WyEEdBtfDjEfmrKq94MsLu6mTiEXgsxJo7FL3ci_JdVtBswcVfOBC_VIDggdyIrwxKPbHRSyDH1ROlO0lhpsQ4sQwbiJIrANHeWquRNosqbExQHhewsRCRvz-kiDBLWoejuxicIWBm3D0gPh7PQ6xhWvYIv5C8YnXioqWi6E0Oae7KeYWRTjIfk6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جواد آقایی‌پور مهاجم‌سپاهان:مردم عزیز اگه تو رشت هستید و نیاز به کمک ضروری دارید به من پیام بدید، کاری از دستم بر بیاد براتون انجام میدم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/24647" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24646">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/24646" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24645">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WU52KL0ZneZhKnqXRYiHWHEXS7RrBIQnmSwpG1yZOLGEJNsgCwN1-Vwx3_apRiQ9dAjtYCR6KBX0ThoIzCpMxft0DyBodDRYfjKuevgwMPMJ4nOVq6TEsDjr_sI0ovhSQoZNBetuVypD7CMhx8kFNuHkvXdxKUArHlaUvvRqJagAuqV97b3coB0ClW5ndYHfl_spaySTK7BUhLa8nc-NfXySK3BvRHvPpFx1sX1983XG8l8IfKUCTc73YQRwjghPiM44FJk8Pb2C1sO4Q14RMHn4LsoIUR5VEWheVq60U9OOFLr6SFQUoYD9QxIYd9I50z2EFJe6ZrTdo-4-Rr-sUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
عجیب و غریب
❌
اما واقعی
❗️
🚨
با هر بار شارژ حساب کاربری در
#بت_اینجا
میتونی
🤩
🤩
🅰️
هدیه شارژ اضافی بدون قیدوشرط بگیری.
💖
خودم 10,000,000 میلیون شارژ کردم 2,000,000 میلیون‌بهم‌اضافه‌تردادن قابل برداشت بدون قیدو شرط
😍
همین حالا شروع کن !
👇
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a8
@betinjabet</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/24645" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24644">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRxcvB5bgejRGBX64qMRfzexXlWwbpmumqqMhrMoCR6DiJ5qbx-dl1N-UFWeDuwHERzrNtLyqIYYIkX80KVeaXEFKps01ug7GgQUTR-Z4iDzINwM8rPAOhPA_O-Qh_fvkwcPnmpuIsADe7SeaiSzywc-kOXKMHl023ptOqo6LKhwAWuvY9CH2KX9Ei3leXr4_aC8OvQ1vFtDKfKuksMazSOX7LQkj43qIYl-21Y2kgDhxlhiXvZHr-1QoyzxPQFOkszxWP9burP2K5PojKH3jujVb6yICl2k40T-MdK2G9_W0iogyIsQdghbQ4vDmqCWGRdd7mGdhrpbfky0B6AdNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ علیرضا بیرانوند تو جام جهانی 2026 :1 کلین شیت نویر تو جام جهانی 2026 :‌ 0 کلین شیت
‼️
تعداد کلین‌شیت درسه‌جام‌جهانی اخیر: بیرانوند دو کلین شیت داشته. مانویل نویر - 0 کلین شیت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/24644" target="_blank">📅 01:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24643">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqyJ2rBybwy1hA8rnDgZtQs9qNeU_DQ1cTTy5q8fbThMdr32sp3Kfiax68noXFujRdcLZniDQlKOmFd72G2-qelgKd2n7BzzBp77CI_rVlFoF6rcvHd59GNi9L74K4ezul_nKcOVZ8kn4RGCCL7qd58mNF2PkACmQbFUTayso99DcBRDhvlOBPnKVrgnIbXPH-1_18QCkwYG5OkZnOI1a8Rtms4JvHjt2dYpKd42t6myb9gKs5R0zaWjrkvIN6rbElehdRRW7gsgPqBIHK1e-iNXxDZAY4AxBGVLc3KFsoxeFZjC4osYYaE0NT-h43qcBKHq3tbk8zHO6Wc7ZDxdrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/24643" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24642">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1fPT7yDGUnY6o3ShR3ce5V0F0yxQ6SKBG5J0ZOQVxaqJks46A_PGLm1DrQ_Y4YxItzpUy4B0AU5Z3w82eXElwnnWWwFmAnZB1UAhMAmxdy3edoQZrmqQbe8OuvKyVnONd3uyj1vS2XVFC4v8fwfn85envznfD4R6snCiYEHnvMo7ULBZu26hGAf1a2AHY3X20Pp-b9wHDXF38WB5gZd8c5nLWOrDUH3pbZ-n5OdouqUE5Nfr3MvR7ImuoyAYtyhj8uiTIm_u_mt0gcMAMn_IscztFZLWea0iluOLT2vrmOHI-npwNQBpFdGKhongJ0YuCBEV47Es9mGXXpUvhYB1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
جادوگرغنایی: تیم ملی آرژانتین با تمام ستاره هایش مقابل کیپ‌ورد غافل گیر خواهد شد و باشکست در این مسابقه از جام جهانی کنار میرود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/24642" target="_blank">📅 00:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24641">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxTtbtuFQI_UypHu_5Ems8_AT9h3IyAyWl87gciFKwpYXbu8SlqUglopvbME9Hpo6sRkUbaZqIP3DarfPDHzzPQsV7r1jjtVhIjJxWQ8FjILmSpqST39Qk1cFDnNqbv55j8azVxSOJTOMNIDgMC0KjTkGM4lI_Mht2upmY0f52mA90x2vkM_5CTjUiEu0cpjkbH_s5Ykd5gvSkmcZe_uEb9BjHrw0e1Cn9bK20BBXRV1G0tGyQ493hr_swoU9YKAWg6xXEZRN99zOUHPpCn0oCMrbpDeUTS3TPLqZZ_-Ck1mzK5_NHzP6ATMLIaQg1xGMw6T0_scei5Z53gE23VIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق پیگیری‌های رسانه پرشیانا؛ بخش رسانه‌ای باشگاه پرسپولیس پوستر خداحافظی از اوسمار ویرا روآماده کرده و بعد از تسویه با او منتشر خواهد شد.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24641" target="_blank">📅 23:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24640">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=NzCp9n_sVKErlLWxk4GuQNWbzog15Boh192swVWDSx3RR2QqkTb9gF5IBOjnnx2CupBB2ILMP_7Vb-PRATXxoFe5SoH0_t5hNrQ1mB1uSHxgNGnmrEmMQJ1dBEkXjmtj5iup6VRl7QR08jbmzOpLu2rLFHUStFbCSgzLRnzblm2DuU4tVsS2pV4AgpDmYHNVyFZ4CigOqPQHX53XkSByos-nSec9_2dLzbIOmo5C3j9IM5IuzsidxNKvx2_c1VGeN_melrNJ_q8YO2dwiDzX1PxYrtWcVgQIoh3a6Iv0bF_yBMkr0h4baTXfx-0ovAZj80rrCkRpeVgWjM3fNQuMdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=NzCp9n_sVKErlLWxk4GuQNWbzog15Boh192swVWDSx3RR2QqkTb9gF5IBOjnnx2CupBB2ILMP_7Vb-PRATXxoFe5SoH0_t5hNrQ1mB1uSHxgNGnmrEmMQJ1dBEkXjmtj5iup6VRl7QR08jbmzOpLu2rLFHUStFbCSgzLRnzblm2DuU4tVsS2pV4AgpDmYHNVyFZ4CigOqPQHX53XkSByos-nSec9_2dLzbIOmo5C3j9IM5IuzsidxNKvx2_c1VGeN_melrNJ_q8YO2dwiDzX1PxYrtWcVgQIoh3a6Iv0bF_yBMkr0h4baTXfx-0ovAZj80rrCkRpeVgWjM3fNQuMdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24640" target="_blank">📅 23:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24639">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwnHnd08GaXtjpIv2G33spMKvafNQmPbxNC3ZjNgwis5lZovY2peaCcVmtYhk6xBiu_wpp78H7GyhEzsizcYrVZCjYMmtQERgWE2R70fzxjTbUTHCwJqb0cVM8lCcP46P0XxMGEkWGj3okwiYZkOIPjvN7GLs0uzJVt1x1LrdrEviRe0EdaT2OvZH3F60Ap46CDfIIlX91TlpiuANxlCxT3HaRIXWMQcF6cTYzrJtzLqfzOsFcQkmJlOUHek_fdV3o9SMJUyIbWgFGIunKg8USyfMTyTK66udbUZ85T0q8JobDq97RPHucg4muwKq7OzKTb-l6TBgZtnWQXyV3rYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24639" target="_blank">📅 23:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24638">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls_1P_wySArlWWGht1jsb7lYY58QnwWEsuYyQg2tFmrh17T87puLJmhzZc2BQ_KeqlCbnwn0B-fGQReV0tIxJEaOGObR7Atg9BrUNIuLVAFwcTjAhm8ODo8jkPErIhWjRfyqscVFHXZtXKD9rxz4_gKSQ6Bx6fT9wSHbXSDKgQOfBxloGc2V4wSaJEBmSctD7Ms4jvf3uzVa05OmDGg2hSkD-OAL9632U4eqlK9kFxUjus6B24qwkqK6GPwhkw_xJSpvHKXbmXVjeZw5gG2RKpp06vbtS3ydpo7x55mBDa8u0i6DAuwHlwJOGLeGPDYZRujcH9KdVJ9pO3i3nG7OJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛صعود دراماتیک و نفس‌گیر شاگردان کارلتو با برتری مقابل تیم شایسته ژاپن؛ سلسائو بالاخره سامورائی‌ها رو شکست داد و منتظر نتیجه دیدار ساحل عاج و نروژ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24638" target="_blank">📅 23:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24636">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_Ip5fwjosYmVO57UJWi11kjLWZKVsV25QEno5k3mehcgpa95K8tp0y5pzfHmbmdLSpm3NiNdNJUbXI8gWF9H6v6oz-TbbmMjIEZdpw-42GXaQkv_o7MKHNLKM0EB0-h28Hv9Lmvp6-ZvDJRaFQIcs5cAOuRoKKAEFZ0SkYRLMME9zuZnb3dVSCMqrqpa6ZheJo4rvdAEkiXoTDKhq-2ho77OmADVDwTpJubeZOpCI7CGi-RIcEJxkD1gJ-FtJOqCSEN_NOWn4cdubRruuAOOGT5LjDQP1KC_0JMVDV3_UxUfm7KEhWH0XUEDN0mZIYHxq6cCtVpqBBnq6TW94fVMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛
از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24636" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24635">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JK8h2PYEHCb16ee2k2p08lBTCU_petDL1Jj_mn_m7HSzigVrHWOCGb8BMkHCs-bo5IeBodEfQh9YBP4GjUCHVN4g74P_Rb6Egzle6HsdJxVkHDZgbLMDisyxJYppGRrh7bcRngnIpDbY4etDQ7vYOXx6ocsnwkj1cz_5tkVTWpVGeMtNCP2pZ_DzRzWYeU2r6n-YqMFEJkWr0lsVJJy3OVeMXlACtcMWXpU4M40wtzMi2DGQ7qUonaF0roI2vdPiV1oDeeDsHUSsoooSacd2FMQwensfO1YFNYqLkytxlNKMyzPHZwD9mwYE7OQNlNgRIOJ7LRmqwgLuqvIvfA5KeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛
گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/24635" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24634">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtdPFfzG0Roi2f4pJmU-wqjIzG0QJbFSOyzg4esMF5pSfuWEE1u_ml-toIG8AGRT6Xtkm3m9R2e5BDeTHFz5dtVCwhNIDiMWYqKDg3CWrmT6XMsgrlzTQrW1s_OXCPvBulOeqBeDm-X8p3CBzcrRxKadHpwV_hp7qhwsgUjAt4PGE4_Y2XgfUtN-XPkTUPeE8swz261l40PGTcZJiajy_zldmYpQmMxmOaf7Nv--PQM7ZXkzocJnOHUjC7aLcXHHGmtjhUbQ7yQqae9hZNFvnUf7MdOXzgEqeHZQa08_7B_GEQ54YezNQ-TkNx2qwqkHHvf4q-0wVJn8zF28PPXo0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🆚
🇲🇦
🗓️
۹ تیر
⏰
۰۴:۳۰
هلند
🆚
مراکش
📌
هلند یا شگفتی دوباره مراکش؟
⚽
🔥
هلندِ که به عنوان صدرنشین صعود کرده برای ادامه مسیر قهرمانی به میدان می‌آید، اما مراکش با انگیزه تکرار شگفتی‌هایش، حذف یکی دیگر از مدعیان را هدف گرفته است.
👀
⚡️
لاله‌های نارنجی صعود می‌کنند یا مراکش همه را غافلگیر خواهد کرد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24634" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24633">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3KfqEW3b0AQvdNjZ7uQH3g4lfek0rqHM9H-ZqHod1J0R9eAmziyaUQlmzMg4EB8HDBJ5r6PDFfnryeR8bFBuyzMGnRqdebNhiKPIRXCtlUN2VkPv7O86I-sWnZkgrFJ7e4S3oiNUFxOs3CQgaUVzhmoCVX4sW38s62diZOArINdmbaHmqvez8FuNeiT28a5fy3mN2N3JJRnQL77086G45PUIHvnnBr-jK49Bum_Bm5aCNrj22zeKYI9vGKXRghqfHiCDzaPbElfZer0z6Ir61IR42-fFzwzB4oJn8YSewbf22WAU27iSew-0sV0FsX7SQgwb0KA37YXraZtmiwa4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24633" target="_blank">📅 22:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24632">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbGpqMY_LQwwcLH5WmlJXHAkBTORebXz-R93-RlM_7O0OEBLZrN6nHzCy_efHeUQzurilg9igh8_v6kNri842rKs5kz3S7mKZn92ULRMHlse0FQjEIku7Hvn5bjuCnPJzymTUgfUZ1bF4cR-Q3_E2BuSn0O2sFNSwMU48FSM03mF5nPQda1Gk7K_6bnbmg_TYBnykUw9CXwbaAVX7GEDeG532q64qQYC4iV19JxTwC8UeVVjml3ygMvvf3NeuOshJqXxHrncgQiULn0zU8z6zDF5IgOF_WgzBZJ9bZwjZLX75OrBGnBxa6VzyjiDaz64aeVyoCSEIpM0gzmqxqXGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاسمیرو ستاره سابق رئال مادرید به این شکل گل مساوی رو وارد دروازه سامورایی‌ها کرد. سانتر دیدنی گابریل رو ببینید. قشنگ گذاشت رو سر کاسمیرو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24632" target="_blank">📅 22:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24631">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=HN3aZjjgIKa-M0zLrgtQK1ImjxUTuOKW4A8tpskhRlbajo7oeIPjy_yMH2o0uKpG5HHytD6cTJRP4oSTv1GuUsKII89eNT9gregXNEWuuM68HElpqdtWouEu6D5fZf21pQkvfgeUDeKq9DmaTXzf_EfAxO76g2shXFDdUnvAWS-tlS0E3DwOydpAyEX1sNBZLAqZ3-FAVW2mNBsiDbuO45ufR9J83srUHzLMZMz0egTrm4RBU5C0a3BfZdzOb_VHyQPSQ5MbBwgpBl7u3d7ERKs1JB4enuuKhcLDPqPqGrMUBnvpUUredgK3t-Jq6hSklilHmjVfbAhGfAT2Df-PfFZjlKETJGWknj2Up8yIGNC5gW3my7015BVoqAM8IOlch9wxhZg1qO6uj35lGQckxCxs8jXvc204woJc8XdbniI1d2OOG5EVVAC4UWSSYyX_ZDLQS4d92DXkcc315rTqQ3GVr3WCw7vAiyajqz-LjHvph5gg0ho184OAWGWYG8XOqBpJNHIY1ZmyON_bQBP_1P8diFChJ_spLh54CHmBoPzVJGKfnTMDTQj9RJlUsLaicBIBfDDBwZtBLX7V-3VjF59ocFP1TZJ1J6nWtTKJHiOztRnbq-Bfd8C13RV0wY0UqXiQXCbD6t7Dc0K8M7-WwgifwQA9IT_08bSk1kdIIgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=HN3aZjjgIKa-M0zLrgtQK1ImjxUTuOKW4A8tpskhRlbajo7oeIPjy_yMH2o0uKpG5HHytD6cTJRP4oSTv1GuUsKII89eNT9gregXNEWuuM68HElpqdtWouEu6D5fZf21pQkvfgeUDeKq9DmaTXzf_EfAxO76g2shXFDdUnvAWS-tlS0E3DwOydpAyEX1sNBZLAqZ3-FAVW2mNBsiDbuO45ufR9J83srUHzLMZMz0egTrm4RBU5C0a3BfZdzOb_VHyQPSQ5MbBwgpBl7u3d7ERKs1JB4enuuKhcLDPqPqGrMUBnvpUUredgK3t-Jq6hSklilHmjVfbAhGfAT2Df-PfFZjlKETJGWknj2Up8yIGNC5gW3my7015BVoqAM8IOlch9wxhZg1qO6uj35lGQckxCxs8jXvc204woJc8XdbniI1d2OOG5EVVAC4UWSSYyX_ZDLQS4d92DXkcc315rTqQ3GVr3WCw7vAiyajqz-LjHvph5gg0ho184OAWGWYG8XOqBpJNHIY1ZmyON_bQBP_1P8diFChJ_spLh54CHmBoPzVJGKfnTMDTQj9RJlUsLaicBIBfDDBwZtBLX7V-3VjF59ocFP1TZJ1J6nWtTKJHiOztRnbq-Bfd8C13RV0wY0UqXiQXCbD6t7Dc0K8M7-WwgifwQA9IT_08bSk1kdIIgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
جالبه بدونید که؛ گل حساس کایشو سانو مقابل برزیل اولین گل دوران حرفه‌ای او برای ژاپن بود. تو ایران هم‌بازیکن‌داریم تو بازی دوستانه هتریک میکنه تویه بازی خیلی مهم مثل مصر پنالتی خراب میکنه. فوتبال ژاپن 100 سال از کل آسیا جلو تره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24631" target="_blank">📅 22:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24630">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔵
تیم چادرملو بعدتساوی بدون‌گل دروقت‌های عادی و اضافه توانست بعداز زدن ۲۲ پنالتی در مجموع ۷ بر ۶ گل‌گهر را شکست دهد و به سطح دوم آسیا برسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24630" target="_blank">📅 22:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24629">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZdohz2TApj49LC5iZPm72kpMdzwWCQl0X7TEqq5J-4AaOerzczm2ZGzT3jquEoUd9EboDoAi0mu7iknISglPiKgzK80Y20HBzb94tAfHnvwJPHpOsmEh6co7BS3CFfEwa47M-J9NManNuqRJ2Yoc4GJ4NbYVtGBeiifIvokamy9dgaWfCMwQS9IeX16IMnIuJtV7hkCIUqhxBy60ROer2BW7yuRFATLr30wdDnUvUMZ7JQv1rJ77NkFCJxEkiz-BpvNY2VmvpuD2UPtMwXQvmBN5fXsH62RvMkdp1Xg9lwT5q-V28BOAHG5M-5znF83QSvWWf_iVL4NEgL09vyBFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
باشگاه گل‌گهر سیرجان: مدیران باشگاه پرسپولیس مدعی‌شده‌بودند که این تیم یک ماه کامل برای تورنمنت آسیایی‌تمرین کرده و این تورنمنت باید حتما برگزارشود امادیدید که تیم چادرملو در تنها دو جلسه تمرین این‌تیم رو تهران باتمام ستاره هاش برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24629" target="_blank">📅 22:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24628">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=STtO8qA9kJ7GI8F7T-uBEx204hVTHAwyAoX03DmB0HqtsETPPgHpEM5-lFobHfClA5hR_40L3F5KH5SGkrITOqhes7AINEeBj-AblXAmS0Mre_PFLJ3ENz0HYwjb3btoaX2SK1HDmfvdtP5ISgHkKJ9Re1JEJVj9kSYKAcf80voQqtB9GgYF1mss_A81m4AU7lSYWdm6K55Lb5lRK_36tIJT6az7RnnEJh5f3kpRehBLIwfUOMnHYK4Xoj--HMJVWG-5WoDnWWRmQqbeKS1HyOvU6xGGgCtQek5w9BTk0cjSP9SWh5ludmoCebiREoENWNp2C_gfAprM5pg-91Kq1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=STtO8qA9kJ7GI8F7T-uBEx204hVTHAwyAoX03DmB0HqtsETPPgHpEM5-lFobHfClA5hR_40L3F5KH5SGkrITOqhes7AINEeBj-AblXAmS0Mre_PFLJ3ENz0HYwjb3btoaX2SK1HDmfvdtP5ISgHkKJ9Re1JEJVj9kSYKAcf80voQqtB9GgYF1mss_A81m4AU7lSYWdm6K55Lb5lRK_36tIJT6az7RnnEJh5f3kpRehBLIwfUOMnHYK4Xoj--HMJVWG-5WoDnWWRmQqbeKS1HyOvU6xGGgCtQek5w9BTk0cjSP9SWh5ludmoCebiREoENWNp2C_gfAprM5pg-91Kq1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های ابوطالب حسینی درباره خوشحالی بعد از گل شجاع خلیل زاده در بازی برابر مصر‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24628" target="_blank">📅 22:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24626">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863d336b56.mp4?token=bq3K7mGH6cMCvZ3hyaJqciyy2qwBB2fsSN-VUexWrHxUw5WmPPlw4wFrjJiP2evdwT-5DNNlhoIWDl3ZfuWfp9gYAht0Po_RXbNZji16uB-W9dV8JJPR7_Tgo8VnPzeiRQCgKbKAk_X27Ms0ZlXkHsY9N3o28er9ZmKujffnik9xonX5pZ24boTbfsf0dLuF83kgxUSh8X4KM0PMVWLZAQdtn-cJbmrBkQupkSom3Rc6egZdaXbA41Ra4FP9_CwMOgUjb51RCumjoFoeyWgPe-kpb2T9lCX_zV-Ek_nZpGIYStUCBXZS1pT7sr3YWWrEh7lD5hK7CWGYeqNi9_dTe0oBBofg7ZLAO0lVpVVyO5j7iQhsGq79sG7eK0i6mSAQSsBQep1EmFJjRQevAweq0-U2gQ94mnsrBiTR_Omrw7XjaMoEGp9bGhwit2sFgz9P9dePgMn-VKrpc78DNdYnZZg0p-deO5LiK9fgZ7-5T9CoJxKGBqP0Tn5XUvgVgaj3-4HSN-kREksvPz_IedIRCjS3vhVoelJ4SLoh8CQe615oREjHOL7iK8QJrGdOdLbgRV1GZb_NH_Vrq6C8x7SWjU3hjjSsSUTZTCREtixTTGvEiJ987cj4oAksjo7xLxSfD28GGGMnddfVG7OMGkZvhtNjsk7VAiF3NbI_EXPLpVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863d336b56.mp4?token=bq3K7mGH6cMCvZ3hyaJqciyy2qwBB2fsSN-VUexWrHxUw5WmPPlw4wFrjJiP2evdwT-5DNNlhoIWDl3ZfuWfp9gYAht0Po_RXbNZji16uB-W9dV8JJPR7_Tgo8VnPzeiRQCgKbKAk_X27Ms0ZlXkHsY9N3o28er9ZmKujffnik9xonX5pZ24boTbfsf0dLuF83kgxUSh8X4KM0PMVWLZAQdtn-cJbmrBkQupkSom3Rc6egZdaXbA41Ra4FP9_CwMOgUjb51RCumjoFoeyWgPe-kpb2T9lCX_zV-Ek_nZpGIYStUCBXZS1pT7sr3YWWrEh7lD5hK7CWGYeqNi9_dTe0oBBofg7ZLAO0lVpVVyO5j7iQhsGq79sG7eK0i6mSAQSsBQep1EmFJjRQevAweq0-U2gQ94mnsrBiTR_Omrw7XjaMoEGp9bGhwit2sFgz9P9dePgMn-VKrpc78DNdYnZZg0p-deO5LiK9fgZ7-5T9CoJxKGBqP0Tn5XUvgVgaj3-4HSN-kREksvPz_IedIRCjS3vhVoelJ4SLoh8CQe615oREjHOL7iK8QJrGdOdLbgRV1GZb_NH_Vrq6C8x7SWjU3hjjSsSUTZTCREtixTTGvEiJ987cj4oAksjo7xLxSfD28GGGMnddfVG7OMGkZvhtNjsk7VAiF3NbI_EXPLpVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خطای شدید روی وینیسیوس در بازی امشب با ژاپن؛کارت‌قرمزنداشت؟ داور به کارت زرد اکتفا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24626" target="_blank">📅 21:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24625">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8A5E75KdTy_NAA5GPYx4mo7IlcPz-9PvboPem23rXXiRIvEpgFx7Op3hjmgDbhaE38otYoIFDjIEAr3mIIUfFP0fuq57ZtdkbOLheDi4PumrsHb4UNjRcEipCM7YnE4QtegIBQfJZ8lmcax3WiTEEP_xyym_hlH_HUmmnDTb9ii208wP7AkANy-UqJr-kcRpFHHTlOaERzg8SHikRJDao5f7C1HDVNVY8JNaRwmbiutWAT9hN1C7_56eTXeIlLv_C6aMBOHFGWmqhyY35mEpywUtIGMz4jvA3f1UoxKhzg4YbNf7ZhGbFEKe8k-Hq47zs-yvD-0vWb9K5XchRktGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک شانزدهم نهایی جام جهانی؛ شماتیک ترکیب دو تیم برزیل
🆚
ژاپن؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24625" target="_blank">📅 21:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24624">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7056183539.mp4?token=XJrXqclN13soqQT_0fo0ApG9TO_VPwjcO_Ky4A0Uf_8psrIMhsuzxuJRV_uDY5vSgHsIFSm7wXMU9-HQLtl_d9Qa6_f3p6867eSJ7RgPe_hNZ-KyN5VAIkXM_yYhT0gE-rgoPrYSKWKLxxJgL3bK48BzcpxJaSLjGwi6y6m40GvOBkwu60U8GMzQmYo5eC53HFIAITAsaT00Hu51GXMk8DZQPxAS3jEK_a262jj0-wrn5lWYlgeYVMy8dv-qX-4vxCfnSbT2PcV7N43WJQHnh9ycUJILvSRmD4W21BE1n-Mut3trKupiSyjG_FKcRBrFi8nyL1fyTcPPLpC5a8VD5avR-OXLirvxz8ndwv75k0ZBqxMjS87A651YlMM-UCKbOu70zLpF2lWoYhysQhVLwnLjJcZviJke7yjYO6R-HO0vlpOBAS-DDWKPhejZUjuEK6nZi6PFT7MKWlRMlQEO0Q41D5hrozWLAU1kcO-wWpriyeC2BM0BP9GEjCOFwpldHx6JNfth4FsJCZ6w9ao7Zq0Ep_TnOVir-YBDJ5dDS2U0CLVoY2H_IfZp5BNN8okd66E0hm0hs3TARmt1qhTH0t_TEoCivLttJpDlWh-NjidSCWsSNkLfIHEhVfUqfK4-d4hCi5PjpUGgRDL_rtXLj9AE0LTIr7g0IFaatv36-54" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7056183539.mp4?token=XJrXqclN13soqQT_0fo0ApG9TO_VPwjcO_Ky4A0Uf_8psrIMhsuzxuJRV_uDY5vSgHsIFSm7wXMU9-HQLtl_d9Qa6_f3p6867eSJ7RgPe_hNZ-KyN5VAIkXM_yYhT0gE-rgoPrYSKWKLxxJgL3bK48BzcpxJaSLjGwi6y6m40GvOBkwu60U8GMzQmYo5eC53HFIAITAsaT00Hu51GXMk8DZQPxAS3jEK_a262jj0-wrn5lWYlgeYVMy8dv-qX-4vxCfnSbT2PcV7N43WJQHnh9ycUJILvSRmD4W21BE1n-Mut3trKupiSyjG_FKcRBrFi8nyL1fyTcPPLpC5a8VD5avR-OXLirvxz8ndwv75k0ZBqxMjS87A651YlMM-UCKbOu70zLpF2lWoYhysQhVLwnLjJcZviJke7yjYO6R-HO0vlpOBAS-DDWKPhejZUjuEK6nZi6PFT7MKWlRMlQEO0Q41D5hrozWLAU1kcO-wWpriyeC2BM0BP9GEjCOFwpldHx6JNfth4FsJCZ6w9ao7Zq0Ep_TnOVir-YBDJ5dDS2U0CLVoY2H_IfZp5BNN8okd66E0hm0hs3TARmt1qhTH0t_TEoCivLttJpDlWh-NjidSCWsSNkLfIHEhVfUqfK4-d4hCi5PjpUGgRDL_rtXLj9AE0LTIr7g0IFaatv36-54" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب حمیدمحمدی درباره شبه علم، خرافه و فوتبال در ویژه برنامه جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24624" target="_blank">📅 20:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24623">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufmRqLNLDeJlqFYpsADBdn0_RezOR3lGimo9wXNDPgTvIvbamzXAlVb20lR0wEEcXRhhpLBgSj_H1NdJKhcW78qfZLOPIVsPhfqGU6GKaHUafNichqXhF2V-wvUkuQC1n-wLsyxNYTDUAB2kIhMszaOdsEnyW3WPPmEDimz9k4pIcdwybLN-IQ6wO2N9Izt6L99Ej-MUq1sD1fRfEDqaDGnD6jVzNqAgzIlRSK0mLYEzSCIzyOwp_-jBmk_f4V8Bi9Iatg8Mbd276u3_TR4rm6p_FEP5kqd-6y88IHgjx0Cq1Xkn1u8puf4mTM4hvnJJmtchcHo_02Ehp4KZXUr8BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
طبق‌شنیده‌های‌پرشیانا؛
جواد نکونام در جلسه با مدیران‌ایرانخودرو برای‌پذیرفتن‌سکان هدایت باشگاه پیکان برای یک فصل حضور در این تیم خواستار 55 میلیارد تومان شده. درصورتی که پیکانی‌ ها موافقت کنند نکونام قرارداد خود را با این تیم امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24623" target="_blank">📅 20:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24622">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmSRFaKSRNz3TsWZ2HEO3qH6ZDhrCrdLFTVilXHYSCWDy9mARSSsY9_4QRLUrTy_UHVWdKSvC8ETOFYZ_2Ey8hdGYIfr9MG5CSz53EBJHo62sMHuNzPD8GKKoa_lCP2j_UuO2ze2yeX9xQrIGwBTJBnT2t9gUD2c9__NPQ5BO8AA8UH6JCWtgZt-9gHzI6GEfIeyfpLcFVLLgKZRcrw5YJ58wMsRCgFrwXG7sp4z2oZdKHcLYi01xgMykx_MKnpgvxlE89Co8_EhFnHiq7co1MwSzg9Rqd3PnyoPMiiAETS6wUggGBS5uMgdyGtqAZdzAoiXXj-rnUoLvzY8QJjR-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سیدمهدی رحمتی بعد از عدم توافق با مدیران ذوب آهن؛ با صنعت نفت آبادان مذاکرات مثبتی داشته و احتمال اینکه به‌زودی هدایت این‌باشگاه رو برعهده بگیره زیاده. تیم صنعت نفت در آستانه بازگشت به لیگ برتر ایران قرار داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24622" target="_blank">📅 19:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24620">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZFn6PvIKjH6YZQ6HLPS01OmOjxx0vr56v16UFNp9F2wpVauMqh9ekAZ3fN1yUWCxiLqrH2gvmlrsbi6bfKe-Ukyjm98hOrNT90GDcI9DgOUcW1i8zymZwYGQwvyKn3VX5ea4o_uscI5T2t0xSgsPkwTLuBmq907FNbQ0Bd4eAeYJ8AmxKGNPRCACVCZkyc44YU9TaTb6-7vvnfFvHrzuD8YjflW2lg6lZlFxQYanzbbFpc-hjpy9lOzcNG8ZVRoPhfeNFNgeX9z8RKCevtg4QiZtTeKPXXE6JPCrsnux0loXrHd7zlhieaUhogqkjTxie_m0ZfBmnOVpUQoKiMy9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/givv9g2lmwSCgvhOJveNTQeS8tsFKkGcmWj6BBsqnCYZsDIv_sfw7AiY1knUrW5ZyDgUAHrIP6bEK9p2uoBsEGqSOxOvinJlqpvXpFBc0jopYou2MaKm072UKgDIBRNrojBtycFuMVb_iJqxQbbqv4pzPqg_31fe8SrTEs3B3h0dGQjlc9pKkSUtpIylM9Uja6HIZYuiNGCNasm-GUPkAi9AhaPJPNFjowVSbSJtbA8qvPDRZNVIa-UOpSWjwzpsvMJP7STjjxb4iTCMS0PDWLMoq4o7Jaom0Jp_526jaV1ElXE4JEwkRabyyIroexDAqlbjJDlDH2TzYgUi70JYGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
از تلویزیون تا زمین فوتبال؛ بالاخره اتفاق افتاد؛ تقابل جذاب ژاپن
🆚
برزیل؛ امشب ساعت 20:30
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24620" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24619">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQ6sgMqG4FCjjw0QEtylPseHHICwGhLs5sTnFYJ_70iNqy5dTbHdQaD3eWXowIjFMpCBXS72KLV0PBM74EHT1gphC9nk1cCdFjx4aJi6iQRlDGKPdsHevyA3GsEYUTkZ0JKC1Ok36NBEUQEJSce7vPEyPYZ5zRejyMUeQilIlfB8VmSoklveKWTht7BgfKmZ5UJQY7C2uy3k0ye0jd6t9f57e8VEwK0kT-tL9ehP16JX6-tfU9HM1188BSVqnsbcpNFHLD9yym4zlaeD0LQycZRFWzm248ZZ0IIeyM5_xLYwxIE28M5mApU0KOnSTp2yJ6gsqXfrR0zDo51CQ1JP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شانس قهرمانی تیم‌ها درجام جهانی ۲۰۲۶ از نگاه بازار پیش‌بینی؛ فرانسه با شانس ۲۳ درصدی در صدر قرار دارد. پس از آن آرژانتین با ۲۰ درصد و اسپانیا با ۱۱ درصد در رتبه‌های بعدی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24619" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24617">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5MtM3bfRJwtNK5uxkVlkuCWSoYzxlGojjknEUHCYkARpBibcf3Uwh15I0s6Moap3tQKz4jWhb8CanOH7Pa4JZtkT1kTr81OlrDUNslyL3ppxl6h6MVUOCIszkCP0FdK9ULZEQ0_laqqZtjqYgWk9N5uBzZ1iN3Xe-xi_7ukBYMVyOmVWeRU5CO4LhYSgNTlKc7S58EuOaj1fsre9PRwfxVLfU3QZbDu9JnkOUMGYwjtNkasiE81m6IxmO7fVfPQW8u1U68JnTil-12C4tCWH2R5J7U6T5yr9voktv7nkU6FT273BTxjISCS75auycbjGn8ZKeZEBD09xZaKN1aH4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24617" target="_blank">📅 19:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24616">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3unXK_-xOVfiqr01xHg12u_HfWxXr11oSOFm5ZCMmH_XWSHFkDSK8cV_lJb4fWnJvn3cw5ffc3T0VbmnyvJWUt2catdsovOnrcteWWgLcg7nW_J6nHGCbXQ6GkImkLz1DAL1E5e7OCcc9jBlwic7wvVwl16oz0V272zig3ZBsitQY7vtHbInMUeO-ZINgqaLm37ngHuYQK74jwsFNR8AfaYkjCdKtV-egHUxg_-YjgNlI4Hz8l8r8B9rZnQ1HUkybq62qkyv5df7R0VHnmoK4IBaIUzVxVN-gbf_YMQLSc_LTkoVtUNQ3tU8Cml6TVbaMAlSxwNdKOt1NmKy-HCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24616" target="_blank">📅 18:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24615">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ08R7hUtlSjbzd0WEGjHClsEo5wySHDXEc_rzNzsqWAXdFz3nUQscS9uDMhOlhOY7TTtm5A8rXg_uKoZSv0nu0kLPGfmPdHFkZozsuaQeXlcDBtHmLDycL4GFO5-QROf5eoOOLfuA3WNp0rB2XFfTqsDhgd6tzf7RWO456TVjjSo7nXKSsHMNXXeQs6uAkzKM3GiiKoAUpNWPVxjrTYeVIA3y3qTLe0cmATsYkI5831dLmqU-VXSmpWHUVmljq2ovq-7D4chmbikp5DKdW-YMsXguWPKSdfGpN_ueGv-NZ_BT_k1_BS8gpRMTTXI1IMIEwd9HP68MCfH4FEmrC7zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24615" target="_blank">📅 18:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24614">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1ecOWSbOcQ6kXIjndACDuuOifidFZtagJNBmb_6scZflJRy5o9uYTqxWA5KXBIZ0vMz4pVTqHHm2FDlKJmIDWd7ArFvYRKIH5Bn0-e-zvpGJaUNlU-nLfETpHQMywK1nm0mq0yi_mGnyetLuG3kfBx6K3XeOsXZuCcBp5aJTd02w8LrryK4SaLX9dO_OleX3QOn6DhhRH-t5z7kX8xjefZjK_t2E0gctL1p0sPI0icVIwR2XnocZkwNyquNmevRvmVkJqDd3xDHaPPMUUPBG_GfD5Us0FbvDHT9FXSpKUEbX30KTiKSw0AB9dpCgqaVHdxXnC_Ckq_8HHfaDgkjJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه مارکا: مایکل اولیسه بله ضمنی رو برای پیوستن به رئال مادرید به مدیران این باشگاه گفته و اعلام‌کرده‌درصورت کردن رضایت سران بایرن مونیخ اماده عقد قرارداد با کهکشانی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24614" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24612">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkoINk6vpaP27D7pGVDn-PpIyAONfd9lb_1tT_zk7d-DBfraoJLuxPsHQsIiwWe3SOh1uLPlwzn0C6LC-hAlADxDDNkYywrrlNalspXctjaIHM-SGQ7vEvzwwWwetlweDXuQOaUAbR2qwTSl1QMKekSDlJSfyLsVBBMGdf8hwu6bnwIhYBUeeHREsIMEOatKWwuVN-tjR_M89jDEahflHc0GryhUkaZlejzqSq7SLqLq5iZFt2c3-j4NlNR4TceKQcOAd7hbeqa8HOaesmGHpSt-QI15Q77LrWOsTliiw4jbhU4hgwoOYRVvqApgFGu2WLJEeaR0x-7pFdOar7CCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
محمدمحبی امروز به‌ایجنت‌ خود گفته تا دو هفته‌آینده‌افری دریافت نکرده به استقلال برمیگرده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24612" target="_blank">📅 16:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24611">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9BcLJDYjDEieQCSTxXMquzIDqkYtckUrxar7W173a42EykiWxHARE_qrATRyE0abowfh7Z4XINWJRi-V8KoLDBp5RH8ynjrOLmZ9BNbeHqMweMXZNV3ge02rXlG4NoO3MrRtzeailSAgyF_9OnFsYFYp-kSvJ6k8I4SwuaAIqk4QSlJq81EhKSCDDnKqSDdIYAibtiW8Z6-zWaMVvQvtlFB4-WtTKsqMo0pAr4Y1GMiBQO9S3UOb1OluoOUKmJOVTJ3OVn7ixcdywynBOPGooQAJa9CuGI6zXQvQWdqqPSwzRCjMwFF6QHct0GVW0suAAFbjazh8Wq6MW07ESZEdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریتزیو رومانو: انزو مارسکا با قراردادی 3 ساله به عنوان سرمربی جدید منچستر سیتی انتخاب شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24611" target="_blank">📅 16:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24610">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZEfYCsk8LsMO8y-6_icBv_I241EiMpFHOTNP3C8xih7YC493FHve5lmdAQVlwGbjfJiJote4KQET-j3gxwA70-wT70OtQEK_Kq5Yb6wWblT6iFjNQsFnoa7r9wTHL12UL4Bh-GCyZe6nGgE7qa9oH6usT-cbGM7YvFsr-8jUNtvWH2NlLaCE9s_LjsXpGF21TH8_yogknH40ZePlHKJGLkk69iqlJrBN4vtIP9CHuaBTiw2cKLywg2ELRdaoe0C45x4VYf1VsAfiPVJ65wSFpc6_VvN99tJv82NuNyeLYPjb5KnbtSnm47fB6v9mz89PKkODHzPzVsM_7YrmuvGRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
باشگاه رئال مادرید رقم فروش ادر کاماوینگا هافبک فرانسوی خود را اعلام کرد: 60 میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24610" target="_blank">📅 16:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24609">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=bKoFjovZXq3xCkAcCi7Dz1DLlbNUfb3lWQjjnKafz1l0Ytbts2PZSSRPuh40i8wv4UbJHYQoju0J_q6SOWLMS1kEvaa3d-y_F3hibrWEQ6EPvAqYQ9ksscsftEXPUWQpKn9DOhsZ8qEgBm1_IwtCTFsKekLyJL37Txd6qgEk4CI77NsrvdSHx5_voITUk_1SL04t0u8whmc5f0A4vC75kGGzj1uLQzGsL3l8HQB_po155rCbWCd1-fb_mk67886tkElreALopWohQ5JAGrguhqE5MzPPVxTLakm1MZyLSmZitSjDrSdjyxP9xoNuIoCSEF6YJqCqZ0BOFxgi1ufdlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=bKoFjovZXq3xCkAcCi7Dz1DLlbNUfb3lWQjjnKafz1l0Ytbts2PZSSRPuh40i8wv4UbJHYQoju0J_q6SOWLMS1kEvaa3d-y_F3hibrWEQ6EPvAqYQ9ksscsftEXPUWQpKn9DOhsZ8qEgBm1_IwtCTFsKekLyJL37Txd6qgEk4CI77NsrvdSHx5_voITUk_1SL04t0u8whmc5f0A4vC75kGGzj1uLQzGsL3l8HQB_po155rCbWCd1-fb_mk67886tkElreALopWohQ5JAGrguhqE5MzPPVxTLakm1MZyLSmZitSjDrSdjyxP9xoNuIoCSEF6YJqCqZ0BOFxgi1ufdlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آهنگی‌که وقتی شاگردان قلعه نویی بعد حذف از جام‌جهانی به ایران برگشتن باید براشون بخونند:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24609" target="_blank">📅 15:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24608">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rboPCV4pJQzBwGKVxeoxddq59hwc9hQgimjYbZM4i5jVdohgz1FzJEfRZifalEBEqHq-KJcOYHi5gEFA9pEnZWB4vC_y7Rs5Mpfq5uvk-7g75BETLGGc7iQ1nGNM0XzrJbT8znL7tmWzazO3nzydQF5gjet61V6y1nZ_B-m2SXs5FgCWgHxSOt5SapRTgNKTxjmPDtmClHkhNY2LC2k-vR8Hb-ZglJw88w8mWKvb86yucd8jOFgPVsyRIyxGpJlFUZLz8Zw6mUpHaCETYjhfI8BhR3ilfx7v1z50kV2h1ORvZiHRPepUtTRfBbPItMBU-_JvPoVWtX-FOrrVoAYOjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24608" target="_blank">📅 15:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24606">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FujRct46l1ZHAIW5_yIY_TkN2_vUIZVW9QCz6bz2dp3iwRSCETzn999vmQA0zQa1MiyO7FBz3WvO9qE88V3tSikWIMD4GWsE1Th0pUjJ0YSUaC7L63Z4VFyEYRAEnK0zo5AzVFCNv9CxRMfcJ5_kwQb7Tswx-CUSm_yTHIF6O4zn-sWhscAtpzbubWRGAw_oGCpEywPaTfeawpyOvUb5RekNY3a49pSCxrVEulzQmHqbKAxuiW1dmxmmV-Ur1RKoRLYJN3XoAnV5T5bRb3DHzyEZAVd6POIIfDRJeVLjRgLdg4xBWiYz0Cq7RTjGraflurBqLDCjvK-rnqizctYeyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDy68uEHHcVXYPSKLAI7x3Kf30VMAqn4zLV8mwr7-xH5peP_VhUuJvS70nacwf8yfnOdewPo63ZpMqv4FgA83vfxqJ8BUFWmUOvTR66TKEROWHbtNYETEwKEvne79pyZf3WkCGGHDBey0qwuCnrLq5ae5WEETvCXe7OHXnxuNoLLYuyUMJpPVE0cAQclY_VxIhY95Yz3RAbsEGbQVocffcjVd2GLNbmX7RUBj3hyKmLHYBOpyqGvve6lUntZvdi6QaPelAhWaQqFRoywB3Jn6lUh-7czd3QxO-S7mfhpFZniR54bEe5b94maHnBdg2AUl0Vlk46gqvEpdMDLhcouqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور کاپیتان دوم تیم ملی برزیل: وینیسیوس فوق‌ستاره جام جهانیه و مطمئن هستم که میتونه ما رو به قهرمانی این رقابت‌ها برسونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24606" target="_blank">📅 14:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24605">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJKC3N-wE5_8Hm8d_eFBlN3fK6oKZdaKTGsUiQon1fkAzb2Qe9BuWwtBbmQGKUb-rsbWKoS4C2zsP3PD6P6vItwvkZD2XKnKXvCayrG2s2dTaqsPWlItVZ82Jn9VGJGtY0EXgPahcxxhWcI2cdUSJKlDGw5TZK45T3CChr8o1EUvI8zhnrAtaxXiQ_5XKZhqGQDiFCZosF1kyCekbpPqCgfJPfYpkozP6tW6AReuC1OA0l8704cuUxC04R1R4ZGeIlURoFuDYD0re4vt-Lp1NaYVP-s23GijalqWAT--tmpJ9o97pHn1stW-g4J_sIvMD7DNmBNLhOpYtAgFgI02UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این بلاگر و هوادار تیم ملی اردن در پیجش افشا کرده یکی از بازیکنان متاهل تیم ملی آرژانتین بهش پیشنهاد دوستی و رابطه داده که او رو بلاک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24605" target="_blank">📅 14:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24604">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvlN6ZFNB79wG60-gMLrY1hXAOvAbjMkOtQXvS2JYmk8GUJu-XrL4xOLHuA1XKGmJL0wzVZS08JBu57RYWalk1AsjHY7QxYS7n8pwwuiMIgyZcTSKfQT5ofv7thIL9NEtMEMfKuVWFiAPo-q5DhTWZ8BHh17e8TK8nT2TSSIWidKFfzY8ID7YS9hS58k_nN5Ijqy-Me0JtT35YRVWqU65RIDYy1_3PoRevEhVLhCcsJlezht2gAQdP4r7rJ66KWSi0XQRDVJEv-wd-z31HUqrAEJdGIWLwBXvoscRJqzyBs3BGHH5WcWSTA5kzCt1L9wsUJY30OrrPzB5_1YOZ603A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
مسی باگلش‌‌به اردن حالا ۷۲ گل با کاشته به ثبت رسونده، همون‌تعدادی‌که جونینیو افسانه‌ای داره. لئو به۷ کاشته دیگه نیاز داره تا این رکورد رو هم بشکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24604" target="_blank">📅 14:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24603">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uT6cy6YqUQyV_y1N4KBLZkQCm78tP9gAPNemVZh6URosM18vf0tQOclLUb7C-HPGkJ7_GQw6gq2TU5zhd_uxE8skrUzGHP81O8cVR_VWkzM7qFoOAOV_tZecCMYabT7mxHVyexTVknGz5s_LOMKC_6Iq42sI1SRJqfa9set8Gng7pzUFjzqCH7UenoChMHH-psd5eJ_0oHWy5wCT1NpqZTglPuJbXTWt4K2_GRlm87VJaeTfE4vjG1kMI7BAN0uPl_ycWjYe3GZn3TuYl77ds7tQ-lgAHvIzbwANh7OKm6g0cb2GqxV7jcRTQbM4EGmm-zODUlopDWeZFwq3cGHcvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24603" target="_blank">📅 13:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24602">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=H19150G2xhEy-R_r69fOb5_zyDq6OmlDIvoQCKAQx1KR6kO320L-sTyUk1gk0pfCKh8Y8_-ecsX6DRQPtMQ6zIZa50lldPgx9oBHDo-wV2hieblfId4SigL5jedrPo4wvCXvO6U1YVh7keIpGmElfxnE5ZdiJiOwU1SMxHjEzIV8JvUoH3cuN4da_jScLDA41eTSG7JLeYNdmj1eJU2OucHozQ_8i7TNtGSW-BVqsgTBHv0JvLIk6b4E4xw-irteQ_eBPQ0t1p4YsAMNHTiKIFN7NqBad1b4ptwFhV30oS_4wrAvURAZRrWmmBRxtLjlmC2lzJY2UEBjquCXeDV_ab16Za11TPTs0dyvODxQy_3xPdr8q9cvv5TnGEXMthQZF6RdGP1ybnDyXZvnxG1LZpPVleGDUK9VGSHu8D6pYPcl2brGopwXscdhlEwId2bAmLPNomQQYO4UfdfD8LTT0I7N0jM5zOnMlDlqePzYCcNXWyjLQVO9IejLsQ_qdyr_qEXgmFai6l23kvvFvGzBqJ_DY2nZKjUg4_OFmIiLetKJFDddHlcJUOBOb7Dd6Ga4xpdSavVAhdLMnnFsQDaypfjfT17TTSlAVt2nuLwyC9S0V9WxQEM7IJ6uhA4mfxsmAt8sCWgjI4JC6TreUvFUZaVjaOAh9m-R65qB-LJGx4M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=H19150G2xhEy-R_r69fOb5_zyDq6OmlDIvoQCKAQx1KR6kO320L-sTyUk1gk0pfCKh8Y8_-ecsX6DRQPtMQ6zIZa50lldPgx9oBHDo-wV2hieblfId4SigL5jedrPo4wvCXvO6U1YVh7keIpGmElfxnE5ZdiJiOwU1SMxHjEzIV8JvUoH3cuN4da_jScLDA41eTSG7JLeYNdmj1eJU2OucHozQ_8i7TNtGSW-BVqsgTBHv0JvLIk6b4E4xw-irteQ_eBPQ0t1p4YsAMNHTiKIFN7NqBad1b4ptwFhV30oS_4wrAvURAZRrWmmBRxtLjlmC2lzJY2UEBjquCXeDV_ab16Za11TPTs0dyvODxQy_3xPdr8q9cvv5TnGEXMthQZF6RdGP1ybnDyXZvnxG1LZpPVleGDUK9VGSHu8D6pYPcl2brGopwXscdhlEwId2bAmLPNomQQYO4UfdfD8LTT0I7N0jM5zOnMlDlqePzYCcNXWyjLQVO9IejLsQ_qdyr_qEXgmFai6l23kvvFvGzBqJ_DY2nZKjUg4_OFmIiLetKJFDddHlcJUOBOb7Dd6Ga4xpdSavVAhdLMnnFsQDaypfjfT17TTSlAVt2nuLwyC9S0V9WxQEM7IJ6uhA4mfxsmAt8sCWgjI4JC6TreUvFUZaVjaOAh9m-R65qB-LJGx4M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24602" target="_blank">📅 13:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24601">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsHl_4OX5ZkMMc67RMbX3C-normxOh8cHulCM6VZ74p7_ioqSeDoIEhfBIN9ptVlE7JMHMEohksK2GRihURApuJQzqDZYiw510VBbUtiQVAY0DMytgrUaR07iBbOU0FuKuXJjvSWPMXeJcm8PV-gnxMo2-odDRTUnEWfh-UUnzeoq4tfcgrVGgWBQSldgGEyaPbqiMntV4mW0GW69Dm7fQRJY5rwArnGWPqnlQC89Z2S_31MgeagkeDiG1fW22tgpp7TpRBepeEpZsiPgI9Butdxlo2h2sA1qRGMTY3t6anbdpHWrcCcu2BHR99-_hv0cZjb91oi9JcxmtWTQ9pW4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24601" target="_blank">📅 13:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24600">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=AvYJtyD37DOMH9gXTPsOn8U4YDW9PT3aZ2YCzJpYEXhn9m65B0XZOVoa4-kg-_2143kkKl1Ca9PXqZi92Z4JsNUOyBeKliyDjBfgqhpQGumSyYJNUWanWRuxtrzajCL_FP1m1o__rDThQEzbEXn8QjltyvJjkFWzQq22a96GhB17nHfeNXDxTKGH6VXAwaFo-wXzIH5B8rNxtVTI033tuD8tgevHVQWjsf-WGtawDDQqzp6vLwkZRn1HxmNs4Vr7KF06hMv9YWTOnuilPdIeR2dMrJxpO9Qc5va2Uu5V_h6IaUpGQHhUf0aRHqLOuEmIsm-gVfLDSrsAYPfZuVdCaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=AvYJtyD37DOMH9gXTPsOn8U4YDW9PT3aZ2YCzJpYEXhn9m65B0XZOVoa4-kg-_2143kkKl1Ca9PXqZi92Z4JsNUOyBeKliyDjBfgqhpQGumSyYJNUWanWRuxtrzajCL_FP1m1o__rDThQEzbEXn8QjltyvJjkFWzQq22a96GhB17nHfeNXDxTKGH6VXAwaFo-wXzIH5B8rNxtVTI033tuD8tgevHVQWjsf-WGtawDDQqzp6vLwkZRn1HxmNs4Vr7KF06hMv9YWTOnuilPdIeR2dMrJxpO9Qc5va2Uu5V_h6IaUpGQHhUf0aRHqLOuEmIsm-gVfLDSrsAYPfZuVdCaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌مناسبت‌دیدارحساس امشب؛
24 سال پیش، فوتبالیست‌ها رؤیایی را به‌تصویرکشید که میلیون‌ها نفر باآن‌بزرگ‌شدند؛ نبرد دو تیم ژاپن و برزیل، جایی که هیچ چیزی غیرممکن نبود. «رویای ژاپنی» فقط یک مسابقه نبود؛ یادآوری این بود که با باور، حتی بزرگ‌ترین غول‌های فوتبال هم شکست‌دادنی‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24600" target="_blank">📅 12:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24599">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLXqcPD-RIJKGeMQTtqst2v6WnL4HbwNOef7h1-hMn1PlqojuErhzxEZ5mQPNNlA-RLUYFj3rMp5I6ahDw_tERfPPGVhy1AehLMidep2ZISaej1cSLjj-i1zOFPmOdvPM6weKbUX7E7n5G4AwWAJFeQJbLhn2qkSYwRBR5Da1DvmsoPHE6MIqPyfC2cqhxEF16iE6mtGwkYKIlZQpmTLHKFagCaqs43iGQ5dqL2tSNc52OAya6lxK0ARnU0idEAur9egIQ-O1UQtFpDrIG62L3GWDD4PeSpGYBM5voHocW93wbxYfGE3MTPIhScBmRwuTLfsmzDgY9K8sApVowY1EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه‌فلیکس‌دیاز:فلورنتینو پرز رئیس باشگاه رئال مادرید بعداز فروش نیکو پاز به کومو با رقم 60 میلیون یورو به‌اوقول‌داده در تابستان‌سال‌بعداو رو به رئال مادرید برگردونه تا برای کهکشانی ها بازی کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24599" target="_blank">📅 12:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24598">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjQF1j4zxn8CE9T-JYons9OoKJvBi_OVlTSK_ksVfM03r_Tu_tfn_O1ND8o601K_kFRzV60pyvn7W4DOVlDZ1mpRGEBQGp9AL9oklJfiVaIqa4fuxVK1J7NQ-fRJQjjZ3LLw9GCNCvaicR8Hy7RLMaA7DPaUYIAcYk__TagmJ4merNVDgU4bLQ3JRnOJ1SmxRofXzueu6fDPYV_qkz52yYL3l6pxYDn6ndQG3hcd5mbnhwcvMO4L39moKHV-ORTOGpuIE2KqzS3pUtQrKNLX05k3sWkJt1duHbBcXoBLZ3GO9bSATkkA-xsvvnmJfrQd6KOHHLx0WZIDL4hjplStvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جالبه‌بدونید؛
پدرو همچنان‌تنهابازیکن تاریخه که لیگ قهرمانان اروپا، لیگ اروپا، سوپرجام اروپا، جام باشگاه‌های جهان، یورو و جام جهانی را فتح کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24598" target="_blank">📅 12:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24597">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLFv2IWMvV5VeIa_4ZjrTjjgY0u_lyAqsNgQgO3AjeeedqwYdjGphEO4HD96goe8jb4iRLVkZNoMCpFG3mHLbrWdVmxh4v9LEgT7nBw2LJ9w6PDaqG6eWaqgQBE8xmzXMy-24aG5x48UJ8ZEG0PODprr8ujEsz7aHVGFTHHrcHjdvjujkOt6vCuSLt3yWyOj-WpYPNRl3m_475cwie2y8ry_nS_p0Pe9OhMs-sdgKQqfUrK0WiesAstxx4nMrDLiKqSsqKHl_mQBLZcXwditPwgq82H3Hi7C9wa2SUKB715RzDUywx_XSkflh-pHV_0d_z8wRfbmZ6KNvE1ojONKlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا
#فوری
؛
طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24597" target="_blank">📅 11:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24595">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGeyrwRClgCp__fEtipZJGCvLBmQzwgGI30zFfxJqPHS2MT9gSRKB9PP-X9FBcVo_k0Xa-toDa4HYSTsm-csgcMM0_xKiivAM35SveNhE1-Ks7yAv4osdj-HhXfPOZC0k1M5q-GvjiZuCIXs0ajZWqYbBfF4VRY9KXxdO-h5ABubXV6xq5p7JyV7mf37Bk_S0ND77eGpeLoGf9XYxuxN_g_rKqWOim5rbFFoNgOCcGxNjCr0T5rp3IOwEIFnEmI4L-62XX4JHAaax_oETrXy-kJplK6dv1XT1LZlorrwJiH4elxTkTmSQwEb9NfiAJJ6J-9qh2tMa5o1SbB4ShjerQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛ تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24595" target="_blank">📅 11:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24594">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUb4AKyWL-ZDJSg6HeMuP4duuyNxAb6aTY3ranZstVKp-lnRneC3K-9CXW_93kG3AHkxJqVe2ETSd4SeCUfU1l1xzK5ZO9vIRAo7XumDYLHyJQU_QnTxB86sBsyz6K4i8rUAp_sOT5Ak6Myh_0Cy-_AsqDIaYS6Vk5KLbEt6lKTbzrdEQM5-Y0PcnmbZyj7XuNbdv2-GHVWLQPMLVeyCpgZilnJNL9RUXZx4To73uXtgUKAGrUrTTbFxnyvREFVJixpPkf_5T5UT_BEewoOWDR2vPEJ-ops3-3Ja_3Xjbcn4KSHVqx2e9AKBF7V_1ZMXsyVrEAp7M0xzxZoHbsDWvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه شباب‌الاهلی پاسخ نامه باشگاه استقلال رو در ایمیلی داد: 2 میلیون دلار نقدی پرداخت پرداخت کنید تا ما رضایت نامه رضا غندی پور رو براتون صادر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24594" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24593">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UR381mCXsbg8mwTCyKP3g2q3S9U5jtsQHWUIuRUFtkG8IyT49EYPxv2xhT6iZDbVeKQDIcqDXuNKHvNrdcEtqXROgiTCJUq42tT1eoroSAaVNtdt91gBdQY-kXlGKH6tjkuuMBnJs1kTORqILq9tK3jM_iKUZB6W2FfitVyCE5Z0BPO8HxLYatQs6BDLA8a07Jzqic-FC2H7tdL2OeuLJTBpDd4zHqEhm7x5o6bKzYcyUnzxXF9hLkXgDyDug2FQP22ingeVaozYrnS5_4E98Nelf_xizKGztaLTqMoB2QWddaPMkfFHiilPkotBs8zoxUHIXAr116MOj5ZKZseKcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال در تماس با مدیریت فولاد خوزستان آمادگی‌ خود را برای‌پرداخت‌رضایت نامه یوسف مزرعه وینگر چپ تکنیکی‌این‌تیم اعلام کرده و این بازیکن بزودی با عقد قراردادی چهار ساله به استقلال خواهد پیوست.
🔵
باشگاه‌استقلال پیش‌تر باخود…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24593" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24592">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=pXKhxmMEwnt9U7pNdPeDxt5Ev6_Kt8DMgQZa-DsfMjE7mGoVDbIMyKuqV5466IUPmOdXdP34ECOPuOIZBXR01SIWbqHAhxQxqiX9jTYBStT_lFgQrQE0cvGgTFFtCsvYBJrbsIwLHm1te5Pa0YLNIXmquR-sw2drML--3XTEoODxiG4zTEhurVY90fyW-MAIiuK6_xARIfXvT0cS-z2ygctVcQhu1DMLK9QsB8KUg6cdJHyAly0Y8-2DTXS_dzyZUiz2YgaMi5sVzKJu3qdYEgzN9KG6QiOPSOGBFqw89Vit3MvC7nvUqmsDtzvBBSD-v8aIbNwIgFIF_Lxm5QjRdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=pXKhxmMEwnt9U7pNdPeDxt5Ev6_Kt8DMgQZa-DsfMjE7mGoVDbIMyKuqV5466IUPmOdXdP34ECOPuOIZBXR01SIWbqHAhxQxqiX9jTYBStT_lFgQrQE0cvGgTFFtCsvYBJrbsIwLHm1te5Pa0YLNIXmquR-sw2drML--3XTEoODxiG4zTEhurVY90fyW-MAIiuK6_xARIfXvT0cS-z2ygctVcQhu1DMLK9QsB8KUg6cdJHyAly0Y8-2DTXS_dzyZUiz2YgaMi5sVzKJu3qdYEgzN9KG6QiOPSOGBFqw89Vit3MvC7nvUqmsDtzvBBSD-v8aIbNwIgFIF_Lxm5QjRdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24592" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24590">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtljqD9bdC3sKdG7hYgiR9e-tmSj0IY925eVFhPYHEyYD0fXfguoIzBx75z1EQO5YuRiZWWpiDDPGvdh7m4adAOO1MYyiRUAyDynHEnQ9fOAJ1PbuUvk2EMjgoZqRiL3MEPoI2Pe80TjDnqPpKr79iXpRuvUNhDyP2lbSE-8dkqSGyYcxmTc3VLnxsxXPN7ZU91hC6wGJI9aqMdwlnAIrwGf3zsIIEK1dtUCw9fuq48wdtghCnrtgXzxR8ny5jIQZplBEiBDleSYEjrN52GhPckKM7tfGSOWHeubFpQAXncKqhDxrg0POVEZPXRp-erc_WOaepBLdS1PUqAPt-TiGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24590" target="_blank">📅 10:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24589">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5Z9YKsxpKvefcGQs_rghrzzbt_GrnVmjYcG0VVoY6ivLO0ILpJxa79dwJUhNbhgp-oQTPzl7WdbOCVA7Py_0pG5O7rsfst1ohApP-YxhWiS7tT1XwSRmfEb7P0AYPBPZTGakcMJbeLhFwFBWIVyPAWkRNL9CjpQhkxI-X0A8962eYJ-z-rIjMPN9XI6p7S3qkeV5dIqKsV8yVx1icPHOATVzL8miBoTROrijcA9oibtPlzufapF315y0ory5J7QNvJt1bEc9lsq0qehfc7MqBsYhsiWSX9da9KBFFGviD5Q1zQ_w4jsQ085hssW_Y4-LYSFCwhqmk-_na-uJ2Gadg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24589" target="_blank">📅 10:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24588">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=fiwy-4qBJdeWYNKeoLe8KtJ8tGsKMp5Un3NVkbdIwIT_SmqatuSer3PtX37kAO9Es_8kOl9bAktIMOFsIe3wpEI8f402zcCS0H0NK24zsG04r3gqvaJt-K9xZgohlShlNKZuhe6xF5PVls__RWind1h_HBz7sbTmY4H8vnqT5Ogwm1c41wXXFtY7DJ81FXyM--9_OqCQVtGRE35yAUoJHYiDncdZdvDBfChgZU7vk0afERgL9_xBMQovEMGnMcmS-NTb9oiujfMnzH-FOFDlbwYwoSURDWkJoqkM4L6AxBfABj2f_F0RUgWNAit8zI7rEYe34aM99xrP_xWnok6Mrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=fiwy-4qBJdeWYNKeoLe8KtJ8tGsKMp5Un3NVkbdIwIT_SmqatuSer3PtX37kAO9Es_8kOl9bAktIMOFsIe3wpEI8f402zcCS0H0NK24zsG04r3gqvaJt-K9xZgohlShlNKZuhe6xF5PVls__RWind1h_HBz7sbTmY4H8vnqT5Ogwm1c41wXXFtY7DJ81FXyM--9_OqCQVtGRE35yAUoJHYiDncdZdvDBfChgZU7vk0afERgL9_xBMQovEMGnMcmS-NTb9oiujfMnzH-FOFDlbwYwoSURDWkJoqkM4L6AxBfABj2f_F0RUgWNAit8zI7rEYe34aM99xrP_xWnok6Mrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
صحبت‌های‌رامین‌رضاییان ستاره استقلال در دوره از رقابت‌های جام ملت‌های آسیا و جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24588" target="_blank">📅 10:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24587">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=UCq3QQ5OxmPa91VPcjyGTYnraeW_OPr2Lj02HSXAv5w2_wSvCvA71QDKKOtKCnZzasjAKCkWUq5g6CP0QMBEh3BZ-GQOXBbcGTH2r5XDk7b1O438GLAzfggwHObv1a8xsxC4YP2ous3K8vpGKI6HYJ8yxGZE7IZuIBC4vm_DgeQ6g_ezHHyAb73j3GUojytURy25L-kg4CG5VWAiO3fhCBuL-d63ZgRm1vpx2UWtCc5V29iq6C1hW5SGIJd-khMjeVBhnhvmrCdF7v7sEHsNXkn3bOBRaeUgwtPl63tH5jHAtuFroRGQ70cIUzqLUNLEXj7vaimZmF25u_JVbWRluoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=UCq3QQ5OxmPa91VPcjyGTYnraeW_OPr2Lj02HSXAv5w2_wSvCvA71QDKKOtKCnZzasjAKCkWUq5g6CP0QMBEh3BZ-GQOXBbcGTH2r5XDk7b1O438GLAzfggwHObv1a8xsxC4YP2ous3K8vpGKI6HYJ8yxGZE7IZuIBC4vm_DgeQ6g_ezHHyAb73j3GUojytURy25L-kg4CG5VWAiO3fhCBuL-d63ZgRm1vpx2UWtCc5V29iq6C1hW5SGIJd-khMjeVBhnhvmrCdF7v7sEHsNXkn3bOBRaeUgwtPl63tH5jHAtuFroRGQ70cIUzqLUNLEXj7vaimZmF25u_JVbWRluoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ابوطالب‌حسینی درباره بیانیه اخیر جواد خیابانی با زبان عربی برای الجرایری  ها؛ که گفته‌بود تلاس کنید که اتریش رو شکست بدید‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24587" target="_blank">📅 09:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24586">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=DI2Z6OTQTJNljEfQoyyhDdjq7qRPRQPeJhui1NeNjoRYqHpTOrDVRAVS_xAVg7nVNS0yWmNgDaMJyACmwGgapSuhXyl-ZtaaV_32ldFJrHI32oo-4p1j5POW8BUXFSp7kvLVenqJNtSHxG31ngsvnmyjG0Msr0T5BGnfs2lAneRIk40QKUtfp8YXMqmHnLniSnyQZz2BcDL5Ya1NFfYjocPAHD5jgJmWR67yx3QkC3wGzT4lX5Q5rCb7aujRfP9ANGvw_uLKXgEYpXFYc-BvDq3kKYeHGzN6qLMnGjcCneZr935Bh7zLn9PY3w4wI-nl60EBapOHJ843Yo116RJMMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=DI2Z6OTQTJNljEfQoyyhDdjq7qRPRQPeJhui1NeNjoRYqHpTOrDVRAVS_xAVg7nVNS0yWmNgDaMJyACmwGgapSuhXyl-ZtaaV_32ldFJrHI32oo-4p1j5POW8BUXFSp7kvLVenqJNtSHxG31ngsvnmyjG0Msr0T5BGnfs2lAneRIk40QKUtfp8YXMqmHnLniSnyQZz2BcDL5Ya1NFfYjocPAHD5jgJmWR67yx3QkC3wGzT4lX5Q5rCb7aujRfP9ANGvw_uLKXgEYpXFYc-BvDq3kKYeHGzN6qLMnGjcCneZr935Bh7zLn9PY3w4wI-nl60EBapOHJ843Yo116RJMMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
فوت پسرتازه متولدشده کودی گاگپو ستاره تیم هلند و باشگاه‌لیورپول درکوران‌مسابقات جام جهانی میتونه بدترین‌خبرممکن‌برای این ستاره هلندی باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24586" target="_blank">📅 09:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24585">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👤
واکنش عادل در ویژه برنامه امشب جام جهانی به حذف شاگردان امیر قلعه نویی از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24585" target="_blank">📅 09:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24584">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1TLF_7PflGmO63gXPfFHwQ85pxq9aXllnzkSp4cBBBOyf87qS64ot5S5VSsuRQ1nqdUFCaT896s1NlPYytC-yezbHrXKoftaKbDfpKPvcZyQx86-mBfkXpmW1TvjClniGTH1bAUroLOjQl5x2EzjsN2K2EmLWw9JeVttUTUrvV7OrOqzVdq1TYcSc5_td-GDuU9IeUfEo77Ai43nmfFiloCqp0_iB4lzBmE6tqdUh1xNFyDvHNtPxqgqloqZX4miJ2e8XHiUdyE04YjYRWAQIqOQXQoPRAXsXbEZulx4v_43uRtt1_n8j57sW2Iyq0nF7xm0RBs4C_AfRElzOp2ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شکیرا به پسرش میلان میگه قهرمان‌های جام جهانی رو بگو اونم شروع میکنه همه رو میگه بجز قهرمان سال ۲۰۱۰ که باباش با اسپانیا قهرمان شده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24584" target="_blank">📅 02:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24583">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQPUnImmz0XTWwLtDAgnIa_4dCqaUQBBg-Dp4jci2zskWFs-Wha_bmf-F_E-xVRqzSxerHPSpLkO6eHHDJdGYDQ240KwSXA7tgls6dJg_0plJ8eSNxxzafdvbQChzoMo9EqtOOvWN3cSrBtszJrE95gJUBpO3WkUHX8hbQkNxeUmy7VOGftXJowfjhLKx3QYR8F_sNTdfej3HYKRhv3wRk-gJPmOLfkyTjahb724-Fc290qAus2soXM5utd0juJNHbfUxh51koJDjHCyuc7LZIfgL5ZPM9WHcV6IgTyJdv3GsZsx0dmGeTu7x7I59xqsm5GdGtw3ODPnqXCTcTo5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان با گلزنی در دیدار امروز با مصر، شمار گل‌های خود درجام‌جهانی را به عدد ۳ رساند و درکنار اسطوره‌فوتبال‌برزیل کافو، به صورت مشترک درصدر گلزن‌ترین مدافعان راست تاریخ جام جهانی قرار گرفت. رامین رضاییان: ۳ گل؛ کافو: ۳ گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24583" target="_blank">📅 02:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24580">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFiPgua12wVI6UJAkgmv59wkuioLqBPdRQvId0mZQzsVytBkjd3I8xqaQj1eTIYQnsC9joqmuMl6dWDWWLbh1ayCoj7pnhdLyb98c7BAEsz7kdjpaQACfU_sWsYwLRMeWoibSFeJD3WCVsA5dafaIloSbYtSKZGYZjQtWrNHCtRZL3XfaeaWY61VIieo4FlanL4IiEVndmHJj52gd5YElbeOUY7zHwBNn4KLXH_27wckXGZ-VCgPrSsrrP36UTSldxMhI3E6VrNO2AUKlmqYDjbxOJsL9wpAVqkCZYOp7NtWWmSSV6ohuxN4ZtfYAfmaTDiNXI9rYf87XuKQjX3ubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دو بازی، 36 سال فاصله، یک اتفاق مشترک!
‼️
سال ۱۹۹۰ دیدار برزیل و اسکاتلند درجام جهانی باوقوع زلزله رودبار و منجیل در همان شب هم‌زمان شد. و حالا، تکرار همان تقابل در دیشب، هم‌زمان با زلزله‌ای بالای ۷ ریشتر در ونزوئلا.  اتفاقی که بیشتر از آن‌که نتیجه‌گیری…</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24580" target="_blank">📅 02:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24579">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW5gzHaHUco6SRzPvbyqLzlVNVAOTlQXFdf7SSD4NYrimE_4k8KEequ3kmIbEREPRpolatySw6JMmBsFOj1u0UM3bQ9lVNYEn_P7Lx9ZDQiHAW7ciacKFd7TaUkFgRv03wg72pO8W-ILED750ybzEY4h-g-4aVMzx_fMSOvuatnjZ-ZtVpVnGVRgeTxkoesGcI1-CgMEm3xTvA5oqg3IAJP9Y1OiEmBSwGdHvLchLQvrRDetdFo0BUl7HKXuBXfHIo206a1yS7cDdl2Aen-0djovCmKutZhE8sepP_pBr6JFGafUMJvrFqKGq7oOxgW3GRBlKd2dxwdmHRyERdzkPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24579" target="_blank">📅 01:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24578">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBO0tw3tGwwnr6Ug208QfIRajxAkq9mB6OP-LLrppq59tIeVIGhbjw2xlsur5-9WJW7DhzFC9J6jndOdzWDgn516I9YboWycKW5SoWX4LLVYn_Hgzi5L54DwTVQtK-2TlCU_e2VP_8ULa3rfYXnXPUdyqw4k5NdlTHE0JBuwzyYv3pBxYqS8VyDVVN9y6NyxJoPfRu48FHhWnqOi8N7MKpMMKkeatL_1yuRtNPem_pG79Bcw9pGEKYDn5fmfRwBF42IEzgxEHzzl_fRgyCMtHTFhWNvnXLdk6NfwOcVgyCmwAMeHAVME_0KxZUmkyNjfihtt6LL4jt2AhWQjhgw84A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛
تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24578" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24577">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlDF3CHaFksqYg0hR1HFDqZIdPOFrwOMRn5kpKSTVctuTeGHrEinHZc2H33i6v52WB8oKQ4ca_ogTk-JzAk8IuonJq_uRQu1fPYW6QtGNwQxUQ4MlhdYXeBPJqMLxUZDbw9uEYrxJnYlDId_n9Qawp2nuSC8MxRgbjdz8bPVz5CjWPrm4CJ2yvX0uqXi8V1AUOkg4EmPexSpVyeiN1vq8aTDQgnLJOFU5lEmSjlanTulP_vcO2gl4NysLc68pqgJmbhuWBt20owT8AxVpJkcppQB_RYaCvMRAfk9aN8GZy7yKMadGAxpV0UfU9kIdxj4-yQD3vRdznkWAXaQeK6Rig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از توقف بدون گل در جدال کلمبیا - پرتغال تابردآرژانتینی‌ها درشب گلزنی مسی و راهیابی کانادای میزبان بجمع 16 تیم برتر جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24577" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24575">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgkaP-zl_aw9tYjgkr6HwKfJdPy_BK66KkrmTJld19nWh3k6TsuFDPXq_JJcFOnvWv7vW2t7CPqagltUDZrnh33N1ZG7oPLODf5ftrNMRI9ibT9XinDvYxyZj9wyDI4pg-hm2zCCXSb5-pwrq8XWLTJngeRP7UKZmrghpQms5QuXxdhUkF138Nbrdb9xz3BORkcay8Y49xznbu-E5fRZlWDhh-5eJdLsK68kbWE3CMmT1lqBBcHdizMnlELKcQLEnJN_J24rs0GrxOBnXL-_wzTimt6lOtAedN_swU1ky92RGtlJ457Pu4P3B1t05t6Uh6KWQImbkpGdY9RulmjDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24575" target="_blank">📅 00:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24574">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=B_z5j5Mz2WxzZR7jps4THqoxdg2Mrcgp5K8O5idblUHiNy778ocNGPT00_788teVUY0MSWcQNuCh5NEu8GiGkL8PPgQMC-KWNS7e-xU3OoXF-uwWwBMbxQ69v56380_nUiVL-wZ1xvvJ8wVkTj0c4Tr2CMJSK354u53cCGVyiXg3FbbAxjOhXluIEs43jaCM7pqHVgo7cAYOruyz7YC1hew03QWl6JeR5mQcwYsljekNVnIRgqrdANmVs7i6jZZyV4aYMWFW3twyEFulU0rclbIEE67urVo-nqyBTKi2_vtKy_169OIkTOtclXWMv-X9m_TgP062bE5PJQdAE3b40w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=B_z5j5Mz2WxzZR7jps4THqoxdg2Mrcgp5K8O5idblUHiNy778ocNGPT00_788teVUY0MSWcQNuCh5NEu8GiGkL8PPgQMC-KWNS7e-xU3OoXF-uwWwBMbxQ69v56380_nUiVL-wZ1xvvJ8wVkTj0c4Tr2CMJSK354u53cCGVyiXg3FbbAxjOhXluIEs43jaCM7pqHVgo7cAYOruyz7YC1hew03QWl6JeR5mQcwYsljekNVnIRgqrdANmVs7i6jZZyV4aYMWFW3twyEFulU0rclbIEE67urVo-nqyBTKi2_vtKy_169OIkTOtclXWMv-X9m_TgP062bE5PJQdAE3b40w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیابانی‌این‌بارگیرداد به تتو روی‌دست امید نورافکن میگه حالا که‌اسم بابات‌علی اسم مامانت چیه
🗿
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24574" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24573">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzM33moQq6Umg7kq8aly4OyGKb68SOYjPW5FLS0qeoVkSjOVC5hxEN-YuaT03ne66S05JrloLZHCwO3go6qS1I-lw2AzSfA0XmCFzV_SOHPjb7TzOqk4Pv8xjtZBrf5lJgBHsbutsTMaEckSNrVZWOsX_NKKQv20UuBD4U2V1chdBAQA3_y1GoHdMVmrlWqYwbAfL9usLC40--vZP3RDd6MkFH2UKKVyL9WOB-8S6WQwpNsPqBUk6mA3C2_L2KbR8dxuCr-iyjZIKaqGCIZnEgEXaCrhedONjDkObVgu7MAvuAa_Enyh_rZcfRPQMcZS31G67gdZmp96g61EIDC1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
👤
#اختصاصی_پرشیانا #فوری؛ مشاور محمدرضا زنوزی مالک باشگاه تراکتور که در نقل و انتقالات اختیار تام گرفته با باشگاه اتحاد کلبا وارد مذاکره شده تابرای‌گرفتن رضایت نامه محمد مهدی محبی ستاره ملی‌پوش‌کلبایی‌هابه‌توافق برسد و این وینگر 26 ساله‌باقراردادی 3 ساله…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24573" target="_blank">📅 00:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24572">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCaiePS8PprXtft-M7ZeIaq4NWNPtN5B_9Ttfw4sOPHjY7zSjdGYG7lJaGdHIHYBoKHn9du8DI-d3PO3nBnwnCVBbkEPe_SLJQmWqYAZs83BYlk1z0SRd5_kBHLvLtQhm7ZFfEQ5WP4X9wT5Nx1JAkaf8EoIW-DwVt_K4X_vzqhK-4df2bgOkCoNOC6ByWPJUIJye7TUiKUK2UehIfzcgIpplVUhTFiLknBjz9T9ZjGvRxX2CW8wPz-zg2cc7J2VgDGxLL_ceBE0u2WAhaLIuTufjutRPSSFRuVinpYYtLX4gn9AGOlCyJsmRf7L-gbYj7q_vAt3yYLWiMyNJ_STgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جواد نکونام در کنایه به امیر قلعه نویی: شرایط جنگی نباید بهانه شود، عراق سال 2007 در شرایط جنگی قهرمان آسیا شد. پ.ن: این رو کسی میگه که خودش بعدِمساوی‌تیمش باد و هوا رو بهونه میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24572" target="_blank">📅 23:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24571">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bbd868c90.mp4?token=b7Zg0u79h6Yj8A9_0_65v-NEuJwSX7MFNBeYOzGQpTnv9yHYNPF75kCdgNfQILzTtmNDdV1HcWLoAmb_ndzMy5anLXnAQTyWSELRdf87j0cdALY2t1-t0HPANnt7wP4GjAomDucoxM-VmWfowMvn0n7UcU4c6gDxRRvNUmf52KEFHBOWMU49Dl4TPFJqELv65-W3YWn4ZLqa_iWUZv619XO3Lhu4mKls7cUdM45z-FAmonL2Bl_3zbYuwGfDFybics4DzLBnOcfUvr0gPZ1X7Leq-bpQA0NhGbHXSQ9D1bDhYjzLQRHg8vtIwrwIyk8vTxzK5WQMc1XXMEd2q0lokA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bbd868c90.mp4?token=b7Zg0u79h6Yj8A9_0_65v-NEuJwSX7MFNBeYOzGQpTnv9yHYNPF75kCdgNfQILzTtmNDdV1HcWLoAmb_ndzMy5anLXnAQTyWSELRdf87j0cdALY2t1-t0HPANnt7wP4GjAomDucoxM-VmWfowMvn0n7UcU4c6gDxRRvNUmf52KEFHBOWMU49Dl4TPFJqELv65-W3YWn4ZLqa_iWUZv619XO3Lhu4mKls7cUdM45z-FAmonL2Bl_3zbYuwGfDFybics4DzLBnOcfUvr0gPZ1X7Leq-bpQA0NhGbHXSQ9D1bDhYjzLQRHg8vtIwrwIyk8vTxzK5WQMc1XXMEd2q0lokA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب ابوطالب حسینی درباره حذف شاگردان امیر قلعه نویی از جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24571" target="_blank">📅 23:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24569">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c12652e71c.mp4?token=oD-wAPhvc67vs6lOXccJKX1y0h2v2vH3JLY7VpbgGg0QLQTJPGBSsIOfcMfFhs1ViqFn3-78mTDFgl1eqez9Z5TFS90TfBXKRVMiEArprzqLDGqenO22jEiex7BmqeZyeCwzuT8nHIBR_QHiRa8ehoS-39Le96GLU7PGbMYk25Xf_NeorVi3IA2gPYVLznoFdf-JVsmchCIlMxw8VjtxN7bIctrex3RvnQwsJXA5ROfkqaIRs3RGA_Y98q9WozOMCjArevdAkWQO_YrTaQDgYPXP_czAm_v2TtAffSzUeYf18qYlJb9xlq-asg2LW6Q6OD73cXsdZ3nIfRiGqeTpxIX9gwSZN48kCJz9fB8TavnpYat3FGpufLk5xy4GT2DiCR6ZvqRsoTJY5JC8nVKhsDUOFqt-G5-YhPtHlWwrZ01mF7W4UtBvARxqD5jFK_Tahw-F1NRu2np4J_pWwKwbNtueshpsvrqymSCfQ51s2m6nCbbxVAKQ8TkIiA7U0-iMM7TFOOWUhx3w2x8BpiPndYF4nn_5oUiZIEk3InNwN74-PzwqA9we06UkvhcJcCq2lZiloYTk2gbOUUCiZtyFUHhpEirLp8EvaotAU2zRxQYmpnUvF2_SSFfVGO-jaPmdgRD6ty8TC-dfJVgDPCE0Za8qxwiFw_5gvpG43iWun8U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c12652e71c.mp4?token=oD-wAPhvc67vs6lOXccJKX1y0h2v2vH3JLY7VpbgGg0QLQTJPGBSsIOfcMfFhs1ViqFn3-78mTDFgl1eqez9Z5TFS90TfBXKRVMiEArprzqLDGqenO22jEiex7BmqeZyeCwzuT8nHIBR_QHiRa8ehoS-39Le96GLU7PGbMYk25Xf_NeorVi3IA2gPYVLznoFdf-JVsmchCIlMxw8VjtxN7bIctrex3RvnQwsJXA5ROfkqaIRs3RGA_Y98q9WozOMCjArevdAkWQO_YrTaQDgYPXP_czAm_v2TtAffSzUeYf18qYlJb9xlq-asg2LW6Q6OD73cXsdZ3nIfRiGqeTpxIX9gwSZN48kCJz9fB8TavnpYat3FGpufLk5xy4GT2DiCR6ZvqRsoTJY5JC8nVKhsDUOFqt-G5-YhPtHlWwrZ01mF7W4UtBvARxqD5jFK_Tahw-F1NRu2np4J_pWwKwbNtueshpsvrqymSCfQ51s2m6nCbbxVAKQ8TkIiA7U0-iMM7TFOOWUhx3w2x8BpiPndYF4nn_5oUiZIEk3InNwN74-PzwqA9we06UkvhcJcCq2lZiloYTk2gbOUUCiZtyFUHhpEirLp8EvaotAU2zRxQYmpnUvF2_SSFfVGO-jaPmdgRD6ty8TC-dfJVgDPCE0Za8qxwiFw_5gvpG43iWun8U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌از یوتیوبر‌های آمریکایی وسط بازی ایران در مقابل بلژیک عاشق یکی از دختر‌های ایرانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24569" target="_blank">📅 23:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24568">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/un9z2GlzPPRoHMDlrp1IHF5IdqVFNNqrfbgeAG_7xgHH47DqOrqV5l6dCGp4wkdeTBdWwfQ-pzMjPyB3I_gI3jGOeKt7ZUvFfoIRFyl6lWqAgP-yJAzcQj15MLtn7mDAok99LZGLw5eG9FyH73SNdqDFdqX2jTqe4xdqtRtqpHpIe3DASB_r-iis8K3KjawTzQZvKQRthKXgqHdUBjVSxRZtDEBOaSk4T_E_BLbz9d1lYfqYkM3BONA0W5fIhQvNGN_fSiFLN93PR5oH4vENfGLfbC2509dlPZ00EkCd4AOZYZyvghdlGdxp_7Zl5FM_T6K4KxGhNhdDMqPIWRTDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24568" target="_blank">📅 23:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24567">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=qpEqTwt_k3XK578ewvUzuzAp5yg04Zupo72MRhRbQXQQJws2kbEFJxMU7OZUpIYXkWDUbyXJyooXIOmYEpqefHvQ_o6EacLV0yPWYkP_3M_1bZzgPOtEWWnIEyxskD23Ocw4T3xL2M_0uZpyA8CI5w9swxQ5_5mlFTFSvZ7KkkKqEE2R8kcPwXYz681u_Ea8hhjAhc5vrrPCUOaxSNtM73scUBvS2xVAQ13NRoryK22xpaa8-1Ool3-g_XG0DOnP_HGOUQbJT6dlZoyZW9se9MmrHLZdnC5PkMxKhkbm7k36MbgsirPEqNvSled5iZ5jXvHLiielR944hn5M65sEtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=qpEqTwt_k3XK578ewvUzuzAp5yg04Zupo72MRhRbQXQQJws2kbEFJxMU7OZUpIYXkWDUbyXJyooXIOmYEpqefHvQ_o6EacLV0yPWYkP_3M_1bZzgPOtEWWnIEyxskD23Ocw4T3xL2M_0uZpyA8CI5w9swxQ5_5mlFTFSvZ7KkkKqEE2R8kcPwXYz681u_Ea8hhjAhc5vrrPCUOaxSNtM73scUBvS2xVAQ13NRoryK22xpaa8-1Ool3-g_XG0DOnP_HGOUQbJT6dlZoyZW9se9MmrHLZdnC5PkMxKhkbm7k36MbgsirPEqNvSled5iZ5jXvHLiielR944hn5M65sEtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24567" target="_blank">📅 22:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24566">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🏐
دربازی‌امشب‌آرژانتین - لهستان در لیگ ملت‌های والیبال ست اول این بازی به شکل برگ ریزونی 50 بر 48 به سود هموطنان لیونل مسی به پایان رسید. قشنگ به اندازه دو ست تو یه ست بازی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24566" target="_blank">📅 22:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24565">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5D7UyW7CP73UEepj_ayOa4dPJ_-VF9jBCo2rrqDnfDLRaDKVQ6Gvw-Ebew9xlVBaqd7hJx_8SCo-dmMqEaA8f7sPFj6qx56E8iDYG2SqqlmUPCRB43m-dLyaJfo_xbmJfdLlvAqIjB6nNzM2uv0AS4X9PE_BqFYMPVqCi6dfO3yzRm3Evj1sTsTcQKQDFmGYB0F7L1fYOxknzzKRMhP1s1Sj-S2DEYXqVwmINRE5OemDC01DRCjJioDnLPdR88XHBFHj-AZh6YUatfbqGcGkoduk_Pclbc_IS_ob23iFmWPlE_RlHaATgpDo5fKFNScgp4uPEF2rQjH-RA0Fpy2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24565" target="_blank">📅 22:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24564">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=I2uabiB34O3_q5haNAzvKdhXJFSOm7uTPdLQWgLGs27eRtZ8mYaH-rLAnLSeNgDi8ZYibhNra7aff_kyLvarXWxB8cJQSy8oPQKSw7bbAPVmy5svKlWAbDwdCl-3BO-nRp_CUFx1f51RJczoMfe-phFV_SOdWMTVKYr2-E1N-K2xO7S1Aik1fqWclRnP0leJQv-tdV9YmQC3pcDnOj6mt-ySTvynMOS-hDLPVI8vVU4T6Hf3no6Pl0Sl4ARkZ2m6DnoakfBuXnGCxpn0vROdRc-2yCx3zTce6JZCU1A7yi-Bsh62OGVb0WBZV1A3Vd30zVTc9gjiHu-SApOoZfOqmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=I2uabiB34O3_q5haNAzvKdhXJFSOm7uTPdLQWgLGs27eRtZ8mYaH-rLAnLSeNgDi8ZYibhNra7aff_kyLvarXWxB8cJQSy8oPQKSw7bbAPVmy5svKlWAbDwdCl-3BO-nRp_CUFx1f51RJczoMfe-phFV_SOdWMTVKYr2-E1N-K2xO7S1Aik1fqWclRnP0leJQv-tdV9YmQC3pcDnOj6mt-ySTvynMOS-hDLPVI8vVU4T6Hf3no6Pl0Sl4ARkZ2m6DnoakfBuXnGCxpn0vROdRc-2yCx3zTce6JZCU1A7yi-Bsh62OGVb0WBZV1A3Vd30zVTc9gjiHu-SApOoZfOqmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🇧🇷
دلداری‌دادن‌کریس رونالدو به رودریگو ستاره جوان رئال مادرید که به‌دلیل مصدومیت جام جهانی رو از دست داد: باید صبور باشی تا موفق شوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24564" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24563">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=banK5x9d_1i9nMnxqY3BlM-Lu8Q5Ybk1TiLJO6IdyIRSv1aI6vcoEQ18VjitjAZJ5pnLY64ca_OX_t8wZt5BE5o02_WlamYApFla_SIUPO6uscaOcSsrD2qr162j8_VN9zyjxQMKcGT1Hir2A_qq1frwb70Oob6MWWnuxbLcHgVOFoEeF4L41SmMopbzbsBIXKJmLPaBhhua1Fbj2pDyTYCFr8aftZpovTGfmEpptqqtT4Cc5SXO9GmR3raSevJfgNmZ_10VHjpOQTRlD7bZ9Qor243hUB6dOFXkhZwNqF6LoLxgUvq6fZxLMpY_Zgc3DU_enl0Y5j92o3016Advsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=banK5x9d_1i9nMnxqY3BlM-Lu8Q5Ybk1TiLJO6IdyIRSv1aI6vcoEQ18VjitjAZJ5pnLY64ca_OX_t8wZt5BE5o02_WlamYApFla_SIUPO6uscaOcSsrD2qr162j8_VN9zyjxQMKcGT1Hir2A_qq1frwb70Oob6MWWnuxbLcHgVOFoEeF4L41SmMopbzbsBIXKJmLPaBhhua1Fbj2pDyTYCFr8aftZpovTGfmEpptqqtT4Cc5SXO9GmR3raSevJfgNmZ_10VHjpOQTRlD7bZ9Qor243hUB6dOFXkhZwNqF6LoLxgUvq6fZxLMpY_Zgc3DU_enl0Y5j92o3016Advsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24563" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24561">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc1de478f0.mp4?token=dX8DO6cJ111gvnnEYXoGt8n993jfg7ZL6TXhw2uDFuxacZIvyk3dpdlCLVLHLpS_I9vNfuIAZzpEm0tmOasJlmaQ9fofixd8XpyMPBoPWbFNPpdKlak73Hq2qTC5zYNO9cG7khvzBiEtXThSpic6dorFETsu2lhuSNOFcswq4_vReIL6TFqY2C6xvUl9RlpI860Xy4vanke93FRFuqX7firuPIDySjqMC9CuvWeCskyu34VB3uWCXTrzyfKQq-mphArDcHF-hEWRgYgj7GKCxyVQ_slt-v9U4NkTIo5gq6afm5USfaz-zIwDzoCeW3z6d0mUcg_gW8k3WxBK7KjKQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc1de478f0.mp4?token=dX8DO6cJ111gvnnEYXoGt8n993jfg7ZL6TXhw2uDFuxacZIvyk3dpdlCLVLHLpS_I9vNfuIAZzpEm0tmOasJlmaQ9fofixd8XpyMPBoPWbFNPpdKlak73Hq2qTC5zYNO9cG7khvzBiEtXThSpic6dorFETsu2lhuSNOFcswq4_vReIL6TFqY2C6xvUl9RlpI860Xy4vanke93FRFuqX7firuPIDySjqMC9CuvWeCskyu34VB3uWCXTrzyfKQq-mphArDcHF-hEWRgYgj7GKCxyVQ_slt-v9U4NkTIo5gq6afm5USfaz-zIwDzoCeW3z6d0mUcg_gW8k3WxBK7KjKQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌ های تامل برانگیز آیسان اسلامی درباره باخت شاگردان امیرقلعه‌نویی از جام جهانی 2026
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24561" target="_blank">📅 22:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24560">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc38dbe3cb.mp4?token=Iz8NbR-Zkmj5wIl8q-lHC1F_n5dKa9_vkZX6AJauUjpTMWi2x2Zmv-PDD9z8ffwHUnCmXZtWUj2Bz8KHtKLkoMGXwCXQe-kbZ03Lsp9624rAN3cu9yy2OBjIlaANdPKi9yG2JdTyuulXjk2MUqHCsQhgE03Ii7XUsBSZsi-NUL304YbI2SyYdMfi-flL9e4ZfsNLtKANwzjkjJiafjFqUA2_Fu0cW90JUunOwFsmmqChqNvvAaIX7FqL3SwsXnKUmQaJYyvnFA4W6LeX22_MCvNYWWeU1Bm-Kis69vfz_ajtMCSSrx5PzoxG6_sgAbW0M93IUv7WwuYAn-kt88qM6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc38dbe3cb.mp4?token=Iz8NbR-Zkmj5wIl8q-lHC1F_n5dKa9_vkZX6AJauUjpTMWi2x2Zmv-PDD9z8ffwHUnCmXZtWUj2Bz8KHtKLkoMGXwCXQe-kbZ03Lsp9624rAN3cu9yy2OBjIlaANdPKi9yG2JdTyuulXjk2MUqHCsQhgE03Ii7XUsBSZsi-NUL304YbI2SyYdMfi-flL9e4ZfsNLtKANwzjkjJiafjFqUA2_Fu0cW90JUunOwFsmmqChqNvvAaIX7FqL3SwsXnKUmQaJYyvnFA4W6LeX22_MCvNYWWeU1Bm-Kis69vfz_ajtMCSSrx5PzoxG6_sgAbW0M93IUv7WwuYAn-kt88qM6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یادی کنیم از این ناگفته های عادل فردوسی پور بعد از تعطیلی برنامه دوست داشتنی و محبوب نود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24560" target="_blank">📅 21:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24559">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rwm1wYG8Mv3mQlpoq6BvFLapJdYcKFChTv6uMc5CXAOFygl35V1nyJbG5ULHRVuXvkXyPAfheYmVdni0XlZZKXsCaOiE8ZHJkZRLbORxPgheCEadKzHHUPzTZT9Vcmo9Ctw5-5VJHuKb1r0yIJdSeIkg6jX4x9liMQRiyfAx6qcpoR7fLWl8HBK5CQVdWmFeKr8OzYBYnOcHrkyR6VHEoSk4POu5IXsPKiGVDqP5q8fiJfzNPP49uH2E6sw1RYU0xhj9cLXjaIXWYNFYwtsINg0za35xYWWg-NnhImBGhCPi7Ec16U34hzNtFraMJP7ucHqmD6kA9LDTijaOu_JVXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ باشگاه اتحاد کلبا به ایجنت محمد مهدی محبی اعلام کرده که‌حاضراست با دریافت یک میلیون دلار رضایت‌نامه‌این‌بازیکن رو صادر کنه. مبلغ قبلی که باشگاه اعلام کرده بود 1.2 میلیون دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24559" target="_blank">📅 21:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24558">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSatYJ85K6TRxdCIsUiJyp0QQFVEnbh943odvcsdMouFwA1V2nd-nFTF9L9B3hcIvWCIVitV7_i8WxzEejsao5kzEaY6vkPbSWQ6Y_0RRh-A52X-4YCm1vDa0hUpxgga74Lle2B7o2AOtqnlQlUxJrcrR4YxikpgFMEaW5up-3aJwBwo14CE363KNP8wTfaptHJ2mKk4bQdJby4n9aoAnzSgMQ32Uc9IC509uUvDbPfm30CeWgtLhBlm8PLcrbejbuz3nipDOz9got0MLUPN1kFb4_rc-HNLQO4m5urYEjSzaFR5Mk2I-IooMix1OLQ0KUmTe8GStLksqnLFeWo37A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
باشگاه سپاهان 72 ساعت به سید حسین حسینی دروازه‌بان 33 ساله‌فصل‌گذشته خود فرصت داده تاتصمیم نهایی‌اش‌رو برای موندن یا رفتن از این تیم بگیره. مدیریت سپاهان همچون بقیه بازیکنان از حسینی خواسته رقم قرارداش رو کاهش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24558" target="_blank">📅 21:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24557">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cK8HXhdDvuNB0u8w3soygDtwQ3LRBXjhG7ROemr5oKXGfwanr5RczdcZbu6daQ9nDrhKmtr9BA0fOILJKnihTDWUB9lq4Aau7BvQcQWOabTyWI0ZTF6iAf7E9dIbr75QsjZVg1udXrfVLVaCRKBHSgeII5QgPJh_sPzoIvNB614JJUN7CGr78f4udQ2wse1k3izE87wVX-FvxTeJW8QSmTp5pe2cHltjFf6kL4dVQjI67kJxuz5agzrIDLyOIz4yKGp5cd75_nS9TehilhIbNZFsheaGqSTAjj5iAk3Dajvzw8_L7g8EzPQs0NbPIMlm5PXWg93naIbOsmejRrbH_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|رابرت لواندوفسکی با ایجنتش راهی‌آمریکا شده تا با باشگاه شیکاگو فایر مذاکراتی انجام بده و درصورت توافق نهایی با این باشگاه قراردادی دو ساله به ارزش 6M€ امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24557" target="_blank">📅 21:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24556">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwRHAeJDtgUaDnuwbPSU9YhjjwqGTWTJ1MV6njDUNUfXQofJSF5lrSFKPpcQCjD8lpf_RI-sscg4AiqFaZJxfUF94YFqSuQx7PPswfNeJsvLSZ06_WA-_L0KK7hPKPIb53wB1pypDyHR8NdQs79bCpCO2l6Gf27IIDdXPYTjHN8vCse6xngsoYI7aWvkehWh6W8Xtdeby1La6Ah-FaWwZza4G2r_7OS16Vuqrd43_jvRUyvkgCqVwi458_nkFLnCPYzHo-AwjhlrSukjQpOPEwK3Vez7z7YZAtD2c2E5M8fZDUUCyVj1rx8DbeMXQy7Xxlq4BP0nYkDCcKbl7EzUxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
🏆
#تکمیلی؛ سرمربی تیم‌ملی‌کره‌جنوبی بعد از حذف در مرحله‌گروهی‌جام‌جهانی ضمن عذرخواهی از مردم کشورش از سمت خود کناره‌گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24556" target="_blank">📅 20:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24555">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=bCCjGa-nFu7oq2aU1zXpTU1tA608ezlI2jrSs6FxlxG5XvX3KsoCsVt2SKy2h0N3Ks-3k6sZDo46BikS2QfUJ0gXPHouR_2uSCiOq3PgQu7sPKPrgQncdCK-i8-OtgzJdj6CJhI0z_sUuTB3gVJIcu2eWlDnrJhvWGlaENSb3ICsQHCOxOZuRLdgCicFTcA59p4aqpxrmz8uU2D2Sv50xIKJ64EUU4lN30fZPrzLeCKhOj1Pehfq7wE50MG1ApGePcY-9U9EwoX1Q82YjOrOe2Y5quAON8TPmhmt8soEQu07DcTrd0IQFgP_W1-FVMMDF7o1tJlK9VVOUor0J6LRpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=bCCjGa-nFu7oq2aU1zXpTU1tA608ezlI2jrSs6FxlxG5XvX3KsoCsVt2SKy2h0N3Ks-3k6sZDo46BikS2QfUJ0gXPHouR_2uSCiOq3PgQu7sPKPrgQncdCK-i8-OtgzJdj6CJhI0z_sUuTB3gVJIcu2eWlDnrJhvWGlaENSb3ICsQHCOxOZuRLdgCicFTcA59p4aqpxrmz8uU2D2Sv50xIKJ64EUU4lN30fZPrzLeCKhOj1Pehfq7wE50MG1ApGePcY-9U9EwoX1Q82YjOrOe2Y5quAON8TPmhmt8soEQu07DcTrd0IQFgP_W1-FVMMDF7o1tJlK9VVOUor0J6LRpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌ازتاریخی‌ترین گزارشای صداوسیما از رقابت های جام جهانی که تا ابد ماندگار شد. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24555" target="_blank">📅 20:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24554">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=dswmaTIMR68qX6emFhotd6OWNqprgE6QVGWXbi_J3AxjX9ryDHiWs7Rf9oJfu7nnP4375TJ-QXio23d_YUByQxm5qGMyRtaTF8w0U94SK_dOuDF-p27oVJzBPiezW8EJMcRu439dyRn1SW9DdGHLnBePo7SlJd9aRMm5NL45uDqh3mWtlIpqJF8EbDc3llPvsXfpuRPKRHFsp9o4CCBxqt6KnYKPpkYxcbfrP1W_J83EwnH9_aJu4mossyop9eim3cgllr44ukmU29Ns0XZUln5VCoW4e_QtKK4DltAyxIwMXKAyZ3L8l1iaJ_xTXaq63IRAH17qU8moyNkx48LieQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=dswmaTIMR68qX6emFhotd6OWNqprgE6QVGWXbi_J3AxjX9ryDHiWs7Rf9oJfu7nnP4375TJ-QXio23d_YUByQxm5qGMyRtaTF8w0U94SK_dOuDF-p27oVJzBPiezW8EJMcRu439dyRn1SW9DdGHLnBePo7SlJd9aRMm5NL45uDqh3mWtlIpqJF8EbDc3llPvsXfpuRPKRHFsp9o4CCBxqt6KnYKPpkYxcbfrP1W_J83EwnH9_aJu4mossyop9eim3cgllr44ukmU29Ns0XZUln5VCoW4e_QtKK4DltAyxIwMXKAyZ3L8l1iaJ_xTXaq63IRAH17qU8moyNkx48LieQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24554" target="_blank">📅 19:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24553">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSyPoNZmGaJhkjdOGJOITdPPrI1ngGlOBLk2bFNuEDS9jM49Pzm99GDqkkifBxlOQTxf4Ldqu81sppyy1f6rUNzFhCjwdNbE3Qxa0VCJKrsOMjyitNxHqVaOo_1QqicH-XErs5_TV7cusWK2FslK7eVt7eN2UzVNnU68dfy0s3gZbAOyOzWiA3s_YOu7GtKsvtKi6pWHEPURSVAvg-mfvSa3hSVY8V-FFO6zLyjU7UEh1vG2c7I1SuU_i3dW_h-SPp4OHdZGMGWN_O82KLFR4t3d33maM10X0F7yIJMPOvd7WKfB_0cayV9LURtsZZm7ukMPCo99DgEhnRBhWbmt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ دراگان اسکوچیچ سرمربی فصل گذشته‌تراکتور؛ بادوماگوی دروژدک ستاره گلزن فصل قبل تراکتور صحبت های مفصلی داشته است و درصورتیکه فردا بعنوان سرمربی پرسپولیس انتخاب شود به مدیریت باشگاه خواهد گفت اقدامات لازم رو برای جذب این ستاره کروات 30 ساله انجام…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24553" target="_blank">📅 19:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24552">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030de140d.mp4?token=FRQ4_1TpET_Tfk2ufKG3TngbR3o-ByL68t7aZFXMARcO5sX62jT3C-pta9qyggUPB-Tf3rOjzCPjfxJyBr7D0Ue9KwHHpcMRp2J8VUBGvuHsgCvanXACEjre-Wxc2mr1hOInQ818nDMVp33-dke-rw0hniSZIp_JB53IyeJcn0AvcMHL-bpl_d80BBll2toFVT0n_o5NfEQLEDtiLqO67fOuz7kHHjuRTTA97c5U0urZ3hk0EgeOwd2e7Kp7KPhPruIYBBKuy1HK0RNwNXd9wT4WNRPf1z35fbd-yjwgIwlopQzU3DVnAWM66I9bzmpqihSDJrz67CA5sSIfArghaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030de140d.mp4?token=FRQ4_1TpET_Tfk2ufKG3TngbR3o-ByL68t7aZFXMARcO5sX62jT3C-pta9qyggUPB-Tf3rOjzCPjfxJyBr7D0Ue9KwHHpcMRp2J8VUBGvuHsgCvanXACEjre-Wxc2mr1hOInQ818nDMVp33-dke-rw0hniSZIp_JB53IyeJcn0AvcMHL-bpl_d80BBll2toFVT0n_o5NfEQLEDtiLqO67fOuz7kHHjuRTTA97c5U0urZ3hk0EgeOwd2e7Kp7KPhPruIYBBKuy1HK0RNwNXd9wT4WNRPf1z35fbd-yjwgIwlopQzU3DVnAWM66I9bzmpqihSDJrz67CA5sSIfArghaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24552" target="_blank">📅 19:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24551">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=l5msLpWa8WjeZiJU6SjzPtYMB51NM05vU8-nv1_39HoTdtLYYPk9frTkIHL2LetYHGvJUJhSEz2D_-GCUDHr-briFHrHNWMSlIsvQTIJHQdmV0QD0e9pNI_D8Xdy58_FgZDuHqUDSbD7XpghVKm1E9eJHOLwzw9q8MNvh91vuR_mV--Ibrqs5VHYwo8yJjuh7gYdBypwVGhF2ydotmEETlAVnnxcRff2n7ufCt7kTgkDIl21YGsRoD5tFDHT7rLXJ9QFMZ3mpaPE1Ecqm9iDjZuS2c0XNRGXOL-usRGav8jwRwKyrEPkEEq6z7HWEVC5XM40ArqaGxb8wde_rd9vozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=l5msLpWa8WjeZiJU6SjzPtYMB51NM05vU8-nv1_39HoTdtLYYPk9frTkIHL2LetYHGvJUJhSEz2D_-GCUDHr-briFHrHNWMSlIsvQTIJHQdmV0QD0e9pNI_D8Xdy58_FgZDuHqUDSbD7XpghVKm1E9eJHOLwzw9q8MNvh91vuR_mV--Ibrqs5VHYwo8yJjuh7gYdBypwVGhF2ydotmEETlAVnnxcRff2n7ufCt7kTgkDIl21YGsRoD5tFDHT7rLXJ9QFMZ3mpaPE1Ecqm9iDjZuS2c0XNRGXOL-usRGav8jwRwKyrEPkEEq6z7HWEVC5XM40ArqaGxb8wde_rd9vozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24551" target="_blank">📅 18:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24550">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCJ9w-OcME7zMn3eWCiAYI2N83TLgjk1co-6UispPl9Oibf7AkPnJkmFMEDSWUslxMM8BNZk3eI7QlX9NoZ-X6gfmujjymAR1k4zZ-YW2EH0dXdm3SEfAwZSqObSuasnnF0gk1hrgrtM94xPgKyB-ItieuXBbEQQkP2Z_k33Y1g8PrM48yhEtDbYREKxmBbvQeRh072mtCRRlKd_IQy7VGsMKYsrutJoAqAKK09EM_Ehm9X5EVh4r-a0esh__BGiXWncYfvt9l6qo16BE-DDkN_Q6AkGO1ElhlRvD5srmSypFbCT8KiGGc-1ncTOyjtT78BQ5mvqmCXowsjgwIPEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه پرسپولیس 5 روز پیش پیش نویس قرارداد این باشگاه رو برای دراگان اسکوچیچ فرستاد و مربی‌کروات باامضای‌آن رسما سرمربی این باشگاه‌شد. حالایکی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده که چرابدون هماهنگی با ما پیش نویس رسمی قرارداد باشگاه…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24550" target="_blank">📅 18:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24549">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6osA0fcy3L5gvmrBcs6KQAxenNqYWcPKPS0voajgVBhauJKjkAgItSss_taaXE0yDTnxjcu46wY9HqpljY9mn-G1A13a0ojHe2PxdTiwRG4QBnvQPdVIiQF_rr4cUycZHUgxEVoKiErz8MrHV3vpj_eSI0_34fzGpTMyflxHE0hTqJ4Vu3xGjt5BqOPojHMRXjnQwkZOXDZAPLA91Flc08Gk9PwEtTo5CeTDbImm5g5wTMfFc2-Ech0nK_o5q-FKC-_7X2NX9qIVcZpqTTjDSjPBOF071F3k3sPUGVlaYlnGaPb0oyyFWhwfmzsTFB6XpQ2Idu6FDrpax5771-OsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24549" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24548">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1Asu3cvlskPYu7GMKcC5LXE11C2_bu3QM5JXKKq3DeazQD1X1_8R1mhA1oHBk2YLJ4cmKfIEDIAjXvHU4teJP1XLtpCAKKoS24MCF-wyQukes8Y7qx4VI5HtWIjEuBBHqDZ6U-Sx9xKISTkvbkgHmsarhn9hFxkPZH3A4W5Gj4BuH4iB8nRA7uxJGLt14zTxu3mVQVuqf0_oVzWU-IhzKUo-yKQII3K33QUXFBGtpBW1lWbXeK3dr9CB5U9fTtOBEGb_NgECFEV4PbS4zIVZ9S7ZnohQjrq7PPBP32P7-mn1PfFHBq_mTrhgfEmMO2D4v9Qi2bwzrsxL6EwC5617A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌والیبال؛ پیروزی ارزشمند و شیرین تیم‌جوان و بی ادعای پیاتزا مقابل کوبایی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24548" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
