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
<img src="https://cdn4.telesco.pe/file/HpcoMQUr7qVHz2TdCYJYsi3WTgIoWms5MNZPCmEvcTOFpWfRRzM9KJx3_YzZ3K5EBkUWfriXSZWioiLar39BMmuuniwPWPFxAlamCyxzpbz0b1RFlicSTbLyakfOjqyp_41nn--Gztcmd4NjdNhEro0ewVZX4Kpg8bbkxVCta70yaDdFhqDuknDm5UeIxU_u12DaMwO_8ivY4cAJmJEi_bxT30QWJxi2k0MXvAuKOyAOAJvSfHcx62CdlemB9hwzKLNF4Izl4uW8mdyMi49V5wH8r93ukaXtGlVJotez3jKVfkEoUYesO8pBGiaNDAZx-rLvXiIH2b7-K3UkjgksgA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 21:15:36</div>
<hr>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سخنگوی وزارت خارجه ج‌ا : «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
🔺
یادآوری : جمهوری اسلامی از سال ۱۳۸۲  (۲۰۰۳) مذاکرات جدی! در خصوص فعالیت‌های هسته‌ای‌اش رو شروع کرد!</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/farahmand_alipour/5113" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqulMgxIz7Tec-0X5fZKvxfFuusRIXVzJwt6qEXXJLtnPTQvt7lkGh2DEQ2W1JwBnAQ-O6k6sWDMCclZ5dyeJhCFJ7WPvvByS2309uO_GOx7a3hEO09N7g7szGsTism8D_awWUpF0NMp_nmVeusKjqxXPf-T3gHdyeUVRKas1BIfMt-NL9tzRHmaLIG0B7F4EA98uFsD_xFYwxCHgNNntaJMCxOn8B3OSq3UuEtbOG_fwvmP5-AjZ_e2OroMqz_CVws59Njl83cqifW-AH4O-7c_YWaqVkdSrxIg5NoVZ4dQ6KlYac3bic5a6A_4775i4wbZK8gZkrRHMlGLsN4rmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NODy6g42jK7Aouw0EDSkv7z5g6loY-zndARer1KBAdZZ9fh-h2vahLeVJkGF6YevRqirrTpE6OPTxjG6Q9RZ8heU78zuK2G78cYwuPv5g7y6sqpOEAvBzU_FKG-noWf303CRGgmwhCVYjRoE3ipwMiEkThXENd8kLr4cs_tVTulLO6WXni2cQb-xx_CfVSKgjCnP3cuyyszOBIxJX8H-11hHd4zGvjeuYzltaq4g9pigw0_kUrHCA2qYb7JM4-PpTK2u04TzRBQwCY6lFvMgLpDRPSpQWgSBX_dCy-8eDN7b52lsFbE3uCkz8PkL3VwqmiGeFRmcNr79Xajhcm-0NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUwgL-98ls8W4FfDYdSYaR_TjhymtpJRX9uXIH6gQHdOiVF2Pl-G9ll9IASITg7qV99WJ-4KWcunvv9fdx6ckXIy8hLhEiX5M6j-dgE-Ot4yEWOCQCm9rmhoWz97mn1-xWlIV4q5t5xB_otBhHvyF4reHR0-ENpjLCi-05ECOhkfOyDoJrnJmUckkYPKM3aeElbThcaBKZjFH8-m2MUlc5gGrYyq1rnhWpO5x02Z1jE9__J8BRXrmau7nh-Ea8Jyc0vnGxIWFBGZEGFDAsDAl1wgDrlzrRefup3xgX-c2KqwsCqJLD6yDsrMxIfsVccosJdXs2Pb8YgReSqdU8IYJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW-mgaeDBCVy0iK6psiMs5FL4oynpiogUK4spA3EjS2db0VYKDwXz0rDEhpY1Rb1yizumrgE7lIssuJnQfR3lbBFefBDa7nO2-Sm6394m8xBOh2PF-BMnzZXXa2uw27pUvY8PdFyvaYzjs8xhO5Hif6_WfbN14wR5vDB9rSbocuYRHWswlyVzWIH3o2S-rHHS19dXBAdrCmFavP6KbLBw2ExI6W2AzVldQhLXzxTnNqXksYVa10gRhDbnPvMNDm7t7hX8uZRsBKjDyvZbCMbpyzkz0zvr9QTf8M5dx5gAX5UJuhvdp-1YowDa7YcIsMyWkOo2R66ikXxLSQhlbhBjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNJk4sEEJHlVDnxY9yrY2SWSNFQa3-b41kbSw__xroP2c62XuV65rP2Sn0rKthW8naQUCcIqz79aYe73mf_4wvUwq3xqpp7WgGRf2rs-F71C7S-WPAzy835VqzE1TlzDC03i_Q_ps21leAqLY_4p4SxumcSgFWVEg_MF4Vc3j-04ls8d2g1IR4Oda7UfFJktnu89Tak2jyWlrtQJV0a8j3lWgdPf_wyK3ANzRc5Uf0dW6ltTWmoWo5DQbZs4sqiEtNvh8ZBUl4PV2HWnLHGAB8az8fpMNicEKiz8sxFzU4jVhwFlK68MYR2AMdkwGyZZMfO-d_xHN3bXMJ0Iyn3VDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=sshVym8f7_ADoe95e4da8eykzwTD6Z3MrqtHpNjiknMy89Q4e5N6Je0C17Q5TXBYufM5kAtfIn7u9RllF9-fV5_FxjfgZ4MU4hzLj-CxgPIQbmooqNrZzUYHnBuYdGHiGSoNK4iqAubgARWxlGfepJXx2YLN7fyUaz9bWRjHoqtFywFmooEUsYoHuTV2i9OXi8atEO4lUiOKYRhC9sDdZ0Vpc0ulaZ9S8Ksiu1dPK8fi1cMzXJ37h7c9LD6XaX1F78LvxzVodmD-lZHc3_p3lvfq2Qi50KVgrwmQ_aND2U-yJhoEqQjWEn84SWd86syGfL8Eg73SeT_Agngcd7AAVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b7e3e4f1a.mp4?token=sshVym8f7_ADoe95e4da8eykzwTD6Z3MrqtHpNjiknMy89Q4e5N6Je0C17Q5TXBYufM5kAtfIn7u9RllF9-fV5_FxjfgZ4MU4hzLj-CxgPIQbmooqNrZzUYHnBuYdGHiGSoNK4iqAubgARWxlGfepJXx2YLN7fyUaz9bWRjHoqtFywFmooEUsYoHuTV2i9OXi8atEO4lUiOKYRhC9sDdZ0Vpc0ulaZ9S8Ksiu1dPK8fi1cMzXJ37h7c9LD6XaX1F78LvxzVodmD-lZHc3_p3lvfq2Qi50KVgrwmQ_aND2U-yJhoEqQjWEn84SWd86syGfL8Eg73SeT_Agngcd7AAVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
جمهوری
اسلامی رو :))
با یک نامه ! بدون هیچ مصوبه‌ای
مجلس رو ۸۰ روزه تعطیل کردن.
«اگه رهبری تایید کنه …..»
اصلا رهبری وجود داره؟
رسایی می‌دونه وجود نداره و خبری نیست!</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=BKxOtK_zsX-kQh4eqCbc4r9ILoH6o-XgHP-ulylKw1P4GaD-RyUFPM_vYzl4dTKxM-QCGLJIKqwnyY8em5XfXXRgqs6irtJPbf2htWVBmY9y4g_Zy9RW0Em4ejjFJS4Ds7LqLCqEsITJtgHpph3xn7ioltBfETshW-J23akSCK16_BkGHYj9CM2siD5O387EBZoqXMk-CY4n3cpijJADztA_79DEHm-TATquyuVHVfuxxRsc4ev13i7cIh2lf-NdJKzYrGJFgE1lsWZ4Z1cjZQJza9KSzV1YiF-l6-mfOcadFh7bLOX7XHfF1lV7qIhOvQhmpHuadAubomj5PbGxng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=BKxOtK_zsX-kQh4eqCbc4r9ILoH6o-XgHP-ulylKw1P4GaD-RyUFPM_vYzl4dTKxM-QCGLJIKqwnyY8em5XfXXRgqs6irtJPbf2htWVBmY9y4g_Zy9RW0Em4ejjFJS4Ds7LqLCqEsITJtgHpph3xn7ioltBfETshW-J23akSCK16_BkGHYj9CM2siD5O387EBZoqXMk-CY4n3cpijJADztA_79DEHm-TATquyuVHVfuxxRsc4ev13i7cIh2lf-NdJKzYrGJFgE1lsWZ4Z1cjZQJza9KSzV1YiF-l6-mfOcadFh7bLOX7XHfF1lV7qIhOvQhmpHuadAubomj5PbGxng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euXzC1q5uoTSmUv5AF95LHdDfC2t8m95eFYAVVMw8uS2nBycBeG8JWBnNU2qu_my2dOwdTbXbZxcfE1EWithS--OCwoGBCRVMddfQAn31hUiKByqZA3Y6gGBHVQomeKGn7ni7Hjdn5zov1fSKK8kKw1rxhsCwNutR69gFuTdhcNWpJRTB8jI6xLC01VYhxhyDAO8LSRvPBqOwKyXMTogLnh-iRIKRvIHTx3ShgrtC9BTAQwuANNYNIhFYCaMNIhytAx6Jz446SZI_6qPqICfo8_IFmuwBQgioCuNOLgC_Ty1M9oRxOoh0Riz_xMFAfK6rA_-jAPmv0Fjv6c9HYRJAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeHsoWlsjBaCxS0Zb9CT2iJcjdHUJaT8WLZMuBPFHbV1XA-GIKypcmIhuEMgPmIPTq0rzIowHna2JtPEt3zG9C9tuQsxy3k6BFmAcwbREUJhhV_NrzJw2-XTwOjr28D5tc971A1tKF-uv7mOdJGUsXtl6jj0xOi6BCCurr5gEOjjh2oy2-LMzDLnxDpHiJRC-HHbBtHFru5R2WWVkm3Uw3e018iC-vH2r7FqJdbk0NW218amFuWbgjo4HpkU-TS_C_WCaNawCoB_7m8H66Zu53oUnPwUMgCl1exIhiprbz8w2KbG3FqiVp5xqMh2X0QTPuFYxNEwnLigKrlwPxWHHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDY9fhlzeqbIqjc8bW5cIJ7mU6dfLgpTJDcZNqZWMWImWFVJ6GV0A4Bg0XEA4IXYA8BSR8KKR7IrkqskKaIMtTsvN8eDJMb4TnecWqFymTHXBkNNTyCpEBuVCi2gNd-XNAAcD0MRm2NN05fixJQ7tI-6stDURnNd-CPIaMggOyjv5_1ou1frg4pBuoJU-DNkwG_EORn5kf4TPOQWE195GSlmFrngfOIS2h_gSetnHUXoGNCC2hn8qoNDCLdhPnTUnMIfXGstonoqypvJ59Sfsj538Jrf2JX6oFjwxMzqvbJC_IfUcrEau6ybdVADK3DrC_cVD8rohBhNl1UOwzyORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=IgB1tVVnG9iXSKW6QDOsaHHSC7YLROVI4rgM8f55EY2TQNBFW2g_5Xwzg5MlbDZd-l5-nFJylxO965fkA9HKnBNj5TZtEnsjLdg00g6viF1uJ420BPhRGQnNdwgzhkIlOYcY-pbvIsKGZWrvuutxY_wNCbVHphYsrW-5iDFddEGsQ41brZsnxF_pRzT1n7-DYYmWPY3r2D0gX1t8XdS4gCLzaBVFAhYrK0IU-BF17nqGI-DMPVOlmrVrxSXcAR3Omul4bkmXcU1WrCdPauhvrYCFopYE8F6rsG4MBtJ71c7BYtJLmgFd1mV2b7xpH7XewLV6qIWwcHQtgSq2OCkGoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3794683c.mp4?token=IgB1tVVnG9iXSKW6QDOsaHHSC7YLROVI4rgM8f55EY2TQNBFW2g_5Xwzg5MlbDZd-l5-nFJylxO965fkA9HKnBNj5TZtEnsjLdg00g6viF1uJ420BPhRGQnNdwgzhkIlOYcY-pbvIsKGZWrvuutxY_wNCbVHphYsrW-5iDFddEGsQ41brZsnxF_pRzT1n7-DYYmWPY3r2D0gX1t8XdS4gCLzaBVFAhYrK0IU-BF17nqGI-DMPVOlmrVrxSXcAR3Omul4bkmXcU1WrCdPauhvrYCFopYE8F6rsG4MBtJ71c7BYtJLmgFd1mV2b7xpH7XewLV6qIWwcHQtgSq2OCkGoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5097" target="_blank">📅 10:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E29o9no41s3aKqD4rRe8-p4Zx6P2ShOKUtbjeh5T-pglQhneK1X3UF02vfLJnpOi1ZmrrOB6I2f5BWyZ3qIw15taIA03kmdXlqsyhq48-XIIf6zq6JgxTAuhFf4XV7wqgI_sSN81S9zGkzx0vMLh6BB0YjH8BKoGzmGB13JuVyHe6HjxVjjeLUSwwTt_Jpp8EX63Ij1cslG5Zeu_ISGmZomr9h8EpEfVEjXnUTYPYtNmkeCuQHKowjs_T3SGmFjwZYIujXvMwCC4y0e7qxnb5DLf09AgH8IkYajwllVTZV-77OX4TM-5gqh_swtmhim7t41z33-b2gToIFrLWVkaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OC4GxLukLytdnRYhqriDygh2eZGGTnBOvkUD-YcvFLI9RcsQ6SZ56rCI-JUKBoCZ5U0liPXmeCLVY9N6lQgL9gN1kgOdYfI0XtLwMHkN-oO6BqoaUuR1mp_wIhTgvbEsnc4__-19_mrPMqzWYVA1lEevbYznq4j2BXHMi4C8Bu9uMnORuZ9R81gBB54sONhSQh8wbfFITVP8NDSGRkZIumzV9SvQZ8PKdoSHacPBpbF9cm64zXDbLNkDuKrLkxAt4fFquhSec-ZRHPbDwX4dPfzptyvR8Ros0sHRvW27xWud1QRcduoDCfXaa8fl4uIY4uLpLOGOTo8B8ks0nF5geQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESmGUEpVo3nP4aM-VtOmu7wi8FESlTxp9v6poasAq0__0fOrB5ye53Rv9ae5zpIf4N-eDuoFSe8DsqMiKpAukXdTeYylmgVRhAHU3lBBjDeYkfvgJNS1jxlwFwo0zI7Qhb_JfU9E5QODfMF8gAgUeZDpCYu9TpXociCcWpCSrlQhOwvmVzmeB-Eo0WLtx15RVw5T4zq1nCgkmTlt5zYsLNo90pcy8pQkl767vc1xLmqBwJGhoeuX7w16jybm0w3xuV9ZnLFjKaf96zamcUcfMSUl8PmcyPZVmm6JkqGKap2lneIGm8dRp7P4qzS8m9Z1iAlHkjHmqnumJ4EZoRoUnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhfDPGB1ejk_KP6TUfL3dv22Ks1hbeh85_NOmwelaUvDcoNZUgzdsMGnvfRg1SXV0DRwz5JzhyqWMv1S9TRGws1hZd9MTp0oFdtRM8eP9gX9-piEpOJ1QVsZ3zNGhtjDZYc9h5H8F_LoXR6fa044ufutVfDOMSwkpIjtGt3sfVSCa0HaVKyY5I69r2BJZlc7NQqL2hBm9nT4hEHczmm0eRT_jSqK04qUmXLci_1j3ieXGgVh4_65hCviTzwi8MDVjHJVFBH4FeJe0B-AMNhM-Q4QXXvR2cONtDwUce2MB_jnplza36yX6tvrueWWxBhriCOoF-JlgKiLdp1xUI6rKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ez4sFC-qYN3nZf7--oU6_euP2kZmhUpUBAoYwVFEBBvbd24LJW0A6ctDe5TrgQeQah3oUg4F-hXLyVeT1SZ5LsQTpXaaQaPpA2uBu0C95AkdjV77U3P-L9bp0RCOO2-FbWPIkATw4sj37xsb-auRdhQwFe-lXA73zNxXGb9NI9ueAIYXLWURX3nHUiOOc3XgQHDgOSnBwgTl6Q0BkPZv4nH8-q6lbXgJWx043MEvw0krnLxcO0x4nEdeGqWXZdE5naIUwgRDyjrIFkUAYJGtGeLjyK6YzJ_ENcKTRgwg3duy0Gti0X1kWlHDjpmifoazTY9x0xApmDXhrszH-VTU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T81rBEl8SkfUxB5EZU2KncEHP0V51GQyp490sYvY-DgA3sXbIJyDqJDGXf9hpEE0R7jMyazFyO5LcGUxFcEZ105N3LO9HWWWryWWTgZXJPqFIIG4YNHsGtMVKwQWBYzLPdjkDsqZ6DtkP8jiKm5PREM9jAaDwJnmAfT08ljXKbg_shTg3dSSDty9F_wP-85XCwN2JpU7JeGOje5Bph7I2FMVNvI6wsbReopBfDgK1B4vaKgOxOSSITgc7T1AoAG6aWLdqGw0tzIf6dt2w97jYRKXDK-66MXwd6HiuETUFMI5-4nft1KERpLjXPjmuBDp-5Nqq0jQZjrfjIejP8nE3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqlOr7T3rXV5_UrrAXHvM-xHc6QknxU0N1uPHcMpc2l_9Hombue-8AO31x8vEZswpi3KkpMFadU5oou7spjcDotT3sJQhuQAaCa_M-5RtU1xsHAmmEgZZysanUf9i_d9R6JACOMn6tQ8ns6jG1dC9LnrgjzyXyijvRcmIl5OCgnIMjxs-Q58xjr0yNsLbEUZ-K7IwA_UNfg74DEb7GQ8NRWfqQQ5RqstXo5ACN8ICfaI_X9EHQqSp5NWNgJVQbxw9ispI8r2cJhrElDcNx_saHF1-D3BZhOcETkI_6Cuvgf4sv1IeyWqkWzpUulGSJFZFdMJuhlm1A1PsbLoTGIglA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LWOO23E3yNEahrd7MTWtTTqcgVC16EHBrupyObeuLpEpy_Q_cevQAbIo6IrbRIDd_G1Scy2pTxBQ8G6gThRwotULVCpmA1g4MAqt5fco4KLdupDdOg-yvYVwNJii22F-OEIzGxX6PudazRk0pHoeDwrPnX-5OD2iXbMzKqy5HtdmL10eut40PgvSoemigVHBS__TYIB5-mbfdHl2cXUh-CnrWvomHvWmx5YJNrKQZSmsZl0NgUU3Xbtuvc1aeUPUtAunv65NNzfLRHCzyux6OsN2fDy6yM9JggaYfLtDBOV1-m0aw77nggZJI-b-e1EVU6h42cM-XSKdfJ4k7hDYqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qrf3fiyXRAJzLYZXB3JlpM-gsJHwvMh8JJY-71coaC4H1TGV7R4ZNtwYfg7YiN1jpRW4YhlBFt6cwatn5nRV5e-t7t1M51EVGGEb605Mm1V9cCGN_GpYSLAgQNlgF-D_atvkPnOwrjHMcVBjTltl7-Or5dp4v-aNGEqNocQ2SsQ_TQtcHWokyhFr-2XYsqEKa7MoPNPSumLIJ9C_uSULcfh-4EB6ef1EcKiD84-SfY2r128Lm2hB9Zeoe_GcU18BVe5luG5vlXDDFJjeesREoBmzQZoqINFwuKHwMUTX1Jw9EUeVFMaKZh3gww_kQddd2kdfNl4JNEU6nPcROOL7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERDMdbQIuBEfcU0J1ZCLXCPVcnZtzlKhhRc9IIqLCDxM8DSqNPEyzItrH1-YITigDCru3-VGC7t7WxOqrlVJmacq_GefgVq6IfZrHvVPIgs8-Hko0yWAu15DjZAKRibitSh_i2gqyZCvpIMjirPmuq9xm79fmKMs4FokooizGFvlgOMcPOVgj6Rxiwc00CGd53GsooSSjFqEw8C2BG2sng7EXHYe_e50_KxkYBVBDJxPxlv0Ah8_oCmaHHjSXxUFOmXp7UupN7DWrbOHYc8-HMZii3eZ3qOqtE0OIvBJg-T6jOH76oO2szafwJuQP8YGaTKVa48Oi_G_aQEp_OMfNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKVKNqEdSFGjnqO1oHzFql9XI8j-ig9cVYCiha3CvswCcD2pp9mFryrnH8DEJpPW1-TMx6MEh04HOvInirfYYrJRCggyzP_MTbnLRDQNIH1ndQyYomuH8ZUK51twlPdTt54bCDkoZL2GpamTd9v_Nx0-5JMsLPbRh4tR4h2tof5mnrfMF8tJgl0eP6-PELZEfVgL4hKuzXEqqxtFas-mmpLdsVzs9GLqVVjZ7UqiHP9y5wFnIFWrdPSfaPFrhaCB3vRJiq4vzF4Q0M5pCVK-b73tvE5ffP78nIOKo2weKbfXmlA5l4UgLD6Gchzz7oqhDSN-tlS3xCi5o-GweU4wbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=Cc1YXfCW9SKShf7zHJY4C2vdBJevpbS1AyEYuW8xPTMGOByFey5iyohxjVo-J774LynNMrvge8bLV-Ek4yUquuPm12e5Wr99ZSK4P2Py_e120_NSU3WuD0RxVixSZmrdZ1i6yGohRt1mZ-tG9Qbgm6yb8AywC-7rf3qPerzeD5LWn99D1LlW5AIHrOYeYRFk5RxrkBD9RTErj6VOn7mZVsHqANExW3j66bJ-wk7UhSggmWbBUaPLETkJL0-W6frDBAkgye7dY_whDSE4BcU-MN-u9L9XAJ9AG41XjbI-XaCB8y9SHscBoqLcHlrmlkgO9W21GY9jmU47TyBurmFiDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=Cc1YXfCW9SKShf7zHJY4C2vdBJevpbS1AyEYuW8xPTMGOByFey5iyohxjVo-J774LynNMrvge8bLV-Ek4yUquuPm12e5Wr99ZSK4P2Py_e120_NSU3WuD0RxVixSZmrdZ1i6yGohRt1mZ-tG9Qbgm6yb8AywC-7rf3qPerzeD5LWn99D1LlW5AIHrOYeYRFk5RxrkBD9RTErj6VOn7mZVsHqANExW3j66bJ-wk7UhSggmWbBUaPLETkJL0-W6frDBAkgye7dY_whDSE4BcU-MN-u9L9XAJ9AG41XjbI-XaCB8y9SHscBoqLcHlrmlkgO9W21GY9jmU47TyBurmFiDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاصل ۱۴۰۰ سال علوم اسلامی!
علی خامنه‌ای هم به صراحت در یک سخنرانی «اجنه» را متهم کرد که با سرویس‌های اطلاعاتی غربی علیه جمهوری اسلامی همکاری می‌کنند.
در زمان محاصره اصفهان
توسط ارتش محمود افغان،
روحانیون بلند پایه شیعه، به شاه صفوی وعده دادند که به زودی ارتشی از اجنه
به یاری ارتش امام زمان (ارتش صفویه)
خواهد آمد و شورش افغان‌ها را دفع خواهند کرد.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5082">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=rXwBdEQWx_oeXstAIb9Jn-KPTZ_5q9QnTGv7kbfbgXLcy7tX8mMLLBFNBtHnM05Q33RVecpNn29yaItoq2jwUIAIExEkc8k1fDA4lEUMi9cCb3wzFizN5UUwmPoEefK2eUfOJvf-plLyg3xcFDMandJHce6f9plhzihXo5Al5h22D1V1K2jERue1vXvjXqI7qYVZ091wTdk_TzLlpd85BrctjHSKHoO9Vb-9ypdnwervMCq0xFhDjXgK-hjLUW6P6X46KK0d-AbyCFlxy8_uin60Jc8Fxbt-2okPXxlzG3az_0XqSuTbs2ZWTwl3FMMkPvwFaL29e8gKBzCwD9uRBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=rXwBdEQWx_oeXstAIb9Jn-KPTZ_5q9QnTGv7kbfbgXLcy7tX8mMLLBFNBtHnM05Q33RVecpNn29yaItoq2jwUIAIExEkc8k1fDA4lEUMi9cCb3wzFizN5UUwmPoEefK2eUfOJvf-plLyg3xcFDMandJHce6f9plhzihXo5Al5h22D1V1K2jERue1vXvjXqI7qYVZ091wTdk_TzLlpd85BrctjHSKHoO9Vb-9ypdnwervMCq0xFhDjXgK-hjLUW6P6X46KK0d-AbyCFlxy8_uin60Jc8Fxbt-2okPXxlzG3az_0XqSuTbs2ZWTwl3FMMkPvwFaL29e8gKBzCwD9uRBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادآوری :
در پی انتشار رسمی خبر کشته شدن خامنه‌ای، در شهرهای ایران جشن گرفته شد
و ویدئوهای بسیار زیادی از این جشن
و تجمع‌ها منتشر شد.
و به قول این مداح
«صداش عالم رو پر کرد»!
حکومت از همون موقع اینترنت رو بست.
تا الان جمهوری اسلامی بیش از ۴ میلیارد دلار به خاطر قطع اینترنت زیان کرده!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5082" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5081">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=MQhYgLgnsupuRfNO4YdoCiIcjZfjVODI9l_PaN4mE2cuNxyhgNZ3eN10dy7cgdmbnMalOwNe6TfEz2aRIQ-2U4sc_qKR6hPXprQoP5SQhyAYVfmJeEjpLuWXcltXIKlTK73ev6LWG-c4sW2fMD7TKRcvSfumnr4ceuELwGcQPCAsHx1ZWvqATvdJsalEdV3IEvUIBzm7EVr7RXLG83NT6tdJ3-Dv_EQV60Tualkct8xAlD0f9hbtmbUINQUjOgAK7inifzZFPEkESY27803DXg7doxEDXs2R3ommneFdsXf3i_QUElZrNUAt_s9mtrP_y0VhqYSGtWmEvv-5G0GkzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=MQhYgLgnsupuRfNO4YdoCiIcjZfjVODI9l_PaN4mE2cuNxyhgNZ3eN10dy7cgdmbnMalOwNe6TfEz2aRIQ-2U4sc_qKR6hPXprQoP5SQhyAYVfmJeEjpLuWXcltXIKlTK73ev6LWG-c4sW2fMD7TKRcvSfumnr4ceuELwGcQPCAsHx1ZWvqATvdJsalEdV3IEvUIBzm7EVr7RXLG83NT6tdJ3-Dv_EQV60Tualkct8xAlD0f9hbtmbUINQUjOgAK7inifzZFPEkESY27803DXg7doxEDXs2R3ommneFdsXf3i_QUElZrNUAt_s9mtrP_y0VhqYSGtWmEvv-5G0GkzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXzHsUMZ7B4_YCvutGbuLozQph4n9oLJkuTMVI4lKtCXzC3KCO4qg7J57TrY_R6yVB_MG-MnJ5Q8sOnV0Q7HusmsPsslJx5jtdWDHG4wzr3FeJkTlY5pbzgFUoJMGJ4QEDviqtTRtYTJeQhVK-0VUyozLiiawg8cTxYKX5eaQnbC3ZyY4-_s3ER8bx6YnRmEWLVqKCpos7y30W3Ab2NKRpdbvngBdfztlhzygr3x1C63r8luxjC9eBkSemgnDxQxK7a3hU_FSM0B4JxyRyBTL3v8-xpJ8VZ-buVS7oYRYzdc_vZadiCQC0dx2NImYwrXDFxaXAXBcpe2tTqvrL-3lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قاآنی، رئیس سپاه قدس: «دستاوردهای ناوگان صمود ادامه دارد؛ این ناوگان چهره واقعی تمدن غرب و رژیم صهیونیستی را آشکار کرد و فلسطین را دوباره به کانون توجه جهان بازگرداند. »
🔺
یادآوری اینکه جمهوری اسلامی چگونه از موضوع فلسطین ارتزاق میکنه و درست به خاطر همین ارتزاق از موضوع فلسطینه، که مانع هر گونه صلح و سازشی میشه.
جمهوری اسلامی با راه‌اندازی گروه‌های تروریستی و جنگجویی چون حماس و جنبش جهاد اسلامی و… هر چند سال یکبار جنگی راه می‌اندازه، که منجر به تمرکز جهان به موضوع فلسطین بشه و اینگونه برای مبارزه خود با آمریکا و اسرائیل اصطلاحا مشروعیت بخره.
وقتی نگاه جهان به این نقطه متمرکز میشه، پیشنهاد صلح و گفتگو مطرح میشه، که خب دست نشاندگان ج‌ا صلح و سازش را «خیانت» معرفی می‌کنند و تنها راه را آزادی همه فلسطین معرفی می‌کنند.
و اینگونه جمهوری اسلامی از عوامل اصلی تشدید این بحران و عدم پایان این درگیری است، چون از آن ارتزاق می‌کند!
اگر جنگ و دشمنی نباشید، «مقاومتی» هم نخواهد بود! محور مقاومتی هم نخواهد بود! جمهوری اسلامی دیگر حرف و روایتی برای ارائه به دنیا نخواهد داشت!  تبدیل به یک رژیم عادی میشه! و این عادی شدن چیزی نیست که نظام ایدئولوژیک جمهوری اسلامی بخواد.
اینگونه فلسطین درگیر و قربانی جنگ‌های بی‌پایان جمهوری اسلامی شده.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=P9WiERBJ_WdMCDkxw1lDUfQ4FK6oQK1uGudtQL2BM7OGvsNGFKLhLs8bePP3fh5vhRNyBlu9maKwFIXc7OzOVya66_NfWF1dkA18CBXrjdTs5jxXToVuShUqtkbf53rUvi5o8iuG7ZW5qDrdUI330BCJ7Ivs09n5t_hilI2S_LTSWWrlDxgQFZuUV9xypAufdkqldghcqwhEsFSYWP-LuDfSVEBtTEJvfF_l95Ne2_8AI5CDrNO3JBkk0rm1u8QssqAhvYk7-wr_b63SpXW6Xkv6RoCpEvD8GhiKuyDo5W4NgdBMy40MCwnUSrMQCM0RSueoH7rsSxql8pKs2fNmKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=P9WiERBJ_WdMCDkxw1lDUfQ4FK6oQK1uGudtQL2BM7OGvsNGFKLhLs8bePP3fh5vhRNyBlu9maKwFIXc7OzOVya66_NfWF1dkA18CBXrjdTs5jxXToVuShUqtkbf53rUvi5o8iuG7ZW5qDrdUI330BCJ7Ivs09n5t_hilI2S_LTSWWrlDxgQFZuUV9xypAufdkqldghcqwhEsFSYWP-LuDfSVEBtTEJvfF_l95Ne2_8AI5CDrNO3JBkk0rm1u8QssqAhvYk7-wr_b63SpXW6Xkv6RoCpEvD8GhiKuyDo5W4NgdBMy40MCwnUSrMQCM0RSueoH7rsSxql8pKs2fNmKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=N3R9Z5My-cu7ccvSniEk0SNdtIVbTFn-KM6LiAhlb8rMQ1s68pWO5nqWedQ40sovx1t5sHyf48Pbd210WJ1JRQMPk-aJqJENK8nX3uwv7Fgnh8ErBdxewjdfetbEPWMo_DHd_h5MCyM2Jn-nIxHSi-9voTed-bRsIFHRFgO_Hx7378IvotFNP4S2moBm0c2z_Lg0_1P_BRioMAaYGVBginZnHzUqA_YyV2ejZe0PmjBurPprotL3NxpYba4eH9ThpkRVYcsuqPSQ3bOxHMPX8tVwyXd9GdASsfQR6sur9uFhDO4AeTUOKmeJxDxjkXL8zqvT0-Ertp3pYdHp40tdBA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=N3R9Z5My-cu7ccvSniEk0SNdtIVbTFn-KM6LiAhlb8rMQ1s68pWO5nqWedQ40sovx1t5sHyf48Pbd210WJ1JRQMPk-aJqJENK8nX3uwv7Fgnh8ErBdxewjdfetbEPWMo_DHd_h5MCyM2Jn-nIxHSi-9voTed-bRsIFHRFgO_Hx7378IvotFNP4S2moBm0c2z_Lg0_1P_BRioMAaYGVBginZnHzUqA_YyV2ejZe0PmjBurPprotL3NxpYba4eH9ThpkRVYcsuqPSQ3bOxHMPX8tVwyXd9GdASsfQR6sur9uFhDO4AeTUOKmeJxDxjkXL8zqvT0-Ertp3pYdHp40tdBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5074" target="_blank">📅 19:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjfsRVco7BL7i0973rcDBMDUMdtai-qK1zLKapBbbCFiGBkdUPEXzgHz5QJB5NFR9eoTSR0e_WUjin0l3RklrYGyJyXfATEncMe-XB5XdOYebrGVKL-PDs3XRTqjHDaEvMonejHOKI5NXJXjMQrcKbrIUNIeKu5BHIKWzrzbM5B64ogKgqE55YKdIEUqjenzR_s4wa_BrRqW6hpX3hLBH-8IqY6CsWirf0KWLKrCuhSH-tx-xlLh0PLZlkKOmUb0lgVXoDEQOKEWrwcpS_XAYpPWs0X7XJhW94u961RdktvTY3ocwCw-o2-3nS6Rcez-uKEFPBn3SYMVLpBeHBh62Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5072" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIuPv9H1J-x819-MY8qKpRnynXic0K0Dq_XfCUpy3YBKbg8H1_0vFak2l0YwnuSsyr-oCBRjSOTcZVa6fTXtZ8SBPeiMw0-0JzMJdU6Pwrii8CgfTTY7QZu5bxyUTyoi_cDNU817LBU1mF64VR6D9KoOzZrA30IEn5-UJupFqqNOE8V5eMahYOZwVSCTrftoLGT15xH5A7kYmsIBeBatK-Tkyr6hzuys-ZIUlQpqTnkiW_KvjeHoa3710q2mwrYo9-pbJXRyb2waHPegqF85WHaAbyuxkIKAxF4NKkIaJX9xtkIqOFTxUMJFEhuX6mHoLzfRizMkRdog96KtIQQXuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_0OW9T5KyYkPnwqg5n83K960CPJdH9MnIKhewFax6Xk2fDfglmSjWmy4Fn8ClCu1opftZp4CFdWg13ihaV5wHoXaSVQ2fSk1QGnz1Q802SHaF5d0m-bRZogUqXTsoAPyXtL_sWG9p5r9kh1XBiOdFmQ3g6S97zywRLMevJ37CEXK9_FLpZHiSM9h-6yNu1y3nD0v2WnI873ma2HE6K46fISOahjqM7bqTC3HZBkZ93pKXFLqDpGRPK4brfbx5JMTq3Zc8rwP7vodArCtqZKdnC6qqEmEm8ploxdwh61AicItUmgGlbRaHkDJNnnA3vQZeHFbQbjdObv0Y3vQP8GGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماها تحمل کنید چون ما میخوایم
۴۰۰ کیلوگرم اورانیوم غنی سازی شده داشته باشیم و «استقلال» داشته باشیم ،
استقلال یعنی چی؟ یعنی هر جا خواستیم ده‌ها هزار نفر رو بکشیم و اینترنت قطع کنیم و…. انتخابات مهندسی شده زیر نظر مهندس جنتی با ۹۹ سال تجربه برگزار کنیم و
و بقیه کشورها هم در این امور دخالت نکنن!
بگیم مسائل داخلی خودمونه!
خودمون حلش میکنیم!
این یعنی عزت و استقلال!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5069" target="_blank">📅 10:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTaaAhl46xLSUrj-2FQZZiX0_HPNPgsS_Qhw12CEfR9G8aStI98LYEaon7qJ7Yh_H9ykfqcrNmPLbY1HUkgwkC-qXT9ljz-a0ygIuxp45hPdiW9QPFSsItr5X3KJeRGcq-XVEsC5ZAV8rdyidKlZld0PqqMjlXI2GNhGs1Bu3nT3lJthCLMY4B2dnyxy490EJ4bP_895lw0ybJMVcgTEKgpSiSgS7wj6FIc2b7RI1B7gK7x6aG5z6z_04Nk_hk8xgCf6ST_341FlAwVBOl6lAO7Sf97a-LANf6v3E1jFXfLCJ0iLdQ6TcXEVoU_W2B-3K5rx2DvCVKT98Cnw7GRRVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LaWMvOUC0HlA1I3xDLrkVCJ9Rr9G0T4kqADReKtlsOnF6jO29eMnaAVH0aHnehaPdn1Hv4SwDafp-FtgEjQQvGeb7qdGOX0Jt7UUdOsZZGf3iyPQJz4E3KVn-j8u0si2cOGe2n2KHNS3rr9ZzyXoMZeX7IAuuQzS5kV9_FwEYsP_l7VvnfkxW-hjwNFK8g1CHi0bNLFhknMS-rf-DvBNvVysnJWs2fP5fAsLGsU5ony4WzuELy9ArECQyStZQaJ75i2NShh3y0U-LSmwjyutvVjcPf-JrAwgQBy4arKgEMNKArMYWhkcFUn69gKV0ryoTYDxncuZqTYTLhgl5gUiSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nbmwZYUKckUc2Q3IPT0aLar5rB3mok1Ub8QydCOzz0Od1iubC_l2yOmDAcNkb0DDQXR9LfNzhwN_yaLFBn0tHClG4t5FvQu3pMoQpGq6nRtYNrkXnKhOioL3ATEnlSgLwm0M2MzfucoKev_gs5c-s7HqtkOdo3ft27jVDGhmQhUirbizVHLdu0r_JlKOMn2Mu7fdTcNiSM-Va3usD9wUkJfoh-Dj3v5Qj_AJu1ff8agGRg7E78pQSqtz0HuPJofJG6xywLfcfvjZRA_dDf05OY9MAI_wVnYMBJ8A-JCCWK2V_JvKgx1An114zHXgKUltUyVtMBNeH-eoFwzuiV0cvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DmcvbgzyiErROmeDKBVxohXqGWGy8epA3s-tjB5FWS3j9HXg04uB53pFqixy33EJGN8pl_gRbyAiNVo1MCjJzyLMUOuR2ucM_o193-pd8oIyanKN_qAt2BEz8KEGMd17xfg1rjcN20of_DRp1eYznb1OrbCHSic8jiqDPFEeyf9_ixEn9idKVMn4dsKRTbVIYnPlaDOs8Hm8MJBrHa7-nkIW7Qad8DBR2t8v1iFsNNXGFvltwHNZh2j3ous4MnCg6zX6CFcnzuyzoF2y8RDn76zImdV46YFp9tSe_fk4qHbs-R7D1tc62TPZ-xhnxJZwm_tYfDh_r3UCzzDnUKwvjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=BjPFvj8VFSFyXgmy9dWAkb5D2oVekdzGsr1q5tf8o4QopQp4csJqruKWhVQsbLML9aZCzQw3H5EGwS22hikLmXnJXzr809zYhRm9IrcGlc3uLr8PKydz_zYHdP9L6eUdfXz8afPWIN5PAzWiHzYpWAIU8zGOgECJ5mQoLCztoW80epNrEE3bmvmDcn8s1VMKOLcxglkDV1MM-xtTzBj9cnwZXSCiCujJmTX-H15bE5zKAlaeQKr1Vxm1ntbaAm_TJaKaitOZyLimPEaVE7GwPdGOtJM9p5Z0e7HgSsFHKOGSchQ2NecHfbfH39d7iUhw8FnZWbpfrQK2M0EgTgKANw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=BjPFvj8VFSFyXgmy9dWAkb5D2oVekdzGsr1q5tf8o4QopQp4csJqruKWhVQsbLML9aZCzQw3H5EGwS22hikLmXnJXzr809zYhRm9IrcGlc3uLr8PKydz_zYHdP9L6eUdfXz8afPWIN5PAzWiHzYpWAIU8zGOgECJ5mQoLCztoW80epNrEE3bmvmDcn8s1VMKOLcxglkDV1MM-xtTzBj9cnwZXSCiCujJmTX-H15bE5zKAlaeQKr1Vxm1ntbaAm_TJaKaitOZyLimPEaVE7GwPdGOtJM9p5Z0e7HgSsFHKOGSchQ2NecHfbfH39d7iUhw8FnZWbpfrQK2M0EgTgKANw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pstL_qh3mi8dmyag4gbN6ADWUQjm7hydDm7CliaT2IkNx77B5SQxG70QLqSEJmI15pZUn1bx2tkB3yMhunN8cKojCATr_jFHkLKD04lPG15hy_ch72Bm6hao51ElXxuLN-TMckINJBp91ieHtvnVdlXqCkjMJKQ5EaW6K5y4g_CTaHdPvv2hAuiMjJBFzUqXg_fSXyYDnMWIzbywyut7nEOBOJ-w9be6S96DmBhdHEmULuMlKchC83OR9wMtHeTuwa99_z1XxDjcreX8pYx4ENhZL2-_iZuO1GpnAN6p1o82yABWABj-rv81GQ2zlOh84J873BzK0Yg29mDVUFdpdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKjsOPB3x-hB15vFxcOudLzQZNnVWTT9X0IINBYgPBwsrXgp0FzsAXZjEk96-iokXYw9Jz4Jc1nm9qDsGs9Qmv24gKvPJ3PN0XSoWYiTUjMZe_piIptKko4Nda26r5NVS06AQlnaAhSZiQxTbuM-Pr9HhFBUySzhhBYLGkSo_Ivmysa28kgAS3X-6h4szeZRJb4ptKC6FV1-mOJRGgnfI4sZ_UcKVZRmKh4mNZXn6PBbqmaUCT2ym-EVJqa0nRvlfhugOBqnXttrB8JyOnB9cTuRuE5jTpnk98aWHglPaYDPv3ENC7U7IyaDhZ5cOfHRETrtMi52KFgEe4qbKB-wuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.
هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند کنترل کشور را به دست بگیرد.
این منابع همچنین ادعا کرده‌اند که اسرائیل، با اطلاع آمریکا، طرحی برای بازگرداندن احمدی‌نژاد به قدرت پس از تضعیف جمهوری اسلامی آماده کرده بود و این موضوع پیش‌تر به خود او نیز منتقل شده بود.
اما عملیات طبق برنامه پیش نرفت. احمدی‌نژاد در جریان حمله به‌طور اتفاقی زخمی شد. هدف اصلی حمله، یک پست امنیتی در ابتدای خیابان محل سکونت او بود؛ جایی که چند عضو سپاه، که گفته می‌شود عملاً او را تحت کنترل و محدودیت شدید قرار داده بودند، کشته شدند.
از زمان این حمله، احمدی‌نژاد دیگر در انظار عمومی دیده نشده و در حال حاضر، اطلاعی از محل حضور یا وضعیت دقیق او در دست نیست.
….
آدم قحطی بود؟ هیچ کس نبود اونهم احمدی‌نژاد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5061" target="_blank">📅 08:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5060">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ictn0JE9DhExs1mFQaiffY9bYccse0uzUKC-fyDbTsGFevDddyb1potyRUOZutbOpKxuX5gOVmxCj8EqxfPLUDEf7PxVxav9TiK-gicqUQRiJ3mD6jPeCItt1JvEHL7Lf7hPqaTl-wvXyOWxANj0raIstP9DTfVPZUhkB9fQwTtqsZZgeTE-0oUxnzq0AYqNHvMmseQBoRB3ZfLdXh3LNc9eTtccjSV4Hjz-zeJ51-3vFuf5fKeC4D9xn4oYqac0iDjpx0EBd9-zR7nJoyc84CcBCcThAH9Kaa2UGJMIk_87LRjrr5CVHi5R1vi5DtF5N9hqyEGG_wZd0edxTJ57DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqGGVwUQ6MLgc7BcelFxjJdgGey0nCPCM4CTBSJGGbLE7p_p2lJS7eWYUsauxnYqX3ZHQvDdIfF-Hq1GroTXDWa1Dku3nj7d28ahp877G9Q1vIYCAbR0DnWp5y_r94tOq7lmCjXwZXo2YMjPc_mo14HcCHCnsKc3XYVM-6gH7xaIjoc5c-M5PT9pjZzHz8YdfMc_Bn4lCrU4g0AEc3dHVOxOk3_ZMqa97U7qF9I4vSHjvKK5iFkbynRR8xaosd-ipOQkrcWhzfIcOPz4n7X2mX0dt05kCenUlqB2aH1Uxx5bt3Svo1VzaIR3qznlpi1ad9uJ5yg426bgcjtCfxqj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=MuSumjZ2uWUU1CJDRD_6pRjUq5w47MWK3ZVLdpIivabOKgzBKOmDxOvH4O3p29wh3MQiYIWZ5BLlGz2tz2dHyYv1CRywF9i_dsP4JOhcTNz44C1oB5N9Qc_eN_nQEQ2P77m-D2F5nwntH2jTMbhlaoLZxnBi0Ow8l7D9CFBa7s8pd0AVKpIN5ABgSNDPzWYMQImVVuJzsveaGHl5UtZna5tWG4GTZgLbVzS3hDq8HcakeRgkCRlF-Z3aubJi2ZO-BAc52vpuVmF2VFwKN9JrMrPtnssv14KTTzuMhAvBMuNBz5UyOTWrfCjscO4XY8nBG2cmJkHegFMVuKG1NO7iDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=MuSumjZ2uWUU1CJDRD_6pRjUq5w47MWK3ZVLdpIivabOKgzBKOmDxOvH4O3p29wh3MQiYIWZ5BLlGz2tz2dHyYv1CRywF9i_dsP4JOhcTNz44C1oB5N9Qc_eN_nQEQ2P77m-D2F5nwntH2jTMbhlaoLZxnBi0Ow8l7D9CFBa7s8pd0AVKpIN5ABgSNDPzWYMQImVVuJzsveaGHl5UtZna5tWG4GTZgLbVzS3hDq8HcakeRgkCRlF-Z3aubJi2ZO-BAc52vpuVmF2VFwKN9JrMrPtnssv14KTTzuMhAvBMuNBz5UyOTWrfCjscO4XY8nBG2cmJkHegFMVuKG1NO7iDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف و البته خود علی خامنه‌ای
گفته بودن : شهرک‌نشینان اسرائیل «شهروند عادی» و «غیر نظامی» نیستن!
حالا حکایت خودشونه!
که زیر دوشکا و خودروهای نظامی ویژه سرکوب مردم ایران، جشن و عروسی میگیرن!
اینها سلاح های مبارزه با آمریکا و اسرائیل
نبود و نیست! اینها سلاح و خودروی سرکوب
شهروندان معترض بود!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5054" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fu3Oqqi8Gyrk0932szDxLkfIfozU6a_ckFVo76D8CpuVa3wl_OauruqpevluYtsz3teI22k57EEx6WuxQO1TKYJyLQyGaMjJOczEHLXx4a-gl6-UwON4dJtN9Ac8EmxZfSsrCBEojHs2S7nYGEoueZMbwcB-PK-7vyWkeOTjmqpL3GyrP1geFOJ9Oe68LHkrUdDZ62xxrJiqoC8MHPM8CxXtt2iCZ7DYtpRQFcnv7Xrb9F1FsdJB_BR5ZGgt4_o-FOzaPQlTnJmZDdh6JrLDxD3Fx7ThwLuas1nBVIGzTtyHTK7AHokW1SyB2Nufo1pweLau50ah-DAvDcVlrIRUXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sj5CXhio4e-PrrYbTTZ6-mJXvI5f17ndfRfo_8ar_BteZiqQgeisCTwpyJGIzX3Kkri_FgKWeAd7NZVaG7b-ngjcOuS6s5GZFEdQqodpGKMoRQIHxcheT0MKvQRn-MBC8skP-V_XUzjF2GtANNdjiRFzCQgVVcOX1QjdwzFqC00v-6_dUA4q2W15kjTxOA3nec-KmZi2sP2_zij37fz1MioFKVOLYqQr39MPO-M_s2ytv0O1S64IN_h6QMHTqHfi42toLbfzRzD7CL4NS50tnOzmD5MkxFBG97czwNVl02kvVD2IM15ami5k2yMRdzbkdNIQenSUFuHPD6VTg6KaVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6c0LkbVd6_Hn8QlfyoJMEgkBnzSha20D2dga6efyBMtpqeQMHtItKFUGChWhszMSFXnugeL-bg7xj4Hh4bEV-ENTttxR74RUqm08i-I4wNm_ot969-Y3nxf5jI_NVGkJC1771jHOQRgB697ltdzMhT-M0NzlBU0Y9_i5ZkrFHl5nuC68xTw-7D8urykbAqV6oGVr1gdi4TsvRNfWZntWv00AspqZOqR5JcEUiOD5vH_KJ83iyTeQK78QaiV_Ig1mgctzGxi225L-1iMJc6TQMItsZg23b97vjYDzIOhqAL2WFu51_gjVrWNEtLrHVj74rNrbnrxzypf6NfTk5CaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUIVVL8QiC6HHe9UXb7rVoURUccztutu9fbGXb0RtLtv_OeMRI_fXroWNC4a4m5XA7TGn6Vzq9zKM0dsrxjNwQLpCMF1V0790T1qnpr2cfCsMu0NJ4ljEp5fm71F1PQIT2b_rWq3vzn_L5h6CEytStxc2FjYYzcAna_iMYlnotR5JfAvWsPwK43RbEZL4uibKPZYxrCGy0_y22-eMDwgbgSR8VcmQzUYGwVb195RVQ9sRjIXuN45ct0zx8_Syk3EYeZGZG4Xyi-jVEaXe3BpRXNSMOk-GfjWI0O7hgqniM_0fqS6CEgofiDT6iGIaUMsoClVnROXrnZJwTn-2PS-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2K7qCAhmbAe7U7vnuepp3057UdXp6vKoXtwiI3ZcFfsPcK-7--vogug4D3s4Yr1_AhGBGyiXv9qMzCFr5MPa2sgdd59qoPxlbQH5nJGMxHWLgcbCi-CE270jR9-TNDAkeI2gvVZ3OGhXIigYcaEQHT4qV7lG2rqMN6cjJF6UH3ukMlwQTgZKU2kDovVO18aXjZwk_X5q_tI74ITdkhUfs3gDBh7LxPhq8FQh39FWJossRbKX0wWYuirCxdYUF-lj-Urm5cgtp7JRo7QU58jXFpeKmOxcLv4D7vellrF8aNBdTSTt48egwEXMIMzkDSS34qeNo_NM_Xff261LBW0pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=OerzsISm9_7w9krVhnlrr9WUkx28MdxjuVcsDvPMbPA0236PlovxmPTHdMOuMlPXVTA47nt5m-iHnueQupI8IN7pXmk4unXpW5Nw1kPqX9LKC3kTU7RW5X_tH5UYi6QgRP4mF1FYHPtp1--DdLugwq0ydAQjkS-Z5CQQDbRNjRutSAhBZarUApgJ0rKP0eWfhcDjwCW_4Wvdx7IRT99rLGr7tQTq8lr34tNrgYgoeytvdoQnYwzxqg7JKX__B0NhV5BynK5W-QOP-TBArbQMZTqnvbiQFQB67XG1_anFiIke64Ir7VV7EQ8gjFjXrZ429pWClby4Jcp7NQQgIPU3Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=OerzsISm9_7w9krVhnlrr9WUkx28MdxjuVcsDvPMbPA0236PlovxmPTHdMOuMlPXVTA47nt5m-iHnueQupI8IN7pXmk4unXpW5Nw1kPqX9LKC3kTU7RW5X_tH5UYi6QgRP4mF1FYHPtp1--DdLugwq0ydAQjkS-Z5CQQDbRNjRutSAhBZarUApgJ0rKP0eWfhcDjwCW_4Wvdx7IRT99rLGr7tQTq8lr34tNrgYgoeytvdoQnYwzxqg7JKX__B0NhV5BynK5W-QOP-TBArbQMZTqnvbiQFQB67XG1_anFiIke64Ir7VV7EQ8gjFjXrZ429pWClby4Jcp7NQQgIPU3Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5046" target="_blank">📅 23:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ :  از طرف امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس امارات متحده عربی، محمد بن زاید آل نهیان، درخواست شده که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازیم.
آن‌ها اعلام کردند که مذاکرات جدی در حال انجام است و به نظر آن‌ها، به عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همه کشورهای خاورمیانه و فراتر از آن، بسیار قابل قبول خواهد بود.
این توافق مهم‌ترین بخشش این است که
ایران هرگز سلاح هسته‌ای نخواهد داشت!
با احترامی که برای این رهبران قائل هستم، به وزیر جنگ، پیت هگسث، رئیس ستاد مشترک ارتش، ژنرال دنیل کین، و نیروهای مسلح ایالات متحده دستور دادم که حمله برنامه‌ریزی‌شده فردا به ایران انجام نشود.
اما همزمان به آن‌ها دستور دادم که برای انجام یک حمله تمام‌عیار و گسترده به ایران، در هر لحظه‌ای که لازم باشد، کاملاً آماده باشند، در صورتی که توافقی قابل قبول حاصل نشود.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5045" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5044" target="_blank">📅 20:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=c50WkwKZIa-zp1PRa9puuHwF-Bt8sZMwS8oYwcXjrPeXuDnHTjvNd0YW4DzHqlNwxBoPDgn51RKxZHtJkDZW-mhW7Xe6z8X29mBV60ix2Khp_yNVmXtarB5ryZXVZBT7BZgEpPm-fLyeIyofhphHp3uO1amL2CIacm1WizlxRHdrjbt58EoPjB3h5ZAYQz1Kws2hIaW_0gxsA7I6zUgkx0i6IO5B2dgoc4luTjkQ_bXuPhiSqzNKVNlKW0XT22BR2InXjCdhntr3A09AgPEHUF2viY-1IwVR_gGQhuNdqrjJmuwrQWx1wc_JzRt0PWQ1hTZ1DJNPyEtPkBGStfHleA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=c50WkwKZIa-zp1PRa9puuHwF-Bt8sZMwS8oYwcXjrPeXuDnHTjvNd0YW4DzHqlNwxBoPDgn51RKxZHtJkDZW-mhW7Xe6z8X29mBV60ix2Khp_yNVmXtarB5ryZXVZBT7BZgEpPm-fLyeIyofhphHp3uO1amL2CIacm1WizlxRHdrjbt58EoPjB3h5ZAYQz1Kws2hIaW_0gxsA7I6zUgkx0i6IO5B2dgoc4luTjkQ_bXuPhiSqzNKVNlKW0XT22BR2InXjCdhntr3A09AgPEHUF2viY-1IwVR_gGQhuNdqrjJmuwrQWx1wc_JzRt0PWQ1hTZ1DJNPyEtPkBGStfHleA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‏رویترز: پاکستان [کشور میانجی‌گر میان ایران و آمریکا]  در چارچوب پیمان دفاعی، یک اسکادران جنگنده، ۸۰۰۰ نیرو و سامانه پدافند هوایی به عربستان سعودی اعزام کرده است!
سامانه پدافند هوایی برای مقابله با موشک‌های جمهوری اسلامی است لابد!
پیش از این
مصر هم یک اسکادران جنگنده و خلبان در امارات
مستقر کرده بود و به ایران هشدار داره بود.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5042" target="_blank">📅 16:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAGCkrj0by2VItyRapWl8OkD9_QeP6tYj2dZlkg9uTfHCM6hk3bZxjSnsfCQfdjZa-oiO5L4Wg7M71Rg2i0MuAk_qZG5JpQyp1W8D1RYEITu2B7W8yMfRn1ygYlW7xSPwHKzQ0EOSM2F1aF55U759Y2p3TkDxBQp2KYiY48Weya5oyn3C8IkSiOUSaJGCYVbJuui9BazXfFui2EmBUsrm1jZ3ELpjOUQBrH-6Bx2Fq9Im19ofrKAzqFcUoeQITKs46Z_ssGK6sPT4MVp8znvASA1kwMAlLYRkkCepC8kLiKchO6B2wAyxQ4SrHbXg_bec11S0mBlFDQmTTaHlXWS_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ud-vF2npwZ_sEHQubJRLFSDuSBQcSOS0gxb0IQkLdRpR2z4t0WQCJpdHn-CoRtF4nEKhb1LxElHa1I-NF2RParoqMBGWGVWUnxhYYXixN9w3dgFAelJhDNhat3iuWi-Ck5zh4urSs5HaUKMLvxvEs2Dayo2eO901M3GFDYG_Ct34_p59h52cwKaiFLPa_NmBMqMAMbmGarbYATq9GS4SoA0GoJLFXkEHryFdh07GGXBiBQz7faAZ93DDuccig4PLsk5pJ7KHl_SG-UrFTT7X7dNbaECc_VqcMZCFOcq7Toj8XuyuYob_NpM5OwPvVWQ2rJv5_SQSQAF-LVUO-ODjHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_5qGrVZ121SBg9tiice-ZqZitdTamCzSZvGah-0gpnXo3f7Jky7kWwfSrNNaZpPgGoCOXS1N2IGK25ISaIH3jPIvEBvb2DV_FDqXE8rGvL2l2psjqYZrzua5ltk6GRp0-P6wtKHqKSxDP_cRcke-gYToI8dwM-rX5GkdR2RMA4ppUbvyrxqIBsZT91n6lw7kCNDUVj4tYsG2ViHN8d8g7eMYJ5afSvwREFJrp18Sz2HdfJOjmCzsL35hqoLbPNyE9qixgiTOGcZWyLTC_jZrrOyWMadSi12zym0teYrVh-8pn0JT_gpQUkqZJd2SX_e4Apydc58bYhG1b7TB-DAhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jRXzqTuIRfI0sUhZjI1tdoF7n5AFhVq2pi7nQulkI8ZeDQVOFczxSFbqQWvuHC0zR1Dg7GBO41SbCKRLUjvBx2K58KvVKW-4l3Izao-Vh5jX3ZJq9-_NTN1sD91Tb-ZZymM7e6wpGWQFfGKj-1J1HX682u4mOm24cNXXzhK6vPYR-4_EFmIoTJBTHmUJxbqaZj0p6TDrJGMQfaqRJj0HnxVpqk_rcLHcm5re4x6o6Iwo6eUBU_DazIGwG0M9pLh_fpOhumqFMKuXfDPbq8JH5fRwHW_or98v_bn82jjoaJQZPADUTujI2TRcgQ4Nc0s362Hd3qQsQ5CWPo56R7YZIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی
۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!
توی ایستگاه مترو هم از زبان رویترز
نوشتن که قراره ۱۰۰ میلیارد دلار درآمد
داشته باشیم!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5036" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=fsy8S1poOqEy2DzYQZ7M3gcMORSobGTbYC97QQ4CCRo4-CjSmE3LKd1Qf_FFe8Xsqdb2i0du6p_9Yzkth1mY8AxkYLod4PW4wu2Ew-J7CfDy04cYlF_j1Ks5ZPrLeTBZBWIFrl0k5mNYDTn_JSjNeprBmUMrXLzA8ui5ga6UrnUabQN1bCafP-azUXlUsfdWM_q4jq3aS0VnYUAkC9FJHg3HfpXZ5srlCR6X8DESanGidqQr9GZVxsBz5qPM5HwFuV6A5sATTX6QoSxuzhsDNA1W9mMjv2HJl2ql5jw1xKb6bz4XTpFUAmALgqCPo0I1GXBc-MC4eFS1fqu7v95fkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=fsy8S1poOqEy2DzYQZ7M3gcMORSobGTbYC97QQ4CCRo4-CjSmE3LKd1Qf_FFe8Xsqdb2i0du6p_9Yzkth1mY8AxkYLod4PW4wu2Ew-J7CfDy04cYlF_j1Ks5ZPrLeTBZBWIFrl0k5mNYDTn_JSjNeprBmUMrXLzA8ui5ga6UrnUabQN1bCafP-azUXlUsfdWM_q4jq3aS0VnYUAkC9FJHg3HfpXZ5srlCR6X8DESanGidqQr9GZVxsBz5qPM5HwFuV6A5sATTX6QoSxuzhsDNA1W9mMjv2HJl2ql5jw1xKb6bz4XTpFUAmALgqCPo0I1GXBc-MC4eFS1fqu7v95fkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=UMZyXZpSHDZGnYbye9_7Ljfs237Oi5XvHcNu2aAxEqdbKWioBdGNSG7_MUOpJ5vjVciY0UDcHzH1aSHvpums3UVMLgUF8b1dVT4WqKjZ5903k-dqMeoKMBYm-zWqvcQhaT_B9g5zObWk6fB0C1UBEs5nAc9Ju3sbnxYzSZRrQgwlQ20jhAZVopEG9edchZvQqJvzRKo-O2dsn-bK_ibAwCxBx-0ePTIOVeGPtXSIsyNQYLpSYnTzztvjK3rFSxG2-0ekCPw1LEftRRsh0-oT9rJ4e7_zs-6WhUb1cd2UfXkA7PD5VP8R-05mACc6b1uiDipsSHT44u8mSxhpikSXmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=UMZyXZpSHDZGnYbye9_7Ljfs237Oi5XvHcNu2aAxEqdbKWioBdGNSG7_MUOpJ5vjVciY0UDcHzH1aSHvpums3UVMLgUF8b1dVT4WqKjZ5903k-dqMeoKMBYm-zWqvcQhaT_B9g5zObWk6fB0C1UBEs5nAc9Ju3sbnxYzSZRrQgwlQ20jhAZVopEG9edchZvQqJvzRKo-O2dsn-bK_ibAwCxBx-0ePTIOVeGPtXSIsyNQYLpSYnTzztvjK3rFSxG2-0ekCPw1LEftRRsh0-oT9rJ4e7_zs-6WhUb1cd2UfXkA7PD5VP8R-05mACc6b1uiDipsSHT44u8mSxhpikSXmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما :
آماده‌ترین برای حمله به ایران اسرائیله.
اسرائیل نه خسته شده، نه پشیمانه
نه به آتش‌بس مقیده ، نه کم آورده</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0RFAjwiKAoEdMYPjnfL9zZ7Wi-HRQJHHNdDqcJudOctnRWOU7CIAEqGZstCg2hNL9pTWd0dS2PnJ2iaXqBjNMd7UurPX0DB8lOM0KlMgQNTUfdvigMeaxwwTr35-cbH7Yk9q70L4s_rcftzDPWk1Oo86YJcb0bOyBjfGyg0wm2XO0X0B9Smkv1FjDyJPxnHg-uw8olRM0EWUE2YiK5BDEyz3IF4aedHKSax6k3h8J3gOQiy0ewXe28AGPbS6PsCliSQJ4zQ-IDym_P3iKTgrE7fglWcqDGMOVCk8Ee1wU_2SB6VUqW2pX4b4wji5gVXRzOfjFmk5vbSHLWrF83SeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrWG0k6QYNl8Kdf-eTkJQlNZo1JRyboRGcAVlT0m2aHZSzbmzjtWJwFon-UbWdAujBmvtj3oIY2cBBgatW8mDfQQuOktGEUL4UTvjkXv1wrFAnt70IqpPObSkwR8e2TzWMmSfWz8vOGJD_XUZccGTfRAiCYJq6ryMVCKd586GsdCgSagSFt0f40mv1e8SKT4l-Z3UaaSmqvArUyDBNqvbMjwXOj6vzzk7n8A6P18mcI-n7rHNolSkdfB37pNV863pbDQVt3Utl7w9v8SqnOTJgyqfzrITiEWB4ZkT5GvfJrtGN1G28fEEuLV2cCuklsGisfYeaWCL-rbb6EYSWkZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKGWSTPNa3SVqRrlCyaZzF2_Nh69NOrqg1Nvj6DM8N7PJdDG34EI8n39YjNl3L5qKFWmz0r1x--uTRMWIdApN40Rj-5RSuxrgMd0BzzXYKhykoPRmawtJs9l92EVVn_MHUkRhX-XiH1ZLbghZYakGoUa-O33G3OQlGP_X28WD5aTk-YwB7EsVru-wia81Nvn93EAOA0A9Ki8_2EwVpbU5mzGAiaNiqfrqu1-lVjruEVdI0XnOd45JDHe1HIo3xqMXE3E2BSWg-NOxIefjvJhRcPu93Fj6ggj14skyW9MH1YwvPJhwAH9wfm2dyhetTv2amnoG79xi45eMggh0JcKiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات سخنگوی کمیسیون امنیت ملی مجلس.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5029" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5028" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5027">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7lfdh1i4sLhSy1tzDGjF8QXM60D2naNAWqLI3ba84GmmNFlG-k26l37TD8US7UIesDp0Zc-DK_vqkmcun-m3WjfoK2HmF2nYGxFCxgLc1nQrv1qZ0Mee4DDWBQb-e5pKr9VAdYBvbaV-o9lJxWpaZsVxfKd7ad8u2GIOkjfR7AC9P7-gy0xlD4vSQRcS_-ZDRwq6tBb3Cix1UDK2_TcBlgZ7EiJiYn6RlwFDh8a6LnFZMraO4kKMTB4N-ZkM-JobjqvaEEHmlwRwaTN_hfcqdSLIl9anEYbAZLHhpRFxG97wIJ8iqa_KSMja9YvsRCdPgx_-YnqrovNz0ySFdnNag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟
در پایان جنگ ۸ ساله
۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و
شما «جام زهر» نوشیدید!
خود صدام حسین در سال ۱۹۹۰ به خاطر حمله به کویت این سرزمین‌ها رو آزاد کرد! خودش به اراده خودش! نه به زور شما! شماها که جام زهر رو نوشیده بودید و تموم شده بود! اصلا خمینی بازگشت این سرزمین‌ها رو ندید!
چون یکسال قبلش مرده بود!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5027" target="_blank">📅 23:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344237687c.mp4?token=jQqWqbAah7ON7nTOVvRnfppULkzGbO8GQ04u3nOyaPwJsZ2BGfZgvwUgbr71FFsj4g88uqfIUopBph3UvLsA1gPadZkxplMWuyWttDBjcfqtaMWuPiej17uycOsmN-IOH2Bpd83B_qkSvskpPDWSYa6N1GGlL8n3Ix51oOdWly1Aiw90Q9JUcS1ONT7vJ8WQfImsS1LJpL1-duVcjWNuCo-83LfckPInK7viHnf3p5TNwzQ1JErFIyCh-BZmkuvPKRLKwBXzh2E2mPpvE_1M-YC8BHhNHQ7E4Dd9ulIa4NTogZ-jkHNdcC_kJh0bshx9DJx2TnOBARX54wkwacIxvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344237687c.mp4?token=jQqWqbAah7ON7nTOVvRnfppULkzGbO8GQ04u3nOyaPwJsZ2BGfZgvwUgbr71FFsj4g88uqfIUopBph3UvLsA1gPadZkxplMWuyWttDBjcfqtaMWuPiej17uycOsmN-IOH2Bpd83B_qkSvskpPDWSYa6N1GGlL8n3Ix51oOdWly1Aiw90Q9JUcS1ONT7vJ8WQfImsS1LJpL1-duVcjWNuCo-83LfckPInK7viHnf3p5TNwzQ1JErFIyCh-BZmkuvPKRLKwBXzh2E2mPpvE_1M-YC8BHhNHQ7E4Dd9ulIa4NTogZ-jkHNdcC_kJh0bshx9DJx2TnOBARX54wkwacIxvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶۵۰۰ ایرانی رو به اتهام‌های ساختگی - که سنت همیشگی این نظامه - در سه ماه اخیر دستگیر کردن!
هر روز هم آشکار و در خفا اعدام میکنن.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MY9NtDpPWwv1wNObug5ezq_7AODyVt48fOfr7SuKx33Rsstqt2QyYhIk4i_0CqRdvk9XRO6PIfspfxd-SWdLYoYYqQsYymDhJ9s5r90OX25Xf3_P2pT8QoRrKINDbSzcaJWKvqYDHxfAwbwaddvBKXkhYC_Nv4Th_LggSHNGbppFEvnzmksUk5d7QPb5AlO3QCrVDR1q0GRWw829VS83wpr-5QwskGGeCiWJS8nGyrtE6liauN8aanVxMdD3iKKCxSrnXneW4ZT_IfXg_52Ycnkdz4L-aDkAYPJiNgYyUCIobpdrt38qEx_MotX60werKkSpbSnYGSniZ6R5uQLzOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدصالح جوکار، رییس کمیسیون امور داخلی مجلس : «در این مدت پیشنهاداتی از سوی آمریکا مطرح شده اما جمهوری اسلامی همچنان بر همان بندهای اولیه تاکید دارد. شروط ده‌گانه خامنه‌ای خط قرمز هر مذاکره‌ای است.»
🔺
ده شرط جمهوری اسلامی که میگن خط قرمز هستن:</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5025" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید شرایط جمهوری اسلامی را بپذیرد و تسلیم دیپلمات‌های ما شود یا تسلیم موشک‌های ما</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5024" target="_blank">📅 22:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏ترامپ به اکسیوس: من هنوز معتقدم که ایران خواهان توافق است و منتظر ارسال پیشنهاد به‌روز شده از سوی آنها هستم.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5023" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
ترامپ روز سه‌شنبه جلسه‌ای در «اتاق وضعیت» با تیم ارشد امنیتی - نظامی خود برگزار کند تا گزینه‌های اقدام نظامی علیه جمهوری اسلامی را بررسی کند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5022" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gz2JQc2I7UOTykhK1sejgB3SCbIro5d96X2IZ2GzcyeU1yngChZiebxcbS0ugJyzTOGU-GlBt7gN6yJpx29u2NzP7GEY7RdkUhJTpkRlQyYpMth9Lbd8_m07b9Ppk6WbGX1NMb8FvtE63d2mlGwoDDeKr0gBLyBnIQW1NMyfsGCBOrsQORSzrhaKYfty2ZF3mQGmCkha01oixdnvgyJtr_N0T9Ud9j7nYFuliZV1s0drSJAd7TCF7wJs8eVFmZUEqFtdPLT1bpfj066--aH9SMQ3MSl98nLV6JzrxJS0BYNLNftBR0mmtxQ7uaqXHn6XC3cKH3yA3sxO9KdC0Gb_ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=NybcyFudTqURDawB55KhDCLVrvKAhuZ-0tUoPfGLki9JyOCqsyCTMzLHUtY1Q3S1BHEpv-1TMZizxV1Drtuh9j3_A8FJ4IXNFd07IDiNMN0q4g_1pb8zvv1-IXffo9siJOpKrogKuyk8nWwufsu9TVuk7x6ElDTZHCFhLE0Ed9cPs3FIiAyOUuI-EXw62-Brwhx-T7uUE5M3xzhwrR_7VjxA2E1RzzCIt7ljJavzh2H8rjPK00Z0IS5ypny4NJiv6zhx_VghaN5wmrjcPClhT2Fo2B4s650HkJ8_MXyBmnE-v_PIiXPIIux6RkSjzaS3FTx7xUPx1VG4gVcjIQbCqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=NybcyFudTqURDawB55KhDCLVrvKAhuZ-0tUoPfGLki9JyOCqsyCTMzLHUtY1Q3S1BHEpv-1TMZizxV1Drtuh9j3_A8FJ4IXNFd07IDiNMN0q4g_1pb8zvv1-IXffo9siJOpKrogKuyk8nWwufsu9TVuk7x6ElDTZHCFhLE0Ed9cPs3FIiAyOUuI-EXw62-Brwhx-T7uUE5M3xzhwrR_7VjxA2E1RzzCIt7ljJavzh2H8rjPK00Z0IS5ypny4NJiv6zhx_VghaN5wmrjcPClhT2Fo2B4s650HkJ8_MXyBmnE-v_PIiXPIIux6RkSjzaS3FTx7xUPx1VG4gVcjIQbCqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5020" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ju_0HJzHZ-YsmU5qy2V_dCoNV2t0N8czeb23K23Q-AO-8r7iUC9lrU7nBK01QDoRBd-5AqiW09dMLo8lpMklC7M9-b78g9WXf3ZwReXeAHjrFN_opsjkMrHi4aQ39OwJi8h2Xj-725G6z8H-ZWKHwPdbw5vCBCiV3igxmB0393RFdE1y-AbqzarD_EFJzF_3YVRT4VWtOSBlujZKqR_pL7coYTxyotFCRe80ynt9BALBYszqtizKDXd0p-HRxqqIJ3NDOTjpa7BI-IRbyjD0ox3NbEwZhJuTKz4f9sQBvnzmFhqiX8Kb4BG12knHiV35Pkt-NColWohk1Ha1Vc1B8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5018" target="_blank">📅 15:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5017" target="_blank">📅 15:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !
‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا
‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا
‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای
‏۴️. عدم آزادسازی حتی ۲۵٪ از دارایی‌های بلوکه‌شده
‏۵️. توقف جنگ در همه جبهه‌ها [لبنان] فقط منوط به مذاکره است ‌‌دست یابی به توافق!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5016" target="_blank">📅 14:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b64429192.mp4?token=H9erJqCG9RykqvQ4RUbGxVfDGi8wEEsAy-oq1lFhEddNtGYh9vc3OG5wMCecKFzFO2KhJcmbbqDFdkk_La2G4TVSscsUD1wqVB7zydisXsTNyfFIYC-sMF8-zRwj9eGWxkP9GNYiIVATsuooaKjlFcB-7EOgesj4cHzdqN5OAYJdnagJ-vZMZfOmtDUDr0bEdwZkS57eIUTFYr7dfxGOeTspX4ewMHGIYdtmrXVJ_ju1Dvkj_o7wHOlqW6HjZawKSc3SVuMpUaZzGHzEHMN33Y8ZLSHDCVFytl9-PeV50ikF1Hib0aY1Ff_IvpnUOT5Rz-RPdRVVvS8jJPT_9YyvnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b64429192.mp4?token=H9erJqCG9RykqvQ4RUbGxVfDGi8wEEsAy-oq1lFhEddNtGYh9vc3OG5wMCecKFzFO2KhJcmbbqDFdkk_La2G4TVSscsUD1wqVB7zydisXsTNyfFIYC-sMF8-zRwj9eGWxkP9GNYiIVATsuooaKjlFcB-7EOgesj4cHzdqN5OAYJdnagJ-vZMZfOmtDUDr0bEdwZkS57eIUTFYr7dfxGOeTspX4ewMHGIYdtmrXVJ_ju1Dvkj_o7wHOlqW6HjZawKSc3SVuMpUaZzGHzEHMN33Y8ZLSHDCVFytl9-PeV50ikF1Hib0aY1Ff_IvpnUOT5Rz-RPdRVVvS8jJPT_9YyvnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشه عنبر خانم!
ولی روی این حرف‌هاتون بمونید
فردا که به خاطر ۴۰۰ کیلو اورانیوم
نیروگاه برق و پتروشیمی و پالایشگاه و… رو زد، نیایید بگیم ما مظلوم دو عالمیم و نیت اینها تجزیه خاک ایرانه و… !
اون وقت برو پوست پرتغال بخور و عنبر نسا دود کن .
تا می‌تونید از این ویدئوها پر کنید و یادآور بشید جنگی که بر ایران تحمیل کردید بر سر هوا و هوس‌های هسته‌ای تون بود و دشمنی‌تون با جهان!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5015" target="_blank">📅 10:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=SuCHwzrNPcCF7thryzmzq0oOJUEY1WkHfPGEujsDxbP67t5oZImJWdrE5dyXwNPhCIzoR2BhhlqEC-q0DXZpyHrH7XBVKkKBBDFiHzSREGdqX5UR8ecb8u9K7fCenkHQ_nFZhNxe5A-iOg9XCyfymPW6u5PvQle3IYJuJl7iGyud9-2g0tAtCvTeBAngzyMGA9h8N8jAVnDqM0pHdAmmuSrpZ5uQZpkGAlUftVc_blTXNy0qGMiiY3uHCUQRPyvJOxjZDDYqzE2hUtiZYWmQmzS5j7kOrvHTn3DhktK78FrO0Don6Ows5MK_i54pYjr2MWEH9auGiymAnkAAQGf6mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=SuCHwzrNPcCF7thryzmzq0oOJUEY1WkHfPGEujsDxbP67t5oZImJWdrE5dyXwNPhCIzoR2BhhlqEC-q0DXZpyHrH7XBVKkKBBDFiHzSREGdqX5UR8ecb8u9K7fCenkHQ_nFZhNxe5A-iOg9XCyfymPW6u5PvQle3IYJuJl7iGyud9-2g0tAtCvTeBAngzyMGA9h8N8jAVnDqM0pHdAmmuSrpZ5uQZpkGAlUftVc_blTXNy0qGMiiY3uHCUQRPyvJOxjZDDYqzE2hUtiZYWmQmzS5j7kOrvHTn3DhktK78FrO0Don6Ows5MK_i54pYjr2MWEH9auGiymAnkAAQGf6mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5014" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=jklT0txa0vcBJM_G45iXarL9PgyDxR7dUVEpMfbNfLoKZd5VlH16KpWok2TsjiNu2nCqTkTcbblI9rM2RPZalM9AX9VNdrx9otGSBJHw7nuvn-RI1hAXbKuZjN0zrZB-W84fOqd_YgRPamcVXlx2PQ0jUqnkIK2WGipKwwjX0Yek24QajyuN7pp-yKulryr6fEKFxPIZQje8vjNCbqV3d-yETFv46F4vIF1gvZ_WZUd5suVd_yUosmT8PcJGt-lEs0drDZJubmrcPtsteG-gCYzo7Be9emdXSQCvxPcIvQ8toaI_3nxw2i4P1J1FMxSFVU-xcT9ZYxdUjWNcErYjLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=jklT0txa0vcBJM_G45iXarL9PgyDxR7dUVEpMfbNfLoKZd5VlH16KpWok2TsjiNu2nCqTkTcbblI9rM2RPZalM9AX9VNdrx9otGSBJHw7nuvn-RI1hAXbKuZjN0zrZB-W84fOqd_YgRPamcVXlx2PQ0jUqnkIK2WGipKwwjX0Yek24QajyuN7pp-yKulryr6fEKFxPIZQje8vjNCbqV3d-yETFv46F4vIF1gvZ_WZUd5suVd_yUosmT8PcJGt-lEs0drDZJubmrcPtsteG-gCYzo7Be9emdXSQCvxPcIvQ8toaI_3nxw2i4P1J1FMxSFVU-xcT9ZYxdUjWNcErYjLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=SOgYzaJ4jpufANMHMItxZS0SgrmCmaQnPQXDcgsR42oDL0ILwrXu1LnFmZu_0PDk7N6dk0rVMKYLI5RSrhYloAJ2sU4236Vdee0eecAO8LR-pTzB4ITaYjyykdtTN9_ngFn6WVTswiVXOkZ3LhW1ynz4D9eipq9v_aAUQ1Ge68WGwnEWPOICiW7Oxp_prfLSx6HpDpQUuHT8YhjAAgM1SJfJlyryrLMsdL3-2klU35-tfEL7kmz8KwN1xxOcNF1MlokFdC1h0DTmAOnbbvBLOzBKDElY5gKPMP_wkDpobLqIawSZWXCruuVUC8Xw-qvY_dCUqAe1fwWoG-3TIxuLLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=SOgYzaJ4jpufANMHMItxZS0SgrmCmaQnPQXDcgsR42oDL0ILwrXu1LnFmZu_0PDk7N6dk0rVMKYLI5RSrhYloAJ2sU4236Vdee0eecAO8LR-pTzB4ITaYjyykdtTN9_ngFn6WVTswiVXOkZ3LhW1ynz4D9eipq9v_aAUQ1Ge68WGwnEWPOICiW7Oxp_prfLSx6HpDpQUuHT8YhjAAgM1SJfJlyryrLMsdL3-2klU35-tfEL7kmz8KwN1xxOcNF1MlokFdC1h0DTmAOnbbvBLOzBKDElY5gKPMP_wkDpobLqIawSZWXCruuVUC8Xw-qvY_dCUqAe1fwWoG-3TIxuLLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=aBPkeRAMY6ogmzATPcTryn6ibqZ_x4vip0hZ1oFY_jKoRWGn9UDFgODcbPcCqna4-6iuKYZtPkBCYoQgaGmgps4-F4iYRd1S025RuUrfQvrOlCfeaWIuME9cHNK73cMt0zVt3EvoVnSOUa_PiA165Iczsv1kEWu_soujDhwpN2lAkBbTOYYL49IDloR2IZJ75VKG-Mv0D34-BetSqn9af7u0fi2E2zSPQAk9JLBFVSH_U3kvympD2SEFCyYLDjFZtA0MGvoBU8KssqiziwG5z4lZFp1ezmlpqpvQEYJyVnvO1lPNpC8322TPFaSa11N74VSj4eM-T4ZGTonyxoyW3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=aBPkeRAMY6ogmzATPcTryn6ibqZ_x4vip0hZ1oFY_jKoRWGn9UDFgODcbPcCqna4-6iuKYZtPkBCYoQgaGmgps4-F4iYRd1S025RuUrfQvrOlCfeaWIuME9cHNK73cMt0zVt3EvoVnSOUa_PiA165Iczsv1kEWu_soujDhwpN2lAkBbTOYYL49IDloR2IZJ75VKG-Mv0D34-BetSqn9af7u0fi2E2zSPQAk9JLBFVSH_U3kvympD2SEFCyYLDjFZtA0MGvoBU8KssqiziwG5z4lZFp1ezmlpqpvQEYJyVnvO1lPNpC8322TPFaSa11N74VSj4eM-T4ZGTonyxoyW3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/emjUsj0Nr0HoJKSsTO_yq57AST5HSOm6kX-NDMzQ17fVgfLytqIgLQhckBlSHDdfGVriT_v09sTa-_nDf5SaZHjOAHoIu3zto8-1YMnh9OrKlGzCf4tOYFT3kX5Kge-O4EPH1xgIAP2Pd_Ap3Kmx8qhCslNFWj7pU25l-d-YiJfB55spumoSxUdSL7lO8_mX4dfO64tfpyUEN2xqihBTR5MdNrwUZ4mZSplO_dxmPxgPGTCUlWtlm4XYR5LNW1zgX5X974adN8fHd8tRXsQracHC3XdvS9n7yt9gT0FA-yEaiCEpNCGdGLl_S4zE6sJcvona83xtX2zIGht7aXGKUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FzDPTQlk21oDI9uNBvxlCgsBZGPh43_Kzz0nlKoHCh6h3k1vSqRg0tUMHxUwHF4mmbSUZCZgeILsuViPAErmta1ZFaHArMOPqU-Myc12HB3SiNT46PCXH1ZjvCTUX50S7R93ESLEbB3ZMcd-S_j6WTddOeP6XTUByWQMtTRyN7pOE_MOLTXoG7n7CAQbJksrdUKn0CJD2GEDRs4mowpR4VngZEIrRjrRqufAN9cqQ2skF1FMXLVvhFnCrtN0oAnh23lmeVBOzCaus9wYcm6mxLdZ2r6u8iHVJqQOChJx7A5_in1ED1Ll7rfahG8PRU2QFUEDapwulWBd7YP77Ai0rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دوستان بزرگوار، این صفحه به‌صورت مستقل اداره میشه و من تقریبا همه زمانم رو صرف انتشار و پیگیری اخبار میکنم.
اگر این محتوا برای شما ارزشمند است و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5008" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">در ابتدای این فایل صوتی که خبرگزاری فارس منتشر کرده، به نقل از
حداد عادل (پدر زن مجتبی خامنه‌ای)
نقل شده که فرزندان مجتبی خامنه‌ای در این ۷۷ روزه پدرشون رو ندیدن!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5007" target="_blank">📅 18:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMpYtQXpgiMZXrzEUpgynXWErVMowKdAeCzTfqy9nN9fQiLIi3AJKqOR8Nl93qAxZf2dBB4xFONjPfbLRqmISHzhQ1_qP5AfUpU3kv7CqJzxXtYwTJ6820Wqk3YofdxQ2PBimaSBZRrRgtsy4y-0kSs4EwtEMJgc-2_5Vmi-yJQORR5loaLV9dkiX0a03BnVvWaIhzEv1wR_EpLVooUXQJiPejbMIRBRyVVG1GdFRtZIPUKILUukRmVi4VA5aeNe0Bgu83UK8evzmTlQXnoTfYtumjjP36r9N3wq1T40D701mU52GRizZK5r3RVsnkDf1bFPlePmRVzgkQbaRbJjfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z5uUCIs_6h3HXmQKssP97410fXsfljktjgoVk1LUdPAtSQPWNtLuTLTs-wocPnf2-N61JsvmhW6DUL5sqUjljLxD--59NU6bSmsWfNiO6Vu6Mkv-oGhaUdJ-CkSXHI67af9aZBQY9pp6cWfTp2Jcb3C4caSy4ovBiV_KFwj9_g52s6auBBktAuQA19W8SFX9Q-rcuLOlDxsl6T8e5m7PtdUIqKq1nkxd5ZRt2ELeQzaWo1dwEVwUCknWIwLTEFZlr2Ub2qD9qBuDKO0fFNOy2m3wPBJukoxpceXuFMKPH3SjtZc56zThlVXB3LuUYJnuZ6neCjpLxF7ug5ag1b_9rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5005" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=JIFS0xN8oUJz4gHz171I-7O8FEPgOxj4nAsJyltLkQOIhdfgHNj3J5ro9QUVCIAQ1fXGn0HNSyEBMOZjoiOFnu8O8r6tLm-n8CDLU97rxJDEki0BFAJfVjRu6qHcJwzS8TvyDXqzpj42f2YxU-QtjPEFGARuI5L01ku0NI6riUGHYtR9LPI4G0Z4QQ-5rQhkGVE70dJWqzlqzXORmFnsoJv2Qi3Q9Tf95oKgbXiiVj1iWqBgVB6PUfPwTekLnW3a6vQa9uP_6Hqj0WpmiBy-QwTswQnuHVYYZm-I0Vdp4hHmV7KLRn4CIL2O4paTu9U1Br16YAznaiOkV1THKG_BKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=JIFS0xN8oUJz4gHz171I-7O8FEPgOxj4nAsJyltLkQOIhdfgHNj3J5ro9QUVCIAQ1fXGn0HNSyEBMOZjoiOFnu8O8r6tLm-n8CDLU97rxJDEki0BFAJfVjRu6qHcJwzS8TvyDXqzpj42f2YxU-QtjPEFGARuI5L01ku0NI6riUGHYtR9LPI4G0Z4QQ-5rQhkGVE70dJWqzlqzXORmFnsoJv2Qi3Q9Tf95oKgbXiiVj1iWqBgVB6PUfPwTekLnW3a6vQa9uP_6Hqj0WpmiBy-QwTswQnuHVYYZm-I0Vdp4hHmV7KLRn4CIL2O4paTu9U1Br16YAznaiOkV1THKG_BKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟
چرا خانواده ، چرا فرماندهان؟
چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته
لذا شرایط عادی در بیت بوده»
صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5004" target="_blank">📅 18:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پیام‌رسان‌های حکومتی «بله» و «روبیکا» دچار اخلال شدند و بعضا از دسترس خارج شدند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5003" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=OqMH6qaJJjCF66LcMWTTUBXBNd5M0C2ZyZOFgIsgvI2LjmNNkWX_T_45hDP-8K_5JG5TXbZ2kJu6FxZtL-ylOj94-IKi5E66zcWzAQAtu5nnISm57yByAH-ZqGTTOv-BwD1odfhKzKjI8GlByk0E5ob-OfoGE4XhiMgPGsSFQd_1iB4WnnyHTD8sa-dTSHqQRNxczx-qeF9dCiO8m5rApnuZnrVLNm4UQc50Teico9TlhFLguH5THwQzNOmQATl4_ejKeYnBBclzvTnWKLTgs8jQwCZoVv0_GEyy0AvxoRt2gmWUH5KsVIZHjP2pTBON_VPm7UFFlD6R0d7glh-U7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=OqMH6qaJJjCF66LcMWTTUBXBNd5M0C2ZyZOFgIsgvI2LjmNNkWX_T_45hDP-8K_5JG5TXbZ2kJu6FxZtL-ylOj94-IKi5E66zcWzAQAtu5nnISm57yByAH-ZqGTTOv-BwD1odfhKzKjI8GlByk0E5ob-OfoGE4XhiMgPGsSFQd_1iB4WnnyHTD8sa-dTSHqQRNxczx-qeF9dCiO8m5rApnuZnrVLNm4UQc50Teico9TlhFLguH5THwQzNOmQATl4_ejKeYnBBclzvTnWKLTgs8jQwCZoVv0_GEyy0AvxoRt2gmWUH5KsVIZHjP2pTBON_VPm7UFFlD6R0d7glh-U7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
