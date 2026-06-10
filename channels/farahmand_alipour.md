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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 21:22:53</div>
<hr>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ne5VXs8_ybH8mf6UEBsxaL2pYoMWWo5IrH0pMm18xD9Vorjb6QWPkECZY1QmKo4CCGABwVqMLk19yHMx1f26k974K46bNvbaW1z6g_Hwtfjww_ISMeynlsnMnnbinnA5NV4yB2fq982lgO8hEk82HiUQo_rfnY7MGq_FX0_gUud8XvbyztW6v5YbwbIOgCULdDItWJQPgdnox8jSrMU4GzOJPqd0ILtdxcBMrAkuJZZYCvrBdl7ukcCztg-6nZxWGPTiPAuJeNjcOY94XZ47WxJXT7DaRkeVU6ZjgX3brljYIftAM-L8nK_NaHA7M1zCTiMCLCvMZlEltk4PqhYiEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2gEVfDNi2P5xJPA2jdHSxi6kPrADS7Rw0FjMf8Kw_jBsIr1zpJ3AzY9Mp-KGll5pSEg6ZRRorBXzaShFb8dVFPOHgayUIEZHRdePB5biqWNgNXqN8BVEoJYw5XZSekqnMaR--rXvpZBflwZQ5xu5Wr71jK37mCHqjJC4yjRaUQ48vjDHTHEYq8jZsa5tjPubm_7HfyIZMryLotBz3jdMcx0bcbnpX5-G4yehipWpWgMmsu6HTlJ7vI-4BLJFbQ3KFi0HHGRc2EJeg5wWaK8TVWCZhpzNizbR6QEWS4OxsWkOjjOn3X5VRxnr3_WnVOclNKVcxe5z-kAyQKSo-vk1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtXZZ18k6CXgAGabiA5BbzzR9Dd02r_fglbvXEzG5TgL9XKO_BP-IIwLPvuB0xHmpcQDFXkJNVTPIyfwNLde5Rzj5JlIvctpUg3zZzZ2DOhTktGFWjkuFKqBJPPAswdunsNvoHi8VQi1JXThfMbKcGQNBrczufYnl5MGRJGAaSawElp-UYBHPuysH-B0WP40vh9-iHTA3pDaQAdg24Uqg-WAG3hXzlpUn6eht-qNKpu5nscuBU88WvSB54uY9ESc5rHWrKXLpTMr-e3XlvITsydRsnFWLmluY-K-cp2rh6bjv0v7xZ21lDw7aOcNKWN-mP4xsNkK9sBSL_d2l7R-zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ac1rsWVa4vuw-tJA698YvUTjHCJ3n9XLL-eFKBuOFpRLbolL0nUM1JHm9FsMbf_gkqAMY5P6xGF_lAURMLJoR94fboXyv0KLH7JMEiUGgWoo7FwASLNR2BQyBHjsMOh-tfqEPBYE5QYlJA8qfAFzCQQcIFTyeZAdtOLN73WI1k-wigcXccWIVlJ3M9xe_9TdNnE1tl0DmkU2uMRGhJ8f1o-3RxcnZGCYV8gG7_dTXUuhkYw_vlFLBwkMmIWEIOZ0BJLSNao8LgtTC4kdfLhLZ3XQfEXLAV1-s1DsoH8Mt5PmrX7Xe2_1AY9sXkTQAOyu_F0b55tGUBZV8BCWF9pDOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7W4UWAWzom_YpDm639DqpB51nQ5AVPULedmS51YdGfqkPbIA9PuXu2mPltk_9VHf9XaUgYott_sNnty42D8GAwJ-5Eyx8j4mSqqL1CV1Ib-3w3Rr3IiMywkxPP1R1WeFx5EZ5IiqNwTarEqb-E1cKXHiRdWMTxMrHFbYk7o7MgVqTza49ZMOJzZ6PegZsPVqbkXNap-U9F49GwXDtcVEE1VPcby_t4PMrRUAlAZQ-1rmth569xYYVSn0nc4QikeN_uNQI99lFsCcujIy0QrmD8s5QtPQORmVH141Tw3u9IcozGPuQfmo67I73_HuzCCyF1l934EokzzzfSPHHztBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GotiR_dL3SD9PhawJJWZ8pjM20wdN2tPjWDNBwFWHnd3P2-qWnxyZbsPt90TEfyhnas9qIv1cCqAjDdfIroJ9X3cRy3UsQ6aNE-5ksBmik6eG__7yNcwHG0zLY6ztZfNLVXjMwWX-KQ0u3Z9UxYy-mN72NGrPRW0nRbd5ZqfpVa2N-sXqLZCiZg9xGxekhlgWezkqhbu6SH-NoSsLD7siXuBcId230Z5_0w9ajsvtpPx99hnZog_vRmRKF8LDd14pfq2xbAzssmABlY6A2L5ZSEqzHrdMssIrtWHocJniswD2vteHghhYGz8wOwJSv-GZbksic-zADd97tnNGDqQhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlNou3N5_9MR8bF8St8i4VJYDTd7cOYTd6f82Xnpu-5CTTC0bdaiFVp_fy01iUIFRNTPTTQMO73IlZlNH_FLEH76SlURas_Z_c4rC971KQFP8IXo2IG1peVmJsghN_3W4RZ9yOZ8UpOqw8PCtxhfFa45tiB5TiZPt29dRpXm0Od2tCR3Iu4CVZzO_vaCzMmujf2ZhY5Uf2iCE1xm5HSleVjLfcaUYDTr47TKvO7znYu6R8IK1DWwKSXvAlGDiVycCXSeKv99xUK5ubJa0tE-lDlWTx7buYXvzPdLCCrgfchaBX-Bfg-gVPSgqYs_gZKoKh4ihlnAKvoKv3tGlVfapA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=qJiDfWiNcqB3nmMe37_Fw_-XiMFPvOvx1SJJITtC5yi2-aLCicNJMYlpOLak5drLsPn5ys16q1CncfX0BsqZ3Wo7QVCh8TvJOoLp-yklmwVKhS_1YE4enedKDUZsGt7ofjmFsHGluirv2jwACFbZ612UBEB6Y_8XhYuKZMs_9BGU6Ms2FuObuNTEp42s01__7as4Wdt57KPS2S2_EIl0eCkk3c8ENegcQul-RHSdSUbGEroBD5iNSiacY3_E7DA3OEl5s4Ssb4wWa1KqtU6ZN5zgcwhfVkuzVN_fMLAV-DDrjAqSSsFjWDTU7uQu6G13_oneuUe7NDPt2pLNAWZiKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=qJiDfWiNcqB3nmMe37_Fw_-XiMFPvOvx1SJJITtC5yi2-aLCicNJMYlpOLak5drLsPn5ys16q1CncfX0BsqZ3Wo7QVCh8TvJOoLp-yklmwVKhS_1YE4enedKDUZsGt7ofjmFsHGluirv2jwACFbZ612UBEB6Y_8XhYuKZMs_9BGU6Ms2FuObuNTEp42s01__7as4Wdt57KPS2S2_EIl0eCkk3c8ENegcQul-RHSdSUbGEroBD5iNSiacY3_E7DA3OEl5s4Ssb4wWa1KqtU6ZN5zgcwhfVkuzVN_fMLAV-DDrjAqSSsFjWDTU7uQu6G13_oneuUe7NDPt2pLNAWZiKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8_JI_fZhfrKUhIkhR3jkGuomdiCRnQzQbPtA1EdRWWXCrMWIfBE8dKPA5jjWY-n0HdiQnMpZUrCcpH5q0UrHVwDv7CvAbiYIwsZ48q1vlqxSqob2P6xXuWqOWQocbCuC_Z9meIkqOJ6YKTdEDSDJvAEeNRJRuc4EuDeDA7b5x2wnD-zB7YCBo9kZHTbrqbwW0s3ROqwFxkEym822gutTBNZZBwpi_vZf2qJdTp0kc4BSg1tooMdNg9CArAO_6j7QNKGvC7o6DsJPmtCJes8_1cN0zzTQ8vkDSERBU2fVbr9JbqSkvUdoPV-tGZ-d1C_9GZ3hVVuiTQ9uIGq6Qf6mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5444" target="_blank">📅 14:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlPvz5YIn-yS8KOhuZ4v2pBMIEJRqFJSQJaOdMYBSxgnQ8FGDwGs81vM0lipAbQMz3JHcUntAjwIrK7YWZVfbC_elufgJNd9HAn4mOHqjkUuvBmRfEyllp4QzgpnKEcOt93updhIXa8AOT2NPcSr4Ysr0J7t5B8VUCalzcGtEGiSRn9M__bkPArg682PztjhdqIQE4kLqfS4Y5BwXUPL3BaUhEQEJUleTIY5zJIIsQEKN1P95U226gPr67BkbeCF7m7l11G5ZuTd5XFlZdZh3qNNMfWC50cDZLCKD-CsgYlOiQfn4YPuq_1a_VLAvcZ7ocA79mXzvviQus6pKSq_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در حملات دیروز اسرائیل دو عضو
پدافندهوایی ارتش کشته شدند،
اسرائیل گفته بود که به  علاوه بر حمله به مجتمع پتروشیمی ماهشهر به پدافند هوایی نیز
در چند استان حمله کرده.
درگیری اخیر در دفاع از گروه حزب‌الله لبنان صورت گرفت! جمهوری اسلامی با حمله به اسرائیل میخواست مانع از حملات اسرائیل به لبنان شود که عملا در این زمینه ناکام ماند و منجر به حملات اسرائیل به ایران شد.
شهدای دفاع از ضاحیه و جنوب لبنان!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5443" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=W9IQ11nFI0GpW871wBYvIDOqoRl3hVz4614zQy9FkLViMrgmic7mMzrYR-l_SKkj-4wRU4CRIheK6cOGyWpI-WlvBQxeCMt095KpnpdrU2yDCQoqnQljJ3yvzaJyrMLqOEY972PvQwV2eU0RedJjwY2rp3IWoPQ1X-IeKchu-P6__ibwGsrr_bvE9g_8C1A4qzdd3g4fZZ2OxmGgrULb1HV144NBOnoHW9dJk0P02OTwfP6IgALLSfkxaVetlJFRLFi-iBMolSnEKTC6oZep63LXuF3L_EAlvow--M_JMjmFX98gyV8XCdeTKnCIHerI0uu9kW981E7jZVe2c_QkHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=W9IQ11nFI0GpW871wBYvIDOqoRl3hVz4614zQy9FkLViMrgmic7mMzrYR-l_SKkj-4wRU4CRIheK6cOGyWpI-WlvBQxeCMt095KpnpdrU2yDCQoqnQljJ3yvzaJyrMLqOEY972PvQwV2eU0RedJjwY2rp3IWoPQ1X-IeKchu-P6__ibwGsrr_bvE9g_8C1A4qzdd3g4fZZ2OxmGgrULb1HV144NBOnoHW9dJk0P02OTwfP6IgALLSfkxaVetlJFRLFi-iBMolSnEKTC6oZep63LXuF3L_EAlvow--M_JMjmFX98gyV8XCdeTKnCIHerI0uu9kW981E7jZVe2c_QkHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R-A3Wg8ZFfPdV43-VN42XEko7i3677PHx8OoHNC9gY1pLcmgONsBIzA21X9_LIHzrt0Flj-4JXQldIl5r0AR1l5cxMEnMpKNer5mewrwcNHhfHNqNE0RtAfHTufPr4DhJ7l4xAj7tAYBxK8JSdPRGO_YjCvlqufALeUBqa_STVFNRmJqhV2BqznAwkPp-b1zYjYStF51t5JA5oBEAn2AwJsHbFDl_1q1mM9t09sivWDe4oVTc_OYbfBkRBncwe7B3IqdvwpJ3AFWDwIs7GWnLKr77rJLkwEWMiEQDaDSKQKlVeiyn5YqEeN38v6OPMYSB_qaObhTpenKhEL0w_vT7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iIEeoMZ4X0y2H5dxPRc9XYo_-iSnAdmXnbnYH1YN5ChcqnEgJphu6VN6tB-PhuNqDf3mTZjMIJ7NWRR9OuK4LB3HTy9ako53gi4Lq9uTScHmQWOXPSfl9QNr5IrWdT_Rp_a_fA7ukqwYkAHMK6DJ_7DHyvAjm3Hx0LutQfF58PAuqx6i8FNfq6_I2UNPFSeSBOpJ9cZBtsC5h53D-iFOp68d7S3g8Ex6_rcE_wayRquYNA2F-lVFN4LqHoPECYu0MO0ffycdC-7_6PdwLlQDTs7ZkZELcCugWxUx0nQfByPWy4CNCx5qCJr5PV6AvF29c-r10PgvVoHHdFzwSL1p-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=FDNUjDXirFxIp6-TGXB9lJYADGI_l42MKdR1KrOhVqGb-x4R9lQszwZIrXsdA4CE6s5MbM81rkCugPpkJEDbmUTe4WJxRKa9vOqpDmt-_i5LK2jw5C-QY15Ulp279jrNpEHHyN255DCOsY1uawCdO367TxkPfejArevSUORyWw44fDbiOV_d9MJgmS4VbFlrkxp18K1JfvIxvRkHlUiCU-BID5FBmP3oPeZz-V9z9FDWPJKAuhPm-Ck2bnSMjFq7XvopKHu0UV1sITK18biO0JjmyvXQ-pkNJ5TgjayG7prArZCnh2dnm4hTyrhZwuvDF2Q3mUlw8NsaFeM7PRO5BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=FDNUjDXirFxIp6-TGXB9lJYADGI_l42MKdR1KrOhVqGb-x4R9lQszwZIrXsdA4CE6s5MbM81rkCugPpkJEDbmUTe4WJxRKa9vOqpDmt-_i5LK2jw5C-QY15Ulp279jrNpEHHyN255DCOsY1uawCdO367TxkPfejArevSUORyWw44fDbiOV_d9MJgmS4VbFlrkxp18K1JfvIxvRkHlUiCU-BID5FBmP3oPeZz-V9z9FDWPJKAuhPm-Ck2bnSMjFq7XvopKHu0UV1sITK18biO0JjmyvXQ-pkNJ5TgjayG7prArZCnh2dnm4hTyrhZwuvDF2Q3mUlw8NsaFeM7PRO5BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqrKUGUG7OvSn4y1NbUMWuCKfWHr9KlNt3BeifYPTG3zAzRtTJgEz8ePTbCvf5KLWqQFaq0rcj0XjFse6Vup7GPwvu9E9l2Cq2Jyd95LVmOO28fuZIYThKIb1Qf5uSEyofa-JKJ8PyYYAs-YYMRdUapnIQckMWxafzeBKgTR6zXBeK1ee-YPoCERo-xbh7r2wNChBY11E4x4UvgMAiUVwe1EF44TUF890WxCogeoyNISJfXEBAvkbLv7tz6Ef4Y9Hb9xxfy6SGi93v55FbyzZpxjAQIyAaVEKqDD8vnh6CLgBf1D9w8FlyWvdz59ZWaq0jj_ehpEHMobIz8hTXjH7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O7IeDPsnfKpzatNGySC2cKpgsJFOb2BXYD_rg4kqYyWbjSNwvMHDrc9UG8-0Vn4U6QussK0m85GOGIH8OqVtneY4nSoTWZKHXQLn8W-mBaUdbNldmfJ4JoWt8ryVPDfPmguz8QZ8BSt-fT50QFj5PzA0Umw-C1DgrQnnptSiTaN-jh9jBTrlJlxbSOlfk-_a3_sVgaiOZKHhy8lfQHAKkZOIiFHhfOnTIyik4myMyUVGiJSxy-E7ygKSu-GTRaXXiP5k3gHdQKRKAQlqgU6YcN5wag4dgzjMxBAU1DDH2CJi4tVqnLTATMAQ1Odp0qY4tu0mIlpshF1vv2HfrfrCag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=Loqel2gQpkMuvh1hVyudWMadkasvo1Z8fdk1s-RVnoL4R3dwm3qpWARldBxmNu0cCCRhP1mjZcs3WWD_Yn0qaYODOS6ypwUB9pLBUOZ0lELAZJpW2T6FY_NIN31Uy7uIHyuquBAJjVwumm53ryquuhuW-BDfi-GEufIPZlYuNFMVRT_l_yJpo4JmkGpM8ffq3LHsf8bTnl4fE5XBfPZhnkxszQEMjJN7D2uPPX7dv-SDOL7jTD3P-4eoxdnI0FZdtPc1COCmuPdjCtNv4xEw4xObZlGMyisZ0LtGtQF-ci7x-Pys_jt3bWLptHWEnM9USF0c1QdeXIbgCT7AjGkNRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=Loqel2gQpkMuvh1hVyudWMadkasvo1Z8fdk1s-RVnoL4R3dwm3qpWARldBxmNu0cCCRhP1mjZcs3WWD_Yn0qaYODOS6ypwUB9pLBUOZ0lELAZJpW2T6FY_NIN31Uy7uIHyuquBAJjVwumm53ryquuhuW-BDfi-GEufIPZlYuNFMVRT_l_yJpo4JmkGpM8ffq3LHsf8bTnl4fE5XBfPZhnkxszQEMjJN7D2uPPX7dv-SDOL7jTD3P-4eoxdnI0FZdtPc1COCmuPdjCtNv4xEw4xObZlGMyisZ0LtGtQF-ci7x-Pys_jt3bWLptHWEnM9USF0c1QdeXIbgCT7AjGkNRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4_gXohrX8vybghipaHOu2r4yxB6WpmOdjoB8on6TJ930D7-SFA3HFJ0AlvDSoIhuKAlwlM7x--CQVTTj93ursPbSdEiAjxmWqiVS-HAQy3xVqjZM6Ew-7Emt-iET22WH_1zI8S1yJpijquxSrxPAgMQ18rNa4xJA3nykMNSn_NXVzbr_FxzVj_66adceGpMBDLftkQLVGY0_Au2pYn69TntFw23oqXobRfdxnp3mw_-pt5yjGSR11FqBA23i1sKIEp3e4et2v2w---YPRS7b8vEXW1B5P2JmHegO8BLYtUbN3X28NNzhr3zWFb_RDC2Amz97Qvfow7ERuoL3OV4Jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnskbHKDpMXzf1XwOxW13boHlaVhzA4QpPB7DrxNQf25q_2Ae0n9pCgT6ATHWsWVZypwv5yCYMBu1Lwh9o86BISjaX6SaTWUr3KfEp6D1EGqdi6XR1hMTQarXgKdAirUXMdwLT749oEx8YVKqsI4gZEESpiTrcJCR4dX54LcgvHuoM9bhRA2X8lzhv_dytbf1v39v_-pWUz3r0CSJOmk9_Ysk2HlFwvWjQ-U_QHGbc4UQioO9DrPfl6UqT9_ESB9jCQWUxl_FTMbHABmJnPU60-BB3Qm-0xdwUO_ZjqOUuV-OqukQIJn5M6Jfb8u0cOhpNUqfukgGF0wGUArnN9o_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wp4jLkd2Xv587pnxn2PEglmV9w0H34V6UoL3_OobVDeZmoD3SZhAxz8CMq5jUE12TPwkToB5NHxEgB2FIn9dfm9WaZ-1keqLPQq5cXjzL2eEW5j3jfttpaGcfl2w521T0NmaL172qGAKqDviv9KCO-CMZtOwGUhMUWtOUCut0-3pf4qPlaaC-DrwGFEDLtrcVsSAh9KWs5bJRgiC90uXhJzmRXazp8zrMKTSyy4xaVd2hH6zkBJ9oBttIe7xlTfV625FvBLFWkzhl7uKJ_oahTJQoVfdaluBP1AQq1pKI4ZtS2Po_XlObqfhfNGJtlil7VxZ0bkTDx6houEk6UL-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TviRo3YyZxs5n73A_rRU3TKJOMb6S77-QPsw7sqGKl7ScPTNqYINoxxff0mQBEovsJKABUCD4ZucGVdpf5y2WTLlxCa-nFH2fxB2_jyqMWSqmweqjt5xzMX9io8IfrVIix-MPZyWOT_YG8vaC3E-h7fMhvgtusVHhvySnzgG3_VpYWUcwpQSBEPTeaxXm8PrfZ4UPC0qBceMMwjwU1n246TXqYwvDxnbgu9geBEl07s9nl3W8YZRH_ThkQZzkzD_j9h7aWlQOPM2rzLc_MqPQaOQasI9sVwmR0Enwkm6NJUQLfaoJgA5xjcvSs_Y5WOtXRX0baniznixp7DRH5wcIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOyYzvsEQy5jt4l1bHohGDSWaLsvFGaWOTxINgCg6NXCYuOcqsjbSkEaZ9dodU4TgxOJemUcnNg9itfmNyV-vR_vwYNkHKWpDO237BbN138x21EAl_MAx5ftQ9ptl8cg7kpI2Aa1s-jmO9gK8XxU9430bHmjS9rprPGTLY_p4WcwZb0GAmovGuh-MLH6kt1OYCUwMI6Zq4SZHf5h39wzRWHpCPViLmr0IuM0cqANpkzy7-fCnbLK8gPuUc8KwFs1AUZuSifrbXpDbK43BUyYqx2ZG9GUCDAQVGwXd7LwNI7lkDHC_PBW9BxrqMAlq-QIEkWIVvo5PeK8bXOj4VCZYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0V5WVmdQdn17PR7BPd20jt3kd2KorOafXeytaz4WU-x_v0hAjUrQlMEXVDqrJHFU34kdVYoCy9WcjUfns2_nFyzimcCLJZktt2NOeUttIKOSkzTIYNkSeDHOME_h-vmtf4vHqhp0N_L2EysU_YROSof4DJz0nWdPlG03GNHQIkzdo0l84J7vcQW0KClBnQiAkDfKjWLC4mIfdce8GwQRN3NnIsGgfzktODMdIlvcAWW_zyeL9carPoMJyQnjGL4T7zq-sBswr64tOR1MtfU9RhUt3Y7IuGWP3dTav7pKEthzzlMvQdOGvEMyOBOw3_xPL8qlUmEmqZclJgHLhCqDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyFycql39Ln-ho-x9r_jByqZ5Rl5E0_VRUTx5PqD__sGDso97LIOScDvCMEU2tQQ6bNd8QL95yF4-TrSNy7nqtGwz8fsrNi07SmwjpDHBLzqGX4NC3cZkLaLoyNRAHhPAPDcHjz3TshJoxp5f5AgQ9qOPoCDA6x-rVbvAFtEdJPfuTt37lI3LBa3USHoZcVAfGNQEVswJO7e-fA7uh8I0h1LcmFA6HB0nXxOW_TuiBalKIbdSgGkGIAcMq7h_M_llZNTyRWfmLUXIP-l9A_i3dPrRDGcWHHHB5wkQOexHv07BLu8j1qhcwlDxEu1eD-wUOifPnl5cyKfOidlloW9Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7axRvsKK6OnNdGboVDMFyp2q6F6UZT3Vx1PKyRd_wgMsNuTkZjrQw6KNsr7K4BhaWeGFnsoLYRrWBNU8d00b9MebqxbpUcrS-6bMC98BqvbTUN5mih-EsZoRqpoG0gRX1Ozv4yySA4pG27iTaQNkVr3h5oXkv1Awq42xu-Gh_WFu_3bvZvN5aK1mNVQRibtvtnRgGGWvNveqT9l68uwW3Dk_-HOFoGsMF5-WyrBFCAdAC0k0QSzd4036xEQvk36lyEaPQ69kxFIW0nDpb6yhfTW4BvgMB_7ZIpCVmmXQYnlrotbrlKMJryhgu4Wdi74ubY9mRKZhJOlqKOBj99wjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=n4yBv8xQewgT_IJoMWBFpP5WsYfDX5DzndgH--zp9GIcnQx94Hzg1ydbgsFwy73NpxfVMJE1EC0Vw5-IGG3ji8CxBvPXgq67NE_npKJBKuDop8eXgwHpP4keEbMewNQ3xwQJNHy54WRlIYK8rmsyZHNkI7ajBpFiYtAq8mJFTf_0P08D1adbwvfWgBlX9ZSlu-IErV_DRtwEDGx2Y0Yh5XbHFu10dJA0Sb77oki9z5sbSZbJPvm1Qpw2aFor-hCUmYz2VQHQry6LJKzInRpgduVEdy9gi2VeQhdHnyOSYdwn77cCDDXfFIkMwNt9nIYHmzwfkF6awH5SO_N-LvI85w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=n4yBv8xQewgT_IJoMWBFpP5WsYfDX5DzndgH--zp9GIcnQx94Hzg1ydbgsFwy73NpxfVMJE1EC0Vw5-IGG3ji8CxBvPXgq67NE_npKJBKuDop8eXgwHpP4keEbMewNQ3xwQJNHy54WRlIYK8rmsyZHNkI7ajBpFiYtAq8mJFTf_0P08D1adbwvfWgBlX9ZSlu-IErV_DRtwEDGx2Y0Yh5XbHFu10dJA0Sb77oki9z5sbSZbJPvm1Qpw2aFor-hCUmYz2VQHQry6LJKzInRpgduVEdy9gi2VeQhdHnyOSYdwn77cCDDXfFIkMwNt9nIYHmzwfkF6awH5SO_N-LvI85w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5421" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0181i3H3u5LHgnZXXE0A3_k7Ph2OG_Gyigdndf_VRpReHMivXQ_ZljCdQn553rSa-JbZUrYoCvk0FPVDmy5d4okjZt8EJjzXvKSZHxbJVK8n75Dswbswd2VuNSDuPAkmLrPG3FTlfDwcg0jdJTG4n6ZOOIDgIY05MqGr1JeEh5i0lFesG61a8CVODyuoKeaBOb9Rw2O5dkUzCVN_zXnOTYDPRWcw0WzhYD7w7ptperLQOzrA6w1m7_uZZswAHXzRkTSdSJ3DI-46f_AeiZ9zz7UUrMpZ2hZ022gOxz480JWL_KbnIUFXv0dQW1MUtaUruw0EElKgF1X0b50v_HlmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=ba_xpdVj59dasjUgCHZFwClzAxFcF4tIleQObF7-Xfvrmfhnj5NnNFVEk5QZnYzyctup21YiO2d41cbJRVJW6dZNJ5sMHQlDqsJSspG76ZiUlJhEHe5486uKGXM0HzRFLdxhabRglcyoH3WxGJH1o-U0Y-bSZBw3vKUhasav9QWt2huekeg46cvqrqLubxyylLF6YGabnXePokt8vpb1G5RAijqeWW5YjlPvzZyrnJQCq_sEeZrrRQ3VXdAS7kGy0bOTHIgKNp_QSTgv19jMFVMSO8r__nJXEUyMcSen7EgBRC7e_MCtPFv3x7oIW5YNn7YJp4WvRDUjMG1qqTfYRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=ba_xpdVj59dasjUgCHZFwClzAxFcF4tIleQObF7-Xfvrmfhnj5NnNFVEk5QZnYzyctup21YiO2d41cbJRVJW6dZNJ5sMHQlDqsJSspG76ZiUlJhEHe5486uKGXM0HzRFLdxhabRglcyoH3WxGJH1o-U0Y-bSZBw3vKUhasav9QWt2huekeg46cvqrqLubxyylLF6YGabnXePokt8vpb1G5RAijqeWW5YjlPvzZyrnJQCq_sEeZrrRQ3VXdAS7kGy0bOTHIgKNp_QSTgv19jMFVMSO8r__nJXEUyMcSen7EgBRC7e_MCtPFv3x7oIW5YNn7YJp4WvRDUjMG1qqTfYRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=NVXwbmQoS8slyRGEQJj35wpaSuUHSbM0FA2bT6Gi4Uj9LRaPqO-lMamJHNYp7uCv1hpQCKrP_Vspu-ClRcHNqjeJDSVC-hgW7G43tYPGH_6LpSXZxqhiOmGvN-Puu20ApEF_D4mFJPuiK0ttAgivitwSqSwj8JxW4WCVF3pMLgYnzH7SzBwDhNqb4eMcO56xbHGj_1Q18DVdAuga990yM5qd8zrZzeCLtUjSQpCFryK_xAdguWqgN26u8eDI-AF-t02Z4lUkpCfvvhn3uw8y13vDRAVTra81klUsdJmq4bvZIxOnRqp54h3NG2PvG6pXDKGY_9J7_78aazuOuMmv3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=NVXwbmQoS8slyRGEQJj35wpaSuUHSbM0FA2bT6Gi4Uj9LRaPqO-lMamJHNYp7uCv1hpQCKrP_Vspu-ClRcHNqjeJDSVC-hgW7G43tYPGH_6LpSXZxqhiOmGvN-Puu20ApEF_D4mFJPuiK0ttAgivitwSqSwj8JxW4WCVF3pMLgYnzH7SzBwDhNqb4eMcO56xbHGj_1Q18DVdAuga990yM5qd8zrZzeCLtUjSQpCFryK_xAdguWqgN26u8eDI-AF-t02Z4lUkpCfvvhn3uw8y13vDRAVTra81klUsdJmq4bvZIxOnRqp54h3NG2PvG6pXDKGY_9J7_78aazuOuMmv3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=YwZ7EIjmnLBC-nTawGJVJwqdzOutTsPkMO00UEMv3vRzLEV4iY1_s0Z23FJXSt_89qsPvbDm1kt9jTeN6W07czhJ07QnhxZqFioCiZe70CH41DzLVrskrLQSEWGMWgJETveLYFDOy_u9wvC0AEdq_6zrpfZJjqTCx_3c6DEqkaPk8pxWKeZdkz3ru1htDRgoV2g27B2NGdsYsXtmcCYVKqrJoHLzawcZtzgFwixv3UDmtYTKqnNz1zPAZ5dFuHaIrJHuGGhDDxHj03I2ag7oP_e6XJsK1RqOscFpSA3kId38jLy0YcYLEqYtPitLmTsUceLmdesIxyKzMWONrzgZdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=YwZ7EIjmnLBC-nTawGJVJwqdzOutTsPkMO00UEMv3vRzLEV4iY1_s0Z23FJXSt_89qsPvbDm1kt9jTeN6W07czhJ07QnhxZqFioCiZe70CH41DzLVrskrLQSEWGMWgJETveLYFDOy_u9wvC0AEdq_6zrpfZJjqTCx_3c6DEqkaPk8pxWKeZdkz3ru1htDRgoV2g27B2NGdsYsXtmcCYVKqrJoHLzawcZtzgFwixv3UDmtYTKqnNz1zPAZ5dFuHaIrJHuGGhDDxHj03I2ag7oP_e6XJsK1RqOscFpSA3kId38jLy0YcYLEqYtPitLmTsUceLmdesIxyKzMWONrzgZdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WtRUyBpD71QeHqm9gSyPzxa_BoR6p5PTZZd6NYw_v8QWDYlDB4MBtzRWplt_JSPopPoPYaXi8zwcs4ktVhpM8NUVpB9_SkYJQMfOwLz9xJrcOVgaiN9LRFRjbZSiHWWs_mCe0tmjCJow7jwM-ZN7TtQII_xhwCIYrTKGi4k467bf8RxvszdeYcKabfpwSM0LOvhhSjSbM8iExsPrZcxBKq47C4VyGAA9v8XTWoDV5YgTS8HZuj8IOVK8gduNRbrbqYgkxZUXQWMG4moJ3kRQHP_JInMmHkPSLcMS1MhhZ52B6ujP7LTqTSnFPLeDh95ZneeQNK5asSdMl1DNa3C49g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfvN0ViMXPRL_P2KDaVxDie_66LIDhbBFYgygntjwQdreYG6o3S1eEfyHpWlo8YeYzAfh3MzTkGQV1qk0vcoFuxgc97_yoPBKQYWewssvUoHU4id-9dWYW8HOGkyVTFeVOfmaZqDgRrcJqeN8n0F1I6_93ufE0FHOCXPHt2tGVX9CCCyy8RZRp0uq3xfjYyi-MEwlsk3MtVmv1Q5zB_u8n6cU4aYTnz4G0_tnNsX2baeJ_pGiTzsat2SjCw8w0UiqYZ9A7ZVVTmR33jocz81gh0IZ_TkFfRxq-L6AAN5FKSdUslpE5E27Sz0N22lztvu7-Bj43Cdg1hVME5ew6HicQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=RK2BiVX8_tdGCEA3i_rrTLhuE0ME8xJ_ZHbQYqmuVPptWWLgLcl0y0yKpRbcoQNEH_cD3YNk1Z2dwKDPd964P8fD7je-utR0jtsKRAxy0Jkt85tUl_2lZoTF4CBOpr2P7IM3gziequ8TxF4vH79S6h8jIQ4GSnsK3uYZBnXotLSAg4QlDSLztXffHAk5xu-Isgw9dKx78QdjnEDlRMEggPIFFLTzf_axTGmbB4swpT05AjVqc59-MQO2QlhIdzW0J3rDksBIn8JPZAlfUY-Vb7B9NhXHLgV4N8F83FRZlyQh7EGSuzFwZQ_Z-kB4xMabwuCSptNN-f0VikajdsBplw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=RK2BiVX8_tdGCEA3i_rrTLhuE0ME8xJ_ZHbQYqmuVPptWWLgLcl0y0yKpRbcoQNEH_cD3YNk1Z2dwKDPd964P8fD7je-utR0jtsKRAxy0Jkt85tUl_2lZoTF4CBOpr2P7IM3gziequ8TxF4vH79S6h8jIQ4GSnsK3uYZBnXotLSAg4QlDSLztXffHAk5xu-Isgw9dKx78QdjnEDlRMEggPIFFLTzf_axTGmbB4swpT05AjVqc59-MQO2QlhIdzW0J3rDksBIn8JPZAlfUY-Vb7B9NhXHLgV4N8F83FRZlyQh7EGSuzFwZQ_Z-kB4xMabwuCSptNN-f0VikajdsBplw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله به یکی از پدافندهای همایی غرب کشور توسط اسرائیل.
این انفجارهای پشت سر هم مربوط به موشک‌های این سامانه است که یکی پس از دیگری منفجر می‌شوند.
این سامانه پدافندی قرار بود از آسمان کشور دفاع کن (با شلیک موشک)
ولی اسرائیل بهش حمله کرد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=FMiHMcicPxOMjN4Zd3tUXz8lCwmzgeJtUDokisKYCBXdp0K4UYoTnW2DVvBMimDlTtumCXGJGGSs8zTEcdvghqkIn4K_w7e4ywY5B9wDYa9TavwO1Y_1XDj21ApFvUYb3rHjFgDNq_ZTFjWGQVu9Yp3YfRtsGC6q_8W7-YAbqyHQhljrgMP_hlEYOnI_AjbCeSCRLqrdIeudrLzoO7tUiH2_AyvH4LF-bL3_dwLiDNm_x4b3Xi5z9d5CPrrrxSKjrtGzoOE5k0HjgaT3Et7JU9vBmX3bxg2LnwnrhzvNDGTqItpAf6Tif1sA0oxfX4iFEsdpvFtuPZs6Nw-s-rtqJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=FMiHMcicPxOMjN4Zd3tUXz8lCwmzgeJtUDokisKYCBXdp0K4UYoTnW2DVvBMimDlTtumCXGJGGSs8zTEcdvghqkIn4K_w7e4ywY5B9wDYa9TavwO1Y_1XDj21ApFvUYb3rHjFgDNq_ZTFjWGQVu9Yp3YfRtsGC6q_8W7-YAbqyHQhljrgMP_hlEYOnI_AjbCeSCRLqrdIeudrLzoO7tUiH2_AyvH4LF-bL3_dwLiDNm_x4b3Xi5z9d5CPrrrxSKjrtGzoOE5k0HjgaT3Et7JU9vBmX3bxg2LnwnrhzvNDGTqItpAf6Tif1sA0oxfX4iFEsdpvFtuPZs6Nw-s-rtqJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2Qu3oDEip2wwF8RmXadKWzJL1vpa7IclbkNfU-GKIn-A9c6qaIzsnFveIz7n_qJs93EjJdfDtkDEuLfWDfIyQhmhjVwWd5WDFodd1Mp2QMqUE596cF2PDEJ1FjxdSFCTCV4LiIeKl_tFyWPLaoXqFWasupUjJjr0u1i116cygmtim_RpSP8oA0C8LbpYhvFRou6UO5XsX2xbHU6Oi_XGoWo_Ai_HzbeP_Q2CVaQHuH3JMgbiSZbRjPbFz3KSukQpVTyLgFTqcYNNBJtFtwOBc0HI2hXl0OxNE43L5v29yNhE1O3vSv9KY-eNSx866yPrlhs0eWGgG06jyeyL8oX-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=Z-Zy4YSQlmGLinHPrdR0GX165NpOw1FxQpcGWPXTad94_oZMRxAYPRPzT-5c83LdJJ5K7FrcJklU2uRKh7ilaAG-3XiKgrulQ7UGSGD_mEUVsvcedf1obH6mNZI2u4QUBcYAVp5EDCJtqQgXBGFEsuCo-PtvhE__AYW47p5l5BRTwbHATEukqQszmjOLiRh6-io0UgY02Koi2dDP5UQDYxn6iDVJynTER-VVeEcdFZ7fdZT4yIFMLBGF7WdIwdQJvfJv5ESUP6rLdagMBuzVXT8AYLeBrGd3FxRXEbSHGqfDnXT7WcY_2HYHhItZWjR0wLW98r2YaislgZn7ww7xYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=Z-Zy4YSQlmGLinHPrdR0GX165NpOw1FxQpcGWPXTad94_oZMRxAYPRPzT-5c83LdJJ5K7FrcJklU2uRKh7ilaAG-3XiKgrulQ7UGSGD_mEUVsvcedf1obH6mNZI2u4QUBcYAVp5EDCJtqQgXBGFEsuCo-PtvhE__AYW47p5l5BRTwbHATEukqQszmjOLiRh6-io0UgY02Koi2dDP5UQDYxn6iDVJynTER-VVeEcdFZ7fdZT4yIFMLBGF7WdIwdQJvfJv5ESUP6rLdagMBuzVXT8AYLeBrGd3FxRXEbSHGqfDnXT7WcY_2HYHhItZWjR0wLW98r2YaislgZn7ww7xYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq00lx9eMvos0qsmj4qWaRlIRvWReysoZS6YVCroMl_liueAW3v2i9jyLiqH_3qa5_DVRDvJ8l2d-7AFq7HQ7oOy6mDZG4zFPgJNdOW0n1urfy060T3Gv9VvPqZKbjR2u5ENMsxPRXYLxVkosg2xeqvffKLMnX24f-H2Ptra49GSujGBP8x3rlDK5nmChSgdCKsZnaXmokuPo-bz2SlkW4IiGain_ywwO6RmrcmrWs2S6ApLysmzN2mLKK9xh8E-XjSKftbrrjNW64YZXh4h1W67nCfd7HGRVszB_M5kSMJNyRlBsqERpPerqsrcdQsp3nizzoCE2aa75Ab_zNVARw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJwepIhZK_Iw0fhHkfhtbZM2CZ7AuqFMSNcJSdsDdCUe2RjDdWZHho5-k71Xkqndk6omj9ymaCRg37VMf4SDO0tcrpwD2HcYB7n09oZRmTPbXj0IXU-3Nk-dMYonhiq9XsrpBks0dlde8ExR87FWmohRsIGUZi5xqOuame66nIUq3vHCqLcgvae6hSX8QFujWnkoJNuKf40RL9uM4FLNajWVVhRZOtiuLJvdozpH1a-8PwDBiUmKL56hu6nvHuoCWFRBuKlJTFsWpU2bbvLYL_WNv6pieCwz6WbSJoqTJnnQceQeGbSotKSTgYTxb6hK6yztQ_cSl50ibvlOfjNULw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5401" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8XwSHVQeACuYBVar3lYdNy9mwqIUEo5_fGGiyecL07kGWdusdktTTX5Pw2oLdDDvkxO4pUO44YFaSHE2TQzk7kxhL0luFDM9uM8U_nqKWdTQalEGjUYwQqAevOdbTk83LySWX2zGxF4FcAhPzXOs4ksWpzWsMI1GwLY1AKXcPgSutgKbLdLlohC76OT9Sb4ZMoWcKw61oOX5xjKxtAOY_E7ZlOXW0x_xFok6AEhqVnXjRf_0yXCiJ5kCoU2cMJnSlElVnI0K2mhHeUHZ0kACiIZkCTdbCTDDDf_eovzzBMbeNwRiWmn6yJqle1war3LOr-b03J9w-Qas99gq1iEtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QezOw8DcCdBgqKfT2OS0KxroYBN8s1HJwm4NKhNJuZhicocKNSY2XJzxPhkAMtn93nR6E-3ZkUe2qwboM9ZN5Cl7HQ4tWDHb3nWnLnGGEL0-fS4PJqErL3CLcRBBTptsSUCHoJnf5-1A1GdsYNrCWhUAUhOzip_qVku_aU7MR9eOmaH-CEdjYqdz4-sQh8WTgRi-vpmTJ_n8hwoi0LH1eC7MYvQr6kqblyR-kvn3CJmJ0mtzIdsTP2XQCFBDek_oqB_YfOJMn9Fcy88e1c8mREKXRHJVUa6qwFSqhncJRN9PtqgQ7qNVZjwnrZ3YMKdlb161TRkO1PYwR_c-QApprA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5395" target="_blank">📅 09:53 · 18 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=E2TxH0-SV0GebxDryPDbEXZEw3_A5xgoRNU9O6-LtU9jcGPWPaGi-aRjRNnFvgpGZYs7-im3YIWpXVY-GxDWMn0jCpo1k_YHmsFIaihavFExluoQzawKTX20T54xvCYL_ZEN-61dPe1JQyPadtm3YNVJdTD5caAkBcOPf22JdIghv2WCRzuSlCBiUwX7umWg0dFQ3EX1HkQPnPdnd7uM8LlV4JwOrdt9BzhqVLfFveVrKQ6y9Vb9zXE-l4YjNwyC7wxvWuv7iSG1HLX60sQqoiyihuWSS5m-ZWNsmc39vA-U2sCWhfnK0rNdF9LJoPZKWl544lVB4Ix6A8JqfSg1MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=E2TxH0-SV0GebxDryPDbEXZEw3_A5xgoRNU9O6-LtU9jcGPWPaGi-aRjRNnFvgpGZYs7-im3YIWpXVY-GxDWMn0jCpo1k_YHmsFIaihavFExluoQzawKTX20T54xvCYL_ZEN-61dPe1JQyPadtm3YNVJdTD5caAkBcOPf22JdIghv2WCRzuSlCBiUwX7umWg0dFQ3EX1HkQPnPdnd7uM8LlV4JwOrdt9BzhqVLfFveVrKQ6y9Vb9zXE-l4YjNwyC7wxvWuv7iSG1HLX60sQqoiyihuWSS5m-ZWNsmc39vA-U2sCWhfnK0rNdF9LJoPZKWl544lVB4Ix6A8JqfSg1MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی  جمهوری اسلامی به اسرائیل و  واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5393" target="_blank">📅 09:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔺
وزیر کشور پاکستان صبح امروز تهران را ترک کرد.
با پیامی که مهم توصیف شده بود، از سوی رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان، دو روز پیش وارد تهران شده بود.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5392" target="_blank">📅 09:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=UZDPO_dEFOnwRD-A_masDj9U9vsVJDl_qV1_8456KiseQ7q9X_XSmfD8rOV8loPV-LDOTtGRPP34ayTKoqEE__ALLzIZEnGShyLMnLwA4KpUc-PACU61ZKyd_TQbAykF2wNBsuv4tZE5W72TE9FBLnUpj-Tx3ibL08ZtXa90xGWVtaVWlxZQk4NMZwq_RBlOfg06CSxD3aI_75-c85OWkoVM2ATj6bb8Bk_d3E2GuaB5NPxW1NCiYbJOkdz9weK7tOlke6xJFdSRd-sBGf1T9x39mlsw9yHjhUFHIDpmin4SlLUOfdaNUjSK4WeuRny8MbZt2PbkUYQksCm20Mo5XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=UZDPO_dEFOnwRD-A_masDj9U9vsVJDl_qV1_8456KiseQ7q9X_XSmfD8rOV8loPV-LDOTtGRPP34ayTKoqEE__ALLzIZEnGShyLMnLwA4KpUc-PACU61ZKyd_TQbAykF2wNBsuv4tZE5W72TE9FBLnUpj-Tx3ibL08ZtXa90xGWVtaVWlxZQk4NMZwq_RBlOfg06CSxD3aI_75-c85OWkoVM2ATj6bb8Bk_d3E2GuaB5NPxW1NCiYbJOkdz9weK7tOlke6xJFdSRd-sBGf1T9x39mlsw9yHjhUFHIDpmin4SlLUOfdaNUjSK4WeuRny8MbZt2PbkUYQksCm20Mo5XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی
جمهوری اسلامی به اسرائیل و
واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها
میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5391" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZ5eWvrzxScVOtz4Tj6Akxs5tA3eftX-4ugFwhLTdz2KtvByMD1o6dVc6CVAyEq8SHjesypFikLlFE4RqXcIlKS_Z1rCxvbjIwj0gSnZ-W0xBLVLpXchF6Hkb9v98YnDBc_Ung3g7NKhYnfyTeGN_SEYptBFhDECU61e6nga3pHD082RGeIj1WhjAoJ3hCuRvl6PLFEqR-_94mL0uy8s7b-Shk5jumT_0ZocMgF8WQ_CtX3dmqSPqBh2IIPe9e6fK0xq2x2J5zhvInIURAV746os0kCA_-dowKhNf-WJcdkMhJhq6QDGhFFo9tCGlqE0Ev7r0xwARQMu0Q4Et5rSZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاریجانی هم صبح زود از اون دنیا توییت زد که غم ویرانی ایران رو نداریم!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5390" target="_blank">📅 08:53 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5389" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIHGvZ8Sm6wVke_FO07tURLyd-tme1MUmJjbd5_8LpLq7qfaFp9I7T7s2aGTgRLAtRvWfFoQBaqq2FVaP23GHBHcOP_TBFPej7lW1edbO12ChaEihGCH7xcKzxgFxk4p4ZSmt8PYptgTrXmoL9H_A0Vi0OrjxUlwbWeTXz3Ss38atJKanCVNzHR-j_jLDMkDVFbofCiwTCbjfBAnN-hRLgKr0z-TMhpj8S2lpVx2f5r74JZb0jgcu539F-4IarVOCz-nOFeLuqle6UsNAB_PdcczOxlA3tK9e4WB51ykoN5eDJ5TUyYKKSbnASf5ao3dyo51DjVe0F_d1ZRP9zLJZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/5384" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5381" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یدیعوت آحارونت:
ایالات متحده به اسرائیل پیام داد که بهتر است چند روز صبر کنید تا ببینیم آیا می‌توان به توافقی دست یافت، و اگر نه، ما طبق برنامه به اقدام مشترک ادامه خواهیم داد، و ارزش ندارد که این را با درگیری‌های محدود تلافی‌جویانه هدر دهید.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/5380" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3HEx8Mj32TcJ5dDpNdwOhfaayRc4oORRteW-xP1-fCMcMfKAen8D0JfHJ0SqPOjz9sz3T-kgtJHCjXlV7P-B77WqBJ8ZB_vtIXK1PneN0BGQfLz2pf0TA1_JbsEkia8tzI6kxnWlD_-rNNkEUIRMo-FZfaDiLYGfpenskwypoBARbXAp73Lus7nyaL91-6W00Bmbmz1SazgTUD7-RZT9kHXgDYMRAanbme_1c-o1GhiUCwXueYXr6S7qXWZIYWuEIOhZUk8fFRnquMNzcmDOke6APp7AqArz4Yc8nCh1C2Ql8TU9nQBy-PmimvpWQT5rWb_espd4SGojQG3XIpPQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqqYreeaGTrJxh4wNVocCBW0SBFB86qHAdaXHTdIxuQUz42NrhWECXB4SxyK5sSCwlVY71rumV2uGbxPXhmYwnFzAxfsvn5LUWV2WI7XMC4gwvkJcpHX-FU_BEWxfp59-RFj4CyCOFc0hGkxoGlZkLl0OEMW5J64awcnAEoJPDRe_NyBfpoNLOMwvlbgDhIMzPDPWRWCTeQbq3PeSeKiuhfCn5rYHGBrTkiKw4E8AzqR_AcRUW3MTsnG9UzGIYYXLhdtwQ7ZHUj-RUJxBtNOAcAoDTX_OLGhlobAgkdb4hjYwVf9t11HTP6sea5yzC7mtBHeO0VbspUekZ9hrTT5Gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5375" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
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
