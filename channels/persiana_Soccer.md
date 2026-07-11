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
<img src="https://cdn4.telesco.pe/file/hOTE7QUM6m_9PsZfirNGW4AHVt4kHsZ40Hu_7J9ERg3khoOu4G8cMub_OiuTMtgQoCcCJJ6hXhwuVm__dDRQz3smlnFMjOF9zXqDSdTvORhGXNdlZWKmRlqJEqY9TDLYP5peIhGkTCzqENcLGGJUxHLnTCe8j-GuzpiFxLlhX8pfdGh3F0CbfGjyEN6bC79Wo472GyW_BRY7-ktDrVt08X23S5nVI4l7QMNVLauFZZGgaZqqNyKQZPEd_u4QCpIwTTz9uHtCxta3t08jnibATlEYJkvCUymtV1t2lOHb0fVkILMNqPVkC09Et1oT-YL8dRr3xIo8AHQBBMesnSop6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 425K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 17:52:09</div>
<hr>

<div class="tg-post" id="msg-25452">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RA92UrkPVvO5oncbNgEdmpwN_E0t_0Ec_xy7NH4x5C2SuV225LWRuXS_5xiUL25GD-zjHYJQ1FXgCvcJE3TB2X90ZT2rieXVkiknl-KHDW0rOcbeJiCAOhGxARf70RcbCh9VcnpTqoRjndtUZNKqhVtoQJURFCbxbGMNbZ1kBdRHIp4k5pJVgrsB1gMJMWkO6dIT03_pNnVYAuAx6UHs5vYzy4VzRKA-0kmCRht2Dde67-45G9l_xXLmgS_rZSvMYMuQYRSMl9I0q-LV_6zmDR__sNOy21JQD_EgW88NQu5Xeg8H1P3hYZBowcQzWgScRUbe65rXyf4R9flzsoXWbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/persiana_Soccer/25452" target="_blank">📅 17:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiQ40lKidiwAgpCBV9qfkTIsc_t8uCWSV3RJMvg9jEN0U8uoiJ_1smTajhTJDt3G6kTvMA2mP-U0b5HEoqjuH6TvA7NFHxXPd6BHWabiaDx49k-5cbKemO0LYZ5NFikl6QydUblR601rAqJz0c1BPsgB-QJyrs1sGdSH74aQEBRq_JyG8fxAvrndn84ZD7Ey1hoG7ZXJbAzcFUC_So-afu-0c29j0CBkMkJlHSjN-WWYIOKmBP7qYy9IA1QAD-pYTSdAqJF227wpiSbFQNB9GUlJOY9GxB529_uS6B6GrPgA5p1JbwafypWKxCvUnLAfSClwe8ftHDzAsv3DXwLEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علیرضا بیرانوند دروازه‌بان ملی پوش تراکتور: اگر در تیم پرسپولیس میماندم شک نداشتم یه روزی مدیریت با من هم مثل وحید امیری رفتار می‌کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/25451" target="_blank">📅 17:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROOItZ8VNtR9-cyqZjhwjf6RW_hN5Pw3DPWmgMykZLaoyrLgCOJhWsP39dY6b2tEQobJxoJiAFrlcsO4nxm5MBUJe5Xy5D3v-WZQ7IX_UDiB4_T0rpEbZMZSsu_E30_GaZV23OlOVpHacSiOVkAsBzgkkbZVt7dlG0VnE_QJqQTe5cBT_lGtqZBBQUNjM_xodm94SiXtEzwB2DrNfOjIG-hppu06zit7X-TlO6m_b-1nFXO5FuFRay3fXhTXnSAXrIFsCTN-SHKwmFhUE6q7CeOC-0O3SzM2nFWnsc7Ie4Dq39Tsu4_zjhDpL9O051fdPK-2K7Fq0CYs6VwFk6CBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/25450" target="_blank">📅 17:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7bSr3WeT0WfIBT7Yd-GxAQmo3yFhANXMbvcwybw5gBvjoHT7aB3Y3sD0-8II7pPn5VvtMWpl3zvoEFOg0zBaE7ot8GnNoQQtngcGJ4wlMmhs4i-RIVMd1c6THVlcH6ksbshhtM64wkGIR6jkRHysrWMKzLgzu-LKG4JqOu0AqlaK0ZKG6Uylq4FQ2tb4UxZOXDUoMZDhOs24PnglDat0YRPKAZBUD4KUu2F3KvpyPiE-yRTf-z05afYBlBoT1-2fHsMQo6yUHLXFZ3CxQCNZ8U4ajH-RaFQ1bDK5vjuTuLhUsvUaRP35ZsuSs9ZVaTPtj-15slZ60KT9qMNllekBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال
؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/25449" target="_blank">📅 16:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qyk0LMIwkAxLtPakownpgSQAzoy-5t4zoL9fFf68ew_BJwfuhTQpOo0R89qKEJQcTp0nhhJuJ6UKxEfNPfEkuRsF8L-LW1CXcNa0YBHup0JLLBa0GxT0TlCJmmV2J1DtU3Pe2WziUU63KnCYnRPtHnq0Twno_QbciuO_7zajDykrhvjnFFq3PhhYkWNBW7iCQ1TemhEXCPBdmEp1y6Pj0_hvGFWT1vTSnPSQD4zbLgsLq2ppPkeD0NOq53rKjnpNx0IB1LJvC-9-4mm85RqqqGJ9dcZ-Z0Q7PZSXCXQ0PZ4Kn3gCGJsdTJiL6YfcJSzUx-7R5VeBwAS8L0nnvKs4uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#اختصاصی‌پرشیانا
#فوری
؛ باشگاه گل‌ گهر بدرخواست سیدمهدی‌رحمتی خواستار جذب ضرغام سعداوی مدافع‌میانی 20 ساله تیم استقلال شد که با مخالفت کادرفنی آبی پوشان این انتقال انجام نشد؛ بختیاری‌زاده به سعداوی گفته به.سبک بازیش اعتقاد داره و در فصل جدید بیشتر بهش بازی خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/25448" target="_blank">📅 16:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25447">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTwChkSfxQzqiBvhaniubPFE4M5IjbvUmW87Uy_0ra7cgkxqDGjRek4mH4elgHRz5JZ_0MfOOgpAtAeF1icb0u2Vp6N9tS7xvo147ZowlK54YfCTdOMXk_XCyfuvaS_TH8Yl9jRrY3M-Gi2l24LN-eIIBlG8DdgWtkmiQ06zqE82AePGW16MR95a_Gd7nS3j36iSzJC839PnYNRLYGFCSIcUELBdGbQRKjAotKHz7O23QNO50NQx4HC1RE3KxadiGGJFojPNHS6J7jJ4K9l89FNawupg3FfTtJkgYrfOhRzrQzqKBGIolzKZyVEC5jt3vMujNY7TJXvBls632kXVaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/25447" target="_blank">📅 16:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lk3GnIEwrxW5c4Ctgg_MM6nvcagjPCBEUHH2TUNjeGpYUNpppBarelBSOISREOorfaqs08krUccyVKze1IzDr7fUWJrA7hVS76EP53fW-KuiOIo1SFz6xkqxafBQHpGGE856a3ofOGPBn9njXDJZxLfsle1_ikZECEkOuz9T_IARRe6nO2l7gwlyPCfZH89rYviBZJR9jH6HQqOgCeVtaJSpjlz0J2U5p1tmdxWXt5K7Udy65wESNmDQrGUpzNqJS5NP5TiDgDi9YKxHmpuTXbWknX4HWWFTDGcD-arSEOQo8ttf7AhpZMbCigW1RSQ_qP7IGiEC_MhUdZefLtiH5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛ باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/25446" target="_blank">📅 16:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kz4XYmiLMeJhXpeYvf2Q18l1doF1AczmabpR77AS5wDymGORoXhBorljv08TU_jQoV7XGGPP-RcEuquGwvVIGYNVXo1mhKbhhoiVHD3-JuanhZ6V4TiYo2jHVqkC1SHwAxT7xypksrSdL6Gq0DT98ykjcJ9YFkXI3E-_XqThp9e13H-VZM04_rURv4ZuviLXIccix1UTrSu_EoFjKYCVqHCuJ90HEQYh09LGaxzaaqfQ1TN7b7I5vrgXIWz1g2j7ZLUARepSK8CzO6zlJBvUz4Hxmsan7qJPfXKSxs3Y7057bt0uQDJr2qRd_mPMLLaSBi1yAZgFHCR31_V6LEn1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/25445" target="_blank">📅 16:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nY5LvNclVQ35gJgzu-cvnHQWz6Cp2amGWmg7o73HS8PHdhGp-vvQe_5lR5LM-5IYOQNXpwNM4VNqvq6ZW3KEJ8gMUx23WtTCg6tOmZJavMUgoaDE3S9Qx-vpiw5gRH37X2jd3kG983IxUlgmvHcaYuaTkKJmd2wEsnZH4DO7YJK3We_okuSajbyOqsmbHkUJoPhN8zYSuJEogkr-Fp8FuoMNe6aL81mAyJJyFpt6vwtsc786T0u48CCvsYeYPgiRFpBnHSRoxp6KICdlyX9uFgZqMSvB7-hLv1M_8XROpZNF3j9mgZXCQns6fgAj6-Mf4PBa7Poj8L813vIeAYXVmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/25444" target="_blank">📅 16:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f29VcSfIkNzXjSsbl8FKlqsxBeWDUvoUErXKoD_pmvpN0gPNAaTNxzSOftrVR8DkQIRpWtq9uI3k3kcOuhclprIYy4WnPl_4Q6xBXb8eeCH1WtEAAyBENFMlukO2An0Elh1etoBQLsnKvbRduUuMZFgso12_Z8aLHHzuj6QndrsO3jK0T4gwXFKwpnVK75he5hCnepLTnnHwZGf6ig8McQb3gDkNIopmp6wjttl4PjBWA7MugYrUDplh5LFMqYs6Xs5V-v2b_pMwzKaEtx654dbLyEI8qYoc2eQbyJJQCgPx60Agk3Licul418Z3Huya9vNQwXpqSwGIfsl-outSqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/25443" target="_blank">📅 16:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9PkffCtbuCZC4-lffGKH9C14u25mzi_Z4tph4tDe0pOFPKDN4LmQMfpe2RdAJSg2FBt2FrAfhHqQJeI6lmkgfZO0XM48mPNEm5JJXxnYm-DmrSLj9p3t-b6oe2ULR_9EDS2wto8ratuPv3EpMXVtg3J1NiSUbhVP8xm0S53LfT0aAFIvh2SvmDo-TwTsLcanaG5zlACeSQW-Fzia-d7OzoSIyouZVtp1edWb-jlOkWuPrw-pQbmC2x0MGKAQhuXTO6V8to_CoT9EaNlPbP8cf67B_43zm4_lZsp_w_U4TGrEyE5LfZ-uFjQJUxqyUqd8VuCjB-fSchbJL2Km52DrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/25442" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25441">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=KVCQxjLXR-tT5V1hHcag3dNri6BJ5LLH--Y8kr9iUnq_ydjoXhWUfoWjlSUQnmxck85dZGLzNzorlLu5jRLDngU8nsOHbEwOP0YPvr7tUAF8vJn1cwMjfvIQP6rWQoaW9qcfeLwhmp0Wwk0HJABBWBax_-PovEMxh8wet8Z70DAFMwrDQ7vi3oEzWDqbs7ErhqI47IsiUR4wHAzlcoeHhDifE4NV5cKjBW_8ejkiXfPf_mgziF9MU1kXpt-VpsMTqWwNRacGl542lZ0WGqHVMSSY-AmeTheWA-9l6mjCmQVO0w0bf-ESKsXaLN1eqsnot7PvZQU2WnmJHu0fqdj1yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=KVCQxjLXR-tT5V1hHcag3dNri6BJ5LLH--Y8kr9iUnq_ydjoXhWUfoWjlSUQnmxck85dZGLzNzorlLu5jRLDngU8nsOHbEwOP0YPvr7tUAF8vJn1cwMjfvIQP6rWQoaW9qcfeLwhmp0Wwk0HJABBWBax_-PovEMxh8wet8Z70DAFMwrDQ7vi3oEzWDqbs7ErhqI47IsiUR4wHAzlcoeHhDifE4NV5cKjBW_8ejkiXfPf_mgziF9MU1kXpt-VpsMTqWwNRacGl542lZ0WGqHVMSSY-AmeTheWA-9l6mjCmQVO0w0bf-ESKsXaLN1eqsnot7PvZQU2WnmJHu0fqdj1yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
خواسته‌تموم‌پسرای‌فوتبالی؛ روزی‌بخوان ازدواج کنند و بچه‌داربشن، بچشون‌حتماباید اینجوری باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/25441" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ug4Hw7ZivYcmdIVFA129aEXD9grmBQwrwd_3NO6gyKgWHGvMxLN_bdQK7mU-WRVxKXQ7ZZ7EjPIoYTd32b2bQpD4t1p1EUPb_8Tmo07jetxXBq0e3f0-jiR96l-60sB6g03FCbXxcASRu6RxaavHHStiHkf79rhWZj5bQzPffsvgFkAPLcVhgSINkjHSbSaFVoyiMk7kM0qi8Vo2WDNTdVR37gMUTQ8x7yn1esRfE3ifXw2uv4wZjOmjYWq0Pbd27coe9-yohX2CKfIW5PG6-T78gmGKSQzoh8Q-nbi6HrJCUFMtxYkgBvPyaUp0wbr82OQ3aATBx6lTOQ2rDofKfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/25440" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25439">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3-UiCZQ7V-fCeBkpPHdxAAvxeFEefk4E6fOh3n_TadMpsJI3eAGmfbfl7PmkgzhVPyc46oavDIQHXiV1SsxPwEV1J-FLB3Uy-KW7K8Gsx1MjOAe42XQ32moBdDAYHibuZSYCuZ-mup4lAwhe4QhGZQ9U0aQ0CEYnEOPn90K7aUC1Jr3w5PQs5BzxZ88_jYU6RKNNkaJYMeZOmk-gJ8D9A2l3Xpzi_Gu4Rg3eUUwbxqiGwwvp9OzC5yMbyorp-OnmQUt-O1u3X2CESNjQ-IeGZOBkCiSsz32453mgASTydZkwlHjlg3ykUX0wGU69By4Gp-Wloh9r25lJZsmtYlWGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گردنبند جالب‌ دوس‌دختر لامین‌یامال ستاره اسپانیایی بارسلونا که اسم او و شماره پیراهن‌ های این ستاره از ابتدا تاکنون هک شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/25439" target="_blank">📅 15:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25438">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjKw6s-uTvVe2E-rPu6k6m0_-ztja5rzWFYlFGmHfq3gnfsMnjixgsng9ihqCqmPDiyOHGDJYCjGtYp1WDTPd2OGox8n6flepyYGyz9tKy5iASTY_KwCPHzyBiNBurcrL2iXyd_qWcoUi1rGlFVbMGmoDrG_lDxTvUxGqvVeQ6QvSFGERqdeN8cac0PoKwFWKdkEZ8pWqgu6i4MJxfeL5KHL6iNw_BHJQt4i0Fn_s6cpg6Lwd3esPMKmfHutRR7bUbKDVMiEHTDxIEoi1JWkM40CSmiDTUBsJjV5i11AfJqOlkXNrOG7SjYGtPkOluFNN8wxKakhsw4X4mXAyangjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌هوادارمکزیکی درصفحه‌اش افشاکرد در شب بازی پرتغال
🆚
اسپانیا؛ یکی از ستاره‌های پرتغال که درلیگ جزیزه بازی میکنه بهش پیشنهاد رابطه داده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/25438" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25437">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r36ArEaf3Zpc146X1fLUU4B3KHNusHJMhKQ1XRbA1nKtuotBrZ_fdSrThuvypQt3ooY8HRPaB_5ZK921FgCmgImRnl1dUKJ2luKGdDOVSLJzzDLTOIn1WejFIS4k1zS4l9mZyHHMPb30r1KHLEeU_4cSzfPUL17eEBsRSNxgbAtX8zrwz5eSrYrSLy9nMxZTzbiQ33jER1Oh3V8gQttJr1UAXbWQ3Nt2d1u8fnkYHn_T7GFMcL0V3MMKxgWZZQcugz_8hfXd59HBw8wKzIT4tjHgy9YZk0uhVGpCF7tnAGRFCYM1Kv5YyHwvm3Cz2M_1li7DbBtOWfOuInDVO2BGtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
نشریه موندو
: باشگاه الهلال عربستان آماده ست که‌برای‌جذب رافینیا دیاز پیشنهادی 80 میلیون یورویی به بارسلونا بدهد و دستمزد فعلی رافینیا در بارسلونا رو در الهلال چهار برابر افزایش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/25437" target="_blank">📅 15:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25435">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D7Dxxhyz05k8N4zA4SkQdQneKJChbUHumD1G6BOmFXRK2JNVhOEq3IkmKqaMNHCPtrZQ5agdfMFdpJN0MBghOu-mnzsJJ2nOcjSW9vqNnZUtgrlFWklG-FAPR1j7XAWirIP6xNoVhUN3vkirngv0cb7w5pN_5CEpeKZ4ftxXbJ5VHmPoZp6JelQXmM0BDYLQ43rdsKx8TwISZ__gsnJWgMtlKkhA-5tguAOS2bpW4lTNwAqqKy56GRhO_kEm-hn45V9_7nb5r5a_U4FIP7mtG3W1VoOP0rQlV0PTs4CGsLJSu1DQQVJRn-WJuDxpJLLveb1sQ33x-8dTwlnZvOfqvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGgLmFVYaKR8l9xSjnkyFNarXnXsTmZTzQY8Vz6276LMEVWChtRqjKoGjwIAafEoFnfmvVkmKx_l6KOL_rPpeoNsIzL1wvNM68hOzNAkk1Cck6wlyOp-KPlEazkW-AD5fGU9QvfnKEv2ow_egEw9MaQmiuw-rSNOhboSDiorFzLVERuWygMM9QAz7pG-buKbt8wX4EdjCSaFo1JdpPlKLk45gywEnZEQze1kmy4j8sTzzn8liY49U-FP8qrg9cx50Gy1PSQgygJqAOZ4JlhckPHQzkrHK0iUEPYR9G8cQFWdc_GsiTSx_hHLw5fNwfP8xps_kvU3bQFPesIiI-J0og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
جالبه بدونید دوست دختر لامین یامال قبل شروع بازی امشب گفته‌بودکه اسپانیا دو بر یک تیم بلژیک رو میبره و راهی‌نیمه‌نهایی جام جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/25435" target="_blank">📅 14:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25434">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=vxTlHzoeh9DTHCHyUzBFRTKW70lAxyjC7N7GJqVIymAcnkRdIUXmVvzYB6zwD9nfCYMaahcF2QkKuJNetzA813E6nSHBdJKjKl7f_8FY5VsrTYnRyWqeqmfnjV6H2dDznCYssLp7FZqSglOlhmsUv0Qc-9FdoSBbRL5-5EwZBlRtw-jwY-nC9mVxxbYCeKGon4TS---ygiC22GlQ-KcKYaFXAJ2_82scgPYGR2VaNeQkWz6rL51jyTAOZ5fs9Qsl9IOHmWkIlD2T83shYz6SSwZKP7ql2xGV9T36kjbkBQrst6S97WVYgNlGy1UjzV0N4wg2aokxB9J-HLmvkt7Mnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=vxTlHzoeh9DTHCHyUzBFRTKW70lAxyjC7N7GJqVIymAcnkRdIUXmVvzYB6zwD9nfCYMaahcF2QkKuJNetzA813E6nSHBdJKjKl7f_8FY5VsrTYnRyWqeqmfnjV6H2dDznCYssLp7FZqSglOlhmsUv0Qc-9FdoSBbRL5-5EwZBlRtw-jwY-nC9mVxxbYCeKGon4TS---ygiC22GlQ-KcKYaFXAJ2_82scgPYGR2VaNeQkWz6rL51jyTAOZ5fs9Qsl9IOHmWkIlD2T83shYz6SSwZKP7ql2xGV9T36kjbkBQrst6S97WVYgNlGy1UjzV0N4wg2aokxB9J-HLmvkt7Mnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
آندرس اسکوبار مدافع سابق‌تیم‌ملی کلمبیا بعد از این گل به‌خودی که درجام‌جهانی 1994 به خودشون زد توسط افراد ناشناس به ضرب 12 گلوله کشته شد و پس از 32 از این حادثه بسیار تلخ، قاتل وی در یک رستوران هدف‌گلوله قرارگرفت و براحتی کشته شد.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/25434" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25433">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEGG2VQs7mKAiluUnoFhNa5-NLscgLHLoL6AuOKsz7kBVVycV26Vub2aN85Td0RYM9GqPNFjcP2QeDBb0Cgzn9BkYGMgAMGojWpqJOj6JBRRKTWty5Fizhmq6QgTXTGynf7LmtfAPjygVjpY5EyTBpe5PFceXXCSZzbtz4SvFBs19j9beqcxiKm1K2Gmzga7rLlIcsMSuf3PstpUPBlfgowAMg5C7PzuPadelhEZBBz_vKzKpPTCeJVKQzp0WqWcsaWcPnK4H-URnmHpzSg1Ivd5nMR0tembkT4_HBKKnXQec7HaY5xyy2iCSIqJJL6Na3Lc02U5SeJ5e14k6muNDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/25433" target="_blank">📅 14:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25431">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlJe5WjnWK2BClSb6LCaZFtXzgr0x6fRaaB-2LZkU_xhwqExkkZbU6E5oEtqph4U0kbb7NkOXV5-HtDAP8Op7TKPDz7jqWMbmhnvcAxYC1vggvC7sdNBvDmCQCw3GCXNSfMDvul4HW96jkFFeaSCnNJ3xpYbcCcAGhjFj4jyAv3ktvpJW48z8oAtbWihVdzdOHkKf40AOI-26NkzqfZx0Dj6-8gdSTGQHJJTukQgfV-xyupCKybAm6Dm9a8njfzcj3IM6kZ6mpI2xpBKzH6eJVu50SP7Ct8yQigU70kSHV9YZu11VVAUEyob7nobWeVYFCciBzNmfgRYQvRunirM0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/25431" target="_blank">📅 14:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25430">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf__u0qFYpuD_1-6Ohm_m9fujtjTc02TtbHq3RglO1sqyULvDgv0XIwzgZWviBKcsaQ5oa5ze6bKxJ_8J4JaMzCWHNanXblPTvkv60y2anLUkjXizwGLl_dcawKGWcZUcuAgSPAfdcMWRBra3UvgPDxKETWfa4J5wY5vQHjQAq7rkYrgvHAR9mkAnraaghKXoD_0IwG33OdEPHR-H_IX_xXGlMhQw-qkxje0JyfdelhgxTNjWY7X0zBZgqg4BbxMcXSxn5wdYKJrbREv2Be5c1QiS9HOPN9YCy47tPuyBlLUQv9r9XBj9zxuzpDU1Gf_U9e_X-GdzeK-znRxNDvp1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛مدیرعامل باشگاه پرسپولیس قصد داره که ظرف روزهای آینده با امید عالیشاه کاپیتان 34 ساله سرخ پوشان جلسه برگزار کنه تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/25430" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25429">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi1qFi5NPtQNL8jN0ao0sqmK7yugCS0ZaBZZAGTgAZKbW6hppXJtvLfEkEEERPdku2GYdO3-k1mVx1PXHR63VzUco1hAwVksuIW_PyNbt5sGVXUUOg_NnlLMhkrxK6QOBC4KdZImznHvpCovOahdNBxwbcd-P8-9ISItDPsOZitcsVQzweDMeByu6GZRlQ1GyFl3Xav2uhpmSfuOoE519ZfVg87ALKUWQyyFQE7hni98UhKLTJmYrMS_n97bJZe4Ltce0uEXx_J6me5ZErNdw09NH0u_46AOWVkqCGUcXDXNzNYzj6gqpKY5iBoPJBseXmxjATAiOiR9y3EUbfEOAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/25429" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25428">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m83TIinvhdBIIYLJT7-BCiqG3J-s-yVJtiY8-ODzaWnXUVYeAGlyRfv7Nc13FzN-KIdcB0KeJr4s7plDa74bozmuxtCiUJamcFmvJV4N1L8IlZXs-wEqL3DmFcqjhMj5zbkQa9r01FW_tClDYzurb3D_fYINcAOJwqp6BZWEYnyAt_-KbBFwI9kEohnYSbgh5XLKIcIcfjXSH3bTV3iFgCAB-dRMs0MlLu1jTSi_DQW0qcQz-sf2lC8eBS4wvTMHf8o9WeOS5Xsq46N7aCrLIGdgOy8llGZLIR2BS1KqwzCarq0D610-YRHo8FPBbdm0oddhlW2C12fxdO_t4sWlGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/25428" target="_blank">📅 13:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25427">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vg9ELHzpF9cxq3SSQmX_rdj2lUT9Ux5Vx3p_tkVPmKQjGwh6te6dxDLLWCU6XKPSV-2wSp-6IQQnqrzyvAAq0n5tO7h_LUWixOxD2Mqt-Fkd4_IH0inUohSbyiOVBjcnuWsE_ft8Mw8OcwMfFI5BYsuDBHK2leli27wrhPsj1BQN7ida1IBdNZCV31oQ_KO6t8NnuTqMUAvGyWQR10lTSu12HvhboZw55PDsG3VaCvtvP7ghUOoVU2dfnTyPqTbYKGYDCo6L-48qHS8FeGIARNiismcwGOh58eq5RvdE8n0cycB8fKRj-VULG3OXyu8JwzMZW5JmTVpXpnfmrppI1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛
باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/25427" target="_blank">📅 12:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25426">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jfa97lGFEDUmhkFGsDXDBQU85ta5icewxOT1aK8jFTd9Z2IVZAnFGS0iQfw9mxdYjo42HAPNyel0-vFXJHluR0ukc1FM29Hm8K8jrdP7EnSaRMg8gxklPoPuBTEyTYj2uq2ef6eU17bZbYiJr6Kylv3S0I5Ug1p5aNNliliwSRGR76uh8FfXclIDGtSFdajGLvUOQanPe__3AT29Bzk4FMsQVwQ4Uan_NbYmqRhITXIQbDzlaGgLxt3_J4abkTcbJBeyA68c6SvQUKl-PbvbfAfUq1loJ2UN5oULZvCYHSg_jAhece11ojXe9wc0ec8JNIw_ZgKe2vbO8SQd6G0xmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/25426" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25425">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06676f902.mp4?token=aO4LCMdOdR_DIUlsiTW7V3P6E2mh2ZYhB0EAN7yDNTbn65MuC4qQo-ojcNeYh7r8pwMciCp3LJxFgM-s4iy1Mq2-YHJCBR6qiF7_TrI5rOCWf24XlSlz0FGrR2KXTy2ygPQBJUb6YpQJCh5gIOv38k5nlc1dvHjNi-kkSwTE2StQeybY1V60dBJMowmKZtZ2xG9_oomMxHT-tV2rhQLsqNd3ShtOfVQ3ZpYY4-RC0zH_H76gC9Z7dDnV5DzRAnHM9Xa2afrJJNYJk26Kk8zW315M8W0Xxfr_xttZosdMzK4SovtVnvtdh6V6yq1cH_lOvHOf2q7Tb8AX84A0Db30iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06676f902.mp4?token=aO4LCMdOdR_DIUlsiTW7V3P6E2mh2ZYhB0EAN7yDNTbn65MuC4qQo-ojcNeYh7r8pwMciCp3LJxFgM-s4iy1Mq2-YHJCBR6qiF7_TrI5rOCWf24XlSlz0FGrR2KXTy2ygPQBJUb6YpQJCh5gIOv38k5nlc1dvHjNi-kkSwTE2StQeybY1V60dBJMowmKZtZ2xG9_oomMxHT-tV2rhQLsqNd3ShtOfVQ3ZpYY4-RC0zH_H76gC9Z7dDnV5DzRAnHM9Xa2afrJJNYJk26Kk8zW315M8W0Xxfr_xttZosdMzK4SovtVnvtdh6V6yq1cH_lOvHOf2q7Tb8AX84A0Db30iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌باشگاه‌رئال‌مادرید به این شکل از کیت اول این تیم در فصل جدید رقابت‌ها رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25425" target="_blank">📅 11:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25424">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6gTrlnCYnlBVz2PZYIbM7vK3SOSUFwI07EbwVmLxHPJi8cSoZwH42k8O8V1IPEyi69sZthk22jWjKTBC_bC3-OzuV3XjZ5dmFlSzaZII96u3uT-1Mt4BMWT-8a37KezYvhSB9bM1_LFlFoLNnR5ORRqJkx4pM7NUdNUI4zKCiNsOujWiGs7Sq9kjBaPUrbm5R2EA6jXOdcrI9p87t-mYcnTHkEJyIBbm48Qx2svcYBjLZgO3xsi2cVXsjSMAegXG8_5lnci99XVQvj4gyTQT7SftTQ3yUI4Q82x8gGTGPTsgTj28PoEp359wPENkL25E1BWQ-ywNNup0JemTow-GFqo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6gTrlnCYnlBVz2PZYIbM7vK3SOSUFwI07EbwVmLxHPJi8cSoZwH42k8O8V1IPEyi69sZthk22jWjKTBC_bC3-OzuV3XjZ5dmFlSzaZII96u3uT-1Mt4BMWT-8a37KezYvhSB9bM1_LFlFoLNnR5ORRqJkx4pM7NUdNUI4zKCiNsOujWiGs7Sq9kjBaPUrbm5R2EA6jXOdcrI9p87t-mYcnTHkEJyIBbm48Qx2svcYBjLZgO3xsi2cVXsjSMAegXG8_5lnci99XVQvj4gyTQT7SftTQ3yUI4Q82x8gGTGPTsgTj28PoEp359wPENkL25E1BWQ-ywNNup0JemTow-GFqo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25424" target="_blank">📅 11:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25423">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDSW3-7qmipyMzIG_lx0YpeQpKg7OfJ0iZ7uAy0UfaD-GcjBFZarEbiIymFFrdXF4glene0nDuVpr2mVk60qyiGY_eNKwv9aSnoR7yr68E-ZmyA3pJZ5PZgVcSo6SANSJdPAtDaZt54IbZDrdjBLo-WDekrRioNPqe9KBoG2Ndo3cHzcDPCquGPa0xgC8obm5n9ePdgmiSKj4BV-DIHtl5AzykrEq0MCtRv7WgTarrhVQ6oGmvyh1pGCFRL8gCsILQwXctvRNTKr31UwS8P6j45yCz3LI0PMUQ2xdxhqX7ft8SG5zlyXyMBsFfb7i7vwURU83kvEDNJqrdWcnZdfPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25423" target="_blank">📅 11:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25422">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu7Wz2898xkIBpegUNhuocBpFt2YH_cEVU7GMKLTHW28ztiHMW0lFL0lnSZL0FBdsCj2_mNGNWcbzR0vjRm0ymYjWKeDv1YtJx40ga9Nrn8r_UDW0jesfuwDTfhBXmfZaY-4u3Sn6c11BqzQjHA78tG_txaF2CHlW9J-knnhb2lL_-j-42KWAC7Ol1oGELRE7rKdoIS_AZcfoQ_zXcf4KRtZrUG1CZy8_0xnicVOixm_lYVQUOCEONhwRkiAUNxofbuzTCfdGPxQqwV5QptdYPurhD7FMbVyVh_c5mo7m94mgSyJNPU0K9xyJAAaQ01Xit053M4zRsMVVF5gH0jo0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب صداوسیما از تقلید از ویژه برنامه عادل؛ ناینگولان بازیکن سابق رم و بلژیک رو آورده باهاش مصاحبه می‌کنه بعد ناینگولان نمیدونه اینجا ایرانه همش از کلمه‌هاه‌فاکینگ، اوه شت استفاده میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25422" target="_blank">📅 11:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25420">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=G9eOBEQNxH4X-P6vEFaQ9sRUa6NFYiNcU3jr3IIPFO6CGg7etUQ4WaRsztC4khorpUSplPup160WuqwGLdRnmoviLOYzZrwFinOpsAtwxdrzHK0js7Gt2IgC6Hh-fuiseiDMsHh_NMcYOqsjnIa0Z_8z2CioQ6Iq9u9T2gSVQi9bFTJtyzIiggtz-zJXWurRiczNkC90-ahmh8ltx6tDoG3zP7S6mpYYzjX7W1b-NOOyeGAr0si6Ur7alHS60xqzwIj2DoSz06qoHfgQVybN5_kCw4ltczqvMkq8O3rxoZCkHPIHa39NPS4LabK3n-hguc7St65W-kBDsrnju4L82w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=G9eOBEQNxH4X-P6vEFaQ9sRUa6NFYiNcU3jr3IIPFO6CGg7etUQ4WaRsztC4khorpUSplPup160WuqwGLdRnmoviLOYzZrwFinOpsAtwxdrzHK0js7Gt2IgC6Hh-fuiseiDMsHh_NMcYOqsjnIa0Z_8z2CioQ6Iq9u9T2gSVQi9bFTJtyzIiggtz-zJXWurRiczNkC90-ahmh8ltx6tDoG3zP7S6mpYYzjX7W1b-NOOyeGAr0si6Ur7alHS60xqzwIj2DoSz06qoHfgQVybN5_kCw4ltczqvMkq8O3rxoZCkHPIHa39NPS4LabK3n-hguc7St65W-kBDsrnju4L82w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25420" target="_blank">📅 10:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25419">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu6XFIQ1oKkXASsjAPbIi5hCAWfABZ34L9JISH-hnYGWWFoQrZ3x4jz2XgPc7yNLfjZ7akraVVvwcxXtdq4_m3naHKEE0rsogln_PIADmHsXlJ0mAksyYHqpZmmats1InFFRkSE2z1E-O_5OJUIcpXC-ydk1t8snEySvSci0RciBiK6zc5zM0DU7IUEJJ0vCO7lx1akwSh8VZdgh_GqR95M1vJTBluS1arYB5vkQB7HlKqpfcebdITyHlLDeU-uZUe_B-Dfd4VMZPaaMDwHbJgkZTkKHBKT6a6BfeBuNxq7VkDrtcRNln1bmtNFlfjRkkYUFakSqag3FBKWyE3D_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛دیمارتزیو خبرنگار ایتالیایی: فران تورس ستاره اسپانیایی بارسلونا برای عقد قراردادی پنج ساله با پاری‌سن‌ژرمن به توافق شخصی رسیده است و تنها توافق با باشگاه بارسا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25419" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25418">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdL2097y-Q1lOEhQya_kygl3FwmVrwbnNoHs4yZa07-OHesMqx48uNu_bWwEMANpWdVNNry--UUZ-mP4Pal3nAjDqscM8yDMxX3OFOgxs0LIpmMkg1JqrN4JJA1A0PTHQ4dPviW3pyCIQS4k4AsHPwRpwafTnG6Mwl58y8y6XNwHFeC2t2Un-OyXWo94r-OxR-vwYANeO121VwGElWfnfIYqm6QVcTGskWBhz5t36YyFzIvBqXOzsMD3eXlSN4UVLtxYrsnLoxdvmvvkNm4GSo9yy773PUHp87yCNr6rnQ0Rw08ppo2hNFwDq5CO8XCi-Y8NloKc8rOL7yOW2Hkczg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25418" target="_blank">📅 10:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25417">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf40WH2GQZmuSCfmrRjVmAxfDsZQZCwVeFNJWLmt1NU15fjvzWMve1jSFVS-P0ZuWnO63OZjBmi2420_BJIqZIjgC6YC9w5GP-0fhklwhgvRidFM-DzQDC7MolookGGz1zAbAM-JXZHhS6eslCsLT4F-5mgo_QGeWeh_BW6dw7nfPZgm75budMuZAZ_3-e9dWl5Rw87Uynb5e9YxRfwMW86E0vuSATNTY9Lbb8JNIVX9m416rlr4BAnSQLe7k-nJU1DDSveRU4RHyrcbeDXOA0fTzJWZ2sQ_IoZ6cCxk8TDl-wCcvZmw1dKbjawjoCtyN-Upfj7pTpS7M0gAuks26dsfc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf40WH2GQZmuSCfmrRjVmAxfDsZQZCwVeFNJWLmt1NU15fjvzWMve1jSFVS-P0ZuWnO63OZjBmi2420_BJIqZIjgC6YC9w5GP-0fhklwhgvRidFM-DzQDC7MolookGGz1zAbAM-JXZHhS6eslCsLT4F-5mgo_QGeWeh_BW6dw7nfPZgm75budMuZAZ_3-e9dWl5Rw87Uynb5e9YxRfwMW86E0vuSATNTY9Lbb8JNIVX9m416rlr4BAnSQLe7k-nJU1DDSveRU4RHyrcbeDXOA0fTzJWZ2sQ_IoZ6cCxk8TDl-wCcvZmw1dKbjawjoCtyN-Upfj7pTpS7M0gAuks26dsfc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های‌تامل‌برانگیز این داداشمون راجب حذف تیم‌ملی‌پرتغال از جام جهانی؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25417" target="_blank">📅 10:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25416">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8oZwv9Tkts9WkNEHzqQ6CpAE8gvnsflN2pKCYtpLjW-63pyfzU5EmBW6b5GbTKnqCtUAO9XM29Us0pshfsBlsm2fSen_JKDJg5MRepJpgozIXA1VgudNlKsSBOy2jPazC4HkzPsj6PPhUohd6IRjc1DWYpG3t7hpggLOXxsDzBJTjtc1j7sAhdQlzqEEDAVuQ9-K7LjAYd90crKL_D4xQrFF2969GnYMHo5nCvxwaGCBjL73hwPEZlENdIxbWbmrHwU2mBIStTJUkKov68sNevwG8ZjncOm9kAc6JPP8hjPG6N9p5KFLWn3u4Ytls2xP1Es87zXgRkvm9nhzHp8AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
کریم باقری مربی تیم پرسپولیس: بالاخره وحید هاشمیان هم رفتنی شد اما این رفتاری که با او شد در شان و شخصیت باشگاه پرسپولیس نبود. بهتر بود در دیدارباتراکتورهم هاشمیان میموند و با شروع فیفادی سرمربی جدید میومد. الان وضعیت نیمکت تیم برای بازی با تراکتور مشخص…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25416" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25415">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHGcg19nVXZi9-PdGwWnfVE74E_u_slWoLrJN-Y0TWJIC2f46xjAn_zKaqmZBDBLB1EhkvOyEThuYr3kWZuBeK_XArKoskA3SexZr3sGb9Bnp801Cs0fclSInCNDkP5jIiAinK2lHl7SoB_Mc1_Vq5HMw-M2eDcbuBzRODVJa1K2usXWmg9x1ZRu7eLh17IpQSA7PnT9Rnj26OAvzXDK4qUvIJafRF920dRE_vpKWL06a82yn6AvcDfBrj7xvu98bCsn3Qn7q8eLEbdPbsl1sLB2RrGYN73sI4TiXp_u3A751l1noR2MGKgJWk6lTu_R-ud8OJJL3Ftf4O717jurfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت
:
سال‌ها بعداز این جام جهانی مثل 2006 کلی کلیپ میسازن که‌چطوری‌این‌همه ستاره با هم تو یه جام بودند. تنها مشکل این جام ساعت بازیا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25415" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25414">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RT-_935UgqKj0Y4j6xwVMLoen_wwv-ob7jr-IcCLBwOlwMnUQw4vFVgzZo6n-z9TBsxYFE3z0v3BCKTx2qydSL-N3IVtMi5yK2l_RAF-H31YRb0UDmTJb__ZDBEnPasmol1YurJVwwPFCRdlPVu20D0f7C8Z1Npa-6vbNsdsEj_S4suWzYY6Sn57J68DF2PB6aS_HyDCZc11IhNrsvHKZi0Zm6bEiYLKGLWj2uWx4oSHetWApWbHHPf8memKeXJVi-BS2DBQBfp7QBSSyKzyhDWjPBWZeMbFfxgz-nkdCw2manJCqA185zvQEeEEIu0rQbbUfjjDIEWI8M40GINxrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
بدون‌ریسک‌جذاب‌ترین‌مسابقه‌ی UFC را با بیمه ی 100% ی وینرو مسابقات مهم را پیشبینی کنید.
🥊
بازگشت مک گرگور به قفس
🥊
مسابقه جذاب UFC
🥊
مگ گروگر
🇮🇪
✖️
🇺🇸
هالوی
⏰
ساعت 06:00
✅
1میلیون‌تومان‌روی‌برد کانر مک گروگر پیشبینی ثبت کنید در صورت پیشبینی درست 2.5 میلیون تومان برنده شوید ، در صورت پیش بینی اشتباه کل مبلیغ را از وینرو هدیه بگیرید.
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr20
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25414" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25413">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJFsXlzqt_8u-YxUUAIQ1tf4YqRyCNbAbYckNLAn9YNL61MWu2I7Pp2xZKLSVpTCjhqmnc-jY7TFniCXJ4cOY24Bg5K3muHtdaxoDUPPHY8U12_G3zCwK2Noy9gNYan1QzyG_LUmF3HQZTKqU8QOTIK39CkUrEOcl-ZdeHJxRpE-PaP2cKSrZonkhQtVsWv20X5TqQy_X3A31GN8Ktj7MlQ3wKWCjsDlC0bTdqXMXb0D1YlhIpFFnucAGVsUkzyUPvZvmmKBMLOlkGySbpcP79EHHeOxjhHee8wJ2rRIUIVEVenRX6YvG7W1MWf6RFEyu_EIwtmYsrEJE618ZsNRcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ 5 سال پیش در‌چنین‌روزی
؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25413" target="_blank">📅 09:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25412">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=q5OIJr7mBhmi17SFWpoBAwqzdjceFXTx47Od5ljXH5KPitqSw0uz0gD4b8Ljwrn8qrPtTS76nzl3ZPepZjDJAYAojo1s5RV9XMqMFclc4qmRdIosBU0IEwklvVzt0pDj_Rig3W9yzuGWEoCcuO-Q1suqy1gahfeZ7zi4XCC_Al5zeKQzkKFDRob_Mx2i7f-v3s8UFvgDb8-6FRbHneK_KdjVEIQKVJKdOZGx8lZDgNLVCyg-ux0HIu72hFwvtDoGaPbI6FtbbM4s1WQDBFfxMVaWMG8oPmcO3rxhT493tbgyRWI4Lwh531_AVb7PDoyGRP81sVnPmiO5bWRdXanGVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=q5OIJr7mBhmi17SFWpoBAwqzdjceFXTx47Od5ljXH5KPitqSw0uz0gD4b8Ljwrn8qrPtTS76nzl3ZPepZjDJAYAojo1s5RV9XMqMFclc4qmRdIosBU0IEwklvVzt0pDj_Rig3W9yzuGWEoCcuO-Q1suqy1gahfeZ7zi4XCC_Al5zeKQzkKFDRob_Mx2i7f-v3s8UFvgDb8-6FRbHneK_KdjVEIQKVJKdOZGx8lZDgNLVCyg-ux0HIu72hFwvtDoGaPbI6FtbbM4s1WQDBFfxMVaWMG8oPmcO3rxhT493tbgyRWI4Lwh531_AVb7PDoyGRP81sVnPmiO5bWRdXanGVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آدرس خونه و محل سکونت بعضی از بازیکنان مطرح‌فوتبال‌ایران؛ هرکدوم از اینایی که گفته خونه‌ هاشون کمتر از متری 500 میلیون تومان نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25412" target="_blank">📅 08:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25411">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=q9gxOG4m5DWb5NofCDb8AqOOUCI7Atb9hOEMzfhJiyl1PWCtVT2V21Q2ql6DNPAoDYe1GkoDOx0PGEks4HdLA5BqtgDSMTkWu45AWz3QCA2-VcxY3N6je19NzcQrjUSX7txo1xdKZJnYt65n-4TZm2XDG4LzfMEdboyh9d-Sr-CbWUl0L5OZL6DcaV3F5pvg6NdusqPqEaU9sP1oaaUAJaDTrCKEHDlGEhdp1SBdCFAZYuF6L8gTFiZFgd2ot9nnHII2uMUUuBvnnIyLvVT9sfU5X5s_XXuCKCLKB92rI4n3oCYQpOV97y8FWeiZxB2CqzX4oMnTGfdNg_gr1y_oPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=q9gxOG4m5DWb5NofCDb8AqOOUCI7Atb9hOEMzfhJiyl1PWCtVT2V21Q2ql6DNPAoDYe1GkoDOx0PGEks4HdLA5BqtgDSMTkWu45AWz3QCA2-VcxY3N6je19NzcQrjUSX7txo1xdKZJnYt65n-4TZm2XDG4LzfMEdboyh9d-Sr-CbWUl0L5OZL6DcaV3F5pvg6NdusqPqEaU9sP1oaaUAJaDTrCKEHDlGEhdp1SBdCFAZYuF6L8gTFiZFgd2ot9nnHII2uMUUuBvnnIyLvVT9sfU5X5s_XXuCKCLKB92rI4n3oCYQpOV97y8FWeiZxB2CqzX4oMnTGfdNg_gr1y_oPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دابسمش‌بسیارجذاب‌ازگفتگو اخیر جواد خیابانی و خداداد عزیزی در ویژه برنامه جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25411" target="_blank">📅 08:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25410">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQWarg_O8X5JmVD0XbbTPZ-8ZLfhvxQQJQiqspc6QH5R8MqvkdZZ9D2AsBNpzI-64pFrgag14qP9k1yecFzJ954vxvXdPuUzS3vn3xu63jSBSBDUrs2eu0j3aF7ndKA4564FT4nNilZZIURrH7TPb9ir4mm6UXemcV_21T-XTwiSa-vDBR0LPN30B4_B7aQR9U0fiZpRTt9KIOgFCd6Lb9rnw55j4bOLl73Kdt1LgVC6qjjZe_71fvNElSTb5PlxRE7-h3oTeDZGJb_4wI44Hv-XGyQTCkeKivJPB9WaeAli_cs3crWepbL57A88Z5wOcLsIwYxnQQK8yfcac32LXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25410" target="_blank">📅 03:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WluyItEvSk3K_isSejg-IEgPZ4kHEmYktlcm3z0nWYkEph1Kt6_ewaARO33S8cjr_EhZyGBLqPGd5z6KyAF2C4pZ_fZubxyW1QjsQm63jk7LsboxvQrtGZLV8Z3hj1LGwFBqvdIZvhSx2gIXTQ7C--kYpA2t-uqi-K6Vk37BiK1gPHUlh0I5YMo99cNXYf6y6rwJiuuEfYDt_QgMAbFfq5lsV2dSvbSGdEcxLwG3LjxJvP9SjXcgf8rq-cNIfDG8orxLXmKVkXCTagc2KwsvCcZTDyAmJSgYIRlgzzyUd84Y3jXFA186CrIZMbrJI1gGn2sIelFPwfGd2c_HRwjasA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#نقل‌وانتقالات|نشریه آاس اسپانیا: بردلی بارکولا ستاره تیم ملی فرانسه تصمیم نهایی‌ اش رو برای پیوستن به بارسا گرفته و درصورتیکه لاپورتا با ناصرالخلیفی به‌توافق برسد این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25409" target="_blank">📅 02:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25407">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=pPF-imhS_XR1tFjSRfytdVk3Osb-ogLHESsTCTrgY7vgdntqWuoEl6Iq8FvmZzov9Gib8rKpLqA2VaucdyWvElvCVcwo4dkJ5XyEQ6PW7JYZehMzRYJ1HwgpD9SPXbodIO24XYbAag94fJLGJCls-oHP48BvjyFbfrl8d0qN7UNnbKXsmSg37cTSA4QnORc20Dxe9QA3UmS4Q5r_uXo8JsarS2TQymPwg5Q9JAdo9nYpZ3g4FQQTNw6CU8nfJGg5KJ2KCOE8pm-V-oKSuB1kwRPlK-8YLZw4WpI4PYhjF4FhY1JbCgv5cdLVYiinqofc8MRhazTb6rAHy7EBwqujPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=pPF-imhS_XR1tFjSRfytdVk3Osb-ogLHESsTCTrgY7vgdntqWuoEl6Iq8FvmZzov9Gib8rKpLqA2VaucdyWvElvCVcwo4dkJ5XyEQ6PW7JYZehMzRYJ1HwgpD9SPXbodIO24XYbAag94fJLGJCls-oHP48BvjyFbfrl8d0qN7UNnbKXsmSg37cTSA4QnORc20Dxe9QA3UmS4Q5r_uXo8JsarS2TQymPwg5Q9JAdo9nYpZ3g4FQQTNw6CU8nfJGg5KJ2KCOE8pm-V-oKSuB1kwRPlK-8YLZw4WpI4PYhjF4FhY1JbCgv5cdLVYiinqofc8MRhazTb6rAHy7EBwqujPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25407" target="_blank">📅 01:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25406">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJLnxZGOkS4OUM5a5WWYfcAHc6TEYpC1cVcmk-i6o5L7l0gEYPmsawZ9c6xbkbDw8-woJv5jV36dfBXSlpDUyjIPFmIXItYyv3Np-OfWn5hFkAWUZKPOIXBg5_p5Wa_d2diH2sDRbSxkto_uKM94ZFSWJ4I_ZrglLs_f_jaaLfy2Reu-rQgUAlWzKT3a1cOugz5eCRCuroNxY6Hz_HNgXF9X8OZsuy8Sq-DwjbdFjUPJddWv8fT7da3k9Nh5b9U4sSwGmUjJirm_djM33XyYgU4-yiw3h-dBu-5RN4M5E6ekXiOhcx2dxgTcrv5hg0G1v2inOeYG-HXN1hE5HwUU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25406" target="_blank">📅 01:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25405">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iqk4lKIG-g2dmHFaqSNV6OMC7udbRRxlZHp4nkvboxppeXdz6WiC_8VdPNYilB08OsAaqnFpJI-8FoBBGJ834tGkLTlIKI6KCeU-D0ZRhdUmJ_fXrP9jzxq9FD4k9v2m1IWtoBnMEeFnFO3DI4UdOMmWwqGGBjjnH3s8F05KQZNEd_8bVRh2YW1ae5J3FN_40Snh1aivKjXxiBnLThwJVbExAfD_jMSuMdpXHJhbp5QA96pIyK4u_UT8yKYAJS-Sae3UvOtc6h4nr4AxXaVA2Dlf6Dm9E7FjrwDFtiO6EE-vfHUTsE3zjLhWqSNbxcpOeNEOKOn7v3kD9izC79CobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25405" target="_blank">📅 01:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25404">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTl7sswmE-CCfbwJC60Z4aX8nUT6gzrf09gsFsV7pjTfBA6h3zQl2VSBdy1BfYJ5ESmNYlYsbOii30xcuSi3RMKPjC7Q4q-4W34aebQ5WvVIQGqsT8_4JOa3yH8A2tPm1CodT8-vh5OBwqgds3pAXZdMoVFyDS089y-2LccO1Y3B_G09XGKKREHPI4hyJdHNsKiXRLWEhPvZCavkhk24Qw6ZColLs0pqm-oirHteXktbvEPv-7YUH5gsfXVwBomR81K3hAq0789JETyyH37IKRt1DM4SoHYlERcNd3loz-ZZ54kKJgoA0ERtNcPBEYmpSty8maja5HCGBKE7wcPb6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛
از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25404" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25403">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjDuDx_QXHVaQvF3gp3LaJzAnowD0LgSalyN9IeKg47jAJq8IImgKVF1TmKP-NbYdT_t8IngYf9OPyiPfGdIOkpKHpJ2xb7-MEin9i_DGK9v8WzeMO6DDHxNOx7NAquMuRQNv9ze18cNry0JRXCBQToaP88KsNJM971ad1inE9OAv98Bx_6MQqlXr9G-i-4bM-vUibwuIYfPKLrIJTiXc9scJqYp6ujlzfqhnMX1FgNd6V8ljhYBxInqZdalNU0PXcJ6_BPw37N2AEH20hZtxgWIv3M1kZbI3dh-C4lVqvQ0xzEke07nXFitrJ4TCX9iHGOXSTxyqaWlGNeDe_y0fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دیدار‌ دیروز؛
سومین صعود تاریخ لاروخا به‌نیمه‌نهایی جام‌جهانی با گلزنی مجدد میکل مرینو
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25403" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25401">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRL9lbdaSI1cEFbNjCsPxp642PfutWPUc-R8el1cOtkVMQkFo52_QvW1YOrW788XrUaV-KLGy9iBkcqq8KSW-2XsoBrdzLXXzunWLpzto4p7qJ7AXwuRiOJp9D3WhbFL1MY1G0U6mnZoU7CLC9LUhNxaw7_mQeeQlVUWmtGJ496IIeCooC8nheOSe1ymfgKVP7ZGznfnfvGs8Xk-yvfUKej7frt0qRZIcpXY2Rkyw-iN1AdWyUhc_7_W4xF2h6gg94FePByPhOsHiLq6ny0jBZh65SJEzo86wAkxccdusNveonQSBbkbH9-xCd6FGyI_zUw8CU-ih0QAsE6ELJdYuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/25401" target="_blank">📅 00:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25400">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AApilATnLRxxB4UdomS7RZa4pgMOi0bqceBg8vVkVHtabsx-wfp1lz573PTCfdJUPoODkUANLlAFCf0ApU9FhmY7Bo298jbwchdwHyvYEjVoVAPNqRCy_fxXNl7nDOJSFzzDuEF8mMmbjKUGfrVIwLkhtDCI-zIrpYIjhmRQzwOjzvdpCu5He6CC0dO4IJLUStyoVMWCrndgxirGiCoO2AP-EEfxV2UswecY8EDqOGNhtgDFibcafDNz84tqXtiIgotthes3Agtdkagn9d8eC89eHNiT9VyAA3SmgNyX-Ec9tdkMi8O6p8uGZVDl--pUO7i8euvLUrjdrbt2tOrpng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دو تیم اسپانیا
🆚
بلژیک؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25400" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25399">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iL4S0_FejAlcnBX4lG3FLwlZyYyCDvVNemBju8I1hFUwALYrc148zOpmlzSHAMQ1cIHt6HvO25YSDQClXvG3_LxWZNuunY3E5Qmh79aPEuimzVGSuQMfPJlblWOS6kF9QPwt0xb6ZfrAiVqYXeyMDfIAYctiL8KUZgyqMBK_1UyKtDb6fat2INqCQjBEyrM2uYi2ksY5gk5iiYelRtbVNtFd1PiUivvZlcCqDq5w5gMG_KjBEoE4QK5bumJXnGMbtuBRbM79XREu_oQDoZ0O039RhDYR48xEL-rBU6uGICJCOmOrtNFhROHmX6tKMnvW0Zf3kzZbss5XDlUGuEMvGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25399" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25398">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mtg3Kil6sQhDDbMsepauqQaQCzNtO2cczSsC6iyS-wYvpyFe3Fm63wEgH5j8mg-icjVcey0N_EKinUxdHlnHyKNITfF06Cd4MZB0RxzfK86e87TWfTfokbINu6MFQhD-uOgMJsGj-mTFRE7cCWJO348jsTkrEzSyTzc52hPYZdsifLOKx27nRIkVBJv1RkDSGVP0mDHQDiO6__hMHbmJpovhGaXhfZW2katHUmf4_o_4gOSQ-B47eA2cpgOsyJlob6LR2qlrCLgimD6T6yOfogvoT3PLgZtUFYen9_N5EqkutejX6S0XR6QpF_H4twF72xV2l24Md3ZzJNa9FBFVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛
صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25398" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25397">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKx7cqEOQtczTeqn43dSlrgWUuNyGXBzjFKEZFdzHUyA2UMzHz9T-1Q8oVj5PUtDu8lLvBmF--2t7SHXRroDei1lUZiofajMH-_CCZ8qcvlY-NLeoaEKz1_jKhMNq0SPAUB9wigPgTKdy2DghXJjkgWzKj9BSzCxfq59TqHmGlWtbrKl3z-oH_guP_vAYRJwaL5WrNK5yVeo-mwwqONrr5u7hBGpSIGlillCJxx5R0ApTglJMhuw2R2Se1qDNr59WL0shoxVZP7PVN7HhCFR8B9aM_s4PndkdDJzwV8N69eHAcS68cZDb4vM4SdOjaPX8yrWLt4dBfwpcq65T-h7Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25397" target="_blank">📅 00:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25396">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndqQ9imSJ1dVHsy4BHOBmfGh52gb1wER99d_qMZBXUM_JLcqqaK7bBLa_zX1FqmIbYnqrTmLPDI0GMs9Rl96af-yly6QXAAX1oNABqW_yUKi4ZBFAiC5BVliUoSSTviR8bTHiThb4vAFfQWY99YrMglA-KMYkavFllxpDZ5tCIsvEKQ75XKsT8DJvIxQ22aKQ3Ahh5lSOHytKZ5c9TQC-uiYewq8XRWiV6UCal0KDA8Ujq27Qxw-67y80JhgcNFhb2kXNIE41GikHk7YMk2r_Akj0slRlUtmbIkZVT83KqRU-bYoBR9j2e3C5s_nWfsPajy0boSGgqVy8M_gMW4IGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25396" target="_blank">📅 00:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25395">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTk4D_0Z81XMHpmGa7FgFiNAn1CA1mhNwuQUcPOB1trHJV3F4jHoRsWAMBf8oU-Hu9i5rWJy18WOsDYi60CWdjnHNzEvyXUMWDWSn9fQsb44eV6FDmbIlO3e5v5yRqxZjxHyPmCM_WvDyd4H3h-ljZ6_KbfXCmqDf-9Ix1V3DOof4MSJWiE30MjV8IUTIahiP7932w3qU_HRIlqGFFs5_oBrDLdfKzbhdWklqMDJbNGWoce3L20e1zq3LkK12aXong4aTBGtfKP5wG_UL05bJDW9CvTW0_U28I7xjzSGWi_YL-AGrZrmjZgzyzjZNRPD4B2kD_tk2QP_O4_D8ijesw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/25395" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25394">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjYxpk1ml4XlgjHy-7eU4vneTBL9XHWpsq633avsIoPC-VR7SEH4v_L1WIkCXJL5zXaQTrheHAbgASUid4_DIz6bf6uKK0MSW5XPaJm5hqbx7ePMoS4TicH0oWddWAoOUen32zrkYuowlP-c_YTaCO6S0wv7Eknjhv6P2SAFLg3--BiYrlyitJKPpEPgsauy3JNnoQXhrsHP4Ai8S0xs5AH7veI5BcsKxFP2YScmDEtGJsivbfFxMaSjs9yrPR3yHxunvZUVTqZz0CcMYsXRPtTtYvBNFyTnh21qkRT65y8qjN5CGFbaxHsvJxUS4eBLBpKWmokXGs-Y7Aiw-KvUNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/25394" target="_blank">📅 23:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25392">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrZco7pn-x421rrbnH0wQP1wcolIgr-aq4i7vSy4PUfI12FW5r3PyDNibLjf2OdsqvSDimGl_LyUgAOOCeozxjvW22AOR1c58QvTMLeA5wO5_Ly5Hl9pSN93-ZWvm3GryAMWaVq8fzavhUafsQXafo1F4VeU7GCl0cix_oIMMNOK8h7uerMRq9bZlg3RefRG5pVQdylSo4hiygVrUMiCs2WddMvmbbhEthojW3riufw02nNJ3QrSWKcULfWGsD9-A2qh0IXMC4Rzc_rLfm3WfcU6e7FjWahMeihSuQbozBRAjJ6YjVkD51AJy3EWv5d32f2emd0hf-fuI2w6MehLDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nb5n_ZOmAJk6EOhvPK5n_3FFZTl11CIvP7g1lnEAk-vS2nPBA6T2yxN4J-7grUnBw0aDN7tz1RhlQ_0mf-XKK1QNF9jzsVlW6gOnX3g9x5_KslYJuQ8YLOQG99w3rroGak46zqNnRz5vgZuW7Vioq6FnxEuD3UFNawt7Q5xDGC5JiySmyKfRoWkJhUyzN6ZEYzghfgy35hNulv8rb1DBDMrjvAp06p9KiIt7Z3b5dAEx3iq1nTbON7s1qsPhKELN-KuT9b1buFyae7m2Urk5AoFeIQ9eFDiDxiPmdB5dKPF1PsKAisQwn7bxcXpQ49NPqeUOvzND124Qi0s_JToC4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/25392" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25391">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tF0L_HNBZwa1HMM7rvc8XANJHj6nwdYpuSoEcsxiAJ-U0Mu4Z9NbiMaLBD2RQeQ7HYymm6B6NaQMRvLSWcgKpM5GsypmjDLtrNT0i9p27lrh2lJU6ZdL5DycMm2Q4FC02uzToDOwmXfWsRM4LtQmRSSvE2JTaBs7-uyuMWreSYIgL615Ki1T318eahdPh9QZdmAMRw5UPxwjFzWScGTAoMAv5AmPW4gnQpCmN95QUVS0-G2eud76WZ2H8krMpuc_F3CwhE8BpFntdnc-VG9xBJeJGWhwBGFtMu4bPlLzd5n8TkCP8_29S0_vLctDxe-pbL013grA7yQ05vX6YIQVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/25391" target="_blank">📅 22:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25390">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxWpCsjrAxI1bYNWSg8IzAi5bU5MF8KlOot1hDAr0jwQ9S2KHPdzm2TeDWUHc8JUAj3Vv8yCG2RkVr4O6UYFPuqK5dC3Y7Y96cnSfRFnwGnikXWG3gKCOPPO26PFZmEWY-aA7tC_XgnLNSsoCx2lD0jeh2_hRguBOIsg5kJWwaHb4Pbk6CNwI1jaPMRIZ-IjtcQNMNxnOm0YQdUQ5WkIEFlVZdleTkxURBKlSeV01MKeiz8h4B5uP9mfpn_kd_CJTU96N4cwwVLS2AM1K5PF2BMCcEkUuL8uEJs4MtNs5YtX-1PjODsHUdFoIBSDNScVu2w3q_LYk8ZTxsiOhTFF7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/25390" target="_blank">📅 22:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25389">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ize3kEa_n2ODDN715TbZ4kNme4j1C5kqiEiF5_msDaq7_nSJovoXvuswxBFFvFXS_BEs26YNtvJ_JHyxwgAWuOy19uS202Nt0R3NIL0tBx-jboBv7lShX4Xe0vPqXlblXGwjjHxuoeB5ahUcfWFLQmJfx11L2UfXbIg5b_bGEz_YfPHoMn3aEA6eFsVyn5R485869kZ0aoApWZiUhPPa1weLZKLmR7qeMk0Dv-jDI_4OIh5u-n12nq7gmsg_-E4XAKqreNiJt49_Eh_HxNqRr8JVjEK6nquUOttOcQR5CzuwihcNCbpIAIah9uj4lsB3MoEnmvOzSgSh5xcKxlMwpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/persiana_Soccer/25389" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25388">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jl_TfqPEp_yroSQiys1Zwo0hRzxPfw9z3wfkIZyIb3nE9WBdGJ-KFjnDB6QMDEXtd1xxs7unlyIf3GL6twRRmXEHGDCVmRrzB7UUzPinkZZNYHaIPrbJ6Lov32RN-1iDiqZX1C0-3NQDnnfMnF5mKd3-Y24D6JWkgOriPcYWZ_gEdYe92u_C1DMvBq4Aj_eWdZMAF38PmA7MCpg443nvS_2_GCEL2Og5zqsRqVXV_gmpoV9jUYNLBIQZKC-zn3p70rZqguO6Z8rCS7QbVhNGLw1MalUWAiOu2c-B7LUTkpIJKItHHln_of7w03EvsNhAmgTfQXBzNkqZtnYmGZGvog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/persiana_Soccer/25388" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25387">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/As7ueXSKxLccd2-ngdwYDmymFgEgenGBQal9ux7L-gwxRRzQQ7ItVYzPOl3UUHCZDhTM6SwOmjnFr-glsRTVO04qq9UcSit7njJmqU1KW1ETcgRrxtB3NztZJ5WAaTfV7ZarxbkkPpQTw5LWyQjz1uhHvBCg8KExFlDZSNgj1-4b6tL5nD4XgX2BRkG5hoeb0XR5iwD_VLYU-ZLAES-wt2X3l05xKooMNQvRyRvCNZVx-USIBrver7n4BJWe6wJzeI_weqmepcNVV7Ueu6hVfx6AntpQ01aGL1q2Qa54gm_rGCiAVnKuGaR_O2RE1-eICZ2fbtlyBG532s35ESC5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تایید شد...با اعلام رومانو؛ کریم آدیمی ستاره دورتموند با عقد قراردادی 5 ساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/persiana_Soccer/25387" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25385">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qLv_KT8IEVP5LtwgS1ntvjLsbpa0uPGdO5qYwKGmAXuUhqvZuoL-b2mENf-5DP-NC2EfZ0Ka--6Hm4zIMinWFLTdW5HO042NEj7uEsvWF8SzTO0fYGSMPnR7ib6xEdxtWWqUGpP5rCh7xCEDrqbs5xpn1NNi56NEee62ziu5jgS9XKN3WdGUGDFOh8QB1c-KAcwHVgQZtlqbA46_hTsV2PaqxkqeRMe0hLT2f8q93LudHcJ2KIQPTQVDiJ_rLvQINqa-QOji7DE79rfMM38Ip3pb7FStpcmuy1rkhpqWsIY80s82w4ccdlr_MtcXeWmbBqdffq7Gq_hvQMLIhgeL6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jpPSZvUCRfwawqYSrdyvgau2WhyyySV7KFZhWXJrMNJEL8CJ7IuyS3rTJF_4BpA-rZ8fX1YJwptEjKkraYoJ3zKplKQgZw4l1AnURM9VSMlkNdAs95SRvoIp3BpVozEvIrW2kCYHs1VjoGbaV2TkfuAsaLa9DDwJB6yiV8ZB30-O0fOxXt57FUeRMqxlsgTBQvieNrpZk5J4S7NaJ7FCYuwZO5gjv4LTAEGBRr3sILje_ACcvur4kRfns4KmOU2Oww-QjXMUvX1Vq0xTXmnEGAwpsaMITU03EJFMzsP4VC1V1NEzdD_MwsMaXfIUvnrl7bmXWvOhllZ7HYH5tMKePg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/25385" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25384">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFPLlNyy8Sv8o9jjbSTw_jn4WK7v1MsiEvzjvGp838WuG41XHNKDrgpnHecDT93z6IP59veJGvuv7Be_oCpKso_O6UlvMD5x_RRbmesEFX_2NITVM0KblHtRx8QZzA6SAscbVVMoheHvISrQmJHYgGVBmkk_giWZmULEA0P5XeLJVX3GgYWmyKu2heZFAs6Gpk4g__2ba1RyZ6DLIXyxhB3yPC8pBiU9rLm3mne4wQLQkPkfnHkzhblswT45NXoOYUqGIEJbBJoMIYaCP4LQM3CdzMJcVqAyazuVt2ukVV8kilqKELrNiirwe6bBwBQuGrMUsp29U3TlM4j-KUhv4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رقم قرارداد ابوالفصل جلالی سال اولش 55 میلیاردتومان‌ثبت‌شده‌است و سال دوم 70 میلیارد تومان بدون آپشن. در ازای هر 5 پاس گل 10 میلیارد تومان به رقم قرارداد او اصافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/25384" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25383">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI2q7OQnAvjMc9p4CrbOd3qtJImjcYK6saYQFEWkHCvG0IRYRug-W2ufqUBGDw2lLHkbsPUhAo-l2AE1rgZWI5YECEn_GnEvR2cvG4QLZz4JZmXF9UXplMT7XGbuAPtDcQ9OSyjI1rfKxtasRXZclIsKz-21VAu1MEXbuQuLRcqQjzttnbO0PzclrQpEzkNN6Sx4CrI7JqE060H74TQGnyiAOJu_UCgf2lGgdxhMU7TP10hMmo4VFF7b7mc7CcEi8a9hy4a4pJXdrS665ktN1rsyYq23hClfFozXwpqXP0rbPF19vOuXcjX3uzS7vKpUnfPjWFtG_0PS15bDFfk-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
#تکمیلی؛ رامین رضاییان ستاره فوتبال ایران یک پیشنهاد دیگر از المریانیزدریافت کرده. درصورتی که با یکی از این باشگاه‌ها به توافق برسد با پرداخت 200 هزار دلار به باشگاه‌استقلال قراردادش روباآبی‌ها فسخ خواهد کرد و راهی لالیگا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25383" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25382">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sp6OYfeyUyQg3jcjmpEKa7ErzO82oxq4cHPnyU0h5kLNTztuOE01z8LoyELaBrWndkCOtXyFeCkV7swOhu3DNQtDlCZsAXQ6pDJcT72U4_VGv7QvHs2fX9kZ5uavS-CiWxhcPLCyml3aF21xbe-CqcQdsWdq_4fB8ZmGpNXCPLhXAGG7bqGH92Qc_S-v3YhU1Ndg5H_dZhbDTlw8vd62AD-WLFrgeNYAwD-W6GnBWBMCVjrM1a4fY8WdZqycAfcr7C4Gwl72om5KjSaJFM1tkc1PxR_FfRQn01bQYVSd9Qhz1caneVqiFrYWTf0WnFKlQcZ90dKgB9www3hY7j1ivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری #اختصاصی_پرشیانا؛ انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25382" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25381">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snCRANXE1aAemceOVyN7LCk58nPTAdi2n5BHfFzCRrMjc9ICfuxCOq7DDtSCRd5-O2WT6xDhwfMB2xfsAmqki4wstW1JKQXdYPP7gkXOF9zUWh2RgMV7j1d0Yg9OkxjYso51xDUlO1SanOItmVYXsK2e-UKYePbFGQCCYSpHOxxomRTpXWaypplGuJhGT1t3PWpz3VFXheMZT7Gm9NGFSnMXaigiOBO770hK3A3wdZYFosXB4sfL6CkzwPPdMqZkgW10A1tEqzIxTvfD2QUTo3SfrgzY3eMiK-SijDljiBNsG-uUUy8ccUuLcoQs6VXAyVscBloJujGGIiuAhHh_oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری
#اختصاصی_پرشیانا
؛
انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت کنه و درصورت صلاح دید کادرفنی با او قراردادی دو ساله امضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/25381" target="_blank">📅 20:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25379">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyJ3jSOmFEOiiD9ZPZpO5J6P4rBZ6k-eYH2SETDzpPZlH-7urOD-cqp01pJphl-2ItI9tJdC0m1g5oSA9_WFaluaew3bSwh5ffJ6Dj3gcEtjK59SJJ3FMBIWpA-h3KJtw4nOR_wax11l4gh-9j38QapP2XyPEonKqx6YanikinP368queuYq16TUM1eI8eFNfCvePqH5aB6P9Uc4DqMoV5cbTCs9JvozL14yku0nojhgFfZRIA7ltz_fOQb8-qCdOqTqN-nmw9Rlq-rJadbhhZQtln-LI-7B-vKUC75qtT_l32yKstIjARl80xfAxNlb-WKSIL9f5xQQ-Rypr3t_4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25379" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25378">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ppuv7g64OKcZHLfEwsNmGAPwftOZsKHYZgN-QtqX1eiocPktCPFfXnaOwICCbzWPgyxyytFZ-7iqLJk8wOQaAoY4hdF5CRiPSyzseyHKPCTrY_k6IhPYbGL5Lqh-Qcue9ja4vWqoa9LYah1Fc4ePrQwnlN4WhTPUt27Wj95-Aa0EigO6mOeN0hxGgK_Q5TR75C_cviwV7uear4pUGAB9ikWkDE4Pj3Yp9Cxw7_69zGTz_Bq4OcgbX7f1g7v6hAlLrVsYHKYLbyqdlp-VofPC3VRkLP3I0m0cHYqRyv50lduoAiTHYmz_dxDCovA4VV8HvcEJExuNsUP8evdyymJJKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25378" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25377">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7xI0RdjguUUweCfGHg22vAJ7LTq6Tu3cR4bKAcZxDTHIen62agGwcjKjgj_VK0wwGiVGw9-X9phvu0FyuSqPEh4lkISzlOdmNAsTXK2b_HffNpdTi1xeRMA3sW6n2KBt3E66uKVvgaaX2L7WQeBcjl0KuC3waG87dFa50CRPbvf0I5EYnKHLgjhRS95hh90le0hWV6Eic5byKBmFd4xIA2QViAz03eTbzrXULl2f-xGqQwVvSgIOMt4HTnJ-e4dCAxFUU-M3rGftjivEKwcxh-xIIoSylZy6QH5dFT9oN16cmjIVFyXt32kf6La07lelN4LQF8mi2AFHQm1TqEhGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پیش‌بینی خودت را ثبت کن!
🇧🇪
بلژیک
🆚
🇪🇸
اسپانیا
🎁
۵۰۰ دلار جایزه
بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، مطابق قوانین سایت تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه.
👇
انتخاب شما کدام است؟
🇧🇪
بلژیک یا
🇪🇸
اسپانیا؟
🤖
برای ثبت پیش‌بینی روی لینک زیر کلیک کنید:
https://t.me/betegram_bot?start=p5_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/25377" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25376">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICSk1mp7XLCMUvU5KqBN0aGGTeZuM5vH-X5FPVskLRJULYPEJQN9J4l1GuRQqXQ_AQRKAfB84LyHIqw8Y2S0eKe8ps5xHtGfNJqTbsXhgaSK7j9pG9ixtV-nxNiDTHzmlzpxF-gnty2HvY8sY5F2hnxwXL5FY1xXgYoYC5q4vBT3DlShVuZWaj2X7A28BlpC0BJZiqbUy2boLt_sA4gibkEY5sIxhZRJ2zYkuuChzhNb5oEbtgvKKk2ru4UscyiainAYoDp3R9jKioY1-gXX7-DTd40_K7FcuDZbC7UhjmskxqOCTaBvK4vfC93E3CANizocTu0ORBvbZkb5lzdUQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتوجه‌به‌صحبت‌های ایجنت حسین نژاد؛ با اینکه مبلغ بندفسخ قرارداد این‌بازیکن 8 میلیون دلار ثبت شده اما باتوجه‌به‌اینکه تنها یک فصل از قرارداد حسین نژاد باقی مونده به احتمال فراوان با دریافت سه‌میلیون دلار رضایت نامه‌اش صادرخواهدشد. سه میلیون دلار میشه چیزی…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25376" target="_blank">📅 20:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25375">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-34FTAOuIH1Nqk5nlGKBc7tamJc0tJPbVTa36964_MaQFAbisW8bKMvmv5W-mHtIkJUybtV0DbwnuObcYPdQg4OYAvTfU7Z59k1IcRsw-pbgGeCONnj_9vSZNvciiPhNUKF7AbeagnE1E2Lplp9eW6OysbAjfUEjIeRIQyXsc-x09SEE3cGuL8rvMz_2Kb-YHudt7ZFNJIRCxxgFhSeV2Dpaujw2Jae6sLR7D3nzONVYzTH5-i96q5X9etwWvpBZgryYqoDbP05P1Bm6xA3dvLQQrB8fOjzRcnIEK0pOj_hmnS1jQ5-DxUXP8xBsGg48JxKECfBfgJhT4Ja0EqIkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
🇩🇪
#فوری؛ سران بارسا برسر انتقال کریم آدیمی به جمع شاگردان هانسی فلیک با سران بورسیا دورتموند به توافق کامل و نهایی رسیده و به زودی از خرید جدید خود رونمایی خواهد کرد. جذب آدیمی ربطی به پرونده جذب الوارز آرژانتینی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25375" target="_blank">📅 19:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25374">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luLyut6apo5dCXkJum7BnJp-ruQfhwnGfwYcaUIglA61xbtUqwWtxiZsk4LNllD4f3U29CxvsE4vZnu4cB75gRJxm9hEXt0qU1Tubh4tXpZjdc6ITjku45HOZb6TTISgY7mbKwKSGtEVYAQTD6ezN0oir9uWfnEXYDNOQ5UEete_kyZ_xFsmCrvxi3mkxQHQ79hW7AUmczWcsDiEcDKfkIz7I31gk4uHvQlCaeM8J2oA4b45uuQf1Kuyj0H9CZ0po-YFzDCMemZB-KLxG5ukKy6geOvLfJlGjPKSQFzs4SDiZmtS5CJB6GNX2Do9N6Yj9MCndi1624aTnEihEtj5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ ظرف 48 ساعت‌آینده "تایکشنبه" تکلیف نهایی دانیال ایری و پرسپولیسی‌ها مشخص‌‌میشود.باشگاه نساجی برای صدور رضایت نامه 500 هرار دلار خواسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/25374" target="_blank">📅 19:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25373">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=IexIeILuozXSI5fUp5HX7Pt84bkdPwzcHiJHt8Ptgb4uEihb0bCt947EU5mdbiOSqjNqPmsjHtc5sJjyXbmPAvsMi-kEYEhQKnmXWqFilTJjwMXwmQOadbxUkfXStQ7-C1qUIj-n3yEImw71BYwC6qkVGoNA6V_P5_UfoNkcu-EAFQ4nKwB8V631jxv-ZA96t68COZMlKg0TC8CEGx9ifKXnjuYLzswbD2wk7orJM18wRyq_gWXhPjq_59h2zIOdMNbkw-HUYx3F7PKBATsy2b-pIz3W3f3WXh2bFLie2qt6EMyYiFlOf15lUcds_D_Mfm-4NQSSXO40f6rumebOpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=IexIeILuozXSI5fUp5HX7Pt84bkdPwzcHiJHt8Ptgb4uEihb0bCt947EU5mdbiOSqjNqPmsjHtc5sJjyXbmPAvsMi-kEYEhQKnmXWqFilTJjwMXwmQOadbxUkfXStQ7-C1qUIj-n3yEImw71BYwC6qkVGoNA6V_P5_UfoNkcu-EAFQ4nKwB8V631jxv-ZA96t68COZMlKg0TC8CEGx9ifKXnjuYLzswbD2wk7orJM18wRyq_gWXhPjq_59h2zIOdMNbkw-HUYx3F7PKBATsy2b-pIz3W3f3WXh2bFLie2qt6EMyYiFlOf15lUcds_D_Mfm-4NQSSXO40f6rumebOpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین فیروز کریمی در برنامه دیشب شبکه جم‌تیوی‌اسپورت درباره مربیان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25373" target="_blank">📅 19:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25372">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tv6z4_tV9ud5qy7V4icY34GLoqgD0kRfTJ9MnGVH0PGebw6OFMv2gl5lt021pi3wafDD0AuATN1Ljq3qIkI1831NzhZVe2Dz77w-AxvjXpZ3VKEyQz95wivcReZD7i7q31M5EFJTItn-0kmGWxX3tHdDfcbZ9FPtzI93tEXau_isS495AGX34BJBt4_hEkVtWQUAnS1jMrgCIBh8b6eRRQZBlk1lui1vBIAMEiiJ4XR7DDAFaHOOaY1ubjTkYIq7zvqVZgGBzuXTt30yfIcm3oYbQUG43EQSoyQRpYAQisyd_BBz22KVc1sZAI7M4aK7vlIDTWzKJbYOpARN7S56Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25372" target="_blank">📅 19:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25371">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsfPmsCKKY7zDWt8K16fJ0q7TuZjHjLPtjFjiT0CDX4969R6vfKz_uP-__RIZIm5mp7M3BmOA2RTFbA82pnMnLax3cA7Ghm9kXO1mztxnRCy-GUi1UYuFZrUaWaKomC-yY7c08JBV8DkeScN7OWIa767TvGA1uI3rXW3ATofoBJ6EsjE8VUeaRPAthvIUZRl4s6XR5DwmG8uc2YYQUTZl3QNllGuuPCrhRxs1sZ5PZ71OMeNUiJygtax1WFLLWtQiwqeRA6mbYX7XLQreFJb1rliE38qprh1OPmwMT0mMrhTN4vqGHT0_rq1FW1QEVtnUEHJHSSTpwrzxOIiKaWIeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برترین‌گلزنان‌تاریخ‌جام‌های‌جهانی؛ رقابت برای شکستن رکوردها همچنان ادامه دارد، اما فعلاً لیونل مسی با۲۱گل در۳۱بازی در صدر جدول برترین گلزنان تاریخ جام‌ های جهانی قرار دارد. کیلیان امباپه با ۲۰ گل در تنها ۲۰ بازی، تنها یک گل با صدر فاصله دارد و جدی‌ترین مدعی…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25371" target="_blank">📅 18:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25370">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWXwByVSe1r8i9RkHlIbVe6UrksVR8zXouJaJQq_1fDehuBVfDDqHY3qGzKv1ydu5aSn_EMMpBX1AsaGciiidHwCHMCj0QX5ONJI77YHlOMxL1NBWSko3WPcQC66OLytXZBwi-B_-o3R_suadQVgnklGVRkKFw3ya1tw_99eg_7uUTsWMLNd9f4EVB-QnwyPgum-DH6QI0yk35IZPd3_nfHpcpPpNiOJimM3DTAcujh7lIHEFuekX7rvEfa8s4gLjD3IBV64O1QjGAtKL6WDZunSWyn2FZda26CeDRhxJ0GFsCaxVrIpMxkzAUHwBTtIdJsClYMKO0cyRVdwmS9lFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/25370" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25369">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxbjZct6bysRebBjmnn6Mo-fh9tWUv2pK57xiRmPy4Glx9NCP1Sz_5nlhFHlS3mM5K4DIFHq-ul4CVne4hAs11ApORIsAYI3C6CEpF6xPQaO3o99Xx936eoC19EEN1FcDA6JiJ_vAfUUnbEEko9ryYO3Vsi8kdwCmZ4BoDbel4yw1vfOO5t4D855x9-2-4CCnUv3N3UQueLps0Kq4YaKPuE_wDmqONEDtJVasAy_dMpKh3w0ZWvQc0uQGykgYR04QO_FB9-xVm-8SyX9K8JXTPeDegySQWteSDNEctoXTSRiJg71hOximGJ1CS2aDQBF9c2nPpyqRNHBybnAVIpfQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25369" target="_blank">📅 18:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25368">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdeIEh-Tz_icshSAguANT-Av7F0h48FR5X9ddDFUPhvyHnqJ_l6nJfNWACkNLw_ifHB7ihXmXnL9mPJJxM1TXv-piYFt5ROqnHmnrPNXQDy_wus-H4KvWtJA73pmgL45fbyKgPIpMpTLDwMVvQ_rYvD16g0iMa0Pf4gV18Uu_9aEWtGWtyOvpqO_XVRtIlfmfw13v0O9dVUUYnfHa-RjPY5XFNQ8rcJHHFHLl4v7luPv0Xh984LxJ0ftZhLswlewsn4OvebSP9eMx612jRYE3A_I1l-S8XpvwZqhB5P3u-pzzNLhyqaFeRU11bC64skw3f3xskp2ioH4P7-jDyHoRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌توخل‌به‌بازیکنان تیمش گفته در هر زمانی نیاز به رابطه داشتن‌میتونن با پارتنراشون برقرار کنند که جود بلینگهام بیشترین رابطه رو این مدت با دوس دخترش داشته که باعث شده بلینگهام غبراق‌تر وارد زمین بشه و برای این تیم در جام جهانی بدرخشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25368" target="_blank">📅 18:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25367">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIC5hBroUZcxL_2q-4GDExfBOaHgOD9NMElA8yvCdA0XSE2iAOUq7ZkmB6GJ1VEGJHZ7orJFulRPH0gLDPgXfTPji6q4Qq-FEsm8lEJyLIHJZ0I9u_RC4mfRA5EcxWB3AyEyml2kvgIF07XLtsQMt9VSgppxUHGeJIboHqY6LCUDZjtEMXo8XNj6u1WRjm1U9m3AtyXH0uG3irQvNPdjpvdrU6sSIeAtbr7EmTYWELJQ_cA4vzRdp6zmbsHu88aLB4iefEcU8DugeEhWnBJlKt00-S1XGbHkYtae6Wmq7KTWlonSnlOJ4cQ3nUCZ0HTOmbSAEeluwfPmJEGCqKF9qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25367" target="_blank">📅 18:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25366">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/typRm68j6LbosKpJfdueRxqrYujB-ZrMaUcL2_Kw93EUj4LLh_-ONs6pqcmokdNAjmR-ibgr01hb2joUAeQ3d9hcYkysBvFEcFvkLkg2E1tq21AHQzppYgAiOl0t6n3OWOCQdtRFHrU-oFX7Znddg8FmC_9N0HHNMX9NNbB1URqddrSVzmhyajVEdIZsbaKZ5BbYm-IMWhVRkk_8gM4sDMVzbjfhfGFaBfU9cCzm68LDN2q0zg8azpKnoLLEZYB4dc6k-NoFasY-Ibvo1jDFR1bGymoQ3uvaIAin4BcTdjqoqtlWAVsiDJAs3QNd7ajD4ADxYW-Xx9GiulGpWrFv-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
به احتمال فراوان جام باشگاه‌های جهان 2029 درکشور قطر و فصل زمستون برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25366" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25365">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4-yLyzF07T_QBL5mx6i5jcVaCVwtmEQvY1gQWxrnLjZqHquPRYZLphbb4M5FND_Gjai_V9jssrTQwkqKy2Pm8Mbid_bI6B44fCNgx2ocSx6qzmrzhBt83IasVKk6T5RCpsKEhOM02BYn1T5JJjEldDAva5jDkvobR8GMaS7iw04KrZHfy7M6Q-NgjQwabUZwYRGTD6KvNPODXbMFin_kZsGn0brKAde0W1Snzy265x7EcBPaLnLbVLoFvN_MB33MpOzQRxxPMiiQOswJw3jWDfWi4y5AEe3muocWKLkNJZru2HNt4CU_rUeuHVGGLG5l52QfNYDhcwYewSSWX2qMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعدِ بازی، امباپه بازوبند کاپیتانی رو از مانیان گرفت، بازوبندی که خودش بعد از مصدومیتش به اون داده بود؛ الکی نیست بهش میگن دیکتاتور.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25365" target="_blank">📅 17:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25363">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUEQC4Az7jeK3sikczQUnKSl_ELnQwhcWvkNEWnJQu7BsDuGKE8Yn0teSIIAf5oBfXilZif58GCkYocsyIfAvCRGF8xiojBo-HIdmEEYYW4v90wNyqSo4vxhaFcIxx4J5lHv8PphiaU04b5HCQhB3CfJKQxl4jQIWm8sFO5it616qnhGMk3l3nX6M9TZ3h-s-xQhZjFj3Izo1ap8KGE2qn4YdZz6_bkpn-bGZRZ_AMQj7ZDqE4VyUqfu977m_5hYRGmj1cLPsSphpfXEzmnVKuw6pPOpn4fTi_YZ8xH4meJXdgH0v9gaxDuNxpmj_IzHX8BHKjSdlxvQ0ae074yrYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛ فرداشب‌فرصت دوهفته‌ای باشگاه استقلال به‌محمد محبی به‌اتمام‌میرسه و این بازیکن درهفته پیش رو تصمیم‌نهایی خود را خواهد گرفت. تابه‌این‌لحظه آفر رسمی از باشگاه های خارجی برای ستاره تیم ملی در جام جهانی ارسال نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25363" target="_blank">📅 17:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25362">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wccu6E8CLa4lWmG7uSF4SfmIhXDwV9fNOZ1qvTHiCHJfChZrFgs1tMzrtiDZy_ExFpH1NTeZqCUv_McHhMholcdtXsBwBZhKuYSEwk7g7vrpmPNih7KVl5GfPFro1PQx4a-SZ9sPKeNHbUwZCzl6saTBLvtZcgrUHXTjcPu1gTp0lJ2dqKah0rklDsJNjAW5dcxlGOFKttwgYg7F_Mv4TXBRYC2Y_4NO9naoB_ecYc1FV1D9ufJTOdiqrL6ixdnaoh81tRNIP9shwSs2qmSEdd_LteFjgqqB7ZluljpyC9F7yjFtkPT2OG43oosfdvUjkHFUb135EZJY4aXD-qYaTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇮🇷
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال امروزصبح باردیگرپیگیر جذب محمد محبی شده که این بازیکن ملی‌پوش از طریق مدیربرنامه‌اش به مدیریت‌آبی‌پوشان گفته‌بزودی‌برای‌انجام مذاکرات نهایی به‌ساختمان‌باشگاه خواهد رفت. محبی گفته اگه تا20 تیر آفری دریافت نکنه…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25362" target="_blank">📅 16:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25360">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTrSgJ9QRaXr5mzKwi0bX5ad7Mmyen7Ko8UP40CP_n-x7FdVbuXk2IyrjoKaSbmjIdF-ThTN8FERlCQ5e_j1v9M9kANsGUb4CKGQb0Fkh1i4hxqyBt0tBM4boC202VkS8z1mJJzRRH-2Qzc2wXxP-NOo1GUPjmmgxOgGqeukTVllUvWYMKK767C7s32wOvmnexvAY7zDgPKp5PIfk4UTchAnq-rIfdz1mqi7h7bwhSRbzPBcFJnHr60XX6tdKY6XgWSC9Bey6xdAC-TSND0TKIeU-VXWjTLawBUCgba0Txx34IqfVW3RcD9KmrJMScGhg4IrZSKYU5xrxWnUhefXqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مدیریت تیم استقلال بعد از این ایمیل وکیل ایتالیایی که امروز به‌باشگاه داد مذاکرات رسمی خود را با گزینه‌های مدنظر شروع کرده و با مسعود محبی مدافع میانی 21 ساله خیبر خرم‌اباد نیز وارد مذاکره شده تادرصورت توافق نهایی با او قرارداد امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25360" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25359">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gx3P17lKoOooxDnWD8-GOlZ3AplRRgXgTkHo8rE6bxtPbISNJ67Fd_Pbhj51WFwSyJQiEQLUWxrZ6xrcOsdNK3Lq9Tq9BnIHJkqp3IJdmdTGwZlx51JmmXnJvVQkazoq9baz1FIueB_YTD5Q5pwXFgE3nbC43K5udRVt7pSw3CDesd8NZ1qgpVNA2ZTPTUzypizQ07r23KvkoqLEl08gbJqbmINzJhrRntJkIc0IIQkx4hn4VlNTyffx5hmtkdh_tFC64jB0Nu7s-zbYQ5NtYPvDgcc83k5HKJi2SKEZz-oeks9zxSRNLEqfiLInnlm6CTC_97NBWqJlCTGVOhXlvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی که در یک دوره جام جهانی +8 گل به ثمررسانده‌اند؛ امباپه و مسی به لیست اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25359" target="_blank">📅 16:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25358">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇵🇹
10سال‌پیش‌درچنین‌روزی
؛پرتغال‌باشکست دادن فرانسه میزبان تو بازی که رونالدو مصدوم و تعویض شد موفق شدن به اولین جام تاریخ خودش برسه.
🇵🇹
رونالدو درباره‌اون‌بازی‌تاریخی:اون‌روز با اختلاف بهترین روز زندگی من بود هیچ جام یا افتخاری برای من به اندازه یورو بردن با پرتغال ارزش نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25358" target="_blank">📅 15:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25357">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6lfx_QnpWUOYbwm9td9jh_bTkuSD-NAvinSUn_lBCTH7dhZ0oMg0h_4aVuGmkTcXAyDbgazRen1hHiDvCcWMKe2ckvDDZQlar4nJY4sqCrealePm0eDHRLorRyAiKgpS7WwJjTfNyU-z3-e1t2Erc172Eqv3NLtA91PQcwR7vrrOl226SkyeZ2E_opAlwN_lVHRUAZiBeuepL2b0GGveWjWOf-CpYSyDmd29lKZpQ_x8Un2hdgxEKqC-L4lzRj4CQJIhfY_RuD-77sSbZtUXNF9G6_4WRmkIDD4MaJph2cSCMUH4v5tfwlb5Bvii1u8MvBUBCswveRPJNHZDHlE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25357" target="_blank">📅 15:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25356">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=NIafStRcqD4BsqkyyRSLLGfJyP-jGq7YCKsIwBiI25XqhHo1ygdM8ToBDBsMoMWz_e-MACnNw5qJ2Mx3AOKclvbfH6OQ9gnjKCBLMXJ1fwQOkiucmrnDGGVUocbYN5YCwDWQUk70M_BuIkOsvpmt92d5Yjm-ACWBxOu958OBCLJTBbhRatPyQ2HmGXUEXWMo5iCL-WI0moyK7mUnLu-CmZqtR64oUGXjIPt87shDF2n1uElODXW807t5u_xlOD_ZW-KIh2VfvhB3yXhMQh8tP6dBFVaLFbsfx2DhrKQ9SaazAZanS1F3S5qI4VnTIq9fQtO2UAvfs7PkMOoz5Ue_2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=NIafStRcqD4BsqkyyRSLLGfJyP-jGq7YCKsIwBiI25XqhHo1ygdM8ToBDBsMoMWz_e-MACnNw5qJ2Mx3AOKclvbfH6OQ9gnjKCBLMXJ1fwQOkiucmrnDGGVUocbYN5YCwDWQUk70M_BuIkOsvpmt92d5Yjm-ACWBxOu958OBCLJTBbhRatPyQ2HmGXUEXWMo5iCL-WI0moyK7mUnLu-CmZqtR64oUGXjIPt87shDF2n1uElODXW807t5u_xlOD_ZW-KIh2VfvhB3yXhMQh8tP6dBFVaLFbsfx2DhrKQ9SaazAZanS1F3S5qI4VnTIq9fQtO2UAvfs7PkMOoz5Ue_2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
ویدیویی‌ازکریس‌رونالدو
🆚
لیونل‌مسی که به پر بازدیدترین ویدیو چندروزاخیر دراینستا تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25356" target="_blank">📅 15:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25355">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=lhJXqAdmFUQBIlbBnbQIhiENBUCPgpuHsLWqv1qbln0odtuJMn--f_FU95MGTalQxmzrlqwjCkdivhupf9Lm1nuua2B8viX7PEqQdhzAxpsKIxYVZbb9aVZa9z6zCoeXUqHT1S7uKC48haU4EvACt6rV3vBBHWL8l3voFl6_ARsV8cTMaz6sdd4IhVzKNRLXL-t3MBSNs9ZnMScGY-NpUs-Wt_YXXRUkIsxj8_1MqEo6xBg54JeVauwpBjrPQ4uIhh7Mn1PFfc5Nf55pS1GAy-Tk87hamuxAUjboqRkMVNVpA8xuVSAPLQGhUpqQUo6BDY5IThoRS5G0pTFrRnRHXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=lhJXqAdmFUQBIlbBnbQIhiENBUCPgpuHsLWqv1qbln0odtuJMn--f_FU95MGTalQxmzrlqwjCkdivhupf9Lm1nuua2B8viX7PEqQdhzAxpsKIxYVZbb9aVZa9z6zCoeXUqHT1S7uKC48haU4EvACt6rV3vBBHWL8l3voFl6_ARsV8cTMaz6sdd4IhVzKNRLXL-t3MBSNs9ZnMScGY-NpUs-Wt_YXXRUkIsxj8_1MqEo6xBg54JeVauwpBjrPQ4uIhh7Mn1PFfc5Nf55pS1GAy-Tk87hamuxAUjboqRkMVNVpA8xuVSAPLQGhUpqQUo6BDY5IThoRS5G0pTFrRnRHXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25355" target="_blank">📅 14:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25354">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXrdu8bnXaF3oaqao17gUj729gmk5syg4_J8d7Fawr_Sff3Uo37gStvWvAoLZU4u5dWT7f_iouesuYtUw7iyLCKzhPKUHgNwn8V1XAoM0yNRhXrJdO5_N0I8Vi_NI-PGFO7epDAy22_wFpwVr-aZVr1aS420P2UYsUoDcm35b3snz2_j7weSlJ4jdgwysfAGi6b7lLw21No87iJhpu0kLanZw9tQeWW2uw-CGWqYQiYRSotxA_SD0AQIjd5OXc9DiL5E4axTW6Zwal_yx442pIg-dR1fKwDa7InJpl0XgUWIYBHpi7XUw92gidvb8qrOsSwPl06ACqet_1ReD3zHNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
ابوالفضل‌جلالی‌مدافع‌سابق استقلال با عقد قرار دادی دو ساله رسما به باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25354" target="_blank">📅 14:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25353">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9_ZPDgiD-mHYedwKg8JehNJZ_13MOWdjya0iuEihHG95LpzlnXYe3M_RF9FPDNjUbfky0y0CXdaub12w50ABf8dexDRUI5IdO_V8iDaI_qLkSyuEA2x8hQOu-DThicedrOJZh4fRh6J8mqXvxsjK1Q0EmR92oy70xxZzlvRju6-B6Jr8zA2BzjJCfFrQkZ1gnODa8d3BXAmX8w4vQ6TN8-q-9AvNhGcl9_9q_FvDS8jp6MWRZ-LRHol7eFD6ehMJVTmVWfJTMlxNmb26E423tSEZ8CIvr81MkiqkcLNIsDFNa5wHaAQCOAPnQCjz6G8PO2hwVunBQ2GQjQnm5zlKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25353" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25352">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4wzfdw9nXitLxz_ag3OrU-2SMI3S3StFDkxWNe9k2t-IlfkkbmBpL62HsNOXN-MDa6enE4AezsBBZm8nTQruPdWZA2hDKCCMKX8dbds2EKQ6jDWQENLGX6rtqW_tH0uyGFB0i6EL5HJEQaJYt4MhDHwcjOr9GzV7o6F5iFzwTYx3q-IX38UpPTHql4zmdeHlxafCgRBiQ03H8H6XEacDrb05YxYANrcwIgHRfn-y4hnCzld0SGWRn9cSFzyCGY-U2fOMBT5c9nz7M6dcVimLMb6F-VD7v6IJeyZZv1YosWkZYGQRgQWNA7WPR-97Dn6TQdU2FwNFjyFL-DDlXb3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
نماینده اوستون اورونوف به مدیریت باشگاه پرسپولیس اعلام کرده یا رقم قرارداد این بازیکن رو برای‌فصل‌جدید افزایش بدهید یا با فروش اورونوف موافقت کنید. مهدی تارتار هم در این باره به پیمان حدادی گفته اگه با ترابی ببندید مشکلی با فروش اوستون اورونوف ازبکستانی…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25352" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25351">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qasl1L80kkYi3RCoqe5y1iWrPGM0mQBpftVUoiI-do4v4UtIXS7bpbKiIwSMWCZQNuQ4NQcew4X3fXONJgkVO-9US0LDUeOhUITlLJRwVCDTMalGBZDLATnCzjk7dxmrVb5efGYMvhZ9IT1esBDIIE42Z8EtRmqEU79uYXe1ru6SjGQVwBc8aGoxaPirWk1k96CWlFyhbkaiYrfstWahcIbu13JhcdDM_OrcswlZjuBe9nmulRrJEb2WwCLTop_PBiTMczE-RCZ29joD9VGkIs4VVE2qCj4jEfLmQsQlQmSRmnCwQfqmnPEnsU4r6eEcMY1hyHu_v9GK1r77AF1Qrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25351" target="_blank">📅 14:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25350">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/so5RK_-5irpr53gLFtPGJGZ9AzC6paK6sdPGiHZfx37_bT7g9UtZEAd_vdZebeQscT_QoxH-7toCMpnHeZEawwK4kSlduGm6tWpos8OAG-cfnMdGLV9W03XejtJCtw9k8Rtpq023Kto5uz6wzpDo9ESpjgTx3LqpfVwXXwQcogwf_KP4JY_PnT_q0J8jZIywULY6x3fAHkqoDqUDKR2fbFSH_VQ8JzT-Y8a0_QYkODJpx_EIPtTQ04YP-s9P59XroK8clDxkNTkU3IfOGiDNdZ8N66ft2io80pFUG7sD9b5g5_XijvDtom9LPYPbvt35jwOnWProMTq1MD-v7nlwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25350" target="_blank">📅 13:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25349">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGItyPehC0JIr65l1QtMzGUJyFwEDLvoL-kNivskTgoW5j0bm9fpu_PJ1eYZoAdihrWga4dSmNtn2tVZAl0ZeE5WWj0b4uURUYUncBnSb8qnutsvCweQjIWA51AqIGWqGhcoPBpQNa7umL33EJdpI-IiifrZNtCfQ0lWsrkwdEtCzgIhsh_aiwJRAMZXa8070VVal9oSrI6onyF0NE8WQ0OudfY17rdGaeKuAu9QGNmsO6b8YVw_VpBhhkDkTFgIcoHZ6QCUzouITGh8FkfNaQ3MfbfF7wSGH841FySOqtD8NofplL3hLMkZAhFK7x7QfgW-nfkmE5HMvPhKq3In6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25349" target="_blank">📅 13:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25348">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGsl_XkxZlPxwbtTl16v5LL_D8SmRy_IBv9M2wF5S3s2DCkxVtuAmv9fpddLAAxVtXCjdtbNPVqSUeITRpLwVaCDy8ICgtLnHP15o2Z3j3v8F44OM8oQcqGDFAVjmBN02s2wcfqjfBnX-XNg-Ien7sR6yZ6V6YJVrGDBB1PaRF5bIJazxW77s7i08mZ2Mqa8S9iRKC6_oJJUnZ4KeOM8SPNVEtH0T8ofLs6ZMwWpz_-lBUOK-cxL3LJurAZmRJ6SsJrFhBdnrbp-72jBtzhGlYu901KCfy0H2QucP9Yp6NW21tW8E519j8fO5r1yMVbf1vfHP0lHPwTDnzTxCkkb3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25348" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25347">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2lzpbRVtdLLvmdvpqBM6EKL48OdqngkI0GkjLA2xRtTGN0d4SIZFUKNrIlJprkjF5Y6X4E2nZsCyN-bPTPUdZtzriPdLo0IOrmsaVJEGLxgHdiTon_LTQRtF588v3oxPo9b5m_8HOrVf4jBBJsgd8R3Dw_Cm6nxN886wuYHNlIyQHJiYjDwIhS12uhcwEZZIsJzp2D6voNJo00poyvDfBXG2frBK5C9mapJ4uG6V9plio7ruUY_5oe6tkAUuTgZuT8V1rFyQ63Dv1MVGKwu76XAYYJhQb7NBKHre23L_5UGQM-VulfW8nlhLvosjatfSeEDgL7TIq6mtJdANat0BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره استقلال ازباشگاه الشارجه امارات که سرمربی‌آن‌مورایس‌است پیشنهاد دریافت کرده اما به مدیریت باشگاه استقلال اعلام کرده درصورتیکه کادر فنی آبی‌پوشان به‌سبک‌بازی او اعتقاد داشته باشند به قراردادش با آبی‌ها…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25347" target="_blank">📅 12:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25346">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">📱
اینستاگرام دراقدامی‌عجیب، قابلیتی اضافه کرده که با آن بقیه می‌توانند از عکس‌های شما برای ساخت تصاویر هوش مصنوعی استفاده کنند! اگر اکانت شما پابلیکه این قابلیت هم به‌صورت پیش‌فرض فعاله؛ به این‌صورت آن را خاموش کنید که مشکلی پیش نیاد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25346" target="_blank">📅 12:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25345">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWafSvizwaZWFva-oKP4XMOCL31ffFcuBmjbbwEepufiClskvQY6SApn-mIDJ6z8_BVXiDqSrzc9hzJu5Bu_MaAAUWxCAQOaqld_cylyvWWsXz5eFazf3wr7dks1OBFoa5PpiFROuBK16m2YUI6hXKRhEwKwxhx9_udTe0lqw2JZ1l03VRmIIkoK_5eetGKI6yHxI-NVWSvRgA3z2R0BsXjtM0QiwGwjd5Ken8rYI2uEYSJsGsRmrwyKhTakYULJ1UeTDyerHcXClTu1ZIRqXb3il6v3M5HAp-tqgS39cvPgMzxa0KCfTd_5yugdALU4y8Tx-C4zeAynpbtH05ecKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25345" target="_blank">📅 12:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25344">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pI_ZSObz1lqyZ1Ay6nr1ajL5Uqd3KKRvWv9dL44JY8TKL5v6WcI7JCx9AysV9kCe-BcOjSvZio4a2CDULnyy2193h5WwqN7c8ykFP2EesHtCN35xTuKYxyGQQLXEQTDLBgV658iOptgnBQDjfhYFsTNqSlfRU6zcnDpXrCrn0hzYC9RVCmcOd0HMjQ89Hzjripe98sNZxh7pfarxeOE-HBdhKUeTNk-7KIno87Kwd5m6oWUWEQ_jX57YZ8U0EBPgJ08Xy66DmPQE16VfbAnHkzt4Iv-PoAFkW1OxxUm4CfCtflKClK6wH2uyjt-puefZfssnh3jK4GJmC4jEMl-scA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25344" target="_blank">📅 12:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25343">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c669eea570.mp4?token=BDRkQkWD3A72miPSP05G9yuKwPZyxUdudTH209rDGfFAkezR8EOE-zRHnm3buN8Ue8PALG8clwDPm18pclK6aO2Kc1-WN_KmiOg7Q2AR9IeFOQAejRb5ZtL98mM8fDF-qwNCmJfEObJEci5t7nlAvWoApNWch8ajIqhRTCJpqo5y-cucRb82aX_hpzv-gV2av4HNkDewQz2dUoetMsfV4ztvMLEiKWiYGs7BRUMRswwkIbvHlocecPymGZNvaWSILVAx3P3tmB7QZU03RFsR8lyDCVQAycoVFm5_MfajIglbfJ4r1ZGXjfKh0PaOpYNT5UMF2By0L-utqW_sE_Owyiq2daPVbiKhFyMGBp8Lb68lyg6PVLPm0SNzntoxPZDkHgqF1CvdslM8xBtJu8kHNYH5RVyVeQeuktNbI2vlme-Jgj8PQiWXYCOcj2Gdul6aeWQkLvZY_qb4jOZwifS2EQRezP25tEkAl2BGRNPuk0N8tvfcxoY8Z3etoOT7NRIKUWPDisfJcdxlC-MJJHXYVpRAFvE3yfOcDJZgpTMV78suZqMH2rCobB7h91SRmu8EEmo0yhNg8mj2-DH4WT5MRWtqioJIbbKKk9Q59ZgGkG3KVJaKNqkl4iGHwq-wZ0VL3CAPbF6S4ZqxcYuvU7L7Bys04vbTkJDh3tRElfZmkdo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c669eea570.mp4?token=BDRkQkWD3A72miPSP05G9yuKwPZyxUdudTH209rDGfFAkezR8EOE-zRHnm3buN8Ue8PALG8clwDPm18pclK6aO2Kc1-WN_KmiOg7Q2AR9IeFOQAejRb5ZtL98mM8fDF-qwNCmJfEObJEci5t7nlAvWoApNWch8ajIqhRTCJpqo5y-cucRb82aX_hpzv-gV2av4HNkDewQz2dUoetMsfV4ztvMLEiKWiYGs7BRUMRswwkIbvHlocecPymGZNvaWSILVAx3P3tmB7QZU03RFsR8lyDCVQAycoVFm5_MfajIglbfJ4r1ZGXjfKh0PaOpYNT5UMF2By0L-utqW_sE_Owyiq2daPVbiKhFyMGBp8Lb68lyg6PVLPm0SNzntoxPZDkHgqF1CvdslM8xBtJu8kHNYH5RVyVeQeuktNbI2vlme-Jgj8PQiWXYCOcj2Gdul6aeWQkLvZY_qb4jOZwifS2EQRezP25tEkAl2BGRNPuk0N8tvfcxoY8Z3etoOT7NRIKUWPDisfJcdxlC-MJJHXYVpRAFvE3yfOcDJZgpTMV78suZqMH2rCobB7h91SRmu8EEmo0yhNg8mj2-DH4WT5MRWtqioJIbbKKk9Q59ZgGkG3KVJaKNqkl4iGHwq-wZ0VL3CAPbF6S4ZqxcYuvU7L7Bys04vbTkJDh3tRElfZmkdo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوهی‌های‌بامزه هاشم‌بیگ‌زاده با حسین ماهینی دو مدافع‌چپ و راست سابق استقلال و پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25343" target="_blank">📅 11:26 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
