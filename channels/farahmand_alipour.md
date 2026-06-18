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
<img src="https://cdn4.telesco.pe/file/HZgd3rN0R4cYtz11uP4V7_rli696yxEQvqnAydyoN9WDYGotzNpHUdNu4DJaGgsgtZy32R1g6X9OqD2euTPT_8Dm-wt5kz44rgw8OF0nntmksYmRX1doMc56i3Tw1GLVlnIjD1T6i3tVpBhFj8R49orfECZ1VxGtyJwaoicB9Z1gdtWKYPzPTGx4-ZH1PL95AIobZD0rbegRAoxdliPfxtNvk-0aVAtT4D04r6Lo32-KQcamFz8_YZ7I6XRr9dQp_2pgdw00tCKrI3jw1juNj45uCytL2ZpZnydoynqv98WVKgIw-RhzRLU0B_qD4kGzzxoN7Vw487geeC5ZLorV4g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.2K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 10:27:23</div>
<hr>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYwsTfVckdui6X27eQmEuORjefB8vf3SxEdXfPDjvlwOAG6FcSMLuNOWbOlxweZa6P9gnf3YhjBvO-RIYXhhRaTKwC7HPrtj4gXlA09lIHju6tSQQCxB2Xq2bcRF4OZ622BdW5zJG-PkrVkcsBwYXLXb9QLjjyTbUXaxX4AXDS0EDOrOCg8lCtXzT1Y9JLMW_E5rqyx3LjnTRFeXq6rApmEmOC7d0j58DB2mOHQdvEmpRmKHws3wQUWL1OV5JUclPLiQn7AuijEgW5iNMHZuEu5iDw8CxBgUMXZBkGlfohEJtDokCrwBiJG3moP2V_C5S9JnaMQdOwmFsFMQDyKbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UP1OQZXMlBAqkFpy2LLUBCgV44cbR-pDocMzLAh8jIIxKGyCT-KofOjEvjXcELSuDnmEHvMJlXDwMkWU4g1qgSZ5YIu-henkAw7oCx0fhKvlqgSH84geZlyv-ojSVgZ4fHvFIgp6Gh6k5FGjfNXMIhnyGDW1BSlfXOgv-gTmKtY4nZVs9HyzHEUPaUNQ31aUYOom5PPmrQ9oacZZPZZ9G4ymZtb4mlrmDc4OQ342u7bnsxBxL4_bGdSIy7PbXBx2mGeYLDDZB6UfAqg6exDxjGSygVFvPUv_v1A9h2gm0Qg80LSsLAiWO1V9MYIF92LYNXO8qmGr_C3MhKZW_thSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=PFYVTojENTp-rtSRwmrybw8WHnFblqXWtxa09dp9EXczhG6vLvxtVsqEotljqkXaF8cXfo7U4hT0RjpraXSD1V-ZS750SinN8Pandu263YhTfTRdHqHvIjOtEoY-H311spWSktt9PwrIxmTxOh90KqGOqGvV1p0pNiWTviEb156_KNGzn1wyMn4yE19ewGcXPX0m40Z7dlsGhGi9vUKUndrulCQwVTTwSvnAzPq3-oPp1OpZDEJYga5ZMQd9afzXFsidtQN4I65o4Y4kcIkcl-0N0VbNv57uXn5kcjoa-9R6fCaWbX-mR-mQWIKdFqz9ed1dK8BGGQwPqJTPQqP6pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=PFYVTojENTp-rtSRwmrybw8WHnFblqXWtxa09dp9EXczhG6vLvxtVsqEotljqkXaF8cXfo7U4hT0RjpraXSD1V-ZS750SinN8Pandu263YhTfTRdHqHvIjOtEoY-H311spWSktt9PwrIxmTxOh90KqGOqGvV1p0pNiWTviEb156_KNGzn1wyMn4yE19ewGcXPX0m40Z7dlsGhGi9vUKUndrulCQwVTTwSvnAzPq3-oPp1OpZDEJYga5ZMQd9afzXFsidtQN4I65o4Y4kcIkcl-0N0VbNv57uXn5kcjoa-9R6fCaWbX-mR-mQWIKdFqz9ed1dK8BGGQwPqJTPQqP6pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=RI2LVf0juEZKlxEe8fOyUxqso8ZpH6MvFn3CXezzSwiiGFIWn8gngzWm09NQWRKhmClzqfA00n2pYx3rW3cHuioc_G270kGoV3ETw-6cPFB_zKuBsroywsSJcMhcyscntgslErux9BO2vHMn9wZFDUHFp370RRjkpc7XLJatTg5mELkz2cmNUZtbT2EdMvToJe1NDaklzEl4LtanMlFIrmEwjid7dJTHYQjd3IvtQWnFrrGwV7fckGuHEVYcQol-fdNfIbWFxlX5ofYYDZeHe0O9cpbLACvZHx-TOony6UPyIGnMbG09dXUbKZYcuduAaMx8QA0U9d0bAp26qCLafw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=RI2LVf0juEZKlxEe8fOyUxqso8ZpH6MvFn3CXezzSwiiGFIWn8gngzWm09NQWRKhmClzqfA00n2pYx3rW3cHuioc_G270kGoV3ETw-6cPFB_zKuBsroywsSJcMhcyscntgslErux9BO2vHMn9wZFDUHFp370RRjkpc7XLJatTg5mELkz2cmNUZtbT2EdMvToJe1NDaklzEl4LtanMlFIrmEwjid7dJTHYQjd3IvtQWnFrrGwV7fckGuHEVYcQol-fdNfIbWFxlX5ofYYDZeHe0O9cpbLACvZHx-TOony6UPyIGnMbG09dXUbKZYcuduAaMx8QA0U9d0bAp26qCLafw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/re8Ivd1acJr2AYq_VM7tBuV0osFyLtc6mK3P245ttOu6Iq2qX76CrvfRCjBeqGzRuFp0QFj3RH8k0gFxMAZTGrJ1I19OFWVpaWxRrrlRAuw0p8l78rRk3nhQazHBXnNEHr2a9DqpwFos-ADwLJnvCNYCqQTT-ey2M7sDqj-KJdKgUzN-WMl8oSXrc8gHUjnty3LQsfP68x-f1-c6d2tbS4fJ-DG6T-UMDxZxtslrKxFaTWHmMrYPxDJZFJpRvEBO-8Drgiqbl0iK06VDjyPApXY3CgfxcA7oJflirROvqrGRY1LuwZ0feiJEkLq8FoKFH3kb3DfTcTbbHHoANP03TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRkNt9P_K0cLX0X1iCZoQfyrbNeOd_JITf75SFDcR1lVcltYSUOBfL7nSm9u8yzj1LlAhpNTt7Zm7wG53cl8PGIUGKVNZLLBYSNStKSZ0rTm1cvJR6lkRS-NE63ed7WZqWQ584z56Fj9tiRjwhGiQ0NIBagqU3Ip19kHXNu7LWcs1Q52OWwuslV1-OKjej2vrM3iixpL_s2iMM1pw9LYwIlUhKFggRnRyt6j8-qSQz7GAYSgtyRkc1GBiytPfid7m-w2UgPEYWa4zDMWTGHi5HLyWLfetuG8KlP-bs-oh0cnqP_AvCushNna2NMtHtkT6CaSMVBbsCbBlHgcn_y2uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHP6jUqEI51WHu3T9IcoZbP0cDTF9GxNBxxbDwILXFWRFjpsoi0_27j8nlIYzjEt0__XILGIiBY9VPiEYUHK3zXqL-sL6IruHPTke6gxGiwHm7Wk8xB12CTXjKB_l16kOVJDR3T3TL3qWIswxhbjEqX9sPyiWsqedMPrGJQzFITCX9Orpnu3eiuXzjLKaZ5SMYb_k4TShE_Ync6Z31ViStn_d3BplMZBRSUYcN0fkC2hMP0mVJrqA6sBL2GUGlyW2Nt6z06jVGsAMZJ6k0ooee1ZPH8FoXKA2Ct72IwIgZSBD4TVplt6WDEarU3hCHXBEQ4mA6bgbHAx1Cy0sHnCOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJk9eU7zvd9Y86X0GZrNDV_bEiB9k0T18W1Bw8aDRDiMe84SooMoKoBHp_tyua4tFABIURqhRwhVDgxrolIZdozJ_mf1O7IjEzXgu29wrt0JjWV7AdixXpF8ooXbFsNF241U6_rKxroW1SeNREqtqUNtHBPLsbBv8_rCYpeEnF_Us-38TOrI0xS6jPobbqMqtEzUUcbC8pdUbvYLN8UjYtYKcD9EyZ2YlAH-Hnw2txRjGUwmmTt0mIsNheHyeKDDqcn3SlTScXJhwKwMKIFQuuTsfIgt4mJt5ywYP-fz0E-ASUDf8G6fS0JVST2auBsW-cTmT78Sfz0Ygj1y69RWFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TU_8xyjimYjbjX1tsVOJBd7UFjg3nV3KUt4SBSrsxIEj5EZkcLJs7RVrkAKS0uyAmCiJd0ijPQJCUh5KZ7_FW9tlxJvH56DViz_bp1lT8tQ9S051RPq5EBAhehfWt6KNyzm9rINkUtmKkrxgEy7OlCQhTdL0oooMCsMlP1fCsGxBZxGh1jfyW_4PM_4U0jhZtqrJFtBDw1Ae2sOe4OOf8WTzJch8WAS22qXJbXiHOsc5WZAA7Wb75H_nM6dgkxLOFfTg6lucyuwXPkctD_Gf-UVCkfCqPBn8jS64BSLgfdV8YDoXyVJWBTvp-fd3o4cDZX0FryfLfhRQAOGGOQCcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=LBVpjEjAhZqqIQ1sV0OokRhSlMiK7llPZYZeab9zoljhlblhteBQpaLG_rMxxbYHpaFKHYpG62jDc2IUfwCtuvtZmK8mR6LTRXxi3ZiMdpY5-P30OJC7CiiUIABJJPfgxcSWECCgDCmmXbtM7TUp-HcC6YYbIRP2vbfW4uxnUz4IU2_qaWyM9IrsC8WvI44kvk12ZgHw9D8FxxQ3htNsZu4MjKfnIcavSj1thIZbNDkK_pG44r9IpG6YsRrRADz6A0iiWjuFUQ9RvCGxMLALlmm6RU0KydP0hWgjMa8Uc6wsqh4JLRp7yeahUyfUsLUVfb2c3EbxpM2c93OEm6Ek8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=LBVpjEjAhZqqIQ1sV0OokRhSlMiK7llPZYZeab9zoljhlblhteBQpaLG_rMxxbYHpaFKHYpG62jDc2IUfwCtuvtZmK8mR6LTRXxi3ZiMdpY5-P30OJC7CiiUIABJJPfgxcSWECCgDCmmXbtM7TUp-HcC6YYbIRP2vbfW4uxnUz4IU2_qaWyM9IrsC8WvI44kvk12ZgHw9D8FxxQ3htNsZu4MjKfnIcavSj1thIZbNDkK_pG44r9IpG6YsRrRADz6A0iiWjuFUQ9RvCGxMLALlmm6RU0KydP0hWgjMa8Uc6wsqh4JLRp7yeahUyfUsLUVfb2c3EbxpM2c93OEm6Ek8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftTLp4fYueL2tArKcetwHxdR0WYHDLctsqehkSRZUlxftiUZJ-6vLBlwKYWVk0fFOHltcX0cIGM4nyjstmT666bdTudDi7LRSglxhdYKYBRANYKmBd6AJB5fZSZ7kVlgkPEF8zcqFam0VxweXTSoN6B0gc8lOLtF82ctMw-jBn__aTh0vQiJ61j82FE9Mvs3nOmQIhiiTbzTmTuCi2sRqkjGVyVo6KVFYyz63ypoRbAaL32uoPAc5SFGev6ktVxxQjNNfu9ntuYt64AaAAdhiY5_TqSEmvu7DAaXPZqfkvQPRHxXelfugGlYRCliNklVejsmsZiKw6srPAW8pDztUg5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftTLp4fYueL2tArKcetwHxdR0WYHDLctsqehkSRZUlxftiUZJ-6vLBlwKYWVk0fFOHltcX0cIGM4nyjstmT666bdTudDi7LRSglxhdYKYBRANYKmBd6AJB5fZSZ7kVlgkPEF8zcqFam0VxweXTSoN6B0gc8lOLtF82ctMw-jBn__aTh0vQiJ61j82FE9Mvs3nOmQIhiiTbzTmTuCi2sRqkjGVyVo6KVFYyz63ypoRbAaL32uoPAc5SFGev6ktVxxQjNNfu9ntuYt64AaAAdhiY5_TqSEmvu7DAaXPZqfkvQPRHxXelfugGlYRCliNklVejsmsZiKw6srPAW8pDztUg5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-ekFqLmcnmsMUVt-Fhpaq6b3r5cWgjIaTYufBui9qHdNv8p1nHWyah08cTvsZJZjIgTZGVOpSg5989ufgBx4ShaKaNtQtTtXUhKg6sc52-68YY9G3wPeByguPmKFkRoR2t4eEw1gsxsnOyk_vZWOiA6H_UP9HcnNVCVc5yNkOhTlWCZr3BGSyloU7h30U0ercvzdenqHUOJ_mBk_J8tfozLpg5i1VTMPt98mwUCs22oLuw_tdPRVeD4x9Qi5AVwShR0b_SDURQgkjqtFe8EkGahBf9DXJPuOrY-Z2fYf3C6gqYv5iy67kLJTMtUOLPcoQm3iKRZ3NZzP2dRpnuBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها
محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار
جمهوری اسلامی و نیابتی‌هاش رو به
«اختاپوس» تشبیه کرد و اعتقاد داشت
که باید به جای درگیر شدن با دست‌های‌
اختاپوس در لبنان و غزه و سوریه ، عراق و یمن و …..
باید مستقیما به سر اختاپوس کرد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntKGPx4iSNDVYS_PJzXRm79EBoH62Dp892kI0cNYLQTu8HbsFEkgWCpoZCh3LCXLwIQsixJcmnehA6FdmR8a7qYFCI4XqPY56Y-m_gQx3fS95INWJpv_ZpG9Wgd5bUe3C8XVlobBTZWXrmD4s3iHuZEQ5-I_oYWBz9gS51WHS1p2Du9m8ryCyYsJkh-fipqjOh5Hx40y95Kfb_zvE6I3JX5U7dQZddGaWSK5nPTdIie2TJyTtYWRHobahxV-zep7A2Onw_Di_RmxBy16MXW5AIyvarCkqF_32BUmdI9Ny4uv4AP0dT-xL6OrhIWHReTdaDBolspyEN2DsIz-ekCppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J09HSrHOgRINwk_dbxlrLHeQ6WEwiyypp9qcs_NcbhsRs-Vkb6_OJ_byTxrRcN-LIpX4JBhFglZMb-cwmOq1zcDRJuSusON1wVr91W-kUZj2c0-wI-wEVMt79KK6-KVOSyGw1nfbJJ6PKImN_61pTeQLpGT22GtDw0zDMG7ANYVm_pqyQ47m7l88GThkzs0Hrh4ToYThVezs18DRPTlqqXEhZa-RErpve1EhKmHRiR0_jNveYXsy09Zj9FdrAk9pv8zvW0XiRQzdHLna0cvo-pA7EshUIRv18x2rxAjqeRluHqzQeLtoHJ1Jdom_YX6hNnnaA-bDtFqM_I7DdAzK5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pn3MePX-DfQABMplS6yNDBrLz8OdEWEpbikiBV5yP0e7N2E3djGLgu3IhKmAlCNC2TE4Bgy8fNr_md8QwIOCqO9P70cs3hH9Nmv_4U47kV9SnNi1pd1vRT-HWQGVXMJTd6evU0jcE8e3UBQbEypr-IX88VxeoIBvCVuIEOAQcmIp64JDupzwYo1CL2uDKvxxD5Ywu1lTRdmCU__v21lGBYYpvz5t9GJXcK5k80N6eNIX7xhXbhB2jzNMnFiE5A1Xu16hZwq97yTwmCxB0aTjjEzu7xV-P8x3X8T8rYtiGGoKPUvOsY6bCay3oe4i-f-5FnyZEdqEAILTGT9wSmm5vQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSKlr91UlmxQdcpi6i58GeYcOy1jBEpCiDfJmMrWsat-EVnhePeU2OYa2tbWv5g46brebjdfuMDhqw_OyEtuVaTJbztDCP61OlOyKalQ8xxYIVs01-cFmt7Og9S2iSCvSQiybmu_oiGwnhXqouo366NIjM5FjgOJ0v5q_3Q2ve0u6Yv8sBkrXi9ZF4h49VRZDIWEoMrRFSZGtO3a2UcHHA4usNi_AOAcugQfxcROUZKzK2xL-1LASdR3EETP2Ag9FqmHHyVbkaCPWCUxivK1UWU-Q_Ffl4ffl7sD61ilvzZSPOFGpcJmNq2tZ8J0VC52umgHyeWzU_CH2zpXy1iObA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=KOyyWOEYx-wC5v8MzFxnkCJHTyTCpkqMe4JFOa3PeaJifWl4OCfP3-HQD8YtcAo0YYSneKU2GkIY3Qslwtc_Q5MJbXHdnas77xEokVsiem66cMwbHX4Z1hNfWieoWR98reqO0qzHgbpWH2QqsQ42o6vQRqTQ00ZF1J3nhHCReIICngr_6AFmX_gHkW2lbP5vCw17JWvUGjx4SApvbWjaeyReMhZKafWu66fVuLoNqdVPIVWknNcBoIthbGE7h8PwhD1JwnvznXX2eU589I5MIqU1PPWDDcE19QNOKhpyvdqaDQwbsWsAFqCGS9c0xZp-xaaPeQ5ks8ufyO2R317XqaFzBEtwfe9TEb4rn8ZoHcX476qh6wANyfhmoDEbvHtkIlfgJIj0Fq09EaP5pEHCsk4TS64NdnOZO6mk_AvQfspvpwoScVR8R4XgfXE_M2SpRyYwwIfWTHJA0G_6O7DMbI9n4opkgt6At6c0ymGbg_alTidM83hsNni0uf7c8FvDhSt3EOyJmvAtm6ChXntMf17b94BPYYqZAPT4sbVUUy3oU8ksyfpDWtiaNY6Myk6BlgBmkimafaAXCsITnQxAgpg3dFVprvzRDE-Tiwcyj-k4Zng4dg4W2i47LX80AVCKD8xszjYTeKBAdH-DUB29PstHV7_oVAMQdj5shBTPySI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=KOyyWOEYx-wC5v8MzFxnkCJHTyTCpkqMe4JFOa3PeaJifWl4OCfP3-HQD8YtcAo0YYSneKU2GkIY3Qslwtc_Q5MJbXHdnas77xEokVsiem66cMwbHX4Z1hNfWieoWR98reqO0qzHgbpWH2QqsQ42o6vQRqTQ00ZF1J3nhHCReIICngr_6AFmX_gHkW2lbP5vCw17JWvUGjx4SApvbWjaeyReMhZKafWu66fVuLoNqdVPIVWknNcBoIthbGE7h8PwhD1JwnvznXX2eU589I5MIqU1PPWDDcE19QNOKhpyvdqaDQwbsWsAFqCGS9c0xZp-xaaPeQ5ks8ufyO2R317XqaFzBEtwfe9TEb4rn8ZoHcX476qh6wANyfhmoDEbvHtkIlfgJIj0Fq09EaP5pEHCsk4TS64NdnOZO6mk_AvQfspvpwoScVR8R4XgfXE_M2SpRyYwwIfWTHJA0G_6O7DMbI9n4opkgt6At6c0ymGbg_alTidM83hsNni0uf7c8FvDhSt3EOyJmvAtm6ChXntMf17b94BPYYqZAPT4sbVUUy3oU8ksyfpDWtiaNY6Myk6BlgBmkimafaAXCsITnQxAgpg3dFVprvzRDE-Tiwcyj-k4Zng4dg4W2i47LX80AVCKD8xszjYTeKBAdH-DUB29PstHV7_oVAMQdj5shBTPySI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoYe1-kOJSaJXY_p2QxFmeEhAtj5bUyBu7u8ecQQYwupbs8-3azag2pWNn5u7ydqIUGJ3LyETLvjNna7vV9Z8v2Pp0Amm8vMCHNrcxXTTqc2Zt9KE87OEos0yN-EdtWHbCFp8tgPuWgYpCqk71Lza5s7blvV7HTasmau77FdRuehHFTY4zwnefCYMwvljWwNG26LZOBi_G_KgZ83K-hrfGiR7q8u6Ud-GORm6ES9lpQm79nD2RFeqllRh9F_gOOzw0lCG7s66S1KhYXhBl7dRrzVvL6aI3pt9YALsaQ-5GCg18QNQuVcsqrRD9BVgfOjuYUKhi5bmS6voq13TCqbMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=RszC9fI1uTbEy0p0MkBFWkmFkKAuXbZ1Hy8kqmGzp9SmuiWo7wv3zXjtjNk58LFJk-L3BT7aWERfSrqLy2KLCsuX0u3ZQkk3mPEZjjBkW-5bkxllUq-K2cB7dhb9biiCnJJ9ycxC_4yJCu06TiAH0x4Dh8fUEZaDcqcyC7j4GqHG9sAIg9wW9UxnNY4Q-lq4-d4bRTQdV_t0MViF2rdG8E-PjhS3Kld3CCB0MI2NjT215olnF-2XJdpj6BP7-ewLhQvCF1pFB9BoetqyioOkrfbDo0zSlNXlH12lYuBnWhwS1BdtgXeiqVYjCJsVZyKnsrDSEPdNp2WbLb-52j3P9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=RszC9fI1uTbEy0p0MkBFWkmFkKAuXbZ1Hy8kqmGzp9SmuiWo7wv3zXjtjNk58LFJk-L3BT7aWERfSrqLy2KLCsuX0u3ZQkk3mPEZjjBkW-5bkxllUq-K2cB7dhb9biiCnJJ9ycxC_4yJCu06TiAH0x4Dh8fUEZaDcqcyC7j4GqHG9sAIg9wW9UxnNY4Q-lq4-d4bRTQdV_t0MViF2rdG8E-PjhS3Kld3CCB0MI2NjT215olnF-2XJdpj6BP7-ewLhQvCF1pFB9BoetqyioOkrfbDo0zSlNXlH12lYuBnWhwS1BdtgXeiqVYjCJsVZyKnsrDSEPdNp2WbLb-52j3P9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=vPi1e_Bu8w-LysNlg9cnUagsJAdf664tLe3GQR6e7bidJfeePX0XDCpo2_SYziuYrfiUQ8HFGot4t9Kr_OgD4HDFZS_hue0izZCdeLFeFtqvaFLKDusGBhVjaTk7_DqDP-Lyixg8MtJkvznqJjxpx9lUYalrX5ganxww_tIrNzeXtBVaH6v1VttfErLivCEDH6HoxyAAj3vVFR07DCH5zDcjGd-GX56p6Sv-K9U7rgGHPB0Vh2u4i3GLO737v-jStb5qR8SNaojX3u4NzIUqledMSStN6nfQ-dzaN1mnsUMONtc51N-Vuu_wiFNYZ6mrXL1s17TdyFwzhl5ZdzKY81CAwZZ-_K6Tnk0bjiVulVt6fuKyu-jp_nTVN2tXBjOS1qejGzZYM_LHse2eTARdjFQcspvqc9sEtX4OxYT67bDq2Ec5tu0NzPRoXNtmn3VEsuTj8KhrkKfTWrywZQU8R9k_I37yaBTAfrWTnUBb8GgocVsMaqisxE62EnHkltEHvQn0y-iZf1IJ9UPGaYDel2o4zu2eJ-FpSnaYGwt6DAKGeBB-hS4jC6qETusj4S9TwMVkOT98F25yRVA6i9JxwYclUH-oX92olG7amoufx5aVsc800-yMNw0mhzB3TObZlKb18ZtJFZNLk1JyP34JJ3nzcF4cnbLmnOq8B54W8Po" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=vPi1e_Bu8w-LysNlg9cnUagsJAdf664tLe3GQR6e7bidJfeePX0XDCpo2_SYziuYrfiUQ8HFGot4t9Kr_OgD4HDFZS_hue0izZCdeLFeFtqvaFLKDusGBhVjaTk7_DqDP-Lyixg8MtJkvznqJjxpx9lUYalrX5ganxww_tIrNzeXtBVaH6v1VttfErLivCEDH6HoxyAAj3vVFR07DCH5zDcjGd-GX56p6Sv-K9U7rgGHPB0Vh2u4i3GLO737v-jStb5qR8SNaojX3u4NzIUqledMSStN6nfQ-dzaN1mnsUMONtc51N-Vuu_wiFNYZ6mrXL1s17TdyFwzhl5ZdzKY81CAwZZ-_K6Tnk0bjiVulVt6fuKyu-jp_nTVN2tXBjOS1qejGzZYM_LHse2eTARdjFQcspvqc9sEtX4OxYT67bDq2Ec5tu0NzPRoXNtmn3VEsuTj8KhrkKfTWrywZQU8R9k_I37yaBTAfrWTnUBb8GgocVsMaqisxE62EnHkltEHvQn0y-iZf1IJ9UPGaYDel2o4zu2eJ-FpSnaYGwt6DAKGeBB-hS4jC6qETusj4S9TwMVkOT98F25yRVA6i9JxwYclUH-oX92olG7amoufx5aVsc800-yMNw0mhzB3TObZlKb18ZtJFZNLk1JyP34JJ3nzcF4cnbLmnOq8B54W8Po" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=J9gINv-MoI_L0Xohvsrom2TyyOxRIwhaa8U4lxlPpk66RccYtEJmipU2HRgIyiIZRWDLObHUSGV2YkTPfL0FYlvLdqKJ24rlBjvcAtsDGIZbHe1Ddn7YFT8Vbk2bL1i4nC0khmVIJqOL8OzWRUFBNnHZcLHaoipYSxudlsaelT5n_kq-qkeGBhhLiwo_esgJUrb-zQG8Kz9Tw8-EhJLoaQ6s3TELTEZE1RNCaRB2IxWmaVMmkny1NVK9o506hL57UnwXEX5TBiJN8x0DsqGQA85Nm3ebHAFgmJox97HPWgebKtHJ8IQVNpWORA4ohX1N_YODpFqjIyOYBKMohBjNhYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=J9gINv-MoI_L0Xohvsrom2TyyOxRIwhaa8U4lxlPpk66RccYtEJmipU2HRgIyiIZRWDLObHUSGV2YkTPfL0FYlvLdqKJ24rlBjvcAtsDGIZbHe1Ddn7YFT8Vbk2bL1i4nC0khmVIJqOL8OzWRUFBNnHZcLHaoipYSxudlsaelT5n_kq-qkeGBhhLiwo_esgJUrb-zQG8Kz9Tw8-EhJLoaQ6s3TELTEZE1RNCaRB2IxWmaVMmkny1NVK9o506hL57UnwXEX5TBiJN8x0DsqGQA85Nm3ebHAFgmJox97HPWgebKtHJ8IQVNpWORA4ohX1N_YODpFqjIyOYBKMohBjNhYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBFdPH3gy2cy9OmQrMAByNMdupj6UQm2KiAzEYz0ZaNrRFODPWWZYWNpxPQCxG5WFkaBhYnxD9DC6GhGZDVXD15u0jvj_SAHGPkAm-XiaE-TfKAVPqj9Yfj1jcagsJx6wSSpkRS7qcFkNeaW8FEKbUas4cqjdjE_tILkaoyniE9sz6ICW3wo08ZD_BiR5UFui71j4uP5ZhmlXdtlxliG5XrKEC-6op0ME_y8BBgKbVdD6H4XDSEyfgvZ23rjhNDMV_J5qqewBN1NA20-b8ZgUh86wjAfG44W-KkLg9D4kjJnBIx4GLzwr0koemj3xBmgySxmg_1JHHPpW7fydRmUQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M9gTnAKnyqWcBAbTFKiLEVBDPLXuDc2e_IhCVFkExdwUoUJpCwc_csH1TPtHiw0VLm9krFjEmOiHGZbwgHoGT2oP79bo2BtAkQVLC2LboZk0-T8mJJTmdNr0HVzqs_WpCjixaEcmvRCdceRrmb37qNzFcdKcsb2adiWESZ75CieiAoKbl8s5f_erMYyJDa3WD_XhHVBM12NKBtumwBk7WopVZMTf9mZS1jC6Rqz9BEXzS5T0OmBWKZG5ZVHwjzcNaizxUzuT8BS_cY2SVmqAuhg4W3UhXu86V9WT1LS9Udc4LtMm4DqUDus2nA85y0BQTu8UX6UxGdjLdX5_zzuTmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwtB0MhRogCjarB6Fqlb-R-wPCQ4srZP9DwxRyyhiWjQGqeQe-41KLZ1Lq_9eSq_YTHHh_uqYWwF7W-mZ6jZaV_yGSjPSjXQBhpjnYYK8v_Y0j2JX7lxwaO4Pn82IJMxW9V0Bk2B-KOGz6PCh5MSoO_sOyzOzIw2iA6DcREFrmyxaZiFtoFfTWKUtLHPDsCpxsCsWF0Apv-QexM0METIQiT-o_faYjv5Kw7eLjhTVeg7k-ZEM94HqHW6X4V3uye_-7kYotz6e6_wpqc69VdWaVlUk4L7PpQirWLcC7WAQOgXaC9vFWUlh_9VRtjhlxsv7IiRYHp1v_5L59_0mpvuSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2yQi-J95B22kM952-8fkJ367pCgHNuJBQOs09fv4ej0qs6_ot2mYd9nLSNcklECcBBYfLhPDO2vcNNBb372uzhWdKGWyEKeVfG_549eWvDEvBsZoZVNzNpKfH8yTwBOhJ2x7NP5vtQewFcd3_5mcn2btBQIHyUPGLh-LpMJ8B89ioJyYKHBQAW3tGylM2bQFwDd87MZT6KyYMInRreXDfJ4y3lwlmgl8TDXai2wX6rA1SinFUVjXXxQUxaAc0x6Ye76mbZfUFOSQkbP2U0oiXqqEPSweMlp9wmCyUhBfRgpQ8FDZQh2GDy_KRvV_T6JJCAa58ukzUvJbfQAxVI58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ytxc2_JVl_D72nj8hUDWr7SafOQQBNdbcJFvMLbYHqEXJ-Nf2jPfrXhFmtKs2fys_8Zz-z7Ly1KmyOYWiM-uLeMadl02A_-izYJhC82lBATVJEUGfJ12r6iDt0qMsMI6Ieq7YJGP_Pml1EpvpVm38o7arff2XYAFIbpe_eAb0H7WqiX5HtevcYYgpkEW6V-mwcG5lXq3YTdXAuedX4PwveBjjV4aHftQPC27TuneNQs5xjCeEixGtXrSUxLl2Pe83hggsknyQB-YLM1LYiVIoBnD4GFFFrR-H1znATg6_uGj6cqCrz9jJpnF3Tidt98xRkFthpSHCH4IJihx3yWKBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=uaWUxebXKcWLHsc69imLGfB5TBODTlCB4Ut1DuFL6q_u3VKHunvFT9UEPD79qv-Qn1Ob2H0iw28MJd7JC_TH-1R9wERwIlNEzCeQJWcN9tiv8YQLyfZCMp91ih0T0QE61Nqdqs6PlBysqYxym-1PIF7mqGlnkG1FoToTUeUsWCqzuF_HbUfiw6ktsuPdMo-ID4yEj2ky46Wbg_C0QwOmlrYBbIgRFTeMqKSqeZX--lpD-U_6ETMsSni8mYTfVuFE73rl2yVBa4RewA765k1f0qTx2hVIyte4b-Ls5l60rKGrLEWxuT64y3WFQggeEFqq3B7izWbL7cEfbhBD4hK4Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=uaWUxebXKcWLHsc69imLGfB5TBODTlCB4Ut1DuFL6q_u3VKHunvFT9UEPD79qv-Qn1Ob2H0iw28MJd7JC_TH-1R9wERwIlNEzCeQJWcN9tiv8YQLyfZCMp91ih0T0QE61Nqdqs6PlBysqYxym-1PIF7mqGlnkG1FoToTUeUsWCqzuF_HbUfiw6ktsuPdMo-ID4yEj2ky46Wbg_C0QwOmlrYBbIgRFTeMqKSqeZX--lpD-U_6ETMsSni8mYTfVuFE73rl2yVBa4RewA765k1f0qTx2hVIyte4b-Ls5l60rKGrLEWxuT64y3WFQggeEFqq3B7izWbL7cEfbhBD4hK4Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZf_EFkZ0SvvoR30joUc03bjGvJ_5_OH4UFf_5iTLWPugoVsdYJYD1MSPYIitJSLv44bmZhNz5qeNcJidUssfTZKiJbIjpkpbzEEWjilQ1lUl7Pk2bL8oiglYU651T8FuqpWMIx85OCy19la6VWCjvwXyBrHMXronVnvMWIqfzCAs0wzTlew9hgF0_JaryzBfK6xNOrSOlTlwAKIRnGiqxuq3E4QdrvUxKEoc5a5zZmXdssG9qtFreWK66MNU9IO_YBi045zpVmUX3_LTADoH92_Xd1iJn36kRZRO-9HO09WGvHnTWfjzcRg3rn1QHnW1It87uLaduBrqxeVBHFcPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NO7LGrl1HK6XJmBRRQl1owlj0KWgSnXqF7fvA88WCIiofeilkPxTsJkgt_6WR38Dyl03FV0I74LrcZXaSMo2G5XBc9hThiqCE2uVMKisLlPz84R2_AjklJ_qi-jFvJtdt5qxxDltTmh63r6YnzC8-GxsG8L08phQE1u_zod1E6EuEjjxvUh387hEnGITqzBpZjPGQu_zAaWEcPf_bJLYv5ImWKEZ19BqcxgPF4WvaPU4YXvIzQPYWQJbzrK8b2wDnqNmPUakNPEA3XTxdPap32-fEPwWWVlcWEglrHf5vItaIjjtTpFUt1BLzDM4NeWp9wfFhy8SlsAJSHN2EVaWvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMEPDmF-DvjhAEPTcHWVpc-CccwIgnt2pyZSF4BIoIblYPy76hKCcOlvp-gwPMGtrKQY8U9JQyFyZaUVlrfsght0-8zDG8AGPJ4gpaPUq2D0gXxq91X3wi6IupEy8chpVlpQaThqx0rHZyxnPb_XgJ070IImEO86KeHGK_JWxHcIDTzrrwKVX7PoaZhAQ6YTZ45dvagELdrAzmsrHPUx53p0IkxiM3pjo50jKHFL2BOByFiluWwzc1iSRHFW8ky07BzYHoVgTZDDewZDEoHfd5iC01KSuqpaf0e1cucToPu7FlL8ow_QUClGIvAEjHEyXgZbkizcykoqmXMf1dZEXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoYXPVXei5TMRBcVNltUwq-VRXOgw9kxMzLHsOJvukqJrbzauTctXqCBap5Xl0xlLSrRYqaCHHp6o9-817ysRZXfPM75Jyg281NnCUZ4IOHhP5r9GpvpJ4lkNkYLd79YJEAfzGhe1KmFgqrypLreiHhONZXssMd3qL20yvaAK01AOhZ6xvLGo685S0D9qjzY1I5VN7ZwPVYyVRDVJCRerdJe2j1SwUIrxnPXMsbunlAQaubWBFOO7mwpdQ0P8DONxnEmhoOWeA90RQ1Vk_mhy7LwGpmvKfv4B07lsXLmvmDn0zYarfpWuEPIXTu6HdETcCjbJ9x3PCSPuhWdW_iKjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qaH6kk4UskvbR4cd1B_7cTC8L2Cqky0Rc9k3SEA4CIeUkPr3ulNN1B_mNxbs0xo8LSW685UbMoUhoVv4wKIspSFO-GzIeOe98wF07N9R2IDbCKqyWWTjItgSgMgBu-GtvvQrrjFztC4JYcE8DWpCGp3AM71Xymt0cC_I_r5JT96N41Gbw3__fTma_Xaqo129jLUpO8QJggoa8MScyosBBhGFsoJPV9Wvn9wgzAg2g0fbrx4xTumYhLC56IEb9eOOE2vMxeGv1_cU6JkTYkiOI1IUnbblzNM5DfL-0VPb0amr8UgWCoGTdgMysqarxzKoyNZ5_3KJ5TNrKfwDxQikfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHKJQ20luYNsfvyQymvnaR9EOgTs8NgxGTy0nULu5MYmZC-tJqdeSr14DxrtBpvZlhkBngNAZg5y_5EXncQNW5goMM7jfi4bmQ2nXC-Rs5nsahw0Z3WPPAeWPeolvs_nfa-mvUroCOUpFOZqZNa5vi0f8kepUChSca04GR3d8vEyR0FzhLqRVu3ltfWs3fz6XBKzg26tLhlapa9x99QmtLR_LUBicOGg15zSirty0Hm-P-PHfW0HJ8SPqplEdvH7W3xHu4TyNFWFrKKG_h4b8xx1NQRXTdWzDdlBcMg452f-vlIcLVi7p6mVeIfWMqcdmYivtkmYsCWPjP-hr6GTmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoRBDUcHOaxkhHr3RcCKrewrbG2CC2IkE3SUxt068CHUNoKMfTs2l_UfW5fjXI0JIZWLycRILxuceHULfISMsEixG87aqfTZq95SDFxZ_EWMh_ykLES8cy_4Lugc5BOaGaeoTP77TyhqrbhA9oIj5io5OEfu-E-bcgIn1FJ-QwAB4KN9d97xaEsn4TA7mtHv2nMlWqjAAZd29_ivkjtzmSlM9cu1PNSXTkLkFV3HSyw5OyH168ZRqTxJGP7j4SAHpgLMQC_6iC3ociS-GwXauCtyoOxIvYT2-j6dZdxLmE5rZkwx8a0wi9Zdwd2ZhBgXIMzkbJQdDM3FC0lvSiK1_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVR_-3uRwfK13tXjPmz5my0DukR9db1iBwxXwi2QCvReOcaDTDlqdQLApp_ceb-O_iJLTdhhTsbsuTGiH8JV4LxFiajHJsgfPsiuTp-XLqEXMeFKPDdXJhStT2yNqQ8VCUhhTQcxA9y4-OFIfi4hb2G0e4abnpiqyYQZLnAgWWLfB9zViP_TSxTVJERUcbI9tmo5ZfvgJLgGm9VRqPgPpkLpSHGyXnwWNlJyCZRNuCWn43aSNzzESoq4v5HouP5mBAbUsaNy99aBbjT_mMsAke0DGSDVqC8b-hEt6kvD9uef6xmMY4jk3hfOaggn7ba_p4AR-kvxKzFgNmeWqBMfIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=XnCQGWWIaLxuhs9Kbnyi9u2qENDSVDO1LXoY8sBC7Pdi0V3F4jeI8qHaqgCOrHPGQK2TqwV8szDGvusf8x7QVH_AoV4WZXqbqm7n32hqZblHD14ojYQf9nI5BNVoHilUM2Hq8uMZOWvvahsllMwvjEEkYcqZ4KmEoThSMwLsyIeZk0k47c9ks9TrYncH0NFPcyjMrnlCzetsCGK_Ef4DKuiguhd6fgYDID50V472f36r2MeGdWhoz5GgZBVcCBjIcYCxeJzD179QhI8K_5q7wKWAjV3s1isdnBTpOO7dCiTVIqL-wECLy4kuP4iudnizkHlxNl0NxOL1fMPQQHDOtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=XnCQGWWIaLxuhs9Kbnyi9u2qENDSVDO1LXoY8sBC7Pdi0V3F4jeI8qHaqgCOrHPGQK2TqwV8szDGvusf8x7QVH_AoV4WZXqbqm7n32hqZblHD14ojYQf9nI5BNVoHilUM2Hq8uMZOWvvahsllMwvjEEkYcqZ4KmEoThSMwLsyIeZk0k47c9ks9TrYncH0NFPcyjMrnlCzetsCGK_Ef4DKuiguhd6fgYDID50V472f36r2MeGdWhoz5GgZBVcCBjIcYCxeJzD179QhI8K_5q7wKWAjV3s1isdnBTpOO7dCiTVIqL-wECLy4kuP4iudnizkHlxNl0NxOL1fMPQQHDOtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=mSkNWEEn9pLYAGP_-V6xsaZ1K6laTZsrRR5rXURqEmllLN0tpuAVVHAqyK4J7PU5YbkABtxt8s5N7rdHMS42NsNojARTocImQuMjB6L_cFDO2vPVtQ1c0m_h8YP953Q53x6WJ8iF1y2AF90lcTSvJQNbkU99r-vwCj2QdoNk_W4SKX_5ISWACMC7jwAjlB99FG0a7ML4Ip9tIyIWffUyXv4G1dN6ZhcuhvN7usILx8N-_zlIJG6M64haDKns8JHjmIokUX9oQRITgwlurD7NbRsK9gLkG0dFJ8CmpygUHZQUFbqTs66FV1ksZO-2luCrCij3uMaPjxD7DoCqL5BmhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=mSkNWEEn9pLYAGP_-V6xsaZ1K6laTZsrRR5rXURqEmllLN0tpuAVVHAqyK4J7PU5YbkABtxt8s5N7rdHMS42NsNojARTocImQuMjB6L_cFDO2vPVtQ1c0m_h8YP953Q53x6WJ8iF1y2AF90lcTSvJQNbkU99r-vwCj2QdoNk_W4SKX_5ISWACMC7jwAjlB99FG0a7ML4Ip9tIyIWffUyXv4G1dN6ZhcuhvN7usILx8N-_zlIJG6M64haDKns8JHjmIokUX9oQRITgwlurD7NbRsK9gLkG0dFJ8CmpygUHZQUFbqTs66FV1ksZO-2luCrCij3uMaPjxD7DoCqL5BmhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=Q-Z9cj85i3Va_Fcxuvq2qpdzH_M30JSqc-_WseDINdGe8iIeVqa7r0RyLGABFP7nBHrGCkbWqb9punZ7frbDBisjrvM3u_My84ORgNYjC0f-SoM9pF5p_cJhOosvWIu074n0UXutoMiowNlhrYWRlq0OlpbFyeeNcqZY-O8n_X9G5r9kVecKzaTDh13V1bK3DlKOBoPlpHV8O9xf44e5mIhFK1PH1jmf5zeNL2keoRsvwVwI_yTzy4MGstGb2yZvE-CbExcbtzLx9D8FAL1rnv12Z--jwoZGB8sxYTJVdyz9K7ENFTSX9U3JoSV4N_Dfe7gG60fAoByNUNFJ0RVcog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=Q-Z9cj85i3Va_Fcxuvq2qpdzH_M30JSqc-_WseDINdGe8iIeVqa7r0RyLGABFP7nBHrGCkbWqb9punZ7frbDBisjrvM3u_My84ORgNYjC0f-SoM9pF5p_cJhOosvWIu074n0UXutoMiowNlhrYWRlq0OlpbFyeeNcqZY-O8n_X9G5r9kVecKzaTDh13V1bK3DlKOBoPlpHV8O9xf44e5mIhFK1PH1jmf5zeNL2keoRsvwVwI_yTzy4MGstGb2yZvE-CbExcbtzLx9D8FAL1rnv12Z--jwoZGB8sxYTJVdyz9K7ENFTSX9U3JoSV4N_Dfe7gG60fAoByNUNFJ0RVcog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=RB3EEMjMl6SFbjNqZNr1NbeMCFA5lXoEn00Hr__-3EslqR5sI4JfOFBDubyH_6DUVVB_iG_zBNnybUoT8oBhzpan9iGOYgK5QpEtJKAMi4rYnHPXot50qjUwEc29I2kWlEaGM1-OtCu00Ood6vZuF6jUVxxl77SXFEAwt1UxYIbDC1rephxgcWunjEokD5auzi3kj11h6nSmgx1EWzRLLLwtySWNL3-YNPp6hQezDAYe-CUxnldZ_9VwxZ8hq__wmqhUYvSwkOgDb85eja0fNESI1P9OMn308Q6KPPcW1_h7FxckI-WsSY5Y2YNlHon2JA1T162nuB-bnH_ga57poQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=RB3EEMjMl6SFbjNqZNr1NbeMCFA5lXoEn00Hr__-3EslqR5sI4JfOFBDubyH_6DUVVB_iG_zBNnybUoT8oBhzpan9iGOYgK5QpEtJKAMi4rYnHPXot50qjUwEc29I2kWlEaGM1-OtCu00Ood6vZuF6jUVxxl77SXFEAwt1UxYIbDC1rephxgcWunjEokD5auzi3kj11h6nSmgx1EWzRLLLwtySWNL3-YNPp6hQezDAYe-CUxnldZ_9VwxZ8hq__wmqhUYvSwkOgDb85eja0fNESI1P9OMn308Q6KPPcW1_h7FxckI-WsSY5Y2YNlHon2JA1T162nuB-bnH_ga57poQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=vEPpwiZPm4WuI6NyRZr_fYWe5mOh0h4BE3eCP_jugykwKgDqvPerH-OqRtrsRRO1PPPJvrwt8a2OAun2CUEpcR5aLuEuN0WyBq2HyoU-zgGn644xaaWnpOpl03HZL2ycbw_RdBetXrJr9pWxqxK7xOluLwGv6oGIcZBYVaJJEvYnbFjkufix6mW1UpkxtMaMvfvzljQ9J8YsxVYuDHntFGdq-SkYWFYyZ3k3QBjWbVvvn4VPwJvRTIBgf6PGIfMg-2dEWtuGdcfVm7HwMvSmkcTa22FiV6SYKlfSDjG4_GELESnHhy1qmxHTDyb4PLp3DEK7PuSb1CYVqugpMwQlXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=vEPpwiZPm4WuI6NyRZr_fYWe5mOh0h4BE3eCP_jugykwKgDqvPerH-OqRtrsRRO1PPPJvrwt8a2OAun2CUEpcR5aLuEuN0WyBq2HyoU-zgGn644xaaWnpOpl03HZL2ycbw_RdBetXrJr9pWxqxK7xOluLwGv6oGIcZBYVaJJEvYnbFjkufix6mW1UpkxtMaMvfvzljQ9J8YsxVYuDHntFGdq-SkYWFYyZ3k3QBjWbVvvn4VPwJvRTIBgf6PGIfMg-2dEWtuGdcfVm7HwMvSmkcTa22FiV6SYKlfSDjG4_GELESnHhy1qmxHTDyb4PLp3DEK7PuSb1CYVqugpMwQlXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=Wgp-ePCi4s6k6Y5eaGmU1augVsL-rtIGMOxfjpRNEIEv4NVumpSskv__f56iVlN62D6K1rbUUvnINYgNP90YIYGreMVyJVUte3OY-umN0JPKpfwXD18VbUrq2hwlP5_xDDcnadUwNZ9kJlZmvBIqrPwzgNncULG468m5kA3DCv9Rocl71yoOeHYWeCRkXymrFkScv8at9ai27RM8YTOVhbnOA5wYiYWWe--LAtIsDk5hTJnrvb9CLz2GYIs_s9ZK-w06pEEBM6hy3vC8uM6zWWnIiom6715c5VxWOAImkGjeYXmPhX9dul1PEJAtyqKYTXAMZVDI5jCeyLC4q4AHQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=Wgp-ePCi4s6k6Y5eaGmU1augVsL-rtIGMOxfjpRNEIEv4NVumpSskv__f56iVlN62D6K1rbUUvnINYgNP90YIYGreMVyJVUte3OY-umN0JPKpfwXD18VbUrq2hwlP5_xDDcnadUwNZ9kJlZmvBIqrPwzgNncULG468m5kA3DCv9Rocl71yoOeHYWeCRkXymrFkScv8at9ai27RM8YTOVhbnOA5wYiYWWe--LAtIsDk5hTJnrvb9CLz2GYIs_s9ZK-w06pEEBM6hy3vC8uM6zWWnIiom6715c5VxWOAImkGjeYXmPhX9dul1PEJAtyqKYTXAMZVDI5jCeyLC4q4AHQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO97mc1IvHgSMvFm31P31QBJ633gA057nGm5kDo2ncv04OFx9RS5oDJfY5xQuxQIXeK7CcXwEAj6lnDNV1lnluCr4bYBH91Y-SbmsTHGMV55MUdR0ljMICUFsOO7pzgpv10cfWuTnN1O5ibzsrPTtDEDtvxSsC51ekvy_5qm3OK25mcif-Jqjzs9xAU5cVr4XwsXK20PvSHitQLEVjPZVf74pkJNRyqXWQRpT5_Mkl42rqFJaoNxFIbcAt6h88oiXyhiPktn7wZxqsa9Z00Svn23Sq-csN9IAOgDoPdKdDFT-U2ku_HvtZyb1F6a9qFYDX7NmH0k60hF8XNwus5C-7g-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO97mc1IvHgSMvFm31P31QBJ633gA057nGm5kDo2ncv04OFx9RS5oDJfY5xQuxQIXeK7CcXwEAj6lnDNV1lnluCr4bYBH91Y-SbmsTHGMV55MUdR0ljMICUFsOO7pzgpv10cfWuTnN1O5ibzsrPTtDEDtvxSsC51ekvy_5qm3OK25mcif-Jqjzs9xAU5cVr4XwsXK20PvSHitQLEVjPZVf74pkJNRyqXWQRpT5_Mkl42rqFJaoNxFIbcAt6h88oiXyhiPktn7wZxqsa9Z00Svn23Sq-csN9IAOgDoPdKdDFT-U2ku_HvtZyb1F6a9qFYDX7NmH0k60hF8XNwus5C-7g-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iELpYydPiyisJRGp_neTbfPj3TWka0dW77f2-qvfG2OKMSnU1EGnU2GH5wfY08KHwF-GK1vHmBf5pdUIKVacLeqxPFdvYCKZRNEFQPtR19RuwvPhvwqJz6k5bc4Dd5Ud8966HDZaIz20d72Wh_ImaUUcNFIdGXi65vw6TxhT1b9XCO4baPRp6VRVW2KShP7bgOVGURu3kmBkzDWpvw172l7xrVhbJ3Vp4BIL5dZpn0KaglluPkkJX2cPbejgvvKzIRC6yqey7T1MooLEu6r3XM-96PbFf9975rIN5K3h3yYQbapPlqfBsFOcmj4LMZpRe00azXwiKoBq4mLGSH2LDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=ajnbxLaK2L6dmJwTThbJr8ZJ3YakwQ8l061kPH_xRL2w7LEUvs34aHcKGIRcYr3XAdFg0w8lqh1LMcYihZ-MT6-uEKlz3n0fOYSzdEyrCPkoj8_l5WX2kJzUf9C0bjTMrGrwiOsmDBUhcHa2CcntPRbOGO1jR0cybnh1_1OUcARk0sOVPR6cu4KcCG2GeohntsoCh53SimXsKOLuJn1rhoZBtVyCQ7fiGwewY3G1JDbuLH_XWX8YGKU4VNfQAbRTfZJ8FNrx9W6MxHtt3jUusUgvFYRDgF11mN1XMT92zFLS8haW7VGrUDL_CWNn3Dbgzf7QQobJ3NYtUoGFOo-AAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=ajnbxLaK2L6dmJwTThbJr8ZJ3YakwQ8l061kPH_xRL2w7LEUvs34aHcKGIRcYr3XAdFg0w8lqh1LMcYihZ-MT6-uEKlz3n0fOYSzdEyrCPkoj8_l5WX2kJzUf9C0bjTMrGrwiOsmDBUhcHa2CcntPRbOGO1jR0cybnh1_1OUcARk0sOVPR6cu4KcCG2GeohntsoCh53SimXsKOLuJn1rhoZBtVyCQ7fiGwewY3G1JDbuLH_XWX8YGKU4VNfQAbRTfZJ8FNrx9W6MxHtt3jUusUgvFYRDgF11mN1XMT92zFLS8haW7VGrUDL_CWNn3Dbgzf7QQobJ3NYtUoGFOo-AAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSyTs-SRNvo4lIColTC7co8JZxCuc3sDMxaONrVcF5LVv2zQNs46YNMAK7gFAyScTbNyLEL8StqTGWmkXAr5eNME4jCJ551WggOrXXKDDF6uJi0YJt1Yn_uk4qVDVeFb2rx9b0fo7s1Id9OOPx0RVh2S7i3bC4J5fxXSaRnIbQhOVU3uhxnpC3eNfdaUek4j_iufiA3zuQ6Sh7bvKKHfkWyLTMk38ft3o4HZeainw5c74c-9EuKzRVxnW7NUmbKZe7rPSNAF1ai817VlITo3L0OjZDcSI4EMt-sAvt58tiWvzeCojyzkTwzi8ESJKgHYv_JKKxHCi9RE7x8BF5wNgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1-kwwLTO7trJuPtKs4_-Lb-4yDf__4Sv61_khvzZXg3HUkDyZcBeqNLmgijWI-NCe893N2ixpBO4hOUyYN75kMzOx8a_ByV_GZcJXfq_tlTlaCbme8QNoyn9uxvRU_IeHVXbDWIwRE-hCUVbVrFOkG_bbDSvFqnmLFkxEbQU6XdBtMyMVMBqD9bK-Hc72SFXLGZ4pL5rfmPk-MGqRkOb7LCwzsuUovnwsJ_V2saLemlGPYpAa4bnunvM0UwsKcQGT4QMtiG0riwqU2aidJFiCD7zuPU-WvToTJL1beHq9yLCuZpLqcQWO-fTsWWdtt8P2OSr-YWmYmKLyxlhnZLDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBSPPj7JeMpLIvfediy9FLa9sJbZkudbuZIhXLG0J6P1e5HVSmNm3aw8tV2FFfj777hcx9r7yEmEI1QVwaN7y2xKbZE_1ByVeK3s3FVgpSi70QwFTAft1NBQYZ7L8lbVVNqn7HtaDIUSgfyx8AVorwar5Z_A45lw8Lvzksk8Nc-wGHhkw-KbfUN0QCRQCSC05bh_0Ufy-JvFzanVMtGF1VNkvrqApdZIFute6gyEj8AHqOr9JGoM9Rml2ZFb3GZjDR-ZWtjoILRJb49uShBV4GTtHnaOTc_ax4_ga1155gPRzjOW-fjOGX-xihIdKLR-d7AaOnZ0fmrU4oI_9Y7yVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=q5nkCTyclN59tqAaFC-_aCUDNku8pjYaKJ2f98mmRyKQe2gas6bQlLVnRrbMSlDw4ziKPk1DJoRS5-Ig2dVFEETbWZBzLy86ncCzBxhClRNMWmb06CmKgG9YjphtJU3Oiu5QqPFgVgl8tjNgl5D78vwLDaycS8PmrktTmU-LjyZHUNktB784PeJfwV_PXOKXkTI9pAseg_pRv4go3N5w8F4NH8Z-0f7GTYNo-TGZW75HswMlgVaFEUc0az4CKDALu6ubcZdh6egpRpyz72cQJdU7dUACVVAlrqx9wFeHOetcJOtPh4GEqbEAqz5uRPym7O_ydRPeWCDUYyAQMxGvQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=q5nkCTyclN59tqAaFC-_aCUDNku8pjYaKJ2f98mmRyKQe2gas6bQlLVnRrbMSlDw4ziKPk1DJoRS5-Ig2dVFEETbWZBzLy86ncCzBxhClRNMWmb06CmKgG9YjphtJU3Oiu5QqPFgVgl8tjNgl5D78vwLDaycS8PmrktTmU-LjyZHUNktB784PeJfwV_PXOKXkTI9pAseg_pRv4go3N5w8F4NH8Z-0f7GTYNo-TGZW75HswMlgVaFEUc0az4CKDALu6ubcZdh6egpRpyz72cQJdU7dUACVVAlrqx9wFeHOetcJOtPh4GEqbEAqz5uRPym7O_ydRPeWCDUYyAQMxGvQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COIpBG2TjDzvCPPrXvcL8aJ_p8jidkWqAAgpw-oSUKbFsTdXuCxofBAlIMMucINHqCzRinBXFGpbUqjUHMeRRM5S_dkZ_hndCOqQzE-spAMgUYr5jfIrDZ-Cs9Kl-B3XefJv9UIQGgHFSMBX5D-XN_1uy7fdnXCyCqldvZdZ5t6MaAomD47XTQ83bHiR_J_p0Gzq1IL8F5zT_8qHm4Tlaf-CWMfAvYiqFaiPfAKB2-unzu8JiHmIdSToEV1RRp43B6o_L3fV2TioXDesdGJ2m3dWkF19NNTqx3T3QKsHM0f6fdgbO-grPhCKm5JyqUaedIvifNtwr-RL1IHG1Rzehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9Q4it2fAmWhB-Gp2rgmkankNncK7Vo6dAUB7XwL2l1tE3t9CbO77vb5-gxgLpsPgX7uxVD2nMDZJYblPH9IqOn7TYk8eCPeD4kw4zcK0vWeyHs6NEyOfb4VOovDVLl-sHcVSKBQQTpbT1_wmoHbyXRxM4BQvTZbwqwFrG8HtgKulIF5CBs0OzrNVQni8gY9GoFP0Q04-hIbmyoYuDC1jiLGiYsQJbs1KkTkzeI7ytj3tkRhyiL9fhyfaH3o8CYo9HVkhOGlc48Yb671KdmuvSe4FXTJdOFqPqdUE0YpLqHE60ozzZS-mbVilsvt06K0qlHtw3ktj3GFu04qVye2gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_Mxk03E2h5GFG2D1MDXL-LHB1cuXNNA6gE6Gig-bTwTcP7KknjVHI4_H-Q78yL1ZdSZcizrcA0bp9sfhMsBgl2RohaszNenv8I49FKPbVbUpZP8DfyRJYCEdLcN7bJsGkFPwVby5Zms8q0N7OnxqWHIPwto9L6Tv_P0qm6lotge3ibymzodxjxHggrX1zSoleqxTsFPgSl36SZQ6S8BSSkBheDPvJ3m5zK5kITszzziMGNTANsVc49-pPGwL5EDuR68D6ewvfhOeKRoj4rvPGgVu0rTKZ5WZumd9Oujpo4ViBPBh7k4X8ZfwtSBcVtixzTdjuA6IWBhakDynKnnOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kD54N6fggL4r3ogOqqqXy_GZy9Uv1t_CqClQd8VZemw0Iv0LJ57txbQGqCpAHIaV8t5_qE_WQY2aWp-Nd8nncu_wv_d2FaZG9N3LwqUlGrVqZxGwSTviogleuS-4nP5RCFEydhY2vH9zm-lVJvBudMr8iMiZBFVIxcbcjflv1eJkG_fZnk0Us5m0yzuvXo36I5pZq3CKnLYu3lSHmCxT0f5wwIrIkTEXtAVdizoE0zI1fJDZH1NgrRkkK9i0BfXOVM70lQydot-FvRtif4WNiN9jMqk8dcfwxtiTC9608qJ0Y9d3PwD2UwiQKCQuhAU5jLUz9oGISemuWxt6X6BwFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=cdOs60nAGxjJ1bLBl3ikvdtZb0PMsbxagQ9gRLfH0JZavOl2sMZ-0md__2J66GyCYZDmAkG8yemNde9oTHsWUYzaoZgLPfgwSzEMS9pRHttdlBScSxD_gBL0YXLBppdNJwT2ftNTlCxIfFJWOpjaZv3_cYZtiQADuOGAUNlgcZZ8DstPyXRFB7j3CAzNJoCcyfoPoY-vLK69u8oYk-viR2w8d03WTC5EdZtiTblvj-kmwX7cXxv2m-0vlbhDIRVlwTlLhNEYFtGzH-zUhaxsHwoo6Brwvu6vgjiboo7tKWVTOEEWFELRKxICoRIp9axF0oe9NlYSvIdMybGgbFZrpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=cdOs60nAGxjJ1bLBl3ikvdtZb0PMsbxagQ9gRLfH0JZavOl2sMZ-0md__2J66GyCYZDmAkG8yemNde9oTHsWUYzaoZgLPfgwSzEMS9pRHttdlBScSxD_gBL0YXLBppdNJwT2ftNTlCxIfFJWOpjaZv3_cYZtiQADuOGAUNlgcZZ8DstPyXRFB7j3CAzNJoCcyfoPoY-vLK69u8oYk-viR2w8d03WTC5EdZtiTblvj-kmwX7cXxv2m-0vlbhDIRVlwTlLhNEYFtGzH-zUhaxsHwoo6Brwvu6vgjiboo7tKWVTOEEWFELRKxICoRIp9axF0oe9NlYSvIdMybGgbFZrpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUskUelKMn_mtOmgxyb_xJ48nhdhDOo3PqnFFj1APmQeuuhdWsTWGw0j38Bv-seGksoIsaZOEsbcsAklEWXuBc1sAb5drQLzv3iak2ywFtd3kCOK9g4RoNvQBfqArqjCz7sWeqa1W_Rfyrd4MR6jqhilV-Vi8JVszjk2A9JRE0APVpFxdt0aLOoWWRYz_AQ9KWZJFt1hGZd2r86Eb_OVVuSuzciQD8b98rIYSFAlqEdz5Os0ThZbeXQ_BzxUhWe2rw8Eu0-PlTllmobcraP-M-7rzZ9KF7jyAIgl9YLv6rdVQ7910PtQlUJca79Ca2zWeUwqnjA91IbCBi2aVB9nvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzRbFhLcg25Ql9Y0G_EBJpUH1bA68AypUfK1uvKZPoC74oIlgfMRRGje2hJ0iw-8JzesISFJTrHsjEk_jRv0jeIz142h8rPs_AxQ1ldYmCAW4HSeWFTMlYp4OFG4-x5IP2GxwWXTdsQ0zIg-rz-gA3GT7Tg9ltyLEJJFoEOVJSiCV2iMhKtkG9T1V_YiG21782dP6-aqwGeZMeY3Vl3NhwaFUj6qZgAp1VFGqk03br034Uo1_AZBVUok-Xe7RCNHFzc3C-K3sPYsv51VVlg_kwcZGn6w4HQi8dWgodob_pZI8m9ARIaA4kxrcDqTTg_B3NOvmdY60AzUUpZw8XFUCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=NZav4u7pBoVeJ98aqg2tTT9NVMqyyNLDcCUC1XyGjgp1rkSHGNCLyKd4TRRRU5GqSjZ3PSY8YiQbyBx0IeaI2wkEZpi9hKBasjPK-oai-y6q_WBItcGxj5kcTSveCpZYPSd74JoRq-bVp9D1FTDZ-loYU2pt6jLY0zuKWrshzaHxfG1VDPIf7TC0xVgfVGSMaUbxYlaG0TOZfhB7SHDKzJhFlPsOWEfUj0pVoc88Zy53blsgnLckkNVlkG2o9o201Lb_HjxgjnS5Giud3hSkQaee_v82Vjs8x7zkVMgDUhOZnZRyBO5kNB9-OF1jpVhk0QiMnUq6IF9jPuNmkq-IKZFADzXF-BBrKHznf4KnHar7gW0tWUbrb5JonXwCZA3qkngsTcQFcSapLTZZmfsb2ZF-5GU20SpO_81cPIrMJvhtzFo7QB-id1gkA58Fg5xDahbpI49kkgaGlFBEEMzt3zjvHTnXdDjOh0cKbxHB2xIfkJY3De39my8s9nd79KX7eWupV58tVq_rSknfWyvPOzxACujOsoGZpZlFrRQNRc_X1azN2_ClCQS09rX3KbNXIQa2p5dkrowUyaZEqlwJsM5AlVd22NJLnES5MPNrJu76O1RYt2FBEfxFE5B3e4OiFEdsh8fAM5EuudlFoVVthX3HVQYo0DNtAkW6e2ub69o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=NZav4u7pBoVeJ98aqg2tTT9NVMqyyNLDcCUC1XyGjgp1rkSHGNCLyKd4TRRRU5GqSjZ3PSY8YiQbyBx0IeaI2wkEZpi9hKBasjPK-oai-y6q_WBItcGxj5kcTSveCpZYPSd74JoRq-bVp9D1FTDZ-loYU2pt6jLY0zuKWrshzaHxfG1VDPIf7TC0xVgfVGSMaUbxYlaG0TOZfhB7SHDKzJhFlPsOWEfUj0pVoc88Zy53blsgnLckkNVlkG2o9o201Lb_HjxgjnS5Giud3hSkQaee_v82Vjs8x7zkVMgDUhOZnZRyBO5kNB9-OF1jpVhk0QiMnUq6IF9jPuNmkq-IKZFADzXF-BBrKHznf4KnHar7gW0tWUbrb5JonXwCZA3qkngsTcQFcSapLTZZmfsb2ZF-5GU20SpO_81cPIrMJvhtzFo7QB-id1gkA58Fg5xDahbpI49kkgaGlFBEEMzt3zjvHTnXdDjOh0cKbxHB2xIfkJY3De39my8s9nd79KX7eWupV58tVq_rSknfWyvPOzxACujOsoGZpZlFrRQNRc_X1azN2_ClCQS09rX3KbNXIQa2p5dkrowUyaZEqlwJsM5AlVd22NJLnES5MPNrJu76O1RYt2FBEfxFE5B3e4OiFEdsh8fAM5EuudlFoVVthX3HVQYo0DNtAkW6e2ub69o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=k-FkYf2dysOjDOWXBW5njHVg3Wd9AmAibcEE4sKVuIesDEXS8ozMihZBxLfAEXIJG0G61V4EbROgNq3W6G2ny6KLeJVqo7PRjbHpRvrl6zSmepYYuh92LNNDJGWjrkyXePqUcj_zTxLFC33cbav171ecZBu2do1DR8hScYAD3Ozenl0zQSN0kDto1H2xgigzGZuWI7efIZBRuDH8G5mSo6w8O1eL7fQkW6ESBhiBIDaZp66rtu31ey0Y-yCoRZgd27QeV7NKV7AD1oZSNpbx9QqlCqPHY3metHaXX6GPSf6PsSmwbf3oAI_N0Hfpi0lWzgLUUJYUhZ89SrB4dZEMkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=k-FkYf2dysOjDOWXBW5njHVg3Wd9AmAibcEE4sKVuIesDEXS8ozMihZBxLfAEXIJG0G61V4EbROgNq3W6G2ny6KLeJVqo7PRjbHpRvrl6zSmepYYuh92LNNDJGWjrkyXePqUcj_zTxLFC33cbav171ecZBu2do1DR8hScYAD3Ozenl0zQSN0kDto1H2xgigzGZuWI7efIZBRuDH8G5mSo6w8O1eL7fQkW6ESBhiBIDaZp66rtu31ey0Y-yCoRZgd27QeV7NKV7AD1oZSNpbx9QqlCqPHY3metHaXX6GPSf6PsSmwbf3oAI_N0Hfpi0lWzgLUUJYUhZ89SrB4dZEMkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxSZPpBh_Q9L-411g3ZQ3jw361f_g1b3WSFRyP7yVCpgsYTHxE4pMIJl2wrhXD-3PVc04eI6aEJACh1Nowsfj1Q2jwAGJrRTnG2wwDSz7qDyFlTUnHbYMzPlnUVgaO1C3_Mc3RCVpmoiYaUkK_YulB6ivJyRR3Nd814e5UJ1xMEs0hCONjwvoiT21P_BJrWOTmKhy-0pvc7lrHauj-k6ucTHd6C8xi58LTKl7hhrdHh21rphE7TYfgVK8IzeQRS_6L3IVwc6JGfpaHixPBzVC0LXPSv-7sYn3d-ANF4-CyLDyJuTSr5g5dBLksC3Pr-Tt9a-0vEst1Yr-BjypxD2Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=G7BNVGxElJTfULeXzbYq_Fz9KdVzN2pAVJiOUn0T9aw1VT7h2v0kKedjGDOSQUdCPvHzifVjc-w4fp2NKSpdtLJzLTXll91TXHqSmtTupmLdQ9bNxfoLPQHyBfmHN5WnwsbSeiwA0Nkm5KwQn3OTYxJncA1izD5mQMXuSQ5W1hVvDVI3g_dbxjx8bUh3B2PH6ludUFRTIZHe0Y1DDptsBpxqjKImSVpgkVF2i7DZ_tGMLk3nUkvS_BQ4n5KY1S6To24R3Q3xYXKDSdiG8TUn49-2hrZ3jJNMvX5NUd1-lHRPBJ3JZLu0Gem1H-dDnvgdGo3x-3nCue7-EQNIQRPHWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=G7BNVGxElJTfULeXzbYq_Fz9KdVzN2pAVJiOUn0T9aw1VT7h2v0kKedjGDOSQUdCPvHzifVjc-w4fp2NKSpdtLJzLTXll91TXHqSmtTupmLdQ9bNxfoLPQHyBfmHN5WnwsbSeiwA0Nkm5KwQn3OTYxJncA1izD5mQMXuSQ5W1hVvDVI3g_dbxjx8bUh3B2PH6ludUFRTIZHe0Y1DDptsBpxqjKImSVpgkVF2i7DZ_tGMLk3nUkvS_BQ4n5KY1S6To24R3Q3xYXKDSdiG8TUn49-2hrZ3jJNMvX5NUd1-lHRPBJ3JZLu0Gem1H-dDnvgdGo3x-3nCue7-EQNIQRPHWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYiFdDH7FIM9URQK5VT6mpN5WmWhB7k4vP4u_H0PUdLMfhu3Fx-qog2Kf6sM-eKOs2pgnVxuBD4vIs32ZMDR3ln4u3uPxXCo9Tp0eCm1xC7dyrjsajALhC9IW9XToFLKR6lNNeb-Zxkv6ma9_Q6xVDnHJwe3oU3gdQvlsv_YazG4N6dPdTuqCvP14ljdzkjAWS1RANLcZx75ueX-PB4pt5HC8HnySmtVDxkvAPqW-PDGNfAhEux8kHPpJAJTB1dGcwAgNZ6KksXq3ZscdMK8uJHa4hR4Pkk7IemDYmsHzmkNF8kRu_3i4wHlFqJqjeu2XdI5-ruMEuteoiWbhtPRyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=d_ttyPZ_Zj1hqnlPyRFuYZeVThQ5rqdB8Mj1M5AySXXHSs7BFIN1uFblF0R06F_la8n2-rvB_PDqZQoMNHvu-NbUqx1tlTlNiFmgZ3zsuZjzitL9CzycO9PeoAQCbeFiLIpis03dPlzB-WkIgWQ0_DFaJcm3lsXRXYUHWmihZLugI7mscMwvgFgZZmW-2ZnqWUNgO-M8Z4xWBn7nI_UKP90LqQlP-_L8DMUGckv31DewOy8Xt5zzh7FKRVSCBx4LuirEpbqxu8MuGzt-sOKS_-dy26XVrZhqkDJL5HA0WWJBvkzVfGUN8FET1X7sOjjhUxuYHLmyfD_b1SbTjgy6UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=d_ttyPZ_Zj1hqnlPyRFuYZeVThQ5rqdB8Mj1M5AySXXHSs7BFIN1uFblF0R06F_la8n2-rvB_PDqZQoMNHvu-NbUqx1tlTlNiFmgZ3zsuZjzitL9CzycO9PeoAQCbeFiLIpis03dPlzB-WkIgWQ0_DFaJcm3lsXRXYUHWmihZLugI7mscMwvgFgZZmW-2ZnqWUNgO-M8Z4xWBn7nI_UKP90LqQlP-_L8DMUGckv31DewOy8Xt5zzh7FKRVSCBx4LuirEpbqxu8MuGzt-sOKS_-dy26XVrZhqkDJL5HA0WWJBvkzVfGUN8FET1X7sOjjhUxuYHLmyfD_b1SbTjgy6UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=aWj9aJ_GBHqukTW0KGVOny4-zii6cRgIxKdY-2xvNQneUshvMsJdhnQctM8D_Y3HC3CCVK8ksNp1Qexv4c2PWG4gosyD-tUvTOD200v6qFkaweJUcqwqnLgnir0VsXaVpvKQrikTw-1Q_yTwED4BzxE2XPFDBrwZY3W1xMqva5y5gi5VOKQpLY7q9DEF3CH_OpbIuz08DlZTG2ZtcTKbwNj0NpPJoU1aKS63n_VZKkQggINYUvmVS2buvO50jQ-HCB7I_OW5yE7Hm7MyLcOr4F9nac0jZVXqBsxCUPuBDW1hPHd7C73Yk5bMmZ5WblfuoCHvRSAJPf1KYzDFCeP1QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=aWj9aJ_GBHqukTW0KGVOny4-zii6cRgIxKdY-2xvNQneUshvMsJdhnQctM8D_Y3HC3CCVK8ksNp1Qexv4c2PWG4gosyD-tUvTOD200v6qFkaweJUcqwqnLgnir0VsXaVpvKQrikTw-1Q_yTwED4BzxE2XPFDBrwZY3W1xMqva5y5gi5VOKQpLY7q9DEF3CH_OpbIuz08DlZTG2ZtcTKbwNj0NpPJoU1aKS63n_VZKkQggINYUvmVS2buvO50jQ-HCB7I_OW5yE7Hm7MyLcOr4F9nac0jZVXqBsxCUPuBDW1hPHd7C73Yk5bMmZ5WblfuoCHvRSAJPf1KYzDFCeP1QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
