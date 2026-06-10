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
<p>@farahmand_alipour • 👥 63.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 03:23:56</div>
<hr>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1UyKuzIY7cfOnUVQ9UM2fscDXF8kkklybWltOYW-tvjOpmGj0MUxVcClkAgePVl_U6NboCYtl7jSMN3vpQR0CXHAsMdFamgOvI79hU3OAEZPcI7-UyF05SC_qKwRGD50DPsimKhC0sT0rM1WmpCqLQkGzKu7TDZyRtQNnv6RCsslC2DlTlLJxPEi7_P59rvGu6rYKen9l1VonOZve3_6GjRK8SHB3VJH3NNi1kc1okAWg_3eSm2fAFoD9bD6WhykHvE0Cn1n2BLCDH3B64BOU9jiUi5GGyXGOAJUUavGhAIdn9PHSN3HREaBhFUBsYZfJEHlYTC3mqWXO-wY2J4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هگزت - وزیر جنگ آمریکا:
امشب به سختی به جمهوری اسلامی
ضربه خواهیم زد.
فرصت عالی برای توافق داشتند، نخواستند، امشب «بوم، بوم، بوم»
بمبارانشان خواهیم کرد.
این به معنای  از سرگیری جنگ نیست
فقط برای فشار برای رسیدن به توافق  است.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ne5VXs8_ybH8mf6UEBsxaL2pYoMWWo5IrH0pMm18xD9Vorjb6QWPkECZY1QmKo4CCGABwVqMLk19yHMx1f26k974K46bNvbaW1z6g_Hwtfjww_ISMeynlsnMnnbinnA5NV4yB2fq982lgO8hEk82HiUQo_rfnY7MGq_FX0_gUud8XvbyztW6v5YbwbIOgCULdDItWJQPgdnox8jSrMU4GzOJPqd0ILtdxcBMrAkuJZZYCvrBdl7ukcCztg-6nZxWGPTiPAuJeNjcOY94XZ47WxJXT7DaRkeVU6ZjgX3brljYIftAM-L8nK_NaHA7M1zCTiMCLCvMZlEltk4PqhYiEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2gEVfDNi2P5xJPA2jdHSxi6kPrADS7Rw0FjMf8Kw_jBsIr1zpJ3AzY9Mp-KGll5pSEg6ZRRorBXzaShFb8dVFPOHgayUIEZHRdePB5biqWNgNXqN8BVEoJYw5XZSekqnMaR--rXvpZBflwZQ5xu5Wr71jK37mCHqjJC4yjRaUQ48vjDHTHEYq8jZsa5tjPubm_7HfyIZMryLotBz3jdMcx0bcbnpX5-G4yehipWpWgMmsu6HTlJ7vI-4BLJFbQ3KFi0HHGRc2EJeg5wWaK8TVWCZhpzNizbR6QEWS4OxsWkOjjOn3X5VRxnr3_WnVOclNKVcxe5z-kAyQKSo-vk1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIwqxjJT6kVpK31KpdcD4eAm5Cw-34XsIZWpvyNt5PYyZQF5jkX--RVMjGdgpHT0uVBXWxCIxiJCz_pWPWO7-wrFPpIo369KzHc9f3BQe9Qv1bMJmERPlKshwopVfCIKjnB3poVTmTc7npnmIY-EA_QMUdRw8c5f9puNCk3DwXpSy_A9M17wCQb1FP8tGa0JiX7VLITnCWMwk6kqap6OpwqqgWTrkHwhNGJ_wmNcHw8v-IH7t9K_Fy1eFWUYSLrN01oly_oocwDKaOxzdqtuOnpQWyOfYD44Bgi-ltjb5Nfu3tP_66cCshhifM2g1wibrStfPRi4VRoksAFYfpKRqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtXZZ18k6CXgAGabiA5BbzzR9Dd02r_fglbvXEzG5TgL9XKO_BP-IIwLPvuB0xHmpcQDFXkJNVTPIyfwNLde5Rzj5JlIvctpUg3zZzZ2DOhTktGFWjkuFKqBJPPAswdunsNvoHi8VQi1JXThfMbKcGQNBrczufYnl5MGRJGAaSawElp-UYBHPuysH-B0WP40vh9-iHTA3pDaQAdg24Uqg-WAG3hXzlpUn6eht-qNKpu5nscuBU88WvSB54uY9ESc5rHWrKXLpTMr-e3XlvITsydRsnFWLmluY-K-cp2rh6bjv0v7xZ21lDw7aOcNKWN-mP4xsNkK9sBSL_d2l7R-zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ac1rsWVa4vuw-tJA698YvUTjHCJ3n9XLL-eFKBuOFpRLbolL0nUM1JHm9FsMbf_gkqAMY5P6xGF_lAURMLJoR94fboXyv0KLH7JMEiUGgWoo7FwASLNR2BQyBHjsMOh-tfqEPBYE5QYlJA8qfAFzCQQcIFTyeZAdtOLN73WI1k-wigcXccWIVlJ3M9xe_9TdNnE1tl0DmkU2uMRGhJ8f1o-3RxcnZGCYV8gG7_dTXUuhkYw_vlFLBwkMmIWEIOZ0BJLSNao8LgtTC4kdfLhLZ3XQfEXLAV1-s1DsoH8Mt5PmrX7Xe2_1AY9sXkTQAOyu_F0b55tGUBZV8BCWF9pDOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7W4UWAWzom_YpDm639DqpB51nQ5AVPULedmS51YdGfqkPbIA9PuXu2mPltk_9VHf9XaUgYott_sNnty42D8GAwJ-5Eyx8j4mSqqL1CV1Ib-3w3Rr3IiMywkxPP1R1WeFx5EZ5IiqNwTarEqb-E1cKXHiRdWMTxMrHFbYk7o7MgVqTza49ZMOJzZ6PegZsPVqbkXNap-U9F49GwXDtcVEE1VPcby_t4PMrRUAlAZQ-1rmth569xYYVSn0nc4QikeN_uNQI99lFsCcujIy0QrmD8s5QtPQORmVH141Tw3u9IcozGPuQfmo67I73_HuzCCyF1l934EokzzzfSPHHztBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPjsvmrGJ3LVPTE68NXw-lKn9COWjkYlf2mzy8g9J834Q6s2pbSxsnSPFJhnRwlVQkeOK6vaapMCNadZCWnlFIL5_2cy2GWWrOobn_zDfTJU1BlisgzNAm-z9_GQOeVIV5muh54W_PgDv-hPBXaKdmLaGT5Aw6DZ2SJ-U1Wo7oQKzAVMqE1jVhzPE3Orvdhn7oNuvX4ybgWPc-jjKlNT2CBPgeZlyBKdjKYBJyeBl9-L8tPixPa51ZXK1y0mAy2BiAkTioGEWKhoK9mDFYTbwLhWMEvjWLTAVRZIE-ypYlspxM53w7LYuXfAd5uu3VjrYcCMw2wSFSjHEs5VbILK5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEiRrGdAkXqoezYBCQ8UqG1cnwvGEYmuDzGX3fIXukjGIGY15IlY4t1eueVfqR9a0N8XYr2k9VVpyz6UI1QnCHo_UjjvunxYFBQxzBeRCQGSGaJOanL3zzLm3Z9ZW6sErhT-Z6BmXqha4juvNaHkS_2rQaSkNVzy--9UDEXASSIrhcVsoIVuhhSkmEyF-E0K4Qj2EVTkiM4JcUBLjlbaI5dQmzN_1Yw7Hi3QLfoKIL9Q9RMWSe8iqJ4VHxMz5P02uFGEcPVOL5Ie7RbvnF59bx7OJJEtWRbZbRMhkhH5z-IhYM8gwzlV4rUXmDWlmW2qROKqAn4n_2Ge5Ax14tsruQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=qpO_kXrCuYMvP_SgSrChpeJUeQ5_CRPVpTXlKYhfm9Z2Vy5x83N4VW1FpR44tLGH6UBaKNf4AvQkcghB5ZxJ-3862Ul8jxWUdv62EvRaytaG4awFNQekX0vbn6wCEz_0IqIv3_WBZZZe8CHP11BDfkWkwei8tgwCHmEqjbymf7nUq32PJ2eMvi3SFzZKg4_ZsxqsFH1Qrn4FWCUMzhiv6HnUzWCs3_aYL3nS57kENkbbuuWZBcwAYktvurZPsH6lJWXWv8co7etCnMFfglHUfInoIK_qxc0kkXv1hADIunnRcby0LsYTxBEKK1T8p75HIwwfOMcFvXYyhNz3mIe-Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=qpO_kXrCuYMvP_SgSrChpeJUeQ5_CRPVpTXlKYhfm9Z2Vy5x83N4VW1FpR44tLGH6UBaKNf4AvQkcghB5ZxJ-3862Ul8jxWUdv62EvRaytaG4awFNQekX0vbn6wCEz_0IqIv3_WBZZZe8CHP11BDfkWkwei8tgwCHmEqjbymf7nUq32PJ2eMvi3SFzZKg4_ZsxqsFH1Qrn4FWCUMzhiv6HnUzWCs3_aYL3nS57kENkbbuuWZBcwAYktvurZPsH6lJWXWv8co7etCnMFfglHUfInoIK_qxc0kkXv1hADIunnRcby0LsYTxBEKK1T8p75HIwwfOMcFvXYyhNz3mIe-Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJrKTHsWCAOC8HgpPeI3zkGxmjEGui0ySAGltCKfla99tuLHZxEEvjvUkJujOPIEH5LziAH8whEfA7HsswhTeDS7NJF7X1MVyX2Ov19nKpWyA-CSy8KcuZanfzypHgu5oSYjh4JjO5cmHaIbK_7ltQEhS1XE4I-0k2smiTX2zjcOBPS4ECoCTzIdrSMGy7CRKjnogypZq5FRpYIiDtdIWnsswLtl1YXVQ7BeSCG3aNkgkoHBclDRunn84aJsD-sAI-QSJh5bsTsXRJ0FahNY86V91w7fUJvWk-up6No1WuBmatHjEjMSslSuTOUmLPyRNV_t7NnThXl5BUqMBxmsAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5444" target="_blank">📅 14:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITOsykehGIZFTjtpOjOjxMNsku2jNdFgO9JiUHmSb17nxutoX_jMxHSQuOJ5Uie380dxxorGDsCIQ9ldtGQNwq9NwLM7LPyNLAvo-7s5jTKg0ezq5Zpo5nZNjG2wJWS57pt3On4u2wWet4KM3yQZiB-wDKUpa4aDpChZdi-Gt_KvL81JkGKsGlZfGsI8CMV4ootQ6Mxfzglg772xpRnY9l45HpJuXmO5AffjTP2Gr2tDDxuMg6pVdu-LpkkQ1JlSVn93ZnKyLZ12rXGFQimrD2eVBTYp4lOFgGUzgmX2p9P_Okhjfv9RCioJM2-mHRHGGYw_N2yQLQeYd7I-mAXFSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در حملات دیروز اسرائیل دو عضو
پدافندهوایی ارتش کشته شدند،
اسرائیل گفته بود که به  علاوه بر حمله به مجتمع پتروشیمی ماهشهر به پدافند هوایی نیز
در چند استان حمله کرده.
درگیری اخیر در دفاع از گروه حزب‌الله لبنان صورت گرفت! جمهوری اسلامی با حمله به اسرائیل میخواست مانع از حملات اسرائیل به لبنان شود که عملا در این زمینه ناکام ماند و منجر به حملات اسرائیل به ایران شد.
شهدای دفاع از ضاحیه و جنوب لبنان!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5443" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=jbVzrlFPkiZehSevja1FHxulrK5vSLOaGB8OGbmhLHon4BInloDsOGMUoxCzsZXNFJy9fEYm-PcqJ8tApFhM8jAFwTwLc3C-VqikOrc0cYA_VdVnWbhBCurTeLG4Cazu8Nx2yd-JkxvpSexxitlfhd7kUzHHrvsHgMZyonvXEmHZjvZJZmMy5SllyQAyMZ0wiOevWcdqjQfI4S9xvL_-jyvgYAX6t-xD3CkB1hkTcv5iuEGcRlpATyeSzgz65L4s8rl0cieTgL_LPuFjBFWbpFjeB5WeC3qs9APL1IcY8BUN79LIkBAi6QaWuQPAJb41oPS7Io_fjfknNjgoC02wWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=jbVzrlFPkiZehSevja1FHxulrK5vSLOaGB8OGbmhLHon4BInloDsOGMUoxCzsZXNFJy9fEYm-PcqJ8tApFhM8jAFwTwLc3C-VqikOrc0cYA_VdVnWbhBCurTeLG4Cazu8Nx2yd-JkxvpSexxitlfhd7kUzHHrvsHgMZyonvXEmHZjvZJZmMy5SllyQAyMZ0wiOevWcdqjQfI4S9xvL_-jyvgYAX6t-xD3CkB1hkTcv5iuEGcRlpATyeSzgz65L4s8rl0cieTgL_LPuFjBFWbpFjeB5WeC3qs9APL1IcY8BUN79LIkBAi6QaWuQPAJb41oPS7Io_fjfknNjgoC02wWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bhucg-_ZJZrGJJrtpFHixKS0NOTZTet-2K1IeLximUZlK60HgTNYlio5MmEcEy9F23xWw8itbi7-o-B7B1LtXvGVhfYm7X3NDwuXRfbjUA3cGWNZKZMA41g-gRC-DfyMW8Rsku7juRg-aJaThXCQj0g95DpmGaF3zZDHjgqUhjf3q1TVfHRo2q1HaswC3dwKrauDDPmFUL_fx6v2btY_BQ6R0hHpE6dnM7qFd7jdeYj6WUzxDc6tKNCI8vN4fa-5xZBiC5DWjCzRUiShpyJZvrdfbJD1gijbLXmoDo8lb7otIKaPMFmg6pFi3ecajTtSEhWGu086bPUM38D3eYKtvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RCsqLaHh9fSuD-IK0dutXe5isCcB-H6hgAyQGZ43S9tZ9nhZuIJbq5NAWzI11cBfv9d4CJjslVxc-IWirvdIeRaRAn29S2vtiNtSMrT1ReymGDeOlNRnuSbZCKnopQ5EgtRcAbsTufuPf3RpbteN6VnwSDScApDPF7U8ZCp1IliqmC73Z1QKMbjdpw9z3OPONOcbVlFouEGlGaOtsHxR--EHKA8qZRYChFNzT_xW6d1zjr1QZY7N1_WD7NdiQLMuYgCVqpLzYkabIrRaNJkscoSW0zpUmjLWPnpGmSy_hd6VhZNJhM2DEfOkJp8z11okEXEMn_cjAR94LHC0DgUgpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=Ty9MKi-KOFrDhSKeRasXh1mXSEQqd8AungTHM6Dmw_3SIHT2vhqqnUR9QCp3spDd2W0uSVUnBoYSq1rQO4FkaMV7fY1S3KUss7HzY35sGEnrtKkgDXXyVZxVdWrEVfSlB888QQ-6LLQPQmO-xcnp1YFLh3igFn0jwc4E5aAr78nylUVK89ZTfhiYUzkFMMfEBhkTWe6drYmWNPpMh_yxFDq1H8xCBS4mfmV1jq4WRg3jLLXgwPalaoIo6ou6yyLDcbsLRTAMRCYV2Ah9rQ4zVTXXEokYzdTyfTsQGz63X_MaleMhvLoh81iKj-Nehcr1lFj7lrvUBw1eGiwxlb22vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=Ty9MKi-KOFrDhSKeRasXh1mXSEQqd8AungTHM6Dmw_3SIHT2vhqqnUR9QCp3spDd2W0uSVUnBoYSq1rQO4FkaMV7fY1S3KUss7HzY35sGEnrtKkgDXXyVZxVdWrEVfSlB888QQ-6LLQPQmO-xcnp1YFLh3igFn0jwc4E5aAr78nylUVK89ZTfhiYUzkFMMfEBhkTWe6drYmWNPpMh_yxFDq1H8xCBS4mfmV1jq4WRg3jLLXgwPalaoIo6ou6yyLDcbsLRTAMRCYV2Ah9rQ4zVTXXEokYzdTyfTsQGz63X_MaleMhvLoh81iKj-Nehcr1lFj7lrvUBw1eGiwxlb22vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5439" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OK6Wa8RhSnU6RHH0jr6ihRv60UR6FQ1-811N3EVf6oqZibD6Gj_f-5omQv3uOFZdesmS8ppDhrw6h9ONG47sGhzst3DzBK6C91br-dWxTRPYLnJxOoHaz4sCbKwOeD_m3Km79ZVCPiz2jZTd4FmJKiBw9yeC83GjDw6L6zouZK3-IjA5EkeDYYfR6f3_nNuXUvu7bJxUDbZFF-2aZq_aisGrvu3gYvY-kiSCUPtJjlzE_tCM-kNCrqvLnek1k0408KSbZkitsaM1kr_JqExfVyDVJvXCKnFHvlwmQWp4mfdu7PeHl3LoJ3Kd4lc2jHqazAB7b6FzrbCeqZyp_wLD2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRfhTtiVk17pRWfA1kyQwLBibkd1irpCWjY2DDatDzmLJUEB4sx2bPW888BhewXkYAiBhzCSO6J0kash5tIw9FrstLXXWbUIzIzRkqajhp8atKACVZv3wtaDEQFJS34rRSPF5RL33aU9vPTihAZXRoZ1IGCrpL3hzEVZ_AmrLvnSDbZJE0xizuwea2jVTQ_Y0Lm1fYOL-y8joUrTpqn-Bw5CrCbp6GVk7vXPwfP1ItOGDfhcrrJ_UOwV9chmFnwvBQEwOSPGlChDw9Z7tZcBU7MBa3Sx3vqdooJBf01XwHve0BVo5v9LxR91bsDcR1xd4HTrUzQrPvGiFLNS_jxsWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=a7jGvJXFX4Z0X6lSZQQ4YaJSSeVyeMi9meqNXqStp8hjsvlrdNH5cu-3KLUgfd8ji1IAmgOVwUSuJmcXvdjMzQRKw5OQOvUKWNc6A_fxPRJ7jqZMaVx68O8jkER6YxFNwEXyBVeMtCEzzFaHQ56gsvBiAjEtyxfqLZ767ZnUc2fppW93UfsX7RvYSWu_k7gkyl3Hz6qQkEMjS9elmqNehmlnk44O1nq3fJVNHusfEzUKBuGNxCmoEPIW8zhrvEYaWx2N5vimcbx3m94Uc8hoSQa0a22-EG_jP11mSpRiWvk5qSYTejl4ibJaxeyy-DTclbw151NUQtOgJ4vTjEdp3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=a7jGvJXFX4Z0X6lSZQQ4YaJSSeVyeMi9meqNXqStp8hjsvlrdNH5cu-3KLUgfd8ji1IAmgOVwUSuJmcXvdjMzQRKw5OQOvUKWNc6A_fxPRJ7jqZMaVx68O8jkER6YxFNwEXyBVeMtCEzzFaHQ56gsvBiAjEtyxfqLZ767ZnUc2fppW93UfsX7RvYSWu_k7gkyl3Hz6qQkEMjS9elmqNehmlnk44O1nq3fJVNHusfEzUKBuGNxCmoEPIW8zhrvEYaWx2N5vimcbx3m94Uc8hoSQa0a22-EG_jP11mSpRiWvk5qSYTejl4ibJaxeyy-DTclbw151NUQtOgJ4vTjEdp3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOCz1wKOQRaEl6BtYoYza3064mMzOK72vCzI8LZ-xq4K6flg-F6Wsj7EvRJYIlz_RIRvBSj3prbhkCiP9Wo48xuD57m3hONPxvfHD8evdLm0O_l4fa1GwAIot_8bM7eEc5_YuZuDFViBSA-SbuS3RcbBie3JL_3Q6f0ueydKhsjP4aRuTnpiBwhAiaBAB1qbxgBwK20-pxaPzlrRBXhDpSijlAmtUFokQhU6EjG0t919U-nz_j8llRyNpc4iiJK7vHTTaJDtYs9t_SOFB8Oho5Q8DDwCIAcEmxiJpKXvZ2tUzQeuiusJBBHWoGvi1vw4kpGkToojQB18CRAwBU2ryQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9bPIZrDGe_crfK0yDCLe3wY0eKP1t7_8Jb4RIrzSbFdy8WF4VRt5exUsuZNRiTiwe1kz9kcYFHNBVo9i9MgWksqB4t2Rqt7VCIvp-uhiJaVUNHsYdi5uqrWVddIhDBMj_b2kRKLReU46izp0J4HEnCMGAAwZrs448VpNzf27_Uzp-z437ZwE7Epx-NEegaQFRjHFuBOQ3dPPjaX5mTz2haFz3XFKlDEnTZLys5x5Z9pnqbDUzpi-z4WxtDxf8jHmykGCXFAABB3q5Z3i9Ad_p_-opAwOV96uAtQxL7gijIsmVsDmaR5aqz4QA5TcBdwQ4YHlsJtNETv-O7PJzbVVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4ZTwQSj0ny3WIoxJ_vj_kMcO0AiGh7m3ELpGszPjRqhXBLrXbmgnsnmEm9E-bvUTc9sMQM1hEy0i1E6jQZCJ9NG1aZFa7amPwUexSCVl0L7FCFFmqGus-AtfAxQ7mOPlz-z9Ea-s0fCbcMnmYPHlNCEJTD-ulSU7K26LS4YOD5WEzDckyzOyrFdFE89IJlBpywImon88NG4wNZ_TKXA1UYud4FNBDfJu2gg4G4yJ-Z5oz7X9U9pTVONhHFUGBFaz6f-1XS8aXnfRwSPFx3bg0jKSRWU-d4V0xuhq5bcv3Xhys8Snd6eing2QKyc0oCKmDUOBW85llOyYEnAFk2TTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HIRYJPZZUrz4VApwecCv3NtFs8LUyP-f2GZ9cmc6zyP_1RkAQEFZjakly5oBmSl3TFrRTxBduOx81Gdo8DxGnbx_tMmkHpWepw_qWHaETvcKBYW7dQRBDozlNQLuGF7uBrM1iguVbpwx5q164AkhlSOGdCk_E8Ow8WBhrfzOpwbufcK1t5mS4eY-ancW0C7i_BvofQnQZVvxwxYANIv-RFwMUYDK595yLaz6jnW0QLYM-_vTGgjq5uRvIVhN3i3lmYkWTYbYpKiOVouHkZAwwOGPjNh6lzLE85MyUYfBmmsY3HZkTrOIMUwO2ldvb8oM61Q9MJClUT9IHvsPrqMe8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/io0adn7IEsk-JlQDToI7pJHwSiO-WXfWct9QLShoz6kNj_4Po42DJpBgAWzWt3IKObs9-QCgQIhYobjc5hQuEIy0EzoK9tLRY6B3Q1nMchfL8mI3Zrxg8P2qX-_1wYk9mZSnUFLnn_r8AzgUmTt55OAwU9IfgBUJfzb2N7KsNdIuO1Sx9jJ7KOwiicgrBLDjdL9EQV792kddfDq2a_xdbU8DwlCTNtCVQ7iAa0nvpPClxrwK05GUPEYk3mfYIJ_IUqOytJf_2oNw4VwiefikhhHkf2fcUWW9dzQr0fGwwJOMLo5dryLcrUDvzeF-mb0nJZeKBhPiABqpQ5jYuiUx3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3-eSwp_5dRLUsmVu8Id4-UfT5IoDKorN-M_oqGsnf8rSgX8MYhVqcG1c3SYQBrwEjn8lynAJlu3DcTa_1ZRAOyjQ0AwSPY4wKk-aSLZSjEPc3jqZuPK0To007IHiiwcIvEEsGDcE5kOMGnhd6_yENvr7uaAiMxB6V86mCpY7TiWfDzG0fHC2zRpwppo46AlgSNbll1UlYIp0rY6xrsCKSR54dN4CwKwkmgMubn9yDXNyxRcTk2Uy8WEHSqwIpCdQxwtjqY4IMBpyoskRwp-NZEDZAc6eWpUUUxSyPpCRgAQgoxVeUaMiBWxDOz8c5cRX56Z2c5ldMKWV_BfApPwLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uF28TB0Ux7eDFgAyf1Z79jLvKY-Uncva_3E_zhufPwOI4Mm6P46gJHMCAHrkEOL7zDwdMiGE7hkl_v9kJNVzhfx3dSc8krtJiKOshH7Clr4xpTJy1HRiqLJmmNE7onCKV_NbkaaUo6-h1AAoFPBV2JF9rQBfuAoBOESf9Us6nAFbHOWE2kna6fdHa0-jKwrNmCY_raAXeEmPFx-1rtrppZTeNmGRrpiifggGnWcOt8A-d_vMVKGIU8cGUdX1veuILwtFXATC5OmVUXs0OrPVsugmce-Rx9VHZk-1mA6B0Vt0BHdNaoO0A93hfohre_gfGKzWkiH1lNpX_UykpG4TFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKaXngdRukTmVGGLOpepeb0NUrgcflRgIEe0GyrrgKjUFAn54v9cqdMTz1_aHq_aKGdUnU2Hj1BTjLekEMmQ4iur0PMe0QTnAqsmW6KQqgE7FVN3Zqnh7TupJP_fhSGErQa481MZFlJ87Jdp9OfnFewfojSq6R4N44n9OB71ek_QLYBMghxhy_PNsV9oAsRCqsoIQfv_oA_D2nlCl66yMvGr-Hk99STMgIodvpX31pJAOcsGqJb3KAUd7Ng0twhNMiALIzriKlRqg2gfyfkhEFVGfn4R8v1SaiFc3_2Zoe8v8OUq-Dz2RgfMDIpunYe4721GblL7Y9zhHTvBn9ZGhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=MCDKIEsWZYTGiAYbkSqlGboPsFsQa6O4LSPJ4AO2sX5v-G7qp3LJVY3H3rgYiUw-7FX5hsLrTGmNA8qToq4UURgcZ8Xg2ECBbfckz_1nKzS3g2ExM-YHTGMN_dji1ZW_qt_KJEdpUNgcSZWHQrYMhL3byL4wtyQHgSgs1lxbjshfpzqLbkvJS3dIOOL660mFXOIeUTDmNsATWIdm7iPKemd8PC7TjUeRhpYyqLzJryJZLmbS_-UFqX8-xEgUhIsOXxvc2G649KmKK_E94KFsq3mCIz9QMlef-ARe29Am_KyER5mcJfHZEn8Ddb4aFEZr6Jq4fJ50XoBGlErDfOTYow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=MCDKIEsWZYTGiAYbkSqlGboPsFsQa6O4LSPJ4AO2sX5v-G7qp3LJVY3H3rgYiUw-7FX5hsLrTGmNA8qToq4UURgcZ8Xg2ECBbfckz_1nKzS3g2ExM-YHTGMN_dji1ZW_qt_KJEdpUNgcSZWHQrYMhL3byL4wtyQHgSgs1lxbjshfpzqLbkvJS3dIOOL660mFXOIeUTDmNsATWIdm7iPKemd8PC7TjUeRhpYyqLzJryJZLmbS_-UFqX8-xEgUhIsOXxvc2G649KmKK_E94KFsq3mCIz9QMlef-ARe29Am_KyER5mcJfHZEn8Ddb4aFEZr6Jq4fJ50XoBGlErDfOTYow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5421" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPcJbIOCZZ9Tg1Y0uDedTHi3rfJWVAlqmOSdyIqJabJ56y45nOGZvpyoPLaoFbjv-hRhaC0CKN4Srt30Fx5YSukIdWJoZHr7m1ABbn8fjgbzmbT1VwRZAyTS1KlAw4sMsMTUaD_Tp0T7CFiUSOSfiI3yCdINT8HdBQ_rTOWhlEQltOibmli9wsD9EPtC_9HtS2tJqy5ANG0XITZFD679YUMj16CkcKI7uRuN6vZlUqOKCpTKi7cj_fviTqAvBWZ_9z70y_KRrbEEEML1PEIj3dOgMWRv4nli_dyky3s3Eedm2VkmSRPCTMikACqt-BF5gBtLB_1Yszp_qy-L5Uh2TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=ImunHg9ZCJdFkddOjygy1b6UJtbQzr1W5AW-gppcYFT8NYcS7bEBoX5DqTAJriRLqnBZv1EMRFdZOo3hG5IMG9zFl5g25Z9OFkhS4VTxYgoxAne21d2i6PlSojszTMPaB3LAyKTnXLa3rcMmQARAVUZLaYVrnQE1A6-rhp3jaPkCySYCAct04-37oRUX41KPv_AhsIDLQQsTvQntkQvMbUAnYLgHa2LF8o5AI8UxYNN879VkNkFhNMvZwvRqAwGCNyNb16Xv7nviz2kKnWcWdDowS4AyTz8UQWaatNRMatwe4AkeNC8BEGL9T4qeF6fyr2NSRfqxQj66H0hVCyLsAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=ImunHg9ZCJdFkddOjygy1b6UJtbQzr1W5AW-gppcYFT8NYcS7bEBoX5DqTAJriRLqnBZv1EMRFdZOo3hG5IMG9zFl5g25Z9OFkhS4VTxYgoxAne21d2i6PlSojszTMPaB3LAyKTnXLa3rcMmQARAVUZLaYVrnQE1A6-rhp3jaPkCySYCAct04-37oRUX41KPv_AhsIDLQQsTvQntkQvMbUAnYLgHa2LF8o5AI8UxYNN879VkNkFhNMvZwvRqAwGCNyNb16Xv7nviz2kKnWcWdDowS4AyTz8UQWaatNRMatwe4AkeNC8BEGL9T4qeF6fyr2NSRfqxQj66H0hVCyLsAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=RSFNyjRh82_dURO02nZ3KT7e0Nz-6NAAXLLDY0hH5WuZhgI8Uloc0oYc6QekTnrskXr371KROz9sz362xgVRcIFMmp9TXNcbJjScsZbaI3zheCwcyLpuDuQmk1meMclBIo_OfJtgTfvGf-a2GAL-5tkXUh7d0FBqI5NVc0c79VX0JddTFJ_-zk-DzZFMuQgQJWt1eCZrEo_hIK7BvkZPu145oqJNIhPEwqG8BY9pygkdLYknGsUZXtQ1SBJfg82t_yo8oFKpHC7mTYTzMvAId-RCJ2omrNwcHWHuJYA9VLXkXXff256DW3EmgAS3ynVUfiwNd6C_gH4cIRqh5tCChA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=RSFNyjRh82_dURO02nZ3KT7e0Nz-6NAAXLLDY0hH5WuZhgI8Uloc0oYc6QekTnrskXr371KROz9sz362xgVRcIFMmp9TXNcbJjScsZbaI3zheCwcyLpuDuQmk1meMclBIo_OfJtgTfvGf-a2GAL-5tkXUh7d0FBqI5NVc0c79VX0JddTFJ_-zk-DzZFMuQgQJWt1eCZrEo_hIK7BvkZPu145oqJNIhPEwqG8BY9pygkdLYknGsUZXtQ1SBJfg82t_yo8oFKpHC7mTYTzMvAId-RCJ2omrNwcHWHuJYA9VLXkXXff256DW3EmgAS3ynVUfiwNd6C_gH4cIRqh5tCChA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=gUPoda5aMQDkU_64hQoOjpAn5P9nOKpnaZmDZ5YW7mSNt5vZoRIaaUWSQ-rIpxksySfj-9cn-gQPG-rggd9zfk7VHIjfNseABh88bGh2U5dp00IoQfipuKPZJqwwlDYOB1JWw8sccKUnHaNXNO1PMFPHecup-JsP9hR86G27E87IrK3iqtHfzLCXddmTgNqxtbXO6FFiIXMNfbEJZRNX8t9xPLedOH-nLxDn-c5JB3UMa3Q_QhXNc1qxH9RjgFIfUZs4QJ6_6TMbA-9ChxjvnTI7amDhA-9Krv2v72gd2Ooq693UhE-UlgSxFernNCJRBb2p-1DeaVZTtaq77HuT-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=gUPoda5aMQDkU_64hQoOjpAn5P9nOKpnaZmDZ5YW7mSNt5vZoRIaaUWSQ-rIpxksySfj-9cn-gQPG-rggd9zfk7VHIjfNseABh88bGh2U5dp00IoQfipuKPZJqwwlDYOB1JWw8sccKUnHaNXNO1PMFPHecup-JsP9hR86G27E87IrK3iqtHfzLCXddmTgNqxtbXO6FFiIXMNfbEJZRNX8t9xPLedOH-nLxDn-c5JB3UMa3Q_QhXNc1qxH9RjgFIfUZs4QJ6_6TMbA-9ChxjvnTI7amDhA-9Krv2v72gd2Ooq693UhE-UlgSxFernNCJRBb2p-1DeaVZTtaq77HuT-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRjtuRE5YIhU0rjl3vAMo1815PjhtAcGSyeoWlsXbSd7tZSmorurk-bxtrJlGql0QOQxbgJJG2YceXz1HlKkwA5D-Jq0_fLbeijuTIFdwZoyfuVci098ZRky-rjXuBrbtbE5OYzmtsYaN5C37WFQVvlCde4dZJfZRTBTMQAjZubtFwaVWnxwVZNzn8ZeBvZEXIg597twAJ0lPmipeMaOCLR1B-nxW_OHq04CaRUqSAV7uiwlSg9DqoX9JW3xn7u3MA5RzaLTRHNH5llQ5fVsbnsNN7q3K5lFHUQI1orzPWWZAy4m0r-6LjX9Gyjqk6dx0FNgU7X94sZYtI5WcBq46g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzmFv7eWrel5IH4vtyspiu4R_RGNhICDvUd1Fbfj6Rfup8OKn-n0eyJC1pkHN66b8bFCPiFQlWLFQvuBlP5Vx28zG7IudMneWNUeL6oSAAd-OnMmND0Rgx5VhC-x8QV1oSyUXxP_KEjNwd7ayJtMl-Hfp3MHiDya0mwVtFxQGNYIsF5Io--Ipn3duBQKvc9sc3MnMNxtuIWoXwXx6XXoK2jg0t3ETKUhyalkYl4iuYmD5ahC8z-lmbIDy5Sp4dRaqjfnsvD3mdk9PNHmZwkz3KWyK_C9h75WQ_xvrHBlxRoAOef_kfjPysO_XHKfUXgiunrZCXuCNH-xACC_7czSsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=KEt8e9pmBAu3ESed-QFGHy0SmIouod56GTaySoVhoqP6KrBo9SV-CJfsljvT3eJBOkYzu4dkFtKfU_QpiKe4BDaxB2gv9alvFUbqTFO5iXcb3Ig00JeMWqU06-DO25dsWT9JX4z6NwzPgIIen9jVlOHd49b_UkgLxSbMKg59_JuF3Y-Bx0FaecekXNb-tI8S2dntScDCZo29vzDTJePTq3IW7iP1EQ_o9R4O_6iGbfqyEgicWEFzMm7WUqXOfDN_KjHa_sN5IRAydk8_fE7Z0I2ufrItFCMesBI7To0tAgWAQbbdCbkIS0qYVujT28PdeC0rhIg9PKJ4JcgghkgthQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=KEt8e9pmBAu3ESed-QFGHy0SmIouod56GTaySoVhoqP6KrBo9SV-CJfsljvT3eJBOkYzu4dkFtKfU_QpiKe4BDaxB2gv9alvFUbqTFO5iXcb3Ig00JeMWqU06-DO25dsWT9JX4z6NwzPgIIen9jVlOHd49b_UkgLxSbMKg59_JuF3Y-Bx0FaecekXNb-tI8S2dntScDCZo29vzDTJePTq3IW7iP1EQ_o9R4O_6iGbfqyEgicWEFzMm7WUqXOfDN_KjHa_sN5IRAydk8_fE7Z0I2ufrItFCMesBI7To0tAgWAQbbdCbkIS0qYVujT28PdeC0rhIg9PKJ4JcgghkgthQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله به یکی از پدافندهای همایی غرب کشور توسط اسرائیل.
این انفجارهای پشت سر هم مربوط به موشک‌های این سامانه است که یکی پس از دیگری منفجر می‌شوند.
این سامانه پدافندی قرار بود از آسمان کشور دفاع کن (با شلیک موشک)
ولی اسرائیل بهش حمله کرد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=NFF3CHXtJJPFKqFOvt5a-peke9xCX2Xf9lGqmosll94rgi5wz9Bp2sceIPBuZzaDBoJ0uDD-ES0XScFGnXpfQW0iqB0MHpSzqeVPOqwjDwLCDBdKvR4jzy5KMZczHB0zhX3C8E_H9b0psf9FEQGAyONRmTWO7Hef3GKRhYy6Cnn_53kr2VPdaF2K4zb6hwVs8x2xXINrj5QqM9xRjlydAJ7yrothqtxOCQJSmiDW9WpB72n6HD2K-E_h8tiDqB9_dz73b1gs15d89IzWLgX2MzVHtOw06Q1IhJzessCyLTTgMHix_4czttBojELLiAeNy9Ly1pT9luMJidKbS6TQ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=NFF3CHXtJJPFKqFOvt5a-peke9xCX2Xf9lGqmosll94rgi5wz9Bp2sceIPBuZzaDBoJ0uDD-ES0XScFGnXpfQW0iqB0MHpSzqeVPOqwjDwLCDBdKvR4jzy5KMZczHB0zhX3C8E_H9b0psf9FEQGAyONRmTWO7Hef3GKRhYy6Cnn_53kr2VPdaF2K4zb6hwVs8x2xXINrj5QqM9xRjlydAJ7yrothqtxOCQJSmiDW9WpB72n6HD2K-E_h8tiDqB9_dz73b1gs15d89IzWLgX2MzVHtOw06Q1IhJzessCyLTTgMHix_4czttBojELLiAeNy9Ly1pT9luMJidKbS6TQ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFtZg_DzJha6rwQn9DpbG1sMf4ipSijL0BYJf5duM3QhYtZyuAFYFTfRKXmJfNxpwgWEoo7lY_c0mFj5jfkV0Lvg6lYe4HQgZVlbkvNMvG0qgoarDk7NrbxTbj8VKClll7i-8RoSSrqJOP2R-2kkRBdjK-gP24D1LzkRqwkbXNeKF4n3DN5bNciIEklTynTlF-teBPZR5hTZ1LrFlMTuljnwlrHHyzfKARwYakK--TKuaYRq6Zhy6sQFIDVj0PyP6fh3v8_MsdKhdyfiHtGRGIVwiVB5pISZlDxX67LXVKdZl2dVhmkC4i0GleOLw9sHq0Uzdc0QkQUjSk8DTTdc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=EcAU5fOKk-2hU-B1vF-boqPazlzaPDCe0JmUm_xvJcnNx_8OyuAHSSaIBn1yAziiP22-P6lTcK-7O0NkVMDeqE4RpdOPUgEU2rlW0wc2O6lzaoKgQTY9rCBsX-KEk4W0lBWz5b3A1U3qlv02VVYCDHZ9k0X3QMofR0LFtHlIPWvSUKUU4OQ2MdJfG1MWlvK9GJ07Uwb1jZrngZgZGY6bB9P6wmZrX_TorF-6AU6q74NdmmWIncTP47WaWHCCFKdoSZ8XBTFtcgDXyDfNS7euwvuz1w7JQIRvQLE325ntryWo8cP-tb7jnrDQUjVIBC370yDQ5628TYHfNbZdXxqd7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=EcAU5fOKk-2hU-B1vF-boqPazlzaPDCe0JmUm_xvJcnNx_8OyuAHSSaIBn1yAziiP22-P6lTcK-7O0NkVMDeqE4RpdOPUgEU2rlW0wc2O6lzaoKgQTY9rCBsX-KEk4W0lBWz5b3A1U3qlv02VVYCDHZ9k0X3QMofR0LFtHlIPWvSUKUU4OQ2MdJfG1MWlvK9GJ07Uwb1jZrngZgZGY6bB9P6wmZrX_TorF-6AU6q74NdmmWIncTP47WaWHCCFKdoSZ8XBTFtcgDXyDfNS7euwvuz1w7JQIRvQLE325ntryWo8cP-tb7jnrDQUjVIBC370yDQ5628TYHfNbZdXxqd7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط یکی از موشک‌های جمهوری اسلامی حوالی شهر فلسطینی «اریحا»
دفعه قبل موشک به یک روستای فلسطینی  زدند و
۵ زن فلسطینی کشته شدند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
در جریان حملات اسرائیل، حداقل به دو سایت پتروشیمی حمله شد که هر دو استراتژیک محسوب می‌شوند:
پتروشیمی کارون در ماهشهر و
پتروشیمی سلمان فارسی ماهشهر</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5404" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnP7IscMY4J-pHsyl2w6ULZ50pqHzoVYENQi1BW0pH0i3PHhSb4D-7jLxbYHVBO47O-CseEj4dYDx5W1arUJCH_Lcxv1yPVKDng0_gMwBYW6TbU3Pr3UOFBlr0W_YddbtjAtVUO5IPsV3fIsoetvGx7FO15WAtkIxk8OUDdE7Wjq804d_tjPAMsYrjArPHLGP7KAV2tJk1A42zv-ok3lKUebkF97y54W0M3oao34Ko9QORsHCFtbY8FD00sUyLJRc92UPuBjsH5y7akZMV1NeqlYSKyzi_a2lgB139sUghbGgffIKdHgRUspDuk6Qyc_8J97Ccign6VpgagPxrsjqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ : اسرائیل و ایران باید سریعا حملات خود را متوقف کنند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5403" target="_blank">📅 13:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.     دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5402" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCbzRMwPHbxeQcLxxt-Ukx9dw1TuHDAOqLm49z8H7Atj46BMOeYA1M0CAdkmBpP3pPm0vFqk-ksHZwkOvcG3cvilgjYK9G1_py-VbLiJXOhvhxxOyLbL2WptaGFXDf2vkQwLoVaax6SKUeq6HdiccypHtGZ1PU-a-ERET1E-qoiWKETZP5MFdxWTnkZaoqWehtt3SR6sk_rMzZQVbj1xh0bqWsUnhnR9SoENk7hlDgM7KfPxBe2zhbrtzlpt56MhFPG-bpbBMq2qEgMLgpbf4OgqWMEXD_zhyDSTa-lsxLDFJWlbUrgqK6v36B88iM3WeMSN-dl-Xnxfk2JJEbej5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5401" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
انفجار در غرب و جنوب تهران
🚨
انفجار در فرودگاه شیراز
🚨
انفجار در کرج</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5400" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2Fo2-nKCiLKiw7wP4SSLdXd1Kpy-YIOLgfotMMEb6F9-pHbhpdzfEGUbVocT4tva29xENKd5duEI50yG4wyZ28jZH7j9SKhFULib3CInPnk-3dMML6y-7hjgEqGOiJbSV85XZ4xbxjl9yonOZ94LcoGTSmhJFMBJax5px6BXO-9Cz-2rzGHirbMRQlLojdXqWyzxwGXX8fwpd1iREd_6IK6vj9UGfY_6DvhvtTqsDQrdsBeGzjaIADG8JOg4ZqPWCipl3IdwZoOzIEqyGEjjcqwRc_h9nnhEXHMSBMSfTf16v29mVVJlUtbQSwWD6AaE8mio8iIpr5oPo9v77HsMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداهای انفجار در تهران و اصفهان
🚨
حمله به دانشگاه هوا - فضای سپاه پاسداران در تهران.
🚨
گزارش‌هایی از حمله به یک ایستگاه متعلق به بسیج در کبود آهنگ همدان
🚨
جمهوری اسلامی در پاسخ به حمله اسرائیل به پتروشیمی ماهشهر : صنایع انرژی کشورهای منطقه (کشورهای مسلمان عربی!) رو هدف قرار میدیم!
تصویر : حمله امروز اسرائیل به تهران</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5399" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5398">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN5J5WpTTXNFd32mpDOWHrDG4byywCjm4NtNt_jNM8nEhnrp5Hs9N1XINsSCIF5g8zCITf5I5VVdlfTv9_rBjxoHFR_BZHUTIzeGIEEzgfbqh523Y6QWeH-ZuKjLWliOFh-Jg5H5IRYWPRAJTG_SuRuO59ZxnGzmxlHpGimz7nGnIBHJ7uvhMoHW1I_aat4jennYHggOygQruFq2oA_zQNFqlbRKwuYKS_vfI_1jEj2QyGrPdjHTJwtAvITkgoevBsb_JQjqZRUa8xI3swklugUB4gwyQaASbQgI0NbUPKWwQm4dDi0eSUoP9IMXafsBysuGpat_orD8nZhQ3yKzwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5398" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">۴ موشک جمهوری اسلامی به سمت حیفا و ۲ موشک به سمت تل‌آویو شلیک شده‌اند.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5397" target="_blank">📅 10:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5396" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5395" target="_blank">📅 09:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">جمهوری اسلامی از دیشب تبدیل به نیروی نیابتی حزب‌الله شد.
وقتی جمهوری اسلامی در خوزستان ، تهران و کرمانشاه جنگید تا ضاحیهِ بیروت بیروت آسیب نبیند.
مقامات ارشد جمهوری اسلامی بارها و به صراحت گفتند که نیروهای «نیابتی» را ساختند تا آنها سد دفاع از جمهوری اسلامی باشند،
مثلا خامنه‌ای سال ۹۴ گفت :« اگر اینها مبارزه نمی‌کردند، این دشمن می‌آمد داخل کشور... اگر جلویش گرفته نمی‌شد، ما باید اینجا در کرمانشاه و همدان و بقیه استان‌ها با اینها می‌جنگیدیم و جلوی اینها را می‌گرفتیم.»
یا قاسم سلیمانی گفت : جمهوری اسلامی امروز در سراسر منطقه دارای عمق راهبردی است. این عمق راهبردی نه برای کشورگشایی، بلکه برای ایجاد یک سد استوار در برابر استکبار است تا دست آن‌ها به مرزهای ما نرسد.»
یحیی رحیم صفوی : «خط دفاعی ما به جنوب لبنان و مرزهای رژیم صهیونیستی منتقل شده است. این توانمندی مانع از آن می‌شود که دشمنان به فکر تعرض به خاک ایران بیفتند.»
دیشب اما جمهوری اسلامی تبدیل به نیروی نیابتی حزب‌الله شد!
داستان بر عکس شد!
جمهوری اسلامی دیشب در خوزستان و تهران و کرمانشاه و تبریز درگیر شد، تا دست اسرائیل را از ضاحیه بیروت و حزب‌الله دور کند!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5394" target="_blank">📅 09:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=MU7KnaUSB3eC4fcgYo-iPGU-noPJFnHpLFmZ7dL_WER1xI4wyvovrAIO1NAz1Ypp-UloCywdlaCjSQ4xey_LIgEXxcItw_w6j2IXLptLIFvCsw_ASzRdFPAM_Yc23YQXxRz7hLJhFwD7tHT8mmcgrt4DnfmSD4UzQVkL_8v0LVL6rvhVLR_IBkK6L-obYou2kbZQOjXjG1yBXAYIgV0sqIwwrLFkmFb_D_qZP2PiG2nRcE8XEy1ev2iUyvF-pY-TaePfQPPwJfzY5Ap7Sd3uEU-SgZD_0YSPBecdpMvoB7-dK2sA8b5q_TynAhuL0rSILpJNWQd8wIBDsvOeLuv4FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=MU7KnaUSB3eC4fcgYo-iPGU-noPJFnHpLFmZ7dL_WER1xI4wyvovrAIO1NAz1Ypp-UloCywdlaCjSQ4xey_LIgEXxcItw_w6j2IXLptLIFvCsw_ASzRdFPAM_Yc23YQXxRz7hLJhFwD7tHT8mmcgrt4DnfmSD4UzQVkL_8v0LVL6rvhVLR_IBkK6L-obYou2kbZQOjXjG1yBXAYIgV0sqIwwrLFkmFb_D_qZP2PiG2nRcE8XEy1ev2iUyvF-pY-TaePfQPPwJfzY5Ap7Sd3uEU-SgZD_0YSPBecdpMvoB7-dK2sA8b5q_TynAhuL0rSILpJNWQd8wIBDsvOeLuv4FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی  جمهوری اسلامی به اسرائیل و  واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5393" target="_blank">📅 09:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔺
وزیر کشور پاکستان صبح امروز تهران را ترک کرد.
با پیامی که مهم توصیف شده بود، از سوی رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان، دو روز پیش وارد تهران شده بود.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5392" target="_blank">📅 09:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=EM0_zEdjPCBegPiDNaRys7rdmyvzJSX1Y6x1RU-I7_-4yc_o_Io14NZQA-cu2VURH1fB-49MHZDeCNHbZ3exsxHZYd_iGwNsX8tfH9zKk0dPPUg8qN252SQSuhzINYlVCxwT1WIw0qAVRIfc09p4tX2-USubIjdzQ_bvBkplbCmYwo7iM9XM2lnPxQ8BSyk-icTp5CjDWWYyxQWFH2Wcwmm3bh19pBQLx3Rc8Zq15aVJ7ikJXuRhTYlVldBFj3lufQJyfbA9dS_yJe3j6D7XWH5irzH0wWXWQgyPGKjjbQktEHBTNNGUTvaWFosgCUPrL5q3AJfcBAFKR6qGB5sTGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=EM0_zEdjPCBegPiDNaRys7rdmyvzJSX1Y6x1RU-I7_-4yc_o_Io14NZQA-cu2VURH1fB-49MHZDeCNHbZ3exsxHZYd_iGwNsX8tfH9zKk0dPPUg8qN252SQSuhzINYlVCxwT1WIw0qAVRIfc09p4tX2-USubIjdzQ_bvBkplbCmYwo7iM9XM2lnPxQ8BSyk-icTp5CjDWWYyxQWFH2Wcwmm3bh19pBQLx3Rc8Zq15aVJ7ikJXuRhTYlVldBFj3lufQJyfbA9dS_yJe3j6D7XWH5irzH0wWXWQgyPGKjjbQktEHBTNNGUTvaWFosgCUPrL5q3AJfcBAFKR6qGB5sTGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی
جمهوری اسلامی به اسرائیل و
واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها
میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5391" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBCUQlrbjYJZ0UXEXrXBgxLEBYzlffa-aTveZDtxzVF8vGp_-pMIdUVY424NCnNCEA0arQfNNaVsJmchQ7cdn56hqmDtlGpcGeWYHuyJXVsECIuyrYPAGfMaUz_YYSsfuW5VwyxuVs0FU9-VRTGdW-Lzoy5qpavSj-eooO94qjUKrhpvQ0ew0ALLbA4l1fKXOUE5tCUZV6sR69kFKkJsMRfEo8yarnwGG_kt4NzX7sZrdupVhAhaJojH7A89p5INKLP8A1Mt_QOJmmNs06bxJJsGjqbdYr_GMiHnP8HDlEIieReUlFlDijG9SzKNNJdvDziRs-IqxB3UM0Hl2AgSqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاریجانی هم صبح زود از اون دنیا توییت زد که غم ویرانی ایران رو نداریم!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5390" target="_blank">📅 08:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5389" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qic7lVdv3C1s3PQiSku5SI8fJF0xBB8YTAbybVqugrG2OEXekIa6DRPAC2PJbwjcIB2lzpVgXTYJU-e8VWaRLyE0yJ5o9uD6jKstv3AiRKxs84Yzloe7IG6WxJwFGJDggrgo0fmJQwYE57PKlyGcmxHvdeAGBCuDVUwjr-7oLB-WvcUJiZGOINqeHCq-rtt6VBPPiupDOK2_1Ez-GMfKHT4mOti76z2Jra7drCHoHY01xs8Oe04QK_1tjSSQwIuz9j3NFzoUMpWZOxEZylL_ll41HXuxBXiPKsdxW1iMWEg51sNU_CuWkm00ZGHpSCYg9fXVY65Ara3EoLhkM35yDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5388" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای موج جدید حملات است.
🔺
کابینه امنیتی اسراییل تا ساعاتی دیگر برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5387" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تاکنون : حمله به تهران، تبریز، ارومیه و کرمانشاه گزارش شده است.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/5386" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل رسما حملات اسرائیل به مناطقی در غرب و مرکز ایران را تایید کرد.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5385" target="_blank">📅 04:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجارهای مهیب در تهران ، کرج و اصفهان.
کانال ۱۴ اسرائیل؛ آغاز حملات اسرائیل در ایران</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/5384" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اسرائیل ارسال هرگونه کمکی به غزه را قطع کرد.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5383" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یدیعوت آحارونوت:
🚨
🚨
در گفت‌وگویی که لحظاتی پیش پایان یافت، نتانیاهو به ترامپ از قصد خود برای حمله‌ای قدرتمند به ایران اطلاع داد.
رئیس‌جمهور آمریکا تصریح کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/5382" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5381" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یدیعوت آحارونت:
ایالات متحده به اسرائیل پیام داد که بهتر است چند روز صبر کنید تا ببینیم آیا می‌توان به توافقی دست یافت، و اگر نه، ما طبق برنامه به اقدام مشترک ادامه خواهیم داد، و ارزش ندارد که این را با درگیری‌های محدود تلافی‌جویانه هدر دهید.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/5380" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrbHrX6PXwn9IOh9YzOul8yUMCRXAOuO4cJdyExYADlXQ3x5JxiQZjuW__uPeFDQJBz2pH-etd60-Mg4qMvgWLzkFfXEMFXlWM9fmgAlAmiVEZAF9kcfqt2J-srJoatKgouzd0bdWc9Q-XUMKkMtKo4UnoJO_5hcOnjXLh1Bty77Np4DkUt60iBsG4e7_b30bbGMkRQ41ente3b3Shk3pz5ms3yI1xCBlQvfnOui334QXiFF2SdzEDGYsDlqLeh-rWGLeRYvd42uujN383cpOk2-FDIiZYlmBKPOk37W9OYWtC9xh_Kgm--RfiSFyn-u_jMJyig4Hd-21ld1tfMUrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.   گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.   ولی این بار رو بعید می‌بینم. عدم پاسخ اسرائیل، یک معادله…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5379" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رهبران اپوزسیون اسرائیل، نفتالی بنت و آویدگور لیبرمن، خواستار حملات قاطع به جمهوری اسلامی شدند.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5378" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrcvOUn91yJkditBcNlqBnH25entth1Mreu30G1NPQ8fcj_S-hMpaPNkfnS1yn_7UjRuW6_UB1dabZwy1wJ6-tCTkJhKMsJWdXKxzbAfoYzZUXgWcmCZTvUh4DYrIHvByIIsGPzZEVQFOotyJ9omszxuf83hAEeZgUJFirA7rpAL-7FKly2X2AibV13OcLPrt7ZlUl27sAjGlL9R93im9ILT6bMzHuQjocCbA6DVLnhS7Kwx1cZVIgzMWb-2Cbzgp6e4iVKI7JqGhXZz9Pt1sC6WO8VaXKRe3AdylF9ufU1q3LiECrSlo-UGoim3gdccvUOEAbXj6HpJudddxaBYsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ وزیر خارجه اسرائیل به توییت عراقچی.
عراقچی پرچم جمهوری اسلامی و لبنان
رو کنار هم قرار داده بود.
وزیر خارجه اسرائیل ولی پرچم حزب‌الله و جمهوری اسلامی را کنار هم قرار داد و عراقچی را «شیاد» توصیف کرد.
اشاره به اینکه جمهوری اسلامی حامی لبنان نیست بلکه حامی حزب‌الله است.
🔺
یادآوری : دولت لبنان سفیر جمهوری اسلامی را اخراج و جمهوری اسلامی را عامل  جنگ در کشورش معرفی کرد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5377" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5376" target="_blank">📅 00:21 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
