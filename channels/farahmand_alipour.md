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
<img src="https://cdn4.telesco.pe/file/YH5RcJrLUcOruxWu3KpnGwAfc_LPVJIn7ZuEVpV5LtNQEXvzEgbpgKyiMQfdTgMb9S6St99sjfIOTEIZd1x8UKOl_3qmSrnNd1w6kdwxIgq18orT34UuDhNW7X6Yv-IBe6GQxRRrlCqNmB4h53FYzj0HKI5Q1HhZGP5dJKvJ1_MefUvByvLYXOkAWBoWZG9nWEFWW27cyv2UaE3zJFKMJE1jlk9Sp3WsiTcU9IcjUicskpSU3sgVL5b7A6JyLXMvMfKI3KZMltQeuDwthJQW9CvQ12zE-Wppc-rIj9UO17a6omPlSlCULJhR2ox2VPDwL_TQZyWnkW81EUu_7egeoQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 01:10:31</div>
<hr>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5FydOHjNuTiD-8dDiS1igzC5k5pshIFfTHl2n5mgU8S3kZRWMsQhY8C92MOm9ZmgRZUCiIIY0qq-Ai28TQgY7ccJf3UxEW4q4KRqi1X5soa86tpqdhGSXe4yvtZWBR2kHgyovliJo5ik_F3hHxnsZKqMxOkg5ZCwN3HCN0c1kh4ZT2cEcGxVLgnqVTlmQJTvU3GIcMXXcxnsfsiWOvgvxhmJ_AfIAgwOVVOVEY0gWnhAKMrXmfkHv5Isef_oXexWsF3MFT19WBei4CEEx2nIoPEASKYs5QaNSFA2YjdGoVT5qRbrOFhmlU2ceTHLLnnpGwAx9FV1ngjjujeX4d4HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=qReOBQgrkZQrlYWw98392ezsI9ESBAwWh44ySFRQl2ftCTBZrr15ZzaPyoQx--jfDixFHTngGFuIWesZV_QjEtmJyzM_MpsVGtv9Z58IAc4fje4QTMEGCpLi0haHmH0wbiyPsikTY-mPghf5WhS3rOcGxR_B4tUuRFUJm5YLv9q3sOPZcrMmKUQuk3O4WJ1_2vSQQV4F9q1pEsogzFESBkKqeRCZbyKc-Oik77lehJDIMsgmBmnwWqNWqkD56koQ4A1gg2y0eDWdoG7TSKbv02afHuycQyKOZ1vZrHsdw2fc7kbdk-H6OHvRT6MwEJr3uH4eh7Stg1BTDEseOTD9iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=qReOBQgrkZQrlYWw98392ezsI9ESBAwWh44ySFRQl2ftCTBZrr15ZzaPyoQx--jfDixFHTngGFuIWesZV_QjEtmJyzM_MpsVGtv9Z58IAc4fje4QTMEGCpLi0haHmH0wbiyPsikTY-mPghf5WhS3rOcGxR_B4tUuRFUJm5YLv9q3sOPZcrMmKUQuk3O4WJ1_2vSQQV4F9q1pEsogzFESBkKqeRCZbyKc-Oik77lehJDIMsgmBmnwWqNWqkD56koQ4A1gg2y0eDWdoG7TSKbv02afHuycQyKOZ1vZrHsdw2fc7kbdk-H6OHvRT6MwEJr3uH4eh7Stg1BTDEseOTD9iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXI-NPoNnSo9x-x0kN-Lxb8ulmgsGwDuFLiF_4idoyKe7rPr0h0CWp2H9tcE_sqvgO0RbIHn7LzIJiZlcnk0SQfmFc932I9baWy-q0dIIbn-kkGW8TlZI1d8gGapvgupmbTZ0PabY3qRwNbMIfLGPU8AYYMJH7DhFCG57ffyM5XTQ-_X6Kd4Go1cUZoT3Ug9lIXTXO1o5rXSu0n5XIziL4r21G5fsAy7hkZSKMTAjU4AcXmv-lWwmnOnu10LeOlhPMnnb9hDPEK6DwBoufIzLwtWywO_V3uFLitrBj4mpOZ56TWzn7FjdiCY-jjt5hIctkgiCJyUQ527KB14Njpc4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=T_8FELIfbtUdJgPAMNpgKovdevVEhqB0Im0UsD27k6Er1aGL9SmaDLqcpbyeXN6hZ4clZ0vMzdF6ABvNYmtSrCO5fzWT5yfbzT66j6yrpJcQiZZOPbJADmLWYItN-N8pDdqBPAaVyS4KHO6er4SuAaI1VYDVwx1zEC32GOg1jkFecp8WLri_oPH8n0fZ3nuiwQxY6sk2MHmXgD193ouR7LiLPOuKZXNFDAlBlA5a4XFoYfszA424_y1ghu2ZY0mIV6cIN7RNeu1VXSqq3cYBGckfngoIR1lepGqWzLu3KwmIPthNF18RhTB95lpR9RM3Qm7s-EuZRnS-b5b1PDNTmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=T_8FELIfbtUdJgPAMNpgKovdevVEhqB0Im0UsD27k6Er1aGL9SmaDLqcpbyeXN6hZ4clZ0vMzdF6ABvNYmtSrCO5fzWT5yfbzT66j6yrpJcQiZZOPbJADmLWYItN-N8pDdqBPAaVyS4KHO6er4SuAaI1VYDVwx1zEC32GOg1jkFecp8WLri_oPH8n0fZ3nuiwQxY6sk2MHmXgD193ouR7LiLPOuKZXNFDAlBlA5a4XFoYfszA424_y1ghu2ZY0mIV6cIN7RNeu1VXSqq3cYBGckfngoIR1lepGqWzLu3KwmIPthNF18RhTB95lpR9RM3Qm7s-EuZRnS-b5b1PDNTmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخلاف
گزارش صدا و سیما
۱- بسیار بعیده آمریکا و اسرائیل
به جمهوری اسلامی حق غنی سازی رو بدن،
۲- غیر قابل تصوره که آمریکا
کنترل تنگه هرمز رو در دست سپاه بگذاره و چندین کشور ثروتمند عربی
رو بگذارن گروگان اینها باشن.
مسئله بزرگ‌تر از جمهوری اسلامی است
مسئله سرنوشت منطقه است.
۳- غیر قابل تصوره آمریکا تحریم‌های اولیه
و ثانویه و….. رو برداره و دارایی‌های
مسدود شده رو بهشون بده!
🔺
اما اگه این حرف‌ها ۱٪ درست باشه :
۴- فاصله میان جنگ ۱۲ روزه
تا جنگ ۴۰ روزه حدود ۲۵۰ روز بود.
ترامپ بعد از جنگ ۱۲ روزه گفت بود :
« جنگ تمام شد، ما پیروز شدیم و تهدید
را خنثی کردیم! »
۵- ۱۶۲ روز دیگه در آمریکا انتخابات میان‌دوره‌ای است.
ولی شاید حتی پیش از ۱۶۲ روز دیگر،
جنگ سومی در راه باشد! و شاید پس از انتخابات.(با فرض اینکه حرفهای صدا و سیما درست باشه!)</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=H8WqJWu2QiTWI8PqQ867AfxJ-6cmg4UAEyGRU-JQd6HtlFUx6VAQEasc8aoCVSVBetTY3ugafbtdlCCY2bQPKoOMURpj-Mr_LGrTQZ5yJzreP0Ul7HfjdnefjXCfW2O7sDhOyv6swCaYfhxKgTnLqpNrFJchSd3D6Mw4is6ApTimF2ZvqCB7gmkd8GvsCKzFj1qlTBfxFOTVnPQ0UGSkSiq9vLV0wdwesVuv9atJA67CHNV485Q0RuUGMl2ooLuNPv15CdIeyXJHK8SqnFS872ITN70fWJdlLYqGpxaGRDgSsICxPqMVPEqlbHYqIZfazdDXIoDU3bkA4hT2aGtlmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=H8WqJWu2QiTWI8PqQ867AfxJ-6cmg4UAEyGRU-JQd6HtlFUx6VAQEasc8aoCVSVBetTY3ugafbtdlCCY2bQPKoOMURpj-Mr_LGrTQZ5yJzreP0Ul7HfjdnefjXCfW2O7sDhOyv6swCaYfhxKgTnLqpNrFJchSd3D6Mw4is6ApTimF2ZvqCB7gmkd8GvsCKzFj1qlTBfxFOTVnPQ0UGSkSiq9vLV0wdwesVuv9atJA67CHNV485Q0RuUGMl2ooLuNPv15CdIeyXJHK8SqnFS872ITN70fWJdlLYqGpxaGRDgSsICxPqMVPEqlbHYqIZfazdDXIoDU3bkA4hT2aGtlmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما:
آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده
‏۱. آمریکا متعهد به عدم تجاوز به ایران شده
‏۲. استمرار کنترل ایران بر تنگه هرمز
‏۳.پذیرش غنی سازی
‏۴.رفع همه تحریم های اولیه
‏۵.رفع همه تحریم های ثانویه
‏۶.خاتمه تمامی قطعنامه های شورای امنیت
‏۷.خاتمه تمامی قطعنامه های شورای حکام
‏۸.پرداخت خسارت به ایران
‏۹.خروج تمام نیروی آمریکایی از منطقه
‏ ۱۰. توقف جنگ در همه جبهه ها از جمله لبنان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZ0Hxx0_a-WvJJSJz7H0yKui3PGAdW_oBT4cVvDwGwK4Lfh6-DGl2rOuhuiZW0gnnLXVtitdRYuki1deDKQ4IsfXuieIdowiSS9dSSk_CSHfimXNg1pj-Ohb0V_01DY_el13HBaS9qEW87FyDhn0B5WBcc0MblpzX4XDDTHgfo_67NP6B-aqpZAauJ12G0URN6XXEUNF3IaTMsh2P8vHl-JiYjUSiRStV3df59PdKk14P-_Gc6Ks86wrATQKZeK65sLKed_Ry5gjh7yvTfWrBxhAXAFtW_STNTAN2kONJwluku5NfDF_DsCknnWm2nD8XpWNhS06Y_0tXKNeBtW9-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏
🚨
🚨
ترامپ :«من اکنون در کاخ سفید هستم؛ جایی که همین لحظات تماس بسیار خوبی با محمد بن سلمان آل سعود، ولیعهد عربستان سعودی؛
محمد بن زاید آل نهیان، رئیس امارات متحده عربی؛
امیر تمیم بن حمد بن خلیفه آل ثانی، امیر قطر؛
نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر؛
فیلدمارشال سید عاصم منیر احمد شاه از پاکستان؛
رجب طیب اردوغان، رئیس‌جمهور ترکیه؛ عبدالفتاح السیسی، رئیس‌جمهور مصر؛ ملک عبدالله دوم، پادشاه اردن؛
و همچنین ملک حمد بن عیسی آل خلیفه، پادشاه بحرین داشتیم.
موضوع این گفت‌وگوها جمهوری اسلامی ایران و تمامی مسائل مرتبط با یک “یادداشت تفاهم” در ارتباط با صلح بود.
یک توافق تا حد زیادی مورد مذاکره قرار گرفته و تنها نهایی‌سازی آن میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلفی که نام برده شد باقی مانده است.
به‌طور جداگانه، من همچنین با نخست‌وزیر اسرائیل،بی‌بی نتانیاهو، تماس داشتم که آن هم به همان اندازه بسیار خوب پیش رفت.
در حال حاضر، جنبه‌ها و جزئیات نهایی این توافق در حال بررسی و گفت‌وگو است و به‌زودی اعلام خواهد شد.
علاوه بر بسیاری از بندهای دیگر توافق، تنگه هرمز نیز باز خواهد شد.»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MehFjieTuEtvYcQyJjRPiDKYPcD7HNmCOEQ4mHp3vt8mI62p-XeOKwC8rSj5rEagPJJ2flNEIWDmGXAbnxQe-Sxkkrxbu3vI0GvZc_t8ZgoHVYFMSUFdzzeVZuQM-lVTaIUbp0GKBMMIkmN7mQVTeFk8X0DbgStwhAiTRw7Jf2CNrqOXinmPlvkTQdINRDXckhOUB2QJY6DiMSXF7WSuXFD68ptH9wsxisBkXTmVsXvvSerRlY-PyHTBq9kap5Cn_K51rrlahn9MylId1tErGhkSD9ri_IkxtYTX1ddy22hftsDDp9LapYyBo2AwXs1iuS-6H1GQuH-w41j2DvPx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
آکسیوس :
ترامپ ساعت هشت شب امشب ،
در یک تماس کنفرانسی
با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=TOH1EsOUsfU13wOFCHTmPuCB9Q41ZXgJcVtaQlzG2Ko4PT5j_-4fdlGUOxjFwMKkcUV7Igt_MFzE3LjBJTmX_V_qUfIa5y4a5jplUaUClPgHhOCJA00KCedEoyfA6iFcUD4N1zPwuPfmaDrAPNRB0xQygzvw38Heo-0xR3RisnwIvLU2zH24AQIA1hCQke35G9h-CmyED18rOjknUdpTdUix_n2_e9TbE8e29t6C5BjRe1sG7L1LBCCQAhGUlEf6-8lKBogVJU1VCHE3w6yGOCV7IiOIHmpvQZbfh8u29R7cwIfz-ONwM6BEBcL-6gaD0GzWPx1B8vdgO2w12yKXhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=TOH1EsOUsfU13wOFCHTmPuCB9Q41ZXgJcVtaQlzG2Ko4PT5j_-4fdlGUOxjFwMKkcUV7Igt_MFzE3LjBJTmX_V_qUfIa5y4a5jplUaUClPgHhOCJA00KCedEoyfA6iFcUD4N1zPwuPfmaDrAPNRB0xQygzvw38Heo-0xR3RisnwIvLU2zH24AQIA1hCQke35G9h-CmyED18rOjknUdpTdUix_n2_e9TbE8e29t6C5BjRe1sG7L1LBCCQAhGUlEf6-8lKBogVJU1VCHE3w6yGOCV7IiOIHmpvQZbfh8u29R7cwIfz-ONwM6BEBcL-6gaD0GzWPx1B8vdgO2w12yKXhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyvXF2ZqkK7-qQCzgTuWqYJ88YqpBfTzeli-DXRntmFKncDCLTrkLaw3kmFFYtsSG1AwIJHFuRou8KEKACOLiRlQ8H0aFEewZ7_kHrTtwud6nLrGuE89Z830n6bAEOYVG1O3TuQ1eTV5NyWvahkGaNUSv2adX0VWvbbMm4pPCKJX_AiwO-1EaecAaz7rcQF5VaC_dq2eiaIUILaFWD6DCmWexJQhV8ai4favTmTGrvrn5P-46CdWT-aJccGDr-Tc1qklbn_DH6TocfK7YkbolXM2EmK1H8FB5wYRRsIJ9e2_zWrolPU3TUmaf3tLSs0JYjQdQnhY-Rdu_AnkjuIAKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمال دریای مدیترانه، اروپا، نماد پیشرفت
آرامش، ثروت، هنر و معماری و….. است.
جنوب مدیترانه، نماد فقر و بی‌ثباتی
و جنگ و سیل مهاجرانی که
از این سرزمین‌ها می‌گریزند و …..
مصر، در جنوب مدیترانه، برای ۹۷۰ سال بخشی از جهان یونانی - رومی بود.
لبنان و فلسطین هزار سال، لیبی ۱۲۰۰ سال،
تونس و الجزایر و مراکش حدود ۹۰۰ سال.
تا اینکه اسلام از راه رسید
و تفاوت میان شمال مدیترانه
و جنوب مدیترانه شکل گرفت.
و دو سرنوشت متفاوت، دو چهره متفاوت گرفت.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKSfN2Zg-AmGTFnG0-RycqqnG_0s13YgZlhjpjshJdx625coHJ19PbhPidED3Ex5W9OmS7t5zPX_haK-4Bn-uEh4mJF7nDWVHp5N6gO3Gpa7YAqjzLMjX9deFkdfeM0Q62nEG8TH1Z1QtRz-YkytKOOe-GtGyqpTWagZ5nOwzH892_NqnQ6PiRD-SsllqDacij-J-AUdpN9_-onT4mrEbBEWdnfyjqGiJjirdoYtbAFD0yROIkhZ0G1IFOdJhl1xkI_4vVwrACOWoGosmfXg_J9a0whna6h1m2v8gdWUjhmvAJQ7m3Qqa29aBMoFkRXrbCUzBDXp9QP-K0kUlAcrfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgHw3jnMplh2A0YLwmT9NNnlzdkR-hWqAcGYdxIAx22Q_U9GE8gLwQNbzl9w6znHD4W1L7C-elCMwIlKmp9-5UF9_gmaFU137KA7VgokiZInB160W7fUaTKExtNP5dcSOmu7d4r74fSe2iLsUOshi8wF89bE-B2v79XmQ_zK2oPvB80ssyqZjzPGgkCj6-pVEnnMjCMmHB8iRGr33xdSAxHliYCtiwZeVb6VTLl3_kwW5C-J4QGjBYlP-vEPf0Lr86St9WFLKltLlx6cvmiqm2lEc-J-Gnb0Gs-JPYGBKtQagRDPLd0ODQ145-0-WceCEcng_j-J7-dyYK5I9bdTxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTggv82Xj7n9BKqChiY-2HTQcEghicT4i_XaJPzPIB6kN87amg5KKIZHkBl_A52nNq8oU_vt5rksdzyza9b7pu6BTdqHMOUJHqirEyNkUU2_YCxInAjHaciMuIZCqq93dNU9odu6K2GJYc_siPLOaE94YbTEQIfvluvkMkcOPUis-LC7ZaT3IH0jl4N2IS9eP9yqt7tkpG5ObnHJ4Ev-Dq-H8-PaypvrpHiUh72Y3VfbyOIu162Lk_zeuDcFMkVc3FgadlQdNhTLzUrIsQCDiB5PUrKfZ9qs1uMmA_6T0qeNi9i03ZhAM9iAL7aGcGFolZpvahBiC5IYNhV_aXvo4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
نیویورک پست در گزارش اختصاصی خبر داده که طرح ترور ایوانکا ترامپ خنثی شده
.
فردی که برای ترور دختر ترامپ تلاش کرده «محمد
باقر
سعد
داوود
الساعدی ۳۲ ساله و شهروند عراق است که گفته شده توسط سپاه پاسداران آموزش دیده.
انگیزه او انتقام از ترور سلیمانی عنوان شده.
نیویورک پست نوشته که الساعدی از اعضای ارشد گروه شبه‌نظامی کتائب
حزب‌الله
عراق (از گروه‌های نیابتی مورد حمایت جمهوری اسلامی در عراق) است و گفته می‌شود
آموزش‌های نظامی و اطلاعاتی خود را مستقیماً زیر نظر سپاه پاسداران در تهران گذرانده است
. او با قاسم سلیمانی و جانشین وی، اسماعیل قاآنی، ارتباطات نزدیکی داشته است</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIhWCOF-SlsoGNwl3204r_2V8lE92lL-BwHkaQ5xd_sRgMDgacKNwtJumr1GVHVBB6hIVCJpoOjfoW6iEBwp42J5vSchqJNLvOIKO7mK1xyfWpT2QSmy5rfoNPBRxVi_5N9Q6CRFuLLFbL0otQ70B1AOzHIIXfp4Y6ZkyWkvjSf-QjPYSfhLPdtBVbbl52Tfjj0l7dqkEeiYjELKoowF3bcwt_tjSjt0FEG0OFAnRPsLpTXHivc7j8IAoFJlYkfbyj_DmTPxIn9dv090pgBLwD-1yVm62PAdv8X4d9eW9UNf3fbHlaGQxmOM_y0SRDsWjbO0M5-897q3EM8EVQ2Shw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C72lM98v43I8CXb26WD8rL5EXhE_6zzds19T-TiA91m8UZl6079kWsv1lX5d90dv-qlZpS-W-vAz85Ps25X0QrdOYW-xchRE62ssOAZVBWL9T66mriLH38npUrYhuQ3CwSBx-FjduQ8VTrvE-arkpcufw4SwxxLZIqioCDMTgsUMhxhA3QHcFIKjEY1bb4qjcBuHViac4-ZFZ922Lyum8NRdgDBEdpkVpPm6bTwV1N7qBI-ULHgbVKTcdLmL8FuxgDn_1ib_48nLsATSGCcRRGw-Mv1qWaKNQ8qpkSJ5cSFnRuSUl5IvTl6K98s5cW0oVtg_RgfMnyjBFfPjqi4ENw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">مصاحبه اختصاصی با قرقاش: ایران در موقعیت ضعیفی است، دور دوم جنگ فاجعه‌بار خواهد بود
🔸
انور قرقاش، مشاور رئیس امارات متحده عربی در امور خارجی، می‌گوید دور دیگر درگیری میان ایران، آمریکا و اسرائیل «فاجعه‌بار» خواهد بود.
🔸
آقای قرقاش که در نشست امنیتی گلوبسک در پراگ حضور دارد، در گفتگویی اختصاصی با گلناز اسفندیاری از رادیو فردا، گفت که کشورش از یک راه‌حل سیاسی حمایت می‌کند، اما در صورت بروز یک دور دیگر از درگیری‌ها از خود دفاع خواهد کرد. او همچنین گفت جنگ کنونی نفوذ آمریکا در خلیج فارس را پررنگ‌تر خواهد کرد.
🔸
رادیو فردا
: آیا امارات از مذاکرات با ایران برای پایان دادن به جنگ حمایت می‌کند یا ترجیح می‌دهد آمریکا و اسرائیل فشار نظامی بیشتری بر ایران وارد کنند و همان‌طور که برخی می‌گویند «کار را تمام کنند»؟
🔸
انور قرقاش
: نه، ما به‌وضوح تلاش زیادی کردیم تا از وقوع جنگ جلوگیری کنیم، زیرا روابط ما با ایران در حدود ۴۰ سال گذشته همواره رابطه‌ای پیچیده بوده است. ما همسایه هستیم؛ تجارت، سرمایه‌گذاری و پیوندهای زیادی با یکدیگر داریم. موضع ما این است که حل این مسئله باید از طریق سیاسی باشد.
راه‌حل‌های نظامی، همان‌طور که امروز دیده‌ایم، پیچیدگی‌های بسیاری به همراه دارند. ما همچنان از یک راه‌حل سیاسی حمایت می‌کنیم، اما این نباید بهانه‌ای برای درگیری‌های آینده باشد. مسئله تنگه هرمز روابط را پیچیده‌تر می‌کند، به‌ویژه در مورد دسترسی آزاد برای تجارت و انرژی جهانی.
🔸
رادیو فردا
: پس در واقع، همه‌چیز به جزئیات بستگی دارد.
🔸
انور قرقاش
: بله، جزئیات بسیار مهم هستند، اما ما همچنان نمی‌خواهیم شاهد تشدید نظامی باشیم، چراکه می‌دانیم تشدید درگیری‌ها در منطقه همیشه به بن‌بست منجر می‌شود و آن بن‌بست مشکلات بیشتری ایجاد می‌کند. همچنین باید در نظر داشته باشیم که منطقه نیازمند ترمیم فراوان است. به‌طور مشخص، امارات هدف ۳۳۰۰ موشک قرار گرفته است.
🔸
رادیو فردا
: که حتی بیشتر از حملات ایران به اسرائیل بود.
🔸
انور قرقاش
: بله بیشتر از اسرائیل و ما همچنان در حال پیدا کردن پهپادهای زیادی هستیم، بنابراین شمار نهایی از ۳۰۰۰ فراتر خواهد رفت. کار زیادی برای ترمیم روابط باقی مانده و پل‌هایی که سوزانده شده‌اند باید دوباره بازسازی شوند.
🔸
کامل این گفت‌وگو را در وب‌سایت
رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDTWjFUj5HX3jIGEXJVjxOtHN8pz4S5ov4XD9RqsCqwLtNkhKkajgBZu7u_8ldltdYGndvEFY1Vwe69dpdMV6SND91F7MTiLqEBR6B4TTct7UWgs3LzeU_8cf9UzMN7LoiHxvrMwtzASAAtcwXR8h9MBFHrI10zx8CcCgbFdAQfXLMzwJoFItiqLGWrIoLSIHbhZ4V1teF_mBSU5Lf3wdQ9NyZK5IOa1iC5WcTYAoJK2nFHTVvXumSafqecQp4d78iqumQXe7-kHz1bOdO74KF4xA2t6OvagY-KFuQDgI9poh4Ce6OZn0r6kqsseujR7_pTvsWTCCoMTarmkbf2bfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJ2ZaEF9fJwfhdV_w06JufEKlfAFJOQoA8Wal1fVzKVligvqTBCq28EJ3Hn6LUJFvLLS21E-XRBb2ObJkMwofN7o1rbNJExKC9KQ09B6TWxYeKDRgFnfOccj3fWZkP5XSY2kiglxgjHtEbMu_VYgpxb_Np7DF-YOqbP9EhAPROWJ8WLcCc3bgSqiTq7CqW4vIvAVvFfXVwrxoU8O7ywDBVHsk1U78m2hzZR_TLTKG_9PUx0yvChwvrV3tuZL6eZqHuVfqwxs-HNRP_A_a2YzddOhC-dRcBTsf8R7Wdi7TtoSD3l9gVpO_ODt6XXPlrPVVmur3hjGuH8pSbq2rDpO3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hY1YNpfd3uh-tbs_jwW6GVolsFMIVegPhNFMDPQQgi3jeroND5_2c18Lykj39Cxq8VdZeNiyC96RDVeZfrNlbRC2f13pbLpmQjrHaV8bEN08h4mIj0gE2a_T6FyD9Vpv1XQagFYlWJSgRR_x-W6Pmkj7eNwUPFvCdn81vvZKLGMGdOVuPBt4dlWX_Z-7WR3OSX5z_-yW1DV5375sF_25XTMlGWT9XagKBsXkkujwhjFEE5NbuALd5xO4ec8E4JIGr_1JRZiLKoCurP70J5AyIZvWyjT8W_zUUrHSqupmdKA4Mfl9DeSSSZyZqcTDRCGi6IPsAHxHkTTy_KCjjWpCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bc7ekARqPNHuL38RhBCnGi9kWcvf4SIV5x_QMHO6mtbnBEl5uY2yc7obIPTAQPs7-nKkBbvsly5WtS9SqvMavmZSbYFMw_tudMh6PUxup0muD2NQhhu1yJoNN1DbPVAz66vSRG1W26fdEkxqDvTG00ZK3FaJ6K41UKjsQK5rCIVMnTBe8t_FcHF7aBXh2UNGoL-yaKFUibod2VT7kYUn0B2rVF_WRpjn-txvT52JVjswooe6xxyUq3M6iGyLNtwR-_HDfqj4tjlIWdEu3mWt2MEM3k_Oi9mGqIx1KJLUJExLtQ6inp9Wc6aa9wlv6AHYFEGqSMdBYSyFmU_f2942fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S98lfdJ9PBkZTboqnijEkSqmdFgcw2u4RYjoQFf80I1pHY0ggxiY-T7mU6oPcpu_s88A5xswWn2MKObmIc9LoxmbylkW4DhxEFXaeheFdzRFXlyCFJU1kINCA7IJrLfAkHFCBgPGK05QcQMRWEXPzPVVFtWLN2s7JSwTgTeAA7uH3amEzCQk8qqDBexhkWxkMqVOWeKsAW7Wm5Sy6Tqq5sJ2DbtWMMXhojIbkz-F79RMBxJkbYGAIvoX0W_hL7YhE_AI4B2sg5BXpy0bXa-MJbaofh1cKCLLAYkaVW6bGZ4bPDa9qF8ZAtG08go4LX_wJWGjFLDTvN2_UNWm5nwIYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=BVvtUvodkcNFvtC8G-Un5TUAq1r6WVnBrtFPEis92fwGrU0LnE1Kgh4Z8MIjK_wVn2jabYfDvj2gSoWN9w1z_t7-Ub5y4H4XKHuRxA5hwyDDmJHyRB1hI8B4KY5aWvmzmR-kpObHNp4V94whYvA21OStF8BArPiWL0MrEJ7wg-qMSkaS5sxuOfdU4mRICKrRhLV2475vij9dzZmS_nXxM6QVs7iiDou7B65uqJJRkfaKBl7QCb6tSvabAMrunGQphUENEGMOzFrdf4X_TPSCVp4sCIGmzi9hRaDNsFjzrX0fiELLnUhRfNmh_qpMjXzLdCwh_XaAdVIXd09CEc_BrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=BVvtUvodkcNFvtC8G-Un5TUAq1r6WVnBrtFPEis92fwGrU0LnE1Kgh4Z8MIjK_wVn2jabYfDvj2gSoWN9w1z_t7-Ub5y4H4XKHuRxA5hwyDDmJHyRB1hI8B4KY5aWvmzmR-kpObHNp4V94whYvA21OStF8BArPiWL0MrEJ7wg-qMSkaS5sxuOfdU4mRICKrRhLV2475vij9dzZmS_nXxM6QVs7iiDou7B65uqJJRkfaKBl7QCb6tSvabAMrunGQphUENEGMOzFrdf4X_TPSCVp4sCIGmzi9hRaDNsFjzrX0fiELLnUhRfNmh_qpMjXzLdCwh_XaAdVIXd09CEc_BrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=kPfjwFpKDhQZfenzE-XLJKirPQwY-jn8W2i24fFV95x6r6WGuW_7gqATPGlYjmDNGevVEXoauwUXNRQ4frhKWrwpJY6H29geSDnA_J5vZh4YpqaIfq0Dtk-BPswtwZETPaKTVn4kI5pPYFiK3e6ZWtUFg3wNcoIMxZdV93b10yxQzSPler3ZBHsjIfz97xxHJn-Wb1Op-39bVZ2Oc9Pkf67gbI0cYosctoBuit1D_jGmZmXANTAn8T89muw9f4tKGKcYsGyjWmmGoQswDaSBAXvb2e_avYoYo2a00toqQPakhR-7HOtaBQ7rcTzt5ZEALf4i1EzvZUFmvpcZB35eXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=kPfjwFpKDhQZfenzE-XLJKirPQwY-jn8W2i24fFV95x6r6WGuW_7gqATPGlYjmDNGevVEXoauwUXNRQ4frhKWrwpJY6H29geSDnA_J5vZh4YpqaIfq0Dtk-BPswtwZETPaKTVn4kI5pPYFiK3e6ZWtUFg3wNcoIMxZdV93b10yxQzSPler3ZBHsjIfz97xxHJn-Wb1Op-39bVZ2Oc9Pkf67gbI0cYosctoBuit1D_jGmZmXANTAn8T89muw9f4tKGKcYsGyjWmmGoQswDaSBAXvb2e_avYoYo2a00toqQPakhR-7HOtaBQ7rcTzt5ZEALf4i1EzvZUFmvpcZB35eXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUgIaqu9noIhENl2XhSUjYh47ao-kJYtblmbJe4JAc4_8XAmqtZW8tdxRtu_yPxUpNcS3iIVypHt2QYGwmYgSg6qbXNPS7EvBDWvoOk4ripD4_B3y2vtrmQKzp3TDQ7ApSbB3yMvrOgoa_UaGvpE2QoDkso2sN6ZeSn-2yc9P7jBR8S5P0awYssbmNImpLQsQNb3vWag_M1WKrkY3sh8aKJ0VjuB-iJ0Ldw00ceBV5Ml6SwVZUHOyy2eKgg8VdsZCPk9ppy7rphH1wfzZOTP-eZZSoW5x0zoE0bFqBmvYnW0ti0qP94HXBSJRjbqkq1AdCv_3n9o-DG59kuZkJp1dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oo_Beqz8yU8CNWT0vyav5BgiitAyBs-vuOEfK4gdfA_vblP4einHENFe5DNYEQt0pGekRh-o0LOfeci6bDtdgJAP13yUEfIlxbJGis_PSz_YQcBHepvTXh5JdPkkJqdhbJptlezPndf6NLkEfePypqi6J9aaNRoRcj2Dc6eWpk9pUiuEtunEaI6FtAvgjw_G7GhoQ9kTv7H8zTZgOmuxdwI2cLEFXSzaplUuwRdmej09nhXBT2A8b6_9OksYKcVTEQm7YXfOvjPXgRVFyKHAtvyu6g0XRTIY0V25OSeqgJtaVIddQ0_kdz4yTzyGBHtFLaUQ8qtAJ1k9WGG3Ip0W5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vnnk7xtT4xI4iXK7qeOAjhP8jnWMYRYmBYxz0RYhKklUFLnq_A-diUMkiBSIZ9cz_KqHK3UATkCIF4pSiu6A1pm0jav5oWmuqHvq10hCUam7dCCtiaIc5cgwEi7BKpsmazC8cP-z4Q2MnihGIA_brHZyEEYhxTX-RHpgvnG3dQdqsLgmBgOlwgcEHpfGdtVw0a97Z_JVbCvrTW4EEwUxFgi1QbKiCSiijxbxDvQ7MqBxOYGKlJRVuL6-myUZp1cmPL0-78xozIgjKYKZ33QuPEmAa2fkg6tI5D3JrnXPxw0c0pXEEZKwO3AHMg2Q25hC9ykzXgRN3HgEfoQUx8vz8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=lv9x8Q1Hn9ONTazKNqrsO5-Mwn4zb-Coxilemr8pVwsb4g4zx-5mGkQGPEjkyWe0VeFEJCE_iiWgry1henOmH2ET73D0C77vfeLhfIqb8U9QMNWEZDcc9pSS5zbK6uosM7T5x3-boSH3bMAAMAvMtA-VeaKJDpeV7tumgjWvSoT7etqe-h2akdZoBrlt5sVL_h8ftAlknwIy4eNxBtjf5fwzIHP6oQjq2aGxNUWi1U9QzZ2jeyrw-tyaWFBWQXXnIH_TSCPQL23Smc4Rz_5W6d5yQV_BmLH4aCSygdbzhHHSGOPelhcnhSo7xU0T3m4SFcaTnxrIJCiSePIbEieLPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=lv9x8Q1Hn9ONTazKNqrsO5-Mwn4zb-Coxilemr8pVwsb4g4zx-5mGkQGPEjkyWe0VeFEJCE_iiWgry1henOmH2ET73D0C77vfeLhfIqb8U9QMNWEZDcc9pSS5zbK6uosM7T5x3-boSH3bMAAMAvMtA-VeaKJDpeV7tumgjWvSoT7etqe-h2akdZoBrlt5sVL_h8ftAlknwIy4eNxBtjf5fwzIHP6oQjq2aGxNUWi1U9QzZ2jeyrw-tyaWFBWQXXnIH_TSCPQL23Smc4Rz_5W6d5yQV_BmLH4aCSygdbzhHHSGOPelhcnhSo7xU0T3m4SFcaTnxrIJCiSePIbEieLPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انترهای جمهوری اسلامی
یادتونه برای حمله گروه تروریستی حماس،
شیرینی میدادن؟ یک‌ شب شیرینی دادن و ۲ سال
به سازمان ملل و به دنیا فحش میدادن که چرا مداخله نمی‌کنید و متوقف نمیکنید؟
(شما چرا نرفتید متوقف کنید؟ و البته میگن
پیروز شدن و نمیگن اگه پیروز شدن
چرا خواستار توقف مسیر پیروزی‌ها بودن)
حالا هر شب میگن «بزن و ‌دوباره بزن»!
فردا که «زدن‌ها» شروع شد، بخش «خوردن» که رسید، مقصر میشه دنیا و این «لاشخورها» میشن «کبوتران صلح»</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5097" target="_blank">📅 10:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuBWHHW5JiwLOLMdqqXMh-aPhf3y2-PjhfDMeUHABYQ8LY2CPjjNp_7BFdFWhK7I7EoF4Er__iWI9kYy-awPLVYI08a1RznDomTdfjlZ6qiGDk_9EHztKOGfpCkY4hnNmnQxrIuzx7qZACSrGXrwsdHbk1KFfWPq3V6-1I-l_IJEymDTikAxCOG6uix2cZyB451wVwiFTi4qNfS1yVWlMW5Jl3GckGm7KA_du-uzPZvhEZbHW-6hrNqDicoF1AVJ1nkbmFsXdQEpLVIcikiexpSnKwQkybGwAGMTy9PmgyV5NbOJ4maoYruGFnBTgz8Gbyq0nVWloUzn-CW0U8USOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvvuxvUkweUG1tJGtnaqGZWFTLnigY-FyBBuzukbu4NCcd_jtjCrau4yncbiOU-Ecd86ighNLMWbiwHJoietrutkB6ht09HW0ExcdGk3mgtJtq-WWIOMrjnLTRpCvSP7Sjs-50v7rMw9cQ9NCZNhjS88pu8wBFCcZpeq_CNpofbe8rTs9hTGhCHllPZqYcwEAKG51eMCQ38y6h2Hyxc3K6dPJB2sESahUfxaAJ11aflFAsOIM-DOJ95iBmbigzifiPorR28uGLSoaNzzkmw6QdELTOB81c2QfpC990IeTgtYPG3v1zCwcFoB4D8QdAeW63dujAmvMYaoTmUU1JNr9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcrMRmGlmeJdIIpb6MDEzDs8xRqiXbRVutHrSFQJAhVc5n_qahb2FJztGoj_k9mLsxA7qyajE1Rw8ofgjJPnpZk8f1SfCQbz1cm03fg0MGaQsxtdKrMB2gS0luP4Jj03sjJQLyJv3jNCmmw_5a3iF59kEa1lqIXqExqgMucTLEoCz7S_XMLTMA02ur_qWx7wLgcfj0x3InBsSq2TARx2s0ytCjef3MfeQnEAUQEVueUebUYs22I7JMk43h62F9I_pd44iwkMyowSJCLv8FosQvqhdVR1hsv-IKdSQSZKvfb6td4ryRWc4Hg2LVUp245ffO20vhlGoiiiUqFuCWqUog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7HiDZTqnfpWqj9fvA85rgt0NrwMmIGmoUoyge332Fi_lHgYUZUYQwSmv8XGLA-pbNuLRWgv7NM1sumzpYmCr68N8LBF8okg4irx6dL_DKmRGj0kz0PdHm3T5lcYffzjBymV5byNKT5mVJBhBIeqN8lQdzsXMNhz6EM8ts32OStCp7lVzhJSiSJmSaoQ-Vqi02_70HLHuYZVCUBzRXjM8VOa_1et635IYkwWo4R-xBMcqo4jOnaKYvWXfY_g30lsYRL3gpgDtWIUYevabjpIvEG7NdpIEpnpZscKo7s6sIcOMLG87wKmqmdgFO0neFUDR1RdTlzn4yKc2WJD82GujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoeeRMzsYgH5J8RoJwYZkH-813IM6j6LzIO8-fc2rVrPQJvxE_EUjUy3-EB2CD9zaxUcaxL-z9HoaOl0XKwz7ADBGIROgMcJBb6QqEuOMmV8Pu7-j0RnMKa22Ow6rBvu0EUKGGVGS0Ly0PlXawm6Kj8GyRbnmLWAPXVAdaTfEqoOX59C-qCSN_ZhaaZcOFNCcJDb8GQEyeOgDm9zjkpZAW-bLUq0RFQvsYgk115LgcWxwk4Wv6vUfJ0tLBNnze1EQlKCb9vFE4f-9MEhTQPIbt_ySIrggi7QbdqecfZh_NegW-13inlYqx0y0buDWndyuYJSVCQpoErtYssfvhx5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ozNURpfgv2OaQNRqHGpmSs89F0VUsPv7sw_Wq7ezy24--QTFlmvOr57bpbdKvJWdZLo3dvh1QW_3cI8TDt_DNBpDcLlyTWD6k3ocrYqFQcRUQ5RBCX_535HqsLYrIKyDskJ7MJQ0z-FI-93RFJcpdXFCKStO5KbZ5uPxiKAOz35nvNZm8ORyNzFzFLHd71impFqG5Igg5gKtulTfS3gcXBazBtlB7fz9ak8XXFKzcBCPFrHCKB0ckRtLFclABUJhm5dj71GYtASzKYKFSsoUlBmOU9Q8NkM75L9zh8pKTEYzA13JFqQWkNdpYhzmpmDh-cw7FdS6OYUdFIOtS_D2eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kkOcMKHbhN_VDV0S8h3zgUBtOC5QohaCdTvtGTDrHLn4Zg_AwredM4pJZIv6AwIXgo6NbbC3D2MQ2OirdumgyftfglQX5gp2rflOIsnGd3W0fEbdh_1w3p-Pl3kkvvCEJNr4DjzWZ0ncEwo5ONdlKTRkNE8XwMC8Z6Ss6_wP6JKwTC8tl53iQqOO48pPYn95bVkYQPBvON5p8m55fH2k-7tR7EP9p53XU429_ioyT70XEJ6FVKlRndZ3RXoui42I1I-3B_-71MGex1HnpGdLihcI-9TgF2bPw1rfQGTE_vl4nfoV-kTiRt4MobOnOs26KhBG9kzMbRthnyPt4g8sJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IT1gsAKap-6kGVypBihgJsVMzYSZ-Z_LfJ47ZaxE_ZPpoOe2ogYQxx-2gA0EpF3BazSpFxEqg6bVCvGeucLNphg_AWRHKTsHfn12KOAZeW82Gv3FxVSyxF0mm8lm_GVZuho__tzi0tHCsql2TvEv4xI-sjpDMC_WeYSVo3F-5V9PWr4NCc-92vVWWIoPf73O6Gt_uQgeaHWxDudPF9dXXEzazl0ImhBXyCDdAQ5aOf2hgSnZJgbQI-P_VnG5Pen-TK2WNQKYXueY5nJsx7tnNPbTQMavxOfQjqe3dH2CMbWNa6BhzS1fv6QKDT_ovLidFCXvW-ssH1L8UQ7-RkP5ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQRHoH4JsTYH_uSs9Kd-nyN-pMGy5dgy89j6wyRJ1nVwBP8mwNmpvvdypsWgrPmh7df6tXRl_iKNBMnfOTqi70RVrDFERuxw_0TAE30gyHa_gprIR5ao920nxhukJTz5Law6wSKPde4MF-Vi2jSBGdkeLUIL_SL5CqCwDuuWdlo3yaoUt1zajnjA8hfwkoQH4rbWUyi7VAmHryJbUm_sXe78piS3amT4eus_6EL1dAaMbrA97_wFWGz7iBSi-gygx6-lT4K7gxoGeRVz7w0CL3T6H5ktI_YnGDjGSIT6ifROqHRPk40DypB7oIIEiijgLSDRFBFgZwvURibEVce0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZDnJR-zB7UNkTK2K1qpbF0eSsZ7Y10rA5wQBjyw9BJbu3Bbw5tPZ6rAFRcJI1TM7i_Na5Vupx0LV8Z4Rabua_WBQZKky3yhPP7Y4Y8wSyvSOZMXb-O73BBrIfYhulgqwjrf51Atrx2TA_I7rLBVKw-jr7VjGtas8WpoadgF5IqA4MuG_AvMRr0SQh7sbxjShgZ4zIPV-tf7Kn2Yh4f7HDrnQ5QLO1b7Q1l-rEYmnLR181b8zh4O2X_e_DztLl0F7FOwxOSvhb16B-d-nMSzNx6iu_XZobWzvEBpANF9tCZfRXad4VkzbyXSwC7RGCFl-IT71B1immehkjaLjBYq7Lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kztuV1yCddJgZa-R2Sh3V9sOXcOv41pzACsGXWCa4arEkoZtXKkryCV8mlxMkjxf2tkbv17KKKE5nUDvaoD3v4m4fcc7wBN9UoBnorkR-R0gdYRopF-8kKOmUV7efG8vLdh10rlqpZcZEoXOhbF9K9LhQoh5-aY-CDQ8kZt4hIJj0dCxpjkRy_DId0pMX4PQr8u91in85TmQza0cruxc7xNicjDXJUPzq3tjKqT9nSWRuDHmZJlGe-CgT1cus0EIvkcDAVYkxrCrFPZJjUXUU4pGf9uchuYwxs9tyQAFIwW97Zc7Upepy-XgzV4ZoWE5Rq44yOQgIFMPXAUh-6Kf0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=KI8-fMcoY4DrgXADT4Bqh_dAB1Ox5zyyGmBx9SYSqJlbl_xwsLuWOxulIp2ZaQYl972dAvZ4txrWSbS0GPG2MbG_9JmI9eoZDmdpD-GofxazwRAWF7tOwLeoUmPcTvnt9UNWo6YjE4KcGIaSHSd27gBOoVRx6oMd-syK1DVa69r5sMksAhmIbHX-yavFXlRhkcaZReEzIHQ1Pf0lSggAJPNAqKXM7ZkjTNneOusueS_6rFZR4oHotgKNc3b6TjdLyrdOyaSOowfyj57l5dH-w5Xsxo2I64oKKOVrGo_q0HHhVFcqmAwb9kQURmHn19rvssNwVmaMkTuQ1RXagtPpAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=KI8-fMcoY4DrgXADT4Bqh_dAB1Ox5zyyGmBx9SYSqJlbl_xwsLuWOxulIp2ZaQYl972dAvZ4txrWSbS0GPG2MbG_9JmI9eoZDmdpD-GofxazwRAWF7tOwLeoUmPcTvnt9UNWo6YjE4KcGIaSHSd27gBOoVRx6oMd-syK1DVa69r5sMksAhmIbHX-yavFXlRhkcaZReEzIHQ1Pf0lSggAJPNAqKXM7ZkjTNneOusueS_6rFZR4oHotgKNc3b6TjdLyrdOyaSOowfyj57l5dH-w5Xsxo2I64oKKOVrGo_q0HHhVFcqmAwb9kQURmHn19rvssNwVmaMkTuQ1RXagtPpAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاصل ۱۴۰۰ سال علوم اسلامی!
علی خامنه‌ای هم به صراحت در یک سخنرانی «اجنه» را متهم کرد که با سرویس‌های اطلاعاتی غربی علیه جمهوری اسلامی همکاری می‌کنند.
در زمان محاصره اصفهان
توسط ارتش محمود افغان،
روحانیون بلند پایه شیعه، به شاه صفوی وعده دادند که به زودی ارتشی از اجنه
به یاری ارتش امام زمان (ارتش صفویه)
خواهد آمد و شورش افغان‌ها را دفع خواهند کرد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5082">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=B_UI9pjSdMKqLlmAV3dNIXv5SXpr4iZ77fsBToZvMQDIHZiBsTr_lFwk5cqPc8IWT_cnwGwe4wRaUY9KNwQXYAy5JQPg_wRQ0yuL7BP0cz0HC95dxb9SXi2WDPRsDRgJbxmoan-OfjL6otETb40SjpgLBz1AygPqnhrDeCpmEz4j6mO1Y_uI4JxeyfWLmSlXZSs90AZqhD4WOv0hsTmbaM4vniHpNrKluzFYfdQGfgntoWqAQmI5yyKm9-KoL452KzW1739wiIWq100YkWPtmZ0MqTxCeYaqdguITYMdQlM2CDvhMgDM6Dy2CkQW9Im9iB3ywMyoYOwq6qiKbvmZ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=B_UI9pjSdMKqLlmAV3dNIXv5SXpr4iZ77fsBToZvMQDIHZiBsTr_lFwk5cqPc8IWT_cnwGwe4wRaUY9KNwQXYAy5JQPg_wRQ0yuL7BP0cz0HC95dxb9SXi2WDPRsDRgJbxmoan-OfjL6otETb40SjpgLBz1AygPqnhrDeCpmEz4j6mO1Y_uI4JxeyfWLmSlXZSs90AZqhD4WOv0hsTmbaM4vniHpNrKluzFYfdQGfgntoWqAQmI5yyKm9-KoL452KzW1739wiIWq100YkWPtmZ0MqTxCeYaqdguITYMdQlM2CDvhMgDM6Dy2CkQW9Im9iB3ywMyoYOwq6qiKbvmZ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادآوری :
در پی انتشار رسمی خبر کشته شدن خامنه‌ای، در شهرهای ایران جشن گرفته شد
و ویدئوهای بسیار زیادی از این جشن
و تجمع‌ها منتشر شد.
و به قول این مداح
«صداش عالم رو پر کرد»!
حکومت از همون موقع اینترنت رو بست.
تا الان جمهوری اسلامی بیش از ۴ میلیارد دلار به خاطر قطع اینترنت زیان کرده!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5082" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5081">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=OUS0tqcXGxPqN3KWpQwwZjKyTKtTzZ6lD908p5KL17WHdkYQ0oP9nSJ23A4v3IV3ZVI5-wpOfL6n38qXxiCTI_wr0rl5ktJ0MjWYEYMVqITAhPcvXIzSArdJ0f3913_ZAhUe-UU_0JXj_-lnaAS2HhT40NrW5uIWvNyj1tGPBomfhps1Unx-4Qjt0ACfAQRZdCda52khlzzRGwefWY5MahGe2364HkZYz_e459il8wG13ueS_6znynOoo20LmtMVDbtcYsa0pd5P3eyw0tR4b22M7d_6oCh5zaXnXBdKymi5sMKAHXIpYTY5utUDWsmGFWbo5LUnf8zikxCqf9TyPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=OUS0tqcXGxPqN3KWpQwwZjKyTKtTzZ6lD908p5KL17WHdkYQ0oP9nSJ23A4v3IV3ZVI5-wpOfL6n38qXxiCTI_wr0rl5ktJ0MjWYEYMVqITAhPcvXIzSArdJ0f3913_ZAhUe-UU_0JXj_-lnaAS2HhT40NrW5uIWvNyj1tGPBomfhps1Unx-4Qjt0ACfAQRZdCda52khlzzRGwefWY5MahGe2364HkZYz_e459il8wG13ueS_6znynOoo20LmtMVDbtcYsa0pd5P3eyw0tR4b22M7d_6oCh5zaXnXBdKymi5sMKAHXIpYTY5utUDWsmGFWbo5LUnf8zikxCqf9TyPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuw3-XUqJaxg8aP9jWEqbJ75wfBoaWZ9kvGmaPKDxPRQdJPhxn4JLwK_noNeayRX0i3jLqAo3cLj5kw0zaQsyVISicCFUpvkbgnHhv0w6d8q5Biua5Mh52bS67FsuNhjITn361UXZzl-v3xyKfU3jBOQxHT2Xh_FaifqQR_PIRj761KpS4KkosCkKSxApdUz3bsjwQpC3PlxMu0nvI4xwdzBIKIhxg98WbBkt-1hV9BRK4DeF7Ztl5yctXKtne4f5Ewazh3SGVxY7VM74ndX4LQPchkHwJpZxFarlxJnXBaaDqhSSstsRauVMqbVpT2cXQ0VnY7DoXatngPoqP1maQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">قاآنی، رئیس سپاه قدس: «دستاوردهای ناوگان صمود ادامه دارد؛ این ناوگان چهره واقعی تمدن غرب و رژیم صهیونیستی را آشکار کرد و فلسطین را دوباره به کانون توجه جهان بازگرداند. »
🔺
یادآوری اینکه جمهوری اسلامی چگونه از موضوع فلسطین ارتزاق میکنه و درست به خاطر همین ارتزاق از موضوع فلسطینه، که مانع هر گونه صلح و سازشی میشه.
جمهوری اسلامی با راه‌اندازی گروه‌های تروریستی و جنگجویی چون حماس و جنبش جهاد اسلامی و… هر چند سال یکبار جنگی راه می‌اندازه، که منجر به تمرکز جهان به موضوع فلسطین بشه و اینگونه برای مبارزه خود با آمریکا و اسرائیل اصطلاحا مشروعیت بخره.
وقتی نگاه جهان به این نقطه متمرکز میشه، پیشنهاد صلح و گفتگو مطرح میشه، که خب دست نشاندگان ج‌ا صلح و سازش را «خیانت» معرفی می‌کنند و تنها راه را آزادی همه فلسطین معرفی می‌کنند.
و اینگونه جمهوری اسلامی از عوامل اصلی تشدید این بحران و عدم پایان این درگیری است، چون از آن ارتزاق می‌کند!
اگر جنگ و دشمنی نباشید، «مقاومتی» هم نخواهد بود! محور مقاومتی هم نخواهد بود! جمهوری اسلامی دیگر حرف و روایتی برای ارائه به دنیا نخواهد داشت!  تبدیل به یک رژیم عادی میشه! و این عادی شدن چیزی نیست که نظام ایدئولوژیک جمهوری اسلامی بخواد.
اینگونه فلسطین درگیر و قربانی جنگ‌های بی‌پایان جمهوری اسلامی شده.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=mHE6aVrwa_FFMKZUXp0kb9Cn3ZYiHyqClb8mTBLAwKQhBoC9kbmXlwnJ2718UhEY3VuE4k4LZa1C5pTKHrakGL1Bx4ASMffm_Acc6FTfmwoPVqqzMHidrH5Ib6CUiXid50r6L7JTVvId1r8T-fQvceFyLrVgbB8M63S0FQTqQWnyJVF2_u03X2EDlsJGfLDUF34gEI3itMMjYSH0zKp-dx2O5Fwy2eb8LErGMYS7HxGlD6ddyCuWZt0Mn42oyJp2-oeKN3vmesuhTFf2jhAG3M94UmhPJFrUhM1ryTL10LK0HsJbtdC87klNho6ZU0-XUd3zkda1xPNqIB9jvD6BmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=mHE6aVrwa_FFMKZUXp0kb9Cn3ZYiHyqClb8mTBLAwKQhBoC9kbmXlwnJ2718UhEY3VuE4k4LZa1C5pTKHrakGL1Bx4ASMffm_Acc6FTfmwoPVqqzMHidrH5Ib6CUiXid50r6L7JTVvId1r8T-fQvceFyLrVgbB8M63S0FQTqQWnyJVF2_u03X2EDlsJGfLDUF34gEI3itMMjYSH0zKp-dx2O5Fwy2eb8LErGMYS7HxGlD6ddyCuWZt0Mn42oyJp2-oeKN3vmesuhTFf2jhAG3M94UmhPJFrUhM1ryTL10LK0HsJbtdC87klNho6ZU0-XUd3zkda1xPNqIB9jvD6BmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=kq2A52bXngicYPgWPGRVh_Hb7riiPRJvRf35vMINxLlz0ZcHOh4Ig3P01VkdQnoMhaL7NkGzw71wDPtFK2ewjcvk0XTbUrKo2rm5LIdXbmvbL-qNZ2ueK4vsIquxP30GvINMdPb54-Gp6htN3kq4d_IOB99VM-vuNHfNPW34uxG32lUxzlhgoWFjh6XLKw78xorRv4aZP5UfVDvP1GTddV292nxhCol4Cxh0wu-aZwt8NPSN_UNfCOz3MKwEFt_85HtO8h_6hQ3slM0QgS8dZ4birhoPnbKm1HlS9od0abvwCUC-SPzu_6DG2xQv84_es3dEEzRpNU1qsMAXu4afdw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=kq2A52bXngicYPgWPGRVh_Hb7riiPRJvRf35vMINxLlz0ZcHOh4Ig3P01VkdQnoMhaL7NkGzw71wDPtFK2ewjcvk0XTbUrKo2rm5LIdXbmvbL-qNZ2ueK4vsIquxP30GvINMdPb54-Gp6htN3kq4d_IOB99VM-vuNHfNPW34uxG32lUxzlhgoWFjh6XLKw78xorRv4aZP5UfVDvP1GTddV292nxhCol4Cxh0wu-aZwt8NPSN_UNfCOz3MKwEFt_85HtO8h_6hQ3slM0QgS8dZ4birhoPnbKm1HlS9od0abvwCUC-SPzu_6DG2xQv84_es3dEEzRpNU1qsMAXu4afdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mygLa-MUie4i-syBDmGVumUlVSPKhZ4JZYgot-rm6RTJKSPOapqHWUbpdGxGvqEAbe8JwI3l6LbxEIyymV-YilL4boHaqzSC07G18F8ni_ncl2ddQD-N6UnU4zelnNxOV2CIpb1f5Tn5DXW6Q7zQu-5QRviPQDZ4VnG4bYcgODDSWI6GQTQ9hxJVh2K3i8Z0dA0HdaTHkQAaKomKl-UedR0BaVs40j488VLM5203ORH4UI2IXnQ9NfXdBpyN0yNCaBYOWmh5zgxlx0tsLAX0rDfZjHn9qnCdQhqtQcT3PyuNytC3sV-CFZMjaBUww6cw3u58jmf9z3BBYh980UIOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قراره جنگ بشه و هزینه‌اش رو هم ملت مستضعف و فقرای آمریکا پرداخت کنن!
قالیباف توی پیام‌‌هاش همش به فکر
یا مردم مظلوم غزه است! یا مردم مظلوم آمریکا!
مردم ایران هم که مشخصه
تنها نیازشون توسعه موشکی است
و تداوم غنی‌سازی!
الیاس هم توی استرالیا توی کار ملک و املاکه
زنش در شمال تهران
خانواده اش در طرقبه!
گاهی هم به دنبال سیسمونی و خرید و فروش آپارتمان در استانبول!
زندگی زیباست!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siTLTZsmpIGBsMdKQ4PfwH7tZ6wi7nRCnvQJMte0Z8ZoseqvFjMZ3xKKiYctaRVujL7VOlLH5XO-13y358e7u_mnqvHIZDzjTPpdsorsOZIQA-jWaMeBiFKT_dio_Kwzlpuv_8mOGNT57NqHDwdA-TcQDMDwWjhiVnf154e2GrVUErQ5eSqtHr0MDBBlaeCNuTxoz3DANMl2wa7pJnGXxc0YiIGkqoHZJTYtDtK_QNhYlT5ICBSbSfK1XdKcWHY11FGC2JKBeIRcp4tyAaqPjd_l1UH4mxJmRQHyYqYk1BJD_Em9rYdBUQp1NvgGwr3l4Qu8tBc3Kk8YMxF3qPnI7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3GGYkrzW6g7W2VIznzmqTaEuFrcc9YuWPP7YUoFUM8pMbQi6P5RIoH9EXGXPDt-m8ctFOuB9T2dTf3yfsy-QoSiX7SvQc-NMqrxTJJteKExvT9s2AC5P3wGcOjkZYZTPuHAzH8mga1a4pvjd4lM4QqArzS22tz9N_18ArC1ziQQowG7G2NF48I2SLejuOyaBTPfsDlH-rjFRgK62YHG-M26MQWYBaBVTxkj311Ms8Dad6G8qVC9oO-sRHho4QT6tOuMOytdO1Y53kBZN2T4tR_SLu7OLzAFY2PCoou6K8g0-Kl63MhJ0Ki3mki6_BNsKv0Qe7mQQ_BklpkH1R8x1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماها تحمل کنید چون ما میخوایم
۴۰۰ کیلوگرم اورانیوم غنی سازی شده داشته باشیم و «استقلال» داشته باشیم ،
استقلال یعنی چی؟ یعنی هر جا خواستیم ده‌ها هزار نفر رو بکشیم و اینترنت قطع کنیم و…. انتخابات مهندسی شده زیر نظر مهندس جنتی با ۹۹ سال تجربه برگزار کنیم و
و بقیه کشورها هم در این امور دخالت نکنن!
بگیم مسائل داخلی خودمونه!
خودمون حلش میکنیم!
این یعنی عزت و استقلال!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_zktHg3WxWO9vbrFNq0qOAyFyu47AR02qAdFzOSetQoZK_aZNQL2CqjadPWfba4NeEtV8RqLQ5OFzmrdkQQXO9qQdCbBXDZJ-2zFh96vUI5JGe5OkTsk4kw_3EtJPEurATnAz6DRCjpaMGELWY026hvt25sPwBtDtw8eWM1LlMl1iQlAaJSgx86Lvmjj_ppUVfTZfZPAJXxwtV1xm6tSpF6iGjp5P9A9cvlDlWAh6AzLwP6Tg-RsvR1nVWArSKQ5y_uQEgWSD1ab0CyBwkaiNeqHzsS4OGvIMCJOdYhsh1M-kmE9P41o2wTqYRq4xkNfE9YWdf3CTfKqtG1gVvrnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vjsGWncRO-pEuh3awc8Hvp8eoQnAmnhZEs8iBu8pMT-sKqcMwFfUd0whlBavrmOatGnWEaIhVTVNyEnMW2hSAN8BF-IG1lEXhn6v6T0vgMM2KwTRJNC5lC7OwcXTX3kO-FJ_tA2nUReIYNowL4nr_RrBcibsTDHMWXQkSp1oDEaQljpHLO_TUpUP8syZA02rQi8LmPwegt2k4XzejkgXwENg1rOwOmHwLiWNo8f9WNcvnU0CaxJ2tna3fDmoDjH0Vp4TZYfP8yhMnfSgy6YH4QwaV0MoFvSWKNYsguEvR-CQfsDH0h9CKgvpo8J-wRUJlSI3thXTDsYHAUG4xYrA2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WCP5QAfWIAr4dsLeqJprV0CbWlm01t7N6zXq0lFzZe4Hpgtf_JeVhIvpHDOFZbphX00G90-ZMNIycmFg_eWKtfsZk--U19I4Cat81hT2JkyxYFO_iHxI-9ReOfnVUoxUcr9INFcM1RWDKokz7QEtP2py-_SQFMB53PuSERCNkcB3sPzr3UWlf4srRRlnfwvxCK9CHs7UFf2Xct6nT3kIJwoQk2f2x_fmBLeXccRLCa_HQxDLbLhcmHT7fRcst91EQH7ZJo6Ccu9GmCKh5RDRnwOgfMtdOa3vJ-ruWXugml7ruq5sXuRFoyF3W406avINOdbRvVPfo6p0RN0_M01UvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPzbDRiOn1h1GElW4KQCBPB_QFCwMY7zvmTV3pW5_SVlazlU5NyOArLd1a_HfgcnlrwRyajDzwZoGG2Go9f2OBYC5PRuNZp01UbCaDx8RVmiFW6NBI5Sap-FjJSRp24ItmSd9VD9KIfHLQoN7gDnNyhADsXWLPlC0PS_xmrWgT3g3oANafylCySqTo4pNKuOxegJRluETetQ9QY7J57kFZKHlwkBO5FYmU3roMnP2EaDQQsMQr_ZloMkvt9W8c2CPBpUndhvSqmuS6qoJ3W-fmItj_xjrBeH5wQsKaSYoF9uUclmdxv47yd1uYHLVduvnwDuupbDxqJcCZfFkhl-9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=d7cdaijb80DZT4c-piblXXF_vW86ceSJw7ImmamrKTyYY_R_FSWGcOes1uvuRVeyuOjMyqFnR-Qf6BMoQUx217V4XxxmaruadeM57-eYZccLCXvvggPoOWwrL296LorMNhL2fxo_8D5DfKlGb8QgBtbadOGjQEn4zYO03ZC3iwtuqyTa7ygXA3fXdnFQ0GKGwzJHI7xkbT-YuUHuYu-9AwlFE4ozsMluv6v0GIJYCewskhhtNytESJflLM20rY7f1wZ1cxuqTiMK9QSDlIedWMY8ffD66I0eQfIvIcNUxvDrNuS2ZnozMiS9ZXnSz9ElpFthKa1Bhf_oO1ewTz3nxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=d7cdaijb80DZT4c-piblXXF_vW86ceSJw7ImmamrKTyYY_R_FSWGcOes1uvuRVeyuOjMyqFnR-Qf6BMoQUx217V4XxxmaruadeM57-eYZccLCXvvggPoOWwrL296LorMNhL2fxo_8D5DfKlGb8QgBtbadOGjQEn4zYO03ZC3iwtuqyTa7ygXA3fXdnFQ0GKGwzJHI7xkbT-YuUHuYu-9AwlFE4ozsMluv6v0GIJYCewskhhtNytESJflLM20rY7f1wZ1cxuqTiMK9QSDlIedWMY8ffD66I0eQfIvIcNUxvDrNuS2ZnozMiS9ZXnSz9ElpFthKa1Bhf_oO1ewTz3nxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5jVoLEzRvt7jSALoLDzxG3-4Q2MIhq91rErYdrvGraM8IgvqMJSRikdXnk5IDrajFlaL9AdMha2b3j21JyuYiinwdJlWVlsBh5v5kQUhspBH1DTc_eJMA39Z6rN6FNBicbOmaA033tDIwPVFAboWDnswRL88bSLfsw96YkJdzO_0mHEnwR--VlI-pc9OGmgGrruSs-X2VMMMAh8OtgU7ovGUVXeARfX0dw54_aLDnhbW6-tE3hjX4MC4et9LnvSzN0Z7Fs_XthJe8a51ojvotrcziJ30ua1JC15yPX9FtGSsXoHux5k-A89gd2moMiK29GlsH_JYMJJYVJOPfk_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMVJQyiKNkLclioAoiqaT4hYjuGwuy_aYa3L_P4jhWunNvxy1WQKPtnByUW49Wo0SZuGbTESO_EH8Lact5t059-k9PoTE5looUTjeOFDS1iZEwwfIH6r7sAgEd9b5KZju-TZ56Xes2dZKsv3HtDt0i950Cr20bRsPcNMDmGOAOhlLBnAMvUWl1vHRXAoX7sdKlhRzuMR1oNC6h9WkI7g6YFGWppOED_NTfkOsJlqOvqmxLgHJFA8T6JMdxM1luKE1NBSO0NVDDLjLVfmPv2MGZeTGyQzbItaR_r78ofIL8faVVLxxIyqJoou0Zx6alrKkXdpz64D-3f6AW0LCMFMog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4ncGnh-tq5cTyjZuo_1tg-NXClXFtEWWQ76UckZ-qDwwqma60x4YXkp8DD0YHVgB0Q7qiAXFEHmEZROIGVQ_kkaN9H695wUK0WPxVHWZPdMhUCRYOFsId8A8G77MrcMnsEuI60msvbPfFLhK9JFvRB0GGJZxDUdR8lkEXa-YzIz_p7mff5MJ0PBRwUa7F9dWVuPUVdyexGzWKJgyYBJwp22lcyvKMFX-IN6VW2gfioTjtThvGG_56eRq8ETgoUkZwFF5MtPXdspa4fKMfs88WoEMOt5ysnekhG-P0v6Sd1dsDaB2T44JnFiSHfvjllhnuFEUYbfbNGG_FVmlIrqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ah1SY5NuDScnUfoNS5yae8_hNX9QVqPrfAMa0DuVwUApsbCblTWAesp2kyBPeB_gvSYNRc5VeL6CQrwt8_a_04X1XBkuPkrKol2LxkClq-cdOHjTXLFU9gHHWv6q6oQN35KoqxW0QAfGEe7ljZejt_BdZViaXA7y55KAabS4OYruEvFNKjUIUG4TnPeab8LXyWgTFBWVLt3qnQEGoEwzujrSPa69d_EikpeFxBsX5Bdmmg8mi0Q2-qJ4q5wcNllx1ZmpnMxj3QD8HCOPmq4SQjvjUoewUDcUa7EykE9p2HKTeRpIe_XtBBv-yM_kUuaSZkNSf2N-5ZP58zysri7_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=nFVl2SxzrJzDjn7uCjD6IRmnHjVrdp6claFTxG-qY7O1ctCbSUDxF-zWMeX78dmVhJx1nhGrHA3vQleMlkUEe5hPNwl08SwBFxq0_z1YRy4qJtjO3IO9X6To7V8cevumF7oeg662-ilOO5G8DlRzu_5RnefFgJJ2OVQtCNm0FSVkRLkfsNI1aoUm65ZsbrLc_V_hp9F4vUHONcqicGtJUIe9MnrJ-Wv2Tr9I0y7tZzQqpU8azb1n9EZkS_RojFPwprqgIk0_NNiI67Xfd0Z0A9jWmxs35MtTr8SUvoHF7lsgdJEDY-GY5g_2S4T78aFwpgjLJ3sJbaVFAWrhaVaQjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=nFVl2SxzrJzDjn7uCjD6IRmnHjVrdp6claFTxG-qY7O1ctCbSUDxF-zWMeX78dmVhJx1nhGrHA3vQleMlkUEe5hPNwl08SwBFxq0_z1YRy4qJtjO3IO9X6To7V8cevumF7oeg662-ilOO5G8DlRzu_5RnefFgJJ2OVQtCNm0FSVkRLkfsNI1aoUm65ZsbrLc_V_hp9F4vUHONcqicGtJUIe9MnrJ-Wv2Tr9I0y7tZzQqpU8azb1n9EZkS_RojFPwprqgIk0_NNiI67Xfd0Z0A9jWmxs35MtTr8SUvoHF7lsgdJEDY-GY5g_2S4T78aFwpgjLJ3sJbaVFAWrhaVaQjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف و البته خود علی خامنه‌ای
گفته بودن : شهرک‌نشینان اسرائیل «شهروند عادی» و «غیر نظامی» نیستن!
حالا حکایت خودشونه!
که زیر دوشکا و خودروهای نظامی ویژه سرکوب مردم ایران، جشن و عروسی میگیرن!
اینها سلاح های مبارزه با آمریکا و اسرائیل
نبود و نیست! اینها سلاح و خودروی سرکوب
شهروندان معترض بود!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5054" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMia0D2ygc97FxYiumTujB0WfjjAXqTOHOnrIwOn-nayIR0wPNMUvTdmb3DCMgrZQjsx8z1Q4m59lVnDudUy9cNF0BrDEendpFxZNRJmXD-okbsrDSHtbJbnKt6dOIF0f2CyLEoABZJNMIRKcZyWqhY5D_VxkBMiIs8wj6WOXUJa7kZNLpiV6l3gnPedQ7lWNMrPE6Y3d5AX-2vUq2KAriB3nGofqMHv8fvT6dje8Mg8gqeaU8fSwm_wk2UQqr-EJkrVK1rEFWuValaRDDZSwh3JFC1-G1QAmqWn5Xf4V6erH0WTF5E_31DT-2757v5eDRnaxTct-GhO2OFDt4PQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVbOipz4W_9lDfilWKmsTZBNpwu19i7dvFHBSAyYXZnUeb1Gq5NDjV5pZRDhwVMNQPV5mE3HVYCmGZKUlDXGWE2ICnO48xXfUrGNUxnFbNa66AnnOlXJUbV2F359CkpB8U4r8T1hc2U8iquJURRcluASWz7AYaMWYzs3U1z3fQ6vELg5GE5WuQOzOTN6TDggFQ1aTsrzdJrE1-NSq-_JdIzdlGfxHRHOYXLyHPtSU1xxSN6-aZCYa4mEF2ZEJ1hjmoJ982onSnRxlhS9BMgCy8coArs9Lsf9fPe_HS1RqZFv-VuL0LdF22AWe0DQc_3zMaF66QS-_U4-uL-Jvz_LdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BINW11vmA-F2TivN8bSXVJMyFTiiqSHRC7cEPeHF8K-_hSM8yRx_BmcIj6eqvUXr-8nUJ1gdFAg3nWjEgtfg0-LPFyuG0SdV6Sv51ERNUg_EMxkd3bVPh7wI85oWNIf-CAzlS5vtXIZWB3e8VAUT_HvNfmQPk3MyWUCTw28dqCfM2do7td_PhF1sSI2r2XfD3oEmOr4BnlnS_rer6nLoKCwU08xhROR9-yu91pVNZxtlL5oPEANj4tKl7Al6wIM1V77prS2_510RAMx7zr2OqTzsc1k-HGrOdLyGK_PGFewEzXj2nM8tdOgrFX0xoLPCPhOUuHvvAAvBhrTebz6Zmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJrBHYz6Xhmky19-YCU7SSVJbjXmz8JXYR83dNHJXN3nb4Ne74f4S_dfFWsdiIFInhgerJSEzFcq2mE9pnv-H4XwSU-gNarLznGy_XbHV7F1gr4CZ5zuVnD3Djk31XZ22n5a3-QMQqGnislJDUDdxuVgkdJgWxpn7xE7JsjVPiS77qG49Rg-Fpb-MeU4jq5xLpBC9dja7ZmHlCVbuOtclFHUvv5hUMa7NgYKFsbh_43BQoxEo2Aa_-QtrVAmJ52qIpSmLmQuo36v4sXRYb-VWkjkdg0rTQT56GEQQ9cAOV7qPYDTDcgsZQAv2qYXQ0GSIwKHZqXcPGU_7qUGQBQ8UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5dQOXxZvbnq2J8JiJXFQEwvqm8O20rmMNdUvsoiMmyppS3DWfpLx5xOG0OFBIQj-9aia5RKJgam-o6QwHFXGDfcT_u_kNUX4i0iR7bPFmiXoxqsUmchu6XTZFg4EkL6dYt88oiBz0jrsXIws4bM9jfEQH9vT6zXWXy714GyCYLzR_v7SUbBhy4WID8qA8oFAxkpoIopXRihe8PlKdidCUKYfJtamhcDlIKHTQMvm87d5oCMZYh1ONfDO-boXg625Acq2swL-piackJOse7kembEOhEpDLLK3wZhLWb1nDxV1CmicN0ImFZGS8m7-TGuWm2i8eRu3Gtw38qGRLaTRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=df6Fwt6Ec9xiOQ7Ey_RCN3afnBtuMn6l6HcCB8pBe2S0aSq8FjONx9oXWUVqtOmgkM_uFGJv60ISO16lDQKn1ieu0vI4MWGKTN3PR7i2mYSb9Mc8r5pqCkymXrwKdMLvNYL5xoH-7ERSMeB4YXGS8ZB7HoAO2uqm4XMWRehSgR9HJSsU8GwX-vAh5_Fn6kzcyOzE57rAPvc3as3tUvItEYM9Q6z8FdQHxhJtxyFGWNrtsqpVtNqbe7asQ8TQZ0SqXi1wFIEszO1ciZu7wTPjvyweGfm6fjoeMTEhNo9fzZBzFwNeBXqMUDbRZEETYGlKCVtHYtwVPnCMfhJZoFM8tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=df6Fwt6Ec9xiOQ7Ey_RCN3afnBtuMn6l6HcCB8pBe2S0aSq8FjONx9oXWUVqtOmgkM_uFGJv60ISO16lDQKn1ieu0vI4MWGKTN3PR7i2mYSb9Mc8r5pqCkymXrwKdMLvNYL5xoH-7ERSMeB4YXGS8ZB7HoAO2uqm4XMWRehSgR9HJSsU8GwX-vAh5_Fn6kzcyOzE57rAPvc3as3tUvItEYM9Q6z8FdQHxhJtxyFGWNrtsqpVtNqbe7asQ8TQZ0SqXi1wFIEszO1ciZu7wTPjvyweGfm6fjoeMTEhNo9fzZBzFwNeBXqMUDbRZEETYGlKCVtHYtwVPnCMfhJZoFM8tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5046" target="_blank">📅 23:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ :  از طرف امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس امارات متحده عربی، محمد بن زاید آل نهیان، درخواست شده که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازیم.
آن‌ها اعلام کردند که مذاکرات جدی در حال انجام است و به نظر آن‌ها، به عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همه کشورهای خاورمیانه و فراتر از آن، بسیار قابل قبول خواهد بود.
این توافق مهم‌ترین بخشش این است که
ایران هرگز سلاح هسته‌ای نخواهد داشت!
با احترامی که برای این رهبران قائل هستم، به وزیر جنگ، پیت هگسث، رئیس ستاد مشترک ارتش، ژنرال دنیل کین، و نیروهای مسلح ایالات متحده دستور دادم که حمله برنامه‌ریزی‌شده فردا به ایران انجام نشود.
اما همزمان به آن‌ها دستور دادم که برای انجام یک حمله تمام‌عیار و گسترده به ایران، در هر لحظه‌ای که لازم باشد، کاملاً آماده باشند، در صورتی که توافقی قابل قبول حاصل نشود.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5045" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مقامات پاکستانی هر ۱۰-۱۵ دقیقه یکبار میگن به دستیابی به توافق بین ایران و آمریکا خوش‌بین هستن.
موضوعی که نشون میده وضعیت برخلاف حرفهای مقامات پاکستانی اصلا خوب نیست.
🔺
یک : پاکستان در کنار بنگلادش یکی از متضررترین کشورها از بسته شدن تنگه هرمز بوده. اقتصادش دچار ضربه بسیار سنگینی شده و باز شدن این تنگه برای پاکستان و اقتصادش، به یک «ضرورت» تبدیل شده.
پاکستان فقط برای یک ژست در سطح جهانی در پی رسیدن ایران و آمریکا به توافق نیست!  بلکه برای نجات اقتصاد کشورش دست و پا می‌زنه.
🔺
دو : پاکستان قرارداد امنیتی دوجانبه با عربستان داره و در صورتی که جنگی بین ایران و عربستان رخ بده، وضعیت پاکستان بسیار دشوار خواهد شد چون بر اساس این قرارداد باید مشارکت پیدا کنه در دفاع از عربستان، همین امروز هم ۸ هزار سرباز و یک اسکادران جنگنده در عربستان مستقر کرد و البته سیستم‌های دفاع موشکی،
پیامی به عربستان که در کنارت هستیم و پیامی به ایران!
اما وقوع جنگ بین ایران و عربستان، برای پاکستان یک کابوسه! خصوصا اینکه جمهوری اسلامی در پاکستان نفوذ زیادی داره، اما ارتش، دولت و نهادهای امینتی همه با عربستان رابطه بسیار گرم دارند.
🔺
در روزهای اخیر خبرهایی منتشر شده بود که پاکستان مواضع ایران را به طور مثبت‌تری به آمریکا منتقل می‌کند و همین باعث سوتفاهم‌هایی شده بود.
بهرصورت اینکه پاکستان امروز دائم تاکید میکنه که همه چی خوبه، میشه حدس زد، وضعیت وخیمه.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5044" target="_blank">📅 20:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=u8Qj23xlEbDBDVafqlpfTj20RK5BlgPhQrroBp9LoiARFcZx_DNNgpNS4i6nmhXRrvlMaL1R0ikMVUDanIIcNDqQoBXgL85PBmnBps7REN-0dtKNbKjvQUEcvym7ZVlX48JdstXn_ascli0ldVBADic3F8qGhqaLQPZa_0xbPvkeo6QXigpvZZyyYK5rxdCJ5iwiWnRAwrXf6VKpuz-3odNswShXygHd9O7FAAReoXEQXRKrW_I6aoOIonLQC98tXpdvKAXFIs08_PEuhK-ofKVRTy1XFF1YmbxFmyiPXHijElEkgk-gJgdPUvMToPb0xQSknOidLwyNvl87Ahfj4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=u8Qj23xlEbDBDVafqlpfTj20RK5BlgPhQrroBp9LoiARFcZx_DNNgpNS4i6nmhXRrvlMaL1R0ikMVUDanIIcNDqQoBXgL85PBmnBps7REN-0dtKNbKjvQUEcvym7ZVlX48JdstXn_ascli0ldVBADic3F8qGhqaLQPZa_0xbPvkeo6QXigpvZZyyYK5rxdCJ5iwiWnRAwrXf6VKpuz-3odNswShXygHd9O7FAAReoXEQXRKrW_I6aoOIonLQC98tXpdvKAXFIs08_PEuhK-ofKVRTy1XFF1YmbxFmyiPXHijElEkgk-gJgdPUvMToPb0xQSknOidLwyNvl87Ahfj4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‏رویترز: پاکستان [کشور میانجی‌گر میان ایران و آمریکا]  در چارچوب پیمان دفاعی، یک اسکادران جنگنده، ۸۰۰۰ نیرو و سامانه پدافند هوایی به عربستان سعودی اعزام کرده است!
سامانه پدافند هوایی برای مقابله با موشک‌های جمهوری اسلامی است لابد!
پیش از این
مصر هم یک اسکادران جنگنده و خلبان در امارات
مستقر کرده بود و به ایران هشدار داره بود.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5042" target="_blank">📅 16:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSR92axH-3L0ffWX1OJ2IURVnNxuPdR9sEdQS3VkS8YspZG6pS86EcMLCNzMDURUnc5PCLLP5HFeKUDcnoxCLnDLflIQbjvRlwSkIJtALvcWpuu9m2TpBKUHbmcnw9yNS_U0iTF2dD-ttlC-ZQKi5azISpttAZiCzNBi95J75B0Y-2RWmZQmaOBJuMo1zgO1-JU-ZV6kjwh2qgoMJjW-q7FwKWSczpr6DRfrssZdaovQW7rOwR59YjB9Xah6z6zO0mT-VWOr0wK1xe1haDl0N7j_Cp7qtr2Gtbdh8tZyd_WnPVM6uQomT0oeTFq7aM8Sk5qCLLNZigwiqb3YRw2zEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
