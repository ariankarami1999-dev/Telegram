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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 09:01:53</div>
<hr>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NR8JAIJzL-MkFoIp9N3X5I0_fFWOsDA_KZ2LYCRXp9cXrXI7an33UOdVHEwsxxgKBH3B0nbnSvZX7uCZkW19xSnyJXlawqi1uBvHyr4FWXvDgaL960otiBzG0jr46ih1I3iADWVDK5XdGMlWaRXn1I9-M4xwpap9F4jbIfwCl82NSbtKfOLyI4VjjPzwA4yXT1P57x84QiQkqUIFgXB8gr_sG7wT3kQC6xgwe4hRiN3yCBC4tTcGh5yboiTRgxyFFEPUCt2aypiwkTyig1CqlAs8weh-PMHsfAheQ_-vqy93mqPinViKts0nZzijk3xGAcAthPX24Aqnp12KciyymQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 937 · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aECkuhEdwBJ5-V8aB9IruK8z4kJjmNi0Rt90cJopx_Sbe3HSIgjsnxhsMl6_OO7yQb7jIlFp5O1-n96OYPluHTQpiCJFNXqNZM_F0MiqsR_fKAaFRoylxbYplmUnVRFdyx3RYj3RlmaXjLIT2xBhWAsxErCdED5dGjsbbnOS-xUTsIAz6BYj4qWL81clGrGx4AqKgfUZUTbwELYeLqRym3kZLbZnw9ivRqU7b-H_x3A4gyXcqT9ucFP5UG44i3by-49b-sIpfRTS0ihgD645LHkKjVsFu9WwIxa8FOd6CHQ7y1H8yjY-XTar3keaz5KWO1dzPOuIYnrvtbSbYP11yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpM-RZ5JdQKGve3K5rgAZ-UJxoBkPBBHGtjSa93Mj1mK7_IRaTREVtZ1wfdJu1BMdp9dkoWji_x8RGL1pXiwSmyBS6ijjMOy0y0OsfkqGyc-G0O72jQyu2uolzLzCIfzeWRIFQiuIp3WdE-auPm20OM7uRUSBLSl8Lunlj3807mgU7iMdwVcUgFVKy5Ua-hARJtaoibGLgzZbkXU5err3_WZs7OW9CWri3bPH9KYpjZ4dt6Is1fvp3gTigvo5_E4pOu07I10mhKel7NNo8We8RzLGz4ixXdaQGY6e8yL_kVThGBwrqGA1_keHDsmsXfuMLm2KD70yuQiPTcetPsWSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=bioQav7JfjRE6SnxCODbpUoiens90aIeoHQefoi-jTOC6hZ8cQXGFADElz_qlLKJsf_ffFsk5D_Zix1SNJV2t9bBds2DwVtfsGY1XiS8XhNm0lsEjXMJw6ZTD8E7kGLMfnfIhV4slyyzszU8EZis7Ipou0C-yt4CurukKKk6fsLUAgMH18ultG3YMVYYlh5o-iL3OsAsOwYUHTSRanDJ-l6zaVR8kARTPDCTLaSCjLv3cLjoIJ9GD23bGpXAchhxFU4Gvpqbj6FaaqlWVTlxkczWubTl5atYdYoMVQLaeJYZIklyMk50EoPhnVhpymfmNMRhBlWPuuLX6djGO3vVjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=bioQav7JfjRE6SnxCODbpUoiens90aIeoHQefoi-jTOC6hZ8cQXGFADElz_qlLKJsf_ffFsk5D_Zix1SNJV2t9bBds2DwVtfsGY1XiS8XhNm0lsEjXMJw6ZTD8E7kGLMfnfIhV4slyyzszU8EZis7Ipou0C-yt4CurukKKk6fsLUAgMH18ultG3YMVYYlh5o-iL3OsAsOwYUHTSRanDJ-l6zaVR8kARTPDCTLaSCjLv3cLjoIJ9GD23bGpXAchhxFU4Gvpqbj6FaaqlWVTlxkczWubTl5atYdYoMVQLaeJYZIklyMk50EoPhnVhpymfmNMRhBlWPuuLX6djGO3vVjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyhagpcupVXjPk-nJKEJJ8eFP3HRp43PmbI7G265Q-OYFtT-KJAkqFZxy8bLm0kGY1zpdikpz3uUozvfH43cbsXwqJb4OcZ2ls3Xs__1fqMYcgaV5uQyLe0kuQAQy3b_KI9c7eZdrNx1w-jjpwwMUmgPh9wyCMB7xkDrQmQFQ7gJkt_HF4p9LJ03uPXAD1_-nlwdc_r-OJmoqMjlZMB9CH21NfJMdHq2RhQlfE3ITXxJzHX-PvPKLdjMaTWmW5Q_GlACaO9DqAtALNT4ue38sOX0HQYQVODwG0EdWd10BPHT48-eSuV0tLO65YayiUq6hv0TzFTBjbvPi-GZKCf1HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDPUKyHHYioBeobAF_FBiqwj6fS_xju6xNXDRSUfat3VzjDKtZDxp2j-OtGRpwWrCRsld6WQUnb52VHNswBTVWoZ6HYMV8RQ79FQpjDNvgO4mIjyXYxfkRzy_Td4w7VUV9Crw-8ipAax0xpW5b045XmgL0AqAxkNX9tYlMG13w12gZzpMHrM3FQ1MGedrC7jJTinKv8L50sznVG7MkGaDwYG4QlMjkQJ41xsnkH0rG7omFdFjnxqhm7dGoZJCfh8oVuvY2cqYPL1PaUAGHabv19BuYgubVN-pOq_TLy3rRa3iTPMMNtI89nk6rCtwnNe7iafuLDjLNus0Xbw6hSyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlfjZ2qS5jxiyZJCCxgt5bB0_ck_sqbgIrutNbja16zqHV9n3YzMvzRzd0-2UXKTQj2mRk_jSrRuuCBqvqye2VwbFLuUa1OqySqJsjFO8sg-d-NwpctguF53B09j5Sl4jadZAqL5pDlpu11Asjqw9C24y17waGVZ3701u9ZPqWThjrWStu8GYkKqP_RD1BUlisZ8j5l9CL6X_1c489ox8A5ggQ3v02JvWESg203iJt5rMKyeph4-vvCoScnGAbG43o9YNJDjHb6fqQBSbWMW6x4U4Uy6SNWfL_jWOFvTNWbWMCtg_QCqSjcd2vESk2NDWEDb5-LefSONCflHcmi-8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTEk4MXhVeOCfJT25zVOSb3akt6E-A5ggvxcUVy3l8D82fxW4tyemyNSaRu2NSs9iWQwaoG8L8kfQbbXNvNgN0V9gDmUAcBc3_-ZP-LKJwW28xTuCXNpDuNCdb0_u1ji62kaUhdsKYHy7FAFgVxDIN4hxuf4XMzkMruvwtY2ti9Qq7ixR9SmwBuvdDevATAOkVpJ8RSpEKR86PhJtZX3SGPdmLlNbpWJubCBl-vySgBweZOg3Ec6GpbtPvuf_2gQ4JrKdhs5VJ8zAmR5HK-AnjGJzlDSRi13VXeZScRs6oX8Jh9iMlmYM_znIKjI0eOjEingt6puFKR3PG5z3HMr_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=ePz2f6mB0tWSHI8tSVnRC05_fHUcb7IardiF9_EF3SDv12bYHw5c-BouABh0CQA05LdFuUulv6XMSFAvYVMbiso9_zP2JIlf4hXNOBz1wktJiTyqYMbr1YF6jXBV3PkZbcN8352jTcM6g_fY4Vw0p8lKpk0cWxi5c8S67TfdG3hCtNPADWhwm2zLgv4EU2rLTzugSktyeW7gTiYZZXp05qWXruPry8te9NvnRXoc2GqO-Z7C70GwzSyIdg4s78q3xf13CmYzs_oPA9MZBps2X9PLLHSyUzwAJf4Hz2AyyIjY6UOIsy6nQ_zJvZ83WOa-sf6Li1HLqaaZmPAVB-VgYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=ePz2f6mB0tWSHI8tSVnRC05_fHUcb7IardiF9_EF3SDv12bYHw5c-BouABh0CQA05LdFuUulv6XMSFAvYVMbiso9_zP2JIlf4hXNOBz1wktJiTyqYMbr1YF6jXBV3PkZbcN8352jTcM6g_fY4Vw0p8lKpk0cWxi5c8S67TfdG3hCtNPADWhwm2zLgv4EU2rLTzugSktyeW7gTiYZZXp05qWXruPry8te9NvnRXoc2GqO-Z7C70GwzSyIdg4s78q3xf13CmYzs_oPA9MZBps2X9PLLHSyUzwAJf4Hz2AyyIjY6UOIsy6nQ_zJvZ83WOa-sf6Li1HLqaaZmPAVB-VgYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=Rl0RuRJXE7W3Q9nXjZgIs8sOEwF67_EuWt188Qw-nY01D7N6xzW95e70ht9H8DHqfuyECte2tBtKIB9XtFkkHjlrdO-sPlYxvNzhYpqjBjSz_6nwhMnS8pDCC7qRBOivrvLSoRGTH26E78pze217D8fACgLrJ9hCe11xPPLQfx36cih5SsWrXJmdSWmo7kKbVp5qbzc2AKCwPbNdGVBa-3yGJ15B0OMbSrRsTVojaqGrUyAWTCW6tt3hQN3gomNxhpieQVZueN8dyaENu-ifU3__rxSA80ZZujspGJu1IFW6IQtbKtzm-JTQolj2WXLmhhPluZHcaDhow2AiCccVNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=Rl0RuRJXE7W3Q9nXjZgIs8sOEwF67_EuWt188Qw-nY01D7N6xzW95e70ht9H8DHqfuyECte2tBtKIB9XtFkkHjlrdO-sPlYxvNzhYpqjBjSz_6nwhMnS8pDCC7qRBOivrvLSoRGTH26E78pze217D8fACgLrJ9hCe11xPPLQfx36cih5SsWrXJmdSWmo7kKbVp5qbzc2AKCwPbNdGVBa-3yGJ15B0OMbSrRsTVojaqGrUyAWTCW6tt3hQN3gomNxhpieQVZueN8dyaENu-ifU3__rxSA80ZZujspGJu1IFW6IQtbKtzm-JTQolj2WXLmhhPluZHcaDhow2AiCccVNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJK05cAkntmuny8k1UrIoCbtyi3jxItNa74GXpG2Y2l7GMn_-9Jgo6zSYH9VX1FVNdG24-fd_HRsztvnkL_g2taKR7QqmD2aSgZ0IcfNSbp4tYhQbDiiuK2swnEk9UNGaEbN1t_RnRjlWt0pPvN429VnYLvpuIwobSBloiom8teOYk8i9bRwgSzumMLXiVVi823KOKLp8Hx9cTBcSyD2L6YOyDA9IfhE-FR1wP7_l_wfkyIA0U_eSQ_xgta8W0CBGKFyqhMHmnU9fn7LmxWnDDWDUjjPotSkGw2Wd85qFaapM42IWuIBY9XPeBsxNhohigE2wA6hMHwUU_tsMQyEqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWH2IUPzfC9pmW2RPeiyfXhZ8EFrnH69DE6xYz8-wgt7PgjG2jnWYaqnA4AQ2LhyAwKDBNoiiTvAeo96dlVYcyXV_ZdtRj6o5Wu_NnYi8_LoJQtWGDqxNEyiccGo9kqWbhChL4sQlNdNKZep7NMbUr9SwJ7qsoJPOv7H4WOEzoZutfu2CsUvM_TDNO9i8HE0i_B33zD2A2fsBhZ1iHRL5adpLPGmDHQdM4oQDrHggGi8zwrL_HhUUxRrPeCSzOc29DGIsyNgtew1YmoMJKrjKGMQ_mhsqWoJJ3aDLB9iA6n_sbXwxs_9JuUXYYOYHa1nCMY4gZ_UzXXuZkEibDIcYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7PALIB_T8wTNEWY7Bqiq6fnxtYQY1WZOXYhniP6d3WzZERP88ggWJOq2OXAHR6MgOlrxNTTCg2hTkijCSbc0_RzeatM5xN5AyKsKLyrWKaEFc-iawrhog02N3CqIPPwQyv86FxRYQ08yRu2CzvG-VgIPWD26s7EKuYqJHcV47o3Xf6GwFVeFCNAwNp8Zwru6gkztmccKN6Gkx-doHzYfCDRRb2z-_yiIkig0MGHcO6R52Y-R5UTpaZfxykbVVZedA9gflq40KTSgD4_gzzzzWUiC0tbFowlU3JJjpv_eqQCp9dfpPyXcDeS6vjGcUBaAIpGLFdwPj3JuyQuaFzvoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k06PwN4sOu3dqWpsN7iOaXPW8RAICzYy6mKUTUdAtKMYZVZEZ5vdBEiVfE-6Kakxphm3_bRUTQiZgC2dASJltWYsdgizlpRgK1Vd7uuypKFqRUoeY7G0uDeMan0qwvZCLG6k_4gt2zSVtB1y0WNrDTB0CTF8oLbpsJEC_-AYU9IvYMcB6nDth6-ptUeQy7cff13p9UPfSMkjhg_XHl9HNQ2t-cykL4s55gEM7Jmfu3Lq-vtwkSGlqOMjM3LQSlCXGF5wC6BMP5ASFFLbVTbUlwKoMXU1o4PxxZNnzYnMRJLCBcjYJI-lzu2VzgcBEmw5-3NQShAyey8n_zjPlMqx5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmqGkwrYSPe_DzaTtj4uKHk9hVFAuB1VWqZhV0isMTyiN_nGjZ990J-Ylw5xln25bNqKIa1M4j-ggJ9agXf-d6BXXU7wJFi_djb331dI69xljIR6iMrXnI8gTwtAT7ZitMTN1TMTV9MesCUW1j8rFHtqyub0HbxaFP-64A4j0IhzA0jSu00VvUh3j02k4ZaJ1mtfMxvKh2WwlTKkDsVLDTpqgMEV3GBbnpH0vTWfYwcZXJYqxIzB3oe-Gs6wIlGPEH3FznqaznIn-roAgehV3ftP7cOvQJ3rCm9tygRZqnoT9SkCVuIEQn5r_fltktxG6D0QczAbbu1nWC0scCBVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=EI0IrubheU1ZPJeWhv6jNlJgW-FwwyQL5cal43ATgU2FTps2OeIiocu9Q-Hlml5u08j0VPHMag5uJB-A-9P8n1-alrYjI9KMuo5L3nYxFxtCIPKHQWEiKKIL--Wa4KfWUUwYi8uU1vHeHQBa37miX9ytL8XQ8X0kd-bXe8gkQumwLYy3l8nQKI8B1MTNvpetTImqTmkP7eUICH7107VE8ZCzynb8kdE3losDz1ippGGq1iA41oUngQzCS6jZLChrc4dJkP5OBZCWexOZ16vpcfatvSVZPVb1XiZwh4tRLZj6hosczbqNZyvHMR_gUdGfINdrMhhzLkK8gNctVLWz3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=EI0IrubheU1ZPJeWhv6jNlJgW-FwwyQL5cal43ATgU2FTps2OeIiocu9Q-Hlml5u08j0VPHMag5uJB-A-9P8n1-alrYjI9KMuo5L3nYxFxtCIPKHQWEiKKIL--Wa4KfWUUwYi8uU1vHeHQBa37miX9ytL8XQ8X0kd-bXe8gkQumwLYy3l8nQKI8B1MTNvpetTImqTmkP7eUICH7107VE8ZCzynb8kdE3losDz1ippGGq1iA41oUngQzCS6jZLChrc4dJkP5OBZCWexOZ16vpcfatvSVZPVb1XiZwh4tRLZj6hosczbqNZyvHMR_gUdGfINdrMhhzLkK8gNctVLWz3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftaNFVCNwKmyiLn-g3NlPLYWbQ1dQaZ_PFDvr0uq9gesHSfulSb_tBMgkWpco9Lw5IRZA4wb5kDfOda5XOu9dp0dilYdPHdxmOsQBborope24-L20TxcgS8Zxl1DwHoN2VmNoSypmIWYPW8MMxV1Fc-07z3ToO3GT43kAoiI59HGO-a2CVoBrZxzc-8s4-GnOEPOB6Kw-REyAGgWRQBS9ljf9rwb4vS5zpzNK4k0AKQxECpdyCahsKP_SVyg1zlI-mMSDmx9pfdqKvyBr_5Zvo4vtHewllAPlac2KCyI4Aq90QUNwvyZRoO-p_RbESNzEHfjnESu0ZqcDow9adDjhnBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftaNFVCNwKmyiLn-g3NlPLYWbQ1dQaZ_PFDvr0uq9gesHSfulSb_tBMgkWpco9Lw5IRZA4wb5kDfOda5XOu9dp0dilYdPHdxmOsQBborope24-L20TxcgS8Zxl1DwHoN2VmNoSypmIWYPW8MMxV1Fc-07z3ToO3GT43kAoiI59HGO-a2CVoBrZxzc-8s4-GnOEPOB6Kw-REyAGgWRQBS9ljf9rwb4vS5zpzNK4k0AKQxECpdyCahsKP_SVyg1zlI-mMSDmx9pfdqKvyBr_5Zvo4vtHewllAPlac2KCyI4Aq90QUNwvyZRoO-p_RbESNzEHfjnESu0ZqcDow9adDjhnBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GR2WRjMLOA4qkF0E1ErrVsV3D9FwPiWDjiFErXEyJ4mR4X8jDyDXDH_1DohZ_AhaCn82o14qOEUwKTaLNchqYXCKnq15t-SoOSByop_yE09qpyRZRDT2esxnLeFnjXk7Obl6Ge-uX591AAZYZyiluRBv_4u3JWzvt2dGaCA7IVOAJA_YotwEsjzsffNu9ZS9notmZmq3RFMFvoQBw9xO5akneWbL46hB6AEoL8WtDXccZvXE8ztcRP9ldyvElhtjBRMT55a3d081QjhIaoCTDu2TMsy0Cie7UImO20T4ShsLJSGArsf6jKaMbXrQ7rq9A2XOHL78LAd-olpQjSzBQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb9sC5cDPI5uXxA4fih-UocnfZo6hPSidWdQ5tpfltvVIi_x29WTEZT6lNxXZb7ePVenjB-OOHkidAcgR7Wnjjp63KrG83IWixxvXraOypysHEcf9HVBUUUYT9puMnQ-Bovs5iRCuxlFWQoJatNy51fIOoBti5hOJowwI4gVvPWPqCTQzn64kZL0M9uxwS2bQ1pCKoyvfCLN_aX8bfQJ2vKjyE3z03gsRlVrqnbi77MV4Y5Nm1ZzDr2-ShqEmdTe3GMKHep5aW_KVB93dGH6hjUCg8jmd49m-keEh8XG5-Ralcnenwv6fSOKxmLypqwuWGcOrVQDTAvO0IEUBVlosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gyiHFowRHqHI1fgP57VxXWY3rO6672BAk9ePX-I4-mzzdiBCwDzQxwhJbfEdRu1ed7rdtSs5nMdeM8UtY3eUEPJNXPuOvq93BSZj61u61MF7Obfd-KB_lrlf2wO5sj7vvypPQJplXNeTST_ouZYQ-A8orIChj2ic3Rb1nacBwv0Zejb_HGLo5w-vjZsGECfku8sTPHXuO058f3rlPmdWPh4QGe_hHCAZSAfatW8AvigAAdAIFJFmVIV_q4bbzYfPYqiw0863rVxIW_7nm0xoM7rAD9l6uuv1hgz43aEN0W6G0typ3ouKYxcznBKaG66kuuPgA7LCKTETZQSiZ5gHMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvFTRxKbXrE2Mt0NzmYcw7FmLud3jYLZAd-jkZQRNKMTf63zbdVz0YdbwXTeACZUgC9HtKeZKNNdvrfoV5dVAxUpjBAqDjgAyKUFRUsM3VzymPBr2USV8zzOFhX7icrZlDqinAS5WK3MeyuxYkZlQsS7wpDXW89qccrgsiLsWg9T8JJxQMem8mZEdKFHHJx3Ffndk4hCqs0-8Gt3ToyvnRbHSw8GKGRmBjrEiIJCgbI8qZAu6NjrQTECZZzc79wP5wMSEjvfEWZ-nCY8-6G4muG1vNxGOSDw-WSNclbT_ttebez5y2boB5dBww5lAqLCd3el388CzPkjNCq8B7N5pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECud2s4rXeiphuLyqptAIsF0LR_C1QwDXOp0FiXnDvOVWp9bpkYrsk7QNPDUmOaZuUsAwaI-12Gp6FTBOGc8OWNCm94MYYHEFbN1w04VpzybzwAzr52BT5-IsPPlGWgjnYqmudQzFERVQ1jJnS4-SMI67DvHBDLUa4q-cRqE4vsVExQCZ64LwCSLEVwk7OGj4i2ARiHdMPaP7rHzavS7bhrETG_ilF3BUpmhNYYWpanNiDQFpt1rBuTZechg29Rsc_bGlW7KasLfygLVo1uiNTVfeAS7rxWdlOKOe9hbBFmYWRc7peMhZLZGSZ7emHEMOdUKvmKKdGHEmx77dnwgLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AB7gSGf_lyQs10I0oMisnqVl_1kVFct7qY7pi5jPOsYCaNeUmy2oPv_QYxhoeIfhu_VyMBHZSGcrKDF8gPw5e50c9jYbSGN34jvicrA9RKO5EfJaqsyX2fCLoQO_lnOaBJA6aKdFA0pLq7Mk9-7EttnA_aeois6Elp664LAUbxzc4c_N_MADny86vVC1NXOFxiGBI9lNKtNK9k9ErU5l9gGc-SsAyJmd5381nL75T4EDQ9JLVBUwbDx0N8NMWX4mAdv87I2-ODFFmfHKdXozbxkXWLvbRfmw0b-r64fAdZDYchAE5VUFgqAlN7Mwo32BhWqWAaheDRL-DGj8bjNXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=PyQNJ6L2YJ6fdsNybt6_2ZSg00RBs5m_7lybo4Qx4j-3mQQIP3Uce3kDpFAnEU_5LfeNalJfpoMRbMQoBh2I49qqOPc1PVO5qkAmHiUNMdwY90R0ju_V59YxQFf3apxP6EzdLdb1XvHpqYlOCafnhDkYmxNq53RiVZRymAiHyaX2JKOC60ArSVDaXNRVEQtQQIphaba4Y_nVYgV5jJTG4ycHxUfc-hAAqgqNmo_l6hA85oqboUpwWqEkn8qkfZf67-lzJXn-qF6x2qKi_Boc2zFvxJ5gUH8mmb8Pbt6S45BVYXou3ZBasjgejqstdF_Qbv7pi8xtJ8AOYjlQN8cQ_Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=PyQNJ6L2YJ6fdsNybt6_2ZSg00RBs5m_7lybo4Qx4j-3mQQIP3Uce3kDpFAnEU_5LfeNalJfpoMRbMQoBh2I49qqOPc1PVO5qkAmHiUNMdwY90R0ju_V59YxQFf3apxP6EzdLdb1XvHpqYlOCafnhDkYmxNq53RiVZRymAiHyaX2JKOC60ArSVDaXNRVEQtQQIphaba4Y_nVYgV5jJTG4ycHxUfc-hAAqgqNmo_l6hA85oqboUpwWqEkn8qkfZf67-lzJXn-qF6x2qKi_Boc2zFvxJ5gUH8mmb8Pbt6S45BVYXou3ZBasjgejqstdF_Qbv7pi8xtJ8AOYjlQN8cQ_Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=XxKl5ykc977yMzef4_6wvW1DZqkfgOWyBKPcILJBjrzh94HKTDJYq87nbTOKfx4AenCvQmGUPSkTMwL4CdJDmGcMgfS3ENaZx3XZf94RW6FyEbvaxSvkHTvCWv8H3qiKNsNaWoD5pjSiJzpfV8s2SYQrKTd675CiiJrY1aZocMJJw888p_d2emZAoanhAdaKDkwiyofIDzQDZBVnVu0zJJWym6yz9zVsBPGrNjJH_G3ASHCmTXA9kTsEPc_29injh0ufyOU2WL2yHlPzfDlF8oVUqtbiY6tnuAxPrjqDKn1EnwjEXJV30OcfS8dIPRMdh7tRXLiVbox4ffGdqmgQWYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=XxKl5ykc977yMzef4_6wvW1DZqkfgOWyBKPcILJBjrzh94HKTDJYq87nbTOKfx4AenCvQmGUPSkTMwL4CdJDmGcMgfS3ENaZx3XZf94RW6FyEbvaxSvkHTvCWv8H3qiKNsNaWoD5pjSiJzpfV8s2SYQrKTd675CiiJrY1aZocMJJw888p_d2emZAoanhAdaKDkwiyofIDzQDZBVnVu0zJJWym6yz9zVsBPGrNjJH_G3ASHCmTXA9kTsEPc_29injh0ufyOU2WL2yHlPzfDlF8oVUqtbiY6tnuAxPrjqDKn1EnwjEXJV30OcfS8dIPRMdh7tRXLiVbox4ffGdqmgQWYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dfea1N0PQRZSldCbyunwB69rIAXLi7P_2EBsuovVbPa6VE4QPuJsl9m7-mkPXj39_xKUcnc1jtKmRdpth5KKsR7hH4q3DxKM-8etL8WhyifYCXwlohZszFGl0KzkADAwDzHP_OLY7wiPsobvEy5F-8If_grdzRFFuLm8TxU1Lk9KJV_CPY7Vd2yPdxZDuzDRQjvAKpzM5lkEo6nKTi4tofG8hw0PQ_3sxc9bnrTTsPA4AEh_OmS3rZJHv1AEOYc9QbSnOHgZEuBzGpYXiFO3HN4EweNfnsL-gqAdPe6BOJ9kkWHcrqGwMY87Ht4a6ceDiXlc2Mce7bMrgfnYILMPgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZOCfh3tp9DO4RrLRPHIxy7PxvTFVaHGODJ5_0iNfjXgcC8Z5Zhq_kC8Xg9AQKu43UXt4M8tuAW_uJGiPlQP_d9uPED9QTC37f1sXhA7yzYwN67PYiLXozm4rmJ1Ug2LphfMsV51Yy4YpzighiL6mytk_WKkPGMQaJoV9cUzPsRnRw39KPFJrNcolzzQtctLmvW2wy6oGrWHJ_6tvOMhnH6jYyZNtdX7bx9qq3JofaY1M_rP-s_GCCWmAg39cjuQTvVpTnZJlb3AHNFaqx0SS-UnBTx4D_pPFKrTqkUwVlN3HCpdWJpDo-PFQIQS02EcnbRV8VcjG5YyzBQznT2vTmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPM6f9hWsXzYuO-kN3Y5JxiT6Vtojm_Yue6utu8HGRdFQBPiaIxukzzLW-UkpLu4-RBHnJN0juJ1_pgeqMW98B6pvm8felcSmOwmyl0zT482DNucDnS7EWv605SIiyvLgwWIpqti29y6sIeJ53qBT9WS1wmPinJZcY2h3zu6qgp5AqGme_85fTWKvGwzIeHjHNk_AobvhMIc6P5LKox5FZkF-CYzUiug6ufolJIvBWX9HDy2ygP1wHV_AxKoUA0dtJ2L_W2xWmIjbnK7La1Yamdhr3f2KfeKrBgriiIWONcy583ulCi0KFn2wpek3u07nLWjSZjBHIUIqY8dsOcONg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GouawB_BSWYhM01BCqEm8lxBjVS8rn-oqD9wqLIyEEE4QUlDwZ9-aEtHmBD699vXJ6RbJS0E82k6zx10TfTRl-FOp0o9grWqwq35doKML_sg2sNlB9nsaYZZarw_sIDetgTweyIJAKylIYWaCLx4mAUwQisfyvJHowcZ0eLrtBD5z5PV3aIDgJa7fiz9SlUdUv-ZpdSG8pf02AfqbN8cc28I-kPfdkpFgJItGiHmGavs2Bh25dQfKKFuy-tc2hSW6wloIcW6vzFqbp1AA_u5j4syhgkvICCYrMk4qXnSPiOOtWAwZn9N7BUiTlxEmBEY0LmdbNOy7Z9rMrjwD7sfJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJSGueS1mzq7s-R2zRIHhZlF-SCZXHlAHyZDv0PXu4kXN78vyqiUAuTQ258uLx9t9Ud3tBflZK1sUrMjl1I3oCJzSNnEdf6R55q-pFUCTbYcB9wkvm4oNTRBap3qN-PgaeQSLh0lN8eYwpAq_a0RFjVTRXSWd5tp0z8KkD03ijzPQZkCPsyQb2cgSTKzjaJqAzCL_1Fi93Ax1hdnqxsFq6A-P75Ylhh6nimy-AiK9pIgc6giphnJrvX_RoR8wxvlcXRZsVwAf0Y4r9yi_eVyca0WAVtgU5FYx4TY1LtMtWaS_SjyFe4gs5FXxLMg0px8l9gjRFhpNg1CuXzNNgHAlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2P4buHRiwdCImzgBorQPl9d5EcJ59Xhyi05rSwf_N9olRdIGxIFudl7_aFGXUHKfmfR5iwSJGVU-9fDcK8CaH4yMQQE2JfEVesmFOgde0JFWHeBvfCm_URXRdmIuz1Z4HDtIQAHqd9NZ6s5XcPx88UpRl2xPqf6iE7PJp0lKZsQKxVDrpBrIV1r8_CIkbNmIYA1Dg-SmnyXzx6D-MZnAOqP-hnezjtQo1KegkhlIkKv4sJ6zdMg9oEUWf8feb-4ZrAB6YcYAhTVj97ReIyfsEHJlHDO3xqfxHVSZcY6zN_P1P8Z6X8GH_AtuNJQ0-AH6bzY5pykFkjrt3sH_6ODxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mdv2mSvH69rUifV_TfJN1jMY9RSOefK_l8JibkKLQjyvYy44PYNyDnsdNkkZJWeJhj75duru9RiVRmhEmt3esMBdl16UvWXp0ky261ZQl93aRcJ2bIbcLmih-hLi57ojPC7VfgK_nqRLAjQ-yC-OE_Ax8QbnselDEhiEf5YmX3aYlgFSkqYhcgzqJED4L3eVYDebQZ1vSTLUw01vfHZSSKhTjhHcXIFfLSozVKbDI8CByLjxHk_qgTZlc0TBMgx4E-hjQhfbziYSm0aNDF62invEKdIvSKlYwRmcLhBitqFckKpN5vqqiR_-ym7rzvlDBpk-rQbPBdzNwVPaITZsVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2OkLq-r46BgAfSXJ4pB88RbU8G4okYsv5hkQ36ts9ET3q1g7qutVUV4CskhSTPUu5qZm4ME7YVC7FlVrMwRKBHb_2WAq7GNHjZCOpAGIzXp-yTyoae7_qsAbgvtafg8mOqKBW8x527Ra2lFqZUbZIzNORWL8zPxEWnuQ_DoG2oS20rYHPbIo9p_v4au-_TAe5XhRK2gOkrQ_07l9maKpxxLJsS-q-MhYJhHqQobdvdBIaINZQrZLMwgor3g_M0n2-xoD_SwfAam3rVfl2Zf0ZHvh9Az2v42ODHDR2XUazbg8-KN33bg_26T5GLleXwUSGV6bG3N_sFTIkAiQYTO2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XY58CL6HKCPSP18OBzCOCaagCdfiUFB-VBHq41lNoMRvZD9B74nbkvm_cmfhzYQT5R_XynGMv9G3Sg51N-H3TwW_ZPHAW1X_JjrIhTY6_rqHb22IV1QDpRl3tQPKPC75hw-HyuuLCkVXyD1cA6t1wCLhYfZd8OSWhKplHKcVZnppMSvh2Kvfdlg_c7nNd_B2MPtLXnlzZBwUCWpHFLb0QNu73A6Tzd2QB1UAAphoV_oZSPisg2522DQ-mGOkOP1Njah4g558b1bDqcInpJuFMrENvzzQfbq9y3GosiV6t0jmSTz0GgP_G4qD10WYd0QWaaY8Ff3bpsg0XlYVLKPQiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mEStazW90RrMYH9iba8zvQ7lAsBD0_9DmIjvujEz5hQyUd7Aku2FBbcCnf6FvFYjCMa91Dbg37nD3FmmZANa9pbHZHhMfIRVg4M3XSfCuonB5gDqlSo97L3PWhScy40qmd7J4-F_ZYCspvONdDaJ8GnW5t1tNoQ7Zvk2ykIB2TlQ_-SRIh6sFMBIdMxUI61TKzVwgUG5CO4E_C0VmhC_gtX5t6D1pHjXVnjstmxIm2SS8JsQuMxTCVQ4Sbzm51l9M1jzKxp8nLr8S078Q2iZFgpNel3OaMwoUQOUfOQOJERapz5qs34QpFkaMv6PxFb63Si3ZGyZI1PRhZuuaBCBJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xio1I7NTkZ2QPwz5f1qd2x1lEw4OdKxw78uLHk53GKFc5usjHHQH9rT5LxDSsS5SmCtKo2qNqWklYJl6jBkMiYf0Fdz228LytmSapaVHQEhl9n8UDPDyF0xmsWLl71lS-DIZxTqxfKEchnc-aVtBgcBp24mxmGTMUtpwH0GMu-5SvIr1Y_RvcOwZjnWju80-qWOGa5yR81ycgkfGEam5SaOPWPZmQ_a6CeQPHsQoDob2kOZT0Kcb09fKrQn6nk1fleV5K-5X8K-Gd4siTN8fzCrhrvad36S-pPnJzTWrwcFf2syJD6su6NOhw6kEOzUzFZxeIVjYPCKDR1ZC2jEpLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b42i2LhwHMt3uZVMa83lSFl42RV7ns50Nn9ol-mBJGHAA2O4wVvExR24xqQwplOCIL_yt3p8fGt2_EJqhz33gih4CQSPN_K8NxbpZW38V5tzrKG91KfeEK_Tii9j0LHnpz3te2oz0X0rwL8CN29PRlUQy0yDMzZ1IO-nI-ikaHOJSvzyfMOaStHt3GXQYv_If6JTHqm9_C_F7A9gf9sYGK6Pytiv4_E4N0JjeQy2A_HHfJpUhEz-OTSL_Og5PcZldWKg43VKS0BNwoXFLWvEZyuOkp1Ht_u94sDW8ODZk5mEyt2_3uGKn-D3gcu7ayypko4q273kYYVNdPGbpK2EJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=YYD4hgZ2JyW_nP-JcajO9MvLDd7YyHzGfJ0RZY0fkTELZOk3OeP9UKL82ZTK-itOHGJ_oViDKl2KxQpvqYfby4-v2PPgCkCcH14OIRXVmOhh0jQuEnuBSbxs0Jfr0z79hWRg7YE8NvhvG8DUKCm-YLqoxRBNN8Xv1hwkhAsuFvKA-RPSbKAmHdE-8e3NLyRj3QMUdzMGld1xla7t08b1jeB5nARrHbiXWgJ-LBPcripo4EZFTqyzZLfxQrwBDeXdz6DZA4M1x8qT2ESwWmLOQZpqXHt0TTd9yD1KKrMnw6-BZYRX-ImK94AZqGVqyy2TAZVaoH2w59S1HaMdGMGe2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=YYD4hgZ2JyW_nP-JcajO9MvLDd7YyHzGfJ0RZY0fkTELZOk3OeP9UKL82ZTK-itOHGJ_oViDKl2KxQpvqYfby4-v2PPgCkCcH14OIRXVmOhh0jQuEnuBSbxs0Jfr0z79hWRg7YE8NvhvG8DUKCm-YLqoxRBNN8Xv1hwkhAsuFvKA-RPSbKAmHdE-8e3NLyRj3QMUdzMGld1xla7t08b1jeB5nARrHbiXWgJ-LBPcripo4EZFTqyzZLfxQrwBDeXdz6DZA4M1x8qT2ESwWmLOQZpqXHt0TTd9yD1KKrMnw6-BZYRX-ImK94AZqGVqyy2TAZVaoH2w59S1HaMdGMGe2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=Y8ulKCaTLTcmrKeq5--MlHB1QYXNHUL573B_kgEnSc-m3PTYMvPqh74-mnphIXRScMdHSUlQN1x3_0BX-VcInTJI8_fILKymHOV99ywal3dEtOf3uXmqdz-Aihb4tngWksR0IlhxO3aBFYwZip0mHern66gLc18spfD31PuSLW1WGM2cmXlikO-96VF3z0jtB92YkpVTIXBoZfC3Pe7rNfICfNq9Pn14MXs6_1FCWZyfClqQvhTBDBpaht5wj2EA9LOo7l3c5sbZiCz4E1fMZYYVwXncS4l2yF2gdXfEgTykZay1giofPFTZ26iuzbFdFHrnVq5ohJEGeP7gW06VmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=Y8ulKCaTLTcmrKeq5--MlHB1QYXNHUL573B_kgEnSc-m3PTYMvPqh74-mnphIXRScMdHSUlQN1x3_0BX-VcInTJI8_fILKymHOV99ywal3dEtOf3uXmqdz-Aihb4tngWksR0IlhxO3aBFYwZip0mHern66gLc18spfD31PuSLW1WGM2cmXlikO-96VF3z0jtB92YkpVTIXBoZfC3Pe7rNfICfNq9Pn14MXs6_1FCWZyfClqQvhTBDBpaht5wj2EA9LOo7l3c5sbZiCz4E1fMZYYVwXncS4l2yF2gdXfEgTykZay1giofPFTZ26iuzbFdFHrnVq5ohJEGeP7gW06VmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=J6EaEDwR-KEOjE0oDofqUuFbRDh_65zCY19U0WW50zuh2dyT9gWT-Plrf5XiwE2gwg5HEN1959L9clAYErswESkpGMJIGxw-TrelqfFZ5zkK17DkC5wuHOYul12eaRAA-p9F0e7dXLgHJbtXWQosG9oMcC9ENuTEE0wUOBrRVqSU4aSQkc1Ifus7AHayy3o7qNlmrvq29uaNBtzXS5WtoHCullGNG6YFX03lDjhpeFfSEAtTtKtYnwGKNKmt4kld6aKtevYhQ8Knf4ZAFe6jO0GwsB2JAnN28Q_Gv3f4Gu_eZDSDvV9gLjXHRNvXljgpBCybytVctdJ1YZ1asCf5oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=J6EaEDwR-KEOjE0oDofqUuFbRDh_65zCY19U0WW50zuh2dyT9gWT-Plrf5XiwE2gwg5HEN1959L9clAYErswESkpGMJIGxw-TrelqfFZ5zkK17DkC5wuHOYul12eaRAA-p9F0e7dXLgHJbtXWQosG9oMcC9ENuTEE0wUOBrRVqSU4aSQkc1Ifus7AHayy3o7qNlmrvq29uaNBtzXS5WtoHCullGNG6YFX03lDjhpeFfSEAtTtKtYnwGKNKmt4kld6aKtevYhQ8Knf4ZAFe6jO0GwsB2JAnN28Q_Gv3f4Gu_eZDSDvV9gLjXHRNvXljgpBCybytVctdJ1YZ1asCf5oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=P6ZKkQs8QRI3D85I_3OMeTOoRlFDSIA9tuqwaLaXvT5Vqsh_ZbIyNXd9-zS1RKDqmxV86s6Sr6CZUxqW7Aii8ZEaQfdxPe-GOlkt2DtF6uD1UqFGQtrJBz6js1MJ0nXxWP0-IWHGfFPyfUZb4Q4fZ5_yrA7tFhEWv_xfyhRABf8MRZIdfWlCxN1MFd0WgJD5bsBMIWvRiqaW2IedJRbOC9kB-4vwwu6B2TFMWQpLTw6KGXW9j9OQPWh3M2C4T1fYI4xC3dd6rGhWa4onXplvvJPZBHfo3FAz_UxzVKG1TbOHNHRW9tzkpsmNLuXr9coFgU3POYNHAvKdJIO6jBx7ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=P6ZKkQs8QRI3D85I_3OMeTOoRlFDSIA9tuqwaLaXvT5Vqsh_ZbIyNXd9-zS1RKDqmxV86s6Sr6CZUxqW7Aii8ZEaQfdxPe-GOlkt2DtF6uD1UqFGQtrJBz6js1MJ0nXxWP0-IWHGfFPyfUZb4Q4fZ5_yrA7tFhEWv_xfyhRABf8MRZIdfWlCxN1MFd0WgJD5bsBMIWvRiqaW2IedJRbOC9kB-4vwwu6B2TFMWQpLTw6KGXW9j9OQPWh3M2C4T1fYI4xC3dd6rGhWa4onXplvvJPZBHfo3FAz_UxzVKG1TbOHNHRW9tzkpsmNLuXr9coFgU3POYNHAvKdJIO6jBx7ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=Ss8zU3KEs6WcoNbODPU4AMYnN82vUWQdA2bXjih7bKttznezXjLQn-Aiuu44o-DLYpO3ZBj6KJjETjOOGrAS-6F7OTmYiJj1_VK2NXGTkO0feNHKhL013hGyLxoz35TUm1hMgWpa0rbaFpYdQSihMGd9vEI0vQEID7v_C6jmmoz-XwYenB7QMpFH1dUq3qRS42F--ldf9VCSVzVbNdlToxn7DbfJwX8JIBTvx10m7_VrlSQH2jmOBkmUsppCp1VzyT4hsOWkcUY2WHyEtWXgZj-q9b_t8fm4aImlab7yOI16UVPb7A1Ty72tlR4QoJhPfkN95KqoqrzbaOiKAuE-Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=Ss8zU3KEs6WcoNbODPU4AMYnN82vUWQdA2bXjih7bKttznezXjLQn-Aiuu44o-DLYpO3ZBj6KJjETjOOGrAS-6F7OTmYiJj1_VK2NXGTkO0feNHKhL013hGyLxoz35TUm1hMgWpa0rbaFpYdQSihMGd9vEI0vQEID7v_C6jmmoz-XwYenB7QMpFH1dUq3qRS42F--ldf9VCSVzVbNdlToxn7DbfJwX8JIBTvx10m7_VrlSQH2jmOBkmUsppCp1VzyT4hsOWkcUY2WHyEtWXgZj-q9b_t8fm4aImlab7yOI16UVPb7A1Ty72tlR4QoJhPfkN95KqoqrzbaOiKAuE-Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=EIx44CUWnAQLNjTgt82ffT269W_s0gEGm0S1KeK2l3_XgWeiwBHLDqFG8wrts4Vgk1joYSk-fxcLQwf43wa9Cwfyf3gwfR2rLGJUkJYHQKtiQLyqTa5cy1MH-jksVeLkAwXKkXxEwCWa2ZUs40uyAAc9Silytib0Z6NBg2BurcywtW_VhN1ZYQodYVzTZC454-3-agXp90Kk_4N7jvDy_ILE4l6_S-cVfLtIUyOnXiHwL6K4998HJNkB6oGl2a3WkOgDeKkyjIqlu3uW-_9gSlieVigGSCYUtox3DCb-pbCvYxs1w2Ir4Nwv462Jwmk4wAL0JVgGZ3xzkhpSNQ8fBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=EIx44CUWnAQLNjTgt82ffT269W_s0gEGm0S1KeK2l3_XgWeiwBHLDqFG8wrts4Vgk1joYSk-fxcLQwf43wa9Cwfyf3gwfR2rLGJUkJYHQKtiQLyqTa5cy1MH-jksVeLkAwXKkXxEwCWa2ZUs40uyAAc9Silytib0Z6NBg2BurcywtW_VhN1ZYQodYVzTZC454-3-agXp90Kk_4N7jvDy_ILE4l6_S-cVfLtIUyOnXiHwL6K4998HJNkB6oGl2a3WkOgDeKkyjIqlu3uW-_9gSlieVigGSCYUtox3DCb-pbCvYxs1w2Ir4Nwv462Jwmk4wAL0JVgGZ3xzkhpSNQ8fBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO9wp3AkV5gbLcneYQ7EuFvKPtsiUZQe_NC8KvovtmlArqEGTObXdcWgSNXmxsastTpnWv2dbyG_p0FN2wopys8CfcIeslZ-W3cqagdx6Lm81xvRBQDajWyAKqenCh0aTCOjzpH2yd0a65AavIgBj8nl6Aefoik2yz4pvUW4ZCd0qMF9AjXl-u56BarDAOFDJFnRLsA4PmrT4nzVNbdB4PrCFm-9cDdTL2UNdseJxIyc9A-TW-1ofDAqvEdhWq-jiRneYvLmBdns-TZO7f7FjiHIj0TFy0l3QLowRMNADnTKSyfOpjyX2cPjzBaScVHnFuVC35gp6NGMPbwOeP5aJ5lLI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO9wp3AkV5gbLcneYQ7EuFvKPtsiUZQe_NC8KvovtmlArqEGTObXdcWgSNXmxsastTpnWv2dbyG_p0FN2wopys8CfcIeslZ-W3cqagdx6Lm81xvRBQDajWyAKqenCh0aTCOjzpH2yd0a65AavIgBj8nl6Aefoik2yz4pvUW4ZCd0qMF9AjXl-u56BarDAOFDJFnRLsA4PmrT4nzVNbdB4PrCFm-9cDdTL2UNdseJxIyc9A-TW-1ofDAqvEdhWq-jiRneYvLmBdns-TZO7f7FjiHIj0TFy0l3QLowRMNADnTKSyfOpjyX2cPjzBaScVHnFuVC35gp6NGMPbwOeP5aJ5lLI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDL-0qTCGOcPJMXV0VLkkGo6ZCfcWvDk6B-TfWC9LnDfeSdZOA2w1vVJ916cYMQylIiETgoMf1s_WzappdX3yiIZf8yIbNEFTCqdXeyCfETBx0CH0ppNNhi9bxSjXCe2ZzGQIvZcl3UQ_3EdU2ZfSKXV1N8coK767-r2C3ob78aSD2GMI2ko2NT9onv_3rzZkcf9yCJomHGsks1wep03fiGKtx-vQ19dAkATLM6-ANRqf18VcLVcmYy3YrcuqXUoO7nxWuexg6IKoDbvORqfcgln9av5e-1jmfrNatSOVBf0xZrlpphiuUD5Yl_z_2tfis6Kc1MaB-XTLjtbFadKdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=VNuUN7NqW2q9ASCR3ytzXq3b_e7NorHkmddJ_jxWabEK1CDOisjmoRasrTblj7vBDepF5XAw12xfgMIP2NBj_JVsavMKM0rMFMje7tVNYYSoOi6wOXf11Sr0bQjn6UttZFksNcL4Zx8ClteeF1H42_4zGTUSLilDCMdwj5TODhVURYz7VOjOXdGNXK9appnlsD2p5mojsGhzMeqPciBV28zqzf-kQFXAP-5gMa_j6mS73yo9WefkMiKdq369HYwsu8MnmbtKB51maoD3IPLf8iIteUgIiuBInuwksXfKFC0xxe_a3oJKb2OYmppbaTWD8DZPcmcyqtQHnZaBDJvnQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=VNuUN7NqW2q9ASCR3ytzXq3b_e7NorHkmddJ_jxWabEK1CDOisjmoRasrTblj7vBDepF5XAw12xfgMIP2NBj_JVsavMKM0rMFMje7tVNYYSoOi6wOXf11Sr0bQjn6UttZFksNcL4Zx8ClteeF1H42_4zGTUSLilDCMdwj5TODhVURYz7VOjOXdGNXK9appnlsD2p5mojsGhzMeqPciBV28zqzf-kQFXAP-5gMa_j6mS73yo9WefkMiKdq369HYwsu8MnmbtKB51maoD3IPLf8iIteUgIiuBInuwksXfKFC0xxe_a3oJKb2OYmppbaTWD8DZPcmcyqtQHnZaBDJvnQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upTjQX4hugYWwC4lhdLf2itP4gt0YIDksgoC_r2pijWt8UMWVcn_TI513sbA0SrrTMrIj1Ap2xjvd6owCDOACes__AWvQx86mdv6Ec7thl1VIyasOfpz2AHwj5j3b5f57RiEUwQV9C0f16ffUhnVp5c6h5Hgr3T58hHX_ZjwJU8h02OWoIFg_4qSCpObm7a_K7n2V2CQZulAZSsICRh3qxFuZ8LvtmlrGQnWSef1oP6cw_ThFo3Xh-m4rTx0EzUPrIoBjIaFrQtK0UWwXhmfu7fONOXhpDh25_CXvbvEnHf7Ip1CK3PJP3Xsd86Qw2QonUiy7QGdDxxAgUqGeJF4Ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jww1IUM7Ju4tlAGWu7o7PEP-E0c2MboBUIoeanu0j9YRiMGzWzWIQz9KbHEN26CsTfMG_NAm0m1Zs7wduHiijldGd3jXlcvOpdtrnPO1CrLtm4savL90qEqaptiBQRgJ2zAwArhXfh975eW6v5oJ4CPFclOqn2QGd2iLyPgfZ9dEqQ0IdhZCqyLyop1I4Fxh327CjbEIkhE7KXA3UsV5fH37RBv-5qwlD7CDwnnnmSDfbmOZmAk-1xuYB7T3wUjp7QxW3MYJhjJoJeAKjmkSKLZ9hOLT3JAyxxtnvv8eqxHkzX80gDM0PiSLAHcp4stmHc8vRWqjtvmDdohT7qtyjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3Qt3EPnXQWYazRZHx65wSanEwFyKUpt8wHoIwPpa5QCl1ywirCAzPWrZFAsAWCuWhqkIA5VDZ5zzKs9FaEAdm2a4o8Ljl3OIl_C7i8pplIHcouw3JgIuObfNlwHQXnsl4iiAmOWh0WP2MUcudTs_OiYwV8UtoDIVr-WyPwIUlCOIEor16tNelU6VaMORJ6DG8J5_quHV_39UcVBHpBzNa1Y9rsHMNyaHB5cywbx-NUKd6C0JAcW-t305Uao7Li1npKtU99pHal0JidluAr6TOMo-8ZzrIfn5ueMVE6vq9z4SqYcZmUMk1Km6yTtgd_13ZrZV8SbaT5-l1INUNNqOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=YEH0UN7boFQoqMIcnFnpB8V-wm1s-Welz_JdZQNbz7M0VHumnkNpCdbLU-GX8nV5OMGniOp1YGBIvvs-6DNFp42GDB5mzoRUwhiv900bvuOC2tDniOKfLiO2Q7S5iJyaj8DOW5xK3mWGBk_ffN6LbpESshNbi3jt8hNbWgJZ7MpES0aYV9UBaDyGefHBm8vzt5TaapTEKM1PbpcESoYwE4ld7Ho_G6Z1cVU7EbcHbnqMYv7CwR4D2MXnigPTKLoYF9rRZn5hVeMqumW-Xr5zzw1gx5zMJol75Tbd3ydvkBoL-6OZOiVYIPFGgVaH16jntBz9-hhkzrZBMTuw7cO3zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=YEH0UN7boFQoqMIcnFnpB8V-wm1s-Welz_JdZQNbz7M0VHumnkNpCdbLU-GX8nV5OMGniOp1YGBIvvs-6DNFp42GDB5mzoRUwhiv900bvuOC2tDniOKfLiO2Q7S5iJyaj8DOW5xK3mWGBk_ffN6LbpESshNbi3jt8hNbWgJZ7MpES0aYV9UBaDyGefHBm8vzt5TaapTEKM1PbpcESoYwE4ld7Ho_G6Z1cVU7EbcHbnqMYv7CwR4D2MXnigPTKLoYF9rRZn5hVeMqumW-Xr5zzw1gx5zMJol75Tbd3ydvkBoL-6OZOiVYIPFGgVaH16jntBz9-hhkzrZBMTuw7cO3zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zu3uk2RrvgvK03JZ0oh_P1igi5bvcxx7g3zVLD4VVPIgMACBft1b18qmE-P6cXixBhHSNPf7X8mFpTN_lfxkpOQLkGfjL7UF35Xmb2E3nc80JYbMEbL07FYI34lpNxN8upoami33it_mHQgQtF88H7NQEiYFHxgDzfQIYUVXoh_TrWOtQV5Vj_JrF7hNloNzE4b2oPWtNaAOYIiQtChAaE0zYznN_OVWLMnYan7Nz01jQMmuXxI-jX-HuBGZ3-1qyCPNaxIYiwVD7G6oAi-rjlV1fCXW30qR1KfHZ2AtKIjzFDzxNXSPgQp_kKBoUksoDnP5s5lHhxtaMFXSwyYS3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6GaSWSdRQWHLlmYNGY7OdVrcHtHoxfTkO0DWH7Apek7kQuIz0hPZH6e_1zvtFfUjKarZSGbtPuFssDabz8lgYCXs9qOxtmA9k0dZQq9xvyGpq-w09JaJ2KZOD2YoCltvsOOd-XUTa2xCQOf9gZT16JHVJv9MwVW5BhvMkUW6gd9tHlPlOYBtdvsVPNp_jmGIS68CEZqlBuQvdJLxAS5H9Q7WxS7yYHsvxkzpbfogR4KI-ty_bS1epskbUvhfjToQiw7pmIGfVdwYfG6IXpUgkE4bNaYc8Mbwc08Czo-hTDXw3e7DqqTzaZ62wo17TvkbOljZGgGKHK33OHtoLyBwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1_QHqK8Ws8S_YJROC6V-86wxtB2EwmqUDnqUk21qYszvorRqP3WdA2U7uH7bFcYbDwY4WqyRuWjqF4CEeTDfUga4p4mStY0fLSDA6QAVrU4P3dyyOnpQPKKmY_mlDyIumU0IIvAKu8cJFoLDPKg95wjiHu9-8vsQtvcOvzBmXeL7KZB0tuPUe8XyNgH6gd-PD0gTCHubzBJYnnmq_BNz6BoxNQ1jiQUDm49j3GpFTjWEeiEc01SlTU7tGOZ4UoSYp88NwBPVoaW7npYUkrk-535nAtgGBk1S6OAPZ-_SThasxg_GEwj3f6owHQjwIr95CbsDga8IphWbOss6SKf5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKZQdwf6nMeF6iR_xF37uVLfbSWNmUSySdfqnz22ie053JZDLLtdQaIFf2YkcgYxMq1wSd5d0OOFHNhI_H5JF6DGEllLw473qsEk_XMS_NhlHt45jl4yO5wnhuEPvWLMYWRfy1wpYb_4EpfafAFMSRK26gg58Ck90G4Islq_HKGHj3LcREqvguzjvqGEVvY5yDxoD3hYaNdFijwKRP3UpYS0eZfwQqzSPoMkRG5RrIUwdIRQbtnM6N6Fiw8J6JQovebVrNqjfl0uHfPBAyie0-kMo0YecwYj3O3-DYBjMkD8CY0e6dsgJzMYtZ7Jaq3o1i2oOk8TsqFhdXecrfnorg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=CB_2nQ8f-aedotJMAcA5ulFx7RShVqLDcl4kmb5u6S9OXJ9PQ8s8gYdfng4aRkL7eWfbfW5GD69j03FUAaoPYngl-zZiDfSeB1U-RltPmxqKMI_fv8XbGu33VrTEWfO608G0zmhZPxIB74bmQ-bB8jS8VIMJBkNkC_LLDDY_gk_NEgXAToEBAiLE0qhYEl09dFO8FwKdFo9Txazqm41w4z-M2btvMpHbA12g4dErYc7W3ZVH24663sANUTHDrYc_AzoV0MGUS7_HutAoaYEvEfiQgyQ2HVJQ6N_5hKzzlNudpxhhFYeYmywO63eDpPriQu8OhF78t4NloQNum4RO5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=CB_2nQ8f-aedotJMAcA5ulFx7RShVqLDcl4kmb5u6S9OXJ9PQ8s8gYdfng4aRkL7eWfbfW5GD69j03FUAaoPYngl-zZiDfSeB1U-RltPmxqKMI_fv8XbGu33VrTEWfO608G0zmhZPxIB74bmQ-bB8jS8VIMJBkNkC_LLDDY_gk_NEgXAToEBAiLE0qhYEl09dFO8FwKdFo9Txazqm41w4z-M2btvMpHbA12g4dErYc7W3ZVH24663sANUTHDrYc_AzoV0MGUS7_HutAoaYEvEfiQgyQ2HVJQ6N_5hKzzlNudpxhhFYeYmywO63eDpPriQu8OhF78t4NloQNum4RO5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVP2MQh-fcON588uE-eG4CROu0Tlk-DwaqP0GwhONmXLuDfZsnQBWDhwbF4k78Ata51Krr_cfbSRhv5pGM4fdqkRs0897h7EJm-abOOrF1mo0_C4XXmQ3TU4J7bmnr8T203un1ANJyj8Ig0pznpzNstzVSQkVUa39OxSIeG6ALkgTRrkT7K1pDWh0NALiAjPsSvJZMSlfKIFsTjMRxudCzdd-nmYXzAbaCLQrTa97qoxqIVTw_PjQ1bLSb4HsOcFzfTjEfvRutC2WtCL9ILYzeO3DI5dDvF2yzZNeuwYF_WyKwd8CVlCqNPQBS_A-uhwO2W-EbrX5T7ve5F8uNZo0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERfPigB8OPBkxIg-IUnnFg8C-qj820FtieM3NJ-NmfSS46qDl7M2vqIjRj2xWxChv9LRzabUU0uQDa8qqqJHXy-8uKWbUYYTVDvIIUA-qIlSsnd4lo1S59NCM6Ehu2VyiBeyzmp9gmdygzSXHrvqeGSjv-yMLkivejaxvwXLCgvFaOsTF1dT7iA-nnCHolqejCfYYJVwDRTEBap2N8dpU971oMgxYLQBR6PEpGOx7EsAWEJ8KwK83KAgHHpUVODtH7s7SoDddHvrCGimSM_n-bZDNCH27Co3biNXz_UdOka0HG6RrSuhrHLjDammWPQ8qXzcH36EEQf2HsVKGbBwPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=h89AxC25wPjeAMf9pNo3dIMQvyImaUA8aPgDpbbljOV-GQuodZXZar_SP8v8iPCPQF-fvXvpEw3gSP_4V4kJ3C98kEUvfSSP-nOuPY5mjYp35UE3wV61JgmT9FkJf9DEeMRaaNxjdreZvNIzO1PLwb6gGGgeO-jiwlqVe9RKctivdCn7vSauR2rUJfza_qpRv_WcNgEkXj7SkgkpDS2gYOXKyC91LP0F6LbcOglJghHkwGwweAlntfTEilhTtUVeSPKVtxAA5Ogj8-RQ3HCnMedqCwddeh1kcYfYqWIqWKeQI71tLtn4EfngNRkr7UIWbnlsZ1z2orY-Nc669z4geo9HMpuirS1gWuaVS9jXemrY7Mtrz5_IDQGcb3-TuWiRG96_5luiim5DhH80QSJDvHWz3HVafVgwHuaKq3cytFiIlW-5SmwZCxIvZBmXKcM90Zt-D4WZIZfmFulCCBd55vr_VOYSzTVI7Ccfln7NmqGNu7NqNGrDvvkQIxUh2tij-CjH0lT6ieGinn_fcQ4t-sIWSNh3Bl_D5mPFgZO4gWCMO5z8b_vJr4n5oHNfF7aWZY-1ACwl7e01l5yuZweCg7UBPyf-M59w3kMU7cdiF7ffmUmXQSN7N0G2TSPT3CSP_4QCKk_ZOdFU5Xhgkn80IibI88BW60MnKoMxZ_5Jrhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=h89AxC25wPjeAMf9pNo3dIMQvyImaUA8aPgDpbbljOV-GQuodZXZar_SP8v8iPCPQF-fvXvpEw3gSP_4V4kJ3C98kEUvfSSP-nOuPY5mjYp35UE3wV61JgmT9FkJf9DEeMRaaNxjdreZvNIzO1PLwb6gGGgeO-jiwlqVe9RKctivdCn7vSauR2rUJfza_qpRv_WcNgEkXj7SkgkpDS2gYOXKyC91LP0F6LbcOglJghHkwGwweAlntfTEilhTtUVeSPKVtxAA5Ogj8-RQ3HCnMedqCwddeh1kcYfYqWIqWKeQI71tLtn4EfngNRkr7UIWbnlsZ1z2orY-Nc669z4geo9HMpuirS1gWuaVS9jXemrY7Mtrz5_IDQGcb3-TuWiRG96_5luiim5DhH80QSJDvHWz3HVafVgwHuaKq3cytFiIlW-5SmwZCxIvZBmXKcM90Zt-D4WZIZfmFulCCBd55vr_VOYSzTVI7Ccfln7NmqGNu7NqNGrDvvkQIxUh2tij-CjH0lT6ieGinn_fcQ4t-sIWSNh3Bl_D5mPFgZO4gWCMO5z8b_vJr4n5oHNfF7aWZY-1ACwl7e01l5yuZweCg7UBPyf-M59w3kMU7cdiF7ffmUmXQSN7N0G2TSPT3CSP_4QCKk_ZOdFU5Xhgkn80IibI88BW60MnKoMxZ_5Jrhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=CdXFJUDVG_ztiiMpefkKdnY-nVYzzIZmyW58QBRm6OXedQeQNklatgMFg0DmTUk80QOKsFsKZ05emr9aK-7WfyCnout_lc75zAQjxXlXztREuGlVw2Y8fYIopvDPNJ-KKvQuNIbPPtLCe8wEC-TvFC6QWXBdbtMCYvNx0G-GlH0tSdlVPQ2a2O8mAek8nsS32iUk409GtxYgAIcXF4tMU98Zy7FUZRKFrvs997H2SYbSgCHC_aCt7AuZci9YdQU3bE5eISC2tKfGYMyA-b9dsHgrqLkjpGCdbk617_W8Z2_9jXii0KyeYmS45UXrdyGopBmRj3Mo3h9DULgi7U7VGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=CdXFJUDVG_ztiiMpefkKdnY-nVYzzIZmyW58QBRm6OXedQeQNklatgMFg0DmTUk80QOKsFsKZ05emr9aK-7WfyCnout_lc75zAQjxXlXztREuGlVw2Y8fYIopvDPNJ-KKvQuNIbPPtLCe8wEC-TvFC6QWXBdbtMCYvNx0G-GlH0tSdlVPQ2a2O8mAek8nsS32iUk409GtxYgAIcXF4tMU98Zy7FUZRKFrvs997H2SYbSgCHC_aCt7AuZci9YdQU3bE5eISC2tKfGYMyA-b9dsHgrqLkjpGCdbk617_W8Z2_9jXii0KyeYmS45UXrdyGopBmRj3Mo3h9DULgi7U7VGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vk5u2sDvAYK1SgviT24ve2RWN1NE0P0aXE1U-2q1YVfp1H87ZtGJkOcZUhV-Gr9LdnxcOUJgyqSIOAzgJbY-YtLngZM52Lk-mmAm1VvmqaIvdP_yIAfV2kzCk_uW_kM1nFJtNH7ud3qJIDmyw-8ULYDNBG_2P4cilFJl_jg2gqBCDNtIGmdsivkaY5QTgY0sDVXf0qoILYejQgVOF67XsjfFkdRgY9cOvIlfZf1S8sIX0O8-4Ni9qEQmXfkZ-k9BZHCvN9RVj6RKDzaWiIzljoAC-lxHnT4QJ-bY8qBWHh5QJ0RYpOAbfjlW-a4IScwEHpJnTGZpwg6uq2hqiDSnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=PDheZn10h9f-DUB31W3HnCawT7d8tSFAU_mHfxWfro51t3Oy6gZaxfDujNXcyhTnk3P82_uKig5mw_on7uNJ0lccoLpnnTO-p2wXKfrjqHTENveVsgt5Zp3qD3Zkj8h4ztRMkXAukQWUPV3VpTJaHZiqHzcF3laPB2iAWllvOgI1lR-xrWzNspJsYOC1nOucHLLEjMuQPc_cC-mqAzfcme6tkHRseGvRXPJFfR5qGUbxwlyCKdoMjtb4Rxmvp7N_Dvx8cWAExAHr5hcCZPmZcA-qOX9c1Rydb8_XwfUnBNWDfaBY_l_fsJ5uCrBvqOXEAmbl7Ey9ZfXIZIFuWwHaiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=PDheZn10h9f-DUB31W3HnCawT7d8tSFAU_mHfxWfro51t3Oy6gZaxfDujNXcyhTnk3P82_uKig5mw_on7uNJ0lccoLpnnTO-p2wXKfrjqHTENveVsgt5Zp3qD3Zkj8h4ztRMkXAukQWUPV3VpTJaHZiqHzcF3laPB2iAWllvOgI1lR-xrWzNspJsYOC1nOucHLLEjMuQPc_cC-mqAzfcme6tkHRseGvRXPJFfR5qGUbxwlyCKdoMjtb4Rxmvp7N_Dvx8cWAExAHr5hcCZPmZcA-qOX9c1Rydb8_XwfUnBNWDfaBY_l_fsJ5uCrBvqOXEAmbl7Ey9ZfXIZIFuWwHaiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/athvtGmAZxB-Gv5Ij_wEl6IqfXxiIMZqGSyhfD7y4GOGa_Bv3aqHEZH6vUjr7sT5EVHz21xSOKKSaEkf961_ORkv9x5T7oaRfMp6lZ44h9_DpNCvKNV8GkmTEMYGQ_5vtnn1oNz2D6qeGHjRotwfWfQnh07Luo-n50z7L19PPMx1hUM0KLlyh5hSj7Sbm1kZDLUyn1hTzIY3KgNgHWtKNH8_DunNVxiMx9FwtgQAwHYtkX3qmrdyAy_mC6AIi9NGkhZeeeyze8HJ-aDYd2xDHnXuNIcz3qEg4BR96IidUyOvaty2AklBvQOdDvA3sKderE846Tr2ppd9wHz9EO2j4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
