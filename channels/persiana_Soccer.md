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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 20:07:55</div>
<hr>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThjbyQeNHqMu79xJR43-BnU0P8nGmZ2EVQOmWeUROYnDnc9anhIqmwYY07A4Xv-YHrbnwOnQIc195FTdNAerCJ0PDDvpU5TcVekW8UP7Ph_LczDCsWk6IUqll1dTMAmLglcr7L2YGu0hiOqZ6ZbMmP4qQ89WAKXvN85qh6-6CeBM6C9JrE1nAOStakbH3VMUXqiowHcQ925FeiqVp_ZMlouj2ioHi60UsJoOy1EGsqD4ZN8neXorK-YtuwjHaA1hP4h56xTnqq6QLskj37KQ4Xp2QKEb2iHhyqmpMF72I6Vc4XltHoS6-2NfLUyx_HX65JyIzHeAuRD-TorGmcP-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzKuMUwsX_OEQ2A4CewD8M853V7kWTjegvX4Jyp9nEl1LBII_rZPOhw8hHOtTczbV14JgxLLpTWJ0kMrRmU-6-IW565OQs1XQSBJ869HlVy6BQDQM4sFeZ4llP3K3CyJIswa2oyfdfgXZveeyImfTsyrraodLrzeLPWgiuYFqIjJWeJDFuggISAsxrh7CndpeACN1rvlQqUAZ3qj2ulh9Jtzj-ZS1sdB0GoMiahVjPD10BoyR8HcQaeekPFGaSMvBRwaLq5itH9cC4LUi-Q1JNffsSfZOpKKfkZSiFnxrCcEps8tKEu4d6GcnqaRD5CxrOBaWFPTJ2LUEo0S2tbwAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ien6wdLFa1M9xhYdRin8bGZ0aIfXR8lF9ywnVH7IrtDREzZVUtCrrJLA55akbk8clB71c4WfzJbnI6zzrXZdC4ILzlz8VXdL13gp3wa1XeUELMDewoUzYC7RtW0S7EolLZgRZzk6Rc79_7dAqS5XR5oSK9nxZLI_8fyKx8Pjrr-cuE_m8Ilfr5E_Zl2Iz2vRh8kYfMJdl1B6nJ-6vZDEOnxkQc0rDokW9N91GQxRcaY_n4hFmhc5WPIzz7fTJ1qp9IzEMpvSpsYs3FpMO3SLFU8ToWSvb2qeH9-JMUvPGQTya4jA0VkL1NKQ8y5eKNnyfg7thQWlpRDOwgCgIMEQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRHynLFx9ET21d-pFx9x5VAUdI1dNQ7BXT10fJmYPLDYUJM_i5C7rKLq0Bbk6NaU4RwF389WTUqBQLI92CHMNESpeXbGIN8YBeKLaTy_jT3Qn7gE5Ex276LD2GQvJhDqU-yDrTh1xvpRGsL5r0zYzc30aS7zr-SqwtuPbDjd9dTozA1skvnOJy4qaPtCN8IzZy2N1pM1b63gZusB1iQXvX5j-19GKURhIQ63rEjNjudUFQM9KWJmGu_GTj3wPmcZVhPDxuT0oA-JbMsuZTn5Oi94p9ocf1rwqflwetq_PPCGw_lrHI5gTaSWtZ0jpnUqmm3oWkWKNmTQ8NsbT4VIiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSTQjJQd3hPXHw-lWMtIAIkfCqcMMqFi8cxi4qD9ovk5ggS2n2uOvoL84HoDfyS7ibQq6YyQsTGsSHJyDpVX4eqwYTFv2q-qK-9sf_fmsTPgulIV7nXQGGwieRsmaoyjixIrKE3tDlbQ40vOHiySPe7o8d6q3W_qrIrgCkqxsahWvF-TzpafERqqh1Us8pVwXn5icnOMqgfsz6IAj-wmZFogjN_aalBzKt0UHIPbeO2SjdWTxM8OCQ7zofvQSErZaONlmtAbLza4zDTI_jcdVbp_s7k4NQhvOsi0ZreKumhnMO15XEzrhKZFaZn7oi0wkKohwTlps_L21JW8hcphTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=r4nVlVxUEWMXG9j-PK-N5_QkEY0BUP8xwmWiMWB-TST792pHk5Kah3lFKxq090J3XemaSDoCpG9YJamwY4TppIu549Eu6JuDH9-Bvbuq1yJJAlRM9nStsCfvBvRyzF2hK5Mwba3PD3UscDV3be8L5tSG3v12slpbPZLUlJIml2v7IxKEe7MrIEcinwuphVF8yLMwzTrvLfxRjcMc0m7xQIIAKctZvpA0Crn8dE4q1w9Z_FzRQQD-6DSn6in-EsnOcOKGVAa3qHc7SBrwOR-j-2OyZphNaFQ4TcxGkHnyQQ47DgYxF0q78kFjuiwJpHGpPTtbh462URHGaNaVnN3KEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=r4nVlVxUEWMXG9j-PK-N5_QkEY0BUP8xwmWiMWB-TST792pHk5Kah3lFKxq090J3XemaSDoCpG9YJamwY4TppIu549Eu6JuDH9-Bvbuq1yJJAlRM9nStsCfvBvRyzF2hK5Mwba3PD3UscDV3be8L5tSG3v12slpbPZLUlJIml2v7IxKEe7MrIEcinwuphVF8yLMwzTrvLfxRjcMc0m7xQIIAKctZvpA0Crn8dE4q1w9Z_FzRQQD-6DSn6in-EsnOcOKGVAa3qHc7SBrwOR-j-2OyZphNaFQ4TcxGkHnyQQ47DgYxF0q78kFjuiwJpHGpPTtbh462URHGaNaVnN3KEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22120">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dM7Qbg7C4ZbyWQw9BBMKSVS9OjLJnLiG_rhQXvUb7xkhAk06ppE-TVCcdE4j2AXE1kZVSkYdr8TK46I_QdZ_HHKJ6U2zQMJeY9NvmBKgivAzgVarctz1aNqH6tdb_YwByVN8aGncttiarW3C7nrDDd3_pxdYidixHasRssoGPLmbLBH37Y1xgmvGwqf_Qrxp8p6YA-nh8j5TbIfwWx09P-nfjFeeTkjcwbYNPBTj2q8zzCpshqfQMd-YepWNMYvx0kdWYkduhch09dB84wfc0GMbBwDShldnqsa_ECRkZJDDFqQqkjIFXE8fk6bAdZ4mEAYvCEPEzZ95QpD6AHcjng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/persiana_Soccer/22120" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsE0fViaXWZiWNyT1J16v-mWdfWVyweNwBYkdSk4ZHKE5bH1ZmAurZ2nyat2sA38p8HjciPQy2k4uNsWHkHPLilNMrpGcO66QRsnYT5ieFlfFEIuj_gYCthPG-aKiyVKWb9ODugJmXgKKq9KukKPUrzQa5QKlu3PvrADBUV50q9jzRfhTiN3k40SrUp004BKsWStzKv1YGMmB-m8Y4qkrv1WEgsAba9TZsw6_rHWseJqW6qTEMygsevmv0fVkHEHuTYSEiznxPv9VXyYLuEEaZvoWKg-fJtJ_EHEYSFq6U4NomdjHDC_Ie0S_cAgX_7JxU6ETPFlodCrQr-jXbmW7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xv4MxdOj2Zj2CCoIwW0UayljEpy1l_FIzkgvF1m8NMP9o2vWdoUfNMzqy3LW1LmK4CuvVBRh7vhJIQLM2tCfrXi4adUSEp_Mxcu6XmHkB5iojTn84tL--oxZHvrKUQ_8bo6ktiSAFYCDQsioPVGkqzUG-BfTqCaBmyUB0XFsW9xPSQw7oxLx3OJ3jHUzoWtovT8WC1BFlvfAItZOBblW20gGuY2j6nc0M8hU3BCtKTLrmEFSppntYUAYwrSpnkHTum8v7Jg3ufn1UZdn8GJi5UGhmHJkh5t9jcEFw53wa20JBs_G-bJYs2yylSW6RmZjXlNuZR55pCMJuO0g_DZPIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npPOJgp7U5iCQFk8H-KIe7EhRjpoXTwL_c_V97zfpjGLRXrHO1tXpIvi9ht3HvX-00s-2fUCIaEnHV9VgTj3rqxuOSEGY1NsE13Wxg0FIspBtjGiZwOCVnKbWEKE0vR0Bd4mumXne8DK_avv6SHupq1oP2wi_X_eKBwlYQid3yU5bSF2tukBeObMAFw7OJLJAij07yht51330nX-wjwsH6NTsshIed5I3BpeiT8s2jnBSIY6opsX3sKwpfmVBU7SmYjwhjQ1YzcRG44pB09IKqT3T4rDjqJyPSDaaTot3SZOTUAigNBxl3Vqtf2CtLDr-v2_lWqnoCNYyBNYoF8YnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niqCgpKWx_Iz6PXuKXCHlilV9JKYvT4yJPLxiigsdMANZPbxjWhfx8i4SYWWWFBQvBVSMkil22pT0a6Q099XeBNmk31_lTlBq2gD7MaGcYKuOaPsTtZWPxs3hvLzIOpQY6S0A9p7cSiVecN-EvLMHmfk4EoN9Iv3c3ZEdnYYPofejn49qOb0hQoq_j7CbCR-3-VHawGb2VvDFzPUCDPq9l6KJ7sQBV_sBTxPE1i2jxBLePUuzjEq-GpYkQhaZZQlYh-gBURMRN5exlMatzZmq6dxjl_W05h3WlM4pw1sZjha7ZAHuT8hLgu-Ey05ysnebQnRuLysKNbz2VX8lccYaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0wlq72lcwngfc4uyNmQ85WgSqOEX6-qqhYcUuR3HjZTIAjNX-RNXRJMOPlP8Zt3KPx0SrPwhaZjP_BXvzzJzCP8EQM1LkwfhLAJSa4_hjd98G30aJObMPrfWfVknSH0Z1kqFkK4iLuygpA5_NEizO506Esw2u_UXd4iqOZ-WH6fE7JqgiThNYE9AZLhInjRexssNdZfeyQJZODgGgYX3nFBNd7IrX0dM_9v0vzHIqlmvggDT1gKELs-a7stQ9MCtrOrtGOsdFoeuad5345H6SAn00m8logvKtvMsqzox6lqriGncNy9EfEWZubOKY8pVNTqrdzEXn8B-Xj_gukobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTMa7aY9rz_JRcdTs724gTdYzJv9J-f0hxExZtS6JAflWRjRx5QgEr2jECru2FprjW3vpqSoghhRMexLkk8PHwy2XitWpcALLTGJfaj2TdxpBwBqKfmjaH42RW2zjtsPFeJgG7FJj2wogeySySpFJaHDtfumLN3zUBxFFDo8SpVj9cNOWd0WFJSBK-f9tUEVat2otvzlwmlxRfvBS8raOFuD8uyst05mQ2mnC1K8_6ChTC19VXHjzUIvam2l_YGXLg37QhhT_lCA1JBeSuCj2XWzwqpZjJT2tPxs4fJ1rAdNFoXtOK_Ki9IVyXpSo9M-PBYEpQ51vW8tdp0duOavfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jpx9X4yYicz_rX7fcEtyCcq84rjAPlJbpZMsNKQmPBSXUGtU0o1dmj85EJZuEpebtKsdxiNuuEW86VpAOneA3tonlayh3cDBMwuEHSTvrGNU4i76Tabx9XhQeujs353IgKqx5FgJVnj09UjMPXk2jEorlkxQMGbcMHpyPrOBXFbNneBjO8OYDf49wND_eYIBeoQVrSxvnWeGbdyumnMeVwFX9adfVVkCuf82TLlfTyRuUVE3m2Mh5_NmzZTr2wscjF_8bJjp2k5uP5cRzggUg1QPVvLMgEiYmx2sNh8b4stkFUF191XpNzJ0l8YW7M8K3pYqUT245IuEyPV8hAtI4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3JE2O5WqdA7Fhp_BjV1Zna41WOfHlpILM8fOX-1PO4tZG9jKixkZ900A2_bIhr7du-T9tgHx1unoH6-N4AbFXwfxnaV6LSRVKUQMeAi8zAgnaDSdqlfyCyZ6uqaZv1ptjdJYOV_8Zw1x1DWd25DmBC88H6P_L_K-w1dif5lYvwwE3TtHoj6XvU-JtEARIwCjJH8JBJyreu-aa7c8ibyBsHT1FjW3LE9fSoCaSnbE0E5zHhknLE9bB1_Stc9Ie26HMMEbU2VvDNiblW24kXll7xIzyyP5-XEXEUGQj1JdtpcchBm8fYNSToKuxpxHl56mCzv2jnn_pXblKrvqHFUtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqpRLcUGyUSXrwroWtu8y3-OzLaf6rSNlMporvson_siWV_2Du0VmyTv3NJ5G0e6tbORy6cDAToEYV0MVciX8jkI7OJ1br0RNREeViGrjIKfF_l2Ybl8Pd8FZfl8m60-eDqkOAnZNwx2YFBTD7NO0Qq7HPz5UcVAndyblDoBuxZtOiPa3fdHrtYhfOY_e_cNJIovG7tXsEWyHDH78rbNwMHd15AuBqVvCewIAvgUs72xCFNYTxHbYQx_ZqS_dGRl9F8lIKHhorEuKUjP-yy3Sbpt1ffZmcn-hLdC6_s0V6fRM_FSir0T4sthOcUaxWsIKzEkweMM8l6iW7jP1rHQOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMGBJTvVERXdym5-07Rm4x7kA8-I0ecopp7A7SYa6BeZ6fmktXos6Z1_BzFgR6Oe5h1j9rzsVKQP4_XVis9k2w5L6XgInhttcpMYK80QLg9z_c0TgbxJvw0JXcYCkeL2IlQ1tGyf7mM_qyLLPD4zfzE2zWIkeGOqZPjC1ZQXVQZ6-pXZJAFy526IUBKVXm2QeLXtJAHUy1CsqU18-bxsBmP1qysMzExxDdPIwO9G2wrA6O6Ldi9enzFwNt2ro5klwPIlab4N9J0rC4dHAeuE4M0hLwzH7lWm4pA62z1Kxd691cTb-iRehHxfbIeLP5kZ5-CJj3VUBqPRXQtLc-KkXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8k90byaOL97ba6Vdp3PQhD9MU6WFNtI65x-k9TyXONgSPgpgiidFiDC1vWtyL56c057Go5UWf1CBz7yA5uf8BMHfo8p_mo_PIMEsEIgzARTJX2AIcSiXrnOGNv6AErSWwkRIwc9jallnJM5LQJtpNKUKcDlv4npnpKKw-qBSjvZKgYMkMXL0LWFEM3p5Ri-vnUBmMOL9kCqw7F2tsoTnR5KVcEeOft-R7fLxJiJO8uZdYIjSUQESLr5ezCWamu-8MGH2QH7rdKLWREJHLPzCGO_rj2x6YAoDriyEDHQUmcj_JkfVR8mUIA-92O3XgaJPSExjFazR1e-tbYCzAyzfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJYJXOAYif5lwbmsHqOAkliVcwQv09oI7jEUqWSlhYkvUi7qGBqXrQb3Gy2oaAVz7JfRFJ7zfZAbH6AIScllFV5729qS-sVNLlA38g995apAK8U0oU2NINE-iGcl8E-oGk6uAhJCDw3smKYRwyE32ssaFnCj7m83-Ad-R93m4CUvzzA_c3vK-trv-w2D0uOmZWw52cOczHIgv1w6_BmdFisLvSIqSeDi_f7gpokAaHKw6horOoveQNXnyVFtlvE9aaMWZExAPK6PXA0WEqXshFgg2PkYHsj2FDIHNKQqrTvgtRsmjHBVvso71kaLls7kLoKJe62jrPax92r-YtobrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCx7UlvAa0mbGtr1MDq0lM9M9QbmZiLXBOuv1k87cxd2NhocXX3EhJ3phySip5i66xPRHPH1qBNuVq0Um1w88ir4LWE8XoGPBH6dwsTDtt2EOhC-0eMBAACvkse2Xd8L_O2W9YwURENuBv0yoYwqeBDfeQ1j62dO5yKCIgBPbuIl4j5fY5y17WVOZrhLke4DLbBqMKCIeVPis7vPVcah1lSmgT7-Amrct-KYxHbQix1bHUreuPYqwfrXBlHJL3GJEE04N12tWJ-87-IOesU4Gl0AMdYvXTWGH-fdnKq7-CRGPyL6dlctxih8tS5-M67u_n2WwmE6KU3WVbGO-PRL5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUqd-fWfp1Wh6HTDxsedFYHThf6ZZIDrdKSbEIXA0OmFP0kSoJ5_7e3odaf4D1TD2Vs5NPWrcT3lAT9ErcPQe5iTloVJP_XAKWvf6otfsUfvm7sS1yEaYlhShN2HxxA7EH-xfdD9Gxzwj-ebK7qheapu2OT7iFfHqtyOHQGQ7NdB6Gu4n3UhAU8cuKxoMnE0lfr-GB5CCObX5qHaDiDHJQuKQiiUmj0NQdyVQquG0dM3P8w4Eu_vgoNNtSsppshAxxE9th2qOWErd1FOYTNPgbIy_AKxhurvfHTi8IIBEbl19VL7semjkpaDaswzl5tz5kktDCgmBiKSeW6U_YHu5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emaLFkGSWnFXEOaD-yyZRQKsfldekLT6Ad28M8cJA0O_18keDkNxpMCDjFxQO-DzcRvX5L4gksz-mZQ_pUttY5qfjOdp3hxEmas0qemEim-QAOu-JW3S6BNbFY9ZMMvgwPpYTa2kLbz-faVwJIWxbVG5FNwfD79Bh4mb7oTC02cj8zGmC_-kteJHtFT7TDU-IH3XvA9orQZ9aXAiY90yByOwOsJSD_MOxzKUwUCRuV5Zpooqfkycocd1OUV7bfjsGB1BlWRxqVXWeQaJ9bDczpxmyEl4utPncUfwn_OAr6VEsZvz4r05EM-L3TxhAudvPX5MmBa2GEslzDNcV9fEjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=VqOgaQv4opju_09B6tCJknaz8TJU5UGwJ6vZ8TQhpXce0oGF3KUX8Kga9C1qH2zgY9hE75fXSHzjtbdiRvcF3hE2NHJepKemYL9uAJOY40omVVpxJG0Fq86z-xyK7eaPYdHBTESczLaPtzw6VsGNRww_i9B_kBWwHXzU_X4oEvwnZDSi2aeS25baF1sdOBXU1FwJiE1Qt80BEs_mJY0C2dKB74r1lXGeoZPcubsUUwxKAb1LUkeSQPUfULXVUzBabtmC7B7rdtA1NccTMdtW4iV_VpYzQa4hlXkdL_6FfkiIoXdRuIGuApr9faiXJMi4M7bpReIT3AJ8AzkPXA6g6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=VqOgaQv4opju_09B6tCJknaz8TJU5UGwJ6vZ8TQhpXce0oGF3KUX8Kga9C1qH2zgY9hE75fXSHzjtbdiRvcF3hE2NHJepKemYL9uAJOY40omVVpxJG0Fq86z-xyK7eaPYdHBTESczLaPtzw6VsGNRww_i9B_kBWwHXzU_X4oEvwnZDSi2aeS25baF1sdOBXU1FwJiE1Qt80BEs_mJY0C2dKB74r1lXGeoZPcubsUUwxKAb1LUkeSQPUfULXVUzBabtmC7B7rdtA1NccTMdtW4iV_VpYzQa4hlXkdL_6FfkiIoXdRuIGuApr9faiXJMi4M7bpReIT3AJ8AzkPXA6g6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5vexPhaGNTjz9xuZpA5b3VAEzz1Vmfy8TPH5bicMzNUsvxkQNVnJigTOkQ7m0ItEqsbVGGlweeAEw6mrA8KT5q0Flh1BaXOt5tuRHAMxg6SFYfGHqroEPqZIMzWUGHRm6L3_LYJcuABZLWy6NL9YkftkBE-OcBQ7koVSMm_Utsv44ScOiV70kx6g6WIrU0mOqqXIpLQ1gVXxy9M7C-zybpskNeSoNJsR9NjtAhTO_xv89gdpsLHg4yk7gXsUtJySP6rFNi7yVVnOpw9mUVyBEVNBrp-KQ52U2t2Pl8UlYAp4kvyP9bd1vrKZl9mJXhFNZ3WEbH4Z6a37mfe_WQIAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8rasSlkEDIatIsAloz9IouwttPOIkcCpe38EbAMthkurYLMhrgm6TKfwPs51SPWgqKivIjPtMM6hK5lV1y_lciD74KFtCh0sdf9iVLThlWDY2o3BiNcijxFqtnQzy7mL0ZMpLiZ4hgUYzUOSRDrzSUl15Zf03lQP50TgMrnRN3iby478OL1_5guMLXJeaC107vJp9qZvNiqI6OjDgbbNlDZ6sbmqJVdvWvDFmXRgOXIEUdXVuycrcAM0wb9907aBwrWZzHkp9gtFVQPnvpX2p5ER9iXDXRcefB21zczn3V3wYOc82_Z1jRHz5CKgLI0gz9zNnVvZRuyXhOrhFMPBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9zsT-COL1wE_Gi5C00ZQhIbs5-JcdqeYiTGhVsnpJBW8y1XNGmw0xNeu2mYsdAWHxVFXBEasV463uKLiXc9o-cBZOfFFT_EMttJ2TrmZeq5biII1-F6M4K4Jt-3Gw57oSKR9hH-W9-0McC6lRbIRFktlWohAA3LaSnhhmznOzXyD-9ZfYil9EYhdOfIImfy1llNMMqZQ8CRloGzP05fsxv90_5RFXR9IcDKcOUZBr9oXBEj5OY514hDfu6LmLT7mOc1VPOBv7dk6Is4hENq8ix4snwj4HE98X6xUUfzg4kuIiDoQOup70dDpBWOp5QQFhsTPP8hP1IhmH-LV9Mysw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nnq5fe9BOpqrsJJyg8dgfb71MpVkKKqqTZzg5NGMi3aouiRnnHAJJWZYizsQWCV9Slmi1stM3bVAETGOL2aC-0DQvV7AamIPdFyy4CD9csFlF25ZIydehGezvScRY_Mt1bf_O_-FcbpS9cGX-VAAO09gidZrCDUnvopfA6apr8RUoY1UBpjMyyMzX4tRRX1OCSEnpkQI1B2AMOrvpaOGbnMX1awIg5hsx6BpwSiOFxQ0V8_4K0pTOk-y3BrB--xl__iX8eLi_Huajcm2OvKSvGA166UuqNns6yWzWZhoQCmALxe0mvNCaTgGcCWq_f7Op1nDHapwpRUMl-DwPJG4jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7PVh2fBSwQU7UfKwCc_VqAEUzm8CQVPMMK6MY6E3dhzg2xfqF4IvcyOMCGH9RbtOyBo-1YtUjiEIpjAn9HMKmxn_gpVxorsczoR-15jD-rgKNdJtss3yC_9DXXHg4x81xrvZ7ZB0tOvkhtzSCiS7c13mEcEInKXuIqAXfN2s755rFlgVfjA7LxvfhZLcjZlUSuyT8ETQGN-3Y766V-VeUxJQh66FxrZiJ2xSD3TvdQehI4IzfyRsl0bm4lVgGQ4pvcnc_ZAMlH3LCe5ML34djh9FUEOkxrkx0fdRC1xMGu2auofwHwbpryrYV4PcqvCx8Fhe_fNOeNZ8PLbCRxqbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBVK2dCZPJnzFdnRcSOfTvleFhmjK4V2CdT5lvvTlmBUa6KeYpT1MUmaDF2SyOu6EnIypcWJqurGL-ZPXEXtqY24OzoY8o-BAzCTyZLsG5flAuIpyY1AD1tHwBNX-idTh4RBrA2c0NAnHO1VDL76PyKD2GCTGGl_OJ_ffy2POAzfkCrth39WlSQxD8xkp5gu7nl6RRcPkkS_Ww2ZG3_zYL9Q4_VXmcGChzHBNCdB8R2W8t210qrOm3YWFa57YoJP1CSOrN4oHxK9vJjiHCzvCc7OuZWhFMLvfjUrzxzGhvqlceAebbOSRUuj7wlynl5c-gkD4SdEI5TP_2JIZs6zMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gA-bgroq1YWSQOJsbAo8neTO9Pt2QlNxKT3Q_dhFod9PcoCutrZ6DoByz7fwzGByTkk8th8p2d9dmVQtjnU0YP55En11MckPZZopIEFZGvose8v7SIDZ0ZJA23If-ZAzvDINNp9QQ9AInqFc8TowVgX02PLpjYFJIAcfiN62_sHZufWbKsGKhHboJARkhjUAlTJuUzrppvVSZurEhuJu_zyGgFJMIHShGYdydwmEB7xyBy9OYM24nIUKgQ3eOzL6HsPL8RK_BF9daOcpR3CMK0WlrbLSnHBRbJhTVPf-aKZVcHuteJkEMp-4EZdz-DUksyVViIFA3zdyjyWKbtilcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtM6RsusrZsbEfVABxCgfe2qDiL29vSl0Kw61qQ_kmN-OEqSq_EwIZtZoOosgpPLvPavR3TDquslqItGTD7FMMLp5L1V0B08584HWFUt2sk2U4em-XTgqQJH9znHH_Kj0QcZHshGWslebr7pSuFFztKuP1kQRueEpf-XGI3vD5UGYP5NdWjzEqOFcF4D-G7eYBK4IE74L6BrXe3a_rb3KL4cTO7waAmgASozzccbWOr51_DNc23cCU__klkZgAv4KAUKXBvCIVQW2LbXUaJWmuAW6_pw55YRECKKbAbcg-jELs0vFMDdqRmc-TY05iFvVXxapBuIvZB0AUwKQl9HdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nARXIHtW7WhPG-eAWgcR3VJr4WjxizQGb7DD5Iwlb4uvdkC6igeLY0W__IG4o0NW1nzzf2JmmwdahftyTPHyEgONuCJ1k8y2G227ZF3neiP1KDhduSAWld9BDiH6E9SZDbEmcjGt58ru9Xt-5TPoCx4uon1Vbkzj3k_UTt8AZ_uMud03xVEx6hSsYOeDif_69OuyFrm9cWOvlW3zlVXYk8bvojiX1js0szNJunlLWyCtDs0O_RlWGUvtdEkJvKXTSYBZp_yU_vL1sJHb1fJ-PC1ndCS1PzDIypxWHc_Er11StoQeXu7qfgNa0WN1yCYvn4JSToQMyj-HsVvrJ4AeuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvC6EudYTEYu_1VOzM5TCRaqjzdsV-4rZmA2HQGBW05WRln9riUBjEhS0A9NEMTE3q-4VPK8vihiGOJSR0Pq3Copufnr4Ieq_QUEJe2p0_GVhGysF07NBqSJj66gjrr3s31SmSZ1czJEVYu3q4Muxhf-MWepV8L0hRtJmMDWX-jGRN5HzhTRNKtuW-u5Sl0XrHX1rUsU-8viJKJxLM007rGcEbGUnFjwi5CvBplMbPD1ZHUj8s6quybsQbIRS8OwXU5uFOkBoHW3i1EJkToYMECw-6jqN6blU2HMqeFZOFu1u8yCS1NtU50DNOPjYPlfRIM_oqFixfJazJ47jHomTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eoc_HgcUe4TYwR8gonWIlOdNpaNhqLXH2b_Gi9S2soBWVJRg0CBS2ps4PTQDDAj8i3UT0cA6r-rEEi8GJSE_dWrr-EEAPGJZvRefzurkxzPMZ1XoyFf4cXemA2M3zebfuo53vA54G2OrQ2Abt5BDTH6byC0_Nr7i8VPTA9geUOr7PcVf_i_TYPWIydJ29UXS17S4gUBilJ1i6CRSauq89WmNVeNckHs8u8g1UY3dbMT8vtTLwGzv0crDYTQHXwml6jMNQdFr3LDoqPVxsjJkOUBuizAQsMgck-0R2Qvk_ojWkAfLcYCNy1lxrLo6arUtO89pKjDea3Z8xchuGAeypw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8SyScm6T9F72RvyhajWD12oDfZkPy-pkD2nWD7wURPbfn7eAmhTV-0NFzZqRRB_nTzKPO4l3yQdUyJda6tZSajt6R9B02qP4Caimh46RzpbWiSHm-sYe-YzJvaZQxOkyWBbKvOpaXEIWkvh834mHY2eKH_AszavWzm-C3Q0GDPoSkWL_D-soEWBeC9AAoRddFhzPyL7ILH6WQEZa1UzqQX-88BmH8OUyrzq10wr7iIoH1XQXQ2sj-gU_WYAn-OtC8gNsZmDCssNz_rWzc5QDu8AZoW1YFnEToH4DLP4wRDc73BMzdiCetLUT014EFQyOh0xlRPhPnMy2lph_5c2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJMbyJrV8vYys-05CCiY5MdS_NxcX_V2VZ7oSZMC1ITf1gHcFIs65g1jopUQ-4FmIUT6XPUjCoJIBpAVNJP0cia-_YUrdyYdfq_AlD-jQgui_SpU1Q2Sc8Rqt-FOsS9k0OrYYJEkzzFb3_13ahlJo8Sm4laHNa2q91ECT0fuKmGGvzjLwx9WtEwCm1D_9vrbDFN67KEOWUaA0w9nHWx_zmlFScVplE_BcKG8YQoeAN_k-VVTWd0rZ5sh-eqvwQFHSESTU-Gd1LnTcxm4FXd_eyFBvK9evyv3cJjdv4tFja_H5dHfennrZswGLCO1NUUwHXTXnhYK1QBdaWiiI2LigA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGajdM40TcRz_xdx3W2SEytUtiraUl3PKIOM1nukhcQht5P3n5vAYOtf32FohUO2ZrQBGnLv5jiS9lvlHsYOZqYU96bSsI_QfzPGwV-uudgqBRDsOCYSPJjTO4uZ0KZaJ6dkrEM-i3kC7VqakIMwOBTAh5idHZV2_jkazHmZbhnLEFp6iwJ6J9u2Kta1tlHuutML6Oj9hnig5frjEDDAKr1XcueofBaNej0vKkuNvBlR6QPDhv8e_GdYAzt0dx-vz5ppMsD56EA37foLEsUQ3xfXhGGc1X5mSkVu_wyGWt-65vsosL5Sevr-G79dxt9KXPnb9X8r8xEzWVzBRxtWCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDrQ0pcZkMroIK8JLEWdzKuQRYN64P8wMrwLmmIJTF2z6Qn28ZQj6ELiEObEVOnzm3gF7D1fgDYGcHXmn6VeIbOTTk3oLCQx40tfWl88YKpHs19dBmKsBf5uvKajOpFdYVXn9MNV4m7ZwoxjgCLYBFGAonhI_KjQ_a0eJP323pvnwkJpCMJ262SeFIBYqtxBEqlCYfYwyV2ZEh66-9UamGECUgzA6WQueNUFVsE-mgjFPW86MQmObb32LuyCViJ3fPMMnNkaOTY3mDkhgKVs_6g7Y2SxVtVzmPrGPnMZ2IiQoaS49QjuVLIDlbH-mSsDem5jcVN6w4jWCjLDYXNqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCGSyD-fdhGDSfSb9lpVgNeXfHccm5EJM58Vqd2xtbtsKMQvF4b6WjLYcD2xgIhJXBES9zeU5C7GtqN09QIrLOHmuQWVY81AXPvvC-c7zzcl5lDU2MudmrgT9Z7ARCPbjfn111Ww0xHS1P-nJMVdqAnljEbk1DDlhtfV97YbvQK4JpvS8c95N-fJDJPaPPnHCV-IYlc6s9clhupWGpG4Z-A-_s-v0DXtm2Ik2GqRNVNszGEmuaBxDKUH0w-ytSk1CVlVP0dMHYDBygk7hm5RS5scvAUQH9DYCyis0Fxst-pLbm0KGDdobwtpI7f2h-GBocuhu6Ih69mbVCHYJ-qV0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPL4Te2-o3KGGhtUGhFMYvj97POqluNnlZGaNjjfFO6Il5YBUQifTugByRTqFj1549oLgxOey00KMnuIDan1eDyrcBqd8eYNU0D6uTDV2KWOrnmsMfy_T7HL5iykCGZF4AS-rGCwGedPP6K-qdDhlyFCiWvRBR4zKvL9lpAA_7vFkTj0AwZUGgBybzfZnEnR60_3PiXJxeTuHfZdS4XsVMo3NakljlCkYwtfxkd4ZVnAg_77Os2NcomhrW4wk4RzimoD5SH_rvRyApzgCWvt-zhCB_Ue5DSefXdfL4wgSGYaBAQZWDW1TMb3GcqcOhV8oh8bCbxScooICnQB-Rfzww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTzGu3-kgf_vMr6UiocbqAEUlD6dXpu3L0GOpgQ1kxHoJV-WsRunj1EzjIoXhzYlaahobzoXg3Wg_uvGEXZgDvxEQazJjb8as86I8ctmpOqX50z-YXYR8XUbvu3JA5D4JaKUyrMYDFj5aPUpDY1u_6iHiltIA5WlFQWZoERYqT2zxIMTeorSC7cAMVPvBZOVkYy68ibbRYfEGLwJMQDZRyrCqvxdBO-skuHOxfOvPP-GhjuY7rO-lEONte18cRw2-gHbPOHzHcfVgbSQykbF5gW4RHTlY1Mnm6LMxvLVl0nxZyoYdOEaXTjCrosZdGCr77wRYZRRSDm-FJDMNzc6MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HV7B2_mskjeLtbWJ1w7fJAGlFK2yOLXPTukE0LUphLRObfxko65vzyO15ssDCszt_86IEgET7lQG3OqPwhZJLThyaIVNA3Xw5ams8TUfZu2mjD7fIOBUSlQ8fISyTAkJGLjQuLkS7udvM9B3LW1BXXDH4F1PHU9YmEI6o8s-JQpuS8ps2LLRQ3qldeEKAZK8Tn2zjGU59VuJW4lgGrcaXgZ1OC7xb9fw53bbKBAU7OIJtBJL6QJ0sqdrrCdKIUsU-1Vu79kX-MPUyzAxM9DcZ_tKGPQDlnw3mdKEGjuk08R8xuG4adapscXgWDhrC3Sy4XhF2QJVRmyV8yZoTbFbsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMI7zkauYw5HeEOPZgXgNhAdMxsBP_Hy5aHzoQXAdiFzOdFZTVmMvxyhrYdttK0wmGTHK8_3sFe1AYPwFQl0L0Njig9pCJig7bai5o0jiC30mPpA5gWqakFA5q0WFNY5oTNwJX2M4Vt62DamcPysoXqVyWh4aDmOTi6-hiJnXJTIqFDXWX09natxhkbsInXfkeA2LrwC_c1mbJ6whrClFHbGB3oPYbAsPmSD5SPG7gIbS_x2WB0fo09pDz767GikwDojZU-EyRjkN9OizmhFw5uyQ3-nYzPj9sPW91OJAeO-EphTA9kp4aDE1--CcJtPVv3MKq7_lj3pwsaqZmGifw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuPN2sR42_z5RpBR1antcmmfVDrdycuYT6fV5PMdIaf0MVYuhDMHx3I4qI5Paz-xN74zVed2NHAIWOXSSXVMbJncBZ6vgwu87Vmtsy10RW3l3jc3fv2o-R9PIcdeRdsgVCy8O8FBf9RjrTRMuoFvt_evSvwAH8zELkGOM9HPxu_LGRp_heyMEiB-i9XCUoGzK6sYNZpvRe8S-Cqp4BQW_3KaBt12_T_7XIIdP3xpfboUpvVDZLEyMAscYxjd0X3EsvXAWcSfGzqE8NSdT-0cSkluH8hLpyjS_-O_Nc-M5tq-px0sVLHl_trF8VOz2EbSB919ckWtGnSW-S745WjWAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5Ura_4d_GOUQwiVvxsGteId3l8WyoYeYVO4E4FkzDSdy0RKo1EnjumpzhGYBgFWdMdP7EKEDmWc98N7v22X5USyMi0XSz8qCZPNEoWvonEPi2d8wM3fYSmA_H5ikaOeHlxZcQJbwcBma9T59psXXh6v8aauQYth6ho_D4PoXVh3SQptYcctENcdWvW0EWMaLnYzs2TjJ_7OATTGyP89VcKn1MFDKTwOtfemv06fQ8ZLDHDHOuo6dJltVjcD_FTPl0yK9IVYlt3k2VCukfX3f8JF0uaLZunGlXmKwYLnOk2atBV3WpB41REjbi9u21w40d3KSgod6JLryb6PsKOpOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgciDCuFsHJCIO5WOJ5R-4hHw6FxYC3dqkJaxY-hPfvdFtsmbc9BkESN6kRwa_Emc6r0g6XxiiAK_Nz1QApXHS1_LBxkqtwL_8V7n4ijpmFHvOoTfRcOezAX5O5uGThlGjTVE2-Pfnuru7feibVNBEaaM6LoWMyJp7SfpkPhwxGNpWe4r1jYoBVHk2veIWE4oejlNYfNfWzProFqJqa1ukIrLU3D0A31QGMAb-FnhCQbPsdgDVK4HCk9BIwCsLc2NUo69MuS0Z9ZXDEgaHO-LkLrwxXN-anuEUMUKtp66Ql34PcWQUnHrGd4KIgI5yxzNqF-7hvVDI7qwHUpSHP6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=CWpzLfESfUqrI8misvk8wMOo7fLhXmQhlX-ccwxpDLGbjEE9bIFKfsD_Xpd5bl_ON_8txN_g9p04Bb3-htlO6imk5YHDqFh6D15b70yZnVyyKedysLvavdQgcaGIoDX-ASEIyI9gyjPOAWhMHLeydIgoLvsWl1bQkZ0ttssYAtRPh_xMONxAt-H6YzBIaC9BeUVn5ws8T-V2y7Vwvk1QIR9UP4kQVnmltqmxOuy5F1f1tlAgFME4R-_ULnoDjVxp-VbmmTVH5XsKRBfdhCEs0vvcnIheFm-oIMEe3g6J7dC_eEX-2shC7Uj3_U0iusOmsHNb7FWxH1mshXr_A_TwpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=CWpzLfESfUqrI8misvk8wMOo7fLhXmQhlX-ccwxpDLGbjEE9bIFKfsD_Xpd5bl_ON_8txN_g9p04Bb3-htlO6imk5YHDqFh6D15b70yZnVyyKedysLvavdQgcaGIoDX-ASEIyI9gyjPOAWhMHLeydIgoLvsWl1bQkZ0ttssYAtRPh_xMONxAt-H6YzBIaC9BeUVn5ws8T-V2y7Vwvk1QIR9UP4kQVnmltqmxOuy5F1f1tlAgFME4R-_ULnoDjVxp-VbmmTVH5XsKRBfdhCEs0vvcnIheFm-oIMEe3g6J7dC_eEX-2shC7Uj3_U0iusOmsHNb7FWxH1mshXr_A_TwpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSDLG6qxuRD0P-1Phb_UgdK2Gq7W0tv-G_tHq3aIoLHdYVeOP419LPAwZFEHOavV3p-MkNUxtVdJ9jNPtMdIvfgUDhJP4exBs6k1dIYE3Cy3Oqn39e-k2lMKuI8Ep14l9d3A3yBCF0bGAUk_VNAvRKPm2A5jUOoRbprmEWzlVUtwy8bCcyi169WsPrmHqsbMOO-dXDIw7Z4iYi6t5TCN1t5HJv45RexLoBP-f-UvRI8h8awYafxW83d1kMemIUmI0Wvoy8R6C6MAYwAjSS-66oL5hylX2ISsHrhkxjfQdtbXhExnhERN54wkL7ib6mgCs4lGy3Hzv9oMtX00847iHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFYwshn4PuAnEZ1qngcq2dwN5-ul9GaV-4cQ3gV9iV54u_93LHf0W98iorYLvfbnFBIZRZTqzZJnZqV9ulwULmi9azlk7gg_ad2ChhShG7GU089ohH9qLL5S1F7bCPFi6yHh217pRsgysM7aicgnUf6nKWEg7-E2OgA9lMc02cnpYVZp3OC9ToQNBT9lWYb7xJbLWL7HgmkF5U5GtiGOQWM6cvKknWr0JZ3Xn3faKwWnsTzfdxNPZZ6cGoP2EK8uuvWaFqjr2uQDgjZkj1OYIhgkdv6bbxI1zNQ71Lcjq_7QrP7acyO3ZOkpkOL8LK6a1cPliQ6aFPlc0y7urf5y81LI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFYwshn4PuAnEZ1qngcq2dwN5-ul9GaV-4cQ3gV9iV54u_93LHf0W98iorYLvfbnFBIZRZTqzZJnZqV9ulwULmi9azlk7gg_ad2ChhShG7GU089ohH9qLL5S1F7bCPFi6yHh217pRsgysM7aicgnUf6nKWEg7-E2OgA9lMc02cnpYVZp3OC9ToQNBT9lWYb7xJbLWL7HgmkF5U5GtiGOQWM6cvKknWr0JZ3Xn3faKwWnsTzfdxNPZZ6cGoP2EK8uuvWaFqjr2uQDgjZkj1OYIhgkdv6bbxI1zNQ71Lcjq_7QrP7acyO3ZOkpkOL8LK6a1cPliQ6aFPlc0y7urf5y81LI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2jMDhlDgkfNUGPDl9wkYB4DQGcZA1QUvvXkkqPK4WQ3lCrKyx1L7PSMUMgJAX7XE41xP2AToHe8jb9BL_djYi9M5JViBf02qj9YE7b-Le-BXnCILjLDkDUR2KJBJH2e50-DNlAkCLi1ixcUOSZ1SQoL4AYlLlnGRR0tkkzlO_4ou6zZutz1mSsvYnnRPUF9Wl_UrFWxqQ0JJe9YZ78OD5zGbXsO5pdMDEkt8pE0UWaGcsRYoVP3q4squy1lRQkWVfUQe4_Bl-PYwjhirjRV7FYFoZe8Nf6gafY7YgmhkwlXX34sMxOgAskAUE0a-RCb1eEHlOwzyo9PeaVan7iiJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlwkUUtgV_BlIZMQLGlBteVHkcYVfDmSUC5_BZLDXfSEtXEuFahoCV9gnnbHmXzjdPDg-RtHtWvcr6HwbYwhYmiCuG4TE9A4uEoDjDrb83TWdpQmK7sWeGGW88d_vjldvaagaAFB4OMjb_ewNXqcpIFOu-wNH-kOnaQIAxVOowjF_AAlAI1muD9cOygjoen9vCWqeg3AbZCmDpTxN0a8OIqZqnzoASo--v2KqwKpLR7yvYf7SFCOcCV9j3X3Re7V75sMv3i5TN8idP5N9n2GErg-Jy1tgvz6Tsa5aI5o16CWdiy4H_qkVL90Cp5GSwQUputpuJcdV8fevt8QyOeRzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3LB9DwmW2S89ZwdXzxEOf8pUqb-WKPwzsIjjvbyuY6oMfZszlCDE8iN5nu47QtR7HT59KQ9yhfxlVSUGNQsybjSDvBnNP70PAKI3yYObXwpT1zmgsXaqEzF18NjbEXljEFHKb88bNXN_CPdimHSXDDzpC7p6AX7W9pSYeB6DiZeo4LZ_ynqNxgXu3o1vR_EA2vn8KkG8b9uSjGKa_bta4WYt9Tpy2mnglZbTbuhVAL88mKXd7xiBiFqOGyAB2_kgCDAHVHNn9N5u88dkdDA2Y6zDuz76niPpWjeqK_Y0bVbwUofzDVugAz0MvX7kMLSh9F0HzF6wymgMrwKHCIMFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfpTgt89c3NeFVXi6MsCCJMuozA8Irs_cFyfW4Yjh_R8VQmNa2PMlDRD6ltdMMSrDKSSyIn-Wb_r4PCPMJ-BtlPlRVrCUvNRQ_Wmv_AYBfFKUBNZCpCXscblL7pRvh4j2GJB6_BwzHIwI7i6o9Ud-R2Asm93TbKBuxhgR9yVv_edkX5TnzBGXCHfbYCuYY_op9gdKFknawRUMFnaHg1lNowunGGd3uPmWNCaIS44OVHDE1OXnDAwn4vilfY3xDcJJRvhCuBoPSN14guM9LVg2uIBCgntgNlo-aIoanAo7gA-5RHtppylxVElRLW875p1KRDbSTxJFyQaGMNZZLeWVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/er8bJWaDDHNlWnfspgCF8V1IkGVsd2e5AAbHC55Wnz7wqD-IIHtCl2_hH_ICaj1Sk_RTCPCG9-lMIZ04mVVpvTC8f9n4POqflHC5DMrBI9gY2ogNocbBNdiym9yeKp5Rv3bQmUU4l7J7qLFuaGjo9SerBgJatEzEeLMgw4EZxNOl2irxUnb7H1xRQQDOQINafF2ZF76lvOORXweVHhfL3Hqv6nd-YJAcqnYqMWG7XD5OYLgisOSVcqjPTMelhfafahRcdlelOeJvb4gkjl1cWfHHq10WwVDp705z0dYxDT_GtIJXNBV39GZgHDIigRnloRP6qfuqmapNUc9MgkSajg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlezPZQYwfvHNkGX8gtx9Tzup0j0nyPiF2iUKLuLY8WVmDur3sjSW2_YgZfRl44rGriZQdMEQSAWTTLuYXM-gj69I_iqYXS149_QLHxW1uBLHBJWvX-lfiTF1XaIOJyFG_RYz6a9QwYzP2lIIyC-SMmx8iOS79_Tu5klOrFuDsdE-GhZRCbdloOMF1N8dqT5U-vZdtpad1FyzRb8nbsPL16QXlaPu2L9b6B_SZ_k1x7BPEv3OBUPuJuOc8QbkaY6eg33b6eL4nkoUGdf2Oad4OFE51kaKMcXAT_3pajQcUmqoVvfmDUqGsdw1JoeX1Be_0RWoYf_wi6P7AcHVIa5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1uVvZeEIDf3kGvfz6RcrMXaBNyjZja6CiBnLJeA30Yz-oARfYOudWpBLjpL1JVqoTNuu6Psek5hoH1jFMistOpR2-6NIB__3DP8RUqTw2uzxNI7S8fRvPHa_7AATxKwiEBeSRz0D7WCWREj1_h9PD5vn1ixf2N0tn4N3Ae1HIYVsmIbvF2kgeMTikbHc0uSfQDUB3ICjB_QoS80XDQIZHXN91R8OIWwYSoxqb5M529UzeOBbbRfKOW1bAntYht8ZMcMSCNDbKgaqif3lcunbCherrDzklT0GqEyd_LeRF4p06glkbM35kuso9pV_xLcBf6hu4hwRBddxhRWmjdJxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy45uXXQGMx5xI2_GUTI5C-Wb0DjeYsJ4M2kYKJfrpAwVjkB7cPtJwsjbWzlZGsxn4hIL7P0VAK3gIGlrDRD3iZr1RbqdHJSbTYDWNbw8siqqareyUoH9dLvkpw0qH2mrlAihmnmEPYDuO9E2TQIc9VyggBlYCvoxnfGk7s0vgR9GNaDlJGn0d7ySB8W6ldzu7QRk9MNwdX079qebxzjHSPu4BZ3VcpsfZq1TpIexpc-IYYjfRKLa199NxDMs3JSJkLK1Qe9r0NCls_B2oKwxrkcZrg-PouJKj5AHjD2crNktxRn-WDsyyjLeO33jCYUa6bHrybGpSKLI04bqhZUFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZ7TO3Q6YReSf5kZYT9ipK1oQJjAXmcsFu0C--t_556JdUqh_iGKmpsHbrybyEZBkzrTdPgyj1MxyNwJ_AKG90rApw2bfgAzXmZqDSS7wWlJ7OpQafAyz-e8SbPTmVByQXs-C0Qf9lUIWRPxvcw2IFJoZnZSKk_GeHXGXLJTsnTXOwZZ2EokovnahkPcGgMOA3iDno05NLWiX3GKK0-l_X93pjfi6CSdVxw2Wh8IwbnjLrz3opvBB-BDTkNGHqhtWNr3mzgpO9_3XkSvC9iFPHx0ysSxv9H0agv8tVQ5iTWdyWcVP1KLmYfD0_pf9TTWcjs9iW_NLj6aRumsn0WYRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h5bMBhX6Rs6jYonHQpnWmbUdMIlKKfnbVE91Ut_9OgSesRFn7j2_b4Psh61Wr5zC_9l9vsrm4t-LBx8z91I3QoCdzTFNvzefgC9CeGQC6eUfJvrPZVjWanWo4riKaqVsuc9lIDCgq_vJuxQlqbDN1FEiN30Zh7945WP8Y-pFqsoxPNC9fAbuM761OxkjZsv1qgmtTnHeGBB8jkGTzQX94kS1nTUdrLSSk4P890Wxv3w1djoB8z1K7hQG2bVjmIsoV2KolxqthzSyBvl1Lnhrhb3PYaGguyeLm69_gbj5ecsqL_jl_PSt_gk0ggPf2NhdDt0m32vwIjjCSu9b_EHFFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekQ9VaSefjeeSzB8EOrWAemZQYpx0gRobJT6wchGKRS0euokPS_VFanFfkUWA9Ws5v9pZJ5ZwyXzpEt8p2kKMh13iiDKjHBdOuc0Sg7woitlRTTFTUi45Jb1pLqZ0XcwLMw8Cnn0bLtHXaLC-_kPJRONpuEefAba3b892beuCArGEr2xC8W59ns16H9XplMhmdHwpn3eeuAWgdFgbtosiyp9rZ-uFA6heLrvNFOQHozWR304V-ldhUuQ0lzTf_C7ROBvSckD3tXbb0whSKJ0DtY_2SOSJpkM_YV5DhAwWjEkUr0E8nX9TkrpiJynOIkZ_LvyxD1d4NWLcXZKGsilpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=K7ZGSTz1gQt0b8EeEnkrcP2Z1GvYS2OGD3UGGl9SUe1BIJS8X-r2cTXenkhLXF7IVhrNSp48gajYj9PY4jkELkXUldz9plK_lCiUfjY2R-FbCZ5o7XiMlUK13fam3D_H3NjhN3P1_g5dtAyGvALK3afwZdEJOfRoV6OKwU_BMw02idOiFASeemmH6F-b0dKz5fr8Erd4giTpTLPSWKlMfeBBzSky6NXEPZcGstdf7Pqaa_4ix28rSdPf6TnqQpXOnqp73LZv3I9FTFdyXj4O2K-OX5Leniv-3f2M4cGOeFOVxnxpGvlgY2HQ9RU_FiYkwOzlTcKrwyEv2nIF0-elPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=K7ZGSTz1gQt0b8EeEnkrcP2Z1GvYS2OGD3UGGl9SUe1BIJS8X-r2cTXenkhLXF7IVhrNSp48gajYj9PY4jkELkXUldz9plK_lCiUfjY2R-FbCZ5o7XiMlUK13fam3D_H3NjhN3P1_g5dtAyGvALK3afwZdEJOfRoV6OKwU_BMw02idOiFASeemmH6F-b0dKz5fr8Erd4giTpTLPSWKlMfeBBzSky6NXEPZcGstdf7Pqaa_4ix28rSdPf6TnqQpXOnqp73LZv3I9FTFdyXj4O2K-OX5Leniv-3f2M4cGOeFOVxnxpGvlgY2HQ9RU_FiYkwOzlTcKrwyEv2nIF0-elPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7uUtoCj0BtweDMw02YaBF4jN8qYAcWKcbd_L5M5Y96NJYzvFDzKPOgZ8LmEL0oTRBXOer8FI-mxqL-N6L1JKd98QJjSt5rDHZ6In6tdYU81qtfqadCN1cZCuflG_x4uUeqD-Ii1snRf3kHI_xG6Qdhmuls4n4zjNeSGPCU5gWdWRFadArRMQZG6GkzDRCe_aizhDg5--Fbbt6PlMCzV00t0WbPjeBQuMBKSKK5Z6RxKdSoj8JnUUlbhxch8qr7yBCdeFK4J-IlKej2wwr5E-oNJ_iNwmrSfzOC7y2GoWPjYsIEF_EfmY-rZXQEoCg0OuIdj4JPWw9kUZLbG0uM3DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exMKLQ1HUcfyDn9gkMXvPOJsU7Z-L2JaMlgy4pAVv5F3UG-BJlxEEkQSdz8L2QUkUALRAiDloFjp1M_nPbZFf-BFCvtF1oO16MzC70oNjK2VJ3nGP1Ai4IecatDaudjtfGzKyOQKAyk5XDP3-bzMqr_YYzRneSX_SjyA-DcnQai0QgIcpTMR-nDIF-mLsO5-PyHT0QGzGVLCdXrLEuiFn-baFim5IGJGWlyLCmKfHKDBZ1qGaD3OQpTrXv1PMYOdl2t0tTT7S3G1VWeaFuoSgx1228Rzf4JO1m0Sn5pG7SDODTUy3_Vz-zd5M_r_uBp7QnGjITN11OhUr5fGSKf4Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXxEhMNjtkHOY5UiM1fIyUbMbORVo_-3ChxTsf7LJEFZRhGwSaUN7VRirRynRzNn-iSf5GfnXtAN8B-2FugBwJYnQXK8j4T_gUxyfj2Bd7X7Eh9jgS54GksmCauPSdLcZHw7nfbqP3VzxoqEYsm2oOSbgguTAVZVPP2eYEoaQtSWyoZ_M3uqU4UOFwz2zqHF-NTBGDwR1RajQrYkxwshX28rd-La8dOyXz2T967S1kXkwbkFbQC4kw3XZQNamPrJAhBL9jYD5fA7WSG6X3Qjrz1x4TEH3d1WQOchMQXrcRInjHJBCnGGN14XeV29AoouW4OjM7UV67LeljZjcDA1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛
رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22050" target="_blank">📅 12:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22049">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IG9zlmJzk_dp7qSG3JGHvti_6mn6v_BMDrYLRpLZ5FN63jUVinS8eFuJkjnMs8fpi3em3F6ILY1KHSAcOdsJKzvSac-J0OwuHqQWkD36O6qmPKmcSwuHLCcGm1-UBblvVgwbxWuV-KE3hdvEd80nas1IR18q3UZmIpP3ozu0obWtlvhpApKi_sBt_XcXCtVt0MeJ_K1_Tw8-wqMcfitGFrJjjHYSn5YHJjHLLr5-HkloG33C3duHJrj-q0jlXCfkdiYOuYiI_z4g4nQjboTzhtMdyQGJM6BmVHUwJhrRG6J4HntI08mcz3p4-3H55G_0Q_UeJgE2CTeC1jqy0fqZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5_kKjCiXueITb0Ul1gzNcTsTFbeU0RHXk022zOv_NUuFPFIZqt_DZM9MBO8PrE1GKSccmUkjRNhSESFsRij6cC0ve_r3t3M1O3Kb-HqmG0pSdWI2C3tMwFRI2ASWmb2FgAm4iNLGlQpBOhOorDb3xa0JGo7F3eecZ_EVaK3zu5DiN2kWX54TdUtc5TyyunqpJt8k2LHZZ_-XsJtMDFHTRJhZpGjo5Y4C_S_kn1aqmhboO3AruH2px2la3Wz4NjU_rfYmsLugkCkXMyZP1feuVa58xyO83UrJCNBCIWtzUgQWI-rOTKYdFni2AOmj1NreNpzEHV5OUax1NzPjLxxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBi2UMP1LLpvT1qN9yXCiXEWfPia7H7p96udO7Fy3DlntmuIl78Mf2bvFA18q4yzgNlS7MBS3fcXki6GAs8-Wa7Y4g-xkaEA1CXS3ZXi6dLCiOhTBG-932-N2_8MTyUIGGojpQ5s55DggvEOgHmpZOFMuigMULCCS2a4fYBffie4tzi_aCJ_eqDeSegc9t4MPjsfDFtEKBrqeKrJCHQs1yafznqo0D_cNhSRy0P084X8698CjXVszv7VO9fH0hSfVgZ3FKu6dGLnROPIs8zMXwvHdq-5sNRJvaMkd3jJAgdUyqHzt4d0UXGeWWs65nPTKUEcjbwiV1p_sWHikyKuew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7C_IWe2DDCYGUyRzWFPJ80whv8C28dy_zMw8yfm14l0aenU65W1xoAKBLtcm9Xg6yOIBrYmY6o21v8hZ8HbSnkJbB-odq2SSFRuMT1LDQqXkFhKKsGEKiLTN0F5JUwqRgJPbgFv8cOpHHMF9baLratknN5qS_3ifn30rEpVjcZN14a8c4TVad1pdOUIN_o3KpBYArnmYoijEyNpgioZI5dL1ELEsfRSrPG8M_icn7arGYekYTOr166VYlBUIituSxuCv5i5buLu8wnjGTZiP0tIWU5jJxbpb3DE8iv4biA2vAMCz_w5NcUE1dMb2Ah8TXqxEy0SahhfYD_tsEOQhA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=f252sUTJ5NYsKtzuVwQt7sjT5LBZkHD8jjMC91aECj3Sm-jKkVv1RPCEHVMArV8jZgI-90yt8DhM-Xcdo0iZ_SiSGP3Y96AzsVoxUelY68ZdvXLuh0pfHtzvpp-XRf6GGWJtAsVp5VtquQPW1pliL4Kpij8UoFT1rqvSvP6z3t3ugt633PhZk3QiBsdj8zmUY2jTDmuefAxKTGFVO7-TjapuG4tI-RTl4RcRg75GKD3oini6MiQA9DUrovlq_Q-aJU7kDqoZAZxQXp90QOzHYOXRx09JfZDw79351KoUQdmnvfs6yX4KZpYhVMNTw8Qq3yW7kN_7vVIQGnINNskOdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=f252sUTJ5NYsKtzuVwQt7sjT5LBZkHD8jjMC91aECj3Sm-jKkVv1RPCEHVMArV8jZgI-90yt8DhM-Xcdo0iZ_SiSGP3Y96AzsVoxUelY68ZdvXLuh0pfHtzvpp-XRf6GGWJtAsVp5VtquQPW1pliL4Kpij8UoFT1rqvSvP6z3t3ugt633PhZk3QiBsdj8zmUY2jTDmuefAxKTGFVO7-TjapuG4tI-RTl4RcRg75GKD3oini6MiQA9DUrovlq_Q-aJU7kDqoZAZxQXp90QOzHYOXRx09JfZDw79351KoUQdmnvfs6yX4KZpYhVMNTw8Qq3yW7kN_7vVIQGnINNskOdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله موحد اسطوره‌تاریخی و بی‌بدیل‌کشتی ایران متاسفانه چشم از جهان بست و به رحمت خدا رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/persiana_Soccer/22045" target="_blank">📅 12:55 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=umG4Zw6fXaN91Ykn40Y4-lfUcmmEMiHYjOiwWw_pethzwCG-qhKhQcNkhr-zNJGrcZcKP1cvtmFvcDwqjQPFb-niGkLft64fp4SHi5Pmxw_zaCtXsw6g55q0074tcU9B112JkqoqWmAvv8bR89iewRR7Rq_NXttMIwjTGAfM8uDqyk_WT64usXIU1wQetNfV_CVZ9e92a0JvuG1Zbk3tTeOQo_XEwpdC2xHb2NP5CkL8CLoHB3FRar95ZoEXUmAw3PeGTw2Kjf6HxNq2FfeXvNMpul9UsRswfCefse9ejJLA1WYHg-iiwWMkLx1gE1LvCxW82Df93eNiO42AbqPNfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=umG4Zw6fXaN91Ykn40Y4-lfUcmmEMiHYjOiwWw_pethzwCG-qhKhQcNkhr-zNJGrcZcKP1cvtmFvcDwqjQPFb-niGkLft64fp4SHi5Pmxw_zaCtXsw6g55q0074tcU9B112JkqoqWmAvv8bR89iewRR7Rq_NXttMIwjTGAfM8uDqyk_WT64usXIU1wQetNfV_CVZ9e92a0JvuG1Zbk3tTeOQo_XEwpdC2xHb2NP5CkL8CLoHB3FRar95ZoEXUmAw3PeGTw2Kjf6HxNq2FfeXvNMpul9UsRswfCefse9ejJLA1WYHg-iiwWMkLx1gE1LvCxW82Df93eNiO42AbqPNfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوال عجیب خبرنگار:
اگه تیم جمهوری اسلامی قهرمان جام‌جهانی‌بشه‌چه‌اتفاقی خواهد افتاد؟ دونالد ترامپ: اگه قهرمان بشن باید نگران این موضوع بود. احتمالا تیم‌خوبی‌دارن. تیمشون خوبه؟ نظر تو چیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/22044" target="_blank">📅 12:52 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22043">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8o7lhiK_ovRpVx2NhGtt9DJL14lVVBm3gV9KJVulLoUiNynPBARxi_jOjDOYMNhepOStEgFxJZ6372CgCtO6tAwMqUsm8Y4e38SfJqx44QvmIw1vjzGL5QH_vRt9NceB-J91H9J5C8T6fmCeovirCUSgc1fSp3tTcl1V-teVzcuiWryIkmq4sm9NtgDTUNkGRl5n_Yc_BiCn2kdGqXVyi0zpyqTqwGCjFUgaOuphWiYE_Mo7hCDqea9JWDNRAThVaydk_ECB7a2jymPiFcV6goPiEnZrpNFcTnwHb8UA5lomd9x5Y51FDZNLMbTE6p1yO2KR4_IzWeuo7ApG6i3gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/22043" target="_blank">📅 21:22 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTRPUnghkd3OJpceCeb5XoHLJJg7Nf1H26Jw-9y7RkXP_ymsZhZlLK1ouBVnTTzllxKBP4ditibABLyzFwe8ZWqd1U8etDS6Ju5UEWp5VuCSB9ddOJtU3OG601JdVNxR6O-CAoD59-qBi4ukql-_FYu8RXAY7rfFxBlgLUQo768loDcirai3UfmjB3WFyzBwwLCospS7MKX8vfe8CbxLzgAEAopmwL7C3daXbmScRwmyjL85pX5FIGIRAletEIke58QtDKfz7QmKzkaUsjjgG98bZdXk79OWC0zROF32wYK4aX5HUSlH5kDCeKSX1VMFr04L-oskVkb5-C2_POjQcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/22041" target="_blank">📅 21:17 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1-mQf4TlwQSLpHONJ0JttES63nHo67Bm2Oend4enh2-xjhswcdCbq62bTMkp2_MuFnAL-FSFrpETskxR8VmzY2Or76qDLUpknptWtzAHhFi2DU_Gi2gxJDWb3EHRUSrBeXzyWVgjVqBW-htNSnXTZoxMGNo84h3qCbUDFrPUyw9r2K3XIX1Qi7T3A3Q4XYFs3UOYPMWzBSOMJdOV7mJnE2iOpuRRN1WLH7yXxlgqoy5_mVwhuY5ZM_wIaA9LQ_2JwIc4JEILRA1FeyXEGOR0WS0eEfPc9N5r3bDa48FO6eMdW6kXc9g5Gc1-v_gdIKgOb0LB8tm2TFZBC9SSQDRRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلیس‌کانادا از ورود مهدی‌تاج‌وهمراهانش به خاک این کشور جلوگیری کرد و آنها کانادا را ترک کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/22040" target="_blank">📅 21:14 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22037">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGqUyfXtXh1We8BPrYPTItZ5AzVJ7v6Eh6Mr8w0DzU0yEvFNv94ZRvLMw_XMytF7l0MM7NMkOb7B5P43AY3s7HOSt3VIdVF-4MlldMxYOCQ0Dq7mAo5Jr8NyPto3R63-b2OfmX_MP6bAp8vEmW9Y8HM7lQrEA9SkfYewBxWcNB6yUry-gqT_LXocsdq529B8b1gS4nhbFKFJ1UoLEmfMhIBRRDvm_lB8tSPKeuPi-Xe6kaEPu1rqdW8AhQagapYBMCCCYsYe71998gU7eltJ1XcmtHnszq8Ey3j-yIrDsteLX75TfV1Fnsyuhr5lsJVmOduq9YW_QW4-qMB6b8wKpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تاج رئیس فدراسیون‌فوتبال:
اگه لیگ برتر برگزار نشود استقلال رو بعنوان‌قهرمان لیگ برتر در این فصل به کنفدراسیون فوتبال آسیا معرفی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22037" target="_blank">📅 11:35 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22036">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0fEviCI6TF2nqWyG7-UNBTHUZpM55YEWvcHjTLWQ--rHSS5cU4SJBL_gRITrZdkB7gmhhMwT1Ud_eSj0Njz5p6tKaKaTvnTGBuXJylLzku_1Vdm-FQKQe8foXyC-Sj6l9iepmVhtbSPs5iUzf8v6fPoXUTU86ReQVhAFJHbozJBfMkbbxc7ZkLODgCFLSnPupHWNJxbQdM1AnOzgMrgu-g4C5MLLLRAf8JVXgGbXn4jTnV-X3AWgLwmvl6rb_sL2d1xNPvCzc1WzRmjx60M93zQkYaqxA2cFUC23Hx4truuqfjO6JsBv2iWvwtK32awKWYnAcs2Z1eO5MQb6RzA5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجمین‌حضورکارلوس درآوردگاه بزرگ!
کی‌روش با غنا در جام جهانی؛ کارلوس‌کی‌روش بعنوان سرمربی جدید تیم ملی غنا انتخاب شد تا برای پنجمین بار متوالی حضور در جام جهانی را تجربه کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/22036" target="_blank">📅 11:27 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22035">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lm962c20-re6gel0UF3qhLr0EWvUHT5EDu4JGtVebyI_uk0BM_zONPRmthZgIrlve8lU7MItaMOPlx0U9hp8BK-AjBUTgPjxsCLaqlIxGNVkCsgRiBDFxo5Z2vAvC9uPlpWm3GDR3Ppmyuhubk6vYILcvhO22m9gApU8MBCF65TdQTkhj5jwgfrjw-M3YlCAFgi6MBYp8W62lRF4JPLVOQPHa4DY6lwNgF9is1EQt9tADzQKc8DjpDOzrPhLxC4bLlq87eJqRI_uyfcV58WW4bxQz7FJJjbn-IUIWt5PAv027WBgpenkwEss0SohkZjNNj37GuBm8OfsHtqhZmQz1w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=Yf0cQw0KR7WpTLwFwaTHrr0XSBPz09nKqArIetvGyoUBtIhW6155CIYwWBf8g3W8imNsmOVV0-0D73C5rgqct18btbgKDGuL5q9nyfCXgrS0JuKvwYRzc0bYyM8YNyvc7orhM_pX57AkXwoDGrVC8Pq4zpXEYHp1R-BEkOVR_3sE9THZj3aIrubMQOTmbtTL4NBzdVSkhT3bJWTY152v5MXPiOzRosFybJq1MmjQuKWZpaIPW4gunMoZNO_XifLWzXc3dTV1K21H1KPQvByUIhRRaIEHpF2C5QmeA514zmlgzooNER7qWjZSuRdmPG5VOQYYvxJck6esFxYC6EwaqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=Yf0cQw0KR7WpTLwFwaTHrr0XSBPz09nKqArIetvGyoUBtIhW6155CIYwWBf8g3W8imNsmOVV0-0D73C5rgqct18btbgKDGuL5q9nyfCXgrS0JuKvwYRzc0bYyM8YNyvc7orhM_pX57AkXwoDGrVC8Pq4zpXEYHp1R-BEkOVR_3sE9THZj3aIrubMQOTmbtTL4NBzdVSkhT3bJWTY152v5MXPiOzRosFybJq1MmjQuKWZpaIPW4gunMoZNO_XifLWzXc3dTV1K21H1KPQvByUIhRRaIEHpF2C5QmeA514zmlgzooNER7qWjZSuRdmPG5VOQYYvxJck6esFxYC6EwaqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سوپرگل تماشایی در بازی دیشب لیگ‌مراکش که احتمالا برنده پوشکاش ۲۰۲۶ میشه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/22034" target="_blank">📅 09:07 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLNAQT1URJ2z_HXFm0tRBrpjkfLA3EDxEoTKPAkowgKt2OkeWGAU1pcVRRdM2hiYy6T9Ffffbh5DeoCJp46HE7tjoJJkrMGYZK2SD4yKKhXDwvq7KB8Os7mDwBWXOqmaeWBosNRD9O_qXtlo_wLWZMK8bsi8aJO8XWf4CGwybu6AERW6HJGeRQWnW5dzJZaRQoP2k3y9wxCqqWujnG71e0ZgEMMhQPZrmDGmweLz7KIB4B3Y8wWtRnikx09bNDlDT9UMU3l7h3aChQJnqqXYa4WX2yhU05JXOV6m3eOiz11B9KTncMmUVSLhIce68NC39ewPHeHFuymVAFeGlM5M0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSBoU9S2Cs8Gatt4sJTqB7fOCDLz7QZ0FhGjBhRFHbci6RNnBo0Siq9Ac7gZvMerD75FcUl45zkq6j0cnrgXvmb-ofXUedVzNIcuSGCUPqvzzN_QugllXl3oAMjSCpmxlOSqFxL39Xt_zYhheLSt0TqzHv0kwrNcdKcWgnq_NOXqqOUav_nh7apD16R_Dvn8P0npSg_Nz6MF2i7YxuGR2FyLp5_fozleIeB4VM3-MtaeVl0B9MaQj0yVhoM0SRfyCVAhSOFWOUpeGj8rhB1LXK1yZI0abMJbXAzlTo4hbODtdQFHq2AVOcs-_6sYSug9HmdmQ4X2uScFYKyP-oO3qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چهار تیم‌ نهایی قاره‌ اروپا که امشب هم موفق به راه‌یابی به مسابقات جام‌جهانی شدند. ایتالیا هم برای سومین‌دوره متوالی از صعود بازموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/22024" target="_blank">📅 01:10 · 12 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdIyEs1gsBy135oDUIbZgOPPCxfclyo1LZGuz3Gcyhq4iLwpMWbNENJZqCNPidMuMldb6u-bToHoXuWWOOnMaZ0DfW7BQ9a5wIbI2hV2A_uLm28P543uyIwcq7H7HltLvFY7HgeGzhJntYyXHiSY1vOaQrjKH0BgsMkK11xFLt_LZIgzvywMrBJVuEQcVjJtLmYi8XHa5wQKrFm-Z3Fg2NNUC9rRQeQfAZrvL7iiTRbs-sklYC5_LyPheMA1FIOo6ogXSPJpPachUbwtIPV8W--r1IR0OziM2LGUgt-fQxCcWCMvYi2LkBEeW7oeE1dGp8deGYRp3w1YuLnXIou1bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏مثلث رجزخوان‌؛ یکی‌را ترامپ‌زد، یکی را نتانیاهو و آخری راشریکی‌زدند.‌عاقبت رجزخوانی بی‌پشتوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/22014" target="_blank">📅 10:29 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aThfXG8EMsXzJjM1zB38WvEvCbR8oIPCd8hMlelWRSuVymZr1U85rUc-w5BYX56IcaGlqq1VXgUeViYUpvCF-es7Hs9oxxn5GHPtbzTrSTcG2ssouEkBTLN50zpMpnlUum6bHrmGiH33ddRjNcY_AoONfwPwAHdnm8awHfzOVELV5eIw_sdkJC5LqOT1K4XH_VoPtEMKBZBuE7aKnjSane2fPPNCzOn-Ta-Is-ss8ZGgzTUlDEK6h7gUmvEcDbqE_vIhryAGwkQPa9TmLJH5Xi_w7FiXo348unxYTSrBvf2pSRE_JfNYrkZ-k4ALi1ZKe57NFOe973SQxLS_7DS8Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22013" target="_blank">📅 01:26 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22012">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxAC3FT3nXPP8HA7WX26jzTRlySSqA1VMiwx8Stfbz8k27wFYIyzDVHl4gBZqUz4-QzJQjkGVpcGt9yGot_4dh91loHyVS-GQcbkYiynPXeRL0ACJi5G4chrkkdO0jqSM7mRCs1MVwVj-CprH81dQev6Yt5BLvPC77zX2PeKGBu9wtNPS71_nMdlV28JS1WDwc7W7xzy8YhHbfu9e8yFrznhjXgWWPIRFe_2WZIq_DBaJUm6T8efr5UlZ0gkVrXnBSlW1Q_nrqKmBfEcJqB2T0R5rCGwLHLltNwu_j3wNWVoeRB6jnXR04h6pHqtsFlnfHG50nVMQ96LQ6Lu33KxLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید مارک لوین فرد نزدیک به ترامپ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/22012" target="_blank">📅 11:23 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tta9s0lWqgxdMu9U9Kfg-fEO5giqMl81a_MKa33UvCaG918chqcW02_tPkcrIu0_1s6zonfODrPjNf9vAKFAfmsalhquNH6R4S5rMXyN4-P4gxm2Bi0i5p3Q0_fFgz1mV41VcgXrebpuskTZSm7IHLo6sjXdiRIyUaNWcgu-PvKKIC5i_PNoe94yI6bUSX863nfyd0OWoVkTCawci4lWKb0UAajoqSzYZk79XzBErMGReVhvcemPvapvXuMRHujqWeNzMeddwdHvtL0XpNCU1kHTnbEnF-EQXQoYPh-2Lhl92ZrC50qmeWkyX4f7ZDkKdJs_zdbC2wrYF7yZ89cGwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گابریل ژسوس مهاجم برزیلی آرسنال کل این زمانو صبرکرده‌بود که انتقام‌شو از موسکوئرا بگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22011" target="_blank">📅 10:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22010">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_qcGuDiFtz9Vjiu0rmLzWMdcgl7p1K_RMGM_U0meIDtp-fnReqS6fOSOx-_q4ElOayRKUInTHS5FoZTomae5kcynBy5B3a_g3l4UbHcUC4zIgYdZQfCJ9pCOXpWNQq1sID3tywZPjz2mnEdp7ReJmRIAThb6P4vxQGctWJPkd2orRiKidnYpJY29rWZ5o7ZY3v65OrQS6lsEa0vDBCxalO1Zn8HgCaez-suBacD6_fDtzBM4NYPq12vzwzqd5hUsYY_c9B-LgJpg2JnaMZsok_VMQ_o7jRhZCJUL5fZUwfcJmt6I9IPRbppZxIOqjkjxMFpGrch4pIjsRm_-q84mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22010" target="_blank">📅 10:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22009">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf8dgO1mguxpdv4ntPIlgOI2pAM-wfKRFYSPryJO2CIm_XnrxogiO08fYafbqkJx3D91Is-CVECojjdZRi2CrG_adjNtyQB3pQI4o6JQJBJ8t2QJJ_SUaqUREMNupfgQFWHqf9BfHqvFhpqPHmZznslyy47zuddwGvwDDA_MhbgDPQ3mkRs6xPQ-3RD7Fi-XQ1IdEvS-AAAQL1Q2wsJ9L5vsa2ibnD0bSJKrySKEdkGYAcbGoUX3BcyalW4pXKt8AiyrvswtFgxOwYvcxodJSNtQ1nSt7l0eNX26BPLMP3-parwNQXlO7nzUi2kXdVKRzkgsa2wRVJ4fBs1783Ppuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uryQEYVCFkMTmvtLN5y5UHvHy6mbzMSB-LMsmvRsfMS9_n9AucZEEtQXvCIqZhRCDmt3-vyxMfZKOL3IcXKhcgnr8kTKImEFc1PEgXofawyNTGuCBFeO99-Gft_6uDpJwfMNAkj5UZVM7QewdHrpp0YVzH2K7l0j4FWBL4E8VgeDl-tcAPWwo8CwPvAIarn4BY6_YoSO2U57osiWFXay07O6XpUfUjT_qSTB3JxHWJJwY0vZrtIMf_7yLA0gj0troXeUB_-mbxh-YGSEyv8ucTjVi3zzgkgbI6P0CsJmKDyGtES3-zubCERSJWDJ80xveH604GHU0VVxKKURjdQYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22008" target="_blank">📅 09:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22007">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnPWO_EpB5vEWWYzhGTnB6eMFgTbN31PvqjGrTOzZZkF4wMdXKbehlx1jSpVCH0YzQrPNF2k-xOaq3SZUI68HkHsetVtLxGhdvl7hNMj1s2H-W_pQXZzKzrj_KlOrLLxMqhbwSXMdjxyQyuNC1bP5_Pd6ohcbn9PfAOY3gnLmqpU9IxkkZPQmb1_y_CiwSRP7jI6HDcxCjUPK0R2B9zY3vMxFMbbLO_aApcMpz7be2CgvAxUJA0ha1xE6mtwM5XEsUDEO3X14gBcyKsWy2eu2rUIY1TN_25mlODmtaDbC4bVMXUcSBAxsQZLekQHdV4KgasER5BpYyBiY0JZPFMdiw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=a_EOmzqwsjV4-Jvf857mDJYofh2IrlX9UIpR-3sT3OOmKQZ-08kYceE2ub4Ypq-NhRRtlsykr4srYSvLAIK3cYF0YjwH17wE4YPWJih-2HG0jeLDOhUPZM-0bwwdGgZAWzepRJZPA46sD0V1W8Fz9b2w9Lf2UPhQskGVriU17RLQaW3aG6Ms7lhTDWAI5ElLJFQUiykFvcBAaHo0TlvmOjrrKzLVSynmZvzSeAe4RH08WKd23tzRChwKU2Gi6vmr7EK5O3PfZzGXsqaffViZxGrY2uKPCqY2ynj6ulKcQCPyz7OmuZESnbuos5HZPQpMqyPYQcwZzVw5r4I7h5ko51q_NzkfcueoYTGvouY5oJQ40Z-TNEmZhVuwvPgfW16DMwdjAx9-Jzii1lPVuD6baHv-5j69xXzTYpPosAkq_UTVdzEMOCDoqfPuUts2pHBo5niD3fzrtJuGNKthnApMOU86S9Epj-IbsWkIQFua9cs7uXxkKUnIbAJuBscDkgvp4FGebFTy-3eutFQ0udwBv7e-JT52uYSGf8zKIcgpqrnb2PstfXkzXx22YEgF1CEYL4pAh8H5iDko-f7h7xoMT_mDLRGsct5lW4PImGa7WoyAr93vF8pzOLUQdUuiU5JJ9evJ7FuwCANv8BVwFPExAR2BjKiVzAR4JecMljgBV5o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=a_EOmzqwsjV4-Jvf857mDJYofh2IrlX9UIpR-3sT3OOmKQZ-08kYceE2ub4Ypq-NhRRtlsykr4srYSvLAIK3cYF0YjwH17wE4YPWJih-2HG0jeLDOhUPZM-0bwwdGgZAWzepRJZPA46sD0V1W8Fz9b2w9Lf2UPhQskGVriU17RLQaW3aG6Ms7lhTDWAI5ElLJFQUiykFvcBAaHo0TlvmOjrrKzLVSynmZvzSeAe4RH08WKd23tzRChwKU2Gi6vmr7EK5O3PfZzGXsqaffViZxGrY2uKPCqY2ynj6ulKcQCPyz7OmuZESnbuos5HZPQpMqyPYQcwZzVw5r4I7h5ko51q_NzkfcueoYTGvouY5oJQ40Z-TNEmZhVuwvPgfW16DMwdjAx9-Jzii1lPVuD6baHv-5j69xXzTYpPosAkq_UTVdzEMOCDoqfPuUts2pHBo5niD3fzrtJuGNKthnApMOU86S9Epj-IbsWkIQFua9cs7uXxkKUnIbAJuBscDkgvp4FGebFTy-3eutFQ0udwBv7e-JT52uYSGf8zKIcgpqrnb2PstfXkzXx22YEgF1CEYL4pAh8H5iDko-f7h7xoMT_mDLRGsct5lW4PImGa7WoyAr93vF8pzOLUQdUuiU5JJ9evJ7FuwCANv8BVwFPExAR2BjKiVzAR4JecMljgBV5o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdhHs5y1pjBLgjV3IFro191lExmCXGqUK69zsFeZTA8f7tdS1tw9HyHGigUsz74x3FomXpX2vg0mc3REicI-WICSfP3F0xY3Vfu7rw3LVQmRYzmthW7fP_iuW3Ok297uHmbYviQsP6IXez-qTGN9FZfh0MIOnWC5YRAMPR0roSFBNfn6KJWVd2gKEAvrw4bZaBNudsD6zkGm2hlWdCTXFCxG0LoxqpPaTi23PGjX0uJDKK_DlKCyGW_KrMomwFmvta8nCd2pnNix8YsORuWNnYq28Z_Jk0MMAGkSFhL8cW5S2H7CzpOWCLOq8BcOeCfdoxdGL3jnZ-FS2OB27Cvrww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛
از بازی خانگی بلوگرانا مقابل ویارئال تا دربی درکلاسیکر آلمان و دوئل شاگردان اوسمار ویرا برابر ذوب‌آهن در اصفهان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22005" target="_blank">📅 08:04 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22004">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFq7Cj9WJs9oaAaCyGuQ94Pd2FMEs7-EJU7Z0M2-ARiqqhEW10pANAJua9WxmjtOu60xEQUkYIlGPgGtEtXFi8ues6BMLiNvsBdI7zUDCsvSMGwXfO1S_mXP1KmZPorczAhB2FrrD6KTktuOmJk7IXypOar_pDADdFqj0ZuY4teFKJCwK7ZyZUWQ_ClYG6mKjSzChgKLPW4N-b0k9FhqsYtZVtKEHP5Wz1bTUMguDlffodxs2rnHcYJynzNxg7aIYy9zdj5AsaRxaA29GShOtCDPkMQXZPmAbzUDeGKkibEjt0k1UKRkGKO_nzIYS1Undde_U3533PpdPlZQOpyp3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌‌‌‌ دیدار های‌‌‌‌‌‌‌‌‌‌‌‌ دیروز؛
صدرنشینی آبی‌ها با برتری مقابل فجر سپاسی در شب درخشش روزبه
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/22004" target="_blank">📅 07:59 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22003">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqJYfDDq3ipatqlU5LgUsL4_Xsx3sX1tutzykv_uMHjEbu5L5iNoOFCsnY-cOickKavalr9PDr1_FkYFzwTWUMk-i2l7U0K6Mbdzwci2BaVf0cfuoWLGccWuylViw8WLnUaQHh1um4ykOyUyLOZDZf4Cb7hEV1CrAreYnvafnHnh3cmL3xkw05sVQ_3ZWFXk3gw1ahLoP8VS3rRBPllwdC8XAXFeIW6BEcTUUCZt3V45bo_WUOsNU_fMNSIMlkbiV_FFwT7QYGid-eqtzI_0ynfOsamToz_4DB46vWbq1JjcYj6kQSN6Vw1kaazLEORZO1P_3qhKzWib2ruPqwPp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین فرد نزدیک به ترامپ: علی لاریجانی، علی شمخانی و پسران شان دریک‌ماه‌اخیر نیم میلیارد دلار 500میلیون‌یورو ازایران‌خارج‌کردند و به‌روسیه و سنگاپور بردند. آنها از ارز، پول و طلا استفاده کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/22003" target="_blank">📅 00:21 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22002">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S75SJ3YFxkthuE4dNgiA8EECUfVpygcdZi-2kiDn5Fqr3arX3z09i3vG0krDyvgCM0RL5JcJmDbbiDXWmkUsg4hFjF5kY_c6q914mJOWf3ZpcKHa-lZTUiOU5NxSjq0aFmum-FAB8TbcbgPtcBI6U0l6_R5gat-pgP1o6Ovdia1gm4jhBkxHXs-n9PdCWZyB4PqDBrWNvI-fmgmZWLoFpg7SgYVtZFY3xywWYPci6Zn9bLgRI7XRHI5lzOxB4yyc9rAQTJxMbNxiiJ_HzhHZTdkBLC5ambQFKk4HcZHx3BNWmncMh5pJTcC1bnpHUuzAJGEDKcMPDRGkwV-kk3fu_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KS29L3mCVXev_nnNzHgiSx-oBqdyajGCqCSVhYBE8J3Fchix3FuZoby7I0h7zy6wwIAlYQ8zNP703jDQvl4tovn6OUkvVfK6Np_g_14BtDBlSibnU02WNHGPJiGo_QYgecsE5E_KTYsjMkDbfYvYxmQFQgc4dWq4mlq1RuMz8OIJIoL7vSyDThyzoyus7VUrlUrTgH8mN9y5-4nMoyviNKJNH8N9PKflB7zepRKflLsCfPyu_kWot34SwJvFkw6qqMGhrrdGeggU5TKT0uEAmN13cYYKD17RBIAS3rd0aeBQr3YV8_s3qucpEHwv0qXdZGaG1WS5WxU33zA3Z9u_MA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=bEZO1s-1peHDRgiVzbhIO4W4QsNdh4rqLDHMDUqeyOtlwq9m9lNWKFlrBHfbfROfzCelI5mFdv82OLqNqzQHFL7bFZut1UsSqvA7Z7WMI1TrhuVNIilXj6ePNz4ePh23jGXrSPqIOYzPA6CIm7Y7OXg67CSW853Py2YCw06b-Lnn2S_GGkGriyskMuRpw8J64INyv_FXwnG3o3105Qyge8KYBx_hhEeFlclMLpwCCQRi2U8arqYOI0IG9zc6qXw0aJDhUYuAdwTj_BfA8EPvJgbt-fG4Hc2PUKLcQ4uKsiKhnjFN9PZp3sl8MWS09c7MRM2lm72csQra_KJBKeB45Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=bEZO1s-1peHDRgiVzbhIO4W4QsNdh4rqLDHMDUqeyOtlwq9m9lNWKFlrBHfbfROfzCelI5mFdv82OLqNqzQHFL7bFZut1UsSqvA7Z7WMI1TrhuVNIilXj6ePNz4ePh23jGXrSPqIOYzPA6CIm7Y7OXg67CSW853Py2YCw06b-Lnn2S_GGkGriyskMuRpw8J64INyv_FXwnG3o3105Qyge8KYBx_hhEeFlclMLpwCCQRi2U8arqYOI0IG9zc6qXw0aJDhUYuAdwTj_BfA8EPvJgbt-fG4Hc2PUKLcQ4uKsiKhnjFN9PZp3sl8MWS09c7MRM2lm72csQra_KJBKeB45Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لیونل‌مسی بازیکن‌سابق و اسطوره تیم بارسلونا یه‌تایمی کاشته‌هاش حکم پنالتی رو داشتن و تیم‌ها به هر شکلی که شده میخواستن جلوشو بگیرن اما!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/22000" target="_blank">📅 23:38 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21999">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpSkNLvG-lCY9v_0hh9TnH2G8DzXQnXrGwXl3DErDkOkfP5t7zv5fPymoHM8keGEU2y6XL_DATQrsmDIiNznzWqUcCvsbRZNzPvSS5Xh8VfUrVF-7QvvTEaCo0V7GFkm53iV6I15OhXxhzr5pJOsqdj6hBgXwR9-g3HMMW3H98ECjr8qo3CHwvukm8xGxf4w0BeJ-SInmRDYzNmUpYP-JPUSEMdUdWlC4gMxCBGSvsi5TeD301OaT4A9mozWbaGhh4X5O9gzDByq6fImm7mYwufr2D8cEk1ZrbpCP6I2t9irwdyagwKM1TKa0m-faC1eZaMIpsgdP0ZzEay1mmEgGg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=qDPNgj0syY8DBQYPibIUM11BTEqoiiqIEoAK3H72tXBBG9wM43GGmdOXr_opLPpI737mb3t99ITDxSO51F1Wr5Mg5NnGxXQ51IXCWCMBuaU4-HmNoWI6vFVvuOpa1Uog0wV4HOC5NREv5V6N5Um-2lB7pYyPxokgoedkkRUhOtUCdghW_nnSAYNNcGRKuySp7aVJYio81q8on2BydmrpXj0vNbQw8WYA4qjAwP0K_ShlNgCimZB2zHlJvSpTNiX8i8psE-nQxMXIEI6CyeGOLeS6ibDaAawG8npIDzKqmFIM6JW07EWc4ptJHZ2yq__k8YpbA5BsAdPL6PoxX8XT_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=qDPNgj0syY8DBQYPibIUM11BTEqoiiqIEoAK3H72tXBBG9wM43GGmdOXr_opLPpI737mb3t99ITDxSO51F1Wr5Mg5NnGxXQ51IXCWCMBuaU4-HmNoWI6vFVvuOpa1Uog0wV4HOC5NREv5V6N5Um-2lB7pYyPxokgoedkkRUhOtUCdghW_nnSAYNNcGRKuySp7aVJYio81q8on2BydmrpXj0vNbQw8WYA4qjAwP0K_ShlNgCimZB2zHlJvSpTNiX8i8psE-nQxMXIEI6CyeGOLeS6ibDaAawG8npIDzKqmFIM6JW07EWc4ptJHZ2yq__k8YpbA5BsAdPL6PoxX8XT_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/194acea631.mp4?token=vjKvWfRauquQwu8mRh44Gz0M5wbflv6DZv__uLvx1EV2trk6rBQ9U69HEtB2PFPzLFF-4KykA3dR-HZjYgsCxaQVmvjkqYzTCzbaL674ZIto6sO58jA_lp2bkWgdz0f0vkNqeL4X2JR75870wHUo0NuqdXJsExpojyF8mz0EE_ar2hHI-jRV-zTTepMw69CnvjFI25HTftpIB8SHF2OzowqToOuhX17X36mXPs0tjPMTi-Y1jIm9t0sxK92H59DeHNnndy7KYaC9fUu5w2qx1siRSHzEwOnR2lExMcgIkGAklb3sL1SmlQNNTtdj4m5yU90XV-j2s7LV3wjcqQN3hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194acea631.mp4?token=vjKvWfRauquQwu8mRh44Gz0M5wbflv6DZv__uLvx1EV2trk6rBQ9U69HEtB2PFPzLFF-4KykA3dR-HZjYgsCxaQVmvjkqYzTCzbaL674ZIto6sO58jA_lp2bkWgdz0f0vkNqeL4X2JR75870wHUo0NuqdXJsExpojyF8mz0EE_ar2hHI-jRV-zTTepMw69CnvjFI25HTftpIB8SHF2OzowqToOuhX17X36mXPs0tjPMTi-Y1jIm9t0sxK92H59DeHNnndy7KYaC9fUu5w2qx1siRSHzEwOnR2lExMcgIkGAklb3sL1SmlQNNTtdj4m5yU90XV-j2s7LV3wjcqQN3hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش رضارشیدپور به فحشای‌ناموسی عجیب و غریب گه در صداوسیما جمهوری اسلامی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/21997" target="_blank">📅 22:35 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21996">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9P_4Fcm0X5s41PC78rkDMwC4aCS21Y31YBrgDh0Knb3e1nWmQDOLzhPxztzdze23kzVrrHhZGoElHHZtJEdApFitrMmQBDIcX7PYiL2BJnjcYXj5QDycmubkmfMV4Z00qiNWRJw_A9hsomUWqj-55oFeYPTE9KrG5F2Mt7oiuIk_nPQbqfI36s3aoEpcsiZ3YPfH85HyGnZml4YGDL5PETupWHqZPb1EQBpV4zAda4RAetxjOcE0bS2rAZpLd2rjqJxT1YXXLXIIvp2GL3OxwQcToYTJmC2GvDQjob2s_mwURyZftb2avmGPnSmzfs3DzyAcjuVY3CBYKcOkCv-lQ.jpg" alt="photo" loading="lazy"/></div>
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
