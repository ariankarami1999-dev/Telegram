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
<img src="https://cdn4.telesco.pe/file/arziyzhV1ZYOrb2_hynS_a6JEF7CVzsiHGnUSih4vBt-45FRMgGS1XoxQsyxs0vquIoAmi2OEhbJqQ91N3xwjikJy5v9Bv5unqgbarwHDmWnEd7XII7ULaXB-wtvVJA65jeQu7la59SPvPdDp55EX5_acatlcteNL-Eodl73Zgkwn0o29UPsDxu-ySvehQsmUY_MYbYxPSi2JumAf6OaS8SPBUMqVmPpKDYkDrlFs8VVoT-DXUGihZ9bdLnKkCiZT_qOZGkg4BlF3VzdTSRom3W8QrjVd1lysvWjRJafbTQUOr1dHI3S2wQzU7GdZ1q4MJhMbJ4HuN-5u3yctI1I9Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 15:03:20</div>
<hr>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5FydOHjNuTiD-8dDiS1igzC5k5pshIFfTHl2n5mgU8S3kZRWMsQhY8C92MOm9ZmgRZUCiIIY0qq-Ai28TQgY7ccJf3UxEW4q4KRqi1X5soa86tpqdhGSXe4yvtZWBR2kHgyovliJo5ik_F3hHxnsZKqMxOkg5ZCwN3HCN0c1kh4ZT2cEcGxVLgnqVTlmQJTvU3GIcMXXcxnsfsiWOvgvxhmJ_AfIAgwOVVOVEY0gWnhAKMrXmfkHv5Isef_oXexWsF3MFT19WBei4CEEx2nIoPEASKYs5QaNSFA2YjdGoVT5qRbrOFhmlU2ceTHLLnnpGwAx9FV1ngjjujeX4d4HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=qReOBQgrkZQrlYWw98392ezsI9ESBAwWh44ySFRQl2ftCTBZrr15ZzaPyoQx--jfDixFHTngGFuIWesZV_QjEtmJyzM_MpsVGtv9Z58IAc4fje4QTMEGCpLi0haHmH0wbiyPsikTY-mPghf5WhS3rOcGxR_B4tUuRFUJm5YLv9q3sOPZcrMmKUQuk3O4WJ1_2vSQQV4F9q1pEsogzFESBkKqeRCZbyKc-Oik77lehJDIMsgmBmnwWqNWqkD56koQ4A1gg2y0eDWdoG7TSKbv02afHuycQyKOZ1vZrHsdw2fc7kbdk-H6OHvRT6MwEJr3uH4eh7Stg1BTDEseOTD9iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=qReOBQgrkZQrlYWw98392ezsI9ESBAwWh44ySFRQl2ftCTBZrr15ZzaPyoQx--jfDixFHTngGFuIWesZV_QjEtmJyzM_MpsVGtv9Z58IAc4fje4QTMEGCpLi0haHmH0wbiyPsikTY-mPghf5WhS3rOcGxR_B4tUuRFUJm5YLv9q3sOPZcrMmKUQuk3O4WJ1_2vSQQV4F9q1pEsogzFESBkKqeRCZbyKc-Oik77lehJDIMsgmBmnwWqNWqkD56koQ4A1gg2y0eDWdoG7TSKbv02afHuycQyKOZ1vZrHsdw2fc7kbdk-H6OHvRT6MwEJr3uH4eh7Stg1BTDEseOTD9iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXI-NPoNnSo9x-x0kN-Lxb8ulmgsGwDuFLiF_4idoyKe7rPr0h0CWp2H9tcE_sqvgO0RbIHn7LzIJiZlcnk0SQfmFc932I9baWy-q0dIIbn-kkGW8TlZI1d8gGapvgupmbTZ0PabY3qRwNbMIfLGPU8AYYMJH7DhFCG57ffyM5XTQ-_X6Kd4Go1cUZoT3Ug9lIXTXO1o5rXSu0n5XIziL4r21G5fsAy7hkZSKMTAjU4AcXmv-lWwmnOnu10LeOlhPMnnb9hDPEK6DwBoufIzLwtWywO_V3uFLitrBj4mpOZ56TWzn7FjdiCY-jjt5hIctkgiCJyUQ527KB14Njpc4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2d1dzSTEe2rHc0fAg61_jayXXVJI7yvBBpEaqzi1RB47-wycMaZVBinhPaNr1lJkne5QBkmTSgqyBkDY5sgKNCUu3Telglo2ZDzxo56uQR6G8YCn_yG6nvCHCqH0Hbw9KRfTT0e1DVdbhYga1Nwfz6P4mDB9EnjAGhwBhZu0cJvwR2gjTHMGaofWJM1pImQkn8ZJFVRE6b5bzTbMa4zFUhFqYbxa-INj4-ZJDox7J2-d0StX8LxtmX1RkG_uEYQ7wlgLjdM6NIoXZyo402g9lC61vtD7QBXZy_jni7OdvRH9FCeC8NA5JfLHmPDtZpN83YORjTCVnzWFZDH68NvlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bibQA0SdPsLkMTfFiXy-Kz22QK0x5u2KtR-iA3fr5nCpCrtiOUHkAfnszh5R-yAVGWQk14rNB9YAbC-1ius26cP30lE_BVpzMWp9zyojL3Fdyt8bAtUWqaVfw6w05d7kJ8Fl3Nv0GVHZijLCeuAWCk6w2rY8vTYT-Sll99VE-xviYtY2VF7ITuLZfBbceREGRE8eCzkOQZRuayipMuB4WjRhIeZboieFItkCIGuZS3E69_8CLFXzEGfxfve65AzSNzyQrLw7VBu57Rs7QSVHrkk91Z8EjeXcBVCxOKUlZEC9MCZiLdnsBbVh1QM_sRRz3ILzCUJx9mkFAyrem3OewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
آکسیوس :
ترامپ ساعت هشت شب امشب ،
در یک تماس کنفرانسی
با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=a3Hevze2ZG6v05bApSk5C4Wfnl1wtPdJtdgx9QSNrJAwKhvBNMDVu0K7-Q04JyP3rX1ju-3R56CrlwoJVQj7_dgTBLFQqP0Dz5U5a1LzThUkYQ5B8zaTR6ZuZ8O4WjeHKK78JLmSfyNSSF6CLXkwyc17LU4eNdLmjpu-FvreeEfoF3AMWDlBZUUB9YyZjz2bMh4z1l5iy0eADTMDNONMCBP5kxR6zty9x1-s6n9ERF7NTB5BThY2JpH0NGi1Sxp8NjX-v8JyE8KAqAGFUjWT9nYCOAgZfpELuHvRUFYuh664ZBZsOPqgYXV6nsZOJG_mcLS1pNwTjn5MbE9gef7Isg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=a3Hevze2ZG6v05bApSk5C4Wfnl1wtPdJtdgx9QSNrJAwKhvBNMDVu0K7-Q04JyP3rX1ju-3R56CrlwoJVQj7_dgTBLFQqP0Dz5U5a1LzThUkYQ5B8zaTR6ZuZ8O4WjeHKK78JLmSfyNSSF6CLXkwyc17LU4eNdLmjpu-FvreeEfoF3AMWDlBZUUB9YyZjz2bMh4z1l5iy0eADTMDNONMCBP5kxR6zty9x1-s6n9ERF7NTB5BThY2JpH0NGi1Sxp8NjX-v8JyE8KAqAGFUjWT9nYCOAgZfpELuHvRUFYuh664ZBZsOPqgYXV6nsZOJG_mcLS1pNwTjn5MbE9gef7Isg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzGjNM5g-9Fagez4JpZ5aGKIatQv9vOqAfN5jsjv-NkAGJ9oelCzMKJ5GdyA-vTO8LLY5o0TvcjPSOJZm5WvzuXqesQydBPpWSQ1D3UjGKg4LIdzAQVExd_6FgwG65xf8fUjM3GRDdzatdHjriV0FYq4AiRSq4P-KySIMAvjqmioLqPIkzygNyKjOa5s8KA_l_Xe6GKTAx8vqeGZNw3TkzC_-LH2iWmCWgFsAlSlaEz3LK2Pred03UZM4zepltqSROfwPET2COonkWoNGC7umy6AF9K30C6s_SX_Ke5aS1tqSsSEyXuCahMaGa04cj_rCKNrB3BD31EZFlDi1-OPcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHbJTiOt-XO3MhoK3cIFdpp0upe1Wd7RCcrSK5IPs38z2MCPGeM9fx_YJYI9TxDj443h5rJC24By5kZ10ZBDHUy-zUXfFEvAaQDRh7Vz5ZyEUGTd7znjxF3buv5of9FXustb4ZUkricJnVlBUPAvlbwJFJqx6FWvKX-H6D5ovRRMwv1DUFW_BPPTafF4rrMjt5BsYteytq_byMYIN1nxO9afLvqQIIakhrf1IWJYhurCvy8YJKf0VRh5ULK1yqNsEoqseGEdkbk19J4ZzyWRihQKTYmyV4jghsf3ILcBPnXYrtwB9t419fouPzUugghAx40jtjDVddav5YBe5ALoig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahBFxUTl3kuJpxmhaKn00UKgo8ve5fKF-uAnKPU2y44bxdWYYdv7UdXDlEiVicH5atOZNJcLoIOawJeaIak8N97INSedo8RdtD09DyNs9ACICfhMkdWjILXnVUIeTOVDZ8UsADOEYBaGzS589nDGWN2HCPJ_koLD-JQg0bfS8QuBovGCJw8tEG0bp8vBdha4t-M1SiCh8oxPpeIARaSJnFLT9nKQj2o2ZAgxCXj4IfiWaliCXADzNpBDuLhXN3eLWBFafBuzsx3MP7Ds9NORZFY1kVnnbsJKH-wjJBvEagYKp71IqIoXLTUdHDz7nC2yjBnneQFXLCFFCekw7wdZ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTggv82Xj7n9BKqChiY-2HTQcEghicT4i_XaJPzPIB6kN87amg5KKIZHkBl_A52nNq8oU_vt5rksdzyza9b7pu6BTdqHMOUJHqirEyNkUU2_YCxInAjHaciMuIZCqq93dNU9odu6K2GJYc_siPLOaE94YbTEQIfvluvkMkcOPUis-LC7ZaT3IH0jl4N2IS9eP9yqt7tkpG5ObnHJ4Ev-Dq-H8-PaypvrpHiUh72Y3VfbyOIu162Lk_zeuDcFMkVc3FgadlQdNhTLzUrIsQCDiB5PUrKfZ9qs1uMmA_6T0qeNi9i03ZhAM9iAL7aGcGFolZpvahBiC5IYNhV_aXvo4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPzHp8Z0KN8_EL2-kt9840TwMr2KEYTifO003FuXWtnW-XTnFYVbGlSU_pwcO6twscO8_0TaI7mZrWyA5_J7wsx_vqCgzBNjRY6GmVGGbDtwRU-LKBGa1IX0Zr39kEdCUlsySOQ_C8GZvmXinWLI0e4JARxPvmEDhJmh7FVeDcuYCk9neM5xrg0LyY0kUYtMM95wwQINGTerwTvqRTts2w9A0od1OWa5vqPaQDsvSYIopmuokKod9CwaLgW4KLzDobbM3b9fF5khfwE8I1IgZFBAYEIGZvVkFxQjZBW_cA3sTrY5wJ_rHUWxMP4nWEYX_e602bSZHISmEpI7F7JQ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C72lM98v43I8CXb26WD8rL5EXhE_6zzds19T-TiA91m8UZl6079kWsv1lX5d90dv-qlZpS-W-vAz85Ps25X0QrdOYW-xchRE62ssOAZVBWL9T66mriLH38npUrYhuQ3CwSBx-FjduQ8VTrvE-arkpcufw4SwxxLZIqioCDMTgsUMhxhA3QHcFIKjEY1bb4qjcBuHViac4-ZFZ922Lyum8NRdgDBEdpkVpPm6bTwV1N7qBI-ULHgbVKTcdLmL8FuxgDn_1ib_48nLsATSGCcRRGw-Mv1qWaKNQ8qpkSJ5cSFnRuSUl5IvTl6K98s5cW0oVtg_RgfMnyjBFfPjqi4ENw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9bol9s_eg1qAgy1aYVJN6gWna7e_9JbBpDKWw5NBHfu7Ue-mZacZcSFa0NkLXWtAYRd-ntVAPXbqk2UO4q6S1F58lkPLimL_jBKS3MDcWS4KpmBkPoXUXUoFI6ensJXFZjCeEgUCnY5vbh3_uwF765-mATXUrvlfZHn4YbXBCQKas4oELaNZ0qdRt3iip3p3V1_bNd161xIYs7GDuckVF-AWQq2JUFb-zrkusLiKgot3G_jWtQ2t8a7qFMde2Ruk84-SlHgaat-8k9VV14bHWWOLQLga9vxrDUUnLOEV7SyKVZXx0YaTOysW-jKv5hD34N2QIOHnaqVURrDRrXxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6hRGDZ-9nzJMqdmfMLv3S32vjpL5GyFB4jl1Cp2NzaMKx3Kpvfntmvj4EAguwRRjnCQLezHViDaBUmiR-1zd0uZ2CppthvkWKm5fBG6R-6aUpykw5oZNZazu5D94WnVWz5kBUhsWn82vYKg9IIjjL6j1F59ovEqxdSXvyD7_EdP4ndwRcAsKYMHc1Wk4pjCAQM7nOetPBCs5zVtifSHHeh82Ip5G9PFWL8bHBBY01O6FN2po0KA_2jpQoN1N1f0OxshQmU2WEiFstqyp0Qnm2p0oYMTqSAgUi4W4AZesmmI5gK9Vp_30ZXio4_DuGXAEeNMBpXhP1fcPNGl8dHCkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4lpur_H23fLEykRi8e9Ns5_2Kiv_TvPmoXhozq_KUMFcWg3kCVtbOZuw-R7lhC9oPHwnn_F-i47RDdtMAqcMCl5ythjQz5b1qA2xQTKvrXnPlM84IQ_RPSB8r9CNn0zeYUfGmrthxUrIUg44rnhpLkzWHQuiH8n2NQWvIVKf_O5zQbjufvm3OCW3Qa2fFoa4JFuQL71C8hXsfk9ndmMduRWKqs0IiJpSUFketZKo0FgmylSmxGxX0Qo2zTb9x5JWFMe0FshbSlWnR5DYEZ9q1jL-l-QpHIotLF4vAChpCVONIQLNEVJcm8nhcA8GzkKn9TCQfT3940RNsq4jg43PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-8LIfY-BPFnVNSC3dJ3qGvGI6BkQ2zY5xDtvaf2MQcUKBliXcd8-sxv9vphsPMHDo4uYYCWHJaxlE2e5NdwR8-nkeSwAL3NWw4HDjZcwjKTZGyCaFp8uBGRfC3E1MVJ2Cpyk7EkISl5yByL5sfQYZ3EhdaezfivkWbZ7n5M2enN7-HqM2167eRs01tEWel4XDMyoatPWzbdbNOnN3qe9YsSu8-JTV8q1artktqIsDDOK3MHfjzgagsQ9bLUxPeQEwO0dque30MVwSoeFltZTMVniaz3mtdM0kGrNRVwJHBHPq_b8e7BO0frFPekIuBHhLQ5pfWUZQb3jOeb-pxAcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRc77I_cmKABozFxAbue1gUpDl96Q4gl0-rfnGV4d_BfNRhDMWm4LhXAMANub6IN9lK_gN1htDzwcRQ5arCxxO-Ox8wUuO2OxsK19tR1MugHQZSezTICScK_aKdKe9III56YeiXvHDpK3G02iDamQmZ6RIiA9agYl2k128Af748xzGJOTaRPRrXKJrfKWKS10Y4ql5GOfkO1g80dqjYJB5qRjnaCb-3feuPcR2i8WHy9mMpbwG7aiRF-56CtvjdOyt7oy-FuFbMhRxKf4v18us1xAQ1x8Y2UPmk3n3wvqAcq1QkPcsXhcB4foqg-yE3iznjduAke4Cwb_1ToejiMEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=MwJtQuSZ6Yxp3uQ7PIlmB68nUMJeDF6hw4bwQjHnxKHf4J09avicAkgaITlno2xe-v3Fsf_adZoZOyFg7XdLjs0phQ0SnOqV1f1FiGpVWqokOc0IPQmhikgo3ljEqAMUplBuJdIHp68ZNMJ5Spnbh22c1U5jdEDjFUAaCUg_WFG1qLMSrkjKn1U9iJOwWBlkK_rovHvXNUNRhyBTS_XAte5vJXNHa8xgEcY5EYFiOP-mz9iTcsehV1nKgQWenmXWjjIiMouaF4g8lxJO--Vrq0xOC_5IHSvPFxmlCUNOMKO0ZGn4De-p4ycsOJvaW4aaVOqUFN8ifi_RBtcfH33ffA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=MwJtQuSZ6Yxp3uQ7PIlmB68nUMJeDF6hw4bwQjHnxKHf4J09avicAkgaITlno2xe-v3Fsf_adZoZOyFg7XdLjs0phQ0SnOqV1f1FiGpVWqokOc0IPQmhikgo3ljEqAMUplBuJdIHp68ZNMJ5Spnbh22c1U5jdEDjFUAaCUg_WFG1qLMSrkjKn1U9iJOwWBlkK_rovHvXNUNRhyBTS_XAte5vJXNHa8xgEcY5EYFiOP-mz9iTcsehV1nKgQWenmXWjjIiMouaF4g8lxJO--Vrq0xOC_5IHSvPFxmlCUNOMKO0ZGn4De-p4ycsOJvaW4aaVOqUFN8ifi_RBtcfH33ffA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=q2vV5jmsUW9wEL2x-phIUnn3DqAdNE5rQgamlFW3r-L--8RlzmS19GynjmUOuxFyg50bgD4aXKV2WLEU0vUewshe_wNtQAqxBqnfyzFw1J7U4wfI9e1lL1gjZJHzW7LxOnDGOir_UlVlxK91m-5_FUCDfr7w-8nkrCIUUAoiYg-y1Auy2JIOIFjiF8bmudwKDgDlZHh3rQ62ghynnq6t5Y1AGr0xCkrviX-zotWI0V7vMgAOfXwdJ82yxjE26zzXB8hW8hKKCW3-mXcp1qZR6wHnzroo8QjOzjZEAB71HteGRRveRsmhUuXwPtm59Uk0WX0--YSl1V05NlR6ohw0ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=q2vV5jmsUW9wEL2x-phIUnn3DqAdNE5rQgamlFW3r-L--8RlzmS19GynjmUOuxFyg50bgD4aXKV2WLEU0vUewshe_wNtQAqxBqnfyzFw1J7U4wfI9e1lL1gjZJHzW7LxOnDGOir_UlVlxK91m-5_FUCDfr7w-8nkrCIUUAoiYg-y1Auy2JIOIFjiF8bmudwKDgDlZHh3rQ62ghynnq6t5Y1AGr0xCkrviX-zotWI0V7vMgAOfXwdJ82yxjE26zzXB8hW8hKKCW3-mXcp1qZR6wHnzroo8QjOzjZEAB71HteGRRveRsmhUuXwPtm59Uk0WX0--YSl1V05NlR6ohw0ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pN9rvBXMht72EE2jQYRTS6e0qWvtIxe3xq-nhUTL5OdE14OF23OeamJGfcUVyM_TTYge29bdYTdv2RcHjBpb7B6IOqGVg1BTdwupIjlfzOpSWXsAq9p_aE736bUPjRabYZ26pFAtXl2iFC82OFZLlYai_HpeQQVL_Dy7q--DyAg_0lVtbYHSKhjvLRKMpnz-YkURSOzWpCOrjAhgjGWq7arMY2YU4mw1Kp4lbPZN7a3DbF_mAWbNeNDN_Dnn0DXIna7XFUuXnyp8qLRoW7w2pIaBcfTyLv8WHZnXzKxGSO1-o-tPdiNShSBwx5rBTz9XaMqi-riO-v7bF9ZC0klxYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZIlkzB4QdYg7aklA4qUBkLUMb5121ZJcq2D7hUvAY1Pzu-PGBHzW7OvqkjRbdmH_m50feXvS2jIT4VIf824k-VBqmoa1-HR_F-EiLmmWv4q_o7AJnOaNAEO6Lnhs1x_DPVMBdfOh7TLhavEPRdb0-z7JMzJOReABkG5fcjt8Ixr2YCZYsF-NFqy0DQ_pFVQ1p5IqSbqpPYRUeTeDj_ScwHnOllmWPFdL7YiFqaXHLHyoJzzpANNx8WfrS5ffXPMs8BDvkhGCeJ4eA4KKC9YRX_1Azi05-y_3Np-JyrZsEaBhbHEsOS_Wm2jtSX1ci0Z9O31xuJYUawzuhr4sMtdkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXNReTU0k_aWUR4LeLQjNq69R93lI9Nb712c9mqjXkqsDXbqFniHeenglyQ0MlRweDz2RlvWojheshcGil7Md_z0f-z-6DImfeWv-N291SiGCxG6kb6a42Xc-D3F19Xpj6tUnCau-MaIa7T-ySSG9oWVTbtHombZ029zS5E2SouolAlXqJWJ-5GxU8L6gwOCi79BthidJmjSvyLVllp8Is9PFPEMCxBjejCkpc_emBP-im4PLmnZdUQ7CPD6frkYUsnbKnN51BUhupUu9MkGrylnl6z0t_AqprcNcIOCv2zfFLr0dk835V7WmQimsx2yx42HZQIFurVzGeUdFXID8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=b6AaEPZqbVVGLcQja_QvOpbuhRNTV2nPROEPdhBM-y0rmorHLjoBYFn3PJksySicOd3d5xD-Qs9V-x7H38qYTYh4hGekKhzwNLUqhtNDQdCPCYDStzxpKciL7WYI_DMAGs1psp93InEsLQV6KWwGzqRqVOZGvu0X3bYUHo97Vy7J6RoIjJ9D4kCMaEMruwVbPerQJm_2nwSK4_QU01avbXaV952nwW9GjNeAf4SHExY8BpXfsqas6Tk-wf_foR9yjfwZ_k9GyeXbiJhG1tIKBPkdyTl37X752ZP_89KWcZuMv0Uf5eFtprwsiPzDHsP6P1kmLNhsjbVelWM13uH-eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=b6AaEPZqbVVGLcQja_QvOpbuhRNTV2nPROEPdhBM-y0rmorHLjoBYFn3PJksySicOd3d5xD-Qs9V-x7H38qYTYh4hGekKhzwNLUqhtNDQdCPCYDStzxpKciL7WYI_DMAGs1psp93InEsLQV6KWwGzqRqVOZGvu0X3bYUHo97Vy7J6RoIjJ9D4kCMaEMruwVbPerQJm_2nwSK4_QU01avbXaV952nwW9GjNeAf4SHExY8BpXfsqas6Tk-wf_foR9yjfwZ_k9GyeXbiJhG1tIKBPkdyTl37X752ZP_89KWcZuMv0Uf5eFtprwsiPzDHsP6P1kmLNhsjbVelWM13uH-eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5097" target="_blank">📅 10:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDtw5AkTIaEDhr2zgDRoAOGsS5GU4aCTx9lKf6ahMWcXOwyHPrI9rZxDHoRnVmnEkJhRYOXszHtCcaWr6zP5YODteMxgphzj1R1kWRe7OAeJPeEVhid63Zmros_6vX_H2wMf-ygL8xXbYNce3WzXJRO5ORdIAZDbBvzwipH4alq3xbTKbul4WHwjkVIjg1Dg2dbfOwwGU-A_3GEoCz5mDPPaGyt322S8DToR4CkDL98Vuo4vBM6jJitOAvF9Jm5xJWBoWyXfatNkgDPWn0h5gwOczTf6vuxNk3P6UaEqvR8MAOej1N8Ldi9R-k31wajuxT9qDTSDzybqzL4-Oy1Q4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkopmGhgzyuQK2zOmi6Eq7mOyeDZJWFaH1vZOvptMlcFT_BSImmZVb3Jt3WZdxhTaa5NsfKGt1DVbTl-VML2071ZKSJ9fkSiVs5UL7McpITyWCa55XDji4WCtExnksEYeZemXFuh2Tkj1r4QdI4acynMWMgLc_jycDFaCjGrhgflp-tSKccosM5RSqCV4Vhfx3RtWhZG6YI7-BRtMswuMXxsVU623d--WVL70EOHeFmwsN-Dy5xjROtoO17U22xb6ESUaMZyVMaLXs5OkwrkFJc24sOygK7hhpVxAHB1MnCvWP81AKx0DYWtt34tKuBqFTeY-mtADUspw67qZVQzQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NseV1liy85L4Wm27VFTx6UMbNEOykT_S7FmGRF9JsSE0VlgBqPi4FizrptRUEBvfM_EPP0SF7ZAfBnvdnue4AsCPXhSu_A0ra79d7_s29yynsBrFfvhCmuRhpe9-C8ZHCDAhLcnKYyHSm_j0EmH8HpkFnmWXcITXS21rwQ2QQjeRA0ygK17Lj6w2l-LN4IPzbLsROo8v9UvwamkZV3Se1Pqrk-OYKbLQ647gXZpjzC-2I8jun9Ki5g2AI4F1RzRPZDqbbVrWiDiWTNnhbdFy5lk_styLd9sti2t53axtxKmLpHbPTpSFQGxsbffRvR81dEjaoXg9JAjxME3GGGLTGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7HiDZTqnfpWqj9fvA85rgt0NrwMmIGmoUoyge332Fi_lHgYUZUYQwSmv8XGLA-pbNuLRWgv7NM1sumzpYmCr68N8LBF8okg4irx6dL_DKmRGj0kz0PdHm3T5lcYffzjBymV5byNKT5mVJBhBIeqN8lQdzsXMNhz6EM8ts32OStCp7lVzhJSiSJmSaoQ-Vqi02_70HLHuYZVCUBzRXjM8VOa_1et635IYkwWo4R-xBMcqo4jOnaKYvWXfY_g30lsYRL3gpgDtWIUYevabjpIvEG7NdpIEpnpZscKo7s6sIcOMLG87wKmqmdgFO0neFUDR1RdTlzn4yKc2WJD82GujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoeeRMzsYgH5J8RoJwYZkH-813IM6j6LzIO8-fc2rVrPQJvxE_EUjUy3-EB2CD9zaxUcaxL-z9HoaOl0XKwz7ADBGIROgMcJBb6QqEuOMmV8Pu7-j0RnMKa22Ow6rBvu0EUKGGVGS0Ly0PlXawm6Kj8GyRbnmLWAPXVAdaTfEqoOX59C-qCSN_ZhaaZcOFNCcJDb8GQEyeOgDm9zjkpZAW-bLUq0RFQvsYgk115LgcWxwk4Wv6vUfJ0tLBNnze1EQlKCb9vFE4f-9MEhTQPIbt_ySIrggi7QbdqecfZh_NegW-13inlYqx0y0buDWndyuYJSVCQpoErtYssfvhx5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NkipBHnT2dRiY79I5WWtLijdB8-UzrDFCQiJ2xpi9DTrKw2Z44DQ0tQEmwobRkYkGH0XXm0SLl-xJLyInY5I1j-j0D2kNqTPkCSXVF_jUWU4E-PGjv43tyQfarJ9dHUVYWf09I0xc44P2Wv-868roTl9EcMsG01_EzX_h_QW6v1KYrHGd5COccucD_3n0K2Jtj0-lu8ciD_ZBJES_GEwYTrswLuWhokNWCIPfgQoexLhVcVBCyk2-y40d29gMdfSd_6DSFDwYr-pu0VVWiYrH9Pim8z1jY_l7UfmQ20iMG5q6tainQ3I-LOuUR4xJGr-sFHaf3aB-YNQlfrYofTw4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vVXp7sRR3eYLTVs-JtklRrle7S7Jd2DuKFFYoYg98pm3g1bXrj9am7JQPQrmTuRJGe9v8odBkAiz6tu2ThHWRSu46hJCdMORcBA7e91nPtyC4mJb4jfuLRkGHQvCr9kiFxQn1xjySBLNjBin2lbPW-rEWKwU0Mq7sDxNUMoaXx3omx0yldCpoi4Ja8U6w1k6yXeZ5ao1ws9ivt11VqfRSJoUFJ8Lf7qSyOycts_oceRf4FFwUPMjKqoQ7Z0DmZAV-OXSWF-D1HZWWss8TVQGat7hT6g-VJFQfuUIFhrorkniF2DFbd0YvSg_WCgtc9YX7xq2-YJ1IxyvJ6a64gdzYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zv5zJEgzbRsclDT6sRhw33pKlWe4tRqphcxD4hFX7X8rtyvwEDC-Rhi68HLI0Ru2hm-ZFh4CkLiMjx7b3JeTw4QPb6zhccwZe0YcoMt7FmP30SgQ_hOXGkqq3m1GnkIf7liJvvz8iifrj3PHl5SkkyoBiD7PdRHSVaer6e59oHXAhx1Zs3xLz2wq4q4Kp4sdU1-WYwRPHAr9-SztmZbwFr4nOb55uXZ-d1WZBmLPocplXN43Q-kITRxezyOTrLoGO7H2TXgwZVJhKps4s5gBJEeMUa54cpLRxJLRwi79THiLsC7wgixOGt2BWKMUQw0zqZtnPO2UgFVy_4RiJv2ijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQRHoH4JsTYH_uSs9Kd-nyN-pMGy5dgy89j6wyRJ1nVwBP8mwNmpvvdypsWgrPmh7df6tXRl_iKNBMnfOTqi70RVrDFERuxw_0TAE30gyHa_gprIR5ao920nxhukJTz5Law6wSKPde4MF-Vi2jSBGdkeLUIL_SL5CqCwDuuWdlo3yaoUt1zajnjA8hfwkoQH4rbWUyi7VAmHryJbUm_sXe78piS3amT4eus_6EL1dAaMbrA97_wFWGz7iBSi-gygx6-lT4K7gxoGeRVz7w0CL3T6H5ktI_YnGDjGSIT6ifROqHRPk40DypB7oIIEiijgLSDRFBFgZwvURibEVce0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mEJ0GcAjXyvJa2I7bUjk4WH3T_sN00tVHqkk1q4jHHG5u5KY2dNyXSfqWA_mhEYorQGqkwzDYIIitBs7-fMcNkd4H5WFytCW1AxWd9tjzzUN48cRrNHRHZe4wAz961Vps4vaeesQOZrW-6wYZcZG6XYRXsbTFPjs7GbHSt0CgIQjfVGIj0CXpNSL2BclHjm_spF4O_Zotn6l6aITDehWHFEiyI22SZgXVR70zDL8M9xOaGqEIFNnTCvBCFIEyZBiKGz1gkRfbBQ01-RyCjVEjy3yNKRdJmKoR4pLfGoZDlxKyOEC4XZ9LLgqaWVqDTvx0W7_n22Vkix7NRyaceJxEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2hFcw8x_8ISM-st4Ymd6USTHWXmu9N28hwZJOnNPvBhmq-AkWZvC4CGevBscoWlZ67rK57YMgqi2lpNWRxaZlkUB_UrZx6GcG1Av5yDaUIoTGbYwTBgpoVJpNV6BLH4kPwcJtCvhqVlPbGWnhNlA4Jl1dgWlY4MuJgtGZHf4khrR6M2v3Rmvwym1R8kE_pr1R47NCD-4PScTWX6dFhkASIqAQKz57z8Vc05LEIgXwwjGI_zAhyClTxeDWdUMXU3ZmrMKyITwyTU5jrGr0Mpj172sQAif3nKLm13WTbbipJ6OKq70ESZHqAjPAhccGv60EEkM11sicqNie47GV3s3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=RyPBegTT3LuiiDbESVHhGdz3NTdHta9xIzDF8SHzlYn0ZRllq-mMJKD-vS-SqVoCpxMIdFJgT0xqBT16IxHHbZF39Alb8v0o9Ui0elMcBRGmGgRg5cvJe4L1k3q1nqAWRm6K93cueE572JkHB0K6jv9Jd74Os_TLwE9HEQy1d3zScHixN5O1z-V-BQzK0OCUj7UWhl_b0_Brjj8G8bgztvqluRLZA0A5UxRzqP7QQs2lhOhWEUP2M5teCytjTzFRQT3265yTpmJsFTSkU_1fMbpJ7MuPcrNeDTWeeGyB74Dm0DsUgBXJRdp617KDNG34H-m_-2X2m9_rDy_iL9rbpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=RyPBegTT3LuiiDbESVHhGdz3NTdHta9xIzDF8SHzlYn0ZRllq-mMJKD-vS-SqVoCpxMIdFJgT0xqBT16IxHHbZF39Alb8v0o9Ui0elMcBRGmGgRg5cvJe4L1k3q1nqAWRm6K93cueE572JkHB0K6jv9Jd74Os_TLwE9HEQy1d3zScHixN5O1z-V-BQzK0OCUj7UWhl_b0_Brjj8G8bgztvqluRLZA0A5UxRzqP7QQs2lhOhWEUP2M5teCytjTzFRQT3265yTpmJsFTSkU_1fMbpJ7MuPcrNeDTWeeGyB74Dm0DsUgBXJRdp617KDNG34H-m_-2X2m9_rDy_iL9rbpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاصل ۱۴۰۰ سال علوم اسلامی!
علی خامنه‌ای هم به صراحت در یک سخنرانی «اجنه» را متهم کرد که با سرویس‌های اطلاعاتی غربی علیه جمهوری اسلامی همکاری می‌کنند.
در زمان محاصره اصفهان
توسط ارتش محمود افغان،
روحانیون بلند پایه شیعه، به شاه صفوی وعده دادند که به زودی ارتشی از اجنه
به یاری ارتش امام زمان (ارتش صفویه)
خواهد آمد و شورش افغان‌ها را دفع خواهند کرد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5082">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=jpedjWfkW6p7axNq59xUAtrk0eP4IyAI-93JilZSDs2fnic2yxRLz7_NIiyssEd5NgzZnnfa5A2rwXqABXkVQi6Nh57Ti-YfwoJyZ6-89k2MDP946G9BQO4pO49d1k19lQRVesDMCQN-RsujRj6OJtxwExUTK34Hs7ZJV4wfH0dxWNcnBMiGMLeuRzDEF3F_Y-Wwuqx-D97gCCCxWJa4HrBj8ZD1FSD0wL4fTxuNUt8XYKjUHeldSAoOuzow4eowJw8AamBIf4OMuLZENyoiYk54EWO3HBYSXHRH_SpvqrhncM6JbjO5SvrwxaltNOeFuaegFwGdbVgClZ_Z0oC9ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=jpedjWfkW6p7axNq59xUAtrk0eP4IyAI-93JilZSDs2fnic2yxRLz7_NIiyssEd5NgzZnnfa5A2rwXqABXkVQi6Nh57Ti-YfwoJyZ6-89k2MDP946G9BQO4pO49d1k19lQRVesDMCQN-RsujRj6OJtxwExUTK34Hs7ZJV4wfH0dxWNcnBMiGMLeuRzDEF3F_Y-Wwuqx-D97gCCCxWJa4HrBj8ZD1FSD0wL4fTxuNUt8XYKjUHeldSAoOuzow4eowJw8AamBIf4OMuLZENyoiYk54EWO3HBYSXHRH_SpvqrhncM6JbjO5SvrwxaltNOeFuaegFwGdbVgClZ_Z0oC9ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=RMpPFr0Z9bTtrLmv3V_Sll0j82rePmiTs2ckkoBoCFzch19PxPEnjoFSAVRvwwVlr5F_MldRVBQ6_hbUgTCJuO0rpJtGZXzcnKiSRFwuJGrmdWhhPC2pLQUabkNAIHkvyXAKE9FWrHssymf87bocZXdARBMylnOMbVtCRwjcXtmA5gxpN4EZdf2aQR_8r8jocvIxi8ho6_30ifh9UkKpHiIFZmMVY8FbBm3PoDx0EFPTyznGXyR8yBb2hdH4WOoNR08wWBjgFeB2dOwcQJWr3xkEpNYIUME86vVka5x4GSfSkxzJ65gI5h13RvbHH11aiMHunjxPxi_xEHUzLSZLvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=RMpPFr0Z9bTtrLmv3V_Sll0j82rePmiTs2ckkoBoCFzch19PxPEnjoFSAVRvwwVlr5F_MldRVBQ6_hbUgTCJuO0rpJtGZXzcnKiSRFwuJGrmdWhhPC2pLQUabkNAIHkvyXAKE9FWrHssymf87bocZXdARBMylnOMbVtCRwjcXtmA5gxpN4EZdf2aQR_8r8jocvIxi8ho6_30ifh9UkKpHiIFZmMVY8FbBm3PoDx0EFPTyznGXyR8yBb2hdH4WOoNR08wWBjgFeB2dOwcQJWr3xkEpNYIUME86vVka5x4GSfSkxzJ65gI5h13RvbHH11aiMHunjxPxi_xEHUzLSZLvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1oDD1xHWkrLOwTu0_ch8AxLF-3crpU89Wm71hyUUoMSjgiPN4PtnkUKK-lz7c6U3GFmolQ9Z_rusc5roRH9imlx7nHp_YFe7iRBm88Lxdr1cL_zrCDDcvGZT34ttXA4ZJdo4kIJI_VHHsyLOz5Vuphrno947VCfc7zmiy1YBWG1RDrx-Yr5pry8-X8JMAVhEMhnKmdij_wo8v0o3DinydB6sTm8TbC0CaCgj_Ha693cBxExZ-tewgOWLjVinBmVLkKJ7mBe3pGJdhJcbN_hi3R_YcZ55TPrDpyIvMaoNCKV5q62imYjeZeCgB-cTX3S2PWod9pclndgHgEmaU8Bqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">قاآنی، رئیس سپاه قدس: «دستاوردهای ناوگان صمود ادامه دارد؛ این ناوگان چهره واقعی تمدن غرب و رژیم صهیونیستی را آشکار کرد و فلسطین را دوباره به کانون توجه جهان بازگرداند. »
🔺
یادآوری اینکه جمهوری اسلامی چگونه از موضوع فلسطین ارتزاق میکنه و درست به خاطر همین ارتزاق از موضوع فلسطینه، که مانع هر گونه صلح و سازشی میشه.
جمهوری اسلامی با راه‌اندازی گروه‌های تروریستی و جنگجویی چون حماس و جنبش جهاد اسلامی و… هر چند سال یکبار جنگی راه می‌اندازه، که منجر به تمرکز جهان به موضوع فلسطین بشه و اینگونه برای مبارزه خود با آمریکا و اسرائیل اصطلاحا مشروعیت بخره.
وقتی نگاه جهان به این نقطه متمرکز میشه، پیشنهاد صلح و گفتگو مطرح میشه، که خب دست نشاندگان ج‌ا صلح و سازش را «خیانت» معرفی می‌کنند و تنها راه را آزادی همه فلسطین معرفی می‌کنند.
و اینگونه جمهوری اسلامی از عوامل اصلی تشدید این بحران و عدم پایان این درگیری است، چون از آن ارتزاق می‌کند!
اگر جنگ و دشمنی نباشید، «مقاومتی» هم نخواهد بود! محور مقاومتی هم نخواهد بود! جمهوری اسلامی دیگر حرف و روایتی برای ارائه به دنیا نخواهد داشت!  تبدیل به یک رژیم عادی میشه! و این عادی شدن چیزی نیست که نظام ایدئولوژیک جمهوری اسلامی بخواد.
اینگونه فلسطین درگیر و قربانی جنگ‌های بی‌پایان جمهوری اسلامی شده.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=qIHGzEHOLtNYW6hMih9_yCmaL-JSjHtewt6LNNci8pFeo11g8grYzzX4So02ztKoLUhGgp8EZb0R-PVoIamUZl0le9GC082Z3ubNkssCQKCi2VdT1SLjM7rL72O9NN86kAdCTMXH4CwclSGqfDUzU3BOAMnRuhYwG1IcLAGvto7BKRrorCHpM7699l6UMHjJQF4KcvDSKL529rY_KNa1W7xhGK9CK2-p5foQH4kZ_hVFAwuFu21HoVO0LAkars2RkFWXR-wG9DDZJUkpKW2rENpqZuVlP1KuwC7Hh6NC7nU0ApnNH5Fb3v22sZVWjLjXQChi8ESBDsLZXK76Vpsg2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=qIHGzEHOLtNYW6hMih9_yCmaL-JSjHtewt6LNNci8pFeo11g8grYzzX4So02ztKoLUhGgp8EZb0R-PVoIamUZl0le9GC082Z3ubNkssCQKCi2VdT1SLjM7rL72O9NN86kAdCTMXH4CwclSGqfDUzU3BOAMnRuhYwG1IcLAGvto7BKRrorCHpM7699l6UMHjJQF4KcvDSKL529rY_KNa1W7xhGK9CK2-p5foQH4kZ_hVFAwuFu21HoVO0LAkars2RkFWXR-wG9DDZJUkpKW2rENpqZuVlP1KuwC7Hh6NC7nU0ApnNH5Fb3v22sZVWjLjXQChi8ESBDsLZXK76Vpsg2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=bmGhbP8BqUPJXy5uWdrpgUGYueYrZPmjvwZSzom_jPQEOn1Hg2CsrpRhX7BBZsGOcrsbPtARd34w4y8yrnYHUQ-s6fDZ2F0_rE3Mo1YV4pACc9JGcSoACD0FpCf17PepJEN9MzedNJFiFkpZT6lgIjajlXvAl3YZjMklJl-zobVcz1q8sLYC8AmPpj1OG7V1ANR0p_CHdoLKnfEv9bXwWrLtnuPrTM5cdwK11fcyBKKmCe8GgC_INUjolaSoPf9CLKIjeJsrvkU3_7wpepQQdvdnq3NMHZdsmd8SYIi43fHuSh7c8n8TZFlNo2UryV3z9tafd2P4Ve1su63cxp30Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=bmGhbP8BqUPJXy5uWdrpgUGYueYrZPmjvwZSzom_jPQEOn1Hg2CsrpRhX7BBZsGOcrsbPtARd34w4y8yrnYHUQ-s6fDZ2F0_rE3Mo1YV4pACc9JGcSoACD0FpCf17PepJEN9MzedNJFiFkpZT6lgIjajlXvAl3YZjMklJl-zobVcz1q8sLYC8AmPpj1OG7V1ANR0p_CHdoLKnfEv9bXwWrLtnuPrTM5cdwK11fcyBKKmCe8GgC_INUjolaSoPf9CLKIjeJsrvkU3_7wpepQQdvdnq3NMHZdsmd8SYIi43fHuSh7c8n8TZFlNo2UryV3z9tafd2P4Ve1su63cxp30Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmzfhmlRKuwZbcGJ0S76y4QriQ2REnOr-inbQwMChebjNMbvEI7OgNindH4LF_m_gzV-863Ohks9PmkZuhBkldxcpswzQ6UqYIB-1QW8yhq_ke6QRFI3slYt4yPxgsoXWcYP7_dD14zlJoQoWTYdtPulyw_FSi8Htod-FqgIXsFQkAe2Pvzo0fiu4hUGBfvkgHgUUM-4ivI90t70JQAHM5QKuF7ZhBvHe5nEVt9r6Kk_ht_k9dj_Nuz1CU3dQ7WE_KkgF462LoQul6hx6cX3H1_KjBD02h61dp9KXkahcLkgZiRZ4Q0WGKMogOnboWkStowbkQCLR1lONnpjKN25pA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/himbo_O7hnxcdoPvog6W_giakOXOKsw4xbfCjinDVGFfBjBYgXl7krrZSHrt8ITdxOTQmxr8iG61CXsuIaRqrmCUkSQSAvgsqcF6C3ofUj4EbeGc-qNlJQSWK6cKp1JiKgAtXaWTtu_-YuXT5IbJhoTH-OdlOyPQuabdGxM7lqWAl8NNDc7V-FosqVEucfZ7PrnCRpOYXGsyP3p_bdUT18pslqqvkizP3CZ-TYjvaKSe__xacvKUMMTZ1gRb2PPTch8uyz9PmbFAl0hxaIzQftjP33Ivq7-xIgss5v7F1_ZaOhMj5yc_9oUgmO0mCNMCujR6MYfhnIspcxlrll0fZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFqy1xJN7wpWvtIqy0Cw1PexqOXsZtGgnxLyQcvruaWDhfox3JItM-vza2JrhusbsPSBWeaHEqfaDUBwOs2PsZt-zncX4_eDkk3XCqcZvEgD0uZGZc-V_ZVVZ0R36Lze2bNCZLDzLBZj0K2LxbgdIVX4xyAKrLmYlwDOtNCF5o4DPSYEsccJwDGGPVW_hxgoy5nHgOj63ue-AvtFwc2nmjct8_uHMlfW3GkyH7PyId51CDjKJujGzuuUJzQJWu_7VC6DNDkeKhs3esHO84JHK-TBnWFzxShx4qO6mlmT6q8Oi6HDTHk_B9Z_aydLkfWpRU8t3uoeOH5Gf_pYGVmMrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUChdeQm4diKYHPbOOyGP5g-MuULnxRw3GsmZ409_HfSHvzrEUELWBBdnU7KRwM6dhlzeDCu0vG1IttjRg0a63fwsFW1XuTHiL-gTx41qFMBRNgmMRYob5h2gqMXM9v5gslkhLrs47eK6gkM7h87T0Hl-jacfvqgQ_Up2Xw-MgGLbRMT1d7HgRhLwYyaQBNu92RMedXdE1X-rnV0vcwDIZv1_4-MasdlBEzD97cjfC5N5cJ39-niSIL-e0SDWa51AL6FMgppO41-3l_RREAaGS8kPRULE5lcwvbkL9IhUM7saPCHNdxGvjgpY_T_EXrkUltyYwOwSgEtMvlA8Ui0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDWuhgaOXdOV1_JGKaOzP2JiyTji0bQwwDoxFPkTv8nuWSEsJj8VpUuPgG3iQdZqNBylwQeYOOU1NFBLfRZMtnZUbhe7JdWnKL3KUIdCN1TWMzAR9AfwvL--yiTsP4OFuFIcsfa73T3tJHTONeb4YpYikU6KmgA6ou281PvfVRfmSOQ_yUZnhopb08ghhnl_AtAJOChdVUtdX4vEuJ1O3sGHEAE-SO_q_38aT6m_XnAKceZAXsNS2IUjhkqSu5HmpLXfzrlhDBw8hRgE3HO9lZACqbUUIENIjdbCDR2Zar-pi27rKqAJEgOxp-hcQVCY8nKxRdurBc5LlwL9y2C94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gW3he3l2kXXQ17Bk2wTyaRceE5UZBLawfqNtn7r_Ep8L1xQu_AI4fhxQW6li-Zjk3lyTwJfICCaSvgOZgrXvG_GJPc2_iLSUhi98gHFGeKxn25Mo_7_UkodOFHHd79yUr5tBWYZgSGihgJui9IxygY7Q3R_io7BX2AZxGac-f2oqtxR0gkwyybFHS8asMTQQVgpFX2OeZpPAJ9pCv7hu-vOVYhtd2rEASHvkHEgsINi6hiRVJDLpstceOcES3lIS-VphxztbJ90ODGZ2-Jy05TQYrRvZZmdqiGdkKhLUflOtsDVATQPvK0MvS8q7vLbz1AGdBY4JzcamitPkzKChlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/boB_-MXY8oUebLh8ScfeBtc1JP1qI9f153ec6timu-iaqQGR2UlsJbB-bqZPS3Cskl3DpRXpyUNEC2u1VZzFbl6clkaNY1iw11UrMu4H0b43-tnNjzL4GJltZ3CVcBEduxD3OtPEpaJFxyPI3VjAre3DrwmJzoLF-Bmu3VLtdds7CdsTsJeyBoHgbjsa_gPNn88QdNfl4UYwDBJ4Dmzt9APM47BmszK7wv4s0lnhFaumh4JXw234bw7e7kNmqYE-xQNneefqBhirrm-LaC9tsMEpEyhA-4APf1Haoq2NXnhNknNm0NhMkVEGJTbVGGhnR8hvDCNeEUI26Bb73mPU8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=GhAwaoB86AfMSoPbHFZApvp5Q73YDdD9extom0lNL8QUPcDk3Jy472FoJqdl_Yj5GqJ0aYCu2DV0oal28z5Qf-Lh-cDs6upjkPWagxy9_vjpNwwOMgRmb6PEey10NjSUWRXdX-DfzjGeyXZoSJx24ZpZyPfw2OQr38hopP5vaqEaPAHcQMi-jvK7o4irBv1L-kl5KYVOXr8Cbs0rHJsoE8ZUeQrhkmtWjHz5s-YlFGzj-4ifoTnsr04lpTQc0YEI-kwItWXXS9yEjUypjc-8eVrrTUziPaBtclE897263r0on6OMBmCC1tqrPmPxTVDsaiWPAVFIE3zx0vH732RFnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=GhAwaoB86AfMSoPbHFZApvp5Q73YDdD9extom0lNL8QUPcDk3Jy472FoJqdl_Yj5GqJ0aYCu2DV0oal28z5Qf-Lh-cDs6upjkPWagxy9_vjpNwwOMgRmb6PEey10NjSUWRXdX-DfzjGeyXZoSJx24ZpZyPfw2OQr38hopP5vaqEaPAHcQMi-jvK7o4irBv1L-kl5KYVOXr8Cbs0rHJsoE8ZUeQrhkmtWjHz5s-YlFGzj-4ifoTnsr04lpTQc0YEI-kwItWXXS9yEjUypjc-8eVrrTUziPaBtclE897263r0on6OMBmCC1tqrPmPxTVDsaiWPAVFIE3zx0vH732RFnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPncK7p5oIKpaNDPJeGUXGVsiH4YlGl7LBPBZr1JwbK3DPOXIheUgGBHmW8Llbj7DgG1G8DHPBTON3JYH43-vUacJ3m9mfEBV9MjhpUr8tR0tcZXUp_QB8hlkDDut6OUdFT5C1dqgm6uCaJyR6neONg9ZXwGCROjr_iTsXioq7zv5lPrX3z57PjnA7Vwb-9TJz0lYYDLgCtUFPRooUw45BlfZEZitasE-R0TQT5gFYJzJv6grGlT8LlAY7hpaZrPi2LJv_18-3gbMVWKIQ1_MQn1tYDT3FbpZgoVawdlptdbzDVAYKV3B8_nCdgjKKED_tCBoJqHFxn99PLsVrUI-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuBiwn3DnU0X8HFwTDaVc8r7A699sZRdMxKt6vUN0g32rHCUn6cSJI3khQ7OZBgsvtHOAzBcxpszmdPkvR3UveFy9xG5UYRBIJcOiJiCGX2QWgqbeJgR1aeqgtxFxDuA4dlo8H8E7A76u_aK8TpxFgyxABX5CZvONIAeyhrlSyvS6ncSy-JsgM28rEhyD-LUg0uCExTQg3gGfnAKwdDiVSh06xAwWXCWEmidVubUkZxsC2lPUpzfeVdduxSdKaQnoRxxrtMdYvP5iMa_yo6Nb-7LEXgmU6q7NI2zC6jPUsZDzIl8FkRQSSdXLvkgxXWXOH1tyKYFG700ntWgcn-qtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxiRPblS1xG0auHPfX8-cBRP4PUxa01amnciC8zXGa6VkR3wB4DEUnBiQ2jfJo8VG4RTHbzhmfbt6NonFPU2hwtL0jc5dEZ0QTF7Z8EVF1P-sM__N8qqbHbKZjqmb0N1q4OpkI_2dMTS3l2pK745bcqGE0P00HUVchN_UR-7M0KhSOWv_IhUryQz57-xJa729CxHqKy0yIrGRRrXOapYW10qCSYNRUkygM4RJTZN5IalaNd1aOAkOspwUxhHSXXA6lqo7yGJun5wiY9nVpZLyM4lnPlIepVSvPFx7Vh_mW1vq58PZfSZ3W-lBE2iepRrIHzcWIDmkCfZ3t2W_Y7v4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY4kVXY4MoUBcLhrtspeepJPU14XsFK29esYKWNsZPZnhVO5FBX6gcPw75i7TWtCWW0fk2YTnPxA5joJlQv-oG2aVMNaSpektdGSw-kccScrxITD7D8E-zKsanR3O1_1_UCscX1omh5j8LheSTSWqmcNbFpL9bPMw-8SQ9UJKnJBTvnokThbYoW25RLFyDQ72hU9f7LW8Ow78qElGIolZvH6Bp2qVPBQIOjHI0sxprfwOPLO1PNgbIOma7yx7DXr6JKdG68dTXZhh_RZgu-ZSDJ84bjwNzmer7B5MBd8jAkGtGVcwX-DfLhrUKN8ofxKnqacdIdwQsiRIsEJlBt9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=PjfkpqcFJuyquuJq4fsGjZwKemVN5oSAIUPflLmZwBk0XmtZ0sp94pradIrzSEmvsXhUxT8-A_pUTgm8klE8jsv2glQJe4oR-QPaPn0OOxh6Jg2hjDL1voGzwY3mo_MuZqcuegI2Dzprbl4QxIb7GhmlEB-ZbOvPPrM0W0jJc1kXNBJCS9DE3ne4FNN0HqDpw67tSiPp0QR1kkPFv5BkhS23478ZCKSV3xMk8voxWmVjm_Xguqisj8cX8AoLWmQI3N3T-wLS_uC-bF_A7Z4fEpvAm2S7u7IbbdZApZ-S1uFKJQyexcmC5IJaR_wyrx70AW6AfjLkdX4oitHpK1wCcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=PjfkpqcFJuyquuJq4fsGjZwKemVN5oSAIUPflLmZwBk0XmtZ0sp94pradIrzSEmvsXhUxT8-A_pUTgm8klE8jsv2glQJe4oR-QPaPn0OOxh6Jg2hjDL1voGzwY3mo_MuZqcuegI2Dzprbl4QxIb7GhmlEB-ZbOvPPrM0W0jJc1kXNBJCS9DE3ne4FNN0HqDpw67tSiPp0QR1kkPFv5BkhS23478ZCKSV3xMk8voxWmVjm_Xguqisj8cX8AoLWmQI3N3T-wLS_uC-bF_A7Z4fEpvAm2S7u7IbbdZApZ-S1uFKJQyexcmC5IJaR_wyrx70AW6AfjLkdX4oitHpK1wCcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف و البته خود علی خامنه‌ای
گفته بودن : شهرک‌نشینان اسرائیل «شهروند عادی» و «غیر نظامی» نیستن!
حالا حکایت خودشونه!
که زیر دوشکا و خودروهای نظامی ویژه سرکوب مردم ایران، جشن و عروسی میگیرن!
اینها سلاح های مبارزه با آمریکا و اسرائیل
نبود و نیست! اینها سلاح و خودروی سرکوب
شهروندان معترض بود!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5054" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HW8qV7SySoMOFcj3u4XMOFNq_DGRAxThomM1yOZWMDpabTzleZpUowyg08WVuizIltvdarzvTnwVNuVipWDTnvpb4aIp6FHvdxyxn5czXdmUpl2mydIK4cDTOgWYIh0L7t4V8sIBH2omW_bKAoE5VHKIfnOheg0tsRjiKwCQ7OZ2WoPNRXNZ31dAMYJKsKf5lt6QoebKCk95rvwE7Ic8yOz7znw6Q0jnUDqX15FKUITiNvm6tp8RHuc3CbE-nxxHEAdeqJbWkAcPJKiwfaiNHq0mzjmS47DZde_7JDvPikrUYIvLpEq-Tq-d0qVvBhLYaFAAlj82JcQBUXPefaDhMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcEC9rJmz1pxY7SxFooLg00ghi10SSyFvvJIszDnFD1DG7bxok7pQrQOvj-WWGb2OisoniCIrkK70XjP21_bnBEQrOCyZ3W6PGU9WnyouZ4wZPZGtru3SyJquYiu38ojutdUK8s5HJobYgHxdSJd0SGWI0QfMheqeU0cj9CsTCiaEU6zN5tFObek7_p4BzkQal_ZPruaSSBXuduH8WhAePJUJu6ctI3WDbBHEy0pduzWYXTnveBunY2IugJwShUlT4oafKtZz4t9ZmKNfDZLZQLkRjdYyDj7eu1fbq9Z4pSvgFviPaGou8QcKooxdos6DkQ5beOuQ1eSY_yfT8zoxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T43zg-fp3TnX4aPIPMfcBmBtPVfkav-CDSZhFPnR27Adw3N9Mfwn80cDH0fZutlN0Fs4DBMohHz7-wzJul3_odRFMbtTZOXZMzcV3rm5GoHBVg7PJUkxQhAflusDTR1jFCp1lJCfqUE6p4remHr1RWDjQXf6o5_Ra0wBoSGjFYLIZ9OHviWnFHnTfCzXx3V5tIVp2lAKOSNlrzUphmj2sLsWF3Js3frKlXO7LUDMNPrjK93cRl5r6c6ngql_bEd346S8t15h_7m5R8h_ZmVfDxM4G4huqRgTKe25VWClaYX1Swx5nbjcpLkG3LPnLCsnKBZFwJMio8LDqvQpiZ33pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SidB21RN-GlnmU1CGSn0hdN1F1EU1XNQa72cPsNOlniSwvSNuhfIe_OBHTjVjJpBp2gqMw9BSp_rDwclFSEmLFhZvwVkQoXnj1CqIDJjQiZDAq040xW6nzJLO8o3QuL05hKt71UMG8VDD-5WOxvP5V2X_TB_KiW1ujIR0oSYPpZsIB_OvwaDTRFAet2DlteHXmNpUI8UgEpbAXcWBHnr14Gvk7b-y0bHInSrzN51Iw9GmmUpdN_1ALaEEiMDkyyC8eDwi1Z4bbslhHdS0KgEN6wSFoX7fzBzoBlgXXTG9j_bbAZNyR749RXNlecdWoHx88-x-pKWZSfIZtHlSr8JXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohbV9qVX1rxfI0NVnHdie27YMBNa5FD0An-yPj7sUQZ5k5v6b9zmqp7JXcVaVno0Aij07BqmFlk85HbR9Z5i8Apcl9F729R6CSlAQVmR5HaXVi8XSqyncWA6Nr5Ooz6eCW1LGUGSmAU3gzhwHLNc1hlt3qzIyc2BwmegIPiXFQanjPtXdDn2eEU1tkLZG82-dszZwUUX7unv5hhxvksUu2TrcW89aHxF5QucZl-BBteoQsWcB4tpTbvdTZjIN2FIaz-dhmSo8e_q1Z4VJ0V8fHp44iBPrGV0ArigQZLxw1b2dY3rPtlAI7zrBRIV7BlFtB0mg750PcLs4yoB8D-zAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=T3kFZrJkhKa6oNDY63jcRn1PZY_B1BxKnLoIqEg87Y85_pfALpsyOvEGiO4GPPcGJO0dwv5VmxOuWdZsFZdJ3HYyMMwO61Z_q0ovcWe6RJ69Q-AQudSYLx0go3r4PareGGIjUcWBpPI17RQmlSO_lHWJUks4ZoarTxK5x_sQAo2FdeDmpdJkQA7o_EZlk8Feib1vkjctFUiGe1AFHweaBiSmOdWMKaBKMvkI2RKGvkOrsTjp6TWkEKHok13r_sf5knh8wKpI3nV0KN6Lyj9McjYpDBzQ4qbiXzh1vw-OtV7rT-vwexVIUUBd6gBAhedFoinA0ZHOZVPNvpLY2IBQgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=T3kFZrJkhKa6oNDY63jcRn1PZY_B1BxKnLoIqEg87Y85_pfALpsyOvEGiO4GPPcGJO0dwv5VmxOuWdZsFZdJ3HYyMMwO61Z_q0ovcWe6RJ69Q-AQudSYLx0go3r4PareGGIjUcWBpPI17RQmlSO_lHWJUks4ZoarTxK5x_sQAo2FdeDmpdJkQA7o_EZlk8Feib1vkjctFUiGe1AFHweaBiSmOdWMKaBKMvkI2RKGvkOrsTjp6TWkEKHok13r_sf5knh8wKpI3nV0KN6Lyj9McjYpDBzQ4qbiXzh1vw-OtV7rT-vwexVIUUBd6gBAhedFoinA0ZHOZVPNvpLY2IBQgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5046" target="_blank">📅 23:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ :  از طرف امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس امارات متحده عربی، محمد بن زاید آل نهیان، درخواست شده که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازیم.
آن‌ها اعلام کردند که مذاکرات جدی در حال انجام است و به نظر آن‌ها، به عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همه کشورهای خاورمیانه و فراتر از آن، بسیار قابل قبول خواهد بود.
این توافق مهم‌ترین بخشش این است که
ایران هرگز سلاح هسته‌ای نخواهد داشت!
با احترامی که برای این رهبران قائل هستم، به وزیر جنگ، پیت هگسث، رئیس ستاد مشترک ارتش، ژنرال دنیل کین، و نیروهای مسلح ایالات متحده دستور دادم که حمله برنامه‌ریزی‌شده فردا به ایران انجام نشود.
اما همزمان به آن‌ها دستور دادم که برای انجام یک حمله تمام‌عیار و گسترده به ایران، در هر لحظه‌ای که لازم باشد، کاملاً آماده باشند، در صورتی که توافقی قابل قبول حاصل نشود.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5045" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=MEPIRBJtz27Hg0DQ6mV3R7A_p93GDkVaQetHwrPJlAl19KIU45OfvpB2nLRs8MJNaArjOetqFyQZUumbEBKjDhkdNqCMl9CgUk1qvI_VC872oagMeORSaN145mfZgJm9fdTMNi3oj2DaBhHnccMo1Rtk7KyznIRnWUf4B6UrmyBiZsvxZ7eMFm2NZO_TrViho3DRmuiANuJ6pf92P_-at5LTquSBqX9m9FCmSWtwjARMmRfSbTMQP4mtlvBJIDdoIADMkI4ngu8fZBfNBIyn38hxYeAbntTF1BiyrJmDLmwGCSLQdP01IFW_igjmZHgthyM--lNdQvQuKX-BRQ4RBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=MEPIRBJtz27Hg0DQ6mV3R7A_p93GDkVaQetHwrPJlAl19KIU45OfvpB2nLRs8MJNaArjOetqFyQZUumbEBKjDhkdNqCMl9CgUk1qvI_VC872oagMeORSaN145mfZgJm9fdTMNi3oj2DaBhHnccMo1Rtk7KyznIRnWUf4B6UrmyBiZsvxZ7eMFm2NZO_TrViho3DRmuiANuJ6pf92P_-at5LTquSBqX9m9FCmSWtwjARMmRfSbTMQP4mtlvBJIDdoIADMkI4ngu8fZBfNBIyn38hxYeAbntTF1BiyrJmDLmwGCSLQdP01IFW_igjmZHgthyM--lNdQvQuKX-BRQ4RBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmHfM6mGX0x3edJw2WhDsww_ODWpFH_4WKEGBYhix_PQhqO0GmwFs_WLBZtfArLsd_mh5ANe189CIKXhht9hsCQxL7uYtDwnCfzd0SYvIrIJseH6gIeioPQ9cMkhCUCqYWfqMAhfDjiMuMaF6-QYJ8bCisKoHMu-8-vEGI7LCxEgOywIOUOvXRJTRP4DYU09v019YTuh9vtHRFHYEGlFcUNyFAivI-YqbEUdsOFJCXj1UJONZHmuNyH-ndvYuLxGDwPjSOQaKNEQxIj17HBTCmVreZCCieKtyBmomS_QwvNM8L4xVMmSbKEsR3VFFIPG28gwVVuHbjhHJHKdYRpTzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_1XMUfNu5GmEG5xlyo00F66Eu_Lp-f7gu2u-PV0y7f0Hd5f212B7IPieKxchuxkbADWvSDgjRf7_BepKQDzL0i6D8mxrrBNYllYgbNT1ZMV1RXcRVBkHhnXTxhtfDdN0Ndpz2c1SU0190veFcGdu9Ywpo4Qs_DMD70WLgT_vQxuIYY6AMO9bFBrp4jlKIHcXqP0wYuuATfK2L_0cjUReKp3yNtrJ-JSpBY7R0QLorJvmnB83Qz-4vFTSOz_GgpQoRyNsoIaJtg1OnflhEtrVN6VuPZfTNeWwg09SQTCwZd7fbnsTLMnNBM-qgZvbVmWnG-9jn5q_YXreBiuAq0MwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
