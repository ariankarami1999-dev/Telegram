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
<img src="https://cdn4.telesco.pe/file/JrsEPndXhLSjgYLqJVYtMPs8BKmyyFw6I7YufMwrAmGr0ltk2v91X0R6QEfJP_UaeGn28zUvMlTG0FUF_mH5St4Y4_fYF5xAISMptj1K59NCaCBeUCYIObIal48mL2bcQGyHXLZ_1sJzera8WgmnXupcWYiHwXsoxntCvG2JyyeAIP4oURvC4rqelfBpsMBacRGGXHbuqFnpFfrbQPSEIKAFhtGdilZ8gAFX-EPz-jQUWrHzICM1lYnfobjsc-6_CW5WvkYHpqLqWU6o7R8VHwUJAIbNOtQUKPSjRdu67mw0tu53ahnVKrK2IO8_APifon-X93ujEtC7H1BBwdGFmw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 172K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 22:38:20</div>
<hr>

<div class="tg-post" id="msg-22961">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmMPa18yyZ3Uq1itibpjHMiIt48VcFZbB9LYD0dvcAltfE1RWERzoqCmHRsbqV_90hxJBsSIJ6MUbI1rtEN2X6U9sa-DQLxctjv4PCF9KpsAFFoDtbta3ZrRCwKR_Sq2XSFD6siVF8X3uNAhdEVS11x9u9QgQa9W2S87EwN9b5CRDTGZmuIr46YvCr5oXyzajJoZX9_6i_5yxun7xZ1s2qqgm_0cuz3gIDvtMnCjOhCWQC16EdmI94mlTsxozTztXOBnfvDEHmoIifa-WDhANGSvbQKb38f6ok5-eer2Rw9sjtJH9O2oXgENRXOc8J6KNaZ4OKOZYM5c-9MWf8a1EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/persiana_Soccer/22961" target="_blank">📅 22:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22960">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW5xHiADNCzQQJZvMe8Ie2Ffbs12QZ2h3qkfxjgshjIFejvJrJCCag1QHqNWgG4iTm92T9QgHwc2XULigigZFQQwmSTvVpuviyIyvs98RSm3e3kT8cPiWFa6_kyNvX1efZ0SVBgqNm34UAE8xUEIrU0SXxnBryHEHpeVrbUflyo68I_XzqV_ClA3IhiKfucmQKKymajexekBXYekGQbf-YFcUWrJkHq41gESQQkf_5g1_V5N4OY2UmylrDPcpD4ouK5l6MSNm3FSqTZiQzpRMDnc8lTWhM-2uakNqqJdqme-J2HER0D4yvcdxLnCDxXuJFEc3KXNdwiYEFI9mufRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری
؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22960" target="_blank">📅 22:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22959">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j32RGU7pAzFhewz1alEYdHiSJqRPqPZ-ihV6kSMrwWszcENa-P3xEfQHcj4i7opAHwwa0iefQmAG-r1IY3IjRUY4dMXsLA053OEUlR3ZeL69RctcZnSwJx0lCpAtQtxl_V8B32D1KWIK8MdAQ60hZn-pP32eyTQKYWlO06J1BRMsdilQO38l5Lcw0M6EwdQL0ncjS1n87HMyCo0Mzc27HaOorjes0Qj4vWQeIpsTo9cjWmmTLkz_PtvQlOQ6hPBkc5_weM2ZsLHOkFMrDs1F5QWARCdLvO9ZLuUrbMU9PswtXk_zU1SFiN2SBcU2j4GFCxG-yuWEZHcpFK6p7RI6TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22959" target="_blank">📅 22:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22958">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=pPPyzydwm8yWNg2uhDNL0xR9xgFgrqc8NEXNccridLAPP7AU9-9-OlfAJKwcYiO7whEnLxf1fFmcHIkb2g0L8DHTiZx5h9rD9IUZJCUBiD9eaDv48VT2U8-fydINkh3RwOXLYWyavTaLnM2ettwdvHPcK7gAnM1qWEdtjrtBLtsS08-9ln2Qe11mqEeJVlTjHZ73GbGkysEq962Z2IDPdcTjIk9BnutZNxe-XfRHZjRnlXW21JXj0nRYtRo6MDvB47qRllc0PsOuXFdUEUk67DD5QWttvzTcu794Eko0i6vLW_BpWdrA1NBatCyYu7t7tdk1OepF8XADiaARh2QCIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=pPPyzydwm8yWNg2uhDNL0xR9xgFgrqc8NEXNccridLAPP7AU9-9-OlfAJKwcYiO7whEnLxf1fFmcHIkb2g0L8DHTiZx5h9rD9IUZJCUBiD9eaDv48VT2U8-fydINkh3RwOXLYWyavTaLnM2ettwdvHPcK7gAnM1qWEdtjrtBLtsS08-9ln2Qe11mqEeJVlTjHZ73GbGkysEq962Z2IDPdcTjIk9BnutZNxe-XfRHZjRnlXW21JXj0nRYtRo6MDvB47qRllc0PsOuXFdUEUk67DD5QWttvzTcu794Eko0i6vLW_BpWdrA1NBatCyYu7t7tdk1OepF8XADiaARh2QCIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/22958" target="_blank">📅 22:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22957">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCWZL-LZxPjDR8F6sWHB0JeT58_XTjZjOBQrmbhPjKelpYUdq-mr0vhHUUkosUoCGogfq3VGAHY7rkdvvTEyJAofo_ZeK4U6UqmwYCCjC1qvutakJNmBTsQeVj8v1Bt_cCvdu1Ztc0dy0K2sBuYlpvffDTd1tasE3WLPPpL46j01f6GXAsDyo86iW14Ce0j97ibpirJvbDIM7jMN-AVkNfOtRuhD69lVgxEHEO1ozG3ya3UojDtyoW0W01m10TQVN4otz9j5wHojT6kvCSDf3WgmjOMn_8y4IIAvmOVmETuN9Uibf_Xy7BMepvBp8mHIUo7PsTr3tn5VmZEcKHckVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ به‌احتمال فراوان آنتونیو آدان راهی لیگ امارات خواهدشد. او دو آفر از باشگاه‌ های اماراتی‌دریافت‌کرده.همانطور در روزهای‌قبل خبر دادیم جدایی آدان از استقلال قطعی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/22957" target="_blank">📅 21:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22956">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=NY8MsVSBv8g6Ru7Gav_QV9SPmDBEdffJ-vi8PhyXFOnpselKd93vft99sDaKXgJPeyECOxWJcKmSXl-mq7hgm-d6I6tunxrnKKxTPW_FNs3AqfVizG2r6AHoZdKxMKFIU7NA9uUd1XaNBKC5FjxAqJhs3v4usdgkuAFIK7L0mqgOGOdYJQwnpdUyBCO_llL3szy7E8j2HGX1iB7Vi4k6MwYBfDKYiwmEb_qi9A7XwiK-l1FPO4hkiQql1C8SVNddZGJq_3PIA65sLj85qrLlhK16YaPOHjYiEMl0jQsamApqxO75DMhfwE_C6u8uhSZYoNj7QwdXE3Om6Sw5yxRv2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=NY8MsVSBv8g6Ru7Gav_QV9SPmDBEdffJ-vi8PhyXFOnpselKd93vft99sDaKXgJPeyECOxWJcKmSXl-mq7hgm-d6I6tunxrnKKxTPW_FNs3AqfVizG2r6AHoZdKxMKFIU7NA9uUd1XaNBKC5FjxAqJhs3v4usdgkuAFIK7L0mqgOGOdYJQwnpdUyBCO_llL3szy7E8j2HGX1iB7Vi4k6MwYBfDKYiwmEb_qi9A7XwiK-l1FPO4hkiQql1C8SVNddZGJq_3PIA65sLj85qrLlhK16YaPOHjYiEMl0jQsamApqxO75DMhfwE_C6u8uhSZYoNj7QwdXE3Om6Sw5yxRv2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری
؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/persiana_Soccer/22956" target="_blank">📅 21:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22955">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-GJg8IJaaZDWavB2kObT3iojTopHIfQbBwry0Cx56pKoyqgegvK9t3URmq3UDvmnJ8af5ZvOSiAoOborqAFQuBre6beWjW6sfccDqbgkHorZjlJF8ZZ6cu__XmIGU13DKK0nWjUhydxFdfla1yp93-NemjtWX_vrFBemK16PLax78VAo7k47c1YcvjM6_boGCOhOUXkbe1Cagjg56SuSXBmMK_jEV1ky-a7SwVd3Uq6WZJLtxiKBxiAike6spiBecuASqGPPsIXpaj7HCqtc8ezBMcYdf6mNSX9AWbvnXXA4I3xRKSiElyOXnyUGoPZd6onghfZUHOCcrHukFgwPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ کادناسر: بعیده که‌سرانPSG ویتینیا یا ژائو نوس رو با رقم 150 میلیون یورو بفروشند. برای هرکدوم از این دو نفر حداقل 200M€ میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/22955" target="_blank">📅 21:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22953">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDxXFEBbpeVfGP--ZwyZ65s3CVyypGx2F0Rzp0cs-Tsa22Bk0vmoKdPQBMxvKDrIE4mrgKb8ypQGI9etiyh41coQmlUtYHO-O-yksHdVAQeGqA9xJyQ_HQfdGHv3d8jujlh1pS3VEO04ROfEAEYWK4Ywfyu0VAYIfofj6xq5z_KX9q35K2Z3p9dbfqbgORWxtN0_dznNaduEdX5tuBz0YPJMEcTdn0svjZXyaOIbqE-Kd3PQ9xEhuA165XKyAdZGF5wzg1jXVcuo1YFBy2GaBvem6U4dWQryOJmsp8itv14pXfISIiDoBeV8NWupT76GMAxE5fhgYnB6O7mHEdTNIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNlIWDAMawI8c-F3q0sHw3y64e35YIDgTy4DrHzuYCiZKW27JNJ0PTwYzox12QCvUMgHzMbzmNSEDxe9yPZC16kIkrH3yaQ3f7l6ZZybr54Eh231B6z3IPtm-BXRrUl7MxgjwDLn4qui0Gzs8vLdGmbnUJ6yDX-K0GVhfTxdsdEMNfuJEy9n2iBaCtoQgvmfX27hjdpi5XmncCvMGDBgYdImbsgpiw-oPJ2rFdiif5jvJzTvPeeJcpr4co6RknNnrcjRSROKvU35RCy6KEkHeF4cc-oFzU8jgeDtrug4I2P_BNIY4gJk_ZAzvMw_dPaoU5e21qDcUN81KtuRiDmxCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/22953" target="_blank">📅 21:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22952">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-aa02eBvqq28SPB36dYSmj8JZGpoNjsJYM7wLq-py0dUgm5sRHFjoSHBfW3ScrYziKJwSslblAyrfYvmK8-Wv8WZ6LQVhap8-5pnCkQBspBRxHgfxLviVf60TZgFU5lyZR5HBr9FCpNqmdYLPqYyWB_43poyQJlS1GxqAR8ok5XZqMah49D8h8POl4OmNwyiM0CFT3Xu7pHegH3G1A5kr5sJnvPBryOD5TehTiinusex6RMfsOO88gicBJMkSCcNxQ9KqRZY63cGS8YTml9IePaEKInEgMY1s3PCJvqGUtzeZ4py6m5JbTdrC_9v6OrcAcLYTuzThFw3Pe2FJFrAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
حواشی‌ دیدارآینده ایران
🆚
مصر در رقابت‌ های جام جهانی 2026 از نگاه هوش مصنوعی ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/22952" target="_blank">📅 21:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22951">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=vjDBSYmEz7LiEP1hUlZhHJC0P4yfojf4dO9K_USq46sg6P0wNpVXVrVb4kB0w4c1MaEOXplQKK4XtS4VMQNCFIldZv8JV95jGVK4Qt5eLC8cIvjlutNraqlPUfUHm7Bf0HcCAYtPJ5okIsFIQg3EzgrN5Vm46drdeBriropnKhejPpULjnfNOyAZPMmM14o9u6DtyieitSXhu7GZ1ar6sBLwElsQfWj4TkRRIgO4-t3MErIjJ56RDJdhA0d0n2HS7dYTYLT4gL3fz_3UdbvNqh-uxgY4Ag9wie97K8H3Z9Vg3xGkhAilvG_feNl9CjuO3wSdWwE3LiT1whc6KXUWvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=vjDBSYmEz7LiEP1hUlZhHJC0P4yfojf4dO9K_USq46sg6P0wNpVXVrVb4kB0w4c1MaEOXplQKK4XtS4VMQNCFIldZv8JV95jGVK4Qt5eLC8cIvjlutNraqlPUfUHm7Bf0HcCAYtPJ5okIsFIQg3EzgrN5Vm46drdeBriropnKhejPpULjnfNOyAZPMmM14o9u6DtyieitSXhu7GZ1ar6sBLwElsQfWj4TkRRIgO4-t3MErIjJ56RDJdhA0d0n2HS7dYTYLT4gL3fz_3UdbvNqh-uxgY4Ag9wie97K8H3Z9Vg3xGkhAilvG_feNl9CjuO3wSdWwE3LiT1whc6KXUWvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیکه‌های سنگین ابوطالب حسینی به تاج رئیس فدراسیون فوتبال درباره عدم صادر شدن ویزاش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/22951" target="_blank">📅 20:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22950">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_r2omQk9nt7Zps8EMMLifoiGAmIoUVnYyoVPuy8yJ6eW2V2XZTTIpHr-4TlbAryRqmZ4I2y_Aj4scHq7ZxYzoqVHgmjLOXi0DR39BCd2wxdF5MIaw8xiB_8dVCsmo6_hjiLLRcll-ppWp4KxEwsJ1k6x3LpReBuRFj0mY_vF89EZY2FGud6lBplKdElDum1gvTZfs3xhP7fd1_9UwHSTh1a_nT7QVfp66JBbtqLcsFYk1sQ50uJktfavONRHjqDrBbc95y4HL86qAzv22XwyntoGMopiy6BhauP4xBCvg1Q2UN3JUF4eNv7OGrfWpEZpwTaV7bCn_qb6_c47QcuEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/22950" target="_blank">📅 20:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22949">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNqMziCv3v7dKNR9Rlq0zLxoASKMR7wUPTzc6gUHFKiSiS-nTBB2dwvG-vKvy133OZQuYCpwX1F3z2c00bzo4D5Ee3PRx1FvQKoavQP-pf7PTZ-iI7xMyRfONVJa6ehAK-ojIqpdaNRnig4wAoY6XbaK2QIz3e9YPosaThF_cRrieggFVkfy_nWlCsQb_am5ho6q1hy0U54vc4XIcu3Rftf8JEoX_GvRW2dKSR5wSCVIghG8s7AiKQ7bcHxgJjvtG6q7dELy-j8voDl1P9fe2lglEiOycGyWkbglVZDLWQCqPozpdlgsP96YvQyvFnyWk2_Msk52ui0J4POInQanqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه کریس رونالدو در جام جهانی 2026 موفق به گلزنی شود؛ به مسن ترین بازیکن تاریخ این رقابت ها تبدیل خواهد شد که گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/22949" target="_blank">📅 19:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22948">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL8PzbXjWNhxaG9ojosFD_dHAvwFc95VqFuR-oZllT061v-mgsUXLDXLRm_QU28guRfBdTrGsthqiRgO3DdHzmwOIZHRp1qOdgS_6AleOkhQBpNAIYOqsQkGAQuVZmjT3gn-Qis7qQUqqYbzCe5q9G6oONldHWTkQQ4zU2drl9AlsndaHNqYklqFUXbBqFbzJ0FZ1KXIzMVr32lFjXWEMvREPlR1odC9OgpVbBb8hOWBEY7Iq4Xk444C4CpMxqVRTWk_TeIf1YUwGfoRqln9qxjk0Apxnt0yLHSxAGKKMTJ90mT0gJwEuCUPz4nGPbOFIRc1pdh2_DXv9EdDK8XDlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/22948" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22947">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=bwDwM3hh54NsAIpwkleiHjar4hFF9hWJqHUL03-apWvExh29eDY6QacCO-kVaGq3xzHqY0Vh6kYVXYPfQZHPSVicNLCH_yailZUUDBpbeoJ7Ya0kcKDIMtE-mexvZHoyj0V0zIaEuUvcU0EopL3KAljXxdgsgi3ht64tpitBCftaBFgtXLpFl6d3VUFTamK4ymWfmSqS4KMiYTrZsXk4cnT6loyRvlfsOUj9Sftk4guYeGcmJKQjheH_kgVn6q4SQwI_T3_E6JUif9Qd-iSn4nX6JIbDMN1_w8NlIKJuWThGyNFsXHbGns0a9CLD3WtCF1mSPUS5z7-8ekqhb7KmYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=bwDwM3hh54NsAIpwkleiHjar4hFF9hWJqHUL03-apWvExh29eDY6QacCO-kVaGq3xzHqY0Vh6kYVXYPfQZHPSVicNLCH_yailZUUDBpbeoJ7Ya0kcKDIMtE-mexvZHoyj0V0zIaEuUvcU0EopL3KAljXxdgsgi3ht64tpitBCftaBFgtXLpFl6d3VUFTamK4ymWfmSqS4KMiYTrZsXk4cnT6loyRvlfsOUj9Sftk4guYeGcmJKQjheH_kgVn6q4SQwI_T3_E6JUif9Qd-iSn4nX6JIbDMN1_w8NlIKJuWThGyNFsXHbGns0a9CLD3WtCF1mSPUS5z7-8ekqhb7KmYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
آقای‌ممفیس‌دپای‌هستن مهاجم هلندی اسبق بارسا منچستر و اتلتیکو که داخل و بیرون زمین می‌نوازد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/22947" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22946">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYjKdyXsQ-8FYOBTQMNQ0AWVscdVN4-INYvRyTzAYA3XLh0zCzY8oE3I1X8Ng9A60Yyb6qNtT9H3EuyhTxcJTLRDM2b3fG4QXG4JKtaoK7PBjZCB_ykcY4on6Qpa6AkfjJa4ki-O3_wk6jK0dcSVbgJKsTZ2xqcLPwZdHWIniJphhusiPQLl2sDJJnnhZMrDfNZivVBJ2rt3jZJPyVW_N1NhEYc49X-LLM3vHcUUVltMor-WHNOACsiAkhHZEw4tCZz18XOljc_AQQ7xZj4CJTe1RFFHF3jLSudAuN89YM9Y8e9K8RnXJOQJFvLK9YeoHgQVax4AmaJAfPaM6e7QIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
با ارز دیجیتال حسابت رو شارژ کن
🅰️
🅰️
🅰️
شارژ اضافی بگیر
✅
🎁
20% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
همراه با درگاه‌
#ریالی
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
16
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/22946" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22945">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zjwh9ZsOS26doBb8Am6h5R-Qv9N5RjWyY8ejGS7QtDeO01QwwCbad2U5ltNSqg8adGb7YYPw_OQjpq98tSipOw1stGhQl9w1YX_lirDfW3NlBDnt6J0QAJXvw3N6-9nDPPl-_eYyblywKpyTgtaeHgpr2VA5blZ0DV1Q8ps1ULzlnlJ1GOF76B5nXLPte4ERFEFSJg6oe5oENQoPWdvLRynDK5YIBp-vGQSUUWZvpeQ3KyzsxOM7PqfDFKTqbpnDiT5lO_qzM5xF5eETmYpzeQlF71LmQ67uu5jfr6dppYtI331ghS6FkneN3RUCvu0lwvxEPzunw5nzMuYDs4vG9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/22945" target="_blank">📅 18:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22944">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZePzDdby3EhFWEOxF2K5f7TeI4XBeEFlN24sQW9iMawxPT2tchFxBMs4gik9YaNjNgED9XnOaBeTGQrrvaLyXTp9vyOhKUKN_fRlemHHI6CX9KDBfmv2y3fZlcJy1uRL29k-MHfe90UCnnwvjqb94HHpXwn8VFyHLyPn0MhwBFPwoKvpM2oZqvnTjQdTwQWAMyBFr6MzeRa5V8KyW7GD721dxk-NIhA5UYFkeNgAgtmeWaDfSjDttdffkPHlszGfYNGeEcVRHGb0De1lNq2oVBqsY2wQkdCeBPQoIWPNWwAw5Ocb_jIHANse7JHJOl1ZPxoL1kScx2xcBG-EYoijA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: منتظرحمله‌این هفته فلورنتینو پرز برای نهایی کردن قرار داد مایکل اولیسه از بایرن مونیخ باشید. پرز قصد داره به هر قیمتی که شده فوق‌ستاره‌فرانسوی باواریایی‌ها رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/22944" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22943">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHly0IILeiePF_qCHBD4SRbb9Rm3urhHobK0ors47cB9I8QQvBepAliO5wsyqpdUFzNFhltqt32zv1QIgBgV_yKtTpQQ1NwCgTJhOMnDyaqiXGu9X_TkqTpTflW5YhfVvnQzRVWhorzEnwfhMX4MgUnyJ2VLeZg6QX7dZMadjSiU2kR0lpm5zPJQRoRrcJ5ldkuxTOOYKm0lPEpw6KVmykMlI6l9ljLmolS-5l1SifyNnv95zp8KQOD9H9PPWnFgtXJL_eJvZgI2mMagS0bbeAFr79NL5pzjoTE0npFC3GiiciTRK2-VRLH8qeyvqefG25hTwehdCDKPQky0bp4aQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22943" target="_blank">📅 18:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22942">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=sicwJ6XRrYTPdKE3leVthno2oNtLtV64FifYGqduBnaRPq4a9FMjQ2t9OtF0ElI4gq9V1j6oExA518h0NQp9WV1PG5azfxGNRc3GUnF0TFV9I2-8CAQRhj6Qz2iz8i-z8dmlPri-zVIoiruPQG5qao6YD8RwO8uvgO_aMLNGdJVYVXOHAjmjeNqVlJZFZsTZtrM2aQb3KzT1Nbp51TWl0cUEQ-5kFPoMuKdqwe_sDQCPd2ZPP-aqS3iPOUwkO6lAtfYjBTrr0CUDcfOUzUHFKqxVXTH1XLbwqLcjz9BRmY5AYfxFBfIXPxhGG61aSx27eEzm79st77ouGvCQisUghQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=sicwJ6XRrYTPdKE3leVthno2oNtLtV64FifYGqduBnaRPq4a9FMjQ2t9OtF0ElI4gq9V1j6oExA518h0NQp9WV1PG5azfxGNRc3GUnF0TFV9I2-8CAQRhj6Qz2iz8i-z8dmlPri-zVIoiruPQG5qao6YD8RwO8uvgO_aMLNGdJVYVXOHAjmjeNqVlJZFZsTZtrM2aQb3KzT1Nbp51TWl0cUEQ-5kFPoMuKdqwe_sDQCPd2ZPP-aqS3iPOUwkO6lAtfYjBTrr0CUDcfOUzUHFKqxVXTH1XLbwqLcjz9BRmY5AYfxFBfIXPxhGG61aSx27eEzm79st77ouGvCQisUghQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی‌از مسابقه‌کاراته‌معلولین؛ این چه حرکتی بود تو زدی آخه؟ چرا از روی‌ویلچره انداختیش پایین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22942" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22941">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-n7wNNqUz2oQks3v0F5Zm0KybnB3haXJNlAHOqHBg1LaHHONGaCgQmcgGXSKpUHCdiA9FzRnAXLUc9fXRRHSEp0r8QPdBgjG-4YIrWsQYaG4XAroy05o3YkiAqvhSyGwQzsy0FfMS2fLWVWyCMCb3w2-ozDSBxu2XA6U24GOIl0MiAsNg8Si-j_we4bpSuyQcILHlSuFCiDb4gRmzlTn-TPPb_oKfBaFwwdrrOs4vAGrHXfrY7YGPQI9o5t2OGTfctK7qlJlwlt18Ak-TYOR7xG1QzZHk2oHCjHPSbbZtMLboyJdxp7Jghm_bGWNCRPsKqAi0djslyPbZrKhp3IWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22941" target="_blank">📅 17:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22940">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzkX9afF1JyUjP2XblqhnlzKxxp9MMvVj6JCXbqln0RJ-yAuOsgERa44Gmt5_3GOnVzu1Ibxh45nChvzLR_JkDFearF4A5QRlYCQIHYedNSl_IJ3THg1RCwQayo5JL9YeW0FjLdxI7RswAxB2bzY_GYJ_3riLmDUKjp6Xvf0KoHfRwe_CQOSO7sY2Mc11s1EUUN0IyeRac_DwHOt8kWdyxv28qArW1-9Uz2jFZBjVP5DnZlG5QEYfmn5DtYwyK6_4sFTlX7U8d0ZkcAm4YEJ09lF7UXdazMYN5-OHzs6r90L2-_NeZYmoBmsw8cc7IpLUcoBEexaz4TqoFhmnQRE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ مدیریت باشگاه استقلال به دراگان اسکوچیچ پیشنهادداده‌که تنها دستیاری ایرانی‌اش در فصل آینده سهراب بختیاری‌زاده باشد که درصورتیکه جنگ پیش آمد و اسکوچیچ مجبور به ترک ایران شد بختیاری زاده سکان هدایت تیم رو بر عهده بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22940" target="_blank">📅 17:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22939">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJpOnoB_70ioQ34EcOzw6XXvOhoGCoG_7ZOe4YmWioh4jMWADJV7jNdvMikhCNsxgXsaYMPayCiqrB7UiIIl4RVV01mPyVUHjAP7zi_lzPtopQPVqq7teAoiIXUw_totezaVqImcUKj-7ARgtTGE5sGfkWLCqpEtdyrU1Xi_qmy937ywJe9FB6CpQFjGk-_QUvlBkBMjSDcc8OvlTxDBd5YuJeQQadWEh3nKcJm5G9tSykuu6fW64N-e3xBLPt5tFQ3gMsOzc1TAulABdh578DNwNILlhab5n6BnSvXHIxa24-1PUzPOaXG6OSJAxEobRM5U_RHGQbEImacCjRjoUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌ های رسانه پرشیانا؛ باشگاه پرسپولیس در تلاشه که مجوز فعالیت افشین پیروانی در لیگ برتر رو از نهادهای ذیربط بگیره و در فصل جدید رقابت‌ها به نیمکت سرخپوشان برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22939" target="_blank">📅 17:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22938">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOoqj4OYUryczkD-XGCOhBBAt3-iIJYwAG0Kzv4mTiZDu44CyfT9ImW2bVTHGkUfMecrM-fhEPbuABeFNeE7xn6E8aBeNdH300rsqBkREGc-cwGGhZ6s7Tlcimr7ng2zX27zNn8KRDrDpkmrxB0GEGSk0q_rgPDxMMQQpIUzFlZLc24zXJR719OEqaJucLwgWuFIlyKh8U9WBcA-G6j6XVzBibitPzAEhXU4xhiMktWUw-Znqz5hz5N9S-YjkAGaeTB4o1gFc_nu2-DyWTnNACr3BdGETWn2OGxADWE5RVV4cwSSIb_aZTMWZtlsbPXkpsleVvnnxvgkJG3lBYdQyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22938" target="_blank">📅 17:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22937">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7buQpaLnH069WTdS3o1OPcm5mGVwoiAGfghO_qN5VQxcJUMIekf-gb1eunHBOhT9E49vJS3UiwuaWCyif5CmDLiaDCgGqWDNTn7iL6srnX1nPVMn238Zze9y98AwxcZJgxd20b4zEPPjqVT-CdP5zhRwUsnsqaQLm6RVBC9pnKAdhlgpu3QDxGkEMwKS0fZN7bIP46xCJerw_YIMX0avNlVmW_7rSYkE_CtB0EVHukOO_2xGwiNOKPvpYTwMCVacTTQWwfskQgIEuH-uk2NipmfFbbn1FWFJoWMaZq0jHBZHMhClOElvWT3jkYt3EclbluY2MjvUeRZ-34RgtXr9u9k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7buQpaLnH069WTdS3o1OPcm5mGVwoiAGfghO_qN5VQxcJUMIekf-gb1eunHBOhT9E49vJS3UiwuaWCyif5CmDLiaDCgGqWDNTn7iL6srnX1nPVMn238Zze9y98AwxcZJgxd20b4zEPPjqVT-CdP5zhRwUsnsqaQLm6RVBC9pnKAdhlgpu3QDxGkEMwKS0fZN7bIP46xCJerw_YIMX0avNlVmW_7rSYkE_CtB0EVHukOO_2xGwiNOKPvpYTwMCVacTTQWwfskQgIEuH-uk2NipmfFbbn1FWFJoWMaZq0jHBZHMhClOElvWT3jkYt3EclbluY2MjvUeRZ-34RgtXr9u9k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اجرا چالش فوق العاده سخت ورزشکار روسی توسط یک ورزشکار ایرانی با رکورد زنی روسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22937" target="_blank">📅 16:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22936">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6gCaC4-YZtUZhvHU8FQ6AXoDXtYL_TvXcwTHvyMYnilnXHuuuXQhmfGkgNjokOFhcJkBd14ICrlavWg7mZiDz3vJVt2SMmwy-MXlImOcgJBuryZIiBSLBE1EyQkEHFvwuS6BIIbVfuc1L58XeQcZodeG_cx7lrvwSaju8drVhwxCruHjt4lpBEEJUkopBnP-Tr9knSZ7jB403xs8UyyXDS_VSvNVUxYa2Atn64z0HA6pELtA_NPsr5dbM6vRqA1SNBdNn-XOdSIbCPUj8ituD5Ki5o5VdnI2JDXvsIBid7O80V_TEhPrdFkIlF83tXmMcPQfg1uL0nEpF5eqr8cRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22936" target="_blank">📅 16:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22935">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lax9yhjKNL9vJ_rldEiGHvr5zW8Gq9qoZTiGGwjt0-BqE9KGiVEQIvh5wMpkvYPmjI77wipqWd5lCKHUh9fJsxhpEVfbV9uGgQWU24WmpqF0udAaHM7_NDRNZBQrNAWxXdzRHWWPDnXsycTjhJCMiskVQZ6vq2gwnSRVImDb1DX1GIWTfCWh4moLC7beDzlben6Y4hmakti5qd8yigLXiBKsILU_CHvHjI3oGkapZU-ISbsSDj_dfYUwCA9jE1pCApkwWTV_F3PDOqZMPKqAGzjaDavK3jeO7yjlYzxpHG9DbhiTLx6GDPuJ3k7IlFk8MBWhEtaRTvW1ymSGCaB54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌انتقالات|گستون‌ایدول‌ خبرنگار آرژانتینی: با جرأت بگم که آلوارز درنهایت از اتلتیکومادرید جدا میشه. مقصد بعدی آلوارز صدرصدر بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22935" target="_blank">📅 16:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22934">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGb4bf1aCCyq8tuGJ5mvYk5fT2TvU2YIOv3PTNnLs_2-y_Z1atgivEOjM_MWkpPA3HQj-fGN5RgYrq0VXXKIEuFL0rkXHttGTH5pkqyqTQzdmEDVJ4NODfcCZltxY3HqhAHHYBdTu5N_glROUyDovTrL3QoAK5i-sgLTK9gURw6EeMIMGFY-aX1kwPhHHQaR-vybV9arduGsVX4eVwbWG5j-L1r12oU5LElUz0EXKWzMMEMXLtsMYwKyloxJ01OetbKSbKVAuYwDmhQ85x8HM2-90ImFWPJTsye5urEOXgIB9c_BZTmt0mERtma9sVuQVdGkshcXk5ogMXbAqF_FZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22934" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22933">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=XkARHvqKBgZkA05ewjraQ5MTp94QtQjnNjc1iI3JMkQ2cHMu-rsr9XOPBdOwisFiInSU_uF0oNoK7QhtyyBlAKOj8w23wLhcwr9jl5Q_eJGE-UwPBMmGBY_2fSouINCnk1WBsf_9DsrNQqFScNvMZ32BbOd8RkO0B9LrV8ZD0NZ_xeWmY2RtdsNH4CRL40BtxQEqZGGnLe2v2DQzzP4gucWqPvWHxwxjU-2sQQnEEzAPYWTqg2uC6VLE-8vphzv7pY2M5gcBy3qgbDc_nl48rMVIe3sXnlGgWZEC1vVezgHIKPGu7nLJRx-_9AGB49lx_BAAf-hIZM-I_jdK6Iz-Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=XkARHvqKBgZkA05ewjraQ5MTp94QtQjnNjc1iI3JMkQ2cHMu-rsr9XOPBdOwisFiInSU_uF0oNoK7QhtyyBlAKOj8w23wLhcwr9jl5Q_eJGE-UwPBMmGBY_2fSouINCnk1WBsf_9DsrNQqFScNvMZ32BbOd8RkO0B9LrV8ZD0NZ_xeWmY2RtdsNH4CRL40BtxQEqZGGnLe2v2DQzzP4gucWqPvWHxwxjU-2sQQnEEzAPYWTqg2uC6VLE-8vphzv7pY2M5gcBy3qgbDc_nl48rMVIe3sXnlGgWZEC1vVezgHIKPGu7nLJRx-_9AGB49lx_BAAf-hIZM-I_jdK6Iz-Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آدریانا اولیوارس مدل مکزیکیم رو بدنش عکس تک تک بازیکنای جام‌جهانی رو چسبوند و از دخترای مکزیکی دیگم خواست این چالشو انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22933" target="_blank">📅 15:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22932">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icyxPyIMZLXOhBnszi35S8RatgFTuemTgjKWycB06ecJQF1CE7oE8D2uRfWfpGq8MPhhghIAOGgio9DV2rzWJ6FTB540MMUaqEGO2JEM_tIQof5YYfwZxdNP2LUysVdBz6_uZnKc5gKePympxw9b59Xfgon_4LHOh56rXpAdGv-X71IV_fOUQTaqOjmvtVwwBTe-wXCQThNIdBhoNQwRez4tEuin8y6_QaQM2CxdOdvzLrYsbx1uH-4Ssfn-X3D1cIaZfvGIXh_8Mr-dEsZG8o4G5FUqN0YKxB46OtkhpSA4aUvL_loQA3C-oglqH337dZAmcosOSOLc0HmTTQ_w9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
انتخابات‌ریاست‌باشگاه رئال‌مادرید از دقایقی قبل شروع شده و تاپایان امشب هم مشخص خواهد شد ریاست کهکشانی‌ها به کی خواهد رسید. شانس فلورنتینو پرز بسیار بیشتر از انریکه خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22932" target="_blank">📅 15:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22931">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu3cCPiB9biljzNroIHYzHyC89wbuPEBbARpbRLYq0Cm5gWvEqqkZeJgaq7ffeOaeEfH9mNTmxEczRW_zWx0HQs-8YvIYax3pjf5ISUkGWbpQywvM8yIo5k2EwzpKvK_-IllC1THLR9aCGvuHkpsixcGG3wKaQot2TsSSFyygcGDSOm3Xvn6BMz923GtXYWcr1Q4XwVKRkcV7OyIVS9srylj4oVSxs1oIse42mqBP-s-ktKnM5DgoztYdCYE3qhi7bGk9zvuYKT0zvpCjCfELURJ-uo07tt2J4dwGqrzqUmWhQuYgS-JTNpZzTNGzGDVekZMfRt0n1EPY3zTiYYMGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22931" target="_blank">📅 15:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22930">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvhkRFYyRgNlK-o_v4rpmEogdBCaM5gcd_UpFF7oQKzr4yzAQiG2BGm10gp7bc2HdalE6he3RQps4PrRds9vH8yfH0rsux6Sw-H3SO_F3U0s0I7MdKFRAMKQT_9e-GRjW_Dw4jUxa7kVxwA8I35fj0BjhkAREoBPfsJ7zreTrz_j622H3aocOYow6UXGLBsHUi5PV6ZFWCG0vmyq0qXEVGlVCvmjRX3Ci9jAW14xKmdmx2JsG2-Xb6xkjSkYshK8j0XVACLubgK_DCz3h-2Ehslj0TRxqsV7qOp1A7mtXjiagi_9MCd0Pxbd1z6NmQeoBWYGAB0iMkUleN9aBU5u-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22930" target="_blank">📅 14:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22929">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZl1mcDoI_JdnFB42XtXrYojR63BnVD3abjvllFIOeXuNhAFgQunmic6pVr0gK64ccnsf5_4FSr1ydBWXx84W6axrtVLpYdB9LBBH9f09pnwj7d46I3I7voEuSpPNRoG5jeEH81E--R0LoLVI9Z0cVg3XZCgGPwayf9SApwvGJINzcIXbuQltH3arXKpkkGclXCTsuejlzVeWmEL531IAuiopnl7e389Z1o9tLPQ2HGV6KRvG0WBV7pd69s0pyOy9esz8u1yWr-cwHopVPT05upQ78bYa7uhWTZmeMiJZqhv8u7ikLV36-XMa90qn-T4uVisARe8T_e3MQAeixzgXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22929" target="_blank">📅 14:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22927">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fq1YDIVfOjXgt2_yDpN6M-hVNnKckgY2c4cViBNErqKiXb5aRM9AjPyaiGGHJU-ME-ADEQ7OYm2jpQy1OUCGc1j7MJWliiQjnj_1fhM3IcmEPItjgmvLoisopdWOSaTISVMjFwayNhNJC_zMkFk9DtvwQu7NfalD-Wu0d9x5nL_oHjhhTdGAe7peTw1KPDKShMBsQgPwmUz07zq8GfJk63bSLkzXgP0ziPGZ7m4pTEAWhzHkNibcI_mQJ7GP72I2dqNe8vfhdSfWtFSPgr-d9HHOTX4iDWhKuhwT15MPuk-eXvrEGlcsj2hD71i9fk53ErSnZ-p-1bDQOsrkg1XJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGpnqHYCr0dQ_DyiXnVBayshFJ4LuhoXSzR_Jmq5XbtBGnpuNZS7j1bxhDoNQTlHh8KlEqVDEzEmk5eDE88VHmutflqJemHm7Zitez9Yf5WlTFz23jy8UvM32QsqgzHIJcejE0xg_ZFym2zoA8Y9-zeT3_I4KlDCURbGRzU5_8niK2P_uPNcliZ1U9-0TVsJdVuoxVYzi-ndLem9TzXeagOO_5L6VHmX-q7lTWZivqqqJ9eVAN4U1T42QaydtBmaKPWqGWL42XHYROHukcXmf0UdqSGqguyRueCUUCL4LxCh0VpUhP9TYJVjmkmKXIiDo6PkCSRjosidSPTBMa2XOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22927" target="_blank">📅 14:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22926">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZRbNBgpsVD2311F6i1IL-lk3Lj8sYXnf0ZdZnM_1Ox0PBmhYOJ7cecOV46KNXdqTsoNjBkJXdw8y3GXCKk3Q5wNa_j6Ju08XGIyU_pFvmK4Z7qwgYeUm_URcCrzTcs1Xx15hZOZkOlW2xY9MkJ-BUt0lw-De13pVs4LMw40LZR0pegjeDF-dFSTXfEqRvM2rnXZcn7WIh7g-qr3l4sRqI2f52KrLWJrCmNp1y4X3uFf1G_VIVgQl5GopJSXoooJY6HyZ_tweCxB-Uhyx0ItutGmQVPIZsuMdUJS6xVFdMkPWOQgDa_APUAtFqwcdJya1eP-NKcXku2BrX77pI_low.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22926" target="_blank">📅 13:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22925">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moUtooTgecRiJfSZkBFiXpQEe9gpqP-n619GsI_RbrUGl4ZJuJ66PQ7uZMXBG5XALrjO7RelA1AIN4IDJbu3AKo6ijWnId5RA9o2Ns97yQKTny-huZMcZGf6hEgYg0W2J-lcAcj_vJHFI9wL-UEUdaB4JO5q32zAh4yxAIEuDJRPVETWBzQXZ1Y1ZhHzVUvM5kaWpG85VvO-PfiLJbR1xT8hyWkrW_jRsX1X4MmvsqhMOTGZJNEEaZlSTKzNuM3Wst1wNGg2DC8JhrD4_dyKkLnKOVMfv2p5_8Acxed2WUYd-Vd0FwWqWAGSQ5ruU1e4F0QRmNa_6NEglyAeH7uvhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی‌کنیم از این ویویو بسیار قدیمی امیر تتلو درباره استقلالی و پرسپولیسی‌بودنش در زمان‌های مختلف
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22925" target="_blank">📅 12:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22924">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYFOij0AgEd0DxBV4rQUdrdAcRzSvtLbM9gaFcBQMcJ5mbeFgMfpmKd0-tXrnARchmxvWoaFoga4dLvyXmELkuaTZBl7GlvhJmS6lhQE2wCvdyBuBtyA9bfBVNG5SIq65mObeqFZzuHR9WHQdob19IFGfdoznqRiKDEgADVb5Jc9q3RFRinpbkh6kYC0kfz0BrHwta2zhGbWKlGSEiwNYgVZsmk7HH5BrMJAltrndrg1vGhRHpGEebupPTkm2OnG2R51T1ZKdhhUYWMOT6I8MRt-F38oF0eqwBKbQzyKt1niIn8Yym4DP4xLcLUmWeszpyxQIdr5ue0SQOcb900LZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ هفت سال پیش در چنین روزی؛
ادن هازاد باعقدقراردادی به‌ارزش بیش از 100 میلیون یورو از چلسی به رئال مادرید پیوست. او در طول 4 فصل حضور در‌این‌تیم 76 بازی انجام داد و تنها تونست که 7 گل بثمربرسونه مابقیش مصدوم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22924" target="_blank">📅 12:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22923">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a056081.mp4?token=JvFX29dfyr3k6eZoNzbbizD2pHcgYcYd9ObKJf6fvHB13GErjG5qDn9Sqq4OuAI9uJUEA1Rbt--SICKN-knnrdtWwgMhDodGpR-vVqnwfZNdU876nZ0Tg_bOoCMa6IzIOH0i5HTbECln6_nEyxurW0S53VZAKg-6h-BCJWHeafM3Ep8rg_QnrPTznprIHv832X4H7hX-Gv_h0QgxMBHl6YUaKVhxGDcKdM-atWTG9U7kqRNrVAdBmlHVe34BDy1aiIB1rt-6khjRGSuES_fVgL36QMidInK9Kf9WdBrGuykFBRIT7JDoDnVAw4nkgR4QIxE6fFlOxW4JZJhbKHYHWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a056081.mp4?token=JvFX29dfyr3k6eZoNzbbizD2pHcgYcYd9ObKJf6fvHB13GErjG5qDn9Sqq4OuAI9uJUEA1Rbt--SICKN-knnrdtWwgMhDodGpR-vVqnwfZNdU876nZ0Tg_bOoCMa6IzIOH0i5HTbECln6_nEyxurW0S53VZAKg-6h-BCJWHeafM3Ep8rg_QnrPTznprIHv832X4H7hX-Gv_h0QgxMBHl6YUaKVhxGDcKdM-atWTG9U7kqRNrVAdBmlHVe34BDy1aiIB1rt-6khjRGSuES_fVgL36QMidInK9Kf9WdBrGuykFBRIT7JDoDnVAw4nkgR4QIxE6fFlOxW4JZJhbKHYHWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
وضعیت‌‌آکادمی‌های‌ژاپن؛
قشنگ‌ مشخصه دارند برنامه میریزن که یه روزی قهرمان جام‌جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22923" target="_blank">📅 12:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22922">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKnxU1o3xGCGkeus0PDmo-Vm-nH9h0ktOfQnd1Wu7ujFzwI1BtMayhq98EAeE382smq_RaiHXnlcyWjfmlX5dBhMT9cN19xhtzglL6ktj5tWc766Zczz846iRA3Gk1KiSd8zHap8qi3rEi05LzMuXnCRQzU_7AFVP_13CQgSQcFDiQzLZpUbmVAEVqBkXBCOLvZe-lJeWDeZ1kBSwPViW30E6qh2zgztLko054Voxliv3fxInDZm6cs6D99i04NpFvelBsB4oyyIoCJwTnXRgLVXyghaqSouGHIMDwwsRIb9UgAq-vkG7gcj2XKz_sYozNT5NzXrouLPWbr47pkwqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حدادی مدیر عامل باشگاه پرسپولیس هفته آینده جلسه‌ای با مدیربرنامه مارکو باکیچ برگزار خواهد کرد تا تکلیف نهایی موندن یا رفتن این ستاره مونته‌نگرویی مشخص‌شه. باکیچ علاقمند به موندنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22922" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22921">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=n3OgRashE32iQ5Kt0TzVA-6iyCFhjq-z0wbAAUPrgMJH8ID95-YevPfbS6UUmMzWsDc54Nwq6pK2REdzeAoClbEhp6S9JFvOMPoG5Qfw1j8vENjOENjU-d6fGDa8Fe1ns6dtp2m7rSDivnpJYBEY1z3SkMazkd4yB4s4V3rj8-aTVf1T0KS3tspyruSNAR9gQ8-ZAd0SHbhU8BDHxH_ktgNPxrDwMbN1kMZUGdvAX5XzJCF3ptqsH-OF7xUE6_PYdrtEmDTyp23rYzCOlUI0XjualbVtrmHrEPc2zUd9BNLN6lJR95_6olhd5_Evh2bYPOC09wwFaCaTM9ITNSt8NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=n3OgRashE32iQ5Kt0TzVA-6iyCFhjq-z0wbAAUPrgMJH8ID95-YevPfbS6UUmMzWsDc54Nwq6pK2REdzeAoClbEhp6S9JFvOMPoG5Qfw1j8vENjOENjU-d6fGDa8Fe1ns6dtp2m7rSDivnpJYBEY1z3SkMazkd4yB4s4V3rj8-aTVf1T0KS3tspyruSNAR9gQ8-ZAd0SHbhU8BDHxH_ktgNPxrDwMbN1kMZUGdvAX5XzJCF3ptqsH-OF7xUE6_PYdrtEmDTyp23rYzCOlUI0XjualbVtrmHrEPc2zUd9BNLN6lJR95_6olhd5_Evh2bYPOC09wwFaCaTM9ITNSt8NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیبروین یجوری به تیبو کورتوا پاس میده که انگار هنوز از دستش‌بابت دزدیدن دوست‌دخترش فشاریه و میخواد کاری کنه در تیم ملی سوتی بده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22921" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22920">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22920" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22919">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okeDmGPSsnfqlz1TZJHa7O4wjFo_t4dttwoBH1LsumkFzCKGiffhsB76nIyI-FrV57MfqyHkKegCYw9QmQORBlt-b-GzixJbRC_5PtkHVwOTWVaFnEjJMbDBS55UDD6FEsEBQuSIVfYZOaWPqu2MXvmzErCNQ-NtR0bQ2pzBM1gOkEdC7D2h5prblUJ6lh_KOr3S6sHdDX4zLVsiAHnbp4ddDZE7Yd3gTEK800xrsnpCDIImcU91pPZu3LQtg3VrT7WCqu-zFdrF4VEd5ix5IDlxPagQUUK-fjAl8G6npUCfUTBCgUQqYXP0tU3Hh4ka7-Q6NKEM4p4fluZkmtaPMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22919" target="_blank">📅 11:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22918">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t21qgX5LTokgLK3BRgE2cgPt70MYznGmEjk9d37uQ62KhmblNZmdbFyxdA5kyLhM0QFEFZAZqKdS8SMD7yduqxmhj-bvZH7nHvDTyUhtgNrNpi39TrUNhD9Lgg6-O1E6XeY3wN_-Xb2dIUByj045L5pvDt7FlOXqKP_0HrbpF_7Dm3T33bUD0KRuhe6vXLs3MwdPao98UwuaDHRpfAQvI0mUXRqDUS2OS1U2P443gMLrtEK176__cE6UHtLCc9k4hc8Y9GSg1Vbdh-nRq8JikDHQyhDjPlfBFsQymzUbkI4jOOEQucF_fVWH2unV98rIy8qS8cFVhL1SEpjmhNgYBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22918" target="_blank">📅 10:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22917">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=j_Gzgp3T-pK-Hd-aNx_gTryRYWXxA0k8sc50UjzXq8qsQjph0RrKwoSWigw0kQla3heN0Lh0VtjH90yK7XIpJBuNoaARjTIThT5fyU-iKSsjleSqh4TaTfe9TAFe0HdsRPy2w5xm9pttjsxC1tlTMrNELy1vTLu4gK_6MvKaM_IF7Mwao_hjFQAtdpeKTM1LPtJgAsHJ_SFxSKeNunr-YTBM8ETeCZTcoCzw_-0PcIWU6ebSEsqjm1vZQYBa-YGiv0kVE0h4l9YVFG0aZPRM4BEVRsCcE-e6Bt_W0Ez0k5ZIZxBbjebIa-l48JjLfIpodMVLTO8956oNVpPkb4itdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=j_Gzgp3T-pK-Hd-aNx_gTryRYWXxA0k8sc50UjzXq8qsQjph0RrKwoSWigw0kQla3heN0Lh0VtjH90yK7XIpJBuNoaARjTIThT5fyU-iKSsjleSqh4TaTfe9TAFe0HdsRPy2w5xm9pttjsxC1tlTMrNELy1vTLu4gK_6MvKaM_IF7Mwao_hjFQAtdpeKTM1LPtJgAsHJ_SFxSKeNunr-YTBM8ETeCZTcoCzw_-0PcIWU6ebSEsqjm1vZQYBa-YGiv0kVE0h4l9YVFG0aZPRM4BEVRsCcE-e6Bt_W0Ez0k5ZIZxBbjebIa-l48JjLfIpodMVLTO8956oNVpPkb4itdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایگزین تشویق ایسلندی رونمایی شد، تشویق وایکینگی هوادارای نروژ؛ تو جام‌جهانی اینکارو بکنن ارلینگ هالند جوگیر میشه به هر تیم 5 6 گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22917" target="_blank">📅 09:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22916">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0rBoKmDsahUAsx6lmB7bdQCob-TLx_eFd7mgTDlgw2niOHugjpEy9Q9wYsZ8AHKMkW3ogL-umi9C5ETLhGnfWBRG-r7vLRkz0vrgoUlSEQpfZiHvzSo_5i9yp0JyXF4RHIgoTHFCrxmdLvW5rgmR8Z5EXFmLrZFr0GJHXG1CMPAZhqDmc8tEErKg5CHlbqD61FFUZzBvzB2ik4m2v9ltCzaSas-Cp5scyvpEOtYBQEpbrNzDW4HdtCMJ_nHmp7cF3q9mbUqYS_xiBGS51hgXHZPnwRN6q3xEkn---LtTtp20bIlqcNB6BUudYePCyFv0rXE5k0h5oD8GIeNe_1zPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصاحبه تاریخیی کاکا:
برام مهم نیست که بچه‌ هام بدونن یه زمانی بهترین بازیکن دنیا بودم؛ فقط می‌خوام منو به‌عنوان بهترین پدر دنیا بشناسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22916" target="_blank">📅 09:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22914">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oa9a77bO1fyHM2Wr2ffCNBsImgBqUQsW4PqpuQrTQDV4rJCIyzfsF3FunUW9XLJ4DzbeoOea0ZUuVSp7i3grdp5Q5K9ILdfvb-UEtLCADVkDyBB2HVHOGMBBG8ev99etVXrSnO8s5rYwQ0aAmrIQzTG-rX_7Ls6t4aHym46eTHWMQUsbJdeMW9ueaQp3l1TU9L_XEA7639qWb0GlOeqIxKWCiCIbOlCmcnAUxSKZFUB5bmz9gI4R_qGdoXHOvnNPlmdLqkWFH5RCflKMQyAPFaX0nuhdezp6BvSVlklDxDmobK1iyK2aGqvOw1ifJ5UpfcKLkNAK0ONHDiT1sunoLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
تقابل شاگردان کارلتو با مصری‌ها و جدال یاران مسی برابر هندوراس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22914" target="_blank">📅 01:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22913">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Js8sL91lmRY057269qdO1punBCVaZHzViD3qLADrjrNjLLHkygsGGMxkCcgYINOlnxLTS4vGpBiZ4B73jaSWtnrNeWCnqxrbYjQKNJySuyW3FL5JK2OYOeLpNsVprj5YNekb2YYji5P2oRIKcwJdgHaAZv8vHLvRqTvv-w_d249UpSsHV5x1lSV6RNga-8X4aYxiyiBRLHBUxOvNiMt0ChcTy09Nc3HuZOKUSoT7aa4InYA8TF-6Utzz3nv4DQAvghUG0R59tA16pRqVRi5yJCrRUyriXn_QY6w3DZnpooc2k9KPr4ORNJ_GunLkAVju46Mykrf6VvNgjyxuQKqp6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از بردپرگل بلژیکی‌ها مقابل تونس تا برتری تیم ملی پرتغال برابر شیلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22913" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22912">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvLLkO536MxvJoQ7KU1-KR4WS0P02LRidK6-ZYsBtsgBCJhqzJftDuuasfmZFnYate8GFC39tMDkOkTe60w7SwT0iCZvgUizLVue9KWqMKvUy391C3xyLD-9mTqrZeVBYAU6PU_XhrlKbY5aIwTY4X9koGNvWketwRmYd6Dy_2WL9UH1mnmgrYQS6gWkl0ptu8KOrlnGgR1Hqh4PxDinbXnRFg9F3pXM2_7_B6xV-ur_9d748Bn7me6r0JoKr9Wsv043HX8wcztNsNtESJil_ZM7yT1WKRpqfIbr0-mVp9aP43Zser5cAtAQOE7IZyfYpt_CCB0RTleT9cSHwP5Xnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/22912" target="_blank">📅 00:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22911">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=JUTHVb_ykci8As9Jy1jtEv362kLt0oZAqnRroOnh4nCsiJVojivA8RzJCEmcNhrYv1rSe-Yd32t7wanwL3OpQ4NWMMWDGQindmFiy-8kEz7TuYu7ngDtFjRxUaEQpqYGQU7doxd3rgFeJMhJMfSt364-ea7mQJJAz90n-njeenzZcB4iNDb85cvk4NxOk841eltzmX-NAebGIncZ9YqRPgUpctFca6P8SBUTCmDBokkzm8mXvLy-xixx6h1-wulGhQuq3UhYEwEx2ZlVtQv6ccoy6-nGKTfGavHiJrnHcoIvGgqJPFJS5kV5eqrZaPLcQTw91QiRjQ4TcOE22Co3PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=JUTHVb_ykci8As9Jy1jtEv362kLt0oZAqnRroOnh4nCsiJVojivA8RzJCEmcNhrYv1rSe-Yd32t7wanwL3OpQ4NWMMWDGQindmFiy-8kEz7TuYu7ngDtFjRxUaEQpqYGQU7doxd3rgFeJMhJMfSt364-ea7mQJJAz90n-njeenzZcB4iNDb85cvk4NxOk841eltzmX-NAebGIncZ9YqRPgUpctFca6P8SBUTCmDBokkzm8mXvLy-xixx6h1-wulGhQuq3UhYEwEx2ZlVtQv6ccoy6-nGKTfGavHiJrnHcoIvGgqJPFJS5kV5eqrZaPLcQTw91QiRjQ4TcOE22Co3PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصدومیت شدید مهاجم صنعت نفت؛ ویدیویی که روزتونو میسازه؛ فقط کامنت‌ها رو بخونید
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/22911" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22910">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=gblvwv9HwOGd6KliPqUoUvwu-vo4hOE-hbYkhYB_ijTLYJd_LO2I-2flsYWMRIfnV7hSPjRBWWl56kE23b6J3WTDUb8DF0PyRdtTrPCujFaYixEyqg2sumetOLl380ozNotjBGxClkuqizLbW06IuTO7ayBIoqOJ1Ti5VncXETwtgBImAD_7klPFL2FHVxG-gMjcm_VfDCmEGjRHLt_mW3ObWtrdOZT7r3DD1rQSFjlgjNgU77gHn8LMA2TV2a29PTHn_bO4J0ljxW4NwQNn1ogGSnJF4XSastolLd9HQwdHdeXvcFa4MWzdTglvM8FhzxxHPKh9pFlDg9I56I2CnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=gblvwv9HwOGd6KliPqUoUvwu-vo4hOE-hbYkhYB_ijTLYJd_LO2I-2flsYWMRIfnV7hSPjRBWWl56kE23b6J3WTDUb8DF0PyRdtTrPCujFaYixEyqg2sumetOLl380ozNotjBGxClkuqizLbW06IuTO7ayBIoqOJ1Ti5VncXETwtgBImAD_7klPFL2FHVxG-gMjcm_VfDCmEGjRHLt_mW3ObWtrdOZT7r3DD1rQSFjlgjNgU77gHn8LMA2TV2a29PTHn_bO4J0ljxW4NwQNn1ogGSnJF4XSastolLd9HQwdHdeXvcFa4MWzdTglvM8FhzxxHPKh9pFlDg9I56I2CnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
امباپه27سالش‌شده؛هالند 25، اولیسه امسال وارد 25 سالگی میشه. اینم لیونل مسیه در 25 سالگی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22910" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22907">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=G1z5HtUCfaaVpq7iZjyZSaAaJ7T32wkCMTVblyfebpZqMPyXACqtH22DrddgGiTfatPlx35umQhNaK25D5Am5U7wNtqSkZTQ8yUZM0D4Ehw2lf_vIkpLpNESGLPRKSJ17-_W2WJiOG745b667vQNgFcZSUKfhKZjD-fiCP_8N9bQ4P2ZsdTBhkBbfsTYv1t1PxUGFqBs8Rh8YNDQV04_y4sjLRFpEUDTNrOck-qpCGlwLdaqL67vNKXX-mNF-GJM9ToWVfOf2_3DzYIDbnbtQgjAwX9rRG269C9Z0pe7Vczd41E_KUzK3qvnHSY8UnobM5BQc_cKHnYdSNaZogEZeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=G1z5HtUCfaaVpq7iZjyZSaAaJ7T32wkCMTVblyfebpZqMPyXACqtH22DrddgGiTfatPlx35umQhNaK25D5Am5U7wNtqSkZTQ8yUZM0D4Ehw2lf_vIkpLpNESGLPRKSJ17-_W2WJiOG745b667vQNgFcZSUKfhKZjD-fiCP_8N9bQ4P2ZsdTBhkBbfsTYv1t1PxUGFqBs8Rh8YNDQV04_y4sjLRFpEUDTNrOck-qpCGlwLdaqL67vNKXX-mNF-GJM9ToWVfOf2_3DzYIDbnbtQgjAwX9rRG269C9Z0pe7Vczd41E_KUzK3qvnHSY8UnobM5BQc_cKHnYdSNaZogEZeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی‌داماد مجلس خیلی فوتبالیه، کریس رونالدو فن هست و به‌هیچ‌وجه هم اضطراب اجتماعی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22907" target="_blank">📅 00:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22906">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=NhIqeLIyaAUVd_Mm_ELaMNX9VlWu4B7_sGWtI1MoFs3V23IDt7IS_nei1vABNsqMUuMgnkuzNNNqWofqtqnst4dXbqLJLw5cuaFn_nCcAZjJOLHRYbIpi2c_cekPJ6Tdh1SeWKaPz8d5PBO4LO_IO3FtUMm_7MplYrhrUOvRckXV0-3IHGLB187gRTRWHG7lEioJ_2EGk_w7ff7nI6bypgN4gjZzXT6IwgEgMvg2PwEiS0i6HM8pBANeTqlPk4TsRZddLGDkuJO4QKdZcppay4_KMHIR91_w5mU29d-nrntId4sWKDIrOqMLdscrcNSFezyq64fVFE2584hhxZynRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=NhIqeLIyaAUVd_Mm_ELaMNX9VlWu4B7_sGWtI1MoFs3V23IDt7IS_nei1vABNsqMUuMgnkuzNNNqWofqtqnst4dXbqLJLw5cuaFn_nCcAZjJOLHRYbIpi2c_cekPJ6Tdh1SeWKaPz8d5PBO4LO_IO3FtUMm_7MplYrhrUOvRckXV0-3IHGLB187gRTRWHG7lEioJ_2EGk_w7ff7nI6bypgN4gjZzXT6IwgEgMvg2PwEiS0i6HM8pBANeTqlPk4TsRZddLGDkuJO4QKdZcppay4_KMHIR91_w5mU29d-nrntId4sWKDIrOqMLdscrcNSFezyq64fVFE2584hhxZynRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22906" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22905">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ks9T_UtmMUE0zMHumTXbt6yqiDNRDITrkASy4yOukTpYPnbcu9_684bEhsrazSz-ifukxEutaLmFbnu9fOM-xhzHB8N7lztCnX4ta8pLdybPUqds6W7PStJExmFmBCy6mh-uekiciIi8JDZpI_5szWVH-3TiSyh4oQRicAjjT85ypdt_CFghunlMjXMqR0zLd6svRvo_PJSjh48dj3O8XallkzbtUpbrsbSp-ZVt7D7WVshDIiRMuPvIarU-0D7SGsxvw5n2rnDekKsaG5-cRqIqtDv4B9udwynfALBJk4P-51oxgUU00BubHfp7MJbNAdJHocge84xvC91J1b8OiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
#تکمیلی؛خوزه‌فلیکس دیاز: مایکل اولیسه از طریق‌نماینده‌اش‌به‌مدیران بایرن مونیخ اعلام کرده که بعداز جام جهانی 2026 تمایلی به ماندن در آلیانز آرنا نداره و قصد داره راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22905" target="_blank">📅 23:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22904">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7O4ED3dK706BpzIKC5oRiik3YNibmNFsiqwCTfpfm5z1fuRmcLhdBdLHBD9cxlzgwqHm-mOU2X8vHL4ZZACgLjbLxbzu3e8_dSGYlf2NWZIDxP3xALUWuJ7picSkqDaFAYAEXtYTyhxSkEJFGUFB254lx0OpPXgYlkzly7xfIS2cV2IIpPntYSFnZsO36F2-pVXG8JbPu6fbo_vrtrrqDhODVPvK7V_z9iL2dUhnCYSULGYYdWUoGZHSsGsUISuw_F_D4_d93js7WYozU6375ZXTL15mDxpbVMxoS4QW2o1VW_xeLISisiwT1KQkCEckducJYIPj_nRNuC7Cxt0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق گفته رسانه ها؛ یوتیوب بزودی طی روزهای آینده بطورکامل رفع فیلتر خواهد شد و همین الانشم روبعضی اپراتورها مثل مخابرات رفع فیلتر شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22904" target="_blank">📅 22:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22903">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LD1YWFb0h8WiFGUeh6X6-IubC4iGldYQjkljk8zkXZeca0qcG4EXMQ9AeBh-5g1FFacG65CKa4Rfu_P98zncdDWASdl3vYPBZ7lfKCejXG7grNss43hWBU5BCSotG8t_o3p41pE-SnrFYpVdBgr9OTHVxShbDZuHpcEt-Xa323AjRYiLBFhQbrqBVs3M6ME7tpcXH-Ej562w698TxmbCuoqq__hcK94ZU4eGE4KEkk73m49XGyhcZxPMo0qXvTg4kQQ9mZWraN7WALbhPNOGKzerXSdzuGrqP-t6xyw_H15T1mRy56o1VEXRt9nsRtXO9Kt7SP5ZPM6AGWTv7OTqEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌اخباردریافتی‌رسانه پرشیانا
؛ ریکاردو آلوز ستاره پرتغالی سپاهان که با شروع فصل جدید چهار ماه از همراهی طلایی پوشان محروم خواهد بود به مدیران این باشگاه اعلام کرده درصورتی که محرومیت او لغو نشود یا به حالت تعلیقی در نیاید قید حضور در فوتبال ایران رو خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22903" target="_blank">📅 22:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22902">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4tVPzemnwsBZpDZQ_NjtPg0g-rLY50IkEbE947dBQGhzuGxIrmcqOFCV2uCGKR5L1kMIHD-Zlpjq4QOcbYUrm8muWAXRL5v3asLaOYvxOCZjyPEj37FjXnS7sHIderHOdflx-SwQjaZsuCmrT_ySaFnDd3EYpPBSHn59_M0A31x5vQkamdrl0JhjTEzeb_As4F7T5u4CoPvvW6sWT62VRZSo9ln9iRVGQuT_CCGO4pe_ZawihCKcP-OmsEClcbfIWvBFeT2IBu3F0EQFIu82C1pjA5XthkeGzl1ND4k1NAeeQvOtB-eiY5EXUVlkcFIlAcfWfIGx9NV_5Sa0cxnCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22902" target="_blank">📅 21:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22900">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ef07jZVB_3gYK6K9_RxJPCT7yJKgRGK-mCh_kmFyEt5nyeH65Wr6KqDBbBzv6R5pDA8go2nRwpOR_qNOoLd37rfxqnzVD4QebF7W8Ot6WOSRF3kHKKO6OLXJ5tNMuXDV_zBYBdtIKKZndpmBprQoinVla5CVQYigv_GpeRWq622Vk1FEmBUR0TUwSARbWJjQ62dot7TGBEzju9GY1zNH779GXyHJkbel3LnlkxhinW_5rgXXDgGyFzicwHkOI_mIFcqFmhFqjz4uqRr9nOzH5W0K7u7Lcx2NtORggPckfnvhxyrfuAg5_MBlnr07x8uZE7B3q_uuQbMCC8x8mBIdFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E2g_rBT9RoZnPZspq0ugEGfKIVbL3AtjiWlaLXmfuP95ier4bcoY87u5vDi3JWHqE3uDlr-7c3Rqk2WMTARCedZJzkBW1lBE695Rqc2FpsmnBAvSPGuaUeTtZoGHinsXk7FWu1DpZebD_UXn5abhSY6R_eV1N3U_0Tzv3IcPWdQRMaCiRBWWUGRuz_UlCANdQq1yuMdYeHIWVO9qk_WmMeSqi9U7RaLo2Uy95OOd73KubuH9jRUlmrz_9QYy6jCCjgy1NBzefGVlGgORIt9AehHSOH3FddhnwE3Cz9T46XAcxtFexeeK24lfNF2n-49jekVBS1NDBhJRHWNGcSj13w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار
؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.
مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی نسبتا جالبی را پیش‌ بینی کرده: تیم ملی برزیل در مرحله یک‌شانزدهم نهایی توسط ژاپن حذف میشه، آرژانتین تنها نماینده آمریکای جنوبی در ¼ نهایی خواهد بود و در آن مرحله مقابل پرتغال‌میخوره و در نهایت‌ فینال بین هلند - پرتغال برگزار شده و تیم ملی هلند نیز قهرمان می‌شود. البته این فقط یک پیش‌بینی آماریه و تضمینی برای رخ دادن قطعی آن وجود ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22900" target="_blank">📅 21:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22899">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmBQNESvY4Mcot7HHesPCXw9NRBQYATHh8eu6bG8_k5S21n6vKTxmMoAfpSzeW_OZVJ2vVzQFZE1MNWK3Z_VkZgjAoizeOdU-523MtBl40ZWWAugngjalZGu5YqAhbuuTsgty3xbUWxpMDP1Ntku4yo52NmzobYMaD7T1Bb79vYxyjZcMwIcYXHHV1PmSgxjvjbrNHzcHIpJV8fa9IufsV8-njx1MQVyikJ0A7FCBZlUeoJLNtul78ipqKKEVU_b6eYGsH4FF3Ct2hwbwT5Kc2y9Mn-LhdW8ewjt8LrM0YiuCP6KLfRBPU-LHt_P9sfHhQO2LJ7Us7WO10AuWT-9-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22899" target="_blank">📅 21:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22898">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClTE2e1KqnLDmpBYP8yZibMGbt947g8FCF23cyXVnEWIgCFvz-Ih409rRk0XKeQCyBTFP3PAnxk-ybj6D_MievFjECOySSwA75oTz0WslTKcOqqdu2beMX0XLsDZ1vTZ1fU3Ztf2wtJX9BnuKFRgvB-2B0qpc4rteM1Tu6H96ibf-9USbig6b2AIge5sOPQjOGqzrGarOXfJJx_165ed09UxMx1lmMfz4hu24TuiXJvrDJke50TX1ubWsKQ_0es89NhinBGf0XKzukfIMkHnRHYycJ4KvcyWfIFez5Pu2ABFod4qZeNw9uUpIIZugVgLXCAs6wdKq2oChwBDqFSNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال با فروش جوئل کوجو به تیم نفتچی ازبکستان‌موافقت‌کرده و بزودی این انتقال‌ صورت میگیره و کوجو رسما از استقلال‌جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22898" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22897">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73008adba.mp4?token=q9wS23cKCkFYS3eS9ZZl7yOXdcYFaSsLd1jr8x9bIFqAvsbtE0vqrz3ja85FtbMcBMQE5k34PAdzVQQZWQirF8eOY2ddWHNrZ8kxH60DkMnu9yi0lQNxncdxd2Ywr97Ff34CCqWZpJVXVHqLGIrfoVUgYHjBMwZDhV0rrzyV59gxCRbrCthLu6UaoPisEjLxiW574uI_NwLRz40LzzOzT9ZyyiHwKKlzwDp-HVSP8SpO9jCKjvCbE3WnGCiOHrU17Ip_9pwGM1R_LNXDYSghc2j3WXmh10Jo01ThZc-eUR2f7F5tN5YjT_N4_4_MHKF0qhkmJFdgnpkBihxPB9qEqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73008adba.mp4?token=q9wS23cKCkFYS3eS9ZZl7yOXdcYFaSsLd1jr8x9bIFqAvsbtE0vqrz3ja85FtbMcBMQE5k34PAdzVQQZWQirF8eOY2ddWHNrZ8kxH60DkMnu9yi0lQNxncdxd2Ywr97Ff34CCqWZpJVXVHqLGIrfoVUgYHjBMwZDhV0rrzyV59gxCRbrCthLu6UaoPisEjLxiW574uI_NwLRz40LzzOzT9ZyyiHwKKlzwDp-HVSP8SpO9jCKjvCbE3WnGCiOHrU17Ip_9pwGM1R_LNXDYSghc2j3WXmh10Jo01ThZc-eUR2f7F5tN5YjT_N4_4_MHKF0qhkmJFdgnpkBihxPB9qEqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیکه‌مسی شخصیت‌منفی بود؛
آرژانتین ـ هلند؛ یک چهارم نهایی‌جام‌جهانی 2022. درگیری بین بازیکنا به حدی زیاد بود که به نیمکت دو تیم کشیده شده بود و این موضوع باعث‌شد مسی به قدری عصبی‌شه که یه نسخه از خودشو نشون بده که کسی تاحالا ندیده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22897" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22895">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpUW7DD3vZGnZu_js33sCaGrA5f2bXjog6KpzGVuEjFDdEXrPoLLpaLGjXSCprhY3OlZ0Yt5gnxwEDZm1yXpV0pI8n2_5fBog0FmNhUEi1coY7s_vlvwrH5b7_gcpod6tyUXzggI5wDlnc-W9wtQx9YI71aXYhRPQeyYP9tVbTcvkCl8RuysQdxDnrwo1ZSO5uXCoU4t2P-ACp11UE8d8sN_kbdt0Pt1LOpsNaheeHkHUdapQAnpOjsBuILZRLgxtVC1sQXd8z3ikeTZ_1QVMaly-bjFtLhxzHCDKw2W71mGYQghFUp6lmD1Jk4dl0oEhqdmAXkUyxbT1wd-Dcxofg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22895" target="_blank">📅 20:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22894">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=d-33DGWAcZK3WaKi5dlotvKjW_GgVz1DvvJzWwONssLeepJwiL9xxzhALp-Zb6i-cDUdOiel3Ckaoc89Q0OeX_5J0wEyFQgx3Bae4yVsFvPB0xjqu9QFKuv7Dj_MqqzsjM8ZhgKIWNDiwUJisRuot6DP3Ni-T15yC65bkj_6r55xAjUqIMKODs1-b7lGLPhV3GqRw7N79YtoXZ81M9Yv7MqqHo698kcolgGDivFmj9TmZd8D4rSbauwAGSolVkvo4joSuiSCnbp1rx4H0dmHCARu5N4yC_Ys2ETPKoq28zTRX7qqxR21IBacC2zodWsncnC2MHPYR2gykG20OfsTMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=d-33DGWAcZK3WaKi5dlotvKjW_GgVz1DvvJzWwONssLeepJwiL9xxzhALp-Zb6i-cDUdOiel3Ckaoc89Q0OeX_5J0wEyFQgx3Bae4yVsFvPB0xjqu9QFKuv7Dj_MqqzsjM8ZhgKIWNDiwUJisRuot6DP3Ni-T15yC65bkj_6r55xAjUqIMKODs1-b7lGLPhV3GqRw7N79YtoXZ81M9Yv7MqqHo698kcolgGDivFmj9TmZd8D4rSbauwAGSolVkvo4joSuiSCnbp1rx4H0dmHCARu5N4yC_Ys2ETPKoq28zTRX7qqxR21IBacC2zodWsncnC2MHPYR2gykG20OfsTMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇨🇴
وقتی بازی‌های باشگاهی تموم شده و از بازی در کنار هری کین میرسی به بازی در کنار این:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22894" target="_blank">📅 20:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22893">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qC6NzVaO0GIX7-Jm02nUDVB0NrxuKPCvh8hYXr0oprAd6d9eGDTQ9xRc-Od436McrqVSQa_IGJnguBxJ8XYUBjsfmRnCqLvkfa8asLHCvek-BbkRYLv6Bg9ABtU3E-EY8VE36LxGjJMgrw4IhAYKAV1ezofsv03-9zkya2AYBDLTRexZjboPXto5ZfJuC67SlN8UU6NxLcImMid6nfaD-fpaeEJbs45W1inV93lDOJ3tbrkBA3MUiWr1wfVIxsmeL7ZteKAivEE2KQPJwdccg0KNf9W8KCYfQsmfITXV8uITPSI6J1R0hkjtu-pzpE4rkJgr-MMEDX2xZLIvEsShoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22893" target="_blank">📅 19:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22892">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uceEOlgQ5vWtNslPadaQnCGSg-BphTjyX_vfbply1M9VQ7Qw5h7wM3EdK6UXE4Xqh_U5V_S4_ISEQHQ6-9pXjeftn35Ej0TV3dXcAd90nleipMNujRlrBDPXhNnEiXNrlD1RnjBZZp7x7r8ccbUVFN8ASfvX1rpGHwOw0MnRp9DquZ8wgUNkKP9-ldp7DjO_sPx9546Y60b8nyYMFXTBPlpFieg9eGn6Ub7mmxqAsSVkKmovkUX3sgnmsKYZezOuhWqdF6UNlsuy1MFV_1i8QgUwrtT71mW3OhJJMzLppnTNEH2J8a2D_lmc_3wf95IbdAAAPbikAE5mXCWkHLh67A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22892" target="_blank">📅 19:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22891">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=OAcqXnbRf19y6Ye7ClRUcPO8m_FoRwprsUibiQ8nRjDzYzYmORGnj8eMts1JTJjJ-X75ysHCkMAE375FcBDuoZh8MQQ7Ulo9UQ7QZtA-_xTcTfe86VQVV8nxf-aSlI7hKWe9Kkl0Z6nCUeh204P0K95EyZrRRBlURiR3cnhqbZjpGLTDbVIpR1R9VKuwOZ_FwbLbwVJZhs3JEBY4NePWexDJ0PIwjw4RkJE1TBOHixeLxH28izI689uVhZ6rR2GqisdIgoe-jL5lX-DpO6lPc8_B2z844aDZYv-o6KILWzawjk7Eyqe1xxdoIEJQi4ykewWLo3wZvYoYhuNGUjNsWIWTQtHInXShnUxCpCrUNcbsBrKbOAQMcxdN6ndj20pMM-3EV-CLRtIiHIZWbsVkaYyIGikIbaNnkdy3vMPgoNCq-j03mbPTfkv8RxouHWESbEYtXJ6_5-Ihb4lMw-Vlzt3Fc_62juf7IkzrFWtPnHZ70dkCLZVddO-FTd4WR9G1PQIAtorMUPR2RDETLetV43dNmTHlAwFWmTrZV_OpA4OiPeHMgeJcs5BleGNlAaHBP32sXyp2BBzszdANyIRLGQrW0tX0fA1yy5BFyCNSaX-0kFyCAT0Iv8HU_i12BOdQIZpkFKvsq4Gf_lGFzo6JjlcN5X_AeB8VoH8lzZ-m31c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=OAcqXnbRf19y6Ye7ClRUcPO8m_FoRwprsUibiQ8nRjDzYzYmORGnj8eMts1JTJjJ-X75ysHCkMAE375FcBDuoZh8MQQ7Ulo9UQ7QZtA-_xTcTfe86VQVV8nxf-aSlI7hKWe9Kkl0Z6nCUeh204P0K95EyZrRRBlURiR3cnhqbZjpGLTDbVIpR1R9VKuwOZ_FwbLbwVJZhs3JEBY4NePWexDJ0PIwjw4RkJE1TBOHixeLxH28izI689uVhZ6rR2GqisdIgoe-jL5lX-DpO6lPc8_B2z844aDZYv-o6KILWzawjk7Eyqe1xxdoIEJQi4ykewWLo3wZvYoYhuNGUjNsWIWTQtHInXShnUxCpCrUNcbsBrKbOAQMcxdN6ndj20pMM-3EV-CLRtIiHIZWbsVkaYyIGikIbaNnkdy3vMPgoNCq-j03mbPTfkv8RxouHWESbEYtXJ6_5-Ihb4lMw-Vlzt3Fc_62juf7IkzrFWtPnHZ70dkCLZVddO-FTd4WR9G1PQIAtorMUPR2RDETLetV43dNmTHlAwFWmTrZV_OpA4OiPeHMgeJcs5BleGNlAaHBP32sXyp2BBzszdANyIRLGQrW0tX0fA1yy5BFyCNSaX-0kFyCAT0Iv8HU_i12BOdQIZpkFKvsq4Gf_lGFzo6JjlcN5X_AeB8VoH8lzZ-m31c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شنیده‌های‌پرشیانا
؛ایجنت‌مطرح فوتبال ایران که ارتباط‌خوبی باستاره‌های‌خارجی‌داره؛ بار دیگر ارتباط خود را با خامس رودریگز ستاره 34 ساله سابق رئال مادرید و بایرن مونیخ برقرار کرده تا درصورت تمایل او رو برای فصل آینده به لیگ برتر ایران بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22891" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22890">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=C0_zsweBAmSk2iKZvE3zviu9vXh9VBeHRCtpUsy1uNzehf8KzWa1f0A7_WwxZF5h7rxa6YJXjIX3Ua0MzqDK98CSTh_3u0YqBGIC_5dlhxPo1lctR4gAkaB8Pu2GVxcOd2mZ-85kuUD9lKYYpcT7Te1yp307fJx664j7ZGkXxupSeqaNIcYihCQKMQvDnEYxwVT-6BN5jyHWS1cDLilyMSw5mY6IZ_UunU6Ij9tO-l9i34QZSUwW8pIpOJDOwguXdkNJObfErkBXTkVL7tlDR0atXWwuHkWMrAaOIA35mey_N8XzEMp7y0slhVZ7hQdBUOZTIp3tPN6gT7pkcVft1Rbjys5n6wlx1zc3GEwP3cNL7XicZ3kzvgUJ-6NXt4q-87ea_Gs-J-2Ky2xkOwMYk4Uxlv-ope3d6vFh_L6KrNXMquC8JW1UKE0ZNTUWohwZyXvVWdjBbR5qNpXH8ZAo3kHZIfx_8l46k1fYECw9xbHIKWmZ13ZaJlyG30aXTUWCOEFLjgc3fRSqGfSe53j93PM_KWpUIFG74fJTg0n3U5QV7ai41X8ACnz4371rDkvMQaR4aImWxZyRJP-RFdNam3e_Ps-_vaP3V61WfxLvKu34i9yPLd4fnAB-ZWZyIXEMYIEH7MqL8aJvZFsMstpqDq5iEcXq5qkUzvbpZtKgmz8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=C0_zsweBAmSk2iKZvE3zviu9vXh9VBeHRCtpUsy1uNzehf8KzWa1f0A7_WwxZF5h7rxa6YJXjIX3Ua0MzqDK98CSTh_3u0YqBGIC_5dlhxPo1lctR4gAkaB8Pu2GVxcOd2mZ-85kuUD9lKYYpcT7Te1yp307fJx664j7ZGkXxupSeqaNIcYihCQKMQvDnEYxwVT-6BN5jyHWS1cDLilyMSw5mY6IZ_UunU6Ij9tO-l9i34QZSUwW8pIpOJDOwguXdkNJObfErkBXTkVL7tlDR0atXWwuHkWMrAaOIA35mey_N8XzEMp7y0slhVZ7hQdBUOZTIp3tPN6gT7pkcVft1Rbjys5n6wlx1zc3GEwP3cNL7XicZ3kzvgUJ-6NXt4q-87ea_Gs-J-2Ky2xkOwMYk4Uxlv-ope3d6vFh_L6KrNXMquC8JW1UKE0ZNTUWohwZyXvVWdjBbR5qNpXH8ZAo3kHZIfx_8l46k1fYECw9xbHIKWmZ13ZaJlyG30aXTUWCOEFLjgc3fRSqGfSe53j93PM_KWpUIFG74fJTg0n3U5QV7ai41X8ACnz4371rDkvMQaR4aImWxZyRJP-RFdNam3e_Ps-_vaP3V61WfxLvKu34i9yPLd4fnAB-ZWZyIXEMYIEH7MqL8aJvZFsMstpqDq5iEcXq5qkUzvbpZtKgmz8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
5 سوپرگل دیدنی‌از روی ضربات ایستگاهی؛
از بین این پنج تا کدومش رو بیشتر دوس داشتی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22890" target="_blank">📅 18:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22889">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKlARYFDnDnrEClliO-HNdrHi4cyFboozsrFcOVIqpnLloIIuqOX0mS2AHBtMEm-5L_GkZX4r9prz6IQG-mnXrcYyuxbxdFZXIhP0b_Rv16AZT_EgfWyJR0vWyXbHyf6MUZ16LANorNdrcAV-lgFn15zE-SsGoRy-2G1zWzMRV142YWzcsU59sWniq1_e9WPjvkYv2-99UFWI509XFX7VPA4ykI677wz-w8t0IohKE6bCFtgzuYh1cycT1rZOllmIybe226Qqi1sFUrrMxqlUlMOnLeDW1iEoWTqOrgEx57gSoT_SZuEzpbAqgvqwIdHS90bcgSibDMkkZjraqqlCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22889" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22888">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=tImBfuQ15B0BkJJTmWHgJmTokSlACxe-wupc1TPH1NwREpo92EpQGLPpZ7eupNaK9RjPG4zXcYoDbj7A_yBMX4vvncouqMqhDfjN8dCbzM5UqgxIJFfxA0G38Z6CrRBVAV9Buj0yiJcAKL035O5UlJog0e6-xGiayGNFmnIfRbH_ClWW0Nr7uA6_PNAKAAFGnlRceNccTKqQBWgyUDhAuSn4OqCl-s4KzF_5CfmyELOgc56LwHktfhcCDnjeLfRev_Yyq82OzorPovCPOM5IzW2doxaKCX4aT1e2qTzT9eLyKXmoBMglTMnaCC25Akz36-Li7ZNtpwYRfVUsR5EajShUiWazEglbm0m0BdAa2hn7b4uLkP9oDdhfF0WjYLMKw_9ad2W7pWZhVkI_9W4D1XNnwt2-aCA2kacXi9IEss4H1-F0X0M98jMCAyWZMxw-IvCIUdA0XdlPNHw8p__0Q8CtFT6II0kmU0PrK0U-9Apv__O_rtvWX92d3T-qfMG5wlgoj_LBm3AWozJY8iu8KLWtCXkAyw0_CWKAPbbcxWgbEvDIsMZW_OmFfmWgTzOHqC7-fcsxzwXh_uHnTxTgoZeEJEcIhNePh0XfjorzNGKx9cM0r0cp62eKzPjM7yJPDZ2T1R9nCrcS_8oO3DKdmqC6r5a6J5NoCLbXvBoQg8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=tImBfuQ15B0BkJJTmWHgJmTokSlACxe-wupc1TPH1NwREpo92EpQGLPpZ7eupNaK9RjPG4zXcYoDbj7A_yBMX4vvncouqMqhDfjN8dCbzM5UqgxIJFfxA0G38Z6CrRBVAV9Buj0yiJcAKL035O5UlJog0e6-xGiayGNFmnIfRbH_ClWW0Nr7uA6_PNAKAAFGnlRceNccTKqQBWgyUDhAuSn4OqCl-s4KzF_5CfmyELOgc56LwHktfhcCDnjeLfRev_Yyq82OzorPovCPOM5IzW2doxaKCX4aT1e2qTzT9eLyKXmoBMglTMnaCC25Akz36-Li7ZNtpwYRfVUsR5EajShUiWazEglbm0m0BdAa2hn7b4uLkP9oDdhfF0WjYLMKw_9ad2W7pWZhVkI_9W4D1XNnwt2-aCA2kacXi9IEss4H1-F0X0M98jMCAyWZMxw-IvCIUdA0XdlPNHw8p__0Q8CtFT6II0kmU0PrK0U-9Apv__O_rtvWX92d3T-qfMG5wlgoj_LBm3AWozJY8iu8KLWtCXkAyw0_CWKAPbbcxWgbEvDIsMZW_OmFfmWgTzOHqC7-fcsxzwXh_uHnTxTgoZeEJEcIhNePh0XfjorzNGKx9cM0r0cp62eKzPjM7yJPDZ2T1R9nCrcS_8oO3DKdmqC6r5a6J5NoCLbXvBoQg8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
انریکه بال؛
سبک بازی فوق‌العاده و تماشایی تیم پاری سن ژرمن که ۲ ساله هیچ رقیبی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22888" target="_blank">📅 18:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22887">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Stszw9QkggZBnsJadpdCH9CuSFwhedrXax2PrA5Eg9x4ws3n5KJ7NGiPmFwbbREJ7k9xcLbKV7sRFrFXA17mCyroUW3KNKBdtuEwKzL9UmbKGBTst93zu9PPaUazXe8ZFOOobO4kJqs-lfOPy9zlkxvrw0hzND5W9YyaGKH0PvNC0FtitDq73tCWowrbvYrtdZw4A8OITbUuKXYLdD5bbP3gAiil4C5V35VfHdAJZclLnmws3NQST2BmQ3emTjWhqE1BzUwEfvKmi4_wJ1R5I8KJUUG7Qs9L3XAA9T_2y36sdH9AiZbjcvv1642ibHXwl55VoCfawHGA0BfoF_uHsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌ بندی لیگ برتر بعد از سه هیچ شدن بازی گل گهر - چادرملو بسودشاگردان مهدی تارتار؛ پرسپولیسِ اوسمار ویرا برتبه پنجم راه پیدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22887" target="_blank">📅 16:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22886">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=PQ9RqhDuoOmuIDtm50tq7wBEzvQETQcPTXEiO63vZsmt5Zv8cdv6XXv3GyH0tOCf_kBUzyKT7AIKOE_qJBnV362ugY39k1sl3gQ64d6J6uuYVkFLG0ohQQkEUMqsixqpvWzhDlH6xvD1Dpy6Q_cbspu5oHIN0AIArXo_msuq3bgZN_ovjrPhbXsJKOYoEDJJbqScWzNCyZ_h9wcU2Q3AechMX73u_i7ZvE3kHUou4Cf9KVMJpB2DFRzHzRVToBiVU34bRpEpGmPxQzSXwn-Jllv9ZQd0mjCZ7o2408QgZLfzOu6slylob3Jsk3PNx7plE_hcnpUqKL-psK11mDQVEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=PQ9RqhDuoOmuIDtm50tq7wBEzvQETQcPTXEiO63vZsmt5Zv8cdv6XXv3GyH0tOCf_kBUzyKT7AIKOE_qJBnV362ugY39k1sl3gQ64d6J6uuYVkFLG0ohQQkEUMqsixqpvWzhDlH6xvD1Dpy6Q_cbspu5oHIN0AIArXo_msuq3bgZN_ovjrPhbXsJKOYoEDJJbqScWzNCyZ_h9wcU2Q3AechMX73u_i7ZvE3kHUou4Cf9KVMJpB2DFRzHzRVToBiVU34bRpEpGmPxQzSXwn-Jllv9ZQd0mjCZ7o2408QgZLfzOu6slylob3Jsk3PNx7plE_hcnpUqKL-psK11mDQVEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد‌هاوقتی‌میبازن
🆚
وقتی‌میبرن؛ لبخند برای پنهان کردن درد و اشک برای رها شدن از سال‌ها جنگیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22886" target="_blank">📅 16:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22884">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKVUxo25PumJaRX0rXcatHqRwZsoy4Ex8oQ0dyFHqaUqzamoweGjBOcTuPe0t17ezwE6hu7hCvs6kVvrh6uVyxuVdwsbrRCBKv90PgfKmKWA_eVtndumdrYEgF9-LaFme1hjI4RB6rEKoqynYbhDxH8DK8wXHisE9nb_0LQona5omKYQErAW9yEbiCli6NuTdR2NxfWZea4fIeV9NClQJB5jWYjsg4b0Dh9ssilgKlmJrCawkgJ60S7oPalNOBiGNcK6-3Y8X8DFnR49tprx2XJYL7y-HI6-tWx6x7_xG_03SES9XsJKSTu3siaksrZin9x8SFs_m2slCCOqvmWkDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XtRgtqsYKx_89h6D-7DRp5Mus2UPzmgcox3hzK3CLFaQiBsrtJB3EoWUZhGKOtLDYlCP--CHplJsBriQlmuQGKtjj3oKhGJA2aoYqpjBcyCeGpsLo4dEhbxIzO5oUzjaNbD4Z_aKxql1jL7ygUD5An6G8_S251HcpVnWulYBDkB0lGFaGcXjvYoG7lJPoAs3jKx_tZvwJM65I3Y7hqGZ6RepXI_un9R1fyxjGg-Ajfnomzwuk1zfLuva4wf2s4G4AgI2MPDaPtddmBjytbxHJxjF-ToRoNEZOSrtBa7AVcYFY6CV7c3s5CTeQzVD_DIMVeWQDzppvET_5UKNbx9SfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🟡
🔴
#نقل‌انتقالات
|شنیده‌ میشود آتوسا یوسفی خواهر آریا یوسفی ستاره‌بانوان سپاهان مدنظر تیم بانوان‌پرسپولیس قرارگرفته. آریا هم مدنظر تیم آقایون پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22884" target="_blank">📅 16:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22883">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QczNKapnyIaiZxAviLrSPkYLJ4WfXq_8iof5QC02kx62LCMsD06Yxs5RfZAmqJST0knRLJ2oCi8M0QDTwH91bT4ERwWAFXv7KMc4drNgHFA_jjIao6Q-mKPAUoEidjSTcE_fRvQct4_aB7btgdiq4Ow78ASqYEPBTZS2hvFHqiTV0A8z15GNENMIlI5ec2PDFY_7yNFED2DI9sluLjUt62PHRWedJ-eiBh0a57PRiAF8lvnm3uK3ddUa3CbIms7B9plhd2-Fw33NpHu37Gz85Z_0ta154aKp0sLqewmDMjIrMrPCK-8Kju-sOVbA0er5CTRnfZuzPTtW8WiksjbF7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#تکمیلی؛دولت‌آمریکا: به افرادی‌که حضورشون درجام جهانی ضروری‌بود ویزا دادیم. دلیلی نداره به تروریست های جمهوری اسلامی هم برای حضور در جام جهانی ویزا بدهیم. ما هرگز اجازه نخواهیم داد پای همچین افرادی به خاک آمریکا باز شود.
‼️
مهدی‌تاج:اصلا درخواست ویزا ندادم…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22883" target="_blank">📅 16:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22882">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dU2-olgJSin7ez5P-VBirRrXvjQog0LhSD4-ju0BzTqLyYI5DrO_NUYnl-hqfU6BG4EMs0ZVD1TlUeunQn3zfAmZpq2nczFOpwd3I-2G3bZpWHY9hBhIIT9lk6r9b2ct4UT-ONUquAenqvJmskeCUzHA2tNRwvy2Jv60Zpxb9eafO2otvv36wpEdMLS03GEFK1QL1BwpqYeC-lJjuyslE1gjYYqgu8oq-sf8rT1D-6c0GvB2jUOen_aTG6xyUtMenwNJjL1HkIW0uctv5Z8Qda_SnNSwTkyLjZYXlf_YnQFeB9uuKKnDtEeo0Gl4pF3LFUykvkjK7ffPvGdhZ8I21A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22882" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22881">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vda57GdktzqMAxHDdtPY98TOYvrNjMqZ74cLXT6dpyvgmUmGAV370mMgFWCg14PKM_0PaRvmb4WWvY_C1iH71Vr6vTA-lmSV5CCT103qfkf7GOQq0RlTDyePuAj5gbsNvKhpF8jcia73DNSn5lfow0azQY8krZOZno-EdW5mRhpbQOzRVawHoWFSfswWBzPKjqLMR-dHZ9MsXcCowD8hLpKi2yFuqA1r38QcW9COEyBe-YZrYzcUznsjXJp9afKA54EekjhM00vzg2mWzV0coK3viamX4hIndCTdKEspiGn07kCOBGxjsw7l0kXMmmTEcGTa7fM4h4COl_qMMQbf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22881" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22879">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S1Ugzju0luLXx-26jx4xjHLrkGnFMucF7nPpNVYG93lgVwxuXn4FRwVSCAi_q67XFy2ZCYA5BiCGCJ7t63if0vOYsaUlXkng0Kr66SZRS9Sy0wyUqqwbP37Wy9Tv2u6DEXNyQ6gb0u6wEuxciOGDcVBPX6iEqjeOkMzUse82xxXxzaVuHaYmc3f77dkyW5nVUedv-QQIkgDK9Ta1pn2jjv4raVngBi40LHdymCjtG4bXBNwXaaKj3L3hau8VQzItaWuCyiziT3H-j19Foe9RLdnQYwc-levRakp_IBtJIMwhM9KGA-f7YKundDuWoyY11ea6v_HSzqDH7cFCY8SkOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AjvpOCJey4YON5I-NOce5pD3OnbtHl8CWpxlgm01yDVrUcg50uOAKn50i-6IDIbM9HcwCskn420YSz0u6FegDbr4l85gT4769g2DSM2SD5cfqYGAM-NXHVx_mkuTQErXMQQanb86YmJsedDYMBCYzepYu-CzBbv2fJqBdXQ5v2LyDTaOgAqTd4NduKguB1BBbuYPR4XHQdw46bd5rzWeLdgAZg19P6U020XaVlv0cM02Kz32tUarcpCdr5ZlvT4iE1YCSw6BQ3Sq1aB3cTn38-qk5JZlDWJLRjLsFSRZG8FTFctVtzgMKW8-IdIwKtUVFuo_l1VD6yqhjEDXUJ4SIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
خط حمله هشت تیم مدعی اصلی قهرمانی در رقبت‌های جام جهانی 2026 آمریکا
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22879" target="_blank">📅 14:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22878">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfafMnFOGcBR8BpE9zsm6aHpoHqwaqXeXkBsfY8pw-c4XDu6dwSouJ4O-KjYDExLR2Wuko9IedbWbkj5Hz3hV4i1qk59VqR0yoAUp0aP5EOVEnikj3fO1F9aRvb9Z4aE1c2O4YGDQzOipf7WxBoXF2w8tObPZ9rSdPuzdugO3oRt0WS9AO8GGjRxsDlgMISukJWyGlYbNUctTRrsY_XI11OGZ9Mvsdk9oBTVl6OQtVWCs7Xzl94UVuLislofOdROWikPznezIr0D8S98WFExGZfpz-i7xpZTiWTZ8QP-ZnRYcXvqhdn2K3-YR4nx5K8MGrhDHsDEIn5Py4qO0UIf0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22878" target="_blank">📅 14:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22876">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUSWE8QshIqwYHDI_k67gADUrZnoKQIogDVsgz9Q_pACzixmG1iKVIZ09mWJFieRuC1jlsX7lnXO-wx8GRsYdgmL9LYcHEQywJYx43YijH9zLFvwGhEgGKIDZHQjiN3ebO7j1F06etpTr0Trhx7n2OSvNNd4pRTkcatQ-baudbLQK3FCE5ek-u8FcqLCut0lGKFd30Upyb0HOzvuLuiZ1q35wYpqKFjFAzf3u5Dfkcajvwmnh79LWzlG1-abUE1h7KbEgS18waUfv65mN6OIn8_2UftBek3oFw5zzZfzOk498KDbqz0eCnBxqZ1CizruLyTL0buj2590Hh_XxfFNfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال با مدیر برنامه‌های موسی جنپو برای فسخ توافقی‌ قرارداد این بازیکن‌به‌توافق کامل رسید‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22876" target="_blank">📅 13:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22875">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=ZVMLxeXDPNl6XYtk_ue28CgXT3KPWHQL184aSZg4e29J3gxLtfo7R8-WgpzCwNTPvUKMjU1eWo_I0hrZimjWA-FSptxXc1Q8Fr6AuaQEq3yPnRt59-0Wol1u0kemax3YJosqI1T70jGOLoz0Y2ojnfAiG9OO79OtQkHRU5gsF63MaU9NpgaxQ7Xeeu52UDtWlQX5Bid45eSZHa_Hws8i3bEZzMranXjagU2fAi-4u7GndIRpHIyX9CT1BBeX0Odq_ySYP54ol2BquQXch7Mp0AWb2ayyIFkMrNu9rg72Ei1QUrxFyznuAfiXm5LcgMipXAAA3G0Px-xTUx_EExRzcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=ZVMLxeXDPNl6XYtk_ue28CgXT3KPWHQL184aSZg4e29J3gxLtfo7R8-WgpzCwNTPvUKMjU1eWo_I0hrZimjWA-FSptxXc1Q8Fr6AuaQEq3yPnRt59-0Wol1u0kemax3YJosqI1T70jGOLoz0Y2ojnfAiG9OO79OtQkHRU5gsF63MaU9NpgaxQ7Xeeu52UDtWlQX5Bid45eSZHa_Hws8i3bEZzMranXjagU2fAi-4u7GndIRpHIyX9CT1BBeX0Odq_ySYP54ol2BquQXch7Mp0AWb2ayyIFkMrNu9rg72Ei1QUrxFyznuAfiXm5LcgMipXAAA3G0Px-xTUx_EExRzcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22875" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22874">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKR0nVn3hvoR-Gi5RvuoiT4GNh0cG4O5SZQnaLvMPMdyHKHPLZeFsDc2Wkd4WWzj50l54JqNTdXXarZATh24azd0bXZDOm1bpKnvOJSJUajodpg_J2bsqWielv-pr-6AiUvbzQK5IReowDzFEQtqVOGPoMcqxg9I0yaO3aGKphcqrJ-pL25mB7k0E1LtVdn5iopxL9TXEJu00c3sfZjW7B_Nqdy_3RdFQ2psX3rsGRmVl23XZa7En1LtHIGISg-_RmY5rFVeTR8eN22QHuGR71Z8dxpfRUTZnMcsDyV0draucqti9BbQAwfDAVuJR4eiReDjPU8UxRfxcJrLhmCLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/22874" target="_blank">📅 12:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22873">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWIlDcDFbgT1XHaO68WI1x7vrm9NJZTJmjHNnxDzJdPYLo2B2-Mny97uRjN7dZGxez6WF8wVMeHlmBrjKpMzon6upcOO--T8SwEZ_J-M_DJTDaaiPDLexkhF28U2oFEzvO8RsiliksaIv1qFwCKGQ6MSxM0vd_g8FTGUXPLHOCKjWYPcuN-4fJlfM94J5U8s5qsiYi9bW9j2i3Lj5RTCB3VngkAIoms3WA---PgXIbxl3ne-gQIHDGQWQ3kmIpqM50dhU-KyXdPMr3xLLo-xc85iWYUX9GQoTkGH6VGJXlA1kayBYdAm5nkOYB-lzSGCjXs6lJOt2CoxcYMS_EeSbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
#تکمیلی؛باشگاه‌آلومینیوم‌اراک: در روزهای اخیر مذاکرات مثبتی با یکی از اعضای هیات مدیره باشگاه استقلال برای فروش محمد خلیفه و بهرام گودرزی دو ستاره جوان خود به آبی پوشان به توافق کامل رسیدیم و به احتمال فراوان این انتقال بزودی رسمی خواهد شد و پول خوبی به‌باشگاه…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22873" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22872">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Trc2eMc1a-mraci0CLYInKTIoFJB5xwEOcRCeD5S7fJviCVpHVun7_H7Mo7077WFdTeFUarf1IoOwKYTI_C7DCgXYdhGQ-v1pajjXMuFzzbAyaUHAq0DBYM-89QnzF3HniEtpm0M4NdjwsFhbQ1aQPpwRl2NSZy0d44Un0j8kbegz017sEAD5pETq991Q6SXvoKvqwCcmG1xenrQkJHZzv1Bftl2Q5_WVS8BRPpBa6yUpe_oTAUcti5HHA1Ahbdv6B1P9sOR1bChgmy-fdQXAB2KnEEJbq3O84XnIstUxcZB7d8v2bb9l-oDa8ACGOrB67t1zkq2m5qXv4KXmWaXhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل‌نفراتی که دولت آمریکا براشون ویزا صادر نکرده و گفته حق ورود به آمریکا رو ندارید.
‼️
مهدی‌تاج رئیس‌فدراسیون، مهدی محمدنبی مدیر تیم، هدایت‌ممبینی دبیرکل فدراسیون، محسن معتمد کیا مدیررسانه‌ای، مهدی‌خراطی مدیراجرایی، مسعود اردشیر افسر امنیتی، مهدی ملک…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22872" target="_blank">📅 11:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22871">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDw_FKnxCLeDGlHwH4a0rpbkaerbqbehmzUtysn0bp5Ow9BwnQls5Sc1ei8cM0Yct8KdXV5O3GQbq091PYp7mrE-EvqbAhjUHGzrD0DqjpGoXn2Bk93O9J2dwrycf1ww2z-DJfEH8G3XvfOtSWlEuhjIoek3prrTvfeyj2fkOdiGi2sSKmBK6LbQW-fg5Uhk0vSI3-d-aSy-N7_nKkTdztZ1UuRmJLINJPW__QbleL4iwKlxTbUb-KdD4UaJl32BAJxDAdLQE3yBsHgqdk9bwW_JuU5SvrPr1nLMQmtLhMXSW6p5lu5ytZwn7rWAVNfAAHrQOeMoQjdJScksCrmw3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام رسانه‌های معتبر خارجی از غیب احتمالی چندبازیکن تیم‌ملی ایران در رقابت‌های جام جهانی 2026 به دلیل عدم صادر کردن ویزا از سوی دولت آمریکا به دلیل خدمت در سپاه خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22871" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22870">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=rK7HW38znZeduUGe77taNYXWL4iHmAc4pkot7dQLt1jLy8tEianX-vvQvC3t8eXfSsU9oP1oR5G80-1eIrtta8gQiPYBs1IEWBwU00B_FxjCoSBwdy1XEENoxphdsZ_Rk2eB4jCPcCRnvpwnSbYwi5oEVnE6TEnYb8z9cvDk9LjoDbuewSZqunBIeOdIw_78gKYwMaQDx8CPXY4I0AsGzCSM8gMoUpoUYo_ViLB8HW6o3o5z_FvfNo4Lm7G70YAEvy46qVssOE6eVrNIjKqy67NyGPCOdtRdTFiLq9bSazXkfI4HOIiqJiwUf_jUaj7mpx37rzt7PB7julkoOvkyZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=rK7HW38znZeduUGe77taNYXWL4iHmAc4pkot7dQLt1jLy8tEianX-vvQvC3t8eXfSsU9oP1oR5G80-1eIrtta8gQiPYBs1IEWBwU00B_FxjCoSBwdy1XEENoxphdsZ_Rk2eB4jCPcCRnvpwnSbYwi5oEVnE6TEnYb8z9cvDk9LjoDbuewSZqunBIeOdIw_78gKYwMaQDx8CPXY4I0AsGzCSM8gMoUpoUYo_ViLB8HW6o3o5z_FvfNo4Lm7G70YAEvy46qVssOE6eVrNIjKqy67NyGPCOdtRdTFiLq9bSazXkfI4HOIiqJiwUf_jUaj7mpx37rzt7PB7julkoOvkyZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اجرا‌ها و موزیک‌ ویدیو‌های شکیرا برای جام‌های جهانی ازسال 2006 تا 2026؛ کدومشون بهتر بود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22870" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22868">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFS4hEy9594zPFdcqC5iGsCbGQjOcfFMpPOjcmxCaDm4cnvYOc-0ewSanCP0u6j8p4mxhkMMG6MAvbvvYElNrmCm1oy7GYrutbWkr4HBHWUDfBIeECdRBk5yOWfOj1nN65d8GYfb6bROuULGzV9-xnjKVDcfKcXYPrw1CLT9qiqU3UASOt41jGnkQ8w9zYeuTbzlIX68AN2wNBWjPYIiWnbjgkYECiOjFO_qzgOmxYu6q_BAGIz2svlP7a1KC4tPOhWij_PL2aNjIbooj1yklYH2KWVKfc7NI5RR5v0W7YnKCXt5RbpWm4o-UpEXwi8TnQpUXt3GnZ0m5Sw1UW8j4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22868" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22867">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mt9A8GeHg4iQLdi7jlozNY_FC4yQ2TTM6L2Kh6Ii9558FPT-ME9HSMgCE0LoIXyUnBJKuc-I3zAG0nn-fsMHanTBjhL8TZRJpDProhdVm2JQuJSCRysrk6tk0TRgXr5qHcbLxstdmwLMxtztD4rHweIqHdH3_KaYIafQWA3IyhX3AcnQFxzsQQvifE6aOSCXIEOzw8rNILPkF2OkQBOaZnKnS5x05tZqqOdjA4lPRqRMrEnnydOBzfivtgSNILZqdzEKWm3FQHCLJy2440P3-LMkimBAoVia1N01gjxYBSQEEFMasgxcgNSZyxAecDNGAPHFOJCrYpb0A3v6sR_Kgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22867" target="_blank">📅 11:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22866">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=d2VSxjSZHiNK6zDfdSGbphLS-ZU5_KQD2ejQ4z1fEEEiNTCcv-7Bp7EQzTV7saG9NdlBzW0mTxL-j9BPFVItq7cSjvgk9I_XjexPZ9RTG269rw2OUJtjqu-MFrpco89spT4K4tCGAOCLivd-xhFf91sig2eSNoR2zWOTismFvDmiDy8-1wYpXzce39mMXAz7TFCe49K_zzULv1XfHqFMlpUQjSFYlr-chdWc7a3XPNR5T7wxLPvDt7iSqjf6Tb9blzsakdUTjRord42j6ieqzct2975fQEKeclc-kMnhei3nYSd3ghVU6Dds6RWZmlKq1-usz8JOY6ebs0J-dEjNKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=d2VSxjSZHiNK6zDfdSGbphLS-ZU5_KQD2ejQ4z1fEEEiNTCcv-7Bp7EQzTV7saG9NdlBzW0mTxL-j9BPFVItq7cSjvgk9I_XjexPZ9RTG269rw2OUJtjqu-MFrpco89spT4K4tCGAOCLivd-xhFf91sig2eSNoR2zWOTismFvDmiDy8-1wYpXzce39mMXAz7TFCe49K_zzULv1XfHqFMlpUQjSFYlr-chdWc7a3XPNR5T7wxLPvDt7iSqjf6Tb9blzsakdUTjRord42j6ieqzct2975fQEKeclc-kMnhei3nYSd3ghVU6Dds6RWZmlKq1-usz8JOY6ebs0J-dEjNKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تعدادی از هواداران پرسپولیس مقابل فدراسیون فوتبال جمع‌شده‌اند و شعارمیدهند که پرسپولیس رو به جای گل گهر سیرجان به لیگ دو آسیا بفرستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22866" target="_blank">📅 11:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22865">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">▶️
هایلایتی‌کوتاه‌ازعملکردخیره‌کننده مایکل اولیسه دربازی این فصل بایرن مونیخ مقابل پاری‌سن ژرمن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22865" target="_blank">📅 10:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22863">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=ldzADCg6LLry87EQh8WU0iXpvJCPBn6FyxUXFuZVqb6JWzIoiOW_NUPf63vaLP8NsESbK--4QXP9Xu1bcrXiT-5Y-vFJwrrV3k_Ng89pmmTdtCHYAv4WZ9AGnw8uj3gtCbLIKL9py28ZOtPAaMncxn8wMrpS8IAud01Zi3dSUdTyujf4BljgNlvem43dQrPGhWMziX6vwsOVCb6MYYBXCp1nKZ0p5y-PNQtNBZlvN0RZ3epITkcfdJyXBQCPYS_NXG-1mm6WZRtFgcefkHxNDjhAU8fiIpF4fnIiDqle3OlAOnF4-vP6OgF46HGMcqNTShUOJUzTFJ-xB08RjzE_aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=ldzADCg6LLry87EQh8WU0iXpvJCPBn6FyxUXFuZVqb6JWzIoiOW_NUPf63vaLP8NsESbK--4QXP9Xu1bcrXiT-5Y-vFJwrrV3k_Ng89pmmTdtCHYAv4WZ9AGnw8uj3gtCbLIKL9py28ZOtPAaMncxn8wMrpS8IAud01Zi3dSUdTyujf4BljgNlvem43dQrPGhWMziX6vwsOVCb6MYYBXCp1nKZ0p5y-PNQtNBZlvN0RZ3epITkcfdJyXBQCPYS_NXG-1mm6WZRtFgcefkHxNDjhAU8fiIpF4fnIiDqle3OlAOnF4-vP6OgF46HGMcqNTShUOJUzTFJ-xB08RjzE_aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کیلیان امباپه: همه فوتبالی‌ها قبول دارند که رئال مادرید بزرگ‌ترین باشگاه جهانه جز هواداران بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22863" target="_blank">📅 10:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22862">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQCcFniomzwAjQUK-me4joX0rqNZzgDGL_MkEvGgMkrEr4AC33G-jqlpugnInrOro1avVqaXKN6g971sbG5hUtbolkBTO9pUSK6JrXhUI45canrhhrNNM3E58bkFyPCAFGx35ioSz4GSYjTX4TcFD_1PzmWrTfI5-xvgp9079CYCfPSMtJ-Dl2vjOrWcnhJ734iFXYhv5UzKKLINoMjMuWcTivTXs973BvER4kv37bhBAzBa4vVqmcFN1hee33nkCEdBFPEzD-vdKnEfHCJ7yqLgTzFa8CSA35WXt2FU_h6oUL5o0lB8JzgfBVCyFpOVwJotFBPrJWwRszvOWGRtxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین‌سرچ‌های‌ایرانیان‌بعدِ88روزقطعی؛
بعدِ بازگشت اینترنت مردم اول دنبال چه چیزی گشتند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22862" target="_blank">📅 09:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22861">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=j6P0-7SWtrRKSACEfea8kG8PPeeo7ky7f72BNRukztjcbXAoN3nHDy4EeOfZ45SkUdsEm3gTkcFmGVT6G_srsj_Hi_Rq23JFhztNr0GVqrFSs8jIhZVthE79RZzPqO6u2YMUrp2BB6eql_bX4h-37vvpbSYJH7J-_fnOQolO1sgmVZbaeoBMTCt_MCELh92Z98hx-nGzuBJZ-l9ry032-LmPkCJIdmiSfrVxjDJETmY95B2P_Iqo0KzVA42LmU3k-4ZEHAHidOqOwZKndiSAgvptaXKgCfV3sits36hgk_4AbgMs1C_4GsyeOSb1vJM14YYbAKMKRgb8L8B5dFjbC4nzZ9QrM5cY0YW5Ot3oV4wpl4N-Y3PDJAQZgIEM0K9M6Tbh2IrLy9XPMwsJSRp4c8xu_EG6niptbiEikPkQxL-Bbyj8amnJK3fSiCHSxA9guVMjyJvZLNs6vDJZAcMJr6e7IhT9UNFQoENna2claMsk8m5M-IfOe78m677J9zorJnEGa6mIZ7k23QcwINFjrk2dNxPKZ2u6zGRHhwV_xxPwtSM2lW-ff-Y1G-0Q1SWlDB6vmyAToIOtbSXu24b7AbJzLgETZanowdNBw0fJZDgmQmIjbW7cno00efiDWDyLAS3hKWJpFElm4JePKQnnck6zXFmvoPBqeu_yrGH4dFY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=j6P0-7SWtrRKSACEfea8kG8PPeeo7ky7f72BNRukztjcbXAoN3nHDy4EeOfZ45SkUdsEm3gTkcFmGVT6G_srsj_Hi_Rq23JFhztNr0GVqrFSs8jIhZVthE79RZzPqO6u2YMUrp2BB6eql_bX4h-37vvpbSYJH7J-_fnOQolO1sgmVZbaeoBMTCt_MCELh92Z98hx-nGzuBJZ-l9ry032-LmPkCJIdmiSfrVxjDJETmY95B2P_Iqo0KzVA42LmU3k-4ZEHAHidOqOwZKndiSAgvptaXKgCfV3sits36hgk_4AbgMs1C_4GsyeOSb1vJM14YYbAKMKRgb8L8B5dFjbC4nzZ9QrM5cY0YW5Ot3oV4wpl4N-Y3PDJAQZgIEM0K9M6Tbh2IrLy9XPMwsJSRp4c8xu_EG6niptbiEikPkQxL-Bbyj8amnJK3fSiCHSxA9guVMjyJvZLNs6vDJZAcMJr6e7IhT9UNFQoENna2claMsk8m5M-IfOe78m677J9zorJnEGa6mIZ7k23QcwINFjrk2dNxPKZ2u6zGRHhwV_xxPwtSM2lW-ff-Y1G-0Q1SWlDB6vmyAToIOtbSXu24b7AbJzLgETZanowdNBw0fJZDgmQmIjbW7cno00efiDWDyLAS3hKWJpFElm4JePKQnnck6zXFmvoPBqeu_yrGH4dFY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
#تقویم؛ یازده سال پیش در چنین شبی؛ بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/22861" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22859">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e0uA9jp2HWzDT36zlMxIK4klllqGqJdDl6r26Q7oruZ0DIJKiTYIVNHpBGeSN1HOBq3xaI31pqdP4fN4_pWm00U5K5oyuu_D9mlBn5AI1EljQzBKMVjrZWDITGWNqI27yt2q7jKlIqG9c3tescLaaG0_lCrDLA0ImifBAo4kLCVtfG3wQdjbl-iCuXtpVyB6zlAV0A8kr6QJCjiWZ7jNHaELIVI4M0I-rzBimr1gJIZwvJ07i8xeGsNehMVEHyzUxGF_vGefXBsMCGzq7JLELBSFUo2a2Pay5OBKP8zf6rCL8oGgIQXoaRyuqcM7fLYi0b5g71qfgXXw4sb_YuwJQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S75tuWW-K9D_x_ScarB7p-eUUNeYjrwj1Iyq7M_NpDBfTtEiMR-ic6Ulax6pZlhLuIwJB-OdYtxf8d68Uym6MuzNq5ZjqarrPaz5gvUDuS8GvjcMXWH-qLkl_SIWSnYFMHVEcMbG_e2WQrSuPCvH0XBeFjdURCfZOkBmX5zd1UVDaKzQ_KdiSILXXrQ2Sa6fVbqIFNWZg48Tz0aPlYUNGQTK6qguDzUU7v-p9AiYAURIxsN6EO-MNPMZ7BcZC0ezBcwRHiviR-VOB_YUa1YHYp9-qvX9DxrN38ra8AaBb8QBzToPn1VkSnXZnQmQBFWMnaT4TrymLzTTjhmeriXTVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
#تقویم
؛ یازده سال پیش در چنین شبی؛
بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22859" target="_blank">📅 01:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22858">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqtCkJzwHB3NdTMWyZO-gezHkDYKanrL70tiJ98vBmQovZksx0XOsrApstPX_01udYRPXpDRjcUovKsc67yGicbBOkJDvT82SVPVgygKMz0xtMNYMcSLGnsAVPHOxjGOoMdtBzvYW8aF8LDcSi3fldoAoANxMWR8_ClL6X1E3Quw1J0LaIvk-02AYtZM9pQsOiwJ4wawKIoeB1L1MS672BEcDP3krz2UuOAy16JiWYEo585wF65ImXuRHeqwSbdQsmL-jAvbw-QSildwSMsLwpiRcy72k0_0cBheJxyjsEHnXWK1zQgm7OLN0aXpx_mbtSHTYY-WNKWiec6adnDQ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌کامل‌دیدارهای‌‌‌امروز؛
ازجدال‌یاران رونالدو برابر شیلی تا تقابل آلمانی‌ ها با شاگردان پوچتینو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22858" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22857">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUroQV5YLPyKc1aDusEgXL5D1fl8H6EmCS10Z09hvbOIODFmFZgvop-f85m5oev3KY6OFRNsE0Ayb1hjjT2eoQOTa39xUsEFRKZuaX06EOsfo1f4QhD59IwTZUS8oCvUnPSvWBnxRyhlFRc5Re9JhFq9g8RqigYgnZBVcQQqTXSDSTBwmKv1N2ejWYwdfXLHZmwozXpPp5ZuCcpOmrG2O7YFw0B9n32--vZTR2LYNl8NWYUaIz5qBeKGMe-6VZAp2hu9SOdE75jXsNl7OxM6vUjFXsW29oHEAwt_Vj8_eH8hzTPRxJEzDXBM5VAdlMHy0Ejv7v03KV1uzFPYAu0-AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌ روز گذشته؛
استقبال مکزیکی‌ها از جام‌جهانی 2026 با جشنواره گل برابر صربستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22857" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22856">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHedOECEvFHNGV8HYtTJaU4i22tC3idyl149m_G_0Hpu63zSBFI8kT6G2Fy1w_tFgz7KOEhaPbLKxvIgm4agjFEiGtSYGgG-pmxS_Zyb6lFByLJ4xpm8E5x8DuAaUa58amRroYuKkJBNcI62eDrEb8zgVmmzDIPwFu-wAro_zbQnNLVTzsv7WTz3KY1NcWiR_-P6-MHCVjeuWAprTj12AwkfHJTv1BeWI2F1-CmdmimCdtHRn4tPWrtqMHKuUIGx-5ocOG6b71H-dTdv2dZoOQpbx_xPje0B6__azpNW7Vx5RvQZQEHCJ9lQR13p6tpVwbCzmS9BaiEExiYV87SQGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شوک‌دراردوی‌ژرمن‌ها
؛ لنات‌کارل‌ستاره 18 ساله تیم‌ملی آلمان درتمرین امروز این تیم بشدت مصدوم شد و رقابت‌های‌ جام‌جهانی رو از دست داد. ناگلزمن سرمربی‌ژرمن‌ها بلافاصله آسان اودرائوگو ستاره 20 ساله لایپزیگ رو به اردوی تیم ملی آلمان دعوت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22856" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22855">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvrIQrC5wFPX5-Ssu8333W3cAnnXhAzxze5h01nTwTPTXTkmLg-Ri8qzSBrwGbk-BK15b3ZnynwgMMaOqG6kbYqAby99qyTioxvufgfDso8F04uHC25BagdO51cXrwfJ_D79goTZ_krFPDRYZblaNnEzOyBprX90r48aQZZD5FWkEo_tHH_h0AbF8dKgWUQGjOJYrHfId9r7jOKTeLcTZ3rYVoBRiRgQ4lMzWodybfNyJn3laus3-xJI-SlqFtOp7gchUIwJKV6CV0KoctRjGPjHbHTSvYDmQttd-_HpIb8xnFJIgD2pzIIwmqOtFTPHtSO3_YnyveRPCvhfLOal4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22855" target="_blank">📅 00:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22854">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szAfim2uj9A5BuiReRt86Z15VQT3X1AIQwUoPzSAFipvuosqIDzwJjaCER1sEmzdvi6Cs9a2L511uiozdWMhzYdgPUJ_TEjNd2lIVfvUsedji1BD-F-wlPIPUgurg943Qr0ECvYbN2I4Lt1-6XgD7zHUG8830d5etx7rEaMtXOxb3xyA0S0qlISO9XAx8mwP_2SSmivR3S388ORGcLoU0jXBoNv1S9WpnsW4FJ74tnIDPRmJIeRfFpg9hfopqSH3mWAvLi6qCyykgf4r3MmGZdRuMfNphb0-sKrIPRN8fwTQLzPB3Im5sLKpCrbGVOPUDO_C6UcEklm82MmbWWVrTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چت‌جی‌پی‌تی،دیپ‌سیک و گراک بدون فیلترشکن در دسترس قرار گرفت. همه برنامه ها دارن رفع فیلتر میشن جز تلگرام،اینستاگرام و توییتر؛ سه‌برنامه‌ای که بیشترین استفاده کاربردی رو دارند باید فیلتر بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22854" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22853">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=otYcJG1a3QaZWchvlEVxZjG1IIQ4tjuxK9tw56xYyCjGu2R5p_gVSqVVydr8Ti_ehyBKwmJ6PHMCuE9XQyKZbodQKdERs778g04Np-DVz8ssmMordHoTKRBpSnYqOV_zwm6LWEYB1hk_gRege-a_Yhk_gPqVb35A-yamwLI_ZRXh2vk25bUMpa5ItKvqcN1SJ_PMJMA581q3f04cwHxTd929J7tvo7DPQe3RJSvIrsDSTNeco96DjetDa9sT4_0vetdwqqG2tGvRiX-qOa3K0f80z2fZv8ET-yF2ckdvp6w2yCCQPUmU3_dJ0tlLGlh3zZQ1ncXc4x8WccdLzGRHlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=otYcJG1a3QaZWchvlEVxZjG1IIQ4tjuxK9tw56xYyCjGu2R5p_gVSqVVydr8Ti_ehyBKwmJ6PHMCuE9XQyKZbodQKdERs778g04Np-DVz8ssmMordHoTKRBpSnYqOV_zwm6LWEYB1hk_gRege-a_Yhk_gPqVb35A-yamwLI_ZRXh2vk25bUMpa5ItKvqcN1SJ_PMJMA581q3f04cwHxTd929J7tvo7DPQe3RJSvIrsDSTNeco96DjetDa9sT4_0vetdwqqG2tGvRiX-qOa3K0f80z2fZv8ET-yF2ckdvp6w2yCCQPUmU3_dJ0tlLGlh3zZQ1ncXc4x8WccdLzGRHlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ابراهیم کوناته مدافع جدید باشگاه رئال مادرید هستن دربازی روزگذشته با ساحل عاج؛ واقعا مدافع قحطی بود که فلورنتینو پرز رفت این رو گرفت؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22853" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22851">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTCZ_UUihpgPj437MuKqluE2O08n3fbfzV8dCSTDsSC1A-DpX4AMgwWjMIW1q212MjO1sBLjLR_2UkrV2S0nhX0Dsce7AsDjHU6wM2fZU1S7VQqY89kFnmfZh9ZsUsI3ScD22xiBBHhAppM1NYVwQhAVH8OM3U6OVdokvYT722tJ3r6-ie6-RQDb4hmYcIf6QUTn8-ePcDOWFeR2WKqMmEhOfJHbTrU3A6hNyT-yOGHl1_yyhSDldS-B1pJQVFG2tr2sJiNtblxgIwltuacuZXQolh1LaZrNt72vNOgbXxJVg9GS5lQdJTfpgK9BQ8F7DYFVREl0CEmlSkwU6fua7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
علی‌‌تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: یک‌‌نفر از اعضای‌هیات‌مدیره تیم استقلال در طی روز های گذشته با مدیران باشگاه آلومینیوم اراک صحبت کرده‌ تا انتقال محمد خلیفه رو نهایی کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22851" target="_blank">📅 00:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22850">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwaxQ9YtQeszA0uyLq129gwKnZxQccYOJjGjTeta95XsoymeJUbK8qMH2SNB5B_PhklxEwtoiIQavg1T8_jks9pk5YahZPxJgJpcY-JBgmEeSx1eYunYVCJ84EXq2T36N6zzOEp57zhr6pjfuoZon2aSy_oWB3LJ34S25-TB2pCENnLEUJv0Q8CmV1LlCUvKlssT-Wrp7E94Ghjv8oUGYjEeKtOPkAcnxpgkVCxcBOVGCm0dFu5K-MicY1zNbXvauxYzRkVM7dJHQqq2pERmrvvbuixTMgYeNJYTTl0u4xEVrCulTSQ8FshnptXhxuJ0uDeVKznNlpWAKha1c8iLyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22850" target="_blank">📅 23:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22849">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=RvMUPq9lYmi81jnMFmA8KyJmMdtIIiBxEyIMyt1-NWT_yeikweoVCzBu_QNW2Rlk0l40V1N4j7OZ8c5Cz54i-5hj19ZkwF3W-47d3wnbdaSvg7rHEoca7wVG03PP5RVrUHLf-K6_Zu8F-Yk_rK7UcZyHp_Yt-dyghcLd0qbjQoPtcR0DZITv4s3HfPD7RY4UWFr4TKQ8kogSJWv2pp682OOjbB-1ZlpJOR7n1hgisyV1NYBW8XrN9oLVm6dNYuyTHpIvPCO8qoHNAbzuBD_-eDzhG3IfDMPa9--LV9dAXcv6psSWLazq_0LkGwR9n7EHl0JTVf9b7uDyLfnPti3BRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=RvMUPq9lYmi81jnMFmA8KyJmMdtIIiBxEyIMyt1-NWT_yeikweoVCzBu_QNW2Rlk0l40V1N4j7OZ8c5Cz54i-5hj19ZkwF3W-47d3wnbdaSvg7rHEoca7wVG03PP5RVrUHLf-K6_Zu8F-Yk_rK7UcZyHp_Yt-dyghcLd0qbjQoPtcR0DZITv4s3HfPD7RY4UWFr4TKQ8kogSJWv2pp682OOjbB-1ZlpJOR7n1hgisyV1NYBW8XrN9oLVm6dNYuyTHpIvPCO8qoHNAbzuBD_-eDzhG3IfDMPa9--LV9dAXcv6psSWLazq_0LkGwR9n7EHl0JTVf9b7uDyLfnPti3BRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه پرشیانا؛ باشگاه آلومینیوم اراک اعلام کرده‌است‌که هر باشگاهی محمد خلیفه رو میخواهد باید 100 میلیارد تومان ناقابل تنها بعنوان رضایت نامه این بازیکن به ایرالکو پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22849" target="_blank">📅 23:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22848">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=NC47FtZb_N3g9eYNacl1rT7y9U14kXl9Ro9jXNyNTSsXg3qyJAxNaGePzzVBYw6DkyRupWChTX8keswDVDc_XPaQGpNTENV3Dwx1wuUdWg1EkcsuERupt_Ep5AIirAZx7dTbEXUFwUfhd-EIJ0-i2NPWQC_ft_WjcaD7Adh2pHr70fXtXAwg0M-33ToYP52XgrF9oqQO7BlF8xbGQSagoo41kbcleUgiukUFLrmwWFwZaEEb2BMf0TUlxa1my_FF4nggK2IpD13gz3dD8jgijOUWdhIao2QXmFmk2AMZ39DkIE2QKnxi0HgERutTt2WPKNJbtfFmJwA8szLBs37vRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=NC47FtZb_N3g9eYNacl1rT7y9U14kXl9Ro9jXNyNTSsXg3qyJAxNaGePzzVBYw6DkyRupWChTX8keswDVDc_XPaQGpNTENV3Dwx1wuUdWg1EkcsuERupt_Ep5AIirAZx7dTbEXUFwUfhd-EIJ0-i2NPWQC_ft_WjcaD7Adh2pHr70fXtXAwg0M-33ToYP52XgrF9oqQO7BlF8xbGQSagoo41kbcleUgiukUFLrmwWFwZaEEb2BMf0TUlxa1my_FF4nggK2IpD13gz3dD8jgijOUWdhIao2QXmFmk2AMZ39DkIE2QKnxi0HgERutTt2WPKNJbtfFmJwA8szLBs37vRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22848" target="_blank">📅 23:34 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
