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
<img src="https://cdn4.telesco.pe/file/jDFH9e1F1WWYmGaAYELCFkiT1x3VyNUYST8tzWPT_egOpT-6akL1D4jgGCoXBphpxgZLNOznq_CskYKP2XvrAHQCGpjbs29FJ1jmLLeDSwKI4F_ha2h7AR0w-Xdpt_jC04IriuE2WcVcJBP1Dlb6QIKzu_HITf_WhQFMFdvsy8fo1BylAjLcaS1XhG-hdeias2066ZVQCDk9aqg1tdD-6TZ2tJJkChJ90DoqvhjauTKNo7K6rBPfsOQuHD1Yhwxftt4rF6gv1rbJ0XhYrt-VOdRJf0v9C9t4_uC9b09RJpuEPWl5Klcz6Co7Vn1HMws0T0EWaYqafybkxUrAZoxc-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 15:32:00</div>
<hr>

<div class="tg-post" id="msg-21191">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بی حجاب ها بیایند توی تجمعات شبانه بعد که تمام شد لطفا خودشان خودکشی کنند</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/SBoxxx/21191" target="_blank">📅 14:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21190">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بی حجاب ها بیایند توی تجمعات شبانه بعد که تمام شد لطفا خودشان خودکشی کنند</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/SBoxxx/21190" target="_blank">📅 14:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21189">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خاتمی، امام جمعه تهران:   کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/SBoxxx/21189" target="_blank">📅 14:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21188">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مخبر، مشاور رهبر انقلاب:
پرواز در منطقه یا برای همه آزاد است یا برای هیچ‌کس
اگر ایران امکان پرواز و دریافت خدمات فرودگاهی نداشته باشد هیچ کشوری در منطقه هم این امکان را نخواهد داشت.</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/SBoxxx/21188" target="_blank">📅 14:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21187">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خاتمی، امام جمعه تهران:   کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SBoxxx/21187" target="_blank">📅 14:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21186">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خاتمی، امام جمعه تهران:
کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/SBoxxx/21186" target="_blank">📅 14:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21185">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bE_iM5W_sHNGQkYLg8mhEcHVSlv3-V2njnfZIWYMAZP1JWD6yScayuiTBqgZa5NK4RYjHhTp4R65cbKY-zwZT75DnQ0x2FmPFO5FaxsVuvMTJTZFkuAm3xa1or7heqKWpyuCPqfEwfexq6UoxURmX1J_h3KlUTT0cZlCOhYeXUMv34S0_GHODUIDj5obhL6UxBPP6idSO3coTTCmTKRck6bhIAwbvq-lVzxJK2PNJelROLG1dAptBrhLCjhtVC7tgs7wVylNZoZAiWy6T2YTc0CdyV2-bbRxmh9zwoUd3aS6iqLx3hCeRUrrO2OP1bpKK-fVWUGUDnYsW-yNUNkTng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در حال نزدیک شدن به کف محدوده بیش—فروش است.
در این شرایط پرتناقض، بهترین استراتژی فروش در مقاومتهای نزدیک (4292 و 4308) با تارگت 4235 می باشد.</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/21185" target="_blank">📅 11:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21184">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrtnlVE8RQaGdvKa8bnlC86P4dPS0i8V4jz2blAx39Hw5iE2FCdgYiEu8U6vpsK2xUiPZ73hCobP3Oj5gkY4dPNWQ6GwR6NL2pcYJKuwacjdXPyZhvXjRqOUxp5D6xC7YLcfY7ajyht_-PME_nHUJu_p-LGnJINKaehmRFjrLd7UH5zXiwmFbwS2Ma-JVpwJVaSOhNYrKm0X6vm5E3IS64GzrF0mXB7Cz0wlopNq1IWeCZQj0qSSvmsvjt-lFqJMg6Erq8yRAaWdUUQt5J1YfYOGE7FPy_BnhzbqsS17nPfTtMSZ6XRzzTmKlHaS_ON3zgFWTGVBnnOND3Y1l6C_bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است و هر بالایی فرصت فروش است.</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/21184" target="_blank">📅 11:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21183">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پاکستان، ترکیه و عربستان سعودی در پی افزایش حملات حوثی‌ها به خاک عربستان، یک جلسه اضطراری رؤسای ستاد مشترک را بر اساس پیمان دفاعی مشترک مکه تشکیل می‌دهند.
این جلسه اولین گام در سطح فعال‌سازی تحت این پیمان است که مقرر می‌دارد هرگونه حمله به یکی از اعضا، حمله به هر سه کشور تلقی می‌شود.</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/21183" target="_blank">📅 10:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21182">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کلمبیا تمام روابط دیپلماتیک خودش با ایران را قطع کرد
دلایل اجازه ندادن به بازرس ها آژانس  بستن تنگه هرمز رعایت نکردن حقوق بشر و .... بود
یکی از دلایل جالبش رابطه ایران با گروه های مواد مخدر  بود</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/21182" target="_blank">📅 01:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21181">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نتانیاهو:  «آن‌ها اسرائیل را — اسرائیل کوچک — متهم به استعمار می‌کنند. و چه کسی ما را متهم می‌کند؟ در میان آن‌ها، گروهی در بریتانیا و فرانسه هستند.  به نام خدا، آن‌ها این اصطلاح را اختراع کردند — مستعمرات آن‌ها کل کره زمین را در آغوش گرفت.  استعمار؟ لطفاً…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21181" target="_blank">📅 22:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21180">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نتانیاهو:
«آن‌ها اسرائیل را — اسرائیل کوچک — متهم به استعمار می‌کنند. و چه کسی ما را متهم می‌کند؟ در میان آن‌ها، گروهی در بریتانیا و فرانسه هستند.
به نام خدا، آن‌ها این اصطلاح را اختراع کردند — مستعمرات آن‌ها کل کره زمین را در آغوش گرفت.
استعمار؟ لطفاً دست بردارید».</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21180" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21179">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dad7c5c99.mp4?token=jLHhshoOFs3YXLZNzr-Ond38ZYhLs1fLAge5GvU_eOyMl7BA0emlJI4VD5ezD1_X6-03dPYrtL-qhTB_niCqhkAEg2kJ4cuOzm51baYS51zxEB13w2rFSsVhOcj-Rbx1wxEcIZtjnfS4JiSgWgzny_BapiFPeRAYJlrfmkIgD1KebJp2uo3kg1fC-Rzzl5qdlvWJg-MrvFYbREjppbvhvkKmccHptO7VwZUQ4KyBRH4ReisgRoyKf2KPV8expeozAlwp2fuCc_MDK2CmE43ZiO5n9l0zZ85yDcE4PNB-BGHYuS4cwpSbNsaJgYsEUPrm7X02HcY3mTDE3lBKGC83-REx2O8LIGg64PaEQ3P-7J2gHzREhQ5jwSM98lPjdT2BwJKEghifPIpWRckqOchJR_1TrSzntAyDo8FRm82VFMPrEogRIQB_h_rgU7xbgBKEITvRMs7k6MjrnojHbnglkajo2nXEK9gpbUcr6X2-EcuNVC2ySqEoR92hmUh7He3helOjSml6iovP5_ogcSj3x-PhkJJALPJA6QGTmLDxF4LBwDq9ozaSZNWz_Ghe6Y_PKnc8tAVMkm8Ct_YagEGveIDDkbhH8kCxr5qVMkEICL1H-5Wk6hwvlpb6z6Po2dcNpoNFfTxqu6wf7O3iF2uoFOfqrYbw84RXD94_NF_y0dY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dad7c5c99.mp4?token=jLHhshoOFs3YXLZNzr-Ond38ZYhLs1fLAge5GvU_eOyMl7BA0emlJI4VD5ezD1_X6-03dPYrtL-qhTB_niCqhkAEg2kJ4cuOzm51baYS51zxEB13w2rFSsVhOcj-Rbx1wxEcIZtjnfS4JiSgWgzny_BapiFPeRAYJlrfmkIgD1KebJp2uo3kg1fC-Rzzl5qdlvWJg-MrvFYbREjppbvhvkKmccHptO7VwZUQ4KyBRH4ReisgRoyKf2KPV8expeozAlwp2fuCc_MDK2CmE43ZiO5n9l0zZ85yDcE4PNB-BGHYuS4cwpSbNsaJgYsEUPrm7X02HcY3mTDE3lBKGC83-REx2O8LIGg64PaEQ3P-7J2gHzREhQ5jwSM98lPjdT2BwJKEghifPIpWRckqOchJR_1TrSzntAyDo8FRm82VFMPrEogRIQB_h_rgU7xbgBKEITvRMs7k6MjrnojHbnglkajo2nXEK9gpbUcr6X2-EcuNVC2ySqEoR92hmUh7He3helOjSml6iovP5_ogcSj3x-PhkJJALPJA6QGTmLDxF4LBwDq9ozaSZNWz_Ghe6Y_PKnc8tAVMkm8Ct_YagEGveIDDkbhH8kCxr5qVMkEICL1H-5Wk6hwvlpb6z6Po2dcNpoNFfTxqu6wf7O3iF2uoFOfqrYbw84RXD94_NF_y0dY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک موزیک ویدیوی Erotic از اتحاد عربستان و فاکستان ببینید شب جمعه ای دلتان باز شود!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21179" target="_blank">📅 21:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21178">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رویترز:   آمریکا و ایران درباره توافق مرحله‌ای برای پایان دادن به درگیری‌ها مذاکره می‌کنند</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21178" target="_blank">📅 20:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21177">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رویترز:
آمریکا و ایران درباره توافق مرحله‌ای برای پایان دادن به درگیری‌ها مذاکره می‌کنند</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21177" target="_blank">📅 20:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21176">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اسرائیل می‌گوید حملات جدید علیه ایران «مسئله‌ای زمان» است و تأسیسات هسته‌ای ممکن است مجدداً هدف قرار گیرند.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21176" target="_blank">📅 19:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21175">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">محدوده 4255 بسیار مهم است.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21175" target="_blank">📅 15:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21174">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbBRpDkIG5V3R9odAF7VcleOaB5zXW9hOjPB24w3fQ5ZmRhSxbMC3vC0RT0A_DcYvE8PgPWjsJJ30LoCADa8VmGStL_O669Y4uXZm1wSwV-bqbADJ7MZxxowVO-GbEHXZCFwqnMKj2wHXqQdQ2JjcZqRpPbvYRGUoC4uSJ1UzsDQcCobamoJacPzcsN2NVImk9B8Uu9Rv2EvWxSQLUARK7f4UorGo0DsDUAOjzLyy33V-TlHGFNKuAj7dNILSo-DG1-n9zFplNhxN9iAaOcnYlPZL6YSQsYRj3Ltb-KgCd9-o7L8PCHe_atBvcQMTkWke9MugHz3UI2-_i4gR_xikQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناس صداوسیما اشاره نکرد که اگر ما توان تصرف بحرین را که میزبان نیروهای آمریکایی است داریم، چطور توان حفظ خارک را که مال خودمان است در برابر نیمی از همان آمریکایی‌ها نداریم؟!</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21174" target="_blank">📅 15:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21173">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کارشناس صداوسیما:   در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیربم</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21173" target="_blank">📅 15:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21172">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کارشناس صداوسیما:
در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیربم</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21172" target="_blank">📅 15:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21171">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مرندی ذوالاکتاف:  اگر کشورهای خلیج فارس جلوی پروازهای ایران را بگیرند، ایران فرودگاه‌هایشان را با موشک باران تعطیل می‌کند</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21171" target="_blank">📅 14:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21170">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یک پرواز از شرکت هواپیمایی وِارِش ایران، که قرار بود از تهران به دوشنبه، پایتخت تاجیکستان، پرواز کند، لغو شد و به فرودگاه بین‌المللی امام خمینی بازگشت.  علت لغو پرواز این بود که اجازه عبور از حریم هوایی جمهوری سلطنتی باکو به این پرواز داده نشد.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21170" target="_blank">📅 14:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21169">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏
مصادره ۶ میلیون بشکه نفت ایران توسط آمریکا
تانکر ترکرز مدعی شد:
نزدیک به شش میلیون بشکه نفت خام ایران (به ارزش تقریبی ۶۰۰ میلیون دلار) که توقیف شده، بی‌سروصدا در حال عبور از اقیانوس اطلس به سمت ایالات متحده آمریکا است.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21169" target="_blank">📅 14:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21168">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b70a5ce7e.mp4?token=EPG3Bgl0LdYao7Q9FYhZNaqLuLtA2FyWOs0CRvOOB61b8We3OOLz6kbrLgOJhgi5kA8r2u0K9ZvKIPGk1RVrDUdNFI00a3FrFjMWbaaQuEoZC65mQLNAZYv0bFpB83Jvro1YsFzsyhRqzq7p_Ni6qoktBG4yyjkz2eqkP0qDCDcHH44sRKsjma5VanEAfEscOOJQPCRBZf8ykOngPbXzuKUD118EdkthNN5HnsszPRkk4RThLWlKwzgt8BHo9nHGmOrpixrQ7HxCnPdJpkbVnAiVr-JqYx3ChU5BSNmF7v2uq1QapOitVh1LscHlKxHhp-guZYF25CW0Gc_BP3QPuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b70a5ce7e.mp4?token=EPG3Bgl0LdYao7Q9FYhZNaqLuLtA2FyWOs0CRvOOB61b8We3OOLz6kbrLgOJhgi5kA8r2u0K9ZvKIPGk1RVrDUdNFI00a3FrFjMWbaaQuEoZC65mQLNAZYv0bFpB83Jvro1YsFzsyhRqzq7p_Ni6qoktBG4yyjkz2eqkP0qDCDcHH44sRKsjma5VanEAfEscOOJQPCRBZf8ykOngPbXzuKUD118EdkthNN5HnsszPRkk4RThLWlKwzgt8BHo9nHGmOrpixrQ7HxCnPdJpkbVnAiVr-JqYx3ChU5BSNmF7v2uq1QapOitVh1LscHlKxHhp-guZYF25CW0Gc_BP3QPuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پرواز از شرکت هواپیمایی وِارِش ایران، که قرار بود از تهران به دوشنبه، پایتخت تاجیکستان، پرواز کند، لغو شد و به فرودگاه بین‌المللی امام خمینی بازگشت.
علت لغو پرواز این بود که اجازه عبور از حریم هوایی جمهوری سلطنتی باکو به این پرواز داده نشد.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21168" target="_blank">📅 13:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21167">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پاکستان حملات هوایی متعددی را در افغانستان انجام داد که هدف از این حملات، مکان‌هایی بود که برای ذخیره‌سازی و پرتاب پهپادها استفاده می‌شد.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21167" target="_blank">📅 11:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21166">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECNRRTXDZnw1isBwiZG80GQJtxnJv4SqgjWH0pNx6qz8p0ZXAVBU_ZJP57OrnSTHzS5aUmrowHLAeqEVXYgBH94Gnty8wjFPamo8qDi2IOPkRifvlPu28huHsIia470kuQZuV1bbbapSrfP9eA1F3TFl7ME-zmLoypH96DrQUSiOxJpkMzYyvrEiGNXbPbd1Gw0qNJTg6sV41-qLCsQhNNGkThN3MvfMlGQ1wQKXB9VDLPo-ItVWXKCdUHmP6jbMAtqksxRBdM4IZq_gUBquLyRYV6Z8MBTJScfNFCZaaJiqdMfXaj1l7Uy-rrhPd80XBLab_XSoVxA3lEdROgGhRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC در حال نزدیک شدن به کف خود می باشد.  در این شرایط و با این تناقض، 2 راه داریم:  — صبر برای رسیدن طلا به 4335 برای فروش با تارگت 4230  — خرید در محدوده 4260 الی 4255 با تارگت 4300</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21166" target="_blank">📅 11:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21165">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/21165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21165" target="_blank">📅 11:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21164">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان نشانگر پایین تر بودن قیمت نسبت به سطح ارزش منصفانه طلا است و لذا خرید توصیه می شود.  محدوده  مناسب خرید:  4302</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/21164" target="_blank">📅 10:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21163">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhNBE_s8wshAusdTRFc6OEFB51jo9hbS2RilHGjJYyUiifEatH9vLcaOz7vdQyJ0f2mXOhhGN4pIT_u8uOcEvp1-Og0gv-2upJyjaG16JrqFlO8YiuZd4Nwez9lkBuPpVPBJNp5Un4LalUYTQ5dCb21SOzLSlU1hh0Vk3IgG70uyP1bQROsXjSY2gc98mA6iLz5dx02i2KiDPSdwmm1Sb1SLy-f0EEgU3oJJ-FZtNBYQQU7807gUm5b9xV92noGV4hX3AQ7shtjsM0UgWMkjiLJULda3e6XQcAoUdHU5qegk9CNyuF3qkfpbMXxCn4tyChP1NE7kHJX2oou0oZzlqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در حال نزدیک شدن به کف خود می باشد.
در این شرایط و با این تناقض، 2 راه داریم:
— صبر برای رسیدن طلا به 4335 برای فروش با تارگت 4230
— خرید در محدوده 4260 الی 4255 با تارگت 4300</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21163" target="_blank">📅 10:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21162">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0FepR13EVgCs32iB8y5pA4TdfEEp9n0AL_umxiADGACIDDP1SqYo_xBCQO9MNFQXedGmvC1eiaGjbKCh4cE1lZdz_GzYedU_982yqX7_lINu3TXpKv1kPtTxWlHN8kxHBdyQiM6uDgJ-YRWsNk-VQ32xBtNeJBNg7h9G3plXjER3WUtkVi5RS4dnaeM-KGRDMAw_VPjy1rSjR87va2FlXgtQuP6NhFw7h_qEhw84hVYrrqDoIe8G2rTyCPw_86mctRcbuFJZycztCmxRIz4Z1sY8X7OaH20o3_-D1m5KGGXrxWb7pB8aw-S60DHxSvE0SHWqaIXFIQtDRSREyF3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بسیار بالایی قرار دارد.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21162" target="_blank">📅 10:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21161">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حملات هوایی پاکستان به ۳ استان افغانستان
نیروی هوایی پاکستان بامداد پنجشنبه حملاتی را به استان‌های «خوست» و «پکتیکا» و همچنین «قندهار» به عنوان دومین شهر بزرگ این کشور انجام داد.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21161" target="_blank">📅 09:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21160">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مرندی ذوالاکتاف:
اگر کشورهای خلیج فارس جلوی پروازهای ایران را بگیرند، ایران فرودگاه‌هایشان را با موشک باران تعطیل می‌کند</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21160" target="_blank">📅 01:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21159">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شلیک موشک به سمت هرمز</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21159" target="_blank">📅 01:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21158">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuUai7qQpRoF1zA2JISQ64JjwLQJB4RfKtN3jNV_D8rK8-mFw0LpDZv9WxnbOloIChnujvkvCw3XU65H8PAOhxRRF3O5dkDjFiwAbg_ITlubxVptCxzDW05dQyOt8mj0XWJQ109bkgfUCvRg6baCxhCQPFvjHiWJAS2zgaRO0FXD9KqrE69-mQw4RXRn6NXeoKeFtWDFs1joSCjuXmsXEI73snQ0ZFqlzA5mDJbnuEMBoQulixK1UXBiU3x4XxI3O3Dj2uMkaiZ33gOjgBSt5QYldaWxxftrvRGtiw8F1mHr4a0aQ3Ax8w5-o8cBg1CERfJ7wUHUDJky_VTwWiEiHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تی وی جبلی هم عجب سیرکی است!
خود مردم ایران صداوسیما را نمیبینند بعد اینها برای اسراییلی ها به عبری زیرنویس میزنند!
باز عربی بود یک توجیهی داشت؛ دستکم بدبخت‌ها میفهمیدند کی قرار است توی سرشان موشک بزنیم!</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21158" target="_blank">📅 23:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21157">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بیانیه مشترک ترکیه و عراق اعلام می‌کند که ترکیه بر اساس یک زمان‌بندی توافق‌شده، به‌تدریج پایگاه نظامی بعشیقه-زیلکان خود را به عراق تحویل خواهد داد، در ازای آنکه عراق به‌طور کامل اقتدار دولتی را در سنجار برقرار کند و گروه‌های مسلح خارجی ممنوعه را از آنجا خارج سازد.
آن‌ها همچنین توافق کردند که تجارت، سرمایه‌گذاری و پروژه جاده توسعه را تسریع کنند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21157" target="_blank">📅 23:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21156">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vS1dA5zbP31YJwyBr36jFyUpQoKYHhbFlxz3ap19nclXqFAVMd0QwuQRf-_wu0qbAyHgr0rjdWldvNmeiNzsQyfuGqUQ-pU0LqUrOSoMzko4BoGi-kXqnLgJSMWasmCG5cEiK_00fF_0oBr35aGeJi-9Rv_dHMkhimhYoRNx0rL7IhE_cAqQaCyRmuFTwwxEmpmsnd8gswMk91fybEuGVsZZaRnOrs-aO7wJBADtnSkUIr_fk4bsmkmIP1nD8aRnaQF9Ijd4cRQsqNvRxml71S74SH6g__ItcrmWnXpXvx_86Urdi_f3DHVnJtRuh8yDzRH0WaLGkAXZP1fGhsZtZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا چین به عنوان قدرت بزرگ عناصر کمیاب جهان غالب است و چرا این موضوع اهمیت دارد
چین ۸۵ درصد از تولید جهانی عناصر کمیاب تصفیه‌شده را در اختیار دارد و در سال ۲۰۲۵ بیش از ۵ برابر  ایالات متحده استخراج کرده است.
این ارقام تصویری از بازار جهانی عناصر کمیاب پیش از بازدید آتی شی جین‌پینگ از ایالات متحده ارائه می‌دهند.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21156" target="_blank">📅 23:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21155">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">درگیری مسلحانه‌ میان نیروهای امنیتی و افراد مسلح در محدوده جهادآباد سراوان</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21155" target="_blank">📅 20:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21154">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">صندوق بین‌المللی پول: جنگ در خاورمیانه که از اواخر ماه فوریه آغاز شده، به طور قابل توجهی مسیر رشد جهانی را از طریق اختلالات در حوزه انرژی، کالاها و زنجیره تأمین، تغییر داده است.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21154" target="_blank">📅 20:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21153">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21153" target="_blank">📅 19:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21152">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ایران معتقد است که دموکرات‌ها در انتخابات پیروز خواهند شد و ترامپ نخواهد توانست علیه آن اقدامی انجام دهد.»</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21152" target="_blank">📅 18:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21151">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پزشکیان:   بمب اتمی در اسرائیل است، اما بازرسان در ایران حضور دارند.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21151" target="_blank">📅 18:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21150">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پزشکیان:   با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21150" target="_blank">📅 18:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21149">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پزشکیان:   با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21149" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21148">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پزشکیان:
با فشارهای نظامی تسلیم نمی‌شویم. به دیپلماسی معتقدیم. از جنگیدن نمی‌ترسیم.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21148" target="_blank">📅 18:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21147">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سخنرانی پزشکیان در سازمان ملل اینقدر تند بود که حتی کانالهای ارزشی 6 سیلندر نیز از او ستایش می کنند!</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21147" target="_blank">📅 18:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21146">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رویترز:
دولت امارات فعالیت شعب بانک ملی ایران در این کشور را از امروز ممنوع کرده است و بانک ملی ایران دیگر اجازه هیچ گونه فعالیتی در امارات را نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21146" target="_blank">📅 17:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21145">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جنگ ایران.pdf</div>
  <div class="tg-doc-extra">300 KB</div>
