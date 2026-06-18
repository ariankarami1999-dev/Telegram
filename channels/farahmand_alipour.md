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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 23:42:23</div>
<hr>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aECkuhEdwBJ5-V8aB9IruK8z4kJjmNi0Rt90cJopx_Sbe3HSIgjsnxhsMl6_OO7yQb7jIlFp5O1-n96OYPluHTQpiCJFNXqNZM_F0MiqsR_fKAaFRoylxbYplmUnVRFdyx3RYj3RlmaXjLIT2xBhWAsxErCdED5dGjsbbnOS-xUTsIAz6BYj4qWL81clGrGx4AqKgfUZUTbwELYeLqRym3kZLbZnw9ivRqU7b-H_x3A4gyXcqT9ucFP5UG44i3by-49b-sIpfRTS0ihgD645LHkKjVsFu9WwIxa8FOd6CHQ7y1H8yjY-XTar3keaz5KWO1dzPOuIYnrvtbSbYP11yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpM-RZ5JdQKGve3K5rgAZ-UJxoBkPBBHGtjSa93Mj1mK7_IRaTREVtZ1wfdJu1BMdp9dkoWji_x8RGL1pXiwSmyBS6ijjMOy0y0OsfkqGyc-G0O72jQyu2uolzLzCIfzeWRIFQiuIp3WdE-auPm20OM7uRUSBLSl8Lunlj3807mgU7iMdwVcUgFVKy5Ua-hARJtaoibGLgzZbkXU5err3_WZs7OW9CWri3bPH9KYpjZ4dt6Is1fvp3gTigvo5_E4pOu07I10mhKel7NNo8We8RzLGz4ixXdaQGY6e8yL_kVThGBwrqGA1_keHDsmsXfuMLm2KD70yuQiPTcetPsWSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyhagpcupVXjPk-nJKEJJ8eFP3HRp43PmbI7G265Q-OYFtT-KJAkqFZxy8bLm0kGY1zpdikpz3uUozvfH43cbsXwqJb4OcZ2ls3Xs__1fqMYcgaV5uQyLe0kuQAQy3b_KI9c7eZdrNx1w-jjpwwMUmgPh9wyCMB7xkDrQmQFQ7gJkt_HF4p9LJ03uPXAD1_-nlwdc_r-OJmoqMjlZMB9CH21NfJMdHq2RhQlfE3ITXxJzHX-PvPKLdjMaTWmW5Q_GlACaO9DqAtALNT4ue38sOX0HQYQVODwG0EdWd10BPHT48-eSuV0tLO65YayiUq6hv0TzFTBjbvPi-GZKCf1HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDPUKyHHYioBeobAF_FBiqwj6fS_xju6xNXDRSUfat3VzjDKtZDxp2j-OtGRpwWrCRsld6WQUnb52VHNswBTVWoZ6HYMV8RQ79FQpjDNvgO4mIjyXYxfkRzy_Td4w7VUV9Crw-8ipAax0xpW5b045XmgL0AqAxkNX9tYlMG13w12gZzpMHrM3FQ1MGedrC7jJTinKv8L50sznVG7MkGaDwYG4QlMjkQJ41xsnkH0rG7omFdFjnxqhm7dGoZJCfh8oVuvY2cqYPL1PaUAGHabv19BuYgubVN-pOq_TLy3rRa3iTPMMNtI89nk6rCtwnNe7iafuLDjLNus0Xbw6hSyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYwsTfVckdui6X27eQmEuORjefB8vf3SxEdXfPDjvlwOAG6FcSMLuNOWbOlxweZa6P9gnf3YhjBvO-RIYXhhRaTKwC7HPrtj4gXlA09lIHju6tSQQCxB2Xq2bcRF4OZ622BdW5zJG-PkrVkcsBwYXLXb9QLjjyTbUXaxX4AXDS0EDOrOCg8lCtXzT1Y9JLMW_E5rqyx3LjnTRFeXq6rApmEmOC7d0j58DB2mOHQdvEmpRmKHws3wQUWL1OV5JUclPLiQn7AuijEgW5iNMHZuEu5iDw8CxBgUMXZBkGlfohEJtDokCrwBiJG3moP2V_C5S9JnaMQdOwmFsFMQDyKbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UP1OQZXMlBAqkFpy2LLUBCgV44cbR-pDocMzLAh8jIIxKGyCT-KofOjEvjXcELSuDnmEHvMJlXDwMkWU4g1qgSZ5YIu-henkAw7oCx0fhKvlqgSH84geZlyv-ojSVgZ4fHvFIgp6Gh6k5FGjfNXMIhnyGDW1BSlfXOgv-gTmKtY4nZVs9HyzHEUPaUNQ31aUYOom5PPmrQ9oacZZPZZ9G4ymZtb4mlrmDc4OQ342u7bnsxBxL4_bGdSIy7PbXBx2mGeYLDDZB6UfAqg6exDxjGSygVFvPUv_v1A9h2gm0Qg80LSsLAiWO1V9MYIF92LYNXO8qmGr_C3MhKZW_thSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-163T1-8foO1eF2v6_mTs6NJeCbnfR9CS38ZJ5kn5KFr9fm1aKs0z2EE3riY1D6D4SOO84ztQR0-hoFEU6HgVAWxBLaBBByj3NHMHiaxkom9ZDIm4ZBCYKIj3vOeQu0tHuRzWTrUVP9fm4PopGhZI6zqUXiqG45jIQDAFy2OPsWkJi7jkQVqPWNbk_YzzpBBzpEXsQaiipMllGuhrfoiGIKca-crJImFBcbH_4yaUE9pDWpF7mUxWuvWs8lyt_pNoNZoDWX8E-MvE3Orsdu8-tQSatV37iMJEXRGSHwbQRTGINIi1u0hbNclhpLokrBSSkPoiMKw1MyrkC8GAFCIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=W7IqxDQMgq2G1rN6J-kf9S_D28J1Axvhn9q7hsnc6--ctW3rKajxGMzFzn9jPr6KHl0iSp3zUqNRmvX6CFT4FQexJ5PwOghR_tqWi8JzzIEhV1JqGWCxOxbusZ9j8TSOJj6iW2QWZama4SPBfro8d5TIhWHALYYioxGbthPECc66yy0dFDnhSgrR6aVKsiszAEqn0eGiJMjaGRVEw8tAG7MZs-gtZlotID7u2KofzaXan108yqa8tuguPJ_HyWvlgCQOK9SD5dR2-8ecCNtwWPrUwMLk4c-0-AK4wFkp2lRLp0v6qnlvgi3ZxkAOjKsNkO_Op0okE2En0_LGXvV2Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=W7IqxDQMgq2G1rN6J-kf9S_D28J1Axvhn9q7hsnc6--ctW3rKajxGMzFzn9jPr6KHl0iSp3zUqNRmvX6CFT4FQexJ5PwOghR_tqWi8JzzIEhV1JqGWCxOxbusZ9j8TSOJj6iW2QWZama4SPBfro8d5TIhWHALYYioxGbthPECc66yy0dFDnhSgrR6aVKsiszAEqn0eGiJMjaGRVEw8tAG7MZs-gtZlotID7u2KofzaXan108yqa8tuguPJ_HyWvlgCQOK9SD5dR2-8ecCNtwWPrUwMLk4c-0-AK4wFkp2lRLp0v6qnlvgi3ZxkAOjKsNkO_Op0okE2En0_LGXvV2Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=AjNvpk8SIAejH8Xap_JlIyhfiD3fyKP2B-moz62_lt6To0e4pV5FfFFXvB98uh7LML-mx-cSbZpXhj6Lg1jmcZwQ2BuiWSjxN8SbCFRtsuj1he-Mn6Idrv1Tuh0_lEjMXyxAm0S3EfygQY_Uq8e0HB0CqrOxkIA0NCmfDQtl_W2W3lBYyxQONuwT_pjl85OCFnMfpA7BpqdciC-r0jGOu5s0LiGc3gtIWvxB0N3apV890OvCGWqTpfVnLpWzbIvRGfKP7coBr5PBEOWJ7_6_4pp90G2eQlkcDD7nS4HMXoHw3Ql_5F8OynPGaZzvWLq5Xe4r_nCxPLYGawmpLZxD5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=AjNvpk8SIAejH8Xap_JlIyhfiD3fyKP2B-moz62_lt6To0e4pV5FfFFXvB98uh7LML-mx-cSbZpXhj6Lg1jmcZwQ2BuiWSjxN8SbCFRtsuj1he-Mn6Idrv1Tuh0_lEjMXyxAm0S3EfygQY_Uq8e0HB0CqrOxkIA0NCmfDQtl_W2W3lBYyxQONuwT_pjl85OCFnMfpA7BpqdciC-r0jGOu5s0LiGc3gtIWvxB0N3apV890OvCGWqTpfVnLpWzbIvRGfKP7coBr5PBEOWJ7_6_4pp90G2eQlkcDD7nS4HMXoHw3Ql_5F8OynPGaZzvWLq5Xe4r_nCxPLYGawmpLZxD5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvF2C-4CwgMZdh7ApGLMxPNdWQclWbc3-N2rQn6NCJNVZmT8Qt1hy0IOLFKuKxYB5oFnQJpSXgTyRtK9roxqEaysGVclPABDl7a7PoD-tghjtYoQbAt3h4AqquZfTs5ErFm7GEIyGen0S-HpTS9fy3Y9MNTg7ATUE8UGasLlwBvAwow_mxIUL-i7wkK2gOXOjQ5By2byVo7PRiKGqSF702xDVMLF4ZBLUwBGH6aLBy634vYjXHWikIG6nlF2Hi7eEA-eik7nTzBf9yWI1TGbi5E3czQjGjyDikepb_2_UpoLEvH1Wuq3vqXQDdewMbZ1vPkVdxWCLkpKnWFcMyqcaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3-d4iOsmfD-Ybk68inj39Kg3HwVvOoikk4sVY17XuUbdGjOtxhE9rxqbBNxyaxJ3Yu3k7V1edcAxfw9kxDsL5bVrkexPHGJL0uHVSCDqfr8KLJxvm6Nz1tnqGJOryPqGYUUlXbs7xIW7eiqMK8ZuR8DKPdUxmynxcGeQPrOEox9B5VHiaP0TOdcS9SUSl2sA8SXwGqQL608K_g3_2gWU3656jwy11jF4f4FzUQTILVxBSHn3ljixcNGD71VoEFhQ4K-2Di-zPujJx5vPajFx95Db-fyIYn4SFSxy4BP-EMh2XgRH-CD3GFWL4-BrqUOv2rqOCqtwS0FUGfZvWx5_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k06PwN4sOu3dqWpsN7iOaXPW8RAICzYy6mKUTUdAtKMYZVZEZ5vdBEiVfE-6Kakxphm3_bRUTQiZgC2dASJltWYsdgizlpRgK1Vd7uuypKFqRUoeY7G0uDeMan0qwvZCLG6k_4gt2zSVtB1y0WNrDTB0CTF8oLbpsJEC_-AYU9IvYMcB6nDth6-ptUeQy7cff13p9UPfSMkjhg_XHl9HNQ2t-cykL4s55gEM7Jmfu3Lq-vtwkSGlqOMjM3LQSlCXGF5wC6BMP5ASFFLbVTbUlwKoMXU1o4PxxZNnzYnMRJLCBcjYJI-lzu2VzgcBEmw5-3NQShAyey8n_zjPlMqx5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBm6Sc2nkGP_lwWY61lTD0qladaL0EKwB1cHMcbUFQB-6uyKuYkUVTcUNkhGHwZuvlJhR_iwkVT2rt8KKcYRnWgrPIQIk26bvTD4jFmedMBPCd-HOi9I7H98RRGRs5Ayon0flkjeAi7T6jQbfA8kr1LOAi3xuBWCVpRnzCkxAkc_P8bEcSfLoN_AYKulTfM50ks7MtENtsggk96fAzV2-fgbP3X2Ojy3X6oMcMvnjoi2bzvcMZkbxMJOy3tAZHQv0_yFzpCpLlbndaRdzjKZHdGnJY7CRcAhnVBXPIHDFPtoMdyDD8FmYM_o2G3GuoAs6sYDhWW6aIqO9hwfaVqAbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=aFHdNePAkULQzuh25H2nmFKtAc8wbhV01a_hoGFdl5E7zorkBJGaIGZdQkKEB5wNh56pThC5aecku9gvaQk0LGWRQ2WlMrpVZP6uOsm3V7iuGbMATYEXOuJ3PFYWVYuYAuw3HqBVXNLvXq8Jz8owqZbnbw9fWrcEBcOjB9wc4aPg-jf494A3PTBv6EqHIS4PCdBYw0Luugcebev4P-3jZM73hw-H9lc-QcIJrf6t4KyhYBMewlNmOEigsPcJvkft9m7Jj7iRujIDSY8xJwdLB_sWxOimq1Fn1d-grH9yGUiORnNX7drFSxDp09B2dCFwZU-Mv3i4Qfr8DFaFkbGYIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=aFHdNePAkULQzuh25H2nmFKtAc8wbhV01a_hoGFdl5E7zorkBJGaIGZdQkKEB5wNh56pThC5aecku9gvaQk0LGWRQ2WlMrpVZP6uOsm3V7iuGbMATYEXOuJ3PFYWVYuYAuw3HqBVXNLvXq8Jz8owqZbnbw9fWrcEBcOjB9wc4aPg-jf494A3PTBv6EqHIS4PCdBYw0Luugcebev4P-3jZM73hw-H9lc-QcIJrf6t4KyhYBMewlNmOEigsPcJvkft9m7Jj7iRujIDSY8xJwdLB_sWxOimq1Fn1d-grH9yGUiORnNX7drFSxDp09B2dCFwZU-Mv3i4Qfr8DFaFkbGYIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieLGpkLyjzUGq9edLLzxDCOEAvOlTtgbPjAhTtTgEMC4cJyuhMXlN0yGj4EpDRU0CKrLPmWghcOVfuNGEN8PKvnnUV_5nCHFBzazZTdZAd8jrUXHtt8fSqPByzkRSMXwjcshllVL6FnSUHzlnTMAYwS3L7h8biEjjdPiKV_GcbtcOyJmP5WjjuupdkEYIMoIFWXUtWLTNebvl_OU4D2lGiVdmW_hcTFt1wX6HfR-1mix04_P1DQnE2vqKLIekNc2HxWRgfie3Z1VPi-kMr3yLzpXuOLCBMGqngKEZ-spwSnVY6JCKbknquioKQ50ZIAB_HtzXbz0LkcFXrX4gki7CCYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieLGpkLyjzUGq9edLLzxDCOEAvOlTtgbPjAhTtTgEMC4cJyuhMXlN0yGj4EpDRU0CKrLPmWghcOVfuNGEN8PKvnnUV_5nCHFBzazZTdZAd8jrUXHtt8fSqPByzkRSMXwjcshllVL6FnSUHzlnTMAYwS3L7h8biEjjdPiKV_GcbtcOyJmP5WjjuupdkEYIMoIFWXUtWLTNebvl_OU4D2lGiVdmW_hcTFt1wX6HfR-1mix04_P1DQnE2vqKLIekNc2HxWRgfie3Z1VPi-kMr3yLzpXuOLCBMGqngKEZ-spwSnVY6JCKbknquioKQ50ZIAB_HtzXbz0LkcFXrX4gki7CCYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM67VOaFxLP6aOx99SwxyM5BjtoVNjcHzu9SU3ud-ZK6KhCVe9989TdecvqUtwrrD1cBFXOLJXCC_IOm9zspjWgv9YJhEYCI98FXKQStpNpq2NkYVOFT3XwlJgYlpXyeg8MVSHIriw5BrNRDGpIDGnThVWEZ-JA3IViQeDg0yHpzxNMKCm4Kv9ps5-VkQlR2VWc9fqYc83SQA330XfXRDr26nWfvUj7J6V2ncDi_di9b8gJaOtR2542isqVUDHbZu3z_0pXfCsnW-EDSFYPs8F1D-mtetj1aNzarw9r-1AaHsUKDOt5cJ7ZBppn1hCYh4hDX_gbleSAkeu9Py7JQSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8wE6juWIVtXocY6uBT4tycYbGDtYsEjDRUrcVVcdbTM7aUy72uPVmyVK0bt0CHcebtDHb2HfenUp-aJpS0oTPJasU6NO6X3YF5SY6OHEouemz8ktj9xbUag_VIjYfRwC12rXfQterWBYdkSxUAG4l241YswZQQotkThdgwkRV8bXOwXBi-BPwiEm11FzksGs2lVUMQbAI1P5FD5g3h9SQ4rTNHVs9_bj8cj9-J9gj3VGzFPi-u0z3KXX4xYU_GSY6gZbojuYQOAAEAtQKFm9UBafDVgc52uMW7najQzqJhLg_eGfQyYgpWGdNqNA5xcb3py4M46sfdj4y1iAYxFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/atmnG5AIYlJsnCqenvLsNkVI6HWwCJq_sLguo91MzeQ7h4y9fFySG4oG5X64RrMJHDOI-h4-fIyjV5_LNXTVuZQTNLf-taz4xQ5blk7L4qaPOl2BqGw2GHPVRW2KzEmvTVjEZt9Mb0686tsYn7tZy5WohNFzcbTSE2I7fUJYCLqgR-VgziIBMyoolq9d56nGndu0rS5vFpElmsmQaLXW7LdSetcEd6vZi5Q3iTMf-W_2D4AO28TE_IS7cUiCkPtv4AVvzTA6IOt_2ftP2QlFMsxTdzckBBbMvQ-j6e40pGcx3D4YKoYUslMIPX17BbXObht0qKsJvRynx5MYsdPw5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvFTRxKbXrE2Mt0NzmYcw7FmLud3jYLZAd-jkZQRNKMTf63zbdVz0YdbwXTeACZUgC9HtKeZKNNdvrfoV5dVAxUpjBAqDjgAyKUFRUsM3VzymPBr2USV8zzOFhX7icrZlDqinAS5WK3MeyuxYkZlQsS7wpDXW89qccrgsiLsWg9T8JJxQMem8mZEdKFHHJx3Ffndk4hCqs0-8Gt3ToyvnRbHSw8GKGRmBjrEiIJCgbI8qZAu6NjrQTECZZzc79wP5wMSEjvfEWZ-nCY8-6G4muG1vNxGOSDw-WSNclbT_ttebez5y2boB5dBww5lAqLCd3el388CzPkjNCq8B7N5pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUmjfCqKpak4A8QTNQzn88l2p5p317Z3ILkE0jr_2quRJ7x13fMLB9u0Vs7tw2k6wlqJ6weWQckq3Z3PqFAZ7JKUo_JVJmEmks4wUfgoluZ0wTMLQZTlQ4milAQIzX2O57GzktD7RDK2rhhymy-p4a3UTojUry6yOfweF0khZzjhHNmRokadW_lf2jyGqHpNtqtp-fKq6FiOs28FRc3Q82J2UUiqJhluhp_nyjVacBVyKgJL0nmsGTT6Lk28f3VeaXIlL-3J4F2JpvPzqjrXLqP0EAO1Xv9A6Nzv3pdxxHQq2zB5fM-zl5bYOVWiA-SsoyNC9K2QEP2qQJQMjqOtkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=uq1U3C2Bcp4qOHuLVsvUNk7-tFpQEKHtqZ893KRAeR5jGzwDO0sNWlVmAm5yA-OQXBV45oikdrPEH4ghHzZ1cGRomj2dy5dQv2xMYqh5C_AM8bUfl7TBQW9hPuwTJSxuee2qcr8xgJvHziadKFkXFudWnZzkKmQC-q3JNW-onx4cdmQ35vFp6lxm3JV4d-F_cbXUN_E4s9S7MlLwC1NE2kBzkmmr34MPQ6quDDZwtdVjqkX0uSwOMR3pN0nC8Z-_If3ez7rUQd1IyR9d_bLaRkspmZ00EGFypJHyvjMvoLdmO0MuxqNMg-Yi1PMUoquIFFnZq3dVKRIhG07N_TCr055mldCwrt7CpTOU1ZQEeXgGGqlpCeGrRihXNLk8smssYRFHT4jiTu1K4ewQjiMGBHvpLTtcTUEgJssgaP7CHTLuinFeCCfdJ4z_e7KN7TxL9l-YxfRmsSEXVJxJ6kAtPfdE_VaJ6wgXPAmQfcqYQf5HcycSA-BIKCdC9LaJbuf36RFmX4ApHzGdObtcqbkqdSRc0qkX1QQJrmLXoGsPL7D6qL1zIN7Yfj2Sn5HTCg4PeI6_d9HtyErBl-BLtnz_i7Abply93Tjw94Zf_1fYo8s7mYWXXdhO88tdnJTS_HblUw3MIo5sTadOIU7c2AG3N9bQjw8H6lm77t5H8B0Mwgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=uq1U3C2Bcp4qOHuLVsvUNk7-tFpQEKHtqZ893KRAeR5jGzwDO0sNWlVmAm5yA-OQXBV45oikdrPEH4ghHzZ1cGRomj2dy5dQv2xMYqh5C_AM8bUfl7TBQW9hPuwTJSxuee2qcr8xgJvHziadKFkXFudWnZzkKmQC-q3JNW-onx4cdmQ35vFp6lxm3JV4d-F_cbXUN_E4s9S7MlLwC1NE2kBzkmmr34MPQ6quDDZwtdVjqkX0uSwOMR3pN0nC8Z-_If3ez7rUQd1IyR9d_bLaRkspmZ00EGFypJHyvjMvoLdmO0MuxqNMg-Yi1PMUoquIFFnZq3dVKRIhG07N_TCr055mldCwrt7CpTOU1ZQEeXgGGqlpCeGrRihXNLk8smssYRFHT4jiTu1K4ewQjiMGBHvpLTtcTUEgJssgaP7CHTLuinFeCCfdJ4z_e7KN7TxL9l-YxfRmsSEXVJxJ6kAtPfdE_VaJ6wgXPAmQfcqYQf5HcycSA-BIKCdC9LaJbuf36RFmX4ApHzGdObtcqbkqdSRc0qkX1QQJrmLXoGsPL7D6qL1zIN7Yfj2Sn5HTCg4PeI6_d9HtyErBl-BLtnz_i7Abply93Tjw94Zf_1fYo8s7mYWXXdhO88tdnJTS_HblUw3MIo5sTadOIU7c2AG3N9bQjw8H6lm77t5H8B0Mwgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo8IW4-gAzaaRrKkrwTd06PQu6vbVqBB9B-iTnasvfRZi1TETs-yzONQsZbPU485uMgEda1zIZgoIhe2A7qt4LcChxoLHBQmk0E3z2GRR-tpWFTqXHoELrbmYmAeMa_YhX_zv_MchIwsa104R9bSN36Cxat1NcBVMFn4tpyMMdzQ5c-F-UjLNNaBshk4p7jJh9TlAwk_gFmx6_WgNQkgQyUP3hH5b61uN6mfEN7AUVbR9nYdgP58BKI3aAQcdAuzpVxBxlH8ctb6o6XH-L4RK4mmyJyJ3_5rWbYHWAt3Ak0OiVzl5jrpWj89slqxmBPloMqgqQ7-TKmimwqcfRsfaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=H6-uB6Ry-NT0Rk9664-mkdE4PsglWKjOGgg4duQHiO8gsZttp60v7rWVtwaSMmdhP8uf7dGrn6J-pylVMwP6Sr3ExA1Glwz0j_eyasiuPJK2_suhOmuM4m8cxSBQ0vWU_O8jVXHMQaNrEAy_jaJhPQMLp56BwA59Vm-odOEDaH4ynv362xBGTY9b66P6NbtGo4HLHedEZRxcd4RFYaS7FbylwnV9H_X8yYqzxxsaIUJzWdiU4bvFEGJP9mEzMq3EdWM0DDsXHwIHnshRFKDWdL74OvMj6kciIZMrTb8AVKeyFYgcmwLoh5B5sflOq41KEJdaLUepYd293cegTYbrsYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=H6-uB6Ry-NT0Rk9664-mkdE4PsglWKjOGgg4duQHiO8gsZttp60v7rWVtwaSMmdhP8uf7dGrn6J-pylVMwP6Sr3ExA1Glwz0j_eyasiuPJK2_suhOmuM4m8cxSBQ0vWU_O8jVXHMQaNrEAy_jaJhPQMLp56BwA59Vm-odOEDaH4ynv362xBGTY9b66P6NbtGo4HLHedEZRxcd4RFYaS7FbylwnV9H_X8yYqzxxsaIUJzWdiU4bvFEGJP9mEzMq3EdWM0DDsXHwIHnshRFKDWdL74OvMj6kciIZMrTb8AVKeyFYgcmwLoh5B5sflOq41KEJdaLUepYd293cegTYbrsYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=oyDZZ20TErFXfTbqUTu9E-CRWTJEwEReeBrWvAhY5re-8oH09rTWHNSligb9Tjee1R6MCPs65zl_QnubHUihQKX6pLyqB0dPLD8YrBjrB3H0uuBvL6LXQs2pojuTlb5Kaz4ko20tRECzxFAHbfLAxX1LFxC66N6jTGjMp_fWn__ZY5UPDvSowpM-H0pfwBRxxNDTGH11e6ngQM4eYwmWi6XsUa5Hy3RU76hXfgCEqVI1dtqAWayfjE1hmgxQLo_LLNMFSvrn9cqWx0q-oX3Rp8z58eTzLnPVY-EBsm61DnTtRMV1QRCaWZTYNsAoAntLrxIo0QzrkCOq0tAGeWYrNWWEh7aXhYnbG1J7LbV_k9lq8_t6SonB32N3JxhA-LSEJcfrJ7hMygkTmk3ZozouQCQ2zK7IVldOnhwHPdj0NcE6tpAW16JF_Lkc2m1z-_z9mtlkkpY8TzZQm_mbx3Mh3gVjQzZA4URKcEsTY6ZDFY7O0MvwVS4Jlt6yLAY1uNl6y4r6gJmccUO3yn16_7X3mAyIEsM2u8gAwdSQWeQDHgofnYa5BYldV7VGO0nLzqoN3tOOI5zWrPs8exrwnFgrqb9sP0abxFkxD9ksUj8E5kEJZIfHxNyCGGm6SNWHinGXUCAUMASBPmCs4xKt3g7jtZEIfdz5GrJF-FbyjQFzNXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=oyDZZ20TErFXfTbqUTu9E-CRWTJEwEReeBrWvAhY5re-8oH09rTWHNSligb9Tjee1R6MCPs65zl_QnubHUihQKX6pLyqB0dPLD8YrBjrB3H0uuBvL6LXQs2pojuTlb5Kaz4ko20tRECzxFAHbfLAxX1LFxC66N6jTGjMp_fWn__ZY5UPDvSowpM-H0pfwBRxxNDTGH11e6ngQM4eYwmWi6XsUa5Hy3RU76hXfgCEqVI1dtqAWayfjE1hmgxQLo_LLNMFSvrn9cqWx0q-oX3Rp8z58eTzLnPVY-EBsm61DnTtRMV1QRCaWZTYNsAoAntLrxIo0QzrkCOq0tAGeWYrNWWEh7aXhYnbG1J7LbV_k9lq8_t6SonB32N3JxhA-LSEJcfrJ7hMygkTmk3ZozouQCQ2zK7IVldOnhwHPdj0NcE6tpAW16JF_Lkc2m1z-_z9mtlkkpY8TzZQm_mbx3Mh3gVjQzZA4URKcEsTY6ZDFY7O0MvwVS4Jlt6yLAY1uNl6y4r6gJmccUO3yn16_7X3mAyIEsM2u8gAwdSQWeQDHgofnYa5BYldV7VGO0nLzqoN3tOOI5zWrPs8exrwnFgrqb9sP0abxFkxD9ksUj8E5kEJZIfHxNyCGGm6SNWHinGXUCAUMASBPmCs4xKt3g7jtZEIfdz5GrJF-FbyjQFzNXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=IPd4sRXtfmUCBnRCP3ep80ImabzZeG2Q1GK1ymYA-Wj5Q4ffrpUFV3gkFS1wIe8GBaG2ShUUkz5p58oY6n3kuDRSb_Oc0I4Nz4jJtQxvSkQwx2tWLN4j8m9VHiTNYYFwBC42uh5ooCvS9Gb43gMvye5h7W-Asj-yyyoK0NFYCwf2SLHe5nFlvsTjUngtICpcnevoY7qxu0FMoi0TiI6_coNV6HjFfe7CtctrZK6pwZG_4nJq9I7r2JcKK9bnLbZozH7a8SN_ppckFLsy8gXs662RjaenMnqba3zVDTiUJVMVxoCAHf-k3mWrLTW2eHG8iT0wqQc35n7kNZ1CM8_s_4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=IPd4sRXtfmUCBnRCP3ep80ImabzZeG2Q1GK1ymYA-Wj5Q4ffrpUFV3gkFS1wIe8GBaG2ShUUkz5p58oY6n3kuDRSb_Oc0I4Nz4jJtQxvSkQwx2tWLN4j8m9VHiTNYYFwBC42uh5ooCvS9Gb43gMvye5h7W-Asj-yyyoK0NFYCwf2SLHe5nFlvsTjUngtICpcnevoY7qxu0FMoi0TiI6_coNV6HjFfe7CtctrZK6pwZG_4nJq9I7r2JcKK9bnLbZozH7a8SN_ppckFLsy8gXs662RjaenMnqba3zVDTiUJVMVxoCAHf-k3mWrLTW2eHG8iT0wqQc35n7kNZ1CM8_s_4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/suWp5nJFjH8BB1yudpf3cAQnxMZfVLqfrb5YTfBSwxhiBmid0ilnSblFEon6Lkg7VE5GSanttVeiZheCnINf56hpstSLAwZppxJNleGC0FYzT03R7tje_oMvtVaZVRIoui8PXaHCAT6CaeL8A4LXyYKh4KMQOExYbKQrxx3HsgQYJ8dtYpAEZ5ktbDX-SvfnHlV05w7RWMJCAs4xetBE7sPogxgwDHbYE4yNMZ1_IY86Q_a6nH6azY4gYCMl1XSdeuWAjnXTkEwn1kMunsIW7TU4tGLve70jMzQzJAPxS71oUaJQVEOw8Pq8dr_jIuYVCJJnFzVTaCoD9pEMtitjpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/deI0NLmitzOKEGm-IicyRh7DWHBusGwlLir4qD12_sLE-6cMstmCiTlSjuT23B2X9xTKyUoxfwpO4PLx66XXue4pO8YRsU8w7rnn6_Ep5JhFuXYbomkTKvzWVqsSsex2ysZPl2leuRYnFrMlq0ygncxZzEyevQolE4cLTH8vqkQjxKOTE5jIFaIabvkNRsaAc7j0IkQuWlcmh-Ib9pSvFJWC5gOA2msc6waXvdZA7cY3fM3zFJhnZJRnUTNrd6_1VVvEC-e0EnDT-BNfQGwFKpF6ykBGDLSGXxBjdaD0RLxV9RoLCIRa00PNneZunULxq4WCJLMlt2aPN8MtCVN_Qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJB6FfA3vLkmNLzGK4iKJpZHugEjGmnh5MuO4yYSkImS8ojKmPFHyrHoppqWWJbzhfscB9emD8dIEwnCn5cTAM9wdIMtotwpgFXa4JzXyTrYtnFMVF9rsHLnALQrpurmr44ZP7wdicDYHmuB3sb1G4CDQUPxd8A-zv1LFRo57ULLXwVxS_bxU6kNJbS-PGkjK0_1Z8c_A5apVjGu3k1wtW6dtzuzresERw7VHZ_NdbpxamqdVLrAoC4DTb3yaqjYpKRtykCyPtBT2wcgDSouIRdvwjO49dfumKc-GBdXlK_5ObdC_EdwMYGxdE-VoJTzU7Zy7rJX5_5Dna2pp2tZkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWdZIFuHnGIDMKlnZVpOm8WZyR67TMtrxjUqpOp_X88kfaWn2cS6kKyv4wa_6y74Be4nWbtshHNe9khozXszI6c-248jLdmcYBswr-AEc4RDuwfKRo9JWzvG7yyb3Jm2egAH7GalH11lFuDCV6YLu8HjANsTdbIeObCXIlMY06GQw6ThDYyIcEsBoRcWzvMw7sYQ2elp34vVGXBr0CwLNjtogSsjxpwarO2vB-op0EXmW5Gw8TNaZSyEA9T63oQ31t0N5uPgKXgNqfTlb7OsiZ938A2hx81SswuX8_GlNolmnq0V5U2gnlfmdm7Xlke_iqfeKWPjP_EBVTynPi5WKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVE46s7zaT4YzXvgbbCozTJIZ95KriZzpaWeXm1Dr9aTljaImSHjk1580kl5bEGkV9Eoac-sTn2l14XwjOfFcnFLk4K2LfZPX_uykwhS9k_9aePBTj8frYemU4wU9B42o4ChAkLxXYH1Uu4Ewz4CfYLoTaryaIR_rlxqdq4gyKNrnjdUNPsftDl56s_VLhhZYJ8F7jpRw_EPDQm2cvwgu60e0NQAcYiU4uf9s4IG8z7GNL1MstoNtD6qJZGRuima-Gi-uOO15c3HnZEe--jOG3TXdgQhAc823xFgCR_FDLZVU5nKkhjOx-4iewR11bD6YUdnLNp6XaMCO2HYrkKYCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=UmM7grfSpRY4MCGz2qG9syy9r-9CWo__ms-Y7CjPnUN-Mpp-rRxOcZY6Y9MtL30yEgQLRsigD4WcPC4y3aSoY59B_D1n1rtAhKkqtYBZgytx9L8EbvBaGurC03M3feLKRPTyA1WBcJu3tCgxRKO9Z9rgxUOhrAb6pfLRt9SJhaH-zp4dwhEDI1keYjK7KM9diZs_VxMblXSFZSa0C2Za2LMXXfh4uLCWlKmXe1Io51gxgh8KfNxRMPLNB8BFxDhTnM3ENrHLdBN3cgx_nKi9YfmetZ8f5dq_gyA7zuge6Wc4gNaKykFogE4UtW5RwRdNmtO64bYM75eL7x4aVibA7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=UmM7grfSpRY4MCGz2qG9syy9r-9CWo__ms-Y7CjPnUN-Mpp-rRxOcZY6Y9MtL30yEgQLRsigD4WcPC4y3aSoY59B_D1n1rtAhKkqtYBZgytx9L8EbvBaGurC03M3feLKRPTyA1WBcJu3tCgxRKO9Z9rgxUOhrAb6pfLRt9SJhaH-zp4dwhEDI1keYjK7KM9diZs_VxMblXSFZSa0C2Za2LMXXfh4uLCWlKmXe1Io51gxgh8KfNxRMPLNB8BFxDhTnM3ENrHLdBN3cgx_nKi9YfmetZ8f5dq_gyA7zuge6Wc4gNaKykFogE4UtW5RwRdNmtO64bYM75eL7x4aVibA7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omnnWQOY48_uiU-hfFfogupDX31qx4zpehrxHFl3QHJURbIdez5g14geS-KBHUWUoF-JiK2fJ4GaUAUVKW6AIi8XBcx3ESoGWAXM7g2h_DiMulEas5C2l5MD1IL9lCVcdduTsB62yKEYPaFgAvDRNp3Xxb0UsdlQfKrjs2AycKXrH8XKiIIeAC8y1A1JWaQ7Hwa-DtKTBahRoxiaZs8h6a0LjbfCnrIS_HCU0lUKc5TAafvjYIofNQyEuC-3TEfFVl56yLJMcGI9AN9GcOkcSIZkZUvMtE_PRhhLfJSWOggrq578uOgttgfCHTJyb0fDQJ5oJaZOx4TLO0rB5W2VPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kraFFWcgMRT0MHRV_eX73FVruDjhrPSSwJ9h4pX_N3KKGlQhs9oaISAS-39hJ4t25fi-Onneb-NDeuJlpMZFDgkBt7PrqxNgvCZ7psehYQBzSwGCiJnPxtvpzgbEVPJoNcbM6wOVXU_wLRMrzWStBoK-9Pln-gn5Kt7KNJpLHKZKswyYj58nrvhPCRmszMMMrzs6hgUkRuKB5vJ5xO4NPN6YvaFDJrFUtNlZLLLjLzVBHr9TPYaBJxkCRJnNXXRzeW5LUa81v2IrzC_LMwlfcTiAvSAUWhS1QmCKdks_ZbtGu0UwBown1HURExhkKcJcrblxEYP7GKPkczxgPyZTOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KALGl7T633kUDnBmQyiBXw5Tg53Qnl4SWezkWB7tEnn4gzVoShRvC1OeonlGiOUyKDsg28h5pmhciVMepUxB4EkUuHOqihpiCE80xl7Jp9vJFX74urpjstH4tl4SmZWRSthRhAo6TUx8OjlhAzZAcyYH_QM6rwFQaa2CxcrC9MWhAM1d7VhlTKufrpQrh7tAlq3NrP-zjGSmIkktYFeI4wV301d0GOH8KUT27BcftOGqVk9eS5_2-cbT6BR5eH1K0JqzzOvxeqOgTqV9udBQnFHIUO_OYlVaFFx4Ybh1TKkawt7XwReg1pD3JvoP_G0Jf6wzYqrhkxhuB9AYeVmpNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgP5fqC7t3lmq8dUmGKNQGL4jR7HSQiGMdLHnAYj9bWQlXNIVaKWsyMn1TTJsI9xLsB1RUJvRf8DrZtTfpyrCZaPt5IqZpDd41WwoAsBebYe3GA6AsooyMlOo80hEUfsBD4stZQrOdvixJl6bny9YwLi_zpkJXFKa6QpAj_qC5EiU-QQ4zHDkE1D-gsiMnqyg4EVn5-nMQqAQo3pFm2kPr00oJbWVfaKhIQkBPeZSpYQFbzAUjZ7jDfAnE9_Al1Ll-3up5pba0saHgOMJ-qLQBmSXMG80PfG-qjTuv-cAL1HmOvMNI4kW7CTgBKJrTR5GusKjPWTE08kk19197OY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTRwYnIyJnkLOej1S5JSYQIURSZyQJF3mXGRHfo5EfLCrt04sJLTpc-Pjrfj8Z79F774iy-WAtrOsNo8x8ekIiVoBYktzKtvACEEH0iMNxgelTdug59qxyLusEtYdQejd39M4S-3t-NS0Wg2MB2Yljyd_FSZsq9xhN7bCmFmyFYLUNUkaf6fVMkjjL_sqpqyXKB8usryGDb_qx1UjMUV3alma8DZdtquX9IUsFxPc2nEYtIa7C1hgxv3nne8K7J5G65fEgkZttTUAhUiLSiK97X-_e_q4QfiesQktnlHSgk5AP9-DW09ASZYaI-BVOn_Rhn72wsmbcNXPhNVjG4EhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KRocNEceopLTWphMtHty_fgyMedFffFd4rdHy6Obcip7JL7pmc2lw7eFFtQjd9UcEmVJg9cH_fn8I91OTyPvKNST858aqBTdhV48sxUjtifMcaylR4jVDIFZGQ3O8Qe-x9Go7D2xvcZDX8Rnwmm5qP0vSmBya0bdwxcAg2gyJ4CFHfjctMDrEqediNRHi6CHmOBoObUenejs2dNbuZeUs7W9Yxrv9fPvg79ZxFHIxuiuKaIwwpYACj1LlJDYnQPfU0WVsDAJB892XNBaeLLFKIR1Svm9KtXCEonSVxpiJhKkY-8AwVNk93K8a4yeOIALekdDOMhkiHdQJXetvDFJ8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزادار کودکان مینابه
عزادارن حکومتی!
میگه حکومت همونطور که در ۱۸ و ۱۹ دیماه «به حساب» مردم معترض رسید و دست به قتل عام زد،
باید دست به قتل عام معترضین توافق هم بزنه.
اینها هیچ وقت ایران رو دوست نداشتن
هیچ وقت ایران و مردم ایران و‌ کودکانش براشون مهم نبوده
اینها عاشقان جمهوری اسلامی هستن!
اگه برای کودکان میناب هم عزداری میکنن، چون میخوان یک کردیت به جمهوری اسلامی و سیاست‌هاش بدن.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhZEWvMWxRwDU4vl761bzpPyYFwO9rmwtiarzhhvHzx6wz1SELAZQ6TzzhZIenQz5LO1jKbcfsvG_yQ-6d_OHdgATlm2cbhIWPgobSpLTIG5SoiFzx4B3ITHf-ymP61WvKLyVnfkoq2kIX1yyA-WignRqubhxSxTtsBztDwp_65YA6cLjlj4FIVbH74fVB9r9wryB2NN6F7kNDRrFvvED6Sp4C1NcP6dIt8Rta0iiWwM9aVABvILB5aQJvCQ1JMmKYN5WmTDwZI9ZpAmTuPb0DPbiBLN-ppGxZKSxspUuHVATRhlquCKr4EQb4dv_YbSWH3XmZ16gDMuui8jjOfYZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgCdMZBeSKvGiQrKU5E3FByKlk1p8qjTqJd5wvT-PItjxhQeTcZMnISym7p1F1SUgVyXHKGYoRTeJ2iHXw2Jol35WdaWcSKcHwY1eV45Zp4C2Kk3FGLFIdUqJD5QSJN_cT5h2YF1mTLSBGBcr4S-E9AN6WyxBTz_rSi9hzNmdPsxIAYHmLyOmtKX2T_EUy6IpMKAvQptXGrK2EUl02j8MPD5-_ITWlIgKw-1kXueE6jBIV2b2sgsG1imK-MZ7oi7kpVwOBwbhvzhgt4sFgRv0TAWWXnJMl-fC5E_1RODTxrpP64t5q15vAEO7u4oI9ToSnmFeFUVL6L_tPQ7vBLtEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=Yzqi7VIRwcofLFrcCA9DIOT3PZ3n5eZLuCA-eWlZkPsFc_MLTgovfMLSIlGyHu-32GlLAaO9-iVuURX0LtZwi3dJneSiHBGkV9V4HnxKKvWpPN899JiIZWvKIy1U4ZNzg_9V0wB4ZCJRT9VfdfkFwCVcSHbsdR4DpwaS5KD0eHlrRvwJ9VSx6UMb-qekmd1Y78qa7QmjGSLE24kHiPW9VMAA_-fHYAWB0Z_td8dQL16hVFRKLdWFRXfEeez8Vkr7TWILvhfCk6XDI76Uhx7ul-4odlC1K_r6ueKCfBWxRgUN73bRg7cnKngNSLk9-E6JWhnM9m90HXyqIh5dqX9gIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=Yzqi7VIRwcofLFrcCA9DIOT3PZ3n5eZLuCA-eWlZkPsFc_MLTgovfMLSIlGyHu-32GlLAaO9-iVuURX0LtZwi3dJneSiHBGkV9V4HnxKKvWpPN899JiIZWvKIy1U4ZNzg_9V0wB4ZCJRT9VfdfkFwCVcSHbsdR4DpwaS5KD0eHlrRvwJ9VSx6UMb-qekmd1Y78qa7QmjGSLE24kHiPW9VMAA_-fHYAWB0Z_td8dQL16hVFRKLdWFRXfEeez8Vkr7TWILvhfCk6XDI76Uhx7ul-4odlC1K_r6ueKCfBWxRgUN73bRg7cnKngNSLk9-E6JWhnM9m90HXyqIh5dqX9gIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=oLptndih5t7dQhokgSC-xxIF02-M9nWE7rCoXoDDAvBP2EENUv8qPqfehxPof7HMAOF6rqdnPAtMPotMGPMtwyCEc6Oe1DEnORUK0fkqDAxIoU-dAzUOrGRcQhkQaDCRooWav-68Ac4Qoa2J0KbkN2Rm9md5KyCsIGYNZ5n2vKfsb58YJaeawrKBv6oDEhhHn4cQSjdn8LrJpKot89xXIxY4gREPDdgfF_QxiaX37yb5PyQuGUcviyGPj6ujgrgeusEBdqbvP4oOR1QBRQ30_bBlof3XoaXv-VOGOmQDHByLbzvK5vNMmjTA3FPWLnQB7PldO2WvyH_Oe7S8bxW4ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=oLptndih5t7dQhokgSC-xxIF02-M9nWE7rCoXoDDAvBP2EENUv8qPqfehxPof7HMAOF6rqdnPAtMPotMGPMtwyCEc6Oe1DEnORUK0fkqDAxIoU-dAzUOrGRcQhkQaDCRooWav-68Ac4Qoa2J0KbkN2Rm9md5KyCsIGYNZ5n2vKfsb58YJaeawrKBv6oDEhhHn4cQSjdn8LrJpKot89xXIxY4gREPDdgfF_QxiaX37yb5PyQuGUcviyGPj6ujgrgeusEBdqbvP4oOR1QBRQ30_bBlof3XoaXv-VOGOmQDHByLbzvK5vNMmjTA3FPWLnQB7PldO2WvyH_Oe7S8bxW4ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=GL9QhfWjDpXVcDMgkDabxT4MU-tZcJ_672pNbWTqcwdw1WYfqXX7EVmmJN_kMFDKOD8_PZ_CJOoGhsbWbk3xMZQRjxjGOyuo9iO6t1sWtPTtfP4H6QwTdoAr1y_vEYlI1Egb8PB0MNq3Av_UTViPJLKELJGrYWAZUJf6R8zyfnJdb_7Z8tXi7mjRp4Agau0K85MyzKytgFq0o1GkkBV66JwcIx3f4851yplGBxnmbspbTZRln5mOkyGKZc00TCPv65RSaEJ-P3-3V7FMExGrM8hvi6PtG3yeYqTi7veYCExJH5jLGVZvUbK14Ol5q0g7rC6UA9jA84bEYFT8Xbn0Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=GL9QhfWjDpXVcDMgkDabxT4MU-tZcJ_672pNbWTqcwdw1WYfqXX7EVmmJN_kMFDKOD8_PZ_CJOoGhsbWbk3xMZQRjxjGOyuo9iO6t1sWtPTtfP4H6QwTdoAr1y_vEYlI1Egb8PB0MNq3Av_UTViPJLKELJGrYWAZUJf6R8zyfnJdb_7Z8tXi7mjRp4Agau0K85MyzKytgFq0o1GkkBV66JwcIx3f4851yplGBxnmbspbTZRln5mOkyGKZc00TCPv65RSaEJ-P3-3V7FMExGrM8hvi6PtG3yeYqTi7veYCExJH5jLGVZvUbK14Ol5q0g7rC6UA9jA84bEYFT8Xbn0Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=fejX46jDla3Gvr9_0NFinfSxKflVGAfiFhc43WU5cJyv9l6xVufjoLJ2plUewLPibLs_HBJyBYbz6ppinhKYkZwtsi_Ym8tCnXV4X7pBTFbE0IR8JtuG8XbPF_zD0cqQ4O-hSlwVrLTsz_PBYkqX4tUX1nb5CXPcf6d-zYFKtDgcM5pKPYTGGMAs8IUupTIwj68vqlOFlCoGEFVomoFHpoLF1rkmxc6naUw4aVLIgCKan2a-iK1Of4RVjdrW0MrRoRgL_pwlQ_VPdPuINXrSUcYOZIvaoOwWR0nwHnZWKnxip0b7rZ6JiYQUiZOHFQIIv55kJeLbURw5TUD1nD35bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=fejX46jDla3Gvr9_0NFinfSxKflVGAfiFhc43WU5cJyv9l6xVufjoLJ2plUewLPibLs_HBJyBYbz6ppinhKYkZwtsi_Ym8tCnXV4X7pBTFbE0IR8JtuG8XbPF_zD0cqQ4O-hSlwVrLTsz_PBYkqX4tUX1nb5CXPcf6d-zYFKtDgcM5pKPYTGGMAs8IUupTIwj68vqlOFlCoGEFVomoFHpoLF1rkmxc6naUw4aVLIgCKan2a-iK1Of4RVjdrW0MrRoRgL_pwlQ_VPdPuINXrSUcYOZIvaoOwWR0nwHnZWKnxip0b7rZ6JiYQUiZOHFQIIv55kJeLbURw5TUD1nD35bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=LTXSJgNd6jlV9MOEfu4Sz1Jz666CekGtXP9oulKIdzgV2Hp4YhFDTXm4dk0bFk6dJzxOs7V9wCStbDIwsAizTJRSCLqRj4QRYVMnVQfK2vxdW3f0GMb2f9w9_R7tons8YDsWvemXQfW6BFCNNzYxtkRdYWztumkmRdcB00vlurmqniH1F2G5QfSvdEXbFG7zDqYOaGjYK6uvQBz7-KheTMcPrcsw9Si0W6VvhDnwIgqJW_qcEp40dSFIBGPkAzneQb5scgYnuoKNOw-80yYuap4mPgAkIFq1Kvs__HG1G1jPuZNhppuRnfjCDDC1XDHuRRB_0o1bxSU0bM5TC0d_fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=LTXSJgNd6jlV9MOEfu4Sz1Jz666CekGtXP9oulKIdzgV2Hp4YhFDTXm4dk0bFk6dJzxOs7V9wCStbDIwsAizTJRSCLqRj4QRYVMnVQfK2vxdW3f0GMb2f9w9_R7tons8YDsWvemXQfW6BFCNNzYxtkRdYWztumkmRdcB00vlurmqniH1F2G5QfSvdEXbFG7zDqYOaGjYK6uvQBz7-KheTMcPrcsw9Si0W6VvhDnwIgqJW_qcEp40dSFIBGPkAzneQb5scgYnuoKNOw-80yYuap4mPgAkIFq1Kvs__HG1G1jPuZNhppuRnfjCDDC1XDHuRRB_0o1bxSU0bM5TC0d_fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=hYdkOn0z9LBmzugyeCrsB84IKNkma_ere6TkFcweb95-0h9zqH5mCT3MKm4hJITK_lHHbylfyDe9bhUblXjF8VopQUALhyvdJvHyjJID6tvu4qbaDZbxHj6lLJmgqS_q5RhAMJCseP4hoO24KXJ8YnqaR--jhLbpDiAKsRDjiVOgI23Ef_5bt5mRhieMSIeFGX96ziD8JHg3SXI3d7TD6HfLroAyExL8tDd5G6Wr2ad6eXktFKZji-vU7CGOnE3-sHL_nujNva2Z-opSUrM6jrUKChY3FIuHH9ohILMjN1Vvdptyp0CozpnxpMhVg9NGzU9hXhZ7Ybo1bhrYgJjVkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=hYdkOn0z9LBmzugyeCrsB84IKNkma_ere6TkFcweb95-0h9zqH5mCT3MKm4hJITK_lHHbylfyDe9bhUblXjF8VopQUALhyvdJvHyjJID6tvu4qbaDZbxHj6lLJmgqS_q5RhAMJCseP4hoO24KXJ8YnqaR--jhLbpDiAKsRDjiVOgI23Ef_5bt5mRhieMSIeFGX96ziD8JHg3SXI3d7TD6HfLroAyExL8tDd5G6Wr2ad6eXktFKZji-vU7CGOnE3-sHL_nujNva2Z-opSUrM6jrUKChY3FIuHH9ohILMjN1Vvdptyp0CozpnxpMhVg9NGzU9hXhZ7Ybo1bhrYgJjVkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO916PdjKITByyTNT3dMEbrXEm0p1FPwNOPILazUhFb5dkaAtghopi982X7N8Wh8ElZEtAt4CxZyXSSftBnWvveK_U7E8oTEPouL-0wIthZltxd6CDG_N1TONtCPx_J7yau90ar0B0N5oTsH6vBPmmULslXWHJA01HpIxG4DZ5OMC1IB1ANOQsRNyXW5aNUSG_564GmxTm_34ydGSSp4H9ATvPglAtBXA9Y3RQCbnfJisYTW-DjbMWqB-0LT0TOo-MCgMT2RVlZNwGx312yl6hbuTgKIDLrK5hBwyImUXWEO89lXN8jqwxkwOp_fSKaEXfMB0dHG68p8mqtt2C-fh03cY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO916PdjKITByyTNT3dMEbrXEm0p1FPwNOPILazUhFb5dkaAtghopi982X7N8Wh8ElZEtAt4CxZyXSSftBnWvveK_U7E8oTEPouL-0wIthZltxd6CDG_N1TONtCPx_J7yau90ar0B0N5oTsH6vBPmmULslXWHJA01HpIxG4DZ5OMC1IB1ANOQsRNyXW5aNUSG_564GmxTm_34ydGSSp4H9ATvPglAtBXA9Y3RQCbnfJisYTW-DjbMWqB-0LT0TOo-MCgMT2RVlZNwGx312yl6hbuTgKIDLrK5hBwyImUXWEO89lXN8jqwxkwOp_fSKaEXfMB0dHG68p8mqtt2C-fh03cY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMJO8KwNZJ-lJLiviC3uR9wd5Ci-GGdh2gC2L3hNHqjIdAc1FL9Jq0MX0gYVb4gUWbMk1iWtAWgHCKlvOVS0YQvwGh-NmGhEzUmXgEKZaT-iIYq1ZfpsvAwo7IkVFW6I54I_OaxM1vi0l5GHnoJ6sak8T41W2gkstsOXGJs3QvEfCnVaHw-gidfgD-3IH6grF3g3Z9VLr9FdTiBzcRCqlS7b94bupvGwe-tEt1o-jSCr72ubG0XoeVBX-wBD7_n66HlzNQxt0JuqCHUhcWNHTrJ1KtJEsrlkMUEUSROkpiiFTDrubJYNWKDagf_eA1GsJTiDYY3TInYMf76Xb11GQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=GMtMfAbubPrPyJa2e--_hMTdjqXFIIKT5BUhyOcXTUt4GN2V3KD2SbnZE0tJKwRHoX106Re5SPURi5Durzq_6_v3m01gSr2Fg89G03EYgyT0cF0KyOIGmqKt3e35hjZ7WLvMPVpYMKzJlrTppcUqBjoqwRiq3L5CtyYaiivrpbldrbw86DsRmZTEN2x-4SZlLWfnZRHETpUAb6d0sUTqe_dugufxg8q6VehmLk-j4Kevd215-aL2tiA_5KyDpc7jsg8AxRlkWNAzaWSX8dK6S_SmC6JMHVfqrtWRFWHsEqs7GZbMF0qcqRZkAWVxQgYXvzGlGkcI7NrkumvqNOvz_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=GMtMfAbubPrPyJa2e--_hMTdjqXFIIKT5BUhyOcXTUt4GN2V3KD2SbnZE0tJKwRHoX106Re5SPURi5Durzq_6_v3m01gSr2Fg89G03EYgyT0cF0KyOIGmqKt3e35hjZ7WLvMPVpYMKzJlrTppcUqBjoqwRiq3L5CtyYaiivrpbldrbw86DsRmZTEN2x-4SZlLWfnZRHETpUAb6d0sUTqe_dugufxg8q6VehmLk-j4Kevd215-aL2tiA_5KyDpc7jsg8AxRlkWNAzaWSX8dK6S_SmC6JMHVfqrtWRFWHsEqs7GZbMF0qcqRZkAWVxQgYXvzGlGkcI7NrkumvqNOvz_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKKoJk90JRVEWvytRG5MEG_C2nFuFsOyKFoFy18YqHIlVnCSU2n4jxFqBKetv0NGIYcvoJ_b5zfDhRV8D1uVItjiSRnG1gP9jP54KBDYhIzAOnA3I47GzVnNbnBuJ0v6teTf00dy3TGiE4zTSZhkupud8NbmdtSfOEa9h1bXo6DBlDBx_xgFd64-WGJnPj8KpAYd6ht7p1I2cGMHSOP6UI8K13q2YR4aIqyhdo4M4kOhdzYIyE3NFZv7CiMEUUNNBRfnesunD7vvzj6E2FAxtwr2iWIWn6sSe7oAEl4TXYs5r_M1LcKp-4uPDwvIomFMdQxU9yqhKZj8jR3ZU3xE-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6ZqoytlYt61ML6Y4xZixH0dd8rn5I5XWHH1gY3jua8HIfMz3mAbeY23p7NJ8Tlb0bzNgFH_3za1r2ZU6uBVNIqpIB8h9G3NrOkjB7r90pIAu7Vf0MXezyqW_ZLuJiGKMKXuJOJhs9oAi23iCRRclzyvNjNKamRgsypswBEcZW7BZOYkeqw3LaydoDE8YL2qRevLXkJlfIRdH8lMPdx-xLjhDt-Awxn4jrrjDo8Y1AAHbFYOaihXN2S4M44__WXaYag2iTO8iheeTOxjExZpCiN4OFSWfAgoVUVGb0UH8f4gyHnmpdipTJI2Mh6OnokBh3S-zCqmBXUwkOj6Y2-qpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9D7k8VIynrTi3Ufov4x3kJKDTwdTvOgbhMYQPFa0_MFisj-Qbexltlmo0ISdLCk85W_OOrJmT-yfJ465hVZZyCzSR47RLHI9YK-74WS4_GpEUeuDS7UdcWyPYVg5anVjDantbycJSsgKRthZD6qOKsaEg4OpK2vML60ItTqUO0bYv6HLxiIgPWxicxDg-mKZrj_Gu4uzniZrclsdCFDGkQzaNBynS45NigYCKSUF8lC1GpZ6WoEFooPqCoZBk-qRPoucDz8-aR-NQH1YeqJBj7F9bnDz85lLL1vTA5FtfluM3GRYp-dyXKKKbZpW80lvWp4E1gm9TKe3vn0c5_tdg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=nl4hZi2cwlKuJvM960OddrspC457DHusPIuCVlMBYdEtZdHCYNPW5IBUaD4fEnKdOYqKhU3Qgj2sDPmomIfpdCtt94c74T_wKTUCk8dSnEOZK_dipIYGIHKVmUlW71_MR5ls3oIVG3xAogaWvdGh9CrTytvAsAqwLkdAJMxZUX-0FKqgM6wxdVjAurYitQXvP6xpH9GJbpYDe7cVrl_nzmSOoFn7qCSiASsGcDPiusYicI30M15beFMoCKJjuYSeGhJ5pAdwo0hQJ85WJbno9wYtQRNis-M7B0bQsNgIf93CpEl91w28EwQpBTY2KEhA4MkelezRP3dTmXCgo5NfkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=nl4hZi2cwlKuJvM960OddrspC457DHusPIuCVlMBYdEtZdHCYNPW5IBUaD4fEnKdOYqKhU3Qgj2sDPmomIfpdCtt94c74T_wKTUCk8dSnEOZK_dipIYGIHKVmUlW71_MR5ls3oIVG3xAogaWvdGh9CrTytvAsAqwLkdAJMxZUX-0FKqgM6wxdVjAurYitQXvP6xpH9GJbpYDe7cVrl_nzmSOoFn7qCSiASsGcDPiusYicI30M15beFMoCKJjuYSeGhJ5pAdwo0hQJ85WJbno9wYtQRNis-M7B0bQsNgIf93CpEl91w28EwQpBTY2KEhA4MkelezRP3dTmXCgo5NfkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRCsVndFmt5Gq8Rq2O91txBP5wegXUsDaF-8FkKuwI-Hxtx9orj7yuNXY-MO9iGoSbaGfQE0V_438hsvYbQ4wPXMpopAF3AxS17VD7xOn-FpyKA03D7VF5h5SzmdiKBwMs3uAUWHogA1jrynZ6xaPFiOQ_VNbgncUB4UoVl-voZut5WrHigFq0_jR9QcQXyOio4tmBlyw3KnxqkURsGFG5cmnltYQTz9NIs_ew8HVhF5Stv8bcR7YuRYvU0I7bT7l7Y5rRtk9ErzFr4VwvUhq0VRSDXKT-7s45TenrtNtosWWphXzA67R9l8_Gi_Y7H6R-Z68nn4eQeEmQLZyj1xrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KD0Ech16BGo1gHWOUJqP2p2aNe6oWIgjXFGD6oGLmEIwBQEsl_EchyLsb6QaFTDSmoQ-FUwUI2TVOYji3fDnuZydT7KwVu4S9yup894aPURK7RQfZEKxlcPLbR8jCIli5qID_JEPqPtO_1dWSUFv9Vrn8QSUY7XKviynmCbf2ViIU-1Lq6dJdaMtzGyvQ39Kgn1zCK18xRA1n44_PlD4QHIYX307qhIfBWqJLLFj_QlIOHOKxS3sFINd0JMMHs80MqWOb3OB_JyoVmmPWqOED3rBx6YVto1TH2DNPhHfkzQxaKXJJhSmfKsb8qXM-nqQwYLsk8-8n1HQ9IYIAVUO2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RL_BzDV4frC86pAiyHC7PFIvIcmVlIjkpQswBulNp9peMX0657VaW498zTyiiMxNzufD5ZiMI6V8K4nlRnff9slole813XSEI8wfMfbZANEqirM0xWufJKTMcRXFjtczNDSv0lFLgDFFiaEm_K5FAG5dxHDo-vWZa8Cr92su2ZHIEgqXY0OgUleiVTeVtTmO-EzZz1SOLXJv7cMzyfwTyDv-2kgIqxwUvGpi1f6m-cvjZkVj7AdStPkznlMP3Y83W3S3kOlkFqxpTKlM1NFVqbHFo4WjPzgZvs4dxFX-aMksMrjB3PjpU-SbGBZ-sWygxPn0dlWG7mrBMgFsKiC7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXLNmcnk6V9lZM-3lUeCVE0bq38dqkqG-WQBsDyM8ozWbUwcVIBdpMdNZ7ebSeJsKozfgWdjxaYy5oUyvQtlZdT6iFMcgtdMVk2pU5E8N0EdmxXxlQMcXy8J9hRUR2G1WpqVnIbBb5dxjrMU0x56C7Vsb3KBCAxuGVk3svcePIJ5nphJ30mYLPXU_JiRtvrfK9Nu7E7pzV2cHVWfeqBMFCZJwDuBYgXOBm_FK_AgfcVJIhBH9-e-KOgsf_-FCANehNPFRIpInLujFLHEW2FK5L-TfdwlBQteeH01TLd8kVIP--y9LGLwAxLjMelz5lmyn0MRGPDLzHe0_xVZLex5kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=CXmqc518N2cw7Djuv-ZWRVck7nLJBgTGkBNfpct7STR5HJuBgYHvT_dqAZMbq4RaKAID1JAK3FjkIgpt_buez1sjVpYHb-DkfbTWMpOmy0Ar0bPOvugu4_RM0g6T0OaZSeC46R-Mlux2XXo7OIo_BZ4djkq9OxiFfP7kN-RUuuwp3GG_phJvEsV-cZ9j8XgXUALpiV2C19174HEu1pvYFJAJhVc_gkTKLLdJQCiysfK-4dllKmM0Qf4LTcnzqOzL5qnJMftiSjopR5QJudw3qthdzazpKdMQplTJvAMNBdKRiKv7_05bFkK7xCpYPL-EDqplMDM7zEqzEWRTwZliwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=CXmqc518N2cw7Djuv-ZWRVck7nLJBgTGkBNfpct7STR5HJuBgYHvT_dqAZMbq4RaKAID1JAK3FjkIgpt_buez1sjVpYHb-DkfbTWMpOmy0Ar0bPOvugu4_RM0g6T0OaZSeC46R-Mlux2XXo7OIo_BZ4djkq9OxiFfP7kN-RUuuwp3GG_phJvEsV-cZ9j8XgXUALpiV2C19174HEu1pvYFJAJhVc_gkTKLLdJQCiysfK-4dllKmM0Qf4LTcnzqOzL5qnJMftiSjopR5QJudw3qthdzazpKdMQplTJvAMNBdKRiKv7_05bFkK7xCpYPL-EDqplMDM7zEqzEWRTwZliwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMuLpDIN5OUh0tywCdgy2V_dBet6fe8bD6ilXh9HgifPSY7djlMK9CZYj54Kuzrkz7N5U-nyT9qZQl3RyH-dW6FhXBXhtnofka7QgwjbF4q8yR2v4FuCWZr32JM4mSOd-oRErRlXPVvHHgAjSGjhQBUVz_u4nXZbgwhSmFnamaQ7tIMuV5uplKBU4vTDEg9JXBryJGOBd3LQnsjq5H9vSlszMD_MDfVaw0NOELSIxlvi7x5BeoY7_Esk9sCKLw-hmZduIG0iK8uo9GLJenggrX6_awCBZh1odS57Z4KWfc4Am2BzTlWb4RLVhgpeYHFateyqctOIeAny8Jep-4aZJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDAS7VZZ7KMCIQ3p4hTFjVRlSmm5IjXcbx4zHBYtm_8CwqSs8lBzKTv4Iywqq3fBc9EYnzbPls9-MOA48XdIxRKjQEtuzlxfr87dVtcEr5wVqKjL7amHdhtazZyB-sjugRn-iAA-HoyeFRf9xkHKpo02qIVOlgQGqHaTFnQ23Urc2i2iKLmivnOyzgipoeCsLjxGJ8QxRW2hUS8-9CMbTFjP7Val5PHICjtMB_35wjKmlPycYqpPfBiuXBVjHRLHVKe7Xh87XWTqVnvwUwtUHOj1oJbAVPvKszNeaijgcGWYN7mP3dhYXHX6MGcdnoStgRDKijePSN93lqNvgPjLbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=InCrXkjyAN7VJhM6muAzEKDAZjiNUFbLHrggI3_YUSbkGMn5W1PCHiAlXSP5YnZxS6sS5j1ld53TxMhFm4YiCDkYKF7C6avRF78esW0JQE_vol2cmOkjcO7cI7tkDJlqUqYkH3MexMyVUzK98lA8NXdIt179JGSUnZou6w5VJwHFzPfmjwh0x8dpv1-hWTfTjKNhhzNiilfPCbgdx1WMoI8Es8OhJ66bkJRIcV61hd1O5SAddyIz0lfJceesHfjWPsLW7gtJ2x_0qgOfn8S2iK1W2Pb__uTLr6NsF4VyLrWb7vWnZ3LM5a3rfTu_r9ljBpJf_Rjovo1MafcwuTDM763AgU5oM1zNYIWYxbEIdzvSCrwImzFQlFF0-yu7GPYKNVOMQQNPdC1z-YGdp9P1I3i9nLWa-sCDmsH3xF5SNp6_F3YFplvpuxcUF95kNWcmvbWwCOddgudDEpWuPul0SyRgOcZg9EjUR3XACVw8QNGDQhBlxDITlgka62MHe7TY2ULBb8x3cmgWAehwZcTz95-DjSrT-33VIGKH6HcvDe5ARHdJsYCUrhCZ6L_MCK1gydThMpzltdF2FJTrMufQOJWvdiziTVZc1iMLLuQpRyFVdpe35IMK-5nZuZDNo_wmuPU9nAwjLLLIXqazaEQ8IUySESro9-BvlqPzxcgr4WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=InCrXkjyAN7VJhM6muAzEKDAZjiNUFbLHrggI3_YUSbkGMn5W1PCHiAlXSP5YnZxS6sS5j1ld53TxMhFm4YiCDkYKF7C6avRF78esW0JQE_vol2cmOkjcO7cI7tkDJlqUqYkH3MexMyVUzK98lA8NXdIt179JGSUnZou6w5VJwHFzPfmjwh0x8dpv1-hWTfTjKNhhzNiilfPCbgdx1WMoI8Es8OhJ66bkJRIcV61hd1O5SAddyIz0lfJceesHfjWPsLW7gtJ2x_0qgOfn8S2iK1W2Pb__uTLr6NsF4VyLrWb7vWnZ3LM5a3rfTu_r9ljBpJf_Rjovo1MafcwuTDM763AgU5oM1zNYIWYxbEIdzvSCrwImzFQlFF0-yu7GPYKNVOMQQNPdC1z-YGdp9P1I3i9nLWa-sCDmsH3xF5SNp6_F3YFplvpuxcUF95kNWcmvbWwCOddgudDEpWuPul0SyRgOcZg9EjUR3XACVw8QNGDQhBlxDITlgka62MHe7TY2ULBb8x3cmgWAehwZcTz95-DjSrT-33VIGKH6HcvDe5ARHdJsYCUrhCZ6L_MCK1gydThMpzltdF2FJTrMufQOJWvdiziTVZc1iMLLuQpRyFVdpe35IMK-5nZuZDNo_wmuPU9nAwjLLLIXqazaEQ8IUySESro9-BvlqPzxcgr4WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=eQo_7qSRS3V8ZcQ-OnoBuOmI6_AzNSByAq6QQbptdhlNPlCZQhnsGg1aGs8seWpAXMQ4SIrrxYOK86cYw8tBmEla3qc2sJKb_gbMwmsWSU7SBU9Ty2YZtPKAqbN3mpByQx92z1TUOi24lDoQxciaOD5a8dzRd6-BuZG05T5P6QWE-uHQaRmesrhcsRvXnkB547tgLq_sddH_-TANQW0NGjqlX_35nMdwqYOw6Kiuco8SLrjpqowLpEKYf4swvFKBi48Z-9nF_aPgm0GyGSFecsCiwzmXDRxTiceUAAzNdSIu8d_PP4PI8EP_4RI8FJURTfguK0X4UHKZrwD9AhBT4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=eQo_7qSRS3V8ZcQ-OnoBuOmI6_AzNSByAq6QQbptdhlNPlCZQhnsGg1aGs8seWpAXMQ4SIrrxYOK86cYw8tBmEla3qc2sJKb_gbMwmsWSU7SBU9Ty2YZtPKAqbN3mpByQx92z1TUOi24lDoQxciaOD5a8dzRd6-BuZG05T5P6QWE-uHQaRmesrhcsRvXnkB547tgLq_sddH_-TANQW0NGjqlX_35nMdwqYOw6Kiuco8SLrjpqowLpEKYf4swvFKBi48Z-9nF_aPgm0GyGSFecsCiwzmXDRxTiceUAAzNdSIu8d_PP4PI8EP_4RI8FJURTfguK0X4UHKZrwD9AhBT4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odY5ntgo_yMbZ1ZLsMFcEYl5Kz8ZM_dTLMnPESmXlrV5tv4aQMEXGhcRepfS66ZsMYMPeF5O8VAk6xP0dralltQ__GAriDI8gnHPMIbQ071ABsUnrvvEIc0WTqo-HTC0v2KuOlFv7Ttlw9qMHqxRz9TkauTTnNrFs7vTuvLYe7HOi3BjxZENgDPAlJ6kUV8JMGhoZpEXLu97y1_QYICiELb-usuiIM8dW7hNxfWhCVK0LPIhKOnAlubafT3KYoVaRh57KeXDpm0LJ_XFTjA0R-dW1HeClZLcGV-J7dZHNHWks3KnOKC6sRg-jT1LKA8URZ5s4ZZEblZYipRiPHMAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=H6SNBcJ8PlUS3gnQSqyCrCHJhA5Z2-HsIVWBvR1u6BzmYrP2Tg7AkaxHLoC4zLG4V_P_h6RXHh8eUlbi-AjlWZXGfRNTbKMEr2PLrNMvDIqbiuFdEwbPmoD7pPJxjlnnNDIePmetJnkCG8eGdb1CZEcC5pVDREnPwgGD8lD6xTszoAKCSwl0SP7xRykzdkT1uKovT-WC45UCRMLDR3oZS4KRz4XhqkOtN3sS0HR2pTedx3JAh22hwgMR6nh7PUPjHl-Nop9IvainFYJfRDmmW6V0eXIr3cHsCjMnpqxYYy9y9Ij5rz9hFiEyJWHO4943TDFE-npAES6loiXqpJ0VNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=H6SNBcJ8PlUS3gnQSqyCrCHJhA5Z2-HsIVWBvR1u6BzmYrP2Tg7AkaxHLoC4zLG4V_P_h6RXHh8eUlbi-AjlWZXGfRNTbKMEr2PLrNMvDIqbiuFdEwbPmoD7pPJxjlnnNDIePmetJnkCG8eGdb1CZEcC5pVDREnPwgGD8lD6xTszoAKCSwl0SP7xRykzdkT1uKovT-WC45UCRMLDR3oZS4KRz4XhqkOtN3sS0HR2pTedx3JAh22hwgMR6nh7PUPjHl-Nop9IvainFYJfRDmmW6V0eXIr3cHsCjMnpqxYYy9y9Ij5rz9hFiEyJWHO4943TDFE-npAES6loiXqpJ0VNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTsi38Q-XS4qdckY9nIQ2TbIdVBOA9Dxxurx2-UV83Nb1GBhOQRIXYrFCjWQP0nano2f8VDt048gcuaGeOm1tTfnDw96tVMEF5QeVLQETKWWvvxDZEge8BtjDpMIHSJQNx7QMamXMFsLniJQB05R_YHzw5FLOcemNcO2Zmihi3WeeWmHVEiCAW6bHKQ1yiWD-xFiU63i_UZ95x8PUR5xArBF6HJ_qXJO07uRIugeMg2vkSNxCCN74YF4FNpNPnfCUqZVJ9lIp8cb6oDEUKJMJ9ZnT4HB32aviKY4jpETCB7qBwpxguFl-8voeuTyHH_LOeh-IBBgkf20PU8onBXoKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=IMsZJmRSxASNzdq1NN7Z_3Zo7CgKysfYySptw28EKm9uRa9wk-aBOUh0rRhVSDq_Eljr2nBF-HAa9udfAja4hE5iRZRTLQvJZmJysqXTbcJoo9dzSyIwu_QoE2idNjL2Bnf0ok9a2P48k-M8EmDr1XF_O0QbeR552tkFefeYddqpvn4sppBkH7hFHgET20O7Bh8PYDmpEN45hqg76DQlfP9XSJtQonklZTSgze8pi2fJ0RLAdY7ITlCWZWw0BF04XdhfjoqWDYZj9ctObl0GIYQOo0jaAaf72WNNB4sfq9vKJhTOj1PGcpDssXHjiQ2H_GgJ-4fOlB2565HBPHFCnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=IMsZJmRSxASNzdq1NN7Z_3Zo7CgKysfYySptw28EKm9uRa9wk-aBOUh0rRhVSDq_Eljr2nBF-HAa9udfAja4hE5iRZRTLQvJZmJysqXTbcJoo9dzSyIwu_QoE2idNjL2Bnf0ok9a2P48k-M8EmDr1XF_O0QbeR552tkFefeYddqpvn4sppBkH7hFHgET20O7Bh8PYDmpEN45hqg76DQlfP9XSJtQonklZTSgze8pi2fJ0RLAdY7ITlCWZWw0BF04XdhfjoqWDYZj9ctObl0GIYQOo0jaAaf72WNNB4sfq9vKJhTOj1PGcpDssXHjiQ2H_GgJ-4fOlB2565HBPHFCnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
