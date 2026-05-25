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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 18:07:08</div>
<hr>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5FydOHjNuTiD-8dDiS1igzC5k5pshIFfTHl2n5mgU8S3kZRWMsQhY8C92MOm9ZmgRZUCiIIY0qq-Ai28TQgY7ccJf3UxEW4q4KRqi1X5soa86tpqdhGSXe4yvtZWBR2kHgyovliJo5ik_F3hHxnsZKqMxOkg5ZCwN3HCN0c1kh4ZT2cEcGxVLgnqVTlmQJTvU3GIcMXXcxnsfsiWOvgvxhmJ_AfIAgwOVVOVEY0gWnhAKMrXmfkHv5Isef_oXexWsF3MFT19WBei4CEEx2nIoPEASKYs5QaNSFA2YjdGoVT5qRbrOFhmlU2ceTHLLnnpGwAx9FV1ngjjujeX4d4HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXI-NPoNnSo9x-x0kN-Lxb8ulmgsGwDuFLiF_4idoyKe7rPr0h0CWp2H9tcE_sqvgO0RbIHn7LzIJiZlcnk0SQfmFc932I9baWy-q0dIIbn-kkGW8TlZI1d8gGapvgupmbTZ0PabY3qRwNbMIfLGPU8AYYMJH7DhFCG57ffyM5XTQ-_X6Kd4Go1cUZoT3Ug9lIXTXO1o5rXSu0n5XIziL4r21G5fsAy7hkZSKMTAjU4AcXmv-lWwmnOnu10LeOlhPMnnb9hDPEK6DwBoufIzLwtWywO_V3uFLitrBj4mpOZ56TWzn7FjdiCY-jjt5hIctkgiCJyUQ527KB14Njpc4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bibQA0SdPsLkMTfFiXy-Kz22QK0x5u2KtR-iA3fr5nCpCrtiOUHkAfnszh5R-yAVGWQk14rNB9YAbC-1ius26cP30lE_BVpzMWp9zyojL3Fdyt8bAtUWqaVfw6w05d7kJ8Fl3Nv0GVHZijLCeuAWCk6w2rY8vTYT-Sll99VE-xviYtY2VF7ITuLZfBbceREGRE8eCzkOQZRuayipMuB4WjRhIeZboieFItkCIGuZS3E69_8CLFXzEGfxfve65AzSNzyQrLw7VBu57Rs7QSVHrkk91Z8EjeXcBVCxOKUlZEC9MCZiLdnsBbVh1QM_sRRz3ILzCUJx9mkFAyrem3OewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKSfN2Zg-AmGTFnG0-RycqqnG_0s13YgZlhjpjshJdx625coHJ19PbhPidED3Ex5W9OmS7t5zPX_haK-4Bn-uEh4mJF7nDWVHp5N6gO3Gpa7YAqjzLMjX9deFkdfeM0Q62nEG8TH1Z1QtRz-YkytKOOe-GtGyqpTWagZ5nOwzH892_NqnQ6PiRD-SsllqDacij-J-AUdpN9_-onT4mrEbBEWdnfyjqGiJjirdoYtbAFD0yROIkhZ0G1IFOdJhl1xkI_4vVwrACOWoGosmfXg_J9a0whna6h1m2v8gdWUjhmvAJQ7m3Qqa29aBMoFkRXrbCUzBDXp9QP-K0kUlAcrfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgHw3jnMplh2A0YLwmT9NNnlzdkR-hWqAcGYdxIAx22Q_U9GE8gLwQNbzl9w6znHD4W1L7C-elCMwIlKmp9-5UF9_gmaFU137KA7VgokiZInB160W7fUaTKExtNP5dcSOmu7d4r74fSe2iLsUOshi8wF89bE-B2v79XmQ_zK2oPvB80ssyqZjzPGgkCj6-pVEnnMjCMmHB8iRGr33xdSAxHliYCtiwZeVb6VTLl3_kwW5C-J4QGjBYlP-vEPf0Lr86St9WFLKltLlx6cvmiqm2lEc-J-Gnb0Gs-JPYGBKtQagRDPLd0ODQ145-0-WceCEcng_j-J7-dyYK5I9bdTxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTggv82Xj7n9BKqChiY-2HTQcEghicT4i_XaJPzPIB6kN87amg5KKIZHkBl_A52nNq8oU_vt5rksdzyza9b7pu6BTdqHMOUJHqirEyNkUU2_YCxInAjHaciMuIZCqq93dNU9odu6K2GJYc_siPLOaE94YbTEQIfvluvkMkcOPUis-LC7ZaT3IH0jl4N2IS9eP9yqt7tkpG5ObnHJ4Ev-Dq-H8-PaypvrpHiUh72Y3VfbyOIu162Lk_zeuDcFMkVc3FgadlQdNhTLzUrIsQCDiB5PUrKfZ9qs1uMmA_6T0qeNi9i03ZhAM9iAL7aGcGFolZpvahBiC5IYNhV_aXvo4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPzHp8Z0KN8_EL2-kt9840TwMr2KEYTifO003FuXWtnW-XTnFYVbGlSU_pwcO6twscO8_0TaI7mZrWyA5_J7wsx_vqCgzBNjRY6GmVGGbDtwRU-LKBGa1IX0Zr39kEdCUlsySOQ_C8GZvmXinWLI0e4JARxPvmEDhJmh7FVeDcuYCk9neM5xrg0LyY0kUYtMM95wwQINGTerwTvqRTts2w9A0od1OWa5vqPaQDsvSYIopmuokKod9CwaLgW4KLzDobbM3b9fF5khfwE8I1IgZFBAYEIGZvVkFxQjZBW_cA3sTrY5wJ_rHUWxMP4nWEYX_e602bSZHISmEpI7F7JQ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9bol9s_eg1qAgy1aYVJN6gWna7e_9JbBpDKWw5NBHfu7Ue-mZacZcSFa0NkLXWtAYRd-ntVAPXbqk2UO4q6S1F58lkPLimL_jBKS3MDcWS4KpmBkPoXUXUoFI6ensJXFZjCeEgUCnY5vbh3_uwF765-mATXUrvlfZHn4YbXBCQKas4oELaNZ0qdRt3iip3p3V1_bNd161xIYs7GDuckVF-AWQq2JUFb-zrkusLiKgot3G_jWtQ2t8a7qFMde2Ruk84-SlHgaat-8k9VV14bHWWOLQLga9vxrDUUnLOEV7SyKVZXx0YaTOysW-jKv5hD34N2QIOHnaqVURrDRrXxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6hRGDZ-9nzJMqdmfMLv3S32vjpL5GyFB4jl1Cp2NzaMKx3Kpvfntmvj4EAguwRRjnCQLezHViDaBUmiR-1zd0uZ2CppthvkWKm5fBG6R-6aUpykw5oZNZazu5D94WnVWz5kBUhsWn82vYKg9IIjjL6j1F59ovEqxdSXvyD7_EdP4ndwRcAsKYMHc1Wk4pjCAQM7nOetPBCs5zVtifSHHeh82Ip5G9PFWL8bHBBY01O6FN2po0KA_2jpQoN1N1f0OxshQmU2WEiFstqyp0Qnm2p0oYMTqSAgUi4W4AZesmmI5gK9Vp_30ZXio4_DuGXAEeNMBpXhP1fcPNGl8dHCkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hY1YNpfd3uh-tbs_jwW6GVolsFMIVegPhNFMDPQQgi3jeroND5_2c18Lykj39Cxq8VdZeNiyC96RDVeZfrNlbRC2f13pbLpmQjrHaV8bEN08h4mIj0gE2a_T6FyD9Vpv1XQagFYlWJSgRR_x-W6Pmkj7eNwUPFvCdn81vvZKLGMGdOVuPBt4dlWX_Z-7WR3OSX5z_-yW1DV5375sF_25XTMlGWT9XagKBsXkkujwhjFEE5NbuALd5xO4ec8E4JIGr_1JRZiLKoCurP70J5AyIZvWyjT8W_zUUrHSqupmdKA4Mfl9DeSSSZyZqcTDRCGi6IPsAHxHkTTy_KCjjWpCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-8LIfY-BPFnVNSC3dJ3qGvGI6BkQ2zY5xDtvaf2MQcUKBliXcd8-sxv9vphsPMHDo4uYYCWHJaxlE2e5NdwR8-nkeSwAL3NWw4HDjZcwjKTZGyCaFp8uBGRfC3E1MVJ2Cpyk7EkISl5yByL5sfQYZ3EhdaezfivkWbZ7n5M2enN7-HqM2167eRs01tEWel4XDMyoatPWzbdbNOnN3qe9YsSu8-JTV8q1artktqIsDDOK3MHfjzgagsQ9bLUxPeQEwO0dque30MVwSoeFltZTMVniaz3mtdM0kGrNRVwJHBHPq_b8e7BO0frFPekIuBHhLQ5pfWUZQb3jOeb-pxAcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3PFLyLBl8kwbcR5vMrx5RiJtturoX7C6x0X4Mcqqlca1AEaGj_meX3F5qpF5WM5d4QJrGRcarouC9igHCPrq2V8o6Bg_D3LLnGCctWMlL5FOy3m55mm71KkzCF86CkLfQxBZgzFSz3j5x2BltgPMjAR9V_NovcV74BZSXfnM-fQGPPHNDL01jXwdF0ZIyhbdXlPsajdCuj0yTRoh-5z2yNttqbgK97iDzMR3abLLu00VqwC_C17s8U2-EmkQZGL014u3swgHsHz6NQAf_snLFr663NegUzeFhCjbVhp-WFpSQAtzwY-YZ6LdKhQDHRdjBHGeMpNKNj0Da9ExsHAgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZIlkzB4QdYg7aklA4qUBkLUMb5121ZJcq2D7hUvAY1Pzu-PGBHzW7OvqkjRbdmH_m50feXvS2jIT4VIf824k-VBqmoa1-HR_F-EiLmmWv4q_o7AJnOaNAEO6Lnhs1x_DPVMBdfOh7TLhavEPRdb0-z7JMzJOReABkG5fcjt8Ixr2YCZYsF-NFqy0DQ_pFVQ1p5IqSbqpPYRUeTeDj_ScwHnOllmWPFdL7YiFqaXHLHyoJzzpANNx8WfrS5ffXPMs8BDvkhGCeJ4eA4KKC9YRX_1Azi05-y_3Np-JyrZsEaBhbHEsOS_Wm2jtSX1ci0Z9O31xuJYUawzuhr4sMtdkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXNReTU0k_aWUR4LeLQjNq69R93lI9Nb712c9mqjXkqsDXbqFniHeenglyQ0MlRweDz2RlvWojheshcGil7Md_z0f-z-6DImfeWv-N291SiGCxG6kb6a42Xc-D3F19Xpj6tUnCau-MaIa7T-ySSG9oWVTbtHombZ029zS5E2SouolAlXqJWJ-5GxU8L6gwOCi79BthidJmjSvyLVllp8Is9PFPEMCxBjejCkpc_emBP-im4PLmnZdUQ7CPD6frkYUsnbKnN51BUhupUu9MkGrylnl6z0t_AqprcNcIOCv2zfFLr0dk835V7WmQimsx2yx42HZQIFurVzGeUdFXID8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL9pMsnbXQpG2PSaHRP-nFG5ggTZtv6_kLpyrtNsoXANzQfd2MlfgEvNhaTgsaaQMaehN_BolItHdT4GNJDS-KTpUuDO4nO7tf8cEdTTrTikFcppuFtUzbyQMaGg2n17rgyZD10MlilmfvJC9aFg9LUNwhM3lEYZcwO0mqC8bKpIKkzr0xfE5mIIDAes9pimDyZN2_S59eF-EENWLXu9IZ0bZ59tLyDzYTYdopNyw60jjruXUVIRCpd2ZkSAZaBmlk18lybvjbFeqIeWR9iMgJ163RejMDJmMubOsTuBdMreaHYBRJEsA3NO--u3kLxKuD8okPAm3MOZG8OlFR4j2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poCyvIpuN4hirrj-w4gQraeuVxHDVV6Zq6nhm8dK_ecvD9rewGuOB9-2QwXpUnaqJNKaZ8yEPZLi4RinFX0ten85_FQBCyfg1LNrzYTvcslunDJQniQBVGP1B7ugl7ge9RUjknG0pl6gn78PmantZ_OaO5SmaFwhPhMn15HEsR-0bMJfvqaNrhf776GLRJJsg8RwrTlMVBoH8bTWf4xAndx89dHBpsQOvdnuRhbjGqA36fugUQbDO0WR0K3FUWhI-3ffq8tJU6yeC5r7KR0qR1lZ9a3UiSzfyG58toG2ztaeAh3AdIqWPyph41PFdrV47DF8LVzzWHM08lL0S5chtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NseV1liy85L4Wm27VFTx6UMbNEOykT_S7FmGRF9JsSE0VlgBqPi4FizrptRUEBvfM_EPP0SF7ZAfBnvdnue4AsCPXhSu_A0ra79d7_s29yynsBrFfvhCmuRhpe9-C8ZHCDAhLcnKYyHSm_j0EmH8HpkFnmWXcITXS21rwQ2QQjeRA0ygK17Lj6w2l-LN4IPzbLsROo8v9UvwamkZV3Se1Pqrk-OYKbLQ647gXZpjzC-2I8jun9Ki5g2AI4F1RzRPZDqbbVrWiDiWTNnhbdFy5lk_styLd9sti2t53axtxKmLpHbPTpSFQGxsbffRvR81dEjaoXg9JAjxME3GGGLTGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NkipBHnT2dRiY79I5WWtLijdB8-UzrDFCQiJ2xpi9DTrKw2Z44DQ0tQEmwobRkYkGH0XXm0SLl-xJLyInY5I1j-j0D2kNqTPkCSXVF_jUWU4E-PGjv43tyQfarJ9dHUVYWf09I0xc44P2Wv-868roTl9EcMsG01_EzX_h_QW6v1KYrHGd5COccucD_3n0K2Jtj0-lu8ciD_ZBJES_GEwYTrswLuWhokNWCIPfgQoexLhVcVBCyk2-y40d29gMdfSd_6DSFDwYr-pu0VVWiYrH9Pim8z1jY_l7UfmQ20iMG5q6tainQ3I-LOuUR4xJGr-sFHaf3aB-YNQlfrYofTw4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vVXp7sRR3eYLTVs-JtklRrle7S7Jd2DuKFFYoYg98pm3g1bXrj9am7JQPQrmTuRJGe9v8odBkAiz6tu2ThHWRSu46hJCdMORcBA7e91nPtyC4mJb4jfuLRkGHQvCr9kiFxQn1xjySBLNjBin2lbPW-rEWKwU0Mq7sDxNUMoaXx3omx0yldCpoi4Ja8U6w1k6yXeZ5ao1ws9ivt11VqfRSJoUFJ8Lf7qSyOycts_oceRf4FFwUPMjKqoQ7Z0DmZAV-OXSWF-D1HZWWss8TVQGat7hT6g-VJFQfuUIFhrorkniF2DFbd0YvSg_WCgtc9YX7xq2-YJ1IxyvJ6a64gdzYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zv5zJEgzbRsclDT6sRhw33pKlWe4tRqphcxD4hFX7X8rtyvwEDC-Rhi68HLI0Ru2hm-ZFh4CkLiMjx7b3JeTw4QPb6zhccwZe0YcoMt7FmP30SgQ_hOXGkqq3m1GnkIf7liJvvz8iifrj3PHl5SkkyoBiD7PdRHSVaer6e59oHXAhx1Zs3xLz2wq4q4Kp4sdU1-WYwRPHAr9-SztmZbwFr4nOb55uXZ-d1WZBmLPocplXN43Q-kITRxezyOTrLoGO7H2TXgwZVJhKps4s5gBJEeMUa54cpLRxJLRwi79THiLsC7wgixOGt2BWKMUQw0zqZtnPO2UgFVy_4RiJv2ijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQRHoH4JsTYH_uSs9Kd-nyN-pMGy5dgy89j6wyRJ1nVwBP8mwNmpvvdypsWgrPmh7df6tXRl_iKNBMnfOTqi70RVrDFERuxw_0TAE30gyHa_gprIR5ao920nxhukJTz5Law6wSKPde4MF-Vi2jSBGdkeLUIL_SL5CqCwDuuWdlo3yaoUt1zajnjA8hfwkoQH4rbWUyi7VAmHryJbUm_sXe78piS3amT4eus_6EL1dAaMbrA97_wFWGz7iBSi-gygx6-lT4K7gxoGeRVz7w0CL3T6H5ktI_YnGDjGSIT6ifROqHRPk40DypB7oIIEiijgLSDRFBFgZwvURibEVce0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iUkUji9lHhnhi1yEjX5kbqFBAOfTxuitIQi3r8FSHPn-JPEuAud-j9L3MBCfdoadOmkujToxnsStwkRhctAvmsO_lIRBXH_FxJiXXgWdMoG4jmbp55sB5LIMAc2kaby29NqYqwi_yUiEiLn8AzwtNcKqzOQgJJvJTpG_ui4DmNgMCSyTZ3DOb7sXfvos6bJSJWVD2le-G_PsoSF9VHAKnez3i3UeFPWMvTLlN_ws98i7rribFXBE1CdU1aYoNiPsIFSNxlwaKWTUes8qBdY5l5UmjoeENHRn-AfsUVR-We_xD4wZymWrqmAJNW8IZXFW8MMSteKqv7vRwjR0t1LTyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TY4JSW_zfQRDCUBiHko9s07luJm7S3zhm76xiIrLtWkD7JqrklN0u3rGJSUKw7WpyMFGvBt7n7SYY4KSSZFhBipjGK6_lmMfyn6w5oi4i8kIh8y4WYsOprkol-TaO7QUB_k84UuEnQn3sxOoQCbK2CYJGm795zvhc95Q2G3ct5-dqZCYAO1f40FKd-3jPHKGcH1ELte_SSW_-eARVuYBntURiMDGCWKYdsMSqSj8dPK1qJ2H3ke3z4CuZAD1ZPAqTDMWIRne00ksebqXngx-DYDwdAomlRpDPtFp7pkK-JTEjsfWuk8D0u9UNvFGMi5acgSJKaS8tUbiZsQPiwLnpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=WhDM0bGDaRMmy8i1Yhs4CQlv6ljKE-u8evEeiTemKXl-D_P3Zx36I4S141t52zHL8aMp3xNntZFPSgzvIHHE6XUHnfzWDr7Te_tYF5Tg8eG6nyFuJa99zR6fCTJYaKJyRQIrG5fRZDognc0Q-RpD8JBjr4k3LpNm-zqrO1WAb0fzVPZjvMa0uUuPjkwb3ADY2wOy2b1-SHhoVrRt4HB7-nFjzAVuDtG9UfnCTdIHPcC826PDOizKCtH_q9Sj9KnVcfv3xTdf2ry7sm0NYHF3y0h0FwE5Y-BVGte_7hzexFk_PifYfNiB9DoDKwimUpDTqd8NuIrajlb91DagvJam5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=WhDM0bGDaRMmy8i1Yhs4CQlv6ljKE-u8evEeiTemKXl-D_P3Zx36I4S141t52zHL8aMp3xNntZFPSgzvIHHE6XUHnfzWDr7Te_tYF5Tg8eG6nyFuJa99zR6fCTJYaKJyRQIrG5fRZDognc0Q-RpD8JBjr4k3LpNm-zqrO1WAb0fzVPZjvMa0uUuPjkwb3ADY2wOy2b1-SHhoVrRt4HB7-nFjzAVuDtG9UfnCTdIHPcC826PDOizKCtH_q9Sj9KnVcfv3xTdf2ry7sm0NYHF3y0h0FwE5Y-BVGte_7hzexFk_PifYfNiB9DoDKwimUpDTqd8NuIrajlb91DagvJam5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=X8-zhKVYMvqWxGaYITX196Ak71STtW_F5Sfx1DelZmKKhM8StWb5FxXIWWYTnSLGNLBtZarV4Ve3I2V6YKb6L-Mq7Ydg_CelZEB3ye72XYMyCFWag6iOl1F3sE0quMqOH3Nsz7I1AfaUwzBFLDY0H7XX5AnMg09mccNp8wxpTNlqF_ixgUOSgQYqGHdTO3KrRsqQg2PJSEvXUx9nVtVCAmz_vDGaz9Z4G0TU7RCDeIHW4yuKZiNf-OFxaynZ4wp0ylFBqKsgOYTmRRotpqGZipcplWMOhgAa0gXOOn-yHanvFmHPh0_Bahtdxec_Fu-tzlf6gc4W2K3wlts6qWk4Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=X8-zhKVYMvqWxGaYITX196Ak71STtW_F5Sfx1DelZmKKhM8StWb5FxXIWWYTnSLGNLBtZarV4Ve3I2V6YKb6L-Mq7Ydg_CelZEB3ye72XYMyCFWag6iOl1F3sE0quMqOH3Nsz7I1AfaUwzBFLDY0H7XX5AnMg09mccNp8wxpTNlqF_ixgUOSgQYqGHdTO3KrRsqQg2PJSEvXUx9nVtVCAmz_vDGaz9Z4G0TU7RCDeIHW4yuKZiNf-OFxaynZ4wp0ylFBqKsgOYTmRRotpqGZipcplWMOhgAa0gXOOn-yHanvFmHPh0_Bahtdxec_Fu-tzlf6gc4W2K3wlts6qWk4Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=cEZHYOsTG1PrnBqYW6QXgVBLyd5gsO8dR_apVNx3T2G8Jv2AAE0U18E0-DYRQJa0Yc8ByH_vTayo_7prVgc95VM1ljMf-N9DTCq4eZ10NymrNhkTpXVSkSpdQN6pemHHkou_EczJSdnuKTYuPHBqgXb6bxouA70K9_aIno-zpV2IhjwTg-5UkDza1jAy-AxjwmvkzrANzzNvmU_YCocYsMyTzQFDLAcQLRpqXdVNEBnxEz9IJgIZCFY9FzsdVro4okQXae_nbok5eRD0a1OX7aVLgrbg8hrx5to0rD9gt0cHYn6bO0ToQNUaGiK7KePBj0PMYXbavELokCIX39tEaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=cEZHYOsTG1PrnBqYW6QXgVBLyd5gsO8dR_apVNx3T2G8Jv2AAE0U18E0-DYRQJa0Yc8ByH_vTayo_7prVgc95VM1ljMf-N9DTCq4eZ10NymrNhkTpXVSkSpdQN6pemHHkou_EczJSdnuKTYuPHBqgXb6bxouA70K9_aIno-zpV2IhjwTg-5UkDza1jAy-AxjwmvkzrANzzNvmU_YCocYsMyTzQFDLAcQLRpqXdVNEBnxEz9IJgIZCFY9FzsdVro4okQXae_nbok5eRD0a1OX7aVLgrbg8hrx5to0rD9gt0cHYn6bO0ToQNUaGiK7KePBj0PMYXbavELokCIX39tEaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZmByq6BuLI44L5iINdbS1T25E0dqTHuSPLHoJa7q0rzz3f8FEHsYTrDnKZ2HhWqj0q9pMwa9KqzH4y9r6byZWwVzLJ0wMBRnsH-mM5EWj6nMyuSMVAeAh8DinrKiSD86RP8t6gq4yP-hvsAsP5P_PXL_VbwOtJJ_T3LKX1gyJOX3nDlx_n1aG_yTXk_Yaf0aB5Oao62jgtQnX_1PZjLI8rk-eV9N_EI2DiqGYeoORF_FQY5cVJKdtzwRIkZvbVgZ3GIM2QiOkmDulI-u-_kwi0TFSodP-FEhJ6l-1rEfilev89LvPtSGGbWHKg68Wo3t8M3U60ndJ8QnLlsxXTS4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=A7xYTVk17m8OOoHVbceN5cLPkpH0et_t_-FAv2j69uh3gnId0m3YSqJWZ1YDNKKCvrf13lg_lcqzMpYykSIllHq0v9iVp4ByIcncx3tOGLXYIUlo6X49_62j5zPjq9RmzXqXKjGe706LqTU_iDbaN0cq51vdogPT7YSmvRxQSyRHAPbzUQ1bLeEtNyNI4ithMO1a6hesNunmkjteunDWuHxprj-mquENBYx7_CliTmdB8Dc_Eb6WRG7Aq1Ep2UisSiPcjBEhXruv_62VLVFsk049q5mBo3UR_e65slDq-GtmCndIEoxgmBlUaogZv37b3F57Znuj9CyzsyBvWeam1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=A7xYTVk17m8OOoHVbceN5cLPkpH0et_t_-FAv2j69uh3gnId0m3YSqJWZ1YDNKKCvrf13lg_lcqzMpYykSIllHq0v9iVp4ByIcncx3tOGLXYIUlo6X49_62j5zPjq9RmzXqXKjGe706LqTU_iDbaN0cq51vdogPT7YSmvRxQSyRHAPbzUQ1bLeEtNyNI4ithMO1a6hesNunmkjteunDWuHxprj-mquENBYx7_CliTmdB8Dc_Eb6WRG7Aq1Ep2UisSiPcjBEhXruv_62VLVFsk049q5mBo3UR_e65slDq-GtmCndIEoxgmBlUaogZv37b3F57Znuj9CyzsyBvWeam1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=cYffGN6BD6u3bVpO5hnatNtrW8UjCtMCEqq-sH-1D5FrMoqmHkM35zqle7T9KBoYtA5MdRl-ecvbBV9JfPUc6LnbFxxCeG7TMK2vjnrwtI3DC7BXkwYTGmjsSAjjS-w5ZA8zUKz28iX4seVc_DuNTWcmY4P9BfvhVZqMgnX_UtBGVCMSq5ps2WvBiVvzkC9GXHOWL05Ap_MuznqBIcOtDN9pnlldhZL3jBvIcv9w0iQ6gdijMVpgTMibYWEfQ7HsfkyFoPe6SNRp5VNBSM-VrLllGaIfaRFTmXHA_vnrYdoX-An-k1t7hejq7Wvsts51rwyuvWe19chLmVfvPIZGcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=cYffGN6BD6u3bVpO5hnatNtrW8UjCtMCEqq-sH-1D5FrMoqmHkM35zqle7T9KBoYtA5MdRl-ecvbBV9JfPUc6LnbFxxCeG7TMK2vjnrwtI3DC7BXkwYTGmjsSAjjS-w5ZA8zUKz28iX4seVc_DuNTWcmY4P9BfvhVZqMgnX_UtBGVCMSq5ps2WvBiVvzkC9GXHOWL05Ap_MuznqBIcOtDN9pnlldhZL3jBvIcv9w0iQ6gdijMVpgTMibYWEfQ7HsfkyFoPe6SNRp5VNBSM-VrLllGaIfaRFTmXHA_vnrYdoX-An-k1t7hejq7Wvsts51rwyuvWe19chLmVfvPIZGcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEkJCrhqJf_ijCMCBbbrMUkGz1gRCHhgHtfNqVbyLPpOzm5JsedS7dMO0PjMLa7qML2JEGeFwgx5OmoSbNLBtmTE7VJPMSuE-iubQlJfeDtLLmKHQC0AKgDUhPyd5in5ofuNIRiMq7ENilO2Jmdpk__QogTrIGqOR707bSIoggohzEBurix99ZsmjJPdqyzSKQ9VV5i7jGPFnm1z5Hbw7VQFMhJfITALk6Jjd3EMLf4osJVSJXVN1nu37foTaeDR7feAwKWb3y7WR1sVqHbgoh7vroKEcC0O_bIZL8Txl7DJuMoLmh5JrFA2d-8SxCDmBEQWH8j8nZsMDfsxRRvsGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGzNK1qmV_J_MzDoBA7rjbiXR6lq2agoNirSlVnt4RXIaKPeAPZ6dENk8e4kv7ynmkDeD1tGe0QrHiMPgKbwbSm0IPZIFD3vfZnnSVwMKc-TPcH7ZUhD51lRdPIvkyewKIkVLaL16P5XM_RWSLUYAjNC-xVmx7RGHlYq3Yw86pAc-S2NgGFbQjuZM0Pf8CYFQSrA9ZSidQiUbyQveAc6ZwEZvj2dJT7M1Iyx6bieLkyUg8we1V7Jfp1bir_rhpHwNxdR5PfoqSLz4BzJICEdPhCP_-B2BtJDb2ZOY0EqSuHr3q49jcPywlAT_zNzi5nBWqge4ug-44GYmbRgrSUlKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHwz0gjAkWrIirkOEUUEwsZ9Pra4y0wXyEJ5r60-5U3GkFtY0VmwIN9U20C2bqn09hdOlgmpZ5dhqLEU2Zl_mpik7x-Ujn3XmT8fRcVJkTAT7uCOXUVo_qUl8PCyBySMnZQ-_K8So9uzBCK_WgNPULoea_G0lZgyYHVt8upE6yQmC74JMPdWT5uS1YsHzHECnpVhk61L0o_MhPgJfews7VgqPQQqgqBqEEpXo281l7sVQUmCXyRs8UZKBS0AW5HudFsSCzo_FLOJSY_ul9_8p5Fxw0GWXtyZucOJ5rZ-onep_u4_3-AZoo8L2KKas1r-6PLSYluL6qdvZLXhAB-h0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MLkot85XJJmpBPlKPgEGcYe11vJ-KWr7JfPhozUcAoyEGB_4lwLkuuwSUlrgKcW9ju1ooozc46snEpRp4REtdPMlva-klSIoeh97oHHubqnYSX1shU27UkT3vTckov0Npt6aZSoheyZUT3nqNwywRePtc_PnOeSIdzNAcYEY-hKizE1f9K17FPWlIgjSJVhBOM0vZCkriE0W1RnivEThLB748NO-PyCoOvQAUKC9fIZpBbRCMhlNoQq4SVtbH0-gWbEzHpTAvgvbedAvbY0mQbr2FhzzNXe-JaQ-5dIhzPpMJNwz1pSaQ96mmopmLY5YrRsdxZBd4Ftcvit116osiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZCTUtjweAikjFznHvEJzJmyvKMCFrtjbeVE1_UjYP0IOwkATOVz2MdB72MSpyvMqOqNMiEgoFSd9VrLhDmEhCjncnbEf3UBExZuARad0tHlpnsk-QdnBg4Liro91-HRUCo9v4ZEZxeJZCD5Rt-mnKbixCODoUEN51kOdSv1UwX2C8TskR2uMeLTeyOybBNNtCQIC8ryez78IcOtoDOqk9Zv_mrcuFyKxmG8KwRaYMmE0p00ScO7xwc0ZYr1axBi8tc_7Ra8z7QxKvWKQKI3pKpgqHMZWLE9ECfRywpKfo_AQs_ZxD4tQUAOlBznRXeL9vnezdlOtEYmMdTRuEUXuQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=nwWbta31ruqLbsid_5DW_cq8pjOg3xMwaI0HA8xNKZ9wbCujLJx31YO__I8E2CTgcACLiRgFfLDI45rxuzDpwHnU81Mjzjt4Is38llqWV_a0sc5F-KOvho6gc1NunoSLc6o-ijJ97Wa62WA_aytvZQoKdevla4Q0-fxFiMl1YBxopWWRKgjLTL4juKWHLeBB5vXPdQ21dh9EM-USVM9C3g_OZaGNH4oInWYzlzqfi_qM7QHMk-bhbhaRMcozLWG-ClH82nWL_BTpk5o-QopeRyark5Cvi3J0d71eG9YyTtEH-VnKpuVnVRIYyMjYxfyBbJJNRU9NbqAsvL7PL1lvEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=nwWbta31ruqLbsid_5DW_cq8pjOg3xMwaI0HA8xNKZ9wbCujLJx31YO__I8E2CTgcACLiRgFfLDI45rxuzDpwHnU81Mjzjt4Is38llqWV_a0sc5F-KOvho6gc1NunoSLc6o-ijJ97Wa62WA_aytvZQoKdevla4Q0-fxFiMl1YBxopWWRKgjLTL4juKWHLeBB5vXPdQ21dh9EM-USVM9C3g_OZaGNH4oInWYzlzqfi_qM7QHMk-bhbhaRMcozLWG-ClH82nWL_BTpk5o-QopeRyark5Cvi3J0d71eG9YyTtEH-VnKpuVnVRIYyMjYxfyBbJJNRU9NbqAsvL7PL1lvEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEs3q4ivdoOF8J6z46ByqWxhjrOqTayBvOuIu0JcdU_MotZyzvcGMXk-kC7vuiovwCO05bAAZy0kmM74wjOPp_wQkmtjXJbEdVMEEfB61CW0z-Pd_Rz7Z3qVXjUptI0t36EgAJjSVXSmO0GFiETfwOCBGQfJbsUwQhLkqHcFcuyPkx6i_D1LQYZI5HfkL4_Qy3ZXzk_kBYBCgXEvYp9SMnYoCouqP5fUey5kDIkHP4T20M-y81ZubPjGs3h9Flx-CCsOI9n2MmssuPGXisp5etQtnNilrlVFYGzc3ohYVr0xyCckGhE1uy5hgDJtb5o2uIpYkBLD32zsN11_watrvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqOJeIpmXAgFi3-dQC3I9AOrbxU9Yv71edbLvUAGrePvvQORhLg1YvLeyGezsw_Kl1V-DnwzBKGRBG6d4MgmKPuNuJo9mIGJlrefLXn2nfuVGlUlIJk11wZbcziIDePc1_G8r8Wo10Nkf-ay8_PUxYqiXBvTawrvKirh8RWZLz9_WcC9zclGxfoYQ3tlgbRWnO6iwAJy4AL2xxHT63IaS1CanWva2vMx9ZakymGp8ZCNYze4bPbYWwG0qpe4OHPdWAmEYkyL-XzXQYX0J6ziMB6GoJ6_CiyJrOqvu5gQaGf2xNcr1N8SBgEHPbXmUxrSycgNfKkkEqyl8vxusGT_Jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggsO5xIG3Nu-iI69g33xMme7on2IRrxlRnYaAgU0iUzeN9Qz-v9R5vr64CT9EB2QpePmSn6zESR8xOOvWR6q2AakPRYG7cmY6Z0tn_6vn-6TyKIG-lD6nuj77ZBx7GFYbgFlaH6ZIlza1O45Pg6D9OPhSkb7Mt2A0uOFE1QvxmmLGroAsmTIDhJAZQxu6fsbdh3XLYNRoguPQp42fYhR-eu8sj189bVVCtowRS9U1mvI6JRgBsj3SLA4pjhbheR-wm3su-L4WNni2N8ulFvP0InyTH1Be9SXPEzHuo3iEHWCD6S3WniNIEoa3zdm2Y12e2rtg0Vs_mALUF2qMf93ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZ7AKv1d3R3EBS-bS1QnivM2kHA_Vh4firq7LUXRyDZMS0xfI9BV8K8bJSMiRt8LMoRu8G-uh-TufeT6vFLS6mzN2upbKx2ttVzoaAC0wa6uWgA3U9C5-Zzx-SgqBrot_4RK8y7L56NL24yS_ovkYYPOVDRNemxAMN6_0bGdLO5nSFFFgFdPLjXb7DXnro-HUMgAfogV6gob2s3bC15M4uxi6Nlw4nOnEzSp53U87183PP_rBnnQrRNEWkacTpgv_8aQ2aPyWChg6SBDSbWGVbhid5BsX0lXUWVReHStZuBKUs5Q1-wtP6ZIAnPmiT_vclXStx_Gh-EL2g-PN_Ta-w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=W9eWyHzn6UNLEdgWVEivI2AhEWNsdyh1QhAlH9RlWhkLw5VU8SsY8rFIx3BEARv07bZN5VQ7e5wMW_CEGK1FUvr-d44S5LEogGqqhHqxGbzohko68N-jHEjiMf2ETHrkwkbwRc3A8d_dSDePZEgMpy-qJDJTqWT0MaiPTUS2FBmegheYhqouyYlP7tZ2GaJSxHDHGLrIYgEB19nguj0D0h7y-1EqxmmwOrEmn7niT_pSvMV4pZmEQ-gx1Kzlm8pcWOkgG-LfcsN1QJMd3QFIH3rNx8D-3wYveoM4nADaj7V3WmTv4gMqYlhRqnnyeJ3r8LFb97vmhrOdJDuhfPKfeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=W9eWyHzn6UNLEdgWVEivI2AhEWNsdyh1QhAlH9RlWhkLw5VU8SsY8rFIx3BEARv07bZN5VQ7e5wMW_CEGK1FUvr-d44S5LEogGqqhHqxGbzohko68N-jHEjiMf2ETHrkwkbwRc3A8d_dSDePZEgMpy-qJDJTqWT0MaiPTUS2FBmegheYhqouyYlP7tZ2GaJSxHDHGLrIYgEB19nguj0D0h7y-1EqxmmwOrEmn7niT_pSvMV4pZmEQ-gx1Kzlm8pcWOkgG-LfcsN1QJMd3QFIH3rNx8D-3wYveoM4nADaj7V3WmTv4gMqYlhRqnnyeJ3r8LFb97vmhrOdJDuhfPKfeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQFO_EHofmWqbP2EfctPScgFgSX3tNqITwGfUcqYf7pCJuofuBpCKrVek6EmL9PkVKIkuM2tw3nFL_nDAtNDRh2xIs419A3J7jakYsjlZa5HmyBTQWlzmfSTpzxEY3bIWlQcHdFiBjx9RXdlSDfkggh06z-UbPxV5SvELdDJ4hn6SXGB51hhQVqdXXnf07UVJea0WGdBRaY7tBjrIJN5XVqJgikwy5QWR7G2QbpIjdTyXsxc2_Tx120OIpAJio0P-uQt8uP4kqlapNboA3ExhVHRboSxzheFwpHLFW6kvYgrW78SSSZ-GARrsLaZ0SdNcLue6iGrlUrOhxVkK4oXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVbOipz4W_9lDfilWKmsTZBNpwu19i7dvFHBSAyYXZnUeb1Gq5NDjV5pZRDhwVMNQPV5mE3HVYCmGZKUlDXGWE2ICnO48xXfUrGNUxnFbNa66AnnOlXJUbV2F359CkpB8U4r8T1hc2U8iquJURRcluASWz7AYaMWYzs3U1z3fQ6vELg5GE5WuQOzOTN6TDggFQ1aTsrzdJrE1-NSq-_JdIzdlGfxHRHOYXLyHPtSU1xxSN6-aZCYa4mEF2ZEJ1hjmoJ982onSnRxlhS9BMgCy8coArs9Lsf9fPe_HS1RqZFv-VuL0LdF22AWe0DQc_3zMaF66QS-_U4-uL-Jvz_LdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kO-POGXlgBkP7JG8FUc5DHnSvTS-P35TrpMJtlgK3jRw-3jVAU47TC1LoMAYcjj7DXbpjUMxjV1UJlWTgQC00NDdLiLEmAP4g_5fiVNtw--RS_K2evQjv6oVPESmjMfsRKqnxYmNjdh7SAUNod8xo5ppS45P-lENbJm32gBeHD-ecH-eASE-tjFWQCjPECh9pbagv4dCiD5QC3y1FnHzFOsSx2Ba2bSXABCgwpDbg_Z47FUPha05PJsssrhXN2q_epfHW7E8Cem4NL4OcAST2vZssvdY-kI6wvaL4iTJfm_53YbEkMvW5bvn6wUaJ3g0tbIPS-tFa0WJPhXXOWa5vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g15F5wZwvjEURm58ToOaSkj5TJ_VDzmxSiNde2FdPcOChnvM_-DRX2ZqELYKFv5Uak89IFok1FBkhruexGH8weoz1pEeg2jg68D20eD2moXIE2CaLGEqucU48wLEfYQ4yUiXwYUp-IVMh3kjSaaOr2iZ7YNUG8St9fidCxRwwGR-b7UaAq34Zi3agaCPLP1L2sNFKOephqF3duw5ho9kGWM8yAGeM47zkLvMF7Qh4UhCmBdfFzx3NunGoYzIIZuWp-qZnHcL4QiKqZFqGgt8aKEmSRVlVRQGkmIFvhornZTm3cjS4dzaCTEhJ69684Ztic0lrMArgDsMDz7sOtFlrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKnsgnfnlcwS3IFnUUa6ZWFjO5fCjkRqOajZiX97PZIq4kGBLGu0jk8_iekcqHL02Tyw36QdR26FtD4u2vyhwznAu3nOFBcq-KqFUuurvzT5jyeplC6pbjpMGm7Mvyx5KIA6_uKCtj-kxJTYpEuX0C3SCyOIfjS8gVfXjOSDnK69VVOb4g1faG0Gm6ZkobCBld7H8TkHPPxqdoKTBsCB9IayctdVWAjtO9-_Xmk4GYb5E8IVv39qj_jNEBDM8ydn9M8J6yMkanIbCCc9G24yi1IfKXE6-Yd6N6nGPsoWJiwyX-3pSv7_gRE0RiB1eCW3of3eD42CepFzIPcXHnfjHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5045" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=lfuiruhw8CyZEwum-reqg0QRR1ZelPOCO4sTlPDrCLk57Di3r1Ch6k0xmt4KUu9Kz9oRkkgpWgOTcnfsoOy8cb4Kky82WQ_NWFKCFbQPSEc4_sV0B-TpksvozKc2EeYc1DlHhCUWj2K4EDyukPfM1JpJC80896IGtQM1sz0ljVYd39zizYwmF6UmNnIq46qjn3OJIVYk109DqCFho8ouk5VQ8ThVnUWe8HYRJ1hlrZsi23jnE20FVk_jOLFVB8Vmjt8QWYmKEtR0G1uI_RTr5KrCUr_Tf_HWmdt0kjrW2ZLDPFPcDSZd8-xQR0xOPc1OCz67PFzk99HA0b1asPFgYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=lfuiruhw8CyZEwum-reqg0QRR1ZelPOCO4sTlPDrCLk57Di3r1Ch6k0xmt4KUu9Kz9oRkkgpWgOTcnfsoOy8cb4Kky82WQ_NWFKCFbQPSEc4_sV0B-TpksvozKc2EeYc1DlHhCUWj2K4EDyukPfM1JpJC80896IGtQM1sz0ljVYd39zizYwmF6UmNnIq46qjn3OJIVYk109DqCFho8ouk5VQ8ThVnUWe8HYRJ1hlrZsi23jnE20FVk_jOLFVB8Vmjt8QWYmKEtR0G1uI_RTr5KrCUr_Tf_HWmdt0kjrW2ZLDPFPcDSZd8-xQR0xOPc1OCz67PFzk99HA0b1asPFgYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o85KopOB5WzHA5HfKr4R0cceGOkYz5RolL_JleXZh2mNBVvBvJd8LbIVKDmiyhANq0X-QQ7hmPjKz5G6VA_RzUiGF27zog7BUfYZ-4KTFWisJJ6iTeabjmyurFSpqzHsUboZI_JVySdBPQIw6ebZRfcyBVrWyD64I9MIeLEK3cJFsUtd7BPP7jPJeSoRpPXyV2n7dYAH9ziSgmKtdeY2FlsONzc0xp1QDKIuOzS83qSdCR4tu8kEM3Spt_9B9_kCnLSM5krA_xLW-67UO7QxOkcMeN4VDGbjnyIonLCa_OSgVy5eCqdPABThd_N2gwn21gxxo2rQzJcERhzTCxLzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
