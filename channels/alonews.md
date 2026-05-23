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
<img src="https://cdn4.telesco.pe/file/GF3qY5PHxQrJubVCVnqCBGxJVuDmbjZNpZDpQWCvz4v6KP8LR91hMGs76EOdmBEHKmQ_2dTU_673JQVt-OZ4X6yM88Fcjoi15jLKz0odBD0-LkMpW6L6w4ZjVOmV-w35U9xBVskEvkAg5Aaz--V0vghYMO0Wz4gI1qtyBp7r4dWTyEttM2ks_lpiJeNPQmbvwfMedrMWh9VjicJ_FZZuhtjyP2MwPvOELM_0yxjWcup1Lx2bVUsmFkT2igAzFJjoXqAMJwJqbISNB93xZxbEI5jrhCF5bbcKXGiLKBRw7gnBRg-rHEW6sJJ3X5O3xLuohUGt7smAjsvfU5LrM4XOfg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 940K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 18:15:48</div>
<hr>

<div class="tg-post" id="msg-122064">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ارتش پاکستان
: مذاکراتی که در ۲۴ ساعت گذشته انجام شد،
به پیشرفت امیدوارکننده‌ای به سوی تفاهم
نهایی منجر شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/alonews/122064" target="_blank">📅 18:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122063">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
الحدث:ایران دو مسیر برای مذاکرات پیشنهاد کرده که با اعلام پایان جنگ و محاصره آغاز می‌شود.
🔴
ایران تأکید کرده است که در متن یادداشت تفاهم، به عدم تولید سلاح هسته‌ای متعهد خواهد بود.
🔴
ایران خواستار حفظ حق غنی‌سازی در هر توافقی شده است
🔴
ایران پیش از مذاکرات هسته‌ای خواستار آزادسازی دارایی‌های بلوکه‌شدهٔ خود شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/alonews/122063" target="_blank">📅 18:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122062">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4fd66f216.mp4?token=s6yTswWGgze4sshJDzG8_BYXSN9W4mqGXer2_LJ0C7j203mNhERwTgxtvGmjjIuhlM0gmajr8jAPBK2XAkUuE3RL1ZW3Jew4zQYtuNCvUwc6pHzAlHTufcomn-gI8trMyaaoxVoKYBtmJzuqhuyqvHVJxsE0hYhq8Dzzb8QxR9y2gjcmCv3qTl2-Xu_y7-hVxEzR4Im283J4Qh5id30aatgFb-TRkUUSGCs4nNFwLlKjUS4s_KvacqSo8hElZ-R9A4hUyD5wYmzoWtbzEIAe0cvdTTmn7F2Ruhnp6qsGGtqrfw7dSIgiRwkj4aCFLIG2dFFEgEgu7_7Po-okBJV0yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4fd66f216.mp4?token=s6yTswWGgze4sshJDzG8_BYXSN9W4mqGXer2_LJ0C7j203mNhERwTgxtvGmjjIuhlM0gmajr8jAPBK2XAkUuE3RL1ZW3Jew4zQYtuNCvUwc6pHzAlHTufcomn-gI8trMyaaoxVoKYBtmJzuqhuyqvHVJxsE0hYhq8Dzzb8QxR9y2gjcmCv3qTl2-Xu_y7-hVxEzR4Im283J4Qh5id30aatgFb-TRkUUSGCs4nNFwLlKjUS4s_KvacqSo8hElZ-R9A4hUyD5wYmzoWtbzEIAe0cvdTTmn7F2Ruhnp6qsGGtqrfw7dSIgiRwkj4aCFLIG2dFFEgEgu7_7Po-okBJV0yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارسالی شما/سلام ادمین ماهم تجمع کردیم جلوی اداره آموزش پرورش لرستان و اینجا هم امتحانا مجازی شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/alonews/122062" target="_blank">📅 17:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122059">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7394b357e.mp4?token=YgQc6GOrjQKA0XIIZn-UCzw8onaQVI8YFFxQJI3uFA5o1-rv8PfR6d8ey-Cm3Y63s-Vkd-B_IHDYCmyaI4QF2KEPxMdURSQq7dxC2cECQh2YVe4d3wiR4Q2aHDRA8_WlVK7QcXYtgdjcQHFFidFVVCB_8y15_UuIbRcCuj8duFEBq_t7wGkTFwWU4Cp6290RKP7s6weg2RDXADnqZjgWthyz1WKCda6UkPh7P1EriiJKICJwhkipAkF3ZPjwqOG323SnAzJEGupIKJG7KXwsS38GkASy5AErG4i58jL5pH-xiHeHogmFU3uG9rZA553bStHzYJk83bw3f_1X3n0hDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7394b357e.mp4?token=YgQc6GOrjQKA0XIIZn-UCzw8onaQVI8YFFxQJI3uFA5o1-rv8PfR6d8ey-Cm3Y63s-Vkd-B_IHDYCmyaI4QF2KEPxMdURSQq7dxC2cECQh2YVe4d3wiR4Q2aHDRA8_WlVK7QcXYtgdjcQHFFidFVVCB_8y15_UuIbRcCuj8duFEBq_t7wGkTFwWU4Cp6290RKP7s6weg2RDXADnqZjgWthyz1WKCda6UkPh7P1EriiJKICJwhkipAkF3ZPjwqOG323SnAzJEGupIKJG7KXwsS38GkASy5AErG4i58jL5pH-xiHeHogmFU3uG9rZA553bStHzYJk83bw3f_1X3n0hDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جدیدا دانش آموزان استان‌هایی که امتحانات‌شون حضوریه، می‌ریزن جلو آموزش و پرورش منطقه و میگن ما فقط مجازی امتحان میدیم؛
🔴
اتفاقا جواب هم داده و تا الان این استان‌ها مجازی شده :
- یزد
- مرکزی
- گیلان
- کهگیلویه و بویراحمد
- کرمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/alonews/122059" target="_blank">📅 17:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122058">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران:
منبعی به من گفت که فرمانده ارتش پاکستان قرار بود یادداشت تفاهمی بین ایران و آمریکا را از تهران اعلام کند، اما
برای تکمیل هماهنگی‌ها با ترامپ
، تهران را ترک کرد.
🔴
منبع تأیید کرد که پرونده جنگ با تمام جزئیات آن مرحله اول را تشکیل می‌دهد و آنچه به مسائل هسته‌ای و تحریم‌ها مرتبط است، به پس از ۳۰ روز از توافق موکول می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/alonews/122058" target="_blank">📅 17:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122057">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا: تنگه هرمز باید باز شود؛ ایران نباید سلاح هسته ای داشته باشد؛
🔴
ایران باید ذخایر اورانیوم غنی شده خود را تحویل دهد؛ معضل غنی‌سازی ایران باید در مذاکرات در نظر گرفته شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/alonews/122057" target="_blank">📅 17:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122056">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c565cc9c05.mp4?token=gt-EF7bEjwOSPqD9LcBF0u76e8ii96ZFEVxMHuAUET6csbgKhq0H8398DO2oeWcnoGPntSqgTgd5ovbs-z1AC8Ad-6ASxT7aTV-BT0v8im3Iz8gvcOBl_Tmeezih7dp03zSQkDKsUyk9wUwAmaKPbHe934F7y28pKJ0SXbluKeLVx1ZyjzKo1UGv1Flb4m4E99rZ_mGeNcvMSN5ZNckp4b83_1T4URPLqt21gUkpLJ8kNtY_YmErzAgGw2yS0QtUCS92yWlVMopAfQF78YBN7emIPLzkv6Ee6rYOP3UcxOjNQbI6r-3157dqNKaAtlzNh2EzRsa2QRln6FURsoCo2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c565cc9c05.mp4?token=gt-EF7bEjwOSPqD9LcBF0u76e8ii96ZFEVxMHuAUET6csbgKhq0H8398DO2oeWcnoGPntSqgTgd5ovbs-z1AC8Ad-6ASxT7aTV-BT0v8im3Iz8gvcOBl_Tmeezih7dp03zSQkDKsUyk9wUwAmaKPbHe934F7y28pKJ0SXbluKeLVx1ZyjzKo1UGv1Flb4m4E99rZ_mGeNcvMSN5ZNckp4b83_1T4URPLqt21gUkpLJ8kNtY_YmErzAgGw2yS0QtUCS92yWlVMopAfQF78YBN7emIPLzkv6Ee6rYOP3UcxOjNQbI6r-3157dqNKaAtlzNh2EzRsa2QRln6FURsoCo2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو : شاید امروز یا چند روز دیگه درباره ایران خبرای جدیدی بیاد یه پیشرفت‌هایی شده
- ولی ایران نباید سلاح هسته‌ای داشته باشه و ترامپ میخواد قضیه دیپلماتیک حل بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/alonews/122056" target="_blank">📅 17:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122055">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری / روبیو: فرصتی برای پذیرش توافق توسط ایران در نزدیک‌ترین زمان وجود دارد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/122055" target="_blank">📅 17:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122054">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/122054" target="_blank">📅 17:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122053">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrCrdTGh4exDQoryZ4QmpBVOY8zMlf3WRGWsGNzJYlDcr3lhyWzx3CAnSVJB_iJYl_j2XO66PL_O_azBPagP6gAoZ8xFrCdM7pwn_RYwheBuEtZmFnXGoSuwPUJAiHFSEtlad-H_4gdOrGfFkNvRCi_5f9JDJQl4TmmpEmpGfKnGOYC_G_BSTQTd6Fd3Ex8FYSOX_iL5yMMwTNNxA5dTFgbj7OEB4wRfJ8aguxVPKGg_topx69ab84dyKFrhS12uPQ9ntm7n6v2NNafWb-REuWkhgzxf7wxsieG4XL2MiD66lbKfpUEOlxWijN9oiB1Q75fsYzWHxrq2MgPtrSc1jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
9️⃣
8️⃣
1️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
💤
این تخفیف فقط تا ۱۲ شب فعاله
💤
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/alonews/122053" target="_blank">📅 17:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122052">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تفاهم‌نامه چهارده بندی هم موضوع هسته‌ای مورد اشاره قرار  می‌گیرد و هم موضوع آزادسازی اموال بلوکه‌شده.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/122052" target="_blank">📅 17:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122051">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوری / روبیو: فرصتی برای پذیرش توافق توسط ایران در نزدیک‌ترین زمان وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/122051" target="_blank">📅 17:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122050">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تفاهم‌نامه چهارده بندی هم موضوع هسته‌ای مورد اشاره قرار  می‌گیرد و هم موضوع آزادسازی اموال بلوکه‌شده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/alonews/122050" target="_blank">📅 17:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122049">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
یک مقام ایرانی به شبکه الجزیره: قطر نقش کلیدی در تهیه پیش‌نویس این یادداشت تفاهم ایفا کرد و بین میانجی‌ها و واشنگتن ارتباط وجود داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/alonews/122049" target="_blank">📅 17:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122048">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه:  پیشنهاد ۱۴ بندی ایران که چندین بار رفت و برگشت شده و در خصوص بندهای مختلف آن دیدگاه‌های طرفین تبادل شده است و در این چند روز راجع به برخی نکات و عبارت پردازی‌هایی که راجع به آن اختلاف نظر کماکان وجود داشت بحث و پیشنهاداتی مطرح شد که همچنان برخی از آن در حال بررسی و اعلام نظر است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/122048" target="_blank">📅 17:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122047">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
بقائی: حضور هیئت قطری در تهران برای تسهیل برخی بندهای یادداشت تفاهم بود
🔴
میانجی ما در مفهوم دقیق کلمه رسما همان پاکستان است. طرف‌های دیگری هم هستند که تلاش می‌کنند کمک کنند. ما از آنها تشکر می‌کنیم.
🔴
قطر یکی از این کشورها است.کشورهای منطقه به دنبال کاهش تنش هستند.
🔴
کشورهای منطقه شاهد بودند که تجاوز آمریکا و رژیم اسرائیل می‌تواند چه آثاری داشته‌باشد.
🔴
حضور هیئت قطری هم برای کمک به حل‌فصل برخی بندهای تفاهم بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/122047" target="_blank">📅 17:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122046">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
العربیه: تهران در ازای پرداخت غرامت از سوی آمریکا به ایران، پیشنهاد بازگشایی تنگه هرمز را ارائه کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/alonews/122046" target="_blank">📅 17:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122045">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری / مقام ایرانی به الجزیره گفت: ایران نمی‌تواند امتیازاتی بیشتر از آنچه در یادداشت تفاهم آمده است، بدهد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/122045" target="_blank">📅 17:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122044">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
یک مقام ایرانی به الجزیره گفت: این یادداشت تفاهم شامل مسائل هسته‌ای نمی‌شود زیرا این مسائل پیچیده هستند و به زمان کافی برای مذاکره نیاز دارند.
🔴
30 روز پس از توافق، می‌توان درهای مذاکرات هسته‌ای را باز کرد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/alonews/122044" target="_blank">📅 16:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122043">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
بقائی: تنگه هرمز به آمریکا ربطی ندارد و این موضوع بین ما و کشورهای ساحلی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/alonews/122043" target="_blank">📅 16:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122042">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
یک مقام ایرانی به الجزیره گفت: این یادداشت تفاهم شامل مسائل هسته‌ای نمی‌شود زیرا این مسائل پیچیده هستند و به زمان کافی برای مذاکره نیاز دارند.
🔴
30 روز پس از توافق، می‌توان درهای مذاکرات هسته‌ای را باز کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/alonews/122042" target="_blank">📅 16:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122041">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری / ادعای الجزیره: مقام ایرانی تایید کرد با واسطه پاکستانی به توافق رسیدند و منتظر جواب  آمریکا هستند!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/alonews/122041" target="_blank">📅 16:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122040">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری / ادعای الجزیره: مقام ایرانی تایید کرد با واسطه پاکستانی به توافق رسیدند و منتظر جواب  آمریکا هستند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/122040" target="_blank">📅 16:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122039">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcmKACQA881OZ3ZrsYAgIpJiOrui1Rv9R7w0WeH9azQb_-WS63jCmEM1JUnqpTHCWqxYDPb3oq0zFWYLN9Ra5JY4UuKyJCBMcNsrk9ryHwDkuXPU_ml87eXIhVSw3fiIjkg969fVG2hsL_HIKQpMufmGvpPZa2Aw60Eu-7nA-teAj_Rv7x-tVNknSJq2ia4md7pdohGqmWN1CM8-CYKc5SE0C9Ki4h3cToYw7Ho1j9iEUdh8ZXpn4GJSa3sIUfamuPaPtdiQ982T8nPr_FRL9oMJylIAZ2WMUM_ybFpYNJdRU5Z_kDQkJgyuqeFCODTyhGf4jQWkEDT-uCDHvbWOvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ درباره رو کانا: یک دموکرات!
🔴
اجازه ندهید این دروغگو و آدم کثیف در فاکس نیوز باشد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/122039" target="_blank">📅 16:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122038">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-blWkxEkwd3vZJF3yXu6P0JR8GGc91sGPeWOYkqkioNi_LyzjkxO-YxuUj5ExIrOiv_4Zax5qdS3qbw9Qe79ACwYRvpUCH5Obuv8sLWAkHNCiuzIJ7NxB2fC29l0KQXNh6Zh7YQLz4kdZX_bbu0qmuRwjIAxfEybgqjBc47_YHjQ9Xcy2tCwY-TEnV6S6QNjtppzPub000C0cJZdi4Kv38VXp5Gun2gB3sM9EryhA7Z7QrR-JbABwKYI4nCCCUI9NWQFPGV16NlITfh_sVFZyRgTfhYUL-C2hWlU_Moxsj9cM6TlLN2Vmol8jik0OFDy26tD0ijQUsmTGES2Dr0Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید و عجیب ترامپ با نقشه ایران : ایالات متحده خاورمیانه؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/alonews/122038" target="_blank">📅 16:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122036">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4354c59d.mp4?token=AgBIVPYFbybogL78sHDL2oHh00RhBk0TFstIC_KgRIDliSPCFkH8WSba3le3Kl3HvAhFLks0D46mNZVwcj4kdQ9D8I7D0Ghw-s_YG3fcCxCnE2qz8NDeCoLJSlcFJAE5DwXPM8meXE5nKGBOpoXHI7FscycuLiXUFXAbhoRuc3f5ce7l3yRYBaQcZMDLt9lqbYDa_OPVlsck_JD_4tHyRRTwjwlysKoDrtEL802Tgiw0j986G4PakrAnRIwHdurNatlD9hwLMrPG0t5CYvGeodS57ZIQLZ9pN8hOEIpTHvZHI_8uG8MPGqbGpIoAjY2eC15x3mXi-qlhIDJOKn8RUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4354c59d.mp4?token=AgBIVPYFbybogL78sHDL2oHh00RhBk0TFstIC_KgRIDliSPCFkH8WSba3le3Kl3HvAhFLks0D46mNZVwcj4kdQ9D8I7D0Ghw-s_YG3fcCxCnE2qz8NDeCoLJSlcFJAE5DwXPM8meXE5nKGBOpoXHI7FscycuLiXUFXAbhoRuc3f5ce7l3yRYBaQcZMDLt9lqbYDa_OPVlsck_JD_4tHyRRTwjwlysKoDrtEL802Tgiw0j986G4PakrAnRIwHdurNatlD9hwLMrPG0t5CYvGeodS57ZIQLZ9pN8hOEIpTHvZHI_8uG8MPGqbGpIoAjY2eC15x3mXi-qlhIDJOKn8RUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز یه عده دانش‌آموز تو خرم‌آباد جلوی اداره آموزش‌وپرورش جمع شدن و اعتراض کردن
🔴
گفته می‌شه تجمع به درگیری کشیده شده و نیروی انتظامی و بسیج برای متفرق کردنشون وارد عمل شدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/alonews/122036" target="_blank">📅 16:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122035">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a73d6b362.mp4?token=BNJ0jAbV50v5DG3J7wRViCL3Q9xhW_b_ycd49Efi91ZTaokVDwEzdJaAhM7bZug8_DMUBHXLo0w5wHKcAIf15Cv3DaLb5zoa8UbYSAaWr4j-1Y7LohzgIVhPLJAZUiOoqn3Ig7v--mNz5JIyCBgagApYVFjlRpQGVy2y3Bs8Q9pzDe0jlGJyzKVEvh7aKXuq2XhZST3YaonurBqDIPwYckjhTcywctNgstij4olnHKqllvH_aNV2d5IaFFd60adF3OKZou10pdAts6pNT_7O6-nnC7qOZdiZGhcWJexgBNVvhVROGKiF-CBhA66mCHEue6JXlJXeyrR348wUcSlZjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a73d6b362.mp4?token=BNJ0jAbV50v5DG3J7wRViCL3Q9xhW_b_ycd49Efi91ZTaokVDwEzdJaAhM7bZug8_DMUBHXLo0w5wHKcAIf15Cv3DaLb5zoa8UbYSAaWr4j-1Y7LohzgIVhPLJAZUiOoqn3Ig7v--mNz5JIyCBgagApYVFjlRpQGVy2y3Bs8Q9pzDe0jlGJyzKVEvh7aKXuq2XhZST3YaonurBqDIPwYckjhTcywctNgstij4olnHKqllvH_aNV2d5IaFFd60adF3OKZou10pdAts6pNT_7O6-nnC7qOZdiZGhcWJexgBNVvhVROGKiF-CBhA66mCHEue6JXlJXeyrR348wUcSlZjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست ترامپ : چین عاشقِ ترامپه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/alonews/122035" target="_blank">📅 16:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122034">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: گشایش ممکن است نزدیک باشد
🔴
فضا به‌طور موقت مثبت ارزیابی می‌شود.
🔴
در این فاصله، توپ در زمین آمریکاست که یا مثبت بودنِ فضا را تکمیل کند یا نکند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/alonews/122034" target="_blank">📅 16:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122033">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ادعای منابع دیپلماتیک به العربیه: ایران
۲
پیشنهاد به میانجی پاکستانی ارائه کرده است
ایران خواستار بحث درباره پرونده تحریم‌ها و دارایی‌های مسدودشده پیش از امضای هرگونه توافق شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/122033" target="_blank">📅 16:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122032">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ما به توافق خیلی دور و خیلی نزدیک هستیم
🔴
هدف از سفر فرمانده ارتش پاکستان تبادل پیام‌ها میان‌ ایران و آمریکا بود.
🔴
طی روزهای گذشته پیرامون مسائلی که اختلاف نظر وجود داشت بحث شد.
🔴
با مواضع متناقض آمریکا نمی‌توانیم‌ بگوییم که این روند تغییر می‌کند. دیدگاه‌ها نزدیک شده است اما نه به معنای توافق بلکه بتوانیم به یک راه‌حل برسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/alonews/122032" target="_blank">📅 16:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122031">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5bA0V6zQbw7eBII3gG5mS0Hoquuu-L5Z9M8WWnNourOnSGQR09JtzIY80v-dWTrWXtA1Fdl28LwnJFU-LW0HiwX1e1OvSByT0PlAXYD2K8YZjw6P3qDqNmEe6nlgRisJJ4ZKQLT2WlfeuvENMGKt_V12PzBxbcCSFH57az9CgMc_d9o7x0xlTJDFCgBHBP0uBra_R9VgJF8XrzlO3YgX4fYr5dsbdhD0IrQELTvRYC-kjwXSk07f4lhNKQ43wiF3UC6_H-LGh68fNhmgPN5f7eDc1Sq39dFv_XXwyt04VNV7ahHz4HTrcirrma6NOKCir-0xcZig387B9UgVFPw_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام : تا الان، مسیر ۱۰۰ کشتی تجاری عوض کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/alonews/122031" target="_blank">📅 16:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122030">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
علی هاشم خبرنگار الجزیره: لحظه بحران در راه است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/122030" target="_blank">📅 16:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122029">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nv4W2D90ATR8PlWe0I09mj3rQW0Bklzj-lUcuQObd3kXhkIkeiLn5ybR2kHG9kYdnphNo0J3Mo1B0TO3c1anDLXLEq4qnOdjOob9NiMVPcf2v2viHUzs1RGJUcug1UVlhHdnHU6nfL3Cgh_npN7UlayVDL65Ci2SV-fjU-413WJdKZ_RW3ZtyJboiuG7i_Jf6iN-olM5h4kp3zhCYDvFgIOiHIV7W-Aa6iCPElCvATa4I5vLcZPw8FsMhQDmIv6ZR0yKnLHds8TRQMphu3T2emQbrZm17UpAJYRx2UEHdc7aZuGsXEeZh6o79WY9bCUgP1unDjuQ54JPRTLRneAiwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیوید کیز، سخنگو و مشاور رسانه‌ای سابق نتانیاهو : ۲۴ ساعت آینده تو ایران کاملاً حیاتیه یا هم شاید اصلاً نباشه، راستش خودم هم دقیق نمی‌دونم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/122029" target="_blank">📅 16:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122028">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ارتش: آماده مقابله قاطع و همه‌جانبه با هرگونه تعدی دشمنان هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/alonews/122028" target="_blank">📅 16:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122027">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ناو «جورج واشنگتن» امروز از پایگاه یوکوسوکا خارج شد
🔴
تا برای تمرین‌های پروازی و عملیات آموزشی (CQ) به دریا بره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/122027" target="_blank">📅 16:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122026">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjl2rr54ULMP8qiKC-KdUy1IWsbXaQrhlolCyKv4pcqS7tdbvKQvX4MqBRcMEvC_bQ12DzgzrkSOlcrXiingF297EpYPFbcB1tCrwCt_j22VBXRtTl0ebT2_A5ghDUipGb1CPaMJhxcLbx08eVTu5INMijQyrU_-nBJW6Hbi3M2c2YnuK9fa6O6c0TMRCznflztnaehqnbP6ZsP4U8kZV4susL5L4TnAiMEuO7m0aY-r9eLn4GZfBzgzo5NWMmBZauCqTIy0tt83YZkCqTSWxk56bh1k2nyC7Ffd2yNorhKLUdIhkuB-lZodmIhGYj-o4BFtpCIUH71bxGhX_yS8jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیام‌های متناقض از سوی ایالات متحده باعث شد آنچه یک کابل دیپلماتیک آمریکا آن را «شوک سیاسی و روانی بزرگ» در لهستان توصیف کرد، پس از لغو استقرار برنامه‌ریزی شده حدود ۴۰۰۰ سرباز آمریکایی در این کشور توسط پنتاگون، رخ دهد، طبق گزارش POLITICO.
🔴
اگرچه رئیس‌جمهور ترامپ بعداً این تصمیم را معکوس کرد و برنامه‌هایی برای اعزام ۵۰۰۰ سرباز به لهستان اعلام نمود، این حادثه باعث ایجاد احساسات «ناامیدی»، «سرگشتگی» و «هشدار واقعی» در میان مقامات لهستانی شد که لغو این برنامه را نقض اعتماد می‌دانستند.
🔴
کابل دیپلماتیک، که توسط سفیر آمریکا تام رز امضا شده بود، هشدار داد که این حادثه ممکن است باعث افزایش احساسات ضدآمریکایی و تقویت حرکت برای استقلال دفاعی بیشتر اروپا از واشنگتن شود.
🔴
گزارش همچنین اشاره کرد که استقرارهای چرخشی نیروها که پس از تهاجم روسیه به اوکراین در سال ۲۰۲۲ آغاز شده بود، به تدریج در لهستان به عنوان تضمینی نیمه‌دائمی برای امنیت دیده شده است، اگرچه هرگز به طور رسمی به این شکل ارائه نشده بود
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/122026" target="_blank">📅 16:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122025">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزیر امور خارجه فرانسه: «ایتمار بن‌گویر» وزیر امنیت داخلی اسرائیل از امروز از ورود به خاک ما منع شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/122025" target="_blank">📅 16:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122024">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نخست‌وزیر مجارستان، پتر ماجار، قرار است هفته آینده به بروکسل سفر کند تا درباره آزادسازی میلیاردها یورو از وجوه مسدود شده اتحادیه اروپا با کمیسیون اروپا گفتگو کند.
🔴
این مذاکرات بر روی قسط ۱۰.۴ میلیارد یورویی بازیابی پس از همه‌گیری تمرکز خواهد داشت که باید تا ۳۱ اوت رسماً درخواست شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/122024" target="_blank">📅 16:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122023">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
فرمانده ارتش پاکستان تهران را ترک کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/122023" target="_blank">📅 16:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122022">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwCsSUf2Jy-QsjYViUEWWh12j9zhU6bo-4w3fvxOrEjyEoOZWJyQ2poUNqFuCJvxbPXuEqEsOjOcNY3pQvk5VqgQQEusAnYF-okBP3idwAWvOGgBvkkjPlpdrimIAAzmXANkBexUXfNdX6iz-w_b5O5pZYLjMeijCzwZ_LwA7Y8ibq3sQRKiCmT-y1FB89fxOBmL05ACJ43qsWSmyKJSvKmlv6DQJmyt1kKjw0j5i3OxXi66BIPHLACtOb8VkfIhuJrmf7DKCgJTjcLRCoqRI6AFxUjYRh2imDYEmem1fvjuyZmaCDUZyyHAD-JF1Cm3as0prkXQNQ3l_Ghm09oYlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارکو روبیو با نخست‌وزیر هند، مودی، دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/122022" target="_blank">📅 16:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122021">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdG9TaiIing9RnJvHNyvoT0_EG6zjY3-7yJ2w3kMNX41STjMT-hcRh4khy8sG4n9Phb18Nejy9PpPaDP6y958ptr7L8yt5-KiaXBZetFENN98tmPx84Ded8qHiTny_T3zihXJZOe7MKPpXoBS3RVaVR7Gl1fJY4Dt9Y82b7OkF6NeP88PvpS8MlfBLT_jAixwRzIp3EDsmcPy1QgMplOD4pBEdghqM1bH7yEGoy5H9e4a3uQ93Y9OYKrI_MkCFv_6R_YKqbDDDiL6XmiIUaY-WKYoZliIFXsQ_Ow5qwDlcFW-xOUHltNrpMw2lO8qGnGXx5IWxKZ2ngNyuyRpJjncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهد که حدود ۲۴۰ کشتی در آب‌های خلیج فارس و در پشت مرزی که ایران آن را به‌عنوان منطقهٔ تحت کنترل خود در آب‌های خلیج فارس تعیین کرده است، جمع شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/122021" target="_blank">📅 15:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122020">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89737c591a.mp4?token=gmocAY_BP7WgrkOay4ibtepQg6uqy9aOjTFUA3WtttqS7X66NJSCa1e7KiYnVWRo_UVKrSrfAkMnODeTtgTHRUERudjNTxb3VmXe5jtFCfhWMhfRXdvPZgkN2i0o5_MgZVLDnWJnE5HqPL9ykcv0KNYEwbmGBzW5kMbzlGcwgsxmT1JDoejPHB4HeV8rV_DaxAjJuRsoyFDuyfZjWwiL9dNVeC74Vz8y09rPxKtm1U7-wP_zdZeAveBuoc4mr6K5qFtC9cgIjQx2zUc7ls-Aj3LZBN7f9S68ihW8MxbUsuuGIMBHRYTZBClxTEFBYdENPhzWHdFFvlgfKKMsuE-eWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89737c591a.mp4?token=gmocAY_BP7WgrkOay4ibtepQg6uqy9aOjTFUA3WtttqS7X66NJSCa1e7KiYnVWRo_UVKrSrfAkMnODeTtgTHRUERudjNTxb3VmXe5jtFCfhWMhfRXdvPZgkN2i0o5_MgZVLDnWJnE5HqPL9ykcv0KNYEwbmGBzW5kMbzlGcwgsxmT1JDoejPHB4HeV8rV_DaxAjJuRsoyFDuyfZjWwiL9dNVeC74Vz8y09rPxKtm1U7-wP_zdZeAveBuoc4mr6K5qFtC9cgIjQx2zUc7ls-Aj3LZBN7f9S68ihW8MxbUsuuGIMBHRYTZBClxTEFBYdENPhzWHdFFvlgfKKMsuE-eWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاپ لئو چهاردهم به طور غیررسمی در حالی که به مردم محلی در میدان کالپاری در آچرا، جنوب ایتالیا سلام می‌کند، حرکت ۶-۷ را انجام می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/122020" target="_blank">📅 15:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122019">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ffh2tFJZothOVZjjWXSUAsSJ_8NSDcdGURgImG0bOGq2mDECH1pcq1CnwFsCL8pVc10dCa3_daLTHIV9voQVDeQdn2Rs3XAwOBxCWAKBZijxTRWZKwBC09GL3SiISGio_eiTyH4EKm2AxRUVsx4utv3PANyHgGaPkyz8HgC9C98-WP88SVY2Zpr6Z4p2enktu4T8VimwJk3qNth8EiFNTkOnk1oCNZnYcg9MXvKmu8de7JhlV4qIb2wBiB15zufJAA3jYpunbMPrSgorZ2huraeIwF0NBR4P0GmJybgqLLaPgkuJGxOC7SRkBvqDOvL5-JImgepIzmLuYc9Td6rKDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده ارتش پاکستان تهران را ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/122019" target="_blank">📅 15:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122018">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
خبرگزاری فارس: همچنان نمی‌توان گفت که توافق به این زودی در دسترس است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/122018" target="_blank">📅 15:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122017">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
عبدالملکی، وزیر پیشین تعاون، کار و رفاه اجتماعی :  کسی با قطعی اینترنت بیکار نشده..!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/122017" target="_blank">📅 15:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122016">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd18078aa9.mp4?token=aO4c2S4VraN0jMaxvRR8FCElAUz0V_4cLe5rDgu9aWBgISO3lWPEcnaXaNVYSl6I7b8Ol-9oZGd_mUJxTjaiOEUW414BK4iehEywJ7WX8ThiMDu52oLMOJtlYmB8rCoBhL1yhOm7zu0G9CpbyEHpwuwmqv_4Cu5e0WHbMOR2NETaebdwsRW_97PYx5wccUTzh_KycxoZtoQVrq3UibH5Oug5j9UIing26khNun05i_lJy-Gz4flYh4IcGSms09wn3CX02eaC-sMF5JAJ0duri88fZMoDXB454NQao7jYKG5mnjMFjd0Z7KXoyCrWgyaOlM8QuC1UXEDePCYBjY5Wqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd18078aa9.mp4?token=aO4c2S4VraN0jMaxvRR8FCElAUz0V_4cLe5rDgu9aWBgISO3lWPEcnaXaNVYSl6I7b8Ol-9oZGd_mUJxTjaiOEUW414BK4iehEywJ7WX8ThiMDu52oLMOJtlYmB8rCoBhL1yhOm7zu0G9CpbyEHpwuwmqv_4Cu5e0WHbMOR2NETaebdwsRW_97PYx5wccUTzh_KycxoZtoQVrq3UibH5Oug5j9UIing26khNun05i_lJy-Gz4flYh4IcGSms09wn3CX02eaC-sMF5JAJ0duri88fZMoDXB454NQao7jYKG5mnjMFjd0Z7KXoyCrWgyaOlM8QuC1UXEDePCYBjY5Wqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراینی بامداد امروز به کارخانه متافراکس کمیکالز در منطقه پرم کرای روسیه حمله کردند، که حدود ۱۷۰۰ کیلومتر از مرز اوکراین فاصله دارد.
🔴
این کارخانه که مواد مورد استفاده در هوانوردی، پهپادها، موتورهای موشک و مواد منفجره تولید می‌کند، عملیات تولید را متوقف کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/122016" target="_blank">📅 15:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122015">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
مصر و قطر در مورد مذاکرات آمریکا و ایران و ادامه روند مذاکره جدی گفت وگو کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/122015" target="_blank">📅 15:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122014">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/929e0fed3c.mp4?token=Ay0yyxGbiIpG-HPgzl9B8OXkfF_4tWQBW4ydAUSdwj9g8NrQtOQG7ej9E5EoSsTRIPjdrPS7aQ2-IfE-9OjSnTMccoxO96NG-cw73k9N3cScKadhY8VEs90dciqNu-vPvQG6met9oOZTSwOu60zj8B_VX49i7rQ3WfojT08Lou4gKGWv_S_AeWUJfL3rMPfjEYoXF0kRnqkh5wz6XrfvNv9k7j51VxbFELJ9AuVRzcVcXmUdzUJ9UpQOmX8p_G3sZ0eZmZhffx92f6a6HRRhn6megszqrJZME_NucdyCIdd0Vh5_Z3cAeBMMcyFE7MEuKM-ezPKD0GeYCgLfU_bhWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/929e0fed3c.mp4?token=Ay0yyxGbiIpG-HPgzl9B8OXkfF_4tWQBW4ydAUSdwj9g8NrQtOQG7ej9E5EoSsTRIPjdrPS7aQ2-IfE-9OjSnTMccoxO96NG-cw73k9N3cScKadhY8VEs90dciqNu-vPvQG6met9oOZTSwOu60zj8B_VX49i7rQ3WfojT08Lou4gKGWv_S_AeWUJfL3rMPfjEYoXF0kRnqkh5wz6XrfvNv9k7j51VxbFELJ9AuVRzcVcXmUdzUJ9UpQOmX8p_G3sZ0eZmZhffx92f6a6HRRhn6megszqrJZME_NucdyCIdd0Vh5_Z3cAeBMMcyFE7MEuKM-ezPKD0GeYCgLfU_bhWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه کاربر با هوش مصنوعی رفته "جزیرهِ اپستین" و همه رو مثل سگ‌ کتک زده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/122014" target="_blank">📅 15:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122013">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
روزنامه اعتماد: به احتمال بسیار زیاد در این هفته رفع انسداد اینترنت مصوب می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/122013" target="_blank">📅 15:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122012">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
خبرگزاری فرانسه: تایوان می‌گوید چین بیش از 100 کشتی در آب‌های سرزمینی آن مستقر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/122012" target="_blank">📅 15:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122011">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
خبرنگار الجزیره ، علی هاشم در پیامی در شبکه اجتماعی ایکس مدعی شد که یک چهره بسیار برجسته منطقه‌ای، بی‌سروصدا از تهران بازدید کرد تا آنچه را که بسیاری اکنون «شکاف‌های غیرقابل عبور» می‌نامند، پر کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/122011" target="_blank">📅 15:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122010">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
روبیو در گفتگو با نخست وزیر هند: آمریکا اجازه نخواهد داد ایران بازار جهانی انرژی را کنترل کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/122010" target="_blank">📅 15:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122009">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
عاصم منیر: خوشحالم که ایران توسط افراد هوشمند اداره میشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/122009" target="_blank">📅 15:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122008">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
کلاس های آموزشی تحصیلات تکمیلی دانشگاه علامه حضوری شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/122008" target="_blank">📅 15:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122007">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزارت خارجه قطر: امیر قطر با رئیس‌جمهور ترامپ تماس تلفنی برقرار کرد و طی آن آخرین تحولات منطقه را بررسی کردند.
🔴
تماس تلفنی بین امیر قطر و رئیس جمهور ترامپ به تلاش‌ها برای تحکیم آرامش و کاهش تنش در منطقه پرداخت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/122007" target="_blank">📅 14:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122006">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
قالیباف: در صورت حماقت ترامپ پاسخ ما کوبنده‌تر خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/122006" target="_blank">📅 14:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122005">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
دراپ‌ سایت به نقل از مقام ایرانی: ایران پیشنهاد جدیدی برای پایان جنگ ارائه و مذاکرات را به دو مسیر تقسیم کرده
🔴
در مسیر اول، ابتدا جنگ پایان می‌یابد و با آزادسازی منابع و لغو محاصره بنادر، تنگه موقتاً باز می‌شود تا «نظام حاکمیتی» جدید نهایی شود
🔴
در مسیر دوم ایران متعهد می‌شود که به سلاح هسته‌ای دست پیدا نکند و اورانیوم بالای ۲۰٪ را تحت نظارت رقیق کند
🔴
این طرح توسط همه طرف‌های میانجی و بازیگران منطقه‌ای، مورد توافق قرار گرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/122005" target="_blank">📅 14:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122004">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
قالیباف در دیدار با عاصم منیر: ایران همانطور که با شجاعت و اقتدار در میدان نبرد از کیان ایران دفاع کرد
در عرصه
دیپلماسی نیز با هوشمندی و قدرت برای احقاق حقوق حقه ایران و تامین منافع ملی کشور کوشش خواهد کرد
🔴
نظامی‌ها بیش از دیگران و بهتر از همه ارزش صلح را می‌دانند، اما همان نظامیان هیچگاه اجازه نمی‌دهند، عزت و حقوق کشورشان لگدمال شود.
🔴
ما در حال مذاکره بودیم که آمریکا جنگ براه انداخت و حالا می گوید برای پایانش مذاکره کنیم.
🔴
در آتش بسی بودیم که شما واسطه اش بودید و آمریکا با نقص عهد، محاصره دریایی کرد و حالا بدنبال برداشتن آن است!
🔴
نیروهای مسلح ما در دوران آتش بس به نحوی خود را بازسازی کرده اند که در صورت حماقت ترامپ و آغاز مجدد جنگ، حتما برای آمریکا کوبنده تر و تلخ تر از روز اول جنگ خواهند بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/122004" target="_blank">📅 14:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122003">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار کنترل‌شده در شرق اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/122003" target="_blank">📅 14:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122002">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
صداوسیما: دیدار وزیر امور خارجه با عاصم منیر آغاز شده است، طرفین در تلاش هستند تا نگاه ها را به یکدیگر نزدیک کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/122002" target="_blank">📅 14:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122001">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
قالیباف در دیدار فرمانده ارتش پاکستان: از حقوق ملت و کشورمان عدول نمی‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/122001" target="_blank">📅 14:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122000">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
امتحانات دانش‌آموزان کهگیلویه و بویراحمدی غیرحضوری شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/122000" target="_blank">📅 14:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121999">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnPnTElHgwK3m7jcRGpEuP_w3h5EpgNxE03yVcIqPHAaV5fY5xgPhUI8z8Caurli-KBzIyoLGAeuOXwMMQHAY6FFIf5LjOoxhU48CtsyTQfpdwOgn-eZkGOcECOvfNBKUZiEDdu8x0K5ZTH-WddAK7H7H9gOa45lIlrHQP2yyDorh01O0YeCWJtSuzPKFkI9U6YsUmOflmV4JEh6AUiP8Gu9YMHYvgvy8RCQy5x3TalMxrcwo_gCO4Q8WGy2QvJ4QMYfNczGmeIQtNzCo8lt7JtdIw5xh9XHC8dbAgfCYjRg3ALGcyAKrOkPECZ4lrIoIOQNXrC34V48eGCzfXtGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏روزنامه نیویورک تایمز به نقل از دو مقام نظامی اسرائیلی
:
تل‌آویو در جریان گفت‌وگوهای اخیر میان واشنگتن و تهران عمدتا از مسیرهای غیرمستقیم از روند تحولات مطلع می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/121999" target="_blank">📅 14:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121998">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
قطر: بستن تنگه هرمز تنها منجر به عمیق‌تر شدن بحران می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121998" target="_blank">📅 14:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121997">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_G5A3dpa2IeHd0ulWPqA6Ec2xZmgeQWmugp3Mle_PyYb6ZsMBdT7yYxYK7iieyoV0cd3ofB3g_rtXbSx1cvhws5OufL6QpM8hRswRMbn4B63Aa6T1U49ZTnbkD1z6uWLW5NmbskyfcMw3WULkGNST0M8GoESQiOnizuF_8ey0MCy2YLxM0DJnLUj6E3GkJoqwQl32oZOHTOmH1lk4mxSZdzQPi3KQ0au6XOs4gn4yMoW14o9m7Ab8RsRM0XVJ5vo1qLo09RZr3VUVQ5vS91yC8qC75mjJNkU99Q24BpfcBrrGBL8wB843USx3Wfddx2MnGmGFplYnDV2UnV6HgSHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع الحدث : آمریکا به تهران پیام داده اگه توافقو رد کنه، عواقب بدی در انتظارشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121997" target="_blank">📅 14:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121996">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سازمان ملل خواستار توقف اخراج افغان‌ها از کشورهای میزبان آنها شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/121996" target="_blank">📅 14:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121995">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
دیدار مجدد عاصم منیر با عراقچی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121995" target="_blank">📅 14:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121994">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeklJiDkD0uvc9ibc7z3egSjbArg3ETDwGBVytaDBm2BpN-Pl2HWOqM2p_jfwCv9V6G6I0DLLkptIqpeW940JZ21lf8khduYiOlJ4fUKBx_pWFW1jJcKVbE4f7Ruzwul74-Z4EzcCfSN2mYWa790kwwSkspbVhqAjbIm6ZR2i2o-_XKQbpfZ20xfp5Xhym48XKxFN7Uj-YfSaLkfTp6qzM80nZwC0HrmZNsh4kgxFKlbPrm5pHaTKPkpOVtUiZq4LSPPdx2WxUmRGAtum_mnreno457jo3HJh3HIZki7G2XhTYi6pH7u70E4buljD5tIIJ58weyChDwsUYbDdpXEzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عاصم منیر، فرمانده ارتش پاکستان با پزشکیان دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/121994" target="_blank">📅 13:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121993">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
عاصم منیر، فرمانده ارتش پاکستان با  قالیباف، رئیس مجلس دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/121993" target="_blank">📅 13:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121992">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
منابع خبری از حمله هوایی اسرائیل به شهرک «مجدل سلم» در شهرستان «بنت جبیل» در جنوب لبنان خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/121992" target="_blank">📅 13:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121991">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: وساطت‌ها بین تهران و واشنگتن به مرحله‌ای رسیده که یکی از سران منطقه‌ای به طور مستقیم برای پر کردن شکاف‌ها وارد عمل شده.
🔴
ظهور قطر در این لحظه حساس به طور مستقیم و بر اساس اطلاعات و منابع موجود، نه صرفاً به عنوان نقش کمکی برای پاکستان، بلکه به عنوان نقش محوری است.
🔴
منبعی می‌گوید که احتمال دارد یکی از میانجی‌ها به واشنگتن سفر کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/121991" target="_blank">📅 13:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121990">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
فروش متری خانه در تهران آغاز شد
🔴
مدیرعامل سازمان سرمایه‌گذاری شهر تهران: عرضهٔ آزمایشی خانه‌ریز در تهران آغاز شده و از این ماه کار به‌صورت گسترده از طریق سامانۀ شهرزاد شروع می‌شود.
🔴
قیمت خانه‌ریز معادل میانگین کل آن ملک است و افراد می‌توانند از چند متر تا کل واحد را خریداری کنند.
🔴
قیمت‌گذاری برای این املاک توسط کارشناس رسمی و در روز تحویل ملک انجام شده و به مزایده گذاشته می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121990" target="_blank">📅 13:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121989">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚀
فروش کانفیگ استارلینک و VIP با سرعت بالا و اتصال پایدار
💎
پلن‌های VIP
📍
1 گیگ — 200 هزار تومان
📍
3 گیگ — 600 هزار تومان
⭐️
پلن‌های Starlink
🔸
5 گیگ — 1.500 میلیون تومان
🔸
10 گیگ — 2.900 میلیون تومان
✅️
آی‌پی ثابت
✅️
پشتیبانی ۲۴ ساعته
✅️
کیفیت تضمینی…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121989" target="_blank">📅 13:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121988">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRYTqffSa01I7n11ZZRvyncuLTYO3-LlK6pwFaas9pdkaot4jZBzYv_0bf5QAXGxoKYF2rKWnStdXXQQARqwhiPk6Bxre-K5_1uL6rlgbGgyouw_hm6anOiivts1t4OTZRvstWGQ-ij25tjkJyMWiAiA7dA-Vyn00MOdN61yGE-ujl2NDVylPFZiqRtgCx7U51G_tZHXFigS7g6uYnpiflZYaHGlsHBgJZ48AZ7PANBhFa14-sgpctgvAwhWfaLGbzGlcxRSMvSWg58U7LO8ZmAPwFoUrmUuHFEo4XEYIiHOClnmsDO_9ft0ByMeYRa1fVhaHtigbetxBzucO8xS5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
فروش کانفیگ استارلینک و VIP با سرعت بالا و اتصال پایدار
💎
پلن‌های VIP
📍
1 گیگ — 200 هزار تومان
📍
3 گیگ — 600 هزار تومان
⭐️
پلن‌های Starlink
🔸
5 گیگ — 1.500 میلیون تومان
🔸
10 گیگ — 2.900 میلیون تومان
✅️
آی‌پی ثابت
✅️
پشتیبانی ۲۴ ساعته
✅️
کیفیت تضمینی
✅️
دارای ساب باقیمانده لحظه ای
✅️
متصل در تمامی دستگاه ها و اپراتور ها
🛫
خرید و پشتیبانی:
🏠
@expressuport
🤖
ربات خرید:
💻
@vpn_express_sup_bot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121988" target="_blank">📅 13:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121987">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ادعای العربیه: یک هیئت فنی و حقوقی پاکستانی عازم تهران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/121987" target="_blank">📅 13:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121986">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ادعای الحدث: پیام‌های آمریکا که به تهران منتقل شده، حاکی از آن است که اگر ایران با توافق موافقت کند، حل باقی مسائل به زمان بعد موکول خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121986" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121985">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
وزارت بهداشت: مورد مثبتی از ویروس‌های جدید در ایران گزارش نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121985" target="_blank">📅 13:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121984">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
خنثی‌سازی مهمات اسرائیلی ـ آمریکایی در خرم‌آباد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/121984" target="_blank">📅 13:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121983">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n_tUJcjxwSyGwZzh1AON910gdylGbbj7jYqJJ6fkZkx7Kt5AwEHmARteDy6ixfatYG2cfeOuJLeJt3dVG4Vrqf-RycFVB8w5HnUVqMS6LohHs3JXGrGCXE6ooURgDIoEuAh6KXgKkBJP8Y_fcOsCIjbj-u3nDLRGBZ2E7x9UW7TMfXA7VHFevKO_mu19D_ax7y0vTciSJCRjFY4jUKnIrXnLsRbTxfmoplHJNSqCM9hegZ0dAbahzhB4IUxnY9-5xS4U5aO8R193R0-3NddSBhrosgQbb1296PRaHswdC5PbNb8ecW8X6gPOOxJhkzYbc4ZCVKvf7PIPWBii7ZQuFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ترامپ با دموکرات‌ها در تروث سوشال
اگر ایران تسلیم شود و بپذیرد که نیروی دریایی‌اش رفته و در قعر دریا آرمیده است و نیروی هوایی‌اش دیگر با ما نیست و اگر تمام ارتشش از تهران خارج شود و سلاح‌هایش را زمین بگذارد و دست‌هایش را بالا بگیرد و هر کدام فریاد بزند «تسلیم می‌شویم» در حالی که پرچم سفید نماینده‌اش را تکان می‌دهد، و اگر تمام رهبران باقی‌مانده‌اش تمام «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده باشکوه بپذیرند،
نیویورک تایمزِ شکست‌خورده، چاینا استریت ژورنال (کنایه از وال استریت ژورنال)، سی‌ان‌انِ فاسد و تمام اعضای دیگر رسانه‌های خبریِ جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است.
دموکرات‌ها و رسانه‌هایشان کاملاً راه خود را گم کرده‌اند. آنها کاملاً دیوانه شده‌اند!!!
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121983" target="_blank">📅 13:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121982">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
الحدث به نقل از منبع ایرانی: آنچه تهران می‌خواهد، توافق بر سر چارچوب است که مشخص کند جنگ چگونه پایان خواهد یافت.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121982" target="_blank">📅 13:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121981">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
الحدث به نقل از منبع ایرانی: آنچه تهران می‌خواهد، توافق بر سر چارچوب است که مشخص کند جنگ چگونه پایان خواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121981" target="_blank">📅 13:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121980">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df35f5dfa.mp4?token=N5GoB83MpXb7tAGWIKIVyG2pNvR6Hg7mwUASH3VKmFG-pazz8GSYxEUFWRZnzjbVyU7wTVZZdkvyo9MPRdy4_--yXXowPdXNJ81-al26PnPMJs6JZeBoAvvi4xqX5MzGgpHz4iHu2h2a9KTY-CrU13cwNa6GXJBKidUCjKSXuxptviuqB3cTfi-522vKv8G0Ukf-AZrXak7BxjBuZZdYIe9RCmV6rpQI3hQNylH4kkQevRoVNU9ZxCYJkk_iS3yFyQZaFmIYiQOZixWYpANtaiPoSC0PWg2OmaEOq0X69qn1Hk9vULaPB5mJw9Or9xXS7Ib9AbaQzfDDqvHzhqpqbIIP7B6NjGml8oLX_i5WX-3VrGtjpA6MA8-pkHGFNpIhnjLJmtkcwYPEqu6TCLIw6AeGBfHaYVSZLG5eHS4peDFC0giQJTOGnDgZ-lW6GWESSr2lTIKvnfPPouwGccNaG8VB2grHrtaiYyz7xzvte5mANRhrRloPjyiHa8tnr0gjh6-DpWPxT_ny_FPMA57IcCOc2vVXMIf83FU5QZGd3_0ufo7aGVqAq-V_AFq6zaYN9sNigtHscMPqkpcIet--A5chgqDPLTnETtCe-HPevLSbALcAw4h4sj83xN0hq3NRzK2HiXMxHXm21ExPX6RR-KfsyVW5Y_Wsj0tNnZ6Rrs0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df35f5dfa.mp4?token=N5GoB83MpXb7tAGWIKIVyG2pNvR6Hg7mwUASH3VKmFG-pazz8GSYxEUFWRZnzjbVyU7wTVZZdkvyo9MPRdy4_--yXXowPdXNJ81-al26PnPMJs6JZeBoAvvi4xqX5MzGgpHz4iHu2h2a9KTY-CrU13cwNa6GXJBKidUCjKSXuxptviuqB3cTfi-522vKv8G0Ukf-AZrXak7BxjBuZZdYIe9RCmV6rpQI3hQNylH4kkQevRoVNU9ZxCYJkk_iS3yFyQZaFmIYiQOZixWYpANtaiPoSC0PWg2OmaEOq0X69qn1Hk9vULaPB5mJw9Or9xXS7Ib9AbaQzfDDqvHzhqpqbIIP7B6NjGml8oLX_i5WX-3VrGtjpA6MA8-pkHGFNpIhnjLJmtkcwYPEqu6TCLIw6AeGBfHaYVSZLG5eHS4peDFC0giQJTOGnDgZ-lW6GWESSr2lTIKvnfPPouwGccNaG8VB2grHrtaiYyz7xzvte5mANRhrRloPjyiHa8tnr0gjh6-DpWPxT_ny_FPMA57IcCOc2vVXMIf83FU5QZGd3_0ufo7aGVqAq-V_AFq6zaYN9sNigtHscMPqkpcIet--A5chgqDPLTnETtCe-HPevLSbALcAw4h4sj83xN0hq3NRzK2HiXMxHXm21ExPX6RR-KfsyVW5Y_Wsj0tNnZ6Rrs0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رضا تقی‌پور، نماینده مجلس:
شبکه حیاتی کابل‌های فیبر نوری جهان از تنگه هرمز و باب‌المندب عبور می‌کند و ایران می‌تواند این کابل‌ها را قطع کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/121980" target="_blank">📅 12:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121979">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
شهباز شریف نخست وزیر پاکستان امروز شنبه وارد شهر هانگ‌جو واقع در شرق چین شد و دیدار رسمی چهار روزه خود از چین را آغاز کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/121979" target="_blank">📅 12:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121978">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9l53y5PPVRF7RJn5EsEUYNSim5xBV6sR2PdqrIGB09_aoaoGKeL2Sb31IE-G5nZGJA4oAPi5VY9_aXwKIBi6e-p_KMk9pEa2gp-cGapyQrwaobgXv9PwU5ED_REYylSwq55N3EXwNmDjUOO4Tp9chH9Y2D-5kNNPpTRqSHUDHDDeqzMIiCnOEooda0XDwWWuBR3zStwRKqx4dKNJzG3EqVUzOJKixkv0k0eDHRW65lo-Wb3y7UXQt9c1GMnVphNXFf6uOmgNSqXEqgwmbrMVsDFJYfPDoKOSDDizvtqjk2ctFKsMT_RQtpKt_jkVkNJh_7uzRB-2bwzCjedKesBMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۳.۵۴ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121978" target="_blank">📅 12:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121977">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نیروی دریایی سپاه اعلام کرد در شبانه‌روز گذشته ۲۵ کشتی اعم از نفتکش، کانتینربر و سایر کشتی‌های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121977" target="_blank">📅 12:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121976">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
تایوان : چین بیش از ۱۰۰ کشتی جنگی رو تو آب‌های سرزمینی مستقر کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/121976" target="_blank">📅 12:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121975">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dde66f77e.mp4?token=BjDziGdd54aNsB1etnn-38S0MBzzr_4tl72LUpNR0PMLMsSHyPiN6kfuoU9XmIMPFYpFdeS88r_pqGFOZCU28YFQBHKK2OYbfrMOFFZcwQXHv-vSHcb9Nm2v_Uq3_V96Oqpr4hUbWmPSXuEsQLbJtQxEoaadc4ThjeR1BHEhuV_wUjCqeqOMiTG9yOrkZ3IpsQsP6Bo1c2Im3Op1W5cX40_ZNWO0BKzizSUofPXss8g_F-lgUdQrz3QklAzklKfh0wsJNeF0eZ4LYiYEj8vSwC8py4sykFE57WfMEsndpVtlJLUlNWFgJCmlo5k7fCwh3TtdL3LcvaZ1Wn3wIsuZiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dde66f77e.mp4?token=BjDziGdd54aNsB1etnn-38S0MBzzr_4tl72LUpNR0PMLMsSHyPiN6kfuoU9XmIMPFYpFdeS88r_pqGFOZCU28YFQBHKK2OYbfrMOFFZcwQXHv-vSHcb9Nm2v_Uq3_V96Oqpr4hUbWmPSXuEsQLbJtQxEoaadc4ThjeR1BHEhuV_wUjCqeqOMiTG9yOrkZ3IpsQsP6Bo1c2Im3Op1W5cX40_ZNWO0BKzizSUofPXss8g_F-lgUdQrz3QklAzklKfh0wsJNeF0eZ4LYiYEj8vSwC8py4sykFE57WfMEsndpVtlJLUlNWFgJCmlo5k7fCwh3TtdL3LcvaZ1Wn3wIsuZiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش
تند وزیر ارتباطات به مخالفین اتصال مجدد اینترنت: این نگاه قیم معابانه به مردم چیست؟ کی گفته اینترنت را باید خلاصه در دو پیام‌رسان بدانیم؟
🔴
ستار هاشمی وزیر ارتباطات: صحبت هایی که در رابطه با نقد دسترسی مردم به اینترنت آزاد می شود، نگاه قوه عاقله کشور نیست.
🔴
ان‌شالله اینترنت برای آحاد مردم و به صورت عادلانه برقرار می شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/121975" target="_blank">📅 12:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121973">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjpJGxu5W2HDQOiDx9O5qrhQRRtlGmM-18fEZZN6mwekMlDG3ZLurJn87DvW_dpAFWBAuEpn-M61oNfvy4nhqFOTKlzjmqCShkyxOis9mDIT7sXV_e_yt0tsJwnjUkG0kl_Oi5VrSdfjX7n9qlEWtD7JLmqDC_71uGOpL_QcbULv_Wpel7T6nYav_PI9Faf9O2-_IIPyUFg0NEer4mHMVJ5BshnGQZTpKf-etNckCo-1ANxVYZDV693f1r8rEZFG5jklysSKj_dAbI_g1_Y6XlRhUbXjSnhPtLu050135c0gUFloIVtQZut7PWtdxY37BHw29frcALiGh-PeMlrrHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efeb4d8934.mp4?token=Jf8Je0e8IZHlubAi1vkkD4QXUK3I8m9wY5AK57GHgRPF22QPhb5sterwS5ylyrXLxO1MaApuyFCTFqSuKXw4POOXy_21OXxAWgjdT2z7TKuA7aaCNf2S_x5Mj69lVhbThpcvkdHomlGENJynyHv2Y85iDzyaXPcgU2lHZC7Du2A6YPkfHVvzDUhiWHV_Zbj1s4i3imovWH9vbzK38-rrVUEFUNXgp6DHDtXbpKeOlVtmQHwGaJoxY5T2d8ftnZNttmYu4gbh_6dmPVhm0dRvMf3UuQsSNbVI8WbmUoroayAoB1MppoiKLfwKJoCZ1I8LNE5uxYGxPF61Q4zCKV_Ehw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efeb4d8934.mp4?token=Jf8Je0e8IZHlubAi1vkkD4QXUK3I8m9wY5AK57GHgRPF22QPhb5sterwS5ylyrXLxO1MaApuyFCTFqSuKXw4POOXy_21OXxAWgjdT2z7TKuA7aaCNf2S_x5Mj69lVhbThpcvkdHomlGENJynyHv2Y85iDzyaXPcgU2lHZC7Du2A6YPkfHVvzDUhiWHV_Zbj1s4i3imovWH9vbzK38-rrVUEFUNXgp6DHDtXbpKeOlVtmQHwGaJoxY5T2d8ftnZNttmYu4gbh_6dmPVhm0dRvMf3UuQsSNbVI8WbmUoroayAoB1MppoiKLfwKJoCZ1I8LNE5uxYGxPF61Q4zCKV_Ehw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز جنوب لبنانِ تحت حمله‌ شدید اسرائیل بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/121973" target="_blank">📅 12:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121972">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
بلومبرگ: هند برای سومین بار در هشت روز، قیمت گازوئیل و بنزین را افزایش داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/121972" target="_blank">📅 12:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121971">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
بلومبرگ: وقتی کانال سوئز در سال ۱۹۶۷، پس از آغاز جنگ میان مصر و اسرائیل، بسته شد، ۱۵ کشتی در داخل این آبراه گرفتار شدند. آن‌ها لنگر انداختند تا منتظر پایان درگیری‌ها بمانند. جنگ خیلی زود تمام شد. نام آن، به‌درستی، «جنگ شش‌روزه» بود؛ اما کانال به مدت هشت سال بسته ماند. زمانی که سرانجام در سال ۱۹۷۵ اجازه خروج به کشتی‌ها داده شد، فقط دو فروند هنوز قابلیت دریانوردی داشتند. بقیه آن‌قدر زنگ زده بودند که به «ناوگان زرد» معروف شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121971" target="_blank">📅 12:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121970">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
هزینه دریافت گواهینامه رانندگی با ۵۶ درصد افزایش به ۱۵ میلیون تومان رسید
...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/121970" target="_blank">📅 12:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121969">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f5a8b8d1.mp4?token=FoyuOdUe6Bnsc2rBD6E_dt4PoX00URZTw8w0xtBAXmrzXALPrdkPMQ7dDMRrcaUTe3tq6_znG_nCSdbkxkhcD6lhxAJow-Rzx1KR0n0h3QJwPpMvWz0z7AssFYqaqTCF88rVc0-oVDumpjAIxDDSMBlhgWqqms-UJBEZA90jZnXhW_ZteChBi0QWbcq1-E34rRoD7FakAOxBGlF13uo-VtSPpq3STHs4h60sFBLgLHk93-yHwMOIB8XXO0vyudPwbNABdZfhliBoJBK3y-IJ9Nqzf3XVimBBh6HNDPvOPqth-IYRN8ZwcPC1sAJbb0JGsOB0vtbgzYgst8Wo9T-rlbBIjdB-voJVtr62oXBqHQWkJyX_UapqdDQElDBZKvcQqYMbKA4BBk6HWD3-KINImbhSHBCm3LPoOFTpVi3hnqBo4Irj0bUyX_6EI2p2hPKmTz6ZPj4RxFFtXyG3-_VxiVbaCJ1t37IlNYdlmkmHtMhTRfZDXw3JfKzcQZltBMCYIfZ_6KQH2W-g0IAdkCw0xcAblJ4xHYlOXB-VVxga__K0MIYVi-XmmFRYdxGcjr_6Z1rcx6asGbKJtQjXIgIAcxraVy6x4FhC74o_ZL9eR-PODIluQ6ag5l0fbleR6bs2rJd_ppbeLKKmh9rQZf5MMdt9NANjiXI2k4x05qLrIzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f5a8b8d1.mp4?token=FoyuOdUe6Bnsc2rBD6E_dt4PoX00URZTw8w0xtBAXmrzXALPrdkPMQ7dDMRrcaUTe3tq6_znG_nCSdbkxkhcD6lhxAJow-Rzx1KR0n0h3QJwPpMvWz0z7AssFYqaqTCF88rVc0-oVDumpjAIxDDSMBlhgWqqms-UJBEZA90jZnXhW_ZteChBi0QWbcq1-E34rRoD7FakAOxBGlF13uo-VtSPpq3STHs4h60sFBLgLHk93-yHwMOIB8XXO0vyudPwbNABdZfhliBoJBK3y-IJ9Nqzf3XVimBBh6HNDPvOPqth-IYRN8ZwcPC1sAJbb0JGsOB0vtbgzYgst8Wo9T-rlbBIjdB-voJVtr62oXBqHQWkJyX_UapqdDQElDBZKvcQqYMbKA4BBk6HWD3-KINImbhSHBCm3LPoOFTpVi3hnqBo4Irj0bUyX_6EI2p2hPKmTz6ZPj4RxFFtXyG3-_VxiVbaCJ1t37IlNYdlmkmHtMhTRfZDXw3JfKzcQZltBMCYIfZ_6KQH2W-g0IAdkCw0xcAblJ4xHYlOXB-VVxga__K0MIYVi-XmmFRYdxGcjr_6Z1rcx6asGbKJtQjXIgIAcxraVy6x4FhC74o_ZL9eR-PODIluQ6ag5l0fbleR6bs2rJd_ppbeLKKmh9rQZf5MMdt9NANjiXI2k4x05qLrIzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله ویدیو منتشر کرده که توش یه نفربر زرهی نامر اسرائیل رو تو جنوب لبنان با پهپاد FPV زده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121969" target="_blank">📅 12:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121968">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وزیر خارجه قطر در تماس با عراقچی:
ما از تلاش‌ها برای رسیدن به توافقی جامع که بحران را پایان دهد حمایت می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121968" target="_blank">📅 12:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121967">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVUd3xEIuqDe_n8JVeF3x-bhghjJo3LIRvO1aDbyyvHu_OqwNbpXHbfq2chGY_ZadJ7-Dknj3R0fc8NZd0wHOBpsPA5d3aIXW-zMKMOkP0UigdmuuVApzuDWHoSUbx6t3QgkyfH75DOHMwcn1zdNuG_0pcCZLgHhwOF6iCsKOIVVc5G9XqfHQayh9IA0UKBb1M8paWXNRwQ4-7YQ-FYkRyS8n3JyFTcCZddGV2WoLiIWW7H7-iBQoi1662RojRsUm0vh7WuDAJkcz6zHSuFc-IMRmlw1giViOU1xO39L38i-v6bubhmhuQYF-_srfxASxmnE2Ug7rnJ3die1xB9t0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
/
منابع به اسکای نیوز عربی گفتند که میانجی پاکستانی موفق شد بر مانع پرونده هسته‌ای ایران غلبه کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121967" target="_blank">📅 12:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121966">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سخنگوی سازمان هواپیمایی: سازمان هواپیمایی نوتام جدیدی صادر نکرده است.
🔴
نوتامی که اخیرا در فضای مجازی منتشر شده، تکذیب می‌شود.
🔴
شرایط آسمان کشور همچنان مانند روال گذشته است و پروازها طبق برنامه انجام می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121966" target="_blank">📅 12:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121965">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
نیویورک تایمز: ترامپ اسرائیل را آن‌چنان از روند‌ها کنار گذاشته که رهبران این کشور تقریباً به‌طور کامل از مذاکرات آتش‌بس میان ایالات متحده و ایران بی‌اطلاع ماندند
🔴
اسرائیلی‌ها که از دریافت اطلاعات از نزدیک‌ترین متحد خود محروم شده‌اند، مجبور شدند اطلاعات رفت‌وآمدهای دیپلماتیک میان واشنگتن و تهران را از طریق ارتباطاتشان با رهبران و دیپلمات‌های منطقه به دست آورند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/121965" target="_blank">📅 12:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121964">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f2d8f3736.mp4?token=kdWx6ilIgi6T7zBL3i9jeHGTFTyOF9kPamdEAzIBuNRReMSzkqcPuFCIZNwiQGbl4LYTX9KFLk036sMqeIpkg5CVVOsCvmwcrAVtoVLd4lFuxu54H24MqFtEMDn8Lx0odywcsy9p5cEBgDDtUNnm_M9ML5gNRcex78o8CngtpGBV2OQM-8ZLhQ78YIvsSocBEQ4h_eRIlU6Xsx2WhRUhCbze1vOq_m6RhnmHNJMnq0_j95iYViNX3RsewzwTtS-vAAitj4waCc2vR8bJG-22lHvv9q9nTFFJo0D6fIVBS3xHAUFGDZHYzlSULAPoq3_r3eJB4_Vo0KlGbBTYNyEZcA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f2d8f3736.mp4?token=kdWx6ilIgi6T7zBL3i9jeHGTFTyOF9kPamdEAzIBuNRReMSzkqcPuFCIZNwiQGbl4LYTX9KFLk036sMqeIpkg5CVVOsCvmwcrAVtoVLd4lFuxu54H24MqFtEMDn8Lx0odywcsy9p5cEBgDDtUNnm_M9ML5gNRcex78o8CngtpGBV2OQM-8ZLhQ78YIvsSocBEQ4h_eRIlU6Xsx2WhRUhCbze1vOq_m6RhnmHNJMnq0_j95iYViNX3RsewzwTtS-vAAitj4waCc2vR8bJG-22lHvv9q9nTFFJo0D6fIVBS3xHAUFGDZHYzlSULAPoq3_r3eJB4_Vo0KlGbBTYNyEZcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیراندازی عروس جان فدا با کلاشینکف در تجمعات شبانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121964" target="_blank">📅 12:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121963">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49046a9f4e.mp4?token=Rtf6LysbJvUmntmc528xNzWptY1Daxzqb7SnUledcx7KaIyO9IVG2SAmyXhdU0svP_ad-LsBcluaruuDqIXNjJKehdFvxkbn4bDiaUDGWo17VR12xjuV-EQdZgn117UDlO77N-NXQVJ_5a-DBeLpyMgL7HAPcpSGf9j_NQAxgK4_pqjtRrcZs6A06Y_gZeNMkVutz8NDUScFSNJxgVh8lsYSabBKadzTPLtaKGDUcnoyW7ZsvXI2gWnPboNBOE1AxwCHSrAacvIiOOYWWEXtJu_7rP9iY8T9ZandfP6CcGM9u1KamwKPOVDOXrfZnC9eUNwHa_s-hHhVMD8hOfPIuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49046a9f4e.mp4?token=Rtf6LysbJvUmntmc528xNzWptY1Daxzqb7SnUledcx7KaIyO9IVG2SAmyXhdU0svP_ad-LsBcluaruuDqIXNjJKehdFvxkbn4bDiaUDGWo17VR12xjuV-EQdZgn117UDlO77N-NXQVJ_5a-DBeLpyMgL7HAPcpSGf9j_NQAxgK4_pqjtRrcZs6A06Y_gZeNMkVutz8NDUScFSNJxgVh8lsYSabBKadzTPLtaKGDUcnoyW7ZsvXI2gWnPboNBOE1AxwCHSrAacvIiOOYWWEXtJu_7rP9iY8T9ZandfP6CcGM9u1KamwKPOVDOXrfZnC9eUNwHa_s-hHhVMD8hOfPIuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید ترامپ توی توییتر که با هوش مصنوعی یه مجری که مخالفش هستو میندازه توی سطل آشغال :))
🔴
تو ۸ ساعت بیش از ۵۰ میلیون ویو خورده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/121963" target="_blank">📅 12:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121962">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
نیویورک تایمز: تنزل جایگاه نتانیاهو، از حضور در کابین خلبان، به نشستن به عنوان مسافر، می‌تواند پیامدهای مهمی برای اسرائیل و به‌ویژه برای نخست‌وزیر آن داشته باشد؛ کسی که امسال با نبردی دشوار برای انتخاب مجدد روبه‌رو است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/121962" target="_blank">📅 12:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-121961">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b9eqnPbhlZPiTQiodE0jie0SfKbNIo_SHsWG3ejh2FwNfOi4NQ_bu2oPcyCb6uRBPL7C_KwM4qFRNQCHlqn1yz6Xu351jiMUpWbi_8nCBoeIK75j0SPcwp0uArFDc1p4dNrLCq9pfZxt6e5k3sstVzXOY49hxasZcHJHju5d_nD71yO5ckGOwVzNrvoh_mmVl1CqPxXP98eguOng714eLJ--FNTXYrWRDCEopN_RR-cU4wfb3eTj3YkAlMal3k6jMQyUiSEzxpLenuMw2qCEGN6UFmuVZ2XivFVfPhNd5b3w_EyRc2Xj-Mkif4VLzOoY-_nppa1vTQRgPTvheO_6gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: سه ماه پس از جنگی که قرار بود در شش هفته با پیروزی قاطع به پایان برسد، ترامپ در باتلاق ایران گیر کرده است و قادر به یافتن راه خروجی برای حفظ آبرو یا گسترش حملات نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/121961" target="_blank">📅 11:59 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
