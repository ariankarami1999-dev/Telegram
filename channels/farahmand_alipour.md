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
<img src="https://cdn4.telesco.pe/file/QpzIRx6W7kpfbSUkGfBpe9d8FAl2Zx1zv4ndjG-oQ77b7khfY79b3-oZGHJCl4PtGS_pz3XEW6Xtsp5GL4IPszB5B5XQWesp0AVVZnNoP4AybYabeEVKCr0Eq93PV56raYJh4Uitk5zbwf8iNhygMSIrW_V1QmhczYiox0QOBzsxv45NAqQa9M3f5fjyOrjjTf3U9JWdLGKf6ZLpOJvGkODfNLv2nKKTPyAqkNFu9Br8hgyc1aMyKaiGE9Ft_gMm8m0mbcF7H8BQyWveiOlYd4NZQ2RoTAFL__E6ICO9MTeQLF-Mc5WtUzM2VZvi-Q-DECC0xw_Tilfo5NUa5KIK7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 19:15:28</div>
<hr>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/farahmand_alipour/5112" target="_blank">📅 18:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5111">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqulMgxIz7Tec-0X5fZKvxfFuusRIXVzJwt6qEXXJLtnPTQvt7lkGh2DEQ2W1JwBnAQ-O6k6sWDMCclZ5dyeJhCFJ7WPvvByS2309uO_GOx7a3hEO09N7g7szGsTism8D_awWUpF0NMp_nmVeusKjqxXPf-T3gHdyeUVRKas1BIfMt-NL9tzRHmaLIG0B7F4EA98uFsD_xFYwxCHgNNntaJMCxOn8B3OSq3UuEtbOG_fwvmP5-AjZ_e2OroMqz_CVws59Njl83cqifW-AH4O-7c_YWaqVkdSrxIg5NoVZ4dQ6KlYac3bic5a6A_4775i4wbZK8gZkrRHMlGLsN4rmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم! از چهره‌های معروف چپ  در دانشگاه تهران! در تظاهرات حکومتی شرکت میکنه!   بدون توجه به اینکه جمهوری اسلامی طرف  دو‌شب دست به یک قتل عام هولناک زد!  پس چرا کنار جمهوری اسلامی است؟  چون جمهوری اسلامی ضد آمریکاست!  از اسرائیل هم فقط به این دلیل بدشون…</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/farahmand_alipour/5111" target="_blank">📅 18:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NODy6g42jK7Aouw0EDSkv7z5g6loY-zndARer1KBAdZZ9fh-h2vahLeVJkGF6YevRqirrTpE6OPTxjG6Q9RZ8heU78zuK2G78cYwuPv5g7y6sqpOEAvBzU_FKG-noWf303CRGgmwhCVYjRoE3ipwMiEkThXENd8kLr4cs_tVTulLO6WXni2cQb-xx_CfVSKgjCnP3cuyyszOBIxJX8H-11hHd4zGvjeuYzltaq4g9pigw0_kUrHCA2qYb7JM4-PpTK2u04TzRBQwCY6lFvMgLpDRPSpQWgSBX_dCy-8eDN7b52lsFbE3uCkz8PkL3VwqmiGeFRmcNr79Xajhcm-0NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این افراد، از همون روز نخست حتی قبل از وقوع انقلاب ۵۷ در آرزوی  تبدیل ایران به یک «ویتنام دیگر» بودند، یک سرزمین دیگر برای مبارزه با آمریکا!  بسیاری از سران و اعضای بلند پایه چپ و…..  توسط جمهوری اسلامی کشته شد،  اما این به چشم خیلی از چپگرایان مهم نیست! چون…</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/farahmand_alipour/5110" target="_blank">📅 18:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUwgL-98ls8W4FfDYdSYaR_TjhymtpJRX9uXIH6gQHdOiVF2Pl-G9ll9IASITg7qV99WJ-4KWcunvv9fdx6ckXIy8hLhEiX5M6j-dgE-Ot4yEWOCQCm9rmhoWz97mn1-xWlIV4q5t5xB_otBhHvyF4reHR0-ENpjLCi-05ECOhkfOyDoJrnJmUckkYPKM3aeElbThcaBKZjFH8-m2MUlc5gGrYyq1rnhWpO5x02Z1jE9__J8BRXrmau7nh-Ea8Jyc0vnGxIWFBGZEGFDAsDAl1wgDrlzrRefup3xgX-c2KqwsCqJLD6yDsrMxIfsVccosJdXs2Pb8YgReSqdU8IYJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلال آل احمد، در سال ۱۳۴۱ کتابی منتشر کرد به نام «غرب زدگی» که تاثیرات بسیار زیادی روی نسلی از ایرانیان گذاشت!  جلال آل احمد با اینکه خود مقید دین و مذهب نبود،  اما فقط به علت دشمنی با غرب  در این کتاب می‌نویسه :« مسجد و محراب و حوزه، از آخرین سنگرهای استقلال…</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farahmand_alipour/5109" target="_blank">📅 18:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW-mgaeDBCVy0iK6psiMs5FL4oynpiogUK4spA3EjS2db0VYKDwXz0rDEhpY1Rb1yizumrgE7lIssuJnQfR3lbBFefBDa7nO2-Sm6394m8xBOh2PF-BMnzZXXa2uw27pUvY8PdFyvaYzjs8xhO5Hif6_WfbN14wR5vDB9rSbocuYRHWswlyVzWIH3o2S-rHHS19dXBAdrCmFavP6KbLBw2ExI6W2AzVldQhLXzxTnNqXksYVa10gRhDbnPvMNDm7t7hX8uZRsBKjDyvZbCMbpyzkz0zvr9QTf8M5dx5gAX5UJuhvdp-1YowDa7YcIsMyWkOo2R66ikXxLSQhlbhBjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،  یا به اصطلاح روشنفکران و…..  تا این اندازه در آغوش آخوند هستند و مدافع آخوند!  «ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.  اینها ایران رو سنگری میخوان برای مبارزه با غرب و با اسرائیل…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/farahmand_alipour/5108" target="_blank">📅 18:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNJk4sEEJHlVDnxY9yrY2SWSNFQa3-b41kbSw__xroP2c62XuV65rP2Sn0rKthW8naQUCcIqz79aYe73mf_4wvUwq3xqpp7WgGRf2rs-F71C7S-WPAzy835VqzE1TlzDC03i_Q_ps21leAqLY_4p4SxumcSgFWVEg_MF4Vc3j-04ls8d2g1IR4Oda7UfFJktnu89Tak2jyWlrtQJV0a8j3lWgdPf_wyK3ANzRc5Uf0dW6ltTWmoWo5DQbZs4sqiEtNvh8ZBUl4PV2HWnLHGAB8az8fpMNicEKiz8sxFzU4jVhwFlK68MYR2AMdkwGyZZMfO-d_xHN3bXMJ0Iyn3VDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سوال زیاد پیش میاد که چرا مثلا چپ‌ها،
یا به اصطلاح روشنفکران و…..
تا این اندازه در آغوش آخوند هستند
و مدافع آخوند!
«ضدیت با غرب»! غرب‌ستیزی! اسرائیل‌ ستیزی، باعث میشه که اینها به آخوند وصل بشن.
اینها ایران رو سنگری میخوان
برای مبارزه با غرب و با اسرائیل و با آمریکا.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farahmand_alipour/5107" target="_blank">📅 18:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farahmand_alipour/5106" target="_blank">📅 18:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d143286b29.mp4?token=BKxOtK_zsX-kQh4eqCbc4r9ILoH6o-XgHP-ulylKw1P4GaD-RyUFPM_vYzl4dTKxM-QCGLJIKqwnyY8em5XfXXRgqs6irtJPbf2htWVBmY9y4g_Zy9RW0Em4ejjFJS4Ds7LqLCqEsITJtgHpph3xn7ioltBfETshW-J23akSCK16_BkGHYj9CM2siD5O387EBZoqXMk-CY4n3cpijJADztA_79DEHm-TATquyuVHVfuxxRsc4ev13i7cIh2lf-NdJKzYrGJFgE1lsWZ4Z1cjZQJza9KSzV1YiF-l6-mfOcadFh7bLOX7XHfF1lV7qIhOvQhmpHuadAubomj5PbGxng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d143286b29.mp4?token=BKxOtK_zsX-kQh4eqCbc4r9ILoH6o-XgHP-ulylKw1P4GaD-RyUFPM_vYzl4dTKxM-QCGLJIKqwnyY8em5XfXXRgqs6irtJPbf2htWVBmY9y4g_Zy9RW0Em4ejjFJS4Ds7LqLCqEsITJtgHpph3xn7ioltBfETshW-J23akSCK16_BkGHYj9CM2siD5O387EBZoqXMk-CY4n3cpijJADztA_79DEHm-TATquyuVHVfuxxRsc4ev13i7cIh2lf-NdJKzYrGJFgE1lsWZ4Z1cjZQJza9KSzV1YiF-l6-mfOcadFh7bLOX7XHfF1lV7qIhOvQhmpHuadAubomj5PbGxng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیسی، همون فردی است که منتظری در دهه ۶۰ به خاطر اعدام پنهانی هزاران زندانی به او گفت : «نام‌تان در تاریخ به عنوان جنایت‌کار ثبت خواهد شد.»  در دیماه  ۱۴۰۴ نه منتظری بود و نه رئیسی، اما خامنه‌ای و لاریجانی بودند و دست به بزرگ‌ترین قتل‌عام ایرانیان زدند!  …</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farahmand_alipour/5105" target="_blank">📅 17:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farahmand_alipour/5104" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euXzC1q5uoTSmUv5AF95LHdDfC2t8m95eFYAVVMw8uS2nBycBeG8JWBnNU2qu_my2dOwdTbXbZxcfE1EWithS--OCwoGBCRVMddfQAn31hUiKByqZA3Y6gGBHVQomeKGn7ni7Hjdn5zov1fSKK8kKw1rxhsCwNutR69gFuTdhcNWpJRTB8jI6xLC01VYhxhyDAO8LSRvPBqOwKyXMTogLnh-iRIKRvIHTx3ShgrtC9BTAQwuANNYNIhFYCaMNIhytAx6Jz446SZI_6qPqICfo8_IFmuwBQgioCuNOLgC_Ty1M9oRxOoh0Riz_xMFAfK6rA_-jAPmv0Fjv6c9HYRJAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دست خدا عیان شد» و این صوبتا</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farahmand_alipour/5103" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مارکو روبیو: پیشرفت جزئی‌ای در مذاکرات با ایران حاصل شده، کمی حرکت رو به جلو وجود داشته.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5102" target="_blank">📅 13:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)  فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/5101" target="_blank">📅 13:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5100">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeHsoWlsjBaCxS0Zb9CT2iJcjdHUJaT8WLZMuBPFHbV1XA-GIKypcmIhuEMgPmIPTq0rzIowHna2JtPEt3zG9C9tuQsxy3k6BFmAcwbREUJhhV_NrzJw2-XTwOjr28D5tc971A1tKF-uv7mOdJGUsXtl6jj0xOi6BCCurr5gEOjjh2oy2-LMzDLnxDpHiJRC-HHbBtHFru5R2WWVkm3Uw3e018iC-vH2r7FqJdbk0NW218amFuWbgjo4HpkU-TS_C_WCaNawCoB_7m8H66Zu53oUnPwUMgCl1exIhiprbz8w2KbG3FqiVp5xqMh2X0QTPuFYxNEwnLigKrlwPxWHHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5100" target="_blank">📅 12:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDY9fhlzeqbIqjc8bW5cIJ7mU6dfLgpTJDcZNqZWMWImWFVJ6GV0A4Bg0XEA4IXYA8BSR8KKR7IrkqskKaIMtTsvN8eDJMb4TnecWqFymTHXBkNNTyCpEBuVCi2gNd-XNAAcD0MRm2NN05fixJQ7tI-6stDURnNd-CPIaMggOyjv5_1ou1frg4pBuoJU-DNkwG_EORn5kf4TPOQWE195GSlmFrngfOIS2h_gSetnHUXoGNCC2hn8qoNDCLdhPnTUnMIfXGstonoqypvJ59Sfsj538Jrf2JX6oFjwxMzqvbJC_IfUcrEau6ybdVADK3DrC_cVD8rohBhNl1UOwzyORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سخنگوی کمیسیون امنیت ملی مجلس! (مجلسی که ۸۰ روزه تعطیلش کردن!)
فریبه آقا! فریب!  موشک بفرستید!</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5099" target="_blank">📅 12:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رویترز به نقل از یک منبع پاکستانی:
نگرانی وجود دارد که صبر ترامپ رو به اتمام است، اما ما در حال تسریع سرعت انتقال پیام‌ها بین دو طرف هستیم.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5098" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5097" target="_blank">📅 10:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قرار بود امشب و در ادامه تلاش‌های پاکستان برای میانجی‌گری میان جمهوری اسلامی و آمریکا، عاصم منیر، فرمانده ارتش پاکستان به تهران برود که ظاهرا این سفر لغو شده.
رسانه‌های پاکستانی هنوز چیزی نگفتن. اما العربیه، خبر لغو سفر رو منتشر کرد.
عاصم روابط بسیار نزدیک و ویژه‌ای با ترامپ داره و غیر از این، کشور پاکستان نیاز بسیار شدیدی به پایان تخاصم در منطقه دارد، به خاطر اقتصاد آسیب دیده‌اش و…
اما به نظر می‌رسد که عاصم منیر به این دلیل سفر خود را لغو کرده که چشم اندازی از موفقیت و دستاورد، برای سفر خود نمی‌بیند.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5096" target="_blank">📅 00:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E29o9no41s3aKqD4rRe8-p4Zx6P2ShOKUtbjeh5T-pglQhneK1X3UF02vfLJnpOi1ZmrrOB6I2f5BWyZ3qIw15taIA03kmdXlqsyhq48-XIIf6zq6JgxTAuhFf4XV7wqgI_sSN81S9zGkzx0vMLh6BB0YjH8BKoGzmGB13JuVyHe6HjxVjjeLUSwwTt_Jpp8EX63Ij1cslG5Zeu_ISGmZomr9h8EpEfVEjXnUTYPYtNmkeCuQHKowjs_T3SGmFjwZYIujXvMwCC4y0e7qxnb5DLf09AgH8IkYajwllVTZV-77OX4TM-5gqh_swtmhim7t41z33-b2gToIFrLWVkaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5095" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OC4GxLukLytdnRYhqriDygh2eZGGTnBOvkUD-YcvFLI9RcsQ6SZ56rCI-JUKBoCZ5U0liPXmeCLVY9N6lQgL9gN1kgOdYfI0XtLwMHkN-oO6BqoaUuR1mp_wIhTgvbEsnc4__-19_mrPMqzWYVA1lEevbYznq4j2BXHMi4C8Bu9uMnORuZ9R81gBB54sONhSQh8wbfFITVP8NDSGRkZIumzV9SvQZ8PKdoSHacPBpbF9cm64zXDbLNkDuKrLkxAt4fFquhSec-ZRHPbDwX4dPfzptyvR8Ros0sHRvW27xWud1QRcduoDCfXaa8fl4uIY4uLpLOGOTo8B8ks0nF5geQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5094" target="_blank">📅 00:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COa_DSpBnwP3Oes85QVPsMo3KtRfciq14s2uMiU5ZsUF8j_9Q8U6zSuT7rbu9krRrx1K2kR0kf6i_kT_xskdHduQ_6a5U6f_W9JytZxe6WnT57AC8oxpwGYcO2IDp4CRYgHvav46bavNn326zHjZv8TnsCwLLzQRQgJMEPUSq9SpnHByWSfVUybrcDj-h6IdXLVZ1ftYwpJk4_8CmFtwiRzAeEZKAXubMVcUJZRbdZwItR4g--KPKObZS9a_659uXb3cgWI6D73KHB2Xl9hUUuDVtF307I-s5ptYJlgm50ddqCEsI7kx5AzsFAky-WTro7IYDNK4X62YWNrVNnm_pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5092" target="_blank">📅 21:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3NsPUbdrLJqzw0v9b5gQPrAEVXTCYX2WARHi6xepxBx7vOlxbOT4tgKfoBIaCcZfP6roIipr1Uj8VhDubXyAE6BNJ6WXciqnRdWIxgQnaXEiyPzA9wVqTCHP1tnHASs391r8ON-CYsptq90G4oRNBDq65IvHkkQq5iB8WqvI3uOZ4sYZQ9kSp69IEhjZnmEmmtEGLDVQM-cby8JU_egCe4BMQnWOu8Dore4PoUifNF1mnvA_AK36nSOZhTHq2Dh4uzUj6PODsETdw1tGUQFg3pBn9pVF_PkQd9l4lZjYyPkGtMSnXu7OSnwi_12F9wI2BKALRwZoN0rTCvsxiBZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر بار مطلبی منتشر میشه که نشون میده
گزارش نیویورک تایمز چقدر بیراه بوده و بی‌پایه</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5091" target="_blank">📅 19:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ez4sFC-qYN3nZf7--oU6_euP2kZmhUpUBAoYwVFEBBvbd24LJW0A6ctDe5TrgQeQah3oUg4F-hXLyVeT1SZ5LsQTpXaaQaPpA2uBu0C95AkdjV77U3P-L9bp0RCOO2-FbWPIkATw4sj37xsb-auRdhQwFe-lXA73zNxXGb9NI9ueAIYXLWURX3nHUiOOc3XgQHDgOSnBwgTl6Q0BkPZv4nH8-q6lbXgJWx043MEvw0krnLxcO0x4nEdeGqWXZdE5naIUwgRDyjrIFkUAYJGtGeLjyK6YzJ_ENcKTRgwg3duy0Gti0X1kWlHDjpmifoazTY9x0xApmDXhrszH-VTU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی رسما بخشی از سواحل عمان و امارات رو هم تحت حاکمیت نظامی خودش ترسیم کرده.
از اهداف اصلی این طرح و نقشه شهر
«فجیره» اماراته که برای امارات راه تنفس و عبور از تنگه است.
تنگه هرمز، تنگه احد شما خواهد شد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5090" target="_blank">📅 13:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ej_7Cjz9PU9oY6nkhsgxdwMZbHtLfzs05JTAanIKt1RsCzYa_ElgtLFAXj4SrkMogtbuQXiUxRiwXJo4xIi-LsNZZtkn7fpZtikV7byNhheOxOWg_dravqeaa7JkkJuOl0GUf1ZX-YAWhLtuM5J8pv341yZknJJK93AfSDUsVXvNyI2t_k_3idJc0bXg7UjC8jbeKi1Q07HSVC5ZZEb_pE1TzfnI9MxLRUS-_m0begQQUoA-kdTxvCvSt-LeThqGT6gd_-lsWKBWacYSSgbV69dkojkM9Ckr76XL-Qm4uouNaCNsY-WUFJS5v-VJAIX5L_PV2LONimy9rMngszb9bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XL_sg6kSG8cEPjr5gEyKUhq5ORFlax7nG5r0I1PQJ0RbtdwNyk3Q4JExnl0ksUhHGaWxgqzklEea3hJolXuKWT1nsDiv5zvJyHJ-LVuMTduI0fxB8ioCYIqNKqUKVdevWZwBAb_7q0xE8tx5k8n4sT7MnZQrdh2ieyFdfdil9aMbpw4YIzrkBuksw0JPfiOxhGdUTS4HnmGPbioVOhnKfaV3Ln5CsSbc0YCZYraEMb1AJlXyC0cncayYnlHPChuCTR3OhXPv_0c4tnOmc2woo4XsoHVe2I8arL7p69k7HQazvlt0FrQfnbfnkwaEL3CTDgp0Qkdkdh1ljnDLGukDdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPH3zqNiDzrVSiNWya6T24cFXwSwc3CeLkK2zeWkU_eIlQhwrvDJYfr4mMbEJEM8VJzljH90leNqOf6xpzvSiYeaVL3Kj4RS4CK3Nw4Lm5lQR15EinqKyU4XScYnY04Oah9n9IOFq72evTZsg5CrZVDUUZXG0FKvz9capUNlc7XKpNzMkHu5KyN6KZdpDF_Ju_7UTgL9xCCYtikeixs7JFB0CWAt0JutCXW3OdpIerQcfEGMATfxUZoK98YUIot0-VId3HzWo8M9OY7PhLfTPCQV4oPhCAU-vgu8rVG-BhWyxsAG5e0i32txb3WQnjUra4ZPjX8qV3uBl_09ULzZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qrf3fiyXRAJzLYZXB3JlpM-gsJHwvMh8JJY-71coaC4H1TGV7R4ZNtwYfg7YiN1jpRW4YhlBFt6cwatn5nRV5e-t7t1M51EVGGEb605Mm1V9cCGN_GpYSLAgQNlgF-D_atvkPnOwrjHMcVBjTltl7-Or5dp4v-aNGEqNocQ2SsQ_TQtcHWokyhFr-2XYsqEKa7MoPNPSumLIJ9C_uSULcfh-4EB6ef1EcKiD84-SfY2r128Lm2hB9Zeoe_GcU18BVe5luG5vlXDDFJjeesREoBmzQZoqINFwuKHwMUTX1Jw9EUeVFMaKZh3gww_kQddd2kdfNl4JNEU6nPcROOL7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyRX_HzEaNuVSvuqvelCY-Y_RncpqDf5jJjzQHImyo38gbe8nzqYXfLGW5LSJOJ1NY_tnkav3uV__1L8K8I937q_3CWODfxDMpraU-QLMGr5alHlI49FbxZ2bKiDXr5qswUYnWzTok2b5J7gH74TPPy2vBwM-hq65TmQabPBCRjEOSjQVLGu72BPGk0PdtQ5uHVAlO9Wbzko8944Y2m4fuaz7c_aPWNrbt3yyg-bj7fhdWsUopwpETx0Wk9ON211EgVYN0PdlQbq8mARuQnAWC7XAxzRU-e_slIvj2Qh406ZICXBVCTtqINktUiYN7YtnNvLSwBcLykREqaHksh-EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5085" target="_blank">📅 12:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5YZO4QWyBmwIx1OBwr6MZYNttEbn3fxR2WMYSfJUm8NWzg7GboVt087ULL5Mqlo7dxFm_2OoF54SOenJyeSY1cQ5HysiPPjrHdHzuzFmDS82yJKIDPwvESJhZ9rgGXTDPff5z91JWWvaz8Y9WJDTJhgr7lMNHhnmy4wWzycYpP9qihkOUGdZbgKXJ0r6-2XLWYkNAECVa63-JwOOQhdhzxkuzZ_MB_DXb7sWk9PUsCZhyt-kiXr7Zmf6T8nEKobgWuVrE76p4G_Z7M32Qcfm6Ek9jqIBq14x8TdtJdzj-vnoVFxXGyLURKnShVmTXGwWdLZyNxVOMgXamAqiqJ9Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=uJfi6ye0LGhvBDawl5r1o8VHPnE4Im_2nGHB_NilF81GpeWZyjvVaAyw-uhzMwcEXj193HO52FuunURZWFyyYoxUfwGaMmcDWvlzyu2hymIL0czj1f2bhZHsLRtXBI-lherQ_qOos5CiaKL_Pbb5wboSZuco_S5SwLGcjJ6fb9HSOCwFi2qVCEikVc7gtezy4kiWxSTBc3t6LLPwLqfKolnt_vr0ucj2TTU-LOQYRDVLUcXfHYiDo2FtaT1C0Y4ZYJKTAemSWldyEFyTcRXOdfhrk7cNjX2-9vyYQRta75aVHj_ew0Q4I09Xx9ncOOyA1u9-0YgNhVR4QaVUnFjA4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c0c9f59b.mp4?token=uJfi6ye0LGhvBDawl5r1o8VHPnE4Im_2nGHB_NilF81GpeWZyjvVaAyw-uhzMwcEXj193HO52FuunURZWFyyYoxUfwGaMmcDWvlzyu2hymIL0czj1f2bhZHsLRtXBI-lherQ_qOos5CiaKL_Pbb5wboSZuco_S5SwLGcjJ6fb9HSOCwFi2qVCEikVc7gtezy4kiWxSTBc3t6LLPwLqfKolnt_vr0ucj2TTU-LOQYRDVLUcXfHYiDo2FtaT1C0Y4ZYJKTAemSWldyEFyTcRXOdfhrk7cNjX2-9vyYQRta75aVHj_ew0Q4I09Xx9ncOOyA1u9-0YgNhVR4QaVUnFjA4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاصل ۱۴۰۰ سال علوم اسلامی!
علی خامنه‌ای هم به صراحت در یک سخنرانی «اجنه» را متهم کرد که با سرویس‌های اطلاعاتی غربی علیه جمهوری اسلامی همکاری می‌کنند.
در زمان محاصره اصفهان
توسط ارتش محمود افغان،
روحانیون بلند پایه شیعه، به شاه صفوی وعده دادند که به زودی ارتشی از اجنه
به یاری ارتش امام زمان (ارتش صفویه)
خواهد آمد و شورش افغان‌ها را دفع خواهند کرد.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5083" target="_blank">📅 10:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5082">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add91fa506.mp4?token=cGz3Yx-cVT5Qa7iJbmCRU5nZxxoyHyjqYTbCgzNYz9mvuA5EePqizfxnlwXZWwPSFg-iOocQdI2y15lHF_79l9xJ8e3iuA4X-aBM_TVicq3VNFrJqSR4uUc7C1i3LnZHVWhFTX2ijD1_Cy98sqxUjv80Kbk26axjg3jsPCZXeNQ5OBu_PjYqC5gHDvDmEd9jrzo2Y0SCbJoZctYfu9HDLqIHzcrs7Or1XK7bYaeY3vD0wDa5DmjY9wxaF8jyG53mR-TcD8xql05e32vCR8GSU6D44aq2o46AiIFREpWe6bis4lsofXdLAWBL7J1cDKQlb75AfJuRWmlyYUGqxccGWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add91fa506.mp4?token=cGz3Yx-cVT5Qa7iJbmCRU5nZxxoyHyjqYTbCgzNYz9mvuA5EePqizfxnlwXZWwPSFg-iOocQdI2y15lHF_79l9xJ8e3iuA4X-aBM_TVicq3VNFrJqSR4uUc7C1i3LnZHVWhFTX2ijD1_Cy98sqxUjv80Kbk26axjg3jsPCZXeNQ5OBu_PjYqC5gHDvDmEd9jrzo2Y0SCbJoZctYfu9HDLqIHzcrs7Or1XK7bYaeY3vD0wDa5DmjY9wxaF8jyG53mR-TcD8xql05e32vCR8GSU6D44aq2o46AiIFREpWe6bis4lsofXdLAWBL7J1cDKQlb75AfJuRWmlyYUGqxccGWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادآوری :
در پی انتشار رسمی خبر کشته شدن خامنه‌ای، در شهرهای ایران جشن گرفته شد
و ویدئوهای بسیار زیادی از این جشن
و تجمع‌ها منتشر شد.
و به قول این مداح
«صداش عالم رو پر کرد»!
حکومت از همون موقع اینترنت رو بست.
تا الان جمهوری اسلامی بیش از ۴ میلیارد دلار به خاطر قطع اینترنت زیان کرده!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5082" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5081">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">محققان ژاپنی اولین آزمایش‌های بالینی انسانی جهان را برای داروی
رشد مجدد دندان
به نام TRG-035 آغاز کرده‌اند که در صورت موفقیت‌آمیز بودن، می‌تواند تا سال ۲۰۳۰ جایگزین طبیعی برای ایمپلنت‌ها و دندان‌های مصنوعی باشد.
از چند هفته بعد داستان جدید شروع میشه : اسلام ۱۴۰۰ سال پیش به این علم رسیده بود و پیش بینی کرده بود! ولی چون ما مسلمان‌ها به دستورات اسلام به اندازه کافی عمل نکردیم نتونستیم این رو کشف کنیم!
یه حدیث «معتبر» هم براش پیدا میکنن، مثلا حدیثی که اشاره داره به رشد دوباره گیاهان در فصل بهار! که به تفسیر آیت‌الله فلانی، اشاره به علم رشد دوباره دندان در بزرگسالان داره.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5081" target="_blank">📅 10:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'  تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5080" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=e0zCq0r5ehtDXHXNQhUhDvMSBWtTTP2GM3IMOmyyiwCMKY9wrrYl8nyxIBmk1OVLEtY381u74zSwd2tpgnri06aVjfiQFAYd0ClKbKKrrNG-Q6o4zOazOCntud4naQ5Xc0dxvMtt54VvKHDFeTSeRErDjdTw-rA0l8gnawQfa16NpiFevdoybzA5I_HelQP-0UcZU8URGMn1aOd0XVR_rF1_mCLpP3RmQ3pUGiJiM1CMvGUvH6XHF8fOtNvm0gYg_BzMQv0LLU_0TtSnn4G7aYgyqJRgAqn4ifGRAMt4Ju56t4W3-sMAPYetrCtp6-qQqk7Q92M1W5VvnTPRgxZiFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d635b5ce.mp4?token=e0zCq0r5ehtDXHXNQhUhDvMSBWtTTP2GM3IMOmyyiwCMKY9wrrYl8nyxIBmk1OVLEtY381u74zSwd2tpgnri06aVjfiQFAYd0ClKbKKrrNG-Q6o4zOazOCntud4naQ5Xc0dxvMtt54VvKHDFeTSeRErDjdTw-rA0l8gnawQfa16NpiFevdoybzA5I_HelQP-0UcZU8URGMn1aOd0XVR_rF1_mCLpP3RmQ3pUGiJiM1CMvGUvH6XHF8fOtNvm0gYg_BzMQv0LLU_0TtSnn4G7aYgyqJRgAqn4ifGRAMt4Ju56t4W3-sMAPYetrCtp6-qQqk7Q92M1W5VvnTPRgxZiFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'عمان، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5079" target="_blank">📅 09:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wia0twXakGw5DrJhnAb3f2HdmuUggwzgKO69xzZtrNIvPx4Aeei4QzpfZE3IEnYzoSrl5UPKXJg3hsXaMbuWpvtNoKNx87W6SR-rJPizoVLl2_vzyNFSMU7_G8ZSpr3QyojtaNBuMkalDEt8s49JDxZECVid954MayeVFWelXU6kKE8I0wUVQI0n9e3diORI5E3yKvOWewqNmD2PpIBC2u6vr9azuVr_s5GOWgITOLZQ-LrmvyYoVv_jk_Nz13hLm3iq-Xm90QXRYPWxe1hncDhZqK1hArkt6G817t0bT_rSS5e9OyueOozKni8y9LQbE3ByGqJhnRULv1-4xt3gVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5078" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">قاآنی، رئیس سپاه قدس: «دستاوردهای ناوگان صمود ادامه دارد؛ این ناوگان چهره واقعی تمدن غرب و رژیم صهیونیستی را آشکار کرد و فلسطین را دوباره به کانون توجه جهان بازگرداند. »
🔺
یادآوری اینکه جمهوری اسلامی چگونه از موضوع فلسطین ارتزاق میکنه و درست به خاطر همین ارتزاق از موضوع فلسطینه، که مانع هر گونه صلح و سازشی میشه.
جمهوری اسلامی با راه‌اندازی گروه‌های تروریستی و جنگجویی چون حماس و جنبش جهاد اسلامی و… هر چند سال یکبار جنگی راه می‌اندازه، که منجر به تمرکز جهان به موضوع فلسطین بشه و اینگونه برای مبارزه خود با آمریکا و اسرائیل اصطلاحا مشروعیت بخره.
وقتی نگاه جهان به این نقطه متمرکز میشه، پیشنهاد صلح و گفتگو مطرح میشه، که خب دست نشاندگان ج‌ا صلح و سازش را «خیانت» معرفی می‌کنند و تنها راه را آزادی همه فلسطین معرفی می‌کنند.
و اینگونه جمهوری اسلامی از عوامل اصلی تشدید این بحران و عدم پایان این درگیری است، چون از آن ارتزاق می‌کند!
اگر جنگ و دشمنی نباشید، «مقاومتی» هم نخواهد بود! محور مقاومتی هم نخواهد بود! جمهوری اسلامی دیگر حرف و روایتی برای ارائه به دنیا نخواهد داشت!  تبدیل به یک رژیم عادی میشه! و این عادی شدن چیزی نیست که نظام ایدئولوژیک جمهوری اسلامی بخواد.
اینگونه فلسطین درگیر و قربانی جنگ‌های بی‌پایان جمهوری اسلامی شده.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5077" target="_blank">📅 23:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">به گزارش تسنیم آمریکا پیشنهاد تازه‌ای برای جمهوری اسلامی فرستاده</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5076" target="_blank">📅 22:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=VVH8ntYwwrSlsAVq3y1TYxevRmybHdXaRu8sKkTHQFivdkKqVBFhqHBGVzUpThPa_HkJQizTuOa7g6mqiOOVZID7Jf1p-BVkz3xvZJh8I1raqcNErzMwedLFNoJMjX4ceq_BnvDYb-duzHjJ07L31aI42ZkDZVCrIlmExQ6mKuwM6Aq2pleaaIqZHE6f45q-R1gtLaemY3K1rJgImnqip99OVQC5hPj_elquP3pLmOWKM2Tj-pPx44lGahymCaecODQsbicbebOynyd2h0lrHQe-qKvOxSXpNSrJV-fEOiQ7b9gsmt_OLVNr-IHsN7swJejRYBTXCFP3IGpYyQTHOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76a3523c2.mp4?token=VVH8ntYwwrSlsAVq3y1TYxevRmybHdXaRu8sKkTHQFivdkKqVBFhqHBGVzUpThPa_HkJQizTuOa7g6mqiOOVZID7Jf1p-BVkz3xvZJh8I1raqcNErzMwedLFNoJMjX4ceq_BnvDYb-duzHjJ07L31aI42ZkDZVCrIlmExQ6mKuwM6Aq2pleaaIqZHE6f45q-R1gtLaemY3K1rJgImnqip99OVQC5hPj_elquP3pLmOWKM2Tj-pPx44lGahymCaecODQsbicbebOynyd2h0lrHQe-qKvOxSXpNSrJV-fEOiQ7b9gsmt_OLVNr-IHsN7swJejRYBTXCFP3IGpYyQTHOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در خصوص ایران : همه چیز از بین رفته است. نیروی دریایی و نیروی هوایی شون. تنها سوال این است که آیا ما می‌رویم و کار را تمام می‌کنیم، یا آنها قرار است سند را امضا کنند؟ ببینیم چه پیش می‌آید.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5075" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=KAA4oiRihCI-3mQZgCwZUcxl-ckZZD8As-cgjPEmNrydDpeEPY2QniPWW54eNpYBfettC4zWL4NTEEh4tmDYu-u9xmamYiKmG4895Sr5KIU7adKvrM5mUB-dNk0EIxIVsh8BnfgKfYO7Cf8wPoBhaE6oCbHn1rtUCeSp--EUgcHCiqdHNM41TuPytOqWIoo9wzOseelv7dobSLZaK_WXuUFUH-cTH3i6jvmgm5c1abT7ztU8YCJdHfGqhuTiap2VfNSQO98uJRhGtkrmLdli6pouLH78a_JXYN-xicyALCWFViC1ZZuBhGiAlHn3_cF3hF9TW0fTlT42dwo4eWIgEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=KAA4oiRihCI-3mQZgCwZUcxl-ckZZD8As-cgjPEmNrydDpeEPY2QniPWW54eNpYBfettC4zWL4NTEEh4tmDYu-u9xmamYiKmG4895Sr5KIU7adKvrM5mUB-dNk0EIxIVsh8BnfgKfYO7Cf8wPoBhaE6oCbHn1rtUCeSp--EUgcHCiqdHNM41TuPytOqWIoo9wzOseelv7dobSLZaK_WXuUFUH-cTH3i6jvmgm5c1abT7ztU8YCJdHfGqhuTiap2VfNSQO98uJRhGtkrmLdli6pouLH78a_JXYN-xicyALCWFViC1ZZuBhGiAlHn3_cF3hF9TW0fTlT42dwo4eWIgEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
ترامپ : در مراحل پایانی هستیم.
یا با ایران به توافق میرسیم یا اقدامات سختی انجام خواهیم داد.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5073" target="_blank">📅 19:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏عراقچی: ‏«نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه اف‌۳۵ را سرنگون کردند.»
چند بار هم ناوهای هواپیمابر آمریکا
رو غرق کردند! که عراقچی نگفته تا آبروی آمریکایی‌ها حفظ بشه!
راستی این جنگنده اف ۳۵ که زدید، لاشه نداشت؟ پودر شد؟ سرنوشت اون زن خلبان اسرائیلی که در جنگ ۱۲ روزه دستگیر کردید چی شد بالاخره؟
آمریکا در جنگ ۴۰ روزه، ۱۳ هزار سورتی پرواز بر فراز آسمان ایران داشت، روزانه به طور میانگین ۳۲۵ پرواز در آسمان ایران
!  شما سنگ هم می‌انداختید، شانسی یکی از سنگ‌ها باید کنار یکی از هواپیماها رد می‌شد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5071" target="_blank">📅 16:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0WHIrupy1x-HyTcd1Ow0P3AhwHSMVp8naA1y-SzZ7JYt9y6KtsfJvGFqiVVlM9AAzb04s5lT3zoeQPsRHRzm5xw0FeFaZms8Sfn0I7orCDBt68mLWjIPOuM3pGzEgLe66n2EmkwD1XrkdiudEr9OpTHd9Cl821O4q7Y0DottkHpiFQxv4EU3hvjOtXWfLHu3MQMcLfFnlZ8l2_Csc6_hbrY5ypzoO_fnuMBzsWdoIL-qzgyoert6joWqjXBp0q0XKAHDqvJ-MlGPAcnRLisj7r_4xOebIVVa_Rs5K6Q5z81UhAcuYWApdCczlSGhjWHNei9Wp0EGxD4sEfLxon0vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش ۲۰٪ قیمت لبنیات از ابتدای خرداد</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5070" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZaEFA3kiar1fO7VDB2Iq-zDbihp5ROStp2Tx28VHJjuWSLqomZoBDkMpQZNw5PIx_duw8ZfHwNihiOscZ-yyhTcHP4reP1qb6wDk_YR8bprff7SNgvRsdAdVnEFJVeySDrFx9L62WZpSn5snsozlV2yPyFB-jaia8RdpluOBnofpfn9_5stR3aUqiLmYESZ4CI_wVmUXeElo8lHf6UxmMrAIT37B0JdyiCA3AFc6CJra7V-DsDZpzWrOR3l19TjeO4jP1LNM9CdH5hNZPGeETyoZlZlBPw_6DQX2yCuy8vrDl3SRMF6KV3_1nxwiBUvJl83GK5zSXzT7UpydAHYhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxldpWrt5uvVyyGd_iDb4me5xfE20PsQLDqSm-RExqgt1q0FtSn8ViGB5l_LmrsFZR5TzhMio82UM9k-75V1K3V9uY2BvO-AjWcdm6SU8kHv7iMKvouysV9ayNoB2y2tK1o6xDjY7a0hB438RdrcSXdh2-ancLGHIvkUSxXilC3GgVkb-dNOgH8xIsE_kr4kjqk7c2DKMh3mRgX7TtbbDo2nLq07ouXgY_I1a28eenjUc2PQJ0LhJfuGc6ef07X6qMHHBl36dBtt5O_91d8w7lRu23G2NOiUxVhhRl-onyGkzurnQT9YRS7NtQkOHRsp_n0BL0ZaP-59B9lgRdqEIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خانم تا قبل از اینکه اینترنت قطع بشه،  به خدا و پیامبر فحش میداد اگه حامی این حکومت باشن!  یعنی حتی خدا و پیغمبر!!
حکومتی که می‌نوشت : «خونخواره! »
خلاصه! ما که علیه آخوند می‌نوشتیم، ایشون هم ریپلای میزد و از ظلم آخوند میگفت که ۱۵۰۰ نفر رو میکشن و «فقط باید لال باشی»!!
یه سه ماهی رفت توی «بله» و «روبیکا» و برگشت! ما که «لال» نشده بودیم و ادامه میدادیم یهو تبدیل شدیم به گیرنده پول!! و دروغگو
:))</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5068" target="_blank">📅 10:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V4cbOgZ4YaiTGixyaq1f6ILA2fHmz6Q5bOb5N_mrJYKSdS9pf6UiXHwdiy2Tz4NwpCMOOp5GCg5nys5dNXTXwKjHMjY5P9yJNyDDq3PloPUtG7NTk9-fNJdw2Cu-Zw46iM8Cc1D8K2WwFtZmbtT3VsTIJL92cVpv5hcU_TqyOnS7Mv9SoDXOl8CgAJKDSeU_xaTvDiJaxqlOXW3QIHAC3yIaa9CNf8mykqLWr0cABdmDsr1s4jk1tueSy4_2wNZX4j4tcHte2gsU-x18ymCl7JnZ3kjWVRJOclzBXSqR_sZs7a1XU0JOOV6VvJTS2NW5msHFGynjq5_xGkTjneDJ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WL2cBR2OCin0jVCswqPTKOf9nqaxLD3v3lIfGcXaNkZPsKnOlP0UP53MZ0Q4hbJafXpT7FxtqMWcG9Z6pYiHM3fN7ZnMF6R8pmiToID-hngeCADLZWs8Q7bXROOZXeUkqWxFslbqVtx9SCD6dRNqi9Uzjvr-EgkltEXBQBe5gGot8NFI3S8M2W4QR0Zb1gbL9urvjnA28pGgxLwN9XX-oamDHEwvZ6Gn4CkgAI2p9VqiAJffaWejGGtLmJU8VVV4-YHLOFnd38XgAH0CEsToMK7jdvsZ5syG-DDmWYGYCxXBICuwdG_J7SfzKrZNgntOxUupYS0XsMSwmsfDOm410w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DmcvbgzyiErROmeDKBVxohXqGWGy8epA3s-tjB5FWS3j9HXg04uB53pFqixy33EJGN8pl_gRbyAiNVo1MCjJzyLMUOuR2ucM_o193-pd8oIyanKN_qAt2BEz8KEGMd17xfg1rjcN20of_DRp1eYznb1OrbCHSic8jiqDPFEeyf9_ixEn9idKVMn4dsKRTbVIYnPlaDOs8Hm8MJBrHa7-nkIW7Qad8DBR2t8v1iFsNNXGFvltwHNZh2j3ous4MnCg6zX6CFcnzuyzoF2y8RDn76zImdV46YFp9tSe_fk4qHbs-R7D1tc62TPZ-xhnxJZwm_tYfDh_r3UCzzDnUKwvjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد. @iranintltv</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5065" target="_blank">📅 09:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=dnkQZNUMgJXxU0sRLz3bwNLAcTYuPjnbjBmjohjNwH5Q0E8PsSudevRbxJCyTveQIVXadPj4xKB1qh-Y5cizuCe5Tf8rP7uY8Ir_L41UEVYKm6CEXfg7799pQiU0MtQivE38n5Axd6tRyx-seAzJDykrB-9icX3sFCEmFmH9XWK3TG6MJ-5bXPdHlAIRhr1w2I7uY0TKEiTTQfiVqsb1tNW984e0su3A53NT2tU-D20GSCk1ijsoslHMtvqmrzgeuy5TYRrCyS2WkXOBLD4YEH7GetXY4UUdXGhMmBG-0ZGH1mO11YMWlXqjMSNECX9RZOdsABudAdHZ1xTCviSyhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac9d9acc3.mp4?token=dnkQZNUMgJXxU0sRLz3bwNLAcTYuPjnbjBmjohjNwH5Q0E8PsSudevRbxJCyTveQIVXadPj4xKB1qh-Y5cizuCe5Tf8rP7uY8Ir_L41UEVYKm6CEXfg7799pQiU0MtQivE38n5Axd6tRyx-seAzJDykrB-9icX3sFCEmFmH9XWK3TG6MJ-5bXPdHlAIRhr1w2I7uY0TKEiTTQfiVqsb1tNW984e0su3A53NT2tU-D20GSCk1ijsoslHMtvqmrzgeuy5TYRrCyS2WkXOBLD4YEH7GetXY4UUdXGhMmBG-0ZGH1mO11YMWlXqjMSNECX9RZOdsABudAdHZ1xTCviSyhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما روز ۲۹ اردیبهشت‌ماه، در برنامه «سلام صبح بخیر»، از تندیس «مشت گره‌کرده» علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، به‌عنوان نماد جدید میدان انقلاب تهران رونمایی کرد.
@iranintltv</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5064" target="_blank">📅 09:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pstL_qh3mi8dmyag4gbN6ADWUQjm7hydDm7CliaT2IkNx77B5SQxG70QLqSEJmI15pZUn1bx2tkB3yMhunN8cKojCATr_jFHkLKD04lPG15hy_ch72Bm6hao51ElXxuLN-TMckINJBp91ieHtvnVdlXqCkjMJKQ5EaW6K5y4g_CTaHdPvv2hAuiMjJBFzUqXg_fSXyYDnMWIzbywyut7nEOBOJ-w9be6S96DmBhdHEmULuMlKchC83OR9wMtHeTuwa99_z1XxDjcreX8pYx4ENhZL2-_iZuO1GpnAN6p1o82yABWABj-rv81GQ2zlOh84J873BzK0Yg29mDVUFdpdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بهمن فرزانه» قاتل «الهه حسین‌نژاد» اعدام شد.
الهه حسین‌نژاد در خرداد ۱۴۰۴ برای بازگشت به منزل سوار یک خودرو شده بود، اما راننده او را ربود، به قتل رساند و پیکر او را در بیابان‌های اطراف تهران رها کرد.
«بهمن فرزانه» ابتدا انگیزه قتل را سرقت بیان کرد، اما در ویدیوی کوتاهی که از اعترافات او منتشر شد، دلیل این جنایت را خشم ناشی از نوع حجاب و وضعیت ظاهری الهه حسین‌نژاد عنوان کرد و حتی از واژه «بی‌حیایی» برای توصیف وضعیت الهه استفاده کرد.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5063" target="_blank">📅 09:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز به نقل از مقام‌های آمریکایی نوشت که در روز نخست جنگ، نیروی هوایی اسرائیل به خانه محمود احمدی‌نژاد حمله کرده است.    هدف از حمله این بود که احمدی‌نژاد از «حصر خانگی» خارج شود و پس از حذف خامنه‌ای، در موقعیتی قرار گیرد که بتواند…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5062" target="_blank">📅 08:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5061">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewSuFKOO4s1YqRdUaKnDQP4Wr92cIoKogXX7LRzkcyOulll3eOMOaEZK-g57hsTWMFvJBNQTg3Jf07rkTAdJveAql1n_ArcKo1188iz0SxBvd-1-fRSTO3qgJLf9uKwCGJZ5MA_FcDeb2EtSEFXEZkBCikA72x8tOc_JoruIddRIgzAI4edAdGoHUQ9uBUFz-Ha116NfP7UsrRTGeIoCWaNvcElryk0GOWuxGunecCy3GBBn63It3ciCNV1zCRi1ecssIfqrCPoFcjcvSDcMEzMntREb6CezgaXby_hwm3M1ZPvqI_KSZpvWIxFR-UH_wOJ8XhF8Tlm4TdK2J2qESQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMqXxsuuONVxWa-Y3EJ0nxz1Mx44eQ1OBMRpEhFCif-3qCp0q1oHIiI_2U9Cvqk_G5uUgWORfRy03_gA15GkAGF-c5NJFCFz3r2FOTSPSWggR0R77ntNdvgwKb3JO3SJoiGeO8OnQx09o26EetO7AHuhE57AVho8kJeRjSSfmI9p6yV-UvxKHJF0pnVDIMWvlZImAoRq_7NAHEtPd7fVT95fyHd4lRjA7oCdgDFK7Rn-VjjwtQarWOP3Z4dUx9GNy768P8pN1xkOuK37DxIZQjg6PvFJfWP0Sidyw-Byr6SKzQbxII_kK6u8q7QKNRTbsgwM9KUvUCxny3cA7NUM5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نقشه‌‌ای کشیده که یهو از  لغو حمله نظامی، به گفتن این جملات رسیده.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5060" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5059">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">من وارد توییتر  (ایکس) شدم
😊
https://x.com/farahmandalipur/status/2056814391148834909?s=46
.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5059" target="_blank">📅 22:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
نتانیاهپ خواستار لغو جلسه دادگاه خود در چهارشنبه شد و دادستانی با این درخواست موافقت کرد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5058" target="_blank">📅 20:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5057">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وزیر خارجه مصر به سی‌ان‌ان : در هر گفتگویی بین جمهوری اسلامی و آمریکا، موضوع باز شدن تنگه هرمز و آزادی تردد کشتیرانی باید در صدر موضوعات باشه.
مصر اخیرا یک اسکادران جنگنده و خلبان در امارات مستقر کرد و به جمهوری اسلامی نسبت به تهدید امارات هشدار داد و گفت امنیت امارات، امنیت مصر است.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5057" target="_blank">📅 19:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5056">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
ترامپ: «ممکن است مجبور باشیم حمله بزرگی دوباره به ایران بکنیم. هنوز مطمئن نیستم. به زودی خواهیم فهمید.»</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5056" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxiIWaiN6foFZvXffhohPTLu8-Y-FfhNdNjU_HvpTMeR8JC5Lq77O6YXzhmK6_01QmeXNkQsGlEN9ziiB_CYBNVRCEhOqDVCSM2NsNLBD4p5VFDgHIZgqDTGhIGqAZ9T8LzpG88QORM5a2r-xQwnw-183CW5wLWz7kFMTDEDjlXV8rQ3nrAF4B7ONmeKfVggZLhTgFrvZnOncbg3idFyXxiAj-U_oLkg3RxpqKFh0ujsJa3EjYedcFKa-9TuvSgF0PkGqq_fCeCJiu0UqPxvjbsp-4SN0V7Z6A6uRd_n15IerCE1X71G-SKjCbW0rFmoip6UYHHz6poB8Qpn6agBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طی جنگ ۴۰ روزه ، اولین حملات به زیرساخت‌ها، توسط جمهوری اسلامی شروع شد! با حمله به فرودگاه بغداد، فرودگاه نخجوان، فرودگاه کردستان عراق، فرودگاه دوبی و ….. بعد حمله کرد به تاسیسات گازی قطری به مجتمع فولاد امارات و…..
الان هم که مثلا آتش‌بسه،
به تاسیسات هسته‌ای امارات حمله کرد!
و حالا هم به روشنی تهدید میکنه!
این بازی خطرناک حمله به زیرساخت‌ها رو جمهوری اسلامی شروع کرد!
رژیمی که به روشنی بین زیرساخت‌های ایران و فعالیت هسته‌ای‌اش، دومی رو انتخاب کرده!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5055" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae416835.mp4?token=sgUCnOaaYgFueYiWjfuwNG0by0cIvNETyCM77D97rMUR_e5sDBdGaK9rUGtAnn0qQEeOhz3LHwrcoB8oXMsYuzkCkhhqF2i7PUKhzKEUz7l_1jdH9NXwlI-4rtUpnkdwk8FwKic8x72GGnZAfEV0IlLc7sKeL2SokaIkK5QKjlXz7zHHczFkobbehrp3AP1zD1CnfwwepKQgqjzcDrclrI2OZDphXctt8P54AXQNZSo_1ZVb-_rJUk3Pu27JOiOlQBCKqHCwj7ddAXLxzc53Kk3a-pgkr4ti8S9l-r1O3TGpbjCa-J1RAJRBRISX3qnEvoIi3oKfclDci0xvML7C1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae416835.mp4?token=sgUCnOaaYgFueYiWjfuwNG0by0cIvNETyCM77D97rMUR_e5sDBdGaK9rUGtAnn0qQEeOhz3LHwrcoB8oXMsYuzkCkhhqF2i7PUKhzKEUz7l_1jdH9NXwlI-4rtUpnkdwk8FwKic8x72GGnZAfEV0IlLc7sKeL2SokaIkK5QKjlXz7zHHczFkobbehrp3AP1zD1CnfwwepKQgqjzcDrclrI2OZDphXctt8P54AXQNZSo_1ZVb-_rJUk3Pu27JOiOlQBCKqHCwj7ddAXLxzc53Kk3a-pgkr4ti8S9l-r1O3TGpbjCa-J1RAJRBRISX3qnEvoIi3oKfclDci0xvML7C1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف و البته خود علی خامنه‌ای
گفته بودن : شهرک‌نشینان اسرائیل «شهروند عادی» و «غیر نظامی» نیستن!
حالا حکایت خودشونه!
که زیر دوشکا و خودروهای نظامی ویژه سرکوب مردم ایران، جشن و عروسی میگیرن!
اینها سلاح های مبارزه با آمریکا و اسرائیل
نبود و نیست! اینها سلاح و خودروی سرکوب
شهروندان معترض بود!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5054" target="_blank">📅 15:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp2uIkLNwBFkncTtw-jx2hA27S28NUEwd_AVHhS63Vu1a9YU1iaN2FrHwDCY4MlygTBOgnYo8sWLY1-2hVnA2FblXIm-HOh5qtcQlcw2lfVCaCbEjT4jJ4QpvgnX6KJWeG_CC7hG-a0ohT2NJNBml1P4DiebrPZW2d86bSwgbh-EhYWbLtKCpZDG9crsJIa9YMSBPJFqpqgThP6UWiqhDAXGSmU5dWsfjhJrYw3iPhDMEhlzvXcDffIUyvSH3wY45hncWs71Sf9aIHG_XC5at64l0HzVIw4CTWmMsadcOa606edjQAJ47vByZNHNmVVpOTp3g8DvNflhgbz3w8GIDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اعدام و غارت و سرکوب!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5053" target="_blank">📅 15:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sj5CXhio4e-PrrYbTTZ6-mJXvI5f17ndfRfo_8ar_BteZiqQgeisCTwpyJGIzX3Kkri_FgKWeAd7NZVaG7b-ngjcOuS6s5GZFEdQqodpGKMoRQIHxcheT0MKvQRn-MBC8skP-V_XUzjF2GtANNdjiRFzCQgVVcOX1QjdwzFqC00v-6_dUA4q2W15kjTxOA3nec-KmZi2sP2_zij37fz1MioFKVOLYqQr39MPO-M_s2ytv0O1S64IN_h6QMHTqHfi42toLbfzRzD7CL4NS50tnOzmD5MkxFBG97czwNVl02kvVD2IM15ami5k2yMRdzbkdNIQenSUFuHPD6VTg6KaVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSulvsrz_ZT3UdizMGjBLq0a_GAjxPpWU7CeGDIatU8b5MjYc8nEfUMv_yzgG-9C6m259GivLB9NDmMm8rpjjCBBsOI7wz3kQd-maUOrISx4k7c9XKCgXadSN1twkRb6rLq_YXIBKEDX_cr7ZvvSM5bi9WXsewJUhuQSdLmQdFMAtmzwi5gZtTnXbz0ILQG6oQxAZzyTm-B0AoIrPqTpDnl2i1QEszxVdMaAC916Dv_ZUM7YsyYbv4kzK13aEFGuRY1-YfYrKHjOFZfLhJHMmzV-2kUDET-crMkswHjoz-BPxU0fb--Wpcha0xDKfO9PXXTwVwl1JdWc3dyhXRG_EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJBT2m_bIZBClXMWkgv8zPCz8BXyeGG9IsZYTBc44Sp4gfns-7Z2WoB0b2_hpOYhsIQQ96bOnJ9pF1k5iDUrr1ct5G1i8YRmnwU99C1EXRvC078Lcyt05y1HGW5inVtxGiUDmKTEpoPxibzddNkAHspBofiugEB5inUMvZ8pTuC35GjijO6bNHjXefnjiQyxWdC-_ykH8sAVI8Pf14BjdDuczjdgosyFb2E1d-tcDSmas4xrkS6cQpSSnfF9l_LI340zoZnsHqx0WXPaGcg_hSYw45JrKzi9dJAiP-25r4HBQgyPZUE7zvbLKLkV4_nEIeWzlHYkOpmVa6xYWob8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwAVAlsH5fW3XwY5olpRrcdhclPIzzQr_a3n4hgHIJB0MkN5Zj-9wSPPCYCfHHxq0SgB_R2LnN72DveRiXFFIkp0QuFH4Nofj8mZ3jJ6jVNeueIyL5-Iaw6GUZnBMypoPh34unFvHoziD6p_pppzp47q-NdnMzbzPdbXwZQSe4CUEN2rkrHsK54r6k_erQRnTAwJhrJbznrsrdfkqMjyf3bxOE0FHdIIxXKYy-vsstH0-GB3smkqDQNqfn1KXQbv77bMvtKpEcvYkEbWQK9YZI7ji9HUg_uVg6uEINXAqkpL0KvA99RZQCTdEfBR6HEtg73vQAuWKNLDv9vp9FSfhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5046" target="_blank">📅 23:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5044" target="_blank">📅 20:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=Ztsk-y5rX9SIIBg7QQZP2xWHMaUyBuiRu7RUJqOrqskxXsmuaCoUkMxXIEseSu8IaEPioUpztcPMzTQv-WSj4y3m85dG2A6eipY1idPW7TUutW4Hmige5Ar6ZyUNB8hlLkTP8ktGzctDt6rg9O3EXMSv85lmBEpLM5pf-8BeNZZT4RDpIwDDyMe8VuJE_LQjGzDvFsqemIiGRiEDPKhdUhWzOnVdKwrl55v3H0u7rBlz400y_YNau-UeMMwgzjNd_hXLu5lzvrL_hiHrDeRSRhJRn-8UMPMNl51l-32Ma_o5SaAqu_JXRCruCLixC4kM7EpsOao6aD3jS6CGSPsXvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=Ztsk-y5rX9SIIBg7QQZP2xWHMaUyBuiRu7RUJqOrqskxXsmuaCoUkMxXIEseSu8IaEPioUpztcPMzTQv-WSj4y3m85dG2A6eipY1idPW7TUutW4Hmige5Ar6ZyUNB8hlLkTP8ktGzctDt6rg9O3EXMSv85lmBEpLM5pf-8BeNZZT4RDpIwDDyMe8VuJE_LQjGzDvFsqemIiGRiEDPKhdUhWzOnVdKwrl55v3H0u7rBlz400y_YNau-UeMMwgzjNd_hXLu5lzvrL_hiHrDeRSRhJRn-8UMPMNl51l-32Ma_o5SaAqu_JXRCruCLixC4kM7EpsOao6aD3jS6CGSPsXvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXvwuEmey0_ldmb_MnpwgwNdSvPdv93Wb3eh0vLRPl_nnXNA7OiBfocVxigqth2ixvdTelyjn8K5PDh3R0m01jJJMVDML8VjHnu_ahKYotfIyQpSWAdYDcsBYp7rGyF3g36EkaI69xmlbfbW0ZRtYLS3MmMt5xs2vaUUivWzVf2cV4e2ouEmGLMyQo4Ni1hGV0L-txjJLO_FAwwRjFXlgNq6AjO4-h39bkopld50qPFp0kD6z3fyj-jl8gJOK6ScPTpAtnJ_bE3F_-ZL-7E2t_29etkjQ8v4PlknZqOidBj3vf1wjAutf3ls5QluoMDTr4Xyr5WxC9YLrD8Xo5eL_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXjdH3Lg7AZuuUd-P9REG_IbCryK6QOmsnM-WcP1eSm_RrUYkTD4yLDa8W21VV7VxQsLcTY7TtjUXHgFvc2VcwIM4X-dX6KDgMnsSUy4Dp1tbwMYZYN1ZzsRHtKKgtYzsW_M-609xAVXEblI44dS_7Ilpj-clKtyxy2LSb2elkZ64h_2xRf2CSkzFe8PKz1bq_3nvNRqg_ZM3LYbN2S-iRr_17_oKngwyNNLXWTl244ruhoUmmnsSGejv3d_Dey4AjQT-UfqDRo8yLdGebMsMuXe6GIpmg7VKpdQsf1G79v_LnEmlOSqoXaNOhAX5UtlK9YEoF7dq7YH5331wfu5wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v0sJ9n62o6x2PpMhKFast1R8_4jj9AU0ihA-SyGzYXG1x9MemCZHD3lZkiEOHUdI7xIz9KWtC8Vm9uDMWyZbQIaAS9v3p_O0k_McQ6kyl31sLei49ZiXoXb5dr8yiH9ywocnj59La5p3bEizHbHpfdewbE6nHoetStNG9hntjxKQz_3xAzUP-3u7ocLw-MISjQ8RZsSae79JJDjA8BZ7uanUDNTXeYYoeFNIyTDsAzze7qN6czqNE2DGq1PYu055eoE43gnXuzGzbp2re5Km2mmtnpkZdET7kxlVqFJ6RQrW0vLqfmhgyLlvRVvn21thsQ_6e5-4AtKGX3ZXISmh7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=G_rH1q4lzkzbkfwumO5GgzVBDLIeZ3L5zSR7CpPcPGpI59861V83XuMONNxso2GjJ4JpoxBbQOjplEnqs-Yh14sAdEgpiZieAIfSahtXjC9a7cKdcUfW3IGsChpz75nFUQNjw0bGnxVQp_N-sv7Z8Fayj-BpLk6soml2YMpJNGMYNuV4yXcyhiw22zvyyy7dfm4TtkBtHWIphYUdv_MxSXU74_CbZ59lyBYCZ0H0wGW1Z5Ny47Tp-Z6NRkcqs1m_wjNomJwzZlXZJTwc-jSdfiCMQAYdMUjGqSH1qAsyLAozcfsELA6wVIMn6eELTMQ6-3OdP_UqsUxk3Bse3oLKWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=G_rH1q4lzkzbkfwumO5GgzVBDLIeZ3L5zSR7CpPcPGpI59861V83XuMONNxso2GjJ4JpoxBbQOjplEnqs-Yh14sAdEgpiZieAIfSahtXjC9a7cKdcUfW3IGsChpz75nFUQNjw0bGnxVQp_N-sv7Z8Fayj-BpLk6soml2YMpJNGMYNuV4yXcyhiw22zvyyy7dfm4TtkBtHWIphYUdv_MxSXU74_CbZ59lyBYCZ0H0wGW1Z5Ny47Tp-Z6NRkcqs1m_wjNomJwzZlXZJTwc-jSdfiCMQAYdMUjGqSH1qAsyLAozcfsELA6wVIMn6eELTMQ6-3OdP_UqsUxk3Bse3oLKWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=rAvt4BETKDafkMtiXTqodcRvbs8bpRiGwLFsXKyqPYVZLeaAxiO2DDfqAOY479abo-AVKFszT5388fAGzyDf-Mqk5PH97HH5wMqsIRkBlTUO1MlxJw7NzieKGAjvBOJoEXXvL9GmxQuPyPtwFN1YAIPrMzblUJ06sI63Sdc86amNOfyxtLqYfOZ9mZT7LeohWJ2BgI2BdfvCEtEfooX9KPEB9w3FrhIZmAczNVTkWlMXKFQrkn5WimLAzwngvlsW9lUmmpeTUO6aVzb5T46UgpvshqZ2opqB6E534-2zSNIBkqWDAc8lJUgHrKfdskulgmnguv8qeL7KA0o52mYahQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=rAvt4BETKDafkMtiXTqodcRvbs8bpRiGwLFsXKyqPYVZLeaAxiO2DDfqAOY479abo-AVKFszT5388fAGzyDf-Mqk5PH97HH5wMqsIRkBlTUO1MlxJw7NzieKGAjvBOJoEXXvL9GmxQuPyPtwFN1YAIPrMzblUJ06sI63Sdc86amNOfyxtLqYfOZ9mZT7LeohWJ2BgI2BdfvCEtEfooX9KPEB9w3FrhIZmAczNVTkWlMXKFQrkn5WimLAzwngvlsW9lUmmpeTUO6aVzb5T46UgpvshqZ2opqB6E534-2zSNIBkqWDAc8lJUgHrKfdskulgmnguv8qeL7KA0o52mYahQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما :
آماده‌ترین برای حمله به ایران اسرائیله.
اسرائیل نه خسته شده، نه پشیمانه
نه به آتش‌بس مقیده ، نه کم آورده</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Obkpd0bTqXeCJul4hYlqW4QkesXhICthj7R_KMniRkpihddJatvZiQdFNbrHzQV8-Qei-lCCC7JxxcpVRYcZ0rvXh7nJwOxrhUhuZZYuw01d0XlDLclXeYSt5h4qsN98oiO_mGFPemAg7abHqq6mrGO4IR56rSarjezf7lER7vTnpV7ZrETmnHAwxKWtCUX3d7syfN2OZZ4Y78d0Qx5tU4CoZxacuRm-ptWS_LIjZvF3S6EioP4K-3OHHx-nsbF14ITGK21FW8SwfLwUR3D7oxHhD_NJv4y50ugZPnPDo5nHx3bU9dXt6Phy4BFqPZY3NpBcXGUgP2kJxBoPwCmoeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrWG0k6QYNl8Kdf-eTkJQlNZo1JRyboRGcAVlT0m2aHZSzbmzjtWJwFon-UbWdAujBmvtj3oIY2cBBgatW8mDfQQuOktGEUL4UTvjkXv1wrFAnt70IqpPObSkwR8e2TzWMmSfWz8vOGJD_XUZccGTfRAiCYJq6ryMVCKd586GsdCgSagSFt0f40mv1e8SKT4l-Z3UaaSmqvArUyDBNqvbMjwXOj6vzzk7n8A6P18mcI-n7rHNolSkdfB37pNV863pbDQVt3Utl7w9v8SqnOTJgyqfzrITiEWB4ZkT5GvfJrtGN1G28fEEuLV2cCuklsGisfYeaWCL-rbb6EYSWkZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ee5E7Hl2ieMyUZTFdtbi4NWgtXKqwxfyjdo1ZRfmr9BxnUo3xn7dnMAHMbhGXJ7ZOCAu7mEBcQ17rjE5ITyY4YpzG1v8y3LpXt5aoYeEBSmwch6eZZRaOYCtffKr7MqYlsI8A1llrEuTOMH8d-jo5Pl_1U9PxZkgTSdb7GCiK6vGcdDRVXdaHUuHsv-l2IvyWrfm3sKf8yizhQh7O6PvjZTH_EkSy9BdI6XonOtMxhagnwKrDaNHt3Ch3MVk_6-eRHrx_A3R1xK10O9_yPpxhGZ4X5Hg6PiK7H8FR4hTxGGiUXyKRNrucX4AgJz-uxJI5ADTtyywdyvuUVPfPAHAUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات سخنگوی کمیسیون امنیت ملی مجلس.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5029" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5028" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5027">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7OgkMfIEEUFEp3yzIhXnArOILGZkx63thwLIa-mYvT48pPvRxPnTy-MgvQBeBMH77cZkNT1TwK9nS5aEq76V85Rms0CiCIb8xU1-Fmo1kRQyF3IG6uhnh3rysgQtik2mbN0FUGSJ61DM6gwFfW42K7RNy5Bs1ZzzxbMMWpYA1rz81eOFND2_O_mXEqOsF2wDTNiIgtbNprSpyBtJNtSSAP6pRPhOHpeQpwTrG5WD7Vqan_QBjAbaac7XZPRbo5wSgHTp6P_EJBaLBtLyNn-rRHEq7-vqmOQNFh67V0xWgORjjZGRZtdM1JqqJxrJQiNeWNtyUxCV67ZqKft0noP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟
در پایان جنگ ۸ ساله
۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و
شما «جام زهر» نوشیدید!
خود صدام حسین در سال ۱۹۹۰ به خاطر حمله به کویت این سرزمین‌ها رو آزاد کرد! خودش به اراده خودش! نه به زور شما! شماها که جام زهر رو نوشیده بودید و تموم شده بود! اصلا خمینی بازگشت این سرزمین‌ها رو ندید!
چون یکسال قبلش مرده بود!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5027" target="_blank">📅 23:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344237687c.mp4?token=O_dOlBDKZsXk7QwuYfK2Dbrug0dZbjjA7JzdbQAfrQmlvZkNrnPtWFaWGfw1Xsyj4EbobX-wnn9Jlj1QnREIOvP4rmfgQMFlIxeogU5yopF7Lr_8sgkksPsry1Th977upaBp8DIcNjsltBcEz3gYcmepjFWpio0-nAx0b35G8Bd58WVObFnWwZdG38LYdVnhfHx85r7rPzhfKblX2QzuZRP7lO8bGHnSXv2JA0miLuqPRZkb-X8mhfxFLS_6DJvJfPG6p3W2smWXPMCLNt2JYNIdxtQiXPHr1qyIgAJBV9fsfydYDyADjTiYZuN7Lh2qf3PHHwibb7lYXYySnHrqjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344237687c.mp4?token=O_dOlBDKZsXk7QwuYfK2Dbrug0dZbjjA7JzdbQAfrQmlvZkNrnPtWFaWGfw1Xsyj4EbobX-wnn9Jlj1QnREIOvP4rmfgQMFlIxeogU5yopF7Lr_8sgkksPsry1Th977upaBp8DIcNjsltBcEz3gYcmepjFWpio0-nAx0b35G8Bd58WVObFnWwZdG38LYdVnhfHx85r7rPzhfKblX2QzuZRP7lO8bGHnSXv2JA0miLuqPRZkb-X8mhfxFLS_6DJvJfPG6p3W2smWXPMCLNt2JYNIdxtQiXPHr1qyIgAJBV9fsfydYDyADjTiYZuN7Lh2qf3PHHwibb7lYXYySnHrqjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶۵۰۰ ایرانی رو به اتهام‌های ساختگی - که سنت همیشگی این نظامه - در سه ماه اخیر دستگیر کردن!
هر روز هم آشکار و در خفا اعدام میکنن.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiYp_6Ak9RW-YicVXX2R0ezKu37goJ1x2k-bGiQHuvQErY1SznSqPxGNChmwuVt4GqIBworv-y4kEDQ2xJv7qZKjlFB5AHJFyfaafnkZeQirkDf0rpmK_FQHwSOikX2xsTDmTEsgqq_TVmKDNnqhGkI5W2gDjH3iq91sBhJ5kOfs1Kk5mI0N3Ko5iP0fWg4nqXB-FY8hF1yCZPMQSX_vqxXoihjn_dCArDI-8fbke6xEvP3g68N6Hz1W1GFEqLfqhlWR1mdNZWWNIaWbgo1KjGmA91M63XFy_9iAY10V3BlxFD2JycBXj1mpxx1_Y_bz8jNiIhtaqck16HEtcZINKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدصالح جوکار، رییس کمیسیون امور داخلی مجلس : «در این مدت پیشنهاداتی از سوی آمریکا مطرح شده اما جمهوری اسلامی همچنان بر همان بندهای اولیه تاکید دارد. شروط ده‌گانه خامنه‌ای خط قرمز هر مذاکره‌ای است.»
🔺
ده شرط جمهوری اسلامی که میگن خط قرمز هستن:</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5025" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید شرایط جمهوری اسلامی را بپذیرد و تسلیم دیپلمات‌های ما شود یا تسلیم موشک‌های ما</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5024" target="_blank">📅 22:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏ترامپ به اکسیوس: من هنوز معتقدم که ایران خواهان توافق است و منتظر ارسال پیشنهاد به‌روز شده از سوی آنها هستم.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5023" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
ترامپ روز سه‌شنبه جلسه‌ای در «اتاق وضعیت» با تیم ارشد امنیتی - نظامی خود برگزار کند تا گزینه‌های اقدام نظامی علیه جمهوری اسلامی را بررسی کند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5022" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJPmBWLpMRlNejK7xMhTknzTfsLkKHX5F9r5W1Y2F2HTUUNBXN2NRGQUwvWZnyuKl5a0oDamEaRNObxdcXXmz2WxPBYDEZc-LkXvUKK2I1dTsqeYY0PvUYuB1HrjX_mIDw1J_RcS0VxEplwQOuHwwJ9o81wJ6BxCIL3P3GLELsvGaCeH1BE6RIR13K9KyX1L3bmU7tfX_jku3dCaKkBRQaQ6xojVSaU0ppO1XXyDq2XNVdl4WMDdb0-tZfHamBNr-aoM_2UUfY0-SJ8pSONuQoRlbGQZepZOFHIQbdBcwBBsFe5kMMzH0kqHP06340989BfBzBr0tsRQLqtoGkGcJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=R6Qy8sWwVTyG7idNwkbVGaCDGBP2vCKTJ_HgVboKlBV6bA3-yzF_GbJ5Vb420iGA0n7XKiCZrOMOg84LvcRnq0PbglCPFojjsz1X1WDS8hl9pAl1NJ3GIWSZmPGiOUYEeDsXxrvq_VReDD_b1-95ZJAQ_8KxbV-ftWC-O4LGlam6S9GDisbrU07paAWk9gbUYMCY00_sEEBhdwOKcUsdWQfuvjsPXMHJwO95aOP1QCvhSre2n0noQzRrpLx-BQLbgNbmeXPu6FUp95j_kblw1paERzCTOeO11MNV4h9PGI2jIQqWoce4gaqJOjtUaK9zXUYM4Q_YYsgUfX-aB4tXhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=R6Qy8sWwVTyG7idNwkbVGaCDGBP2vCKTJ_HgVboKlBV6bA3-yzF_GbJ5Vb420iGA0n7XKiCZrOMOg84LvcRnq0PbglCPFojjsz1X1WDS8hl9pAl1NJ3GIWSZmPGiOUYEeDsXxrvq_VReDD_b1-95ZJAQ_8KxbV-ftWC-O4LGlam6S9GDisbrU07paAWk9gbUYMCY00_sEEBhdwOKcUsdWQfuvjsPXMHJwO95aOP1QCvhSre2n0noQzRrpLx-BQLbgNbmeXPu6FUp95j_kblw1paERzCTOeO11MNV4h9PGI2jIQqWoce4gaqJOjtUaK9zXUYM4Q_YYsgUfX-aB4tXhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5020" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKMrzAOqGnwbK2AgPn0XkNT9U-JdXqSOT6acIuuCwSppOdSA4J_UgfHEUejRz9EQ4bY9rYp8MY3GiZUuRnQsLhA3V87Hjh6_nqP0JP3KpZHRuVUQn24cZzclIP8qRA0BIblA4kdnP1rpEaNPJsv8kvqBtBYYabMtPvpVMP2-SwdxCL_NSqexHpAPYB-o6BwJjg69hDivE5hjkkTh4v3sbtMHJz7TtcyQofemRHdSbMW8UJgHRTpYOwGWes1_OQxxrK4NZerq3TozX_fusyLm3cl17hP6X0HrAj1cQb3qAlX-qVrd6rWyeUipmDatDgI0IF_JCEvfhjJaUzItYLicmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5018" target="_blank">📅 15:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5017" target="_blank">📅 15:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5015" target="_blank">📅 10:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=THXNko3socN0deBeuv5uiocSCR7HxJQuZQ302nziXppiFU-OnHyG8Sd9HVY9MRRxg5eNw8L7wKakQ3aeo78PoUGqGJmSxokwGhoJIdkfL4HIkFhTHwuCIx6h6yvT6ilgywYcJeHQtkhnm-UWJkRCU4DRgLJCKFfwdSdEzE_dbHrOzR34H_jSEDIcb9GT2v8nqcZAoVLMqHg8SDn0VHMAHt2gicTktf0tdt21IkIAPQSntJHEzjlYymOwxoBtBlFw_fyGZyZ6GOKCLa1e6mWqDwhPLOI7LWPdQ0AO8xS02WfI3aXv5gb2ar0t1FLgGr9LsfoNm9L7jD014J1-_rt7gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=THXNko3socN0deBeuv5uiocSCR7HxJQuZQ302nziXppiFU-OnHyG8Sd9HVY9MRRxg5eNw8L7wKakQ3aeo78PoUGqGJmSxokwGhoJIdkfL4HIkFhTHwuCIx6h6yvT6ilgywYcJeHQtkhnm-UWJkRCU4DRgLJCKFfwdSdEzE_dbHrOzR34H_jSEDIcb9GT2v8nqcZAoVLMqHg8SDn0VHMAHt2gicTktf0tdt21IkIAPQSntJHEzjlYymOwxoBtBlFw_fyGZyZ6GOKCLa1e6mWqDwhPLOI7LWPdQ0AO8xS02WfI3aXv5gb2ar0t1FLgGr9LsfoNm9L7jD014J1-_rt7gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5014" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=CqV3sUUFi8_SQSTGJPmjObZFyo64u2qn90ZYlqo1j_-4WM8enDwW5THXH-8vhA2IOl6B40RVAzuolll5bZ-vy3krDH9QImRzvgQqJgPMdtZ02A8H28qnKboEQM_-xK5u_yxkpnMH_sE_89mY7CnPwgl1I6eJOmt13LEgLuI_dSb5DinELesdVTQbGTpWsYaBlVt1iSR6F4eOFK8WUME7dti0YIOpNZ4qr5HQaSnDmGt_8UrZOupSx52axc-5ZMPefU14zCrh33QgmknRCCW6fJJpDS2dEKuN91uUDEJsKYJAGvlPVzWyDjZZW3BpAJ2jJu1PRj-S0wL93SoRQlNlxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=CqV3sUUFi8_SQSTGJPmjObZFyo64u2qn90ZYlqo1j_-4WM8enDwW5THXH-8vhA2IOl6B40RVAzuolll5bZ-vy3krDH9QImRzvgQqJgPMdtZ02A8H28qnKboEQM_-xK5u_yxkpnMH_sE_89mY7CnPwgl1I6eJOmt13LEgLuI_dSb5DinELesdVTQbGTpWsYaBlVt1iSR6F4eOFK8WUME7dti0YIOpNZ4qr5HQaSnDmGt_8UrZOupSx52axc-5ZMPefU14zCrh33QgmknRCCW6fJJpDS2dEKuN91uUDEJsKYJAGvlPVzWyDjZZW3BpAJ2jJu1PRj-S0wL93SoRQlNlxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=MdFnQ7AkVJRQP5tDPPadLi2VzS7iJLm5Ddp8AOTqVCAkABDd65turgU002uKcqY_6qQ5vsmAV5TXSxxXwc-4BYdzgAnVjxuZkEN6GPY8jGBDAB3fM2rQtme3JfVjNFLlO2rYh-NmdKAoJCbZ3LXNxQM9TwLboAkZjIxjYkIXMNyp6nac80e--UDWDP7JQGthd7_-PMP-SwAH70c0fRtPE5WTFE5_KxbCs877SAf0dpEpQzxj6bYEb8x3ko3dAjAD9hlg2n0S36J6pW-JQIXcr6_gjmfFj8F7WOhHzg4PuYaqSBtkTGEvCQiGvA-XS-P5ce3kFSkPJykWaz1uwwAIwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=MdFnQ7AkVJRQP5tDPPadLi2VzS7iJLm5Ddp8AOTqVCAkABDd65turgU002uKcqY_6qQ5vsmAV5TXSxxXwc-4BYdzgAnVjxuZkEN6GPY8jGBDAB3fM2rQtme3JfVjNFLlO2rYh-NmdKAoJCbZ3LXNxQM9TwLboAkZjIxjYkIXMNyp6nac80e--UDWDP7JQGthd7_-PMP-SwAH70c0fRtPE5WTFE5_KxbCs877SAf0dpEpQzxj6bYEb8x3ko3dAjAD9hlg2n0S36J6pW-JQIXcr6_gjmfFj8F7WOhHzg4PuYaqSBtkTGEvCQiGvA-XS-P5ce3kFSkPJykWaz1uwwAIwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=loNnUgl_kCRh2fUgBey6_9xK-VChNrGBDxVBFegjPbro4HU9bECypPPvIGR0WzCc_iHkZyHffipmhO6qXlDzt5FIXL3FQqE1LmM2G09fFQGKicW3mv2DY-GyiQXE6bFxw_9w3ogWKPKIhecFdwCkZoB3rhLsM2xDEmyKGIdQk84Paeb5yhSUBV7xxQn3uAL-ybIhqBlpP9XQ9f11TPEiCjq5lLjJroF7_4umBnVpe3HTFaXd3j3p3UbIFEDLLTkCUaU1bAAFx3dQWcMzXrQwEmDmS7moo_aR7vEuqUM1fbiGZo0zytzEcwThPA34qIC9-wJzHU-s-rFlzcpnzPrvTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=loNnUgl_kCRh2fUgBey6_9xK-VChNrGBDxVBFegjPbro4HU9bECypPPvIGR0WzCc_iHkZyHffipmhO6qXlDzt5FIXL3FQqE1LmM2G09fFQGKicW3mv2DY-GyiQXE6bFxw_9w3ogWKPKIhecFdwCkZoB3rhLsM2xDEmyKGIdQk84Paeb5yhSUBV7xxQn3uAL-ybIhqBlpP9XQ9f11TPEiCjq5lLjJroF7_4umBnVpe3HTFaXd3j3p3UbIFEDLLTkCUaU1bAAFx3dQWcMzXrQwEmDmS7moo_aR7vEuqUM1fbiGZo0zytzEcwThPA34qIC9-wJzHU-s-rFlzcpnzPrvTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/emjUsj0Nr0HoJKSsTO_yq57AST5HSOm6kX-NDMzQ17fVgfLytqIgLQhckBlSHDdfGVriT_v09sTa-_nDf5SaZHjOAHoIu3zto8-1YMnh9OrKlGzCf4tOYFT3kX5Kge-O4EPH1xgIAP2Pd_Ap3Kmx8qhCslNFWj7pU25l-d-YiJfB55spumoSxUdSL7lO8_mX4dfO64tfpyUEN2xqihBTR5MdNrwUZ4mZSplO_dxmPxgPGTCUlWtlm4XYR5LNW1zgX5X974adN8fHd8tRXsQracHC3XdvS9n7yt9gT0FA-yEaiCEpNCGdGLl_S4zE6sJcvona83xtX2zIGht7aXGKUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iSfSN6eKhBgVDksH84ayKtq034Z8-QyPZrpaCFt8wSjdHfbc8fLkS_mBV_ZABwAMFIWTS0r-9VetTqTzwUbrGuI7u83AeiL2QSUYNrcfWXVvNO6imgAkrTzTWBpPPwOyw0xc1PNsd4RV8lKzExvzZ2MJfv2__kexORJcvKabAYH6kBKwqtfb7rnRV3U9rYdpq7OesmC62rEbDOB_g5tM8SudLIP8HI3TFdOf6ze1Vkm9-iGSi3xhIlv1qz0CXAN8e5E7r60e3vI_IkgvhY6-hSsaT1VHJzGRndizapscRq4POUcpu9nD3PalbLR9eVO1JxOWXx9iU_slHnRvt6dcNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دوستان بزرگوار، این صفحه به‌صورت مستقل اداره میشه و من تقریبا همه زمانم رو صرف انتشار و پیگیری اخبار میکنم.
اگر این محتوا برای شما ارزشمند است و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5008" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">در ابتدای این فایل صوتی که خبرگزاری فارس منتشر کرده، به نقل از
حداد عادل (پدر زن مجتبی خامنه‌ای)
نقل شده که فرزندان مجتبی خامنه‌ای در این ۷۷ روزه پدرشون رو ندیدن!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5007" target="_blank">📅 18:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbjqyuGk6bfj_QJ-_qaslbuNuAEpxWgak0c2mhONhage0Jaykr4AvGfZ_h_H7eexmMCy3tMhaNubceleUsS6Z5wTHIXznO4E7hpT1EO6DDX5eK4hxSg8KhEFY2Ldk6Sywq_MWR0wlUnyTnMfcUeBqOhMGCvOOsy66mMsGDwa8K6Dk_Abh73vSZ1Aoysk4FI4kdtWa8X8wn23j5EtLhG5TJ4VPOGx4V6HWGAnEylYbQRTTD7TQU8db84GA7iQiMvMXbA7TWmSDVZ8WwKac0Oqkadvx25Ooc7Lq4SdpxUEnLhGsNWl6YqhLkyrUVbJokZ_Y0TiHKfDsgRQBK_AeQR2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z5uUCIs_6h3HXmQKssP97410fXsfljktjgoVk1LUdPAtSQPWNtLuTLTs-wocPnf2-N61JsvmhW6DUL5sqUjljLxD--59NU6bSmsWfNiO6Vu6Mkv-oGhaUdJ-CkSXHI67af9aZBQY9pp6cWfTp2Jcb3C4caSy4ovBiV_KFwj9_g52s6auBBktAuQA19W8SFX9Q-rcuLOlDxsl6T8e5m7PtdUIqKq1nkxd5ZRt2ELeQzaWo1dwEVwUCknWIwLTEFZlr2Ub2qD9qBuDKO0fFNOy2m3wPBJukoxpceXuFMKPH3SjtZc56zThlVXB3LuUYJnuZ6neCjpLxF7ug5ag1b_9rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5005" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=qPlfTMh4gQyD2jNdPnmPCz6aqWt8PQz3g0tTvFV2gQKmyErAyJzqiqFKM2JLD13WPXSUcJCNc3ZHeFKvabBFO2DXu1IGZ4BxclSIKKiUVhKAumARIk57Xf_igydfX9B5NRnYNBsA3dH2yGroUtTyr5ScYpk9ahV58MWGRQSchytH45Dkby-eB1Pesuh42nq0k_K3SJwlw3SuR-fGTF5Zl2sT6cK2srqq5JuoyMv2EckTHZ0AqR1Y7eTOFUIkf9caOXz82jKz8FDeBfcSd8N9UvqUgE-5v1yahCngRe4M3vNtOZQik9wrWxssnacbV1fuNcOc47YQxmBb_BKgEDXgtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=qPlfTMh4gQyD2jNdPnmPCz6aqWt8PQz3g0tTvFV2gQKmyErAyJzqiqFKM2JLD13WPXSUcJCNc3ZHeFKvabBFO2DXu1IGZ4BxclSIKKiUVhKAumARIk57Xf_igydfX9B5NRnYNBsA3dH2yGroUtTyr5ScYpk9ahV58MWGRQSchytH45Dkby-eB1Pesuh42nq0k_K3SJwlw3SuR-fGTF5Zl2sT6cK2srqq5JuoyMv2EckTHZ0AqR1Y7eTOFUIkf9caOXz82jKz8FDeBfcSd8N9UvqUgE-5v1yahCngRe4M3vNtOZQik9wrWxssnacbV1fuNcOc47YQxmBb_BKgEDXgtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پیام‌رسان‌های حکومتی «بله» و «روبیکا» دچار اخلال شدند و بعضا از دسترس خارج شدند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5003" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=OqMH6qaJJjCF66LcMWTTUBXBNd5M0C2ZyZOFgIsgvI2LjmNNkWX_T_45hDP-8K_5JG5TXbZ2kJu6FxZtL-ylOj94-IKi5E66zcWzAQAtu5nnISm57yByAH-ZqGTTOv-BwD1odfhKzKjI8GlByk0E5ob-OfoGE4XhiMgPGsSFQd_1iB4WnnyHTD8sa-dTSHqQRNxczx-qeF9dCiO8m5rApnuZnrVLNm4UQc50Teico9TlhFLguH5THwQzNOmQATl4_ejKeYnBBclzvTnWKLTgs8jQwCZoVv0_GEyy0AvxoRt2gmWUH5KsVIZHjP2pTBON_VPm7UFFlD6R0d7glh-U7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=OqMH6qaJJjCF66LcMWTTUBXBNd5M0C2ZyZOFgIsgvI2LjmNNkWX_T_45hDP-8K_5JG5TXbZ2kJu6FxZtL-ylOj94-IKi5E66zcWzAQAtu5nnISm57yByAH-ZqGTTOv-BwD1odfhKzKjI8GlByk0E5ob-OfoGE4XhiMgPGsSFQd_1iB4WnnyHTD8sa-dTSHqQRNxczx-qeF9dCiO8m5rApnuZnrVLNm4UQc50Teico9TlhFLguH5THwQzNOmQATl4_ejKeYnBBclzvTnWKLTgs8jQwCZoVv0_GEyy0AvxoRt2gmWUH5KsVIZHjP2pTBON_VPm7UFFlD6R0d7glh-U7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=UWt5NWm2LbRUbIPGfMOJc0gNf4hIsk_t82GdDkSBV7AIXhQMuKMEaLSB0ZLGTMxZSRnIlj6aFS_8XnIu1_wYQf9TS-pylFvrXB0LeCUPwRmS9OvrY0d-otBpJ1TVna4IJEdcHSM16XmEmJwdo_Y32aXV6IJOc7ihhpHE6_3f0XO8gk04cUNC59zlZZWaZ5XxPBrvWmC80v1jHA4P-MxpwAA6H39xdrtzmv3BxLYa-0UqU2KNOYBYM-SEObRRbrvNRe3aLyVMiweYd7NGyxVw0d7tSThX3KU4nok660GN_3y28LqXk7uRLsmWjyaQRnhtCCwdrqowEee27StLqDc4OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=UWt5NWm2LbRUbIPGfMOJc0gNf4hIsk_t82GdDkSBV7AIXhQMuKMEaLSB0ZLGTMxZSRnIlj6aFS_8XnIu1_wYQf9TS-pylFvrXB0LeCUPwRmS9OvrY0d-otBpJ1TVna4IJEdcHSM16XmEmJwdo_Y32aXV6IJOc7ihhpHE6_3f0XO8gk04cUNC59zlZZWaZ5XxPBrvWmC80v1jHA4P-MxpwAA6H39xdrtzmv3BxLYa-0UqU2KNOYBYM-SEObRRbrvNRe3aLyVMiweYd7NGyxVw0d7tSThX3KU4nok660GN_3y28LqXk7uRLsmWjyaQRnhtCCwdrqowEee27StLqDc4OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.
و نتونستن چیزی پیدا کنیم …..
این همون حادثه‌ای است که میگن
مجتبی فقط کمی زخمی شده
این همون حادثه‌ای که توی
صدا و سیما گفتن همسر خامنه‌ای (مادر مجتبی) هم کشته شده
، بعد از ۱۰ روز  گفتن نه! زنده است!
یعنی وقتی داستان زنده موندن مجتبی رو پررنگ کردن، داستان مادرش رو هم تغییر دادن!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5001" target="_blank">📅 15:58 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
