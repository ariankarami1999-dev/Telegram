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
<img src="https://cdn4.telesco.pe/file/SxKk7R39wYfjwZ54pVylyL9corcp1W6vez6l5Hetd4SH-sTpDgH1RMqihucdgTCFrokAFjTJOV95BPh8sdg7LGplRMc2wRNTlj456rW_pkVKjE5gyZylSGVNPwxxBUPxe65iTfjILCFOweeXQilJMuwnmeBI_KOQG9DzR6Np2nXDvQetYTNoa7hkgbsW90kfCRU5ourEt8mxvDbPGD7wiDP7L7_6dvTmLP-SIT6CqD-7amtmoXAlFMReQurHDRw410nwAV1pHOfy2CNh4yyoR9sKgSAY5Gy_EDYRxHFCSYBUrg6dQ6_gAQGTaj7rXShPuzioJsks04K5npUh8-yhvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 02:27:34</div>
<hr>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACUGh3arGkX-E5PEp314WG_cWS_qQ0Lk0SZHzMg1-yP8NnyXzmzBbWaDvvzonpSksaS7kFUwzZ2tyNxbGKMUiOXcWugUL2aCPrOQfEr18iEvge9E-uZThd5I-U86AQaIe-SMufPHv5zDX53etpVpqov2byNECVDiuIVh8lhLDz8xTG2yq-6yNLR-jj_w3B03ZOUoZbOgqSzHtPamuXEeG_CNdOYO0B-0V2kTpxA7adWcgNvpTF9ftL2LKn6eZuGLWZ4gIutKBSP620pTtl7nyoYcA9yviEPMGTLyt1dHLnyRz6pz4yd6PHOYCIXe-766nBpy7q5zN3TLKwfYrM6VbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=LRmi1VhZMsNR0q-QCqms-nWNprtyYlL2Tk3vy7U6bQ70Jj5HJ-44RKG7XIzqcwfDWxkeNwPgx3UndC7AbBJBcT8dX5jwank7z5KPxdWFX3RDQOyVN0YT9CEZdP2u3KpVyriH4-m7A1r-O-dK2CnALHFEm4itMoyTVqkYXltQG_Qtz_6M-83EtQCRG4D88eRSL1Ml74OonRYOrkTBAJ1JxCCZTohg9NHIxUX7T_oexYgggFEFZu_lLWE59w4kGxSKX-3i9IS3fdVFslXiuRsysuD9fftdquNOvxQVFEtE0lHYywj1hOIQAXWsnELrRL8C1unNx_WjN5dU1ixl0CsWMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=LRmi1VhZMsNR0q-QCqms-nWNprtyYlL2Tk3vy7U6bQ70Jj5HJ-44RKG7XIzqcwfDWxkeNwPgx3UndC7AbBJBcT8dX5jwank7z5KPxdWFX3RDQOyVN0YT9CEZdP2u3KpVyriH4-m7A1r-O-dK2CnALHFEm4itMoyTVqkYXltQG_Qtz_6M-83EtQCRG4D88eRSL1Ml74OonRYOrkTBAJ1JxCCZTohg9NHIxUX7T_oexYgggFEFZu_lLWE59w4kGxSKX-3i9IS3fdVFslXiuRsysuD9fftdquNOvxQVFEtE0lHYywj1hOIQAXWsnELrRL8C1unNx_WjN5dU1ixl0CsWMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف و البته خود علی خامنه‌ای
گفته بودن : شهرک‌نشینان اسرائیل «شهروند عادی» و «غیر نظامی» نیستن!
حالا حکایت خودشونه!
که زیر دوشکا و خودروهای نظامی ویژه سرکوب مردم ایران، جشن و عروسی میگیرن!
اینها سلاح های مبارزه با آمریکا و اسرائیل
نبود و نیست! اینها سلاح و خودروی سرکوب
شهروندان معترض بود!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5054" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJHLMYQprHSuOFZ0Da-ORJDMfcZI2e6ZJtkzaamZIowh4SU3uqPy0VjwG_dHGmRJ9DBCNbCm9vx70mU3vjvRKW9Ma4XMpCswYeBQICwhJ2e-5wPzHDFO5pv_XPoUQmNgZr7SQ_xmaKVAZOF5M8xK_JW24LSWuEpg4o_rY6geN8zaxHr1hYdKRCxdzJq5ayQvTLg8WZCnV9FQOHxtR5ovflsDDlelEntxLlrUC6gKfo9Z4pIlj4ufl2TLsXVvMzB2bklIrvwLmpNURvQ6yWB8KS7of97poCaNUaxXe0ciWsldx1tV0pxDr0HNETJ43dY-BPAtE2SyqU_V0Da62UtNOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sypTZV1vIjeI7eIZT8v9hz1EQc_lP7yhE61zkCt4YdBI7GD6XVDhT4n9V9PuY_GZ-bCO2I7wjVyBSxU2z_XaOuG97KApb87uMSjTma_2N0OCYzs5KaQdewxdQ5VgeBJHwkso18nsFOEvbHS4G6ZpfEfOF34Qe9NiIWuWi0cnqUGn73gX3wU1v3Vl8tKV_TPFcoQ-MI0vOCPt7AAXs_afHszQdE8OcDj_w7IG45_ex-FflSll-LIAxBVLoQY5iKzplfZ-tXbTYgEQFPa7ePs7W07I-jTV32hJAZ4ZA7N7BysRkYAdNCa063E-qP9AhwQBd1Vt0UtUaYMx1nx3tQYtww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1T0I1r9fQwHM4B-imEB675behykA-L6MpQiZ98i40kXJS--SQMazXi44oNktcIQFVcfcpK-bzpQElHG5mArbEgQ9vM3A2Ubk3g8auZka4sJHjq1grnBHBxd_cK1UHcyjonAzacL4faeaTn4vqUmTtWM25UqEUifUP2DJ3NgsoZ0Tth8GhIVoBDRttrhZ0ZBk5lm9r7dpuxzvkaFv7bmmpHbCXVCAqc5DVctbjMADuak9dvySqgw9EfcI75aZaGl638Dl5a6E_dY09ffhdUjlJj7jix8S8f7KK79s-NcE-lGXr_UzgTtXxUbG8uvUffwPxxBcUH5Xtjfw4GKFp20RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpthwZgIkbMA7sCVK_0cl6bHgWl6QYolfQcn9gsCb3SShyFHUC4APvsnvWoB7qXrEamAEcedjQySTX8EdvftiFBhN6rh0wTzB7OuGZzy2OY1wG-ihxvTB5wtuyK1ADoSxEcqg63GK2UPDrOtgtZ3IgSUCz-nszcGFkOptyescNLpDv4Jr2iDaAXIPOsvFZ2jlV4Vpwt307Oz_huSF9-Irm5LvVqMZHx_2oMgEcIVIvdirY4wwFP106_GzVBTqnqb2v1SklDGy927LUw4mL9SWpXNyvW4lfZzBd4mj3IJxm3R9W1FAcHeFBf3EqA_wKRPP6wd-YOrIyFIO7aPJkNPTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BB7nxT2BVsuKQrRsYOAEjZCdn0nTXXohY1afTJUFHov2tn9Esb0UXvG9H9cPBUrzn7WSzwhMnk_Nw9nZSHL5HIo1N9bKHE8uylxdZc1_uvZEQ9U00cmRv6wMP812twnMYMCrTdcjQEUe4IWHZIxwChmvX1ZQNfTQErvSc8iiauM1ZldpwU_7KSQB4v_I_DPP9A1cqSc-IZtpcTpOFC4jPiTQQ4UAfjBuSVCDz8Nu9mov61TfqZ6hqCF3RKw0S68fE2LP2Lj1Q0DGNGGkcUQNUDFtpa0dBQHJ6_AbHhBVplrbTOK3sUbxk-hP-C6CRqkLMtoxvfmMk3rRxegruGFMng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=OnV0-ulZvWprG4XT0rBJgFET3h7PSD8Bgwt94IntRuRwm5IyeLo80w0CL7XZYH7AbE2jfheerM59EZuf4Q7mX8Sw5rL3fewTE6TupoPlJ6rp9LaVYYUJ_25wnWl90Im8kp3x49EzfKLSLD9-vr9patLR1g13DDx3CBO1KrPDWHCU9u2Pu5fgN-uWDJdm6MosLLlXCvUgQPFaTlUv_w5jSQ6Zl3maP7SJYwsXF6Ycz1VnS8fy5RatBsP5lccIUKCoDs3RpD9SW_fXGmbFT_dPp95jcWh4dUhoT8aYEJlvWTnsQ7jd2dazBQl2yHbtp8gSEFadt5j5uzm52lIy5HuwIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=OnV0-ulZvWprG4XT0rBJgFET3h7PSD8Bgwt94IntRuRwm5IyeLo80w0CL7XZYH7AbE2jfheerM59EZuf4Q7mX8Sw5rL3fewTE6TupoPlJ6rp9LaVYYUJ_25wnWl90Im8kp3x49EzfKLSLD9-vr9patLR1g13DDx3CBO1KrPDWHCU9u2Pu5fgN-uWDJdm6MosLLlXCvUgQPFaTlUv_w5jSQ6Zl3maP7SJYwsXF6Ycz1VnS8fy5RatBsP5lccIUKCoDs3RpD9SW_fXGmbFT_dPp95jcWh4dUhoT8aYEJlvWTnsQ7jd2dazBQl2yHbtp8gSEFadt5j5uzm52lIy5HuwIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5046" target="_blank">📅 23:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ :  از طرف امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس امارات متحده عربی، محمد بن زاید آل نهیان، درخواست شده که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازیم.
آن‌ها اعلام کردند که مذاکرات جدی در حال انجام است و به نظر آن‌ها، به عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همه کشورهای خاورمیانه و فراتر از آن، بسیار قابل قبول خواهد بود.
این توافق مهم‌ترین بخشش این است که
ایران هرگز سلاح هسته‌ای نخواهد داشت!
با احترامی که برای این رهبران قائل هستم، به وزیر جنگ، پیت هگسث، رئیس ستاد مشترک ارتش، ژنرال دنیل کین، و نیروهای مسلح ایالات متحده دستور دادم که حمله برنامه‌ریزی‌شده فردا به ایران انجام نشود.
اما همزمان به آن‌ها دستور دادم که برای انجام یک حمله تمام‌عیار و گسترده به ایران، در هر لحظه‌ای که لازم باشد، کاملاً آماده باشند، در صورتی که توافقی قابل قبول حاصل نشود.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5045" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5044" target="_blank">📅 20:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=cfnCovzdqeJc4dQiucLz30A1nQgnW2OinWTBUAb-hh9Ne1y74a86EZ_bUdsFuWPD7sBgigvYKz27PXk1pIsURs89t04PZRVzJfysrk8hUWIjlg_x5ZJ6w2RDBSUJpdQnA2cjM3rObT9sFAkXQxVfL6E2Y_0hMB8j7xAt81H1omz-JnVWVwqMWUsQjqbtaBSWnA2bhY37KLsNnitlzSenxtkzmwgrHAxh_c4eAbnCJMys_sJfyjdREYDhp5NhJnI-xXlu5vNmeKCviPM_qNI5ln1ndiI45_6IDkdY-AbxVErNduteISmUII-gLF-UI2g52efNocc7Wx_aqhTLkSISHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=cfnCovzdqeJc4dQiucLz30A1nQgnW2OinWTBUAb-hh9Ne1y74a86EZ_bUdsFuWPD7sBgigvYKz27PXk1pIsURs89t04PZRVzJfysrk8hUWIjlg_x5ZJ6w2RDBSUJpdQnA2cjM3rObT9sFAkXQxVfL6E2Y_0hMB8j7xAt81H1omz-JnVWVwqMWUsQjqbtaBSWnA2bhY37KLsNnitlzSenxtkzmwgrHAxh_c4eAbnCJMys_sJfyjdREYDhp5NhJnI-xXlu5vNmeKCviPM_qNI5ln1ndiI45_6IDkdY-AbxVErNduteISmUII-gLF-UI2g52efNocc7Wx_aqhTLkSISHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‏رویترز: پاکستان [کشور میانجی‌گر میان ایران و آمریکا]  در چارچوب پیمان دفاعی، یک اسکادران جنگنده، ۸۰۰۰ نیرو و سامانه پدافند هوایی به عربستان سعودی اعزام کرده است!
سامانه پدافند هوایی برای مقابله با موشک‌های جمهوری اسلامی است لابد!
پیش از این
مصر هم یک اسکادران جنگنده و خلبان در امارات
مستقر کرده بود و به ایران هشدار داره بود.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5042" target="_blank">📅 16:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8KHSUCPPNm9cRF6DQf-9VAThw4tHtuo8e6nXu1d78RzS9fStZKNpOHeePjVUr0LwZ3qhdywpsR9QOQaHjQF5YRs_nBP4XEnPE32BP8rarwiaMeVpmp9oNSUZTp4IFrX9pI2V_Dq63wxgT8I_5Q0rYdI-5UGYKC9bZvPI9Qf_s2neaAXGzKiUCwALDFTmSh-wHDC-Ycm-7N6QiMz4FfpiVZXQlzNxvql3kFSCve1AK9AI_KWyUCEv3dwDRogpvVvbg7BcfkGsd5fDFA9pH71Xa2BwQGkzOMdr7CiNSni-HgOh64VmRdvDHkA1QO4qDyYASKMizw-EjdkAIe6VPc3mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPoewp7_F5K-yeoIsycLFhr198zjQU72kDwL3Dbt9FmG2h88H2S8xlSDwvYwIsfz0u7jDXNTch9t68O45q4Otl_BVvpuBNAVIwHLrAt88URtZY_YM0yz6JEiqI9Cbh8k90yrvl342rleODHuCPxq6WllhjxPlEDtn6TxMSSc_3-ySo1nEss8ezJeGY222SIpxm6wxk10TE2Xe55Gll--yo80BojmLohaUPEL5GQWgf3a5DrTUMLg9ey81puuVZL-0Sb7-4SlwXuNWyR3gGCbSNDTuh1Yafrmvy7oI2VYxWn13kbHgyNZdPk6ZyyNsrxRb4Iuij8SJsyZQ5Wo0-QF3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qovF1RQJrYac7F3P1nqYA2m_ugkQGGsM6JDfKahEIXZIe4J60IyCfc3DYzEzPSzZlyO3cxsdzL2YAvXsl4M5q75yruwsukuTZOhtHqNKgOBXabnmxbQJ2sswfyyECM6FNhuD43O9x7gB5kSfqQQW2XpW0g1TvhLrM2xB18i4apLSa-3BqJNuPR23wwQFHwqz4rcF7qAwa1l80pDUKa5k78WRiQVFWkiTWJyvII2CNz_AXXIKeQqXLtDYDEu9km7SzU4xj-4xd3J5-Kgblh2N15hjHstKqyESWYsVK_lupIRoa92Ni1C1qDJXRr0ok2JlVqsyOxixB2fbRMHc8R9iNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DTW09uoG9JfIZJyuKf6LgxGxJx6nzdYBOLGQdOcpZEOE1cljlj4_aqizurn8fG1UN-r9X1ymuVCzmdsJudP4b0P1Wg5Qy-RHEinaepHUJnWnd4f_PkVW6-LlHYPukitp_Pvm_59rS0Y2ynrSAqZzC4ReFS0XpPzhSwqbJK-rtwxpjzLlh8EhH7ZgVoIjTU2du43fUowjMoxGAvKCyxqeAXETZ34YHo5HerjIBPxs_9sHNNGoV55K90-Bre0qhqsPsO9NqypthSNeIgR8pyjfGBVYrXRdlmIDI76SD3HTxzIyuDJHJHWB3dbdY1wTnfq-syNwvIneiK5zoQ6kj4ElxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی
۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!
توی ایستگاه مترو هم از زبان رویترز
نوشتن که قراره ۱۰۰ میلیارد دلار درآمد
داشته باشیم!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5036" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=eez40R53icFlDJlRSuW2UeuGSGGmqcIb5TEleeeRHVQPa5LTrmCYgCMO1i2vTPofilSZutb__aSc1Mqbg_bZ2QrcZj_F-mylaUN7TYh732yGZUVWe2geneCqOpf_TqwayZP-YPMYLbqfvGVvBGX5Hq_bDeXqh2UHYzNd9bNhKncmTAeRMFx6KpRL9G7woZgsRWjteaXGmw3tvPKEkDZlw3h1ETcCldMu30VR94uiux9ClM6obFbfbLnS3i-a5X1Dwynh_ELcGRur3cizS-44LNlMwupV3VCE9iaMQ50R2c7-RGZH0J0K5vS9ztXCceQK6m4vdIuQtSJ_N2FUBeVMEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=eez40R53icFlDJlRSuW2UeuGSGGmqcIb5TEleeeRHVQPa5LTrmCYgCMO1i2vTPofilSZutb__aSc1Mqbg_bZ2QrcZj_F-mylaUN7TYh732yGZUVWe2geneCqOpf_TqwayZP-YPMYLbqfvGVvBGX5Hq_bDeXqh2UHYzNd9bNhKncmTAeRMFx6KpRL9G7woZgsRWjteaXGmw3tvPKEkDZlw3h1ETcCldMu30VR94uiux9ClM6obFbfbLnS3i-a5X1Dwynh_ELcGRur3cizS-44LNlMwupV3VCE9iaMQ50R2c7-RGZH0J0K5vS9ztXCceQK6m4vdIuQtSJ_N2FUBeVMEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=FlyIN-xAxOJD1GG9E2mrp4cRzaLuMVuqj23CIzWM7yr0pIeX-6oXC4UGi9S_0MfieD7VZjUfOKip0-XHTROonPMOfW4NOY0_w5TV4ITEbTudbilGnVsJkQJPdi7TW6aT9lTdxNJcm98GL8k8dni8vQDgHBv-qpi7beNVln30TpQjnkjfRNfWo8xjwJ8YHgtuUVpechb8JhpxK9MurRAjTbjXTfuyyNNmaSKDLSJu-0Gj7Qfwh6skXiL2h8ksZDDPlH-90Qk_sIJKWN5Ao4wE36jfc_03D8xXrf1jL29mcj4Y4nrGOCuUgu6iixSU2_0juuJmukM6eC-uOsSOdIXHlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=FlyIN-xAxOJD1GG9E2mrp4cRzaLuMVuqj23CIzWM7yr0pIeX-6oXC4UGi9S_0MfieD7VZjUfOKip0-XHTROonPMOfW4NOY0_w5TV4ITEbTudbilGnVsJkQJPdi7TW6aT9lTdxNJcm98GL8k8dni8vQDgHBv-qpi7beNVln30TpQjnkjfRNfWo8xjwJ8YHgtuUVpechb8JhpxK9MurRAjTbjXTfuyyNNmaSKDLSJu-0Gj7Qfwh6skXiL2h8ksZDDPlH-90Qk_sIJKWN5Ao4wE36jfc_03D8xXrf1jL29mcj4Y4nrGOCuUgu6iixSU2_0juuJmukM6eC-uOsSOdIXHlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما :
آماده‌ترین برای حمله به ایران اسرائیله.
اسرائیل نه خسته شده، نه پشیمانه
نه به آتش‌بس مقیده ، نه کم آورده</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8-sAhw2jTnOZaC67Q2cawF2wJTY_DJm0EguvXukrSaJGZqXDiaLr39jPW03o_KoadGw6KXSP6cDREEfTHHjh6ffyubnBcXbwcLxOM4ATmpQDpktCHpKILVGIwE_zdSQ-gSYPN2URSuqkYFOg6keoDDmsDnfhjc7iHEzP3Q5EZNOrs-eqOOhBCJnYVU-EdcMmpad7aF7XsXgIxHhvjpkBrn9K9wTxeWmPUGJFLr3hSXH4AJDVGI0wU6ljJWwou1kpgstaZQJe_mQjdu1U8o6KizR37ZBJ0jFnVVFCYtG7RH79uVpzccA3FJnVaFtBPZ_iqNOzckMIWRUB4UM_iSMbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lb7jDxx1orhsTiCtZS_XSlASHCqHPtgf-SYvzIc-zYo6sVU0Bk7XCMU6sIvnXVOzU7DNjuwkXFDDCV1cH2uauDUydPEdm-C-rBLTvF4RkH4JNc8Bt7MWEFfB5q8Jhl9QvuuE7rwYbDZGS0eXCBb-n4vPbAmd43VnrtGC2eo2vd-ZQcDN4LsX933qwOB_ae4asksRLExoF3YAu0pwFUQPAt833d8kqnXom2Z0traJ_lpdS1k3JFKdfwopLJDHM-x0SzBBarGhtBFhEnape-xOYfsV9v2KcwrYYsXcOYE99pDNAA48utV8Hsd-fjPLTFMY96IOIby0q4fNXmUCKEpoPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxfpNKsaVV_ZFucVoMoep3vNVFbUMnLsKSH9eKKg4rDBT-nnTAggldxSQice5H7s4l0qnNi1gNIvrSfMMd3h8Y2IeXBqwfRP22N2wa_JIIRcLjqVN9AMObV8lMGX8ljnMH2p2ucMEZi8aojSehvx38D6F-562qEe_eVjLJ9CZ253LNjQbdLzmjugIsUdLgmW2JmD2ji3L38ukf15m2nBKW1ap49OZyyZt4vIeYgFowCpe8xMmQ019czOPpBvEK0V4szqbalMDZAV7myD3K6om3DpjtqhSZ_VeNw7Mgb21h5vW676BVXJG7Qn5iRCcfiRCCNqwyD27RboO34QsHAeOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات سخنگوی کمیسیون امنیت ملی مجلس.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5029" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5028" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5027">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CERoAtG_sMWKTqaVBD0v5MP6HWI5SvU_r-S0H3x-X2_Tun7DtFuVb_FMtS8s-6gFAJVciwTbS3aVecBwyHH69zVPUhjOPrjq9YBbfPdkp0NOXyaS5yy1YVlS-c8xv0-DPEbt4DLSftcSckf46awv9gPJCunBBuaTrF48Njm5Ov1fEj8rFIgK5jFCARYnuxrqG2TA1XLrgerEf_OLtdlMRIyjQ8Plg4ruNd3PK7bJ5NNfUCQo5VD3PVhdz2O7fN5fZJcEaNL77HSNEjvNbQRN0sW1WSL7PDRwYEECZwJV7Z2QNd2sD3IgdVg0nIoomLN7TQlJl3ekQ3Q1RS3QMB0tkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟
در پایان جنگ ۸ ساله
۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و
شما «جام زهر» نوشیدید!
خود صدام حسین در سال ۱۹۹۰ به خاطر حمله به کویت این سرزمین‌ها رو آزاد کرد! خودش به اراده خودش! نه به زور شما! شماها که جام زهر رو نوشیده بودید و تموم شده بود! اصلا خمینی بازگشت این سرزمین‌ها رو ندید!
چون یکسال قبلش مرده بود!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5027" target="_blank">📅 23:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344237687c.mp4?token=Sk7yRoHSdm6Gi_Mn06VwfRxotA09crJpc05LJxA2W6KMlYqTxFRYS5fWGTlJ0pvwCOuW-OZQFoULn9Rx9PcsPUTLbAw_XeOevOxyO1r_eTVq7JXqPmuv2fxGqW2Z48AkaA_oSLUmbVEwJypnaGvq0nUq7OKtSPy6SNMC_bb4LCsWCUKbC4i5562iYqsaa4HjwHAsN7_3uGigXLmJEDyNLj3rEFQfNz8RDaGVugSRVE-GtIfmY4NclS1dIaOd6uhllvRMJkKul17udGvtmGTu5e5tV2WpCdf_rnkFkmqwPMEtQycW0M_qg3YbLa8VnK8rHnAXo78lxk4IbCVJrHGuSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344237687c.mp4?token=Sk7yRoHSdm6Gi_Mn06VwfRxotA09crJpc05LJxA2W6KMlYqTxFRYS5fWGTlJ0pvwCOuW-OZQFoULn9Rx9PcsPUTLbAw_XeOevOxyO1r_eTVq7JXqPmuv2fxGqW2Z48AkaA_oSLUmbVEwJypnaGvq0nUq7OKtSPy6SNMC_bb4LCsWCUKbC4i5562iYqsaa4HjwHAsN7_3uGigXLmJEDyNLj3rEFQfNz8RDaGVugSRVE-GtIfmY4NclS1dIaOd6uhllvRMJkKul17udGvtmGTu5e5tV2WpCdf_rnkFkmqwPMEtQycW0M_qg3YbLa8VnK8rHnAXo78lxk4IbCVJrHGuSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶۵۰۰ ایرانی رو به اتهام‌های ساختگی - که سنت همیشگی این نظامه - در سه ماه اخیر دستگیر کردن!
هر روز هم آشکار و در خفا اعدام میکنن.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQ__qtm6yvT8I1EBvWT2gnltO8izRG6WH6z8Wh1jLwW0S-DruiKhrbU1aBQi-d9MJr5FzbGFxaRL2JgNcHLCm1_theqUCRUZGImteU9Cb4thoAZl6mlwnD01ZDMxxYYl7EvSsPoR5GkY5aNUcl-_7OYWsAW3E5cAptzlUV0nOEpRzuoctaVphBe1YC_tmAkDVtZ_YXdxwT6kRkIscEEzcpOTgkhlR7gj8TIAjdpRJVGXfnVFxJZRigSNmbRnvYYcfcY0485YnVIzE3GVNOfoUyQiHvWYGAcdcPVmGdHf4jDgWfRETY9nIEYRRiwZ_PVZJLIA5ijFu1NT-OQ8D70r1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدصالح جوکار، رییس کمیسیون امور داخلی مجلس : «در این مدت پیشنهاداتی از سوی آمریکا مطرح شده اما جمهوری اسلامی همچنان بر همان بندهای اولیه تاکید دارد. شروط ده‌گانه خامنه‌ای خط قرمز هر مذاکره‌ای است.»
🔺
ده شرط جمهوری اسلامی که میگن خط قرمز هستن:</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5025" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید شرایط جمهوری اسلامی را بپذیرد و تسلیم دیپلمات‌های ما شود یا تسلیم موشک‌های ما</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5024" target="_blank">📅 22:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏ترامپ به اکسیوس: من هنوز معتقدم که ایران خواهان توافق است و منتظر ارسال پیشنهاد به‌روز شده از سوی آنها هستم.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5023" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
ترامپ روز سه‌شنبه جلسه‌ای در «اتاق وضعیت» با تیم ارشد امنیتی - نظامی خود برگزار کند تا گزینه‌های اقدام نظامی علیه جمهوری اسلامی را بررسی کند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5022" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZyffIdw0WPyq_IEloLQPR8az6Iw0EEZdH_SUF-FvPlF9yT_A9vRoLa5OheodZKhM8YpDOn8B2LqGJdBT9vdBs-fiMyYNX5hFi6ysfu8b5P1jm9TtD87_52lQ90CNaEFbJ6p1NWkK8hvJGvHfJbl_moTUrDdNliGHQw7OdEXnJ5BZmwiLOJnG_YNoVDWU9evJ_CB448SGy3c1O6MrxvEh6lA4LccYNnp3kjIweNxabxE2a5WKJTy6zndp5VEF6TXw-bMGR0HBUpU2GZLYBuv7CLs6w9lOqXg1yNQDj4VDNNyHJka5klDax_ebvVRFtuVesr6m_uBcDynvXG46EuIsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=emHRJbnjeuSQaa3RFCPrM_cIFOsy98bJ7Vq4JdtA_Vm7j1weo8BguR40eBLMGzkxU8F6XVHNlGY6y39ArhgI8iifgvxLBnWBmWAR_YDtlIp7QNkm1YT-ef9CwgYeN_KldDOx1j80-kGE-hClrSo-5TFmFCbjt2uLbmabiK1SF_2sMXYq-mY6BuP7pxmdiv5xPDAXuP-0L964kpr9b4X_5D_jUBIE5J1uj5ruNdqkqvfrzyl1UApyfnWLzYtqVPG9ub8xAKzD4m5Y3Q5684lpFujzI4XxsGyRGfRwaD7l_j5LO5ncubuRHz5iity2ffuy_wqf3oCunhbBxvoRjo3gIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=emHRJbnjeuSQaa3RFCPrM_cIFOsy98bJ7Vq4JdtA_Vm7j1weo8BguR40eBLMGzkxU8F6XVHNlGY6y39ArhgI8iifgvxLBnWBmWAR_YDtlIp7QNkm1YT-ef9CwgYeN_KldDOx1j80-kGE-hClrSo-5TFmFCbjt2uLbmabiK1SF_2sMXYq-mY6BuP7pxmdiv5xPDAXuP-0L964kpr9b4X_5D_jUBIE5J1uj5ruNdqkqvfrzyl1UApyfnWLzYtqVPG9ub8xAKzD4m5Y3Q5684lpFujzI4XxsGyRGfRwaD7l_j5LO5ncubuRHz5iity2ffuy_wqf3oCunhbBxvoRjo3gIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خطیب نماز جمعه دره سن‌گابریل - کالیفرنیا:
تغییرات بزرگی در آمریکا در حال رخ دادن است،
و اسلام و مسلمین نقش مهمی خواهد داشت
وقت دعوت به اسلام فرا رسیده.
مردم آمریکا «باید» به سمت ما بیایند!
باید بیایند!  باید، چرا؟  چون ما «راه حل »
را داریم! خدا راه حل‌ها را به ما داده!
قرآن و سنت داریم!  اینهاست  که
آمریکا را نجات خواهند داد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5020" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puwbST4X25mbie1YYYOP_j7aXAsBWhElmrVBRptAbMeNawMQTdNTCMmIoD1PxO9ogWvu7PkcLuP5muh1p18zyiu73_LjBTdMCqmqkgTdKmQQOifv9iw4Cc44FptSjRHvNL8ADnBPnwVpZK__nsjl0yyUp406GxdhjupLyBxIOErPulTtPDZeDXtyQ5flJW_0oYsEGmK1ZUw1yI7mXy4Xj-l7J3Q7WqXij-x0G25TDGx3Jtah6TIY3sxh6hkh1gM-PrXzzDRGXm4irytjO2VHTxYCJYd8gBcOSHVHizBdl0Cb56-CSwEzMPHIBD0N30gcKMeROd8EYqyEMpWkFG-w6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5018" target="_blank">📅 15:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5017" target="_blank">📅 15:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !
‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا
‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا
‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای
‏۴️. عدم آزادسازی حتی ۲۵٪ از دارایی‌های بلوکه‌شده
‏۵️. توقف جنگ در همه جبهه‌ها [لبنان] فقط منوط به مذاکره است ‌‌دست یابی به توافق!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5016" target="_blank">📅 14:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b64429192.mp4?token=NPzc7g-fcuk6oLqF13V48LxjMgoj7ZjyidjBZdScjlSDCjbUsrYmkitYfe9ozQ-UKAz_fLMkgwyzNbl6O3rZGN7YcccSHRC8loZPbbp2bVeIpkDgdvSLfJi5jC13ujFSkuK_Sv2vgg-3HY7nwQB3rFGJhaIcTN0x2Fqw6hhbK31r2MtcupRIfT64-BxjW-v6x-3HgLXI2zRlvg1MPD9LUe6WnVL3_GQLh69EJhVQdkfXwtf-kB9B9WLt_7XBbfJ506cQrleaCew_yAfE5gNafsga9YQcStlR0RCI3oEuySe_N194djmuIiPaTU64e18q6Cs8t3IvJBOu_f27CAxiUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b64429192.mp4?token=NPzc7g-fcuk6oLqF13V48LxjMgoj7ZjyidjBZdScjlSDCjbUsrYmkitYfe9ozQ-UKAz_fLMkgwyzNbl6O3rZGN7YcccSHRC8loZPbbp2bVeIpkDgdvSLfJi5jC13ujFSkuK_Sv2vgg-3HY7nwQB3rFGJhaIcTN0x2Fqw6hhbK31r2MtcupRIfT64-BxjW-v6x-3HgLXI2zRlvg1MPD9LUe6WnVL3_GQLh69EJhVQdkfXwtf-kB9B9WLt_7XBbfJ506cQrleaCew_yAfE5gNafsga9YQcStlR0RCI3oEuySe_N194djmuIiPaTU64e18q6Cs8t3IvJBOu_f27CAxiUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشه عنبر خانم!
ولی روی این حرف‌هاتون بمونید
فردا که به خاطر ۴۰۰ کیلو اورانیوم
نیروگاه برق و پتروشیمی و پالایشگاه و… رو زد، نیایید بگیم ما مظلوم دو عالمیم و نیت اینها تجزیه خاک ایرانه و… !
اون وقت برو پوست پرتغال بخور و عنبر نسا دود کن .
تا می‌تونید از این ویدئوها پر کنید و یادآور بشید جنگی که بر ایران تحمیل کردید بر سر هوا و هوس‌های هسته‌ای تون بود و دشمنی‌تون با جهان!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5015" target="_blank">📅 10:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=FbUam2sPzrABPRrfFuKTdqUeM31cE2wO9qB97bsMefNCWiBzi-Kc1VbQhTW-Fq81fRK9IbXvu-BN7kJ2D8XCTeTkBz2cB_Ev6OGFDizFnX2VQk6yLB2fzqKRFoPmmO9Mb9bD97Tp8zrqOkHZzrPiX5t6wE25v_-YgT2PAcw_dwgKwjfEa8b1KCT4yIHfwhUWokJGWW0hlRniRpygYjrpaGG6xDdFp18yO3XQbkNvjsL6zhTAqBYlDaSnZVtIuclKmGi4xwSh_cmgHcMtrwlPUmz6tdUILeybiBA35TVeNSmv7OI4qgK9py2YH85N_zppahO1xnd1yYWbC4HbgeC1yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=FbUam2sPzrABPRrfFuKTdqUeM31cE2wO9qB97bsMefNCWiBzi-Kc1VbQhTW-Fq81fRK9IbXvu-BN7kJ2D8XCTeTkBz2cB_Ev6OGFDizFnX2VQk6yLB2fzqKRFoPmmO9Mb9bD97Tp8zrqOkHZzrPiX5t6wE25v_-YgT2PAcw_dwgKwjfEa8b1KCT4yIHfwhUWokJGWW0hlRniRpygYjrpaGG6xDdFp18yO3XQbkNvjsL6zhTAqBYlDaSnZVtIuclKmGi4xwSh_cmgHcMtrwlPUmz6tdUILeybiBA35TVeNSmv7OI4qgK9py2YH85N_zppahO1xnd1yYWbC4HbgeC1yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهزاد فراهانی، بازیگر (پدر گلشیفته فراهانی)
میگه ما … داشتیم و انقلاب کردیم ، شماها هم داشته باشید و انقلاب کنید!
چه افتخاری که جمهوری اسلامی رو برپا کردید!
چطور روتون میشه اینطور وقاحتتون رو نمایش بدید، در دفاع از رژیمی که فقط در سال گذشته میلادی، مسئول ۸۲٪ مجموع اعدام‌های جهان بود!
که ظرف دو شب ۴۰ هزار ایرانی رو قتل عام کرد!
ضحاک روزی ۲ جوان رو قربانی می‌کرد.
در یکسال میشه ۷۱۴ جوان!
در چهل سال میشه ۲۸.۵۶۰ جوان.
کاری که حاکمان شما در دو شب کردن فراتر از افسانه ضخاکه! این نوع از حکومت افتخار داره؟ تباه‌تر از این در تاریخ وجود داشته؟</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5014" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=ADe0J-NjAMQx7dUdOv-zXDcUL8xcBfR3P2JLqnx1ILSEYx0q3bU3CiNemxIMyIYTVLda5hlyKQXBWruOTwQx_mQVXmLlRdqteHr-2LNHMizP4fr5ktadrQiLKUW5H5d0zxgkHuMoiFhFS7HjCnjlGzaZJ5IQAFXMLvlr3XAWdrNMzOG66LF3bK8a-VJVU2m-V9U3XQLA3b-3kUBc2pKFTgFP3DHTcUfXPwHQVPmXkZ1WwCzyea6DtQPkUYuiZOxss-ugIM4sOvAXklvRdcEdpKC9I1dYnzvwnoEHYkSH8Y3vAOjR4fNirbfFkh2PzBAcwjSc9HIqTDZJi1Z83UkIEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=ADe0J-NjAMQx7dUdOv-zXDcUL8xcBfR3P2JLqnx1ILSEYx0q3bU3CiNemxIMyIYTVLda5hlyKQXBWruOTwQx_mQVXmLlRdqteHr-2LNHMizP4fr5ktadrQiLKUW5H5d0zxgkHuMoiFhFS7HjCnjlGzaZJ5IQAFXMLvlr3XAWdrNMzOG66LF3bK8a-VJVU2m-V9U3XQLA3b-3kUBc2pKFTgFP3DHTcUfXPwHQVPmXkZ1WwCzyea6DtQPkUYuiZOxss-ugIM4sOvAXklvRdcEdpKC9I1dYnzvwnoEHYkSH8Y3vAOjR4fNirbfFkh2PzBAcwjSc9HIqTDZJi1Z83UkIEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=CMNwWpIaDLJ190m-d7z7eDqdDmy5LQtE0t1oE17qwq4xH8Gz38ZAJSaIoX2O1Xzqg3wdSAIoeEbsB1dHk7R0_19U4kFFA-rPNMmjpDAO4FZbN_i-Xx-50QKd9zd-T3aLqQi-vDt5vgilU1g8k0ISl3OzenQmWLkkwSQ_w2C9vdCsFqJaFiDdTwVfGT3rz69LZM4PJQOhzgI68w_rMgGmo2kwHxFIwHYiVZlCPKINVdlNEVo09cF4Mn3DV1aseCyQF05YR6MiZxonC6qMtmBvJwgIxrpnYjd_HNdDkRcq7iwdo_3KIzbTzH7sLrz-Dkm3T14LpLWVfhqcPBHNwLdenA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=CMNwWpIaDLJ190m-d7z7eDqdDmy5LQtE0t1oE17qwq4xH8Gz38ZAJSaIoX2O1Xzqg3wdSAIoeEbsB1dHk7R0_19U4kFFA-rPNMmjpDAO4FZbN_i-Xx-50QKd9zd-T3aLqQi-vDt5vgilU1g8k0ISl3OzenQmWLkkwSQ_w2C9vdCsFqJaFiDdTwVfGT3rz69LZM4PJQOhzgI68w_rMgGmo2kwHxFIwHYiVZlCPKINVdlNEVo09cF4Mn3DV1aseCyQF05YR6MiZxonC6qMtmBvJwgIxrpnYjd_HNdDkRcq7iwdo_3KIzbTzH7sLrz-Dkm3T14LpLWVfhqcPBHNwLdenA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=KKVVepsGH58jXafioi7I206GcvD-OyCudI9EEYR4FwtJ2WzSp9UJNx0_EVsuPlaWf_GtWU2-RFo2gWz3VMIxvyMLfxVmqi5FNG_takuROJukyDxBMA8Lu_0d3ChbIwZERBFyGJx644uQ3RqNrzn-kqn-gEOrSGks86zgCLVGjovHedUCPpBsviaVeDs3aG1tg0oJ4DHkRBcqc2F7Wsbk5lvWgxcewFYmR2ZXZ7yI0JOqMOpooiMgmAghu4jB8tGaWvvXCquIR2BSggquYyD_x2vvYyNjU00uNLPTgI_bhj5EEAHsBbb3UQPHYOjKmmt_da_JHrsM3qHAN3j7XIRo5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=KKVVepsGH58jXafioi7I206GcvD-OyCudI9EEYR4FwtJ2WzSp9UJNx0_EVsuPlaWf_GtWU2-RFo2gWz3VMIxvyMLfxVmqi5FNG_takuROJukyDxBMA8Lu_0d3ChbIwZERBFyGJx644uQ3RqNrzn-kqn-gEOrSGks86zgCLVGjovHedUCPpBsviaVeDs3aG1tg0oJ4DHkRBcqc2F7Wsbk5lvWgxcewFYmR2ZXZ7yI0JOqMOpooiMgmAghu4jB8tGaWvvXCquIR2BSggquYyD_x2vvYyNjU00uNLPTgI_bhj5EEAHsBbb3UQPHYOjKmmt_da_JHrsM3qHAN3j7XIRo5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BTUPHM9s9ta1coHqaiTvMFjnsGJZcUccLUWq-rlIbhbmTqurI41Y12gDsFB487IKCFCPoHapURMyNletL-8oyZ-LYgLG5vwNyMzWGJp9ABRI7pDd7AkThyMq8GkkEBhrY4GfchXyc4L6i0VAXIg2-8Jh7jWSfXTs55CJImJ6Rh8y-l7UP1Y2cRlR5KZbqcuPQOzv2a1a-pELZr0QtNdYbS6jzcTNcm4pV0dOl_n-dwEp3cGvzGAbvuDlISCvgj2LbJZhtaul-K3PX1knIE13cCsHM459MWiHdqVotINDenjcp3JAWeTHpRnwVr1wWKCzhRj93WBCDjUZnE5l4XcVLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LaAa9pbeHHWtcH0xbeOG9XSpzw4R0LVqV1AfWZByIMhS5OX-UjKWQSOg3TOJnf0RuH6qFbAe6YRC0EX7p7Srqv2jZO8W_GmnEBjgsBhqmcGofdyM29xN1vPSNOXIYQNwmsG05LNH-5_XqVeCXwbylOWfKQEJ9bXoJcPOcIn5CSAKlRCX_gxwi-jxH91ZQxUG-ZOEHEkco-AZUqT-2pZ-85gf7gd0tSTB9cbOAwruSiEo1ryLHU5zqSZ5LwcF4cY-5UKE7ko09GTJcQa5YZ--U71sbaU2brVirAzE-brUqZSylpFrJeoWQEMvS3Cw2JGO8kqA3HRqVAPb9g83fI4VaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دوستان بزرگوار، این صفحه به‌صورت مستقل اداره میشه و من تقریبا همه زمانم رو صرف انتشار و پیگیری اخبار میکنم.
اگر این محتوا برای شما ارزشمند است و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5008" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">در ابتدای این فایل صوتی که خبرگزاری فارس منتشر کرده، به نقل از
حداد عادل (پدر زن مجتبی خامنه‌ای)
نقل شده که فرزندان مجتبی خامنه‌ای در این ۷۷ روزه پدرشون رو ندیدن!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5007" target="_blank">📅 18:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HcUpwx1wxrJ67nZDMTZAKmlvMW7vu7ZxWQ9l2yQyicW1zGGwNR1x5vRuwVBfYZmXKssS7SOwBvpT3XfaT562-rju7Xp5oblNAJUxsRonDiMrxu-MXrVFrpa_xBXMoBuhfHewdbTIgnYWE5j_1GWm37sMsLWAo4LRJJD66tBBF2y_sPSJ4iFpxvBHMlP3zPktr6XKA4V43aKpw5LghjLpe3HVImUllU19a5h6kU-VQxXHn8PEXjwbwhjsTRQBP8vvEThlWqG_vLyhV8lD6nKcNf2cuEY9F24j4PTzQx3DnUPmqXLTqBb6eOAvGyppLZ1LKAROh6jLZG3EFKilWesyVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VK05-8NX9X5rkN8SouRNpaDeVOpkahcrzkDlA-HsgIXqDMjcyyj_SefKRiMOEQQRBSNtsWeFfzXYUyflhfbpqfjA4sH2WyAnjtDDDmlZ1vxJ5mxhfDFBgUhUcMqah8UmjlKCg20rOcyjZYnK3VIJj3Y2j7rJke4UBFdyzlE1R0uK_WFM4mDGvJdxlpVoWGCPByU3ozR6P2PA3SlHLH7fps9QEqsfX3IVI0qE3UsNLWtVfKqhD8oAyurw1ojbydnZbFbsrqI-s2bmJ0kWOGSlfktmxiqZHEixjN2pj1yYGvLU4lb3fODCdp_bz-3ZdyjZ_R82wZf2uq2FM_6KCF9D1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5005" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=b-x6UNdzAgwEYFrF58FYhGiMVGE3pgPy_3KkNY8l46BMgWtJybF2nFIwqMRnCkvkXE1sJunIXXdDZbzgZMNNE6757A9Xi1WPHg9VMdo6PhBtVqOeixbJ3NbnDSFc-DU2H7asj_25Hbl-MOZJZra6qg35YmjjeyoRnX9gcVPqd1_uTuZpEJAHkYdN1NK3ukUt5Q0_1AsxwKeS6zDBwoHFkZm2iCdbtdXiIB8ulEDfXKnHBJUOALfbXUGjWN5QRv5BYYUcrwr1kp1yzKIY8nGk7PkvhPKQjO-cJtVgkHS70YKtWq1ACiIslOl_figW0MxbFWJikQgLOVpcnCN53gMejQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=b-x6UNdzAgwEYFrF58FYhGiMVGE3pgPy_3KkNY8l46BMgWtJybF2nFIwqMRnCkvkXE1sJunIXXdDZbzgZMNNE6757A9Xi1WPHg9VMdo6PhBtVqOeixbJ3NbnDSFc-DU2H7asj_25Hbl-MOZJZra6qg35YmjjeyoRnX9gcVPqd1_uTuZpEJAHkYdN1NK3ukUt5Q0_1AsxwKeS6zDBwoHFkZm2iCdbtdXiIB8ulEDfXKnHBJUOALfbXUGjWN5QRv5BYYUcrwr1kp1yzKIY8nGk7PkvhPKQjO-cJtVgkHS70YKtWq1ACiIslOl_figW0MxbFWJikQgLOVpcnCN53gMejQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟
چرا خانواده ، چرا فرماندهان؟
چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته
لذا شرایط عادی در بیت بوده»
صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5004" target="_blank">📅 18:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پیام‌رسان‌های حکومتی «بله» و «روبیکا» دچار اخلال شدند و بعضا از دسترس خارج شدند.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5003" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=UK91w1AZb38JH1QQzc8cM_S1FoHSWbhXHlxTHCy367_Ty83I91vglpXiI5I82SffTwXIDdXH7gmQkBqpql6DoxF7YdOrBiqCZVd2ct08JqVkzH4CUqKO823Ex8Uc4-YqbZP9S8l7GQozyhTeUJBa9ohoA0CktmsHa0kkqetJcTOwoaR7Wz4UjGa2bY3TxBqqed7YsW_fzh65U105V-dsGtZSR8UtE1uLskIedR9QHh0Hmprj9NaP7W0rQsaeBlMLfTPIW4weMFB65VkGrIUGf07giTnXsfLBf3sDMlvdQl-8ZTF7HnQbxB8P_0VAZRmZIGWsaSxwMZGbdfpLQDPILw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=UK91w1AZb38JH1QQzc8cM_S1FoHSWbhXHlxTHCy367_Ty83I91vglpXiI5I82SffTwXIDdXH7gmQkBqpql6DoxF7YdOrBiqCZVd2ct08JqVkzH4CUqKO823Ex8Uc4-YqbZP9S8l7GQozyhTeUJBa9ohoA0CktmsHa0kkqetJcTOwoaR7Wz4UjGa2bY3TxBqqed7YsW_fzh65U105V-dsGtZSR8UtE1uLskIedR9QHh0Hmprj9NaP7W0rQsaeBlMLfTPIW4weMFB65VkGrIUGf07giTnXsfLBf3sDMlvdQl-8ZTF7HnQbxB8P_0VAZRmZIGWsaSxwMZGbdfpLQDPILw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=hK3JJosDZCRjaMRlw9tVPVeysEjNzK4s5eY7Xeu7GS0w1R5vjiNOPCTvLjP0O9hhUDXEt6Ny8FE9p9nqdsbdrDNyHnMTNMEMW8sMWgPoYWuU2EXXjnSlx5bSZQ6O0_ADEvkos2Ilk9YjkbL7lt0Pc3UGSaKYYDD3fLqueENCFj7_7NoKtUyJvagrQVCwMULp3FAYeKGDzBthHtfYfdp3MWEAiFgjNPgBd6TbD66qLM9Reh1PCMBjVmLfdJ4kWdQiPXm2-eoGa6RiYd9eiD3AIvmeTda7AAf3lSoIYWTNaHSw57GU2U2FxsBaSUuvEclt--eBQZ0FQPFfTvgP10bMGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=hK3JJosDZCRjaMRlw9tVPVeysEjNzK4s5eY7Xeu7GS0w1R5vjiNOPCTvLjP0O9hhUDXEt6Ny8FE9p9nqdsbdrDNyHnMTNMEMW8sMWgPoYWuU2EXXjnSlx5bSZQ6O0_ADEvkos2Ilk9YjkbL7lt0Pc3UGSaKYYDD3fLqueENCFj7_7NoKtUyJvagrQVCwMULp3FAYeKGDzBthHtfYfdp3MWEAiFgjNPgBd6TbD66qLM9Reh1PCMBjVmLfdJ4kWdQiPXm2-eoGa6RiYd9eiD3AIvmeTda7AAf3lSoIYWTNaHSw57GU2U2FxsBaSUuvEclt--eBQZ0FQPFfTvgP10bMGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.
و نتونستن چیزی پیدا کنیم …..
این همون حادثه‌ای است که میگن
مجتبی فقط کمی زخمی شده
این همون حادثه‌ای که توی
صدا و سیما گفتن همسر خامنه‌ای (مادر مجتبی) هم کشته شده
، بعد از ۱۰ روز  گفتن نه! زنده است!
یعنی وقتی داستان زنده موندن مجتبی رو پررنگ کردن، داستان مادرش رو هم تغییر دادن!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5001" target="_blank">📅 15:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5000">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fp5Ksuh-g3tNEoa56Czava65lF_nYP19gk1T4rkk3XTo38ClHO1vj64XmceJPv7w7K3-76d83EIFNMwJaz3d_UBx69NWWu-nX-yq9E-0SCu_vY1NBw-SuSfEjOUJat_iuCdbMQJwfmeTD9vTZa9IVqoxc8OCWrfwjLwqWclxnunIRJD9x5603Fe9Ijzufp2j7SYZ5BhZlrsLmwiVa_vT4Jam5-yG-dm_wfX9ZLPiTVLfeJ4EcayODuhXgo3-l7EwCYh0N7jAD_7GX_4rBZmgTWm7M85xvdeMZSRXuPjRhu4m9p-wefdrd7yXLOXLvwR5iMNh1_V2DVc-VmInsZciJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5000" target="_blank">📅 15:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=lJC3o6y3H2ROMuXu9Pd56JBRAgRYkcxBi2tzYmfejNum5dRhF-pkDFWOx2BYlqT4H0f9kDWsfgvTbx4FZ1bF1yK2qX9xmmfuXwGXMw8qTffL_tPpA92lQlxbvEsjDwCgNGgmzfzNHq9CAmTBFZYAQUIx6tPg13YRDx3r0Kk86WpLjJ7xOccfYxUfDCIwuL8BBjoCYE73nm1-0UHmc7qvGtDTEzbjGU3OFd_rMdQybpDBVqzc_fD24H75iL98mBJ_oNOHPKyoE4vRntPg10JiZW_Xn4D3IMGumnHJkkbUGY1_GdteKa2kH4UiM7fS8JDIIDWuEeSPYiL-no7N785i3BZJeNbm4iclOI8E9UWsXmRipcFHq-J0LD-BUhqcHgRsPBRLArgcuJblJRJUhurc-ICHck5H_brUW_lLTshlZsEvSlYT8qdme1F0_G8wf2F84fRvUBzi7qLz-fGFRBicOZNl1Wspvxo69dNsvpCH_5Z3TudrIsnGHrY6bBXEWMLmkP9niZ09UkGpg7Pw_hexLXMOJwbmv5D-xoliYKi1KEMMvK0_ZenlYXv9JD1aaDxwRkejebOw_TfqszCtkkb3WzEOanwnpk4v6HhG25v6NP-6fXjQYyU2Th4Ml9cLXz5oUtER3TTLxfgGDujqqcSgDl253YZ4efBpUDbqFYs85Wo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=lJC3o6y3H2ROMuXu9Pd56JBRAgRYkcxBi2tzYmfejNum5dRhF-pkDFWOx2BYlqT4H0f9kDWsfgvTbx4FZ1bF1yK2qX9xmmfuXwGXMw8qTffL_tPpA92lQlxbvEsjDwCgNGgmzfzNHq9CAmTBFZYAQUIx6tPg13YRDx3r0Kk86WpLjJ7xOccfYxUfDCIwuL8BBjoCYE73nm1-0UHmc7qvGtDTEzbjGU3OFd_rMdQybpDBVqzc_fD24H75iL98mBJ_oNOHPKyoE4vRntPg10JiZW_Xn4D3IMGumnHJkkbUGY1_GdteKa2kH4UiM7fS8JDIIDWuEeSPYiL-no7N785i3BZJeNbm4iclOI8E9UWsXmRipcFHq-J0LD-BUhqcHgRsPBRLArgcuJblJRJUhurc-ICHck5H_brUW_lLTshlZsEvSlYT8qdme1F0_G8wf2F84fRvUBzi7qLz-fGFRBicOZNl1Wspvxo69dNsvpCH_5Z3TudrIsnGHrY6bBXEWMLmkP9niZ09UkGpg7Pw_hexLXMOJwbmv5D-xoliYKi1KEMMvK0_ZenlYXv9JD1aaDxwRkejebOw_TfqszCtkkb3WzEOanwnpk4v6HhG25v6NP-6fXjQYyU2Th4Ml9cLXz5oUtER3TTLxfgGDujqqcSgDl253YZ4efBpUDbqFYs85Wo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راس امورشون ۸۰ روزه تعطیله» :)</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4999" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Picz6ydjuYVRbpf9f377Rg5yVVAOwCx1Bqc-vlHNAl3h-7o63U10RK3RjrOn7aQZWynaYj9H5fE2hQuw7izKC3KnVQ_r3oQEKIYQ0hHEVnhNNknQB5CT2jxnvIttsorDZ9FPaQ_ahMcbLhoVxZDY15Vvl3990HpSnXvEpa6ae3Dw6S3g9BWW0MRFnG6jSau_yDnqlAYFUmnbO_nZMEysZFqWb1K4lvbCov80jG9U8osPDpTSukEMoCdlKwRnNG5WYQ90L8KPRL6t2Dn3A1KytjdHfMbI9yxTFJKq60-HeyZaG5VzI4CS8ElvIrkC-khRoGOmoIR_HBLMFtARNas0ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/4998" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af299654a.mp4?token=sIVwGMGGAmEmE9EgQa1amOAtxfbqP2CollN_1HPevC8Qc2TPRY6jiG2iyUTZjXwyzM2U4LuUUuvPPrPOycaqZDd_Yvauc_fnkyVGXkF1bmk4ekUJZI0mH0QhBZDGDGMuxDs4wtVO5Wmv8GCMkhjZxoaC0omLo5ObmIbI_LUnxfd5wtRzt_gWOjQLWBCXzFMQF5dV86359w-a4T9BF3BFWn_G8JAhfCChHi3ULsOGo_wPt8ARG52nIE0KhAM2dE7EYGMoUZ1rAe3vDpkgiRPB3pIinM9oUdaISHF3yN510Xw9Aaq9TweQIcczRn3zdT40IUONnjPpck-KMtfuPR03jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af299654a.mp4?token=sIVwGMGGAmEmE9EgQa1amOAtxfbqP2CollN_1HPevC8Qc2TPRY6jiG2iyUTZjXwyzM2U4LuUUuvPPrPOycaqZDd_Yvauc_fnkyVGXkF1bmk4ekUJZI0mH0QhBZDGDGMuxDs4wtVO5Wmv8GCMkhjZxoaC0omLo5ObmIbI_LUnxfd5wtRzt_gWOjQLWBCXzFMQF5dV86359w-a4T9BF3BFWn_G8JAhfCChHi3ULsOGo_wPt8ARG52nIE0KhAM2dE7EYGMoUZ1rAe3vDpkgiRPB3pIinM9oUdaISHF3yN510Xw9Aaq9TweQIcczRn3zdT40IUONnjPpck-KMtfuPR03jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری تلویزیون جمهوری اسلامی:
- بگذار پرچم امارات رو نشانه بگیرم
- احسنت</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/4997" target="_blank">📅 15:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsxYWDQdBOXwGXXcpxqcbMGToiM9oKBLK8WmGmC3T7119mtFYMcoC_VtnbEiIQWk__r-yeX3tZJltyGHMk5Iy9aDwVM-vaOR9gJ-Y2hESeIOtWTcJy1QF8XlQomir2-j-LSdighX7T9rFgyLuVi6CSwlbpkVpqh9YTWoekntE96OgVzlMffm0y0YwnRVnUWV22old9p3e8FG03aBzTJDcZ752GPZlfaO8CbEkhyh08jSRK-9jvlL2CTif5UbEPUNt8I85PqXNyEJ5H7ccektqZDVRKUWN6KAhP11xVm0DVfe1e-kXOhUD64EPS3MqWhAlYHLdQd4ze05yacl4zc8YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل نیروهای قسام در غزه دیشب به دست اسرائیل کشته شد.
قسام در واقع نام نیروهای نظامی حکومت حماسه.
مثل تفاوت نام حکومت «جمهوری اسلامی» و نیروهای نظامی اش (سپاه پاسداران)
البته ج‌ا ، متفاوت از همه کشورهای جهان، دو نیروی نظامی داره: سپاه و ارتش.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4996" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4995">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYTd50Nk3j1_lVHdNEvccs2nLij0qIhHRxlucSD84tEXqlPIK6_L7urLyP2enGqONXQ6mayh1urPiGRwKcWn-S1Hw5zVBkW16dleNyC5AoUTXfXdazhJqRe7Eyci4cnawoSfhq_WzvPu6ThrfdOZuw5w5WHn8Od74GvOBM0PcR0nga-wg4ycdKP_sAygFOCfYOlCHYaXvKpSCTiGR_f_QZaxW9nvVvmEW7a67md3xn6GfVrplbhrEwoEi7YK5RPJYV9DUbuUQhYuU9QgzwgiRdgChs53lkhS7PtiJWLYCIXOIpWBTjicJTRftRLmlXTQ8wArmF2MVBPDkewE2ZwePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم جنگ بعدی‌شون در ۷ اکتبر که توی تهران و قم و مشهد هم شیرینی دادن و اینهم از ۶۰٪ خاک غزه که از دست دادن!   دیگه توی آمریکا هرگز دولتی سر کار نخواهد اومد که بره به اسرائیل فشار بیاره بیا و به گروه تروریستی اسلامگرای حماس خاک بده کشور اسلامی شعبه جمهوری…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4995" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qplf2z4WISv_kR6xCag6NYn5vVR36imSPI0NcRvEIJbT18p2op217_W3LZ0IaLNvjykf4k5vNR0P2Xi7-QRdFw_vTayHtxrYdRZ6ulkzSUFStIEJNtSUQJAo3j20yvhogCL28i79WOZqTjJOqGEhgI4O7iHaPtWuLmSilUOjg8m25eDsiGsoSA8RD9XnKzvKHE5l8zWTAM5wXAssNgl0un9lmDKUCL1bG5Ilq0-5cYDspQV_Nw5EFDs7m0NxHez_TwdijdNbVVpsB-2Gkgnpf_KM6nHskZhADY4xMYiZ-SpQGzs3sgNNCgHgvhYWq623qvk2w0_PM75pK_w2PDXHjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا سال ۲۰۰۰ از توان خودش استفاده کرد، به دولت اسرائیل فشار آورد، به شما کمک کرد گفت ۹۶٪ خاک اشغال شده شما رو از اشغال اسرائیل خارج میکنم (در کرانه غربی)  غزه رو هم که خود اسرائیل رها کرده!  بیایید و کشورتون رو ایجاد کنید.   عرفات گفت نه! ۱۰۰٪ ! کرانه باختری!…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/4994" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGOG9BCWlM6PcMuX3LvIjMFY6LNFzmnL6SmVYYfm6rrxHnLwl1VGaUBkalxboqTX9T0A4qe8mFqtJjwCeh4SCYpZCQEcdKhH3OXfzTdopYcBEZzI16Yfr48PCRZ3yjHoIuRzc7rpzF1cPxqag7iaRlUVG0rC2o1wYi3V8Zpj8LX_vpNDO32WyBWHqvTTGSpUYtTKaTsyqUfKknIHRQahydQaOX2FwddziFRnA5MRUoD8-GSXUfZBqfU9-LB5Gy8O88TMGi3OL7tzRDnXAL_whe-V2ZekPbvRwTIO99FqEWAw7yXO1D1FP6dLFBTlHDessH0lkfxVkc78fYG5zzVKuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض ۶ روز ، مساحت اسرائیل ۳ برابر شد و غزه و کرانه باختری اشغال شدند!  ولی اشغال نبودن!  برای ۲۰ سال هیچ وقت دست اسرائیل نبودن!  دست مصر و اردن بودن!  دست عربها بودن!  گفتن بیشتر میخوایم! نه بیشتر بلکه «همه» رو میخوایم! باختید! شکست خوردید!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/4993" target="_blank">📅 11:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEKFtyE-GPa8oz97W-NZhQPowEHYTR9q2IJtE8FFqF5MCMfLW8pR1PDXPH5HgiAcXf3JPKwJzEsYW1B5qhp8xx4eCWik12rg-q6Fq84_djqqnzpZn7YcbjNaejBId7ZmuLp1tX4jz-3icIY2853dvfoThGduWdjsb2GXjX5oPa_Qrl7rGCXrY8JsXCZOzxzSJZFmtX4_K0KKrtT-GL0rAbHSg8DgqC0O9PTHb7efjmFZRfUopHdTnhqxlUSIGxpGf-nljJ7refH_K-uv-CqPIwF7tK-5bty5p1B6fFYOOruDHUzSYRBMJPQPJnNw_RSHeVxgZm0Yypv-jvGNOfggZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد برای ۲۰ سال!! از ۱۹۴۷ تا ۱۹۶۷ نقشه فلسطین و اسرائیل این بود! تمام این‌سرزمین ها دست مصر (غزه) و اردن (کرانه باختری) بود.  توی این ۲۰ سال می‌تونستن کشور فلسطینی رو تاسیس کنن! اما این کار رو نکردن!  چون «همه سرزمین‌ها» رو میخواستن!  اینکه دوباره حمله کردن…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/4992" target="_blank">📅 11:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sV8F8U8ogo2ZOvkoCzrsytF9FPmJtnK_62JwyRYKwIgDjtYTeBjFWxO8yMuRHxisCvqJdmrJt3EZRj3t4_AXu_sI-l9mCfcPlQ4HA0uVAoNIRJ_bQLRqZoEzjT03lXCOZW6mrs39IyLsjWU-9eUXj88LkFqfGjOPFJo4jBYv52UjWUdQrqxsWCoOpIq0jFz-g5nFclxodmoKMkoA85QJz5UFga89fLF3xn50lf155LKvgYkjXlxC0TaOz2VoASx8Dl_Vt4Y7Pt-kAqCj-O1G4CQ1LEP2aYaDpP0u1tcGE88G_rW_Sjw1n4ZSNA9A-xKPDdnoI9eUlSrmKsVI8cXxpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی سازمان ملل، طرح تقسیم فلسطین رو ارائه کرد (فلسطین یک واژه و نام یونانی است برای این سرزمین و هیچ ربطی به عرب بودن و مسلمان بودن نداره!)  اسرائیل هیچ سهمی از «بیت‌المقدس / اورشلیم» نداشت!  در سرزمین‌هایی که اختصاص یافته بود به اسرائیل حدود نیمی از جمعیتش…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/4991" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVcEvo0ZexYLvakDZs7Z1HxUUDEvFLMJtQn85s4LOlQstdiRIQ8dSj4E7aMrE1AtpXJfaDbQqWtcg2uN_5lw57X3OwVLSr12RFraxwY9ynpXOoJShbh0b4d9UgijcyKsvoWNlw2bFopZxYO-3ofWsXmwTIW0OhvUZAa68lMj7v8H-nhghjy2yMfvY9jNBoteijao_U57TZFoovnJI3nw_K8qe2YxgovMi_fmGvo1CB4IuRe5cgx2R6y6vL1wVRYXGoEHYDxiGE0hETVUWSyNO1tqRtc8uMKyVOmT2n3u_Bf2UpuTWYy_HuoXqQ43j-8iSgUzo94M9oIaJ0jubiEHKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیل کلینتون :  به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.  اما قبول نکردند و طرح رو رد کردند.  حماس به دنبال ایجاد یک کشور…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/4990" target="_blank">📅 11:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=MShg550IWTGbgqyb2bnVl7ZV0X4jxQYzDXgzu5sLJXFanm5dfYDPKq6Y3GW5xMsQmRVManzgPQbWWZkO6_TxZU89c_o-YZoAiyE0eRP5eya0dJpHxfSYbLUnzqLOSmnUlBabXxSIHbF_-Yr2guG-RFMbQYL1Mu683ojpi6nstg9Gol_yCZN7Nh3Hqype4_gGhVjLEX5DIegFx60SOEQKOUxMPQa8vyhPipqeNaDm1rnr_zeXNBdZ1rNvdPGBzYJroLtrgljvYD_CFQVeFZz9bChAbecIDW4kSBv16liU4NWS2rjkkb57qfeCMez0wNQGUtxS0udluVJPu3xtfss2zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=MShg550IWTGbgqyb2bnVl7ZV0X4jxQYzDXgzu5sLJXFanm5dfYDPKq6Y3GW5xMsQmRVManzgPQbWWZkO6_TxZU89c_o-YZoAiyE0eRP5eya0dJpHxfSYbLUnzqLOSmnUlBabXxSIHbF_-Yr2guG-RFMbQYL1Mu683ojpi6nstg9Gol_yCZN7Nh3Hqype4_gGhVjLEX5DIegFx60SOEQKOUxMPQa8vyhPipqeNaDm1rnr_zeXNBdZ1rNvdPGBzYJroLtrgljvYD_CFQVeFZz9bChAbecIDW4kSBv16liU4NWS2rjkkb57qfeCMez0wNQGUtxS0udluVJPu3xtfss2zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیل کلینتون :
به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.
اما قبول نکردند و طرح رو رد کردند.
حماس به دنبال ایجاد یک کشور و یک میهن برای فلسطینی‌ها‌ نیست. فقط به دنبال کشتار اسرائیلی‌هاست.
🔺
بعد از عملیات ۷ اکتبر ۲۰۲۳ ، اسرائیل ۶۰٪ از خاک غزه را نیز تحت کنترل خود درآورد.
در تاریخ ۷۰_۸۰ ساله اخیر، هر بار جنگی راه انداختن تا با جنگ، سرزمین بیشتری بگیرند، بیشتر باختند.
🔺
امروزه در دنیا، نه آمریکا و نه کشورهای عرب، هیچ کس هیچ فشاری به اسرائیل نمیاره و دیگه سرزمینی به فلسطینی‌ها تعارف نمیزنن! هر بار بهشون تعارف زدن گفتن کمه، جنگ کردن، بیشتر واگذار کردن!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/4989" target="_blank">📅 11:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAkD7NIzDi0i15uPTf_RxHRO70zJotanNz7O1thlUbFahTqBPI25zswCuB9yZUQ97sP9h2wCN2Et0Tme2OuV2VshLa7EXkJj5yl2cFES1deEN_Exi1dRTVpipVYUisfMSz9c06c4K9UP4nKw2j7vv6Ka03AJA6wqe0-pCHZ1o3txiJ20m56yIadbG-6SVRM8q0lr4XGY2t8XkPpyuuwaQS_O5GwY5SSNpYMoE7yhjJVvgn10EPnjaSW6EiSw0FgYxSOcKcLEI2PNTFBJvetpNmeglad465oRLT8ycFPgvVt5RmDzlES6uqfl4ZJlbum8qVv106SMbniK59WyiIE_ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/4988" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9fS2RT8h6bbTqhUieiXBjZzDbVqehCUSDaSAbV1j-Bz1maJexossEvmAuiwDnQzK8UnoTEfijYqcgGi9gqnGBXn-lH-FcCYBLTQ-FvwK2ZhlRfhEO0T6foxBoaOvTTta3NUD7HVw_YcFG14OIgFI-2EDEmPO59E4qOKvfub6M_kyZIZNXO-uc5P4P9zLhUIPItUxE509SGgEgwuHmzLgOVABT-z2uW3S2ijOSHFMaU-4vnAr77lsS-rB9ZqjI0L52BuOPl690PDddcP0xAmDyMS-PAt5jOdfq1IEcKF3yjMnZ2MGiRM5RcvHYPkLhvNb6pqw-fqlsdesyvGNtUiDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4987" target="_blank">📅 10:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4986">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=HBEKGTLH_F2OGTg_baHsvOI9aIMDbGxqNHdoO4cQwq9mF7IBBGdciRa6LCdbDLT_ixk7_OaXkboNxq8GahppiVwKSGc8lQWjC6deOS67rUWO_ePiYyGeYhN_Vho6SRxUvYSzix5eMEMtt_LWFYq4RKdQLg2z4vugNZZ6BMN4oEBR15G9n2_ynhrqcnKWuBct2zIQItGvx7mYywi07g0-LPKwf_vluqCUub7ptCpslj99kd-Xq51ynrfmLlPSM2U8sDfRcMBdclMGVuJWuuwqss-si_mzy97zMK9aYDtpugZkCXkKCn_BFxUiUTAAbj446-c9t2KQt518PCpHbWgrxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=HBEKGTLH_F2OGTg_baHsvOI9aIMDbGxqNHdoO4cQwq9mF7IBBGdciRa6LCdbDLT_ixk7_OaXkboNxq8GahppiVwKSGc8lQWjC6deOS67rUWO_ePiYyGeYhN_Vho6SRxUvYSzix5eMEMtt_LWFYq4RKdQLg2z4vugNZZ6BMN4oEBR15G9n2_ynhrqcnKWuBct2zIQItGvx7mYywi07g0-LPKwf_vluqCUub7ptCpslj99kd-Xq51ynrfmLlPSM2U8sDfRcMBdclMGVuJWuuwqss-si_mzy97zMK9aYDtpugZkCXkKCn_BFxUiUTAAbj446-c9t2KQt518PCpHbWgrxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین یکتا، همون چهره‌ای است که قبل از شروع کشتار ۱۸ دیماه اومد تلویزیون و گفت خون هر کس ریخته بشه پای خودشه و بعدا گلایه نکنید!…
این همونیه که اومد حامیان رژیم رو دعوت کرد که هر شب برید توی خیابون‌ها
حالا هم در کنار تیم ملی فوتبال، در یک اجتماعی اینگونه رسوا، داره مجری‌گری میکنه و میدان ‌داری.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4986" target="_blank">📅 09:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4985">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمملکته</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=vvHcALIk0BxFvx37Tv7yl0tPm2vr9BphaDGnsohZHnTI2vAhD-H6gqCmJ0jQTqoirwusc7ikITaM17JEAMRDZQT_Xr-XJBlv7I_bmTw8rq1uxBCsZ1WuIxfN24F84Ku_HwFxhmku_TOBzEUCCQaHr5pjlMRuhDXODrBV2SQn8Ru3e3WaGPB0g95gymjYmgE1D_5fyrhfYDZyqLY5PuLWm5Kvc2mCLHnStkge2soPrCZaXu0S7z5cZv0nRUGz_H5OCWSaYnDLiPVfTTSg4t8bDZ9s5J5SEUvCATG0q8g39Zp2mmYTzn-fr_Pb004uBC4pGRtoG_lPqmbLvI2dEwwFIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=vvHcALIk0BxFvx37Tv7yl0tPm2vr9BphaDGnsohZHnTI2vAhD-H6gqCmJ0jQTqoirwusc7ikITaM17JEAMRDZQT_Xr-XJBlv7I_bmTw8rq1uxBCsZ1WuIxfN24F84Ku_HwFxhmku_TOBzEUCCQaHr5pjlMRuhDXODrBV2SQn8Ru3e3WaGPB0g95gymjYmgE1D_5fyrhfYDZyqLY5PuLWm5Kvc2mCLHnStkge2soPrCZaXu0S7z5cZv0nRUGz_H5OCWSaYnDLiPVfTTSg4t8bDZ9s5J5SEUvCATG0q8g39Zp2mmYTzn-fr_Pb004uBC4pGRtoG_lPqmbLvI2dEwwFIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
جمهوری اسلامی به جایی رسیده که نفر آورده با ماسک آموزش کلاشینکف تو برنامه زنده صداوسیما میده
📝
توان جنگیدن با آمریکا که ندارن (در صورت جنگ زمینی)، این برای کشتار مردم بی‌سلاح ایران در اعتراضات آینده ست.
📝
اسلحه بیاد بین مردم، فرصت انتقام تعدادی از ده‌ها هزار نفری که توی دی‌ماه کشتند هم بوجود میاد اما ابعاد این احتمال بزرگ نیست. ابعاد احتمالی مسلح شدن، اختلافات بین باندهای مختلف مافیای اشغالگره که با تنگ‌تر شدن محاصره اقتصادی، از خشونت سیاسی به خشونت فیزیکی دست خواهند زد. برای پول راحت‌تره آدمکشی تا برای عقیده.
@mamlekate</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4985" target="_blank">📅 09:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4983">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShFnqAV25mVEVVNpyq8jSdpBalp_m522IeLV8T0gkjeJ3pNfVRpb3hg7dB2vmIx2ycN1BEJVz0_kDw91Zz_Pa3pau-E-VShQ6YGypIgYv_weIQqlPObe7r97NmP9AeTfqPmPQM49c4wdkju2c1n3pKRx4YDC3ixvLTYKnBnecfCQTMbFAiV9v42B1VdqtsjE2XflQzCXe0I_1kUpcmFYAP-bXMzupCe5vIDurKUt0XLnVu0oS8FcgBRoW9tQZ5fYXnGsaN5SXXqFKcOKJ-EBzoBt1rdMKydRa-2JqbfgmqhX5LAp1Pxl7GYmM-c_aDwnh00_YqcgmCVYn_wYQnTUVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=AyIBz1YVdU9WLsX9zpyG0ttJX9LwstWpvTfEsJh-Cc9QrDXcQVtDrLuHjWau7dNcZs3itFtlW-6CH-pSgpytOhHk6NrRMFazsrjJXiid032k62gRH0poWuJNy3OJp-C_juVTOyx66BcF5uHTKSrXKx8dqvOQsABv4lVrL1LiEi_UxaHpLzy_qgZfkXwhTNqyDXwHaZhwFira7S2cTLtU_G3mU0-DngvVb-SshnphOqR8TRm_yelnQIsfja17Vk6Ez7DOG6rRwN_ZGgdI79CMiFtFjteFQefKuyNje6PcYLpjR8MkIwGrjCBqPlVpPNvv44etp1TJaMgpQdjnTMUWbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=AyIBz1YVdU9WLsX9zpyG0ttJX9LwstWpvTfEsJh-Cc9QrDXcQVtDrLuHjWau7dNcZs3itFtlW-6CH-pSgpytOhHk6NrRMFazsrjJXiid032k62gRH0poWuJNy3OJp-C_juVTOyx66BcF5uHTKSrXKx8dqvOQsABv4lVrL1LiEi_UxaHpLzy_qgZfkXwhTNqyDXwHaZhwFira7S2cTLtU_G3mU0-DngvVb-SshnphOqR8TRm_yelnQIsfja17Vk6Ez7DOG6rRwN_ZGgdI79CMiFtFjteFQefKuyNje6PcYLpjR8MkIwGrjCBqPlVpPNvv44etp1TJaMgpQdjnTMUWbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/4983" target="_blank">📅 09:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏ترامپ: امشب، به دستور من، نیروهای شجاع آمریکایی و نیروهای مسلح نیجریه، مأموریتی بسیار پیچیده و با برنامه‌ریزی دقیق را برای از بین بردن فعال‌ترین تروریست جهان از میدان نبرد، بی‌نقص اجرا کردند.
ابو بلال المینوکی، نفر دوم فرماندهی داعش در سطح جهانی، فکر می‌کرد که می‌تواند در آفریقا پنهان شود،
اما نمی‌دانست که ما منابعی داریم که ما را در جریان کارهای او قرار می‌دهند. او دیگر مردم آفریقا را ترور نخواهد کرد یا به برنامه‌ریزی عملیات برای هدف قرار دادن آمریکایی‌ها کمک نخواهد کرد. با حذف او، عملیات جهانی داعش به میزان زیادی کاهش یافته است.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4982" target="_blank">📅 09:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=TniUe7E21qUljsLrwGHcMjg7OnZqIybZiiWhTmUTZeEqZEa2In7POxnLS2q9NExPE8hMK4MTkCT31nHxUxA7MG53C0rha6LqGO3GUJV8YrLZ6LxqxosG2r8VWCxWbBCp2_dzNbAtAQhUSdW4d6rwvhBrqXojLYCUTrFIMOL8uW2mT8i8xFMFC5Iv9h1ynXeFJmj2SP5RVxSf_eTKqplp__yERMflQmD9TVL9JqsgmFLyoa87hsawNHRoZb13jCKG-YudSiN-5YtVBYFzS4Mh-04RBRx-qKEyT7iaQqa-accvCTysRaX4Cs6tHmdI0PEUHQYK-zBj_6zTnCO7ijKTAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=TniUe7E21qUljsLrwGHcMjg7OnZqIybZiiWhTmUTZeEqZEa2In7POxnLS2q9NExPE8hMK4MTkCT31nHxUxA7MG53C0rha6LqGO3GUJV8YrLZ6LxqxosG2r8VWCxWbBCp2_dzNbAtAQhUSdW4d6rwvhBrqXojLYCUTrFIMOL8uW2mT8i8xFMFC5Iv9h1ynXeFJmj2SP5RVxSf_eTKqplp__yERMflQmD9TVL9JqsgmFLyoa87hsawNHRoZb13jCKG-YudSiN-5YtVBYFzS4Mh-04RBRx-qKEyT7iaQqa-accvCTysRaX4Cs6tHmdI0PEUHQYK-zBj_6zTnCO7ijKTAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها نشانه سقوطه. نشانه هراس.
پروپاگاندای پوشالی رژیم رو باور نکنید که میگن بعد از جنگ قوی‌تر شدیم!
اینها ۷۰ روزه رهبری دارند که خودشون هم تردید دارند که واقعا داشته باشن.
اینکه ۷۷ شبه، هر شب هراسیده در خیابان جمع میشن. اینکه ۷۷ روزه اینترنت رو قطع کردن و علنی هم میگن چون ترسیدیم و …
ترس اصلی‌شون هم مردم ایرانه!
و اینکه خون اون چند ده‌هزار ایرانی که ظرف دو شب کشتن ، حکومت ظالمشون رو غرق کنه.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4981" target="_blank">📅 08:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tshKnrUb4XwCZdTY-qUUV7rOvDVjXmVMraHK5FmI0dGpxXfRe2_Xwk2Q3HJx1vItpBuSzHP9DZ6Ym6OMMC0xzYdlG7bzVqJcg3af8iTBvrlMhoYcEJUJQ2yTMnm3tMkEL7M_RL2YT75J3ZORg763U0-AEn0UtoJpzqesRp55Ldbpg0Z8EPqvHsymims8Y1tSvx0XyKyYrryzYcS6Ji9lZ7nfFIqtAJbbNOoX7gcfPgmpXF8_dK6idCs8-5E6J67X0pyfby0y64ivLphW7sqPJHJyDCpSOrBPYdmPquEK0-SV5MRD_qExf51qtEguDsJpF9Vbs8ivB2s9usYFIj_eew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفت‌وگو با فاکس‌نیوز با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او 'گفت: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا گفت شی جین‌پینگ، رییس‌جمهوری چین، برای کمک به حل بحران ایران و بازگشایی تنگه هرمز اعلام آمادگی کرده، اما تاکید کرد واشینگتن «به کمک نیاز ندارد.»
ترامپ گفت چین «۴۰ درصد نفت خود» را از منطقه تنگه هرمز دریافت می‌کند و افزود: «اگر او بخواهد کمک کند، عالی است. اما ما به کمک نیاز نداریم. مشکل کمک این است که وقتی کسی به شما کمک می‌کند، همیشه در مقابل چیزی می‌خواهد.»</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4980" target="_blank">📅 08:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBvZYBFAC6jgihLhg7EoIDuQI8LnhVahG-6j5YXbEAh86tBCaFM1GCuQM9XQ4Bw9P_MwLCvsNV35belRYjugyvyRlRIO2xZMUxx8YToRaQRqvV_XyUORqcPYR0DAu-NZQ5ba3oKoqWmmzNj_e8SlqXXxDnqRgNZu0r3RGQqhxZN7p6QT5PMislarw1olZThgZ4I0RW3ypAolySajo_AGEIn-uxo0XRlOk9ByBd5zh5gxXHPGf_u5ICPJHrS1K-__EjPay5kmbb2c2R7yfZzYyLDoTTHsQcMPjqdYjDaRBZkNJS-vW3nYGA2r_3UDYMoazPebnXd8jKAULuFQC2ydPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن رهبر شجاع‌شون  ۷۰ روزه قایم شده
یک عکس بیرون نمیده!
یک فیلم ازش منتشر نمیشه
یک فایل صوتی ازش منتشر نمیشه
پیامی که میده حتی امضا هم نداره!
از طریق امضا می‌تونن جاشو پیدا کنن؟
یا موضوع چیز دیگه است؟</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4979" target="_blank">📅 19:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7uvDbkNLzl2drCUQHLGZutYP0RSGixgj5T766xXsjzTU9L_arJ1UMOBmCTdjVJBzrNaq5DKydNhCWg2hHdTIxmQXP4Ns0uFURt0F9UlSKJnU9bWOW1pC3MOeGaWL31QdoklLKakfRLQpRjyYzDw691OmMzHv4kIuoJux4ZLE4xzOmaDw_cFCParEXr6spvqI8gdPVFt9jH7mvEuwZWkwOx2Z1wWb8xm9zSTl31uZhMM2Sj1hj9BRMi_RbyEdnrv_C-CQ5ELy_iF4xBVjJtBJB_gEdrubQBTqANBi4N31fqZhoa5ev5yhEthMDndpQwAbAJ6ffI40Uw4hZvdOfgINQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/4978" target="_blank">📅 18:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVkfFb8rxvVxdFF07RyhOBOvGOcRKDVFatOZ2s8pgUzwAzanjZ2r9Iz33hvftOULIbDFdzMTMujLqe3f_sfQxSfWKpDiviFl5OoxzhCwAoTm5vf-DvAXmgJ0vVSMPmbypLmkE0YfVsdgiPSuRXhVttUomSjXi-W3qoAf534ky56DUpdzUfNCPk6KGXML3uFFVJNfoug6jJum6vFUPXJrMnljPYKe0-W2lRbjFU2lwldPHsm1holrtvuMXCkRuAccBV8B27wyGbY0DbMFZcY_MlmoYGMUIElGiPJAGWPsIhpDzOcv6wsSAfo93BI7Rh9pMgL8-FW5rMGC7-nn95EDIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت آمریکایی تمام هدایایی که چینی‌ها بهشون داده بودن، قبل از سوار شدن، در سطل آشغال ریختن،
نگران از اینکه مواردی در این هدایا باشه که برای جاسوسی استفاده بشه.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/4977" target="_blank">📅 16:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
برد کوپر، فرمانده سنتکام، گزارش‌ها مبنی بر اینکه جمهوری اسلامی هنوز ۷۰ تا ۷۵ درصد از ذخایر موشکی و پرتابگرهای پیش از جنگ را حفظ کرده است «نادرست» خواند. او در جلسه کمیته نیروهای مسلح سنای آمریکا گفت ارزیابی‌های منتشرشده درباره توان موشکی جمهوری اسلامی با واقعیت مطابقت ندارد، اما از ارائه جزئیات اطلاعاتی خودداری کرد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4976" target="_blank">📅 16:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=q6yHJkxltEB42JyjAYdeIpThjc5OX_gWteInSuk4f2vSrd3UbRPFtrtt7uwsUZ30xoom0fbP8IIqi4nTZNT8Id1oNoU166hIBJcnYrTbb0hWe1hBwqxaqt0j-VtPEFBKPnDrQMTgtn2G28vngfTOeNkNeQn7vibjxzV2bl3vZJoAsypbF6jVN08MLkQjlPkpVXj25ixXMechEKgO4uVjpbOBl6l_WBBtNQqE0zqmRidCGgxAxRUE2md3kTLqAzGy9nE1_Fkl4sS3dZYn14KhIturMl-g7mqzhC6c9-yhOQC-2bq3RaHL-TqLtyiqCa4qd1htUY7Pky4g2h4CNU7ZVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=q6yHJkxltEB42JyjAYdeIpThjc5OX_gWteInSuk4f2vSrd3UbRPFtrtt7uwsUZ30xoom0fbP8IIqi4nTZNT8Id1oNoU166hIBJcnYrTbb0hWe1hBwqxaqt0j-VtPEFBKPnDrQMTgtn2G28vngfTOeNkNeQn7vibjxzV2bl3vZJoAsypbF6jVN08MLkQjlPkpVXj25ixXMechEKgO4uVjpbOBl6l_WBBtNQqE0zqmRidCGgxAxRUE2md3kTLqAzGy9nE1_Fkl4sS3dZYn14KhIturMl-g7mqzhC6c9-yhOQC-2bq3RaHL-TqLtyiqCa4qd1htUY7Pky4g2h4CNU7ZVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : می‌دونم سؤال‌های زیادی در خصوص سفر چین وجود داره ولی بگذار اول در خصوص پیشنهاد جمهوری اسلامی بپرسیم ، آیا شما طرحشون رو رد کردید؟
ترامپ : من طرحشون رو نگاه کردم از سطر اولش خوشم نیومد دیگه انداختمش دور!
خبرنگار : توقف ۲۰ ساله غنی‌سازی برای شما کافی نیست؟
ترامپ : آره توقف غنی سازی ۲۰ ساله خوبه، اما در تضمین این توقف تردید هست باید ۲۰ سال واقعی باشه نه ظاهری</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4975" target="_blank">📅 15:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
ترامپ در خصوص ایران: ‏«ممکن است مجبور شویم کمی کار پاکسازی انجام دهیم، چون یک آتش‌بس حدوداً یک‌ماهه داشتیم.
‏ما در حقیقت آتش‌بس را به درخواست کشورهای دیگر انجام دادیم.
‏من خودم چندان موافق آن نبودم، اما این کار را به عنوان لطفی به پاکستان انجام دادیم، آدم‌های فوق‌العاده‌ای هستند، فیلد مارشال و نخست‌وزیر.»</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4974" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا دیروز گفت که : «در جزیره خارک در سه روز گذشته هیچ بارگیری نفتی انجام نشده است. معتقدیم مخازن ذخیره کاملاً پر شده و هیچ کشتی‌ای وارد یا خارج نمی‌شود.»
او افزود که این وضعیت باعث تعطیلی قریب‌الوقوع تولید نفت خواهد شد.
با این‌ وجود امروز خبری منتشر شد، مبنی بر اینکه  یک تانکر بالاخره بارگیری کرده و اعلام شده که «برای اولین بار» در طول یک هفته اخیر بوده.
جمهوری اسلامی بخشی از نفت اضافه خود را در تانکرها و نفتکش‌های کهنه و‌قدیمی ذخیره می‌کند تا جریان‌ تولید، نفت متوقف نشود.
با این‌ وجود و در صورت صحت این دو خبر (عدم بارگیری در سه روز اخیر، فقط یک بارگیری در یک هفته اخیر) این به معنای مشکل جمهوری اسلامی در صادرات و یا ذخیره نفت است که می‌تواند به توان استخراج و تولید نفت ضربه بزند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4973" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔺
رسانه‌های اسرائیلی : ترامپ در بازگشت از سفر چین، در خصوص از سرگیری دوباره جنگ با ایران تصمیم خواهد گرفت.
تحلیل شخصی‌‌‌ام: گره میان جمهوری اسلامی و آمریکا و اسرائیل، از زمان روی کار آمدن مجدد ترامپ تا وقوع جنگ ۱۲ روزه با گفتگو باز نشد،
سپس در مذاکرات در حد فاصل جنگ ۱۲ روزه تا وقوع جنگ ۴۰ روزه، این گره‌ باز نشد،
از زمان آتش‌بس تا امروز ، که ۳۷ روز از آتش‌بس میگذرد، از جمله در مذاکرات سطح بالای اسلام آباد باز نشد!
بلکه حتی این گره به واسطه بسته شدن تنگه هرمز، کورتر هم شده و هم به واسطه حمله جمهوری اسلامی به کشورهای عربی منطقه و پاسخ نظامی آنها، وضعیت بدتری پیدا کرده.
از آنجایی که هم جمهوری اسلامی خود را پیروز جنگ ۴۰ روزه می‌داند و این موضوع در مذاکرات اسلام‌آباد هم کاملا واضح بود و عامل اصلی شکست مذاکرات شد، و هم آمریکا خود را پیروز جنگ ۴۰ روزه می‌داند، اما تمام مشکلات هسته‌ای، غنی‌سازی، موشک و… سرجای خود هستند، پیش بینی وقوع جنگ سوم بعید نیست و احتمالا این بار جنگ با حمله به زیرساخت‌های ایران شروع شود.
برخی از کارشناسان جمهوری اسلامی در صدا و سیما حتی پیش بینی وقوع «چند جنگ» در دو سال آینده را مطرح کرده‌اند.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4972" target="_blank">📅 09:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6XmITT35KKaft0JSpGsedfc51rVGdNtKnihttw23SvESM6vCqSS104fZYG0-rm3nHbLmyORiEnPYAoWePAZvNDE_6LYZ-qNmn1WEpmPUqyL3zgfwjDbK4jy6MN2vKx1Id8T72n9OzWxH6nmPb-Z4hWy1W9B3BZgPsURxLMLMXBUuXi6GEOh7zIP9Z1UrJtO3ZFqKhiRTn9ZcJowdYrW1lTqRQByTk--42uPVn0QRYOPmp16fsBnQBTdxz7wbw9COTBi4OvmmxTDvX7XbQtiA0OAggmBHcxsw73_I4ZbtLL3HWn52UlCfFacgnDn0QBzTtGfiAHamTTjPTIPk2JOOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WD3OF4xbcGD8Ciws6DX1Bp4e9LqBkh-cTucuJdveobtTFVgwjhkKJAQqwUf9Aofd34dj4Is1GTbrqvGkxvB1aBVItWQFfz8IU_3kRUdKb-DdaW3jbN59kl1zXg-9RiJo_tpYmKYPtQaRy_yQpM5gOaUHR2zc8wAlH0dZrHDSdZOuqPzVvraV_13AcwK8MCvjoiF5CNfAYJesw-UQtK6Dj1Ta4jlfugkwcB-ZYAPawxgc-kbABNZfqj9nELsMKOIvf0qUpvCKHjDgDf1QgAtfQTGqD0QlTnTeUBgWkyN0HY4c4x740x06UZXFT1rAtApzTufZONRhrLwNcPDirLanng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی توییتی زده
که «هر کس در نهان خیانت کنه، به طور علنی رسوا میشه»
که منظورش اماراته و بحثی که بین عراقچی و نماینده امارات در جلسه «بریکس» رخ داده! و اتفاقا حرفهای عراقچی نشون میده که امارات بوده که اینها رو رسوا کرده و به شدت ناراحت شدن از حرفهای نماینده امارات که چرا در این جلسه چنین حرف‌هایی زده.
اما با زدن یک توییت! اعلام پیروزی میکنن!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4970" target="_blank">📅 08:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDzYKnKGqi0-9DVMZeTDvfvxTa_9LgP8dDiqd9-yUQGJ6CnGRrV06IvjE7YbgKUCv8PU3273D0j1psi-gycPxLWxNrSMOvM0p11SqJi0bztjO9KED5f08uMXMkpvdd58Efe-zYvhuVtajlflf27hiC23Qjj9LwyaGiUmLmaS0fPmSa5NxKDkN5siIvCkAZ5sBJQ3D_EqCc1zSqSwfv1YuycluLilfoUg3jvdkTxfv7c5ACk2472r_4hebeof9oqGRxatmzZehmv1zKiakMMXGYShMdJhj_s0nXwYiUMDuQB11r2TsTv-BiACQd-lfJtFoaxz8fiBdR01YVVkk0h4Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس جمهور در صدا و سیما:
با علی افشاری، پرستو فروهر، عبدالکریم سروش و….. تماس گرفتم
و از مواضع آنها تشکر کر‌دم</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4969" target="_blank">📅 08:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نامه رسمی کشورهای عربی به سازمان ملل برای درخواست غرامت از ایران
بحرین، کویت، عربستان سعودی، امارات متحده عربی، قطر و اردن در نامه‌ای مشترک خطاب به سازمان ملل، خواستار پرداخت غرامت از ایران برای خسارت‌هایی شده‌اند که جمهوری اسلامی در طول جنگ به این کشورها وارد کرده.
این درخواست در نامه‌ای که دیروز به آنتونیو گوترش، دبیرکل سازمان ملل متحد ارسال شد، گنجانده شده است. در این نامه، آنها همچنین ادعای «غیرقابل قبول» جمهوری اسلامی درباره قوانین جدید عبور کشتی‌ها از تنگه هرمز را محکوم کردند.
پیشتر نیز در اجلاس اضطراری وزرای خارجه اتحادیه عرب نیز قطعنامه‌ای تصویب شده که رسماً از ایران خواستار غرامت شده بود.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4968" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=N8XPBgxeDw-cPVBqiFdpclwKI9qC4BJOlrOiK6sbjQHrYL7z7yx2f2EbcU7R78oNhh_V33_dBhk4T6ZD5ATONazOc36smeBEOu56YiXwjpPVFyQuEaLSLR_AZNZelto6CeEaK6EVtQVc0udvPzGQUqS56P4_PpPYRvkI3FOAC8J22iYqvh8ZSQ3cEFliCMDmKEBLKb-YNesH4ERxnGpcAA32r_bGwJCJl690miIE41uQoJYEHvnEBMrWkZ9fIz3RRJhj8Mu90mmyu-tOEtZk-7TCw_17MABIWzgXjZpoYiyplrCa0C6QBKDGD5XD7yHikU7qm1sChAWJzNIUQpE3eZUx85ITMXULPJLSgZkNH05e2qlG1KZvDSliI3MWOyOzPmShHuC0eqUI1GvhLx_IpM4XNfTTF0CEwqpipqo5e1DfjR8wUBPLX849LIY46Mq_oenTkB66EXZ1OHTcXiWg631gUN4uxnyKJAqhls-tTX1USZTfPi_MVIcCcTizePSYpEmwmCCwpk2WjL84qvmRMqtzD6Gv0rxj1EqI03Vun7nmgKyJDx6Fs2HXZAF7YgGpxj4PfwRtHXzew1eEEb1u2btI77Kw55Ej37zBRpKgYQxFBtJzeDR-jr8vd1nqMoNxbG7nrc-KpHzUKI5hvIuvSWEEp4Z95QovznFKCigldqI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=N8XPBgxeDw-cPVBqiFdpclwKI9qC4BJOlrOiK6sbjQHrYL7z7yx2f2EbcU7R78oNhh_V33_dBhk4T6ZD5ATONazOc36smeBEOu56YiXwjpPVFyQuEaLSLR_AZNZelto6CeEaK6EVtQVc0udvPzGQUqS56P4_PpPYRvkI3FOAC8J22iYqvh8ZSQ3cEFliCMDmKEBLKb-YNesH4ERxnGpcAA32r_bGwJCJl690miIE41uQoJYEHvnEBMrWkZ9fIz3RRJhj8Mu90mmyu-tOEtZk-7TCw_17MABIWzgXjZpoYiyplrCa0C6QBKDGD5XD7yHikU7qm1sChAWJzNIUQpE3eZUx85ITMXULPJLSgZkNH05e2qlG1KZvDSliI3MWOyOzPmShHuC0eqUI1GvhLx_IpM4XNfTTF0CEwqpipqo5e1DfjR8wUBPLX849LIY46Mq_oenTkB66EXZ1OHTcXiWg631gUN4uxnyKJAqhls-tTX1USZTfPi_MVIcCcTizePSYpEmwmCCwpk2WjL84qvmRMqtzD6Gv0rxj1EqI03Vun7nmgKyJDx6Fs2HXZAF7YgGpxj4PfwRtHXzew1eEEb1u2btI77Kw55Ej37zBRpKgYQxFBtJzeDR-jr8vd1nqMoNxbG7nrc-KpHzUKI5hvIuvSWEEp4Z95QovznFKCigldqI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور چین، شی جین‌پینگ،
با موارد‌ زیر با رئیس‌جمهور ترامپ موافقت کرده:
۱.
در موضوع ایران، به آمریکا
«هر چیزی که ترامپ نیاز دارد» بدهید
.
۲. سویای بیشتری بخرید.
۳. نفت بیشتری از آمریکا بخرید.
۴- ال‌ان‌جی بیشتری از آمریکا بخرید.
۵. ۲۰۰ فروند هواپیمای بوئینگ بخرید.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4967" target="_blank">📅 20:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=D2n6JZaEPpqmorX0KGex7vUAAlkoU2dqX1_6wITmO7Lsa71i-gWTKNKRioOwg8xu42UoujVt07VgVSjQhWWiRso3YBtFHoYZxuMWky60lFnS09uEFM_1LiCkllsLZpx34JMT_21AkFXY-I8gezbmtfC9f0fIvUTMSod4mfhfhoHJD8Oy1EIctR_n1-rWnynjyUnwNIwv-PkwVBuIBQLrZOfpIFXYrN8kmHB1iqic9QDEFeAMgUraM8jw952hGQaxVfOzXN-23lSPQW1h5PO5yyBlAdO4QfpU0Cr1THSDjgf2csPmi9fil-olBB7OqUOcqc5f8ckdt0J__6k9fBdeIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=D2n6JZaEPpqmorX0KGex7vUAAlkoU2dqX1_6wITmO7Lsa71i-gWTKNKRioOwg8xu42UoujVt07VgVSjQhWWiRso3YBtFHoYZxuMWky60lFnS09uEFM_1LiCkllsLZpx34JMT_21AkFXY-I8gezbmtfC9f0fIvUTMSod4mfhfhoHJD8Oy1EIctR_n1-rWnynjyUnwNIwv-PkwVBuIBQLrZOfpIFXYrN8kmHB1iqic9QDEFeAMgUraM8jw952hGQaxVfOzXN-23lSPQW1h5PO5yyBlAdO4QfpU0Cr1THSDjgf2csPmi9fil-olBB7OqUOcqc5f8ckdt0J__6k9fBdeIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/4966" target="_blank">📅 17:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2182de948.mp4?token=OgWMKOzngB6xiXkNM1in64ZqMXNryMXtVRsOsZdjVp2iHmook2f9U5NrA2_cvyCsMgxitnw1EGwaTaR3-LOyJQCIwgq5cW7w74eKRP-uidshQFedTYg69-C5jHvCXJ3r93nZt8muiEAFtLvZInFr-PtasuQlhigODoETDsi1uDGItxASAr8eJqryfkRV9ByVsIolabI5tNelH7jOkfPv4vTnDz-XXpLmAdSJflxRqEf3rTnBmdSOLQFj74TYUj73k2TwCHrdinMd9CK_ufH-kHcqxVuAvqAhuRkSskmQj_vTzXPTvxmCDhA42j1aZ0-dI2kicGzxjnpkgc14xqCZ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2182de948.mp4?token=OgWMKOzngB6xiXkNM1in64ZqMXNryMXtVRsOsZdjVp2iHmook2f9U5NrA2_cvyCsMgxitnw1EGwaTaR3-LOyJQCIwgq5cW7w74eKRP-uidshQFedTYg69-C5jHvCXJ3r93nZt8muiEAFtLvZInFr-PtasuQlhigODoETDsi1uDGItxASAr8eJqryfkRV9ByVsIolabI5tNelH7jOkfPv4vTnDz-XXpLmAdSJflxRqEf3rTnBmdSOLQFj74TYUj73k2TwCHrdinMd9CK_ufH-kHcqxVuAvqAhuRkSskmQj_vTzXPTvxmCDhA42j1aZ0-dI2kicGzxjnpkgc14xqCZ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4965" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
سپاه یک کشتی رو در اطراف امارات (فجیره) توقیف کرده و در حال انتقال اون به سمت سواحل ایرانه.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/4964" target="_blank">📅 11:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=UuXSBWD-XbsxSDPPC3ADnE5Be6rBxm57w5z16dwD8dXGFOzpWMlPMHEHA1L4s06WeraiXFfZ7VcxNFdgnAtWkhfl2W0xUTZjEbrX7AXydXWZoryoTGpI7hmPn3DjdcLVh4INI4Vk6gQi69MtVns-Vs7PL8wzlNqgD5piNJcx_qpx72qYundyX93fnaw4VjnQ_iG3HmfpdQMqG37eXBWPAZt-7uFcPZHvkmpi71qunFNiuaVN2UUp04zQL9T78v36RJZoNoPfq89b-GHBWtW34HT2hUgZUHKrk-7Oo_vZcnlB59qP8fcFO1KxDh2mY6X-69iTmm5OKUSa4CWh6oR3QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=UuXSBWD-XbsxSDPPC3ADnE5Be6rBxm57w5z16dwD8dXGFOzpWMlPMHEHA1L4s06WeraiXFfZ7VcxNFdgnAtWkhfl2W0xUTZjEbrX7AXydXWZoryoTGpI7hmPn3DjdcLVh4INI4Vk6gQi69MtVns-Vs7PL8wzlNqgD5piNJcx_qpx72qYundyX93fnaw4VjnQ_iG3HmfpdQMqG37eXBWPAZt-7uFcPZHvkmpi71qunFNiuaVN2UUp04zQL9T78v36RJZoNoPfq89b-GHBWtW34HT2hUgZUHKrk-7Oo_vZcnlB59qP8fcFO1KxDh2mY6X-69iTmm5OKUSa4CWh6oR3QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب اگه نهادهای اطلاعاتی آمریکا متوجه شدند که جمهوری اسلامی به ۳۰ سایت موشکی از ۳۳ سایت موشکی در کرانه‌های تنگه هرمز دسترسی پیدا کرده،
[دسترسی پیدا کرده، یعنی در حملات آمریکا دهانه ورودی این سایت‌ها مسدود شده بود و دوباره دسترسی پیدا کرده]
نمیشه سریع اینطور نتیجه گرفت که : پس اگه جنگ از سر گرفته بشه جمهوری اسلامی قدرتمنده و…. چون دسترسی پیدا کرده.
این گزارش یک بعد دیگه هم داره
:
اونهم اینکه نهادهای اطلاعاتی آمریکا روی این۳۳ سایت موشکی اشراف اطلاعاتی کاملی دارند!
می‌دونند دقیقا کجا هستند،
موقعیت جغرافیای اونها رو دارند، و این گزارش یعنی وضعیت اونها رو مرتب رصد می‌کنن!
و خب اگه حمله‌ای بشه، می‌تونن در همون ده دقیقه اول شروع جنگ،
اول دوباره دهانه اینها رو ببندن!
اگه قبل از جنگ ۴۰ روزه نمی‌دونستن
موقعیت این سایت‌ها رو،
و در پی حملات موشکی جمهوری اسلامی پی بردند به موقعیت این سایت‌های موشکی ، الان همه رو زیر نظر دارند و رصد می‌کنند
و شناسایی شدن!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/4963" target="_blank">📅 10:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فهرستی از رهبران کسب‌وکار که به همراه رئیس‌جمهور ترامپ در سفر به چین شرکت  کرده‌اند:
1. ایلان ماسک، مدیرعامل تسلا و اسپیس‌ایکس
2. تیم کوک، مدیرعامل اپل
3. لری فینک، مدیرعامل بلک‌راک
4. استیفن شوارتزمان، مدیرعامل بلک‌استون
5. دیوید سولومون، مدیرعامل گلدمن ساکس
6. جین فریزر، مدیرعامل سیتی‌گروپ
7. کلی اورتبرگ، مدیرعامل بوئینگ
8. مایکل میباخ، مدیرعامل مسترکارت
9. رایان مک‌ایرنری، مدیرعامل ویزا
10. لری کالپ، مدیرعامل جنرال الکتریک
11. سانجای مهروترا، مدیرعامل میکرون
12. کریستیانو آمن، مدیرعامل کوالکام
13. برایان سایکز، مدیرعامل کارگیل
14. دینا پاول مک‌کورمیک، مدیر اجرایی متا
15. جیکوب تیسن، مدیرعامل ایلومینا
16. جیم اندرسون، مدیرعامل کوهرنت</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/4962" target="_blank">📅 10:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=czJUjNnGqYcsRC5McVxuORp7x621MKD7H1WsTmPQO_mFI4w1wtCQjyN3Cq9SI1BggANA8ITLxo1ADnoLGB9B-Gp0DhP2WSgEPeWAJMJLdtUTBu2UxOuLfzf-8_zjVov0TIzkO1l-UEFDzCPNSNT3r8V30iiGsrg_thX2I-QceeaYqYevNbSSvZfFqg5ialuJXt-s-dD7NWd4NjLAaL5OoKiBAfz63IqXBYd0aunmjDqTHCq3LnFm5FMsF8KRAaVXi92DYKuCX2zM2TTa0neap_4n8QMM9kKoBk9yjUNmw3dUcYbLB1UeVHKeqUYjgIh-63FrRd5guIF0Yl8vWoq9Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=czJUjNnGqYcsRC5McVxuORp7x621MKD7H1WsTmPQO_mFI4w1wtCQjyN3Cq9SI1BggANA8ITLxo1ADnoLGB9B-Gp0DhP2WSgEPeWAJMJLdtUTBu2UxOuLfzf-8_zjVov0TIzkO1l-UEFDzCPNSNT3r8V30iiGsrg_thX2I-QceeaYqYevNbSSvZfFqg5ialuJXt-s-dD7NWd4NjLAaL5OoKiBAfz63IqXBYd0aunmjDqTHCq3LnFm5FMsF8KRAaVXi92DYKuCX2zM2TTa0neap_4n8QMM9kKoBk9yjUNmw3dUcYbLB1UeVHKeqUYjgIh-63FrRd5guIF0Yl8vWoq9Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور چین در دیدار با ترامپ :
چین و آمریکا از همکاری سود می‌بینند و از تقابل زیان.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4961" target="_blank">📅 10:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kdb__o5Nzqy17ePEBobrfJyF8qqCh4P1_YCT8AZuxIvCGS7CByn2fefJ5d08Fs62JhCgJY8LyEYpL95y1mHCu5bW7yt3awWF8wGnKDgK1NExOKYNe8sP-oo8YpZo0drXtnsweX6XDmQRNIpolqmPFxZEoCbHSzmIZnvcDQ980TclLGB275VbXYFM4U85vjNUE5Ux99mkv6LF_LMXuFGI1LP-HgF9b69bftudK2YMWxXfSzgoeNslY0tGvMW5OjSnIP36linMQdVbVyejJ6uDO94O645YkrmI49poZ9yx4BFxkfFo77hj2vWDPiw-QpEYUMWdMHJ6YGmN5std-38X7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات در حال ایجاد فنس‌های محافظتی برای دفع حملات پهپادی است.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4960" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">جمهوری اسلامی : ۴ مامور دستگیر شده در کویت در چهارچوب ماموریت گشت‌زنی دریایی بودند که به خاطر اختلال در سامانه ناوبری وارد آب‌های کویت شدند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4959" target="_blank">📅 20:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
ناکامی «هفت باره» دمکرات‌های سنای آمریکا در طرح محدود کردن اختیارات جنگی ترامپ در جنگ علیه جمهوری اسلامی.
دمکرات‌های سنای آمریکا هفت بار طرح محدود کردن اختیارات رئیس جمهور در  جنگ علیه ایران را به رای گذاشتند و هر ۷ بار شکست خوردند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4958" target="_blank">📅 20:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
در یک اقدام بی‌سابقه دولت لبنان با طرح شکایتی در سازمان ملل، جمهوری اسلامی را مقصر تحمیل جنگ‌های ویرانگر به لبنان معرفی کرد.
لبنان در این نامه نهادهای جمهوری اسلامی، از جمله سپاه پاسداران را مسئول درگیر شدن این کشور در جنگ، برخلاف خواست دولت معرفی کرد.
‏این شکایت می‌گوید که این درگیری منجر به کشته و زخمی شدن هزاران شهروند لبنانی، آوارگی بیش از یک میلیون نفر، ویرانی گسترده در روستاها و شهرها، و اشغال بخش‌هایی از خاک لبنان توسط اسرائیل شده است.
لبنان در این نامه گفته با اینکه سفیر جمهوری اسلامی را اخراج کرده، اما او خاک لبنان را ترک نمی‌کند!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/4957" target="_blank">📅 20:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4956">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LojCq-Jr-rbM2UG4JpUv1YBlOeC5tnJLudVIXajXk3g6hN-W2QvECSxzdQVP9C9bN0RwQAjWHR61BlMi4p8j1jZ7MoUFzcR2J3AxBAKpViEnN31uNxo2Xz9xiHi-P9rJXvDL4h-dlcSG9iV0AmlImO1GdnZXp0GJyUw_OMh33h3g8qR56B2ypeL58IdIt37e2SXm2-153lsdQACi1T5SYWYLjrNiuo-xNmhF7AqEFfOqV0bLJV4ksO9CSXFxcJvLK1vA2_IfEBgov6-Z0HxPPxTLx1VWlREjvadaB--HaxdY6POiUo_ew4tsjkthGl5jlZ6rrauURI8ei47G9RVRhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی از رسانه‌های فرانسوی دست به انتشار گزارشی به نقل از «فلورین تاردیف» خبرنگار «پاری‌مچ» زده‌اند که حکایت از روابط پنهانی امانوئل ماکرون و گلشیفته فراهانی دارد.
این خبرنگار فرانسوی در گزارش خود نوشته که سیلی که زن ماکرون به او در کنار در خروجی هواپیما زد، به خاطر همین رابطه بوده.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/4956" target="_blank">📅 14:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4955">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تداوم انتشار اخبار مشارکت نظامی امارات و عربستان در جنگ ۴۰ روزه توسط رسانه‌های غربی :
وال استریت ژورنال : رئیس موساد در طی جنگ ۴۰ روزه حداقل دو بار از امارات دیدار کرد.
‏گاردین: ‏اختلافات داخلی میان کشورهای حاشیهٔ خلیج فارس، به‌ویژه بین عربستان سعودی و امارات، در محافل خصوصی معطوف به این مسئله بوده است که آیا خشم کشورهای عربی از حملات ایران باید تا حد تلافی‌های نظامی ادامه یابد، یا این اقدام ممکن است سطحی گسترده از تنش غیرقابل کنترل را ایجاد کند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4955" target="_blank">📅 14:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4954">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
‏«کنگره ملی کردستان»، نهاد فراگیر تشکل‌های کُرد، با انتشار بیانیه‌ای صحبت‌های دونالد ترامپ درباره ارائه سلاح به گروه‌های کُرد برای مقابله با جمهوری اسلامی را رد کرد و هشدار داد چنین اظهاراتی خطر ایجاد یک کارزار خصمانه هماهنگ علیه مردم کُرد را به همراه دارد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4954" target="_blank">📅 14:17 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
