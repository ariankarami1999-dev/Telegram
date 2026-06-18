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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 14:37:40</div>
<hr>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDPUKyHHYioBeobAF_FBiqwj6fS_xju6xNXDRSUfat3VzjDKtZDxp2j-OtGRpwWrCRsld6WQUnb52VHNswBTVWoZ6HYMV8RQ79FQpjDNvgO4mIjyXYxfkRzy_Td4w7VUV9Crw-8ipAax0xpW5b045XmgL0AqAxkNX9tYlMG13w12gZzpMHrM3FQ1MGedrC7jJTinKv8L50sznVG7MkGaDwYG4QlMjkQJ41xsnkH0rG7omFdFjnxqhm7dGoZJCfh8oVuvY2cqYPL1PaUAGHabv19BuYgubVN-pOq_TLy3rRa3iTPMMNtI89nk6rCtwnNe7iafuLDjLNus0Xbw6hSyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYwsTfVckdui6X27eQmEuORjefB8vf3SxEdXfPDjvlwOAG6FcSMLuNOWbOlxweZa6P9gnf3YhjBvO-RIYXhhRaTKwC7HPrtj4gXlA09lIHju6tSQQCxB2Xq2bcRF4OZ622BdW5zJG-PkrVkcsBwYXLXb9QLjjyTbUXaxX4AXDS0EDOrOCg8lCtXzT1Y9JLMW_E5rqyx3LjnTRFeXq6rApmEmOC7d0j58DB2mOHQdvEmpRmKHws3wQUWL1OV5JUclPLiQn7AuijEgW5iNMHZuEu5iDw8CxBgUMXZBkGlfohEJtDokCrwBiJG3moP2V_C5S9JnaMQdOwmFsFMQDyKbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UP1OQZXMlBAqkFpy2LLUBCgV44cbR-pDocMzLAh8jIIxKGyCT-KofOjEvjXcELSuDnmEHvMJlXDwMkWU4g1qgSZ5YIu-henkAw7oCx0fhKvlqgSH84geZlyv-ojSVgZ4fHvFIgp6Gh6k5FGjfNXMIhnyGDW1BSlfXOgv-gTmKtY4nZVs9HyzHEUPaUNQ31aUYOom5PPmrQ9oacZZPZZ9G4ymZtb4mlrmDc4OQ342u7bnsxBxL4_bGdSIy7PbXBx2mGeYLDDZB6UfAqg6exDxjGSygVFvPUv_v1A9h2gm0Qg80LSsLAiWO1V9MYIF92LYNXO8qmGr_C3MhKZW_thSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=PFYVTojENTp-rtSRwmrybw8WHnFblqXWtxa09dp9EXczhG6vLvxtVsqEotljqkXaF8cXfo7U4hT0RjpraXSD1V-ZS750SinN8Pandu263YhTfTRdHqHvIjOtEoY-H311spWSktt9PwrIxmTxOh90KqGOqGvV1p0pNiWTviEb156_KNGzn1wyMn4yE19ewGcXPX0m40Z7dlsGhGi9vUKUndrulCQwVTTwSvnAzPq3-oPp1OpZDEJYga5ZMQd9afzXFsidtQN4I65o4Y4kcIkcl-0N0VbNv57uXn5kcjoa-9R6fCaWbX-mR-mQWIKdFqz9ed1dK8BGGQwPqJTPQqP6pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=PFYVTojENTp-rtSRwmrybw8WHnFblqXWtxa09dp9EXczhG6vLvxtVsqEotljqkXaF8cXfo7U4hT0RjpraXSD1V-ZS750SinN8Pandu263YhTfTRdHqHvIjOtEoY-H311spWSktt9PwrIxmTxOh90KqGOqGvV1p0pNiWTviEb156_KNGzn1wyMn4yE19ewGcXPX0m40Z7dlsGhGi9vUKUndrulCQwVTTwSvnAzPq3-oPp1OpZDEJYga5ZMQd9afzXFsidtQN4I65o4Y4kcIkcl-0N0VbNv57uXn5kcjoa-9R6fCaWbX-mR-mQWIKdFqz9ed1dK8BGGQwPqJTPQqP6pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=RI2LVf0juEZKlxEe8fOyUxqso8ZpH6MvFn3CXezzSwiiGFIWn8gngzWm09NQWRKhmClzqfA00n2pYx3rW3cHuioc_G270kGoV3ETw-6cPFB_zKuBsroywsSJcMhcyscntgslErux9BO2vHMn9wZFDUHFp370RRjkpc7XLJatTg5mELkz2cmNUZtbT2EdMvToJe1NDaklzEl4LtanMlFIrmEwjid7dJTHYQjd3IvtQWnFrrGwV7fckGuHEVYcQol-fdNfIbWFxlX5ofYYDZeHe0O9cpbLACvZHx-TOony6UPyIGnMbG09dXUbKZYcuduAaMx8QA0U9d0bAp26qCLafw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=RI2LVf0juEZKlxEe8fOyUxqso8ZpH6MvFn3CXezzSwiiGFIWn8gngzWm09NQWRKhmClzqfA00n2pYx3rW3cHuioc_G270kGoV3ETw-6cPFB_zKuBsroywsSJcMhcyscntgslErux9BO2vHMn9wZFDUHFp370RRjkpc7XLJatTg5mELkz2cmNUZtbT2EdMvToJe1NDaklzEl4LtanMlFIrmEwjid7dJTHYQjd3IvtQWnFrrGwV7fckGuHEVYcQol-fdNfIbWFxlX5ofYYDZeHe0O9cpbLACvZHx-TOony6UPyIGnMbG09dXUbKZYcuduAaMx8QA0U9d0bAp26qCLafw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/re8Ivd1acJr2AYq_VM7tBuV0osFyLtc6mK3P245ttOu6Iq2qX76CrvfRCjBeqGzRuFp0QFj3RH8k0gFxMAZTGrJ1I19OFWVpaWxRrrlRAuw0p8l78rRk3nhQazHBXnNEHr2a9DqpwFos-ADwLJnvCNYCqQTT-ey2M7sDqj-KJdKgUzN-WMl8oSXrc8gHUjnty3LQsfP68x-f1-c6d2tbS4fJ-DG6T-UMDxZxtslrKxFaTWHmMrYPxDJZFJpRvEBO-8Drgiqbl0iK06VDjyPApXY3CgfxcA7oJflirROvqrGRY1LuwZ0feiJEkLq8FoKFH3kb3DfTcTbbHHoANP03TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=eqPeDj95TNkx-BDcuhGDCT5Sj8IcT3fswfrVXM4_u_wS36yGj9qkYPr24VmV_zpn1U2iYehiSNfHdvvjMjRa1oqJSVw8HwA1PZOOTL0CrCzEpl8sN5JSZeZZG1xkdTraxzGc9TcJipy2GE6td50o7M0cF_v-Nfs4v_pGi1lKaji9QOCzHgd9XAGEME7oGlz-BlJGf4j0TnkscDoiNkB3FzmU-viM6mPJozcG60pq1dIxlNw1ASSGMgbScJyShx442zO-WrSK0lNefcX3YyKinIq9GrIopWg2lntYN-UgmtyvE5wZmlEwSw2NEKZDRsscZcghqn77ANTVx9N1vdlicA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=eqPeDj95TNkx-BDcuhGDCT5Sj8IcT3fswfrVXM4_u_wS36yGj9qkYPr24VmV_zpn1U2iYehiSNfHdvvjMjRa1oqJSVw8HwA1PZOOTL0CrCzEpl8sN5JSZeZZG1xkdTraxzGc9TcJipy2GE6td50o7M0cF_v-Nfs4v_pGi1lKaji9QOCzHgd9XAGEME7oGlz-BlJGf4j0TnkscDoiNkB3FzmU-viM6mPJozcG60pq1dIxlNw1ASSGMgbScJyShx442zO-WrSK0lNefcX3YyKinIq9GrIopWg2lntYN-UgmtyvE5wZmlEwSw2NEKZDRsscZcghqn77ANTVx9N1vdlicA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRkNt9P_K0cLX0X1iCZoQfyrbNeOd_JITf75SFDcR1lVcltYSUOBfL7nSm9u8yzj1LlAhpNTt7Zm7wG53cl8PGIUGKVNZLLBYSNStKSZ0rTm1cvJR6lkRS-NE63ed7WZqWQ584z56Fj9tiRjwhGiQ0NIBagqU3Ip19kHXNu7LWcs1Q52OWwuslV1-OKjej2vrM3iixpL_s2iMM1pw9LYwIlUhKFggRnRyt6j8-qSQz7GAYSgtyRkc1GBiytPfid7m-w2UgPEYWa4zDMWTGHi5HLyWLfetuG8KlP-bs-oh0cnqP_AvCushNna2NMtHtkT6CaSMVBbsCbBlHgcn_y2uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frfbQ2YcJtmF3QIHhAfCr3JyN3RGLMbFhllZeW2eYS2KAVRO8xjpDlUCxIJdQ_upqNhYsJLYD3OXQm8CVou78iOmRJeC0El5gT35OVhMrzsljjQjyGKjRTkdq5N5E6Fa4UXbaiZD3r9MkIop1F_eJpzqwvioOFdP-IcYe2Xu1WqTGqZ6mII-o1uj7IsgYHeNySUfqUVArQU_iONApc3Yi5DWf7xjYnv5xO2vALCbQo35LSPipkhLKRB7SyNVCh33fpmZefxtCINdGzvBly9DvEmsBCwLsLzWIb4ZnH87ebXQc0GNJ02Upt4z_QYCAZ8E1YSiXQz0exEExYsDMaMrXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQq8mELmYklp0dhLKf7XEUF83ZgYw46tR8PbuEL7BLkb8_L9WwjS4JmTMSVUbIHTfwHSEECGLcotJVNx1ZpNt3rdzG9prp99TTv4Lgy043pbenOW1Ht3Ea4QhQ13GFTQ6npAGjf5eCwoaG6tKrCzYQV4fvMCYMuCy9ujYue5JWGizC7C3wM-S4LXNQJ9wXMWf68VYZdg0lPIHm-9LVwJlckOE5KQ6HpCwtpqJETEu9G5RDqmqeFW8gzsKre88QGGlIp3nJr9MzIfg1RdOBBTjka2DRT0tKvMarUV4qkdRWvZ9dHLhATlRCWcw0nXlzhbeJpVt75xpq0SyU7MvoOSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suRScTpsGKwVpD41FwjRpJfwPefP6OuoeVo853ctBmuqNzIvfH3NmLtChZZU2CQpxO9kDnH3axCzOSvq0fDQzj-H9alfS46BNKv7CJQtAHUn2OSrcdoBcj-l1vMUBBgHIsIQbIACbPvJlp6lTeJ9QSYP6U9RwAg5lyJG38aEZgUFxTpKGIYV8UScCETjbPDvBjHlkGcjSKhZDsL0X8f9ciimAnzMsTChb7FCR-AOwezbP0Uo0ca8ZfSE20YSIc5A_5HlGhF8u5BfeZPox54GZT58heVPgXKcjzBKqNJAgy0cjl2Tybq5Q8v1iwOJe2nxc_AFs69HuJKnnaVp6YeP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=QX-plbSv3xufIbsJf1jnt4zaSKcmpWFm1snpxjXO_vAt6S9duf1C9jz2RVuoco-OWS4triWEro9BmOgHrwlMTNMKmcG4LHzy4wCk8QzMcTuc2vxtYGKEZvHJPj3pXXWk2yfujvjTTV7uIdjlQIJTY0AqEaHLGSUOigcS_5YLUXzEmFuKrthq0wZaU_6KSRBZfSedGTaAohSzLnYG-HEAvUczDRvmAjMbvH2LWxOnUbhuPaurqbfpIir81Tq9op13we6LEC8g6BBVpbIyph_-OhXphuK7QhcFwCoe1m4x_YRHD7vzVSAvYdbhUJc6XWLk3IErNP2B7SZ-bseFs3YvNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=QX-plbSv3xufIbsJf1jnt4zaSKcmpWFm1snpxjXO_vAt6S9duf1C9jz2RVuoco-OWS4triWEro9BmOgHrwlMTNMKmcG4LHzy4wCk8QzMcTuc2vxtYGKEZvHJPj3pXXWk2yfujvjTTV7uIdjlQIJTY0AqEaHLGSUOigcS_5YLUXzEmFuKrthq0wZaU_6KSRBZfSedGTaAohSzLnYG-HEAvUczDRvmAjMbvH2LWxOnUbhuPaurqbfpIir81Tq9op13we6LEC8g6BBVpbIyph_-OhXphuK7QhcFwCoe1m4x_YRHD7vzVSAvYdbhUJc6XWLk3IErNP2B7SZ-bseFs3YvNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftbUJRKY-PSOxL0AVsnq6cSwPtnXIXVUX3MaLRDcN5e-OHdyA34Lxz7dux-6Fyr5lZBZqHXLFJLE5m5wrna9oQ98FAsEkpXIyH7oG3RgG26RrPAdCVVLBw9F21uH7BS1VQ9SlqHcCeRPGugDgR8LCxQmIsvFAJ4Pqu2ZrZDnzu7IwSymkvNiNjDRPt2MGato2dip6fiL-FgG25DjVuaeztn82V3mwBDP13lAS3ZzqwmYuoCoiM9ufRgKQOGP2GisuCsApK29qdZ8tOFlYl0MDKPpUaMXWYqgBBEr_HWaUZr5rmrdU7-JNejg9JfEpl9VI8uD5ljJZa2DyE9n5mEjjujI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftbUJRKY-PSOxL0AVsnq6cSwPtnXIXVUX3MaLRDcN5e-OHdyA34Lxz7dux-6Fyr5lZBZqHXLFJLE5m5wrna9oQ98FAsEkpXIyH7oG3RgG26RrPAdCVVLBw9F21uH7BS1VQ9SlqHcCeRPGugDgR8LCxQmIsvFAJ4Pqu2ZrZDnzu7IwSymkvNiNjDRPt2MGato2dip6fiL-FgG25DjVuaeztn82V3mwBDP13lAS3ZzqwmYuoCoiM9ufRgKQOGP2GisuCsApK29qdZ8tOFlYl0MDKPpUaMXWYqgBBEr_HWaUZr5rmrdU7-JNejg9JfEpl9VI8uD5ljJZa2DyE9n5mEjjujI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJzUxiy3DW70BydNAfTtmCc4qWjKcXqWxdle4nJq0VUF8xuBmkI2gyByN8y3DT1eiBHT__RLYjtItJszRTwLTXxpVE8zztAaSmj6npUz_M5Y5zD1HDoyJRSqeJrczEm5y4szJsOuq50kduqBohoGbcl61WlMo5vpVUu8oKf3gIk2TAFW_u1i4X3sd0PVDiMqs0l4c6-BwoYyf1r5GGRZIbAhvoQX6NgDxj7g9iiwQeE-SlKBeGXblE5ci3A1Vt2GYqmHtSJel3oZEe0oKA4J5ABWvE3aHz7kiOaIoklBs8yym-WWmP6FCUanXDExyJV1KF8JLfgCMRLvKmFLfECXaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها
محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار
جمهوری اسلامی و نیابتی‌هاش رو به
«اختاپوس» تشبیه کرد و اعتقاد داشت
که باید به جای درگیر شدن با دست‌های‌
اختاپوس در لبنان و غزه و سوریه ، عراق و یمن و …..
باید مستقیما به سر اختاپوس کرد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDY3ttWZ6QqcFkVSTc-wMdtb-4NWDdaw_G61GY_Tl4hnMw3fvxpHkCvaaXyZESvzZk_h8rPBFcOv8QXvI_HMSbXjsj9pfaQeGtc409Cg34vuVPQ25d46866KeaVYkxWZPy_GEdJ9YoQKtJMTeV3rR3EQIN92sO3lBAKLMiL8OFN4crZrmN3v7Wurw39aAmCYGD-58EtIzc6oOVxzv4WPtzUiU19YqU6vEPld82FhpoK8uvZqIo7Wk0EGv68YuE2_w3DSB5Tief58rrdRTStYK_GJSBJHXXWHMLXUvM5r5qecmsDyHQcH3Bi8y6xwzzUflIJDx_pDjOx811Cxbhvm0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RlKmphYRFbqVMvf7Q9bpzHi1ev4uKc_OjUcRosmh6c4_Othd8HFC6aIY43W5u72vsqdBla4gTVhUfynQtePh9C8yLwp6e3GDR4fFycxBJfhDl3tzUmQH3hcnkLyXTLTRR-oHl5JPwsLTYdnbb6LKort50POR24VgS_kcbRJ3cnVkreTbHGxrCLDV0ttkEZ8hWumuK-BR9hPnuB_ahp50nz-WyqMrN8xT0r8R7OqnWADK4sOyRz4pmb4qavk28tpJMPQhKIAAm1XCzJBI69bTQn1A77aBVB3Bz3GgdXPyuLP1S_lw1nNnByi5FoDilR_dDQF_lEHQV-2N4z5aFJQYgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3oLd1sO2E3D5WQW_YjfMALM2G-yW30QF7FyD8lGwlKKPzmjhRH0x70Md2axneSqM6GkNV-xEoSi1F19NxVVIcqsEz6_f0tOrDW3mgtIA__KjLsoPEm28wsP2IcUdYpKwubpItfOuerNvbWIGZf_qe-nXyzOZ9v2nxr-7VXtAu8nNNSJXtGUmxiWaUtiWoei-lHzWJYjJPJ0f02rFze6dHSEHTO5OBdpfqTxrmz2FtYgirkDtsYaQGlcZBssppCOiOaXteeALTCkDQIOuR9cdoGw8EjQ3Fm2-67azNZ3hFzwJSopUYRPM65jpTSHAmeB6H1bzjPcZBDV-NHVvoFZ3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8vR6QZtfy7mHk0yCEMZxHgdl64dyiHhq3nojB66e04eQZB55Xg2RTBuxDjiuFoHnDFpQ3HUnUIwkHVOJBvuR6T8vKSLfhT5W1hlQQ9Wpk-aG6u5ktHMKQppMNrnnwDFyghrjI-nWM964KSKJj1RVpeg9j0E0mGVEXnyaNKYnSHzwEg-mEsBl-AU4Ym8Qq4lBbHNv-yZEYAB2PpQWzI_jD0HnlJ4lC-ZKup2HpSw1yrEnUD3kR5WCyK7UTrIsQbyZ-ibjSUBxcvfsJ0UQLqxSWB8iYv_4Cgj-xF35r7709l1vznJzJiV9EQv02jYe2kfw40eEt4lNFDMk4ngwvgROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=bJi7oesxp9fepcpZ8qQqBlXaOVUz4Ky5hKDw15vPANolpd1yldqZ3qCklwLRM09kdD1me1QbpaXUC9E7ifKBzL8Kmbb2eUyy16Lh8Y7R9eZRE-bSV6jbxXmXYHtEayAV2Tz8I_OMyKZxb3Bu01CBEChJb_Sp7Avyag652hekET6dKcEFMpLRjA8JsBcmv6uKDKgqfE3cC4OigKnvvSSFy-a0fvO3C6Gj7CjBOrvD3q3kHlaslfB2HU2z0yriWJgtYT8HvlAI-4gG7pMtQ7FRdCW23IRQzUBB20jDITH_eTJgqnp-fJbMKbr5GWg1DZY5o9tILglmCjxKjhwtKpdleJROutwR1ju0ZIumRFU1JJTdaaF7FDeii5EkA4C_IcIGqh11kFq1vsKI5moSTheFy8oxZ92HQ3hPzq2VezTh343tJQx7Tvoqczvse1U0TuPBkX_CxbJoz1t5JYOOVUz39J9XfzaejbABaDexBKBD5YPxN2HN5Lnan7XoXOSPOdkkxCE95WVhbqyoeiqxQB0-_CaEQEdhhQrU_kEyxoOPwG0-uaJOL0jhwjMvfCoq3-cK5fpyCXbfwqXyVz3bk4kgBEoOZFuT8Wb8En4uVXvFVyyoEZImezhQuoL_zNsF9q8o6eZBrwwbgJjrkPfTVKdzCrUqrXMskzJsAm5GZkLjmmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=bJi7oesxp9fepcpZ8qQqBlXaOVUz4Ky5hKDw15vPANolpd1yldqZ3qCklwLRM09kdD1me1QbpaXUC9E7ifKBzL8Kmbb2eUyy16Lh8Y7R9eZRE-bSV6jbxXmXYHtEayAV2Tz8I_OMyKZxb3Bu01CBEChJb_Sp7Avyag652hekET6dKcEFMpLRjA8JsBcmv6uKDKgqfE3cC4OigKnvvSSFy-a0fvO3C6Gj7CjBOrvD3q3kHlaslfB2HU2z0yriWJgtYT8HvlAI-4gG7pMtQ7FRdCW23IRQzUBB20jDITH_eTJgqnp-fJbMKbr5GWg1DZY5o9tILglmCjxKjhwtKpdleJROutwR1ju0ZIumRFU1JJTdaaF7FDeii5EkA4C_IcIGqh11kFq1vsKI5moSTheFy8oxZ92HQ3hPzq2VezTh343tJQx7Tvoqczvse1U0TuPBkX_CxbJoz1t5JYOOVUz39J9XfzaejbABaDexBKBD5YPxN2HN5Lnan7XoXOSPOdkkxCE95WVhbqyoeiqxQB0-_CaEQEdhhQrU_kEyxoOPwG0-uaJOL0jhwjMvfCoq3-cK5fpyCXbfwqXyVz3bk4kgBEoOZFuT8Wb8En4uVXvFVyyoEZImezhQuoL_zNsF9q8o6eZBrwwbgJjrkPfTVKdzCrUqrXMskzJsAm5GZkLjmmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2_Xi30DSOm9LH1HJJhLCj_kZNiQGR_QPVoTd9ufnYYwyUoHINOP3j4IqefuVvV9yT3uh9ME3MVMEc9hqaXA6mDspOYNGqgtukk_p4_2rcVtAYFP7sdp9r92OIIqUeta1BHjbDJSk5YRTOvuCsPX6T3rdwu1iWg4xcXzRX_M9s3P2UXnvkKpM0-RYH39G1ZksGFKZFqsvzfgczBJyG0Y-qM5aAb34buY0Dw2g3nlu6yj9MvHLa6KWN2nMxWrW5CRKZDNf6sq1znzQ6a6S8M3oI4trmMR6GjytdJ8vdaCbzuztXtkg4eRbA7RcXSZs5ff8WjT6dsihWQALXUpujWkdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=RuHNQE18wy9SzIp_9FqB3KBZ1677w954vpKctFQpyC6668nPmw49l-r80cZ1uKdugvu0UHhe-BzNSJQC0MRUea-AgiTRh6P806VWlwjLmfevs1gLeS-W0mYSBsqput6XqkkZO_oEajD6z7QOep-C52n0c2youUE1cqS2fEwJMMgYusq6MM_f3biLHznfp9iOyTvPsDhV3ozwfNpGv4K36OQCRueJZv9iRIU3SK7SxuA0T3Aa5mFkDTSTHNvwM2t_AfdbTCkodwGPYXNA8I5o_USz_1BnzEoVVDLs7Ql4w0jNwCAYoxCZUYM2CYD-lzN5i74x-f5VrmYMu0iEoHFBwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=RuHNQE18wy9SzIp_9FqB3KBZ1677w954vpKctFQpyC6668nPmw49l-r80cZ1uKdugvu0UHhe-BzNSJQC0MRUea-AgiTRh6P806VWlwjLmfevs1gLeS-W0mYSBsqput6XqkkZO_oEajD6z7QOep-C52n0c2youUE1cqS2fEwJMMgYusq6MM_f3biLHznfp9iOyTvPsDhV3ozwfNpGv4K36OQCRueJZv9iRIU3SK7SxuA0T3Aa5mFkDTSTHNvwM2t_AfdbTCkodwGPYXNA8I5o_USz_1BnzEoVVDLs7Ql4w0jNwCAYoxCZUYM2CYD-lzN5i74x-f5VrmYMu0iEoHFBwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=szqj2EWEmku42NNqB51AP1vcz-0WLBfKfhMfDGWajo4bdmxn-rCD6Dd0eWJsUfViLQaYlhpgQWQeD-vfpYi3Mbe0tHl9sQejE1vfTC-m8MdC39ojGfl4TEZgw8zbUjEazg7X_iGSTUPQb3aqa9JGwcq8JSfJuvNE1D-eksd5MCWR4nlh2zlCY9RantqvHRUMiCU21sfnuE54-izy-ue4X5Vujoe3qEfdd8r8OwvyTIgN8p59mY6EPc0bUWMpILxKPdP3-TNZam782tnGaSNVREfJZhNoojfsdtISqk1BAvU8Y8RNtM121NKJ5saGQyJ56AEILyQGeMcH4bVCS98lL4RN3MvMXvY_a7ZihlXQlHPkIrP399-1cVx_fMRctN1ooLt3zhBwAfQp5SrUMHIGEqHC-R_h0d1h1PlmnNEiGqJGH728FlZ_8u_mw699-tapVdr4lA3yyePeJ9T7hqb9kd3WDG2JswCgHSDrsx6tdVG3KDl0QaxSSO2yTEf50iS6xTlxVwe37IQ-Ks72kw5WNr6ILRSfQYoyu0zId7QXH4vnfUW28-Z6PpZjZhFV8jZKOm2RfPNzZ6ga7XlpxU2jpe5xATe2IBbZUBQ1PgLgJA5ql4tiysij1_EqCCwO8q3dMIpQG_Gb5v6IVANun35IFTQSO6SJTAr01dAnHL-koSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=szqj2EWEmku42NNqB51AP1vcz-0WLBfKfhMfDGWajo4bdmxn-rCD6Dd0eWJsUfViLQaYlhpgQWQeD-vfpYi3Mbe0tHl9sQejE1vfTC-m8MdC39ojGfl4TEZgw8zbUjEazg7X_iGSTUPQb3aqa9JGwcq8JSfJuvNE1D-eksd5MCWR4nlh2zlCY9RantqvHRUMiCU21sfnuE54-izy-ue4X5Vujoe3qEfdd8r8OwvyTIgN8p59mY6EPc0bUWMpILxKPdP3-TNZam782tnGaSNVREfJZhNoojfsdtISqk1BAvU8Y8RNtM121NKJ5saGQyJ56AEILyQGeMcH4bVCS98lL4RN3MvMXvY_a7ZihlXQlHPkIrP399-1cVx_fMRctN1ooLt3zhBwAfQp5SrUMHIGEqHC-R_h0d1h1PlmnNEiGqJGH728FlZ_8u_mw699-tapVdr4lA3yyePeJ9T7hqb9kd3WDG2JswCgHSDrsx6tdVG3KDl0QaxSSO2yTEf50iS6xTlxVwe37IQ-Ks72kw5WNr6ILRSfQYoyu0zId7QXH4vnfUW28-Z6PpZjZhFV8jZKOm2RfPNzZ6ga7XlpxU2jpe5xATe2IBbZUBQ1PgLgJA5ql4tiysij1_EqCCwO8q3dMIpQG_Gb5v6IVANun35IFTQSO6SJTAr01dAnHL-koSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=oDH6k_FaLXCQcbGXCUT-yAzOgL_lJXESPqs5BMCKukzF_vkSf-kcVb3gVKJpWVeiolkLFGlb2_0ieeD1PK-MoD9jpVu6moAJqr_idL8k0sVOo7E13CWSbOCFzhPsPBbfDZx7fGeLEcAOOUsvVDCrRlp47LdbI3VKYTmkByBXvY7HC6t4lVUM-aZSoFVHp2Gsotsy8bATc2CECuLZue1IsLyeXgl8OWlBzdhvZ7_NK23IEIn4ES3e-2TpYtjO-_Isvy2YROiVdGSJJxNQrsvgcKgB-c2YWUttt9btqDAvj2B_MzKNmbld6oXdF9z_Ux7znd1jjVuUjvN9sSQbNyZ0vYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=oDH6k_FaLXCQcbGXCUT-yAzOgL_lJXESPqs5BMCKukzF_vkSf-kcVb3gVKJpWVeiolkLFGlb2_0ieeD1PK-MoD9jpVu6moAJqr_idL8k0sVOo7E13CWSbOCFzhPsPBbfDZx7fGeLEcAOOUsvVDCrRlp47LdbI3VKYTmkByBXvY7HC6t4lVUM-aZSoFVHp2Gsotsy8bATc2CECuLZue1IsLyeXgl8OWlBzdhvZ7_NK23IEIn4ES3e-2TpYtjO-_Isvy2YROiVdGSJJxNQrsvgcKgB-c2YWUttt9btqDAvj2B_MzKNmbld6oXdF9z_Ux7znd1jjVuUjvN9sSQbNyZ0vYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJlf4h1GifXheDIBK6ucYnp-UxMeTjJxKlW6vLMmGvputHVLJzl4FL-qG1lm5WzeUEeiIDZRrEquO-mu6scDiFEdXk0-DzriqoW2EatUkVCU7IaAw4dMpFT9ywCfq8NPRKJAx9U5nqjZ6OZqu7mlExE3zteiOqBC3lQI4u-U3iWbnT7eloRHIgMqN-7JJaUj6lWSxQkHV5oCim5er2o-r75H30ONuPT33aohCzvk7Sp2-O9A_CS3KQ1U3OaQppKR8xx8b3jfdfudo66g3hVcdG11WiEjTo5CfK0ujTktvZx6bEORwxYsY3eYZ7nlEqdvJOWHu0_jgAkhbNCSJW-NgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BLTEAF8jZxPvBz_WrAo2zmEU81ptR0evDMjImbiyv9ImEK4UWiJ4suoUr4PYRhdG6DqDQta8X3tOnHTzCGYh19em-PRAdT9cgO-CSuz-l0Kaj2MumHc92Bis2et06uy-IlPq53crunkQCBCq3BN3FJ3p0qXXP0jysBY96aFRK5FgHEJBzSi6eyatLqmIWBrnEcEGwp7D-OR1_NP5iLapfmYSzjRi_9jcoDWlvfl-cL4zNo4608bov4Jwr3bbKDBXSchdsZm5ig-NZTdZBh0e3Wc_MQqbmFnem0_Pv-zwzjeEX3icB5xwPRusivXmfJlgmAeT3sLXGKwo2bnCrbGqKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzEleU1hAttKHP4OfemVTrGtxsssCIpGeK8I1jLCEgpfGpJ-yoSid0qI4fFx5ykOSeJzn03rXoYTjvI55MCh-iopJZrXbQZVyI7XCTa-azkzmfI1td8FFNMDQ_pk6uUrVg5GlZjUi6AkQRkfb_vw4A_A43eXW0cr8UYj2nwLKeAED1q-lnhlgHLBxdjvEEwqqau0jGr2vCHfAP4fNjNkNisy3j4FYNixXuGLN0ONgWGRs2AX1I4XXwnI31B3GjkEYSrKa7tge5VBeKGhdufbEZfD21n9uDieNs6uv1JxDqVXETBbF9fv7OHPSnTeBg23_8-BEz4HIQuaz-djrwPQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3KsGdj-ilR7QlKFARPHD-OaNb8hzL5tH9lkxR8YN1AOzWI1E4lMJCX__IaQEqAZBxFSsoDiTdYfBD-geS27cSLy_nBbHqbn3pXzkVNMK8fihwijwLXSrHocI6iOdQcNjxHJzC7vACqnXNPtjN0LruGVg9m3DZ7Gj6M8_tTjxdUSYG6ej6KmQ4L_Nr4jpruS5bvYQy3ghk1ymlWm_obmRdxhWs9JAzGR8knoBBccjT9Z7FHdlto3yEa5g96YA-ECHsOyj-rVZ-fHuy2RvPAIWEfzfcgPhjE5jbs-p_nZf6hpEFC53aIqf28d4qdM1yDTKXdFAc8T029hR6BvX-Sm7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMmZmKxPrWc1LG_IlFuVofoRILARHxUCEKYVPBwOsyoBvtaUireMkd4q9Sj1yCOKuWSKh731jv5XJ2Bmh0_JU2XVjzg9Yi5_rIFpKJYkbwds6HSMTF0woPm_Cd5lz6URSRD3F4rXnVgM5L1NETFdcyJRt1Y_EzfzQhOcuyr2eNtmZMCvIWDmEjF0SWazPUavgFqfyyuhq58oNX8fFNJi9jn6O42vPA3n6vvmb-38HjIX-kbI0-dYZYztvfcxgni60H-ScLjHacuoo-PdqCyhH1HocgESLxk3u7TWIL2eUD5tEYn2W1NQQngnOvhzvRA5fvjxcNuUh2LVjYM99jod0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=VXqN5_xFA2ZUXJaXZaVrUoxgburzPT5RnSErRvc1tsAKZxAfmNQ-Zj94ekmq2vQHyFnREve0WUd3tB4o_6CxHEHm4GAEJTuTuk6Xnn5MO8rydWbWeSIrXDO9LzUhpdWurLJtSCy_Lb7ccDQaH_v6XL1IhgOAmPxDu1c65DJjIbn2q5jDE1DkEWmozcJj_gSuxVBGTnN4ylT1QFW92l2uFwFS3-_zthZv2ub5xsuTm-dJsvJG-lXc0bfG_up0hSeFKPGmM1yFyk8D67bKF8G8SJ8ZkrZxaAzCzoFOiutgmqTHAWeVauBXojh4mElCc1a8zj2GBHrKbQ3WKHI3qpOK_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=VXqN5_xFA2ZUXJaXZaVrUoxgburzPT5RnSErRvc1tsAKZxAfmNQ-Zj94ekmq2vQHyFnREve0WUd3tB4o_6CxHEHm4GAEJTuTuk6Xnn5MO8rydWbWeSIrXDO9LzUhpdWurLJtSCy_Lb7ccDQaH_v6XL1IhgOAmPxDu1c65DJjIbn2q5jDE1DkEWmozcJj_gSuxVBGTnN4ylT1QFW92l2uFwFS3-_zthZv2ub5xsuTm-dJsvJG-lXc0bfG_up0hSeFKPGmM1yFyk8D67bKF8G8SJ8ZkrZxaAzCzoFOiutgmqTHAWeVauBXojh4mElCc1a8zj2GBHrKbQ3WKHI3qpOK_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPyISZMLzo-G-OzYxShJFnCR_u6yTmFDT1KeaXc_bmQy4kwUGknGYorRbluimoE4hnT7SftcGk84raHT0tujH3TZuxRkMvheognt5aeHNRS-90x3Sf2F0YTSN8egBJoKKMeWUS08J0sx65XATcJ6q2yjRKYD3ZYV8XaHjt5csF7rwkYQo1tJdhO44T5EPR73b4BSf0qInsBzCnz2zfvpRrtBgBNBIudp_7c75QfkIvumb2A-nRcm2D8kSuCwgH5nRDyw9-e4RkMhwH2p0kYdPleS2Q3ZknpFH9GhZ54cLtEyYxFi23X-WGFUoWikUIvtyZpSDmQTrpSK5kwRnZL2qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrBhw-ud4XZ33Nu1nC3_Sf3ShJaeHuF7bdvjFO9kssKs-uZLpbCtQTpeYxLJFxQYvwIIeLp6E9PQEK9feU1KpNb0uzw3hkKysCi4XZMFf_Fk5981ZvnrJv1Dl2fkqP4Riqv5X7mEVASzT7pk6_LQx9nLDzb_Fank_v67i89GG_2iLFVOztXAyI7dZ2U0YF8wxkfTwYJHqaMcfQCMdEd__aSo4YMcYt5PQ4AqV8Iq60Qu5xNSPJywbhmzIyd_WWKvd3WW3f9VJydEzHPx9weXVf9dVdi5Q2umKxNzLkuIEdD6kALADIo_ySpoVskinC3aHz-x-wb-Gts5Wg_aIu07Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTUot6HlgWPOvv17R0dtwS_LKaZNeC1MT81jv0T8P573iQXRo9O9QKJDfaD9A77Li82yQrX3hIyw5450VXdHxSYyFXjGKZIsRNobUq2Epe6kv5E9qzAzYTcIk7h9pcXOQzow3zyrmZb2E4MXcBS6TE-B-6JogQhXqd6XdBTAPgTWzJEjvXIOvoXhHnFXZhac0wf8zg3QnHYg-axTExWELvYa7B4XPJpu-_O7Mw-UC2z2WPqQZMISyNRQ8SeAlZxP7r7VaoOM_XyVjX689MSLACUo8ePf0hV3Z52FSz8hjj4zOcN7v8ztCqWz-VZpimIIm86DtTTL5iKsShOg9ro3rQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkOs-v3ikbWsucEFGRYgcWBqk-ON3Ljz27L9GWXaVlJgAgoJQPHvXrWEsedwTaHMri9VCimiF-DC_NrYJ7vE0dEAxrt1APXN0Z2J96BM37fbQpYy48mCrYihHxxQky0ftaYM38upAwO35drdQsr-evRY-t6tqHGF1LVecgVKAx38iJqSigRkbOFJHlL7GNHEFGfl_sYVOt71Dh5Yq-2FAyK-HxuLLzhpClLpQ6B4H--Fp-HbyE6qUz_pAZBrnp_Cueb4SxFvXsxdEMIUWPFhs2k1tsYc3gFEML52cmmsa4J_Fd_Bb3J2Gd-wA81qAW9uZs12DLGrZxQZw8FBwEbHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TvM9rJwj2Y2TyIvQE5RyKD5K3nHF5dJdgaaeOhkNVooCVrfUFOf_LrfhHVN6UicWQ9cb0X12SmEk7LJb8FvcLhAErKJBkcKf010YaSmV3FM5y4ndKdmee0OcMaVs45BLjSjSooWLXbcPKcDZby2RBQ907zac89MrqbL8549fIAMBoOW6jXeutSANIxKpBMZDZqg6nf1O6qSLjTanEhBBzdkfMthPxMH0GrXzqFPmsBZboHiwPyDKWGBvgT5snaSyLHw2sXp_Dnkg5_E3R9Gl8-PiVC-ZMiq_UKy0WU5BAfkfKrycfg_jfNu5LltE_0GlF8iY0XdRFRpRKoh_rSGBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J-7HZKrIBcBYsqn1OIyh_yGGyjcrhnctMDNjGIroeyhUNhW_vgPaB9atOgCJdrZMZUfTBjuXombSfEL_ve9bINkwog2kXQ8OvNIytNKae1BFuRCq_9YMUydOINn5_HeHoIQ0SHt5a_h5bnjieRclDQEDL73--9RFr9cq1dFiX1eFnFjAuhiaN_cXW0RVfSpHo7y9VQt5ZUAPLEWNvQT-zkx8mWCfNR4DXCTN-hB3kGv2bIwwUv5eaOa5Cz6XqB0fx-eQoZXMmferh5UUh3lHbN--0tks5FqTjHEmSrBX3wR3f7zwxKEsvIzG8ZQYkXxWddROJFgi8MdK7YKMr2EU_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزادار کودکان مینابه
عزادارن حکومتی!
میگه حکومت همونطور که در ۱۸ و ۱۹ دیماه «به حساب» مردم معترض رسید و دست به قتل عام زد،
باید دست به قتل عام معترضین توافق هم بزنه.
اینها هیچ وقت ایران رو دوست نداشتن
هیچ وقت ایران و مردم ایران و‌ کودکانش براشون مهم نبوده
اینها عاشقان جمهوری اسلامی هستن!
اگه برای کودکان میناب هم عزداری میکنن، چون میخوان یک کردیت به جمهوری اسلامی و سیاست‌هاش بدن.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lO-ARlPcIZ8xS_P5fxyq9y04d2Eblfk5dqVqM6Y-nJCIkoGwTq7wyXF2hV_vd1jBpYqji-AC1P8EDxYkSLv06qIHic5WT81X_f_hBs472NXpIHXS8Nm-lgnPbKPQ2BrpFpSCRtdtMdMFEJb-qQa36o88fhzYcFPa6h7GgasqMUUcuZdKJArwEsXcUTSDrFwCFJu1y6zOX5i6oFyT2PEUsv8aaNHM_cFCXTcMmdCWvcTDyfVGCy00fYZIWUPOJsR2cMvzuSRdVWOD_4gC8_TcTNNM3wySbLc6vhOsb3shMwpN-kzpVA17tftw7D67jBUENqL1vyJSzcjsn-c3jqPLRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk45spyFkzXZ6tpNltxQqhcaZJhla9LmdhHyFPn9Tpm049FMwPKN7HTqmwjEcar8n1Z-tinD8QMbmKxEyYseMCKlsMbUwmYNvWiI-jgcHGlYk8TDkHP9Oy5woKaNff3rTuJq1lKAsF7nW19sJWZSOZzGhmV3WzEoQeNr5KdUuFFnAa7W80sk4c12dBwQanuUyyxlOb8qC7jNwEHOoqwORQWFr53PvYjSWED4O1_9LEwUQZo7ImbdIOxH41-r4jFAi9F0zSYHrwbwgE8XIlml7YnRMqzIjE-RguaasMEoMpSr3wzc4dRGJwJ-YyktinNExyfdfpHzX0i_s7p2M_mEHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=htVAozZCQACCw3TJ8IAmBQRVJCb39oS0KW8E3-jJrx35krbDuPQ12CLPzoS7-E2WL4N7aFN627uklm9u2kXHxB1wCn1o51s0KHSWFrvj3Rmf95uOoH16o1R5A-dNI4sFyn-dBdgO0GJJCv9yShMevUutpSHYEzuEoqCdEuuBG0gl5D2gxfsLiVtKm3zhUSoIxXWGvXQOy7ieyLrLV6lPlqMxtX9JN0ywpPzniHz8h-c4bWzUs9wvq5ZUQmlENO4wNMnagpIfm5O1aIR9l78etikcwGdcbMpZfRLVoPI7vJrJEkA2xfwXEUVMzn2OryDiT9vK9JKjGZcywqG7O7cHAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=htVAozZCQACCw3TJ8IAmBQRVJCb39oS0KW8E3-jJrx35krbDuPQ12CLPzoS7-E2WL4N7aFN627uklm9u2kXHxB1wCn1o51s0KHSWFrvj3Rmf95uOoH16o1R5A-dNI4sFyn-dBdgO0GJJCv9yShMevUutpSHYEzuEoqCdEuuBG0gl5D2gxfsLiVtKm3zhUSoIxXWGvXQOy7ieyLrLV6lPlqMxtX9JN0ywpPzniHz8h-c4bWzUs9wvq5ZUQmlENO4wNMnagpIfm5O1aIR9l78etikcwGdcbMpZfRLVoPI7vJrJEkA2xfwXEUVMzn2OryDiT9vK9JKjGZcywqG7O7cHAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=l8zbH7JyhLcXf2WNDndM_8DfzMDceFDyaUKP17tgAvOMahVSj_8HTKOOqTRpU8uHqQXHboUj4TXLzyyjd6GDTpx7l2jkKP1WS2wndl8OgCvS7I-FULeQIgmmwGPgBM1LZlg_NlX8PimEekDusP_EMRwuBVQbTJpJ6qrwPMYp2d1PfY3hq3mbhPNjew0b90EOSYyQRBPGYUerSxMwfRhFgiwbryTp9yaNsbQwxIkS-QateqAX1YBi1UO9LU3Hta48CTXS9lvauqU8aE4ecM24Qvjt_ZLvK5R2IshnkkjwYrfcRrzocHQS9fRUI87aZaQS2KpDMq6AW_uY5cFz88G_cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=l8zbH7JyhLcXf2WNDndM_8DfzMDceFDyaUKP17tgAvOMahVSj_8HTKOOqTRpU8uHqQXHboUj4TXLzyyjd6GDTpx7l2jkKP1WS2wndl8OgCvS7I-FULeQIgmmwGPgBM1LZlg_NlX8PimEekDusP_EMRwuBVQbTJpJ6qrwPMYp2d1PfY3hq3mbhPNjew0b90EOSYyQRBPGYUerSxMwfRhFgiwbryTp9yaNsbQwxIkS-QateqAX1YBi1UO9LU3Hta48CTXS9lvauqU8aE4ecM24Qvjt_ZLvK5R2IshnkkjwYrfcRrzocHQS9fRUI87aZaQS2KpDMq6AW_uY5cFz88G_cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=Ezhiwq1vSLIHE6z_RECzeu-UnUy_sslEzokBWxNDwfEwD6QgD1mJBr6K6iBHygvrE0d1-XqdcLTP5U2s2AnZvSdpadZ6W_imk9dKZoIFrvGJgLO11Yw52RRiBmXOlcBrGq-agSI6xqWUJihkklzVNdW-DoXPsA3VvNpfZL2SDFHq3Y2atBoVy8bcDbP-utaW5X4AeBh0ROnkaP7du-UudYuUIOloXl_O-bQIti4mvX3-8-wCc5uRnOVgz6H7Di2o36Qf5Cf7CMSRs6wAHXPKWPXrFrXgVVTMT8em__sBToUU0aVWRD1uwxBuiP05VuGUJRP2JR46-Pu__N5VjowlCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=Ezhiwq1vSLIHE6z_RECzeu-UnUy_sslEzokBWxNDwfEwD6QgD1mJBr6K6iBHygvrE0d1-XqdcLTP5U2s2AnZvSdpadZ6W_imk9dKZoIFrvGJgLO11Yw52RRiBmXOlcBrGq-agSI6xqWUJihkklzVNdW-DoXPsA3VvNpfZL2SDFHq3Y2atBoVy8bcDbP-utaW5X4AeBh0ROnkaP7du-UudYuUIOloXl_O-bQIti4mvX3-8-wCc5uRnOVgz6H7Di2o36Qf5Cf7CMSRs6wAHXPKWPXrFrXgVVTMT8em__sBToUU0aVWRD1uwxBuiP05VuGUJRP2JR46-Pu__N5VjowlCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=jz7hN2WnbnsL_GjsOywDkkh0wdli0nBYEl3dDyTpFh9FOyHry1wqipQwoLa0uxDOttucfDAKJBapl2H-r5LvXewPfDNdgipHI2jLkQZltBI1UEq4-qZujSupZuXD07Y0ttZoPjh0MbW1QrQMVGkm0A7jlPOfAhkmeuqAIPax9YQuNCizPbyiSHEMejPvdy9sk15Qme87Ai9ASXnC9iGsCIbHLja6p1zWwx6QE7r8gR_NMBSWUPC_viJ6_KFeKU1lp41jXkJQpO8tseAA1SPU5jX_MFltXZB0fg4uHcISFyNrszvn8SWuAkGmGIegtBJOutoFrH4ldo-8L9IC11Arig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=jz7hN2WnbnsL_GjsOywDkkh0wdli0nBYEl3dDyTpFh9FOyHry1wqipQwoLa0uxDOttucfDAKJBapl2H-r5LvXewPfDNdgipHI2jLkQZltBI1UEq4-qZujSupZuXD07Y0ttZoPjh0MbW1QrQMVGkm0A7jlPOfAhkmeuqAIPax9YQuNCizPbyiSHEMejPvdy9sk15Qme87Ai9ASXnC9iGsCIbHLja6p1zWwx6QE7r8gR_NMBSWUPC_viJ6_KFeKU1lp41jXkJQpO8tseAA1SPU5jX_MFltXZB0fg4uHcISFyNrszvn8SWuAkGmGIegtBJOutoFrH4ldo-8L9IC11Arig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=lVTryk8rO6e2Cu1VbPzyGjpXL4dL8TyyAEjqwM4JghUP0q6RvG9m6iXMZfSNOWFf4AjxzpiGYbBKuTkhyPz1uG-4x5c6NSqNEWtUlbxQue2qvabgOtewSGxLfrHC1omSwg6xOIVvvUsf0mYvmQto_FJ68vQC_1YIWnBSzM4hk6EbQSO3kR9feb5k-HNCVy2fpfwx8rFbSL1KYbml6ek1Bjr_sjYFYvG2Ov15RiI0ujzYmdlBav1yOPScUiKwMJHXCazt4yPZAZu3GwFZAy24EmSZpEj3K8FLL_NU8Jm3dkR5bJc0hb1lGg3JximDdvEu-7GuznOMxqtBBJ_eE7zIhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=lVTryk8rO6e2Cu1VbPzyGjpXL4dL8TyyAEjqwM4JghUP0q6RvG9m6iXMZfSNOWFf4AjxzpiGYbBKuTkhyPz1uG-4x5c6NSqNEWtUlbxQue2qvabgOtewSGxLfrHC1omSwg6xOIVvvUsf0mYvmQto_FJ68vQC_1YIWnBSzM4hk6EbQSO3kR9feb5k-HNCVy2fpfwx8rFbSL1KYbml6ek1Bjr_sjYFYvG2Ov15RiI0ujzYmdlBav1yOPScUiKwMJHXCazt4yPZAZu3GwFZAy24EmSZpEj3K8FLL_NU8Jm3dkR5bJc0hb1lGg3JximDdvEu-7GuznOMxqtBBJ_eE7zIhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=UOLN3_w-yib_VaqmEnTIO5YxA6CrC2NKeBcKwlcPvmy5vwWYhbeAuVRFF_ZbC-kD7nn6ggW_EIkZwz7n5E6_v295EP4dz3Pfn1XaEmxDGzHo9jIyUfXi25-gN0IwDQeBYRP1MTIK_7bn2JKocyC8VdYzHGLxIJPANCbQ7CbOUbLWNPfPTQ50Uf6JkWsc0MbzifxaoYgfMaG5KEEK0AfrfYyzY1U64J66CNHYUlBAJnQZPC0Jzuddu2RzyID8qxQRNWAhtWdShA9uTh_MfRZ88eYXKMIYMZh6UPLn66ncjq5A8H8W3nohVVRx4qmUyxmUIwzbW1LSQKwz_-9gtv4GMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=UOLN3_w-yib_VaqmEnTIO5YxA6CrC2NKeBcKwlcPvmy5vwWYhbeAuVRFF_ZbC-kD7nn6ggW_EIkZwz7n5E6_v295EP4dz3Pfn1XaEmxDGzHo9jIyUfXi25-gN0IwDQeBYRP1MTIK_7bn2JKocyC8VdYzHGLxIJPANCbQ7CbOUbLWNPfPTQ50Uf6JkWsc0MbzifxaoYgfMaG5KEEK0AfrfYyzY1U64J66CNHYUlBAJnQZPC0Jzuddu2RzyID8qxQRNWAhtWdShA9uTh_MfRZ88eYXKMIYMZh6UPLn66ncjq5A8H8W3nohVVRx4qmUyxmUIwzbW1LSQKwz_-9gtv4GMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO9y-T5IgkClMUDnaQV6vnnfdPI-_vWhbXLWNccv6miYmNE47sImWPoMYh6WQSb3yZWHFE2EiSDc0X65Hgxd1P3KQLfEpz26bcUao78W5Yocex1YCiaMKMfJRppVTRUvubfOEYQwbECqS7Vqtt86e5FsL-FTnCfOD41Wb4lGl8VBjzmx3xYWihyu3X7P-pMJ2WkkeEX5rmnpTf_FXfFHXMalFqAWkaNTANdUMAI-bJyScxD5uK9DuTaN9i1lMmm2kQ0UHWgsjgT-09oZdUY2S6drzN4A2thjX22gr46V0rkb9zwSpI7wBP3zoLicD5yTmKUuISc6S8wF19IAxGXyGPmrE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO9y-T5IgkClMUDnaQV6vnnfdPI-_vWhbXLWNccv6miYmNE47sImWPoMYh6WQSb3yZWHFE2EiSDc0X65Hgxd1P3KQLfEpz26bcUao78W5Yocex1YCiaMKMfJRppVTRUvubfOEYQwbECqS7Vqtt86e5FsL-FTnCfOD41Wb4lGl8VBjzmx3xYWihyu3X7P-pMJ2WkkeEX5rmnpTf_FXfFHXMalFqAWkaNTANdUMAI-bJyScxD5uK9DuTaN9i1lMmm2kQ0UHWgsjgT-09oZdUY2S6drzN4A2thjX22gr46V0rkb9zwSpI7wBP3zoLicD5yTmKUuISc6S8wF19IAxGXyGPmrE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoDz7lyr7HRTokk273giYw-655a2kqFvdFOFVZG91Dgoh-_PnQA5SLCD8jChfqsTLCx1RC8oO9_EcDV-gXTjJ9w2WGV2efoBsGtW7xJjPS3XwSxc_69hE2wG5WXWIQ9IKBAf07qKTorL7ssKCGjyfh6WoA7hJUUbnlQ91r5tl--xIF4T8qgXqnstC2VdyQ6k_rekhasrtCeFPVSicRBEKc48KrpLPJMTQMB--1r_45MIeqOLUxWO1Yr6U_XgrBDzICbKJpgbwOtfcpEmntPxoMW5Wq2cyT6npanMoC9gw5BQrSJU9wiTAJhZPQXp0jI7sW_uYsPI_muUSYWLuAQ40w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=DTnqH2oQ6b3OYM0h3aqXLgmf6ptDCH0XGo85cFoTIwPvwbI5Z9eeeV7SwNBs4y0i3ioxPM_tOl6ht5p-x5B3Yr4eaSVQI1A_obz1BEmhbWuGm-1NkJWk5teti2rWDTAN9vMhg-HxLdjLzhNZr7AreMrSIN5qVOXTOQVNxZ_xWg5R7lRRmjQ7wkWNQ_icVDyZnmB2nnqf7t2SuUN_frZfse1OTEQ7uROBDXdzne0qmULPmCcwtwFIKjDgtR8JmOZveLvN3FwG6hrS6OncCpfeJYHgLAeCcovCkLwu5yJHPCQvktvUvQsPzWsrc5TgrjOGpDQHESzjWo-74BSllZ7gRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=DTnqH2oQ6b3OYM0h3aqXLgmf6ptDCH0XGo85cFoTIwPvwbI5Z9eeeV7SwNBs4y0i3ioxPM_tOl6ht5p-x5B3Yr4eaSVQI1A_obz1BEmhbWuGm-1NkJWk5teti2rWDTAN9vMhg-HxLdjLzhNZr7AreMrSIN5qVOXTOQVNxZ_xWg5R7lRRmjQ7wkWNQ_icVDyZnmB2nnqf7t2SuUN_frZfse1OTEQ7uROBDXdzne0qmULPmCcwtwFIKjDgtR8JmOZveLvN3FwG6hrS6OncCpfeJYHgLAeCcovCkLwu5yJHPCQvktvUvQsPzWsrc5TgrjOGpDQHESzjWo-74BSllZ7gRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0OkAwt_doJX_rtrqeK452IAwN_-B16RzmGmmzce5n7Ei3wQWR058UWsMQ3JWNXVr9RJzB6xdllf7DaCXPU31Lz-OxLXLc4xp7hQaz5JwL0nhtx96A5ZGLsjyOtJyl2SuUHRzp5MkOxS2dt4JcfIHW8UPr3TT4_M_x1EMpwlN8nbqf9zJoX5z1-epmGSLozWe6WFz_tEIsK7htIw_AzC8j-Ps8xqGbfBR2YLPLH4bAXjhbpxXVE3en_fFp-qsoKlr4Mm4WId3_bt88vFL2eUNKlenkXZk_9508VrYaS59qF4qyGb1v8tdnyNptBI0k-U_WeBa4S_c72mKXq_EaCGxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b22HK_w6ZHM8vSTe_h4x6krkq0JvOWJzhF_CcmuagaqIp_HNccO4KGQ7IL8DYf4gdJayYR4ZiMNdH9IfbCRQGNqgrlGVuEABZdiNWcBPdcP6Y0rFCtXkaZAu6C4vI5HMErgGsiMHP0t_FZ7V2y0T90j2N29c6_4X0W8sQzJ_LIRup8EnBUqpv0xqpl0nPtJRIabCmIvmoywEkaGtR7-Nn2Txf4uPrR5o0y4JRA8GBgU5USXnyUlAyA8iq4vEhNQqbx8y4mgr8av0X4N73NN8Kb1pKvdxWCGFDU2jLe4ZLIOHcQkAbR7xyI_O--V5X-zHeJoh4ybrnIFvRJifmPloqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adCrfwN5DLlMw5Xl-adVpDzBBF9eleB7NtkI2mGArDcPwsTpglUI9t-i8BwL6bgORmvC22_sku13qjnDVPRy3cml5wvB0fEAnpciFGv6S2mMMiSsPywRMNd1mVXMsO50lX6fLWElNFL_sDTxV7SiY1CR9NPVxt-t2XLrOq4bt9WiJNFNFDHUrgSRtdoEWPvmgObuHj5SIix03taba0-YxgnplUrFguavwi2rPrho4bf0kVGgRUBagQQniSMvbQet1FhF8gxE3siwDHeCyC3VZ47Xq4X6IWotHPj8sBWq-D_Bk87ddHCmwpBsjpxS6KNDyUNcXaB7V5DszNfN3tCZLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی  وزیر امور خارجه لبنان:
«حزب‌الله یک نهاد نظامی غیرقانونی
و بازوی مسلح جمهوری اسلامی
برای بی‌ثباتی منطقه است. اقدامات حزب‌الله، لبنان را وارد جنگ‌هایی کرده
که هیچ ربطی به لبنان ندارد.
ما فقط میخواهیم در یک کشور عادی زندگی کنیم! نه اینکه همیشه در جنگ باشیم.
مردم ایران گروگان نظامی
تمامیت‌خواه هستند.»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5530" target="_blank">📅 19:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=kyWMMyo-WiO1s81138b30V2CtQoixeZ3B8h_vYPL63nE6ysZd5ZwD9JT-nogzPCwj1LMwoM25C1ZhYmUF6WUXc4AGF3qeaohSXlT4TnZkQ1Kuf8V85W27XKxBZUDHNa2pTRnuItfVggrl6T112Bt1CdAy95ucl-590l2tmXSu8iyjCINNsv8lOEW_uffoPAxrcnbhzsnhrAVWsdZ7lR4-x_gzqfMqmu22rGUuQ10pCKiabkyisvoFT0ExkcKY3ZE7Cuv4ZGxXyPDkH5GBj7tqNutklAu4Y_TVhNIAsu-tFzJc-a2cRHyPzDuxrG7s48NmYmC1-MzT2_MnoU6XhdRng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=kyWMMyo-WiO1s81138b30V2CtQoixeZ3B8h_vYPL63nE6ysZd5ZwD9JT-nogzPCwj1LMwoM25C1ZhYmUF6WUXc4AGF3qeaohSXlT4TnZkQ1Kuf8V85W27XKxBZUDHNa2pTRnuItfVggrl6T112Bt1CdAy95ucl-590l2tmXSu8iyjCINNsv8lOEW_uffoPAxrcnbhzsnhrAVWsdZ7lR4-x_gzqfMqmu22rGUuQ10pCKiabkyisvoFT0ExkcKY3ZE7Cuv4ZGxXyPDkH5GBj7tqNutklAu4Y_TVhNIAsu-tFzJc-a2cRHyPzDuxrG7s48NmYmC1-MzT2_MnoU6XhdRng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJhbbi8wam50VgSeb75oMICNTRyFFZi-qfW35eARFr4ki7Mdsns9PXrzCwLqcAelDdOlYNk-1j8KydXjr8J-PIjYDCCj44koSu9xA5hlKTUkHBnTyUXAgAnETupAOBOyWcMebul_K90e6U_ansYp1isCBeiTz25OzTaqWbLhGO8-hS5xhdbQB1Nfog-OQHVLjgGloIMVwDvoS4MGKvhMIsU0oenT6AKJTNhHyKCC5LSzuB4yGYiF8M-fyUv0J2AfmAA8z7zD1rfxMUV2zIn9a07CiRU5ZYWthwosLf4wNUQPrT592Pt2JJ-0F887rTXOOXqCeomBG1zjUSFHwNGcNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/as-d37qhdlRuJroKet-uNKPJgB9P7A7Nht7E-zqWPgepqfRFD-va8X8TwYXqBRPt9vVpmDJVSxK7PkIQdfkkvsJsKh10TZ57S0ajUiVFgHxunxXi4JvDhIS5FY9Adbb03lY_Hfxmqc5bU5gICRsY4Uxi6NEjfa5E4KwFCPjtKq-2hhf8oWy-5dkN5FkDBDV-HoKVbJwL4Rs74OFDRKm3X08-_WeiDllYnH3ivLjIFhLpz9EmzbaEjHI_czomYD3sr9X0NodhbO6LGwesLWorh35kQ0HfInflqbuV3vM1rS0BWj1dQv30-NHGcS5uQCHmHhzG5HdmYjPE5hQqvssdZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rw2b3Tl800qfRWr-VdEj1CHd9eAyLn06IGbOwIIYxjQEw_l0RKS-dZXr5DFmqu-UJhOSSgLIz6NIiVT6luQzaw-dCxVz4X2o_QoJdO0HZ7qj7YceNYaRTJAv1JGBjJl6YDgRAOUWeT-Ws2fubpKx5GJzo6mZTGw9geG8lVLPrjMzcbd9CuhkuBy3TZVVVDeDVnY8LEFfzPYliQbgsH-ljLKgQbH2djSGJsK-VHSBLWwybUugKycsSl4fBxiOzgvPh1QxSULTILOd2ER0w911dQiyw5xL0osLRoi7l1Q1Jb63URoUIg7nYwEFSLZGS7fZYEJejNDMxSxr97xm_vKlBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucJ2zYGaXERB-UkG5rRvIke4n0sTP8fnNNKWz8ZICsOTm2nATiFfZCV07VLHDiVkK7ir7uBD9vyh5UuY2Y2nr1iI5FQ8x8_oEQmhJGvSTsZSLnoYNcsgKyDfKpOXY0UN3FUeLWYDeVn7YXPkeFA3npfaZ7JxhMG_zSZTYu_27Lwz4H4EUycL6gJaUAeKqGKF_guZhT3UYeUHxpXXSzc4-gjaSpuzaAXbibWZn1MSwkHGIg7ZxVgAgvGD5yQ2BO5CmmnY9J6J_4QSfzKhCjPk7uqzjHFJgzP9EqNTdC9jG6e7G-WYNvSviNRuOutm0mh4ZmBjOkr3ESVTYiLWCvTJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=D916DQCDgntWzsndmlFuMuFMhvBuimaDcCIWWQP_i2-kt_xCsEMyA5x42BS6TkqHOVrkSP7a1cvnsvhMjU6erkULWxMTwPYhYFTvlwYvKlTEEokBPXKfpmNJJ9d4Utb1i1n9lkfrD37zORVdLZmPEYOZ27BKFH7Kd8uEAtA59kgC3FTbQNIw9hQhy6BCnyx8vXD3Hpwtm_cZTShxLCt6hNrsYgT1lt1G5Hgal7-snf850WTcGVlA2YVP8691iCXe1Vq6YQgdecvfkbMCnTuC0t55eH5S50w4tc6hBqB5jTa1zvHFnHaCdqYJ9WlAvL1rwTAeqdRM4cLZlWbte9BM1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=D916DQCDgntWzsndmlFuMuFMhvBuimaDcCIWWQP_i2-kt_xCsEMyA5x42BS6TkqHOVrkSP7a1cvnsvhMjU6erkULWxMTwPYhYFTvlwYvKlTEEokBPXKfpmNJJ9d4Utb1i1n9lkfrD37zORVdLZmPEYOZ27BKFH7Kd8uEAtA59kgC3FTbQNIw9hQhy6BCnyx8vXD3Hpwtm_cZTShxLCt6hNrsYgT1lt1G5Hgal7-snf850WTcGVlA2YVP8691iCXe1Vq6YQgdecvfkbMCnTuC0t55eH5S50w4tc6hBqB5jTa1zvHFnHaCdqYJ9WlAvL1rwTAeqdRM4cLZlWbte9BM1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9Dwzqrb3wHNkd0ODr2YcKHIe6kE09nm876RVZU94durbXhoPZEuRfnweCMGn3rE93ZUf-M55QmDzyIkXDWKtRPgAl6uyLk9A1f1oRccHO8hxEpTpD4Mcj1-HlTDmrE-vxvVyFXFCS5cUz_TI1ztPJe4csEvx4fIda60hbgjRx-J7eC5INskB3m2EOPLcEleQeQhArwJ062jGqhNlSnHPxP1MIxSIKzMiANAvQ2TFrlzz4Fn0QYmEfxkuKrpCJAfZMQ1RmRJCQP6fcTmRDEPjOZOqYZ61-IrWvKMOQ-jUkEtDWY-0R4Thjb9Z_vU_UDqzzLr__3odtlOl9UcwBdUMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i58X9quY0hDuTcHQxtYOb-XcHPLO9F3sAIrEa1fmIAWKGteD_KiNGAHYQXqL_wM7SjXDzZIMy8wrkrjo3_3-l7twxPsSP3uoKTs8aBSqdhvmPiyNWVorDxKnoCVDjIiRpewYUNHoCfSuiqwO2HO_4BKjMezFr5fFiNdG3107gPg2zI4mI7Sv0Ifhr1IFFN_BhWBuKwoGFq7ENkEwzDemso3yp452RBRbyEKhqZiOaQKyZpydsACxAMnvnqyTixMXFqB0tWv9CvJ2X_1uqosxS8hy4cW4W-qfM-8lgrtZogecA3prbh3wofcAFOkgKb9htvJ56NUkgz89TsLu4lho_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=fLmP6T0ceMvMU7128YLPi0aHrThLWz1mLITniVafiD5CeDxTZ_bbARbDH-VA8qUNTTKvDpvwidq9ULWCsxWlPYspsziw1WRi5hf3pR5CdWdtUmvKKfHRgA3Jip6HXD0R3lveMWmpETg-_y8cJfrXEQeUpBIbj21zP1rPn0hF7E3hXdS4fUUWc1K4mwLq80LdngXPX4KI3MC8orLSBplz7V1D-LYJik_TuXkoxBiuZ_0l550ASsXY23SCX7L29v7No3mXLcadXoUsgFPYPVCxbqVlEWXL-3lNnFGSD3gZQ6bu9v_KJgc-1qzCsfAOYtpvK41YNWY3vXGisF5WFRSofCeTrMSVJxZbrhfhvR21WkehX18UDuN35M70ZsSw7W7ecPMqmgtWJqKMovNr0dRd1uJXlcEo9Ti-SgVkdxeDYTw52orY87zaGxNMCpKew2Spr4rhWvFxnwu_z1LPWCa2UaxMjc5p1OPsjp9mfZmihJ2Deon2yaBldi9ADAfRuc_7n68deLxFItGyyqj35S3Qu1GB0B8hLzIKJvxS0jvNvWETc9cwjYqEz8bUwjeU9V91Rts02ZPoetoyFHchXXD5wUCCUZn-xHcVQDaCe8sYPXatI9L76OXCrdecXH6TMt2XcTdW-69D546vPh8wmVz7bIPLQkdeq19sBZU98g6IUQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=fLmP6T0ceMvMU7128YLPi0aHrThLWz1mLITniVafiD5CeDxTZ_bbARbDH-VA8qUNTTKvDpvwidq9ULWCsxWlPYspsziw1WRi5hf3pR5CdWdtUmvKKfHRgA3Jip6HXD0R3lveMWmpETg-_y8cJfrXEQeUpBIbj21zP1rPn0hF7E3hXdS4fUUWc1K4mwLq80LdngXPX4KI3MC8orLSBplz7V1D-LYJik_TuXkoxBiuZ_0l550ASsXY23SCX7L29v7No3mXLcadXoUsgFPYPVCxbqVlEWXL-3lNnFGSD3gZQ6bu9v_KJgc-1qzCsfAOYtpvK41YNWY3vXGisF5WFRSofCeTrMSVJxZbrhfhvR21WkehX18UDuN35M70ZsSw7W7ecPMqmgtWJqKMovNr0dRd1uJXlcEo9Ti-SgVkdxeDYTw52orY87zaGxNMCpKew2Spr4rhWvFxnwu_z1LPWCa2UaxMjc5p1OPsjp9mfZmihJ2Deon2yaBldi9ADAfRuc_7n68deLxFItGyyqj35S3Qu1GB0B8hLzIKJvxS0jvNvWETc9cwjYqEz8bUwjeU9V91Rts02ZPoetoyFHchXXD5wUCCUZn-xHcVQDaCe8sYPXatI9L76OXCrdecXH6TMt2XcTdW-69D546vPh8wmVz7bIPLQkdeq19sBZU98g6IUQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=Y9UAhlmAB8ih_NvQUr6lDWg3k_w0HryOIVrn-04dQgOrhDxhQd_CfDmY5yfLe60JCxU9IzJvt58_E691KlC1qBvu55EI6_G8Q9C9Po2JSDo7Th7T8GRfWVPhWwAAfiqrZTJ-HpGJ6PdWT0_Ixjdr4Zjz0jS3cYYdYMuibO1oJVMF6NmrUfjSLxAh6VtT9m3yiMPA-FH2ZBg6zwuwSaJ9RpQ7mcpl-BxRhdukAS2wB1Ke6yMP9W6LAq9OH_5QFai16gc22t3LbIRViPEhd6lRVz7BV-ovcIoz9t36nmhegU8QGhIH2aULBI-RfUPB5RiJP2EcJeN5TNB9KIeZp9_1mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=Y9UAhlmAB8ih_NvQUr6lDWg3k_w0HryOIVrn-04dQgOrhDxhQd_CfDmY5yfLe60JCxU9IzJvt58_E691KlC1qBvu55EI6_G8Q9C9Po2JSDo7Th7T8GRfWVPhWwAAfiqrZTJ-HpGJ6PdWT0_Ixjdr4Zjz0jS3cYYdYMuibO1oJVMF6NmrUfjSLxAh6VtT9m3yiMPA-FH2ZBg6zwuwSaJ9RpQ7mcpl-BxRhdukAS2wB1Ke6yMP9W6LAq9OH_5QFai16gc22t3LbIRViPEhd6lRVz7BV-ovcIoz9t36nmhegU8QGhIH2aULBI-RfUPB5RiJP2EcJeN5TNB9KIeZp9_1mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThrOFVeqmiTO_H1XWUggSF_UPExTVknVOfmVHu9SHfxwn9AFHxcjRsc6m1O0717yqHejYvJQ9P1NvKKJmkDXIJ973pCFss608zGIJ01YxbTOgnxOYWOOihcPkb_mcKIDyqDqdEJpUYiv5yCPjenuXSoVy2a7NZ6INvIkxZ24jdAdmzblh_P5rKOSsunPhNxmYJoRzwheSR25lCWSKcYJ1zo_tNkU5PV3Jh7H8szDd3osK5pxnuiUCJDCvA8rikZ4nx4HEie4l-l0J1Tp6T9zJUCfZY2FxQYaoZf3aAeHPe8ZlJD_h_j_xgDjtO3IjqJWe5rV6wNaMLfOCIdibHi-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=j-qzBl6zQSvBDMaArJpzpRELC2kc4MNtNZhaTmy5Q8tNRjcm4_QTVjMTwJspaXUSM_qSPaEPQzYiVRUCq2oQKq-CJo8fr6-Ol6YC480FvLSOPp0dtcOX6WBn1v-ErN4N14HRKSaS__0CE0D2dreu1vQHBnUkf0z_IPHoAlnwuHL21UBuNQlDlWeix58TbV4q-cPGxFcdftLBe3qxCULCJH8BL0UriHSRU1g5N_zk3FHAqbbu4grm3arHV0R16AzZKE6NZwBhL0wVbXvEOQW0fMCO1kQ2VY7ZcJub3yct-wen99YaLW9iEldwtySakIsahWKLHFExx5JrIcBwRdG_UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=j-qzBl6zQSvBDMaArJpzpRELC2kc4MNtNZhaTmy5Q8tNRjcm4_QTVjMTwJspaXUSM_qSPaEPQzYiVRUCq2oQKq-CJo8fr6-Ol6YC480FvLSOPp0dtcOX6WBn1v-ErN4N14HRKSaS__0CE0D2dreu1vQHBnUkf0z_IPHoAlnwuHL21UBuNQlDlWeix58TbV4q-cPGxFcdftLBe3qxCULCJH8BL0UriHSRU1g5N_zk3FHAqbbu4grm3arHV0R16AzZKE6NZwBhL0wVbXvEOQW0fMCO1kQ2VY7ZcJub3yct-wen99YaLW9iEldwtySakIsahWKLHFExx5JrIcBwRdG_UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhbmHnwgnHMJ1VqDjBvDUOdafOrXJyKOp5KefokzKf0yF-cWygJFO1dyWJm0L5aA9v7Dyr33mAyK5ZszhqNnwYYY0bM2KBCh4fz0nQBNq2iWl6g2_IJfgf3AVQm0fgiGrKecNB_aFH_Ijkz98JpkDfChryj5eLiMmDYDOiFfMBxR8VY1Wr2Lb7thTWlucMmFXbAdL97pr0xEjK4ginZf4sV2EdH6imyrjHsRKKr2NMwgUj_D9UiHJIEMIVSIZWABidvj4tEpHnjq_90BZiLVBljgaTWTyeGPffy-vAXaxpl-ILjZGW9EuLC4fjjZ41DK9B76-QxE2UYhzFyboXNdbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=ou_o0BuecRDateiaX3kEJLj6bcpKk46bFcPctyCw2hWKkud1WzCafZbDdOQ-jaPVI5CcWun8VcxsfZ1Fvybj3k4QMAKvwZenB2VXnPj1aE3JfrnYL5ouFCwQUQGiOfOF03LLv_QidmTymrCyIuP2xX6IbmjEe382y8tKH0lYXerqaHZIZTwv1A4tX4tQzD7_WM4bMid81OZ9__SzQb-lY9MoDXyGHd6LSkvA8VH4ZSIQbhHWbZfw_kSfddXbb84JTLN6Eo5ycPaMKTs5JGLwAIB7SPE5k6hIL033RTFJBTIfGfycdYU2BdTtkonmJUapMmx7CbnFTbNzwKUEyUt5vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=ou_o0BuecRDateiaX3kEJLj6bcpKk46bFcPctyCw2hWKkud1WzCafZbDdOQ-jaPVI5CcWun8VcxsfZ1Fvybj3k4QMAKvwZenB2VXnPj1aE3JfrnYL5ouFCwQUQGiOfOF03LLv_QidmTymrCyIuP2xX6IbmjEe382y8tKH0lYXerqaHZIZTwv1A4tX4tQzD7_WM4bMid81OZ9__SzQb-lY9MoDXyGHd6LSkvA8VH4ZSIQbhHWbZfw_kSfddXbb84JTLN6Eo5ycPaMKTs5JGLwAIB7SPE5k6hIL033RTFJBTIfGfycdYU2BdTtkonmJUapMmx7CbnFTbNzwKUEyUt5vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=g-itWH_spmroTgfO58tfpHycPssj-imjfTiARpHxSzeAUP2keOk9uE6C5UwbfTH4_bNqotZbwe_sos50ZGzvBP_8lV8gpOpBvbnZhgWpd4XYu0l38W_Sqvfr_yk1PQBq0SmBuSdbBSMG8XOXRGa55fw5sbDYqRzGWAUWdcv-NzFG0rI11QN_41poe-XdDHbivmOTwA55W83NgYvuHCUJLbwpDueLO9w_cvqRIIqZkDm6kwXc_Ai9zN3O4ReZX1CRbltOBSAbZCYQLQzCH5bVj9SAFq3wt3cnU4h681hAMpD_XpXiKIGaFeWQemaA184Rp0A3-dIH3ptnZtTGEyVpAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=g-itWH_spmroTgfO58tfpHycPssj-imjfTiARpHxSzeAUP2keOk9uE6C5UwbfTH4_bNqotZbwe_sos50ZGzvBP_8lV8gpOpBvbnZhgWpd4XYu0l38W_Sqvfr_yk1PQBq0SmBuSdbBSMG8XOXRGa55fw5sbDYqRzGWAUWdcv-NzFG0rI11QN_41poe-XdDHbivmOTwA55W83NgYvuHCUJLbwpDueLO9w_cvqRIIqZkDm6kwXc_Ai9zN3O4ReZX1CRbltOBSAbZCYQLQzCH5bVj9SAFq3wt3cnU4h681hAMpD_XpXiKIGaFeWQemaA184Rp0A3-dIH3ptnZtTGEyVpAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
