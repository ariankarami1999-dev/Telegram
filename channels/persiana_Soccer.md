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
<img src="https://cdn4.telesco.pe/file/RGcu3xmIcfBQPfslLY6VZyssRALkeDEjz3-XfK_3Newv4EzX2eMXZ36aTBQpCrzPGMidn6AzyxyQjuu-MPlPish4jsl4manRXxMD6Wn5g68VH0fxDNeU6Jq_bwnGYGyHvGilN60Na4oFdQ11LfcLR3lhCNVcnkT5llqvW3y188HrKfxTfrsQGElzQ8BAEyDZMJCVGfgr6nKQTiWWV_OHtvF0sqUDlNTDXvNaOsPMFT7HvfEsUUasTQatDETSVBMYCgmrrO1lCUKHWix7yuq5vdir-D_sejNDoL0AJiiQyxPl8PQMFbNM1q8JkzShlMkdEQhfJEBXY9x9WViKMRchRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 460K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 19:38:12</div>
<hr>

<div class="tg-post" id="msg-25687">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONoG5C_v9zg2V6A41jbnPzvTUmuLxa2nesE18NR6T_JP7ESiJCuxDby477nqta7ZcM-wXKC1YbQnwxdafVusxZC4yhC3dblrfDYjHwy5as4OiKJljOZeyI55I4uTTa0-QrI8nnJletAXqnaroF7AhFyu6R9WpraNiqgZ4ShMdTSs7e9WH3386H2PzUJ_cVwJQpsYdwVpPX1ip9jfopRfimi_2EgM4wrYBs5e8oqhJGVdgk_w00LUKaecXK48vUGLaErBpEWPIbNcv1RXiUaSdJ1LauQyW028-CtXgJijauSA8QeTQSGXpZHuFurzTgmuIK8dfMsJW0GY_vvb4M1dGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8vbCiihuY_cUM4ffYa0bPQEaB8x7j8hg0xusaf9h7FeSXbjPfdYU1MqgVmQy2huE4-F31JVII6fvS9ShwRPC7r9K45foeQ62wCv38pPer-pNpRgIPcb28jQlVVYdEXpUIYaru29veIZooXpgSLUJtGbuTfqK0CrArLNCnDFKgbQ15TWRZRC3Q6Z72cWpA8PcHtRgL5rZA0cJ_0CF2sAAqc2mGfs70tOibd9UOr218LpnFvkI4XpQpsYtpgOn1afp0phC71vBRvWnsliZbSKCYdVD_W-cZmlNuZ7VYGRAT5VOx_etyIq77jAtGoEV8yb4f9fp6oCH6l7w2dmAnf6qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/persiana_Soccer/25687" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25686">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGCpvVZok_FztYJ43Tq_JVa8-oTNCPtKH2BxtMIRQ3dyfBYJR5etSONYEniT-ztYIwcNbY3CsqnzYtBfa2030LmmGrdZVF4CsGI5liDnloZwaHbaGg-toaOf0k7TovjUozhdcpMc3OjuxuaGLYCijLCfZe8FzotLIh9zEib0QgUFLm-nw-8Y3JUJ-bz7IhAu7naff1R8MxP_GD2LTuXxFZTZLua6LerM6f8590KZgU2-QC6pMVytVTs_UOnjvt2guw-Ab82Sv80GB9B5ZzG945g1Exjx5yTAopOYS0eTgc8shFpV9hGmmGSXobnQ2o-3Fziebso2kCPRUZvl7mEBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/persiana_Soccer/25686" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25685">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYzCm-Gff4UbFbKd_EXn7Sz_bhrswI2UX5jbUiEK-f_rdFX9xQ_TIqGegNHKEeGaZcQ_y6OA0-ID4SZDA_J-e29OUeGO3rMwJdL4M-SAAGZASiQLvWiFGG0Rg2mQKm0vFlSlQycMdXptahATgzTd7hPIMtrN5bD9FFq3sKLmwFMyTXC_LNmJQ-RmnDE1RNPwOtA0mc48irpWg56a4GDj9FMmZwrYS3erm8xBLx2eczuthFDIxUS5YYKjocd5VR4SJoepQ-P3gkq3fvDfoD35e_ss39paZBHuIMIuTzrusRbMTpXyPepNkF7tINB93UMEbIWhWs6045WR-LwPtziKzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا؛باشگاه‌استقلال علاوه‌ بر پین؛ با یک‌مربی اسپانیایی که بالاترین مدرک مربیگری اروپا رو داره در حال انجام مذاکرات نهایی است و به احتمال بسیار زیاد با او قرارداد امضا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/25685" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25683">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M6cxROF32YOiorVKKno5WmRT_T8XeLdVe2vMF__Ra21PIVHT9VgYNfGBfRyQ1tmoyqOKl7Fu_mSlKAQyebmzlpisiDKgfLUW-JIQ2HFAICZBsPiLZ1ee2uUtcC1qmUXM276PHfsbe72IBElUQXDYPzjggaLoIfyZsFTIHMuMnVb1u6Lsx-bp-55p0XSul1q-eeG-GcA1hbHOqFcYcukvtoJoutfF1qev2A3uDRGfuf5AS9Td4-FCalikRsORqYaT38TA89guJ8zNfGjfxcUjmXCQl_ttGYG_k4zXhYKpAmtVQ6SjLI4jy5SDKjZLuR5o0JaaLOJV5HHsyzj2ItsTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eo2ENMGups1Z7nf2h822ojfdArOAI3ISQYOYvk1Pf_x10AqU2blIwL_Ui5Kt7g0sm5SjyOi0S93uM2lgDQo_XlCLKDf1uv7eawX3GqtZYy4Pr4bV1tCeVaeDVp2SEVPdzuBYi2s0QfzHfMxU9yb9DElchnDCNXiRRfMSDgpV46HCICgA41oVPtphzoaCfHqdD3hmraH_oOHjJN0Jr7vTwjvsAWPt4tf_H-4TPcAxUQYBkwWyXF9k-soAFCBTkXwMTwWk2uT0YGFi0S7C9qEyTbi8hOWQ4Orz6ozWDmdkrPoDMuCr_k7TZDnfX-Z1B6BNGdbXvyUdnvckdCrW765Ngg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/25683" target="_blank">📅 18:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25682">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🏆
40 سال پیش، بازی انگلیس و آرژانتین یک چهارم نهایی جام جهانی 1986 گل دست خدا و گل قرن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/25682" target="_blank">📅 18:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25681">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq-Bo1CfK-9Vw7NWEinnvnnrvR7-2M39V4BoCHyZLKj_PG8WljmUIT_xbZ6lILGuUF99csQTHSAUOQPH4a2Ib53dmKD1LBlHAOkl3Z_887MCE7KP8NTpgvNT4F8UMW5p591kb9CH_9EdcwB9dfuRDtl9hjMKlNgyFt_Fh8_PK9V2s973-7bABhdLYplHIUGMwX7WkQWUXHB5A6zvbl7kFCRMdbsZOCQhtSpimK-l9L_kukd9bgMuSWrdov-vchbwWBBVyQG9hD-XnHuP8iIG-qooLJhF1wASFwR-eiixnqi9sN7TTPgnR8qH8V1n96odn9uPZkpXUA1VjYqWOUhlaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در انتظار دو دیدار در نیمه نهایی جام جهانی
🕐
فرانسه
🆚
اسپانیا؛سه‌شنبه 23 تیرماه؛ 22:30
🕐
انگلیس
🆚
آرژانتین؛ چهارشنبه 24 تیر؛ 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/25681" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25680">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCvi9xg4xeLltkf9YePO9Ec-s877JD2-pOrJkVTS9BJjToK754_IPpCLbyS_SBsLjyrqlZQyWfMr-wncx1jivK3ESKq62yNUS_Cx4Oumy62SveK1bvBqUl2f8PsxbqUdjvI2miE3kZne1wUzfXH87Hzk5Et92x9E0Ur1uyk5oQ3fdPoVILqfaU62P-gCs1_KvfIl47DHpdX8CSYPHG8yJWLohLGsdtPir6L_WsuDviWnMj0wW2vrYCXMUZISchqGrmie6gtDV3Vx63Y5lEsa8onXA0aiuLok7mfjQIa53FqaGmAWt825diKTS474-G15g6CB4_BFioSe7AoaQ3Z-gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مسعود محبی مدافع جوان این تیم رو 350 هزار دلار اعلام کرده است. یه چیزی حدود 65 میلیارد تومان. دو باشگاه استقلال و پرسپولیس به دنبال جذب این بازیکن جوان هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/25680" target="_blank">📅 18:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25679">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtZKSmmBAb36WnoEdObz4jy4ah7AHR7wt5fVBzqVuysVrN170WxLiZBnu4uEHunjhMlOu8i8p-88CImQvRraDIxlvKdoYwsZHdkwRD4EdB5vDC_cpEEl4eM2DHKkOPeqkIpYzqe-DOOwzWdFCISxBJN0MoS5c_GHeiG3ddB7pknDy-OHAy-eVPrSoXFyaYwTQ78NmgNB3rzqEVo1RHG5Ak2QL7xms-ck9ZAJVdE9B5pH0w7OIjLAb9ntZKc6wMry_xcjqTAI64f0VL79XGfNrlKTTtBYeFjEOX8xGPqV3cS47ezXx5vBOZkev2gMyCznpxzhB8PvmPv5StYg_imaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری #تکمیلی؛ آغاز مذاکرات سرخپوشان با ستاره سابق برایتون!
🔴
بعداز صحبت‌های شب‌گذشته علیرضا جهانبخش در فوتبال برتر؛ صبح امروز پیمان حدادی مدیرعامل باشگاه پرسپولیس با کاپیتان 33 ساله تیم ملی ایران و مدیربرنامه‌هاش تماس‌گرفته و پیشنهاد مالی…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/25679" target="_blank">📅 17:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25678">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0mGgrbY3t1DIJ-MdKR6mVYN7as0LeejIsYmWmd4UCzrGdR3O8uc5LUQvx2xG9Eu-PutnBSYnUofhs1RnDHQVSvQioa7OIDc68aMtc6WKCoDcjIei0wKe23DPz6xOT_P9gj54R4m8u7v2ak4_cGf4icHbS5jBBJpsdCy9-vpnEuBE8MJTVSgXgtWMxTBijSxlHziC7gVj3nNHzICP973GPRCrPweF2txfZY8Ai6qo_4Dp9xoA-NOfYNC3r3NdBuWwhnTx76KXA7An7p2teLxppma7IJjuet8HQuvLxdZCChOTPlimJATdWYr-nDyEoBukHXRgmcrd25zQifoAQblCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی: تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/25678" target="_blank">📅 17:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25677">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-1rMzDsH669EIrd2mk7P1mwpKBnBPsGh6FWaSWU94nzNKPNFLpx7CchC9dLV3zIiMVGBlfi6rboXraBTKSzC_RrnObDf__j0lzyfUVJo8aG_kGB_04S7B0HeQFmQ4GSHNsnLYVgP2Nyh3jSZC9GUwM551wGVAwawU8_mjOonFlsbuxUALqTrNhTBqpC6JAGBJcDR9IILF7YOLK2H0a-7GjAHt2n0AUpA_R-px7OCFQpAPRE9whSuxOFAZW22DwIGYm_E8rJr48qzUEUdpZpY7solG4_5AtuODnuM-Tv3MUFmVsUONwyYTRs1YIl_gh4-I65cQxz38b94GawnBtjcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسی، نیمار، رونالدو و هالند اگه دختر بودن:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/25677" target="_blank">📅 17:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25676">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTV4dROefUiO0u7oOWWL1KF7P76ByP9LgMzg6iEA1hYZ6Lbx_Qe2offr5JjaxTZ0O8AWru7Uw3b0be3eNahf_XC_2Wzyn8JHbWpJlSUaABV2h3nmCOMPdO2gQA6ylS58DnXH4rLC8qhDaIi3YMGZLiEmZDXz7dgKh7h8asOv2cf7Od29pXVGIAspqChOd7j0OI8VrGJqTkyu6uo5LDOgEFwDBcbynIVX51U0naPDahfNHjGgWHv0oNuv_FChusz1tN3S1jWD1t4JDjCpS4KYsu-EyMGj3-Zp4_RLu38fiRWBMIupauCd-mXXCMid45VBwkd6v2v34mDqZ50VpvnVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... علی کریمی هافبک سابق استقلال با عقد قراردادی 1.5+1 ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/25676" target="_blank">📅 17:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25675">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBJWSR-yAJCxhKtEb-PCKYCu126syHB7B1LBa0EVomKAotZ3WNli4SjKtqfkC5vijqMinGmwGlhyM8CC-aINO-uSGz99Y5129ryf-AO4W5cq9jufIG47ueJX99y03KSbD4Re7i38iVoP2TBPpov-gkGhBvm2eUfBmdaR721NJpI-wBf77RYcwsEEihcJ58-MXvW09Mjc5ryQ34cJ6kbj85wTBrwWN-DT5laYtNUiJsrUo2V6Owz_ux15791VSxLHrGQduaEkm5ipPCnODYMzSVdeGw_bqSo6ZDLYzQo9T9Wnl6SUyYJooRN4OsasuuPRhTuZbjjEWeN7S367dIrT3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/25675" target="_blank">📅 17:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25674">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0znaSXysMmU5hTNAomq9Y_W8Ao7jNN7xoTMmm3GC-Mu1it2l-rxkiHCS4us75IOGv5nlA5GEkTYFXhSu-9hQfOv2tKrta5zmZs5ArJQ-Pi14s8my1vJ-OPQysUeZTI_F0mMB5zzh5hbpHocSG3TqdgImHCRP5MFeeHhfdNBHj5k9LYVpBjyiq_YQvQwJ9Vyb2W_glffYLzxG6sycy_SEFgQD4OeVz9v8gb3aZsKOL-omcIjpk4AUWd5kuoYR5VoO7vLLxrueXn6D_exbMqBGvqWDv2y3lZn1p9HbkoSO1kT8FUjMEnh22rnV9TTQOPR9lxnc0zpRzbUh9Wdw1t6tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آندرس اینیستا اسطوره فوتبال اسپانیا و باشگاه بارسلونا مهمان امشب برنامه عادل فردوسی‌پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/25674" target="_blank">📅 17:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25673">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=Zuc-4Apwc8w9gVyfbpIH5UQYL9R9tknWth5Pcu0YF47moFKsE9dD8YDUWe1PrYLIum0uweKWfTrgHZhcTMrXp0bB52gNFT2z5znzOSF4o1kT992RISTBEKGOUjGLRMkrCSIjtqqpZgipg0YZTKliT9xee3AjO3Ti0f1TeWUpLX5uCO5h8ZSM6C8pTF5o5aawCeZL8Pmbc4FUV4sh2tM4jC7fEjhE62rhDQEuEAbUDK5W1Gtvucwe3MWyFQDo4_Ot5-Qm0OxDwnUCbDmcAf4f47KAnCoC7twUA2-M58DcZ6thutW3Lm8ye8wdea1K3g266DBZpsp_--gUFm-Cq_hymw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=Zuc-4Apwc8w9gVyfbpIH5UQYL9R9tknWth5Pcu0YF47moFKsE9dD8YDUWe1PrYLIum0uweKWfTrgHZhcTMrXp0bB52gNFT2z5znzOSF4o1kT992RISTBEKGOUjGLRMkrCSIjtqqpZgipg0YZTKliT9xee3AjO3Ti0f1TeWUpLX5uCO5h8ZSM6C8pTF5o5aawCeZL8Pmbc4FUV4sh2tM4jC7fEjhE62rhDQEuEAbUDK5W1Gtvucwe3MWyFQDo4_Ot5-Qm0OxDwnUCbDmcAf4f47KAnCoC7twUA2-M58DcZ6thutW3Lm8ye8wdea1K3g266DBZpsp_--gUFm-Cq_hymw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/25673" target="_blank">📅 14:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25672">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeCY7yzELLfWhYa1L8cBls2uT7yWFCTOHTzTgqYoflT18dSdLMbE0BSe6NDvnkhvqvGBcDAwKJR--EXQiMVAKqW6Clc2Su-0Eh3CzRmyHSbHcWqjZBzI2oKwTj7PWBb6-9amSDdOp0apf0p-4NlWAv2KprnOqzfdJ2tyr6cSU-Hm2r6Ck_sI8iV9vCIIp9_6c6GGfFD-5z_zGbJOpxAzbObZ0oauFCkHWW-QeUO0QjXrd0wBw0ysdwHt7tbpmyRjftJZAFeMGSesBAMv5zC9qXitrGYYO3PRE6RnmvwI-iN-MTWq3CbY1urCTzTD3tphy8wiHnyyURgU4j4ZABNbuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛فرناندو پولو خبرنگارمعتبر اسپانیایی: بارسایی‌ها یه‌فرصت 72ساعته به اتلتیکو برای خرید خولیان آلوارز به ارزش 100 میلیون یورو داده است و سران اتلتیکو رو تحت فشار قرارداده تا زودتر این انتقال انجام شود. آلوارز به اتلتیکو اعلام کرده تحت هیچ شرایطی فصل آینده…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25672" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25671">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=uesQdjV1W0msJ5AMVwf0I5R5G_AadY_aA5qA2rMAI8UJYnHWJDUJIu8qRBegiJDOWUE97QNC9oaSVPRCZELEmmQ76ol1BNAVPm9ArvlxqM2-8L6WIiHMFqFiwDIDUVKUONBaNlreEmNPp_Lhjs3FxYZbMRWyWAl8ezTUuC6dgc5pRR-CkzgrwwhCN82fgsB-i7d4F9ftVgf_M_j4EyNuAYtmfWo-sk4Qz-VkFdYT3yHdF037uHFTwgXW3RkXLTFGwRSB_cxhLcl7oXGIeNH4mgyr3Zgoal7V5ph1nKkQ439kwFiMQDaHAgofbuFjLsdHx8pDBjN_gV_Gb9Y5d9MxEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=uesQdjV1W0msJ5AMVwf0I5R5G_AadY_aA5qA2rMAI8UJYnHWJDUJIu8qRBegiJDOWUE97QNC9oaSVPRCZELEmmQ76ol1BNAVPm9ArvlxqM2-8L6WIiHMFqFiwDIDUVKUONBaNlreEmNPp_Lhjs3FxYZbMRWyWAl8ezTUuC6dgc5pRR-CkzgrwwhCN82fgsB-i7d4F9ftVgf_M_j4EyNuAYtmfWo-sk4Qz-VkFdYT3yHdF037uHFTwgXW3RkXLTFGwRSB_cxhLcl7oXGIeNH4mgyr3Zgoal7V5ph1nKkQ439kwFiMQDaHAgofbuFjLsdHx8pDBjN_gV_Gb9Y5d9MxEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
کریم باقری اسطوره‌باشگاه پرسپولیس:
تو عیدها و مناسبت‌ها هرکسی بهم پیام بده جوابش رو میدم. اصلا برام‌فرقی نمیکنه طرف روبشناسم یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/25671" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25670">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=P9ijkgYwO2VT0eKcAl1Qm6CuM--sUuYQjI-NMLxrPQlIs8GvQgSR_9jhBHikI_gav_cdBjGVP6iNydX6gjhqfORP4HbTZZTqh-N-KR-2qT1b2yzz8AQ0NIfAujNfAmvU9ld5k3qw34sD-w_eslAqs9DzpiX8n707pJmvMBSnVM4jyTEA8vOkHuw2LcHguEPBA0jcKphQnzHE3vcm-JqE-NY3729789pUZSi37nUBn-IX1V6VWr95HpKv1G9H1IKEczxComMNPJjAEVtatpr61G5Pvpx89tlE2l_yEzLx4xlmkcp079vlH5HDe24kKVwxPUAvuD8SoN0P-KStN2YRu25EiJ6-GkPNsTLDFvXCBlA_a71pXS8V_Osz0RvhziO-a1b0kxFcYkTo7OvSb2hKMqSrXRQ7km6sEg4AbD7rMHnhvh9GMQHR-sDvkg38Y3io648eXSpxOXvYeyPBX9_S3fkfSZ8b2xCp894cyhV5ZY6bFzhFv3q8C3SnXYbb1WghIsm_vyphPlBJ5Ky0GQkywDedgpUt1k0dfzcSNhC7BIvoxCG-cHRwlAjEuOlAHFkgi1cmnUNV0N8uZNMRFrbHLN0vHdNRQovs9klpG3JxfajUKFD_3VauGOcHL5ptnUv39wdQc8kcLb9th4eitI-Wy5AjwlaXUJGPYrpSRxqGz5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=P9ijkgYwO2VT0eKcAl1Qm6CuM--sUuYQjI-NMLxrPQlIs8GvQgSR_9jhBHikI_gav_cdBjGVP6iNydX6gjhqfORP4HbTZZTqh-N-KR-2qT1b2yzz8AQ0NIfAujNfAmvU9ld5k3qw34sD-w_eslAqs9DzpiX8n707pJmvMBSnVM4jyTEA8vOkHuw2LcHguEPBA0jcKphQnzHE3vcm-JqE-NY3729789pUZSi37nUBn-IX1V6VWr95HpKv1G9H1IKEczxComMNPJjAEVtatpr61G5Pvpx89tlE2l_yEzLx4xlmkcp079vlH5HDe24kKVwxPUAvuD8SoN0P-KStN2YRu25EiJ6-GkPNsTLDFvXCBlA_a71pXS8V_Osz0RvhziO-a1b0kxFcYkTo7OvSb2hKMqSrXRQ7km6sEg4AbD7rMHnhvh9GMQHR-sDvkg38Y3io648eXSpxOXvYeyPBX9_S3fkfSZ8b2xCp894cyhV5ZY6bFzhFv3q8C3SnXYbb1WghIsm_vyphPlBJ5Ky0GQkywDedgpUt1k0dfzcSNhC7BIvoxCG-cHRwlAjEuOlAHFkgi1cmnUNV0N8uZNMRFrbHLN0vHdNRQovs9klpG3JxfajUKFD_3VauGOcHL5ptnUv39wdQc8kcLb9th4eitI-Wy5AjwlaXUJGPYrpSRxqGz5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
رونمایی‌جالب‌از شباهت مربیگری پپ گواردیولا و فیروزخان‌کریمی دربرنامه‌جام‌جهانی شبکه جم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25670" target="_blank">📅 14:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25669">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-g_760eFBS4glTmHdN1V6JBV9b-vUt36D9sW4kOuml-lrcuBw_jT91NFZy3D3z4vXW_eO_AjsbAMHAlqV_as639xtlRABgACnIu5T0AFugtKmis9wsPTF8NDqr4oT7PYl98E3xB7GBnARnK2_8J_glULzrQxjqGVt_5HiPPTcjVrvcfHUZ_67liX5Gv3r4l8qste4dYYLkweeoMHqFh1avdO68xjqP6HSlfNgZHoeo5BuuA3pmAMecR0rRd8FnElc8XhBKmONKrcL4QXHBKrsa48qKOSzALzyxL06Dx_Z8RvZQvci2ftlDRx_3Hqwt0_TUBgAGo1wUXPFrRWSC3Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
کرک و پرتون بریزه
؛ رئیس فدراسیون فوتبال سنگال گفته که: من‌اعتراف‌میکنم که بعد از حدود 10 سال متوجه‌شدیم‌پزشکی‌که همراه تیم ملی بود، اصلاً پزشک‌ورزشی نبود؛ بلکه متخصص زنان و زایمان بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/25669" target="_blank">📅 13:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25668">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd10299011.mp4?token=QQBRza5k5GcuT6dfFI5QJUfx9DErIt-mmetRX5B4pNwqoczEPSNU5QcpcUxGFKejZlc4wXhIZWa1AphsAujMB1T2CW04aI_NfMTrVEJuU45pfu7mvlpISGxxhYZZwJjtgxzo01yOWNYvMZVrUhJ71B-IUa-tVrsliW2shTFaS_MJfArc3u0kKYgVgjqby2HV-IgJtqHSol__nUM_VDx82K3Dcq14X33e78OgR07PYfldOIg18Cgx0_5C_cibE1zqO6rWpCrtVMgIXy03Smf6f-5tP_EwBS4fdKdJNIF1H0XnuzuPlDcK8ssPXAUw35-5wmw-edVKH7E5C60G9U6UdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd10299011.mp4?token=QQBRza5k5GcuT6dfFI5QJUfx9DErIt-mmetRX5B4pNwqoczEPSNU5QcpcUxGFKejZlc4wXhIZWa1AphsAujMB1T2CW04aI_NfMTrVEJuU45pfu7mvlpISGxxhYZZwJjtgxzo01yOWNYvMZVrUhJ71B-IUa-tVrsliW2shTFaS_MJfArc3u0kKYgVgjqby2HV-IgJtqHSol__nUM_VDx82K3Dcq14X33e78OgR07PYfldOIg18Cgx0_5C_cibE1zqO6rWpCrtVMgIXy03Smf6f-5tP_EwBS4fdKdJNIF1H0XnuzuPlDcK8ssPXAUw35-5wmw-edVKH7E5C60G9U6UdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25668" target="_blank">📅 13:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25667">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=h9zustLE1RR_wJ8EsOHKwf0Eq2dH8OsWnkaRa0MiPQ3n2ow0F1EReCkEb4_uS2itELxj1boHTzjejF-nTZNvwYTXV_plGVf9Wgb_-UM18lE2SwCw22017WnN5hwLKTYHB64QSyA77YpN6gWfsTJxad5Fqeu6Pe9uw1JmECOgZkx_donnzVD7usBpphPAABi1ovLX1d3YqWi7E3pn2LYD2KmDxO9ChaU4pLeplsuKiocHxqVDfGg9QrtCaVuZ86vU_hYT8FgwgyfvsBIoW4FiZ-x7GpSvFVv9-xa_C3uWKxR7VqMHGdP9LW--HbvaawwXwRWHT9V8gEPkfQK8zl7LAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=h9zustLE1RR_wJ8EsOHKwf0Eq2dH8OsWnkaRa0MiPQ3n2ow0F1EReCkEb4_uS2itELxj1boHTzjejF-nTZNvwYTXV_plGVf9Wgb_-UM18lE2SwCw22017WnN5hwLKTYHB64QSyA77YpN6gWfsTJxad5Fqeu6Pe9uw1JmECOgZkx_donnzVD7usBpphPAABi1ovLX1d3YqWi7E3pn2LYD2KmDxO9ChaU4pLeplsuKiocHxqVDfGg9QrtCaVuZ86vU_hYT8FgwgyfvsBIoW4FiZ-x7GpSvFVv9-xa_C3uWKxR7VqMHGdP9LW--HbvaawwXwRWHT9V8gEPkfQK8zl7LAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔹
فدراسیون فوتبال و سازمان لیگ بزودی خبر به تعویق افتادن لیگ برتر تا اوایل مهر ماه رو منتشر خواهند کرد؛ با این‌ شرایط موندن بازیکنان و مربیان خارجی در ایران سخت و سخت تر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25667" target="_blank">📅 13:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25665">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfugoIbsbMo4pq081ZSxLCYSQsf12SZQiervVSMMTXXxqptruOFz9IJ-5frUMTib2cD1vnY5IUN9WwJls5bJCuYobkvJEdA6zekRndAaiW8g1uagjo9-BtrzA9dSPdKahx9ibgOcPsJryaak49yipz1nL8BTY8yW5NdbyT-JJ5pTLskp4dez3xd1JHwJkwrX7L5QlGVTIl2KnXTJEZFY2PuVRtZ9Vg1mtRale_Sla180yqdTb2pPaSp2e6sJYXPKnzW8_6KsvTWlKgg-r5HRqmYcLEX4SIwY37zC5R0BbdtDtJqAV8PsSrHWLM-H5vYmg8-vLfaTGNxm2nxP9iQR1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=drmlS5H_oE6ov8QN4CxouvVS6FhE2EdEnp0CYj8MSNlJqMNEte299hpMblrJbednRrIFjp0E397GfdboZMsGTAK26LSN_-OkhRgaFl_QbkxYEzNzRj1B2kK9ufgCsuuG6IkfeDlqO8TpGz1XxEfxB9rXA1rm-PvFmzhStT41sQFlkj0qE4pVoy34reCmt7v7vnFxhP4qmHFuOckXtZYh4qLTBIWtKgQbU4TR6Doo5csZw75Qcu4G_5OkyZFUFpQwwFXg80vshiTVCThEhCczy06cSvS0PYE-JlkDFGVzMFlhEZw6CC9_M2qVHVLhUVeOevM4sTal-qx9fgIAMXTzrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=drmlS5H_oE6ov8QN4CxouvVS6FhE2EdEnp0CYj8MSNlJqMNEte299hpMblrJbednRrIFjp0E397GfdboZMsGTAK26LSN_-OkhRgaFl_QbkxYEzNzRj1B2kK9ufgCsuuG6IkfeDlqO8TpGz1XxEfxB9rXA1rm-PvFmzhStT41sQFlkj0qE4pVoy34reCmt7v7vnFxhP4qmHFuOckXtZYh4qLTBIWtKgQbU4TR6Doo5csZw75Qcu4G_5OkyZFUFpQwwFXg80vshiTVCThEhCczy06cSvS0PYE-JlkDFGVzMFlhEZw6CC9_M2qVHVLhUVeOevM4sTal-qx9fgIAMXTzrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بیژن مرتضوی خواننده‌وآهنگسازایرانی با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت. عمو بیژن بابت این یازده دقیقه مبلغ ۱۷۰ هزار دلار نقد میگیره از فیفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25665" target="_blank">📅 12:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25664">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URFy2dV9_j9mGqY5ibJ3XdEsjKET4QYN8_S1-x2Hr2utCNW5_9J4NDvjOkh5IHsw_MaNuB-qoEmzZVg6hGZEenaX6OcIUigQtIhgFkCytL-j0XZ5sIPhkn20hQ9aoIGIfPuR-Pj0e-QhK31r7zvgqHRTD0bMeC6z5mE4sJer4RGO6b-V9ELMBfX1BMobJJv1wfaMgl1hJP2jvwBDJYiINSUdPyCRZ-eKpZja6Ntk6OjDV34nljJGDzXO0TOj1o29HMG9SRBMwfwBIWjhvRIB0z7Bojh3hnLr2wzY7MChMYzO-uCbxBy2CL9TGnX-ZIFzAeielVxZofaZJcC0mxTSAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25664" target="_blank">📅 12:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25663">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=HzSQ8szYbF4l6hN9lLUCAWdFv826Fctegxs2RdYa1ug0qDIDfB1Qu3Qupsge9VyE7m1SfW7KIaBvpDOLkn16z2VoT2QPqRpdtt7YwxSVGCMnu47NYdq_hSuUvcNz1Toy3C169CLg6fruQot6vMsNq0F-zw8Ln34siPUY2E1V5WAEQY0Z7i7lPOxAE0aoC75VdXCg8hFmsj0t0w5pecr1_7db9hN1zHkOlJ8l3jO0GOyWGHv14nJ7SAVXmtnQkFFYS20zF2svui0j4WBhIGMyIiRTt7wWcpc_dd08wuoSf86ZelJcWkprwsI9ctJJkHOGYBue0VOkZSn1sDY-cmVBQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=HzSQ8szYbF4l6hN9lLUCAWdFv826Fctegxs2RdYa1ug0qDIDfB1Qu3Qupsge9VyE7m1SfW7KIaBvpDOLkn16z2VoT2QPqRpdtt7YwxSVGCMnu47NYdq_hSuUvcNz1Toy3C169CLg6fruQot6vMsNq0F-zw8Ln34siPUY2E1V5WAEQY0Z7i7lPOxAE0aoC75VdXCg8hFmsj0t0w5pecr1_7db9hN1zHkOlJ8l3jO0GOyWGHv14nJ7SAVXmtnQkFFYS20zF2svui0j4WBhIGMyIiRTt7wWcpc_dd08wuoSf86ZelJcWkprwsI9ctJJkHOGYBue0VOkZSn1sDY-cmVBQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25663" target="_blank">📅 12:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25662">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjqczQ2hFjEwU5rLhHLeod6FfwNprPgAUu5TNpMlUXzVIyBdndff2ot7tzD41lt39MDjJj5-F_rvhaaJCiUwgAnkb6Mn7S9acozqR6ZwvfEDXu7CRZJhk1XFuplFBN8m8TPG4ZhiEHXM2YpIFa_UvqhaxG9E6hdf3kTJ08P0a8qw5Wem_V44V_SgQsmzqP3l9YiPKKYvwfl7m0W0Sil817JBd2V93FadZEr51nMjv5wR7LSy6C1d99drDB-tvpily2Eyp936ZPk3Jy9pBW4nabAHvM6yo4sVWZ0jpNnWLDcP89miJVSeRNJnlrUM0YIUzmgKSqHrx3XiCifq4wNfjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25662" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25661">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thff6Fel2Bxpk8tIkoFktChDg3wjNunqBgKR367EZ7vtDFPmfvgfaqYY5RDjLToLfNE879mEFZGVz_i8Pj0AYZZF6KjpSnc-5NDGbNgdPPCY4L2sZ80SXx6Kw1EM1LvRhmxZNqVzaQFMU9MNjM7RhqydjaZEkvbPMpoBj8n07qdo4S2kbK_nfPBHEBlTYAoJFhG4yHtwr97_eH7kZkZlpmxoypurQNgQmGLA4UYdTro9WmLD5zQKCr_AtSXTTUO7W-0HakcpLjFYqHyrnk7Q35-7UsnZymbAx8P4sp3Gtx6aiW0wHVz4HWhvxqFfHjbj1eWNJ02CL8h1L5Y7fr2m3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین تصویر از حضور یاغی جدید فوتبال ایران درتیم‌جدید؛ سیدابوالفضل جلالی بعد از پنج فصل با لباس آبی امروز با لباس قرمز پرسپولیس دیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25661" target="_blank">📅 12:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25659">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcwOCiV0Iay2BsuD-MEtFD2R1nXrsxriAPrpxvVTSKxQbgdKj8-3BMs0SLNZjJzGeS22FbnfQU-ljWVtBs0pTVo-FEERq03druKbj1aZCsXDza5Hz5Y564R-HPdD6GmH4qebjGeUE63quA2vG9UGFbcLmmHfYPB2ULb-ov6yY7pBHOtWOuCJoCAKphmt9h5Zd_lDR9Z9R3s7sORUMsOpHTVeZeokXkGY9uUwVqHCBPNJNoflaaX6afFMO0y9mC47EQ09jKW2iJXSI0lT3CsGAtzSBtYEKC2vUZab4uLx4bm1cPDs-SV-PabizoYR7s9K4fG3beyHMBVNR7D86N8ekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی:
ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف میدم و روی نیمکت تیم ملی دربازی هفته اول جام جهانی مقابل نیوزیلند نمشینم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25659" target="_blank">📅 11:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25658">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKY87OkvvJkWdtJFwZ-a_QhEOAFWuxBrVb5in188nSLqa5hNnnmsCAoOQm3SSLLY4zABcM3D2n5BrN--RgeRSvzDW70vHwipS-ZJrZ5DJA2arP4bsS0xgK7-baGte8Ie1DlBUYRmI4zoi9oz5ltIPTeZPL_U9zXgcwADYy7FKS6-RC3CaMyVtjO850BuniDBJSvDy1-rMJKdXH9jolw8umJDqSVP9AwgRfk9SQAKNZ4V0b8-caNRoOLYF-gOyRubBGqnwjqZKSpZ5CsKSBucdDNag2hYJAC5rID-BhhLHblxIwXil90qXbNrmBY_etRZfZYx_BJBpVOevHU4fatsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
5 داور نامزد اصلی قضاوت مسابقه فینال رقابت های جام جهانی؛ علیرضا فغانی در رتبه سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25658" target="_blank">📅 11:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25657">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=F9ao35pfWVJNf-gfAOcpgk_qbeGXwFIYe5i1S0vQLSgxF6aDgIMtwHZJsA9p6egK-KF-TNyztGTbJfneIunf4jEW14_LE6aYWB7aLj_k6IHmULowDslnzQeaVG8sB4_ttuNkrqNWGkueS_6Nw1V8bZbgh0qaKDTeT4y2V8WPk532qaC2clDKJRs3JH3e9K3wL_oUdlNtsNYXRcAveBtYkIuIkXZGkefdvIyjhWTp0mC3pMSRObtRbuAzNTFlcv3uILuEQG1ijprQmXprmXSd644iIBy4kgX3IlAbrvMHSq8kC8IVrATWGJfWC6pturpgZ0-b2GIMLI4BxIgzD2Ax3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=F9ao35pfWVJNf-gfAOcpgk_qbeGXwFIYe5i1S0vQLSgxF6aDgIMtwHZJsA9p6egK-KF-TNyztGTbJfneIunf4jEW14_LE6aYWB7aLj_k6IHmULowDslnzQeaVG8sB4_ttuNkrqNWGkueS_6Nw1V8bZbgh0qaKDTeT4y2V8WPk532qaC2clDKJRs3JH3e9K3wL_oUdlNtsNYXRcAveBtYkIuIkXZGkefdvIyjhWTp0mC3pMSRObtRbuAzNTFlcv3uILuEQG1ijprQmXprmXSd644iIBy4kgX3IlAbrvMHSq8kC8IVrATWGJfWC6pturpgZ0-b2GIMLI4BxIgzD2Ax3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25657" target="_blank">📅 11:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25656">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=TkH12maaxsESPIB4J2zGr3rgYDpYwvnbbtATCdUDd4FItdgL8s7GJ7Tifs_ICZbgoiWaB-N0o9PGE8teR4gjx5kKOfUKXQpSbTarVyhAhNlnfjWnT3-nN0QDAVm4B-vKQGReL1e3nPZ2ecrderuD7GSLkRUHZqlH2oag6keTaFSXbKgn-KlqaZ8AB3xUUOfvZLSdKQJzTNnly-utYfmL_vo6Mi2BjkYY8QR7_Eavo860Zk_s7piOtlQ2Ax9pGv1fzM86P-IdMb05lfBWyonTawYuu-IhDb9SLQMb3x1iiub7spZUFKM1xQxS8E-Bgn0TKe8b4f9e2OCEMN-MrWfTCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=TkH12maaxsESPIB4J2zGr3rgYDpYwvnbbtATCdUDd4FItdgL8s7GJ7Tifs_ICZbgoiWaB-N0o9PGE8teR4gjx5kKOfUKXQpSbTarVyhAhNlnfjWnT3-nN0QDAVm4B-vKQGReL1e3nPZ2ecrderuD7GSLkRUHZqlH2oag6keTaFSXbKgn-KlqaZ8AB3xUUOfvZLSdKQJzTNnly-utYfmL_vo6Mi2BjkYY8QR7_Eavo860Zk_s7piOtlQ2Ax9pGv1fzM86P-IdMb05lfBWyonTawYuu-IhDb9SLQMb3x1iiub7spZUFKM1xQxS8E-Bgn0TKe8b4f9e2OCEMN-MrWfTCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کسری طاهری مهاجم جدید نساجی:
من اونشب تو شوک دعوای آقاخداداد باجواد خیابانی بودم که به یک‌باره‌رسانه‌ها خبر دادند که پیوستنم به پرسپولیس منتفی شده. بله از الان به بعد بازیکن نساجی هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25656" target="_blank">📅 10:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25655">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OylnSll1Zio04qumMO2xUQ3qnnmS0VFX1a78kKGXtAsBxSmqGEbAnzU7qj3oT-UxM0gYuyoNDqult2idAYKr4tqM51AhuBjffj_zkesGjsBe_SN_svDGIDZU4DQ5Nwekuz0moAbaBIMzYjTrHqfWTl0vICJZu2dCnWiatRpI3xMOv_-DyLET7Aup2DX7V90WfiTH994XU63IR_zzwQYgD3qIIdcc3eaFo71_iJGysBqVbC_SWbnh8Wl0_yRuBsiDaaegqZEHvF_QdQkaXoTmxTwBUW0c90P_hIhBTe3Cdxm5JSczdtWOVHVDz2gzKLLw3UkvZOAbxSZK0_jCFHFwWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25655" target="_blank">📅 10:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25654">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=CmxMzGg8Z9n7MeRJ_zkMB4Pf5kfsI0ttrwCDCAu4ZYm3nqUpjDCFfQ6TW5CVFUDbl7Elnr9S30w111zH7Ac0ZVzGkFV8hke0h_OzK9bgiLB-WLXON88nfCD7tgnGHwOsr9JZU88DnRZjtY6vNXmP2ASRoGTyr5ieQCZ-0_FCnvIm9OLjtCS40f_dyf_h9tmFyaxyGN_OuS7r6rrG_Vu5OltF2bJB2rLKMK01kkqjLRALc9_qoEMToYdYSIZIiJgEdrkP5lzqMXjGMw62XuvMkzYitKUdSxVj_7P8JV5tFvvrz32gTUdyQZNWZ5kBkS-xgi7m1IJJS1pXmOLwlrpOqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=CmxMzGg8Z9n7MeRJ_zkMB4Pf5kfsI0ttrwCDCAu4ZYm3nqUpjDCFfQ6TW5CVFUDbl7Elnr9S30w111zH7Ac0ZVzGkFV8hke0h_OzK9bgiLB-WLXON88nfCD7tgnGHwOsr9JZU88DnRZjtY6vNXmP2ASRoGTyr5ieQCZ-0_FCnvIm9OLjtCS40f_dyf_h9tmFyaxyGN_OuS7r6rrG_Vu5OltF2bJB2rLKMK01kkqjLRALc9_qoEMToYdYSIZIiJgEdrkP5lzqMXjGMw62XuvMkzYitKUdSxVj_7P8JV5tFvvrz32gTUdyQZNWZ5kBkS-xgi7m1IJJS1pXmOLwlrpOqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ایسان اسلامی درخصوص درگیری شدید دوشب‌پیش جوادخیابانی
🆚
خداداد عزیزی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25654" target="_blank">📅 10:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25653">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=TS-bGC3qsO0zTeRGfUZmm_3Kqwz0Hl0QZdHyZjDibeWYUVi2Fd56atIOjZP06MJ01IGmXkrCptPWfBl5szsO8_fhtea9WzxLz8uw-akcKQDRO1ZDu_SzbZRLkHbn6CR8EGDokig5ZbT7_qnpqZlikRD2-aNUOb_vFx53cOunCvRrK0BPTLfUWa52BiLX11UYGs_MjlxqIs-OT16VAuRo9zaB82RCMi4a4A_dyDhd8y0lR2KhNDLYpf3EkF1rg8pysrOIfb-EPCSKcehNmPXuoKbO7_OcO0355Tn73Ms7t6BJ8AVjknwJ97X-K0o-c-iM4TvZjZYHNF74rfGRSb-dGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=TS-bGC3qsO0zTeRGfUZmm_3Kqwz0Hl0QZdHyZjDibeWYUVi2Fd56atIOjZP06MJ01IGmXkrCptPWfBl5szsO8_fhtea9WzxLz8uw-akcKQDRO1ZDu_SzbZRLkHbn6CR8EGDokig5ZbT7_qnpqZlikRD2-aNUOb_vFx53cOunCvRrK0BPTLfUWa52BiLX11UYGs_MjlxqIs-OT16VAuRo9zaB82RCMi4a4A_dyDhd8y0lR2KhNDLYpf3EkF1rg8pysrOIfb-EPCSKcehNmPXuoKbO7_OcO0355Tn73Ms7t6BJ8AVjknwJ97X-K0o-c-iM4TvZjZYHNF74rfGRSb-dGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند: توقع‌داشتم‌عادل حتی به دروغ از من حمایت کنه و بگه‌مورینیو از من تعریف کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25653" target="_blank">📅 09:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25652">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c3b52fc8.mp4?token=LMmLVHYwTjFfCRVSx0BGe82946OvTa3sOiG7vjvDoh3E1ZGVTe_3EzWBxR54AKOH-XAb7Ms6iGZ8Jd0k5DCTsIqDSlCE68A8_5SbtR1aIxEXYvBVfjMoFrZ5evjvuDrlhBJevqfh-8QFfRgwnnXdiGesjUgJ1I2rXxfBRmjNAan8v5mJQ4V4v_O-u0dOS3YsIpZmQVik-AsuFWCL4b-C-aYoFH2n_I0htSQDsHm3NEXkjgcQReoq7U3yEz9MRpYadCy2uX4gSWmAwfsitLcSoYndz-V0eFkuqRMOtdCGnjuys_dmNOPukJegybag0uQYzQ93q65mVrHj1x2W3rpcNDti0c1X-m4S-PvUuwqqj3xa_4wqao-LeBJgBjQbZZqIvjpDn8QSUNhksDie0269enwB3xTVAcQ-pL4Ge3htPgnUlr9E-hx07-APCwUUJ38YDYrEkocmMGq93KMFsDWHWRcf7OEU1b4_eMyf3SSHS0SZBlA9AhR7dffzcWckpnHYyp9PB-FvcbBY4z9QROBCfJNM7UOw6Ma-0lbLQw4FHLAc9ZitXlT8PUArRI-AXya3rFlK9dZWOEZeo8QnttLw5bgtqFVQa30JtHNoQ1Np5Dog25PYtKYqC5vqDeAdy1dVzzzejB6oH66ic9rEFSJ5yzjNXmUZAb9LDu7h4a3IJ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c3b52fc8.mp4?token=LMmLVHYwTjFfCRVSx0BGe82946OvTa3sOiG7vjvDoh3E1ZGVTe_3EzWBxR54AKOH-XAb7Ms6iGZ8Jd0k5DCTsIqDSlCE68A8_5SbtR1aIxEXYvBVfjMoFrZ5evjvuDrlhBJevqfh-8QFfRgwnnXdiGesjUgJ1I2rXxfBRmjNAan8v5mJQ4V4v_O-u0dOS3YsIpZmQVik-AsuFWCL4b-C-aYoFH2n_I0htSQDsHm3NEXkjgcQReoq7U3yEz9MRpYadCy2uX4gSWmAwfsitLcSoYndz-V0eFkuqRMOtdCGnjuys_dmNOPukJegybag0uQYzQ93q65mVrHj1x2W3rpcNDti0c1X-m4S-PvUuwqqj3xa_4wqao-LeBJgBjQbZZqIvjpDn8QSUNhksDie0269enwB3xTVAcQ-pL4Ge3htPgnUlr9E-hx07-APCwUUJ38YDYrEkocmMGq93KMFsDWHWRcf7OEU1b4_eMyf3SSHS0SZBlA9AhR7dffzcWckpnHYyp9PB-FvcbBY4z9QROBCfJNM7UOw6Ma-0lbLQw4FHLAc9ZitXlT8PUArRI-AXya3rFlK9dZWOEZeo8QnttLw5bgtqFVQa30JtHNoQ1Np5Dog25PYtKYqC5vqDeAdy1dVzzzejB6oH66ic9rEFSJ5yzjNXmUZAb9LDu7h4a3IJ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌ بهانه بازی امشب فرانسه
🆚
اسپانیا در نیمه نهایی یادی‌کنیم‌از بازی دوتیم درجام جهانی 2006؛ فرانسه‌ای که به زحمت از گروهش بالا اومده بود به اسپانیای آماده خورد که هرسه بازی‌گروهی رو برده بود و اغلب فکر میکردن فرانسه رو هم میبره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25652" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25651">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9cNZh8-Ho7SR6tmYJZWCCQ5PREJUG2TRc531obHfByhHMatBzKu5FukuA4ji6GLTHnBJbmYnIS9NUSRHATfj6vJGEqNCIKfMlHqlKE7OGrWfEIRSrN9aXF1LeYikIpnXPHrIRbU3DHlARJSXyjR1uVyWg4FL0_k6OU0hbSr92NatBAbLUM2RE77jqm6Zub8JF-zxeYQVvRqroEjWYHHzS920CgRZQvbxFtcPmrxy5SG3KMznwEavRki1jjUPM-eTWXtzizq9aTfS9nCqHmQ5mGGQc9RRMAzUZS9kFPnnnTH8muw1fxDIKYV7ORzWfq9n5a0Hvqh-TVJp_HPUGjSQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25651" target="_blank">📅 09:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25648">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/298c4f2fe3.mp4?token=ULxb71JDSZb1AEbQadLJMLYHCR2RHFqKMwFt-TpdsjGqftOIqYnrhQQX4qvPgGkV6SRRS4Wk7PBrm2dA8HqGKfbBswRZ0cTf9k2Qa372hmtapO-_gwqsusNuaQVo0kPUR3GPVxxyf-VrxWEdIlMJ5QlVbyzEtfU6zSvgGLm-3Yxw83SRDI1C4OKlqiN2BOWIVsHXKrAhYfeANhoqnohMXRyVZGWsSYRBQP245HgQ664Q4ajGzheC3xZWlvuLGfWf4gOmxny6d9l1GbQncoCoZE6UDgn9_73aQG3Ypb1fLSLi4-jWkVvWPySSwPfRsFSI0s89njm3DwCV6B4UBOiXgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/298c4f2fe3.mp4?token=ULxb71JDSZb1AEbQadLJMLYHCR2RHFqKMwFt-TpdsjGqftOIqYnrhQQX4qvPgGkV6SRRS4Wk7PBrm2dA8HqGKfbBswRZ0cTf9k2Qa372hmtapO-_gwqsusNuaQVo0kPUR3GPVxxyf-VrxWEdIlMJ5QlVbyzEtfU6zSvgGLm-3Yxw83SRDI1C4OKlqiN2BOWIVsHXKrAhYfeANhoqnohMXRyVZGWsSYRBQP245HgQ664Q4ajGzheC3xZWlvuLGfWf4gOmxny6d9l1GbQncoCoZE6UDgn9_73aQG3Ypb1fLSLi4-jWkVvWPySSwPfRsFSI0s89njm3DwCV6B4UBOiXgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
افتادن شال یکی از مهمون‌های امشب ویژه برنامه عادل فردوسی پور؛
تعجب عادل عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25648" target="_blank">📅 01:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25647">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlyp7QnlZ-DM6220aLNe3r2M49NyU_QifVckbIgBDR6cFdExiqAo6gqS7QJvt1HYxSakQ1SX6igojlyl-heg5oSnizLC8omXbxzr58CJjx1gRLXMICIFuyDQ-xqd5WxDEKcX-Exx4yqxqve6hPLxnK4_yxNl9KvEDrYY6tt7AVK0sMGMAHebRsRwcrMrZSHSrIUZTQuaPbwpwh7WIgRQMVL8q8m-vXt_nyVJy-no8GheOLL-Is2CSpFnCYHPlEkMLoY39ooR-CDtfubU-CrjdE8Mc8PEBi5ge5nzzA3EBs8CKYSq2SBA-Z1M_5u0KXGm4B8-5XhQyW6SI0jMFVTOeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی:
تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25647" target="_blank">📅 01:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25646">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U98Ut2NyL3zWMm6CwRhKecP_XPbYAagN1B-wOUcZfcmCykXZG8vjP5khGSS8tf_RV7lBNai0tuqVlSIW57ao8bbl-U6zBOwsG_rkFnSXbudbAgcwLUQg_VtXIoUrl7ieKo2NnpWbuT-MWYWhojcsz8k1V5PvZWOMmw4vllyDauPGpe6Ky8M85lY30CuGovb3bMlqul1wTWDfU9sijHvaLM-UsC_aNy5Y9C0Zjz0pziDKShF70rFemQjZvXp1G5VJmDFJLQJ3QAJ4Teao4d0R4SqGJqn_OLRgtHSZc-OkeXeQ6eCot8moKaxJpG0QjyHnbq8TORKJ-TjqM0eGdwBlyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
نبرد فوق‌العاده حساس دو تیم فرانسه و اسپانیا در نیمه‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25646" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25645">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e63bfe28.mp4?token=pAOuclXc7VqvjvzDptGyDa81Ceu5UvgRFHkhRigUZ8uEviIqlTV9a5RVfQDq5IhQOX_UQlvpf77cQp7fVyWBPRqVK3L18RPLc6j8NzGd0sgPGr4ncjYljkYZTgQgbwpPke0Uf_d1uGmVJYR2TnTsI9B0b6EyyT3NN4cqNeDS-c3GAVhNsK3l5LGypLPf8Ei-3gXBDFuVk8BhLJ5A3orAu8j4xJlrbiyubgzqemh0rd_V-NpEUtWaVl4uSP3YysJWy6EOfVn6dHJCV9yZ1zGR96g9hfKtV2QuNl2K1_4TXJ5rw0R8qFXKRJwzYkJvZeZIknFp-VPBspPXgfRvxHjdfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e63bfe28.mp4?token=pAOuclXc7VqvjvzDptGyDa81Ceu5UvgRFHkhRigUZ8uEviIqlTV9a5RVfQDq5IhQOX_UQlvpf77cQp7fVyWBPRqVK3L18RPLc6j8NzGd0sgPGr4ncjYljkYZTgQgbwpPke0Uf_d1uGmVJYR2TnTsI9B0b6EyyT3NN4cqNeDS-c3GAVhNsK3l5LGypLPf8Ei-3gXBDFuVk8BhLJ5A3orAu8j4xJlrbiyubgzqemh0rd_V-NpEUtWaVl4uSP3YysJWy6EOfVn6dHJCV9yZ1zGR96g9hfKtV2QuNl2K1_4TXJ5rw0R8qFXKRJwzYkJvZeZIknFp-VPBspPXgfRvxHjdfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25645" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25643">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZUb9zJGgXOLUJriy4iUeTkgXJ4QfxxtfD7NGpMMqLWNDzBx2QosNRO_p03cpLyblD59Ukyw-RBn6EAdMzy890KJFhhxGBJJrRgbqYs6zbpBDLHXfkuh4J02g4Jawso0c5w1fV-2vMO9omMQW3nCTQh_1IMZbL080SkaS1gmx43aLGZaii5nyjPxkrQBg2uKVB-iroBaNPzsF-CMjlHazdedrWmIh6HjD5W-w96f1TyQOalka3RaGDjcxRutXWdswFpFIwxD9oMvYKB4Q5vUeH4QKm12Bcx-aQ2om-qFa1bI3xM1abYrZlMZMh266BJny3RlIiUDG6OxmLlCqYjOCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
با اعلام باشگاه فنرباغچه؛ اسماعیل کارتال با عقد قرار دادی دو ساله رسما سرمربی این باشگاه شد. ارزش قرار داد دوساله کارتال پنج میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25643" target="_blank">📅 00:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25642">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98ca4a5638.mp4?token=TdAwcMwyyWaYKc4I7b6r_xZomaqiBBNxi_4HLY27jNsoGU0zDpILuCKAV7_SsmSi35uQDY5remP4X2-Ssqvc9UK4ngSmkG0Aqy-cpevs3Zyo6pIdfTa16rOf-Ly-bD5KqYvDj6SHXRV3GlY0sv49_s_4N9p2VinNRbac1choWHcUR-CB6kdNzUs4UmTNRqtIhb_E11dvUOcX38AnogE6kuQ6nHPAesQYPbbmusAhMk-puHqQctAzDSjfFo_CFJy9zfXLUu-dbLLqId1LfCMr51G3kEa4XZbU7bcFdZKJFR8RzK_Y1DgxRwmpUZmzRdyolEsR90gN5CAYDka72Nj_MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98ca4a5638.mp4?token=TdAwcMwyyWaYKc4I7b6r_xZomaqiBBNxi_4HLY27jNsoGU0zDpILuCKAV7_SsmSi35uQDY5remP4X2-Ssqvc9UK4ngSmkG0Aqy-cpevs3Zyo6pIdfTa16rOf-Ly-bD5KqYvDj6SHXRV3GlY0sv49_s_4N9p2VinNRbac1choWHcUR-CB6kdNzUs4UmTNRqtIhb_E11dvUOcX38AnogE6kuQ6nHPAesQYPbbmusAhMk-puHqQctAzDSjfFo_CFJy9zfXLUu-dbLLqId1LfCMr51G3kEa4XZbU7bcFdZKJFR8RzK_Y1DgxRwmpUZmzRdyolEsR90gN5CAYDka72Nj_MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای شدید و مجدد خیابانی و خداداد عزیزی که مجبور شدن پخش زنده برنامه رو قطع کنند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25642" target="_blank">📅 00:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25641">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3d13a462.mp4?token=F7WMF42KCbpAxeiAC4PWSvM0BdFPrsH6VPNOMWQX08mEPNfPgw_4tyS4s22G4Gu1NOc5G83KXo-fANpMZ5X4Pp_9q95XWzmMttR_6jyEwVviOjZZWNYPeN2Z3C5iO38qx7FHmHJec09zB7xRjtMBoOqgLCdqeMd86ofH_Mq2Thcvfll8RtFeTFDezhhbKIFQCIcnQf9wkwlzB0yuZF4ARNUf6O2YX1Qic3WlqMGlHtDzcu5_FD-NGzsok8VcqSMWin4g61DfgpATDlFEq0d-foXDfsb0V2kg3_SCB7Bkp_s4LMv4WxXFHzo5AGI0SwNqPpeTp_nuhGNPdG8xl9qEpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3d13a462.mp4?token=F7WMF42KCbpAxeiAC4PWSvM0BdFPrsH6VPNOMWQX08mEPNfPgw_4tyS4s22G4Gu1NOc5G83KXo-fANpMZ5X4Pp_9q95XWzmMttR_6jyEwVviOjZZWNYPeN2Z3C5iO38qx7FHmHJec09zB7xRjtMBoOqgLCdqeMd86ofH_Mq2Thcvfll8RtFeTFDezhhbKIFQCIcnQf9wkwlzB0yuZF4ARNUf6O2YX1Qic3WlqMGlHtDzcu5_FD-NGzsok8VcqSMWin4g61DfgpATDlFEq0d-foXDfsb0V2kg3_SCB7Bkp_s4LMv4WxXFHzo5AGI0SwNqPpeTp_nuhGNPdG8xl9qEpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
فیروز کریمی درباره‌انتخاب دومادش بعنوان سرمربی تیم پرسپولیس: انتخاب خیلی خوبی بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25641" target="_blank">📅 00:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25640">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-g1P5_rbGE-IignzlkknBCbvY2B9BA68Rn9eShAE9cTHZ2Y1GHPStqRSxIz0u4-3WAC1WG3yIVWO9MPDkqYcg9Ze8woNfjYtJOyU5CYzDVTN6HrEUYEMXpjKZhmb1fuEO53JJ4EmpJYUI33DTOmEKUZn-pZ9PzvxAkDZRQbHunLIZ2m4ViN_CjTJYX20uNmtbuO8YYzCrX8YoqOzxtr_2Z72hH8NwUo99IVMt2BdkZu5R_JXbqn7l_Cwu29h4jmVHmdeMFywpOXJjO0ccXkU24RNdRMRBb4hX9CW6mEuPQMr74L9DX_F0a_rtEoa9Q3NdiqXqBErBZhnljERur4Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
رامین‌رضاییان ستاره‌استقلال درسفر خود به فرانسه‌کیفی‌از برندمشهورHermes به همراه داشت که مدل‌آن Birkin 40 است و قیمتی حدود 21000 دلار دارد؛ معادل 3 میلیارد و 800 میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25640" target="_blank">📅 00:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25639">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnU6Rv4oM2vLuFkQvzuZBdFZrDpQVQ2CXuAKXunWe4REqmSxXKR5KItmBO3flvjB_qa-ASihGK7-wR6gigP4ut4b8mRKF877rDaN4Zy8H9uZu-kX40ZcGYmCYiU8B7KLkIdN3HOhUy4ycJe4yodHyQI74F6Zt5-4sNSRnKLY_xX2-K-DDc3V-ovqZQGLVLroo7YxMzQzUuC_Vjrmn0G7rXxZDAc-yLril-30eYSJhYPTQytYeu0PxC0R_CezGvgYRmfIGMh_6xksN7BsBoWgdK5LDLIDrwEH37sSRyIQrI9ZbvnNsAC65yeRKrXbY6YAuHs_oqw0ixJIgtGuxOrBfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس باارسال ایمیلی به‌باشگاه‌‌الاهلی‌خواستارجذب رضا غندی پور مهاجم 20 ساله این تیم شد. اماراتی‌ها پیش‌تر مبلغ رضایت نامه غندی پور رو 2 میلیون دلار اعلام کرده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25639" target="_blank">📅 00:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25638">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwaYKvm5ETecedpAls7JctjksrxgsahYjcc9b1Kmmb4CZjclXIgiKudRld1xtWNrvs_Nhl4IYi8AeiVhAOsEnPqIygzjT5DX74h0be8xfpq6TSeowpUMutduCbGXTG-qdnMO79gTWnrQkmv3avkgGPZCd8TddsZ3ZBemHNdJQo_sBGvgjbEuJDKcqBKKuL9Bm0zGmZ5CpJdESBSwsT65OgtphYEjaRFOG5p8VYzAwFCfkAAtKCaFdkIyvwGAPTNKx5fOyQiU4qt1fNwBBd2u6js_UikEnkThNI8Pb03pwhZeTJrNrjRpG6u-EPKbRxaKOEXbc1DEwfeRlD9CqUKBhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
این صحبت‌های مدیرعامل تیم نساجی نشان میدهد درصورتی که باشگاه استقلال در جذب جواد حسین نژاد عزمش روجذب‌کنه با مبلغ زیر 3 میلیون دلارم میشه این بازیکن رو خرید. فقط مذاکرات باید حرفه‌‌ای‌باشه و بی‌تعلل مثل آقای زندی‌. گفتنی است باشگاه استقلال برای جذب حسین…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25638" target="_blank">📅 23:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25637">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8ae1ae07d.mp4?token=Ei4qEH_XFgwIn4EFzpAq3Nbmmw19ixWaP2DLcEFsYPa8Q_cE1QAxID-nZr7T_mPA3QXSY_TsD4au9wDDAKTbBFBWPt8_tVbkRMoKdBEYkJ4CR_CUUVlZXhkMvR1eZQ2Kv2wNr2ZWR-rnHTK7xXCA530k8FDLS3slXpgSdlqpQVvllHG-vFOY9JHRV4597DIqSwsMJwBFL3mXtmGeP7Z4QDD-UhdEQ_cVsJTEw61d-qAax8K_7dOYHwLNvNhUC3kJeIpR5apBuMV8cl8uWTZU17qRs3jWo0UPXK_mXtVRwsMaOpkiqLRf9pbrtBNh3YjrvuWGGHhsEq7qoj6U4DHkkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8ae1ae07d.mp4?token=Ei4qEH_XFgwIn4EFzpAq3Nbmmw19ixWaP2DLcEFsYPa8Q_cE1QAxID-nZr7T_mPA3QXSY_TsD4au9wDDAKTbBFBWPt8_tVbkRMoKdBEYkJ4CR_CUUVlZXhkMvR1eZQ2Kv2wNr2ZWR-rnHTK7xXCA530k8FDLS3slXpgSdlqpQVvllHG-vFOY9JHRV4597DIqSwsMJwBFL3mXtmGeP7Z4QDD-UhdEQ_cVsJTEw61d-qAax8K_7dOYHwLNvNhUC3kJeIpR5apBuMV8cl8uWTZU17qRs3jWo0UPXK_mXtVRwsMaOpkiqLRf9pbrtBNh3YjrvuWGGHhsEq7qoj6U4DHkkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند:
توقع‌داشتم‌عادل حتی به دروغ از من حمایت کنه و بگه‌مورینیو از من تعریف کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25637" target="_blank">📅 23:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25636">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4483a354d.mp4?token=YAZQRGkB1JF_lp_0H8zTtUP4TB4LcLxR7wJWrBo7v9enywvrmkM_olw3tYVzDR4V8cCfowXhGzNVJNgNg6942s6K-pFp47hvfA9KmbJIqnz7iICCSrDoAgOhogxF1_TcokpZqKwHvWEo5lKOzphfxjDXoDdR6WM-SOp6ZrDtLpWa0GcysA0-ytEGj9TUH8y2vdrvQ1t5XI7-2M0OZpy2OZ2s42VGKoMFIaCaVZhSAAkyGBmWEHdb3iSfi9LHP27lvFesRGWW8V7jPZTaT5Ff52f7HT3rFXHSFWc6dpdtYu40DdZCUTz9cn2l0tm3WwNNu6tJ_tocvCDes1X8ada1eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4483a354d.mp4?token=YAZQRGkB1JF_lp_0H8zTtUP4TB4LcLxR7wJWrBo7v9enywvrmkM_olw3tYVzDR4V8cCfowXhGzNVJNgNg6942s6K-pFp47hvfA9KmbJIqnz7iICCSrDoAgOhogxF1_TcokpZqKwHvWEo5lKOzphfxjDXoDdR6WM-SOp6ZrDtLpWa0GcysA0-ytEGj9TUH8y2vdrvQ1t5XI7-2M0OZpy2OZ2s42VGKoMFIaCaVZhSAAkyGBmWEHdb3iSfi9LHP27lvFesRGWW8V7jPZTaT5Ff52f7HT3rFXHSFWc6dpdtYu40DdZCUTz9cn2l0tm3WwNNu6tJ_tocvCDes1X8ada1eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وسط برنامه زنده شبکه ورزش برق رفت!
رسول مجیدی مجری‌برنامه: بازماانتقادکردیم نذاشتن ای‌بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25636" target="_blank">📅 23:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25635">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBptpEfh46Ic6ZncMBpys2af5e-io0lofpgMqCyICJu6NpJa3xD5kPAXVOlRwz_r8ChcAX7Ca5v82mAG8gsFGtSqHmygaXXy9JDGAuJJQg42pTYlDcYccOrrcEciprnu0sUh7yA9EW9TTofEouySkWCqoxW8897v0g-RQH60gl68wsLOptFUn61yReiJNgbi1vTPMz75AzttRfqqeVz50m_NiaF-RfaLJA3q776gTJd1YEMqaRGJ7jxKJ5TfNZEuOJhNUbU3_mCom-0N9MIt11tqv-L-0fweFh9KDjBskwc_3cWvz5d7AOSRcpJfyscsiUHGD8-w0FUNneo1Te08zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
خوزه فلیکس دیاز: مایکل اولیسه به سران بایرن مونیخ اعلام کرده میخواد بعد از جام جهانی بلافاصله جلسه فوری باهاشون برگزار کنه تا تکلیف نهایی‌اش‌مشخص‌بشه. اولیسه میخواد که در همین تابستون از بایرن جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25635" target="_blank">📅 23:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25634">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaDyQfOB81QB-i3zcje95CaNask3ZBXXsa7TcpG8oY5pxAtR6-crpFXPpj_7h8CLbnDO5pNqqjk-QPqNnCRlxL2Blb3T0myeRpDorIOTxlM1jpxBJcC4b31DuZ3L6otvvvOJHLtqwNfue-DJqM3CJ_hg7tQaIg6Pjc-ht157j-VR-uU3qOFamUl5c0S5W2J240Ws8FnAHmkgODDATSuT_cTB1uL0R1jxboMlEz7Hz2CHOW3lMqHcA5fxaS7gxy8sywTYZIMQzt75m4BwA5q-Wetb_ycNO9uM-UBUOlGrXNL_LasVgpPGXprMpbf8kQlbapC-u6JIp_7WZwxyIGaS9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25634" target="_blank">📅 23:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25633">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQIBUP1Ctg8G0JzGjhksHbUG0gl7TUTrCqsmyv1nX3N1yjbpcZS12rB89B8hYUGWuRd8TZunJFwWCVJdd8yXGu5tiBs-GU3kktxO5LJQi32TXO2V96zybixnxqXeja1A5bFrHusA1gliFwuW9DQmoKZJkWFjeRHdhSxJo9zgo7pI0LGELQYg-9ETgFYpM08jO7SZQfYqwdPUo4GxrudbXgOxTkudsKfdLU5N0tQS6HA-ekcvoHN5bbRQgfEWgYiMqBN9roRZZD4sLhgBqRdl-cO3EzLTnqUWQH-dqoanEV92PXH88VLHEybPgMoOcgASuasVhsqaDFI_20Lsqo-qhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال ساعتی قبل بازمصاحبه‌کرد و گفت کار انتقال محمد خلیفه و بهرام گودرزی نهایی شده و باشگاه بزودی پوستر رونمایی از این دو بازیکن رو منتشر میکنه‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25633" target="_blank">📅 22:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25632">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2kTBOzwF1D5YYWNldfJ6goJo6KIhzvQY1uqmNmOK1ujrMQ7Zgoyj49Gxr1xyyqTYuFsMlCTj2QfxXolpp3wzCT5lWmfITiUYcL56KRC6v9AEEmj9rxHQXEihuf9Hyp35eYjbxrBGdOSyRWqxVjtDc03JKqMqzoiLvnsvhNkPPx5eu-cc7v-fOrCXITRHZVbLFbj7EJ1zR7jsAnm99yFKse_ixysZfgZ8FUvuuUbC1wzhDTm7uEd71FRxSjU3hW7u07OQnKekiZbre_Jcm4EV21mfZsNBnJ4b2wcIGLJUmQBV87ZkfNdt5yPnqfT616Y5JlwGZzaXNCiJnwJeNxSDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25632" target="_blank">📅 22:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25631">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4c24c7d9e.mp4?token=d1cmxMlvvYKaafBvZLX04kzfcpQ47zbZ2XtigXbU6aCXGgADeF3L8lWDmRAopuLCQaly_A0WCyjJzB4CF9WX_C48xJrrN2KzPp829ldFdNJvNK3lwId82Ejx5N4hgduZXTU8OQMiRyiwQwplfuzqmWlip7fPliBNUM3pv1anmPJBZxWicjgJxPkLPyU3yfVNa9rt9_bfY0E0GadIwiNJ2N13-yheXNEyJObdl8HTjb-fb9dI_NwPJgrpggpXy8Vfv0uS4RwEUSCQfgywsBS3QMdZaLdOopRHZ07LF6oigBOXipVGT4xwRE9SQzy96M7cwgdMH6Mo_rVeKan8EvpfVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4c24c7d9e.mp4?token=d1cmxMlvvYKaafBvZLX04kzfcpQ47zbZ2XtigXbU6aCXGgADeF3L8lWDmRAopuLCQaly_A0WCyjJzB4CF9WX_C48xJrrN2KzPp829ldFdNJvNK3lwId82Ejx5N4hgduZXTU8OQMiRyiwQwplfuzqmWlip7fPliBNUM3pv1anmPJBZxWicjgJxPkLPyU3yfVNa9rt9_bfY0E0GadIwiNJ2N13-yheXNEyJObdl8HTjb-fb9dI_NwPJgrpggpXy8Vfv0uS4RwEUSCQfgywsBS3QMdZaLdOopRHZ07LF6oigBOXipVGT4xwRE9SQzy96M7cwgdMH6Mo_rVeKan8EvpfVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم استون ویلا یوهان مانزامبی پدیده ۲۰ ساله سوییس در جام جهانی رو از نیوکاسل هایجک کرد با پرداخت ۷۰ میلیون یورو. اینجا هم مارتینز ازش میپرسه میای ویلا که میگه آره آره بزودی میام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25631" target="_blank">📅 22:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25630">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2zfCHXePKhIeAKhR33kNbT_N3Ib_ifTCCTBxxZvQMtq8lIJVq56BpLj5V6DpFKX3Op51zJ8tiQiompU2M10Q61fkrkhk6OxVIj_T2ewOwjCVa3R-oaljf4nAZ_GzDhg25WEP17c-uNY2ldt14xwAuc05AgwAzgS31kFE5i_5gmlZguS8dLyhdRdzkoCE4YNXm4leRxpJcHQG7PvpsnkYQKA_b1J3e2vxUUVtP4_wG6SLGm2pLw4rPAzbzYMijtU1JTLcoW9psN4IaXBZJfQNsNSbSVbjDnDoHy7ve1sFveXPXV6ZXz6IZMr4csLedi91UYBNLJf6AwVaksiIQ1ypg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پارتنر جود بلینگهام ستاره انگلیس هستند که قبل از هر بازی حسابی به جود انرژی میده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25630" target="_blank">📅 22:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25628">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l69qXczksn0wAyaSgo4aESTyRpflNTlPB2qWMr3e7mHN6J_WwP604lp0O0ZyKe26w_goVQ4zzZc_x-SQ3cxLQvGsDI6ZtdpuN-2IMXQcJQXKadVsCLwumisjqK496dbMSxizGvVFO2pNg3ejyyPP5Cxyl3cvmsyvTwQnZmL5WglZFrHOs7Eno9OqkI8H5nLeuIfNdAcyxgqSt_t0owKt51CLcSvxPnzFjd1yBwWfXL-CIGNYsKQtPFmpeQwvGC3e-IOhsoaT1O11P2dD0-NPz0wKr2zrXoQczmtjF-0F3u-9Sk_ENaz5Lklsh4labQ7MmOaJUh1nK-gXguWuYS9xSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#نقل‌‌انتقالات
؛
کرارنماری‌وینگرسرعتی 19 ساله آکادمی فولاد با عقد قرار دادی به تراکتور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25628" target="_blank">📅 22:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25627">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUsHLDyNDx14dKynuz_zlq-nIy1o0p7jfNiztHiStQAcQDoVh-3iM8QTYXKuW45rJijujTrdUelBjwWGutrvhZvNK_9QBJuUlptuyBAbQJfchpg0le4RztAvoLOHmQh05J77sUSOtyzHDQkBPCWnLB-lumd23UlsoMAFtPTzg1rrPxtX78JBY4g6o-Am9xEPDYUrMbuaGdaHyNW168fjdtuJwO_xaudrvzpoo2OrJQEdd6qmHSyrYw-AaPurLnm5xmFuNDXHGs-BcsgCBsXMj8rQPmDRdJmtsqIIT4Voc-kACU1kg9TQznvx_lysKGT3vAeDQtmIn3XOHD0MtQxyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌فوری‌نیویورک‌تایمز: ترامپ رسماً به کنگره اطلاع داد که جنگ با ایران از سر گرفته خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25627" target="_blank">📅 21:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25626">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGDjo0gVePIIayG8PrB1roHV4CwNQ_R9SkUrvh_of7-jp2KvYnGIJZi-Ln6-iyR-adbc5RebO2Pr02pUdb3wGQ1ZtC3mPrpE3ztCfjIMa2tM7gASbD-07q0VhxHl8wj8yOTFQyClAxJii9U48-LFpoDTrpop-gtp1WYKOvnc7xrQB5uMMY32G2NZyV9aSXbuEtH8FblbuUh1RFbCgXQnmhLoj9PGkkl0q_ifkCrBvBgtUjCzBbEHaW_GHf4zekFdkArPAWPvzQBTJOb-YcPOOvSmY3h2P4Yibd8Y0NCG-6jUaK0rPiw-FatKI87DgU8QpkWjs_8BSUS2b1dz434mkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25626" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25624">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vgjVs5UZGzeJLBbaCGnvqV8uKsb6CQdCvJHbKrdBdUddVJFsGqEyUs0M-mt6cS0kT3RqE_LA681HYr0K6y-wWHrgiXdP4p5CslIwx5YsUnSwWKSHnUfDt2nT_4HOduOSqQBibB5MaJe2B97D40kgIDOyGi9oPc7ztjZIVJicUBg-b-pgLyf7NabVmE25rvA90h9qcsQJyglvTYOTLcPr-YENkIw4eWKD5wq39xdMIprx1XsJJ0qapOEMLvFqOah6Y4zn8C5L5Ao-LzSUNJOfRGPKIudYIq3r-sMNHvZ6qbiMFLpQuCfjC54j0yhTuP2CfHpQwhePvyVXJMwCtckGBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fic2HLSUDXmJmf9ok8Suynf-JT8u2_i14ZxpKi7CB_DCieqlitQPD0zrHuZp9ycC6C7sRI8n2UeDLy-s1PUNkfxTuncgOlaNCmX-UoEfvfFs-yLYOVHz5eLgS4ppCOg_vsN9PMHGlpZmUJVgBUYvzOPHHv7am-y4CCxIkpS8e_tl2KVOqZ4y2K-FDt3F0-DOgakuB8ZiDaVHo6Mhqebg0Ljy5hPE05gQVa6gLtD4l3yVy3AZ6z0WGRr9DLRpWDF0BMVlkG4_OgMvJysbm-D5akdW9Q2uqyX_OVwiwg_ciqT_sfjPwhye31OrvZSaNELq4eQM5CuAO5hM4nKXS3E6mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25624" target="_blank">📅 21:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25623">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzFf7bztCRxTEqNW7xwQG0gYv0b6DYTBnx47AJldiwAEitPR7AGfEiaNRQAvzHAgVONnM-u_Ub0BxXbJPPl4V4i_U1qIOSrDDbKm6Tt_qnaZUl--xDxDjdk6B8urtugtQRUG2Sl4ud20CsVq1i5J8SfnfGt-ehZ3iYkxDFVmfWdt6oTXxdWXx4OQb4uxn7ztWPtqoGeza8KdIIdgLzQt95e3dQX-huVblb09j9yWw87PKyfqCvhiZrkVeO0jqymRWMW_mj7Jf6lFsLVOWoguioSyWfPTHpfpS4DPPyUB_tEr1-j8qxQSyhUcWQ25GmVwPkVOhg3YnpgAYtOLOyqY1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/25623" target="_blank">📅 21:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25622">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDuf5dCbMH2fh7bwqzk3YO7N67Ol7y9N0tJRW4nUEhF0olPMchlnh0IM4-cFpfDuES66ycbkLU8EjIycZnt2WuevBhnLifC3waJCGSU1Cq7rFcI_IYtJsDP9gLQNFT8bBMSScBK58yUMmHVwdTQF7Wk0QMlP8R51CIpHIiJGkA-aCbugT7FlxeQarSN65w9JgS-tJ96s37tFgyrybOSo7NcjOok7IjlUCQPQvTVlCO07CuYABtDBYcRv8a81QLBLpJ6EzECYpiyUJee1Yk7AxqM2ayH_D30b_hiUj0zvpyNCklJWzecNzBhA7uTPpA6mkJJrQ0JbCFgOgSS-wO7tEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعداز منتفی شدن حضورطاهری‌درپرسپولیس؛تارتار سرمربی این باشگاه در پایان تمرین امروز با حدادی تماس گرفته و خواستار جذب رضا غندی پور شده. قراره باشگاه بزودی با ایجنت غندی پور ارتباط برقرار کنه. غندی پور از تراکتور و استقلال نیز آفر رسمی…</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/25622" target="_blank">📅 20:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25621">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acK_gGyYJsikgE6VhMm-8a6bhIZY3Uyr0eB6BnvJJDyiXhTuCUzBuTL4FkzMP58OPJvk91vZuOYyyc0FW-g20N1b-2QFDxzw7Pmbpzx22SEWb4ODUKdc8XWnLrHdN3UjmXivRmtWHnxHPv-uEsCC_PWMhJOmj9JzxAr-YSXMfKPi82Mb_WmLCi-M0E4Ur9kPgeLFY2bRnnXUBXHRdMlWkJrfY5-uuIfg85IgUBh_FscTOrPoXcufKvKTrl6WtTGCy71uRUM1thRaz_moCEqJJr_Zd2HtoNl3pIGyoLNxklOncywOFHyVw3IouWPt7rFidG4QEop1amXHRHG3mY7wjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25621" target="_blank">📅 20:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25620">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lf7pgnMk6UHPWWCgk0GwD7Y_Br3fDA5Bq5uM5sTDZeCKNObXaJhONKJe5ifsd3ObrziS7iJVuZVbMSjv_wkCsMhNblwuatTLeUd_0AnODn3Oo5CcceSWQGTZ1tCb106mqCbkjI8ArFJJap3TQY-qJM3gJPVgudUBzLdk69UuJO-0vqng1FOZx9Sj3ax4UXxR5TbcdH45Fqemf3FxmVK7waOFIVgUygK0vI32Da2lczTNpQKjwpjOQpaorj7bdxyoljGkOQLY4JnsLQuVtEEQqqOGx3z7L3opAB2GR-aA1ZmYxItyX2u6rXx6wUSNQ7D45RFIlFvRWnc18x7SaYaBVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
خبرگزاری CBS: علیرضا فغانی داور ایرانی الاصل قضاوت‌فینال‌جام‌جهانی2026 برعهده خواهد داشت. فیفادی بزودی این خبر رو اعلام خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/25620" target="_blank">📅 20:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25619">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw9UKj9ZshIVXD6yN_WbCzwnEDMXo017Z4SefsBirRqLifix9aBLRGOuWQmboblzOe84it61T6MHBlYaSlBemW1rpywMFI_RLcRhaquY-4FYK16-RwiX-XSZYKMuycjmJe6RgGNEvEIf7K-jg-57tN4k7x71WcxQLnF-i3l2geKur1XlGykpUfY1hOUZuns2gN5B2g2z_1ZgMOF8VN94fOgUYz-K105EIQoHtjtbPUD2UwI-3FWhyoAMf1v2sYC3FRUxpSZy4grWN14zXXnHoz5pgAx9zeg6EXzLab-wJnkgyFYWyfeVzUdzS5Xm5MyVodqfRayvKC_sp5CIxpq2SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال: باآسانی برای‌تمدید قرار داد او به مدت سه فصل دیگر مذاکرات مثبتی داشتیم و توافقات خوبی بین طرفین شکل گرفت. امروز آسانی برای دیدار با خانواده اش به ترکیه رفت و به محض بازگشت به ایران قرار دادش تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/25619" target="_blank">📅 20:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25617">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0a0hGLGsMiiLjnoeBx0PcQ6sJNZIxbHne7GMbkOQF_Lha9IUPmwlG0iGUQsoEoVLsc2lPuP4ZbdexuEeAh-SYDmxMaNfLiLbYX4j4wyFAs4lLnSvWx2DVc5jVGT6Yy9nEkKzqnEKpogmNFeBUAreCxNwjG9SUxxZfpSoOXM2GRTuWC0mxU37GTqMSKjYKumHtJM9DQtXo5p9SwDpvNdbwqYkDeDaqkhlpUgVifl_2y_dol7DqBlFROAt33heGZC6fEkC406_IBYD7kEx5Z0e3zViYpkZobw6mrUYrNwrd2ZevCzRcBHNOZCfFi6ilrbiaXWf92WcLcmU06S0No7kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/25617" target="_blank">📅 19:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25616">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cD0Dto3wTUTXOWClKHcSrgNH3oe4XJggo8yBo0QMrdY7_W7x5F5pLuO53DvqxeBjCpAxn7T8peMbvIhx4CGsYO4UIIL1UudEM1EZwUUBi6Nz-PPWXhOJGWif9zo_lOqECwfpeOrxWgMXDr2q3Ne6Ic0Mb6KsFOhui4MSyTiNk6cLtzhQ5sjTG7_AyNhzXuEg2mPdY2IAatbtie_lVd0TTI-vj1eRCmLbdpnIUujTcxCxioIKg6qkpPyEWgWxJJ5BzjH2lWmIog5ZUKVf2NyHzgBBF5b-4sHSE8jrrcLEemtp5vNlqyDH11Nl0vYSI8PjDeza4dXQgiCMENO32gY-Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعداز منتفی شدن حضورطاهری‌درپرسپولیس؛تارتار سرمربی این باشگاه در پایان تمرین امروز با حدادی تماس گرفته و خواستار جذب رضا غندی پور شده. قراره باشگاه بزودی با ایجنت غندی پور ارتباط برقرار کنه. غندی پور از تراکتور و استقلال نیز آفر رسمی…</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/persiana_Soccer/25616" target="_blank">📅 19:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25615">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xi5Rdmd4km4ZY32kAFwjpq96EWLJa3H5fBXTBZdePTRpeoSKfuzZ_kqBysB1XmZAyV79B9Fi7OSGKP3h_AzORpGWCyB9M438aszxxcpF7sz9GGsY0xTJmDvitZA0iSr_7ke1Na4ANziki6PvfihaKk-zpAIYxb4sk38ltrqrvnY6GZE4gj1fCZM8Rk3lGzs9HJZcT8iRiVmuTiLt5cj_n6srgWGEyBccVEcb7-rZIOLUVW8XT9NFd8btseo6_-giwdyyO4Ga_SRBPgDJZDDA39zNrrnMjscFC_9VLJKxwFZ23iCUP2yQcWW44OcsabpicOP6TP3an7bPSgEGW-_Zhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه شباب‌الاهلی پاسخ نامه باشگاه استقلال رو در ایمیلی داد: 2 میلیون دلار نقدی پرداخت پرداخت کنید تا ما رضایت نامه رضا غندی پور رو براتون صادر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/persiana_Soccer/25615" target="_blank">📅 19:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25614">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d281ac96dd.mp4?token=M31o8JsHhiv_MS39eUXYkse6WLQCJgC3h4l3gcMgjzVLJJsOJ4U5IPslLOP-HV6ZbWC_cVALs4RsM4s1cUtL05EC8O4UpEMk_zNXsg-YtRmzNnqIIzQtjbwW0uTv93xyyXZ3vZkUKA94XZgxFL-e2lJvv6pFGanrHrR7-b9bqO9Tu9tsi_t8wVR8KSHFZt7nLRsDRO5AQnNyYBP0QjsBhI48kYqePXZUk0X9TPiNBdELb1--Cu6mfs9ZXgp3q24OysH2T_xlkpNd39S6eVcerA8MvqKzx4yPs1YJZixbwrm7KzNQ9h9_R2S9vefN4jfvzguh2IyaWNrWXAdrdxXrFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d281ac96dd.mp4?token=M31o8JsHhiv_MS39eUXYkse6WLQCJgC3h4l3gcMgjzVLJJsOJ4U5IPslLOP-HV6ZbWC_cVALs4RsM4s1cUtL05EC8O4UpEMk_zNXsg-YtRmzNnqIIzQtjbwW0uTv93xyyXZ3vZkUKA94XZgxFL-e2lJvv6pFGanrHrR7-b9bqO9Tu9tsi_t8wVR8KSHFZt7nLRsDRO5AQnNyYBP0QjsBhI48kYqePXZUk0X9TPiNBdELb1--Cu6mfs9ZXgp3q24OysH2T_xlkpNd39S6eVcerA8MvqKzx4yPs1YJZixbwrm7KzNQ9h9_R2S9vefN4jfvzguh2IyaWNrWXAdrdxXrFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ یک سال پیش در چنین روزی؛
تیم چلسی با‌آتش‌‌بازی‌ مقابل‌ شاگردان لوئیز انریکه در تیم پاریسن‌ژرمن قهرمان جام باشگاه‌های جهان شد. دوره بعدی این رقابت‌ها احتمالا در قطر برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/persiana_Soccer/25614" target="_blank">📅 18:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25613">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5adfb3366.mp4?token=kat49Tx3VCsRaCL8mBWDd9WC7UnEcjzFF67IuhbDLJk4JSozWHRR8uw3OlJ43CKuF62QlFzu8eZSXHyzYzI0WKh7YfqIzu97gVQFgopNkaBe4aIEgNkmUqvNnhHOIT6RYLyCGTFuTLAUeApoSpXEaDJn0jBBvx1AxEfoNIo6BII9IMpLzGlKgS66VIfKUjWAaa0EmdbBkJcCgHn1hTmKUv_gp03Y0D71riml5KZTXWy_-COTrFpUz_ot9KSqrQdV5Gt7mrblowuRBFKdCYSBAJ2kXnNKSqrK6itKXWS6hmQzGTImAcj_VhYSXTCiPRYeK9TSBKoUSDHNy9B8A7HY1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5adfb3366.mp4?token=kat49Tx3VCsRaCL8mBWDd9WC7UnEcjzFF67IuhbDLJk4JSozWHRR8uw3OlJ43CKuF62QlFzu8eZSXHyzYzI0WKh7YfqIzu97gVQFgopNkaBe4aIEgNkmUqvNnhHOIT6RYLyCGTFuTLAUeApoSpXEaDJn0jBBvx1AxEfoNIo6BII9IMpLzGlKgS66VIfKUjWAaa0EmdbBkJcCgHn1hTmKUv_gp03Y0D71riml5KZTXWy_-COTrFpUz_ot9KSqrQdV5Gt7mrblowuRBFKdCYSBAJ2kXnNKSqrK6itKXWS6hmQzGTImAcj_VhYSXTCiPRYeK9TSBKoUSDHNy9B8A7HY1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/25613" target="_blank">📅 18:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25612">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORVexODQw27UXLFTNbWXZAPh03O3gn5QVLw6NwxSecea7STG7OH4_s8fvu4hiz7-BzgwGUhD6BSCBIYJbVx9zM7LlsSfk7-Y-mP9GSIkN8I01L8zllI_fQCAIXyqiWBLIFLjZabRCDdICuEv0aZ0rwWouPUidqki1DyofTfr6NiYJuOKoSX3cih9LSULaY8LlXTBZQlsDNAtIxs4zDE1VrCxO3eeDuMeDq0TFHTeQsIlrL5CoIu9oVcPGkUzJeKaMVvIYbgE9nWWdMLjhKNrtt2nw8O73aBBc4cYfPKmG6EGysT495aej4828pd-WISLpcrqVzKtkAf82KgrycPfCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی برای فروش دانیال ایری به باشگاه استقلال دوهفته زمان خواسته تا درصورتیکه پیشنهاد بهتری برای‌فروش این‌ مدافع‌‌جوان‌ملی پوش دریافت نکند این بازیکن با قراردادی چهار ساله آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25612" target="_blank">📅 18:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25611">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsESlZUh7-msD7vM3rEC8WnE4Q3NlMewp0-Z4S_RiExeOGLwh_4lEskOqzJ11-lW3s2yGzfLIKTTNJtGW3cE00qyz5iy0LliUid9MiLJRUxUzze6aY0M_NDfGvZyOO-YnblZxS_InlhaQ_JLmedppSHvt5UDTzKDafxkOrP_OUNcw8TQUBX1ta3TWNOBanP9TIaoGTm54D_vhXorsG-ZaEB23Lc6Ejr9warw-AmcmneZm1xce2ys8vNdGJdwpJj1NZ-1gnNKqZ1KU9ZpG3uQ__GGw4GxrbRbsDoDbBv_9ddgtAJz5CZIy1psiLycWDKXQoL2G5PsJF9vou0x5AbXaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
مهرداد محمدی وینگر سابق استقلال و تراکتور؛ باعقدقراردادی دوساله رسما به تیم فولاد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25611" target="_blank">📅 18:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25610">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jt2c7QLBAvHRKlYyAS-yQQg3BBVIxFI0spf18fO7DY_J0UxpW03ddYOH61RzOM7vrm3ZvI-to4b082VH3StuUEccsJ1aYNZy2Jtruj_XCIh1cklE42WA6mRMtMrpWpEACBT0p4TVFJBCbiMr2cnzIviSDEC2U-1-BxRAX8eitv6P4HKldT7X8RTOpb8ZoPhLnNBgBOeK5otn2m_TW7HgoY4TxGTJ0ev5xhrXClMPxw5P8idFbHRyfZD1jXNU6__9XQ09MIFt3hVvBTsYqdWgdT1DtrfsWe2PT8LjgV0jsE01pibw2g6Zwi6UUSBPRJ2G-v-q83c2W37ch9edCv6QTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محمد کریمی هافبک طراح سپاهان قرارداد خود را به مدت‌یک‌فصل به ارزش 65 میلیارد تومان باطلایی‌پوشان تمدیدکرد و در این تیم موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25610" target="_blank">📅 17:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25609">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7e39tnaao6ccj9zUrMYLVYoZrUn-L-frfjTPsWH-t51tKLHCOb8OLuc3RsPvgNQHRuGobfCIcSOQNy_cvi-vp9l4d0gI1rI6pzR2VxZsUow6Xnuj_W_wMrjIS-Dq_o9c2X8ovgrX4ZdcA103nkc7FQasU6mFgHctElOwjlu9pdaUdqsAPNcZmI3iOxACZLn2NbAAQCPrQALBK1brKO36dFXq1kLTYCFoW-yJCRmoRRPFGfhQMaBJw5cvSURb-_xppmpruDpN63fVe9Tb7CU4KNddPDiLvUQ4_zvO0xeKjahsBqY_C1jNjHxmK36qGGhRgdNmdHT8_iXYruyY5MLyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25609" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25608">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxOpgCJ5jllIf8KCkGE4i-gLIUQA1t0ewfNWGPGi18AVeGy7P-oAshbE67-Ya8HYY5KuTawgWWwBiSbDrSux4kxCNoBNqs38nNv6U0_Qr_VzXEhfgaBlG_S-2tkbLSFYj1DKPiPv8ubjwc9JfqnYRxTfW6UnyGXrf2kPg3b3vTsPq1zyvUSpt6bm88IeyV1EYelh_zibI2_t35J1s1TlILDOS0nOqAVZxhBOol31DTRSRelQvbyyYxJm9aG7sm5esZy5G9vhXx1it41RtAxKFJ-y15BzzHGZO7AyYTHHXkZizkgOXphIzxiR87jh9gBR2y4D1BSKquI8JbrcOvZ8GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
خریدخوب انریکه‌برای PSG
؛ لوکاس دینیه مدافع‌ چپ آستون‌ویلا با عقد قراردادی رسما به تیم پاری سن ژرمن پیوست. آستون ویلا 10M€ گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25608" target="_blank">📅 17:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25607">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCOdt3-su5cheaWY5LCrJV9F6RqM9aeJCtg81hXjJIQ3098S44F36V5mitjrzaPCJ3TMv6Dw_mWKbWtEVb69kF3cqCyeydKh-Sp1UrDQm6561-_ibbovXCOBzgzN-d0IzlMsvNPPHimg7I4HAEHrkjJvFY6pydS2h578IPt-usq3IBKyQSjJS_fMdNW6ogdbm9u50aszEQOqyDnhsaDc5pEd_h7WaJafQJPMVy0JxMNhwQmcC0eYudvVG-lGDlqOvi6CC2JC7faxDZswhIp1xigf-YgCL5-K6E4uU0uV5j-ajCeL9hsW7XRbfjtDX3YRx_kfPnWmqC9SZL0wAMF1ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم؛ 5 سال پیش در‌چنین‌روزی؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/25607" target="_blank">📅 17:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25606">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wf1mvW84CWfsqBV28oqQFvi2hgFzLsfkdiUsAVFdwq9_VjqvcitwRo_jJqrmuWXCiXBUWjhL9muehp8WKPNwsBDH8M_4Ql_KQms-Bad2koyZMFPzxoPJ2j13DOOs_LAQVbD0L_qzkGROanFjjGaAyXtoqakClm2X4ttdJfWYOKQdL82yOKqNvfVo8sCN1f060zeNmoPYf1mqdQUmRBFUKOyI1lSWdU-0bwromhqcUg2gds9IAvgS30WUWuTR2FV3P-cUbwFTIfH9olCpgBT9DZzccsyvzkBOZo3tdrClZxas1jOB0tfjYqRTRR3_yWnIjb5V1MZwvnUJaylUWiJGGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پارتنر جود بلینگهام ستاره انگلیس هستند که قبل از هر بازی حسابی به جود انرژی میده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25606" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25605">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksKbse3AU8aTVWxK4ldvX93GnLhlYO4p1LX0rYRi6qYHvWCJ6Q5H_XCnOO0Dv3p2imeCE02ybHCm3828FUMQgW-FwEAAtdjSUfg8Zu0ZHCXqCHlbuj5RONUtPfLmAFRHWfu5tHjBGej2mFNpRXPX4mLcJVNIdaVJc2_2EUv0ausEDYu9IDoapEmXvFf_7yvKv594Q1Vh4hF-X7gBn58EYGVmEFH4qAR0sTFFkSLogbQ1kVkc8J5k2X8syLos9bRXHij4dd5pZbSnNbi352RsucvIDR8vJjQAVkMS2AX2r3QSEdI3BfNT46JF50tfA_mrcgJVJStkgQAu4Ny6fOjZ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاقه‌ویکتوریا همسر دیویدبکام به فوتبال کاملا درتصویرمشخصه‌چقدر زیاده:)از سِر الکس فرگوسن پرسیده‌بودن‌اگه یه اسحله بادوتا تیر داشته باشی به کی شلیک میکنی؟ گفته بود آرسن ونگر و ویکتوریا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25605" target="_blank">📅 16:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25604">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J06BBx196kYEFP08V27GbrywSdY-bglbI1ElvfgpU5MXbxhjgHFlktOFI2VyHAsac-QaOnoEDo3rVDGur641AE6f4z8TTHn8O9wMwbXoGLGlB-hSrtPCwvuywBTddoMGhIp75F60L2kxe4RJ161B7-w0voGhpOB5mKd37IYwaqRDPLm2nHqaXiIb6VMBxaRabjGlyU-FZJJxrcCZePfqWkShmIeshRYJkTJNxPylQoCS7gDJ_yX0LuzFFmKr8gJGmAns0gr6zOcZiueYMSjXH1zXaz-nRQWUPjBTpQ80vNcsdQ51BaOw0M_KCUGH6S6R8TAj4maqmkZjA_iqDpRuNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25604" target="_blank">📅 16:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25603">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHV1iEvp3M7dUoPV0WKKvyaQkmsRARDd6zqak0UypVUGRHdeW5XJeVHRv4yS4Zvo7LZ5I5JKgcO8wnFKBDyKM7GXmfc3BaiUfJMrqeqNBGZq3sPWVP3klJJIM_aDkGP4etZGPUeGpwhnd0_5OguhysJX07JCOc_tappJOwnenFrRPtLP2FTzjU3EG80dd7Tlqy_m6WJ-vlaQ0n4irE303ISS62KvFGXNs9lZQsPZVruX03CvjAnttaxmJeuZA4XUOVGNcwHJrQm0PxUwbLQDLn2tEvAPzbk62_A4dfqx7fiYchkE7lgmNHxf7Qf4UmIaX2HWTzUqxOzLwankeLIeEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25603" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25602">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxcW8kh1DQgFIZ6nLoy980cxWJULW2oN774NxKi1vXCHodsUSPqlXED_Y55rXl0O5giirIAR83HkeMJyDPTGGkKrQWNp7YtxhYAamJMiOxswIVcMMwRy1WdDCQljFtD2eLI7YOsHmQ2sDEGoONgsv_5XDO83PxDC362fPTOzva0txBnmvNy6k6eeAzVFlX78ah_ZaKyShkHjdKSSRmbEGNRRgvdYKGuXd_AGyVimeB5SpaFEyLvrPT3wLGwNUAh1vYB7IR2hz_Qr4vhlsuXO-IpJYklOhInlkBJdl6I0VR_rjcAY23pEcsSFJV3YP2ePrT98R__LhNjW0Lb6i_yOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچنین مهرداد محمدی جدا شد.</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25602" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25601">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">📱
دیگه وقتشه دانلود از اینستاگرام و یوتیوب رو بسپری به یه ربات خفن!
🤖
👑
هرچی بخوای فقط با ارسال لینک برات آماده‌ست
😎
👇
📥
دانلود پست، ریلز، استوری و ویدیوهای اینستاگرام
🎥
دانلود ویدیوهای یوتیوب با سریع‌ترین حالت ممکن
🚀
بدون دردسر، بدون سایت اضافی، بدون اتلاف وقت
✅
فقط لینک رو بفرست
✅
فایل رو تحویل بگیر
✅
به همین راحتی!
اگه دنبال یه ربات کاربردی و تمیز برای دانلود از اینستا و یوتیوبی، اینو از دست نده
👀
🔥
🤖
لینک ربات:
@instafilerrr_bot
📱</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25601" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25600">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cf6sDkK6YdixRqWUNHDwRa9Cm09u23uciB79j9yx_nlsZYqO0uLc5zcZH87sbwMNLNObfRhP30jrUxyGNvDcpTKru1WznJFAqRpPQNnn9osQ7X3MpBOf4Flcfz9AUR5-PG5FuS2rOrVMyUmqe29OPxgGyroHkHg4nokrZ9haQQhurY2asu-mtmIe8U_-4r2WUd154IRRZ_aLInTHt6-9qi7z4M9QXefSalR56Z09JpG5JAbxTDNaDLlQwekx9VCb-Z6tTVgTVa9unkGV1UKVVoM9WKSmBprUzwSPuiFe4CbRM-2_sCg0GyRJHP_UmNFDHUiWbpb0vU5LCx1XRviNfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق اخرین اخبار دریافتی رسانه پرشیانا؛ امیر هوشنگ‌سعادتی‌ایجنت پارسا جعفری دروازه‌بان‌ سابق ذوب‌آهن او روبه‌باشگاه تراکتور پیشنهاد داده و عصر امروز جلسه‌ای بین طرفیت برگزار خواهد شد که به احتمال زیاد به عقد قرارداد منجر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25600" target="_blank">📅 16:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25599">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a69b3302b.mp4?token=jTJ77_UpvoX2tT5gaDQ0qlG4h02MUs7xzHds8ZJ8EFbyIVgFikeOQ6VhO-6vYyYlD9U8IfzPvCbEnj2H3dbuUXsR4d-tfVe_FxXzWkaHnw_Aa1RY0mNvuiwGqivL7PEw-KYdwbNSyRi8eGl0-wqnaQEAraiWf17u1MNWDdiMQ6hRycgWOefe6Pcw5i2V2jF1mkdpf6HVRD2XqfY3gtGZVLZoNKsi9mbVKVF8Kr2a_Bk1rMhMVPASyhCODlVUWsMJOTdcg2jVdVA7LIKnXHY1lDRIrLB-R8BznpcI8JeT_TJ24CXQnur6MZZkt-FpG1qQTUBc8Shhwmixvuj299GFJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a69b3302b.mp4?token=jTJ77_UpvoX2tT5gaDQ0qlG4h02MUs7xzHds8ZJ8EFbyIVgFikeOQ6VhO-6vYyYlD9U8IfzPvCbEnj2H3dbuUXsR4d-tfVe_FxXzWkaHnw_Aa1RY0mNvuiwGqivL7PEw-KYdwbNSyRi8eGl0-wqnaQEAraiWf17u1MNWDdiMQ6hRycgWOefe6Pcw5i2V2jF1mkdpf6HVRD2XqfY3gtGZVLZoNKsi9mbVKVF8Kr2a_Bk1rMhMVPASyhCODlVUWsMJOTdcg2jVdVA7LIKnXHY1lDRIrLB-R8BznpcI8JeT_TJ24CXQnur6MZZkt-FpG1qQTUBc8Shhwmixvuj299GFJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
علی رضا بیرانوند: یه‌ روز طاها پسرم گفت بابا دوتا اکرم تو رو دیوانه‌کردند. یکی اکرم عفیف که همیشه بهت‌گل‌میزنه یکیم اکرم خانومت. منم گفتم اکرم خونه خیلی خطرناک تر از کرم قطری هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25599" target="_blank">📅 15:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25598">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3I-ARPdhxf5mzTxPngPHBajGS-FyhBOKTlWFKo7zcgxPEUj8SeWJ6hHwDVA5lbymNnnfhEoJLF5BuL6BSkumWyN-lnL6hJMMY-D6YnOy17iZg5HzK8qajkea2_A3N2r9wyvs_3Ha-FUlhmA94xVzpCMvqOU_Hi7SgSEZoykcGIoZ4-9eASQUhUKQ-K43B8MHxLm_lxRtUyNT-ucRbf8U4hc-c5CkCGBF5KKL6kYftIufuKuPEcywW1oyT2DMVpCbj72THzSGeiS_6Q2sKvlxVJ1hp9dTzwjLCSZ2hVJbDVF45j1MZWVtac-LpDcHgs2-IxyS2wBDZyoM8yYz3yzww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25598" target="_blank">📅 15:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25597">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prwqTtQFLs-HGpKfSCakZqwIzQV-erMIIlTaOWxNInTvuX5ClyfA0KV5ZeaGIXBYE8Mtqpa3SeY6SMDmTLEHin4t8iqd0yFWYP2JpY8fgRdZD4BTZhyxF2Ch_a1nZD_C8T22hBwN6UTixPeH2uhn6tFk5NQP7X6XHVo9w5TgLCWwOYf7p37P1Qwhd_rLcO8z568f2TDWU7CIGJhs76mLEsKm-OyPdjMJuM1IjHb5TBxVZwEXEpfJKiYvCdIl6xj3BywayjH5vc-xTcoOylEyppu_tG8vFPnHSxl_67iC-LaJ9AknX1ybfYRiqYoTNMxpXnEnhlEwWphA_0h1RgWn1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
👤
محمد جواد آقایی پور 26 ساله که دو فصل پیش سپاهان برای جذبش 100 میلیارد تومان هزینه کرد باعقدقراردادی به نساجی پیوست. آقایی پور در استقلال خوزستان فوق العاده بود اما بعد از پوستن به‌سپاهان با اون رقم فوق العاده سنگین افت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25597" target="_blank">📅 15:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25596">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7jiMo4xtHvJVgrAT-EMO38QxLRyvvtJiJtz0LKqJdOm2yM-PXXjQaKlAdxNJY7KZhm5PWZYWnAMX_sqRimoXR0aEiRHhPDt50mHgnZLPskvoOpT5NYvXB7fwHWbjDrnBvsvlfNCpI7-sC6YQiXGGRCpfHcnywTXWpwZIKBELoTSjU5_r_njs8xZSWEu6D5ADNYTFcAYx2D3opHmjiaFgx2PGSXhiLa2bimhwvGqt6BruXNW8kYXdm-uRELftxSCG8CgxY9mcuj5ugZkBtEYpUtqMp6Eq3BywL2Grl1eO_V3mdgQCivnszPYG2IaSopgzlgpwEPgaXVhAWuNiAxNrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
فرانسیسکو ترینکائو مهاجم26 ساله سابق بارسا باعقدقراردادی سه ساله رسما الاهلی پیوست. ارزش این قرارداد سه ساله 45 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25596" target="_blank">📅 15:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25595">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhfHBws4kE3TydAw-j2TPba6SNxwbRs7T3R9kn6jYpDoOE2l5wB829CcuFx_a0j5Lri5AuigRP-4GN_7w44UesgAqAmCs4BJLhvSM4aJGV6w95jQw1GNcGeatZV1Et2LSMPXoP00e-CUcO2xGPIyExKKHobL_UlZn-_TEHMq5euDLjm40xtCPuwykrLlG4HuGrvdiiohcYTSrvrYEgouV50eID482CqaUkcV01EHDmDNVoFqhtxVHwGfnU3Cy4gvpajVmLnH8uMujMusdB6vD6RfylbcgKAUs76D72cRTTE6Y2FPSNyiRZVMa4WB4SyqdLc4CzkQyEqb29P-UQcZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇮🇷
بااعلام باشگاه سپاهان؛ سید حسین حسینی دروازه‌بان 33 ساله این تیم قراردادش رو به مدت دو فصل دیگر با طلایی پوشان زاینده رود تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25595" target="_blank">📅 15:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25594">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeIWAVR-ecmhEA0aMMJi3rS46Yl9f6lb2kSf_0ttmbg2k6PG-4YmmknaV6Khgbdnff-kkb3tfZO-su-TY1knV-PTVq4i6GWH7uAXRloXz5iD6L82g4yUE7Co4hlPy49RmGVPuiQIX6eWyZiVYAcmF8oKiPCBG3G89LhvZbRV6FZfiYNCIeUlj-t4dVTGdqNNVmwcYKJIECnzHQNcmx-6S2SLt214PzbiG68x_jjkz8jaIuEuPJMuD8P2VwHxAbu-6L88lzq-ipa9STpeu3wfsUtb1XfID4zcVQZ_y8Nd-TBZsucvDg14qoaRJu9166rLvgeFzQOtKvcoZTQfaNBO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بیژن مرتضوی خواننده‌وآهنگسازایرانی با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت. عمو بیژن بابت این یازده دقیقه مبلغ ۱۷۰ هزار دلار نقد میگیره از فیفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25594" target="_blank">📅 14:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25593">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb9J2LkSBdezSB6pIEjyPjJ3CaqN71FdFdVzBR31YGf6Am6rt2Dc-NGO5XTI687TQ6ZVP1lVyq_pIdtvXOxUsvoK0Q9-cuhZH0TKbDMtBepknk637UWTYbtf_ClxjiSrRWw2vL_UiPqSWPnLz6LAZbSgDVv2ZCc8HN1GBcflJ3Yv6wEKi5twF49JhBpPJCNOoQXl2T6aaRixcymf5_qb2CoLQdMnNZJP29exns9I9E5_IF6yPwcNvjOX2uPIguzgc5uwamlQzCeBIPHg6O5wxdSdcjrMIOVmoDo4MfwMcvzPQMOgFfG9QYqOsNctGbnEaMcuBTYOoXVcW7YgTqKeLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حسین حسینی با تخفیف 10 میلیاردی که‌به‌مدیریت سپاهانی‌ها داد در این تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25593" target="_blank">📅 14:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25592">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awOQ0V8ktrMw9W42LZDtaKY_53XKItoMmexJEJ6tMFv6p5o2yQ_OG9KzOaajoIztUa6QU5iFu-bbz13E1OKTamax4qBGUGG9My6Q1dsCj2A2CgAcUzwlkrRgtY2Haj7xspzNEF6qrWoaJqZufQ4VQ9IUxROkBR7yIVatjHVPZhZIennNBXZb_xBTV4bvefINRDUfFYZdzsJoo5dw1_xOgb9oK4NLSXWzIwVAJzjFV58jjFIjWD2XlM2zsLAGnQDN-ZOpEOSGT-C7_BsRlPYgafk_4DXczuvbWnp4YdGhGAxZHyJ_yffmmCna4t6U8WLs34nWNSIvJGGGOuSLn5b5Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25592" target="_blank">📅 14:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25591">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WY2GdAOb5_kYH9YEduHu-cekRbAzjB2txMn1L7JA0fCOvmsOqUyrGjSNM7SDWY1kvUSlOunfqQmmOYE3GMxeXhI70V3oCIxHmeoDQsSK9B1QWky885UQtRsLugHOzZY30jnZLQpnMqvLHmeLyBppXEwUubneRmE3BkqqDPswx2tXOCpTZ-0XwrBPZ5afETPH37pgfqRXus41TJFhlcic2jiLWfdaQCskuyoqib2xCccQwM-X-pIRxl7_Zg-bQSpr1F017y54LbDzHwTXGnkUQ8veVBJ5XpDEaG9LxKQapLI417_7nn9Y1ACQU2GR3f04oJrCijQTI7U_Y8VV6sQf9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی سابق دوتیم النصر و الهلال با عقد قراردادی تا پایان جام جهانی 2030 بعنوان سرمربی جدید تیم ملی پرتغال انتخاب شد. دستمزد سالانه او 1.8 میلیون یورو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25591" target="_blank">📅 14:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25590">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAjB45ArSCTuh4IgQ8EFsFAWHumF-PQOQuwDAGdjxINCwHflY-145MG04ch5_IxA9koIBkdbkedrXvpk8IgiBxacDD8bhu3tUCreOl0V5MJSYwZSniFIWNMqp6NUxamWC5awzkG4hoasB2ZpFdeLDRRzBB4dFJ9vgxx9kDEQZzH55LvrusIuRyTR1U9MZAD5rcJVJYSK3Svc8Db0FzsLUm9L59KkC1fwHR-6JAVcIuQ2vLsc-jhahJ5-XJR86rLVnHOqYlYWVMDW_XYbJqJPGSyi9kGifC7bJKbLsX2Ac5PYAwOGLium-CmdeDPMiJUlK1qWYUa9UUupI6dtXUa6Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا #فوری؛ یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25590" target="_blank">📅 13:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25589">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyJ7nBKo41Pf7LEX7wTVCU_rqMmNOQvfSOzYRtNyw3My7PiA1BDBJDITVwiKU67mJNJWta7k619O-4TnBNs6gCjEAfW7X2qp8s6P5TXENQprn_HcMBQdRqV4rw_qGSNVhDAbLjCs2iPTsyPQs94NgWet5LRLnqO1XmehYjPpKVOz_lTxvbpPO3Ki9yBYd-ybi3TOnsBZj4zm7t3ge10W_c0ucb406A7RsJcAxyZQqX9zog2X2j1B1ksDuPl1fd5EIV7mgosvVuABrKYF6RgCMTbGcPOSMHlqGD4l_QQfOw8I4J97VwrcWoJnSrCVW0zbT9z5Tvy7bo3N7vQdqEmHNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛
یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25589" target="_blank">📅 13:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25587">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jDfShmUl2LqknTf5ANnholqPo-4eOfjlR550f5ksFHT2xCl8Sn3KTo-YA6JIqCKyHn3nI9HMekCJf3IB_WGftXODQUEqozXoEES7A3OWcCmtaAvGvBp8-YPf0XdEBPBqSfQSEO0d9HyStH2eGP4-Q2ESir2wsFVZhCcoJZxkMOuORT7klVXZLbHjFiejqQC5o6Ba8GXmJkE28vuzmXOa2T0Mwec7f4W1X3BrulpDa99qVhcmFvGwJaxSZo5SJLu8wXiUESEVTTw2JZn56lylkwzQG0A2gx-jKWGDxCm7YZEFj8nVqfMkkNyrd6pOx35QsugJAxtciQ-92wKtMH1TRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZacvs5xI77ZCQVA4OFnbPzbDUtw-MVqJpWEq_p5g5XugiAQSQnjGtyOXEPLTkQV-pOvCFKkU796Nsrcz-u7bKCOZjZFXlNfzYE_xSDeyrbMp55_mNfwj6yNHlK_riMspwwvsF1ouAT7Qf2MHRBnB9hMgWuumQlezCJWltdzupxkzeOy9gkjvL1_6fWILxa91p8OZLu59tswEFjMWeH_Vie6hZS91xV0sYMha5A_nvCgz4hVOW8uS_E7DjVfI4nk0OkjXhv5Os1F50RS6tMPA1bkgrQLM3trCfgz7q09KA0ZhhMZo_OLkl9AYeZ_DMOEaKPDHK3M_cdkYbuuEOvUDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امیر سام دلیری مدافع میانی 23 ساله نساجی روز گذشته ازدواج کرد. جالبه‌بدونید که همسر ایشون مدافع میانی تیم بانوان پرسپولیسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25587" target="_blank">📅 13:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25586">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-_a6lzp_Zjg0idBeOHM5NRPuUQDtTQfpYkX03hJQOXqSru1FJRwjlC_RI38xq8h_0l0MeSvUSjAPJGCEWAnhwBxwTzv4tVrroYjVSY0PA6Z1WyH7NjQ7bnbqsjuc9a_RkKgKgp_0oi7kAJMmljFl1DoNnEAwvKxZZwcv6YdCDs46zFaKlbpQatNZjUnJdzgbgb1sekA-SwehrPft4kc4ngmMDGrG1PjzgK-ywIAgdjiMb7qoirqNNwGQ6F5NoI1PG0ZUSZfkyR0O-6DL0uCxDy7XxV2hCroX_Ew0baDcyowYcoKsb34NnQW__bUgRncDvkvA0QEOaoy4DUR-tepug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25586" target="_blank">📅 13:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25585">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acb9b44092.mp4?token=hgI9Y4fa87NZqKrMAIVucuyQGtJ4RJeeY31XCkn-idv9xdvzseahttlTQNyUul7fK72Yy9aE9cL3EpW_Y6zYd0QtBfPF3_8u4PiO4A04mUnxVgnCPtQiL42sxcqSz0HKnXK_hd_QIr_iCD_Zx2uaKlQJzrWso2GXNmSFkxY9Qll3YSf7IiQMANtvBD1ZwjWE8boZwm0lXgvlxQc7goMuiD9vXK-ahxg5qbdhG7skfufXIhRykD2U6vBpFSFxRimYPOW2vm_5ikLbuxFJTEj0NZNAwkKyvLFJECvLInKpMNMj6v3qy7wr7TFqUGw0PzmiseK9lLEb3uPkNJjsnFFuhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acb9b44092.mp4?token=hgI9Y4fa87NZqKrMAIVucuyQGtJ4RJeeY31XCkn-idv9xdvzseahttlTQNyUul7fK72Yy9aE9cL3EpW_Y6zYd0QtBfPF3_8u4PiO4A04mUnxVgnCPtQiL42sxcqSz0HKnXK_hd_QIr_iCD_Zx2uaKlQJzrWso2GXNmSFkxY9Qll3YSf7IiQMANtvBD1ZwjWE8boZwm0lXgvlxQc7goMuiD9vXK-ahxg5qbdhG7skfufXIhRykD2U6vBpFSFxRimYPOW2vm_5ikLbuxFJTEj0NZNAwkKyvLFJECvLInKpMNMj6v3qy7wr7TFqUGw0PzmiseK9lLEb3uPkNJjsnFFuhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25585" target="_blank">📅 13:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25584">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxD2tmx0VZA9G7Xam5TtOydMp6SbCSjbMbOExVtfVNKY6gfXy-dUrqiWJWjefR5dDGVgoley4mpGC2spjdTrfrSCrOKkDGUE7SBhyUe2Fn-jP6I6Am2k0dCpHZcH-vRB57f8GeXe0M2BJX3jxJfAM2-aH3L-clA1nQwSvCpV4PT-xi4KSiZR7dZyuPI-BKBo0ZiwCDSpSR2GNVPtBtXoiPEy7Vygjw1UHMzl54o_FOhZa8doqsXjOPuRxNj5EX3PNT4vVBSJp8DID7NWLqfb538LMccN1f7-QQaDS2fAWWc4PlfD8N16JaIxjEY4IE0eHuXyPcPWNlvnUN5vSgJjdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیرانوند: چرابعضی‌رسانه‌هااومدن‌گفتن مصاحبه‌ های مورینیو درباره من فیکه؟ اصلا فیک باشه وقتی می‌بینی همون‌مصاحبه فیک داره به من روحیه میده چرا توهم نمیای همون مصاحبه فیک رو پخش کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25584" target="_blank">📅 12:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25583">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuGyfCm0w7QdcsKd6MYG6MoTIeSZG1KR9p9SlzaUiAd35fMRntWtjxzOiVAVVqzb43TeC_0Js-Q4QdW741wR2bYmRs3nEF9VXTclZCGpva19OMRcs0C9ww8_rw7-ug_iLnY7E8mywSoyiRvBTgcNopLMMytKefAWo84CfATo05L2kDTNYun_BF7Fy70S66RGHmfw7BEchE8TpDsLBKZf1jwZyHhPUyFGqp-RTc057kc4rsyydS7fDv7QkY8A5IOe01G6Fcb-On3btIf4mxKRN9dYmaUnRSuZ9uh4Oi9XiQHa7KusBT1iygujJYjKWe2qivP355w71gMzdzVXLu4WPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25583" target="_blank">📅 12:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25582">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fw5pmc2Y8byxKe0gpjcZm-df-C-35zpA_PMjg2EHsRIA_xayhZh_uWPsjokF9KdFpAL2dGTkgXEQ8n2fxOB0dLXjFJ9IBSp6CIydQR1iXHY3uMvrY6zEGfekedB6cINxGeQhwW1Xyy1S7SFLPiqzxO9_w3XZwNjD-EOgCjj_uc5X82SAokGX8rgBHc54xt79q78EWxIWR764fgnA-2J74mA9AxLpX7ILIghVuIUFdFcZqjnbOM_tIZf0AdRCFxWX4f0R1DZRfggaD4MyblmyALgGBL7Pe44SasqaZzivXjUdAx9woksb5hKAspMhJW1i9C3cWoMAneeR52ckWQZi6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25582" target="_blank">📅 12:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25581">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QM2FVN3atnIVv9j-fgDxdSnR1WKTvOIp_kb4yUyhu3CTs6lfrKxhB3fVRei0xtvfeAAN_D3LvbaBdvM5V1YB7NAZb0_JJ5UEHKCp9GsO9b6il7OJ_fIKZK7wrL3IWDx-bdz0JP108VxeAgTsb6y-sy3m7cnA7guzRMqo0BkG8ibc9ReD7uhmNWVirq3uThfn1R9zKSCJJBXI8eg-PtJx5pXH2Uagc2dZP5-p_YI824lchCQPqZhfrpgOb9vrOypwEjQeBdnT9bvWuqeVuCoo9Qz0DtiNDbZRk0KZiWGiv9cuPgIuP6JRRIBkMdwhEj7LZYpXtwBzu1yP3TkCz6Bmig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25581" target="_blank">📅 12:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25580">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZP3BGM4w0P8puJKJjAXeDG-OZ4RlQjVrboIZaQBjEAVoaCXq_yfl2TH78kVSnPwQUOVh8cPYl_USAZ6EJRaYYIr4HHhcUufWWpoAUOfWypgpmIGxgyp32PEw-vsfehV8T1ZDhDKB8-DYsXVeH-k5k9VSct5XYtAM6O0oOcORmPFZQNFi1wRZgyk61DlQgX6r42QKaBOLLzru9j-u_5yD29kmnKS7_Io7KTb26Rd9KCtHtGJQ_ElvE1KiqH84Qy9Ab95_-XXn1xKtFlrtMIq5Slprc-1NUkubxL5n1dbeb3lc7wWrp3khMic-ppaltSdMpcevUsZO25ro9rcIv06hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25580" target="_blank">📅 12:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25579">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gn1l71CdWZY9_H-RB1_1Y95ltpFC-3LNy7j5wbsLmk0NwVF4QBTj_JKSnxb5jU8vc3zUqdQWwo9r2QMZqOgTezpaeV5Riazt8DeUXOoKQCeneySQgap3eJFgOOJrdw-sjidz03TfSGO87YLHUGucgVxBp705I07Jhv6a5GWvhrmLm_dxcJWAvoX_Q5dgktxWfEXjvtbL-mU9lrLR4eyqw5rmKu_rSptYWT6mnHFOtMiM4SJMiNf7SO8jIJb6sd7rJJxC11KBjK0yJIuEJqXM_G4b-jGkP21dHoEmzRXS72E07cCB3iCsIdYKbcLBMEcRNsGiT_fAdvScOuy6USEKtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهاب‌زندی‌‌مدیرعامل‌‌تیم‌نساجی: برای خرید یک بازیکن‌دیگر از روسیه باباشگاهش‌به‌توافق رسیدیم که روی 1.8 میلیون‌دلار این‌بازیکن تهاجمی روبخریم اما خودِ بازیکن حاضر به امضای قرارداد نشد. پدر کسری طاهری به نماینده از خودِ او امضازد و به تیم‌ما اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25579" target="_blank">📅 12:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25578">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caIzCOJIpoUkTNd-nwAbmyJD-oWOTfTMhK9frm1Rv9AXjowdO3DVoU1zIWbMvi6sDkRlrujUKtwDtpfsWCUVaUse3yT9Ud2_1Rzq2bfN8qvrcqpUp101AKhb7Y4ecyv3k6YGSaXG8ziT3kFgoV9ds9bHkIDliqb7PKFVhVMzMgC2Ak9AqrxZp610gYQ9MAL_cO0YpOEjGxx0-mw0H2ph0STMNwNU7QhtUZ4o4Z5hNMlBZrGNWLnEGUoTShbm1NNgWPrgwKJQeE6PP4dqEQFRFb7AnFwiXVCMnWg3wtEHUJwL3X31BPGzYL3yQBCdETAd_pjw01DmaNbAFzbm6nmVxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25578" target="_blank">📅 11:46 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
