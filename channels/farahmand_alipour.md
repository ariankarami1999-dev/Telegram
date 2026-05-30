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
<img src="https://cdn4.telesco.pe/file/AXlvdrAnLa_Bmc-Mz2IUu5H4FAG_D6rgD4SHpQPszXh6uYBQrLQG2LZmWouIVEDdkZj_t4-_78HbiBaeZbSUH4MAuEilOAQHsvYyZ8kZtLDbshw_BLfDMpaeAuRU-VXoFIeC7pEbKSSc9ab6fIAwfj0_FQNO1yKkfl_tu3kguyTYqWZm4PSlcX3NOOSLQGLszxspklEMvI0SoIg4tNeuK1ir98lgf2fK7iC1y0gjituSoVzbHnZq-zd-zRVJaIAfitbL6Dl0C8YksHTSRXCPiMFEYAQUCcSb-YFw3e--1maLCgSd1bDv6QFPaZZ6Mm4_QPT05QNCpz1V--VCpGTr-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 13:51:29</div>
<hr>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-2FYTo4tNQZdQjV9-gto5SwhM0Z4KjxOKs9KyHxGQ1mFJM7g2rS6NPryq1aRPVfjN3O6APqmNkIP7h1lM4KZbJHkRO6Obsnmnlsqd1xbz-Gevain3RXHz7KCPHSzen8KgesZAhTk7qtzeqqPnVxT1UiizLOnJwK1AGrf4LJdG4Wmq4wYRF3WaUBhgmRhXwlEE4aVrwSsNxG5KVVmGykqzck9W7qpgz1-lOAT9qw-Y0YFoXTWYokvHSwGVuo2AuePEMXuzcCM8mtybO7zhZBBTGHgeB6XYrtJMPCm8TxQ4Tl7ksQ91N-uEmNX5S4UO_PHAhtXOYY5gc4-aP03UU2xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی با آب و تاب می‌گفت
به امارات حمله موشکی و پهپادی کرده،
حملاتی که ۹۵ درصدشون توسط
سیستم دفاعی امارات خنثی میشدن!
اما امارات در عوض پنهانی با جنگنده‌هاش
حمله می‌کرد و جمهوری اسلامی هیچ سیستم تدافعی نداشت!
یعنی اگه به ایران ۱۰۰ جنگنده، یا ۱۰۰ موشک حمله می‌کرد، میشه با اطمینان گفت ۹۹٪ ماموریتشون
رو انجام میدادن و اهدافشون رو میزدن!
کما اینکه اسرائیل ۸۵۰۰ سورتی پرواز در آسمان ایران انجام داد حتی یک هواپیماش آسیبی ندید.
آمریکا هم ۱۳ هزار سورتی پرواز انجام داد.
آمریکا همچنین ۱۰۰۰ موشک تاهاماک به ایران شلیک کرد، جمهوری اسلامی قادر نبود حتی جلوی یکی از اونها رو بگیره! یک در هزار رو هم‌ نتونست!
جنگ با امارات رو جمهوری اسلامی کلید زد
و هنوز هم کامل مشخص نشده چه آسیب‌هایی
ایران در این جنگ متحمل شده!</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/5206" target="_blank">📅 10:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyvzrqol1jfG0LMkc_tnkyeD56cY09VswK7gySi62alPzQy3_i4yheTZm5oCYTIKcRGtwIWoOYAVYjIDMuZ7VAqAQO8ipx2IOEAeGWeJCugmip2XAQNKt2IgHbg8hOcM8GZQPhKtzzHQ2gC6nud10zHBOYOgI6xRIREPDKUWaWSMLXZ6O-syZ83M27E_sDNmgjFnyVYLb3TENvu2g3qqB9ALdxAr-bWu-Y-Ke8_1mMaXtLxvEPg8pYnvQK3knmv79KADMQ3jQoaK9Y8ApWMLdAvfklmeb0FOj9VoqQr5ObxjehAzHZiTviNKdiLh2fLPNnRrQAgN2oLk94QaCcMCvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5204" target="_blank">📅 21:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX46z-Zl_bUQ96FCDfakt8VmPjUTxZc-gqaMVdTXF0XYwicLx-KBp9-MAAV_o5hBRB0Cm2-WxyNM3OcWANCZYCvpWNHGuTRMy8abB_JMQ54EVIG68YHt-BXD09Sw1c_ZQbFc490EtJaKwQ8okJPOITPdQKbalQDda_DMof-UTSZ-H5w9VHSBjRHfhknn-pBg3XxMlw26nUTWhoI852z5DzRCgeBukEDG-kCpuqxnHVrN0qaV63JNveb1P_eS993dn1ZfDoc_FAcoE1y4zCe4khOXxVip4VAHRK4AGiT5FaiJ7lbt4QxqmJMn0zZFL5RE0RM3cFQzCAsNKzuZDXI-fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح یک دیوار در تهران و گفتن از نابودی اسرائیل در ۱۵ سال آینده!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5203" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6FfAkHOJVdA2HJC1hXZ97SoBO6uRKXbfY2UzvFWnlMInEJ5h4wnwcqeIZQSGhoM_FM4X2fK9dgAnwGxwrcFgmx6T-bynjERrc3c5YjPeqeRMIpJyUNHBjIRuVBsJNOkSHGMgKOQXBGZP6IlTdxFO5W3n4mroiWXVhMniu3La79ldfTgML9Xf-SShv2ZSXALjvuTBpiwoNwO6GvZaGyML_6Ztb9-6Fpd4dkWpaJ3xg7DEGKgdZceFOw1YPQ4DLQHDFFDhJUdbNAR-IlRnwZg7CRU47CBszHE35kU4favY2Q7sRTdYN-z0WaxYzPm0NvHkAiwJch4kMbf-H4Qq74LkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادگی بهتر برای جنگ بعدی …</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5202" target="_blank">📅 18:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : برای اتخاذ تصمیم نهایی اکنون به اتاق وضعیت می‌روم.
«ایران باید موافقت کند که هرگز به سلاح یا بمب هسته‌ای دست نخواهد یافت.
تنگه هرمز باید فوراً باز شود؛ بدون دریافت هیچ‌گونه عوارض یا هزینه‌ای، و رفت‌وآمد کشتی‌ها در هر دو جهت به‌صورت آزاد و بدون محدودیت انجام گیرد.
تمام مین‌های دریایی (بمب‌ها)، در صورت وجود، باید از بین برده شوند. ما با استفاده از تجهیزات پیشرفته مین‌روب زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده را جمع‌آوری یا منفجر کند؛ البته تعداد آن‌ها زیاد نخواهد بود.
کشتی‌هایی که به دلیل محاصره دریایی بی‌سابقه و فوق‌العاده ما در تنگه متوقف شده‌اند ــ محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند بازگشت به خانه را آغاز کنند!
از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده‌اند ــ زیر کوه‌هایی که تقریباً در نتیجه حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند ــ توسط ایالات متحده از زیر زمین بیرون آورده خواهند شد. (طبق توافق، تنها آمریکا و چین توانایی فنی انجام چنین کاری را دارند.)
این عملیات با هماهنگی نزدیک جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و این مواد به طور کامل نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی میان طرف‌ها رد و بدل نخواهد شد.
در مورد سایر موضوعات ــ که اهمیت بسیار کمتری دارند ــ نیز توافق حاصل شده است.
اکنون برای اتخاذ تصمیم نهایی به اتاق وضعیت می‌روم.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5201" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E97e-ybw3Pw5Xg235io7lCb1LKIB-_C7LMim_K7iGiPKtygGnOYX97zUMIm4_DoeWsLiCGYcV5Jl0zruXHFnzlyOZvFkfjiOUtxwljCtVAKxUibqNnhIyKRo_ExBKDpIF4w7S_VPdafshn01e6Xx90GtCCVLcg-uzxToMUruPZls3g25YKCX9yW9YbRTsK21s9qz6jS8biEI5wJbpMNPmzizgk4o6LNtnyGU6mOcDOpAP-7E2FiX45HgnbO-9WSc9JRtNm7cQUXBX84iys3b-o2bMXaP8JDv1qc0txs1-49sNlXxvG67aNkwKeehuFTpW2hU5PStjuYqr3aYW7Uc1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wz20MFN_mcpc3Y152zaxEj2ybeGeave3YdTTTO4hGKLki2_QGE0o6kmot9aHzQ8Qw8JT8jvCK30XA_XgQXAqPp9g8LI121X2Mzu9VX3lf5jeEqYjI--pdQkCydcveAoUc0mN0uNdHQkggJ9BApXUnFvL53CHdgQ7vjGMw9k3fKZl9QmBNp78e7gqX2EQioNzSnycs7CvsNK0o2w1CrNdbkZFIyZZYv6q1M6zwv6Y0ec6AkSM1G6kmvmW_RHwnhaOaexxTofCi8O6Pmn-bh6Wygq2uj2tBBxT8s8quOHdGKPmESVaWP6w3ocjIGHMnBmUvPl_Gql-z48hVtgUU1UsQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
لبنان سفیر جمهوری اسلامی رو اخراج کرد!
گفت «عنصر نامطلوبه»! گفت که جمهوری اسلامی عامل وقوع جنگ در لبنان شده و جنگ
رو به مردم لبنان تحمیل کرده.
اما سفیر جمهوری اسلامی در درون سفارت خانه موند و گفت برنمیگردم ایران!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5199" target="_blank">📅 18:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IjQ7PCnJhOx8TwfAaZ3_6l7Yzh7TpgmQxNncHSckGd5COzf-k0kJxAhoUWNYR-zESKlKjJSY5X0gDx2fVTedNrMGW3GvVAQwLdFSOsZadl-zxQqzA4MGw0Nj_At0720cjrW9lnGuGfbyL2gdWPH5WJGsW7jumKNtOUyd5GbQJt08g7BCA6xtSDyXkbpJVDL_V0xakglW5lQo_vvI_Fc2GX6VyOyu-Hnm0G3kq-gKFvQ-ObUkRiOM6U4bMhNeNsMA-EEys-j-cJqpiK6nMJJrq-lfXDwz5IulQzt1q4gPtf09FZNsAkgaa8_nSIgARPtYpGIpJ_m7jh8NXU_rDrcIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/br13uVRb3SFFeaGRcVhImJ6MagK1i9dmvBlr5w6pajhUDnQJeBCT4C1rm-10f-ymKcQFs_rbUhIYGRopzlXA5e6oOiawDuKy5qOxV3SSiiBb0WX0GCqt24rUnc1NQ_-oixv8On3ye3IxGy8gvqxN38DSg_Wl-EN7gjlzAxR6UFAieA55VmzsS9v0_-qYkJPbATAzyehaEOm3jwG7jqtz-b0regKy2dGIz3DnPgdf6A4nXRXjvCFcBM0RpziWWh_w21qc365VmWcIk_ItjcYen-Rfn8eBLOhIcQI0C0gKkKzUgjR6BNDUI953ANlvFCqbmLg635rzFYTZvzh4CwDXkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
درسته هر شب توی خیابون‌ها بزن و برقص و عروسی داشتن اما در افغانستان گدایی پول میکردن :)
سفارت جمهوری اسلامی در کابل در اواخر اسفندماه رسما تقاضا کرد که  مردم افغانستان به جمهوری اسلامی کمک مالی کنن!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5197" target="_blank">📅 13:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=vc58TESrB19SXcX22JDquOHN5mr9e_0xTLmO0xEXhTPl3TnBv1myvM6tgehgUnhwnlZGiU90S17cFbu1-OXRZTwWf976s8_DCPRxkI3Q8kGPVyKb9_j99wGZ8GUSFzSmcRZh01ncbbOnupLZa0KJeFn0j4tWo7p4V2y2A2QbvWqcAm8edlWTtVZWi1-A8BbVOcM8pVRJUfvEBr1hi-H4ZOeCGc6capNagQgs0B8sVhD9Yk_eonMNR7JVGB8wq-4QrV8cWL-6xOkt0Fd8GQn95qtKuC5mOATMQXbDgsG5z_ENMAg8nMXpTujiLsKB9_5u6anIQOFay2xcjUAHLT4gng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fac9d6ff.mp4?token=vc58TESrB19SXcX22JDquOHN5mr9e_0xTLmO0xEXhTPl3TnBv1myvM6tgehgUnhwnlZGiU90S17cFbu1-OXRZTwWf976s8_DCPRxkI3Q8kGPVyKb9_j99wGZ8GUSFzSmcRZh01ncbbOnupLZa0KJeFn0j4tWo7p4V2y2A2QbvWqcAm8edlWTtVZWi1-A8BbVOcM8pVRJUfvEBr1hi-H4ZOeCGc6capNagQgs0B8sVhD9Yk_eonMNR7JVGB8wq-4QrV8cWL-6xOkt0Fd8GQn95qtKuC5mOATMQXbDgsG5z_ENMAg8nMXpTujiLsKB9_5u6anIQOFay2xcjUAHLT4gng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید در اجتماعات حکومتی شون هر شب عروسی داشتن!  «صیغه یک ماهه»! در برابر «یک سکه» :)  با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5196" target="_blank">📅 13:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=PiI8ZQuEEAK2i9vZU-fq2Xgl-fwbNl2gJ4Y6DOCciyteSi78Al2wTuI9ae-gD7hdjnqYzETj5R4f3EKVDLCIA5jaF9r_khJPXc_ZT5H3TrZRaVSyLA2g31dxb8SEX1oemsSktgzBSWRBrwW50DxZMzCcMMKU4CK54-Jlu-tnfKVUluSVw1Xdh8mS82DW7Aog5qqtU-DDsFr4FPcKp85J1LEdOSgT503CxllIQNDkTeDAg7JfGrPcHX9krOP31e4fkMZ7sysf64zbye2YxC05CdaPeOtQY2S98Bv3R_v3ESCARUVj7PB2xsjsS98LPgMFHyqPDfrXQbTvvqsu-pZdDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f5663381.mp4?token=PiI8ZQuEEAK2i9vZU-fq2Xgl-fwbNl2gJ4Y6DOCciyteSi78Al2wTuI9ae-gD7hdjnqYzETj5R4f3EKVDLCIA5jaF9r_khJPXc_ZT5H3TrZRaVSyLA2g31dxb8SEX1oemsSktgzBSWRBrwW50DxZMzCcMMKU4CK54-Jlu-tnfKVUluSVw1Xdh8mS82DW7Aog5qqtU-DDsFr4FPcKp85J1LEdOSgT503CxllIQNDkTeDAg7JfGrPcHX9krOP31e4fkMZ7sysf64zbye2YxC05CdaPeOtQY2S98Bv3R_v3ESCARUVj7PB2xsjsS98LPgMFHyqPDfrXQbTvvqsu-pZdDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی شما نبودید
در اجتماعات حکومتی شون
هر شب عروسی داشتن!
«صیغه یک ماهه»! در برابر «یک سکه» :)
با کسب اجازه از امام زمان</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5195" target="_blank">📅 13:18 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وقتی شما نبودید پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،  پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!  حتی زودتر از پیام‌ شهردار تهران!  حتی زودتر از پیام جوادی آملی :)   پوتین در پیامش نوشته بود :…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5194" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XyuMfEoyjh4YhZ12nVvdV111H8UmLpS8iCUCtRqDOJwS_1Qinnqcm4bG5he5AnQlbfbtGzPCALD1FdeXOk8eQhZasIhjaie4CC2fvCU9vojt3ooVEPjG8kz34Cm38Ji-ADDHhQ6Ixq3E2Yw-kegJ7unfHss2nQQIJUokBUkV7IJXrIJPlUb39jfwEoDT-84xkHf_heTCxjDRfEcKvlv2r8otI7cIx1kqJJszRtyaR5Re7l553B5YPXkpmQfZHfgr1276M4ZqkIs8jwvi1fI8LDKGiA8tEin1LZqW8QeJ-44QMIww0Y6k3fcPEZAMG8kKr3vzlSnqTFtqk7QCULi3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FIkgZ9ZunmeloGe6y83qCP-9VUn7z1rkgZ0lbEJzfG9hjMlyVLC-wGj-04ppx7eHYWbPvc29s4bQ2MnGvOuwNmARTsxsoJ2md2d4xJ5sYnOxhdaev8ZXzfyEvtgWb3REaRcIgaJEhxE6gS9teDDKjeRrl1thLrH_QAz1DhZjKIdrlKSWsq743HNaHDcL_I62xZLLtARCa1CTrLRxFhIcr-PwzQvORJuFfJ7bs1ijgLeJHSFwE2XXnJWEnxHmgJ7-iuzYbKqwsBK_hB0jRfZcEfSMNNVe57JjerAw3P4a0iDi00SDVm37rsnGxXcFJD_0Gzg25i0UaswisrzhrZQ06w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی شما نبودید
پوتین پیام تبریک برای مجتبی خامنه‌ای به عنوان رهبر جدید جمهوری اسلامی فرستاد،
پیام پوتین حتی قبل از پیام گروه تروریستی حزب‌الله لبنان صادر شد!
حتی زودتر از پیام‌ شهردار تهران!
حتی زودتر از پیام جوادی آملی :)
پوتین در پیامش نوشته بود :
«اطمینان دارم شما راه پدرتان
را با افتخار ادامه خواهید داد.»
پوتین راه پدر مجتبی خامنه‌ای رو دوست داره :)</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5192" target="_blank">📅 12:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=ShnVZxmkxslZ7zchFV8EPMj9a9SnU0v4KUhUwnH5nTdsKZYC8kkHLZCvB9KLYGRTASA6MWBzftw7bOwLMN4FE_wM0urwAWhm2NUZWYiAqwdcj-NdZCwg4JKsfHgJ2bsZTErSD5tGK--LIXK-KuzV7qqj6t_QZQ-mpXw2wfi0StijRC__MsLL4aakLf5Wr5Dj0BH2lButzaddTZrSwq8EeDxVslO56PH-RYzIrkjfclSbNrYjFgjNGdzF4Ij5vvHZ5L7GlwzGvHMt8ptm58e0x1gDSAnOCc6HGgxtecSDkSd6UqC6SLMkBRYM6K5umD7nEs_fNYY-2FILHQxtiWwDGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9993037d5c.mp4?token=ShnVZxmkxslZ7zchFV8EPMj9a9SnU0v4KUhUwnH5nTdsKZYC8kkHLZCvB9KLYGRTASA6MWBzftw7bOwLMN4FE_wM0urwAWhm2NUZWYiAqwdcj-NdZCwg4JKsfHgJ2bsZTErSD5tGK--LIXK-KuzV7qqj6t_QZQ-mpXw2wfi0StijRC__MsLL4aakLf5Wr5Dj0BH2lButzaddTZrSwq8EeDxVslO56PH-RYzIrkjfclSbNrYjFgjNGdzF4Ij5vvHZ5L7GlwzGvHMt8ptm58e0x1gDSAnOCc6HGgxtecSDkSd6UqC6SLMkBRYM6K5umD7nEs_fNYY-2FILHQxtiWwDGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم مشهد از خبر کشته شدن خامنه‌ای</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5191" target="_blank">📅 12:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdrH6xB_gqYgkfyLri2Q06i4ZrBZGEotYDgRW1Mm-Uc4X6FMSYJxcXaq25WTJLkE2crRPSs9q98LscVWxT0YmotlGNGzdbCOEkvpY0dtSjxvDen2OtdRVC35YoEs0O8VqRcFS-ZGrhsQiXymeh6uvJFwKAozVIWZHUc5WIsxfzbBd7SB6UWOiF-zRdu8qpD5iOgiiW7yO-s7Par1ObFAVK25d1GmtzJ9h7HXqTxKWsszyvKlVwRbSLiZgH7oxGeM1bj4-WJMTFAZkoSa395L0p4DtXNZPQnjfc9qjoFbWM7eH2fLFKQFwXpKMDToL6JXydlsLJTFCBmiciweuA9Ogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نکته جالب :)  امروز ۲۶ روز پس از کشته شدن خامنه‌ای  در کره شمالی هنوز خبر کشته شدن خامنه‌ای منتشر نشده!  فقط اعلام شد که مجتبی خامنه‌ای،  پسرش جایگزین او شده،  اما اعلام نشده که در طی یک حمله نظامی  خامنه‌ای کشته‌ شده.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5190" target="_blank">📅 11:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏حالا که تشریف آوردید:
‏از ۵۷ کشور اسلامی، فقط ۸ دولت کشته شدن «ولی امر مسلمین» رو تسلیت گفتن و ۴۹ کشور سکوت کردن!
‏عراق، آذربایجان، تاجیکستان، پاکستان، لبنان، الجزایر، عمان و قطر تنها کشورهایی بودند که تسلیت گفتند.
‏بزرگان جهان اسلام چون‌: ترکیه، عربستان، اندونزی، مصر، مالزی،ازبکستان و… سکوت کردن!
‏تروریست‌های طالبان هم حمله رو محکوم کردن اما تسلیت نگفتن!
دولت فلسطین حتی حمله رو هم‌ محکوم نکرد! سکوت کامل!
فقط تروریست‌های حماس محکوم کردن و تسلیت گفتن!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5189" target="_blank">📅 11:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
امروز : کشته شدن ۱۴ نیر‌وی سپاه زنجان بر اثر انفجار مهمات عمل‌نکرده</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5188" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5187">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
رسانه‌های جمهوری اسلامی  از بستن تنگه هرمز خبر می‌دهند.
🚨
🚨
🚨
سخنگوی قرارگاه خاتم : به ۱۴ پایگاه نظامی آمریکا حمله کردیم و «صدها» ‌تن آمریکایی و اسرائیلی را کشته‌ایم.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5187" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5186">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پایکوبی مردم در تهران</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5186" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔺
شادی مردم ایران از شنیدن  خبر مرگ خامنه‌ای
🔺
بیانیه رسمی دولت اسرائیل تا دقایقی دیگر</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5185" target="_blank">📅 10:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حمله به بحرین
😅</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5184" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شاهکار جدید صدا و سیما  اینها رو باید تلوزیون‌های جهان در بخش سرگرمی نشون بدن</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5183" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">«دیشب مردم تهران در کوچه و خیابان  کل می‌کشیدن» مرسی از بابت این اعتراف و این مستند سازی از وضعیت تهران پس از انتشار خبر مرگ خامنه‌ای</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5182" target="_blank">📅 09:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=Oo5QHqkz2M04TXdSqJ5Tmhn3LZoTefhb8rNI4CSyVqcedjWXGIxTHFyAaQ6mVPaqcqUEzStp1DAsNI1LHCejvEcU3FUBO0eNNNQ_9xqcSZSM1kW4ZRhMYpxOFSKR8mqDXIw0Vml19H5jnBSLtbWkPO0GcgWWp43OO35kneDBm5HE31ozBZeRHYPLcArSZm4RFV4w4BQZC3eB36yFUi7tvy6KlxefvmwynyDVnBoKaFFr8bBzRrmTJpTnnYtwt7Whj2lGSD6AmLpmWgBShspzeq2vkT7jvpqiRiEXU-JUxzP_E76kh85AfbhkisPz4AvyfB4jlLxJXQZ_8sclNDWsNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83519ba27a.mp4?token=Oo5QHqkz2M04TXdSqJ5Tmhn3LZoTefhb8rNI4CSyVqcedjWXGIxTHFyAaQ6mVPaqcqUEzStp1DAsNI1LHCejvEcU3FUBO0eNNNQ_9xqcSZSM1kW4ZRhMYpxOFSKR8mqDXIw0Vml19H5jnBSLtbWkPO0GcgWWp43OO35kneDBm5HE31ozBZeRHYPLcArSZm4RFV4w4BQZC3eB36yFUi7tvy6KlxefvmwynyDVnBoKaFFr8bBzRrmTJpTnnYtwt7Whj2lGSD6AmLpmWgBShspzeq2vkT7jvpqiRiEXU-JUxzP_E76kh85AfbhkisPz4AvyfB4jlLxJXQZ_8sclNDWsNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس پاکستان داره عزاداران خامنه‌ای رو با چوب میزنه  دیروز هم پلیس پاکستان ۶ تاشون رو کشت.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5181" target="_blank">📅 09:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بخش خبری ساعت ۱۴ شبکه یک و تکرار ادعای زدن ۳ جنگنده آمریکایی  در آسمان کویت و تکرار این سوال که چطور در آسمان ایران به این پهناوری نمی‌تونید ‌، در آسمان کویت تونستید؟؟</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5180" target="_blank">📅 09:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فرماندار جم در استان بوشهر، می‌گوید که یک «پهپاد متخاصم» منهدم شده و وضعیت شهر به حالت عادی بازگشته است.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5179" target="_blank">📅 00:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از شلیک موشک از منطقه جم بوشهر به سمت چند کشتی که در تلاش برای عبور از تنگه هرمز بودند.
گفته می‌شود در جریان این حملات موشکی که از سوی سپاه صورت گرفته، به سوی یک کشتی آمریکایی نیز شلیک شده.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5178" target="_blank">📅 23:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=MELARSZSCa2c3XCf2hsgI-pzGiZSxrxosFXwB8fRPtSk3f5N7pr7abOhEM9w8SlwMq7Kzx_g4wO_j0Wg3FEfPWu1SBG-Iwm7lLaEmuPffEQAD0nNuVgY43hgttdbPfNFPmsthIcMXQe56enpHlh-kN5p91WNsxukXjptwThW9UXwn3d5ICJ_DaANJDCwh3Q9QcqfUVBeywZrq91FjKdqKox7eo42f7EOvsOzUsDDuphLqWcAkVrhBtQxPJ260RdQMdJZYAhOMWMdBePA4TOqsW_jR8GXNMNu9n3dXWk8mm-oLZ64iA_R1rsQIm6m2KIDj62Xi8IhXmmTOF1kQ3Rd1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7730b3f12b.mp4?token=MELARSZSCa2c3XCf2hsgI-pzGiZSxrxosFXwB8fRPtSk3f5N7pr7abOhEM9w8SlwMq7Kzx_g4wO_j0Wg3FEfPWu1SBG-Iwm7lLaEmuPffEQAD0nNuVgY43hgttdbPfNFPmsthIcMXQe56enpHlh-kN5p91WNsxukXjptwThW9UXwn3d5ICJ_DaANJDCwh3Q9QcqfUVBeywZrq91FjKdqKox7eo42f7EOvsOzUsDDuphLqWcAkVrhBtQxPJ260RdQMdJZYAhOMWMdBePA4TOqsW_jR8GXNMNu9n3dXWk8mm-oLZ64iA_R1rsQIm6m2KIDj62Xi8IhXmmTOF1kQ3Rd1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف رهبر شهیدش رو پاره کردن :)</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5177" target="_blank">📅 20:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=U4z79j1BpNABQjNAGAe4Tw_Q99EpC5u7VNx_h2yhEjV14CXKiniBB5cjiYmJH8ZetJzN-IgGIwfBl1HYY3n2aI5vEbviuWsjoPbByejYw52WN1LLe2OBRGXFPMKjlfUx90rY630tyXDTLRm2B6ZUC1ac9pjlBBUYPvIN8klmExN1dZE5W7qrx66uBsbXEiid2rzRcUldzWQ3u0_-Q0zt2lIs3b1998kWdq970Rm1-91c_ugLyINIdQLA_EYZRxeSk050v-9_rQwhAnHXSOmaeMnyK1CMptwScOEhWADcFygD40ouJREnc-rzMeSDT2gg18DkpAziL05UndTIGt1Bng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbac44461.mp4?token=U4z79j1BpNABQjNAGAe4Tw_Q99EpC5u7VNx_h2yhEjV14CXKiniBB5cjiYmJH8ZetJzN-IgGIwfBl1HYY3n2aI5vEbviuWsjoPbByejYw52WN1LLe2OBRGXFPMKjlfUx90rY630tyXDTLRm2B6ZUC1ac9pjlBBUYPvIN8klmExN1dZE5W7qrx66uBsbXEiid2rzRcUldzWQ3u0_-Q0zt2lIs3b1998kWdq970Rm1-91c_ugLyINIdQLA_EYZRxeSk050v-9_rQwhAnHXSOmaeMnyK1CMptwScOEhWADcFygD40ouJREnc-rzMeSDT2gg18DkpAziL05UndTIGt1Bng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از ۹۰ روز صدا و‌سیمای جمهوری اسلامی می‌پرسه در حمله به بیت کیا کشته شدن؟
کمیل خجسته، برادرزاده منصوره خجسته باقرزاده، همسر علی خامنه‌ای، میگه  افراد خانواده خامنه‌ای که کشته شدند، همه در یک نقطه نبودن! در جاهای متفاوتی از منطقه بیت رهبری بودن که به همه اون جاها حمله شده.
این همون حمله‌ای است که پسر عبدالرحیم موسوی ،
رئیس ستاد کل نیروهای مسلح میگه ؛ ۳۰ روز گشتم و جسد رو پیدا نکردیم!
عجیبه در این حمله فقط مجتبی سالم مونده باشه!!
چرا خامنه‌ای در پناهگاه نبود
!؟</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5176" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
آمریکا و جمهوری اسلامی به یک توافق ۶۰ روزه رسیده‌اند تا آتش‌بس را تمدید کنند و مذاکرات درباره برنامه هسته‌ای را آغاز کنند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5175" target="_blank">📅 19:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/208f980645.mp4?token=v07zFKf_icT9UiljOd4I92lIOhE_iV69-rpFQJ5zBxbQPH3CaaWfiJp5s44Yl9nf0bzfuhCt3TbkVYI27ZTkLFsE4ji8T5Jm3n3W_7PE2LqbG4ug0LfVQ11wQxVvPRqVHDlqk5lE9FpT6Mm-4UYZANEGTJc9RvCtpsKs2YOGlIbNsqKh96BJOX6c9swfl7doQ30KlDybVtkd6LqT844ph_3IbWTLhw9iFhwdCW7hgx9xgiz6ikcCQoD0PzFnMKNzVljjRgkz0WUUO4TYW8AAOZH3DKA5WGENip2p63eCOiaZV4wUnhoDko4jNb1N3ilaz6PPCFHqgbgfsdEdQ2UqcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/208f980645.mp4?token=v07zFKf_icT9UiljOd4I92lIOhE_iV69-rpFQJ5zBxbQPH3CaaWfiJp5s44Yl9nf0bzfuhCt3TbkVYI27ZTkLFsE4ji8T5Jm3n3W_7PE2LqbG4ug0LfVQ11wQxVvPRqVHDlqk5lE9FpT6Mm-4UYZANEGTJc9RvCtpsKs2YOGlIbNsqKh96BJOX6c9swfl7doQ30KlDybVtkd6LqT844ph_3IbWTLhw9iFhwdCW7hgx9xgiz6ikcCQoD0PzFnMKNzVljjRgkz0WUUO4TYW8AAOZH3DKA5WGENip2p63eCOiaZV4wUnhoDko4jNb1N3ilaz6PPCFHqgbgfsdEdQ2UqcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش زدن ظریف :)
نوبت عراقچی هم میرسه!
این مسیر رو خیلی‌ها رفتن!
از منتظری و بنی‌صدر، تا موسوی،
خاتمی و روحانی، احمدی‌نژاد و…..</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5174" target="_blank">📅 19:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=no3LvxUcOin-wEgu2rMXZWjsOjIySlSPqXEm6GPoYaT_i-WAW39xuiM1dv3qRuNS8wfcvg0GzzAeJWZpLdBtzGn4nHrJ9lA-TQZUvxAzHdQvjbQrzMoILKYI14Nd58Ppdy7Pljg-lE1iqBjiSLYTH6r7CkLKHulryR_mVQ0jcu-HhKxVPpaRUiTLiazFiHUyQnB-9y5WdwfZt6nSzRVfykCeylQ2qyrrzsQeXOzG836kLkxlT27ND9TopYT88zl60mgX8SUpapxAGGinqdAHQQU3zhje0MnG8yjdImi7lh6ZZ_To9kzCCsp9toS6k-DIe7gmnO_rmf0Q6EjAnf2o6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b8458a9e.mp4?token=no3LvxUcOin-wEgu2rMXZWjsOjIySlSPqXEm6GPoYaT_i-WAW39xuiM1dv3qRuNS8wfcvg0GzzAeJWZpLdBtzGn4nHrJ9lA-TQZUvxAzHdQvjbQrzMoILKYI14Nd58Ppdy7Pljg-lE1iqBjiSLYTH6r7CkLKHulryR_mVQ0jcu-HhKxVPpaRUiTLiazFiHUyQnB-9y5WdwfZt6nSzRVfykCeylQ2qyrrzsQeXOzG836kLkxlT27ND9TopYT88zl60mgX8SUpapxAGGinqdAHQQU3zhje0MnG8yjdImi7lh6ZZ_To9kzCCsp9toS6k-DIe7gmnO_rmf0Q6EjAnf2o6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک مرد مسلمان چاقو به دست در محوطه یک ایستگاه قطار در سوئیس موجب زخمی شدن ۴ تن شد.
او با فریاد الله اکبر دست به این اقدام تروریستی زد.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5173" target="_blank">📅 14:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=PHxfyYTcxr3sqa6bTe97n5WT-aAeYoLgywn8y1xaM1mPclzwsjxKbx_vKiN14KwiL-Vg6Fhkv1R5YuVogT4PxS6RWZR9VC9Bk_M7iGgm0tmlYui8hA13RfgbpgSdk4XawTQmyXIq0h6_OkVeTEipYO5NW9zqX6F989BkmBV8LfBAiQ4-bfAYTM7Gg7EvzZUS7olqFnK083QKHSd86rySTqVa-BiV70RFxtYQckzc5ceoIsZA4opp_r7vS64K75FAAe5XGPjBDGHikj0uQPGY1zG61DaE2O7ntcHZWcSLqnwGowTTG--D1XhZVRH9_TyrFOfiXNm4lhH8rPZ6S0VRuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2527ef2.mp4?token=PHxfyYTcxr3sqa6bTe97n5WT-aAeYoLgywn8y1xaM1mPclzwsjxKbx_vKiN14KwiL-Vg6Fhkv1R5YuVogT4PxS6RWZR9VC9Bk_M7iGgm0tmlYui8hA13RfgbpgSdk4XawTQmyXIq0h6_OkVeTEipYO5NW9zqX6F989BkmBV8LfBAiQ4-bfAYTM7Gg7EvzZUS7olqFnK083QKHSd86rySTqVa-BiV70RFxtYQckzc5ceoIsZA4opp_r7vS64K75FAAe5XGPjBDGHikj0uQPGY1zG61DaE2O7ntcHZWcSLqnwGowTTG--D1XhZVRH9_TyrFOfiXNm4lhH8rPZ6S0VRuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله هوایی اسرائیل به بیروت
🔺
آمریکا از دولت اسرائیل خواسته بود تا به بیروت حمله نکند
🔺
گفته می‌شود که در جریان این حمله، «علی الحسینی» مسئول ارشد موشکی حزب‌الله لبنان، که در واقع یک عراقی است از «فرقه الامام حسین» از گروه‌های نیابتی جمهوری اسلامی در عراق، کشته شد.
🔺
اسرائیل دیروز هم در حمله‌ای به غزه، فرمانده تازه منصوب شده برای «گردان‌های قسام» (نیروهای نظامی گروه تروریستی حماس) را حذف کرد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5172" target="_blank">📅 14:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">علی الحسینی‌ از فرماندهان ارشد و مسئول واحد موشکی «فرقة الإمام الحسین» حز‌ب‌الله عراق در حملات امروز اسراییل به لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5171" target="_blank">📅 14:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaV42ZWlKMZOD8Rt9hLt80fcf0PHF4k0ZIRm7RFf6RFhMorB_w_Nh5-Q0KAG4D4lTbb5C_KppuhrSZO7dLlJoif28_xmO5L2oPW45yTTVAJhhBoKD_he-GGDhOlyry-V5g_vP5TndN3qLo8qwgg3IORjE2R9uiZaFsv7ohBUAORRNdPpQ1HXm8t5ZpWiex2nziq89ajISokG_eUEpIUEKw97j5Z8FmLpTaoVJ1mF0d5wTdf9FuQ8qBbjcf8jkro84yv4KP1wGUXvAcd17UvetszgsXyZPGZToCOK33Q_1f4xB5XJachSZILYBLMuYK-a9ihfml8lBq8NmgztmMCrig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام:
ساعت ۱۰:۱۷ شب به وقت شرقی آمریکا [۵:۴۷ صبح ایران] روز ۲۷ مه،
ایران یک موشک بالستیک به سمت کویت شلیک کرد که توسط نیروهای کویتی با موفقیت رهگیری و منهدم شد. این
نقض فاحش آتش‌بس
توسط رژیم ایران، چند ساعت پس از آن رخ داد که نیروهای ایرانی پنج پهپاد انتحاری را به پرواز درآوردند که تهدیدی جدی در تنگه هرمز و اطراف آن ایجاد کرده بودند.
همه پهپادها توسط نیروهای آمریکایی با موفقیت رهگیری شدند.
نیروهای آمریکایی همچنین از شلیک پهپاد ششم از یک مرکز کنترل زمینی ایرانی در بندرعباس جلوگیری کردند.
فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای همچنان هوشیار و با تدبیر عمل می‌کنند و به دفاع از نیروهای خود و منافع‌مان در برابر تجاوزات بی‌توجیه ایران ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5170" target="_blank">📅 14:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=da34OLPkW3VVaroHJp3Yobdy6o4soeCMDJL5YA87-8-tz-o4kn0jbAYFyu4fV2MWmeLI0L3Bnc8aiNwNwe-TZQ67cEQRpDPV6cubLIctzbsORtHfG_CGV7ESfOQjnWT0yC8nquzikMLJIGawF8naixNlPY8_IpAWweh7qO4JZfc5q-datWOkm1DApYFgcNWup_P9jG9yrXm-k0p0SZ7CTa36ObH65t22fNzZXmj_GGUcrR5KcBJnjb-TcjSA1c89xB1Ka-YcUo4gihBJ4UgPq5QwynVgktn75iGeqE0LiD_f-aip_P_LxOktpmfiDK63ZaTvtc7Go3qip6eaPB0ZxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7f2acbc1.mp4?token=da34OLPkW3VVaroHJp3Yobdy6o4soeCMDJL5YA87-8-tz-o4kn0jbAYFyu4fV2MWmeLI0L3Bnc8aiNwNwe-TZQ67cEQRpDPV6cubLIctzbsORtHfG_CGV7ESfOQjnWT0yC8nquzikMLJIGawF8naixNlPY8_IpAWweh7qO4JZfc5q-datWOkm1DApYFgcNWup_P9jG9yrXm-k0p0SZ7CTa36ObH65t22fNzZXmj_GGUcrR5KcBJnjb-TcjSA1c89xB1Ka-YcUo4gihBJ4UgPq5QwynVgktn75iGeqE0LiD_f-aip_P_LxOktpmfiDK63ZaTvtc7Go3qip6eaPB0ZxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلام یک دوره کوتاه از رشد علمی داشت،  که همیشه هم سنگش رو به سینه میزنن،  ولی حتی اسمش هم گویای همه چیزه!  «نهضت ترجمه!» رفتن شروع کردن به «خوندن» کتابهای دیگران!  کتابهای ایران باستان و یونان باستان و هند و روم و……  خوندن و ترجمه کردن و شدن باسواد !  اونهم…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5169" target="_blank">📅 10:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zk-PGjyyFtn7QLI6hjj49e0x2N3OKE8Ii8EaB7Vc0luwh-9URKieeV43ASBT67fz537CorHjGM38XxJxZBm77bvOhdDqjfSZ9FOTKUHCy4Xo1w4xxZ9fChsVWzEZaKyulxGnwS64tTy1s7BZvTN0QVIDzyiX85S5_U9jwRZ3dFfi9ZiNY9Wv2dPw-CsXAR-3k8EGfNGeDixiCFMOxpDTmzfTHwzZejBl9MQYSFNsJJTDL6nG4zqvA1lOwZBDixZR9xqUGCB_GkZdPwaGh2YewvkZ7CFQi1MEy43gPyVHczjCDxk2MMPGlmpE_-VkxA96YHBjOH_SSg72v0t2NLQbTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !  جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،  انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5168" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=UDM19usC9BQPTC-nrA0JjuLnG353IrSG2qjqDo2kW4IOMdycUjL0HvQPkwGO0eYwZ613h5hxPQFus24QBWvN1sAbQL_CiZJTl8NLBB8Fpl_SNXILxQ1RrX-_Dj2Kw0kRJFsO6g0zp50nZsf0Z9_S-S86ySmVJhCSM-Qx717o6sYLXZhRT2j7rVc5fMv4-kuYJOnQa07MWakrAgb75Q31YgYK7_kmot9hbFLdGvdRZGo225hCn5r3I6jNNbaiRjO00hmyYDdLoXYhonbhOesGxHU83zlzwBmKskYIxN6BLiK1V-zBxVERppU7qs5fFucQq7uU_kZJcO2uSqaG1Jyu9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67cdb18f71.mp4?token=UDM19usC9BQPTC-nrA0JjuLnG353IrSG2qjqDo2kW4IOMdycUjL0HvQPkwGO0eYwZ613h5hxPQFus24QBWvN1sAbQL_CiZJTl8NLBB8Fpl_SNXILxQ1RrX-_Dj2Kw0kRJFsO6g0zp50nZsf0Z9_S-S86ySmVJhCSM-Qx717o6sYLXZhRT2j7rVc5fMv4-kuYJOnQa07MWakrAgb75Q31YgYK7_kmot9hbFLdGvdRZGo225hCn5r3I6jNNbaiRjO00hmyYDdLoXYhonbhOesGxHU83zlzwBmKskYIxN6BLiK1V-zBxVERppU7qs5fFucQq7uU_kZJcO2uSqaG1Jyu9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر و وضع شهردار نیویورک رو!  دیروز !
جوامع مسلمان، از غربی‌ها، آموزش مدرن رو یاد گرفتن، آموزش دختران، مدرسه، دبیرستان، دانشگاه،
انتخابات و حق رای، تفکیک قوا، داشتن حزب، داشتن انجمن و سندیکا، داشتن روزنامه و رسانه، سینما و تئاتر و موسیقی به معنای مدرن، مناظره و مفهوم «شهروند»، دادگاه و وکیل و حقوق مدنی، پزشکی و بیمارستان مدرن، بروکراسی اداری، مفهوم حقوق فردی، مفهوم و ارزش آزادی بیان، مفهوم دولت و ملت، سرشماری و شناسنامه و داشتن فامیلی و..
صد مورد دیگه!
مسلمان‌ها در دنیای جدید چی داشتن؟ هیچی!
هیچی!! لباس سنتی بپوشیم بریم توی خیابون هاشون نماز بخونیم و بگیم خدای ما از خدای شما بزرگ‌تره!
با نخوت بگیم ما خیلی از شما بهتریم!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5167" target="_blank">📅 09:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
سحرگاه امروز ارتش آمریکا به ‌منطقه‌ای در اطراف فرودگاه بندرعباس حمله کرد.
سپاه نیز در اطلاعیه‌ای اعلام کرده که در پاسخ به حمله آمریکا ، پایگاه هوایی مبدا این حمله را مورد هدف و حمله ‌قرار داده.
بیانیه سپاه اشاره‌ای به محل این پایگاه هوایی آمریکایی نکرده.
اما خبرهایی از فعالیت مقابله پدافند هوایی کویت در برابر حمله پهپادی منتشر شده.
🔺
برخی رسانه های حکومتی نوشته‌اند که یک نفتکش آمریکایی قصد عبور از تنگه هرمز داشت که مورد حمله سپاه قرار گرفت و در واکنش ارتش آمریکا دست به حمله‌ به اطراف فرودگاه بندرعباس زد که ظاهرا مبدا حملات بود،</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5166" target="_blank">📅 08:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ  به PBS News: «جمهوری اسلامی غنی‌سازی را کنار خواهد گذاشت و «هیچ» تحریمی هم برداشته نخواهد شد. هیچ خبری از لغو تحریم‌ها نیست. »</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5165" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gz2jxEasH88kFe0qsccBBQh7eVyjEeTC98ER6sVf5WIfStA9FvXoo8LwGpmUF2UD8LdbkM1s0kf28wUJbGpjcSbnIBhNX89F_7u729AFOpDGsV032RzXUf3m3qJXr3nVHGs-8cnhawXhSmna_KDiiye2uB8vUl1UVVBnPWchyuRBcCuaEgcJEy84vUqVi01DS5QrAIqmFV6bozyDOG8V3TOWvv8_0Cy8FFUlN5O4TpSVewxXjTkPaHEr9Rc3BDyZ8_5v5a3tpEGWjlCFwtUCaBKc8Cdd1ygdOn6TjiHu4Og7310jMEBZtlJpqR0mFVfrHRxI9rt-FPV9o7IFkwxPTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۳۵۳ سن  حداقلی ازدواج برای دختران ایرانی از ۱۵ سال به ۱۸ سال ارتقا یافت.
جمهوری اسلامی اما سن حداقلی رو
به ۱۳ سال رسوند تا کودک همسری کاملا قانونی بشه! جمهوری اسلامی اما ازدواج زیر ۱۳ سال برای دختران رو هم مجوز میده.
فقط باید دور زده بشه، اول صیغه جاری بشه
بعد برن دادگاه و قانونی اش کنن! به همین سادگی!
در بهار ۱۴۰۰ ، حدود ۱۰ هزار دختر ۱۰ تا ۱۴ ساله در ایران شوهر داده شدند!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5164" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiQGh1g7YULtmdFDwwZkC7aSgLmyLijJ0rBCO7jze0QP15SNzOs-6_zZSDipjV0s-JBaSl4qtlbbhIRl2nEBAoF2lZNKfHqO-sTAu88aXiqsFdYM9j-30FcOSbYYBr02egGySwCOhlNuC3A3RJqZB8NMPVfE0aMXYOD9h1LzBrgoyzRDzB8L-1cEEJnYBSJy8CLsjCKKCVJIN6XLXNToYz2Mos0xX-pl23Thfr_RtoiSHncnqB-SDGUJtGFHHX2IAqxu262DFbOkVAJP5RlkKUwG-U8avcns_bXCLWpKK0I6xS4_amIu7ysYU1j9HLBMbYiCe6YGexFXEz9ZgllYiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5163" target="_blank">📅 11:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iz3P0jzUGd_YeRnpXLjXVWiIL3z7ki0ThRT97wdawf7u_DNz5-OdTWlgfLqo3Ck--qns2vtuAu_UJtTTl7bh9gRmjzter9NqhLfD7secoOI0zUs1eUjPOb4VJXiaJNqOD5C20XJJlObiV3dFCYPHYokSYz63o76qX012maSSGDPYkwUfcvMttBIG_98rOHWs4QOpmYECEret8_KCmxWt_ETIYrL1Lo2fr-m6ULAJ4bCczLjfwT69fg5vkDEL3NsQ_Ut7Lppyx8gnAaGaaYTfDdVwJv187kVlUw8Wx5PT1Q5iKJWBiQCr5NMhuJIufbS7YLmyqE_xIIM5J07My4LsDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه هم که فکر می‌کرد زرنگی کرده و با حاتم بخشی از خاک چکسلواکی، کشورش را از ورود به یک جنگ رها کرده، هزینه بسیار سنگینی پرداخت!  به قیمت تصرف پاریس به دست آلمان نازی!  آلمانی‌ها دقیقا با سلاح‌هایی که  از کارخانه‌های عظیم نظامی چکسلواکی  به دست آورده بودند،…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5162" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp0pSGkpwoFuV3A2zNCNeahir-nAeR_hadnd8S3QMntCLpbFZV6nSqZkT0rb-5XFReBf5u2weQuOuRmsFgPJu-w4vJjc-6W1uLv7yc2O7OSvh0UKNP6lOlYHcXdJnwwdeU8CzXDy3QdjEb14f3Do-02zWhcJPHZTw0pIgvWomt5yn-0jD1cx7o7HN_w-mu0Msh0r92QcDSVwXO3NbzHySkkLvfT9oiTSufKR-yElgxfmEW8K9JV7IYTXembuYNRl6sbTRWG1WGvVfLmP9tmBUSAkhv9DeWTdJ6Ax2BVmyBE99cT-ndaz9Qt_mDrgOhd-WcxPWj0gi_clzqh7ZupjqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرچیل اون موقع نماینده مجلس بود.  دولت چمبریل رو سرزنش کرد و گفت :  «به شما حق انتخاب میان جنگ و ننگ داده شد. شما ننگ را انتخاب کردید،  و با این حال جنگ هم خواهید داشت.»  پیش بینی چرچیل خیلی سریع به واقعیت پیوست! آلمان این مناطق چکسلواکی را گرفت اما دقیقا…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5161" target="_blank">📅 10:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_dRBw7lNIeRluX6Ix4pLi2zOvP3fPajXlqrpaPVpszqYBpaIc_wrJtFw0Ayje6NcB14viar2WcYELwIwFUsSDx4qG6R5vjRDNpj_c43zZJ1H9ZgSOpCxgVE79YQpaH8fQx6cXnr8JrD60OJwdZI1GFshvlQJhjfNkS4jiS4vRh8mD-2eWq1PRKq38GmGoJae1KpgZZqcFSGRBVkYgEH8vVOMq63mKGE4nFvqGjBSQTun5SBcGQjl1R4qfu2wyy4EpJEY0rKx380fPAIwDRjG0_B1qmlZjjf4TZ1SFA7CuVFF9X5Z3OWTw736-gysHd62JMOLF9M-NTmFh74tqdBow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمبرلین، در صدر دولت بریتانیا،  به همراهی فرانسه، قراردادی را امضا کرده بودند که بر اساس آن، ۳۰٪ از خاک چکسلواکی به آلمان نازی داده می‌شد.  مناطقی که مردم آن آلمانی زبان بودند.  هیتلر میخواست همه مناطق آلمانی‌زبان در آلمان باشند .  بریتانیا و فرانسه، عامدانه،…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5160" target="_blank">📅 10:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEQbKzDp5rb-S7Wj8J_YP6CvklSKXWgH72nnV4m5ndN3hVnANjF-XkcqIhilWzAr3k7KbPOXpvMboGXT7fZLs-JeG8deIzlk-mKXlvl4oHDWgso9235dQf6MrRmYv3EKXr8fxPWUSz7bCz0XG1t-BwdgFeyLIOsZEavIvzJXjV038faxcf2-fEgaLzYEf-PCdUoCs0Gy4j6RjHGlC62UNzdHwJTHZhaZzGt1L_EwG_7AVqI_F7gNSvA0jxAJUtmpUhxCSUjb5kCc2S4-dm6meH-4RMdAyZv_hfZMGSrO7Z1d32GeXb5smEt5Ng4Vz_04TGxT_pCWC7kEE1-CIM3qvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس  با این تیکه کاغذ به لندن برگشت. کاغذ را پیروزمندانه به خبرنگاران  و جمعیت انبوهی که جمع شده بودند نشان داد.  او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5159" target="_blank">📅 09:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHPDbM6ZIjPzq0caWhImykiLG2ZKQjQ3OtPw70EIpVbu9Sl7_msV3UVX6rM3KDPUE68vegKJiWhMhF4ssBycKUMuEO26Cs-jrSs4UPO5QTLrW2WAWrZxww2-fMQKLexD4wYWa4aN9I4whpDf1N87pUXyfy4D_NvRwST8Lz6iXFdWZ5wmD9apN-V8TeM7x_JIcqoKCscuXSA66shLfgfsGNethpUUqmTvBjW2xOBsMsouUGEi7EWfARi5xY3NZz9cXA1IfffprbRM-nRIXp8FD_VksqeAU2TKsqlYM2LLdUXlrg-8-Kn3rxJCxX_WyUY5RXBEODUyo5nExu-wmuQqBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۳۸ چمبرلین، نخست وزیر انگلیس
با این تیکه کاغذ به لندن برگشت.
کاغذ را پیروزمندانه به خبرنگاران
و جمعیت انبوهی که جمع شده بودند نشان داد.
او می‌گفت که به یک «صلح برای نسل مان» رسیده ایم. می‌گفت این قرارداد اروپا را از افتادن به دامن یک جنگ بزرگ نجات داده. این تیکه کاغذ اما یکی از «خیانت‌بارترین» قراردادها بود.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5158" target="_blank">📅 09:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_w8yK38sTiwdyTVZ0rx0rL556QaM8X_4Vr4bBegcc3GHfPZIsfFaCSn-iqiVSQCD4TebzHo2SLbyEwg8jyVa_dYGnqLGH-Ar0msHWi7XN7VRuTMXqu3deKpnByhjNuWfh1K8S-WsybuqmVdSGNIhcANJ7-HNnX4SWdlZd7w72EeS8S0efmihHaKr-7jjPR5go-H1zZX6mI53o5F8ZWvGaN6JCHA_39XfEFlLfZLJuFHIsnpgMWRn-2c0-z8HsFqrY3t4V2t_bKhV97c05Ex5DPcwuZKW2BfTrgK7MRZRCylVmb-jlrE-7k9YSAEb1oVnIc0B5TgGvPM7lCIgI4ijg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما دیشب بعد از انتشار خبر شنیده شدن صدای انفجار گزارشی تهیه کرد و گفت : منبع صداها مشخص نیست!
بعد صابرین‌نیوز و خبرگزاری دانشجو و… حتی اسامی کشته‌ها رو منتشر کردن
بعد سخنگوی سنتکام رسما گفت حمله کردیم و زدیم و…!
دیگه صدا و سیما در همون مرحله « منبع صداها مشخص‌ نیست» موند که موند و داستان رو ادامه نداد .
«مصلحت» نبود!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5156" target="_blank">📅 23:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=k393MVm-RdJtdQczzJs95oVZlzqutWS4pQ5pVxaQT9IPGyEduTLbezpcTpYAQt8RzcSZDAw60uenFHfldqZ4zjQP8W1KImlTTWJ-8_HUhNiPnUto1hDpN-TFNzhRE7s1DgaCQRBR3RPKVozkGocm3nmgcaT2BfF6iHv3U4rf11MW4mlRbc6akxXcMRp3Do3ult-J-479MVkK2BS7zR4ayYV1eXzNdDUh7EPkhWN6-eWZJIyWNCwzxWBCX1UyoTmoy-h-LGHFS1aOAl-5p4Y1JJf1TbhaG01ON22GmvSwdk50wa6-ymvBms8vmTjhAjPkxWQBhKMa1ipo7A6MdKoa7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbae4d271.mp4?token=k393MVm-RdJtdQczzJs95oVZlzqutWS4pQ5pVxaQT9IPGyEduTLbezpcTpYAQt8RzcSZDAw60uenFHfldqZ4zjQP8W1KImlTTWJ-8_HUhNiPnUto1hDpN-TFNzhRE7s1DgaCQRBR3RPKVozkGocm3nmgcaT2BfF6iHv3U4rf11MW4mlRbc6akxXcMRp3Do3ult-J-479MVkK2BS7zR4ayYV1eXzNdDUh7EPkhWN6-eWZJIyWNCwzxWBCX1UyoTmoy-h-LGHFS1aOAl-5p4Y1JJf1TbhaG01ON22GmvSwdk50wa6-ymvBms8vmTjhAjPkxWQBhKMa1ipo7A6MdKoa7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا دبیر: کارمندان بهایی من‌وتو می‌تونن
در صورت بیکاری، تو پارک دانشجو مشغول کار بشن
مدیرِ تراز جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5155" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpZi9Ee7R6lysMm2A4TamMtRc2fu1qPwqUdGEFCUNsxnW9sVpU6cMyCSh1r7taeyQdftbq8va4D_c1V7LGoROUrBmuAmYehmPagaMzEVuZv-2POyPIwbAS8bBnNYFW2j_AhLW4jzarPKnu7vGrNToBPGfXgINJbvWxRqvKLK1oAKi5CUTD2NNP1vwy1sl_1U5nBCTp1K3Xx--okL-8u3_15agRQnKlupWmTLIhWi0MisKdOmE4A8fFU6nvrSuoO9KJkCfhkz9VKDsYl4_Gd7m9cxlr5TPI5TJv7uEgQeJms71BmuCAvmqDjaxxOfU31SvU0sCTK8VaO882KFfOpTaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاریکاتور شارلی ابدو
از قصد جمهوری اسلامی برای گرفتن پول برای عبور کشتی‌ها از تنگه هرمز.
آخوندی که میگه : به نظرت
چقدر کاغذ توالت بهمون میرسه؟
اشاره به پول ایران و بی‌ارزش بودن
ریال ایران که ارزشش در حد کاغذ توالته.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5154" target="_blank">📅 20:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏پیام منتسب به مجتبی خامنه‌ای به مناسبت حج: رژیم منحوس صهیونی ۱۵ سال آینده را نخواهد دید.
باعشه!
بابات هم همین‌ها رو میگفت که باعث شد امروز ۹۰ روزه که معلوم‌ نیست هستی یا نیستی، اگه هم هستی طوری قایم شدی که گویی هرگز نبوده‌‌ای :)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5153" target="_blank">📅 14:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDrEt9ziGjMucqF36EMgjxGiCEmyup0TdIo0E4ViwDwwp49mx53Vlb5o8-Cif_LGvT_ZfHwQEUczXP4I8iy1cewGbsIGMRBGmwqaZI-Y9KPP7vAew7io8STDMfNzernACWWJNflBbZUk2WeSfCoM8eok3MdowJcfS8F_xny-nRXmZ2J8dn4SkhHUaqYWnSk6oN3DYzRLPuZ4oOV7t44f_tSQeH9_HD65gVWbB9WJu9sQFeto5XoJ7y_i0rfp0exedTecVl92qxzfdsPow7XudgppPlKKpyjpyhkcHGQFPI_zwAhPqCR903l3QEQFthgpohnmS7WwC1X1iHfr4qTobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر دبیر شورای عالی امنیت ملی، میدان جدید رو معرفی کرده که هیچ کس نباید حرفی بزنه که وحدت شکن باشه!
دستور خفه شدن همگانی تا رسیدن به پیروزی!
اسمی هم از مجتبی خامنه‌ای نیست.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5152" target="_blank">📅 05:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8yy35ZzRwxFPVt52O1mquxJRPYShbcHG7x2jI3lEhHsgtH7x7N7DI3HBDx3h_basVwEfOr3BsoC4S2FiYuUouo-ff77hLip4eQqpA7I0E4K5rZDFWqKbcB7603_sM5KMFvDlgZYzZxjXyfDk0qRasAR6L-Ugr24AhYlZ0pkEwWPYAxTvHNQnytJCAjAG1hgiua80bmzUAYeXBlJ-7twOr2dXR5MqVJoX0OGTNY1ZI8xuW1EVo7KHs36muLs6Yv6EbVHwus0gyC36xalPj3OlqBs489bp_rvbUfkYgupZvgBEh67P8Fe-IkGHCxoSudK0k13YLcdPcN9y9KwBAV3xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه.   سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است. خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5151" target="_blank">📅 04:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lq1Nvy9g1u97HFme5qdIribxkUD6OEFITp7O1UauQxHg9X-G39M7F5EDD5rGrQMrYPoksjafa9Yvhzf52b2_Y8CGaZ6fDDMfE503WDitNthTwzzoID_CrJu6NDAP9SyKjPWkrjcnJSitQMrtlGTLUlHr7ucTf8Sk5JftidrlgJR8OHfkGyJAzy8ijhQjLgmd8_WGUEPdS7EfpKOhg2959Lay9Ua5oHjaXJt4Bq5m4pytz_v8HAJPVMYWngLJq4ZB4cGIAnvk4W1VUIE6zc9zcxyBH4SzvgqmtdtRr_gUnEeMGTVLn2RrFz-8uP5sXLJN-LxMbHIi2mNwzMsXt8ow7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا حملاتی در جنوب ایران انجام داد / کشته شدن چند نیروی سپاه
.
سخنگوی سنتکام رسما اعلام کرد که جنگنده‌های آمریکایی به چند سایت موشکی و دو قایق که مشغول مین‌ریزی بودند، در اطراف بندرعباس، حمله کرده است.
خبرگزاری دانشجو، وابسته به بسیج، تعداد کشته‌ها را نامشخص اعلام کرده اما اسامی سه تن  را نوشته.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5150" target="_blank">📅 04:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ : یا یک توافق عالی برای همه خواهد بود یا هیچ توافقی نخواهد بود.
اگر توافقی نباشد آمریکا به جنگ بازمیگردد.
کشورهای منطقه باید عضو پیمان ابراهیم شوند.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5149" target="_blank">📅 17:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قیمت نفت : ۹۷ دلار</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5148" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bN8bHrFV9DsJM7KK14QKJpKUpTdvUfVXPtykSXmSC5B3Yh1mTrQVFJ7AkpqCBHaCSxAYojIX2EpGWV1btu89zeuGYA2O_MRTfgBBvESKXCXfBL0Ot1Hnd8aJLQkOHkGx6g_FX6phyIdUUsFiPcMBoncqHF6VN2YsuPvcLFsAw48fBOn98UvVgH8Du31xi-7LsZ0s3XnJB9VLtmQ-Rc-BcKkMg1T8JFLYSPsG61WBHIfPJVMUr3nBTPwr6s8wDGn0ICLVyX8FWWrGX5AWMyzeN9zO4ZFTZKhWbLP51DRkImnXPxvx7F6rU187ItxJFPW8OZ6z1UlGfgKqtzzUWfY3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که صدا و سیما شیپور پیروزی میزنه و از موافقت آمریکا با هر ده پیش شرط جمهوری اسلامی میگه،
سخنگوی وزارت خارجه امروز گفته : کسی نمی‌تواند ادعا بکند به توافق نزدیک شده‌ایم!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5147" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔺
بقایی، سخنگوی وزارت خارجه:
آمریکا به عباس عراقچی، ویزا برای حضور در سازمان ملل نداد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5146" target="_blank">📅 14:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b6861470.mp4?token=JdQ995PRwFkKMqSRKboZGcSDW21lvXzIrUSetsanTxCOMDMitZErTrNi-9V_Fb6jhIR3nXmkn9yVb5a0SM_UnsvaSzlNTUFpsUH8HXAZbrK51WHfhsDu-D7CJpvOgiq13bPAYUQJNe6T8qjURvfI9_ZXsxJomhkGq9Wf9k-zuKyB0_pNw7uqoRne_LQ2PpzQ4aQeyM0DI1N4bm4wTSttb81jmM5CBzUOEapQZ_vf92BgbihF74z7tNmVXFI-J_p_bnxAwrPENIQzhjEN4d2lMmL2dhRZxoMJTCRu_T9lNoRDkSBCcQg1uequn55U6UGEmXzP99z8p2HciH9F-A_tSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b6861470.mp4?token=JdQ995PRwFkKMqSRKboZGcSDW21lvXzIrUSetsanTxCOMDMitZErTrNi-9V_Fb6jhIR3nXmkn9yVb5a0SM_UnsvaSzlNTUFpsUH8HXAZbrK51WHfhsDu-D7CJpvOgiq13bPAYUQJNe6T8qjURvfI9_ZXsxJomhkGq9Wf9k-zuKyB0_pNw7uqoRne_LQ2PpzQ4aQeyM0DI1N4bm4wTSttb81jmM5CBzUOEapQZ_vf92BgbihF74z7tNmVXFI-J_p_bnxAwrPENIQzhjEN4d2lMmL2dhRZxoMJTCRu_T9lNoRDkSBCcQg1uequn55U6UGEmXzP99z8p2HciH9F-A_tSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایی از شهر رفح در نوار غزه و پیروزی‌های محور مقاومت
قبل و بعد از  حمله تروریستی ۷ اکتبر</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5145" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل - توی این مایه‌ها -  گفته: «در پاسخ به هر حمله پهپادی انفجاری حزب‌الله، باید یکی از برج‌های بیروت رو هدف قرار بدیم.»
حملات حزب‌الله به اسرائیل رو یا دولت لبنان باید متوقف کنه، یا اسرائیل.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5144" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taYEmJNEt2DQZDwa0YRpl13NvcYtSnkdZO9YOAdjODdBMHfskhy1xuwCN2a96L_cuT8EZPxIQ4rjzdSGXDQQ17EpapE1MqwLq_1X3dZIoFnbXKSjO4cQops_dr7HVcULvCY_uJsmM4I4ud2K44jlDBrBvbF_hzGrizZ8eyXgg-HRjhIdUn_mSEQKNY9B8O1qH2VmZovZEr_nXjwVpxjVpSAzHYrY3C9hztGBFD2D-67AjNBzvYRVUer2DvJtMmsKB6h1UNE8rD2D1j24NOi4YsS6SkvWtCII6K1ykwanjehwOT4Jx-JDOh8vdfvuCFNyFPvcn-jWss48pjiCxgLTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح در ایران با اذان و با اعدام جوانانش شروع می‌شود.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5143" target="_blank">📅 11:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=KyeRPbhABKtRJrLYqk_Y3BEyLcT_fGAbYC0HSg7cCp93GMdibfBAXjjeDCW0IKmZHwZZgUNjoqbURK_BWW6boy2j027alGX7np9mTaTm94An0EIx4EmqCDF6u7RPOOmfb76zE7Qi7k_7EghJDiMIyx2ChFfe5zMGdtsFbZqgCwiXOpDduJ_UnAPEENrF4Q7i-sj3q8obb6OD-Y553A3lj7_nybgIjvJvvy-DsI0s_UdQz67JgAlHTJTCz0QAElGJm8uvXt8cFgpmBsIkcYqLtdttgobrEKGwR_3kqIRcFaFbdBp4lDqjV2IjyqPzaTN_CymZvW8G7JtoQ3Fe_RxH0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69381f4f87.mp4?token=KyeRPbhABKtRJrLYqk_Y3BEyLcT_fGAbYC0HSg7cCp93GMdibfBAXjjeDCW0IKmZHwZZgUNjoqbURK_BWW6boy2j027alGX7np9mTaTm94An0EIx4EmqCDF6u7RPOOmfb76zE7Qi7k_7EghJDiMIyx2ChFfe5zMGdtsFbZqgCwiXOpDduJ_UnAPEENrF4Q7i-sj3q8obb6OD-Y553A3lj7_nybgIjvJvvy-DsI0s_UdQz67JgAlHTJTCz0QAElGJm8uvXt8cFgpmBsIkcYqLtdttgobrEKGwR_3kqIRcFaFbdBp4lDqjV2IjyqPzaTN_CymZvW8G7JtoQ3Fe_RxH0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5142" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=iSR8lTRdcRJhu5CIAEAEZ160M_m0e2k4NhS1apqKww-zCz5qSJZaY8_ySzz20rTqdAznAkUe3WqfLADcyEQ_EVSdjkkS5c2Y0IyJhx__lrtra1c1h5Y4v8YuL_pgIX64hHGZeyzB-dXjoYDEXRvmInIVfkSolrwjKrXZxi3NvI46_TnowSr1XWZWtT_yQGtvoTZvGD31f_bLndZhHxrVpi085ojNvnrdZS1uA-uggZP4uhoFf5K8uZ5iUx2Bodb8FeW6hnE9d9CFbCSA7GfT5xdtw0YYzjKUunukOKi-_oZdmPcRqLjnMuQV7iPWKiaCJR1lQPyCUZsu9UEJlIrN5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc885feb3.mp4?token=iSR8lTRdcRJhu5CIAEAEZ160M_m0e2k4NhS1apqKww-zCz5qSJZaY8_ySzz20rTqdAznAkUe3WqfLADcyEQ_EVSdjkkS5c2Y0IyJhx__lrtra1c1h5Y4v8YuL_pgIX64hHGZeyzB-dXjoYDEXRvmInIVfkSolrwjKrXZxi3NvI46_TnowSr1XWZWtT_yQGtvoTZvGD31f_bLndZhHxrVpi085ojNvnrdZS1uA-uggZP4uhoFf5K8uZ5iUx2Bodb8FeW6hnE9d9CFbCSA7GfT5xdtw0YYzjKUunukOKi-_oZdmPcRqLjnMuQV7iPWKiaCJR1lQPyCUZsu9UEJlIrN5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmcZbyGhsrYKwQRF-xW43ygUKLtvIqF3Xnjiuj5bX5wXnNOLvvKZJDnDWr75RdQjpreU43_usDWcnH0mK7dFJe1EVzyrzuYv0gOTjwtrAZBEwbgSYMW82h9eUZjooYWp2mATIquEDnmxHpu8HaKsn0AUCW-U_x3QDVQTEqtdSrFx0mofWpkmE3iUv40UDSoj5NQCXb2OZhvlAzBURUSd5xTj4yuhwFzzOkFR8W6_BWjT5lkcllBs-oRjalHaCi8uEzC1tf_1h4BjVPVCOV7T951qx6PSjEeKJGwIt-yIqMVN5CEdl23lIiYw6nvaTvN4eI5QG_3WWpdRnc_RYD5S8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSSVnToDyHXY9NaCjtmJ3h2InYrQTgOXFQ3iGsHivLA9w2NXde4Urj1Tx3GTeDQ-zVQdfeIqaEp9u3mOpD_3eK5KMGIMwX-9_Ybl79vtoo6ndDeVnXV0OKGD47gMdA_cpoW7MdQEssDjkPOocF_EIf-PbVq7Bg1TzwoDT-YDomFsAuaOgoQo2xxb5yD9FZG2el3zaBshCu_xOnQU-JHnJHtfs2BDxS7qARkK1J9Hr3wJTuJ2iYBuaDSzPAsb9WJkFxbcg_PsrnzR_f4XBbG4qvz_BSTZY3yY1lXKtZMYEnfslV-LSTFcXalgv4Nq1zTQFehDxAkQDd6SoRVaIHKeXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
آکسیوس :
ترامپ ساعت هشت شب امشب ،
در یک تماس کنفرانسی
با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=ANZAp70H-HjY_mrzjbeWOmx67u9JTGflsLia9srOBQ98wmYKR1xYjak7ECcPTvm3pE5T_J92KLxeej-dYcMs8llrKnAdmWuh_3090UZ-GLNl9aeDfNDbYBmVkEG3Jp7FSBntHB4gYJEnEkv8ez9BiArSSyDPkwaRDAT1yCxPWb0_OrPVgKurJ2szNhv2hE-MbFcZXqBUR_vrDoPcQcqJatygHmvCgMq5j58u_l1v1ivqIgQ6JpoDuhy-jsCKY49cVOx-nZF918wnlcA4n_iL5Ydi-Ol59UPhGCELFwPWne4SIejVleG4gD_Ns5N3b-CzgLNBKwrDnFx_wo_Sg6jhlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b5c3d0822.mp4?token=ANZAp70H-HjY_mrzjbeWOmx67u9JTGflsLia9srOBQ98wmYKR1xYjak7ECcPTvm3pE5T_J92KLxeej-dYcMs8llrKnAdmWuh_3090UZ-GLNl9aeDfNDbYBmVkEG3Jp7FSBntHB4gYJEnEkv8ez9BiArSSyDPkwaRDAT1yCxPWb0_OrPVgKurJ2szNhv2hE-MbFcZXqBUR_vrDoPcQcqJatygHmvCgMq5j58u_l1v1ivqIgQ6JpoDuhy-jsCKY49cVOx-nZF918wnlcA4n_iL5Ydi-Ol59UPhGCELFwPWne4SIejVleG4gD_Ns5N3b-CzgLNBKwrDnFx_wo_Sg6jhlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بعد از صدها سال
مردم شمال مدیترانه و جنوب مدیترانه بهم رسیدند
الجزایر سال ۱۹۵۲  (۷۴ سال پیش
مناطق اروپایی نشین
و مناطق مسلمان نشین</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCUmSC2GvQ7V7kt2j1_ASx5NrjoWKP-CDnpmAzuLDRH1fztXLs3k9ZwzbZUbZsVRf9uehxsrAh5o5PcxSPPy0Xyq3Wu52jdE_CXd-vhHVRAcBBAes_IguiXHqNVx1ky5xgbwZL6nsQYF1qsKOj8TE_FShf0t9IdzwMRHABksiEqmXb7KypSYDB_6yN4XxAPTqsADhlB1IbvINsJF12fzSeaBw_Y4LCG8rSakCweLl2JIJrtgrOD33zGAK3VV04S_PvYCfy43xXL7PrUDvo54CBddeBHQxvN8ZLcsdiYmVnkXKiOi8z9hqYKRXC0wGvuhR4gAYX91-_b0IYEc0S0g0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLZYq9VEwvZPU0U7LbQ8_UMsg5U2XrhYzFuBt5LcW2JI0bIYcmFUUQnR5tdy5Nw6thJPqKBFdv4X2MFiWeCEw0tk8oreYb24kbzC6bkGJChOg9gifqw3wzd8IbV0aJR4lbiNkx_PYxNaDDQbUS9sQON4awM2cGQzCe7mT10OyTGrwpW9gyump6Wr5Ce0MIEigwaQcjGH2b0GCCQ3XABAOCpaA2PxHEAv-zPsaA7UHufezQ3z_c2P1E0hr4IfSGWsSOFwPEK7szB6HKh2YzY1MiHPgkqrhZukY_WpGsU1d0fc8KauVZ2D2cKpeoeNl6tvixgkS3cX16F-DVweq0O6AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKgapcje4vp3I0-sxURDKlwqLFvX9CD8O0MS8f62eEWRDlnpjpqsQM6iQkVcfpdaDmisoRDfk1UuZ6CPAu2JKuIdSDHmSVHGh2cWFDnDyi2POnqwQgRe56vBeyP0EWCP28LHa2kIKdU26ZkFXgFaZkEwXHHRLCTEhXClCuNNZ1rF6AV6ogFnCj30AaIKRAdJBw7lFS-Ve7EGNztBJjk7s8Jz-EIH3NNhY6DCYK3Mw1VZZKpWGmAHhK72HbhRSCoFtaMXD6hhDOqg6yb01EutXrOQklCdl9TCKRA7y1oV7e-vGDQKvwE5R6xic3F1_T0efBCxj2O7U79li4dWv-p7UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcLpayf306ej27eL6nAWE8G_uUZaOy2JMm6qay0bn_-WU1_n-lHdiNeBAcfA8uZSGTNtvbu5bfWRkn25WnsnWmMhR7AwJO-rG76dEPzWjV2k5mME53j779IFpo-FBsqVPzlSg4pOzXxt2oV1DZUoGfjKQp-LGB2hjcoensyMMDyMqifNWWsrELEEkJYclwjHZSgO0rrE_c06QqFdjPbuW1NgEABNMw9R-gMuAKD-HtsFJp-BSE2q-nQ7l1a6zwf9g9C5fYz85Zr2pOuaLeC8vlaDgWsLyqeBiBo8psNwWQhXZLgvqPwAvl2doP5ktSC40tZeqiAo04W_4AGeCPGUNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqDybIs4tVJDiMSxT-V5X4YJ_b0eBDNAbWeWtGfyHMSRhWWwI1rVvNHm3f4eeAlnI1jap27lADtg_Rt0Gs1EW9dIgKzPEKnW4TgiqIyqiI132qV_Sxi6k991DDXJInjt61cfDpjP6OHPJ-zlJ22zGcW_K0uBS4ebv611vhGe7kDWmeW9g-pZukSBqT-1SjzWMdpQCPTnzN63eUuyAoK7YLQJseVhHTsPZO1W1M04k5ggovseMJ4z2tSYoHwmiU33MBXB2tAj1iikvZnacdVO5TsMPnKcWQIPqB2fZpfjVu-lcE5QUTbsoUh3oshy5Q8yolBnqINVHRf6TNTmA_2bXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNw3QpWOAjqKwcXpzdai1gw9ckuc48a_z6y-ttvnuF-duziTYePudkzYpiiX19_DTjiCQAdHkqsm-UtuhwdKjw_27At1HAG5zk5SdWG9fGcKKSxrFMSYA_BkwIYxAuXVARXwb4QhCyuLIfSoacqS_3rzfgvNrwHEU0G19ncC7_NfYXjSo35Ef5t5dEEQ1UEWeVHn48qDec2YfDb84Yyr9PJdg1lmwewjQ6cj0U4N3L3RQv8LSXkOPQb5FVorLYTn-acFxm-bxZGlaJCLZ2_SlwB5Gs4CdD43KoXGyW6Jzo_g147oQ6_O97ZxyV6mEDHDz8NdVGcvVZ0E0Q_UHTiBpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZjPFr0sqTmHfEsiw83LnVELi1VtQO6NRscdiky7WBGjdUiRASaLVY-lmA99i_Iz6udLjSVZbCNqEPeVOyE-2kIwvx3o6Tji7AwhE6GvvEu_fGsNENROzTMI2ZVy1TUXQyLcRwN9E8WmvP0j4E5VIT4v4xhp69Gy_pwG_rYyYpEfI8GW9vtp8POYdXkt9kEihddEH8FH1TAfOK_KIxvRp_7FLHyEvrrM-kaBBNM499abp4KZJELkpPJdoneHPkabUcWr3PmApfXpaaTCd4f5pppekRYjuzNYvPWLajSbhrfGB8dbzW8o9lBlKJWhZ42yqiZBnuU15cY5vxoRNhv-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJNWyTr1XpTBNC4GSmKrtLk8A3JiTM3Rr-3eYuYPAYkoTZw5qXwX_YJ_0jKI991RIvddLl-qmis6iukILMDMeoOVhkh-ylY0itviXWvCgUA74HIE9C_7m7GoNkZWvV31rY45hHne8MN5VOfnaadfa8AZswLXBB6JsFeXCSQzfgAvV4qbAjBgXR-hek8n09uEzgeaG4gkVlBmGnT0apnsHNCrtHzwJITYy4hZghXKknMmMD9puKkmwdwQo9sbvdwaaocCC3fVQ6NGRF6vDIXD4xzbxyuNui-sXxVBbG6FG_5EdJksY7ifuE9KvyTuHBDqb9LKTy5_5juJjNEyEELs1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDsuvI_9q31wXr-hC7mTJxRQq4DFm5vukKhz15hnir1Xk2gdAZDnqliz7WclfoBXuRCd4k4Hsx2yHbQIG7WnYZzFU10X6nHUr3QHjflBDdb0pQ-7WygPPLOTqW27JOgdyqEGDvHxAhqEqQsuF5-orGPQqdozSXJ98PdcEfCirxflwleGQebiFWv7d__oMf61p86xxrNpfHPbsCf7IYGnQMij8mFh6vApVNQ2ekh9VnldYSmr8iJEO2cYOtdjot_tULmVulqvVeDDJqsnERVRRm9_AX8j2z-7cpVWnJkJVTqjh-SQbA-v8f7AmtWhR4gSN8FfWc3UjglUT7HRiRNVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppxWZsDB9CrSQISWrKAAiRyBjJNwGkEcywHpFjmLWe4i9RTyHJno1XQbskuUGoyfVkALUsyqFbt5vFP2k9MPvK07S4cj7mPIrQxC__0smbv4aYaB3sv7iz_DgIzZB2MuPNV5yQxg77-Sf10t7Rr4-Puxu_iawzBHjQiFOi5jxqQzyZYF571OcT_Jjmy6p-Jx1HgazoiQDfrmdTNckOAN7eqMdUPxZo6Tf7wbPcPmWGBLNQASScEc6C01qyCgeHoVgaAliTKih9K2BIQtjkw-gl0ridFaCrKCKSs_5_FFMGpaioUS9a0Xynl4O-LFHZF_iIesWNTkglXWpGWtWDtpbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNdmF287jDWs4c3-NZ30KC8thekOdpWkDRmZhnS_2k1UFaNa-zWXWdySMiD_rrK3oxJVlrySBM4qSDBZUlbbH9TfcNmg6DJ7XnRFVC7Tf_fix0umCjcVC1FWFkkvzeA9_OCU--k_3LITHYPlFfTW5R06PJqNHWho75oiIMvpS8qOMhjC0EWcuFbsxeXAtylO23OBI31IY30OjklGBGjSfVELTmLDw1KkOiIflGAz0OuuPdk4w2MJrCcsaPw8R_K8weBgpqV-A9B0uNSteItQv3QNLjlqtV05GJ9GB8pcSVb4pQFZpmzP9W9C8opvmTRYD-BuM5HF9dOE2byVHPwyCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=p6kM3JibR-8TwJ_ZGymQNMiQ1yviTaUXhvRilptLKU16VyLUiG0kbbpOY_f3N2paGH2YwBIw0CVN6xAubS0F3vjW7-lzeGW1A6HJYGqx9kzPHbUtRXxN_Ewoe0Xq2H5PQaVBbdUU9ePxz-BPOm89HK7KibQROTfbDc41TC3OOOZLNm3j3gta4NKNrmB8h-3LklcXjRteKwooI7jC6pHaAU2q_cqu98GrKBqd-vLQUAocKdbyepwhXD6lsVFpBG6XxYvtVjHUleEZ09npa-eoUV0DgZ14hHZOm3ni-A0-233sxFh7cKBpKE8TPzFOXI2MP8pNmopSzTZZ6p6ox0xnxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=p6kM3JibR-8TwJ_ZGymQNMiQ1yviTaUXhvRilptLKU16VyLUiG0kbbpOY_f3N2paGH2YwBIw0CVN6xAubS0F3vjW7-lzeGW1A6HJYGqx9kzPHbUtRXxN_Ewoe0Xq2H5PQaVBbdUU9ePxz-BPOm89HK7KibQROTfbDc41TC3OOOZLNm3j3gta4NKNrmB8h-3LklcXjRteKwooI7jC6pHaAU2q_cqu98GrKBqd-vLQUAocKdbyepwhXD6lsVFpBG6XxYvtVjHUleEZ09npa-eoUV0DgZ14hHZOm3ni-A0-233sxFh7cKBpKE8TPzFOXI2MP8pNmopSzTZZ6p6ox0xnxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=ISBFle9onoAaNBRF3lYBnIgxqfp7s7pAGtKl8kbFD_seojBrGH_BDsMjD82IJvXC87nZWIbNr1rEEvFjjcOHgf_2vBoK5BJta5tn_8YYO2RerCB15PbjrG_NYZS0yUckM050HpPoAp-Dl1l1yro9eSVKRT6vG6q4gnwupCF88fFfuGUeGlWyWi1aL_Z6ps9rgNW9k2KFhgbbdnM4MHNdnVO7sh2Ro9nqelSHvxJtIGOrd1rAf92zp5sgUa2vwiaq9kqq2xcSdzQYivPgKQAPnRaKWhhGsDxnxXff0_O7ntHDG0IcH6EGQ2J00tJdkr8ULQBcCsooRxiz-j3sJ-7new" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=ISBFle9onoAaNBRF3lYBnIgxqfp7s7pAGtKl8kbFD_seojBrGH_BDsMjD82IJvXC87nZWIbNr1rEEvFjjcOHgf_2vBoK5BJta5tn_8YYO2RerCB15PbjrG_NYZS0yUckM050HpPoAp-Dl1l1yro9eSVKRT6vG6q4gnwupCF88fFfuGUeGlWyWi1aL_Z6ps9rgNW9k2KFhgbbdnM4MHNdnVO7sh2Ro9nqelSHvxJtIGOrd1rAf92zp5sgUa2vwiaq9kqq2xcSdzQYivPgKQAPnRaKWhhGsDxnxXff0_O7ntHDG0IcH6EGQ2J00tJdkr8ULQBcCsooRxiz-j3sJ-7new" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAyQQSIN9y_-hmKJ-ezHeLwMaeYDpq6OSUcw8U09zBa0q7fPQkGfhrfTkHNPQ2rEmfBJgg2TCsABpyCkQy8g9mXErq2SSGZKPfz8c7xQuyEAw37j9_9bj3yeOT5wn2b7xK8VTw6Cuerc4Kq1XkbJJKhWQlEHieXaOKHsUnOFZGlZpfGq1mHdQQFYBoBPrPh_h12lnHl1EZs-V50_Nv-TgykHuYbFf4RpDDWCui7ZztvNo0KmzlwDRdg3HtMcgJyoYoYtHV5_nmLU4sGBtd7dqAZ-DrydViFdfu60KndKhJnC1Ynw54nMRyX-VckxpTltGdDAiC43wgEAPmDgCDuqFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPawUYdobh-f9ixXMGnPUyrpz092LcogKjeZ7hH1QsrtTKS3zN7ZWrbDHqUBeRomS_8uBnsk7OxkX0RQe3NYzEDB9_cUI0wuQyBtGcnZjZKgNXjcUROktkmwG5vjytCDcVn7AwcXs_xPhF21aVBkkmyc346VMbG3jvIw4URlHKDLlkV8DZf4eai8ln6Q1gI60aXlPL0HOAP4UWWjJ3f6TN4lF1sc4l8DtUB4Cl3R0jTlb1aIirNm4wNa_8ZlarF8rqTR9Vtf3mftWbrhsc4Fj8sjrNiUUiwo8UECRT3mqCIE7sgWpCAEe_532Pv4qs-KylAOQNfP6nL17Ct84V3Ogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
