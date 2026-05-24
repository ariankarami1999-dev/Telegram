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
<img src="https://cdn4.telesco.pe/file/l_SxlZhQW5Zv5CfqmtTi2t4b3xD8gL47YZUt966zj-76ClbP1TNTtIrWBVgNY2ySMgo8Dq4H6nSFsbg4b3qBfSLP7DVbU-L6fwHBuZu5Izl_sZPEw5OcJVT16DXM6CEWhkgwGfhzWEzP8Ns_Fi48SDD_zm9U0W0cE7Qj5k3hcCLzkofiSdDHAGXL4IvEdZaW0w4FKXpfiRxmnrDauzVGC7HABOrmNoiz3xmhKl0CYWywU39dJXiIVi1hRA3TkyJ2HFVzvATfSnUbGW82SgOqwMr5ICwc6-CIXl8UkAqdyYgxH96nH_aG2hNxqZ4tBtl-h6-Sf9Rcd3VFE_Q2jtMPOg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 193K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 01:00:26</div>
<hr>

<div class="tg-post" id="msg-22294">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK-I_BQw3lI9Ob61iS5lm37uXpJSYDv-hkEdew-QerucM4XWh7wVnW0FOM62yXUIsBrtndatAIfLuxOBFmQEfVkNvULAKOUjQXKgcOoYdecOnfGro5NRXjOgHSKx0pJB9dSEHskjIEvDzUHEC2tIdQ0aJnOYNshoUNenA-LEDGxyJ_MFho21FXwIB_-DUPri8wBxDDzYy6vnICcH0Vs52X5uD8K4EcyEpke8OucUQqjEzFD6cbW--LeP-KnUVsoUM2ic2TzErHsZOOM18z10jBhffHZJX8s0EDSbiX4vlr2zn9mz0IK4LqEGt6A6_P2I99b1nMv0osVsCuwBK_edLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/persiana_Soccer/22294" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22293">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCWDtZ-6TY1HYeNKjl4b6IFveCzoC5nbsDsZlfJyAG_0GHuY__mXUp0gCL5n8wEL44CB6VI7MXfPDR3FUqJGfMgX5xD4BhNDuGsnf1Id8Nrqd7gUQc9xVvkdZK1jxk2Gv26vELbBRaZPP8dx36b3LLbT8rMeIxQ1T_zyP3NOxqgqus4ATD3508E2bo4KxA9Ux22_mclgqvowQqzXAZ0Jqfm5tlwa21CS0RCcJMfI_ONXLZQeN9k_R1BMtwCulZ0sFg44hJQz_5nCZZoysrl5Mt8CjBFIxk_zwzcvUjqeXFm39OCXZmGLR4iFg9zdqBzGp2e4osBzZIWSo0JIObCD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛ روسیه با اختلاف در صدر، ایران در رتبه هفدهم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/persiana_Soccer/22293" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22292">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hM8owcGlDXyl8yEhK-sL741NPdag1bm14dqwy-8JtuV-Mn5UwXfLx8-_rWSgiEskCQCR-vwdCwaGQ_M8qiQZmoCIXBIJKvMmtwuxtnEnHDhnwQMXv9DDP9XoKI4n-RhR1DiiD6xTiumbVpNrOgykrVlrPMhV1d1fZUz-ZnpBI8w8FHw7SdKr20Pswlyhjfjz3zwu8_XI5VpFHS6FLpR3ABAbmlAc-a3Lpi668qnO_h_5yqe2FLE2lVSu5f4zYTA2locBroexjnA03yi0OiY2o2jls3IGvT40K7WK7tmbkfBZ-_PpaQU20fptp4q6qTqgGGVLEDN1ta3RzL0tVO8tuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/persiana_Soccer/22292" target="_blank">📅 00:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22291">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpUWKzSb-S6pjEX-HwafBmPXBybjP6Wjy_QTyjYo82JkO1xiwdgnzq3_V5I1dLoKdBlPZC6UL4Aa6KNtU1elqa10LyiRZUVc_GHeikOwA64o1ZQjy87t1gB73A4DriW8c4kJWSOeeCzHtx3LD4T6u8nLgk1JCPwTqY5wQv04xoH4g802og3Rx4Fzoxl7hI2cYDqMOrF2p-L_EffyE3lCVwdKzIQN8Yieej3RSDv0i2h2USwJ2eNWsoKQp4YRPYnG6sLLQXgY2oNmkogoaRQjuYFPLByeisa2Js8IYCyQ6b3PYuGV9WOdLwnm3_f_Imc-PyDpemn0pxa1krrU5t-f1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/persiana_Soccer/22291" target="_blank">📅 00:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22290">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbyP5rCImQuIV1L7R6YiEzQucAcQgHOt6vIgaVIDGDhzbWlBR8NYwlG8I_Kjzi7sDnPkwQj3c8yftP8erOGM6JP3VfJ2zPlB88IQkciTzjqAYu-jXmCaU9tezmGUUC1NgM5hTDd52VCTMdFlfrrswvyQl4nl15jq50vbPy0slcR1tqUJfAc7cl6YvkmytCuuPO-K_qBRWWlAHf9P0hOopZXoZnEV2wgVlnJmhzcmMARMe8mTEh0vKxvUuhdQ1GYMswIbpdNpHkk32ByW1ACptkqq7YgcgcWbw9tQld3lHhGOJkLp7teLbrlpvYqWANJKjH4G-29dV9rstARqFJHciw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/persiana_Soccer/22290" target="_blank">📅 21:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22289">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fgp9flRndDHijEnefALIxtHFzqeIq7xi-WASXHBiFHUvLbdzdkUeuAKSF0E2pkLlPwAgdd5HnTB8ael0pWCOSSvVddeWwI4qHfrfF3nH0t5K0fLjEadLnRIRYVLPYl6QKmk8_ZvDy_hQ8qrQp_OPKEarvXM_VDzT8VdV2O2Kepc3SCarI2iDcoWx-N3NKIIL3ei960kqa8pdShIjMbpPSgRXOySAwhNsTYD90Ul1ah_xMkBMSC2IHb9DFvnI-RrgUtBYd_Igv9qOn0kw9TsDQFjQ3rEAhsQ8yr_jwrkTagiWlXbfLX03zvRFyd7P4NRK0UXueD9NQTEuTQl7Tkj3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
باتوجه‌به‌توافق‌‌مدیران استقلال با ایجنت آنتونیو آدان برای‌فسخ‌قراردادش‌درنیم فصل؛ برای پر شدن 60 درصد بازی‌کردن او و سوخته نشدن سهمیه خارجی‌آبی‌ها به‌احتمال زیاد او درون‌دروازه استقلال مقابل فولاد قرارخواهدگرفت.البته‌اگه بازی لغو نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/persiana_Soccer/22289" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22288">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rfq2x-w7zxyhoqJGIOz3zuaNq1m8CJLu_Z31mtxRx0pBzmwJUHKnZx5GjbvOLbxMFVAOrpg5GDqZIh5pj8u0tpUPdzFCJWJnxjH0otyZKrLkkDI3-L-Q57EekQTC1gIcuzhBmzW_pVwSrn1qyELg5FwJH6OrRVloca-ecfUAJ9da3E3KMak3h2WMT5Va-K6PY9VcYYi2CyvCNJ-yx2FaKBeTR0Qm2TVNBPUJy-WZReq_TaNNwmK2vfZqc-SmZ91TYM19VIV77jDD_hy_XQ6Me6KEQj96XHTZeF0DIziQYh_yWrlaV3-kgGNV4opMnWIiKBrRGgZD0UMPrt2lixjYoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/persiana_Soccer/22288" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22287">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fD2a_srpo17oyOc6Jh7pKLfMroxmLEfoMVH2lZAc16TFuqGcpkF1G3uhkT1_5oYgSWk99DWLBqvi72JMa0NL4E25FYq213E1-nT2ABhFrrzKJ1pksnDQwmAZctgaCwVcZ1gwMmcxNUGdh9rQz-S-C2PZ8iZXA0r-93IU1qUK6FrtmNChGHIFxWLhj1xW4LmEgIb11RS1q-s_DHDyZDyMxExB4v1rbJ1ZO_C_0NiO7KZk-rw2dmkvCOPL0Hcuqc_68UgCcVby7xpqyzmNupzHQ-ZwpvMX-DNzTOkQ55M64KEaP6nwWbUDxHKFadfsVsNH00eFquRj3A4jJMZ56GuhFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رایگان‌بدون‌واریزشرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g3
📱
@winro_io</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/persiana_Soccer/22287" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22286">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSIXqnIHO9Uqm5XUuvViv5CfI_bEJ0JmQOHWsXPc3r0-jArkFk7EAGWDjsm6idFuzPNu47Awf3Q02rT6ngNVBDpbLWKwysHZlhRuU7pETIpurai5_bQT1as8nw4v8CA8ppZmmHpNNq8HbktnwFSE1tNPugGRh_tOMyV3RxrY3tjPaQmoEWGuOJbMMc_7kvn8BCUABiadU3EAS0FxDRe-jimZyW2Png44KEF1N_pgITyI1I5Qk3Kqe01lg5uVz8Zi9U7CKdirsVCOjKXs6ckL2fyTQwsfZQK8rihOuZHrbtAKNHQVOZazjUWIwFWetG9teME9pZupdfSDOlqFE2VNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/persiana_Soccer/22286" target="_blank">📅 21:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22284">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AmDYPcF6QUVsPsgUPd85HbHQeYmK-CcZYjNpYgjIcR6oz9Ju8k1DpOiBpE7ZhSV6k7AW1ImMkgx7rweVVGSm9_A-qsKRcQVj4pA8SQyNKnUAjCCg6VD0LiRhGjyo3rWhjq_5j9RZykmgUXg3D_GOJ3H_QJ_2rbpxjB9moYfyjsM7bNGJNAJ51wJ7H5RhlE9wruSIk7wNqGnlvwmLOq0r11VlEJU2x0pXk-YrlfCdJVkUW_3LDP86eivqneFd0_3uoraUC6-Fmx7Uk-K2xljpv_PD5lMt6JPHrVAhPdS1XxR2cH6wwLpVEpoWLorsGTMDxymb30w3C7ll_QhBZzyb_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZK65iP8s61-s8_kB3PX_7zjs6UL8fLq5x_kwYhI_YxZGjCmWpuHSyoaiu4AF1uT77IiXgKTAfiQzRKGmi9LrTQybP-W6l_J9MKE90cWd7iOeJ8WWPdvIFJTPiWyZnx47Ba2b403_9TOIbEwONe30q9bg3gslAjNYghzTX6MLtpSp19MntkSe670IzbSn3YjrvhqYgvFSQ1IIJ3Q4E1790sS5toNyRx5aY7kNFNbz1Qh6Gz9YxMC1OrfqWAV7mg6XyeWO7HuBV6sRs2OvBo1VJkS8xPzHXte0lCkPFx2lCQGAKUhP82i9kkOFaJ1aMCQQvIxVYrm51WexMfDo7bTHEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/persiana_Soccer/22284" target="_blank">📅 21:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22282">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5hsW6XPz2f0RXevfiejkdnhUm36gZTaaqE-IWBX7gjPwI_IQyquKKi8T9ZSs0ke1d0ARVcoOVZNWMleM9Hv_rv-ViN6fHwh5kCdd8d7A_YGR5VVCmZRojv5_MPqeoi5mCBRVxTuiG2Am13Ar0HKAAzauY-mazBhxSVIfDdJqxljlt3OigQ4H0iIM68u-uxRWyDRUeOCI5zJdzK0LePng0SNdBq1NxjzsXuNR5IgYBs7b-AyrBwxXVnky4yxUlUC8fC4_81nq7mg9GwN2dCXgs-WZv--UxNkA4vw0nQ0lOQDZuWeGLAmKk0NmdaRC2lkgc8PqUt8rVgNjtvNdfnJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lY0g5bsQP_hxcLZtvxxwBmfqjCMJZJehPD8SOwpAzbzGyVYUOYkBWEr20WfUi8xuEzST9yuqtiJ41WhWltW7lqtF4Wuj2MUavQ_f7QJFyH0k-YLygICx1lyD1F4lyKWqgZSS7gHUD2i5VZcbpNeVfLUjn3Yx9x9IgcEOg9fEfHK0yF5xERxSXLDyeehC8pBotMcIYUD2dpZyZc0XXrbBcx6gmUU5ZP3N_iSBg9dSEGWG3K9-RMH7BZdJ7PJYc5leJnJCZbl_BFgaDmhRkG5A8z4ICP6y3g34xsOvfdSHMROYZXRyG1rj2bY1ChYgyymp9Wkd422uUfxfOrplmgdEnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/persiana_Soccer/22282" target="_blank">📅 20:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22281">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYSRgwZzinI2HDrwrXWASX6Dyb7jPhd5nh4KCOQgSgk_sxjvMKCWn_sV8LdDAC73W_jsTz0Zt6qYfpM1P6pk1sz9P4WtukRaJgYCtxjJOrheQeUJeVh4xbk_cnCuxzrJW5KsP4fd-eoAGmJOcX2tCfJeD_WHCtW0F-xe2YUyxhQUyhu1Q-yId1S_XIODflx5yt25E1NNApY6jojtu_hNjTHlYwo29jjYXHUdiAr04aTCQzOj7PoklvTctMa-Uk1m344tzU9D-g4bZAXV3F0ZmVMlYq2o-6FDtdtH9PCqfPKOrUF9IJkACo_EQR7Pzj25aUEZwaZZtHEumcartYQrfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌لالیگا درپایان رقابت‌های این فصل؛ خیرونا که همین‌چندفصل‌پیش‌سهمیه اروپایی گرفته بود به لالیگا دو سقوط‌کرد. بارسلونا هم‌که چند هفته پیش قهرمانی‌اش قطعی شده‌بود نتونست به رکورد تاریخی 100 امتیاز در یک فصل لالیگا برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/persiana_Soccer/22281" target="_blank">📅 20:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22280">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DD--C-bRinMlyh2xogf_hcsfDgb9objtfg8h4qDuELl7NLZwNpgooojwwDZyiTX0bKVkMtDgOTalm7Yf_sSD5p-L9DOA710I6_cpyvgwf76fAOCSZ7dfH7UdGMXtNV7VtF2PpzZedI_QRV2VzeG6INY6wJkBJCTymTmuhGr3OM00eadp6ybCh-giCvC-YY9tB5PEv7Gqf_ekFWWM8IXvBALo1yFvvYDs9YkHmGk8sWRbtSLpX-ja3vVoVWRgLW5v7HyUH6rDSjRbGiyxMBR5fRAaPJEYrgjk6iH1SBLHKUPPtK8hY1iJlPUSyFE78f8weiOzLqXIIZTa6DoRD-XNFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ محمد امین حزباوی مدافع میانی 23 ساله باشگاه سپاهان قصد داره از این‌تیم جدا شه. حزباوی از باشگاه پرسپولیس آفر رسمی دریافت کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/persiana_Soccer/22280" target="_blank">📅 19:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22279">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJgvfVupLDtdP6BaccRO3tHuEyHGrVFUw64eNqtDS2IonzH0L869y2Z6nHtHCfBPx-MpvBOb9oA2acBaxl0liGAYdd3kA5eLVUZOC8AR9R2YrY_JC2j6b8V1WmdzErUFDOIAhPNb1IRQV_4udCjx5LJU9Tz09y-kePOA8YiK_qUoRMhW2ZBQdQ0Ipk4JrTS8MHlNIK874hQpa-hULlDKTFefU4UxJWoeRyR5Ym4MhtQ31Se6UZ9RBTAshuU0TuZXXtPbx2pCL6OSoC0lyC8yhhIMI4tyqgOA4tnNkqlse_hTVLZEdyXJAoTiSH1oqF3T9ElxHvfY3Iey451VcJCRPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیتنا پایگاه‌تخصصی اخبار اینترنت: به احتمال زیاد تا هفته آینده اینترنت بین الملل متصل خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/persiana_Soccer/22279" target="_blank">📅 16:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22278">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmfSRcXvRBHXDWE8GgAUz9sdWau_B2IH9HSF5eGBcQZo7QGLe9Pp7_uJgLfJbncww0YQKsi9r1p_rAxVKC3NODj0pNLKV5xscclK346EIyNSsn95zn9QSpaFpBu5OelN3eDGZQXUCB248T6o9eURRGKrK61RPD26D7x0N21TPbFsPB2P1a7ZJYReKLuf9FKcwC9zwS8dRRG2b0O-tgjr62ReR7huPF9HRBme1pUjv9nJ02DSFIZbPuE-CVRt1gKUzxUtwQcbh2QDmoE_rNPLRNwd1tEbGV80qFtVa3C3ceO7Te7s8FoLtmkDr2zltEnukGYt8UiH9F4BgBvqCRjmdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات
|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/persiana_Soccer/22278" target="_blank">📅 16:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22277">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky39U6JiwcFHjrmMVPX8KLulI7T7laKU1qYnNdPvgrUL-HWvT8ii7hIhRQlwUnObiP0TTDQMGNio6fIYyWeeSh_ZSTwK_QqHeheflOQqx4WDn6H4x5T0GIrovZb9TON5NgvO97Ql8bzRaPI9yZyp0D81643TIJVOcfYz62_0nr9srrXw7lKNn5_aua1w7aHDvGAgxoM883BvsNM-96elopft6wEtIgUd0Ct8quHfpilo2SQdfuIEEbksG-JXEDAUjcdNFa3ueKKJtgHT-3NEkKhnuNVIobvM3nJRfibM-oTdEkVE1OuqJJV6uQLqydaeiaJkOH5urstx56kkhNAvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هری کین بازیکنی فراتر از یک مهاجم؛ توپ‌گیری، حمل توپ و دریبل، پاس به موقع به هم‌تیمی و گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/persiana_Soccer/22277" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22276">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nb5mUTIiu0cl7PN3bU13ILulesQwL3nLptvar1VQgqXjkORANXo-7s3XQyC3WZ14RvkMkbmqkAnb5omX1DDTObopPtJfMEl7W4POXSvsQo3qbbXrLEWAWCtR8OXKafMjmTSgZy0Am5Ts8hUfare4AIBQCXU3t4mkKjF6Q_ZXu3aIPivQH0ICiqQGrn2ArcUF3eh98NeeQTSnJpfBjntX1Fh4nRHneS-zlerLtdt546pVsbyQGqTX4k-mi07R2ck1caI8mucK4XwbfvCuUSofBO8_uqXXJC36xi3OQPF4ECSzZGt7rehvuJceHfRMZLW8xPsrzoAm0GCAqXEUZ47W3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/persiana_Soccer/22276" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22274">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9q8acx5rfex9diGRuWcn8fOiQbKvaFCVFuzYKBb017osRUvvhG9h4qI0gcBgFyGFelG3E48jP1EO0eC61MjgPgeMU2G70NqDehMVYOK8k-f3Ca7nGEA1VdCayUrHquZEW_YvtRiidxIJ6Ndmo7j6VEyTbSqm9QBlL3VyKrfmOq2iL17g2T4SKF-N3up9OG4aXn5UUGbtlZO39JbAIYeRv6TPRptV5sTlLpb8XPMEZ-arBmmRVEgpxoKNY2MSCr7KNqyEueeV_2lJjIM6GLTJUV1N2YpFkfOsfymx4nFhefPHcypyOPt_ij2cFR4kNfQbOvlLiwmh1ghuRd9P9I7ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌گفته‌‌روزنامه‌های‌ حکومتی: اینترنت بین الملل مردم ایران تااواسط خردادماه حدود 15 خرداد وصل میشه‌. حدود 2 هزار ساعته که اینترنت مردم قطعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/persiana_Soccer/22274" target="_blank">📅 15:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22273">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTcX-M59TnC072x6dY8vhwhFJI8EfOUK9YFqmJnxnSeO3lGYVC8UL_atMjXiOSto4glnuchmpYNL_-bIC4sX2uUI7nMHWW8kJNlp2Z3jol06FWaQaewSVnADtR7rIiRkLBCcabXYqdSCwN-FtG5xLS2DtSgeXQ3AE2-S6e8ybYvJk_T852UTQidhXli2i9c94i0Du1Zh8a7GXzyVaHrHHcasAEc-Jr7rpHQuqBxqhqs9MsQYXrYmSMAk8NEc9qPrhkzpuvZInX2V1BPDwmG_dJ7cXSNrLi8WuSRh74PZPf3WtGVII5FgSFajmZ7u1RKRETb5MgzD6A7zlignHL4jKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در…</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/persiana_Soccer/22273" target="_blank">📅 15:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22272">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hH7z1mYDsCiHBNarg1jW_NhwhY0juUKqZDSmM6rs2wbg5EoJmwROCFVIOGG7LFVZT8YkoMwpmPFFRFh9iJgGwFQw7YnTCOlf7CddfLdachaWhPsl3TTaVHk_yLwEHUVOkEHU1k0RlFxUxEmMI_U66f-yDlhjrg0mctSrNrhnBd45I14CTk8H-E-rQqXj21kFwDwO_h5KidYWNlMUQVV3ya-PHgVlgpDDmjXdh1c0o-jXDfv6GxNevralmCInqeTIybOkj2I32UTm5JVULikVK2M1-iot4ZTdoOQmhZ74rfX2m2aSC8O0lugjb1LsxTuSPARkGD76Neqm1KIxUzCaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
درحالیکه وب سایت ویکی پدیا از تیم های حاضر در لیگ نخبگان درفصل آینده رونمایی کرده و در بالای جدول هم اعلام‌کرده این جدول غیر رسمیه اما برخی به اشتباه اعلام کرده اند که AFC اسامی باشگاه‌ها را منتشر کرده و برمبنای آن اعلام کرده اند که نمایندگان ایران از سوی فدراسیون استقلال و تراکتور هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/persiana_Soccer/22272" target="_blank">📅 14:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22271">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=WlBGEynB7rL0INyzIjXm_PKl8I2iUBgeIKUUlo4XgtLgX_yu5YscRiWRkZ6CFGyBoqCPKF4TJqNJ2Wq5EQFzi36tzolCEMgaOyk7vB7OU6R5cV_3pu10_fGUuWNFz-MQ-6tkh7BsMLzTdoY0xxcndLLYqEJIHclVOI28xY7BjlbAtsGAR6RyofEsiMAjbHm3dn88uwFioiYRn4mYtP0TVlV9l-qoo6B_rhVG3BiW5ihap9DMM9IM4bkHMoQ8jIvQ0FmM3aFhpt1x8BTto_EwXCvbeKhRSQMPABNO6VrXHE6-GlJN9oPRpWWOSqCj6uWwmThKH4q6p4bS1Bg5rAw8dGlPkpWwQnh7bcVFfngZZB4MlC4N_qAsR0ql3MuXvS8YPEoWEjPbGTBIvEyO8sjmi0UxnZvBiBVqqaGHAs9dlSkAy_Z6M73SSjlCO-1bMZdT6-gIpHPGF1xhloWNPBFxh23mRT9a36WTRBQZ3mPuThU_ShP1U-rRE2TwBeARHvO0g0Zds2b_gz49Z8NcYxtFx_XAXwm7tLkqHHMpbBPdlCZXV5M3qXp3lWbvoc1EPdkp2dk1d7HGdURehP-X_TXrBtJ7zMVcnG6nx8TiPHz1ByW5C94B-g6LXy_dV_fd_o5ebKSdQeoWDzD0fhNJ4RdYGjOEYyIZXX8OHSku_G0WQFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=WlBGEynB7rL0INyzIjXm_PKl8I2iUBgeIKUUlo4XgtLgX_yu5YscRiWRkZ6CFGyBoqCPKF4TJqNJ2Wq5EQFzi36tzolCEMgaOyk7vB7OU6R5cV_3pu10_fGUuWNFz-MQ-6tkh7BsMLzTdoY0xxcndLLYqEJIHclVOI28xY7BjlbAtsGAR6RyofEsiMAjbHm3dn88uwFioiYRn4mYtP0TVlV9l-qoo6B_rhVG3BiW5ihap9DMM9IM4bkHMoQ8jIvQ0FmM3aFhpt1x8BTto_EwXCvbeKhRSQMPABNO6VrXHE6-GlJN9oPRpWWOSqCj6uWwmThKH4q6p4bS1Bg5rAw8dGlPkpWwQnh7bcVFfngZZB4MlC4N_qAsR0ql3MuXvS8YPEoWEjPbGTBIvEyO8sjmi0UxnZvBiBVqqaGHAs9dlSkAy_Z6M73SSjlCO-1bMZdT6-gIpHPGF1xhloWNPBFxh23mRT9a36WTRBQZ3mPuThU_ShP1U-rRE2TwBeARHvO0g0Zds2b_gz49Z8NcYxtFx_XAXwm7tLkqHHMpbBPdlCZXV5M3qXp3lWbvoc1EPdkp2dk1d7HGdURehP-X_TXrBtJ7zMVcnG6nx8TiPHz1ByW5C94B-g6LXy_dV_fd_o5ebKSdQeoWDzD0fhNJ4RdYGjOEYyIZXX8OHSku_G0WQFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22271" target="_blank">📅 12:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22270">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3L9q5zTE1ys4pizdjjKYKg1JRM0SBIfX5j9CpaDn9MyNly_bpv_R2Hc1v0foTUdgOGW7lhxGrARTaloBRawxnGIR1s9ELsw821aiQdLrxyCjyyflW7TQTEk0UXConeHAHID0wwt05ibmEsSqILRqS8Vxq4GRsEvSPgrc55IWXhyUEF7TWF29R92NwDb8a5bfJVzMhxWL45G_JEMHdUf6pRTPl7hEgVCGngED5T41lnHMDq2Y3Iz2nt05z-oKuS3X8venaebFgrMMXMK2EWzq7910CY_ExoVYo_YOjx6-4JrrKCQDbxNMnCfrL39d9NXJYmsaeSw320NhEmmaHjBzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دنی کارواخال کاپیتان 34 ساله تیم رئال مادرید امشب آخرین بازی خود را برای کهکشانی‌ها انجام خواهد داد و رسما از این تیم جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22270" target="_blank">📅 12:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22269">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=XItYQMvmR7mHMSyPBONvPwE-1Wh2u5TaRgkuC7NpUTK2Xnjg2SCZ5IxQJBOX2NR86kkJsXtHrdby26ESdB-8_zq3Y6ktvGdHckMHZF0Xr0y25a61MCs-0qhwjxFg8GaJ-vn_yZpHXmGXitjsxUmoa66sutrwQMi34CH9ivNiEa_uMWy5FfAURH4fC6GROyg_4_JyayAjmGq-TkXrAlp1eqvbbm472yXlQBdX32lnEP8WwqMGuPHC8Ng082wEfCGr_qRTbjuM5srfu_VWmeR64Zy6BU-RmUHKItTxE0Q1UXdluwZwD2h6QLkgjNZesTnokJX56L_LckNNUuyCs237pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=XItYQMvmR7mHMSyPBONvPwE-1Wh2u5TaRgkuC7NpUTK2Xnjg2SCZ5IxQJBOX2NR86kkJsXtHrdby26ESdB-8_zq3Y6ktvGdHckMHZF0Xr0y25a61MCs-0qhwjxFg8GaJ-vn_yZpHXmGXitjsxUmoa66sutrwQMi34CH9ivNiEa_uMWy5FfAURH4fC6GROyg_4_JyayAjmGq-TkXrAlp1eqvbbm472yXlQBdX32lnEP8WwqMGuPHC8Ng082wEfCGr_qRTbjuM5srfu_VWmeR64Zy6BU-RmUHKItTxE0Q1UXdluwZwD2h6QLkgjNZesTnokJX56L_LckNNUuyCs237pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
روایت همسر ناصر حجازی از پادرمیانی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال بدلیل تاخیر در حضور در تمرین بخاطر تفریح با دوست‌دخترش
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22269" target="_blank">📅 11:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22268">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=PeeMqGk0hR9nyniq1t5o5EtLPKVcbAYtR33ZjujhTj30-5fH_qrPj2gxDqbAr0sC6XyShzmsTuVba1D-5rH0o89xQoyeYsSFlEbfmDoUt-pVjhv-IcbUs6sF_DwJ_FXx5zSyldRQ5oyEnTrHNcUn6bsikfP-snG7lgSuLBPmU3wgY7K7sb5kdGLN18WQZsQQT9kIFmV3RPe9xOStLe7pWizZOXO4FrDCAdj9Ye2Lw3N-pK8gQ23GWCZxqatPZd3nAl82UjpSjnZgWF6vbGIacR2t3_HnW4K3m-PDs5awUNZfPgKmgR6RwYmcXYKf7NO7UPcOkhwwv9SILzT1hiqQSUgDHA234qB_xQ0hgwUPf0163SwgMaqquVmQFkKr5cfSWXuXPKYfCLd5hKv3mipxMlUrDKvDZ_xn_ofCPbNnE9j8qX5OQm4sK70nbk8PoEIR2u-QUHVmeJbFH5mVvmVq9zEHTQJhrkp4rEBM_glkRgRdGGyj0HFtGrHqYQrIIxPKCL3OdvTwChCXxZyi8kD2r9PrIz7OgfJLa_XyDrtE-P-MtRFxezV6ct6ugw28YKXOkig4328ed4yFgRlAmMcll-Trd8QFIMqx_69eldVCTpvxqIT_OYqk966ApwgRTeUNARHHewg0nYsjHZUdNJmLy5FAdn1MIFPt9HEz__hSo00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=PeeMqGk0hR9nyniq1t5o5EtLPKVcbAYtR33ZjujhTj30-5fH_qrPj2gxDqbAr0sC6XyShzmsTuVba1D-5rH0o89xQoyeYsSFlEbfmDoUt-pVjhv-IcbUs6sF_DwJ_FXx5zSyldRQ5oyEnTrHNcUn6bsikfP-snG7lgSuLBPmU3wgY7K7sb5kdGLN18WQZsQQT9kIFmV3RPe9xOStLe7pWizZOXO4FrDCAdj9Ye2Lw3N-pK8gQ23GWCZxqatPZd3nAl82UjpSjnZgWF6vbGIacR2t3_HnW4K3m-PDs5awUNZfPgKmgR6RwYmcXYKf7NO7UPcOkhwwv9SILzT1hiqQSUgDHA234qB_xQ0hgwUPf0163SwgMaqquVmQFkKr5cfSWXuXPKYfCLd5hKv3mipxMlUrDKvDZ_xn_ofCPbNnE9j8qX5OQm4sK70nbk8PoEIR2u-QUHVmeJbFH5mVvmVq9zEHTQJhrkp4rEBM_glkRgRdGGyj0HFtGrHqYQrIIxPKCL3OdvTwChCXxZyi8kD2r9PrIz7OgfJLa_XyDrtE-P-MtRFxezV6ct6ugw28YKXOkig4328ed4yFgRlAmMcll-Trd8QFIMqx_69eldVCTpvxqIT_OYqk966ApwgRTeUNARHHewg0nYsjHZUdNJmLy5FAdn1MIFPt9HEz__hSo00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از تکنیک‌ ناب‌ودیدنی نیمار جونیور فوق ستاره برزیلی‌تاریخ‌فوتبال در دوران حضور در PSG
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22268" target="_blank">📅 19:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22267">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXgyTP6ItLasGFOnsUZWpjWL7_BdCml8nVTEG4z54wEIki9jsb5Hrd6d2AtQoSMwmWNJ9fWhOKcz6gBcK0xfE4upRAX-0ZQQ-LThBjGgYu6wN_l1xXew_ENvcjeS3oFBoX35FCnfJIcZ5JitbC6JAtDlmseT3v_aZHOs4AU-OQDVK5yxTGEbr0y4P8niusBiUR-wQy6GOhskdrMJdPbh7aJm53i_FZkvut0Z-WOgOYzQ5UPb6qyIb4F5qxnE5xx8Arh0pZ_61-6ykCIK8DJm4r87AKsnh2Z9HiGbAUECVTkkaxhvBBslc1M3lC69tBgl0UYJn1kPByTZui8d8mpgzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22267" target="_blank">📅 19:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22266">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvBIliyt59KferGhNgLFtCGlLJ9aiN1Tw7LnyUJy4jWngYRYXlWnw-rC8VwTQHlUVn_dDKggLUhJKwHRNhnOND1HZFvaFc5npsBXtioCWMY4WiownVLf5YyfxAvxqr1houzrn4zJkqcfxNK6NNYKPkFdSlQpYRCeWaIP5pbS5WTkXiwNDlK961DOJPGB7O8OJ4hBgb6FFD9kjtHq4lGs-SGDSk223iUw6aO3e26KxDO5xeb4T_QoxhwuBNwYDw4rRdbMclGJV5xzLdOagwJfc7rdw9XjBusMbOnUT6RNVpKEs6uzdA9G5ldv2ZJNzLirNBqrzagD08y1L2fKrBLCBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22266" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22265">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYWGOhcfVbNZpXWfSDDCqQywK9Ao7iGfE8MAZeNiqaf1FGq-VuJUMuHRJo201M0mVI9M06azLd7sO4STXWAYO-lZvaKG3DWwcJG51P6XriCmrRPkf1xcLRN0P-Y7J8Xrs-yxnFSMqQYaR8IppDRK1byQmAP2kAWdSAm1QPIOdlFUqjVHy1sxScumUWCXWUXvA70wZ6UrBWQWBf5c1BO5FCmK_YVkgPKTkdDALO7p0nYO2aHRIpCoFN5nFA5eQWoo1KX16zbmWilySUtqIozkzu-B66ljD9kKEvKszFoc-MxwQdb-7BMmS3r4xjZ5zQNx9-9bP8QbnAAU-Bdb7eLP1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسمی: پایان راه آلابا در مادرید؛ با اعلام رئال مادرید، داوید آلابا، پس‌از پنج فصل، مادرید را ترک خواهد کرد و در تابستان، بازیکن آزاد خواهد بود.
‼️
داوید آلابای ۳۳ ساله، ۱۳۱ بار برای رئال به میدان رفت، ۵ گل و ۹ پاس‌گل ثبت کرد و ۲ بار فاتح لالیگا، لیگ قهرمانان…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22265" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22263">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSHgUcEWBjv5Q1uO0M3FJWCnyD4-U7ychiVKu8fp2gekDPIhdVBj73DxSzG-f7gcjfjYWCg1m3BOrhVfm9CQ5Ei2NBx5Uhbpu-Y3uYdjT9RrY5OOu9JSNwJiFp0Os0yFhoNr3wfi2Sayd4SE8LC4ZMmdjTjs6wczMUCFHmGyr_VK2FTYsKvUlqvSS7xZUjy2Z5otqg8C8BIAcTEs5XUIGcDFkrz0Bj7_au8ByzEYHcj61I9yhYUB0i8Idd1xbJX8GvheCAvqaAR5LdXafE2u0X8Zb739iU4y_9Ma_0rSL3wvAPRWsEfivgRjzmKownWC_nGF0o7XberhrsWqzUFX4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22263" target="_blank">📅 19:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22262">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkFhDdt7N9DEPVB6_4cVRck8xUx8c5Mk_w0lWacJcwzQ_o2CPDA7JoQ7_F4U8lA8XVdSYZe0mmBvep6hnFvy6xZc22Css6AjiQEH-fspf2HQW-owdL9S_uJZWtHKZddLO9MY1zIiGyDTt4L4nETgfFK54wmpMQc0J6W_gRB3GglCe0tEY9doEHDQyURcxByMFPe6AJAhIf3WcZAc3BVG7lZ2BuaiE_zQbuWMIIkOTSDFFZ1EkzbT6BltMwHqHovE-inZooGcD-snE6tdlzJR2onHCwN89sWW5vsS6u55H-3dwgQAY6yMOT56v6nMSPEKdLSOR4kxnz3uMJbL7xpX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22262" target="_blank">📅 18:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22261">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ge-O1FN9u35iETTcJ65JhgvkshO-T6xK0xKSZmUspSB1KPajAPw4zy-_LZX5KxtM06WsUlDCHYHKAdFLN_E97_3JTrx4CTbL_4to-_tqmomFcVVPbvGeuHOMmi2ZZfaIEVunD1PodXBxmMFsukCcTuISSHmVipbh66Unr6QxyLVAYIWv8Rb6nPWGjPBL-VmVgzGqaNZd89kXI9t8ri8GYc2DajM_Qg83zkRONqQtozzL_bg4MCjAwkC7cCbuh97qYCFQNPTGnWpMkJ5XkbEHPjwXq4gp0kq2YpI4Rau_ZwAlY42hULT7Kkyjwp7GmlG1HdhtsmPx9L0TVEOob1KWAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22261" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22260">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJtftad2sPl1kjDlf2fUbVnWoZLH9p5OPRnxw3yOEbsoxWREtPQSxPtDhbQRbHa4j6Z8dRNjtpLQrQz3d_hni9qBHzLuIHdFocFq9Bjbw0kta1urp0wsXULAGNSuWSGTgz8hJ986vxexQsq_5fX0Z1h-bq_mfIC40pAMxhTyzlCox2syh4jSZsxEfjHS535iR-277-hXCle5P7JLWQWLALVPkn0Vw-mNkEi703sCzgWj7LW6EHyjlILZtBHTAG4IUpc_dgIwM81wkwF5hLIgQ5DcsRcpCTLw8-T7dKZFm8dYuraDz7bPqePZTXJEVeA66SwGVrwZUpd8rx69XqAdQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛
باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22260" target="_blank">📅 15:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22259">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiZ4rJY8hvv9dVrs4jPH9MIeB1yr_PSwVPV5l3r2rqqfer6G-tnFgbLdh7-rcMJyP9XYvPyykoXS4ppYeO9kfEd4N5AECjrh14M3l1Azt0c5R6YuZRVeN3lS9b_TABN_GDcins95gK5p5hopZnPMFZz9TcEPg3u6-1ZRyU8_GPeipK99Q3uMCbSJRzQeMHFVbpP4i6xlaamW931IqmdovAOzF0anZ2Tj30rUwMZLKKuNrqL3vgtMP06e59DFlUjgqsUFxNsd4cK1wQ69I7lSqe6wc6xW-rJYPIVdWzrzGWBTJ59_J5lMl4qpVBBf-J7yYq3mOHXrwRgQwnsa91KdTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22259" target="_blank">📅 15:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22258">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIuowQo0E7yKwMBABs8Ttz-5N3u4SwbJpacyAsSEBGJLn3nEifiMdar_IUlf7_3J2uxZSvjygNmZXQUOe5Uk1q_hzJWzKVIzCd3xtMpYODxZqUF_eK2sorpEgkaNpCDSkgNyWspv9JTVxkmS3bzp3a3xd3275n_-CsCQFeLmj0uN_r7GIjEE0JSAynIqTj9YHsS5c_jSLIyCASChZEnn9icgoTCPGXw1QItFP6DqH0cvngU6c8tIpmkaqfzy2AjkwZZVwh02iA-HSeiDnozeBHiIMxbV_U232fPt0V34w9IwnRp4Da8IPbjpzfoLvEpnnd5bQ3unX71yQs8cI-WeOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برونو فرناندز ستاره تیم منچستر یونایتد به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22258" target="_blank">📅 13:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22257">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEcvXovOPStvS4oZn47A9l7ECIjAAE9JpaR-cXaAdJDEQvZceyki-E6OoamJp4pQowNvRn05Ko1bj5XITwlfC4DG73GhvhtyKLJ_fM2FbaD6BTVeoWieiMudod5zdeVnV8RFncz817XViEehLJ6t59YdWBVwuHHG2KsoetNYKR750UdL_5iCQFLCX170Mx9oS281srAVNCYwBX2j_rTgCaWWyWeMzqnsYdf_p7F_wHK-mq8C6jEsxlEsoHotOeu55_AchWlMM2KCg05O5e_1GZgsln7vpfb7bi89h_cZJbElgpW5JPtEld0H5fuH0pPJHVd1jqtAKaBiL9HVTpiZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22257" target="_blank">📅 13:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22256">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-tBcV26H7HC1VImJ3N54_YUBMPUyzMATNf8If_UGSrx_PXoObxr6LUjhVQgTvYcAUkm0nJlNqKlo8xLuNO2-HtV23sPBA2VE6H75UC_EI0PPsj3Dd4cQPvdPq8HaHCl3UP7NXOWrqNQuTO4TS_ek0NyzM5WM9p5RB0pO6HT9YmxkVl_tVmQ4d9-47NRwJ8zzD1wlQ9Si_CxWOU0WutBAi2hjmcQRt3-5wkquAwh8S9Wa7kGujs8CogDG-erO6KFd7W-_b6WuTyN_Lx-i63jY7ZMgsNCMGxOxwQfKCPrszkufNi2nmC-lZ8Okl_ELeH_OhiMz6LxW41zDUFckJzylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسعودپزشکیان‌رئیس‌جمهور: اینترنت بخش جدا نشدنی زندگی مردم شده. دستور دادم با نظر رهبری و در جهت رفاه مردم ایران بین المللی وصل شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22256" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22255">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwHV0SrEvKPVba04IrnbZZ8jCH6SobdfN3kbCQDievmRdADhJwtzpNOxRIk0QGxG6eUC6X92nwFQUDDUzdmpLAkRsznAZNcIDg7IqqPWjzggMg5hvWHktefz2zWe0b1rEFie4o6z8Acfw3yEjnLkKj50mds6_pHnI2AWqDlZ5APmU3WX2fBidsbaHWk7__r8xQtLmr-BSput1DT74YNgccu1bFq-x-ht0fe0lvthGU7pdhCAhJToXGTSYx8D6kDW43SZeBC5_a3t4FRk46nrZsGcugBobdJtDIvEzbhlTIS1OX_I-5RTobaWNq0xffQt63YGuTr6nsryJ0lcsZ6pTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22255" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22253">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcflKlZ50HXdeZVQdVVo-giaQKOIxX4GLTU8ekBGO7421L4DtUzQsm_QWGw2qm0PBbOh9rw6zOF5D9gHS98ZnPDLOy14Rub6m7kZPnouDYTo32qNW-a_r0suy37ZKpOVh29FMRHewP5DS1pSdDuWdOy-nnBfAz_kSBdWbjx9LcOQE2rNVpYCwD0sruOK9CUguJ4qu_F9HJ_SxKV_DXPAMH9_4ZFcysN6A8-Lp7tHrmfb-6gjT8sGfb7N6MOkDWmz19HM3sq6PwclBqxDZupU7t0Z6A0FLl1d9alz4KAw9w09g0kkAkYDes-3Zl3mZBseT6TIZSgGsOx37SXKAUgtGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فکت؛ کریس‌رونالدو به‌اولین‌بازیکن تاریخ فوتبال تبدیل شد که در چهار لیگ مختلف قهرمان شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22253" target="_blank">📅 13:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22252">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQKFWfhsZktHVlbuCYbv9x1QRjaph5QhdW-Jr37qUbIQcXUVVoUv95zFjaZf83UsNt0YVN2YIQb6yNKy5qkPVizUXkQvAErDA4RG5dkALChiY_AvM2kJurRTaz4ER4aKHGClCxaAardFQ81Ocl4aqs4PG5nok4v7-fQEcG0ttl4Zlqxx5Fl5zRMoR0GU3J7Sug4Y8S12OyG1pc6Hgn83MqAuFvmuJcMsIvdwIgr76nSgjPicBNj3WSIVNk-0OSSzLYNLES9tMewUzb7bM2bXW82VY2Tyv0iTGN59h39h5ZdFbHdPkK1kLu1ueGasFCCBjfi84rOBoWPjxzzO8TbNrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب فوق ستاره‌های توماس توخل برای جام جهانی به تیم‌ملی‌انگلیس دعوت نکرد؛ توخل در مقدماتی جام‌جهانی‌نتایج خیریه‌کننده ای با سه شیر ها گرفته بود اما درصورت عدم نتیجه گیری در جام جهانی قطعا مقصر اصلی این اتفاق خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22252" target="_blank">📅 00:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22251">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY8D4tkPab7ou3lhozmdwmgWb1R_XIv6OZlvqcWahKw_WT4HGBdB9Nq0eUZPBWcy-l-oqr1aDp_m_y2XPw9exApfI6sKy7K3D9-26qq3gg94IJeE0WQf0jwbWTF7W7VcUYlnlU_1hLRdj6bc4m_0P8UsJQBzBUEiOr9KCqH0F2RX0pafb1SEmbVwNwlGqw5Sxx0LS2YXusOCB2qFddiuvR61LEOQwQ2umnqo_LV0tOZRPv2A8IRa1FUqXDWOo9Yv5Y4bQxfQO-jKtOCuGkuJxiGjNgXJCS4x3mJAnooZx3tzgqrlV_xwoWQlsJKY25p9RI6r47BKC3o3PULX6SMvzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22251" target="_blank">📅 00:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22250">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecqNF3WzMl86w2bHhsCuw36aSqj6oEoHreI10zHHwJbZgA7NyD1SouEiwlbPVeQzsjMnzVYV_aYOboPIGNXQWIAz7s9gsTQaROLV4HXfDDD2gALIIYmWiypco3oGPpWL90b970t9BK96orFcyqLfHwAIj3BcY49rzDeBC1fUVZpzOe6X3WLEvzBJkjN1tG0RYKw_iPOlgvBBnsOw24eTCDKF9gFoGtyo72LTV5Q0tikAaBzJQhvNgkpyyaZLbJ_YGoQqSKvqy9N3lHoJuSmnFU0HPRK2BLLaQCMwt92Q2tSDCGNmB_vZt8i4O_FCely_5tWlXXU3fjhdwyGLk_S1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22250" target="_blank">📅 21:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22249">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdX_AEs7xbh0YSHIdrfL8_B53D2r5PfYXHbnO8a5b4L4trN9A74e4D_jBJ7yFpGnjnsMIs7SBZ8KWLVAIMuU5tRztFpvIlEaqNHo1m-w5RVD8laLPGZ-T3pPXZ8lEmD04K8gY7E09YulemtN05OOV-cbwXX-X-PwuZwcVezPlpcA3-8OvAjW9hRoiCACcGkNARWdZ2tLViQt0h58LyD6gRMuVSlNnmgdYv6aBL0Hfnk6rNcYgkeW4cgTbgGzHgzQcYZxLCQ1Gfdkprh7m5Yt-vaay63ARJLtNUa_TzCh9FQemK1ziPnmLAi0-eF8RLuMULePvndlfN_f5qqdJPCLNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه اتلتیک: باشگاه رئال مادرید به داوید آلابا اعلام کرده که درپایان‌فصل‌قراردادش تمدید نمیشود و رسما در لیست مازاد کهکشانی ها قرار میگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22249" target="_blank">📅 21:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22248">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_dxufqR-Lw8SDpjXBdak0swoZWm30LXF8TXIFYcisKOlYVf3AoWq_cxg07sMiAalG9Q82AMJrvmSuXTr207D1YTfRRW0dGbJArFG1COkiHmZpH00u4G01OnWmyJMJba5cRAQFOQJtttMq2gFEfVY0TVFUomMiF6nr1IKALrwxgg902Am10PrU49OR7N4MAw2SqR6DpTDxpUQ-OOyMm2jjFCfTFbXo1ADxfXUZj4OWuctHhAVMoc0mg5jzb5h4SDAC2TU52WFyEmTIWbZEEzjVfQrID7upzYwzH8XBr0QlUgPEc0SEq2EIToXXQWUD5wNAP8CeSCQ-FzKkVtHnyR8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22248" target="_blank">📅 20:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22247">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cxkeog8fCkn5wi3_QiNAK804ovcKxUw7eUfqpuHioIs32yxOCgENx_a7ID0ZYh5LhKbyZcRkUAEzMzczm1a1WJiiCo6F4DFLdz8qR_eExcnw9i0rqjOH9mERghNd9pK8QerOejrPVt-rJUfxwsEH1Iyc1qxxTSaGLVX7-JX-4ZdfKWEeQoY-Xqo6pEL_xBLSsS7pDV7iEQE_PghU8Vjl-d67bpjnkvlUkMI4uP2iRXCOIPVhqhKlEQsjjRJtV40BCsjF_AGCZy3Qua2dvCLgVzSUQtTHtpV710gTxN9vnzwbZYP9nwgM92d2dk8hyy5ve1eC0yuAshR7OOMEzpUYwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22247" target="_blank">📅 20:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22246">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEdQQca1GaMouGmYL7G89q2vRC5NgFv-QMYhVvchEB9zSonbKoqZRNX7AJzd1M26beVHBmOd_rPVS9hlJD_vZVZjKyGUF3iOXUKR5k_zaU1FWkMd12pgUCNzzN9fzaAET4RzqwxF8H96y2wXHEqXwMNq694LcVudglU55QgcgJ1baIk1azz65yXxWM2mCLUHM4WrdEbWjANu-y0XJfJwOtZmAtyS92Gn8Iy73L60SRoZ-a9v_nnAQ-ckoBCxUeUvzkG_CCdTDmk3bKT1cxdmDmiNloMZRbryCNZxhkNxq1lnBVBDh58o-sbANlgmwXr4ghbpM7uDHSajICSZ7AMSBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ایوان سانچز وینگر اسپانیایی سپاهان بعد از دیدار آسیایی این‌تیم به‌احتمال‌فراوان از جمع طلایی پوشان زاینده رود جداخواهدشد. سانچز از شرایطش در ایران بعد از کشتار مردم بی گناه راضی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22246" target="_blank">📅 17:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22245">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=QrS9VIz1b1mbDzxj5DFf-bh-eK4KXeSZRwj5yDNPMNVq5SvG7zQn4DW1R2DEId38XgPb2W8VuJ6w38LYqY85X9BGK9jw6MEkprG8yw1AJOYEJRlOHt0Il82HFmhF8w8YGuKN_YZezbZSG53q-hSJSkihSYZ2gm95af-mmbl-sFyIRaPeGxRi4e8EUwLu6Lz_KBwUOfUiZl8m4bkEFcF6H1CgJ_1844k6B5oAAAAwKV2RHevG4p2vQP_IJUQ2t3KYNj-vCFHFlRVPv07OVuMErKI3-hKWb7bDOwZ7ipmwkvJL6UdmCSXjgkXmYuD3bS9M7HpQWrAtfnbQhGuffaQdCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=QrS9VIz1b1mbDzxj5DFf-bh-eK4KXeSZRwj5yDNPMNVq5SvG7zQn4DW1R2DEId38XgPb2W8VuJ6w38LYqY85X9BGK9jw6MEkprG8yw1AJOYEJRlOHt0Il82HFmhF8w8YGuKN_YZezbZSG53q-hSJSkihSYZ2gm95af-mmbl-sFyIRaPeGxRi4e8EUwLu6Lz_KBwUOfUiZl8m4bkEFcF6H1CgJ_1844k6B5oAAAAwKV2RHevG4p2vQP_IJUQ2t3KYNj-vCFHFlRVPv07OVuMErKI3-hKWb7bDOwZ7ipmwkvJL6UdmCSXjgkXmYuD3bS9M7HpQWrAtfnbQhGuffaQdCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش‌بینی‌جذاب و جالب از فینال لیگ قهرمانان اروپا امسال؛سال‌رویایی و تاریخی آرسنال تکمیل میشود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22245" target="_blank">📅 16:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22244">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQ3ur95r4RuZ86bXbycOJhR99atu_Vhr_WniRo7h4aayf51nE_cct6knb51MFCqJYbKWQMqdq3SkRjpvD1-6HBPN4Keu9wwYmMjJNOIwh-1TQPDXTscg3ftoh_6D5IMazr8YvOs6WmEeRRJ7qDAVYbFF9xSxwRm4jTEevg89QqR1WTYXBgOUG_I4PxOyRIQjLE0Kg5qW9B4gr7qqyDwv7AZ0bd-RB9mJgDI3rhZFbXXOu5e2-33Rms26vqy5eHXer-l8pWYN29HhHqnzXqSdLfAIzs7Z2BOdYxAofY12oKcunppbFwoyUq1WFrye542d022hz9KqdMlFqEzc2CT-uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شانس قهرمانی تمام تیم‌های ملی در رقابت های جام‌جهانی2026همه‌تیم‌هاباصدر؛
اسپانیا در صدر.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22244" target="_blank">📅 15:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22243">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRxxRjSWn5njx5MYP2XL4xOXVK6e6PlSyD6RlGG8lAiDYXfQBl3o_NGNljmClw8V9ryHd1zMjtEKDw5cz2tgV5jKSltvdzECYiCTZ4pPxKqYea_Vvlj741Vku9sCqJ_gCwEAWc-NIaPn-34y8X4paa-hnDVDP1j2uGRrviwB59MGhS-HMvYTQmmCGmjXhmGjGe2QqLo7yziHS5OeiY0KGvlf3QOaG3t5O3MD4vbEBl3HSqZ47edqNsRegMJ9hsrCQyvT9p1BVYuZJk2Z8rTomRS8i6_jqhIUpODkcXA1nPNlQfoNby8b2Zkd99r5c9jYbWw03Y2vxNkDA5XgKw5wsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22243" target="_blank">📅 15:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22242">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHy2_85-6IaEerJJMqhlRoM_DL3OsCUUd_R9wwCtE4-nrpVYpGNEx8R5RRAqH5Ne4xCVPHY0JXX86vTGsBPDf3eaPo9iCeRkS25tB63edVn_8ySUxXi7VTdlr1VsRJKSFRwI4sBnzQ37mBG4fbZCgIYSgFqGPg2btOt7MmSkNvRHM7ocsZ5ik08af1rL90b_QCq3M_bAldWtdAxiZaJF59ElE_y9mTEogIvH-mAgk3Kh0n4_H2Y9_2eITH6rNVMkdnau7vS9DGmTxybp5fW69HVhdmOjB2ARPIU5BAqBC_PQkZZ2R72UTzR03W7r3uVpMY8Y9q4pRSgb51owJ4Do5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22242" target="_blank">📅 14:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22241">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqyw2PGs4B1qw18xWfGov0PYuEopQQi1gngMzf8qL7YFDTtcsdGToc4LWm4CJVbETD9cWCp0Y99R4mvyu-VXOfgZFYlFMAEjY00vBacnDNAWNDeMR6zODF97OFkBL0j3l4IB2PhU-2oGrWqsINS_AYEBcH-SjoEmzDw9fuvT2zMtZr4csYQwpF8at32fvLHAj7mQHt-UQzPBJbbSzBxnSFVyB5rIqtnI_WQzYbVmhIZTHGivKjHxBBEs8QJwScYD-bvWEVHHqHUIiXc4Q3IlKA2pIkmJwrUbohIA-7XDAPeWTucfzbMCSdthDjJFpFiZhUIgaVQehwJWHc3KLN1nNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22241" target="_blank">📅 14:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22240">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNdw63916AellsesdF2Aw3LvEckl3oODzQ4Hv1pYv2cNXqqB3xDl-_W6XZ3rGQKCy_C8_YW9-pEZR24R_Li6hZrlp8juRBSpc-VnnaRsCWhTZIk1tY2xJ8jToAx6NWrh9j-MX5I2Eg7JEb1w3Eodgpnsn8yLe9YFRXHGCNs9ue8f2jP99sgZhy8Men1TtJpAbiFpIhJyCbmjeWgpz42mVEht1Vjpsd5f-KcoSkXXi4ltclsRWkaZZcc6VBsl7Tir_ue2ZaE8vlwQjGtpUv-EIdGG3kjysvxYze5WjECqIJgOhXNdrZGCporSDtmQHxRlQ3v7adeA-4kEzZkyIwdwsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی تا سال 2028 رسما به عنوان سرمربی دائم منچستریونایتد منصوب شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22240" target="_blank">📅 14:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22239">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXhHHqtsidUGDDJh_MB2OrZ66nD7M5ZXoySBfQtS_w0K6uxQB7x7XZ-N2rljImG4x5mAXL45jEHraGdKBEWbkR1ziU48LNxkzpyPtjxNozjzk8Ay5faMxOPdrbSbUlEaHgC_iRtf4PD-mV-dUFTHRFC6LZ56Tsx3Wtz4bQpUwaXMI4JDegWuSZjdHKB_7qQvb_3utY4ibWmarhxXWDQCLecjmzEvSfrktRcpceV3OVS5UQ6fOrLem75wL5L2yF0rt21Ir3MBy3PJPYvV0_Cyi5dpiJ5RLVkl7K3UCm_ps6_A_RCFy87JNPWjJoVKKag8HLs0TBAgIZ0QeBHlQk_zhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22239" target="_blank">📅 14:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22238">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkVqOPMT-zzAOpx7rvQd-t-PeUY4KHXoVXFKbGN_HuhGoAL2Ao0LjEkujTYEHDjxSAWHA-gUcFIasGMg8vwGD1lHLnbuKID9kK4ny3b9GK8Vx1BxyBSidJ4KdZTfqeD8EqP-IkrrqIjWmhqZZpYYf8eA1hketaEYk-ZMD7EstpEgAeHkdRquiXWH53pDen5AJLlIuAYaOjIlYXSVbsNAKG8ubFyT_wQh85LVC2T1OsGU2tc8bOCqA-zEJMzvp_jopBm2xY1lCKCg0ORleLyOhL2d82ZKHr7xXEdvEwL8jBfeEoe2TxA6iNVYTrBRo6bTp3F1L3g1rScyDNp4vgbweQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22238" target="_blank">📅 12:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22237">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1ExSEdO5ec9vFF3DSIE6XheZrnL3EvSR0RS_Ii5pkLgH_OadbTOKppJoWHKGKwUppXnMAZiQTh8nG3WWiqfTYcriSFrrTfWOenl9gCKA2TxCbdcvQR1lhs52NGlXjNYOfIgTL5N9OeeQZRUNSY-3oTjTWBiG_qcP-LProLvKyIEFlegrMTY8F_lXy6TtxBqXnzOP6jLdqm5xd_N8cUYee6zktLcDsGQ-Wxe1HHF6iWw8yrqcQQZbSgBUCraK6nXyw_eGkp5ARxyKrUTgNBqBp-uow3qC-VGG2b7ufr9r27yipjMXr7BMcjcC8UZLoq_tOdWILBvLg8FLFDYA905jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22237" target="_blank">📅 11:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22236">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDHOM4o_YXWWveHDJe-J8ucQZP6VXP_d4_dCMOfCQKiamUbWM6_5snoRyGP5ln_SUgf0EIw4Qa02XFvNC8nyLH5V_Sbv4TEEPev2fEul0cxJAiu3YOHQVNX7lbC8wq9_ZgWCGc3Y-eenHD2D7738ued4Kpsx0Zb_dz5rpEZQUgooS1s0kjywRSQvmMRKYBMPpeydfMzikepos-P90jaeOmj60y_a4IzsGa7sU7N_unVheqdLjRcYFj_0Cd77INsCClh5Lhsq95FVlWCxx93-CkyMuI5lKn8TbIreMkGfcSxS_NL6Zu6sqLxGkOlMfo623ITyr95nWb5MTkZkT7kVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22236" target="_blank">📅 10:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22235">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asr9JBxlNaI5a3A5CZkyF8xIOysDrXGBRL6vo9xERjuahIWZzeK4v2lQarapWVU4zHR0EEgkZx3m0NNaE2EPjSPqumVvMWRc-vE9s6TvZiZ-YQd4QdlvRZ85Yiny8-9lLnucLXD-uxsM931kmt50jgv4HMcZAVWoj_G-bCOOcHPxTW_XaYTZpBmYbmztR-qTNX9e3Yl2BTgT3o3BXJVQE03OiCdx1gnM_7zK_4TV0ef_Wm2vQa79210XsgXt5tDjWDu54omhYVI9MLJESsQd_-EKyrUkPGx0YywDvDurgHsBEPD_Mtqz1bytTrqaJcscvB0BOO7zfoz9yF-Z9Hm7ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22235" target="_blank">📅 10:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22233">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4IoHNz9H8OnhT3mTOFvqV-38IGOYCyRghe_haa8L0zELM1bHB0i9IL46EnsCtUopA6FpjuEeMo_D7hbGHCbacYMTIYt9-F9wh-zS49G_76pWLXYSfHmX12878NiXZdlz7XIsapfvQrotgXoF2vycZWK9xb55PCAGFQRcVuf3gE4mfa27HkYClnfncoe8DIMRH_5aiIB7IhIVp10i3k28Hfsy9DCn61CBrjV5wIdgKAzJaOiVSpkf-D-ydcREgh6fxPbWwlpwLJYrdmnrm5gPFu1JxDeYFWWNljNMrLQ2fHMsQgySDlpwtVDDd1vrBxyuh7Q34IWZxh9TNIJFmknhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MUKcgPRCILbNFX85RPzlpXhB7Cvmp0oF1nt60Bl_HNHmpSlZuUSWGVOqJsmo-KtiBU8TnevhhldlAVRnOEk5IA4Y2A36Hxnrea89OPpc92fUYhmZeuazkeZSkkgHjkve3Lx1nqh_omIBSviNr8E7CloEUbsrbhVDzhj-zWX0xWx7bf3csvsC71Ie_vTqKAtWn9DGc5zfv8kOVzt0R4KOBAULkpl5Sq0_6bVeNl4Q4BAz0MXd18_lC4y4C30jsU3l-p_DLCLzjWGjTsUhw_OiDvmOodfwdYqCoHEWleO5QtjkZfoMWzeNlDL5gYj6LY3hZ2EmP8L5G54z-v72NJVGaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22233" target="_blank">📅 00:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22232">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22232" target="_blank">📅 00:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22230">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n7jYThcybv9LZRK_EdLOGF9cKgAG4PziQ4kMRBhsMUpGTFxsMCuqyEWYaCq9beYMlnv0tyNKx9FIss2XssgfA8F31-nHILN1vDG5zMyJCtaNihjBJkExkDLVNPkZ0n72AsD-i2fM293EHIodRwQhkEkLn0LOebhnnkTDKaQAByXIskFSSQ9CM6X_iAiTClodfjyfNu--xlgWF5vGxnDohOe6kR85FqEuMiKrlpP3JhZuUNOb4hhKsnPywS3WCxWLysTcuJv1SqIJw5nzDBWOOLlMjrWqHr_-mNlLkjZW_DK0cRMbnN1I9mkuipotBCVLVvROMipcWn9Us5FdnyEFxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vG08D3c1pi4dWs7qzgXIm_ByhnQQsMYE00YfA-xXojj5OIszcyqsGeT3UEqDnLBKTReFisxt5w7UjpTyuXgZDUi-WcE-BlW5SmRso38n27ePns3Z3HCpMFPrvSnmmAPQAtbgUAOlS2T_ynb1WOcnLzBexIolUJ3gPokB2CPi3YATUrniIdNPFqRVlPcl_G4v7gu4wVjSyYkgllGiv9QCuPoF6prhWrQdbMF9TD58fnkIo9aWmjO0ptZsg2WU-6O9DcUyE_LaMs1uVzcQ7ao3S2eqB1JFNyR5UVWHXz3YKlrHPXa5saT-2Dsy3zFcwGg8qKSan1Wmp-hVMS8QcKcxBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
هواداران پرسپولیس امشب پیش از دیدار با ملوان انزلی به این شکل ازدواج امیررضا رفیعی دروازه بان جوان این تیم رو تبریک گفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22230" target="_blank">📅 00:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22229">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHwBa5l3_UqbJ2bHxxQVNJWZZvFDGGfRh2n064hfU2wusq5u1AWNk99-UIcjvMnCXLjJGnGkdkG0HfhBy4FQMNmqudqlV5CONOw91gmXdGZO2UYVoQ7PlfgqAI63OQgZyLUYtN7yOMyz9xpPCa1hz1aDx4SFB_ucUqKlMfxbemmXapk71Bljy5LWfRLZEeZBPa5io2v4CHBocLmsbbdEeuRsTLgbaSVfP6YQWF_rn1B18ZtjiGCxMyXuWtW_zMDHpIR-vh_mvs_5cTz0hLDU8sxZmIO5qLcjowUeSD71aKirySEKyEshJURCXYsIO3YeY2Rr2edbHf2GrKeJJG_NCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22229" target="_blank">📅 00:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22228">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdSV-ufCVx9aO6MzH1KwB8iBIK9KJmHOKe0Uau6IxV6gwEa6xKN_cXjza1x8hUkt1yPiuJ9_7SnSBFfpKgYadH5IFiA7Pj2epDCI0fCLQP-lXY4nFQDyqtjuWEX8lCnNQ4Ztowwjdsb4gOa6LBMC6kTaEvoD_lLdKrWdJGxdhcOXFZqUVVyBCFrSuI0eKU7rzgwV-09kXPLQqBIez9RmeNjDH5nkHxJuINXcyM6nYV3HNd9jP7ao8tmXnRlWWBFJygBUlNWy9OSu9l7PPSlytKE_r3uWt_pq68anA3EhnemWQpyniEfte2U4tTrBvMiKId53TMxpzTJ8b9Yy3tBPqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
والتر ماتزاری سرمربی سابق اینتر و ناپولی که در دو بازه زمانی تا آستانه عقد قرارداد با دو باشگاه ایرانی پرسپولیس و استقلال پیش با عقدقراردادی دوساله رسما به باشگاه یونانی تسالونیکی پیوست‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22228" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22226">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRbh_2waNbXhihuRPR-Bn3FBCWKTrejPa2YkRZLPwDPV6DaSk3QLb4JYcbZp8GAHPv9_AHPLPXaL7e2Aks1FufzAUThS90_ZoFsIBJwXOZ5vMXUK3qLRR6QIMKS9XXpV0K0Q31Dp6K-HpTR9yyG7Y56dAry4EDLkorcN_df_Ci11dc4td1LbHg_sLHlhniaYkmQKYPsapvgcQ9IRtq4-b7MrHLIPb9mcjn6iBKoXjczr4sSwjpZT7ebgz9qhT3kG8s6h-8WL5Ok0FA910xuJ32buYzqDBL2Iw6vY22nM8w3j7seYE9QBohSs3LXxHRE0ABakRdjSo9uURawpT_DpGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ النصر عربستان بعد از هفت سال با کریس رونالدو قهرمان رقابت‌ های لیگ برتر عربستان شد. قهرمانی که با درخشش کریس رونالدو رقم خورد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22226" target="_blank">📅 23:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22225">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkeaewXs-bl-7t0aRZuke5KiEQqDhMnEPK2DgylL6UbNJXaynICrION2N1Pr-ZCJGj5Fqkxfn69RAj0g0rDAWGvNKYnKQXc2mI5QXBhDL8mC2Cl0KLpV_PH650_tC-sY32nIKefGlW3b-ccBVWsjoURjEf8crXpjhwTqZ-BlUQTih5BKls8brbFJ6CjewTBpJH_AsPhNCUA3H86hJVhyE-LJPP7ay9ppzdh69C_nxgioPIK8on5dSdMDZlyTsuR6cvL0ttIcufTbAZF5dosZ-uwzph-Ys_DxOPsMrCmko6Sr1WqsLCt57bYaHzqmIxjE2EUVDfHhTRrZ_YA9u30LUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خط و نشان CR7 برای رقبا برای جام جهانی؛ دبل دیدنی کریس رونالدو 41 ساله در بازی قهرمانی ارزشمند النصر در لیگ عربستان؛ این 973 امین گل تاریخ دوران حرفه‌ای فوق ستاره پرتغالی بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22225" target="_blank">📅 23:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22224">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d569523e34.mp4?token=rPHD1TtUs9CorPWvz1R-4sdqBd-vR-xuOFG78LsNs2jGuckwjZM60xWTI9EQiVJ1CMhe1ZG2YUwPRr4uDEFs9luvX12pzvYdaY1Ja7LzmiUN_eqdyjPQ_NPGlJJgKmLnQ2ytcwbAzuBK0ixQSoq0FFEeBb0q2O8qUiAS9A7svA8Hy3D8bi4D4GdZCss8odrf41ukMU48QGxjNIQSz61J5U7SHzc9DPAXYXLWXgfsbUaq7XOek82tUhZ37-BjWi3xNq3tA1YL6LgQYYWkb6IHR-9-XczfyVJrRp3AXrm0pErhajAWhWUz9beJj452Wi5BUP-QiPJ7xbG24a6pzMvILQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d569523e34.mp4?token=rPHD1TtUs9CorPWvz1R-4sdqBd-vR-xuOFG78LsNs2jGuckwjZM60xWTI9EQiVJ1CMhe1ZG2YUwPRr4uDEFs9luvX12pzvYdaY1Ja7LzmiUN_eqdyjPQ_NPGlJJgKmLnQ2ytcwbAzuBK0ixQSoq0FFEeBb0q2O8qUiAS9A7svA8Hy3D8bi4D4GdZCss8odrf41ukMU48QGxjNIQSz61J5U7SHzc9DPAXYXLWXgfsbUaq7XOek82tUhZ37-BjWi3xNq3tA1YL6LgQYYWkb6IHR-9-XczfyVJrRp3AXrm0pErhajAWhWUz9beJj452Wi5BUP-QiPJ7xbG24a6pzMvILQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22224" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22223">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=DwLSeHmhb53cPbicGsSwnXCGlBG7FtbkuvXSXHrv_hMJZgIzaMSgzh_BBWFp6wJ0nOHyDOR2asNFgjQIQEd4vsIUkmNYgodj2zAKxwVG0cp-IFsOA2OdiIcnFmWoStR4Btj5XanpIeTIu-0_7coUWGjiGPFD2A_IRek8TU7H1EBkJtLkRIM9YZiwGUxxSeHqk3W4bzOvb0tEHshQfgFK5Lm5hugaNZ4BSwIxQGdkLsQ04ta0HaicrOUjd_nmHTkneLDxFUYehA2CLaH3zFeIKyf1AzhLDVVU0NBnzDOjqYYihIG-CEyLH18zyRasjTGDF3DLFBs1FBoXLMIPkMPfpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=DwLSeHmhb53cPbicGsSwnXCGlBG7FtbkuvXSXHrv_hMJZgIzaMSgzh_BBWFp6wJ0nOHyDOR2asNFgjQIQEd4vsIUkmNYgodj2zAKxwVG0cp-IFsOA2OdiIcnFmWoStR4Btj5XanpIeTIu-0_7coUWGjiGPFD2A_IRek8TU7H1EBkJtLkRIM9YZiwGUxxSeHqk3W4bzOvb0tEHshQfgFK5Lm5hugaNZ4BSwIxQGdkLsQ04ta0HaicrOUjd_nmHTkneLDxFUYehA2CLaH3zFeIKyf1AzhLDVVU0NBnzDOjqYYihIG-CEyLH18zyRasjTGDF3DLFBs1FBoXLMIPkMPfpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درصورت پیروزی النصر در بازی امشب مقابل ضمک؛ این تیم با کریس رونالدو قهرمان لیگ خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22223" target="_blank">📅 23:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22222">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5GFt4rgpyP1oR9GMJPaAnFKZeaioRQ6zGJbv94RpzyiE8kwqCLqUgSOsqbqKpbiBAdi3h3WDebC8ZAeLlp3moiY2L0cvV6E_JsT0LhIPzoTELDsws7x0XdPQSdIVE4gwlYFzaqKATaDshQfOEFaXttAOnHSq7WTyVo3L-SpsV-xXXpRZ4nMJqXf9R3lRpmblmgLK-AibH0N8GpdrQwNCvzlxXbkGrClv49MpGx5uaCtiTzwg8jS3ahKeVoayNXSwmzxDHLqIdSk1q9oVZ0cfOjZPTHVAh8Vuf4CZZrGHAA-OGNxK56RICKdmaSk2gtbdAPPq4b223OH_rcUjcuISA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22222" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22220">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rdhi_YG60M95z3z2K-nv9U8u3n8t8ckmcmgdBGkQKDljad4hI1jBHG0SIqEnxxlH5nVtuISVhrW2aaX3hueQHegmR7j3oZrl2dRB-kZAQV6Ue815uc2VBYbl1RLW7HkycobQTUZiAjHCPfwoQ42ukmPtOmbeQsx_bOV3sZBdVorPDsTO0Bv4znA-lj_gnBs3uX38KFIudpYSmbWvI8EXM-YVXF_T3KMddSstYNKXHaa2pG2krd0lNjYjgFcX7UzGOtRX5oDn99eRzSNLjbhCQp9qIoXYk1dYpq99hPENpuJoPywVHBw-96cDjnBbvJ2s-0GgnECEM0wdEJhnnCvq-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام فدراسیون فوتبال؛ باشگاه استقلال مجوز حرفه‌ای خود را از AFC گرفت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22220" target="_blank">📅 19:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plW2AiIxXGgdbZbIemA6AtTcu3DjOu8pcmrGOqwwvb3QLNtIBy61E8nD3Ou9ttKxiLzU2yh96cR-GNC08otbM5xH7Ffe6kgeTjhQ6s9Bb1pjV8gUB3hKM1ZKDLihrapQUiIlEsC6FK9lchtSK5P5KJXiwNUvOFECY5slWFatIMpEdC2BLOfRh8sYBaDtMMxCTKXrKIUtCqVgsySz6d__uOHfSmqsry1wIJ8IKYbCwE-2i37C9HssKonygZ656wMGDQqyfCCj7UcbDE-VM4V1TQzYKf2l7sBdtxADlY0WvMAma9YD_zc2rD1U-MzqS05SPklNygDTNZ09WfS9ZoAkxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتاییدیه رسمی کنفدراسیون‌فوتبال آسیا؛ مجوز حرفه ای باشگاه استقلال برای حضور در فصل اینده رقابت‌های لیگ نخبگان آسیا 2027 رسما صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22219" target="_blank">📅 16:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFIuzCzLd6f36cJrmdnJTwI1hsnwQBaSWBcl94IJhazeG-FWud40-yJBToA6D5tG96JmMCLuZiGvXPzQqOCPF7Tg-Sak3WC54WQL5cbmSIFl_nh1ndJ2NNorB38rMp4_4BU2g-rb8MTxsM41PjR3idM4VTxI4d_Rol-iZxr4vjag29Ab0Io25UuDthZ0IIXjuzx2EUe9moqmg41NgABnE54n-BhvafBrFQaZzd7pRdJS3YxHksE3fl2E22x3v__Psic2ZSeHTV-KlN2AbPtWwCJ7e9sD43ApSzaj7ORJJGeUL2BbENEuqmwtT3SK0ESrjN2PGSHmmItKC2u-LGZEqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22218" target="_blank">📅 15:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDSxyXSY72SmxwqoRGuaqtKceB6toJ1-atg9BObGy_1EVfHnDQM0FP3bdtgXYYvlMVnZHG1YMzkWe9kms3-j7_Zmr_y_-E0COO1oIeL2QqowehW4mqY5G60szkcUwghUvzTKo-g6KPBzbd8595obZ3eUdxLZbZmYPHJG1D-9QRENeyuntw6XN7QGjfDeppHTlFHuTJAraOWAiqew9Qi66AtBh6NIMrNvDhPiaG5wYgX8AL6hquVcGQYrkkVX0gQyJAkB5eIWooOalHM6Me6CL9EC7bNegX4f-vHiE-Ypfb7aZXmEO5LMRLUwVivUHQddcvOZS3_bGRY2P0qeDEVdLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان 22 دوره اخیر رقابت های جام جهانی به مناسبت چند هفته تا شروع جام جهانی 2026  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22217" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5qQsyNwGc-cuj5QIk4yvZ9PhEOrZ-Iv6seYk8HzSS39blq_LwYjO22Y2mQ5uc8LpdafxxALBQNtmEOK2t1YeO-3-0lb8C9ifMWlYEkbkLVOnatvhPPqi6UQ883YbM6-Dp6b4mKhEFnUqwTg6s1lZCk_EPplBBQCZNz_5AA0CFHqutqDlM0FbaQ7gfCwFvC4YJjeEUE85Ae90qI6dUk2Tf-gbFSlEePuNhKNzMTbutTB0AexwQfHvTRkjG2aK2FWckLGH5QJtbNDM5HRO-wnyxhYCUdtv0vYWbDLgcSxhVlJwAr7RQhIHJYhaqKnh3qxSOFCN4nCfZpFYWlXWhvBtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیشترین حضور درادوار جام‌های‌جهانی؛ تیم ملی برزیل با 23 بار حضور در جام جهانی رکورد داره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22216" target="_blank">📅 13:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22214">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/um4SgtEUcrafMfxQVC1eieLcKSmvDyS-7M-SI4LzaHtrPMrtRL3GX1D9PBdIBemSqCFF9SjkXaoSkWtcUw2_fiTQnC5ZBx1MmA9CZSdL6w4dFQ-jR9OyFfgjrPtyKVf-Tpo2UwqP44O2gV5hb137CbxfHg0zzJVQZ-9hLJVLNuscQkEj6L1fsq6KmBM3IQHndzPX3nnEoJ1RxU_MI662sosXDk_50ILYjOg9ZYxMQZLBhWiwi0DJwiBZo8e7wCc2Il8B7UNaxlsb-MsDEuNLO2FR4UEPXr5bB0W5Hyp3ImBKCBgi7AL9FkXTMWMe5JRVXazcOPhEDGmZjQfvz4g3Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XFDmmc0zI_qUDMDib0MIudQ_3uGaDEdIOeQwzRSAQErkB2bJniQcsytKWxsC1scIgaA2YPWOrxl2oOrKC_fqTnS26p3HzxzPS2_Wa7vk8bB1x-WjYrURr-CfWwOp2OKG2Ep4MWQq0Gb3A_tkavf44NJWgs1xQtkxoGb35tErtCR5Tr638Fns0XMloVUizwulS4NIJSj9aIT7qAKnHnPVRfyiVpUXbQPuA9fRopG0DCAz_X67eRJLz_wJYWZPfAuii-o1sQ37GRf7Nc3P3g9fNCcALSCnE1F91JOo8mGo4Tyd4FxQ5GIJ92ByFsnL4e2NOAdWcSPCMdsqgpSYw_-DoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇧🇷
همسر مارتینلی ستاره‌برزیلی‌آرسنال: رویایم قهرمانی آرسنال در UCL امسال با گل مارتینلی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22214" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJdjvigxDHDIPdUlhwRiv8qBN4sq8j-H1tnwnbLgcsuVKpKmhn_qbACdVt1ILsDaHI1Wl9y6voZYUuP-h0sSs3tW1pyLuRKZoYdB55SPxIQUJ2698AR-l-KtmGMHGDVmjeFnNEi5GUae5LNFWTRrpq7YrTb-twTetKkgUqLl7zlcR_kNwMeyrgaWbCqlkNUedxh3frfq1fVRLpECJX-gun0eUUaelkDbDdYU_HwMWANyyk6cPL7W0QfpamvbWGAsOAb4D574hY-mLJSlHyJ7t6UxsyWSzGB0PO_2tP1t1NnVY6I8iDLD3bXG1MQpUeSF8IxsW5G7vpftN6SN4QWdDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22213" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2UAmCv7nhWlcqCW6YL-RagdrfJtPno0xyBlCGFS-WEgWz4039IEdO4csb5tguyw_F0hDBSSfdFBa5t0ZbGijOr1jGwvSoG9rtVWyfPzY194rWqJnKDlGljxtZ4g3lGHmcFMUOsLKDXa3OmyDMeyT3SwjDhylG45LOBA6O-gSywzqN4xpDs-wHmLY3kI4ExxhEri_4V1DCb10W8UtVazvpwz9aQ0gBmEsepjhp-IXRRVUScfm9JeCBqfVVJ4tOxW62Y4Zq2cTzUce8PBB-NezwXc-2TpsUJHmIeJ0ddAsvcsk2J5qRnaYUf9wz9-kQ40FJBzRfmj9YLO26gbCCewAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛
روسیه با اختلاف در صدر، ایران در رتبه هفدهم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22211" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ix_jVusNgT3tLvEARXN0sBEA2sS1JsMXeRuioKgExCI8BMn9xIcgMfDoqHhqwpJ1DJA9bDnSMUEgR2wPewGkq8WuJWpnn6G6XmmShTrkhMaBob03MfzEHv63f7quNiE65fzAEPpd6kSup97CV8nYsL_R1lHpTPD6adGwLwLMXhjDMdWAk7Wy-IdBp_2zb7k6clVJKQ98-q8kjqDY4C5Jq28q5MaMr6cLzG-CQJ6HYJ6YoadCCeWuuYmKpTyudDa1vugCbK_HYCJCeYS9UAAvnRjlXJ3-tirB00mcWhkyWP_k-lOjo0jrrjR-v4HZ_pU9mOjUT0-AbzTiDQP-xnqdJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22210" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnbP2roMCNXuNaRRL6pDNpm6MVP4HyJFM6Efqxhn42-qJLkMLG7qgvRn2M6e5JinrYgJNBHOgRCWiOmZznYnaaBW_aPxUkzB3Dfy7w9w6H_JdE1N9289XI7oD0eriH9vV1MWELuLx0AmV_w-s-NgRxtDLOYSYrlwuCnDGIr1MevmX_A5PguR_qiQl9G3W1UiDnVSMMWlRfkyoJTqwYFyDVQVBHAdIzfpj8cBR8fYkzOQWrflmtX2gylriQpgxPkW9aUEZAXeIscK8JuzsCnqceBOPl3PiyorZMj2J3f4cgolwyuIntfAUumM544FRPhUi1bxGAp-yUIcb7Kcux1UXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوستون اورونوف ستاره ازبکستانی پرسپولیس در پایان تمرینات روز گذشته تیم ملی کشور از ناحیه قدیمی‌کشاله‌ران دچار مصدومیت‌شده و ممکن است رقابت های جام جهانی 2026 رو از دست بدهد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22209" target="_blank">📅 12:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZhyg2I53uQYUNEHxqHndqM6vlGOslQMSCHwfxC2MA7PRgiB3mB-W0ojQ1_okZFRhTDq_3DxNCM6O8Dz8C6-I3sZukHTGSYN7NCD59Og2ZfQPJbCWy4zmms5VxYrfeJLKnWy-4zcHzSNn5WAiAGM_gSiAgycECFkphcfItK_-h8vJP9P-51wrQpLD_Fv12PEgU77kwX7SF8V-3A6ppk30PcsnKApHdyiegpaap-ekyTAALJeUP2z7R3qiNXw6g-OE0BreGry2XR4cki1g8QpAT9X_2-olvFSDgJ29GclCYqDW8K8a2Goxp4Kkvs09WOQZwrS0-2pPxbJKid5zOYO8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22208" target="_blank">📅 12:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFpQG3nYiXo6ALmdbhnqxAZZ0kJNhB-PYB4NYHZpnKNUXjs5IO9kmpJChRFXk30uZB4j6u3fgfrAm5mr1aqyy54uPUOfBh3CtCr2GkH4BAVr-zKcsPwmPALbaVz1Xsq1qsz-NnshQANpHp2Yx_XpG4f9naRLuTMTWqoZydnwMXyNkMJh0qucLp4NFNv4LG8TwEXfVZD5Qxr2hIcR3tWtscIGm5dRiDBWgHylX5xqZwjtdtF5D2LHQFy4IWuYym_ekAF11bLnwZ7BcHU2e3nE_RXb-9oQDDi4AF79wi1kUFw24NizeIkjM4T-ma0VXdJfkhSmkXXxO3u6J7pgwAQhvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22207" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cER-XT0tx7Uc1J3sW0GNaVVVJsP-gkDDe05hkbAoqCzG6DtH-AcZXRqSNaH1fV4Aq7LgHy5WVxNotXyOhkwC__G9hNPBzQIQHbB3Z_gfHiR04e8CJMQ7XeUD-vNcC_oly3cvSrW_FWaTI5m-19hAF6YeEs3a_nXJa56zwYVGOjpP0Qgi-aEPbO-jK7buBcn4qY4C6yGswvC6QTu7wgUcCbR_K7lGoP-wTBAB9IVCzqWW9nmzjaFz5lopaO_rRT4kLgusriNJABTTT3UlKMI4_DNVMCXh_OIODuoRMJ2vfTdP8ylmDiz5I6ioe5jW9Tv_0j24591snlLn1sYHg1bSow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22206" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tndrsgkp8I6LVjBNW3tlh6PnWi2CHezq6FMQs2Woc57p5OdiF8V-hRqF_mIu1r8GQBJjnfWeGu2yjbuAblQKMJGBgd6xM_MB9mwp9XJsBE9ly_Nusa3asdx1JBYCAjKNQb4HwvYFc6d54r2aGhw2uHRasotX8h_AH-x6AYSPrsblLeBkEGoSqsmeTiAk5nh7yfvmrN5xmepE9pDjWFXoDVKidoVQMeH8AXioWzVkNu_HAEnIfGdff28IwGsTjagbzUYhHp1aLc3Fu92rONxFjdLZTIZL72UjhoNTeQOvIW_GN1EXYsLe_nm8nM6mEJWEZ4UE0gEu92uslXixVObvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخبار دریافتی‌رسانه پرشیانا؛
دوباشگاه سپاهان و تراکتور بشدت‌دنبال عقدقراردادی دو ساله با سردار دورسون مهاجم‌سابق‌پرسپولیس هستند و صحبتهای اولیه با ایجنت او نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22205" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22204">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy5PtIHfB4eCPQguAFmUapjnDBfo79eCZT26tLlXaFe2mlRhkDgrGVe9EOJbFtbBaAC9rSnCVQbfQwZ9qwMU8jWAiRuS5OGDYem0sbHfphlCieQK_4js24OGPw46MCXpbVq0mrDCCYJHC3Ke4bPr705Srw7mSCxALwGXkl8-_x8PGN79EhIFu3RqzcEcPJwMoudC1XnucaJtYiWTy9GcB4eLBm9i2dp_SsZMoU4zWMEgVQkiGv3VSr9EewgRIngM93NTsiFpbPBwf3ywTRc-esuhDtYHdeNccZrOY2rYuKCjedosXAyvBDWvLl04SvHfg6ZXNYZ1MUjFJjAf8J4WwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22204" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLJhvLP0zKHYUFuESfKaiVf1j2ckSAw6p-Hobywh9xGn1EGlU7GBlOOTcnXELJ2QRG__56YtVKZ86mOkOBoMoN-TZRzGh0J_ECInnctTL_jIhMQfK6XbeDsIpDp0SwZxOE9RV1FJPvenDiH6VOUHliy8X396E5kpGZXLw-3xZWmpuV_9fq1BXDtMWFHWAnzE4BN-FfwnlJ3CtKAbKNI7JWfn5Lvw1yX9wndTKquZNrfYY6eoIb6vLcK5c0c3CvlBZYhGGF31wYQf3pgehmOt4c9xQpo4jgc1toHyGKT5JDJNtFSv9YGtw5EZgeHWThgsry-ypDK-cO5EcF3UaZXRrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22202" target="_blank">📅 20:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HRxE9M3GhurS9EmiRhFnQivUXPFBErrDHSzLUB6v1MskGz7nmkFrxPKMdcglMDQph5lTHvmmPHhkmjCONJniwyQENLITuvcWIMDhQRTygnfOCIvn_KAWrsxZ60BIEkVaZgUsdaj_vuqK6A4KhlsIl-qUW78Qp40JLGIDLjcOdlqjc9KDVze9vH0N5cR4ui-GlfmeVzP0EJ0LnLqksqVO3v2VEjl4_Efzr1v0tMSmKgURd2zs9xby7bWmkVWnJsfUKF1_yKxGyGyHLQ7YT9Dpqub4K67qZ79WkQosVFctZ-l5q0NgJckMIe1ATVWCgED2DR5Sjt8oZyX3IowTyLONog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hlzNfjqOTepbpvhyA4dLRsM8Pk60OST0CNN9FyJz2_dJ1mo39Z-2cjKF9oATYxrGeij_Z8HwEEcrCF3T6b-bvYR9s0oW2FM7ph0gVwJtq5N0I5rVCqSUAix8bC3PEZbdy3RDNG-WFYkdjEDV0Y-cLT0eEqxTvJF0MHq5om2hk07EFbgUKavAdjDeHLc4qiKKCShdg_GPCHaTt3BeuspzJ0MJSJrL9eRgAXbN6sA3ORvHRXbIG4vey26N-PSRj_HpRlRGMGsoBu873HGrbUBmrF107hjW6p5ZxdF_wEg_ZLoHgGZqG6dd67CPlqjlHGevbgPgtxz7o_b-aXHSXLmVgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=tXlAYTL6Gt4kiC5AWlNOl8xuLY31e1f6jwnrLB7Hj6Q_H6J7NUmSwLhvIOut0LH5l4Mh0iVkKBeouy4PZ3zBOqcJoQ3QzTjDLS91Wx8mNo6NT5YWYK2g5DM59g2eiDdwEscf2VpemZj5CSCRV8sJuolKz4WVDzakedXYW8uTDED1DyzJooLzu1h1SW5A9Pfy0tSRyb1CbX2hXVYe86U9T3HYMRyc14vk9T19xCwjJGDTbbuPsqdLcDgonlNOgFgywUpQUbmSL-c-1xXFCeVdhruji1-8tB0JkDLxInea_zfbcWGS6eIJsvlvj1TayuP6lsVE4B_4WcMbRao1kkFVyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=tXlAYTL6Gt4kiC5AWlNOl8xuLY31e1f6jwnrLB7Hj6Q_H6J7NUmSwLhvIOut0LH5l4Mh0iVkKBeouy4PZ3zBOqcJoQ3QzTjDLS91Wx8mNo6NT5YWYK2g5DM59g2eiDdwEscf2VpemZj5CSCRV8sJuolKz4WVDzakedXYW8uTDED1DyzJooLzu1h1SW5A9Pfy0tSRyb1CbX2hXVYe86U9T3HYMRyc14vk9T19xCwjJGDTbbuPsqdLcDgonlNOgFgywUpQUbmSL-c-1xXFCeVdhruji1-8tB0JkDLxInea_zfbcWGS6eIJsvlvj1TayuP6lsVE4B_4WcMbRao1kkFVyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MclXA4F2FXdsgiBdmC0FPHRL2LhuS1PLvrbb9tViS59jtNzu3G0zawau5bekCfNcPnSvZTaarCLoBlEtVg9jpi0igiiyNhQelIEjpGpIi5LcRdF7Atssxw_ELhEWt8M6q8yFK_w7NtwIdUisNL9gnexNlTmM7_kUlWmRH3K6OyKfZ-hZlV2zfh3Lf9O77nw-r0cjATWMi7-tT4q_Jct9QQhTbN-2tV1ca7s2TNMJEoCYCLk9AjxeBSX4_DcQoijQEUAZyBY6Pwj5-aUVf-EpuWXozI6BbE0s6EnCtUiBb5XDlDDxvgwuQrb4FN-WG12y1WCut-lZhQZm_sCBtUAc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqTBAksGLn0JXW0QGtdpvrEXGefV0yk_X4rfU7YhuODFrrFRFab4q_sYTzxb-if6oCwFRd7tDdBH1DVkH-WisUgAXhTTStkol_9s2-pFLgRwRc8NYWMBhOhELrXkZ1JzsPwo9FEvD6HrjkgIYBU_y_kCFMQNnvpIb5-1MzIKPz678qfzAWr11b9zLbxDRkhFxU91oAVueEgf5PYCCOVYdnCZlFEk9Nu0596ihm1HPzdV8_3Pt2KO7bVPvoKt17w7tmzmDwZnSLBUmbYyqcDzXcNc4QbCH9FhiClLw97Ia6GsJA_CjGCUmOg_5adrBe6fjjuXVIjqsecI0cmo8qgHXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMG0CFpOBhQyD0N5ndfEuCD0uAol0xfYvSBsm_peAnrt7LIwy6nmbFoOKVKKvJH9D46Uk232L3n1evxtsJ7qCmGPPIYK2zr-9yV7lQu2kiuH-HA91aQFPljn5nFFFiWvrGlu9q9xK5GUpOL-YoPk5vfZ0DPuwn5fQFevCtQd7uq7PgCrZz7oLWryKi8GoIglQam_tocZs8-85Rjve5__rlx1Owk1eKiRfo4P99CSU6zDdytcY1qL_-MznSsISPAQjPjuIIk_bxjcesZ7n1xySd-Vd5m43EXn0N3sPcHMe9mJ2tPXUAoatXMPiE7Q13dty9aGIL7NCU7M8zrZB_dKOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5oNpvETkLvO5f-v0oubEvkf7wJi-TL0Ab8sll4itRNvxbOQhdo18HPRLm-SFMF8_jqn65PXfCnlssAqqF5SzsiZEzHYoTkJShu05thp0QOWpjVfGV4QlPWQWMEntSVjHgPWkw6EQwl1wgtPyE6oUzLP_wXr-tmeEExi_4hJrQfLulRTZ5QPEzPXPPtcy-yWV5JFemNDnzzMIAjFd5u8YN36w3ihkGrrs1pcgIvI7ONSxkiOzdBFDRpeRu9AjOeAFWNFfcnzR28Oa7_qSRKCfnCWTqB9VmobWqESjJ5DY0AMW3loQbFI_MuISXF7Mt5eI0kd9JmymxWY0Uy2nGiiQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9BAL2RB-1Wc9bC1oQZCKJSOnQsBnQmrOKXWkmYPHuak9xqlTQ6xSni982GrOSoF8TGMQk4CKpec_WsTQ6ySKIEfZZqdbsuY7zwGII8sK2_I_MWDS-39ZHCRzpQUk8jsQ7X2o9SbvwU9rCaNMv_aSJ6gYy4zDFtjVFRpMHGDKd6beSkpClT59XJEG3XZMK7XCSMXxgXuIIbaKIdci7ZbzoEfy3i2CyZIOM4Yp0b64NYDj8NowC0tuEYZYFOmTiqtyrOyueMhUlE-BS2V_1ZcfsQlUFinb-bRnvyQPcvDxImCWInjI_Wj3RgixWJ_WUo5zcv6TNzqxSxH8chGZvB7Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5XGx0t6HEQ20r42YcmoXgcSggC3P1Ehrm7YMEwPoMbTrgdSi63dYmjUnn1safw2OrtfXnLIaLmetWgUqB-CDaw-t7GSy2Y5MMJMy4UhlUJP9arrRzvamNrh2xdRioAE2x_NuzlQYbaIfSQk6a-Yy5JzNdqUSasYZy3ABjtQOWeQZirNdTrydrVHASU6vVpMkBernwhhOolgwMjgF2IK436wRvfOmXjIbcgyEzCAm4oei8cYmGD5SCmmzGhFCZs9L_zDpurE78AW88nFdkMnun3DlMlYQQAuM6CjgBv25JyElrcKBbpMnwEVGnKCv9y1RJ1cHd2YejbgwteL7xmOpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMtCXAYlV6BcDAgcqJfzmu6olwVPgL9nOLEUgZYd7pX3QVmU_2DrUJ6Vw8KIK0D6nIAmDDjJw-s_ispUCDoLiF6lnlx0M9hZ0laTA_p8TE7EdRpZpR9KHE3gs8TQP1z7wYmQTlcgz_RM57BkrO4zuntZPdMuh1nZVy3b9r5E-QtvJ7IT4WljBktjTquwIOzIvpyt-jAJkaIrnjvqV9yRwE3p-_SqmDbI-_wvzz8zCWb91b97AKz-vzyroi4tNd2ZplFQmLmydrjqo5CiDzZkLDn1td3ErlPy_QzBW7MJBBOeKWqVPonoFLdwpwKW5wK78wQGuNsTZURIK1AI1SxJYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeIGj3YL0oA3eY-HiF-M3BE1wN1RpsBAZ9NgeCXWd5Yz1KxXHARdpNeZm2APofGg4cGReCaS9AQ_CRuy2bf31N6xyX4uRRP4N0icEagpPHQTYeIEMvWW_7fH991OSrDeFyiVmE6EPPl6EqdDpPQv299kCKYYruG8smCMCse5DzUlfShkdP3XdbETIyqzuW6B0mWe02ULbab4GD7BhD11_FeCerNXG9ZXyC4jrWwM6gSAiG3ejS5P3vpHzRLYZRCKexqx0xzC7_-ZSuHBv3HDZflJhxaVc33wb_rypdPWt_ja7XzoE4HGUNuWniabPao2zFZ6zRnBiHzF44go1SG_tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBxkCS0DgprSZpvQcj634IbUcB47PLz5M71M41bK8MZyaFDnLEOffckfZJSn7MUCMLPexlxfQUGaRXMotvB2oxOpnht_vzoAx-k6GCuZsbzPDsDIRQwc549ad203n3eX-jkUpuPJcBAlwE62d9C7qPW3jaB3Fq6YvuCiELJJbxlmnOMK036Hr0Jr2ZSJzRkzogpZkW7ugHYx7aoasgTRjRz4PiGykKbJlS0peDifQRNlwXBUGX5nhMh73o4l8qbIUoZnkQtWwaYnXIwB8AC_lkcZAnx14AlLwOuzJPXKDFXiFo62tbk6W0piqdeHn4Ak6BoIazNhe5ZHY5vOOJ06Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGH4NLX-53wR5c3ynOz8gglJjLCdGVBuTTIrbFjc_IMFLwVfyxXh4KsFvleeVHckENDJ2ELzVMKm3rAjrv3P7R4IkfqP3GbBpraHyLPovBexsKDJrThVwYFVF4Tqr-0gFkjbnhZA_Z8tmEMyyAzde2HiecA2IjaDRzuzGrwGpAjYN-NoNXURj2JKkf6qdTYff_JZVwkeQJNAOChDoPjbuIugp7IX6sVn1t3WFqBq1mQ99ZE5G49kMM3NZZGcfeCPwyqPm3KBw_KIlmEtyvoTIFXPXnB2uht_a7jX56uVcO62SymkxammiTlbx7g4RiW-xN1R7PyhRmp4RCXdlAXZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZJtvKkMI2PHcjvyHR37mWc4XHI_aMu006cIVGPZmXGpld5IEF897QBXGWxVkSdU1K9FBRxF7-7Lhu765D4xQVvs0uxhfQPCkEqk6h0nAiyXef_CmYCDoq2zIHIQcSw6BuWGNhuhBdmKgiwK8fTZzA1oVoWZ_pQ-xFjjDt_dpLvie45vSTk5o_o48kAXaEIEl6Vwdm6iwU7Y3bMgqVkrlS0Gajp9g3_cyWyUWZboweY0EHgpx7ID_XEH0IbeFKTM41pqWgC81N27Cu89vsWjDhfvqEObkGjp0ZujONMsSayuP20_-zyKcUaFLczIDMFwBayUfeqlmeTXDr8UwY_xVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=hCzOe6liUdtoZWW8og_VR5q10323bgmx10e4vh5HvWHgUKcB2uNj3x_B7GQH0AInIoGjWNV5mFtVRviBfE_NRZq8XlueQ1m7cgHXGAJp_WX9yYzu8XoZSz74a8X6VqjfGIRMxR-_xrLV0GobBhP-Y8JzdyEqb2vziDjtUA22yPDQlI5V9u_SbyANOlQT7twD_Fo2G7SWK-HW7q6HmCK7pN4clheuyEOKrPlIg8ehDdntha0Uz_cEu0QUtTGhJUm14d9Y_FeclV-T0SAPc3b5pPPtgNBqbfA21TMNFRByKfHs-VyY4zgIMIVoK4vefvfeTFvEKzOPcjix4Kli-ZLjIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=hCzOe6liUdtoZWW8og_VR5q10323bgmx10e4vh5HvWHgUKcB2uNj3x_B7GQH0AInIoGjWNV5mFtVRviBfE_NRZq8XlueQ1m7cgHXGAJp_WX9yYzu8XoZSz74a8X6VqjfGIRMxR-_xrLV0GobBhP-Y8JzdyEqb2vziDjtUA22yPDQlI5V9u_SbyANOlQT7twD_Fo2G7SWK-HW7q6HmCK7pN4clheuyEOKrPlIg8ehDdntha0Uz_cEu0QUtTGhJUm14d9Y_FeclV-T0SAPc3b5pPPtgNBqbfA21TMNFRByKfHs-VyY4zgIMIVoK4vefvfeTFvEKzOPcjix4Kli-ZLjIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raasbC2iMeAz2_fhLWa33AbP-gkzWoxUImrO4t-t4zF-qSUYgU3X32ynMx2CvufaVvyaotdZovnAnFZgaH6YLPtI_NmBeW4d49Tr2uVPoCML4RIcUVzGfkKnPt3934GowFF3Glr8uRsZ5PPIwhQrY3mx9ZILWIWSZfxrIQ-oPPvMZaAHJnPwlU57lKL4gfRfZNAaeuK60BILD7DIIuSm4gVHwRGt7LYyWHZxe-iqBksSgCyu4eeZMjO9jpWARBR8fps6yVDSu21HdiqELscNQouDWKVnCjFRh28EYXTXC3YZuNq1lzK2KpeGSLzZwZSX2d1TtY8NfpcQaQhtoDRb8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMQY2oBTSXTQDfT-jYmlaG8ET-Sf_SIOrQhFA7ql7nyhBg_QNbmvUuN31qBGHUuTCjuZO_NWxOXS0TRWiZqq0QlVkOJJoDDd_Jn7frd3laaLaQGLIe1mW9DUkYfOB-E-KjxHaLpqGGfUmpwHK0onFE900pp3PmjmWNDFvhowJ9KIng6auzX-V79b_uDm6KMgje_WfKP_Hfnq9UD85LADI4Cd5XyHUiZ4HzQBOuqbjK3_CF6GVwjifI4H1yYH_1k8msiRxZ1D6YEXN9emxAhWxCQhgBBj0F9KAp7J7-O7EEg2O_5VtmMJDPUeueob4Ba6x-SbyBqjLR7qcZr50PErKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdboWvEYyntEGcPPLLlVnChN4sa7nWwGADJCEo5eex9Jp1cFGTpIVvfUcKsA34nrn0VqTMrw9rkSLrxNdCGaXe92ZpQkRUewX5SWzn23MTtgLaboSO0imANngCtqX_ukVVlNGtEzP8MjBZ39iy-d-5i-WrLcxa5lZZpwJz_WAP7czsR8wSIsHD1eNgA2ogoOiCWxrTky8H78gheRbavmr8DIhNrB14BS6XNB-P4HzzvgF4JqOgZ9P2W7YFhvqQdaDSNiutHqEQz-vpsPLIH1gB-cn9h-PvfuQfpgm5SahRlfSPoQYrVw2b5QcWON9dr4PDwGVyxtmBP60dxnyAZKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
