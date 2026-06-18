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
<img src="https://cdn4.telesco.pe/file/aAdX6S0ILmdi1Gxbz1E1AF8cK_yEwo1wsZW95sxfOuQPcDdHt31och6QtyLJ80kRVwE6DzQIkh4DwrhGVaL-CprmRmj2kw2j0j1A08b41OkUCP3VM4fbg1MoOEi32tbR0Ukyoh6Q-efTmLInsP1ib1VLmFjTYoA61Upn1sqhm3RpmFLooBLS10kcFzl_iN-bQvdl29grUZWQK3a1kXmqIjN_lCpQbUT6kijVqNkAvimkqXNoh_O1mZ2ixxdPdMGqC5yTEGalaiY6rlTLRX2MUgIeN2OAdRA7tzH6051D8iDBQSSm_DlLR2q1Vzx-sdwcaon8RPvsWmBCv1Ppn-jevg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.2K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 21:11:13</div>
<hr>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpM-RZ5JdQKGve3K5rgAZ-UJxoBkPBBHGtjSa93Mj1mK7_IRaTREVtZ1wfdJu1BMdp9dkoWji_x8RGL1pXiwSmyBS6ijjMOy0y0OsfkqGyc-G0O72jQyu2uolzLzCIfzeWRIFQiuIp3WdE-auPm20OM7uRUSBLSl8Lunlj3807mgU7iMdwVcUgFVKy5Ua-hARJtaoibGLgzZbkXU5err3_WZs7OW9CWri3bPH9KYpjZ4dt6Is1fvp3gTigvo5_E4pOu07I10mhKel7NNo8We8RzLGz4ixXdaQGY6e8yL_kVThGBwrqGA1_keHDsmsXfuMLm2KD70yuQiPTcetPsWSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=bioQav7JfjRE6SnxCODbpUoiens90aIeoHQefoi-jTOC6hZ8cQXGFADElz_qlLKJsf_ffFsk5D_Zix1SNJV2t9bBds2DwVtfsGY1XiS8XhNm0lsEjXMJw6ZTD8E7kGLMfnfIhV4slyyzszU8EZis7Ipou0C-yt4CurukKKk6fsLUAgMH18ultG3YMVYYlh5o-iL3OsAsOwYUHTSRanDJ-l6zaVR8kARTPDCTLaSCjLv3cLjoIJ9GD23bGpXAchhxFU4Gvpqbj6FaaqlWVTlxkczWubTl5atYdYoMVQLaeJYZIklyMk50EoPhnVhpymfmNMRhBlWPuuLX6djGO3vVjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=bioQav7JfjRE6SnxCODbpUoiens90aIeoHQefoi-jTOC6hZ8cQXGFADElz_qlLKJsf_ffFsk5D_Zix1SNJV2t9bBds2DwVtfsGY1XiS8XhNm0lsEjXMJw6ZTD8E7kGLMfnfIhV4slyyzszU8EZis7Ipou0C-yt4CurukKKk6fsLUAgMH18ultG3YMVYYlh5o-iL3OsAsOwYUHTSRanDJ-l6zaVR8kARTPDCTLaSCjLv3cLjoIJ9GD23bGpXAchhxFU4Gvpqbj6FaaqlWVTlxkczWubTl5atYdYoMVQLaeJYZIklyMk50EoPhnVhpymfmNMRhBlWPuuLX6djGO3vVjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyhagpcupVXjPk-nJKEJJ8eFP3HRp43PmbI7G265Q-OYFtT-KJAkqFZxy8bLm0kGY1zpdikpz3uUozvfH43cbsXwqJb4OcZ2ls3Xs__1fqMYcgaV5uQyLe0kuQAQy3b_KI9c7eZdrNx1w-jjpwwMUmgPh9wyCMB7xkDrQmQFQ7gJkt_HF4p9LJ03uPXAD1_-nlwdc_r-OJmoqMjlZMB9CH21NfJMdHq2RhQlfE3ITXxJzHX-PvPKLdjMaTWmW5Q_GlACaO9DqAtALNT4ue38sOX0HQYQVODwG0EdWd10BPHT48-eSuV0tLO65YayiUq6hv0TzFTBjbvPi-GZKCf1HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو
به
ترامپ
اعلام
کرده
است
که
اسرائیل
بند
مربوط
به
پایان
فوری
و
دائمی
جنگ
در
لبنان
را
در
این
توافق
رد
می‌کند
و
به
رئیس‌جمهور
گفته
است
که
اسرائیل
خود
را
متعهد
به
آن
نمی‌داند
.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDPUKyHHYioBeobAF_FBiqwj6fS_xju6xNXDRSUfat3VzjDKtZDxp2j-OtGRpwWrCRsld6WQUnb52VHNswBTVWoZ6HYMV8RQ79FQpjDNvgO4mIjyXYxfkRzy_Td4w7VUV9Crw-8ipAax0xpW5b045XmgL0AqAxkNX9tYlMG13w12gZzpMHrM3FQ1MGedrC7jJTinKv8L50sznVG7MkGaDwYG4QlMjkQJ41xsnkH0rG7omFdFjnxqhm7dGoZJCfh8oVuvY2cqYPL1PaUAGHabv19BuYgubVN-pOq_TLy3rRa3iTPMMNtI89nk6rCtwnNe7iafuLDjLNus0Xbw6hSyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جمهوری اسلامی تا اینجا با آمریکا به توافق رسید، اما هرگز با مردم ایران همراهی نکرد
و به توافق نرسید.
از قضا با اسرائیل هم به توافق نرسیده.
مشکل آمریکا با جمهوری اسلامی
برنامه‌ای هسته‌ای اش بود.
مشکل اسرائیل با جمهوری اسلامی،
اما هسته‌ای، موشکی و نیابتی‌اش بود .
مشکل مردم ایران با جمهوری اسلامی
اما ذات خبیث و خونریز،
غارتگر و سرکوبگرش بود.
اینها هیچ کدوم حل نشده.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYwsTfVckdui6X27eQmEuORjefB8vf3SxEdXfPDjvlwOAG6FcSMLuNOWbOlxweZa6P9gnf3YhjBvO-RIYXhhRaTKwC7HPrtj4gXlA09lIHju6tSQQCxB2Xq2bcRF4OZ622BdW5zJG-PkrVkcsBwYXLXb9QLjjyTbUXaxX4AXDS0EDOrOCg8lCtXzT1Y9JLMW_E5rqyx3LjnTRFeXq6rApmEmOC7d0j58DB2mOHQdvEmpRmKHws3wQUWL1OV5JUclPLiQn7AuijEgW5iNMHZuEu5iDw8CxBgUMXZBkGlfohEJtDokCrwBiJG3moP2V_C5S9JnaMQdOwmFsFMQDyKbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UP1OQZXMlBAqkFpy2LLUBCgV44cbR-pDocMzLAh8jIIxKGyCT-KofOjEvjXcELSuDnmEHvMJlXDwMkWU4g1qgSZ5YIu-henkAw7oCx0fhKvlqgSH84geZlyv-ojSVgZ4fHvFIgp6Gh6k5FGjfNXMIhnyGDW1BSlfXOgv-gTmKtY4nZVs9HyzHEUPaUNQ31aUYOom5PPmrQ9oacZZPZZ9G4ymZtb4mlrmDc4OQ342u7bnsxBxL4_bGdSIy7PbXBx2mGeYLDDZB6UfAqg6exDxjGSygVFvPUv_v1A9h2gm0Qg80LSsLAiWO1V9MYIF92LYNXO8qmGr_C3MhKZW_thSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=PFYVTojENTp-rtSRwmrybw8WHnFblqXWtxa09dp9EXczhG6vLvxtVsqEotljqkXaF8cXfo7U4hT0RjpraXSD1V-ZS750SinN8Pandu263YhTfTRdHqHvIjOtEoY-H311spWSktt9PwrIxmTxOh90KqGOqGvV1p0pNiWTviEb156_KNGzn1wyMn4yE19ewGcXPX0m40Z7dlsGhGi9vUKUndrulCQwVTTwSvnAzPq3-oPp1OpZDEJYga5ZMQd9afzXFsidtQN4I65o4Y4kcIkcl-0N0VbNv57uXn5kcjoa-9R6fCaWbX-mR-mQWIKdFqz9ed1dK8BGGQwPqJTPQqP6pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=PFYVTojENTp-rtSRwmrybw8WHnFblqXWtxa09dp9EXczhG6vLvxtVsqEotljqkXaF8cXfo7U4hT0RjpraXSD1V-ZS750SinN8Pandu263YhTfTRdHqHvIjOtEoY-H311spWSktt9PwrIxmTxOh90KqGOqGvV1p0pNiWTviEb156_KNGzn1wyMn4yE19ewGcXPX0m40Z7dlsGhGi9vUKUndrulCQwVTTwSvnAzPq3-oPp1OpZDEJYga5ZMQd9afzXFsidtQN4I65o4Y4kcIkcl-0N0VbNv57uXn5kcjoa-9R6fCaWbX-mR-mQWIKdFqz9ed1dK8BGGQwPqJTPQqP6pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O07E_z406qk9KhIxHXiH4rDy6WpaS0l11ZarOMDQD0TTyc635mHfDYYMg4kL08u6-HEXQK7FIyAKx95N9MjWq3hGqmmd7wQNgAkH2mFsVduIChjfFKI60CebQhOGoWxlUfZzhk71TkULT0VV38AP6G_-fT5CkQF-b-X9pBcWkBbJn6uneTlrnclKrGgy7TGuz0QPKNCfRsrG08ADHM1sLhvXpXgVOVwYxO5dsFOrgY7ul7UQRPvTjP3TWfp3YvdBRX2GnwSF4QQMLRrdnjCBcRbd4Iu8fmhLGDa-tht95C5s9z3bcrQYfmjNs2IhJMS1cYPRr2DgCEGb5vQT6mm0Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منهم صد بار نوشتم!
جنگ رو برای خونخواهی خامنه‌ای راه انداختن!
بیش از ۷۰۰ کودک لبنانی رو به کشتن دادن!
جنگی که نه به خاطر لبنان بود
نه برای منافع لبنان بود،
نه با سلاح لبنانی‌ها بود،
نه با تصمیم و اراده لبنانی‌ها بود.
یک گروه مزدور تروریست
از جمهوری اسلامی پول میگیرن
که هر چند وقت یکبار جنگی با اسرائیل راه بندازن!
فقط برای زنده ماندن شعله‌های
خشم و جنگ و کینه!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=SeWkIfxZ1chyMbAAtm5c0LKNkWbqR2iEHAXoj7V68xtpBWCi1i_T-auBP2Xmk3wDTzvqTyA7jqJKQ86yCI7Raz1t7dKFp58JPNocDsFdHpBZrDOrVWM09Q-6Pnmhqry5jiXQbmZGy5M1WdQhyltqhRUkZ8D0N2fFjD2qBx-msSU40Gw52cmzH9C_OgnYiU6yCS-UhjegKQxtWIAN3IYKNwldihqnibq6pG8P7NDzz50d15zT-T7vCHLu9K-LvkwidKxTkUrIAzcSHqVLgZSiTJTtjgAzHVaGxcePfz5zIlIRDajGxvVnsp1VI-GiyMMXV0u89fEiqGtK4pDGIVfeFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=SeWkIfxZ1chyMbAAtm5c0LKNkWbqR2iEHAXoj7V68xtpBWCi1i_T-auBP2Xmk3wDTzvqTyA7jqJKQ86yCI7Raz1t7dKFp58JPNocDsFdHpBZrDOrVWM09Q-6Pnmhqry5jiXQbmZGy5M1WdQhyltqhRUkZ8D0N2fFjD2qBx-msSU40Gw52cmzH9C_OgnYiU6yCS-UhjegKQxtWIAN3IYKNwldihqnibq6pG8P7NDzz50d15zT-T7vCHLu9K-LvkwidKxTkUrIAzcSHqVLgZSiTJTtjgAzHVaGxcePfz5zIlIRDajGxvVnsp1VI-GiyMMXV0u89fEiqGtK4pDGIVfeFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید برای من تصمیم سازی کنید
تا من تصمیم بگیرم!
قالیباف همون مجتبای پنهانه
مجتبایی در کار  نیست!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=Rl0RuRJXE7W3Q9nXjZgIs8sOEwF67_EuWt188Qw-nY01D7N6xzW95e70ht9H8DHqfuyECte2tBtKIB9XtFkkHjlrdO-sPlYxvNzhYpqjBjSz_6nwhMnS8pDCC7qRBOivrvLSoRGTH26E78pze217D8fACgLrJ9hCe11xPPLQfx36cih5SsWrXJmdSWmo7kKbVp5qbzc2AKCwPbNdGVBa-3yGJ15B0OMbSrRsTVojaqGrUyAWTCW6tt3hQN3gomNxhpieQVZueN8dyaENu-ifU3__rxSA80ZZujspGJu1IFW6IQtbKtzm-JTQolj2WXLmhhPluZHcaDhow2AiCccVNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=Rl0RuRJXE7W3Q9nXjZgIs8sOEwF67_EuWt188Qw-nY01D7N6xzW95e70ht9H8DHqfuyECte2tBtKIB9XtFkkHjlrdO-sPlYxvNzhYpqjBjSz_6nwhMnS8pDCC7qRBOivrvLSoRGTH26E78pze217D8fACgLrJ9hCe11xPPLQfx36cih5SsWrXJmdSWmo7kKbVp5qbzc2AKCwPbNdGVBa-3yGJ15B0OMbSrRsTVojaqGrUyAWTCW6tt3hQN3gomNxhpieQVZueN8dyaENu-ifU3__rxSA80ZZujspGJu1IFW6IQtbKtzm-JTQolj2WXLmhhPluZHcaDhow2AiCccVNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVFkyalSQdjsb0mOWl_I_EWuLKjTxsnPVYL6eACrT6J9bEgty0_qWDX4R79Zs-ZAlvpxcCpa4DtHTh4hqv5oJPCjJGMRQYU_S2ySghhsmwGO7MlDQEcTOHjaHW__KZG2vQRDOxUrjOn09Gii9m6KyZps4JsnXs49PunE3Uh5HkvF3LHHQmY7U7_9m_jkr0e9nTfzbJueWfaU8hFKCSVK3ArTjCaBi0dNt_nEl94P38vdCUt-suSp6PXpix8Ll0BHriiTdL3WKCduCx4VzxRLInNxEh7f4_4dl3i8C4ww7hMfAkNzK3NP_duxREw0zIeVUOd5-1-1Tbq0pFgur-NIgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=k2jGhWXEappobjWFiFNDFTU_4xRvN2frIwTvvxS2Ck4N9xWuGQ6RJYjXiO4_YBRH4Hf9uvb61VkGtgsYu4nXtIMMWjTE93Yoq6G9dAYILQsAnUGfXLnZhCs_MMoMtvhOOkHNUW09_8Q9xo7A-wkJJ4PLn3co2bmZaEVGeQcJmN06ozk3p6ymMmIUd7PjPkyMKp5-6VoX_ssIjotCS1I2JHFsxFtP59MMWiDgmPWvbsh_FN24V_rKrBnN1cRvLqDi_2CucnsZ5JhcF2iysQFlAfM6YC0J2AkTBOCJadIL_QAoPeW7HvajV_S6jN_2LirXYwSihXxC7eCUpGz37Q2qNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=k2jGhWXEappobjWFiFNDFTU_4xRvN2frIwTvvxS2Ck4N9xWuGQ6RJYjXiO4_YBRH4Hf9uvb61VkGtgsYu4nXtIMMWjTE93Yoq6G9dAYILQsAnUGfXLnZhCs_MMoMtvhOOkHNUW09_8Q9xo7A-wkJJ4PLn3co2bmZaEVGeQcJmN06ozk3p6ymMmIUd7PjPkyMKp5-6VoX_ssIjotCS1I2JHFsxFtP59MMWiDgmPWvbsh_FN24V_rKrBnN1cRvLqDi_2CucnsZ5JhcF2iysQFlAfM6YC0J2AkTBOCJadIL_QAoPeW7HvajV_S6jN_2LirXYwSihXxC7eCUpGz37Q2qNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=tH1KCBN0aSQCAU7AQgT5f3Fnf10lcwDYzau87ViPiBr8uubiGslhJwgmyHMVjopFDLy2mh93xcq6MA6pasVmBQZXNjX9mk9Q17w3iIwDAPJQCmOcAO1UWnib6CeI7PyKutz3Pu_A-6VhjgUv049Vj2OOYEPR7Gdcp-Je1noL5kPcYwr8k05EK9IKyhON53kxP4znJiQAnj3IoYmcF_MDLob6fynRi-brZVCDNmloHLAj7czQ1pd0RW-zOZZL8Lm0GgALCmJu_tBZpJuCGZ3ZSL54waUGU2brkgJ1WbWmSTkqs4Dl8fz5DXXDG70GonbdcjUh9q7WC5bOOOM82vY9Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=tH1KCBN0aSQCAU7AQgT5f3Fnf10lcwDYzau87ViPiBr8uubiGslhJwgmyHMVjopFDLy2mh93xcq6MA6pasVmBQZXNjX9mk9Q17w3iIwDAPJQCmOcAO1UWnib6CeI7PyKutz3Pu_A-6VhjgUv049Vj2OOYEPR7Gdcp-Je1noL5kPcYwr8k05EK9IKyhON53kxP4znJiQAnj3IoYmcF_MDLob6fynRi-brZVCDNmloHLAj7czQ1pd0RW-zOZZL8Lm0GgALCmJu_tBZpJuCGZ3ZSL54waUGU2brkgJ1WbWmSTkqs4Dl8fz5DXXDG70GonbdcjUh9q7WC5bOOOM82vY9Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPdj4wyP7gOGQ6byI49utaocXcQXmgc5fBx8dxrVugRDpVli4PiE9Cp60KGwvZtyei6OYU5uoCC2J-328L-VpM4X7ctn1VlVs1Y9xdou3qL2u0R-BS3mnSs9qD_Q6bFNcVKaM30Ng-rkcS0Aq4cEy3riqdK2wu8HxFDGGjE71AAXCCUqGZc4m18b7H875oaM5aByHrXmycIcXfi5XJpJfeH8IQ_58K8Amg9vwX-K5BrLT0AN5p7P7zML9bN-NGVi5QGD2wUAR7JdBCpqeFTIFcpp1eonc2cjYT1C2xY8R0UGuhLr5fiuCESAp0tqkDVrIkkxDc7TelbTrpaQy-Vgyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHywQ8l-Y3TJOvMWZ2Iwz02FvkCBLbqQLTVgBgTjjtsT_8-MCQW0zEHPIzSWB5fpd-01p_MjPw00LPDSPsqFTqRk6QY7FJVdJVgqFa2EVB9Sko6YDcsYmzE4c-lSE0EXflXuj8lUaX4a0_uO5waJeY9Bq6cXawa5sqGXusxb5P3mSWnBoH36uE2CRapPgYak03rEEN-jVRmANUmxLAB0mq2bjbKB8NAkxLeA8ZjJ00WVdIkYj1LTpVun8Sj5GS9l23NLyLcGKNB42eDqH7aenOVO4Q5onWFKafbUuxzUx_VSaLVpF9ZVmEpWz4KQjLCiQNBhgKRJUckiHI-MmRvGkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای حزب‌الله ۱۵ سال در خاک سوریه و در جنگ داخلی سوریه مشارکت داشتند
تا اینکه یک روز همه شون فرار کردن!
مجبور شدن فرار کنن!
نیروهای جمهوری اسلامی با کمک هواپیماهای باری ارتش روسیه به ایران گریختند، نیروهای حزب‌اله
هم زمینی به لبنان برگشتند، گریختند.
و بعد به سرعت نیروهای احمد شرع
سراسر سوریه رو گرفتند.
بین نیروهای شرع و حزب‌الله ۱۵ سال
جنگ و خاطرات خونین وجود داره.
احمد شرع اما در این ۲-۳ سالی که قدرت گرفته سکوت کرده، اما اگه نیاز بشه، می‌تونه تا ۱۰۰ هزار نیرو روانه لبنان و مناطق تحت کنترل حزب‌الله کنه.
انگیزه بالایی هم دارند!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uy6eISBimEAi5dSjRMfX66egI27Z3pA7USpl1q_ePE8ZFi7XI0urFnZ0Z70XrPgGh_4fCBJNAegwKaqZlMOLCwvCmWo6ACT8TrsqwjrSM64c0CDlmff9dHo7rjfzUlMpqLjoWXJCAYmSAnZDRvXikMJXlKQ74FK0WNqqV8Ka-N1ARZYr_RoctTW0AV1Z8OUg29iKJSeLqIQ6lV_mvofeUeLN744Bnpu9LzCqPByMgHGm0nmFHUZ9-gkNG2zSRH8L8OVLrrsO4uE30KysKn6ElibtisDJCOBlSz-oW6djpBtoyxt5KJJygzdosp4kK6kvt1b1IlBK-EaDrqMO74TRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBTbkSRiBU--0-ey3fNp_OfveWCmVOYw9sms0FevM9WuVJMKLg3ISqLhZKiq1gyJaDlesxzQBbtWY6xke-e4nbpliHVmM2uB0Xz_FNBLHDjiAnn0iLawMBB0jUCx-i83w2WDAYeRgoznxet_ryHSnXQP-2IvDFz4U5k3SOlKvIgLsXOzB-OW3u4ep8tdzeJeCzAOM4ijWg9f2HrpO2toadybq3MO4qMLUE4I1KzUxA2FToD3v3GS4rwG3DqNZqXhpY5FckX0jtjWmnhk4GzZMUWsCkgEylEhJAJvGa6mrvQkrVLCez0X4wW-J3ilDmS4Hx8z5IeEtZv4phh9nwdfZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=vlrpJhp7aiplZf3u1WDa-kb7vkDEPQa2_sOPaP0o4rm9LEAOyUD6Vb5HJMjY06l8TX1fCbk-vvcf4FpG3qAOWfSg-4ALo4xh7Ve9l8ksf5kb5hXpXoZIPtkX7X2t3RTrQOZl2FRRyClTOkg7SHruF4PHOGdEk2ZEqJSQ4g8uM4rrE5575YH6qgi3V13lwDOrcQUt0RJM0KyDn-f6ZBCUhC3Nx2V3aAlb02xZRSZGE5B_NACxr3cyuL5supVPlzQjVv40lMetjylxM8InFx7mG6UB7lRrWSzWrv9KUCE2g8EVWENbfSfSPuFR0Lr1E54xbRYIQz4W8R9qQIpogWiFvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=vlrpJhp7aiplZf3u1WDa-kb7vkDEPQa2_sOPaP0o4rm9LEAOyUD6Vb5HJMjY06l8TX1fCbk-vvcf4FpG3qAOWfSg-4ALo4xh7Ve9l8ksf5kb5hXpXoZIPtkX7X2t3RTrQOZl2FRRyClTOkg7SHruF4PHOGdEk2ZEqJSQ4g8uM4rrE5575YH6qgi3V13lwDOrcQUt0RJM0KyDn-f6ZBCUhC3Nx2V3aAlb02xZRSZGE5B_NACxr3cyuL5supVPlzQjVv40lMetjylxM8InFx7mG6UB7lRrWSzWrv9KUCE2g8EVWENbfSfSPuFR0Lr1E54xbRYIQz4W8R9qQIpogWiFvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieHueihTa_A11VNmb7-v7YcFD0z6AYIHaQm9FCpc9_L_pBphTbpn3nAGwUBXnj8DRWpX-zEW3txtjYdxT6CBMxv9mLeMhhB4I9-YMzukBmUHsYxUADn5L7MrSkr2nsXugb3kl-wW0uYbgas9_Q1poJkJjBdTKNoHlVaWN5fjjQHMyxhYTyMnBkUBrAso90pzpEFu6_bJrzPbC1m475w_uLz_VbphqJNW-WpTfQA77zpXqv5-ommywZvkweI_QDBLN35mom6NnPvf4vWx1VNYXrf3dzK86h8Cu1msXvtMyr52-D6DEHGivG-qmGk7hOJy_mOqrUxfEuVj_W_HM8h1WY0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieHueihTa_A11VNmb7-v7YcFD0z6AYIHaQm9FCpc9_L_pBphTbpn3nAGwUBXnj8DRWpX-zEW3txtjYdxT6CBMxv9mLeMhhB4I9-YMzukBmUHsYxUADn5L7MrSkr2nsXugb3kl-wW0uYbgas9_Q1poJkJjBdTKNoHlVaWN5fjjQHMyxhYTyMnBkUBrAso90pzpEFu6_bJrzPbC1m475w_uLz_VbphqJNW-WpTfQA77zpXqv5-ommywZvkweI_QDBLN35mom6NnPvf4vWx1VNYXrf3dzK86h8Cu1msXvtMyr52-D6DEHGivG-qmGk7hOJy_mOqrUxfEuVj_W_HM8h1WY0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUfdLLVEWrLNvMA6w1cFLlpIxF7kBsSLvoz7nlQqGvoxWdAXpUvQTuU1f8ckgDokDHJfxI6nTUd2Q09Fmwmuqo6ooZ66Zx53lOW-iR0xtniM1CdvkseTWPZRA5e3s3B0yLu2JLWQsrjs7uwwjZs0MoiE1YeTJknwPEq4Nlp0cSnqF2rvCn_B398Ji9I7tKnezz2ukJ9OWADl6LFWH0G_mBjQp5qk34IJLEWZcVt-T8h78HGeypkHYVS-DDH6R1bxcj8SzHYffxjxHa8akMCGYau7746HzJRXw4SywKxnX05_BAXxs0XX0epX8WSo-QFVl_0A1OBXcvTYTmirjf3FCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها
محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار
جمهوری اسلامی و نیابتی‌هاش رو به
«اختاپوس» تشبیه کرد و اعتقاد داشت
که باید به جای درگیر شدن با دست‌های‌
اختاپوس در لبنان و غزه و سوریه ، عراق و یمن و …..
باید مستقیما به سر اختاپوس کرد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5SP4B1rkalw9t0wN15YH5tTiEZKdzC-akGG4-hczJTUhxBMAyjqhSRwTfnqyBwkWgwprW311lOIDzXFL_HUnJJIKtsCf41GxlJOjpQIo2CQ5qoAf8Da8Pnc2iX12YXvfXgVQwnsclY4or94a5UM6bBFT55UyrRbVnM5wUKlTqsqRaYRBjOe6-fOr5RnC6N2d1qO5USZsWiII9XXwNQTg0Pzt5m8W6UVNA6sKUnSDWXC664BwDMmp4dlcOE9TerXsyu0kVaJ-nfkdeUJjU0DqUC0kJJCspgHyngqwSP4l6Atwdikqtsrgum1x9kRaanYGDzYNBN6S9q8Y8XQzRqwag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vl001x3N5SJMusGoNwo73kiIgm0ZkEMzS1SZCnjfuHjMSgG1t-hTV69BC8ucT37s1ZLoTKSjapnk-4YBHlBgx9u7tAQoLCpu-vzbXSEYuivTP-Xn-_eKE5ft-LoyMuSpzDBoPVCPvwufAWv9-29Tr5f7LgCScKKTIz1wizgNjq46GMbfFqsPif8m2YYvIKXEMYCBUL4DaWqYYgmfFyWjjjmOwLlS5lUY4Jq_Hcvga4OJUz3ZLqfHBCebkAZflldpr3Vt-MFG1TIPi-D-HWk0yd1xyyufc3efK7sKX6udiMKxN8nMMz8RSPlI4dZaLKzR9Lw9wcfOi2IbY8olsB77Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iMiOgVyh2I7J00llZ8WK_6mMWEC-BKKu2McIqlEdN_DUzu-ZBYTJWmiNhwyWyaS4pSBR1Wib-bV7TPFLCdNSSS2VkQt3sfs4AfiV5OQrEsxPZwSykoOnh2nblVquLFpGK9hqO0JDsKTuvNy7tCMgxUmDTXY_6szPnRpPgUm4kOxTEcUlzpYARcCjSea8OO9JmsxrR72Hyg-mTd1pXq_n8xNAGdxNmYb7WQ3xdswOW0N7m5V72H3m_arfH00deiVrz9s0wkMElPLh_g76OFoSjzqDFNsLUyhwhx-F6o8yCnopFQxsUfoYLqvVecLoZlAWx9NX3FwwtAuNvPM6yexr8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBQt9LylybsSk5jqFbfV5tLhKe1cl307F2fUR7LwpE-m6xocdFMc7ofDFQ1GwZwY3WTEZQoG-8iytYQMHVZLvrbb62aFrDsQoumzaLxc9d1KNDm0fZ7PUPLW2ge1HXwEh3wDPkCNCY0V_jGbxRc8f-fZT4zdsGiQaWbnbiRgkDAHTN8KAH_f3xZMVO85SrSNombbNuzJ1ueuYYmqHeLbk1UjjCBYTaFTqkSKnK3iWbOpF3ld41uKHYYXQysk44ieanov_TEcDNdWW4ZulWG86RUgpJMdJU1BGTcf82Bes9LURuemw2DJSwP1S2p6iUZD4UW2F8ap_kpjnWGYZHCeXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=cdon3y4f956sCi6YYZ5sJ5t7DjYaDRvROohrF7BjIMu-JHdakSrj4YLMWJWxqjvciYfr_KdRkejlD3U-A93cPZXPXBRU2NmNWeY2VpT7_2rr6firDUpNW8bWfOwVzxOv9CiLVIfbxNQsBN7xcsrVVpEFu8CMpcMAARSh-TMVaqJVoXWtc368Y4JMbD8ROMBLgWRB2Su0LuU7qT34t0bPSzrT8m-ZVTAgdxyUbifvE9OoFFj1ziqTDO1PLiZ1duA-rgp-6e-suHX3rhdEc9RPPwg1q29XGxgSpd8yCD15rs9BC_FLmPqU33-pyeO8pE6TVB_lzoLhAxWNYEdiuLtc3yipybpbBNbC309pB0FoUHK6mWO5_xPhWf0otdJ6FvJeBQGbx5shFJ9HKMFEIE4FPmuyjYZqlmVR8_FUtcZHx3Y-N40sysP82rE0WkPcxQb-Mg5rg9Zg4WZjZjvjV7fPjIiJfWZKax7m_HMOcB7u8QHl0F907aTIThGBvLRcyO2OGlhKKVWFoICkGA0e_deyY6a1A49fxBXBHqQZ08H6FE3U-AnPhCvpKfBhe7ttu26o85giDszTw3wCSjEevgxsMPt_E430F0L2dhRDnIu-9FpXNw0rhJmnPfWDAwRqrHJPfG4bLHwGQ4aVwnpgXOoaHVfZCIGEt9osJJ4dNGbOduA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=cdon3y4f956sCi6YYZ5sJ5t7DjYaDRvROohrF7BjIMu-JHdakSrj4YLMWJWxqjvciYfr_KdRkejlD3U-A93cPZXPXBRU2NmNWeY2VpT7_2rr6firDUpNW8bWfOwVzxOv9CiLVIfbxNQsBN7xcsrVVpEFu8CMpcMAARSh-TMVaqJVoXWtc368Y4JMbD8ROMBLgWRB2Su0LuU7qT34t0bPSzrT8m-ZVTAgdxyUbifvE9OoFFj1ziqTDO1PLiZ1duA-rgp-6e-suHX3rhdEc9RPPwg1q29XGxgSpd8yCD15rs9BC_FLmPqU33-pyeO8pE6TVB_lzoLhAxWNYEdiuLtc3yipybpbBNbC309pB0FoUHK6mWO5_xPhWf0otdJ6FvJeBQGbx5shFJ9HKMFEIE4FPmuyjYZqlmVR8_FUtcZHx3Y-N40sysP82rE0WkPcxQb-Mg5rg9Zg4WZjZjvjV7fPjIiJfWZKax7m_HMOcB7u8QHl0F907aTIThGBvLRcyO2OGlhKKVWFoICkGA0e_deyY6a1A49fxBXBHqQZ08H6FE3U-AnPhCvpKfBhe7ttu26o85giDszTw3wCSjEevgxsMPt_E430F0L2dhRDnIu-9FpXNw0rhJmnPfWDAwRqrHJPfG4bLHwGQ4aVwnpgXOoaHVfZCIGEt9osJJ4dNGbOduA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFcPeyD7Hv37nwrvuWTp0m4GE7mFO2oCni3HJiCdGc7XyofWXU4UX4H78lAHYhI5BKWjXsYvQUEUHLIdyU9o53NjNOcCD6H6_7nfjg6VwB2VoXZ-0f0-nNDxrVEcobcAc4gGJtStV6Ft6Wr88ElrgP0RsorGqugT0DZNd6FRgQ0dMvQ0uIdshRrcqF_oYmXHuTxfaArOHickMTctN87oB-f1E9uvu6CIkUX9o_uTnkmnoHd8mAQ1XBYUdArRLUCOJAtRwaqkPc0NTuGHdmwuXOK18LbUfs8_OynW7FBIgwtr1Z6qLv_cLHeO04T-t86Vjy5KqQaJpf01GN0kfOUiQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=B-q7es2uAOK10kZl7egCXbu2dDjv7izF5xCbLJQwGmQ6xhahD37-uBBZFHDR4-mtqNDbDh-Dui0H8h_gVUmNy8foVpPTxp3MQobkZpDgQ0sW2Mf2XFFKjHy-uOixbO3QoFaLe81qpe5xdM4TqXGSoJEfzMKsto_NgySSFTQo7QTnchFuai6XPZpzOFBJjObzVK8f6cXdCh9hV4AxuV9THqkuc2t2KDCQ40kKFLIBTF07bk4BkuVSXYIJsd70LF4OEnCKqFXlTk16V56cQHMAj_A1Dax7dlTi878vBP9Dn8rFn_aBU13fiPPjQIhUs3-a509Dy3qoMC0Da7FIMrCt-Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=B-q7es2uAOK10kZl7egCXbu2dDjv7izF5xCbLJQwGmQ6xhahD37-uBBZFHDR4-mtqNDbDh-Dui0H8h_gVUmNy8foVpPTxp3MQobkZpDgQ0sW2Mf2XFFKjHy-uOixbO3QoFaLe81qpe5xdM4TqXGSoJEfzMKsto_NgySSFTQo7QTnchFuai6XPZpzOFBJjObzVK8f6cXdCh9hV4AxuV9THqkuc2t2KDCQ40kKFLIBTF07bk4BkuVSXYIJsd70LF4OEnCKqFXlTk16V56cQHMAj_A1Dax7dlTi878vBP9Dn8rFn_aBU13fiPPjQIhUs3-a509Dy3qoMC0Da7FIMrCt-Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=hCd-_qHavlSAEyQUiY_XWMEHSY6IIygGRIGJ-qYOYxJdwsPmvQvZnAO7ECkiXqwngn8ieOCa85I5VkCmej_Vs1LoM70LBMlwt0289RlSvP0K4Lcn-rGlHbf7yOG8hs-L8x_FWfGf0wV_ft3JumrItXNjepZf3xlrB8OlTMza0krmvB_UEDCU7xjN8F2WgAFypbwCF1bZctoN0GlUoGK39fzbaLe7ihlqSY5P3FjJ8FMYWMmYveIrWwsBQjApdmK4q4_Vzq78P-BsMahH8e_-HqzBLWevIPH67J674Vs72_xkdAz4masdG9E_g1lornxH4apRd-UFWdQfwAjdTC4NfzphNoO8iO0Nv39b5QXtUbhN_cg1w5MSSi_jbLIy4XKkNxCU0_AIiOkf5uSBDvwJsKglpziWdKgYJz2MZh1BDDEjv7OM4R_5tHnExX9s0HKv3XXOGLT-Nl2dSkkjcQO3Hn8A32gX-_UtoY1Q-WBp7qHr8atuMRRJLaziRferoVtc-vz-Qwq74p_MCGlk9PdEhfHRmvwes3tQHvRxPilJdIB52Tia6wexlX8au7SdEVn4eze1bndZhvpD_MSWT6hZgS0PKnLHwsz_enmdkDh7716hSKykjQuvfgtpob8KqEjeOvSlVEeEltY-laGbUWyeLhVoOD5YZZQziL7uWQCWqeU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=hCd-_qHavlSAEyQUiY_XWMEHSY6IIygGRIGJ-qYOYxJdwsPmvQvZnAO7ECkiXqwngn8ieOCa85I5VkCmej_Vs1LoM70LBMlwt0289RlSvP0K4Lcn-rGlHbf7yOG8hs-L8x_FWfGf0wV_ft3JumrItXNjepZf3xlrB8OlTMza0krmvB_UEDCU7xjN8F2WgAFypbwCF1bZctoN0GlUoGK39fzbaLe7ihlqSY5P3FjJ8FMYWMmYveIrWwsBQjApdmK4q4_Vzq78P-BsMahH8e_-HqzBLWevIPH67J674Vs72_xkdAz4masdG9E_g1lornxH4apRd-UFWdQfwAjdTC4NfzphNoO8iO0Nv39b5QXtUbhN_cg1w5MSSi_jbLIy4XKkNxCU0_AIiOkf5uSBDvwJsKglpziWdKgYJz2MZh1BDDEjv7OM4R_5tHnExX9s0HKv3XXOGLT-Nl2dSkkjcQO3Hn8A32gX-_UtoY1Q-WBp7qHr8atuMRRJLaziRferoVtc-vz-Qwq74p_MCGlk9PdEhfHRmvwes3tQHvRxPilJdIB52Tia6wexlX8au7SdEVn4eze1bndZhvpD_MSWT6hZgS0PKnLHwsz_enmdkDh7716hSKykjQuvfgtpob8KqEjeOvSlVEeEltY-laGbUWyeLhVoOD5YZZQziL7uWQCWqeU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=i08sl5753WMY-26P0XSQzACrGVhf9RrddZytco5w5F64Ldg-qy4t4VKQvMvNzouDq51Q9meH88pNuwV2G5rYhTu8CH8OMPOCAnjDzBRzTJ6Qrtvc6J3UaQA98piHnw4lQEPRvf0UDN0guUVDEtU_3qrdMjs0Nf2WBXTQvnrhvsqkqwmLNzLY2Hj4QbG8My_BCMecQUWZfiYZmnRUtdXNeRDiyFs7SNKASV6BH-7yMdWi5d9luZ2XIjnzAuMxwfvOF7LVqkff8T_mTBwzJ_ddDxLQVx8Nu0ES2p4N8aCWz7a3EM-fedULeTRlF6VV21iWUCAzT8jWSmbymv4AHtwsa4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=i08sl5753WMY-26P0XSQzACrGVhf9RrddZytco5w5F64Ldg-qy4t4VKQvMvNzouDq51Q9meH88pNuwV2G5rYhTu8CH8OMPOCAnjDzBRzTJ6Qrtvc6J3UaQA98piHnw4lQEPRvf0UDN0guUVDEtU_3qrdMjs0Nf2WBXTQvnrhvsqkqwmLNzLY2Hj4QbG8My_BCMecQUWZfiYZmnRUtdXNeRDiyFs7SNKASV6BH-7yMdWi5d9luZ2XIjnzAuMxwfvOF7LVqkff8T_mTBwzJ_ddDxLQVx8Nu0ES2p4N8aCWz7a3EM-fedULeTRlF6VV21iWUCAzT8jWSmbymv4AHtwsa4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VREn92xsrLhX6iVV_19FvXi_M8LPzP3ohcFuLdNZBKpbRXC6fHggdpzbfHaoKbK6aFBBXCGCb6jmMzKCj4GwQ2CPrsoT2YUg3ln7xkH9zemRf03tKBHqcCRNzjir17bRwwmfmHGxIaJXmbib6yLixsq6k6lQHJU4IYofUj2rpNLQ58qE58HDcS-E6CzDFfG3BdB0spXQNbaBDX2RlSo6SKO4dRxIboJwBE0_HpiloCpMryrvhLAUvR6X1xavEFkm5sYXxi7CEH9xybrpdVUbOSOVMJ8GlwuJCL9OKOPLKiQ8cb_H8SLDHY-t7XmgGYMkFLgDMn89BBm5GU6725uc3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z5PmgW_yDCS8sXa0Y3uYTcH_R6SIpyoYosWs30RnXa3XO-9F0qfD6aHvEikCUb2IeO9ehIGUIKZEl48mtraLsgjcyAuljUfQyMOd7n607R8K7DM-wKuLhZRA42_omgnhZ1F0MU6zak6G0rg-VeAW4Bmxto1A5BtInZpTXmZAEv8XRMXpJmPvtfgprqnAJBwDc1IJW1I2m63x2BXR3A1z8RkdqYntv3v-ui8_3tCFHskF7Aaq58Gf4zUY9jZ3j_qhcPHdWZrzbTXftlDTOnrkdJmlL1lgeYr3iG36_fSsoK5i4jmWJrapyp2TPhcbmdGdIEndaCa_q28cFQytT9cJsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq8Y_5vNVL7-0eMapzD0_GUX09mCckiBHQeEOVSMPOpCulLtfN_hd6grFhHYppkZNoEMphXngOS8FBHKQivHFj7P_Nvu5-VzpqzsaXRlw3pXLJAJX4XXwsVOtK-9c4xAgzizwK9NRjZOFUQQB3tdFRaWZR730c7CS8pIi1vcDMbJNDnptF-HV8zuzmXLcusY2VwUeYi7nm52fS2iCVJ-a7ykSDko7n9-jIUr99XZW_xUVC06hHlHFqr0qGP_mDoT2VoqRvsKMP00YmEXkx6ejQDuGP_q5MEEIgD984f1BputkdCjEIro9NeZsIb1gD5xWJQf9hZHkmopIrXTENR-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owAQpz6XCZ4T4qtFDzvOrn4h-2u2PyF45RsMS2Hu0DBt0d9aWHowkhaJ5cv7i1kbzdsa7Nv1-vN3BctmQ5JFA2X4f8HhAhBbcoZ8ZtfLNHQcJp5K2bMfSGBn0T6WmI15SRz7PpjlrlxIM_PhhC2sKSx7jtNew_Mx6UIcvVzBMMoh3wvcd3N0BAnvr5xzo0LfWI9o0FXGC9qMY0jjoLuCE2wGZDvYlEWryRLUCM94zutY7_3dRTTKjYthy4IQQLBEXlnU775gX-9UzZk2qB84lILIJ6N-_FbuTbm1I13_dDdqN7aXY0WVi6B9w4YQjtw-asPxXv-w2lxZy_2jkX1M3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnBvQXyfzjetrv06BZMT80tuSXEC49_UuhBE9Rp5rkGgLdlatkDTH7IRoUT5_tg1M5xeO8gTAX-JTU6eaWBshoB_3tscqUDN4oOibR5nSATm2NOf1Q00El9WFW1cdOkAPHEAJu7LJq69hNFTDAD-8ChfwQ6hNP-d7bBhIIlYWZKv9Ll0s3WvHG5p7ZwhmcRs78PG-ghLU9n4dGtx3wHSqq1Jo-K9cF4x5ky2l4aVptrLj9tfYH4jcicK1Tz49HCRpyoBhAciBBpmtKDdvRnVjVqoBXdjw1OS1USilCH5U83j3A8o5yjScxexOYdHMkCZEP91qzRotX2guxiwhGeBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=ZsvagEdpPoHzx_HoZap59pJ5B5zybH37XFf6xkzxZCx2QXj9bNt3L5MU50-uzlPG4iMfozqM5tfLcLuRgFhWL4nuWvzDFdeTKdWvRePdX859YTbIz6clG0qauFYlF5XXo51zzDWYBbvOtBP6l6pMaMFnMhMXA1JdVBu-D5jerISoaUiabyD_5BQqNtmabSS5Ld8uZH0pRaPzLaEG5pW-NACME8LnRIE_9h4xpU7FKY9p3eRrhrjhWQzQg9DllyWwSaPgqXQihZRyTAccrrewpU32PIXm_-QSIWBMvyKAaJI0bql8Oyum2L3BRsxlS30ROR49b6C4UVf2AwihklXHWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=ZsvagEdpPoHzx_HoZap59pJ5B5zybH37XFf6xkzxZCx2QXj9bNt3L5MU50-uzlPG4iMfozqM5tfLcLuRgFhWL4nuWvzDFdeTKdWvRePdX859YTbIz6clG0qauFYlF5XXo51zzDWYBbvOtBP6l6pMaMFnMhMXA1JdVBu-D5jerISoaUiabyD_5BQqNtmabSS5Ld8uZH0pRaPzLaEG5pW-NACME8LnRIE_9h4xpU7FKY9p3eRrhrjhWQzQg9DllyWwSaPgqXQihZRyTAccrrewpU32PIXm_-QSIWBMvyKAaJI0bql8Oyum2L3BRsxlS30ROR49b6C4UVf2AwihklXHWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNFQkFJQ8hIvmNPrJKo_AtMn_-AscZV24vvHi6mo7-apekGLrX-VUB2kLtrANfz1zGpRb_oo4KXaL_J3zb-ZiFUIxE7QN1kwn_FmQABig2ofl8Ac7RAG30xSnLaQeHNBGH7RGpmZk-mpOSgaVv_mogidZ1-Lo13CVBH9HwoW2RUzB7GQqIDIPiqlOFyT89ejRr81gzr4Ygdcs6uXOVCInOm8xGp4aBWeEEyFKQETUCeZez8s24ouRiOtVcHVJKmPHyZ_P4CG_23YU2X_54Cvh-_qHlqFvGBoTmRH0MPoVfe1MpQEwmtrlUFwdXNajKrjqvL8hTChDSP5jjEt3XyjGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANEVIIm6DwyqPBdlXZB3hBRNG4Rq4CAp9afTDyrWL3Lk_8ZNyWXAwI9hCGsfgS6CxIvjH3WhF_T14A5Okbq6IsnaVz8CXx0DT-Si5fbGuQ1IoVuvgvzTYREGbRv_BRDs1XNCUNnBWerQeu6altM-Hyh_3kkGopGd08cWRzUw7LtHkCSDvDApH8CFYcl2B6bF411gs4cXjGsgl3vh5CzTcuP7-8N7HWF60dHAwEbM_8Q4GJHfkRg5xXdGbP8EdI7VTdOABcevjFUvE81DxCHZbPkrHk0gQiflVqcz1RZeXeEGbfKWAy4yuZrf_Ru0yznFhePu-f_eP3c5nT80T7N6-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FupUwn_7_5Yq9uSXS966iRKhwJxzILQ8uOlLvZ1BZjiNTyurbkO6NhbRiRdlSCnQXPin-Uz3KQS3s-uWVPhwPCXajwkU3J_mjMxGaKHoFCgAeYWQIwXvJ-koDnBF11j0SIcD3XnEPF2JJCi93V_YS7xqI9Qs1HeMyAIuv6WPd-JaB7t3-Qc3PG0Z3Fr7zBlfb3vch5ho7srj_F9wwMVZFYpNx36u31S7ycl59GbmtUXm-sUCt4aCARsyL8Zm7m8DymKZL2UgWGXsq2evjOgHaMpp2m_aw5y4R3NGzCHNvKqRdadS1eeA4QmzNom5UITSuuxcW98H5I6cYaIq9zOTaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «تمامیت ارضی لبنان عزیز» !
«بساط جنگ افروزی اسرائیل
را برهم خواهیم زد!»
جمهوری اسلامی به خاطر حزب الله لبنان
دوباره میخواد وارد جنگ بشه!
آتش بس به دست آمده میان دولت لبنان
‌ اسرائیل رو رد کردند، به جنگ ادامه دادن
الان هم توافق نامه پایان جنگ با آمریکا رو کنار گذاشتن و میخوان برای حزب‌الله
وارد جنگ با اسرائیل بشن.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvWZn2bberCOXbDKURcFddGgeBsQxpx9395uy3ZIJ9jyyNiesUGRjkaNdmoJyezQ1hMf2mAzYxkX8ApL7XZcyYucpUmHDWI22nxN8FolaGrh-q7lUT8tqWyHlUd3PIJmymaU33MpdFXvaHvwKwElFTIhRr-T-1F0m5C7ttNAvMzP_myur-cup88-QB25k8q8BIbnQ2U6SRw-C0DnrH_m8yzdWLHqSoUBM7eyhgYbVnzt8VPlzTViq4_0HABw27XDWmG1mFmZGR0uBd0ct2njS1DPHI-B5thdfR-p3_wiJCdnvQer4M9XpidcLdkxuhgjwR583a8AdyW7JNeKNQPPhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PvOlvG7WQswVvJYNPJyhcQeHHFO8RJtqxSZ_kn3mNM3htfaXDxlKEnN0X6YSQUy3P-Al2EaODORRPJKpXbzMbz4EER8mS6d08pA5EUQUbcuqTsyjrbaYhuXMapeu64cbv6urpE7Se0yJ5kwMv7ilEZcFxz_amM-JDj_-FbqbqxHC2FsHA4JUgQtm9nenhL-CLeTgaemoHhTLuY18MvQ0EWEkUv2uLiElLTT8kvH8Eh3W2n4VRtbTkJJ_O6QRSxv4OfcTV1NRSeMXgUyDCaHlDo5U_G3JNr10zSXyx1OUHQ82cAAeiYIxmKc1iOSleUcUj2AF0T5ptLzwdVjgoNAU0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lWn63t1WK62MxGhc0xtHaiymrzIi0fI84nHy1bLj64U4pQxIk-PsMn8oRBbr-FymZ7PPxBEkiRiwLjcltdg7dW4MP9dJeNn7Q1jy5kdUguezVuTAYSJTJYqFDZ9BvIWCB4c1dzww7eC5Psef_aKNBCkdVTd7es7nR1Z6NHdXfGil_zDx04tSKs0WkA1Xab5yU1djSF0V0P8KtSr_f4wr475-mRwlF5g7wa-PayDXSPOblLFV-tQwv2Sfc5ZJB_XTlWLkXwbXcUmfJGZ_eO_AO3aee7bMj8we_CoS9KhbuaJ7_msod1IP7maBNf_GKJ8jk-WH_sIJjfZIYZ4m5dHtBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزادار کودکان مینابه
عزادارن حکومتی!
میگه حکومت همونطور که در ۱۸ و ۱۹ دیماه «به حساب» مردم معترض رسید و دست به قتل عام زد،
باید دست به قتل عام معترضین توافق هم بزنه.
اینها هیچ وقت ایران رو دوست نداشتن
هیچ وقت ایران و مردم ایران و‌ کودکانش براشون مهم نبوده
اینها عاشقان جمهوری اسلامی هستن!
اگه برای کودکان میناب هم عزداری میکنن، چون میخوان یک کردیت به جمهوری اسلامی و سیاست‌هاش بدن.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXKw4Edj7ImdD7nIuHCMVUIY8tBg8ZqV5HWI1_ig7bBBz32jRzE-rI2JZ0AQ8QIVyphUg6nMgauRXmHRNg_so3s92uW6oMzpFqYk5Qp3s_H2RaCFFY25SA6jL--iGIQrS_iJ64nnyEJ9f7YkkWDt1C0aqYzv2o3UYobK2dvklIrQ6rp50n2_jaOFbLeJyqUApWTwyUFtxmAWWnXhLPnlKb6ccGLt3PROeJWaQdxZDCMsVAOsFYEIR8RGtSINCSmUHag_KTn-kqXEU9aYq-ETNMxo7sTESw92BCRXnRouZ94p3bZmMMt_yfGTPskfPLqaVL-PnpjMyLUgYSreIEi3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل خبر از حذف
«علی موسی دقوق» از فرماندهان ارشد گروه تروریستی حزب الله لبنان داد.
علی موسی دقوق ، بعد از سقوط صدام حسین، توسط جمهوری اسلامی ماموریت یافت تا به عراق برود و به ایجاد گروه‌های شبه نظامی شیعه عراقی دست بزند.
او از ایجاد کنندگان گروه شبه نظامی شیعی «عصائب اهل حق» در عراق بود و در کشتن ۵ سرباز آمریکایی در کربلا دست داشت.
اسرائیل امروز با حذف او،  پیامی چند جانبه و جداگانه برای حزب الله لبنان،
جمهوری اسلامی و البته آمریکا فرستاد!
فرمانده‌ای را حذف کرد که نقشی کلیدی برای جمهوری اسلامی و حزب الله داشت و آمریکا نیز از حذف او، نمی‌تواند خوشحال نباشد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU4rrhkDvYM3vbjtuOaVHmz88hm4ow8UNRqEi6T1Ub_PzthrkBFMtIQctz1K_AMlSaVJoNU-nwdYjgT--l29_Molog_Sjipf2AqJRBn5mjYlWy6HAcH3SqdbhhBFtWo6nysvw09jrUY3es6-nQx88_0PadwQOoswQGW-xFxW5KQsXXthm6nTWstWzSHrBAcVwgb1fiPZEwyhCNT2DgcGGSpIwzi3syMve5oIAzTUIj0L984fnGzqI4t7EVGe_7LfJkOOravg85ZLxs2_uzPF17OGFtmvgDh9ZYeNHH5lzUdfnTIiD4WMhlQj5XQbRDqdwqvw9wb5jpZrGojRmrfPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=TFaEZsGeNz5wLKlUWMAHltKxwCvJYsx9B6k-CSHMt61JpcwcCaeANtPx5-Z3BW4ZqAQFRgHaNq9PyM3RG8iB0sAXec039ct2TtlcchBfFkHInypGyp5JJC1NK-3gL0Uiu__zLaBOp-FREHOERA6UkQotnUsOr9Ap5tbzipbZi8ehhFMSLA7KczLb3CHJVgHVd4K1YAxl9Bd1YTASDysuW9PUgwv1QaBAIsnoNKykTmsv7ruMPcStbClLZysDdToK-ghT0wUDh8l1OVL3hV2AOSh0Tqxyy5qUvlWtRwmLYaySt1-ndVHKdLjmLL2fGPiDPV-sdNbOYZ0hYXfLIWInDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=TFaEZsGeNz5wLKlUWMAHltKxwCvJYsx9B6k-CSHMt61JpcwcCaeANtPx5-Z3BW4ZqAQFRgHaNq9PyM3RG8iB0sAXec039ct2TtlcchBfFkHInypGyp5JJC1NK-3gL0Uiu__zLaBOp-FREHOERA6UkQotnUsOr9Ap5tbzipbZi8ehhFMSLA7KczLb3CHJVgHVd4K1YAxl9Bd1YTASDysuW9PUgwv1QaBAIsnoNKykTmsv7ruMPcStbClLZysDdToK-ghT0wUDh8l1OVL3hV2AOSh0Tqxyy5qUvlWtRwmLYaySt1-ndVHKdLjmLL2fGPiDPV-sdNbOYZ0hYXfLIWInDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=eXr8a0Bc2Hua9qo2SPOo0BrIHxKRJr0jHB8fH32axAlbqQIjiirgFeWGmcKOy6fBAetJxJ1N0AoVyhp0UBZoZkQT7WqsbJ5dbVVeSYM_tPhorsvJ8JCi735EWyYJiN5j3FWVNXFbAn6GawAfs4IbG7qUoUDDnRLuasiv1Ah_8r_iRqBmOljCFAZsykETj2tni6coHdcVoL4mJkMfTg7mExJYzQKZr0gpb4V3NzYVhyv_a0FUyWbj0PXTLvzYc_3USEDK37y16ffs6DDH1QYEyGxu6WVvmn4EEZDQkjQsk5a_4U5oAF_XcWqI0jb4X5G65fBp-JCaJ_jT5ZCLTs0L2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=eXr8a0Bc2Hua9qo2SPOo0BrIHxKRJr0jHB8fH32axAlbqQIjiirgFeWGmcKOy6fBAetJxJ1N0AoVyhp0UBZoZkQT7WqsbJ5dbVVeSYM_tPhorsvJ8JCi735EWyYJiN5j3FWVNXFbAn6GawAfs4IbG7qUoUDDnRLuasiv1Ah_8r_iRqBmOljCFAZsykETj2tni6coHdcVoL4mJkMfTg7mExJYzQKZr0gpb4V3NzYVhyv_a0FUyWbj0PXTLvzYc_3USEDK37y16ffs6DDH1QYEyGxu6WVvmn4EEZDQkjQsk5a_4U5oAF_XcWqI0jb4X5G65fBp-JCaJ_jT5ZCLTs0L2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=c98RsJmmVMS8UkGeWgBIf5F--1Cr288_VnF5FskFEP9PnqtFUZuCF7BD8uC8_KLqO8XYVUx9qvdY-m-g5jnEs9R73ZcSPah0o2KjLxK4cBlB_eehIPb_JgGhwvlSRPzEAFAFsxqeOqfZrXGz29I6nskzWYABNSkDLjLBKLhtQaYpqw14gAmlJFFscxrQkyQXCJlRNJ-cMwZ6oAdZA3Exu8GMN6JemEPCsvjtj-UpzDdZBEBQiwDfRLA1aTgXBXe5OV1nzsoxzdF_84XPdDB9Ow3HA7-7Ar-vEeDhSgo_WbX17TbMVOU4yGJT8T54ek9EoZRnAnC5kxSH6W7hpPd0iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=c98RsJmmVMS8UkGeWgBIf5F--1Cr288_VnF5FskFEP9PnqtFUZuCF7BD8uC8_KLqO8XYVUx9qvdY-m-g5jnEs9R73ZcSPah0o2KjLxK4cBlB_eehIPb_JgGhwvlSRPzEAFAFsxqeOqfZrXGz29I6nskzWYABNSkDLjLBKLhtQaYpqw14gAmlJFFscxrQkyQXCJlRNJ-cMwZ6oAdZA3Exu8GMN6JemEPCsvjtj-UpzDdZBEBQiwDfRLA1aTgXBXe5OV1nzsoxzdF_84XPdDB9Ow3HA7-7Ar-vEeDhSgo_WbX17TbMVOU4yGJT8T54ek9EoZRnAnC5kxSH6W7hpPd0iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=C15DY6J0Ux9XOSPhmkaE-ht_JxYZA7hM8TapDXFwgbUFPCnHvlFCqwz5pk9bPrMbmKvSSQ8cEx08WDvYQdNP7gKAgxyPYc0O5axuYrE0Z_AvvyG6p9D6ZDCevruvQ74lnMRPDQLYYE6HysnoIat59oJCKAtF6uydUPCIEHI80FeutS8EJ13YvlIgsgcpn4c2qER3OoiyCqop5ja3E_czZj_K0fHY6kgl2tCIdC4v749sAfQ7B1bzEEe24BNwXHPy_xpOV4gqw075u8da3H8AtM0IOCaZcYZENA4RPnHIGRzgU6DrjaUUBMnm1pysgh67i6HvKTMie77rbq2fdjA-QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=C15DY6J0Ux9XOSPhmkaE-ht_JxYZA7hM8TapDXFwgbUFPCnHvlFCqwz5pk9bPrMbmKvSSQ8cEx08WDvYQdNP7gKAgxyPYc0O5axuYrE0Z_AvvyG6p9D6ZDCevruvQ74lnMRPDQLYYE6HysnoIat59oJCKAtF6uydUPCIEHI80FeutS8EJ13YvlIgsgcpn4c2qER3OoiyCqop5ja3E_czZj_K0fHY6kgl2tCIdC4v749sAfQ7B1bzEEe24BNwXHPy_xpOV4gqw075u8da3H8AtM0IOCaZcYZENA4RPnHIGRzgU6DrjaUUBMnm1pysgh67i6HvKTMie77rbq2fdjA-QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=uzuvERNkw3NnDevM7QA0GdXCPd2RisCfheC2TyPIZajcwPJT1aUuT2opR37dvAWgRtkRnp9XdjWMqRDitpci6ydFLDeOr8zseHGmb-MVQijDuvMkqeBJaXKCcBLTabWHH9J9JqBRLvtG8AYcyW8RjK33dprc5SwY21cY2TKyosWWk1xZDPD0DA8-7t76ocumeSpM9oUhaPOWm2KNslQU4wBODTVimMLGSnDo_CElPtauiFIgoRZ5tnWk6HgFdxyhqz7YXDQVWKou2k-nFJ9pGwALqs4FIAhx1BeeW-88o8r7oosGt2KIISkz3ZEnxiWy9N9NZBhy2v8zKwkzTDC1Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=uzuvERNkw3NnDevM7QA0GdXCPd2RisCfheC2TyPIZajcwPJT1aUuT2opR37dvAWgRtkRnp9XdjWMqRDitpci6ydFLDeOr8zseHGmb-MVQijDuvMkqeBJaXKCcBLTabWHH9J9JqBRLvtG8AYcyW8RjK33dprc5SwY21cY2TKyosWWk1xZDPD0DA8-7t76ocumeSpM9oUhaPOWm2KNslQU4wBODTVimMLGSnDo_CElPtauiFIgoRZ5tnWk6HgFdxyhqz7YXDQVWKou2k-nFJ9pGwALqs4FIAhx1BeeW-88o8r7oosGt2KIISkz3ZEnxiWy9N9NZBhy2v8zKwkzTDC1Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=IgFXcdl8Ozx7mubd0sSB__mW6_NLo_JEPx0FLRmod5xyRY0bI7CCiJM_vaCdzIZcXXmOvcqyA3Bhe_ioKzObTgK1DGOkcaKTohflySUUesPaSh6PbFD49-8F7dqZuQURCwsfjyEK37q5CHuUmASdi-vF_Zyp4XLaVF3e6iOm7R5pW3ADb39cRgy5XjD8aHUCxd7gNXPs1JzXd_K2R24UNGm23aXP6SxvXFZjhwj9lq9GCo3nEUO0tnGKt7b_iluTtAb1VGuaFtEtjrPbr_3-ruxynyBErOoMCim0Xlc80dINxchR13Qn-6BZEKDOWvLheRz06uqFtEAnCouZAwnfMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=IgFXcdl8Ozx7mubd0sSB__mW6_NLo_JEPx0FLRmod5xyRY0bI7CCiJM_vaCdzIZcXXmOvcqyA3Bhe_ioKzObTgK1DGOkcaKTohflySUUesPaSh6PbFD49-8F7dqZuQURCwsfjyEK37q5CHuUmASdi-vF_Zyp4XLaVF3e6iOm7R5pW3ADb39cRgy5XjD8aHUCxd7gNXPs1JzXd_K2R24UNGm23aXP6SxvXFZjhwj9lq9GCo3nEUO0tnGKt7b_iluTtAb1VGuaFtEtjrPbr_3-ruxynyBErOoMCim0Xlc80dINxchR13Qn-6BZEKDOWvLheRz06uqFtEAnCouZAwnfMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO952Fn6y6nypr-mfdUsKtDVw5THAP7dYlUJBG5Hv-nHjgdMG0bn76HyxYb_WhSRBfW5FkmddAgICITXBgvUojzubdElh-vNQqd6do5LqUXLroNaUA4uaTMg4XAfPA2Q1rFPW3Kh2C71tl1eestzYZ62S-vKHaCRkC5YVzADa7M_6Tq7jaJ_raS5Wm5dYTK1YJAZshcRa6EUDMcqBU4Fa2rVj2U-w-eSUJ9MnRzM5LU51nHi0Kf1cVN8eURrkgwYQ5Y1rQJjZnX7sXuyYrbzKEpKhx_h1tTfskgm8_172-cgKB7ikI9TFTY1icZ0otCHpL2PDHH5uToG2zNxqdZpKOLHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO952Fn6y6nypr-mfdUsKtDVw5THAP7dYlUJBG5Hv-nHjgdMG0bn76HyxYb_WhSRBfW5FkmddAgICITXBgvUojzubdElh-vNQqd6do5LqUXLroNaUA4uaTMg4XAfPA2Q1rFPW3Kh2C71tl1eestzYZ62S-vKHaCRkC5YVzADa7M_6Tq7jaJ_raS5Wm5dYTK1YJAZshcRa6EUDMcqBU4Fa2rVj2U-w-eSUJ9MnRzM5LU51nHi0Kf1cVN8eURrkgwYQ5Y1rQJjZnX7sXuyYrbzKEpKhx_h1tTfskgm8_172-cgKB7ikI9TFTY1icZ0otCHpL2PDHH5uToG2zNxqdZpKOLHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txSixXTU6o_gTgq7dsl3HGcIPDGs3CFwfpCBBh1IgviX6zctaa7u1JLAr6P1HIjaBhk3Sc7-dczyuRM6e2clmDraBjhR2RQ8DhznOdc1bnV10fOvkfMn3mepz0GWkGfRA2LfGgH3WnYkaAlRV_A_T3wsC_ou4AihBEQof9vyPvzINqYDl-fNNsOhyIZt-svC79WgB2jc5pyrjizxwiBqi8QjNgC3sbgdl374BUiIXbOAhTJSbzTpEWW6XG1dZFpx_bF9eZjcFh6wprqLLWwq3y4AWh_agS6UIxdaz2384LkEEHMZF6LG_ePJq69E4luU_O7gABZB3RG-psehrQ2l5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=Ls0MYd0XX_4--_w0Evh8MINUVAh7d06K7zyDmc1XPn3F8iD8N-2r_NSp19UgKbpIYhtsrQPO-Ww1JiuD0Lw_JdaVmtcwalzRxB4k2loNwXwEJpcYMXnb2QnbJvfuVK58EYK6IdkcwGmdrvIPpwuUE4CYuy0znJflLIVOvW0392KG0UH9amtUFI58IKa0UA9N3vONbcetr2iCY0rXQJfRR0sRzP0r7lQ6BxpbLTQJA5uUdnzrHURT18u04qHQBvO7tMfFtunfVvr4LGkS712unG4DITF2d2bMpUIkhEe9Uk1Y3ZCntMKuINuP_8gD68vlunoVCp4L9apG59iYifgprQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=Ls0MYd0XX_4--_w0Evh8MINUVAh7d06K7zyDmc1XPn3F8iD8N-2r_NSp19UgKbpIYhtsrQPO-Ww1JiuD0Lw_JdaVmtcwalzRxB4k2loNwXwEJpcYMXnb2QnbJvfuVK58EYK6IdkcwGmdrvIPpwuUE4CYuy0znJflLIVOvW0392KG0UH9amtUFI58IKa0UA9N3vONbcetr2iCY0rXQJfRR0sRzP0r7lQ6BxpbLTQJA5uUdnzrHURT18u04qHQBvO7tMfFtunfVvr4LGkS712unG4DITF2d2bMpUIkhEe9Uk1Y3ZCntMKuINuP_8gD68vlunoVCp4L9apG59iYifgprQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVyTU0cehKm4lTQVzaMlxzU-89hfV3pc5OtAVH6JOqLFKKIa4_PjQlk1gzHdAFT9cnBPjyC37eP9ETY8Hv6f21ex-4vlahgHSQ77XsYmgTs7DIGU0VPaYicxZ6uZdWJ3uUugdgIdElOVkSkooVqvmTb3l1dlaxSkgSlj_KJjhnnVdPdNbHdSBgkCLddoh1SJTHlXwPeADQ2Sypajox6VTgLB96jOZHjCXHhTdI9IDdJpq7srU0pbFtmOOIMP5gaHG437iaYo0pSa4fG_eac8Z2zEL6nuPkqEk-TYkM9eYfEMG6SzmmlDydNyYaejwLhchVrfzHY11rUxtvp9ZhsBsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اکنون:
توافق فردا امضا میشه،
هیچ پولی بهشون نمیدیم.
دیگه به سمت سلاح هسته‌ای نخواهند رفت.
تنگه بلافاصله باز میشه.
بعدا هم اورانیوم غنی‌سازی شده رو از زیر آوار
و خاک بیرون میکشیم و نابودشون میکنیم</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYbpvnqkLFaiVx1U3A_pmdsJjHejDDl53r3Z4IhXyBUebnYleL5npMD9O2Bf9orPj1ec7Aj4lLOkJ44SE0Eq5oJcVpQV40Jv7VLvVStfUiIi7xE6ArGVGS2cvrDumoi_1doH-ynPJn_471L9Gw2ANtCvJ1ZHlbAJbDFg9Gp6N9nQu9epkaeeLDzqSlkMICV3m05-6IpfoMx0n5Hdx-RS6kJfr0I40J9KKWHmcK3K4vT-O0v-GIjxjl5pKiilofBEomJK3P31RJFXbOlCzEAzGj-Ld1-UJvJhDIRug4zkwzgBSaDQ9sm9V-qjKkW5yB87rwvzy7nF_uTzVkKrxaGeBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLSMuAcoYRNz27fxcSWUH7ismwNtwpAnqz1d_brFWdECpkV1mlVVAfYxFZ4Adyp7xggK7OlYAwLmIrJj4ZMHOup4AtIT6MxigAts7csnoFqSiwluDzJY-rnIprhwqm5XHqAmtNv7GH1bS3wGWf8cVp8mVcdLekXO13DiqvkzuWgG5q4aGhqQS9KBIWVmcEbFv2kup2T-X7A4kfwzhOz9Fk9rWGdTxmFwG6wxwBdtm65E87tQx_77Fu3UFyANYafDCWbRIENEDC_Lv-uGHV7_p1UUjmjcfoFAfEvlKT-7Ve7X3zjscaQ-B-gtjqOtGmmE1L38nS2dx8F68pSYeo1MDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی  وزیر امور خارجه لبنان:
«حزب‌الله یک نهاد نظامی غیرقانونی
و بازوی مسلح جمهوری اسلامی
برای بی‌ثباتی منطقه است. اقدامات حزب‌الله، لبنان را وارد جنگ‌هایی کرده
که هیچ ربطی به لبنان ندارد.
ما فقط میخواهیم در یک کشور عادی زندگی کنیم! نه اینکه همیشه در جنگ باشیم.
مردم ایران گروگان نظامی
تمامیت‌خواه هستند.»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5530" target="_blank">📅 19:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=uixt6cfPXXpVsbvwexWLTytSZE2LJZxnTTC3iRau6zskPaVNeGypN277UXSYohz13fMmuFThQWNtaEYtomVkScLXSAE_BxMNl61a5Hb9uw5tP7loVgHIVGk5ohSciJ6OHRfMt67qdNn45QaosQLGQmwgeqQ2CZzswO-WSyOhJgjbWC90L7k2g4U0yzL3Fn8_HWa-X0G3P9L_d8vUN24IvgaS4zGH84uGRhCNBWBdUj5Z51TVXtXLDpdxokI3Zzc6fguFuauO7pWGFLdDYc7q9zuu9Vro7GeIqN29ktPs0qlxraNg6hXjdZ1bRk4AaQDs67vjixsginSzR1_6VQ2kzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=uixt6cfPXXpVsbvwexWLTytSZE2LJZxnTTC3iRau6zskPaVNeGypN277UXSYohz13fMmuFThQWNtaEYtomVkScLXSAE_BxMNl61a5Hb9uw5tP7loVgHIVGk5ohSciJ6OHRfMt67qdNn45QaosQLGQmwgeqQ2CZzswO-WSyOhJgjbWC90L7k2g4U0yzL3Fn8_HWa-X0G3P9L_d8vUN24IvgaS4zGH84uGRhCNBWBdUj5Z51TVXtXLDpdxokI3Zzc6fguFuauO7pWGFLdDYc7q9zuu9Vro7GeIqN29ktPs0qlxraNg6hXjdZ1bRk4AaQDs67vjixsginSzR1_6VQ2kzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTaU0G_I8Rdm4ayG5MuuLt5gRkZ301Xj6XDjna0aSc6e_WhLroB3hi4c-zt1LG6I6A8Lsd63gzuiiEi3lbaLlY81MCqkt4ZE0KRtWPYDdsiBVPOj33j-huliSru39UEtaeHcoQ0QiKdUf184mAgMpy6yT-O2xzJTbhTE6qQjKWQU_qAqzPsksxd432iBFEd6KybwuPCOR2gOIysDCXQU-vr51nttykeHr2qPy2DqicuPfc5A16bBUKFibZ1i5T-BSQLEBvCIqZqJ_QPH9mS_TmL7UnBwL2TaR1kirC7pGaxUhGUadSlEy3YS2Umj5j6mC6V-fvaJZzgZvOcPLmyCrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9W-_oMw6ZgKxdl_qW2KrkMi164pxhix5mh9QrmXzh8Tk7HLwoUSAbCv_YG9Z1jSk2pJ-3gWzTSJXsqm6tqbLKJhBcm-7ZOXnOszR0kbqg07vpw_DQNvk4_inyuFVhnk8u1WAXvxL-QCxKIkGJ9Fr9qNgjIYJh81VcfgI40kNRLO9zkQ3u0Of3o3UbZ7830RYM8Cfx83PWKbwrOyMnAGGF0g-vzCEjQaI4IVlP3OeqDsXHZAqvwhK0RlPrNpTrfISKNkUyk4WHategzEGGgAC17aHpZ0aBhwUbSpJRArvjeSCc_x_DuhORPGkUmfmh7uZoGZS3v3eyXOTIvhF4F9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNPVwMQQclne6Ort55LQ1RLSk6g0ZOS0monX_86c1wkyxY6bxZmuyNkHv5WS3_wmvGH6a8sJnLOlMZayJ2y-isBJqPrWZVJJRGaGGv1TnAnKSp8pZbN6OueG23dBmv3SOvz1Atjfvr4BQU_a_KWdBkSBd4gs7OpwlmWslSV5LHpagI1UdHY8A0vAMS2Ml6sjb6e-0wwB5ITIwAcMXriuzBnoXFfmabAzdanHiptrgQLqdABEXNNIvo15CjKeXTrJJ95sXvsLdE0kXT0PaRPpYh0MbG59RAMR5AbxZyXJJKgITZODdJjvN9cI6rI-gyxTGq5Mtl4l-SOuaawPaeW68A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtDaQbk8llfq_rfS7gcGhjVlbewSJcdu9AleKXiBw9XlPi1Bbszngmw32yRKVSvLnHSQB1933aWr6TR21wRn-wV5I2lDdjHHZtlFCLOtPSFqFSb_-HG7uuSwn_wgGXPQZt5vv6lwoaqH6W58BSV1lkRRkucIOwAhAh4OEqGWXAhz3ej-Uf3sPUBBFlFpepSbIe0veQqWR7qmBIDh3p7PL_4yl1V07_HQOrd2xnYrH2I11ShxT9e_aAvotVoLLJ3kOrs_YmwRVlcGsEZ6qvom0CBM5GJ6QzC238vKzniYmcQekMkMg4AzDveZUH6wIW_SiKD-kVWzVRu9aPZpoIvpog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=QMW4UZvy6ly8blYVOZPBpPPu0tYwRHjJqhoxPp7_z2MoGw_G3B-tIXnD1PlnAbCt6RfgEGywfDXvMgk7hUhKroopuxwRxxYmcGwnSZX-1aF38y1T7fnamNllFdq-sLd8vl7RUVDfxhGXDVg47aXa-oyWYIacxKok1sLMLdqeuvQbEAIEeNSWK2EvdFz-gWqkGtyGPkmZboeBwSlacPDImrMhK2F5FabaHgawGX3Knkhh4eSL_28sz6RWAT9LJkPD0v0qtTSTz1BMXsB_XDjha6hq1yKMI9x2oGWwjLhv0OTpj2-mCzg7twyya6AqSynC7rp0sqIOGtTqunptMfoCcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=QMW4UZvy6ly8blYVOZPBpPPu0tYwRHjJqhoxPp7_z2MoGw_G3B-tIXnD1PlnAbCt6RfgEGywfDXvMgk7hUhKroopuxwRxxYmcGwnSZX-1aF38y1T7fnamNllFdq-sLd8vl7RUVDfxhGXDVg47aXa-oyWYIacxKok1sLMLdqeuvQbEAIEeNSWK2EvdFz-gWqkGtyGPkmZboeBwSlacPDImrMhK2F5FabaHgawGX3Knkhh4eSL_28sz6RWAT9LJkPD0v0qtTSTz1BMXsB_XDjha6hq1yKMI9x2oGWwjLhv0OTpj2-mCzg7twyya6AqSynC7rp0sqIOGtTqunptMfoCcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز میگن دشمن جمهورى اسلامى
ايران اينترنشناله!
همين چند سال پيش تلگرام دشمن بود!
حتى «روح اللّٰه زم» رو به خاطر داشتن
«يك كانال تلگرامى» ١عدام كردند!
توی صدا و سیمای نکبت‌شون هم گفتند :«شاهرگ رسانه‌های بیگانه»! یک کانال تلگرامی!
قبل‌ترش وبلاگ! ستار بهشتی رو به خاطر نوشتن در یک وبلاگ کشتن!
قبلترش مشكل «روزنامه‌ها» بود!
چندین روزنامه نگار رو كشتن ، دهها روزنامه و نشريه رو بستن!
قبلترش مشكل راديو بود!! دهه ۶۰! امت حزب اللّٰه بیاد گزارش بده كى توى خونه اش راديوهاى وابسته به دشمن رو گوش ميده!
تاريخ جمهورى اسلامى همين نكبته!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zhm-n-zhue8f5hc0LzU_y2JNjAEVz7irB5hj59qi-e1Qh94xGExec93UXLUsMdrnraUJ56oSioZGXFh-VFjjFt5jRhnh_jK3Dej8V4ywBxLlEepxPiU25l4rNkqtSIgibg3CyNO8WGx0kZBQg5694bVxymZ2tdIof0bWuKe8v1kDzQI3uDDFV0Y4fE-fHm-1K2_9a7mNd_FoTcDcCdGZPQ36DniXsl8y5HSbVXHaXEWHMGbbfcSnZWtCPrtCF25Ttg7Wn9fDgG1mpiTIX9VQ2sFJefyt4pN8xfG4HU2QAv8ZYMpcw2vkAyObdvIBn0xtNPGu3nhAO_BfQUGM-OHLtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن ترامپ میخواد ۱۰ میلیارد ،
۲۰ میلیارد از سرمایه های بلوکه شده ایران
رو «آزاد» کنه،
و این رو همچون یک پیروزی دارند به حامیانشون القا میکنن،
جمهوری اسلامی بعضا سالانه
۱۰ میلیارد ، ۱۲ میلیارد دلار تخفیف
نفتی به چین میده! از سرمایه‌‌های مردم ایران!
اون بلوکه‌ شده‌ها توسط آمریکا یک روز،
دیروز و زود نقد میشن،
این چوب جراحی که شما به ایران زدید
هرگز برنمیگرده!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc5PSHoyEKqyspHIyCmwW729U7GedWrCtsaLYIDQ3Fc2Kh_ta_n4SvWmpP2aC1SN5TlzxiBSQAyQG11rDcEafnUAN7xy51XDMr3dFhczaJAFwTHNun3p5T9oPODREqQ_b3WKnPCnQZkD4sKA5YoVw8zWP_57hoP9SLjWMMWljmvSchjQC2BTIHBXrBVT7oiiFJmG9_pN4IN4MwnVDQNORJAbnm711TLFDlhjuhAWXFN0h4lmhzacwcPYxyVmwKyevgHgok8ScspnhCVhuFsxBiUT3jc6sTF_eDFflsiP5OQv-HequqJYML7DBgt1zQw6bp0dde48UIIDR7t6nnnJZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=a8O-V4j8Ezrx7lDHLRQRcXH2aeQvNORvm38qP5ICpj-iYIQT45P4gD9_xFcesNc7ONBOuA2nTWtDWmZRAV3JYJOvxoEvZ2xuP_gBLzf7pliXbpysiy6YznTU6ePsZLSNGDKOHAOL5VfjcyBWlXfB84GXMrPrDQh6T3-HLd3G0FwEwKQdghs0AZf2m8AstdZsCFbpseTZiKAQ3qb5AF8YCPME5oWJ8vKObYzfBqOsjKaYiGChtJMCde-zaCzD5ywFdTukDMxNL7RgnzeKYDMbPqpd3DsfvteFl2pdBRp453gdKLw9DboQ-4fBXJvGRe9s80ZIxSuGHe9LvcNTcl-kHxNyj8CKHg-kpZppIU6xkkPJEBlmWrzRizFA_48yLSW5eqOy-1DjDgYZt688xdzLUR-IdiRJXA5EkAxRCQ_oHxJlxSCJyWnoP9fRTRycIhvMZVICoEXuDXY3yLFSnvRIZ1Bdo_RKU1cMPTAKVW-NK1Zjz60O_MOVrG3K_J4hQxZ6fcREJMKwr78v4EoFQXCMjsVv79PLeA9IdcQuvcGIKoTT4Km_Sw8SQpAWn2v7-WIsVcPJnZRAONCsJGDorgV6gcDxNWaCh2rSls_or-K9XD5zIa19_qNZrN662Yu9hqBHSwvPI7SOddIGEpiIyyFkgkLE1Hs73Fu1u2_Q9cOFpKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=a8O-V4j8Ezrx7lDHLRQRcXH2aeQvNORvm38qP5ICpj-iYIQT45P4gD9_xFcesNc7ONBOuA2nTWtDWmZRAV3JYJOvxoEvZ2xuP_gBLzf7pliXbpysiy6YznTU6ePsZLSNGDKOHAOL5VfjcyBWlXfB84GXMrPrDQh6T3-HLd3G0FwEwKQdghs0AZf2m8AstdZsCFbpseTZiKAQ3qb5AF8YCPME5oWJ8vKObYzfBqOsjKaYiGChtJMCde-zaCzD5ywFdTukDMxNL7RgnzeKYDMbPqpd3DsfvteFl2pdBRp453gdKLw9DboQ-4fBXJvGRe9s80ZIxSuGHe9LvcNTcl-kHxNyj8CKHg-kpZppIU6xkkPJEBlmWrzRizFA_48yLSW5eqOy-1DjDgYZt688xdzLUR-IdiRJXA5EkAxRCQ_oHxJlxSCJyWnoP9fRTRycIhvMZVICoEXuDXY3yLFSnvRIZ1Bdo_RKU1cMPTAKVW-NK1Zjz60O_MOVrG3K_J4hQxZ6fcREJMKwr78v4EoFQXCMjsVv79PLeA9IdcQuvcGIKoTT4Km_Sw8SQpAWn2v7-WIsVcPJnZRAONCsJGDorgV6gcDxNWaCh2rSls_or-K9XD5zIa19_qNZrN662Yu9hqBHSwvPI7SOddIGEpiIyyFkgkLE1Hs73Fu1u2_Q9cOFpKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=b4ZDSJRjQNSXR_1iVW8jnKnz7XpAbs3EE_Rspl_L2bvTEaN1PqhFWnyMkh6b8QaFYohSRhpZgFB9JOoJbp_VRAJIjJWR0V8PCjexv2yCVYi2yaKixGE26X83q5XMHa9BJN8QEPcXv1HKG-Gnkf1w9nmGoEoIbGNXLzR22ULl6unkp1txFyCJs2tG2Fu1G5kMv0BDnLI5uBfnhXjBrPyZlLFbaQt16SB2VJP1A09ECo9fKto7tQNMeAq3RjUjz1txS8t4e7wP-Hmt0zF-yKW66mSDjiOC8D0cODisYb1jlaAxv-WdVPXVW0DV6UVTM0nRxnmD3ana8DZug1E1VPTtdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=b4ZDSJRjQNSXR_1iVW8jnKnz7XpAbs3EE_Rspl_L2bvTEaN1PqhFWnyMkh6b8QaFYohSRhpZgFB9JOoJbp_VRAJIjJWR0V8PCjexv2yCVYi2yaKixGE26X83q5XMHa9BJN8QEPcXv1HKG-Gnkf1w9nmGoEoIbGNXLzR22ULl6unkp1txFyCJs2tG2Fu1G5kMv0BDnLI5uBfnhXjBrPyZlLFbaQt16SB2VJP1A09ECo9fKto7tQNMeAq3RjUjz1txS8t4e7wP-Hmt0zF-yKW66mSDjiOC8D0cODisYb1jlaAxv-WdVPXVW0DV6UVTM0nRxnmD3ana8DZug1E1VPTtdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fofggAAC97Xau24dWaBXgMyAPi3BliHwerPudQ4INWnqDDWaq9OAcUDxyPYxrt5RpVq7_W_eqBu7wSoBUQz6DiJhpBj73b0iGv_hjEOnemjnUOVksAu6m5i9vthJ9T_jJ9-dmamSZyWq-Sh6P7syAyJVgyEMb4cFRYgYFwCesev4D-mFSxc9_LdFblYShQv2kVvGSxfeNFufb8KJ3YAiPkAli3R89coXnA7r19497DTaRseXGkImuUZQpdDfDv4tLRVwqU0EpXCvSFA2yzcv94SXwP8uJk2wcNATIZWa2hYY3BFT3AAA2xuG6vmj4EbDm3VOYR3Oc-E7Q5Ho6C7I-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=g1D7PWkb9GxHzoNc6dXGNrO5Dj4QNfT7Yx1vZYd-Z3NLwN4D61UHw2_4y5TTizvdWuCKT7tXtmSwbU0krkMf_ZgqlK7JKxMmgjFOz4lHJsHMvGSvNFkHGAB3EJydzsA-8TA17ogLtgKQeLHlJZXkEAcTzjb2D3T7p_QEGh0VJaC1QJUFezs4emBsFrkNAzBUszKBP4wVQ5gbDEI0H5vAWM1h_KaVjhGBdwod5Gq51TeONPpx1XNEVW3rL9RcZq22Bj3iCcTuHWmzEXHABC2YC7GBx6KQJmgbg1ye1qQyulEP7OQK5ZUYXBFFRaef3P84-kH7okNE3FFoMbt2x1IVtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=g1D7PWkb9GxHzoNc6dXGNrO5Dj4QNfT7Yx1vZYd-Z3NLwN4D61UHw2_4y5TTizvdWuCKT7tXtmSwbU0krkMf_ZgqlK7JKxMmgjFOz4lHJsHMvGSvNFkHGAB3EJydzsA-8TA17ogLtgKQeLHlJZXkEAcTzjb2D3T7p_QEGh0VJaC1QJUFezs4emBsFrkNAzBUszKBP4wVQ5gbDEI0H5vAWM1h_KaVjhGBdwod5Gq51TeONPpx1XNEVW3rL9RcZq22Bj3iCcTuHWmzEXHABC2YC7GBx6KQJmgbg1ye1qQyulEP7OQK5ZUYXBFFRaef3P84-kH7okNE3FFoMbt2x1IVtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jB3k6YEx4TRRmXT7jpER7bdIPmdIkhU0ieFQlSiwam_vixPtoafYK9Y4C_aeBeEb6V53qRYGI6yXL9-z1HdsIx1v-s6oPoepO2eGzHIKPia9SyS1IXVC0c7hTjjq6psk9SysJLsK5raZ9b0C_0Tjobrectj1hsMfJkmKZb5JbFC3iUqNFCCVj52-Hul66bPuIez9kXWZeRl3NLMJm3J68Ld_pgrZfphy8S4-Ra1aUFd3ONAFH07N-X_eeU13DLWvjS0T6TmlbrXtFWxc7tYJUdFKuPpKTGjgk8W48Voygym9If02wcGFbA_KO9eO7C53Od2iZL3AE-9DY5mMM3ebRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حتی اگر همین امروز جمعه، جمهوری اسلامی و آمریکا به توافقی برسند و آن را در مکه امضا کنند، بازهم این توافق به شدت شکننده و عمر آن بسیار کوتاه خواهد بود.
آمریکا حتی در بدترین حالت، می‌تواند با یک «جمهوری اسلامی مسلح به سلاح هسته‌ای» کنار بیایید! آمریکا بیش از ۷۰ ساله که رقبایی داره مسلح به سلاح هسته‌ای.
روسیه، چین، کره‌شمالی همگی رقبای بعضا متخاصم آمریکا و غرب هستند و همگی سلاح هسته‌ای دارند!
۲۰ سالی که کره‌شمالی مجهز به سلاح هسته‌ای شده، نتونسته کوچکترین آسیبی به کره‌جنوبی و ژاپن و آمریکا وارد کنه، اما گوری  از انزوا و فقر که برای مردمش کنده بود، عمیق‌تر شد!
کوبا همسایه آمریکاست، ۷۰ ساله شعار ضد آمریکایی میده!  آمریکا اهمیتی نمیده!
مشکل اصلی جمهوری اسلامی، آمریکا و توافق با آمریکا نیست! مشکل اصلی جمهوری اسلامی داشتن سلاح هسته‌ای نیست! می‌توانست حتی، مثل همان راهی که پاکستان رفت، ج‌ا هم برود !
مشکل جمهوری اسلامی دشمنی ذاتی‌اش با اسرائیل است و تهدید موجودیت اسرائیل و مسلح کردن و پول‌پاشی به گروه‌های تروریستی است برای تداوم مبارزه و جنگ با اسرائیل!
آمریکا می‌تواند حتی با یک جمهوری اسلامیِ مسلح به سلاح هسته‌ای هم راه بیاید ، آمریکا عادت دارد!
اسرائیل اما قضیه‌اش فرق می‌کند!
پاکستان ‌و هند ۷۰ ساله در یک درگیری پر نفرت به سر می‌برند اما پاکستان هرگز شعار نداده که «هند را نابود می‌کنیم.»
تا ‌وقتی جمهوری اسلامی دشمنی و خصومت علیه اسرائیل را ادامه دهد، نمی‌توان به هیچ پیمان و توافقی خوش‌بین بود. خصوصا حالا بعد از ۷ اکتبر! بعد از ضربات مرگبار به حزب‌الله لبنان و بعد از  اینکه کار به رویارویی مستقیم ج‌ا و اسرائیل کشیده شد
و بعد از تجربه جنگ ۱۲ روزه که به اسرائیل گفت می‌تواند به تنهایی با ج‌ا وارد جنگ شود.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=lC-IaxPCjHiGMf_QyqPZLyTtq4wRhqUNUVkly8CYujF0789SS7K30pfGxmAx8qhaBGF7Opa9gLuJ1-CbUAM65fHuvYeyG1HK1jtzlF6ZAgVEMcXG1_o7a5zFjbpl3WZeDQ_l8L_rJx81HSB5uJd4vegLLFW9PQpW_R5GHVyFTI4oP9zrE9qV9TiBNPfdaPan27JqRa6KsuMosNjFLz8o1jvioWH3y_-R8lEjDRr7aVkO1E_frCcAGFAjQJb8BZB3TQVcNQP2oK0kj7cnRq56rrN7aW94TXpzez8zm8cezllUcSckFRlFc2xwBK9YdBkLUuuuBPEYTOtZWBXjeXzIcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=lC-IaxPCjHiGMf_QyqPZLyTtq4wRhqUNUVkly8CYujF0789SS7K30pfGxmAx8qhaBGF7Opa9gLuJ1-CbUAM65fHuvYeyG1HK1jtzlF6ZAgVEMcXG1_o7a5zFjbpl3WZeDQ_l8L_rJx81HSB5uJd4vegLLFW9PQpW_R5GHVyFTI4oP9zrE9qV9TiBNPfdaPan27JqRa6KsuMosNjFLz8o1jvioWH3y_-R8lEjDRr7aVkO1E_frCcAGFAjQJb8BZB3TQVcNQP2oK0kj7cnRq56rrN7aW94TXpzez8zm8cezllUcSckFRlFc2xwBK9YdBkLUuuuBPEYTOtZWBXjeXzIcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=X5E-3ryg41VytmJai6exPjr8ieEQOm7qc1iVM8jv6K_g0AxH9XJMT_VwwmACSzByDmxp8C8xQJAr4oIcQ26e8y4Ffqszp5cvDV8xlDcuEyIj9T-I1JYW-KURha87031RKVg5WG5tqWlApfH3ae0roO0wAdSE6Ki5oubSk2PkLQBnjIv7lg5r0CQJIrXuyFUdwlUbUttW13_tQkspfs7uIPFmOQdhEtFA8ZxJIxAWrSAIhRweGvj270bi1cgKZvk91EgRUk8MlMIqVnUbbkFm217xnWg6nTSrXCKlHLkFBmI801QBJBaRpW9Raxigqusy1ZlHLRo8nnLpA7oR85HLZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=X5E-3ryg41VytmJai6exPjr8ieEQOm7qc1iVM8jv6K_g0AxH9XJMT_VwwmACSzByDmxp8C8xQJAr4oIcQ26e8y4Ffqszp5cvDV8xlDcuEyIj9T-I1JYW-KURha87031RKVg5WG5tqWlApfH3ae0roO0wAdSE6Ki5oubSk2PkLQBnjIv7lg5r0CQJIrXuyFUdwlUbUttW13_tQkspfs7uIPFmOQdhEtFA8ZxJIxAWrSAIhRweGvj270bi1cgKZvk91EgRUk8MlMIqVnUbbkFm217xnWg6nTSrXCKlHLkFBmI801QBJBaRpW9Raxigqusy1ZlHLRo8nnLpA7oR85HLZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
