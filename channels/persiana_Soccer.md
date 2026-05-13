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
<img src="https://cdn4.telesco.pe/file/PvrGVCWlBJJOzJi66SX_YqOGAGIG6wsfTWFWppR9XlUBDKIyJUUOI9bblA23GJvB9vPnFT3O6Q0kJ8zckvgAGzfjd1VkjIfaGJE_hJuOxuvv0Xv4pJpkoVUQBoAEazhG0khNGrrKMGB9mHzJWcfW4BP2aRkKfP2DRVoEh47G1dH-koqjwqG_Vs3FX_sCmKfa1kV5g1QnahWOX17K2SP5zLa5-KKEuwr9CgqTXA79wjpdXnO61E2oQ8WqNb4VZv2lphZYAB03QRu0o0oZHH6bUK4mPsLAdjb_NGAlCFxWMXnFo9wqxqm1bcqESm6eMulMz7d3YXSmE67rCxcYmeccQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 215K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 05:55:22</div>
<hr>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRHynLFx9ET21d-pFx9x5VAUdI1dNQ7BXT10fJmYPLDYUJM_i5C7rKLq0Bbk6NaU4RwF389WTUqBQLI92CHMNESpeXbGIN8YBeKLaTy_jT3Qn7gE5Ex276LD2GQvJhDqU-yDrTh1xvpRGsL5r0zYzc30aS7zr-SqwtuPbDjd9dTozA1skvnOJy4qaPtCN8IzZy2N1pM1b63gZusB1iQXvX5j-19GKURhIQ63rEjNjudUFQM9KWJmGu_GTj3wPmcZVhPDxuT0oA-JbMsuZTn5Oi94p9ocf1rwqflwetq_PPCGw_lrHI5gTaSWtZ0jpnUqmm3oWkWKNmTQ8NsbT4VIiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSTQjJQd3hPXHw-lWMtIAIkfCqcMMqFi8cxi4qD9ovk5ggS2n2uOvoL84HoDfyS7ibQq6YyQsTGsSHJyDpVX4eqwYTFv2q-qK-9sf_fmsTPgulIV7nXQGGwieRsmaoyjixIrKE3tDlbQ40vOHiySPe7o8d6q3W_qrIrgCkqxsahWvF-TzpafERqqh1Us8pVwXn5icnOMqgfsz6IAj-wmZFogjN_aalBzKt0UHIPbeO2SjdWTxM8OCQ7zofvQSErZaONlmtAbLza4zDTI_jcdVbp_s7k4NQhvOsi0ZreKumhnMO15XEzrhKZFaZn7oi0wkKohwTlps_L21JW8hcphTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22120">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/persiana_Soccer/22120" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsE0fViaXWZiWNyT1J16v-mWdfWVyweNwBYkdSk4ZHKE5bH1ZmAurZ2nyat2sA38p8HjciPQy2k4uNsWHkHPLilNMrpGcO66QRsnYT5ieFlfFEIuj_gYCthPG-aKiyVKWb9ODugJmXgKKq9KukKPUrzQa5QKlu3PvrADBUV50q9jzRfhTiN3k40SrUp004BKsWStzKv1YGMmB-m8Y4qkrv1WEgsAba9TZsw6_rHWseJqW6qTEMygsevmv0fVkHEHuTYSEiznxPv9VXyYLuEEaZvoWKg-fJtJ_EHEYSFq6U4NomdjHDC_Ie0S_cAgX_7JxU6ETPFlodCrQr-jXbmW7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8fUBx8FynyQjs_wrZAHz2UmKG2Teq0sQw-oihDXvaNypk5tUACTZb7maAH2CzuUQpmHHUleyDXGu0N-NoeM3_g6jdr4L5hVDkbLDbD95iuR7DMstjwcwCt-qnnZuMaVZlFC-lsvQFBCb8e2yTN-qPBecidk4qWWEbGEP6ClgZjZx-RDiIVbnDqDxLlarDFhHGLztVFCKiYWke9TZVfPv72ox7XxuPHFwDM1wiltjVJLtFGYfyxfUlqiUqIS2HE4myLS2yvM2InQw2lsgoS-y01CA_1E4UtbPF96hOyuSwUbOIB3oCAZaEqk_DD1fZ8CbogD1eUXvm4UYjDhU3jamQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTPqEV5sx3SOaE38WSxobvwitbbB7RT2FSIY7YHEMKV64egQ0dU8D62Vy0t0FwPMFviAft7CZb6rYunzMIH4l0C0oH3gK7nFifSh-2kmicMz1mihxkY9HE0dfUGglCKMVBjGpvEIaZ_x5S2Lqe-8qPdc5Z0sFzq_nFPK4m9tAkZ92a5B6uetyDtBqU9LR-SwHFwKYPZuiDHsG_zNR9CohOWCjz9pc946fu0ETxpdjHuEbC_fnsUop7q41Mm4ZzwPabBHNVRPIoGF2svw8lzlpRxKbZake5VLGsyRbsCXXWpDNiewm1P9NHYWBPW-fRb0C5fL6pYF8Un6m9BAivl9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/uQsXMV0qRFlT3EPDMojYOkubsn_YlpqTHBFmwN34WM5Jh-ffcxDVsHF23XQZXpdjJqpu5xbAAAiWBcbrdgrTYUZWPE2YMQANGjROQmz-ZcLMOXagI5GegMwLz8_eRGChYyBLYY9TYixAazL5j1fuRbHeIHW_HWkkVlIbVDuFnooKFdA84sYTHlh31VfEjmu1lOLL5eaiMM26P9OOYmT-Uo0g8lPToLxYmuqjfnC0hM1G_OVv_2NHaQzrsp-ehQ36o0f8cx1N8DwQXeEfqWb1gasOlEvip3aT3En4MdFl_E-c8BboJkaCmGyC4JD9GtEYvWvF2LW7VYwrk5zl3lgxLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUg7deHtpops_hMEXg8XelEjMxFooCLYUj1zbSrBE1AzAGlLrHelwrhCnc768pjJD8-rqKCBBPIjFN8T4gfz84kcPwnaQX6XESt94tZGFLNjLzoxVkKs4_GSMHAVYCyLv2gGnSkkKPjrN4Eid-ProapQMVceKaoS5Wk5U0cUkZjcTiAntZfbTpBxlekrM12Ul48k9UAK7tO2o454s-aUStmzwATc91uidkWLJM_rARJ7ZrMqB8-73M_RjZb6mbM6pXy5Z5X2rRKe3tvdTfWJn_0zFsFwAyJglW_VwN4o-k_gSdRWHkVWWizahNEXrn9KKT2IMnRCYVU5hawM0VEZQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ET4wljfGxeN8Ysuon59b_A2lXXvgdJSL9RpeN7rJ5eRbY6Gqvj6LyYJDRCZkNzrh354W6T1bWSaMwCObMVx62IHV9yz2gNbmdlejle0aqTl7BjnOJW1N7cgbdOFYO-se6RW9_sWggLUufFf4GjVJHcmSgkLE8W-zcnzBzVMjlGuduNfMFK-Irztwmy6sLpp2A3dXZC1W7nm-BMwed6l6YsHjlLlf8RInLNk7yUtwKwwsxyXSh5eL99sNzs8nNG5dHx7rO3YgI7UgLAgCEqwO64jWTc_5w2rAr6H-sZBeO_kXAfY-8rnHsUS6ENDqb-3zLiy5Xuj-xZlPUlaQjxXQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8c-WhP5w49EiLZwCL-nRUXrcDnL3pcpgVO3sTJB4Uz_cevQfLL4OJ9iw1clhXFiM5ej3OiVrwjBdnW-wHuYrnFu68C7rx_xL17caj45noLLLEyc55NvKGFnbrn37eIDNrXD--RCrxPFQqOf7Xy1u9-Wf4TB4IDqEbjoqISFg5yP7JIFY57Hhu2hOfv0DXVd3udDwCYSEHS9BnH0AN2T_0MB866je-s7tA9xLRjysQJEGKOm5-QW603PVpS7cpPdlo4V4icVu08WJWvBsXce-2fmdT7g_tupScdzy6uocQWqRVQmHnsXP5Q9xleSR-yWd662VwCOqDxPgE-V3efbYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCZbAy48bHDkxzjDsxaLPlt74ZDUwlyjAWQF2Cwu9jHx8JaGpjgI7RyHxmi6fp2g1AtnnQ3nrpJGi6LXL9RJ6Ewiv7gGFFOsG2wyDJUXnT-jaBUUNRy80cznhO1Z_XO_gxJuthjbS3Zp0nRbZT4FcM61p3td4y45sczopc825CQvPmwvIUJzKUnUdqc_KAqe0n9SGBZjAiPbF9UNZev1FoBOYS70tORHrqK4FEuHWhjoV8CnBJzVTBvEol7vCojo4Yl8scKadSra9XJy_m7yL7B9oT1a8E1EzHnrbi3VRofW9eUyB7FqDs4cNoQkZNpWFXiOTQMfDraXwI0SauTmWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY3fcbPK46eGraC9ret7kxRLsHKVyQy4fzG_0UHoEqCeLGPod1KB_Y3hf_gkIRSzKi4zACrYDieKXtyRtheD1UronIoR7B4sH7KinLhNCbXb7e7Yl-L8yGvTI5RZpD15MbsRwNTnddr6kllk4UnpBznF9sJeB3bESsHqMVHQJmHhJldwu_mWSFZtcePiwr8y23in20zqEMocNrdmeUhWkwUPDvfJdAM0c_ghIem8p7f3043T4gWMsDCTxcE9AqN0eO8fn0o-Ky6OxAcEKUoMLkUVPDMluw8M2W2PzUMjCk_lI66mcSGOBUd5xXBLXxidJ1I90glD_ZNCHmDCSakPjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iC_FycVwSOqgOXIuNg5N-KPxYAohg9fepCzllkF6xDaoSZbzpk5lsDFBrj2W8IK0rVVPWFaFA3dFaaknRk4iAONgrZ-wQ8DvvqBqmt4AgOapF683caqrhaBZNx2udj3CJBJnht4nuZox6k-P6ukKyFSOEAiKzJTaU5-Cs4zHdTduA8MqeUO2ZI6u4yeLYRazJn00g6vFYs2x5AXY77rw_0HTaIOw-wSHqgTjhkDY1HtT3oTLDblpUTezXHa8JmrLMv8e3RjSQig_85Sigte0c0TGSNI5jzI31rPRO8CaVtMIaGyoPNcUBCGinxyx59p4K_N5FP_HZPxhfq4IVE5cPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RG44Kt6F7x6V9WjlMFltWZoSEl5tgocR7dIRz0kWiSFAEZ2Sp89m30_nd_mkMTwEtptYbKm7dtzFxs8cMs89C-qL71PAiOxhVJp4gQFfmVNrG75dievQDAYtmX8sP1ntITmIuxVePoUBdzOtIH08yx2TAcT123V1xiDk5zJVcliJVRWvJ31BNOwqw3N5m03DZXUSuY8-1apWBSNKllemHW46b209EBNnjb3-cMkj_ozSo9AV1hpVtdlqQb2GEIPOjhhuU3kY7pDrFb8w-90yHfcmmkGsGeq0g6uReaxAs8L6ug3M6a_0b0G4azM7mjm9RC1fvl8pzH6I6e60L-HC4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbZ_0G44t4uCM25-FhP1LY3Nh07R3g8gOJ4FQApa8CaGGBH398831Wvwo8TZcwRX6Oi67knbXJ7Tv-eGGqg1s4j9AbamUKDf4cJoiFGIP0D-SZcS1o2-oM050ncPncgO8BfxH0mMW91VtWUFmK8nFsb4W6t10Nau6JvSwRxBY4xiRWXXot4gm3bh8TJrWmQdR0j605bRWFxOYK0tvT9vlH5sD1ou3aTBdtsYYsELZUN8ZeleGZ7_P7o1WpsiJSOZYjU_SOcgqRhz0NOEMM_EPizX91VkVNoO-jBHvC_iu3J5-Ib8W6NTH8RfKbWxvNSoajwGm6uC5xbeBB63Pfc1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5MGETIMt4VOXgrzTq81qUP_waVRlZRN__TjjNSKuS43id816bbUgvbrhQN6lOGpYScEe1HKGtOJGKHX3dobgjmhHY_qiKop6ETGxE19WrZNAnJSzBgAjRy_iNnhEkHebP_ODKHnM1gW3F5_TUGsn0qlGiwbOzmgxCLpSd1XB8NiHiUTP3k6U98xPgYklj1Ugzn7SMsBhHimjPSftLWuUGwlxSr2UkpMLAIHckLKD2j9fcot9FVXb6pkC3RpdJ2VVHUa_rlxCPuYSvxtdJ6Ut3x3eDH_JAlX3W5ASRqwOZuFiWZXKHmO8NyQ0xdMk4ZYYKOEDrgZ_dWhRW2JC5AO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXOjEHDYWMMqNSOivFJEi4YM2ahCX_vVEO6rMg9D0qBAmFLZIWaMNYWXHKSDhfDUOXwhxTuz9sFwSNEW2v7q78_Dk0gDqXpVYl3YyyMiDqc1OFN-1fSsbZulDmtO1qTQ1u6bvuqwaTrCbP618oZtUt5gzOKaK1pmPprNrNi5eAZS3ocAVCmNY_nThLo2C7aDXNv6i5dko447h1lqqAyAmywFkJXF7gDCXfp29xDQEDh2IMUxNtR3CtDAj35ZgRHXNFg5iyJssAxshQpkRKGwNN3gZ_wUoeWAvXN0xNxfLFBxd5p0E56n8Gq3hY60LvRt7FHgKwgwGdF1cTpwWGFNDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOJYK5uRjGWElzOLhyV_RZNq8YYhe2q0EXzkccPEyoYsf9D9nlr8Vn8vYnDmVdbsmHAiCMJZa8x32_bu3kl4liHB7dSG8VZpre6-vDsRvhcSh1e-4PIRNyUrPvOr3jET51PuveTlFO2nf94BKxmFO7nZD8PXBA6hlkp6fU8cHXqoqcbkaTemvIMGOr3FPbI_ZsItvL7q87H3YzE-pYXTnNNHMV5vCQz1NPElRyYJbGl2OmX3eAG_1C98tpL5BkTYaXkZX6pvowYWekDXonm4SOn3bgIeNFxzAYvO9vf9Im5_szv9ZHOFPL6EHeQMw9OQoONbKs1E6m6uyrQ3JWvWQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkaFtF-a4cvtJ09C8qMy7shLZJVYHPGjhNOLKffln7pTfqHCnPCp11KQEwVJIEqS9zgFZpkCjWERv96GURHwxB4fqulzq2LMiTsZPZv3mFOD6CMnRBOgjKP6CRSadVxhZ4ZXDnqc0ENJE6f-gYIFfSg5Y-c4oDxr2xfRf2J5hZAKlp4DXwQbrCbRtQFHYfDo1HzXpt0ioLvLv8lIljA7mtZMA-5ADlDwYyG6jpbEfRTIKMBsQ-5nnwImhGK7Z4SHi5xvieaZMKQckE2ZkKNyjDDdmYayy9005skdPMBMAjhMtBdbXRoWSAQ87_4I7WOsmRy-pljEDyXs0k5UhTtILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgJdeK89ZqHkIgKajFqjnLE1XeIN0lyCJDMvAq0RSnxa3rAwulYhzFsZ5pS2YJI-sebADmn1Zh0CSOS3K34G_Uc_IzI-eOEx56jHycGxIPwmMAWhy5zuzM_wBCL3qVW0pX8bHjnVucmoGKaIiesopXtlkBbr-SbxBGltE1ivlmteIKlP2FXrUjWYo16yvNLoEEXLgRda19_9VBXdwZool8wdd2i2YZkt1xR3HDRLOBusaeLYwR0negxwvuYvVHkWOzASGGmqokBcmfseZfaWwfjslO5Lx4XfK95H0ufNy1NgA9Z9vBvSdS4e6EzJBX28cogCqktE2kIV1quD1rDXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLZl-qdFce9ho89qHZqbvusgOJwMuf1zjCmrh9NU4aG2c_8FrsF_WnRvCegSwwj6ffIhFLe_6F07c1Bsi__NIWiB9XRxV7AxCM4tqpcTFeZmM2n5CcLRWivTGJUWUpArYcx96FR5jiwzomTQc_boVI7bcXZQ-Fuu5gsB1y7z_ZrfnKt8VERzQdVblk6NbkKwwFQWVRK6wIdOxsCwKQKMlXsbGxIxgnfYtrv5VVlAWaq0OKhJUdX4cxCsvVW_feyb0TQIEyDh79iRK9tO7sC0bPk0cbMGtEGtaBRWIDS7rv9UgmQkUQvJQr0BtCqQ6xUpPleRT3u-a61DH8dk0ZHF4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkbTOHtIgbkJpoK_3mS6dgm-FyMKpqT72-NdJkSArBMYHs8_z_Jfv565rY7J4OL4pPUQwI3w3XPge3IVJNd9XYDtWw-vqE7LN5rs5mX2DubWF7LQMwWPisBwT7yYKWeXIyi-k7KA8rMZNxJ_Gn3xcdCDO4k8W_vifg65pGOBUiOg-KUQB6fkPfksuR5K5udmU44PETFk-E3LAHB3WP8jwXkZ4yBfgthzOMF_K9jmoML_mB_Rt2O1XWnczAkJIDKBh2y1RWHxVKzWlturcUsmvL7trUU9R6eZqQouRQRei5oiNXV9ZFY2WhLzTMAMjuUxSqQxKtLjFLSXhWZ1C2HG3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jz5evn3oGafMeKDWZGLbp0X684XcnRBtuXQgDN6QDmUjMNuuM33cSiYvYeZ-xuOFZF4s1_t8_kNN4-S-WKRmLtkrjYCiOWQrgWQLn2x-8MjUXgBT322oGuTIo0AbUJnqodoFZ9sBLRot22Q2eyByeGtnE-VuNt2X3WQOBrJhW0Q3GfFe-6NxfCG1ziAmK1pMEzxX95wZ0x6SatrSil5rHIem4DoTEVvRRvFs_Ad68Z55fdZq9Ws8CyQz9kH3w6-8gWZNnFe_be29sg5p0Ol79SDOV3913x5kf3d7OLfol1j19oP9833i66lmjBAgG6UpsbYV1vTOvAHUq0tWXvj3vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlybaoHG-bCNpLc0sz6FFEvl3lygdQRImnYxaf4B3cFL1pQOmkymlW6dQgxse3K9q0HwScBFK5Rkn3JqWDX__8vAvU8e2hpV15jbvRfepJOARUweBoel4q0CliHaAdRk9TZ5KcjM2wXHWtY_Rr4YpJyS8DTaPi5wuCNrZpJbQHc38tbxavLEH45uaTOpSsFwz5B5tS01v4hDeOxKMIefvaItBbgS3Upk3uwHhsUdfFOhfNNFBfy1AzmxFHujuC3BcA_wDZuMBR_ED577RW1GqXFs1gWkn7GEKrl3P_-qGzwNlxsXE2yYjInRUP8a7R0sBxPkS0G5Q5hToiJaX7cs3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMwHMku0yUJyVxyLSXopNoApi3ewq0iGu4q0CltadjhX3uH9JrbTNTtZPhZz6DqNUHfNq00qiZy42uwGF7TtLd6E3eYgeINsNCiA0nBzAIulo95erAg77l3Guj_vFNtCvKiuzMHjeJTGHlj3Qc4OoOCUDwNHNT6P1o3JCOC_cL6R7P9gxDghQpvuXp2BXtbpllnCRbYbuKg-4vxr0Z_aQvo2dCNG2sB1KWODHowEwPah_wRp7a70YVa48P3QgqObm3BecRy19EJInHB7J5DKxJKUQ9zR2n9kQ42sj6aEGXNahOzQgtOE1MUNhEpKH3ck79FXePq0TySrmuf9_zx_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJrq-xHACXua50ZnchR23rRRBTAJxeDRbHRR-MfcHBsysvQIn0FUZ658GSy9kopfCIq1Q-fF89KX9LmwkJ3u6Zu_R3gnelTSMct7pMJoZysUO02tP6kwl1SNAhsV2EjhgxQ8ld9c9eQToW7-k0s7rfe3xlCaRZQY2El41cmdEn2oW63shtIxIgjZP5mQZOtCNihaZCPcqs-g4Pl-n8W_9SxqIeEIw-KO-WwjzSY7l7jmQbT8hj60vdwFwqGphzTKuwYsLAxKOeI2rfwaWmLVS9_55RuYrZN0j4UWw_Qca-_Oukz5OUFk7UsMApBWZe-eBoRi9jV1oU72g-qNi17Xgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTDChgkhSXacAxkDpu5RoQz52PrCnhMy6pwq_P8TJgQmnX7Fm-Vrk7KqmK7IYsK9omijEU4wHIOeqKziNJUyqdMcsJHMfHEQJ7Wh4px_xiSM-JvU40AD7SGXOqtkaLZeMwRGwOHCLXJSOAxeSI0qqzuIuEYa-c1j8iKbMftipUmtNRRxH0wrxH_YxxhyXEuOSI0zP6FRgIlucxSav3bbVGsJrLtAWO20PlsUBciNLzdTUFHEoGyddY3IVXS6jPg62Lp_4EZsumuuGRb7Yv0UCrc8srtokncl8EAE8B8Vs3K2siRyOdnTpLsKl6_jFGJz3wHlSz7syM1XB0zCSZYhmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9LqWlcjp_u8RzNSBnOwQmdTRTQvTsRh0tC4pZwTSFpihDBpDksMMNCCiAZztnlZNUK13Fjm4lBAgfg1PL8TgPPL-7jntE5WNNkJxiqMA2d36YTqDlekL3EnFqQDcnSVsz32_65X6ga3wR7ztteYaS_EZC6QVj4hST24iJfYc-FJPv4uGxLm6SLNhjScHDDPDWJm8we2YWJoWMANBwItNnX_qXhpR_Z7E4UiHebDOe0G3__7oDZh_iPqreKLHZ1V_H3D-pWlCdsUq06eP-UUcWFqJYOW2IqshWUWojq0lGkUtBYrCMugQZts9KMId4p5gGEiQ5JLbJQT9rj5sOZEdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtFxy4-ul-oG4cxI0CpHXud44AdsCCpSp_Gfxd0cx8ry7sEOH-J5rZNKiuLCRNQA4slZ70rKDeCLpxgQjeBowJJyE9I7MJW6RrMJ7FqWtLDQJW4z68ex1x71XjZMxHXW4svcfGpDmxRjlJtdJgG1Td4ICRen0SJzQLmrujuuV1O3Mh0Icanc17Hw87GcetDHuYAYOoZofYAVq_CFZ2pzxBPAf1A5X8z3RhNLjaWmvcbdx3M95T0BoL8-5iNJMGMrSSVYocq8QfXFQd1lxjbH-g7aRKI0n-XU-rI_Gc7yICp4xCVWDx8C_w0CXff4YYTq11cUMeYVzMLNmtq3XwWAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJKHL4zDL19iFaXu3z0y61wfXXrYdA8orD0DZZPW1EdU5wecqnN2etoErpqVdE64aQx8dTSd_p71Zz7SGrsJoljWTbZnOmRveN9ZRbCCe0wriNNWGMzsbObuCvsD0nST1ETlDMV9oO-df0dBNrH-dMLRg_yOaGxZkulwnNOc5okAPLdQyKZ5q7nPQavnkVwmrzxD7BdMeUvXlif1Zz8Ir88ICy3cMViPwPJKEsxe4n_vszA8H5vVRUELcAkXk4GZg7cqpYDIcqbXspmZyfBs3BMMWnkKJR9DNmIbMfTovSsCNGOV_6dJk4Id7m1g7UOJ6M2tx7NYDiyDV5N6RMzcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fb5NUQAKLRysDhmZt0BNszzCf4yI0GndR1ClCWtM7eebNBCjV3GNPPc6Z2dxwaFa0TsT71jlT_YcdFCEVm5XpNHK-Z8kaOnoXeVpLiSHk2fNxbdoKTWTl-e7HIP-BcXIDEhFTonUql2h1gFrcDt1Uk4ELuxXDLN-cuzB14VrM3XvpO6Imh4V359rcR9vOJbRn_P_MIIOnsY7A1VkDYvr6VjsT5W0oM8_m3IvnhXU03CC0zPOXpDR7jpiyTFj6PUcwlY_Yypm0C5oYd7ezIQYi62l68ebKnc4aMCn-LEu3CV3-IkCXsZw46ADlFVPVKP5lioNCQ8NGsMwsVVMX07Hiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-k5O9_soLbQbI2oVNYiB7VQDOx2IbJiUQCf_U0d9dKKf6D5DjVjOaj6uUaguTVaBBYzv0Oyscer8l-AEyrkQPZV8tBdFOMOpOT8OZBNaW24uB9v-WwH9jqdRPJdBb_u1Mz4OdJkojNFOim2lmGWTbR-tcq-c8-5lac0k1_u2cZGPRVECV4WF9ZvpR_xoQHPHXe8RELpFlsccElgKWwVLBqAuwgN2-MDz2BJ5jbawm3Q2ZCVhOV5jMnyqmsn4XwB71kdIhciBFwljVIjsI-8JiBJBt96z3lfJs7OAc0GEoK_USBx0zAUqXZHm_cm0zqEyPnKqi9FBQenCHRBABiFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrU9gqF_LdpK9PVLAc8gIYGmHiMNmXtRH3rwT5zimJ-UOgeZXrbBvl5Ymmvhs4u7Rk-uFxe3uZyN6c3viMr9Xr28ESzHm93nHYBAyrTsJxyDskCY0O2dQtxnAhTcpQAJLOvu_hGbS8bEeafmtTW2g6-ffnlwA0pwcnNL55CG4Gq-MvFbhpFsTz7iEG-hzH71puezQHujbEOcs5JWx8CKGtKecyU6ffhKEKHuz0jmyhDwmSEhCMgwCwM_1GV6Ua1xnfCgfQ6C3NjeFwQUfs2jjieF_b8A1v8CQ3SzsqM2hKEkKi83vV61TdZ4WTV_4AM7E82ZcdjChqj2bisJYg8KDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLFtWAxESLfISDlFpDz_TpYOT-DaVbDCwai3CS7-1BipNlHXg8pDMYlUkjRmzHaTVYeNbRlt7oju-R4f3urVFjLdb_olYMSEupfNREmpRHa2etUOIW2tAdPmzRQMokbodXd-wyvFBTortIM729NDFbdGWwnkFEeycpCo74JydzJvV-qiclJuQwH026W1UJyTaPN0jjrVyLRIroQBxLZ6CKoXYS2MNKuiJN2P3RB7ejslwz_dlTcGi03bdSe0locRkjLm27HqRRNrB-YnpdiX0YdEGn2vL6KRm1JOSZePqcIGDT3fwwQPhU8-N6Jc5l0Wv8Pv0nfRaUdGf2YJnEsShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1-vMU7k_gI4IQPnieaB4UKO8VOrtXt-XhpS6JLlwCJEADMpW0DaHzHciUj9iQI1Fb-sii8y-VEw5JeE9w6YqDn77kIIO1qxDLyApeu-JaUJixQQrhOpZ7ex_IWROIwoORADtI_XRB6LeksGDORBQQAXd6bGTovZnoMOgr6LeVovVur39tYgkxinnkLy4jI5eKo4lnjljv0fPVe9KeCD2BTh5vcit8J8Ffc88F5pb5NWTnHf8Pe-dgMTSOVul-h0AeOiSU8cvFNGkxnRvHge8wPT6rSsTsBklCJ-iwhtwoj2L1TJnH7b1grbAAdOLqKd62QHcuyQE2sd8xPqq5WJug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jD2UD732_lKMwE5r8RviS5c_XtMMetR6qYsmOXwxfvFHPbrRz43md9xOq_uM43LEerIVkIaBTs7fZJBaS_mmLX5UOd7Djwm0rkjFjnO0rnDP3YJ_l9ylPsNJQ-BksmT-5H1vys3OSQdgKTLTcKqc-9TEJBaSbGZKNV4vDwl_G1nJfLSZraOedaqFhG8HEaXKBLCtr4i2M6eeh2RDsME_qm5fukzrZH6nWPp00eOiNfhJBQ8B9B4I1_7Fj2XocfsLYDEEKA8JyZ8I3phbhsdA62eUaLKEt77y_npVOxA9o2nyA4ZldiOtNxAARfCaxJxgk-Hl3HUb4ah9E79U00_gfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0lp8Z43PmDmdR8f08K8dcrVl0tQnJLRUIkXGUVrWd7Ssw1lO7pfNWUaA7H17bbsI3i52JtfimoaAleUsisngVDGe3q-IPRyeYJzTgwI3LmLAWRvLBNLCIakfeGMKdpdBM5Cgx9M8jlUPX4pkXRh6ol8FOGqnMwieTYvcCAfGNS0PPJvkFcXfzqV12wofl7qMBRJ7yXOI77QXyqebPmbxFGoSiI69zvH-k1689OkXS78xeQe27btmuehRY11pc1s2wQhIPWu4Y0Rs_UE3jv6h1ABstcZvW3sFkGBo0R8CDtN85oZwwvUbqXfig14jTwVVDRG7R5EvqqAJaAqmMWKJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5zvIDnlTRWjQQLJ-hUs_hz_nhUCHUUudw1m8C02mqGKPtkupZ021GFKTrw-HHZ_FNgosQc1GDz_0DZyfCk026m1z4a69z-IvU_Pu4wu3_F-4ciNs8as7F4TWem-L0S0qeJ38-kWtO0UOjdl9zHE7VMAs1fa8cgxPlSwY0thlESURRM3ayi1aSqV1uHr7RsG2mn77v7iwrwYJhTD4dIJiw1hEem8nFqLfgRzZuI8QqE8aOAtmw85dmFVhcrLAG-ytxxISUSFF8_AClRmpot_Llsfy9PRz5z76Dfo8N07whsiYbcdFZ4BY_pR0mr8-MU2-DhkWpM1r0-WMJCe67SCMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq9Jul8UzPKXKJyGDZBVf-cDBiB3J2-wBKH3J7m9xtjtZR_a5Uk5NMTwuFn7GEgd9eYI1MqX1l6jd1BafBiHsoPW-wdTRyZ5hHrbSPxw765sC-54lOXZ-hEkxx_CtBXK_F8dSMDu0gNjJw3UVW3cTs-Du_YCP4PMuJpwdseV2yyjahx4sTbHo3yJSGEtswK5H_CCZ_MtifpVzo4XyY9arqw19HCPCy1WSIXn7HUGPmM6ekVqTts-DkKIS-VU1q-8F_yru_ciVgo1vlwnK5X0JwcmT20qr4FYeSfmkc4ZdP2AUG-fZJ7CnT27bLLyFTlUOshuuiLp9XzBotYPN1N0Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1-0BJENAnuio-cE9lcu3yabwTdnYachmehfufQb-zqS817wkCek3Xz39Qlju2Fw7GVFqhS70YUsqw-t_LknycQm3ybci8S0NHGc8A6sN3UsRYe5wzlT0XN--ZVTXqDPDo1qun4fj9P4je62Gjurjk7luO-ujRLxDuHo_PtEqVTXc6MeJ5nsSSfePCukW-X_526LwQUOsTOzd00zWdFCnJZd3QG_6DNKoub0CuZGBpEcrdkXYajQI5bmx0457ubzcaZQGvpyJekTGclaFFRuhlOaVUelPbNjy6LbWqyxc6i9Tb03r8nhl4GBwD4VG-dGAynvMEIdO9R2U-x6-9sJyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5Ura_4d_GOUQwiVvxsGteId3l8WyoYeYVO4E4FkzDSdy0RKo1EnjumpzhGYBgFWdMdP7EKEDmWc98N7v22X5USyMi0XSz8qCZPNEoWvonEPi2d8wM3fYSmA_H5ikaOeHlxZcQJbwcBma9T59psXXh6v8aauQYth6ho_D4PoXVh3SQptYcctENcdWvW0EWMaLnYzs2TjJ_7OATTGyP89VcKn1MFDKTwOtfemv06fQ8ZLDHDHOuo6dJltVjcD_FTPl0yK9IVYlt3k2VCukfX3f8JF0uaLZunGlXmKwYLnOk2atBV3WpB41REjbi9u21w40d3KSgod6JLryb6PsKOpOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyT3RGklawVqJGHVx_JSwPzIXH0cncmxvM8ZMzxOzfgEP-Qnmxj3h3clNcX3C-IHEPmsy0_9agXbl45KSamCoRpL4O_j2qGQMwg4CXdKt5vWFO9N8cm3q25vY6NLRPKeuptXIFv9Rojqt2btG9YWWwADEmH1BBSm7NFD23aTniP-es8fX0-YTYSwq7wlfOBirBLfn_xbTQDf5anM0ZW8w-_QXLBIf3haY1YSQ5bNHsQO-wenKwFeCasmr7oOg26Dpj7Cu61N0N0r2eCI4AHyaSlF1G9WUADiUWzgVuI2NWQJrR9GQYSEz6_-XawIYYhbia9YywwmSYWIHCvoHX-fTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=VHlOrIA_hqG9tD6-a-Tjr8mCJg4b1LXU_CJCkkSf9LdAJKTpDU2NYsfO5GnbM9Q_vaFJjJtrhKEjV2qXBLufwZRXMco2HISn3YAigvVB6wyZHqtPbJCmaIxO5hKHBwRSfUuL9VkAo_eRQBjgiqBNRm53KmXDVa3N-V1Y2Od_0dgcNV8bkCGHKFfOofM1sSKEVL6yURCEWFO-LkaO1Vu3CRYB1Gjboaf1uUFNCgKHV8l13szPfDObPobGDPydLqzz0Jz0O-nW-0NUMkGAvX6hcv5xf3RiNA8_KDBWKyklN5ggMjWtY3ArleLEGPR3Uw8M5vAw9_BCU_xXd6_z3f6QyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=VHlOrIA_hqG9tD6-a-Tjr8mCJg4b1LXU_CJCkkSf9LdAJKTpDU2NYsfO5GnbM9Q_vaFJjJtrhKEjV2qXBLufwZRXMco2HISn3YAigvVB6wyZHqtPbJCmaIxO5hKHBwRSfUuL9VkAo_eRQBjgiqBNRm53KmXDVa3N-V1Y2Od_0dgcNV8bkCGHKFfOofM1sSKEVL6yURCEWFO-LkaO1Vu3CRYB1Gjboaf1uUFNCgKHV8l13szPfDObPobGDPydLqzz0Jz0O-nW-0NUMkGAvX6hcv5xf3RiNA8_KDBWKyklN5ggMjWtY3ArleLEGPR3Uw8M5vAw9_BCU_xXd6_z3f6QyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMGhdVvSdX6gUodYcK0csTrQa_sM5C3qK2iiAbUhonWd6XdeQ3diez_2LmCN6Dcj_6YME-5lLx7QWFOlX6mzbKFh7CznhJtBM-3vKrGRkohJrYjnyvI0GyvX1AnmBPZpoQDiccVTr_Wba600KMQVD0rLZ36oBB37Vd0Qu0LzFG9PzaWKo4PJMXQck-J35V6lUDsUWpV3wRA1nhnohJP64Sn1gUqadgTf2FlphHucrPFkS8XwCP2fiCnQ3OBsEJap5Ygur2C8egf5MvgJpHEyfsjeS6z5qlUzd3lhXe78qMniwX84aso_AuSxJ1jEUkmRn_JtnmjvjzxXnBQEaMFx_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW5lbZIErGgblUfNTptz3uqvD40NExL_CrDhEcINYJ4iXwNzRv8tQ66-WzcKiFBZT4RDieU7avXPwp7iVVpY3zwAujmwGqkqguT-KCJbeZjgvL33F6W4fJgW71HAbPEnFNWi6GhdaEO8EOPblB-2gB98MHVCpllRr2V-T0oBaoUCF5UfpgGndYzH1psVpcnnrhoG95YDfwPt9EfVm-LJOP22ZkdOJ7JD1SI7tF9YssmxJla-rO9Iej6c3q8tFcgmU4btDE9o5phXgIuULgCqp-J1cMJdxJiAhi6sUggskDSYNfbK2Q3k5IrESY_1ciNwfBX13ABial0w5XQ-CAEo4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkWvHtzy_RzkC6NtNMYV9-EUVjHh4vGS9U6oQFfALKC23nT9J7m65qayfnmkfRxvLeYuFumMdC_nMZ7vE0GgNGlmBlmdICVvaF2h6q60539qPUGRt_6yldKnmXw4xti2gWtBkrG02qVCDQ-T7yJYbIm0YWFH3G4tLlWZjPgLU_JQ9VEdAAtJI7seL_rKws8pqTkIUPad9-al0XIdNod8MCTMoFu_g3vbuydLjbI1phzrefFzpytM1liwIPHGBIWE9oNKrdmzkfgGt1qdmZqL7DcbdfZWjUKApw90zaZVKRS-Pq-TelHUVyAGiJf3mD0goSgLpC-vr2_USr9NHxSgiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWZgLuv6eaw0HFy3t7ZtZpujKdrrGsNwmlk6WAjZj7TTEJa981CzwW7nkMDljCNZuMph2qWcS3U7GwtTXhZfvhYf-AoPrnQLT753s0OlOu-z2tIUyTc5WU5rkjC0Hm0GCJZyZE13aM7a9kLnxwoYMgJuXIMZLgZ-fdo1qEByb0wT7Y7_ACEIr9qgPhkyrIUAnKGxxkAN7j5nKEKwO8_rjTV3cPHmutVO94kRRN-a0r-FzpZJfQhltIse0B0NqUZgcUJc6kMqzm4jyCOyLUif1pVTK06mmhaMwGonX6wViIcfCMFm7eOV2meInUQCWykLOdfUdQF-qKyc4hw12R4Zxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0thXY-fvsnr2xUb37Dqks7zb1BR6_jlbTXtJYGc7APH76owOKLr6w8p1rlu0WP7fhf_GVaSNbtFYt_Z9DctkZV0zHuhhUapoxsCIXF7_zu2RcJKrvVf13DXiQVYcwWaMeVIJVBOMVoiIZtkw2zcnbmkvjTLGSpezh9hh3krwFQ8YwrjEOya3QXqAjkmE8Ulwz_wUevF9YKSPm3KKFmcFJjfYJYNgUJtjBTnRATf725Y74t3Ma3saCi-BU4iWbPRAUxTYOc-Bh0lZggPygrlV59r3-2NEJ0e5NWjGE3QA4x-AYZvRtsbtg1tZqNLgp4zbqydvWkyHifd2gwZk7slKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJmgjmlHt_zu_qshV0n_N2CELyi7GSrZJgLqTN9UaC1eoe26UJeq2ja57UjKw4l2bxKJU_32T3NB65se8hRqLBIhwicPa5ZvxavGBnaA_rCSxjWTTT6HHeJnwvyP3ItJjnswIOr7014-GODwWT2AQyx3A7uyuJsJvKVoHrX4vY2WTjVPrf2465lFWPD4vkkZGs8XEN5Eka1OfE1C7x8KuHHkcsY-pFfKRLgywFQG-Lbf4j3P2J_KD0YTvvvI_WaAD0O07rnGRUGjNpYNBjoz74oU65nxLs9hIMZhtPRim23qDLScCH8tHprcLc__NkQkG_7dpVc9unlLwq4UzbczAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yhdp1fCUN7Fw9PVE91jhpb4bMOcBWBSzO8KDHyttogODjmkc_1cP6ihl9iOkjuVkbtdGvtSCfVS00BmSz19akV8fb0dZBZ3q4rj9xqe9GYnp1W3s4C0pXIfPSKE9Z5XuaEFy9frfY0T6jHEGHCYfi2fCDGwf1NoFNLTMh2_GiBBzbG7E_WSShOzOiseeR7IfBkOxeiHqQifNhHFTWV7aj9escn-cUSvb9RV6N_8s3SKmdJB2CmccwzguqYEM3vRl7Sv2sCIb43_LjKcJSl_1BdMUsFmX1IZiPjep8tFxw2NXGXFfez5zennPyjTinplR2-W7AM4E2iaYSmNO98ttdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4HnfWR0t4thdLR_OPTuZ6mkTnZTLcl2LFQR7iTR7RL8dj1BnDqVkdnN3v3V5whZ09w9cjuRW-Zc1DQXn8mV2qXF9AFUtnG8BN0svWuDAY9wTJanhsqO4sLGMiOiHcBIzHGeyUMHGKMKqqEpLMX4TNdmx1yAFp0Rn9MZevLxmr-glBvREhvJEfitnNCvMe2-9a8OLeetvEp7UAMpbm2MLWpUYeNY8O_mxaWiFpr1iKQrzLf9TwkCAltW2QJRGlTBIBX7NtqHwJfyw_90HIjGgDkIveueLah6l_xMLUhw0CXLQKaBnDPEYeWrl6EWrSvcF8n82yT8Y_6YT1p5wgOgBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2JjKxYYy2uAA9V1Zrfv0eeKbNaYhSQpAtj3WxsAHX9kVmB3mRyp6x8BlafYnNdRs5fcp0XrqDO35XVK9Ssr3KidJhP_sw-BKFAVtMziFljC3-Uo0qrl24ed95_uSPb-F2lmxuE2Vs4JLjFiMlNNrfM-ESUg1kDg24Tno-GLC6z2XSvlWgA_k1aW_I2QXSzYTY39jOSIMIHRM5NR-9-GLDzoRf10TnMKzfk3KLZmfHnYTmWXv7kc2CpL40rdV3rfvAfEZf7PRTA5cTMiqZ8xGb__OqQdc8zJV2nCMbErvW5Fq8NigXnfJYcQJSjrMA2DdWyDJzyZwhucj86mVX3WSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VAFIcLdRdtI3LzeoQYP3h4hBGNCjUlfduuBxWWi0EfBS1cP7mXJq4YoZN9-EfG0xGeUiKHJCgtsGPkr4OO9Gbgiq7s2l_rrT6fyFWJqcLxa9sgTB6jKPcPhV7WnIeuh2orKhgnQGYm27JnhlXvnmhylReuSJKf5Z1LGZvi-ReLz7zii8cKgWiZT6aRBboTuvtDbBexgB7g_1RArxBGJ4m0XX2EmJfr1_8wp2oCpqdVRVvKgxMY4w-TJzvy1EFbI3gBj5E7wnDLTMVocu0uHcOZfpJsWukAtK0vo1BsX5xwKGd35QR2iLhHLsQTR2HWUT3h0ZkSHupLzw4CLkuvG5dQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKVUUAwycGMv479FMhmSwajjtp1GhMBLweoUU6K3MIYIiXvyLuwjiVKN2zcuaAZwsChLvdnK36a5XQTL6bZ4UQCKL8jh9TNHKz9ymdbKSocvRuOes1mHBptRqcXC0qvWUPqy06WYZHp72XBcJ50-dtytPlH4l9oLrnDfu6gSxoSQO1QBoz5HSFkp8MovtJfbkvLDiAWpUr5QczM96M-MXubGTfDqwHrArZBgRc2S0GBwQZk2XZQVeAuhue6jCJgqZqucCR-O0nbf3LMYgoceZGhjEWiSqxKhTzi8isJ3_TJewOC_pZ4S8hxtH7aCyRrqWire38glLyF06exp4SXVsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=U6eklplYRunUigj78LWmy0wVTeat9C5KnzPA8beN0xTzCGHqPY02AocGb6dkNbl111nzs7App977ItFlOuhISlllxKr8wDYqZsM2JTkV9HH7m-IwupyT7als0DbsXkGpSy3goc7KZVGfTzmBukIQt1Atsa_8hA_3CB23Q0pE6yieixUeV2CGsKe4Sl-3CTPW5MT2rJNdY1qbdIECM0ipgZBABp5s4xSvQbxcXi7GlZWhcATd-0I5b-U_jKep6nZn-TgtsKrZ7L-98Y_ak8UseqjeIp8KPLMox0vuBbwQPlmqU2Ggs-UYLZ4hKPRXM0sF6kE9A6aigwksGhVOGa3Fdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=U6eklplYRunUigj78LWmy0wVTeat9C5KnzPA8beN0xTzCGHqPY02AocGb6dkNbl111nzs7App977ItFlOuhISlllxKr8wDYqZsM2JTkV9HH7m-IwupyT7als0DbsXkGpSy3goc7KZVGfTzmBukIQt1Atsa_8hA_3CB23Q0pE6yieixUeV2CGsKe4Sl-3CTPW5MT2rJNdY1qbdIECM0ipgZBABp5s4xSvQbxcXi7GlZWhcATd-0I5b-U_jKep6nZn-TgtsKrZ7L-98Y_ak8UseqjeIp8KPLMox0vuBbwQPlmqU2Ggs-UYLZ4hKPRXM0sF6kE9A6aigwksGhVOGa3Fdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZ8MErY_zk2XxgK5GMxYE2uVXZ95E6qHTShi_6mgPP3GF68tTioUesbIbVMliZ7zHnVuqqYBWjXscpmtQqYDi0yhM9ODpnRo8IQ4OHp0R7uh72dQUQEBUsogM8u6UirDjqLSSShlAhkGwVul1xpVaPBkfYCauv4xTz_4JOgZQwvgIhR9HRelKOSFvyv2bof27LFMfRhVRNuW3fmk2YDH8GpTBlUPXNbqG8ceyd_cBBL5C63WtB2ei_o185AQdvun-BYX9LVN6AY_Unb9WqKSV6oJDcz41QOrxut5e-TI_HDRBPZjq5ozxbmtw2bAV1qAT84KGS3-PQRCQ5D1c62mCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLYWdk-oJVR1QsSQbu-dzj5lWMaX9mye1y4zvA-6DiE4XutfSzqIUC_bLjumWo0PGMSo6Ehpug8qMxPEsmdaR2nowEq-ZB6-U4YlaweVm0gigPDYjkPGX5SvJuDK2brTzgE4p-8qFupUL20UOVyFpT-1QlzL6r3c__IavqPnpdAy2hiPhbGCQA4oWvBwyHUoHQTsgUrUquOFHkfvPSLjPOr3PFV_RtecBNIiClgoh1rFMzekfBBGutdlf1pCfkC8pjGbJ5Y7ojIEg3SnSEhGsfqOsGZAh9CepFqIfJnwkzxJ6Lc5r59Qe95cTTJ5abib3U6yynwJwOSDdcLHEXfbfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBHYHdH8VNdyLEIejyE4j9N2MuxztPW_I0x-VpyUJCbvFLDQnHSk-5j-_nyj6kHBlkqRBXm0bZl_bY7K80ca9RrpbRwBcnxYHCDlv3NGCiW7JKn15vHB2aCc5uFn9FL71HBgzrqfncjp2pWCe4t9g_XPIcLgLWMzp4thbQJ3NTFXWaERLX0gTkf1emm0lKyAY1EJ-htpb7eu_y-cls0gp0vR1lUteQxXQLdXLWFOjS8slMHzcyxxpFl8B75tL9_1WeEE8pL-iHJC-j_wYHz1PlN6s_4aZulVrBE_zja58PE4csyH9D8ssmWSv_SBFYLZdW6DXZDAvOWfQBhgC2_Rvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛
رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22050" target="_blank">📅 12:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22049">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hePfh8mt-RKyprzo70d74oi91Vl0PsMH7iRRFZp4KBOhsHYnm8YJf24ydMsFd1QKfj7hsh2uc0XBL0Nc8M9Q0QK5nkBfRe7V4SeaGfaXiQ6LJ0a2K-zP3zpkgeSeY1pjrjciDdhJKb2PZqaTvspib7sXMaawxb8ab1EafhKCFqQUoxHdyM25qZNGBtIFW4xuA-5Uro1_v1lOy4WBhua2qpSK68p9K1VP-xaWvqYDcwtlTFUQNGyyatWBfSSm2GIwBCiQ-1x2DxjpdzbJ3EL6_fzizlgmVGHxpK1QLBCMrJFdXmcrK1cEa4OEB5LQfEEGwKzjDV8N2jxWo7ypVkjfTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITVwCMPKPHfaGGmyvSYSVIw40X7RLC2t1Q-4sIjcvDPNcfpZcRNawRxAqp52DreZ2b5r0IXDcC1REQcXnLtXajlRJymXgQS8O-CyjpLzWhkNYUUzxiurESu2_ZdqBWosSfQIYkKXB_oV2O5ECZeuUEuMqGO0cFe0m2ll5QvvWrp0SArjADMfU2y3Vslm0e9C91oSvtooGXFEzeEAuKeHv_pwxjTYltlbzJ0R3v97SQZQKd8ew7q9P5LkCeX8w4AjRmYtziKpum86Wsm5VYbrJUsCz49Y05Fli1xpAXokGo79s09afbmYE2rRsmEDLg68jety8BFF5FZ5EIVbEiM-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3oCMYcouinkfHMpNj_pnc0EBCAgFKT7l1FKg5rZ86HlEPQYBJZR38ROcCNmiP0XM1tAC3gNzpoYZsdmn7XWAWBbYZ7A1D-F8XGq9kCI6s-g3cTNkmtPpVZ2JYkNdszlUmrSgBUalUQrAaUE2i58Ee_eR6QE85FqvsM_mvBXYU2RYR3JNiBJoQowzu5DLJom3Kq34-ICtVoLR-KGQG3rOi5frANn4bwbyaPa6M6m0Cq5x3z7vHwxBcpKQZOGKTKUkNUEPE6HTIPBkz706iW2cdMTQB_Z1dCzOD-cg2mWir2F0gueS_MJMb8-30m-BSvRjKM_fgt9UODZelexY7d85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZko77XF2NSDBSDFp90dfruEsaxsf9OUC_N2lDDrxlqnJ8N7UPAZ6ibc6asiNIQhILnby63vsPXjOy_9RprBBysssRu3MVb9kKKIt8PcljBafuuQr_gppQeUJtYdurrwhcCctYQIflglS6NvVC55ROW2nxVGEv5DpSrNTbAkVxTnhBqN_HjohHBHiLNS2NWASPvUd3O_la5BwVKfgEnthY0ZgOvbDXiFAbRO16S_4eQeMvInviD_qxdff-alwH9K82ooLvQELNiGyBKhPwzrxQoGYK2gI8h5AMSlsVh-B6AqpDST6Y5boUP6nKcqRTLV5M07Ui-OdlpxEA-8j51ceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
طبق شنیده های رسانه پرشیانا؛ ایجنت‌ خارجی‌های باشگاه‌استقلال به علی تاجرنیا قول داده که تمامی هماهنگی های لازم رو با این بازیکنان انجام داده و درصورت‌وقوع جنگ‌این‌بازیکنان باآبی‌ها فسخ نمیکنند. ایجنت آنتونیوآدان،ماشاریپوف، آشورماتف، یاسر آسانی، داکنز نازون…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/22046" target="_blank">📅 12:06 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22045">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=XU85Nlyr6-o4bA-7Eqyo7xSg5I9YFT_4-2KvG4M0gUaTxcENHUJzRDExODcZWqxRTXTLEyIbVpnaLdBclka5DDvi3xA3rjQEkItvdc-I7NSZM1VwUt3VcwPiRsShIfE80bSRN3uItU74omgXsU1816r8SkaRqAkTYDsEQJSfmZD-koBWjsVUtsjtX3oAu0lhTLIcn7RkmzhSI_S52sImNvvUfxzS-SJse2JThvkclPLad7EjHz0YM88eL0BCetnzmtO9CQDMAiyKd66iymzmMFOC5fCiZ9xujDW4OSpXv581XBf7-eB4zLbhtJYuO0gbhlSm_VNYce2M92MHyc12vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=XU85Nlyr6-o4bA-7Eqyo7xSg5I9YFT_4-2KvG4M0gUaTxcENHUJzRDExODcZWqxRTXTLEyIbVpnaLdBclka5DDvi3xA3rjQEkItvdc-I7NSZM1VwUt3VcwPiRsShIfE80bSRN3uItU74omgXsU1816r8SkaRqAkTYDsEQJSfmZD-koBWjsVUtsjtX3oAu0lhTLIcn7RkmzhSI_S52sImNvvUfxzS-SJse2JThvkclPLad7EjHz0YM88eL0BCetnzmtO9CQDMAiyKd66iymzmMFOC5fCiZ9xujDW4OSpXv581XBf7-eB4zLbhtJYuO0gbhlSm_VNYce2M92MHyc12vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله موحد اسطوره‌تاریخی و بی‌بدیل‌کشتی ایران متاسفانه چشم از جهان بست و به رحمت خدا رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/persiana_Soccer/22045" target="_blank">📅 12:55 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=oiu_MgkwDWDIfSVwyM0otoUV18t-MS7lr3z5q5lrreYf47zn1mU862B5txBuH2PqzhxPfgoqUw-CQQ4B5OSLtyriGHCYwYMLb3WStB-k_w2R1BGKjWXvezN-lqYu6t4OFiZmFAKDtsXWxWDUoLRm2ivaTb4rTbVQ1uQCdcVVxbBz4cQ28xeRITBhBduNvdEqGLet7Nbbyork1VBzSLLa_6dJ4kE0Gh2Dtp11oXN9jAuVm_36FRV6oqf8gckorwFyu4C6X0sNTIEp91A2ijb20Rbs0BphUjWpMpkGzYQkBNeJuK8bsfcmMNSoMMllzTVIO2Muhiv5XJ0tEL-fSdlmgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=oiu_MgkwDWDIfSVwyM0otoUV18t-MS7lr3z5q5lrreYf47zn1mU862B5txBuH2PqzhxPfgoqUw-CQQ4B5OSLtyriGHCYwYMLb3WStB-k_w2R1BGKjWXvezN-lqYu6t4OFiZmFAKDtsXWxWDUoLRm2ivaTb4rTbVQ1uQCdcVVxbBz4cQ28xeRITBhBduNvdEqGLet7Nbbyork1VBzSLLa_6dJ4kE0Gh2Dtp11oXN9jAuVm_36FRV6oqf8gckorwFyu4C6X0sNTIEp91A2ijb20Rbs0BphUjWpMpkGzYQkBNeJuK8bsfcmMNSoMMllzTVIO2Muhiv5XJ0tEL-fSdlmgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوال عجیب خبرنگار:
اگه تیم جمهوری اسلامی قهرمان جام‌جهانی‌بشه‌چه‌اتفاقی خواهد افتاد؟ دونالد ترامپ: اگه قهرمان بشن باید نگران این موضوع بود. احتمالا تیم‌خوبی‌دارن. تیمشون خوبه؟ نظر تو چیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/22044" target="_blank">📅 12:52 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22043">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kv1sHZs27iIyVFa_s17FgTRI5muSiVuFLGzPGiQs35mUwb7c7UaXUB9XNu-Qbp5G77TXmbX1a-VmVODOK0RzzT_HlzFFCVfaBeK736ybUlgPwOQ4a40ATWtsZ7eKTv4h5jGIgu8Sdb60BtxcGK0qH826AXLnviR_s32NESnEebXSORSYZUZeJb6ZtNm8CWYzD0RK0_Kco8eK0qBSVsHh3yqMN2vf45zknWCkbcfzBUmA8v4ti4Pb4qKx9H4oaMggpdXolUAxDbIfFwuLIUZanjXM7TyulayTiMPx9qy6JI99Z7Gr__9_RAFsPPE-caJWfFbQJKvTHU7O-x9QrjM6zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/persiana_Soccer/22043" target="_blank">📅 21:22 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfvanphqSDw9hTMj2hub6eV4zAGf07yFYYiqT2qSoKPuioz0R40F_F6bZfThGWLvBUBnHU7zcCPQWRI1mdOsnUwZ9teysru41zBPBJ_r5aYqgZSZeWCZuGnLi0bSYZDODkt0cu9JYVmVeZAeIVeelOtJ57whX4XJNB1oKX7YkOLAOX_vTLpKuKrxOPkMoNZwh4Oqcg9PbR0jndTh_Ao-oig-vjfbSKkA40kaYM7p2638Xdu6dpRGmtvH-968MVvsmG4TmIbQzpJr8gWvmuRkfHS7YrpAfR8N5w4E5OnWEDrPZhmsk8Eu5HAvnbuL5P8P_CCnGAwnZGQp3VsZka0z9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/22041" target="_blank">📅 21:17 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvkNsVEgafRMavzA5zhGDooM2qKQ6SISZnGWbTzaPZjX5Ur-U2Dhi0-D2j2DF0xwB3OoHT7CYxfXxR8dpx1go2-a-9g147xYIW4el-2MziCd04_gZ_PU0mjJixlPfEjd64XY5sOarMe4qVxuiQyp5I0MSba_lw9psuMwn-Vj1j2d0jdSFpH3BaMIy0V4y1QppIXMrBAb_vsZsk6qSL8wf-GcMOKM36Tc6QuIUsVtPukB-AukkUIQelMzXruF-0muvW9XwAnZ8pv0z4HQkWema83vSs8KDu2eNwANYS6lbTonm6ZrO_MZzAUl_6L1CCI7NuzXvbJJlnQw_OAjn8yBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلیس‌کانادا از ورود مهدی‌تاج‌وهمراهانش به خاک این کشور جلوگیری کرد و آنها کانادا را ترک کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/22040" target="_blank">📅 21:14 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22037">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGQpj4TitP9IcSE0cnEL4Ak5SpzICGEUQUEOAplNVyS1UJarl-RnDdLAR4TWIrv0s09Km2H3yqmPyjJ62rZLcDRVKPEz1Q3uROQBe-b_kZBoBhm6l0rdncQUMuMEocLQ7PYqE8hqYAjgWaT7TEf-HNmUtl7E6piQagPL7Jib0D6nUgFqJyjIMzSFc5mTOllCYUo1empcog93JGTM_bsdqEU7I-zf9UjJh-myTjiXDZDcq7ULBOG79PvsY603fDBkqxiUfhloaOObiJeCM2e4Sugaydh7z2RXg5iEep6XUXkScSZFV0Zuv4tebFe0Atq00sVqvO4cNgGvyEhGRgZisA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تاج رئیس فدراسیون‌فوتبال:
اگه لیگ برتر برگزار نشود استقلال رو بعنوان‌قهرمان لیگ برتر در این فصل به کنفدراسیون فوتبال آسیا معرفی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/22037" target="_blank">📅 11:35 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22036">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLtN_OpnMOUabbBsfzGPtNJ4XvyEPABFPSV-Ww7D-kwjWSX3sy6yRD-BVSczGdKnm_Ah7Xjk6kYRUUJkwzIxcd9KJMq_Y1vTN5RJFfoQCJoEtdJBKjSg67yNfYQsyMi4XbsbJHASD100VLqiKjqn3ri51KdNiPg5TOUDOhu9glqkxpecuU5m7w5S_cuyrtzMtuEs2Uac4uP3HRb4UsIb-qvbxCfjs4mv99RlZab8ytsu6k9sTK3bw0C2OGQ6bq_STbncJrAu8FGNdsvEdHgv1H9QzwET9B47mvheQKka5i6c3MGO9ebF6NgZigzFk5BCra2cO_Z9ks7gV4973MdnPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجمین‌حضورکارلوس درآوردگاه بزرگ!
کی‌روش با غنا در جام جهانی؛ کارلوس‌کی‌روش بعنوان سرمربی جدید تیم ملی غنا انتخاب شد تا برای پنجمین بار متوالی حضور در جام جهانی را تجربه کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/22036" target="_blank">📅 11:27 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22035">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lb9HbNuZuudVLQEZMez78Hd2d9wDmEJuvZtn2qz_VCV6FYuyUDNpAjmouZY61N_i5AqWSkDjNx_BfO7MCv5aHg54Gyr2jtXbnOPOGq2-VW0Z3Ov4V6SFSXybKuSyqIQsepRK1tfg_HDF7kKXGynje99R-vPrCJ64nRBKI1HoyA3rEv00G92CRZKGAteEEeGk4HZcLBoar5PmKAMcezzhwwhePu76Yc9esqxfhK-qGLtGpR-OBahbNBwfafpYBBnToCBW136GgiRQW1TK9fc9luRWCtu5m1zhy9SZ0JiaxP2W-f3_nx4RIAmEYNArJinB6cKOUFg7Fu6y0o5xUWAi2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌انتخاب‌مارکت؛ 10 مهاجم‌گران‌قیمت دنیای فوتبال
حضور 5 بازیکن فرانسوی در لیست 10 نفره نشان از خوشبختی دیدیه دشان در جام‌جهانی پیش‌رو دارد!‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/22035" target="_blank">📅 11:11 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22034">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=l1uMUZJSlhPyoCAyqVmx6TlYmE7JD8Ev-E0rl18QZubBEOfaE1dLTncT2J3m74TaAXj8wuQKr3LNvqkQFXuS3nXuVOekYKQGlhk60kM-MyC1cqy5vFZ7qnmBU0-WN-Jkrbq59WbfmS5qVn4HeW4l7Du7ccES8TMjKpVRUhg8D4rvLwhoKVIlnP1-jfJVwkdsM2XzZrPRNlpgB7bpjYnREdw1hNV5_5RKbfOmygRRu0GEfI1LHM0EYawwTKOxsuKMSuGxk1WNODX90PmuoQ7g_9pHrEyEnP5TVMmvd_vTZ9b7A_6gxmJH5T1GDBrHU0afvzbdvTziauTCxJHcBPKmYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=l1uMUZJSlhPyoCAyqVmx6TlYmE7JD8Ev-E0rl18QZubBEOfaE1dLTncT2J3m74TaAXj8wuQKr3LNvqkQFXuS3nXuVOekYKQGlhk60kM-MyC1cqy5vFZ7qnmBU0-WN-Jkrbq59WbfmS5qVn4HeW4l7Du7ccES8TMjKpVRUhg8D4rvLwhoKVIlnP1-jfJVwkdsM2XzZrPRNlpgB7bpjYnREdw1hNV5_5RKbfOmygRRu0GEfI1LHM0EYawwTKOxsuKMSuGxk1WNODX90PmuoQ7g_9pHrEyEnP5TVMmvd_vTZ9b7A_6gxmJH5T1GDBrHU0afvzbdvTziauTCxJHcBPKmYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سوپرگل تماشایی در بازی دیشب لیگ‌مراکش که احتمالا برنده پوشکاش ۲۰۲۶ میشه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/22034" target="_blank">📅 09:07 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0eJg3Aq01dhWZpafYNykKsqhhDYnUwnsY3TKN5dt6DJ7RqIb82ow6pjxxBzTCx7UXyxymZZkls7DkA83BYKGykYtN4nnuDUu3z7JfHHSJiZZlqhRfCY--WA3hhKwafRr-TaiN4p4AgMKoXhQfy1odUuTQSBrYwK_kJ7isQl7zbOsKFqakjXX1whuzEFlbBfh9UsrcSy77h9zwts20Mxs-8LBXhzvxQh82ERicE8J51bKlCtEMm-qQ2XE1cy1BYpqYNW6o1kWiEYbfqM5k1D_UmvaIEo3Rxs_eVY281KmkBMXi0UH9q7lrRaauFypjfhkTVY2Slxbp6akZcwOkqc7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTDbXlSeuuVzbkOSWar2ym7b8B9WBvDGWxlRjUg4Tx90XfADFmSet9jKqk63oBxynCrN9XalE8CN5FLiaUQj89RIznFpQp0fIqnm_u7Qif6y-SEFC4KQmGGr7tGJNSj6o-_aTlNxRfeLJ_3Fdy62WutLvLT9aEa9c56eK756olHRC_HtDWvuAbw3lkyjH4c8Mxt610i3mUFe1uTZdqDJDiiFAi_k_J7gyJ8-VM3Jf-wB-u5g6zGTd_ErOwbuyBoZ40Ow9UwZHCZ9cQUC-_vZP-LU7a2WF1qRyXXEBmwveHmC2t6-yj6vTUspeFAdfLbZgbNgyvfLh7JNsL5a7KwWOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چهار تیم‌ نهایی قاره‌ اروپا که امشب هم موفق به راه‌یابی به مسابقات جام‌جهانی شدند. ایتالیا هم برای سومین‌دوره متوالی از صعود بازموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/22024" target="_blank">📅 01:10 · 12 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LL9Iw3gSfFqT-x1agowk88JYoE9G5Hq7V-9tT8zTMNWnJ-hX59EMlR5eCQolboJx2eC9dD-ElMpg5C27pX6Ghcie5xn3sbwuDUB1iNLDIESgLhhYX4t4Ii6mbkd2UEK2yLxAzy-62sWy4gQdN5appwcXMNNqTOtgGQuTRkboemCJdf1H6CyXkDtBe2Dz5R9DrWKlR94f3l86RhDiNZsgV9f9Mg3aUCMWT-K5OlcHfq-S4oa_zlvzMhMnkUBqGJvnQ8-BHG4vwOCwNVxx2-Fj-Mf91im8NWfVcI1GUsiLgqcyXlA5HtaUgOCaklo7O4LuypR_NAq_RieoGQtI5SS98w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏مثلث رجزخوان‌؛ یکی‌را ترامپ‌زد، یکی را نتانیاهو و آخری راشریکی‌زدند.‌عاقبت رجزخوانی بی‌پشتوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/22014" target="_blank">📅 10:29 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRmIxHkWVZTftaLYNYC8qc9zWwTGA4PKJMAFdgOlWrHSuq1QKPmvP46chKKhXXqZx_bgH3SPeAKp49qoI2R5d6eiGCaBTP3-kXqPkdVAXgbXFGM4reBzwXKDSkjb-6Sa4KM8AYrg5micGXezCENDunwP-SVV64j4P2Dk7MYyTCfwNrHYoPUNcL-zW1wEHBdWOnEr1nbj7ORM8iINsc4GTq8EoWjluBpl87f37f3KnIW3bI5DE3YJ_QN_nOnSCj7MmYzhlcObTZAcFQwjSlgXf4OvB69LzvN5_X3s7Mbp6bLklmWVv8XrbNgCBedDFtsoOy0J7m9ASlL3pjcDeYibFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22013" target="_blank">📅 01:26 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22012">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMd9e6q2_ySlDD6upA6ltLmgj6IHac7BFogj32ktCrKPHoE8Poc13FxyG7O3PRkmEliw6pxAB5O5iUvDTgPs8eHk7GTfdOq7vCkh0UhsJ8vTM1GlcqRNv0pHSvHPo1xF5V2noeFwu7Kge_BtBp_HbVRC-KNLTMEKf6pF4JVsAhmYcpfbf-wQMSsx28jqi7CO7Mki1Vbyo53u10LKyRCgRTINT_jDsKF2e10RtWqZj3V9s6zoZ4HmHHen5bzLOHHHnxNFOUGU2JLuhKhO9AyTZT09KJfpoNOb5jsC6-y-cqaNbWZeghG2SPDoFJZzxKON2gV7uaoEhkc6_Y-g9Qna1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید مارک لوین فرد نزدیک به ترامپ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/22012" target="_blank">📅 11:23 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwcR_O3yw0h-g2wh1iVw8P98dLrTAiWFyVEUMyqKJaKeAFB-oTl6AENuab3Damcv0pq6tJ2mfsGjEiKmo2ayiF_B9cqk-pj4Avs3RzoLOtkKcO_w5Fw_yYuVOgbKwrdnx9IhBRUxxgI2mLWotBc-Up3tPByK9G37ED46ExIZ-DKqAWTmYydHfdPfRsgvSvCfB3Ojs70UgnsTctjGxbDBO81ppOTxaLAWf8898K9I-zVePmJoiCg-pcX_AOmvqxpvIi6wGhgMVgIZpDTmMxUBaueF7NCY0tYlZVHAnzbhPrNYW8r9j2h3lkt4cNdx0u5YIHA49hnudraoysfsgn4xqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گابریل ژسوس مهاجم برزیلی آرسنال کل این زمانو صبرکرده‌بود که انتقام‌شو از موسکوئرا بگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22011" target="_blank">📅 10:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22010">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGnIFKd70hdbHmXaelw7C7tVvetaJ9F_pZDrrTsmuA6m5yapTie0HKsL0cniWX0SywgUiX67oW1CedQr0BGzjQaFsltB7jaJGYi7pTox7NpEwMWX0qTJ9EdSHbbmBroVUgsjG5IsIcLHq72K436btXQNezc76CYA9WX4qfO_zOhW5B3-7Uh1fwHW_1B5LxIf6HlA2nYLIe9wGcFEolJRI2LTqsKQGLrc_-qdSxlHXEIHit1mDKccbYBvpWHC_KredIQHAafCB6p6pJ-Ayl-MLnujstRM6pnEZ9s4V1jXlI1GSYcgUx5uLagwhLk3f_cmD-vizFN6p0j59KkRaU5gFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22010" target="_blank">📅 10:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22009">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEvORuuxmruF-bK9POg03ba1rFHCT9CkE6v2S6S-mw-4mumwPAnw-04fVDLKicuBRCZq2BV2xtprZJX9pEDaxvHq4VF6nFxUhUkSPZfMDg_vgsxtpg_xHVNqE03mE4hRGNJpmZA7CX5CsUKSs9_bOXssGQ__O1pTLaH_sv_C0FQClWUiBKLYG-P7h9iGv_WBAm3_5Ku8gyq32ojMoS6vcOQUM-laMg9MvTn4Ovy4F7nDD06ejoPSrPZbWhJHk2_zuEQ_tJuRAhr9LHeC0gc3hs692U1EHJFbBrlZIi7tmr3PJDyXsoqirhEWtMZKm7ev6juvdEphbgUh8v3zfAbpyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L89ddluc3VN_hKN0K5qM91iJ7saD_ZzYOcfMpRk7QV5gf0ye-RO0GM6kf3easD-U07ecDSBa0d7_p6MuqPsvAMffMq8HthwHpv48rsujB07S095UQrWXK6wocjyLx7nWxyv41Kz5-1nGVCJStgzpwS72bzx5sMeBBZgfUSX4KDYYLxvz4sW-TPKghdFo5e-59a--7kqtsEjPaorngXNM1M_hICOc0mQFwaFLdYErWAe0rst3I1C3PUOoUs0z8FGgPcu3yZ_vGqU0Q_XgPWN07gcrZWWh-S4KrNfyOd1zTUtzXJWpCvFoIeDtVmFgh1B1jT3EHTM9KViu5XrhMyL-4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22008" target="_blank">📅 09:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22007">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLr9UtFGRfXyIIuvYWTqyaAM_Kl60yBVRzvKoZ9ShE9hdFLqGqOp1G-BlNRqhlRcHbuNWFlU_Ax-9CJJVZkAk9H4AADIZegrRIzskN8qtT-XYMcmehNDtl0EtEdi3PTeqLRVYqu34bHOyNhVIur60Y5UZleYwtfBCYZNHKqiEPnKLTvZiFsuQvxDCT2mS-MUoY-Dq5GTbPoCcFwgd0mRiJzVHS5nqzSr-mRrKZPRP2tdr22RKp7Tbl6Kfoz_AQ2cdoUVmY5ipbpP6E-eGQm9oEh4XpSducSEf3mnegUNKL49mgA53innbyrBNbknDH-WZry_ytydpLaiDDL8Qs4TCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرانکی دی‌یونگ کاپیتان هلندی بارسلونا به دلیل مصدومیت از ناحیه همسترینگ یک‌ماه دور از میادین خواهد بود. کیلیان‌امباپه ستاره فرانسوی رئال مادرید نیز به دلیل مصدومیت حدود 3 الی 4 هفته قادر به همراهی کهکشانی‌ها نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22007" target="_blank">📅 09:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22006">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=PfXzvPG38__LzXp6ymUMEHyGPCI_UuXy8_MDWc9dfIc58O4H6t4BKMlkgXb99ofOgxk9RS7RSwW8peNiKalQlbAtuWEEyS9vqgxELhTzYWvRHEW2h6lostRXIShPsVe2cFXicwfSF5sfuFMIzaY3JWiCQNJ6ohe_MVkIHH6FyuhFFymqrBH1OTSENZMgEX68NljZWOzLTJ7JcDev64T2LOFPhHO_fvxXZ9mj6gYwCeviCMx98wyKIxojHcRLFsY-CQUeN04HRqiqiN6xW_KcsNP12dV5WYP_8DCJHekFKvkEdpplakkb05qMRjjWS_nkoCQytlLX1KIgeNxJdz1LXBHLZBpT5J95folH-adxvy30-c5tnVtkYgFHf0-CGYHBQkavzNYmRjWIyMel2tDfzGoAyem69aOR2cOFgRMYIhbdLXfwWbHXfZIMzAvu13q2gXRYeA3c3O3NfpCGGG6cDTGa7m1pucDNfgjOZSBPzxvT__WHhljnUPk8GPNkD0RoysjeFUC5GB7ZGScto79jGOSdzxveQyloSPHYY6kHUZlhsNPRREalXGIX-JLgiSzoIGbEa9fVc_imRi0M42TWI1igItegnTWlsWxbOEgohwGUuOL1QB-7J1N2kXE09WbJ4qK2_gLFiQ_MfJ00ze4y4vM1qXgKg4jP-YtS-iMKmC8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=PfXzvPG38__LzXp6ymUMEHyGPCI_UuXy8_MDWc9dfIc58O4H6t4BKMlkgXb99ofOgxk9RS7RSwW8peNiKalQlbAtuWEEyS9vqgxELhTzYWvRHEW2h6lostRXIShPsVe2cFXicwfSF5sfuFMIzaY3JWiCQNJ6ohe_MVkIHH6FyuhFFymqrBH1OTSENZMgEX68NljZWOzLTJ7JcDev64T2LOFPhHO_fvxXZ9mj6gYwCeviCMx98wyKIxojHcRLFsY-CQUeN04HRqiqiN6xW_KcsNP12dV5WYP_8DCJHekFKvkEdpplakkb05qMRjjWS_nkoCQytlLX1KIgeNxJdz1LXBHLZBpT5J95folH-adxvy30-c5tnVtkYgFHf0-CGYHBQkavzNYmRjWIyMel2tDfzGoAyem69aOR2cOFgRMYIhbdLXfwWbHXfZIMzAvu13q2gXRYeA3c3O3NfpCGGG6cDTGa7m1pucDNfgjOZSBPzxvT__WHhljnUPk8GPNkD0RoysjeFUC5GB7ZGScto79jGOSdzxveQyloSPHYY6kHUZlhsNPRREalXGIX-JLgiSzoIGbEa9fVc_imRi0M42TWI1igItegnTWlsWxbOEgohwGUuOL1QB-7J1N2kXE09WbJ4qK2_gLFiQ_MfJ00ze4y4vM1qXgKg4jP-YtS-iMKmC8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
​​
مجموعه‌ای‌از بهترین‌کنترل‌توپ‌‌های سرمربیان در کنار زمین؛ دود از کنده بلند میشه و از این داستانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22006" target="_blank">📅 09:02 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22005">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aG0w0j5YzbiAgeJKvH4WwzoIA2MiHyliHiJVl7c0oHFQyqOoBTQxLD10RayT2UHTYm5Lslo3_onbsQuCDz6ZaQYmJR5PY1OT9uz5S0WdewTzNIJTWDO8G9FyqpbQxCjro9T79Ear8ubJeF3Kp1aE0MZsVjs-ovSGWB2bLxhqJPhmyKiUSurLDy7Cc1W1YkikQntmglCb_bVepNjwa5Bv619ClGCNJsNdMYAbkDTGgJxiqWCD2LX5t40rfSQFYmyI2bHXIztw2WdYaMgSGYiMseZlOBbeZgNLva_YGGnco2NvQgLe0egig7-MAYYKDuQLKwO93pfmJvD516jqUZh2UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛
از بازی خانگی بلوگرانا مقابل ویارئال تا دربی درکلاسیکر آلمان و دوئل شاگردان اوسمار ویرا برابر ذوب‌آهن در اصفهان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22005" target="_blank">📅 08:04 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22004">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfVzKi_ssuomx0AIwnxDPzUM8v2KkP9Qc3pz96tcEMZkpZQYoOIpVVfbp9ZSnaIxHhmQhpjPD5YI8Q_ILULt-mQ1ZkBYkK6KdjP11FTDh7QHAA6j6pX-XWJ3ZzkzzZP5hUYVwcuT9z8kNETbQrUjcKJCtt0wonn6skvK7rE5aXHctVsUVfVYATvF8hW95zuBAjPqdxM_RiwlsujB3rU7VCfwuHdkI7lP50kI1NqpXQ1leu9gfwi1M3P-ueRVb3Yu9xIHz95773U9l7c3By1hZN4BbhzxWTVymYFsNlnnba_MQtj0uzilC2j1GCB31zy6oFBAahKMuMomgDdc99ESUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌‌‌‌ دیدار های‌‌‌‌‌‌‌‌‌‌‌‌ دیروز؛
صدرنشینی آبی‌ها با برتری مقابل فجر سپاسی در شب درخشش روزبه
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/22004" target="_blank">📅 07:59 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22003">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B07h9RbnSYyv-aiicAoY4L7Glyz1GJ3YaWrYodzVqQAzC1Olag53-Z-ivdfbRCDE2_1SOd8Ai1sOyYYydtl58KtZVusmBrX5iDcKdqt-FOVze-qKk2ao-REITFyTKJgQFi9ETZZD4JfXgC6eHg2X4tltK01mFZ5hRjLO48sWJ4XZj5gUVByoReqChEl13Z3PM2jT_U6zEsXo-7ezLtSUCyPng6RT9iHPsKHVHM92cneOD-ktudU3p_eXBcKYUKdfj3KUN5VGPyx8o76Jwi_ntIvMKIg2mOnXEOIf6C8Ec0AF0ym4btLNc4Sbo66ah5kS952aqChOiAuag23WhROB0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین فرد نزدیک به ترامپ: علی لاریجانی، علی شمخانی و پسران شان دریک‌ماه‌اخیر نیم میلیارد دلار 500میلیون‌یورو ازایران‌خارج‌کردند و به‌روسیه و سنگاپور بردند. آنها از ارز، پول و طلا استفاده کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/22003" target="_blank">📅 00:21 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22002">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFZNildJIDuBeJRJlApG_z41ljoQdrOaQMJvl0IK2MQ9I9Z0q_w4w5ewHnKZW--Joly9Q8gnOrfHLz84lM7rXizui0DLQZk8aePkxxjsITJ96FxW5rvKMCwxK6iZliBLN--3tP2shjrdlnwQuXQhof6l6rHNZpu9GY4HpWto33vH9v40-uyrAJMxjO66GWmnaA3rd14FDzXc1-_2ce5oE23kdGik4KqY7-nWnLVoRtRA6GCPb9qVtClTj9PEsYBVUaZb1jaGfiDK_zkP66hegVc6jR8Id_vnNpXA3Y8VEtfCigZDaElAGL-_Rxh-ul7AePin_B-7J82ZOKKm5d7dmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/22002" target="_blank">📅 23:57 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22001">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQSYE4qRPZ7qBf6k7iOuuAx9v8MCzrFhmY-zT78dFoHX1p-nVgRiIjdYaSiG-bC7vZR2aC0S74Ye-tqyXrCQ-hqwFO-H03wRTtSI5m1r00WDVZI5whzvWf_9riDi3VGM5vIsssZxe2kioSso6at-eRKQpILOt9IxVX8ItF9TUT6ovHHZhZ0T_P6GQytdWpd8zSgPVUYHJM_g32Q4mu5_FpttQV2neCQsyq6u0oVNNBKN3m1Bba1omXvusH33igUyfP6EUqhpJLGkGc72O4ko2Mi6T_DIevgtxi2l_spCXVmknnAZPTgU6_ldRx4NvLyk1FNSFTLrrQpLHZYvMEkc4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌اوسمار ویرا سرمربی‌پرسپولیس؛ سروش رفیعی و امین‌کاظمیان علی‌رغم‌حواشی‌اخیر به‌لیست این تیم در بازی فردا با ذوب آهن اضافه شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/22001" target="_blank">📅 23:44 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22000">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=Nn3v_-sNjNCFAVOIPDNtYyyXA3Y8iHbG6y1fL_plaKhwTMGdRB5ot2_ffMvxshMsop3vWHNVibp5hNmVmGe4aC8-zqJAwXtoLq_lAQdCbq9U_wIZoJaiq8rZy10ByLCpiR9hWaekExIHVLe0TzR1SoTU8oYDNiH-vrX5ldIshvhYe_tc2FPxP3CZD3Y6sFzTe_vfVw4yt6L8U6igxDaRTHqh4rGsrWiBCuvbXGP7d7e8D2DvnC8cXzWEfFAbTHT910KQCH51FPqoorvtAz-k52SuZ89_Sqrnckq-UAgoEbFiWeiLvStJy_VxPegkI1m6kGHPEeUAStF_VaZWCDCGTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=Nn3v_-sNjNCFAVOIPDNtYyyXA3Y8iHbG6y1fL_plaKhwTMGdRB5ot2_ffMvxshMsop3vWHNVibp5hNmVmGe4aC8-zqJAwXtoLq_lAQdCbq9U_wIZoJaiq8rZy10ByLCpiR9hWaekExIHVLe0TzR1SoTU8oYDNiH-vrX5ldIshvhYe_tc2FPxP3CZD3Y6sFzTe_vfVw4yt6L8U6igxDaRTHqh4rGsrWiBCuvbXGP7d7e8D2DvnC8cXzWEfFAbTHT910KQCH51FPqoorvtAz-k52SuZ89_Sqrnckq-UAgoEbFiWeiLvStJy_VxPegkI1m6kGHPEeUAStF_VaZWCDCGTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لیونل‌مسی بازیکن‌سابق و اسطوره تیم بارسلونا یه‌تایمی کاشته‌هاش حکم پنالتی رو داشتن و تیم‌ها به هر شکلی که شده میخواستن جلوشو بگیرن اما!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/22000" target="_blank">📅 23:38 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21999">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_R8tDNy-1d3hO2cgo4w5VzZvH2h4cEi0UOQSSS41yOQ2fd-gSwmYgrLwHjXa9g8_6Uzahn9tliOZoCg_6tjXyDerkxfBS40scYfMx8FpBqhdGOaFCBUoBsGajGvoGTnsrBjIlfoy24i3YqQA5jg9QdEhP_Hsi2D96MyDzdjk4Jh4s5xWMOtqIPBD0xXp56IHDC-RKYKgquhbLXkYvZMbbbXxGVS22NWYIO69pSkP3ipqr3XE8z_SiUjqbVwQHTu4_M4cCYHsI4hNDWhdQa_BPaDjZI42fUl-yyyEHn9RcOyTa9deJ8ltDZRB9Z5d0tMK3rYL1ODXzfL5m1RT0ucDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
سعید مظفری زاده مدیرعامل تراکتور:
🔴
از سازمان‌نظام‌وظیفه استعلام گرفتیم که اعلام کردند علی رضا بیرانوند سرباز نیست اما باید تکلیف پایان‌نامه‌ دانشگاه‌اش راکامل مشخص‌کند و معافیت تحصیلی اش تمدید کند. او طبق قانون مشکلی برای همراهی تراکتور نخواهد داشت. تراکتور…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/21999" target="_blank">📅 23:05 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21998">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=OFLrFfgygOTU1n5hYHmLEv-tYpDmPZHg_aAzR_9_pSkkv0jlZXKcQ3wOCWggXv2CsnRFlxBJ5aFm5vDpYx-2A3uFpk2Xj2OcJSQYV8Z3G5ziIgU7k_5XvaQtt2IxZNP-4pFKxdh2kkbxcYj3Mt4m32AZdStQpjQcm0CgoSy4aK2noRSnCyTRjbwK4GO7PppDvAGqllO4mq5kGmWMAlaTIO78LkIVjHzL2ABl2zuY_TxDgoIuN4mlMy1CtlM9ZCJqvChyf9XU3gSJYVRfcbqK6RvKb5Wl6pLP1jJIyiznRWc8Lt4e3h78sEi3H0Zju5L5oUoQVAgB9d_b6ZHuhtjQDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=OFLrFfgygOTU1n5hYHmLEv-tYpDmPZHg_aAzR_9_pSkkv0jlZXKcQ3wOCWggXv2CsnRFlxBJ5aFm5vDpYx-2A3uFpk2Xj2OcJSQYV8Z3G5ziIgU7k_5XvaQtt2IxZNP-4pFKxdh2kkbxcYj3Mt4m32AZdStQpjQcm0CgoSy4aK2noRSnCyTRjbwK4GO7PppDvAGqllO4mq5kGmWMAlaTIO78LkIVjHzL2ABl2zuY_TxDgoIuN4mlMy1CtlM9ZCJqvChyf9XU3gSJYVRfcbqK6RvKb5Wl6pLP1jJIyiznRWc8Lt4e3h78sEi3H0Zju5L5oUoQVAgB9d_b6ZHuhtjQDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
مهدی شریفی مهاجم چارچوب شناس این فصل فجر سپاسی؛ استاد گلزنی به تیم‌های بزرگ ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/21998" target="_blank">📅 22:45 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21997">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194acea631.mp4?token=a0T_c6oROrLo_Zpd8gSODS29OPDrQAZY2mdedHoOhyOeX9v8uiYIcJW37pnJZHP1Nk7DWjIDYSl6z7Afc3Wj_RrqxuDmnj0eZ0ygj4HmA6QIXts7e4hVsPOJYRcCxzu44uoasT7Dtwm4LjNhJcMBkwb-n9fQYtAPwSwnKCey9SorjQZki6qPMd1mgsGE6umgYCZnNNitTp3ASFYH7OwW-DZi9V6iLsAHv4kDbQUIhjhpoAd9jMqOEzjigokm_kJimOcDxoq4gAE9cv85SUpgv4lNZwM-IO9rXMDPa_aeV4JlwwnA2CV-nw6Dja1E3V7n3ixy0PlZEXAjdKQwxu2heA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194acea631.mp4?token=a0T_c6oROrLo_Zpd8gSODS29OPDrQAZY2mdedHoOhyOeX9v8uiYIcJW37pnJZHP1Nk7DWjIDYSl6z7Afc3Wj_RrqxuDmnj0eZ0ygj4HmA6QIXts7e4hVsPOJYRcCxzu44uoasT7Dtwm4LjNhJcMBkwb-n9fQYtAPwSwnKCey9SorjQZki6qPMd1mgsGE6umgYCZnNNitTp3ASFYH7OwW-DZi9V6iLsAHv4kDbQUIhjhpoAd9jMqOEzjigokm_kJimOcDxoq4gAE9cv85SUpgv4lNZwM-IO9rXMDPa_aeV4JlwwnA2CV-nw6Dja1E3V7n3ixy0PlZEXAjdKQwxu2heA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش رضارشیدپور به فحشای‌ناموسی عجیب و غریب گه در صداوسیما جمهوری اسلامی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/21997" target="_blank">📅 22:35 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21996">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dk8TvOc7IXheKCYa05NceIgvkcnXaUeeHidudGKweZFF3okYP79AM-2SG2eYp2ainEaOImvzI8Odym6B3ycXu99IMmxsv6Q-RDxz_6X61_q-tTKT_YIPUyyMa1ihHPFV-2-spjbOCgavS10TpkpHgfBtzEHhOUqcqgLhYyKwyT5bpGiDKcZYutTzZruE_z8cikQWhOIlOaNfSaMIjv7QkThcWTf84LL3pAX6cBbL_Elye1_BisAsjlY1xEgYz51e_uv_DkDpSy2Kkcgc5RvudeO-Z73VjqwbsV10VbLda2LZr2OGhCs94svFHY65zmJojzGzxcGvP8ZKfGtN-3PKLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نیمار جونیور بعد از گلزنی‌ اش و شادی اش به سبک وینیسیوس: هرگز توهین نژادپرستانه رو قبول نمیکنم و به وینی‌گفتم که اگر دوباره گل زدی، همون خوشحالی رو انجام بده. منم به احترام و حمایت از وینیسیوس این شادی رو امشب انجام دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/21996" target="_blank">📅 22:21 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21995">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bebf41053.mp4?token=etcEi7Gmhe4Yshx-_NKB6Ajgh9k0f0e5SeZGIxs4KRJGKR-fvSkO7LvBKmWKxieG0dpQGW_cV8pokDR8-Y79aAwzX37HKLYE6fm-LUBGqKHrF7DtqqED5O1MCoRDKiTCi74pLIBvGIEl-uUA8nLbccVPhOEmEPdeIHbvU3oLjun3rO-8Hr_mrbl_Agi7ylF9w6n7AuiH2Z4E-Hc3TETxFlr6Ax4Tg5LPRJVZsz5aji15Zyr87SjICfO-vtWc9omGaljFzAFQk2AMqTxlhfYq8JMWIZXqjcEopsw01Ap4l5gaFHhBi-pWNN98uQ8LJ4EumqdeCypSfeZ8ChEQqRGDyruh7QfPPhPcW480HskfGk3U3mdwOj3-RUTUnap2J-XYfcBGakKRuGoWIjGwCffmt8YksMpThBO2YM1TOiVEHo1OAPyhl4CR-ZLi2v0lEmhxg32bQMuCNdlRCSKaHiJRmOyi-g4YjUHFlWEOgfuSiz3nSGn1vE-AC_icNhzgj1KMYqlpHgKSlEW-_zDg9R9PcRHePC5rI9sLZPJeuPB36ieur01AjOYgbQ1ptI2uVsX69Of7Ny89cudkX_ytMOYkpf4TysfsLq4V4uF9W_0jpoITBftYKEgJoUoVZWWFVcgdOOFP-uPTORWTMvkLfgBSrLk7gsqmhy-d38jcJscl4vo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bebf41053.mp4?token=etcEi7Gmhe4Yshx-_NKB6Ajgh9k0f0e5SeZGIxs4KRJGKR-fvSkO7LvBKmWKxieG0dpQGW_cV8pokDR8-Y79aAwzX37HKLYE6fm-LUBGqKHrF7DtqqED5O1MCoRDKiTCi74pLIBvGIEl-uUA8nLbccVPhOEmEPdeIHbvU3oLjun3rO-8Hr_mrbl_Agi7ylF9w6n7AuiH2Z4E-Hc3TETxFlr6Ax4Tg5LPRJVZsz5aji15Zyr87SjICfO-vtWc9omGaljFzAFQk2AMqTxlhfYq8JMWIZXqjcEopsw01Ap4l5gaFHhBi-pWNN98uQ8LJ4EumqdeCypSfeZ8ChEQqRGDyruh7QfPPhPcW480HskfGk3U3mdwOj3-RUTUnap2J-XYfcBGakKRuGoWIjGwCffmt8YksMpThBO2YM1TOiVEHo1OAPyhl4CR-ZLi2v0lEmhxg32bQMuCNdlRCSKaHiJRmOyi-g4YjUHFlWEOgfuSiz3nSGn1vE-AC_icNhzgj1KMYqlpHgKSlEW-_zDg9R9PcRHePC5rI9sLZPJeuPB36ieur01AjOYgbQ1ptI2uVsX69Of7Ny89cudkX_ytMOYkpf4TysfsLq4V4uF9W_0jpoITBftYKEgJoUoVZWWFVcgdOOFP-uPTORWTMvkLfgBSrLk7gsqmhy-d38jcJscl4vo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول رده‌بندی رقابت‌های لیگ‌برتر درپایان دیدار های امروز؛ سه تیم استقلال، تراکتور و سپاهان یک بازی کمتر نسبت به بقیه تیم‌ها انجام داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/21995" target="_blank">📅 21:59 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21994">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1529297a6d.mp4?token=ujtXcOd7hV65pzXc0Ny2mmLL6sY1Mf757LTwOCvbBHDGPC00tb2Sb__eqlPiteSdu1e2M7su27Fnm7_O2T97L7fAM9bWD0PquEkUkPWS9_AJzaCuyGzIOhinPnoBFKNtKgadUja0U2Il4Ddt0Pd6SDlaDessiAkDjyliCII8wzs1SahxItle6t9SdMAVRDF2a_rcoUC78vVHpfy2j93qq0kTAxKNSEElbsgb0BQYFYsc8dG5JBtT6dDLnzBTqm2wV7EofaNrGLtaHxKpgV6ooTh71ZLVtDPLeIL8ZFttnKX6DU1VJt1vReLQec495jZdkQxt5BP6HtzzTjh8vdfsW4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1529297a6d.mp4?token=ujtXcOd7hV65pzXc0Ny2mmLL6sY1Mf757LTwOCvbBHDGPC00tb2Sb__eqlPiteSdu1e2M7su27Fnm7_O2T97L7fAM9bWD0PquEkUkPWS9_AJzaCuyGzIOhinPnoBFKNtKgadUja0U2Il4Ddt0Pd6SDlaDessiAkDjyliCII8wzs1SahxItle6t9SdMAVRDF2a_rcoUC78vVHpfy2j93qq0kTAxKNSEElbsgb0BQYFYsc8dG5JBtT6dDLnzBTqm2wV7EofaNrGLtaHxKpgV6ooTh71ZLVtDPLeIL8ZFttnKX6DU1VJt1vReLQec495jZdkQxt5BP6HtzzTjh8vdfsW4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
#تکمیلی؛ رامین رضاییان ستاره 35 ساله فولاد امروز پنجمین پاس گل خود را برای این تیم به ثبت رساند و گل‌‌دوم‌‌فولادی‌ها که توسط محروقی به ثمر رسیده شد روی پاس ستاره مردمی این تیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/21994" target="_blank">📅 21:45 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21993">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeraTB8MDrtSqxN_ESKiis95ZK1WvOHePJjEBcdTkXUZoAUvYdkvsSzpF4C7UlpqLx_05Y_HT84tMYsrxtCR7eWJ_VMPCIAwQWOW4eJwgPBwu5YKLqm3hyUU3qiVE6RyY6Ml_JDv0JErJtbfldMDF7XerKXOz1-21UzroewmQJxHFs35QwaUlaFtygzH30ClipCouAIjH2KWC1_MRS1xoAOiZ1bu3BMOA1erCeqKiPZAGVMwNCG_Wy37mB9Va65CQu-TOJYV4O2lnWoSov6WL_oH5use8xaV133y6gIayW4W--oFyFYADKWosAEfgBbmgRv8Zxm4CgG67PUhYYxOKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
#تکمیلی؛ رامین رضاییان ستاره 35 ساله فولاد خوزستان با ثبت 1 گل و 4 پاس گل بعنوان بهترین بازیکن ماه بهمن رقابت‌های لیگ برتر انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/21993" target="_blank">📅 21:39 · 08 Esfand 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
