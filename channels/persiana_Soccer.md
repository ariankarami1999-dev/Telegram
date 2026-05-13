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
<p>@persiana_Soccer • 👥 214K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 17:39:47</div>
<hr>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzKuMUwsX_OEQ2A4CewD8M853V7kWTjegvX4Jyp9nEl1LBII_rZPOhw8hHOtTczbV14JgxLLpTWJ0kMrRmU-6-IW565OQs1XQSBJ869HlVy6BQDQM4sFeZ4llP3K3CyJIswa2oyfdfgXZveeyImfTsyrraodLrzeLPWgiuYFqIjJWeJDFuggISAsxrh7CndpeACN1rvlQqUAZ3qj2ulh9Jtzj-ZS1sdB0GoMiahVjPD10BoyR8HcQaeekPFGaSMvBRwaLq5itH9cC4LUi-Q1JNffsSfZOpKKfkZSiFnxrCcEps8tKEu4d6GcnqaRD5CxrOBaWFPTJ2LUEo0S2tbwAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ien6wdLFa1M9xhYdRin8bGZ0aIfXR8lF9ywnVH7IrtDREzZVUtCrrJLA55akbk8clB71c4WfzJbnI6zzrXZdC4ILzlz8VXdL13gp3wa1XeUELMDewoUzYC7RtW0S7EolLZgRZzk6Rc79_7dAqS5XR5oSK9nxZLI_8fyKx8Pjrr-cuE_m8Ilfr5E_Zl2Iz2vRh8kYfMJdl1B6nJ-6vZDEOnxkQc0rDokW9N91GQxRcaY_n4hFmhc5WPIzz7fTJ1qp9IzEMpvSpsYs3FpMO3SLFU8ToWSvb2qeH9-JMUvPGQTya4jA0VkL1NKQ8y5eKNnyfg7thQWlpRDOwgCgIMEQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRHynLFx9ET21d-pFx9x5VAUdI1dNQ7BXT10fJmYPLDYUJM_i5C7rKLq0Bbk6NaU4RwF389WTUqBQLI92CHMNESpeXbGIN8YBeKLaTy_jT3Qn7gE5Ex276LD2GQvJhDqU-yDrTh1xvpRGsL5r0zYzc30aS7zr-SqwtuPbDjd9dTozA1skvnOJy4qaPtCN8IzZy2N1pM1b63gZusB1iQXvX5j-19GKURhIQ63rEjNjudUFQM9KWJmGu_GTj3wPmcZVhPDxuT0oA-JbMsuZTn5Oi94p9ocf1rwqflwetq_PPCGw_lrHI5gTaSWtZ0jpnUqmm3oWkWKNmTQ8NsbT4VIiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSTQjJQd3hPXHw-lWMtIAIkfCqcMMqFi8cxi4qD9ovk5ggS2n2uOvoL84HoDfyS7ibQq6YyQsTGsSHJyDpVX4eqwYTFv2q-qK-9sf_fmsTPgulIV7nXQGGwieRsmaoyjixIrKE3tDlbQ40vOHiySPe7o8d6q3W_qrIrgCkqxsahWvF-TzpafERqqh1Us8pVwXn5icnOMqgfsz6IAj-wmZFogjN_aalBzKt0UHIPbeO2SjdWTxM8OCQ7zofvQSErZaONlmtAbLza4zDTI_jcdVbp_s7k4NQhvOsi0ZreKumhnMO15XEzrhKZFaZn7oi0wkKohwTlps_L21JW8hcphTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22120">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/persiana_Soccer/22120" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsE0fViaXWZiWNyT1J16v-mWdfWVyweNwBYkdSk4ZHKE5bH1ZmAurZ2nyat2sA38p8HjciPQy2k4uNsWHkHPLilNMrpGcO66QRsnYT5ieFlfFEIuj_gYCthPG-aKiyVKWb9ODugJmXgKKq9KukKPUrzQa5QKlu3PvrADBUV50q9jzRfhTiN3k40SrUp004BKsWStzKv1YGMmB-m8Y4qkrv1WEgsAba9TZsw6_rHWseJqW6qTEMygsevmv0fVkHEHuTYSEiznxPv9VXyYLuEEaZvoWKg-fJtJ_EHEYSFq6U4NomdjHDC_Ie0S_cAgX_7JxU6ETPFlodCrQr-jXbmW7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8fUBx8FynyQjs_wrZAHz2UmKG2Teq0sQw-oihDXvaNypk5tUACTZb7maAH2CzuUQpmHHUleyDXGu0N-NoeM3_g6jdr4L5hVDkbLDbD95iuR7DMstjwcwCt-qnnZuMaVZlFC-lsvQFBCb8e2yTN-qPBecidk4qWWEbGEP6ClgZjZx-RDiIVbnDqDxLlarDFhHGLztVFCKiYWke9TZVfPv72ox7XxuPHFwDM1wiltjVJLtFGYfyxfUlqiUqIS2HE4myLS2yvM2InQw2lsgoS-y01CA_1E4UtbPF96hOyuSwUbOIB3oCAZaEqk_DD1fZ8CbogD1eUXvm4UYjDhU3jamQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=dnOGtGY7DeH8Q2UKqUkAeCC4XMhovySys2rFx8tj2u60OiT4UggcpPy3DbEdyGnB5DEgPCxbP1m61lCuoLAilLF6QtTFbdDlUSZtgxczMieiZ8MTrldsrB1k8GCUfsFV9TpQpDYJc9mYWJBkByFbHjUtdfDNBrxQfyKnqbPlyN1tJI8O6advoQ-z6ICm5ZplTf-X60tPcbxPxtVWq_CBpebzt-2ZpULgPu82gDXk45j0bf85iZkZpd44LeX7rfB4g3VQETIoduxGXQYgiBAwe6CkDL4LUYERelw3CNmnRCGfL7hcaTHYpn1iUxoc8DPNDo-ZWNaCgYICf1JRfYOVkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=dnOGtGY7DeH8Q2UKqUkAeCC4XMhovySys2rFx8tj2u60OiT4UggcpPy3DbEdyGnB5DEgPCxbP1m61lCuoLAilLF6QtTFbdDlUSZtgxczMieiZ8MTrldsrB1k8GCUfsFV9TpQpDYJc9mYWJBkByFbHjUtdfDNBrxQfyKnqbPlyN1tJI8O6advoQ-z6ICm5ZplTf-X60tPcbxPxtVWq_CBpebzt-2ZpULgPu82gDXk45j0bf85iZkZpd44LeX7rfB4g3VQETIoduxGXQYgiBAwe6CkDL4LUYERelw3CNmnRCGfL7hcaTHYpn1iUxoc8DPNDo-ZWNaCgYICf1JRfYOVkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTPqEV5sx3SOaE38WSxobvwitbbB7RT2FSIY7YHEMKV64egQ0dU8D62Vy0t0FwPMFviAft7CZb6rYunzMIH4l0C0oH3gK7nFifSh-2kmicMz1mihxkY9HE0dfUGglCKMVBjGpvEIaZ_x5S2Lqe-8qPdc5Z0sFzq_nFPK4m9tAkZ92a5B6uetyDtBqU9LR-SwHFwKYPZuiDHsG_zNR9CohOWCjz9pc946fu0ETxpdjHuEbC_fnsUop7q41Mm4ZzwPabBHNVRPIoGF2svw8lzlpRxKbZake5VLGsyRbsCXXWpDNiewm1P9NHYWBPW-fRb0C5fL6pYF8Un6m9BAivl9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Ggu2WqGtdXFGUlzxjOnEmGrpIuPYmINqMOcLnIQ6uKC2Usn0kzGqyrGY6ttnDS5-ssNCo53HHlxiThRWK66eSDZaLoq5ViNH2SP47qdNTAL9h06e0MQ9cTTrpCMuIQ1sSoRZT81EoED0Xk76Qu_xDZsiqXuXefQqvNVh1Z80RHbhzXddnQObASrjGMId64Ejp8u8f7etqzwSiwQcvghdfAXOjdP0G2PJFhj_aOoGJUX1mFOZnNlcvhHTWlG4CYf_2njZfsrwL9ArwXoYe-igo1OOhPhPxcg5z-PeItUP01EKJqO5Epg3dkIeIioax8_ilGoT50bUyyzlAqURH9TSog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niqCgpKWx_Iz6PXuKXCHlilV9JKYvT4yJPLxiigsdMANZPbxjWhfx8i4SYWWWFBQvBVSMkil22pT0a6Q099XeBNmk31_lTlBq2gD7MaGcYKuOaPsTtZWPxs3hvLzIOpQY6S0A9p7cSiVecN-EvLMHmfk4EoN9Iv3c3ZEdnYYPofejn49qOb0hQoq_j7CbCR-3-VHawGb2VvDFzPUCDPq9l6KJ7sQBV_sBTxPE1i2jxBLePUuzjEq-GpYkQhaZZQlYh-gBURMRN5exlMatzZmq6dxjl_W05h3WlM4pw1sZjha7ZAHuT8hLgu-Ey05ysnebQnRuLysKNbz2VX8lccYaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0wlq72lcwngfc4uyNmQ85WgSqOEX6-qqhYcUuR3HjZTIAjNX-RNXRJMOPlP8Zt3KPx0SrPwhaZjP_BXvzzJzCP8EQM1LkwfhLAJSa4_hjd98G30aJObMPrfWfVknSH0Z1kqFkK4iLuygpA5_NEizO506Esw2u_UXd4iqOZ-WH6fE7JqgiThNYE9AZLhInjRexssNdZfeyQJZODgGgYX3nFBNd7IrX0dM_9v0vzHIqlmvggDT1gKELs-a7stQ9MCtrOrtGOsdFoeuad5345H6SAn00m8logvKtvMsqzox6lqriGncNy9EfEWZubOKY8pVNTqrdzEXn8B-Xj_gukobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTMa7aY9rz_JRcdTs724gTdYzJv9J-f0hxExZtS6JAflWRjRx5QgEr2jECru2FprjW3vpqSoghhRMexLkk8PHwy2XitWpcALLTGJfaj2TdxpBwBqKfmjaH42RW2zjtsPFeJgG7FJj2wogeySySpFJaHDtfumLN3zUBxFFDo8SpVj9cNOWd0WFJSBK-f9tUEVat2otvzlwmlxRfvBS8raOFuD8uyst05mQ2mnC1K8_6ChTC19VXHjzUIvam2l_YGXLg37QhhT_lCA1JBeSuCj2XWzwqpZjJT2tPxs4fJ1rAdNFoXtOK_Ki9IVyXpSo9M-PBYEpQ51vW8tdp0duOavfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jpx9X4yYicz_rX7fcEtyCcq84rjAPlJbpZMsNKQmPBSXUGtU0o1dmj85EJZuEpebtKsdxiNuuEW86VpAOneA3tonlayh3cDBMwuEHSTvrGNU4i76Tabx9XhQeujs353IgKqx5FgJVnj09UjMPXk2jEorlkxQMGbcMHpyPrOBXFbNneBjO8OYDf49wND_eYIBeoQVrSxvnWeGbdyumnMeVwFX9adfVVkCuf82TLlfTyRuUVE3m2Mh5_NmzZTr2wscjF_8bJjp2k5uP5cRzggUg1QPVvLMgEiYmx2sNh8b4stkFUF191XpNzJ0l8YW7M8K3pYqUT245IuEyPV8hAtI4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3JE2O5WqdA7Fhp_BjV1Zna41WOfHlpILM8fOX-1PO4tZG9jKixkZ900A2_bIhr7du-T9tgHx1unoH6-N4AbFXwfxnaV6LSRVKUQMeAi8zAgnaDSdqlfyCyZ6uqaZv1ptjdJYOV_8Zw1x1DWd25DmBC88H6P_L_K-w1dif5lYvwwE3TtHoj6XvU-JtEARIwCjJH8JBJyreu-aa7c8ibyBsHT1FjW3LE9fSoCaSnbE0E5zHhknLE9bB1_Stc9Ie26HMMEbU2VvDNiblW24kXll7xIzyyP5-XEXEUGQj1JdtpcchBm8fYNSToKuxpxHl56mCzv2jnn_pXblKrvqHFUtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqpRLcUGyUSXrwroWtu8y3-OzLaf6rSNlMporvson_siWV_2Du0VmyTv3NJ5G0e6tbORy6cDAToEYV0MVciX8jkI7OJ1br0RNREeViGrjIKfF_l2Ybl8Pd8FZfl8m60-eDqkOAnZNwx2YFBTD7NO0Qq7HPz5UcVAndyblDoBuxZtOiPa3fdHrtYhfOY_e_cNJIovG7tXsEWyHDH78rbNwMHd15AuBqVvCewIAvgUs72xCFNYTxHbYQx_ZqS_dGRl9F8lIKHhorEuKUjP-yy3Sbpt1ffZmcn-hLdC6_s0V6fRM_FSir0T4sthOcUaxWsIKzEkweMM8l6iW7jP1rHQOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RG44Kt6F7x6V9WjlMFltWZoSEl5tgocR7dIRz0kWiSFAEZ2Sp89m30_nd_mkMTwEtptYbKm7dtzFxs8cMs89C-qL71PAiOxhVJp4gQFfmVNrG75dievQDAYtmX8sP1ntITmIuxVePoUBdzOtIH08yx2TAcT123V1xiDk5zJVcliJVRWvJ31BNOwqw3N5m03DZXUSuY8-1apWBSNKllemHW46b209EBNnjb3-cMkj_ozSo9AV1hpVtdlqQb2GEIPOjhhuU3kY7pDrFb8w-90yHfcmmkGsGeq0g6uReaxAs8L6ug3M6a_0b0G4azM7mjm9RC1fvl8pzH6I6e60L-HC4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8k90byaOL97ba6Vdp3PQhD9MU6WFNtI65x-k9TyXONgSPgpgiidFiDC1vWtyL56c057Go5UWf1CBz7yA5uf8BMHfo8p_mo_PIMEsEIgzARTJX2AIcSiXrnOGNv6AErSWwkRIwc9jallnJM5LQJtpNKUKcDlv4npnpKKw-qBSjvZKgYMkMXL0LWFEM3p5Ri-vnUBmMOL9kCqw7F2tsoTnR5KVcEeOft-R7fLxJiJO8uZdYIjSUQESLr5ezCWamu-8MGH2QH7rdKLWREJHLPzCGO_rj2x6YAoDriyEDHQUmcj_JkfVR8mUIA-92O3XgaJPSExjFazR1e-tbYCzAyzfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJYJXOAYif5lwbmsHqOAkliVcwQv09oI7jEUqWSlhYkvUi7qGBqXrQb3Gy2oaAVz7JfRFJ7zfZAbH6AIScllFV5729qS-sVNLlA38g995apAK8U0oU2NINE-iGcl8E-oGk6uAhJCDw3smKYRwyE32ssaFnCj7m83-Ad-R93m4CUvzzA_c3vK-trv-w2D0uOmZWw52cOczHIgv1w6_BmdFisLvSIqSeDi_f7gpokAaHKw6horOoveQNXnyVFtlvE9aaMWZExAPK6PXA0WEqXshFgg2PkYHsj2FDIHNKQqrTvgtRsmjHBVvso71kaLls7kLoKJe62jrPax92r-YtobrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCDc9r6VqgAFO7ajsvL9dXjGw9_Jt3OU0XSExmGo_Pcck9DmKPLug0aFMrM4O_YbnkrX53E3U1gfGBIJacJgMr4jHt1d0VNhaSDyPSUI4kzEiJlPWqpdaR7tRZ_tgJfN_9tG-fO-mAr2ExjkWo3oQP14e-9OBNz8k9cDP8vL9hLU5i5YqlpDZ4KCNw4FnIGO-oFXV0leDweDHNWbWTFDyMDWm94CVckD17rLhlazx9TdVpj0ZBMrUetGjBEr0IqpVVK_eKpl6dATVKx8KJGVtJu4bAak49FXtDQzj3WMz9alETqpk6IQ8fwnVgcDv7vZsNNRcmacOuT0IZY3a1VSFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KntE9Ws217DzGS-694iqxjC8vgAwsMSKoof1T11qpGgTnx9GuNrRERMZuUqtcGXFt5Nu3CLcWHyQBjyzTWA1j4w4DQdMjKyrZBQIsyzHm41w5dGsw4hc0wSOOmVS5IeTlqerdodACQQLopB4fPNKm_u_sSFKqdBSRgJw3hB_zDWzq6qYzpZDfhx9LnUVZXA3YVIim32H3AT_FKWrnxj2zets_47JZa5ziwJ8SLI8e-WL_vx4RxCg5BL4l35G9UOALOSQSEKl-Re6CMpiuwh8_6GldUqgmT62MFYSI8Jf8BdD2S2DOTeDQ67BPepXhc7MzdtRH8SfN3HtERQ1HsQ8Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4MC1f0zRNHAdku7zFqREOvrUwoEHszcTY0W3yHLEii-HkBgS7Qvt-ZNQdczYDb7pvCgg6Y9-2BR6bvsalfGQThSa1XV01RDU-bI4DTAvw_nnDiQZ5rNEGCXTMK_ZivOOkAZtz_4CU6QcTjmSWdlD7Xagg7uYupWy5AxKIaBDOlM_uI9qG0vcuoglGdwVWR6raCaaPtVDPCg2ZaKOTvr-GuuEKc8B2_wrQT6BvsnESpOdLu1HeWJIdHyv-CXt1HLmqskevjQQJiQ98y5v9i1fGqzmnvSWCru1KTXU2Kii_oREskdRgMYh9gBwnKH0gmXjWKnjYPDDRwNksiXhK2MaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=maFFMesa6LCztTeAycsDrrd0SmVeBRBAzRiEDRyuXS9DQIEfh7JqWHqOI6jR1j9C7BkskOQ5NOpOc7pvOIppG46aLREJOnWQ1i7nKxqMycEB1eF-aMX4UWvRGWpe4dabOc29gUrBKcp6vw1KNDX594mmW8KQIBDCS2rDrOUKClWgoPTIYYdi2__d_xvO-M3wBpDj8Ax-YlyCPnnv8YStzeOS5ZoD3l4MJmJwz1UNFnGHy3L6sWPIQCpQpfwYHAF06mwJO4RUYk2fzQ-14WsvUJhzzgyhKrx_AwwH-gVZPUaIKSEFVMSiBz8weFsXKIqdpdap4Y6g3K318GiPn0XYIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=maFFMesa6LCztTeAycsDrrd0SmVeBRBAzRiEDRyuXS9DQIEfh7JqWHqOI6jR1j9C7BkskOQ5NOpOc7pvOIppG46aLREJOnWQ1i7nKxqMycEB1eF-aMX4UWvRGWpe4dabOc29gUrBKcp6vw1KNDX594mmW8KQIBDCS2rDrOUKClWgoPTIYYdi2__d_xvO-M3wBpDj8Ax-YlyCPnnv8YStzeOS5ZoD3l4MJmJwz1UNFnGHy3L6sWPIQCpQpfwYHAF06mwJO4RUYk2fzQ-14WsvUJhzzgyhKrx_AwwH-gVZPUaIKSEFVMSiBz8weFsXKIqdpdap4Y6g3K318GiPn0XYIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKNaW9SCLq-iprPK9zZp_5x8KzgwBzpAwKdLbr5fp2H3eJ0o5GKUpwEfodpCMgElkH5pnHhpFt-qf_b9UlCSI4me0mDIThHNqd-cXiIHEn8M0X5zLmtErKsCvd9HIPcyXU_1195SvK6emMQAPDIj2eYINE_q2hmxLlWHzI2v2DqaIM_dLDnsnVYNYY7iHEmyB8Riy0VQFDC66uTvEVmn1sVuJqPxv3YK25VF0ENAzNNqHLNEqwzQcHPtHPMwa--dR8pRxkkJ4voNhpiLt5t_uv6l8YAhsM6HB2-VfwUfx1tBq4JEYFGnnz7_RHDmSWjH9sVxiI8WFQ4WSpUeprkVJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vH93ZOwA13oNzG0G3rvPMUto0dCOSnq5kjYI8z9Pk6aBnHICwTMa_bFkrBv33LiTJeKJGQ5kwdHz2iM1aJ2Zq17R6pRhoOZhdP1D6tWiK0ZNrXAhAz43ShvC4bBp05gkcqb9z1Dw-je3rIgHtz6iZJGMUUR7LubvicQiW4wST3M4dbV1kAc0DBOYHVz5dV3l-elYEhGSuFWDqcDonB_r3b29vOXWr-BAfTtHUian5QEKf7J9-LW2KBxx4YBjvUBl9jTgXiSFouIIkLrxXcGiZ_I5yVevluD8bJZLgym8Efih-sOQqhZZp7lMY0_QHgTXgM6FPRej_SS7K_B3_PMU-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HV64AJXziH5KRYqfJNGmwpcAQlS6TKeEZalH7Os9u0m3Jp3SogoouP2-JjyR6TWYlWMqxle5fgwLDndhDcooGI30CYZ4gvkZ4RYVib-2jgRjiAJVpMMMI58MhaoA5rWH9Gs3x_j97EJXJokIp_nppgaJMfDR3aeC7_U1bx8cPDerJny0W01l9y2FlofIEAOfTTEi8GEcGQ34B8vPi7zoZIqEdHZJJ66So2I5_m4RzeNPTKQ9wkeowBHyrUOMN3Afb_0gKSWOsBQ853-6F47jpJIdD_lIRMex-_pOxSTihAXB1sHvHf2HmXGmGQGJ_UcGXKDEdu0uZ-_zgomD0QYP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nnq5fe9BOpqrsJJyg8dgfb71MpVkKKqqTZzg5NGMi3aouiRnnHAJJWZYizsQWCV9Slmi1stM3bVAETGOL2aC-0DQvV7AamIPdFyy4CD9csFlF25ZIydehGezvScRY_Mt1bf_O_-FcbpS9cGX-VAAO09gidZrCDUnvopfA6apr8RUoY1UBpjMyyMzX4tRRX1OCSEnpkQI1B2AMOrvpaOGbnMX1awIg5hsx6BpwSiOFxQ0V8_4K0pTOk-y3BrB--xl__iX8eLi_Huajcm2OvKSvGA166UuqNns6yWzWZhoQCmALxe0mvNCaTgGcCWq_f7Op1nDHapwpRUMl-DwPJG4jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvme4GascrxXwGnx6c0rLxkpICq5-iLOv8AAmAhngTiavWdUciryqCMyQ3Bw4swqmhCYTCcjkjgeIre_KQNDkY3IaB3Cx4yVVeyYJIWl-NDkOpOontN0HMBxWgSS8cz761vgYslRZh1DGbyZlMRH5VQcPMX7JLTrKWJROCiz18S_YtiOJZ3xhGyzSYtkKpc--7e1vw4D1o8AUmnb6kN7M_J7O8Afkahel37M6QL6GVA4Y16EgsgxnHX29f_Twpjsti4qq_IBHOYhYzbqufmtJsuEd8FF-99d-kT3kICbnXuaDuXsalodFFuMgr-5CsM2TF1rJP4KHewQCsLod29amQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBVK2dCZPJnzFdnRcSOfTvleFhmjK4V2CdT5lvvTlmBUa6KeYpT1MUmaDF2SyOu6EnIypcWJqurGL-ZPXEXtqY24OzoY8o-BAzCTyZLsG5flAuIpyY1AD1tHwBNX-idTh4RBrA2c0NAnHO1VDL76PyKD2GCTGGl_OJ_ffy2POAzfkCrth39WlSQxD8xkp5gu7nl6RRcPkkS_Ww2ZG3_zYL9Q4_VXmcGChzHBNCdB8R2W8t210qrOm3YWFa57YoJP1CSOrN4oHxK9vJjiHCzvCc7OuZWhFMLvfjUrzxzGhvqlceAebbOSRUuj7wlynl5c-gkD4SdEI5TP_2JIZs6zMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJrq-xHACXua50ZnchR23rRRBTAJxeDRbHRR-MfcHBsysvQIn0FUZ658GSy9kopfCIq1Q-fF89KX9LmwkJ3u6Zu_R3gnelTSMct7pMJoZysUO02tP6kwl1SNAhsV2EjhgxQ8ld9c9eQToW7-k0s7rfe3xlCaRZQY2El41cmdEn2oW63shtIxIgjZP5mQZOtCNihaZCPcqs-g4Pl-n8W_9SxqIeEIw-KO-WwjzSY7l7jmQbT8hj60vdwFwqGphzTKuwYsLAxKOeI2rfwaWmLVS9_55RuYrZN0j4UWw_Qca-_Oukz5OUFk7UsMApBWZe-eBoRi9jV1oU72g-qNi17Xgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTDChgkhSXacAxkDpu5RoQz52PrCnhMy6pwq_P8TJgQmnX7Fm-Vrk7KqmK7IYsK9omijEU4wHIOeqKziNJUyqdMcsJHMfHEQJ7Wh4px_xiSM-JvU40AD7SGXOqtkaLZeMwRGwOHCLXJSOAxeSI0qqzuIuEYa-c1j8iKbMftipUmtNRRxH0wrxH_YxxhyXEuOSI0zP6FRgIlucxSav3bbVGsJrLtAWO20PlsUBciNLzdTUFHEoGyddY3IVXS6jPg62Lp_4EZsumuuGRb7Yv0UCrc8srtokncl8EAE8B8Vs3K2siRyOdnTpLsKl6_jFGJz3wHlSz7syM1XB0zCSZYhmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9LqWlcjp_u8RzNSBnOwQmdTRTQvTsRh0tC4pZwTSFpihDBpDksMMNCCiAZztnlZNUK13Fjm4lBAgfg1PL8TgPPL-7jntE5WNNkJxiqMA2d36YTqDlekL3EnFqQDcnSVsz32_65X6ga3wR7ztteYaS_EZC6QVj4hST24iJfYc-FJPv4uGxLm6SLNhjScHDDPDWJm8we2YWJoWMANBwItNnX_qXhpR_Z7E4UiHebDOe0G3__7oDZh_iPqreKLHZ1V_H3D-pWlCdsUq06eP-UUcWFqJYOW2IqshWUWojq0lGkUtBYrCMugQZts9KMId4p5gGEiQ5JLbJQT9rj5sOZEdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtFxy4-ul-oG4cxI0CpHXud44AdsCCpSp_Gfxd0cx8ry7sEOH-J5rZNKiuLCRNQA4slZ70rKDeCLpxgQjeBowJJyE9I7MJW6RrMJ7FqWtLDQJW4z68ex1x71XjZMxHXW4svcfGpDmxRjlJtdJgG1Td4ICRen0SJzQLmrujuuV1O3Mh0Icanc17Hw87GcetDHuYAYOoZofYAVq_CFZ2pzxBPAf1A5X8z3RhNLjaWmvcbdx3M95T0BoL8-5iNJMGMrSSVYocq8QfXFQd1lxjbH-g7aRKI0n-XU-rI_Gc7yICp4xCVWDx8C_w0CXff4YYTq11cUMeYVzMLNmtq3XwWAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJKHL4zDL19iFaXu3z0y61wfXXrYdA8orD0DZZPW1EdU5wecqnN2etoErpqVdE64aQx8dTSd_p71Zz7SGrsJoljWTbZnOmRveN9ZRbCCe0wriNNWGMzsbObuCvsD0nST1ETlDMV9oO-df0dBNrH-dMLRg_yOaGxZkulwnNOc5okAPLdQyKZ5q7nPQavnkVwmrzxD7BdMeUvXlif1Zz8Ir88ICy3cMViPwPJKEsxe4n_vszA8H5vVRUELcAkXk4GZg7cqpYDIcqbXspmZyfBs3BMMWnkKJR9DNmIbMfTovSsCNGOV_6dJk4Id7m1g7UOJ6M2tx7NYDiyDV5N6RMzcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqhCmpkS8TOOZ6YSB4mToOikEb1gs1iNSRiladu3qVNqquyval219BpT2kofCal05NHxABP1fa0pBjYk2vhylnObe2bJlU3qrkxLba3x8eGfkravtUytdojPGAzflzBFwDUFfOUE-aazraXHZbcYQIL4Ic0Dy6WD7fdOibdml0A4O7hANn7BPRn2Vf45fxY1PqWAvfdklk7FXYlHd-1AV1_jWhHbFHrlo8Ry5lbaL9Ln3qTLJyzgCrWhB_AzY3UsiRG_n23Ql8rzQhMIN9W9W7m2rWd27HK23xXaaOJG4_hjqpqhwXWCoZ38ye-1eI1etMJbgmUFL4kZujLbKf6nEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNdnxnxJMA0o3Zu9bIJc9pMm628rCXlCO-eNL4sDCgTuK52QAr8ezBJL5jNkNgyiwvTlZoAFYNkHx1OP6JePZaxl-KHZem-Vli1UorJm3Os8ER2Q_q-Q8Nf_919nAinOphE3OXd2z7NtbRUq4xTO1DHMgEt3B6-RtkZlPmiJFb4zqSWRKWidGiWLiGsi1RlFxFr5OSCd464GiFDBpgKO1BdTMLYXYyeA7rFcng2yEMs1NGaaZh40L4xUJhT50zhKAjZOoKceI-22qe1kwuBNE8AvE_iYUAwwIpdlIXyhCnwUispmyE9eNSyjIxfPD2O5zo7MD5ZgWjEd5IN5uJZRlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrU9gqF_LdpK9PVLAc8gIYGmHiMNmXtRH3rwT5zimJ-UOgeZXrbBvl5Ymmvhs4u7Rk-uFxe3uZyN6c3viMr9Xr28ESzHm93nHYBAyrTsJxyDskCY0O2dQtxnAhTcpQAJLOvu_hGbS8bEeafmtTW2g6-ffnlwA0pwcnNL55CG4Gq-MvFbhpFsTz7iEG-hzH71puezQHujbEOcs5JWx8CKGtKecyU6ffhKEKHuz0jmyhDwmSEhCMgwCwM_1GV6Ua1xnfCgfQ6C3NjeFwQUfs2jjieF_b8A1v8CQ3SzsqM2hKEkKi83vV61TdZ4WTV_4AM7E82ZcdjChqj2bisJYg8KDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXK6AUByCAECdDFOwGPNm0uxodA9ItwfPQSVFeSk5_NJkq6crJKYvdCAZ-ptTwlHNiYUxZfQL3jfNgBU9pN16trasHtUTMFxnctu20GDEdqTaqWnm8aWpN0gF_Xy6Gh9SYyIuSLYsaG5R15eA9bjAXXFwvLNpbT8bm9wg3bqkOOqQ-ZMc3eAx5k_TtvuHG7RxO_BLOCxve7qv0aCftITNmXQb9DpTRuToiX9lKWQe3gSG0qZ6NdETNubvS10b-2yb4wEmLL4_TLq9qHB16_hYDJmcY84tdEdgFxv1O2UcjvVkPy8BXuz4ymGBemDkqzpwC3vDHruQCAAy9GtFDoOsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oilVuckBp2XMHdE0oY04guRXwjMQCHNOlkaRNqw6nl6Vsb1V977aEySi0mxlf2vVKCzBZidcT7FggKtrQZtyjlk-NPyYDAVaYC8QzskJ6OXRS9sz7vPVfa4UteJIv4i7uGpkV1StaoNGaZV2n7hnLWqjDvq92aYrhldVf0nLJfvk0IcC8NH7A_CI2-yYZQ13eKx9-dDoQg-tm_Kviyg_XP1QdYsF1ODv-nrb6X7Rpo8Pt9RhFAgqUKEjigW5X5hPnpdaIQbVnpAKvZXXVkaG1KOayqkvC_2zZVFk-UsYTuzEoSgJB6-7UJr0lU8scwih9PeTOunGfb_UfTjxgvBerQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jD2UD732_lKMwE5r8RviS5c_XtMMetR6qYsmOXwxfvFHPbrRz43md9xOq_uM43LEerIVkIaBTs7fZJBaS_mmLX5UOd7Djwm0rkjFjnO0rnDP3YJ_l9ylPsNJQ-BksmT-5H1vys3OSQdgKTLTcKqc-9TEJBaSbGZKNV4vDwl_G1nJfLSZraOedaqFhG8HEaXKBLCtr4i2M6eeh2RDsME_qm5fukzrZH6nWPp00eOiNfhJBQ8B9B4I1_7Fj2XocfsLYDEEKA8JyZ8I3phbhsdA62eUaLKEt77y_npVOxA9o2nyA4ZldiOtNxAARfCaxJxgk-Hl3HUb4ah9E79U00_gfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLCvdWua4RAgGPJFGcl52AeRuDcSdVO7qj552TtOHLOiLaAr2nX_VVdGWv1ph8nmY_tDKWc0hYS5caAfNq_d1tFcWJOCP8FNizU8cK4tE0eAFD1jnMNaYmVPTrNk3abv-351e66ex3Vbj_I_kQAb2uQOyXYgndjIFpT8SUFXuUPhycYP7yWXf9MORpPEHvC39SRklHtou4-6vAqeiEHv54WeW39F-o8u-urqGe7FI4iIkI-yepBAoRKAh29A1wvAnwPhqGwTopCt08dy0SL5gxUsNRoDM6v05Cv49UN6opNsWLfAB2g-9C2vAMnnb5KGDC5VrQzYRTZiP0n-iiPprQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jStY4qIPtE2KKvr_B0VB3ViErQb3Bog0_f0MCLQzaJKr4o6QU02b0Wh7So7HmXLy6AK2HyqHdt8YDae872acJLJbvLxOoGUaJkuEdEC3oOH3B3xTYVCXlz2mPhPIRUlfSL7dn-t00jqSvr0THyFWEH9862A4qVsB4okYwD-us_-M4_98i6_MBukXnEW5OUyAQ3xRBoX_4aZIMTPl-n1W6VjTCxCU4UxZoaTaJttBJVR22Hw40UCgPeQFGWg5HwfEbC5gS0BKrUkECcpy6AzqAcNZ_m5_oldY-sJ4u-b3WzZvvisAwFo0Wfpw_3A7bXLNgpABib6OvFSsP5pSRZybtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzqcCsveKWEV_lHMny-Pmi6zr1nxWRw_zn47-cIajbKijboAxLOl9_GkgF7rJqo8y43J59lqWXZtcG8hjtnbNeQgdp2-gRRQIBcA3WfCngwAGd8qxkPGnMZYkKGMVwFoR-c10X1wLZ30cgrUylTS1JuuDb2pXR_2Hn_z2S9l2gpBAZnmOPLFzeCC98igLDDXC3COxMoQbz0PRGbF7bdeYduke7PFmDIpx_S1KcVGhwzxTndLfmBCri7u5WwSP6f9Dm301GIOTiZpMQwwuBCrNgamSpWfZboZdDM95eNJUmTURe67goQbrzdWTVVTwVHh_Py_dHBxY7cXgLhIO-k4Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1-0BJENAnuio-cE9lcu3yabwTdnYachmehfufQb-zqS817wkCek3Xz39Qlju2Fw7GVFqhS70YUsqw-t_LknycQm3ybci8S0NHGc8A6sN3UsRYe5wzlT0XN--ZVTXqDPDo1qun4fj9P4je62Gjurjk7luO-ujRLxDuHo_PtEqVTXc6MeJ5nsSSfePCukW-X_526LwQUOsTOzd00zWdFCnJZd3QG_6DNKoub0CuZGBpEcrdkXYajQI5bmx0457ubzcaZQGvpyJekTGclaFFRuhlOaVUelPbNjy6LbWqyxc6i9Tb03r8nhl4GBwD4VG-dGAynvMEIdO9R2U-x6-9sJyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5Ura_4d_GOUQwiVvxsGteId3l8WyoYeYVO4E4FkzDSdy0RKo1EnjumpzhGYBgFWdMdP7EKEDmWc98N7v22X5USyMi0XSz8qCZPNEoWvonEPi2d8wM3fYSmA_H5ikaOeHlxZcQJbwcBma9T59psXXh6v8aauQYth6ho_D4PoXVh3SQptYcctENcdWvW0EWMaLnYzs2TjJ_7OATTGyP89VcKn1MFDKTwOtfemv06fQ8ZLDHDHOuo6dJltVjcD_FTPl0yK9IVYlt3k2VCukfX3f8JF0uaLZunGlXmKwYLnOk2atBV3WpB41REjbi9u21w40d3KSgod6JLryb6PsKOpOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyT3RGklawVqJGHVx_JSwPzIXH0cncmxvM8ZMzxOzfgEP-Qnmxj3h3clNcX3C-IHEPmsy0_9agXbl45KSamCoRpL4O_j2qGQMwg4CXdKt5vWFO9N8cm3q25vY6NLRPKeuptXIFv9Rojqt2btG9YWWwADEmH1BBSm7NFD23aTniP-es8fX0-YTYSwq7wlfOBirBLfn_xbTQDf5anM0ZW8w-_QXLBIf3haY1YSQ5bNHsQO-wenKwFeCasmr7oOg26Dpj7Cu61N0N0r2eCI4AHyaSlF1G9WUADiUWzgVuI2NWQJrR9GQYSEz6_-XawIYYhbia9YywwmSYWIHCvoHX-fTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMGhdVvSdX6gUodYcK0csTrQa_sM5C3qK2iiAbUhonWd6XdeQ3diez_2LmCN6Dcj_6YME-5lLx7QWFOlX6mzbKFh7CznhJtBM-3vKrGRkohJrYjnyvI0GyvX1AnmBPZpoQDiccVTr_Wba600KMQVD0rLZ36oBB37Vd0Qu0LzFG9PzaWKo4PJMXQck-J35V6lUDsUWpV3wRA1nhnohJP64Sn1gUqadgTf2FlphHucrPFkS8XwCP2fiCnQ3OBsEJap5Ygur2C8egf5MvgJpHEyfsjeS6z5qlUzd3lhXe78qMniwX84aso_AuSxJ1jEUkmRn_JtnmjvjzxXnBQEaMFx_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFbo-Ne3h6uztv3md_vBjn4UmKICkcARpi2t2zNw4_5T_yx9S4A3mJad-UqUml8qkNPeHst9RmfjeJoriABa5r73iu67l50XnyM5Xi8eoGGZPROHQaC1bUJKgzJp_fcqo5s0VOydFITbakNtciAwt0d71pfbL2QuIZte7RV7uw0tZU_dIFhGlo2kXzzWJ3OJ8sNEGJp5X-pjsmRHYTDvLTemAZjmxJS2ukVZUh-R-SvtPSbKi2do7r2_3RC-1BJ81lhGB5kpEg5z_TMG0pHr8LDbRNkYoDaiwm3SApGErS28MEdPDglpkhcTVGtb4tKhEDCKfhSNFH6OEGTqfDRP_gL8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFbo-Ne3h6uztv3md_vBjn4UmKICkcARpi2t2zNw4_5T_yx9S4A3mJad-UqUml8qkNPeHst9RmfjeJoriABa5r73iu67l50XnyM5Xi8eoGGZPROHQaC1bUJKgzJp_fcqo5s0VOydFITbakNtciAwt0d71pfbL2QuIZte7RV7uw0tZU_dIFhGlo2kXzzWJ3OJ8sNEGJp5X-pjsmRHYTDvLTemAZjmxJS2ukVZUh-R-SvtPSbKi2do7r2_3RC-1BJ81lhGB5kpEg5z_TMG0pHr8LDbRNkYoDaiwm3SApGErS28MEdPDglpkhcTVGtb4tKhEDCKfhSNFH6OEGTqfDRP_gL8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fax3oya4TaQ27gBQ5XjtnEK5aXufpNoYpTvx19rejHH-hxCKu_LDQKrk7lmP-QnIsYMbmnaRKFycFJsAqiUarVXd96t3NKjCDVsW1NIYYvYg12ktK28n0NgmVg3yb74zV0Agzk2-O546YzYYo_J-ddciddxlICnbgg_cjln6uU1c8CqrKSW3kjTMCQokXt5cSfFDRS7JFG7uT4ms_x8PUPVRparLxbswo_mxtX1MNVcwNr1127GHn6YpcsqVo-EtathH_ERoknbWFGDUvLa4_j5STRY-9a2WTljdO1C-r0q4a7-dQafxp5CaQWweJ23Zm9AFY5TLx9m7ZKShJGC_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و سپاهان در سطح دوم رقابت‌های لیگ قهرمانان آسیا حضور پیدا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlwkUUtgV_BlIZMQLGlBteVHkcYVfDmSUC5_BZLDXfSEtXEuFahoCV9gnnbHmXzjdPDg-RtHtWvcr6HwbYwhYmiCuG4TE9A4uEoDjDrb83TWdpQmK7sWeGGW88d_vjldvaagaAFB4OMjb_ewNXqcpIFOu-wNH-kOnaQIAxVOowjF_AAlAI1muD9cOygjoen9vCWqeg3AbZCmDpTxN0a8OIqZqnzoASo--v2KqwKpLR7yvYf7SFCOcCV9j3X3Re7V75sMv3i5TN8idP5N9n2GErg-Jy1tgvz6Tsa5aI5o16CWdiy4H_qkVL90Cp5GSwQUputpuJcdV8fevt8QyOeRzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkWvHtzy_RzkC6NtNMYV9-EUVjHh4vGS9U6oQFfALKC23nT9J7m65qayfnmkfRxvLeYuFumMdC_nMZ7vE0GgNGlmBlmdICVvaF2h6q60539qPUGRt_6yldKnmXw4xti2gWtBkrG02qVCDQ-T7yJYbIm0YWFH3G4tLlWZjPgLU_JQ9VEdAAtJI7seL_rKws8pqTkIUPad9-al0XIdNod8MCTMoFu_g3vbuydLjbI1phzrefFzpytM1liwIPHGBIWE9oNKrdmzkfgGt1qdmZqL7DcbdfZWjUKApw90zaZVKRS-Pq-TelHUVyAGiJf3mD0goSgLpC-vr2_USr9NHxSgiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWZgLuv6eaw0HFy3t7ZtZpujKdrrGsNwmlk6WAjZj7TTEJa981CzwW7nkMDljCNZuMph2qWcS3U7GwtTXhZfvhYf-AoPrnQLT753s0OlOu-z2tIUyTc5WU5rkjC0Hm0GCJZyZE13aM7a9kLnxwoYMgJuXIMZLgZ-fdo1qEByb0wT7Y7_ACEIr9qgPhkyrIUAnKGxxkAN7j5nKEKwO8_rjTV3cPHmutVO94kRRN-a0r-FzpZJfQhltIse0B0NqUZgcUJc6kMqzm4jyCOyLUif1pVTK06mmhaMwGonX6wViIcfCMFm7eOV2meInUQCWykLOdfUdQF-qKyc4hw12R4Zxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhGufsLJsVf_iVtA18umDi3gXSoaQr_9yiEmlWqy_tPMTnBBZNMIhYP2FcALahu-l2dcm9fjAtPRpPbNPM4DC7OdX05XFiYEoPCmetIWRdS5tkrqRPikKaIPAD1I8Uv2fDXRu9lKlIM9s2WnHv2nO0MwBITqPGq3GhfFBXK36-y1BAfbUI1sm3BsLusQgeC3Xl0Q5ALzyOiDBwjE3mc-KpPt_bd8KnAEXoAAcBSJEaBDSFB_nn5odC_7XzYbHhSvPZxhO5XitRCjYbABjNoZgBRfIGnTaD_XRQEDyAeJ9BuRbhEgQ_hNC4f1ApOj-H2cdCzGFqCuwDZHGU6bINj0VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlezPZQYwfvHNkGX8gtx9Tzup0j0nyPiF2iUKLuLY8WVmDur3sjSW2_YgZfRl44rGriZQdMEQSAWTTLuYXM-gj69I_iqYXS149_QLHxW1uBLHBJWvX-lfiTF1XaIOJyFG_RYz6a9QwYzP2lIIyC-SMmx8iOS79_Tu5klOrFuDsdE-GhZRCbdloOMF1N8dqT5U-vZdtpad1FyzRb8nbsPL16QXlaPu2L9b6B_SZ_k1x7BPEv3OBUPuJuOc8QbkaY6eg33b6eL4nkoUGdf2Oad4OFE51kaKMcXAT_3pajQcUmqoVvfmDUqGsdw1JoeX1Be_0RWoYf_wi6P7AcHVIa5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yhdp1fCUN7Fw9PVE91jhpb4bMOcBWBSzO8KDHyttogODjmkc_1cP6ihl9iOkjuVkbtdGvtSCfVS00BmSz19akV8fb0dZBZ3q4rj9xqe9GYnp1W3s4C0pXIfPSKE9Z5XuaEFy9frfY0T6jHEGHCYfi2fCDGwf1NoFNLTMh2_GiBBzbG7E_WSShOzOiseeR7IfBkOxeiHqQifNhHFTWV7aj9escn-cUSvb9RV6N_8s3SKmdJB2CmccwzguqYEM3vRl7Sv2sCIb43_LjKcJSl_1BdMUsFmX1IZiPjep8tFxw2NXGXFfez5zennPyjTinplR2-W7AM4E2iaYSmNO98ttdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ud3bjqd3noJxZ75cXSy6ZvSs3t_el0pmRg82b-SBy5i6_krivMgnxAPGHwtg2LaRghdBZiQ_10UYEW6pqbs13ZrHE-wBKYIcyxo-EtlfafeT5LKOY0DZGgmy0v1xc3IWu1zCxv-uAYjtrclpaSah69R-D3T_D6Hkh9RP87P3Up3gHLEkU-jP5BgP9DAovF-DoYCC2_3YqAT94sm0R9QxQy0jKUiELSLuH86UNsjbUmObI9Dbhofp-8POvjmHjhVIb97IfLdAzu0Vhy5P-CLyf-pLfPCYc1TVWCb71Qc2za_JMzQ0Auh7nNpGA3lRfRPcJonNXIhRH2ZTKI7nf5uh8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2JjKxYYy2uAA9V1Zrfv0eeKbNaYhSQpAtj3WxsAHX9kVmB3mRyp6x8BlafYnNdRs5fcp0XrqDO35XVK9Ssr3KidJhP_sw-BKFAVtMziFljC3-Uo0qrl24ed95_uSPb-F2lmxuE2Vs4JLjFiMlNNrfM-ESUg1kDg24Tno-GLC6z2XSvlWgA_k1aW_I2QXSzYTY39jOSIMIHRM5NR-9-GLDzoRf10TnMKzfk3KLZmfHnYTmWXv7kc2CpL40rdV3rfvAfEZf7PRTA5cTMiqZ8xGb__OqQdc8zJV2nCMbErvW5Fq8NigXnfJYcQJSjrMA2DdWyDJzyZwhucj86mVX3WSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VAFIcLdRdtI3LzeoQYP3h4hBGNCjUlfduuBxWWi0EfBS1cP7mXJq4YoZN9-EfG0xGeUiKHJCgtsGPkr4OO9Gbgiq7s2l_rrT6fyFWJqcLxa9sgTB6jKPcPhV7WnIeuh2orKhgnQGYm27JnhlXvnmhylReuSJKf5Z1LGZvi-ReLz7zii8cKgWiZT6aRBboTuvtDbBexgB7g_1RArxBGJ4m0XX2EmJfr1_8wp2oCpqdVRVvKgxMY4w-TJzvy1EFbI3gBj5E7wnDLTMVocu0uHcOZfpJsWukAtK0vo1BsX5xwKGd35QR2iLhHLsQTR2HWUT3h0ZkSHupLzw4CLkuvG5dQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dycDm7g_cOaSiwb11bXkwJG_uhlScOF4173-rzOTwBdYSTbasXHW7VBRBBErESirWdQWNt-a1gFE17kwEA8QaZBm8JKvaVkt-X_pS65GPXaeoeekVnWwdyte2gVBQXJRGaMH4bqezvgTjJnmGbBqh7XUMyPp9761eDKFuwh3Cjxi0p-8NturQqMwX7OEtwSyUJBYLrfA_Fl8kac_GmXqL8N8__5TLVqReGiHCBOuXpaQ3Jj-eC9XE8FpGczSisI10aq6HS3UJCQDAUpqHvjDFOVf1RWPy-AuT-kgf0oX9Re56QUSzFcF2JWUydthzdIhC0J7Cm36V8NbkaLelB8ckQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=qbdvtcLqAqX2u08k1yPa5KD8jTDxjHF38jfuxW3k0CgONbVni4_yjhsqtqo8I8DBOLpjOB5-gbaQ-GgLgkxVUquywNqhGBhJkwCGVAKL2z7vSJcniYKfF3Pj5l6lJuZm6iMVgSKX6SCcpXEqgfSk9SIZz5i9RDLxiad5jRpGNu9zLRK-UQc3AsDR3ofzrLTzo9cuXII3zZMwM_pmifF1H-VLqcaXWURRCoPXjScYy9lBKZJtjFSCz1VAP-JpdJb6UgcGNS0hcJx5MIoBFe5FBmh3cF-vzHE24sIViGWIE0qyBjz6WgBCJltENqGsIc3KqKOTIZt9DQjHPqmcxo2Wxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=qbdvtcLqAqX2u08k1yPa5KD8jTDxjHF38jfuxW3k0CgONbVni4_yjhsqtqo8I8DBOLpjOB5-gbaQ-GgLgkxVUquywNqhGBhJkwCGVAKL2z7vSJcniYKfF3Pj5l6lJuZm6iMVgSKX6SCcpXEqgfSk9SIZz5i9RDLxiad5jRpGNu9zLRK-UQc3AsDR3ofzrLTzo9cuXII3zZMwM_pmifF1H-VLqcaXWURRCoPXjScYy9lBKZJtjFSCz1VAP-JpdJb6UgcGNS0hcJx5MIoBFe5FBmh3cF-vzHE24sIViGWIE0qyBjz6WgBCJltENqGsIc3KqKOTIZt9DQjHPqmcxo2Wxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8RMI3fd994Q418jq2dLndD4nXaBYXUifxcwxgFuql9_MUurgcsel2g0vfpH9BrtVSLsocBprXhufBDFiMW1b0yzjx_v7fQJ_QzLnW8b9Q2VXXn_lRxp5aNtX7T08KS3Xs55kK8_0Dx1-5nysF5SMm475QwAoZiGO2GUTGorWaPP-sOjfY-7rcJrQwhUqJiqkUtK4B13XRE-ZX7h2MTj1LLjcgI4MitJwFv0Gv4sNE1C8xgwQe1TCPJe-VETS5lOlgHKMivh7D3_JgZdd8uKj7lFC8QrxZkCvlhVA0cfWmND7K68QMVTwf25h8EeY8P36nnRiu5Kpy5NKA-_OaJOCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdd_PmAQbumh9uUgokqGpk9ZKfZclM7u7xA8Tg7dD13Q47xCwMP1pXzYvyAH_1vFUvb94euaK4DWYQwKykmYl0o145BBORkJAVsqBt-WDXhoIyj_c8MVvg-fdwT7pXUkNX5cEf3igFv3u6mFNfY2NjuxYkTjkMyHI0NHriBM27RmMOhcPHNEZXtg1BQRbGSokLiknbfJCOnF8zl9yNLiKYQfK_v3xPQa-lEEIsu6ydiybnqhU6D9UZTMdPSUdiaF8kiPmYMxZF-cz2EN3qcdYSlVgTnnSGoAOzPbHSqVynvmWcoM-AmqFeum59kB1CcFO1NKlTpMUp2Fnhpn-9N03A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p08EYtiCpCkU5TnauQAeTqy5A95ERPNO61eJAU24xgSg2NAifV3qsLRAi2BLLBYOcUVd85lQevKTvi7LziIXAye1LT3OmO2senjz8DQEt5b-3gMbjO2MCvDIskAKrBb6ffISz5SviFsLE0k54Z5dnSAu3q8IZLIKBmO7h9miRyjxPCZabMHYCAQnBMCfgC5B5g0QBdD3s1byMT-8mV3eKhIA58zLCr8k-eBl5YRVHotkfkbu6_bNtH3TpBoLB-e_a8p5Tjp9r7fdyglytlh-dIBizXoq1zNfoQh1a6G6Q5JdrKClHeV6gzGEY1C9WLqc3D2pPyHsG3VdlLWi93yWzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twHUXf7IpGRqC9sx_XH1HLLUc60YalU-ZUWvTjq520XApr6ivQR15Zt86h3Qz015a3raFXXWo-U5u7ZoA-IwqfiVVkH1SyZQcCWeHbZQXvLO5i4AAGLUnP_UVjTfY6y1iq3-wn4sR_3JdRyjjHSQx7XCoX5tG3oZ_wBAr6GsM68kNkrFFEduY30-jSQVvEQq9d8IhRasKSeJNU20Tq_XsGgbyDU5AalWE8vdaQVMAADp28atUA2G-drfq54SlyGH4C0YLWwef41girpbfDqy9SnRAo5MNAHq8Wf9-PRJi-jZYzfYQFudzhYfSah9VrfFxlDq3vy06RAl2NARARjUSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5ymasazU7JEbifk2J-5N4Ukvf3Pc4CttqxEUJopdMCjdNRlhcPqa1BcV3s9JoP6lnAHZUtaAB_vSLDSe3oZegIVR4ih_LizksqzJeAHSdMf7v3gfXdyDJQCasMcdquewrmTtSJEXpTM8itgODBAyBqK--6Re-ipSgxeZbuom1ZVPb-gnnbPEqS4I_5dI1HehfJMIzAAWrY8fxnwHAmwoQQwKEN9mw2ZtsuFCs77P7-5hfeCAxHDapNzUKZnjTe7jBREDRR8T7RXn3dduxJmJi3lKmRRQSXKotEE8W-25CIeSvJIEwgHwNeTmsHLMEvcvVJhwJGD15ccViWzgdOgww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAJdrLBc8p017hceJXFEnFOcogdK-5-Zx-mY2omD_d0Pi8fE-RZ3branTwFn3WMSzm0ncVL8FH8OjWEze0nTEzsnGyL1DKRk3N81q5dkpdmR61lL6vO_-zLyx_QcnR25KaoHZgASJcYO3vQNSOtiW9V8ttR9L8AjttmBtp81LnNftZzVabtK29vqJwdleAmDAqMc6QcUzCw0Tyck0FUEkOZnl7TZ7cLGSxCSIaiok5KEfpJUADece20t_RCJL3j7NlQJ8weVNO-_phzUL18V8gxWx5dC0dVvFdvW1rxXae-tgjqo_pj8zz-OL2V_y2v_RmRtuZaCF4Bvn2bWTV1xhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AL0VB1EUwakfSneeW8oAD0Ow8qJIUcoPziifXHZwo-nhE-udwLYu_ZKEHvN00nEKwElqjx1BrP4qBdJgTwb5szD6YozfrmdhRMe4nFqulXUZaVMRv3b9zOaOmnhZLzGzpLcgwwC6BSDc5KKV9nAiPTVlSteQRUXUZyLqWMnk1ihlU_saWOyAsySiMVb5PkUrM6cjh39ri2sf0t8j0m3G8yqkLt-Sas1K0AMUFNGkkM8qR9g21UtBi_8BjuwH1ZBXDD9Sm-dA0GS1wkrpfU8rKsbFIgC0WTOPpMeruQFcSifBgR87Wdl9ZdIZRy4oaZKf00h2c8Ymu7oAkkm8keuWiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
طبق شنیده های رسانه پرشیانا؛ ایجنت‌ خارجی‌های باشگاه‌استقلال به علی تاجرنیا قول داده که تمامی هماهنگی های لازم رو با این بازیکنان انجام داده و درصورت‌وقوع جنگ‌این‌بازیکنان باآبی‌ها فسخ نمیکنند. ایجنت آنتونیوآدان،ماشاریپوف، آشورماتف، یاسر آسانی، داکنز نازون…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/22046" target="_blank">📅 12:06 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22045">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=ZCRyAGMkX_KBVl0TVrW6uIgQ1dIX8UZaeBp5bk9fH9fRtCGQFk74lZhaONVaiXOmIc8xk9-zwBIpM7nFyhadY1s-VJ9Q4XkTcWG4mOioxMI-hMX6GdAVK-jagYsJT0uYBGtLfrvaHPwTVPLbTwSFbayzAe6xASoUUIRrxqTLLXRgLYnOrk_Ha3-n31tD0d4me9TZWau3FgmWuc8Hh0e3EEuHLp3uqngTndZVptwhr66wjXX9pXwC8Y2ebk32V4IYUI81xwq2MGh-XXvmMALxn7b48quj-rdJGFkjfU8vzr5-MpbPiEFKH2ioRi7Kjii0Y9b-9g8iZqVG0PJdEgfDiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=ZCRyAGMkX_KBVl0TVrW6uIgQ1dIX8UZaeBp5bk9fH9fRtCGQFk74lZhaONVaiXOmIc8xk9-zwBIpM7nFyhadY1s-VJ9Q4XkTcWG4mOioxMI-hMX6GdAVK-jagYsJT0uYBGtLfrvaHPwTVPLbTwSFbayzAe6xASoUUIRrxqTLLXRgLYnOrk_Ha3-n31tD0d4me9TZWau3FgmWuc8Hh0e3EEuHLp3uqngTndZVptwhr66wjXX9pXwC8Y2ebk32V4IYUI81xwq2MGh-XXvmMALxn7b48quj-rdJGFkjfU8vzr5-MpbPiEFKH2ioRi7Kjii0Y9b-9g8iZqVG0PJdEgfDiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله موحد اسطوره‌تاریخی و بی‌بدیل‌کشتی ایران متاسفانه چشم از جهان بست و به رحمت خدا رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/persiana_Soccer/22045" target="_blank">📅 12:55 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=Oq5daYe-GW_5nxrpSwbgbiWguZXVunKeZlWxILyLCJTNSnshm1FWVH32aWV3FkJdW-hcsZsDPS_wjo-gB_n6dgIqPZfGL7bXlHWdLjPhFNy_PdAuPjRE3HmJYX5hhazaEAtMyB4d0wJtGjVqfjWv7rMBA1uQgjzafR_nO5si21X2dgLXImYF7kp2-RU_fOoM1AMCPAsGKLsF6EAL6RdXXTgUleXPhpPnCJh9MOMd59oBbhFd6Cr7oBpl4lh27F2fGNViP2gcXhEQf24mcw4YiULhDw16LjN9DHiCEBw28CI9-nFEBz-xCs-6QXr-yJj2ElFpWHsfD6ie7ZagufXe4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=Oq5daYe-GW_5nxrpSwbgbiWguZXVunKeZlWxILyLCJTNSnshm1FWVH32aWV3FkJdW-hcsZsDPS_wjo-gB_n6dgIqPZfGL7bXlHWdLjPhFNy_PdAuPjRE3HmJYX5hhazaEAtMyB4d0wJtGjVqfjWv7rMBA1uQgjzafR_nO5si21X2dgLXImYF7kp2-RU_fOoM1AMCPAsGKLsF6EAL6RdXXTgUleXPhpPnCJh9MOMd59oBbhFd6Cr7oBpl4lh27F2fGNViP2gcXhEQf24mcw4YiULhDw16LjN9DHiCEBw28CI9-nFEBz-xCs-6QXr-yJj2ElFpWHsfD6ie7ZagufXe4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوال عجیب خبرنگار:
اگه تیم جمهوری اسلامی قهرمان جام‌جهانی‌بشه‌چه‌اتفاقی خواهد افتاد؟ دونالد ترامپ: اگه قهرمان بشن باید نگران این موضوع بود. احتمالا تیم‌خوبی‌دارن. تیمشون خوبه؟ نظر تو چیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/22044" target="_blank">📅 12:52 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22043">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwLAM1JFxA_Xf7rqL3xO75XR7iowFFY3JY5lQuO3rS6E6cMjwX5acg9gjkCtH1maBNssZT7hW3r5nOT8-YC2d45qtHDO79kE8QYrARRffIzbIMYXBiXi1OKyiQuiqLBYWoiIOzWrSxFboykDZRH9BLK7jpeiurjJZLoebjU9TqCLCloQ6Ycj3hCrJO-ZISqA8AWa9h4w9QohZeL9B60-2zOlYKWJDpYfEQUDNaksq8GMAwP92tHrYaTBkKJGVwrX6cKqFTTIPuu5JS3Ruq6sV5xkf0DfG6WQEFs6KB6BrlB0Xz4fn0cedfoaU2qnxudqJM98-qGvSwAoDQzWOIyR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/22043" target="_blank">📅 21:22 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iM0TJsR_J9u__uNSWk726OTZIg5a3Lwtk5p6BxzhVcglV57Z-DaMjssJy64RtcgfGmz8ddnsEy-ItBwhhRFIZPIpDFxrkAjveXzqnnU7yqekTDWm0qQSvcU4Lm8x5fvAu7CqaAJDgJBUWg4W4B-VwogLaqC2LiAdXR1z3f-U6BIMJU4EuatlV1gJlksQ8fETQpNEFYhguSegqlETFsij2EOQRa8hBQA66hZCXbWx-72U0TftDd_n4IaiRhduDEhV05HDHkkLWV8mslVjDcxqFEz_4ajqLH4jQdT_6DiZeW0UiNoAa5Sa7tNsvOkxGY3DH6ou3ygnEvF1xPSoTAyDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/22041" target="_blank">📅 21:17 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLv2qvl03mx9pxEj67OyZckvE3RvmuPFBmWNHfDwvshcJ3_gBECd_tE00eJ1BN7HNzmZBCY5Zph_cC3ncrtPmsCEsDtV53Jc68FEEtakI76SXOsk-em2hHjeiJo7pd_NN1s6_l5rDmhg7n3uLEGf2qAHWvZG-cFcL6k5b934x7VN81ieo2sOMKkaqidN-VLmyIp5Om3GW1PckYu5GTpFHsW7njzm6el_RizyYpXFf-YCulL0YFIv5zLXYN7EJ7HVOU6gMyxYF-MsI_PwhUxPfZZXFeUTprIGgXJMUB4fd6Uosim1ywhvPMfBzvyxky8RWgv1XSqeO86-xHfBlrJrHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلیس‌کانادا از ورود مهدی‌تاج‌وهمراهانش به خاک این کشور جلوگیری کرد و آنها کانادا را ترک کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/22040" target="_blank">📅 21:14 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22037">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERvFNd1O85LFLH4_Zb9-9YjD3XsHFoqizh7uVfV3Ov03OJkwQF31RRXtgyveSLCv_--o7DvO3Z_T4RvjINmFP7IgLe2al04SyS5ji4JdcuQGGKjIuGQD7arhMIBejHJMQC3Es-nyZNzbE18GuiXwca1dn-SpepUzlgNkp7EIMbpRgMaSWWxv67vGD7idZaV92pplhEU270IrV0UnnrBUBZZ2leMA0ylU3l-E0FinkynSISgGTq1IPrp1Eu2w0AmAoWgNt8YmH-j2tjXUcxIzN1Ozm2W1guxdZDf-93-x2nWcJfzp9LFjx5-GzVAxsW0OZkyEuu6UYExxjCTFR99RXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تاج رئیس فدراسیون‌فوتبال:
اگه لیگ برتر برگزار نشود استقلال رو بعنوان‌قهرمان لیگ برتر در این فصل به کنفدراسیون فوتبال آسیا معرفی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22037" target="_blank">📅 11:35 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22036">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbuR2RILBkYZCYZLausso0CPslQn8nsHMrvc_AwhOuyrnj0qeXmZOxAhI8VnW-ruJknwDyL1lNxYSlTNHZGkOGVlo-6k0U7wHGIWihmamg0pYUK_GwwLDRwDTcXnm-WnrKRwfYHsqjnjRb4FnLUEsGoRYwwRR6mnA_sF_PnhfRsBMqd9NjBLXe5xJ3c8Y3aFGyKmr1i4N2ZNSlajIHUWT8tpzmP6hy-psffJsMpd6Ae7E8VIb6GshFEGuEQR8_Tho39zFyvicKAciPLKq79eVENJ6Z1YVOSYgYenFgWbpLEpmRIyXsxTdBgkjZ5ZrrCDsLdbauM_kR7Lf-Zl3iu5gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجمین‌حضورکارلوس درآوردگاه بزرگ!
کی‌روش با غنا در جام جهانی؛ کارلوس‌کی‌روش بعنوان سرمربی جدید تیم ملی غنا انتخاب شد تا برای پنجمین بار متوالی حضور در جام جهانی را تجربه کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/22036" target="_blank">📅 11:27 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22035">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPTUU_gIF-glUfGtoz0_rLC1Wpp2FjVwkN8hdQdJtfKIlorXFV2dJt7syOOPZPdEALE5Nuz0QATfkBNNh0B1lhodA6Wz4n8vkxsVQWZguEKXUoxLlgPBOaD1qwuXxlFXjaOvOiC6c_Xm-h6JUspK1q8OHY7aiBfRU84RAET4-UN3EU3DRPyHThNkz5-IOXdvpJRPgwhW2oDqEKfO-ksPMjAZhrdbBAkpzdirrDIrTFgJ9J_10VcOsmXgvrw6cOZZWDGWW9fJGBlpoZ-QYY91v0TQeoKOa2OKpj1rDs5JKenK9_d__PTWJj0FWo-dNtptL0WcGKTMLdUZ8lpJ-m-5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌انتخاب‌مارکت؛ 10 مهاجم‌گران‌قیمت دنیای فوتبال
حضور 5 بازیکن فرانسوی در لیست 10 نفره نشان از خوشبختی دیدیه دشان در جام‌جهانی پیش‌رو دارد!‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/22035" target="_blank">📅 11:11 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22034">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=l5x4D30UIYz6owgJjM0eDxYdSDBxe7D7-SDH5z3eycFRZzKeg7r961ZJrJdh--L8vzohf8IQx_49tKIWv9cfuXHrfIdRKV87HbB0koHuDZBGHSKTHMht2Av_PHmVJ4ldRnWX10CtMHGgS0DtqcFai047NJRnzZ9VeR3vUwzgGY8Zq2xcygaRi7I5IatjS4mMIidqVRx5_SZ52y8wVRcToB-xbhfYzHx98WEH9z1GO4miqVzXKzQLP76VFtASgIJ7RzJ5X1YqBM2H2YEspChdaFe22MQSpOz7BuTC1d_wvqtE3BuG9_ZQQIfA6LuCbn0My162A1BOsNF-rFo0gaBJvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=l5x4D30UIYz6owgJjM0eDxYdSDBxe7D7-SDH5z3eycFRZzKeg7r961ZJrJdh--L8vzohf8IQx_49tKIWv9cfuXHrfIdRKV87HbB0koHuDZBGHSKTHMht2Av_PHmVJ4ldRnWX10CtMHGgS0DtqcFai047NJRnzZ9VeR3vUwzgGY8Zq2xcygaRi7I5IatjS4mMIidqVRx5_SZ52y8wVRcToB-xbhfYzHx98WEH9z1GO4miqVzXKzQLP76VFtASgIJ7RzJ5X1YqBM2H2YEspChdaFe22MQSpOz7BuTC1d_wvqtE3BuG9_ZQQIfA6LuCbn0My162A1BOsNF-rFo0gaBJvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سوپرگل تماشایی در بازی دیشب لیگ‌مراکش که احتمالا برنده پوشکاش ۲۰۲۶ میشه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/22034" target="_blank">📅 09:07 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE_-O85GVbmG1sfSNPYNrzUJO3r2ZJMgZSOF3jprmZq151NmJLiQEPPS2UBjrde1jYEDPorEIsrNxYLwYU2xjkCpNLRgCE7BWWThSMOC-jO55CqUY1c_qI3WlwP_uo7_gGolEGx58JSPxgUxpBFLKzz9E7x3-Hhr_TREx4MZ1hcRoTRXoaKXU8XXZ7pCUPTbdUxotMaNqPOR3KzSh-Hf_CYeCkxokplFDGM4UQsZ9FTYm1_ftW1lPl8lwOWGtILISrwlloH2VoldKhAGjF2N9EXd8428OvtEC0gD-_Iy4HOOChm_ZbaAzoTW99_kGCcr5UFDXjrsyb4W9y9GJh8JFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2qCivqQemU6MRv0BB8yFy2G4HN6yzBBJ8Gt07sbpBSJQxVw4GTjqprDKeJ0VCrozDxKFHOMdsX5kGz-ac3kO_Swgp-s7_UbS4TnSKq-NFzvS6zWoxaCk9v6dwSekRFc2Idm3WKOMs3K_WSfNXs-SzeNQvrsd9RsXGFv4nWiUNmaemFGSAfBC_-VJslPIIlSaah2Yde35-CULpxADvOGJouxymt_FKzptqvZ3JBwYORl0tt_dhYb-HYDD0UR9StY0ibPTpF6VgZM3bthjgyd1J6KDjLWHB0zDoXK52vrFrnmioMcLdQC0VqC_LSxTQs9CMmzZ10W8zabh7C94CKGLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چهار تیم‌ نهایی قاره‌ اروپا که امشب هم موفق به راه‌یابی به مسابقات جام‌جهانی شدند. ایتالیا هم برای سومین‌دوره متوالی از صعود بازموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/22024" target="_blank">📅 01:10 · 12 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9luFDfi-zo29Asq32CVCWpfEo-5I4VlEq1xXi-mJPS0ERNxYsu6i6GpJvRnT4NvqTw31Q873d9NGro6vkP4Wxcycb4mcfngYXfBbspYBRmzLqZ3G7JIhadatNfKak-i5wT5cNTxZ6YuQozXVI_kX6a56Il3pzPfL-xHiPP4RLnztq7Fv6J-LnGD8abvZDHJ-_dwo35GxwhTUCv0ALOb3UgZxEaVSWEJ2o5lbw3xMe2arqOFst6ZcjdK7Z9iIWH0iXkAvSzkOa9i4c5X5mzjcE9k7YR8p_dhM9Gf1qozvuW6htZEvDcy1aAWsQingezhSsXThat3fZ2Jdhs_9_6Lyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏مثلث رجزخوان‌؛ یکی‌را ترامپ‌زد، یکی را نتانیاهو و آخری راشریکی‌زدند.‌عاقبت رجزخوانی بی‌پشتوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/22014" target="_blank">📅 10:29 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToRtB4552e63GZsDqEBWAADi6WvYWS197YyoFO8L02fKZILZluaJt9keh5NC581_eNZpNKAL9Wt5I8Bu9hr_RCj5vv9_gbTMFLANpxHMHg9djbAJX-zZQylkoV3qkWXUIhQ-NpfU_A0IUhKrD89rPpmx03seBHMpHVaSYwYuSyXQfd2CmIW7ANMSZGiGOFlRGp5FYEN73itbLcUren9yjfr8KI2rVhZhEcirJmgtKxPgFAficvbk1VL-jLluQHRwxqjMxi2naw-6QOg0UcpOAnWBDIweplm87HiAFwFkgZsweRDTfnSxATddwGRPAGXJy_PvkqyQSsp-ZdcE9LNxCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22013" target="_blank">📅 01:26 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22012">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHDxd9lytaifq2ZNBjFjB2LkRBGWgd-_iPNELnaJUiljw3RkyrEhi5Pgy-vplUwjR8sceeX3ljZcD_dkvLu8GACHGo-7qOJVUJ-IRwJWx2skdqulFqWRpJ3QtENd3T0LMe5NkuirXapGlSQIV-02VCkTH3OZ_lfOCuUZcC38ouAVq4apN1EI8dQQxS_onurDyxiQnZ1jyS3nbrbZyMyGHSlG05okX26dsfKcy8GN8SYPpbOzwlcXlrs93SOL6uBTW0Q5sGqxL_0WRA_lT70nh8WToqEAa4k3zZZ_gC8EGcI-uVxvKtVLB1cIk4T3SWvAJ9vRxdc1aN_BV5uHUh9wxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید مارک لوین فرد نزدیک به ترامپ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/22012" target="_blank">📅 11:23 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPXGSc0vUcfW9P6hQHnVkzR35VTx_K24cWrSEZXJqVsTamokofPma_gOMySwkg1YvvmbsQ6hBIy-41CVNOHUHMyNWFxJobKdjMRF6KWoOefwJJxxnM8ZcawznjciyBOoyTHNEocdp7HdPLHHe0Otl4jSC2Avwfpm0f6M_o0eHOlO2HMuyg364w6ATmzVyMrmDpnEWhiWU7ovRR1NswNdOOWmSfuzxdkI7qUrb2KWh_93CEmLP7_FMbLDAnAGZpx8rr0NwAm0wPzYoGRIKIuQNesxF97dRF81Zq2wBl5CSjFqAiT_X3QyxcYHb8fMfLl3OcoZDnWFLjAcKX1pSEm5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گابریل ژسوس مهاجم برزیلی آرسنال کل این زمانو صبرکرده‌بود که انتقام‌شو از موسکوئرا بگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22011" target="_blank">📅 10:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22010">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWSEABgeMACAkw7RXhuCH6zhp5Wst611k95ZgxZ6Ql8wGg77RXBvDZJbryCHNOObzTCG3nE9QrYqJxcnRdDCCh8mCyrIoV3S8GE-fi7GVIphm0tBZJzv6sXEPJxr2TSUXKiE41C-B4U39ao-13cPYv2XI6D0hGyUmXKl9iMuym6LQ1HwjxBLzqN7XLU6p6CprNxu7wWPz2Hx2MmqhtFqfaJaxgGOjkO1C3WTy304EMsEJzpKVf-WQEjsl6faGCb5NvRsOs5MtC985I-Qodgdfhv4X5rws5uHwfXvh3sZwHoIejBghsBYB00PQ1z2Jut2vNwIL1BDojlHyqNzRX-cqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22010" target="_blank">📅 10:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22009">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLrJOA7tM8fPZOdFQUBUdVfZONmZizzX1YvDwSh9WHGgU8uVIFT43opX3OVzCIkbD588grYxyp5iny4YLsLSNJYP7qIEMkD1QtIIPW8NKaDaAoa9ag-QmtJDCe8LXxHiNCx9zez95rKuWJ5pxdy1XffWXujeEuwmMWUqJjUTbDAGLP1YBFPJT9Xp70BHgvzTwvElp9hmDp6LjQOTmFHqy4LWBQEYZ4DG47VDr7XKkLb3RGGqkl46Y4ZJxZEzyUC8NCPwxwLPZ1SIExReWUwEQh7M8DZ5SHSltLOFcCtodq8EmUMYpJGZl9oYI1ZHDfVpjuW93RtqWxaZplpAPtWnZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/22009" target="_blank">📅 09:55 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22008">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YynGhTVyQ45MoD0kZIMmj4BE2s_d29cYPioSdm_afkwJetFWVnufnamhldWDnoT3m50nWoEbMdLitc81GoGz6Y7RMB95QL3rrSt4iCJeI9YkzfAXgQwExNLPE8kt94cFqc5XbsPG9GeTTI2SoD8ftam4vEy8KByecTS6QNOCoLL100v0EY0JoSqwu80mQ5TZoDYebfdbsIf6P84fBC0unMl-nzw-fBre_W3Wm38ICPBrNb49PPySlE3zCK8b1adpvsxJTGd7Xz2qoh9RN_ujHPFRGN9Y4FtnyOPeL2UrjOj-4-xduQOUFonJgb6GVmnHJY5SBhILZiggSeYzf2wQmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22008" target="_blank">📅 09:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22007">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdW9jCNVeQUiXEbPr5AHzj9o52oBy6IAKcI2LkttPVrbguByjplrAznsRIxJGzWdxX0Cxpiab0O7WQ0yGLy2cBz5rVsgGJmI935RFuQLK2UQpw2sdnTL8aQg1Lta7d2Rud_M1sCiyfJoWGwQZ1y3Yd0qDL_UfJd_ZNsV7h9uzueFg1BQYDP72cGL7qdcwJNkfGaCavUdhBH8h8UNYc2VDqveZgN1ghqZhac4wkccSrrPYQd6DM3Mvfmm8E-UezsGTresJkaADxoVIbnYAfW7LwyljxcSoNmTFPkmNmP5CwcJrhAOnv6SC5g0hDL9lKs0HJGva4ruMLeDbNLzPDEdQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرانکی دی‌یونگ کاپیتان هلندی بارسلونا به دلیل مصدومیت از ناحیه همسترینگ یک‌ماه دور از میادین خواهد بود. کیلیان‌امباپه ستاره فرانسوی رئال مادرید نیز به دلیل مصدومیت حدود 3 الی 4 هفته قادر به همراهی کهکشانی‌ها نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22007" target="_blank">📅 09:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22006">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=Rmn1qYvb7OnUwzhSJVZ43ziZk9gsqWbzvVjeXcvgZ1561MENjmKvsZiOzNTzOeXh3Tn6HPbdK3cfb1u2QTyev77o1nrErwTcVl7f5M9k8qaNPKOEIj24bcri0iR_N57TYdpqi0Fpn9qS0UkKIaTcoVeBuHb6OXM__8NKrEECOzyWe9HRdj7-we2qXIyPs7AeUCL2h6kR486VZpvXecFlfxjLYuKJG3SyJl7X6nViZnVyOuuhq4NGcW4scDqrKmG3EoqV-LYEnf2YDourde4lLy6JKxrioJR_1L8iBLkfwHnSGuPszB2AAdo9W3bXBDwcpaClrfrTYYkSz04EW1nJcafCfhuX6YkSz7ZhBz9uNiqJGhUU3AzUYNOHpKeGGjTlI-Hnbo45DqA731ddM61RwwGuG1GvYQacpt0dv61LfKZFQHrWlYnUNpSaLwc1j4fr35ruE6_IyocB_4-JPwjq2rabh7iFdFqWEcKmROJNsUbrLULrayqjfTCARDKih9Z-cGf4rcZtLzHpTRyXGVOoVNhOzviJB-Tkhv4uuZnTsV7_SVlDJRcoklMaWLOxqqywQ8TxoDsUYMUsWycl8BQFXRaZ09T-RHS8qe5aFh2RLISYEgvv0JC_Bo1a5bjbggy8qZw--tlZWVMqkMafh3aO0GvMyCucDkbl-J7WNaCsVXY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=Rmn1qYvb7OnUwzhSJVZ43ziZk9gsqWbzvVjeXcvgZ1561MENjmKvsZiOzNTzOeXh3Tn6HPbdK3cfb1u2QTyev77o1nrErwTcVl7f5M9k8qaNPKOEIj24bcri0iR_N57TYdpqi0Fpn9qS0UkKIaTcoVeBuHb6OXM__8NKrEECOzyWe9HRdj7-we2qXIyPs7AeUCL2h6kR486VZpvXecFlfxjLYuKJG3SyJl7X6nViZnVyOuuhq4NGcW4scDqrKmG3EoqV-LYEnf2YDourde4lLy6JKxrioJR_1L8iBLkfwHnSGuPszB2AAdo9W3bXBDwcpaClrfrTYYkSz04EW1nJcafCfhuX6YkSz7ZhBz9uNiqJGhUU3AzUYNOHpKeGGjTlI-Hnbo45DqA731ddM61RwwGuG1GvYQacpt0dv61LfKZFQHrWlYnUNpSaLwc1j4fr35ruE6_IyocB_4-JPwjq2rabh7iFdFqWEcKmROJNsUbrLULrayqjfTCARDKih9Z-cGf4rcZtLzHpTRyXGVOoVNhOzviJB-Tkhv4uuZnTsV7_SVlDJRcoklMaWLOxqqywQ8TxoDsUYMUsWycl8BQFXRaZ09T-RHS8qe5aFh2RLISYEgvv0JC_Bo1a5bjbggy8qZw--tlZWVMqkMafh3aO0GvMyCucDkbl-J7WNaCsVXY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
​​
مجموعه‌ای‌از بهترین‌کنترل‌توپ‌‌های سرمربیان در کنار زمین؛ دود از کنده بلند میشه و از این داستانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22006" target="_blank">📅 09:02 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22005">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWDLdjquJ4E6wfnTCWFe3ig8BNscDQpVnsrfE0GYA-nfZW9oPs5oIxCz3TR0QKt5zZWxjL32Wi_scavAP-W07kEjyYAZFzygqxLD--tWRQRcfxCHNd4DY4tlgk_gXezAKcsnTDDP3EC26z7_vocO-eyTn5MriNvpeDs9nAeADaVmDJH0iNTXYX_CIbOhrkBuR0XvZYjhFRaUYJJuot0QEn2yamYghbUnLIA3PAcgy4SBk0qJu8yJh6I6dlW1YcHsI8xgEr9ljgXln8WxyrO1-aXmGS8GXdtopv53_lSyV4Nu-0P2OdY3muWmepTDq0L3g-oJfF2iPnvEvsgk2h5Tcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛
از بازی خانگی بلوگرانا مقابل ویارئال تا دربی درکلاسیکر آلمان و دوئل شاگردان اوسمار ویرا برابر ذوب‌آهن در اصفهان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22005" target="_blank">📅 08:04 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22004">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMrFiKUnQnbNlBTjuDZw50KdQjPtL89_85f1vmJ8uElcOvyir__DDSOAT3gDnqZDk9g61pHgAqFFyO_W3xa4LprYG6k0PeeuF9ot6RQ9ucOMsMiikWwjP96fkrVJpE1HkVOQTfqEB1_98o2sQNJXMDkwjqF8pLlOeWbbhFQfkVb3dw0E7f8KsYdsfLjC4Hcu5JCUa__xPW-FK-iIH61K8M3sVg_MwZcBkyk5aVbaHSg9TxNg13rAYzv68cPElE4cCsF7eq60foNhx6h1HHGBpYzwEcIeQLE9egwihbplrTtP5YhUkiiIW-34bSvWWnEP03MHt97Z2uX2p1FHs_WCFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌‌‌‌ دیدار های‌‌‌‌‌‌‌‌‌‌‌‌ دیروز؛
صدرنشینی آبی‌ها با برتری مقابل فجر سپاسی در شب درخشش روزبه
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/22004" target="_blank">📅 07:59 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22003">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6B-iSf_g0QlHNxkHwhrxnqUhP1rrB9PvlxW8RbWCf_-H_7hgK4XwFRqBaDdgsw1sZtPmsmJj9ce0QqLPOrc66TzsiO6SUU-xMyJKddoZw2FWcrR6jgLs3M_Y-0q35u2-LQLZbgDA04DKHj-rxxLdwN0U_IgowjQBpmcLdXgv1NIOL88SlMlJt8rr_heGwhVtuvyLOO-ja_8MZs53L5K70_vIfLeAMyNI3TTIe-JudR0zpqe8FJAMlYelhFB2vfO_9-jVaNxniv93cafRzy9yrjShcyfO1VCNZ_2JH3BiCKNb-u63aexYHQVkdFqW-zvoYPXqa0Kkk2w7WYENBOxkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین فرد نزدیک به ترامپ: علی لاریجانی، علی شمخانی و پسران شان دریک‌ماه‌اخیر نیم میلیارد دلار 500میلیون‌یورو ازایران‌خارج‌کردند و به‌روسیه و سنگاپور بردند. آنها از ارز، پول و طلا استفاده کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/22003" target="_blank">📅 00:21 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22002">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkV5F_1dsws_52GFBQi5rPD8bMfFFoyJXBpL7zVBaUN8YFWuqxCgmjzJs4-xPXRdOcggDSY_4HdAPCSCWzzmwvCeZsepzWvR7Y_X-EnyLInfjjSmiTul3cdfE7ivYlg1EyVMZTkhJB6i7dJeSamgZH2hmLE9PJrN7gPcBH2jFLkitb7AzR8--q7QQfVoyQ6SZS59n8aK56K0NctZbfZt7xEdOls6CHwFnN8NcWu9bUNCkHexiXqxOi8Dr2LDpszY1UBuUraj-DiDM_WxCyOmSpBjQilV0FXsNwdqwMZqLXHCKULrQ9myUjCCq2bFdeGoWlg_j3Zxcwc8E_sIEL_xbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/22002" target="_blank">📅 23:57 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22001">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkswPGq6iAu-7wd3-auaNipB574PP5QNBJPfcDt2TITcelmOgtW6EL5EBJZT_l1FhYsdOUzPMrKfwpLsd8WhJpQozmlkaSn6UBzhSvOueER_0_mLnFxGxWMmptdCXN-nT_uskuUzNPH2U8DmMlDseLbvyVeJ3W1FvOBr0p9fZEyYD8MR17m6sVvwsmb9vF95kr2SAvPD7Dh4QiPLL8D9SKZTrpF4taQsEzBSfCzVlLKmaUrMytDYZvZV5W9lV9eHrhYh7EW3uB1qu1Sv0BFk3TQ0ns2QXBtDXxXlfi00j8BpSkAVQPV-pZY1FT0zqXxLqKuukLFGc673U8pfNyuVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌اوسمار ویرا سرمربی‌پرسپولیس؛ سروش رفیعی و امین‌کاظمیان علی‌رغم‌حواشی‌اخیر به‌لیست این تیم در بازی فردا با ذوب آهن اضافه شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/22001" target="_blank">📅 23:44 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22000">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=VRfm-eX-5FXWi2vklrBR-Naj_0isdPiJCuAe6FPad2DdA6iD9XgO8MM1znRTKR8sbZnk2bZveRl2XYizsnES8Mcvsne6-NZu49tKYAVUGJQR9myXt_Va4dCpXk8akdIT-e7-4oFmBbWnhGOXfxGqYIkSHZdZoV5VdGS_dW2GQZFNkbJKRv20QwGq_kcmo8Gcg_XdMRIPy2YUu5-imhqYpth-h7pIGhMQfLDYSkoQvJlJLm1djdh-E7_SxWd3s7ItFa6WMGNL_j4k-tvWukZSGOQIEJyH7ewW7tXIIQFbpUGNUQjGNFW4lvTXOG3KXpU8FbYW49hxdDNFDjebebl1LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=VRfm-eX-5FXWi2vklrBR-Naj_0isdPiJCuAe6FPad2DdA6iD9XgO8MM1znRTKR8sbZnk2bZveRl2XYizsnES8Mcvsne6-NZu49tKYAVUGJQR9myXt_Va4dCpXk8akdIT-e7-4oFmBbWnhGOXfxGqYIkSHZdZoV5VdGS_dW2GQZFNkbJKRv20QwGq_kcmo8Gcg_XdMRIPy2YUu5-imhqYpth-h7pIGhMQfLDYSkoQvJlJLm1djdh-E7_SxWd3s7ItFa6WMGNL_j4k-tvWukZSGOQIEJyH7ewW7tXIIQFbpUGNUQjGNFW4lvTXOG3KXpU8FbYW49hxdDNFDjebebl1LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لیونل‌مسی بازیکن‌سابق و اسطوره تیم بارسلونا یه‌تایمی کاشته‌هاش حکم پنالتی رو داشتن و تیم‌ها به هر شکلی که شده میخواستن جلوشو بگیرن اما!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/22000" target="_blank">📅 23:38 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21999">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-No92zhp2qqXRFwkUJr3V65MFeiNgBIfn2hjuyewWd0P8famp-cHLXTV7tnQIhQ3KoJcwTylZhShR-v6swoE_Ymfo_ZROykBwzfgYczbG-g-A7YpHatn7M9Vsz_gqbk4_X568kb6nokfzP28Sy-iMQytVVu1kAt3WbFPUJ090gu4eLKoQyVcc1Ee0jjSQUfWLFqOlcEMdTBk3k_xC74aI4XusXMlL0YXsScYDA5CbA0E_vZXGxhRS4ECefPreulqB1vEatD7kStFR1XV9Ve9C4AeeiwbSLqHhNRIGEk7l8ETLahr7D3J4HA0-B_aWuD-lKHr_iFW9yCRzqE8IwRng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
سعید مظفری زاده مدیرعامل تراکتور:
🔴
از سازمان‌نظام‌وظیفه استعلام گرفتیم که اعلام کردند علی رضا بیرانوند سرباز نیست اما باید تکلیف پایان‌نامه‌ دانشگاه‌اش راکامل مشخص‌کند و معافیت تحصیلی اش تمدید کند. او طبق قانون مشکلی برای همراهی تراکتور نخواهد داشت. تراکتور…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/21999" target="_blank">📅 23:05 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21998">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=IT-C7heW8hi8Wh2fQ773wiFtLZWpLY-x31_NGyYKGQDOYFHgsnlJ43k6t_hrjwH8nnb7-_1yPUcO8MtOSpm64qjg6sgsEedIq5eniQt0lzYSk8BGLIWqX6Ia_Rm9aa-ib0f-pwlFpQsbmDDM45z5A4tjWbhZYINPjRNzYvjs3Nr4JSleBp3epGnqrT1VgfoOYAFINxU9HsIC0gD9hYpHe-Ez0pZsuUObjeR_hYeIZ3lQnG9Tm2WT4m1OetQm7NUeN_5Lk57w5BAEMVPnXwGB4QJn3skpWUre2ZNZtHXaQlThf6j25obllWr8_otMjUnK2t_Lf3Gz4ioD6_QeEsVpYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=IT-C7heW8hi8Wh2fQ773wiFtLZWpLY-x31_NGyYKGQDOYFHgsnlJ43k6t_hrjwH8nnb7-_1yPUcO8MtOSpm64qjg6sgsEedIq5eniQt0lzYSk8BGLIWqX6Ia_Rm9aa-ib0f-pwlFpQsbmDDM45z5A4tjWbhZYINPjRNzYvjs3Nr4JSleBp3epGnqrT1VgfoOYAFINxU9HsIC0gD9hYpHe-Ez0pZsuUObjeR_hYeIZ3lQnG9Tm2WT4m1OetQm7NUeN_5Lk57w5BAEMVPnXwGB4QJn3skpWUre2ZNZtHXaQlThf6j25obllWr8_otMjUnK2t_Lf3Gz4ioD6_QeEsVpYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
مهدی شریفی مهاجم چارچوب شناس این فصل فجر سپاسی؛ استاد گلزنی به تیم‌های بزرگ ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/21998" target="_blank">📅 22:45 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21997">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194acea631.mp4?token=p7rOgaQnOz9NPoCgixvzdsWUq7Lsnq4QBsiX48ATpt8wugpdVLitvobIMi1Q8c4HMBgC7W1lrKDlXls-EXrW7zydGWo04qKOX-Sw4-Z_M3dYn1UE5Oj_ePwNTNTd026aoLvSsV8uX7dr0Aysi3waYElHichxG8HXYSTkUKFN0La_mbsLaI0HV3siLpZDd6iKqvu61EhXScAGv7eS7TwgZBvCxmtgCZCv4fpNb_QLjEr_NVX7LISJcE335qsFXGKUBCk1jRv_6-3HlfFtFsPggkQFhOttMvQx_NWLA4lPZZTV7AUycpOhsaNmFHPvFsNnm9fzOalF7ttvjRNzavkBeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194acea631.mp4?token=p7rOgaQnOz9NPoCgixvzdsWUq7Lsnq4QBsiX48ATpt8wugpdVLitvobIMi1Q8c4HMBgC7W1lrKDlXls-EXrW7zydGWo04qKOX-Sw4-Z_M3dYn1UE5Oj_ePwNTNTd026aoLvSsV8uX7dr0Aysi3waYElHichxG8HXYSTkUKFN0La_mbsLaI0HV3siLpZDd6iKqvu61EhXScAGv7eS7TwgZBvCxmtgCZCv4fpNb_QLjEr_NVX7LISJcE335qsFXGKUBCk1jRv_6-3HlfFtFsPggkQFhOttMvQx_NWLA4lPZZTV7AUycpOhsaNmFHPvFsNnm9fzOalF7ttvjRNzavkBeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش رضارشیدپور به فحشای‌ناموسی عجیب و غریب گه در صداوسیما جمهوری اسلامی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/21997" target="_blank">📅 22:35 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21996">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVzO_L2rUyzWlN_YLRoYPWbzjps8ONxBaR-MYEsctCcc4_k3qOnjGDFuZz3CzvcVhAy8J8J964wDH-gcibV_lkjDkTj87JktBO96tMUKXfY76cvrRTtDuHucwThGM6fejPlYxq9P5i2J-htvHUJ2P4OuGk0V99_2M7ieapJi4PKegDyhtDlfJaqJ44GOprbjo4vrtjNiuCq743MtagqYLD0VgBZBI_SxnAPsUL3Jkz8LEYLppb7NlUx_kp7BBvcAxMmPrJdAu2u2ovEb0j9NJ90vR4FfpOvYYPegxGVjfBXyq6E8MuEMCDdWE641g_eQyURbVX7vnAWxAo3k8OFKnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نیمار جونیور بعد از گلزنی‌ اش و شادی اش به سبک وینیسیوس: هرگز توهین نژادپرستانه رو قبول نمیکنم و به وینی‌گفتم که اگر دوباره گل زدی، همون خوشحالی رو انجام بده. منم به احترام و حمایت از وینیسیوس این شادی رو امشب انجام دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/21996" target="_blank">📅 22:21 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21995">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bebf41053.mp4?token=l8MnBK9o_BbN9Wwg9ssFgL2JpyliWDPVMZjhFdj02Gy1jXW2wBotLgH9MG3mij9jqVRE8Xab1YwIqEb7cCzRMRb1sU-uY6Il_KodBzYQVpV8bWK9H8adB6KhLFbYH6POHcv_MBWCpxkxQ8yKZMuIlybE6zOxfEx0hZJQVwZkSYyYHq2O0nJ_tqIqRI-xhPNzJtfrH0s3IanWIV9Dcf1p13xBpk3lJt3fXMeo4VswOns6KR8Oq2LgQQHj4IhYb1d5PtKgpAmHT6ausoo-J8-h2JnR6qKGuzt_zpDvKZh8nTawT3U3ZaCDTOwy7KyoAkJ9ehY4HauaDgqlXtJ38bDshFzEZHZWGxk7-Qb8fXMh5fm6K0SdRblF7sRQ7FBdtKhx8QNxuaVx5XgqQ1TKcLZ4lfRaNlsJthi-9R_8FWarw5wtvFq7iLSfiY0H81wW8PqYzR6fawmhKEiy3Fxu63-1brqT-OL_gnKpCudWlAghDq-Uvp70eM9fRf6boDd-gvLULTCWTKT_gW2I1fG3rFRx8NwAenvGl7dsJcfo7jtw2wB6Q2na6jfz0woli1-CSFdGaTeRndwdIuO6l5xccLlLS9-w0fPmLO8_zeSU2fXysIAi0ne2w3ABvwfS1xQelodgQri69gj-IIQRSFyMU22K09aEJuAz1ZR1GbhUjD_go18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bebf41053.mp4?token=l8MnBK9o_BbN9Wwg9ssFgL2JpyliWDPVMZjhFdj02Gy1jXW2wBotLgH9MG3mij9jqVRE8Xab1YwIqEb7cCzRMRb1sU-uY6Il_KodBzYQVpV8bWK9H8adB6KhLFbYH6POHcv_MBWCpxkxQ8yKZMuIlybE6zOxfEx0hZJQVwZkSYyYHq2O0nJ_tqIqRI-xhPNzJtfrH0s3IanWIV9Dcf1p13xBpk3lJt3fXMeo4VswOns6KR8Oq2LgQQHj4IhYb1d5PtKgpAmHT6ausoo-J8-h2JnR6qKGuzt_zpDvKZh8nTawT3U3ZaCDTOwy7KyoAkJ9ehY4HauaDgqlXtJ38bDshFzEZHZWGxk7-Qb8fXMh5fm6K0SdRblF7sRQ7FBdtKhx8QNxuaVx5XgqQ1TKcLZ4lfRaNlsJthi-9R_8FWarw5wtvFq7iLSfiY0H81wW8PqYzR6fawmhKEiy3Fxu63-1brqT-OL_gnKpCudWlAghDq-Uvp70eM9fRf6boDd-gvLULTCWTKT_gW2I1fG3rFRx8NwAenvGl7dsJcfo7jtw2wB6Q2na6jfz0woli1-CSFdGaTeRndwdIuO6l5xccLlLS9-w0fPmLO8_zeSU2fXysIAi0ne2w3ABvwfS1xQelodgQri69gj-IIQRSFyMU22K09aEJuAz1ZR1GbhUjD_go18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول رده‌بندی رقابت‌های لیگ‌برتر درپایان دیدار های امروز؛ سه تیم استقلال، تراکتور و سپاهان یک بازی کمتر نسبت به بقیه تیم‌ها انجام داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/21995" target="_blank">📅 21:59 · 08 Esfand 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
