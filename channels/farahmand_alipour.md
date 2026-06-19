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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 03:39:11</div>
<hr>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aECkuhEdwBJ5-V8aB9IruK8z4kJjmNi0Rt90cJopx_Sbe3HSIgjsnxhsMl6_OO7yQb7jIlFp5O1-n96OYPluHTQpiCJFNXqNZM_F0MiqsR_fKAaFRoylxbYplmUnVRFdyx3RYj3RlmaXjLIT2xBhWAsxErCdED5dGjsbbnOS-xUTsIAz6BYj4qWL81clGrGx4AqKgfUZUTbwELYeLqRym3kZLbZnw9ivRqU7b-H_x3A4gyXcqT9ucFP5UG44i3by-49b-sIpfRTS0ihgD645LHkKjVsFu9WwIxa8FOd6CHQ7y1H8yjY-XTar3keaz5KWO1dzPOuIYnrvtbSbYP11yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpM-RZ5JdQKGve3K5rgAZ-UJxoBkPBBHGtjSa93Mj1mK7_IRaTREVtZ1wfdJu1BMdp9dkoWji_x8RGL1pXiwSmyBS6ijjMOy0y0OsfkqGyc-G0O72jQyu2uolzLzCIfzeWRIFQiuIp3WdE-auPm20OM7uRUSBLSl8Lunlj3807mgU7iMdwVcUgFVKy5Ua-hARJtaoibGLgzZbkXU5err3_WZs7OW9CWri3bPH9KYpjZ4dt6Is1fvp3gTigvo5_E4pOu07I10mhKel7NNo8We8RzLGz4ixXdaQGY6e8yL_kVThGBwrqGA1_keHDsmsXfuMLm2KD70yuQiPTcetPsWSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=bioQav7JfjRE6SnxCODbpUoiens90aIeoHQefoi-jTOC6hZ8cQXGFADElz_qlLKJsf_ffFsk5D_Zix1SNJV2t9bBds2DwVtfsGY1XiS8XhNm0lsEjXMJw6ZTD8E7kGLMfnfIhV4slyyzszU8EZis7Ipou0C-yt4CurukKKk6fsLUAgMH18ultG3YMVYYlh5o-iL3OsAsOwYUHTSRanDJ-l6zaVR8kARTPDCTLaSCjLv3cLjoIJ9GD23bGpXAchhxFU4Gvpqbj6FaaqlWVTlxkczWubTl5atYdYoMVQLaeJYZIklyMk50EoPhnVhpymfmNMRhBlWPuuLX6djGO3vVjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=bioQav7JfjRE6SnxCODbpUoiens90aIeoHQefoi-jTOC6hZ8cQXGFADElz_qlLKJsf_ffFsk5D_Zix1SNJV2t9bBds2DwVtfsGY1XiS8XhNm0lsEjXMJw6ZTD8E7kGLMfnfIhV4slyyzszU8EZis7Ipou0C-yt4CurukKKk6fsLUAgMH18ultG3YMVYYlh5o-iL3OsAsOwYUHTSRanDJ-l6zaVR8kARTPDCTLaSCjLv3cLjoIJ9GD23bGpXAchhxFU4Gvpqbj6FaaqlWVTlxkczWubTl5atYdYoMVQLaeJYZIklyMk50EoPhnVhpymfmNMRhBlWPuuLX6djGO3vVjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyhagpcupVXjPk-nJKEJJ8eFP3HRp43PmbI7G265Q-OYFtT-KJAkqFZxy8bLm0kGY1zpdikpz3uUozvfH43cbsXwqJb4OcZ2ls3Xs__1fqMYcgaV5uQyLe0kuQAQy3b_KI9c7eZdrNx1w-jjpwwMUmgPh9wyCMB7xkDrQmQFQ7gJkt_HF4p9LJ03uPXAD1_-nlwdc_r-OJmoqMjlZMB9CH21NfJMdHq2RhQlfE3ITXxJzHX-PvPKLdjMaTWmW5Q_GlACaO9DqAtALNT4ue38sOX0HQYQVODwG0EdWd10BPHT48-eSuV0tLO65YayiUq6hv0TzFTBjbvPi-GZKCf1HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDPUKyHHYioBeobAF_FBiqwj6fS_xju6xNXDRSUfat3VzjDKtZDxp2j-OtGRpwWrCRsld6WQUnb52VHNswBTVWoZ6HYMV8RQ79FQpjDNvgO4mIjyXYxfkRzy_Td4w7VUV9Crw-8ipAax0xpW5b045XmgL0AqAxkNX9tYlMG13w12gZzpMHrM3FQ1MGedrC7jJTinKv8L50sznVG7MkGaDwYG4QlMjkQJ41xsnkH0rG7omFdFjnxqhm7dGoZJCfh8oVuvY2cqYPL1PaUAGHabv19BuYgubVN-pOq_TLy3rRa3iTPMMNtI89nk6rCtwnNe7iafuLDjLNus0Xbw6hSyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYwsTfVckdui6X27eQmEuORjefB8vf3SxEdXfPDjvlwOAG6FcSMLuNOWbOlxweZa6P9gnf3YhjBvO-RIYXhhRaTKwC7HPrtj4gXlA09lIHju6tSQQCxB2Xq2bcRF4OZ622BdW5zJG-PkrVkcsBwYXLXb9QLjjyTbUXaxX4AXDS0EDOrOCg8lCtXzT1Y9JLMW_E5rqyx3LjnTRFeXq6rApmEmOC7d0j58DB2mOHQdvEmpRmKHws3wQUWL1OV5JUclPLiQn7AuijEgW5iNMHZuEu5iDw8CxBgUMXZBkGlfohEJtDokCrwBiJG3moP2V_C5S9JnaMQdOwmFsFMQDyKbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UP1OQZXMlBAqkFpy2LLUBCgV44cbR-pDocMzLAh8jIIxKGyCT-KofOjEvjXcELSuDnmEHvMJlXDwMkWU4g1qgSZ5YIu-henkAw7oCx0fhKvlqgSH84geZlyv-ojSVgZ4fHvFIgp6Gh6k5FGjfNXMIhnyGDW1BSlfXOgv-gTmKtY4nZVs9HyzHEUPaUNQ31aUYOom5PPmrQ9oacZZPZZ9G4ymZtb4mlrmDc4OQ342u7bnsxBxL4_bGdSIy7PbXBx2mGeYLDDZB6UfAqg6exDxjGSygVFvPUv_v1A9h2gm0Qg80LSsLAiWO1V9MYIF92LYNXO8qmGr_C3MhKZW_thSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=PFYVTojENTp-rtSRwmrybw8WHnFblqXWtxa09dp9EXczhG6vLvxtVsqEotljqkXaF8cXfo7U4hT0RjpraXSD1V-ZS750SinN8Pandu263YhTfTRdHqHvIjOtEoY-H311spWSktt9PwrIxmTxOh90KqGOqGvV1p0pNiWTviEb156_KNGzn1wyMn4yE19ewGcXPX0m40Z7dlsGhGi9vUKUndrulCQwVTTwSvnAzPq3-oPp1OpZDEJYga5ZMQd9afzXFsidtQN4I65o4Y4kcIkcl-0N0VbNv57uXn5kcjoa-9R6fCaWbX-mR-mQWIKdFqz9ed1dK8BGGQwPqJTPQqP6pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=PFYVTojENTp-rtSRwmrybw8WHnFblqXWtxa09dp9EXczhG6vLvxtVsqEotljqkXaF8cXfo7U4hT0RjpraXSD1V-ZS750SinN8Pandu263YhTfTRdHqHvIjOtEoY-H311spWSktt9PwrIxmTxOh90KqGOqGvV1p0pNiWTviEb156_KNGzn1wyMn4yE19ewGcXPX0m40Z7dlsGhGi9vUKUndrulCQwVTTwSvnAzPq3-oPp1OpZDEJYga5ZMQd9afzXFsidtQN4I65o4Y4kcIkcl-0N0VbNv57uXn5kcjoa-9R6fCaWbX-mR-mQWIKdFqz9ed1dK8BGGQwPqJTPQqP6pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkFpNR5fNKxqc9sdPOGQ9l3nGYJ7PBCp2qCxux2mv1ki_v2wy5QHDj1-SS5GiNaZqx-dWJy0Q54O46ER1tuByB6GwD8IWu93RPedOZdB3DzBJwVD_PKP9qzi8Nm2giRrU7lPJUyjK9UvZ2n-p5IJ7kBxeha5QFfl-hABW_HhV4hzUdxTqVOK3l8FAOq7n45Mv9B4hXwMsGdZMSkuUWGUXjaFy0jrl1Vntu04znBenmFJeDKxUN4ne4qEahgtBp--oGr2Hw_1VSzvoyeJAqjcnTRXI9_-LCFJj_bxkuH51Gn5HPlXTWE0fJT47fmU5d6v6GCeItIf80yU009ZJW-QUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=pwVUx1LrMblKqrRodZ7rjW-2jd74qGrk0R28kns4lxU2znZA97s_U0FJ3w8l5Re5zBd3dKjkLI-bSewvxXIxt0jXRuW9e_clqYe33GnBRWmvTbs3ezFNyGlIHNbSoZ2UQOid2Pk0aAnAhcnm5m7QGAbFkW4Yt5PvxHiK-E3-CbHar0L13X_qfTeaGOOQIBhhlwfBbdOuHWguXVFHy_5UWmqM_7NLHNAymEcCv5ZLo4ktgtGJPFR-39CpIv6nEZRhSBdu45R3SU46NCTVnTPbplfyRTk1AQBWwFOQkxYUMN4VARRdU46CxyuAs_hVWG3RFhpRKbT2loC1jsDws9T7LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=pwVUx1LrMblKqrRodZ7rjW-2jd74qGrk0R28kns4lxU2znZA97s_U0FJ3w8l5Re5zBd3dKjkLI-bSewvxXIxt0jXRuW9e_clqYe33GnBRWmvTbs3ezFNyGlIHNbSoZ2UQOid2Pk0aAnAhcnm5m7QGAbFkW4Yt5PvxHiK-E3-CbHar0L13X_qfTeaGOOQIBhhlwfBbdOuHWguXVFHy_5UWmqM_7NLHNAymEcCv5ZLo4ktgtGJPFR-39CpIv6nEZRhSBdu45R3SU46NCTVnTPbplfyRTk1AQBWwFOQkxYUMN4VARRdU46CxyuAs_hVWG3RFhpRKbT2loC1jsDws9T7LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید برای من تصمیم سازی کنید
تا من تصمیم بگیرم!
قالیباف همون مجتبای پنهانه
مجتبایی در کار  نیست!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=Rl0RuRJXE7W3Q9nXjZgIs8sOEwF67_EuWt188Qw-nY01D7N6xzW95e70ht9H8DHqfuyECte2tBtKIB9XtFkkHjlrdO-sPlYxvNzhYpqjBjSz_6nwhMnS8pDCC7qRBOivrvLSoRGTH26E78pze217D8fACgLrJ9hCe11xPPLQfx36cih5SsWrXJmdSWmo7kKbVp5qbzc2AKCwPbNdGVBa-3yGJ15B0OMbSrRsTVojaqGrUyAWTCW6tt3hQN3gomNxhpieQVZueN8dyaENu-ifU3__rxSA80ZZujspGJu1IFW6IQtbKtzm-JTQolj2WXLmhhPluZHcaDhow2AiCccVNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=Rl0RuRJXE7W3Q9nXjZgIs8sOEwF67_EuWt188Qw-nY01D7N6xzW95e70ht9H8DHqfuyECte2tBtKIB9XtFkkHjlrdO-sPlYxvNzhYpqjBjSz_6nwhMnS8pDCC7qRBOivrvLSoRGTH26E78pze217D8fACgLrJ9hCe11xPPLQfx36cih5SsWrXJmdSWmo7kKbVp5qbzc2AKCwPbNdGVBa-3yGJ15B0OMbSrRsTVojaqGrUyAWTCW6tt3hQN3gomNxhpieQVZueN8dyaENu-ifU3__rxSA80ZZujspGJu1IFW6IQtbKtzm-JTQolj2WXLmhhPluZHcaDhow2AiCccVNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhgfB_ccXIuIvfb3JOysozJO0VODiC6Lqy5PdpJ6bnmG5Sl2pSEq_OW9QppAwDkppR1ydwbqyuirfmQS9i8MgZbAcu7GlIbna2IXI_95Wz4Lo5nTujuzBXLVBni0ZiXVKHoMjGZzPrycicKo4r_IdBwrIGdLFwULjC_B_Ha8vQQPlSAmxjUCC6pbik9VpP5bcHX_eInGI7Ea5I7KCW98LmRFySPwBPoEFfSm986cdyK10ZewWau0FSvsv7kqLTIlxrijgtXdC0PvOevZGtCDW0GuPf53RLr_YgQJRU5UDKz4NgfaC7zPunaOtmTf03hyVchJDoOccnozUsTao5QZag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=vOO76UBE5KHEyZFLxhv7rIwRUsxfmBQNZVDQIqYecOXPzgXBriIayGy2HWwKwSA7xS-z4ulFg1Oool78jbmNitf1witMDz47YLROZEuqV40aevbr1ISvH2a5lt0VxNb54Zhw8FLiQbmDDfQP3N-OXUM5zCdbkRRrkBZNcMgTBWKfuPhuKh6bJcuGUELjNHTMEoHVvnxatwVfcSRHHGljbpKU4RXpzalxpaZBJOhB08FdknT8uFbhpAQB1i6jbXeq_V5M13z9wO_OtP_Wctqn12FLv3VaTU_FxE4v_ixQGBY5tRjhexyZgw0XMKU_wZxJHlWoALp5TqbOPGsef-27ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=vOO76UBE5KHEyZFLxhv7rIwRUsxfmBQNZVDQIqYecOXPzgXBriIayGy2HWwKwSA7xS-z4ulFg1Oool78jbmNitf1witMDz47YLROZEuqV40aevbr1ISvH2a5lt0VxNb54Zhw8FLiQbmDDfQP3N-OXUM5zCdbkRRrkBZNcMgTBWKfuPhuKh6bJcuGUELjNHTMEoHVvnxatwVfcSRHHGljbpKU4RXpzalxpaZBJOhB08FdknT8uFbhpAQB1i6jbXeq_V5M13z9wO_OtP_Wctqn12FLv3VaTU_FxE4v_ixQGBY5tRjhexyZgw0XMKU_wZxJHlWoALp5TqbOPGsef-27ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=ejZxnSr9nUo99QWsjjKmlnEHObPrCx7RiF2WW9kF1jHByeG1LEGnSQk3a_Z2B_ZJPwv82n1bRWBmirh7IbqofqqkQZxsQZveX8axnekxI_H3mOI9Dy257FpNCtR49ntyoyBXsQ1uFBjrW84g02SQAOtAFhlnViw1amOcay5cq7T9asw5qZ87sEXM_aa0ZaZl1ksg1nKl5PSoFgb8i2gUi68namn-6KCfR3M_8iHGWRaSYJggumFqXJNpouClzkSeBEgMZPaVrqCRFS7JlnIowKw8wfN5dlDZ8lrj3zk7slao-U3fVoFp-GR_IUM923PkyFX9c_51VJFaEZeJteVtoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=ejZxnSr9nUo99QWsjjKmlnEHObPrCx7RiF2WW9kF1jHByeG1LEGnSQk3a_Z2B_ZJPwv82n1bRWBmirh7IbqofqqkQZxsQZveX8axnekxI_H3mOI9Dy257FpNCtR49ntyoyBXsQ1uFBjrW84g02SQAOtAFhlnViw1amOcay5cq7T9asw5qZ87sEXM_aa0ZaZl1ksg1nKl5PSoFgb8i2gUi68namn-6KCfR3M_8iHGWRaSYJggumFqXJNpouClzkSeBEgMZPaVrqCRFS7JlnIowKw8wfN5dlDZ8lrj3zk7slao-U3fVoFp-GR_IUM923PkyFX9c_51VJFaEZeJteVtoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpcACgoGIVr5sq5LSV3BJuhv50ZFcoqJIs9OVIWY6HFau2RQNmR4hRW4Oa86S6oQJTgi26172IUvmObRBuKBqmZhMX445Von2e-JPuIgGgyVLX86JZjV5-nP2p4eHYtG5YUPlO2x7CF40W27GQpFxQYiMURgS6Tsv7aaHZmGqP4mlMkQr5O-G09IOXjZZ8JSy3Wi63-WJC0H0nElLp8lhyBk0bcqpC2ke23c1VhgCkvr3sYbVvART9G0D-RUHqBNOqgrcDauyqqa1Veh3Im35yFY64DNuDq6QI0O0iIWWdHbkr3bHYRccxRWKlRX2Mu5NJ1wV86z_d8QCPMuJn45nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mije02hwTxFGqI78AFFC2lB1u_wZzPfADXRIx2eIw0Dpu9H3ZYniyTflKbBmbjFOyuiRZdjGzd_4MfBJ673t9t3IHFlVS2MXYXhCoEui6_Rs61JIbEgxzcyX3I9qxzFdkZywdyvRl0Ra-rKx5Yj0J77kQ3XRniqEuBDhYobh_0O53DjprXzSm61r1ytu56I56JdIOAsNRh-Auj8bEdlw06p3Y7cCcrZxscG4ynskbhuExNBAVXLs2BudXypt2BzFlDI_5DjU-xPWLeZlyo39J8yoBBayId3S1Bc2N7wjL0Ta9hG7MHfXT42eLNOwYMVw1C9pVx-MnRne9mwm5Xc-rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k06PwN4sOu3dqWpsN7iOaXPW8RAICzYy6mKUTUdAtKMYZVZEZ5vdBEiVfE-6Kakxphm3_bRUTQiZgC2dASJltWYsdgizlpRgK1Vd7uuypKFqRUoeY7G0uDeMan0qwvZCLG6k_4gt2zSVtB1y0WNrDTB0CTF8oLbpsJEC_-AYU9IvYMcB6nDth6-ptUeQy7cff13p9UPfSMkjhg_XHl9HNQ2t-cykL4s55gEM7Jmfu3Lq-vtwkSGlqOMjM3LQSlCXGF5wC6BMP5ASFFLbVTbUlwKoMXU1o4PxxZNnzYnMRJLCBcjYJI-lzu2VzgcBEmw5-3NQShAyey8n_zjPlMqx5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4vjyYZ7sSt2_X5Ly1WZPwtgHk5wHHptOCBkvEZSyjeV_EexOMIm8bTBoFSvtko_pf2FlWzCNY3Yvk-2ggH4SKX_aQh9SDMoiAUQGQwlBT7UNuSOp3uP-s3Ts0QfsA5uV89XmOCLyFWLDsZpjtK87nynTgYDfmUk6FhVPdlzhup2fHVXzJ4P9dCZdqwmGx4Ycl7CkChUlB5i1ko3aWzpReQ6nwEXZcQdaL18W7x7-7Zre0dylgsz0_tsZvqCdVyk8WKXK0qHStO1l5Q0WIyb0VGVdCZ6RdNVi6xN-frjt3v8bu8TTBFXHo8vSLDk4_e69SzJwMpBaQpA2RkfAbJWeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=EI0IrubheU1ZPJeWhv6jNlJgW-FwwyQL5cal43ATgU2FTps2OeIiocu9Q-Hlml5u08j0VPHMag5uJB-A-9P8n1-alrYjI9KMuo5L3nYxFxtCIPKHQWEiKKIL--Wa4KfWUUwYi8uU1vHeHQBa37miX9ytL8XQ8X0kd-bXe8gkQumwLYy3l8nQKI8B1MTNvpetTImqTmkP7eUICH7107VE8ZCzynb8kdE3losDz1ippGGq1iA41oUngQzCS6jZLChrc4dJkP5OBZCWexOZ16vpcfatvSVZPVb1XiZwh4tRLZj6hosczbqNZyvHMR_gUdGfINdrMhhzLkK8gNctVLWz3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=EI0IrubheU1ZPJeWhv6jNlJgW-FwwyQL5cal43ATgU2FTps2OeIiocu9Q-Hlml5u08j0VPHMag5uJB-A-9P8n1-alrYjI9KMuo5L3nYxFxtCIPKHQWEiKKIL--Wa4KfWUUwYi8uU1vHeHQBa37miX9ytL8XQ8X0kd-bXe8gkQumwLYy3l8nQKI8B1MTNvpetTImqTmkP7eUICH7107VE8ZCzynb8kdE3losDz1ippGGq1iA41oUngQzCS6jZLChrc4dJkP5OBZCWexOZ16vpcfatvSVZPVb1XiZwh4tRLZj6hosczbqNZyvHMR_gUdGfINdrMhhzLkK8gNctVLWz3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieB81Sfypu3cS10yOPwB1etHtA18ibSNn-i3ZhHlwbTaVRrcwKPTJjsPxOgZ5pajCCxeVMNKHGsA986yfN7Xq-U8ndX3DF43tpIb9HzlLpR8eftVrvHPEBxckooN8b5e_3ip80uF3gcyR_FNpyTKJ3LE0wf00Qnzdk82YLyPb9CRCZPPROt_kcFErfY-ZUJaRJ_HiUHIZSpbx2camZePY1us6oHdLTG10AnGAP5SClC4ijZL_dP-o9Pi_HoTp18AN0G6PHr26fcM4P7ZlPKroSRQkY8U6WbmwEAAjtbvDSKPjwoyW6N560h9NXPfXkPtlgCtHQSGYk3RyXXxQI_XwK3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieB81Sfypu3cS10yOPwB1etHtA18ibSNn-i3ZhHlwbTaVRrcwKPTJjsPxOgZ5pajCCxeVMNKHGsA986yfN7Xq-U8ndX3DF43tpIb9HzlLpR8eftVrvHPEBxckooN8b5e_3ip80uF3gcyR_FNpyTKJ3LE0wf00Qnzdk82YLyPb9CRCZPPROt_kcFErfY-ZUJaRJ_HiUHIZSpbx2camZePY1us6oHdLTG10AnGAP5SClC4ijZL_dP-o9Pi_HoTp18AN0G6PHr26fcM4P7ZlPKroSRQkY8U6WbmwEAAjtbvDSKPjwoyW6N560h9NXPfXkPtlgCtHQSGYk3RyXXxQI_XwK3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTipBnC-T2HTNyrv14ORP51HMnCOt7AlaOyrK5NB1woCr9MoSikDtbK4gFjSv6SQXsrZw_oASZ9NxcmhrmEt-f4Pq4t4LmKlwNgPjZYocsCtmoqrn88I4b3Bk-iCJYZPh9lipLsaoOl2j0wa0I-maZ-zysmyM_oUkzAO1PTG53hZcHDmW5V1_45T9RmMKDGXvN0NG3a50ehUMnANxksYCmFfw6g5lxNAqtkGJuA8WLlqO-MQRMKPzdi9x66yNHi6Ma_dtBsCQ7Ys_9dW6RnKWL4LvdfH2rPMNsodob9Eh0MaqQaDmwapEWIQDeCnQMTrPHOdm3MQwy8qVt7mvlIncA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها
محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار
جمهوری اسلامی و نیابتی‌هاش رو به
«اختاپوس» تشبیه کرد و اعتقاد داشت
که باید به جای درگیر شدن با دست‌های‌
اختاپوس در لبنان و غزه و سوریه ، عراق و یمن و …..
باید مستقیما به سر اختاپوس کرد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSnOqauSLpIbyNJdQ-Kj0u3IFnMzXAQFNs8hLqoSevsIv6dNpMK2matwfhiOS1ADFE2yEaD2p9-eHEIznkUebUJ5CzJFfWbs6lok9eeO_EF3OjNdzJKfJXYV16j2ynzLp7sCB1WjDUUUuZAvSz6P5co-8NQO_0DIsqF_KCJlij9WVxy7JwLWUHmdSlh6ytEW1eqhvCT0ZADtLe6EO_EjTdKarTMuYS0bfeyON3t6vDgtmGhA6X6uQcpQJBpQDmKMnj5JsRR36p2aM7bR5gTSNNAGCWofCiBNKYS85tT6JqKDodTCqaYhrbByteYeE_DOyMQlIR3ENF6UcnuXTQUbng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gyiHFowRHqHI1fgP57VxXWY3rO6672BAk9ePX-I4-mzzdiBCwDzQxwhJbfEdRu1ed7rdtSs5nMdeM8UtY3eUEPJNXPuOvq93BSZj61u61MF7Obfd-KB_lrlf2wO5sj7vvypPQJplXNeTST_ouZYQ-A8orIChj2ic3Rb1nacBwv0Zejb_HGLo5w-vjZsGECfku8sTPHXuO058f3rlPmdWPh4QGe_hHCAZSAfatW8AvigAAdAIFJFmVIV_q4bbzYfPYqiw0863rVxIW_7nm0xoM7rAD9l6uuv1hgz43aEN0W6G0typ3ouKYxcznBKaG66kuuPgA7LCKTETZQSiZ5gHMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvFTRxKbXrE2Mt0NzmYcw7FmLud3jYLZAd-jkZQRNKMTf63zbdVz0YdbwXTeACZUgC9HtKeZKNNdvrfoV5dVAxUpjBAqDjgAyKUFRUsM3VzymPBr2USV8zzOFhX7icrZlDqinAS5WK3MeyuxYkZlQsS7wpDXW89qccrgsiLsWg9T8JJxQMem8mZEdKFHHJx3Ffndk4hCqs0-8Gt3ToyvnRbHSw8GKGRmBjrEiIJCgbI8qZAu6NjrQTECZZzc79wP5wMSEjvfEWZ-nCY8-6G4muG1vNxGOSDw-WSNclbT_ttebez5y2boB5dBww5lAqLCd3el388CzPkjNCq8B7N5pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-s_Awu6z2lCuB_W5XGHPIWAEaCDowAf9awrUCoGq7Cyc6XLszccQjFoPdpCcXxmJItNIx4OaHazbStWZ6mIi4NW_ybbfvna8fomNA-ahyfG40c9c3fA8cPR75zxbwKRf6FVqi_Vq4ZdWT81nh23TfShdTwhjbJS9lxyYUI_UfA2avOFSxgetaPDDrUiHHHJruqN-wfg5PPcpKVcR0zMdiF8DVr4KArGWzAkJaNC4f2l7nMKChsLR4wD5a9jaBaQ8tTaFUrJNQzOCvFBXu934OVzhlDoiT5ubNDdmpLeXsMIc_zm3t7-djUXrrb8U-Ou-xnhJ_0qOMfhizgTveWVOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=TMpWsKiXHSVAKhmay8qjBcfLr7n03_swSKWu2XzjgILcTWSEj4wZaZKuWg_0zQV_lez-aYiDyt5c1xeeu6Oz1lVdJ_GWTk75ArozktBjqtzClTkDR0IQ-xyljT9S8mnwi2F5N27D5HT3i6ixZPoQp4twUj43EtNfcZKZtQ1Jp7dF034BSm61y1DEdMHFHaL65FqqqcBWzbd34L3FFTK5Oy855pWSAnhfTN2mwuzdxy-OmvVSqttwkuZIHgnGjfJj17jLS-rZKMej-uqxLqlaajZcebKSydWlozzsbNcmT8RIvM-vW-LgkdzNNXDhIj-svl0cCyIjywYR5aNEUE97bQrlOfWwZBLEFUziMou8tCyXaTxL6ilgO6dKGVUr8BRks0R_DicHjFryIrpyKVDnhVVeCGIisdknfjqGYKVrhhH-dLA6nS1iO4dOBoxWJGUUD99IsKibr7faF3bDNu967HPelzwdSbFIRYbwXLpoM5aMiNShM9jTaYIlssT9kFz55aKw4BHJ6F-LgxMdf3ecYWJyUeJoLgNb9R4K8pYvYTkWdLNEQ3Oy55uyDH40-d0ef6wNY7PMWtEIo6c-UQ5Gjy6VYKd2b9VVMwtWz1moAkbwrHUrWK21sAvYm4uFyIdCFZAGs-Nh43g8JmJibak-9Eni40XBKpoZqnoU5zAXEG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=TMpWsKiXHSVAKhmay8qjBcfLr7n03_swSKWu2XzjgILcTWSEj4wZaZKuWg_0zQV_lez-aYiDyt5c1xeeu6Oz1lVdJ_GWTk75ArozktBjqtzClTkDR0IQ-xyljT9S8mnwi2F5N27D5HT3i6ixZPoQp4twUj43EtNfcZKZtQ1Jp7dF034BSm61y1DEdMHFHaL65FqqqcBWzbd34L3FFTK5Oy855pWSAnhfTN2mwuzdxy-OmvVSqttwkuZIHgnGjfJj17jLS-rZKMej-uqxLqlaajZcebKSydWlozzsbNcmT8RIvM-vW-LgkdzNNXDhIj-svl0cCyIjywYR5aNEUE97bQrlOfWwZBLEFUziMou8tCyXaTxL6ilgO6dKGVUr8BRks0R_DicHjFryIrpyKVDnhVVeCGIisdknfjqGYKVrhhH-dLA6nS1iO4dOBoxWJGUUD99IsKibr7faF3bDNu967HPelzwdSbFIRYbwXLpoM5aMiNShM9jTaYIlssT9kFz55aKw4BHJ6F-LgxMdf3ecYWJyUeJoLgNb9R4K8pYvYTkWdLNEQ3Oy55uyDH40-d0ef6wNY7PMWtEIo6c-UQ5Gjy6VYKd2b9VVMwtWz1moAkbwrHUrWK21sAvYm4uFyIdCFZAGs-Nh43g8JmJibak-9Eni40XBKpoZqnoU5zAXEG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJlsLlm0Mz2J0TvHkNzXuSg3xA5GcLJZqNZJHXATc8KwxixD0OGY8oG6UvjqIg6AeaRqONHJugWR8RMMPTpn0biqgZOkUtsGEPsmDa9RHMKIY58pQtANucztV-T5-DvUFTU07eLJGMwwAYOXr5UfztzdekB-1kdi0GUU4YqzrQ4rgHIfTvBs6haWiaaW5AUGsrI8ph4I4AY1PkDNoHI6HtCUQ-UBzsBujQw3_4nJ9Nx5QpclzKNXShdfGl3T8Znfzw6RhmounT7vnL7dHl8R8qbaQMTEfv5CHMHsWMrEr5sSokE6XG0iZVACKkzCugDaj2vQZGQBvbMyKuC7VnBGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=gckHn-Q1C-4JrgC6T_1zlXlNyh7bP9U7iEi2iEohC8fwGT47w16ku90GHtPcZPEjGFPt-lyda-X1eXDiC6wvdSBrXQ0Qhxu3lFy9iUuZxjoIkwrOYFQkWDVVKKqGnjLval6fn9fI7o7uSq_hWrirH5ILPlLrxR28PhvYYf41WclmCKtcD9XDm_F30bb4WG4Gl8Ay2EFWwXJmxCnFypKtcTg7aW_EATCiY0ULnJvFr3ukRcJOurslOi2yNKy-aV1wwlpf4kjbdxkvvH0-8mRIVEY50t2-S1Ay9J8qW6lHF8v7DSX6HtMMHugBunAG6i7a3kyR3YR8_oT6-drhAydmyoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=gckHn-Q1C-4JrgC6T_1zlXlNyh7bP9U7iEi2iEohC8fwGT47w16ku90GHtPcZPEjGFPt-lyda-X1eXDiC6wvdSBrXQ0Qhxu3lFy9iUuZxjoIkwrOYFQkWDVVKKqGnjLval6fn9fI7o7uSq_hWrirH5ILPlLrxR28PhvYYf41WclmCKtcD9XDm_F30bb4WG4Gl8Ay2EFWwXJmxCnFypKtcTg7aW_EATCiY0ULnJvFr3ukRcJOurslOi2yNKy-aV1wwlpf4kjbdxkvvH0-8mRIVEY50t2-S1Ay9J8qW6lHF8v7DSX6HtMMHugBunAG6i7a3kyR3YR8_oT6-drhAydmyoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=iV897VHrMBygC4jau4SnHwNmRa2tLyt0VnCdLgVFdRcYZPfvgyNtHn87wkqQORgu-4BBlgqpF2IJJ1KBouJicBmC2j-UMYmuEjhbkyzSyu4GbqNQM7WLgJ7B7TxctHmYNiVh7MBiUc0smzq87YAol2M2VDWg07TmYKw-F0zP9Uvw3KdaeCD_xZYwuGhm3UdQPnJDDGxfEiD60Ej5wlHRarLbj22ogjWJ7RPIZbEoPlOv6RWRsiJFxMDW4BbqPOAWop7eZmro6novA4rgPpRz6W4Fbxiz34L8siifuRGrVMzFoVKXmb_va1tBvjvgARBeG_e1zNy4vuu9ZlRVwbXUPVQIq6uQsgz5561mlhJfc23fE5nBI0pkB7ZzOi-CIPVs_y0iyzSYHkCekR2E9VSGL31_-sHms9SARfZ3cXQ2Nup51MH4sQCFmp3mvXZBPpDw6QObW7VKLWB0uicgHl331XrOWtQgtkFCRYRXhBHtBrZN80_tz6widhgn-cNk_b9g_k6xnISr69hF8MEjTBCNH6SmVD2xqatq9NT_nPpkXLW36QEDbuoA9IsUdojreaXPM6Usold-S3YWPunRhMv2HEaCLycQHSDz8sHfOKCefY4O0JIvrR5NPuuI0-Io68OGdr5Fy5F_FJpq_131wR86sSgaEJ15BdgwNh9TK_rwDeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=iV897VHrMBygC4jau4SnHwNmRa2tLyt0VnCdLgVFdRcYZPfvgyNtHn87wkqQORgu-4BBlgqpF2IJJ1KBouJicBmC2j-UMYmuEjhbkyzSyu4GbqNQM7WLgJ7B7TxctHmYNiVh7MBiUc0smzq87YAol2M2VDWg07TmYKw-F0zP9Uvw3KdaeCD_xZYwuGhm3UdQPnJDDGxfEiD60Ej5wlHRarLbj22ogjWJ7RPIZbEoPlOv6RWRsiJFxMDW4BbqPOAWop7eZmro6novA4rgPpRz6W4Fbxiz34L8siifuRGrVMzFoVKXmb_va1tBvjvgARBeG_e1zNy4vuu9ZlRVwbXUPVQIq6uQsgz5561mlhJfc23fE5nBI0pkB7ZzOi-CIPVs_y0iyzSYHkCekR2E9VSGL31_-sHms9SARfZ3cXQ2Nup51MH4sQCFmp3mvXZBPpDw6QObW7VKLWB0uicgHl331XrOWtQgtkFCRYRXhBHtBrZN80_tz6widhgn-cNk_b9g_k6xnISr69hF8MEjTBCNH6SmVD2xqatq9NT_nPpkXLW36QEDbuoA9IsUdojreaXPM6Usold-S3YWPunRhMv2HEaCLycQHSDz8sHfOKCefY4O0JIvrR5NPuuI0-Io68OGdr5Fy5F_FJpq_131wR86sSgaEJ15BdgwNh9TK_rwDeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=XYF2rJnURLbkHbIvsm6iuYFSQv2UkJReFtL3cSadGnpY8KXpm2ccfzwfs-5Y-s3R-I5atsOFyCPpj_o23GXO_IOSJS5JJsd-2EQ9vbiNYgcQDMOVr86mW-TIj6WfSDOokx-OIEIcNDZnI10JDw23B74GBXMbiRFOKQYrjK6mBMJv2AEwWrJxZvpmSn--bIJY_dlICEQQlweGLSK1cl8mH-0D28IJuiAKlkBLOesqTEFdVs8a5Xbe8PgR7wnOuiGeHQll6rZbTBoreWqjX15qITTQ15OX0mYbWsfHkVv_D2Xq8QUhvFqMdwu7a05xNx5sCnHGDeg_E4gmhEm86D0JWoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=XYF2rJnURLbkHbIvsm6iuYFSQv2UkJReFtL3cSadGnpY8KXpm2ccfzwfs-5Y-s3R-I5atsOFyCPpj_o23GXO_IOSJS5JJsd-2EQ9vbiNYgcQDMOVr86mW-TIj6WfSDOokx-OIEIcNDZnI10JDw23B74GBXMbiRFOKQYrjK6mBMJv2AEwWrJxZvpmSn--bIJY_dlICEQQlweGLSK1cl8mH-0D28IJuiAKlkBLOesqTEFdVs8a5Xbe8PgR7wnOuiGeHQll6rZbTBoreWqjX15qITTQ15OX0mYbWsfHkVv_D2Xq8QUhvFqMdwu7a05xNx5sCnHGDeg_E4gmhEm86D0JWoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V1aKViMqNo-o2sw_xjowNIhu3HlplwzPeHYtfMh0scwPU4KZYWi-U_Rb7KyhzZTkqCEfEXWpax1Yl943hQTDtxCAKT1h51QSyFJkZjQF58N0d88PNYnymcJmqbXhQA6NXEfGov3CQefsvUoNn2Izv2Pgg5wolnJCXcP_qyfH0-MkrPWO29LHRGXryTEs0TdmLR7g6lWbfmEJlpk7RTYbpK-zPf-5bgn7Pc1pry2quljXLHwTf2Mw429SNm4nhzIX4nmywbQpW0TjqBjkWTwf35FRDLr_Ymev7-je3OLrR5M1d86QJbUBPjETwN17tKTA_ekhXJ_p_jp2AkxSz2k0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZOCfh3tp9DO4RrLRPHIxy7PxvTFVaHGODJ5_0iNfjXgcC8Z5Zhq_kC8Xg9AQKu43UXt4M8tuAW_uJGiPlQP_d9uPED9QTC37f1sXhA7yzYwN67PYiLXozm4rmJ1Ug2LphfMsV51Yy4YpzighiL6mytk_WKkPGMQaJoV9cUzPsRnRw39KPFJrNcolzzQtctLmvW2wy6oGrWHJ_6tvOMhnH6jYyZNtdX7bx9qq3JofaY1M_rP-s_GCCWmAg39cjuQTvVpTnZJlb3AHNFaqx0SS-UnBTx4D_pPFKrTqkUwVlN3HCpdWJpDo-PFQIQS02EcnbRV8VcjG5YyzBQznT2vTmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPM6f9hWsXzYuO-kN3Y5JxiT6Vtojm_Yue6utu8HGRdFQBPiaIxukzzLW-UkpLu4-RBHnJN0juJ1_pgeqMW98B6pvm8felcSmOwmyl0zT482DNucDnS7EWv605SIiyvLgwWIpqti29y6sIeJ53qBT9WS1wmPinJZcY2h3zu6qgp5AqGme_85fTWKvGwzIeHjHNk_AobvhMIc6P5LKox5FZkF-CYzUiug6ufolJIvBWX9HDy2ygP1wHV_AxKoUA0dtJ2L_W2xWmIjbnK7La1Yamdhr3f2KfeKrBgriiIWONcy583ulCi0KFn2wpek3u07nLWjSZjBHIUIqY8dsOcONg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GouawB_BSWYhM01BCqEm8lxBjVS8rn-oqD9wqLIyEEE4QUlDwZ9-aEtHmBD699vXJ6RbJS0E82k6zx10TfTRl-FOp0o9grWqwq35doKML_sg2sNlB9nsaYZZarw_sIDetgTweyIJAKylIYWaCLx4mAUwQisfyvJHowcZ0eLrtBD5z5PV3aIDgJa7fiz9SlUdUv-ZpdSG8pf02AfqbN8cc28I-kPfdkpFgJItGiHmGavs2Bh25dQfKKFuy-tc2hSW6wloIcW6vzFqbp1AA_u5j4syhgkvICCYrMk4qXnSPiOOtWAwZn9N7BUiTlxEmBEY0LmdbNOy7Z9rMrjwD7sfJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRhAfKyHdPSr-o54U2XmEx9vGYPqKFlZk4LhLnkDFNGevPMesAOfuYonuSOXyskb8TW2VF7GEMGUKIpIk_76G55yyIY66TiJdW6Ku5OcYqzqwo6cvS03CTqDPO2lHKWyfpFsSukw0lhZVQZzGf6aAxaKB-tCAndX9UFdm5-dDOmTGbAVb5NjMp_lMxSXKM5KyxgHJrHISH0RhgkGMQqKrkZQ8Z3oTaqNjAFKLaZw0kTXJdt6FUeA0z-4lKKldX_VbuD2OQiAoLQ635NNcNWNXDhIedYhn07i-k_jgmXTsuQ7NYtC3aaC7UFa7NEg6HmPQjW4Lq4UJIP0YlxC9EWTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=spxmvMx4k19n8pSkBemHDaFYa-G_NkhQS8a1d2B2DBpv_jsbirH-txL5fGZRRSgIWHTgJvZ_bIdcAq_0CVx0vIcYXA7_rY-tx91XpapaXlhYSrbZlrO7gXW9ibV9z4nb2IqC30p_aOt5UcTOHQQ-5e2eMi25oDOcPtnirchDkzJDJdUx1hAu4ZYyQ9TB0aNZ23YPgJSO-w06pDjpOXpH9l4CwpL_GT4z7SZVB9mw5m8A6eBpUgeB_r852z47ZmBE6GRuuTKtyIAjJQml5Gx6ANuEAXZ_PyteMpRkxLtGuNpkZHMRzNxJIZD76dRnAAhk9WuRN5oiuMcVbCS8FYf3fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=spxmvMx4k19n8pSkBemHDaFYa-G_NkhQS8a1d2B2DBpv_jsbirH-txL5fGZRRSgIWHTgJvZ_bIdcAq_0CVx0vIcYXA7_rY-tx91XpapaXlhYSrbZlrO7gXW9ibV9z4nb2IqC30p_aOt5UcTOHQQ-5e2eMi25oDOcPtnirchDkzJDJdUx1hAu4ZYyQ9TB0aNZ23YPgJSO-w06pDjpOXpH9l4CwpL_GT4z7SZVB9mw5m8A6eBpUgeB_r852z47ZmBE6GRuuTKtyIAjJQml5Gx6ANuEAXZ_PyteMpRkxLtGuNpkZHMRzNxJIZD76dRnAAhk9WuRN5oiuMcVbCS8FYf3fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPOpi4EIApJrXVkc3NLPj5hAjuER0fHZNEpFOJRmMwzyMsA-xlPI1m5AdtI_02s3qgdz4Z92ZsKzD5nbNLlVSxYqwzNu6PI19gzkyKnr4tC2DoBCo6cUxkq15hCQjV0rwyz3L4w1K6tEY4_9TH1ki1e6j6AVgH4x5Opo5TDHFt2P9aNFAEvAnk19w-Tv5AKp-OIiF-F5t07wplVaRQMO-XdnbY54hdIvj4ld-RauTbyq_4mDsO9Wlls1WdWlL9A2xa3gG7b4mcgah0OxPYOHvDPatnoKUCDQmTrhJrMSDsNgDDF5aKPmL4klssT4upUdeZS5YkdslAr3y-5DcAs7SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wy0OSUU4TBWxGwbEO5OdZri9KU640YpqohzOwhK1w1Ut0Pu-8_aFI3xg0gq9-a4Ni6Xr2oTRTSaHaniYvIdRIwRblEKwX4p6ASkRf-2jtmMQSwK1X7aMxcphSaifVskKDUBauUgYGr9OcoNVWPnEfrMiNieIYDKfPzb8p3EeAoumoLJfdzX6zvqEC8wUSLaOkET0MoBlGW5k1FVf3C7XIZXkFGIWjgLaaROgeefxng_oHtRxFCaBkKRwLzdsev84iFmkklY_gpAgc3BQwgO4us_dCTCqiBqJAJHIcmGPru21B1F6pAmsD9sU90hcgGNlJjgNXHWfZ_fWyCadTmldSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMgtE3hLAwSf_IAEGJWJTWZhBDnorrb-VyGHQ4EgWxgpICIMapdomQsiAQozEoTzusvdJpUgoSqNnYd_ulf7xvoLf29BtsgK9939mpHGoi3MDK-pIer55GDJJLkI8-uSV3PcP2mA9ScQLAGRvLbiSk38UBJFFOnYedfoOyZFT1UGEqHdssZubzPn69r_UaucRzbz2F2u-KWaMnFAhMxCbWuqBWbzD8X2v5lqJJ4Y-heVQUKsuRPDqX0XgcaA9aSEpm47NN6LMk1KaCnQHeOJy51JzFR0KKNyKa50FpU_TUW_iu55kmj-FaONfrIwaDHbtO6uWYsQ8QzuHEYjmMVJpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «تمامیت ارضی لبنان عزیز» !
«بساط جنگ افروزی اسرائیل
را برهم خواهیم زد!»
جمهوری اسلامی به خاطر حزب الله لبنان
دوباره میخواد وارد جنگ بشه!
آتش بس به دست آمده میان دولت لبنان
‌ اسرائیل رو رد کردند، به جنگ ادامه دادن
الان هم توافق نامه پایان جنگ با آمریکا رو کنار گذاشتن و میخوان برای حزب‌الله
وارد جنگ با اسرائیل بشن.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hC3Tfj4QG31APHlWd_-2b4Lh2e5ZkmFR-kGQJ3IkCrZ6nCb15uVmZ2E8DjDZsNLTGK1Ww5UGhpfnixO3t1cFgDILNbWuUM9HsAkaCrlwKt4xymJjcKFlg2Zdveqf8D4It7T3zU_krY_J5Vy6fvBPIR6AXLck2SkyA3-YDpcIYXLU5JpCTSVeyhtYEFTIiGk1ufvXcabj5PeuhNsXOsLEkWlp-EMNt8LtaLohlwOCs16xofO5U8nCIEMcwmSwG5r13l3faZiKnDmCPqUNPhlKBWpEO9Gul_e1evUXQyULGZm2gNWtk4WqngooAoVfKUrVefhtdtQMXdPX2OgKi_uWRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BycWNiFGHd56DSXgC6WVyxRas_S-HvW4R5_goFpZOmceF2Qo7cm-tnN9pwevG7t9uxSWoOhZxQO-xCkS2kFYRDrk-Wa1qG9YYnQi76yJPcTOOP8WvsUzdaJWhfdtu9z_I2ChefI8697rinKOFO2m3sPyZC4Qd0vESqrLPZwz-LIeP3k5f6jqcNCfXcsFO0wZf53b9PhIAV6gE1DCdkmdU7afn6mtm30yAkMTSR9nFA7dfKKiI_gHV3rw4x7U8mQ_8ZnCsEEtdPhNOmVFBcB3ZqBWifwaQ_qHFM-S4v9PkDBfx3mziVV7DAGFcXL1A0amNRLXCX1q7gAJ-cyMGQ8sdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NlkduuJryZeQls-2OPxyQLSK2lTReMAwE7YOcC2kUKMV4FtmahAFs9Vp7N81faM0LMw5663ms_HrX5DN_TEnqinN-FPoS8PyBITf_gykITayvliQHgcAwXVk_6CLc20WTcO6DIPlum5cuGHemflj-wRwZYw1Z9i8xQYUtaMG3C_P04DkkjgYQmIG5aHHF1AwODzM09eO_q9vC4cjsNFT4nmVYDKA9qbUZJbZ5MfFRx3cKTVidf4abxnhboOoGNelJxm5Ovxs3J8h40crVl0jFv6v6XlhSufkQL8u-XIIfYwKKw8UHiqtmUpIkjiD7wvJcmyjTNFyjRbygzL6n-74xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزادار کودکان مینابه
عزادارن حکومتی!
میگه حکومت همونطور که در ۱۸ و ۱۹ دیماه «به حساب» مردم معترض رسید و دست به قتل عام زد،
باید دست به قتل عام معترضین توافق هم بزنه.
اینها هیچ وقت ایران رو دوست نداشتن
هیچ وقت ایران و مردم ایران و‌ کودکانش براشون مهم نبوده
اینها عاشقان جمهوری اسلامی هستن!
اگه برای کودکان میناب هم عزداری میکنن، چون میخوان یک کردیت به جمهوری اسلامی و سیاست‌هاش بدن.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzyldqFjRCPgkcvPuIjk4IUK1Rtm4Mu-nyYoIRIkrDA89YyLDapIoL52MwlV1i4ruJsMXJOraZ__f91rUsTuHHed98uzNqYaatZXhyuxO9EmwpoZfRYr9xygSYGyB1-Zf_h7UcFweP84gJeXm4SwtPwRaHS5fj2D4gYVJZZA19H2Fdxm-2Ttc0Z5UmHmnwGbgYyBpn3-69PUFvspJ15YilpW3dvfLRlHJrVp81LZJeQ0lvEr6-36gMX_YGvFTfJ0U91WRnewJtJi919EUmyDSrQPLcxEhonv9X1PqFXKMLS9DDEgBPFu7da64ddHYyjl9EO57TC8smHMCXe-4Wy07w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBsvBjEWU1YBCRGUel0ZtsvzgRmIFgWibVaVD6ksOyw3a76Rxa7AScetEowZne7Qa8oKfkOHIAFh3dnVy3iLQdQTkTyGeLIygiKzQX3uDWIGhIB6QUFkNkrzDJs90xGqZgKRBROVPFJC0v_RjR1_u_B4KfEFro--UomQajjhPyQcOgB6JFLUR8gxU_-S0bGebGVjU9xmFci333qnM3jAhIsPXyc7TDklEJv2dlKyCZYL74TqnbDQmbReMj-VFUcdXLmenPR6DaaymhTA-xMXpATgGKveWb1yy_KRYX5HU0simmnlLp3wXLMezqIwFnM8Qxx6nCw6b-YflL5BQW-brg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=LM9LsQrK_pseaNgCcwULXwdulrzUPMM3MJs7NPuVAdAX4j7WawFrQsg_zPavTj9czeGemypfYq7rNU6RNL1ERkD97BHuCox1XQ1vYYM0_gNgb53RdZFGyKjM9iP8QQHikleljbA13ktLlkVJFNmB3bwQpDo6KfxTNkyXcFrd_4iVFZlpjpJL0Hpx7Y7HTiv3Sf0bhvmWSkTJY8bWVRlgQK1f_qUtKjzp3q-K2XrXvQ6re8OAECxiMyBt608sUY0H5hq1UOOqu1ohi9UUsl5SMXqWJJU_8ko-3C28TK6IN6DBbxECzy1J1Wh7YhjS73jjc0sExCK3sKtxvoP7GsfCfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=LM9LsQrK_pseaNgCcwULXwdulrzUPMM3MJs7NPuVAdAX4j7WawFrQsg_zPavTj9czeGemypfYq7rNU6RNL1ERkD97BHuCox1XQ1vYYM0_gNgb53RdZFGyKjM9iP8QQHikleljbA13ktLlkVJFNmB3bwQpDo6KfxTNkyXcFrd_4iVFZlpjpJL0Hpx7Y7HTiv3Sf0bhvmWSkTJY8bWVRlgQK1f_qUtKjzp3q-K2XrXvQ6re8OAECxiMyBt608sUY0H5hq1UOOqu1ohi9UUsl5SMXqWJJU_8ko-3C28TK6IN6DBbxECzy1J1Wh7YhjS73jjc0sExCK3sKtxvoP7GsfCfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=F-a35KBxyw0hO6BJojuIofmFl8qzKWX6Zgqu3K0YIqD0a9bnwffl-hbxtH6YPXGx5rQLhNwzvbzpxGCJI5mCWGA6iFJZhVW5FLqEXtb6s3FTgyRlujerOARoNBC52FfwzRaEu6gbUM-M25xqXDOtAgIJ_IkoyBPX79VLCdXLwPmNZ9aoAsnykRFWXOHgSz-3HGSxYPo25iv4IumI2f2MdD_Nt92SjilQCcYBFGf3ZLz_XqBu4TPAnXx71FofNdo_LanO3bTXH_qSH9U_PDY1EIj4V3BZu6MmZXFQOQeVLrKIYslUMDTOB9jcy9V71MjFoXW4D6WFh6K2woOcR_BxhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=F-a35KBxyw0hO6BJojuIofmFl8qzKWX6Zgqu3K0YIqD0a9bnwffl-hbxtH6YPXGx5rQLhNwzvbzpxGCJI5mCWGA6iFJZhVW5FLqEXtb6s3FTgyRlujerOARoNBC52FfwzRaEu6gbUM-M25xqXDOtAgIJ_IkoyBPX79VLCdXLwPmNZ9aoAsnykRFWXOHgSz-3HGSxYPo25iv4IumI2f2MdD_Nt92SjilQCcYBFGf3ZLz_XqBu4TPAnXx71FofNdo_LanO3bTXH_qSH9U_PDY1EIj4V3BZu6MmZXFQOQeVLrKIYslUMDTOB9jcy9V71MjFoXW4D6WFh6K2woOcR_BxhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=ZDLategKLJKN5TYaZBri6lQ-auK_i9i-iWgF2e982Biglrcly5gZU55OFtjWcX_D6oEkHWqef158GyVCU-72XwBZH9dDfv78pljD6VDyxy4gHlH1IZkQCTNNObMJ0J6pbMfxNiGugANAzug467YSqr9IkgTBsSVxcej1QErcaGB6AN8VXeSmq7XJHidpZx3XeQxKBJTKKmgApRYBkqfereMRHnK1LTowIRqJw0vJRos-8RT1xDrwttwsVgjvo3ibdMOgX4dyncqGGwjoeEDScwrmbH7VWYugvLpl-XI5IWveinGAbd3xJhifepfVONg77rgdnAaeI4NlIRchzipuPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=ZDLategKLJKN5TYaZBri6lQ-auK_i9i-iWgF2e982Biglrcly5gZU55OFtjWcX_D6oEkHWqef158GyVCU-72XwBZH9dDfv78pljD6VDyxy4gHlH1IZkQCTNNObMJ0J6pbMfxNiGugANAzug467YSqr9IkgTBsSVxcej1QErcaGB6AN8VXeSmq7XJHidpZx3XeQxKBJTKKmgApRYBkqfereMRHnK1LTowIRqJw0vJRos-8RT1xDrwttwsVgjvo3ibdMOgX4dyncqGGwjoeEDScwrmbH7VWYugvLpl-XI5IWveinGAbd3xJhifepfVONg77rgdnAaeI4NlIRchzipuPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=fb7tGYLaaIYJkHUQGS86kv-CJcws3Z8EXjiIRbkMA3zMqsuptQtZRryLgpnArSzvCsxlR_nuVdOFvNIKKxPYBQuGQnJ0GjxmH3AV4NLiORui3ypS4jJND6eXwqWrlABHEjrgv8rBrTaqpoBFhPxVXV7lbjJtwwQRjd8XNI-9PJ7ESYoC7bkeVrWlmaIy8dhdc0bBOdufKS-IbD0QCc-fLpkhod7OeQSvMwD1RnQaha_2HPpuhyGQBwhYT_WgKspGg_YyiJu1__0tmLTkJRz2o6HuMSEokT_vcxmPXXBgs0z9cUFPyxEayJdicLRS6HmdJjtmCWhn1GHgowZBR9PUkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=fb7tGYLaaIYJkHUQGS86kv-CJcws3Z8EXjiIRbkMA3zMqsuptQtZRryLgpnArSzvCsxlR_nuVdOFvNIKKxPYBQuGQnJ0GjxmH3AV4NLiORui3ypS4jJND6eXwqWrlABHEjrgv8rBrTaqpoBFhPxVXV7lbjJtwwQRjd8XNI-9PJ7ESYoC7bkeVrWlmaIy8dhdc0bBOdufKS-IbD0QCc-fLpkhod7OeQSvMwD1RnQaha_2HPpuhyGQBwhYT_WgKspGg_YyiJu1__0tmLTkJRz2o6HuMSEokT_vcxmPXXBgs0z9cUFPyxEayJdicLRS6HmdJjtmCWhn1GHgowZBR9PUkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=OezYfS1cKc07Rt7ZUbndMNHcaVsA5ILIotPHkHPRMlruo_3k90QPmnnOehWdsqaSszrr4RZ1G91m2riRCxkysvSsTzcI_mpFFhyDaceiEaxvvBSleYAG2fIF9C6-Ertb2cr7fSVLDeqXFbE41i3A47ArnjdNq5MgL0Gzd4U4PmWFPO17NpX0haj7U4KEWxzsKGGJCNfYNSKyRS0arHaH-obWVPtP9MgH40bVu3sKjF15pzprvWayCYxb5YgFSL9mqEq-bXN8UaqQDZN_zT1itd5M5z0riubdR-VjRkRa2s1nAlRVeDDKVX_aRezRsQMBWMuL8QWdjSHgi3YQz91R6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=OezYfS1cKc07Rt7ZUbndMNHcaVsA5ILIotPHkHPRMlruo_3k90QPmnnOehWdsqaSszrr4RZ1G91m2riRCxkysvSsTzcI_mpFFhyDaceiEaxvvBSleYAG2fIF9C6-Ertb2cr7fSVLDeqXFbE41i3A47ArnjdNq5MgL0Gzd4U4PmWFPO17NpX0haj7U4KEWxzsKGGJCNfYNSKyRS0arHaH-obWVPtP9MgH40bVu3sKjF15pzprvWayCYxb5YgFSL9mqEq-bXN8UaqQDZN_zT1itd5M5z0riubdR-VjRkRa2s1nAlRVeDDKVX_aRezRsQMBWMuL8QWdjSHgi3YQz91R6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=dwZVFAveL3ijknm9fqKEQ25ldSginmH9m9Er-y2q5CEFBzqqCuXEl2gAKEj-Eak0yc9HQq7dyArgAucPGKXMVZ0olZAoJTDCJxXLMbu5kXGV_BNTjHKdxCJ4nBfEP0IPCabL97TZwFbqkZ0efSS4y21s37dJJ90KhbHfdSm4ru12WNGSWORYCjYW6R7zEUKw6XOmOc3Gmn717X5-zzxCAx7H6gLnbC4BFgHN2ByHq3h704J6FlF7iLUhePIiK6kS5HZOeNaKWxAzLPTyy36mN4cWZQyXvBKtuHo4Mvbj3tn9pQfVyy5inyjcbF4HtSBOFdrdvZjlnIm4rtYINICyvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=dwZVFAveL3ijknm9fqKEQ25ldSginmH9m9Er-y2q5CEFBzqqCuXEl2gAKEj-Eak0yc9HQq7dyArgAucPGKXMVZ0olZAoJTDCJxXLMbu5kXGV_BNTjHKdxCJ4nBfEP0IPCabL97TZwFbqkZ0efSS4y21s37dJJ90KhbHfdSm4ru12WNGSWORYCjYW6R7zEUKw6XOmOc3Gmn717X5-zzxCAx7H6gLnbC4BFgHN2ByHq3h704J6FlF7iLUhePIiK6kS5HZOeNaKWxAzLPTyy36mN4cWZQyXvBKtuHo4Mvbj3tn9pQfVyy5inyjcbF4HtSBOFdrdvZjlnIm4rtYINICyvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVTEFSDPO0ESg2Hj0vs-si0c5jjDrTlbEncFPQrcx3CVl2fA1p1brY8djmgh1DKIyLl-lcolqajOMKFQuWDPKmQf-vlV9dn0UKcViti4KXnGnXbaas7PRp6GjcispXrfO7eToHYVnpRmuJ8P5iEtkGwJ3wgqY0PDPiO6MIkiAqcQ6tJp9K-OwZnZmFvKiEEp--ie2Sa18F4hNQXIOii7_Rl9huX2zma8fFAGEFL4eHkFA7DlxFti1ppIqyF23OEwdmzmp5VzpDS0292hZXTJodmgDdeipwGeAsdwSqL0gs_4n-JKLVdwJVvy9hb35LqEU0S7-zkphXT_jo_63pgi2TVE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVTEFSDPO0ESg2Hj0vs-si0c5jjDrTlbEncFPQrcx3CVl2fA1p1brY8djmgh1DKIyLl-lcolqajOMKFQuWDPKmQf-vlV9dn0UKcViti4KXnGnXbaas7PRp6GjcispXrfO7eToHYVnpRmuJ8P5iEtkGwJ3wgqY0PDPiO6MIkiAqcQ6tJp9K-OwZnZmFvKiEEp--ie2Sa18F4hNQXIOii7_Rl9huX2zma8fFAGEFL4eHkFA7DlxFti1ppIqyF23OEwdmzmp5VzpDS0292hZXTJodmgDdeipwGeAsdwSqL0gs_4n-JKLVdwJVvy9hb35LqEU0S7-zkphXT_jo_63pgi2TVE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfQuLTUnIcp3CNre8mpZJAEK9NQHQDQCqSxtxtJ7u9-X7Scv1ZBtd-9HVLW83Fv242OlsrJSCl_WLk6DMI5mK_-t7ilG9u4Uwsg5HPsQZ3yG0G_tz8KIfP9eLVsfHGOolCoECAmhfp37J2wPkhBQ33NhS3Lc1z4OAGVcfQ2hyyiyDs_wu5X6lfJ_m21NGNJOsNx8oPuYtm0E6gYV6Bn6r1BJq0EuDLfaSLmIn43_0OIxWZ2PRSBJ7tq1Z6bWUUURXEYJMzmMW7NAsqqhxrbemiBdei3Wa281lFyNQlFxpqr1BbOqGlHUs_ylvbFM9ek3QYzw-vfBRnEsVYsGZHZz2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=peTzZ_3f23uc2AK8KmLpnpFNqkV1LmCa1X73Yb34vyDnJ5l3DvgeGqKw6AkwrKqgHqd4KGVIh0a6JY-urDTwCHXp5ALW6eDKylr941pC_iHcGArHKJP8N92gNqa7bCrAMmTDNY5GkbrHHPNWCrLl1m_cN0IwJlX-Y7A1HoBaXTAVgAirwQy69hzbwVabldVvZqeHBGs8TEVRUD2E1V_WIGBgWnKR-8QCqv5Qs9GGAkwTApCP1h618VFvVv6-_UccVSXhNanowEoNX55MxMLqRs8g4qlbK48Xe7kBb9WNyLs6ihg2pjKV3qYj7tMMJ2X51vamFSKvnovkTYOy0yDMDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=peTzZ_3f23uc2AK8KmLpnpFNqkV1LmCa1X73Yb34vyDnJ5l3DvgeGqKw6AkwrKqgHqd4KGVIh0a6JY-urDTwCHXp5ALW6eDKylr941pC_iHcGArHKJP8N92gNqa7bCrAMmTDNY5GkbrHHPNWCrLl1m_cN0IwJlX-Y7A1HoBaXTAVgAirwQy69hzbwVabldVvZqeHBGs8TEVRUD2E1V_WIGBgWnKR-8QCqv5Qs9GGAkwTApCP1h618VFvVv6-_UccVSXhNanowEoNX55MxMLqRs8g4qlbK48Xe7kBb9WNyLs6ihg2pjKV3qYj7tMMJ2X51vamFSKvnovkTYOy0yDMDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goF6bFvkbEdb3T4p7SaHpLsHY9rHpMODo59w-ogSkyRiIwXvQWbcoIWpCdOemd8uMTcOidzLTiAjHTnVyJY81OpWqxWuHHZoCglqBMSqygO6foa9SmTZOtGEpBf-8wKjxFPdVu6tj2Wv3m9G3M_I173JpZ-rz8mlhvih1O6l5eFhA7IZRo6TVt5_zG8zj7QUiNbeIi_2VPdi3PRxiEnn1R2Q1ApCm379is54lLNlByFh4OSMWhImTmRqtQUFh1zBekRS8fwvDTS7pa25VRMFfWHbI-xzs1riHLxsD90P8-Ev4wfgySgKct6cthUDgL92rcbamuumUfe5JXtvf4NMWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اکنون:
توافق فردا امضا میشه،
هیچ پولی بهشون نمیدیم.
دیگه به سمت سلاح هسته‌ای نخواهند رفت.
تنگه بلافاصله باز میشه.
بعدا هم اورانیوم غنی‌سازی شده رو از زیر آوار
و خاک بیرون میکشیم و نابودشون میکنیم</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7w8XjJ_0E0W_PfDofShhVtiP4P1i5pfqyuZkU64rLpHj5z3GdAT7i68jYqgFWd2hXJ6qp-w8N1Y7BlsQMoO51DOjWvW7E41DvDP1UFajIZXtpetWmTp768XMLcCPiDdl3caPRvGddJD77Qn-vo405mvSal0-VK8AqmJ1ZTKe4ebmCmqFESLuz1U0tu8L_oco67e-mHIAr5efHwWu09w8ZtgVUmMX3wdFKOwJa_3i948eAyr5DUycd8gkXVgVnm_5N3byll3NrCak6w4fLTIyK5193c3QCtapDggHRWFWlfKZfMbQ8vAdWuajxC4VY60hkESJ95kYHVBTJNQgHuiJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpwSyTsd-QEVjMsazVS9DewkR_m4HGXkwWDOWiBrtAzah_bss4vNmarzoGD0Cb1QQZwRtNGv3qx_KEMzNpQwCK7jdWMp90Brh080UKq_ZZaV2RhxPtq1k0zoCEMgKvVxKkKLyxta0ZdR0ms9YozclQPUaU62FVJq-qKIK9w0Jeg65GoFvCQNyN9lkAGNpTPaB5vmAmMmTHejXazNVOSvBpPinwkfyHr_PWBWGKhFxsW44Wx3GfR_KXL6rmov7rRiu6OZDpFGVEtBeWVzndhPMOo_jg5nB8U2KJocFnmN_kO2b4ni7yDSZSICYBEFngz22ljc9AuHably_n91_7oqTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=KxachnlxsbLrcB7rp8YzbYHXznRZqC0xEpAYZP2PNDl5G3-dwUf9ZlWF9Q5BnR04jkpG_S0yYVkQRDzLISlh5uX6is7DAQ-PerGwDY5dt8wpKW0Z8IuR9hOn7DpqSS9aFNTD47fm_1F6_C5iMW8rDPmX34SusEzwxyy90LYUVCxGr1EJOF1HjUMdq6_3hn0kc52Jiw1vmoa7uZHGfW2ACfLeUxqRKzeB1ne7OBT_k-HhfSQKyuP6Mf-TZBRQ2Vvfw7Op-V3wH6eGLhrSvsNOTCi8hye15Pilln8bvcxz4k58QfvJUjxc9MTSsKX4OYpJebpt8j_w0cv8eOta4gQScQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=KxachnlxsbLrcB7rp8YzbYHXznRZqC0xEpAYZP2PNDl5G3-dwUf9ZlWF9Q5BnR04jkpG_S0yYVkQRDzLISlh5uX6is7DAQ-PerGwDY5dt8wpKW0Z8IuR9hOn7DpqSS9aFNTD47fm_1F6_C5iMW8rDPmX34SusEzwxyy90LYUVCxGr1EJOF1HjUMdq6_3hn0kc52Jiw1vmoa7uZHGfW2ACfLeUxqRKzeB1ne7OBT_k-HhfSQKyuP6Mf-TZBRQ2Vvfw7Op-V3wH6eGLhrSvsNOTCi8hye15Pilln8bvcxz4k58QfvJUjxc9MTSsKX4OYpJebpt8j_w0cv8eOta4gQScQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n34We7tZ2drjfCoeBf05usUv9e2n1BD4LLOU-87B20XgGwFm_-b_U0DpteJagrWFutTXJCQXbvBSXfbDb_lIvYchA6a-iUDLMLcVlMG6KzaPnGwGGvmhiUtnGNqvOUxHOMkY-eGn3pkR1Zk7viagZiM_s-Oq5TqF4P0jd3JdbmM3TKzKspXAdEKFq78jXXpQ6EccCwNRK7NF4KCVckitdkiHtduNkI7HRjHXX1p8zQvAvOkMaVHg7EEWWTzFfZb4Mq3yh5vsoQDTXjdUEjy9RaZB05GSzrlQgJO8pKjXeHCn3T5fx9g_p-xmzzA6f89clmcKQnK9Dl2DsVYIz4zFDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zvbo0O3fh04IQS-a7VLwQ9jjnxsUQA3btNWp0XqewvXpXxls96SK54-HMZrOqyoUC_Hzu2m4JdexDMRsXiE37lIU2zqNB9rfMLqMGnK70aCYmDpZXznnZLD0XtFYMhIGko26lnZjv1CV0A1AcDkVF4-H0FSRovapl2uWKGLaFQ-gVsJQ8uihUVBFhp5RW0Zh0Iqij8e-t0TkxfBwAXobqoVJWQPLIAqdke__b3Mrs5g9AySHGq7J8ioS4A_aSB9rNvHQvxT4gd_oFzlJEBbllYOZjj91VBaDTN1-dNe3O8WcDLpPTHtLYnT4afltlx0-GRN8YnUKNVi2iVWFcBVmUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7m5_ohZcdWmRaYgNOtqwbSgV5V8pNdo6BRT8QykTJmzl6rtrEC8897SFhQahI4Fp0G9iDlzatTzg9eSJgJq5UkAkxN0Stv4H6Dr0r1UVGYpbbKy2LHcVzK_9QSebBneT2KDw5j497aumh-mFzx1PC85F5J9Y5mj_JreY3570Gi8Eo-PqoBVOAQeqyjzTNUaPvd9ozZWhI6qUHXqItxOVUUTQxBbLz69BViDDINVCmKHc06UYhNP9QQP60C4y27yeSiYLYd0Y5KVqhcVxsTH3wxpjQsliqfUC_bUWAdg0tHp0ifWw-5oZnW5778ftaIb1_hRkid68zDuMbLThc4QcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foKN47wij0YWWM-NPEzAbqX6scDkfT1vjXK4vEmOwRS94LudahL15eukkG4ncW-banDZwIfV_cb_KKQY765UFJ1DpuTP83EJ0irBMe3XfGf2IUjmWNO2mfIphWE3xXmUyYa3vfnFUmXmYlFDO-SnDa6aLpo3vK26MX2eNjoq5C49C_tbQiCwHj_qVj9d4HzTx2qhNuApTRWYPMs3OHR3w-DMKCwPkzhQTl6ZLKvV2UoPe9HzsX7cYCaNhgqm4E6crgzbhEmtRM77K6nRvXAaconVPf9fiFHee1LaoOCljDvd_ouBGQIso2iGjum4GSlydnCZGwGLtmoWaaopfaQXeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=Q4sJkZZULtIRmuGYtPtqiM9MsPti9M6XdHMK_OO3BwNuUfMxWiWWucK6gV5UGLZx9NSy_kkGvXvMfcNdlYc5T46RYPZAO2s5foGidJwZWRxFL_VOlEVw2A2giSKEJgyqHdsp9a9AdrGduPq9AL1mKI0f12_XNb7lvbuwmLwIMpm3zYJeE0F6FVXzJmAD6npnk6llpksu7_J8fZ5AI0AC3nxrdGmYvKh5vwQs9IbKzAhpGQcdIAHfygCAT6FGkdANxPvJRytlqyOKK7I5fIS0bfWZnNYa1cRQ6zdYChyHiVG5lkXppl-1KavKu9714rD7FXIvW93dOqICzoRttk04jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=Q4sJkZZULtIRmuGYtPtqiM9MsPti9M6XdHMK_OO3BwNuUfMxWiWWucK6gV5UGLZx9NSy_kkGvXvMfcNdlYc5T46RYPZAO2s5foGidJwZWRxFL_VOlEVw2A2giSKEJgyqHdsp9a9AdrGduPq9AL1mKI0f12_XNb7lvbuwmLwIMpm3zYJeE0F6FVXzJmAD6npnk6llpksu7_J8fZ5AI0AC3nxrdGmYvKh5vwQs9IbKzAhpGQcdIAHfygCAT6FGkdANxPvJRytlqyOKK7I5fIS0bfWZnNYa1cRQ6zdYChyHiVG5lkXppl-1KavKu9714rD7FXIvW93dOqICzoRttk04jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_fPfpBSTm9O9vG4-btUvYZ7Vd2dBrjj1hzTUwnkHnywDbBo9PFZ_lKJdchiEg6scD-fHwZw2ptnbYWAg4K4t4vk9--SLKkV_UkPXCouZpb4Au6iGpkGauCKb770KTDcYZW3rCTakXaKjDX3mGXC7u7UITPpg86Yjh8MWABn7ZAhEqUItPQK0Zy4qEam0pMrqumZWs4hUu2GrGFB7ndsirrkrrPzmN2OuXqxRt7tBwwKP-YHFa_zmyO1XCj1oqicwamomvpiltkrn3IO3R-7q5KtUKo53NwpMJ-3C5Rb7KgoRDGrDAA-hxsVlLMJPKiDI2c5qoWsgQGj3coYnZUXKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZkRBh7kRRxKKLb8ntZXUHXrh47b6eWb0JOU7PGjaE-DYGkmRK8kebnLctzVvcK0KIwbdMdDIjtnHWe3v_faXF5DHkCSrQM7SHJhSS-N0CUaWAYGDdNycZoXfcl4_SUN7lU3NGTnIB3jy-E5fzUqE5mMTnHM-YKBXhxsHTBdw67Q4PHAp5Fm1hZw-aUE6MK86ljoQdzJBVHiKQimAUe7SunazwmaqYX-hZD90J5y1QIMHcdnNyRBX6Zn2ZrDIcEIr6B-8yEf8xA7-BQABiVuXUm_ufjgBsmJGDIe3P6eLPQoEvjslBXR6ZSk_5xIftrU1qRZZ3DyURlCEhzjUx7sew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=hn2WWN1RlHQdU7WEJCPgONYhJD3kOAQVhb0ku_a3kHs1Pkst0XU54XQS4VVTYsNDwyc0O-haV-ZQDhSnhMO5ck0mdmm6Khxo_-8pqMM8h-GN1iTSvhtN4tvGiLlCygscgE9iVXpz6-ojF5Rpumj_Xcc590Ak-k8EqCrnWyA1vXla8Xjsv0oCzwcfxbHpl89yGBvjXVdEupBYAyNIKq5JzLEKBYHvtEwWFslo4rs5chQLqwiiMAeht3Ly3y8mhtEv3yzKC2vekUCsWqwQwofsmlhQHK-zEf7TXCjkzdlRLydM1GgCb_JlUfTH1VN85zYD9FGIWQo0O_pcOCfrJamn8b-GXvGzYg446hcu5M_s8xH1w20-v7GLZ17W_fZDaD_M0F4fyOp-mU3UlSubvfQ8Ey4o17rsjwsOGyWiqxMP1LtqUkbvJo4i4bzRx4nYvPPpmVjtlEoVrjbrP_Nmd0RnFIYs-ftwR_to9n5uE5fCslpOmEh6tunUjC7wUQ2bJR09BsnQ4Q8fpZSwnePBc1p1HNFu48fozogMMZj1busAvEPxjCBvVibYtIkRapNvFzFJ3YALJLwESZqq2qReD_a45bqxutHnQ3nTzadD4V_BUlvDT0ptofWEQ6mriIc4bRX99lcXk0I4bywEDNTAXh8p44wiE6lyTPAcbxVGiNWygi8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=hn2WWN1RlHQdU7WEJCPgONYhJD3kOAQVhb0ku_a3kHs1Pkst0XU54XQS4VVTYsNDwyc0O-haV-ZQDhSnhMO5ck0mdmm6Khxo_-8pqMM8h-GN1iTSvhtN4tvGiLlCygscgE9iVXpz6-ojF5Rpumj_Xcc590Ak-k8EqCrnWyA1vXla8Xjsv0oCzwcfxbHpl89yGBvjXVdEupBYAyNIKq5JzLEKBYHvtEwWFslo4rs5chQLqwiiMAeht3Ly3y8mhtEv3yzKC2vekUCsWqwQwofsmlhQHK-zEf7TXCjkzdlRLydM1GgCb_JlUfTH1VN85zYD9FGIWQo0O_pcOCfrJamn8b-GXvGzYg446hcu5M_s8xH1w20-v7GLZ17W_fZDaD_M0F4fyOp-mU3UlSubvfQ8Ey4o17rsjwsOGyWiqxMP1LtqUkbvJo4i4bzRx4nYvPPpmVjtlEoVrjbrP_Nmd0RnFIYs-ftwR_to9n5uE5fCslpOmEh6tunUjC7wUQ2bJR09BsnQ4Q8fpZSwnePBc1p1HNFu48fozogMMZj1busAvEPxjCBvVibYtIkRapNvFzFJ3YALJLwESZqq2qReD_a45bqxutHnQ3nTzadD4V_BUlvDT0ptofWEQ6mriIc4bRX99lcXk0I4bywEDNTAXh8p44wiE6lyTPAcbxVGiNWygi8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=N5UtXeC2Y_6RHkuKvfA2x5QVS2Yre4Q-lSJL2d1Cw1GUAelW9zCUUInK7VTaAtKESn5I08dJyizwZ4VNSocRstSyo9bOe32Y92lHDB1L00oeal5EInsH6YXv0ynlMUFuQB1X-h9hscKIV9JQdngJ5GdWqTncjTfpbbJnPyb1umccBLE37F_3Qi26xzmsiuJFMWQ2gpBkMoliXQGwIcogqMYrSDYO03nr4s1XLPLXo5g-jm5jgMWj-Fn0EtQwYtr4xD6nVKuZnW6MvIfCDPOP-kiDlBbG_i08_7GoRxfgPkDm_KW9mxpJ0qWLI3Vh567cAkXrk_F7WCe_LKzlzvvcWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=N5UtXeC2Y_6RHkuKvfA2x5QVS2Yre4Q-lSJL2d1Cw1GUAelW9zCUUInK7VTaAtKESn5I08dJyizwZ4VNSocRstSyo9bOe32Y92lHDB1L00oeal5EInsH6YXv0ynlMUFuQB1X-h9hscKIV9JQdngJ5GdWqTncjTfpbbJnPyb1umccBLE37F_3Qi26xzmsiuJFMWQ2gpBkMoliXQGwIcogqMYrSDYO03nr4s1XLPLXo5g-jm5jgMWj-Fn0EtQwYtr4xD6nVKuZnW6MvIfCDPOP-kiDlBbG_i08_7GoRxfgPkDm_KW9mxpJ0qWLI3Vh567cAkXrk_F7WCe_LKzlzvvcWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l59p-YhRqVtiRzRQZQDNyVmJpR5wej7B3RgQo0iz-5oa8B4jBoqQoNEjf3RqtcWbZ71JIFjIyxasxNeOIyYQRkzaxge167SpiiLsKbw9LnWp2esOURVUAIEE1XNHc3xqFz326-HzrP2mChMMgsNQYsAil5-VKXYs0TipUtXKmS6Y7y8k-2qWbVGVIor51Z2ujnU2lFFstQCbSCPEtRvL4rPJkJgJLZ6lesIW7rRfTmxjYYZcX0M2sk_mPn2W6mpJnSfa02atxoiS8_Hh9SxHJPOh_rK_xJrJ9b6Q_AniqPxlCAa0XdIEwPiC-XLe2jP2dsBaEppSi2Bc6t0xrWWNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=mDCgyCZnHhcMrLKzTBor_MEJbtqlhbq2C1GzxnOygwM8KhHrIBOkYoC0uUqlS25oIwkYTPKT09yIpOus8z1gr3gyzXTMGL_2sEjeZjtdvX6FX0gYeWeR2f6SdnTSX0_c3Vx3XOz9bdb94znqoTX44pcTjvACYqdSWlG4DCdpli5YemFVC2J2M2KaI1eNyNbGoBi15djIkk_xCXjPYnx1WBA5WbAzDFM9J6jvx3dYgwDB_GeQ2gQTaPwR5JW2BTJV0_7A_PvFMVGBtjkGF455RZvcxeRKBOKJw-Oy-eYahUpPV6_439QvUf3cgM3s0wfkkIV3DHWaS1iNV8juVNclkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=mDCgyCZnHhcMrLKzTBor_MEJbtqlhbq2C1GzxnOygwM8KhHrIBOkYoC0uUqlS25oIwkYTPKT09yIpOus8z1gr3gyzXTMGL_2sEjeZjtdvX6FX0gYeWeR2f6SdnTSX0_c3Vx3XOz9bdb94znqoTX44pcTjvACYqdSWlG4DCdpli5YemFVC2J2M2KaI1eNyNbGoBi15djIkk_xCXjPYnx1WBA5WbAzDFM9J6jvx3dYgwDB_GeQ2gQTaPwR5JW2BTJV0_7A_PvFMVGBtjkGF455RZvcxeRKBOKJw-Oy-eYahUpPV6_439QvUf3cgM3s0wfkkIV3DHWaS1iNV8juVNclkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUzB52W6oSXZh_EGsfXoR79LMouXzaAAZmm2TE5VhxOFUZsSAVyakcGgkKNiIkqXngNUMPj7dczB3PR8wrb48hU2uEnmYhqEd_Yj69Zci2zA7ZGq87SE2pSx8LQqWxMO1FQaBTZcGcRMHqDRePLn2Wqho06v_Dg9vLOScCQywb3pplaALSCYCE2gbuxkpnQc4cgmzyng651nraPE1UMjoBmNh0wluRirTWS9iJxFtxMd9SqvjpsptY1-1piHFkpWJ859Jh5RfVLEwyn8qLogaNyLQBuV3JVuvjqOx-BpuAQIb5SwfXT33jKCJitM2wIfr2jcDpdCQHOODUZ_qOzjgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=ce0lPxXlqJAStUVkFVHpH4jCG1FxdmLzZICbc78cPe3vfdmrrGE9_XAj7ucqFTGbBN6HCptDOYIB7KbsIUijxgfFrnKXAeqQVMsrauwuAUf-2QEYUARhg1Evy2vzVrNeGoPqcG7o9JpVTH6VMfFoyQU2C4jjvxidIMGdvGqo7pKfJ5E1LTnbStNp3SIVS9VSMWg1I6d0TamEtkiW5Qr0QGSy1BCuHcPwvAgbWj8tHVoSZLkYrq57FHGaGmZ8wueuvkdbz7SJ9Ull5a6Sum5ezP3RBXz04r3XGXllOMwvOuFImUqtyRjYLuYrZHyzNU17yNyTHcCBHlCID89UsZZBVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=ce0lPxXlqJAStUVkFVHpH4jCG1FxdmLzZICbc78cPe3vfdmrrGE9_XAj7ucqFTGbBN6HCptDOYIB7KbsIUijxgfFrnKXAeqQVMsrauwuAUf-2QEYUARhg1Evy2vzVrNeGoPqcG7o9JpVTH6VMfFoyQU2C4jjvxidIMGdvGqo7pKfJ5E1LTnbStNp3SIVS9VSMWg1I6d0TamEtkiW5Qr0QGSy1BCuHcPwvAgbWj8tHVoSZLkYrq57FHGaGmZ8wueuvkdbz7SJ9Ull5a6Sum5ezP3RBXz04r3XGXllOMwvOuFImUqtyRjYLuYrZHyzNU17yNyTHcCBHlCID89UsZZBVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
