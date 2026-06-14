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
<img src="https://cdn4.telesco.pe/file/iv3EvOwhabNKqQNzrE-bZyuzblLB216nD98c8-EDgDyXtL2-9e40AlTv1sNT4WBhO4yVP14BAUcm2ycMxrlM2_CXDcmM78befFUl-u2kqLZa7zFrHBfVUeqE1h0LSx4Y-cp5jWgBIWsgp8HAPcDfUx1b_z6E3OltQ1xWLCm_Ig0RNinTtFKs5U5VbSID5Xznj9OGl8h3_0JMpZWcJ3PpB7sVMnHAub7C7wdgXJAjsn8YRkdHbdus4loXnBwCMLIndPXo15qVRt7Goizq6GWM0CQGnZyFTb15uSt6j95RoRQZewfikxPc9M3eCMBLAXtmUH6o806DXE-0EoKC9UPoUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 225K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 09:56:35</div>
<hr>

<div class="tg-post" id="msg-66043">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cL8baVe59o_dtDaAJweGTtUoKcNa0e3NQmezyYlGBXwRFz96WFNN6hLA9mYDc4YmswPH1renR2oF9z5mAuyh-kVAjincfxlzbjsiwH6vCxYvhO3_wo6b_3e0-TIOdOTBEQ2TZLh3wzQjLhFez-BtuFYUbj5LlqyeoD-_9TRlMXaUyRbOO9kCPdFykZfvMC9BgByzE5SouoCzWqywE3aygaGESIHkrth9yaD0CX-8I8KLh1qVSWVCu75FmJ9cHzqyWHv0MvjLXupu6eEyL1pev1oMLA8Uo1DlH1zjeZKLOPsdafom4OxqSsoQyUg5EEc-ifMlNpOFMIMv8EUugRU9jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط عباس میتونه جوری توافق کنه که:
جمهوری اسلامی ناراضی باشه
مخالف جمهوری اسلامی ناراضی باشه
اسرائیلی‌ها ناراضی باشن
آمریکایی‌ها ناراضی باشن
@News_Hut</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/news_hut/66043" target="_blank">📅 09:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66042">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518512af42.mp4?token=p0Uu1A6DgbFeZQozZdmHum68oAWx0-Xr5Fr0Yjg_MEFSDqhM3jJjucVKUy1qiRH5KY81GiJ5pxVs0ERSa4B-M5ua2gpmH2Jh2BURWvsLSYAxHd4WOI2npS4pL6VfKKg1UPpO-_hMtV57TxtxP-IVew3712XTEQHzGh_vJb0ZZqNt5KPDfKZhJvdjDhqS4HKft9l-Nfipp4JDJAAv3BWemm-vKaHXPeCvoBXoMbzaG6SHH2NfY-ezJteCw4MMFVMo6bMJuBseGJsNVr9ojM_so4eLwq4Be7kdYr_WzTfY3HdJtqNNyG0SM_00RCOEm1ejurcN1jSxdYut4WJqRbgdug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518512af42.mp4?token=p0Uu1A6DgbFeZQozZdmHum68oAWx0-Xr5Fr0Yjg_MEFSDqhM3jJjucVKUy1qiRH5KY81GiJ5pxVs0ERSa4B-M5ua2gpmH2Jh2BURWvsLSYAxHd4WOI2npS4pL6VfKKg1UPpO-_hMtV57TxtxP-IVew3712XTEQHzGh_vJb0ZZqNt5KPDfKZhJvdjDhqS4HKft9l-Nfipp4JDJAAv3BWemm-vKaHXPeCvoBXoMbzaG6SHH2NfY-ezJteCw4MMFVMo6bMJuBseGJsNVr9ojM_so4eLwq4Be7kdYr_WzTfY3HdJtqNNyG0SM_00RCOEm1ejurcN1jSxdYut4WJqRbgdug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه آخوند آوردن صداوسیما داره میگه به پیر به پیغمبر اماما همشون با دشمناشون صلح کردن شما هم شل کنید دیگه.
«
واقعا بی شرف تر از آخوند هیچ جای دنیا پیدا نمیشه»
@News_Hut</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/news_hut/66042" target="_blank">📅 09:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66041">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66041" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66040">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d34_hrPG3ZOJx8v7UijVl4yyfeXUbf0SgyTNCxuAJiWBtTW0AYeAnvrG--ctf4Rv5m8IwD1i2NLxhFtuPsevf9iMLz_M3GaSUfpesES0d8fFA6WFpCU9h_WdrJ9PoU6fgR53i7bfDMQI0dVv74nWfyOQsKtNUIdWNev4EInAz2iHgNGdOgIMO2jpr97MtCcEYPScdVlppqr7_PPX5C682BiBOfhn9ChGRAqrib2Ci3IrDpY3dttMiHo6VSaQ-bltYR9qcJjccCuDB0PL9Q9Ls6B2DlxAkCMtq_5jaBesJNKB8jWi3lju7ewAOtYC4cUiGuHXFfM5Y_3XVKYiVSijNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66040" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66039">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzBmN6aosgtTC6u-YpF27yHp1am0wUt-OLHs8XACG32FUx-DG0Janzh3Z-p7f1o2oimMIcdT0tncOKJCWqZiyuY9IdGsChm8UdJ39wstR_iDOwmbUt6fPp_guoUqNV76ID8nmOvEtMioch_6jwsEzyzly9H1y0TqO6PTolNfihth9W70psIu0r5HzVEzclgS3GB_EvLvzOtDUKiBJe_7mrQmOheRByl4zd7_Dik5v5_E_LkEgPkVxONYZ6TToQpXNYeW7MEx5m-h32Fub4O1Xq4DruorzhSbJLHUQ9rm6vp1GG9_HMvKCwzm-6O4qIaHit3EOiTrKBQWJ0UnxneYJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
دریافت مدرک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_chat
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66039" target="_blank">📅 01:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66038">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d1d99919.mp4?token=UKynp_fqx8FsXAUz5h0568nJ5k3Z9vdpjYfxyOaMgA5yC0fmimIYWNXJ0xfYTLyCl8s1Wqr0y28VBY39Dn_ovVb3US8BPlaoDlWLScLlvOT1loplq0khOxwbEmdmSbMC64Bgh-k4wmekzp5yqfZGMkPsnif9HAMFRt_uMSH9RF1zMCG3Y6Uv1ZCaSpu9YXIi9AjLHXkwMkj01jsj9TzX9342SUv8kKNfQB58mL2APvGVzm_bW_-d9qcYfYAHYU9QV7D9Lh2KRSfOV6V4IaHr8PVRw-DFXvHLUvZ4bIG1GY6wKzBIjLpYncDyv9HgpG2GniLt7Laqbz4celzlYtrvzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d1d99919.mp4?token=UKynp_fqx8FsXAUz5h0568nJ5k3Z9vdpjYfxyOaMgA5yC0fmimIYWNXJ0xfYTLyCl8s1Wqr0y28VBY39Dn_ovVb3US8BPlaoDlWLScLlvOT1loplq0khOxwbEmdmSbMC64Bgh-k4wmekzp5yqfZGMkPsnif9HAMFRt_uMSH9RF1zMCG3Y6Uv1ZCaSpu9YXIi9AjLHXkwMkj01jsj9TzX9342SUv8kKNfQB58mL2APvGVzm_bW_-d9qcYfYAHYU9QV7D9Lh2KRSfOV6V4IaHr8PVRw-DFXvHLUvZ4bIG1GY6wKzBIjLpYncDyv9HgpG2GniLt7Laqbz4celzlYtrvzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
شعارهای معترضین به مذاکرات با آمریکا
اگر چیزی امضا شه، مسعود باید کشته شه
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66038" target="_blank">📅 00:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66037">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
⭕️
شعارهایی که در تجمعات امشب حامیان حکومت سر داده شد:
۱_ تا باقر کفن نشود، این وطن وطن نشود.
۲_ مرگ بر سه لاشی، قالی مسعود عراقچی.
۳_ این توافق خونیه، باقر خودش کونیه.
۴_ خایه بخور با سینی، عباس بچه قینی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66037" target="_blank">📅 00:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66036">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puV5Q5XAwmHhm7YZ4JmyFDivrvNUsqm8mAM9aME_hMTvIW9YxsM3SMOJ9EkHxEfpPEC5pR1SqVdOBrrf4wOOUNI34zy6wRLQEIoccl4FH5SCU5lR7Mf6tWuylUOxfa2PMQ1b-4VZCa5Kp6vT16TRCjCL2QWUduHj45ZX6arGbji-AezDsKupMYHISIiwQQ24UyUBr0Ef7nnvNQvx3ED3BBpWZx7Jwdf2khmDL01d2xRjXiaiCBsd2wpUwQdQ1exWugbTWJbVITmhuUUe2R6kyZLFQR6f8ZLsxGDM5Oc9EJliQS_A3FBsXBgBIBA14MgYIKMA7gVHQTBi1fgmFyTMMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ و پیت هگست در موکب هیئت محبان امام صادق (ع) کاخ سفید:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66036" target="_blank">📅 00:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66035">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLnJ1nQlzTioGx_CycgSHcOH4ts33WabHrGW3GXrDjLc9YazmqtgOk37oEkyq6E0pmm9Msj4TKks6GJmDD7qTdsMTF39T2E0SZO8l21XlEPevBUla1LzSORri9AtDXrh2cf12K-BvyViKc92yzeREO8DDXLjXgEo8H2Z-EEY7-bS_38TrZOwtkAETEzrWwfm3MOQ10rbkOiFit8XjON1P7vDFa6cPixt5WnmePc2iUebwOcc2YBRnywa_WxCpf-gp5nankP0j4YH1J3hqUbE-_i1Sa_gJi_LPN5dj8EPiOd5v1x1hjxj4LUD5ue98aULKaOGwjazCcOEh9I5IWG1Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
توهین و کنایه بسیجی‌ها به آقا مژتبی
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66035" target="_blank">📅 23:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66034">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
نبویان :
امریکا اومده به اینا گفته 300 میلیارد دلار بودجه بازسازی مملکت رو از عربستان و امارات میگیریم تامین میکنیم که خب مشخصه نمیده
اگه آمریکا بعداً بگه ما از عربستان خواستیم پول بده ولی نداد، شما می‌خواید چیکار کنید؟
«وقتی توی متن نوشته شده هزینه‌ها باید با توافق دو طرف انجام بشه، یعنی آمریکا هم باید درباره محل خرج شدن پول نظر بده. حالا اگه آمریکا بگه این پول نباید فلان جا خرج بشه چون ممکنه به دست سپاه برسه، اون وقت می‌خواید چیکار کنید؟
من بهتون قول میدم نه پولی واقعاً وارد کشور میشه و نه اختیار کامل دارید که خودتون تصمیم بگیرید این پول‌ها کجا خرج بشن
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66034" target="_blank">📅 23:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66033">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiDCS4XEsVaLco8Dq7BOJttgMGGSBQPPmfLLJNSzxp7dnDC7vjJRCxHB6JTFy_ETg0FPxd_sZWOIj1Mpl_m12zbBkS1qLSczUJ78OtDRdlKp-tzN5ri9j5PttwY24ei1TSbSzy5T_VzmfEthjkVSu4a5dQp-oF4rXOedxzfwIIEL6zj7DCeYTfFXglL4ylIL_dzHe0v1ajadODjYzr6LPZBXZPY6YSECllzt_Xxq_Pol8RV4LLaBn5eH04CEdUmS7I80jq1GWDv0z1bcyLVLG02cis4OizPweHrs-jRQMzngNRv6spSplCBybCTRSHxT1cZYHCWIwdMh_8kFb3LCDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز دفنت نکردن فردا هم قراره با قاتلانت توافق نامه رو امضا کنن
😂
...
«چقد تو مظلومی»
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66033" target="_blank">📅 23:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66032">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:  طبق اطلاعاتی که به دستم رسیده توافق احتمالی بدتر از برجام است. نه احتمال جنگ را از بین میبرد و نه گشایش اقتصادی دارد.  @News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66032" target="_blank">📅 23:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66031">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/077634d539.mp4?token=H6YerXR0B9BBc7p51OvHJDdzYK9xDPMeRqkKHQn24NTFhpJSVBCzz0HMSIbNjY05UhHFIrUueM-uTAP6V1PMEabR4cTGnPNz58qRwAuCVMByIzxaoRFLwb8x2tWm4vmfK83uIi3BqTT6g4HTHROP4OeCuXfTJErWPvjURKvrq6JOjIs_r46NiEmDB7PBXbtNXo1YFc_VYYSN9hz0c643K0vK5YcNoo6RnMGL7jvzg62rMVmLG_VEKX4RWqWkwyThIocSTX19AjgofwfI_SJsJGk2RBZ3KmT_rBsZ1HwPoSdOKTnHzRMqGxOG0nyU2mmUHeFwMJiQ_nONJukazgM2vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/077634d539.mp4?token=H6YerXR0B9BBc7p51OvHJDdzYK9xDPMeRqkKHQn24NTFhpJSVBCzz0HMSIbNjY05UhHFIrUueM-uTAP6V1PMEabR4cTGnPNz58qRwAuCVMByIzxaoRFLwb8x2tWm4vmfK83uIi3BqTT6g4HTHROP4OeCuXfTJErWPvjURKvrq6JOjIs_r46NiEmDB7PBXbtNXo1YFc_VYYSN9hz0c643K0vK5YcNoo6RnMGL7jvzg62rMVmLG_VEKX4RWqWkwyThIocSTX19AjgofwfI_SJsJGk2RBZ3KmT_rBsZ1HwPoSdOKTnHzRMqGxOG0nyU2mmUHeFwMJiQ_nONJukazgM2vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طرفداران رژیم دارن شعار مرگ بر سازشگر رو سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66031" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66030">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9383ea7d9.mp4?token=QdOjKngEYuOIUUeM_fspHg03G3RF2KicYvbh9ZUnzcs5WiILwTCztPyHgKaxb36fgH_WYqZygUrbBmlpBSt9VTs9CnhPHhi0XBhy3WYYE6YFI5kg7jmaqYh6bonXVrbwIU2g09w2jLISpjamo-hgYgOc_TLC_-ke7eXsYr515INX_flz14eSgiusJ5WfPTCI12RJ-8CTS9t1Pi5UykEUqvSmshO7d0QL1xIV4gpjN5lBojKBcPl37_tOAkmysY-iJ9FVbFvcZayQANMag9Kfg4CWBrKFfi8qJRXdwGigZgrSXTyebwV_2ZzvbPKubopg9KVOPVNJj2pNHMHu2MHS-xTBPCxT-BgJCtWf2Eh5KUsoTvrH3LobE9qshM0j8d3t_q0G0JSc_Gx5b4VCS2VKr7nUX1T1F5jY3miOeRHwQejSOvNRpkmV0-ySxmyGpDZ_0ZZtuF2ISTnKApUzzvS9G3H-W3n9wI1LwNFU7FtJT6m6mBM2NRhEkDV8I0oeAkHv9jzPUZ-QInspa2dICK5d-HXipmt1aDPNmIsU8eegp7yO6Gibdjeq2U3W3qXUeZ8PEKV_VbMpj9jBGgEPp15bdVlA5JlUzA8VvFSbfzE5RPebAEN1MIv0UeM3D7pHGG-uFHYnXNGbxj9ARiLu9eNQWP6oK9guSdcc0QsID17Y-j4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9383ea7d9.mp4?token=QdOjKngEYuOIUUeM_fspHg03G3RF2KicYvbh9ZUnzcs5WiILwTCztPyHgKaxb36fgH_WYqZygUrbBmlpBSt9VTs9CnhPHhi0XBhy3WYYE6YFI5kg7jmaqYh6bonXVrbwIU2g09w2jLISpjamo-hgYgOc_TLC_-ke7eXsYr515INX_flz14eSgiusJ5WfPTCI12RJ-8CTS9t1Pi5UykEUqvSmshO7d0QL1xIV4gpjN5lBojKBcPl37_tOAkmysY-iJ9FVbFvcZayQANMag9Kfg4CWBrKFfi8qJRXdwGigZgrSXTyebwV_2ZzvbPKubopg9KVOPVNJj2pNHMHu2MHS-xTBPCxT-BgJCtWf2Eh5KUsoTvrH3LobE9qshM0j8d3t_q0G0JSc_Gx5b4VCS2VKr7nUX1T1F5jY3miOeRHwQejSOvNRpkmV0-ySxmyGpDZ_0ZZtuF2ISTnKApUzzvS9G3H-W3n9wI1LwNFU7FtJT6m6mBM2NRhEkDV8I0oeAkHv9jzPUZ-QInspa2dICK5d-HXipmt1aDPNmIsU8eegp7yO6Gibdjeq2U3W3qXUeZ8PEKV_VbMpj9jBGgEPp15bdVlA5JlUzA8VvFSbfzE5RPebAEN1MIv0UeM3D7pHGG-uFHYnXNGbxj9ARiLu9eNQWP6oK9guSdcc0QsID17Y-j4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
نبویان: من خیلی ناراحتم این چیزی نبود که آقا گفت. پیش‌نویس توافق بازتاب خواسته‌های آمریکا است
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66030" target="_blank">📅 22:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66029">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/722ec8c49a.mp4?token=WKbVQOV8NPRNFhU_gh4ehHFFqLyuhi2jFSjDjI-AdoUFbTqv_ynY0BGCxSzaVWMhu3qUqTBcZhIWeUb4GGTiuI2yyR0Ybh6Mlr8QcnJQOZArfrTndC6FDemMtaaZk_S3VhmdXsPHAI9BH8OtKkl7YdN9uA750PEIV2WNF1tQTabZjyGGfcvtR_kPmskT4o-3ar7qu0BQj7zrMOa6LtYbVa1D8aMk52M1fGjIihM3uP-pbfEguzu4udy_1-BeLgYxkynyKWK0Zq7pzMpuYS5y0CQe5QYIEuge4UQD2_1C1NbRt3qP7yQvGn1z_fEZgA6NOox_dbjoZZZXPIfHuh1lXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/722ec8c49a.mp4?token=WKbVQOV8NPRNFhU_gh4ehHFFqLyuhi2jFSjDjI-AdoUFbTqv_ynY0BGCxSzaVWMhu3qUqTBcZhIWeUb4GGTiuI2yyR0Ybh6Mlr8QcnJQOZArfrTndC6FDemMtaaZk_S3VhmdXsPHAI9BH8OtKkl7YdN9uA750PEIV2WNF1tQTabZjyGGfcvtR_kPmskT4o-3ar7qu0BQj7zrMOa6LtYbVa1D8aMk52M1fGjIihM3uP-pbfEguzu4udy_1-BeLgYxkynyKWK0Zq7pzMpuYS5y0CQe5QYIEuge4UQD2_1C1NbRt3qP7yQvGn1z_fEZgA6NOox_dbjoZZZXPIfHuh1lXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازگشایی تنگه‌ی هرمز که قبل جنگ باز بود الان شده‌ی آرزوی ترامپ، آدم می‌مونه چی بگه، دهن تحلیلگری که بگه آخوند تسلیم شد رو باید گِل گرفت، می‌دونیم که این تفاهمه و توافق نیست و توافق اصلی در طی دو ماه آینده مورد بحث قرار می گیره ولی همین تفاهم هم فقط و فقط به بقای جمهوری اسلامی کمک می‌کنه نه تضعیفش دقیقا به مانند برجام.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66029" target="_blank">📅 22:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66028">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH_x0hfmwawJo9CP5swOBFlCYTfNBfzGeEQrWboiJNUOyReItDYXlxLO9PpYmkvlezxBLluTXRplqGZepXFVieFyUYsPHRYx_72omlJm02m1OxVyb5z_KhpJXTgh7_IRlIQA3zgX8iSO5H7z6i5lx_g77pyqp_0EuiJvyU6y1I_Wphse3RKFvY4huJ5dgajq7bHCyCgOBwgJ7Eul-3RaxWtYmEbf0BrE_SrR2MHRb5oX-Tpbkq1_aHxpTl_OE6drka7l4BejjKksekBFfPeyqMv3VRxQct4Y4pSaluXc71mowJy6sDWFlLMLpniyOU_1rpwr7bTpK0jgffMnbEmomg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فراخوان اعتراضی نمایندگان مجلس علیه مذاکرات و توافق
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66028" target="_blank">📅 22:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66027">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
رادان: هر فردی که در تجمعات شبانه برعلیه تصمیمات حکومت حرفی بزند یا شعاری دهد به عنوان تفرقه افکن با او برخورد خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66027" target="_blank">📅 21:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66026">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3933369d.mp4?token=ZLIDu6nYkYZb8qsw-jdJGVSzL-Yxd3gfbun8v1vRuOk-nC5cO1KK49pKNDdb0J721MrTEJVcnHDNdS-OXQM7N9iK4EuUdvuZoXft0cwvlTgwQVs30H3vmHrWBvTGuhUas6H4506KIq8HNCQKLZLuWA_sTL9MiJ7DtFj1XIwEu6gTQgFFV3nn6jxj9k5-FclnWLv7Lddvi6LDWr2kypBaUs-6771iUF0_DEREGVKBL4YduGEgZ-lg2lO57xJCHi1pQiGswBxB8f2XOCkzvYD4IQj2vch_xTxwMlBKMuMEsxQG6QI-d_ObTqQj1UZ2gBRq-eMFAlEoeY9wKAN-0cuD9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3933369d.mp4?token=ZLIDu6nYkYZb8qsw-jdJGVSzL-Yxd3gfbun8v1vRuOk-nC5cO1KK49pKNDdb0J721MrTEJVcnHDNdS-OXQM7N9iK4EuUdvuZoXft0cwvlTgwQVs30H3vmHrWBvTGuhUas6H4506KIq8HNCQKLZLuWA_sTL9MiJ7DtFj1XIwEu6gTQgFFV3nn6jxj9k5-FclnWLv7Lddvi6LDWr2kypBaUs-6771iUF0_DEREGVKBL4YduGEgZ-lg2lO57xJCHi1pQiGswBxB8f2XOCkzvYD4IQj2vch_xTxwMlBKMuMEsxQG6QI-d_ObTqQj1UZ2gBRq-eMFAlEoeY9wKAN-0cuD9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
در تجمعات شبانه:
عراقچی حیا کن
امریکارو رها کن
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66026" target="_blank">📅 21:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66025">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‼️
⭕️
🚬
🚬
فرهنگستان زبان فارسی: از این به بعد بجای کلمه هدفون باید بگید گوشینه
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66025" target="_blank">📅 21:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66024">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpfdvoePFgl8y2Vt0GwRq-bICO6DUS1boJiwdY2bnnf2P087G_Khp5Wkgct9VpvLhnzPEjKXQTRsk9pTymlJk-VFhx-pxdME7flM2cwg40_omwSXytAobvCavJTYaMJqZI3_c157GXuYdoFpz_5PFEIdCn0_OnRFli6EYMGMKWgK0hPnhg5vmkfN5ubJ97yvzbZ6XP_pXh7VE_LJL8IFing0R-78K7F1AhJzQ5hfCU9pZifGFKqDoMia68a0cCpKHqEsMQZYbp2HS6oM_Mo47c01aR53dZB-41NcNWb61PtW5OrWaIY1avH50c8pwhcxISoFMuVRasvT3aakWYXwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
⚠️
سردبیر مشرق: رهبری در کدام پیام ده شرط را اعلام کردند؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66024" target="_blank">📅 21:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66023">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbzwsQKhE6ycUJMU2mJUWMHvErm9BPa_NF53pdbBqmre0xYbEhyn4rf178Lapk_4kWs6g2u2HVRSGgNNvCUsjtkX1nkmJ1Xb67l2f-8WJXdvzplf8ySJ066jMGv0BlWKY9NEwmVzYr4NkhzDxeKlo_jAHkRJRvA5WTHUa6Jk0wlizcx9Hu1UhdvDzqaWxigG1RoauhfS7APWDDUfweNefrUtCTrThVFXBbVG8BXQ6kXO8mRPUOS6OFf_vFjwz5w29VHAIY2eLYN2lAibiw2jiM9mMSvxaLZi3e7EbOufF6ARRQ4juvBV-CFObAGycPuXjf834ItmITSJqpif33qY4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هلند
🇳🇱
-
🇯🇵
ژاپن
🏆
جام جهانی ۲۰۲۶ - گروه F
⏰
یکشنبه ساعت ۲۳:۳۰
🏟
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
🚑
بازیکنان مصدوم:
یورین تیمبر
از هلند و
واتارو اندو
از ژاپن به علت مصدومیت در این دیدار غایب هستند.
👨‍⚖️
حقایق داور:
🟨
میانگین کارت زرد:
۳.۸۵
کارت در هر بازی
🟥
میانگین کارت قرمز:
۰.۲۶
کارت در هر بازی
🧠
نه گفتن بخش مهمی از استراتژی است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66023" target="_blank">📅 21:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66021">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71f300a74.mp4?token=Htq_zJHsAv4Tgms94Rvr3oPtsI5DRExbJ6lSrDWn1FzacjvAsqB1kz5-1IRbMq20lMe3looFprYrg9vhw0Y4G6hvF5YrcFEZyD0_7Ua13LEfN3WZi9vDIDg_Ty_vAIRrKc50uOfg1jEw-rbwa5cly_QmEWegk0YnqdluDxuxSlmtFMBnm2Rc1HK37qQBsmoXiIs6gV2na-HASXYZVl_j8wrY5uG1VlMaPaXTnSNBBTBfpL_3oNnMmmOv1Gnr3piB4lPNVeUPp7dnmVqsWr9znCa9SO0CJ6WdQ-kCev-5su5FCUMNdBfQdvcoxrwHWoXNiz3RzTJ5Sf4twenkagC5iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71f300a74.mp4?token=Htq_zJHsAv4Tgms94Rvr3oPtsI5DRExbJ6lSrDWn1FzacjvAsqB1kz5-1IRbMq20lMe3looFprYrg9vhw0Y4G6hvF5YrcFEZyD0_7Ua13LEfN3WZi9vDIDg_Ty_vAIRrKc50uOfg1jEw-rbwa5cly_QmEWegk0YnqdluDxuxSlmtFMBnm2Rc1HK37qQBsmoXiIs6gV2na-HASXYZVl_j8wrY5uG1VlMaPaXTnSNBBTBfpL_3oNnMmmOv1Gnr3piB4lPNVeUPp7dnmVqsWr9znCa9SO0CJ6WdQ-kCev-5su5FCUMNdBfQdvcoxrwHWoXNiz3RzTJ5Sf4twenkagC5iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عربا با ماشینایی که تو ایران شده هرکدوم۱۵/۱۰میلیارد و شده حسرت برا مردم از این کارا میکنن واسه سرگرمی...
💔
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66021" target="_blank">📅 21:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66020">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هات نیوز | HotNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/news_hut/66020" target="_blank">📅 20:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66019">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری؛ ترامپ: فردا توافق با ایران امضا می‌شود  توافق باراک حسین اوباما با ایران، برجام، مسیری آسان، زیبا و هموار به سوی سلاح هسته‌ای بود، که ایران شش سال پیش به آن دست می‌یافت و مدت‌ها پیش از این از آن استفاده می‌کرد. توافق من با ایران دقیقاً برعکس…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66019" target="_blank">📅 20:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66018">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZAsukQNgkMq2xjO3zRKIJRnxeLVQCsYJwWJtwCnnkwVw0QcjS3fjUlVLkxDjno6F_mQX_PqLe0jTNw_1LrXSgHmq5d8-zDjG4DFQi_BfBAB_4yuX4pkQLXZ6E7mXRc2SVUlmXwtXcPxvinoVvPrPswjjj10pupZmYTLF3E9rppxzSdx9cxbGJb6JLxp4uGBAzlHBXOSgBnUR6zhcG-EgVOlYEYzJ0q_USlu8u4U6YPTTFCVJmi8Gl2OgXZBDI985Dgiyzm-4qShzRCiCI48b7rAqPfcEOyQAxb5fNOQ4aa2dRGonNfYcKPjzd_7uVopy9QxiKHdMhBxwaTvwFkLCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری
؛ ترامپ: فردا توافق با ایران امضا می‌شود
توافق باراک حسین اوباما با ایران، برجام، مسیری آسان، زیبا و هموار به سوی سلاح هسته‌ای بود، که ایران شش سال پیش به آن دست می‌یافت و مدت‌ها پیش از این از آن استفاده می‌کرد.
توافق من با ایران دقیقاً برعکس است، دیواری برای نداشتن سلاح هسته‌ای! در واقع، آنها دیگر سلاح هسته‌ای نمی‌خواهند و نخواهند داشت، چه از طریق خرید، توسعه یا هر نوع دیگری از تدارکات. قرار است این توافق فردا امضا شود و بلافاصله پس از امضای آن، تنگه هرمز به روی همه باز خواهد بود. رابطه ما با ایران بسیار متفاوت و بهتر از روابط دولت‌های قبلی است. برخلاف صدها میلیارد دلار پرداخت اوباما به آنها، از جمله ۱.۷ میلیارد دلار پول نقد سبز و سرد، هیچ پولی رد و بدل نخواهد شد. در زمان مناسب، وقتی همه چیز آرام است، ما به لطف بمب‌افکن‌های زیبای B-2 و خلبانان درخشان آنها، وارد عمل می‌شویم و گرد و غبار هسته‌ای را که در اعماق کوه‌های گرانیتی قدرتمند و غرق شده دفن شده است، جمع‌آوری و نابود می‌کنیم، چه در ایران و چه در ایالات متحده.  ما مشتاقانه منتظر همکاری با ایران و کل خاورمیانه در آینده‌ای طولانی هستیم. امیدواریم که این روند به سرعت، به راحتی و به راحتی پیش برود. اگر این اتفاق نیفتد، ما یک جایگزین نهایی داریم که امیدواریم دیگر هرگز مورد استفاده قرار نگیرد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66018" target="_blank">📅 20:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66017">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b00aed34f.mp4?token=sTiItmvv89s1fNxCfiTYzq1z69deuAu6EfznZbLgBCF6GPWrcQt_5lTVIZiYPdxmxl2Q__bnpb_aMJ7sitPHaQ1CRTzcfUtqBEmi9s2ihZ1jht8h3b4IdY4mZ9pOT9tmJH4myownOA_Ue04q-pNa3Vu94UGKvQlVvAoI4MjsMMTJaTqAwUfsQS5oKtMPYGockMP62WyJdLiW0hAI42LGhTdjTCcaQyO1Z0EdLpr4Sy4PIVWa8NCDnQByzSVXiF0RasNCgMgYiIaUyjyd5JijxGA1TdkjW9pdbfRb0bVtJ5dk-dRdtWFSxRUh-WIMI81WVG2TMvMF6kF48cPwmHOVLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b00aed34f.mp4?token=sTiItmvv89s1fNxCfiTYzq1z69deuAu6EfznZbLgBCF6GPWrcQt_5lTVIZiYPdxmxl2Q__bnpb_aMJ7sitPHaQ1CRTzcfUtqBEmi9s2ihZ1jht8h3b4IdY4mZ9pOT9tmJH4myownOA_Ue04q-pNa3Vu94UGKvQlVvAoI4MjsMMTJaTqAwUfsQS5oKtMPYGockMP62WyJdLiW0hAI42LGhTdjTCcaQyO1Z0EdLpr4Sy4PIVWa8NCDnQByzSVXiF0RasNCgMgYiIaUyjyd5JijxGA1TdkjW9pdbfRb0bVtJ5dk-dRdtWFSxRUh-WIMI81WVG2TMvMF6kF48cPwmHOVLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
تجمع هواداران جمهوری اسلامی مقابل وزارت امور خارجه: مرگ بر عراقچی بیشرف نفوذی!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66017" target="_blank">📅 20:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66014">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4e2f8eb4.mp4?token=swUGovW1oUVVttYLedTIIGLJCCFE2QMdEJkhVNEVKrDUSsih1tF63T-mPKsPGInY-vp9ZEP1-AE_eQID-1NdpdYaXkvk7WnoU1B_CwTmFnf6b8A3Qqd_06jgMoPEV994-1lwzg-Qvjd7peTq-YhDXeBDudaODpKNS-jTiZ4Kr1IMxLmFR4BA25zQTAZgAIy5HFF8IXTfbkTLlDDX_G13NaVfMzDo5PDlbtT3APIG8hzH7RGXob1ZrYozZyJ1rVvqe9EREHKtUTDAJ4oRKr1BaiKK9sqn2aEe0VxiDHkmGELaS0LB6qbNswU_W7CG2NUZGkXLfouvRW20m_9uRi9s7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4e2f8eb4.mp4?token=swUGovW1oUVVttYLedTIIGLJCCFE2QMdEJkhVNEVKrDUSsih1tF63T-mPKsPGInY-vp9ZEP1-AE_eQID-1NdpdYaXkvk7WnoU1B_CwTmFnf6b8A3Qqd_06jgMoPEV994-1lwzg-Qvjd7peTq-YhDXeBDudaODpKNS-jTiZ4Kr1IMxLmFR4BA25zQTAZgAIy5HFF8IXTfbkTLlDDX_G13NaVfMzDo5PDlbtT3APIG8hzH7RGXob1ZrYozZyJ1rVvqe9EREHKtUTDAJ4oRKr1BaiKK9sqn2aEe0VxiDHkmGELaS0LB6qbNswU_W7CG2NUZGkXLfouvRW20m_9uRi9s7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی وایرال شده از کیوماسا، گوریل باغ‌وحش ژاپن بعد از دعوا با دوس‌دخترش
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66014" target="_blank">📅 19:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66013">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7hlLxEYvz8x5GrrLbZsjBkUFCzYFUuYkMewqDrCUqHKIc-n6EZTUmPUad6blKLYLIJlch-hnb4aiXxQxZldCoD-8bBcVW71Nv4HL7RZk4WzyHfFpZIkkS8NHOPC9lHB5r2Y6sF6gsMd1NCHuFDfZtjqidHdCnb_NRQNuQXYok3p4jZu6s3DPEawp9HigfRnhK4S1qzrzRsXZFW0boQSJNRaB2P3RFsWdLr-aBq4IIpmG43jYyZuY72-fJLkvbUW9r4pbhHeF96UsrcSQK8bkX0NvJIjoww_FDpz9IbEGiZs_bwGho01OXvQrsVaLW17p1zn4BGSdTEWfW2Pljqn8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید به نقل از یک مقام آمریکایی:
پرزیدنت ترامپ روز سه‌شنبه در حاشیه اجلاس گروه هفت، دیدارهای دوجانبه جداگانه‌ای با رهبران قطر، امارات و مصر خواهد داشت. نتانیاهو در این نشست شرکت نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66013" target="_blank">📅 19:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66012">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xie_fjDoYUANgszsHJIXp-U9oyAeUuZnd0pn7eCJrw3r_BrqetjLJTjQTsC1JtoGmLTkNvq72huEpHc964qpWtJw-VmS76IpFISugjoDykeDCwS0Y0eJxPBy_ayEfIcHSc0yeMEiMxlnDwGbFkYjhz0SVIfJQbsAa36TjUZGk1aIic49sUqcUm0miDexXUovY8cP_VXRDhvY9_anz7xP7ZjZREoSHyP3iGzCs0xsOXOKM3DPNvKoo4211QM6jngxXpJe1PylU9Tzn-bUdmpGULv1Yx-VqiGfeYayAF6oF5R2_xbO8qJRCGn0HDTBgA-RiJx3ZM9DFNxH3O50otzc7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تجمع اعتراضی مردم تبریز به دلیل توافق با قاتل خامنه ای
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66012" target="_blank">📅 18:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66011">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
#فوری
؛پاکستان:
توافق آمریکا و ایران فردا بصورت الکترونیکی امضا خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66011" target="_blank">📅 18:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66010">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_RBDjLTBAjdhYpzW10wBx5JVhf4M2nqU5NKZfT3eNUGU0lFi9ly4Db9ObEeCMgFkYx9laM7bNU5DZG0k5Wl-9pkDcop_kL4JjG9thLsQW3oUC3vudElsGVvMIi0y7a2BAyUo8vV9wQ30IAHYgYsba06lJKNfQ32JyjNuoc07wHeS5QRRYabU5tYBaJPZii-Nac_aStTTcMPlvfhqLcLiaaQAmWOnRN3oFbGpIeSZXXUtxuJTL-nvgQU7Fu69VZ8LLC_OwAL-y5rasQpE2VlpdzElMUFzbMdIiS1hNlinLZPwUQ2dkSAgFaf7WFGc4erf1jc2hfATC_sgkKTzwgsJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ توییت شهباز شریف نخست وزیر پاکستان درباره احتمال توافق تا ۲۴ ساعت آینده را در صفحه خود بازنشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66010" target="_blank">📅 17:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66006">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fq38QXVV1aN8wYbVUI-xpzB_EAf4Y4x4nv8ju01tTWXnN3CcNRfEuXVd1oRAKz4ytdttX8iXOyXbKXUuKpZT4AnMY0i-U5NyopylBjS54PzrThiC1zp2othpmX5P_MAWhp8j5kxkuRpvzujqYshEJKsZATPXc4CXuEFxUogQ2IMLyassqCLWt56b4wNZq4RQ_9FF9Z3XYavIM4hjmybZv9ueKt2hgDVn1wnal-vKn6URTeAW0ESSivdNuofgG40RX9qbb6qxsUu1ETndMdOWMKKmbpe9iM3PtVG0PaX6Iv1k0nAhEVDWG5rMOdkmabGK-D_FndqQmFXr2E-tTTePwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0b4wAChLNbqMsqchXZwxY54nLcgeBoGXw9c3gXu9gDYisX0pu_H-MjhjMVWhCVbe2DuzcQGzYKQEwXqWbX3WYDe5IdZlapHTqlZeXEdGzSIu9yhNTqbUGkJW67nTXgLNCL5nbVms8pSt3RsipExEu6mK2UHheV9tl1Ogie1RVmWDhEU8N2Kh0N03CeoqwRJ7wUN0xqg7t1K3RhRStVBm7kut0IqxMeRo2B8BAdFq2GrN0Y6w3FXYA6BkAQTm_0XmkLs5gPrYm8FASSGtyAtaCWV0uajApROkSF08Lqr7KiGFkE7PhifLpTff8QracW8YedIF-10Vqanwc4rvsnlqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlGCCsxJyHF0lxNnB6QbXpd4SpMP6D6RYqf_bPqbhSGtdBuI81LiBpoRTu46tXudNQAy2DDmLZx4gHMpUEP3vjn8gAIPgaa34o84bsBeup7LEZNsWgxx_U44fLnjGaX7NwgV4ezNNwFP1AGh2c9tQ1Y5C0CQdNzgg0OPr8_7TIOn6lf2cEAmbtm-xUeuSjbKSvB3CimgTlEVwb8Rae1mw79g3BlMR3-q_cR-SSwndon2fIdvlHcF0-iR2wJa2nTFBxQWyKqMuf8gn86oCp35r8mRVefRD47f4N1SobaSi46Eb5pW2_DyY-F_UvR-HP1R5OXwBYi3aFGhhbKnGmPPbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6ZnSrZDfurIy-blOf7vAuJ-5jgO4Gd3_qDfQ1IZ_gjY7q3VLMx60E1_ZEFLOysLbiX_UX3Or0XcAHoNjCi5RPit_gQUdCmjRjihTOv400yDMwDQzbxrAXCYXdenUOKoXrWKcdGlvfLuyzyqU9IS0T80lzgKO5cWBpFxue-XCnjoUVPt8eSADwPaL_VnBiPnKjulE4C8LFWmUJLcrbXuUdf7k4iwJxUDPwqE3i7-hVkZ2E0y8lWjdfWX0qX7qaqyq_i-0FIKgxOIxAvN2PKNXBhA8K7oPNaWSe91XGUCl8uJc001LoBSu-HXCN2uKlbX1ZnYI3IWI4pWZkfemHXLxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جت‌های جنگنده نیروی دریایی ایالات متحده و هواپیماهای فرماندهی و کنترل آماده می‌شوند تا همزمان با عبور ناو هواپیمابر آبراهام لینکلن (CVN 72) از دریای عرب، از روی آن بلند شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66006" target="_blank">📅 17:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66005">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">از جام جهانی تا لیگ ملت های والیبال ! هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در بت ویژن در نمیره ! فقط کافیه یه شب از گلچین فرم های بت ویژن تا استفاده کنی تا ببینی چرا سایتا دنبال ترور ادمین این چنلن بیا اینجا تا ببینی فرق ما با بقیه چیه
💸
💸
💸
💸
…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66005" target="_blank">📅 17:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66004">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJC66rm8tZJTFlTzlL3TLZCOXPKhT8854SnD0s_dl0OR67VDxVu735mnlrEy41xUvcWijy4cuQauGMHI4QEp_nmvtN7XkOob2DPtuvc4BjRLEfdh0dt-Q0exRG6GKq_hQNQ_aItk6Dh7cLO_MyBGOZp14wQye3-8WywnA89h1ACG006Y1iddnETVqBKs1XcQegqnfeWF7s1T7SoE0kaJUbGn19NqBIs1mJVfpvQ7RRCN5zRH-PR_OlLCUC97R9rGdAfeFdQrsgwa1zyPU9yNq2hfPGrk1BDyHodgDpxBOiqnttEYp7qadXbgo-ejdNC_tzZegiobR-AftWiWk6eSZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از
جام جهانی
تا لیگ ملت های والیبال !
هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در بت ویژن در نمیره !
فقط کافیه یه شب از گلچین فرم های بت ویژن تا استفاده کنی تا ببینی چرا سایتا دنبال ترور ادمین این چنلن
بیا اینجا تا ببینی فرق ما با بقیه چیه
💸
💸
💸
💸
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66004" target="_blank">📅 17:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66003">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgNssTpGmiu6n_BNM62lLGwCuYQlXHithwktfSPl5GpMAkQx2eDeIwTO5o35meac9HUvw_NILz96SMXeefikaTD7k3QBbDKxnUqau2qI6id22gQZQx0oyOz3L7V_w8K3eTUOBg56FgSnKb-NFKim_-hbN7Tqe8hsTLlT6H2EBfLrhzX-vStCNh5oRVOyMZImOiL-GSkbXA51KQS6dy3P_oXopozZsV2r9DA7Q8OtvHjrLqQM2tG5nslWeh63fM1PJAuGFCI8I3YzJV0zdeWgdmZ0Zj-mqWqkaqcvqM-AnZwPgbxXfZHvHrgF_l6_2qHhMEMNOlU5H8xFosmN9xcNuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعدادی از نمایندگان مجلس به همراه قشر تندرو امشب جلوی وزارت خارجه تجمع اعتراضی برگزار میکنن و به روند مذاکرات اعتراض میکنن‌
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66003" target="_blank">📅 17:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66002">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHz7jttngGa6rqYopiVkV2b4YuRcn2Ehe528uZjVseiJb_Vbu58ycnrpwS5bnGDpY0QECELZGEzmXAstZZs_9hS7WGn_pPnVW0cbOUgqube6t1bx1BcYncjjeI7cCxS-VJGPNSBtRrx-zf0z5irTnMrMPn0UW-FyKqgTsIHLetlr7Im8Z3qSCC6j-41rL5ZvxnOP7EVAYh9wxyQdRkpFXTotnZppg544DMR6kDxis8yz8DKxsLTf6yCKwIS4A6MigSmYDf8ehnnGY4cir_szmwJoMrGG6tt1NAtsmwjTiaz-0RkYyLFplgmYbRqY0azv6B85l03wQDSqII0GEb3Gsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اواخر بهمن ماه پارسال، ترامپ مصاحبه شمخانی که گفته بود «اگه آمریکایی ها سر حرفاشون باشن میتونیم رابطه خوبی داشته باشیم» رو بازنشر کرد ولی هفته بعد کشتش ، حالا دیشب هم صحبت های عراقچی که گفته به «توافق نزدیکیم» رو بازنشر کرده
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66002" target="_blank">📅 16:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66001">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b2c6552b.mp4?token=NGPp7t2K9gBSnKSjGjVcHraTP4JEK-WNm6Adn6uv6wxce9QTgcwg3Cvmptatip-aMvu0wfhfH9FYQLxrDiMH3QzvAO2A2pX2A-60yvMfQZz6GIJWZxF1xuot0nwJA0vA64Ehj8H9zJIHv_hKi2lgIOow4q1i911e-I0aWCgEZsqwiEkGJgBL4-QPbh94fzsHImSiQ__D2R9mNw-UyFRBmmcEughtO56HLY1oN3C33YmIY6Sg53hVU-tJM9ypcnsMIg-dEM1MRHcSVkAORWZnaYjXuT4gKL5qCNRqv3mDyFebCJUPiRAsmR5pUiKV7X7ZA_WDzRg5JEIvAusjgJFhRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b2c6552b.mp4?token=NGPp7t2K9gBSnKSjGjVcHraTP4JEK-WNm6Adn6uv6wxce9QTgcwg3Cvmptatip-aMvu0wfhfH9FYQLxrDiMH3QzvAO2A2pX2A-60yvMfQZz6GIJWZxF1xuot0nwJA0vA64Ehj8H9zJIHv_hKi2lgIOow4q1i911e-I0aWCgEZsqwiEkGJgBL4-QPbh94fzsHImSiQ__D2R9mNw-UyFRBmmcEughtO56HLY1oN3C33YmIY6Sg53hVU-tJM9ypcnsMIg-dEM1MRHcSVkAORWZnaYjXuT4gKL5qCNRqv3mDyFebCJUPiRAsmR5pUiKV7X7ZA_WDzRg5JEIvAusjgJFhRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه هدف قرار گرفتن راکت انداز Tos-1A روسی توسط پرتابه FPV اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66001" target="_blank">📅 15:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66000">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSUJzjjDvwcO2TXPgBuDba25NmklK0gStI-hgnChz-hfoIgzNp_Zu1VyE3PZKVM5oIT8aPZmBR2YDAPZI1dQrYwXiabjLJ-SsbywpzWKzjJ5zElIZMNY3T3BweAQOJp6Qfmdx0zZ57U2HhoYgN3kF2QsPBxRcxyJaxgCdlQ933ZE1mX9LAXkvZRc_OdtZfh5EQMaWz1blpTcs761bh005f06IJcI-hW6M0-P3jLvSTfGiTvzt87uUq7usxo3kHxI1EdxBsx1gvLr51pNH7fV_Vc8yZleNWyhW0ZVIgZBnZJ3Hlu17xsj75xN5-WyJWcLBiFntx92gjcqZ0yoiL96qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقایقی قبل سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارشی از حادثه‌ای در ۶ مایل دریایی شرق عمان دریافت کرده است.
گزارش شده است که یک نفتکش توسط یک پرتابه ناشناخته در دماغه بندر مورد اصابت قرار گرفته است.
خدمه در سلامت هستند و هیچ گونه آسیب زیست‌محیطی گزارش نشده است. نفتکش در حال حرکت به سمت بندر بعدی خود است.
@News_Hut
﻿</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66000" target="_blank">📅 14:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65999">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
من مطمئنم که توافق تاریخی بین واشنگتن و تهران، پایه و اساس صلح پایدار را بنا خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65999" target="_blank">📅 14:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65998">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
مذاکرات فنی هفته آینده پس از امضای الکترونیکی توافق آمریکا و ایران برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65998" target="_blank">📅 14:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65997">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
پاکستان در حال آماده شدن برای امضای الکترونیکی توافقنامه صلح آمریکا و ایران ظرف ۲۴ ساعت است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65997" target="_blank">📅 14:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65996">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر پاکستان:
ایالات متحده و ایران بر سر چارچوبی برای یک توافق صلح که به ماه‌ها درگیری در خاورمیانه پایان می‌دهد، به توافق رسیده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65996" target="_blank">📅 14:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65995">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوری
؛نخست وزیر پاکستان:
ما بیش از هر زمان دیگری به توافق صلح نزدیک شده‌ایم و احتمالاً ظرف ۲۴ ساعت آینده نهایی خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65995" target="_blank">📅 14:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65994">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شهر عجیبیه! تریسام بروبچ دهه نودی  @sammfoott</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65994" target="_blank">📅 14:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65993">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
⭕️
مراسم خاکسپاری علی‌خامنه‌ای روز ۱۸ تیرماه در مشهد برگزار خواهد شد. از روزهای ۱۳ تا ۱۷ تیر هم مراسم‌هایی برای رهبر دوم جمهوری اسلامی در تهران و قم برگزار می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65993" target="_blank">📅 14:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65992">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
از امروز صبح خدمات الکترونیکی برخی بانک های کشور از جمله ،تجارت،ملی،صادرات و توسعه صادرات با اختلال مواجه شده است.
خبرگزاری فارس اعلام کرد برخی منابع از احتمال وقوع حمله سایبری خبر داده اند اماهنوز منابع رسمی این موضوع را تایید یا رد نکرده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65992" target="_blank">📅 13:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65991">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65991" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65991" target="_blank">📅 13:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65990">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoS-kBpHHhuj6ZZ8ZiG2KSRf-HIS668LgZcyTNbnmLUwvS31sht916h0I3fQVT5omp4vOa_UC9jDmIFHqNss6My2lbWWOMnTcbmIUkXA_uL_ew67QEzI9LYFYyZlNy1lKujcPdE57Nk5xjmBnDQd5hLTWrunJkWZ8vpQ3GmNtgEyiHZ_0fwkQH_REzFRSuIE9JfABp-JMZmGIWhrCvZkg4J5ySorAHe2jQCadwKc25Wg4vhXMEQUPY-SnmfVOEx31PpnATAQ19Y4jZiz-kjr0OhJgdOvZltaowZcwkDxsMOpsh5n36a9ekynP-dO_zYQlYKdlabOMl5JO-IVAjeFlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65990" target="_blank">📅 13:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65989">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5MPFz3ndWoDfNaoKO2l_bcuq9c5twpcI20-OSdy2_iacNNYyu2snqUZ2Fv3OimUTNWrtQWeiIe5gHmZYoS16GtIKvl7yH8vbaFs3CAzAJbgRLboNYPJpkkMRhN76HTUuD7Jdve--kjVyl9zoZ5Wenx6sW5aiDEa93DwVXI87UPwV4mvmNR8Ll0oNOSUKQAo1uVXYMv4MNf0owc_83_PFBfxdKS2rY7f4jSTD8DpHyXRVvY4pXqol4lCuhVURh_73W9E5UhjL4IISxmL3iWDREt2gEE3cNIXf7NyXm5dZBn94i0B02wUygcclOyNKArESUc67Ur1mEDasyUoeb5dfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
جنوب لبنان؛ارتش اسرائیل پرچم این کشور رو روی تپه العویدات و کنار سازه یا حسین نصب کرده
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65989" target="_blank">📅 13:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65988">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEHFCZf1wux2ESiABJiTXfWWgrY8pZXL1d0rYzLW-rZrxaDdT6HklYAg8Nfnk8RvEPxLD-Z07OasSC4Jy6IYchZnOGsCOqTBn4AFlLSV_odgiM0KUVgfo5SajIoWCEZkyD16hruvlqB9tUVeNLQwIbeFZBr9u_y0Ro7v2lfRg4JE9b7uk6BEoS_KYtOP1e4iKEINAi95yHrWLQ0CtJXeggKCxc92fzv0WBV1B-KGUyBz_DlXwGdwfIbe45cjI7BWJJ2D51VDYA1HJIiEGqRXHD9QV-WFZK40MXnMtyqufIAAbEjfCtXzsE8p6Tn84MovBoiop6UefMcwJvewJl7Iow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ایران تو هفته‌های اخیر حسابی دسترسی به انبارهای اورانیوم غنی‌شده رو سخت‌تر کرده
- طبق گفته چند منبع اطلاعاتی آمریکا؛
- ایران بعضی از تونل‌ها رو عمداً ریزش داده و ورودی‌هاشون رو با مواد منفجره مین‌گذاری کرده
به گفته این منابع؛
- الان رسیدن به این انبارها نسبت به یک ماه پیش خیلی سخت‌تر، خطرناک‌تر و زمان‌برتر شده -
CNN
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65988" target="_blank">📅 12:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65987">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85b34abe01.mp4?token=i7w-FdvNm_rrN-GRs3iNp0nshY1OtoEr4kP9pkB68ip7GN0wqaVzoY6shqeOk7xtOEtLYM2KM8x05ybt7RK3CYtpC5DU9Qa71lEMATTh3oR_qtlFJ-zi2vreih0VFeA0Erp4NfAB--dS31SuPdKyLqXZ2Zdjh_uJKK8OfTR-0aqE7yIs0mN0fufD7nl3NNb92qargCfkLjmb_-czBcOjkcv2YGQD-uDzeT4w4QkQC7wAvOn6qbhpfBpsSw5KcFHO3LnkEE4_mx8kdzq5BBTQ8sGCtgKQlcCujuvPMh-VdSWXkrrnyeS3BolkZVaZRiz3Hxpx-YF84f8_ZPQezxZP8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85b34abe01.mp4?token=i7w-FdvNm_rrN-GRs3iNp0nshY1OtoEr4kP9pkB68ip7GN0wqaVzoY6shqeOk7xtOEtLYM2KM8x05ybt7RK3CYtpC5DU9Qa71lEMATTh3oR_qtlFJ-zi2vreih0VFeA0Erp4NfAB--dS31SuPdKyLqXZ2Zdjh_uJKK8OfTR-0aqE7yIs0mN0fufD7nl3NNb92qargCfkLjmb_-czBcOjkcv2YGQD-uDzeT4w4QkQC7wAvOn6qbhpfBpsSw5KcFHO3LnkEE4_mx8kdzq5BBTQ8sGCtgKQlcCujuvPMh-VdSWXkrrnyeS3BolkZVaZRiz3Hxpx-YF84f8_ZPQezxZP8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انفجار شدید تانکر حامل سوخت در مکزیک
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65987" target="_blank">📅 12:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65986">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a45e16c46.mp4?token=JvZuBpucNs58jEtSg0oUCKZEhmiqrvdgWmn_i2X1FE2E_Q75mjLFB3KA6pbEjw9wsq32LrdGutMTipqpubXu_LYRHSFzPL3TmtFqsMk6PgumACGlGnUH7jl4fGl-x9kGlxKbVjuknbgCkjEOyYrwQUU6w3e7Y2kFWMn0zL_h0vCwIFxoQDtnHtndmgRu-Wi8qmrLUYKrW5RbF1uVglxjXuismYXNOTsrKIKXR3MGv5o-LiDTZ77Kc1bACuKGaTaL8hLdCayv2SnwX2V08srWZDIua3-zpsYS7DBgX5_YLUm3mLvkHynetY7h83u5qoRSNQmlAlqvuj2P--acoC0oEl5Zd6a7ZJZQg4Ah20ImIGGv0bUoTbFaivu5oXng3MMsFPojXrxoN58jCNCt5XFOWECZqg0SBlhM6NOBkfyR3LWfoDd1Qr3rACzaA5u5VhhYHNhR3PPqNGyXmWhbj_NYXVRMOSbmVqxSR6m3tYG9m8vyS1lGkE68_g_8L5JCQr4V-gtsFXNU7TjLdybOlr1DFsGd12uCemLpBXiz5buaJiVuUXGsS2jvXEFgFz1ZWg8RLrtlf4-dCowoU7YgkHI7WkCBGD6GmNOxSLiWlWmCsRkC6I-0jYlTzQkLDNo8bJal1A5NHnfklFtRvMDTDCgV9G9UvG36CqSeCkQRYsiwa-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a45e16c46.mp4?token=JvZuBpucNs58jEtSg0oUCKZEhmiqrvdgWmn_i2X1FE2E_Q75mjLFB3KA6pbEjw9wsq32LrdGutMTipqpubXu_LYRHSFzPL3TmtFqsMk6PgumACGlGnUH7jl4fGl-x9kGlxKbVjuknbgCkjEOyYrwQUU6w3e7Y2kFWMn0zL_h0vCwIFxoQDtnHtndmgRu-Wi8qmrLUYKrW5RbF1uVglxjXuismYXNOTsrKIKXR3MGv5o-LiDTZ77Kc1bACuKGaTaL8hLdCayv2SnwX2V08srWZDIua3-zpsYS7DBgX5_YLUm3mLvkHynetY7h83u5qoRSNQmlAlqvuj2P--acoC0oEl5Zd6a7ZJZQg4Ah20ImIGGv0bUoTbFaivu5oXng3MMsFPojXrxoN58jCNCt5XFOWECZqg0SBlhM6NOBkfyR3LWfoDd1Qr3rACzaA5u5VhhYHNhR3PPqNGyXmWhbj_NYXVRMOSbmVqxSR6m3tYG9m8vyS1lGkE68_g_8L5JCQr4V-gtsFXNU7TjLdybOlr1DFsGd12uCemLpBXiz5buaJiVuUXGsS2jvXEFgFz1ZWg8RLrtlf4-dCowoU7YgkHI7WkCBGD6GmNOxSLiWlWmCsRkC6I-0jYlTzQkLDNo8bJal1A5NHnfklFtRvMDTDCgV9G9UvG36CqSeCkQRYsiwa-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
خبرگزاری فرانسه:
روز جمعه، از کشف یک جسد در صندوق‌عقب خودرویی در مجاورت محل تمرینات تیم ملی فوتبال ایران در جریان مسابقات جام جهانی ۲۰۲۶ خبر داد. بر اساس این گزارش، بازرسان و کارشناسان پزشکی قانونی مکزیک در حال بررسی جسدی هستند که در یک خودروی متوقف‌شده در پارکینگ بیرونی استادیوم «کالینته» در شهر تیخوانا پیدا شده است؛ استادیومی که به عنوان اردوی تمرینی تیم ملی فوتبال ایران در این دوره از رقابت‌ها استفاده می‌شود. این حادثه تکان‌دهنده تنها یک روز پس از افتتاحیه و آغاز رسمی مسابقات جام جهانی ۲۰۲۶ رخ داده و پلیس محلی هنوز جزئیات بیشتری درباره هویت مقتول یا انگیزه احتمالی این جنایت منتشر نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65986" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65985">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ac66f6c0.mp4?token=EGMRFmORzZ9sKq8Eb9d9-rnyqltFXbq24ckiX7zYyDVJE6dUz78VgFyuQSPAGRuczQoCGfLkm2HYw1e_jEdTyGsw8yVEx2zVQby7n-c-nw3vWqtSimHrIKo3MCZYfiNZQlMkYkJtd7wBtTQt6l_fXw1HF1XzZD3XJ7auLbCpym5H9olM-MZwDj70oh9RKS81nFusGzP06ugwas-MNnIXqglEC2clpFQ-iwvHUTfpkAZ1zcleH0Xzficz4IPo-ejJhFyiF8G3dqMn7G-EARRyboHEMEieWECgOj7yW0944gCb6uITWa-uI3-BMPG-3wvHcO0b0wca-Ooh6pUG13XUcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ac66f6c0.mp4?token=EGMRFmORzZ9sKq8Eb9d9-rnyqltFXbq24ckiX7zYyDVJE6dUz78VgFyuQSPAGRuczQoCGfLkm2HYw1e_jEdTyGsw8yVEx2zVQby7n-c-nw3vWqtSimHrIKo3MCZYfiNZQlMkYkJtd7wBtTQt6l_fXw1HF1XzZD3XJ7auLbCpym5H9olM-MZwDj70oh9RKS81nFusGzP06ugwas-MNnIXqglEC2clpFQ-iwvHUTfpkAZ1zcleH0Xzficz4IPo-ejJhFyiF8G3dqMn7G-EARRyboHEMEieWECgOj7yW0944gCb6uITWa-uI3-BMPG-3wvHcO0b0wca-Ooh6pUG13XUcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند تا پسر اهوازی وسط جنگ وقتی رفیقشون خواب بود این شاهکار رو خلق کردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65985" target="_blank">📅 11:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65984">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11109e09bd.mp4?token=Zu9m3PqbuyC_KZegVOxIs_Yke3EKGl-bsxXgu8peqI91F_IR3nYbua02wgdsNOtGD4hcFilMz8sUXyrPvoQirVmLPJM_Tr77f9stPNkPtY9AMhekIGI8aIOD04ShaB2iaYo953VMJb30fQ0xX0XUj9-1gj2vxVNmnPmasOA9h0iRvEBzuEvBwb50n0s12E2vJE9cl3p9MftUVLtzfnhMbYB4fXcOgIF3oC5iqoypZzxTxVENW7rCO7ZU6c-DeG69h3aC78WCFFawOtESW8XieIT1X1A-26gIkVZoJ4rofGG2yuaSTIDuzgJnbaTOTst7WNTQ1MfMdESJUxlX9VV6xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11109e09bd.mp4?token=Zu9m3PqbuyC_KZegVOxIs_Yke3EKGl-bsxXgu8peqI91F_IR3nYbua02wgdsNOtGD4hcFilMz8sUXyrPvoQirVmLPJM_Tr77f9stPNkPtY9AMhekIGI8aIOD04ShaB2iaYo953VMJb30fQ0xX0XUj9-1gj2vxVNmnPmasOA9h0iRvEBzuEvBwb50n0s12E2vJE9cl3p9MftUVLtzfnhMbYB4fXcOgIF3oC5iqoypZzxTxVENW7rCO7ZU6c-DeG69h3aC78WCFFawOtESW8XieIT1X1A-26gIkVZoJ4rofGG2yuaSTIDuzgJnbaTOTst7WNTQ1MfMdESJUxlX9VV6xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ربات گدا در چین دیده شد
یک ربات انسان‌نما که از چندین روز بدون شارژ ماندن شکایت می‌کرد تا همدردی رهگذران را جلب کند، در شبکه‌های اجتماعی چین مشهور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65984" target="_blank">📅 10:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65983">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a77f6aacbc.mp4?token=XOVQxUgMK_59hX94F4n4Qnqas2vcsxV6v7SU-L5zCCxtU0CLCiFA6q_HbBuBfKn8pCVpZBYRYp9Rx3UTa7VYkOpUh2WhSSWkOi_JrmBNYsSjIsrPpHkLtnoQbnjgw7zjzj6ilGdpk120BYYzV4OmrfFRdVh2yii84hlDxaF9_XthArZCODMXu-hoNlZoKtdYXGAaRuPqxvBYempJ7tUb6CjLrY9g49_qIJNzr0o4fz1O4BpXybGAGH9iFiHgLEnaogwrhNOZhQYE1skBjcoAX1IltQAUU5GObjKijKCyfzg6m0wDO2ndJi_7Dz-RjtpA9SLuqgUE7xA73jjml8omNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a77f6aacbc.mp4?token=XOVQxUgMK_59hX94F4n4Qnqas2vcsxV6v7SU-L5zCCxtU0CLCiFA6q_HbBuBfKn8pCVpZBYRYp9Rx3UTa7VYkOpUh2WhSSWkOi_JrmBNYsSjIsrPpHkLtnoQbnjgw7zjzj6ilGdpk120BYYzV4OmrfFRdVh2yii84hlDxaF9_XthArZCODMXu-hoNlZoKtdYXGAaRuPqxvBYempJ7tUb6CjLrY9g49_qIJNzr0o4fz1O4BpXybGAGH9iFiHgLEnaogwrhNOZhQYE1skBjcoAX1IltQAUU5GObjKijKCyfzg6m0wDO2ndJi_7Dz-RjtpA9SLuqgUE7xA73jjml8omNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ بعد دیدن این ویدیو از مسعود فهمید جز توافق راهی نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65983" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65982">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vibOD1SNf88QPYZMYuASHyoq7ha0SYGhHDoUSoVuuv8byUbjDkac34N_H62bC1yhW0Nq55l2hcqXV1rmIxtGD0thho7cz0HEx6b5c9z_OfUDHDcquHwADOKPSdoDifHr1SlSi5fJ0xVVOH2AyxgVAxEbHqkCejMnBftnmzwK2yqLMkyJTdOGKzC-gaox0Q4g83CnDqvBQhbCDw2K83ZDiRBEEJBUy6ax64XR4jlyOlKK30kS_TD--IQWAFWtigTNc9n85pgDP1x9NYydMrymnnLnw47bxYgMC6tuWfjbiY5HqOrODhIf9RMTVd7NMzE_c8P-piDX_Zg7UU7XxndPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام:
ایران چندین پهپاد تهاجمی یک‌طرفه را در تلاش برای حمله به کشتی‌های تجاری در حال عبور از تنگه هرمز به پرواز درآورد. نیروهای آمریکایی در ساعات اخیر همه آنها را سرنگون کرده‌اند، در حالی که جریان ترافیک از طریق تنگه بدون مانع ادامه دارد. این کریدور تجاری بین‌المللی همچنان برای ترانزیت باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65982" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65981">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65981" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65981" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65980">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=X2HPk3aQ2rNOKEJjmi0azmiBQTyOM2EbXa5qPxQLY9txJXwD2xufKqgZlD7H2elwM7_i5ljXwEk5h0vD3M2zm3dOl6UivzmaAg-ulJPkIm2dRc-zZ5xgxekmWUW3VlP-4AxdkcJIb9xC_zbGglYgphKDkBYicf1Z8iqOBYxotz3CsiBZp5uiDCebZxn1DjzBEgwHRm3B3JuLCqbMG5fLG7zPw57lVL2GBFb4U65J5RB2YDt3pxm54pX06OsZdCIvHtAJOf9SbpQsygnc0KA3GArLWUU0IEmAqoVx5XQS4_ua1Bc0fLgwQnkictll1jcGhjPa6jHAGsGYgackTaWcSm192mt4jqCEqx6Ed0tVwLP9qDhCpzFlZmUHk9AOT-9siBC6Jdp-VQLtK8fLlxUtPtbHT67ZWZ23-PUDy7IFfgjQRzbKOAhBCTgHvhgL1FDz54BcP2GpZEx14a0h1AfKwiQEX9CNJcvA0GMun78gWjT2n4h_e3j-0GxwR7Te6meNdRV1BkGxmId6c9aekceAuRp8aQO8o_67gQnGJXoGkVwbP5RiV3tudmpNEKIXyLuTVFyzrqNRj4zbSLrfvVQA37m44u_SmdLiHFCSiB66WGrqR8Aiu_lKza1iytgIXVZm3DB8kaQKMgTQpnKate5jxQeUGzORK4q2ESiO6MOZdoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=X2HPk3aQ2rNOKEJjmi0azmiBQTyOM2EbXa5qPxQLY9txJXwD2xufKqgZlD7H2elwM7_i5ljXwEk5h0vD3M2zm3dOl6UivzmaAg-ulJPkIm2dRc-zZ5xgxekmWUW3VlP-4AxdkcJIb9xC_zbGglYgphKDkBYicf1Z8iqOBYxotz3CsiBZp5uiDCebZxn1DjzBEgwHRm3B3JuLCqbMG5fLG7zPw57lVL2GBFb4U65J5RB2YDt3pxm54pX06OsZdCIvHtAJOf9SbpQsygnc0KA3GArLWUU0IEmAqoVx5XQS4_ua1Bc0fLgwQnkictll1jcGhjPa6jHAGsGYgackTaWcSm192mt4jqCEqx6Ed0tVwLP9qDhCpzFlZmUHk9AOT-9siBC6Jdp-VQLtK8fLlxUtPtbHT67ZWZ23-PUDy7IFfgjQRzbKOAhBCTgHvhgL1FDz54BcP2GpZEx14a0h1AfKwiQEX9CNJcvA0GMun78gWjT2n4h_e3j-0GxwR7Te6meNdRV1BkGxmId6c9aekceAuRp8aQO8o_67gQnGJXoGkVwbP5RiV3tudmpNEKIXyLuTVFyzrqNRj4zbSLrfvVQA37m44u_SmdLiHFCSiB66WGrqR8Aiu_lKza1iytgIXVZm3DB8kaQKMgTQpnKate5jxQeUGzORK4q2ESiO6MOZdoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65980" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65979">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkHa4U50mR30D3tRsqiOUcYJymVv9CceOjzwR7V86lEdHzztQRCe5enjAGfEbKCQa8qC0fO2Hc6Vvv-8tMPUwgSzoZ52je5__kfqvUWtbcOh9EOEaKr5QSCF-OFdBuc8V0ZBDFJsRiglItmLrMPzbrbvunywf76BYez3AuyeiL6DsjJBv9YqseJFFOMp6LzBF64a18Ola02cLL92MnxeofUYZ208u7SKoRF2EscWFNnqegKHtY7yCa_sZhEduSha0p1fv-xI2M8DDYWykGI8vzhtaARBW9qEaGfyvonQzIy32XFTWuQQPyRwNWErHTBanvyZfypbE9jCivD2XZ8vLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روح الله خمینی:
اگر آمریکا و اسرائیل «لا اله الا الله»بگویند ما قبول نداریم چون که آنها میخواهند سر ما کلاه بگذارند
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65979" target="_blank">📅 09:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65978">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b92693abb1.mp4?token=J1hEKNEMPxhDBqbyYasBXu6S373QibiKaxheklC9Jt6KpmaOnKO8I1RvSK2Ush0xE7m1BUXlZMznsXn3ANHTEDUgTTH_k8Z5a1i5rqipdnAC7hMR5jPtYnpDPoKu9qwvRbC1Y5UAB9BMZ7-LF_hMfQ6C78QmDdhYOTUmZW_z9ZCbk07emgn4jFoPN1WgR7HVq-lpBbGiDsuhcsI-CJqAbpxtPGj2DJzqL69r9pRIJIGc02EmD9y7w9gvy_avar1uG-OodbjKoRNOyZgd16lk45QiLV80K4rH7BRLruCQlgmi-Hwfp4y4qk92Yh5V8Vx5FQDFmyFuSgQYCBouKDTgrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b92693abb1.mp4?token=J1hEKNEMPxhDBqbyYasBXu6S373QibiKaxheklC9Jt6KpmaOnKO8I1RvSK2Ush0xE7m1BUXlZMznsXn3ANHTEDUgTTH_k8Z5a1i5rqipdnAC7hMR5jPtYnpDPoKu9qwvRbC1Y5UAB9BMZ7-LF_hMfQ6C78QmDdhYOTUmZW_z9ZCbk07emgn4jFoPN1WgR7HVq-lpBbGiDsuhcsI-CJqAbpxtPGj2DJzqL69r9pRIJIGc02EmD9y7w9gvy_avar1uG-OodbjKoRNOyZgd16lk45QiLV80K4rH7BRLruCQlgmi-Hwfp4y4qk92Yh5V8Vx5FQDFmyFuSgQYCBouKDTgrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی خامنه ایش رو میکشن، مقاماتشو میکشن وتحقیرش میکنن بعد میزنن تو سرش میگن بیا بشین سر میز امضا کن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65978" target="_blank">📅 09:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65977">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65977" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65977" target="_blank">📅 01:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65976">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9U6zqCPNf1MpekKeH-7_waQXIpN4v6K7yPwu8JlL9wRk_WOFhLl-c74ClSFLvKjrB8vczdXDFe7bBwn9oi0blcgirNsD86kdDlOa9tkOs2c-65a-8PRYIScZtnVbzKz_izmSJslC04nCFMsAAQIfrHCV3taW-NuOmdKt5Ezo56TzxacXxieNhFOPiEtniloxjZn0CayHMljynU04QMb_m-2L2ROuNL-dAmwYMfgI3d6Dp5V7P1wB5_Nma9UbCG0aNFEXhhGWlQ0nywA9lHAU0ccgr_Kx92OCG76GK47PfKsyq5IPFrNTAYPjq3kTvbTsCfyH3TFnmmm3fKKWJfeIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65976" target="_blank">📅 01:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65975">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6u3MldfbZRHzQA6Qk8ZEjDfmwoL5zKFChtshfvUhK0PJDrvjlYIPOoUxAFDtK81oYAiqac4Ty3rFtFimP5ECa3yzLTWhxE1uobNy1YQKfm_l6GEPeXLD7X7X1AINxVCA1XH-8JVdqZqSsS8wJw2PYaLjTXYictodxNtN9FEmlNDA2nsspKkWZPgRU242qkZSuV4NV4Dn2e0IXRPpE383C7eLIfwOkrSm3xmCf_j9yZA56rLs5OTkBOzYsIuR3PEjr_AllbLzg3aMqXIs-uaitKBuiqFkoBNNGhqBOxDaQhQZsDCJAuXva7fhHQjeIvhzb5sGU_jDbYHjolrsngr9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تندروها گرفتن رو قالیباف
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65975" target="_blank">📅 01:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65974">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
سپاه:
کشتی هایی سعی کردند بدون مجوز از تنگه هرمز عبور کنند و مورد هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65974" target="_blank">📅 01:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65973">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJl8vS8YcRY5kavdRJ72sII447lshqBSXR_y4QKywc6vE2hWGpfbeQGVeXPAUxGFuLiaHCvZ8tG5BxCZtaLhzfVp0J_seAiyVyn-RwKJ92U2G9czQGQRIqe61KfHNcAcF4k8jmF7I7itZGiWWpQ-Clmuen6RZvc5TI5BBj54PisgR_wYOeOaVgFN5JIozJqPJYKMZEYBAPEbR4PF1PeJ2nPFZEwXaZ3EUoQrW8DZ0rZfw8HujdC2EcMbTOSE02LheF-FVerp3dEN8uB99S3zoXNVi_sdBmEHQzuEexfp-z05DA9rTS6gmA4rePpcGfKoGY0U4HO1wRugaTd4nnSSJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برزیل
🇧🇷
-
🇲🇦
مراکش
🏆
جام جهانی ۲۰۲۶ - گروه C
⏰
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه متلایف
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
- برزیل پرافتخارترین تیم جام جهانی با
۵
قهرمانی است و در همه ادوار جام حضور داشته است.
- برزیل در جام جهانی ۲۰۲۲ از گروه خود صعود کرد و در مرحله
یک‌چهارم‌نهایی
در مقابل کرواسی شکست خورد.
- مراکش در شش دوره جام جهانی حضور داشته و بهترین عملکرد این تیم کسب مقام
چهارمی
در ۲۰۲۲ می‌باشد.
- مراکش در جام جهانی ۲۰۲۲ با حذف اسپانیا و پرتغال به
نیمه‌نهایی
رسید و یک شگفتی بزرگ خلق کرد.
🧠
اگر دنبال جبرانید، یعنی از مسیر تحلیل خارج شده‌اید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65973" target="_blank">📅 01:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65972">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
نایا خبرگزاری عراق: شنیده شدن صدای انفجار در قشم و سیریک  @News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65972" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65971">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
نایا خبرگزاری عراق: شنیده شدن صدای انفجار در قشم و سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65971" target="_blank">📅 00:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65970">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=flg5GIHAEQEgft9EkK5JpvZkQuRLOatmcSbzemx9ZZTT1zoWHbZB5ASCkRTqzG7w38c41Ah71Vm9upV1_BB-5jAYqIWp_WgJDaWrlxNGoltf4W3dqc46qP9df_sEWLouaOwWKp18Mppb4Kh-ZpHO0zNMiaLtMgyoQAppbJ76SAP2u1rxb9hYo2K02iPJTFZl_5QMPD7tnc9c2noMJWM7s4ji0X63KqATH7zGbhCquX84MR6na7K5dIGiiDkriTfY6QQJTd2VAjEtB4V0kjVkz4-kH2Ld3Gj3wnRBonkt-1k5wYdJTD9yrPfPw7ZNrCs6OgagJSVX6TiKtfy_JuuxNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=flg5GIHAEQEgft9EkK5JpvZkQuRLOatmcSbzemx9ZZTT1zoWHbZB5ASCkRTqzG7w38c41Ah71Vm9upV1_BB-5jAYqIWp_WgJDaWrlxNGoltf4W3dqc46qP9df_sEWLouaOwWKp18Mppb4Kh-ZpHO0zNMiaLtMgyoQAppbJ76SAP2u1rxb9hYo2K02iPJTFZl_5QMPD7tnc9c2noMJWM7s4ji0X63KqATH7zGbhCquX84MR6na7K5dIGiiDkriTfY6QQJTd2VAjEtB4V0kjVkz4-kH2Ld3Gj3wnRBonkt-1k5wYdJTD9yrPfPw7ZNrCs6OgagJSVX6TiKtfy_JuuxNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صدا سیما: هک تصویر انفجار اتمی در تلویزیون، سیگنال آمریکا بود
!
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65970" target="_blank">📅 00:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65969">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060800d75a.mp4?token=SBO1s_ujv9r-grRNcJ0tRa2xkEQuLR44PFOrMeltEKcLxMEbC2pVo2qPKNk0XoAcDIDUjFw66i4w_tuZN-kypGGQXw22ptHQhkdILuYl8AfG2Nz4iXbCQNoD9ij_DxMh_pZU_tU8IET8l93qLjW06STs2g4Ao1maDKTMM4ER15y4xT0WuX8Mx2jQ_eTVdG2RDJ8x8IKjVjxicWIz0a6pe5olQ6DP7GznrxoMOwUh-YWzc0Y14_wK1yYoK85Dj--_TlzSjTGHexlCAx-8bfMQDn0DEWF-b1vFp-0sl7jQCTRWWX_se_rxJxT7XA7LsvYs4TfgTVZ1o32c17poBDUGlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060800d75a.mp4?token=SBO1s_ujv9r-grRNcJ0tRa2xkEQuLR44PFOrMeltEKcLxMEbC2pVo2qPKNk0XoAcDIDUjFw66i4w_tuZN-kypGGQXw22ptHQhkdILuYl8AfG2Nz4iXbCQNoD9ij_DxMh_pZU_tU8IET8l93qLjW06STs2g4Ao1maDKTMM4ER15y4xT0WuX8Mx2jQ_eTVdG2RDJ8x8IKjVjxicWIz0a6pe5olQ6DP7GznrxoMOwUh-YWzc0Y14_wK1yYoK85Dj--_TlzSjTGHexlCAx-8bfMQDn0DEWF-b1vFp-0sl7jQCTRWWX_se_rxJxT7XA7LsvYs4TfgTVZ1o32c17poBDUGlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
گفتگوی عراقچی هم اکنون شروع شد.  @News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65969" target="_blank">📅 23:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65968">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
عراقچی:
محاصره دریایی آمریکا اولین چیزی است که در این توافق به آن اشاره و تاکید شده است که باید رفع شود
دارایی‌های مسدود شده طبق یادداشت تفاهم اگر امضا شود، آزاد خواهد شد
هیچ‌یک از دارایی‌های ما نمی‌تواند مجددا مسدود بماند
برای جبران خسارت ایران طرح بازسازی در نظر گرفته شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65968" target="_blank">📅 23:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65967">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
عراقچی:
به زودی ایران و عمان بیانیه ای مشترک در رابطه با تنگه هرمز منتشر خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65967" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65966">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
عراقچی:
به طور قطع تنگه هرمز به شرایط قبل از جنگ باز نخواهد گشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65966" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65965">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
عراقچی:
پایان جنگ در توافق همچنین به معنای خروج اسرائیل از مناطق اشغالی در جنوب لبنان است و ما این موضوع را صراحتاً به طرف مقابل اعلام کرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65965" target="_blank">📅 23:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65964">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QREeMIMfIQNj_w51WSN8fX6arBw3CCJrotVKX6A6fOQxtbmYkVS716RPp9PN-xN7hMeR_VokB5rZo2Pa-fuFMeDAYVpMhbxfRvLWI_8KhmRud2-SRGVDJn0GlIlFTIxWUP6IQSqx6gOT6nAtFh1TDTZflZeN6IcBzsUlVUaFzsCMP2Uq18bB7i9TLjrBXDFH9zPMD5R30Us1qHUVIuAlha5CqhdwDRPvpqdwssQI6d6A-SnGW-jasMagdA4JMbUS4wrr6pVX5i5wA1qzcjrt4k6uTOLWhzz0u11RB8kIq7akh41DmGerHZKqjpG4F2ctuhmyaqZAlfc6TEE09qaQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
تعهداتی که داده شده باید حفظ شود. نه اگر و نه اما و نه بهانه‌ای. برای معامله نزدیک پیش رو، راه دیگری وجود ندارد.
هر چه بکاری، همان را درو می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65964" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65963">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
نتیجهٔ تفاهم یک یادداشت ۱۴ ماده‌ای است و وقتی نهایی شد تک‌تک آن را به مردم می‌گوییم.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65963" target="_blank">📅 22:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65962">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
عراقچی:
ما پیروز میدان هستیم؛ مقامات خارجی به من می‌گویند که ایران را این‌گونه نشناخته بودند و ایرانی‌ها شگفتی آفریدند و با قدرت بیشتری از جنگ بیرون آمدند
من می‌توانم اسم ببرم که کدام مقامات این حرف‌ها را زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65962" target="_blank">📅 22:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65961">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
هیچ دوگانگی بین میدان و دیپلماسی وجود ندارد و هردو در یک‌راستا حرکت می‌کنند
به این ۲ رکن، رسانه و خیابان‌ هم این‌بار اضافه شد و ۴ رکن باهم در یک‌سو حرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65961" target="_blank">📅 22:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65960">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
همهٔ ما مدیون تک‌تک نیروهای مسلح هستیم.
همین‌طور ما مدیون مردمی هستیم که ما را تنها نگذاشتند و هرشب در خیابان‌ها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65960" target="_blank">📅 22:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65959">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
عراقچی:
دشمن تصور می‌کرد که بعد از جنگ ۱۲ روزه، در جنگ ۴۰ روزه می‌تواند ایران را تسلیم کند اما با مقاومت جانانهٔ مردم و نیروهای مسلح ایران مواجه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65959" target="_blank">📅 22:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65958">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
#فوری: طبق اعلام زیرنویس شبکه خبر ، عراقچی تا دقایقی دیگر مهمان این شبکه خواهد بود  @News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65958" target="_blank">📅 22:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65957">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
خبرگزاری تسنیم وابسته به سپاه؛
حزب‌الله: لبنان نیز شامل آتش بس میان ایران و آمریکا است
«حسین الحاج حسن» نماینده فراکسیون حزب‌الله:
بر اساس آنچه از سوی مقامات ایرانی به روشنی به ما ابلاغ شده، لبنان نیز شامل آتش بس است.
بر اساس آنچه مقامات ایرانی به ما ابلاغ کرده اند، اسرائیل از خاک لبنان بر اساس این توافق عقب نشینی خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65957" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65956">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 450 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری عالی
✅
مناسب برای گیم و استفاده روزمره
✅
تحویل فوری
✅
تست رایگان قبل از خرید
❗️
پشتیبانی 24 ساعته
📣
کانال رضایت مشتری @kavianivpn  جهت خرید اشتراک پیام بدید
⬇️
…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65956" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65955">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEIrY9NPR8IFrP4DMtt-4y8IQz53kQQGL53j6Uar4Pl1wWWoTFh3mUSP1c8ldbzcrjIWkvUf7fBHtXDcMbdWPYx-vV_P7cMZl7uIfJQa2qk_iRnZr23MjjicReF-m_vOvbL37qd3RQuYybcqfBfS5_0RWi-hIo2uOwGJxSUjY1NnLcPXGIEvTM5z087uwI6gCqhfKJzryyS21yG8nc7Ipjwr2Ga4acHauBVvJhKGsaE3-z1LPrjHpP91Q6D1_4_SQQKOHoXzw7jLYJvTHUziowRDSpA9iLmtT85SfBbXadV2mBpZ6HJ6n21fvbB-XPCKhM9PqiVZJKE0MGiTBai27w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 450 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری عالی
✅
مناسب برای گیم و استفاده روزمره
✅
تحویل فوری
✅
تست رایگان قبل از خرید
❗️
پشتیبانی 24 ساعته
📣
کانال رضایت مشتری
@kavianivpn
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65955" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65954">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
کانال 12 اسرائیل :
توافق قطعی است و این به نتانیاهو اعلام شده.
ترامپ از ایران خواسته به صورت علنی درباره توافق شفاف سازی کنه و هشدار داده انجام ندادن این کار پیامد هایی رو به همراه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65954" target="_blank">📅 22:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65953">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
رویترز: امارات ۳ میلیارد دلار از دارایی های ایران را آزاد و به آنها تحویل داده، این اقدام تضمینی بوده در ازای اینکه دیگر به این کشور حمله نشود
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65953" target="_blank">📅 22:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65952">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brw5vt3p9wsbA2EQuWqpUR30HddTeGdItAMigsXZ9nkoaYOLz4N4TGs6neAkshraCmneTUr8zkKCjbYirIVumVV6c0BdvlHGmsvOdRXE_FgK8HnUIkLR998dArcDm-tEUVQ31yu1UrRdqGfH3j-k3mZT9rSmBm5_wgPd2UUI6GyBXBosuPMLxFzdNHp6kDuel4DvR9ihCVQb2ZAxIr4mZL9Bzs8vZ4WnNYrg9f4qDy8LEfs-IbOO8HDjEuMrEHPvsdJOEiTtJ6TXF51rbp8U4SO9eN_7OAvhXHmEZv7_YuRFPWIduSevE9t9nEFZSPCU8DKOrg2SFbVP7JlTceBpbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#
فوری
: طبق اعلام زیرنویس شبکه خبر ، عراقچی تا دقایقی دیگر مهمان این شبکه خواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65952" target="_blank">📅 22:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65951">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3BY3wIa9owI560SiGfT2QxshLcwDZ3CJwwewpONHzgdPZ0DdQvGmf18gE_qmZ_SHWJltnR4JjeGOZDIF-clf018xURrY7GzVtqUFfFwTJsnF6h8WezMlywhr0XX8I38gsufWA1ey54ia5gJWB_WJBeRrFZsw9zTRsK3bm3xNTIgXW7Npk_5XI-P6-IzY25Um0lTSvTurtYrg315Zkf1zz9c3yzATl3EGENnHtAI4BWlGCXJlQ2UR0UaVNvf9f8eV1czmlpKS0eOOePCJ1pLvcLdyIkH_NP35iDds9gMIlqVCmVxWcVM78JhiDAleL-lUWlgAgNNNPn2SuUhjEbDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا به شیرمردان سپاه اسلام و حضرت آیت‌الله العظمی سید شیرمردان حاج آقا مجتبی حسینی خامنه‌ای، خوب دارین کیر می‌کنید ترامپ زن کصه‌رو #hjAly‌</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65951" target="_blank">📅 21:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65950">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1zPFDSfnJVsVPGORup6fc_csx4tpxO5tyn0RzmdQSccyazvpBOglqhkpWANfmWK6-HI5RF4VZqFxp08VRf-2PU2PUgJkq4Oa26c7Y38NzeTgJaZGOnJC_praaSYZJB8T9nD26_8BvB3-9C_ubMn4bCqesP7kP1lB9AJ7u38tJtLpohFCl2FX3Zw6VkF97CkCwQTdc_yHVQWs3PkQdBZLBiuOz-0Q5u4pLHaiKew6i4QQ257IcKX1vQUW-c9AOon4YerHU6KJLzrlEFzWDV_ajr5OX1DcEh2XXnwIKi5OxBn0YcYJxe4k0Ud1DnFZMp3SEpbYhBdnP7bDJ98vyuH_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:
طبق اطلاعاتی که به دستم رسیده توافق احتمالی بدتر از برجام است.
نه احتمال جنگ را از بین میبرد و نه گشایش اقتصادی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65950" target="_blank">📅 21:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65949">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
الحدث:
وزیر خارجه پاکستان امشب عازم ژنو میشود
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65949" target="_blank">📅 21:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65948">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🤖
رایگان پیشبینی کن؛ جایزه ببر
🍸
درسته! کاملاً رایگان می‌تونید برنده بشید؛ فقط با پیش‌بینی بازی‌های فوتبال، بصورت کاملاااااا رایگان میتونید برنده جوایز ما باشید
💸
جوایز هفتگی پیشبینی رایگان
🥇
نفر اول ۱۵ میلیون
🥈
نفر دوم ۱۰ میلیون
🥉
نفر سوم ۵ میلیون
🛫
…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65948" target="_blank">📅 21:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65946">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_hFVz9onRLcpcVFt-MXrhR_qw7GqL2d8EO0AfiCoICpLgoGixiW9cyn65DUW7HQBB10OjiS0j8chCXMxW-A3wbQz56LXoeJkBYhACtR3SSkKkLbBpGjtIZ7vtokIrbrmMvwI55lXVN2aB9hKBPEHYBrDCHLub2ZCA6rxT5z5zktDYi20XYaxkd2Ay8aBMfeuIoDJ_-U1JmlEFCUVIZGckPOV6fuwAtzsnJ8WAaSiNmeVT5U1yOdIH_idte6ZR-bK4s1ZowFujNr7jLN6R0DyOFK-6TwAvzsGkt4jJxK-Rg95GYKJEu3DkaAWsgwHCX787cUCJHoxc8v_NZz0u7HHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
رایگان پیشبینی کن؛ جایزه ببر
🍸
درسته! کاملاً رایگان می‌تونید برنده بشید؛ فقط با پیش‌بینی بازی‌های فوتبال، بصورت کاملاااااا رایگان میتونید برنده جوایز ما باشید
💸
جوایز
هفتگی
پیشبینی رایگان
🥇
نفر اول ۱۵ میلیون
🥈
نفر دوم ۱۰ میلیون
🥉
نفر سوم ۵ میلیون
🛫
نفر چهارم تا هشتم ۲ میلیون میلیون
📈
۵ نفر از اعضا به قید قرعه ۲ میلیون
🏆
فقط پیش‌بینی کن و برنده شو
👇
➡️
@PishWin_Bot
➡️
@PishWin_Bot</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65946" target="_blank">📅 21:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65945">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e7da6863b.mp4?token=ZblEPTsoxTJA460_U9HFdr03ej-lLXdkoKK5x_b_MbIhYxSK2KDrJK26Dqfox3X4aCvHDCMsh8tdoE9Xv7g-movnRCdOICC7TkiHUAbwBzasZ3hzScydyFW1xR3Rcw0JBqhUiMC478CB-52Bm5kIjNntj7N5RCy0KKNKeweOrxNFMrheLtQfFOkHNSEsiWMcKfRo2GcqnQ6jvpDZDqITIe6bqBQ-f_4-gSKxX0mnGFhnF1w_lYp6Pq43lGz7QEsgcKoE4nye2NpX9z8oVT3f4oozZEM2QUGYbAYi6ciqcK086Uep0-y9VWYjoQ_oylkcYjtmc6c6dK08EhYGo1A7Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e7da6863b.mp4?token=ZblEPTsoxTJA460_U9HFdr03ej-lLXdkoKK5x_b_MbIhYxSK2KDrJK26Dqfox3X4aCvHDCMsh8tdoE9Xv7g-movnRCdOICC7TkiHUAbwBzasZ3hzScydyFW1xR3Rcw0JBqhUiMC478CB-52Bm5kIjNntj7N5RCy0KKNKeweOrxNFMrheLtQfFOkHNSEsiWMcKfRo2GcqnQ6jvpDZDqITIe6bqBQ-f_4-gSKxX0mnGFhnF1w_lYp6Pq43lGz7QEsgcKoE4nye2NpX9z8oVT3f4oozZEM2QUGYbAYi6ciqcK086Uep0-y9VWYjoQ_oylkcYjtmc6c6dK08EhYGo1A7Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهباز شریف:   در بحبوحه تلاش‌های میانجیگری فشرده پاکستان، ما کاملاً از کمپین بی‌وقفه اطلاعات نادرست که توسط کسانی که می‌خواهند توافق صلح را خراب کنند، به راه افتاده است، آگاه هستیم. گذشته از این سر و صداها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65945" target="_blank">📅 20:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65944">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Raamkl0DQsP0lj2KPmtWFQ_uwjIt1P60k-zwo6KRD5503wSrQ1l3GWcuoknl2RTBVuLcO23Mqdv0QXrO0ZjqH1z2XIdUlfzly59MxYIBmWMXduOfaM94bEmJzgKEg_lt0GxyUR_1ejOUhKZQvIEhYyVtuabCJvkaKt1L8lPGzo60wbs2tGHNujer4RxrjlIJ0EhT0PqO_wltav3mZajq5U5iEVrnhAflm47w1qwB6cbDcELt4XwT2IUjiEC8TtNNMgGB2u5ptmDSEOp-DBrNvDx3_KpX7Uwizyn_hBH8ioA-tK3uztX4GuIERfOYkkgdeufG-RmNjcx3LWhP2zJWqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهباز شریف:
در بحبوحه تلاش‌های میانجیگری فشرده پاکستان، ما کاملاً از کمپین بی‌وقفه اطلاعات نادرست که توسط کسانی که می‌خواهند توافق صلح را خراب کنند، به راه افتاده است، آگاه هستیم. گذشته از این سر و صداها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق توافق صلح حاصل شده است و پاکستان اکنون از نزدیک با هر دو طرف برای نهایی کردن مراحل بعدی همکاری می‌کند. صلح هرگز تا این حد نزدیک نبوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65944" target="_blank">📅 20:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65943">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58b6a7c560.mp4?token=JuedeYX03sg_bXdi5Nbd4dFyahAjUouMrFxWoocW1kv2fi07zTzfmEe6chJ0odERdH6i0nAapLuHdAdjOTGEOTTGzYGcr_lnS34ELknXohu19JWgT4dWcu-6A7H0De5TeH95S0LMDD5G7JPNba-2OGu1SFcOssuh-DTK4_uk7XAPZxI8RJDY74MZdHnDv7XjNk_uqjal4-1Me8yqgCF_ChgmnkxlZaMOIfjxeAboV4hDtiK828APQb3Rb4tFVUl7dZlduU4ZJR6p2-pWBk5tPQW8FLr3f6GuRTJBCpA42lf9Jm7_r-sa13k2lRwPvcH3cDWD78-gkcRg_eUtGueCVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58b6a7c560.mp4?token=JuedeYX03sg_bXdi5Nbd4dFyahAjUouMrFxWoocW1kv2fi07zTzfmEe6chJ0odERdH6i0nAapLuHdAdjOTGEOTTGzYGcr_lnS34ELknXohu19JWgT4dWcu-6A7H0De5TeH95S0LMDD5G7JPNba-2OGu1SFcOssuh-DTK4_uk7XAPZxI8RJDY74MZdHnDv7XjNk_uqjal4-1Me8yqgCF_ChgmnkxlZaMOIfjxeAboV4hDtiK828APQb3Rb4tFVUl7dZlduU4ZJR6p2-pWBk5tPQW8FLr3f6GuRTJBCpA42lf9Jm7_r-sa13k2lRwPvcH3cDWD78-gkcRg_eUtGueCVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از مراسم دیشب افتتاحیه جام جهانی
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65943" target="_blank">📅 20:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65942">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmmU-pGYN5VKz9ZWQixQDjS1WzlZZdfZhXUTe9DWU7_bIeafMFeyMzB1MYwAXYJ52it8787pvRagu5u7jjwBtG6CHd3l8Ybg7p3q4p7SH4nKUsXPiXCr_mAbPUuVT2PxB4UwRBuHmZwR9zshDr6vqq5Cz60OrEBdW20xmaQ3TJp3OhFj1zXViIRv2PXSEYaDBxCbPhe99_4moCUVmiWFSMhv9fRM7T-3Fjdze-IqugqFhCUGTGln6T9JdDUcKjDh-d2SIWmrErGQsj5Dx2ExfFS_QOx1vh-F2KT0ZVruOXmyvTQmdAnAa7z3lyW0LhXw8vxbKzVf57o3fAs3_CGH6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندزی گراهام:
ایده یک صندوق بازسازی ۳۰۰ میلیارد دلاری، با توجه به اینکه چه کسی مسئول ایران است، به نظر می‌رسد بی‌معنی باشد. این شبیه طرح مارشال برای آلمان با وجود نازی‌ها در قدرت خواهد بود. آن زمان این ایده خوبی نبود و هر صندوق بازسازی که به نفع این رژیم تروریستی باشد، اکنون ایده خوبی نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65942" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65941">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65941" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65941" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65940">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPSLdF-sJWFkKsbqeCjhOurUA5SrjZg7qLkNtf9h889qNRwY3F4bjQ-sfVpofCSSm1H5JYatkjPdNMupmCB6Mxr2kp71hdHTBuTwoQFTW7f0fl4U39b7Ut1WQzpORK_aO7ePiVsqsKC12y63Vo3KEPh9mQZZ-AFc2QoIlOkVPNvkKAVetmTlNMyyWUK8X9KhysYNlvp-eWqkJMNt7Ua_C0r1EH6jeR-2UcgYFUEFVqStxXqvZi-FPts2yOGIHHKFxKNN6Ga-TVGixfmYsCT2Q-O8RmYPPoBRyTNipFfwfcshUBK3qYfcY4WyfnvgPX6L261gAYpRKhpgayn2tu-KDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65940" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65939">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3P2TzQ47LbPBrLxqjzduR1JsQ0AesoKnEEOAzltARb4dYN0uIRy-d_jJea6bXfcTQ-yyo-epItuNl1eIic9nuE69vVp7a_djnMHKf9WRQknC69kH6FM1qrSyS8XlLnCmjfyJkrYa6Qe4DLq4UuUf9rn4y6-nPCcFzOVP1MR4su-cxOWXz_4PnQ8etl27z2LIWEm_qf2wsinGm51YoELJdQikB6_beLNcGi9apCvhOF2rc7m0_sPp8MrDa4xLLYdxYt__66AkvGo07oSam0jOcMd-Qg8oE-5aBQvl5HfLnIL3nPeqYzjMLzkTnIg7YBAmpd2teAefrwzfQ6p0TM2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام:
ناوهای جنگی و دارایی های هوایی نیروی دریایی ایالات متحده همچنان به گشت زنی در آب های منطقه ای ادامه میدهند و محاصره علیه ایران را اجرا میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65939" target="_blank">📅 19:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65937">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3347ca6.mp4?token=jo3pcHT02gI6tuFO7i_QHo0oW-X8PJpRkG6yrcI5fL8B_fmTUS-CerLksDldPHMiv03oYNNTYMEWjoPbOtOUymWizFkbvnWi1kpAFE7LB1_ZacV9qHY7TfuYt14SdHMMEMMOSpJFNTJf4sxgJA1ZrG9s0XUmm-DhhDLWQBhbOuajebGWMFSjaSmYjFQIuwTYJIV6hPW3zLEDDfyAUkVzsN7TfvR3WvNG9WREFcNma7QDqjKC6bPgSiUHgK5upiptHwRAwS0KXhBRUGTI20SbnjS_wstqrnNlsvqKsAOiU8yHSuh-IvbuYpSMf78eYzz8oIWp5UgPx6NtxqIAaMZVnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3347ca6.mp4?token=jo3pcHT02gI6tuFO7i_QHo0oW-X8PJpRkG6yrcI5fL8B_fmTUS-CerLksDldPHMiv03oYNNTYMEWjoPbOtOUymWizFkbvnWi1kpAFE7LB1_ZacV9qHY7TfuYt14SdHMMEMMOSpJFNTJf4sxgJA1ZrG9s0XUmm-DhhDLWQBhbOuajebGWMFSjaSmYjFQIuwTYJIV6hPW3zLEDDfyAUkVzsN7TfvR3WvNG9WREFcNma7QDqjKC6bPgSiUHgK5upiptHwRAwS0KXhBRUGTI20SbnjS_wstqrnNlsvqKsAOiU8yHSuh-IvbuYpSMf78eYzz8oIWp5UgPx6NtxqIAaMZVnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی قبل از جنگ ۱۲ روزه و ۴۰ روزه:
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65937" target="_blank">📅 19:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65936">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0XKHAzp0nCiq-vk7b-5tuykWRr-yXxRvwO4-ZMUYxaOUXGxMq_YkgfRzxfYbW4ypWpy2LgTzygYiVuvkGyQPjefmmc0_5nrAf0E55piwiY--Pnb6FwO-5PmBvxN4p4O1r1v7YQMELgF2uZNM9uWAcyfKJPDerQ5QrOwZONcOEXshrM7scQtMOXP6fQC7dU6ixgbvPZqu-VCn2Ik0ROGdagqvt0hLotTjb9Fi9lwwO9ZQBCYVxvTFy2HzsEQFznCTDRA_I_a_1YaPUXrVc9dikH_vKMvutihHOXAr4Qi7b98xayxxQAqfKwoQI71WrunRlzBgYob5Tm5tAbYW5S5ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: تفاهم‌نامه اسلام‌آباد هرگز تا این حد نزدیک نبوده است. تا زمان نهایی شدن آن، رسانه‌ها باید از گمانه‌زنی در مورد محتوای آن خودداری کنند  @News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65936" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
