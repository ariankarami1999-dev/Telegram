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
<img src="https://cdn4.telesco.pe/file/tjs8j3mUWFgV3TwVn8pogu7I3yRJHM6csRK_1c-o5-BcEq6SQMSd7Ag_xYgni2kWHkJ6s7T0sM8uubL_zhd_FkAy-_N1f5GeXW-d4XG00M4XmI1U9ulXntyhQgFpTBcbCSPNLWqjVDXsdLr0t9YnZFw6RKp_HPul_srnY4EhwDgfTkd-LAm3bNrax8gRxzMsVyzGLPE3I9YOTlf5pZpPQ_Q4hdrVC_uNmuWBak-wahLIrEIoHe65HEl2SWncWJBcllyDGGWdTFgaCGmGmmglyEhIJWrJxMEvtJmwfwXhPMqhiTQBjMdNQXN8IYclpBmyeWyYlm18PePF5G0IpqtwPg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 192K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 15:03:20</div>
<hr>

<div class="tg-post" id="msg-22301">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fA-LOKhRMdBHUP1ozvCzKr2i1eWAJ9NWIf88MEwaSM1se-XB7u8NYurhIRFh350oSughxSpR6dNZ7fDy3MCeyay9tPraXOuxl4RIxgObtCf60VmKCJodBGcCYhhAitGO2NlVXf10U-NCrR_nZV4KW7NSI0ebuJ4jtm6gIZyVQiVPl_L4Exg_2fUwf7wS_CTnB_zo3ygxkPCsW0N6A9jTyrExyp0Vn8qiJnYAoFjjGofxQhaDxZ3H40nMw3lJVjoPOBhgkumEHaBUHRmu6XKBgBz56brqvLlxXUjpcjbYa6CKNScnaKF3zbq5YsnpbKPxjbqs4cxFWtUa0ru9Zk6uDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/persiana_Soccer/22301" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22300">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_w4_onSSrxRLuHOqx_Dn2vL90lJe0ESN6TCu809s69L9B-18ptTDFfOzz6G-z2hzyORhKxL16HIZoq0DXhFSKbWmy56U2tj9Jlal7n0e4nB1T-qPIHCVve6t1K4RX94gd7ZcSIq1xqHM-7WU1uRXuGrRyVgh8JOxWH1M-C19h_Zrj5fvNUyoq-_B1kaXXmW5CzEmKBMX_s-PYu2vV3eqg4cjUc9ONrjWc6yU_xpVwYGxlIkbSpVmi3qnvWzYlqX0U2RoIgtGTJs7j9aTrDzAoSSv8_7ATueh_M2ZCdOrW82ZcxZAJCDfiCMqyvTD0AfbjJ6FVBqgBAlV7F9hwGpwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/persiana_Soccer/22300" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22299">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlwtrIBqlbUlaNxlitqMEaZh8yij9kEQpdbTtrKIA0J61EcMlh42QE2oCDXcGcSrywpN2bdk399G0B7sC9jiEC7Bd4SmPU5ZiPjB2Ro5X7HSyTh46AVosusGhpBG92cyuI4spLjs_4Ku24Yh5orHaTcy3RcK0utSpFbccBkv9yHHub2Qwwg5AktlzWM_hqo0vdFb_kVIZVuYTaIl0Bm18pHPBxMILq1VzXZy1IVe3M2Mmbohm83MBhdmdwEMsqTe_XmW77xkI9GJ3z_ARB2NcRz5o2ebB-ZOFNXbP1Vd1FtxEsJIL-iBy2U1l0z_Fb2yTu1KbwDU7ZtUz_hstQ9jVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/persiana_Soccer/22299" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22298">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze0a1YK1y9rqTqCyfk_ARnmDfA858p9eylcoxdu1987jiiolKxhH4fXrEjrh386tOswOpF09hdGucQtJh4eiBr-ETAOBBDu29JH5l3WB5Y0ilLKnH4mMYRLiACx5YrkU7T_M9Sv__Gun_Mf2ccMuRHu-_3GPXrUJtBIOCwaiO4sPmOgIpheIap4B5aAfyCtHfoFrb5r_AEebr3hpjXaYiCvZPaOcjD7vNkNvmG8rk1P9-4MKFckoykDhRcBnTyshvsPvOSz4UgWnJpNAaImIiVWVYrY0GBRpZOjFieIc7V7SfdvsxI42qs4EgWJ45nerVwfBufwADrAjw7-L4Xy0Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
دیگه
#فریب
بونوس‌های الکی سایت‌های سود جو رو نخورید
❌
💲
بیا توی سایت مورد تایید ما یعنی
#وینرو
و با عضویت500هزارتومان اعتبار بی قیدو شرط بگیر
👏
🤩
با عضویت
🤩
🤩
🤩
هزار تومان اعتبار رایگان بگیر!
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگانr4
📱
@winro_io</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/persiana_Soccer/22298" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22297">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQmLHudhcuUUBY48l7gAoKZEDsyu-GoPtNtEdAS2BjSd2I1C5ym3IgUva93tm5tsdLm6SLE6fpguvwCg82b9H3lSY2X3ibbU2HT-_vAQgCzlEiyUIb6MQuO_6VcSw_0giejW7iOyeftfghAkem9fhoW1wIFi_lI0sU_f3Iu3ew0qsIDjOqysErG-oT_eVVmZenRxYYHRLWPkwt6Uuc534KCebIuALxI0PKrk6q2WAJyq8TpQ4bqaPUuH476q89h5q6wQASdpCqweXKma5uTbLvApFpyrbaZCL-tuj1CgkSLdGbuFG1tLIvK9GjEepSVXq10q7yfqRgPiQ3OFPcUbxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/persiana_Soccer/22297" target="_blank">📅 14:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22295">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGAzZiI0tUf5x4QvigXvROoE7iQXjyvUmat6cWC77DpwnmkZoX3GYB9TvrjRd_RK_LhDNjMauf68JSbTDeXrsb3KA-NlXYklDLvJS5iDmWOXM-gcZyZT8FOsfXm7JpQEYVaJIIfmhuSVVF1Ca-RFBKN28g2_gQ7xKqkgi0SUF5a3tHOphbgfNAju2BsxZ1JLfZ_XCxoLeAH-REFSex3owocuJqYiIsKUtxdmSS2bE7L9MRKvPsFzl07jFVnLC38m_5GJljvU43-QF6JRMTtt6QfH2faMnRSIkK1NSo681LrO2KcG1d7Q5Bbye96f4cr-ITy6c-M1xRyWOZ3_YpaFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رشیدی کوچی نماینده‌سابق‌مجلس نیز تایید کرد: اینترنت بین‌الملل‌مردم‌ایران این هفته به حالت قبل بر می‌گردد، یا ظرف 48 ساعت آینده یا تا پایان هفته!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/persiana_Soccer/22295" target="_blank">📅 13:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22294">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK-I_BQw3lI9Ob61iS5lm37uXpJSYDv-hkEdew-QerucM4XWh7wVnW0FOM62yXUIsBrtndatAIfLuxOBFmQEfVkNvULAKOUjQXKgcOoYdecOnfGro5NRXjOgHSKx0pJB9dSEHskjIEvDzUHEC2tIdQ0aJnOYNshoUNenA-LEDGxyJ_MFho21FXwIB_-DUPri8wBxDDzYy6vnICcH0Vs52X5uD8K4EcyEpke8OucUQqjEzFD6cbW--LeP-KnUVsoUM2ic2TzErHsZOOM18z10jBhffHZJX8s0EDSbiX4vlr2zn9mz0IK4LqEGt6A6_P2I99b1nMv0osVsCuwBK_edLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22294" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22293">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCWDtZ-6TY1HYeNKjl4b6IFveCzoC5nbsDsZlfJyAG_0GHuY__mXUp0gCL5n8wEL44CB6VI7MXfPDR3FUqJGfMgX5xD4BhNDuGsnf1Id8Nrqd7gUQc9xVvkdZK1jxk2Gv26vELbBRaZPP8dx36b3LLbT8rMeIxQ1T_zyP3NOxqgqus4ATD3508E2bo4KxA9Ux22_mclgqvowQqzXAZ0Jqfm5tlwa21CS0RCcJMfI_ONXLZQeN9k_R1BMtwCulZ0sFg44hJQz_5nCZZoysrl5Mt8CjBFIxk_zwzcvUjqeXFm39OCXZmGLR4iFg9zdqBzGp2e4osBzZIWSo0JIObCD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛ روسیه با اختلاف در صدر، ایران در رتبه هفدهم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22293" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22292">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hM8owcGlDXyl8yEhK-sL741NPdag1bm14dqwy-8JtuV-Mn5UwXfLx8-_rWSgiEskCQCR-vwdCwaGQ_M8qiQZmoCIXBIJKvMmtwuxtnEnHDhnwQMXv9DDP9XoKI4n-RhR1DiiD6xTiumbVpNrOgykrVlrPMhV1d1fZUz-ZnpBI8w8FHw7SdKr20Pswlyhjfjz3zwu8_XI5VpFHS6FLpR3ABAbmlAc-a3Lpi668qnO_h_5yqe2FLE2lVSu5f4zYTA2locBroexjnA03yi0OiY2o2jls3IGvT40K7WK7tmbkfBZ-_PpaQU20fptp4q6qTqgGGVLEDN1ta3RzL0tVO8tuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22292" target="_blank">📅 00:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22291">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpUWKzSb-S6pjEX-HwafBmPXBybjP6Wjy_QTyjYo82JkO1xiwdgnzq3_V5I1dLoKdBlPZC6UL4Aa6KNtU1elqa10LyiRZUVc_GHeikOwA64o1ZQjy87t1gB73A4DriW8c4kJWSOeeCzHtx3LD4T6u8nLgk1JCPwTqY5wQv04xoH4g802og3Rx4Fzoxl7hI2cYDqMOrF2p-L_EffyE3lCVwdKzIQN8Yieej3RSDv0i2h2USwJ2eNWsoKQp4YRPYnG6sLLQXgY2oNmkogoaRQjuYFPLByeisa2Js8IYCyQ6b3PYuGV9WOdLwnm3_f_Imc-PyDpemn0pxa1krrU5t-f1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22291" target="_blank">📅 00:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22290">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbyP5rCImQuIV1L7R6YiEzQucAcQgHOt6vIgaVIDGDhzbWlBR8NYwlG8I_Kjzi7sDnPkwQj3c8yftP8erOGM6JP3VfJ2zPlB88IQkciTzjqAYu-jXmCaU9tezmGUUC1NgM5hTDd52VCTMdFlfrrswvyQl4nl15jq50vbPy0slcR1tqUJfAc7cl6YvkmytCuuPO-K_qBRWWlAHf9P0hOopZXoZnEV2wgVlnJmhzcmMARMe8mTEh0vKxvUuhdQ1GYMswIbpdNpHkk32ByW1ACptkqq7YgcgcWbw9tQld3lHhGOJkLp7teLbrlpvYqWANJKjH4G-29dV9rstARqFJHciw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22290" target="_blank">📅 21:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22289">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fgp9flRndDHijEnefALIxtHFzqeIq7xi-WASXHBiFHUvLbdzdkUeuAKSF0E2pkLlPwAgdd5HnTB8ael0pWCOSSvVddeWwI4qHfrfF3nH0t5K0fLjEadLnRIRYVLPYl6QKmk8_ZvDy_hQ8qrQp_OPKEarvXM_VDzT8VdV2O2Kepc3SCarI2iDcoWx-N3NKIIL3ei960kqa8pdShIjMbpPSgRXOySAwhNsTYD90Ul1ah_xMkBMSC2IHb9DFvnI-RrgUtBYd_Igv9qOn0kw9TsDQFjQ3rEAhsQ8yr_jwrkTagiWlXbfLX03zvRFyd7P4NRK0UXueD9NQTEuTQl7Tkj3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
باتوجه‌به‌توافق‌‌مدیران استقلال با ایجنت آنتونیو آدان برای‌فسخ‌قراردادش‌درنیم فصل؛ برای پر شدن 60 درصد بازی‌کردن او و سوخته نشدن سهمیه خارجی‌آبی‌ها به‌احتمال زیاد او درون‌دروازه استقلال مقابل فولاد قرارخواهدگرفت.البته‌اگه بازی لغو نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22289" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22288">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rfq2x-w7zxyhoqJGIOz3zuaNq1m8CJLu_Z31mtxRx0pBzmwJUHKnZx5GjbvOLbxMFVAOrpg5GDqZIh5pj8u0tpUPdzFCJWJnxjH0otyZKrLkkDI3-L-Q57EekQTC1gIcuzhBmzW_pVwSrn1qyELg5FwJH6OrRVloca-ecfUAJ9da3E3KMak3h2WMT5Va-K6PY9VcYYi2CyvCNJ-yx2FaKBeTR0Qm2TVNBPUJy-WZReq_TaNNwmK2vfZqc-SmZ91TYM19VIV77jDD_hy_XQ6Me6KEQj96XHTZeF0DIziQYh_yWrlaV3-kgGNV4opMnWIiKBrRGgZD0UMPrt2lixjYoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22288" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22286">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSIXqnIHO9Uqm5XUuvViv5CfI_bEJ0JmQOHWsXPc3r0-jArkFk7EAGWDjsm6idFuzPNu47Awf3Q02rT6ngNVBDpbLWKwysHZlhRuU7pETIpurai5_bQT1as8nw4v8CA8ppZmmHpNNq8HbktnwFSE1tNPugGRh_tOMyV3RxrY3tjPaQmoEWGuOJbMMc_7kvn8BCUABiadU3EAS0FxDRe-jimZyW2Png44KEF1N_pgITyI1I5Qk3Kqe01lg5uVz8Zi9U7CKdirsVCOjKXs6ckL2fyTQwsfZQK8rihOuZHrbtAKNHQVOZazjUWIwFWetG9teME9pZupdfSDOlqFE2VNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22286" target="_blank">📅 21:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22284">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AmDYPcF6QUVsPsgUPd85HbHQeYmK-CcZYjNpYgjIcR6oz9Ju8k1DpOiBpE7ZhSV6k7AW1ImMkgx7rweVVGSm9_A-qsKRcQVj4pA8SQyNKnUAjCCg6VD0LiRhGjyo3rWhjq_5j9RZykmgUXg3D_GOJ3H_QJ_2rbpxjB9moYfyjsM7bNGJNAJ51wJ7H5RhlE9wruSIk7wNqGnlvwmLOq0r11VlEJU2x0pXk-YrlfCdJVkUW_3LDP86eivqneFd0_3uoraUC6-Fmx7Uk-K2xljpv_PD5lMt6JPHrVAhPdS1XxR2cH6wwLpVEpoWLorsGTMDxymb30w3C7ll_QhBZzyb_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZK65iP8s61-s8_kB3PX_7zjs6UL8fLq5x_kwYhI_YxZGjCmWpuHSyoaiu4AF1uT77IiXgKTAfiQzRKGmi9LrTQybP-W6l_J9MKE90cWd7iOeJ8WWPdvIFJTPiWyZnx47Ba2b403_9TOIbEwONe30q9bg3gslAjNYghzTX6MLtpSp19MntkSe670IzbSn3YjrvhqYgvFSQ1IIJ3Q4E1790sS5toNyRx5aY7kNFNbz1Qh6Gz9YxMC1OrfqWAV7mg6XyeWO7HuBV6sRs2OvBo1VJkS8xPzHXte0lCkPFx2lCQGAKUhP82i9kkOFaJ1aMCQQvIxVYrm51WexMfDo7bTHEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22284" target="_blank">📅 21:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22282">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5hsW6XPz2f0RXevfiejkdnhUm36gZTaaqE-IWBX7gjPwI_IQyquKKi8T9ZSs0ke1d0ARVcoOVZNWMleM9Hv_rv-ViN6fHwh5kCdd8d7A_YGR5VVCmZRojv5_MPqeoi5mCBRVxTuiG2Am13Ar0HKAAzauY-mazBhxSVIfDdJqxljlt3OigQ4H0iIM68u-uxRWyDRUeOCI5zJdzK0LePng0SNdBq1NxjzsXuNR5IgYBs7b-AyrBwxXVnky4yxUlUC8fC4_81nq7mg9GwN2dCXgs-WZv--UxNkA4vw0nQ0lOQDZuWeGLAmKk0NmdaRC2lkgc8PqUt8rVgNjtvNdfnJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lY0g5bsQP_hxcLZtvxxwBmfqjCMJZJehPD8SOwpAzbzGyVYUOYkBWEr20WfUi8xuEzST9yuqtiJ41WhWltW7lqtF4Wuj2MUavQ_f7QJFyH0k-YLygICx1lyD1F4lyKWqgZSS7gHUD2i5VZcbpNeVfLUjn3Yx9x9IgcEOg9fEfHK0yF5xERxSXLDyeehC8pBotMcIYUD2dpZyZc0XXrbBcx6gmUU5ZP3N_iSBg9dSEGWG3K9-RMH7BZdJ7PJYc5leJnJCZbl_BFgaDmhRkG5A8z4ICP6y3g34xsOvfdSHMROYZXRyG1rj2bY1ChYgyymp9Wkd422uUfxfOrplmgdEnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22282" target="_blank">📅 20:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22281">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYSRgwZzinI2HDrwrXWASX6Dyb7jPhd5nh4KCOQgSgk_sxjvMKCWn_sV8LdDAC73W_jsTz0Zt6qYfpM1P6pk1sz9P4WtukRaJgYCtxjJOrheQeUJeVh4xbk_cnCuxzrJW5KsP4fd-eoAGmJOcX2tCfJeD_WHCtW0F-xe2YUyxhQUyhu1Q-yId1S_XIODflx5yt25E1NNApY6jojtu_hNjTHlYwo29jjYXHUdiAr04aTCQzOj7PoklvTctMa-Uk1m344tzU9D-g4bZAXV3F0ZmVMlYq2o-6FDtdtH9PCqfPKOrUF9IJkACo_EQR7Pzj25aUEZwaZZtHEumcartYQrfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌لالیگا درپایان رقابت‌های این فصل؛ خیرونا که همین‌چندفصل‌پیش‌سهمیه اروپایی گرفته بود به لالیگا دو سقوط‌کرد. بارسلونا هم‌که چند هفته پیش قهرمانی‌اش قطعی شده‌بود نتونست به رکورد تاریخی 100 امتیاز در یک فصل لالیگا برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22281" target="_blank">📅 20:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22280">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DD--C-bRinMlyh2xogf_hcsfDgb9objtfg8h4qDuELl7NLZwNpgooojwwDZyiTX0bKVkMtDgOTalm7Yf_sSD5p-L9DOA710I6_cpyvgwf76fAOCSZ7dfH7UdGMXtNV7VtF2PpzZedI_QRV2VzeG6INY6wJkBJCTymTmuhGr3OM00eadp6ybCh-giCvC-YY9tB5PEv7Gqf_ekFWWM8IXvBALo1yFvvYDs9YkHmGk8sWRbtSLpX-ja3vVoVWRgLW5v7HyUH6rDSjRbGiyxMBR5fRAaPJEYrgjk6iH1SBLHKUPPtK8hY1iJlPUSyFE78f8weiOzLqXIIZTa6DoRD-XNFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ محمد امین حزباوی مدافع میانی 23 ساله باشگاه سپاهان قصد داره از این‌تیم جدا شه. حزباوی از باشگاه پرسپولیس آفر رسمی دریافت کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22280" target="_blank">📅 19:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22279">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJgvfVupLDtdP6BaccRO3tHuEyHGrVFUw64eNqtDS2IonzH0L869y2Z6nHtHCfBPx-MpvBOb9oA2acBaxl0liGAYdd3kA5eLVUZOC8AR9R2YrY_JC2j6b8V1WmdzErUFDOIAhPNb1IRQV_4udCjx5LJU9Tz09y-kePOA8YiK_qUoRMhW2ZBQdQ0Ipk4JrTS8MHlNIK874hQpa-hULlDKTFefU4UxJWoeRyR5Ym4MhtQ31Se6UZ9RBTAshuU0TuZXXtPbx2pCL6OSoC0lyC8yhhIMI4tyqgOA4tnNkqlse_hTVLZEdyXJAoTiSH1oqF3T9ElxHvfY3Iey451VcJCRPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیتنا پایگاه‌تخصصی اخبار اینترنت: به احتمال زیاد تا هفته آینده اینترنت بین الملل متصل خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22279" target="_blank">📅 16:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22278">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmfSRcXvRBHXDWE8GgAUz9sdWau_B2IH9HSF5eGBcQZo7QGLe9Pp7_uJgLfJbncww0YQKsi9r1p_rAxVKC3NODj0pNLKV5xscclK346EIyNSsn95zn9QSpaFpBu5OelN3eDGZQXUCB248T6o9eURRGKrK61RPD26D7x0N21TPbFsPB2P1a7ZJYReKLuf9FKcwC9zwS8dRRG2b0O-tgjr62ReR7huPF9HRBme1pUjv9nJ02DSFIZbPuE-CVRt1gKUzxUtwQcbh2QDmoE_rNPLRNwd1tEbGV80qFtVa3C3ceO7Te7s8FoLtmkDr2zltEnukGYt8UiH9F4BgBvqCRjmdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات
|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22278" target="_blank">📅 16:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22277">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky39U6JiwcFHjrmMVPX8KLulI7T7laKU1qYnNdPvgrUL-HWvT8ii7hIhRQlwUnObiP0TTDQMGNio6fIYyWeeSh_ZSTwK_QqHeheflOQqx4WDn6H4x5T0GIrovZb9TON5NgvO97Ql8bzRaPI9yZyp0D81643TIJVOcfYz62_0nr9srrXw7lKNn5_aua1w7aHDvGAgxoM883BvsNM-96elopft6wEtIgUd0Ct8quHfpilo2SQdfuIEEbksG-JXEDAUjcdNFa3ueKKJtgHT-3NEkKhnuNVIobvM3nJRfibM-oTdEkVE1OuqJJV6uQLqydaeiaJkOH5urstx56kkhNAvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هری کین بازیکنی فراتر از یک مهاجم؛ توپ‌گیری، حمل توپ و دریبل، پاس به موقع به هم‌تیمی و گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22277" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22276">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nb5mUTIiu0cl7PN3bU13ILulesQwL3nLptvar1VQgqXjkORANXo-7s3XQyC3WZ14RvkMkbmqkAnb5omX1DDTObopPtJfMEl7W4POXSvsQo3qbbXrLEWAWCtR8OXKafMjmTSgZy0Am5Ts8hUfare4AIBQCXU3t4mkKjF6Q_ZXu3aIPivQH0ICiqQGrn2ArcUF3eh98NeeQTSnJpfBjntX1Fh4nRHneS-zlerLtdt546pVsbyQGqTX4k-mi07R2ck1caI8mucK4XwbfvCuUSofBO8_uqXXJC36xi3OQPF4ECSzZGt7rehvuJceHfRMZLW8xPsrzoAm0GCAqXEUZ47W3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22276" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22274">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9q8acx5rfex9diGRuWcn8fOiQbKvaFCVFuzYKBb017osRUvvhG9h4qI0gcBgFyGFelG3E48jP1EO0eC61MjgPgeMU2G70NqDehMVYOK8k-f3Ca7nGEA1VdCayUrHquZEW_YvtRiidxIJ6Ndmo7j6VEyTbSqm9QBlL3VyKrfmOq2iL17g2T4SKF-N3up9OG4aXn5UUGbtlZO39JbAIYeRv6TPRptV5sTlLpb8XPMEZ-arBmmRVEgpxoKNY2MSCr7KNqyEueeV_2lJjIM6GLTJUV1N2YpFkfOsfymx4nFhefPHcypyOPt_ij2cFR4kNfQbOvlLiwmh1ghuRd9P9I7ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌گفته‌‌روزنامه‌های‌ حکومتی: اینترنت بین الملل مردم ایران تااواسط خردادماه حدود 15 خرداد وصل میشه‌. حدود 2 هزار ساعته که اینترنت مردم قطعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22274" target="_blank">📅 15:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22273">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j24cmZvBzT9Ct4I8EWErk8gXgqUemCiajw9ZWrzNdkcdbCcWd1OENfx3ScMOizYRhJ-_d85a80derhef1c_4jkcitg6KzhbLb1l_0c1GYF0pDsb2F_9I22BaLK7G5_jkqc1NKS8rfJHOq684z6iLUIV8F4yCo35PVrPgGisnb1jWb2jazX8YK4eT3U07ipSDMDxSIKL3kfSxmVL0WO3Q4u9Y0oSUFsi-aldRem13z52dlkXEPuCqFymKA6Pf9eDj8JEX2btMPQjukan27pKuYpoh8oiQN4k8mRj4OSVkFfaa7NwVmx9RBmpishxx9KZ0_WXZ-exdAhCJGc821k4SRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22273" target="_blank">📅 15:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22272">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5Q9gXGeziE5rCIQn-qV2h1jXXfc0b7rOowHIT2Ju02RK0DfhSBE5g3f5HktcTDAlvcjLItCIyyGayQ7aoBUl4hh6YwO3zcfDvsGWW5Ki96WKwWyijMm0r13aO2kqwpQ3mQ3ipaNG434y4ONNpH_8ZuJEpm0uiQ68x6RaBWpcCasbFbk504paBfNoXIbdOE9bQh2RlztpF-ZlcHQGQNcjvMlvuAKv9oHWgEFZmD_3VXRjOJuO6hcVeXNSonBL1vYH1FI4wv7R9-YE3VTTjFw4mZtd-b7So--xdp4oA5839C3mRmI9BiXcQ-_QpjsUdYpsTcN2CKzR293IoJzaEhQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
درحالیکه وب سایت ویکی پدیا از تیم های حاضر در لیگ نخبگان درفصل آینده رونمایی کرده و در بالای جدول هم اعلام‌کرده این جدول غیر رسمیه اما برخی به اشتباه اعلام کرده اند که AFC اسامی باشگاه‌ها را منتشر کرده و برمبنای آن اعلام کرده اند که نمایندگان ایران از سوی فدراسیون استقلال و تراکتور هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22272" target="_blank">📅 14:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22271">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=IeDpfBF9TXDTwbXA38vLXPonJf8K9GB2VF2MBvGdn7RLlnuCHxgJ5n9ed9iNMXmSoBW0VfTLrmr9hJ1XD87VXMgOdFyVbmvuMVEV5IUNlMZ3et01Axd9KvHKYCDzJ7WKEXtIGHPopxWY3KNk5Iyt6UTd4Qu1HIF_6TSDqAOJS0FawzDebEiy-YCHrY8KJ5OLMtF_BG9eGFFGBaQPBEEjl1yy7NhWDjP3l_EZZWRp77duIKmIr0IwLZih_sEaUzuF665kmCBSXl25jCEsh07eJpzVWEKS7fE1JwpPyPp8RVhrH5UQhXWDK3mBkw2_cHsTOwqeIlSk1ee4SYpGvhOqWoRUQmJIlN8y8Gz7Svu36rTeU_M6Rf-2YNv_nT2Xp18lFjo9yrjIvQEsuQjhCCKl_eBsxhTey-5nfCTmLf4S0KXVALxsVw2MtoD6iB7o4gSprrjysWGXyx_SjdAYxOyxX7DkpRJcHME738d6rczBvipAXvDlOMjGDtgWeeMT1IeEYKKaSNZ8nF12ndwHwc8PKqclgcfBXk-MfVmfX0PcZ5Bvz9t-od1A5pdx4lyzCbbPVdF-j-eQF5biw0CF6b0rPPypgWmOVv8ChRSEmKX1uqCbPyCthBAo3EjRQlbOJB3qsxnirH2OD4fCisUR2kDofODDtnHUMrUK4cZrhGW132Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=IeDpfBF9TXDTwbXA38vLXPonJf8K9GB2VF2MBvGdn7RLlnuCHxgJ5n9ed9iNMXmSoBW0VfTLrmr9hJ1XD87VXMgOdFyVbmvuMVEV5IUNlMZ3et01Axd9KvHKYCDzJ7WKEXtIGHPopxWY3KNk5Iyt6UTd4Qu1HIF_6TSDqAOJS0FawzDebEiy-YCHrY8KJ5OLMtF_BG9eGFFGBaQPBEEjl1yy7NhWDjP3l_EZZWRp77duIKmIr0IwLZih_sEaUzuF665kmCBSXl25jCEsh07eJpzVWEKS7fE1JwpPyPp8RVhrH5UQhXWDK3mBkw2_cHsTOwqeIlSk1ee4SYpGvhOqWoRUQmJIlN8y8Gz7Svu36rTeU_M6Rf-2YNv_nT2Xp18lFjo9yrjIvQEsuQjhCCKl_eBsxhTey-5nfCTmLf4S0KXVALxsVw2MtoD6iB7o4gSprrjysWGXyx_SjdAYxOyxX7DkpRJcHME738d6rczBvipAXvDlOMjGDtgWeeMT1IeEYKKaSNZ8nF12ndwHwc8PKqclgcfBXk-MfVmfX0PcZ5Bvz9t-od1A5pdx4lyzCbbPVdF-j-eQF5biw0CF6b0rPPypgWmOVv8ChRSEmKX1uqCbPyCthBAo3EjRQlbOJB3qsxnirH2OD4fCisUR2kDofODDtnHUMrUK4cZrhGW132Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22271" target="_blank">📅 12:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22270">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfTQinDaTFnk7QW_0DaF_GyKuBQHxecnMDhc_Jq9IXNNmQiwlUEDbg2V8CF5Xu3ulFEnBT7bkY4MzeJZ4AdRMT7DKAVBrDra4T2Kt3_bGWJbimFoDkvZW85fWzess60jimd4OtogoCZAMNeW97Px7SADDSwpLxGinCxT7nmV8cgKcF51DVZQSK2YQu_q7vfmlbh-H_wMOVadOJqeDqY_OPCU440TZjNyMRyhX0wF8j_kIhh6bbrTj1dBJNuOcg5HDUqwHODR5abJWFLqGfOMMaqbpkj2oQwFmzZJAB4TI8oJJc-QHy7fc9ZCij-vSreMuNVO5GZ9yAVW0uRl4fc_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دنی کارواخال کاپیتان 34 ساله تیم رئال مادرید امشب آخرین بازی خود را برای کهکشانی‌ها انجام خواهد داد و رسما از این تیم جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22270" target="_blank">📅 12:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22269">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=ai73lw0gFsw82qJrie3Q3bVNRernAawi6a-pPDdBAi16ZAW81Sl4U3iROVF4XN6QwZJjaZQ3-NgQ8bLUG7VyeDVqivUNb0fWA6N02t6IxXBIondZHxFUrakfSVld8MWdR1dirDaV6QOk4ZY6BzrpCYL2Ss5QePWa162zXuYWzQhw-qn-Sjw1eHbszx0H5a1FcR7pRFZbWRQFxIY0fpqDv38LC2XuotQ1AB5uOtYWS4WhvAKEHIG291tT-UEUd32bZQAJzE-K6OECDhZ0DxDpyUy42qn8_iBnZ7hb10AlyuF4AuzwHDOPuo6CGP1yjJeMud9EAhyYgxbC-LzJLRmk3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=ai73lw0gFsw82qJrie3Q3bVNRernAawi6a-pPDdBAi16ZAW81Sl4U3iROVF4XN6QwZJjaZQ3-NgQ8bLUG7VyeDVqivUNb0fWA6N02t6IxXBIondZHxFUrakfSVld8MWdR1dirDaV6QOk4ZY6BzrpCYL2Ss5QePWa162zXuYWzQhw-qn-Sjw1eHbszx0H5a1FcR7pRFZbWRQFxIY0fpqDv38LC2XuotQ1AB5uOtYWS4WhvAKEHIG291tT-UEUd32bZQAJzE-K6OECDhZ0DxDpyUy42qn8_iBnZ7hb10AlyuF4AuzwHDOPuo6CGP1yjJeMud9EAhyYgxbC-LzJLRmk3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
روایت همسر ناصر حجازی از پادرمیانی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال بدلیل تاخیر در حضور در تمرین بخاطر تفریح با دوست‌دخترش
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22269" target="_blank">📅 11:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22268">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=ora3lZoJLjGfVkT-nHS8g2IDBTe4WzSc1Pzrwgq1fpXqlk0INNVS9w7iF-A7IS-IYoqPAOelvE5Sx9P9QxAmvsEeYm_aWjHY-JKmGzvwjz_GfEEorfrXiC_AGEGR0T5ATWZotTzlxyMExzH72j2mhPpymAAAP-sU6L4gBfTt1nmysleZiFNjy2Jn5OElLou8_iOdzX4pUT8-Voma5TgOy6ecIk4mhN1ImbEP5wYCzp3pUB5YcUaTgNKt0cVg2eU2BdjFdkKyADxqK32TmNcmAw01APqt2LQnxM6qU1d79TbYDNsIRsz5x_MxbmdpkI91Y39ok0KvjWAvsIumCa0V_yPP4-oq_IaKtcHL7jaZSTfUB73aAniaFAw53SBLNK5B1LZ2-ocdzBBsnq4Q8mz6Ovjn_fkfIpFOyqGrBWU9B8yqdSq8BAoD0QgHIvBulLvX0L8pe7gArhl6siFzPT3gLRG01kMfgsrcgQtWs1PmG5MxtcuhCeZGcNLKJWB4zq_EqkiPTzThRnc00AEh3yUHZ9IWrQ8j7KRChr5pLNpoD5SgR_K_HAvIPRTSf7QY9o4bWzFmBIxRo8MKXxAcxsXYncISRGrD1g5wEkhofo4JInfjQizBUgPoJ4lWsUhqLEr_zcS2pkYi0AdI0xqXxI89DEQlCEiJv-tR29qZI73JvZs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=ora3lZoJLjGfVkT-nHS8g2IDBTe4WzSc1Pzrwgq1fpXqlk0INNVS9w7iF-A7IS-IYoqPAOelvE5Sx9P9QxAmvsEeYm_aWjHY-JKmGzvwjz_GfEEorfrXiC_AGEGR0T5ATWZotTzlxyMExzH72j2mhPpymAAAP-sU6L4gBfTt1nmysleZiFNjy2Jn5OElLou8_iOdzX4pUT8-Voma5TgOy6ecIk4mhN1ImbEP5wYCzp3pUB5YcUaTgNKt0cVg2eU2BdjFdkKyADxqK32TmNcmAw01APqt2LQnxM6qU1d79TbYDNsIRsz5x_MxbmdpkI91Y39ok0KvjWAvsIumCa0V_yPP4-oq_IaKtcHL7jaZSTfUB73aAniaFAw53SBLNK5B1LZ2-ocdzBBsnq4Q8mz6Ovjn_fkfIpFOyqGrBWU9B8yqdSq8BAoD0QgHIvBulLvX0L8pe7gArhl6siFzPT3gLRG01kMfgsrcgQtWs1PmG5MxtcuhCeZGcNLKJWB4zq_EqkiPTzThRnc00AEh3yUHZ9IWrQ8j7KRChr5pLNpoD5SgR_K_HAvIPRTSf7QY9o4bWzFmBIxRo8MKXxAcxsXYncISRGrD1g5wEkhofo4JInfjQizBUgPoJ4lWsUhqLEr_zcS2pkYi0AdI0xqXxI89DEQlCEiJv-tR29qZI73JvZs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از تکنیک‌ ناب‌ودیدنی نیمار جونیور فوق ستاره برزیلی‌تاریخ‌فوتبال در دوران حضور در PSG
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22268" target="_blank">📅 19:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22267">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJwiV_S-Zh86JfKecbb3AoCUsnuv_SMsssK9o0iKlhC20qDK-dAu6LD4UsVKbdWnjgp7k2gBMsw2st4djJcALQ1P0nEvVA_jL82PhtLIelaMWTM4DfH3qNVCYwWOR1M_6lHwSuu_3r2LTiKRukGRQQX3bdSCTCMkLUgvQMi7HEOraVAD94I4XKXV6UcORP6f_HfOb3GcnFpj9mOwG1bZf8Ti0zFGSZnvhlqf5U4s2QH5FdCQD_mWVkgP_C3ijwcFX3BzEJOTF1Si_br49mH9pSHRYyKS2b16Dh_BUosPFJUF6Rnqr3thezN26ZWmM6uAaBchagrfZJkNLcey2NOJhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22267" target="_blank">📅 19:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22266">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFYk4AgTrLjRyWkl2btTtoNX_9SRj8M0moo_RiOzQEkleSJH2Yvn5TTgNJKABc39f7IUHeZIEdIqez4ahzPA8pCuthLk_-zB7NTaOwJ4Xaoj_P6AbGxVxXfw3u--hzOUBaBRr4qCM4Lg6GA-q33ktydhULsQXm1tBLVn7oinbSLs9ViwMsiD-3pgNNAZ72z9GJ8GmMknIvAKIhaAFt9aLHuuhYPEXQkSd2iS81Dktl8h8CMC0hwYyZLKREXuYgrFQrxs377YBAUnc0L3mglDmSPduV9XT60KBi4Gs5GMBuCg2gOPk5ab9adtDPa5Hrp0s8NOKoB5fLwlEZqEmWZHqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22266" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22265">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDWFOolOI15wufL9lh5fzzZlMCdo_ku93kL_wbzz1BMBSiuL1wCCnstQ7GHiAP8k54MBPPF8QfRXynu30pxF3xmYfGTWA6ESoIhuvHMyu77Dq7HIKFkuE9Xu1u1eMoc6dCj4II31db9WC6SUQKU2kFOhnke256-HZcBZQ_llENADyCLEA0JbAAJksKTvb-4MnUzCkM0UqbIWuI6kmIBuqbMIbBI808UjUDp9zc5SKhYTJacLm-hy3eo_2k1RYYLQw13x0Jo4LlGsEbQY_UaKbHEaIQMN0Huv8eaZHExAgMq9EJaVanTEjILR6bUvovlfJ9DNK2PvduiJbE_euxVWjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسمی: پایان راه آلابا در مادرید؛ با اعلام رئال مادرید، داوید آلابا، پس‌از پنج فصل، مادرید را ترک خواهد کرد و در تابستان، بازیکن آزاد خواهد بود.
‼️
داوید آلابای ۳۳ ساله، ۱۳۱ بار برای رئال به میدان رفت، ۵ گل و ۹ پاس‌گل ثبت کرد و ۲ بار فاتح لالیگا، لیگ قهرمانان…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22265" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22263">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRkgmKF6C2B3YwOCtDLfM5EI1nesCA8BT7O1LkFxcC_XBUPf0c36tsZ5E0vVdKXqIpD35qNDs3Pwetq_YPV8Dh3DDYKQJdrnaTIq2HjJqwJod0Nq83TUAU6-CYIGIKt2zk5mSCVVV48xfCvrV0jbkxQtL6QF9sNeUje5HOG9OAYrZNG-4mLYpRbpa-w2ZdTvQA93cZmnHw4CmM8Qa5iDckgp2KDWObjkTUcLQ8uV6Tj82yQ8g4F1VFtqCbO1xLxp8or1FiDe9h8BXqg_UW_10vTqBlxqY5RyETa7ThlifawMNyiUgnv7xzR9aF-zzxOdm18nXxNdnnJW3rvuDNSpxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22263" target="_blank">📅 19:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22262">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRi33X-8OqzybTftlJwT0otLe-lWzBWOoPVcuXT3SGHsvxD4uuh5fDFDrVDGDK_50kUc3uF_HTjhrWylnvTGqA_FDd1RV5FOTuoiLmXPnekBOLVOIM8UaqD3mU1UVGRj85R84LXb-VtA37Xp6l2GPXCpIMPkrZAoMEvwuf1DsrQPtKnRm9FYRWh42OvKiS6dqKxrY3w_bQNvBM2Fv8Sq1Uy1CRy6ZrI1K7AOeM471vM_Su7_1rS4NU19InQh85fNI686PQPLfSIoD68yxuVCPq6AsW6M6OJN7AqIU5KAdJaeYaNoAeXeIa5K_1Y7A04bOeu9_45heYgy-z5RuarAxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22262" target="_blank">📅 18:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22261">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zrt_hyMRM5SJItNqWQrCgTd39wLRvw_Hs6YyHwQXjeeW5HBWdxTNj5AYkiS6v-2IIdhkC6mnhbzd9m0A4gdzbG_uSHlvGpiD8mOsxKH-9_cLu5qR3M3ivMfYpoxv5egeCEjw41YsBIKJ5DDAPKlVfdIsZc4kNtUK2SCVO3burdj_YzhKuZELcp4TkYRSVcIDhgV1_z5OD5N-0teJLrnvhYnLT03F2_88SNcV0iZYEzCo-fTD6oSIzt9ERCLUaCTlj3-OK6DH6IyshFmgdmwBkdWssIHKklNliU4pr9iJauzAXobWff8mbYQK6Bk4ULc8QO82OrbhEGItPbx5EWjUOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22261" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22260">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRhfLqmGxbtZYRdDMpyrmn4GTnDn2gxFEHRCxgg-yDd9kTHDzRk0n8mJO3VRGdnjuLS1JHnViiDjXVaoL1mSAsuweIu6P7aC3uPXX8vy_y9Pu32uVAEI4SlLd0vcNy3aHHTMGKJWQWc7MGPSPHLlBPF-Y4M9QRsOhQti3bpLtPByWTPI53dXu_rt0ncsDV3nwo-pDNgbxI9F4x2k4HcHE8AgPuUQhgX9x4j-xKuzTuv5JRTqDJ6oZMx6_YoVXTUFhi_hT35CGcUR-p8uu9NGMrjHmyCDoxQYH_eBDY_RX9a8mN4SBjLcZoMtParoAOfkwVfkz3PZ9TDQUrzhobMpSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛
باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22260" target="_blank">📅 15:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22259">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gm0FrN8cfBn-PQLG-NGNAA2Egtgde3usqrBlM1i-Tr-ZWfqYSp7AWfVHfugQg3dNq2pV9EH6Bx9acOP44My0157a2C8ZYgShDNCO2pbwI2oSaAo4C2iJP49nKvIh-Reyq97f-LCJ6-jpqC0ldKEV7F3UdbkEgGrc_zEY8oM1gvEWo_u2IOfPt77m94pCqqOWExudP7nXb8gSz0NSLUBjGpaapjJCFnwM_bvOfB3NKBkV2mjWHku5xgjYrAOp3s3QtUa3mtKMtSizL7FmM7-d588V753-B94n7jKNUCcSHfFHX5Rq6trCESg5QIjqjZQ5oB1FQyvsGWKJPoDjsccPWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22259" target="_blank">📅 15:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22258">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Scgci2cRh0OR7AQdOIK6bVtxs_albqzGTCB6N1wFlrFrsix0MPYean17ZK_JQXlCB5xrMh5g782DGVWwruKkhrlSYzcCuwSWKoQmDLOVTFeDQqU9otcbUxtMJE_FspZOMzs2hI1ImYDScFFSKcjXD4aI20-5KUtb7iRXEmuF1wmoINkdyL6-uFXyJ_R-WVjqQ-6OJeaUbxJDUdXErVm4_oQ09zrQfNlTZMRu6zuAlDQTW6W6lLAHAIKyoLgIQgj0H6-zmTmU4JTT6M84pGCsg1wWcOjnQJC2ZFSaf0-DvNZxEHoafb1ni5jJcsAjoP_ZPSRfJgwF4WBAYILPuAdfxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برونو فرناندز ستاره تیم منچستر یونایتد به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22258" target="_blank">📅 13:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22257">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKbZhQxN4BKchG2eF_VE5Kban74epgrArnV3ml7p_awWIa6eRU71LRGwdurIzkP_L51Cjz-yGj4HnQ1EfWIzgrXd4LDHD7YaegPsBPHxT8lLNWvYuQCAHA9Wknee0KoR4fuFCAK9ZjKn11OZZpxNbIg4f5V7yTn7Xzp25Erk4UorYdJL0e0cwF6w0Pj89vS3x9tNdb1Lequn6c4MbV2aOrkUwF17_o7YxLVf9wcqeSy3XE1_zrdgyavEjuaziD3UwOrImNfKhPMDVyH4ToFtc1JeXVvkyOYJS4JVlTb0tyeL-Lq-ATi7ROSbBH_vfUSNl-PjCqmxuXIiGUBlZ2ffYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22257" target="_blank">📅 13:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22256">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNJPtgZxfyn6Bai6D4due_EwW_hxf2ZodZ-iHqKWRNJqdhv6u59gIJ4cAAQpdKOKmZZk82fDIv1AGy_SiDVvxq3mU7AFmaq63AptI9_41WUceFJ8Y57penLjUPROpFoV3MbzmXAYJbLPpXc9o5rO9FOHunxdU5mrr_KCc4o-lbyquRniF04mYQx2wIq9Z4V0rZ9DUOt2ObH9LsMCoF2QW6U08xSsUWU-024PjDBLirG27T3Zi0llFH-o_6bxeq83he6z2v7jrC5dxn5oGMY0i0FEkCq0BDqc9pc4V8AsXCeZFzBbXgbLxMAJZ7wsr0ukPGRoMvoaGYWC9EBTiQ-O_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسعودپزشکیان‌رئیس‌جمهور: اینترنت بخش جدا نشدنی زندگی مردم شده. دستور دادم با نظر رهبری و در جهت رفاه مردم ایران بین المللی وصل شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22256" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22255">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDx7muwWPclwevGth8vjdtfuPPfGZrjRHLGxc-81dHvQLc6h99gwNxGULHGU3CbaplSUU2oAQsAXHIkh9RL7fRP_dxcMPTX60ulak_LUPsrtQHKdWPgkw_kGeGAcDAG1rudxRWLkGHqTrfu8g1ahC-n4-9lXuJRF29FEpm6zmMNb9hltUtpGDYGBBWyeDARsGbgsoh81LdRoMlW1YjP8SoBcyHRem3aDyzs0-altBdG0QsU4siGShxToqPC77lCCeVCFKXWwigC-6bUbYGXYkul2Gz8tRKGDOUcrluhNF179URqO3IfzJWB8urPuuy9M1rBtjf7CIHVDNiuByWLdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22255" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22253">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0AKuSbet51OoNRAjCDmK00oiHsFu-NcaaAL0jL1L1er4x7j_uwObVm45U-Hf4FSUtxZk6q4-1yzyvb4j9Eb5lCoHU-OS9tZX-f-Pq6sQB113D_Czc96ApUqNjQHkW89G0N1HSmFbcJggOZzafKHDN7n41QkVnqTnOdizlPAA1AhNKGtgzEky1glE9xPXhow7urg6X9_RrDLyioUgFyQql4jtDQWmlEgLwp_fk8p0vrbcaVZsY_yS98L29WcndrIJh05zbmt6OF5aSrIzIyhbWnFEDRj9-FKsgIOETwvrK5HZpH5oq5dxeGu0Q3qY2Bdh46GbuqdiXBr5YsWD4MuPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فکت؛ کریس‌رونالدو به‌اولین‌بازیکن تاریخ فوتبال تبدیل شد که در چهار لیگ مختلف قهرمان شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22253" target="_blank">📅 13:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22252">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQKFWfhsZktHVlbuCYbv9x1QRjaph5QhdW-Jr37qUbIQcXUVVoUv95zFjaZf83UsNt0YVN2YIQb6yNKy5qkPVizUXkQvAErDA4RG5dkALChiY_AvM2kJurRTaz4ER4aKHGClCxaAardFQ81Ocl4aqs4PG5nok4v7-fQEcG0ttl4Zlqxx5Fl5zRMoR0GU3J7Sug4Y8S12OyG1pc6Hgn83MqAuFvmuJcMsIvdwIgr76nSgjPicBNj3WSIVNk-0OSSzLYNLES9tMewUzb7bM2bXW82VY2Tyv0iTGN59h39h5ZdFbHdPkK1kLu1ueGasFCCBjfi84rOBoWPjxzzO8TbNrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب فوق ستاره‌های توماس توخل برای جام جهانی به تیم‌ملی‌انگلیس دعوت نکرد؛ توخل در مقدماتی جام‌جهانی‌نتایج خیریه‌کننده ای با سه شیر ها گرفته بود اما درصورت عدم نتیجه گیری در جام جهانی قطعا مقصر اصلی این اتفاق خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22252" target="_blank">📅 00:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22251">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j22zm-kT4HFH5E0dP2BvB6PWDhqsJr9PA2WHq6BD4o6IEtuFodGEzsgBbPo_KsGXXmY3JMywjLF2ysTGexq9lHaDIorkgK9WFId-OUksSWuOV7jCvTgt0dHHi5pi6X_AI0J5rbrVQipzXWmW2x3Nm212MnvnA8UQ8-Mb43NbGF4xFZAoGpAwQKiFSwQRLuw3biCrRt7KSHMk9jWm0UCBwmD9kng1MWZy-RBLJiOK5EjnD6wfT7_8NsbMmOPURlmZ1s25TnQufVYC-GYIX3q35ab9qAYjaAvSGXWjHisISXS1T4lz7g80PhfISHbxfDHBnp1PgEUj2FjhUw7Z-GFdVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22251" target="_blank">📅 00:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22250">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vd4kKMp-Mv1zDJzMbQX7yRwGIhJrHWol0wAZlWc-FUVq153LT15c6TOZNmbhJxs9qEU8hBFlPNuNPcfNrHiX_9qePdf8uPF8D_130P1Vvef8xUcWwaLZud6YAgGxme3OBBjUrwcEK2syinpiT4LtS7RAJxdEwwTFWg-Mj1e2YizcIBtNmSXV7tSXvtMLMlJDixPEyMWRJR9qJXU_zxKo8rAucIlLV9gkTIGVXZPlVoqSkqCph0pLQmw_3S2g4vxEYJvPx585cmIzl3M5BrmXzqMFlRwu8hNTqP3cc5Lj9PzpLkSP3TSpbMjxDFdd9ga3Ty-gD79lJ7PDjjh6x-ItOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22250" target="_blank">📅 21:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22249">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGOr8u4enVlDU-VU5U8JhHlZRC5sdKvx08FoOcHT-II275BByorAkglY7RBKBgO8rXEtDnZXrfaEVo9X1A8KF9_UReUeSAQdyMrXTgDnthtoyQGQ6S4ih5DPG3p1uZFkKZ-FElLXc5_BkbPlUppStRWzEsmunGrC8M1MbiWrTs-329cU1Pl_Vo_NgAYYSS9XA-BBB6FCEokFH2Q2AXHFoh7EAmthmehswZZFJlfYU2fnTI3bZkIZJVkqdhlH1_-Vhxv_Ri4gf9Bc4n5lrLez7mV5rJBcQZsD2UiPqjS9iVJMMlPOuc5ayxCESbzL39khOADgRjYbaCNmjpY1eUfY3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه اتلتیک: باشگاه رئال مادرید به داوید آلابا اعلام کرده که درپایان‌فصل‌قراردادش تمدید نمیشود و رسما در لیست مازاد کهکشانی ها قرار میگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22249" target="_blank">📅 21:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22248">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZcE-ObC9us2q67cYfd8XkXdJkOKm_i5SQpGMzQxhHbkjG8dn8kWURqIuMNNIhR1lTfRipE4E-I-X6opUJjNuop-lMfcHCGZ1-AFdjZqHTwcDCGRPjwALFNhNOa4c7AGFzKbtxh3UmmhvOg6hX-Q8eo0n5eR9CAj_vLK7T3QjQNabWcpMUvC-dlGOu8jfiOeqTJ_xIecrgwJzXCcpkbrQjORbv2DMzR5DuLld1-55XWFi_nYxaCszuw5_Lcd5Ui_cR-kjsqvvpSEn0O4QE-ta6RQw04Npw9-iV2UDpG1y6uYF0qpEJbmBnIHwj-8hwzGrNCMoeAOwAiSCJ3khTAliw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22248" target="_blank">📅 20:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22247">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYQ9Pr6hJmL-ryMPBU8YAWljt_sKO0VRDQCzs1qfrBI_IetXcQ0_A3eaGOF6CXM6tCzY5dtXHhpQlCRceHAdINVCw9yAQceC1yJlX5peJnivvTuPwUyQ5PVyN1PqE4MmmvcyCx0aFKNVlWq14LUyAlCnH48irPyRyGjg2e1rHqnhnjDfkWyrgkUOeVI7BAs-CUmrjhju7Hz0gZNdRVNZm6FGcqbz5Yg99CrT8cd_tt7XQp-gwkzbfn9towfejZs0s7gM58W1j-JUIO221RBPMH-JNg8NaCWQWXbdvrvk309SkqR3Zta3XIseIfNVV10GWOp5IZAuLZjGNB4_FEGlIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22247" target="_blank">📅 20:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22246">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7G3cUxjU1uaOuLIfkAsB1h1nXf5tNYO4WCqQggRasZpO2PEgV6oaBd_dmcsx0UuoxhUu-58u3C4TXyTy_nC-R5NxuYtdZnTykWv-s8w-1FxVJZuWAqJqeSPElIUI9MHHw1x_TM9lpzK6LHucQXXCdnobdxV6OKciAmxg_wZfbBE8gG9Zfxdu_0MZ81wSVv8w3V_LXZhXZrKIU9sBytDPfanLsdjaW-mdQ43Idv2klwb6ZTpR1t_q46HND-Y7N6mB6QXYNIMttqjh5ghEMkDQEmW9euTCEITUj38Eb39cUeShe5VO1dPMCMWlvlA-98LpaMVdx1PUuKNBIyoKexzKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ایوان سانچز وینگر اسپانیایی سپاهان بعد از دیدار آسیایی این‌تیم به‌احتمال‌فراوان از جمع طلایی پوشان زاینده رود جداخواهدشد. سانچز از شرایطش در ایران بعد از کشتار مردم بی گناه راضی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22246" target="_blank">📅 17:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22245">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=s219Km8JiWH_JKyEN4ZLoURDQv2ddduKZ0GDlPmuB1zlvFcPodUXAZNcKzNVmDS79ObSc77muwpnClUqQ7hQqSFTMcjbjHbWMMFhAKA7O9hDc4DgyhYGF8yizCQW3fYD-q2uzWiMPDPqC3uNVgyrdoH0qImQnu53ip2IiowR_0FwhjmhJ1NLPKgSMztLQ-BC3oMhbczFXGpDRVVi2B5fnDejAcueBRXuooEdtGm4ST14KQeazWDSn82KXErslrHH5UonaqN5u_slFlmK0wcu88WB73Zp0uz7uQc7qysH9zNqmQCbFRlOCyCiHZCFlhdSR2XTN0GC69yfX_THVseaCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=s219Km8JiWH_JKyEN4ZLoURDQv2ddduKZ0GDlPmuB1zlvFcPodUXAZNcKzNVmDS79ObSc77muwpnClUqQ7hQqSFTMcjbjHbWMMFhAKA7O9hDc4DgyhYGF8yizCQW3fYD-q2uzWiMPDPqC3uNVgyrdoH0qImQnu53ip2IiowR_0FwhjmhJ1NLPKgSMztLQ-BC3oMhbczFXGpDRVVi2B5fnDejAcueBRXuooEdtGm4ST14KQeazWDSn82KXErslrHH5UonaqN5u_slFlmK0wcu88WB73Zp0uz7uQc7qysH9zNqmQCbFRlOCyCiHZCFlhdSR2XTN0GC69yfX_THVseaCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش‌بینی‌جذاب و جالب از فینال لیگ قهرمانان اروپا امسال؛سال‌رویایی و تاریخی آرسنال تکمیل میشود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22245" target="_blank">📅 16:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22244">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJY96xipd0FMhGZEFwqEsM0y8dt0UJinDYGJ4ek2mOqklaE6QpD9mqBRsgxEqhIC5KtBK4zLyBnSQoz2eQ2tNjbJN_eLU79MOb_H_IpsKU2gsCCHRYletf0vI-G0IOKHvoX-q13PvT0yqOfcDN6Xs4i0Ij4y7oIVbtedhbbfis-MEI-U03GJNyeUiqWeDWFLTJ6dNPX8mO23BO2j_WMUgYEV6RxjyN_F57nVzL6NN3An8slDl6yEUtEozaGugu08ooyHlVGLacxPaWJeysYVL0u8o9HJc-yWBBCCfZo_rU9A6RtGVfAjNup14t8EPe914p1kdyxLGtVtfxbEnuC0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شانس قهرمانی تمام تیم‌های ملی در رقابت های جام‌جهانی2026همه‌تیم‌هاباصدر؛
اسپانیا در صدر.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22244" target="_blank">📅 15:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22243">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRaBrnrAo_z4XsrvsdkGCRani_yLPY6IPhqMOrNDgjZZEib0l8u1LuTMT2x4OE-_JAMWmAuUKp1-iRI_8LCbH-4PV2EeUxaOMC2TFxRwaey06rEoUFw-IxE7ZNHngSvAKef-T7m1t4qK0XH8-fwRKcjYmotMV4KbfKFjbxhlJOlPopDXy37uBq9EjMgSupYAzRz0-3YXqSyPU7xTkfSsbwlT9NlQDBw0DSZeArtRcaM9ok6K47Hi2tkExigygQ4_3Vh7QNOaeZGjNSAr0eeNUucQGtL5w2WnfUqve9GvYsdmET_OY2Vxictx7xmYab6XzUzl6GkoqkB4JUTXe513gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22243" target="_blank">📅 15:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22242">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmH4kLUb-jb6w61UKEQ3ZobEuWA1Gq6pX5pBzjcRGuqCsdR9_ItG82MmV-XbfK0nFRFCJhgbAKSCD7JpO-WY8JE30heN2kDUgDdP6v2uN_t2JAO5zm2Xf9cSkP3bUMcqFbzufH0fW-_NeRaxf1WKpqI-3-OMDGAjUoBTH850AD4GO9I2Z72aHIsQO5QZUk5qAZt_cBXsLjkTuQ5YhCCi_ASoke3v2VZCZXRBK9aKMUtkJ6Q-4SX1LZB7GVC65KSOrksce_YhLnIPzK_utBs9uGqtiUcEicU9h0YsiUO0CfLvyrokn3UDg1Mdf7MxhWd6D3n8EH4lwvpdMCIp5A3GVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22242" target="_blank">📅 14:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22241">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyOqvy7nQsrcaamli69VLWGmImFNrLF84pDGAQRvV-PBB6K-M1wWHbh0KJ39I3sUcfyc-okYZzxQPqLQm7nnjSJSbNVdv4x0jhiUNCX-X_nf_dYgySU1CWM0Twmwl3IiwC4mWKtZCOwy_R2wg910YNKTTxtVU9pnen9gjD2wXJcmB5qcKmWO1ADU0okF5vNoaNvvknOHFmlUzZIZtiOTMV9UnkSa74AcpF8i_Hx4Usme7klJQ-7mXoNXckYi6xI4tCkfWQnG9SP61UAudfbahpR1rNK9DfW43hdIyjvp8q0U0r9nEM3QI6ynjDHAkyXXyv7L3-NwTuUPJSv86jBIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22241" target="_blank">📅 14:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22240">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9W3y3ze_9Gk1-9xbQkg_-lgP4zIMlQF9PdvaaLqQ56upLatBnYV8HwfaE7jfqSDYA9VSY8bibbI20zkqwDlGDMolNYXpfHNMERq3WOfetgSQ_ePxKis0tavgyeLg9e7-vXZC8AhKV4VDhThitUdr3whqT3-xU2v2urDNlfbp1iX9uRAcfORtZaRkH8tLxArb5dnuG2a_YQFxAfS4rLs3Np5UNOGRTO7mTrs8nTjHGm2ZsVGCnro2Yak-o0jg7wKHR0TjTy82u7n_kOds5V6Qztru_kR0E4lG64yngVf9LQqHhRHQwR0Yl1GnxTr6f0qBygGIf0fbtFWYeiXINajmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی تا سال 2028 رسما به عنوان سرمربی دائم منچستریونایتد منصوب شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22240" target="_blank">📅 14:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22239">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qungz0A1sa3iLD_EWHUJ0-PMBifB55TYJYRPqlROah9CAtf07VKnd72R3y0goBpbRHRhmvSs4PjE24xohrWJjCS9DYf8MVrzF9hak3uIN8mR4jrYf8Fx2RWIO7Jes0D1weKqzKJ-GbO8gAKvYRAUObU9X4quaXkVZ7isOP1TS3ZZszWhJUQOzNli_7gc_S38r6X1P_rObI7RzoeFwL4DgiJuzMaal63ENjgQ0K0w7YZT_kl_Utu3F-iF5ENbTYYhfGw2k-sK8wIcxNSL8pvwIsa5PBpHDqx3L2Lgmg72VagBcpIU47t0H4qwMqiN0K0Rt-7gxUOA6ydJmCD-2E9PLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22239" target="_blank">📅 14:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22238">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BafSgfBgP96PPR7cMnTN4qMM1F6Dear0GAeh1bZ_xXKavOI8emw8eRKHtIZi1WYbTw3ZeqT1HfWqPLor13f8TDjh77qUukBp0hZCPrPm69TDGk-EmZqvSB8f7yIfmzGRDt5BuUlVVGlXKBceI_IjVrsxjg773loZDasPEDpNvyYpJ_Gb_gH656VdVppsvydz1pjC3YP_IN3_zmsCDC9LiI_eb4gHVw4_wzVszO7kLTOMv4vRI3K2vyb4T0xFtY6H3yMidNjZMj5MVlWusDL0tpephNsDgv83D7fMrLKcvtnbcnOoIErtvzfX4cmL8_3ZZqTqRv9DqV1SWd3bDn-2aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22238" target="_blank">📅 12:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22237">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBuFDa5eK4yXLUmUz471S3aljSrw9EuweWC-npo7KhkcdTIT5qYAG5DseV5H8HI-Bwq3bm3P-M5TGzNzqibbNynsbQV-4WTLEc3sqkj1O1gMlOyzCgWYmMJbMOBQkolEtAFI1iRMR9jG0cekpARM9mRsPdSdWJSM5ZCIf2OeMcKmp9U6PFZjhIQBoj_Zl6rWfNjMgDujGo7CcHOwYZ-lEmCrcuQkfIUZEONFYtv2plok163RTIR09psYsnM6Vd4B55EA5Wod5ZFrs2zVNmDM6Kt5pnRHHj5QPfstzH1dQNfAjlpvNmWoMl2Vcbr7FYK80KElfqNw2lbpsEcJixfzBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22237" target="_blank">📅 11:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22236">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_4siNmyCdofQC9mHHtT2KIVFtZo6rmQCxJgT3QKR1EXCMm3adm6e7BM_0O4iJpMBxTTg99cmhk0TgTiBhqLq9SCNGrarfyfhEMN6KZZ3TllfTlAByegb8PO_K-lzDIqFU9H946lrSJZf0P5jysYkmh5TAKWaB8wrRyfc9GnBCzaL9t092s84MZcUTn1z7ja6UpYMfywDUl_-cGiy6VPpIPXtaKzeN9kiDrXlH-kht9qYJCJTOAKKMfMMLa75rsPfO70I3j5edB2_I0Ic0TjSmrwy2Gby11j3LdWMyLygOkQUje8Vb_xnVcgcEmkfq0IGjAMjeyxsuTrZcQYxf4rIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22236" target="_blank">📅 10:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22235">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JejimM_5ZrNAhvcxwQ86cvMLRkVZEqZDzotGjSjOG9RIUnu4VHOvGjv0OMw92h1bvvynb8Aiu4zqFzyiZdhv6MuZjnh032y10Hxu7eT_coOKOCiQuOr5CgxED98YhG-BNZhZKfkg_XJZ1nvddprc0FJdAYzb1lJQ3weEc90uuj8-HxAdhITEsC0tZVpguDdzM10bkvr2tS_qcio7y6Tf5ro1VWnqtc7yLr4bJxYLqpdJXSYXRxAoEm59Q2-2bSA6mTKuPKgMeV1QKRSOidVY4tulBGf2iKNczY12KWhuiW-TqU1UPAxm4RRifeq3ZEv5_G7WYfXalW_dXYxcqc_6FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22235" target="_blank">📅 10:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22233">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xx834DDDKQnqTX_ViaLxd2fvkYjcAepYteOvDnNxyrspNaOCLs8AVtriJoruKN8BLyntbtGghNxfbLCKT5q-XUg9RxXOoLivLgCKEruC-QrHe01TczTerQd7_8zFlp-arbfI8d1pqASa-FDKNP8al5R0DxlfwDJswGTy04E6VCSDQIgcsSMCSG8ZluHAwIJNFWauGmoN8gTWoBWG3CMFoBRsfZcNbfjKDZRkdFk541ldUbRp2RsibD1BHatrrorPbl82gEXMkFxfWNtaVfK_Lrq0nPacl_l8dRgB0i6JG82ReuLAIWtDWqyD15_8w_xPRzrKoPiGFI_ogdZU7SzGGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H9mzAAoSKffz_aXaWWosgG3wXA5ZaASxlbVrwvZfyKGbX5zLTNENmN85kmRm-F7BOPiJbbY-yiMu1jxpSe0vA6YvLjkY9jtpIRjFB28wdauR4LADrEK_jb9KAg_k_LfBueU0hObj-0Z_kreyJramljQQNyPgB7a-lxYh7BH0Pt-MLvcIUCXi5kYV8eveInlM2uIJDDs8UIrk8mESHJMQu5XKwpPaRgs13XHP2S2R163lrOPvkazmEPxlseagsOqvL7TSisGZBiSUdgX3b5Kc1aaEAIKPy8Ib5GIp9i6RMKU9J-Ui1eLJIrln3Gc5SA1eBoEgYHzp9VTxOhAHwWdcyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22233" target="_blank">📅 00:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22232">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22232" target="_blank">📅 00:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22230">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a3V1tmKltL9njcAvQQWmHH25xdjFjzRtPmm0KUrdNvWBlwz46rI6fjf64XU8QZ1ShQMLESJWDr3k7gBJVWEX8PpXP2TrBYjZcF6wa9oAmIO_MLLmt7ajxjJ22-Vr5885ISD1DbJKamiFuqVzvhvebaPU4gpEMU4r_UPgbltbGyooooTgz8a7mJ8EWYGcMQj4HLWNbvL4cCq_zx0woWnQvZhIZhXSHJ5E_tWceXCu5NKyJvD6wqd_uPiU61V7oMaU5aYiqbuCyZUeA6q9nZjyWmVBqmLO4E3W2avGx5ePWW6G__bd42Cuo2ZS6YtZrlcY4oyvxxadVeTT6w0hykbJUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmUn7g5m80bpSQ1Ri2zwWbcjdCJ_nLS0B7XKZcO0i0TuM7dXVCefE7I-E_2yErIsTdyikyW-AURlajOjSuUHc3kBjdY5q_4TWbH3eTt3TXvXUb57HJvl75vw9qsHtO5ks9vJYPLUXpxBPEh8LGJhmmGqyNpeQnhmIhmax2ukDIfgS0uhI44PTkGyZrX42AhZLAeAeJDzp_gAlsEuRgqhXdJgMoK-smM4A8Y3VGbrDFG7-VQtR88RrPr1aSE3vqb7XbbIkOw1nqq89xA_ldHyQ-Aa6GcnazWR04aA-32E1aBEz8tPXRX4OQzNVaL0ktDE2DuDQ4066QW_CW2wMPEU0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
هواداران پرسپولیس امشب پیش از دیدار با ملوان انزلی به این شکل ازدواج امیررضا رفیعی دروازه بان جوان این تیم رو تبریک گفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22230" target="_blank">📅 00:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22229">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvU5cb-cOhBAPA9gXzIK-sbS6O5B8i_kNrTID7onkYPXTa-QqSi9tJfhTAlj7fqdtxc_sZmLgyVs0rTuXIR5Zo6eWy0iYpMDmLiri2Hl_pqYTtk-vuYH22UbqevFxptZjoet5b_6O-R9Y50DQgDl-JZxNYGAijdtqhutPFLscGCMGm-87CNFN3RHzTZjzfXiUyuyeiTfTMueAsVi_5wJYWYLYx71xjWdTYUG69HBe4H7uzCT-xn5niIET1UfYVfyPtaDvL_6-vXxvUxA482URks23OhAXD21sSd7RFekGovN8BzC2gv9BKhomWcI-uCbuFC5lTM232YhiBEpKq2cog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22229" target="_blank">📅 00:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22228">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7hXLibnlRrnZLpsDz-AeAaw3VdCm9uhqN6fuJABb73tG3yVq_h3xgGMd5soPteYfMpP_JBDrsmsFzqMoT9qmeBKo5ArjgfMaYqIFveDhmLKFIogFe3BS103XgnFZqwiZwAOHuqSjiqEttzeZtSeSfDloacdhuH4jJYeBCPW1bm8vWaVaMzey0BxmXmnOFP21RFZL93QcQfjU2KKyKETSuvSoKtNUqDv0moUx5RxAgF4JjmI6bVIIuW5KxH7mZaz-YuLakLzBW-KMCsfXaTgwJH65aC847QUy1f_ohRugkccRi9TxXtfy6GPbSi5pB2zVI_J2t-sMC_x1ohyxoi74Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
والتر ماتزاری سرمربی سابق اینتر و ناپولی که در دو بازه زمانی تا آستانه عقد قرارداد با دو باشگاه ایرانی پرسپولیس و استقلال پیش با عقدقراردادی دوساله رسما به باشگاه یونانی تسالونیکی پیوست‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22228" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22226">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOyyTOe1jKGxiJu0cmFR6srZ_wldwHiAo3RlIrSQVuWy3S7YECHMjB54AWx9lyOh52cUQ-pQNovGTxkr_XcV6e2_VJFZCFtwb22hviPBP2hR0IO4h5Se7Ax5NzfG1avLnNyuFT8tzcXJEd6SnIuYDRStsR8EiC6YmYk06Prh3wNIaHIzn0nFpoON8du_gdUJtnNxAIdLG_tkvIbNjGrcW8UeYSkiQxbw98oqDO_Hxg8z-hpK_iTFMlQFQxpO5WJbHbiaAuEumVKdt0APwr6iHqq-j8XXRh-DprMtyIvo4THmNbKRN7tm1UTer6buwWAfhopaRniecIAfVlslXlKb0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ النصر عربستان بعد از هفت سال با کریس رونالدو قهرمان رقابت‌ های لیگ برتر عربستان شد. قهرمانی که با درخشش کریس رونالدو رقم خورد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22226" target="_blank">📅 23:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22225">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvZfzl_Lhn5Y-bMKy1BjKsDqlRfbKrBkjswr75zelr_epYv6hfeB8s4CQ8xk65HxD1IJFR8jnfwST3cKF0SUyC4MFtDY5V088OsmDi12JEMvQNSuyFvbo-RXYa6Ps1lUYj0AMPGiIaUF6hUa3H9oUytokJChi8_bOo1vP3otkq7rOOcrt-rlfuUh-ga8kQMoWxcQSeoF423cxwtTEMfkqLxVwks-2Wf0G5Vs-eLqY87JYkPvehgaAWg3obCDiOgdAjCMF4VyDx8_AsNoYVo9rGHAAEfw6CIAYewGri836wf_lcA_CNCFGwzQcqaLCYBsO60IYx7136S81QWe-rkGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خط و نشان CR7 برای رقبا برای جام جهانی؛ دبل دیدنی کریس رونالدو 41 ساله در بازی قهرمانی ارزشمند النصر در لیگ عربستان؛ این 973 امین گل تاریخ دوران حرفه‌ای فوق ستاره پرتغالی بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22225" target="_blank">📅 23:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22224">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d569523e34.mp4?token=LtzPe07o_8kkbbZhE0wpaYhQwx0B3eEJ1bhrQNsZk9l2gJZPimFAd7LCaTFyIxgmRcaHSJz98LcpamDa2Dk_j-wMm1siS-wwvXJA-ShKdRHPSwNuN-oHzpCpp-jrfhxuHPaSx_lyMFxxtNwiLqP_dLXK1eP9-a9dU6_v9FZtTzdjvgLPsQfn8FVpkKt_6WOG_y6GifIzCH3XTnEBq6EDR1mNhPcAjDiGVQJlCryipoDh_ZmDIXJ81F09wY70aMuYVLf5wEHK2Nbf19JzUT51uKqD6Rz7xHb53CRUCX4XYrrzleCg8Wn860HV7ivlWMSgbC6vM3RVqvISvD3rcSqCfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d569523e34.mp4?token=LtzPe07o_8kkbbZhE0wpaYhQwx0B3eEJ1bhrQNsZk9l2gJZPimFAd7LCaTFyIxgmRcaHSJz98LcpamDa2Dk_j-wMm1siS-wwvXJA-ShKdRHPSwNuN-oHzpCpp-jrfhxuHPaSx_lyMFxxtNwiLqP_dLXK1eP9-a9dU6_v9FZtTzdjvgLPsQfn8FVpkKt_6WOG_y6GifIzCH3XTnEBq6EDR1mNhPcAjDiGVQJlCryipoDh_ZmDIXJ81F09wY70aMuYVLf5wEHK2Nbf19JzUT51uKqD6Rz7xHb53CRUCX4XYrrzleCg8Wn860HV7ivlWMSgbC6vM3RVqvISvD3rcSqCfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22224" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22223">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=mP2B80nu_rmcLGaXy7D9HFMBov_oOmQb1ONJ7PzNU8fajPxpRjGsVKeicmjQZAgxBWvLVXr_JDBUBEbd3OEIGElMxZiHABIuNbRZVRVIOu2SG9B-C7tlHUniXz57xPf_7ekT3966LZoZQbSO7YVAGc1myy5Xr7fbnB28PwJ8abbfWJT7noE-37Xa0v2f4u2nxLgfm-7Zx-m2RpMtDfqjyzBqDs6vH_Pj5GuhvhzCRgTbsusrMPGzQmRHRpeLmf4t7YdtXZZ5OF9_BMKfZ2tEuJD26ZVeKDHoQrCqZGDNN377MDtwra3HoCWz7JLkvvJdvwiJqtxgUQtzovrDcYhz_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=mP2B80nu_rmcLGaXy7D9HFMBov_oOmQb1ONJ7PzNU8fajPxpRjGsVKeicmjQZAgxBWvLVXr_JDBUBEbd3OEIGElMxZiHABIuNbRZVRVIOu2SG9B-C7tlHUniXz57xPf_7ekT3966LZoZQbSO7YVAGc1myy5Xr7fbnB28PwJ8abbfWJT7noE-37Xa0v2f4u2nxLgfm-7Zx-m2RpMtDfqjyzBqDs6vH_Pj5GuhvhzCRgTbsusrMPGzQmRHRpeLmf4t7YdtXZZ5OF9_BMKfZ2tEuJD26ZVeKDHoQrCqZGDNN377MDtwra3HoCWz7JLkvvJdvwiJqtxgUQtzovrDcYhz_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درصورت پیروزی النصر در بازی امشب مقابل ضمک؛ این تیم با کریس رونالدو قهرمان لیگ خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22223" target="_blank">📅 23:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22222">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WK4o0x3SbOCyHiYJc5hP43qHf273jZSm_SMfg6FgDnt_QQBIoeKrko8dgOSZjCg9OF4xR6w2wZOCWLPH2-YrUsodt8QDVOMnidBiGYyhZScoUBtdhW7tCt0b7GI9vwsNu4cbK_bP3vfm1zkBUp1V9pnJXDV68eWbgTxN9UWkEPnEloS8WrHS8NHBcSOX-OC22We2w6FapDtcBAkfSdkoD02uhE2jgSv8iP6JByJGUpSXPjAwgmGPzk3rJA4Nvz27ByuTDah7mnlPjWME-usJPmnZ-G-LF-KJwoFKhrvt-QFJ8T9YwYbv3MYfpVVjojZ5_C4jko2k3lkQNqypdMfdYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22222" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22220">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wl273JHT3zxJ8h3GEtCycxL8mMj-ZEHbcBq4HFMUC-4m6JErQ9ChUl62eWUTOgVd-GWVqvWypEqupHXIcNUAIPEf79x4ksEg4djXLbIuqNiCcfWGbIp2JtKuyOl8jKxtDaHMTWKIaLs-E7C79TTB51MSntFFzL35fN3-qw3hqOCGOmuOdmOQbpu2kkJhlhAjVTPyp-RXQXEhB50EGBtzXUhFMUCICteXLyeenUCOgGV35u6ene71bLJGW9GID4FCPGdSOPNtzpUCKgmEmJOMSzca2LzixBusg3K4QInXrfTjJ5_Ay_WR72zq4kI9rRPczXfo3Jjk6TALac_vgg5D5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام فدراسیون فوتبال؛ باشگاه استقلال مجوز حرفه‌ای خود را از AFC گرفت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22220" target="_blank">📅 19:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keVMzw2Pw5XCJLH8yecKKzsZxZf0VfYDLV519lVZid7WPZDJ9An4YnF3_NV_miGvzeZg4ODhDnkUpf_OAhj3STdmo4YXzRpS-QvWV4VJb9SNhIy7SLCwoXC3EvJb-7PHcDO66R0LFuHGqbKnGIR3YSnqr_vw3sVmkD9SIOGQuOh4iSIcti8q8ScHNfdBuyOhUdgMmVoyCqBemk9QLcH_vxA8Q5QRCGnWeCeCfP0Mt5zIkCWsxl5Z3b0lXqbDp1GofuAHaHLdbsw3KH-sFrzCuYA-IQocP923HgETXHI967B_LeaNs3Vt1oAFwQ5wx5DwkU5cixAmc_AX3dN0ujysDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتاییدیه رسمی کنفدراسیون‌فوتبال آسیا؛ مجوز حرفه ای باشگاه استقلال برای حضور در فصل اینده رقابت‌های لیگ نخبگان آسیا 2027 رسما صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22219" target="_blank">📅 16:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVMbAA8gsAKQ7EzPqPL_uMynXNxuvA1AnybIdpZN6zxjhoDIgLGIHM5ZbnFuyTpzczz1-OJrMo4wF4b3LV14kfwpqYSqXh0Zf8U8b8lZCatXIT9_p5SY70pRcDwxibw7eQCF8W0VWDxXxu8a04hLtOEsyeFNPcadffhUWig4bfnyKQeoJgQ7WnOQi013FrlfqMbSi4WHCzkIkYoPzyfSOnsFtqit1G7hSYgr5rnLOYulU6TKtGvjFLaenco6gRE1C8v-kbH5_XqVEOYCK1cAbMR5mSoPLG3QhI28TLgCukIP8_cmc6P1ElGB3dl5NgDOXF5EZ650_3D88j00G_ngsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22218" target="_blank">📅 15:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKIs3lR1nNEhktog934rcMrA4Yywsmvqq30_5Yp64mWXjkgP_YDvQhtGrV3rctwqIhCWjGdydIJYRSSItdoF2W_OdYIjWSETBSjpbrc89iOvupDgXqM1v3H7c3AOTDFQpdgDDLbOtzBSlYE-GmodPAY-qI42fbOb2i1u3barXxxnOK8cYHVBqrfDLD6CsbukOa2k59I_DJrhhdrLzReOZMBP6yQ_EeMjDz2fUhkBWp9G_FI60zLjks5D--wHnGRdXVudiheGNsOaqJz_ekjkbhjDfHcwyMHxiDKtKH3BemJLugx0LNhadMg9SmCEQzBuzabKOqMnu5UAmavIpfHvKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان 22 دوره اخیر رقابت های جام جهانی به مناسبت چند هفته تا شروع جام جهانی 2026  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22217" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXERhUh8niZf6FBl7Yr34dW3GEK7x_4XqhHoMJYM2r1jlj6RbaV4vtqpWh52UOgUFjkbvwTiy07Ww5fIZdWm0axDuk3TDTTPGrLtJ-Pal3byysMrZzr-qfLDOWBWycbAo1KXqXQBOMw-j_mwqrw4n98fk9rnwzhqv5CwNVlk1rZjxqWmiUlIsY3WIFUErMIaeTidrLURp19MSh1vg1Cksdrve9LYgyqJLxVhvqjVkQlbBv0_G0cb32xMrlgnJpIj7RlUkU3CH77T0DcpRps9oFI6xnirXC6rRAdoLbnKZ6iIUOryspknv29fAscw_q2jXuc2Vx-as3Txfo14g6wgig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیشترین حضور درادوار جام‌های‌جهانی؛ تیم ملی برزیل با 23 بار حضور در جام جهانی رکورد داره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22216" target="_blank">📅 13:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22214">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KdB4uHEOH2PHYPxF5dY4x3JBx9pUb0Z4XoujjkoWx9WCymyopM28LK-oSP7_gwiwiXmMC-dEL3ZzAnZymCvTk2-9YOpGB3dnYNAsKsl6L5WJr1gytlee6PEjbcBcRfmUtbC26DinxqjGneg_3PRNmmeGZ_KFULSGQwBODYuq2rC1RRCmNhpgEa0ypGbzRE3TOgFClcqdTudpVKd1GfsDVfK8z1h_4MvAFx3XWhPn9Y1WP-m6q-_kYjmgy1tsB5Fe4AUoas4mLGE8NaTgd4ZQT4ZThTod20CsWgapDGUfcrFAvvhYHBtYEf0E_67lrNW6GoN0eavG5U0IyDubjal8_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ov12Prn6Ecxf7kU8oWkfXuZ7-Vg5HyJK5iPdoXid-Uc_ZnLxUtqqjVNXdyfUVoGAg8Nz-jTM7RDeNmDfby7tz2p2iC1fhLk76_6giybows3JONp3ITcf4b4Fw8KC6hBJasuhrrjggK7DG0hbDdNuiqoHmKMmGgyWo2iDrcqoA_ZgiAPvl6mz5wXJBZYjk7ioMzGLdgK6eYSKzvJAfODcIed_rHPdoosVxuWEOcWgJMxm5H38KmAOxRO9Xm-hkLyAHPwm4SvXiHwk4QXggbzcxV-DHCS1Nr_W3tGa-cGIFmUaQByc0qwO2RtQsFIzNr4j3CwuMb51uJ1WocKFuJu3VA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇧🇷
همسر مارتینلی ستاره‌برزیلی‌آرسنال: رویایم قهرمانی آرسنال در UCL امسال با گل مارتینلی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22214" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1x8qJ7NIzJPlzL9R8LXOuiuHgHKb93I6RfM_EddPyjiWXHs8C_DOjKrOSFRk_NWQybJr647K-GMxHKG4N2nw3avrie1La3bWm4r7GqNeu5b4IWH0BoHuNoxrAB9mM6t3y8N1aXEElyB_-O2bcP6oCrnoeG2keg7-gyAw1dfuiMkikErsgWUkyP-6-yJO4KT0y17FGr7dRgyEXuaf6tGlpVwDv83qdy7b3sh7EAvKWXdpwfi31KtyJATeHGbyF_RzjnuI6DPAPEc32FUqM39HWq4q85X0xpP1XFAM3zBeUcA_goCwXRl_LSQ7JnnUAJgvtaP3khLr4nD6SRttgc2pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22213" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmK092ai_BXw2J_E95zo-r--APi_BV_0hblKVkth1T_35vU1LiUWPDNa9JqN2z2k7wtnNSb6Fvc3lwBp7MaTal0GU04Ders1-iq2xt9XqEbkBUlG3wAxhh2TExpO2GqxA7C0ALd7hhxuBLfJj-Tg_tSE_UdN4hn8zKfDoZr1MPWs22nhhsPYwWfm3ddH-Ob0RGDda9uaKha941xEgnME76k0y76iX5lxK7OUMFrxDJ0K4XdRkDSdD_SLR2Pla_AwePfKnSP6f-pM-aK0VYAHYS0FrBrBarZIzCr0s83i2GUOwb7los1LAYT1C2qH_BoLV1bzkVo2hby17jd65kTBUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛
روسیه با اختلاف در صدر، ایران در رتبه هفدهم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22211" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1-G7QZU11WdXXFf6imRobKId8vyPAQzMtv_Z_ZEOuX_0UpUbTQqbRunlfJCEVYe89vd6C0avb9ZHQOr_wqXlfmfgNPfCY1K_pGVRPsvOarHrOZZOUg5cPbPNd_Y2XJHC65yDsQQ0QEIrSQZ3tieQGB0k2GAB1DvaziDz08kPCw3IC__7bej6k0Xk8AFfY7TSH48MkFjxKV81pFZxLky8yAP-1b4QmvmoEXpxU2dzEvC1pNyON2Zip-HrxGRIgk7LmXXpeoyxUGvFd_rQdCJ7uEjR-9zcSy7CFHeZ6dnRlXeVNXhIl7HmyHqTLWDZ2rFqLEuyc0kPI4VyFEWx4uVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22210" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9Q4MJqXhnPJqUkdV9iyx6RF3onD_LYPXm6PeTiluAH7uGDhAvoFeP60tvoN4_XXODwuN0fxINZ-bbOi_3PPjh35wkJpfudrmrrlCBpaqUNsc3_9ke6yQrEsrjy-vq4HMHWZ2YRiAC52DPmWR_MqwYSWXIG1tyu_x0cVe2pYpiGlIa3-c4QyDYoR72nD9XBYEGtFMHog_tP9re_uxjtLL5ABkb30RaL9yDMsrSRTdJwidJa6ZTdvl6aE0xyap5sRDPQLWqtxMxPAimdoBUumFRYF2jfwgVakLNIIjuusl185gGiuNuZ1C5VgKagyGDaG1lKdyFDQJfgOlZJzlCEt4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوستون اورونوف ستاره ازبکستانی پرسپولیس در پایان تمرینات روز گذشته تیم ملی کشور از ناحیه قدیمی‌کشاله‌ران دچار مصدومیت‌شده و ممکن است رقابت های جام جهانی 2026 رو از دست بدهد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22209" target="_blank">📅 12:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJqhQweKFjwdE5b95dJHJvQ3dfnWAq9uY6oECOjLOLRNDgXzI7OKJsiaF8kK50f1KnMH0ZMcxCZAdiiwj77cQ1_-P4KJq8x-35k_s6quctxYVhCpE7IZVGpjjcWzLn3MznJ4iVxy0IsYbV98wt-oNoXltYDqBU-X351NqBeJR5QxsWVMl4qWl0keXYOrUwCJAteM-65afQhg_Gb7DVLRewRzXjj_hS--QfP97HsLEVAbyjc_vQBmzeug5Dls01nYA7zPCs2TsvPlPti-hVwHnExf0ysdl_06Qbb23WdXSe9hae2HmSqw3BqOvVm10HEgW28cUIsiofvoTJAwcU_M5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22208" target="_blank">📅 12:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfxVDCc0lzAiVAP1j8lPCYzJcj3IfARgV5V22So-15tXFVoatjnU7Ot5sDB_ix-3QDfV-vlXORsBpKJ-GllpbtNiZh6yUj6hpK3k_kjYd7ksgM8vYo7pRjw9VB_SveiKg95j7yu5_-Sc3R5vIkSEmkj0xTWmcXAOPie45SUzsOkD-21rZXxr_NRtlIBm_O314Gt2NH5-bM7A9PngcfdR7pBKA5Ojxw0MaTHrDe3NglWG4TU13WJISKVS6r_D6IppHPhCcS0ztg1Vm99L_oGDIkTLLd4XYh-b7Qc6HAC-_9Vbb2h9uJW2y4ck5SjlWRkvRm0QOTN5_Qgm9QyhVFB-LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22207" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITOoBzLOTbsc-YrowQq2NM0lqMw0zlDXqFe9A6gDrQlNG4sEfBa2ioCIStsFOfrr5Z9oO_d0xZ9RMlypOILEwePzh7GF41TaVYloYQckg9fUTSmGWvzS6Q-dMhvYire_3AUbxs3TyifwtiIgmCw4kEoHDeKb4hkUF75SFKtLm0gsLXZaHi1qvo9uQXE8N-g-V9jeY_KHgw1xDRLBWWoLAc8u3MR-JRvmXcLxD6xKlR-2TWJv4AJgqwUVUh7mb4QowSPMGTjNqB15dealWzIeyTQfhJPBvu9d2tbsOIJiUBnYEg9YqH0m9xXXZk_LOwJiFrSjz6VuKJxn19WWZ0cg5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22206" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDdYp3GXwUz04PskuF-Yyhxx-8_fteuC1chN0wsbcfiSKspO1SlkJ3gkDAdvCpA0zs64udEG9agm3TClEcWz2HQzbzhh23mgN6aIAlmcx_ph-yAQZaTvZf9n_rv4WLe--6n0h-5NDmNZYwoUGApLEmWRQ7c1eamXq-OfBFz8mGKSv_MThRl-e8z96VpPGpIUuAQbfvU1QDjblVb1XO16B5dv_j0rdNytBFGHpW3DxpjKJYjD8yobljJWGOi2HfODAj6qV4wP_FyRQW6kyzROTGqS_dc5zX9-n3_Q3MDuBxwW24d6SAhoKSZv1XdkFAjX_AUyIIckuh7kaqjAxjgjHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخبار دریافتی‌رسانه پرشیانا؛
دوباشگاه سپاهان و تراکتور بشدت‌دنبال عقدقراردادی دو ساله با سردار دورسون مهاجم‌سابق‌پرسپولیس هستند و صحبتهای اولیه با ایجنت او نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22205" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22204">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keBdVIBAjPqoD7_trOfGKcMUtF-y6xWTtXEM0q8E-aSYsSuT4mQY5sNV5TzqTPY7Ad49a9x51TT3hZmdWh2jqYIDKXjVDTNQ7ZjdwzoOodOHWsrBiuvS2lZ_A0z17lYBOG14Xy5xi2H3RvaQXwT_j5S-OQc6Il0FW7F71ViPfdPogBO04ID_K4SD0GxaQYBFf1yRjZyPycIC2CWea2ZLh6BohImsHzYBjoj6LhrJwgw4A5nWWWWrzkdyW-QKRtuRC2WeR1GSdw_1CGkdBBo1sU1WE-zN0GeX4GFgwdZu8q3bYi-msZ1tEesKO0OnCFtheEzW_gKaUkIN_VtLXeC0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22204" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tz5yLq4kH4F6fFLpDchDxAooLqtFakTrMLGQZanmZzjtZhgpmeBwdxiwaobeod9uhNN0qsA8ItGgumkP7p2cz9uXKniLLqxhhZQJqp7q8OGBBPGFQk0r_fx2wOEH5F_NR5jNtljhwHp6Q1VJbHqTQs9PtZWs7N46aj1CwcsTMFApoZrvooM5fYfVfZJmH1-XF6b-5Ygz56U6k7rAifiei_tBS7Q1WkhP8wKxUaQwYiLn2wR3S88obnHNzWuFktWhonOD7djfdR0ySoIdiA8Irhae_Lypwg1kDJRP0inFNRIxG68i4iFYRBEUJD1ob9lCPkWwBtgK_kiCFAingeHaJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22202" target="_blank">📅 20:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tbca2P4r8NLPoF2mKfu3Xw5pV_RYBg6T9fVeibOtHhg6mpuKEEPCxAl7kxDPtVrOX_-LMFaTc2BZBlGc7IsfyEOHGPiI5vVTZQhpruuEPCfJObUtUvG7c-XTXDwRswo9J7pmRhGcJgPeeT7NwHorD6hK8UOZ-hw8okLhAZkMDz-lUZaN3L9zmYONnGCXuSPdTyaECDMtifUKtsdFpBC9vL-WF9OVOcTpEenYBaXa6Of_uRW5Vk4NsN-yNBjWItGtaXL5BHBY0l5Q5jiawWrhSqzbBXK2l1OrhR-ZjmdQ_80YlXZrmKdfkYqTGsX1J-WJ26aLkR4aa3f3RZjj7Hqi-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXDMlY1iAabCwGaOuO5ZdwzteDg5GS8fi9cgyKouCG5e1O8nCffvgtoBdkBmuRBaVUNP0XG0sK5r0doltfUx-VlzRHytJH-94r4GZba3tXB7DD4v9e5Wc28wgk3T8s_x2PsTWD-rOtd1mj_6aVsGSHEy1t5t6w5mg-7pVaGv0uNOWrF7ssZJuD8SwINi-nYi-OADlyoysN0exsoVZ_zjkYY-JBqbqqQVcAdX_Licb3xLw5Lxeas5nfCOuoOyR1eG7yXYg5QwFmGQWyclL5NTd_OJmMXzYT0BIHqrG9Rqv_OfL6HzX8HMKzev717s7C5WLGX9bBsxFLLT6RWwj0vibA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=AMK6jk9-RPGqbWZTzrW-wmarbZmG8tKBPoyfXk78LD9rzedn8HsPoHD1HH7FCH5rsobJ-wIzzxXQOs6PoZnxxv2tuY5zwM3SzY7HTcSDg01ladoiACf2v43vyv3EW104rwnpJcEQifdg24dNEq0Kj_Dyyy4Wl4FK2HmU7sZJkDwbIBJA3JTvYt0xChQZJzyNpVLxjmfmEZ6C0_egdAEqc3wFJLbbJpQVFNCVu4kJs0w3rV_r4eh2DyjMGxixw1HFaSmz9lBu979Tmvf2-CB-9Q8m_qofKz_ow8zuAtRbwQphG94Zhqcmwpt90NH-2DPP9EuZGXwsuUqHEvi2mpeq7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=AMK6jk9-RPGqbWZTzrW-wmarbZmG8tKBPoyfXk78LD9rzedn8HsPoHD1HH7FCH5rsobJ-wIzzxXQOs6PoZnxxv2tuY5zwM3SzY7HTcSDg01ladoiACf2v43vyv3EW104rwnpJcEQifdg24dNEq0Kj_Dyyy4Wl4FK2HmU7sZJkDwbIBJA3JTvYt0xChQZJzyNpVLxjmfmEZ6C0_egdAEqc3wFJLbbJpQVFNCVu4kJs0w3rV_r4eh2DyjMGxixw1HFaSmz9lBu979Tmvf2-CB-9Q8m_qofKz_ow8zuAtRbwQphG94Zhqcmwpt90NH-2DPP9EuZGXwsuUqHEvi2mpeq7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIYkiCY65rvny71rborwq176Vj6hei097MNJ9mjN1iv7VqnXRgBvGyLmsgj2jqDAxsNo3Oov_etRk4oXna3c9zbMTLPfIPX_TdX48nG2r6AKJDdglkbgsJlmiuYcudxCohnFYk5iFIbmsz8RXItN3mnTNyU_mEMXIGxmLAhH0USpTwf-jo_dFNCw60B696qps9_pqxRxF5MhkrfwafK_9BplHq-1-Srw3QsFWBq5yDT0GGe0zrq7SDqMQTRbao4IjhoS624n0iNJhu84IJpqPi7Sq0DTwu_5PcGLSKWuyIABjKcTP9T1AJhq-Rswr2z6NF2pbBnXUUoThY1x5od37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0N7gZRlIEtAjvmKlws_YxfIw1GUyRVK2Rof3pzaPra5nUEF3BQzEuw7jARsA-8YukZwlmEf0FtI4qxR47Jq6H45YD44-CqtH99XDx-cW6Wqlp5tngSHd-1SZEIYG3zd55a93ddyE1pXuSuuRhdtjNaoXosFc9c-ja86IOHU6u8RPKUKewHxGmJZAFIUArSFhtQhe5sP6RzlViltiqT6EksUPnQkUNfWQGamI2sZ_2QBQ1em_fVGa04uZCCw7v06jViioR4FcEImoi5jyJnor5MoXqmDTouKSLZYFBwqJ8BtKRUuJGgKvUQ0ZgDA2FPrHVVEVYiaiEkRqsV1U2LesQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN5qpndbXl4K7MXDDo_o1FgS6SjcKcNK1ctGDgf_tspRZ693hg-LZ19bfQwWbyZ4t88oJ1BhM_ZyyMixMujNlfI-_SL5B_P6fl61Gh3wXySI5zH32U3NBrlEJDLWZFuI9Qr95JXW3V9qUfv7z_TLBuX64RIUkxpi97yFzFrthnVPNteS0Rhwz5U77ejnu5IF-lDQiZuHGAew5DvtLaNO7lMjz0zlC9ypQCFRBrdlTP-0-Lfx6n_XwOKdjMenOVcY5Lmop86qXFA_mXOvMx39BYW88Xa2PsHi2lamAwIFiQemzdNoqRV2Qw4fzvEACP-1EHOseTLR8uWf1XUGJV9iqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMWi-IIDU64GNZDevcwL_gP7tQCl1bACFoTr_rmiuNpVyJhNJsnjPwQLvlekXA79oceGP4y9_3A9zfDhlIOUkrGrZ_qfVMwG-gPiTBJrpwDsNaeQQzcsMfcD9UdlJH-rDLFO3p0wBchqwzfbexluc3A8CERH4t-roSMf_YiekQI2kXxnL6k55oLWZ_xtfJznzMf8MxLEpItQHeJB_eNwy3xcw_JWZRR-vE5s2kQRe_sJCiO1AnEU3K_83N7A8Y3L95ADRG3JILs_k6r3m_E8LRO2vrsxUbetQXh1bY7A981dm4q0YtgaEGDdVUroSjGnGTFCgnX_gw9Im2Su0Gcjmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d7UzKfgxLoEdfpl_NQoZyHohnRtzimdn1jZs_jrAaUXQgh4ealEWDh-TA_iEkWQeJj5E28LmntwZgFJWhtCRu9SdFaYqWWC3tIZS2aNmcF3XVP5rJRjYp0cYlv4as2J79WMeVg1BO_MeWo8QzdrYhuAOqWJvVw0_wDf-4x52rxyQgYDWpdDGp1LI2ZMNjehdvaJWoJJIpWSXdUDvmZ9kQrxWs5m3IzavDIKWr1Wo2SgJGA42M2-fMY5xxYhBP4KsQ1G7IJNVOnY53nKVvXMJ3BBgrRR9t6Kev16pvYgHYDr-1CVgHG5EH2w9SQ7D8ZMPUmcJ0fV_Y5iwi5D5HJDtSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKBYkaIbX3dC84098r9oOIRksvOq-kUwZQSpxQJ3KQV2JGJ8x7GOUByAP6KOrc5uQPkWjc5QJSa8xvhudhgEFjZIcAAbO4uVq5Wlq5ieHeax8u3zNEfF8uApoZVDjBelYA9-wjl66UabuCZatCAveg7JoT2GEKDb8va9FpciLpsvD3Z7TxWbGtROIxl01x2tQIFNuKEvg_bYL64fMkw2qmhUnnUaL-ugWsjqCkhcs4SZE_x12jMvwB6UT14DtSSCMxoAeHaBhDz-k5ZMwqLPUChodj5Rubkgm-xmIL5sp99fC3sh0oPhyikRxojToMddH4dNbQdJLOn_KVgFJmid9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oza5BHGbJh8BlHEfHtLStbuEZuAPrcMTyx4VAxfws19tWTikP7v-Gpcp2x0ev-wA5wSkfadt5QDcgWmGS6AuO_C8PP6FFUPV0e9qRc6XcShrCu11Rf34YRv__IOycBJ5SXRBmnDWFwR9bHDWEwZkZlGK8IO2uc1dSYfEEXHde5s6haANkYXNtT8V37aBbbuHo0oqVtYzVX4UDdd1r9oowbgdXG_tgtNpdVPcqEE2kS8xksdXo7FuicQ18_eADuQ2MbP6ljrjz3lxE36cbVcw6it4w--Cm9ip7aJyF8c280kNdnySh4AvmCuL9Fs3iLnTfx-zf_iVx469DmwYz65m2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvuhymwMnCKVHtn6z9eU0MDFX4xeGSepYFe4udSnpALz4TOfNwGm46TS3tHzPjMrmCJy6SDcMegPdzG_9yQBoqbUWIpDl-F4xdphbpnFTRsoNKeRqF2yvf8ckRQqZgJZ6tADUetLSBvcyrSqkhxXSyMH8LSy3TWHEY1TYYttA1WppH8WPA3rd_6s6Zajj8wsjuR2pzMtttGMse-yMD6n-mfwyUTqrjql-QoONW94_-5rkCVB2PvF-dPkxBDHp5zi2uMyNTdzD-fwIO3mgY0Aii5yvYKaTPgcgN42TsAlE8m7dZzh2t5RsnhYqJ1kCcoJETvcEVUtpQVD4PveOZlLpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7zZl3Psz2Bx0uBpa0ohQzrPJJBNyK1ltWqRQPvhJFf8vNlJVnaHJ5z-DpW6MNyitNWbkt5yPeMKmvmEtvLJvGn7e70cKYRXjGDWkRswqmG_lcjrKKioSpOMAWmNlrlSNZdGdnLPHneHVyN1b0MVdfYyHUzfhewS2eYc9yH3rq7olJRAC-Cbk518G6KUZ0PmABZqEhkq-gdNzNQBltiN6e1b1e23IwoAo8SthnYtz0IHhvzOoGIXjtyRRn62nFPB9wvOvAM71kE9HWk25z4mG4kiNYWZtWUwuN33A2oUryB4dX8mzTvNNa9ZYYG61QWttuPsXc_E4gvb93S3kZbGuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIFFv7AAq7U2ZGk_ORyQPjRREL4g7NLqohR7q8CepBdlAVUDrhwupfBBZQ3B-WgEDNlez0ft9Lg4x5ZTrI1b8pWr7MTDwwMyn9iI6-mDvpMi9lRbXfHHIS9jKhA8aEbChsBTKl7K-U88X6SvcLveOJvVCeosmYzJjTMcN1jHr8Z-Gv_XXhEwmyHrjmoKk9dxyvwevcoMwcKXeetJOyhdqWRjJvnjJscrloSjoSlQtVFLn0ii9RHCb_sOj5720pvAM6DBCB6RNgu9qxTums3DXCj3U1yBgiKUnBwULeBo85yj7wvesN7Vzk5yYj7ssiid_fsUirFVTb3da6co0UV2GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
