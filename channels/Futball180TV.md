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
<img src="https://cdn5.telesco.pe/file/lO_TI58Ueh6tuC794hPzoJmJuV6wfbk3rQ3fzxlBWu7pZrVLA4VSRqyJFQKd5dUjonz5kSR7la1hItT7T3U3D7jW-FVfAy2WVKh05qhTj7VLMwHjLOrbRMNOvQMug2t53bzMwg0CsVMGyweMhNlvfvPzkEawGs-azcwZks6QAr-EusXUgJ7EizoNInmkZjyOaCEiaaadE7ScI50bd9Vdl5pr8bdd2zexxRx1Ucw__rgXOj0UHdC-FBgahek8QaCDUQEPtPbqNw4_zkYmY6a4x3PvSnZH-Nqe3mJFBNehoJ7aAz60bA_hAap5gFYd6ZdQho7L1qi-XjgNmg7RluU4pA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 166K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 00:57:54</div>
<hr>

<div class="tg-post" id="msg-90763">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuP3gko7BgUPIhXe3sTHzDvKsKdx865X_RTQrr8twWXqSri48WEgECkiEzEq3tQOaLU121Y7BR5GUGeHoPNiUbmoEcpQaCXcj1jSdCQ_ti97g4IlXrHGX58tMS098Sq2DwAguMWZc0asu4jfXeXZKd_1octivIQCJ6kkXUVmNO60I0xEAvGOV1g-JTGB1nXNdvmocxz35u0i7hJOEd-ymvErm6CheKNJkR1C7NoobxoXXkQeRaxD0_B_OzmmxsNY_7rqT_Dv_UwxYC24Cysio1j741ZJ3YISl7V8CNi8-CXM6ctlFmcLcRODtqlWYLLzxzCUa6m4sgl1KI5xXmZHuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مودریچ، رونالدو، مسی و اوچوا از جام‌جهانی 2006 تا الان حضور دارن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/Futball180TV/90763" target="_blank">📅 00:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90762">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6OTq0fDJL94N8RCEqYS7bZWk7eCIu40StEs1ZRrdj0psMef0p-xXdVMCKv51musLstfOUnnoitUm7PaMB9XDuYLMu2tgRIItxE1L1a3_h0xsroDeajSvKF7Rn3TLG3aRI0CEKUm91BGH5uJ2mSPZy0VzaoKJ6rvRT6lc_aqZqoNV3xQmdlSkX1NufqE7we9t-g1wFyPfNSeAf3Eij5UrkccQ5xzTfl9Bozqkr1U8_gXk2X8s4Ix-r2SfUtzASplWOupSYXuAhHxM4uG5ajn_JKIRxYSmDSJ5WafkfLa6hStKEIXgPAZFyqoSHjD-h6CprzrMv5hZGUD3DkLJKAwJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوووریییی رومانو؛
دنزل دامفریز به رئال؛ 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/90762" target="_blank">📅 00:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90761">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kHid7n_Dms15unWd62WgwLxZXS3YqkE0vwbD2Ja7agE8eHWPnS2mWxu9nbM1V8trxAMuNjLsjS0GuhaWog8GxlBMk0Xa1TAUJmZFIcJ0_BHp5LxceGOLWEZgg5cKoTjBfLupftvhV1qgokGsB19S1J58E5tKeBsHN1lUsY_rU1zZ4PqOS_WMQ0YJM56UGcvEepiXFeSuK1U_g7mvF42dSIE_etdBbmHyL2hRDAai3CoGh49Bw2-E8LH3wglEHIKj3U6bAwr6TGV-AVye_LavvjBwl8VaZIgZsm8LEKJU-gOhmVC_HVtUYVfl6JKw9ZMspyq9DlrI9YRaKQ2dT5lQcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولدت مبارک کون عزیز
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/Futball180TV/90761" target="_blank">📅 00:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90760">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlkzjkaal3SuyHbenlwLkWSxSMDvyMMUVGwbDDo92ksnZ9N5Kl2OmlinBOAYDCclsKql5qfooMlripycN2N4CiIJSiP8_B9J6aWoHFJMDeocx3sQ-Ys2JgRDD4SSvjyjplFuY2s88qfBAuou_JB20oDu6STvnt0Spjmrg_0mOpNppvbfGIxrBNVffMqvIk2Clffflj_CYW_0SRD1Knuz9Wl1N1oLtLShyumo-HrmYYKqU_3HeUKT1CRtHQNBDnpff6bwz23pJTHyYPE2bt1wRZoC8inFooEIfBpFrQEUeLSyP9VLLtH5PW43_mIBKu0wE9Era522B2qPDNbGWfdYrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎇
جشن‌تولد رضا شکاری با حضور همسرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/90760" target="_blank">📅 00:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90758">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
آمریکا چهار صرافی بزرگ ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس رو تحریم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/Futball180TV/90758" target="_blank">📅 23:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90757">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhfLx5ICnq3DfT7MzdGR2PkFr3f3M4lfwZJqYE8G10KB_vxG-OwWddjjkqu7q_q4wvlmEtmuKiia9xvirMVUbzjRVRfX3BwYSRxeHAnUkHzM2CYK2KU4m6vl-yF0au4OPxs4TkzvA6Fs9Seg7uz78uySeXhVRiR2t8_9yzofgsDAWCU81LcHN9g_LkAiXQkV9eOFfxCPd_CU8Qrao8vtpHQTFTMEB8S2Dz05aKLhLQaoRoX7iXEk1Uf_EhD8r3iJh8uOknVXlWfffbPVKLaeuaPxPJbWRQIaYwQmjFK2tkhek3_PxcLXw80Dg2fhn5batmE4M6Toh8dnoVVxAHg8UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین روش‌های سوپر اپلیکیشن روبیکا برای جذب مخاطب:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/Futball180TV/90757" target="_blank">📅 23:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90756">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7127e40488.mp4?token=upkGLVDUv1ZsceCsAp0G-Whvcl_EPNtklA2d3cfc2Iowrk6X_LNSVMvsmVpADsNWarxrzEBzvIOkJEPQ3-Un_IN4b7aVuOphcIfnC6Rty6FIw-ziOWAu-GLpz85R2_VHz1rW5DwrY-uGn4tXkfYCTFEvYbgd59ZeUAyw2Z01OUdRVVUkVobAel59uVhZIn2Mt6qIoVnl9ax2dNBKW8l3ePXxl97RqeppTSZgE4LK3kZ2kLIHVrHcWZEdyfLjvLysqx-yHL1_AyqdbJK3TC_UZFAzlqbSqUUlgLPsgq7zoGC2Q-v9OdzD1qXK3D_2cEkLWBebyg68mjsb-ih7wNC2CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7127e40488.mp4?token=upkGLVDUv1ZsceCsAp0G-Whvcl_EPNtklA2d3cfc2Iowrk6X_LNSVMvsmVpADsNWarxrzEBzvIOkJEPQ3-Un_IN4b7aVuOphcIfnC6Rty6FIw-ziOWAu-GLpz85R2_VHz1rW5DwrY-uGn4tXkfYCTFEvYbgd59ZeUAyw2Z01OUdRVVUkVobAel59uVhZIn2Mt6qIoVnl9ax2dNBKW8l3ePXxl97RqeppTSZgE4LK3kZ2kLIHVrHcWZEdyfLjvLysqx-yHL1_AyqdbJK3TC_UZFAzlqbSqUUlgLPsgq7zoGC2Q-v9OdzD1qXK3D_2cEkLWBebyg68mjsb-ih7wNC2CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کفاشیان : آبشو دادیم آقای میثاقی بخوره
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/Futball180TV/90756" target="_blank">📅 23:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90755">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7fd2c5dbc.mp4?token=Asa35EG0ZPIqYiIybxkIEb-mYb7BXBuWM5P6x1ZeePMNp2BCocxYeR4Fgt9dhcK1lY1aUUJacHqR0xIHHLmCCooWcFPCvjgHA2uUo6-9-yf1zDg9aeb88Owb8OUHpIQQRzQh0XFASikNVKt3q2To_VbL6vcltLZjV1hvrUK0cy3v8ieg5c9ob8rrmHf64_YRjSxxavPrVVlPAgXxrlY6XiLzXWQ_n8mKq0DaG5zBI_2dxz1NwbGhlUQTN1e-E83f1xySuTz24hRi1T-Av8Zy8dI79QQWe13yFVsvhEFDbN6_ZshrbwYTAk7eqD45fSjuZukx6SOZBwjF5zxuBMeIHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7fd2c5dbc.mp4?token=Asa35EG0ZPIqYiIybxkIEb-mYb7BXBuWM5P6x1ZeePMNp2BCocxYeR4Fgt9dhcK1lY1aUUJacHqR0xIHHLmCCooWcFPCvjgHA2uUo6-9-yf1zDg9aeb88Owb8OUHpIQQRzQh0XFASikNVKt3q2To_VbL6vcltLZjV1hvrUK0cy3v8ieg5c9ob8rrmHf64_YRjSxxavPrVVlPAgXxrlY6XiLzXWQ_n8mKq0DaG5zBI_2dxz1NwbGhlUQTN1e-E83f1xySuTz24hRi1T-Av8Zy8dI79QQWe13yFVsvhEFDbN6_ZshrbwYTAk7eqD45fSjuZukx6SOZBwjF5zxuBMeIHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این شکل شیک و مجلسی تیم ملی ترکیه بدرقه شد
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/Futball180TV/90755" target="_blank">📅 23:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90754">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krDOJXVyDafQzA7PHMPjzevyB-zk2fTwBl48vrtyiDO8qJNuuuyVHM7NnRW0HT27tWGhBOy0B0zCJo-KvhRGPqlKCS2_fbKNGbxJ8QJBmAk1BPirJfSEwCykGXP_EngJg516eRjvyjfdq3BOpuR5GOzEw2ly0Zk8D0S_xUpmU297ha2ZeCVr8z65zDxTHvLHOp-iJHwn6Q5FIZ5k_1rGco00XqAwSHu8rcc4YeeOkXu6mJctTnKAu8IKMGr8eG2EEmoKNsjuiJ3mmeurB7Pd38HXm6TxzLjESQHHiJKUjRpT9YdUr5L_NqByIh877fN_uBsFbHBozHSf--2sdm9PTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هلند
🇳🇱
-
🇩🇿
الجزایر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
چهارشنبه ساعت ۲۲:۱۵
🏟
ورزشگاه دکویپ
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
هلند در
۱۰
دیدار اخیر خود،
هفت
برد و
سه
تساوی کسب کرده است.
✅
الجزایر در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر هلند
۳.۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر الجزایر
۲.۷
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه : هلند - ضریب :
۱.۳۸
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
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/90754" target="_blank">📅 23:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90753">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ff6m-p4d6UzkakbhvfwXVBzUiOgbb6rDyCBUHtprZW7dPLqOiaZj_XTMvzZorAkoPZUkWS0ZrpsKdmeHkTeSkOH8vltU3xe3vUfIcsotiGE2txLyinWV5RBlCctUWHxCd30izOxXN-ZYFSv820Fwe0h4RZof8YRezfZy0vgqm00u_p77HYhXmiIhdAu3D0FvFbjs98zyLPSlFXlj_dJ3ywc5slGz5rQxJR9ySE8YIcfvl69I8tmMALjctgwq-foMI53NJSghsXUVc9I0x7prqEsQgnuoI4A1Zij8HYZJLPrR1yMYRDiL_O2ExHrjBcnbWGNZ4J9lRLu0c2oljvQ7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اون ایونت‌هاس که ناهار میری اوین.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/Futball180TV/90753" target="_blank">📅 22:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90751">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTGn8-m7iNkPo6SyL6P-bf69JZFAjtTlQ-0qcDTz4PpuJ5sD8W4ICLwXAGxe2oZBNo96CtxNOegk1htMTtNXurWrRtmb_jBr2pANh4fK1CXEnvKMOfx9gmbl7odW1IpfGMV-oKLgdKmq20hN12HOREtXS4vbYwFCC3hpunY24WIsyoijd_PRrMDGvaNCv1pi8J63CDBj7UoMfAdUgeYxWqDDV7mqoCAvHuNbYRy-cbf9p-ZsRYL1InV24KQxs6JOC3hnNM-ay6_v-Ae1LnFI-wtJOq2GpGsEwkG8XSquuQA4uvm9IFrwtmTtnvpKr0VCwZZB2WNGqheFPF6yC2A6nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریکلمه بدون اینکه خندش بگیره:
میخوام بارسلونا رو در دسته دوم ببینم، خیلی خوشحال میشم حتی اگه کاملاً ناپدید بشن
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/Futball180TV/90751" target="_blank">📅 22:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90750">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzywASFaWOsOcBlDjTs9ZPZGhcEugP9Z_pn0_k0JziwedNccVTbK_y_DsvBSow9BOhu4Bsfdin5GljVO0zOZE4wKoF3aBG7p2jc9UPp5k7JHRhpM3XhBgg3Vk1wuLKqZ6rp20WjU7SSSn8leFSJoRp7U6Y1YvfvXs2YXAjFEgElKPhH8_lUG_cEYRdTI0xu32_rJHEcMH9ur2qP3vFFOi0jgW3kBsCNhDyPnJTQV_vQt4d6QZvLcRBvFUzJsLafjJp8W-iCz6_ICb7vaGBipA2uBlCuSMAUJEmyfgr4hO0pnhSeW-ywKAF3fH-L7fYEC5u7a1KKUQqB7uRKd2O8RRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنسو فاطمه دید تو فوتبال گوهی نمیشه زد تو کار خوانندگی
پست گذاشته ۲ هفته ی دیگه آهنگ میده بیرون
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/Futball180TV/90750" target="_blank">📅 22:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90748">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsMAF9rbd0Iwc_vEGYBP18uYCuDcuiZc4qirroaRquIJUUUj-UlSseAP56PkAY3SjrsD2s30TreLXvtQ9V__ZmxassnfBoSlR0ksvPc1lgT7mZH0DmP1WyViO8diZR0FfzbgxKUJwyUvSyMF5esZWK80vXRiCkBMct0TIwlGKVoquJDaDLynBggc8SXHXRevPMpmzNfDYDECSuZpo2nb-piul7cLpUD_q2tpGpK2ZVqlCuk6lZStn0LI26gsE2n_9e1N0p9y02DlMDuAnuDNN7GvdvQWRaM5cnDBNON-lKPKqXTIPtTm7AN3USdjqmlQs3SZAKILMwdDmKIJhdn_sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید جدی برای یاران نیوکاسل
بلژیک با برتری ۲ بر صفر در یک بازی دوستانه مقابل کرواسی آماده جام جهانی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/Futball180TV/90748" target="_blank">📅 21:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90747">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromernesto SUPP</strong></div>
<div class="tg-text">🚨
فروش اشتراک V2Ray
✅
سازگار با تمام اپراتورها
✅
لینک ساب اختصاصی
✅
سرعت بالا و پایداری واقعی
💵
تعرفه‌ها 10 گیگ — 200 تومان 20 گیگ — 400 تومان 30 گیگ — 600 تومان 40 گیگ — 800 تومان 50 گیگ — 1.000 تومان
❗️
پشتیبانی ۲۴ ساعته  جهت خرید اشتراک پیام بدید
⬇️
…</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/Futball180TV/90747" target="_blank">📅 21:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90746">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKVN SUPPORT</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDdJKuRDa7rhI2ugEhBTRdYpAoe5q5wNZsZgh0oR7cTHerVc7xCf7A091DngBVCiHJQSix0jm9fBXkcnewAp4y4rAsRSW5z7w_hlCY8x7raVsfiimuYIHo66eq9LSrGYVkiL8h3ZXG25Fcc0u5U0bnj6r5LODnvDptAruC6xCdL8Lxud1oY-ZX_P1__eYk1IarPw6Vp-NidIREaWEGgFLrCJ9-cUlV4aBDayUBlew2ePQoM-4cVE-sERYBymgfGtT-Vdlvg1kH6hpja9R-0npHSNi90tBfyEP1iEoUrfcT7M6lKCA7AIu8DlUjLN9ZONaf3eA9sXNMjFedNUrA9-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش اشتراک V2Ray
✅
سازگار با تمام اپراتورها
✅
لینک ساب اختصاصی
✅
سرعت بالا و پایداری واقعی
💵
تعرفه‌ها
10 گیگ — 200 تومان
20 گیگ — 400 تومان
30 گیگ — 600 تومان
40 گیگ — 800 تومان
50 گیگ — 1.000 تومان
❗️
پشتیبانی ۲۴ ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/Futball180TV/90746" target="_blank">📅 21:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90741">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-zvxam1_7K5rC6UFVT4NImmIV27tH2ICBv1bk2d5UBdpBwnFBA2DuPLSXHiQ6iMrQvS3FMRG6jt-nx88m6YStEdJ5HlXLa36t2bW5TJDpu_7wN4uqMFTJmvPwND0NNjJSmFyVz7nerwDVXHiF58y3dQY7eyX6uRfvElsJkmPELWgwh_Bk1YSn84sgXfY0Oyikeh9nZ_O1IyXdVX0GT9BRM2L6eVKpUynAY_5hsEYaxUdI0b5VP858sLtz2FRyjvSfZkgpN1XeM6TSSS6rvbEmr25xEfnBWPVp2iOpOX4C474sqwkDfmeCqJJt08AlpGoenc3Phq_40HyrGXJDNwSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twGOpiOcn9mn6F3cAHxlQP0v6iRlithO79xagh6-ScErOuBE4uyimUv6E9-8U47ftid8s-VuHGsdFzubHkAXIZRe16xcvfoyeC8NTYY4JF7lJIwlTmuj2ZpootMaCkHsGn8n132n6rpHf1QcLPuk_8-eOPqyMI20fYzxLx70-ifUOzx5uf4EpLlF3eSFGV_idJupT43abee7OjOUCSQ_eITUhI0tmnqZq-_Hh8peL3cvHzZUuZZ7WxmoZ1glGgz1LXon-zomaNmAX5lXFSW7p-U29qTdvPqMlb8auRnb_AqYBvGcfFVpDDhWgfCN2SydUIF3okeQiLvbGqYaPRN2vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیه اینجوری تیم ملی ترکیه رو به جام جهانی بدرقه کرد
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/Futball180TV/90741" target="_blank">📅 21:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90740">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJAKyJfZWjwGezC-xey_7FximuonRqz8EN8xaA8gesV1vpazYrOwtgTHd2lzRD8IaZt3bQ-vXBssxO4bDEL672xobEW3jsZPgsLUfK2hTG6YQTALjFsKMP053qQTyhKQZHj8gq5FY8K3M1bojB4wNjuYTyF76UldSJFILmyCaCcmafEI4B3kUqOwxwr-VyBfYH-oxK1O47hbZou_ZIqs1opwh9ynUl_rxAKdgtqxN13kCGbiiBiwhHWspPFie3qyGs8ULaJ8X0KsV1Yvq6gtjT6RvAiTVmDBt6W7h2I0GNSAwSB5KrYgce39UIFKXqeHZRjuNdEtfPBTdiLEnEFw4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
شماره پیراهن بازیکنای انگلیس تو جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/Futball180TV/90740" target="_blank">📅 21:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90739">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001f1d80ba.mp4?token=Ag5xBAFiGHSE6LwGI1IujAUtyORPP1_OUmB36tvYcuaNo6iVMcFX6t1ANtihKKxZxY22efKiMKj1jiqlQLWe9tAL_ZhevVWBVboCoSXPUJbxdqb1yqySofzi5ByhqcgB9JaDLjiqdygkkdhKrhgQdMUT4zxlJA1Btvj8t3NybKf3ifxLJEtheUQTBUZUlWCHvJuapBbusCu9xm3Ww5Z-jbo_RWrjlkKGH_qQrJfwvSXJgaFMtLcTdYK_qbrhkydfawgWHhR8bd_qdOAuL8aLele6fSxGPas-blz35b-L8z-bcLl4xYBOG5fI3jb4-M8ZDsGW4bbVwsJ8fiz7f5h2eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001f1d80ba.mp4?token=Ag5xBAFiGHSE6LwGI1IujAUtyORPP1_OUmB36tvYcuaNo6iVMcFX6t1ANtihKKxZxY22efKiMKj1jiqlQLWe9tAL_ZhevVWBVboCoSXPUJbxdqb1yqySofzi5ByhqcgB9JaDLjiqdygkkdhKrhgQdMUT4zxlJA1Btvj8t3NybKf3ifxLJEtheUQTBUZUlWCHvJuapBbusCu9xm3Ww5Z-jbo_RWrjlkKGH_qQrJfwvSXJgaFMtLcTdYK_qbrhkydfawgWHhR8bd_qdOAuL8aLele6fSxGPas-blz35b-L8z-bcLl4xYBOG5fI3jb4-M8ZDsGW4bbVwsJ8fiz7f5h2eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هواداران عراق در انتظار جام‌جهانی؛ واقعا الله‌اکبر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/Futball180TV/90739" target="_blank">📅 21:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90738">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loXl1LvGr-zBEZ_Gu-NojzhPs_YiC6UzDOI_xFWYLXqLMQ7WA4oqKTGU3a2RrY1oR-dG4KcXMAO9erMjp_PjT6LvakjQpjMQZTM3ZdA85y57M7uMDt1w3XiaMjUJyQumDIfpSSG6rrTti9iYO8FZGvVeD4IEM-e3ZWiujALhls5vNXKUX0ZTnI-PXE_ZWFqNLs0hvQfBiQ2Oi71eQjYMK9VOimzjrwCxnU3cFqtT7zsW8faUnfG-dauaNkkF7UYp8TN6aOi_dalE80ux-dpWdzUcubNwrJ48ZGA3vq4kPSayL8AmAGByvsCajWkg76VusdF3iDMlKlcLnhDY5sGQ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مقایسه ویو موزیک ویدئو شکیرا و اسپید برای جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/Futball180TV/90738" target="_blank">📅 20:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90734">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oe99EbpPwckEet1TZthEY2sMxmTvgxSe5saY8tMo9C972o0tlihdJDqlLyGDU02hrkQAx46MxNG5y2LWF5vMhtgxiByF0SMs0PiFrhnymb81RK6hYKStNlud46mww9QOQq8QJf-bep0Fw1vquuThFpvqMQWtHetktrFIBj6aG1aP6iJUohAFpTVC-dSGhT3Pv8YbD0SEyfQwktxkiFYxKRfa8aYXEbsZmGJnskC5LyWzrj2B5Kep93pcEy8M8c1OANnjVA0FYgxeqv0i603GPybmF4-E_ioT-VxdJzzlkm5fwx8sX1E5B9bNKhu4lSoQ9WB34i0cvuufV9o7HsIhQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/soSdL6FVBI2AM1DKkcjGylKj29mIG_53vKx50wYa0Yw1Orzx401tJZULsfulv9WohDz8Ny1nUTz1AqWMtiqEqlcun8E6V9XrjnuPe0J1SvimFuoWYe56IfiMUeEqUlQiAhxb8-ohby_cvcyA40VfeRDX5zlm3jTKFUthK-tM1uiA7NDddRCieI1SwFoM5igQlzsfDQiKebrqyVHsKbln6iSXm4PDJXRTidaDr7ii4rwKB3nvhGZSyzrlau67zxyWogE3Cr0ZKxOz-VIGubWt5m09V_CaONl5D-GrsECcR74joZN1D5DOkllKN-O0jQl-U7MqtYm_m-1c88X9FZwTkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m1-1lGsi4GmNU_EWSFVk_IvIAR6zOiXZC0vnTNAjthU0R8YJfe3hJzHEZI3rhPHhnOfJYjsF5XtiezWdeh7AwE4EPNDex2nEVp00ohxcJUpsNdU5FWcDdSc0TrtzLLLSGvohxVkpAfJgN1NUd0aAJylwshcQRiKQ9koBTxDi_xgZkliuGRzbeO7xTprBHT26kEIn4_dHgiBZmt7gbiC22yah4lxN2WmdlzG1e-2jnoLWeuqwxpTk_lhb5wHRfE9FJuc4PJHYsOmxx5L4AG_BGCHB3RlTCsTOH2hK_p5zVV7jMgwdveK87B0iQWJsSubxj8pnhridlTm5O98HiJ_esw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🙂
بلاگر خلاق برزیلی حوصلش سررفته اومده خودشو لخت کرده که عکس بازیکنان مهم جام‌جهانی رو چسبونده به بدنش. طارمی رو زده رو باسنش. وینیسیوس هم خودتون ببینید
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/Futball180TV/90734" target="_blank">📅 20:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90733">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🇮🇹
#فووووووری؛ اینتر برای جانشینی دامفریز بدنبال جذب رونالد آرائوخو کاپیتان بارسا رفته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/90733" target="_blank">📅 20:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90732">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXVTe_bn2QH3e-poAfv3kePCxbFj4IQ23Ii9XpEo0vSSwNTi-nlHtvYFXtgu4RYIm-Nl5_OUfUWmqQRZDTt0zTY7kNExj7w-ywhV7XSZekb2ut4SYpxJvG_LIrvLQKJBc4TkKYksrV-xF1K9V3jm83puReMRU7nqKNEuo61yI7UNpi-354GG0nCpgkbY3dss6KBR7yp7RpxrRZTMBL2Lk1PlIw-lSg-Mn_vL1a0K3fVuJN2f_IDuvKloYkXIkNjgAjaoCOTTokPsiG6ogFNLKOCBGV87Ub9TVWz0sGp8WVDw5mgVocZCG0Pn9czuNuWuMeDeW16NbT7GBsDlIt-UjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#فووووووری
؛ اینتر برای جانشینی دامفریز بدنبال جذب رونالد آرائوخو کاپیتان بارسا رفته
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90732" target="_blank">📅 19:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90731">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsmCQN4sulbG7BvH9ckB9YyoD3z7b0SgrFcouP9gExLclXwUB4aiGnQG4DsbZZZ4HKC7mvCiulBvdH_842WGHpbm9UNiGpDXbpzmyE64kVfGnC1qCiaPjUqrw8InKrPhBt3tXi8ObKmOfB3wsMIiTYkTqRQyHjhitCAnZFo351JBXqewTX8D24lsan-gKjJ2_PPapgAezVS3vgj1Axk7Qrd35b1HVPeKctUFS-uvXaMHpxRQUieB2RE2pVt4WNoHj_442pRt3p2yArwScNb3DQK09Cu56a0z3ZHcutpWzABnb0priZc6utytMqfahkIR_Nsu4thHM75K9dom9B5B3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🤩
تبلیغ جدید نایکی با رونالدو و لبران‌جیمز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/90731" target="_blank">📅 19:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90730">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfqCehcDMaD_tDl_sOMz6laUL9Y8iWmj2vo0TFbn3q1a1zMZBpWkUp_mjeODI7xc8axnyT3AgzrpBLiZKqxqSwPtM3uxBnwUAdnBGYJHolv4jrjc0mJ_9mjGDdhWtnMz2cwU4924FFaAJQLebnzcXuK4-7xAEghzcy-pRlfKeKkpHvu8kfwNV-kn2Kc8OulhLCDrHcmotsVoGQ4-K-wYUWVUzWlx5t_jsDWF8DWGp_YuTPW18TvVkEHE8_b3Nr9alpZAvqGZLI9OLQBU0W23bimoI_5HZItzBoiR332-aZHrIrcuprrAwTV2cZTuCgrXqVA5WoxJcsrx6KDLdxBICg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
دوس‌پسر گلشیفته فراهانی امروز به تمرینات فرانسه سر زده و با امباپه و رفقاش صحبت کرده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/Futball180TV/90730" target="_blank">📅 19:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90729">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOHokP6IgUCUlD3Z1aqb_Ncy6kjKPrpU7OHQGVt4ZHNukz2uU4oh2MISR5AbrX3fBrzd8K_16gVw1PjhyAHxyLfc8CW6BZ9wHmzL0VlC8vYCp8oFKoI-YjJqkwrfgM5bp5ate5QkWUajU0IIzHyIXPSLzgNgnsTKM2AfLnb9npBjRM1s_0M_Qy4LKkgNP6EBxsZG0oYUclV2c-_hBAuiMOa8nsiPTFQ6ANeYcdaaKM8yNEnCAVF4npmFdC8ndQryX8ab3dlSZb5qA1gigjZsQMWEMH6pQNqzzsn-w0ziplZqV4qBLyv8xyBSmXsMZ9q4LqtYOEKMDegonM6AlzqwoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛ گستون آیدول ( معتبر در آرژانتین ):
‼️
من دوباره تأکید می‌کنم، موندن خولیان آلوارز در اتلتیکو مادرید برای فصل بعد خیلی خیلی سخته، در حدی که تقریباً غیرممکنه.
🇪🇸
پیشنهاد بارسلونا جدیه؛ ۱۰۰ میلیون یورو کامل و نقدی، بدون هیچ بازیکن معاوضه‌ای، ولی اتلتیکو این پیشنهاد رو رد کرده.
🇪🇸
الان اتلتیکو در ظاهر خیلی محکم و قاطع رفتار می‌کنه و از طریق شبکه‌های اجتماعی و پیام‌هایی که به رسانه‌ها میده، می‌خواد نشون بده که اصلاً قصد فروش آلوارز رو نداره و موضعش رو تغییر نمی‌ده.
❌
اما واقعیت اینه که نزدیکان باشگاه خوب می‌دونن نگه داشتن آلوارز برای فصل بعد خیلی سخت خواهد بود. برای همین انتظار میره مذاکرات طولانی و پیچیده‌ای بین اتلتیکو و بارسلونا شکل بگیره، و حتی شاید پاری‌سن‌ژرمن هم وارد رقابت بشه.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/Futball180TV/90729" target="_blank">📅 19:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90728">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/Futball180TV/90728" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/Futball180TV/90728" target="_blank">📅 19:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90727">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibPcxACxTLj3Vd4-jAdTII42YYT-T_tuXwpoYh49B0HriyembSfb5FVjm9a2z8-WJNWo4K_33FCi5s6h2qEU3d_j3S5HheWWKHiS7ELrKG099VO5BVQKYH0bnkpy7bJO3fTrG0XnMxA-oCq8Ph76JGq2Eoaviml3-0IPalw3ucKcaemuGFxT1rXOLwcvCi_U9V-JUUNSqhX8B3UBQ-WUTczSNFpyE4Yy9rCKsraCsSTMVR1L5MWvgZRB7OVWtmcueT1PDsIO-qswRxm6ki6scHvzMM_pIQj1fYU0BO6levecFw8T-QJ7rK6L0hzYR7edIaSSYlDYUuJUBz5x1ZboXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/Futball180TV/90727" target="_blank">📅 19:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90725">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fr4SPJvkOp5PGRyKOF6svF2uC_pMtFypheBaZdDJBxT8OaOhnb_F3nMIwWBki7fKkhhid_QrVsfuLX3SLoy0dsmFjlpodpIGue-EmZFBDjL_YLz2tuG_Nh9unnkrFoPHSavbtKfJ8PAZPGOhhO_xbAZTNpEKYWXEy9sPEtAWYyC7VmSYAkwRAOf80anvfe1fwK_afpYWDyqoD7rBsb-GaYALW7NJGFZKL127tiDRZ5X3BhPj8oNcU0GnEOgOkkIHzjY4euM0heJd1ofUZTF18zu5jzF35hjWv14N7PWNpbBD4__x9gPnsHqdYlIP92oEuMbQcTSldyeky7nf5PBv6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووری
؛ توافق اولیه رئال‌مادرید با دامفریس حاصل شده. کهکشانی‌ها میخوان تا قبل آغاز جام‌جهانی این معامله رو انجام بدن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/Futball180TV/90725" target="_blank">📅 19:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90724">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAWefkdKtO9e6PRt1YirkiCfpcDiUuNgTms93frdoh0JktvJH7dBu9anMFnoBma3RWP_aVVh62GZ6Uqaiw3soliwcCoZVa0ohzifN-LA0zTHDxVuMU79fI3rEdTLWQ4Odws6d1svKxKl7PP7sV5sXzVtV-HL-_Av5hOvwbYN9VNf6VGnwvUidAZq-hxfVV5wDeNXeaRfBiG3lYOMdfc1PKpc0PKXPAJ2rPj2TvdopONsgfEBFJmGw8wx1cyT0fy8w_hPJmKpKmuRbN3ndggDZDB5fw_Tep14_hnV5QJ7WVV661lIl5_ffV4zJQzvr6GVPocv2NHNTYmUCf6a3K2wiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ادن هازارد برگر فروشی خودشو تو بلژیک افتتاح کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90724" target="_blank">📅 19:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90723">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تاج: 100 هزار دلار به مالی برای بازی دوستانه پول دادیم؛ هزینه پرواز و هتل‌شان را هم پرداخت کردیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90723" target="_blank">📅 18:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90722">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82b72747be.mp4?token=kVS5_Mw49m2tFcKGZ7sbdVeBtuTr_zKGVZSvC-fq9B1VLVF90nOI8NTdfuJy3Ojap2flx3hnJ5woEvZuyu_fIm_fta9ne9F8eXTTxgNJhKMTa8P5C-TTVNO-8qrNb5x_fdJiKYBZrxqHrjtKU94FYThkKAzAoO08Z4NnzQmvPtBCeTxrHTBuPr2gJ9HCr6-dPOWv59cUX0liVPDBzT5ukUkoXZti7ebxH_qH2SDaxTHkLxb8m1JOUBiig8Fy0Sx2zEstFO7OVyrikhvb01w3AdhQsxQuODA3C1KEIoj6ebGGBf59O53vXAqSAV98tUTkoQYE1bILsF64sAXbOI5HFKU2r1qqC9pvg6lDNKlu4cYeaq4eY3XjZLjFRJrjZVImNICu2ZeH9YU_Igfb14VeIKcpIFoPBwzfK6cKlwd-bLHqbcKFAi9u4LCcILy2gTdeT31KjtmUZKXJfsnD4wYlSHMiSwDSHyY5FgUNixGAzTRXlCmp371m377yWwOQvO4P-Yvy8bdaAcrHnRSxumOLVdsaCpIUNvvUXZLoiKDS42culn_fVV3vASYoJwZHC48xQDBGWezolxQo3BJlKABcDWp5TyTaSDZ5_zQNyCGkz1csSPwbobSDm7R7GULv8m_r90wPKclaq8VUHvOy3C0B7whNlYn5fTVmSisQ025voPU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82b72747be.mp4?token=kVS5_Mw49m2tFcKGZ7sbdVeBtuTr_zKGVZSvC-fq9B1VLVF90nOI8NTdfuJy3Ojap2flx3hnJ5woEvZuyu_fIm_fta9ne9F8eXTTxgNJhKMTa8P5C-TTVNO-8qrNb5x_fdJiKYBZrxqHrjtKU94FYThkKAzAoO08Z4NnzQmvPtBCeTxrHTBuPr2gJ9HCr6-dPOWv59cUX0liVPDBzT5ukUkoXZti7ebxH_qH2SDaxTHkLxb8m1JOUBiig8Fy0Sx2zEstFO7OVyrikhvb01w3AdhQsxQuODA3C1KEIoj6ebGGBf59O53vXAqSAV98tUTkoQYE1bILsF64sAXbOI5HFKU2r1qqC9pvg6lDNKlu4cYeaq4eY3XjZLjFRJrjZVImNICu2ZeH9YU_Igfb14VeIKcpIFoPBwzfK6cKlwd-bLHqbcKFAi9u4LCcILy2gTdeT31KjtmUZKXJfsnD4wYlSHMiSwDSHyY5FgUNixGAzTRXlCmp371m377yWwOQvO4P-Yvy8bdaAcrHnRSxumOLVdsaCpIUNvvUXZLoiKDS42culn_fVV3vASYoJwZHC48xQDBGWezolxQo3BJlKABcDWp5TyTaSDZ5_zQNyCGkz1csSPwbobSDm7R7GULv8m_r90wPKclaq8VUHvOy3C0B7whNlYn5fTVmSisQ025voPU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
🇮🇷
بازم ویدیو ایرانی‌ها برای تیم اردشیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90722" target="_blank">📅 18:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90721">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3-RkD9102olfCjuHGCvoBjY-dpYJypmp8hJk6aHp0KZP6Nh2tJamd8YQ90QQTvny3P2U0SKBzDHDS_pC_6GBtyUEJIPOhgdKQBSQiDOLoebpkpaXGKNnpBmGGMpeDKT5aZ7L4k9-R9ZEgMHrMQiI13GqkpkRlB9oIQzr4mLVDfHtLDa4cPoOs4plRH66h1SLm--ao6LHR-9aDJQxYJYoCxM7PHdOE5R7Zzk6zQpfB0v7BukCJegZIyZEUmUL5eJawHSn5a_afzFYVOuD2FpNA5_gy5RWdBZXWlwPXWOvYJkbI-wV5QRe7zbNRyUoLO1khc7QuXWHcyIGH1LRpwqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
ترکیب امروز بلژیک مقابل کرواسی؛ خلاصه که اردشیر از الان باید حسابی چربش کنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90721" target="_blank">📅 18:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90720">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IADkr8Qs2eUSWaT90fzbNLJ1OYsgX4G4izFdhHiQKpBkqjbCIpSUGlv2Z1sgXq9gOb-PlvQiJtK9SzhkdroXd1Q51fOvMu4B9oXVS85KlX5QaGv-fG1UoxDxDV2NM87rFqLNM31HJU7w5q-Z0hTCavyCVtJKYwrvoOPWvJAYhhJSpkf1_RhssQZFp4v4V-ew2gfbt65mjHTy42wFBvX8xJ6h977nRtWtYrxhRwyuhDohh6C_p1_OOLo0KH_tAY-brLSWT1C6gS5VL6IMQxzGxMwC0nWhbXGzHBGMoNOU4QqK_anEshkb4N0G2SS_8YR1Pu9cqZyBdrtM2KGbMVDSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه هایی با بیشترین نماینده در جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90720" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90719">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRQntoyXLtIryMzc0KKfkwL2CdO3VqHMe266yU6dlTWWuSElTiRtFUgiRq2YxWmPiswleCICtC6Knp-xyJKDGRE6VM1NuySuC-DXno2j_6DcN7B3rXxqSBlETPmgwLjlNsWSXOc-8yCqGIhcfEt7zdHSrIgsjJtFZ8ii-YIuC01Kh_DwbIRPUcWrajLF01Tudhi15saBmlITjh6QbMohHMAenL6QEWhxxWExlDh-O75HFymLvpc7fVwgztrHf2FIW5A_qQedOBDPPysAtn5nyc-gyF_blbCkM_r9cKsM8DuN-uUWWA9HaRY1jTw5TDdA2w1Sxmyg61IIwqbIky5TwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
اسکالونی سرمربی آرژانتین: مدعی اصلی جام؟ بنظرم اسپانیا قهرمان رقابت‌ها میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90719" target="_blank">📅 18:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90718">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNGxF2jRKlj_lghcTBEDg03UMC9ncdP-TGWzO0nWUBvr-V6KpPVtSZlbUQnXAvJl8ZxWK-_sVy56nUIcJmrASr3pT0oGfXsz4npa0nbnQuSffecbDwWAC2GLIIEJghWW0eNUE2Lzm7bMaBneEo-Am8nhllhkb0qZ-sn1_koKJp5B-EinbmZwsIlpmEQcEKFXiS-vdW9-0vTkLB0cNFQ-6DGfWUI6AUBwI-2e1e3cD9AY--UJrUtJ1HyilYe414bMlmVE1UEkX4ZqEscOxAfxyqahTGFexXjq_DKvP-BNYMzVhThZXuhRMt0QNO77gahn2dpef7QTAefbCR_aJ4XNlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👟
هری‌کین درباره تصاحب دوباره کفش‌طلا
: ‏«این یک افتخار است، به ویژه که فکر می‌کنم فقط رونالدو و مسی بیش از دو بار این جایزه را برده‌اند.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90718" target="_blank">📅 17:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90717">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b47c5a1723.mp4?token=ZmLixn1y2vb7JqbPLYfW1AFLr-8q5MQyKvpvNc3J4pYRLVXNXVfS_RL43HumNQn5qidgNjsX9rF4gBB4kCIHWv3fWhWYi0hHn8Uk98fSX9RGvLcNgYQ6UZlx6MM6X6du0pP0l20h84xyeqmMMohrfaWV6QY6mN8tncC4wGmJaZfgIZIc6sXGxXeyDnzfCyFw4yLNpD7VTYZmT0lopdmjKPjxAnq6vkRdknb7nOKZaafCaaJ7zrBCbU6shlQEJw4n4-5g4D981v4gZSa7iA5RMEKbXRgvCZcCzRq8CxFswC_EBZ4LHmcwRWjK_An7kzjR9A9WoIzR4g97HzyQsRDAeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b47c5a1723.mp4?token=ZmLixn1y2vb7JqbPLYfW1AFLr-8q5MQyKvpvNc3J4pYRLVXNXVfS_RL43HumNQn5qidgNjsX9rF4gBB4kCIHWv3fWhWYi0hHn8Uk98fSX9RGvLcNgYQ6UZlx6MM6X6du0pP0l20h84xyeqmMMohrfaWV6QY6mN8tncC4wGmJaZfgIZIc6sXGxXeyDnzfCyFw4yLNpD7VTYZmT0lopdmjKPjxAnq6vkRdknb7nOKZaafCaaJ7zrBCbU6shlQEJw4n4-5g4D981v4gZSa7iA5RMEKbXRgvCZcCzRq8CxFswC_EBZ4LHmcwRWjK_An7kzjR9A9WoIzR4g97HzyQsRDAeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو غمگین و تاسف‌بار از یک گیمر ایرانی...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90717" target="_blank">📅 17:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90716">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">علی تاجرنیا ظرف ۳ روز آینده مطالبات آسانی رو پرداخت خواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90716" target="_blank">📅 17:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90715">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5iXHd1wXI96Rrc0JUuMTIdF-LIvOwlw_FjWYaJKEDsa7zAK1KZHChV7E2A3xJpvT69QzLccXNkMwXIINEGe8yw7snAzqUQyG4EX5JJcTGSAK3xGLMelYZPn8Rb1DZmpgvxLpnrjW4UryIpG0VFT5QCtgeeXuMmp0TQgK03FmCasapLskWeUjda5zJUmib2Zvml1mErENUHRhWxV7L0GMJaMzNNsNgqEOjQ-2ySqxRiHbQn0rqCh4DKgBXt9xyKYf5Vr_NTc_R-DSVw83YJaSunryziQfXhtdkSYZmuWOTLsGL7B7rBw7SB2muYbSNy3dJd3Y58UgyxK7Hv7fhCISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👋🏻
املیانو مارتینز : اگه قهرمان جام جهانی شیم از فوتبال خداحافظی میکنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90715" target="_blank">📅 17:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90714">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-GgQO_MiscPwLchJGroEcfZIsi_aWLbfYP5l6z_JcFAJ5Dpa7EYZnw4IB-jZf88F7ABxZH3I-Jqb5sjCseT-2er3LwVbrePvSIBENf3z5xOA2GgfHquxIWX5JXPBU5dWsDOnNvaHi33Gnbpv2CKc21cqaaspEdTdu9Ok4V-Updj26qmA57aP_Hknrs9ZS8D5bZKwFdErVe2Bit2CyE35bdTzQEeln0MjgSUZZXB2y-2Ds34eObiOKeuPBFg5GP4GMkwsFzmOaSHcd1SG1C9IMKZp2ih8sMAqks43Bzjll3hnTFyMn6TwKoZBOFtt2ZTYTnbEcgYhUoYcGc2JgIkKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#غیررسمی #فووووووری ابراهیم‌کوناته مدافع لیورپول با عقد قراردادی ۴ ساله به رئال‌مادرید پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90714" target="_blank">📅 17:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90713">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe786fd544.mp4?token=IySIYBiABO-7W-mi5W9dPDNb3xfYUQYR5sYpkdhobQZLB3fUCgWe8L-K0z6-VnT4--O0uIjyVQSnEL0J04doh7O_ztCvd09cL9OkYd5fnjtr4HsFKe_hXEH1WBKqhRV6lco8QsuCygBG0Lf0eRfrPgx9zV3I6lZyjkW6gq-HN1_Gpgnf868llsZGC-y-x3NVhJHVVZCe3m_nvYcRWvdQd7GVkFXRrEffcFGkffQdTynr37BrJ1Z2JVHIvKBvRPCYdcZ4BtzVAngyZED77WFTdzCkYV9yEMNtBEvUdcgR0S6-1J0j8JwX9QM8JE_OIIqNmdxLYKKvYiTMIKGPIdJbvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe786fd544.mp4?token=IySIYBiABO-7W-mi5W9dPDNb3xfYUQYR5sYpkdhobQZLB3fUCgWe8L-K0z6-VnT4--O0uIjyVQSnEL0J04doh7O_ztCvd09cL9OkYd5fnjtr4HsFKe_hXEH1WBKqhRV6lco8QsuCygBG0Lf0eRfrPgx9zV3I6lZyjkW6gq-HN1_Gpgnf868llsZGC-y-x3NVhJHVVZCe3m_nvYcRWvdQd7GVkFXRrEffcFGkffQdTynr37BrJ1Z2JVHIvKBvRPCYdcZ4BtzVAngyZED77WFTdzCkYV9yEMNtBEvUdcgR0S6-1J0j8JwX9QM8JE_OIIqNmdxLYKKvYiTMIKGPIdJbvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
یه رسانه فرانسوی با انتشار این ویدیو از فرصت سوزی‌های بارکولا نوشته که این بازیکن جقی رو باید رد کنیم و یکی مثل آلوارز رو بیاریم!!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90713" target="_blank">📅 17:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90712">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPcnPsWhHIwmSqI9OHJse4cnUzGDc4MKuVC2MpMgVcXrPDwnyRwTlohPqPzE_cBkNYcSSfkTePBhB5OF5n7x4M5DfydWdBspbiarcHs14Lko1zkJbrQD3HsQSLEDwwuzKLEufzBwqFtujjgtqfink3LnuahPeISVWtxAk8hEf69Reay1AgOJZICVEmVp2vWO8FouKCBtp6yaska1SGZWr-O9mvHlj91gKTV_2WYWwvffEWWop6wdy9_4KGrgJsL9XbqBQhHQIYsE5fIVXKA6aowxgGajNi_MRrYTW_bgAp6zS0D6Cz52c0bf3eiiszwnTWPW0mH_qmA0JawdWshAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
شماره پیراهن پرتغالی‌ها برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/90712" target="_blank">📅 17:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90711">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQzn0veKxetOP9LYhWaBNnkJ4sQ3gIrLHrKZ2ctRqfB7aSonNm7v0sX7gRXk0Nf69o5exbcu1LCAaQB4fjshIjdNd8zCiIjzh2O6OyYP9o0FXH-GiZ_GH3stgB_9uN1-kGOORdB42rrxGbN4cb999ouA2jfjlR6eB2nkGP_kMGz_okYkZSV8G7ZUDKS9-b-vTpMIdWO5hbSkfQBxIp1GYxmHSL5d_ov5Dy1Pp-wd0TVK1H0F7t8IRzSdyBIWVFK75smjZlD8iG9E0wksn4MPFUNsC03zehRdppK9njc9lCpV835JAvwwb1eNXd7JLyUNIGN0b8t2w2hJSs_sEaJ_8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نظر روبرتو کارلوس از بین نیمار و وینیسیوس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/Futball180TV/90711" target="_blank">📅 16:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90710">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/805387d840.mp4?token=jL-G4bHJaFFWNCLdJgUA1JVCK-igTTjb1MDh_7ShTpqbgR0zC22MiRnPt2PrAi8ftiHm6ZmdetlNGc8TMUSGR6n0QmnAy5mnDV77YKHrf5ad629TUDu0eVExf8dmjFPWukhjvzHhOXRLnlDPqsg08Id80yhMKe4LRdS6TVeV3e4XgGyHaV0lDHVNvyHeLU-V5UzH3jvFzwBTKiVcWeYQpk4Ks9NeaXGtFo3l522quL8Ibs5aKGLv_633WzUJhAXwoVuoFBp8X2lq1-1_qUKh5AwvJMyjaQgUpw528svexsGvVZlvtfWMbvf9tqC-AUn2851vc_tTTq8mGFASb1drr2fDqaF6sJe1UBStu9kZXML3S8MCuvfZOFihoanRzI7N7yfQEXozdBtSFD6AZFy_RAPpR3yAjYsG5ENt1HhNPBYT7AHmZhERJbqd4mYWdgpQ75zkiED9dBBKbZK0t2PH_DcCoi75VkZjWOAtZBGwHCXLSGitD9gA-zCrWhYD6J1dNrCn1iSYML8xGxCZk-bEGwnsCMrr38nb_WNsVae2avZMxuP3CJxPK6NZa-4ImsZBKfKAr2jWbtXNfe1B8YWt1HSEMtHjR0CDpXzUr-u2ybbQg_o2gt8sAftExiehkojn04XLpNjSaEa42z0ET5l5UHVZhJ1o65wwwqrzdB9QpYc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/805387d840.mp4?token=jL-G4bHJaFFWNCLdJgUA1JVCK-igTTjb1MDh_7ShTpqbgR0zC22MiRnPt2PrAi8ftiHm6ZmdetlNGc8TMUSGR6n0QmnAy5mnDV77YKHrf5ad629TUDu0eVExf8dmjFPWukhjvzHhOXRLnlDPqsg08Id80yhMKe4LRdS6TVeV3e4XgGyHaV0lDHVNvyHeLU-V5UzH3jvFzwBTKiVcWeYQpk4Ks9NeaXGtFo3l522quL8Ibs5aKGLv_633WzUJhAXwoVuoFBp8X2lq1-1_qUKh5AwvJMyjaQgUpw528svexsGvVZlvtfWMbvf9tqC-AUn2851vc_tTTq8mGFASb1drr2fDqaF6sJe1UBStu9kZXML3S8MCuvfZOFihoanRzI7N7yfQEXozdBtSFD6AZFy_RAPpR3yAjYsG5ENt1HhNPBYT7AHmZhERJbqd4mYWdgpQ75zkiED9dBBKbZK0t2PH_DcCoi75VkZjWOAtZBGwHCXLSGitD9gA-zCrWhYD6J1dNrCn1iSYML8xGxCZk-bEGwnsCMrr38nb_WNsVae2avZMxuP3CJxPK6NZa-4ImsZBKfKAr2jWbtXNfe1B8YWt1HSEMtHjR0CDpXzUr-u2ybbQg_o2gt8sAftExiehkojn04XLpNjSaEa42z0ET5l5UHVZhJ1o65wwwqrzdB9QpYc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تبلیغ جدید مک‌دونالد برای جام جهانی با حضور رونالدینیو، یامال، هنری، بکام و سون
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90710" target="_blank">📅 16:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90709">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkxJOnWPi69M8mcSg8qaE4i83i4A1fUonKJehMVXqd3Y73-_CtaSnXgf87NBZsKpzpJKuuhWDHJjBRwHZXyvlMH8CA7F2c7Nls_enMQ-Y2owZ9YgDyvYg3r10sb7feZZqFJlBwziowV6cGtRZLkgQjFyGwtJsOyRbEz4SWs1TZzLkkcx8w2gEKnTRZmmhSG56vMXVjaj29pJAavHSInO2M1UPCLUGHZXD3Ke80ZgkZpyCV2CQfLGbrt5HlWurTC_97bSDklL6S1Aq3bJIlwum4J9k_cW2hF7LeIr7ahHN_nrmt5uBt2kWNNmM9DLTqoTNDNfCFtITq9TTem-IPRHTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#نقل‌وانتقالات
|بایرن‌مونیخ بدنبال جذب اسماعیل سیباری ستاره فصل آیندهوون هلند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90709" target="_blank">📅 16:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90708">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FH6-3A69Dpaj4cTZOegRpCFvydxe7e73kogpMjg9Rc1iVIigtj96TZJbO2BpbeAeBBVbQWNLY8H6fUBbwlAySKrhhwHn_x6nD0cD2MhorRRYGDac_YB82A7xYy-o5dq4bOO8kpzAml-iSRYzC3G2vMYrBdMMpOj_6g5VpHpcO2rwYjNKky1YwZLAtfjQIO1u57DzgPu1GfWXtNAr8qLzJMlEfPQFUAieixwYXz0xeBMPuPEbkJZUQgn6QfteSqLhXj1oVHgB4ymmhS1wZAaH2Rh8ehrVx-rxRyuK-84y8e7MH1H-1inDM5Jf0979wXOthbWjeUVwXz49AS5rYMtZbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#غیررسمی
#فووووووری
ابراهیم‌کوناته مدافع لیورپول با عقد قراردادی ۴ ساله به رئال‌مادرید پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90708" target="_blank">📅 16:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90707">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvcUt0f_Na0WMonfcZkzaQre9cJNcdtX5k0b9qXP2v24z83u93Ewnr8xTQiCT50Mp0v4Jp_E9GzW5knqY0e5-XOlwFvB77Cr0kXjiuRr5kPhKx_2b8fsODbxtbKM472pfyutdPhXuiDkhnGmBdYm70aKVEwtxnqa3Ukje0iCVYqdFrynv6HFT4Ob3Jw2R-hDe9j8Dp4NT6_wSgsytcb5ZkKKKfWqH3as56zIwvAbtgWAu_qCSe34MkuX4tSNYZoHIJkr1dVrlDgHeA1L5zmBuBsLdlMBNblRfXmUn_o95rGiKwZ-p87dw3A3AxhKTbOY4f-FSYJgNl9I6w88IFp5Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منتخب فصل لیگ‌برتر انگلیس با رای مردم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90707" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90706">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDxTbqA3XvG-dHuPTrefV8KcwffKkPPQLTm0vaBe99GUQH7HFI7TRG27LXD7DmlIyLkV77SfzRmye1AweByWX_FPzQMtxuQp51GHBsaHRqfpN1NPwpdaz2V9ZVk6iT2LDzib9MewT3BWza0duFNBgp0tLaGT7wPAfEnZ9eJDxu0c3Q2vnhb_xdJXi1LwA5bI-UY6awPTwXT_xgYVqTxTq0hG7gSG4MgEm56AUvwvDPAL_bFg3rEwT5ELCE1lK6SoPDT6c98CSiOQTndXMMUVujzzw-Tu9u_OM8TTgRUAgqw_tZO-_k2Gm7qmy1xkLlii3uhhC9dnqgasikv0Fy69Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😊
عمر مرموش ستاره سیتی هم رفت قاطی مرغا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90706" target="_blank">📅 16:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90705">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWAv0uNvWnJ8f4oSAdbspK4XLW-BO9hjrhQBSU4-k9pv4vjrHZUJnHXY4e1S4PPvGhvDgLF6wJB0Rm-LSVVKJ2hb0x7my35D6MfqCKc2ieqR8jRxUUD3BqHsKHF3qDmG-YsaOme8mt2B1gQ3wvvhYx1lZOGIXYRqiOew09QrxtT2fAWYTR0DnznK_B4gIWdw9qu1xgefFbhV7MXR71XTvJTvr9OwljBsotQ5smXEizp2zXi8sKC0LiYmifegOvxl559P-zH3YdcSyMFZat0tsMIGug0LH_2kh7BM-dFb-ZnU9zRLjO0EETgODZy25rZgrRabn30cUvmqppFfg5-R7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
طبق داده‌های سوفا‌اسکور، دیگو مارادونا در مجموع ادوار جام‌جهانی با کسب نمره ۹ در سال ۱۹۸۶، رکورددار تاریخ شده و‌ تا امروز هیچ بازیکنی نتونسته در یک دوره از مسابقات چنین نمره‌ای رو به دست بیاره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90705" target="_blank">📅 15:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90704">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/90704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🔵
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/Futball180TV/90704" target="_blank">📅 15:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90703">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/Futball180TV/90703" target="_blank">📅 15:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90702">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDA7XIveJRiSNTQqMbnXLPpAlIpDr1PQAv6j-ucjg_Oi_0fmDHaslAEJn-up_owPY1cFixMUErvVF1C23RlemFmwm45qALoHfp_oD6CYZuq91tYjqp0TebKZUMg4l27APdPQnSUTgAGrDiiHIQ7yKuH47ellkMMz1M6ehB113zATrN9fd6bIJzHv1eZufUzZLmYIi4KiBpX7U06hIihayzOWbS68qGemjiA7uB0Sw7c1QbEf76JQH2w7FSSiB5UE3SevxKjZ7YYGKVkWONofRH7ZU79SWvNwjBoO0TGLxLjSfdV97VG9RK0f3311lKGdgCHHm-F4oOEL9a7oLoJZAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👀
اتاق شخصی لیونل‌مسی در کمپ آرژانتین؛ مسی خواسته بدون هم‌اتاقی در این رقابت‌ها باشه و از دی‌پائول جدا شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90702" target="_blank">📅 15:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90701">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b52d4c89.mp4?token=HcX7y1Ln5YN7qRsUYUnx0-BpUgUwnlLNS6MfpnthV7YGAlChOYdI6aUmR3HgO0v2cicK4ldXfkLD03ISD6wdqN-AgLvhF0kX3DqKfOxcWqoug5X3ZGfbubZZ1C9X6WAtCthCCUSgr9L-BHq6AMPW9S4mTqOtq4bpGG6EOIrNOOiN-Udmh4YUiZTEJu_HuZ2tJdxkUn_OmPl8VAaDS70OWAoWiSdluQl_TVYZTwaeAOM4mKTbIx9DsytKBltLdJsQve5wjdE97ol4nUaPAJ_Np7O-CpscjUuq1TbN3omnYbkNWuab7wIh2Hnwl_eaZkNgslSVV3l1HlgwFbTJmogNtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b52d4c89.mp4?token=HcX7y1Ln5YN7qRsUYUnx0-BpUgUwnlLNS6MfpnthV7YGAlChOYdI6aUmR3HgO0v2cicK4ldXfkLD03ISD6wdqN-AgLvhF0kX3DqKfOxcWqoug5X3ZGfbubZZ1C9X6WAtCthCCUSgr9L-BHq6AMPW9S4mTqOtq4bpGG6EOIrNOOiN-Udmh4YUiZTEJu_HuZ2tJdxkUn_OmPl8VAaDS70OWAoWiSdluQl_TVYZTwaeAOM4mKTbIx9DsytKBltLdJsQve5wjdE97ol4nUaPAJ_Np7O-CpscjUuq1TbN3omnYbkNWuab7wIh2Hnwl_eaZkNgslSVV3l1HlgwFbTJmogNtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇿
🇨🇦
درگیری دیشب بازیکنان ازبکستان با بازیکن کانادا بخاطر تکل خشن!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90701" target="_blank">📅 15:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90700">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pavh5YPBqcENEAvAPthc5l-QINzw4LmyqWG4S9rVUBthrObI2e_z41rGMGgs4743eHBAOFFShMKjFYzd06Z74AZLx_k1z_B3KG8lBLvwvKN8lMp7PZ5pAApyDrR0_pmuvYRQNfVVbzZUWqJokzmSMOKwSSsujx9aNG6bWHMMP1RecCoVJs1dYdyojiJwt7SKK9ftpBK1WPviLETesxek-U7BHDnTDry7wJ4N146r-YT9rtEYgTWjR5zepL4zKqMmdgKjQYHjFd1jbTBY4l1KL-wMtRFOrcL5CsxfxSJ5cPzjH5CQZK-fULW9T5e8H60RZN-3dsUGowGSElGwF7A0Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
یادی‌کنیم از سال ۲۰۲۰ و شاهکار پدری در سن ۱۸ سالگی که تونست طی یک فصل ۷۳ بازی رسمی رو بازی کنه و قیافش به این شکل دربیاد
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90700" target="_blank">📅 14:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90699">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cab41e786.mp4?token=laWTSEP_uTDwWmXoi7pHOdK9GKid43haTNkZyclOiOEbaaz1UXFpyiNR2eCuHM-mi4TYYlBN1vRX9FdaIGp1S59rT6ba0S3h4aFFTBUaSkXxu1X23KFO_e8X5lYtkKEzybZuWE9m4DAQkJ66bcUen_q472LFotYnIEjpS364zrCMnEGR6CaXcW93zBiYcr-KOyVg7PmvdWcdVFySeZqZFh7NIDMlyy1Ag7lnOee9L1uRLjwhr1lIWdenqAilUaQJhJwaT0X05Y_Cceo0RmIBLiViCeR6_RrdDO4D69NdEdd0bTgJIiMhiTxhBd1DXgjAlSe6rnTHM599AYQlMUP8Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cab41e786.mp4?token=laWTSEP_uTDwWmXoi7pHOdK9GKid43haTNkZyclOiOEbaaz1UXFpyiNR2eCuHM-mi4TYYlBN1vRX9FdaIGp1S59rT6ba0S3h4aFFTBUaSkXxu1X23KFO_e8X5lYtkKEzybZuWE9m4DAQkJ66bcUen_q472LFotYnIEjpS364zrCMnEGR6CaXcW93zBiYcr-KOyVg7PmvdWcdVFySeZqZFh7NIDMlyy1Ag7lnOee9L1uRLjwhr1lIWdenqAilUaQJhJwaT0X05Y_Cceo0RmIBLiViCeR6_RrdDO4D69NdEdd0bTgJIiMhiTxhBd1DXgjAlSe6rnTHM599AYQlMUP8Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌کنیم از روزگاری که مجریان و مهمانان ویژه برنامه جام‌جهانی صداوسیما برا خودشون یه پا جذابیت خاصی داشتن و کلی مخاطب این برنامه‌رو می‌دید...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90699" target="_blank">📅 14:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90698">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJ4y463bljzHUmT0dBDAf5UgR7Ys5ISwZTHy95n6dubLJhv81jV77FrCJKQhFi5qpqsfLZByoLrgTvmjqvQ4HeW2V3VaQc-_xC7E8A-6g8oIMiUVmwmy5NWKI9Y3Ph6jG5EioZdOKWxarAP_D4rBM19a4wL4PncOVBDV-5_Pw0tGX0vXun1juWaW7JPCH5AkB9-qs3xBPuwgTv8uunQ03cbygBPQvuP_P2fxFzsVNmkms3pLc32ZwO4QFwqPQJl285SubxqCadi7BFuVroqU5oDIcaYrMm-7y_VUlWi-I58sonS4e1k9D2CMp3c_lii36KDM_5_E2NP_MnoGfOejIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
🔄
برترین پاسورهای تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90698" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90697">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/Futball180TV/90697" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🛑
تنها سایت روسی فعال در ایران که درگاه ریالی امن داره
💎
شارژ دو برابر با کد هدیه
IRANBET
برای بونوس ۲۰۰٪ این کدهدیه رو وارد کنید
آدرس سایت فقط با فیلتر شکن روی سرور کشور های آسیایی
👇🏻
derbybet.org</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90697" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90696">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REPtvDgWqCiAFjY86aLlHApG8-bd7GBroso-sZ58bWpFPC9kqEVx1PVLu6sHj-CSEGxtvNGvD9MEGAqcbbd9IYhZGRDT1XU6IyMNEXeSAJcIdPMa--SJMD1HB9iFyY3G8aYLK5s_Ogi29xTqhhh7GyHAltXkDNiylI5xqRa88WRJYuHi2ORWduYsxZhvPgCz49b2h3sVfQSwk9vUP7CfnY5ozBACN77XMBxFskKKf6MfIAA1YX_h5Moqm3gkLKoFQUE5U2mPl79D1IohyKX3HQzq37II77tkaVxbB_Q5MbOu7cIQB5c0WLC9SvxawsXvk_ASSzNc1EK6e1t_R3xCmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
Derby Bet – تجربه شرط‌بندی در سطح جهانی
━━━━━━━━━━━━━━━
🏆
دارای لایسنس رسمی CURACAO
💳
شارژ حساب با ووچر، رمزارز و درگاه بانکی مستقیم
💸
تسویه‌حساب سریع، امن و تضمین‌شده
🔖
آموزش گام‌به‌گام برای شارژ و برداشت
💎
شارژ دو برابر با کد هدیه
IRANBET
🎁
100%بونوس هدیه واریز اول(
شرایط
)
🎁
100% بونوس هدیه هر شنبه (
شرایط
)
💈
آدرس ورود به سایت
⚠️
💈
دانلود اپلیکیشن دربی بت
📲
💈
اموزش شارژ با کد ووچر
👉
💈
اموزش شارژ با کارت بانکی
👉
━━━━━━━━━━━━━━━
همین حالا ثبت‌نام کنید و تجربه‌ای سطح‌بالا و ایمن از شرط‌بندی داشته باشید.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90696" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90694">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkKM7r-FXArisr53MMG5snlIr6Nn-snWWeyxwSHfE8KOH1IEm7QOoHVExRrGVWZ96nQdrAPS_72iI1CEJCGlvKwb-I9R1X3sD2jTBzk3wv4gmUHUKt-ANdqK2htbecxQq97eH71sHe6v-xufRVfPTz3eA3ALSBxUFtB4paw4z1G5nUmr65HjWechWDONt1YW45fJK1DYR7xzQGRgJqvQ6iPjMlHOTf8y_S5cdx5O_WUj1_XiaaSP_bstHMQGuyQbzLr60V-BV7hBBK9p4Y-DD-iN4ZXnoWYzw1YMzUbsX7GV8kzRStmKwmNra4x96fbMwKHZBop-ERMjs3-FTBDLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🏆
مکان کمپ ۴۸ تیم جام‌جهانی در یک‌نگاه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90694" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90693">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری؛ کارلوس مونفریت خبرنگار مطرح اسپانیایی مدعی مذاکرات بارسلونا با اینتر برای جذب دامفریز شد. ظاهرا فلیک نام کونده رو در لیست خروج قرار داده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90693" target="_blank">📅 13:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90692">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuuReujj-MhfcNn2dRK0jfwd6GnptD6pfkkDHjWfL88RhHPBPdQ819kC3B09mWqPHXUlHtkXWnLSGS0rK1ne5IadmQWnGYBsNHeD4nfBJ7G8YwPED1O3Nm0RPnZpqnEJHUrHNaLdBo99c-LqXCUTWqkwTUTgQcq96qHEkFgetA4HMGYDYwJ2D3SiU3AKLxmRs1O054_ynlRAcGaf5q1LHjl0_PicMOatNHOLPoq7E2CdTCSerRDpf2R7TyyLP3QUdqjlFgXbxs8uRd_yQtAQI_bc_6S3qt2hNmVNO8xlah73v2ISnotPG2F0Gt0ZwfZvWTChFKqoBtaNHezexKgHZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
با اعلام رومانو، بارسلونا با پیشی گرفتن از رقبا حالا در آستانه عقد قرارداد با برناردو سیلوا قرار داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90692" target="_blank">📅 13:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90691">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JW50aFWr8ij5270_hUKafo0GZ9RHWk-RGCTKXYlYYFodcwiK_j29euBNLpOTcdWGFFeS4ta-rzvZB6XIiNTBz3ti3dCQ3QhQ7kp1GlUYa9RGyEFdfy7s4RpPNNkvEuzTNwYmim8FIeYSP6Nu4TYfd7yWU9K4l0aN_czolfyjow3rABpR7jCfWTn-dKZTbwvDbQNYpF0uY6-YvKNrpvcaKQt9GbmVnEly0evGDIatS6Q5bFB97bFWFgQDj7xOKyq8gkijiCa6O4f8rAylUHRjMXuTLJPuTl7hN79wS_7AhY7YZBJV7AQ6W0y8AuiUVobKJqJ1KluVEl0pJq32i55qJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
مقایسه آمار این‌فصل مثلث هجومی psg و آمار لیونل‌مسی در سال ۲۰۱۴/۱۵
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90691" target="_blank">📅 13:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90690">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2IZK2AaFvJELp-xD1nBuQN7G9UN7dkGXE50LlWrP8itMGkf7sEmz6BX-wc2RIfVv-Z23Jcgu0yELR9CFfVAWeWbtJ_ms9Aa1rVujDT-1BfEAJ0K8-Pow6ZaP5GjxpwXofeu-U0t2AuB84Si4efBc_nALyDL_Ok9nNa3qt0TiTtm23GPqWtT3L7WnI9mgAZTYxcBQtIsk-efVMhysNnJJnYsUgquu8htxZhyxEqHbb6afy285E99tb4pByI2aO_TZVKTVoWOBOezBS0P1Ih99Es6SkMF31LDuGfr5fgTfj_HF6fnHzbi-4xsAE6E8EHUqBCKXeZ0YzLMyWCEuMmKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇧🇷
نیمار و مامی در حاشیه تمرینات برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90690" target="_blank">📅 13:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90689">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
🤯
💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری؛ به نقل از AS، آرسنال به صورت رسمی درخواست جذب آلوارز رو داده؛ اولین رقم پیشنهادی توپچی‌ها ۱۵۰ میلیون یورو است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90689" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90688">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9DSqRQOlSfWczAFAEzHpVRlIjWR7FHzPOFVzDjZ0dKlbdm-0xdA1a7vwmGHZKTClW-8Dh5OWmFLAIDKYIFa_CZkitrem01CF2BW0gJimr7WYO5WzEQccfHmL7Uh9MFjhavRnS_sGUxj3vA3114CNdqV2b6XRdh-de_HTTuOMrp45X5Te8rJJluf8_uBYP8RYqJAxNjfvyqWktcr3BjZ4vWKZt1dU5swrCwUKl6RbKAIz9htvG6QCndvlL7FtK-1ha9czLZnrTBrHITtLZ3rQ-4vtNQPXCseqnU5RPss6FrhXJRj6Bac7R-Uzs6nIZKzE7inYJ63xEFHfL9JjDspZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤯
💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛ به نقل از AS، آرسنال به صورت رسمی درخواست جذب آلوارز رو داده؛ اولین رقم پیشنهادی توپچی‌ها ۱۵۰ میلیون یورو است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90688" target="_blank">📅 12:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90687">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EW1pt7f_eq4HuOwWjR82iWfRL7gHokOoXH0sZ4Y-brrCELYrFbBrgIFZF58o6J3i84GZ6TCx3B0LEUek6R82segD52bY7m2cPr3R_tjxMWND-J6NaIjR1iRxWH4SLGKxu72pnOq1itSvWSw8t8EKU04Zdjs3svAixugV-A3MQRpXTWq4dVS9f3Nj0hp_68V3DX0CcscgDWKGbgTcivDIwTpiI_4m1KAe1zz465ocG4iVWrIZAmZciKvenpQYPT9fU5RL0rw-QWuD1TpI6Di5dwOzQQZ37-YbTTDkTJZUYC_39KrnWiHtt0aNjlLxWWfbYpytN_5GWQdeaHG2CPOdSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇹🇷
لیست‌نهایی ترکیه برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90687" target="_blank">📅 12:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90686">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aad5b7d29.mp4?token=X1tSfSNicfnS0yFCtg7Co7zIncSmh11PS2wSCgus_YRUHP4MZDwVx8o-7eMmF9zm5iT2vX9JS8sSrC0knC728oqken4ENOvy7Lr2swXPbVPN8o0qzNv4uD36yOiQganlHIpCp8cMUeFrmff-SWGnws70hVJo0_KdWNxPZ4rsbjwTjQIn_49WHaYkPF2J8YndnZche2-GeQkG5X_Vt7bgdBxB3oSJ-M7VwOBEY5Ub7SrXfPCHIrKwKNcJawTSo0gTvmnrQLcUoweX2cUS5YNo8gRoNNloaIbvAALautqMyv6rnj_g32Kvrmb6FuvILHTzPoexdvUTEmpl7uZRIVHO_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aad5b7d29.mp4?token=X1tSfSNicfnS0yFCtg7Co7zIncSmh11PS2wSCgus_YRUHP4MZDwVx8o-7eMmF9zm5iT2vX9JS8sSrC0knC728oqken4ENOvy7Lr2swXPbVPN8o0qzNv4uD36yOiQganlHIpCp8cMUeFrmff-SWGnws70hVJo0_KdWNxPZ4rsbjwTjQIn_49WHaYkPF2J8YndnZche2-GeQkG5X_Vt7bgdBxB3oSJ-M7VwOBEY5Ub7SrXfPCHIrKwKNcJawTSo0gTvmnrQLcUoweX2cUS5YNo8gRoNNloaIbvAALautqMyv6rnj_g32Kvrmb6FuvILHTzPoexdvUTEmpl7uZRIVHO_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
⭐️
یوونتوس ده‌سال پیش یه ستاره‌ای داشت به نام آرتور ویدال که اینجوری پنالتی میزد و رد خور نداشت سر گل شدنش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90686" target="_blank">📅 12:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90685">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90685" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90685" target="_blank">📅 12:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90684">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6tkA-q6Hqpi8NcIfSmFP_-kDeEQKkHteEglo4wWBelim3-_Sh6vyEdHw7vZZglaY8O93ablJPjXfvZGEKSyUKw4oBhAuNDZbnqIZ9AN1XWxrRQnpzRW5lNd1dm_J1L57_HompWD8jRACh_YAmzDPQNiihgmycSiBoa3ZKv3w-GcG47Eu4ifshcqzQQgfz85HxHC_ILI6FVxXiebY77Pv1bQfsKpxde5zDquhlj5RWAk4R8DafJz8ZVVKXxhywGh9bi4GPJ15j-sqII0_INLE-fG8SCPvNvK4mGubaDqO1xL8L_ifTk5ZFHChvsUmQVNT2isgc3PuiO0NLqcSJEPsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90684" target="_blank">📅 12:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90683">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2AQzWC-pr9fyYMw7QUg2IedOvlAs8cyyZiryRjHViQxnUDTxGy3QUYhvtrNREkcXAaxORse_Sbt3yQ5F6DVU9H4s2Cm66PujOGG32wQeD158f1b75gGnr1cGqgAldQVr7cq1H4bEL6qXwdxpMk9KmyIRegQ1j5kISfdYR7BwZX3ViA83sj__DI4-E6fYc_D9ERNPAUod5fGsv00-LJVcp1V9HEWWcV-e7wNeqXCKPT5L-OziGc6fsatTpbhaBEBl2Qt_Sk1nF0vBH5k7AkGi9TeCLiY16ZtBY3AKynUbFo-i6mKh0EAw3ijmWibN8O_phsuCnOfXEzzwT-zA7pWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رومانو: آندونی ایرائولا به عنوان سرمربی لیورپول انتخاب شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90683" target="_blank">📅 12:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90682">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmvwzavGEvu19_TWztWIszw2u6LT3SSlFsvS-4DTorh0WAMFJY_yMTnORXHTlGCUy7ryl0FPrDGc-kr2Y8maYcgJARFE0_ZzTZKX5tSu505TcrRwXYMUd7K4usDgI7OZFBMDGxnsEfamBfne1skn97yejAxDZ8eoAFpzctBpHrzUpw3oFdtPsCJKJhGUexW-nISNPHnIJ3OVcN5FTvVnS8NC5zAVPsZO-s3zbx7Xkx9-PyZ4kN0erFsG2EHFRpzlSEetFCrHotxirJgEQju6Miud26ADsYDAvfMikbXXJ7R8Jegs_XL3fTuFMyqae3KDruyfWMj0ETPiAWgatGRy4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
؛ کارلوس مونفریت خبرنگار مطرح اسپانیایی مدعی مذاکرات بارسلونا با اینتر برای جذب دامفریز شد. ظاهرا فلیک نام کونده رو در لیست خروج قرار داده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90682" target="_blank">📅 12:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90681">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866da1fdc1.mp4?token=aw1e6WUgaI8THBKmZu-VtqMXK9GvdHu1yWP7bko7qNZd6XiMzh3dK6u1YA5YMKejPVW52vBFSp3IDEWDRidIHSraVJMXyy9l19XjhDKXp9zIfFgjXs1ALCg9fuH4c2lV4Wur5B320TKgOwd5VN8oZ1qT4HJrbQ5R2PA9E513xUHbzX4LBKrzWqcxdIPofdRvxYFhMwOWAcGFrmRD-zK3P8CdpBPNmme5VNtqZRF4lyNH45uvjbHU861fb9rdInBxnVv2G1fv0KNt9aajuKE6TiL_q7FaXuXRrum5vtj3m16L3XYraSImVTm1rr_AT73dDnCKpzf4W9LeFRnHs7hAUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866da1fdc1.mp4?token=aw1e6WUgaI8THBKmZu-VtqMXK9GvdHu1yWP7bko7qNZd6XiMzh3dK6u1YA5YMKejPVW52vBFSp3IDEWDRidIHSraVJMXyy9l19XjhDKXp9zIfFgjXs1ALCg9fuH4c2lV4Wur5B320TKgOwd5VN8oZ1qT4HJrbQ5R2PA9E513xUHbzX4LBKrzWqcxdIPofdRvxYFhMwOWAcGFrmRD-zK3P8CdpBPNmme5VNtqZRF4lyNH45uvjbHU861fb9rdInBxnVv2G1fv0KNt9aajuKE6TiL_q7FaXuXRrum5vtj3m16L3XYraSImVTm1rr_AT73dDnCKpzf4W9LeFRnHs7hAUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇲🇽
مهدی‌تاج: ما کاری نداریم مردم مکزیک مواد فروش یا هرچیزی فروش هستن
😐
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90681" target="_blank">📅 12:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90680">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qw3buVRaegPUwq9VHNsmWGAhDNy-jC9M9axH9O_bW3IbXf-2JD11fdr_4yKY1PZShIeQ5xCYL85YlgX7Yy4IRH8ihZi-JNke8kGljQoQMXWzTWlOhImQM-HwJuu67uctVS8J8uu6CkV0zNoU1Iz6aerT533xfn2ZIINhJbQvmFnCayd48-LRAt77rnZM7sG5D2OqNt_PBJaxf-sTP6njm58z4CiXvL4idKWrVEDoOeGAUjC6C5EpzBzwGS1z0CsvmNXOLiuUN7LE-P2RV5Imc60-D9dCseNszRWnf5rqTwgkt_7fd2R2IRNywrwS60_Abiw-_e6CPv4JYmuBIHFf_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونایی که جام‌جهانی رو از صداوسیما دنبال میکنن باز باید این دو تا نچسب رو تحمل کنن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90680" target="_blank">📅 12:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90679">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8766b7f17a.mp4?token=oPDj9UW5CKgpULyiPuugo2mU7NmyR3_k_1e1sMy-bRmjTRfG2dMClcKgiFurZoARIEqFOCN9mr7CFkUBbnvxXo9kd_xyl2R8aoLIw1_5qPUczYg0yiv24ptNilwFeW15xdmzzuesRRkQqXo5nhILoVE44WGwWtJSx-gZArRjJJd6zCidbQR9IP497FBKMHDrgdO2mfB2qM37zLoeId9V5Fm4hQ_OxgYao3B0QX9FwF0xCuMxNzzTmoPB5o6hCPe1qI8GDpxxbwDb_fMZs_iNoDICVXttE9PQDusFFNewvlaEN9qT5Bzzk7eGPW6-eObZz1HB3I920wtga3Eqy1pegA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8766b7f17a.mp4?token=oPDj9UW5CKgpULyiPuugo2mU7NmyR3_k_1e1sMy-bRmjTRfG2dMClcKgiFurZoARIEqFOCN9mr7CFkUBbnvxXo9kd_xyl2R8aoLIw1_5qPUczYg0yiv24ptNilwFeW15xdmzzuesRRkQqXo5nhILoVE44WGwWtJSx-gZArRjJJd6zCidbQR9IP497FBKMHDrgdO2mfB2qM37zLoeId9V5Fm4hQ_OxgYao3B0QX9FwF0xCuMxNzzTmoPB5o6hCPe1qI8GDpxxbwDb_fMZs_iNoDICVXttE9PQDusFFNewvlaEN9qT5Bzzk7eGPW6-eObZz1HB3I920wtga3Eqy1pegA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
🇮🇷
🇺🇸
فرهاد کاظمی مربی سابق لیگ‌برتر: وقتی شعار مرگ بر آمریکا میدید دیگه نباید گدایی ویزا آمریکا رو داشته باشید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90679" target="_blank">📅 12:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90678">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9866c6c42e.mp4?token=otCf_0em8UjisZfw-yRRu1vIhRcHVMZ5ghCdAU9hjtA5SlJ8Hw2g-jHoBOKJLat6dyYGYzrIT3yZfnmcMLRp62KbV-iuvsT9Xr4ICKuIu2s9BijbZNcspJYsXPMWwqeY3OdXy5lg4_CC-b0JETah6pEOb4UB1_KEi7aLNYh7Y7VRlTLT2ZsnjbsopCOHH1vHgNqwHNkWKLosVVaswRirioo1-G4vgM3eKp7L1pXr5pO_AX4t1apmeqHIF2JXoiq-Gj_y0dhRPPacr8KLs4aqyujV_wrW5ip37tY86LYEbogRHPNZRgyZrRqUforRYIHHcF5jE-1QXfA8zkiL1WpvNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9866c6c42e.mp4?token=otCf_0em8UjisZfw-yRRu1vIhRcHVMZ5ghCdAU9hjtA5SlJ8Hw2g-jHoBOKJLat6dyYGYzrIT3yZfnmcMLRp62KbV-iuvsT9Xr4ICKuIu2s9BijbZNcspJYsXPMWwqeY3OdXy5lg4_CC-b0JETah6pEOb4UB1_KEi7aLNYh7Y7VRlTLT2ZsnjbsopCOHH1vHgNqwHNkWKLosVVaswRirioo1-G4vgM3eKp7L1pXr5pO_AX4t1apmeqHIF2JXoiq-Gj_y0dhRPPacr8KLs4aqyujV_wrW5ip37tY86LYEbogRHPNZRgyZrRqUforRYIHHcF5jE-1QXfA8zkiL1WpvNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب خداروشکر تو این مورد هم عقب نموندیم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90678" target="_blank">📅 11:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90674">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HlQZ5RzVtXwCl9dQQj0dTY47CtVGqLssRKuHVCoToEe9_G0nJZ2X5vw1C7HXE0vBQsoIU1h-C_k4c6BXQ9R4oOXDiWPUWGyoIeHJF41OD1ujv4-wgiTe9AVtBnjBDlPJnfxkPt5PLEN-n5JjCkn9kU2KgVIyqB38uwMdjaUu-i_tscy0DSIhR89cOG_fgs03O__hHc8E7b-_o5nQZCWZsnuRxEYo3vXJxV01jH0VQ8mLt-aADQqnvLESZlybtzQQJLLLkA_OeODQhkDxrEvBn_AAHaAcjAoqnEWXoKhv8SPcbIumOnMsuGuMxgeJfW6hG24F_Na9GsdlR2GCaNABPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TjGALmm6xHR0j5srQPFiSDg0sO4Xt6ovvLQfy7dENkQjRQw6sBIZkkP6f6GxDXfygBPvC59v4Aw9nG_qgEud7eAEwVumIhmGE4mPfaKkbqCHmkT1wHp4UGmvfD9KG689Zgs6EnWgTSAmISmblSvugY21U_JiXt_qNFTtLcDSGcs--HHIg-1Mv_XyNWrFYSZn7Oy_kl6q89Nt9tmMeO0BPhq510tuLW4VDGT2t7g3HTe4rtcgsVUaTvVzG0fSGKBzkbjpJO1vmyJnce4zmy94EXuZ4EIabZ56Fp-K6pU4GlC-fun517HBPLl4hwU-YTjcQkJpHtI2FwXDPgEfhFVgbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9-c2KtEdGgqpF8g6LLs9zpdF2g2FC0MQ6h7e11rCML_86S61JvEBRTPk0-vohz9Tzm5d-SjWwnz8NgLU8HN-hBDgXEt9PcZqGY3Q8Ot-BzcOE28n6EfSd-XWXbu0sAsnQyX9NaqHyocDr8tpT4o8stNDrXjDn1lwF0kS_6U97eSAa5IUrEF607hze1FJR-TPSDrZr5d4togtEZeiJFGh6WJB-PlmBbrVqCx_Tp8SWpkfw92vTF5EyKD8IkRrwBUMjmdun3It-fInEjcFbybjDBWGnGIRpgd4K5dBmP68LhrZSjYFL6jPnXFkkKkFIftcTVDOAK97GQIPVo4mYFxcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSVcGjeSBM0wm4CUJXXgXlyevVb_m2R0wHd4gkFzDMVCUm3dDBJXfTNOGJvJ6gmpYiNWMR3NriAdEovPM4stT2NNmuHXWzFogCd7aPf9Ok62gzYLxwC5Co9CwXtBQ5bylWpomET8NcRJNLUNBp33dSM7qcal8CGhPmHLmTtrak3oFVXS4HYBo6XKmwfaNTVcItFLvltPcBCRosRkPLKsBXivUluMT7RWjckOgKULXP26agvAYR9B42LP_J7MLwXFKfECBhgXYXqQycvTpgki0b26a74Wm1iA9luxbWCvB82Hj82K--czw8b9K51nsBBw3saeoInqTMn7VsK-AmrP6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✔️
آدیداس از طرح استوک‌های جدیدش برای جام‌جهانی رونمایی کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90674" target="_blank">📅 11:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90673">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291786993.mp4?token=e7H0ffQvLJuA94xyv7cZ6tY5GIby2sFBdxWq1g8a6gr2-NMgkRZe7duvHJPSlL3yxj_q6_PWFLA3hRf0Dsb2vTBjRB4UDvIFGbyz7NwfFaKCfQxFoCen1RzY0uU39wGelFagV7RkfRqSry_ALixiTSYPOpwqDPyTiZzFu6atmcJp6KUd7_xlD9R6KelyucDpRdFDRLvt02GU-HzDKOpTUWFzbuwD5_treFnRO96D57sm4x3C1A-3541wm3QCbGlzq8AcqzkA_T0IU419briBK7WzZGrztW3a7iiXx8eWY--MddUiJ9sg4umG8Bd58_wR3C7kg7umyTZeXmrqvH24ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291786993.mp4?token=e7H0ffQvLJuA94xyv7cZ6tY5GIby2sFBdxWq1g8a6gr2-NMgkRZe7duvHJPSlL3yxj_q6_PWFLA3hRf0Dsb2vTBjRB4UDvIFGbyz7NwfFaKCfQxFoCen1RzY0uU39wGelFagV7RkfRqSry_ALixiTSYPOpwqDPyTiZzFu6atmcJp6KUd7_xlD9R6KelyucDpRdFDRLvt02GU-HzDKOpTUWFzbuwD5_treFnRO96D57sm4x3C1A-3541wm3QCbGlzq8AcqzkA_T0IU419briBK7WzZGrztW3a7iiXx8eWY--MddUiJ9sg4umG8Bd58_wR3C7kg7umyTZeXmrqvH24ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بدل‌های کسخل و ایرانی مسی و رونالدو:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90673" target="_blank">📅 11:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90672">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJfxBsj_qN5I5brmQIruvpjrDXqyC3PVfvVOTEtdQv9OT53bl8nxCdFg8ouk-UPAUtg0Ja1GDDE-QY64YQy7eysZd3cVEH2oNXMRZ8Q-PMpeJGeqEwSoC0gH-aOI5KDmKJduSCEzlOeSotkt1gCS4wWDgjQE12XxWeY4aGjvTkHKw2RlsMoVCtG-pESErId7aPwTp46c75MELSsh9F4AwP8PosxyI9IEzaKVEpTNpcMVpvmTapXeBb8H9UZRr7wN3umSjuDufMFknr_eYSel6MISPl5fSgo2vzYruHFKI0kZxZW7TWuFh_pGEyNS8rY1-j3rEcJLgSKZiFK9Ji0gbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتوی سکسی گارناچو
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90672" target="_blank">📅 11:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90671">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c911c332.mp4?token=buGVXSiddl7LNvpnGwnmQfvFjex18Ur0dfmrw8mYctGUeim9QI5vK7dUo4RchydNHr3_b57oRV6l2iheO-opq6HYLmVtZbwkinNaERkVMPn5u24ZgD-F5jMV4edQntE5NgPHppMvIyzLmwzL4x72YntwaTbBch8JIGNJe-bpnSxc8BswGI9Oj7Uf3cuqt8MJCsjOnNiBYgh6_f7EF9MQZb5XF9mEuNNX_E1A-FX2vN_kErEf59X1YRfPn8jNDoLv6cX5IQ9TlhHjRFWs44RsWkz2Tyi-FLCcLL7Npcp_Oy6Ye6kKg6a1Dq1R_X2zwyZNs6syrdhuh5WGrORuW4VsxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c911c332.mp4?token=buGVXSiddl7LNvpnGwnmQfvFjex18Ur0dfmrw8mYctGUeim9QI5vK7dUo4RchydNHr3_b57oRV6l2iheO-opq6HYLmVtZbwkinNaERkVMPn5u24ZgD-F5jMV4edQntE5NgPHppMvIyzLmwzL4x72YntwaTbBch8JIGNJe-bpnSxc8BswGI9Oj7Uf3cuqt8MJCsjOnNiBYgh6_f7EF9MQZb5XF9mEuNNX_E1A-FX2vN_kErEf59X1YRfPn8jNDoLv6cX5IQ9TlhHjRFWs44RsWkz2Tyi-FLCcLL7Npcp_Oy6Ye6kKg6a1Dq1R_X2zwyZNs6syrdhuh5WGrORuW4VsxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
🇸🇳
ویدیوی جنجالی از بازی پریشب آمریکا و سنگال که شدیدا بوی نژادپرستی میده
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90671" target="_blank">📅 11:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90670">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=R0spEo07s-hO-ztBQdqanCF2CBlmrthjalKHDH4MEJHhN6PZXq5OX9FsB0A9L52SnfPZp8MoAJ4H0dU2mtYoj45DEMJwHlFVA8Pn0zy1FIr-8KtBo2p8rJf156P_vThjrwx3pEYSfljpA4cEFQfZnXkcgcvSAWAV07idkIwP7_INpUhE80b1pf0z7OZCQIxA0H6sHF1Fd3X5q4Anqy-hIKq4Vkup_T2wNZutxfeSfJYJYRKqwyvZ4k35QpLqJg3sxnJ0CudeVUbP8jKoX4DQEJ64WVnyji63fB-PTu3MicldH3uXJ3ah1NyQ8KFdIrAfcDWGQCMOM0Ju1dg5XM2CXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=R0spEo07s-hO-ztBQdqanCF2CBlmrthjalKHDH4MEJHhN6PZXq5OX9FsB0A9L52SnfPZp8MoAJ4H0dU2mtYoj45DEMJwHlFVA8Pn0zy1FIr-8KtBo2p8rJf156P_vThjrwx3pEYSfljpA4cEFQfZnXkcgcvSAWAV07idkIwP7_INpUhE80b1pf0z7OZCQIxA0H6sHF1Fd3X5q4Anqy-hIKq4Vkup_T2wNZutxfeSfJYJYRKqwyvZ4k35QpLqJg3sxnJ0CudeVUbP8jKoX4DQEJ64WVnyji63fB-PTu3MicldH3uXJ3ah1NyQ8KFdIrAfcDWGQCMOM0Ju1dg5XM2CXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇧🇷
صحنه پاره‌کننده از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن بود
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90670" target="_blank">📅 10:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90669">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0777399bbc.mp4?token=pLePQcrtTnj7gdwAaUYLgat6I5lVdqDYAzhtDbul7CpeOKLW1xP3gFAnZiWERhhiNoMSCgIRmGZqRDQxHAqkdhTVe4V-CbLV8HXfmkRv80_UCiE7qVebdg5Fk2YxJAUKspPaY0gBaCaWK6ySPFZcUf7U0qcpf9ZKnTrj4GbOuy-LkSxH3hosMlK-fKKuDhMaPGSKLkBN2un5sHbCwAhjtwJoxeL2ttIRo-MIDKWYxSorB7LhPB9qPQkzDsGZ9RVZMoTNYAulpXZaPNW7hBNOz5fZRlvvCgmoSSBsGT6heRTNZEcFs4VvrkpTjuVOKp5-dSelZIbFpzEgbjRfwjpPnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0777399bbc.mp4?token=pLePQcrtTnj7gdwAaUYLgat6I5lVdqDYAzhtDbul7CpeOKLW1xP3gFAnZiWERhhiNoMSCgIRmGZqRDQxHAqkdhTVe4V-CbLV8HXfmkRv80_UCiE7qVebdg5Fk2YxJAUKspPaY0gBaCaWK6ySPFZcUf7U0qcpf9ZKnTrj4GbOuy-LkSxH3hosMlK-fKKuDhMaPGSKLkBN2un5sHbCwAhjtwJoxeL2ttIRo-MIDKWYxSorB7LhPB9qPQkzDsGZ9RVZMoTNYAulpXZaPNW7hBNOz5fZRlvvCgmoSSBsGT6heRTNZEcFs4VvrkpTjuVOKp5-dSelZIbFpzEgbjRfwjpPnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید هم واسه جام جهانی آهنگ خونده
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90669" target="_blank">📅 10:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90668">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCDYBGy05l5O5yUVtJGHhbg5C-gFVPY3LdJUjDrnDyrHsFQGvPaAnbhkj8AP2j7h0fpgFnPr7tH6Ub0r99sd2yCEm-R_3mFfjZ83vliOARmAEVSgFDM0CPpCECwzqMsC18-N0wPAnK3SMaO9tSQlnqzS1JdUXJhZEWZ0NLQI7PQKDd-zKwhKHYL4DLan_Jyd3CF8XTVxorZrN5vp1FVkVp3alpZRtfMhCx5yZZI-uYY1rAZdiJeK_wm0vUTh9tlueF7yoswH-zahMrWerrWhABJW7aO6A7njJljv6JSzhRaJQWOw-tCKMrWmn6Ax4RoVs_XR-heTzpdZPkX5EfR_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌اول چلسی در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90668" target="_blank">📅 10:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90667">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oS85ZD1ccNACCxOQVjn2zAS80h6BwffJmFR8kTpdrt5syL9GTggE9Fxz_WQbodGe0cpJoSEYtzciQ72WrfxH5JrndQ2vx11_c4nxyqunRFTPcXPZ-gervTrhHYlvsVsS5HoPxt_pwD_IsdIVtNK97gp9iXq5OTYA9tnYa1exMX2ZXCktK1b-P-EUkyP7PZj9dwJe7j3BnynNph-DA_Fpe8IgMXtqt7THHyXNAHwycF8kYx0jNBbRyC81Dc6Z5zM_I6A0tJEy2UrR5jHBHp2uZxQSijCYKfId9wpLPIjLWHUurWR7YtCnPQe-A5s3_AHdShDlCzwjoIQsGKotDiwuMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد دمبله در سه‌تیم مختلف؛ معنی واقعی شفا یافته رو در تصویر می‌بینید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90667" target="_blank">📅 10:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90666">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=mAFoTYLKjGwuFnKNFnwfG6cx2Gy0DtYHrhb05h-Qe0st5dOKiSNZkuMEaIq0Rzrcot2_7naqeNZMS6UKB2AWwHO0XLwj3jYq4g7TyJ8C0HA-J1iw9s17laX1QaacCKwJK4lY5mEgPgCIICrs-1OkcXPeNQ_llB5G5WOnQSs7tnF2SrzEbOgCLIvjVn6OXbaFt19mpwQNuPO3mjZXIsAlUgGEz3XaFE4O-ryOsGJdd3bWvEm0OjIcb2HWlZTDLJEkP4-tSCElCH0D_RqBwUVY0pdj9qkcSIDickrLxDymiDyYWr9d2ZNV1jf4ajy54z7xeq8nDEy4mGOtbCnU5KQqU7fgXnJfuptdH2_VBinqPYHcxgGRbK6S-iuYdMg_CJooph8Jb-sQcCQRlCgDtv0xvK7wDbLGYjKG1E_QF8RDjtGNtaXwyaHhl2coLbNB6DN2YiAE_8m4P6QPcASlXLZ8EjXhrshg_Mr994P37HGe2DbvLOfjWGBqCXZYXz-6KD4Fi35Df4HbvJhc3QI3N_Lboq2MWCipwfTbmvooIp76qa5N0stMHsjup-Lw7vuOnj58oMSa4sfsb1or-5XaWRPl9zhetlKcXYDFUudD3ERUWgjdjoyjIbXWRMR5a0KTWNuPcOI5pfVKDkkn2XSiq97nZ-P-48sWwW-LuJ-559jS0K0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=mAFoTYLKjGwuFnKNFnwfG6cx2Gy0DtYHrhb05h-Qe0st5dOKiSNZkuMEaIq0Rzrcot2_7naqeNZMS6UKB2AWwHO0XLwj3jYq4g7TyJ8C0HA-J1iw9s17laX1QaacCKwJK4lY5mEgPgCIICrs-1OkcXPeNQ_llB5G5WOnQSs7tnF2SrzEbOgCLIvjVn6OXbaFt19mpwQNuPO3mjZXIsAlUgGEz3XaFE4O-ryOsGJdd3bWvEm0OjIcb2HWlZTDLJEkP4-tSCElCH0D_RqBwUVY0pdj9qkcSIDickrLxDymiDyYWr9d2ZNV1jf4ajy54z7xeq8nDEy4mGOtbCnU5KQqU7fgXnJfuptdH2_VBinqPYHcxgGRbK6S-iuYdMg_CJooph8Jb-sQcCQRlCgDtv0xvK7wDbLGYjKG1E_QF8RDjtGNtaXwyaHhl2coLbNB6DN2YiAE_8m4P6QPcASlXLZ8EjXhrshg_Mr994P37HGe2DbvLOfjWGBqCXZYXz-6KD4Fi35Df4HbvJhc3QI3N_Lboq2MWCipwfTbmvooIp76qa5N0stMHsjup-Lw7vuOnj58oMSa4sfsb1or-5XaWRPl9zhetlKcXYDFUudD3ERUWgjdjoyjIbXWRMR5a0KTWNuPcOI5pfVKDkkn2XSiq97nZ-P-48sWwW-LuJ-559jS0K0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
استفاده از گاز اشک‌آور توسط ماموران در بازی دیروز بندرعامری و شهرآرکا البرز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90666" target="_blank">📅 10:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90665">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sajczaj-0hqwQjs9rCn5Od8yJBeBISBelXh-ApUkDvPA5LHdcsdvwMAWAHsdbXYnaSQHO75DYcCpq08yw7Fkx1bU4ocEHV1HvL5XRQ8byqWTOXAFx_kGFQbJAK1S6TPjCny5vMLLN-_7VtrrauSyMlorH2fqx_daPbNxj97I9OU4nd7l50S2g_m8Y-juI3PiWbMyHBCkhXLEPzWH1M713Js31HfZHgTGdFVsQTt_Irvjn2UxZMhm2f9gXf-mK84OCJ0BKHzsvzRxyItmpHlxWCtosDe0qffnwRJR-Lvls1gorpGET63c3JePHSZCW65MKy4UN2AgwFyXMheod4KRZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 بازیکن برتر حاضر در جام جهانی از دید FOX
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90665" target="_blank">📅 10:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90664">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b95b443280.mp4?token=SG4_bwW7rRj8cEPywFbLO8tcR7DTU19qZYB1zoRqcdte7mNSFzntez97PseOq-J0pYsZcbufpXqDKHICfdhJQKVK3qyQXRXnRuXUhuruI_I5QUz1y-oampfAYXW7UUOlrKNkGdOqYT9trapTnNmVK9OJ19E1z4MwMrVMm2_JjD3QTIDn5XXkvov1CH7yuZm6vbI4FXhkyw5lP5WFVZGoHQY-DAAexIzpXvkRiffNiUL4oXDYGzMJXkEL_Ea37VhuLShLWCJA40-4XRLZWujLeguIor_693vBNsQi-4YtIxiKvDc1VQp2ZwXHTmA6yWdLquHndYvidIX1LTkuZcRfHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b95b443280.mp4?token=SG4_bwW7rRj8cEPywFbLO8tcR7DTU19qZYB1zoRqcdte7mNSFzntez97PseOq-J0pYsZcbufpXqDKHICfdhJQKVK3qyQXRXnRuXUhuruI_I5QUz1y-oampfAYXW7UUOlrKNkGdOqYT9trapTnNmVK9OJ19E1z4MwMrVMm2_JjD3QTIDn5XXkvov1CH7yuZm6vbI4FXhkyw5lP5WFVZGoHQY-DAAexIzpXvkRiffNiUL4oXDYGzMJXkEL_Ea37VhuLShLWCJA40-4XRLZWujLeguIor_693vBNsQi-4YtIxiKvDc1VQp2ZwXHTmA6yWdLquHndYvidIX1LTkuZcRfHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید از لامین‌یامال در آستانه جام‌جهانی
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90664" target="_blank">📅 09:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90663">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfcYjN3Kx2wiACxvRgdVeGmGpeyaQ8dDwo54yYIbF1YZTki1p5wvDPoJHxsPkSTfqhhZkGVfWz6NlKnnPRiT-suBx3lqnjE605MGOxidkaMRIuFOJzKyd8km6ZzhS3drXMtewxGMsbcV-_kdkEFFkAo-xDFWI4Ea1_ONV16HO6gP7WehEZAbJ9Jpzt3uk8rB_VAM6yObwVg8P4W9R8gNsUIU70zrBGXFYJk5EfIOwKlXUDnyE17HX-dHBlxEd28RBXwNt7YG5mo4eyc0oeiQsOJndSk72MxWpAKL2vYpzeKfoniv97yVciOs8ZOZjPp7rfvwMeoJMmMCWUuh-6vJxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⁉️
🏆
پیش‌بینی اوپتا از قهرمان جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90663" target="_blank">📅 09:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90662">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🏆
نماد کشورهای مختلف در جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90662" target="_blank">📅 09:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90661">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwSu-0GOHxXdQDb_vzKSV4KXR5oNBGBS7VnFvRsM-etbXgHnjzcEtNbvwNGicGp7qJynPoVb77bg9NRbAPx7xznB3YxOQG2DoTVlyqY1KG1_58G78LhOY6hebo4U-PgiQ0MoPIM2XtbVKrF7wN_bC5zrii9BTGtnF-aKippkRwn_R23erOXMn0IZql9_jby1QfKDwh4vxeDfWM4ZJCQpm60Lb5aEgV6TKmpa9fddzQjx376w6ahNNbWGUZRZEZUpbYn8KdjrqcOmW-QTZxW9cMbxi_q9NnXBteVk7s8Mip95b_4dlKhI-rqxtQe3fi0uujInOwWglHokFxMxouuRiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
انریکه ریکلمه کاندید ریاست رئال و رقیب پرز
: به محض انتخاب شدنم، خرید رودری قطعی میشه. هالند گزینه بعدی و حتمی هست که به مادرید میاد. سرمربی رئال کسی بجز مورینیو انتخاب میکنم و از بین افرادی هست که الان تیم داره!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90661" target="_blank">📅 09:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90660">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71618ccd35.mp4?token=mrsAhyqwYJQkrmf9RGBzDtJI8cY4dqWv0Y01NB4e5-4rOMU5ZT-gfCCJMXnCtJjVkiZ0ZvSTL3JUJvKzpDf4clq7BV92Vy6k7X4ED4fJYRazNymOqf-YOR--4CHN6Qud7Qsl9AgXvC5abH1SuC1CEz4gv5h09eyqj0ALGNeR1rJYbJMe0k7Xzlv4bJLA3Piip81R753ljOcZkIrDikv3j3CEr7A8zvYFH-b41FFpuAPkq117moHSe7r9TLlZdS-RB0KVWY0ry4pcTmomghoFDPuB-HeslbR2HyPeKW049r6zB4RG7N5p2rvBaBJUJ8a9D2yqfJOnGJGqNal80WL6roWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71618ccd35.mp4?token=mrsAhyqwYJQkrmf9RGBzDtJI8cY4dqWv0Y01NB4e5-4rOMU5ZT-gfCCJMXnCtJjVkiZ0ZvSTL3JUJvKzpDf4clq7BV92Vy6k7X4ED4fJYRazNymOqf-YOR--4CHN6Qud7Qsl9AgXvC5abH1SuC1CEz4gv5h09eyqj0ALGNeR1rJYbJMe0k7Xzlv4bJLA3Piip81R753ljOcZkIrDikv3j3CEr7A8zvYFH-b41FFpuAPkq117moHSe7r9TLlZdS-RB0KVWY0ry4pcTmomghoFDPuB-HeslbR2HyPeKW049r6zB4RG7N5p2rvBaBJUJ8a9D2yqfJOnGJGqNal80WL6roWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
ویدیو منتشر شده از یک زائر ایرانی در مراسم حج که در فضای مجازی وایرال شده!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/90660" target="_blank">📅 08:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90659">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfff56a47b.mp4?token=rVdHDSpPGiPjX5kBmqpx3uKz861TlKRIw-yR3rmaILkv4ogJer0DUbGxGx8CXa2KNXyMh0mHEO-EYjSFzBGw2Ukz5GmIWiABnzMbxXQvCAQingzzj5-r2csYVOOPxYYyKlzvzRySKu9Dz3eL-10Hnrj77qGmqlCWlcaVLt_8FDAYPRRQdAQfeC4uVYbxR8MqLU5k9WjRC6bQ5ijxSidnwRIyfnYKm8Gx3-pIx3N8W6EOJLTUN7Q8f76JRz_ZlnxuPRL625zW8QtZbhwtVOSON1Vla5MS2HP0xsJaoHVOTLl6gHutthsIZfrCGozI_g1L0XcuPVkiAqyAA_F3iZN2AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfff56a47b.mp4?token=rVdHDSpPGiPjX5kBmqpx3uKz861TlKRIw-yR3rmaILkv4ogJer0DUbGxGx8CXa2KNXyMh0mHEO-EYjSFzBGw2Ukz5GmIWiABnzMbxXQvCAQingzzj5-r2csYVOOPxYYyKlzvzRySKu9Dz3eL-10Hnrj77qGmqlCWlcaVLt_8FDAYPRRQdAQfeC4uVYbxR8MqLU5k9WjRC6bQ5ijxSidnwRIyfnYKm8Gx3-pIx3N8W6EOJLTUN7Q8f76JRz_ZlnxuPRL625zW8QtZbhwtVOSON1Vla5MS2HP0xsJaoHVOTLl6gHutthsIZfrCGozI_g1L0XcuPVkiAqyAA_F3iZN2AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
حمله شدید‌اللحن مجری بی‌ادب صداوسیما به مجریان معروفی که قرار است ویژه برنامه جام‌جهانی را اجرا کنند!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/90659" target="_blank">📅 02:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90658">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4aQQLZ6sES0jBeyMrLfuXlO7Z4nG8BQhjB2_hrqeb6XzBvEGYFIjVOZKFeiyxidjnFpn81q3UewZoTMssoh1uS3pd_NpgUbShhQZ0K2zzKERme_B5cgJLh9IZ2pBFc_ZqWdiYCHZzYWy4MrWuKJ5-C19ug7JEFG6w0gt9fD4t_nwX4m3HswJg9_NIeEBai8BOz1vOBycsp1gLLQukCycXxK9om-SXXPLqnHqwRw_TspMCHYNF5RygzNjxeIYQEZvu-GjEWUC9Bg0p-4-NpMbx9csmm1zRuLU0nIcg4mfPxI-oIbp2bmRdOXr0HEdZqT1Oo2Rz0Ip0yF6zw7WSmhAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
یک‌رسانه ورزشی برزیلی اومده جام‌جهانی رو پیش بینی کرده که در نهایت نتیجش این شده که در تصویر می‌بینید. موافقید
👍
یا نه
👎
؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/90658" target="_blank">📅 02:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90657">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLWtLTcIWDnlhIJvLs6IrZWU_c7Xg__R8TFH17OWaA9tSyV-4LevFVcc2VWv17V_hal948ZyQgD7k0O5TN2saBa8PDmFPXZjM2tZyipFbCq8wMPuTCN0D_92nUMmde8ifoAyzPUjbzl63DrO6q_G7YG0iVcdhlv030Bpz7eC4ObW80HQIKiOdXOR3TBpqXRTkxiVESgPH9vExyCmQsrgcqaTefdJ8bOKEjV1Hh7WacNcyaPQBrgYA_dCpPiu93CCOXz_scAshaYnBuWLBCb6SJiiCYdPcd9ySJvNxOUmnC1szwsrsbzObcy46LF0mbH9pIxqCzjY10pfrRKSMr7yCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚫️
#نقل‌وانتقالات
؛
یوونتوس به دستور اسپالتی خواستار جذب براهیم‌دیاز از رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/90657" target="_blank">📅 02:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90656">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/90656" target="_blank">📅 00:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90655">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=fX3gKtS83uMmXgEoQ7xB5El3kfmDZm82IyXTMqw2VleyhhGRVuGpTWGrEwsVhRLz7jTfB2mToD4rzZzuGc-l4FalRh-QwSvXqZG3qmxIrw459IJP2j6QcmKHJCx7QuUkve6_Ob1J3fKmRLvY7QO69Ww6VV6CAFN5IkyqclHor6U1nrwpQfVo6G6xYn2Q0x-CIp3qfOItCMjL3hPRycH5w3nxQZ26M9TaOCK32cQp5IE6pXzUeY4qAyTBayKpuv1WqKT2ZK5hh7X1TmOH90XxprNOaTDIIwm26e-2UuLXMNkeBLcKL-icKI2fWFkGqN0iqSz1Brry08vBEkCg4A1vFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=fX3gKtS83uMmXgEoQ7xB5El3kfmDZm82IyXTMqw2VleyhhGRVuGpTWGrEwsVhRLz7jTfB2mToD4rzZzuGc-l4FalRh-QwSvXqZG3qmxIrw459IJP2j6QcmKHJCx7QuUkve6_Ob1J3fKmRLvY7QO69Ww6VV6CAFN5IkyqclHor6U1nrwpQfVo6G6xYn2Q0x-CIp3qfOItCMjL3hPRycH5w3nxQZ26M9TaOCK32cQp5IE6pXzUeY4qAyTBayKpuv1WqKT2ZK5hh7X1TmOH90XxprNOaTDIIwm26e-2UuLXMNkeBLcKL-icKI2fWFkGqN0iqSz1Brry08vBEkCg4A1vFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
🎯
همین حالا عضو شو و شروع کن
👇
e11
https://t.me/+6ckCmywafrxiYzk0
https://t.me/+6ckCmywafrxiYzk0</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/90655" target="_blank">📅 00:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90654">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbrDkcsPp84Wylun4oIiakJseBQPVSOtK89kIfp6i0r2KkHBU-8uYkRSd6tINB7iNkRf7iFl79MV-nUw3Ybba4GcG3Z8_zm-PTRj6baJJFtELuQND8VnMe6OaEQDLUoGa24wgL98PfQd_wnKvI3HCf_MQiCtJe8ctCKz0MPJFuiP5T6MEuGguq-LbIwHoHAva3ArKNXXlWG7-Gd-U6NdXTR7XTfLpNVjvO2cbe9S-G-IXz_AtQXfHr0wmJr_APA47V91P9CFjzB4fbI9i3kv3MUBjXpUB9FTGNUcNtQTSJOVY_jMNz7F6vIu8L4ZglC_SzMWw4iJ3wMZJYAPZHjTfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ال ناسیونال بدون اینکه خندش بگیره گفته رئال پیشنهاد معاوضه والورده با فرناندز رو داده و چلسی حتی ۲۰ میل هم حاضره بیشتر بده
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/90654" target="_blank">📅 23:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90653">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
ملی پوشان فوتبال بابت برد مقابل گامبیا پاداش دریافت کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/90653" target="_blank">📅 23:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90652">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کونسیسائو رسما از الاتحاد جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/90652" target="_blank">📅 23:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90651">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmwhReZwAcz0GcTbrXlb6GO8aUpETHbKeU263wRDcaeSfVQ_GSih7kEouMRtQr2SIVEoxlcyVrF042swqd1i9sXQmoywrFYR4nOmBJv7Q6vcNmaE-W5qj3T5EYIvlEjrF1r0Hr4_Wk3YiUU7XhVzn-xzXADthT9c6uw-2x7k7sLtZspsRsX9Mb7qNfhKSpiDhLqhVHUc218V6b3RrwpTjlo6Nuacu42yDA4urlFGhOkS5F8xPMLXR6cU2QwZgAcVqRif7idhLF_pdeM5_Nk8UdHz5rQ8c4D5hjSc2NfuEp0QbhlncYroDnGQ1I5wpDaVWUKsz7WKroLFFJ9ZGgW64g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوبوسلای به این شکل رفت اردوی تیم ملی مجارستان
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/90651" target="_blank">📅 22:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90650">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUXPGpCqhLFLwReDDTysre9gsuhGQau_MckY3KJo_8dg4NVnxJDhcG6ksRWkRBWPPUVNwB4mCzM1iQqDn2LUOD_aqSBnkhSBdrASUF9eJTWZtKW12CbSqlHnlV6Zjx2pDGWPtKYJ2Ivk1SShAZ3zKRBJZ-uzMvxe78OdnNXHhAyL8XD5UWLS_bL_vJSd2GuHUKbc6-jM2hGb3eKEDvejIEmM9M_cQCSzsSa5CgiPwSsRRvU0bCuQDyhB4oYaRGU6fsqDQ5c0URhSrKP-TdAfMR9Vs55DAtET5fYCI-vr_kbECGE0409cLNmXIMI-_r-2B4_Q6tMKP4WRmKbnKAQ0cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شماره پیراهن بازیکنای اسپانیا تو جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/90650" target="_blank">📅 22:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90649">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfXTepVykvliMaFAq6LMD-VyZi-MJKiN88HtHHJSm1TXf2gdqwtuTvTTOeoo7jn0sQP6UmKr_TxQR80eMIzSNS584opFkgs6PQoRmDALCn-2mh2dCYmrNiU23nXHd6l0besfHrUO2rK_eUqVBro8bs0K8XZySkqL5NCQLtwJVvuHURvOmt_0FG6vYX3b2rHwoYK2fH12Fa31WwoywIrhLQ5YRJtTdgDr0Ly7lTMQouafLvkbqDdKaeDJqNUmXyR4fx2F2VAnTookQkL2TCaq5U-n3JP9HcygSmkOyvhAhBFu4qC0uNkv53VllnLkV7h01J1YClpTNHl-NaVOwfZaXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ورزشی ویژه اتصال به اینترنت
🔥
⏩
به بهانه بازگشت اینترنت ایران به دنیای آنلاین جهانی، روزانه با حداقل دو میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی میکس معادل شاٰرژ ‌حساب بر روی رویدادهای ورزشی مورد علاقه خود، بدون توجه به برد یا باخت، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/BACK100
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/90649" target="_blank">📅 22:09 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
