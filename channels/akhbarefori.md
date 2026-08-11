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
<img src="https://cdn4.telesco.pe/file/DWOw1fVnu9-oT9hLaH8nzZ9yw8HjzLKd6S9ZDBVuc5cynjVP4qvMj2MRaHeEMwV811ml-4HIRDBYYKwGm8WdrgMyCisOx58zpBYIAMS-vlGiCBJU-iN1p4sERNTFHWS5wQ539VZdGeMkdQftGm8ZpLchFewXzBMxx7eI7aIo_1RUCw9jOCDxKuZkxXB0-KQOsvgi8QwKT5j1KVznupxhii0mMXoZEq9YrwPeXNOCc5X3u6OYGC5KIji2plJ6j89q0OMcgUfzwTHHLx0wg8H62oQUzh3hCLrV5BCfX98CUnXEA9Tn64kPYu53iD7UEac-0J-cgECpCi3xuTqMeOZx9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.21M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 19:21:46</div>
<hr>

<div class="tg-post" id="msg-680350">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
وقوع انفجار در یک پالایشگاه در شمال غرب لیبی
الجزیره:
🔹
این انفجار مهیب در داخل انبارهای پالایشگاه «الزاویه» صورت گرفته است و هنوز علت انفجار مشخص نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/akhbarefori/680350" target="_blank">📅 19:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680349">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4c76a182.mp4?token=G1a7Y9R82T1hSqTXXfIrR17lGS_zX0ckPBrzYGKsrOzH1xNHx5SaeSs8UnGyzwyJkno3Cu-A-KFQte7fAdjdTlE7nDwL-7urr0szNQ_jb6ftA0k1cM08ublc2EXXGYOnN59vVohq__oKl32spyEKw8qGMfHThXEso9qXbGSqnbAHc4BXn4K14_ReoXasI2rg7aCraWal_WJ8iB4IT1viYSxHZVhy2yTzd8zdVRklr3V_lrW3ybDAwyzKOWFa3L0mirWhjtGQ91fSp1p8vtzKwSp-FTUL0bjCsmUGj9vwXiG6Rfa67ceBKRllHeD01DnLn_7F9yRwGrxs6xgCq7Nggg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4c76a182.mp4?token=G1a7Y9R82T1hSqTXXfIrR17lGS_zX0ckPBrzYGKsrOzH1xNHx5SaeSs8UnGyzwyJkno3Cu-A-KFQte7fAdjdTlE7nDwL-7urr0szNQ_jb6ftA0k1cM08ublc2EXXGYOnN59vVohq__oKl32spyEKw8qGMfHThXEso9qXbGSqnbAHc4BXn4K14_ReoXasI2rg7aCraWal_WJ8iB4IT1viYSxHZVhy2yTzd8zdVRklr3V_lrW3ybDAwyzKOWFa3L0mirWhjtGQ91fSp1p8vtzKwSp-FTUL0bjCsmUGj9vwXiG6Rfa67ceBKRllHeD01DnLn_7F9yRwGrxs6xgCq7Nggg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکوردشکنی تاریخی بیرانوند با ۹ مدال طلا
🔹
محمدجواد بیرانوند در مسابقات وزنه‌برداری آسیا و آسیای میانه با کسب ۹ مدال طلا، ضمن شکستن رکورد نوجوانان آسیا، رکورد جهانی دسته ۷۵ کیلوگرم را نیز ارتقا داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/akhbarefori/680349" target="_blank">📅 19:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680348">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
محسن رضایی: شرط بازگشایی تنگه هرمز، پایان جنگ و آزادسازی پول‌های ایران است
🔹
محسن رضایی، دبیر شورای عالی امنیت ملی در دیدار با سفیر چین، ضمن تقدیر از مواضع پکن در شورای امنیت، آمریکا را عامل اصلی ناامنی در منطقه دانست.
🔹
وی تأکید کرد تا زمانی که آمریکا شروط ایران از جمله پایان جنگ (در غزه، لبنان و ایران) و آزادسازی پول‌های مسدود شده را نپذیرد، تنگه هرمز همچنان بسته خواهد ماند.
🔹
او همچنین افزود که توافق احتمالی با عمان برای عبور و مرور، موضوعی جدا از انسداد کلی تنگه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/akhbarefori/680348" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680347">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-NfpXPaJnIA9EmJhdU3kMJQC4It6sBUd4gaw9bUxsKiq-b65wkB7v3hXi72gQ8bjLa7knWWbsw8KF_jJiaTNLr5UDHnMwHcvMoujb3O6StV5Xp4zDnCeRGUXN1D-BUw2aZDsnch5gGOgkBxwHMiusL2S3ZNVdKEa-0iTlIzwB8KTlE6ZuP8AVB08aVyySC3_b3HvTW2gsZ0bAZGwZhUUflpG9MchlIK2Bbae_g1m_0Z6G8tECzhkDuRw4TAYE46GAvmShXwGW0-F5DIwOqCZHt9dCBHKVU8BrZ36L5q3uIBMw-ubPdiBGfSunB8btEz6m9gX-OiIUp7zhu6lgZpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/akhbarefori/680347" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680346">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Erl25SZBltbKvgpqhBfxzoTLqRFL92ZNy0lMOljTfBOcRbgnfGfim8FKiJ95HBlSkCyZb6t90Rgjr1_REi2UwMgIBiWX4VgBjMjtqO--jQ6XBg8S94nRIDcTBjp_LzG1YbGjb52zkv7_FYCzpKcWSdMV1Z4Sr-mGFZs2GEIxAWpcFbUgrG-YdJP0zWOezOdbUop-fQkXetRgRSSs8WDuHYYxAcOU5zbo-pxAWM9YXbkQ7oiSXbXSHWlzePVhyeiql6nKGZjV1CgbpWz_mWp7WaSILHmp7SDwlaSnNxBiqvlqWglTrChpbtpU9o5QKyFK9vYy9aGbgY7gycXd6EN1jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کالا بی‌برگ
🔹
اجرای طرح کالابرگ در برخی فروشگاه‌های بزرگ، به دلیل تأخیر و بدهی دولت به فروشندگان با اختلال مواجه شده است؛ مسئله‌ای که علاوه بر ایجاد نارضایتی در میان فروشندگان، دسترسی مردم به این طرح حمایتی را نیز تحت تأثیر قرار داده است. در شرایط اقتصادی کنونی، استمرار و نظم در اجرای کالابرگ اهمیت ویژه‌ای دارد و هرگونه وقفه می‌تواند اعتماد عمومی و همراهی شبکه توزیع را کاهش دهد.
🔹
هشتصدوسی‌‌وسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/680346" target="_blank">📅 19:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680345">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4nXPTqjr3ZTs8mo9aBGdWFQ1NpVOuGYzH-vajUfp8NKvWxhnMdAb2ge6k-YQ2iYcyhw-ZyMcXoshXWFGX1doke3Jwqn14DNaLMVpEPYDqt5JH74OB8MJtGGMZoCVo4RX5ltxC9I2jnTK9Rnipw92CrKrLD9inXBbCSLD5MvzRNcrcmM6IxuFseBIpFvDOWQVjdxg6K4o_4Tgtd2DFYdKfzVY8R_pKz5XceWaT2gevqgURTDQ9QnW_g_IPSe5hW_7ug6mBosxurzDHxbmGIq6-LZRx6_-346CPRPBTLel9KcKXUVlppxZiHFrW4sQjYfjP-9XOOWjEN5UbCUZAPjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر، مشاور رهبر انقلاب:  تنگه هرمز باز نخواهد شد تا شرایط ایران محقق شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/680345" target="_blank">📅 18:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680344">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
نتانیاهو کودک‌کش: جولان، سرزمین ماست و همیشه متعلق به اسرائیل خواهد بود
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/680344" target="_blank">📅 18:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680343">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeS61uvL6VBTCuyw2InE-oF12oQDZXLw4N8ykdLk-PAt4JbcF96gAQm_c6WJqZpaH56T5lqPrc3JBMO4yxP4wPqEW-eX_3lx6hmyT9rXOCfPqHZB6Wxrsc7qEOAwmH0a84Qb3LabAeIMZTZpqPJqssN-yyUw0tQrd7aD-pY-tH-CuChENUwrXEQbIIdOLRdqul6CqSfXIz66gaqhOshC0M-4HEydaWr1b9W3WexvXjqb4dKzMJV8hAY2lDOhVRJlHuFn0n8PTtzAM56i0J4LP_4HD8GoPTpQo4tuW1cNk8n1Foheon7WYqerJ5hwb--5nG960YbMQJoJ5wl0Omv0Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تامی ویتور، مفسر سیاسی و سخنگوی سابق شورای امنیت ملی آمریکا: تصویری که در ذهن از ترامپ در حال پنهان شدن از ایران داخل یک چرخ‌دستی حمل غذا شکل می‌گیرد، ویرانگر است
🔹
پیرمردی ضعیف و احمق که از پیامدهای تصمیم خودش پنهان شده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/680343" target="_blank">📅 18:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680342">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEiKQnEu3hAd1Upk7UOvmRbGcHDqfZdZLBnMVCTNAlLpIlJp8QBlsbUEbUe4PVn6ZE0TiXpG0ZWAINKqEcu8NEuJeVMEx3f2rDy4Sdeu78hbMP_p1LoFG15a6bkriGbZrRYzjgCtOlakhQkV1d1k0AlFcLM6tUtyVXwuBGbTy9Qu0_JfKu8sYl57CBd3eTJuKHuyI3CgvPLRSot3tLdWaik2hezGJNv-1CNhRij83VbcNOa8USlDNP8kfSIPmOikxCLLMFZNupgdvYqUAUmUCg1JKPOOD_x8ddwYXSqgERKm1BgUU0RmzqUrPe3YyRbiIjrcyOTdxsJsR2WmKtMymw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صندل مردانه نسکافه ای مدل Arman
جنس رویه : کوبا
جنس زیره : PU
کفی پرسی و دوردوزی شده
رنگبندی : نسکافه ای
سایز :41 الی 44
🔴
قیمت 1,358,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/46479/180124/</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/680342" target="_blank">📅 18:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680341">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/122bee6636.mp4?token=r8PhJydjEmwKFn_YltZbrNvbv0RVxjUf_BMQJGqhJBUMVUAYT9BB7H6sCyr3CUUhMyCPuIytQVamJa1I_KFAN0Cn-PxyG9NIJ135-el7oXvQMfJVkkVcixfkYzhj5Q8LliT_bwolCe_TVXLoJb5RLPjRCuBjktYeoKhyGHOAkfrt--G6i0NB4dGa76TtkmoXZmINYWStPWaL13b56VG61KybJ63rKNv3TPU7MyNEyh37eubsd_KbZkgwZc6YyCjeVsDOjC-u_nFuph91eBkKk4regPsApukkV8EPgp3guyqWLjFtfO0mv5Pm0up8rXi4Xxs9W8j7lE_SETQyPtYaNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/122bee6636.mp4?token=r8PhJydjEmwKFn_YltZbrNvbv0RVxjUf_BMQJGqhJBUMVUAYT9BB7H6sCyr3CUUhMyCPuIytQVamJa1I_KFAN0Cn-PxyG9NIJ135-el7oXvQMfJVkkVcixfkYzhj5Q8LliT_bwolCe_TVXLoJb5RLPjRCuBjktYeoKhyGHOAkfrt--G6i0NB4dGa76TtkmoXZmINYWStPWaL13b56VG61KybJ63rKNv3TPU7MyNEyh37eubsd_KbZkgwZc6YyCjeVsDOjC-u_nFuph91eBkKk4regPsApukkV8EPgp3guyqWLjFtfO0mv5Pm0up8rXi4Xxs9W8j7lE_SETQyPtYaNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله موشکی به گروهک تروریستی کومله در اربیل
گروهک تروریستی کومله:
🔹
مقرهایش در درهٔ «آلانه» در اطراف استان اربیل هدف حمله سه موشک قرار گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/680341" target="_blank">📅 18:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680340">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUq-Pib6gmX_f7D8hxa8evDPopUsrnfqXRGzLz4AqHUDR1azTqomkeBwJMKVG6e_yVwEsdAJoWI6pu3luLsr2aX_Hw0JC9M12_GNtgVVEXnMT-bu7MCDPeDIT7EDtzERaRH2qro05rVxxEDJFtsWdlPzVwq1zxOrenvEedcMRMXvI2IH57md6m5HwArnTUPJayPTsgaoYopMv-8Wi0zmf6rjRbWb8Wt9IrzCm0ssgGgnvnmxyC9rnrgluPrZDX4A8EUtDLxJdOgYO4bsH8urUgIcwyvylItb-mbXlar5E5GLCsnmB2vtfgc34V-FWiOC7bxrnWehNlDdfbtwxIvSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه DD Geopolitics: دست از آزمایش نیروهای مسلح یمن بردارید، آن‌ها قبلاً نیروی دریایی ایالات متحده را شکست داده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/680340" target="_blank">📅 18:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680339">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ترامپ کمبود مهمات آمریکا را گردن بایدن انداخت ترامپ شیاد: بایدن با ارسال مهمات به اوکراین، ذخایر آمریکا را کاهش داد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/680339" target="_blank">📅 18:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680337">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBRz_QHzJuepHc-Wd0EVLQkp2fHp9L3y0-QB_8yzn0XvhMpM-SqqJMdnNiiRyQYX8OBJ-Ykt1gtUV0aJuM2JQFxMFFpBNp_qhmoHp0y59qvCnrL3iD0zQXdACPHQOPeqxf_eG1ZkHS8TT_kHJEmppWfAKURzHqV17j8M2Tw8n1sjFvJeV4l-4lxG1ZE6uHWWWnFCihnpPOCWtfgm4V_SMJFu76Vl7lukcZ3HO6oBupcBGrsqS35LjT2XEynEl31MHQvmdPzBVBBXxG1oNUvsUN4rWnOZs42gZbs2MRw193tc1_3SC31HPqJx77MeriVwtZButChqlve-z6iH438MyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرکز تحلیل اجتماعی (متا) در یک نظرسنجی ملی، از ایرانیان درباره قیمت واقعی بنزین ارائه شده توسط دولت، پرسیده است
🔹
طبق نتایج این نظرسنجی،
۴۲٪ از مردم معتقدند دولت بنزین را ارزان‌تر از قیمت تمام شده برای خودش به مردم می‌فروشد
و به نحوی از این طریق
به مردم یارانه می‌دهد.
🔹
همچنین،
۳۴
٪ از مردم بر این باورند ایرانیان
بیشتر از نیازشان
بنزین مصرف می‌کنند.
@metaacenter</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/680337" target="_blank">📅 18:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680336">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
درگیری و شورش در ناو هواپیمابر «آبراهام لینکلن»
🔹
در پی اعتراض خدمه ناو هواپیمابر «آبراهام لینکلن» به وضعیت معیشتی و شرایط دشوار پس از ۳۵۹ روز مأموریت، درگیری شدیدی میان نیروهای این ناو رخ داد. بر اساس این گزارش، در این درگیری با سلاح سرد، ۷ نفر کشته و تعدادی مجروح شده‌اند.
🔹
خدمه ناو به مواردی همچون کمبود شدید مواد غذایی، وضعیت بهداشتی نامناسب و عدم پاسخگویی فرماندهی «سنتکام» معترض بودند. این گزارش همچنین به حادثه مشابهی در ناو «جرالد فورد» در اسفندماه ۱۴۰۴ اشاره می‌کند که منجر به عقب‌نشینی آن ناو برای تعمیرات شده بود./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/680336" target="_blank">📅 18:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680335">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbJ6S8kfjHTRKtfVJguEtc2V4TnAGZL6PiIuNuYWUfOYQQD_sDG3_xGcJySRCBQTcoTK054P7VzjbdiUDVvIbMf2oSncsDPqnGwYFlRLfY6IMyO1IIIEwdE9s02c615ZcY6KQhDtWmUCw-77DKvAm3hKEkNtoTUlsEviNvu__FlNDPbUxN9H0powePb85iyWTwn_0mITGbA0mv3h3r1dpUtFRpYdos7nSL103xasmx0xYFPXWQ3yF11cp8ZuVv-XMka9QdtC5WmTxL5KSoww4wF2CMhKHUCyB58hLMBLoYlSMJQSfP_KjevnkSIVE7XobfCPICDjoMKmpHbvXWWt9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاعری که زبان شعر معاصر ایران را دگرگون کرد؛ احمد شاملو
🔹
احمد شاملو، شاعر، نویسنده، مترجم و پژوهشگر برجسته ایرانی، از مهم‌ترین چهره‌های شعر معاصر فارسی بود. او با زبانی تازه، آزاد و انسانی، شعر را از قالب‌های سنتی دور کرد و آثاری ماندگار درباره عشق، آزادی،…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/680335" target="_blank">📅 18:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680334">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIZcdbRfenGvI9exHMG9D84i0lwFv2ipKxzN6gUIau9Cy2z3VB8MWlYpTgn1bYJenaE-OgF2kfO1xjYJyiI1XlRVZiws63X5ybSwVF75-oZVBr1OO-zyrT77Hf9edDAQJYL9OYzjKeiIjnG5U_Mfik1VP9t_XeoKaqO6n9I7aCfRDHa45pyrRZOIUO0h6kLr2DHD73Z6nw5gdIS-pyeA2-EEAjnceCrmiPLvLQZx7NP1pgQ7saR3ceEQkZnogn-Pz0i0CYU6tJ5QVKGmtCBam5w13qI3VAEDWQYISUz_PhJ2O-JlpqfwgsfH6K9y0VJFKNL3WuwXjHDc1qtC3foy-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرانه مصرف چای در کشورهای مختلف جهان
🔸
بر اساس آمارهای جهانی، سریلانکا با مصرف چشمگیر ۵۰.۱۷ کیلوگرم چای به ازای هر نفر در سال، در صدر جدول کشورهای جهان قرار دارد.
🔸
این در حالی است که بزرگ‌ترین تولیدکنندگان چای دنیا، یعنی چین و هند، به ترتیب با ۱۰.۱۹ و ۴.۲۱ کیلوگرم سرانه مصرف در رتبه‌های بعدی جای گرفته‌اند.
🔸
ایران نیز با سرانه مصرف ۱.۶۹ کیلوگرم برای هر نفر در سال، در رتبه ۳۰ جهان قرار دارد. ایران با تولید سالانه ۸۳ هزار تن چای، هفدهمین تولیدکننده بزرگ چای نیز در جهان محسوب می‌شود.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/680334" target="_blank">📅 17:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680333">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
دیدار وزیر کشور پاکستان با وزیر امور خارجه
🔹
سید محسن نقوی وزیر کشور پاکستان عصر امروز سه شنبه با سید عباس عراقچی وزیر امور خارجه دیدار و گفتگو کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/680333" target="_blank">📅 17:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680332">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVeEoPOO6jxWCMzgxeNe6yMRCUFRmM4Zj-Rs16qI94IDy7E_Q1sy-w_7TGPa9gROJbuCQ4Gwchq4OdV6v97L36ymw4jAV8sO0C5E1ay4PEughlNXcZ0f2Y45aSMgWeiIYyx6fjcQgBJ3QVxAgku70dSbp_UUO2vdLVRn5kkhb-_-7K1O2NYAPnm6Yw1h2CzsfOJMk4jGEeiI0xTnnD5RAdt_a9tDfOH3qItKSre0RQKGUecINT8-prZEZRoqXNkjZBMl1j3SDU_YRMwwq2W1Ehpx9MEijhKaMIZCd69dMqbKuMN5c_LIbGpQSlllrpynAo8CpW6qe1AY-UTfBKiKZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ولایتی، مشاور رهبر انقلاب: عربستان از سیاست‌های آمریکا عبرت بگیرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/680332" target="_blank">📅 17:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680331">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
حمله بالگرد آمریکایی به یک کشتی با پرچم پاناما در تنگه هرمز  روزنامه وال استریت ژورنال:
🔹
نیروهای آمریکایی با استفاده از یک بالگرد به سمت کشتی «ویلا نوا» با پرچم پاناما در تنگه هرمز حمله کردند.
🔹
گزارش شده است که همه ۱۷ نفر از خدمه کشتی سالم هستند.
📲
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/680331" target="_blank">📅 17:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680330">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: شهید لاریجانی می‌گفت این قدر به حضرت آقا ارادت دارم که اگر حتی حس کنم حضرت آقا موضوعی را دوست ندارند انجام نمی‌دهم
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
شهید لاریجانی باهوش بود و به مسائل کشور مسلط بود. آقای لاریجانی مظلومانه شهید شد. در شرایط جنگ باید به طبل اختلاف نزنید و روی اشتراکات متمرکز شویم.
🔹
شاید برخی آقایان به آقای قالیباف نقد و ایراد وارد کنند، در عین حال حتما در خیلی موضوعات با ایشان هم نظر هستند. روی اهدافی که در جهت نابودی دشمن است، متمرکز شویم در غیر این صورت یعنی دشمن را تقویت می‌کنیم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/680330" target="_blank">📅 17:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680329">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMbNW2pGGDx2iU-RUR3VT1LfTdv7Hxzr5w0ztBDiegdZBJ5ulkdA51zNPFzLQ_OWXZKEiSNGMyI8NmjSdfvItbOXQhC8RtCUgg9sjJBx_0ZfoqL1yBs9CILcbxBS-o1hKFNODdb0SWTS2MR5V-_bHKOFtskqSrbPtBpaIC54APwrLqOTo6DJvwi4z6KPS4-4_dYNeLU8rbQNEwvqlYwKqZ4mfr--Pw0Id_vQiSWykcIVuHpe4Q05TCXYjrZep7eH3v9fo0qzfWfxeb8KwOBXNLBNCAi9GW0s894kuA42o7lKKayvwppE9ie-0JUAXUNgwfL4_ToEDMpplXOcV5RXgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
⭐️
جاباما تور رسماً شروع به کار کرد
تازه ترین سرویس جاباما با هدف ارائه تورهای گروهی  و تجربه محور راه اندازی شد.
مزایای ویژه جاباما تور برای مسافران:
🔸
پرداخت اقساطی
: بدون نیاز به تسویه یک‌جا، هزینه‌های سفر خود را در چهار قسط بپردازید.
🔸
تضمین امنیت و کیفیت سفر
: همکاری با مجریان معتبر و دارای مجوز رسمی و همراهی تورلیدرهای مجرب.
🔸
کشف مقاصد خاص و بکر
: سفر به مناطق کمتر شناخته‌شده و شگفت‌انگیزی که تجربه آن‌ها تنها با تورهای تخصصی ممکن است.
🔸
شفافیت کامل قبل از خرید
: بررسی دقیق برنامه‌های سفر، جزئیات خدمات، قیمت‌ها و نظرات مسافران قبلی.
🔸
حمایت از جامعه محلی
: کمک مستقیم به رونق اقتصادی مردم بومی و کسب‌وکارهای محلی.
🏕
اطلاعات بیشتر و مشاهده تورها:
https://jabama.me/koP2PQV
📞
شماره تماس و پشتیبانی رزرو:
۰۲۱۴۹۲۷۵۱۱۱</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/680329" target="_blank">📅 17:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680328">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBKK5DRwa3RTE0R3H1FJNPcnu5-_vL0cxYnOLKfWSZaMeeSc1f-XeK3o7FIz_BP2BjqUxFkoQvrGEXHnDBVuXqXsSoT0snKc_AuH2YoL8HOD795SkcLYQTuZRvD8_7QaVSmbdhasMvpYzl7Gco4hQXO0KLClzXM__pG220ORoCXezHJyFAGihcuhHFFytb3m6QTwaMNrNo7cWMZIg_3rfEnexCN0y6pDowsFW25SfNdR3BNg_SvsMlgql-bS5N7L5j552Msk79lD4p_A7wtfxlf1RLuwkkbH_eJpcWznmY4_AZPymBD3m-xmY8gBxQXpDiIl1W-104CnJE7DWMJ_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازطراحی زیرساخت ارتباطی بزرگ‌ترین فولادساز کشور با فناوری 5G رایتل
🔹
#فولاد_مبارکه
و شرکت خدمات ارتباطی
#رایتل
با امضای تفاهم‌نامه همکاری فیمابین سعید زرندی و مهدی فقیهی مدیران عامل دو شرکت، مسیر تازه‌ای برای توسعه زیرساخت‌های ارتباطی، شتاب‌بخشی به تحول دیجیتال و حرکت به سمت
#صنعت_هوشمند
ترسیم کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/680328" target="_blank">📅 17:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680327">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d17e9789e.mp4?token=YEnnRRN23OsSdSvSEOpiiH_fllsgw2JcF6rfbUFA8gIlxJ2XRmaLIL5VGiE-5qyhZFbhJn7wGRWVkWvDdOxe8gRHp8yJB8ki-bDsqHxq2SOVn1HWi7PNw0HUftTfZkMPYMM5lR-oZxg6SDskLFVg19KqqfZxkZtkDtYy065ZDwpu00pvquXVnkP4qm8RrAdO8r1wAAvwnk2kct6dGjxyMQiCVi1qiZBPGCQIr2ZrbSCG-s8fcvo6LlNuPO9a3RVlcUPAQzMasrD3fm7PLZZRimsCYFVR9AAdUMrBDAeGeRxQbfA3C0JsZhjH6yrJbniB_nmM4xQhCUorlfWOu2MrRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d17e9789e.mp4?token=YEnnRRN23OsSdSvSEOpiiH_fllsgw2JcF6rfbUFA8gIlxJ2XRmaLIL5VGiE-5qyhZFbhJn7wGRWVkWvDdOxe8gRHp8yJB8ki-bDsqHxq2SOVn1HWi7PNw0HUftTfZkMPYMM5lR-oZxg6SDskLFVg19KqqfZxkZtkDtYy065ZDwpu00pvquXVnkP4qm8RrAdO8r1wAAvwnk2kct6dGjxyMQiCVi1qiZBPGCQIr2ZrbSCG-s8fcvo6LlNuPO9a3RVlcUPAQzMasrD3fm7PLZZRimsCYFVR9AAdUMrBDAeGeRxQbfA3C0JsZhjH6yrJbniB_nmM4xQhCUorlfWOu2MrRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز بمب‌افکن راهبردی چین با موشک اتمی
🔹
چین برای نخستین بار تصاویری از بمب‌افکن استراتژیک H-6N را که موشک بالستیک پرتاب‌شونده از هوا JL-1 با قابلیت اتمی را حمل می‌کند، منتشر کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/680327" target="_blank">📅 17:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680326">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13991f0b53.mp4?token=aHoQSXfMHRkSJ6CWlkhyAvcfajhTBMCikvdJZlU8XwBK0a8rhEwunTRucdowcHDixcj-AVH0-AMebRYeWLo22xcKUUK_wY11Fz-i9WgGCQ3mNwKvMPMlGr6wGNsFqXYmEfOxSUfI5sCZL0ISpP81BvYdG0D5Bo54dFI-Xj1pc93OfnfAMh29Pw0768S7SVvzSBfTcXNKm_JUYqoGOc_vVJsW_G2NgLc-lruBnPuV7fo1fODMenu4kydznACCgFk7NDh7R-qDYVFTo2RW-OOVAIKqxOvTStQ0aeJqwig-5xgW4yU6rStrsaz6qgQZLXPvXz9ZtzoeL6x-uYGiU8hNOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13991f0b53.mp4?token=aHoQSXfMHRkSJ6CWlkhyAvcfajhTBMCikvdJZlU8XwBK0a8rhEwunTRucdowcHDixcj-AVH0-AMebRYeWLo22xcKUUK_wY11Fz-i9WgGCQ3mNwKvMPMlGr6wGNsFqXYmEfOxSUfI5sCZL0ISpP81BvYdG0D5Bo54dFI-Xj1pc93OfnfAMh29Pw0768S7SVvzSBfTcXNKm_JUYqoGOc_vVJsW_G2NgLc-lruBnPuV7fo1fODMenu4kydznACCgFk7NDh7R-qDYVFTo2RW-OOVAIKqxOvTStQ0aeJqwig-5xgW4yU6rStrsaz6qgQZLXPvXz9ZtzoeL6x-uYGiU8hNOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صبح امروز |بارش برف قسمت‌هایی از آفریقای جنوبی را سفیدپوش کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/680326" target="_blank">📅 17:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680325">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4ef73cdd3.mp4?token=AeSs7t-VwsFQMG9lVwe-VaC7AcGw11Xit-ZtQB10AmWpszhFz4F9h2OOouXvdPbfha-S0F6soHFxaj9KTfzz5aPUaNqrP0RH8oeHsA7Y6zdEoh5QEx0N4MQN6zbFc6PKH_rsqXNVKbvmUu9ssMlP6TqO-4LJFsojXdOXr8Huz9a3IJ-pp4YDUz5XWrce0gwTgaKjaNpkP89YjFP0uD6cjsHTV_8PMCxK4LqYfq6lu1g4Lz3COAQbRcxQW1hoVWzlXgQ5hO5NWzTWjJrunWhhqXegllrlWf15q3p3FOVUYkVuklBKbbVjLvxWGrfb_saPCBjlKuR0SmQBAqMnMfH8lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4ef73cdd3.mp4?token=AeSs7t-VwsFQMG9lVwe-VaC7AcGw11Xit-ZtQB10AmWpszhFz4F9h2OOouXvdPbfha-S0F6soHFxaj9KTfzz5aPUaNqrP0RH8oeHsA7Y6zdEoh5QEx0N4MQN6zbFc6PKH_rsqXNVKbvmUu9ssMlP6TqO-4LJFsojXdOXr8Huz9a3IJ-pp4YDUz5XWrce0gwTgaKjaNpkP89YjFP0uD6cjsHTV_8PMCxK4LqYfq6lu1g4Lz3COAQbRcxQW1hoVWzlXgQ5hO5NWzTWjJrunWhhqXegllrlWf15q3p3FOVUYkVuklBKbbVjLvxWGrfb_saPCBjlKuR0SmQBAqMnMfH8lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای جوادی حصار: دولت فیلترینگ را برداشته
رییس ستاد پزشکیان و فعال اصلاح طلب:
🔹
فیلترینگ رفع شده و تنها شبکه اینستاگرام فیلتر است!
🔹
من خط سفید ندارم ولی درخواست دارم به من بدهند، نیاز دارم. یک عده در این مملکت پزشکیان را هم سیاه کرده‌اند/ تلویزیون اینترنتی مدار
گفتگوی کامل را اینجا تماشا کنید
👇
https://www.aparat.com/v/inm2imu
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/680325" target="_blank">📅 17:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680324">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ff8b5055e.mp4?token=Duc277iTz2Dct9nW3vKbB_VK3LwLdt6fsvJ7CpmJfZoR0gcQuzGEjh8KgK9lHWepT3vtOelbcj6h_mgVll1kTMRe9zMOzJDpTf7d1cx85p4RRMrXWnT3-1pLW86zJoYjNDFGvHApZ-S1nwN1_xEalfuD-cZJhIfuv0iRjuI3J3PpTPTRjc6v202moVncTpi-hDYff749d_Z6WjJb4iwFqj1t__tC4uNuBgT9xY8DI5F9bWGWRGJlVXhv57qJ8K0KSI9hBarbWrkrel5fCpXDVVfshZkYPi6zSv9J2OWPY70jttfVxkgLOZ7jTdJaJPPlRQaeXsTTV59IG9SjFUsa-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ff8b5055e.mp4?token=Duc277iTz2Dct9nW3vKbB_VK3LwLdt6fsvJ7CpmJfZoR0gcQuzGEjh8KgK9lHWepT3vtOelbcj6h_mgVll1kTMRe9zMOzJDpTf7d1cx85p4RRMrXWnT3-1pLW86zJoYjNDFGvHApZ-S1nwN1_xEalfuD-cZJhIfuv0iRjuI3J3PpTPTRjc6v202moVncTpi-hDYff749d_Z6WjJb4iwFqj1t__tC4uNuBgT9xY8DI5F9bWGWRGJlVXhv57qJ8K0KSI9hBarbWrkrel5fCpXDVVfshZkYPi6zSv9J2OWPY70jttfVxkgLOZ7jTdJaJPPlRQaeXsTTV59IG9SjFUsa-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلزله ۷.۴ ریشتری در غرب کلمبیا تاکنون دست‌کم ۱۳۲ کشته و ۵۷۰ زخمی برجا گذاشته است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/680324" target="_blank">📅 17:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680323">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
حمله بالگرد آمریکایی به یک کشتی با پرچم پاناما در تنگه هرمز
روزنامه وال استریت ژورنال:
🔹
نیروهای آمریکایی با استفاده از یک بالگرد به سمت کشتی «ویلا نوا» با پرچم پاناما در تنگه هرمز حمله کردند.
🔹
گزارش شده است که همه ۱۷ نفر از خدمه کشتی سالم هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/680323" target="_blank">📅 17:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680322">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sD94v1CZ_m0sqBY3MkaosYQRQ0V9K79HGxJM2hnfWkNXPuV_PfR1oNStfr_6BSSKCsr0ndgcOQ-7as2LP0ZACpvKEONtdW7jBzEkg3h1e_rfjkhXHUtmgaLxeVJyzW0zMN4yJxw6zs9GoYVvsI1QO06aUF5vaG4ASeUviC3EGiiaViIKc4Vj3A7MuUU9-JPZwdfpm4YRI57FkQsiNKUA-8OmaKhYzHgnltxmXDd0Ngjv3ECA16gMZ1gS0XxbcIXQnaStC075EKH5MqQNClkMjNE1kTKUmwsFA3fI4gRWUHP1cWkGdzv26qMonN0Jsdap5f6Zcu6Z8JMlhh29QAeexg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران»/۶
🔹
ثبت رکورد جدید در جذب منابع ارزان‌قیمت توسط بانک کشاورزی
🔻
همزمان با افزایش منابع بانک کشاورزی تا مرز هزار همت، سهم سپرده‌های ارزان‌قیمت در ترکیب سپرده‌های مردمی این بانک، با روندی صعودی از ۶۰.۵ درصد در تیر ۱۴۰۰ به ۷۰ درصد در تیر ۱۴۰۵ افزایش یافته که بیانگر ارتقای کیفیت منابع و تقویت ظرفیت تأمین مالی بخش‌های مولد است.
🔻
بهبود ترکیب منابع می‌تواند ظرفیت بانک کشاورزی را برای تأمین سرمایه در گردش فعالان بخش کشاورزی، دامپروری، طیور، شیلات و صنایع غذایی تقویت کند و این دستاورد در کنار افزایش منابع  تا مرز هزار همت، نشان می‌دهد این بانک همزمان با توسعه حجم منابع، به اصلاح ساختار و افزایش کیفیت آن‌ها نیز توجه داشته است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/680322" target="_blank">📅 17:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680320">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
محمد مخبر و محمد فروزنده جایگزین شهیدان لاریجانی و موسوی در هیأت عالی نظارت مجمع تشخیص شدند
.
🔹
مهلت ثبت‌نام آزمون‌های خارج از کشور علوم پزشکی تا ۲۴ مردادماه تمدید شد.
🔹
رئیس‌کل بانک مرکزی برای شرکت در اجلاس بریکس عازم هند شد.
🔹
پارلمان لبنان پیش‌نویس قانون مربوط به لغو مجازات اعدام را پس از اصلاحات تصویب کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/680320" target="_blank">📅 16:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680318">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سردار ابن‌الرضا: زیر بار حرف زور نمی‌رویم
سرپرست وزارت دفاع در گفت‌وگوی تلفنی با وزیر دفاع مالزی:
🔹
ایران همواره خواهان برقراری صلح و ثبات در منطقه بوده، اما این صلح نباید به معنای پذیرش خواسته‌های نامشروع و تحمیل ارادهٔ طرف مقابل باشد.
🔹
ملت ایران اجازه نخواهد داد دستاوردهای این مقاومت افتخارآمیز با فشار و حرف زور نادیده گرفته شود.
🔹
فتنهٔ اصلی در منطقه و جهان اسلام، رژیم صهیونیستی است و تداوم جنایات و تجاوزات این رژیم یکی از عوامل اصلی بی‌ثباتی و ناامنی در منطقه به شمار می‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/680318" target="_blank">📅 16:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680317">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
افزایش سقف وام برای زنان دهک‌های یک تا ۵
معاون امور زنان و خانواده ریاست جمهوری:
🔹
پیش از این با تلاشی که در دولت قبل انجام شده بود، برای زنانی که در دهک‌های یک تا پنج قرار داشتند، در صورتی که برای دریافت وام نیاز به ضامن داشتند اما توانایی پیدا کردن ضامن را نداشتند، ضمانت انجام می‌شد.
🔹
در هیئت دولت به تصویب رسید که سقف وام تا میزان سقفی که شورای عالی اشتغال هر سال تصویب می‌کند، افزایش پیدا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/680317" target="_blank">📅 16:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680316">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2bded3e4b.mp4?token=f3WQVLV5J1_wc4GT4dSsLMBjgDnjklOfTcayBCXSPAZt5RqihHGmcrrApxoiJfE4_3ylx8azW6NWLaqac5K6OhHLi8hAqB05K3BYol4zyIPfN8CPuo-FkQNihqpppE5n58WbUUGMeFpqmBHwQcymX2mo86rixfTKyN_kIj-GYIwy43TlSU_mKIflZt2yLRWsVDlqm-XynQVtf6YPCIe4lTVC2nxJC5tLdvOEOfbsL3GbrS7omu0q9z0rR-59WDLvlLYtKc2s39HsMbz23MWcFLuV4wioXS-Zv3BC-CNcT-pYjjWj-cyaNByl55VUGUzSnjl968rFzD2gxGprgYGKMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2bded3e4b.mp4?token=f3WQVLV5J1_wc4GT4dSsLMBjgDnjklOfTcayBCXSPAZt5RqihHGmcrrApxoiJfE4_3ylx8azW6NWLaqac5K6OhHLi8hAqB05K3BYol4zyIPfN8CPuo-FkQNihqpppE5n58WbUUGMeFpqmBHwQcymX2mo86rixfTKyN_kIj-GYIwy43TlSU_mKIflZt2yLRWsVDlqm-XynQVtf6YPCIe4lTVC2nxJC5tLdvOEOfbsL3GbrS7omu0q9z0rR-59WDLvlLYtKc2s39HsMbz23MWcFLuV4wioXS-Zv3BC-CNcT-pYjjWj-cyaNByl55VUGUzSnjl968rFzD2gxGprgYGKMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با گوش دادن به صدای ماشینت بدون مشکل از کجاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/680316" target="_blank">📅 16:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680315">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35e04feca1.mp4?token=aRaGd_87BhtAN1xXb0mcW7jH6v5C5x241hmyQjryAiTMOKQzI7oBLiaGoHm2PrJ4W_4PbxxOlFOcBu5mIm8pb0xrk_zpBf4ddciF5WlcP_PaonJfmhVhawghm0NFQ7nAVYsDtwqS04wklC3oAz2rknjokqevTUXO9GlgVRPu19Sc6rpvFIj6OZgchIfKP6yrQ3B2Ieo_Vg21AF6FHo-SL3rWZ_qtmk5NwDGYQ95m2f_3dr3DEBXlz-KU6d2eqyxdgOIA9SZmq1z7q2zeBLxNxHAaNqTSSJ2wAkVI2biDtKXde7OC0kAGjXKkVAiCgW5H5xk7WKISi0XdLzJpGzKu5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35e04feca1.mp4?token=aRaGd_87BhtAN1xXb0mcW7jH6v5C5x241hmyQjryAiTMOKQzI7oBLiaGoHm2PrJ4W_4PbxxOlFOcBu5mIm8pb0xrk_zpBf4ddciF5WlcP_PaonJfmhVhawghm0NFQ7nAVYsDtwqS04wklC3oAz2rknjokqevTUXO9GlgVRPu19Sc6rpvFIj6OZgchIfKP6yrQ3B2Ieo_Vg21AF6FHo-SL3rWZ_qtmk5NwDGYQ95m2f_3dr3DEBXlz-KU6d2eqyxdgOIA9SZmq1z7q2zeBLxNxHAaNqTSSJ2wAkVI2biDtKXde7OC0kAGjXKkVAiCgW5H5xk7WKISi0XdLzJpGzKu5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاروان موتوری خیبری‌ها در شب‌های جنگ دوازده روزه چگونه شکل گرفتند؟/ در یک شب ۶ موتور، به ۷۰۰ موتور که تبدیل شد
🔹
برنامه تلویزیونی «دچار» هر روز ساعت ۱۸:۴۵ از شبکه نسیم پخش می‌شود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/680315" target="_blank">📅 16:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680314">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVUhsUp2UId7R_8cVz-udXay3mpiSiUnzL5KbXWP-z84XXpCNpoR7t95rN05c5TX6m_WeP919X2UY4bnIW18nA4oG9mreWk0xLSXY58eV8HF4maqnWvFhVmCDQCZpv6TzJRbsgKynwqf2I5E6_eI7lWvxiBY7Qk7y2UvIWBlyU-wbaq0qQIbcPM9xZR0ri8q1wsnq9ejtJMwxOqtDbPz5OIvp8UdRIvDgEYbv298MyBsD9lCjjGd02CqaoIyA30dhXOKsF5XjM-I9aa6fD9oVmjlkf34R7GpIg2f2SMa1WcF9k9GAg1P66-Psxc1cIGVNIoFKD-asAn40s1SG1TgPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون وزیر کار: نقص اطلاعات فراجا، کالابرگ برخی افراد را قطع کرد
🔹
پیگیری‌ها از وزارت رفاه نشان می‌دهد کالابرگ برخی افراد حاضر در کشور به‌‌دلیل ثبت‌نشدن اطلاعات ورود در سامانه فراجا متوقف شده و وزارت رفاه پیگیر اصلاح این اطلاعات است.
🔹
افرادی که صرفاً به عراق سفر کرده‌اند و پس‌از آن به کشور بازگشته‌اند و به کشور دیگری سفر نکرده‌اند، اطلاعات لازم از سوی فراجا ارائه می‌شود تا از فهرست افراد مشکوک به اقامت خارج از کشور خارج شوند و کالابرگ آنها مجدداً برقرار شود./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/680314" target="_blank">📅 16:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680312">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4fc4927ea.mp4?token=tcW2i2gbyGTd-hW2udDuO8Cc6HKuhhyXUqFEnsACH07Ru80ZChsWuOhQ1hlcLORlBbtZpc27yOOkH05xcZlLl9WFfY5Y7i-j8IZJN-Kd1CKWhMyZ1giGRvcvrt6qUyc-4ENqaJBB3OcXFMPcIwtNqrL8qUyI_k8gJLcceoxfqY9mXvkR4VtGDajfp9Gv4qcVnqXOUae09q7ESwLhT286SSkExVKQkZczf8atgztqGspxaZfJWgYmv4Skl2Vv_3AEo5muDMKYSUBnKy-ghgi_n6uKHs8L5d5Ksg4Ajan-1bJ1hgJ9J2-7nB0Npi12GG19g654ygJcGBvOVYA4DVatvhORZfLrakb0LDkI2x6pXzAS8vIpGkyirHRNNNa_iSiJmTHTL9X33yFKYMmEON9xOn49qybQrbr-31U8BBUEnHyKrm4lo_NOCGJL6UPy5PP4oaoO1TNzwZkPNWd7jgXUcyXbifiraROuqnZ5EPQ-NcpiUM1ieTs_lpzywnWmfEPkoR6ewKqEHKFQDCb3IS5U6dKO5Mox3aOLKanM1ZWGRG4XcUsFJEGMOxSHu_KaCmPA6UCpEJgnlZpHcEPopDnh5BFv6MOWDSnokr-YyZkae9x_cjOlQK0u2atCCOGVs4qRgOJRWoRCSnjdEj0X0eu4JQAEgGkL-y5SJxKH2A3xBpM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4fc4927ea.mp4?token=tcW2i2gbyGTd-hW2udDuO8Cc6HKuhhyXUqFEnsACH07Ru80ZChsWuOhQ1hlcLORlBbtZpc27yOOkH05xcZlLl9WFfY5Y7i-j8IZJN-Kd1CKWhMyZ1giGRvcvrt6qUyc-4ENqaJBB3OcXFMPcIwtNqrL8qUyI_k8gJLcceoxfqY9mXvkR4VtGDajfp9Gv4qcVnqXOUae09q7ESwLhT286SSkExVKQkZczf8atgztqGspxaZfJWgYmv4Skl2Vv_3AEo5muDMKYSUBnKy-ghgi_n6uKHs8L5d5Ksg4Ajan-1bJ1hgJ9J2-7nB0Npi12GG19g654ygJcGBvOVYA4DVatvhORZfLrakb0LDkI2x6pXzAS8vIpGkyirHRNNNa_iSiJmTHTL9X33yFKYMmEON9xOn49qybQrbr-31U8BBUEnHyKrm4lo_NOCGJL6UPy5PP4oaoO1TNzwZkPNWd7jgXUcyXbifiraROuqnZ5EPQ-NcpiUM1ieTs_lpzywnWmfEPkoR6ewKqEHKFQDCb3IS5U6dKO5Mox3aOLKanM1ZWGRG4XcUsFJEGMOxSHu_KaCmPA6UCpEJgnlZpHcEPopDnh5BFv6MOWDSnokr-YyZkae9x_cjOlQK0u2atCCOGVs4qRgOJRWoRCSnjdEj0X0eu4JQAEgGkL-y5SJxKH2A3xBpM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: مسئول بی‌کفایتی داریم که در زمان جنگ به وظایف خودش عمل نکرد و در زمان مناسب خودش رسیدگی می‌کنیم
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
در کشور فرهنگ استعفا نداریم. همچنین ندیدم کسی عذرخواهی کند. خیلی ها وابسته به میز و صندلی هستند و طرف با اینکه می‌داند مقصر است، اما حاضر نیست از مردم عذرخواهی کند.
🔹
در کشور مسئولانی داریم که همه شب‌ها در یکجا نخوابیده‌‌اند؛ نه از روی ترس بلکه برای اینکه باشند تا به ملت خدمت کنند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/680312" target="_blank">📅 16:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680311">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dF3pFLSVdDBRPHCZwiJxsmoQoFPpt-sL0vxKlqlfyro4Zv7fdX-18U6sMiRArliNb_vAP43wZEMRTzmIQhX2WFP3zQr6BGD07fRRR6YlWr0IVpUd7nF__NSwwAWUNKRLHesfJrhFBh7rJNIatkpdIDi4We8xEUaoqFzxgyExQlsiC_JNdBABmgNpr_RVpmk8QRIyg5M9aZJfX1U9vL_SDtK1RliN_1XDT8iZp9ak0SXba8Gypy3mWLQr3DKap48rPrOzl4FhSwRFEwtlZZsu78o0MKRcIzOHZhm4zMy-6k0fpgFh5fsJSqnYcPDzALd1IjsNod7Go8w4logWUcrmIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: ایران در برابر هیچ تهدیدی از حقوق خود عقب نشینی نمی‌کند
دبیر شورای عالی امنیت ملی ایران:
🔹
جمهوری اسلامی ایران در برابر هیچ تهدیدی از حقوق و منافع ملت خود عقب‌نشینی نخواهد کرد.
🔹
در همین راستا تصمیمات در این حوزه باید قوی‌تر از گذشته با شناخت دقیق صحنه و با تدبیر و شجاعت اتخاذ شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/680311" target="_blank">📅 16:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680309">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4b3e15c2.mp4?token=MdxKuXuIkgPugAcWpb-7zSsbBaUOZZpbAFvOTVTGCJGrHFQdekav7CAr1AvG93lirGhnZX45U_5U_dnixERHK9vyOLdrjxXVtcjCFHdcYviR_4X7T2vQRdr0YD2uNRhcHsHw96FTx51rQhb5HN4mCUU22Q48XmaPCPAkMQSwjeQRHOJ92sJ0drgVYK7EuWe6UX0J10YQC1BK--0cDHzSSDFbyMmsljQi1iyHyXR5SLu_bBs6oOEFCtFlVAzh7LSYeemIdUZbLV2yiMGH-i_lD6ZKLB7rsfRgEXO1kjbhWe2WxGNaBijGYfsE-yrgY5Tll1wVAFnH3Z9OYqgr5qSB8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4b3e15c2.mp4?token=MdxKuXuIkgPugAcWpb-7zSsbBaUOZZpbAFvOTVTGCJGrHFQdekav7CAr1AvG93lirGhnZX45U_5U_dnixERHK9vyOLdrjxXVtcjCFHdcYviR_4X7T2vQRdr0YD2uNRhcHsHw96FTx51rQhb5HN4mCUU22Q48XmaPCPAkMQSwjeQRHOJ92sJ0drgVYK7EuWe6UX0J10YQC1BK--0cDHzSSDFbyMmsljQi1iyHyXR5SLu_bBs6oOEFCtFlVAzh7LSYeemIdUZbLV2yiMGH-i_lD6ZKLB7rsfRgEXO1kjbhWe2WxGNaBijGYfsE-yrgY5Tll1wVAFnH3Z9OYqgr5qSB8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این فرمول زمان خرید سکه و طلای آبشده رو بدست بیار #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/680309" target="_blank">📅 16:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680308">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b43b28bb1f.mp4?token=dPFSfWy7nqtpzYRCAfpqgTQgf2j5tBxOT3n-zZ3MAYwoZ1xIuLsNMjlB3twZWc1TU7xNQMIE7uh0wvTf4u7jpxJSckcT6OkLmSirX-hvwOKsWSyupCfSq-0XZ3rJNTaaLAUKXMXm2KHhz4AJMXIuay7pxExzMWczdhfYfnN8UCR85-6MlXbWdNAtOqBZ3_pg4KIpH3IQmfolRsgtNTP6qEgTrcwwP7kdalZsLp5b4sGceLY2_trWXtvDUGjIZFApUsyNHSaO00ziYs0U4ANWG03a58d9NzyH9_1Wxttp5pNEteU4fLQXVJvfiyd5ffaJlx11jB1UPLzmpv3v8kgrsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b43b28bb1f.mp4?token=dPFSfWy7nqtpzYRCAfpqgTQgf2j5tBxOT3n-zZ3MAYwoZ1xIuLsNMjlB3twZWc1TU7xNQMIE7uh0wvTf4u7jpxJSckcT6OkLmSirX-hvwOKsWSyupCfSq-0XZ3rJNTaaLAUKXMXm2KHhz4AJMXIuay7pxExzMWczdhfYfnN8UCR85-6MlXbWdNAtOqBZ3_pg4KIpH3IQmfolRsgtNTP6qEgTrcwwP7kdalZsLp5b4sGceLY2_trWXtvDUGjIZFApUsyNHSaO00ziYs0U4ANWG03a58d9NzyH9_1Wxttp5pNEteU4fLQXVJvfiyd5ffaJlx11jB1UPLzmpv3v8kgrsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه فکر می‌کنی وظیفه ‌ات رو انجام دادی، این ویدیو برای توئه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/680308" target="_blank">📅 15:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680306">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
حجت‌الاسلام رفیعی در سمت خدا: هر غم‌دیده‌ای به زیارت امام رضا(ع) برود، غم دلش برطرف می‌شود/غم و گرفتاری راه دارد و در روایات برای عبور از این روزهای سخت توصیه‌هایی آمده است/ توجه به خدا، استغفار و زیارت اهل‌بیت(ع) از راهکارهایی است که برای آرامش دل و گشایش در زندگی بیان شده/ در این میان، زیارت امام رضا(ع) برای غمدیدگان جایگاه ویژه‌ای دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/680306" target="_blank">📅 15:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680305">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین مهارتی که در سیستم آموزشی به آن کمتر توجه شده چیست؟</h4>
<ul>
<li>✓ تفکر انتقادی و حل مسئله</li>
<li>✓ مهارت‌های ارتباطی و کار تیمی</li>
<li>✓ سواد مالی و مدیریت پول</li>
<li>✓ خلاقیت و نوآوری</li>
<li>✓ خودشناسی و تصمیم‌گیری</li>
<li>✓ سواد رسانه‌ای و فضای مجازی</li>
<li>✓ مهارت‌های ورود به بازار کار</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/680305" target="_blank">📅 15:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680300">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Id1GZtywrNFttz7n4jlskBldK-mwyR6LOuM46NBBVnsQqH09MM4O85fJR8IgjJQyNep_Kr8sBoVfeOXHPSr2feDmCQ8JEHuqtidC99zGhQ39Xoxs4C-TFxP3WDnpR7WIJg_Kp9-btG8kpPszxlQHAorhuYLxBSZvef64Nt5_vOy-5t9FJ9tE7MxNHfuYZSvzP-mHEUKVQT3pOxIOzLssMM4NY7loew-L6PteoH6NchI73LJBPG-pdG03wO7tZgUFenHKkULALMUy1T4xlDG5-VJsqsp4izc7sq_NLwqqgx_Y3OoU1lSXgoJS9fMR2nURJHqk4rf1u4faG41iQ_TkOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان سنجش: کارت ورود به جلسهٔ کنکور از دوشنبه قابل دریافت است
سازمان سنجش:
🔹
کارت‌های شرکت در آزمون متقاضیان کنکور سراسری به‌همراه راهنمای شرکت در آزمون از دوشنبه ۲۶ مرداد تا چهارشنبه ۲۸ مرداد در سامانهٔ سنجش مشاهده و پرینت فعال خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/680300" target="_blank">📅 15:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680299">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Etzh8Q5aEUCKoRgfK96lNzXCP7ynl6oEkzQ3if2FsStQfvWaUkITB_8pfLiU8yon4Sf1o5cYKkeD03hoBk-_Lk3sfH4Nodpjut7w7nFvA68d6Ffadsc4IfbLQ8Gxz2aQ3gnvL4BEGhKqayFYO1BJdoCO4Xa-Pw0-3uMxG-Q_fdIjmjbVFjwMmDBniZUJaaTK2LrjiFTVEUEaJTr5-MfhhsHB7p5LkXK7u6CBLvKt8CWdhp1n5y3d28Pe1Fp2ShyzROBdVUmI-4OGZKhfOMasjSlIekDq3-PtoRbEfAXOj74CvZdAfj5HWxoneUUMswLkoblezeHU0RWC_Tes-0TZNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علت مشکلات مو رو بدونیم تا بهتر مراقبت کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/680299" target="_blank">📅 15:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680298">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ba1afedb.mp4?token=i8WnEM7Gnygw4LfLwaGziDGbht14_ru1cACQ4-h45E_YnyPm_ssKEpA8dOV8alEc2Ag0CC4hfnkRK8GNE3uF7FLzlQjjyc9iybaW4-DrNJkJasjeKHsiWQpom7rAbz6wQP-W5AXkbx-sx7erXWnbn0p0M1t22Pqod7bC9PlPubHYXFnbU8HFyvgNabZ3GaqyTgN9zRuwqySnlz7Ri214mnzG0ZquI_-vvUNlMJfaMyMt8yyWLtfx3yv2-QZcOqLHkppSixmL6XtxhFJ6Ve2nIGcIiRmH5NcpBo-v41Ri_e-bkIwEFzAIIQ8WqdP26umTBEPPo4LDWS5wcRSkb64Q8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ba1afedb.mp4?token=i8WnEM7Gnygw4LfLwaGziDGbht14_ru1cACQ4-h45E_YnyPm_ssKEpA8dOV8alEc2Ag0CC4hfnkRK8GNE3uF7FLzlQjjyc9iybaW4-DrNJkJasjeKHsiWQpom7rAbz6wQP-W5AXkbx-sx7erXWnbn0p0M1t22Pqod7bC9PlPubHYXFnbU8HFyvgNabZ3GaqyTgN9zRuwqySnlz7Ri214mnzG0ZquI_-vvUNlMJfaMyMt8yyWLtfx3yv2-QZcOqLHkppSixmL6XtxhFJ6Ve2nIGcIiRmH5NcpBo-v41Ri_e-bkIwEFzAIIQ8WqdP26umTBEPPo4LDWS5wcRSkb64Q8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فروشگاه‌هایی که قیمت‌های قدیمی را از روی اجناس پاک می‌کنند و با قیمت جدید به مردم می‌فروشند
رئیس تعزیرات تهران:
🔹
با فروشگاه‌های زنجیره‌ای که اجناس را با قیمتی بالاتر از قیمت درج‌شده بفروشند به‌شدت برخورد می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/680298" target="_blank">📅 15:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680293">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19111ad870.mp4?token=WiePHUR8RH-HReJFhLojqCLgCftP8duEU6LW3XJbU2F8WAkaxoDQ3oRI9mlolGUgqfX38_UCbKij1KDG1A2rEPKx0ILfNSwGkZgJ3_RVKKQgW1kub_QGD-QUFPgT6mDgUJXKzLQXw-YLcq6YT6fj7Ra7u7AtDyv5x_UcrhloRQO4x5m6VbLg57PqPfczbOXygZYxgK4GEN9A5fqlyNINcIGDhyqescM9XenLNZ5EtyTETVxzSTgESIA5_Mn8BqtCVjDCytF5BX5qq3xp3IsF3lHdjj7Zq5pXG5vNmdfzW0zSWkXOGjnLu_f7pp89rSjrtjn1m3NUAo_a7n-9pXJ91Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19111ad870.mp4?token=WiePHUR8RH-HReJFhLojqCLgCftP8duEU6LW3XJbU2F8WAkaxoDQ3oRI9mlolGUgqfX38_UCbKij1KDG1A2rEPKx0ILfNSwGkZgJ3_RVKKQgW1kub_QGD-QUFPgT6mDgUJXKzLQXw-YLcq6YT6fj7Ra7u7AtDyv5x_UcrhloRQO4x5m6VbLg57PqPfczbOXygZYxgK4GEN9A5fqlyNINcIGDhyqescM9XenLNZ5EtyTETVxzSTgESIA5_Mn8BqtCVjDCytF5BX5qq3xp3IsF3lHdjj7Zq5pXG5vNmdfzW0zSWkXOGjnLu_f7pp89rSjrtjn1m3NUAo_a7n-9pXJ91Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین‌وچروک‌‌های لاله گوش اصلاً بی‌دلیل نیستند!
👂
🔹
مکانیسمِ این فرورفتگی‌ها مثل یک ردیاب ۳ بعدی عمل می‌کند؛ موج‌های صدا را طوری تغییر می‌دهد که مغز ما می‌تواند دقیقاً تشخیص بدهد صدا از بالا، پایین، جلو یا پشت سر می‌آید!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/680293" target="_blank">📅 15:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680292">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5LrCOvLAhT3ExABjQ4PXZfFV03wTSgArLsFvar_tHZM3-HTaje35FkXgGnAsJqi_PhPk2aLIkkeIqTpQyTh5Fxu5lVbiP1ysXzLVZQyTvy90bMMM1g4-M4EkJ9yLi4tIlZdAgO_UGrWXoiUsXcbtaM1fZVDcF24FgKwlvf0gDtQ_hMdidfZCrAqR_ienfGuHlWWZOzEO5cJB0HNFDC9psl-HMZiOvPWUdpRBrQwowedAWkOPYW_xg7Z8e2EuLvbHSbFT56VTlkHQYKRaosYkesdojvAEsofSWJ9b_kk503i5w3KAlmFG5l8vO7SbHLbNC89hhWAZBpkpRaqEKkMWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رز ترنج؛ روایت فصل اول یک مسیر بزرگ
نقد‌شوندگی واقعی با ۳۹ همت ارزش معاملات
🟢
صندوق طلای «رز ترنج» در اولین سال فعالیت خود، ارزش معاملاتی بالغ بر ۳۹ هزار میلیارد تومان داشت.
🟢
هم‌زمان، بازارگردانی فعال و حرفه‌ای، در کنار حجم بالای معاملات، نقدشوندگی واقعی و بدون حباب قیمتی را برای سرمایه‌گذاران فراهم کرد.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/680292" target="_blank">📅 15:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680291">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e3869a5d.mp4?token=YRJ9piOK3J-cT_uE7-cY6kTgMZr6CUR4SPuExp9ZNhfGyq7_vcW15UH9pJiKrEHV36UlCmCjfHieLB3DXIzWbwjMEvO_gcOKyXBjzKNa_pmJZvC9J25_VoMt16AjDLQE2_lRBTP0rvTCq-G2UaQR7pdALfaiNkZeWN1ozuhRC9GtwVtN19Dh0-AsCbFP1Y7GDLryrCGkDDP66hTT8LDKXe_GsfhPNaNQGWJ3EC2xRw90dcS6Pzw4IGDHcDUmjjFQ6YCO5ihK_EKB4sNsDIUKye0vkdiwtDuUssdeT2kA0knylMqYATAKcpdIHrSCuwxpLL0QGwJx4M5tr_hxdGa-_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e3869a5d.mp4?token=YRJ9piOK3J-cT_uE7-cY6kTgMZr6CUR4SPuExp9ZNhfGyq7_vcW15UH9pJiKrEHV36UlCmCjfHieLB3DXIzWbwjMEvO_gcOKyXBjzKNa_pmJZvC9J25_VoMt16AjDLQE2_lRBTP0rvTCq-G2UaQR7pdALfaiNkZeWN1ozuhRC9GtwVtN19Dh0-AsCbFP1Y7GDLryrCGkDDP66hTT8LDKXe_GsfhPNaNQGWJ3EC2xRw90dcS6Pzw4IGDHcDUmjjFQ6YCO5ihK_EKB4sNsDIUKye0vkdiwtDuUssdeT2kA0knylMqYATAKcpdIHrSCuwxpLL0QGwJx4M5tr_hxdGa-_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اژه‌ای: تا جایی که ممکن است اموال، مدارک و وسایل مردم را کمتر نگهداری کنید
رئیس دستگاه قضا:
🔹
نگهداری طولانی مدت اموال و مدارک ضبط شده از طرفین پرونده ها در شعب قضایی، ممکن است موجب فساد یا تضییع حقوق افراد شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/680291" target="_blank">📅 14:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680290">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/100da9ed3a.mp4?token=XiCs8Dga1sRMpknomGwlfn-Em6fkyCIZZSZ4BAii4F_7bFzOKfhqLiF69Sj1s3Eu6pJC6nL5koNIhprUH0yF0ozU1NKann3yx30jk-NsTVBINOW3pmC-GYqBorElCnAx7DyPw1C0wubY-DjLc5x68BMhbp-kAmdTGH-PveuOVwvFMlmTgGKmA2rGMrwT-0R5cuHWmogBH3yQPQ_7o-71dE6sfq1IgRDaa4JXo9hmE3y57uIkvIEvZk9UTwWWzkWD8VgUrGHr49Izf9Wwkq4-cyvyyvJXxLkdK1lsp6QVbQPHHtT7Z1_oJVpHDzGLLROmBR7k71ILk2mAfuJ2YNEtCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/100da9ed3a.mp4?token=XiCs8Dga1sRMpknomGwlfn-Em6fkyCIZZSZ4BAii4F_7bFzOKfhqLiF69Sj1s3Eu6pJC6nL5koNIhprUH0yF0ozU1NKann3yx30jk-NsTVBINOW3pmC-GYqBorElCnAx7DyPw1C0wubY-DjLc5x68BMhbp-kAmdTGH-PveuOVwvFMlmTgGKmA2rGMrwT-0R5cuHWmogBH3yQPQ_7o-71dE6sfq1IgRDaa4JXo9hmE3y57uIkvIEvZk9UTwWWzkWD8VgUrGHr49Izf9Wwkq4-cyvyyvJXxLkdK1lsp6QVbQPHHtT7Z1_oJVpHDzGLLROmBR7k71ILk2mAfuJ2YNEtCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگ‌ترین پالایشگاه روسیه که در ۶۵۰۰ کیلومتری مرز اوکراین قرار دارد، در آتش سوخت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/680290" target="_blank">📅 14:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680289">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd3c187fd.mp4?token=FGWaaUc34igQMUKP0pbpenx4WBgqooNot1r3WOuEGfceFQgMlK56RsEugNebku6looEpRSHqOoVUEcF5bqDUOqntVhmNircir5RzjZO-8sQCtBVPC8R44fk5BzNNZbfYJmNCNs3LONh12oUHE_er4UbgbE_b7_s_aTrykqyr4O1pmI7vgM1GNsAsA2hb5slkpeon0WBfvp-VkOEl6xL885ZtKOE3g6BBwXtJndfFWFclnpIlHxJAP340wYpTFiSGjRtU9nLiXV82iob_ygQGKNFqDXi5uUugj0opOniaWzWuVvzHc16XXiUGzNKxmgNifdgUdPmpveHV-SJxQJVLgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd3c187fd.mp4?token=FGWaaUc34igQMUKP0pbpenx4WBgqooNot1r3WOuEGfceFQgMlK56RsEugNebku6looEpRSHqOoVUEcF5bqDUOqntVhmNircir5RzjZO-8sQCtBVPC8R44fk5BzNNZbfYJmNCNs3LONh12oUHE_er4UbgbE_b7_s_aTrykqyr4O1pmI7vgM1GNsAsA2hb5slkpeon0WBfvp-VkOEl6xL885ZtKOE3g6BBwXtJndfFWFclnpIlHxJAP340wYpTFiSGjRtU9nLiXV82iob_ygQGKNFqDXi5uUugj0opOniaWzWuVvzHc16XXiUGzNKxmgNifdgUdPmpveHV-SJxQJVLgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش رسانه‌های مختلف جهان به انتصابات جدید رهبر معظم انقلاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/680289" target="_blank">📅 14:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680288">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
رسانه قطری: توافق مکه بی‌معناست؛ چرا ائتلافی ضداسرائیل شکل نمی‌گیرد؟
عربی۲۱:
🔹
توافق مکه مشخص نکرده در برابر تهدیدهای منطقه‌ای، از جمله اسرائیل، چه موضعی خواهد داشت و هیچ‌یک از این ائتلاف‌ها اسرائیل را به‌عنوان دشمن معرفی نکرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/680288" target="_blank">📅 14:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680287">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
تنها جمله‌ای که پدر مینابی بعد از شهادت دخترش گفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/680287" target="_blank">📅 14:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680286">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8715daf57.mp4?token=E8Ze7hLVgKQURM20n9Qg6U7vp8hcatdi5xk7anoE3CfY9YWo7jroZB9sK7LmobzbCdbpd7dqX4KDm4dtgo8ybk-LVXkBMU3Ta0eaOIX89FQE1ssCPX7aWg0Ka01QXiik3Unn7-SaF4ocPP2K4jLsriZxsn_5OXu0Ol9bW9AfvXpzqnYxyFOeqmt6Jlzj5kSKkOr8Qb6K2ceMi-aAwyoL4OaimpMQMZ6o623jwq57sbDXF_9HQNh-sXs2JiM7lxDhCe6z6noVAFGvye-nGDK85pSD2f5yW8plVyHKUMEU1iIbLqOQmSLxj7JnDmYcQ_nKHCdDzoonuwfKrAQzUuyMRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8715daf57.mp4?token=E8Ze7hLVgKQURM20n9Qg6U7vp8hcatdi5xk7anoE3CfY9YWo7jroZB9sK7LmobzbCdbpd7dqX4KDm4dtgo8ybk-LVXkBMU3Ta0eaOIX89FQE1ssCPX7aWg0Ka01QXiik3Unn7-SaF4ocPP2K4jLsriZxsn_5OXu0Ol9bW9AfvXpzqnYxyFOeqmt6Jlzj5kSKkOr8Qb6K2ceMi-aAwyoL4OaimpMQMZ6o623jwq57sbDXF_9HQNh-sXs2JiM7lxDhCe6z6noVAFGvye-nGDK85pSD2f5yW8plVyHKUMEU1iIbLqOQmSLxj7JnDmYcQ_nKHCdDzoonuwfKrAQzUuyMRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
براساس علم عصب‌شناسی کتاب خواندن برای نوزاد، قوی‌ترین محرک رشد مغز است
🔹
در سال‌های اول، مغز کودک در هر ثانیه بیش از ۱ میلیون اتصال عصبی جدید می‌سازد!
🔹
شنیدن آهنگِ صدای والدین و دیدن تصاویر کتاب، دقیقاً همان چیزی است که این شبکه عصبی را فعال و قوی می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/680286" target="_blank">📅 14:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680284">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شهردار بوشهر برکنار شد
.
🔹
انصارالله: عربستان به دنبال وارد کردن یمن به جنگ‌های بی‌پایان است.
🔹
وزیر خارجه آلمان: ایران وارد مذاکرات با همسایگان منطقه‌ای و آمریکا شود.
🔹
براثر وقوع سیل و طوفان در فیلیپین ۱۹ نفر جان باختند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/680284" target="_blank">📅 14:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680283">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
رئیس پلیس‌راه خراسان شمالی از اعمال محدودیت تردد انواع کامیون و تریلر در محور فاروج–جنگل گلستان و بالعکس از ۲۰ مرداد تا پایان هفته خبر داد
🔹
ممنوعیت تردد شامل انواع ناوگان باری است و وسایل نقلیه حامل مواد سوختی، مواد بهداشتی، کودهای شیمیایی و کالاهای اساسی از جمله گندم، جو، برنج، ذرت، سویا و دانه‌های روغنی از این محدودیت مستثنی هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/680283" target="_blank">📅 14:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680282">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: در زمان جنگ، جلسات را در هتل‌ها و ساختمان‌های خصوصی به طور محرمانه برگزار کردیم
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبر فوری:
🔹
انتقال بالغ بر ۴۰ درصد کالا در زمان جنگ نسبت به شرایط عادی بیشتر شد.
🔹
در زمان جنگ هفته‌ای ۴ جلسه به صورت حضوری برگزار می‌کردیم که مکان‌های آن به صورت محرمانه تغییر می‌کرد. در کشور شبهه ایجاد شده بود که نمایندگان نیستند، اما دستگاه امنیتی اجازه ندادند که مجلس به صورت رسمی کارش را ادامه بدهد.
🔹
با مجوزی که با تایید شورای نگهبان گرفتیم این موضوع به قانون تبدیل شد که مجلس در شرایط اضطرار می‌تواند جلسات خود را با فضای مجازی انجام بدهد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/680282" target="_blank">📅 14:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680281">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
الجزیره: آمریکا به‌دنبال راه خروج از جنگ با ایران؛ ترامپ از مذاکرات کنار گذاشته شده است
🔹
ونس،روبیو،رئیس سازمان سیا و دن کین برای خروج از بن‌بست جنگ با ایران، بدون حضور ترامپ، گفت‌وگوهای محرمانه‌ای داشته‌اند./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/680281" target="_blank">📅 14:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680280">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه حمایت از کودکان مبتلا به سرطان خراسان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIra1MrhPoBWi_ttyH8-wrRBCi912BHkrrfqCdVHSBwzoYz7BujloyCqZdvJGJz7EQ-UpLeBxHQxwaZ4AhkGtiH3b5IQinMmgL8T-fFchP4TthJNJilEHBornozedJYTVzNhcFuiejVTt4G_b9hriqm_rOG15rYwT2kkGmnm_wU9PwGpT8iDfCvEXXghPYD4bETCCWZIDzSi1aVwrnGdIwoyJok37ARTvMtsbQpLRt5Di3DPcK_jeFqgOkNxT9ALKqUsowcN9TWoKTkZlbAcJW7a7bwSVFS8eW1dZJIBnB0Zmfz0sqDIc8rKT9HfbtoEdb4-X6EBOVMgh8W5eIiQrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«برای بچه‌ها هر روز تابستون، مهمه»
؛ حتی امروز
🎗
با هر سهم ۱۵۰ هزار تومانی، کنار کودکان مبتلا به سرطان باشیم تا با لبخند سلامت روزهاشون و بگذرونن
💛
🔗
لینک کمپین:
https://sahm.khorasan-charity.org
شماره کارت :
5047-0610-9009-3739
————————————
💛
راه‌های ارتباط با ما:
☎️
051-31504
🌐
www.khorasan-charity.org
🆔
instagram:
@khorasancharity
🆔
telegram:
@khorasan_charity</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/680280" target="_blank">📅 14:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680279">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
مقام یمنی: ما هرگز درهای گفت‌وگو و مذاکره با عربستان را نبستیم
🔹
این طرف سعودی است که مذاکره را رد می‌کند.
🔹
صنعا به مدت چهار سال به آتش‌بس و کاهش تنش پایبند بوده و هیچ‌گونه اقدام خصمانه‌ای علیه عربستان انجام نداده است.
🔹
عربستان از فرصت آتش‌بس سوءاستفاده کرد تا عمدا وضعیت را در عرصه‌های اقتصادی و معیشتی به منظور فرسوده کردن ملت ما تشدید کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/680279" target="_blank">📅 14:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680276">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fICUchnAPuW8I5ygiMz0_fu0nGiGFRRwwdCSyGXUVMqVTWSTCZ8K_eOmvJauIF4Wn26MGwDTvoyUW2G4tXwIUfghtcUB-fteDc8qZQN0wcPqD1sw7Fc2_kDtklb4TWLlFXmAEzZ9_RjIT7F5b7W9yr4T80Pj5XGnt9jSPGb57hMU83pYfXlRIVA7f6CWGTgfP5XrXhQMKVs1sCnHIKMOKGuLRwbbgdL8HmPxrP-mTYCdin62ngFRFy-_a6Tq4Q2OFW7MP7njvGdcQv7OQUXsezhpz6j-4ssHrpFZUiGCnuquLBZm_JYEuN2DRXBShP3QscAmV6RW3q87_x7X_hE2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8084ed1d3c.mp4?token=LrhUgaMIIz2k3b2hdimjAmK0S9fkYZ8D3Ygbp3_GtrCF6bvLRlfcZJFJjAy03rVLJ92x1vfpaIM8dzl6DwWED29nBd3Wru-aQd1q9JhxUtFl4PXTNz2SHxdjVih2CkLHPs4Yy9IQ__U6-7tjTfVTecm_htzI8f7pafR35mhfylBt8hkVdVrFVwc2E_8TjGWGtEqk0AxU7G8jmcDzllPRZH6_WsEEUosgUfzRqFP7lqdrcovtiU3l119n5bbC5YhihCYIQrvuk-EBbufSasaBC_KoCK3MrpJLcQYUe5OS16xsX24r3ffO1xGQz--VN9EXdsKcFiMOnNxGdta3gWBYnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8084ed1d3c.mp4?token=LrhUgaMIIz2k3b2hdimjAmK0S9fkYZ8D3Ygbp3_GtrCF6bvLRlfcZJFJjAy03rVLJ92x1vfpaIM8dzl6DwWED29nBd3Wru-aQd1q9JhxUtFl4PXTNz2SHxdjVih2CkLHPs4Yy9IQ__U6-7tjTfVTecm_htzI8f7pafR35mhfylBt8hkVdVrFVwc2E_8TjGWGtEqk0AxU7G8jmcDzllPRZH6_WsEEUosgUfzRqFP7lqdrcovtiU3l119n5bbC5YhihCYIQrvuk-EBbufSasaBC_KoCK3MrpJLcQYUe5OS16xsX24r3ffO1xGQz--VN9EXdsKcFiMOnNxGdta3gWBYnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاسیسات آرامکو عربستان منفجر شد
🔹
وزارت انرژی عربستان حمله به تاسیسات آرامکو در منطقه جازان طی بامداد یکشنبه را تایید کرد. طبق منابع عربی چندین انفجار در این تاسیسات گزارش شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/680276" target="_blank">📅 14:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680275">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وهشتم از فصل پنجم
🔹
اولین قسمت از روایت تجربه‌ نزدیک به مرگ آقای سید محمد موسوی که در میان انجام امور روزمره به ناگاه روح از جسم جدا شده و از طبقه اول آسمان تا طبقه هفتم را پیموده و در هر آسمان آثار تمامی رفتارهای دنیوی از جمله آزار یا خیررسانی به والدین، خویشان و حتی حیوانات را درک کرده و هر طبقه را با لطف و نگاه اهل بیت گذرانده و اجازه ورود به طبقه دیگری را پیدا می‌کند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سید امید متقی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/680275" target="_blank">📅 14:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680274">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه قطر: مذاکرات میان عمان و ایران اکنون در مرحله پیشرفته‌ای قرار دارد./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/680274" target="_blank">📅 14:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680273">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f478208a45.mp4?token=l5I7rbdDZSb-ulV7NSnNLK8C8UEeS2_GkwIdmLNe9rPsXqK3T0qlNk5XxHq55NlF-scYBow2z4pHRAx4zdpdGndkdWATuRfOVR7uqU0VzSJvWcBQjHQE0BBWX6hxwCGJNMNXZwz1O-aAF5d4AFHmOSjXibGYjLQBEwhvX7nx0B_kvwdBK6kUBbelS8x0VT4z1R3c99KikNPG-xv_GyYlSbcReH4fCSp760aXC7IA1ijIGZVFcDHj7rXPfJRd5FR60HJR0AaJ0JS2xcQ7oz-cDpSEEB4jR5gp7IxlNKI3egY-xfe7sPWWBXPdaaBSpz7DpnYqzfLh9iBucX3go784WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f478208a45.mp4?token=l5I7rbdDZSb-ulV7NSnNLK8C8UEeS2_GkwIdmLNe9rPsXqK3T0qlNk5XxHq55NlF-scYBow2z4pHRAx4zdpdGndkdWATuRfOVR7uqU0VzSJvWcBQjHQE0BBWX6hxwCGJNMNXZwz1O-aAF5d4AFHmOSjXibGYjLQBEwhvX7nx0B_kvwdBK6kUBbelS8x0VT4z1R3c99KikNPG-xv_GyYlSbcReH4fCSp760aXC7IA1ijIGZVFcDHj7rXPfJRd5FR60HJR0AaJ0JS2xcQ7oz-cDpSEEB4jR5gp7IxlNKI3egY-xfe7sPWWBXPdaaBSpz7DpnYqzfLh9iBucX3go784WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقتصاد رانتی و نهادهای فرادولتی؛ انتقادهای یک کارشناس اقتصادی از پدیده‌هایی که به گرانی ختم می‌شوند
/ تلویزیون اینترنتی مدار
بردار را در لینک زیر تماشا کنید
👇
https://www.aparat.com/v/zkahcd7
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/680273" target="_blank">📅 13:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680272">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d533c4997.mp4?token=g7XvF5zWJMeVvmgd5M5HNOK_RorjuyxSgo0QNGXm6a14b_KtL8D-uIjMfu8P7qdS9LVhVrzqSLF2YiFh7UMYpOyicYyjBLQkngG1yiux2zZ3sVb22_Rli4EGM_g5I4s94oQ53fHbc4Uz_EKjEwN5_bOOKLsgc9C3wr4LNeQUN6w0xd-ecJ0QYq30aqNrh6THX01kS_3zlOb0b4aguvV5WkEQpuTKExFtag0qlwYH4bgEe7vxPoH24MTAvUA741ZqWTf5H_6H03sZRmfrCTOxWdaGmUqnWzHyOGnarNOSut17Me3zweDrAJAB0omVmQhZ_ciiZ7s5UFMeeNQZGge9UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d533c4997.mp4?token=g7XvF5zWJMeVvmgd5M5HNOK_RorjuyxSgo0QNGXm6a14b_KtL8D-uIjMfu8P7qdS9LVhVrzqSLF2YiFh7UMYpOyicYyjBLQkngG1yiux2zZ3sVb22_Rli4EGM_g5I4s94oQ53fHbc4Uz_EKjEwN5_bOOKLsgc9C3wr4LNeQUN6w0xd-ecJ0QYq30aqNrh6THX01kS_3zlOb0b4aguvV5WkEQpuTKExFtag0qlwYH4bgEe7vxPoH24MTAvUA741ZqWTf5H_6H03sZRmfrCTOxWdaGmUqnWzHyOGnarNOSut17Me3zweDrAJAB0omVmQhZ_ciiZ7s5UFMeeNQZGge9UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دادستان قشم فرمان مهار فوری آلودگی نفتی سواحل جزیره را صادر کرد
🔹
دادستان عمومی و انقلاب شهرستان قشم با ورود فوری به موضوع آلودگی نفتی مشاهده‌شده در بخش‌هایی از سواحل این جزیره، دستگاه‌های مسئول را مکلف کرد ضمن شناسایی منشأ آلودگی، عملیات مهار، جمع‌آوری و پاک‌سازی نوار ساحلی را بدون وقفه در دستور کار قرار دهند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/680272" target="_blank">📅 13:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680271">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f436d1830.mp4?token=VYcSjVj8bLzPW-tEGKP7wUN6OodMZzw-GCeXMM0jephg_N9RhaglkpIhhBJ-hdfBfh8zc7SEkflK6azkXKGVsMPsYZehQlTHlEd_B3yhpOzXvnKkj_kT9y7Mya-93qou6hqrOTPR_SlGr0KMEysrIwAnDYG-8za0pRTWMXCMlRS7kNLupCAELjzdwOhVXukfRA9PyjCal84rDCp-q0gOMco1qNOsMdaLO4aQ75GLkuTKLe_Vr140QMtZf0jU-FPyHqmvn6JKXOa-YZpTzgdR9VHBUZPGyU7uNuH8l8MienXXyXvukr9VV0AEApV_7itI3Khpm4SmA3Kq_iFCi8zOYDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f436d1830.mp4?token=VYcSjVj8bLzPW-tEGKP7wUN6OodMZzw-GCeXMM0jephg_N9RhaglkpIhhBJ-hdfBfh8zc7SEkflK6azkXKGVsMPsYZehQlTHlEd_B3yhpOzXvnKkj_kT9y7Mya-93qou6hqrOTPR_SlGr0KMEysrIwAnDYG-8za0pRTWMXCMlRS7kNLupCAELjzdwOhVXukfRA9PyjCal84rDCp-q0gOMco1qNOsMdaLO4aQ75GLkuTKLe_Vr140QMtZf0jU-FPyHqmvn6JKXOa-YZpTzgdR9VHBUZPGyU7uNuH8l8MienXXyXvukr9VV0AEApV_7itI3Khpm4SmA3Kq_iFCi8zOYDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واشنگتن پست: ترامپ در ترکیه از ترس ایران با کامیون آشغال جا به جا شد  واشنگتن‌پست:
🔹
دونالد ترامپ، پس از حضور در اجلاس ماه گذشته ناتو در آنکارا از ترس تهدید ایران، به صورت مخفیانه با یک هواپیمای نظامی جایگزین از ترکیه خارج شد.
🔹
طبق گزارش واشنگتن پست، ترامپ…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/680271" target="_blank">📅 13:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680266">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06149768b.mp4?token=LafomNVI30DPKSYiMPLXZ2InOdlKicO9-WjSzvjqpzVyiEpasUnEFRdh4GSeJPYe09a8mPTKjuQsoIIlBsEji89-2p1_nJOhKGMUbL3p5gIhAKPslk8NqwVXWcpLDMOC8s9jvBFr2paXgr0ShOdHusHrjZnCwnwEQk59nz7i29eoB4MKABd65otubuLw51NEUDVBaciijQD-RkMEo2vMir1Q93Dera07ib6fPLzON3mL3aJBpwQW3mUUQX9YV2tvV5lf0KasVM4pQMoqCCyi3TP4NQUoeKPd878BdZyWxM-TKWiFivLq-p4j4-Zw8v5Bme2nre8b3Eg3J93dr6MDhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06149768b.mp4?token=LafomNVI30DPKSYiMPLXZ2InOdlKicO9-WjSzvjqpzVyiEpasUnEFRdh4GSeJPYe09a8mPTKjuQsoIIlBsEji89-2p1_nJOhKGMUbL3p5gIhAKPslk8NqwVXWcpLDMOC8s9jvBFr2paXgr0ShOdHusHrjZnCwnwEQk59nz7i29eoB4MKABd65otubuLw51NEUDVBaciijQD-RkMEo2vMir1Q93Dera07ib6fPLzON3mL3aJBpwQW3mUUQX9YV2tvV5lf0KasVM4pQMoqCCyi3TP4NQUoeKPd878BdZyWxM-TKWiFivLq-p4j4-Zw8v5Bme2nre8b3Eg3J93dr6MDhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضامن آهو؛ روایتی که هوش مصنوعی دوباره زنده کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/680266" target="_blank">📅 13:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680264">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmvASZvgROLuSd_PTMX-CFr_zf3duJ-7Yiim9nupFPJdAA27MoLxgtaU7gxRpfbBMPZrr_WGwSxWkeGO2NQEQg35bdcSHJU0qgIeMWA-8J3E0DFAE9N6Db9QcYyoalKt2zmk33yC43VuXrgpkqjeqK2LfL6yNbmfYnhLLyqT3cBgJ-ldhdDwhu0b0Ngfyn6BBFBwa9fo3kSjx1npDjHGcxc37Gmc95G0vArTmhhTVx8iwQoBTiq8Jj1tdHgQtA1bmqOa2N191zpNdbBxybnT7Uxer8Jycruaph9OT3oKpnoraQ--aw8DxtMlbsA9OTBXimHWkariicC5BJoUssXu2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش ۹۰ درصدی عبور نفت از تنگه هرمز
🔹
تولیدکنندگان انرژی در خلیج فارس بیشتر از قبل انتظار دارند که کنترل ایران بر تنگه هرمز، پایدار باشد.
🔹
عبور نفت از تنگه هرمز از ۲۰ میلیون بشکه در روز پیش از جنگ به ۲.۲ میلیون بشکه در روز در هفته گذشته کاهش یافته است.
@amarfact</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/680264" target="_blank">📅 12:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680263">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9561845d9.mp4?token=KZ82a8OO1eIx5CIonYQOwz9cCvoAhDEdBaOfjQxywuWQt18KVxrtvRmsVTRav2jBdjlDqPS-EOJmET-owcH8j2A6IN3BDSigg-WPv2y3LdjCRrc0sz6i6LgPU-fIIBvEcOLtW36Z0KDHoLCrZfp8mSCDPUjY3oA3Hv3xT6O8BLSUpW_a4Ozvgp4aJVR4miQ2gXT3eF26JScX24MP9mXZGjPxroUMMpQrJWQgNJ1yEJgT60hIsJVQpubXmQNtjD4iVXhSHcMpvS2B-j9Ld_UQhvTPJOrmo86jMBgEIoQWitw1O636haCo0gFEjtRA6Lmrof0MFIm0ykx7Yaa1i2kCNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9561845d9.mp4?token=KZ82a8OO1eIx5CIonYQOwz9cCvoAhDEdBaOfjQxywuWQt18KVxrtvRmsVTRav2jBdjlDqPS-EOJmET-owcH8j2A6IN3BDSigg-WPv2y3LdjCRrc0sz6i6LgPU-fIIBvEcOLtW36Z0KDHoLCrZfp8mSCDPUjY3oA3Hv3xT6O8BLSUpW_a4Ozvgp4aJVR4miQ2gXT3eF26JScX24MP9mXZGjPxroUMMpQrJWQgNJ1yEJgT60hIsJVQpubXmQNtjD4iVXhSHcMpvS2B-j9Ld_UQhvTPJOrmo86jMBgEIoQWitw1O636haCo0gFEjtRA6Lmrof0MFIm0ykx7Yaa1i2kCNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آپشن‌های ماشین‌های چینی تمومی ندارن
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/680263" target="_blank">📅 12:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680261">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEx41BSC9998ltvsvim5XrwgxEj8kKQGPRe4M6r5VUyMy94zvvQWNuEHQFWqirmHWPVQa563vpRVJDp6GAOMIkSwl7GmCg3eAb1bDUG26EzfPAdyzerTvVvqda1JXnab7UhdyRwqf767zAdDwRKWWg4JbyzFow6UhnkjOJuP2n6yvr6j5cjqsmTlIFSaac_zXu44yWGk6f1IXMxUVA6TAY6LgbLARYkS3YnIGd3MKq9j_PEhm3278Ej121LwCJo7k3ZJWB9CsdHq0LT_n1DVFSgFqJSyj1xhl5fis7menwUYmFYSYqzGfo5aJJRgjyHd2exMyXLkAVKQWsxphI4v0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همراه اول پیشتاز توسعه زیرساخت هوش مصنوعی
🔹
پایگاه خبری رویداد ۲۴ در گزارشی با اشاره به نیازهای زیرساختی هوش مصنوعی نوشت که آینده این فناوری برخلاف تصور عموم تنها در مراکز داده یا مدل‌های پیشرفته ساخته نمی‌شود و به شبکه‌های ارتباطی قدرتمندی وابسته است که داده‌ها را میان میلیاردها دستگاه هوشمند جابه‌جا می‌کنند.
🔹
بر اساس این گزارش، بانک جهانی چارچوبی با عنوان «4Cs» را معرفی کرده که شامل چهار ستون اصلی «اتصال»، «توان پردازشی»، «زمینه» و «شایستگی» است. اهمیت بخش «اتصال» در آمار کشور ما نیز نمایان است؛ جایی که تعداد کاربران فعال 5G همراه اول به ۴.۴۴ میلیون نفر رسیده و ترافیک روزانه داده در شبکه آن از مرز ۳۸ پتابایت عبور کرده است.
🔹
این گزارش تاکید می‌کند که ضعف در شبکه‌های ارتباطی می‌تواند ظرفیت کشورها را در بهره‌گیری از هوش مصنوعی به شدت محدود کند؛ بنابراین توسعه نسل‌های جدید ارتباطی، پیش‌نیاز اصلی برای ورود موفق به عصر فناوری‌های آینده است.
لینک گزارش:
https://www.rouydad24.ir/fa/news/465938
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/680261" target="_blank">📅 12:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680257">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ac9d060fb.mp4?token=pxgz9BZOdJ6XbVY7eAsOyxLVoB4Y6R5bzw2IGeqZWkZRP5k8DCBb2zHq0-CXCsHyRFzfrBdxAfnyVIbl8UxmrXdv7BSUNYi1eocDMwviC5i8a9JodUtreazh72BvccDKkb73IXA7IfimnHPo-dKZBmduAhv1FIL9liLBeZxd8L42Leunu99XX9xreh2mkO0Xj2isbI8_Wexwm7De6xhFs_2HzTmj8s8nC4ERAVvRkMwME3DujWn6wTvD6j6JeEUre_djB2mxrsr-WlwGB8-zQLTNRSHzG-zd5wF3th9GZlR1AaV7rh1ZnR4QI3_NiwGIwiMdr65verhNZBDzWT8FAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ac9d060fb.mp4?token=pxgz9BZOdJ6XbVY7eAsOyxLVoB4Y6R5bzw2IGeqZWkZRP5k8DCBb2zHq0-CXCsHyRFzfrBdxAfnyVIbl8UxmrXdv7BSUNYi1eocDMwviC5i8a9JodUtreazh72BvccDKkb73IXA7IfimnHPo-dKZBmduAhv1FIL9liLBeZxd8L42Leunu99XX9xreh2mkO0Xj2isbI8_Wexwm7De6xhFs_2HzTmj8s8nC4ERAVvRkMwME3DujWn6wTvD6j6JeEUre_djB2mxrsr-WlwGB8-zQLTNRSHzG-zd5wF3th9GZlR1AaV7rh1ZnR4QI3_NiwGIwiMdr65verhNZBDzWT8FAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ، آخر هفته در زمین گلف خود در بدمینستر، در کنار یک سامانه پدافند هوایی کوتاه‌برد AN/TWQ-۱ اونجر (SHORAD)، گلف بازی کرد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/680257" target="_blank">📅 12:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680255">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
اتومبیل کایزر دراگون؛ خودروی کمیاب ۱۹۵۳
🔹
اتومبیل کایزر دراگون (اژدها) در سال ۱۹۵۳ تولید شد و تنها ۱۲۰۰ دستگاه از آن ساخته شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/680255" target="_blank">📅 12:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680254">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52844ba385.mp4?token=tOk593Bsj1rZm-kjxpiKwixwk4MJgQRPnp-COIAAITyrUH-poOOG6YQ_1np5dGVDXsbO70r-EE2vETpwJH1i1o64wKveEZ_58aOwI2ER5tTWrw3TcVNF7i8qF65269qnk-is7oEaT3ida800kNbp8VHFplDX4lyfxDAfA1XnzqV3BgwWJD4eGzkWX5Q8-a38sH83v_CNwfEO4DTNPTW9vbDUy_ibkVjDPDbrRGtYBNwutSV91PsitcWdsE5kSUPG8fWogoeCyOQsJNDTlvCoXTGXmg8M77FxBWIlRY1LJ0XBA5_3RnQuHEZaw0bGMeC0Yrkm7lzFFq9u6mfWTM10GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52844ba385.mp4?token=tOk593Bsj1rZm-kjxpiKwixwk4MJgQRPnp-COIAAITyrUH-poOOG6YQ_1np5dGVDXsbO70r-EE2vETpwJH1i1o64wKveEZ_58aOwI2ER5tTWrw3TcVNF7i8qF65269qnk-is7oEaT3ida800kNbp8VHFplDX4lyfxDAfA1XnzqV3BgwWJD4eGzkWX5Q8-a38sH83v_CNwfEO4DTNPTW9vbDUy_ibkVjDPDbrRGtYBNwutSV91PsitcWdsE5kSUPG8fWogoeCyOQsJNDTlvCoXTGXmg8M77FxBWIlRY1LJ0XBA5_3RnQuHEZaw0bGMeC0Yrkm7lzFFq9u6mfWTM10GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعضی پنیک‌ها خاموشن و هیچ علامتی ندارن، اما می‌تونن از درون آدم رو‌ مورد حمله قرار بدن #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/680254" target="_blank">📅 12:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680253">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQQm2pFdvoVLAdSXD83nDPbyQjdpch4T7e9STVvPn1xkur4bx5S-u5h0-0ZsfHJdUH0NMf2l5o8VJJZK2-9tjW-Z1bc17esW38eQrSONUr3ZfWcJ3cQtkJIuEuaJC3TJNjtdLV2i87cCIYp0XVp_1ZN7UvNNaUuxDQlDhkfpReUREMQFS18R9QLqCU7GWXlAoR5yqXLFMykI0-GKqK5x9kBvWeRk5YflI8M2sr9N1WewUeUdkbYqFsNZiAk8NbF89hfQiW89pzxVslbYJAMcV8P137p5r-6zhaf1YaIoVbNcXxcFujmZqq2ERisxeIXoEtslZZ1SntC0T6jU-Sps6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون قرعه کشی، 50 دلار برنده شو
🎉
۵۰ تتر سرمایه معاملاتی، برای کاربران جدید ورسلند که باهاش می‌تونی  ترید کنی و سودش رو برداشت کنی
💸
🔻
فقط کافیه ثبت نامت رو تکمیل کنی و به صورت آنی، 50 تتر رو دریافت کنی
🔸
بدون قرعه‌کشی
🔸
بدون واریز اولیه
همین الان ثبت نام کن و از 50 دلارت استفاده کن
👇
🔗
ثبت نام در 5 دقیقه
🆔
https://t.me/versland_io
🆔
https://t.me/versland_io</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/680253" target="_blank">📅 12:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680252">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k54aBWs5Gac2JL2Q4AH_5TcsOIhRG8p93fkf3gVFSaVKWiFmN95ndQbRbTDzCYWuM0KjhWWv4Vm2Dv4t3X-P7dX02oP87q4qM4DNR5FXR2SGNoUEr6KxTieNdHHgARXFxV67t0K85bOBeR8S34wuZRNNQOiwP5NfAEzTio-aXQ4MClsVunbTdNi6ILK1i7TwYfmgv3cktu2s7SfDhdLkeWVErsyxinpj6OVhQ2Eb-P1vPbvv49OdyaAJ5fOetV_A2VvpIk4jalYO9jt8-dvi85_2cTunGei0yrMBt3MxUeUwuC4ekh8Z4KxOy2fUoUnlaGqm74YCdf46K_gNbM2G9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بشار اسد به اعدام محکوم شد
🔹
دادگاه جنایی دمشق بشار اسد رییس جمهوری سابق را به صورت غیابی به اعدام محکوم کرد‌.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/680252" target="_blank">📅 11:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680246">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RykvMyrkPQRpvOPqxnddRxNOQi3hsvw_l-qYHvE_6GtVaYKghW1egUw7QX-_mJ9-Qj0rdABKJwTy5cAVL_1BkHKlzWd8H3dD5YDxb_2vemQK_G-2mU90o5mXf0pJNaf418sSS_6uQZbZdGI5k--CV8gVZJ-JKfSjmcGqfXCHYbL-7WMQpRLSS6Yh-_GyYg7cYbkfr_WJaCcG611Tu-4g0HpcN9C6sH-yFyp41uPQjNOEIVu26aEaVT1nOEbixUmcTU9IqJs6H4KQkLAXX5KRO6Rew3SlfXWU0UnkDp1pk04B9G-eetfgJmfNKoWAfbKQX3LZ_Azx-rT7339_FzbriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FRHs8ZMTVyzTtIMUfOIf-CD1QoX8iGrZBAk0QEZglZq09qpnJ0GG3xW-2Ez_NhKWvvCHX7tK2k-4r6yzNQmIlD-1-M2VcwEvl51s6yPmcfGet_E47HhhDaeETEMsdz6pFzzPbxXhibMaZgfsjst3uM5tl9CP0oLuFLw1r1DdEc7M4o8HXAypVmHJRxAhmJYS9l4rPLNchtiGCVIqxVCWChqhodOiSHhaUaxqgYeFl5s0EOSyAAa2ANtGAMOXQghQ3M1-u7bN9rv2TYn__fP-l1_Nsda8Dwb6gdcXCuHW3kWzqa4Q3RMSQnPQ52dzFkRIOSorDSP2szxv5cZuSGH6rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVzczK5e9mjIwi20UNsKISMFA_b4lCWOj3NcAte5YgEhfxhKbp7Fdu062LYqFmjNhMHtN_GBGlMvN3pD3WSyhfZEd-kbNEvm08ogQowjpxo3OllD7QOCVtjaTcO4A9j-NCebA2mEYs2CI619r0v2J8OpTPsrl6nc65HNkI14MZ0Fen1vvi3FFAfZ7DyjPQbLiWpZcpybQGlQiUgi0FInTHrc1Le6LJdVenQHQkGr3rTSveqcoCUHVl4Wdd7eBwJJuNwYA12yyGQNzW4aDRJMG1CebUZ7IDMYhDezWaNo1Nuziuqfsq6y-BS3Wyl0lhD-ndYjZO_DLOaovmuGEaqM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDqCPpLfOXPf04QY8gVc5NUlhQlS99hQyjWWDeoHyO9RSdzJ_6us8LzRWNeU7cbKu7M-JChx6O82xVvpeS6iB6DPMBA1Nq9hByYr8yys1-6AlXqTa_YS0yILV4817YcsdFGJn6BPOJsMZQWdXLwnxM4l2fUj7CSd-XvLFP4Ez8Lu46VWSdBCp77cuTEdUxSOZf6abEKsqaV8NFqkEzoEQ00oQTmKnvpy1UfHbCnd2MMKkLEGxmqhrdgMhUL-X7jhZQ-sXd6axQmIre76hRjHWX5mhZutPTGovpT9-xNuCQrYgbLHJJp3tMUNne1CCG5MP-MYc5GzVqSxxcG619dsJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گوشی‌های جدید سامسونگ وارد ایران شدند
🔹
گلکسی زد فولد ۸ اولترا (Galaxy Z Fold 8 Ultra) با حافظه ۲۵۶ گیگابایت و رم ۱۲ گیگابایت که جزو گران‌ترین‌ها به حساب میاد، حدود ۴۳۷ میلیون تومان قیمت دارد.
🔹
ارزان‌ترین سری هم، گلکسی زد فلیپ ۸ (Galaxy Z Flip 8) با رم ۱۲ گیگابایت و حافظه ۲۵۶ گیگابایت، از حدود ۳۰۰ میلیون تومان شروع می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/680246" target="_blank">📅 11:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680243">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVIG8JLScQMZK1uoTQ-gV_G5VTb-rEFQw38hW8wM3ENB6SQDOKlVP1CX7icFnAFPEDnLj2lfWnPYSKW5SNKKr-W9pKklF1BKKMsUqLGHu7OMFV9_f2BLlYt5QEocIuEXBitxvvtHA7GA3-waBT8DiaUB3IE15agCKUkdEgxehiN1X9cj49o7Y0s3EAbB79d-m3AvefjNSRDrA0OsZmkxcDmE8G4Sat44cEml3lH676VDrWQj-Y9D4lkHGP_f2DTnP86HRSktO7gBxSuEFzV0kSKfERfxJc2j-rbS3H8MO75IcAsIM0wv0fVDyOodEHOOzJo5jWxpqboLTCPkEcMjfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری زیبا از سقف عمارت هشت بهشت اصفهان
🔹
علی آذر
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/680243" target="_blank">📅 11:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680242">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358c82a18f.mp4?token=VVgZPkcg7w45STrPnUiTEvi_bvpLVW235AcsWfXQlAs67wZ51b8taDOKgUqkZFsC_Yy-6pfoZxQsFHqqOmRVv173Pxh6vc6JBolFbLIj_Zd9RiAo6uSwUbiKzRq-zvL7jODocE3HIjVUQwXRrgNT-L8Aa-Cpd0aMBv7gztQKsaWFiFFb1IGEeahcZbRceMpdom1uqRYmPEOZkn5r_bj-44kL_Y_pq64h0gIecyf8WYLndGHueiMg7im3Lnf2moYOWFYAYi2_n9Pq0mwQ6LclitTFvgc_omIyraLqsbx4NySshOflw8eVSu_TeoT81_L3rJrK53Gvw3b_p-uJsJUMYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358c82a18f.mp4?token=VVgZPkcg7w45STrPnUiTEvi_bvpLVW235AcsWfXQlAs67wZ51b8taDOKgUqkZFsC_Yy-6pfoZxQsFHqqOmRVv173Pxh6vc6JBolFbLIj_Zd9RiAo6uSwUbiKzRq-zvL7jODocE3HIjVUQwXRrgNT-L8Aa-Cpd0aMBv7gztQKsaWFiFFb1IGEeahcZbRceMpdom1uqRYmPEOZkn5r_bj-44kL_Y_pq64h0gIecyf8WYLndGHueiMg7im3Lnf2moYOWFYAYi2_n9Pq0mwQ6LclitTFvgc_omIyraLqsbx4NySshOflw8eVSu_TeoT81_L3rJrK53Gvw3b_p-uJsJUMYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طلا چطور جورکش ریال شد؟
🔹
وقتی ارزش ریال پایین می‌آید، پول مردم کجا می‌رود؟
🔹
مهرک محمودی و ملینا جعفری از تحریریه ماهنامه پیوست برای آرش برهمند از عددهای بالای تسویه و برداشت در پلتفرم‌های آنلاین طلا، از جمله طلاین، می‌گویند؛ عددهایی که می‌توانند نشانه‌ای از تلاش مردم برای حفظ و مدیریت سرمایه شخصی در روزهای بی‌ثبات ریال باشند.
🔹
اما یک سؤال مهم‌تر هم هست: وقتی طلا از گاوصندوق و طلافروشی به موبایل ما آمده، آیا فقط شکل پس‌انداز عوض شده یا بخشی از کارکرد پول هم دارد به پلتفرم‌های طلا منتقل می‌شود؟
🔹
روایت «پیوست هفته» از بازاری که این روزها طلا در آن فقط یک کالای سرمایه‌ای نیست؛ گاهی باید جور ریال را هم بکشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/680242" target="_blank">📅 11:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680241">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: تورم در بسیاری از استان‌ها، ۱۰۰ درصد است/ فکر می‌کنند با اعلام آمارها، فضای روانی جامعه آشفته می‌شود
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
دستگاه اقتصادی ما نتوانسته کارش را خوب انجام بدهد. همه گرانی‌ها ناشی از جنگ نیست، خیلی از آنها ناشی از سوءمدیریت است.
🔹
رییس اتاق اصناف کشور روایت می‌کرد که همزمان که یک کالا از یک زنجیره به زنجیره دیگر انتقال داده می‌شود، یک فاکتور الکترونیک می‌دهند و یک مبلغ دیگر در کنار آن ردوبدل می‌شود؛ این بدان معنی است که رانت و فساد انجام می‌شود.
🔹
مردم از ما بیشتر می‌فهمند و می‌دانند و راهکار این نیست که پنهان کاری کنیم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/680241" target="_blank">📅 11:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680237">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eee2a327f6.mp4?token=J0xPa9oBDMXEKZJt9kLwJ8k1Hb5Rk3NXoJunguXVVDrS3Z1nMT70IWJVHgIUU1XLO0mfd06UsYlMqMiPhoOvyhGiB7WVOJSKAC72KBU4LnaTB0Z6QoTg-x2YEAOK-hRcinbOPcyPwWvta1272divphT2kquEc4slTYLFInL0ESA2nErvAyfUbRGLtTgkXs3kgeCId3_4xCS2RECHiM0sSmhrJZ1STHOy3dBJpyKyFOaa56WGnrIe2t-DeR8nuu4E9D_MtY3dsnFOdkISE3WcSr4gpkoQcGoySRooLK_EXxkvsXVMYCdI7l_wf3RxZarXs9TyRM4mayTnW_cNl9GbFA3qe_axMpabqzQxawzpOCQ1KqDJXA_ULi6AAguaE3xS5pfmGs8J8WekYeU1M9b_WEYGlrudMEzgQZy9DfeoPIYpzaCqhjrfhQXymhuhpkcfLy_vrtlkCZ11BgQr_q9HdeNTWh1oVL_BFKbB24hmNt2GRYqJNCh1IQKA_6T_DDX9c_b-5qr-PdJuf4W45BjkmAQJu1qYdp-Yt5ezi0iRYpUwOZho2oVnjP95LQdmAAulbUfiYOkET5bkVMHqCNbLZI2wuHFBlQWO60pod6SsFul9Pa-VsKw6cWM7oq2jqzeCqsjgQnR31Um4kHWkowFLZ7PbWsCinmIEwu01WgUWY0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eee2a327f6.mp4?token=J0xPa9oBDMXEKZJt9kLwJ8k1Hb5Rk3NXoJunguXVVDrS3Z1nMT70IWJVHgIUU1XLO0mfd06UsYlMqMiPhoOvyhGiB7WVOJSKAC72KBU4LnaTB0Z6QoTg-x2YEAOK-hRcinbOPcyPwWvta1272divphT2kquEc4slTYLFInL0ESA2nErvAyfUbRGLtTgkXs3kgeCId3_4xCS2RECHiM0sSmhrJZ1STHOy3dBJpyKyFOaa56WGnrIe2t-DeR8nuu4E9D_MtY3dsnFOdkISE3WcSr4gpkoQcGoySRooLK_EXxkvsXVMYCdI7l_wf3RxZarXs9TyRM4mayTnW_cNl9GbFA3qe_axMpabqzQxawzpOCQ1KqDJXA_ULi6AAguaE3xS5pfmGs8J8WekYeU1M9b_WEYGlrudMEzgQZy9DfeoPIYpzaCqhjrfhQXymhuhpkcfLy_vrtlkCZ11BgQr_q9HdeNTWh1oVL_BFKbB24hmNt2GRYqJNCh1IQKA_6T_DDX9c_b-5qr-PdJuf4W45BjkmAQJu1qYdp-Yt5ezi0iRYpUwOZho2oVnjP95LQdmAAulbUfiYOkET5bkVMHqCNbLZI2wuHFBlQWO60pod6SsFul9Pa-VsKw6cWM7oq2jqzeCqsjgQnR31Um4kHWkowFLZ7PbWsCinmIEwu01WgUWY0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گروگان‌گیری در پایتخت
🔹
صبح امروز در پی اعلام یک مورد گروگانگیری در خیابان ولیعصر، بالاتر از پارک ساعی، موضوع از طریق مرکز فوریت‌های پلیسی ۱۱۰ به پلیس گزارش شد.
🔹
در پی این گزارش، تیم‌های تخصصی رهایی گروگان، سرکلانتری و سایر نیروهای انتظامی در محل حاضر شدند…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/680237" target="_blank">📅 11:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680236">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4979d719f8.mp4?token=c3LtkRv3JNhuRFgtrFjtQMPQBXGIC93hJIp5r1EmfzmhBVdvINAW-RiB-T-_BJ9anSNHHfSr8c7EZrsE5EgcLjl33HLklv9C4xiCXFe4fOQWonGgcFLQQ71osKirwjrCugyEzDLYeHr5lIuqmI501CodtQi24ew-Qr3PSIPn7yFwMld87DXkqLt_kccAaZUiGNXtR_oymiXMOj9N9uHWI4XdPrWsSfs1wMa_bwO6efD-aSxSoPB-betXHGDMaIUYOCyljV_bWdHepe_X4VmXtBgCJUxqqLP45orf5EFeA1q-YYz_q9hkMf3plchHwmsRLp95zqdU8aKhBGpykSXFkUQgCdMLa7234-O_4ij1yDVKY4AbmDBvb2zle77iAeH6Hcf65JNiL34MS9hrK1Cb5zGAbKYd1ltvJIfbbNQ4h7M3iqU1Vodknq6v335XFq_zfaq7ykrMxiZ3YWltTsEr0dipuXH6xZ3V7KZNSugqMKZxn5-2wUrLTGl0Ms2JjSNtxDj1iCUWHPJtRI00Ja1lUxJUfe4_N3QBcKhPAyjrmTzsfZb-hPjdsURtTwlytrnYgoa9kh1ePH8kXACMGfRObdp83cB9d4_VRTFgHoMKkrauCfYVAsiYOrBQQvtSh7EE5Xf2D9riTh2q_RAGi3mcxGIj2N9FxlBpv6OW9QQftiM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4979d719f8.mp4?token=c3LtkRv3JNhuRFgtrFjtQMPQBXGIC93hJIp5r1EmfzmhBVdvINAW-RiB-T-_BJ9anSNHHfSr8c7EZrsE5EgcLjl33HLklv9C4xiCXFe4fOQWonGgcFLQQ71osKirwjrCugyEzDLYeHr5lIuqmI501CodtQi24ew-Qr3PSIPn7yFwMld87DXkqLt_kccAaZUiGNXtR_oymiXMOj9N9uHWI4XdPrWsSfs1wMa_bwO6efD-aSxSoPB-betXHGDMaIUYOCyljV_bWdHepe_X4VmXtBgCJUxqqLP45orf5EFeA1q-YYz_q9hkMf3plchHwmsRLp95zqdU8aKhBGpykSXFkUQgCdMLa7234-O_4ij1yDVKY4AbmDBvb2zle77iAeH6Hcf65JNiL34MS9hrK1Cb5zGAbKYd1ltvJIfbbNQ4h7M3iqU1Vodknq6v335XFq_zfaq7ykrMxiZ3YWltTsEr0dipuXH6xZ3V7KZNSugqMKZxn5-2wUrLTGl0Ms2JjSNtxDj1iCUWHPJtRI00Ja1lUxJUfe4_N3QBcKhPAyjrmTzsfZb-hPjdsURtTwlytrnYgoa9kh1ePH8kXACMGfRObdp83cB9d4_VRTFgHoMKkrauCfYVAsiYOrBQQvtSh7EE5Xf2D9riTh2q_RAGi3mcxGIj2N9FxlBpv6OW9QQftiM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ کمبود مهمات آمریکا را گردن بایدن انداخت
ترامپ شیاد: بایدن با ارسال مهمات به اوکراین، ذخایر آمریکا را کاهش داد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/680236" target="_blank">📅 11:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680235">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a073856ca.mp4?token=Ytc50QqSvvv0jEQBdskVG9Q1Um4KEBYs8gHnF4Gz3mPYciRourVPO8fv8hXHMW0Nd6bvqggJtyD6jQnXmfM7N5lgXUBMlqE53MErf5htZtnB-DQdZpEbNwJhV2ZjOcJ1ssWWjOcIKKmPbYfMD-g01X41gVAsr_txz1oUkpYwnS4aNicV40MgNKh7yC4fTLgmqKu4XsnVkbaAJLEQxlM6KRK7TnYWWLHTMWjwuS9DCDMYj0JWO_xkGAKaR_-qZyI42nlM6m-P2W6VXFd3o_tR9bpTs67zAyEKu8AGl4xaw_v0ViFxLaVTTBkPzRWE1MoqCfIhahEgT9rSovzi26FxFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a073856ca.mp4?token=Ytc50QqSvvv0jEQBdskVG9Q1Um4KEBYs8gHnF4Gz3mPYciRourVPO8fv8hXHMW0Nd6bvqggJtyD6jQnXmfM7N5lgXUBMlqE53MErf5htZtnB-DQdZpEbNwJhV2ZjOcJ1ssWWjOcIKKmPbYfMD-g01X41gVAsr_txz1oUkpYwnS4aNicV40MgNKh7yC4fTLgmqKu4XsnVkbaAJLEQxlM6KRK7TnYWWLHTMWjwuS9DCDMYj0JWO_xkGAKaR_-qZyI42nlM6m-P2W6VXFd3o_tR9bpTs67zAyEKu8AGl4xaw_v0ViFxLaVTTBkPzRWE1MoqCfIhahEgT9rSovzi26FxFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هانتر بایدن: نتانیاهو تجسم شرارت است، دیگر نمی‌دانم به مردم چه بگویم
پسر رییس جمهور سابق آمریکا:
🔹
واقعاً چشمانتان را باز کنید. برای یک دقیقه قلبتان را باز کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/680235" target="_blank">📅 11:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680230">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vEJfLubjWESKU_7yjZGkalWn0CgjjjuxIPhPWeqX9bus17IyYrD5__oGk2a9isYmHakblBvREtCCFeo7aXA1fItEv38A7IJN3B8CYi3y3ggKyAtYSVoWKe3nfo384vneBVPhQRg0k6sqo7A2AwU7addQomCucOSXA47f7b1uX1ObEPzin2k3kRQWKqgBjgVrfdx60JJ8E6NhpxH1XdYAAAvUF1avz6NVJXIxZI39ihsdX4ho8Q3YCjaiAr5Fvw54ND8s08TdIuCmTsXuktyIkOx98yYNBXGQtqpBmWiYQ_OlmPjHV1mvGXJCO4FR-EaS4c_-mGBCLzMIHq__vhtpBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sskarh59K3_S3UIgxcX8qEoWmfi-eNwBsTl9j6xy-CTZfu6faA_aSH_v26_v80ZHAAVCmUB1t926f-tpgUpYDjslrZRO-I0JdzzDZAkK45LKpOSPTj6KF3G7ifOyFjvJjl9iBclwg5YJMoHUmypMKrwIkke-BxP6eXxn8q4t6Zg3-FQpvF9SSAcRRPTjpVLbAYp_Eny0Y7rrQagFeoxvAg7z6D-jaw90fIfvf3B4Wp6spt76QMtgvbe-1hsYqnVkiESBOfKpXaaiXU11DV9USaieJ8UjQfZLCidr1o5dsLfyixcVlYA88nFMZljEFdfuzL4rBKIEdYUHIN1YFsFtuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ghPdmmK6_miedAEaeteaNqEN3WoTQrqZJtvy12OUYJaB4cphSiTbdjxQLmsyV4IgNlbWsRE3aWcRnjYY3gVRyMqvR3db1QFSzEXmi7WzlMCxz8tgVTMkANYYWMKOed4-xvwQmrTogKqpG7WioK6HU_SWgaSF7Ax2kMKhEL3uxPUzu0MV7XwT42EZqlL2okGhf6G7HLZWzBntnDldUOa5hsQJdZHjlUG3k-NoRsLxNbPfL65oTAW2AgdgssihJmGz6hyJ0xS3UFRBUa9sJy6GqqawlrToF0hMTcxdQmZNTmF5uam4TqDsfDo5I8G-d6MIr7Um7MV8Cv18zqYtkvRu-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از وضعیت تاسف‌بار بهداشتی در منطقه گردشگری دریاچه ارومیه
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/680230" target="_blank">📅 11:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680228">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
سخنگوی کمیسیون انرژی: افزایش قیمت بنزین منتفی است/ حذف کارت‌های سوخت آزاد جایگاه‌داران
سخنگوی کمیسیون انرژی مجلس:
🔹
حذف کارت‌های سوخت آزاد جایگاه‌داران به صورت پایلوت در استان کرمان آغاز خواهد شد.
🔹
براین اساس، سهمیه کارت‌های آزاد به سهمیه کارت‌های سوخت شخصی افراد منتقل می‌شود تا ضمن جلوگیری از قاچاق؛ توزیع سوخت به شکل عادلانه‌تری صورت گیرد.
🔹
برای مصرف‌کنندگانی که نیازمند سوخت بیشتری هستند نیز تمهیدات ویژه‌ای در نظر گرفته شده که به‌زودی توسط دولت اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/680228" target="_blank">📅 10:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680227">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz_8dSbcvQSHoFO6B1F1FxVd987BT2CZ-qNCkuLMb4HpLSmdiDwv3VqDMSv2r43qDGMTLP_v0k13NYdE2aZlQCRWmP3dNujenJdpFaYqD4uAVPNyR8rMrzaW9iR8CjGO44N58vS6ei3YzqCKiG-l4A5fuLEXScF11zcu_Mqp0dwN4OVT3a6snZF-0T4O2zHQXmGvIVz1vyeN0OD_eGxG-yYFyADsHsiIVXCVAqpMYSU0sdjAlZWrF5BpSdLBQkGLYaUH5hz4n_8TfsvpK23SwbpziWUAiydSxQnVmN1CCXeADFr1aOalevOZWCRQI-OEX4j7LRDY7HJdfTBx1t-8Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت سالروز شهادت امام رضا (ع)؛ حاجت روا
🔹
همراهان گرامی خبرفوری؛ برای شرکت در این پویش کافی‌ست یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کرده و از حاجت شیرینی که با عنایت و لطف امام رضا (ع) برآورده شده است، برایمان بگویید.
🔹
در ابتدای ویس، نام و شهر خود را بگویید و روایتگر کرامت و نگاه ویژه ضامن آهو در زندگی‌تان باشید.
🔸
صدای شما می‌تواند امیدبخش دل‌های بی‌قراری باشد که این روزها به سوی خراسان پر کشیده‌اند
👇
#حاجت_روا
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/680227" target="_blank">📅 10:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680225">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cea4e39ea.mp4?token=Vs1Up5uQFDNmf6PNJ54dUiZu4DHgCYhi6PeN0pO_9Az34I5ppeNNespAl60TzUdRgctvKJzIFLeTuk__CyN17cYvqpIsFktTNw9Yq6hstKS8_zUKqFIbm94q5cDcwqBI5tR3dT3tOvNMw0963SH-VbSB51UkiKxfoUTk1ji3iVi5K5hHMUhMsq00PMzg7zqkQd1CcXyktuX4LgmZNsntcus0hVzU2dn5IM1PJGP52-fvMWhRt4gu26zsw38RrtMVy6MAfxLHqO544HSqBoPib2276xh7oCNYZNgsGCSy4HGkphU9H6TcI9p3mWnPuKgcD4hRYlW6SCReR2OVQLb_ZzvEr69z-heSE1FqYHYTETG7Pe-m7J0FU4F4CNl6ZQtoEFo3jVIw3_pjWYc0WH4aqaP6Pb5z_QggKEiFPNMAVjwwPgdLO62C0OBlkAfpygat1afJGhAjhXWXP91F6TlZXjnjeQ927io8wqda82rzz8kje2CwX2T8xxam6aTmxKvRuwmzXaTPtsOplGEd51OrE5EEEZ5WRKjR0xZtPTQ_JgNsUibFJxt-Z90QHNgRbhivsACZgswRLuwH4CpKAquZNwWiXyp9n_yhD2lSj70vuuCTTwAnkRXDDWvJMKMQ4qDKYxu2ydbSYRjNJkQdY_Gj2le5Q6GUGukRtCZ3qFPERRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cea4e39ea.mp4?token=Vs1Up5uQFDNmf6PNJ54dUiZu4DHgCYhi6PeN0pO_9Az34I5ppeNNespAl60TzUdRgctvKJzIFLeTuk__CyN17cYvqpIsFktTNw9Yq6hstKS8_zUKqFIbm94q5cDcwqBI5tR3dT3tOvNMw0963SH-VbSB51UkiKxfoUTk1ji3iVi5K5hHMUhMsq00PMzg7zqkQd1CcXyktuX4LgmZNsntcus0hVzU2dn5IM1PJGP52-fvMWhRt4gu26zsw38RrtMVy6MAfxLHqO544HSqBoPib2276xh7oCNYZNgsGCSy4HGkphU9H6TcI9p3mWnPuKgcD4hRYlW6SCReR2OVQLb_ZzvEr69z-heSE1FqYHYTETG7Pe-m7J0FU4F4CNl6ZQtoEFo3jVIw3_pjWYc0WH4aqaP6Pb5z_QggKEiFPNMAVjwwPgdLO62C0OBlkAfpygat1afJGhAjhXWXP91F6TlZXjnjeQ927io8wqda82rzz8kje2CwX2T8xxam6aTmxKvRuwmzXaTPtsOplGEd51OrE5EEEZ5WRKjR0xZtPTQ_JgNsUibFJxt-Z90QHNgRbhivsACZgswRLuwH4CpKAquZNwWiXyp9n_yhD2lSj70vuuCTTwAnkRXDDWvJMKMQ4qDKYxu2ydbSYRjNJkQdY_Gj2le5Q6GUGukRtCZ3qFPERRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایرانی‌ها به هیچ عنوان بر سر تنگه هرمز امتیاز نخواهند داد
سردبیر وال استریت ژورنال:
🔹
گزینه نظامی در برابر ایران «غیرممکن» است. هیچ‌گونه فشار اقتصادی علیه ایران جواب نخواهد داد.
🔹
ایرانی‌ها به هیچ عنوان بر سر تنگه هرمز امتیاز نخواهند داد و آمریکا نیز تا حد زیادی موشک‌های خود را از دست داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/680225" target="_blank">📅 10:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680223">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9102b2c0e.mp4?token=uezXWYe7TUnKwt_jcdOIa-4_II4vhTgXyEGUWnylv01izmqnPGJE75tnwkIjU7sne-RHo91aZv3oRNgrmPEiCAsqHnkUQowWvQ-COHepz7GHX8A5_41ppx8W2LrKAqqnzV9-Gj0SGRZy9AzbeyEFnHlz_Sx8b_ZmI_hXDY70YkPjsQiowgv0b8rxutvuybeb_UKOluH_1Z2y4BJr_FR-04StvNZ8d6byS8rwCOjrqA2vcjpIH76FOmHFlb207nUQExOonGk7Rt5xZTGOUxUdtV7eyjevMjOkAqJNtx4_DOa1ZxXGd7yq80f_EEYe_os9wx7AUmvrSyZOidOkXFmvzFpEjrfgqjMJh2BUyl869DUktYb5BwqUGd4plSHiTvRU4vf1tXbWg4IBO0rq4LpfzBSlg4RsrbBZQ1576MiL7xNsK65d6mKvxxh3lTIyiW_NozNhonQL4mRJxm-N5P10jH2srbmnBVGKPyKekATHCjW9AckEGdhh30SR6Eb7NrAIklT8uiVsmuJIdPQubTr8Ym91uBIDTaFUI7LDwimnK4jQw2tcnvgfICSm1Ds9f3IUv8QtmoaqtF69YTcQE97fT94W42vfgAY6r4JZ_4kvbVYDmIxGAQEZsgUsra0KNB0WNi84qGcWb0dFH1h36OxHuxDtdTG-4r6GVseDlAp3s-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9102b2c0e.mp4?token=uezXWYe7TUnKwt_jcdOIa-4_II4vhTgXyEGUWnylv01izmqnPGJE75tnwkIjU7sne-RHo91aZv3oRNgrmPEiCAsqHnkUQowWvQ-COHepz7GHX8A5_41ppx8W2LrKAqqnzV9-Gj0SGRZy9AzbeyEFnHlz_Sx8b_ZmI_hXDY70YkPjsQiowgv0b8rxutvuybeb_UKOluH_1Z2y4BJr_FR-04StvNZ8d6byS8rwCOjrqA2vcjpIH76FOmHFlb207nUQExOonGk7Rt5xZTGOUxUdtV7eyjevMjOkAqJNtx4_DOa1ZxXGd7yq80f_EEYe_os9wx7AUmvrSyZOidOkXFmvzFpEjrfgqjMJh2BUyl869DUktYb5BwqUGd4plSHiTvRU4vf1tXbWg4IBO0rq4LpfzBSlg4RsrbBZQ1576MiL7xNsK65d6mKvxxh3lTIyiW_NozNhonQL4mRJxm-N5P10jH2srbmnBVGKPyKekATHCjW9AckEGdhh30SR6Eb7NrAIklT8uiVsmuJIdPQubTr8Ym91uBIDTaFUI7LDwimnK4jQw2tcnvgfICSm1Ds9f3IUv8QtmoaqtF69YTcQE97fT94W42vfgAY6r4JZ_4kvbVYDmIxGAQEZsgUsra0KNB0WNi84qGcWb0dFH1h36OxHuxDtdTG-4r6GVseDlAp3s-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک چین در هوا منفجر شد
🔹
جدیدترین موشک چین کمتر از ۹۰ ثانیه پس از پرتاب منفجر شد. آژانس فضایی چین هنوز بیانیه‌ای در مورد این حادثه منتشر نکرده است./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/680223" target="_blank">📅 10:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680218">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/681a3a0b98.mp4?token=oz03B3BUKxzGEnGIuUXVhabBudccuNC7plw-qQq08jNXOZB53d4qn1hhkoHdvx1o_NjZBJwN3YTDEHYyMvu_zlEEyXl5n4fxvh69-mJZaRHbq7frPl2JzBboBSWDc6VpI3BCpcQ_0tj2eCpBfLo32hbNkn20Nm16z32GxxNgDyzqbDF2b-hQxEaxebPNGHKjMihh3ZnuvRWYpNdC2kq_UpyyZ09Y1L4QKKiP7USVS2QBhxfnGqnMkXGaDe0wIdwSfsqyRX_aUDQaEj_1zeyyA04LGSKKnd5XI4lGHB74dTqvAcU8N2wgjIJBHZSVLckWNmkdS3fQ2WS_d-A2HK-03g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/681a3a0b98.mp4?token=oz03B3BUKxzGEnGIuUXVhabBudccuNC7plw-qQq08jNXOZB53d4qn1hhkoHdvx1o_NjZBJwN3YTDEHYyMvu_zlEEyXl5n4fxvh69-mJZaRHbq7frPl2JzBboBSWDc6VpI3BCpcQ_0tj2eCpBfLo32hbNkn20Nm16z32GxxNgDyzqbDF2b-hQxEaxebPNGHKjMihh3ZnuvRWYpNdC2kq_UpyyZ09Y1L4QKKiP7USVS2QBhxfnGqnMkXGaDe0wIdwSfsqyRX_aUDQaEj_1zeyyA04LGSKKnd5XI4lGHB74dTqvAcU8N2wgjIJBHZSVLckWNmkdS3fQ2WS_d-A2HK-03g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عطر و طعم این ته‌چین، مزه‌‌ غذاهای خونه‌ مامان‌بزرگ‌هامون رو می‌ده
😍
مواد لازم:
🔹
یک استکان زعفران دم‌کرده
🔹
دو استکان ماست
🔹
دوقاشق چای‌خوری ادویه ته‌چین
🔹
یک استکان روغن
🔹
سه عدد زرده تخم‌مرغ
🔹
فیله مرغ آب پز
🔹
پلوی آب‌کش #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/680218" target="_blank">📅 10:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680207">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vmJbRLl0zz_SwMGgHacz7X0xiB7uL6mzkw3qvCFarQeQVqocc2jQmz374AV1ceNTg_FOSeA-ffAt62hsxtc48MriXJTR4qhiYP71Q_EZuZWxDqYCDxQBlXGADE_1AkOHPBBneWqO1dAMKYloqLCHokeHuDZWmzmCN8mhVaIKgAKonuRp2LzkchjMkOWEagjm_40whNVooQzt1cGchi5s59XOQVkqImat1UdS8-QZMh2gBJ7T_YW_xUsM6b8PIn4EW3CTOCGLsI1ew2a-543samHJIKbHkaF--7Jj9KVUe_whI6b1pab1WhE8toaQ7YMmufc8MBpnupqBblhLyoAtdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E5JNKhDMgjDWB6DBHery7HT8U6qOM0qOG-VJe1EBYN0kHxaFdD7axd9LjaoSRjqrU7rr1LcUknfgzxwnZ2OtIv02kiZGc0wrIB4ib8FuM0XgIc5WMpkbtA2a9NTNvAGShHke2Dn8MaKp6QkAK6xy5CGQTL5omjziasJsEjhG6ScBxDmtm5NBBM8H37EY4N2AULqYvKWEFA4yBQbsN2gNJ8jxJha4R184Ep2tfR6OYaQiFbwlN6MQCM9g3ZnI7fkd1jJvmCxuNqcjjr4AsEYbwJXprH5SeanJ3bGVPAGxzvTlcKQjgqlrQTXTqJXdfJrl_JxSLEL06xNH0I4piphZ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rulio6HXXmDJ1TjL4Es2DtQItObAZUzTEOmJEy69_uY8wbDMPBKdjGolX7qDa5pq4WqWqatKL_y-6ahpd9wNLqwgIg5uvffsvu27N2DrxF5ja4c4hZLC6uC_0HoPV39LLfTuu890B_-7GxLDeo5waqh9iWlr1NqQuZ48ezNcEb_FaPHfLY4pYwNAppRWIfwV4DETpycXhNkLXkDrA0sUjmB-2CWwve5v6BLqPE4kRZg86VH7yypZRTe8raihkoawWR6jI6mE4rV34Hh2ngpCbzG2wzzHbFSGw20dyG6pZ562vtwTfRhHv_G_alu75Ap6OgIzEZnpi2DRgyFrZXKagQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DrNZWmD1UuHkwf_O0Fd3Q9B48HUakS_6X7QXZVDZSHsvIUt4aD8VJwDuQPig4wDC-KiJ2h88hAfD3EgZDbNm5eJfOsFlj_l5kabOPMlFZfEHZZxxmpDQNUWBMqhihfnvg06FxzFpMVkZPNdUOe50qHhbS9AHiTbyfc_P0r6hn1lAWxysAVc-IajXlYo8hplfGlF17kS2HFt2iA_oTk7qhPYF0xEUon7E8QWla_QJHGAQrCjOs-rPCaQiWAe-ZIBp5CF4GyCa4xlWPLOMfpV3phRTDcDgscX5XeP4cyOCeyIEPDpAK70EjvwMYF10FSjbu_e_9RAQJ3rsiml8WaF1UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h6PB7QvH0m5E4D0AG8WUxy2nBn1yOEMZGZWBuRkGTjUSzH3oW8ah016ixJD7jpr2sCC110gAwFDSUptfxE5MLYLNWg2MepR5c1kOOZU_OaudJFWCFjHrZ7RAV8ySd03jeU2mj8NxVND2u5gs1xFit1zxccDUgNhxE41ANhTxTudJdzGvqnTkgNhqaopfX_6XWbNlRgnIy3mPoRYL1-0cAkd3N5JDy8PZefiJCwHNKAljXCCltiMTMXXbyRbBMbfAqCDOwtxCp6dbNTLAxBrIUZjMuy_UueFCVWtxUr9-9IBmelr9PfiXyD3rNJal5OLASGG8HEn2btjRLi71Fu_xfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IBr9scHCImDJwNEqV2Q6YTjAyCWauZmT_MzYpEMxnzl8mVy5NzOB0vInWS_N2TypJu8Yuk59QxHSaFfS3DngQuTi7gSD94KmOREIjoJc1vl6wNoODvnU_xu89CbiAKr9nFxVfJ4NpJLfzyBNlUHXfYB6hzJqFOK7AOT0UCf_BPWjw283lwlym3k9kdee5RdonTVvVKKbP0QKXuKCumhg4vdAawZ4ybXFWDxl_dwYPAMD7GrxcjI0oeh7eiqppmm-qf9G4UxDdSU_Ig_edaopSJGUMGJffqArTyg1yAiQF6hplakTfzaCMi0JkfOneNt4NDpHEdxmT_Q2HjwZwB3ebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJ3mCAG5BjgG8VRjDrNSqX8PmBkgp5dyQInkuHlpTTDFQ7UdUmPN-M6GMngeRaHd472--m7Kx9SZbPqNzTrmIlgInZT1bBuWELRBp1uaLPlEjCe3wvQ8lmnLjunRjWY1YN7NUYkY5avJZf-hG9btls0yQDrA1WrHyImAxtYsa11qO4AKSwfoxGLXJ-gqYMNCg5v-dQ4GgBv1q30CEHb1kL22q4-i6mN63_FrHSZ-6lCbc-nODxzAKOP9tB5Jqdvm4SZjLq6L1_Tg7LY1iAg8kPzD7g0goznPK3YYhLDvXC7nR6AHUkcYeERAuGAw6lpRfJunrXNd5LGSE4j_-Ppw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ai23omX7MCVQxs3pGmkWBG2kcfPsH1_-0TKidPeKNoXC5f6faLs_Uk5joe_7CeswdNND9va9iT-8Sz6qGj4kyzQgCuTc92tt5iSn6bdqMVajjB6B8RHc62tXAvAWMi39Od2ki2lMsqoUpCejJM8qNuo71Ttc-uqkuSRyE_hC9r1fmsELd0A_VUDBYkUtRB3IgXWAKWa2nLIU9OFS8iKcVlINKbSQkX3HI0WZcSbPGJHzjaQ7v1CGlqSEryjrJHMj0dS24h4CmFG9gWU4bb0Jstw4JkIsldM-resQnFod0YRVCuQZ8Dd3wHJCDnJqu6X3dr9gvmJEqnG_ELbEesAWfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhyXxgGuqt57GJZ3VRaMZkZBSQ2aSA6f9c3ecIcEcixU1ZJL2ZKNcrHdxtdrFo22LOSFc9ic66dPfuacYZ-fCy0OsdgVqVDf1VSd66colSDjSRU4ChrFhXWB0ERH5hWeZPhSUHApiXvOKOUFdbEKbUpQWTFDEuMDg59lBarYdOpkdjZZWKJht_wHQsqSNHVk1mSTF7kCK4lk0Jwcb-8BLlboQqFYNrUJRzyxVL8vo3-RiAXC5sEv5oH0YRKgd-4hZgUfqPTqNdT6Rv9ZBvhdWr11XH1_ftuMEVtRqs3lIH3pYYsvyA18fGOjII-rFAvEGdWtIl41wuiU2ZAZKFp7Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4UjMhyGCgmBtuwuPa-_S1g30Pw4oEzfgb2magxKXLTS-7CFt2BmcHgP6xW4Ke6_j-TKW2Wr2PaVxwJObrcDOrpZxCJ06FsSTNBQQkvf5InAsxtHtr4TROeEM7e92DTQUth2X6ohrHMi62JckjENHo8CfzFqOROsqcj_KAZOM7Ct4072u-oxaigJGaa3ukpRU0TQtL9GjK5IfraIQUpmHPCMmEEAPL4CByAgNCtLu0hOI8LB9DTDOtc-b0IM5pEqKyXAVpBNIAy8m9RmmQ4J9sLJdzRjmsgG7N63faSZ19PPULebBOx9lF2eMS--YICsLrCgXkpp0PGn1474vZ8qVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حال و هوای موکب هیئت قرار در مسیر پیاده‌رویی زائران امام رضا(ع) به سمت مشهد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/680207" target="_blank">📅 09:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680206">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
گروگان‌گیری در پایتخت
🔹
صبح امروز در پی اعلام یک مورد گروگانگیری در خیابان ولیعصر، بالاتر از پارک ساعی، موضوع از طریق مرکز فوریت‌های پلیسی ۱۱۰ به پلیس گزارش شد.
🔹
در پی این گزارش، تیم‌های تخصصی رهایی گروگان، سرکلانتری و سایر نیروهای انتظامی در محل حاضر شدند و همزمان عوامل آتش‌نشانی نیز در محل حضور داشتند. با حضور به‌ موقع نیروهای انتظامی، گروگان آزاد و فرد گروگانگیر مهار شد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/680206" target="_blank">📅 09:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680199">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: اگر یک پل ما را زدند، باید دو پل آن‌ها را بزنیم/ ما بسیاری از زیرساخت‌های دشمن را نابود کرده‌ایم که اطلاعات آن‌ها توسط دشمن سانسور شده است
محمدرضا رضایی کوچی، عضو کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
نیروهای رزمنده ما خیلی از زیرساخت‌ها، پل‌ها و نیروگاه‌های دشمن را مورد هدف قرار دادند؛ منتهی اخبار بیرون نمی‌آید.
🔹
نزدیک به ۵۰ هواپیمای ما آسیب دید که حدود هشت مورد آن‌ها عملیاتی و فعال بودند، مابقی از رده خارج شده بودند یا در تعمیرات بودند.
🔹
در بحث خسارات جنگ آمارها متفاوت است؛ وزارت اقتصاد، وزارت راه و بانک‌ها هر کدام یک آمار می دهند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/680199" target="_blank">📅 09:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680198">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ادغام ستادکل و قرارگاه خاتم؛ آغاز یک ساختار جدید نظامی در کشور
🔹
فرماندهی معظم کل قوا طی حکمی ضمن انتصاب سرلشکر پاسدار خلبان علی عبدالهی به عنوان رئیس ستادکل نیروهای مسلح، بر ضرورت تکمیل روند ادغام ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم الانبیاء(ص) تاکید کردند؛ ادغامی که براساس تدبیر امام شهید از سال گذشته آغاز شده است./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/680198" target="_blank">📅 08:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680196">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52aa08b141.mp4?token=W0nCv4Q_r0cwK4Ey_-D3zboyEscsPNzdi11vdTWFxS_cWAMurJT7bnICKxpDIyjELXBDyxU6ZEy16KVgDp9fNr6P12jeNX_z2ZVMJ9FI4sL-lUfODVVqJSs3Vu85ZWXhI2J3yJiW-ZWrKVxlehSU__PJPO93fACx3ZaAelZxFMhqRstPSCaHzEUz_-BDWvjRN8wmkWvn5icCJAGeCDgG1S2RsZeOl4Z6Am_xExtck6C9PKyh3QgHt3664J09cjtNj02R3zj_6NDUw3ZQPLegpbpywJd-3Eb-gPGjBFkxTUlV-lXi19HSgQXhS868JRMxMwoFLJk0JyQ8hjwIAem06w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52aa08b141.mp4?token=W0nCv4Q_r0cwK4Ey_-D3zboyEscsPNzdi11vdTWFxS_cWAMurJT7bnICKxpDIyjELXBDyxU6ZEy16KVgDp9fNr6P12jeNX_z2ZVMJ9FI4sL-lUfODVVqJSs3Vu85ZWXhI2J3yJiW-ZWrKVxlehSU__PJPO93fACx3ZaAelZxFMhqRstPSCaHzEUz_-BDWvjRN8wmkWvn5icCJAGeCDgG1S2RsZeOl4Z6Am_xExtck6C9PKyh3QgHt3664J09cjtNj02R3zj_6NDUw3ZQPLegpbpywJd-3Eb-gPGjBFkxTUlV-lXi19HSgQXhS868JRMxMwoFLJk0JyQ8hjwIAem06w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال و هوای موکب هیئت قرار در مسیر حرکت زائران پیاده امام رضا(ع) به سمت مشهد
🔹
موکب هیئت قرار به همت همکاران هلدینگ رسانه‌ای خبرفوری راه‌اندازی شده است
@Heyate_gharar</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/680196" target="_blank">📅 08:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680195">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
انتقام عجیب عروس از مادرشوهر: ۳۰۰ گرم طلا را با بدلی عوض کردم!
🔹
زن میانسالی از عروسش به اتهام سرقت ۳۰۰ گرم طلا شکایت کرد.
🔹
عروس اعتراف کرد با تهیه کلید یدکی گاوصندوق، از طلاها بدل مشابه می‌ساخته و آنها را با اصل جابه‌جا می‌کرده است.
🔹
او گفت به دلیل اختلاف با خانواده همسرش، طلاهای اصل را می‌فروخته تا از آنها انتقام بگیرد. تحقیقات درباره این سرقت‌های سریالی ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/680195" target="_blank">📅 08:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680184">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c442ac82b.mp4?token=CbG3acC5H5Lx_g9EL0kc7gZ3yCWORpFR0tMUPciz2lMxS79gm3RNkEZ5CzI6Z0bwvzeS2MCi2N60Yqc9126VWDnq_BbWXxaLGyInbud0A7TNo2HY5vij9pguFcz63m4vRkbQq3DgBGMQV82pzlf7AgAnMsyeN9iPKhnR70oQjDcavxe9r58rvK0ztHxMViglFyNczJMmXz-Vxw_c4FqhxVeG5aA7fOC35ecPbo1dKBwOG37JCha1ezjBj8cadfJVyL1R5IxIvYpRDJIV4DLOVR6PULgeLkVVm_PuC6CDEt6UMPtu440e7hdWmNv9nQfm1rOZOrw8qA6g6bS-R_y997-ax5aFuvuJKi4AAzMEy6DpTOroszhqRZraNx277q0ZPXUgjF-b1LFppie6Z4a4vj19zHngEAqSHcCFa1GpGzTR5svmQJqlxbzkI2Mx-6C51fv1du2mBizmd2TDuEcRYKneHil31i_zPhHDSrJTWJUCgccg750CPl4y9d4KxP5-umd6t4-Yz7qUhuMDdrlRLhcthQXedet6-X4DIpzh6nkvGha2-bpS4s176UQnmSqfPsKj5fKQkPgBz-XVAEBugdP3ZJpr6LxSXPHTNln9dPdXJfgzPwiXj01x2gCeiqSC308RfF_YPYRDCvKT9iQ7mF8Vp15DQL9fiS_LZQqwiM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c442ac82b.mp4?token=CbG3acC5H5Lx_g9EL0kc7gZ3yCWORpFR0tMUPciz2lMxS79gm3RNkEZ5CzI6Z0bwvzeS2MCi2N60Yqc9126VWDnq_BbWXxaLGyInbud0A7TNo2HY5vij9pguFcz63m4vRkbQq3DgBGMQV82pzlf7AgAnMsyeN9iPKhnR70oQjDcavxe9r58rvK0ztHxMViglFyNczJMmXz-Vxw_c4FqhxVeG5aA7fOC35ecPbo1dKBwOG37JCha1ezjBj8cadfJVyL1R5IxIvYpRDJIV4DLOVR6PULgeLkVVm_PuC6CDEt6UMPtu440e7hdWmNv9nQfm1rOZOrw8qA6g6bS-R_y997-ax5aFuvuJKi4AAzMEy6DpTOroszhqRZraNx277q0ZPXUgjF-b1LFppie6Z4a4vj19zHngEAqSHcCFa1GpGzTR5svmQJqlxbzkI2Mx-6C51fv1du2mBizmd2TDuEcRYKneHil31i_zPhHDSrJTWJUCgccg750CPl4y9d4KxP5-umd6t4-Yz7qUhuMDdrlRLhcthQXedet6-X4DIpzh6nkvGha2-bpS4s176UQnmSqfPsKj5fKQkPgBz-XVAEBugdP3ZJpr6LxSXPHTNln9dPdXJfgzPwiXj01x2gCeiqSC308RfF_YPYRDCvKT9iQ7mF8Vp15DQL9fiS_LZQqwiM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر دیگر از فروریختن ساختمان‌ها در کلمبیا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/680184" target="_blank">📅 08:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680183">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0124cfeedb.mp4?token=FzgPlLzI83-2Gbz0VBS7WNogWk1NY5g9M42_LKuCk8PCCC-A_4uHP2J8xNNtJQEGvwYMrMXA44_RNgNlT6v903BdLRXrcf_-AZXIedn1gbNySfymaDIrle4XQ9PeDO49LwUybFnGHsin92N4MN1fp2PXkduSDAs4_hpVVir-5v74J622szGUoDVGO_eE_b4L_JB9ua_PiVoD7NVNqw3zFWovAqKQz05_8d-Ro6_uPl6wGTwRB7KbCXnLmaywpUV2Q5B82L9m1HDHGebKa4YIN8P7T8sqHhhQn5jMCbNYQ2Jy7MLq5otztvHGcxZc9eYS02FdvC-0P6FJSnFbWRnp0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0124cfeedb.mp4?token=FzgPlLzI83-2Gbz0VBS7WNogWk1NY5g9M42_LKuCk8PCCC-A_4uHP2J8xNNtJQEGvwYMrMXA44_RNgNlT6v903BdLRXrcf_-AZXIedn1gbNySfymaDIrle4XQ9PeDO49LwUybFnGHsin92N4MN1fp2PXkduSDAs4_hpVVir-5v74J622szGUoDVGO_eE_b4L_JB9ua_PiVoD7NVNqw3zFWovAqKQz05_8d-Ro6_uPl6wGTwRB7KbCXnLmaywpUV2Q5B82L9m1HDHGebKa4YIN8P7T8sqHhhQn5jMCbNYQ2Jy7MLq5otztvHGcxZc9eYS02FdvC-0P6FJSnFbWRnp0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرین‌هایی برای فرم‌دهی به پایین‌تنه و میان‌تنه
🔹
اگر به‌ دنبال تمرین‌هایی برای تقویت عضلات پا، زیربغل، کمر و شکم هستید، این حرکات را امتحان کنید. #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/680183" target="_blank">📅 08:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680180">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hL8ni_JZlQF6lFgD4S5LWJbUHxuzF5JuJ08FTVT7aCWwyY-zr4-ZZauAe0lodIzzT7pBvQTIsikqEQe6FCZywoXppWIgeaC25rHBCS-Xg7lhR7dxOzzh838Qogg_hILO5LGFkMUaDCICIACjuiWhlmlY7iOrjHEkG79hCx4ly6SFMrDx6IeY5Y-TalAjhWL1u8W2x5OlJiXGNFGjstTLT_-4hEfKQTrPgFF4ch71sChLbvDh0MKw0im4Nq8zkFJBPC0x-L7peCJmw124VDIPpGS-QZ4usxeIk6pCyyypfgaCBlk-bR_vFOGMutkTV85RMg_JDzIKopE_2LBh3D34Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن پست: ترامپ در ترکیه از ترس ایران با کامیون آشغال جا به جا شد
واشنگتن‌پست:
🔹
دونالد ترامپ، پس از حضور در اجلاس ماه گذشته ناتو در آنکارا از ترس تهدید ایران، به صورت مخفیانه با یک هواپیمای نظامی جایگزین از ترکیه خارج شد.
🔹
طبق گزارش واشنگتن پست، ترامپ پس از سوار شدن به جت قدیمی ایر فورس وان، دقایقی بعد مخفیانه به یک هواپیمای کوچک‌تر C-32A نیروی هوایی منتقل شد.
🔹
او از طریق یک کامیون پذیرایی فرودگاهی که معمولاً برای بارگیری غذا و سایر تدارکات استفاده می‌شود به آن هواپیما رسید./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/680180" target="_blank">📅 07:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680179">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d7c54a64.mp4?token=D8h9EI46T89yv6KyJ4HjAJADTB5GxqmCCihQaH4N9EYqZqVbobh5ZXONx6KX3rkFquPUWQzIzyAMkeQ_-Z0GCOskoBS4Mgk-mhCy2ShycqyHcygKkow9Oeh6snE96475X17U_y44zl9uKmCumI2hCDKM9WWVsXy91zurt04-IDIC9FQsyJqykn4Caz0eHk0aR7t6xQdb6ZXhC5VB5vDkmYY1lSFZUO3PnGa9Cb5_FmilguOxkn11tgKbRyZ89Ae7EVy13HkMJYnUhkYonJmcPgYPFDiiFtayeyu6TK-UtlzAWakysf2454iAAFdAYWyWnyEcsrkECnBFGFuTayidNlqDUEYN2Ccf7D1QoDnUSRsV7o9GR5NxbYmKKk5Z7GkgxSeFaOwSE5iGV1Wbc3gUdlLC1yPBcK9-xgUPuWzl5eIcv2PnaAtPub-lSAtZoMp0gGv2AHlAf2Xv__m63_P5msGsWYQjGHwvMZPrbe7YBBqMjl9tba5SGeDfSDNWlxNLfQ8n6rmSpFENkPd1JYNh8yubAHl97qFM7op_q3IIgenomYb8OWTiGqWey65TGPTTtODAerWrA2OJM9WlZStlvlMgLRZXV0xFhE0WfIvKCnhMiC8_6_AD4EEgWQgVEeAPv-f1T4S-05IIBNdLZCi4ePrOyCfsas7e6OTl7JoLuug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d7c54a64.mp4?token=D8h9EI46T89yv6KyJ4HjAJADTB5GxqmCCihQaH4N9EYqZqVbobh5ZXONx6KX3rkFquPUWQzIzyAMkeQ_-Z0GCOskoBS4Mgk-mhCy2ShycqyHcygKkow9Oeh6snE96475X17U_y44zl9uKmCumI2hCDKM9WWVsXy91zurt04-IDIC9FQsyJqykn4Caz0eHk0aR7t6xQdb6ZXhC5VB5vDkmYY1lSFZUO3PnGa9Cb5_FmilguOxkn11tgKbRyZ89Ae7EVy13HkMJYnUhkYonJmcPgYPFDiiFtayeyu6TK-UtlzAWakysf2454iAAFdAYWyWnyEcsrkECnBFGFuTayidNlqDUEYN2Ccf7D1QoDnUSRsV7o9GR5NxbYmKKk5Z7GkgxSeFaOwSE5iGV1Wbc3gUdlLC1yPBcK9-xgUPuWzl5eIcv2PnaAtPub-lSAtZoMp0gGv2AHlAf2Xv__m63_P5msGsWYQjGHwvMZPrbe7YBBqMjl9tba5SGeDfSDNWlxNLfQ8n6rmSpFENkPd1JYNh8yubAHl97qFM7op_q3IIgenomYb8OWTiGqWey65TGPTTtODAerWrA2OJM9WlZStlvlMgLRZXV0xFhE0WfIvKCnhMiC8_6_AD4EEgWQgVEeAPv-f1T4S-05IIBNdLZCi4ePrOyCfsas7e6OTl7JoLuug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات انسان‌نما در نمایشگاه AWE ۲٠۲۶ شانگهای
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/680179" target="_blank">📅 07:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680176">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBmcSU1jo1r3Ae4OCKXJjJzij9adMrr_kUDiB_m_WmRHN2Jh1in0RMzFpmWXg40DnFc1gF8pzcBesZpTz-K34pIYWoTvMZ74_pQdt5g-TYz6xbofcmUxM3Rzf2KBy2I5SsBfTz6D7ZJ6N5sCfgeksspjeOfpHzLbzh0F_OIWij5A-uDtwv-1bK3D8sHXOoTcTcnlSaJUYlBRjall_dS6rCOvuvWYylpHWmOYz5q59qWzGlZoVfDd7Nb_PmBAgVNi4CwlbeqN8b4EfIU1IbUtbYC231K5vvBCkP1bcJuct5w8EyhfRm5FJnlwd8D2Jg7MSUM2laNuIuUOfAvvbTKDmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۲۰ مرداد ماه
۲۷ صفر ‌۱۴۴۸
۱۱ آگوست ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/680176" target="_blank">📅 07:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680174">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9ovyiuw6WSdVYSR4cJLhnDKdqupaSIzWceds1V629nxYDsnUfbfdKHp41EHK-QQZhuJqmnVf6v_RZlLbqhRDBz-FWRJJGaulGRbIcqsMu9BLYXJqBm5oGnD0Hb3LcZCmYssKtVUvJMpQ7ERePpS7tSIH_CHyAJePDW7IN8scbsgiPCeV8R7tn6_YKH9xT3xCnwU_jopbytYuhya-7dTLnmWbB4-lY2E_ovRuQ2vMoX4vo-Q8x8toUZa5c2AAwD9lBMOV7Xg3IG3nCthCwYIsBPgtXimlMW1KkbEMZzgxahb0ybSGGbI-UOhM_CQy04JCqz8zLzB2muL8rCm4KpzXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسوایی اخلاقی رئیس فیفا فاش شد
🔹
طبق گزارش یک نشریه انگلیسی، او در دوران حضورش در یوفا به مدت ۵ سال با یک زن رابطهٔ غیراخلاقی داشته و از سمت خود سوءاستفاده کرده است.
🔹
پیشتر نیز پروندهٔ اخراج او به دلیل زدوبند با ترامپ مطرح شده بود. حالا این افشاگری در ۳…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/680174" target="_blank">📅 06:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680172">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-c-j93cFqWYo_mAqzHBNc5DVYarzh9yy1rJ2jAdFBWpaSnbbACtynJtYickGUGTh8yD1NlWELeOB7xhoxbFn1_WV_sFHna4nH-ZGKuczHgUuyRLlU3nDK3MdhkdtPuiSDomDEgx4dUlsSsZt2d5gRYTOJrt0YVkNKLkZUvSEyRazrWTN4CZrQ14rzSr0AsiY7APAPgSyCNXRaCjawTY26sgb3aoDeS9T7qyeHTuxCol4vEWgJ1F6TsAIDQQ4aIaBQHp58eMjFtEhZekmJrwHjrO5qNIPVYlv7bcWZTi7VzN1jgSHgD4dSlHv3bRkovIS1Q659e9yGMFjyssH478RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ، آخر هفته در زمین گلف خود در بدمینستر، در کنار یک سامانه پدافند هوایی کوتاه‌برد AN/TWQ-۱ اونجر (SHORAD)، گلف بازی کرد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/akhbarefori/680172" target="_blank">📅 03:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680167">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c50bf2a37.mp4?token=hXa1CeGCBbbYlTu08gIbdPYNyCSiceDoLT8p2qvHxQEICp638vfKCmz8uxAebA0GcYEt9S26wO5sqNyp7WAf5xPu6HB2z1clYc2Bg4OuNE-2vxk6c1Y7AdRK61GDxcMBXmRsZcESnjmHLUfkuZPYdYd_WRugIFfjm3DpK8Rgwph9U0TQecNAw5OVkj62AEXZhovK64JD8FSUmFtgFLHqiJlQyA8rIr1pmX53BW-Mu0dciU3rqPsuQj4Y4TtiWqTo9hwGk6f3gCpC9kKnaQLEGuqF-ZbavEY1V4QFiiat_V4stvlGKde2w7yIAY0ylYDam7QQcRbz9k8zj-kX8EIZRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c50bf2a37.mp4?token=hXa1CeGCBbbYlTu08gIbdPYNyCSiceDoLT8p2qvHxQEICp638vfKCmz8uxAebA0GcYEt9S26wO5sqNyp7WAf5xPu6HB2z1clYc2Bg4OuNE-2vxk6c1Y7AdRK61GDxcMBXmRsZcESnjmHLUfkuZPYdYd_WRugIFfjm3DpK8Rgwph9U0TQecNAw5OVkj62AEXZhovK64JD8FSUmFtgFLHqiJlQyA8rIr1pmX53BW-Mu0dciU3rqPsuQj4Y4TtiWqTo9hwGk6f3gCpC9kKnaQLEGuqF-ZbavEY1V4QFiiat_V4stvlGKde2w7yIAY0ylYDam7QQcRbz9k8zj-kX8EIZRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع چندین انفجار در مناطق مختلف کی‌یف پایتخت اوکراین
🔹
منابع خبری از وقوع چندین انفجار در مناطق مختلف کی‌یف پایتخت اوکراین خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/akhbarefori/680167" target="_blank">📅 01:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680164">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R26vwlxhNlWw1vSVsKzKl5pFSM_0RkbmXUcZdgqZAw1Wrl6DrzQORSxFOKV5jmPnHWmz-isj-q63zztNqURNm5j2VgsnyUq5m-esk92vXjaG9JUwntaVr6f1pVBIv5I4auns19vwimpxT0Tz_9CBuRZ0b4L_1BXmNo5bgW3VPq1g6qteYmkrBiJCcufmR1xs6XiXJZk4vO0cTh-1gja-OdLgqdd5wy4xzK9e9kEREeIUbfXDKMBwvuWLm12UaLWiBuvw9f8Ts2vjBlX5ceQckhs2g0nPD78NqjpjCNXd371vQfjgaBDEp1spS0GJtCOMOKARwM6XjCkj_uapC01mFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لشکرکشی نفتکش‌های عربستانی به سوی تنگۀ هرمز
🔹
گروهی از نفتکش‌های مرتبط با عربستان از دریای عمان به سمت تنگۀ هرمز روانه‌ شده‌اند.
🔹
ناوگان ترانزیت نفت عربستان توان عبور از باب‌المندب را ندارند و در تنگۀ هرمز هم باید ترتیبات ایرانی را رعایت کنند‌.
🔹
تنها راه بدون نظارت ایران و محور مقاومت برای نفتکش‌های عربستانی حرکت از کانال سوئز، دورزدن آفریقا و گذر از دماغۀ امیدنیک است که طول سفر را ۲۵ روز افزایش می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/akhbarefori/680164" target="_blank">📅 01:04 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
