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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 17:57:40</div>
<hr>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyhagpcupVXjPk-nJKEJJ8eFP3HRp43PmbI7G265Q-OYFtT-KJAkqFZxy8bLm0kGY1zpdikpz3uUozvfH43cbsXwqJb4OcZ2ls3Xs__1fqMYcgaV5uQyLe0kuQAQy3b_KI9c7eZdrNx1w-jjpwwMUmgPh9wyCMB7xkDrQmQFQ7gJkt_HF4p9LJ03uPXAD1_-nlwdc_r-OJmoqMjlZMB9CH21NfJMdHq2RhQlfE3ITXxJzHX-PvPKLdjMaTWmW5Q_GlACaO9DqAtALNT4ue38sOX0HQYQVODwG0EdWd10BPHT48-eSuV0tLO65YayiUq6hv0TzFTBjbvPi-GZKCf1HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDPUKyHHYioBeobAF_FBiqwj6fS_xju6xNXDRSUfat3VzjDKtZDxp2j-OtGRpwWrCRsld6WQUnb52VHNswBTVWoZ6HYMV8RQ79FQpjDNvgO4mIjyXYxfkRzy_Td4w7VUV9Crw-8ipAax0xpW5b045XmgL0AqAxkNX9tYlMG13w12gZzpMHrM3FQ1MGedrC7jJTinKv8L50sznVG7MkGaDwYG4QlMjkQJ41xsnkH0rG7omFdFjnxqhm7dGoZJCfh8oVuvY2cqYPL1PaUAGHabv19BuYgubVN-pOq_TLy3rRa3iTPMMNtI89nk6rCtwnNe7iafuLDjLNus0Xbw6hSyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYwsTfVckdui6X27eQmEuORjefB8vf3SxEdXfPDjvlwOAG6FcSMLuNOWbOlxweZa6P9gnf3YhjBvO-RIYXhhRaTKwC7HPrtj4gXlA09lIHju6tSQQCxB2Xq2bcRF4OZ622BdW5zJG-PkrVkcsBwYXLXb9QLjjyTbUXaxX4AXDS0EDOrOCg8lCtXzT1Y9JLMW_E5rqyx3LjnTRFeXq6rApmEmOC7d0j58DB2mOHQdvEmpRmKHws3wQUWL1OV5JUclPLiQn7AuijEgW5iNMHZuEu5iDw8CxBgUMXZBkGlfohEJtDokCrwBiJG3moP2V_C5S9JnaMQdOwmFsFMQDyKbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UP1OQZXMlBAqkFpy2LLUBCgV44cbR-pDocMzLAh8jIIxKGyCT-KofOjEvjXcELSuDnmEHvMJlXDwMkWU4g1qgSZ5YIu-henkAw7oCx0fhKvlqgSH84geZlyv-ojSVgZ4fHvFIgp6Gh6k5FGjfNXMIhnyGDW1BSlfXOgv-gTmKtY4nZVs9HyzHEUPaUNQ31aUYOom5PPmrQ9oacZZPZZ9G4ymZtb4mlrmDc4OQ342u7bnsxBxL4_bGdSIy7PbXBx2mGeYLDDZB6UfAqg6exDxjGSygVFvPUv_v1A9h2gm0Qg80LSsLAiWO1V9MYIF92LYNXO8qmGr_C3MhKZW_thSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=PFYVTojENTp-rtSRwmrybw8WHnFblqXWtxa09dp9EXczhG6vLvxtVsqEotljqkXaF8cXfo7U4hT0RjpraXSD1V-ZS750SinN8Pandu263YhTfTRdHqHvIjOtEoY-H311spWSktt9PwrIxmTxOh90KqGOqGvV1p0pNiWTviEb156_KNGzn1wyMn4yE19ewGcXPX0m40Z7dlsGhGi9vUKUndrulCQwVTTwSvnAzPq3-oPp1OpZDEJYga5ZMQd9afzXFsidtQN4I65o4Y4kcIkcl-0N0VbNv57uXn5kcjoa-9R6fCaWbX-mR-mQWIKdFqz9ed1dK8BGGQwPqJTPQqP6pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=PFYVTojENTp-rtSRwmrybw8WHnFblqXWtxa09dp9EXczhG6vLvxtVsqEotljqkXaF8cXfo7U4hT0RjpraXSD1V-ZS750SinN8Pandu263YhTfTRdHqHvIjOtEoY-H311spWSktt9PwrIxmTxOh90KqGOqGvV1p0pNiWTviEb156_KNGzn1wyMn4yE19ewGcXPX0m40Z7dlsGhGi9vUKUndrulCQwVTTwSvnAzPq3-oPp1OpZDEJYga5ZMQd9afzXFsidtQN4I65o4Y4kcIkcl-0N0VbNv57uXn5kcjoa-9R6fCaWbX-mR-mQWIKdFqz9ed1dK8BGGQwPqJTPQqP6pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=Rl0RuRJXE7W3Q9nXjZgIs8sOEwF67_EuWt188Qw-nY01D7N6xzW95e70ht9H8DHqfuyECte2tBtKIB9XtFkkHjlrdO-sPlYxvNzhYpqjBjSz_6nwhMnS8pDCC7qRBOivrvLSoRGTH26E78pze217D8fACgLrJ9hCe11xPPLQfx36cih5SsWrXJmdSWmo7kKbVp5qbzc2AKCwPbNdGVBa-3yGJ15B0OMbSrRsTVojaqGrUyAWTCW6tt3hQN3gomNxhpieQVZueN8dyaENu-ifU3__rxSA80ZZujspGJu1IFW6IQtbKtzm-JTQolj2WXLmhhPluZHcaDhow2AiCccVNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=Rl0RuRJXE7W3Q9nXjZgIs8sOEwF67_EuWt188Qw-nY01D7N6xzW95e70ht9H8DHqfuyECte2tBtKIB9XtFkkHjlrdO-sPlYxvNzhYpqjBjSz_6nwhMnS8pDCC7qRBOivrvLSoRGTH26E78pze217D8fACgLrJ9hCe11xPPLQfx36cih5SsWrXJmdSWmo7kKbVp5qbzc2AKCwPbNdGVBa-3yGJ15B0OMbSrRsTVojaqGrUyAWTCW6tt3hQN3gomNxhpieQVZueN8dyaENu-ifU3__rxSA80ZZujspGJu1IFW6IQtbKtzm-JTQolj2WXLmhhPluZHcaDhow2AiCccVNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVFkyalSQdjsb0mOWl_I_EWuLKjTxsnPVYL6eACrT6J9bEgty0_qWDX4R79Zs-ZAlvpxcCpa4DtHTh4hqv5oJPCjJGMRQYU_S2ySghhsmwGO7MlDQEcTOHjaHW__KZG2vQRDOxUrjOn09Gii9m6KyZps4JsnXs49PunE3Uh5HkvF3LHHQmY7U7_9m_jkr0e9nTfzbJueWfaU8hFKCSVK3ArTjCaBi0dNt_nEl94P38vdCUt-suSp6PXpix8Ll0BHriiTdL3WKCduCx4VzxRLInNxEh7f4_4dl3i8C4ww7hMfAkNzK3NP_duxREw0zIeVUOd5-1-1Tbq0pFgur-NIgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=FbmtZNzAr8XGlE3yUGss62nPZnQ4-lbsynqViBaFo6IqiwOpuQNZUBtzhn5L6B1Y5U1_bsmcuj_k-jV7dKjd6Za_C2Li2KPo-aWOOqsQH4Ydwp4YyT7EF1PAQVzeYAql7XOfGChc5oksUgTcj5vWo71-c7o87Ft_t5Kg3QlMs1PoB3Et7UkJGKh9yyy1_rzlbNv3CXzsOxYf-BdykgUJDw_doFRWpyBJXf8DOQskBOZAbUqslVO4Cw11CxQNyAwZiiCJcgobCScWy5BAptGuIQEZfSe_EfGsBbQ6S0iTRDN3DbKTDymyc8Vu7R5vW73gJylyspsWgqCwGlBNlSkjWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=FbmtZNzAr8XGlE3yUGss62nPZnQ4-lbsynqViBaFo6IqiwOpuQNZUBtzhn5L6B1Y5U1_bsmcuj_k-jV7dKjd6Za_C2Li2KPo-aWOOqsQH4Ydwp4YyT7EF1PAQVzeYAql7XOfGChc5oksUgTcj5vWo71-c7o87Ft_t5Kg3QlMs1PoB3Et7UkJGKh9yyy1_rzlbNv3CXzsOxYf-BdykgUJDw_doFRWpyBJXf8DOQskBOZAbUqslVO4Cw11CxQNyAwZiiCJcgobCScWy5BAptGuIQEZfSe_EfGsBbQ6S0iTRDN3DbKTDymyc8Vu7R5vW73gJylyspsWgqCwGlBNlSkjWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRkNt9P_K0cLX0X1iCZoQfyrbNeOd_JITf75SFDcR1lVcltYSUOBfL7nSm9u8yzj1LlAhpNTt7Zm7wG53cl8PGIUGKVNZLLBYSNStKSZ0rTm1cvJR6lkRS-NE63ed7WZqWQ584z56Fj9tiRjwhGiQ0NIBagqU3Ip19kHXNu7LWcs1Q52OWwuslV1-OKjej2vrM3iixpL_s2iMM1pw9LYwIlUhKFggRnRyt6j8-qSQz7GAYSgtyRkc1GBiytPfid7m-w2UgPEYWa4zDMWTGHi5HLyWLfetuG8KlP-bs-oh0cnqP_AvCushNna2NMtHtkT6CaSMVBbsCbBlHgcn_y2uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTBwOvdUAX79gvZZTKQC3tuB--W10AgXnRDgTsDgogl6Xz5TFfX02FTD-_eQ2vGiFgRfrSJ8utAwtaOwahgnvJpzXqrPCIlTocgmkVsoXp1iIV30TReXb9FpLAz4GxdVkx7XABavFXUwDKUtewq3-DgyNy6AQchxOrHOBqsuV5vsRIWvkvMFweS8MrqI1Xt5VHgIBwNjev4aH3261lNLlQOYxaDnDwe_1G-imXhKTkxVIFMZu3C0i1CNfFxxGamMU6s4TyBniHzfM8Ful32i-0xPdzJqfnGAwWkX-q3zRhbHOoYW76VZVTlim8SwIehOX6qRHaPa4IW_2PovDlOvZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IudZbxwKsOt_PaDDj_JgyW6CW0R-28SavvD30tp_gT2n9i8oGFLdASOLzCHGjamZOG1XeHEEhVBM-lcUAkL5Dp9edwxsT9zD_7nzcf9W-GSWXIt6Za_hTDcfGsSHmzzqV21Vdbnlk-5WNWOP_CDzPyMxxDSHSD0SN6JxzJij7A4e2vgTmTQ1MFHXn-JEHqKrEaOJfi-w9QGHRZzPtuh_Ua_dsD19RakxThCJZUQUxRPxjkLda45R1qii4LaJUfdjhI4oZjv2r6Vd-RxaXV7-Zf-PUhH3bPVS-WiUlJ06Baftin4-WekU4RKbKQRwIWDmEeBc_VIXsoGatCLtZXWdVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOBCzJ9zSxUsk-pFD9ZxYn0DNc6Xi1snjiD-_in412zUl7LCLJYVFA_0pzgMZPQGvOKDqy1aHu_ylynjqcgelVqO5ZNfTB9Mo1lzWt5HycS6d_rXzY9IIu-mHvfJ3gRcSBTNo4URROmbTi_ghpWcGn3fS7pvYJIM23ADeo33AV2S8j-8joIfe8CIL7TSK9XZFpTgL3u6o4LLLn5EHGqMaynDziOZUQfLiDqd2i9VdDxZE5rASCKFacSqa4QiKsqZzBdk5JmOc-GqeY5g98hgqvZjBwhzKs_lMtRKOZzAd7byitRqC4EVErm0Fit7rwKdlNA1U8xUWAXREH1LaaW0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=YyCFLy-2ZiI63NhulBI_WKBjZqhmbVj9fOCfw2i-_sBYPKMduhxP7pEu5v6atNW94X-PZiZckfwH4PKXxetpIbtN8hDFDJW5IZVw0m_WXDbn9FqdNpTd8PBn1sgsQ_Tprw1qoY1Kn6xyLk7BfZ6ZDyQaCT8bwimnsQpvHmmtv4QTYnTDMaWabr-RY1ve9TkNtC5U-9yAbx-At-FrfpcyT2d23P3Cx1t_SkOEhTHq8kA9IxwTXDOmxa4V8G7bM9caMOTy86zUGBesHKh6o02W6JyAAWE7cLRt4mh6bbIruyO4lS_U5rfgoBAJ3BuobePVeX956_KoyQ1FPPzyFI3u-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=YyCFLy-2ZiI63NhulBI_WKBjZqhmbVj9fOCfw2i-_sBYPKMduhxP7pEu5v6atNW94X-PZiZckfwH4PKXxetpIbtN8hDFDJW5IZVw0m_WXDbn9FqdNpTd8PBn1sgsQ_Tprw1qoY1Kn6xyLk7BfZ6ZDyQaCT8bwimnsQpvHmmtv4QTYnTDMaWabr-RY1ve9TkNtC5U-9yAbx-At-FrfpcyT2d23P3Cx1t_SkOEhTHq8kA9IxwTXDOmxa4V8G7bM9caMOTy86zUGBesHKh6o02W6JyAAWE7cLRt4mh6bbIruyO4lS_U5rfgoBAJ3BuobePVeX956_KoyQ1FPPzyFI3u-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftQ44zu9Am-NS0RWkH5nKeS95HT8ayroh02hclA9J3HtILqkzxwgnTVacL9Lc8_ffH0vSZ7yTrb28WVVRhUPGOEQFEyV-pDjXThOdGPY5q2lMFZIfHToWeqPaphHwydBgJ-2jnNBEbHLy2xh-j43JKP1Uuh9VRY_I7_NZzoIcg3Fb7d1MNZNI1XHVE0y2l2_HbPuRw6MrArz2GrrnPRx4Ra4TkcAY4f9RcV6sRMgiE4qPZO4Blrb45-LCbYom_QgVDItgLh4pr9_RQw_cMQSyAYECsn8FFnEPvEuYkXamRie6LQMuLk_UO1OnCS1ibc2YrZnOEZua7giGstbYXmUSOZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftQ44zu9Am-NS0RWkH5nKeS95HT8ayroh02hclA9J3HtILqkzxwgnTVacL9Lc8_ffH0vSZ7yTrb28WVVRhUPGOEQFEyV-pDjXThOdGPY5q2lMFZIfHToWeqPaphHwydBgJ-2jnNBEbHLy2xh-j43JKP1Uuh9VRY_I7_NZzoIcg3Fb7d1MNZNI1XHVE0y2l2_HbPuRw6MrArz2GrrnPRx4Ra4TkcAY4f9RcV6sRMgiE4qPZO4Blrb45-LCbYom_QgVDItgLh4pr9_RQw_cMQSyAYECsn8FFnEPvEuYkXamRie6LQMuLk_UO1OnCS1ibc2YrZnOEZua7giGstbYXmUSOZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIpg1HnMiUHSC2fek9oYNkG5Cu4NcO35MNkhFBtaoCAxQVaPtS9qZLk9Cx-QDs1Md73kRYS2fDmVTzgcnjY0ptTaABl4z1s4Sy_sCVvhGWx341LpK84qOgl84qecng5MyS4mP92vhzdaXxJ6EI0-Z-LAiY_fzqrBhaUpjgaJfZKVDwpFpji1A9Ap_Otl1AN2fXflY5_D0Qqe-OlLNChoe-IqI0cujOWGFYaCxxUIeQEptmQFjNQnB0_xMcnecEvXKmMnmwVNoupSg2x2De8DsdNjDz2pnYqrgT89RmiNpFQ01aqJvswA_IbyxfCh5uv6aRLcixtFx-ImQvQ1p0qQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها
محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار
جمهوری اسلامی و نیابتی‌هاش رو به
«اختاپوس» تشبیه کرد و اعتقاد داشت
که باید به جای درگیر شدن با دست‌های‌
اختاپوس در لبنان و غزه و سوریه ، عراق و یمن و …..
باید مستقیما به سر اختاپوس کرد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPuH0ngFmFC7JDQIbcjizkYxeUWs7riFMl7ARx_l2YykTEBwIStYdpTbpHdluIHg1BySCMAAqT4YFDMF6D8kII12tNBdSr2-7sve1XpwyEP3Hd2t3Ua8yBC8FUvbautFaW5arGZruUJDhqnE4TPsehQYXa6ZwKK7eUDHDVtuwCQAUVAjPOEFb_iDuAxmqzFwq6FkslwPRcnQ9Uto8fumiJg8n0eV1dkC2qTZBXMe52wMtCzc6ZIeWLwvP6ouobYROtkuAt3G7LFPnjIyU-aIPvAWo1xRPTZWTpfQ9TaTJyaudB4r5P26TjDREIFLScUEd_EuM044Wy8hjORp0Js9tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OtJLxtrELdr7wLivSk37Jz4PBUXM_tMU9LkA8esfoP-rC7EHzu9TCa693FEsboPhd3krvDzC0wyRXrbzRNGrls8ewtku7rf4hpdLayhMTzpL1ed6-Y74xzhgVFolXwK6zRF9l1lYZ7ZEY8C-iTJosOJfgBAhE7Zr-THL1fdq5sGnjqfhif3m_G6WVUuukUMge5xy8AtTJCSplTkMIjrkQZXhrv5Ec3kZr6YpJz0s-9ZCCaNGS9So2GaqP-9WcEFEbWlxovJfTPvkCIbMs1uXppNxrjC1ENEv1VM_Ugz_WKROmVFiJFpT-lD1qnAqxpComFk7MFYZ3mVWjcoqY4Po_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mnbxKmsT6MU_bBjiQwjJDGJ34Bo2IUxB67rgrK-3e3D988pJN6HBTL_jQU1znTXWhQPaA2qSFi-H09ugTR72IlHS4-bpVskp81X4HDyaVXZpnov0KTCgNGhZRkZ1O3ivxkQrd_Fc-0K7RolyYYA0vqUmQFI4mzemh_KWxqfSeppR4IcZ0IpNEgpns3xIX3GXtdm3bFXeTNVNs6qdo4PJy_wp9zV2Vq71NhHc7qhtlTRAEAOak4X_3SakWXt-0m-V_9BudjyN8mXRzjzWqLDwUCCwRZNMKKdsdcmX6LUoCfTdFy9AHlkfYd8qwUjPQXqhrBgFnp-77ePPO3vPXwqBqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qw0iCDeiPDoScefNkMMvkAxedw9znt530U1O2JZ3w1h5Cvs_uctLtIaqDx9LBPr3SKpCHbRtX6H6CeCiuzW5q4tI09BqA7iefSfvucpdqg8rXWpLcW9QWWvzV7715bqC48qV9t2sNlwXTgdUKHv8Js1giZh82xj5XuB847Awl1sTtcOaBPRy699w5vTgmcT1HcdGV2Qs4EL_SOqMxGlD0cNo3V2UrYDjUs7iaLndCrgv9AfCfR8jdXPrEZt2TAOoYjVban4BalMe810Q9z27VcxE5mietWPbPdFGLeeSHsgRUkAymUlskt0nl8yiFWLXrDM_UqqW5KFm2Q9Ay8JaEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=DGndYGzbXzcVDKnDYdaRi_oQYS8nR8PQnzVC88J6TGiIuLHM0Cj_mSJawZg-CHaLBXNXi7G6IVYxYjbObq3A9agThCCgZjQ1EkKqMJsKnDFZW7XSrVbRGwa1k0_8VLXSK4apV4XxlDuqlQrTC6LOVrBZn7ihREQv_8i_-Nr-fnkC4_uVDjH1xcBLVDZVG4gyB7mcEvfi3jn071Ag7px6N-DIJuatN9ixLnFMpUqeieaZ9PXrw1E32VPOk3BHdVCfCZbXuWyFH5wIN4WynXqKmlinp8j809Nw28Az8rL44ovgQ9F9aB20HXc4dMn-thZJuocxqwVVTbU9oCn7PA6B-nJeyoxWTBkr5XTOES5HtZ2PGnEqmD5x_ADNjPxynfy9Ld_rHTzQCUWlYhjCJS8GEYJYtWknHfanl5coIYZLjsZYM1GCvXP1Jg7K_Yp_-AvFcHLPs_3IiMw7wujpLRUHLGnVHP7rlMr241tH4mjQIQbT0KWlFmTvGWFGR2K_zeTWcPCGuew8JvUzSy4yNuJNlSTF3KnbVzUwi75E1GtD4UNMICmMrjNA7wLHefpIh9tQGBeMAoR1LrWwvEIb-25q_hwikd_UJGQTEJPF9PRec-GCMlEYzPoYpvrOEZwSg2afS8kCjEF8CEeu4HMME7M3OXqvTvTcxcujdpp5CtPAHsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=DGndYGzbXzcVDKnDYdaRi_oQYS8nR8PQnzVC88J6TGiIuLHM0Cj_mSJawZg-CHaLBXNXi7G6IVYxYjbObq3A9agThCCgZjQ1EkKqMJsKnDFZW7XSrVbRGwa1k0_8VLXSK4apV4XxlDuqlQrTC6LOVrBZn7ihREQv_8i_-Nr-fnkC4_uVDjH1xcBLVDZVG4gyB7mcEvfi3jn071Ag7px6N-DIJuatN9ixLnFMpUqeieaZ9PXrw1E32VPOk3BHdVCfCZbXuWyFH5wIN4WynXqKmlinp8j809Nw28Az8rL44ovgQ9F9aB20HXc4dMn-thZJuocxqwVVTbU9oCn7PA6B-nJeyoxWTBkr5XTOES5HtZ2PGnEqmD5x_ADNjPxynfy9Ld_rHTzQCUWlYhjCJS8GEYJYtWknHfanl5coIYZLjsZYM1GCvXP1Jg7K_Yp_-AvFcHLPs_3IiMw7wujpLRUHLGnVHP7rlMr241tH4mjQIQbT0KWlFmTvGWFGR2K_zeTWcPCGuew8JvUzSy4yNuJNlSTF3KnbVzUwi75E1GtD4UNMICmMrjNA7wLHefpIh9tQGBeMAoR1LrWwvEIb-25q_hwikd_UJGQTEJPF9PRec-GCMlEYzPoYpvrOEZwSg2afS8kCjEF8CEeu4HMME7M3OXqvTvTcxcujdpp5CtPAHsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agKV0wbylEK1YWC2NsPtkAQbwP-sGzYavZTdRTmzzWKI28EcvoLAmNzoJYIGrT5thGDndNUFgldx1aMa7xdHuIiJPaNmT_KsUuv0TtJqRsuDG8hRhRR-MP34TlKxVhlKZ2cXxUa1Ul1p6y7eBhBcbetGZqEKIQqNaczegBJBuhS_paiuxlgaMJL1SN24xqpta8hfWfe8cUF8w3KbenpVWxgZMrHFdvEnj80weOtU9U-hzhqmZh1LN7gZrgDRxNedhJS-b5SgRUjJXhYApjP6XNEpmVHG7GUtBGSgAoAzo6kWzXGOJ51bYNxJeyLgHjw5XdqjLC4u0c87-0Pq592pyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=GuT0hru5aoCTbaHqsPlM5IohS4Zyvm3xqS9liyqr98TIL42BcDAlzOnUKlAlXiGEIdA8cH0VwpB_oLbWyZS99KQy-pHtzB-1xwcsNcydUaRhDLOR4TcmPL8UD4BeIi_XzOMGpLygR7GxvRtLv8QGFe3FNWlBlLklhWCl5-UfZcdsgD-hP7Q24rBP4LgF5WVTH8NeRR6ffmygBzJFHdRggEnPomYkWsUL_LK6SFpPi3wfPY242vU2lpM0cnpiA7a7Bq1zNSlbR9-6LG7O1BzY3hOskzvQofM4prPxcjp_dX8mz5kaeO1yr52sLxtwV3m94l1K4Ackb027EPd0_ZI-bIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=GuT0hru5aoCTbaHqsPlM5IohS4Zyvm3xqS9liyqr98TIL42BcDAlzOnUKlAlXiGEIdA8cH0VwpB_oLbWyZS99KQy-pHtzB-1xwcsNcydUaRhDLOR4TcmPL8UD4BeIi_XzOMGpLygR7GxvRtLv8QGFe3FNWlBlLklhWCl5-UfZcdsgD-hP7Q24rBP4LgF5WVTH8NeRR6ffmygBzJFHdRggEnPomYkWsUL_LK6SFpPi3wfPY242vU2lpM0cnpiA7a7Bq1zNSlbR9-6LG7O1BzY3hOskzvQofM4prPxcjp_dX8mz5kaeO1yr52sLxtwV3m94l1K4Ackb027EPd0_ZI-bIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=VjMeD-OaGZNRpu-9JXzGuoRZUOJfa1eaCI0pI8iY0sgktSDEOIzA0lXzsArR6Me8qnEdkhg1kPpulULMk-o28Pcc50Nbqz35pmDpbFq2GzAuge5220trq8EJa71-iZm6n3d9ReJKpk0DlgTxKQ_rYHO3Q9xxjQqm1WQA4ug11vF2RCcgfblWBOVJaC0gW8Yk5hTdVn8uPK0ISFM0KsIJS3g-03RDHa8TELO6VqDZnIef72AGzC69ikVoVeN1j_pMr7Wh8mrR9kIEvZjGdFR-idg_ZlZX_Gw2NwvKyZ2i11mNnr8xv4tzJCMg4sfoAjUuI6Kh8JbWDhBqCVTMH7xr2leNsiY7YKKJ3MohdtE13NW4N2DDpPT82zJ4HNjl6iKfCBha3TL3ANMpCMvDNOut_2VHFzOWjZRYESZE1JqliGD_56oYoo-Morzo6JpsBS3rp7b24TfyBSS3HiiF4zhZBJI-xqsoUlInSRkqF2FAXc3HhFM5sRFjh-HQfqXYbWsLTIwmqKtiuOP7wILBt8bfnn0KGMBlhP8DSInIyqNVKG_1O_NtXjBfPM2K-WJOHWrwKMt6wSVNlFy53y0OeknzqYycQKzXPQQMF7DsLc2uJg1C8QLUh_ryJlax0BlS3JnKpANOkZpjJkn0FWxAN_zERBX9VmRqolDpCz9R8nY2ltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=VjMeD-OaGZNRpu-9JXzGuoRZUOJfa1eaCI0pI8iY0sgktSDEOIzA0lXzsArR6Me8qnEdkhg1kPpulULMk-o28Pcc50Nbqz35pmDpbFq2GzAuge5220trq8EJa71-iZm6n3d9ReJKpk0DlgTxKQ_rYHO3Q9xxjQqm1WQA4ug11vF2RCcgfblWBOVJaC0gW8Yk5hTdVn8uPK0ISFM0KsIJS3g-03RDHa8TELO6VqDZnIef72AGzC69ikVoVeN1j_pMr7Wh8mrR9kIEvZjGdFR-idg_ZlZX_Gw2NwvKyZ2i11mNnr8xv4tzJCMg4sfoAjUuI6Kh8JbWDhBqCVTMH7xr2leNsiY7YKKJ3MohdtE13NW4N2DDpPT82zJ4HNjl6iKfCBha3TL3ANMpCMvDNOut_2VHFzOWjZRYESZE1JqliGD_56oYoo-Morzo6JpsBS3rp7b24TfyBSS3HiiF4zhZBJI-xqsoUlInSRkqF2FAXc3HhFM5sRFjh-HQfqXYbWsLTIwmqKtiuOP7wILBt8bfnn0KGMBlhP8DSInIyqNVKG_1O_NtXjBfPM2K-WJOHWrwKMt6wSVNlFy53y0OeknzqYycQKzXPQQMF7DsLc2uJg1C8QLUh_ryJlax0BlS3JnKpANOkZpjJkn0FWxAN_zERBX9VmRqolDpCz9R8nY2ltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=Lc_1L30TT6R_rBglSuvFFwRxhh2NQ_LFHNoB7OZmYE0svjNRUGYR0NssgZMPHo0Cx4HHB_JfoDj6zb-fliAJ4ihKURVinTf8orLYaOichAmYkg-futUBiTIXDCax0iEgDRxn2TZoeoFJUKCmb4389AzrHkKNlqyo3F0LmudMPpM8KcUI9D4Jx9CxkthGzibZF8hHV0_bGJXKBfimI9gykUQmky_rgyTDFm9jH4ctcE_XIuGvw2DB3bnAEkFd2XVML0s2ww7WSXEv_KU6CqIFLk9ghQyxZvEpv5yFunlpTy8VQaHEubOnjZdm8SNt_dpZzhAAeisG7hKfhc6cMjM8QIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=Lc_1L30TT6R_rBglSuvFFwRxhh2NQ_LFHNoB7OZmYE0svjNRUGYR0NssgZMPHo0Cx4HHB_JfoDj6zb-fliAJ4ihKURVinTf8orLYaOichAmYkg-futUBiTIXDCax0iEgDRxn2TZoeoFJUKCmb4389AzrHkKNlqyo3F0LmudMPpM8KcUI9D4Jx9CxkthGzibZF8hHV0_bGJXKBfimI9gykUQmky_rgyTDFm9jH4ctcE_XIuGvw2DB3bnAEkFd2XVML0s2ww7WSXEv_KU6CqIFLk9ghQyxZvEpv5yFunlpTy8VQaHEubOnjZdm8SNt_dpZzhAAeisG7hKfhc6cMjM8QIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6VfB_dYKxsA-4vqrX9Xzyyov_A7M5kxS8SV6HzqGoDH9zJO1d_RHCGEMKFTGgbbLUtt9NCf1yYEcAVHtTl3Brq0vdhCAvOkaXQXodL7JACkz7vO15AUfeiIWJ43bBgqQP8-Bj-_e0oFAiM_3T9A6UeVeatD1EGsi7ADU41trr0UIVBHmGi57VcYHU2ZgNydI7eF6Avfsuq2eMNGu56T-uhAMsL8pgL-2t2H6WDlKwMMf3HRn8Q_KXa9mZrERDxoiMs8wEbuiULIxUnglMptUZEETNeZw8kjApG2P7GGyuiiAD7492dnuyakvjv_HuBY99Rn6coFXzU5oe0jn4VCjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DgM7Yof2aY7izf5d_j4_4VM88D1PbdQmsHM2zGoU1Z4NZ8765UzvCHWJ7GcGV118qLvFiquFhJUWPuWOpsUw4ECfQzJ9fB6O13PLJYDiuN4VSln7n2VFbDCzXARMnzaPtLa_kkbQCfOa33E8S0BtQ9O7vcpTPA1Iv23Ek49zoofwkTbEPoflR4tmNhbo7FEmDVl0OW3qq0qRQUxFeeCmcaAwuevAz1CoxLQdZWeeXSi3USbKU_Hd1R2L1sgmM_dW8TiXyCPtp9TUjJIzHPkh0GIaWhammVSrw3KlmJ2B7hu-pzz4qp58SLb_hNWYKekaWEeSAV2hmX400ZIEydNPVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKlYpPLS7MEtuHUXPiFobiUCrBf6EIyEzFyFzaHirMqr50A1lpVBTbkm1ndu_N0Fqr-rOU2Ep_6CCQNeDxW_p6_D6mk1OsrGBQ9GrLI7OJj6GTLrhgNa3m1hjw-nyALz50eUD8LvPHnkZDjlnoBV54_D6XnW2fIUOF6AmCKB6KK710d1T-TN8b-cJDxGfzcij0khwiKWVa5s1nWP6m7vibkLR9jLjoDw2eyBvqzUL8gTkc4tty5Cafbcc-BmKF0iVO83QyQEwzf9LjQf8T4Z4TdpanH8KfWWVPKVKGDb3dnyZEggvqc_IjUoTm_Vy7DF9WMKvWbU_qz_RCzqcw6JJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMJAKqg3uI7pOEUBdIKYyHVqh2RV5S7NYSGUv4GUfNWuAm_Xj7UwmR3HAejITCHpp0N_Cd5sesB2IZqyM6nfAv7wnjpzM62zSI4i4W5UQBfsXi_rcWSRrzM3lI9fiDJagvij7wmYXPxEQbF3hUKMd51CTUuIzqKdAqxYUh2MyVvnEMbp_rmoTLB5tzBcj-J8lJwDGaCnHf-v9L89vxEepUAYRUkQ4_ZgvlgvF5M_pFGIHoNplKIv45AE8Bg8YrY2yR8eIwD3le0hbHFZoGdxSuCCheST4ZhToa9FxSjoPdWZ_xYt6d0COZV3TOBM2BC2tDdY-UxM7AolzSVAYvF2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omm7jkxTcRl59GTU_-6SwK7XEdiaOMe52bDupKhwLMzUrJUKKdOtdNZUjGmLaW2H65OkvSNrEPD9nGYknUIGjuT_mYrdr1ssESFOq8uBMHekg7J3f8_LCZI98QD6gGsQwo3Q-11LXcUjE1IZSgoPyTLIvFkF4Vb_mpfNbUlU253VsoZX1YnOitvESw8oCgYKjmGlSuru469x4xOUuTa-E8m3rsLJv084SkChlOPJZFzc-w-gDz4izRD24-2IXw4tZVZ51nYFaSIUY4Tsdh_FVB8zU4pMRXjKRnMbT2n9FDn9evuZ1IIl72sVVqhx92ufcJ9CXCUM2E68uQWayr7j5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=dhwcsMsU7OKvCQc1HUtV56ag9-16p-3DjGscVKW6el-A6_LD0c0AwzGPiD-nh5I246ZSMQMS9V-kLhmq4E7dGoM8Jo5jCg8n1J_jTrrKauu8R-o3MltKW0bCs5e-coyWjpGaJZEgRcQdxBg5Z6kSRnbvFdhJxRAOgRH99yTZNcWDS5uNmciYO2UTovUi2VwlLXpWyav78m52tkrERI9TBjOjagvmjJSGelsnLozk4pTlmhq1FR1SnRlakpfhz3KVZW68s5guoavjbV-BcL6Hhwn-MmFpdfBOvgowT0pH02QLS2UkhoNaR1RNdqXIwcD9A4Ml46rzspIDTTdlCz7jJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=dhwcsMsU7OKvCQc1HUtV56ag9-16p-3DjGscVKW6el-A6_LD0c0AwzGPiD-nh5I246ZSMQMS9V-kLhmq4E7dGoM8Jo5jCg8n1J_jTrrKauu8R-o3MltKW0bCs5e-coyWjpGaJZEgRcQdxBg5Z6kSRnbvFdhJxRAOgRH99yTZNcWDS5uNmciYO2UTovUi2VwlLXpWyav78m52tkrERI9TBjOjagvmjJSGelsnLozk4pTlmhq1FR1SnRlakpfhz3KVZW68s5guoavjbV-BcL6Hhwn-MmFpdfBOvgowT0pH02QLS2UkhoNaR1RNdqXIwcD9A4Ml46rzspIDTTdlCz7jJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWtCrjhYSSLhhOt0SzxgC0cXomuI82L0Js36eGKaPbi4jCoajGQ-ouQ3GxquMpqO6EtWfi0YynkZK31tOUPC9Bm0BELOYWRj1MRqAoIsrfhAbav9xj24I3ZHk0QHOE_ypJyXWeuBaghWPyJDPonG10_p0b6GXNcaQg2YXISaS-IPODxgHqg0uCCSe1f7h-HdjA88idli7Mqm7Qw68tLvd8I92B9noUqKDeZRKy-il2M9lSma4kFSSyVDG42zuUVX9aU8OmsOHRo7j1t6YbTwgReSpZZDIZVX0A0r5YCGGHh8hWY5M15KONlqh2lqb01uUB8t4ce35RoTtX8jHWympA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwXMIh_CBPvYKuGzuVo0zG6oZGpr0NXMtjtqMJLUojBkBwuMihrWdvRTV08sQZWO0rDuzinPch6yHRHC7UzqoTdow5Ssv6L0vXpElkc7aVyUBVmVHx93RBfcWAlPrWLAo3cycq6uwlKbkABgO0y4ym-OcWTXG6NZakO-YMSbHEVbLTCJR4tqfRmOhRTry8AEh92TPbIsCUZDBmy0-xqfTcBY6pTMeKewnvxtYGzFotCIZVQZbwcZdWKS7NPmvry_cDAWHiCnquv03EJNNffRd1acgfoOF1T5Q3uS4WNmXWAusXwfQ9n2AivAXbDv3bSNg2geA37pdrAn4fCTxoVyPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhhA9iUFSCQy-V5l7JzdXQlzQgRKhVGrj5rPLb0ku3XBkmH56pmN12bBz_NkhctzIaWgimDfa9LdDkK3c58qkbBeziPa2Nx6_yX6svtowITdyjRj0NSqXLHFclZ9kFO9_fuzex17fVjj27YTeuLIXVAeS_OKK5ZH5RZnqOHcanWArBVEbMJjnCQxEB3dIQPkFKbUXMVCKQqnX0gxJBE5v17ThKeFOQLiBqyZIXh1TvygCP7UJi0ZzDG4StI0f26eJuag1GV8_a8BCpC6oWBlWit9xZ6n7V6lqW_QHtBfGfuBlvbzn2K-L_XjYufKYt5rlaqAvBy3j6k0zRB4nU2SPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «تمامیت ارضی لبنان عزیز» !
«بساط جنگ افروزی اسرائیل
را برهم خواهیم زد!»
جمهوری اسلامی به خاطر حزب الله لبنان
دوباره میخواد وارد جنگ بشه!
آتش بس به دست آمده میان دولت لبنان
‌ اسرائیل رو رد کردند، به جنگ ادامه دادن
الان هم توافق نامه پایان جنگ با آمریکا رو کنار گذاشتن و میخوان برای حزب‌الله
وارد جنگ با اسرائیل بشن.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwhiNBMAyv8XM_Dg-SedCx-TZX_Um5wJ49Qc1gwRHreTsiqn69-XDQdG5fK0RvwZdoeCLjP_qsmszHxBFroJTublr8Ip1lnkHEYgpa8V5K_PcUdkvoAy_7fe4r9Vdrq74jinUe8km8nyUB28nK9pjCS0e-VX82jxVvd8QwBO8vyX1GuYEtQCxpppSQ4kAu4qaomov78F9bqzc41sppTVIxfVxkm3cxinxKwm9HoID42MbgVdH6PWMIKW3c4uxcHIBOUgTvWbZCl8PIiyxT1ybMXxYEhsZsRrizKhxml2BHsl3pIdZqa1IKzd-kp9MmNtsdlA8NcilSyd6Ql2N1hipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6-PkAgee5n7RJCIY7hRpJzL2sT8KwWH2aDP1rtA3BkODHYoZKgGRwWbkUD61B_ivORAbBE08suLM6eb__zxVu0dHls8-zm9Fr_DKrAGBTgVpAqvr8sNw82kYsL9jCEfkGiFSdw23ovjrqhzRbc69adnJ3FHkreUbc6a7i7qZBHbNzG8C_Hm68vK4qa1KjDuH9miixwprfLiEYARcTgtQRZitea10xY1a8aRd2VmK71Is8FWQ4_XHdsBnRwl1whqs0C1t_5Wbf6J_O9VrmMeq1zvEoQLeuw099HSZviwwTmVk5ZbLvZx9nW1lf95LjNDf5ToRLAN0W3bp5eIPTQnyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3vQx1owJxPGYVzK29JL_UEt1uuRJx6GnE79p_15GnIQKdvVDQRGySiCr8qgwyZYuVCY-nCgzjx-xDtlns8sZQ83Xzx4U6uQDgcH__0HpSYov8YS2eHW1ZHVGsYrXlBkgI9BY9N6kZo3y2n3QJiywAX_lCRqevsUd5uhRe7dGG9sGsmCBqfTUi98wZzwqw893WyhtzNaxnkGRwvFMChtvuIhiY8z4ef_8nq6wlHfeVe-UaBju4ArQ-9IPnCMJbqw4PmHTU8eNaPnjg-gXiOY1q2yp87tUT20METCEPjcUoSq9mk9K0mWeiwJoJuhyYTKHHmYMYg3pc1SGfuUvL0a1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vB4YwYdy2EHrwXjQ-1CbrUJsGWnEwKUb7FHYtOAFTH29r01W_pi826LgvoWOfGPcRiX7LEKtMtpy7dn47XvHQeax5S0Sb1PJ8jgjjOd7BiMd4uNOm8L0ZhwEp2SuCiNmA6Bf_JroxNOD6JPWQvrQVDbX4qQ_GCZsSNWfoHT2-wFf_n-CQq5zUJOUmkVWorl2m9pykFyMjCcGpE3lO2GTmTsTp6FQwFvplevMZAlBCfzt6xRyxE8YKCDpysZaHT1lpKzwLV1B14h3qAkoU1omsFSKcLzBUoK6LZuYadrXNfJACU8ccvk2udR3rt4Axyoe0hQ19iPFm5tacputY0dR_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA1c5fHG66r8AfrhnISbeguQIWKzrKWdTcqK53MZKJwaWuZv13iACOEUYCdcGhF7Yb4PteikIfp0t-RMZzxs-_9EYFMx9_uZdTWlOuZ5apUwgMfBW-Yttw0UyJZzGgCTpqV-X6wt31fvfCXZz8PE8uxd7iYVuNlaHIzUI-TZrA3KZ-HozLDKvv_h20aVq1h2Lc-KmIOTUpjhfVfg0boGdpUd0_zmE5qQBjthGZvJnnpEat0CZoNwbnhzCNCcTmTngGapzXwRolx2gLyG1q7n2tKSQXjqL5Xk7t_StkCs5hA5HOkAML2-Ltru0KD4kA_XFH3VRwFHmHo6_e4lqluNcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=R0fOXTky0PZZ5X8xSDAA9m3x-J6wTCD_lzSAttmog0yI5i3KfZu2GzRd6QVq0BNrF1fIkvr-cJSDXl7CkzEZC9ylVF0zyxcXeyXXOvJ3KNZ_5r4DO-HyVJ0cvX97GnAYZ0EimbzMGPX0X9gKqU84aXx3KpzC8QmcuSzSNiKORQR20bZwdrFKCHd3I_c0m0FjT3ud6CpmbpwszBrxSnQgRNfVzYUWDKeojI9Do_byLNLmGLIi0hvc3lq8B6c3ayP4pTz0pZdcDvRpU-cx8DIDUq2dDWl_lhlrTPI0Zfxm1atmKhUiMRVOaQXpGElV0LkyIqdysVDPNlstKwQwcINvZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=R0fOXTky0PZZ5X8xSDAA9m3x-J6wTCD_lzSAttmog0yI5i3KfZu2GzRd6QVq0BNrF1fIkvr-cJSDXl7CkzEZC9ylVF0zyxcXeyXXOvJ3KNZ_5r4DO-HyVJ0cvX97GnAYZ0EimbzMGPX0X9gKqU84aXx3KpzC8QmcuSzSNiKORQR20bZwdrFKCHd3I_c0m0FjT3ud6CpmbpwszBrxSnQgRNfVzYUWDKeojI9Do_byLNLmGLIi0hvc3lq8B6c3ayP4pTz0pZdcDvRpU-cx8DIDUq2dDWl_lhlrTPI0Zfxm1atmKhUiMRVOaQXpGElV0LkyIqdysVDPNlstKwQwcINvZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=MYwCggbndp1JCQTxFZGFBi1SqmyMJdoGrzvQY_dNliq2XKHWkILv0Y7p-p9BvWtSz2KOnRk5T04OiUJHSWrnQRKK00QER3g_bvVrKqz4y74D09ne15uhgfVC4mmYwGGRqS02_pcSkdPdz0lfzTdCr6zC3g9aVUYkeqNv2OihkGvbx_P4TBWHSCyd2qrZkF5n5j-x31HiKx1Fllj9PbhspHUKPoPrAU5D5w-elO5hgXF3_QcInI7F-rx6nVChu4z49a22A2E9H-qvkN-072M4iMDZf_5j46gfuCvmUd26ZlCU1HEOKdL0Cd4NxWxM8Zb8Kcn4sp1xinV_yDG7wfjx7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=MYwCggbndp1JCQTxFZGFBi1SqmyMJdoGrzvQY_dNliq2XKHWkILv0Y7p-p9BvWtSz2KOnRk5T04OiUJHSWrnQRKK00QER3g_bvVrKqz4y74D09ne15uhgfVC4mmYwGGRqS02_pcSkdPdz0lfzTdCr6zC3g9aVUYkeqNv2OihkGvbx_P4TBWHSCyd2qrZkF5n5j-x31HiKx1Fllj9PbhspHUKPoPrAU5D5w-elO5hgXF3_QcInI7F-rx6nVChu4z49a22A2E9H-qvkN-072M4iMDZf_5j46gfuCvmUd26ZlCU1HEOKdL0Cd4NxWxM8Zb8Kcn4sp1xinV_yDG7wfjx7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=ozYACVaHWZ9YByXZRov4ftIGoaNthSrm0PRABEpPTOkyQMHtbLzDOr74vQtXRIfkbspYNPMzRha2G6oKh43Evx5lCrUFXgq-yp89a11ypZ-7uSebO2HTYZybE4LatHs5J_lVu6Iz7girKrV8zcYnjEpq2uxN0Ulm1tl12m4UBwCihqRRK9sGEt3dInQXS8jB2wvt6o60HpcEmffZUmUmlpU2TSPnPinp4qXqDepzWWWNlvgiHeh1qtz0Gd9WZFOEaHUNzhrvryJc03bQFlMZflMoVbKMK3re4P8WBw0m8KChHMwE_3SX_j3zthLDl48WBHoegCvfpp3X_5oixlE_uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=ozYACVaHWZ9YByXZRov4ftIGoaNthSrm0PRABEpPTOkyQMHtbLzDOr74vQtXRIfkbspYNPMzRha2G6oKh43Evx5lCrUFXgq-yp89a11ypZ-7uSebO2HTYZybE4LatHs5J_lVu6Iz7girKrV8zcYnjEpq2uxN0Ulm1tl12m4UBwCihqRRK9sGEt3dInQXS8jB2wvt6o60HpcEmffZUmUmlpU2TSPnPinp4qXqDepzWWWNlvgiHeh1qtz0Gd9WZFOEaHUNzhrvryJc03bQFlMZflMoVbKMK3re4P8WBw0m8KChHMwE_3SX_j3zthLDl48WBHoegCvfpp3X_5oixlE_uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=TnZlOPVxCrttuSNKsPsPoBiyGW6hs2Q1XcCqAZgidV-ltXyRR_-xTIchJ708bYVrbWvNF4DebMJq7QMXzlXfzMiqiZS0W38NdIaeBn3B5AZ_C55o-5qRMta7DACfU9MJk7GyhYcVoE2LbRWm_ErGIwPp_VwX2jKQssiAJ4U77TCgm-7xvKmG-10wUw6wX1AptuCfh9-qs0zDr0JNqirer-10eFEAzDE4iVj2ctJBuwwneSQ4eYJ-gGb9wD1-XG--MKDZr4k62QwuikZ29jZp04hT2WJNhr1l9OfLjjbRFyscNEJ_Q6Qea4ohPZ8rL2nXPHylBTqj5eyYx2FYlH2d4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=TnZlOPVxCrttuSNKsPsPoBiyGW6hs2Q1XcCqAZgidV-ltXyRR_-xTIchJ708bYVrbWvNF4DebMJq7QMXzlXfzMiqiZS0W38NdIaeBn3B5AZ_C55o-5qRMta7DACfU9MJk7GyhYcVoE2LbRWm_ErGIwPp_VwX2jKQssiAJ4U77TCgm-7xvKmG-10wUw6wX1AptuCfh9-qs0zDr0JNqirer-10eFEAzDE4iVj2ctJBuwwneSQ4eYJ-gGb9wD1-XG--MKDZr4k62QwuikZ29jZp04hT2WJNhr1l9OfLjjbRFyscNEJ_Q6Qea4ohPZ8rL2nXPHylBTqj5eyYx2FYlH2d4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=IvcL2vEdO417JfaRviYT8NbyuG5VxZKy62zqxP7fgI-PKZinSPUWn-zgczfHRWE_NW86q-_kcmzih3CWMRreG_cpwScNLiGXf_rUwtV43j5DIm93aXtbuWrfoU3zDlo34_iHkEcWIvAStDfb-Dajf1zXyfXUCoI-qdTMTpFdYtj85be-_hyHbxlp9eVQtKwQwE1jKLtSOQ40idhUBVWfBRjjNhhzR02s5hnECbowwGUSGsqqltzFYNamm7ZkYanc4FvgUTjmEc8m7NVqxime6E4BWft9hv3TJcfi3KHZEMYxwd3BRghzmiLvt8E9PDtG489UWj47CbJcwVWSNb40Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=IvcL2vEdO417JfaRviYT8NbyuG5VxZKy62zqxP7fgI-PKZinSPUWn-zgczfHRWE_NW86q-_kcmzih3CWMRreG_cpwScNLiGXf_rUwtV43j5DIm93aXtbuWrfoU3zDlo34_iHkEcWIvAStDfb-Dajf1zXyfXUCoI-qdTMTpFdYtj85be-_hyHbxlp9eVQtKwQwE1jKLtSOQ40idhUBVWfBRjjNhhzR02s5hnECbowwGUSGsqqltzFYNamm7ZkYanc4FvgUTjmEc8m7NVqxime6E4BWft9hv3TJcfi3KHZEMYxwd3BRghzmiLvt8E9PDtG489UWj47CbJcwVWSNb40Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=Nejum56INzDZV2KMMPIEHJJxAxUb9sQ0yKltg64bg91s8kWOVMD9NhLxku8u2Wd5IOIa5Y9yY9BRO392Nlu-ooSVZ9T2XjYUKYn_t6G40XslNl24uBN9xYQABwYBCnjlTVBPC_HC9vek0d0hc86MGFWlE9_MwJbVq_di3WUQ3OuLtNPfCZHVMQxHrVaOmV2ZYMB_yG3mAK7-R4OuEVwYd6cyr38zJ_BgMvsBMAbzkX21YnjXMNVWA2jbY7yfZ69GkvUOVzjsdOFU_hJ7o-F_FOGekvKALW8YOj1LFncPrT69UR4oWa-Ki82MzZbKO0tmsmAPVcV80JIjQWomxO0ArA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=Nejum56INzDZV2KMMPIEHJJxAxUb9sQ0yKltg64bg91s8kWOVMD9NhLxku8u2Wd5IOIa5Y9yY9BRO392Nlu-ooSVZ9T2XjYUKYn_t6G40XslNl24uBN9xYQABwYBCnjlTVBPC_HC9vek0d0hc86MGFWlE9_MwJbVq_di3WUQ3OuLtNPfCZHVMQxHrVaOmV2ZYMB_yG3mAK7-R4OuEVwYd6cyr38zJ_BgMvsBMAbzkX21YnjXMNVWA2jbY7yfZ69GkvUOVzjsdOFU_hJ7o-F_FOGekvKALW8YOj1LFncPrT69UR4oWa-Ki82MzZbKO0tmsmAPVcV80JIjQWomxO0ArA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO977Nbvx_ISMJt7A-Cdca4Q0ofc2jnpg3NaN_Ln0yu16djZ5Vpl6o2i_Dm9Y2wbPhnXiR6aDEVhWALIEWSOElWM6W8EqsjgRKpC2JxnTKGTpq7D6GAU47pvAtm91GYvnQQbeIsp75F-Nvhnwk8bJanlh6BplPJpunfwVuvIUk-ZrIYJxvY9KC0x2p-ytXl68IstbQ5UuFCI00Wuj3wNKx7AllW8sMalJsURTYT9H_vCsqrk31-ijyeqDmPl6RD76vDM3_ttG3hlUB-qWzXtEzO-8LOicPd0CkhVJ5IdYgFiQW3oj2Qf5Xm3wphsFQa5VHiNEtxzGXDO_stQ3mx2_rGPs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO977Nbvx_ISMJt7A-Cdca4Q0ofc2jnpg3NaN_Ln0yu16djZ5Vpl6o2i_Dm9Y2wbPhnXiR6aDEVhWALIEWSOElWM6W8EqsjgRKpC2JxnTKGTpq7D6GAU47pvAtm91GYvnQQbeIsp75F-Nvhnwk8bJanlh6BplPJpunfwVuvIUk-ZrIYJxvY9KC0x2p-ytXl68IstbQ5UuFCI00Wuj3wNKx7AllW8sMalJsURTYT9H_vCsqrk31-ijyeqDmPl6RD76vDM3_ttG3hlUB-qWzXtEzO-8LOicPd0CkhVJ5IdYgFiQW3oj2Qf5Xm3wphsFQa5VHiNEtxzGXDO_stQ3mx2_rGPs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAk7THIAqUkNyIMhavfs3TKxMPM4ndD_chgEZQhNmm8FffoVM7umBEhtKq4pS-2xlyET2OwSxlPRbGtCAdCgQfzVFdJ-03hfV2TmdqhPWO0vFYnH_83SJ_AzfLhj7EMzOm-qAdL4q_lJagdsyce5bu0UXFUf_NlqIB__G6wI6e1PXcygWdWlYvN9NbPBu86qtPFcp_YJFOjScUWug4VkY29nUwaOsftZ9K4QhUNhlNcY4PkVlMwHoA-AA-joRviZeIrVoIKTQfn5tBp-0pLopKaedXq6QoYd_qB76v4SncKQmGhfBQKnlDMdaXo1-T_2bmVGuUR4S5E13h9_uGpCiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=IKL4XYJYD9i7Gt1vI7CueSb206tMU7hBhJYLSZjV81SePJR1bpZRZPAXtg1J-tuaW27D4jr474Lk_wekF-y_ndQXYqWNFRxjDZXqejyfsenigdvAOSK0w-g0MAuSGrlmaJaaIt9aS9sHWIlmsY0MrMLrG-oobndDQwIY-QaxXFRLwLPCiafQCKXngOkYZk9TzqWbtEGVGnsIzSs7bQIHrgX5v_nivAJRmHCLaZwmEmHRe4nZWd3ewtczsA13gD9muAjAgSFIB853W8wMUm78wK21NKq7WnFlydM2GA1Wuk1XSo3GaWKsHYL7nxIeL-AL4-SD6-Z8BrnwR5EtV-2uMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=IKL4XYJYD9i7Gt1vI7CueSb206tMU7hBhJYLSZjV81SePJR1bpZRZPAXtg1J-tuaW27D4jr474Lk_wekF-y_ndQXYqWNFRxjDZXqejyfsenigdvAOSK0w-g0MAuSGrlmaJaaIt9aS9sHWIlmsY0MrMLrG-oobndDQwIY-QaxXFRLwLPCiafQCKXngOkYZk9TzqWbtEGVGnsIzSs7bQIHrgX5v_nivAJRmHCLaZwmEmHRe4nZWd3ewtczsA13gD9muAjAgSFIB853W8wMUm78wK21NKq7WnFlydM2GA1Wuk1XSo3GaWKsHYL7nxIeL-AL4-SD6-Z8BrnwR5EtV-2uMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfBfdv1OQ3L9zH9PgrFb_sWtn_m5sVuiTR-oLSVJv_I7o7aoBLbYLZjC1qmcSQJXB-0YAhzgFn9xkLYT2-4NWZxl7zxlM3otiW5TvlDScDkCDzjxdkorZeqxxfpzaMG_w-Ttt2emU3tDDwMffPBW-d9_-m4bxOABcr-bJ12YlaG16PkkuqJ82_htJqorhvBe8FBaqwShL1g6t6GsBdpYsQkIRPcOH1Up8HRbYeW_q3-5zs-NBk2_9H3zMWVtvK6U7dbPdFsqCZnj3TOL4kdUsJgDJQ45gCQ6hLVXahQnGCeJYxENG4Mbkk4ERMCGq66ySbQOxVXKRY8RjzeB_OM1-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0UtxkmMA1-B5TYAb5kAy0LHI-C6Qqp0haZxKYyjfzbOLaAorlMjWxy5WAoPA10ACVDRws6q8m5xWlXj_IJHBx3LpkUtrag2PjFOyKm1yCI4WJcZrrc7a8_QCEgO7BWuGu2lnsN8JlbD6GZbHhlHzxQINsIbHhR-h_m-t2pTJRCIqW9NZPHbZnxE0Nj22p0-g_YlgBe_pjJM1VDey_yUjY8ZpqfmH-2VkQ46NKXhOBzJm4osJnaTYS4YLQyLpy7xwXBTAQmuug4m2GvhxrKqIP1-9EshLmvdwOXKiVU0P43kaFFtx7nz_BNCnFisvrioX6XCDNl_qIEnrbgJ9B-eEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjCxZEROI9NB7o2B28AlJfFTh451xITZ6Tqt--60R6doYy5tzWnRy2ONHOLItkOYAdZ58_c5mF2ZksMQgg9n3OF3ez8V_gWzoHHJfI1PVOo5OT9DwhAGtKWv_7MCuHgcFH9gHzafvBlLN7Bq_CDghQSqmA1YSk7En2tL1VzdXqYei5XNc0OPvtCPQ4tV64NTVu-GtmC35i64b5fBGjpW8HPMhw1AXmAueo8VhkR-3uqyi9qF-OrkJLZWZ_UBsJQbY5fKLFCDCn0cU5KtLWv9fPSCfeg4l2Clw3ih9r1rQlJjg8RVkRbfKnu2QjMPyk_iPC01mH5cRVWwmR8jsI6uUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=tSvJ2HhoACutzObLoh7bcQmMMQOUiyXh11XKAHX8qUt_U5evo9eN6VAAF-s3R1uQiAifryxwZwWcD37nMEIxqOd_hv-6SPnFPDY813jcao8GVEfFmFjG00MpbyyeTUdn77xFI-7iqcF_2xRHOhERJk7YNbfo0E8t981IOv8ZldbY26CvyWs2i_Hij2k3OKqLjgo-bX9G4wWUJyb2HC8RfXeb4ft2NlVjlFPhipqnWVAa9aGTersxrpjJzJc3VcvromZFs1EPhMmlF-8V6K3w83izdZLnEfbtBMYpdWyHXDtqbY2QDMPCJDXy-dPk_wJ34QsbfNvx5cib8pmf84BxcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=tSvJ2HhoACutzObLoh7bcQmMMQOUiyXh11XKAHX8qUt_U5evo9eN6VAAF-s3R1uQiAifryxwZwWcD37nMEIxqOd_hv-6SPnFPDY813jcao8GVEfFmFjG00MpbyyeTUdn77xFI-7iqcF_2xRHOhERJk7YNbfo0E8t981IOv8ZldbY26CvyWs2i_Hij2k3OKqLjgo-bX9G4wWUJyb2HC8RfXeb4ft2NlVjlFPhipqnWVAa9aGTersxrpjJzJc3VcvromZFs1EPhMmlF-8V6K3w83izdZLnEfbtBMYpdWyHXDtqbY2QDMPCJDXy-dPk_wJ34QsbfNvx5cib8pmf84BxcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGY9gKsdEEFQcy9Tat-ES756nQ-wogv7LvbTe6bBUKfu7mx4xbcP6s7xVjvDL8jbitFk3B2ofdhvm_-VvdbDRJe2Szs7RZWwHi7pyN8YYglIe3_qSBey39tTJG9BFb5kc-QCO-ZfvFcgYabhI9I6TC-n4LKAbDm_IC0EvsZU_wO3xVLFKpLOsJeWEyG4TZtP4Pw8HK9FzAVBk2EztFjwGpnj3epEFDYdH0XbIwlaIn-1AS4FhK5y2BiLCSrWczMvsPJDhtOgeYDfNv7wLG4jIaq1-xWoFXCyvSs9P_pphoZo9i7v_2nd7tMwwySukdfYQEioBZTkimJpNUFWsBs1kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-BSLqz1O067Z5gAPLj22qx1wrXcWpe6AduzOjWxalQyXjS_dOYs04aAzQg3FWiTJbHlN-nhDvyVE_oYttPh0TAVS4BH7uV1FLyIa4O-N3qthqpQTjSo8pwqip-NuYcaNNX3TQMIucmf_ioRxiyMLWCMEWVReK17vSB0YTA6DkXXagMyAOnh22WVqx2V5e3X8Qc8ya32WOLRvbGgXgLC-fMrfYzpV-fLW8jJop_f5OO0k7FI9RIstcpzMoz-ca9NGdktfJX8Z4Q-FQR33V20xaqZ1QNSN0Hb7VKt4K2GAmT4Z6NavHgNgyPTSxJv6vmf1wdqvsoU79pnnLAS1TAjEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nc0ta4-xQRdvwvrz50xCXLv96Mk720RcIC8gXkRnVBzEPvKbCs8Wjb_-FIlCPXL5adIIl25FaWouZDC5trnRuXjFzsc0WSMvXs6mZmgRJfaNDAEeRXmyfyEZZYs9CD9uSE1g58CStpT77_GV5FZ1zpuLUgfPrNR9bG_Q9N1YxSzNrDB0LWJS2bjWOzu2Z_bG3Lj_RQB6MRYpcgHYmlu46tt-jCrXzzKuvd5Ln5hH4BYUsUl8ZyFFmGYAaThIX5OYsasdUFKVLZbfq6wANRGumd7T6yW2am6gUI7BIBwnf-1dbcyjke1nQEPe2Ede1LO9xnSmOg-yoMlFvV8y3f1y-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVzireB3J2aAnIoBQJbBo7XVCn7eyTvQPjmdVpBguHGEaWJimmEEJVLGU9CeOaqw-t8UjvoCTxBIUNSIqIJkQp1oBYZ83WkCsxLnJx-yT4L2OyhFvbCYLkHuUdZl5rKG38j21bO2WNtwvBKjYm-n4YPR-jPE5UPTVst18r5Qn4kRXMm89HRSaqrHqhlErR8YIVBnBiDyzou0Mb73qhDq3L3_-TxwZeOA1Cr-rVTekIphTN4t8i7F6EOb3IR7pj97JK2RVnpVRAfD0qr6iT4H4O_dMHzYpCucnK2X_zbu6sRHnUGx9Qm7B6aYwuoO6tsKGb70XNS7DA4jjCfDKsJPsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=XxLZ60TTc-j9CATWM6LmXoGDGy-jnZ7q7RORTqtR85KQTLDg7Bl0pCtr5S81RXjEVloMhTPHw_plrsUzZvrOTg3Bs2aRuogQD9t3g8zLYFUeaJdwl31TW7e3x5YkyyXkA75VcFdlYpYGLJSKCTtYKp63TqpZcLZaICK9yfoqx8DA3Q68n5fm24kLqKHYCi9QXJxwVq0RDiJxRM2iF-lR967TaplXINEw9PtOmfEGvZ0YfrjGbFVsjGuLHCYxRkldoT8xkM94kYnKQCNVfthgRMwLssnXxc-cpVrLSw8hg2rkGFggb9NDBFjXjhowtbXs176D2SQL5OMOItPDLyFUGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=XxLZ60TTc-j9CATWM6LmXoGDGy-jnZ7q7RORTqtR85KQTLDg7Bl0pCtr5S81RXjEVloMhTPHw_plrsUzZvrOTg3Bs2aRuogQD9t3g8zLYFUeaJdwl31TW7e3x5YkyyXkA75VcFdlYpYGLJSKCTtYKp63TqpZcLZaICK9yfoqx8DA3Q68n5fm24kLqKHYCi9QXJxwVq0RDiJxRM2iF-lR967TaplXINEw9PtOmfEGvZ0YfrjGbFVsjGuLHCYxRkldoT8xkM94kYnKQCNVfthgRMwLssnXxc-cpVrLSw8hg2rkGFggb9NDBFjXjhowtbXs176D2SQL5OMOItPDLyFUGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUaeBUDdVYAa198zJTmfH729ug5rQBAWfljm5bP1EAThBjroXqinwPq5LSx1Z7JGrZpS2BmaGmYX9IOkPud_og-hH7yFvLnCQKO9GNwLeXOzU9sROfZiU5E589d0N_qhnd3TJFufegJ1yad9WEJOxiGmGzMKwM4d935QzkJWYLvI2NrKZI7XfJPwNtym4jkhS1_p-VCjrPNQa4MOagsQyhsv4ctQf6trNe8K9nYJFAs105VW_hwR0ghNnPTvAuUqbu68xvUvx6-dZkarXsvkO7_KBaHtEEkmu0lOU3QBaYqMp3Y8-aA02dvRSDkFEvvzg1Qi2wBFFD8V1riiqmQhsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4xy7Gd1IZ3yOUXdx0HQ5fQP-2gKhrsLih6BCa7sBlpJ0YBAzkjCGBsR4QBOSAX29flNccEQ6eHE1002EDMkL--IIOpy4sJiPmGJ_3Uxgp-83zQAhhpX9FO3qf08nYKEmJK5qYPE2qKPliMv-T9yHgrNrOOqqhCuRplX5wP_dSrgJ6Frhq-Tu1fiClMD4zqlELPZr_QyzofxWJ3x3i0dRaEZomM7xIY3pUQ7OgGmWI3-KKP_3XZgv0cfDL_gGC3-T78abfNxVj4U-wLnlh9wTmtpkuUkukBD6ZvjXNL5eonZ2gIpnLKfYakyvQpzI1IyesmUFGVQRWnDSbjPQbcfyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=NB29NOcgKk-vn5yb12mRtVz4DFcA76RlGB6CxcLzaA2gu-jgCYzWC4BHnk-vHmAJzyo3nzPYGTtPOra5O1L3uag5nPpi6lRARfkGidgFQP2hm0EypuV-3zi1n3Z5IyNMUU7XoE1boj2Wi7J74vyezPhD3WAK6ZfAfLVi14XVHXkCIl_8SYq4gmLFvAR5G-Xby16BKnCjg92NLdUxBd_YW_6_18YhrnAxDS1YxWTPSOdGM4K5-ahLNY4qP5Q2OoPACkPpDnNiPODaYVDpOElEwIL3yV3B6E3DdzcFT9x3zTON05uleH3wp6C_WlsnANhX2Mg8yPS8MKx6vY-CFcuNL3Ljv7r4krPcpugot93X2i1HBr6sqjrX8k-LSd-pfOpmk73cnsK7nbRqq3A2r5AlTeZv8g8c0oaxQZZ0XjgCRYaWGiNmPJuhgzjehEQeiHm_A3-1EW0FM6hzXd0jl6z3NZlT8-5P79LynaFdQ-Bjn-1aV7E8L_FHKV0IKFLDm4yuFhPGCFYsPMLDoqFS5AqnMl7xBP7uBPOnoeEMMW1b8PbhIg958euqPYn2BuqlwFZRYV02h6kIPxzE6hDfsdhs1VI4Sn_eEi2YACY5A5A74dnPyJwIsLWGcXDz9I_w5G2hPMdF3_RUPsak7UTHcQA3RPXOgQK8UJzqImkiGtyyAtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=NB29NOcgKk-vn5yb12mRtVz4DFcA76RlGB6CxcLzaA2gu-jgCYzWC4BHnk-vHmAJzyo3nzPYGTtPOra5O1L3uag5nPpi6lRARfkGidgFQP2hm0EypuV-3zi1n3Z5IyNMUU7XoE1boj2Wi7J74vyezPhD3WAK6ZfAfLVi14XVHXkCIl_8SYq4gmLFvAR5G-Xby16BKnCjg92NLdUxBd_YW_6_18YhrnAxDS1YxWTPSOdGM4K5-ahLNY4qP5Q2OoPACkPpDnNiPODaYVDpOElEwIL3yV3B6E3DdzcFT9x3zTON05uleH3wp6C_WlsnANhX2Mg8yPS8MKx6vY-CFcuNL3Ljv7r4krPcpugot93X2i1HBr6sqjrX8k-LSd-pfOpmk73cnsK7nbRqq3A2r5AlTeZv8g8c0oaxQZZ0XjgCRYaWGiNmPJuhgzjehEQeiHm_A3-1EW0FM6hzXd0jl6z3NZlT8-5P79LynaFdQ-Bjn-1aV7E8L_FHKV0IKFLDm4yuFhPGCFYsPMLDoqFS5AqnMl7xBP7uBPOnoeEMMW1b8PbhIg958euqPYn2BuqlwFZRYV02h6kIPxzE6hDfsdhs1VI4Sn_eEi2YACY5A5A74dnPyJwIsLWGcXDz9I_w5G2hPMdF3_RUPsak7UTHcQA3RPXOgQK8UJzqImkiGtyyAtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=BNYoqjzD1XHEOCI2hVz_5autgQOnCCMf5V9Or_RBGYC4n7lhPP_N2ALk_2fCHWBaLhxYeTi52Coh-o3WobWrEmDFE4UbltB8Uq5spW0TXI09oRghH6XMzE_k-rbVyjPuQN2AdcTX3SN5lDE9yhypj_dICo2FTigHx7-WZMjc7x2HfH8ztAp16XPmRaaWniEXZuhtXxbPP0zN9JYAs_BPEV22wVGarFom6xBA0M5LXp9HHdfcgW1VT036c7D1fAKMDhvsAOaWuVdQ_uts1l3pCWE-8acbjJRihVr4HZ-nsk9qfHr9fDh_V7HRmlnvdSxTUXcgK63X9YbF4rXqqi2VBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=BNYoqjzD1XHEOCI2hVz_5autgQOnCCMf5V9Or_RBGYC4n7lhPP_N2ALk_2fCHWBaLhxYeTi52Coh-o3WobWrEmDFE4UbltB8Uq5spW0TXI09oRghH6XMzE_k-rbVyjPuQN2AdcTX3SN5lDE9yhypj_dICo2FTigHx7-WZMjc7x2HfH8ztAp16XPmRaaWniEXZuhtXxbPP0zN9JYAs_BPEV22wVGarFom6xBA0M5LXp9HHdfcgW1VT036c7D1fAKMDhvsAOaWuVdQ_uts1l3pCWE-8acbjJRihVr4HZ-nsk9qfHr9fDh_V7HRmlnvdSxTUXcgK63X9YbF4rXqqi2VBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHha_Ee1UgUQgnsErPeETvzaZGH8sN1n1mzsWiUt-u7njmXVoRSCclqmlHDExZCpAHv2L2Du8AIcVzQm9sT8Dez3Br8g8pTHv7O3aaw2HkE7z5T7EI7ov606YB2YgqwFPLz_bxWf3nNZmsLs3wjheD9jdx12fpCVg9dE4tpeGK17sW24tRu6vgqtHZvUmu-fpSCyUlRNMHcXvSZ8vRfLEb6Tl3WLtm3et1D46xjXueiMFk0V8q_DLZQysbUCZIC91R0p7HzTEJKvEJB4CytMlJ045kJyGLcWGgCSp0WweKoAhzwTOUJIfUZ-Eu2aYXXsplxZIJQ89KcOC9siELpYKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=gGLXx_j_r2yt4hMaV__8vNL7mbl3L-l6yMSNABaQOT6bJRhvSIme7DOnS7kNf9XBHQhRmViT_vDmrTAQE7wLD04n55SQIyFkwBcrksRki0pCbR7I8ZRtrRjy4gS47h45mXnne53WutKppjycBQuEuXOrok1p7Ax4bUF38mMGZKyCEyHRTNVgUbnakcklz0fABae4uhfq2n-6lSJVvivxjYfzg9P68FmIVIl8z3foGHacLjluIGXqrHSg4JzqL0n-ifp58bJLOsPSHhWH8XFlmRjh7zKtr_gqvDgpBlXhr_QXTCAdwtCq-3vw1UBRdtO00M_7m0gKgvtm081jpx2hwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=gGLXx_j_r2yt4hMaV__8vNL7mbl3L-l6yMSNABaQOT6bJRhvSIme7DOnS7kNf9XBHQhRmViT_vDmrTAQE7wLD04n55SQIyFkwBcrksRki0pCbR7I8ZRtrRjy4gS47h45mXnne53WutKppjycBQuEuXOrok1p7Ax4bUF38mMGZKyCEyHRTNVgUbnakcklz0fABae4uhfq2n-6lSJVvivxjYfzg9P68FmIVIl8z3foGHacLjluIGXqrHSg4JzqL0n-ifp58bJLOsPSHhWH8XFlmRjh7zKtr_gqvDgpBlXhr_QXTCAdwtCq-3vw1UBRdtO00M_7m0gKgvtm081jpx2hwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjrDffEueRgYPO7OIuclojKtwD3Gp2L5zfvCn63aLS82isoFXyf7zxtAH6r_mcTF-t-uHP6Ja1DTcd0Pid3E7yTQmNoHfjLVnh4EuMDOADWdHl9xhtgH8j9hDIZhMfBV8s3Py1Rgi8bpex5qhQ1jSrmf_ZJLyfxoRrOqX1NWYCkyH5XQLX-_bA1afZ9uoOtBks0EZVVr0r8cAXAwuLg6O2uoMap2I8wgL34OHQ7E2d5jWNhQUuhYL6lb8Yi_4GTlDu7qfeJHj-qLTRn_1ncaveBFgmG8lNeS5ovrlishPSGe9tEuL-Px--pYKDiPn7DG2ddacvaTEOrf-SbvMa8ZuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=bbQ-GwnZTvyfJ9TaZwwjNpMA-IibnUxfYLPD2YaGQEXwi8LzLKQoHMNgyrFdSCNsqdOZSge0osMw9zIY2zEGbCu7r0StxDhs-GisSxqLRmxcHCFKjofoBQ3_d_mwfrNSrXJQyXkxJ8XI1qWaVIX0YEgYr3NiQ66U-60fCL9nmiJdhiG0pRDwHzDJg9rglpB8MxR2xriwNVHJpUut0MoCxNX_0XioKTADuGhp8Ff5Lp4XPSgqq-AHcqHIL0RWVlLvDNnnGeLA5_55h4WD_VPQhJUPZCkA7ONJ_Tz7dPWM-pysMznpRXE4FgoLWg33TpEbeVTnJaIu81MSXc3u0wf5bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=bbQ-GwnZTvyfJ9TaZwwjNpMA-IibnUxfYLPD2YaGQEXwi8LzLKQoHMNgyrFdSCNsqdOZSge0osMw9zIY2zEGbCu7r0StxDhs-GisSxqLRmxcHCFKjofoBQ3_d_mwfrNSrXJQyXkxJ8XI1qWaVIX0YEgYr3NiQ66U-60fCL9nmiJdhiG0pRDwHzDJg9rglpB8MxR2xriwNVHJpUut0MoCxNX_0XioKTADuGhp8Ff5Lp4XPSgqq-AHcqHIL0RWVlLvDNnnGeLA5_55h4WD_VPQhJUPZCkA7ONJ_Tz7dPWM-pysMznpRXE4FgoLWg33TpEbeVTnJaIu81MSXc3u0wf5bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=wBsWeI8V7_HKBOGLt-IKlDeuOLQJmv-4EeYubB0TN3NzoQaf-TeVGfqdY7Pww_Lqcwog0vwzn4rmFmQ9qRBECNr0dgtErLiAOEbiXj1-Pe8nVwGtzLcUfwBqXekb8MfzxS-BCmvksnWU4Yp0WdG4-k2gnKY-6ukfvmmXgsFTYBE_IxyyjaGjbXdg6dlWvEoW6rU6IW-c7U-iv7STXtitHcqsfGEbqv0cVqZbKgOlHz5_4Tn0zOrCuXKZmW0ekp15ddm--XR1Hba4N-4HG3I0rY266PC9TM2NyQAA9JDtlzRpSITY9bJ_XZLFgCjC5euUvYB9CtBLy-B5ZcPmDzXWqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=wBsWeI8V7_HKBOGLt-IKlDeuOLQJmv-4EeYubB0TN3NzoQaf-TeVGfqdY7Pww_Lqcwog0vwzn4rmFmQ9qRBECNr0dgtErLiAOEbiXj1-Pe8nVwGtzLcUfwBqXekb8MfzxS-BCmvksnWU4Yp0WdG4-k2gnKY-6ukfvmmXgsFTYBE_IxyyjaGjbXdg6dlWvEoW6rU6IW-c7U-iv7STXtitHcqsfGEbqv0cVqZbKgOlHz5_4Tn0zOrCuXKZmW0ekp15ddm--XR1Hba4N-4HG3I0rY266PC9TM2NyQAA9JDtlzRpSITY9bJ_XZLFgCjC5euUvYB9CtBLy-B5ZcPmDzXWqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
