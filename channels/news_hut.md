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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 05:10:33</div>
<hr>

<div class="tg-post" id="msg-66041">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/news_hut/66041" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66040">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/news_hut/66040" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66039">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/news_hut/66039" target="_blank">📅 01:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66038">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/66038" target="_blank">📅 00:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66037">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
⭕️
شعارهایی که در تجمعات امشب حامیان حکومت سر داده شد:
۱_ تا باقر کفن نشود، این وطن وطن نشود.
۲_ مرگ بر سه لاشی، قالی مسعود عراقچی.
۳_ این توافق خونیه، باقر خودش کونیه.
۴_ خایه بخور با سینی، عباس بچه قینی.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/66037" target="_blank">📅 00:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66036">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puV5Q5XAwmHhm7YZ4JmyFDivrvNUsqm8mAM9aME_hMTvIW9YxsM3SMOJ9EkHxEfpPEC5pR1SqVdOBrrf4wOOUNI34zy6wRLQEIoccl4FH5SCU5lR7Mf6tWuylUOxfa2PMQ1b-4VZCa5Kp6vT16TRCjCL2QWUduHj45ZX6arGbji-AezDsKupMYHISIiwQQ24UyUBr0Ef7nnvNQvx3ED3BBpWZx7Jwdf2khmDL01d2xRjXiaiCBsd2wpUwQdQ1exWugbTWJbVITmhuUUe2R6kyZLFQR6f8ZLsxGDM5Oc9EJliQS_A3FBsXBgBIBA14MgYIKMA7gVHQTBi1fgmFyTMMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ و پیت هگست در موکب هیئت محبان امام صادق (ع) کاخ سفید:
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/66036" target="_blank">📅 00:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66035">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLnJ1nQlzTioGx_CycgSHcOH4ts33WabHrGW3GXrDjLc9YazmqtgOk37oEkyq6E0pmm9Msj4TKks6GJmDD7qTdsMTF39T2E0SZO8l21XlEPevBUla1LzSORri9AtDXrh2cf12K-BvyViKc92yzeREO8DDXLjXgEo8H2Z-EEY7-bS_38TrZOwtkAETEzrWwfm3MOQ10rbkOiFit8XjON1P7vDFa6cPixt5WnmePc2iUebwOcc2YBRnywa_WxCpf-gp5nankP0j4YH1J3hqUbE-_i1Sa_gJi_LPN5dj8EPiOd5v1x1hjxj4LUD5ue98aULKaOGwjazCcOEh9I5IWG1Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
توهین و کنایه بسیجی‌ها به آقا مژتبی
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66035" target="_blank">📅 23:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66034">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
نبویان :
امریکا اومده به اینا گفته 300 میلیارد دلار بودجه بازسازی مملکت رو از عربستان و امارات میگیریم تامین میکنیم که خب مشخصه نمیده
اگه آمریکا بعداً بگه ما از عربستان خواستیم پول بده ولی نداد، شما می‌خواید چیکار کنید؟
«وقتی توی متن نوشته شده هزینه‌ها باید با توافق دو طرف انجام بشه، یعنی آمریکا هم باید درباره محل خرج شدن پول نظر بده. حالا اگه آمریکا بگه این پول نباید فلان جا خرج بشه چون ممکنه به دست سپاه برسه، اون وقت می‌خواید چیکار کنید؟
من بهتون قول میدم نه پولی واقعاً وارد کشور میشه و نه اختیار کامل دارید که خودتون تصمیم بگیرید این پول‌ها کجا خرج بشن
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66034" target="_blank">📅 23:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66033">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiDCS4XEsVaLco8Dq7BOJttgMGGSBQPPmfLLJNSzxp7dnDC7vjJRCxHB6JTFy_ETg0FPxd_sZWOIj1Mpl_m12zbBkS1qLSczUJ78OtDRdlKp-tzN5ri9j5PttwY24ei1TSbSzy5T_VzmfEthjkVSu4a5dQp-oF4rXOedxzfwIIEL6zj7DCeYTfFXglL4ylIL_dzHe0v1ajadODjYzr6LPZBXZPY6YSECllzt_Xxq_Pol8RV4LLaBn5eH04CEdUmS7I80jq1GWDv0z1bcyLVLG02cis4OizPweHrs-jRQMzngNRv6spSplCBybCTRSHxT1cZYHCWIwdMh_8kFb3LCDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز دفنت نکردن فردا هم قراره با قاتلانت توافق نامه رو امضا کنن
😂
...
«چقد تو مظلومی»
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66033" target="_blank">📅 23:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66032">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:  طبق اطلاعاتی که به دستم رسیده توافق احتمالی بدتر از برجام است. نه احتمال جنگ را از بین میبرد و نه گشایش اقتصادی دارد.  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66032" target="_blank">📅 23:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66031">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66031" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66030">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66030" target="_blank">📅 22:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66029">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/722ec8c49a.mp4?token=WKbVQOV8NPRNFhU_gh4ehHFFqLyuhi2jFSjDjI-AdoUFbTqv_ynY0BGCxSzaVWMhu3qUqTBcZhIWeUb4GGTiuI2yyR0Ybh6Mlr8QcnJQOZArfrTndC6FDemMtaaZk_S3VhmdXsPHAI9BH8OtKkl7YdN9uA750PEIV2WNF1tQTabZjyGGfcvtR_kPmskT4o-3ar7qu0BQj7zrMOa6LtYbVa1D8aMk52M1fGjIihM3uP-pbfEguzu4udy_1-BeLgYxkynyKWK0Zq7pzMpuYS5y0CQe5QYIEuge4UQD2_1C1NbRt3qP7yQvGn1z_fEZgA6NOox_dbjoZZZXPIfHuh1lXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/722ec8c49a.mp4?token=WKbVQOV8NPRNFhU_gh4ehHFFqLyuhi2jFSjDjI-AdoUFbTqv_ynY0BGCxSzaVWMhu3qUqTBcZhIWeUb4GGTiuI2yyR0Ybh6Mlr8QcnJQOZArfrTndC6FDemMtaaZk_S3VhmdXsPHAI9BH8OtKkl7YdN9uA750PEIV2WNF1tQTabZjyGGfcvtR_kPmskT4o-3ar7qu0BQj7zrMOa6LtYbVa1D8aMk52M1fGjIihM3uP-pbfEguzu4udy_1-BeLgYxkynyKWK0Zq7pzMpuYS5y0CQe5QYIEuge4UQD2_1C1NbRt3qP7yQvGn1z_fEZgA6NOox_dbjoZZZXPIfHuh1lXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازگشایی تنگه‌ی هرمز که قبل جنگ باز بود الان شده‌ی آرزوی ترامپ، آدم می‌مونه چی بگه، دهن تحلیلگری که بگه آخوند تسلیم شد رو باید گِل گرفت، می‌دونیم که این تفاهمه و توافق نیست و توافق اصلی در طی دو ماه آینده مورد بحث قرار می گیره ولی همین تفاهم هم فقط و فقط به بقای جمهوری اسلامی کمک می‌کنه نه تضعیفش دقیقا به مانند برجام.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66029" target="_blank">📅 22:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66028">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH_x0hfmwawJo9CP5swOBFlCYTfNBfzGeEQrWboiJNUOyReItDYXlxLO9PpYmkvlezxBLluTXRplqGZepXFVieFyUYsPHRYx_72omlJm02m1OxVyb5z_KhpJXTgh7_IRlIQA3zgX8iSO5H7z6i5lx_g77pyqp_0EuiJvyU6y1I_Wphse3RKFvY4huJ5dgajq7bHCyCgOBwgJ7Eul-3RaxWtYmEbf0BrE_SrR2MHRb5oX-Tpbkq1_aHxpTl_OE6drka7l4BejjKksekBFfPeyqMv3VRxQct4Y4pSaluXc71mowJy6sDWFlLMLpniyOU_1rpwr7bTpK0jgffMnbEmomg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فراخوان اعتراضی نمایندگان مجلس علیه مذاکرات و توافق
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66028" target="_blank">📅 22:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66027">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
رادان: هر فردی که در تجمعات شبانه برعلیه تصمیمات حکومت حرفی بزند یا شعاری دهد به عنوان تفرقه افکن با او برخورد خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66027" target="_blank">📅 21:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66026">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66026" target="_blank">📅 21:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66025">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
⭕️
🚬
🚬
فرهنگستان زبان فارسی: از این به بعد بجای کلمه هدفون باید بگید گوشینه
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66025" target="_blank">📅 21:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66024">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpfdvoePFgl8y2Vt0GwRq-bICO6DUS1boJiwdY2bnnf2P087G_Khp5Wkgct9VpvLhnzPEjKXQTRsk9pTymlJk-VFhx-pxdME7flM2cwg40_omwSXytAobvCavJTYaMJqZI3_c157GXuYdoFpz_5PFEIdCn0_OnRFli6EYMGMKWgK0hPnhg5vmkfN5ubJ97yvzbZ6XP_pXh7VE_LJL8IFing0R-78K7F1AhJzQ5hfCU9pZifGFKqDoMia68a0cCpKHqEsMQZYbp2HS6oM_Mo47c01aR53dZB-41NcNWb61PtW5OrWaIY1avH50c8pwhcxISoFMuVRasvT3aakWYXwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
⚠️
سردبیر مشرق: رهبری در کدام پیام ده شرط را اعلام کردند؟
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66024" target="_blank">📅 21:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66023">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66023" target="_blank">📅 21:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66021">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66021" target="_blank">📅 21:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66020">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">هات نیوز | HotNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/news_hut/66020" target="_blank">📅 20:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66019">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری؛ ترامپ: فردا توافق با ایران امضا می‌شود  توافق باراک حسین اوباما با ایران، برجام، مسیری آسان، زیبا و هموار به سوی سلاح هسته‌ای بود، که ایران شش سال پیش به آن دست می‌یافت و مدت‌ها پیش از این از آن استفاده می‌کرد. توافق من با ایران دقیقاً برعکس…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66019" target="_blank">📅 20:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66018">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66018" target="_blank">📅 20:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66017">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66017" target="_blank">📅 20:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66014">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66014" target="_blank">📅 19:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66013">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7hlLxEYvz8x5GrrLbZsjBkUFCzYFUuYkMewqDrCUqHKIc-n6EZTUmPUad6blKLYLIJlch-hnb4aiXxQxZldCoD-8bBcVW71Nv4HL7RZk4WzyHfFpZIkkS8NHOPC9lHB5r2Y6sF6gsMd1NCHuFDfZtjqidHdCnb_NRQNuQXYok3p4jZu6s3DPEawp9HigfRnhK4S1qzrzRsXZFW0boQSJNRaB2P3RFsWdLr-aBq4IIpmG43jYyZuY72-fJLkvbUW9r4pbhHeF96UsrcSQK8bkX0NvJIjoww_FDpz9IbEGiZs_bwGho01OXvQrsVaLW17p1zn4BGSdTEWfW2Pljqn8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید به نقل از یک مقام آمریکایی:
پرزیدنت ترامپ روز سه‌شنبه در حاشیه اجلاس گروه هفت، دیدارهای دوجانبه جداگانه‌ای با رهبران قطر، امارات و مصر خواهد داشت. نتانیاهو در این نشست شرکت نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66013" target="_blank">📅 19:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66012">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xie_fjDoYUANgszsHJIXp-U9oyAeUuZnd0pn7eCJrw3r_BrqetjLJTjQTsC1JtoGmLTkNvq72huEpHc964qpWtJw-VmS76IpFISugjoDykeDCwS0Y0eJxPBy_ayEfIcHSc0yeMEiMxlnDwGbFkYjhz0SVIfJQbsAa36TjUZGk1aIic49sUqcUm0miDexXUovY8cP_VXRDhvY9_anz7xP7ZjZREoSHyP3iGzCs0xsOXOKM3DPNvKoo4211QM6jngxXpJe1PylU9Tzn-bUdmpGULv1Yx-VqiGfeYayAF6oF5R2_xbO8qJRCGn0HDTBgA-RiJx3ZM9DFNxH3O50otzc7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تجمع اعتراضی مردم تبریز به دلیل توافق با قاتل خامنه ای
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66012" target="_blank">📅 18:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66011">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
#فوری
؛پاکستان:
توافق آمریکا و ایران فردا بصورت الکترونیکی امضا خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66011" target="_blank">📅 18:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66010">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_RBDjLTBAjdhYpzW10wBx5JVhf4M2nqU5NKZfT3eNUGU0lFi9ly4Db9ObEeCMgFkYx9laM7bNU5DZG0k5Wl-9pkDcop_kL4JjG9thLsQW3oUC3vudElsGVvMIi0y7a2BAyUo8vV9wQ30IAHYgYsba06lJKNfQ32JyjNuoc07wHeS5QRRYabU5tYBaJPZii-Nac_aStTTcMPlvfhqLcLiaaQAmWOnRN3oFbGpIeSZXXUtxuJTL-nvgQU7Fu69VZ8LLC_OwAL-y5rasQpE2VlpdzElMUFzbMdIiS1hNlinLZPwUQ2dkSAgFaf7WFGc4erf1jc2hfATC_sgkKTzwgsJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ توییت شهباز شریف نخست وزیر پاکستان درباره احتمال توافق تا ۲۴ ساعت آینده را در صفحه خود بازنشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66010" target="_blank">📅 17:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66006">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fq38QXVV1aN8wYbVUI-xpzB_EAf4Y4x4nv8ju01tTWXnN3CcNRfEuXVd1oRAKz4ytdttX8iXOyXbKXUuKpZT4AnMY0i-U5NyopylBjS54PzrThiC1zp2othpmX5P_MAWhp8j5kxkuRpvzujqYshEJKsZATPXc4CXuEFxUogQ2IMLyassqCLWt56b4wNZq4RQ_9FF9Z3XYavIM4hjmybZv9ueKt2hgDVn1wnal-vKn6URTeAW0ESSivdNuofgG40RX9qbb6qxsUu1ETndMdOWMKKmbpe9iM3PtVG0PaX6Iv1k0nAhEVDWG5rMOdkmabGK-D_FndqQmFXr2E-tTTePwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0b4wAChLNbqMsqchXZwxY54nLcgeBoGXw9c3gXu9gDYisX0pu_H-MjhjMVWhCVbe2DuzcQGzYKQEwXqWbX3WYDe5IdZlapHTqlZeXEdGzSIu9yhNTqbUGkJW67nTXgLNCL5nbVms8pSt3RsipExEu6mK2UHheV9tl1Ogie1RVmWDhEU8N2Kh0N03CeoqwRJ7wUN0xqg7t1K3RhRStVBm7kut0IqxMeRo2B8BAdFq2GrN0Y6w3FXYA6BkAQTm_0XmkLs5gPrYm8FASSGtyAtaCWV0uajApROkSF08Lqr7KiGFkE7PhifLpTff8QracW8YedIF-10Vqanwc4rvsnlqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlGCCsxJyHF0lxNnB6QbXpd4SpMP6D6RYqf_bPqbhSGtdBuI81LiBpoRTu46tXudNQAy2DDmLZx4gHMpUEP3vjn8gAIPgaa34o84bsBeup7LEZNsWgxx_U44fLnjGaX7NwgV4ezNNwFP1AGh2c9tQ1Y5C0CQdNzgg0OPr8_7TIOn6lf2cEAmbtm-xUeuSjbKSvB3CimgTlEVwb8Rae1mw79g3BlMR3-q_cR-SSwndon2fIdvlHcF0-iR2wJa2nTFBxQWyKqMuf8gn86oCp35r8mRVefRD47f4N1SobaSi46Eb5pW2_DyY-F_UvR-HP1R5OXwBYi3aFGhhbKnGmPPbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6ZnSrZDfurIy-blOf7vAuJ-5jgO4Gd3_qDfQ1IZ_gjY7q3VLMx60E1_ZEFLOysLbiX_UX3Or0XcAHoNjCi5RPit_gQUdCmjRjihTOv400yDMwDQzbxrAXCYXdenUOKoXrWKcdGlvfLuyzyqU9IS0T80lzgKO5cWBpFxue-XCnjoUVPt8eSADwPaL_VnBiPnKjulE4C8LFWmUJLcrbXuUdf7k4iwJxUDPwqE3i7-hVkZ2E0y8lWjdfWX0qX7qaqyq_i-0FIKgxOIxAvN2PKNXBhA8K7oPNaWSe91XGUCl8uJc001LoBSu-HXCN2uKlbX1ZnYI3IWI4pWZkfemHXLxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جت‌های جنگنده نیروی دریایی ایالات متحده و هواپیماهای فرماندهی و کنترل آماده می‌شوند تا همزمان با عبور ناو هواپیمابر آبراهام لینکلن (CVN 72) از دریای عرب، از روی آن بلند شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66006" target="_blank">📅 17:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66005">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">از جام جهانی تا لیگ ملت های والیبال ! هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در بت ویژن در نمیره ! فقط کافیه یه شب از گلچین فرم های بت ویژن تا استفاده کنی تا ببینی چرا سایتا دنبال ترور ادمین این چنلن بیا اینجا تا ببینی فرق ما با بقیه چیه
💸
💸
💸
💸
…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66005" target="_blank">📅 17:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66004">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66004" target="_blank">📅 17:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66003">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgNssTpGmiu6n_BNM62lLGwCuYQlXHithwktfSPl5GpMAkQx2eDeIwTO5o35meac9HUvw_NILz96SMXeefikaTD7k3QBbDKxnUqau2qI6id22gQZQx0oyOz3L7V_w8K3eTUOBg56FgSnKb-NFKim_-hbN7Tqe8hsTLlT6H2EBfLrhzX-vStCNh5oRVOyMZImOiL-GSkbXA51KQS6dy3P_oXopozZsV2r9DA7Q8OtvHjrLqQM2tG5nslWeh63fM1PJAuGFCI8I3YzJV0zdeWgdmZ0Zj-mqWqkaqcvqM-AnZwPgbxXfZHvHrgF_l6_2qHhMEMNOlU5H8xFosmN9xcNuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعدادی از نمایندگان مجلس به همراه قشر تندرو امشب جلوی وزارت خارجه تجمع اعتراضی برگزار میکنن و به روند مذاکرات اعتراض میکنن‌
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66003" target="_blank">📅 17:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66002">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwXu_5bilCIZcyswab3_kV6Ed4ngn6dkz0yToydObH4WBT5amVNCq_oYn0qtVqWoXkb51exEqmkPRwu8Oj1ZRLQOJOLYcrb22z1QAdPZCVGBwneYZZCkp14H0hWS59Unuk4v7XGqdvrjyew1LAmu3mUM2TNIwBBJvKG8rlHYjUpQa-W6kij3inR_bzV-B21PDKiXq0c40scwposx1m_VYGo79W-ZMA3LTaechJDNfmznPnMMkGhElzQpbbKiIhzqRY1d0_KDhp_3vsb8pGEYAD_t5VxGZT9FyQXfqeJkdvXjPjDI_8XKUPhrz4Y1MKJ1jOqHKRbzTlfloHZMFPk21w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اواخر بهمن ماه پارسال، ترامپ مصاحبه شمخانی که گفته بود «اگه آمریکایی ها سر حرفاشون باشن میتونیم رابطه خوبی داشته باشیم» رو بازنشر کرد ولی هفته بعد کشتش ، حالا دیشب هم صحبت های عراقچی که گفته به «توافق نزدیکیم» رو بازنشر کرده
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66002" target="_blank">📅 16:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66001">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66001" target="_blank">📅 15:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66000">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSUJzjjDvwcO2TXPgBuDba25NmklK0gStI-hgnChz-hfoIgzNp_Zu1VyE3PZKVM5oIT8aPZmBR2YDAPZI1dQrYwXiabjLJ-SsbywpzWKzjJ5zElIZMNY3T3BweAQOJp6Qfmdx0zZ57U2HhoYgN3kF2QsPBxRcxyJaxgCdlQ933ZE1mX9LAXkvZRc_OdtZfh5EQMaWz1blpTcs761bh005f06IJcI-hW6M0-P3jLvSTfGiTvzt87uUq7usxo3kHxI1EdxBsx1gvLr51pNH7fV_Vc8yZleNWyhW0ZVIgZBnZJ3Hlu17xsj75xN5-WyJWcLBiFntx92gjcqZ0yoiL96qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقایقی قبل سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارشی از حادثه‌ای در ۶ مایل دریایی شرق عمان دریافت کرده است.
گزارش شده است که یک نفتکش توسط یک پرتابه ناشناخته در دماغه بندر مورد اصابت قرار گرفته است.
خدمه در سلامت هستند و هیچ گونه آسیب زیست‌محیطی گزارش نشده است. نفتکش در حال حرکت به سمت بندر بعدی خود است.
@News_Hut
﻿</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66000" target="_blank">📅 14:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65999">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
من مطمئنم که توافق تاریخی بین واشنگتن و تهران، پایه و اساس صلح پایدار را بنا خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65999" target="_blank">📅 14:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65998">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
مذاکرات فنی هفته آینده پس از امضای الکترونیکی توافق آمریکا و ایران برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65998" target="_blank">📅 14:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65997">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
پاکستان در حال آماده شدن برای امضای الکترونیکی توافقنامه صلح آمریکا و ایران ظرف ۲۴ ساعت است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65997" target="_blank">📅 14:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65996">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر پاکستان:
ایالات متحده و ایران بر سر چارچوبی برای یک توافق صلح که به ماه‌ها درگیری در خاورمیانه پایان می‌دهد، به توافق رسیده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65996" target="_blank">📅 14:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65995">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوری
؛نخست وزیر پاکستان:
ما بیش از هر زمان دیگری به توافق صلح نزدیک شده‌ایم و احتمالاً ظرف ۲۴ ساعت آینده نهایی خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65995" target="_blank">📅 14:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65994">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شهر عجیبیه! تریسام بروبچ دهه نودی  @sammfoott</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65994" target="_blank">📅 14:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65993">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
⭕️
مراسم خاکسپاری علی‌خامنه‌ای روز ۱۸ تیرماه در مشهد برگزار خواهد شد. از روزهای ۱۳ تا ۱۷ تیر هم مراسم‌هایی برای رهبر دوم جمهوری اسلامی در تهران و قم برگزار می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65993" target="_blank">📅 14:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65992">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
از امروز صبح خدمات الکترونیکی برخی بانک های کشور از جمله ،تجارت،ملی،صادرات و توسعه صادرات با اختلال مواجه شده است.
خبرگزاری فارس اعلام کرد برخی منابع از احتمال وقوع حمله سایبری خبر داده اند اماهنوز منابع رسمی این موضوع را تایید یا رد نکرده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65992" target="_blank">📅 13:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65991">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65991" target="_blank">📅 13:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65990">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsFiWYFUkZzGYUeMamjg_p8bzGZALCGhJ8ELobWaB9Hk7aleosRTVIIhZqon3CNdtVjD8P-Fac89H6aXwlvwDuBGz--8vahsGEHekQ4JpirmSjJtnQCgl-XWGe63WvnM1p9y5zDpWl7BTpVB7kDyYnlNmU-eOTeuQ6Pt4OEzvLxYZqi61ipWtCrlLzKStC7Hriuk-yNjDbe1Jqlto94aObcebnnWfNh_-G12bjlIZcdHDVTFMU1Oez89K8tBPpH0QuzqCO2g2N_Mp5oDN6AVk0Kb6BGDBfmak8QYAEAllIHlo5uSQcfYI0X7PXfATbC0sw_yAhCkFc70JX6e3DTFQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65990" target="_blank">📅 13:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65989">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFekwfsq22cIWPjisapT-ehg6FkkP3OWWFOc7cCJSzTsPJSOf3lS3jN9_3QooISM_cAUPvwztdBrQTQgk-PQoEXqUlLEBBf9hZyme-0lB2PwMx_iiqLn2IoYilYSp6vsnf_VVstzUJ_OoGsCp07grm-jmsFUQECcoWL7xrW_-ZhRVuaPPWGoy6SI0avel3Nk_4WxCufmgukYOehBbYh6H-HT3sJq8goNDoqJL-1D-B5QL_unzs7JK3KhtRVACRPFfYAQH1QgfSZkpLYQr_Ertk9FWDnbNqMABraNsRods67uUNzVn1kdXFeBKHgSy-ths9kPdasj_jn9lSQzaebBtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
جنوب لبنان؛ارتش اسرائیل پرچم این کشور رو روی تپه العویدات و کنار سازه یا حسین نصب کرده
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65989" target="_blank">📅 13:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65988">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkBTYLLAnriA00R--DvIV1WqbQnapJPmRF8yDcCnws_rTtI0YiZa-yWlX5cRBFB1tyGVTlpX_2XfwrqfpVgXtI1np1QpE1sx-TOpyD67hWCDkD28PtaKTKiWMOU4ZuK23fuZOF3sPRJENC1AWwf2z_QfcB7Rv7EfYrR-wWDDtpPFITC9z41dbCNTB3bdydn-YLe786sacGMMvYVBxOtF_GqiF13ktqmkQYaUiNrcd3_BnVhE-weydujzK0t3ESpVfpTeNCsy-EtnZLTy91wd1-0j2N3-ECGiZ-H5jMJ0Deme81aTNYLr9nkl-c0NBns-mWmwp5XherT7wO5OWB-pew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ایران تو هفته‌های اخیر حسابی دسترسی به انبارهای اورانیوم غنی‌شده رو سخت‌تر کرده
- طبق گفته چند منبع اطلاعاتی آمریکا؛
- ایران بعضی از تونل‌ها رو عمداً ریزش داده و ورودی‌هاشون رو با مواد منفجره مین‌گذاری کرده
به گفته این منابع؛
- الان رسیدن به این انبارها نسبت به یک ماه پیش خیلی سخت‌تر، خطرناک‌تر و زمان‌برتر شده -
CNN
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65988" target="_blank">📅 12:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65987">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85b34abe01.mp4?token=TrwIjwSi85cVKlxqCQeZI0tjBRYE8pgKMCi1x4DgAuwVnki7HNUrDJSDKOu3W3-3-pqAF3FawqPHRHsRZJc1Hs3K-iSDOfjASZhLVAvm0-G1AAdTYel_4350nW3ef_aytk5wJJp5QcW0viuN8wgXLyJNAamLOfAmkwyI-l5u12rZskCZXwK6VqsbYnYbALEulcoADyRqUDeEnw9e-4L6ILVXExW9fcr9aVtRAiFS6Wm2LEpwqrOGsimoVj9-F22qq6n4PiAj-f6Sg1yjkOy-IU5ffYPpQGvO_Xj8jZVGHCdWlzEcv7b8w-6sc5Hk2wU2C958x_1R62a26XYBybGXmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85b34abe01.mp4?token=TrwIjwSi85cVKlxqCQeZI0tjBRYE8pgKMCi1x4DgAuwVnki7HNUrDJSDKOu3W3-3-pqAF3FawqPHRHsRZJc1Hs3K-iSDOfjASZhLVAvm0-G1AAdTYel_4350nW3ef_aytk5wJJp5QcW0viuN8wgXLyJNAamLOfAmkwyI-l5u12rZskCZXwK6VqsbYnYbALEulcoADyRqUDeEnw9e-4L6ILVXExW9fcr9aVtRAiFS6Wm2LEpwqrOGsimoVj9-F22qq6n4PiAj-f6Sg1yjkOy-IU5ffYPpQGvO_Xj8jZVGHCdWlzEcv7b8w-6sc5Hk2wU2C958x_1R62a26XYBybGXmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انفجار شدید تانکر حامل سوخت در مکزیک
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65987" target="_blank">📅 12:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65986">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a45e16c46.mp4?token=JvZuBpucNs58jEtSg0oUCKZEhmiqrvdgWmn_i2X1FE2E_Q75mjLFB3KA6pbEjw9wsq32LrdGutMTipqpubXu_LYRHSFzPL3TmtFqsMk6PgumACGlGnUH7jl4fGl-x9kGlxKbVjuknbgCkjEOyYrwQUU6w3e7Y2kFWMn0zL_h0vCwIFxoQDtnHtndmgRu-Wi8qmrLUYKrW5RbF1uVglxjXuismYXNOTsrKIKXR3MGv5o-LiDTZ77Kc1bACuKGaTaL8hLdCayv2SnwX2V08srWZDIua3-zpsYS7DBgX5_YLUm3mLvkHynetY7h83u5qoRSNQmlAlqvuj2P--acoC0oEo6hNCpN73a3tsxEfYDBZJKRe-ntKtYdEjJjnOAiWKLpaIZTjOHcWLKLFkHDtNQF2lwQEeUTPeDBvYpGdRWc4rO1CD8UXzKWvED8NSKi4FHt383sLyN_RcG9zaSLGatwY0W-NZKO4-Rue6_om4GWInzlyEpCeauy0bpvqwWPaC8izJ_yVYA6mJ8o-a5frlCTlAeQDBwO47bJsXB4PJ501e7ixpMLh3JRYAuf_EdcH4PdP2gESGC2lTALjZSg3n9nQhVsYBvzD26mP5r5e7gKXmW_SxGqqSrg3DV1RzQIbHtd70VtufYuKXG-IJACqBNA7buB8dNrXMwnj8EGwvGmZeI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a45e16c46.mp4?token=JvZuBpucNs58jEtSg0oUCKZEhmiqrvdgWmn_i2X1FE2E_Q75mjLFB3KA6pbEjw9wsq32LrdGutMTipqpubXu_LYRHSFzPL3TmtFqsMk6PgumACGlGnUH7jl4fGl-x9kGlxKbVjuknbgCkjEOyYrwQUU6w3e7Y2kFWMn0zL_h0vCwIFxoQDtnHtndmgRu-Wi8qmrLUYKrW5RbF1uVglxjXuismYXNOTsrKIKXR3MGv5o-LiDTZ77Kc1bACuKGaTaL8hLdCayv2SnwX2V08srWZDIua3-zpsYS7DBgX5_YLUm3mLvkHynetY7h83u5qoRSNQmlAlqvuj2P--acoC0oEo6hNCpN73a3tsxEfYDBZJKRe-ntKtYdEjJjnOAiWKLpaIZTjOHcWLKLFkHDtNQF2lwQEeUTPeDBvYpGdRWc4rO1CD8UXzKWvED8NSKi4FHt383sLyN_RcG9zaSLGatwY0W-NZKO4-Rue6_om4GWInzlyEpCeauy0bpvqwWPaC8izJ_yVYA6mJ8o-a5frlCTlAeQDBwO47bJsXB4PJ501e7ixpMLh3JRYAuf_EdcH4PdP2gESGC2lTALjZSg3n9nQhVsYBvzD26mP5r5e7gKXmW_SxGqqSrg3DV1RzQIbHtd70VtufYuKXG-IJACqBNA7buB8dNrXMwnj8EGwvGmZeI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
خبرگزاری فرانسه:
روز جمعه، از کشف یک جسد در صندوق‌عقب خودرویی در مجاورت محل تمرینات تیم ملی فوتبال ایران در جریان مسابقات جام جهانی ۲۰۲۶ خبر داد. بر اساس این گزارش، بازرسان و کارشناسان پزشکی قانونی مکزیک در حال بررسی جسدی هستند که در یک خودروی متوقف‌شده در پارکینگ بیرونی استادیوم «کالینته» در شهر تیخوانا پیدا شده است؛ استادیومی که به عنوان اردوی تمرینی تیم ملی فوتبال ایران در این دوره از رقابت‌ها استفاده می‌شود. این حادثه تکان‌دهنده تنها یک روز پس از افتتاحیه و آغاز رسمی مسابقات جام جهانی ۲۰۲۶ رخ داده و پلیس محلی هنوز جزئیات بیشتری درباره هویت مقتول یا انگیزه احتمالی این جنایت منتشر نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65986" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65985">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ac66f6c0.mp4?token=IIV2IFU4s_o_OLy4ZMPOZwBZM9DKuL0L6N0AZRQivwE7guQN75K6eQCDmQ9kar0oUeZYl5VslWCUGfU3K1JY4VIUt_CAwMToCtMRiX2GocrR9WvN8xnLYov2pS6PVH2GMlEajHh9_Jfn4eFIurJxjYlp43HwnWI_4_PAOSkruoHytxKT4O3QKF0QY3z2tJarxmTSzaQKboUAx_GYXdfFtgoR8c0KNJ8CnNrCoWWV2LqvldmROxuZt72MVUA4C5Gejm8t0Y-f5gLELnEK0Pwiaw8c_gKRVn0auv0nUAcJ4iCdASTCkLq1FULQEiGrlzeszbNCypEqcoTQe8lvcIi_9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ac66f6c0.mp4?token=IIV2IFU4s_o_OLy4ZMPOZwBZM9DKuL0L6N0AZRQivwE7guQN75K6eQCDmQ9kar0oUeZYl5VslWCUGfU3K1JY4VIUt_CAwMToCtMRiX2GocrR9WvN8xnLYov2pS6PVH2GMlEajHh9_Jfn4eFIurJxjYlp43HwnWI_4_PAOSkruoHytxKT4O3QKF0QY3z2tJarxmTSzaQKboUAx_GYXdfFtgoR8c0KNJ8CnNrCoWWV2LqvldmROxuZt72MVUA4C5Gejm8t0Y-f5gLELnEK0Pwiaw8c_gKRVn0auv0nUAcJ4iCdASTCkLq1FULQEiGrlzeszbNCypEqcoTQe8lvcIi_9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند تا پسر اهوازی وسط جنگ وقتی رفیقشون خواب بود این شاهکار رو خلق کردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65985" target="_blank">📅 11:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65984">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11109e09bd.mp4?token=nK8CCkhzTaFQpk_kDGLHwHUEIWrsvIFunDMI_bIe-yZi_rG8exVGoqCSzgH-GsrQqz7b-H8eSidXwIiUjzxSGkd1cNLyJHUSn7BsiFngTrSkDFPOBcLFWcUU9-gEy8_89Z72zyz8DLKF1HlML671dfkqxiJ19jMXMsVVnxQ_dE9GGa9aKKs7kxmxKl4uUO26lBPahtcbRgTNNqbyoofTLfDK30VA_YZMdbfh3gvdx1VBqZ-1c2Gx7M2MlpBDKlaXOZCCo4pbiHgDGUbnKgrpyiFMmRTbafbL8Z5fguPs9va3nETApcXKVSlwCG5AEZVOdFChGNENlsdfHZ8DuqmGNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11109e09bd.mp4?token=nK8CCkhzTaFQpk_kDGLHwHUEIWrsvIFunDMI_bIe-yZi_rG8exVGoqCSzgH-GsrQqz7b-H8eSidXwIiUjzxSGkd1cNLyJHUSn7BsiFngTrSkDFPOBcLFWcUU9-gEy8_89Z72zyz8DLKF1HlML671dfkqxiJ19jMXMsVVnxQ_dE9GGa9aKKs7kxmxKl4uUO26lBPahtcbRgTNNqbyoofTLfDK30VA_YZMdbfh3gvdx1VBqZ-1c2Gx7M2MlpBDKlaXOZCCo4pbiHgDGUbnKgrpyiFMmRTbafbL8Z5fguPs9va3nETApcXKVSlwCG5AEZVOdFChGNENlsdfHZ8DuqmGNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ربات گدا در چین دیده شد
یک ربات انسان‌نما که از چندین روز بدون شارژ ماندن شکایت می‌کرد تا همدردی رهگذران را جلب کند، در شبکه‌های اجتماعی چین مشهور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65984" target="_blank">📅 10:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65983">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a77f6aacbc.mp4?token=bV9hsTp_fKYwcSQeBemFTFs2n8MmRBdEETyMgyzeTmCy4u2Ze7a61Z9cDTYAtx71OKPPkXVQ4ZEvBViE5AXB-Byq-GEUTMdo5HcLw01n-vatRyLeUieugn7ZydIh2KF_e77N7fcFBPbgdNj2QzYs7lmr52V1UHgj3-fvFwIm144NS0czeFlpFCDMt6pGMGPovdhXORomckOu1gPbGTdx6gHa6KEaI_yMgSOTGjMqdb9jGAjnwppWzA8ovfnmRcrDCoXmBMy3RYmett-AOfcIl_SMSKmxIhtNfzlGeD_hoPlZrm94c2NZmsY6Uwqk0KT1ZiGMlONaXdxXrulIDPPJDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a77f6aacbc.mp4?token=bV9hsTp_fKYwcSQeBemFTFs2n8MmRBdEETyMgyzeTmCy4u2Ze7a61Z9cDTYAtx71OKPPkXVQ4ZEvBViE5AXB-Byq-GEUTMdo5HcLw01n-vatRyLeUieugn7ZydIh2KF_e77N7fcFBPbgdNj2QzYs7lmr52V1UHgj3-fvFwIm144NS0czeFlpFCDMt6pGMGPovdhXORomckOu1gPbGTdx6gHa6KEaI_yMgSOTGjMqdb9jGAjnwppWzA8ovfnmRcrDCoXmBMy3RYmett-AOfcIl_SMSKmxIhtNfzlGeD_hoPlZrm94c2NZmsY6Uwqk0KT1ZiGMlONaXdxXrulIDPPJDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ بعد دیدن این ویدیو از مسعود فهمید جز توافق راهی نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65983" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65982">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKdP5IkNGCern6J5ZWxtzacNYJs2ERoK5KXSYWu4VvEW9Mv5P1shdtD0OPImfQ-yIrBcL8pemp-TaZl4qtxvhIaIVURX0QaHgc0KizdOBwbzLP4hLHKc0CW2-A6K-Xh7ku0zIASDVgLdFeib1UF54Imyf0xaf9Kc7uUyh_rRVaKWbO0t2YKZ2lb-k6xoHP2FlxmCPRVDJIeSOqpKGbf-8KrHd_aKe6ve_8SU4XcYwu7jyBvCcBRqFoeryp88LcbDjejTurdKV1tEC0bffQ7JBYBig6MP6KxhHDX4_myCNq1U9sjYNHwTHHuFrtqdB1d9QYISdprMwn-Vs7xXf28unA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام:
ایران چندین پهپاد تهاجمی یک‌طرفه را در تلاش برای حمله به کشتی‌های تجاری در حال عبور از تنگه هرمز به پرواز درآورد. نیروهای آمریکایی در ساعات اخیر همه آنها را سرنگون کرده‌اند، در حالی که جریان ترافیک از طریق تنگه بدون مانع ادامه دارد. این کریدور تجاری بین‌المللی همچنان برای ترانزیت باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65982" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65981">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65981" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65980">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=bAq0aA1CxMQ1Oey-nWGuAwpet_3FrfDwGgLi6wuFsXkgbcl_IMjof6I5cnmX-_BU-m2QQx9B_oNIoViTaUl_zBzayAQ6J5NCZWmq6MJ_liArYOCuzDGH0OwjKPoufTcVAk4x9gVyoNsNbwiKpbfYCyfblihPBl2v_9XskHizlHn-g4FxHhKkoiitWLLC2MzHnwnbqGRc5p4q5zax5vZ9oJy4pRhRB54kxKMy7I0I4Hc6d9Ix7nVoYC7ViXSTtlzYfzLh-RKLkmdB4fr6C6ny9b43G6Weknlt3nRiBPshZBxLtcomdN2IOiBL4L2RWv-XrGzMTYI_F0z1eHDYhiCz9Scv_hd4wosgUqciCsLfIfFi7TaBTJ1w7VD_g-_Zq8XKLUOMJUJT1VuIRPU4wO7spcXtBzeux0_i2DGo7_55Zs0NlClAkoHExHye02UCy7EMyykQzYXHtnynAnf8eLu54YWPGMAjh-vOEvrDkRXhcdhbJKJrarskB6mlA5kDf8ro5vNReAynPXqIS1mt8zTyiW_m1ztLC-WSwmGfmp5AefgnVJ2-sUWY8FzYpMVnTO6Dd97BfklRwijQBvXzJ-lIHgy3LZ0nzjGKZyJ2HHtXYomuyqG_w8nBdAdkhAJYu94x0QfQE_uWscag0aZXM9Ghu_ebpfDXpqgUblHrLFk2QJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=bAq0aA1CxMQ1Oey-nWGuAwpet_3FrfDwGgLi6wuFsXkgbcl_IMjof6I5cnmX-_BU-m2QQx9B_oNIoViTaUl_zBzayAQ6J5NCZWmq6MJ_liArYOCuzDGH0OwjKPoufTcVAk4x9gVyoNsNbwiKpbfYCyfblihPBl2v_9XskHizlHn-g4FxHhKkoiitWLLC2MzHnwnbqGRc5p4q5zax5vZ9oJy4pRhRB54kxKMy7I0I4Hc6d9Ix7nVoYC7ViXSTtlzYfzLh-RKLkmdB4fr6C6ny9b43G6Weknlt3nRiBPshZBxLtcomdN2IOiBL4L2RWv-XrGzMTYI_F0z1eHDYhiCz9Scv_hd4wosgUqciCsLfIfFi7TaBTJ1w7VD_g-_Zq8XKLUOMJUJT1VuIRPU4wO7spcXtBzeux0_i2DGo7_55Zs0NlClAkoHExHye02UCy7EMyykQzYXHtnynAnf8eLu54YWPGMAjh-vOEvrDkRXhcdhbJKJrarskB6mlA5kDf8ro5vNReAynPXqIS1mt8zTyiW_m1ztLC-WSwmGfmp5AefgnVJ2-sUWY8FzYpMVnTO6Dd97BfklRwijQBvXzJ-lIHgy3LZ0nzjGKZyJ2HHtXYomuyqG_w8nBdAdkhAJYu94x0QfQE_uWscag0aZXM9Ghu_ebpfDXpqgUblHrLFk2QJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65980" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65979">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEKuz6c-w2VYiBC_W9cV9SXWimKsVg7Rb0iouA-6UnU77OaAZaLASI2dGex73HM9mhrtEq2YnngBq4jDgPtN7Pn-ht1xAWd1hsBfQzhszOl7NBzm_yZf_dY5tSjsxD8FRQlYYb3RzS3mXGT3hzhTvl5xviF6ASbhSoRBJu-RgG52Qzs__vyIa3FF-3-IfLZa1-0R9dBZaLFoqRdw8OwBSfCCadtoasStiyrzbT-al9X0V4jlYXBhnL9PKKJPCBsNMz-fINHd3BMUH8IiGC9GDxU4A_Qz2t3_I7nhOhYAisnb812YzoasZzPOKp2GoRzCblHpveFe_3ohSSe_14CpDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روح الله خمینی:
اگر آمریکا و اسرائیل «لا اله الا الله»بگویند ما قبول نداریم چون که آنها میخواهند سر ما کلاه بگذارند
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65979" target="_blank">📅 09:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65978">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b92693abb1.mp4?token=IiUaZgHqoZ1V8kYlyajdk5cDr6yxzomW7q5k91Z1hCx_nbKOqNkjT8cE7IE8PXSL3xb3tPe29RNQ61ZvsLtUltPqFCK7S_D1WsaOivTVL2SOAWRdAxx86Iwp3NYtfkkKZ9MkKraRERB5WrIioiZm4cTDcbzy5Ftw40QNn7e-cjT_lcjIwxL7_Mo3SJm3_KEEKKPoAv_nx6IQ55FeAGkCFAcKlTLWOezO_GxWCRfQvKvN2Js_3rml-ib9ueqKdXtaYJyzk2azynYnI3K7jQK998EijKJAslTWMWz1leiCZivYqLv81hPnDfgJFCLm28H1kl5IyUsQJUh7GRNyYqMC4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b92693abb1.mp4?token=IiUaZgHqoZ1V8kYlyajdk5cDr6yxzomW7q5k91Z1hCx_nbKOqNkjT8cE7IE8PXSL3xb3tPe29RNQ61ZvsLtUltPqFCK7S_D1WsaOivTVL2SOAWRdAxx86Iwp3NYtfkkKZ9MkKraRERB5WrIioiZm4cTDcbzy5Ftw40QNn7e-cjT_lcjIwxL7_Mo3SJm3_KEEKKPoAv_nx6IQ55FeAGkCFAcKlTLWOezO_GxWCRfQvKvN2Js_3rml-ib9ueqKdXtaYJyzk2azynYnI3K7jQK998EijKJAslTWMWz1leiCZivYqLv81hPnDfgJFCLm28H1kl5IyUsQJUh7GRNyYqMC4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی خامنه ایش رو میکشن، مقاماتشو میکشن وتحقیرش میکنن بعد میزنن تو سرش میگن بیا بشین سر میز امضا کن.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65978" target="_blank">📅 09:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65977">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65976" target="_blank">📅 01:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65975">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dznm-cOmEmLdUT1AHYEsl-CdW3L2XZ4qj0IrvusX2CHNCHWCkcLETHXsC4juh25AYjPOZZnFrAszg0yq_weOOIo-LHZ4PLUBpnd3_-UVSTmcB_nQHpbhBdnpTb0vyiGNjoUPtB2QuNr0WSm7QYUXAp6q-L0pw0daCWBgr7ygUzjaZT00pYEieAPzP_GzoPNqc9a58vzT99kvVxEcokCKztdgGDFu98-eqWFOM7C4U6NJHXStHsDhTwt21w3O93NJ93wVKzCG2z8GbcbepFdmkZw7gHw1J3dlCF_5tfQbiWqeydBmIoPUE3jX1GmFQzulERruQiRiBSH9tT2-DXzTcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تندروها گرفتن رو قالیباف
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65975" target="_blank">📅 01:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65974">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
سپاه:
کشتی هایی سعی کردند بدون مجوز از تنگه هرمز عبور کنند و مورد هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65974" target="_blank">📅 01:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65973">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAvtB2USxSHR3eotodPjL9k0VVRcSYFC0K19JTOgr69_hLT3ZU5mma62PggrA7hySmiGr0pHE0g4BO-17u-mrJRB6NUhVy63PqjuK5pysA66WS5Obm5PcN3uezvPOYcnctw0A1QOviLC8xP8N1xcHnMhvdJ85kOxg3rR6istb4I5sC7fFtFcNlzbDZoa_lHgg7fbGlstGWmKn03V-2e_easF7jFmXNIma8rp2ffx5SaOkuQ7FA5NYpWvRF6-j3SXzcHdxteU3G8Kt17kgV8-EbN9ImVo-EwE-eDDNWHKZrO_5f0PUXhTmZLeNFONLbgdzEwNv3TKa6Pt9I5449ZT4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65973" target="_blank">📅 01:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65972">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
نایا خبرگزاری عراق: شنیده شدن صدای انفجار در قشم و سیریک  @News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65972" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65971">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
نایا خبرگزاری عراق: شنیده شدن صدای انفجار در قشم و سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65971" target="_blank">📅 00:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65970">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=oYAFjvaY98Cf7jUNxx8FfaooCjlNQs1LD2NjafxmxRc0IEYYsGoMnfnAmIIWDpyFuPyg88m6XavX92hIyMg-EivfUwmay6b7A97wKSy8dSJITRQk-Hb14yRTZ1qoy58pNrwSJOkQYy6xJIbevV680QKlVapYZpuFiRe4C3b2eZxF0vu7E5y2JRcGWgql8U6VACDjwp2Xqo_iU8Tjdj5VqA25rzgwP5TSj0wZa4G9QZP5V2A3zpDYbMxum2p06_TqdE6ucutksFwpbbT1691xkax2a7mkr3MbVknmD-HZzRmjGjNkC6KcAdUIchTHytH06u3V_JPq3gp4jWV0W48f3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=oYAFjvaY98Cf7jUNxx8FfaooCjlNQs1LD2NjafxmxRc0IEYYsGoMnfnAmIIWDpyFuPyg88m6XavX92hIyMg-EivfUwmay6b7A97wKSy8dSJITRQk-Hb14yRTZ1qoy58pNrwSJOkQYy6xJIbevV680QKlVapYZpuFiRe4C3b2eZxF0vu7E5y2JRcGWgql8U6VACDjwp2Xqo_iU8Tjdj5VqA25rzgwP5TSj0wZa4G9QZP5V2A3zpDYbMxum2p06_TqdE6ucutksFwpbbT1691xkax2a7mkr3MbVknmD-HZzRmjGjNkC6KcAdUIchTHytH06u3V_JPq3gp4jWV0W48f3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صدا سیما: هک تصویر انفجار اتمی در تلویزیون، سیگنال آمریکا بود
!
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65970" target="_blank">📅 00:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65969">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060800d75a.mp4?token=EMjeuEAW6Uqd5slSfr54k4tvQT0YcdMEBIHXIZnUdi8ndjJU2u9otS40U6bfa8Wthkh6KJAGmSLtCsIxOkZMgsA2ATHdfmuDWE1-_YgupUFrk1Zzi3XnOP71SqClzqsht5aZXQurnpmyqUetFMg_UFipg03iL06ZsHOJffQFbiYOzdaYkiriFaWY9lj4swmUEmfaWXMN6vDOholUYVX5n66X__9MK3Qmqxd5YaJaZjXLnouvUYEfJSG4pD8_rBA3mtKXrGU5gbojnPe20JsLJJQe-zyy4kJMjZufovvN2rlmwhg8Z9L_skG1fbULeDa_wDPWAdscDLXBQfNtgJBvmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060800d75a.mp4?token=EMjeuEAW6Uqd5slSfr54k4tvQT0YcdMEBIHXIZnUdi8ndjJU2u9otS40U6bfa8Wthkh6KJAGmSLtCsIxOkZMgsA2ATHdfmuDWE1-_YgupUFrk1Zzi3XnOP71SqClzqsht5aZXQurnpmyqUetFMg_UFipg03iL06ZsHOJffQFbiYOzdaYkiriFaWY9lj4swmUEmfaWXMN6vDOholUYVX5n66X__9MK3Qmqxd5YaJaZjXLnouvUYEfJSG4pD8_rBA3mtKXrGU5gbojnPe20JsLJJQe-zyy4kJMjZufovvN2rlmwhg8Z9L_skG1fbULeDa_wDPWAdscDLXBQfNtgJBvmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
گفتگوی عراقچی هم اکنون شروع شد.  @News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65969" target="_blank">📅 23:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65968">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
عراقچی:
محاصره دریایی آمریکا اولین چیزی است که در این توافق به آن اشاره و تاکید شده است که باید رفع شود
دارایی‌های مسدود شده طبق یادداشت تفاهم اگر امضا شود، آزاد خواهد شد
هیچ‌یک از دارایی‌های ما نمی‌تواند مجددا مسدود بماند
برای جبران خسارت ایران طرح بازسازی در نظر گرفته شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65968" target="_blank">📅 23:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65967">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
عراقچی:
به زودی ایران و عمان بیانیه ای مشترک در رابطه با تنگه هرمز منتشر خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65967" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65966">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
عراقچی:
به طور قطع تنگه هرمز به شرایط قبل از جنگ باز نخواهد گشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65966" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65965">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
عراقچی:
پایان جنگ در توافق همچنین به معنای خروج اسرائیل از مناطق اشغالی در جنوب لبنان است و ما این موضوع را صراحتاً به طرف مقابل اعلام کرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65965" target="_blank">📅 23:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65964">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyUesRTkPBpF8VwrE4oiqZekSmebmmNq0cnerKPcIRMHwo-oLXzONeFPAEbZTO6T3-6534cKjVg5d1LgfnPxW_hfHZeCqZ5dQnY-jHmu8vO3PhJs6CcMnmdY5BTdup1_BhJRPoI4GX7xBJdQZSXsebkxPgkfS-5jpOGxbrIKhWG4N4Dkdb3N5jgCy5joeZ8HBxNct1oHHm--Rxe-VESVYAVE1hUJhLCmN6ejdqPfpKgSdY3iuhQysyIpzBnFvy2Teipgt0HhC6bbRUvLcnR8gMaNjxM_MtOEdCiWAYuWv3qgy5ENaiqsxsAjZkuwo7Prc7_GEKJVRu8z-LIkIU-ztA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
تعهداتی که داده شده باید حفظ شود. نه اگر و نه اما و نه بهانه‌ای. برای معامله نزدیک پیش رو، راه دیگری وجود ندارد.
هر چه بکاری، همان را درو می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65964" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65963">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
نتیجهٔ تفاهم یک یادداشت ۱۴ ماده‌ای است و وقتی نهایی شد تک‌تک آن را به مردم می‌گوییم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65963" target="_blank">📅 22:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65962">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
عراقچی:
ما پیروز میدان هستیم؛ مقامات خارجی به من می‌گویند که ایران را این‌گونه نشناخته بودند و ایرانی‌ها شگفتی آفریدند و با قدرت بیشتری از جنگ بیرون آمدند
من می‌توانم اسم ببرم که کدام مقامات این حرف‌ها را زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65962" target="_blank">📅 22:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65961">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
همهٔ ما مدیون تک‌تک نیروهای مسلح هستیم.
همین‌طور ما مدیون مردمی هستیم که ما را تنها نگذاشتند و هرشب در خیابان‌ها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65960" target="_blank">📅 22:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65959">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
عراقچی:
دشمن تصور می‌کرد که بعد از جنگ ۱۲ روزه، در جنگ ۴۰ روزه می‌تواند ایران را تسلیم کند اما با مقاومت جانانهٔ مردم و نیروهای مسلح ایران مواجه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65959" target="_blank">📅 22:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65958">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
#فوری: طبق اعلام زیرنویس شبکه خبر ، عراقچی تا دقایقی دیگر مهمان این شبکه خواهد بود  @News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65958" target="_blank">📅 22:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65957">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
خبرگزاری تسنیم وابسته به سپاه؛
حزب‌الله: لبنان نیز شامل آتش بس میان ایران و آمریکا است
«حسین الحاج حسن» نماینده فراکسیون حزب‌الله:
بر اساس آنچه از سوی مقامات ایرانی به روشنی به ما ابلاغ شده، لبنان نیز شامل آتش بس است.
بر اساس آنچه مقامات ایرانی به ما ابلاغ کرده اند، اسرائیل از خاک لبنان بر اساس این توافق عقب نشینی خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65957" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65956">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwHLC21_6VeJaOkKenfA6d_BtKZdUiiQDmYrHCKdEEjTwlCNiI4NFPpvz5yUM0NAYt8-OB6S9ti0Hgrz9NoB6-aCW_oEouvAow98O7kvo1-UI84Z8ZTGMfyLiMSzGxRcMQpe9Kw7cHDa9PKxxmAJYS2fMptxfaC06seGooTSyUcr_UlJT0MzyqAMLMzC40FNRsIM85fxLbQnVyxJcORbCOzXORIS5TCZCSoIY_4frbuuBlqXUvqNtMaMq7GoRj1sxdVgUQi4SKBkEUz8BzkhgTxmJRZmn_-SBuf_ky0MomRXBKPzhVL_0fvBeH_fF5WY2o3XXvSMg8xREvmmsYf3aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
کانال 12 اسرائیل :
توافق قطعی است و این به نتانیاهو اعلام شده.
ترامپ از ایران خواسته به صورت علنی درباره توافق شفاف سازی کنه و هشدار داده انجام ندادن این کار پیامد هایی رو به همراه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65954" target="_blank">📅 22:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65953">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
رویترز: امارات ۳ میلیارد دلار از دارایی های ایران را آزاد و به آنها تحویل داده، این اقدام تضمینی بوده در ازای اینکه دیگر به این کشور حمله نشود
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65953" target="_blank">📅 22:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65952">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XS4st3yPMVOsDk-uKqRC5NEE_lnvPvxkucwazjZseYzjOsAcc0A4CCqBrd4Q3Pzt7NgTEYQiiRTe5x5tJOoMEe0BC1uXhl9643vAkICBSmsKhG1yLxeumLmc6A2F9_SagcxvjFodsuFh5js-zpW2EX3W6csI4ojUN6NFGKJCCmvoHtLOSo8QUInX4b_crKISX4-QC70qEfsSPYVQBC7AkXd2rCs4GAtVh354Egtznds0IkPBZibj5b1pjK3O5qf9vaoirL6p0RnIG-oHu-3Z0NFD6s73_9zn7Mbzvdm1PEL6jNg56XiBn03hORFWlq9wRPLrBDyfJsOtaTe8Vkveeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#
فوری
: طبق اعلام زیرنویس شبکه خبر ، عراقچی تا دقایقی دیگر مهمان این شبکه خواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65952" target="_blank">📅 22:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65951">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4dZO_iJgBWXGhWNveqt1rIBgcwOSolTFrxGJgsFsQ87RHyRl8QhI0Wly_J8kyoYsmmJvZR4W0dCSpwAnrDShqNBW2WY_08Q__HC7TcNgp6C2ais5k7ja3nykFJ4xJ5M1SJaDRrB-WKqMC4DkUDkwZFPNVDE9Wo56NIgx6IXyz21Z21Ys5DkpQ1Gbq-remRu2vTCZTMgF0xYBBI3e9Gt1f5wP6FmAvWlmJy6gN_NYx3284rpd1IaMpEh9-7TDTIMeSQLo7RvwONi8m3yqJ2F0K_yBbELTx74mOyw6-jErnGhObi4TUUiJgermTdzVDxcfFXcVy7ovWPrY0WCZ6LTyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا به شیرمردان سپاه اسلام و حضرت آیت‌الله العظمی سید شیرمردان حاج آقا مجتبی حسینی خامنه‌ای، خوب دارین کیر می‌کنید ترامپ زن کصه‌رو #hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65951" target="_blank">📅 21:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65950">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1zPFDSfnJVsVPGORup6fc_csx4tpxO5tyn0RzmdQSccyazvpBOglqhkpWANfmWK6-HI5RF4VZqFxp08VRf-2PU2PUgJkq4Oa26c7Y38NzeTgJaZGOnJC_praaSYZJB8T9nD26_8BvB3-9C_ubMn4bCqesP7kP1lB9AJ7u38tJtLpohFCl2FX3Zw6VkF97CkCwQTdc_yHVQWs3PkQdBZLBiuOz-0Q5u4pLHaiKew6i4QQ257IcKX1vQUW-c9AOon4YerHU6KJLzrlEFzWDV_ajr5OX1DcEh2XXnwIKi5OxBn0YcYJxe4k0Ud1DnFZMp3SEpbYhBdnP7bDJ98vyuH_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:
طبق اطلاعاتی که به دستم رسیده توافق احتمالی بدتر از برجام است.
نه احتمال جنگ را از بین میبرد و نه گشایش اقتصادی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65950" target="_blank">📅 21:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65949">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
الحدث:
وزیر خارجه پاکستان امشب عازم ژنو میشود
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65949" target="_blank">📅 21:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65948">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65948" target="_blank">📅 21:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65946">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WE681opJbShyDxHOkZRQXql1EuvootfQRya3bUTrMD7KjzlkfgkgK-bLBuVdCjN6xcLQ7IBBd3a_oqryRLWiWlxusAA-neNNhDBwFmEkaMFRJtoP0eEjhhe4bMIuuebDc9jBJFaaFaPcOF8pH1VuyVlEeLMg-aw0ktyTig9nDCOM8btJ9JhgvSAb2pKStBs4IceOjlIuv8plAm5B23lzKFGaQ_pKZtDHV4EOAqMXJlwqldWycw_c3Oa37_Oj5NqJF3Y_1A414LFHE0nI29vwbCMFOK9oNMgstUXbj_Ts6es9q0iRfhigQrBg8IKlIOex41pP0QDKKJ4ZX3746-wu4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65946" target="_blank">📅 21:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65945">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e7da6863b.mp4?token=AbbB1nA33lTAR-RYrHZiuTqtGRbkuvQAWLlIcy6e08iZekgDdJAaC27OXFp8xav-xQEmbAUx_D9nI21CZCX-mNLE8zFJti6rImDnFvY5fFjuBChZTAk8qMoOX10_m5H5mR64LcQh_YSjiYmnhK4fRqP8Y5O8RJhkfFsQXFBaRr_YPflqOXyaY3IIPWvzgc8pAj4mhvfj0scLZoLCdzW89DVHJMXJHC7om4NWcPl8F7zYYLbIwlch0byG2FZZdfpho1a7bZDq7dOVPJcNArxzeFe6ZBjCZKUQNSb2OqF3Tg7fxEH7sjDWK38e7kRT-ffJ0Orlkdc1CNSUPd-d5mMEFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e7da6863b.mp4?token=AbbB1nA33lTAR-RYrHZiuTqtGRbkuvQAWLlIcy6e08iZekgDdJAaC27OXFp8xav-xQEmbAUx_D9nI21CZCX-mNLE8zFJti6rImDnFvY5fFjuBChZTAk8qMoOX10_m5H5mR64LcQh_YSjiYmnhK4fRqP8Y5O8RJhkfFsQXFBaRr_YPflqOXyaY3IIPWvzgc8pAj4mhvfj0scLZoLCdzW89DVHJMXJHC7om4NWcPl8F7zYYLbIwlch0byG2FZZdfpho1a7bZDq7dOVPJcNArxzeFe6ZBjCZKUQNSb2OqF3Tg7fxEH7sjDWK38e7kRT-ffJ0Orlkdc1CNSUPd-d5mMEFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شهباز شریف:   در بحبوحه تلاش‌های میانجیگری فشرده پاکستان، ما کاملاً از کمپین بی‌وقفه اطلاعات نادرست که توسط کسانی که می‌خواهند توافق صلح را خراب کنند، به راه افتاده است، آگاه هستیم. گذشته از این سر و صداها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65945" target="_blank">📅 20:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65944">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WthNvDPTl33G9hz1-nnMqZVIJjsoZ5t-Xiwq8-jRb1PLixPyfr9BBqcDwtL4E9u7FSUAOjSfwBNMvDjv0l5a6vJtI3WhKTivFO4Aigvm71EocJT1JVufhH6klTPLO9syEU2v9xagF0icYj5e7ODqHT8NyV9_ByoZfPYrvnAaH-yN541vJjY3m4nMgLsaUwIabwyQIfNzXzNBEgnqhZh66HCB-13P6AM1fwnA9II7_Emg-w_5QtVGHZ1QDVZxTRAbh6OoZAI63FlNcDYOkcx1LMJ9QIq1Qr7XUff11WZQUdaWLeA0mCKFE7ViABwR4o7NPLAqgrl1cLTGLlfGIK-cVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهباز شریف:
در بحبوحه تلاش‌های میانجیگری فشرده پاکستان، ما کاملاً از کمپین بی‌وقفه اطلاعات نادرست که توسط کسانی که می‌خواهند توافق صلح را خراب کنند، به راه افتاده است، آگاه هستیم. گذشته از این سر و صداها، می‌توانیم تأیید کنیم که متن نهایی و مورد توافق توافق صلح حاصل شده است و پاکستان اکنون از نزدیک با هر دو طرف برای نهایی کردن مراحل بعدی همکاری می‌کند. صلح هرگز تا این حد نزدیک نبوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65944" target="_blank">📅 20:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65943">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPcAwG5wffXd2nMY_BlC29b7Ouqt_5rNDCb8BfbGNXHPNBG8btnn3m7f6fYF32_XPnHVgess9QysGhl_gYa7fQOQA4iO7bKt-q3bIU_9bAhEv813Pa4o5XtUqHutM6ADknt98AU2YINE5zZCa2obKVeKeut6aghgcZm2bcoCUCOYxVMIagcucG43zusQimWpIuj1y8NvTzSLlC7IdvK5UU4anVKyCJIwFiXBg_d9i6jcSl3aTC28R1zsFl3T09L2ZnmTH7iOHYCBBkOt3P-vkj9iH7giy9HLwMCwfjTUUOndrjVww1D6J5M61rUQoDYn8X-RdTXQKJSLZVCVncUvUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندزی گراهام:
ایده یک صندوق بازسازی ۳۰۰ میلیارد دلاری، با توجه به اینکه چه کسی مسئول ایران است، به نظر می‌رسد بی‌معنی باشد. این شبیه طرح مارشال برای آلمان با وجود نازی‌ها در قدرت خواهد بود. آن زمان این ایده خوبی نبود و هر صندوق بازسازی که به نفع این رژیم تروریستی باشد، اکنون ایده خوبی نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65942" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65941">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCTO0Jyxd1j4GOz5vJJzstv1pqSaq1WUIC54BT_CUb7N8lrG3MuMRdEtybOZUqWedPTkfAA_V_Ka9bT_MtRSr0jLUEs82SIZ_kbG7Xnf-GGbL32b0xo4ZXrPkyc7TTsFSVTySuIVvDsLJEAiDRSwXolhv59f6GI4G2LvohIFaFhrRV2GbZt7aeQRZMayrqhvBl8_BB8BllPYUKRvQzVa8jbmFS5CZoDIgE7M2z0c0kCI38pvWdahanuOahPVvUoA7EAg837y-mKvL8UXe9CuDrth5hj4lNzBjyGis3t23ojeCjxrsYT9xsO0CV3buqg_BOVxfoFVvhOZXSEJLmw5XA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65940" target="_blank">📅 20:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65939">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MceOTfjTqAqOsj6mI0lxDlrzy1cyiK4ijeJ6-5VbPWXaVjW8kOQOi8NaPppIe3N7bvQzK7JHf_2ShKMyZrH6IJqlNVp5sXPjyThcPaImzrh6_ZmRQOaWURpBmIazfwDMbjFol5t5Ka21EAjITdRi2TmdrSq_TcudlykaCFjr-JPYNfonxLbECICKs3zA8KNszjgqC-MXCYwE1UzV-InxxZ0I-0s1D5FWWafEbtaYt_9UlUx8HTSA1yqL_YqNE4f5I-Wxe3S3VMFfB2Uw_ykjy9GokGbjX13UxQMURyubb8gQUpURn6TyJgE0-JiQsNWjy5Wgr7F7TSQl2vVBhEgRmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام:
ناوهای جنگی و دارایی های هوایی نیروی دریایی ایالات متحده همچنان به گشت زنی در آب های منطقه ای ادامه میدهند و محاصره علیه ایران را اجرا میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65939" target="_blank">📅 19:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65937">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3347ca6.mp4?token=s3BVlHm54IV_lv2E6twpUgcwafZ8wX7kFjvlX3XiQG32Jo0HGWWGoW2Wn6Z9Rc0fimGs3O_Qa7HekxC3811wPPyJ1BjJj2bhi1smQ55T93Gfx5KAR2F95wb-soyF9m-oaZIqLyCUgXvTQbMmGUixct1FWCCxhUa8N-E7CQiAAofk24QqM7VpEgnrsO9okPIi4-cqm8Q5KwYRMN31VPpjZ2T5sfrNT3BaiK2p4R2yzWWlJNSc-hXo5WCgIF-9vxc-hMHp3ojGR0bYKAnRy3KAbUHb5Qjxat08y-lXtVdO-Hpe52mtQLUof7TDIj4qX4ZP4nyqsF20hOVxQ4uuV5A7OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3347ca6.mp4?token=s3BVlHm54IV_lv2E6twpUgcwafZ8wX7kFjvlX3XiQG32Jo0HGWWGoW2Wn6Z9Rc0fimGs3O_Qa7HekxC3811wPPyJ1BjJj2bhi1smQ55T93Gfx5KAR2F95wb-soyF9m-oaZIqLyCUgXvTQbMmGUixct1FWCCxhUa8N-E7CQiAAofk24QqM7VpEgnrsO9okPIi4-cqm8Q5KwYRMN31VPpjZ2T5sfrNT3BaiK2p4R2yzWWlJNSc-hXo5WCgIF-9vxc-hMHp3ojGR0bYKAnRy3KAbUHb5Qjxat08y-lXtVdO-Hpe52mtQLUof7TDIj4qX4ZP4nyqsF20hOVxQ4uuV5A7OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی قبل از جنگ ۱۲ روزه و ۴۰ روزه:
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65937" target="_blank">📅 19:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65936">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMh_UeJya0075l0XTdys64v-KCEcw4bjH9kPxNHKpYwZ73qtct1bpNVcRyBVppUGNSJxCyXaFLsrpcS31YF_xhLKaX_Dg0RngPHRh2m-8pMMBDmuOFv4-Nfl8tcgWjp9QkroQ4PCsWGkUQhUo1HiaSyR49fYS7w9NREELRyhVbDvmNLWs8PFHvwriElE3Qlu5wbAQUKQLR_zOQ4vHnkxNbaR_abT6rBJJ9G7B4oIJtu8uYRWbQG_cGEehBE9z_rtX_r7hjPe2pHffEPTTCFfT4N2AZDZ97Vxf2m_9jLdjvzyDz5OFwsjekn3JD8Rn4mCZppdf_867IGpWo4aSQAQAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: تفاهم‌نامه اسلام‌آباد هرگز تا این حد نزدیک نبوده است. تا زمان نهایی شدن آن، رسانه‌ها باید از گمانه‌زنی در مورد محتوای آن خودداری کنند  @News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65936" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65935">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
جی‌دی ونس:
اولاً، ایرانیان هیچ وجه نقدی دریافت نمی‌کنند و هیچ وجهی صرفاً برای امضای یک توافق یا حضور در یک جلسه آزاد نمی‌شود. این توافق به گونه‌ای طراحی شده است که نگرانی‌های ایالات متحده و متحدانش اولویت داشته باشد، و اگر جمهوری اسلامی ایران تعهدات خود را انجام دهد، فواید اقتصادی به آن‌ها و کل منطقه سرازیر خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65935" target="_blank">📅 18:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65934">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تا دیدن اعصاب ترامپ تخمی شده عراقچی یه توییت زد گفت رسانه ها چیزی در مورد جزئیات توافق نگید :)))) #hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65934" target="_blank">📅 18:45 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