</div>
<a href="https://t.me/SBoxxx/21145" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترجمه یادداشتی از Foreign Policy درباره علل ناکامی آمریکا در جنگ با ایران</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21145" target="_blank">📅 17:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21144">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">محسن رضایی: تجاوزات دشمن نه تنها ایران را تضعیف نکرد بلکه آن را به قدرت چهارم جهان بدل ساخت</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21144" target="_blank">📅 17:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21143">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">با این منطق، فاطماگل قوی ترین زن تورکیه است</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/21143" target="_blank">📅 17:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21142">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">محسن رضایی: تجاوزات دشمن نه تنها ایران را تضعیف نکرد بلکه آن را به قدرت چهارم جهان بدل ساخت</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21142" target="_blank">📅 16:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21141">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">روز شکوهمند بازگشایی مدارس در ابرقدرت چهارم دنیا</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21141" target="_blank">📅 16:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21140">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJc4DQUEk6L2QGDP766tW88RxFBxnt8pPIr0Mib9BiVNfxYRovxA_lc4v17DIqhnCgGc8HKF8WTHxL0TzF4cV32wTXF99j1q3qTckcH7lyRqYVI3BNOE9eO22XSsvI_-UV4uB1Rxpjvsw-Hkegt3yAxnXJw1M_ZvOFgblerSSPBo2mAdgxI6IaHaxxtqpIDuBqlviJfi3tse8UmgfRC5KJdffXIsSec0gTz04yeHGMyo46Yb1KoELwCMj3vnqhfXzM3l9yZWClVjZT--8C1hQqDBUtuGTIE3HAb8ICu49rio7AoU9SWTS9tKnVIobAXq4GvULUAZw9G3hjWvPH7ohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باربی های وطنی به مقر سازمان ملل متحد وارد شدند!</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21140" target="_blank">📅 16:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21139">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">هدف قرار گرفتن یک کشتی در هرمز و کشته شدن ۲ نفر</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21139" target="_blank">📅 15:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21138">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان نشانگر پایین تر بودن قیمت نسبت به سطح ارزش منصفانه طلا است و لذا خرید توصیه می شود.  محدوده  مناسب خرید:  4302</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21138" target="_blank">📅 15:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21137">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هدف قرار گرفتن یک کشتی در هرمز و کشته شدن ۲ نفر</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21137" target="_blank">📅 15:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21136">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">چکیده تصویری پادکست</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21136" target="_blank">📅 15:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21135">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">📌
خروج عربستان از mBridge؛ تقویت خاموش نظام دلاری  خروج عربستان از mBridge در کوتاه‌مدت اثر محسوسی بر دلار و بازارهای مالی ندارد، اما از نظر راهبردی یکی از مسیرهای بالقوه برای کاهش وابستگی به دلار را محدودتر می‌کند.  بااین‌حال، این تصمیم به معنای توقف دلارزدایی…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21135" target="_blank">📅 13:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21134">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwhe2Nj0b6S0tdsNkRpsC07RqrUBm5fkbElhsN62d-DIy-vuWcR63ZOdQKtfym-d0p2VAs4d-y-Eh9OBJwVUFNlCoh5TeUlPn_6v1rayYOXdJRGjlGbX37-DqIRP74Fpzf0Ge5dozi4UN4O-ejk1jbhedRmKWmT--Z6kdEsl7r1pGpfx3OWrvjHjz4cw936N2mq9bBU2EvflBs9Oip3Wt2lbc3h-f_jzL0LQHZS9kO9a64rKz8xdzuHbTyRAKLbdT4KvlGg7Kte8S2ylw4J9Oc01f-pVvY0vaY3GwGQKF79HsvxtL6qa_N0yamvrMD6nJ1dCuXoIv0oTNv8tiT77lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
خروج عربستان از mBridge؛ تقویت خاموش نظام دلاری
خروج عربستان از
mBridge
در کوتاه‌مدت اثر محسوسی بر دلار و بازارهای مالی ندارد، اما از نظر راهبردی یکی از مسیرهای بالقوه برای کاهش وابستگی به دلار را محدودتر می‌کند.
بااین‌حال، این تصمیم به معنای توقف دلارزدایی نیست؛ چین و سایر کشورها همچنان در حال توسعه زیرساخت‌های پرداخت جایگزین هستند و
mBridge
نیز ادامه دارد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/21134" target="_blank">📅 13:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21133">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzQ_C-hWNDgKbkCCXRUfmcxBcB7G68U8a5MkjT7nHRdJPcEXzyCtYRlx5_6hp_qakq2uR33GaNbV3g5ebO99j36SJRoTySY0NdGCGWvTGqaR3mlW8wtvW0NRPHq8GoV76BDC7L1LTSMWENaOziZNThGT6drihy7wZ6fQYK7BJ-CZUhtcy4znkOzR0pjLC7otmPHEsZyfdlm_mQsWojChQbtHcTGWPBYNgsG4m4PqUJ75q7qN4_6z6foHe0YzvOE9FVvp_0JvbqhCF9YhadQcPwQAvzdyq6DeXxSqnsySrIzwu3sF59TTZEJ09iQarhrjol-AJ9fm_TG8WiTpYCvz3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC کماکان نشانگر پایین تر بودن قیمت نسبت به سطح ارزش منصفانه طلا است و لذا خرید توصیه می شود.
محدوده  مناسب خرید:
4302</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/21133" target="_blank">📅 12:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21132">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uApAUuEp6ydSoAbEqooWeOncCBXuI-dODaeoe9qXeOsbuu-WQ2Hlf6rvxL4u1-QW8kbveqpDpBt5zqGxRttmF3co8lb2l-1f13XK_CQkaXgtFHdYZ4ZB-MOLvTOgNr0tCHIlSxdIv8xDd06WlSOG-dBem4wREny4Z2o8J0ykcUt8i9slKWKiNukgYUddWRwl-Mb5zDcsvk2C1hkc5qv4ShNe0DOeWIOIRDJuU-Nm94-vbkF05bKThTynUFiITvGAyZ4HBGPk4i9bVF3Jl-3zsQuafcIfYNM9MVQrEYcJxkqPQ1nyvTL8IKZHapZzMvMkwzWehxaSeyI5oW-a-_4Bgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بالایی است.
اما طلا از صبح ریزش سنگین داشته و لذا دیگر وقت فروش نیست.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21132" target="_blank">📅 12:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21131">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8eae425e.mp4?token=HaNLqijnxTEPsDyFaKcZsneIj6e_uOx0ul4dSYHC_R5lTqEVO3oJ4ukcieM7m_-trEIgWaIXWqyQeEsfbTPG1-UJUUo6d59KQYI7XFsSq5z50g1eGSmY13tHSEBztZrsAsRBO9HwWh6g-R0w3BwcFntZGl8RBh8UD-TjDAbgyJ1xbYsaSTpU00LmrRhGsWpvxF9harbFLXrXrzdbpgWfDsmojj2iUykGgrQupnhIWjaVEacF7cMd6GHrDvaK_VluorU1EiLbmR7CLyoVz1XbTDyZ2CObHlPclhDMZu-VMnHemlNMANLR8wzPRzBgnTXFzZGBEK5F8iuepwfYH2JjRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8eae425e.mp4?token=HaNLqijnxTEPsDyFaKcZsneIj6e_uOx0ul4dSYHC_R5lTqEVO3oJ4ukcieM7m_-trEIgWaIXWqyQeEsfbTPG1-UJUUo6d59KQYI7XFsSq5z50g1eGSmY13tHSEBztZrsAsRBO9HwWh6g-R0w3BwcFntZGl8RBh8UD-TjDAbgyJ1xbYsaSTpU00LmrRhGsWpvxF9harbFLXrXrzdbpgWfDsmojj2iUykGgrQupnhIWjaVEacF7cMd6GHrDvaK_VluorU1EiLbmR7CLyoVz1XbTDyZ2CObHlPclhDMZu-VMnHemlNMANLR8wzPRzBgnTXFzZGBEK5F8iuepwfYH2JjRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز شکوهمند بازگشایی مدارس در ابرقدرت چهارم دنیا</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/21131" target="_blank">📅 12:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21130">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">زلنسکی
:
ما باید قوی باشیم و باید به پوتین نشان دهیم که او تنها در این سیاره نیست، حتی اگر این رؤیای اوست. و به همین دلیل او باید به مردم احترام بگذارد.
متأسفانه روس‌ها فقط زمانی به مردم احترام می‌گذارند که نشان دهید قوی هستید. آن‌ها به ضعف احترام نمی‌گذارند.
طبیعی است که گاهی اوقات مردم بخواهند ضعیف باشند، زندگی خود را بگذرانند، وقت خود را با عزیزانشان بگذرانند و به فرزندانشان عشق بورزند.
اما نه، باید با روس‌ها نشان دهید، باید نشان دهید که قدرتمند هستید.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/21130" target="_blank">📅 11:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21129">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آن دو دیگر (کوبا و میانسوسمار) هم که میبینید ستاره شوم کمونیسم بر بیرق چرکین خود دارند.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21129" target="_blank">📅 10:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21128">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">موسسه مطالعات جنگ:
به نظر می‌رسد حوثی‌ها با تهدید شرکای بین‌المللی عربستان سعودی می‌خواهند این کشور را منزوی کرده و مانع تشکیل ائتلاف علیه فعالیت‌های آن‌ها در دریای سرخ شوند.
حوثی‌ها در حمله به پایگاه هوایی شاه‌فهد در طائف عربستان در ۱۷ سپتامبر، یک جنگنده اروپایی «یوروفایتر تایفون» ایتالیایی را آسیب زدند. ایتالیا این جنگنده‌ها را برای پشتیبانی از عملیات‌های دفاعی در برابر حملات ایران به عربستان مستقر کرده بود. مشخص نیست که حوثی‌ها عمداً این هواپیما را هدف گرفته باشند یا خیر، اما حوثی‌ها پرسیدند که چرا آن هواپیما آنجا بوده است.
حوثی‌ها احتمالاً این مأموریت پدافند هوایی را تهدیدی بالقوه برای کارزار تهاجمی خود علیه عربستان می‌دانند؛ کارزاری که عمدتاً از حملات به تأسیسات نفتی عربستان تشکیل شده و در میانه پشتیبانی دفاعی کشورهای مختلف از عربستان ادامه دارد.
حمله حوثی‌ها که به هواپیماهای اروپایی آسیب زد — هواپیماهایی که برای پشتیبانی از تلاش‌های دفاعی عربستان در برابر حملات ایران به این کشور مستشر شده بودند — در واقع اهداف ایران برای شکستن ائتلاف مدافع کشورهای خلیج فارس در برابر ایران را نیز پیش می‌برد.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21128" target="_blank">📅 09:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21127">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8V-lApu0JgCWSWTFWF07rsSPfduAMUxwL-FWxp0CHXZK_ykfVxW-uD3cZGxXn_JQw9yoJPderXyULMYRHSurJ7SrvjhtkYqlsU6e8OfYXjiBqdPkwida7WYVAyzIS9k8FYbQJnDFZSEUaamHQUH-6p53cOdvnwa0TIFxghMlxNab5aHYpTQZqtswUffNkFruHOdi17RM48ygTl-iGu1EiEDQ5qXnATlpEbfYYjWjmdsPXn0feHqhayGJhmYGaSSKB39XooevzG4N2DHcOeykXP-UMAdbfJ1nmIeJMYDMf2s6OIsMRArvEpc1sj1urkqejUvAKcAiAYIRHXKTdRaPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 28</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21127" target="_blank">📅 08:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21126">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نخست وزیر یونان، کیریاکوس میتسوتاکیس:
ما در ۳۰ سال گذشته هزینه‌های زیادی برای دفاع صرف کرده‌ایم، اما در زمینه صنعت دفاعی داخلی، دستاورد چندانی نداریم.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21126" target="_blank">📅 08:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21125">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏
سخنگوی سپاه: نحوۀ پاسخ ما به حملۀ جدید آمریکا از اسرار نظامی است
اگر آمریکا به کوه کلنگ یا هر نقطه‌ای دیگر از ایران حمله کند با قدرت پاسخ خواهیم داد.
این‌که پاسخ ما چگونه است از اسرار نظامی است؛ ما اسرار نظامی خود را فاش نمی‌کنیم اما در میدان عمل نشان خواهیم داد.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21125" target="_blank">📅 08:27 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21124">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو، انتظار می‌رود این هفته سفری کوتاه به ایالات متحده داشته باشد تا در مجمع عمومی سازمان ملل متحد سخنرانی کند، در حالی که نگرانی‌هایی در خصوص اعتراضات احتمالی وجود دارد.
نتانیاهو قرار است به جای فرودگاه بین‌المللی جی‌اف‌کی، در یک فرودگاه نظامی در نیوجرسی یا فرودگاه بین‌المللی لیبرتی نیوارک فرود آید، که این تصمیم تا حدی به دلیل نگرانی از پیچیدگی‌های مرتبط با ممدانی، شهردار نیویورک، اتخاذ شده است.
هیچ ملاقاتی با رئیس‌جمهور ترامپ برنامه‌ریزی نشده است، هرچند گفتگوها با مارکو روبیو، وزیر امور خارجه، و سایر رهبران خارجی همچنان در حال بررسی است.
بر اساس اظهارات مقامات نزدیک به نتانیاهو، سخنرانی او قرار است بر ایران متمرکز باشد و ممکن است «غافلگیری‌هایی» در بر داشته باشد.
مقامات اسرائیلی همچنین برای احتمال اختلال در سخنرانی او در سازمان ملل، از جمله آزار و اذیت یا خروج هماهنگ هیئت‌های چندین کشور، آماده‌سازی‌هایی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21124" target="_blank">📅 01:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21123">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">صدای انفجار در نزدیکی جزیره قشم!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21123" target="_blank">📅 01:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21122">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">صدای انفجار در نزدیکی جزیره قشم!</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21122" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21121">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گویا جلسه برگزار شده و به نتیجه نرسیده!  First Time?!</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21121" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21120">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MH8Cdsv3UMvCCf7gRqhHfvBf-gxFlaSEa-x0r_vZeGr0bCb04_NEhRY4C96ACJkRFYe8ho1NWgsJeU9F0AveYn7lKZHYxqBdGpOg4hLvFLG1yHOf_67TLa-ib8sYrpljpgq9bwPoh-LvsCsT_10tG16JGEYcvmlyDey4Qe80keO0U0lZ5POQ3T19YtmS4odJleQGq2RPNKPec7pYlD_plUlnaTQ38dxt-f7ucy2UEbjFwi3fC6akcon4IEs0KRi0eg1fEcRzc0Y0XSf4J_58eqCccPSPCU1G4kFI5vkwlaou2tS8GlMi1somdEktSYDH8_CtmQm1uTxTqCHkBWdvww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا اعراب به دنبال فراهم کردن شرایط دیدار حضوری پزشکیان با قاتل امام شهید هستند.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/21120" target="_blank">📅 00:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21119">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaQd7hqLHZ8KxCUephBQf7VjmumEcdSQYKwMKYiyu2ip_SJliwJOj5C8f1KWFNB2j7wECzeatFRXs1iRpaufm6X0UjWpiR9KO7_wbpGOvwqqFGIcFLd3UDIwxnZkdW7RYE_BLjs2qapL8bm_zwrmp3cHGpMvwoBUJZhbWRHYUlZs8EuijNyJMAJSxh7-Gh0jP95ShIhrls-hdtl0-Dys32IHICkxlpwYGLngdxeg0bxO5qEUIdrMizHz-26QtaJZ-L-TiiNVXLKZfBONRH4AqFBIhfbnABDI1Ti6qVm7QLeFxKk5NCT9_ToK53p4-llgUuioz2MABGVvhi_25mP7nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RUNCFD — W #SUNRUN  مقداری از نقاط ورود پیشنهادی ما پایین تر آمده است اما هنوز بشدت روی این سهم مثبت هستم.  پیروزی دموکرات ها در کنگره و توجه دوباره به بحث انقلاب انرژی سبز می تواند این سهم را به بالا پرتاب کند.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/21119" target="_blank">📅 00:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21118">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USU8U811QHe_cAgeTd-e8oVSIGQfyI99lu2yOPQRu1YUuOLZ_YTL4d1jgBarwi7dcR67loZbnLQRRdjP-JRbIBOGTn9NG1B-EckOeg24iXJH7We59IJ0G2Tg3Z4gm1hkj1qp-rwxKG1_JkZ5pNMlIasVL0-LN_kqrx_DYen2HuulEEgM6_5n4nNrHx8WsFIZoTt5ODgEQQwwPlPpQFmRT6bKTHrVT8Ol9Xeqgdfqfgx1jXZPM3k9U2cDivrQKKibjjq54xm6zotSO9kzoNSjwToRQ6OaCGe-chbU8u8q7NwcXIzmWvmFtQUTIuXRLTQQCrIrT_EMX_f5R72sdWH3kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RUN_CFD — D #SUNRUN  از محدوده ورود دوباره حتی اندکی نیز پایینتر نیامد.  البته هر چه پایین تر بیاید خوب است، این سهم یک رشد دستکم 3 برابری دارد.  همراهان Secret Box در خارج کشور این سهم را دریابند و هم میهنان اسیر در درون مرزها نیز میتوانند روی بروکر WM Markets…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/21118" target="_blank">📅 00:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21117">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLifyujBdKjvkGgn2QNKtoweqFRZcLPozFdyPFqNIkxCzLPkzLkm2MqLfsEhXbMmOTsXK14oCic1c8s4dCc_lpD5JJRvwvQYVtDNg6VTf9TotV7H5hhSrEIlHWNsHlpd-nIacrgg0DoKUG1_PqxPL8ANbR6KXtBJVbRrxcqFXtfYHA0arb9te-WsCcP_jOJLqZ53VDMyZDiRm6JaHwlnxU0cl_S_zrUAVKx19j9J5LUR9ZIvet2F_J0-Ktagcg6qAM8aDzOgmfonuCCnA4jXoTXAHM8WxPgInKsfhjHBmoOfWWDAIANoJ2BiMJdZQ5xOOXoMRi9YUwWs09gPYJC0Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL   دوستانی که درباره نفت دایرکت دادند؛  پوزیشن های خرید ما به هر دو TP پیشنهادی رسیده اند و فعلاً خرید نداریم روی نفت.   تحلیل جدیدی از نفت ارائه می شود.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21117" target="_blank">📅 00:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21116">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/od8BkI70it024LnquDv0VGyJxV_njQh5fcxM72kq72cH_mutBlTrnmsez3QlpZCcnA3o9QuQFKRK8IFbevUOu9sSqr_5w2Ae1TSPKP35lHi3Fi74Il29IZKlNdTMBjfV173EackKlMr7WhCupjGAA6VTwtDFPphModSrp7wOzdbOTZbzRhDfFNaa0EeKWk8bHKzQ4RM11PjFWLN7_Fz9LiYxcbk1JyErW_CWmSmhW_V-LGmxLGp2nik8IezdxnTf7ychI7GjDqnrEXJWYv-IpTWNY1QL6HIFhskjPjOkUXAciW6UbZ2f6rwBhqRuPkha41BKVyRqEzlJDXUkykbBcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H4  پوزیشن پیشنهادی.  ریوارد به ریسک خوبی دارد.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/21116" target="_blank">📅 00:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21115">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تایید دیدار عراقچی و ویتکاف
صداوسیما:
با اصرار نماینده آمریکا دیدار آقای عراقچی با ویتکاف در حاشیه مجمع عمومی برگزار شد
ابلاغ شروط ایران برای بازگشایی تنگه هرمز دلیل پذیرش درخواست ویتکاف برای این دیدار بوده است.
رفع فوری محاصره دریایی، پرداخت فوری همه اموال مسدود شده ایران و پایان جنگ در همه جبهه های مقاومت از جمله شروط ایران برای بازگشایی تنگه هرمز است.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21115" target="_blank">📅 23:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21114">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggcqT-_SmTxNclhUlf77nAmIEBTkOt5JPSndRdDn_SFx0rSe5pMc8SiAY0mUCNwQD1lfLzDuyDO6BvW3UVc3NUCQkBOLyMnsvMgvGfy6hCz5pd_80KSMCwD8sV6u64HZsqTphozb_MAgAKHD7KxRHaCvLD8xRGvDkzTP-MIzYU__VVL0CqFhhdTHfaMCi-jGFyYwoWA3YA-uZzmBDgWUN-wJcgp2sS52Jpi7VckGE8ONnp9gR31YGxfnZJ1HOUmuAyedWJ3MeVuwXY4htZH_UZEVGW6BxC9t7LF97F9fPWf_DjTioLLMPckQZp3PZXtPWISJN8tQVr92AgC4G4OKXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد بز برای پاسخ به کشورهای همسایه که در محاصره ایران نقش دارند</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21114" target="_blank">📅 22:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21113">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ادعاى ترامپ:   ایران در حال مذاکره با ماست؛ روابط با ایران در حال توسعه است.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21113" target="_blank">📅 22:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21112">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06862e3345.mp4?token=CXPRNZoVyyZFHCp8wriXWAWS7lm8QYBsmw0SsLTwgxIXcc-05X4h6IchZi-heqCiK4JXi3_qXGl3lB6Tuq8mKsl2tC4-J_e6gTMEEH_lzE3Cga1xD-5zXAz1wJjGByT8jUq5Ni78NxbYd9x-nf2Rkc1zQ0aG1pHzKcRrlDVR6lUT3-w4WDUCuxFXPoT92OWyp2Ejy-EskEd-xmV6e7dMtU6-UpXOUEtcw8uuYCHRLjrq3G-cTUV6nggoxvSa2Z2tNCSL93PBKaNuIG-BwER9kjh6R4vfxg5eIvrKqSmCmCnVfNqk2rzkWj5j-c4ZStrraNRNOuXcatvYojD9NxYLUxfmmNvuYhtWMIjdYTxtyisFwqAKXYUqQ63v0M44enL2W_OQO_LoPPuF8UtZynYs4N9go89sZ11U8YUB0nvnLB7TCf0acR9TnPlduwns4nucT0TzBzFrkCWSr2RJn0N8RWoB7o7k0VgLSRF-T7EKaxDTMzapzrz5VMMSNVKbDBPbXSEXQ5RraKTUdN0S_dF_WyqpS-aQTysGJJfhMMO3rDrlcuv_8BMf8Cv07UejF5BYwf46hVJdn-_engHFDfF_Q7erc6aRa0TX17O-Eg1KcJkc2sjArQJIKMTb-XKGaC9qWB9n7GXbbNEsXe3V_dpcjFQq6WYXTIcdUUZMuhS7fSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06862e3345.mp4?token=CXPRNZoVyyZFHCp8wriXWAWS7lm8QYBsmw0SsLTwgxIXcc-05X4h6IchZi-heqCiK4JXi3_qXGl3lB6Tuq8mKsl2tC4-J_e6gTMEEH_lzE3Cga1xD-5zXAz1wJjGByT8jUq5Ni78NxbYd9x-nf2Rkc1zQ0aG1pHzKcRrlDVR6lUT3-w4WDUCuxFXPoT92OWyp2Ejy-EskEd-xmV6e7dMtU6-UpXOUEtcw8uuYCHRLjrq3G-cTUV6nggoxvSa2Z2tNCSL93PBKaNuIG-BwER9kjh6R4vfxg5eIvrKqSmCmCnVfNqk2rzkWj5j-c4ZStrraNRNOuXcatvYojD9NxYLUxfmmNvuYhtWMIjdYTxtyisFwqAKXYUqQ63v0M44enL2W_OQO_LoPPuF8UtZynYs4N9go89sZ11U8YUB0nvnLB7TCf0acR9TnPlduwns4nucT0TzBzFrkCWSr2RJn0N8RWoB7o7k0VgLSRF-T7EKaxDTMzapzrz5VMMSNVKbDBPbXSEXQ5RraKTUdN0S_dF_WyqpS-aQTysGJJfhMMO3rDrlcuv_8BMf8Cv07UejF5BYwf46hVJdn-_engHFDfF_Q7erc6aRa0TX17O-Eg1KcJkc2sjArQJIKMTb-XKGaC9qWB9n7GXbbNEsXe3V_dpcjFQq6WYXTIcdUUZMuhS7fSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روند ساخت اسلحه های دورزن در یمن!
با همین تفنگ های دورزن، حوثی ها صدها نیروی مخالف خود را در هفته های اخیر کشته اند!
ثانیه 29 جالب است. یارو در دهانش قات می جوود اما دارد اسلحه دقیق زن هم می سازد!</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21112" target="_blank">📅 22:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21111">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خاویر میلی، رئیس جمهور آرژانتین:  نسیم‌های تغییر به نفع ادعای ما در سراسر جهان در حال وزیدن است.  اخیراً، رئیس جمهور ترامپ اعلام کرد که ایالات متحده در حال ارزیابی مجدد موضع تاریخی خود در مورد جزایر مالویناس (فالکلند) است.  ایالات متحده در حال بررسی این تغییر…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21111" target="_blank">📅 21:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21110">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffb8ac635.mp4?token=HESMeHDRNk35BE8Ky-qHx4FhPpDtNC_nhtpkI7gXuJ1ipKz7AISMq3H3y5BATDRnrGPaPwJ-TJQ_qc4GGwTNFIZ7ou8G6U2-dLZuaYkqxZt3GCmZTCwnN1oCmrreWkEz79iemA9qhixrfJH_VRgEEK3ZH7oqnHlTwZ-dnhV5VnmC5wZlKVEHip0wl6j8FS9hG1x6rMN-aAEucvXvNLwsv7VAgP5WNyccdE1mrN-USzHz04im4YMOy9evrOHbkoajC5UgpGTiUbRaKo0Sw8jcheuc9hhxcowOQa7tPGba28_9CSBM-xpHChrguvVcTHh9cXRBE36G5A_SjhDDzHXVFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffb8ac635.mp4?token=HESMeHDRNk35BE8Ky-qHx4FhPpDtNC_nhtpkI7gXuJ1ipKz7AISMq3H3y5BATDRnrGPaPwJ-TJQ_qc4GGwTNFIZ7ou8G6U2-dLZuaYkqxZt3GCmZTCwnN1oCmrreWkEz79iemA9qhixrfJH_VRgEEK3ZH7oqnHlTwZ-dnhV5VnmC5wZlKVEHip0wl6j8FS9hG1x6rMN-aAEucvXvNLwsv7VAgP5WNyccdE1mrN-USzHz04im4YMOy9evrOHbkoajC5UgpGTiUbRaKo0Sw8jcheuc9hhxcowOQa7tPGba28_9CSBM-xpHChrguvVcTHh9cXRBE36G5A_SjhDDzHXVFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه:  باید برابری حاکمیتی و جایگاه بین‌المللی برابرِ مردم ترک‌تبار قبرس به رسمیت شناخته شود و به انزوای غیرانسانی که بر آن‌ها تحمیل شده است، سرانجام پایان داده شود.  از جامعه جهانی می‌خواهم که «جمهوری ترک قبرس شمالی» را به رسمیت…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21110" target="_blank">📅 20:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21109">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گویا اعراب به دنبال فراهم کردن شرایط دیدار حضوری پزشکیان با قاتل امام شهید هستند.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21109" target="_blank">📅 20:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21108">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آکسیوس:   تا ساعاتی دیگر جلسه‌ای بسیار مهم و سرنوشت ساز در نیویورک میان ترامپ و سران کشور های عربی خلیج فارس در مورد ادامه جنگ با ایران برگزار خواهد شد</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21108" target="_blank">📅 20:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21107">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آکسیوس:
تا ساعاتی دیگر جلسه‌ای بسیار مهم و سرنوشت ساز در نیویورک میان ترامپ و سران کشور های عربی خلیج فارس در مورد ادامه جنگ با ایران برگزار خواهد شد</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SBoxxx/21107" target="_blank">📅 20:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21106">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه:
باید برابری حاکمیتی و جایگاه بین‌المللی برابرِ مردم ترک‌تبار قبرس به رسمیت شناخته شود و به انزوای غیرانسانی که بر آن‌ها تحمیل شده است، سرانجام پایان داده شود.
از جامعه جهانی می‌خواهم که «جمهوری ترک قبرس شمالی» را به رسمیت بشناسد و روابط سیاسی، دیپلماتیک و اقتصادی با آن برقرار کند.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21106" target="_blank">📅 19:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21105">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">صحبت های ترامپ درباره ایران !  یا توافق می‌کنند یا جوری جمهوری اسلامی را نابود کرده و آنها را میکشم که نتوانند به هیچ مردم یا کشوری آسیب بزنند</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21105" target="_blank">📅 19:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21104">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adfd4dd3.mp4?token=ugldCl-iC8n648lqqqAubVHGn2rmNCqXKnw8JhsTxHROD-6IaDPCVJ2OZcgqHRyswasX5bjoBoAJrsx7j2qLVHxQDuu2olXYEM-MaSl4CvaC164A2zgz8G7nRDax1-vtwXPxJM4HhB80ZP-40haBmB0nHIZS0lSnoK5bFMpS5967j5r2SwmtESMHVtfFAHHJrWg_NIyPmQJVI0BTsOP8K7A5kBIF2rykFYWjcqXkWh4iMp3L0zUFEjVu8BnIkx0DEmXXlUkI0d-SGqDpNiWW78owA6UyboDRKCiO-wB72ihxkmSrvjjtR5Eo65k0KaoburC5-JDXP7DErDpFp8cZLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adfd4dd3.mp4?token=ugldCl-iC8n648lqqqAubVHGn2rmNCqXKnw8JhsTxHROD-6IaDPCVJ2OZcgqHRyswasX5bjoBoAJrsx7j2qLVHxQDuu2olXYEM-MaSl4CvaC164A2zgz8G7nRDax1-vtwXPxJM4HhB80ZP-40haBmB0nHIZS0lSnoK5bFMpS5967j5r2SwmtESMHVtfFAHHJrWg_NIyPmQJVI0BTsOP8K7A5kBIF2rykFYWjcqXkWh4iMp3L0zUFEjVu8BnIkx0DEmXXlUkI0d-SGqDpNiWW78owA6UyboDRKCiO-wB72ihxkmSrvjjtR5Eo65k0KaoburC5-JDXP7DErDpFp8cZLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های ترامپ درباره ایران !
یا توافق می‌کنند یا جوری جمهوری اسلامی را نابود کرده و آنها را میکشم که نتوانند به هیچ مردم یا کشوری آسیب بزنند</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SBoxxx/21104" target="_blank">📅 19:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21103">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ:
در ۱۲ ماه گذشته ۱.۵ تریلیون دلار در ارتش ایالات متحده سرمایه‌گذاری شد.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21103" target="_blank">📅 18:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21102">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یک مقام عراقی به الجزیره:
«به فرودگاه‌های عراقی اکنون دستور داده شده‌ است از فرود هواپیماهای ایرانی، از نیمه‌شب امشب، جلوگیری کنند.
اقدامات انجام‌شده علیه هواپیماهای ایرانی مطابق با تحریم‌های ایالات متحده است».</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21102" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21101">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ولی من هر چه میشمرم، رفع محاصره یک شرط است نه ۷ شرط !</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21101" target="_blank">📅 15:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21100">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">— مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ترامپ آمادگی دیدار با پزشکیان را دارد، اما باید بدانیم که تصمیم‌گیرنده نهایی در ایران رهبر معظم است و او یک روحانی شیعه افراطی است».</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21100" target="_blank">📅 15:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21099">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">به نظر من نوعی کرنش در برابر چین از سمت ایران است که نشان بدهد برای حرف چینی ها تره خورد می کند. چین روابط مستحکمی با سعودی دارد و همین چند روز پیش هم مشخص شد موشک های بالستیک DF-21 در اختیار سعودی قرار داده که با آنها یمن را می زند.  در آستانه دیدار رهبر…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21099" target="_blank">📅 14:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21098">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سخنگوی سپاه:   اگر مصلحت ملی ما ایجاب کند که در کنار جنگ، مذاکراتی انجام دهیم، باید مذاکره کنیم</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21098" target="_blank">📅 14:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21097">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 28</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21097" target="_blank">📅 14:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21096">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 28</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/21096" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 28
سه شنبه 22 سپتامبر  2026</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/SBoxxx/21096" target="_blank">📅 13:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21095">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">— شرکت هواپیمایی ترکیش ایرلاینز، به همراه پگاسوس و ای‌جت، از ۲۱ سپتامبر تمام پروازهای خود به ایران را لغو کرده و حداقل تا مارس ۲۰۲۷ هیچ رزرو بلیطی در دسترس نیست.
تحریم‌های «عملیات سرد اقتصادی» ایالات متحده آنقدر گسترده است که حتی هواپیماهای ایرباس حاوی قطعات ساخت آمریکا را نیز شامل می‌شود و برای شرکت‌های هواپیمایی ترکیه چاره‌ای باقی نمی‌گذارد.
شرکت هواپیمایی ایرانی ماهان ایر نیز پروازهای خود به استانبول و آنکارا را به حالت تعلیق درآورده است.
اسکات بسنت، وزیر خزانه‌داری ایالات متحده، گفت که خطوط هوایی ایران از ۲۳ سپتامبر با تعطیلی جهانی مواجه خواهند شد و هشدار داد که شرکت‌هایی که به آنها خدمات ارائه می‌دهند، ممکن است در معرض خطر از دست دادن دسترسی به سیستم دلار آمریکا قرار گیرند.
ترکیه یکی از آخرین مسیرهای هوایی بین‌المللی مهم موجود برای ایرانیان بود.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21095" target="_blank">📅 13:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21094">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ولی من هر چه میشمرم، رفع محاصره یک شرط است نه ۷ شرط !</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/21094" target="_blank">📅 12:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21093">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lT1ku1LA3ynqMaF6d2vVhC6BteCSxUfuIkLP4qyEcaUB-GS2QckB9jSMNd0weDfnZV2s6n9jY1TTAqm7Kb2uwnhcamr8PKTZDmateYOU6MpgQWChZ9ZpekerWKSKodXbndKfb2B6X1bqOUAqPSlYqPWT6Kn8IUS-eU0-JPB9J-C6OkNp4g-cf-_E08akJg2clnxR6gB8GuAOIjj8_hjZZBp6pkFL14D81Oh0pep4oUrbU_xRcrCMrQFwAq_2rXgHaMVTMiqfF9Nm7J5MwnnV_55bitDT-YVRGSHsp67u06npklYowmyv9s0DJk9B48j5wl2QtcV0TNXfhVNdjvpfVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران می‌گوید تنگه هرمز را مشروط به رفع محاصره ظرف ۷ روز بازگشایی می کند.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21093" target="_blank">📅 12:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21092">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6xOkH7DNo3CLrhRiL6jJU6Tbx2eY2I-5TWTi9pCJF3VVD8KFI2PgsckZmKXjTNxBwM8sBODCMBkRXgkBfASZPOQfW7j056bcjoZgwftlWY2nlNi-kpUMhg4YBaGzdYy-UU5JA_lZaT_RNoaKTffOjBJjPffG74DdnYuYHT-oP1OxjAbyDiAGT1C_imcJwXTDNqoo3UqY0KQvt7gapGRNBjfoyS9Mvx0jy37cPMb9BQKsuiEaVTv0MuINQ8ddCrkcKQkZjHBL5p_ozvbNfh1fq0_DcpSrph75MFtix4xDLvTALzwKbKZ5NfHc7ioZgnLGAayPmElinNdG9bxEmITVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه کله پوک پیمان مکه کم بودند، حالا وزیرخارجه مصر فقیر (خر دوم از راست) را هم با آن ریخت و ترکیب ش add to group  کردند!
فقط سیس هاکون فیدان !</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/21092" target="_blank">📅 12:41 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
