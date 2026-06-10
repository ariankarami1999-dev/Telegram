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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 23:44:16</div>
<hr>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ne5VXs8_ybH8mf6UEBsxaL2pYoMWWo5IrH0pMm18xD9Vorjb6QWPkECZY1QmKo4CCGABwVqMLk19yHMx1f26k974K46bNvbaW1z6g_Hwtfjww_ISMeynlsnMnnbinnA5NV4yB2fq982lgO8hEk82HiUQo_rfnY7MGq_FX0_gUud8XvbyztW6v5YbwbIOgCULdDItWJQPgdnox8jSrMU4GzOJPqd0ILtdxcBMrAkuJZZYCvrBdl7ukcCztg-6nZxWGPTiPAuJeNjcOY94XZ47WxJXT7DaRkeVU6ZjgX3brljYIftAM-L8nK_NaHA7M1zCTiMCLCvMZlEltk4PqhYiEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2gEVfDNi2P5xJPA2jdHSxi6kPrADS7Rw0FjMf8Kw_jBsIr1zpJ3AzY9Mp-KGll5pSEg6ZRRorBXzaShFb8dVFPOHgayUIEZHRdePB5biqWNgNXqN8BVEoJYw5XZSekqnMaR--rXvpZBflwZQ5xu5Wr71jK37mCHqjJC4yjRaUQ48vjDHTHEYq8jZsa5tjPubm_7HfyIZMryLotBz3jdMcx0bcbnpX5-G4yehipWpWgMmsu6HTlJ7vI-4BLJFbQ3KFi0HHGRc2EJeg5wWaK8TVWCZhpzNizbR6QEWS4OxsWkOjjOn3X5VRxnr3_WnVOclNKVcxe5z-kAyQKSo-vk1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtXZZ18k6CXgAGabiA5BbzzR9Dd02r_fglbvXEzG5TgL9XKO_BP-IIwLPvuB0xHmpcQDFXkJNVTPIyfwNLde5Rzj5JlIvctpUg3zZzZ2DOhTktGFWjkuFKqBJPPAswdunsNvoHi8VQi1JXThfMbKcGQNBrczufYnl5MGRJGAaSawElp-UYBHPuysH-B0WP40vh9-iHTA3pDaQAdg24Uqg-WAG3hXzlpUn6eht-qNKpu5nscuBU88WvSB54uY9ESc5rHWrKXLpTMr-e3XlvITsydRsnFWLmluY-K-cp2rh6bjv0v7xZ21lDw7aOcNKWN-mP4xsNkK9sBSL_d2l7R-zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ac1rsWVa4vuw-tJA698YvUTjHCJ3n9XLL-eFKBuOFpRLbolL0nUM1JHm9FsMbf_gkqAMY5P6xGF_lAURMLJoR94fboXyv0KLH7JMEiUGgWoo7FwASLNR2BQyBHjsMOh-tfqEPBYE5QYlJA8qfAFzCQQcIFTyeZAdtOLN73WI1k-wigcXccWIVlJ3M9xe_9TdNnE1tl0DmkU2uMRGhJ8f1o-3RxcnZGCYV8gG7_dTXUuhkYw_vlFLBwkMmIWEIOZ0BJLSNao8LgtTC4kdfLhLZ3XQfEXLAV1-s1DsoH8Mt5PmrX7Xe2_1AY9sXkTQAOyu_F0b55tGUBZV8BCWF9pDOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7W4UWAWzom_YpDm639DqpB51nQ5AVPULedmS51YdGfqkPbIA9PuXu2mPltk_9VHf9XaUgYott_sNnty42D8GAwJ-5Eyx8j4mSqqL1CV1Ib-3w3Rr3IiMywkxPP1R1WeFx5EZ5IiqNwTarEqb-E1cKXHiRdWMTxMrHFbYk7o7MgVqTza49ZMOJzZ6PegZsPVqbkXNap-U9F49GwXDtcVEE1VPcby_t4PMrRUAlAZQ-1rmth569xYYVSn0nc4QikeN_uNQI99lFsCcujIy0QrmD8s5QtPQORmVH141Tw3u9IcozGPuQfmo67I73_HuzCCyF1l934EokzzzfSPHHztBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2KwMA9847wAiMbRQYId7Euo80lO_EQMaXvpFrYY3e_QbZzvg17sZrcPj4KYq5tDqyNFjK9vNBCl-RR4-9_CB5GarXYCTDoHvomoGr2Hyrq2S7Ed4OGfGcWP3YkwOwyYmAdGzp6Kz05exun9Tg2wODJhgZwDDGDAVM7dhPO65JAEl4Up7gx1c-4cPBsj8mD4g3z0bs2R9aGFztCm7DV30RDa7drkSjTUm56P0pUzAdCE_tIPvkL8k-WsPWlhdUHUIfDgZJZ2Rkn5UkXqCQqq-LqWABjdmJ-OhmiMl1ALAuH-F2TQSWOR5Buzs6nCHizpGP2kYP3DE2yIR2fhxBTnZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rdq35Hr06SV0m5O477dS1A2eJehRM0V5EqpcQYeBCrMbb8daungvN5gmKgCGEWbaDqt30GbIPFwKdFzlt2WTjMeSVD8g_OwjlHxFnU5jTDHSe1n5uxz40HZq5LHh_lG0eiiZ2sfMSn3N-LfTE4k7tI_q_tdI96tHyWm6F8lswDbK9kBhmyEFNqP7bUQqUjTop0VQWA3CBosQnj3gFfNgBBwiJ4qm1vqAtnzeF8TFGYYXkv711vl0ifMF3VRoT7yiTnkkUeLRrXm6JXyz-CXqiZApH3YUFjx5pYc45u29_C2lYdcX2iRrEjeZspUHcgHKseR-WTzgwJ6bum6R5pxDQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=XDpWg5vVfKgOUJfcbrZteu23NeTKUO2Gniu1ikjVyulqlD1N_q-wwoFvl7PTKizaSMx_Zpcz9PAqHRXJBasQ86ytsvp9t9ST8Ikc0_liAXXdqg2nUugYOq9REhgj1uR6sRfkICYQQ2N0q7MY4OKy_FcMxpoBvpA_fV0tGuUKwLWjcUv9hzVpRoWlPD6kxscvsptGjXs3qsINYcgLsSPfphSRtylnT5PjOHULePuPijp08PQBP8RBCJQ4du00Oxe4nPLTiZRxSOqX9Oqkwp2vvwnffCQDFMJmyQMaDus2aGp0syY4oQcVIie6Wn7tB95jkAjRU8vHJsOyxI_vbmiVLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=XDpWg5vVfKgOUJfcbrZteu23NeTKUO2Gniu1ikjVyulqlD1N_q-wwoFvl7PTKizaSMx_Zpcz9PAqHRXJBasQ86ytsvp9t9ST8Ikc0_liAXXdqg2nUugYOq9REhgj1uR6sRfkICYQQ2N0q7MY4OKy_FcMxpoBvpA_fV0tGuUKwLWjcUv9hzVpRoWlPD6kxscvsptGjXs3qsINYcgLsSPfphSRtylnT5PjOHULePuPijp08PQBP8RBCJQ4du00Oxe4nPLTiZRxSOqX9Oqkwp2vvwnffCQDFMJmyQMaDus2aGp0syY4oQcVIie6Wn7tB95jkAjRU8vHJsOyxI_vbmiVLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3a4rNiEWWh73Qc0t5T6-8y3CF3DcphGdW2uYXca1_QcUlB0180QyFFT_5SIrWKFdTvw-Z48F8W3ZWJ_uVr4ZCz5nKH_xGAWpNvnmXRh-LhsGtSDRs1yO15EuBEvbqPg2kmZLv-P4ReLN8TTERIA2XpPyoZdwH3jLsWJouJpG5vESAbIPbfpzqVSSf8Z3j51i6JAqnUWZl-z6dQn5eyLdMsQYe3Z22A9KqoNPI55kRP3nWDZCqESbs-IU8Igo0JSYsLr7CF5uhmnO2Y6nO4to5mJJ-tT_ZeQQ9Y3DdIkBvBE_tKYsP2E9ajVjT2CTxI6qU2s3VP_2TfJ3qQazsZDcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5444" target="_blank">📅 14:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXbDlCRz5_f25GxXkwcT2K4k4Ja_qXeh8dzxuRg6exX5sRAKk2Mdxc1dPE_DOwU5r1Se7JtZ_vweWjRFE49Ok7E22S0KZO-dnMvZOEN2Q5wzn2mqd8BmZ81drLSVPj7vIQo-YOhblN7W97xWkzKbeOhn9WoAG3Quz7tQxjJJS3cgRNETVtRRLkkK-rsfss5dOw1LDCvxswZXCiMvzYemIyPcAeBO1VgRvMovEJCvMUUiVYxuNPNuCK2dOjpkzFM3s1N73K0h6oniS2OJpF-Nuua3fJYS0RBlckemFabAf-XPP7LsSwIfaQ4JmEmOADl88034knHewd-vf59RtpIq9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در حملات دیروز اسرائیل دو عضو
پدافندهوایی ارتش کشته شدند،
اسرائیل گفته بود که به  علاوه بر حمله به مجتمع پتروشیمی ماهشهر به پدافند هوایی نیز
در چند استان حمله کرده.
درگیری اخیر در دفاع از گروه حزب‌الله لبنان صورت گرفت! جمهوری اسلامی با حمله به اسرائیل میخواست مانع از حملات اسرائیل به لبنان شود که عملا در این زمینه ناکام ماند و منجر به حملات اسرائیل به ایران شد.
شهدای دفاع از ضاحیه و جنوب لبنان!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5443" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=iAtTxAOYfHSMtgNx-RKPVLV-iA0kDHugSbBmxY6uJrU9I4UuXR7PgE6nuDDBkyChW13fn7nex9BiDk8M_jdIfGHzyYZOA5-d_DysePWICVe9lgvNunVQQ89_X5VNJNjVDpajrIAas8BGA6TMES14wjVmcMdKoXbg1k9ax-LzWUY7t_hyViAovGFdsFUHpw2HZeGBTTHqBCqjMbo6Zcmq1JgCm-_LqZpe1XigMjAIhK3vkblpbat12dCTG4Xdf93I5dwV8N_2ukUN-gkszBmfJbmk1YiN33u0NiR6jobq5kT0T5I7V5M5uVigrLgEcj7aNafdbRzdLyqJbTQt_Y3VpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=iAtTxAOYfHSMtgNx-RKPVLV-iA0kDHugSbBmxY6uJrU9I4UuXR7PgE6nuDDBkyChW13fn7nex9BiDk8M_jdIfGHzyYZOA5-d_DysePWICVe9lgvNunVQQ89_X5VNJNjVDpajrIAas8BGA6TMES14wjVmcMdKoXbg1k9ax-LzWUY7t_hyViAovGFdsFUHpw2HZeGBTTHqBCqjMbo6Zcmq1JgCm-_LqZpe1XigMjAIhK3vkblpbat12dCTG4Xdf93I5dwV8N_2ukUN-gkszBmfJbmk1YiN33u0NiR6jobq5kT0T5I7V5M5uVigrLgEcj7aNafdbRzdLyqJbTQt_Y3VpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KRR8MDp8mmt1QbHfdDvuSkm3KDMdb3qIStXE8T866tt18_s9qA0TnBAbxeB08SjbYpaHe_12e9zsbcP3Fy5bdcH5pZLlxSsLPkYv2Lt2UjKW0vAN0AG1J-9bmLpy-K5dCXwQ9uozL22J8uKAzBXVfR2ICeEZA4Oi9bCIbeuk5KChgl31evfLqgyDhIXgtKuanezPySw8OEJ43Apbwu0OczQuQ0rRvY0C19sVbJ0qs7VNLDWXwifvMs__YqANwM6gFXPelu1IzO_nf531z30gWJvJXC0jj81CUbRBc_8dVJI9eA11ijtawVHfV8HrtjJDHWyuxn6UZqTyNpyPpuobjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u_Vigt9mThGwRcR4qzlJFMBIgesoh7tZOtgQNJoA_mIAxZ5CmWoTZm2sd2fi-uosiodObQdW3gnMIPSu3x2cEw7l9uI0jzFIIa77TfboJoSacI8yIdfL5ZKOTtRTbJ-_J0i5ydIJEv-GDSe7iUkdSfaAZlEapTZv8b-Eg4LzU9Viyn50Lp-1i_P_FUBqjLLkSPFCrFEHnSYHJugDFmPQKqisUKbXshKY_bqMFr_x0k3cSYkgisDpcA3wNMQM5jBmJP0U_yLuChcUq7a72dxN6a2uRDGUY9LUanG_GJwvFGSVs55VskIR2Thx6NtC3bkDnXmcYwUqNxTtFLD91SAvdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=Kx1bAj5vX8ZVBhgVzXOcb2EIznxVk_lwQKMDbEnskuod1mN-ybu_89NVDtlKgmY6EN6qk_7uzl0U2YgKwWLrR3852IuxruuaXs10JiZysVFVmnSFEeATLAA-kB2D2Sd6e6-vJeXtaPdg7YDf_esmon0KMfx_MaBgDLFBZYHOwVer9IOoS4sxEH05rI8Qq7lUvEPuLfaIUaMXy0yzrRHhF5KQ20JeYDIUOOrylHSBnK681DZRmNfTwNqagfLTnKGR_G3nSXdHEmtpEeiowAhIbfEaIvI5aCQu7hXNKu_Lq2jwc4gApl_sJil_ENXaLekCqlQKr8Viv3TN9twQn5kzgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=Kx1bAj5vX8ZVBhgVzXOcb2EIznxVk_lwQKMDbEnskuod1mN-ybu_89NVDtlKgmY6EN6qk_7uzl0U2YgKwWLrR3852IuxruuaXs10JiZysVFVmnSFEeATLAA-kB2D2Sd6e6-vJeXtaPdg7YDf_esmon0KMfx_MaBgDLFBZYHOwVer9IOoS4sxEH05rI8Qq7lUvEPuLfaIUaMXy0yzrRHhF5KQ20JeYDIUOOrylHSBnK681DZRmNfTwNqagfLTnKGR_G3nSXdHEmtpEeiowAhIbfEaIvI5aCQu7hXNKu_Lq2jwc4gApl_sJil_ENXaLekCqlQKr8Viv3TN9twQn5kzgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5439" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1xrnf07wS83Btxzo1x1snjwjg51nn7DKkDLblXscNsaI5B2cTl-9fVj9XmYWug7UDGuBg75mdNau5HjRsGNsP37s0dSwwLi1Bvskq6kPTcGsp8drzoqrm8bvhjiO8KwWYxoSwhCD3ZeicUSDAtLK8Ih82xUVT1YxqpiHQ0A7uvPzC9DsdT4xNJCHqroswCr7ySWNdp34htxYRg6Nc9QtjK3MGxFAFA54foGF9fPxbvBxQY14iGQPZKQowymWLLXWzMtytoNA5ubiUONiS-vzyqEpcZqGbpjwfq9WNkIj8W6dAIxnToCNeVsvHq9HVvWdc-4xOsGVwyjJdMIGFRV6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L897QZ-MoroBatnq-mRC0hZ4ezMCSTo0ZxA2J5be-dZ9j3CgDmdlbu1Ufca20uSmB0QMvRorwx2TxPg_koC1SSU0tiRVeOxanFT7moONYNcUi03Sl52fmlNKyLyibEWAs15ChmItNuyNyJ5BgYk1w2rxHHsoWSN2nv5tJSKABFpxyhI5qrFX0Odd_jPXLUgMsUyIUiQoUcUBqS8zmdtFTriHPGCkI6OepYa2hd1XQMwg9rzF725y93JTGGDa4-hEi6MuXYvye8qGVYo3151Se5qSJz9O2j31BP1qOAhT52F0LQ6Bgg2D34f93AkHNDkEZJdM0lrBynUoEIUcpbxW5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=WS-MS5YTrTGY9_kVWE1gRHNBskQrIsfRtFL07y7XFKoKkRMRZDDmQJXcLwlDHD5jWRQ0DzcwtyAmRbnYpnBuoUKZk5gpZdY7gDpSRzlg3q-D4HcbnfIpkXbGYytM4DknwHDWjM5gLUrfglVvwhYqyA2yF7c2h8K5tDxjFPDRTBqIS6XMJLMgFZ9BfO2CaVVlR14EB0WYARW7bGky3I48V8zlI7ns9MsXg8MdTj2Urx9-9KGut-y00s_e7JzHg4kxRsGeVHZRc9DI0ckHmOih3BnCGKd1PCE8nfnN6MpEjeIsaAtiiOC3USlZetijqnl1oauiVzPafPt2T7lyzPXvmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=WS-MS5YTrTGY9_kVWE1gRHNBskQrIsfRtFL07y7XFKoKkRMRZDDmQJXcLwlDHD5jWRQ0DzcwtyAmRbnYpnBuoUKZk5gpZdY7gDpSRzlg3q-D4HcbnfIpkXbGYytM4DknwHDWjM5gLUrfglVvwhYqyA2yF7c2h8K5tDxjFPDRTBqIS6XMJLMgFZ9BfO2CaVVlR14EB0WYARW7bGky3I48V8zlI7ns9MsXg8MdTj2Urx9-9KGut-y00s_e7JzHg4kxRsGeVHZRc9DI0ckHmOih3BnCGKd1PCE8nfnN6MpEjeIsaAtiiOC3USlZetijqnl1oauiVzPafPt2T7lyzPXvmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQW0WCN25gghipo8kpkzFkABcOFq4VvaPTWJ-0dpi4BicBNr-Q0-F_Xa8X_7DBt7nXd-Y5ao0xnR9tnN1PqALe7yX9iu8CZh7xPH6QtATPdP5JNMx9OHcyYgZ4voyh4nhKX-rBz7rIObWr1h_M8O4qO4d-cmoMgejLsqjVslTIebU0Z65uF3bc5wWQbUp2EvOGAJaCBjCpeMMO0Pe8wOE7q0BfLmBIY3Dywt8lOEQ5YF0C-B4Kgtv5vmQzWWhg9Zge4W9GArufgJk9xs6h-3nG30vUU7r-AW5FTHJRNr-40XWJEcBnwapWbmzV7eoW4GzA4qjYBd1TbD0jhsmBSrrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_RPWYS2To6y-xox_DnPUgwZ9Cg6d6DinCre0UjYENCHvGhTEuJRJiD9tJ_mXcXGcb2grKWIlQTxzIs6EOvP9iybOnrXIRKRewCF8YypLnbzwkXV43DUvlhOuhSt0WK4EtArj76fwkeXm104RyeqonXSUDd8TWO-KpG9xpkRrwNhCPbnpM5C-V_GLrzbd_5ImyFqyR6eyJQnrAXqKrwKpcsbRZFN552SU0xosu3tDHCMz8CEtipQSdQW3FyIOhWZbvVuxGt-jqAs76aVR53DgIkR8KSgZM79hXhBix-beNKdmZGF7Yu1nZH_xxeZcUCmDRUNG6hqG0x_CSK47V39KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlwILKd8UpEP6aK8NjegimwhRkpBXHecroZapggHr-wJ_hX7niMTSStsIaGFW5deSBU50s_ZNLTI4uPCLZ2FpnXUYWiVdUi3cUSyFO9QSS7R4VNSTKW12E82UBzYEK_8o4V3yXY5R47M_rEhyd8QbwBdbT9w7kInGPpOcMaUQHV4kD4cmbmItMx2ltY5WDcd2dyOKHqNjmhvYxbK6GAF_O10pJL-TFclPjHKN-keOkbictlCGcTzPwa3qItSmupTldgljrGdL0ApaJkE1LAd9Hk_pCxuDOs6gj59jTHu8iUey4KHMsQEx1oyXATMcF3AN2g_JtB0ruLEjl7MMBnv8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n5Li2PRe7j4zyevJAZDFVhnO1ZkgcoaIC0sj9fPIXmysKn2igyj4oLYjuh3D8zT0sKmSzYw6mRq7cHV6ksoZafKUs5COA1FtVjgn7vbD6jxKEjqpMjuN3z1gRVstKJEkSwGmBU0yyA_ofARwSdsxe9jrf0j2_Lp2G8XrLSiSYBg5b2x5Y5gXx0TvT9wuCHV4vbkycssJddaIB-fhypmIF4JVeNI-v0YrS3Eb4TszILhAl4acH5DEtTiE-IkfV-_89TiNW-9zblcc9iD7c_N3cGSp5lK6Y_ovUMOgFHfrcnxxpVy62HewuRjqCKAjhJ031_KDTqpryHrv6e2KpHErCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBl8rjr1xdlXvUemSsUuB4sW8sIDfqILMeyVnaMfLIw_KtFfoahD8s4KNTBEeyySzcRw7eLaYOWXx7P01kMjNdwplIhVBrgBYttLsFBTthGIlqHgU-470Xosv4mMPG2MqOADsXXL2VfSomvs_U3zfXbX0UF20QEU2He26bB76MqhTqJKfrOMYBwSyXk_0ADb4KMTJ56_RLubeduzVhcqtoQU65Pru88LXfuAkPbWBl7D3THFwpq_anUEU6yJwCxmWUcUrRTWPAPcn6Z91QOip5bpvVrqmNYnqaK5X-yKb5xPebwhZTjgSotTBfDtaZ8NDaGFBGEWzG9s9v3qGTFIkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFUvlNjl-oWgiKqNPxL--AoPfPNK33f_42d9B7vH_c5GDmf4PxgXZf8zt3DLynq0aaTxiMZXeeCaGkb8LtHPRKJwAJUkBZhjnBNFO4Vx2AEpsKdFfBwJdf2nD5eGBwtxUk23p36pA7mEg6OUJHbkC1dvsl9SeaIgzWEp-SGECDxSpldVGU0iJ6ookBdv7A3lYRJHKY-EE945SFNp8rT-EuxENfP_WN9B1te2G4LRo--0jRv3KLMat-LUv2sZxse8kL_Uf5sE_m7A-ia8TW9h_o1Xoj9ur_w55zEH-xyPIu6iEkNYqXChH2CTZnsF1mc2FZaC_v7qhf4laxmbxyOSvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNq20oYk9zlv1pXgvJYnoiPsHtuOLcrNjrD0Htob_o4I9_WNadSGAO9imt3ZIjTidTA4_YPl61gHcZgTGFbFEjQ3XJ7V3As550IbDMdriSVDOpTujMiV-gC9hpxzpfGs4NDIbWmwDbmeI4tK9WCq7ZVxR4Mj4qUZ-GiHZghUsn-zOZyBGG47xsw7PgCqiYXwJWvHBQFCCFYDdx6r_CPVfite1k-iwwfXlAlDkJdtAeZ832ALkOrLQptgr4rykQyDniGvLWSwieViiin_FAcSC-PrEfVUY1Knkka0m2MQjHLQyQyk-ISOsUEaGBJSsCh-2wr6hEuWT3O-ZFTZTpNbVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHTrB17sBN7pvjzAJ_CUYEN16Ez9wJZneOwm8gtn48wvn1txHz0h3w6ek831ACuxLw982rBYM2hoJq5m_kL011yyKltJX2RspRfJT_ACYxTUMOS7DSoeRop37FOfl2qjcA51gXYiUvhedjhaVrAg327WRjmltCyf4tTj23lqSkbody0kIFbOHsluS1mR5jkPM3__mopqrZ2NrPH8McabtMmbbDdeim5RHmdFz7WT0Kni58yZyDR6-w8RETiHjjfyxzQH1bSePKfY0kBK9Xy6_KhVFLXlINB8ViHTkUBzNEQDpCwXgnfeVHMpKXS2q-Hjy20zklGEnkprnpfHyvv-NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=I8QlOE3DOXuCwCSHUjYGW51iSLIA2MBnOOVnz2Z8RNw4uSdZ9chEIbfcDuCTepScqdPo_SokrCN-o3Xfquo-K0vNv7fk7itvY8xGBYlP9RLj8k2Rz0GiX6DEFcK55SWwuHzK0raE1oLXZd1IAKibXZaaujL1cEPn4tBW4er6N1dv9ApPbRJWDk238NKR64NK34Q7xxi8BOZY6xgHhO05fvp2wKhVEM75hMjSBQH8X9xcdBhFCvbSHrJjm11yruAQ9xAA9aqKi1n_zbUnB4eZpz5LCbl3H_S_T5n1NeZseWw73CxMBzft8pDNlX_tw91LKSo-omGXc5s1jLTDLSqceQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=I8QlOE3DOXuCwCSHUjYGW51iSLIA2MBnOOVnz2Z8RNw4uSdZ9chEIbfcDuCTepScqdPo_SokrCN-o3Xfquo-K0vNv7fk7itvY8xGBYlP9RLj8k2Rz0GiX6DEFcK55SWwuHzK0raE1oLXZd1IAKibXZaaujL1cEPn4tBW4er6N1dv9ApPbRJWDk238NKR64NK34Q7xxi8BOZY6xgHhO05fvp2wKhVEM75hMjSBQH8X9xcdBhFCvbSHrJjm11yruAQ9xAA9aqKi1n_zbUnB4eZpz5LCbl3H_S_T5n1NeZseWw73CxMBzft8pDNlX_tw91LKSo-omGXc5s1jLTDLSqceQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cyc0eP0ckna17ilgraulnp6ptahE8J_-qKmxMaEQ4oN0-22SA0fjcio2wqFan7C16liIEOHxbwLZuHSsdRm685vYBZ5hjN4a4CRy8_W-ekQ1KmM5sTmKVWeJ2-C5h8MB2qZROTi0lKbStKqe5sEYhl1d1rJOwVfQrIN4tGaNEVmpbqgGGPoWGGZV9gY2wavfhnegjnb1JNBkISoCJphCJ7idRwcLXy7lMZPG3S3mprtS5TBTmhZB8yHFRtyA6994hFye1oNwj1XQ7ep3AKNznZoi5HA12Z47RxiqZsqnYiIByHwCSNJEMZmkj8cLckPSkRuUN_JqnB8hdq0ltDFskA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=WnvTWHYNemIko3ms9c_4VKTeDbcsOsfjSdpn6hf2bARe5VJQtj_nmjHbKFa4WDp27QaWAj4ZKwEBoVNL8mOGtI-ernqIQf8LPW0MrmjW0GR2lyVPnZ0RtVSvy3HA6bNpJeK1nxlJtB1LXWIfGcPH6SI1wyrYLD58t9fUrixqb4dq8fEvtpyBaTHi341CyKhdYozW03hj8bOsi58X-mQHHh-o-SdFUdLIUUtwuYg37CXAypTL8tlyo_usrofvD53n-ATUQdchev9ebbemwMHjvvfFUnonTNQkode0e_aHQlyk3TlrjYDFCtUeszAN7gSeqBfSA9XAYCNTGtWu-hPePg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=WnvTWHYNemIko3ms9c_4VKTeDbcsOsfjSdpn6hf2bARe5VJQtj_nmjHbKFa4WDp27QaWAj4ZKwEBoVNL8mOGtI-ernqIQf8LPW0MrmjW0GR2lyVPnZ0RtVSvy3HA6bNpJeK1nxlJtB1LXWIfGcPH6SI1wyrYLD58t9fUrixqb4dq8fEvtpyBaTHi341CyKhdYozW03hj8bOsi58X-mQHHh-o-SdFUdLIUUtwuYg37CXAypTL8tlyo_usrofvD53n-ATUQdchev9ebbemwMHjvvfFUnonTNQkode0e_aHQlyk3TlrjYDFCtUeszAN7gSeqBfSA9XAYCNTGtWu-hPePg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=IUnXgkI40qorwek6LgFS-9ZDvE8Q20KeeRwljU6ZHmC5AfsaDsGYth8jYGC19fJcHOpGqWrwtlaI0BQ_DS48d2VE36msadAqMnNsz-r3HSl5Sy7SfQ3yWN59cA0AGM5MJGjfH92F8sd-vRciE_Ug1PIQOSfnXbnSstgSCziTVZNx3T1asQhduE4fhQDDWgvDFlIGMNxlm5hPXVO_MHVnsgZbM2Rs88jcXPOeyuupObFwlA54Sv6hhRZ6ED_99IXErkqGQVNT9v6GS394guBoSoaOxJe54kuAg2Wri6jWoO2O6wXMaxjx61JX9wW9zyBCdRMzB_UtvjY_QHQsdV06Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=IUnXgkI40qorwek6LgFS-9ZDvE8Q20KeeRwljU6ZHmC5AfsaDsGYth8jYGC19fJcHOpGqWrwtlaI0BQ_DS48d2VE36msadAqMnNsz-r3HSl5Sy7SfQ3yWN59cA0AGM5MJGjfH92F8sd-vRciE_Ug1PIQOSfnXbnSstgSCziTVZNx3T1asQhduE4fhQDDWgvDFlIGMNxlm5hPXVO_MHVnsgZbM2Rs88jcXPOeyuupObFwlA54Sv6hhRZ6ED_99IXErkqGQVNT9v6GS394guBoSoaOxJe54kuAg2Wri6jWoO2O6wXMaxjx61JX9wW9zyBCdRMzB_UtvjY_QHQsdV06Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=O4XC8qQSMc_LZDfio8ty5jKjp6FBiMbJjSaqg52nfFmOTjDjnbYf4VrqjNojCxUwP5DpW_UE75GfYSqygD3K81eyQAANiEVbd1_9MS_NdP63oL9WY2jtbiGsiL9aXPcjKoW8NDNCQFbQB7IAGoZAQN2KRCT-BQX-WQDJMHbv9DYZY3W7EMoXEdugIsB93Q_2CP2IaqY8MplBY1jXeOUdsFz5n9O7lpg3X8niQ1GR_RXIJ6CnSEEeieX4rPhVeUKD4GlBrZ1pIhLmvKG1pQxN_Q6z0cdBO2zHUNzEQwsY0IQEnh97SHygTg7Q_0HiKbALUXB6YvKlgUaoSEXKzv8Tzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=O4XC8qQSMc_LZDfio8ty5jKjp6FBiMbJjSaqg52nfFmOTjDjnbYf4VrqjNojCxUwP5DpW_UE75GfYSqygD3K81eyQAANiEVbd1_9MS_NdP63oL9WY2jtbiGsiL9aXPcjKoW8NDNCQFbQB7IAGoZAQN2KRCT-BQX-WQDJMHbv9DYZY3W7EMoXEdugIsB93Q_2CP2IaqY8MplBY1jXeOUdsFz5n9O7lpg3X8niQ1GR_RXIJ6CnSEEeieX4rPhVeUKD4GlBrZ1pIhLmvKG1pQxN_Q6z0cdBO2zHUNzEQwsY0IQEnh97SHygTg7Q_0HiKbALUXB6YvKlgUaoSEXKzv8Tzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c40E9DSfFlqHdizX3VQYPMIUy9MMe8PkawaTMiy1LReOr1I-b77C4-rAtb4UHLD2QxfAgzHlWjLORfZ4jju9o9TkPAInvRgGGQ53bFWg2EbcXg3-Ep1sfb6k4hGzLYTKOegekMud4bHhkz3VYqdgu3a-u1Q8crPx8fbY2xyC6tFq_uZE7aQxhfta7OSumloixH3naCQa-myNdQAjhe33SPwMw1iJD246FdPbXj20So96naoWQBON4zD5tBHhUEW4t7QBIPQG91Bi8CYWYay2eRyc26QBVJiS7ggGeENPoz7du94jTd2IUee5jVr983KcMesAe-bpolMKvUc1WlSi5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ox0Dp13lzTEnyASlpew4Z2L6EsS7ittFHA7wjJPLXGtzBBH_jO1QnklGx1QyvHutcCF8CxtyC7Q71i3U0myHJY1aqVlEKxdNHYG6jz5huog8Y6U28PAQQ1mJkn-pW0GjEoglZhAD4FeefRddAPRymqn3t1Z1nrQlwQ17YleCMV5o1Abz7KasANWEOw08Omu97ZhVwHmQytrBQSNXZTZcynZrUAxtDMJPMxSfV-ycXTXQC6M3wTsnGBdLfnJtYFOdO829XEsV00HAFn-PQo5ImU6dKPP5mvk2-mHdlJqiSRaHvNzaguBaHqyt0Dd9xC3tPbECbopLpDdKhmE00BfW3w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=TluxrREMp8spsWDlOgGzLGb2gokYTGHbDzGk5HY0Q8VXF6-REEBRWfXDkqPNtC0BwfvK6TPQZ2TWcvSHoFHXS2Xih2IMhSxr03s1RtW0pbAU7MDkbtVBsXSewPbnl8vua2JqhwKbj0obQFk7kL5FXjj8fK1LE7m_cV3CmSe5E_IdqXE_15-xAWqSDybFlCi7BwwXsdtwch11FVKDqur-uttfdZYPVD9NkcaYFTHTc2apiQHvlnfHM18kIt8v_Lhvw-tjc9YxrOf7l4CAmlV_llH_TAhexhetLv5p5stxNeJvht0lXpshctXA4RTRZmL81iquDoZtGo1-HkVaGTYw6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=TluxrREMp8spsWDlOgGzLGb2gokYTGHbDzGk5HY0Q8VXF6-REEBRWfXDkqPNtC0BwfvK6TPQZ2TWcvSHoFHXS2Xih2IMhSxr03s1RtW0pbAU7MDkbtVBsXSewPbnl8vua2JqhwKbj0obQFk7kL5FXjj8fK1LE7m_cV3CmSe5E_IdqXE_15-xAWqSDybFlCi7BwwXsdtwch11FVKDqur-uttfdZYPVD9NkcaYFTHTc2apiQHvlnfHM18kIt8v_Lhvw-tjc9YxrOf7l4CAmlV_llH_TAhexhetLv5p5stxNeJvht0lXpshctXA4RTRZmL81iquDoZtGo1-HkVaGTYw6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=NikHwI7061Jj_vo2dyLjjGO07y_d23tSSze8N8DmnheXYUAnYcvgV1hRpu4NIrR3KjpII0DwUr7CIDIuHdehK_MhRA7P0tJzGONXfnLEpk5FbmrVXf7xfS39GfyDYbB466vlJdSnndqxJQ91SlRoPyueOhIWkQLf6DSBR5P0HNnL3lRO6AVpxH_tONWTtdAtNv3MIHyzN2TH-CipatFXwaoX43rlCRUPMktx2i825ut_JXIO3v7RzPZLI3-JapS2-tM8-8ZXzcV4DLBO9aLTeYkCsIVXhPN36gARth6IK2EnSmNfiBvZ9UEJ4rAcjPGpib7WIZyB0yVs1kK_RdUvgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=NikHwI7061Jj_vo2dyLjjGO07y_d23tSSze8N8DmnheXYUAnYcvgV1hRpu4NIrR3KjpII0DwUr7CIDIuHdehK_MhRA7P0tJzGONXfnLEpk5FbmrVXf7xfS39GfyDYbB466vlJdSnndqxJQ91SlRoPyueOhIWkQLf6DSBR5P0HNnL3lRO6AVpxH_tONWTtdAtNv3MIHyzN2TH-CipatFXwaoX43rlCRUPMktx2i825ut_JXIO3v7RzPZLI3-JapS2-tM8-8ZXzcV4DLBO9aLTeYkCsIVXhPN36gARth6IK2EnSmNfiBvZ9UEJ4rAcjPGpib7WIZyB0yVs1kK_RdUvgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLEpCweiLIdQHSb-96QKJVsNOUxMA3yxlCgTaGxIHnus2GsfKSBQKerbRMtTLMESImrzUkitLcS0ChC5adbf27yH7Erq8s1S-uN-ifMGQKlYnH3jogUDYi-C0tyB1bHMqY9DEfc1Rg5sjrmSXST_lc6nXPmxerDbzzGnJxX-NfSGzbxuuQRfpRjBwVQVqaZNu5vCyo3wWHKE_UQUsJqYEKwlF2BwJYxWAKIxaCpZY2YnqYUaB8NZhh8wduL52yAuSvp8xDHaIDBy6v4EBBDHbqyyOADLByWqjAhB9Oa9HPoalegWfZSRTRRYnv51GdH-rfrkrld6E41rBkHOyxHoFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=Cxb9TJEgAFH7oqI3ErgEEhX-E6VDa0gMGMgHbEWLE9zlYSRyQs3xj9HqiyQtEs6jMIxRt5VWhmP499tvsY0MGJ5zSwuRQtOr39GpWSivGHhNuForI_BGuwBY3XWQz0C4CRMVzeGBh91_ROr4YjVQ1UGCtodxya7ps_pYAMiR-sm966jucwMYHcZxKnz-SFQ3oR6TZsMGHameC_mtqOUTEh1m7EWDQ2ZreHRDlFzsLY6aFqgfbSd3U6ZuRbM65fi4GujRF2QTNhHqMTS9t6dYamF98JidPnyHhJ-wL2EZcuNa4L50witY5nse352G74YE60ohNtHqVmtE6ofLdmFg4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=Cxb9TJEgAFH7oqI3ErgEEhX-E6VDa0gMGMgHbEWLE9zlYSRyQs3xj9HqiyQtEs6jMIxRt5VWhmP499tvsY0MGJ5zSwuRQtOr39GpWSivGHhNuForI_BGuwBY3XWQz0C4CRMVzeGBh91_ROr4YjVQ1UGCtodxya7ps_pYAMiR-sm966jucwMYHcZxKnz-SFQ3oR6TZsMGHameC_mtqOUTEh1m7EWDQ2ZreHRDlFzsLY6aFqgfbSd3U6ZuRbM65fi4GujRF2QTNhHqMTS9t6dYamF98JidPnyHhJ-wL2EZcuNa4L50witY5nse352G74YE60ohNtHqVmtE6ofLdmFg4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3mESM_LzQAS37eExmG-lpyMACXX-jRcdElnJsKpZqSl7NGfA4P85zNHIOfJdXpsrswIk0lxs-vos0IV4_shzD8Pswnl_HCd8yp-6KGV8wyWE0CVVbmIaMcj1IQldBWKKnbgSClvzyOqqxvz93b5eL9car9DHh7EcS0kfT9H_JLc0vsTNV8jTMaSDOin0e_qc0gpERF_BqROVAnkRCZsvuGc6yuxf4TxjwB2v1AWKb0woBIv4id2vvbqzrTmoHbtFt1oj6Mm1hmA5RvnkfbaMhaYLXx7dF1X_tqsWW2SdTfYkwBEWHOoGBjnVPX8V0Kt2NArAyFZ8sNMXaT7t6muWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwPpHeVRIkeJWNVzx4Z8_4SMQLxr7TempcpgrgxQUTcQHZvBK6iLL_cMbNfAXe0hXvu8QLli--lAvOwDyhYouqUjfhyyLWmemTEIDvKE0uB5BK0BOpUKecDpFP7sjgtqq5HLWPL1O26SpzIc_Q8HRT4JhCNGgiTK3uo4q3dZ0IK1a8mBe1_AxioSyiUOZX00QDr8EIWbwfat478itahoMRGJ9m8AJQkJ-wtCa57lYUFR3JcGJwVgisaXnKhDISgZdbrNoSI_jnnBmfgjyb6nMHx4anRJqMtL55GsiAFn1r68jsVn33o_PeeAgR13cp_wvlHEFWp-Z4inzugPWq6AVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWgW2jIUFshY0tEiT5UoXJESf6ZGXRet5b__0Hg6wfBOqV8ly-Dinf7S8Ydz4E7SykXQDmV3zT8Bu4LAMRFDIL5qZx9q__VGzzVGG1oEQDm_snLukMnlvbAbdFChREFUJUkGJiPIALYBQ4mJIKHuSLoMJZNwP7_9o7wrMe3N0eqH0G3FBsY4NVdH4VZ0OZLw7yjo2E-9YzQvw2Fa-GM4Cr-BhA561frTzMtV8DAe3znK8eUapfhdLtZgB1kLgSMvYz9YKPgVQCUxIKLlNUKLRdqXIf9MHdj2NSZc8fIWsALVXRmTvF3zJBBFGoch7-9xBfGCgMRMT_29EEGbHfv5NQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTwDtqLUYTuMCxjEM9YtML1vSFLFABr382Oc_oc-Ko7_0xo-DoBudDw3AFU7yIQb6snMM49tm17Ct7mKi_TbykjXQAdz4FqDDdZYg0Djb2L-R3AyXr4SnNCzOXbIYmJlSQdIZE7VLw1mE--2Xuk9Z-E7l6Ov3h5fbh1V_l4qs4G56UT43jsIkIUSQ4UKEgcbLe4UHZk-40B6SbJo2BuzTR4Jpxl0ykZsYswhSREtAFyflgw5A0vWeSdOaOCrz8JPJKC63JjQooTsBBCuQLyCTmReACgs6yAEhfHCUdULDHRneyoVppWfYe5fOrw7zyobXO0xXxNBQ-MbNpb9qJ46_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5398" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=mCNOf1IqIMgYDYAxTKmOwUeksUTxTmmM9UsXFmJqwng3xo8CvDq-c33BbDC6XdmrLM6h4EhbeTBrV-RKXYzaYg8BY7nx2eH-OrykKzFJutnBl0kry0mRh5yieF0Y_-ViFaS_lPx-cKivMpX4wc1b8aU5xkhp4lRo-vkPtxnb-f9LDbz8zL3U1UIXGYTup1S5jibcSZD-GiRuhf9Ox4coxVC5HiKdWvZc20dPWmQ1zyeOiXGAYfR2mzwlkxGViMK6zKv-NY0kw9Opbgmrc9ukb6Hkvb4GhU_knE4XIKEgmZ1B-CN38vQLHTLeXRbkzKlGo4fKHPzH_2-41QLXkKfbvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=mCNOf1IqIMgYDYAxTKmOwUeksUTxTmmM9UsXFmJqwng3xo8CvDq-c33BbDC6XdmrLM6h4EhbeTBrV-RKXYzaYg8BY7nx2eH-OrykKzFJutnBl0kry0mRh5yieF0Y_-ViFaS_lPx-cKivMpX4wc1b8aU5xkhp4lRo-vkPtxnb-f9LDbz8zL3U1UIXGYTup1S5jibcSZD-GiRuhf9Ox4coxVC5HiKdWvZc20dPWmQ1zyeOiXGAYfR2mzwlkxGViMK6zKv-NY0kw9Opbgmrc9ukb6Hkvb4GhU_knE4XIKEgmZ1B-CN38vQLHTLeXRbkzKlGo4fKHPzH_2-41QLXkKfbvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی  جمهوری اسلامی به اسرائیل و  واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5393" target="_blank">📅 09:17 · 18 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=nax9Fz3DOjcoP9N94_YN615PaBNx-8fCpqKn8meaw2_paqisqGiZkhRvOjkot1wkPK80qeZ2_Zvds8anCT__N-f03fd_KxWJcab1zBjQt8YVuMnFit-cuIdLMGC9X9w-UkhnM5fiUoKoWgfkObuqdzIzYPyMPSSbyeE8Op05pTeGW4YFWFspr0gbGvajVHzCmFDIKr08KSKaudrCNiHXt59AXYyLdvor8QBwOKZyviVbrmXEBQLWZ_aX9uvCKrQWi_LBAaFcZ9kIEES2Aj3lAiT8z2eCmkr_QG0WfBwqVt_NPyVILrk9jCafgaeWwI0PL6OisTjMVCvSCTCvwgdrJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=nax9Fz3DOjcoP9N94_YN615PaBNx-8fCpqKn8meaw2_paqisqGiZkhRvOjkot1wkPK80qeZ2_Zvds8anCT__N-f03fd_KxWJcab1zBjQt8YVuMnFit-cuIdLMGC9X9w-UkhnM5fiUoKoWgfkObuqdzIzYPyMPSSbyeE8Op05pTeGW4YFWFspr0gbGvajVHzCmFDIKr08KSKaudrCNiHXt59AXYyLdvor8QBwOKZyviVbrmXEBQLWZ_aX9uvCKrQWi_LBAaFcZ9kIEES2Aj3lAiT8z2eCmkr_QG0WfBwqVt_NPyVILrk9jCafgaeWwI0PL6OisTjMVCvSCTCvwgdrJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی
جمهوری اسلامی به اسرائیل و
واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها
میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5391" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RII2CjN4Z82UMpNnem7KtMV2OBX0L8rMYCKWSm29lfHh1u_cDlMMIVwB_pLQldG2x-FGwIp5D8KCLtmbETMaONO5Z0yIB6hx0Ye8QojiXbmTpSC91lDVyB5cIE7kBYB2po8V4NjHKNpF8iH2JVjhbmYnvHVz82ekxa4h_ADv690rbBgN93omMn5CsD-47F-5Gvqd4Rn28MD-a8tve-INknJbkwm6Wxf2TZxpTywIGek20Ay0st7StZXFnlw-QoWAuNaSpg49tCR8ju6OA6GtDKYjFKdLd3MFyTTi2hF2uJyY7_WBVUISITEcFBu2p-T9XCr6vhMnft68vzge5nYw2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qqid5lt0D5TLMadXQpQUksYR_O7_ko1jqwQsZtLwnKhsa4LctZwU6FoQadyFF9GBWlOgY9MLmr9m4F4nJE4mmRHoKAIjSSU6t7LextlGd5QWAfax2qkcT5Xa7JV5tRmDWbxfLvPlLqVK921h6SKs0MzHY9eQmvpvhpj0tN2lMdty1XBv3CDnJw3STBBqZIfHQm_6jmetG4A9zy145aWt_DciylYTUZte2fc6al4IFVdk4O7mS-nY-Ds5SiInEIzzNtRllg8bpdQ_8SyNHTp-EfUzM1ho23Acm0sOWLLV5_hCSaJsigFMtn2RBgtco32OnDPKUY28H_hGPas4eqaS3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5388" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5387" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تاکنون : حمله به تهران، تبریز، ارومیه و کرمانشاه گزارش شده است.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/5386" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل رسما حملات اسرائیل به مناطقی در غرب و مرکز ایران را تایید کرد.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/5385" target="_blank">📅 04:59 · 18 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzlXkheA-1X9G6HpHJBZmYRGc2ZSndv_2ZpfZB1P4GtJN0rN8E8pGp3gtrVNvlMcBIWRxZD8EkmCNKl2nTjUkyQhxVwgu1nTp3uMyrOyElc-_umb5XPp86YXH5x02QeNTawCPrFx-z6xAYPdwI7xKE596ra--PIJ5_VbNyFq6y-gX_sWSex7E6meB_UzArRFdIhTWJj1iDa0WLMcxhm3xmOyC3SArYGkCVMnsrZSznuExYAvRIEtBfsLdNBW1nnAHU6peUVr15FXKntNlVNoU7LJNOwTsWszRMEFU-B2wPrcp4EQ51CE1QvkKGG31ulLagfEBZniQ5_E_NlicDWw4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.   گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.   ولی این بار رو بعید می‌بینم. عدم پاسخ اسرائیل، یک معادله…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5379" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رهبران اپوزسیون اسرائیل، نفتالی بنت و آویدگور لیبرمن، خواستار حملات قاطع به جمهوری اسلامی شدند.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5378" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSI9kZi2wEr3njg5w_xcFWm80hhQW5KttVIS24b0VcU23F_OEFHckMTDmouyGRkAVst6NKpg7miH6-qZDq6w_0UcIb0scLev74RZNrO5CxBhnpPwos2y868g7F6PKIvTFNEAPOUsEcP9xYCMjtg1l3zKsi1K72LynYSsX-ZolvgT2MdG9PSOwNs7IUPBppJnylMxTLhgfeZYV5aDsAzAOPsTzrQrkS1GJXEpvm4XaTcgMsBnAex0YuFKSApqjftm2gRbjSROetGXS4du3TnL_dukdguKzWY6sQEyQAUcgPKtKtTlZNOwaLgShH7yxjzammlTXGvnLPPNt1BaoURtjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5371" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
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
