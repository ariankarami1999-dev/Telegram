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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 12:53:21</div>
<hr>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzKuMUwsX_OEQ2A4CewD8M853V7kWTjegvX4Jyp9nEl1LBII_rZPOhw8hHOtTczbV14JgxLLpTWJ0kMrRmU-6-IW565OQs1XQSBJ869HlVy6BQDQM4sFeZ4llP3K3CyJIswa2oyfdfgXZveeyImfTsyrraodLrzeLPWgiuYFqIjJWeJDFuggISAsxrh7CndpeACN1rvlQqUAZ3qj2ulh9Jtzj-ZS1sdB0GoMiahVjPD10BoyR8HcQaeekPFGaSMvBRwaLq5itH9cC4LUi-Q1JNffsSfZOpKKfkZSiFnxrCcEps8tKEu4d6GcnqaRD5CxrOBaWFPTJ2LUEo0S2tbwAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ien6wdLFa1M9xhYdRin8bGZ0aIfXR8lF9ywnVH7IrtDREzZVUtCrrJLA55akbk8clB71c4WfzJbnI6zzrXZdC4ILzlz8VXdL13gp3wa1XeUELMDewoUzYC7RtW0S7EolLZgRZzk6Rc79_7dAqS5XR5oSK9nxZLI_8fyKx8Pjrr-cuE_m8Ilfr5E_Zl2Iz2vRh8kYfMJdl1B6nJ-6vZDEOnxkQc0rDokW9N91GQxRcaY_n4hFmhc5WPIzz7fTJ1qp9IzEMpvSpsYs3FpMO3SLFU8ToWSvb2qeH9-JMUvPGQTya4jA0VkL1NKQ8y5eKNnyfg7thQWlpRDOwgCgIMEQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRHynLFx9ET21d-pFx9x5VAUdI1dNQ7BXT10fJmYPLDYUJM_i5C7rKLq0Bbk6NaU4RwF389WTUqBQLI92CHMNESpeXbGIN8YBeKLaTy_jT3Qn7gE5Ex276LD2GQvJhDqU-yDrTh1xvpRGsL5r0zYzc30aS7zr-SqwtuPbDjd9dTozA1skvnOJy4qaPtCN8IzZy2N1pM1b63gZusB1iQXvX5j-19GKURhIQ63rEjNjudUFQM9KWJmGu_GTj3wPmcZVhPDxuT0oA-JbMsuZTn5Oi94p9ocf1rwqflwetq_PPCGw_lrHI5gTaSWtZ0jpnUqmm3oWkWKNmTQ8NsbT4VIiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSTQjJQd3hPXHw-lWMtIAIkfCqcMMqFi8cxi4qD9ovk5ggS2n2uOvoL84HoDfyS7ibQq6YyQsTGsSHJyDpVX4eqwYTFv2q-qK-9sf_fmsTPgulIV7nXQGGwieRsmaoyjixIrKE3tDlbQ40vOHiySPe7o8d6q3W_qrIrgCkqxsahWvF-TzpafERqqh1Us8pVwXn5icnOMqgfsz6IAj-wmZFogjN_aalBzKt0UHIPbeO2SjdWTxM8OCQ7zofvQSErZaONlmtAbLza4zDTI_jcdVbp_s7k4NQhvOsi0ZreKumhnMO15XEzrhKZFaZn7oi0wkKohwTlps_L21JW8hcphTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/persiana_Soccer/22120" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8fUBx8FynyQjs_wrZAHz2UmKG2Teq0sQw-oihDXvaNypk5tUACTZb7maAH2CzuUQpmHHUleyDXGu0N-NoeM3_g6jdr4L5hVDkbLDbD95iuR7DMstjwcwCt-qnnZuMaVZlFC-lsvQFBCb8e2yTN-qPBecidk4qWWEbGEP6ClgZjZx-RDiIVbnDqDxLlarDFhHGLztVFCKiYWke9TZVfPv72ox7XxuPHFwDM1wiltjVJLtFGYfyxfUlqiUqIS2HE4myLS2yvM2InQw2lsgoS-y01CA_1E4UtbPF96hOyuSwUbOIB3oCAZaEqk_DD1fZ8CbogD1eUXvm4UYjDhU3jamQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTPqEV5sx3SOaE38WSxobvwitbbB7RT2FSIY7YHEMKV64egQ0dU8D62Vy0t0FwPMFviAft7CZb6rYunzMIH4l0C0oH3gK7nFifSh-2kmicMz1mihxkY9HE0dfUGglCKMVBjGpvEIaZ_x5S2Lqe-8qPdc5Z0sFzq_nFPK4m9tAkZ92a5B6uetyDtBqU9LR-SwHFwKYPZuiDHsG_zNR9CohOWCjz9pc946fu0ETxpdjHuEbC_fnsUop7q41Mm4ZzwPabBHNVRPIoGF2svw8lzlpRxKbZake5VLGsyRbsCXXWpDNiewm1P9NHYWBPW-fRb0C5fL6pYF8Un6m9BAivl9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/uQsXMV0qRFlT3EPDMojYOkubsn_YlpqTHBFmwN34WM5Jh-ffcxDVsHF23XQZXpdjJqpu5xbAAAiWBcbrdgrTYUZWPE2YMQANGjROQmz-ZcLMOXagI5GegMwLz8_eRGChYyBLYY9TYixAazL5j1fuRbHeIHW_HWkkVlIbVDuFnooKFdA84sYTHlh31VfEjmu1lOLL5eaiMM26P9OOYmT-Uo0g8lPToLxYmuqjfnC0hM1G_OVv_2NHaQzrsp-ehQ36o0f8cx1N8DwQXeEfqWb1gasOlEvip3aT3En4MdFl_E-c8BboJkaCmGyC4JD9GtEYvWvF2LW7VYwrk5zl3lgxLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUg7deHtpops_hMEXg8XelEjMxFooCLYUj1zbSrBE1AzAGlLrHelwrhCnc768pjJD8-rqKCBBPIjFN8T4gfz84kcPwnaQX6XESt94tZGFLNjLzoxVkKs4_GSMHAVYCyLv2gGnSkkKPjrN4Eid-ProapQMVceKaoS5Wk5U0cUkZjcTiAntZfbTpBxlekrM12Ul48k9UAK7tO2o454s-aUStmzwATc91uidkWLJM_rARJ7ZrMqB8-73M_RjZb6mbM6pXy5Z5X2rRKe3tvdTfWJn_0zFsFwAyJglW_VwN4o-k_gSdRWHkVWWizahNEXrn9KKT2IMnRCYVU5hawM0VEZQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ET4wljfGxeN8Ysuon59b_A2lXXvgdJSL9RpeN7rJ5eRbY6Gqvj6LyYJDRCZkNzrh354W6T1bWSaMwCObMVx62IHV9yz2gNbmdlejle0aqTl7BjnOJW1N7cgbdOFYO-se6RW9_sWggLUufFf4GjVJHcmSgkLE8W-zcnzBzVMjlGuduNfMFK-Irztwmy6sLpp2A3dXZC1W7nm-BMwed6l6YsHjlLlf8RInLNk7yUtwKwwsxyXSh5eL99sNzs8nNG5dHx7rO3YgI7UgLAgCEqwO64jWTc_5w2rAr6H-sZBeO_kXAfY-8rnHsUS6ENDqb-3zLiy5Xuj-xZlPUlaQjxXQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8c-WhP5w49EiLZwCL-nRUXrcDnL3pcpgVO3sTJB4Uz_cevQfLL4OJ9iw1clhXFiM5ej3OiVrwjBdnW-wHuYrnFu68C7rx_xL17caj45noLLLEyc55NvKGFnbrn37eIDNrXD--RCrxPFQqOf7Xy1u9-Wf4TB4IDqEbjoqISFg5yP7JIFY57Hhu2hOfv0DXVd3udDwCYSEHS9BnH0AN2T_0MB866je-s7tA9xLRjysQJEGKOm5-QW603PVpS7cpPdlo4V4icVu08WJWvBsXce-2fmdT7g_tupScdzy6uocQWqRVQmHnsXP5Q9xleSR-yWd662VwCOqDxPgE-V3efbYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCZbAy48bHDkxzjDsxaLPlt74ZDUwlyjAWQF2Cwu9jHx8JaGpjgI7RyHxmi6fp2g1AtnnQ3nrpJGi6LXL9RJ6Ewiv7gGFFOsG2wyDJUXnT-jaBUUNRy80cznhO1Z_XO_gxJuthjbS3Zp0nRbZT4FcM61p3td4y45sczopc825CQvPmwvIUJzKUnUdqc_KAqe0n9SGBZjAiPbF9UNZev1FoBOYS70tORHrqK4FEuHWhjoV8CnBJzVTBvEol7vCojo4Yl8scKadSra9XJy_m7yL7B9oT1a8E1EzHnrbi3VRofW9eUyB7FqDs4cNoQkZNpWFXiOTQMfDraXwI0SauTmWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3JE2O5WqdA7Fhp_BjV1Zna41WOfHlpILM8fOX-1PO4tZG9jKixkZ900A2_bIhr7du-T9tgHx1unoH6-N4AbFXwfxnaV6LSRVKUQMeAi8zAgnaDSdqlfyCyZ6uqaZv1ptjdJYOV_8Zw1x1DWd25DmBC88H6P_L_K-w1dif5lYvwwE3TtHoj6XvU-JtEARIwCjJH8JBJyreu-aa7c8ibyBsHT1FjW3LE9fSoCaSnbE0E5zHhknLE9bB1_Stc9Ie26HMMEbU2VvDNiblW24kXll7xIzyyP5-XEXEUGQj1JdtpcchBm8fYNSToKuxpxHl56mCzv2jnn_pXblKrvqHFUtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqpRLcUGyUSXrwroWtu8y3-OzLaf6rSNlMporvson_siWV_2Du0VmyTv3NJ5G0e6tbORy6cDAToEYV0MVciX8jkI7OJ1br0RNREeViGrjIKfF_l2Ybl8Pd8FZfl8m60-eDqkOAnZNwx2YFBTD7NO0Qq7HPz5UcVAndyblDoBuxZtOiPa3fdHrtYhfOY_e_cNJIovG7tXsEWyHDH78rbNwMHd15AuBqVvCewIAvgUs72xCFNYTxHbYQx_ZqS_dGRl9F8lIKHhorEuKUjP-yy3Sbpt1ffZmcn-hLdC6_s0V6fRM_FSir0T4sthOcUaxWsIKzEkweMM8l6iW7jP1rHQOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RG44Kt6F7x6V9WjlMFltWZoSEl5tgocR7dIRz0kWiSFAEZ2Sp89m30_nd_mkMTwEtptYbKm7dtzFxs8cMs89C-qL71PAiOxhVJp4gQFfmVNrG75dievQDAYtmX8sP1ntITmIuxVePoUBdzOtIH08yx2TAcT123V1xiDk5zJVcliJVRWvJ31BNOwqw3N5m03DZXUSuY8-1apWBSNKllemHW46b209EBNnjb3-cMkj_ozSo9AV1hpVtdlqQb2GEIPOjhhuU3kY7pDrFb8w-90yHfcmmkGsGeq0g6uReaxAs8L6ug3M6a_0b0G4azM7mjm9RC1fvl8pzH6I6e60L-HC4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbZ_0G44t4uCM25-FhP1LY3Nh07R3g8gOJ4FQApa8CaGGBH398831Wvwo8TZcwRX6Oi67knbXJ7Tv-eGGqg1s4j9AbamUKDf4cJoiFGIP0D-SZcS1o2-oM050ncPncgO8BfxH0mMW91VtWUFmK8nFsb4W6t10Nau6JvSwRxBY4xiRWXXot4gm3bh8TJrWmQdR0j605bRWFxOYK0tvT9vlH5sD1ou3aTBdtsYYsELZUN8ZeleGZ7_P7o1WpsiJSOZYjU_SOcgqRhz0NOEMM_EPizX91VkVNoO-jBHvC_iu3J5-Ib8W6NTH8RfKbWxvNSoajwGm6uC5xbeBB63Pfc1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5MGETIMt4VOXgrzTq81qUP_waVRlZRN__TjjNSKuS43id816bbUgvbrhQN6lOGpYScEe1HKGtOJGKHX3dobgjmhHY_qiKop6ETGxE19WrZNAnJSzBgAjRy_iNnhEkHebP_ODKHnM1gW3F5_TUGsn0qlGiwbOzmgxCLpSd1XB8NiHiUTP3k6U98xPgYklj1Ugzn7SMsBhHimjPSftLWuUGwlxSr2UkpMLAIHckLKD2j9fcot9FVXb6pkC3RpdJ2VVHUa_rlxCPuYSvxtdJ6Ut3x3eDH_JAlX3W5ASRqwOZuFiWZXKHmO8NyQ0xdMk4ZYYKOEDrgZ_dWhRW2JC5AO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXOjEHDYWMMqNSOivFJEi4YM2ahCX_vVEO6rMg9D0qBAmFLZIWaMNYWXHKSDhfDUOXwhxTuz9sFwSNEW2v7q78_Dk0gDqXpVYl3YyyMiDqc1OFN-1fSsbZulDmtO1qTQ1u6bvuqwaTrCbP618oZtUt5gzOKaK1pmPprNrNi5eAZS3ocAVCmNY_nThLo2C7aDXNv6i5dko447h1lqqAyAmywFkJXF7gDCXfp29xDQEDh2IMUxNtR3CtDAj35ZgRHXNFg5iyJssAxshQpkRKGwNN3gZ_wUoeWAvXN0xNxfLFBxd5p0E56n8Gq3hY60LvRt7FHgKwgwGdF1cTpwWGFNDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOJYK5uRjGWElzOLhyV_RZNq8YYhe2q0EXzkccPEyoYsf9D9nlr8Vn8vYnDmVdbsmHAiCMJZa8x32_bu3kl4liHB7dSG8VZpre6-vDsRvhcSh1e-4PIRNyUrPvOr3jET51PuveTlFO2nf94BKxmFO7nZD8PXBA6hlkp6fU8cHXqoqcbkaTemvIMGOr3FPbI_ZsItvL7q87H3YzE-pYXTnNNHMV5vCQz1NPElRyYJbGl2OmX3eAG_1C98tpL5BkTYaXkZX6pvowYWekDXonm4SOn3bgIeNFxzAYvO9vf9Im5_szv9ZHOFPL6EHeQMw9OQoONbKs1E6m6uyrQ3JWvWQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkaFtF-a4cvtJ09C8qMy7shLZJVYHPGjhNOLKffln7pTfqHCnPCp11KQEwVJIEqS9zgFZpkCjWERv96GURHwxB4fqulzq2LMiTsZPZv3mFOD6CMnRBOgjKP6CRSadVxhZ4ZXDnqc0ENJE6f-gYIFfSg5Y-c4oDxr2xfRf2J5hZAKlp4DXwQbrCbRtQFHYfDo1HzXpt0ioLvLv8lIljA7mtZMA-5ADlDwYyG6jpbEfRTIKMBsQ-5nnwImhGK7Z4SHi5xvieaZMKQckE2ZkKNyjDDdmYayy9005skdPMBMAjhMtBdbXRoWSAQ87_4I7WOsmRy-pljEDyXs0k5UhTtILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=lqf3DlQl08tsLZ4M0FknOIh3GTol6QsVU4A9NUk0XEHSdREEs6VxI87dmvvv7S3a-lVfyHflMlnobxnEZJ8fDvlXKc2yaSH0f2R8anlEC5eZcwJj-Cd-Z0SaIuL8rtAqq8ZNFE9kv-qnN08QmGkigIPwW0fRQZHovA0hg6aQmSIuaUqOvDdmVABiH50hdb-APiVPBhlmrCAkvvFtioitnw8DhNZeedKi_RQle-PX9-iKkUK3azAKSxcCIBKLvIf01kojlOai_HyVA8B2o31_4jKhsBNq3GMRdWMmwJTcNykoEiJEDW6s_4aXxJF9T77N_ft77HkvaquvII7vu7EWxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=lqf3DlQl08tsLZ4M0FknOIh3GTol6QsVU4A9NUk0XEHSdREEs6VxI87dmvvv7S3a-lVfyHflMlnobxnEZJ8fDvlXKc2yaSH0f2R8anlEC5eZcwJj-Cd-Z0SaIuL8rtAqq8ZNFE9kv-qnN08QmGkigIPwW0fRQZHovA0hg6aQmSIuaUqOvDdmVABiH50hdb-APiVPBhlmrCAkvvFtioitnw8DhNZeedKi_RQle-PX9-iKkUK3azAKSxcCIBKLvIf01kojlOai_HyVA8B2o31_4jKhsBNq3GMRdWMmwJTcNykoEiJEDW6s_4aXxJF9T77N_ft77HkvaquvII7vu7EWxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgJdeK89ZqHkIgKajFqjnLE1XeIN0lyCJDMvAq0RSnxa3rAwulYhzFsZ5pS2YJI-sebADmn1Zh0CSOS3K34G_Uc_IzI-eOEx56jHycGxIPwmMAWhy5zuzM_wBCL3qVW0pX8bHjnVucmoGKaIiesopXtlkBbr-SbxBGltE1ivlmteIKlP2FXrUjWYo16yvNLoEEXLgRda19_9VBXdwZool8wdd2i2YZkt1xR3HDRLOBusaeLYwR0negxwvuYvVHkWOzASGGmqokBcmfseZfaWwfjslO5Lx4XfK95H0ufNy1NgA9Z9vBvSdS4e6EzJBX28cogCqktE2kIV1quD1rDXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vH93ZOwA13oNzG0G3rvPMUto0dCOSnq5kjYI8z9Pk6aBnHICwTMa_bFkrBv33LiTJeKJGQ5kwdHz2iM1aJ2Zq17R6pRhoOZhdP1D6tWiK0ZNrXAhAz43ShvC4bBp05gkcqb9z1Dw-je3rIgHtz6iZJGMUUR7LubvicQiW4wST3M4dbV1kAc0DBOYHVz5dV3l-elYEhGSuFWDqcDonB_r3b29vOXWr-BAfTtHUian5QEKf7J9-LW2KBxx4YBjvUBl9jTgXiSFouIIkLrxXcGiZ_I5yVevluD8bJZLgym8Efih-sOQqhZZp7lMY0_QHgTXgM6FPRej_SS7K_B3_PMU-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HV64AJXziH5KRYqfJNGmwpcAQlS6TKeEZalH7Os9u0m3Jp3SogoouP2-JjyR6TWYlWMqxle5fgwLDndhDcooGI30CYZ4gvkZ4RYVib-2jgRjiAJVpMMMI58MhaoA5rWH9Gs3x_j97EJXJokIp_nppgaJMfDR3aeC7_U1bx8cPDerJny0W01l9y2FlofIEAOfTTEi8GEcGQ34B8vPi7zoZIqEdHZJJ66So2I5_m4RzeNPTKQ9wkeowBHyrUOMN3Afb_0gKSWOsBQ853-6F47jpJIdD_lIRMex-_pOxSTihAXB1sHvHf2HmXGmGQGJ_UcGXKDEdu0uZ-_zgomD0QYP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvme4GascrxXwGnx6c0rLxkpICq5-iLOv8AAmAhngTiavWdUciryqCMyQ3Bw4swqmhCYTCcjkjgeIre_KQNDkY3IaB3Cx4yVVeyYJIWl-NDkOpOontN0HMBxWgSS8cz761vgYslRZh1DGbyZlMRH5VQcPMX7JLTrKWJROCiz18S_YtiOJZ3xhGyzSYtkKpc--7e1vw4D1o8AUmnb6kN7M_J7O8Afkahel37M6QL6GVA4Y16EgsgxnHX29f_Twpjsti4qq_IBHOYhYzbqufmtJsuEd8FF-99d-kT3kICbnXuaDuXsalodFFuMgr-5CsM2TF1rJP4KHewQCsLod29amQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBVK2dCZPJnzFdnRcSOfTvleFhmjK4V2CdT5lvvTlmBUa6KeYpT1MUmaDF2SyOu6EnIypcWJqurGL-ZPXEXtqY24OzoY8o-BAzCTyZLsG5flAuIpyY1AD1tHwBNX-idTh4RBrA2c0NAnHO1VDL76PyKD2GCTGGl_OJ_ffy2POAzfkCrth39WlSQxD8xkp5gu7nl6RRcPkkS_Ww2ZG3_zYL9Q4_VXmcGChzHBNCdB8R2W8t210qrOm3YWFa57YoJP1CSOrN4oHxK9vJjiHCzvCc7OuZWhFMLvfjUrzxzGhvqlceAebbOSRUuj7wlynl5c-gkD4SdEI5TP_2JIZs6zMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJrq-xHACXua50ZnchR23rRRBTAJxeDRbHRR-MfcHBsysvQIn0FUZ658GSy9kopfCIq1Q-fF89KX9LmwkJ3u6Zu_R3gnelTSMct7pMJoZysUO02tP6kwl1SNAhsV2EjhgxQ8ld9c9eQToW7-k0s7rfe3xlCaRZQY2El41cmdEn2oW63shtIxIgjZP5mQZOtCNihaZCPcqs-g4Pl-n8W_9SxqIeEIw-KO-WwjzSY7l7jmQbT8hj60vdwFwqGphzTKuwYsLAxKOeI2rfwaWmLVS9_55RuYrZN0j4UWw_Qca-_Oukz5OUFk7UsMApBWZe-eBoRi9jV1oU72g-qNi17Xgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTDChgkhSXacAxkDpu5RoQz52PrCnhMy6pwq_P8TJgQmnX7Fm-Vrk7KqmK7IYsK9omijEU4wHIOeqKziNJUyqdMcsJHMfHEQJ7Wh4px_xiSM-JvU40AD7SGXOqtkaLZeMwRGwOHCLXJSOAxeSI0qqzuIuEYa-c1j8iKbMftipUmtNRRxH0wrxH_YxxhyXEuOSI0zP6FRgIlucxSav3bbVGsJrLtAWO20PlsUBciNLzdTUFHEoGyddY3IVXS6jPg62Lp_4EZsumuuGRb7Yv0UCrc8srtokncl8EAE8B8Vs3K2siRyOdnTpLsKl6_jFGJz3wHlSz7syM1XB0zCSZYhmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9LqWlcjp_u8RzNSBnOwQmdTRTQvTsRh0tC4pZwTSFpihDBpDksMMNCCiAZztnlZNUK13Fjm4lBAgfg1PL8TgPPL-7jntE5WNNkJxiqMA2d36YTqDlekL3EnFqQDcnSVsz32_65X6ga3wR7ztteYaS_EZC6QVj4hST24iJfYc-FJPv4uGxLm6SLNhjScHDDPDWJm8we2YWJoWMANBwItNnX_qXhpR_Z7E4UiHebDOe0G3__7oDZh_iPqreKLHZ1V_H3D-pWlCdsUq06eP-UUcWFqJYOW2IqshWUWojq0lGkUtBYrCMugQZts9KMId4p5gGEiQ5JLbJQT9rj5sOZEdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtFxy4-ul-oG4cxI0CpHXud44AdsCCpSp_Gfxd0cx8ry7sEOH-J5rZNKiuLCRNQA4slZ70rKDeCLpxgQjeBowJJyE9I7MJW6RrMJ7FqWtLDQJW4z68ex1x71XjZMxHXW4svcfGpDmxRjlJtdJgG1Td4ICRen0SJzQLmrujuuV1O3Mh0Icanc17Hw87GcetDHuYAYOoZofYAVq_CFZ2pzxBPAf1A5X8z3RhNLjaWmvcbdx3M95T0BoL8-5iNJMGMrSSVYocq8QfXFQd1lxjbH-g7aRKI0n-XU-rI_Gc7yICp4xCVWDx8C_w0CXff4YYTq11cUMeYVzMLNmtq3XwWAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJKHL4zDL19iFaXu3z0y61wfXXrYdA8orD0DZZPW1EdU5wecqnN2etoErpqVdE64aQx8dTSd_p71Zz7SGrsJoljWTbZnOmRveN9ZRbCCe0wriNNWGMzsbObuCvsD0nST1ETlDMV9oO-df0dBNrH-dMLRg_yOaGxZkulwnNOc5okAPLdQyKZ5q7nPQavnkVwmrzxD7BdMeUvXlif1Zz8Ir88ICy3cMViPwPJKEsxe4n_vszA8H5vVRUELcAkXk4GZg7cqpYDIcqbXspmZyfBs3BMMWnkKJR9DNmIbMfTovSsCNGOV_6dJk4Id7m1g7UOJ6M2tx7NYDiyDV5N6RMzcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fb5NUQAKLRysDhmZt0BNszzCf4yI0GndR1ClCWtM7eebNBCjV3GNPPc6Z2dxwaFa0TsT71jlT_YcdFCEVm5XpNHK-Z8kaOnoXeVpLiSHk2fNxbdoKTWTl-e7HIP-BcXIDEhFTonUql2h1gFrcDt1Uk4ELuxXDLN-cuzB14VrM3XvpO6Imh4V359rcR9vOJbRn_P_MIIOnsY7A1VkDYvr6VjsT5W0oM8_m3IvnhXU03CC0zPOXpDR7jpiyTFj6PUcwlY_Yypm0C5oYd7ezIQYi62l68ebKnc4aMCn-LEu3CV3-IkCXsZw46ADlFVPVKP5lioNCQ8NGsMwsVVMX07Hiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-k5O9_soLbQbI2oVNYiB7VQDOx2IbJiUQCf_U0d9dKKf6D5DjVjOaj6uUaguTVaBBYzv0Oyscer8l-AEyrkQPZV8tBdFOMOpOT8OZBNaW24uB9v-WwH9jqdRPJdBb_u1Mz4OdJkojNFOim2lmGWTbR-tcq-c8-5lac0k1_u2cZGPRVECV4WF9ZvpR_xoQHPHXe8RELpFlsccElgKWwVLBqAuwgN2-MDz2BJ5jbawm3Q2ZCVhOV5jMnyqmsn4XwB71kdIhciBFwljVIjsI-8JiBJBt96z3lfJs7OAc0GEoK_USBx0zAUqXZHm_cm0zqEyPnKqi9FBQenCHRBABiFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrU9gqF_LdpK9PVLAc8gIYGmHiMNmXtRH3rwT5zimJ-UOgeZXrbBvl5Ymmvhs4u7Rk-uFxe3uZyN6c3viMr9Xr28ESzHm93nHYBAyrTsJxyDskCY0O2dQtxnAhTcpQAJLOvu_hGbS8bEeafmtTW2g6-ffnlwA0pwcnNL55CG4Gq-MvFbhpFsTz7iEG-hzH71puezQHujbEOcs5JWx8CKGtKecyU6ffhKEKHuz0jmyhDwmSEhCMgwCwM_1GV6Ua1xnfCgfQ6C3NjeFwQUfs2jjieF_b8A1v8CQ3SzsqM2hKEkKi83vV61TdZ4WTV_4AM7E82ZcdjChqj2bisJYg8KDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLFtWAxESLfISDlFpDz_TpYOT-DaVbDCwai3CS7-1BipNlHXg8pDMYlUkjRmzHaTVYeNbRlt7oju-R4f3urVFjLdb_olYMSEupfNREmpRHa2etUOIW2tAdPmzRQMokbodXd-wyvFBTortIM729NDFbdGWwnkFEeycpCo74JydzJvV-qiclJuQwH026W1UJyTaPN0jjrVyLRIroQBxLZ6CKoXYS2MNKuiJN2P3RB7ejslwz_dlTcGi03bdSe0locRkjLm27HqRRNrB-YnpdiX0YdEGn2vL6KRm1JOSZePqcIGDT3fwwQPhU8-N6Jc5l0Wv8Pv0nfRaUdGf2YJnEsShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1-vMU7k_gI4IQPnieaB4UKO8VOrtXt-XhpS6JLlwCJEADMpW0DaHzHciUj9iQI1Fb-sii8y-VEw5JeE9w6YqDn77kIIO1qxDLyApeu-JaUJixQQrhOpZ7ex_IWROIwoORADtI_XRB6LeksGDORBQQAXd6bGTovZnoMOgr6LeVovVur39tYgkxinnkLy4jI5eKo4lnjljv0fPVe9KeCD2BTh5vcit8J8Ffc88F5pb5NWTnHf8Pe-dgMTSOVul-h0AeOiSU8cvFNGkxnRvHge8wPT6rSsTsBklCJ-iwhtwoj2L1TJnH7b1grbAAdOLqKd62QHcuyQE2sd8xPqq5WJug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jD2UD732_lKMwE5r8RviS5c_XtMMetR6qYsmOXwxfvFHPbrRz43md9xOq_uM43LEerIVkIaBTs7fZJBaS_mmLX5UOd7Djwm0rkjFjnO0rnDP3YJ_l9ylPsNJQ-BksmT-5H1vys3OSQdgKTLTcKqc-9TEJBaSbGZKNV4vDwl_G1nJfLSZraOedaqFhG8HEaXKBLCtr4i2M6eeh2RDsME_qm5fukzrZH6nWPp00eOiNfhJBQ8B9B4I1_7Fj2XocfsLYDEEKA8JyZ8I3phbhsdA62eUaLKEt77y_npVOxA9o2nyA4ZldiOtNxAARfCaxJxgk-Hl3HUb4ah9E79U00_gfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0lp8Z43PmDmdR8f08K8dcrVl0tQnJLRUIkXGUVrWd7Ssw1lO7pfNWUaA7H17bbsI3i52JtfimoaAleUsisngVDGe3q-IPRyeYJzTgwI3LmLAWRvLBNLCIakfeGMKdpdBM5Cgx9M8jlUPX4pkXRh6ol8FOGqnMwieTYvcCAfGNS0PPJvkFcXfzqV12wofl7qMBRJ7yXOI77QXyqebPmbxFGoSiI69zvH-k1689OkXS78xeQe27btmuehRY11pc1s2wQhIPWu4Y0Rs_UE3jv6h1ABstcZvW3sFkGBo0R8CDtN85oZwwvUbqXfig14jTwVVDRG7R5EvqqAJaAqmMWKJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5zvIDnlTRWjQQLJ-hUs_hz_nhUCHUUudw1m8C02mqGKPtkupZ021GFKTrw-HHZ_FNgosQc1GDz_0DZyfCk026m1z4a69z-IvU_Pu4wu3_F-4ciNs8as7F4TWem-L0S0qeJ38-kWtO0UOjdl9zHE7VMAs1fa8cgxPlSwY0thlESURRM3ayi1aSqV1uHr7RsG2mn77v7iwrwYJhTD4dIJiw1hEem8nFqLfgRzZuI8QqE8aOAtmw85dmFVhcrLAG-ytxxISUSFF8_AClRmpot_Llsfy9PRz5z76Dfo8N07whsiYbcdFZ4BY_pR0mr8-MU2-DhkWpM1r0-WMJCe67SCMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq9Jul8UzPKXKJyGDZBVf-cDBiB3J2-wBKH3J7m9xtjtZR_a5Uk5NMTwuFn7GEgd9eYI1MqX1l6jd1BafBiHsoPW-wdTRyZ5hHrbSPxw765sC-54lOXZ-hEkxx_CtBXK_F8dSMDu0gNjJw3UVW3cTs-Du_YCP4PMuJpwdseV2yyjahx4sTbHo3yJSGEtswK5H_CCZ_MtifpVzo4XyY9arqw19HCPCy1WSIXn7HUGPmM6ekVqTts-DkKIS-VU1q-8F_yru_ciVgo1vlwnK5X0JwcmT20qr4FYeSfmkc4ZdP2AUG-fZJ7CnT27bLLyFTlUOshuuiLp9XzBotYPN1N0Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhGufsLJsVf_iVtA18umDi3gXSoaQr_9yiEmlWqy_tPMTnBBZNMIhYP2FcALahu-l2dcm9fjAtPRpPbNPM4DC7OdX05XFiYEoPCmetIWRdS5tkrqRPikKaIPAD1I8Uv2fDXRu9lKlIM9s2WnHv2nO0MwBITqPGq3GhfFBXK36-y1BAfbUI1sm3BsLusQgeC3Xl0Q5ALzyOiDBwjE3mc-KpPt_bd8KnAEXoAAcBSJEaBDSFB_nn5odC_7XzYbHhSvPZxhO5XitRCjYbABjNoZgBRfIGnTaD_XRQEDyAeJ9BuRbhEgQ_hNC4f1ApOj-H2cdCzGFqCuwDZHGU6bINj0VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1D-UhFT23_ZpxD2r8pADmhO--rZ6P6Czqbtrp0cIIL1Nspb-K9QGbzZmUEhAOFrucsxApTrJpSBQyUTAUQtv88oOJofVlFuFvg8-1ZJtAMYjjtCR37PiNrURmePVWPkE6VDd7p-MaKZxnXxrPqbBYde5A-3PnwfI-_Q2RxEpAXPhiSOZSGZb_BfTgqCSN0REUxhYeFqKKQIdvP1ANdRilZibTrWru-X8XdOOwXY0OreHX_EzWtM2j1CVfaCY4IJmEbK8e6STS4LwXL2zmV9rcImTBrHMXw0GGgkpJ-_Zm4MjgFjo-qAzEQ14SMt3VCsc15Ng-ISPUyp0ukoOLRaHw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=X2CGi4wcChopzLlojKC1SZKIwLzeJjNdp6ZZDeLGdlswtanrjLHuiH_4JHG850GIQtLEJWeoevHaGeI1wAh9XYGZuwOc61pAC9dUgi5VR9mS5t6aF6WjmCeSxclHAfQzfQ6CJ52vbf2PsfQJ-UmXo895AmWMut-aBufCNoFN3kquxCTbm3LePssMaeT60RIP6V0YsXEPnY-GAScTTW3QTCJQmeHt9yILgY86mkB1c3fHFSdGf2d3zXFDEZfM8Z7D2CA14cgVwHmARWCPGRqdgp615d_CD49-yTFQKckjtYzkMtNr-274ORVAVfUuRYi4hiTO4vL4441RPXPMvpKdNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=X2CGi4wcChopzLlojKC1SZKIwLzeJjNdp6ZZDeLGdlswtanrjLHuiH_4JHG850GIQtLEJWeoevHaGeI1wAh9XYGZuwOc61pAC9dUgi5VR9mS5t6aF6WjmCeSxclHAfQzfQ6CJ52vbf2PsfQJ-UmXo895AmWMut-aBufCNoFN3kquxCTbm3LePssMaeT60RIP6V0YsXEPnY-GAScTTW3QTCJQmeHt9yILgY86mkB1c3fHFSdGf2d3zXFDEZfM8Z7D2CA14cgVwHmARWCPGRqdgp615d_CD49-yTFQKckjtYzkMtNr-274ORVAVfUuRYi4hiTO4vL4441RPXPMvpKdNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCiQt-Hr_hyvtx4sOH5G1xlwp9rMmdWHkOf1ww93Z0TgbUrvoL0F7xMoc2_Z3sDwWj1hF4Ro7B-ihXczaAzhNxEEjWP9nsbVj9L3GWGn3o_NnThqiKlMudQu_LmpWYuYLdUgkiunzvnNlJOjC7RCK-zAXi2-gu9alMgC9bVZVo7_1JyiDic-vMAYUnWGxJnfb7zq1cAeDdUeibRBnbQltSAZ21R_B4tuu2kSK0mMVA48mDDdupITRqAcp1hVXhPjYuo3mSrgc2knlMVdysHV7P0WwYkQ9EfR_UdAc745_o_XGpfemcKRZq9l1rK95EXeUE98Wg0ZFhh0474oGBeJdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsuBt8JLRUmHyBA-m5StdUeQClaR1KJEOBaQSu7wekp9XtbgRxECqZiMvKdskB9xzNf--_cjjvOdiBdCPj53X0qMJIBPpjBsu1OpfW-i8_2-F8f4ig5zBP6C1YxWKKOK8ugRJApX899s1Ie0nwwSqm1a8Ra4AeIIRRtUJ61FfS-mhqtv8oQD2qs7pOmjj-dr7ZvH6i3-uTxhLRBjZklMbjJrxgQ5mCp4xcc9P-lrX0nO_xFg8QqsqBwtjlGOy9a56I-YSGow1pQbmVVXoFyZLhA2FLFDAg5tNNWW4L5GuO05qVEU-xOTRgtCmCVyY6sb6-6IiZdmP2KBL8qIaTAw0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUG53hqgZl7W3ddN-GNeH1wGJShVJvCuHXpTE0xmz6PxBHBD-fCB7r_BlY3UwXyXtZWOznkAi-xnZuQumiHF3cwq8Seuwz3JC0dFP17wAZX-pcE3la4dLy28_06ndcBJshhJ0D-KhzwOazV54HgByMWIgig8p1IusDOZ8V42IAvRfe6wyko2evpcB98X3maHHvK1hDWVVZjyR2KjKqwtdbPbdSXc2RvipLx0fnK6UpKc8gXWNkTJ6idNhN-Lu2ytboTvtn1V91rYuL1XiJRlu41GC3I03o3Riwme3ush0F4OlMho6hWRWo7spD3HW0PDMEgYsgMONuyc-EcMOvx6bQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqbZZEM1GhkvcC0o0UyJjPseQkk9sPk5CYCvhVBlsGKlz8NWpCSqNWWF0k1i4LMSj5n2ZYm6dHHScvg-OuuOqEWbmkpItU_2_4Z_oVOuHIqgDfWT4vUgFTd6HQB4yLu-uiB4cYeD3rHV10jVqG_py2smsWpPm0SZFCTqEgE9Mo3cK25sdZvFFI8HtxRhcs0QX9rVCRx7qvPl00HW3xzjv92on8te3-JyYIuQXVnOgxN7JBX39LlPDuqgnRBJOo4WNZku_7MxV2iywc-LAubGgV7-RRJWth_dreuGhkxjSMX44rmrsa19hshlPursNrm37W7Rl8pWzW5ae6eknGvsJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NELTfZd5xJw-_7Zjh7kBKoC_agMFvZw8iEtAu_D8v6RDpWO09I7cPgsl-I06xl5cyrIQKNkzl8sY2UKVjmEHsMNmv8DeO2TcZvlTTHYlY4Dd2SMRhIOEmiO7ygTzI269CKRnZ17w1sWCe7WM-OHvU7djujmU0yDegbVNstQ2cZOJsxbqWe3jlcphhumCbtye0nO7EcA7HiNOdjtcMxgbrKfXVMFF-ajLt0MRIaf--ce0bWVAvFBCc0630s43Lm86ZVLqXtmi-y8U-iX9iM2JkKX6EY_1aTa2ygpMqcPbukfUXx3KTiCu2ARZQNW-x5OrshDapIWgdPHJY5m4jnm6CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8Rx9E3p8epnbh7UBYZkeKAIzYfY12kK04B0kQPjUuEHQBl54GcsVOBvBwIH8Ty38SCFxzzI0fD3SBwlW_sdD6BY0PZ6ETHoTyXr-5XhJzj0-RC1VK47g0wHUfHd1YjAg8xUBlbrDIPVedDpPa-FXomZDTtDAka5itB3e17T8SdoMSWvJTIS0kG_Qzwl2lD0qxV7Sk9_8QalMzhORw4ZZzG3gkShaemI0_MUZlzIot5bgeut0eQTuUIK95a1AaW1dHnoyeS--agxxgpZcUsU1JG1v9fe_MyFJ2oLTlw9x6xaYPzqPOSN20jrygnZVUUf03SQaT0QwQxXdO0E9wUNhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mI-WnLx5qqy5b9AS1UeVDu5wTC5SaLmSiO5zcCk-HV29Crg-ZrCDE0Ir_mzWw3R63Jz17BgL8gbNtXJJDrOFAOHgWjzsUs60J2F1SRNaFOew9fEdqZFagOgIOLqlcTTR10sUlvv0c1_vyVnDn2aXi3kNCgrlAWyvO6VnwxMkabsEMHs-RYNGI6WBokLUai4SvJ6vdIcRmjbt0CqWvQub6R7i3QaAcSTBBNa41oLTSWIBtrz2WmLYJ7wui-FfBTTdSeMGsnT1AnP5obJqmlETtOh-LZ-bnjKy0T5fMxO7HDnafpyOdDAhFmUDqJXGlrOxsuDS2KX24U4Ta7dUpFTqhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
طبق شنیده های رسانه پرشیانا؛ ایجنت‌ خارجی‌های باشگاه‌استقلال به علی تاجرنیا قول داده که تمامی هماهنگی های لازم رو با این بازیکنان انجام داده و درصورت‌وقوع جنگ‌این‌بازیکنان باآبی‌ها فسخ نمیکنند. ایجنت آنتونیوآدان،ماشاریپوف، آشورماتف، یاسر آسانی، داکنز نازون…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/22046" target="_blank">📅 12:06 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22045">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=BAxdXL8OWa8IjuWSyYNj-jCY2nYNgvA228HdvWpEerpLiCLhw1QKbHKfCKMJta_SIxpmyIUmNtidH7fW0HB07OM2-IwSYrggWuoMjHmQA569DObgBooKbO7CcjZz7L1zXL7mM3pnllPvzVF3-vuXII_API9-wE_nr0udhTrQXo-i0hi3blaZJT9zQc0GTnYt7JW2jfh8QAgBm3ffckOx-j6ztwMVpe20iUL0WL9RWWP0dhEqAFCH_RQzJ0ccy7FkB98X1o7VwpiLVwooehBDDe3ETm0b_MIF3fAhBAyg41Luhr8YSRaPY8khm2EYuTO6wBcSIg7wUBOEC8TsbnNAHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=BAxdXL8OWa8IjuWSyYNj-jCY2nYNgvA228HdvWpEerpLiCLhw1QKbHKfCKMJta_SIxpmyIUmNtidH7fW0HB07OM2-IwSYrggWuoMjHmQA569DObgBooKbO7CcjZz7L1zXL7mM3pnllPvzVF3-vuXII_API9-wE_nr0udhTrQXo-i0hi3blaZJT9zQc0GTnYt7JW2jfh8QAgBm3ffckOx-j6ztwMVpe20iUL0WL9RWWP0dhEqAFCH_RQzJ0ccy7FkB98X1o7VwpiLVwooehBDDe3ETm0b_MIF3fAhBAyg41Luhr8YSRaPY8khm2EYuTO6wBcSIg7wUBOEC8TsbnNAHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=kcEU4nRU-vfUkIM8Zij-jjig0NxBco78oKQ_8RFoYSvzgzFMuBw_wfl9uNqjAUPsT8pz1QL2D8gnNvXL9YNNwr2tiIeEShbLMPf9OHZGc5SpeA1qISgVRGAiSk-5rUI3Xk-wDjjvSTIGycSgaDKbLlGankAwaXeeS7QJBTLXKaWj4C_MP64Y6vdLziSGyZh5UTj4PuDUSjuesgU9SLEHgAkYuSP91pJkWU-5FoA69p1MShkCj7dNrm4vfbkRgAN_r3econcwu_OphqoPSBEO19_ugAJzaDRm54h1JfjY-7Qg863tfNhTWWGEaYJHf_SxY8c7zAm1m1w-d0nqZDoqBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=kcEU4nRU-vfUkIM8Zij-jjig0NxBco78oKQ_8RFoYSvzgzFMuBw_wfl9uNqjAUPsT8pz1QL2D8gnNvXL9YNNwr2tiIeEShbLMPf9OHZGc5SpeA1qISgVRGAiSk-5rUI3Xk-wDjjvSTIGycSgaDKbLlGankAwaXeeS7QJBTLXKaWj4C_MP64Y6vdLziSGyZh5UTj4PuDUSjuesgU9SLEHgAkYuSP91pJkWU-5FoA69p1MShkCj7dNrm4vfbkRgAN_r3econcwu_OphqoPSBEO19_ugAJzaDRm54h1JfjY-7Qg863tfNhTWWGEaYJHf_SxY8c7zAm1m1w-d0nqZDoqBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAnNdyA3zGOa6XalwYex17gDl-saFmWNdCSKtgOj15vRG8RSmPH9oIZxinovZ0JxT_BfSyqpxn-iK9ifm5aAUgBsSTS2bPeGrVFpCJAt9jRPD61ju7P7W0TliSbXsR-wzHtqBJLa52gWETvuSsT-ZTydrQ3-h2lpDfywYALAinfFb7Es8P8i4fO4Z--5eV3kQVQzqjEFtMnrtn7m-ByJWvESoEcTlED4OZanQkbCndGLLBgb7-kKamDzT94_EYr6s4qDzTzcqjs7thJOs8x1uzCngoUNov_ipiG9cFK5DHLUU5xL9_nv9vVUl6BI7ZJ6EtauMc6nE4mkPvv5FjMYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/22043" target="_blank">📅 21:22 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4-wbfq3wgGQ6dXg9W_cyq6VM-G4PNE0Aqhdgpk_mu7vyKT96iUgjvkoXNH4T5aO3bBeSUGKrQDLlkfXWKt_FyyfsfYDNJYaopRmmj4RvnfCNabMHIQ-IsOfAURrUrPHiX0y5bk1aH4fJO5OdMuhEmcz145G8fSPo9K4fU9FQE2pyMXwioqbxqqPFZRC-s3w03MjxXRRzRGLXe3hU77zKFt9Axfk749_fLynO-jY0BIyrGgwFzpjQxo1_33-vlUxtOrZj33TFby_H4D9xJAE1ooadmXTDap7ig7BV5Kc56rwGMRkS0gUd3lxPRZp66f_-SEa0-wLI2PIVHha3rFlrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/22041" target="_blank">📅 21:17 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvi5SNrk8QMxFzYgfL1_DXsTkr8DMmM4wu8Z39coP036FyCJ_JnS8vfbh9duCp6DaWs1nK4ZMci5GilbDI39XfzZqLZ3uPhn7eMC9a5NbVv2Z2xyHtVDXzM_ub_iZhmCvRB1xk45zQdVqWiNKBwVVXWcCujqfY1ng32qxf8j8_VGf36lpete4jWx3NDg7uIC96vXRDYGm7IpwtbzkQZ4-UMbBTzDo2ElU0j0Xl78V8aQjyRaFBtKoZmG48X-LXVMOS1QvaLJxkko7SGn1PoD0k6cemhepoHZFdsoZGmDYU5Zh6S0aV94RiKCXtVABDPhG3N7Q_bAet2ZsO7geiC2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلیس‌کانادا از ورود مهدی‌تاج‌وهمراهانش به خاک این کشور جلوگیری کرد و آنها کانادا را ترک کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/22040" target="_blank">📅 21:14 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22037">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtaiGqtiGgyVcwVALYbcp8mfKrstY1UqgvXQJAJFWSnymDQ6bnwYJ0OKXEwVg4A9V2VYkdzEPn8BFaVIf_JMnH6i6oapRxcb5os16grh9iXxxkAb5FyuaOeIzHQPI9hhqNp_R8JS2yJpWyUsK6mKRwlWHV6vCMiUzBqFkjbT29l4Q77ooCFZs1_wn66TCAKpYi14odmQuQte06nk82qMQUVPoH4X5z3zoGhjDTQzfDCx2JQcUucwbMCaBpbOM7RtXozF40eO3fAEmyASv6h-DaWSzUalOjSua42PjtjcWLwdJzljvHBbL2JNtTfxIMFLvMGtZEWk9VfwotUFm3FPNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تاج رئیس فدراسیون‌فوتبال:
اگه لیگ برتر برگزار نشود استقلال رو بعنوان‌قهرمان لیگ برتر در این فصل به کنفدراسیون فوتبال آسیا معرفی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22037" target="_blank">📅 11:35 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22036">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvDtRdYT2kohQ85TZwVTylbz4llFPaqSP_ag_dWFarmv6kKEf2a8PRIKyMOJuXn1d_GqjWmGuTY0y9nT_5Wqtb88G_lpzDLjGEuQ_2v3pAFlzq10MOL8iFze8-6j-p3DQtbYYpr7EynMaZy721rQL3RJrfZyCzpqwogKKDa2qW_kOp43xQ1OvhfwD8OYP9o1LUGlYCj4qzSLzQS2O7rfJxlI4whfM-PGHbogsvGbK3QqGyK3k8y7YndAeJyZp1cXZhZwnsy2C4EYlMTrpESo9-zGoJpnWSAP6efyH0ph4ziJpT38BVMN9QStvP8tO7mjIDMc3q_9wtBsptEFUQzrGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجمین‌حضورکارلوس درآوردگاه بزرگ!
کی‌روش با غنا در جام جهانی؛ کارلوس‌کی‌روش بعنوان سرمربی جدید تیم ملی غنا انتخاب شد تا برای پنجمین بار متوالی حضور در جام جهانی را تجربه کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/22036" target="_blank">📅 11:27 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22035">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWUi69QXnWlKEZ1QtbhUtJLzB9QEjVPuASdNm4IsbosZsEwPYFUW5Amwmq2QIBGHRjrrqfPNYRANVy1ZijQ_xcM7V097vvJgq6TOSZpe6Cii44oHdDKrcpVocqTFOMBu05E7U_8mJ80kCDPaPkxUcT_vPOfo_heQ8m1ilhEAc3YztKzvO84YiD5blmYS5P66jK1hDG8gnauVxTn3VwMWDo9HtAE-aEaAOxy_IVBByOnGdN-ew8Im03rk5n5P1f7Ryh8lVlWwxuiiRRO0k3j6jzm0UGMfZ0j_HS7s3Uy2EvjiDpYHRw6bqYbVLwv0zDVFix42q2i6Zrq2lUHyjrx2CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌انتخاب‌مارکت؛ 10 مهاجم‌گران‌قیمت دنیای فوتبال
حضور 5 بازیکن فرانسوی در لیست 10 نفره نشان از خوشبختی دیدیه دشان در جام‌جهانی پیش‌رو دارد!‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/22035" target="_blank">📅 11:11 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22034">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=e2UCaYpGJIjG78Q2LZjwefz4z_yuos4iFEBQaL4GPBGPJRUJthxjt-IBzcRzZ5EJrb03Hmft-f_KAZKUFua2dIYDdP2590EJMvjB192uEtOeNujv_xS3idRpHHjK9ojMoZpduysFvmmcJKQGPwmMNNyWGZa3LNALg6DSoRXAFF4Bry6vgxaUr7TuqwUi_j2G5sxNUl7zTb_3-ZydDuTMeV86NBhSocnP5f0ldI_NBFIQ-fmhP6u8_biJIfsJyOLUfzVh8LcVn3x9NSiLEcWyJG_CvlGvcOMNNJTi5RHImPzQ1zZ3A6qXeOG3XfOboo-24JsAHWT_0mP_kDrfobGnbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=e2UCaYpGJIjG78Q2LZjwefz4z_yuos4iFEBQaL4GPBGPJRUJthxjt-IBzcRzZ5EJrb03Hmft-f_KAZKUFua2dIYDdP2590EJMvjB192uEtOeNujv_xS3idRpHHjK9ojMoZpduysFvmmcJKQGPwmMNNyWGZa3LNALg6DSoRXAFF4Bry6vgxaUr7TuqwUi_j2G5sxNUl7zTb_3-ZydDuTMeV86NBhSocnP5f0ldI_NBFIQ-fmhP6u8_biJIfsJyOLUfzVh8LcVn3x9NSiLEcWyJG_CvlGvcOMNNJTi5RHImPzQ1zZ3A6qXeOG3XfOboo-24JsAHWT_0mP_kDrfobGnbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سوپرگل تماشایی در بازی دیشب لیگ‌مراکش که احتمالا برنده پوشکاش ۲۰۲۶ میشه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/22034" target="_blank">📅 09:07 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1-6C8cELWQkkSpjvz-8sghI6WnMpeh7Iwh8G9xsmPC9VajK78_KtoORmUwj7aG-j-oP5nCDGaMQpLE5vX_9CiUeMc-EvvdNIExlI-QlHxD5A7lQox4icdMLSEqh0dj5C8RK25l2zNnj58wm0Shde_vrX2u5F93BiSDuo0mkfFmcrHR8tqceHQLkbVIkoywjrz39newV1LTd-1vTUJcSERfhqzKSAE_aEMKNMXbB2RZdTNvVQXSvO5-J6_ZTLWxkpylHF58q2OibSFcS92Q2WuDt9NvGkZB-u3IrKhSm3xjH4P7S-n43T_2J9kzpxMBA1xeK6Kq9nara6Y45g9G4kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/22025" target="_blank">📅 00:31 · 19 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22024">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dd2TbntJ2q8eSmEKUJ0MjEtvrdR8Pn0aRFSZfbreF02m2SBgMpq7qluVW8ilXWrl9B6i__K5TQJI6X3uNreQx9QPsvtng6AZSmPbh2ZnONTpli_4CIEyd_Aof31fKtqgLZIDZax2NS0Orm5JMKMRBRJ4sRY2qA0U2YL7K5UdJ2z5V4SS0ZemTDX6FMluKaqNWdPPMCaIbb9dmfR1bGzJtk_ozA9ijauwgbAgZSjQAjmz07-AfGZnhawe_8zFDDLokBYBHzu-9NgqBocgD2cBy70I7CKOev2-NbafxOBwuMCSk99kb-cGc3oXM-otSpHLuIf8kwgWIDIVhA7XqAzO6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چهار تیم‌ نهایی قاره‌ اروپا که امشب هم موفق به راه‌یابی به مسابقات جام‌جهانی شدند. ایتالیا هم برای سومین‌دوره متوالی از صعود بازموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/22024" target="_blank">📅 01:10 · 12 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB_zaB_Q6YlekIZi9JMxrLo-cBh-yPObMJWU7wZiMVEBTcPJXAIdYwzOha58XfFrODfX7U3dAY8QsjzO6S7XsyHgp1J6032jHA5wRSY58TefAHZXVwhwj4Cv_muojlw4rY1TkBvYcT_BaULxIZlWC_blyB8s3D7mqH18CNsiYP0_Q-oTu4TmN-8x3r-0t9x9TkWHEUi8kAeLcp-jzn3pDJXUupL7AUgZS_YKPbUjggKQ8UKnSYw3X1V7MMfWYJb2batHQi3jVH3sfqq2bQiEGK2W2gxDalZlotj-pWBdATuUmF3Gbjc_SL002zKoDOcDyVHric6IjFUqRSb5RQPiNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏مثلث رجزخوان‌؛ یکی‌را ترامپ‌زد، یکی را نتانیاهو و آخری راشریکی‌زدند.‌عاقبت رجزخوانی بی‌پشتوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/22014" target="_blank">📅 10:29 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnVLpSRMnrUspOMyCp3Oql04ptDITI4dZ_sA12Q3LLSLyZLz7AgeUZKow6tuaBHqkCOx5eyEjKmZfQb_jOOr66-VvQHWPCN47ISKPlfr7iiQ0Y5Y6atXSF4AMqqxuqg7RGwEi93y2BJNhOF43iwuRT9dgA6cEduvOR7i12ke6VmdZKqdVH9J5tPx7dzgN49kkrhiLpFTMdEKdOqNYu8Dma2MH5vD6tk4iAhB7Kqv80YvFUrN8vqrJaWJnuZCEwg8dQf3WX8-7TcIxZjT3CK-PZMkrVHE-MuhBUJj39XQGp3wbt5Yi-t2uk4-HE-kx4hJuE6Vgs-vCnN_MefUY7kZeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22013" target="_blank">📅 01:26 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22012">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgqwGUmy3aucwsqbf2Kd1xFjLYFUXvZOk07QCYacTAY6lZS-DOUuEZo6yRaNFSGYW9tW5J5XNRGEC53p53tt1b2OuhbaI7-FIZVe0H9CHYVwpG3wwXRK7Z_u0j8NR6Y9sU4CpaksaaOB2RGA_LBiAgGn2spin0nCQYs3w01LZ09PIua_zDL-x0Xi2hAdY2SRF97HW1AicEFM_ll4xC6YN9Rl9mEivfrZ2Lv55V29qg_AbrhkG70KkIP8S9f-iqhlZOb7LY0mYyA5uszW14QZzhjUcqd2MMn3yPd-FdN13baWNTozkbhvnmHeYKCH5aCPCBr0u8hiiU2vbAhEPcZuQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید مارک لوین فرد نزدیک به ترامپ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/22012" target="_blank">📅 11:23 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7P-4FGn6GY74a4AkZii8qltbRA6WkvRL4qHxj8uU8kyUS33RnEeoP1MkwUugNsgUGpRhPENeMQfiGGKEkSHhJcLDKJ9utYVOMB5VH8o9cW6W9QakMsYfdICfDHaGQCOYvieOx2jUDGPXd4J62ncCnHMxO5fDxeLcuqUAliXsheups1mmiigeIh4OIOACpNxmqe2h5zgs--ZQgRLu9tifPquT807L7G2M6VF9mua1ecFonVo654DNPgMjblfNU7-dPCbb1FvniGOcY2TWvgD61q0fVFBBAwbVfE5R98_Q1xdQlxmDQO1UifGeP2pPlruSCQpgL7z8B6UcH8WJSjhPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گابریل ژسوس مهاجم برزیلی آرسنال کل این زمانو صبرکرده‌بود که انتقام‌شو از موسکوئرا بگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22011" target="_blank">📅 10:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22010">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQRB3CB2YI_I5Qwx60VcNRR2WVWby9BNgNERsoL_UgiocfbvwI2M_zZf1g_gDFc3OrkuOlRP1bnXAyLJFLtImFHoILwede4sUgUsFWRS_WPnkpcylTm9WAQ61cRaojy_cQzwXzowZI0JspPq582UEzwv57ytkjW1qrFbvDsTUH7k1O4IfyBN1mitdw8J896orw4z7lpeVIT1Wl1MpoXODMJiN4WE5QaCBkgdgV_OT8JYUzkFhGITfMwlC41pnyl88oNe4vDO8CZ4k1g_CP8aQUyQZ5qEGwgFxkmRrfN3yEo8KL6MGrSaFkTGMdk9HBTNRbRxzJVsu4He-51IHJSXnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22010" target="_blank">📅 10:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22009">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P35Fu5MK0i3BT4CkvkscnXgsgzBAc4FNlObL85rSZGPRnhgVSzqIqPkj5oEr3ewbP-7jXue6xu8ImlQ_PK5J3GaFevi4qB0_n0Ghxns91uygxTV6-bz5X2921VsX3Lj8EvAsVQkvdezgg9lHFeBcwWFI48BzZIo3ETSVtnha0hQMIeAFPUk--AMShwIgdMR9SWutnKsfeGqJiRgcTCWpRaPh0TOgMP-bcqSuLfjqy24Fp3nnQ6TvId_qqlaXyjVCReQ_--kTfeLjYCBbK0So0Iy7ldWYYDWXGeSv062tiFZyAGmGSPq7ZZjNoLR02mvKLkpT69intuuUAMIO0117jA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3BDl8S9yVd9Cu9schcoNx1u-q6VUjYs0nOlu3JDWSAQMEhH1mthzdILtCXysGAG3p_PyD8CzoZKG2UvkfjyyaOLL-Egy1GwSzP4Gq2xpH1zD3E2VDDhU8NBU_SqEJEQ-n0Z81VF3t-38hm3UV8GGoTTNSJFGtk2_ARXICFhjqowTtm-5festZa4S1NjjjTfK-GtnBsxzla_T7kaJfc1yRNDuaHZcqheIPp_glWwbnZrIDzqRGe59F7NMxZbp2j_1IKCD0tSbU6oNMUb6EYj0-vAhXDe0m1juksMNKt_fHrD8j54V-lc3T9dw1MZZSwJRaHvAZTmxkqapdxLSOqLrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22008" target="_blank">📅 09:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22007">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxcfl4KZOb3o-CWp9YBvRvs-6jJrC9ch5Hiqi3sd-CA9ho53NCoCdpMqW14wSeMWEBfTLtDRz4oEqXRrUQ6PSOBZBgX4p-W5-y_819Liu0e3F0iRQr_vzJs-epIfceRYmfERs6aN8NRoioxaFG9Jr6Z8AmH_36IhOn0hKWMCJH-XLeEYwwIwFq10i8xpfwYuwJqWgdaDiDgwD5DpE_kneLSXgihw6NbX4M_mEjYxKaa5_uYNzlDLFrjjc3kZimzoJfskAX5jx228frEgIVNgCCjowImA7_F20UNS45MP0TdXGoVwcdKDjh70bbYeZPAKGTrBU-OmnBTrUJ2G92k-yg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=lk5eM1dueUYjk5LNNXv9ZTxGPydaxPovqUqB1DxMAYPw3AuiY3wxjJ-KMoN7j-G-b_JD_MeRdCw4UReOm5ppLByBYN7zQcKgSocMKcYg1NLxD8M0fJOfoEYB-X_HTLmBCpZTtok-N-sxCAln_EfQiTT6MAHLgk_m2egjL1q4wgFShaQeOKcEm9Rzs1z0UjqFu--8HAeBDBJX5xID_zl36soBwnyIAa5gMCU2gYcNfGynSAi4H-50aI5UmKsSSWhq62brXJm542r2v_-mkaEsVsiBGP8vJzKvwgUdi34KqdawvdhQG-EbNZiGLlBLarwzveMkDPpU_nOKvwCRoQSiGGlmsfKinY_9xgadjmKPQUa5WyJmkgduqXzqKIl1DaGJIadJRBue_7FV1RzueAj0iE_vmQJyT4VT2M_kqb0tOSD4t3_aa0d1NdXN8gkIfXwm5P0fGiKG4XV3D_QDTT9AGCE03mJE0UxCz6laZH5K5QQZLvGJil_NizafEu2OdDv8RKUvDLP5rjq9ZIaVc1x582eimiFVaiIAVN7X0dRKmvhukNP82C2ZJVU9uznOvbK63NN0OHxK5GO-5jICZhNhQqznPNFAfZDRhT6B5mJ7WTfWnpNCNxfiJfjUwZ127adUMnqonPMXv-gvgFEgwwbd_PkHLNKafM05JgtsM1a4lK4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=lk5eM1dueUYjk5LNNXv9ZTxGPydaxPovqUqB1DxMAYPw3AuiY3wxjJ-KMoN7j-G-b_JD_MeRdCw4UReOm5ppLByBYN7zQcKgSocMKcYg1NLxD8M0fJOfoEYB-X_HTLmBCpZTtok-N-sxCAln_EfQiTT6MAHLgk_m2egjL1q4wgFShaQeOKcEm9Rzs1z0UjqFu--8HAeBDBJX5xID_zl36soBwnyIAa5gMCU2gYcNfGynSAi4H-50aI5UmKsSSWhq62brXJm542r2v_-mkaEsVsiBGP8vJzKvwgUdi34KqdawvdhQG-EbNZiGLlBLarwzveMkDPpU_nOKvwCRoQSiGGlmsfKinY_9xgadjmKPQUa5WyJmkgduqXzqKIl1DaGJIadJRBue_7FV1RzueAj0iE_vmQJyT4VT2M_kqb0tOSD4t3_aa0d1NdXN8gkIfXwm5P0fGiKG4XV3D_QDTT9AGCE03mJE0UxCz6laZH5K5QQZLvGJil_NizafEu2OdDv8RKUvDLP5rjq9ZIaVc1x582eimiFVaiIAVN7X0dRKmvhukNP82C2ZJVU9uznOvbK63NN0OHxK5GO-5jICZhNhQqznPNFAfZDRhT6B5mJ7WTfWnpNCNxfiJfjUwZ127adUMnqonPMXv-gvgFEgwwbd_PkHLNKafM05JgtsM1a4lK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVAebB-eGvasBfthISkUjC8ZgaCPDqTJKtJ_2ZE2QSWEW_qT5P1pY3mJaFBX2C6f3JWGnqQT1v3jgtr7TMXIj6udOlCbtIzhLw-8C_8Rno1QibLrdoG6VR3QO3eG6bj0qjsWf9ivpIjUmwgI5NKlGiUs6F0pomyck8nQ4NhKwJ5pUt2wcipb029BZiEmRXRzP_MhHSKA14hxJI5G2TL02WModaijXmbcCCs-D03oLaIAbZ7om-kXqOSN7Mjd7NeJdLbWK4IJSS_KJbw0h5hklctj4iIPjdHDgW_FFTeT7HuCOqdbE1jVc_wL93FM4mEGKX9hQIOWYblqonah_2787A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛
از بازی خانگی بلوگرانا مقابل ویارئال تا دربی درکلاسیکر آلمان و دوئل شاگردان اوسمار ویرا برابر ذوب‌آهن در اصفهان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22005" target="_blank">📅 08:04 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22004">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWin1-Mgttvqaq5rF-zSYUnjcYknYHifPvO436tQV-yj0qtNQJYem2HNu_4XJQueXhZBKteuCaTA-wWkcdjXdQjRuaYm-KCXG3sYJBlp2MHS7KVuYIq0SGG8f6A8tuLuYW4fL5mhB3_71I6XxgHpliXRcbC4GvPphcoTnHVSyq_yoILAS5WOLBBN22uYqPnw6jFz8DwtyKpXdkcwezgOeWTl5i193r7HAmsLpGBp90oDekaEcko9UOICGSTq03tDdALrEuA3dvGcLMOILmxwKxZrFni6rHbazxGLTZfJrWFc6MABscVZGVuDXFXyRJhD2X1hJx1BP3FOQ4ThxmuY1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌‌‌‌ دیدار های‌‌‌‌‌‌‌‌‌‌‌‌ دیروز؛
صدرنشینی آبی‌ها با برتری مقابل فجر سپاسی در شب درخشش روزبه
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/22004" target="_blank">📅 07:59 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22003">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AphId8IcYfHlQM_wf6ipiQxg_COq2uF9YjsbVnZHr3LHqKHbFcsaeTGR2kWLO_NxaQNsu7Xe2o2XWEC93qsvTo5UQajDOcGAb2wI2e-By0L2hGgNo49-Ds-NpIo4zaRRkyN4FSh5bAlpN1uoa9gAzJam6Cd0iiqSpAMzJGOjOxtXFNuEAZIpD0O8gRGpEoJUsaP0MZyWEd1_IBKmXPAGWpS3SedGA_NJzy7z7GQpsLjhzVVheqhK-cwgdHwcgPprTDfBgHpxOIAy3UYsJ1d-bDajDlXrYqV6H8lD6jt_MlHzqcB_6XXmuT1xQvNBmpWY51ccAbNg9Uywxsk2lQmUvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین فرد نزدیک به ترامپ: علی لاریجانی، علی شمخانی و پسران شان دریک‌ماه‌اخیر نیم میلیارد دلار 500میلیون‌یورو ازایران‌خارج‌کردند و به‌روسیه و سنگاپور بردند. آنها از ارز، پول و طلا استفاده کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/22003" target="_blank">📅 00:21 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22002">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWK4CplnYyYKEI8mx4W7Xpr8SGXtuQrxePrZSsuyp1U1R7Z_Thq4d8Dts9XClT1eNbUktXd-QTdYngWas-bq4ll6WFiOcTf2HiphvHel-rfo8W-JK_R1WCoAWzZLzl99Jv9-lg_wNtDQsm_I30FMfJnxgJJrmT-9mgWHiU7Zk9mrxWt48DBIsxbvaDoMtFSocHD-Zz0xlHZmq9Xz6UFOOswpygL-U1E8eQ5zcMSylMBHYozPB7jLtRYfthVcyPaVHI4ownHc6b0o1Tq_497PJFj4IgZ5vE9bn-m56BxrKR_xZ_mYiDpmOKlpDXXq8kmni-5Rj0cT7cYdaqrI6P6kAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8-sXCWzL9CyKgPI9H5pbmZtf5RNbKwkso18Chr6eXcRT3k-8zw24T5Qp1lKWp5k1tLDag8bNB1DeLVuBpj7sTOQCsbbfFiznjvBFg91gfoHm-EDXry7el0_d6XZFTt6cCHvGeaEt8RiFaupn9pAQzFp1rPr8M0aWe-hNxfxevAme3UoatuwFXjffJCLtnv9YH8t4WuULlKPfVTcz6CmhTZygvsCjIh3Ra5TnY22PmB15YbsQY8kulFHa-TfHN9wF8eo3Drc5ij-HEK9FQjvqvs3t0gXryHFZhQ5AhS8rdA5qET3-QU5jjbhME1X0bODyb48Lw9lYA3VKjUqlPpAzg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=r6JT4a_ItrGab--cj7ZHYFmleWCUSvArKXHOucvKlqL74eNsAyz2epWicd6aXuHPbPNCkGzo7kcnc180QR-i8WkQtY7p6215_WQVnQS3x-u9lpX7WTEtEkAVB4slutLIks8bdNp0JGVHJJcFfYQjleLlrMU6xA45DDdbGIB-6L_PQt7afQ0vOQDfx20ub4JgNPnwWR0T2RxUE-yibKVAt5ylS8uJUdnJLwAZD_vKBSrYGWMYv4sI4kMR6EzWEhZHy8sQc7j-CLrqjKJgFQ_StgoCQonaul30_uT7of2hgSXV60B7vvy-WI2Bz12HIS_EdeomIbGVfp6AuB8u8giCSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=r6JT4a_ItrGab--cj7ZHYFmleWCUSvArKXHOucvKlqL74eNsAyz2epWicd6aXuHPbPNCkGzo7kcnc180QR-i8WkQtY7p6215_WQVnQS3x-u9lpX7WTEtEkAVB4slutLIks8bdNp0JGVHJJcFfYQjleLlrMU6xA45DDdbGIB-6L_PQt7afQ0vOQDfx20ub4JgNPnwWR0T2RxUE-yibKVAt5ylS8uJUdnJLwAZD_vKBSrYGWMYv4sI4kMR6EzWEhZHy8sQc7j-CLrqjKJgFQ_StgoCQonaul30_uT7of2hgSXV60B7vvy-WI2Bz12HIS_EdeomIbGVfp6AuB8u8giCSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لیونل‌مسی بازیکن‌سابق و اسطوره تیم بارسلونا یه‌تایمی کاشته‌هاش حکم پنالتی رو داشتن و تیم‌ها به هر شکلی که شده میخواستن جلوشو بگیرن اما!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/22000" target="_blank">📅 23:38 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21999">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJYoaBlhmchV9KgOMkeh_Aeueutbimcacl8fV3GxC52V9IstkUTeAuwusw8BJpmyzHfzjyJcoOA7h_cI6JWR5pwXnsgR_5y8VhqUy3tFT9uV9Bd3YeVu-aScssKgIdJhsSOIS6LxywPDZkQECQDR7LjQS3nuhf2-6OfZcPQZImPAYW6drrjXeQ0FcCQmh_-p01SEvz6wzVsImHVWkKMiUvHomJaCy_eH6b1OOJvDrwC99UNAFhffrqsBokwXtTMYCJJqvhKd3UOc9LzJotYYwYY570FU0FQlU37dOWor3ZLkA_1_tgZi64z9yBptawtg014hsL6lJrG0ct5WhyaqAg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=dRfqdeederjA0WtTUFra8e7tNV3d35LLaEn_lCjfs5AzuwDI4vyYSYBjBsvCPepg6iR9obEpBTvGc514ID2DzXvkaFCDVYPHXMwfGsrE3Q9hCVG_uz-DxtJJfVpYfgcrqrsvjBJABM_FbQZUgyDzW1vSuZHMadkJq0g0EBwxrtH5klcHk1na8YYnAHkhkbz4QnhuHNTcEZj11Nmx4RNeTZzD-SwNaqgX9EmtkdNVUbz8BNt592hZCiugB7pE_g8Zk6mHLU0z-JK2AD_3Gw6-HW-IG3HTW0Cj4uffT1uffi0Vo7ItgfZxQXJNSeMzpzbpq-TadmFUXjQHIqXmfqSRsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=dRfqdeederjA0WtTUFra8e7tNV3d35LLaEn_lCjfs5AzuwDI4vyYSYBjBsvCPepg6iR9obEpBTvGc514ID2DzXvkaFCDVYPHXMwfGsrE3Q9hCVG_uz-DxtJJfVpYfgcrqrsvjBJABM_FbQZUgyDzW1vSuZHMadkJq0g0EBwxrtH5klcHk1na8YYnAHkhkbz4QnhuHNTcEZj11Nmx4RNeTZzD-SwNaqgX9EmtkdNVUbz8BNt592hZCiugB7pE_g8Zk6mHLU0z-JK2AD_3Gw6-HW-IG3HTW0Cj4uffT1uffi0Vo7ItgfZxQXJNSeMzpzbpq-TadmFUXjQHIqXmfqSRsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
مهدی شریفی مهاجم چارچوب شناس این فصل فجر سپاسی؛ استاد گلزنی به تیم‌های بزرگ ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/21998" target="_blank">📅 22:45 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21997">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194acea631.mp4?token=Gf4l40dUtiufXwsgVu_jil267rhH9CWkWUpkYPdEca_WNKlgHBgfcqcduvZc7ZjnOmv_OXJ5m3qMdCML7JgJ4eHRrNolzRMmyKOi2Fzcofs_9HfU7IS8yPdTpd3jL4AZOQuF2nVgN6e_xtiSIuS1LIapgKFCOGHa0srFrAl5X1r4chNckfk8ruzzC2iNa6wx3_xr_kDCifSDT0Ycy9r0hsEHo4vjRP_eawXtL-u-zwManIG5vijTjcx6jr8Yh00bYgqDxtZvpr59POWEvPTE-LkjrfXwa_TViX2LzUrpcFe3M9bPLt-raQZtpL9dkh7nEKWq9qnia6IWkahJ6kE7Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194acea631.mp4?token=Gf4l40dUtiufXwsgVu_jil267rhH9CWkWUpkYPdEca_WNKlgHBgfcqcduvZc7ZjnOmv_OXJ5m3qMdCML7JgJ4eHRrNolzRMmyKOi2Fzcofs_9HfU7IS8yPdTpd3jL4AZOQuF2nVgN6e_xtiSIuS1LIapgKFCOGHa0srFrAl5X1r4chNckfk8ruzzC2iNa6wx3_xr_kDCifSDT0Ycy9r0hsEHo4vjRP_eawXtL-u-zwManIG5vijTjcx6jr8Yh00bYgqDxtZvpr59POWEvPTE-LkjrfXwa_TViX2LzUrpcFe3M9bPLt-raQZtpL9dkh7nEKWq9qnia6IWkahJ6kE7Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش رضارشیدپور به فحشای‌ناموسی عجیب و غریب گه در صداوسیما جمهوری اسلامی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/21997" target="_blank">📅 22:35 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21996">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVOQBXL_36Bpkn6UoZloURwpe-jYESsJhEj4qOJNCE7EOUQPZhS621F6QA4RXgBRRkGtBvZI_K2ZhsbVm5ECHiQi-Nf5IyCaUdtI9EYVXTgcp7DwWWGoq2ec8d--aH_kQWHPz9HLnNkh3LIVmz2EWn80VobhXwUwAJgfqvaU6N8N9RI23A1y-6gDctj0iUdZpmlvyYwb7YsiJXioV49a1fwju7MOTIbVApotsQYK6LFipPiI8fIq0oStvpJW7pSexnBEUqhrFMed-AuikWg_X3BAsKeYt4e27lQFSmhqJHJR6Jk4kKpcod9uBm3jPvefsyEg9GwyEkmjktSzTTDPeg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3bebf41053.mp4?token=PB5KraH3r_QMznFQmWGvZ3mSLnbBoin52pgMiLZLHocyrV1Lv2vCwZCV4E8-tO0_IAszfC2fMV4V7vam7ydG6f3fdq-Uk1_lW7doq0QUbjSUMQ713uqX79D2-DSTyQgTvpiwR9BKpEjKjSCzdyGFsFlCtigQMt1s2rvwGQw5OWCVFc4xtVQM90LB6ukAQZQsQlUy1TX4jwtLPg9_lnVLqvkcj1LHsbYNhBv3uUnetmrExXYP2xqNSP2qK5A7zs8WykeMITtsvjlFAfspct0feMe8YWE9gLc15e4AVnbwRG5AYNVoOjX1Y8bovVhbeR2eM5v1KqdhpvRAK92c0Xj95XNWz5TZapCMeMWuXsZyEhlymAYAm47fE5Y9Qc7IJatQR7hX1mO8F9HPv3oRwZKnCMOCpCoEuqs404x4PFaiygA_m2IYjBkkPIfSluMv-7rbs9KhEUQF7JvDu4UYNJ4m-us1AyRfB6my_ax1ndNE9c8PnZ59wDhAICYNcX6e73QQifkF52F9ndoGXHTo20dELioQzCzy793IF5hnwmVjRtBu19E90Ex9WEqzthd7c3_LQIlhG1TiXFUmXmpOpqeuh2NqLvKT4u-buQXPAfCIJNMl2zIkzO3cchpifA8zjXUfX70EXg37mjWw2VyQOZsvcRTHB24t8RJvztGV_eHBslA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bebf41053.mp4?token=PB5KraH3r_QMznFQmWGvZ3mSLnbBoin52pgMiLZLHocyrV1Lv2vCwZCV4E8-tO0_IAszfC2fMV4V7vam7ydG6f3fdq-Uk1_lW7doq0QUbjSUMQ713uqX79D2-DSTyQgTvpiwR9BKpEjKjSCzdyGFsFlCtigQMt1s2rvwGQw5OWCVFc4xtVQM90LB6ukAQZQsQlUy1TX4jwtLPg9_lnVLqvkcj1LHsbYNhBv3uUnetmrExXYP2xqNSP2qK5A7zs8WykeMITtsvjlFAfspct0feMe8YWE9gLc15e4AVnbwRG5AYNVoOjX1Y8bovVhbeR2eM5v1KqdhpvRAK92c0Xj95XNWz5TZapCMeMWuXsZyEhlymAYAm47fE5Y9Qc7IJatQR7hX1mO8F9HPv3oRwZKnCMOCpCoEuqs404x4PFaiygA_m2IYjBkkPIfSluMv-7rbs9KhEUQF7JvDu4UYNJ4m-us1AyRfB6my_ax1ndNE9c8PnZ59wDhAICYNcX6e73QQifkF52F9ndoGXHTo20dELioQzCzy793IF5hnwmVjRtBu19E90Ex9WEqzthd7c3_LQIlhG1TiXFUmXmpOpqeuh2NqLvKT4u-buQXPAfCIJNMl2zIkzO3cchpifA8zjXUfX70EXg37mjWw2VyQOZsvcRTHB24t8RJvztGV_eHBslA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
