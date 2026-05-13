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
<img src="https://cdn4.telesco.pe/file/POEiaESeVTGq8viGn_VAawxhA9UrPVO3p_johTtf_w_7_a4SKEYlABpBYOn2QUo4WAXFdLQA9cRLrWktah7bxH5lxiMayJGmyJkOfvQTVI2TKTpw85I-dL7abU-v-wtSWdEAUenbCO73bMmbyJrgRtSx1tttck4srFJkR5Qn5qH7lbvRxkY9kALmEOXHQURnySI5sbVDqnOEXeC2cyj8w0Wf16ven0ErXY0YkGZgPJdZng-Vrr5eelqn39C_cUnrCpY6Xf57wLeuo69psXI0Z4nPNUvSfFc2Di2v6lDPnLl5T2dAsPK2Wd2aQlXpbVJl8L06TjD9_WgqtJreqQTCpA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 213K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 22:22:59</div>
<hr>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThjbyQeNHqMu79xJR43-BnU0P8nGmZ2EVQOmWeUROYnDnc9anhIqmwYY07A4Xv-YHrbnwOnQIc195FTdNAerCJ0PDDvpU5TcVekW8UP7Ph_LczDCsWk6IUqll1dTMAmLglcr7L2YGu0hiOqZ6ZbMmP4qQ89WAKXvN85qh6-6CeBM6C9JrE1nAOStakbH3VMUXqiowHcQ925FeiqVp_ZMlouj2ioHi60UsJoOy1EGsqD4ZN8neXorK-YtuwjHaA1hP4h56xTnqq6QLskj37KQ4Xp2QKEb2iHhyqmpMF72I6Vc4XltHoS6-2NfLUyx_HX65JyIzHeAuRD-TorGmcP-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzKuMUwsX_OEQ2A4CewD8M853V7kWTjegvX4Jyp9nEl1LBII_rZPOhw8hHOtTczbV14JgxLLpTWJ0kMrRmU-6-IW565OQs1XQSBJ869HlVy6BQDQM4sFeZ4llP3K3CyJIswa2oyfdfgXZveeyImfTsyrraodLrzeLPWgiuYFqIjJWeJDFuggISAsxrh7CndpeACN1rvlQqUAZ3qj2ulh9Jtzj-ZS1sdB0GoMiahVjPD10BoyR8HcQaeekPFGaSMvBRwaLq5itH9cC4LUi-Q1JNffsSfZOpKKfkZSiFnxrCcEps8tKEu4d6GcnqaRD5CxrOBaWFPTJ2LUEo0S2tbwAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ien6wdLFa1M9xhYdRin8bGZ0aIfXR8lF9ywnVH7IrtDREzZVUtCrrJLA55akbk8clB71c4WfzJbnI6zzrXZdC4ILzlz8VXdL13gp3wa1XeUELMDewoUzYC7RtW0S7EolLZgRZzk6Rc79_7dAqS5XR5oSK9nxZLI_8fyKx8Pjrr-cuE_m8Ilfr5E_Zl2Iz2vRh8kYfMJdl1B6nJ-6vZDEOnxkQc0rDokW9N91GQxRcaY_n4hFmhc5WPIzz7fTJ1qp9IzEMpvSpsYs3FpMO3SLFU8ToWSvb2qeH9-JMUvPGQTya4jA0VkL1NKQ8y5eKNnyfg7thQWlpRDOwgCgIMEQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGUYJYCeg01_GrUdQ2c5nCK9HvC-pDiORrpwvhatRkzu4zwz3u6JZxXkQtHYwKOSlKcKPKXuXDWbZVBa8TLdu7AYOj_L0rxCapOY7aOHQjcVw8HlI1ro44Os2fVJ86ony9-6KFeUn_QNOXxI_a2SFjxZeS2MEvcFdbpj26M9UYz2yxREerAR-82HLhVN5QcGt1vPDe95HWS5Xe0v8SYk_kHH1oufabHXP0wqR60v3yjC124X8SIZkVlxsQlvtii3APihfJWP2mKPVu1Q6IyGa9y_O1NdCRWph4oUOfnrBqzqtj8Yzwo1j-84xt196Wr85QLzP4wWQ6_mg93UwwoTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKlcARNib46iBTfCqticAV5QV_CBxZjumzVuQ2t1KjZAn8bgcAx98Tf_oFBU7-88rVoabYBeKqShj-mjlSnwdFajGq6ud0G5MXOa-ds9X6LibCrTYJyvI9rToIoWbi0Wt4Y6fugB2ckk1m6pFCYP7JQUCDHmZE80iXRditjW6s0n3-wvCqG3U5wzy_z_kl4vgNZJLquOoHOEXs2y33hGz-VILTuSP104a9ZfUNuSRz3xo8HjZEAgYlhvYE0rtu9cSVejESjGi9-ayRVP6pwGscLqPj3Tj9BIVemrxUYbOvgdhZWaDapA0yGxfS99NEuzQShu6437n0c6iwdpq8rzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=YbZciyXD_KI3AnlF1D9ZCd9P0G4nYi6YzUV8n6dx1cNqTQmCcyKF9BNQVd26M5eIUtTjS9w3fwbJ8TrcztgdYMck0zH1Jx0zqfSohUybTZn_XadSRgUj7tUCAHnm8kRUT7hw4zHOaWSQawnKe5FbYrVgkG0vyooa9V2y91pYSczsXFMaX0_3a-Jyy0jiqATZ-5hgq4SUCtLq1Q3llgv2RPo3kEWbO9JOW6IaS32u7iGJDQGkZipXGIRati_96HdMwyxyh8vo3EWPyl24RUN36hpAEOS9D36BA0Xk4F1GlP5cobTegNcBZgySPk2dVDP_Sp4Ypx0XrKYCxlfnzUbNPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=YbZciyXD_KI3AnlF1D9ZCd9P0G4nYi6YzUV8n6dx1cNqTQmCcyKF9BNQVd26M5eIUtTjS9w3fwbJ8TrcztgdYMck0zH1Jx0zqfSohUybTZn_XadSRgUj7tUCAHnm8kRUT7hw4zHOaWSQawnKe5FbYrVgkG0vyooa9V2y91pYSczsXFMaX0_3a-Jyy0jiqATZ-5hgq4SUCtLq1Q3llgv2RPo3kEWbO9JOW6IaS32u7iGJDQGkZipXGIRati_96HdMwyxyh8vo3EWPyl24RUN36hpAEOS9D36BA0Xk4F1GlP5cobTegNcBZgySPk2dVDP_Sp4Ypx0XrKYCxlfnzUbNPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22120">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaZk6yrncL4VDpcPdrHkHpbDZwK4IKCfR7JaJpTlgtwvH5os4q-_szQMk3D9CMEPDP3oR7ECjJhPTOkG52FPiKT3eZUpMcpzzzZrBtKGfwVPUxSXap6k89wmJbOL5d-ZQR65-zPDQnf9YRoqgxAC-Pv8J4ov4EX0FTm0vxnqH9sc8wnTcJiRzeh3DiHqNJknKengOqRcMvtJIz5OEoEgGSXYYBudlWxYlEXSIP6RrSPjd1H8C42CCt5_fie5X5sSKJSyVbuZgXgX9WIE6-R-64aiLLcgyDnGNsykK6uqVHhAL8y6witSiWhRJ9H7aj2KDToegZFHNNNvUqepP-mjZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورودی کانال VIP بتمونو رایگان کردم
؛
خواستم یحالی بهتون بدم هر کی جوین شه تا ابد میمونه
💯
https://t.me/+--L2Hz5HpiY1YWZk
💎
#تبلیغ‌نیست
💎
👀
کانال وی ای پی رایگان برای همه
👀</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/persiana_Soccer/22120" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvP8q5LYLh3yqr6UqXHauWPrQ5dWvoX2yL7VGc17TecPjC3yQBq5ue6uDAGbZgG8N2phG2OnKJb3RfHevkNlWokeELtoozFo_1dLe9NTts5RpwUEwDF8y326-j9okYI8Q1B-4Qnmyp7kF77tP2HK8EjmIy5gw2vsK_KwYmWQtgDCbAQ4JBR2whyAd3PZHxsWse3rPUsEVsDSwyFINu463uPdPT3zNRVDDD1OoWfxFwMblOLbAlX0dhh7T6GLSE2dyahk3jBdUlI0m5OfftpJub-Bly2MNNHOoV3NlwM1S_RHA1JDlpMlovEorLXh4epxHzRYIv4nWhV5-_hKcGvXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xv4MxdOj2Zj2CCoIwW0UayljEpy1l_FIzkgvF1m8NMP9o2vWdoUfNMzqy3LW1LmK4CuvVBRh7vhJIQLM2tCfrXi4adUSEp_Mxcu6XmHkB5iojTn84tL--oxZHvrKUQ_8bo6ktiSAFYCDQsioPVGkqzUG-BfTqCaBmyUB0XFsW9xPSQw7oxLx3OJ3jHUzoWtovT8WC1BFlvfAItZOBblW20gGuY2j6nc0M8hU3BCtKTLrmEFSppntYUAYwrSpnkHTum8v7Jg3ufn1UZdn8GJi5UGhmHJkh5t9jcEFw53wa20JBs_G-bJYs2yylSW6RmZjXlNuZR55pCMJuO0g_DZPIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=vrRSd5peITwrJyZCZhy02E7AwYNz0h1zwoQFLapDroSXz4rO-lrLJPz4Agrmo7hQTOUWhO1jsYIej1yG_K5oOITin_UlrCh2z0sMy57s3WTGkmINZmHf_ZXKcvj3h3eCkwgwiEFMNoXtfgv8-NFbW6ENF9Hng6gP88D6hAb70nTqC07dit9SiLBOnbgvtbMffdONkx4uBzaKCI2snTSkHZVggubD4mIWwVEJXSXvijSIjxlm9lRsdtaMOPfVKtfggQyhX4IHaVrzKSvV2VIxKJbSy3A0RJXiR1ZfrAgrrlMSKk2DEHCmRyg-jlV5VRt7Xq4xF24XWz69bt_fUYRkLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=vrRSd5peITwrJyZCZhy02E7AwYNz0h1zwoQFLapDroSXz4rO-lrLJPz4Agrmo7hQTOUWhO1jsYIej1yG_K5oOITin_UlrCh2z0sMy57s3WTGkmINZmHf_ZXKcvj3h3eCkwgwiEFMNoXtfgv8-NFbW6ENF9Hng6gP88D6hAb70nTqC07dit9SiLBOnbgvtbMffdONkx4uBzaKCI2snTSkHZVggubD4mIWwVEJXSXvijSIjxlm9lRsdtaMOPfVKtfggQyhX4IHaVrzKSvV2VIxKJbSy3A0RJXiR1ZfrAgrrlMSKk2DEHCmRyg-jlV5VRt7Xq4xF24XWz69bt_fUYRkLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npPOJgp7U5iCQFk8H-KIe7EhRjpoXTwL_c_V97zfpjGLRXrHO1tXpIvi9ht3HvX-00s-2fUCIaEnHV9VgTj3rqxuOSEGY1NsE13Wxg0FIspBtjGiZwOCVnKbWEKE0vR0Bd4mumXne8DK_avv6SHupq1oP2wi_X_eKBwlYQid3yU5bSF2tukBeObMAFw7OJLJAij07yht51330nX-wjwsH6NTsshIed5I3BpeiT8s2jnBSIY6opsX3sKwpfmVBU7SmYjwhjQ1YzcRG44pB09IKqT3T4rDjqJyPSDaaTot3SZOTUAigNBxl3Vqtf2CtLDr-v2_lWqnoCNYyBNYoF8YnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Ggu2WqGtdXFGUlzxjOnEmGrpIuPYmINqMOcLnIQ6uKC2Usn0kzGqyrGY6ttnDS5-ssNCo53HHlxiThRWK66eSDZaLoq5ViNH2SP47qdNTAL9h06e0MQ9cTTrpCMuIQ1sSoRZT81EoED0Xk76Qu_xDZsiqXuXefQqvNVh1Z80RHbhzXddnQObASrjGMId64Ejp8u8f7etqzwSiwQcvghdfAXOjdP0G2PJFhj_aOoGJUX1mFOZnNlcvhHTWlG4CYf_2njZfsrwL9ArwXoYe-igo1OOhPhPxcg5z-PeItUP01EKJqO5Epg3dkIeIioax8_ilGoT50bUyyzlAqURH9TSog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niqCgpKWx_Iz6PXuKXCHlilV9JKYvT4yJPLxiigsdMANZPbxjWhfx8i4SYWWWFBQvBVSMkil22pT0a6Q099XeBNmk31_lTlBq2gD7MaGcYKuOaPsTtZWPxs3hvLzIOpQY6S0A9p7cSiVecN-EvLMHmfk4EoN9Iv3c3ZEdnYYPofejn49qOb0hQoq_j7CbCR-3-VHawGb2VvDFzPUCDPq9l6KJ7sQBV_sBTxPE1i2jxBLePUuzjEq-GpYkQhaZZQlYh-gBURMRN5exlMatzZmq6dxjl_W05h3WlM4pw1sZjha7ZAHuT8hLgu-Ey05ysnebQnRuLysKNbz2VX8lccYaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0wlq72lcwngfc4uyNmQ85WgSqOEX6-qqhYcUuR3HjZTIAjNX-RNXRJMOPlP8Zt3KPx0SrPwhaZjP_BXvzzJzCP8EQM1LkwfhLAJSa4_hjd98G30aJObMPrfWfVknSH0Z1kqFkK4iLuygpA5_NEizO506Esw2u_UXd4iqOZ-WH6fE7JqgiThNYE9AZLhInjRexssNdZfeyQJZODgGgYX3nFBNd7IrX0dM_9v0vzHIqlmvggDT1gKELs-a7stQ9MCtrOrtGOsdFoeuad5345H6SAn00m8logvKtvMsqzox6lqriGncNy9EfEWZubOKY8pVNTqrdzEXn8B-Xj_gukobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTMa7aY9rz_JRcdTs724gTdYzJv9J-f0hxExZtS6JAflWRjRx5QgEr2jECru2FprjW3vpqSoghhRMexLkk8PHwy2XitWpcALLTGJfaj2TdxpBwBqKfmjaH42RW2zjtsPFeJgG7FJj2wogeySySpFJaHDtfumLN3zUBxFFDo8SpVj9cNOWd0WFJSBK-f9tUEVat2otvzlwmlxRfvBS8raOFuD8uyst05mQ2mnC1K8_6ChTC19VXHjzUIvam2l_YGXLg37QhhT_lCA1JBeSuCj2XWzwqpZjJT2tPxs4fJ1rAdNFoXtOK_Ki9IVyXpSo9M-PBYEpQ51vW8tdp0duOavfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jpx9X4yYicz_rX7fcEtyCcq84rjAPlJbpZMsNKQmPBSXUGtU0o1dmj85EJZuEpebtKsdxiNuuEW86VpAOneA3tonlayh3cDBMwuEHSTvrGNU4i76Tabx9XhQeujs353IgKqx5FgJVnj09UjMPXk2jEorlkxQMGbcMHpyPrOBXFbNneBjO8OYDf49wND_eYIBeoQVrSxvnWeGbdyumnMeVwFX9adfVVkCuf82TLlfTyRuUVE3m2Mh5_NmzZTr2wscjF_8bJjp2k5uP5cRzggUg1QPVvLMgEiYmx2sNh8b4stkFUF191XpNzJ0l8YW7M8K3pYqUT245IuEyPV8hAtI4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3JE2O5WqdA7Fhp_BjV1Zna41WOfHlpILM8fOX-1PO4tZG9jKixkZ900A2_bIhr7du-T9tgHx1unoH6-N4AbFXwfxnaV6LSRVKUQMeAi8zAgnaDSdqlfyCyZ6uqaZv1ptjdJYOV_8Zw1x1DWd25DmBC88H6P_L_K-w1dif5lYvwwE3TtHoj6XvU-JtEARIwCjJH8JBJyreu-aa7c8ibyBsHT1FjW3LE9fSoCaSnbE0E5zHhknLE9bB1_Stc9Ie26HMMEbU2VvDNiblW24kXll7xIzyyP5-XEXEUGQj1JdtpcchBm8fYNSToKuxpxHl56mCzv2jnn_pXblKrvqHFUtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqpRLcUGyUSXrwroWtu8y3-OzLaf6rSNlMporvson_siWV_2Du0VmyTv3NJ5G0e6tbORy6cDAToEYV0MVciX8jkI7OJ1br0RNREeViGrjIKfF_l2Ybl8Pd8FZfl8m60-eDqkOAnZNwx2YFBTD7NO0Qq7HPz5UcVAndyblDoBuxZtOiPa3fdHrtYhfOY_e_cNJIovG7tXsEWyHDH78rbNwMHd15AuBqVvCewIAvgUs72xCFNYTxHbYQx_ZqS_dGRl9F8lIKHhorEuKUjP-yy3Sbpt1ffZmcn-hLdC6_s0V6fRM_FSir0T4sthOcUaxWsIKzEkweMM8l6iW7jP1rHQOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMGBJTvVERXdym5-07Rm4x7kA8-I0ecopp7A7SYa6BeZ6fmktXos6Z1_BzFgR6Oe5h1j9rzsVKQP4_XVis9k2w5L6XgInhttcpMYK80QLg9z_c0TgbxJvw0JXcYCkeL2IlQ1tGyf7mM_qyLLPD4zfzE2zWIkeGOqZPjC1ZQXVQZ6-pXZJAFy526IUBKVXm2QeLXtJAHUy1CsqU18-bxsBmP1qysMzExxDdPIwO9G2wrA6O6Ldi9enzFwNt2ro5klwPIlab4N9J0rC4dHAeuE4M0hLwzH7lWm4pA62z1Kxd691cTb-iRehHxfbIeLP5kZ5-CJj3VUBqPRXQtLc-KkXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8k90byaOL97ba6Vdp3PQhD9MU6WFNtI65x-k9TyXONgSPgpgiidFiDC1vWtyL56c057Go5UWf1CBz7yA5uf8BMHfo8p_mo_PIMEsEIgzARTJX2AIcSiXrnOGNv6AErSWwkRIwc9jallnJM5LQJtpNKUKcDlv4npnpKKw-qBSjvZKgYMkMXL0LWFEM3p5Ri-vnUBmMOL9kCqw7F2tsoTnR5KVcEeOft-R7fLxJiJO8uZdYIjSUQESLr5ezCWamu-8MGH2QH7rdKLWREJHLPzCGO_rj2x6YAoDriyEDHQUmcj_JkfVR8mUIA-92O3XgaJPSExjFazR1e-tbYCzAyzfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ost2UbZMk0aGz6NGeBloR2uHoiNfiqS5mtFfA7GfVkGlfiz6QaCcMGak4PzM0mz1oYQe_BP6_qbuBMb-FsX08h_iTLai4MDZlocN78juw7P1_cCyE6mjbB9Np2Y78hTQ3lzZ428LbLy2rjmknOn1U7bXgxL1mcJb3Bpex6NJZyGTMHpLUR3d1Zqo3uE5EYm2SQhfzyNLM5vCQJN_jY13QHGQ2mcWNKyMsh_L_P062ZXpJdU_b3xnqliV209unIPPRzVTiXmSSAaKF7IN5HGsfUHRCKL925i7v8qmma-OqEGqH7ETtnC4OJWJqDTzqX9jchXWUF6xwkgL4Txwe3r7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMU6TTP1VdUXHG6pBwSdKjJKMRSVCojp116coo2DFRYAuhSW0UCIMomh7vaRcz1uO48pl1vnViNWsppKJKx-oUr1WrxLEStvC5XZhmoQukOHKljYZxoAoWHNe9FxZmg1LUL6tUUj-EHkZ6EyDY3zx9i3Xa2p_SlYEBV_g1gllsAm2_mDxTHcL1iaPp1Jh2NDBk7hqn6eFLpVy2Hc6FmMfI3cpBE5621wc8r1XXWpiaCmCsBKFYcWbGuRBSRN9igT5dRYiWGBgPpTFxw4cf3c0X8nXe4l1o0Wib34lGTjt6no-YCRoOFuAffFrjK2c7etbDPfiFoJFTOVTQlJE5vH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p85FpBddC2Cr4VQ9kYO196y3zdkE5LjFJCIg8EzSsz_hApevakNRHxoo4k69wagn10n3mYJlyLIBM1c3BwVPFo-zSiZIewzH6J1iC5TKo0C2jluhYJ1azeS3BlTf3NlfXFyrklmCxozki7pzVO19T59uzm5m9nEEEDsXNymv_zBkNZ9qQ84EO_9os7PhtqyYEpm5g6b7UPOzUncPinoklhJEUXwVtfhlznNls3JQJnIPfCLMcnWHaY2mJshj7yPMPv7w7I4guLIaO7gtGrmZvbwSL7g9DAM_HqbGQVh0hPdb1NUp5lXY73O-L3l82RKhCfcObc1cO48-owJrbxw1zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hs233Rh305m2IwsDBHaT46rWelrpjWH47j4Rjd3FvGmPUwNWTa76Gk2z8NaGB928Ozl7X8dVzbevH4X1PI6RwrkRVRLKConU4QIjo3Mw42zKSM6qPUCZwvvG-8HyyfRZxwmFZwu13GkUghPWd2DT0xPwQZRJM15jRwJOTEVYage8eS-ahtF5VbfweE8ZOKZ86RFpWjzUMyMs5eBHm7tck0X1EgsYsWEyKGBYRm_SW_-tf6eR_BWhVVelOqXMzAOnXhvZNgWk-gUlfrdgfztcLI91Bj7e9ph6Thwqs7RQq5dywX7mpAy7sT5JMtfHMlPOojchoSKPVFL7rpKch7AndA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=NnKxz5DKYUZgwqzeLTgfmA8IPq1ZZvSftAy9tH73HFYtiVVfgzrQF0oEs6jQqR5OVdwZU59xWF_iuyYyggDo9JJbbz03Bob2JqlJRSf6j8lD7f5eZE1q1IrHPhRUVpo2SCnIQw74gV8hOjVEY-vMTa6PLFeX1jhM7heSISiPfzv61auPGSbSa1kuCnSDaFNe9S819ulA5-PQ3JqoweVkILnxKEdnLlLo1Uyyc9evSm1M_3QxFcARxN_71I4zf2BAtV1Pt9sk0B6VX3S9QrrhH5n7gN1d1rCVTzhEHkN7dU4AaaAWyAuw58bHW704ez_xn6mCvGZnLa7hDn2DvWykBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=NnKxz5DKYUZgwqzeLTgfmA8IPq1ZZvSftAy9tH73HFYtiVVfgzrQF0oEs6jQqR5OVdwZU59xWF_iuyYyggDo9JJbbz03Bob2JqlJRSf6j8lD7f5eZE1q1IrHPhRUVpo2SCnIQw74gV8hOjVEY-vMTa6PLFeX1jhM7heSISiPfzv61auPGSbSa1kuCnSDaFNe9S819ulA5-PQ3JqoweVkILnxKEdnLlLo1Uyyc9evSm1M_3QxFcARxN_71I4zf2BAtV1Pt9sk0B6VX3S9QrrhH5n7gN1d1rCVTzhEHkN7dU4AaaAWyAuw58bHW704ez_xn6mCvGZnLa7hDn2DvWykBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsNpIVlZ05S3mXbXeve7XiS6osG9mAtJGU-lZjJyKw1bPUoishGUDkw9AW1dYjnqQw_t9C1UCQfVBlWD6_SzVNUP0bmUtWVXe_YMDusVJH2t-UbBrXJ5adVHSlB-pHMYeNtMq_VJpeSLA2MA6U_uUHSICESAPncAhbm2DedxDUVnlIl9y2puJfSBPaNYGVEiT4Pw1pHxwkp_pohcp_LhA7TwK7B0PPnw9gtY4g5UHA4q3BKl1RgaashSlyQBXkJ9oOv3_cHXoUJuGU-ylHzFTpbPOrTyvBx5W9WC5VOXW_GfvGaB64CcxArCKFGnUBDoSHUJ2Tm_P5Vi3QAXGp3HLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhZZK_9T15GgNec39i5reDfIWQy5g2ABBDVu_EQ3SSbyMWvifHdXJ2z1IYoNE6QzjrIZfxp-az3Dxl1om5IFZCJHsgiHGm_y_lxYkVJhNuTBOYa5E0fVlWNrCClOkQYbMUNgwgDPkNvui6btSXaIXCYDzUj6A0o9QZOzwOZlinFPI34iU3qhQO79iY5inWA9lNlOLvll86kZAyv00pI4wdtQqYCIJ22fHjGAZoZq7eclzQgnunVd-bTFCVf8Kl2SX2SGdU0vsOmO988oomPGtpsrdjmil9ajjgBEo5YND8yHfEnqIgRDG75YvxWNzz2kYQSNFMFs2cJy9pdAivj5Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMDz7xOIJBaJ_Tx1qlXnJzVperkc0vcD1-d4SDQElzNEcNofv-fOjMRmt-Zjzc-xD_v-RSlIw2SNpCZDk_RDF8sckqG-spa0OOm_A3TUwVj3YvLdhV2bzuV0sNeceU_dkyGh3PAZg20Yg5wpcscVylhVcwVlBYxL5scDPdzmOepWdB2lQ1Im-2raQk0K2e0U3enIf6S-3YtyY97RF25DVVnrssMdqjDJ4An3u8sFhffRBdXcRBwu8CMIdhWwnnS6k3f3CBjletkQMrbkbvHMfxrrrK5JFg_ReBxRR3RSbbcXTBMrzqfTrx5thzB_t0xP-g_XGiyzmzteE7PutUaZsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ii42wH4YumQEjb1rh8n9W72lKAWjcpaEDtOT01TeF4GZ8cv5cj9OTivZz3HovI6EroqjCOl02hhVjeagdQuRKx2MyG2okAleWVRBkw5jG3G5wuxxIQ5e1XNRgkAYpkQhgcKk4R2nLUAKOGZvl9YUBJlsZOmdAkkRVT7-WNhteE5BrJdXRlIJm-VjhWAJy_XQg8XAHyasr2nW19u2YrGhuGFVQRaje12K4zIbXLL17Vx6GRvB-uaOn4jRmBW8yFelrezgoY0QeUeXilFa-a_veVfDgfv-Fvn04UTWnEoz4Ar1c1PqCdzG2Q2Gddfqu4x1IP_RXBJDhlazp333ksq0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qamog1u2CPzPZAjKsLX7-pGGftbBhExiQTr_RfA9gcG0TrjU6m8tWLDoeyeMmAxLSdWDFmNa2C7_F_uLm1GUwDv5ewMZWUw9NFYZOa_gbsmEAtrH6yF8mLb4DJ0az8GszppoZ7ojCobWlaD0FSBfGaUiajqHj1ht_Z7p3m7ZWu6zrqPCTzl4YkSifMp3cJK31U9iJ5Sle92EL19aaZatrTiXW9HMqwh1sGL6WC65xjCIL8_lwzvgOjrcxihlrwMEx8sc0L_ImDWnZ-mS2ie1Ftgrp3kbAS6GtWUIURAzL_ing7JG59JjfWmKNdFIVCDyybhuORph40JTVtZZZ6nSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfCPYbK8XbpfUK4p1eduWMSrBF235vtUP12YyBmJcUheyjdyturCc2uzQfii8Zh7yc4lXTOxXCCh4EJK1j26_XU5GJ4w_03GY3pmB6lrO4b4goPu7MlQV8cUWmdkCrULJz_MXricKxgRO8f5hfQMmB0oheFGJSVuai32P4ADmm0U4wZ0qhQk3IsAAbvilSGiv7eecyxEfqli8suy7IeOg2EiC0U8TMCZe57BPJze0hP58vHwIk6eiqTGD70LMBEQTOEIvazkApTUV0C0K4y_Zwt_2W1ZipCis0qXFzGDLf8D4rNWlc--XyWfQHf6nNrBav6t9z-RyKO5dKv7oRBU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1GAZjb-MMwuCsMJlIHaF93uI_pzeZC6HyKBUIKPd6fh2xBYjBZyvju1SB3IH5V9IG8G1BZ_Btdn7NC15dmw9wCAQxhe-DtkUIYCCbF3xcK4Y5-kdgQb4j-1OQN1nXj_rRPumFRlG0rEIT7Ud81xgfiI8s5NyeUgGqQrZNmk8BKxhuTflQE_0RIavvQas6oL97SvER4HNXeCxkuLRnqxx1uQm4R5nw0-uccsLHc2Jpjomrd7VvFED9sIr011hFEyu3PvQOXdTq07ZYx478w7yQoi7Lpf0VSuwhZvoTpaAOneTO1Iis05SsTmhUfsXXl4Z0E743piwHFg-j-_ZzNvtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFBFLjDVA00NL0PWEqgWD8WSvxncwR3jF-Ny5Imx3GRZMVUgoURrvP-XU6aaGA5l5WiZOfaeqS9aZyS6sYrKgFo6ij7bZ31g-iiTKHbfvVriBnJW2LRls2C6LGP97SkVfFeGyhcmcYYxLUZerQ0kzMXLsxeiD_vc6JoHeszMAk5Lv8pzslx5aiDgWlgGfXLh4RPYVaapiNy4UFDXLmNBlBD6yM6ad7GhmlC0aWSpNxNGgXL5ZTas3C_FPbABWqRWTNtJ-4yFkkzKQiElou3VKdl6MuSpSuoJW4d7QacF284-VnJlGcnuRgpGwSPfJi8JYGpDbhj0MC1KUVRjlYRwUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uV1BXR8nRND4-BtY-gdcxyI1jAN2HqkAwX_kM94GVVVS9BYiDEg4p3CDSobBka4erLDbqgJDL2fBtiFuXVUrybAv7j3JxFvALki0OTBJulK9UWkrYiPnBd9VqxVQH4udtf5ZovlV-FzdjuZg08gyyvrbBZluKhW9O73ogCScGpprU2OmWVrP8xZYdWevvXlgauRV_Nbb9D_maZwi8bVYN8wU2GaS3TLLWmxYoQ9x6jc68rrzakK2Hbcg6izZYSZvqgSgv6V4nh4MWcZAX0jWYogGqJOQY2lpK0iCV3MhzckCBcAJXPzcxAZtHnCKPHQfXTesLKmJZd-66v3w1bUODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcoj5l5x6VrUgjVlvdNbxIEftZ2lcd5PJZYY8LeBSqECZhDIxyv7ONqscSuPnkXfr9mO1UYVqKeEtGs__ERzCvAf-GZPv0_G5v9MVXOs2sl8YENOmii50NBcPRP2B5ixychOo-ziKaS8Q9nk_dhv3pPXgbxrB2sYWmxATY_02Um9Kqtf5mGSvP11kO6P0BP1uJY9eg5x6386PpZtbCQ3Yrq8klTNcC3yQDgRHrOTVsGqdRJR75aoCL5InBb8-HHI7MXRfH4z94emaj1EqxsIgwQTo4nYEXDR7T5DNmWyCI5N5iaZ8W72oMl1i3ZOjwxmcRzXcQbLb3x-OuerfVqCdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnUGP2iLacGg4mS7rehQK_aeHE6QvTDQsO9H1-heDo7B47C04710kR4huNNWNoOELShuDdfGuSV2xDJVfaVr8lSwq61HBeV4LHUFvlt3_WBZ4RqHZMamyGI8bitUxyisxo87IRVH0RJDov_B4oCdyBKIE-dkIVwKQGAKkgIGRPKCrD_EPlITu2yvjWfMQcdy4nZLolhFmh-5DJMWEvpw6Cgt9wjPU9uJ3nKNUSvvuspc2EXcraJvLZmobqD_KYnXrL3ubtjAFqSgNz6qCN0AHPJXO4Rh6Ay_ZFWcDkhuuNrX-xa-EO_GfQnEKCun72CEQc83qciileOGuWpfTt9pEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qt1EujpVqmPZhtds96-I3W4nLmkYUSXQQ-wGPYNVpy2VFeistTsZzJkwdXucT0bbLD5Yh3hsfnNvJ3msMl5DuIegqhL5Nh1xQhnw9dK6quwjPiL1aDp339ieXEcw9alA1RQ10P_xSoJomRWKrBYjYOX-pdxOfMBRkmSV2DvaAKZQleGXJdYogd6P98kcW4TAs-7lK4XII20Y4DViPq9FLKxdGudf06HR43aH3wqEbPg-YpvihlT-942VNr9ARuy6ey1HVKVEISJrEsZoWPC46JylyH0D4gQucHpII3K2smS-SAF12HFXBwcMeor6hebRoVbEoZ1e4vmp0AcB90Y2gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6cigNEhc6Gp3xZLF1h67O8Aoq58R_3m73btF3dduiMOouBdOuS6M503A5nQWB9fzu55e8Vm75QWlAnpyad879OB7yEOu1DTRWfdtmPnumT3BiQnIdsfMuNakepboBI1CXrLbjnmxLudNiPpgBbou11MPQkZkiFg2oSaeIscAIUuBRofyrKX2B2RvP0755bZ3-hDbV-lMoSGyL09sBrhJdLdAN9rJ5rF3sXFF6APzw31WeI5_cIpJ91_ah2aqcM6595-iYgAMORNVuTnRGok69Uy-agRvZqY1Cij4VoE2TtswMnjxFyytRj8hr3XtEKg5Q25XYLSSei3kFDgwx3AjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2uoaR1yqhC9OznHb1GTWkrbTTB9v3UcLxNgLDO1fQ0GDIUwZphnE71mH-Q3B1Ypd-rjpcwr0Z0myZ8lefWb1ithTBEG2xlBPKwliJJmehrpLKKlQzb5s8y7cTWSByHdE-aVojC14WbyoN4XsfECwcoP2GGuaaC4uiFl6PFUamrusGZFOjZN--0Qm59QjV6IRSZb2AG-Pjc8-hIJl1vTlxGLjuTJoeKKRlmc8DfliADpDl5zn_SxeMLbqBlojdQOviGsx49Ra-rq2cGBdLhAlo1KdrggRmIFP60tJZpOhDlIwFlZnKUQDJGA_xkC1rWK3yzUSL_g2zsLHvlqTG73rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgCzBYAtCgfnxaXzab0gQlV_m2EvElEesVIev_R5k86IRpEXOx3GiaLObAJ3_RgI2KUfoyr4DpOGNtoxi3NXVOmr2K1rv0buzQ4RSwqOluQXRSjof1k7SexINVu6W0ACZpC7mXWmrh3Y75dPxXwo9UBJJLDrdGUG9ZPqWbRSE3eICqOb62_nFfCDgkISKKnYiykYrHGuXILd4uOtzy8HI_2i7Okrr9T63ui9sPHDW8Z7wcXYdhfWgkPfyD-gcOjwcAPsbzt5MncRIBqPtEm9FY5zZNtp3hbX0kfiFVUe1g00SE51bUB-mnHV7n9luWqQlOYZ493fP_hR5TIdLOdJRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOyUfRmK_yjqZmP6EvaGChpI2uvIZcqphROD8KDtxNAznc-fS70EuFQ1OoUKdFFwzsH9-zgUfHRUWNR0LcrkFG-NbDgim826TgHV6gUDua9eRN9sL5BvMXvwo3UQgTJDGve2sGZCE889b8bEr2IjUzIUkJqnK7vGAzrtkWIr2NjBi36cmpnPdQoPb_aUk2nkOr2VZNGm7nSJGjto_LWK6KqJJcfhGvUk4HG0OKW_jbaAl4TZPnMqo0iz4WAZC8mL0VsjXlSNbhLQGDgpiISC_buAmg1h3rD_FRYNHOQmd34hKE4Rhz9AfQ0T4R-PA9h76ZIHDB4bUuqfo-PNd3F_ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3Ux0aH6JWE6vEiuGPPgZaVoUeM6g9_jKjcy_FscuTseE_dxfM99fpw26BcMheyVlswpxoH_ZJbB9ASdZJ4Zjl6G9xQNqGf59400wGUpSAOy0ipH3pR2tPu2oJVkDgywkOd3qTpRFcIRKJt378P8l1nflvoOfvdk73Zt8pLhWclZfcFgovIw_Z2Wb82IPE_bIAWrsXSCrw9MCYFX-D1SQyc6hR74YarGurZyOnh8Bxstinjm0I1hPvWqNGVAbabgyco71FOIPnjoEYCn4nt5ZeBsvXIIT_Cq70sp12kNomySOktJoNpo5vnu85y-CifTiqbL7M26fCPSNLanA9P2sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVJW6EYHIKLeGaOEbMVe9uG_qWjGgqcl79wE8BXh0OhZm3j4_rH6K56TbE3JZmhBffhP0waI6km1266ESCLRYF9iRIy7qsyq_ABIdUdS5JV6k_l8IUNTKtyu-O8_phuZiRP-bG7yLqX-c1NSpbzBbPdKWcsO1TFuoJ2uNRHfSA5VaCTcE2Vsd0XDBTLrt3BT4hm9p7eWJPD4WLRIu9_0OoqQ4QVloOmu_UtsDsBKGpDbutkWcvMP_ViYzFkX2fRYYkzEamnxA9EL1ggVfGqsGJxR9TsYs-IRi4UODHQkXW5ySKP0OaLTtSWdYisaUBUZVknZ0ZYlCS1Q8v98bH-1jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIK9douNDC_-lxiLE7XB3J25E9GUm1tzxY1rTFzdbI85Oyb2dVR-9ZQ8m2aPCgqNNdFVrNdDAEsdiLXFR4zV2PFrJbKTolJHnzvWnbHw42XEHTPvYSnAXu9uSgcBV_dseomULQE-4uJ6O5LA58OTMvH3wq0-fGKRJodEYJ8b6n5ho8IS2x67VdERH3RutsxglTCLKIuHxf7LS0eqHsIyGaxMuimRIZZm8bZZwnySvAcl2qQE5Z_bl4JpaSkDGa0DwzdW-p1rFAz25lXhV8kZ1PzLulDKd-IGmWJ8z-z4-lQ1vGYqKOQ8aCzidZAK5FGP9h4hiTef9TR9G90YXhvkAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-Z4a85XH8JgEGWbW8b4hS7EDSB1V7-16sI_jHmpMFN1Zdn4ZcOmyKPM7VS9LFdTyMLyJawGQAjHT5SnoOrib4WFWTtgwDo0NsNod7A_0lWJh-9Gltna4YhQrgP53DVNwHwUTZ3NU3KhF1mCdlAqxjkxiFt8RUhB3RtTlbQrdhdswBR3d4aJ6ZCYWr8mmIp7ldKbRc39rfE05s5YLKu2uDTHxjD1hKEjOY8CegkrEyw7kU_s_2NaYasiLUqqDB5BXeQGZbaiuFkRZil-UEQ7LW5ryFnuaUk3FH6vx1G-smufeEjV1wAPfYu7tqUhg-qAjTX8YGnP6LbTH7tOyXr11g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hv5zJWBB19LzZcuTVq4aq1zRrLDY7DgD26xkU4--oTT3ANJ81H0N-IPg8pZ0QY4YROvd3e5mb7BX7u7bKXc_CekWAnbvwLFDpfh4dTPRtTouXuZ4X4Cb-bYVcQ0rYvXq5tF6IbLRlWcwUAD_b_W61OxPjLyO_ncqN5ByreLGZRZrHDwKGikxBLgiGkyxu_XSndYTJm2JdShEf1c3kT5rD2o-bn78MxeEvVCzpVP1KmQ4V1cDEDpYzW1Fn9kxHWG0EJVTTnWzz3y0jIblQWbuHnrx94-sWjNmvFLegf1ei6_b4rRWoVg5fW3bgh5iP3ml0e4b5sQMBpW2djy_lHiCeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-CiH7WZtbkhVyD8FM61zRJ2qa6X4n6UYA-v3j0Sj9hfft341p5CC7b-DXLpHjOh0PkAzKGCLSM39zMpV4ZObr91qah9TPd0g75FvCk9vGE8dqo6GNqH-Wc5PfwAW4AV9ZgRgNs1wEnfuDWmGfb1bN0REierSVcDF-nEA5K14bMLwKcyajmhDeI88MOMh_VNoBQ84v1m1d2zTKvezKFJ9mwvVGuywLL_kUGCu3-CfBMXg9hVUnB9fT69tdmp1ilnaBzVNZLLqO_Peyy62Ddmq4iJXuOzJsQyK2nVrH4TsETUDTXNL0YYyA9ONjZXuurVHbADkcmIIR4SgEBaoB9uCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbEr8WEfkG7iziB4kRA351ExLY2asTYTxbgPSa0NBRgF6qGu48SCatpX9jUbs0yDnvbOT3bziyB3rittNbCSNcK4HK9DetAaaJCbWF356G5rfDbz-M9QiAcC4d0RW_dAOfHkHfxokGr5IVZ3pPPTthjh0ZuWJZpHlMYYn0Sv0l0rRPxe4OTXBJ90WfsaKTrMsrCZSC6ydKQ51cfitHn6pRWXh3zIT2_VDuimKN2voTDnFAaVZm6hZGn5Vqea9b8GLU_DkRboYQ9La3iDz-zoJKAXRB6XsztPPo4Z_UVgFlwH1IoUux15qKbG4V6uTvOMiOFTva_XSmHkulluK7NWUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=oUCMK7Deu5Y0W6WSwvwyZdy9H_vCMC1qazNR5uolkj7VJwKLjqmd6KdM1oADZ8a8-rpMJPmP5jIrFgIHVlr1P6WE28Cg8w1dTWigN3OcmdyhbludikgpnWj7K7_B8eAiKvj3kUcDkgWfW6XA2sjjnRtyQrzCRVWkRcILq0HD_nSrXaeJYK5d0lxnNnqarSULN8IDwkVhLPwiI4mKEhzh4cO0g0S6ALrYzgCCjGg7M5RoQUDSvENWiMMOmltStYqFIaSvJ3L-j4FHsYdoQ6TOK-7IqoaRnnkq9a9HfcOirIG-EHBumnDB1_i0bCkVmcm_mrtuZlTCy0-xB0rmK0BOAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=oUCMK7Deu5Y0W6WSwvwyZdy9H_vCMC1qazNR5uolkj7VJwKLjqmd6KdM1oADZ8a8-rpMJPmP5jIrFgIHVlr1P6WE28Cg8w1dTWigN3OcmdyhbludikgpnWj7K7_B8eAiKvj3kUcDkgWfW6XA2sjjnRtyQrzCRVWkRcILq0HD_nSrXaeJYK5d0lxnNnqarSULN8IDwkVhLPwiI4mKEhzh4cO0g0S6ALrYzgCCjGg7M5RoQUDSvENWiMMOmltStYqFIaSvJ3L-j4FHsYdoQ6TOK-7IqoaRnnkq9a9HfcOirIG-EHBumnDB1_i0bCkVmcm_mrtuZlTCy0-xB0rmK0BOAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ-gDRkIG6-Z2JLuYpEc9OfRkKz5caiqZ0Z8fAijLRcZnNdH8v7LsSAbPGn_oqPNXd-Jt7zgiinXsNeT00LjwUYwGxFLmTVTYhIMV07w7nszFmsf2l9zAa2xFSZAid1FxbfPBU7CDE4MZSMX_CzO-9t3Ts_IC9Dv0gPd_GMz_bkZBBg3UY6IOZFmO6hvW8u-CtDKzKcJTl1Ooe_uAiZ5Bijk4e9J-Uzi2hL4Jgi3rbXdF4cUjD5amzV0CQ0bAJ9K4kTltto0_HQYzDbUIvngvbuSHsPahvr5ghDlg7FU1wvVnoMfCnR911-rjM5i1FsSuMrUvp0oRobNY8OLEr1Evg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFV7Gx0hIwwUOd01xaIKHUFbnhDcUI5V-qApevhkqcknIrFj9ZKXBFTGFogUHCbMTiEwt8ZHhcAZqZ3NXRvvzkH1HOPJGO2RzCnCArKBI9BofNW-rR324G_w-A8aVJ8zchtx7PCKsISAwapR_xKmXAQsTXppEJ3XmOE2RxaHoEOau3ZLacf0WuMOLYvwBuxPGA1tzOWdtoLSK_l8xb3_ZyyYeR83jzdacjH1RYmWnEKI0Ue7StFmdrnBdNe6VyTNq_ucoD7Y5_sqsbR4yHVjP0cxirkwt2RZmOvD1exocwPTLeP7qokGakpjIYSOhjTiFoClMkF3gYfc8B_lPCaahtX0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFV7Gx0hIwwUOd01xaIKHUFbnhDcUI5V-qApevhkqcknIrFj9ZKXBFTGFogUHCbMTiEwt8ZHhcAZqZ3NXRvvzkH1HOPJGO2RzCnCArKBI9BofNW-rR324G_w-A8aVJ8zchtx7PCKsISAwapR_xKmXAQsTXppEJ3XmOE2RxaHoEOau3ZLacf0WuMOLYvwBuxPGA1tzOWdtoLSK_l8xb3_ZyyYeR83jzdacjH1RYmWnEKI0Ue7StFmdrnBdNe6VyTNq_ucoD7Y5_sqsbR4yHVjP0cxirkwt2RZmOvD1exocwPTLeP7qokGakpjIYSOhjTiFoClMkF3gYfc8B_lPCaahtX0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6CXvr8V1pobHLyqI5g42zFHyNy7adeNjCqG5rKUmmNQCqPdwQ6h1Nm6GAx07TKRkINUEJE9eKQPUSDl7fy_MD4E4Yo3l_ilguVftS8VO6crOsr2YIWgYH1lncUYHo_63vExzzl0g36VPwXPqeLOi6-Ymks2RPLEktuAzSpUAqn33v5iXfwCjSr_JjcHz4CumSaMf9vdIlFvbgAeRvsUtO1vxaJNIQJjk3HXl_U0vk8AvLLJTITiTe2F1EA50gotDkFMe0NBq-rCZzOTC1j4D3sBmjixIcnDN9bgmz08OGEDeb7GLOGaIGc25Zqf20zoFcF8Qy-pJko-DorIKdaLcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و سپاهان در سطح دوم رقابت‌های لیگ قهرمانان آسیا حضور پیدا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dqd99gCWMoDYEJ9MkHO1TZ3KVdcx6D6CEDPn0Y0nd2BCbtaHb3LjjZ9ic715LcfJw9cfLh_OGaRZLraUDwDd-wbr7xUn6vs6ZojRX80SB11IMRDfZzaB9BK89qOqWL6zSDioYaSBxhUHP_nFI0h4EaqJyZPIQMsiF8rHhicUtf0GLmCax5GQyb2jzY4vWEj6h7OB2MrfJEBiQpEEB85Y5Uy_jUlF60nyCQKPV4X7AkDrKeOpS7ABSA8sUpXmUlKm6rSzf5WMH7E2VcOEhuGinsbmBoZ43eLLCjfO7rmQLwTyl9BHln_4GNMMgeQFhJRowDgKNW8zwr-zfNGZm9oo7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiMFJmAoYQ8ngKvEWC29jcOYkBbEEUP5UM1ZSxY9Wfun_XpUtF0zuDRRoXk6B-InJqOguexiPMOkpmdwSlvJEonpxcKtEDi4nvL2uljxr5xn4R9T-1r6Udm_AuP6E-eMdfku4pJ4AN36Uq-XDBDxy4oDGNu79j9uFQ6wwBISM2AKxWVfC3jqW4_aUxJ-cmCHlW4J1xA7wEj-1As98LefOPXaj81-oXwc4F6o8iL9f8TYBQ8E0CsqTKTV3NH5q8Hb9zLZ-T-iwIWsNIteOTpOWaYeK2XaIYLL5b5hPcGXPB3WyXcb_i3S081bfJslXp_hcEYtdNXSoiLHXWmU1VMI4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDyVhJje-dGqz4NsEIGjOr4CGCcjjSw_e1bArT95D4quf4Yys09e8ANTUiB1wcDl0ZN58PSXIpqO2r3UrTkRMgjHfLQsB2wfS1Wbxy3-LdCSDt2uYwDYZmuLerLmaXFXnuFTO1beWtP7jVqujbMb0d2j6FVZjm2qndX5uSTQSaJaLbZD89rcd2pfFeSDeXhJll-92KGKCK3LGcYLAKsyXvr9h_EkgDOh7Za9GMaL1JXF0dDBcU_As1PBLkWl2JECX_oRRRoW_2hokBQWCktuTSh2rJrYLP_mcmqUEEi4HegDPr-FBWDyXug6isfjACJgNMgHNIptyX6AygXRXCRnPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtMjQsHxr9Pifh6U81y-tkRZBayUGkQhS9Xrb_W5NS1DBF3kHHB_w6gk_A9S54n9PTNqQjW5egfS4RkLeB1dAcU0YrlC-V8bC1zwPYUc-tvwRxkTjnKh9eY497sM6l0GG9YVMWt3oEEeOAIifiVzVdp-JAR_tfyIIVsA9S0lM7PIkA6FJRM48ndNUffKKuuH8SkUjm8cFohP2WIzGy_Qylg5q46YzbLbZkFk526-PyjtJvpP3A1pjLG4GU-A1jh_W5QNIg69yhzftyLXa0zCT3rJQEYh1DtivUI_DZVVP0dShgGOb-rYcsfsRJZ8CQzm3moUgvMssxj-No6r7gFaxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeRSDsGU_R0upP66vKShwn-IE9KwdHTuzUeIibRlIVmK3yzv92yHIVKOC-JMqx5uEFFYdD8Fb0ztrPj0hsyLVmEp05cf-VQOzkuYiLlkbyTfrPzugyCgxe_FsLC0MM_PaI2I7xjMtP3HcmNBK7sg5Lmvgd_J6LhZPJnjbWUl9yz9_rrAQ__-XU99ZWvwECTVf68ZvE05tflYGSlibyLDcl_2ZK2m3_nOQFl7XUIlq-G2Ec3wr_XeDZuSH29RY1juA7u1hJBl06xmdshMSehaY3amcQ3Q4FIvTf0EPtuUzXQh4MXPO7KmT4qSTBy3gJm0nX9gnaDy9KmjgPaQMo8aDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btQnlv69rWr163xYEbkNUzUK9P64BFy0uGaOcrfoJJ_qWIwB1tvGkvQA2LYZeNjxEKcyM4lhb00OC0Rsi_CF1z6CfjE_1yA_TTlM5eBvsLdOlRf4sBKknJDW8aswa6zJWj5M0VqlaSP_3WDi5aF3_g39YFkGElrAy1hL1_29vI_L7GBolaWSVezYfn__BRnldkOgLlsJVPMBbVVbpfQPf3e-aJS66USHoZDNlRXtX_LwbHGBf7y2kWbZYctjVJ5rEuys1ITQRPeCNo9hDVDNc5eTBB4ZhuDr-6DyjsuLkr86Kevz7KFjJw8GPftFqTzKnJOKOlapd8RavVq_ruEhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6bD4v3Mkv3FWxtyk3UO3KeoYmUmHJtGZmyXxTkYhP3IBFkmbggFjj45S4jGT15LvUnZq6vkw7syzfLZ_xuR5QdmTP84PA6cyIBeFh4bN6L0dn1VbDYLUcnJS95Am5KtcDsHCjA-FWDXJ-eNzOlRao2iS1VYAes2sphlyku4nm1g0IeUKwsVE_mbI80yrHpC_sW2KUXcLeJL5RlW7NO2462IjgsEvnjxTT4DKGG4c0Vctc_InbzX90EsVFbRYffqEuDCYYLw9HZXSQghDyJ2nTKmdzcTx8kIpgyWdUvQxJfQd2VNnGQKwQ-idkvYD1h0Te-PlLN8yDaTb8iJid6gmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BgmB8YRx_SYarRmDffsSyAoWpdYRUMGmm2OYwpavWgWSedF89MyHcMObGB-hBS41OJUD6Zk8DtCQZDqreq818tKxXAAt6MNT9ty14RyssDtD08FCODwsv5X_irotXi-fgoS00a9sOxyTKsiFubQKXHntgGJmrFqncMQ3EfUmUgkvDpWemT3b9cGYbKOwdjch8Tx-8jnk6jdzvRLWnZ_eqWVNgWAJlVykBjfCK7KXTUUlqXjNfOXAhuJhQ31r2HtBeTHdk-aQyWqzorBJGCZ7JLsbLwJ6ZQqqdXQ1Ux0pOGWml8kG_Zn-uR8x8DtgghNWp4QUFKZw9HKrcVLbQ8_Vaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWNFDbURWWB2MaWdV0pwatOlldhxLh2VasKqlHv1PdjiaKV4QqlxyqhwX9Rdv-lYeYb0C6ZvsIs21_6mkFndCJevj9bfCdp_9cNwAfMRqOyQmzqtDPqAR7t7JJm580egZVuwCbp522HPPn9L9LpgEzuSN3VxrCIKc-X0eTlOpIC_CatfbyIGde3JY-9dcx6gjLxCkrz2e6IB0bBNO4XzY6GkqVfCpRkQ2ZbtnlLxss4no0RaRqmiMTeag0OPVOGtyGV6CdhI6wvtE7Q39TKmIJ9_GbVnwAv9lljSha_riWOZ9hZK9rtAa2OYBKQMZ4hDKd3VGevlY2WcRnzk0nz8FQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXAfcyTqwpWx3sHK9-CZrugBltPfk0HtVHdz-1OeU2haIl6Es5F38Llb6GxXda8v6d7RI_E9myYpKJybS7tjHakyTtmdplMGSFwJViIEkBfBwSRyk9NgnwhuM65fvit86gGPbsy_6GlwE4Mv-LwLgjxsJSQBQQ0tiRX27i0gSMErzw0xbGH_Oo9fm3csrTNLvynmxXC7s9VEw-0ecGaeoD9owbxo_1ZAxqU7VR1D21S5TRoKRHRbvm9esKDgAe5hiDRp_jU8D_CO4kvTKIWaHIQl6zBnXq9t-13WPnjvPjx2t9fB04-jmb_fGKMLjn6PCIlWNA7xMX07_UoWGruv3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=Jcu9K_4pxRGfM4DpbQ3y77Hb9Xea_pT9MkJYxtijwwrcV0RlxwzF0oPgAL8bCAEzU9fn-6TpAgv5mZkZu3CfCJhZeuTTQKXrHLajfAdgXHXGNU3HpwYXpvN7wpyYkJeyss98CIZyQDV6T2H3Gq81ZIxKEkuPS_dhAsFFLhh565Qng8i_NrFO8zg4i2w6IfiaY9A1VhAhptQrsmz4kCpjAS3ghv2gHx2PfmJVXlcGEt1QUI7TqY_MYOMDPmg9w15h3KM-gFUMNpjmW2KRrVEwrA3hjjiLdC7aPV-SS2CluFB7TzKfkeuNJs4Ex402aJ3ygvAslqtBrUlHxasXVq3xHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=Jcu9K_4pxRGfM4DpbQ3y77Hb9Xea_pT9MkJYxtijwwrcV0RlxwzF0oPgAL8bCAEzU9fn-6TpAgv5mZkZu3CfCJhZeuTTQKXrHLajfAdgXHXGNU3HpwYXpvN7wpyYkJeyss98CIZyQDV6T2H3Gq81ZIxKEkuPS_dhAsFFLhh565Qng8i_NrFO8zg4i2w6IfiaY9A1VhAhptQrsmz4kCpjAS3ghv2gHx2PfmJVXlcGEt1QUI7TqY_MYOMDPmg9w15h3KM-gFUMNpjmW2KRrVEwrA3hjjiLdC7aPV-SS2CluFB7TzKfkeuNJs4Ex402aJ3ygvAslqtBrUlHxasXVq3xHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtNvCjrT5HXrSxP5XaCm0BOOf8itOyGArbBjIJgIsU-cp0HMpagUirMKmEQCLugVwdtMHr5s5UuM7Cl6bZs-VMVnw_BPjAJQdj1vCZF4LioRsd-ORkZR1br-pYo5tLrRnci1a0NCy8SJybRHiLlzTM0J9Q_Wlf1aKetJ9gqX9C1ZH9z9d9bN5ySCE8qdgTZ3hj8Nruez3kfabrxeSXj_06mwdvWeQXliYF6JHSgXgOquj9ogVPhJNVTcwZpdZRX6cpbuJCgIfj-S9-POdG3W0R3zIU1zB1MP0urjKY61LfNcit-gFhaPL0mNnOXVKUqAqVwSZr1TcU22ZqNYL-rUrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvJacusEVTyN52a4lfBYQzF0oz-tazVykyAH6evkYpdQ-4o6dXpCRZ4Le_uBaaQV0jVGISdLFMyya-Me-Pi2dGc-S44ayY49qtZk7YcIxJjdzoGcuZoAtrH0Js4JwhjiLjSAB8xpdeTTWrK3ld2-XeaW65ARCRaDL1l8iqzHO1jvSP08J2H9QdnMC1lDvZ2rHPNICJa_yWkGrz_CWyO28L4L502CovBo-nFm2Y5Nrsokwo3UtfBtWjzJuLTc0_ItPxTBD5a5niuiro3_yxkFfP0G0VGFK9sB1B-G6E9qouDTwwOm78zXUY4cRJM7PGizKEbU6yHuvxuaQmFOKF9QpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_k78yKqgybbcC7-mxHEnPLkRCmv7MOfrNGO-mt8flGPX_krcmzbOyKg5cKGi9G5j03RxHuETW4PZPR-jtuhK8SN8IqXWtq2YzQyLDOKvFXqIyWNyCMQud7UgG8yq5n4ZsJ3SChZvvzElZM5lhXfpQtpZe7l7QBhqmTXd0E7m_M0OJNCIMpHSsw58Dfb2XsrSJLJm2twgiIhxUh_1JiJSz4UEczm4JgHCZU8f2LoGgb1zyQ8ScUJ0xlLOf4hw8kDTEdiLMf7-N9OLPep1EQ4ge0ttyXWMBZUbISs5i3YRRccSbJvoqBdb3VHHVoxtz-r0U_3GAlOZn92z9ueQHFzDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛
رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22050" target="_blank">📅 12:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22049">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQRnab1D0V3Jx6dXQtSWbtpDT-n9zo1vz1jDmQCx9zvb8BilLWf3YAKOlKk8tHYHnRItR2qoisQc9rvadgqqBgJd3zj7ytwndytJrA4Xljxt90sabYfauGMak0mTA3qxdn7R9to6RFCvZ1UA8GtjZ-gR2TxNdEAonEkP0NjRTuPt3Q7oAM9LALMKOyLTGNw-Os4MwXCI9LgV2010RQJqY7O18I4OZW8opT--E5anc8S1pwhbmjWu6zOVIMg0iM8B68z1rtlrZXWdg7nOzHpn_HkfgGPbnT92ko-IbyC37-Osif1zHcw7RVT41-MNjWI70oKzfpFB8b2Zv3J-TRFtRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcHIcBBowi2ExFptUsV_Z43Bp9sNvhuLphLqzLdpYDZzZQ5vkmBoy2EMTbXgkZHEw8nipyPc3gjtg4hGIX4OMNjLQXdBkBYSssPKlxXawZFVnLo4MGAZ1dbdFEuJGtRfZC2n6OdIjAuM6SBaAYwwhPmaKK5N1-kZ8j3W5rbBlFYVWSUDVmL1QmzHT5TgslYN4dGICMSHGBLbYpSo4jeTlq1KJlHvVwm9upPwaTbDvAU8wE-HraXHBBjAfy1BIwgmZ3EXf2Uy_y3UamNq13SGIvdP7IAydFg4gtQ7wvNKQb0DwthBy0yQFsa6nj-rNeCPoIfP5zYi4CY0uZEqoOkAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccA6kN9az44ZE2amvBc2OwmMt4Yk40AX2UM-1qUkWTiDBsARxsdCyh6OF5-fS6BaZk9UKy9E3ajr4PlHejlWbgA0sqi0jYLcVviPfz_eH1gFUfaqccQgKQ16Jd9A277uEWgHVC1IF9_kSqlagjSiHWhN7WpAzNzyjtl0ZTvmgrGaB-6jLD2wNGv7_uLDe7eSUAiv3qhN1wy0IdrQhKmMa84qTLj0F-8WgZJ2IbOzx_1rzt4LkVipB4iSXS8mifSjWecOGEF1iyMF8o0rO_I5xsOuC6D777cNo1wlvgJ0smbKe6pBPKONO39kj0hjpqTILlp7a4ZpjwhayKMzDH_82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-S77-RZu3CQlUHOy3HLvL5VJaGTAvBfKH3iJ7Rcjh-zuUAoMMUrKhacl8Cystdpfooy0abHRdRqlYhLikrtlxHLI_XLqQFAOBSu2VSLACe3rUd4PGVO-vxpWaoUDaOrDJvBKMGrXAfYu85cjid7Q5VmfoufdZlqr5VkfpUnG9a2QI4d8Y7U_SzJSskr6qI02YOFgUuhvAdTGyRu8Qystcag8w9Zk4eBOEf2Jet_a20wdl2Uu7ZbvG1ascmzEYQMQbsLbvvhr0PfoE47_UyGiRECepCNAihbVfH4w20HZVYzOtuMcd0rre2SPVvv6gNSGgEgu9nE6cACVSvJPdOQJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
طبق شنیده های رسانه پرشیانا؛ ایجنت‌ خارجی‌های باشگاه‌استقلال به علی تاجرنیا قول داده که تمامی هماهنگی های لازم رو با این بازیکنان انجام داده و درصورت‌وقوع جنگ‌این‌بازیکنان باآبی‌ها فسخ نمیکنند. ایجنت آنتونیوآدان،ماشاریپوف، آشورماتف، یاسر آسانی، داکنز نازون…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/22046" target="_blank">📅 12:06 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22045">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=I9lkkPzxhg6Cx85N_crMnuEJiXFTBM0nD00FenQVTYSMPRTt99tLaCFzu7zWWAzS9G0kgxfzfljf1PH-oCXL_AiVNk_eitTWXywbZUkPbQHgDwKIs3lc2XjzggGqLyuAQ-JqLKAQyu0USC8MYMomBjhjlPKCy6V3HOFU2aTHEGiBywDspfBF7f4e7IPxJT2SNB4AZQZEKmXvh-SBgIBWMBOBSiZoT5Mn5UmuJNk14U2SpTy22m1MazOgSb27N-pT08RFSzF02uCJb0DEulKdFOEqL23LTfco7TDcLkvjzlSZR5a0y_VG9PylDiYuZl-KSoaT-M-ylJuWo_kps3i8Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=I9lkkPzxhg6Cx85N_crMnuEJiXFTBM0nD00FenQVTYSMPRTt99tLaCFzu7zWWAzS9G0kgxfzfljf1PH-oCXL_AiVNk_eitTWXywbZUkPbQHgDwKIs3lc2XjzggGqLyuAQ-JqLKAQyu0USC8MYMomBjhjlPKCy6V3HOFU2aTHEGiBywDspfBF7f4e7IPxJT2SNB4AZQZEKmXvh-SBgIBWMBOBSiZoT5Mn5UmuJNk14U2SpTy22m1MazOgSb27N-pT08RFSzF02uCJb0DEulKdFOEqL23LTfco7TDcLkvjzlSZR5a0y_VG9PylDiYuZl-KSoaT-M-ylJuWo_kps3i8Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله موحد اسطوره‌تاریخی و بی‌بدیل‌کشتی ایران متاسفانه چشم از جهان بست و به رحمت خدا رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/22045" target="_blank">📅 12:55 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=GBvLSBYm6J9-ZFqCzA9EawFexbwN80UBhHvhf_EqXsJJ9VaW0yXFHuUp_XsYa1SwPoWLuMO-F67AJsUcDW-87xzE1ZqhzhDePYR6ZqMectYFSbY89lscw9WEFnYgJcr9ulJTmHVhw7AlGRaKkRP5nzT9ItZhbmDOa43B7C1OVt9nLkMAtRThl-cx-GeZMxl6fBa_EMGniMvB7LZwM83FInMxSTE8N8Ol5Mte9OHyzx9ZwPdBni0cpZm1-Gw1XQ2_yRU9BNTsPfFMnWRVoexa7B_8purd-z9AzGRQ7C6uZkmqXldeTuNBLgxua9tyhagT-FT9QacbOGZAT-sF8GS0nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=GBvLSBYm6J9-ZFqCzA9EawFexbwN80UBhHvhf_EqXsJJ9VaW0yXFHuUp_XsYa1SwPoWLuMO-F67AJsUcDW-87xzE1ZqhzhDePYR6ZqMectYFSbY89lscw9WEFnYgJcr9ulJTmHVhw7AlGRaKkRP5nzT9ItZhbmDOa43B7C1OVt9nLkMAtRThl-cx-GeZMxl6fBa_EMGniMvB7LZwM83FInMxSTE8N8Ol5Mte9OHyzx9ZwPdBni0cpZm1-Gw1XQ2_yRU9BNTsPfFMnWRVoexa7B_8purd-z9AzGRQ7C6uZkmqXldeTuNBLgxua9tyhagT-FT9QacbOGZAT-sF8GS0nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوال عجیب خبرنگار:
اگه تیم جمهوری اسلامی قهرمان جام‌جهانی‌بشه‌چه‌اتفاقی خواهد افتاد؟ دونالد ترامپ: اگه قهرمان بشن باید نگران این موضوع بود. احتمالا تیم‌خوبی‌دارن. تیمشون خوبه؟ نظر تو چیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/persiana_Soccer/22044" target="_blank">📅 12:52 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22043">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2kcKy1juZjyJ_dhJTJ-ZU3BKMdQLZC6H404WWbhvoW7UgTcBpCD55XSVJM47gmrS06NEcv9zQ8aojpJ7l5dmpDlY9714z7s3a5_Ktt6OXacnBHe_pq5elRHbRT95-GiPZdc9E2vkPLlIBmtvemCzyDkLu-jAysom8ZPOA8vZqJBwmM0POv2wfFW-9TBi47l9ejn_GWT7NeQBKhrzRr57hEIIE9MylupFsEXRxD6ihtAoj8-BudLe9HWf9CvL9WDuRUpkqh9PXEU2LAXvuNb3sFQFgVOowv2iU2cLA0YrlOScvWBaqh2skZ2s__1jZa2ZRIlebEStXIrQOjytY9DYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/22043" target="_blank">📅 21:22 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOpoloTjuuNa7wwBuscF0wgherQTMjoUDDtsu4yLYIVlH6_H7r9DjggjjJxfsmQ03YFKI9ymIY7mRveINDe7zKtFreZ3mT_fezkUVP_A-uSyNQ_vufwgqQknCk04bMo27SoqPl28KEMA6ZhuUebly7qIPw1WOy2QL1KflwjnlZwwW9I2V_y5ezXe1BLAiZeDBG6FIq_8iXvb8Fm5APDXNYQB301fxUWimk8WAEeYygWCHbRlMnhuk6KWEdfxNryrl4nsThiGm18tpIUP3MKKr305XHwJFQScFeYo_cvRyOifAvqyGvtiUPhV9YklZVpHWbd02NWZJBdP6VCjuiVgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/22041" target="_blank">📅 21:17 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3yBnpfpY5IZQUuRXWsL1p3LssoG3urrlYJhU3F4TGRjFlaeNfR7gI_Db2WhGgNh5mS8aQTpi5js4cUq-V6xCKf5HA9KUesgxAnPKuRFYUHxZcG1qTuPFAQtS5px3GXVfJSnsULfelPdY6_HQ0WyTHIGyGa40LsWzVmLCtQwbO644MIf0wnBl9tJoKBlNSuwjdCt3KpUWjWaGmCMK7OSoFyvrxGsUFkB8kJsOROERyfbwPK_Lg0sgtWJVugaifPUGvFPeKt5wGQFIcC98bPOxJedu1mmuSaOajl3zxAFpm7MnVIgKBGGpwBvRaZbf-IQVBOkLePWxCR-Zwbn5rxMpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلیس‌کانادا از ورود مهدی‌تاج‌وهمراهانش به خاک این کشور جلوگیری کرد و آنها کانادا را ترک کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/22040" target="_blank">📅 21:14 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22037">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlniEHWQAfMlFjVkP7rv7j3WlX730qSDoTie9D6qWEgladM70aahtGHy7tPEeVdG2faQNAq_v4DMpMQCq_ARbR_Bs6lI-sEqm8r4RuVRc15Q1CvAZHcJhwAQqS6LSVBhmtQer3Cga5DM6_bEEcZC80n__-1ldSHN2DeoSwAuvYiwdzMQdnwZjXYSDagAkKDGDT9zTOYeGPdNn--b1NKtAGn8sjU9TicL9SHUPxtB8pOfTJeAuglTAODeYxQ52lRrzeUzoQqWnTOYbb_gtPSO65iDQjckBjcogb99WFbN72FCXzTU6dCcOqnMWR69stLg87TsujBzSKxzisTAvWNnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تاج رئیس فدراسیون‌فوتبال:
اگه لیگ برتر برگزار نشود استقلال رو بعنوان‌قهرمان لیگ برتر در این فصل به کنفدراسیون فوتبال آسیا معرفی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22037" target="_blank">📅 11:35 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22036">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d28iv8z5aCdv1ZacOBxp_00JAmOPDMVEWoxIKld7a53XCrfurHspNVhYducz5XhEZTfYXYMyCq-yrQtM6OAGmPwSwchzTj7R6-zUHN0m_0M1zKZA4gHKeKWgqT-Mn6gV_wxs-7gp1AZo-rsz5FYY_62B9WEl7-AUSMYq4li7K-nPktb8q23-Xy5BEJm7QqckP7CRpc0Y-cNOZ_guJuJweskjyz7yTFP2X-ehc9OYY2vBfQ7HhxdfHePdFnlR_t7PaB9CVkIOeeFxzl4oYiGWvefvRHtVJZFvklyoCyxe9gtbA0SsyYuGCrFtbyMbBvqsW4rWXeLPanOIFzunvdaZew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجمین‌حضورکارلوس درآوردگاه بزرگ!
کی‌روش با غنا در جام جهانی؛ کارلوس‌کی‌روش بعنوان سرمربی جدید تیم ملی غنا انتخاب شد تا برای پنجمین بار متوالی حضور در جام جهانی را تجربه کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/22036" target="_blank">📅 11:27 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22035">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGQcc7WzvMXINb3VmXWXcW1OwVoEhFXLZDE7SukG2NCa_YGh64bZfufZKXAXO5HegfNuLO6rMQV5ODV1l3yLYrzSQzHhzXmJ83m4sStLDrR8S-LTFLXvw9o16dX9dc3g8RgxE7BwUd7sY9e11_ft9OmInJuwr_87wsAm0rw41Cb93wpb72EoTu6NARWAYq3Sz42W_12iREw4EBM7shCPYchwaABLdX0-4JqVGvgWNjC0r15uhGhAHIbRDkPJttqm_n2ohjLnK6HPErO-UDohQGUBTc_hsTU8Doqx-FPY_bGuCsOY1zvKPjdT-mqClkMa3uekaY6vRcazdTSUI003Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌انتخاب‌مارکت؛ 10 مهاجم‌گران‌قیمت دنیای فوتبال
حضور 5 بازیکن فرانسوی در لیست 10 نفره نشان از خوشبختی دیدیه دشان در جام‌جهانی پیش‌رو دارد!‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/22035" target="_blank">📅 11:11 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22034">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=vSmj1Fw_-4fURiRZfdQUxnWQ3vT0sOfIGbCaqYzB0hjSQnPtRMt5a5ss1PjwJp5OZ5kDyARmbW3eUKWnBOpif49PGSezDjlvW3cilpFtcZSvexwMkv74BvxoVAyxHzxKReHSrUwTP8tDBKtS1rLv3TGojmZ0Z-byn6S9ou4hsuNZ_6-dxLqKPgG7hbeZc9UCnR_nY232kpXl78xrZNdKxJwtxh9-6oXIm_6yDX3zjF8BInQbt3vkkEpDccRtipxcutw6EGqUAEbvXPFRe7Bkii_sGI_SYp5K8iCJQksMheviUFvuk7hsTf0HeyZPG-wK4nUNLnSt7insCEUao6UDMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=vSmj1Fw_-4fURiRZfdQUxnWQ3vT0sOfIGbCaqYzB0hjSQnPtRMt5a5ss1PjwJp5OZ5kDyARmbW3eUKWnBOpif49PGSezDjlvW3cilpFtcZSvexwMkv74BvxoVAyxHzxKReHSrUwTP8tDBKtS1rLv3TGojmZ0Z-byn6S9ou4hsuNZ_6-dxLqKPgG7hbeZc9UCnR_nY232kpXl78xrZNdKxJwtxh9-6oXIm_6yDX3zjF8BInQbt3vkkEpDccRtipxcutw6EGqUAEbvXPFRe7Bkii_sGI_SYp5K8iCJQksMheviUFvuk7hsTf0HeyZPG-wK4nUNLnSt7insCEUao6UDMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سوپرگل تماشایی در بازی دیشب لیگ‌مراکش که احتمالا برنده پوشکاش ۲۰۲۶ میشه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/22034" target="_blank">📅 09:07 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6XafgauEqBq-fGuqAHnNGgH3152PnMhQVTanwKM306dLi0R-a7zDG25vaM4YFhWhbIx6qUatotW67XOlzMRtVqF_EKcbVV7dSsBC_zrfjYIfQVt3UGoJvyameOB0cmWOTYQm7T-DyG_8VN0L6Puzk7dbQPUtwLnqbpjDZ2RtcnAgrISzZpLaPT3JPzMJm4E22_mwA4ezNU1DDPbPgWIrha_dmA6IO4HDL574_SosWezEhU1x_gliKAC8FwdLGeJTy5V2fEcriVIzYA_UD_Cd4IacJ1McisrA2L6xMKEHBIbAc7K0B3N62Y5_z935qcYzqR9ESktV76hbHc1FSiycQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتیجه‌دو مسابقه امشب ¼نهایی لیگ‌قهرمانان
🇩🇪
بایرن‌مونیخ
2️⃣
-
1️⃣
رئال‌مادرید
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
1️⃣
-
0️⃣
اسپورتینگ لیسبون
🇵🇹
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/22025" target="_blank">📅 00:31 · 19 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22024">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH5RW5tZZOg0Q4oLQAffZBvmjGV3ef7TEh597RXdL0ZOYL4cGeTjFxhBLbYNLalG62KCFOp1WU-AL7SDB_ESzuJqztvgh8sRQcBO1FPsxpE6v-40A2rHgN7lAHwNQzkaLVefz8DpV6rUmW_CajCgEMPgQ1VGTZY6xR4ojhOk8Z4YtXbP2jitBkKzDWoYtvCka8yQHFoihjfkZCReThpNikGFwwJvBv-8sXqrRiE8b3-aWWj19AafHLRzp57dn5yuiont2Pn94hmWy3uW6H-Fqw2u_NcWmVEwNx2TwemWI8WiC-AA8SBwqTdHt4a8rRfNkKNuwFHCkiloRR6H6xYe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چهار تیم‌ نهایی قاره‌ اروپا که امشب هم موفق به راه‌یابی به مسابقات جام‌جهانی شدند. ایتالیا هم برای سومین‌دوره متوالی از صعود بازموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/22024" target="_blank">📅 01:10 · 12 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MovZlmibzOsavnCce3W5ujP-1JhyXjUQKFRNow0Zt14Gkdep1RaAepXNp94H-su_G9LT4a0Zwvmk9nmLpIkc21g0VyWy91dlHgjzs48Pw6ZvEZ6ldMOd424_uGTM9sBKQuiGRqeRoZlwkUb1HumJbmcFMzgz7fS9MRiHcXD92Bu8u3g8YMYGkWXUHa3FeTVmeHh72k7hC6Guv4AB1SH0wBfYybgu_XShhu-XY79ggpj6rHofHNqyPdYI1g75DCXfOD3U86BqRdo9RaNo5V2dcxzG4v4LteqViwlRlOJZe-AcGVlx1ALjsDtU6vcY6S9igbywmx10sa6Mb9Y46h45hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏مثلث رجزخوان‌؛ یکی‌را ترامپ‌زد، یکی را نتانیاهو و آخری راشریکی‌زدند.‌عاقبت رجزخوانی بی‌پشتوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/22014" target="_blank">📅 10:29 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5bI9o1oyCDUrEk2fVGt5Prxm09Q_FQlvPr2dqQ_axfR3ZYLEITY-zhGoujqV_gf0anFbIeJer7PQrU3vAJ7bUtPSFWeKIyxPymYkvha0Ubc6ClTNr_fjR_r2WiDfcK00DuuGneAXouYneZKnAgvplhGqJq_dcrYj83wJ-mvotth68A1y7tXxJy-Ytdt7NDrdWkjEdRuvvJgkx8NJbIWujtmH4f9jnYcD7UTXfmPUpVo966M1im-WY_7IT_avzuusfYo5UICHgvwKSV3EfFVCll0DRUAON_tguFNuzo3stpO4AmoXaRf1SjitqUUyj93yGIynYAjYtEhZf7VMk2NmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22013" target="_blank">📅 01:26 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22012">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCbYNQwlCAetUUSMibnHMC9wtHjy7rX5rBomDCUn1GfN7vj-qEHenFtYLqbR4rwq2su05d_uLevviGDFmB9FZYvZTZQbaKmKNz57OY3vhb1_IR0lZElCnSYAcohe9VxwPKMmm-mCBS4sYmIuBbowVoThlV7rnCEhRuMphuz8bqEA6SRvttJZNZ3TCoQ7gSHojyUWskVU7_NP9SAEsK9n3Li0cb35Uu1rtYEeL00rIWR8QZeJxN18yoSflLq0wjf4bAzbyxO-MY3Q_fcFDyM02Rvh-HXefJSdhIPRrPEzoDXX7KD4N_gxxIqr_RxM_g-FXIOKcWPD6eNUNrcgXZhPEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید مارک لوین فرد نزدیک به ترامپ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/22012" target="_blank">📅 11:23 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWGlvx4NJcmz-J32JJxBKrRSoR0vRuEOKkRlMuhAtPLx_gPg8sZn71MRMv_8sBybFEMtkV7Oc-ep3BqvfaVoNeLvF9KsJC-zlT1d5PQYcl4rD8vDH1GpsAL3rd4uzOSikoKPtXYaLS2rdS76Bdd2sRDjuyv7AKl8jKq9NRbjfuVEwj6v4qbB7v_i2RoVWfuWaxEYKmsuF08PYw3snizEKqDgoJNHiGc8kWNJnfLxCFgkTQvlCsagUImvMY4dyQO4z06ov_L9KhMrr6lHYvt4G4KAiZtQg4bouO9GycykGpo0k3dW_iTN5U3xFA2BIZ9zeck1NbEWvz0tChQTbwozuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گابریل ژسوس مهاجم برزیلی آرسنال کل این زمانو صبرکرده‌بود که انتقام‌شو از موسکوئرا بگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22011" target="_blank">📅 10:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22010">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZy0iPH1CORJjnktdwXoSTbPC3iw9he1j0gJV2D37ELA57ftEyVbr9ao0jQtFtd25d_4s8bfNQ2KGzgE3sGWCIcv0akVslpGbW_lYOYtNBlu0_vGu8qtqUSr2Je_dZKolYNK-uzxFrkcbUKGl3G972I5I-g6hrbJAhFUB91gccZAEMgBO_A95UL_ETqeT3LEqal7rieJlHyxJvUNNcjdXMYU5RZlkaBusxSG5JCCGZTBp6yiXjeQ4Hjcu6nxp8MTh6ElNhn9Dv23pNhdJTKxbuRvH0H6gUeIlM9J2F_3XlPC3RHe4O7OO0nonCDggeinoMjuLlkMKRHmUEPoLO_WyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22010" target="_blank">📅 10:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22009">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_f274uAY11IW1x5mdwGi_6qMsBLVV0yh6ueTVIn6oz3qCl_Xf40SEV22yGgceeR399ovMtj8cSg7DaAu_l_808hU9G-rLbeXHd6DDA6HcN8F-JMeJjDya7tDyWIDIIhTsuSc1Sz7CzrmFFoNzm6sLeDpd_bo75AZ9J9IBkfvz3hcT0Bi5wq49eiR6uFbvesrm4ytnuaT-Ah_mn8SlOVzfv-6VtWxzEsiuL8leQ6eT8T3cFMjJLbCQ1_bpNcTE_mp259J7c6nUm2Zr8el5kpuP24G_L50iDLG_FJOx_cZZga9dC0-NjRXGB9Be7VP2NMQzNvAxZAPA8zyylFEcOLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
​​سال ۲۰۱۶
: رئال مادرید من سیتی رو حذف کرد.
🔵
​سال ۲۰۲۰
: من سیتی رئال مادرید رو حذف کرد.
🇪🇸
​سال ۲۰۲۲
: رئال مادرید من سیتی رو حذف کرد.
🔵
​سال ۲۰۲۳
: من سیتی رئال مادرید رو حذف کرد.
🇪🇸
​سال ۲۰۲۴
: رئال مادرید من سیتی رو حذف کرد.
🇪🇸
​سال ۲۰۲۵
: رئال مادرید من سیتی رو حذف کرد.
⁉️
​سال ۲۰۲۶
: نوبت سیتیزن‌ها یا هتریک رئالی‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22009" target="_blank">📅 09:55 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22008">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guEKBrI1sh8eJaHBXxzeuqNkfbX6pNLAQo1mylDjQ7mUPSba7MYsR7bZDhzCqAwOiVljHVyTs6GVSuNQH3qihEBRSmnL8BMsKH-r-NR1fQNjXH6PnygXenCx9LbZlgdUQi3OG81lyb6apQReROukhkY78ABzHnHN5FOp5kpeF3b6WGtKzvkO_E_X2wjzEYJu-HUiNo6eOgVn5C7ko-a72xIqFSKeCoQ1kyqq7xZKSEOPFa5ATcrwLSydw4DmtwzZpJdkRWRa8BPihpr9gcFaQ_vOjHJEcMq9bqG2zqwgNGG5t_B900DmnfBNZT9UF7MzkjJNEIdxCvkVfdtrp7n2uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22008" target="_blank">📅 09:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22007">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB3z6gRJwAsr8jCmK8nBy7pNcwJZEb6mN1n7PqMvwRMJi9eiqgC5gV_NoCJc-JeLQJZJ_GuAxICnZoaeXcwvSvZgB7AFQWBqptvADwYNucxWaMJykKNloW8G1N5GJSoOWZ3Y0y8anNdZWeXdCwkinz7zFlZ5umJLqRzt_NCq-8QXbZuyhAFsjZ1WmMnJ8GLqETXNtlwA5g7yuCusC7khAn2Iz1k9sGtKqaFj7BuK9TOoeax_TgfSiTWo7X7P9OU3cB1v_C11OQikggydWLEUl__S1eBAeZDL9G-rBlOQN4nipr4Z3QKUYIFySEDRmizZWenok70l2jOV8TKq_UwRiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرانکی دی‌یونگ کاپیتان هلندی بارسلونا به دلیل مصدومیت از ناحیه همسترینگ یک‌ماه دور از میادین خواهد بود. کیلیان‌امباپه ستاره فرانسوی رئال مادرید نیز به دلیل مصدومیت حدود 3 الی 4 هفته قادر به همراهی کهکشانی‌ها نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22007" target="_blank">📅 09:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22006">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=gXrJXfJmh0cbMIbbboeb7M9W3FqL_G7KtxL2hJm4L0qcgHWlt03kRvHWs74VoJTLEVISNZVOJfK2cXdEUEsy8EcJHdh0zHt0DfqZDboqb15MIDIBOIIF-rE4Wjk3WwLeOBbJVEAEgsWimoK03OEBhDwY1_7Tzv67h5wmh6V3y9Yv1wQkDbhLpQlFOpxpCvIa6YFxS_Se6F9lA1iv5HWlzrh3rRe3j5vlbxW4eGAOQqKY0WeQ0St6ZrF5H8OwqL3M9sB7n_m6VIo07NTXTuKgQA0bVBxQDIEU9WpmqnEmf1vcTH0AMlznL8tw8yg1L7d7LZvC0zTUy095kGStMT_xgW8-dyPq4g99pMZEwCmaDk5AT6nheZYlXTrNJo8eYDmaBNKIj0XvrKSjGXitaLZ8yrs5OFLodzmYhBwTfL8EkD4atxpXoKLECPz8-N-3Df5KADR2t8reADn3p3kVdDGmRqfe3_ybo2202vcB-drg_KsiWX948-2R68AsS1NHhCt7gCnnrpUZxQqSKf0Gp65ibEgbwoWRsOFDaHZNjnDdfa4DumU89q9_yLQE5Qz7uZSOcteOQGHDEbdsSDcW_ELjCLffrWEz5fTXTbMqMZPrcTelvAqO9-v9BT6A5PgczuBEEaizCXagRJlcjIge9BTNXfpCzHzvJhj7XG7dwDSqg7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=gXrJXfJmh0cbMIbbboeb7M9W3FqL_G7KtxL2hJm4L0qcgHWlt03kRvHWs74VoJTLEVISNZVOJfK2cXdEUEsy8EcJHdh0zHt0DfqZDboqb15MIDIBOIIF-rE4Wjk3WwLeOBbJVEAEgsWimoK03OEBhDwY1_7Tzv67h5wmh6V3y9Yv1wQkDbhLpQlFOpxpCvIa6YFxS_Se6F9lA1iv5HWlzrh3rRe3j5vlbxW4eGAOQqKY0WeQ0St6ZrF5H8OwqL3M9sB7n_m6VIo07NTXTuKgQA0bVBxQDIEU9WpmqnEmf1vcTH0AMlznL8tw8yg1L7d7LZvC0zTUy095kGStMT_xgW8-dyPq4g99pMZEwCmaDk5AT6nheZYlXTrNJo8eYDmaBNKIj0XvrKSjGXitaLZ8yrs5OFLodzmYhBwTfL8EkD4atxpXoKLECPz8-N-3Df5KADR2t8reADn3p3kVdDGmRqfe3_ybo2202vcB-drg_KsiWX948-2R68AsS1NHhCt7gCnnrpUZxQqSKf0Gp65ibEgbwoWRsOFDaHZNjnDdfa4DumU89q9_yLQE5Qz7uZSOcteOQGHDEbdsSDcW_ELjCLffrWEz5fTXTbMqMZPrcTelvAqO9-v9BT6A5PgczuBEEaizCXagRJlcjIge9BTNXfpCzHzvJhj7XG7dwDSqg7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
​​
مجموعه‌ای‌از بهترین‌کنترل‌توپ‌‌های سرمربیان در کنار زمین؛ دود از کنده بلند میشه و از این داستانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22006" target="_blank">📅 09:02 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22005">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9oGn4JEh3BZzwt2VTXdRINN_5UbokxZdfJ45VcwmEBLEWKXBFZlX_qshqbcfaLDREzCEXZGXpn8EEMPJ3Au1ME6I4ES0wam4HXbX_dq4b-FBNZIr9MvsxJXRlhzNbkb4kJ3R2kUWKbTJX3PgtAN93-ZduAcNTnqItNOuEvJ1G8qrpZEf7SqixGIAWsoyoUR8-mzq_WR2izonM0DUMTsF9bJDr-jMEVHSC9QeMNKa-ZeXAvEGJqfdgLBmuMr1XazESyghhSZ-s2z46Wv2uH_f62MhUYKxz2IfvfSNShKpF2fP5BLYCa8Rk2UIXvMRsirIYkhFHC6MyRLtfv9hB1VDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛
از بازی خانگی بلوگرانا مقابل ویارئال تا دربی درکلاسیکر آلمان و دوئل شاگردان اوسمار ویرا برابر ذوب‌آهن در اصفهان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22005" target="_blank">📅 08:04 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22004">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hu5f63sQjCofOVM7WawkQT1vRV4ORSrFDZDYaJQm0b8z09qhSjxcpsuOle4Ma8fhCWwDhpGpSmHsoe3jCa0BewhfJL-F52bYVXQg4nj87rnMGuX301rK7tqsnESsd3XEvpEGT_L337oRb2p1Uwxw5yrHAGs5CKYLBh0LrDyE0Ch4YNqQkudFr2G96XRI0p_qQLzA3EZ1lBRJU7pupaNSfbfkK84lUjzABRlMrQrgcYzOy9kTz7zas_mM61PAAGm3szemfVgb3m4v1xkTUyO92orrfHo03_1yY3D7WEzwQtrE08Z5HU-BdwxAqTmeey5n1K19y3I8HC1-HjlilicSfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌‌‌‌ دیدار های‌‌‌‌‌‌‌‌‌‌‌‌ دیروز؛
صدرنشینی آبی‌ها با برتری مقابل فجر سپاسی در شب درخشش روزبه
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/22004" target="_blank">📅 07:59 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22003">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxA0Jk6m4cs6zzY9JRUJ3tbAF2P-GNezKK6CC1YMQKDLsvs-odbnboWRJ8odO6k495-fcNp1qeZRAaNKaSoOGYES3cs4YMbJO8wH9sEE1_hooqI3bcHph4vcPWc3r0PnIh4GSD196u4vRryiYxudra6KHeRzMhF_vZAU0yCfm3c7sa8vykoW09ByhXrU35m1C-nKpiuW372uNtkMKFeIR_kuTF6jvDPLqcwKen43_xdxbnuKQofbHYEHzo0UM3Ii5DI9BRp4g2HXQugRPzWRnufyVbSpkY7RMH5iJ0gZ1sIU_wRlF01EAQUskaTvolUeIOCmlNroEt4ouKQbnLiqgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین فرد نزدیک به ترامپ: علی لاریجانی، علی شمخانی و پسران شان دریک‌ماه‌اخیر نیم میلیارد دلار 500میلیون‌یورو ازایران‌خارج‌کردند و به‌روسیه و سنگاپور بردند. آنها از ارز، پول و طلا استفاده کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/22003" target="_blank">📅 00:21 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22002">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYZwnfZAhjIh5Veg3KwM1KLbG4te1AZKjoIwPMWIGhaNUm84jAFePi94_cucvWHR1zyZIrmnIkHNxjMFdgVslwOYx_EyXGYYkt8TyS-HKBY-Hn7p_3wGUXsv8GRHCWncjKA7Lf2Hc-OkO149vfYv7xTZeJsocf3n3AYz4lD4litwSt29asvOkqLicAoEHZLgUInDWufQXOitw2QJvr5WbcaUfY-L76gdI1z5Fbs0z-Hcu67dQDw_WuPi7X-y78Mr5GcSSXEcg-uZ9vqisTQmCa-i18gCu9ciibxiz2IvVkY9hNDtZ4EuyEpkfTh_fvCu-jNXsHTgkTCtSvbaY6xrmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/22002" target="_blank">📅 23:57 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22001">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfKiOX6fc31-TVvAwlv2YNOLz7A0Zqizo_PAX2URW5R9Khd2oAFEhCvhSesRaRbPVcZPfSpRqNQ4wIt_QZGTMHKRUksQkEt2D2cp0a2z9GnyVXMqwW0p8dgkbph4ZuwTAF-FhQj7PuXIylOC6cn-BpwZW6SyIbfUAm8g8Yqs_bzRAcTTfqQzgcLhCcpq5wDjj1K3yUOk7_AnvBvqoLbX8hgbq7dTBjuvRIN8i9fPzt7kB3Km0rPDlOS8xcOZtqMXkDhs17YnzZBDwebuG4NhB_1iDBSxe_WiD7oL7bAXaCeQ-JF2m8KiP6WKOEf905-F46ZR09AnEBsHEq9HAygZXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌اوسمار ویرا سرمربی‌پرسپولیس؛ سروش رفیعی و امین‌کاظمیان علی‌رغم‌حواشی‌اخیر به‌لیست این تیم در بازی فردا با ذوب آهن اضافه شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/22001" target="_blank">📅 23:44 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22000">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=cdZ4kku0F6HS_gwvka4R-PKa03HiaBJxdfA0Lzoo43scmNcBltArYcIhlbYJ6wZQH7fu7rM-A7_x0r7Q62vnllRqcfdULF5i_0XMxcOl3OSWwMVIcvNlU5FQM4j2kWDolXVd9fpzjs0yGIh9to_CLZCuHflZ8St3up0SnRJNCdP_XZMdoMBldCAOBbsaatxyLR31qX2NwANZap0sZyFR_FfKVQvTmqLKknVemLiH4Oiu4AeTzPJNJ1aKQrfn6VADWHEc1OKBMkSFO_-T9UiDV6KaDftDjWcsM0NnqNT8UJzVKvsjvEcyfAn91xQ49aKYmAbFB_CyvqdXis49N6K2vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=cdZ4kku0F6HS_gwvka4R-PKa03HiaBJxdfA0Lzoo43scmNcBltArYcIhlbYJ6wZQH7fu7rM-A7_x0r7Q62vnllRqcfdULF5i_0XMxcOl3OSWwMVIcvNlU5FQM4j2kWDolXVd9fpzjs0yGIh9to_CLZCuHflZ8St3up0SnRJNCdP_XZMdoMBldCAOBbsaatxyLR31qX2NwANZap0sZyFR_FfKVQvTmqLKknVemLiH4Oiu4AeTzPJNJ1aKQrfn6VADWHEc1OKBMkSFO_-T9UiDV6KaDftDjWcsM0NnqNT8UJzVKvsjvEcyfAn91xQ49aKYmAbFB_CyvqdXis49N6K2vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لیونل‌مسی بازیکن‌سابق و اسطوره تیم بارسلونا یه‌تایمی کاشته‌هاش حکم پنالتی رو داشتن و تیم‌ها به هر شکلی که شده میخواستن جلوشو بگیرن اما!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/22000" target="_blank">📅 23:38 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21999">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avqhsOd_sk9JQPovRKpyJXqvQJ-QoVSMJ_ckf1g37qdPUe4DfiZhfI2I5v5ZkIz_RHN2ZMNNFXRYD3YPe3QECA2IC69B2YYFnsF4Ft1xdM9aGTyPP0EPDT13aFw2upLxj5-r8uhTen2GMJIRUrUj_kivvOW2s-dQzsttFZ0vB3ySFh6Q2I0Lkz_UgwOvHsKwgmXzvXgTpucAXwHCF1jxIufsArt0POj2pw8kS5Wx4KdCz1vW4ewwIg7Ag2iKrCZJSSgDNUEApkdLqUFpeiREIkdtEVd8wwN1sQxG9uXQZFfn2UYRUz2JQxPXYs-_wM6izaL-52itN6OMHTiXVHbAmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
سعید مظفری زاده مدیرعامل تراکتور:
🔴
از سازمان‌نظام‌وظیفه استعلام گرفتیم که اعلام کردند علی رضا بیرانوند سرباز نیست اما باید تکلیف پایان‌نامه‌ دانشگاه‌اش راکامل مشخص‌کند و معافیت تحصیلی اش تمدید کند. او طبق قانون مشکلی برای همراهی تراکتور نخواهد داشت. تراکتور…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/21999" target="_blank">📅 23:05 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21998">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=e5TFcrPKMHwXqAjKe7Z96DR3KYap-L9Np71yB7FN-LpwBRTO48R07ac7e4pelOo-qAYCamTX5F50VCHmoHadNjv6XNOKasTmJWwNrZJNthUBTZOidscYS8mVnZCzRrRe5Tv-JeUpZuuIjooDSTrm2i8n_l5x5NI9yY8FYqT2dh4krZcBMkoXkWizJQTfkSpLqZ8n1wIlOasy0XrvQjH9Z2F0kHNoXLbd76LuCFedmtDfbuCEI2F4IAJwpnLKgrQvUrFgW7dDvAqZwEegwQaeSVBy8uLKNf-1EU1HKhzKS9WR1jEWJmODgwyI5woMnO-U3aKjkI9VxLv2JroKq_TpSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=e5TFcrPKMHwXqAjKe7Z96DR3KYap-L9Np71yB7FN-LpwBRTO48R07ac7e4pelOo-qAYCamTX5F50VCHmoHadNjv6XNOKasTmJWwNrZJNthUBTZOidscYS8mVnZCzRrRe5Tv-JeUpZuuIjooDSTrm2i8n_l5x5NI9yY8FYqT2dh4krZcBMkoXkWizJQTfkSpLqZ8n1wIlOasy0XrvQjH9Z2F0kHNoXLbd76LuCFedmtDfbuCEI2F4IAJwpnLKgrQvUrFgW7dDvAqZwEegwQaeSVBy8uLKNf-1EU1HKhzKS9WR1jEWJmODgwyI5woMnO-U3aKjkI9VxLv2JroKq_TpSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
مهدی شریفی مهاجم چارچوب شناس این فصل فجر سپاسی؛ استاد گلزنی به تیم‌های بزرگ ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/21998" target="_blank">📅 22:45 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21997">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194acea631.mp4?token=PdKtWjzytniWkAejcjJwhu6kqPQKGfFI8XlDT1PCBColpxbPBzBwETcQPIOua-BElggUDa2HUYg-X0fRz3dUGh0jeBmu3hfHxP7HbbilGzDtoY8Qwn6WK9J1R4rJopmYW5ystdcljgvmQS_mBS6D205jB1GTnGEtPYSnaLLftssDtRxnb9NSrtMAZhiLjZMz-5VXCISz9Sad1o22YUd8zB6cua7G1ufCfsPK3mkPxrGhluNpqnzcMFPGPsf4Bekf8eNa4yzBkFcIGOH0KP4bY1skCMkddx19YO-SfLCmAwYV2XpMNh6OUWW-4O29WzEw_7ss0aVafuVAUqrA5LEaVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194acea631.mp4?token=PdKtWjzytniWkAejcjJwhu6kqPQKGfFI8XlDT1PCBColpxbPBzBwETcQPIOua-BElggUDa2HUYg-X0fRz3dUGh0jeBmu3hfHxP7HbbilGzDtoY8Qwn6WK9J1R4rJopmYW5ystdcljgvmQS_mBS6D205jB1GTnGEtPYSnaLLftssDtRxnb9NSrtMAZhiLjZMz-5VXCISz9Sad1o22YUd8zB6cua7G1ufCfsPK3mkPxrGhluNpqnzcMFPGPsf4Bekf8eNa4yzBkFcIGOH0KP4bY1skCMkddx19YO-SfLCmAwYV2XpMNh6OUWW-4O29WzEw_7ss0aVafuVAUqrA5LEaVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش رضارشیدپور به فحشای‌ناموسی عجیب و غریب گه در صداوسیما جمهوری اسلامی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/21997" target="_blank">📅 22:35 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21996">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhv3XTwPJhQIuJWEmHFpHupBuLxbM0be8bTji1hkBlRtuJV_1yShytWuRGyACT0EweZaO1x2pkYZq2jPJKhP3UfFh64WLggGTNL-3BBE9YnHho2Zaw4625SGMONyw4CQn2twLiw_g2rd6G42JDygU4r55t09gUyDUrj2ZPE3Wmz2r63TOtAScW1EWdEOuqD78RlDN7CoOvq9tlnq3nl9BXpgAyrWo0qj2_Nr-LuFD_qTaxyr93FhRv3o-aI6yoRUKTwjUl5Y4v8hfez4_X1e7mHZUQFrZeE3o4xtTvfqdzSZKbREK8a_zIrPPL91EOcgzQRHd3gOm1ciZpHj4Kygrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نیمار جونیور بعد از گلزنی‌ اش و شادی اش به سبک وینیسیوس: هرگز توهین نژادپرستانه رو قبول نمیکنم و به وینی‌گفتم که اگر دوباره گل زدی، همون خوشحالی رو انجام بده. منم به احترام و حمایت از وینیسیوس این شادی رو امشب انجام دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/21996" target="_blank">📅 22:21 · 08 Esfand 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
