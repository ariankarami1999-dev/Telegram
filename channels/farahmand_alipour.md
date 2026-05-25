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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 10:35:22</div>
<hr>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">صدا و سیما:  آمریکا با ۱۰ شرط جمهوری اسلامی موافقت کرده   ‏۱. آمریکا متعهد به عدم تجاوز به ایران شده  ‏۲. استمرار کنترل ایران بر تنگه هرمز ‏۳.پذیرش غنی سازی ‏۴.رفع همه تحریم های اولیه  ‏۵.رفع همه تحریم های ثانویه ‏۶.خاتمه تمامی قطعنامه های شورای امنیت  ‏۷.خاتمه…</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farahmand_alipour/5141" target="_blank">📅 09:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5140" target="_blank">📅 08:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">برخلاف خبرهایی که یکسره از احتمال توافق می‌گویند، فاصله خواست‌های دو‌ طرف هنوز آنچنان زیاد است که بشود گفت :
توافق بعید است!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5139" target="_blank">📅 01:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5138" target="_blank">📅 00:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
اکسیوس : ترامپ روز شنبه در یک تماس کنفرانسی به رهبران کشورهای عرب و مسلمان گفت که اگر توافقی برای پایان دادن به جنگ با ایران حاصل شود، او می‌خواهد کشورهای آنها به «توافق‌های ابراهیم» بپیوندند و با اسرائیل توافق صلح امضا کنند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5137" target="_blank">📅 22:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدماوند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2d1dzSTEe2rHc0fAg61_jayXXVJI7yvBBpEaqzi1RB47-wycMaZVBinhPaNr1lJkne5QBkmTSgqyBkDY5sgKNCUu3Telglo2ZDzxo56uQR6G8YCn_yG6nvCHCqH0Hbw9KRfTT0e1DVdbhYga1Nwfz6P4mDB9EnjAGhwBhZu0cJvwR2gjTHMGaofWJM1pImQkn8ZJFVRE6b5bzTbMa4zFUhFqYbxa-INj4-ZJDox7J2-d0StX8LxtmX1RkG_uEYQ7wlgLjdM6NIoXZyo402g9lC61vtD7QBXZy_jni7OdvRH9FCeC8NA5JfLHmPDtZpN83YORjTCVnzWFZDH68NvlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
یک اعدام دیگر
مجتبی کیان، بامداد امروز و همزمان با اذان صبح، به دست جمهوری جنایتکار اسلامی اعدام شد!
جرم او را ارائه مختصات صنایع تولیدی به شبکه‌های ماهواره‌ای اعلام کرده‌اند؛ انگار که اسرائیل که اتاق خواب رهبران رژیم را می‌داند به اطلاعات دیگران نیاز ندارد...
خبرگزاری سپاه نوشته است: «وی در پیام‌هایی به شبکه وابسته به دشمن، اطلاعات محل شرکت مرتبط با صنایع دفاعی را ارسال و با قید نام نخست‌وزیر رژیم صهیونیستی در پیام ارسالی به عوامل این شبکه تأکید می‌کند که موضوع را «به بی‌بی آمار بده»!
T.me/irdamavand</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5136" target="_blank">📅 15:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">️
🚨
🚨
آکسیوس: یک مقام آمریکایی گفت که پیش‌نویس یادداشت تفاهم شامل تعهدات ایران برای هرگز نرفتن به‌سوی ساخت سلاح هسته‌ای، و همچنین مذاکره درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالا از کشور است.
☢️
به گفته دو منبع آگاه، ایران از طریق میانجی‌ها به‌صورت شفاهی به آمریکا درباره میزان امتیازاتی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، تعهداتی ارائه کرده است.
- ببینیم چی میشه. بعید می‌دونم جمهوری اسلامی اورانیوم غنی سازی شدهاش رو تحویل بده،
خبر هم میگه ج‌ا به یک میانجی (پاکستان / قطر) شفاهی گفته!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5135" target="_blank">📅 07:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5134" target="_blank">📅 00:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bibQA0SdPsLkMTfFiXy-Kz22QK0x5u2KtR-iA3fr5nCpCrtiOUHkAfnszh5R-yAVGWQk14rNB9YAbC-1ius26cP30lE_BVpzMWp9zyojL3Fdyt8bAtUWqaVfw6w05d7kJ8Fl3Nv0GVHZijLCeuAWCk6w2rY8vTYT-Sll99VE-xviYtY2VF7ITuLZfBbceREGRE8eCzkOQZRuayipMuB4WjRhIeZboieFItkCIGuZS3E69_8CLFXzEGfxfve65AzSNzyQrLw7VBu57Rs7QSVHrkk91Z8EjeXcBVCxOKUlZEC9MCZiLdnsBbVh1QM_sRRz3ILzCUJx9mkFAyrem3OewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با هوش مصنوعی طراحی کردم.
گاو : نماد فراوانی و ثروت سرزمین ایران و منطقه.
تن زنانه و نیمه عریان: نماد پاکی، نماد لطافت و ظرافت ، در نقطه تقابل با خشونت و توحش و درندگی
بقیه هم‌ که معرف حضورتونه، آشنای دیرینه.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5133" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ به اکسیوس  گفت که درباره توافق با ایران یا بمباران، «کاملاً پنجاه‌پنجاه» است. ترامپ گفت امروز با مشاوران ارشدش دیدار خواهد کرد تا آخرین پیش‌نویس توافق را بررسی کنند و ممکن است تا فردا تصمیم نهایی را بگیرد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5132" target="_blank">📅 20:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
آکسیوس : ترامپ ساعت هشت شب امشب ،  در یک تماس کنفرانسی  با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5131" target="_blank">📅 20:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
آکسیوس :
ترامپ ساعت هشت شب امشب ،
در یک تماس کنفرانسی
با رهبران عرب شرکت خواهد کرد تا درباره پیش‌نویس توافق با ایران گفت‌وگو کند و نظر آن‌ها را بشنود.
🔺
نظر شخصی :  توافقی در کار نیست!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5130" target="_blank">📅 20:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5127" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5126" target="_blank">📅 18:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHbJTiOt-XO3MhoK3cIFdpp0upe1Wd7RCcrSK5IPs38z2MCPGeM9fx_YJYI9TxDj443h5rJC24By5kZ10ZBDHUy-zUXfFEvAaQDRh7Vz5ZyEUGTd7znjxF3buv5of9FXustb4ZUkricJnVlBUPAvlbwJFJqx6FWvKX-H6D5ovRRMwv1DUFW_BPPTafF4rrMjt5BsYteytq_byMYIN1nxO9afLvqQIIakhrf1IWJYhurCvy8YJKf0VRh5ULK1yqNsEoqseGEdkbk19J4ZzyWRihQKTYmyV4jghsf3ILcBPnXYrtwB9t419fouPzUugghAx40jtjDVddav5YBe5ALoig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که پرچم آمریکا را روی نقشه ایران به تصویر کشیده و تیتر زده «ایالات متحده خاورمیانه؟»</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5125" target="_blank">📅 18:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:  شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته. شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.  جمهوری اسلامی باید دست از غنی‌سازی بردارند.…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5124" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5123">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مارکو روبیو در خصوص مذاکرات با جمهوری اسلامی:
شاید تا عصر امروز خبرهایی باشه، شاید هم نه. مطمئن نیستم ولی امیدوارم. پیشرفت‌هایی صورت گرفته.
شاید عصر امروز، شاید فردا، شاید این یکی دو روزه، چیزی برای گفتن داشته باشیم.
جمهوری اسلامی باید دست از غنی‌سازی بردارند. اورانیوم غنی‌سازی شده را تسلیم کنند، تنگه هرمز باید باز شود.  ترجیح رئیس جمهور ترامپ دیپلماسی و رسیدن به یک‌ توافق است.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5123" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5122">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahBFxUTl3kuJpxmhaKn00UKgo8ve5fKF-uAnKPU2y44bxdWYYdv7UdXDlEiVicH5atOZNJcLoIOawJeaIak8N97INSedo8RdtD09DyNs9ACICfhMkdWjILXnVUIeTOVDZ8UsADOEYBaGzS589nDGWN2HCPJ_koLD-JQg0bfS8QuBovGCJw8tEG0bp8vBdha4t-M1SiCh8oxPpeIARaSJnFLT9nKQj2o2ZAgxCXj4IfiWaliCXADzNpBDuLhXN3eLWBFafBuzsx3MP7Ds9NORZFY1kVnnbsJKH-wjJBvEagYKp71IqIoXLTUdHDz7nC2yjBnneQFXLCFFCekw7wdZ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر ایران باید هزینه بده برای این گر‌وه‌ها
و برای این جنگ‌های بی‌پایان جمهوری اسلامی با آمریکا و اسرائیل.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5122" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!    مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید: ۹ سال زندان   حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5121" target="_blank">📅 13:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UErcqPbVeSBQyib25ma_mEgpuU15v39VJk7lyQ43x4zpUq6AlQD58gCVmT8htUZkLrJ4a6CwnoYy2tZc9eGe5C-A66zhTo8AaVWLOQjnJYPisTzkCfHeyhw-jOToU3ZDLBTB3NJykzcpsrkf4fJBrr82UjMKQcKBMEkBFgXjUGTGwjYwxhd4kSb-rVLtOtW7-H4AOmlSgJ-M9WgInP1TO2xOK_JN3iwvaySB6EwOeuMJvuMlpHduO-LFfQa5mILF05rfEB2Ih5YCgYKUTS5qhDkt_8E53aAj5E4_5eWUUVcFKjHMECz_5lOREK708hsGjLabLqKvnEVUsW1AGmqmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خاطر ارسال ویدئو ۲۷ سال زندان!
مجازات پدر «رومینا اشرفی» ۱۴ ساله، که با داس سر دخترش رو برید:
۹ سال زندان
حکومت اسلامی! عدالت علوی!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5120" target="_blank">📅 13:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5119" target="_blank">📅 08:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حریم هوایی ایران در مناطق غربی بسته شد.
پروازها فقط در طول روز</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5118" target="_blank">📅 01:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
براساس گزارش آکسیوس، ترامپ به‌طور جدی در حال بررسی آغاز حملات جدید علیه جمهوری اسلامی است؛ مگر اینکه در آخرین لحظات، گشایشی در مذاکرات حاصل شود.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5117" target="_blank">📅 00:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وال‌استریت ژورنال:
واسطه‌ها در تلاش هستند تا یک توافق موقت بین ایران و ایالات متحده به دست آورند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاش برای کاهش اختلافات بر سر برنامه هسته‌ای ایران، رفع تحریم‌ها و امنیت منطقه‌ای هستند.
هدف، یک توافق کامل نیست، بلکه یک چارچوب موقت است که آتش‌بس را تمدید کرده و امکان ادامه مذاکرات گسترده‌تر را فراهم کند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5116" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rpo4LyKg1SILx0B4zNe-COuILyH-zUnYGxgfXGhmAe0MXhfdY5PhOR2cqoDfU1Dg4iAPYqbjMBAkU4g1s218Y1fRIaStvWZtOTmy0mANr75U1otrDM-C8nATpS7xQkxj48QsZFcsMs313zWxRDRf_yBeCI356t0feGh_K5IYc8tf4iPxy7wRwp7sjMDg9aVkkCxrpGXvGyJWLEKwqtHrIi02tm1ndCJStlUPSGdVGGpjUN5-G2goXrLrcj36viqUWtwURogpYiqPfZDA2Or-oYla1BpLY7N8pY1g-p8NLaricZWbZ6lSfjWm9-fIriPwq2C-d5nzZ4hXWLF0EgY6Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری وابسته به سپاه این مدلی تیتر میزنه
ولی در واقع «گابارد» از مخالفان معروف جنگ علیه جمهوری اسلامی بود که الان کنار گذاشته شد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5115" target="_blank">📅 22:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE0gImsiJ1PFObx5CH25PsOdCwqWw1Iv2LTXzqC8YlUz7dqBq57bR7MXp8_i8DULVF0KafQPfS2eWqkYwOCEKvCBe-exvmEnaJv9y1tc_-cALvK-b1RidghuZfAzRCrcnupjqspDDBRzzAoX6MrJjyORw4mtM9ZjW0phn5pWQI0IKKqCVcCkX9-Uou-nZtuSYmhPSFhFyMt7OIaYHSFrHZDyGatFE4fYPSX0vP6lp4dmgLp4Bzi55YYcTf0CbiG3wFT-4u-V7xdpwqp4IGk02BnbunJmW9ds3QA8UU_n5d3HuW1GEzu2YVFiTZuy75bB1EWofdPK03k1KfsR6h8uxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به بیانی دیگه : توقف جنگ در لبنان، پیش شرط اساسی جمهوری اسلامی برای مذاکره با آمریکاست!
خب چرا جنگ در لبنان شروع شد؟
چون گروه تروریستی حزب‌الله حمله کرد به اسرائیل.
مهم‌ترین دغدغه‌های جمهوری اسلامی نظام خودشه و حفظ نیابتی‌هاش. نه ایران و منافع ایران.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5114" target="_blank">📅 22:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9bol9s_eg1qAgy1aYVJN6gWna7e_9JbBpDKWw5NBHfu7Ue-mZacZcSFa0NkLXWtAYRd-ntVAPXbqk2UO4q6S1F58lkPLimL_jBKS3MDcWS4KpmBkPoXUXUoFI6ensJXFZjCeEgUCnY5vbh3_uwF765-mATXUrvlfZHn4YbXBCQKas4oELaNZ0qdRt3iip3p3V1_bNd161xIYs7GDuckVF-AWQq2JUFb-zrkusLiKgot3G_jWtQ2t8a7qFMde2Ruk84-SlHgaat-8k9VV14bHWWOLQLga9vxrDUUnLOEV7SyKVZXx0YaTOysW-jKv5hD34N2QIOHnaqVURrDRrXxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSbgNMBlNutXfxo_uyyd1hIGLZ0G8TnsC70usb4bSxfazcrCc0A_ylKjpbhEMe4mT46jtsdG04RtP79mqOpzKbe6ICW1AwYliHxd3QpDBNxggYOcMPZ69mIxCl8n92HLGF8Xna6UXdj7rU3JU5Vm0JAPbBhHkpp45VwZq2rXU4BaL9U3w_SLpatxbWLnANU8VQDNZSMuB4-mi4WYeRRuYSY53KDzCVlzQBe8hEaVRC9NUINMm0VFKroDHURdSpZK1V8cu7VmOBQXeyGTWSwIr7L7GqJaPt02YUSoCCcD-haqjNeBENFVh0cqAKUttgakwlRGoXpjwxhX5j2Y8DfjYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4lpur_H23fLEykRi8e9Ns5_2Kiv_TvPmoXhozq_KUMFcWg3kCVtbOZuw-R7lhC9oPHwnn_F-i47RDdtMAqcMCl5ythjQz5b1qA2xQTKvrXnPlM84IQ_RPSB8r9CNn0zeYUfGmrthxUrIUg44rnhpLkzWHQuiH8n2NQWvIVKf_O5zQbjufvm3OCW3Qa2fFoa4JFuQL71C8hXsfk9ndmMduRWKqs0IiJpSUFketZKo0FgmylSmxGxX0Qo2zTb9x5JWFMe0FshbSlWnR5DYEZ9q1jL-l-QpHIotLF4vAChpCVONIQLNEVJcm8nhcA8GzkKn9TCQfT3940RNsq4jg43PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mF80k_pOgKR2vxxVV6kuUvp83RIq7-ZaM0hWj4vu-OYlUgARw43HBlILWB-71wH9_6lHsTSpResxQYS8GwB0JzgmOoOkv1Drz6C7P9UtS6Nlm7uZ0r5mTJb7YOeyhqT5yvstdG3cXxhBMIHd0rZ79b_tMxID00BiqU_mykGh03rOXfqhE_RGDyQCW5kLljFoja4fJFCoOJg70yxOaPhJdZ0kqusxvTTqu19BsGAKYKpvQsTVyoUncCw8HbuHNntdWd_JvETfha_1EpiWfb5J1m7kmYOQ-r0nOGFlrtEEmY_-RFg_AyLd5D48Qm22wfadcj73DTYKh9xT8QVuqQ1deQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQBneFTD_6GLz5oIms1vyLtBiknWyjLnrbMd1fx9H3JvOM08k6Bx8ZlxzNqrbRTaSZ-JMXE9amyinVM00El2IZPTO2_65nOxGayvUnB8JhXlZrv8DJFXXfyolGWoCZDMaww4BUtmzvy3FpNEecIBB0yT0jmwl-TSVY6YB2ytWFQFCho9v8jW3HBGfIIhiyFDv3sowKzV8HtvH2zlNjUDB95a-nvy9JBB0fWbzNwikzlERDHcMQA1p4yXzulEf-qHMN6gHbvVGoi_uY0VQaNFPLfrfA-6VWc0Ju1Jpa_RAIkuPUDX9CDbQtZKS7yYqWHb6FnxQ0c4u-8lTUtwoQARRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=oNIobAxC4q11FCqNYg0fKd9Cy4yxJwCejTQF5Z4FRtAN82Zn10g4ypoiDJwwelIrWz-m7emxL_v1NAxcxDgnDt22SdaA4TqwAoOyflCvRO5pNek1_rlhbJiMnPKMP50f_Hhj0ky7pSO2JgivByT3pwwaFsDrJ_y9PLnVjLbcCSmrWRmH4KMdxg-cV-Gxf_LwLvltd7f5gDBPMnfrUekfTfMvkrvCmuORojL17VF99hHI5PgeYuPMvkpLs8NeuDZ-yKZHU_gAdRLgo5vLlibIHClbVwvITlWT7NJ1jvMYAmXexBN9ii8FEcqYubnF0ZhmtRzE98NYmuW1Uk4pYFGcbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=oNIobAxC4q11FCqNYg0fKd9Cy4yxJwCejTQF5Z4FRtAN82Zn10g4ypoiDJwwelIrWz-m7emxL_v1NAxcxDgnDt22SdaA4TqwAoOyflCvRO5pNek1_rlhbJiMnPKMP50f_Hhj0ky7pSO2JgivByT3pwwaFsDrJ_y9PLnVjLbcCSmrWRmH4KMdxg-cV-Gxf_LwLvltd7f5gDBPMnfrUekfTfMvkrvCmuORojL17VF99hHI5PgeYuPMvkpLs8NeuDZ-yKZHU_gAdRLgo5vLlibIHClbVwvITlWT7NJ1jvMYAmXexBN9ii8FEcqYubnF0ZhmtRzE98NYmuW1Uk4pYFGcbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=pD2a1va-goHr9flPfv_HKoinytiEsrnQ5HtmAfElpvdB8ZiP4jnYkkwFJQmkWZWaxbTGFRZp3lLGmCNg3qrFrF79MvjjAkH3DBiZiXC2wtc09QUxUbvIgjOIWzVNmHHImfMoZdyDbm6Ul5OgBQD7ihKGCbP2V7fRxMZ1eGI1PzE4eYhfL521pWIex5CqTGAY6ftLfT8N7spenPuTh4i2ws3hIvi82JFfFB-dl8HPm-5flBjBhZ9HpaRbuekbzfVgeL-cxMm1VYCJ1zQsChrYS0pBOJkvAkzwB-oyAx9yDRUejZHvq-5XUaiOHQlshXocwoSksqlLc7H3PlekaGFVjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=pD2a1va-goHr9flPfv_HKoinytiEsrnQ5HtmAfElpvdB8ZiP4jnYkkwFJQmkWZWaxbTGFRZp3lLGmCNg3qrFrF79MvjjAkH3DBiZiXC2wtc09QUxUbvIgjOIWzVNmHHImfMoZdyDbm6Ul5OgBQD7ihKGCbP2V7fRxMZ1eGI1PzE4eYhfL521pWIex5CqTGAY6ftLfT8N7spenPuTh4i2ws3hIvi82JFfFB-dl8HPm-5flBjBhZ9HpaRbuekbzfVgeL-cxMm1VYCJ1zQsChrYS0pBOJkvAkzwB-oyAx9yDRUejZHvq-5XUaiOHQlshXocwoSksqlLc7H3PlekaGFVjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9Fy8ig8Afn3_HUvJBUNYCCZl5cV1bCqJpaMr1NJD-b19ufDds6WTjaQ0HbcWtfbZQb3fnXsL2P5wc6B_8SIt_BkPcYThXJkE-9OVQyg1TESJfrM4w53gjKdP4WbMb0NU_2LPt0FVaqPwxFuDcw5uO6BsDUjZSBDf9SwQJKXS3RvQ1mW-UcCMSGfCYeVCpHPNdiRTy8WWG9wr26sAEkiuHmFJInxz2zXKG0jgHPoDfs25xo4EhbqSTY35-CZVs51R-pNrlIhyJQ6DGEKRNIewgIZ0dA-WnG6liBDHZ7deW5HENJOfNhkuJcfUAGJkWPW3V8br11CzjRm0XZ9SmDXNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzumU2cLAnO8qNBZp2pURsEpVe47HFeoDlCcxbbUG4OfG7Tcb7wCwbnyvHoFv7mrAaYcApYZcup3sP5J-gldO7ETa41FK6Y6Q9i2dP2rDSoTJEixiHWBUn4Ru_8iAlyKE9_1JSxZ3CgF_1X0gb0UBTuH2GpQ40DVnD7O2Ft6wULxPZjLgACk4e_HrBy89y1GqrblD57TeCtJ0AnNzHDo_4bWXu3LEJ0QlFUBTdjl6DjQl1-0w4ChJiBrqivCKdsZ3rYEb4HCHIIc25JawP9bg594Ke4AG5QOs8b1AIfKrhqmyQ4McFRtU34QQ1dqTz2vgsbNLq7VCtgF33rV6cFTsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFmU1yT7BF3hNuMn2_0u_3vc5hSN_k5L00dScDmobyA1YxPpkM2nsbUp7HtWae9cTnGdsWmIbcVNXXyhqSW9a9k4W2GtBAt7a3FLnVOVPAfgy3HqDck-7ZlwS6WoT5gN4JRG5dIUeMsudYfyqbexiIo8jJrVx4jpAkcBBD1aHbiMAwDNGcgfiKvSEPIUvyyXeRLuckbO3NORW7MGozTxTp6X6Dg8FBBLeHmGlVYBC69XIQ7FDNwF8Gg1lbip9NHbJi3BNqipB2LCUNIoI-tfj5svo-7J6udSTGNoka8-Qo0djRcs3XjMPVWneEVTwBzeTMff1wjtw8vqG04wz7idcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=aqSIkcLGp1TO3Zmm12LuOplQAktCwnzoHvReHl_atfq3j-xfWnpvAg-r1di9oX76PYhNRTKjh6KESL222O7392HLD0E7etcMa3K4Fk9guFg2L2gfvvQo_CbANzXeAtdJwVcrkcND6OM-2gbqhbU_apkWacxTM9Ox4KlTBU4Ne7XQ1Vwmg-AViK2hpXGKSto_7EgfAv6HcCDpJtels2sE_3xDHe4DV9QeT1LueMP0mUyEDVDHFDwsRaq6gjyfiO21X4uRzrKaUeIA0546TA0aBT_whqCuykVZX1P7yvJLhC5_Qdhlz8q5F9ed_W60r_A30DYbY7jxAsso49bYX40njA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=aqSIkcLGp1TO3Zmm12LuOplQAktCwnzoHvReHl_atfq3j-xfWnpvAg-r1di9oX76PYhNRTKjh6KESL222O7392HLD0E7etcMa3K4Fk9guFg2L2gfvvQo_CbANzXeAtdJwVcrkcND6OM-2gbqhbU_apkWacxTM9Ox4KlTBU4Ne7XQ1Vwmg-AViK2hpXGKSto_7EgfAv6HcCDpJtels2sE_3xDHe4DV9QeT1LueMP0mUyEDVDHFDwsRaq6gjyfiO21X4uRzrKaUeIA0546TA0aBT_whqCuykVZX1P7yvJLhC5_Qdhlz8q5F9ed_W60r_A30DYbY7jxAsso49bYX40njA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5KWRqkMNZl7pA3EVEgJ3Ah7iCwYzGm4_-cnodzWI3SO-2T4P5k__0Cst1wY19A3CfJxLilqKnpoMj4_1gauUTshbwhsGtOLNl1GS4kqARyyNFpHZ6oYuXcuy8L-T0P0ZbUyyN6ZZb33cPhNw-u07OJ9iAdx2Rv65Vj4ZiTnIXe4gtwd8UBkTh16A3KSz2F487M8gLGIms9LxyHq8RD6vwh6aOxLvYVuGRecvQZAFZcS4YkWD9ttHRRSxADkbaCTmPbmJEyPKV9Zm1kwKc2-1tlVj33JI8YtLmjXvEWtkl9XE75lyLJtuNh0s0vHcNvhmS28xvCEFd5KuojQdZ_hHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTYRLxm5EEqAbXCtWPhhIbKeksRZdMRScdtyeuJP5-djQSTM2PbZN31uPDC3Y1AF2CYVAXwObKHYuK0nsu_N0MM_2L1uYHTZCWDJ_V_RqpdNxGwFSmD7b9IyNR6e6QSvkbInUMh5dX90teowE_9y7uaQXyyZH55q9Ict8mx9r5ztHiW7OkFDanARkqxjES7XAre5HrdCEFNedBqH733thfv32pq-MqsN_YNY9CcUC-6jrsJyxnhu5tIdtz3BlEy0XEXzhG29OZm0nX2hKXTzuFQSI57Ttp4BpJDM6IAmLHTEkA6AdHTUNPYnofuBRJFu8hPUbTLYSO5p6dgudDAeEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEwzwTF82HuoXE-3Yh_cZU9CafPjNrJepIFHPFM0_l8pdk9vHPx1QTOitkqaTm2eYEYmNFFOBG7JIgUM8R0xmCjm_j0ohHQ9WyFWZZ2mO_KXlkwUAIplOPqhIkgS_ACv94WX490lo-Qr1nd0KY3cozZPifq7z7IZh5-yApAdfpP72UMjif08uSMwCfeHtZWKm7yhOd0JyQuKK2mNlIxelcILRm-2jVoETBnZ-meFSIx15o_u_CXbntTrg63r_Oq4G3nRB14hH8I1zviivckuzvwhjbUiFEvepCyOQIsZjaQM67NTBUhdXBEcCH-osix3e8fgUAeci2AfWdVL3n9pIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EftLD0_iNToathXbfp1-R4S1kCsKs_PnaxRanuWSHONwMM8ecSRIRrtPJana8CabMFagHSmjMbAj3yKbfiIJfzK8RpaBp0IWn4edsWwVdoaAod7XyWIq6XGcirRV7BNRH_o6gNPjbnBlE-JMoiciqIkrPBBZBwSuu7cgMzM8ZulHdYfylU6MsiE0x3paw6iPGuFkTCnLdaD0WuKzt93STQ2LW9Sn6zsROp-EDS0GuCT5g4hPPwwfjWpFtgKCsePHjtTisaGpxZ1QW2pxjWZko8E_pyL_0lTpLsJcGJctiBE0GMWhsCykd0wphxdHFCKXvTopec1hfT1ep5MMcZQMDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpBaWSU11nH-XhqVg-VhB_icNwdl1_rYojO8g69gyfsmX0QtKz6bv_8zNvdensEZZqxvbbVE85mU181u2IYNFZ61haMpTTRPmmbUFkqZUOqlbAtczyLznitZr88quVr1Skjw6DtcYNB-1MU85EJmO9onhp3miEHPmCEg25b3mNsYFs0L60YYcKu339yGuDy5845Xmk_o0b9ZPA8nynssIwvl-zTJql1cy3XOPpYYo0YPh9G-fdXmcK457iXcsAhsZTsARag771rGjEHtdDcBBBdc33H8_zZhmQcEuQfwoxHH6j3Gx-YpSsirSKoI2449NDb_KlMR7_1zEQg2WYFI0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFSwZDib_drDiwSP2-xzOjqS0Nrr7fu-lwegJKUDyB83mf0N8iaj6O7asgJorXk8X1J3MAdXBL9vZ2lAoDwzUPtiZMnVKUEMBO-va6UX_HyQtn-stAyW9JgehRzrjB34I3vY3w5eEclUthPsx21VkpWdiQB_x0XoIJ9e8iTmSP-Z0InPp9TVa0PZLGvUDRx857A4ZXzUrrjNh9vMrQr5U0ruEoANThpik2TgqTucsmpNI-iNUZNZ9cWeIJmjUbenh--ojbSxBR647ZYerJZRw-IaQsl9Sdr5zL4il5mG902G8t8Utjbxtuhzt6wEyqfH0vepLsNFkSqKA1_JEXE8pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NoQShDODmQxED2WeJ3y7qnKafbKzcfqzpgJ1HJr2Ls5sB4R1xB6noiGU9AVv0HEzw1jdpcMSMWG-lADBaJqLUeLxHk3hG0eiGNS9dmVE7iumwA6UahK-fV4CO8mwPGiTpRQGhqHm4Lua1wGqW1eQzEavjBk-vp9L6w-VHS5T1UNmuJ3zeYZ_u4mJqJ0MSCB5idmYrjr6EwGL89bt0iLSek9L1-rE4CISkVVwBnsDBfM8kZHrSKt7Xj9amXau-vbhpka2TG2a0D8Q3GfUZdoSH7xu3xRdTNpqvV6KrF7sxuPFgQ9_4ByB0a-By28TyqDjNx_Wh_Xyg_e5Mh8OudlG5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsbEiDIG49Ea6kWwtNd31WCX1TNwJxzR2BG4BE5Fk_Ezqf3FCbsGTeO1kfOfBTzpgEJNoH_E49U6vq_Fg5SHrOXy5BQbMRx3K4ChpFkc4OpjFUylBou7a_w9CKTl6-yEUz_ngkYM1ffGvl6Nl1TczbpjLC2iaG5kUHEQwLxbCa4eKfzo8iMhyu1XynGHrp0DK3u1V-25o3-CIR5STwgNLvRmjC7tmH-ET2MKixB80riRgVROwCaJlS9SNXlQlrOwvfytGTEGqqfWngLHCgzuXh1vcW3T9MhMk8sMWqdBUdjkbLwwYEtBplJox2pVP_t9_kkGwvN61sp13DXY4Vg0Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXWecBK22-TgBD1p-uqYzyraCf8hDYJImrdszrU1wx_mapiHpBJUxPDlP5ZdqfPeVw38Shb_8scbg09ZhQMDMoEF_2FkqC0KDRMxRxSvc-xIcQ-RN9CbJGKBXF76VUd4NrV1-q86BLtjFFdoRxOiF_5TJ6REKZmuggmZHeUHAde6EG6v_atk9bBLejp9ciP_VwY--p5IqbsYLzHMzvcAlmUWLSMR7WIyHCs_2lG365KSWV7pLsJQS5mQTO-PguViKrVVBARwELJlAP15FQQgufCEEDcu5jciMTUmX_VLdhZwk4dQ8PU5s0pbE-tOzJy35yxctEgOWG5IE9gu-L3Nqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-vRqgWhB0-0YMDIstbN_Bi3LLGzELxSTL1QyCwM43vMNwS14OrIQFE5GaLjWoC6Acyxy2JqfcpJ0L8pbJXlYtSf-Ij0nY4EMBwaxZVQ2xcmLmxt74LIWNosM--w8m_x5Lo1HXU50g7Cuq4ei-1equeHUoOUGUURNIw6f-Fm7wZZFnQYwvQh3YY9zDRjANEJ44gzafVKusc0ItgZRC1rWVlAnDfqvxe66OffNNnfvRObqLk80fGevt48oPWe4ZcAHw88huRmUyt4nKwz69roZ47kiOB4ybkfNg-rFzUzbnnIf0zd10fpBAn0r4txxgrKnsnjxtOHblGGyzKG7Bt0qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoXy0ZmR7V3_xXptlCQE8cCVTgWhZNkzaUkLNb4fKaTH26ch0xmDbRLU24JkdC0PW_xywWg2MFjran0jcLZXyJE_7wRb23TGtq3xrTc3s_IEe2evjS_m80wN3xrZy3ihGc7mi9OkfXnkT2Ek-TPQpIxM4r6e6cXOsx_wzmZsDNz6ib9iKoA6n6iIFkXTBu-RkXtr_NovBcuUNTBpHgksPLntXRjDxXSOmqfULZRjmOVTvbwvZ6g87_xNgX66QYqQLhu5BJomsCIYWF8T36JW1_s-XH8JqrUFlKDGBK5ZVE7zDVx0tBT-aYBH-WZ8wUGk4E0SoGJ6NxLMRuwRh7mrxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=Qg9HEAYkCVoq15ZxNZRUvyatG4_jb5OdbvDB0hkLAC7M3ArPs4dPkhsoRj4-DMJM52tJYG6P5tpivy0oxOmYGxck3TiFNZ-Fcu27klnYjtipS8IOvb9-7AY24Lmoet8x-Cpc0krFSoWVgSc8ivtGT3Cd0yf1a2ppYklnlrVmhADWXkV-yfTSYDDEuDk9dNQlRwfwNOoHdf7Pi0Dh6plPd3WZ1c-H2XMDWk1cgXVR4G6zCFuNDUfDHnUdm7Gkz3eZsVLKVADUjaG0XDnpa06vuaZZ4OZIo-1aFVS9bDJtK67mnWhG-FmJcqN0DAHtiZbIPOGrTGfDJk8w6lYuMHs7Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=Qg9HEAYkCVoq15ZxNZRUvyatG4_jb5OdbvDB0hkLAC7M3ArPs4dPkhsoRj4-DMJM52tJYG6P5tpivy0oxOmYGxck3TiFNZ-Fcu27klnYjtipS8IOvb9-7AY24Lmoet8x-Cpc0krFSoWVgSc8ivtGT3Cd0yf1a2ppYklnlrVmhADWXkV-yfTSYDDEuDk9dNQlRwfwNOoHdf7Pi0Dh6plPd3WZ1c-H2XMDWk1cgXVR4G6zCFuNDUfDHnUdm7Gkz3eZsVLKVADUjaG0XDnpa06vuaZZ4OZIo-1aFVS9bDJtK67mnWhG-FmJcqN0DAHtiZbIPOGrTGfDJk8w6lYuMHs7Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاصل ۱۴۰۰ سال علوم اسلامی!
علی خامنه‌ای هم به صراحت در یک سخنرانی «اجنه» را متهم کرد که با سرویس‌های اطلاعاتی غربی علیه جمهوری اسلامی همکاری می‌کنند.
در زمان محاصره اصفهان
توسط ارتش محمود افغان،
روحانیون بلند پایه شیعه، به شاه صفوی وعده دادند که به زودی ارتشی از اجنه
به یاری ارتش امام زمان (ارتش صفویه)
خواهد آمد و شورش افغان‌ها را دفع خواهند کرد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5082">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=YBn6G5KjhlTwRtLhBht5Yy5_U9HwIMvDqip1aILxfwAQmSHKkcPN-_Fp_jaNrWnD2CYgPJ4Qd5KqVG3bBmk0nr9qPShtb6u0e70A9_Wr5u3xW6R_bgKVa1CMkOypQYWHujyBs0bajmOqk0w2GJlMKPsVbnf6maBds2hfz7kYhO3Qd1aXN6EZeHWcvVDC6NEsM8ku-6LrNtcloCCdTnr5aOtXUsVBCZrbAwwysIGIbgEg2TEIGGnKX7OV2v1MzMuFvvLjbeVEhwbgfrn2OVaLypoDxdgLtx9isfvfelmsrBlPJMJOQlhXODygoN4P32MBefiCoFOKhD0yEq7b7PvaGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=YBn6G5KjhlTwRtLhBht5Yy5_U9HwIMvDqip1aILxfwAQmSHKkcPN-_Fp_jaNrWnD2CYgPJ4Qd5KqVG3bBmk0nr9qPShtb6u0e70A9_Wr5u3xW6R_bgKVa1CMkOypQYWHujyBs0bajmOqk0w2GJlMKPsVbnf6maBds2hfz7kYhO3Qd1aXN6EZeHWcvVDC6NEsM8ku-6LrNtcloCCdTnr5aOtXUsVBCZrbAwwysIGIbgEg2TEIGGnKX7OV2v1MzMuFvvLjbeVEhwbgfrn2OVaLypoDxdgLtx9isfvfelmsrBlPJMJOQlhXODygoN4P32MBefiCoFOKhD0yEq7b7PvaGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادآوری :
در پی انتشار رسمی خبر کشته شدن خامنه‌ای، در شهرهای ایران جشن گرفته شد
و ویدئوهای بسیار زیادی از این جشن
و تجمع‌ها منتشر شد.
و به قول این مداح
«صداش عالم رو پر کرد»!
حکومت از همون موقع اینترنت رو بست.
تا الان جمهوری اسلامی بیش از ۴ میلیارد دلار به خاطر قطع اینترنت زیان کرده!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5082" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5081">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=B12MBVuGv4COjFpH1r2a2BnJV2kZOBqV5xZe5_vkepGHerDLi7z4OWWG7-wfyBkq4yefGKbYYhTJPEIkCG8MPHpAYHUun1DJfD0Ah42pRqKlVQuwMgf4TWDvIq-zMy3mNWM4x4Eba1QjzNXmVAxHsVmDUVvT-qrOF9MLuIELD5W12qkEo-lpM9DPGQfHlkaSb3qhMTbeWcYkDbmRdG53qiefIqMKXQkJmHqhnCRAYvsEmpVoxe8ralroCUWMSg8N6QaOj-ru1nYBrdzwrFQQdN5l3QY-_gUbDTBLgE2C7XNqZpJbB8h-b16z7iTfO1pxZS4b74tQfMLcjPY_T6Yg6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=B12MBVuGv4COjFpH1r2a2BnJV2kZOBqV5xZe5_vkepGHerDLi7z4OWWG7-wfyBkq4yefGKbYYhTJPEIkCG8MPHpAYHUun1DJfD0Ah42pRqKlVQuwMgf4TWDvIq-zMy3mNWM4x4Eba1QjzNXmVAxHsVmDUVvT-qrOF9MLuIELD5W12qkEo-lpM9DPGQfHlkaSb3qhMTbeWcYkDbmRdG53qiefIqMKXQkJmHqhnCRAYvsEmpVoxe8ralroCUWMSg8N6QaOj-ru1nYBrdzwrFQQdN5l3QY-_gUbDTBLgE2C7XNqZpJbB8h-b16z7iTfO1pxZS4b74tQfMLcjPY_T6Yg6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNzfxxz_tCGlXIuZQmILsJhU_yaubQwXHwSJGBPXj0KYSyXtOjsFQrJdEuEWDVFH51r1ekyVXSdxOaevYe3xxBm2ZrRxPwHGaEkSViVyscIDQqfywsCdNcYoROcedqikOOUqQGEk6ktdwHt9yuZ5PytTzhf5JzN6vnxvUFxjRYD6NLOVdjpYJgotIwy4D0FT3_a1zhSI3kgqZO44C2ow0pi77p_dzojZuwXdSdPJuO14T5hxwbLJ2L10eyvz-sR7lSBjaLXmVRrzN5ZMfC8TiD5JxgBoirllF0laLk0VmHFuWgWwSQOJHmsCf9MeZrr_kz4Qp2XyECH3DlPkBcWZ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=J8SQuKtr5aOoUdOY5RA4wRoKnFHJl9SLiM8HPpz-3PKOH1GIN4Knl3XcdXBlzK3oI-vT2gxAZyUudhI52V5lrLSJJheGK1imlYfjiA2iGZPYmmkrQsoyWr9_yn8xevLtIHA3Jigo7-b0NobZlDDMCkl6pA7CADHk1muFJPiRwFhnueVI7JFo3SKRVvGv84CxqqTtTjCOrbk5fUux4-GN3pVlF8EwuOontiWvvmHPxjIuLHAvuiNRkmlPkmtIGQiOo2BH-1VFdZERZBS4Svw8Zb-OiApR9xk-_q7ZAMZFxsIltF_5IE4JCmb4IIK_IXG8O-IrfzQWPEkkq9E6Q4utrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=J8SQuKtr5aOoUdOY5RA4wRoKnFHJl9SLiM8HPpz-3PKOH1GIN4Knl3XcdXBlzK3oI-vT2gxAZyUudhI52V5lrLSJJheGK1imlYfjiA2iGZPYmmkrQsoyWr9_yn8xevLtIHA3Jigo7-b0NobZlDDMCkl6pA7CADHk1muFJPiRwFhnueVI7JFo3SKRVvGv84CxqqTtTjCOrbk5fUux4-GN3pVlF8EwuOontiWvvmHPxjIuLHAvuiNRkmlPkmtIGQiOo2BH-1VFdZERZBS4Svw8Zb-OiApR9xk-_q7ZAMZFxsIltF_5IE4JCmb4IIK_IXG8O-IrfzQWPEkkq9E6Q4utrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=ArB8k1zSCyhq9w01jCA4lFxQiLBS900pTAurEUL9uqB3BRp9EjHjM9q4J012feHgpfes8Zi6HkVTQtoWVCsUqTi5IJCMo7d-SFNK-afQlc9HNo-4lrkghr8itl00l6ha322A5makk2uKwAIyX-5vJGNtZTZ5SYbPjvL5rOu0TtvGrdHbszyllcW3Yy0c3M0c97FzhDw1Dg61KNjjErqTkVNiDAdyyfQB34it87DRHs3sY3WbP4_I1Hoz1khn1of1nj4zVAzxZBA-zQkvUM7lKW5ZxbUo6OhGVkrocFGL1e-jE2AfbfGhaboccjCgswDCpEnd00APAoy3MDmtAKqWnA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=ArB8k1zSCyhq9w01jCA4lFxQiLBS900pTAurEUL9uqB3BRp9EjHjM9q4J012feHgpfes8Zi6HkVTQtoWVCsUqTi5IJCMo7d-SFNK-afQlc9HNo-4lrkghr8itl00l6ha322A5makk2uKwAIyX-5vJGNtZTZ5SYbPjvL5rOu0TtvGrdHbszyllcW3Yy0c3M0c97FzhDw1Dg61KNjjErqTkVNiDAdyyfQB34it87DRHs3sY3WbP4_I1Hoz1khn1of1nj4zVAzxZBA-zQkvUM7lKW5ZxbUo6OhGVkrocFGL1e-jE2AfbfGhaboccjCgswDCpEnd00APAoy3MDmtAKqWnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOvULrb37AAVIjTq7HRVndOkT2nRFumR66ebojF0tD8UqAtRO0aSkysjcLAzrYBSESk_fxfvOShRpYJiA2rF-zvEmUVg31yiWVAFmuXVHR7IGHqV6KnMzNc6wXCLM4HJ1IyQInKqxrty6feOGVmDU9jEK7mT3_wKGYgDwKsOh4j6_hLrhdjTixvSwQAu6goaOZiklwzo0T122I_Ks1xS2SdU9aFAdCi11a1aGHRH6DBf4yE-OhwwUDMoryohBPrdI8mM7c09jiXbjDHtamqEQIN10gloRc86iNlyUbXPpCCeDWhB6yqUJk_YO9wn3BSwHc5W-7QtilHnXVu6sCPQkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krhTQJBt9oBbwHsAZjxHqW_aTcYnYIyV56fM7jvgh0-Bn2p5X6ynyySC5JoNGaqBTsAyqekLLVIhuoLJcek1V7G6Tf6aEtzHdgH4V5DyGJQagVHzpTv-iIqWmfep8UIt97R1IAAmXyO3hfLUe31L4ZYgRBUuvz6dXz3mbjrwsfFEJFFCmbTd3zpcWP98rVScmNm6Ya-ZSzGLYP4BZmdgD_R-e556RJ4t8qDyZZFDgSutzVkkfNkU17xeJEN5L6ZMo7yoahYWRMFJNduyR3knySuSCE0IQHvqxsRo5CuvMvooqIsiqdKiJevVApfD6NLpNrODAj4S5ZVPpfx2h1oV8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOZYTn-dahlQ0A0HAS-e9qaNz5oxt6ps02kt4GQo72qt9II85tQIbWpZyWDLK3wdH35oN9cIJYKLMIzORC-USaQsj8EnzgzJ3c6nAMoYhffBPjSzyw-OKiCLOix7lBmJWWf9znP3mkfKKc6FdGXvwcMmhaMpXIxlTuZxZuU6gUYJvvFHrSKD31HrBJeabJJFTwYbkcZ7jif_f9QtiUnwhMFuZWaolyZcm1p1I5yfePHwqcIIblqqTBwho6fS6z4mngrWK2Q3fLxQy7Z4wzLadGv3JRbJG-wkvVhbB7be7C79_BIaucZWtJB2XgnayQQOFDxXVbn1fdOS0qYdhEhcOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماها تحمل کنید چون ما میخوایم
۴۰۰ کیلوگرم اورانیوم غنی سازی شده داشته باشیم و «استقلال» داشته باشیم ،
استقلال یعنی چی؟ یعنی هر جا خواستیم ده‌ها هزار نفر رو بکشیم و اینترنت قطع کنیم و…. انتخابات مهندسی شده زیر نظر مهندس جنتی با ۹۹ سال تجربه برگزار کنیم و
و بقیه کشورها هم در این امور دخالت نکنن!
بگیم مسائل داخلی خودمونه!
خودمون حلش میکنیم!
این یعنی عزت و استقلال!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5AZm8d_3C5klXo8zt-QhvwOOonytVjIO0DKUeW7SCVKBVn-dshM4_Cp9enkK1Hb5XfKSmt62aAuIGuhvMgkaTQ7jAWOnP-EuYkeRh_kwL3xXZ01cqf07qp3ofvyWAbkUXjEZC6sHSY4ygKTA2-Cs8wn1IsBJrCRhZVbUWlHXJgzkwJWtehxvni8CXwykegMzngBkNBXF7ljEV70AYkTbGp-w44DEy1fS0UrrZPpaNFXDVr-Brb1Itc2pQaPp8Zc-lA74RXJBttQ0t_hvPCyb6_4jZmRIdotYNMNUPkRkLGmP0lhWUy6U5TmhTw_c5o0S0rtKZ_nxi0JZxG_McVQwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NU3FJglS9GTC98AetIxodk695eMTXRqsVDM0sVg4xyLdaM2qEuTTnYNpV5-Yery1HsU3EO6hOcd6C5-7cpq0qPY_mcJm_PLSGWdysUla3dPf379IAKBo3OjHih9wJmkDIZ2bdW-TdJOAZHh9HYqKaru5O8czfn-bTA3m0grEoiuxFHg4Q9f4715xcLQw_vtZNqBOb7-ul0y040DWO4lO_xvU90Ew2qKH-T1ZsM0ehiX1twW8-jvLoVH_bJoSemU3oGzdZCoogqrzmG_kFCCFBPX6Ybc3b-bHlcD3mkwo0bACVTNIGBHkSaEYFs8p6VPBfaXaM2ln_F_n0SFq3ZMCFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BpxxlitHOlHIqL9a5MxvTqlsgx6xSqzRbIekNbCV7RGPu4CJnHXmZzMjdH78hPGOaOtkSokxI7n1cclTwOWk2p1d7hiB-HAr1HckffksFHv92_8tsAfK_bqXD7-RiQzblqhaxP-IPcllbaAjPuxt8MaT2hvfnkE5DmeLVnRzCc-mTXiPVR0XSjXu-A6HUrSaOkbX8QTNwPXvDswqyC5APtQvrKK1ibC6TVxyOK6xIOPZnJcRFm8SQpgyJf1r3fhWm9DsFWlm5bpC4zOcLCgb7zvti7-t9Coj8gyhLkspS2pcatQBeO06c3eCwr4FOthRyUEQ2xfixS67OiAhI8sFoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgXddTOkzcsP59dpVpdAm_OA3QUlm86CpPjSXKlIzGMBtkX2QASC21TZ-yT1bgvWnUtjVOfg-NggeCnUBVmTrnnXqaonbF8DKnIVlGSGVCntdnJYGQns_mncrZDflXpEgWfRzWaCXOMyfCHEMk_xATKr0IGrDu7nLg76_L1jF6YhJ58jotbSli-kznxk8o8LOHBdUhiTscCgURLKS07f9Pr356ccP6h1TG0gmsmxGARkwlWCOqmsYkiKevxAooMgbADRwo2TECMK-j3sL_EDTAEdUYriYgWg7LnsRHEkONAGUpOm8Riu_aVUAAOLiN7NfHha4ZvleopQ2tSaPzFbGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=dy4rv0pRhMjHdhRvJCw3FETzcmNtNpEDmJaoMz0GvBROUsvpo-EexkZW7z_Swx6LagyMdNkoB8OvgukCip0uBM-DThNRey1isW4kCyo1_th-HVl_kuueng8Dz3GHleu5kz5YKU3CoTXW_O8OBJ5BCT3u6r8mKOUO8-KyMJ0mVkVdSoRJSF-URz7-eRO99Mhid_jw_AQ6nGxu7ZTG6TvSjZ70JXYZ55PxBiAeIabsaEyrUTOlxGZu96MHK4QN0gYFsZeBTxvCO3tMF1ZZHmotlr53V0IIkDK9PkeQmcL7ML903EO9A7l03AS6lVDM708W_kgP3YIY268ev2ulLYeKAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=dy4rv0pRhMjHdhRvJCw3FETzcmNtNpEDmJaoMz0GvBROUsvpo-EexkZW7z_Swx6LagyMdNkoB8OvgukCip0uBM-DThNRey1isW4kCyo1_th-HVl_kuueng8Dz3GHleu5kz5YKU3CoTXW_O8OBJ5BCT3u6r8mKOUO8-KyMJ0mVkVdSoRJSF-URz7-eRO99Mhid_jw_AQ6nGxu7ZTG6TvSjZ70JXYZ55PxBiAeIabsaEyrUTOlxGZu96MHK4QN0gYFsZeBTxvCO3tMF1ZZHmotlr53V0IIkDK9PkeQmcL7ML903EO9A7l03AS6lVDM708W_kgP3YIY268ev2ulLYeKAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpykFGZHDtC7Ywvi535ab74GgFEvcVvyDuDP0_FrgH5HumKeQjP8-jdp3DfSixvbLouWbTvyHKAbvxtMPqaJhSke7XeAlZ4lH4x28L1x4AYq1RnyrIB18h8YIqv5zme-k_2GWUDoFVjd-JC7Cv9ns2rreenA0s6_snEhuOjRLvBxk8skFMf1L7xmTQi7dlLUiyOWL4KmE-66w3XsS2Y9H1_s2Y5f5YEisQx6bc5_LDT9oFvg6U-b2U8yDmjOIFR_e6IdGotp7DU6bNvk_sx8ccDxsv-el0CUabhJUO4lT_7sAFQvJfIwugxXBIW-qloPP8zZdnqEHfXRcOdZKFj01w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POwYlKeL2FmmiKf11o6FaYq2l56oVxK2UdIuHNuqpy7LBuudDp7GaG5rS13CyiMYVaxu4pwuajFVeJ2oNRtyb8ZPcaKdYXy1VfO-gFEjg7_mDqAkqxNgv3DkrozZRchu_J0A5eNem1gu8-tjR9qH1wp1xrRO_4XXvFNurbOvPKGH5ZBVH4QF1mmTP-A-85wu0YR520ACp2tiLAwRvh4cwBauJn2wxrEGLq3_WFUrVivN4jyWe8hPfjiwK1Yib8p7v32ZWMg7Z_h13EPlKIvP5QQvR2A5_gpB7tQH6xfS1oJRnCaX93Tkt5zNoBEdqAKbhrHIPMg7RrnN7FuMHbOBEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deSshvWleFFchutc1iXiR0GlDD8uYmkwCUch4pnbwXMKoibmf05c5FPpkcS0Z0KJ267ZbMw4apMa2kz9DvJzfNYRrYuM39a7nL4Yx38RJieXjy1_L5a_lV5t-I6tdVEIovenSqX-VKsOoETme06BjFKMQU_LPoHyHK8jNXMJs69AnFDEcE3tvu5MLcHsFZkNFXS8wmcrZSm0rVs-8JiuzVnmBqf3Yvc2T8lorNJ4oflDb0FSzHFI316T3jZTU_qv5aNKz2EWe3GTzxt-5Ve92SQoq-OgkOuWML6i_IlXgCPH-Hagw7ifA59VmwUyuNvdAbNPMtSKpUGCK13XZRyFPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fV2FjIPDm68hohLkh5S1sZajRQoWWS2vzqJ9YMHlTobV5o5Mq7R1I2oe_K1S0KexkcoQpO4jnAk3REMskHjxhIkIKqWlhzUAwZqxtvwS7I00QMM62hRq58rD0pY6HCvorSz6xpgJsDdXYFdtEsWcFD-Kk0FfWcFzk-kP5puej4x3cidSkDR1Ey_kPhr_0f2SO7iyejDNzsWQ5Q6PKFTcMB7aZlUsWrKyx6iIEqXEdS0Eju0VaW_7camccnLjAjxpKx-26Upsz1PZiXjWowkRSyxtXyAJxa8ztOXmNN-MuHRoeDkyj9Z6-PPxeeqFPn8QiikP8mCZvD0HlAGBWpeAMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=snKWnTmsgg3lF7qlJeUWDpElz7mNV9Rrdflwk2iHTGC8tApawDoc8ZVRUbCIF8O-l9zy7aTJUaIRLv5oGRAVEy5k7qbbHC_mRTqbhwMbk28PxAyr02HS1blopRthf-24q4tb-jYqO7SoIDS1OaJtIT4qrZSjKFlbWeACKRMW_k_nSI3QoyTpfe3ihzi8zEeIC8IG3Xkl23PfAYThwdRbDHurCPxhNWulEBk1GWch_RD42pSQX_VEDWykZP5bS-2ZUwIBOGmPBBf2VQ79sM30MxyVeM943TuGieXuXiQf0TdLj2TBASY3cVkDW6leRq1dRgQxqkxxjPqk6vXXNhc7yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=snKWnTmsgg3lF7qlJeUWDpElz7mNV9Rrdflwk2iHTGC8tApawDoc8ZVRUbCIF8O-l9zy7aTJUaIRLv5oGRAVEy5k7qbbHC_mRTqbhwMbk28PxAyr02HS1blopRthf-24q4tb-jYqO7SoIDS1OaJtIT4qrZSjKFlbWeACKRMW_k_nSI3QoyTpfe3ihzi8zEeIC8IG3Xkl23PfAYThwdRbDHurCPxhNWulEBk1GWch_RD42pSQX_VEDWykZP5bS-2ZUwIBOGmPBBf2VQ79sM30MxyVeM943TuGieXuXiQf0TdLj2TBASY3cVkDW6leRq1dRgQxqkxxjPqk6vXXNhc7yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pytMMnDAi-mqjHgHbczwWEvk2ZyW4JWN8limDyYTq8IY13LhSLXfyiQJHJLeg9Pdh_GUBt6rxXKgxBNp3K2g9vlXiZ7ZvDp0k0pD92vNww8BvD4s1bYbqgz5vTZZQo7LepESMV9YpjqeXJW8596erKef6mAWWWfClRlQtPIJzXtDJnBT-Z850ZOKsbsC8s2pVCrLj4_OHCkafT5Z8AQbQkYenNs8cJFjA0i0n_0cJzb8dLRwU8aeHrdyJQ85jC-X7vJpSJX8S_ik1NGAHr-oviDkYdEq8VPkCn-TfFZ62ghh7n-aVtv1B0t2UnbrQkKGp3RotIjAeKFNpAqqcS7TVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VShCMeiQ6FgsS3TydpA_3ZHqPfS_7ZFAM0TPWezixte5COaStXy4RqIZEIkwxJQzNi9z_8Vjdww71NJJ3VMKrDLAeDyWBJTnoOyJzQFfa5OiGbSfQaZBvRcT1vfbtAxDPfbgWNs_LZY4ighFzfYetuAN8cBoGww2NG2flU3f2GxbUFm9uq8ZrFa7gA01pQe9ywnATdb4nUPz_96DyfIL1ER6H1UQ1qhbTrhobKvpmhf_pF73PlqAK_ttiiP7ReHzcOIVkoV3TulyQowQJ24ErF7azG0z4GrlJhBZMardBgNew_9hyxXIAf8KUWMhgrkR0Urd8MJKONpusOTERx0yIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK2w_OaaZ-RQD63_ukAIgUvpAgMAKO5OqPPgZMUk-grQ4KBUzrgAusHqatoDOGhLIQGVQmwNsUwXU7SLKNmECzFSn-r5pjDRBk2dUgV0aPxh8HVfDPbAZUzlZADRkvUGMBHs1EjZVb9dLkIWZpwzdsNpfIep4fRHh5eDIwaE-oiVQ6TpRHzPJSgjj0n1SWuZTs2fm-nmxoWDcZA6UaTyGV_sR3tckRfjKixlZLDmnwzpWaxajswCrzgZwuLl-e_Gh6dHGhESD4Qf7p_AzqjoqN_zSgjYzsWTclCjxwTrQeRPUTF28nEPp1UGbXh2w3kwG-VurfXhRJWxIk6mS4_yJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_uMIAX0qSVuogGkgQENB_8dcS2x3i_CjLku9f0KSy_017i9YUBI9Xiw5wgmVGCUSzbkMl5L8a9jXqB_yGVzDz0nBT-PsrXkloWAIfquNmOsMMaacSFbkeiqqOLhxn6sTcer3TuqQLiHX9gc4a9zqVE7Mhp-NUfmUa3Q6Ovc_rQlCXMdpUmg9lWjhYw6l0AYp3i6cnurxVfP2nB026rybwpnmkPpaas-pWbXHl4cBm8M5j76srWYUU16Ie0X_aSg7b0G5fGRUOMjSA5GodlYOCo5aVkJSQxOxzBkS4RtmmQWPzc6YS2R6oCmAzLkL3xmegb9dP_uGUx5pjqk-oupyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pn9vfWNYKrC5TxKuP6b0Cb_r-8pgw6KYrBKgrgwQ3gR7kGrPEZHaPUVF9uK_vn7XtNuR1kGRIJi65MygipL7DLo1ste_6Lem1zf3pM9K-FJB3HzwcvOZSGwnFWr5UYDS9ShSkpaNTN0fdSsXZjfYRguG7754Bjx6EpkoujGHUDnfouP_mUYQpODhVrQTvKO0IpElcUOFvoRsbHwykjGWxMiyKZ9EnSI-kBiqkdBkP277VIqs-Uu5dUSSo84qDwwndBuhW0QA34xRI5cZyuQ1-oqBJCFtXd6BRpi5kVEJXDjN1FHaAo3jy-ZDWgskDO9YG38egltO6SKEvo9M3YJJOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=nuVSke6HA_jPvZVMcClsMcrbD7viLJNQ1TTsqfpR0KZfRjbdUJZRe44fV8nTwYSr_x-w91TogRUwA74CzVmmGtdxGZTsT1ISl-sw9uxa531EpAgmIL_WCXfYH015Sl6-MuvCHe_8ka0onjBOy_ENSIl80ca6rkx3hW0ByQOvNu7lsWco_wK0s_CzRyziA6FzsX9jMtvjR-C4RwH9uqDpa9-Gt19UwaP4bc60tHDdP-SdyToLx5l5rsQysIuq8mueBsqgB2IuEplFASAuaA9KOUnTJexRcLO_mo3Amkbl32MtMYu6kDIJLUM4VqT210oBx2MeH7ZR4rqMEpjxi2fpoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=nuVSke6HA_jPvZVMcClsMcrbD7viLJNQ1TTsqfpR0KZfRjbdUJZRe44fV8nTwYSr_x-w91TogRUwA74CzVmmGtdxGZTsT1ISl-sw9uxa531EpAgmIL_WCXfYH015Sl6-MuvCHe_8ka0onjBOy_ENSIl80ca6rkx3hW0ByQOvNu7lsWco_wK0s_CzRyziA6FzsX9jMtvjR-C4RwH9uqDpa9-Gt19UwaP4bc60tHDdP-SdyToLx5l5rsQysIuq8mueBsqgB2IuEplFASAuaA9KOUnTJexRcLO_mo3Amkbl32MtMYu6kDIJLUM4VqT210oBx2MeH7ZR4rqMEpjxi2fpoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5046" target="_blank">📅 23:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=EniADGMCKkb5fnuV4Zdw46vbpl01UbLxQgAObOtXcHXdwkRUA4rIory8fHdbSXrt8J8-57elrDAdo9c2diSWqQ5uAXElOH8-d484g8gfCLo1yIq3rF-c5xJZzrQrsQk2VycqClytjX2cQLbfp6O0Ezry-nZIOB2e6yS6fmX5WzXMoAIxxzTEober6_bDj3aZWf0Vwoci7aUHrah2JVOHBPK7ewwIntzgAQMGki0nNCzO5mPiMM__Rf6HbMMWG-Zg7l704m67NScFgdd9FOxMAjJwq6V5RUAWQBHcadxyS2yqvtZdWthYip524nhFxCMxPjvFyq_ultTd9_i-5kzdgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=EniADGMCKkb5fnuV4Zdw46vbpl01UbLxQgAObOtXcHXdwkRUA4rIory8fHdbSXrt8J8-57elrDAdo9c2diSWqQ5uAXElOH8-d484g8gfCLo1yIq3rF-c5xJZzrQrsQk2VycqClytjX2cQLbfp6O0Ezry-nZIOB2e6yS6fmX5WzXMoAIxxzTEober6_bDj3aZWf0Vwoci7aUHrah2JVOHBPK7ewwIntzgAQMGki0nNCzO5mPiMM__Rf6HbMMWG-Zg7l704m67NScFgdd9FOxMAjJwq6V5RUAWQBHcadxyS2yqvtZdWthYip524nhFxCMxPjvFyq_ultTd9_i-5kzdgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UutDvigrGfpyrqIY0rzxJJ04qQsXt5EaXgVGgssuFVKF7lZC0ODcAe952npVH1a4_ufGdLWdPYz5eve2OkIivfGZIfAF84SpSF6nIXrKLTFGxrAVJE9bk_5fdRGodvpV2n2boAC7183LIeIa3KrHqeWJ0qzlpTdfVR7LlrYI_nEx60p1-n4AIV1nWsEYz_TwDnb_UF7CHbU7nZYDZCSHj84vyyEzKnVl6qIJG0XuQY6le1NxZNsEygEBmPnqxPff6SjPYlebeZM2XHQ3JQQM7fnttRdTPdE0kwNBDu0LLKg4Msxm1BcW0yJKfjkcCgPD5lGjyBNIS_ASI9mwnX0-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7YAAa0jtBPZDsTsF4LlHXzNvCA7zrMTM_2kfULrS9QnFofPAtVMFCjDv8PxgN_X4mVgk9i60Ol7PSRREch9QhpTJvte1YctPBRNhtiTfyIPPQtlFrSFrpjcG25Lv0vP9BruuXcZYdXFwwjkCF2eSioSArB2GSLhiXd0MpTdAcAE_u9oto8e-kpV5a7lQBv1_t0v8DAGO2rC64037T1QTTKAaEpDTzNP5-kRmnnjR-x6P55dZh2ZW4hPhhhqcjgYVtPC4SBHqYfHszNexaiaZTAccqHPAhAPiYHqkNxzSKJ7CR1rW8EjIAXsMq8ZyawxUCw0BScTkCtT1tOY4cUPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M5av76p10yIYcjPHQ58_YDuodp_3d8KnZSTmitX5AtXcFA3Fl-emOTX-I7GYbT98O5o8S0jJD8vfYZglJP6Gy-1otuQadI9trF42EIppWRgpsbN6b2QwIZODC7KEW6vfpdaVzTcV6_jI47V7Mj-VUMDUdpTbB3Gp3YFezmU-YkpUX5dR0XRWUTXwjvrc2bQ_aaE4xMkQes0elRcUGQzzcyNY4ZLZKDt_Vs5M5gNfB4QpWvYeE88d0IGqT6nYfh7X0Pjnlnc8lf4KY0luln6lVUdFyNh6ywlQRgC04X5mdgSjVDeaV4Lp1E1pnp-8lY2F6VwP6ys0ME8-qfPuUMxuHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mEso11IxcJEEbPWkp3c5EC5TEMVaJDHBpQCIjahiVrvzsSBPndHXN6692_vq-YrLiu32nUEuSt_Ro8chvLXA2EhpBc2ECfr7FJozV8oM7RwtMRUeJvASeTWLhaLe3_MB4-lCmiNW8SORou2EDFdg_6EawNFPeWFhrLn6KniuwCjbnp8nsXuZ_LILuC6HTzHqMUEv1kf2EwzuOxBU1ql_u-4fPSnjOsxTRlmd3ykFZDD2rNZyOM-3GGdNNYJkq0F8AgsXCkNiw60atZ00VDnMobUDrbOkaZ5kf5gGDv9bTCynbqi-7qTpFCBpOFwD4YYwdBy6NqpE5SkjdR8VbrSSnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی
۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!
توی ایستگاه مترو هم از زبان رویترز
نوشتن که قراره ۱۰۰ میلیارد دلار درآمد
داشته باشیم!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5036" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=uGJ5zJg0O-mF9gWoipfmGa1a_XMAcMvnjBzUNGI4wGQ7WzKg-8tLW4QnMCoW9FwAmf3p1q7QCb-a3RRaWjjJTFEdFjRbJ0OZTAbXr9f4drwVBn_9Pm3IpsUytN36-4Udaedq2Tkpd9hy2CQBPfZyGIBu-kZ68U3wpRTvPefLee-vhEkbXtvqoqBMCmWpp_PQ8U_AY79DSoZC01PyYWH0hiaAXygb0SDXeoAYSNpk3pFqW4s4vapqpl1Q6jhXe45LTw3GXURjWagb2-jsk1kZvlyT2pr9S8pbMPehu1ipn0VaM-fbI-r9iQV-dII-niaxZkpPGn1dhWNvxQqrTAxmig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=uGJ5zJg0O-mF9gWoipfmGa1a_XMAcMvnjBzUNGI4wGQ7WzKg-8tLW4QnMCoW9FwAmf3p1q7QCb-a3RRaWjjJTFEdFjRbJ0OZTAbXr9f4drwVBn_9Pm3IpsUytN36-4Udaedq2Tkpd9hy2CQBPfZyGIBu-kZ68U3wpRTvPefLee-vhEkbXtvqoqBMCmWpp_PQ8U_AY79DSoZC01PyYWH0hiaAXygb0SDXeoAYSNpk3pFqW4s4vapqpl1Q6jhXe45LTw3GXURjWagb2-jsk1kZvlyT2pr9S8pbMPehu1ipn0VaM-fbI-r9iQV-dII-niaxZkpPGn1dhWNvxQqrTAxmig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=gU13ZL2GDkO46rL-sA0BdcBAqPTqaqQeDtpDllYUpskUBfMwtmLXR16OQFvHhrEEn2NJ3z1CRweX6ztjlKQ8kA3bhwZQ67P89ZNsPFOUrktnCAKK-Y51AKxrTuvHs6x9EMc4Y7Z06r4l3gRmhRbMlYiHWB8SKSASjfukcwSW9R1PLQYymfHWuAT6qwkzh2rY3NFhSylEhYUWmx9b3aFJHNREilGopMqux-NiH-yNptIMD8Dg_WQ4TOKmLCPq32C79RitcmmwZJlVgPzPIBrRKlH6LpzbuWpnGtV8enXtei5zbcbnRJQQ--jEtebC__MKi2kIHZSe6F13BlTSrlw6Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=gU13ZL2GDkO46rL-sA0BdcBAqPTqaqQeDtpDllYUpskUBfMwtmLXR16OQFvHhrEEn2NJ3z1CRweX6ztjlKQ8kA3bhwZQ67P89ZNsPFOUrktnCAKK-Y51AKxrTuvHs6x9EMc4Y7Z06r4l3gRmhRbMlYiHWB8SKSASjfukcwSW9R1PLQYymfHWuAT6qwkzh2rY3NFhSylEhYUWmx9b3aFJHNREilGopMqux-NiH-yNptIMD8Dg_WQ4TOKmLCPq32C79RitcmmwZJlVgPzPIBrRKlH6LpzbuWpnGtV8enXtei5zbcbnRJQQ--jEtebC__MKi2kIHZSe6F13BlTSrlw6Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما :
آماده‌ترین برای حمله به ایران اسرائیله.
اسرائیل نه خسته شده، نه پشیمانه
نه به آتش‌بس مقیده ، نه کم آورده</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5IoHP7h-EbF9lxEvai2pP34X8qKPdXXDc2jULuz3mtAy1FOO6-mSEpsFzbSUS1UQPunLqV6VYzfdFTn2GbuyiQDyMRaX3-srZIoJG2U-wKYGE1IIVGH6_9ea0bi18DljcoLQtT6dJby_NMus7-7rJmeRiphHFwQ1A37qi5PHale3wM8ArOA3Uxxoy2U0M12dRs96I_V3hRmjOdkHkAIWdA9Aru_2k8HF_U_4-rrXgXZKwl8ZuX_eTbmG-TPFUKN55OcetbXvpiwwqnOyBP5VaeQgHYSlWIqv5xyZY0GmBhacOqepn2fYpr4-srMh9fkIipmoXKd6V0vn2L5rcB9xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcuDD9LcuJUnubY1bSnZRUAgf-Hcq6JQ6W0rQ5YLt1Ab15Ofk8QG_ZCojuefMrouBGj6JXZx8ZtOdCsuFOc_iK1oPJYHLNiFJz1IK0RacLMNvRciBpHZ0YDHAn4acXIxFr3Yr0isNVdyX1kX0ObRoBs1bv30SVrf16oTLvvCcktJr7wnaLo0wLReNNmpIptk_lxKi22Ms6KXO5ao0rFVGg-v-Oo0_vfEKZ4geaCb3ME8uHMZm0uyyNqCPwveFwYlr_wj52jE2_ybwllKLc0VFIio6F5MbGbSnmbOpzerqSWkwDI2DJfqdCJ88vr8DtmwfIYtyLsuerYIuqu_bJPAxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
