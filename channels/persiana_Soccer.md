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
<img src="https://cdn4.telesco.pe/file/dxjWttm1eoD7zvH2Mb2Uw7FZ-8PkdNfpiViSv_GRNxSYrbP3suAn01wluDKPcu7rJ0hGvSwteZGH1xjXW1Kfm-2QI4q00AN9vUC-MItuVyXFhda0DE59wXlQwG1IHHMy3NDWdfwRFfBacrr6mxrQCGcy8jcjxURnFqZBdRlQ9EZcrl57kYXveMEkGne0mSAmR-Z0EnryxOGI8ti4GBLUK1CeUv-kuwnPQIznEU3WqLjsnh3BU_LR5EG9x1oKN0yIm6fma-vSDmfDR__fSOfFIg3BqCKTsju9tuk39dnvcKqdKNNWLCBdIJy6wWfqSY4LYtHRhzR7KUl8OR-tbUOUdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 624K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 23:36:25</div>
<hr>

<div class="tg-post" id="msg-26969">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGkj0yp-MGBx2IaJGP7PmCZo_G-RgMhArGXjuj6mgNNNbG1KHIUBj4nYHROQ7iBW95kGXiMQDN6e4T1ca6mzofyWZ7B7F3n_iVr5vBoZyaBF1VZ0CMvLn9o9Sl4B6xKULw4kC8f6FC4sKA-OibgwmFPEIAtkyEBXpZKnR1IHfGXB5aleUJh9mPO2dm1RBeBrkpdv0msuB9t6UI8WZyZjFO1QrMHrM7188Oby_lHaZaXYp3ATEHMUYiK1GJsPXmd7SczIstBuIebr-Kl02iNK6qhNwvF15PB7c3scBhNt-85xFGKCDhepVfuCNwDxEmRL2dpEcq9qtwNiHvuEedGN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/persiana_Soccer/26969" target="_blank">📅 23:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26968">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJcGmFTgXeKGsArk0bLpQypS4TrFGYuiEt-dcAUkE_V5fHyfAXtQAXmIU3eyH5NhR4nfMGccWbEGi6iJTszlAma8G8YqmDoUKwNCXTL1CrKRw2Xtt7Os06wzGl0qp8TQA8ixEnBYcYkh6_1_iLUL9kcUu0K8fDbl-jptA1zYzEhthy619GQDSfLfCPF3OkpQIWefQClfyIFQiA7jMa9SfrEftM7x8jSjQyBmRHh8EqLaCpenbQ4SeQfVFYxft0orNx8Fm5h0wLEka4Q4ytOvKs0hSe9rcFhdcSXXPZGBmBiDZqayPu_xPbk5pPeC_ZHTNl04Pb6LRoJqhU08BhhBhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های ما از باشگاه پرسپولیس؛ علیرضا اشرف مدیررسانه‌ای سابق‌پرسپولیس‌بار دیگر به کادرمدیریتی‌سرخپوشان پایتخت بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/26968" target="_blank">📅 23:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26967">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL4M4pDR0qeyngTH3G2rl5nXsujun4Qd2RrygoLb0CJJdSQ2q2i9MLpNx9M6WuchLfAM9fKE9TBMO3FC8Ot2AvWNX5HdTSMMCUknRnT2-izRVbllxRNULbLU1fgoWlQ9RkibDIY_yeoXjPeN7xyrkCSWwbNBnEmOTvaqkBYgI0If9FmftMVVuLZzzAo4W-qmq6MgEaI5aWAAVmxCWvkR8orRprbjS2mCToWlfPnRGNj6ouhgRSaEHc_80Yr1saH6vHLjDNMihwgwm2C7mBKbMCiOoc-xxYNAMbedfxCVxJg5Xep_oWDqe_f23ZCVit1-O7nFCi1l6mwbZe_9ID3s9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/26967" target="_blank">📅 22:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26966">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBoivn64JUdRZr2isyCIh7za7kdAZ6TnMFM9amcc7-dPW-OCLxcN-mWL6wIBlZVieoiC_W-KDuAq3wOXDw8-ZJa68yj4f7p3w4CgNdS61olk4cjja4Ol2n_OlyGdJKCXua2Tig3pvineSrnfHnz0MTIrKyoFo_b-2o1OvalXM-8OD-_Ae-WoZe0aMIfvEhJ-E5ONYmVJIVKj6kF3JrmqC10dv7XcJOC1A3Bc9G4_jwm0VOqwqY7GQ-dtbT7Xn_nRAQ1h9UyStGanJc_66QhttY5LMUsutMp56f0BOm33Ad7JA4KSzzUSVhlbR_DIPb3ttyNMybi_s53EvkLPCh4Trw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف‌شایعات‌مطرح‌شده؛ باشگاه استقلال تابه امروز هیچ مذاکره‌ ای با آنتونیو آدان دروازه‌ بان سابق خود نداشته و برنامه ای برای جذب او تا نیم فصل در صورت بسته ماندن پنجره آبی‌‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/26966" target="_blank">📅 22:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26965">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WW70BsjGJ7O1MFImFenjokgD-7Vf9ZTo9JitdhXIprOj6Y1TRr_mJAFCcNKoziSDK-PKr2LD13SgVplbMajXAMtbaxLVKWV_DXotIS6RB-LlPfcjlOKwnTEINf3OtDiOmOJHL1-Xy3s_zOfsDHhChFlUGhVKGXgtnA08Nwt_C0RSt7rA6CjQ10d3GeaMt4o8o60d8JYfG4kXq0Z184U2scOYytgQTw1qLgn7v757ToED7-KgEQJkN044vB9KYT8If0yh4itrsKoMVqyIHicd0eJ3dwahOinpIgWhDzOCvcbPifxMLhw87SiXcGOg2pLquc5cWNlqx2m-lACC4CQs6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید شد...زهرا خواجوی دروازه‌بان تیم ملی بانوان ایران و سابق باشگاه گل گهر با عقد قرارداد تا پایان فصل به‌تیم‌بانوان پرسپولیس پیوست. همچنین زهرا قنبری مهاجم تیم ملی نیز سرخپوش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/26965" target="_blank">📅 21:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26964">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIPqeXDYxBrS0iA2D4u_ZCig_AUO3ewbJI4TP-g-bfd7oB4sWoZxSfjJmxugwaYTuUaiQ5jcT0dB3061yjm0rd-8ReyvZl_eyOH4L3NQvazyQvdVxit60BmLZySaiNToa2JFR_cxM2qFhifuTQ54dSd51IoFWmnDADLGpTsN7-FqAL-Q0A_NAQLIOdTgnA_2ZC_ZqRtmOazeZz4ZujNHgh1AnxlCLHCO9E_sXMH78PoEmz906nRh-Z8Eo_0o8RJDMEpyj281GYJpOMr5SXGerOeeG5e7eonhkltY4to7VI5SAD5pl9EGS8aCHcq3d8ftoNfcutqCx_IkPsftIR1uVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدید
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/26964" target="_blank">📅 21:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26963">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLjGodyE8R1ZiMlBFrsE2Cgq0WtucCb9tGmxlOQsdZR4k3IKSxDsJsGONaHqRZjh3oPxiUecDaPiRiIOyewc0S54240tU1YKCEjfEkD-3F1yDABy76sFu0bo12KfE_GhK1PVyEI8_CeumSHwofUV4CP5gJ94jwfqZAf5s8xahp1WcCC3YY_9fUkz5opJP7C1qTBzf8dYHgwmunuKM6NdjVWuLX-dlpHq6qsbb7Hm5Rm2ntxkYaNa8CLpD02TeL_yFzkvOezJ54Ean-H1-UFouNKTh4-CMd4GvsN1zBE-ZZ8JzcS6dVkDy7lRnM6HuAa8884cpRWf3-x5cwJmcbKlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه 3 بازی دوستانه‌امروز رقابت‌های باشگاهی؛ پیروزی اینترمیلان و دورتموند و شکست چلسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/26963" target="_blank">📅 21:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26962">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbgVO-znr2-E0VqSA4KErGpsdA1hoTm5fmhZLVrJyDGRFiryDkuAvRgSrmVZOkF1AOLlURhacxWzvRTtzZfWIVLFc0vvqPtHpxxllK0doYIgA96BaxY3pUX3oJDmiaB5yyefbFxy0ZpJe3ERMkhM-rofLDDbGHbq7bdFib6YXNbrMI3lGPN4alIbawA2aKRlbbIDtLfU9jY5vt3MFeABq5e4dEukcviDJ-e2KSf5V-i6CptmyTZi1b65yeOWmvvV2bLpID3tDta-J29Y2UbQ8ep5iZ1f66hk9D6-fV0F6E_VF7Tvr8voY3P6FyrcW0Jaiv7cTxdAFy2Sh3iewYUk1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چیواله وکیل ایتالیایی‌باشگاه استقلال: روز دوشنبه یا سه‌شنبه هفته‌آینده دادگاه عالی ورزش رای نهایی‌خود را درباره پرونده‌باشگاه‌استقلال میدهد. ما مستندات رو کامل‌به‌فیفا و CAS ارائه‌کردیم و بسیار امیدوار هستیم که پنجره باشگاه استقلال باز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/26962" target="_blank">📅 21:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26961">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipQ5ITNIWNnV_Uj4I87G2SFjoNbIB41kffpZM8qXPaHxNF6OJF9o0Tgvc2NTvDkjxPxmqCkLup9z5v4zZj35gzy1AuGhAWnh1QQfmvKLHcIOwVLyutmzmwC0rCr9blDK78k0qtgTG00rPACxh8xiD3dxKKre6A3jctprVeOgz6TPztwME-B28K421HeUbLW8Ysl4yFch-2pFLAPGpdvyapebhpzoTd3a_BoeNS63iLvY43OQ4Rgh_iKnrLnw3UQVj3WSRV_C2MJZWE1X91EQbLE8mTjiP7_MKTTUVKoXD4oEOSC0PPIppmvNzlBI6O2xS42CEYl8d483CiI_NR8DiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌ های رسانه پرشیانا؛ مدیریت باشگاه پرسپولیس امروز مذاکرات رسمی خود را با عثمان اندونگ مدافع میانی 26 ساله اخمت گروژنی آغازخواهدکرد. اندونگ سنگالی علاقمند به بازگشت به‌ایران و پیوستن به باشگاه پرسپولیس است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/26961" target="_blank">📅 20:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26960">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOq_1iGhKLHvT5lFEWP3kNvZvlnkMyU99h2e_xui_rJTUYYGWWR_xA_Bre1MJMYdF9Uwzyxj0W4j7Q51yMQGqdLq8UCJqNFARkhKBjtH3DgmAQMapkPhBWL8v2lpwtn1L9Gq9P_PQ_cQXj7PpuVBzkOxTXgGAbqr_GSUXwdtv8KHOrPvckD-7MfvMpPX7jfiweHQXmx_Dh5tB0hECeIRAdoaFQ4sBmKyBnBi9Uhir0_00-t-ZRx7xGitHfOsPDCvqzYxVn_6wXhDGuBOaAUiKf4x8n_r-HYZXl16u4ESf4v1q1P45n3ytqt-D65MWIxvIwGNzu4HEITAKLm2QkAJ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/26960" target="_blank">📅 20:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26959">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
موبایل سامسونگ A26  پنجشنبه 52 میلیون بود و امروز شده 87 میلیون! فقط در عرض 2 روز، 35 میلیون گرون شده!
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/26959" target="_blank">📅 20:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26958">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb2a69728.mp4?token=GLiFGNdzi-ogH9TrFru1o-zv6lBUQaEF1x8QZg5of9iZ611YAp7aDJqBL8ndwg4PYzgzDrQbSkM6FdtkIbPLWabQXEmz921bmzaCgJWGWc6bxRYq05udMv5IrF9d6eiJs7gXTcNlYk5XOgGQcBqpiMoA8TBwYgLJ1nEkyfMnBMdgwSxI3ufTj3fa_W2t0nSC4iR-0xnUH3_b8rKV69wlzU0nGFpvr59dFFkbx1njp334Jw_sGRvLOXM4-nC9D-lJqiCOVf_UmPBS-anPWPJTUkpzUjI9HyczPkxvNKZb0WaK_EDYRjQY0hZy1vOXe7MOdYRqqMcwux_FW2rtNGEKwn9aXXv2mD5UDmd-DxWh1AyEnsAirbLvvwUi18vhL0ilAQw0eELpeyTDF_92wxO-ZuqiLEiwTg7CMLeqQraOIe62_kTClxVwzboAaSCyiq4qznGvHtf_zcaSbI8JKpw8OEa1AbhUg-3BhlH2YH95HWiIPFvCwXfs0-9o9Mp45G8lVr8QAhwctSHEED_dAMoiZgXJT_-f7hJvIT4gRAo-JmvqBiCZsUafOpUB76E-YNoEb-i4ODNgs_wIZmCoP5hG6cmaV53acL943LutbYtIaJ85yXYkhIW6gdK-c-Mx5zytodbToMSad3kNQetbu3iHEKDQVlWjhjIJYxatwQnQtbY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb2a69728.mp4?token=GLiFGNdzi-ogH9TrFru1o-zv6lBUQaEF1x8QZg5of9iZ611YAp7aDJqBL8ndwg4PYzgzDrQbSkM6FdtkIbPLWabQXEmz921bmzaCgJWGWc6bxRYq05udMv5IrF9d6eiJs7gXTcNlYk5XOgGQcBqpiMoA8TBwYgLJ1nEkyfMnBMdgwSxI3ufTj3fa_W2t0nSC4iR-0xnUH3_b8rKV69wlzU0nGFpvr59dFFkbx1njp334Jw_sGRvLOXM4-nC9D-lJqiCOVf_UmPBS-anPWPJTUkpzUjI9HyczPkxvNKZb0WaK_EDYRjQY0hZy1vOXe7MOdYRqqMcwux_FW2rtNGEKwn9aXXv2mD5UDmd-DxWh1AyEnsAirbLvvwUi18vhL0ilAQw0eELpeyTDF_92wxO-ZuqiLEiwTg7CMLeqQraOIe62_kTClxVwzboAaSCyiq4qznGvHtf_zcaSbI8JKpw8OEa1AbhUg-3BhlH2YH95HWiIPFvCwXfs0-9o9Mp45G8lVr8QAhwctSHEED_dAMoiZgXJT_-f7hJvIT4gRAo-JmvqBiCZsUafOpUB76E-YNoEb-i4ODNgs_wIZmCoP5hG6cmaV53acL943LutbYtIaJ85yXYkhIW6gdK-c-Mx5zytodbToMSad3kNQetbu3iHEKDQVlWjhjIJYxatwQnQtbY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
پوستر رسمی باشگاه لخ پوزنان لهستان برای اللهیار صیادمنش مهاجم جدید و 24 ساله این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/26958" target="_blank">📅 20:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26957">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsnaj5aszU3Qv6imQztKtUejr7ZOLkHmVq7Z5zQ1E8n_Nr-z8W9mP3gVnPq2u6wspR1lP0_4ZjE2UGt3wt0aqF6jl0EsnRZjo08UVxrC8U59fBISdE_1SSOHjwNvuzFZOChBFYoQLeC_EiJWFo6CpZAJWq9o3BhvSXkpJ5zFVur_HMtXurq3LDA0GXaFrZS1R32qUkHdEN6lKD7KxEGV-gQG4-AkE0XF5Q8AFn9QRzj_4KALz9pMn_WxplHxWMZkJ61GLJsmXFLhIcPS06a4hXUQAkSQcFpSiZL_h9HaYgdX8r6RICNCum37HQ1ZLPHN_WYzosWOnw-xTYxHbGhEzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/26957" target="_blank">📅 20:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26955">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZfDErY7x4m8eplMUlbzvYbhkuHilawZnr1pGjNkeXpGu0BG_tfPIObaewToDkbNSKIu4m2meL1WUBIlqEKdSxZbAA9kVPqVU1iAclnIsHv9rUF-rrzN8H6WJYfcbH22vJy-U3akdSkmwN3Xr1jp_P_3ik1LSNUa6Kggbwvqt5yhGh1Y9BVwDL72TMUGupN-2JFkMgwoZaLgC2b1VD8bi0CwaQxNYxVfkku2TtrkeOH4rZZEhLkcZfsoyaX4Z162tv8dPXtH_pJ2SOicsdeQBhjlT-DN-lZ9drmSOzR39Jh0k9ZWFq3cSVJR5x3BftuHO6j5LS-wxisYmUIyqy06eNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCnLKJ6dzrNWYcaYIG5q2nYcUiOS46An4ktx-25VYySRf4SlsEZr4yn95uHgnF-GH9k0bXHzFS4l6YCzj9Vx51ogxBVGQws-C-5AAyMB7dS-jTEAH8xKA3W8-HqtJWOo5aguIpreMaCPteAHWWusN0JlVCG_9hayqcBkhygX5HzgY9XZqwINLOBTE_sCoS-T9Hk0HFxTqRBt5sxkgts6_8jPjPQVz8TkqPWlTuLpnZK3hweRHTH_WxJ3xK05Dqs8VCFUsOiHnvdrrYypV3IdVHniCQWfsczFKL0QHfQJhUCA-Tzg2ef-XN3rsQ1zDA_nPDTLVA0uLPu3l5H_RrTC2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📍
برسی تموم اپراتور های اینترنت در ایران. این‌‌ پست‌رو ذخیره‌کن و برای دوستات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/26955" target="_blank">📅 19:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26954">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-dEmR23PYm_wC-hGhFGDTVa3ovmMQKrLTznYxRCjETZL4lauEMyT8W6aePt9yT-TzyzNw6cZYBVaVp4Xs6c6NqHYChjR3es_EdMiuK3wAVstL2rDRJTiUGzPqUUGKh0fJWt_57vmoepiBGqTAjpDrEAA1V0hHYlhmSsBEt1Khn2rh8GqtHD97v8WgGpGMsQDa-UALKnOa30HnWHe7D-KfRoarYFAT_MzR3E6R6qP5Z1ZnnQ9O7bcscuf_adCu_NmXNRw5ARYyxkqK4OmfHqW4lxlePW4XFGloTymMYPSiKEYsPJL7s5M8LWQ-HVquAB43VyfC4NXOKM06PjfI4PFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ ملی‌والیبال‌ آمریکا در نیمه نهایی لیگ ملت‌ ها بابرتری‌سخت و نفسگیر سه بر دو مقابل ژاپن به فینال رقابت‌ها راه پیدا کرد؛ ژاپن بالاخره باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26954" target="_blank">📅 19:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26953">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMD5MdQ7XIuCJrBrlLFagx76psu_i9F7Rap1Z7uRGfyQYyFlfe5MA-ByjX1XjXN5aB12XmAig_sErkNspN9Q59c0UOcHjmzt3ack-96pMYGbuGLhX_IHx7oxSe4kGuUkCMAaJXPm2WMEHaSlp5ZmtxUtTTqtNDH2ogQgSO14VaqoL_2b-XoCgvIT-gg_sA7AsMBv61pvktarRgPTY3R_P-OarJqdrXP99pfz7VCakAnJY0nAP8OJY2FMARPSteaLemcdXPExunSczTUP85GEVTamAifbX8aWIEPE2dpcV7TJh6fYWwe7EKzbJtcgh3safbNLzU08zYuKNEpjBlo4Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مهران احمدی هافبک تهاجمی تیم استقلال به دلیل مصدومیت دیدار هفته اول با مس شهر بابک رو از دست داد. باتوجه به این رقابت های این فصل بسیار فشرده‌تر از فصل قبل برگزار میشه‌. اگه‌دوره‌بدنسازی‌خوب انجام‌نشده‌باشه دهن بازیکنان لیگ‌برتری سرویسه‌. هرسه روز…</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26953" target="_blank">📅 18:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26952">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=M-CX7UuEGKZIkDbWi0-ciAZ0cEJwCkOhr5ME2Hv5NgAOasA7Y6Ru6vkLj5-OhAl6T9QgWT_TpJET8IhXKOuxN2ZaNpyLdHwNGMHwnSEIFE3KxgY0ejJ16TMv0sJ6G5Imnjv4NQVQjq8MNzfQxiQirzUeZxfzeysJyAxUCskYAM228lYQ1ksY6HkuBBNtPIQUFsgZhZ7As0KyZxHU1Z-acqXN0YSbJxhxCsJxI4ew1GXZms20VBt3VajK44KN3SLoGu7FGyqjgZ0EvMEIBBbX6j1htmc_HE1RCN_XnoIKzoi6GdZpL4NRVKnZNNRmemsdCOAAYYyvvyzxii95uotKkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=M-CX7UuEGKZIkDbWi0-ciAZ0cEJwCkOhr5ME2Hv5NgAOasA7Y6Ru6vkLj5-OhAl6T9QgWT_TpJET8IhXKOuxN2ZaNpyLdHwNGMHwnSEIFE3KxgY0ejJ16TMv0sJ6G5Imnjv4NQVQjq8MNzfQxiQirzUeZxfzeysJyAxUCskYAM228lYQ1ksY6HkuBBNtPIQUFsgZhZ7As0KyZxHU1Z-acqXN0YSbJxhxCsJxI4ew1GXZms20VBt3VajK44KN3SLoGu7FGyqjgZ0EvMEIBBbX6j1htmc_HE1RCN_XnoIKzoi6GdZpL4NRVKnZNNRmemsdCOAAYYyvvyzxii95uotKkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌ ملی‌والیبال‌ آمریکا در نیمه نهایی لیگ ملت‌ ها بابرتری‌سخت و نفسگیر سه بر دو مقابل ژاپن به فینال رقابت‌ها راه پیدا کرد؛ ژاپن بالاخره باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26952" target="_blank">📅 18:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26951">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbUwnAscmcO_b8ea0OXyH0-xnoQK-llRi4FmK8yoPeeA0oZdplN2UcBSgqFGEBmgBj1HMuG7irczTukl95DKUoYSIqJORBZe82sQWUYoKjFqgP3rBpzqO_fUREpY04Cm4h_nfpRFUr6tV9KywLqdQvklcNFJLi8lLi-fa6V-srCnBlHpjj-A5gQNckzS4ceyeh_5Qz5VHiLCKkskQEozceeA4071INcHL4KCWAoAB6zpf3OeX5xAw4csOdALbzuYkIde-qbN_tbNgvLSigJ_dAXxPzYvaTPu70Fl3Z4o91QswZNANTC-0o691rqt3P8yOKzWLcLy-ApGKFKXbp7HeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26951" target="_blank">📅 17:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26950">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=ASTE1FasX188jkZiuyTs-F0FK0BsO_cVFKCQQIB2JUIt_tQfVUTPu3Gt47d7Zb3549furKNZtGxGY60m51wBVdhZMb45vWW2In5pVY539PLV8PiSKxyeHSfM7ViCbxwLM4aAmYjfyJd0bULmZHqDwqGd-c0n48ICABV5XpcJKiEfRGxz_zpT5K49NjFIeQlBqp3r0goPyuxPHfg1bfxa-S6MClOcOG-WfV2LOuY7Pt0vIo4zUTW1OLox4LjJzozUJKbq4rbMqZK7rZHC_FVCEhXiii1DNa3NKaFviq5-_ycqvD7DxJspg1BGEhV5htD4HCpBC9v1_-8Ax765pVlMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=ASTE1FasX188jkZiuyTs-F0FK0BsO_cVFKCQQIB2JUIt_tQfVUTPu3Gt47d7Zb3549furKNZtGxGY60m51wBVdhZMb45vWW2In5pVY539PLV8PiSKxyeHSfM7ViCbxwLM4aAmYjfyJd0bULmZHqDwqGd-c0n48ICABV5XpcJKiEfRGxz_zpT5K49NjFIeQlBqp3r0goPyuxPHfg1bfxa-S6MClOcOG-WfV2LOuY7Pt0vIo4zUTW1OLox4LjJzozUJKbq4rbMqZK7rZHC_FVCEhXiii1DNa3NKaFviq5-_ycqvD7DxJspg1BGEhV5htD4HCpBC9v1_-8Ax765pVlMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی بدنی خیره کننده احمدرضا عابدزاده گلر سابق تیم ملی و سرخابی‌ها در سن 60 سالگی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26950" target="_blank">📅 17:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26949">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVNPF5ylIfHw6rRcCHblYkuAx1f4tdqALGOwWz-Pv8SmhtVYmHrggrtcwbx6ag1zMuxZFoYVIL3mvHjH5X9IUDKRNqrqwxrq_GZX_jMeyZUYvfQzmATi2X0F4FtToT09G4D5oDzyKehXww3uV5ogHFU2q77wD_gHMACMXveVaNkAZMKNVFbkdDC_lf6GTghalY2qdVSD_ZWjfJnnHgE1VaNEnelZPD1ggXC324BxqiilGr7dGz_aS_pv4shgdxEZQLAHlmfDyB5hiUpfy6Jc-LBz-3ezjuV3XjostusFuISOYqS-whsTfL9mSysDzopvqaUigoZLCBrpvxVQkFajBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26949" target="_blank">📅 17:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26948">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQNhnn6_P5sCQli5uZytMLWxgVap_1t5pt9xfVrUR2OqV3LhONyrXtZT0WvnaJDEqVLb3EVcAvJ3f2WUd2flwP156YvYyGEDj2x8Wmp41dL_CDscDPx6uP3Cfl2a9lg9xD5487lbNfTyl2fxkja0YEbKKo2neOAhpuQ2f_jyfqRpouQJfIJplZwFApVTnQNeICwM3pVit02yFYtKVqB9N4WysFYI_2-Ew5WnzUF05FA_1EL79toJfGJTkFqFQqnKNVvS1wl9Pq9vbtbgwWGqhG4ZWwe_dll3JOOux86l0dIkk6n37aIlpZtPkPrakRjxvogks4dNzWRJnefRPGgvRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26948" target="_blank">📅 17:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26947">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3XPZChWv2TYjxTnrvlhhZuuRH4m1HTX_CuZw12ZFwobKCO41195qaQDpYSiMFPYt0g2fHwQP-QRvTrZlXfy9kVU7wSajBvMRTqTr-HYGdYY_B8AzITX0JsuQ-EvOYYjy5bYSedcPSe0pr5csG8WOjT8NnxskyIoMkBwN4IRZfbFFW16jzHji-fOQXRTEIh6FU8AtTc9rTH7b1d9lZEwGLyL_AGz0tghN0zxSwAyTXgDL-XqW8cLaZtAqOW2kdu1Xh7r5R3UEkezwCoPdmoejbD1Uc9h_U2n-_3dL7L705pM_NZI6g8nK58CcSzaE4vr4kIcJaaI7Cc_ZiMbBrEN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛ اسپورت: PSG این هفته از فران تورس خریدجدیدخود رونمایی خواهد کرد. تورس به لاپورتا اعلام کرده هیچ علاقه‌ای برای موندن در بارسا نداره و میخواد شاگرد پدر زنش در تیم PSG بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26947" target="_blank">📅 16:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26946">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HytOmBI9-yN24uC31VcJrrFrGH0GQp9D206okleJ2jW8lffkB45ODCMMezOf7bDpRxTbKracbp1yv5oA_NqdyDFQ-GptZDkBGI_AFYbBYSxa2KoS0rC3PWYQUSxlFiB5eGzRq0skqGqm_ThPK0w8GEBB6lXhpGoGO8oTV5ai-yYgk-inhQTD_aVdozwmd-6X8nVP221mEiderNRjDYYrtdTmnjCaldgSUEJS4ifE7dhPqHW3d0PCWiXv4q_Y-iISowIX8-kReKUzCeDBfveXUQiofPiwvIE_r953ri_xz2C0B4A8kBGbDPFiamjh3VUuwI-OdKKUauXkYuKOEyi8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26946" target="_blank">📅 16:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26945">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vev9AcsSR_XTbQoOUH02RttiuAVPsvEikWkpVai-QUIV-4diZEHXMlI82RwofTZfO-5XqcFPZlKuSEstPuNePXfkKhB_6nMPRYM4hVCIKcMLe2vuVqGAeo_n2V3eV3wM__EiieOFm6A8D0LTheZMQ9sm9VMHDuJVqqTj54wgJ0Tm82CHWecbkHBWvmJPXFbFbvuEK5e5rYKwJqgnZXjxDbMp7jur6irm-4PApAZSfKw0h3ns0I9xfvxkrAo6xMOijtIBvVs1-8cAN8lh2uIlPl5v9UooyYolrZ0b1uBPKNGU0IyvYbjYfDmikFZ2inx6PyT9sdP-TmOqXrMKQ5JM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26945" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26944">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSCyDKaxOarI0GZaK4-PJx9Rz-xiuQ4BSqsi9lks1TefYoPqXKimRKuRyYvOcQu__5LAsoJ5jpI1ZKPi3OPr2OUKbCncY0ZvsXvo-GFqlU67-Z1sttEoHANHhwjx_M5swY8IFoiDVGikyfjIHyMdctw2DTjhSPsL6yHNcuuNt1wowTWe42FplNGWEuMxs0FRmV7i8LiHxthOwO8GYWvnjJCaw8NmC-GfQUEAg3ZWVm7qMYwn59mBbfMbI6rJIAN19im7UNFWz24Rj8R47xcnu4lwQhmLFaj_cXtpVMhwJmPm7rPdfBi5WO0Jq-hQP48uUclMtgNcBP3fH5bCvMcydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های‌رسانه پرشیانا؛ فردا جلسه‌ای مهم بین‌مدیران‌دوباشگاه خیبر خرم آباد و استقلال بر سرانتقال‌مهدی‌گودرزی و مسعود محبی برگزار خواهد شد. مدیریت استقلال به این بازیکن اعلام کرده که با ماقرارداد ببندید و تا نیم فصل در تیم خیبر بمونید. قراره فردا تکلیف…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26944" target="_blank">📅 15:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26942">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSbXVg47Al8IkjRVuX64CUtBIT_UmUi1Y6v4lRA3KsdyCvg5LbdPOichGJhVK4G1kwovVb-3TdFV3GKwea0sHMyGJO2hDEVZjSaY_bKj5RUZGYWtki5wzsGhHi9ic85U58arGBuIFguwvQgC27M49W8ckzDg5YrvNlKhApY5N4r1GIGz-h0-MNOECYn1cA3cpjb2nzIwKdDbFSHijcrxc9uYl6hDbY0jM6cPyBa-HePahHbx8dwfmjQAnyxIanbuPO2zxkHyiX3moahfhFN6SXNR9-AL5UtJ20ipHagGtjas6cozYoodkiO4SeZgYYxEcL_57aRHoxejW_YX3j4NYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=F4unTLIl0ln5En4Ekxn0QEBS2iSa8gtcmZ8rHDMtG0gFYAyywVRuk1UGrfxHKUTTvyj5tm55AeG2zNg1J3LThHEREzO2wHPYipzEau-ow-gD7Zzhcn-thE6-n6OcKfRNbRbSDBfm9jcZyYUP4MFK47xYZ7c7puxh4r8nBr-Fc0B8PWeU_WNGkL12qN6O7DfnA9lUAiKJYuPiqOAtZe81S1B2kLAR_VCMiSvhiKX4Y1fOALRjhcBGAaH3O0S91aVAeaDsCdEwSNOCjg-rOjd1ULcjvMwxV_4Kq_sXETX1q0tP3mcpTBYl7Co84XsDzdM5I4QV81inVLfVT9kFI-DWxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=F4unTLIl0ln5En4Ekxn0QEBS2iSa8gtcmZ8rHDMtG0gFYAyywVRuk1UGrfxHKUTTvyj5tm55AeG2zNg1J3LThHEREzO2wHPYipzEau-ow-gD7Zzhcn-thE6-n6OcKfRNbRbSDBfm9jcZyYUP4MFK47xYZ7c7puxh4r8nBr-Fc0B8PWeU_WNGkL12qN6O7DfnA9lUAiKJYuPiqOAtZe81S1B2kLAR_VCMiSvhiKX4Y1fOALRjhcBGAaH3O0S91aVAeaDsCdEwSNOCjg-rOjd1ULcjvMwxV_4Kq_sXETX1q0tP3mcpTBYl7Co84XsDzdM5I4QV81inVLfVT9kFI-DWxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26942" target="_blank">📅 15:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26941">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=qLWzZbkSKUdw4yo-IQv72wWYvFIf-v1kVnmOyKtWpmryMRb1iT-jRSUMHiSAvmd-LXh4969sJYoHL_aILbdYwgJrknai-DL7eiYB-P2CfvZnrOooOZPtl2ciBzKytibs9Bkj-K2LOo3T0UtG51b7c_QSDk8MmlXzaAwBAo9E6POl29MkRt6mrnabQyuRi_vtWUb-cMgfC9FYEsNwV7uzJuMot4yxZ6G_YlK0xXB4aFp0i5bY4Lwt2fnbIgjswxyaOm2H8yhAvcqMj0c1Vji2pFKe8M-iQj4rKRbHKtTLtz4lXkgqKO4pcwFL8afsn1FsLSvB30xkcmClACIwDkwU1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=qLWzZbkSKUdw4yo-IQv72wWYvFIf-v1kVnmOyKtWpmryMRb1iT-jRSUMHiSAvmd-LXh4969sJYoHL_aILbdYwgJrknai-DL7eiYB-P2CfvZnrOooOZPtl2ciBzKytibs9Bkj-K2LOo3T0UtG51b7c_QSDk8MmlXzaAwBAo9E6POl29MkRt6mrnabQyuRi_vtWUb-cMgfC9FYEsNwV7uzJuMot4yxZ6G_YlK0xXB4aFp0i5bY4Lwt2fnbIgjswxyaOm2H8yhAvcqMj0c1Vji2pFKe8M-iQj4rKRbHKtTLtz4lXkgqKO4pcwFL8afsn1FsLSvB30xkcmClACIwDkwU1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپ بسیار سمی که صداسینا پخش کرد اینقدر سطح ریدمان بالا بود که از آرشیوم حذفش کردند.
🔴
از سر راه کنار برید ایرانیا رسیدن...
🔴
علی بیرو توی دروازه یا که نیازمند
🔴
کنارش شجاع و کنعانی میشن پدافند
🔴
تنگه ی هرمز ما تو دستای سعیده
🔴
شوتای قدوس و رامین مثل خیبر شکن…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26941" target="_blank">📅 15:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26939">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5Kye87fZZaI48VlwD6ZHR2zbbQjH0rOZCI4xs549sG7AkwhnHMj7eJcaMOaKruKheYo2VZj_kRIi0SWRTCBFoVbxWEuihDoi7EFHF1TfLfOEuz0iV1781NgptsqYu9eu2jyZL1RNEbTtG9-SBEj007ZzTa-EG3eTGCEHB4nMpR4uKbsYeq4VNYOR_NzHS7GX2On6kg_Sz7_5LvOa4E3WWsWbsOfhFMKKovXFVnqimJRAJudMEq8AO48jRGH-AyB7-9GD1x5nGUenZCYXoRXdNzshYouvX2B4PEN-vdRXeXaY3PGtQWdLK_odKygrtcpQ87b59SFsyezBo7AHfDsZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kojPwKPGswjunlkauR1LyJpQSHY859fod9vDP5utZPb4jsSGEGdPSEf0ylJuFIqkXzet87s17JbV0_vNGzl6beWAkrMYFsaqJf6fXx6hfHhurnBTxxK7Fh1WYJiJWHaEU_eWg6-uV_t2wyh6pwi8K-E2DEUUNqVcrge3CKUBzpOY5b03plUYUg6fO7QXz9pOY1Vx03pBdvtXovTWQxQPGux1fh4ema3x5uvosmUugoE7vkX5vY2p938CkKuDKmFikpvELhFdPJ4Nxb-uaMBYd78aaLHbAStHIUjgBdKiffPnst6tCts1oDETLxzY8W0NQkuwaQRmY_n-iiaKmjSpww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26939" target="_blank">📅 14:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26938">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5mbmXMmvWGHxKi0E1RKzwlktpyCZUVOnHytEF4ToBD3jHUsi-IjCnKvYz3Pi5ysD4xruDieD29fTXKIwKGyJ-NKWBkn9nFtWXGvBs7XchA8alvlV_GihrON545R229R4H8otF7zxBCIt11HakJeXRo-r-D1VgD3m9_GfGufuir81VyZfsAQ7mlY98T8kLkSTtEiQdu0dE5UzjAX15cAy3t1ZyEx_3TRGp-oC4R0xwS5JTzUbulArT8AD2KD94kWuR-MLHg0kS8lFMOnVBqu3xrji4g-XXAxoDMZzWh-Hrr7nn1AYwA_783fW79YALlmLcmmMfFOA4CnizlmU6ReGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
پست معنادار و تامل‌برانگیز رسانه رسمی باشگاه خیبر خرم آباد با استفاده از اعداد تاریخی 18 و 19
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/26938" target="_blank">📅 14:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26937">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=m0wOZXNkusOQ06wI-mqHhdXgqx68Q70Mi_Yf-7ugZXsUbybJWfxyTcWE9hi98D3HkFoYu_KByvMdBb6KxIsSe1T9l2cl8vbOxQ4w-RgNtURB8J_D26ZwM_gVvah_q9HYyzudWcevJqxAf0OVavzr-eJe30LIPVI1Otgla4bjltyuvpckl5SvL_muw7qSBpQIY3YLZk2omByFMHorY859BQTfj-eunK4NjxegF1VFGCbboboVzAvQYdHr8C6BbTCqNzlyBV3zqs6OHNwQG5aINYtx4KPWfqW3pnmBFrZKTyyl9UOckstyrU_krjq07QOsg-BenmqPg_txL0gS8kkozg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=m0wOZXNkusOQ06wI-mqHhdXgqx68Q70Mi_Yf-7ugZXsUbybJWfxyTcWE9hi98D3HkFoYu_KByvMdBb6KxIsSe1T9l2cl8vbOxQ4w-RgNtURB8J_D26ZwM_gVvah_q9HYyzudWcevJqxAf0OVavzr-eJe30LIPVI1Otgla4bjltyuvpckl5SvL_muw7qSBpQIY3YLZk2omByFMHorY859BQTfj-eunK4NjxegF1VFGCbboboVzAvQYdHr8C6BbTCqNzlyBV3zqs6OHNwQG5aINYtx4KPWfqW3pnmBFrZKTyyl9UOckstyrU_krjq07QOsg-BenmqPg_txL0gS8kkozg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خیلیامیپرسن‌دارایی محمدرضا زنوزی چقدره که هرچی خرج میکنه تموم نمیشه. این ویدیو رو ببینید متوجه میشید. امکان کز خوردن پشماتونم هست.
‼️
طبق‌گفته‌خطیبی؛ زنوزی قبل از تراکتور خواسته بود استقلال رو بخره که سلطانی‌فر بهش نداده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/26937" target="_blank">📅 14:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26936">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eezm3_wEa5GiZ-Uosk4dh8Ymk-tN4y2sAOhlVpe6Kyo6hs-byj9DyeFjPA8CeW9lqbC1emk2W0uTktiox5AQlvQgPj0kpB4O9_9g5O24tVB51pDFRrZP9NukewHzQk-DmCC4eEcRAtfKIMOpFq2CYATvwkPVslz9s_6p2bUtZrLJf3kQZFFJpdsyA3iWK9C9g1-ngfzFUhSstI8VuBCWAy03qJTDWHmcbewgUOsYxvPy5jvVyBN0aXxK-LvAvyOt9z3yr4Gd0rkEkTq8-damWQghTI82eBEAUxBWijb9udrc1FLcIeKeZB_QxYM35maLnnHIT9FGFbVu381DiL2Gyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/26936" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26935">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYgq0drOC_FPZJudLX6tn36gsb5_-G0t5uCaog-BbzngD2_XI2Nwm7m-LaHhe8B4B7vKZCZjVWWkaW_4IRH-4VQy6rzSuusccKx_3DH_3ExHCUChiLHQ3nYb_Pm3ARAEsNTB6TWNbKJnh98jqv1wc4GX0IB42-bhc_xbRh6P-poe0TNb_qh2u0lEvGEa4VV_0A5XOHcbbiJBo92oMrIY4ZvOvqYzEJlTFAFTVOIfi1_9MASysw4oM2M7Yx-lGLq1CHxLRJ5kRJcjFjST05GxTmvQLyTkAebQRiWpe7jhsKmATvc9B5202tLnh3uV44_1aEhlGL0CRD8rX2eeprxWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26935" target="_blank">📅 13:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26934">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0a57Uya4TlkNos1NqnnG8B4RzA68Wy-hYRMk68jgtwVhd-2ggs9CN7EKBC41UbDrKVsHK_hkeW6SF82lc6MFzM0V91Gd3QXdV8ljhMaMfz1tuXrMfl19UQe_GObNzxR6ZmG_CAhp6DkcwO34e102bBkjvSHmdyXne2SBeJ-mxJQtmXSChDNuPhUnVKpaVyLk2ZszdXPFyZqX8ROVRWEf6BKHslaEo0vtopoi8oHXE1HfZDZvxnZMuCIf4A7uTUwiENnhl_1XmaeRdr8R8kQwPNE7gnOeQOoe-70KRDcJkFa-UlMWUNMe61__EgOQR4OgyR1b4VHdMg24_tZLllmYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/persiana_Soccer/26934" target="_blank">📅 13:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26933">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5gxYw8DFPf-pLB3RwsV6zCQB6qLhgEKgAbmcGjg_go-7jW6SFs7qZf7T0_spHQci6UvEY5VlfOxwB_yzOCAoTcBVAMQf7wl8MbDoInOcuM4tN2VzgnyED2_OaHZ1wDBpqzNHca5feUi2ACw_qal2lC8LTVvvuDfNkw5EWf_Ira7jTWllFrjn9mv30eXvUBXCHaW-fwPEsSJVLp1DAOrkPPwNtN9N4eJje8TpZlXTSIN4jtZ4ge7GvgYsKPliT0J7wd5dZvqgVrdCQ5Srb4kS6mSZ6kXu1FnD6V_dFTEJhbjXFKhU2JAMv3FCTk3Sm2yuKRJgTd2-taARYN69mbRkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/persiana_Soccer/26933" target="_blank">📅 13:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26932">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rq_nTPtigzcTF_Bi5BBoJmb5YAxWL2oxitJmcvbO8uKOnqkj_ArYicPox6wdmeOVOkq2c3SUXZw4uEPqgG5wD8kMF8KWCz9P7pUa3Hin9wxSkig12D0oHSoWPq_a_M1NRENgS4INfMWRrLmKQM2U-XX7i3bheztSHv1j6v2XK8sQ58xQync4GDYBicYcWIGTqg5TDgV6YB_NezUXgcWX0ladpoFoi4U5jofXriB2ApMtHSqSuSrnSMBFh7-5XNG2oIFEI2qFNDBjUE-2pYWgnMgdb7eAacULc7AjcD9AXlzXaxcw3fnQaVgimHZlPqT0DiZnJ34EFY2y57TNJjmJOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره 22 ساله تیم ماخاچ قلعه روسیه پیشنهاد تراکتور رو در رورهای اخیر رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/persiana_Soccer/26932" target="_blank">📅 12:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26931">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcHQeIfzsaOA4DvJ5B1u4jFbcBzezLahXc8BsAImFHIvbFufNN1A7fMEqMXb5lz14P8nEm7p9yxvLza96DKegLhncBIEzxmPETNj16A_n6eO9b_NcximpyDl7du659B2-WmjJZdoqWCQ7WeWox9Er_ymy4MzAZeeh4b2QiQQHRBYQLhKJ2V7Ro6bICBVwHJWJkljY67znirQd3rd-KXA407uunrYogSU4i7mixxHvuLx4N5iu2Iwy40qA3hTUXM-UKlBZbWG7O6s23S97pyUE2BSnOJwOdVw0LAC2mcMp5ND5hc2NamA2YdYvPHxUgS7mdMzsZO-M5JcZ6TN9cbghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
نشریهESPN:فلورنتینو پرز قصدداره درآمد باشگاه رئال مادرید در این پنجره رو به 400 میلیون یورو برسونه. تا حالا 200 میلیون یورو بابت فروش بازیکنان‌آکادمی درآمد داشته و به‌سران آرسنال گفته اگه‌وینیسیوس‌جونیور رو میخوایدباید 200 میلیون یورو هزینه کنید. اگه توپچی…</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/persiana_Soccer/26931" target="_blank">📅 12:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26929">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cupPuKfqFkJNNGTPDruIv9JkNCa3Plg199XF9_ukvZVsHsR94p8Uwra-p_j8j81RCDhdQi3G46BnUvzeLJ8wUojBmwTiVdS618XuvnATy0MY6FBkPqbv4M9CbLO5kUlQwmMPkhZOfnKpqDnvz4GNuO2y-2tzKnRBS9nIkSR91YgbB-MGImq6L3XyHSg-77B3URjyR_4kx1fBtMp_vUqcBKweDuUmTXYTmn41vg9MpBbLS_emG-tAyftiT9geEICwCjafmV7ycChuqYpsKNyaj1wONLzUbjOvQXej-1WgU-AdcuFx-Y2TT8D3iULPyV7AyK8bvgBG84alKzqZdMwMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFcKyEByPvrUGAXrqyA-f2Hhg9dFyC8lVTVv2Sv9UbJ3JgnFaTooHZdRkjLI6d5zRabv0AP0HAUQJydoaUdfb7ztBXBAabPgsC8bOVy-Uqi4osxsEHXmGNQmiW8DGML3Mf87Ms2UjTzheDbIyTaFpdxI1MraYw-K1iwCaWLHXAcnEigId1aqFLq2eJbZNDvJaoW3ReBLKu67UNNO8rg2RU_Q_AE-fhCQw5s2pl8M81HIHXKwZ_ySrG_L8BslKD3G0GrQk0GfAGrR2Xm3WVejjn4aVVP7FosxAfQa0vLDsCnZ4so_Ts0xhSBucb9f06nqmoGxKlfW6wGcmdt1o_edGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لیست کامل ورودی‌وخروجی‌های دو تیم رئال مادرید و بارسلونا دراین پنجره تا به امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/26929" target="_blank">📅 12:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26928">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0eEmL5r0qCN8Ne4WHQGj8utcTq19IyqEJqUX4E5pxcC4dqh7bOGGdHkd_4nGTlf9JVq9W2QjBDT-AknBtn7Wrs7TKSgKbxGSulXvh26X9oHbw_X60q_8yC04oK_PA-PM8NOjQypyluTYCQ9m2GOWEbMyLYgAkYCA0egTmx1Jh-Dh12S4wrgNrFcGBUAevT1A9DhNGgGk-6bGA2Eti7JlBHZWwEagEiwbqaavKqNNtuFAH4Uslu5JVyDvqtlwdRY25JdleSMi7eLnmJmD_GpD80MVFY_ZRxUlRFoTmbSMMeCso-uOkWsm3CiUQjAS_VnR9kLfiHanpfH_LVEbfPLxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26928" target="_blank">📅 11:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26927">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26927" target="_blank">📅 11:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26926">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U620xkxK98PnOB0J6PXDHbjdBwE7skXRJeeWcEzl82KxAOiXbi8T3g18Y66wPetkMNsa0WgHTmHdzvzPSIjZX4tR8ZXjHGL4TP2g2fF-2VWJlFJ0eDQHdKqCNHDlkprSa9Au3RdRVMuZYewL6TgYsJsSUg7t9qb9yHgeMzJ5JogL9gIdZFSBttl7GR_N4OXgDBVvKkEZD84UY3Qzz5AFmdx5rVFwEe1XS6IxFF3XTsjUPlIWw_UvaXOfY0_4B43jRxrNIGxHqnJFz5ZZvqWDjniLI4RVhYfRAWNbJhtzBWhsFOQk-4VBjLtpViEbQjJFCWSWB7pdczBVf3Jb5WrTVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
زندگی رو لامین یامال 19 ساله میکنه که تو این‌سن جام جهانی برده، تو تیم بارسلونا بازی میکنه، حقوق بالا داره و صبح تا شب با دوست دخترشه نه جوون بدبخت ایرانی که از بعد هجده سالگی باید به فکر سربازی و کار و قسط و کوفت و زهرمار باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26926" target="_blank">📅 11:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26925">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIeqjoGiiFEnmJWtXrp0KbBmMTGNcClGTzlvKskxvERDEaaF37u-q-4kBYTy9IZkWl-06YMM5CcCi-pKll2F4w-aFcrjt1DIj3B13oJEdOcaL4yZp3i9gQFfbevjbHK-VgU0w4D2Ls7i16tUyxrevz1dRUAmrw6IklfTO1L5g7k4arr4zQjpUcz2Clj7BdfjNIoumHQIzZIupkPIlYuY-2bxPm8LeSYzUvdKf77ghmitd2t0KYEwc4aWbQuGFTnGGn07dGzLnlejdH3H2xCB0LogqZRjwHGubLGqN16KtGM6E7xJIoMcGya-XqsTnZ-Fzc5If64bz0pwntVZZ2tQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛
با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26925" target="_blank">📅 11:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26924">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEvWIc3lWZkVj49QDVIn1MxBHbtamWfaRWsFQdOrm4Pt86HKhkaOOkCgb_Llf5LLqDWpsN9ohJcI1hvialhFoaU7xELB2RLB3NOspS1MccV6OW1pjqAamjcPaI7EG8wBEmia2eBS9F_Ec4R7tsv9oQhb8ISl8dRmZCNN7rcrO1RCSfMwAshR1sC0yG3XDKZtGl8klud8_cr1XcTJVGrDeuy26fdvI26mihQiTaZyEMpAHCkwS4USHmOS0eXKskv05HgGsxOcSgoyuWisR3zNVksNEmpfSZ2I-Yom9UUvr5ZVrqy_q5KEQE_OyoET2ILJ2NDLLc41N7y-bIVKNRiKqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26924" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26923">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRByRPiYCPE68GiKq2CrPHMV74O8QK-QmW-4oPcm1n845h0Dqma7xIuW7m8xhrMSsHiyn6bC39qrZmmTr-tVZWYdnQTXHZ_8nLHuTdsBLfT1CH36XTftIQjcUdFmrUvjXngLhWLwsNfoX7jaAsBBQjSWken64bX8LtM4oNdXp5VyfV0_CYN0DTZQ-jCnw5dfpmfNx5C6IGuobLna_mVArOoT-1j7dpfyHTXSV-uqatGQXMl0dZwtfFltPEZbWWJ71Fm48aYeiOGkCbaEVzY3AdS6jWwbgygbwZh5WGLWmGosszvHHMFoCSvdfv9PUfbp4pvcFn83_F81rKv5dDg3M_NMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRByRPiYCPE68GiKq2CrPHMV74O8QK-QmW-4oPcm1n845h0Dqma7xIuW7m8xhrMSsHiyn6bC39qrZmmTr-tVZWYdnQTXHZ_8nLHuTdsBLfT1CH36XTftIQjcUdFmrUvjXngLhWLwsNfoX7jaAsBBQjSWken64bX8LtM4oNdXp5VyfV0_CYN0DTZQ-jCnw5dfpmfNx5C6IGuobLna_mVArOoT-1j7dpfyHTXSV-uqatGQXMl0dZwtfFltPEZbWWJ71Fm48aYeiOGkCbaEVzY3AdS6jWwbgygbwZh5WGLWmGosszvHHMFoCSvdfv9PUfbp4pvcFn83_F81rKv5dDg3M_NMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
چند تا از شوت های روبرتو کارلوس رو ببینید، زمانی که فوتبال از کسب و کار و پول دور بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26923" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26922">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ja3SMauFUpFAw7hPyiHz2Cpmu9H4dCvmsxnea7-GRCFnw3oGxKmfk8XJVP5ckWuY4wk3_d4iSsTq5miEZDbew3IrGOp6FH0nZe34ezQOf7JmwWcU_oGLd8elgSWrEivjbY4shLSU20nY1ZrFs4iqKWOOSyTzKIzCRMSxx4KdkuiMBOMTtouYE2f62I-aWgmQ3GuHrWcr-DUhzxM9jjujDt6B9YlBKXjnEVDgQYvLmzVNF69EJq9zQeMh2VfuaBFXrC1BvyNb1phJ1JS2OGGqLZghkZM77Ugiw0WVMKaBIf1y7FjbWq_esvnSdkjcrZY048Nlbg2obprneAlCwm-smQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26922" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26921">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EM1dyE_y1egN25fxHERYoeDPy0Us2WUEFvcGY3gnd1Ly0DW7UjDUgZ2p10YxlrbuX7VJ3Og_MeB3XQzABApnvKGX5U7C5P7Ouku-FNgWf9SAc-ACrSq4Ssxsxg574SPlFweWGzpdiL5gm9c8VjHyGXagJbAb6OGkKjMnsleQplwVXqk5js755QEk6QyEcIoz4e0sls60AkYZFU805EeOcmnU5P9j_OtWxeRwnnMozRVxaNeLP65FIUkXwY2Sohp2C2zS7jtDk5YR66jwaTK7At_3M1Cvsl7fPIzrdjdkgQzOmKOpBtuaowNYXGsFZT9blcFHkei-YQu7SK--63inlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیس یایسله سرمربی 38 ساله الاهلی‌که فصل گذشته این‌تیم به‌دومین قهرمانی آسیایی خود رساند باعقد قراردادی چهار ساله به تیم نیوکاسل پیوست.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26921" target="_blank">📅 10:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26920">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_Zpg8pOV5TqamFwASssBaZddOD6FZi6KzghcTclNIPPCm4NTA8Xbpr_x_Qi25Q5j1nypx9MNrI1GXKTfhqJ7bP_aUdZIrA5w34kh6wH0YWOh-82NuT35RL3AUU-41WO6c9AYPGIL0HJvDaizCu7QBweOT-PlpkkBh3XWV92xr0ItDiA846nkOMjbh1dwDV_0l7CRWICI59f2wzlkeTSU7Sm8p9yHyYU1EOkfsmsi-eGmVCRDjdSne5Nugde9ccScmtg84JJ7TznB0K2lXg3olyJ7lXLlGunEw_eiQyqAJF-6iqIlyfgNuHAbN5vJ9S8r4nhyIFwg6khFAhjTYZ4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26920" target="_blank">📅 09:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26918">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zgu25g1-ecNCwjsuYrEp3htU_F9w_MZ1RC86BvYfJ4fsVXDxDbyJ57rtlX_jQZVrbWFig4CXUGNAIIXIQYal79tYdKSYLIlJ31v8lznlczuEIfzO4s94yAgkLkJhZ7tEEmpEpliLXnVFp_e0V_oYSPspgzVctBDr68u5UqOlFh1zGcBmr2pOXQ1vSuAPH6Elw5QKpXw8DK9ASvvzQYIZyGIgNpTK3sXopQZwjAjFg4gugHpty1wOOZNXhv23DmQsGphnl-8fvdaNBEvcK46HRpWbMhODTtDsB0tJIkZdmWgMtpyI7HX7uhTQiFekBLqmt72oFWUqGBN0VR6bYnyQ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
رسانه‌های‌یونانی: تصمیم‌باشگاه المپیاکوس برای فروش مهدی طارمی قطعیه. سران المپیاکوس برای فروش مهاجم 34 ساله خود رقمی بین 1 الی 1.5 میلیون یورو تقاضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/26918" target="_blank">📅 09:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26917">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrOCSKCUq5AwRswTPzHaLW9TfISO1e1JekS3JLEnLUqFYaqlNKnU3qrTCV3Mky9wCHWCBUI-j4cdO2RzJ127XvrTvsiT27wiFBOdpAu-iDn0oJ8OgrXPk-c69MsILzBL0Ax5uqQcW4YJo2HODary93lEoxI0g0EjhOWG1sRW6DvCplpTRt7QvDhPYu7ObtxWlLAq6b4Cc0957Z3rZ9P29evclREt_BaGiT8tKcWVjwM0qLP0jD2p2cu13z1o3IfMFsjQ1zgTp73hN4OebmM7stE6MxS_rQ87QDc1XZ-IdKOuj0Ep3mxwOVAhV4U0FI-lXPblaxvIEwxUdLdU2beLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شامیل گازیزوف مدیرعامل‌باشگاه دینامو ماخاچ‌ قلعه در گفت‌وگو با RB Sport: سه پیشنهاد خارجی برای حسین نژاد به‌دست ما رسیده اما ارقام پیشنهاد شده کمتر از رقم مدنظر باشگاه ماست. سیاست تیم ماخاچ قلعه فروش این‌ستاره‌جوان با بالاترین رقمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26917" target="_blank">📅 01:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26915">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWzfaC1z51Cf5qM4mGQZGjeUgzkeNkOWBsgumtiSNyfTprMD9kOFithwvrx9e1kKmYEFsb1B3ebDG8GXEbi1EMTS1Vsu3zcqhLwAAWDtP9cYeSay4IUKQoi2JjTFeSQ-Aehb3LWs-PNhZfNSrnI6r_IHcM9KWEE-6Lsej0aXZVoyhXmuXoSJ3vlj4PF4ZtVvByJieEywq_uOu0OPguuwJ-_ODuhpMQ9wA_XrKJWQG5zdbpO_64VGXF6KZqT4rb7I9F1c2Xvp4Cbf90C7khe2OOXqPiX08Ff_EKhq9Eciv_9isDqphWzY6K367bIMUORat7s-Q55xQexVKxp687Bd2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26915" target="_blank">📅 01:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26914">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqRfaHRe11c8832Gy1HdgvsIkR9cgsB5q4N_7MZM0qLtZ21KlwnNkhYFgh2o_CzTQNo0D4hVbJ1w8YGtiXhiBhAkCEnob-Sv5FjMDLHCIWRnvSSfu0sog6XMHebBUFjWDmvne0aUJMops8v7lOH-gF06yRNmHVl8HOQf0SwvlQvgoP42CzeCz5ih3Av_-fOr4jqWRbFmjLz0lRE58bfqBohO4TItocW0CbKh1uZZQshVYlUqSPd-2zy2eefZHZYYyMcnMHlFErKUb85_Fsm3nk6ooafvsgU99UUPQNT8yJv5s75KyAn6Au3Ey-Y-C-hbOXd-hJhfZmDdksPa9Y0A9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
بردشاگردان اسپالتی مقابل تیم فرانسوی و شکست کاتالان‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26914" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26913">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxY6jLyyOL_pfKvhlF2KYy1AA40VBmc5N-0GlZv2RvFDfiD4M9AtvRw-pZpcbVj-XSzdGmR8fzYHHvg3Vw2lAbySNA9jkN3bUKL0XHNirE9XmLMcF9SovOge3oy494vQ-cjosB8F7u2xSNognuoTw4uwc6aAMlkGfgxbivgjQrKTReKZlcEPyinzXzWyrTBpPbqElP-B578WKexZYramOEFN4AJJWOLnhT6vHbBgBaDhB1sV_pWGJhxhmIu_M-W1XREnHINIxdllpqEltmufkCx9mvK9WYk6rPchuIUgSfW7NaSp6uxD2fGrMpHTsVa6LC8IOcSCwk36AIhHStiKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه آمریکا و اسرائیل در حال برنامه‌ریزی برای اجرای یکی از شدیدترین حملات هوایی تاکنون علیه زیر ساخت‌ های بخش انرژی ایران هستند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26913" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26912">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nnw6bstDLjfO5VyvpB0hnW9dPtSZnmdqIzPRBv5TxIAbmT__5CQmC0i9qEopH3qkovtnpFEumzTkoAHnOGl50s8iCGZs-1Zbl3GNlykjAe5l5Oz_8rGWnhdjBfWvg0RHFrJdr8YW292JMp_QQG19Wsgv3MpRRYujC7zQo7Z3j8Ju4BG6VehnMBFX99Km9G1sMyoqqv_MxGHf7Dap3ux46vPuBK9hjHBiMfivgtezW23EeWvqnfSFFkjCim2sssesb58h4_SuPf3LOBHNrrlXQdZKeJMsXaNjduPKfc9r5AFGYEqOsVt7C6jYckEkjzijgXC8WzqU_xQvdLBFfoIc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
رسانه‌های مراکشی: منیر الحدادی ستاره سابق بارسلونا پیشنهاد باشگاه الاتحاد طنجه مراکش رو به دلیل پایین‌ بودن رقم‌‌قرارداد رد کرد. باشگاه استقلال به‌منیر گفته‌برگرد سالی 1.5 میلیون دلار بهت میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26912" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26911">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJH0ufs-zIGBxgGnhz-roMyW99V8NTDgCQYTClK_nDl9tRT2LChR3dtqJgrwn8soQMNvohFdStvDK6MC7oIh9XBCHeysTywLqEEsLIlnDb9YR3uMsjSiFx1YVEg0fBkFkOdkrjathLeXyJGQbKZdDkMfjNBJ6qXjI7z9loeX6xgl2LPVBf-yRC29Dw3x1H5cjgLgMBfmN0mXk2JO9U_RxlszYFXZpU3YOxzvNaNzjnmL8MxGngIaQVc9HggRbpshvFQFVyMIVAFChbooRg6xh54ys6Kn53FwwT4l8DaGUYxlCVrPNZyYilTMyGf23VmNPzs6pBdfW8tSGTqSC-YBYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛رئال‌مادرید بابت‌فروش‌بازیکنان آکادمیش درشش‌فصل‌اخیر 440 میلیون‌یورو درآمد داشته. تو همین پنجره هم 196 میلیون یورو درآمد داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26911" target="_blank">📅 00:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26910">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDx_Zpevxb_8Bv0V4ASR_ZzADf-5v7GdRZ_2QBvjecruRdkjsJ2onDDxyIleT5IdYGwnZVaJVed6OuBcIRJavyqXY8OhI3T3ceJbHStY7klYU4MflKRzBLSzpJiOhyxXFOGtb28Wl7zVuepbbb6YBR47k1j4m-E4Y3XGmwfoOZ0BuNd0Yi-pSJqTQ1iQgph4VT2EX4LtEmljaQuSOX8KBGDSCNg6GYktmVLrZuTigVQDCgthW6QdlWbjjQEPVf-9K027_mkZqluTu_l0nyeGT6lvNjkFQII-MoDB5pQSFgnvmahJIKyzHqyaSkGTFTAhooPeHr26GXYGRWvvssbDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26910" target="_blank">📅 00:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26909">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEUuvoJ1Fdup5--MeaLoqZaYzxQJc0Bpyz5wc3Duu4tc0RUJDIF8KLRxmiRpJnIKpXXf3G-futK7cRyaHYh0V1LTmdMtxOeZzMZiIIVkUXjTmKJHLr85UR6H8cNoKGe_vGzQxS4sDQC-A5769yODlKpnTPVL1DC3gb6mM6B2GkO42mrOpb88MqHVlJdcVIKWsxdS63aYYbR9obcEdNpaGzsejdnzVcXN1XtQRKxolSkv9w3gOw_ffpllJY15R3snmyRZO3BiKCxPkxZb01YT-_P6xwQ5YlWg4knnvKcqqiPzLxCPAJi_V6JAb66SVVRXp2PxHBzCuLZj6StF5K16MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26909" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26908">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0s1tkeCDAbK-m2UnwkwVzlKGraclPm2xmy4XQ_AWF4eLP_U_YIXCvk0MFt5L1tyEymkDXiNXrqwb0khXrW2697V9QBCIXzK_dex0t4xEhmTgvPXmBjNeNkwqXVHgmJEIpLoxURi9Y52w9KMcEot0q2jHzk79CxFW0aFi6OnjLwBsdUu44rtCBLw65lax0g8E0suzPqRuFsHhQniS5ovHPUqwzDdJigRf9TOKyDv1NGyemjbSE3Y0AJm2vznErOO666otUjUukfINTLcanHMjcRz-QQn5-5d8toZ0BtWWoPMiCeTmjphDtrKPPpg_ZjGYoHmlc_4l5PszH5Izocdpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26908" target="_blank">📅 23:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26907">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daU-qXFrh3f2NCrCsXIKUGPDbE0kD2c0eSzV-a-d3RLjdTnwGxiaHEhH0MoV2ODubY4J6Snpz4fuo1Q6WXbNm4dOoMk3az7RfQgen74BzQBv2OveQbtQlsPU5LtUmur63km7i9vqOQPaJjnrQb-WhBoM1eNaEDqB8W-_q3f9cpt_xC3fqfrJeZhHA6J3lDdt7Vz80wPzFE-1qfxq920a22S3tmm2GMmzzLT7oQAx7IEvL9EFndB3TdRxU0DYFSqoNJa7IJjagcimRMw9Aj2tP7nKJLSMDYMexfpM1g3VS1Ux78TObv53urZFu1bJf-prevwyWWqm4f0i_9ap-8aEAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26907" target="_blank">📅 23:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26906">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇪🇸
خب گویا سرخیو راموس اسطوره رئال مادرید هم‌تحت‌تاثیراستوری‌های‌رامین‌رضاییان قرار گرفته و دویدن تو خیابان‌های شهر مادرید رو شروع کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26906" target="_blank">📅 22:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26904">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzaSgXURvHXPryyZOZiUtuAY3kL48yxZXGxVCOubklz1IaQTD9Pg-C_wQkv6sTlBVbyOm7k2mRmPJQI3fwdtBrlNIxDDYBPJuDRIivn5MSqeJlyOENbEiQDuQWVhMl1scE9aYzKxLIxyiPBiqS1DQu6TVY7w4bFLMAdRDZU3U_F_VHVSyl3v7zv_KHTkKFRqvUIgpmd8XYhukL6KxhbZQccavrJ3iK4qlY8j6E9zKigfYGIXa3hYyJxuWNUY166GQBp9qPqvxAhCckLdPXMpYOodbxN3Iibl6dxCKF663lxlMGbxmO9iBM2MVN_rHCKEXBJ5WgbsV5APJ0FynSEF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26904" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26903">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfRkv556BP4MEDFfQWbyqQ8JYOykD8aAzbc5Q-ldH0HvKbY13IF6tJ93sBN-qf9O3Twzwh_l0H0uu1vliq_cwX0Ihq2e_ndJZjs4-iMy8DwFp5hZL9S9tU3pyTjyz3CfrI1esW9Hvj29qhJxlumOUW2c2Ij0jqFZBBsxacyGM6HWeu8UqZ0ozVFfP9HgYNQkIZjmAJ-PoMT1rtBG3N1VztWKYLLDi30j2okzRJjcrOm2nxMGIJlF9SYE96cl74pE8EBMZEk8l_xKJUKF36eUnExKjTtxEfdX5lyR1j33A7LUoZREq0SFMndBl5tUgHmZhaswGVTHUmFaLQUA66dNFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شش‌خرید قطعی تیم رئال مادرید در نقل و اتتقالات تابستونی؛ به این لیست رودری و الساندرو باستونی هم اضافه کنید که در نهایی شدن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26903" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26901">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX2oi_fn8YNwARtm4ZQ5v2weA9atlbsDmwgtL9MTRqDvNPFsIGaFzQr7uc-qhOGoSnCH_ubljigLluPHzVh_DQBGPZxYFjnQgrLiFWvFd_q_FekTNZJ3Idvc9XTuEO2GTJuU1hR7d-G8LZDhoLz5gWEQd49niqmlVZ6toyfYdFsSAKnIjTbBIPxvljdImkjmcGOTyM-PzFuxZNedNSf8efXw_N3hmFYAHtp-2ji-cvL8c_jFkAKxh6KYd4-HEaumLgWe6rqN1ofLvlPZ8dHsl9Nb5G9W7uHYyAIzA-QWTbuQI6h-uy6hp37eQDNNsNyzbC3SupsyoO9c0buKz84Vmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26901" target="_blank">📅 22:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26900">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3IzyKTX9xyA77_CEt6xFwGTzUGXCx_yul7RHAdPlZS6rjLC6zvTySoElimeSgflawWJVZVfywQcCfaqy9mhAFkmvRZUjygOFmcmgbBK1obnFL518cp98wvdTDiDmJTepNY-Xv8moXbT0eDrS8xP83Hlcd-AS-xSvPEbqc7JfBrMQlNdE2TbqxWQKiJiRZx4cDyE_P6WhY_ZplXr9boCkixMOCxwQjsHnoW4RMpaLPq3UHFjnDn629vYvjXwuoADUR9DcpG1Ou9zRg-fF0G69yOxkuy5aEuGJcTNqqP_rO6ujignRYB98hpauuiZHFRxluy04NBov4wCK9iTUKDiyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفامیشود با بازیکنی که 6 ماه از قراردادش‌باقی‌مانده‌مذاکره‌کرد و حتی قرار داد بست مثل‌ همون‌‌قضیه یاسر آسانی با این تفاوت که در حال‌ حاضر پنجره استقلال‌ بسته و مدیریت آبی‌ها میتونه الان‌ باهاش‌ قرارداد ببنده و تا نیم‌فصل در همون تیم فعلیش بمونه و زمستون به عنوان بازیکن آزاد جذب بشه و نیازی هم به پرداخت رضایت نامه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26900" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26899">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFDRKgLsnWDD2c8NsuTNttjjfei4dZyx7OnMUcb2H_7B_bDEzEAFiZNJ3Y-qr6yb5M-xJn62KM79l89BQWb6_ZXFxOEcZwQ-a_AoE_m11Dfg5Si-B-6OZhGjkIJ3i3LkiRhYJIrQ7ds0KNjZezoSdGMMySz9uRDUushYaDrVHjn0zLXo_Yu0Gl9LP90EkspifEQt7hAQA3quyVDntjCI-NqKBO5QsiLKG7_VB6yGWQHTcsrBvWwOOi-6YjysO9zOYAlJ0nKeSo_kpXAkpxk9ie9Ei6TugLtKyTt5hI-E29VJ_qfb9LspTcqs-aF71fByRPkBxlVpTjAPAcsz3j6E1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
براساس‌اطلاعات‌ترانسفرمارکت؛ تنها 6 ماه از قرار داد فابیو آبرئو مهاجم‌ آنگولایی بیجینگ گوان چین باقی‌مانده و طبق قانون فیفا میتوان با این بازیکن مذاکره و قرارداد بست. در فصلی که گذشت بااختلاف‌آقای‌گل سوپرلیگ چین شد هر باشگاهی بتونه بگیرتش ضرر نکرده است.…</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/26899" target="_blank">📅 21:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26898">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMPKgBYpC_JJzPOovAMHq8VY_ObsZ_k2CKBk0YWioLMtcfphGXxEvgReEJml_Zq3nS8TO2s2D2ennu70Qv3Xky6Ne_FOWLb4U2_NcqhQ-5InWcJ81vOtcpj4XDD96TH-Ko1L6R0boMFmUlPAID9FRgf8j-ge-lbtBsOPLOVcADB7vLIcJzP3NWe8QOIlBgSLEnyrqZhOfXtYrUeUvb0BYmlXazbwKqHAiNXdMgAIop0yqjdjbD8EhYElsxTC6pTOU9Ae9IfAns7Q3tqJskCBOvsTAfkSCVBapGFVnIiMwQ0AtxgZtY3eyoVgrcOERv8_KqJdP51jfzLxTMjmV8uQ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26898" target="_blank">📅 20:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26897">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ovjz_qiznazx-xucGWUEYzMMqbO8dA_6jo41iRBSGCdsKqlRKfOxHWA_AZRePpezItY0o_0wgVY2vMTR_mGhufRDZaGeYrUR6dvodce5PgKyRn46BKWun6Uq7M0lGrFpToGB4f5jm76Qq9SS529RUH_8BFMPwoP-YLkqWMpm8GXZKxw6GS4LgSSgtnOjJvlpHDemapS_YF8gXLeJltSe_nPm_HUnbOodacmUOc8ZDTq_ZtE_TRsQtKyGlPG-6WJEAKJo7pQ4C3NSSTM_1r6WWAmp2lLes6iDjo6TKAKvriqPuLlolpFaxSOE8Fg3C2_ocSdvizqDawFf8vwXfEelnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26897" target="_blank">📅 20:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26896">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92aea27557.mp4?token=IBrdg9i-iEBbxM8jszBrNzu7v3wRGA8aIZJ3B8enD5sKpHgu8nhb-BwmKIPqyHUpVu4bD98Trdi5tV44GIvIGAWVyCzhYUfCcDcZoaH6nuWhUr1n01E7dadOgvOmPEJZ4cRlMlF_-syKltZYw8-Nm9kNn0zF4sRnvHnD_M58CUiJCbkO7rtB0Ya-dmiA9lX6EeRp8W1CrXViI4dWemUFjvjAagh5PnFTPRg36GfxyIon264GM4jx69MCOCoxPGrGSPOwhwPqfrtrnDZY19t0tjkNbUnLZpfDoo-g8N5NMUDsCNCHxX0L1rFgNGRrtmtkNgAr0lxounK89AkJpkMOUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92aea27557.mp4?token=IBrdg9i-iEBbxM8jszBrNzu7v3wRGA8aIZJ3B8enD5sKpHgu8nhb-BwmKIPqyHUpVu4bD98Trdi5tV44GIvIGAWVyCzhYUfCcDcZoaH6nuWhUr1n01E7dadOgvOmPEJZ4cRlMlF_-syKltZYw8-Nm9kNn0zF4sRnvHnD_M58CUiJCbkO7rtB0Ya-dmiA9lX6EeRp8W1CrXViI4dWemUFjvjAagh5PnFTPRg36GfxyIon264GM4jx69MCOCoxPGrGSPOwhwPqfrtrnDZY19t0tjkNbUnLZpfDoo-g8N5NMUDsCNCHxX0L1rFgNGRrtmtkNgAr0lxounK89AkJpkMOUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از عروسی نادیا خمز دختر خانم پاکو خمز سرمربی اسپانیایی سابق تراکتور به پارتنرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26896" target="_blank">📅 20:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26895">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1QXRQWwulELw6onmNwPfoEsPhToYHHEt1FxGA8K_JspQFAFvz7KqxT9Z2GrrmgTUulzHVlaDFUoPf2Paw__h3-peF5UCGfiSjATnmzQn32RmdfkkK8JyRvyAPPWllPAqJeHadWEVidtj52Wp6zHt6jnpIdmgGKpSXSX3vw3nhaslBGBaKtTFKxAsUKq9aviHFtAd4SSPep5zaD2P8W-kU2rrYw21osnfeUML7rAAUZi4xxYuUGTXo02wzeZDkWk-bMjNjLbOho5wDmu_QKT1gFiO0J9kNsEoeIP7fwRknEtwAxXDkT45APeJwxVjkRwhM7jcJEcFc4A_FR3tGUrlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26895" target="_blank">📅 20:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26894">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-1u3KAXlm_4Z-HNSXI71zCth71edR8LjP3Jl7sgWwkUBIOWoCMZpfcWfw0E2CIflKVKkWDEY6OTuEgcyf9kcdIpHMUdpaiyVrkXnZGHa_XzPRmy2p4CWHPGWDbC9w6ETCHlgJ9_ZM853vGD_l7XL-jALID3DgJ4TT6Mw-sSXKYZ4eI7wHzYd-QjA6tMN27mMbP-4X83XABxsY-Wlslxqo6Ar2Rd3wjRFBrKMyA656k58LmG8yxj2DcnfchcUP3eCyMNdL-NMxJCUu6uNLpPqlv7mJyrpQRwQ31NIQV3pVCsRAW_yDtI8ojrMht--ro0qzLn0FkD3cCZ_iHd5uSMtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شمارش‌معکوس‌تاآغاز5+1لیگ‌های‌معتر اروپایی درفصل جدید؛ تنها چهارده روز تا پریمیرلیگ ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26894" target="_blank">📅 20:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26893">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAH-ywhuaxrFnaI-2Gk4t2ZPmDegbcOl84p0dQIwQ04iNieCV83Z5aOhKu0EL5cEw-Px-UFp_8qYiiJM0xMKtpp5RwRzeNdtboiJS3NxSSNtmZRi1KNvwRhh2DS2fv6bxbwDl2qbWFEMSCUAb-gGYABYMriXn1fMQvweToe5SkJXdlcgYzFyGQJnxTBT-BAEBEknzkiMueBD8ToSAF0xr3nHStUrNMsK2cLFgIgdF7blR6UOu9pAZ3eduxz9c6n3SFBdpx_3j91VoSP_w4nOswP4etWfi6ffRaSzT_Ng4LYXsXjKEbjM1uYpeGyL_NGN8YRNfwowiTZERxCja0T9xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکرد اشرف‌حکیمی،ژائو کانسلو، ریس جیمز و آرنولد 4 مدافع‌راست‌برتر حال حاضر فوتبال جهان؛ رئال مادرید حکیمی رو مفت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26893" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26892">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9ttpZAGKLIGNe9qgpa2wX1vdX_AN9s24D_ijf7SNeDQ0AayGNUdMZfDQiHv-T4ma9TVj8yVjWKnvN8uF2EfBMxL6bvUiRNOh2AK1Ow9UIyk8nXNys27TKUC8upQ0EO3BYteGbi3twdIglxwQA8r2cdFYKbKMBI9o0r52d2fxsMaDzEZSN2sl0Fhw420MbN4Ku9xuON_1pMoTY6ju-WBu1nJGjgwil0tayxGOFhYAmIrxh3yNcpZaHoT2M6-pgrklJUjOs_j7wRg0kxNhhj4HqF3K-ePxmUgLY1XLcxgkGMIlsZXiA_6lvbtGtYJN4bwijq_kwFs2QWcl44j-faVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیربرنامه آنتونیو آدان؛ این دروازه بان اسپانیایی از تیم استقلال جدا شد و درصورت بسته بودن پنجره نیز قرار نیست قراردادش تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26892" target="_blank">📅 19:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26891">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgTNY3TN4UnLEekNI7ioV473V5ACcqePVq2leiMHot4fOTY3sPXaUiQyna3el4xjd5w4lqX7lFJfIeJ58r8MeDH1ttjS0y7b9C73O-ZkWNOqGkPZwnNqvbZ0Qg4H5J4HIE-tWQg_ZIx89p7h0PXn4ds26uukB20lRMlwZVLvT4CDl0DUBtYYp6uhCljRm7j3jITP7udNeBbUsxGIy35DztbiI1PIrKCNpDI4fkOF5m14yfJhkLqqiLVCLYt2pJXzxcoDSe3FIiXJi2XBgtD9PoKrvxVRjpv6aXBaC4alMW-9xty76pZiiesXTNK8zkiKVH_Z70XoIWd8f0sZ8qSjLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26891" target="_blank">📅 19:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26889">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zp7tOhpHqV4HDcTuyw2lqKXYDrXhe0tbrafy7EfvdVkErTs0DR9c170w0WL8O6reAxgG9BpQ64V6okf_ap2eQch67ibF8McgYqVI7lOZiPKTO-mNrTY8OcgkFceoAu21038WWVNgSJSdGcm5J0BwiFv0F_jgwvr6rKHHi3gPKdZVLbDsvauWsP0JasckCeL4ZkDFXmBN4KY8VkhXn6Byxog2__izHTrJNn962CsJvn5oyC_TnEkYjQicruYWhs68acCCfWEhCjfiaDVNHCrkC1vdf-7EFLemtyUCFKasOXazADftvST6R5M_3Q-W_VwJitQ2uW1N_WW429rae2LkvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
همسرایرانی‌خوزه"ممد"مورایس هستند سرمربی پرتغالی سابق باشگاه سپاهان اصفهان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26889" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26888">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoUnjk0TQDOoYSzrkfqimVgg4U1DG2N52xkNRVgL0H3j3700cfMCfyy_6Fpip7b-PXJU8c58A1Axjt4c0W1bk_TfAXjZattnwGIav9HB02MgZWqR5OptCFFvw-hHDbtmd37o3G90fnT3eTa4wXNMj0wVGtscb9QkMLnH8YXWAALdrxfr2BVQtDSJYEILSGNR97dJdMohZ_DQlUlNYEwSI6k0dHzAP3V_wXeJrwvn9n2_VgMIWCqn7jPGNPB9vDRktYGF6CU_3PWMX12g9sJSfImrX8IL878_ySk7R9OC2wSPqpCD9ZDtnohxkrc_vrF_kX3mRjZM35740o_LScKjoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇺🇦
مارکا: میخائیلو مودریک‌ ستاره‌ محروم‌ چلسی تصمیم گرفته که در رشته دو میدانی فعالیت کنه و هدف او نمایندگی اوکراین در بازی‌های‌ المپیک ۲۰۲۸ لس‌آنجلس است. او تصمیم‌ گرفته‌ که کفش‌ های فوتبال خود را با کفش‌های دو و میدانی عوض کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26888" target="_blank">📅 18:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26887">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی از مراسم عروسی کریس رونالدو و جورجینا  که‌توسط AI ساخته شده؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26887" target="_blank">📅 18:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26886">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsFr1rRctil7KQN1-6fAY-1tJ-29EwlnqAo63pCu1CyJ4FoVUayEGP5vmKqlXifxwFceT7YvFHqM-6qXSRJlNN1v7pqSm8WeZpwdzHNRkbu3GQsevC41ssIcZ4_HPe0QARTQaka64Flc2Ug3VrQToH6qSv4kD7wdjmLHBlw1LTwVycE3mMS6k9rRrsf2al426ay50aOcFy1iFIWnaCAF7pc0-pmPI9cdUL7s4rDGyWGDbEtluJaiUYDMhf71rX9BwhG-JwYrx3mqk-Rxvg6bmhyNmcan-3Q9PbtX1BEeIxct9zNnbOf-IWyUVm_npSdmG8_hTu2OmnX3Y-WaQoaAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ESPN: رودری به سران من سیتی اعلام کرده که به‌هیچ‌عنوان دیگر علاقه‌ای به ماندن در این تیم ندارد و قصدداره‌راهی رئال مادرید شود. شماره رودری بعد از عقد قرارداد به رئال 18 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26886" target="_blank">📅 18:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26885">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVvgecPM9Pbe2l1tWTmEaakKRpwmUCrNaMTNrmMLpdpnd-YqdxS6x4CZn4CvyRdB-goJS00LtVKelZBIhhEPkM-lij55M5xmDH0koycWQUO-8Efozcm9jHUXERM00jlNZSdWlBmFqppCGz_V9EV_pdI8JsQ4TWpL5SoxJ_WluBRrhWcU9EOs0sIM55OA-BgQydM2YVe7iM_JKmhLJsJgKf9Q6v5--gIl7M8A4ag7t0Me8TRmcf9slNntl2L-lfyTTblRpqWmqu_RAMjmhbt7eOpWwgl8H6p-REcHmcWcMQme4IiH3FDvm1SL8gXPR73b7ajiN77R8_j9cSqf6ImWyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمارمعکوس تاشروع‌رقابت‌های داغ فوتبال اروپا؛ تنها 27 روز تاشروع‌جذاب‌ترین‌لیگ‌دنیا "لیگ‌جزیره"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26885" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26884">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zc4yO4F9HQ583WbQIbNbVpEYQ2qWOQZUPOr7FCb1aCwo48DQpVC91o0c1YDH2E-g4SfjDpRgdTCQmzLdcfj2KcMhVl7WQENAQUZyI3L2fUEx7pCipZHlht9dpGaiWvy45YcaopmyJ0EKwKAOCoEkQCUTPe2LNdZ2gRDsOGQdwFFSVrLs-sCKuehfdsultAwdq-Nk-9712c7cWy5FsyZQ0B9jBlStPRymyvw3mWgr_26Za6Nx12vV0i6QkpK5Yl6CZICwwlrSj8k6Y-a5iJ3RG7ezZgMHuNZhXgOfgCi5l5GF6vOBtSQ8GV9Z1Ge6AhglxknvcEOkgDXerzX6Diuh8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26884" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26882">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oztXSpto3DH3-WNAJsuISkFSCZamZN0Vn5ABsXlF942D2GY_HRr8IHGzqqsin1r0vIXmIgHw5xEIavvyZU8k9hnlCCGfF_CUJVu89zErOkkrurhSKehL3l8reGaUDp2cEr0dd05ggnJBL076PsPV4v0d6BMc0woeEIfwF2i4CUMreJG7FywdAR8MrkxKznfWpFqmncDd4xYGaoNVNnw4eUoe95MVsAqMjJmpzW1XdLGsQqy5E9HjRFP1s-o1mtR4EuKYxanPsKPoEF1PhN2Nm7Dv0m9ZCycgrYsVAMDkjCK80Y2hsVO7LxQlnT80IXNTve0NPXuwL29F75xUH5X_xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
وحید امیری کاپیتان سابق پرسپولیس برای عقدقرارداد یک ساله با فولاد خوزستان به ارزش 25 میلیارد تومان بامدیریت این باشگاه به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26882" target="_blank">📅 17:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26881">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP2fO4ha-qOPGbfDe2c7tcx78ltn6NF6L7RkNrGO6mYCQjlUxsL-CDcO3EeEmyDvdOLvNq4UWf9J99MxkJQk_YNV5TYNbMIaozU8FbCozX4r6_WEaYhRMzea-Gbxo9VXOgsv6LyIwqfi6wOXmrwRhardO2w6rygtIhMm3JClLdXXAVnti3G2c4F2Kitz6FQJDkkpDMUUebiYHIszImGgMKdm7pK2xXabyLXYD8-99QXyxZDXwV-Jp5U7HGo926RvgIg3o2dSyp4mkz_FKJRmSKdm8prSdhG6qclniThElvfvboHdKRojk5nut3LPXdJe8btp4NA6fP3h37mfw1pGHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوتامندی‌ مدافع‌آرژانتین:
دخترای‌خوشگلِ زیادی بودن که عاشقِ دیبالابودن‌ میدونستم‌ که اونا از دیبالا خوششون میاد، گاهی دخترها میان دایرکتم میپرسن "دیبالا پیشته؟ رفیقِ نزدیکته؟" سرِکارشون میزاشتم و میگفتم:«آره بابا اتفاقا الان خونم مهمونمه! میگفتن میشه ببینیمش؟ توروخدا، میگفتم آره آدرس میدادم و تا میومدن خونم میگفتن:"کو دیبالا؟" میگفتم رفته بیرون مغازه خریدکنه الان میاد، بعد از یک ساعت باز میگفتن پس کو دیبالا؟ چرا نمیاد؟ میگفتم کار براش پیش‌اومده‌رفت‌متاسفانه دیگه خودم مخشونو میزدم و باهاشون دوست میشدم. دیبالا واقعا رفیق خوبیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26881" target="_blank">📅 17:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26880">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alxeQO4koALfRshbVxw-HTlu0DD8GfjK1bty9IGEZ8aALD-1Kcoj5SBF6pp7vNUlfyfm2ErAvl8ly-kRfoktAS-KWgqS5ssEnN3fNpBvOpxZDWHNYkJys4VQLmLWc3KzdoTaCb57tQ-Ae7W7pFhIgAN22NnFtWnSFESqyNqDhtgl9M9fGFOgGk4USHT-T-wP1kdUWyBmZgwQm-isBynkYM1OsSRV6hE3GjUM3f2MwRxznKZizhbKVcXci0L2_8jeQArQ2FWPwnLsUWLTAGyhsBBMeQo-UV8EufuXUePqLQUHbWITW-JbiYQPV9R1czzt5Y-kaKZ0v8pJpH3gPqDSbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
#اختصاصی_پرشیانا #فوری؛ امیر رضا رفیعی دروازه‌بان جوان پرسپولیس که در آستانه عقد قرار داد با تیم‌ گل‌گهر قرار داشت با باشگاه شمس آذر قزوین واردمذاکره‌شد و به توافقاتی نیز رسیده که به احتمال فراوان بزودی پوسترش منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26880" target="_blank">📅 16:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26879">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=DwXW0or_k7vVggr4474aE_CAC5Hk4k9Ji259bk4e-EWWgFwF-y_9B79G2ZTnfizkVEpgKfg1qOu99bl_Nvhn7VsKqNsPqWfnm_u1MJckK6N20az-qOxMUpfp-ZV7DVoYl90SqenQmYZkz0VzMnbmOuIe3vNeEjfoEkMGVcJHwKs5u4U9CCuBSrfzUcKHJc34BCoNqeoykJ3iyd4UQznNhwKi18nX-8lgfGwfsnnfLX77i25QTkOydo9AxtFa6JxHzLiOFjU00SGX_l3Ot8WpeAVMvnwKORWpgyfQ_pM6Nc6A3IfkE9N6bmPPrk-Q78xFmZZ6KcMMZ8WpRT5S3y2QBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e6b766e58.mp4?token=DwXW0or_k7vVggr4474aE_CAC5Hk4k9Ji259bk4e-EWWgFwF-y_9B79G2ZTnfizkVEpgKfg1qOu99bl_Nvhn7VsKqNsPqWfnm_u1MJckK6N20az-qOxMUpfp-ZV7DVoYl90SqenQmYZkz0VzMnbmOuIe3vNeEjfoEkMGVcJHwKs5u4U9CCuBSrfzUcKHJc34BCoNqeoykJ3iyd4UQznNhwKi18nX-8lgfGwfsnnfLX77i25QTkOydo9AxtFa6JxHzLiOFjU00SGX_l3Ot8WpeAVMvnwKORWpgyfQ_pM6Nc6A3IfkE9N6bmPPrk-Q78xFmZZ6KcMMZ8WpRT5S3y2QBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛ فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26879" target="_blank">📅 16:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26878">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=Bnlk3g5mfJVHGAtf6QcLjxnKSpJU_90uoYGidjkvdmt8YjZIdq6WcD_RYb83f0ffhPS338s1orH72Niln7RafXK68XN7FrwvnYBMbw9_MDqRUgJ3lc_-exgXgk_GUbjh3eHg55x_yv2q4UauSiS-zN7IMsi1tdTZcA0nWDH94r4bW0Hr4TDz-9tsbiWhWcJm_zWVmjDWokSFutsjDlA2cfyqaDmApRdbQs9v69C_SF7dJit_xRkhIjlzH4dtIuIfHMsHSNo1guFeyxTj8HcOaseAqP_ZPF-LywHgPMwxZaeC6anRgn06Nc9Q3B2UZ9uCPbOkjtUWeMdF7NNiC77Epw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98c1f92f.mp4?token=Bnlk3g5mfJVHGAtf6QcLjxnKSpJU_90uoYGidjkvdmt8YjZIdq6WcD_RYb83f0ffhPS338s1orH72Niln7RafXK68XN7FrwvnYBMbw9_MDqRUgJ3lc_-exgXgk_GUbjh3eHg55x_yv2q4UauSiS-zN7IMsi1tdTZcA0nWDH94r4bW0Hr4TDz-9tsbiWhWcJm_zWVmjDWokSFutsjDlA2cfyqaDmApRdbQs9v69C_SF7dJit_xRkhIjlzH4dtIuIfHMsHSNo1guFeyxTj8HcOaseAqP_ZPF-LywHgPMwxZaeC6anRgn06Nc9Q3B2UZ9uCPbOkjtUWeMdF7NNiC77Epw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی کوتاه از یه مسابقه والیبال محله ای در زمین‌های خاکی؛ جدا از بازی‌خوبشون و اون دریافت خیره‌کننده‌بازیکنه به‌وضعیت داورای بازی نگاه کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26878" target="_blank">📅 16:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26877">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qI6tk40C3RLVsX06J4i4HBNVsU7_dV7rTaZrCubrnEhHYnpa8D1CDXUQnWUHFK_z7Ruc_XhQbAVOfTWcKxEMlnpOt6fi0jihEsgENO-5MohS_pvjcX-asqZ1EQIIvDN9K0-ByILNPap6-aqq2_Snk5S2jokDn28aBZVqYYhbKAB9ax7MNmsS9ixmlius_XCTRvpzVkU14FIn-gVHcb6stlw-DC6yUzifWdWGHHvFFk91da3UVFaz10kaugNPbE5yioSnozq-6jAH546bkxeKXjBvapry_c0-9v0GD8oa2W7Ag-i_uk1B-EeZ6rlvm3r80qPEZCNzBcWzKvkx358Suw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|وحدت هنانوف، برایان دابو و ابوبکر کامارا ۳ خارجی سپاهان از این تیم جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26877" target="_blank">📅 15:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26876">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhZlUYNveawjZfSC1lYz4vjBJap6XOxNGVU7cuMbf13D623elzfosVaWvVMLoWpauYrdUb1F9DGaoP3lg3zVPqhQBI-VvcGaKOUpj8NogSg83V7-xeWmgbQr_s6LqKcolk2gStUGoTpp9uaBKMzgRUBZ1lF0PbO8BkbYaHoBraaPo4kRm9pF8hU94qzOc-MVGxTQaHinSJLAKG7TRD7XMzlyET2gcKwyvT-xE9L0tWiQkWfefby8Ts-ZA8bUGY2qWAJJmkR71Y7U-qkG02MUAw_zTIHCOEYrYAURwPHT0AujFdzZiskdEYtpT1i83UDZufv3OXXj4TAxLqrMmbx7og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه تراکتور ظرف 48 ساعت‌آینده‌از محمد قربانی خرید جدید خود رونمایی میکنه. رضایت نامه این بازیکن دقایقی پیش از سوی الوحده امارات صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26876" target="_blank">📅 15:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26875">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=q7MIt50OXO3O3jHWKXaiHZ6s9oLwSm892le9bLyYEI6kSkWRVZ1EQpqrSLUyZfcK02t6K2c55XPXhmqHlYeziwb8PzI8gD2kR4ZboaGO1SgGcrzjLLZBzpA5eOzbTRXzwyKYBD03uBdZzj9UoT1yFXVlynFAnr-vcpVHcw7kIm76d9LYMTw9b1upJeElUc8YIBfifNtS8W3ltPBfMYnlmhSn6Lsu69HXsW_hdCVjfgwJFmxeBo8te6gfZw2IYxgk73toiyCopxnYN6kI3mvS0tTApjwFD5_QFtct9vdH_YO_Fb-XCQ39L14vhf9hcPBjnPsZYtoigXlJXtVE_YXcvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f12e49800d.mp4?token=q7MIt50OXO3O3jHWKXaiHZ6s9oLwSm892le9bLyYEI6kSkWRVZ1EQpqrSLUyZfcK02t6K2c55XPXhmqHlYeziwb8PzI8gD2kR4ZboaGO1SgGcrzjLLZBzpA5eOzbTRXzwyKYBD03uBdZzj9UoT1yFXVlynFAnr-vcpVHcw7kIm76d9LYMTw9b1upJeElUc8YIBfifNtS8W3ltPBfMYnlmhSn6Lsu69HXsW_hdCVjfgwJFmxeBo8te6gfZw2IYxgk73toiyCopxnYN6kI3mvS0tTApjwFD5_QFtct9vdH_YO_Fb-XCQ39L14vhf9hcPBjnPsZYtoigXlJXtVE_YXcvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇧🇷
پوستررونمایی‌رسمی‌باشگاه اینترمیامی برای کاسمیرو خرید جدید خود؛ قرارداد یک ساله همراه با تمدید خودکار به مدت دو فصل امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26875" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26874">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSnorqq_eddxy43xSmF9jhRLWl_X7AdYpUDLErvQbLU_A9iDbtToXJYqiSjKzo_YkHjMuze7At_EDktBQFj6NrUVb_Zh7DfPMPSlgH5K1eadtw1DGlIOwSKPPVy_1M9tDWkWl9RS4J759jmRVAJrEzE0HLUeA-BVWemq5cUsfm3kiyaFUpblD2Pj8rThF4w39YND6P39DN8X_quJ7YWbhJuI6iafA6LknMg9A5ZqwtCjAM52mrfTJMJjxjAVbMjVvRzoysVfiv18ZmcpPwSCYo0EP5H6g52W92H-GJKXCX1mdzV6MbTYMDvHk6Pv3IyaqEgiKQ5xxTLjijpM7kBXdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارلینک توکشورعراق‌فعال‌شده. قیمت‌ها هم با دلار ۱۹۳۰۰۰ تومانی: ۹ میلیون‌برای‌سرعت ۱۰۰ مگابیتی و دانلودنامحدود.۱۵ میلیون‌برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود. میانگین درآمد ماهانه مردم عراق: حدود ۵۰۰ دلار که میشه تقریبا ۹۵ میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26874" target="_blank">📅 14:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26873">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCGtgKMtRInmACkXs4Ek6zubNj-yc5clY7enOI7Nvg8CrB9259qLoe8X8crr-5bs3hICOBogZJhLWv978-ONskjgMvW6bYjC01W_QTAX3lh0EP-IsMNtNAeqAhK71WFJJWrxv5p8mQMFpmYKZwiX57K1MZadJFEe-BN6Lfx_oOc71QPV4nwhX9Cb5BC_nuS18eQfFj9haTJCAT0kJR7GlrqSlJzN2AZ5ALs7wxDJ-0YpFoufxKWHim0Z3VUphVffU_vGAZg4ydIoVRkfy1Ifitz1zp2NQ_poONpjgPsU_F4qEYdUrcPa2EUYJMsvV_IYRnrTrfgdxkdFZZGJO8h7bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
باشگاه آرسنال بزودی بندفسخ قرارداد برونو گیمارش روفعال‌میکنه و از خرید جدید خود به شکل رسمی رونمایی میکنه. تمام توافقات‌انجام‌شده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26873" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26872">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=ssrYmWwwhFU6f2LF_p6_4JpdzhsZLNLQgkHJSv9HaR5h3vmo-B7ul2OFPo5FZx_DsMSjlFMCMDODFyIXNTshIYsnWSXMVUN8VWKxXYM5y-he5lY3udIKGv710YB2smcrZvFWi9-mskaR1OD4QD5vB8bDRKWaz9hgbk9E5Gk5wGMK_SLJF7N1d3XQcgg04AeUpkXJX4F_x4XMpLoCz4LHzsVGRuxU5cFCDJO8_GTQYuox3uh51cAAwHio5qn_bIItSRh7DejZ_qzxKm7KYBq2hEmXtxgHFTI2oyq0Ae8Ybu7gh9o0ZANnz6fiV2HUkut5teioirLnMztU7cj22ktJXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=ssrYmWwwhFU6f2LF_p6_4JpdzhsZLNLQgkHJSv9HaR5h3vmo-B7ul2OFPo5FZx_DsMSjlFMCMDODFyIXNTshIYsnWSXMVUN8VWKxXYM5y-he5lY3udIKGv710YB2smcrZvFWi9-mskaR1OD4QD5vB8bDRKWaz9hgbk9E5Gk5wGMK_SLJF7N1d3XQcgg04AeUpkXJX4F_x4XMpLoCz4LHzsVGRuxU5cFCDJO8_GTQYuox3uh51cAAwHio5qn_bIItSRh7DejZ_qzxKm7KYBq2hEmXtxgHFTI2oyq0Ae8Ybu7gh9o0ZANnz6fiV2HUkut5teioirLnMztU7cj22ktJXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26872" target="_blank">📅 13:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26871">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/najnp-WnG8x0WH7165hh-Bt6-q6R9kGyY5q570xAufBDoW8IrLVysCkDsKnIw_oZWJ5L0p3v2DzLZETvnnLX5OzeLDjVSY7ZLgAnyggu8kPoRMsK-RR1xLpm7ahDyC2tGciagTi-8QFvqcBdDKfpcHvx_c8eJQIFsoX3DZry0OfkKY5gD4AAJVm6tRfAyeLwKXRQHZ7ERk4kbphBwR5Fv8ZE4QDDYcPgCEUSuv8t8_kP2671ULxSoUtw5qhwunAMTWdlUZPk_kG9R9TXjxnvFWB_L_9u92epXtswh6UuqOBScyk95jSxuvy5pgE0Cc-sQGCCkvXaZAMX4YcjtHj2GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه که علاقه زیادی به پیوستن به رئال مادرید دراین‌پنجره داشت تو تعطیلات در حال خوش گذرونیه. ویدیو مثبت 18 بود تو کانال دوم گذاشتیم. بزنید روی پست ریپلای‌شده کانال‌دومم‌داشته باشید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26871" target="_blank">📅 13:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26870">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=jPTFgLOP_oNV5q1Ttqe9hyop8UtnAeme9c6DeRMqM-z3u_7H-HjMY0aVSI0k2izdAWzYcLNV9-VR6cD3E6Y_gH_q2N11pw5JwLrzj8tSUNEjq1VNMMeB101jpFi5u7k7reYOnIE_6Kz5y-HCOQE0cipQ-5e62w1i75kIHNWCYcxHXiIcxLUt7CaT3-YBbLlf-f-Sr0YUL2CfabsOPxgtfUwsI74z9Ja6fPmoS0-i1MaQyhBxjttLiQx2VTr_P-PvH7iO21Cmg-RNWICdkiYXmUWngsbBPjEc61VToEpCL3LT3O90012-7F7s1qmdaOHC12dnLfXQX6QPhdOQephTBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=jPTFgLOP_oNV5q1Ttqe9hyop8UtnAeme9c6DeRMqM-z3u_7H-HjMY0aVSI0k2izdAWzYcLNV9-VR6cD3E6Y_gH_q2N11pw5JwLrzj8tSUNEjq1VNMMeB101jpFi5u7k7reYOnIE_6Kz5y-HCOQE0cipQ-5e62w1i75kIHNWCYcxHXiIcxLUt7CaT3-YBbLlf-f-Sr0YUL2CfabsOPxgtfUwsI74z9Ja6fPmoS0-i1MaQyhBxjttLiQx2VTr_P-PvH7iO21Cmg-RNWICdkiYXmUWngsbBPjEc61VToEpCL3LT3O90012-7F7s1qmdaOHC12dnLfXQX6QPhdOQephTBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیحات و عذرخواهی میلاد کرمی ملقب به وضعتان چونه درباره تبلیغ مرز ایران اربعین:
‼️
یک بلاگر معروف در فیلمش گفته بود در مهران ماشینش دزدیدن از این مرز بد گفته بود خیلی هم وایرال شده بود خیلیا دیگه برای رفتن به کربلا مرز مهران انتخاب‌نمیکردن؛خیلی از مردم ایلام…</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26870" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26869">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VomH1XNzDYQMoN6tNTs_p1NN9Il7_yalhM02GoskCrE653_cwEF-zA60LU-F9pELLXe0Q2pvpxB1zQ9y_g3xrH2fzvvBBHvr4cEmy6Nq-lOtLx5215K1rZRxncdzT5sZ3Fk2cNGCuam4QZRTBqIgbkPWVK-nOBF8bo_jkO1s-HNhAh2IEbCxBv48du1lLwiIXaIr_kEbwTM9h9paAaB9D5aVxaEWvceaMjDbVNuang15bw5ywmVYpNUOje0FmAIc1yB4AG7WNGxom-7h8RzbASWBAr9ib7lgEtEliOXZf5lQhor6eS3IRetJA0Rs4z5Wn4EKzqZf5EwePae7YVOvmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26869" target="_blank">📅 12:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26868">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lsml0B_zFBAeicFpS2bAOfVFsUxj-ebLw3vaKf4oEV6pOi94zDcEGOuw30gXODn5-RZWhPJsWx-yv5HTFp3kSnkUPURsHxVfD1LHwodRPWzpc0dQMU1JRTXjhU6exnajCAbYE_rMn9x847B6R6BpITJNiRi0PQ2-64ZxDmPoH14bewKgftgbsqHrtYlscWjYWVfuGDLCQNMveJ9M-k6c6g4QV5jDQrqIy8iVeEbtSlh9OvSfPzhT5QuoEpnMj3UVkUe_2_KRMG8KJ-83HowruPlvrssrw609o6z4-ngiCh_3LPSSpA8cqc7A-P4tg9hxi2exQW2bvjjPX_OP6rPSLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شکیرا خواننده کلمبیایی: جدایی من از جرارد پیکه بهترین تصمیم زندگیم بود. اون با خیانت‌ هاش بارها به من‌ ثابت‌ کرد که لیاقتش رو هم نداره حتی باهاش هم صحبت بشم چه برسه به زندگی کردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26868" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26867">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ctc2MfLqUPA4j0nCeydlDID3fjdn4v0i7kYXcNqrZaw-rMltbT8FHWiJ7kgWoPe8WBbY5oOLeAttL3aYu1wY-hM1iqWACCBoQGM_xHawqBAkkOHocGzoicNbcbPlJrNlBk_CKDhO9k2oEK3f2oIuywx4MDHBrAxIKwMhLQUdOJDLJ78GVB6dkbKOoX42Um93pYLSHjOZo2Af1SPBWRBa3qrglR94DhcPOQEJK92rHD6WalczMEC6EdwDPQL5SsKxWc1_2rQbDQxN2RACyTQm8SxoGsTo6LipuqHe05Xvld4A0UbHJdsSLctns_g_U8HlZeiQ0uDmXj4_i99fnbt2rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیمار داخل یه ویدیو به محله‌ای که توش بزرگ شده‌بود برگشت. یه پسربچه بهش گفت: «من پادشاه این محله‌ام» نیمارم‌گفت: «یه زمانی منم همین‌جا به همین اسم صدام می‌کردند بیا باهم عکس بگیریم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26867" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26864">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pki9wEVRg6y1R1qve9U0IiAcl_mSn4WLErlcVmkhnTfaftOeE8kf3u2CjPUVi4SieQ9vLY0erv50XvrYN0o4krqU0xpY1k9AfD5KG015J-xtqtEQGQAWQPyFxXhJ6ZBLn6xciQVlMrRiB8O_fauL0dGrfmtBR4HefR_V2UzUWSILSCwdzf8u2rGvpiA1lDH_5vA9UncT4mzk6C2uWxQvxWEdzJcinJ3Ff_szjkvxxevptdB6AMYeECEpZYE7Sd8XdtDCXl1Ill1C2EdsIKKdgr2OxA7dJDZMBRwblDQrkGLvNckjh5mzcmyS2Cb8DStYDUsyhchJ6qEKmfO8ADFLVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tlhMKyBEJd8SNF97iqRv6-eepHRezoN9ES3jiB8cn0Ufma12GBbqhiOmFxbJcBcQt5wlOhpVPqr1jUjCASurBr4RTucxhwMDmfcwo167XGf6DUVQGSPRWqyHyvAah6wiN0aSJnW-XFmX9uiSeijAVm5TFp1VwfBmK7j92bebLXzDEBkbcQ23a1VsoxFmZUZM10VokFvipySO8pgwNyMpqybKmlbQQ5tXBMYnzJhdm31o-7ts3lu7o496uKtuUpVqav-3AmiwFHHXrK6xyP8TZ3Gon4wNU7vtIveSMyWqZC6f_h56Vn6lFNHdX7-75U_FQca_WjYfkvcb_L-FTNDFsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رنکینگ بندی جدید فیفا برای تیم‌های ملی و باشگاهی؛ لاروخا و PSG در صدر قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26864" target="_blank">📅 11:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26863">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oh6kh18gPgU-CEsSCFQIPnHxjhag1tGtSwl_GQfLBYBi6PmnIPq6_mGhF5XOlq_0wwI0Lof-JPBAyIu8Mt0lqHi_-nFtuNDZiHmrq2z5vJ91iWjGDtMYfJyEcODgqcwqgwYXmbfoU1iW3rS9lJdYxAI3JEKZbdkuHLEJ6b0-sb_-NNB300dPasl9FQXvd6QduOIaLQ2dy7FAe6qAthMa70eI7EzEQqpBT4-39ZLsaxO8RNhEy5GeHSwTu5zxpgdOUnpAtX5C9OGzbfGvK14YmQPmu3ocezzwcj7kIMTzBU8PFBDgNq1j8ZhH2oBVNR40pJrXHU5p_wcCVq7UZ6402w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سعیدمهری هافبک‌میانی‌سابق‌تراکتور، استقلال و پرسپولیس با مدیریت باشگاه پیکان برای پیوستن به این تیم به توافق رسیده است. رقم قرارداد مهری در پیکان برای دو فصل 25 میلیارد تومان توافق شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26863" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26862">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPl5WnndoQaT4SnMUiuk-2p19nP0H4X0OB5hPRUj7VMXCprMzRUXr5BVtc9MyXYGE0JOKxv92mvE3lgpL371IXNfnbOPudt4LKxU4zQiOChxQ46Bt2vmaolhUZeR8um_DppSZxc82hDztsvuWczI8UOARM7F8bna2bCFaJVp1EJ9XCmCwhDkdFwCDg-4mIRrxmfJ2BAdt7gcGFrI8bbF8x4R8FluEIFQqh223yOXBA4gBJl1DPZaBVdwxpTD130cl4N__1xkao-u9QnOufQNh1q8O-PJENUUqUGKXSlugNRcSR5YLct92gz5mohHIm2cqLGsRsfeXkvjy60b-FlZbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عیسی آلکثیر: به خاطر دلخوری از بعضی مدیران و بازیکنان در پرسپولیس، به استقلال رفتم. با خسرو حیدری و ریکاردوساپینتو مستقیما صحبت‌کردم‌ و هر دو هم موافق اومدن من به باشگاه استقلال بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26862" target="_blank">📅 11:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26861">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=QtiVFkvBB1Jm2M-WSeG2qnMNFG_PAKPxwnNeq6dAUhFJpuDGLGhb8li4il5plMh_eRnwGbw6_ffE-xJyRRkJiu0qpCFbxBHjUjJFzI0KenBwUadGlUjHHWmmQJTOAnwsZyz08jjJHRz8sA7lt5auZHP9SAeKusT3iNC8X5E3my5IxwNOh8qrzY2hYLVAA3GJe3WifBwJ3H8tiFT7QDi1MZPPr6qljh7ir30sut-z9IdDx5zNuH_VNOSPwZYT5DXP4V3vwO6UcL5HZ6bME8NU16P4CS35WrY9iqHIrtjnHsayMvKxWVd4ff7jzx8OqJ8Ht8vmqxb2xClyY0tzuIwLhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=QtiVFkvBB1Jm2M-WSeG2qnMNFG_PAKPxwnNeq6dAUhFJpuDGLGhb8li4il5plMh_eRnwGbw6_ffE-xJyRRkJiu0qpCFbxBHjUjJFzI0KenBwUadGlUjHHWmmQJTOAnwsZyz08jjJHRz8sA7lt5auZHP9SAeKusT3iNC8X5E3my5IxwNOh8qrzY2hYLVAA3GJe3WifBwJ3H8tiFT7QDi1MZPPr6qljh7ir30sut-z9IdDx5zNuH_VNOSPwZYT5DXP4V3vwO6UcL5HZ6bME8NU16P4CS35WrY9iqHIrtjnHsayMvKxWVd4ff7jzx8OqJ8Ht8vmqxb2xClyY0tzuIwLhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26861" target="_blank">📅 11:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26860">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMVpJqShft1LCGhFRk3Fl4yFA2Qb_qxGmLC1V8kLiHy_QJQtzH7UoFcau3nHc9qAi5_tOmItwya_KJEpZGBm7vKkTrSzZXrX_GITnVTWqC6NKptMgFAyiKB-kGdXsVlZgURlddlQVGkyigzVS4q4c0Cb9DXKeZB5YZCbST9EPyYrQz1xM3u27epIiD4-s3GSa0vkD1mbdNXHdTypJtkgplz7fu-DnyvSfGecBYGywtUheKEHvE4xL-HqO7P6wTzZnqGCK2HQVL1w7-cuKznVfNsipm5HHgFCSD6AXh5GIVyVN5nc0HyXkv35JuUKCF2wJFcKluOioJYAvjIbbvoD9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه خیبر خرم‌آباد رقم نهایی رضایت نامه و فروش مهدی‌گودرزی و مسعود محبی دوستاره 22 ساله خود را 150 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26860" target="_blank">📅 10:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26859">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7aoJJNQFBfwoksvUUKu6G88HyTfHis8tDpviMUo1cE2dAKQ_xkZmT4OjpSW3ikp027d6r6abeMiwNwhf7DURVA3IaYpTw0uAsENs_Oxtxqur1fMuusYr0cjiYUgb4AFmNC-OBjZR8WKfIZC4Z7KaKYN7DTQYe9AX832-9bGGtJrF1s31ZwgJixoouW1EvItgZa-phjqbvsyrpWcMh-EpfCsGJNzDNiguEZ3xGUXZoiL0NHyJFU_yJIMAhFIsVMQBK9XdXIXAdPN05MQpc-cwEw6VsG6d6tiGUpPEb4SnQciPs2PI96jvB9CagP1qGI_7Bo6lHM0AB61gCR2FmPKqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ عثمان اندونگ مدافع‌سنگالی 26 ساله سابق گل گهر از طریق ایجنت ایرانی نزدیک به خود آمادگی‌اش روبرای‌پیوستن‌به پرسپولیس اعلام کرده است. تارتار به‌مدیریت سرخ‌هااعلام‌کرده که قرارداد دنیل گرا رو فسخ کنند و اندونگ رو جایگزین کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26859" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26858">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6ogi65iBHA0Q0nCRmPw_FsARd4VCwx-5FvJxTAS_dX1i9E68FV2iQwlpnbPBnoWJCPu4TPvLzJ1X6nzWxVP8FNuvCbNP2GPUzT1XnN6KX4qcDbBNdGMNA3poMhBFbMM5g_PFD_sWlEmdlwuz-THgjIaYr4au_By50BzWdP5bRuNe__C3oIUW0YcGn9D5VSRaFuS_eZtI0VBAqzzNam8BKuqFQDfdMhPF9XjMufl4w7gxUVnYV7nbASE_GKpVDkzvf1qs95iH7BYJDflSOMNPJZz8m12HIKOQVR1lrg8yjKm4aAdn_2DqM0L8PDnuJFXy-nSVfAVjrKOfDLD4JTRmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌فابریزیو رومانو؛ باشگاه رئال مادرید 25 میلیون‌یورو به لوانته پرداخت و باعقدقراردادی پنج ساله کارلوس اسپی ستاره تیم لوانته رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26858" target="_blank">📅 10:01 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
