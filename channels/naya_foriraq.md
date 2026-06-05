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
<img src="https://cdn4.telesco.pe/file/azJYVzDI5kLT4r27UEBmCaLniOZTvgoIfPljZygJCDJpsdHju-13ZvX42akG-74Acv2F8rhHxbtXJFUNFmZxMNDAdiUPBKqwaDF8GyAaF-GYEf5jeDBAeEGSxhm3ZtmMOCb7jpCamN9fKIL9zukcVgs9-fL7GLsNTxpABJJJNgJLW4cXBJfpxuTuIfIQw9i4zYqNC7O60mcL_Jz4FQnP_OPYmfW6yFHFDVQyacd2A5y1MViMs1XKaw_wq2vD9kuwJPyd3LZfwNcg-4iYsvtXiFojgU_DUmCDFW76pdfVHNtG_79mZcZIXVNiDoXxjWX8iyH7nOcV4ciwik0Ij0Bc1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 252K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 22:28:18</div>
<hr>

<div class="tg-post" id="msg-77121">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🌟
🇮🇷
إعلام أمريكي حول ايران يدعي: الاجتماع مع الخبراء النوويين لا يعني التوصل إلى صفقة، لكنه يدل على جدية المفاوضات.</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/naya_foriraq/77121" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77120">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇹🇷
‏
خفر السواحل التركي:
مقتل شخص وإصابة 4 آخرين في هجوم على قارب صيد تركي في البحر الأسود.</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/naya_foriraq/77120" target="_blank">📅 22:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77119">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🌟
🇮🇷
إعلام أمريكي حول ايران يدعي:
الاجتماع مع الخبراء النوويين لا يعني التوصل إلى صفقة، لكنه يدل على جدية المفاوضات.</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/naya_foriraq/77119" target="_blank">📅 22:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77118">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26eeb049c1.mp4?token=dE3XsrXR5rn34pdqIhTlotP3zUXfIzv_Yte3Nl7iRpHy0xqQd1T6CZX-KC9L0taMZc7BMQGTFdaRNoon6JBlb1_V81CROTHB69btlULEbfoxP4wKF5mLEYUKMR2FP9CWrDkoRJQonCQqiMtr6JOF2_Gd8WbH0xZGH4rG7-4oZmEGPlDhsxzTAmg-suKKhsYV1O8LJQHD5C-pkBBv9gR43YFGIaZTUVii30_MHHP8ihKbtnP-NeOZWP7pyXYBp7cvqa-rSwI6HyiGApC_3SY0V3bssJE952KK1HB6pofZAPM_eQ0cgmBQtEoW7IcWcNANXegK-u94OaoClOLSB9L-PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26eeb049c1.mp4?token=dE3XsrXR5rn34pdqIhTlotP3zUXfIzv_Yte3Nl7iRpHy0xqQd1T6CZX-KC9L0taMZc7BMQGTFdaRNoon6JBlb1_V81CROTHB69btlULEbfoxP4wKF5mLEYUKMR2FP9CWrDkoRJQonCQqiMtr6JOF2_Gd8WbH0xZGH4rG7-4oZmEGPlDhsxzTAmg-suKKhsYV1O8LJQHD5C-pkBBv9gR43YFGIaZTUVii30_MHHP8ihKbtnP-NeOZWP7pyXYBp7cvqa-rSwI6HyiGApC_3SY0V3bssJE952KK1HB6pofZAPM_eQ0cgmBQtEoW7IcWcNANXegK-u94OaoClOLSB9L-PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
المتحدث باسم الحكومة العراقية: أيلول 2026 سيكون نهاية وجود التحالف الدولي في العراق.</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/naya_foriraq/77118" target="_blank">📅 21:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77117">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
المتحدث باسم الحكومة العراقية:
أيلول 2026 سيكون نهاية وجود التحالف الدولي في العراق.</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/naya_foriraq/77117" target="_blank">📅 21:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77116">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇺🇦
زيلينسكي: اختار الجانب الروسي الحرب مرة أخرى - سمع الجميع رد اليوم. كان ردًا ضعيفًا. إنه ببساطة لا يريد إنهاء الحرب.</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/naya_foriraq/77116" target="_blank">📅 21:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77115">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2764a561b8.mp4?token=O6H7xtZ8evuj18MBC4kS3JJ9f7rlurW9cZmNgF_wBCRXBRiN2bxTLOqUVYa_A3gPFcU-cEKss_ygY0ydNwGKDs6ff49dP0nFz2F8NPucHRgOaGqSvsfG5pJwfuUyal1ce2h49w5AcTfLTk7xVqkz32ZkIOf5DMcXbY4tD9ksSo-JQgeuNA-tXtbuU_4TwrXg3jsfaCMpLcxFkB7gUQE1tn8voo3TT4qXTpwNCkbeaCUu691Zle_euhLyYwjWltVyOOBLpJuCiAJ6m31dGTGnVgwZt0A-CyoFbCVGwpTF14SGW7rkFSxWrQmu_kC6xdM7vbW5swTBj8Wl4tSMUF_6iGnJ0lSPayF36UYoSXOqm-pPf8ZkEoqAawntZZheEhpqjonDPAkn-_ovk_ytRGb9cQJmFZnHerAi4ZaoTN5B-qgE5007WFghePlX1pDeEdFUdMW2LckJEMKnTxQ8PuqePMfW7jzQvvTKwftSi1fUQUIWHtTAZZLws7Y4-pDYl2q_8N9b102b1aF6LTRI4A1ivKg-sgbVw14n-Gwx8AzuWNLUxEP18ENzYTIcT_-e-c15NlJ3rOMlu7lUVky0EHLexeXKZzRAM-iS6h0ye3kh6FMF3AgTjrg1Sol0L5UKH2ieK9jXQrXwsom_YIWr_1KMeHKW3qUfkwiW_lzPYlEyvSU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2764a561b8.mp4?token=O6H7xtZ8evuj18MBC4kS3JJ9f7rlurW9cZmNgF_wBCRXBRiN2bxTLOqUVYa_A3gPFcU-cEKss_ygY0ydNwGKDs6ff49dP0nFz2F8NPucHRgOaGqSvsfG5pJwfuUyal1ce2h49w5AcTfLTk7xVqkz32ZkIOf5DMcXbY4tD9ksSo-JQgeuNA-tXtbuU_4TwrXg3jsfaCMpLcxFkB7gUQE1tn8voo3TT4qXTpwNCkbeaCUu691Zle_euhLyYwjWltVyOOBLpJuCiAJ6m31dGTGnVgwZt0A-CyoFbCVGwpTF14SGW7rkFSxWrQmu_kC6xdM7vbW5swTBj8Wl4tSMUF_6iGnJ0lSPayF36UYoSXOqm-pPf8ZkEoqAawntZZheEhpqjonDPAkn-_ovk_ytRGb9cQJmFZnHerAi4ZaoTN5B-qgE5007WFghePlX1pDeEdFUdMW2LckJEMKnTxQ8PuqePMfW7jzQvvTKwftSi1fUQUIWHtTAZZLws7Y4-pDYl2q_8N9b102b1aF6LTRI4A1ivKg-sgbVw14n-Gwx8AzuWNLUxEP18ENzYTIcT_-e-c15NlJ3rOMlu7lUVky0EHLexeXKZzRAM-iS6h0ye3kh6FMF3AgTjrg1Sol0L5UKH2ieK9jXQrXwsom_YIWr_1KMeHKW3qUfkwiW_lzPYlEyvSU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
01-06-2026
ثكنة زرعيت التابعة لجيش العدو الإسرائيلي شماليّ فلسطين المحتلة بصواريخ نوعيّة.</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/naya_foriraq/77115" target="_blank">📅 21:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77114">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🌟
🇮🇷
ترامب بشأن إيران:
نحن نحقق نجاحًا كبيرًا مع إيران. هم ليسوا في وضع يسمح لهم بامتلاك سلاح نووي.</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/naya_foriraq/77114" target="_blank">📅 21:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77113">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي رفيع المستوى:
في الأسابيع الأولى من الحرب الإيرانية، استهدفت عدة صواريخ باليستية إيرانية مركز العمليات الجوية المشتركة التابع لسلاح الجو الأمريكي في قاعدة العديد الجوية بقطر، مما أدى إلى إلحاق أضرار جسيمة بالمنشأة التي كانت تدير الحملات الجوية الأمريكية في الشرق الأوسط لأكثر من عقدين، وجعلتها خارج الخدمة.</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/naya_foriraq/77113" target="_blank">📅 21:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77112">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c380297c3.mp4?token=HeQ9c6rGhTTdzlRQU7OIKeCZ1LUHsv20wjAyDzno6W-Lppztlx4xTOTIN1iMh12MGHkmZdBsqhF45qUoMkyvW6D01L3Vxjl9myNTtMoEliQiYxL7hYKYbs6i973VPEjGNTpazJATXrQHg-d_nVJbksOfayB92YH4E5Z-Qr1W2jlwrOYInZGKJ15y60BrSK5i-26WZ5EtNajpmS4_wVtK-H1c8nWyNR3yKyhaekJh68TUKz-446unGmTE-m0yDsq754-6GfXcxJed3xQPl0m_zpgdN6dGL52iLGYmjJlYlW471Vo679YMbNpIFIx10uziOqtOxEdCCAbNb_-6-OWmBD70ral6Ss4BUHrNmmI9z9cnGBv8U4DgzwSXjFIXR7e0jU7inh9_uKFkFxxfHa-GMt5lg5D-2aQdmJUa8RkkXzCqf-_BV3l5M-wwDV0FtGRy0QPL7pudAoeALF39H390mynxaJp_sNuxCsKkjPMmjU4eQpH9eYb4HSrqufzbeOKcazIH4gekmx10jjtIsoYnexc0tm4knesJS2ySaodwGGcwbRT9jg8a0s6ntqE0IIcNr9PeWfgJu3oa_pREd6EYBpnpMWFYGmQzreYc-IcFewBbnkZXmQC-MPUFZ5XViNWh0VWXD6BDKqLkmSxenbsdS0KOZCT4iEeMw_fh0Md5LNM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c380297c3.mp4?token=HeQ9c6rGhTTdzlRQU7OIKeCZ1LUHsv20wjAyDzno6W-Lppztlx4xTOTIN1iMh12MGHkmZdBsqhF45qUoMkyvW6D01L3Vxjl9myNTtMoEliQiYxL7hYKYbs6i973VPEjGNTpazJATXrQHg-d_nVJbksOfayB92YH4E5Z-Qr1W2jlwrOYInZGKJ15y60BrSK5i-26WZ5EtNajpmS4_wVtK-H1c8nWyNR3yKyhaekJh68TUKz-446unGmTE-m0yDsq754-6GfXcxJed3xQPl0m_zpgdN6dGL52iLGYmjJlYlW471Vo679YMbNpIFIx10uziOqtOxEdCCAbNb_-6-OWmBD70ral6Ss4BUHrNmmI9z9cnGBv8U4DgzwSXjFIXR7e0jU7inh9_uKFkFxxfHa-GMt5lg5D-2aQdmJUa8RkkXzCqf-_BV3l5M-wwDV0FtGRy0QPL7pudAoeALF39H390mynxaJp_sNuxCsKkjPMmjU4eQpH9eYb4HSrqufzbeOKcazIH4gekmx10jjtIsoYnexc0tm4knesJS2ySaodwGGcwbRT9jg8a0s6ntqE0IIcNr9PeWfgJu3oa_pREd6EYBpnpMWFYGmQzreYc-IcFewBbnkZXmQC-MPUFZ5XViNWh0VWXD6BDKqLkmSxenbsdS0KOZCT4iEeMw_fh0Md5LNM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله ينشر:
لن تكون آمنة...
לא תהייה בטוחה...</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/naya_foriraq/77112" target="_blank">📅 20:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77111">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
مصدر أمريكي:
منذ إطلاق عملية الغضب الملحمي، تم تنفيذ 39 مهمة إجلاء طبي، 18 منها حدثت منذ إعلان وقف إطلاق النار قبل شهرين تقريبًا.
‏بعد عمليتي إجلاء طبي أمس، ارتفع عدد ضحايا عملية "الغضب الملحمي" إلى 410 جرحى، مع إضافة جريح واحد إلى إجمالي ضحايا البحرية. بينما بقي عدد القتلى في العمليات عند 13.</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/naya_foriraq/77111" target="_blank">📅 20:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77110">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇷🇺
بوتين: زيلنسكي طلب عقد اجتماع لكنني لا أرى سببا للقاء ونحن بحاجة إلى اتفاق سلام دائم.  كييف اعتبرت أنه من الممكن الانتقال إلى مناقشة عامة، وهذا أمر غير صحيح على الإطلاق.  يجب إيجاد حلول لتسوية النزاع قبل لقاء زيلينسكي.  رسالة زيلينسكي تحتوي على عناصر من…</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/naya_foriraq/77110" target="_blank">📅 20:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77109">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⭐️
جيروزاليم بوست:
تتهم مصادر المخابرات الإسرائيلية نائب الرئيس جي دي فانس بتسريب خطة موساد لاستخدام القوات الكردية ضد إيران مباشرةً إلى أردوغان، الذي ضغط بعد ذلك على ترامب لإلغائها.
الخط الأحمر لأردوغان: لا قوة عسكرية كردية بالقرب من حدود تركيا.
ثم استخدم ترامب حق النقض ضد العملية.</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/naya_foriraq/77109" target="_blank">📅 20:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77108">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🌟
🏴‍☠️
إسقاط طائرة مسيرة صهيونية من طراز "هرمز 450" في سماء البقاع الغربي اللبناني بواسطة صاروخ أرض جو.</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/naya_foriraq/77108" target="_blank">📅 20:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77107">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⭐️
الوكالة الدولية للطاقة الذرية:
إبلاغ عن حادث خطير بالقرب من محطة زابوريجيا النووية.</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/naya_foriraq/77107" target="_blank">📅 20:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77106">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fe0d451fe.mp4?token=v0A-LRIpAdVm2kHt6xT8hNrJ8NzuLIROzxevc7T-JpwzvpoP3Sf6mr_d4eCkvw-DV8-wTxVw33DBPbS7RKvCIFB6MLIKi9dfiBIuBDEELz5HsAmt_52v8hoGkt3tyGC4If4na7n0HI1CAJNBBDuRIZp9z6is_ElgSbmwtft18QLYsrB1UKKbym9R8RsNYYoTVbw9NBNVBAtIxMhXGm1gMV6dPQkS1SlKg0xRe5CnPLzL5w6Q4nbSd1pHQXw_Ksglk6DDjKzFMSQmpRTUy6hgo3lud8t9HhsrG6HLCfrqmHK9PcqKJ6qINHG6_YY3bdZvf1FR6MErGlQxmpmfUF7ZgWSW9hKSSrVfVvlNMapZ1vKHWYFX21Z7y43_X_YxajW2x_jCbE-4x8ZhmOsvcKZ3Rw3-9Y5l5QeRA9kOHLk0agVvbxavPIle_s46MDluZ4jIAeqeJE1w3RR2kpWVbYAbfgOQmtAdxhTENKJwVLQV3z5J-wi-IXuldr5u-rgKCi7jotybQEACl9XrZsvbGReRO8HZU2sZzWYufHV5Vzkm0eGz8LrmYQdl0eGp7boHLuAnDkL5SJYZ-0IcJ0oOOKteAUxCO-rAtEsXAHvXAmr9VbXrqyKSaCKQEbjEQcyuKAy2mcpML5cgbEtbF18omBzaTYxMs3bJ7aVo0mKvk6c_Jzc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fe0d451fe.mp4?token=v0A-LRIpAdVm2kHt6xT8hNrJ8NzuLIROzxevc7T-JpwzvpoP3Sf6mr_d4eCkvw-DV8-wTxVw33DBPbS7RKvCIFB6MLIKi9dfiBIuBDEELz5HsAmt_52v8hoGkt3tyGC4If4na7n0HI1CAJNBBDuRIZp9z6is_ElgSbmwtft18QLYsrB1UKKbym9R8RsNYYoTVbw9NBNVBAtIxMhXGm1gMV6dPQkS1SlKg0xRe5CnPLzL5w6Q4nbSd1pHQXw_Ksglk6DDjKzFMSQmpRTUy6hgo3lud8t9HhsrG6HLCfrqmHK9PcqKJ6qINHG6_YY3bdZvf1FR6MErGlQxmpmfUF7ZgWSW9hKSSrVfVvlNMapZ1vKHWYFX21Z7y43_X_YxajW2x_jCbE-4x8ZhmOsvcKZ3Rw3-9Y5l5QeRA9kOHLk0agVvbxavPIle_s46MDluZ4jIAeqeJE1w3RR2kpWVbYAbfgOQmtAdxhTENKJwVLQV3z5J-wi-IXuldr5u-rgKCi7jotybQEACl9XrZsvbGReRO8HZU2sZzWYufHV5Vzkm0eGz8LrmYQdl0eGp7boHLuAnDkL5SJYZ-0IcJ0oOOKteAUxCO-rAtEsXAHvXAmr9VbXrqyKSaCKQEbjEQcyuKAy2mcpML5cgbEtbF18omBzaTYxMs3bJ7aVo0mKvk6c_Jzc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
بوتين: أن ترامب "تم خداعه في الانتخابات" عام 2020، وأن هناك تزويرًا.</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/naya_foriraq/77106" target="_blank">📅 20:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77105">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⭐️
بيانات وتحليلات في قطاع الطاقة:
مخزونات النفط العالمية تتراجع إلى مستويات خطيرة.</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/naya_foriraq/77105" target="_blank">📅 20:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77104">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
02-06-2026
تجمّع لجنود جيش العدو الإسرائيلي وآلية نميرا عند الأطراف الجنوبية لبلدة زوطر الشرقيّة جنوبيّ لبنان بمحلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/77104" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77103">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇷🇺
🇺🇦
بوتين للجيش الروسي رداً على رسالة زيلينسكي: "اعملوا يا إخوان".</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/77103" target="_blank">📅 18:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77102">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇷🇺
بوتين: زيلنسكي طلب عقد اجتماع لكنني لا أرى سببا للقاء ونحن بحاجة إلى اتفاق سلام دائم.  كييف اعتبرت أنه من الممكن الانتقال إلى مناقشة عامة، وهذا أمر غير صحيح على الإطلاق.  يجب إيجاد حلول لتسوية النزاع قبل لقاء زيلينسكي.  رسالة زيلينسكي تحتوي على عناصر من…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/77102" target="_blank">📅 18:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77101">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff208dd296.mp4?token=rpUfZuu2Hr7OKL1bs02qVmk9v6L8QB5u8AIbTzhOZmmPQQM0VURcWPpzJNcNNEkOh0mMjs6EN6gMg6JDvlftkILzCtZEkMptN0OT3cPoy-9XH2qBY9caWoSY4vS9pFYVtChZ-cEBvop-kwalwloHrybKrOe_P_7t5flr3978jJOmQGRvJwva_-hL6SU0CZZ8tgl6SaJpXeutD2w96HVbCjlCT6ZTKwbnRSisk0gOwbFa_Uf2lakxFAvlJ9kEk6xCZ-xXTlEGc0gI_UKvtyqejlDK_Mz2jXNnzRYPdO9H5RmkpI_-HCO7K3HkywT8Uo96buEMwzg4AIiea_oicLaLBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff208dd296.mp4?token=rpUfZuu2Hr7OKL1bs02qVmk9v6L8QB5u8AIbTzhOZmmPQQM0VURcWPpzJNcNNEkOh0mMjs6EN6gMg6JDvlftkILzCtZEkMptN0OT3cPoy-9XH2qBY9caWoSY4vS9pFYVtChZ-cEBvop-kwalwloHrybKrOe_P_7t5flr3978jJOmQGRvJwva_-hL6SU0CZZ8tgl6SaJpXeutD2w96HVbCjlCT6ZTKwbnRSisk0gOwbFa_Uf2lakxFAvlJ9kEk6xCZ-xXTlEGc0gI_UKvtyqejlDK_Mz2jXNnzRYPdO9H5RmkpI_-HCO7K3HkywT8Uo96buEMwzg4AIiea_oicLaLBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
بوتين: النخب الأوروبية تثير الفوضى وتحاول جر المزيد والمزيد من الدول إليها.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/77101" target="_blank">📅 18:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77100">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🌟
🏴‍☠️
إسقاط طائرة مسيرة صهيونية من طراز "هرمز 450" في سماء البقاع الغربي اللبناني بواسطة صاروخ أرض جو.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/77100" target="_blank">📅 18:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77099">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال الصهيوني يعترف بإصابة 3 من ضباطه بجروح خطيرة خلال حوادث أمنية في جنوب لبنان.  إصابة قائد سييريت جفعاتي بنيران حزب الله صباح اليوم في زوطر الشرقية.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/77099" target="_blank">📅 18:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77098">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🏴‍☠️
جيش الاحتلال الصهيوني يعترف بإصابة 3 من ضباطه بجروح خطيرة خلال حوادث أمنية في جنوب لبنان.
إصابة قائد سييريت جفعاتي بنيران حزب الله صباح اليوم في زوطر الشرقية.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/77098" target="_blank">📅 18:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77097">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇷🇺
بوتين:
النخب الأوروبية تثير الفوضى وتحاول جر المزيد والمزيد من الدول إليها.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/77097" target="_blank">📅 17:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77096">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87e355bd52.mp4?token=U8Ph9G8TFs98zcOUfe83ZNZINIaHMaEpJXL0xdyCARswmCqYLoK5aDcFlaFWmMPcRXAz1LaD4__o2s1yz6TqHGLjqLvrWIVu-UTTe5PzrXIw-0PDAZySqlaer5nEy9taJTiVWq79-hD7TcI209PWHd9eik-Z36ewWCKHSfBheJtGv0bw0D7AomXqO7sSZBZSJz12PT-9g-v0FK8I_3VRJVL0Pvrb1FLD6ptPaii9VbOCVVQvi1s1xgeZ_X67ew5K7Si0y3Z6FuPeUovsPnvkTiWK0txjaOGizPiy05gZEavA0IpTUPt2ohsPfqrztVZV5K7HBtudrolTJxwIAhy6Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87e355bd52.mp4?token=U8Ph9G8TFs98zcOUfe83ZNZINIaHMaEpJXL0xdyCARswmCqYLoK5aDcFlaFWmMPcRXAz1LaD4__o2s1yz6TqHGLjqLvrWIVu-UTTe5PzrXIw-0PDAZySqlaer5nEy9taJTiVWq79-hD7TcI209PWHd9eik-Z36ewWCKHSfBheJtGv0bw0D7AomXqO7sSZBZSJz12PT-9g-v0FK8I_3VRJVL0Pvrb1FLD6ptPaii9VbOCVVQvi1s1xgeZ_X67ew5K7Si0y3Z6FuPeUovsPnvkTiWK0txjaOGizPiy05gZEavA0IpTUPt2ohsPfqrztVZV5K7HBtudrolTJxwIAhy6Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
انفجار محلّقة مفخخة تابعة لحزب الله بقوة إسرائيلية جنوبي لبنان..هناك إصابات في المكان.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/77096" target="_blank">📅 17:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77095">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ateloqZSXJ5yxiRMKZp6nLqkt-BP0VnM0erXLtBrRAg9-lB_gAtjJbPtl00k2Lun3SwnS-QweCrhxsg107igxFOFHuit6bVsaBdpWvbSILOiGi7QBa-ogxSUjiMZh8Cyya5KM6mXZ3DnaVsuVxyYamwqRFIDHiiLV3ObIcvMJTFmP_Bm4-6W-ECWhHQlKVGKlpfN4WrA0yF6SCxSbl0n_DKeCnxxPyR6ME9h9QDa1KEpVxdcRy7Eugmg7d_uU5Ps9cCqPOdO6V9ctinY4Ij0xP1jJ-tdX005SSeg5urrSNPRowGrQtjTYsL7vqVHXt66RkMAm9V9gjXFIBm7bDhu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استشهاد اثنين من عناصر الجيش العراقي إثر حادثٍ سير قرب قضاء الرطبة بمحافظة الأنبار
الشهيد حسين وهاب
الشهيد يوسف جاسم</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/77095" target="_blank">📅 16:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77094">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وزارة العدل الأيرلندية:
أيرلندا تمنع دخول الوزيرين الإسرائيليين، بن غفير وسموتريتش، إلى أراضيها.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/77094" target="_blank">📅 16:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77093">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
حدث أمني صعب ونادر في جنوب لبنان استدعى تفعيل الرمز العسكري “هاردوف 1”.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/77093" target="_blank">📅 16:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77092">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">في محاولة لكسب ود اسرائيل والتملق لها.. ‏الرئيس اللبناني جوزيف عون: نعيم قاسم لا يمثل الشعب اللبناني.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/77092" target="_blank">📅 16:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77091">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇷🇺
🇮🇷
روسيا تحصل على استثناء من ايران
صرح السفير الإيراني كاظم جلالي بأن روسيا، باعتبارها دولة صديقة لإيران، تتمتع بمسار خاص عبر مضيق هرمز لسفنها البحرية.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/77091" target="_blank">📅 16:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77090">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">في محاولة لكسب ود اسرائيل والتملق لها
.. ‏الرئيس اللبناني جوزيف عون: نعيم قاسم لا يمثل الشعب اللبناني.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/77090" target="_blank">📅 16:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77089">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد
من عملية استهداف المقاومة الإسلامية بتاريخ 01-06-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي عند الأطراف الجنوبية لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقات أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/77089" target="_blank">📅 16:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77088">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/77088" target="_blank">📅 15:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77087">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/77087" target="_blank">📅 15:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77086">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وزارة الخارجية الألمانية تحذر بشدة من السفر إلى البحرين.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77086" target="_blank">📅 15:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77085">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇷🇺
🔥
مدفيدف : دكتورة أورسولا اللعينة وصفت انفجار الطائرة البحرية في كونستانس بأنه "نتيجة مباشرة لحرب روسيا". ننتظر من هذه الغبية النووية أن تستنتج أن انفجار مقر الاتحاد الأوروبي في بروكسل على أيدي النازيين الروس هو نتيجة لعدوان كرملين. ملاحظة: هذا ليس تلميحًا!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/77085" target="_blank">📅 15:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77084">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69eb1c51d0.mp4?token=H3qVHdxUXySQzlQNYIH-0_BX0sVvBBN5vPeFiJWbgiVQvq0R94AKNM42bXX4Wq8MUN16HxN0671cYc60o0Wya7vPIPy7FakflCHDlg-0remgW5c6-dnPMAzp0pMn57IXlPM9itHrAT9QGMV5xPmvEnMXPg5VDJ6zwJWY5fcJykUlNaL345BzDF06iYKVHPf9FXV9hyegr_xW4GBXuwSO9XYDcedRB36IrNlMgggeVciE2GLgqq3b8wwbmyLik2wzhSjCWRErCBe1gqCsdCScf7jt9LutEsNZxmAaOgUd9EqlZRYvQHjK9tv6Cpbrr_6NyWBXlDBK6yI4HkE3NPZZoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69eb1c51d0.mp4?token=H3qVHdxUXySQzlQNYIH-0_BX0sVvBBN5vPeFiJWbgiVQvq0R94AKNM42bXX4Wq8MUN16HxN0671cYc60o0Wya7vPIPy7FakflCHDlg-0remgW5c6-dnPMAzp0pMn57IXlPM9itHrAT9QGMV5xPmvEnMXPg5VDJ6zwJWY5fcJykUlNaL345BzDF06iYKVHPf9FXV9hyegr_xW4GBXuwSO9XYDcedRB36IrNlMgggeVciE2GLgqq3b8wwbmyLik2wzhSjCWRErCBe1gqCsdCScf7jt9LutEsNZxmAaOgUd9EqlZRYvQHjK9tv6Cpbrr_6NyWBXlDBK6yI4HkE3NPZZoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ايران تطلق صواريخ تحذيرية على مدمرات أمريكية حاولت تعطيل التجارة البحرية والأمن في الخليج الفارسي</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77084" target="_blank">📅 15:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77083">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ايران تطلق صواريخ تحذيرية على مدمرات أمريكية حاولت تعطيل التجارة البحرية والأمن في الخليج الفارسي</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/77083" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77082">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31294dea6.mp4?token=Ts9ZpjVdkfLDLXMd1dTma4DU-NwIt8c4iECrcpTMzKV9-HOTsppOrENb_BWh4z6wqcDtv-kob9a1dmZ4jbFm4kLEgwscr6o8pb0C9Jea_OcJypIr8afTkKDIrTU76Fwo5nTROFDrgdsVBv-HVYDE_5jJbyfaMGimmhE_ymA1Sa0giRBbmCGjiqd_8xQ2vbv1AGutiKtDxmLlwFBkQpWKt7Fp2MOv-XeA1Pw_gIEscRULJJgzdLM2DAYPMKXoGsyZEfwW7Lyb8Vcw0upU7b3neQgstBPotVsx9GoHVLhl4zZhTehIBH1xfdQ62imNnMeqVTl-3lfoyFe1fEbFzo-Cjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31294dea6.mp4?token=Ts9ZpjVdkfLDLXMd1dTma4DU-NwIt8c4iECrcpTMzKV9-HOTsppOrENb_BWh4z6wqcDtv-kob9a1dmZ4jbFm4kLEgwscr6o8pb0C9Jea_OcJypIr8afTkKDIrTU76Fwo5nTROFDrgdsVBv-HVYDE_5jJbyfaMGimmhE_ymA1Sa0giRBbmCGjiqd_8xQ2vbv1AGutiKtDxmLlwFBkQpWKt7Fp2MOv-XeA1Pw_gIEscRULJJgzdLM2DAYPMKXoGsyZEfwW7Lyb8Vcw0upU7b3neQgstBPotVsx9GoHVLhl4zZhTehIBH1xfdQ62imNnMeqVTl-3lfoyFe1fEbFzo-Cjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقتل عنصر من عصابات الجولاني واصابة 8 اخرين كحصيلة اولية بعد انفجار عبوة ناسفة بصوامع الحبوب في كفربو بريف حماة الجنوبي</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/77082" target="_blank">📅 15:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77081">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPz6JD-_8SdwEr4bhC-t67b0hwOKkFFLqOw1_vb7KPPHSqkUApHeYfBr-0wFiHG-n0XK2Agt4HFXCp5leaWOG2V59GtHS6YLq_KguPnx50Aa05O-gTGr1senUqNZjfqnrolE_ouHo-giV_z_7PXJk3EvKdrwxUXM2-wC2h7ODpXshYYH_fFZl6vsbxbp0pn0o9bgQwDocfmQIRXqziGp-Ic3e46lGePxBVJivs2w_SrfhF1YPMgThawO8f9Q4W_XTTde3xF2T8nl5PK4C4qOKMUPazJ71nnnskcSvnFM8w58DZPI5yjxGmSMCewz0SCrqpq1TbklyqKq-d6mVydt0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مالذي يحدث في بغداد   ربما يسمح بالنشر</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/77081" target="_blank">📅 15:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77080">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مالذي يحدث في بغداد   ربما يسمح بالنشر</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/77080" target="_blank">📅 14:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77079">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مالذي يحدث في بغداد   ربما يسمح بالنشر</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/77079" target="_blank">📅 14:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77078">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نشاط يعتقد لصالح جهاز الموساد الصهيوني في العراق   ربما يسمح بالنشر …</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/77078" target="_blank">📅 14:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77077">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مالذي يحدث في بغداد   ربما يسمح بالنشر</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/77077" target="_blank">📅 14:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77076">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مالذي يحدث في بغداد
ربما يسمح بالنشر</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77076" target="_blank">📅 14:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77075">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
إذا صحّت تفاصيل الحدث الأمني في لبنان، فهو صعب للغاية.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77075" target="_blank">📅 14:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77074">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 01-06-2026 تجمّع لآليات جيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة العديسة جنوبيّ لبنان بصلياتٍ صاروخية.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77074" target="_blank">📅 14:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77073">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجار مخلف حربي في مقبرة وادي السلام بمحافظة النجف الاشرف العراقية يسفر عن اصابة ضابط برتبة عميد وزوجته</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77073" target="_blank">📅 13:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77072">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682a69e92d.mp4?token=SnHGFMoioqn9G3xzRGKwRfnLvC_qnvci7B_Li-u2_tkhhMPfIGWh8yJNlCRlWfJA6YsgoK-7mXrFgibKhrcALYo5nzBpeMbOFWOHTayK4rfzeWsXJxeUQVReavSNwfpjgf-j7twSN-hYG2ZoFb0lr-RidsEkypFYUPl9q4OSW0I0oDtVfbvHrrVrL-f-MawqDeFYHAAYRPFX0zoo8VKfu9mMnQZFo7kG3mLw4mKG4phuUSI65g0nmG39N8VbHfVQugeiHONk_U4F9gQuELia3eilVwx1Ec1jKLsa4ICn7wS5R9V77MEGkxCTDI-dE_qLVYRE8CW1EQAILrya-d1jmx7BCxj7n6nXBshhB7QvgK36P-5WpxC3BgmgQWXrt2_tBPTfn_QJuF7DP-OfaD6sqmnz0JH6nELGQZW8HQVZY566MALJVXarTOhS3nOeQl7tFcZFq3w16FGS9XNrWt57FvUl1-5z8A2FFDi4VW2HBdAD3rD2PhahuYzxkCmkWVf8zvB8hlyzYBldIb6vX5v5xw1-6LuQ4VC5RCXwf08hK5jpr2mZgAXq6sOUQd5Ny0VLwlLFZAXNAuEz42-_AI9HuO9jTIJJJ2tVpycGQI--4YnHvsBrZPJrNtkAHvvOhR764PuCZSCSFBkDJ5cd99523opIukhtasAJOS6cEQt0ZX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682a69e92d.mp4?token=SnHGFMoioqn9G3xzRGKwRfnLvC_qnvci7B_Li-u2_tkhhMPfIGWh8yJNlCRlWfJA6YsgoK-7mXrFgibKhrcALYo5nzBpeMbOFWOHTayK4rfzeWsXJxeUQVReavSNwfpjgf-j7twSN-hYG2ZoFb0lr-RidsEkypFYUPl9q4OSW0I0oDtVfbvHrrVrL-f-MawqDeFYHAAYRPFX0zoo8VKfu9mMnQZFo7kG3mLw4mKG4phuUSI65g0nmG39N8VbHfVQugeiHONk_U4F9gQuELia3eilVwx1Ec1jKLsa4ICn7wS5R9V77MEGkxCTDI-dE_qLVYRE8CW1EQAILrya-d1jmx7BCxj7n6nXBshhB7QvgK36P-5WpxC3BgmgQWXrt2_tBPTfn_QJuF7DP-OfaD6sqmnz0JH6nELGQZW8HQVZY566MALJVXarTOhS3nOeQl7tFcZFq3w16FGS9XNrWt57FvUl1-5z8A2FFDi4VW2HBdAD3rD2PhahuYzxkCmkWVf8zvB8hlyzYBldIb6vX5v5xw1-6LuQ4VC5RCXwf08hK5jpr2mZgAXq6sOUQd5Ny0VLwlLFZAXNAuEz42-_AI9HuO9jTIJJJ2tVpycGQI--4YnHvsBrZPJrNtkAHvvOhR764PuCZSCSFBkDJ5cd99523opIukhtasAJOS6cEQt0ZX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناشطون على مواقع التواصل الاجتماعي السورية يتداولون مشاهد لعدد من الحوضيات العراقية التي حولت وجهتها من مضيق هرمز باتجاه الأراضي السورية مؤكدين أن الوضع المعيشي بدأ يتحسن مع وصول النفط العراقي لدرجة أن بعض أنصار الجولاني أصبحوا قادرين على شراء ربطة خبز كاملة بعد أن كانت تُعتبر حلماً بعيد المنال مؤكدين أن استمرار الإمدادات العراقية قد يفتح الباب مستقبلاً لشراء دجاجة كاملة بدلاً من الاكتفاء بمشاهدتها في الصور</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/77072" target="_blank">📅 13:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77071">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مشاهد من الانفجار الذي وقع في ميناء كونستانتسا في رومانيا.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77071" target="_blank">📅 12:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77070">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835fba7d0d.mp4?token=Oq60zRQfrhAVXu0j8VJdQYrzk-mZBxi86OustfUI46VsVrH09WRrfRYE9JqyOpebATge3Rf648JqqwReoZdOg21Xi0YBFGeq2wjP6VtXvDbylHR2863NlTDEexEXCLmG7tviXxkEP5d0LHKLkwNOG5dRboKCzmIKUCcpMoGNAyoNbW7a5hlMGqaFqGhiRMt0FmggUV6UJJeRDix0SGEr6Qvn7WGu2IDhJlQeYny7K8L1pbHUy_wnuEbvXt_mgI4n_erVNqSuVHcvH9ZX21Me4VxByPOGE1Zzww6wfnWsevYIwa2avyi_5j1eIUEFJFiakthiHK1NiQXj9a5MMaLiRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835fba7d0d.mp4?token=Oq60zRQfrhAVXu0j8VJdQYrzk-mZBxi86OustfUI46VsVrH09WRrfRYE9JqyOpebATge3Rf648JqqwReoZdOg21Xi0YBFGeq2wjP6VtXvDbylHR2863NlTDEexEXCLmG7tviXxkEP5d0LHKLkwNOG5dRboKCzmIKUCcpMoGNAyoNbW7a5hlMGqaFqGhiRMt0FmggUV6UJJeRDix0SGEr6Qvn7WGu2IDhJlQeYny7K8L1pbHUy_wnuEbvXt_mgI4n_erVNqSuVHcvH9ZX21Me4VxByPOGE1Zzww6wfnWsevYIwa2avyi_5j1eIUEFJFiakthiHK1NiQXj9a5MMaLiRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
مروحيات إنقاذ تجلي جنود مصابين من جنوب لبنان وتهبط في تل هشومير وسط الكيان المحتل</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77070" target="_blank">📅 12:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77069">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">إعلام خليجي: الفجوة الأساسية في المفاوضات هي الإفراج عن الأموال الإيرانية المجمدة</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/77069" target="_blank">📅 12:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77068">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-o23b8cF862B-U_lXSZT4GlDqCNtuXc6P8i4gamSgmVx8_LokseMLez2tEFfFmMV5gVe3WPCCzkpGVkpo_aOUaEYLMybswRRv8o_gFPZcoZEbw7-Aob_Gj7RsI3O-g-VfGUYUyI80zJY5qsVrdw427_JXgCUbLllcqJzSfs7utUSdYmHpvZDW64ShqTtjuaEyohzZ0JfIlN9LCRxaALPQzRW-zz6cdlicGXe1_j47etkE6s5maQRhcMVrYQluF9lAzxLJ517c3RmrpFnxnabmQdjkkmYAmex42tG8R14vbZW8fszF5XS-OMmfoBzpru9Szg0-ef6PEd9qoQ7qCDBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من الانفجار الذي وقع في ميناء كونستانتسا في رومانيا.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/77068" target="_blank">📅 12:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77067">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c17006916.mp4?token=oMSNvGMjfRNRV2YRL_gctjxXjJmNRBPXTkjWbOPhAOg3BdSRVJKO6op63U9DYxbxJTsU69ZglS7_66YuJ5NFrw6V3LWGh-HiMYmyCd8kmejoEQvLgDnMGs0qRFIJXDitxYPJL6JMeW3yfkl37F2kfhjgPyaqcBpHxlZudxfmHJou2sGtxBX1XiAQ4iXC6vQsgkckwEmspHR75wKC1yCDLZzfWr1dKYbgcGYNfNd2Ws6tUd1TgqTFfAcpPReL3qjUc9-8khH-1_K4-W0OJb45u0Y4V2q5A288bc2MlbvHw_ptxr9GOND2vgs9S6GAlvxE7YNV2SahaMAMaaBFG1p8MjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c17006916.mp4?token=oMSNvGMjfRNRV2YRL_gctjxXjJmNRBPXTkjWbOPhAOg3BdSRVJKO6op63U9DYxbxJTsU69ZglS7_66YuJ5NFrw6V3LWGh-HiMYmyCd8kmejoEQvLgDnMGs0qRFIJXDitxYPJL6JMeW3yfkl37F2kfhjgPyaqcBpHxlZudxfmHJou2sGtxBX1XiAQ4iXC6vQsgkckwEmspHR75wKC1yCDLZzfWr1dKYbgcGYNfNd2Ws6tUd1TgqTFfAcpPReL3qjUc9-8khH-1_K4-W0OJb45u0Y4V2q5A288bc2MlbvHw_ptxr9GOND2vgs9S6GAlvxE7YNV2SahaMAMaaBFG1p8MjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الانفجار الذي وقع في ميناء كونستانتسا في رومانيا.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/77067" target="_blank">📅 12:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77065">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91e0827fd9.mp4?token=OAnAfVvraprm8BH88kS-GLBQJ9iYVxk2M3cFRCF4ywwuAYUuiqXnZ0TwODuVSJwvvynGRRfUc9YAPKfzjt9HRxs2I5VvShn197GV2OyTL1zpsjDrBmr9wZk1jyZJYnO-TbTV0dW2wK4RqrTICRVuLnAOmAvH4V_B4jtvILJEsx3yBpUwAN6pP_Bns-S5RS-ZA_tF-HzndAl3H5WO4PUHikl6GBFcN_uXlE7SX_wm3g25gMWNEAGsLRJ_pSXPuDn7CjyhvgHJ9XwDTcHk0uFvZNduNgBBx89Y37DYAGs_mY2xMkOScA37Vg47l4na0qXDIgQFpysavDR2Y3pWSEyNAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91e0827fd9.mp4?token=OAnAfVvraprm8BH88kS-GLBQJ9iYVxk2M3cFRCF4ywwuAYUuiqXnZ0TwODuVSJwvvynGRRfUc9YAPKfzjt9HRxs2I5VvShn197GV2OyTL1zpsjDrBmr9wZk1jyZJYnO-TbTV0dW2wK4RqrTICRVuLnAOmAvH4V_B4jtvILJEsx3yBpUwAN6pP_Bns-S5RS-ZA_tF-HzndAl3H5WO4PUHikl6GBFcN_uXlE7SX_wm3g25gMWNEAGsLRJ_pSXPuDn7CjyhvgHJ9XwDTcHk0uFvZNduNgBBx89Y37DYAGs_mY2xMkOScA37Vg47l4na0qXDIgQFpysavDR2Y3pWSEyNAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
استهداف صهيوني لعجلة قرب اوتستراد كفررمان جنوب لبنان.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/77065" target="_blank">📅 11:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77064">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🏴‍☠️
حدثين أمنيين جنوب لبنان  سقوط محلقة مفخخة قرب قوة عسكرية إسرائيلية.  استهداف دبابة صهيونية واشتعال النيران فيها.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77064" target="_blank">📅 11:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77063">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🏴‍☠️
حدثين أمنيين جنوب لبنان
سقوط محلقة مفخخة قرب قوة عسكرية إسرائيلية.
استهداف دبابة صهيونية واشتعال النيران فيها.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/77063" target="_blank">📅 10:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77062">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-v1KA-rMTiHoTJSC-fFkis_PyZuuRI-6VLmZthhEAkzU9q4khe5-gmt4GWbUVGHTr7g83qpbyRbrHaxNhS8oZsz_vxzglRXlz8Bl03kGqnTxfiHIh6dSiRXecYDN-uAT4OgAnIxAgxjSAEvbrBYAaZIsuN4-Pnk9AZy9_J4HUm0X8pyQ7pDR40iqmWDoFVqCE0GkF-3ZztYHvGPfyp_eVmN-2P24OUr03WgC0vxlWQVNpVGHrW0OL_Fb4v87n1vlDZt6iWk_p1XMGTFUrW_ZkPEyqcMizZFbz2DaEmWUOUQPttBkZXD4-YmV9qewEspygeCYpA9eS5eP-bvfpKdzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
قاعة الاحتفالات تسير على نحو رائع. إنها في الموعد المحدد، وبأقل من الميزانية (على عكس مبنى الاحتياطي الفيدرالي، حيث فشلت شركة "Too Late" فشلاً ذريعاً في إدارة التكاليف والوقت!)، وبجودة أعلى بكثير مما وعدت به، بما في ذلك مهبط الطائرات بدون طيار، وجميع العناصر العسكرية الأخرى العديدة، والتي تُعد جميعها حيوية للأمن القومي، والتي يجري بناؤها في جميع أنحاء المشروع المتكامل والمتماسك. إنها مطلوبة بشدة، وستكون مميزة للغاية! المرأة التي رفعت دعوى قضائية ضدي ليس لها أي حق في القيام بذلك. لا ينبغي أن تكون هذه قضية أصلاً، وهي تضر ببلدنا ضرراً بالغاً. إنها كثيرة التقاضي، ومدعية متسلسلة، وقالت إنها شعرت بالانزعاج أثناء سيرها بجوار البيت الأبيض، لكنها لم تذكر مشاركتها في أماكن أخرى بعيدة. فلماذا إذن تشارك في دعاوى قضائية بشأن مشاريع أخرى في أجزاء بعيدة من واشنطن العاصمة؟ هل تسير هناك أيضاً؟ كيف تسير في شارع مغلق تماماً عند مبنى الخزانة - لا يُسمح لأحد بالسير هناك؟ لم ترَ مبنىً قط، لأنه لا يوجد مبنى هناك</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/77062" target="_blank">📅 10:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77061">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b2abbb67a.mp4?token=n9_32ryTtiODRr02taAOtn6Kqf-WUFX6PLMVWuC_NOC-1xhBnUXMsN8M2Py4y1SaThxY3PRVEmmoIgFV2FSBfF2SgdQQb5bqLJlKyj6UoZb8n4E16xqOv0W9M6B6HMKCsKthLhLJUsbugv9UrnxllRVw4jTw9FggL2H135MQU_4yp_pnpNey8MEXkn7_sYhhE4X5Q__G0miyEWKGION7P7-g-k2lvOiy4SfU9AxmtTeIJSgCnctxoRFno3pvFkVrlnmdKOMGlvSUOkArspE3-oCaDw8won0O_P8cNY9aNsSqhOqLedOs6N89_TbV0twcSm3wSsg6Y3chg5A2zbIcFEj7Ra9JJEV2fyWmKUzemuDTCtzNEv2s6A99Wpjk_XklCR5ZFJy0albNBRn43u0c1LFZfeyu9sco2OnBNR8ESWA7HKN-u9Kp33GuKrci7503FqYi__L2cxavkPipENpUNQtNY9-57bSE4DHWsCOYtHwTZBRy6f-1qXuS57uFCFBn8WFeukYlIW13SSTR_gCOcHDKZXqsckjciCndyvFI4ypEt1r7W2t8_a30jMItvvXtSrrHzCpvzIiuSVTNWVD5LQPMO9t_NWJo-Q_P_MGO2VX_qZf4znksXAdX3l1bnIIdNhmQM3VYHAf05QovSd3bQguPZlZyYC7Ycyv0V2OjckU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b2abbb67a.mp4?token=n9_32ryTtiODRr02taAOtn6Kqf-WUFX6PLMVWuC_NOC-1xhBnUXMsN8M2Py4y1SaThxY3PRVEmmoIgFV2FSBfF2SgdQQb5bqLJlKyj6UoZb8n4E16xqOv0W9M6B6HMKCsKthLhLJUsbugv9UrnxllRVw4jTw9FggL2H135MQU_4yp_pnpNey8MEXkn7_sYhhE4X5Q__G0miyEWKGION7P7-g-k2lvOiy4SfU9AxmtTeIJSgCnctxoRFno3pvFkVrlnmdKOMGlvSUOkArspE3-oCaDw8won0O_P8cNY9aNsSqhOqLedOs6N89_TbV0twcSm3wSsg6Y3chg5A2zbIcFEj7Ra9JJEV2fyWmKUzemuDTCtzNEv2s6A99Wpjk_XklCR5ZFJy0albNBRn43u0c1LFZfeyu9sco2OnBNR8ESWA7HKN-u9Kp33GuKrci7503FqYi__L2cxavkPipENpUNQtNY9-57bSE4DHWsCOYtHwTZBRy6f-1qXuS57uFCFBn8WFeukYlIW13SSTR_gCOcHDKZXqsckjciCndyvFI4ypEt1r7W2t8_a30jMItvvXtSrrHzCpvzIiuSVTNWVD5LQPMO9t_NWJo-Q_P_MGO2VX_qZf4znksXAdX3l1bnIIdNhmQM3VYHAf05QovSd3bQguPZlZyYC7Ycyv0V2OjckU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفاة المرجع الديني آية الله العظمى الشيخ محمد إسحاق الفياض بعد تدهور حالته الصحية.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/77061" target="_blank">📅 09:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77060">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">استئناف العمليات في ميناء الفحل العماني لتصدير النفط الخام</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77060" target="_blank">📅 09:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77059">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRugNrxQbCrpNbOQrg7S_gh6qmyMk0rn3XBvfOyBnx7mc2qySZQFy71IWQrFJYOKmsnZu-_yQAPzofSDG4mGfZSc4gHH01Crh8lpuFl1s831drSN8V-1Bij8_YvTWruohmbTCEsvemVfUHaYGvtzWE85OU-msmxTM8lEac8hfT96Baa1XPpykLH0InMNehkYJv0REH85BFb-hOOBA-F4IvsNQMXH1-ke_liW9mzHXw18xxjWxtoXa-wI_Zw0OEvBijmO-R6O_fBfKQMQhtwIOBQZQbjcPA5A8bimI9glHV5RWgylrw9k-y8wvDUjjLSyQ0gw-oBP8JL6AVQCvuNk9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر صورة مولدة بالذكاء الاصطناعي لابن جو بايدن وهو يرسمه مضيف إليها عبارة أعظم رئيس.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77059" target="_blank">📅 09:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77058">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGzusmXVoTSddh2vCl-cF6q82qC5WYWRClUI5Sk7UNzFaNqdrEUN45N4S7sbRlFq1MM4hbZRzyKrzTbZXBxOGyyrZA7vquYR5TL2o6h4ZaevqkKB2xtD66MMj4G1p6kiGFWeuzTMd-UYdUeSe7HHvSQhxiNUivDvUyUm1OcwoEpFNP6JFnxcZJqxf-n1r7nJjOK0PVwgVy6nED9yKwV-dLMUJ6-hfy9QVpD_zn46gAlYOAJUhnBg04JwevhrArykm7PCzdLj1Z8Znd6NIKi6X7q30VvkDPRd6vPG-CRiejhjGd0myj-Tg0d0StyS8NUiHrl4t19vlHnThEgcLmiPtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
الدفاعات الجوية الصهيونية تحاول اعتراض صواريخ حزب الله شمال الكيان المحتل.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77058" target="_blank">📅 08:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77057">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXXz_fKQUQRp0retMjUZpiD7TUK_Ed3wIuRpc-8LSM_MOlNlBGAIBduvorrNGm4j-GzMYjzKHEhDJTxUUdK2yy5PsyXDZs3UjzZhOkqzn5BchjJggWt4qkDtishWvJrj7xC6xeirEwJw2fJnmSEaMS7Xz3KKlSx3bssCI7Lit6dDXGLb4BQrJa6vHFlbKrxS4pAYNL_nfNj4c1mZd-Yxm_wUPJ2fzweZHLGKxu8UNWcYpwWzQgv6XZVYpMrAajdP1mA03MqZ1eRPYHDwy2BHO_z9XdQk6WHqIzyJf5N_paBmGmAqYd-QaPj1q2j538Qt0tCBLTjMtaA--5pAGm4dNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب : انتخاباتنا في كاليوفورنيا اتعس من دول العالم الثالث</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/77057" target="_blank">📅 03:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77056">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwLPvRrys84HQp8aI17VwBqZ35nIE4th-lT1V8IbG7FVRwK0WNV6FT9V0C3ZUQqvQCnjhWD62ZMa8Nb6YrsXn2hOKXH5UveBkPa1M1dz7U4LUqLwWReXNSHfbT3gis8jkuK5NT1AckV6xulMZBP7-QP-Gj-08nXwbMmGVVwdcp-l70U8waiCv5VDleq10gtLu8h_z6sYWwLxk4fV_YGNRZUL5Wvx0o8PfW10mcg1b1iG6jBrzp1Mlhr8Z55ohIXyeSQNRMb1alh7mL65cgkG2SEtDq2JvQhLEDR_Ic891Jn--PKLoSfI4CMzml3pmlJW9qqcS9MP1BrWWep51fBb4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السيد المكصوصي : من
كنت مولاه فهذا علي مولاه ؛ تسليم ذو الفقار هو خيانة للبيعة ..</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/77056" target="_blank">📅 02:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77055">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">استهداف هدف معادي الان قبالة سواحل جنوب إيران</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/77055" target="_blank">📅 01:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77054">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/77054" target="_blank">📅 01:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77053">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6-gcuOuzyqlPqAalFxmvw8J2Uinj0eer1MwcJwNLcr13wP7Z4hAQq7rNLvqfuNq3UAIadQKrsz0lUU5ej9SHbBnCGtpiZXlRV-ehMpM1cMtMS-jxDe8iEcf2lW9p9FuBeWSTc3q0AdANaaMheVk93HDtMR7LrdF_8Y0OFBBuSm_NNdfSs1dy41YBGSFu_GatZsVRpjIDBR8v_U4YcOoDM9rdA4KkCYfFXLSw2W4400DejITCbFkp1UiRV6xNjav9UUndUC4mj8D3rpdInDUQQpFIlOd0raFUZ-HmC38X1znqYkr_r53p6aNpiKDplNwsp01dd7SQxNAjPxJZkGr-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الأمين العام لحركة أنصار الله الأوفياء الشيخ حيدر الغراوي رافضا تسليم السلاح: بنادقنا هي الامتداد الطبيعي لـ"ذو الفقار".</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/77053" target="_blank">📅 01:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77052">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/727569b896.mp4?token=GnDSRUyJtqGT9oDmldJCUUol1o5KmmRqfMhoSCj2Ntn0LB04_z1tS984Ajj9weRCESPvD_idKnQtj71Mm6S3ERHYPg8Rnrcbayo906PEdtgFSgKVNhqGaDFTC53GiSfwGhqgtgG7QkkwpFHASM2p7g6H-SybBugePTCtVzYR4mfM0ZF5OJbpActjIBp-lvJ9dmSrjcgIoh6bG-15n42SonJb3R9diPAf5SLIV2T378MasHn-NM6r7eEexjFDsrnspV6t32U8k0yhsmlRQRgZNbxgEBMDkfivVcJVRfDle1PdDn7QI-IhOSlRGTa_SXS2QagIbXuFj46vM1zaXbqZjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/727569b896.mp4?token=GnDSRUyJtqGT9oDmldJCUUol1o5KmmRqfMhoSCj2Ntn0LB04_z1tS984Ajj9weRCESPvD_idKnQtj71Mm6S3ERHYPg8Rnrcbayo906PEdtgFSgKVNhqGaDFTC53GiSfwGhqgtgG7QkkwpFHASM2p7g6H-SybBugePTCtVzYR4mfM0ZF5OJbpActjIBp-lvJ9dmSrjcgIoh6bG-15n42SonJb3R9diPAf5SLIV2T378MasHn-NM6r7eEexjFDsrnspV6t32U8k0yhsmlRQRgZNbxgEBMDkfivVcJVRfDle1PdDn7QI-IhOSlRGTa_SXS2QagIbXuFj46vM1zaXbqZjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواطنين يرصدون ظهور اجسام غريبة لليوم الثاني على التوالي في سماء ناحية النخيب غربي العراق حيث مقر القاعدة الاسرائيلية المكتشفة مؤخرا</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77052" target="_blank">📅 01:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77051">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شبكة CNN: الحاملة كلفتها 13 مليار دولار</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/77051" target="_blank">📅 01:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77050">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شبكة CNN تبث مشاهد لحاملة الطائرات الامريكية "يو إس إس جيرالد آر فورد" وهي مدمرة بعد هجوم ايراني رغم النفي الامريكي</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/77050" target="_blank">📅 01:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77049">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07cb994ab4.mp4?token=KWlYN2vkK7-uIYCwTFCxNgSL4Y9uIsJ0YBaT9iS4bH6RZusHrVN0VqoSp4QGg2KntuXFQxAfukBPseWPV12hPn97c65UziQlQAp-PCJHSHPYTUPZ9BgqttcJKm9lzqJzhJ6PqL8UeJb4GLa5IHXGB_AMizwSYMp8ki1bvmPubTE1joXXfQgMbRQ_F8RxbMWA4fXy8aGbVBkbgVEIb1NM4XXbmJ_AqdXPmlpGL19d3Iv-Xm7gav1fwyNeUfGaWInhLNAZT3G2sN70HF7cobiDzMFB_2DARsTZi_Qj_U7Ndho22OB0nVWWGq9qTHYRgZal6FAQjD0A9Pin77h_JBUGsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07cb994ab4.mp4?token=KWlYN2vkK7-uIYCwTFCxNgSL4Y9uIsJ0YBaT9iS4bH6RZusHrVN0VqoSp4QGg2KntuXFQxAfukBPseWPV12hPn97c65UziQlQAp-PCJHSHPYTUPZ9BgqttcJKm9lzqJzhJ6PqL8UeJb4GLa5IHXGB_AMizwSYMp8ki1bvmPubTE1joXXfQgMbRQ_F8RxbMWA4fXy8aGbVBkbgVEIb1NM4XXbmJ_AqdXPmlpGL19d3Iv-Xm7gav1fwyNeUfGaWInhLNAZT3G2sN70HF7cobiDzMFB_2DARsTZi_Qj_U7Ndho22OB0nVWWGq9qTHYRgZal6FAQjD0A9Pin77h_JBUGsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبكة CNN تبث مشاهد لحاملة الطائرات الامريكية "يو إس إس جيرالد آر فورد" وهي مدمرة بعد هجوم ايراني رغم النفي الامريكي</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/77049" target="_blank">📅 01:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77047">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVJzHi4cZ9m89knXXHp27Yve4etDHg_WtFyxNHM95nonWjAR4IMRksCjZ-H1q19T3WtaL2KeakNl5AmoZxklMn0J1ZzYju-WO6rDDje1Z447b1IYfITT3E9h6m2dtsBXa309JBNYxgvQ-thtekZ1eAspHfYbpxn5_-uCYk6nDZQQ_QT8cLeSxFxugBQfkuxEYqhizad6HGV4-u8h7QtqKvd1TuHuFw3qDmHH0PDD6s5-kJvpOb_CDgH63wAxqoSrI5NxZRZoC7GJcDeJHdYPBqiM1Lz4DH6FbiTe8RLvDR9kTqMAbWx47VSmpOo4oWCSZaPiopwZDxem3Iz_y3LyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZycoF17onRuPylS_xIzuWlz7Wz6fjd7UfRgtI-SyauKuXi2kCb8C_I5yaKhx6Ca0G5bLieWyAq5Mr7GNN0g1qNSXeQCG1-Pi-IwiUiSn7pRHNsHEdjoA-2vrg1XKGHZ77NooYYcz6HLmrE6UIi_puIeqUvynbUGyd8RgbCkP7FZUW8tz4r71TAxe61I9vEG399lM5QzZjw3aoYdukuvWtbJ5stMIcPgeb90gfgkDh-I0ZW_8cxWmFho-3y7y8hP1Uvmo7rhfRHectGOnmkwUeauwBYXSbi8eHcyRmluEgjlRuOKBGI814h4rKvLkIWGSradB1SasxZJ1uo7QmaTNUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
شبكة CNN:  عندما اندلع حريق على متن حاملة الطائرات يو إس إس جيرالد آر فورد في مارس، أصدرت البحرية الأمريكية بيانًا مقتضبًا قالت فيه إن الحريق قد تم احتواؤه، وأن اثنين من البحارة قد تلقيا العلاج الطبي لإصابات "غير مهددة للحياة"، وأن حاملة الطائرات "جاهزة للعمل…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/77047" target="_blank">📅 01:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77046">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0TE69xSMw-4sopYcYHC3y5uMPt1_XuLyaybka2cciEjVvIzfTMN8yfYIn6u2DXG7X880LV7I6X0EejBlRJVQsS4KSjzkf1QSMwBlUknhtc6LZpxAoFxARpthbLRupVNMK-sfJW2vM7diou4FaCWQPIvOpsoGqIaL_xB6NtiwbeYwSLmsxux2yeUzjsJVAtTxUbcXtd7m_jEpVQ3THjRXHqDym5UCnd-THHvt2NFe1udVCsJuRasPD8FAfwYfHbp8xyRRZRraaUmOs7haXVTcrtocTjDdwao7rxhwVhdqYFy0IohYQpF5QwBsllVCGRlnJdXLM3zha8Y3cXaZwhu8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/77046" target="_blank">📅 01:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77045">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/77045" target="_blank">📅 01:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77044">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">الاعلام الايراني:
‏تم رصد حريق بقوة تزيد عن 300 ميغاواط في جزيرة داس بالإمارات العربية المتحدة؛ ويبدو أن شيئاً ما قد تم استهدافه أو تفجيره. ‏تُعد جزيرة داس واحدة من أهم مراكز تصدير الغاز الطبيعي المسال في الإمارات العربية المتحدة. ‏الحريق عمره حوالي 12 ساعة، مما يعني أن الحادث أو الانفجار أو الهجوم المحتمل وقع خلال النهار، وليس في الليل.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/77044" target="_blank">📅 00:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77043">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
التلفزيون الايراني:
مقتل أحد ابرز قادة العصابات الإجرامية في جنوب سيستان وبلوشستان والتفاصيل لاحقا.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/77043" target="_blank">📅 00:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77042">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏ترامب عن السيد مجتبى خامنئي: ‏في الواقع، يتمتع بسمعة طيبة للغاية في بعض الأوساط. ‏يقول البعض كلاماً سيئاً عني، لكن الكثيرين يقولون كلاماً سيئاً عني. هذا غير صحيح على الإطلاق، بالطبع.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/77042" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77041">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e18f8c0b54.mp4?token=hLET_7rT91fGWn8UDNp-jymxF1CjK2VsW8-hvu1cyT0Qrb5oHMsVgnoQJ3CM2Me1xlN9pNPs3DnyG7ZKCARh7CpdsJPL_MILaPK70Gev2rbad9aUOpJ9EeWosubS8qo74BknPVQPCGhE5KCjAkeqI30ZeeKJ462HevnAa3AZWggQS9455WCSul2cafOBdvZbUFHGK1bVukt8G9fLgSZEzKk-ePMzjXi6V29WcXcPvR-B0yH5Ta6t-TBkF2AMmXYp0l4MNkW6IrGjPJ_qOXLBvd91uYTr5cg8c8PIBegQD0j_9ZPstIsfgPSkpNzWQ04PtSFSAXFhtaAfPLNw9DTWwxp0l-WxgQxD6X3fRFEuIVgGtH9iWXrIHnugDyS3ZUy_HO41-Uv4ESV0NCdYHOqZX1D1Jb0LFniaHDDP-MY2vHofNAbBIOggTn3KAGbAv8A4HCF3MnT5RrpII0dmfR40L7MX8uv9vMnA7TJqNOOrAp3cCx8Rr0UCXsJ9n-WHVjMY-wIeYuAHQGBc9PR3A_p9DzK_v9esdz8m-IrWKoaTrUqnt66Zz-6q1PIC0xGmC5Gy8bJ0g2w1_UJvz2PYRojdyppOjqnUxFqG98BEYmVyRLRRaSfXeSSxAdb2h_x8OgFMuNGeSxq7QelZ4GPcps85SC5L0LwGFJiE9goF9vc6I64" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e18f8c0b54.mp4?token=hLET_7rT91fGWn8UDNp-jymxF1CjK2VsW8-hvu1cyT0Qrb5oHMsVgnoQJ3CM2Me1xlN9pNPs3DnyG7ZKCARh7CpdsJPL_MILaPK70Gev2rbad9aUOpJ9EeWosubS8qo74BknPVQPCGhE5KCjAkeqI30ZeeKJ462HevnAa3AZWggQS9455WCSul2cafOBdvZbUFHGK1bVukt8G9fLgSZEzKk-ePMzjXi6V29WcXcPvR-B0yH5Ta6t-TBkF2AMmXYp0l4MNkW6IrGjPJ_qOXLBvd91uYTr5cg8c8PIBegQD0j_9ZPstIsfgPSkpNzWQ04PtSFSAXFhtaAfPLNw9DTWwxp0l-WxgQxD6X3fRFEuIVgGtH9iWXrIHnugDyS3ZUy_HO41-Uv4ESV0NCdYHOqZX1D1Jb0LFniaHDDP-MY2vHofNAbBIOggTn3KAGbAv8A4HCF3MnT5RrpII0dmfR40L7MX8uv9vMnA7TJqNOOrAp3cCx8Rr0UCXsJ9n-WHVjMY-wIeYuAHQGBc9PR3A_p9DzK_v9esdz8m-IrWKoaTrUqnt66Zz-6q1PIC0xGmC5Gy8bJ0g2w1_UJvz2PYRojdyppOjqnUxFqG98BEYmVyRLRRaSfXeSSxAdb2h_x8OgFMuNGeSxq7QelZ4GPcps85SC5L0LwGFJiE9goF9vc6I64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجنرال رضائي لوكالة فارس:
إذا انحازت الإمارات والكويت إلى جانب الصهاينة، فيجب منح أبو ظبي وبوبيان للسعودية والعراق.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77041" target="_blank">📅 00:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77040">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">المراسل: أسفرت عملية "الغضب الملحمي" عن مقتل والد مجتبى خامنئي وزوجته وطفله.  ترامب: لستُ الشخص المُفضّل لديه، لكنه على الأرجح مُحترف.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/77040" target="_blank">📅 00:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77039">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/100efa8385.mp4?token=WkD7fDVWiNtykdIOzJWcsd_FxnnzciMoFniHAmP1GdBdY3YLqtS6CZt9zO6rl_I51pO1KgCUf44lnN4ooxoLGQpHDF7FYbVSn4JyAR5KOMb3J_P_qCDkUnaAgItzSEffDtVKvD6lFA_vgjf1P6Putf5kehPTTqpi0YkNLIJFUJKcvgS6G5ZZGwFQtrO8-VbWYjDlB4y_QUDt_pu6CFCw_Au2PzDLq8M8yzbMxiU5nbx5TVasxbnSMHG3e41zpM8LINOIs0BwdXXnttPIcrTDx4MfHQuDArQvi5iCFLR_gaCV75q8loFGwhKvf9hYm9guNeHoCqji6YNhyfGayCZNMIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/100efa8385.mp4?token=WkD7fDVWiNtykdIOzJWcsd_FxnnzciMoFniHAmP1GdBdY3YLqtS6CZt9zO6rl_I51pO1KgCUf44lnN4ooxoLGQpHDF7FYbVSn4JyAR5KOMb3J_P_qCDkUnaAgItzSEffDtVKvD6lFA_vgjf1P6Putf5kehPTTqpi0YkNLIJFUJKcvgS6G5ZZGwFQtrO8-VbWYjDlB4y_QUDt_pu6CFCw_Au2PzDLq8M8yzbMxiU5nbx5TVasxbnSMHG3e41zpM8LINOIs0BwdXXnttPIcrTDx4MfHQuDArQvi5iCFLR_gaCV75q8loFGwhKvf9hYm9guNeHoCqji6YNhyfGayCZNMIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: إذا توصلنا إلى اتفاق مع ايران، فمن الممكن مقابلة المرشد الأعلى لإيران. سيكون من دواعي شرفي أن ألتقي به.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/77039" target="_blank">📅 23:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77038">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامب: الدولتان الوحيدتان القادرتان على الحصول على الغبار النووي الايراني هما الصين والولايات المتحدة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/77038" target="_blank">📅 23:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77037">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇨🇺
🇺🇸
وزارة الخزانة الامريكية تفرض عقوبات على الرئيس الكوبي ميغيل دياز</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/77037" target="_blank">📅 23:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77036">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترفيهي اخر  ‏ترامب: ‏لم يرفض حزب الله أي شيء. اتصلوا بنا وقالوا: "ما رأيكم بالتوقف؟"  من تكثر شرب بالصالة الجديدة مال البيت الابيض
😄</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/77036" target="_blank">📅 23:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77035">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">#ترفيهي  ‏ترامب: لا تزال بعض الصواريخ موجودة في إيران، ولكن عددها قليل جداً.  من دمرنا كل شيء الى بعدها موجودة لكن عددها قليل
😄</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/77035" target="_blank">📅 23:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77034">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">#ترفيهي
‏ترامب: لا تزال بعض الصواريخ موجودة في إيران، ولكن عددها قليل جداً.
من دمرنا كل شيء الى بعدها موجودة لكن عددها قليل
😄</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77034" target="_blank">📅 23:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77033">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇷🇺
‏الكرملين عن رسالة زيلينسكي التي طلب فيها لقاء بوتين: الرسالة وصلت، زيلينيسكي مرحب به للقاء بوتين في موسكو "في أي وقت".</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/77033" target="_blank">📅 23:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77032">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c38afa62c.mp4?token=KFk26EZmsNOz8Yc-vUx-21Z5HfipCvVPMhGgTkthGxkO1D4S8DkssAVA0y6fXMgOnnu6TLmHV4V4F96m13G6NKgTTokgQGMJtGRP8mL58hKt2jg-1EJ5vC8Bm7R9AgslsAvqL1214cUv1juDN78e3ri6RQgA7oe4Wlk9dscCQMOCTbRM8BWtQsdvid23sTkd_fFboGMJ2AgY2YePI6nj7cR3k2I1btM5HngqytdHE6R7OPHNRCq6jwQHOZw4cKw-lWPaTFzBisT7PrcaFSKBd0KQEd1OtJEVvMSst2ZqsrsjEaGkUmcdbnF93fnERKWlXXC3jCO-mJ15RBnzumEm8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c38afa62c.mp4?token=KFk26EZmsNOz8Yc-vUx-21Z5HfipCvVPMhGgTkthGxkO1D4S8DkssAVA0y6fXMgOnnu6TLmHV4V4F96m13G6NKgTTokgQGMJtGRP8mL58hKt2jg-1EJ5vC8Bm7R9AgslsAvqL1214cUv1juDN78e3ri6RQgA7oe4Wlk9dscCQMOCTbRM8BWtQsdvid23sTkd_fFboGMJ2AgY2YePI6nj7cR3k2I1btM5HngqytdHE6R7OPHNRCq6jwQHOZw4cKw-lWPaTFzBisT7PrcaFSKBd0KQEd1OtJEVvMSst2ZqsrsjEaGkUmcdbnF93fnERKWlXXC3jCO-mJ15RBnzumEm8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المنتخب الاسباني يسجل الهدف الاول على المنتخب العراقي ضمن المباراة الودية التحضيرية لكأس العالم 2026</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/77032" target="_blank">📅 23:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77031">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇷🇺
‏الكرملين عن رسالة زيلينسكي التي طلب فيها لقاء بوتين: الرسالة وصلت، زيلينيسكي مرحب به للقاء بوتين
في موسكو
"في أي وقت".</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77031" target="_blank">📅 22:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77030">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
وكالة تسنيم الايرانية عن مصدر أمني:
- أحد أهم مستشاري رئيس الإمارات محمد بن زايد مرتبط بالعمل مع الاستخبارات الإسرائيلية منذ عام 2015
- مستشار بن زايد كان محل اهتمام الأجهزة الأمنية الإسرائيلية منذ عام 2007 بسبب طبيعة مواقفه
- المتابعة الإسرائيلية لمستشار رئيس دولة الإمارات دخلت مرحلة جديدة بدءاً من عام 2015
- اكتشاف أهمية مستشار رئيس الإمارات بالنسبة لـ"إسرائيل" تم في وزارة الخارجية الإسرائيلية
- الجهة التي اضطلعت بهذه المهمة كانت مؤسسة "ماماد" الأمنية التابعة لوزارة الخارجية الإسرائيلية
- مؤسسة "ماماد" لعبت دوراً أساسياً في اكتشاف مستشار رئيس الإمارات ثم توجيه مواقفه</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77030" target="_blank">📅 22:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77029">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
حدث أمني صعب جديد جنوبي لبنان... التفاصيل لاحقًا.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/77029" target="_blank">📅 22:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77028">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDt7bYO5dY8o8GzOaYr8ae2BZ8eyXQtT0FUWMsxB3eLGTAofaKMzoVtZZ5PhkX505GyErJGlIWg8p6qHqUAFjEbybU_zlaOuQ2LrrqZTB3RADQ082imhSuwVzgEDyJcVtVmrhs1oxnLiPgfYcf9ka_qtx5E_ghDzp97-E3lt4qfad2hnXZxuDC6yC8iXwyg0WB3OKkt5V7AW7OByaZdYqS2qM2yd5OU2oXRY_k2EuNb0noM_T_JSxphmNv2HgPuFHHWoEFPeabKdiDIPkkTvyF0jKVwEg1I9xyAtVEgrVrC-gBDkjZE9nyUU6Pcom0l5bI778HzOboJywEWGW-F-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جيش العدو يعلن مقتل ضابط برتبة نقيب من الكتيبة 75 التابعة للواء السابع المدرع في جنوب لبنان.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/77028" target="_blank">📅 22:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77027">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇷
نائب وزير الخارجية الإيراني:
لا نعتبر أي ورقة مع أمريكا نهائية إلا إذا أخذت ملاحظاتنا ومصالحنا بعين الاعتبار. نصر على وضع 50% من أصولنا المجمدة تحت تصرفنا فور توقيع مذكرة التفاهم مع أمريكا</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/77027" target="_blank">📅 22:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77026">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇱🇧
بيان صادر عن حزب الله:
يمعن العدو الإسرائيلي في اختلاق الروايات الكاذبة وفبركة الاتهامات وإلصاقها بالمقاومة زورًا وبهتانًا، ضمن سياسة التضليل والأكاذيب الممنهجة للتغطية على جرائمه المتواصلة والتي باتت مكشوفة أمام العالم أجمع.
إن اتهام العدو المقاومة باستهداف مقر قوات اليونيفيل في بلدة دبين والتسبب بمقتل أحد جنودها، هو ادعاء باطل وكذب محض. لا سيما أن الاتهام يصدر عن العدو نفسه الذي لم يخفِ يومًا انزعاجه من وجود القوات الدولية في جنوب لبنان وسعيه الدائم إلى الحد من دورها، لأنها تشكّل شاهدًا حيًا على جرائمه واعتداءاته وخروقاته المتواصلة لسيادة لبنان.
إن حزب الله يؤكد حرصه الدائم على دور قوات اليونيفيل في جنوب لبنان ضمن المهام الموكلة إليها بموجب القرارات الدولية، ويتقدم بأحر التعازي إلى قيادة القوات الدولية وإلى عائلة الجندي، متمنيًا الشفاء العاجل للمصابين</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/77026" target="_blank">📅 22:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77025">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbDKCAydEzyDbwacHu-0jx6Bkg2vdM5WPKyzhcMHHyWzJm0wWHrtzrlp-6RUIS43B1md9LKq5x0y75Ie_dR5dDoSDdeb4EX6KMnVOG_1KZhCjT77pWkMS2IFeYApcjc8Cs-ukWtoFlvdEWScyr31-OzeHsuLjmVrFKbOelGS9_SMkC1CqpYoBl195uSaqzIFAHkplynxnPmEKxA9NPpplfT0uFGMZzjUPwOAEFbTPKvgUa4qSKc-BpVbznUJJtM5HeJ_3NAilmPYd0S6UsAv-a3blTEt_36gqQBzWW-dKpR8SQH_gQwbt0i9rnV8ESnodHoDGvJBNEvz8lQVWRggHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
أعتقد أن لدينا أكثر الانتخابات غير شريفة في أي بلد، في أي مكان في العالم!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/77025" target="_blank">📅 22:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77024">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇷🇺
‏بوتين: الحرب على إيران صرفت اهتمام الولايات المتحدة عن أوكرانيا</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/77024" target="_blank">📅 22:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77023">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الناطق باسم القائد العام للقوات المسلحة العراقية: تشكيل لجنة مركزية عليا تضم ممثلين عن الدفاع والداخلية والحشد الشعبي لحصر السلاح بيد الدولة</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/77023" target="_blank">📅 22:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77022">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇷🇺
‏
بوتين:
الحرب على إيران صرفت اهتمام الولايات المتحدة عن أوكرانيا</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/77022" target="_blank">📅 22:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77021">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 02-06-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة
أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77021" target="_blank">📅 22:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77020">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي:  - قطر دولة صديقة لنا ولطالما جمعتنا بها علاقات جيدة جدا  - يا للأسف استُخدمت في الحرب الأخيرة القاعدة الأميركية في قطر ضدنا كذلك استخدمت الأجواء القطرية  - لقد أبلغنا الأصدقاء القطريين باستخدام القواعد الاميركية على أرضهم…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/77020" target="_blank">📅 22:09 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
