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
<img src="https://cdn4.telesco.pe/file/QSw9dBg0fNu8S-6JmttgUDdGuFxL7M3uG6DKa-xcgyQMWQle8tgz3hdXa13Bk3euXhgpQ2yRrTO1xrGC3lKtmvv_kWNIyN99ZPt8LRkX7Hzsh4JQzVi98GKwHu0lKOyBAHHjdArhxUs9J59hmC7PgQ85y3TH3jEGnh9Xvx_lrb7gSucDp44sr6Me1w0G1HPqPIz3vfsEpIM_HUQkhkTha46GLvTw1jUZEWjFf4e1DiXjdorxuwEAHIQSG4dfKeeLtjGBjEhpxTqLnlzvXw1Vi1qIvTReG1i__LpIrArZm2uZiRRrYK0y7rII3cz7W4dSeS5TS_6PK5qgSslXwLLBbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.2K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 18:02:50</div>
<hr>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=Ds7v7nuI_vXaSB3vMD_DvzvT1VVQzPrgU4RvLu3Cswj3hZZ4z6SFTxXkfIVXWWB4MYqal0sNdgrcY8oUfSSBuaZErCZk77au4DJPuOTvIWUDXpZ2l6nIGULi9xS8vISh3bJMNgVi16fR0dokLijrxziNSbLRolEKpEgpPvVdaQB9w9aGjuNE8EcgpdWKplRGloFlyPuLW0EC3nr30t8My_O-G4HbwShNyV415cCoZiABwB1-zItkFxWe2zantWryBTjtQarP-w4ZKaULk_2-qtxbjtMIIi2g86LwaeUlA_mpLDvj0CrSrwzIERj6wpsX9sA8xzWxQdU0xUTGQAfj1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=Ds7v7nuI_vXaSB3vMD_DvzvT1VVQzPrgU4RvLu3Cswj3hZZ4z6SFTxXkfIVXWWB4MYqal0sNdgrcY8oUfSSBuaZErCZk77au4DJPuOTvIWUDXpZ2l6nIGULi9xS8vISh3bJMNgVi16fR0dokLijrxziNSbLRolEKpEgpPvVdaQB9w9aGjuNE8EcgpdWKplRGloFlyPuLW0EC3nr30t8My_O-G4HbwShNyV415cCoZiABwB1-zItkFxWe2zantWryBTjtQarP-w4ZKaULk_2-qtxbjtMIIi2g86LwaeUlA_mpLDvj0CrSrwzIERj6wpsX9sA8xzWxQdU0xUTGQAfj1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clzQnuBVQiCufGySCrFOH6gs1_PI1Tz_UmVg9ED245YEwKlIAvNTpA5s5GTthKfWytFaEQl4YZqvtoJuakV5tlR8KlEX97JYJ0aZ_r6sLoZQyFP7MjdJVcxa_Sjo9vuZdrwACsVSf56x1KJsM6d0IiLIJmvOYGLXR1ykYljq0Q06-MCzCV_iGePwxsxA7t4qrrflglb_yjtpUcw6pd40wknt_cTWzeRlWLbdx7gJc5QEDvM5svHBA8hEuyfS1MokgMrvy-oPIrv2nUbhSBCTcKigVanubQkVXKoEa0cDa2XPv6VndHB279yubEw8jvHzpogcTPo-BgwMPaTetC0jog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا دولت لبنان، پارلمان لبنان، ارتش لبنان، از جمهوری اسلامی کمک خواسته بودن؟ چنین جنگی رو خواسته بودن؟ نه!
آیا این جنگ به خاطر لبنان و منافع لبنان شروع شده بود؟!
نه به خاطر کشته شدن خامنه‌ای!
آیا سلاح حزب‌اله قادره که جلوی ارتش اسرائیل مقاومت کنه؟
نه! یک چهارم خاک لبنان رو سریع دو دستی تقدیم کردید!
آیا جمهوری اسلامی از مسیر دیپلماسی و از طریق ساعت شنی باقر
⏳
می‌تونه آتش‌بس بیاره برای لبنان؟
نه! نتونستید!
آیا جمهوری اسلامی با موشک‌هاش،
می‌تونه آتش‌بس بیاره در لبنان؟
نه! نتونستید!
پس چرا جنگ راه می‌اندازید و کشورهای دیگه رو‌ هم‌ مثل ایران به بدبختی می‌کشونید؟</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGF3RByOIpIUgJDIy5SxGzOweFSa9ha1gWyL_6Cte5jOo9y2E619PekR5CzGCF_S4C_iWX-_W5sIjnxtZLTDOK9d-vjVoSwpBQxIRSRkyerPu8Ap556dmF64R_pqeF8OaygDm8LxJNfjh8MUiKSzHlISvghNP2KgauHP1zZcAisqA-yaEh7O9Y7aHMmEinxvq0xwnQY4lDOkloveDJMrx8bZUDyFDzfkkkmxOPXlJVZ0Qffc8LpRdTSd2bM_lDcoY7ltgyHF0kkjkNpZsrM2PgAliOl4QHO-Z88NoAz75VkxvRqSwuq-MUVcF752nsmWYjCzUqTtISlPgeXsRsi4nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زمان شروع جنگ گروه تروریستی
حرب‌الله علیه اسرائیل در خونخواهی
و انتقام کشته شدن علی خامنه‌ای،
تا دیروز عصر ۳۶۶۶ لبنانی
جان خود را از دست داده‌اند!
جمهوری اسلامی زیر فشار گسترده
دولت و مردم لبنان است،
دولت لبنان سفیر ج‌ا را از خاک خود اخراج کرده (گرچه سفیر در داخل سفارتخانه مونده و گفته نمیرم) و هرگونه فعالیت ۳ پ رو ممنوع کرده، مردم لبنان
هم این جنگ رو از چشم جمهوری اسلامی،
با پول و سلاح جمهوری اسلامی
و برای منافع جمهوری اسلامی می‌بینند.
جمهوری اسلامی اما قادر نیست آتش‌بسی
در منطقه ایجاد کند و حزب‌الله لبنان نیز چند روز پیش آتش‌بس میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات
موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور شیعه هستند
و عمدتا به سمت شهرهای شمالی‌تر
چون صیدا و بیروت می‌روند.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ne5VXs8_ybH8mf6UEBsxaL2pYoMWWo5IrH0pMm18xD9Vorjb6QWPkECZY1QmKo4CCGABwVqMLk19yHMx1f26k974K46bNvbaW1z6g_Hwtfjww_ISMeynlsnMnnbinnA5NV4yB2fq982lgO8hEk82HiUQo_rfnY7MGq_FX0_gUud8XvbyztW6v5YbwbIOgCULdDItWJQPgdnox8jSrMU4GzOJPqd0ILtdxcBMrAkuJZZYCvrBdl7ukcCztg-6nZxWGPTiPAuJeNjcOY94XZ47WxJXT7DaRkeVU6ZjgX3brljYIftAM-L8nK_NaHA7M1zCTiMCLCvMZlEltk4PqhYiEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2gEVfDNi2P5xJPA2jdHSxi6kPrADS7Rw0FjMf8Kw_jBsIr1zpJ3AzY9Mp-KGll5pSEg6ZRRorBXzaShFb8dVFPOHgayUIEZHRdePB5biqWNgNXqN8BVEoJYw5XZSekqnMaR--rXvpZBflwZQ5xu5Wr71jK37mCHqjJC4yjRaUQ48vjDHTHEYq8jZsa5tjPubm_7HfyIZMryLotBz3jdMcx0bcbnpX5-G4yehipWpWgMmsu6HTlJ7vI-4BLJFbQ3KFi0HHGRc2EJeg5wWaK8TVWCZhpzNizbR6QEWS4OxsWkOjjOn3X5VRxnr3_WnVOclNKVcxe5z-kAyQKSo-vk1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIwqxjJT6kVpK31KpdcD4eAm5Cw-34XsIZWpvyNt5PYyZQF5jkX--RVMjGdgpHT0uVBXWxCIxiJCz_pWPWO7-wrFPpIo369KzHc9f3BQe9Qv1bMJmERPlKshwopVfCIKjnB3poVTmTc7npnmIY-EA_QMUdRw8c5f9puNCk3DwXpSy_A9M17wCQb1FP8tGa0JiX7VLITnCWMwk6kqap6OpwqqgWTrkHwhNGJ_wmNcHw8v-IH7t9K_Fy1eFWUYSLrN01oly_oocwDKaOxzdqtuOnpQWyOfYD44Bgi-ltjb5Nfu3tP_66cCshhifM2g1wibrStfPRi4VRoksAFYfpKRqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtXZZ18k6CXgAGabiA5BbzzR9Dd02r_fglbvXEzG5TgL9XKO_BP-IIwLPvuB0xHmpcQDFXkJNVTPIyfwNLde5Rzj5JlIvctpUg3zZzZ2DOhTktGFWjkuFKqBJPPAswdunsNvoHi8VQi1JXThfMbKcGQNBrczufYnl5MGRJGAaSawElp-UYBHPuysH-B0WP40vh9-iHTA3pDaQAdg24Uqg-WAG3hXzlpUn6eht-qNKpu5nscuBU88WvSB54uY9ESc5rHWrKXLpTMr-e3XlvITsydRsnFWLmluY-K-cp2rh6bjv0v7xZ21lDw7aOcNKWN-mP4xsNkK9sBSL_d2l7R-zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ac1rsWVa4vuw-tJA698YvUTjHCJ3n9XLL-eFKBuOFpRLbolL0nUM1JHm9FsMbf_gkqAMY5P6xGF_lAURMLJoR94fboXyv0KLH7JMEiUGgWoo7FwASLNR2BQyBHjsMOh-tfqEPBYE5QYlJA8qfAFzCQQcIFTyeZAdtOLN73WI1k-wigcXccWIVlJ3M9xe_9TdNnE1tl0DmkU2uMRGhJ8f1o-3RxcnZGCYV8gG7_dTXUuhkYw_vlFLBwkMmIWEIOZ0BJLSNao8LgtTC4kdfLhLZ3XQfEXLAV1-s1DsoH8Mt5PmrX7Xe2_1AY9sXkTQAOyu_F0b55tGUBZV8BCWF9pDOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7W4UWAWzom_YpDm639DqpB51nQ5AVPULedmS51YdGfqkPbIA9PuXu2mPltk_9VHf9XaUgYott_sNnty42D8GAwJ-5Eyx8j4mSqqL1CV1Ib-3w3Rr3IiMywkxPP1R1WeFx5EZ5IiqNwTarEqb-E1cKXHiRdWMTxMrHFbYk7o7MgVqTza49ZMOJzZ6PegZsPVqbkXNap-U9F49GwXDtcVEE1VPcby_t4PMrRUAlAZQ-1rmth569xYYVSn0nc4QikeN_uNQI99lFsCcujIy0QrmD8s5QtPQORmVH141Tw3u9IcozGPuQfmo67I73_HuzCCyF1l934EokzzzfSPHHztBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته ارتش آمریکا، در پاسخ به حمله به یک هلی‌کوپتر آپاچی خود، مجموعه‌ای از حملات هدفمند را علیه ۲۰ هدف نظامی در داخل ایران انجام داد.
تمرکز اصلی این حملات دکل‌های راداری و تاسیسات ردیابی و نظارتی بود.
ارتش آمریکا با نیروی هوایی و دریایی خود با این اهداف حمله کرد:
بندرعباس
: دفاع هوایی، رادارها و تاسیسات نظامی
جزیره قشم
پایگاه‌های نظامی، ایستگاه‌های کنترل زمینی، رادارهای نظارت و باتری‌های موشکی.
سریک
: پایگاه‌های دریایی و تأسیسات مرتبط.
جاسک:
پایگاه‌های دریایی و نظامی.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0rdWvRGjiDN2SnkBwEcXj8SbC0wWWZekvVKibebNMqUL0t0FCoSenR1HERP2egZamxdZaZOEtOu2x3k-WF_cKmcohdS7Uys9A1ZLQcmG4vuZdaRUiTVtzmpuaTRHFA-DDHiaww_LHyEC5aOS3NCRa56YKff4TeCrOwsB17BAP5r6oUdFRlQEFAM5L5UFLXAUWykgFTrdvzAjtpD2JL4194KopF3EQDByI3fkxyx-32F6E7c1bMx9idc2oCeQwMUfmfYAIx8FW4WPKENeE22OUeX-cgBBteqQbn8a9j1O6Le0Pc-1RcN7gpTNJxGnmPvNZGETBL3fE1rR5T9eH1HlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SolB7PBRxyYPePPAIqSmqAoOpnLRZyvDjg2YXQ-WuMmwD5rtZx15M5k-kwRq73ktQolZJPdMi_AIyu_aCHvGvtStD1gSvLX_sWCyKaZRugC5eiVn9eStNTt6pszZs1vTXlEGvWvcd4QJaroZc9yf8jVfVrO7UE2jq7RKxWpGykqTeRmlvtgQOJ1n_Ma-bIoLehAz1PKpwUrjtedaXd2Z0W6pLPAGt8thkP-uwOtK7jY9bQ_1rlf4QnWrbHW6w4KojW-JMQ01P_3bnYQStScW1PLWg023Nh5pyGYN42pl4OiPkAyFndZ7yGxnIdYZGikNIJscWlVmPC6UVvg1eYmXGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=S0_mR1K0eckCaLlVmbY5rX1BWAb7Ke59sVNHnNWbMLZYuieta9xn-e7fGLhxevEq0XydSbBFuEaT51GIi5szDaLHCUA7m1RF4yEyXOslYYVzvO8AUGo9OktRmOp5D_6sSap9WMwuJOZJ68yXaaqQJJwPHqFp-LU8JvYBZVTh44V0db_HoBMvHJS5ZeFRxiRGOeaECyzd1ftdcxCJHJ849Gh2I_7DD9MiENlM0Hdj6gXMHWA_GEjecbfhcUQw0Z3-Lp-K5NT1sM9jqpF-OksuCDLXUBOCIihZRwUZ96B5pz2X9--i1NwXAPso_74_FXFvk4iCMRO2hdMiGPZ9J1lV9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=S0_mR1K0eckCaLlVmbY5rX1BWAb7Ke59sVNHnNWbMLZYuieta9xn-e7fGLhxevEq0XydSbBFuEaT51GIi5szDaLHCUA7m1RF4yEyXOslYYVzvO8AUGo9OktRmOp5D_6sSap9WMwuJOZJ68yXaaqQJJwPHqFp-LU8JvYBZVTh44V0db_HoBMvHJS5ZeFRxiRGOeaECyzd1ftdcxCJHJ849Gh2I_7DD9MiENlM0Hdj6gXMHWA_GEjecbfhcUQw0Z3-Lp-K5NT1sM9jqpF-OksuCDLXUBOCIihZRwUZ96B5pz2X9--i1NwXAPso_74_FXFvk4iCMRO2hdMiGPZ9J1lV9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrwjbaJ8NXFmziyMSGvI7r0L1QJScH8nb68dW7A-49S1jgqYSt_t-L1kfeb5AGQAM8pFt2IMY3kD6xr0aiXN2ct8C1_dzrfcTqOMageb3ZMpprnlv7TtotWsHPFXWgBM36DG7TPIdvWsFh7g7pY61yPPUw3ETSdw5mi6ODYYLxNixMFALBpZqwsTWDViChUlVZnOjKR1F1CT5vVJaudGdQL9uPvVSJJrFt8Qcn5WGMv6zkVYAh9hAYR_b5y-MLboPezbcusoubbrBEpDB77c-BmTwaPAXWLhO0Vt-5u0LFScBDPGYNq5lljEZuSf-XJyAh7Awq_oHD6WKPG924U32A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارتش اسرائیل از ساکنان شهر صور
در جنوب  لبنان خواسته است تا
فوراً این شهر عمدتا شیعه‌نشین را تخلیه کنند؛
شهری با جمعیتی حدود ۱۷۵ هزار نفر.
🔺
این هشدار شامل محله مسیحی‌نشین
صور نیز شده است؛
محله‌ای با حدود ۷ هزار نفر جمعیت.
برخی رسانه‌های اسرائیلی می‌گویند
که شماری از اعضا و فرماندهان حزب‌الله در مناطق مسیحی‌نشین پناه گرفته‌اند.
🔺
در اطراف صور چند اردوگاه فلسطینی
نیز وجود دارد با جمعیت حدود ۶۰ هزار فلسطینی! آنها هم دستور تخلیه گرفته‌اند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5444" target="_blank">📅 14:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsoBfAP98IhL68f5_-7M6NzRPQlRcLAk8dH0U-QTOQiieKdSKCpZhuNGHUuey2MT32FWdPwwXY49wNTDpdVkm8U2T2DdnGbY_Q9Wlc2v2pWcWOJHGdtqqVEgPaMgK31JuWfY-c6YnZSxNIXnNNRc8mhxGaEEUNWNHHkZyM3zHAyf5EPKh3lnmRxZUTtju-S1GiSS-FGVi6Nhe9pYXCk0gRfzcaAOIM4-55uGID_9oyytX7DnJcNeQkXp3i5tswGJvG6kbae_hVpuhVaENNeHScOSgl5YehX85K6UyvGeKOrVKo06wVrT9tsEynMoj9XWM5Ahd5SWFPl7-xAjcakTDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در حملات دیروز اسرائیل دو عضو
پدافندهوایی ارتش کشته شدند،
اسرائیل گفته بود که به  علاوه بر حمله به مجتمع پتروشیمی ماهشهر به پدافند هوایی نیز
در چند استان حمله کرده.
درگیری اخیر در دفاع از گروه حزب‌الله لبنان صورت گرفت! جمهوری اسلامی با حمله به اسرائیل میخواست مانع از حملات اسرائیل به لبنان شود که عملا در این زمینه ناکام ماند و منجر به حملات اسرائیل به ایران شد.
شهدای دفاع از ضاحیه و جنوب لبنان!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5443" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=ppealKn6hv6zZoh9UWLJhQYW5e6kEh7LwsbhJ9T70ouvAcD7mAaWMDoerp68OulH3sI8ngdUTkGeogdkot8jWF_CwySNTF4X-gv6VnXABwa2QXRanN9lNzFdNnTO2Wdlyz-NKuugDlWyfa-3tcVL2e4Aotifx8EEZ9r3qKe8mV9_m_qjy0FcG4iBo3y6ebMiZLg6cLxSrFDMRhxAA8rz6VMGoCiyAbQ20V4cm22OUJf8bmofX06ftMHZaXzZPWYK7kDsxaEV87FhqEBt4jtwLzkBI9JYONvclJJSIRZjzakFUH3Y-uRKMS0JCkM0A_UQuFPjFAeY9dN29IIUe_kxFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=ppealKn6hv6zZoh9UWLJhQYW5e6kEh7LwsbhJ9T70ouvAcD7mAaWMDoerp68OulH3sI8ngdUTkGeogdkot8jWF_CwySNTF4X-gv6VnXABwa2QXRanN9lNzFdNnTO2Wdlyz-NKuugDlWyfa-3tcVL2e4Aotifx8EEZ9r3qKe8mV9_m_qjy0FcG4iBo3y6ebMiZLg6cLxSrFDMRhxAA8rz6VMGoCiyAbQ20V4cm22OUJf8bmofX06ftMHZaXzZPWYK7kDsxaEV87FhqEBt4jtwLzkBI9JYONvclJJSIRZjzakFUH3Y-uRKMS0JCkM0A_UQuFPjFAeY9dN29IIUe_kxFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0q6xdiXhq8HSqKLaIq6eqxoxPSnu_CbkiGOMmzd1v3FF-WBdgid1wtWxnci-DOCYpcv-nQMX6oKPqd_lyfl0pqLxrgh1nsFHS1lwpbEHFjq8gYVNx6Wf3kQtIgLAWTByjqMZd5jN5y79N9oNjDsZkUZlLqFXndEou8c3TF2jTkEDJIF7ogDhJW8eGwDtQNXe1iKpCPKtpZpwjwoCOFao8iIrUBsGOSi9c9C4mqXTFb5U_3JbJO4u36SRpvrWtTLz_5RWCPN10xaGF51FYvLs7ivRH-g3wfe0sOPpDSXF6sI0vZNctWzBSns3LnB6TDpC1zjjXz_d8nIA3zfPrQ9tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HfHNvFYUqXpMWAEInPnfcHX9eDUiq7feyGPqB06NvPfUnUdj00Y9iM4AFjxahzDA8Oq7gyhihilEs3POku-ELR040sj_bbsxTyBL6cGq3dxuxCqpZxI8oBsmlaFA_ZyKs1t959Ace8mYpRIiAnw6JGC5uVWhXZWsnvj79YpJYkd4-z32G8BLTDLzDVRdhBK91M3HRlU2DmyCL6hFEwtmP_Ugni7v1s0g3_IqJMVkzQqSly1G6ogbpz3cDQ4m9nwQdTYL2vqFYfxfzq8lF3TSQWakVMwz5vnsT7SXmTHns872f_diFzfpkhqrGJAv5tdb9MwrCI82t4lsPZPbDCTCag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=LeNtc9RFfAHmzjrq48AORJxhP2iWb-HgGWcz9NtSqWf4NNB62nKbJl3rRkAsFl78e3_KeESlkYfdnTyQbEZUG4C0rJR27fMYwRiqYAu9weeGYxFA404VLBAVC--z_Z9iD__a5yNFJmbBh2tgYEdWUefoWTqVKjtpc_2SsqD5YjdjG-wW7Ah1sd-QrSGMLFe8H5rsMuhpujtq6WaquiePLONl5c3bkPorSQ5ZmrisJu3_WVZZPELvMDw7gxxLXx2137DlKZLQItIxi4YDhwLOoJUSMSkPBd-xhH8mYT_lmgzy0480m42zAfyiO0cskycvzf1ibNZnlbweYDYRgqxxZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=LeNtc9RFfAHmzjrq48AORJxhP2iWb-HgGWcz9NtSqWf4NNB62nKbJl3rRkAsFl78e3_KeESlkYfdnTyQbEZUG4C0rJR27fMYwRiqYAu9weeGYxFA404VLBAVC--z_Z9iD__a5yNFJmbBh2tgYEdWUefoWTqVKjtpc_2SsqD5YjdjG-wW7Ah1sd-QrSGMLFe8H5rsMuhpujtq6WaquiePLONl5c3bkPorSQ5ZmrisJu3_WVZZPELvMDw7gxxLXx2137DlKZLQItIxi4YDhwLOoJUSMSkPBd-xhH8mYT_lmgzy0480m42zAfyiO0cskycvzf1ibNZnlbweYDYRgqxxZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شدید امروز اسرائیل
به شهر صور در جنوب لبنان،
اسرائیل همچنین امروز
ساختمان پلیس دریایی گروه
تروریستی حماس  در غزه را نابود کرد.
جمهوری اسلامی جنگ را به پایان رسانده بود
با این شرط که اسرائیل نه به بیروت
(ضاحیه) و نه به جنوب لبنان، حمله‌ای صورت ندهد!
ویدئو : حمله به پلیس دریایی حماس</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5439" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qfDX-fAYzCGSWfZy_kKqMJJxqaNBzDDJckV7oKbhwqSjbuNmHk6jIbepz30y7A4CY3Rnduz-FsUyKFeGYEJzWoTTv9DAaVqs3UvDS65myWHQ0kLv8NYeiFcKnTGdXO-5QCEmtOeLCrFC6ierby9FskXizXPc2J1SZ28_-ak1dKnD3DaDerN_mDVW6yGr0lE6i8vGEPVbAARhKD_TyuhpXLqM8T9qADVnl3Rq6Mg-XZ61ceaMNPoT8k3KBS0L9auq498FHIPloifkndevRfRrJZeM0Hn0qkLW7jDU3Pa4u4_HIEE2_geGF58tAleK3IuA7IPaFFGPAzao5v5tGSz2dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vmImM7uK73nmEy0ko51CxeRlV-j-x5o3Ru2JsCmEi41hnTXTBYppl0TqXupoEviEu_kewFf8q3EGVWia-1YXdqrSauQ7FFSKGbtK9wbbQzU87ECCXxs0P2ZcGg54issxWArVUXnfuviVwxNXSnNwinx8m9ko02BVGlUJzlh6p1GGOwSh1nWrl8BBcW7efw03vTHubhXhU3xQ2-W1YYCnpbJiISbyKkIc6hFF9aHIQ_T-ZhceqvCzWNV8zsYYD9U9-CArk1eJkHAyInD4bgeMCKGi9BHny3Ex4p1Onxf2Z2WAphkYdKFBeWBqNa3R2l5J8SQUXBRyU4PqzrXOCv7J5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=LhppC-rHCppsKxPVZsrxx_eKzNd8xB-aGElcJbaRN7pVmGFElnSSa2Yl8GqReKBzsuFX0RUiyEi6Nv-GdTY5jMeKQ0NFMAxid0vwpvAEBFHVIMG8XQOK_SGknOH8n20eJQYZOOeAFyQqEtwvSC5vwQxrLaAhZokK83zLIgjnsM8iHJoiyYgThUAPmwRuNHCJ44OSNi_rvcPUGuTT4JSDLA5AO6GtDU3Qya2tHsznZl6oITxO3S05J6nrxdh6TVpO6znuf_yLj1FbiMvLHt6cKKZmmigmgd4GEA-vONxgI7VjK9JIFsMrl_eOE1ILVmFnVPeaG8kXtiuo5gorRg9gdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=LhppC-rHCppsKxPVZsrxx_eKzNd8xB-aGElcJbaRN7pVmGFElnSSa2Yl8GqReKBzsuFX0RUiyEi6Nv-GdTY5jMeKQ0NFMAxid0vwpvAEBFHVIMG8XQOK_SGknOH8n20eJQYZOOeAFyQqEtwvSC5vwQxrLaAhZokK83zLIgjnsM8iHJoiyYgThUAPmwRuNHCJ44OSNi_rvcPUGuTT4JSDLA5AO6GtDU3Qya2tHsznZl6oITxO3S05J6nrxdh6TVpO6znuf_yLj1FbiMvLHt6cKKZmmigmgd4GEA-vONxgI7VjK9JIFsMrl_eOE1ILVmFnVPeaG8kXtiuo5gorRg9gdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOA8yYf_rZexk4qlcBwtxo-z8nwB2xZy0flfdjO3FeP74y2U2VG9lU3YOg2ePFuMNNNZA2f6Z4wCqhKrI4XWaaYuEliXMvb5WmxR7YCz09KNVzRhOe4rfBxsubvwgcqZ9-ACmbqQ4HVm7gwVGVQWnFq7G7kGFc30sbkBb8rs7E-hiXP4wslCfhna1flVS3cDu5Dj-5HU4CIvGAKVaSNcVxbEZDNMC-2_Ou2PNpY2eFtdwvy0kpR9N8PPJ9-pn2h53hAdm2RJ-_aJKdCFRe0z84eerj5do1gyK4ljDvSKzYWkNes6pv5GiHGjmYxTbEPGsUkpCx3Bpu11nZxDPLjySg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXe2IfjLk7xsmGj_iJ7xxRneIj_NZOiubCfo7q1QBbiooeSXLd6w593Chl-M-fMUss0Ie4oMY27AQbgkciGDhOaMq7fs3SCUe-tyEhX-FmdOUaI1fHDPNbpT-AL0zPE3McQsZNFS4i7Fy6NLxB8E12Zp2v26GwLLXcrhzS7tRCdDX_cnKkfCg-XkCp8hnlcmyomcuLabmU8rzJRn6p6b927YewLUT2FtKB-CamehTfD9HA9KJkOfuw8QGCL1YaLM6M5BgUJJmdIqX6h-oE1girz3yuzZDe8ME3oZ458nwTxlrqSai7vUHasuTjuNjEq37OhVNOmunodPqB-anGyZ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqnavT-EAlePkNvIggnxKFWdxeKwNFEz8v7f5Evx7QMozbov70AM72aHXK-jGK0Y54TDQrdiUfdLg1hMGiKHG6UIjEIVYuT9GfRJmDwafFBdpebZqhCmPaSwhSfjG3mVnzx1GwEks5NIv8023fNPcAbEZQ_UvDANWHHMkOzVSBPYgVGBVFJMEst5OkomaGmidtP16NulseQs3GnNXPidrVYRJKk4kJNoxgpqfJT10zl925iG0i447lYHKfBPHkfxIbxHmM-vDqmLzyveF95Pk9VHDKt4ubToUKu1m1X53mzHZtRAwPeoHeOdkSdGlY_Xndom9OdMxIuuvPPPWt3zJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sSQXUeC__aV0RAxmjpKfYyTc_vb6zlWbDWqr4649SuehX12tbkZHc5d1hXovLaaeJm3HyHCVrcgF9pQEj2e3YFd11d3nduIRfhuhzT1rRhhZ58mPTi7pEElPmy8_IesPiuWOBbur3-dphI_ySwCScbAFyMm2XSbYUnWlvr2w1F97aV8SfwWuulXgWdf92T0tcgbVXPPTO6rJUvyo_5TLr-0IKbHmXVI5d78aMYDNA6Lld_rjLtOOGrFhlztM4UhuzdzYRzvtOmIxgKV0_u-YpDPIKcUlckN7mrEE42c2F3JvyeZWAFsS8VKQRdSSMVYynQM-IJyAXXg0Dct9Ac-STw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/by6dlQPwVjPJDLAlPbk8vN-olp3r59uUeIrhwNVgGP8pnCtzDpzQyvFa0TPyUArYosvLF-ti5VJY-QGJ75ettyKaCqi_b-w7oDmkwXcmRH7ZslyQraz85eyxkVlkqoaK5RACtB8LYpXg7WukOWuFfsD3SfqmBE2JMWKHO_Ldn_M6RGT8m87RkPZCv2X4xC6Ah9xTE0qTYBNvWU95EcuuQfG8xFwWQzWNHrgw-PYc5hMSuT-iXpOPB0GJaQG2pyN-qApjVuylzbK1uagW1CWxf8UiI0Db1_PuhTv4SQKT86HVlqNX8cLdcXsScZJQ8TxXIKU19srH1sKWn7q4ElxKtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0Hi00hKfv_vzCHGBi4xhgYrY4stlcq-FzXQHiZjfKapJn1UEe4hBs604BZM4-VP56gS1zGFfaWdC3PpR2KX71_IUtLLyFL_GuNIq_nXgBdQtns-rbOFUNa6eCKvf6ncnaC68wmhQBfoyRImS-VNMx7s-fPcszx8jcxYhU7N0R9Ft5uIFw2dHbFO2FuWWSbVYNAhdehMsC_Dh3M0asgPm5LvlfDAz_FEzmwkRTLyI9tU3XUcl-nYowdU_67_IZIphc_Bdnh8vQAw8g4RnzS2zMzwhY62uavjYSDIFSSMIS_KMB28_BjfQnFjfWLkj-v4nCHflSQ8APM1G7QlrVj6Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2Pz_kO5gJgwnBJnTliTkmMIKPgQ0U9Hadgqmq8ACgaeETN1kCRfs7rLE_DbXC-QbPORX1MBdJLNCDjwG2rAHtHyflu-E7yBn-lpJ7BvzkkOzk_F5b5p96YEVH0leWxmSAkC0kZcrvSr11zfjqUdjmBXmJ7Bnl0p_XJ1Ti9hg0Dyd5AFEpN_otmvPY1Nwddo-1rX7VBGNmE5mA2nU6_w_wRB-aPhiKksynDaV4Vv8qloU3yjwSByT4bzNwsUBVevVOGboP9-wPHEZAbRVPhD2zf7nTFejgrLFLVgE52uxg_AITbwEtC5B4goABsYIaDWtCUwRSJxQ9dLResUrYWNAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIWGNoXlOEWwxpcuzvOe-J-HVtNQ-MllLw2WkIXwEhGAaxk3Mf8xMvctOBkA8lK7MZiKfzl45ThF1DYicf4Hx_qS6meXpkxIp5JElGIVcHl7HhMzuZWaL7fPVDY63a9NVfOnRp-rw71m1G5poDmK2-mKkFQKxnN6HgUn5cXsCGbX3MVKS8GoENNCqjV7ykfPP4Sf9nFCju-5sL7-pfLPtFtAMdOTld96mUJAcZj6SGNwL5dWZOJWcUFJ6_6fFp-SvKT2CaGECUvQXsVKox43FttLNbi_Kp8BVQ5p_V28MYNtcDDMkK6iLldPQsGyZlJ0WHLewSKwmaTyg4Fsjo-1Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=QyDofGf-hGmYRgbyPj9c55Njl_41lX4iWh-mAIkVwYZYUypQbnLYrxOzPMqhdr39yJizm5LuZGMeUxHf1WmS2LIc2yI_wtfnFPzpFGunYjjEOU-fjHqbPsClL0Llr9j6SsAqmZb8CGbYspOgny-SHXdepUS0GOGq6S37z-Kx6nWNt0erEt0oNAgNPKeMZGu3kESa1PXh6Q-QmjpCnEBSCDR2SVhyh61EZywiHMB3ACIbwNfdU4N3AvgHJqdYxfOJwyQ7XVaak2wziqj9Y80uovMkeI_2z9wikyTj06GzUBwf9YIZUFuORnop4-K3asQ16yigzg_rKp-756oXpvV-_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=QyDofGf-hGmYRgbyPj9c55Njl_41lX4iWh-mAIkVwYZYUypQbnLYrxOzPMqhdr39yJizm5LuZGMeUxHf1WmS2LIc2yI_wtfnFPzpFGunYjjEOU-fjHqbPsClL0Llr9j6SsAqmZb8CGbYspOgny-SHXdepUS0GOGq6S37z-Kx6nWNt0erEt0oNAgNPKeMZGu3kESa1PXh6Q-QmjpCnEBSCDR2SVhyh61EZywiHMB3ACIbwNfdU4N3AvgHJqdYxfOJwyQ7XVaak2wziqj9Y80uovMkeI_2z9wikyTj06GzUBwf9YIZUFuORnop4-K3asQ16yigzg_rKp-756oXpvV-_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله سنگین دقایقی پیش اسرائیل
به جنوب لبنان،  بخشی از هدف این حملات
پیام اسرائیل به جمهوری اسلامی است
که قادر نیست با اسرائیل معادله‌ای تازه
در خصوص لبنان ایجاد کند.
جمهوری اسلامی با حملات دیشب و بیانیه پایانی امروز حملاتش، میخواست این معادله تازه را ایجاد کند که حمله به حز‌بالله لبنان مساوی است با حمله به اسرائیل.
اسرائیل این معادله را نمی‌پذیرد،
در برابر حمله به ج‌ا به اسرائیل به ج‌ا حمله می‌کند و در لبنان هم از ج‌ا حساب نمی‌برد.
گروه حزب‌الله چند روز پیش آتش‌بس حاصل شده میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5421" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYszJDxZj0Qmt8dyN-8L7nhEO6chsCMZIiv5k43fhhaY_snKmII2gn8-AKf9EfRZFnaledGlHNwu_1I_bO77iLNbcta5KxwzgzHQWzjjdFvAqzK64Bv3sr5zYsLzAzGeMuegwWl2Q7efjRpd3t-BjkYEu8mmkZzfuKjbRPBHIxPd0iRiM_A8i7C9T25W74CyEBHRXZR9H0xMDZkE7q40MuvNIwEMZ3jwFCRRTlwpAWIRTv1QoleWj8_jgYvhJ4PwzyhPLmnU35UDECtsjxnT1URKxt9vYAVLASEPV9M_QHW-sYe2RKL3AbKfXZInx7onYV4bZDOHQ2gSse8EDganWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=sdUgPCh4eS0hNWQKvSzBVjuqR1px97Rob1gaa4iEHJ9cNLv_oGqivmQXMAT0xqE3lu6qDo3_zQwZDjtd6RItJvvf8qkCtcAoMKRgCH2Lacs1JZ7ENYSErEifNrSHi4f5kyw0FhqeRyhkpnL7dhKGSGxU5keHObgwG9GxhHNIJp1JJQWQJEiXYJoaOJYAbdKkGgjkI-_btdufMWCNWtsb9tDyaOvFkqK4DvgEBsvxm8dTSE7Y58bSLlJkBVOgkemrl1cVwWRAUf32z4gM6OCgWQUKo8h-iC2sj8bQj2TovaQy27TT7gC4yNtdvRXyQhQ5LM-VRFjT_zm0EYuHBmz1wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=sdUgPCh4eS0hNWQKvSzBVjuqR1px97Rob1gaa4iEHJ9cNLv_oGqivmQXMAT0xqE3lu6qDo3_zQwZDjtd6RItJvvf8qkCtcAoMKRgCH2Lacs1JZ7ENYSErEifNrSHi4f5kyw0FhqeRyhkpnL7dhKGSGxU5keHObgwG9GxhHNIJp1JJQWQJEiXYJoaOJYAbdKkGgjkI-_btdufMWCNWtsb9tDyaOvFkqK4DvgEBsvxm8dTSE7Y58bSLlJkBVOgkemrl1cVwWRAUf32z4gM6OCgWQUKo8h-iC2sj8bQj2TovaQy27TT7gC4yNtdvRXyQhQ5LM-VRFjT_zm0EYuHBmz1wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=j2hhYNil74aBExzHpKc7nxImMpjURqezMqsVG-VUA8h2cWD_CwWmS99gLtc4cT2-Jecez4rx9zDUMIoGmFfKJTiuS8J_wL8PSKNCSbbLgwkkvUEbAhMNP2eBC0D2iQAPOlE9Gy3aTArVRRpOlLr3ejjBVLCPdOKZoNJlqQFfPk5RcjCdo1ZmIs9uGzGBj95z8BJh23B4jPOdY5zPY-R9mG0qXafs-68_n1g_xLWV_kZUpVGHRaP3iYEPE5TFTSyU1drDv8yhpdPfVBo5p52u5L39u6z1L9Et6nalduyCdALuiAVW3utNj_iB8UbtX82dg9zZso5n4gVG6Lc-WY9B3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=j2hhYNil74aBExzHpKc7nxImMpjURqezMqsVG-VUA8h2cWD_CwWmS99gLtc4cT2-Jecez4rx9zDUMIoGmFfKJTiuS8J_wL8PSKNCSbbLgwkkvUEbAhMNP2eBC0D2iQAPOlE9Gy3aTArVRRpOlLr3ejjBVLCPdOKZoNJlqQFfPk5RcjCdo1ZmIs9uGzGBj95z8BJh23B4jPOdY5zPY-R9mG0qXafs-68_n1g_xLWV_kZUpVGHRaP3iYEPE5TFTSyU1drDv8yhpdPfVBo5p52u5L39u6z1L9Et6nalduyCdALuiAVW3utNj_iB8UbtX82dg9zZso5n4gVG6Lc-WY9B3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=Hh7cuK8STLddzGJdGi44OPlH8Z5I4VQF8M4Rj-gNLqZsInEYWHxZAvJf2JdfTM-hrs_JstE2ZFq1Ywb53HIUyCf7GB19foOZ1WA07okfxViiGrlpqM1kk4q5hG0FAAy1TJhAyfQqP_SagV3qHHL1lKEjuL1nO3XvO7Jf9v0MPXnkXNioe9kRSOPU2LCT0GruEyDoYn0tZdN7A3LkdIvIj1saRYnn1w3xcE-l9dMxWzpqUyNfuY0EXtA4H21_MkZTUip99rtnPBeOEupDHzTchCEeNdUSliKSNYLP-LU5R3YIJuJhbu7zJsOr7PPohbfmzGe4a2v1j4W7qxD9UF-2bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=Hh7cuK8STLddzGJdGi44OPlH8Z5I4VQF8M4Rj-gNLqZsInEYWHxZAvJf2JdfTM-hrs_JstE2ZFq1Ywb53HIUyCf7GB19foOZ1WA07okfxViiGrlpqM1kk4q5hG0FAAy1TJhAyfQqP_SagV3qHHL1lKEjuL1nO3XvO7Jf9v0MPXnkXNioe9kRSOPU2LCT0GruEyDoYn0tZdN7A3LkdIvIj1saRYnn1w3xcE-l9dMxWzpqUyNfuY0EXtA4H21_MkZTUip99rtnPBeOEupDHzTchCEeNdUSliKSNYLP-LU5R3YIJuJhbu7zJsOr7PPohbfmzGe4a2v1j4W7qxD9UF-2bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BXFllFdHCBmXNreAEz79n8joRAOeIb53HJRNTKMrheT5auqQAytf-5CayC00pNCNmq-rJ_5mwvxaKGfqSPY0mL4eWBXctO4lzCL0aO_85fczJ20sud6BivOFJAlrd9AYqgYvZS26WRNrtj_uIlgXIHebxOzvseqb0dqclVTvLoHd-4j394hCHVLyI5UGndDy03thgeMj1Gsx1WriIYjoxbqQ06kbRYY0uYjM5cw_SXMc4TRRCV-PgHnXT5Ywq29A_X5GPp6uiFheEmgalZYcPc6CNgEmPX2v5sh1xSQplQKgktSueZktjlCxjszD0KbLbY70MLBi6yEA8dRj7pLptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F1Zi_HJuehty6QwRwuMSroGUE6o-cBc5tx_F-0JqPJOKUYuHgr8qXNBYPR4DsMApbjITGfDSl8dJEyECySXy13pItpG1F7zjku3_V81ytInYSuJJzoKOQsjhy-9tpiVmrC9WtXOLHJ1KcEl5kFUKu-Sff0az3xD-pyIbzJUrcCKimQHDnPNYNz8Bw0m53gEkWTvLHgke-LSCk95gVGPICsBVHMzYzgAisAUrnSodUhEUXOkN0QY9XIyoL6lzcE8vTaAO2e-IS8Ri7x4Dr09GW3kiDGg4hXI5XrQH5YxcyOTqjx1typpz30W2cnW_X4Rg8D9jGh59KqBJKvzJ4lC1hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=WY_4-QQtiUoxLSdMKA0SK5ovWRmCQkBcTLBx84C5i0mkel54MgMwnpcGmIeq1uMimDcJGGAeFaHLYHyJYBwxTNIqCdsVl6M0FwF1EFrCcnhgz6GnhIisQMj3TJZy6zAoOCgjJA8Z8buwdLk82HtNCvYIurUjjlyW8HN5b2ZH8GavedCR06-ICRTOHwbqBCldycZ_-nxRdTjeoImSciTYPKMPtjsADIocSICOSi0Qr2C1zv3h83lGuP9hyG_ua9btEXuv6L5Ti7s8gWCCIF2qRKtxk_4OUjWpMFKnXEhxrJ7W1wGgqhAKU_jy6hlu4cqH8zEa34lr2OzO29YXzIiM3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=WY_4-QQtiUoxLSdMKA0SK5ovWRmCQkBcTLBx84C5i0mkel54MgMwnpcGmIeq1uMimDcJGGAeFaHLYHyJYBwxTNIqCdsVl6M0FwF1EFrCcnhgz6GnhIisQMj3TJZy6zAoOCgjJA8Z8buwdLk82HtNCvYIurUjjlyW8HN5b2ZH8GavedCR06-ICRTOHwbqBCldycZ_-nxRdTjeoImSciTYPKMPtjsADIocSICOSi0Qr2C1zv3h83lGuP9hyG_ua9btEXuv6L5Ti7s8gWCCIF2qRKtxk_4OUjWpMFKnXEhxrJ7W1wGgqhAKU_jy6hlu4cqH8zEa34lr2OzO29YXzIiM3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله به یکی از پدافندهای همایی غرب کشور توسط اسرائیل.
این انفجارهای پشت سر هم مربوط به موشک‌های این سامانه است که یکی پس از دیگری منفجر می‌شوند.
این سامانه پدافندی قرار بود از آسمان کشور دفاع کن (با شلیک موشک)
ولی اسرائیل بهش حمله کرد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=iBOlAg05sNDjOBKavzi6uoEBo3ISF9i6taovCd3jw73syoaT4YAszHaVZESlVgXt8PzNZW-geQ0r3xI6Sj7vluuXrf67T5Nc12J7LLO1BkhxAnRpAu7lHZQsQtiHVE608iiLCZa5dfE3rTT2cipz6xcDwBDRwTWgQ50L0gwHziV2jWGn9gGkdsh9OZzWOse2DSd1EmX5t3u3p2XMGfL6CKw46j3PCkcGPesxru5PE-xiqMxCkL3PPCG1LwMZuqk71s0rpcLq5JUKV1_Ob9yRl9dcScvU4Pt01RUR6lUbcmvJG_WKuwUFDbcams-bMxKNHMqvO_M7E3T1HH4IGk2h0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=iBOlAg05sNDjOBKavzi6uoEBo3ISF9i6taovCd3jw73syoaT4YAszHaVZESlVgXt8PzNZW-geQ0r3xI6Sj7vluuXrf67T5Nc12J7LLO1BkhxAnRpAu7lHZQsQtiHVE608iiLCZa5dfE3rTT2cipz6xcDwBDRwTWgQ50L0gwHziV2jWGn9gGkdsh9OZzWOse2DSd1EmX5t3u3p2XMGfL6CKw46j3PCkcGPesxru5PE-xiqMxCkL3PPCG1LwMZuqk71s0rpcLq5JUKV1_Ob9yRl9dcScvU4Pt01RUR6lUbcmvJG_WKuwUFDbcams-bMxKNHMqvO_M7E3T1HH4IGk2h0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YL_eSrAA_LmvCVCtwf3ToPM1HEeAk0UR55_7mcLV0NGjl3mTshvr8yKGhMlalkdTLh35siO0a4mYBXWra5PmY8SWHP1pW1XTSeZoFmBE7onOjawYt-0_TF-Nn7QAo_O42cXXJGrhczTdor7kzQPs_vr2YBCCTiuTtfYZ1rc1mmT4EvggBEKPYtuyde2u7oQQglhT8p8xCcoqiXlHnaRstmwbTXPi_99-mfETarsxjkmooTBphw1ATueEF_LfioSVsGrXQN7FrtahVHrV-uXotWVyXNJER8Yt7aE8Z0iyuVNkfI96xWdzgFDWmvxvBK15fJUTKFVXWVMRyLvqZwDLBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=pj6IjTI0uypAGZZbPcAOH3w48BaiZOQJs2-Q5JMlnSbTqAn725dkv9iUf8GrhcI61EKlTmTabqiw61dQfsPxYNqir2FV6SO9LPIDgSd885-2pTzkqUj1wsZx26R2oimE1OhyOjgp_pad8xiiG14lrYw7EjcT1qAnbm6-G9MGXUl6JyvEj4yq1k07MrmzzSsf8skvlZG2apykEESvhjtcwEgea9x5rlQ4lbQUZbX5ktOoJLLpHKMhTfiw-mfW1Xp5cZiuW19QWz3OnJ7VuMMzpmK7FPc19rG0N86JamudopzZu3ZMzBL6musHOmmYUPqooRLt7TPd4KdF9XqdIsNy9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=pj6IjTI0uypAGZZbPcAOH3w48BaiZOQJs2-Q5JMlnSbTqAn725dkv9iUf8GrhcI61EKlTmTabqiw61dQfsPxYNqir2FV6SO9LPIDgSd885-2pTzkqUj1wsZx26R2oimE1OhyOjgp_pad8xiiG14lrYw7EjcT1qAnbm6-G9MGXUl6JyvEj4yq1k07MrmzzSsf8skvlZG2apykEESvhjtcwEgea9x5rlQ4lbQUZbX5ktOoJLLpHKMhTfiw-mfW1Xp5cZiuW19QWz3OnJ7VuMMzpmK7FPc19rG0N86JamudopzZu3ZMzBL6musHOmmYUPqooRLt7TPd4KdF9XqdIsNy9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط یکی از موشک‌های جمهوری اسلامی حوالی شهر فلسطینی «اریحا»
دفعه قبل موشک به یک روستای فلسطینی  زدند و
۵ زن فلسطینی کشته شدند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
در جریان حملات اسرائیل، حداقل به دو سایت پتروشیمی حمله شد که هر دو استراتژیک محسوب می‌شوند:
پتروشیمی کارون در ماهشهر و
پتروشیمی سلمان فارسی ماهشهر</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5404" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEmpFT4fgL6nphyCyaQknN6Z7RHgF19BLBXg1jqKlPdwNbK1vUN5DPod7qkt0cN800xVbEgf0FL6TYNxiEnUmAshkmPtpwIGkfabCDnzbUpcEG8v402aOJ7uok8CTXE9eQzADsEEcCGQ1hlC9zhYWke8OvkIXSnPPYm7RYakEd3CdvOBm1l0Xk02qhicv52TfDYGoN8aKbzNZv-pOw2L2XMMrxW6TB36N05Oi9M1AvTlzNS6ov-h0rMdoBh_DmI-q49KezY4p0T5clnYrbpshKeFoLVgEK4PzvSK4ZTy7-hjZrM--hQE_AV1EeB1bZRTMX9smXKB0DRkU8pwYk3YxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ : اسرائیل و ایران باید سریعا حملات خود را متوقف کنند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5403" target="_blank">📅 13:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.     دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5402" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0iG_3vO13RRFjm5npMWYXSjsdt0Vc53EJn6KgdLku0X2XKJfe24ilda3QWIuRZFrPQqJ4lw6TAXW0xGK8x1QXlpLX5iQXDwrJcdjYzk-qaaoOOtL1jH8ZxbBMelZ1drsnla5WWNrQeQEakfKwglObsAWuRKwSYQbvpjJWKxNf-E5UE4DDSvP65UKu63Txve2VXRs-aVaMSLOQriKxP-g6yDHGSv6T2n5Hy5VbuzbzELGN_-lUFdr5O9oy9stMCJdXU4nNQJtEJ2zmbNOaU1oiTYekKWPYLxK6T0dF5H23wq7QQduuicll8kJ8_t9zLaO-dpZ3WWY7eSzEg6n_0vqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.
دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین شاه ایران است،
امضا کنند
که :« جز تخم نیکی سپهد نکشت!»
متنی که در اون نوشته شده بود :
«نگوید سخن جز به داد و خطیر
نباشد به پیمان او بر، زحیر»
(هیچ فردی به خاطر فرمان‌ها و تصمیم‌های  او دچار آسیبی نمی‌شود!)
در واقع ضحاک به این بسنده نمیکنه که
خب زور دارم، پس سرکوب میکنم و حکومت،  بلکه احساس نیاز پیدا میکنه به فریب  افکار عمومی  و فریب ایرانیان!
برای همین دست به تهیه این «شهادت نامه» میزنه.
و از روی ترس، همه بزرگان ایرانی هم صف می‌کشند و گواهی میدن که او بهترینه! عادل‌ترینه!
که با این شهادت‌نامه، دشمنان ضحاک به عنوان دشمنان یک شاه ایران‌دوست و خیرخواه و عادل معرفی می‌شدند!
کاوه اما این بازی را بهم زد! یک تنه! تنها! طومار را پاره می‌کند و به ایرانیان نشان می‌دهد که رنج ایران از ضحاک است و آن دو ماری که بر دوش دارد!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5401" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
انفجار در غرب و جنوب تهران
🚨
انفجار در فرودگاه شیراز
🚨
انفجار در کرج</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5400" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUa33iXr4djk1sXvoSC1Z7dbPr0lCDualvN-xrha1kBzDcL3_ZpvO-7qie8pa4JJZWV1y7UmULS5nSGIjIFZONwRfXbbvR1r8X8hh3Mp_wu0ITidh9Ypi2DF8Uga8G_qVnzhGhiHA4vs-5jCGOetJI2zMeOscwPy94wKnSlbmjRMKVy9-TmqZLK1bKDVWOQBzQkiBB-xmICHK2lEEMR5q77vwSb2jwbi8A7oI0j3kgMuoYLCSIDV71KqiWRmWHIXPfPE1mQRLNpq9CNrsLdg4fkVc3yGlWDYbiuhgcppRfPpap0h3cGNOMpsVpnOtKr4y-MEATg5rJ9IK_qfSrNAzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداهای انفجار در تهران و اصفهان
🚨
حمله به دانشگاه هوا - فضای سپاه پاسداران در تهران.
🚨
گزارش‌هایی از حمله به یک ایستگاه متعلق به بسیج در کبود آهنگ همدان
🚨
جمهوری اسلامی در پاسخ به حمله اسرائیل به پتروشیمی ماهشهر : صنایع انرژی کشورهای منطقه (کشورهای مسلمان عربی!) رو هدف قرار میدیم!
تصویر : حمله امروز اسرائیل به تهران</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5399" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5398">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agd3qIr6wsuFESIq44GaeyCTom8w9N-O3r8-zwjd4Rwr4MM1-CExosDOltmyRIyp09QdD-Vql2yO1i8SJqNs6Vd6SPoV-LzcqPrNupSHE0YO2C4p8zgrCj3W5ohpHQ7Uwxl6K8Aeh6pLH1Ui7OOonZiFPKrtdnpseJLAaPI1J_MXUDxMFcOS7gl8d58CRlLfrxpHbVGWaOkpGF2OBpy62F7lGviNhdlIKKinwl4DNdfMDsNbSUVxiof7Le8i0eXOobB37gnR7hsvR8Q09U_lEcPbOW3thAv4xh0lE3StYvVcOWVdYUJPzdqJBk9zvfb39xiKbkrll4F6IJZAq0CPVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی برای عمیق کردن دشمنی بین مردم ایران و اسرائیل این بحث «پوریم» رو به شدت تقویت کرد.
۱- پوریم اساسا افسانه است و داستان!
هیچ واقعیتی نداره!
۲- حتی اگه واقعیت داشته باشه :
یک وزیر ایرانی به نام هامون تصمیم گرفت یهودیان ساکن ایران رو قتل عام کنه،
ملکه ایران متوجه داستان شد، قضیه رو به شاه ایران گفت، شاه ایران هم با عاملان این طرح و با هامون برخورد کرد و سرکوبشون کرد!
حامیان جمهوری اسلامی حالا اومدن میگن : ما میخواستیم یهودیان
رو قتل عام کنیم، چرا ملکه رفته لو داده و چرا شاه ایران دستور برخورد  با عوامل طرح و هامون داده! عقلشون هیمنقدره!!
خب شکر خوردید خواستید قتل عام کنید که شکست خوردید!
کی دستور برخورد با هامون داد؟ شاه ایران!
۳- این داستان اساسا افسانه است !</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5398" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">۴ موشک جمهوری اسلامی به سمت حیفا و ۲ موشک به سمت تل‌آویو شلیک شده‌اند.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5397" target="_blank">📅 10:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5396" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5395" target="_blank">📅 09:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">جمهوری اسلامی از دیشب تبدیل به نیروی نیابتی حزب‌الله شد.
وقتی جمهوری اسلامی در خوزستان ، تهران و کرمانشاه جنگید تا ضاحیهِ بیروت بیروت آسیب نبیند.
مقامات ارشد جمهوری اسلامی بارها و به صراحت گفتند که نیروهای «نیابتی» را ساختند تا آنها سد دفاع از جمهوری اسلامی باشند،
مثلا خامنه‌ای سال ۹۴ گفت :« اگر اینها مبارزه نمی‌کردند، این دشمن می‌آمد داخل کشور... اگر جلویش گرفته نمی‌شد، ما باید اینجا در کرمانشاه و همدان و بقیه استان‌ها با اینها می‌جنگیدیم و جلوی اینها را می‌گرفتیم.»
یا قاسم سلیمانی گفت : جمهوری اسلامی امروز در سراسر منطقه دارای عمق راهبردی است. این عمق راهبردی نه برای کشورگشایی، بلکه برای ایجاد یک سد استوار در برابر استکبار است تا دست آن‌ها به مرزهای ما نرسد.»
یحیی رحیم صفوی : «خط دفاعی ما به جنوب لبنان و مرزهای رژیم صهیونیستی منتقل شده است. این توانمندی مانع از آن می‌شود که دشمنان به فکر تعرض به خاک ایران بیفتند.»
دیشب اما جمهوری اسلامی تبدیل به نیروی نیابتی حزب‌الله شد!
داستان بر عکس شد!
جمهوری اسلامی دیشب در خوزستان و تهران و کرمانشاه و تبریز درگیر شد، تا دست اسرائیل را از ضاحیه بیروت و حزب‌الله دور کند!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5394" target="_blank">📅 09:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=WXNCsnQlOtCiiPxBuAUylAMbmSMldDenqCJR7cbeoxEP2TkIuYGd7zfnwZSi9rAKaV1Izt-GpNyolKYDHUzH-q7Tuf_yofZBIWkRB_tsdtKCAZP_b6ayIIfdDst6MekhDk16zZcfOCdvpnA5YG40bJm9VtS2Yxhqt4PYG6AVwIU5nYDx50FuNHkY8tskAypmevUGZpWjqYTUCXRi8D2GG85zGwtWRSN7AIewTLyvsjYZ_GUHzL62hDbHd5wvddZ1Qavz4hDw6GjZdYbpubpL0-eY1RsMI-cLvqyO5sL3lh_qSGwqP6iY2Uhauq3mYi6QeKWe6VUAMphJXbin9dwf-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=WXNCsnQlOtCiiPxBuAUylAMbmSMldDenqCJR7cbeoxEP2TkIuYGd7zfnwZSi9rAKaV1Izt-GpNyolKYDHUzH-q7Tuf_yofZBIWkRB_tsdtKCAZP_b6ayIIfdDst6MekhDk16zZcfOCdvpnA5YG40bJm9VtS2Yxhqt4PYG6AVwIU5nYDx50FuNHkY8tskAypmevUGZpWjqYTUCXRi8D2GG85zGwtWRSN7AIewTLyvsjYZ_GUHzL62hDbHd5wvddZ1Qavz4hDw6GjZdYbpubpL0-eY1RsMI-cLvqyO5sL3lh_qSGwqP6iY2Uhauq3mYi6QeKWe6VUAMphJXbin9dwf-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی  جمهوری اسلامی به اسرائیل و  واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5393" target="_blank">📅 09:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔺
وزیر کشور پاکستان صبح امروز تهران را ترک کرد.
با پیامی که مهم توصیف شده بود، از سوی رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان، دو روز پیش وارد تهران شده بود.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5392" target="_blank">📅 09:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=BGMkHMICIwIjS4GxY2Qx3uzbOfvAdrU1fSBHvlGHdQP7qytw8Y1ERmZFVd9namHdH1Bhh4rRkNTXuJx6tfcKwpilmKI3EEup2BFCjFws-1Es28UuBDi7_fSdBg8vJzA-DqM3GnKEUD-g7FzlxKLK3Ki_m8-WgTt9r_cjVpkSM3OQ-UAlQ0-y1lAYKRwcszgwOpHwRhrbVxPkKZsJSrYzSYgCrmqePKGguQiY0MiLB6Y-5IvAyet2lMiOJl-CWJvxNLvGG8lkuYLyOlyb_zyhsqMhL5l8Nv1FZiTvXY3x2aRkQhDotYbssXD5DZgBh9aY81hjcGlmsaho5E5bA663uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=BGMkHMICIwIjS4GxY2Qx3uzbOfvAdrU1fSBHvlGHdQP7qytw8Y1ERmZFVd9namHdH1Bhh4rRkNTXuJx6tfcKwpilmKI3EEup2BFCjFws-1Es28UuBDi7_fSdBg8vJzA-DqM3GnKEUD-g7FzlxKLK3Ki_m8-WgTt9r_cjVpkSM3OQ-UAlQ0-y1lAYKRwcszgwOpHwRhrbVxPkKZsJSrYzSYgCrmqePKGguQiY0MiLB6Y-5IvAyet2lMiOJl-CWJvxNLvGG8lkuYLyOlyb_zyhsqMhL5l8Nv1FZiTvXY3x2aRkQhDotYbssXD5DZgBh9aY81hjcGlmsaho5E5bA663uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی
جمهوری اسلامی به اسرائیل و
واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها
میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5391" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwnOZsb73pdAXRwPmkBOwpKQbd78iNBteuwwoVycVUILNoa4F_pHbRVccboCmkwGDeI8LEcXo5OSrTx_zysHQuBDE8SSuWtw7bRoIAqTZxhPRPcPlzdqvWVN1c0SqGkjwAcUWYMphV_h_kJWCidlpKcH_0tyqSFrQZj330QTo13ipCv1D1s-58GPw85jbPQqqfU2Nk_QIq8je-3Jk5nuVdnEurn9t370ZpU21zvJBceHyaZNYrk-ongMS4T2KwcA243vxKDZ0QvAqg9aq-w_LeReughwbEQqeZWPwEbsh3jTRp8Z9c2mRBLzmujTfElphKoW_uIFriUsxFsEUoejxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاریجانی هم صبح زود از اون دنیا توییت زد که غم ویرانی ایران رو نداریم!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5390" target="_blank">📅 08:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
سپاه : اسرائیل شب گذشته به چند سایت راداری در سه نقطه کشور حمله کرده است.
🚨
سپاه : دقایقی پیش حمله به مراکز مهم‌اسرائیلی چون پایگاه هوایی نواتیم را آغاز کردیم.
چند توضیح :
🔺
سایت‌های راداری که اسرائیل به آنها حمله کرده کار شناسایی و مقابله با جنگنده‌های اسرائیلی را انجام می‌دهند که اسرائیل به آنها حمله کرده
🔺
سطح ضربه‌های دیشب اسرائیل به نظر میرسد کنترل شده بود. با توجه به مخالفت ترامپ با پاسخ دهی اسرائیل.
اما به نظر میرسد سطح درگیری و ضربات امروز افزایش یابد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5389" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9mrztV1yeljOexDF0FYUhew9vXaJeOZ4KesueXeOpUFs543q16GbrJVEdGDvRORGVkkvLKReNJqRkxI0xkAUAVeJFOkwGq6gp-o9sCjcq0Q15XAe8c78aYSpaDy25MDOedLUjzkdAhswPO9XK4xB0j_jUQaMuI8CXpw2N_r4tskOL43paSUEHKlt6Z0xTNTEXagJg1hitQO30v5v7z1PFwb0pLXykQaR-QFcURhsiiUcqPdVV-sv17JZMhir0zjzE_nq-DUXyuEJaFrHiyM9yJKMvUBV1IiMEio7xYVSPfnNJJ4U9mfwrnjLZ34e5quTULX9YhBL18rDXTN65bzwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5388" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای موج جدید حملات است.
🔺
کابینه امنیتی اسراییل تا ساعاتی دیگر برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5387" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تاکنون : حمله به تهران، تبریز، ارومیه و کرمانشاه گزارش شده است.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/5386" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل رسما حملات اسرائیل به مناطقی در غرب و مرکز ایران را تایید کرد.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5385" target="_blank">📅 04:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجارهای مهیب در تهران ، کرج و اصفهان.
کانال ۱۴ اسرائیل؛ آغاز حملات اسرائیل در ایران</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/5384" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اسرائیل ارسال هرگونه کمکی به غزه را قطع کرد.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5383" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یدیعوت آحارونوت:
🚨
🚨
در گفت‌وگویی که لحظاتی پیش پایان یافت، نتانیاهو به ترامپ از قصد خود برای حمله‌ای قدرتمند به ایران اطلاع داد.
رئیس‌جمهور آمریکا تصریح کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/5382" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5381" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یدیعوت آحارونت:
ایالات متحده به اسرائیل پیام داد که بهتر است چند روز صبر کنید تا ببینیم آیا می‌توان به توافقی دست یافت، و اگر نه، ما طبق برنامه به اقدام مشترک ادامه خواهیم داد، و ارزش ندارد که این را با درگیری‌های محدود تلافی‌جویانه هدر دهید.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/5380" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdvcaBv3PH7Rp5uFFN_MGsJgsl7w8sBdoiMwhvqmIQ1SABPKwxWVJ5PXlgbM0tvuPCXuiwWbUS0QPhsjmRaQKZijR99jGUG00wF6Wl81nExrA-PGLV_yvY2m0RvGk4OEu_yhbzycmu3Ap7QbcHmNRGfx6vQfNABhQjSnryLQiwibfyAMMxWIEHYcJRiOvK_RR27wQ7wWZeI_gV5CvBcaks5husRl7oGqDKQGIk6ridkq8zPVQEeEmfTsFplSOjDnv0_Yip9Q_-q6LDy6nzjEqky3EWrmOdtO7tDPiVjFYf4YZk6tAU884QtmbHyMSJ1j-3tXmhPdLP5xYzqPJ3Otrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.   گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.   ولی این بار رو بعید می‌بینم. عدم پاسخ اسرائیل، یک معادله…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5379" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رهبران اپوزسیون اسرائیل، نفتالی بنت و آویدگور لیبرمن، خواستار حملات قاطع به جمهوری اسلامی شدند.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5378" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etGd_VFLN9Ugp5GB9pzJNbRkwIPdcJu9klDhhsuOBBfUzmPM-Reb52QjoDjG4yL-wr4ZeoN3exs-Kr1Z7LMRBkhoqPpZ4e55MoOhDKeYzXp0fqTUmyHhS4owNHs2-j6VCkKQ_GZsQAEHTnJIz9YWqeG0ri3AtQLKfUhE4ySshC2MLmntAeEw415AedAGYG-3w-iyR7ge_v4f7QRe8sd1mhAcUEbyIKql5WgzdDZO8vc5bbEwQIhtFCDZD6gPg5iuTVaI4OLPb-q9psDyQFvdJqQY_0QKJZxG1bn-ScW0QPSaQIKIuE-XuShwjpGiPFSiea79GGIiACzVYbP2_-C_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ وزیر خارجه اسرائیل به توییت عراقچی.
عراقچی پرچم جمهوری اسلامی و لبنان
رو کنار هم قرار داده بود.
وزیر خارجه اسرائیل ولی پرچم حزب‌الله و جمهوری اسلامی را کنار هم قرار داد و عراقچی را «شیاد» توصیف کرد.
اشاره به اینکه جمهوری اسلامی حامی لبنان نیست بلکه حامی حزب‌الله است.
🔺
یادآوری : دولت لبنان سفیر جمهوری اسلامی را اخراج و جمهوری اسلامی را عامل  جنگ در کشورش معرفی کرد.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5377" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5376" target="_blank">📅 00:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حوثی‌ها حملات موشکی جمهوری اسلامی را تبریک گفتند.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5375" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5374">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.
گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.
ولی این بار رو بعید می‌بینم.
عدم پاسخ اسرائیل، یک معادله تازه ایجاد خواهد کرد و ‌دست اسرائیل رو در لبنان خواهد بست.
چون در برابر هر حمله به حز‌ب‌الله، اسرائیل هدف قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5374" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5373">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/5373" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5372">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
ترامپ : از حمله امروز اسرائیل به بیروت ناخرسندم. اسرائیل با آمریکا هماهنگ نکرده بود!</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/5372" target="_blank">📅 23:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از مقامات اسرائیلی: پاسخی قدرتمند به حملات امشب موشکی جمهوری اسلامی خواهیم داد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5371" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏ترامپ در اولین اظهارات خود: به ایران می‌گویم؛ شما به اندازه کافی شلیک کردید، بس است. حالا برگردید پای میز مذاکره!</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/5370" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5369">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned «
🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.
»</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5369" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5368">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5368" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
اسرائیل : تاکنون تمامی موشک‌های شلیک شده را رهگیری و ساقط کردیم.
🚨
گزارش‌هایی از موج ‌پنجم و‌ ششم شلیک موشک‌های ج‌ا به سمت اسرائیل.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5367" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
والا نیوز : اسرائیل در پی کسب چراغ سبز آمریکاست تا به زیرساخت‌های انرژی ایران حمله کند.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/5366" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
موج اول موشک‌ها از کرمانشاه
موج‌دوم از  تبریز و موج سوم از ارومیه شلیک شدند.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5365" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
