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
<img src="https://cdn4.telesco.pe/file/kMA480aO3f68fndHC4hfG6R_FWf5dLBG8Gc3gO4v6jfzcDIhmnQWE4Hb3HdGdWwuXe-NLIsP8dO8zJ2yY07hL8dvPOgFsHTQMcYR86goavRIV4yZEdxbV4b3c1BZKPuYERw7PlZ1-TEYoXFc6rHOpx8KE6EhFB1QYfQVQMrlE0-vKYaQmjsIm0FooRTTuMzsws5dEvkTgUhX9VCqpZu2VFNV8ZtktZKsTmOyPgR8lsC9rjB7sPY7Q8s_o5gdkjF8DDj3vtu9hhHNs53rH_1BFJftUEtTYobIxlGoXH55tAWy_8npmAdarsrfjuo6DoHTRhxRCg7Gcud9kPWnySH9WQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 09:59:14</div>
<hr>

<div class="tg-post" id="msg-440641">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
لحظاتی پیش صدای انفجار در مناطقی از تهران، اصفهان و تبریز شنیده شد
🔹
ارتش رژیم صهیونیستی حملات به ایران را تایید کرد.
📝
اخبار تکمیلی متعاقباً ارسال خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/farsna/440641" target="_blank">📅 09:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440639">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFwwKuBiPChdz_WvBJ4Bd0pKuI9jWE4RomTFGVtFdvFTAXMUXYitbFhte2zmrRQmAcZXquhJjWuNOwWq_hHUn0dmQWgaxeqIOGT39KBfyDB9nYpq20h3bHq3dkm9_zaODno9x_Yjpzssj9LzehHq_I971XDTF3sA4jjhLkxSCNoJ8oyITM-00EFMMdXiTlQDcBcFrmqFiNO0MPkVpwrrswwijebN49GFHgxIX71qmtj1reJhDHtWhtJ4LKTdXH5FxrR1fAGczTGnimCTvB7p2z0jw7C31JTb4GaLN3YN3dTCpuYVKu9f7pUDjp2Z2_91z26kJTxzWOfSDYDQ8NoCBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی سپاه: برای چندمین‌بار ثابت کردیم که آسمان سرزمین‌های اشغالی و منطقه، تحت ارادهٔ ما و در تصرف غرش موشک‌های ویرانگر هوافضای سپاه است.
@Farsna</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/440639" target="_blank">📅 09:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440638">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تمامی پروازهای فرودگاه مهرآباد لغو شد
🔹
تا اطلاع ثانوی، تمامی پروازهای فرودگاه مهرآباد تهران لغو شده است؛ مسافران پیش از مراجعه به فرودگاه، آخرین وضعیت پروازها را از طریق سامانهٔ ۱۹۹ یا شماره ۰۲۱-۶۱۰۲۱ پیگیری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/440638" target="_blank">📅 09:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440637">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaSP2sGGEQEUz4blyMd7FCSClsTdxzFoJBoXcEgZzC4ekhjM_y3ZIwzg6cS6G0qGGYsRKs4cmPQgbbVtKrLovLlHaN9QAV9anHMdL4re0zH5-fmTBNI7DYvosBuC7R7SEDuTMcLGfbK94PngxXPqL5VP2gbitAESYjXa1NH6CsYLu_CyvwEgD8d_IttqOe21EcQe7QK47MkXqvcYqFayeuGWLpq0ChvzMMbmCmNhbdbNzVZgwnNk3c2WBwqna0w924SNsePkI_Gars906XqCkBmMTbBASVBURcmLU0oNTndH8hGwTB8z4r_gG5r6fwnyFW65jcYxz-aA8qiV1TUw8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مجوز‌ حرفه‌ای ۶ باشگاه ایرانی تأیید شد
🔹
با اعلام کنفدراسیون فوتبال آسیا AFC باشگاه آلومینیوم اراک، چادرملو اردکان، استقلال، گل گهر، پرسپولیس و تراکتور مجوز حرفهای برای فصل آینده را دریافت کردند.
🔹
خبری از سپاهان نیست.
@Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/440637" target="_blank">📅 09:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440636">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI8JgciZ7pSmyLWDjnGVeDTWjKgsc3Y1YKTQX9FkEd38M0phhT7IYzlCEKiZNDgZ_9KRAFf2YhPyzuG32CZK69j2LKIm3I5_R5J2eMChs7PVyijJj2vLm-HCkCrL3aBHpOl08MZrohpS5jh_3IOzcbQ7-MSQbwVDgL1iIhk1H1kfwNv69je8bUC3Orogb0X9E1TKtVAsk58-GpIJteVWk03Y_rpRsTeOas-cKvSnro9uK-WdeYJz6ceh7Gk2boTGzXdTY-ilt7zoaSvUOJcYqjmPPiPp6hwiDWXeQUZRdZJTswzCU-U_yStV2wCBYtYlyJRJfMvX50mouAxm1DHE-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ حملۀ موشکی یمن به اراضی اشغالی
🔹
ارتش رژیم صهیونیستی: ما شلیک موشکی از یمن به سمت اسرائیل را شناسایی کردیم و سیستم‌های دفاعی در حال رهگیری آن هستند. @Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/440636" target="_blank">📅 09:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440635">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">درخواست جبهه داخلی اسرائیل برای اعمال محدودیت بر فرودگاه بن‌گوریون
🔹
شبکه ۱۲ اسرائیل به‌نقل از جبههٔ داخلی اسرائیل اعلام کرد که خواهان اعمال محدودیت‌های جدید در فرودگاه بن‌گوریون تل‌آویو شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/440635" target="_blank">📅 09:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440634">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c1fd0bcd.mp4?token=DKBYJoU1UJ5bBTTsj7syBkdf4vnSQyl-G8calwGNfeXi25MpLVVVvv3hxWjDrCIIAOU06Y7TBdrrHK2r3PIGWIfnpkEy09fdnK-86LMemizIXTS6dzh11Kqi_r1Ru3uTjbzAJhmwDmEeLd5YO6k2vK9HM04OyoUQKhBn9ifsZe5g1ukrI8qtnJC9ZglNyfHcMMf8C3PPw8FUApTlYxYumJ_rOP-7u_6zw-UpCpO7umoVjv01NoVqdMBSbwHvgRmrsqtYoB_Rk3c46686jccrZLXNqZh0aHK0TaU6KVRgaFe700_IQSZ1w2ThCtUGw7NG8qjD451pKJf3-l5qh23QLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c1fd0bcd.mp4?token=DKBYJoU1UJ5bBTTsj7syBkdf4vnSQyl-G8calwGNfeXi25MpLVVVvv3hxWjDrCIIAOU06Y7TBdrrHK2r3PIGWIfnpkEy09fdnK-86LMemizIXTS6dzh11Kqi_r1Ru3uTjbzAJhmwDmEeLd5YO6k2vK9HM04OyoUQKhBn9ifsZe5g1ukrI8qtnJC9ZglNyfHcMMf8C3PPw8FUApTlYxYumJ_rOP-7u_6zw-UpCpO7umoVjv01NoVqdMBSbwHvgRmrsqtYoB_Rk3c46686jccrZLXNqZh0aHK0TaU6KVRgaFe700_IQSZ1w2ThCtUGw7NG8qjD451pKJf3-l5qh23QLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زارعان، کارشناس مسائل غرب آسیا: حملۀ امروز صبح رژیم صهیونیستی به خاک کشورمان با هماهنگی کامل آمریکا بوده.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/440634" target="_blank">📅 08:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440632">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
آغاز عملیات نصر علیه پایگاه‌های تل‌نوف و نواتیم
🔹
سپاه پاسداران: دقایقی پیش رزمندگان شجاع نیروی هوافضای سپاه عملیات نصر را با رمز مقدس یا حیدر کرار و هدیه به شهدای جنگ ۱۲ روزه با هدف‌قراردادن مراکز مهم پایگاه‌های هوایی راهبردی نواتیم و تل‌نوف آغاز کردند.
🔹
این عملیات در پاسخ به تجاوز موشکی رژیم کودک‌کش صهیونی به چند سایت راداری در ۳ نقطهٔ کشور انجام شد.
🔹
سرعت عمل در پاسخ به تجاوزات ارتش رژیم صهیونیستی و گستردگی بانک اهداف جزو اقدامات گروه‌های عمل‌کننده در این مرحله بوده است.
🔹
کلیه یگان‌های رزمی و عملیاتی سپاه پاسداران برای انجام عملیات عبرت‌آموز گسترده در تمام جبهه‌ها در آمادگی کامل هستند و برنامه‌های اقدام را متناسب با سناریوهای دشمن تدارک دیده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/440632" target="_blank">📅 08:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440631">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFPF7JKYTuCudYpxH-OaNbfsHoSq0BOobjD09zL4GYKpqsocl9k2y5NX2gb9cDuw08U1ERUcIk2ZWNah9CHaY6D0QqEXYPNCkUqunef2oJQB85q0CCXshhCxrNdxnCAEfbKctiZBlURU8wG0Ma7wJwyWl43L7nDhKzpr0Zitx3Ngv3sG7xCwO_C1-hhMiOvFvkCIN_CJzDGakvXw_iKFjYs9aX_xY_rdxM2P2i0AI_DLwhEo6G5XRZ3_1ZlVn9_RYRP47vCaR-QKQ8TQkzQ0AjFjUtW_drcvQY2Ibv1XfwHZDa3FdgyotaVwMWSLOjANbdoqhlTR9TPbJKnZT58bUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دست‌نوشته شهید لاریجانی:
🔹
اقلیم پارس را غم از آسیب دهر نیست
🔹
تا بر سرش بود چو تویی سایه خدا
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/440631" target="_blank">📅 08:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440630">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
تهاجم هوایی دشمن صهیونیستی به شرکت پتروشیمی کارون ماهشهر
🔹
معاون امنیتی استانداری خوزستان: دقایقی پیش شرکت پتروشیمی کارون ماهشهر مورد تهاجم هوایی و اصابت پرتابه‌های دشمن صهیونیستی قرار گرفت و بخشی از آن آسیب دید.
📝
خبر تکمیلی در خصوص خسارات و تلفات احتمالی…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/440630" target="_blank">📅 08:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440629">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سفیر آمریکا در اسرائیل به پناهگاه رفت
🔹
سفیر آمریکا در اسرائیل در صفحهٔ خود نوشت: الآن در پناهگاهم. صدای انفجارهای مهیبی از بالا می‌آید. امیدوارم که رهگیری شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/440629" target="_blank">📅 08:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440628">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f6c5571ea.mp4?token=TrgG-lgscR-wR_Z3ZU03UM0gvzGGxLQL9-SqjOHbMwRZwVBxjRRYMdnm53-bz72kNYJiQr7sk6bNew8VMlRWFdOn8MzDHMn2JEZRUBs8uhEnzqf4GKTa3yikRazMLKUoI5Eb0UxD9l8JncFMG0oC6T6lqVwoNRKxFHkdXr-wvcp0lhWr5wAV6LwpS12avWcr9aEGowFA8SPqZjlVuOhdZ897fTV9QuL6EATvIsbOucAOgPRj65VS1drNtB1GZAMZkVPPtU9WaugWEzXG0Y7B08CTxwekfzX06mfjn0ALLWxsNDLhWklxhaf5LyGmr7Wf_zfMi371Qv1baKkdfhNirA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f6c5571ea.mp4?token=TrgG-lgscR-wR_Z3ZU03UM0gvzGGxLQL9-SqjOHbMwRZwVBxjRRYMdnm53-bz72kNYJiQr7sk6bNew8VMlRWFdOn8MzDHMn2JEZRUBs8uhEnzqf4GKTa3yikRazMLKUoI5Eb0UxD9l8JncFMG0oC6T6lqVwoNRKxFHkdXr-wvcp0lhWr5wAV6LwpS12avWcr9aEGowFA8SPqZjlVuOhdZ897fTV9QuL6EATvIsbOucAOgPRj65VS1drNtB1GZAMZkVPPtU9WaugWEzXG0Y7B08CTxwekfzX06mfjn0ALLWxsNDLhWklxhaf5LyGmr7Wf_zfMi371Qv1baKkdfhNirA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ستونی از دود در محل اصابت موشک ایران به هوا بلند شده است  @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/440628" target="_blank">📅 08:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440627">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌
🔴
گروه هکری حنظله: به هر کشوری که برای تروریست‌ها فرش قرمز پهن کرده می‌گوییم نوبت شما هم خواهد رسید
🔹
هیچ سرزمینی بیش از حد دور نیست، هیچ سروری امن نخواهد بود و هیچ شبکه‌ای از دسترس ما خارج نیست. منتظر بمانید و تماشا کنید.
🔹
شاید همین حالا هم سایه‌ای در…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/440627" target="_blank">📅 08:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440626">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
گروه هکری حنظله: از شما دعوت می‌کنم تا شاهد ویرانگرترین حملات سایبری علیه زیرساخت‌های حیاتی و نظامی دشمن باشید.  @Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/440626" target="_blank">📅 08:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440625">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
گروه هکری حنظله: از شما دعوت می‌کنم تا شاهد ویرانگرترین حملات سایبری علیه زیرساخت‌های حیاتی و نظامی دشمن باشید.
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/440625" target="_blank">📅 08:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440624">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
تهاجم هوایی دشمن صهیونیستی به شرکت پتروشیمی کارون ماهشهر
🔹
معاون امنیتی استانداری خوزستان: دقایقی پیش شرکت پتروشیمی کارون ماهشهر مورد تهاجم هوایی و اصابت پرتابه‌های دشمن صهیونیستی قرار گرفت و بخشی از آن آسیب دید.
📝
خبر تکمیلی در خصوص خسارات و تلفات احتمالی متعاقبا اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/440624" target="_blank">📅 08:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440623">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f8a2558e.mp4?token=cAxdFuPr2u8Eib51JiDShdqTLZqea1krjqoFTQ1e5iMovUE7NphSmSZ1Z8ET2WzCOGAllM5CMHkM14sVWwF99VB0SSnxamq2j12QcQ4DuoHHVHmeN-rtVztt53cKo4QjzQRx1NdAvWOiAK5h79ED-ILv5inaxvfWhEC-L82AhXlbhtKwSqbDjX_AvRLsDj0PYy57lL_4I3tpGMVIlns8_WCDD6K7iLUfSZSCzIApSqGU8mVXDVECsAqQsKDQD_kTHfEi6ycijpr6_8Hprs17rsmzc4p-yA-xv5AXAs_AyX3buKJym_NWjCWQwt9GEkUoNahsOezwbYSZyk8OM2py4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f8a2558e.mp4?token=cAxdFuPr2u8Eib51JiDShdqTLZqea1krjqoFTQ1e5iMovUE7NphSmSZ1Z8ET2WzCOGAllM5CMHkM14sVWwF99VB0SSnxamq2j12QcQ4DuoHHVHmeN-rtVztt53cKo4QjzQRx1NdAvWOiAK5h79ED-ILv5inaxvfWhEC-L82AhXlbhtKwSqbDjX_AvRLsDj0PYy57lL_4I3tpGMVIlns8_WCDD6K7iLUfSZSCzIApSqGU8mVXDVECsAqQsKDQD_kTHfEi6ycijpr6_8Hprs17rsmzc4p-yA-xv5AXAs_AyX3buKJym_NWjCWQwt9GEkUoNahsOezwbYSZyk8OM2py4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
اصابت موشک به منطقهٔ شومرون در شمال کرانهٔ باختری  @Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/440623" target="_blank">📅 07:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440622">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvchchLJ54o3wyGoEgZdr7oLwvr8hcHHfmREd9449xC2Yh-hEEwY_aGZUccRkj110b29Cu8XEW9Sie-SAnMro13vFnU-wntctGOcgRCH2_XbwE-1FPowoQMzM267K64bIz0lkOsLwo2738A97Fi-u5CostD-L_Xu0GJv8_odCWDWIFxhXG690Ec9gT_y2lyAQTuj7Cl7JGJtEp2LdAw8EUnWMG3Bsy5UzwvYGds3KRMml88U6Gk9u6dnQ3cDUOZMq0K8X9JL9iE4pHgIfDMtFqwg4AaY5viyEkm0oqdAbR1vdYf45NWKg3Fo7jmtdnGclbcu4MWe272su12Y9ZaVGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آژیرهای خطر در اراضی اشغالی بار دیگر به صدا در آمدند
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/440622" target="_blank">📅 07:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440621">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndAYii9tfdkKCRya3QKplDrx8dgHrs3jYDxFga6BuJrDJVBsHDTMWBgmWHLY9Wp09TbDZbuUQ8LbMK0J9PVr-iF0hyt7sDerqIHxMQiMMqTB7COaEbs32Vj8zDk5W8EZwK8liVHL3qSV_7Kb0cO_rlFZWxXmc5IR_E5H2tv7n8qTki3FoszDCUJ88EofBfJh_0XEeKYrlgYl9aqzME1E8VGG3160r3zuKU7nQqPmfkf5npjGGTdu2eMrJ8wtlRlejExniviXfAuxdmbABaXYyYtwG0jrr5rJaUB0dmB1DtDNzU94UYQuAPQTIY8KmuCw4yhN9CDl_b9nVqiSP4IpNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عبری: یک موشک به یک مقر نظامی اسرائیل در منطقه کرانه باختری اصابت کرده است.  @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/440621" target="_blank">📅 07:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440620">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_gCydviaHckvTlDwE6jIw2CH71f3FhZQVFVwPyuEH7kAIzcO_bryHJQ8x4QmWCfANhOQX3GlhUbzPfhPvHeZ21M_8JncwVFWCirBnVHUfV1xlnV35obGvbBjD2_iz8l9cQfu4xraMYO6zf-SvVXhYC_WocSr7cCM51xZ1s-QYtkESI5OkxlPvZT5eDp-XQUs7Rfue6K7bR7bOULVpEycmiYF3pb7MoYK4co8iUmg9ITTUfND5j6ISD1yDV-7-89hQBiNB0T9G8u7Ot-hJpVHZKjO3hmRVYEWWZL4i9WFI4j3GxnA0ww-1_64FSvEnAW6byR9mD1gTEq_1tgXh_Cnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
المیادین: در پی حملۀ موشکی ایران، صدای چندین انفجار مهیب و مداوم در سراسر فلسطین اشغالی شنیده شد.  @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/440620" target="_blank">📅 07:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440619">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‌
🔴
شبکه ۱۲ رژیم صهیونیستی از شنیده‌شدن صدای انفجار در منطقه قدس اشغالی خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/440619" target="_blank">📅 07:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440618">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
آژیر حملهٔ موشکی در اراضی اشغالی به صدا درآمد   @Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/440618" target="_blank">📅 07:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440616">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
منابع محلی از موج جدید شلیک موشک‌های ایران به سمت مواضع دشمن خبر می‌دهند.
🔹
همزمان هشدارهای اولیه در سرزمین‌های اشغالی  صادر شده است.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/440616" target="_blank">📅 07:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440615">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljt-2gHoHLHkWzlPaJYcQudz6xqKH19K_r2o5cshNK2BX3xIHM5tqT5xKflLWA3hhs5xl_lZIS_gZK_gn3QJ3hLogaSTRCtxPYJudmBvFYfxg7FONDb88XdDp47hT_8YLcsj3pirZw_bzVRO81tG8JL5OLdDbj6659HxeIvEE90DTMp3bxM4cJqA0VM2nqPXr8rIlXtN_-FpjWUCCCEZflKyVkM6P80AFvs8YAO8XdZvzmku-fXb7SissMHkq2EEduSzeqR8CIkj6mtQ2LDDnv6NIJybZX9ta3qFXHciQ3BMqNS3_2EnlZNhWmmuzmbFd0s3jLN6hA4bbXYvhlVZhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آژیرها در اراضی اشغالی به صدا درآمد   @Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/440615" target="_blank">📅 07:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440613">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEtQ4xoEisQ1kdGI0PfoxYKT3bkglfIA-8tNANov_FpTqcwdq9vPlWknz4SGdHdE9vxuZN1mi4G3cOvBI67W2k_kGO1sPkr_tQxm0GKJSEVtYjO-2dmcf7msRCb7nXS8uFBtWiRWlJOQkopF8j8w7WQBxXeIQn1zvqN_tcpTLXftaF5XZdKOcviT_-wm2vfEvepSrdyNSbnuWvzyiDe80xzeDQdq7Asud6RS0oj7yHJZxduWudAruLGTEMAScdYo-z6SL5aZ7MecVuQ6_WYx7TbpgGaBrwIyeV19apw_XKdfNz-X-H-a7iOmt9WbuIHjLhkeIzdQZkQ0i1yzzAwFoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصارالله از معادلۀ وحدت ساحات خبر داد
🔹
«حزام الاسد» عضو ارشد انصارالله: تهران، بیروت، صنعاء، بغداد، غزه؛ امروز در میدان،‌ معادلۀ وحدت ساحات را ترسیم می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/440613" target="_blank">📅 07:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440612">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
اسرائیل هیوم: اسرائیل حمله به ایران را با آمریکا هماهنگ کرده بود
🔹
برخلاف ادعای کاخ سفید مبنی‌بر عدم دخالت در حملۀ بامداد امروز رژیم صهیونیستی به مواضعی در داخل خاک ایران، روزنامۀ صهیونیستی اسرائیل هیوم گزارش کرد که اسرائیل حملۀ خود به ایران را با آمریکا هماهنگ کرده بود.
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/440612" target="_blank">📅 07:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440611">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
آژیرها در اراضی اشغالی به صدا درآمد   @Farsna</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farsna/440611" target="_blank">📅 06:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440610">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4oT6e15KY8r_fAt9xemx5d59aq0h7SIcfsiG4ysx3eV5lMdiJuPkbFslUHWsG7cld1MGIr6t2DoGhpkMS7CIj960Dgr9g-aXRRK12pykl7Y8y12VarkT4glzUwrgeisCtfooi04jsT0rJ9bOAdfif02z5_-weOauCORfAWHruzywsJOr8hnwLZeb4iytuBrN39z8jkPgjkUY1Tney1ARbi8MpJ9UojEv6YNIcwL20e26CMMy97HfRdYIyIRnQ276dKVH4CZXDHkkeU8COr9F6wJvYMaJ4hmL-JOT_BTffbRCfRIG_TcjJfvUXNCA0I1zk-QugOaXynj-VV8FFqpEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
منابع عربی از شنیده‌شدن صدای انفجارهای مهیبی در پایگاه هوایی سلطان در الخرج عربستان خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/440610" target="_blank">📅 06:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440609">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
عربستان برای استان الخرج، محل استقرار پایگاه هوایی آمریکا، هشدار اضطراری صادر کرد.  @Farsna</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farsna/440609" target="_blank">📅 06:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440608">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a18kvgYs4Q1_lErOmZ2Ue_WM78InKKTY0jgzPhGDR1lano-xfgQGLWs5RUft4vkXTSH3N-SPDLVbVONiLYFMZqK4VhxnEcc0be5JfK_E4YMCz1GxuRpqaCEeJqZgv5Z14KxcTvikHqhELX0sEJ6lRgtjR7J_31N9iT8ZW_xLdfO9nnx30wi0FxwGbgYY3jt_7a0b7UBmlvYMy2voL0hIVAR_V9mEUaSj7_cgWuepQJBKV-rxAqug1xiLqe3qtkqCczo9YQt78YdPSjvqKw9kHcxlRJHpQ4NkmTDLRoCJmSZtnYnjO0OJcNVUrenw4pi82ylhag7EpegjAnqViaDB-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عربستان برای استان الخرج، محل استقرار پایگاه هوایی آمریکا، هشدار اضطراری صادر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/440608" target="_blank">📅 06:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440606">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌
🔴
منابع خبری می‌گویند که در اراضی اشغالی، صهیونیست‌ها در بالاترین سطح هشدار و آماده‌باش قرار دارند. @Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/440606" target="_blank">📅 06:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440605">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8c95296f0.mp4?token=lnVvVy1kgeEZoIWuNM8VEqHfuc7mnVc9fW6LKuaujN37E_v0sr8f7VUci92pwmxC_FdFLVGVEejgooG6Rf1SPbu-7JMZTf6HxjxixM8AbeaKAIEmU_B8XmPCYtIgUS8E7K5fPNL1Z02JAXzYx-GLwMHEpUCcOwuwnMFJDAsBPWi_wRV3Mby4gwcdT8GYUF8rVexa13ZPIjsSuo2Loa2-pNqeNZkTxItbz6kdJe5nADsxEp3pK3YxST9uapjEYsMe6I-VwsXPKjb1dmzbfJGGH2JoORAKZOK-JUdZeQVMZke5eim89BQFrkzQycaASCb8gP6VgIGMN6Zus71om6Efmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8c95296f0.mp4?token=lnVvVy1kgeEZoIWuNM8VEqHfuc7mnVc9fW6LKuaujN37E_v0sr8f7VUci92pwmxC_FdFLVGVEejgooG6Rf1SPbu-7JMZTf6HxjxixM8AbeaKAIEmU_B8XmPCYtIgUS8E7K5fPNL1Z02JAXzYx-GLwMHEpUCcOwuwnMFJDAsBPWi_wRV3Mby4gwcdT8GYUF8rVexa13ZPIjsSuo2Loa2-pNqeNZkTxItbz6kdJe5nADsxEp3pK3YxST9uapjEYsMe6I-VwsXPKjb1dmzbfJGGH2JoORAKZOK-JUdZeQVMZke5eim89BQFrkzQycaASCb8gP6VgIGMN6Zus71om6Efmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زارعان، کارشناس مسائل غرب آسیا: آمریکا و رژیم صهیونیستی می‌خواهند نقش پلیس خوب پلیس بد را بازی کنند
🔹
ترامپ دوست دارد آتش‌بس ادامه پیدا کند اما با این شرط که آمریکا و رژیم صهیونیستی به هرکجا خواستند حمله کنند و ایران هم پاسخ ندهد.
🔹
محاصره دریایی، حمله به جزایر ایرانی و حمله به عمق استراتژیک ایران از سوی آمریکا نقض آتش‌بس است.
@Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/440605" target="_blank">📅 05:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440604">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌
🔴
رسانه‌های عبری: اسرائیل درحال آماده‌شدن برای پاسخ موشکی فوری از سوی ایران است. @Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/440604" target="_blank">📅 05:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440603">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‌
🔴
همزمان با اعلام آماده‌باش سراسری در سرزمین‌های اشغالی، مدارس اسرائیل تعطیل شد. @Farsna</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farsna/440603" target="_blank">📅 05:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440601">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌
🔴
رسانه‌های عبری: اسرائیل درحال آماده‌شدن برای پاسخ موشکی فوری از سوی ایران است. @Farsna</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farsna/440601" target="_blank">📅 05:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440600">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
لحظاتی پیش صدای انفجار در مناطقی از تهران، اصفهان و تبریز شنیده شد
🔹
ارتش رژیم صهیونیستی حملات به ایران را تایید کرد.
📝
اخبار تکمیلی متعاقباً ارسال خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farsna/440600" target="_blank">📅 05:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440599">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
لحظاتی پیش صدای انفجار در مناطقی از تهران، اصفهان و تبریز شنیده شد
🔹
ارتش رژیم صهیونیستی حملات به ایران را تایید کرد.
📝
اخبار تکمیلی متعاقباً ارسال خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farsna/440599" target="_blank">📅 05:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440597">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🎥
شعار بوشهری‌ها پس از سیلی موشکی ایران به رژیم صهیونیستی: سید مجید قهرمان، کنار لبنان بمان
@Farsna</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farsna/440597" target="_blank">📅 04:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440591">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZzBLf_nGHh9rDV_wCcuS46US2fM5rgz1xXZ_Xh2NCGBsgiowvsW4qBVMNV7y7fhCdhheTSlwOpolV6vYey5PQKbRsHs6pas03wcHZAAlKUczmNgUnCScOthdZ9TA67_RVCw2RGTArLXYZJdU0OMMlWbKSNjQ94rzKodvvfmbgjdhPROdTcgalIXMToRbrbl-SxdfpmoM1x0MBXwGbKyeE4tyZmhto2obozQUBKI3brfcwTwzZcnnHb0NepCXqLC6QJOysXEQQ5l7Bjrx7nGae3_rkl8g9HsQevlrKH1GvX-pwnJNvay3NPLJp8w3uYY4KIsPljLJWEWJtHF-rP6V0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vk0_yfJdG3T5rREl220EeMXaYCb5kEQkJWdO02lf-zxafYoxhICakyCog6GizmsNyXmz5iWJTaggLX18pzk0tBkdX3WN4oSx9psXEji_y6kkuoAWSJ2cP20nggk6x1ddutk6gNMQBoFPtkLH32LUMc3rebMFyOfoKEXA7LC0eH4yFd0ixRXWAl53ImQStzDQF2uijJMsk01pxgqxHWwImz8IXC6mz_JziO2U_79WjmSg3jfCbh67r0RxikF0P77QCmjv0ylv0TCuWpYwQyXQ3K9AFCoTuU0okUtQU-eJIUE6ZNiRzVTJoq1vYTnWtovWzF4GbybMlkTsqw_MG-IKPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JT3wQTpruLhY3LTYSEsThRqbprYEoJRAqYN4AzXImd6RyOZYNBAJavO37S-V17yuI8H0yIIR3PNnwdmSPmpcfiNxhiLXkKPsBkrPKC0TaLFvExxSK2BthCoB6SHzhCGxDUrG1YSBpRBOyaxdPt2U0mnGGQk-QJ1U_9vPcJC4bjJ7f7DJfB3AfXPnHc6Y0eFmVQshNF4jx7NL44rkygBupTWcO1jE1XGCjoAETlHcODgoGzWeMY_vAD1dh5zX6mR-42c5pgjbTKKKP5lS9QaktOexlkkWBfnPsNkC25y13F25to6qXBoh2VFA0zlUvL-TWQar_t42Z4WG7I08MWfo2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RxvgUBh6SKKdkXOFwX7JuJosEIsGbPe0RII0BRR-a7xcmP_pGFd0x-AYs2_oDTtxRDy6DciFdptgQJak1uEqvdRD_VGVXnp4kT95JG73yQOPoAh-HWrHDVvpsboJWccYvdzkPALRD2-y_YIgyf987rdMtQlQcvbjwvkI31PxK6ElDQJrqrKtJH2Bk2A4NQ7KhrkcJyG98YGJyizbB62NOhUK086xdTklfOY7ODEOPNOUJLgrVD4LVETYyONdGt4H5glFHnfrpHZGouSrpUsiOa9deaylMtJS74iA5Easea0IcnKjzL8fj0UhsINl_CxxEhOOlT3rmy_0zhxwsTmlxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t3fbdms1f93Wrx_rxKw5dXKjlVnejUhhu0t3DxbjmqTBSKWakgtRG68HDfZPGg9DJjSIq1aJtzZMvJEFg4kkyl-hKMM12meeH6xl5qoAFgd9YRO_Ml8bIJhmZf5vp5gSbtexBseb0NbqJDS5gmkiL-q7h48JLjrUPSCGt0h9F8SfTx1LS9sPqrGdZd0Ubsc118nLO5YzwkB-Y8r4CAS5ObRJA8Ju2ybfDmnsBBECjDzfKW2NuxKIkzcBJkfoeFYqNOymcNV3UrlaJ_h9J2htbb_mgTDEvPB8uth39QzKLOonsayRnHSaz1EYBe-7iz47MRHjB9MBzQuZlGrezfsmJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9WWcXQlAlBMCYf4QNMgnGLIsaO63EYHCkKGYp0lsac-t4xgZvMKkIRPW7QAAmeT4du_rF-zYNDi_D2tmy-DFuipB75FiO9ma7p-hcY3vhhMuMweq0hWCeQh0R2FqzOyWHTTGd1hU_ILlTGDE5g6bj3QNgXzy7fDINW4lIy4TvtnN0IOsbJhTLir0RR3nkZaLZftRBOZl2Gp4J7UpoTYvOzCPQlstgvrImLGAkSqacvrcRVnQmgbgVw6AXErgaUlhz9_Kw2g5RbjsDyuoKLYPo5VIAugM_bsMSF9lOAoDgp87zt3qY-sOVUt7uytxl_GgUjHr1M8dWMab3MiBH5mpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حمایت مردم قم از سیلی موشکی ایران به رژیم صهیونیستی
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farsna/440591" target="_blank">📅 03:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440590">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/486b7ce062.mp4?token=rcdHYytGWxC267kMHkKOyXdDLNpmT_V7vMMJ7Odbf47n0YcWHLlWHOfhC-hIW_eNHOjxDa5tYxq6SxNkOV_QWKpEBnUEmzPWz1GpvbJ2XL8x7_tUvVRpdeYWKWxN4izAG7nmT0Xx5ru1Lem12J2atzPOyOK7DDd-wXM0aUW6vEqJkI_F4dfymnyrrqAutKqDtz4xz9gZIA4MsnFXStLC2tbbcwr6EeOXoTePmNbFV-h_xquZQ2SBnOifxJAcS2_r59RaAprkPPr__cM9tPUrdiLW-MCUBVXgedPazASMl2w4EOYTb6ExwIou38h4ezsa8xfRcAuZqn7GTMjQ3cdJ9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/486b7ce062.mp4?token=rcdHYytGWxC267kMHkKOyXdDLNpmT_V7vMMJ7Odbf47n0YcWHLlWHOfhC-hIW_eNHOjxDa5tYxq6SxNkOV_QWKpEBnUEmzPWz1GpvbJ2XL8x7_tUvVRpdeYWKWxN4izAG7nmT0Xx5ru1Lem12J2atzPOyOK7DDd-wXM0aUW6vEqJkI_F4dfymnyrrqAutKqDtz4xz9gZIA4MsnFXStLC2tbbcwr6EeOXoTePmNbFV-h_xquZQ2SBnOifxJAcS2_r59RaAprkPPr__cM9tPUrdiLW-MCUBVXgedPazASMl2w4EOYTb6ExwIou38h4ezsa8xfRcAuZqn7GTMjQ3cdJ9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با خدا بسازید او کار را درست می‌کند
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/440590" target="_blank">📅 03:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440589">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
سپاه: مقر گروهک‌های تروریستی در سلیمانیۀ عراق هدف حمله قرار گرفت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/440589" target="_blank">📅 02:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440588">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اسرائیل به تلافی حملات ایران، گذرگاه‌های غزه را بست
!
🔹
سی‌ان‌ان: به دنبال تشدید تنش‌ها با ایران، اسرائیل همۀ گذرگاه‌های منتهی به نوار غزه را بست.
🔹
بر اساس این تصمیم، گذرگاه «کرم ابوسالم» که اصلی‌ترین مسیر ورود کمک‌های بشردوستانه به غزه محسوب می‌شود نیز بسته شده است.
🔹
رژیم صهیونیستی پیش‌تر نیز همزمان با آغاز درگیری با ایران در ماه فوریه، با استناد به ملاحظات امنیتی گذرگاه‌های غزه را مسدود کرده بود، اما چند روز بعد آنها را بازگشایی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/440588" target="_blank">📅 02:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440587">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اعلام وضعیت اضطراری در بیمارستان‌های رژیم صهیونیستی
🔹
وزارت بهداشت رژیم صهیونیستی: برای واکنش سریع به وضعیت اضطراری، پرسنل بیمارستان‌ها به‌حالت آماده‌باش درآمده و فراخوانده شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/440587" target="_blank">📅 02:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440581">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wAbB6SZkV--mfWO_M9yHypFhD12VHViImqfp3qhQI0KVamD-ZBcaeCmZf_nREoKkwzZQcd_h0kHTL4Vc6GjbBJIAodX4vkxeDRPljcO3DJdeYAWukuVG3hDOmXWGPUTqMLkwpJjNZGvqLpM0Ok8TW9q9i7xn05fy5AdBF5c2XYxr8rW-ZKeCGwK6MKnYIHZgjHFdpMXGOYmZ6B4fORrjBXrYlrBT6WWk8yC-0l-f2i4mF2YU9wP3XkQQ47uJUlpLbz1SzpjFa2KsQ1TjAV6GBN7cWDP3dDN38ig03mlT71UJ2M4O1_YtdaIYdTjENYXkw1OF4cC8llvJcevwZhi3vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VZ98wFJj58Wgl34PgGXNXza28rReLB4sj-FM6gMxoKRNhRzPOBb7ssXRbrovJvWiG29r0OHKEwRAw_AygUo1IhrnI0rihLHagHpbCMjNC2tKdYmVru6xVbN2snG5C20fYsRGT1Z2l89lew8xvmMQHTcek4EW4GC4QLJy4wzX3JYvo42TBQZbmHvjrW8bgrNgmhZkwyV6c8A3MLuRAhWK9yOpLIx6wUQWZuHMvkvDCzf0i4bkOym5HNjYGGOYEW0sla_QBhk4B5Um1XFdSL7-G90sI3oy2MS0QI97nQ0KmWwdIWlgPAkVSc-nTzg7w2196IhAh98r_fpkKvDUMbTndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxGZ5YB23lnQhYcjwUqyUmt3NQMA0JHUo4xjUs-IAtxZzoacixso1eKI0TyEfxyrOtETpCKL0uz8SXNY9hOGgeMEyvjtPCAaZo9QirG3wIuLu2x5_eHcgvlet1k_M1ol07t2RELAywn22tnyHvhXMFOIipPIF4xb0zonPe4NdFgjtE2wWGbwX701pDmwMBdhUKS0AbTy48e2wajZKrG2QQLgLVhBoQ5KQYiRL5H5h3AV1hgt3PT1YHRfhiVxueL0u_hAcTwHo2I72VawUn6pG3e6TyWmUcuXeAowTUk_4JQB-bM4e16jh2Wugj0ha8tsCL1bM70KUYvx7X7wcTduug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GUyT5OT_4ANeKp7CCsI-3ZhLFBkQq5nx5RF0r9bAABU1MNg4rze0hLX_cSPEPTFK3A_InJLQdpx99bAuBNh-lx3x3ubKxyoot7v9WgNjxk59XJ7RqepaYVDNCVIh4CDvvJunP-aTSLL81W-jtrUQCwdgpYgnwc1xEyZJ2DhywTaMvReC_SoDWltbRRqAPoNCx0Yxy5llLtrK0LZOX01zOFzuoO5hpOVrDRkeRRlHjywTXbJiYCgNG5r_hOX_flwIkQkId3pr51Xzs4cpPFr1E20U2Eg9N3q19MyCJ74v4lao424MKy8PukQrGxiuLJlqyi0k12LpErLi7QH2mMVSTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8JoqjED9lS1Y0neeZq9vFfrOUVbB0VpmOMzqKa-XMmBgnvkbLw44DeNlBXy_bYNEplOSL8AomcfxJNs10OCVw7nFujalqVBdF5LYn308gLH-7G4qEboWfcd7X9Gcsd1tdfzhsWKnqt2aYe6kqCeIneKjoelOc12ClJ07WVXYhKSfv8rZHCgBA5qxGpLebdptyIGmRzcKRhnNWprF6xErWixbXV9UqaMT7lkygQiOpcd4jBUWEfnUyMiMLLPcGPTtDzmyEImi3s7dIxEf-zEkwCC2iN5SKn9dkDuoGoXWeSfiHyy7DAUl2AoJfw3Mp7nmIOH9xE6VnSHeKp5wYZshQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YgncbChVQO8h659bxxw8hWXTeG4dL3una8lbr76VDQp3DQg4d7ofQkYmrMlwmJv0460_4lFJlcQWo1Zpa6IWqBCec-OeQ9-WUfzdDswngG3PuI7T0Umbfa-4FSLumuTJ6uP1zOQWXh_Z1fJccMk7gPkiRrs6U8RTLPbh-oGp3RBHBQplvBziazqrMdWb5iTsmX6QC8Zz1qfmXiK4c3b73cyK9-WYckr3C6E0kW6R5Vs6zV0xWNp4DEJn7GKm7kYkgL5F23pQY2ubdUBRNzs-hur9vPelDtxAATZzS6B2MOtlGdwH9q_8GMcEouiAit2UX1UI2kBd-dWilItLa9BCJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۱۸ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/440581" target="_blank">📅 02:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440571">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KVD8oP62wHKnYyCHKMFyagfYtNmwrhKlQVe814Noc1PE9QuRT8HxadQ7zpoiwsWcobUyCaPMuxnSHf5xagzeqdiBPg2867tEkigF7gZPehUJtYsoJf7BN2998ZxtTdEL7hs3pQewTZDg7ocEWU2TNWAx1N3R3huEIKQGe9AwSH8orqtW65jeMD9Lshxt1AUGCXxwNs5JC6NJRHaeKFQ5PFmpKQrX18ng2rGkKNrb2ZlNUA9T2i1od8K4s8LAOBXATUNsuxqTS7TJouyJMwNvOxX9xj9v17qF1UHqXzMMmOB8ky5tsGro3JtNOL4sfnMzvmAfEIdiaX-3r5tSZCHSSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6ewJm1i-tyeM9TAMJEYn75KIjRL1dSHneQoBfBOm1DR8Z1uGgW54bBGIfFQooslU1kHYDs5Tl_090b5jka8-i8aI3BdqfqdKTMx1SBv9Ztil2QNPXvY0ls8wZR7KrwlnqpGCNs9wBMZGETdIv2lND81PUyDU-UMH7tNjqcJv64sSzrNzKW5jkGbI0Og7_B9pDg-bge5P0UM6WVQzL1tFKI3A2w8cdLS-S0iZVnWFT2qxD9BQsJtyBYm5I41r0n1WwTl35mY32fbO3G2Wugcb59dSaipNguRHPdB0Ctpzr0qxT1qBn1kkfbHlpTKI8gKeyYFNkbzPNwEHtN7LuWpMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFDEHA4J0MzFOL8L3rhExpqcB7vYWIo6zyOVzKbg9qs8323viYV5GaFYT9VYA-N5hBkBo_JRF3vKIu5dPWilIkb1zqM7be6cZFXVSQRv0zHzTsuFuZ_Qi8fGquto4UMBF1Sso4R8l3NxreqDM6DbzjJYkStnrAN2se5x_uwaCn5pz4xvmA3avjOEIaUNcPmT_L-elOqkOTJb9VynHLGzaGE0UfoFmAMsFb6O0W5sw78y9Bn8rLyleQT5UIkGfRTjI42zkaMcLwLif7TInmkX03wB9lNFW3twu9N363Lx5dYEIqreHSYvneA_cLb2fhzkvNoeTxX-AIxC82IkqlvADA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGdMY9Z3W_gfaYpEDdd9ONeDHUwtQPn7SM5jSaM3iT5oAuVKnqfbkjv3F_hqrzv4BGo9OX76WidannbJJ2ZvLoxWOVpQKpIDWmL-4ufIfa4IZEwM4g0ZmAiJNPwnK13gjCeh7slKFYu3V5j-sZ0HN3ZtHU5_ACNNeJNegTGueLXNAjqow2sOqPjytkyp60qrVJj4iGqfcgGstvnUVaiQuGqNghOfA8TCPo3S8dV005BkFpxzQ3neofR74IqKq0sJOgFVDeAsaTsjSii7FWwjXymAaXtW5OlSrm-SyaKJALIGRQGcFpuORzjMdXQsLixJSeyvcdQluv7Zt2e-_qu0Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DpA9_Z31fxbTf4mug5EFE_4Hi2cbTclSxYvXEwsL4L7WLcte6q_Koz1z6fB9FSmyNorAJ0CPPWTDwyS__lw7pd-mAMlwG_hKkHL5tv01YN_KH7Lf95nV4rVbIMrNNqSdNz2HNv2c4SgwCASpkdsY6K6rl-n3VU6-ugUuuAqvBbVB3y43LgW09cIhvJQScnqyXkTrwOwYTIZVD7xjDeLbD5DVdoro3XNvEj-rzeiUBto37IpSx606irj3oilXD3XqdavV_D9TOpyH6lQzd4HuJZ0ppBOAk8L12een7D4mRFZHu3PNKILtJlf_mu-bZZNCTC6Ul-6UQmI0vGEG0UyaZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxILYMAzSy3z7NF8hhA0JwM1u-kc-Kc5hONaOVWKwas6F5t4P61f0GZ1J3WyxfZutlRYUdI-BaCRSy1kZG1edrQQmEwQXvOhx9LntfeYh3FWZrHx11kyIi0KOeEJmqq-aWYYCycCqM0dZwiLUTOaIo2PeSUI3U9iQAAF3LzhR8UJvrlozYFbZZ5sRyExK10ZLwnTTqZM2NQKaXJrVksc_eNzBJ1FF8zazcpFBlhO88P99Lsf9FfhgwTI3L0uWkwgbWKE8zOCEblBTZ4e5GY70Su9C7SyJ7cxAsvSCEyprjATZBPBPjL4O7YmmJ8YWA2y7VXajFzBLQB_b1SOodqRXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0PQozQnsHD3Zjpa3xB04w02LVi-2iK7iwUo-bQSkVVCm2AiCWRbJfqpji-HqYJ3wEzpAV8QC8UqURE0l3H2uyQ8aC6s9lwxYGE6zFDFoQvst3sFAweEAnDuhLLeJSBojjgGu33ml5cj1wvzXVulFFdwocwCmyXt6Ee9s48DXUF5IYhERQ5hI-BdAzDyC7R9qEZ5Yd6iGY8NT2i5FgXK_KhszfbhTvYtahZYMGCNSybRiCvHIZrvF-SVquVXaXAYRlygeeHeP_dvSLCpuM_ArYGA2eGy-EaVrTMxUxrOQR_qlYNfTRs4tZoZp7AMgtreVIEi_AEsiCr4SEuuxW5dKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhrOJQfJildGh57UNDMOqnlyWr6rRXuxwVaWeWPsNC1mW5t6-TJMf29bUMyPML6HTQnLinNbBHsnqKcLPUR9OTyGdwZTFdgTXDb8AOzh2U1s6LK-85mTC1sBPWl4eRPVEPw_6Xu2sa4OAKvMl2fcAIlO7eiqUi9FH7rSvRCQWGQFImJgKCLu9mU53HyUsavfvNVhuyEwXSkeuYfI5iAaaWADhcrolZavJKiBtz8zJ7VBvE5VtD8tR4MzLGSPqcc61wq3olT3ticgFwTa4P5ZO6_6aL0dSJtR122btQ0LJf5giv-y2W78tQCxbHuEFpioyLD45R-KPeKLY8Cu9WrI5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_2EvU7ywiHu9o97afJusU5jcIKSZK9dFQGxfqWjRCzkVrRiwguRt4e5QlCp-pqbjlDYWHP3bNFlN7qhghXWlZslmCKA2p4UCnVs7oLe6F4Wbw0xPSIktRVQkYPyKwXM5o-lcsKXgcOSX87sg34OR8cQkWNAICeThb-ZmABQq8ffnXRNA3oGQjGddM0htejBfeB3atAc3JCI50owSvBD4Y9IhfmfzU9oD5R8CUuM7jgtu2Fv1OMzOj1qvsR-Wtvrhye4i5YXoXTDkirpJhUfAFSH8AKyVa1mhIlLxZDCu3Q7UOXr964QDoRNLgrUza4mLk7zIGR1dUMZO2icalg3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTcmDT1WdGsCFXmvux4n7Nj2zZ5h0I8AI2JAaTqjmBsuxGHITsANDyipB81ifwaSXmG6DayiF33K0x5lx7gVUnCRQpk95SNldnADZaYiTnQWFggCOZHePbT98DLAcfs1pSmrmbl0TGdH867_o2Lm2II_IIa5dLeuWkS7wo1tj9hCyFmIfg99RAYopZTc4p3mF9RCWVggImXkn-y4IJPbs1E5Q9Q_fRkoNUyBMZadfqZIGf9KqM6TiStiwt7GoyL-KqX7Xzirb1_3NVfzh86dlUuIdgCGJRXiqcqkdHqIQ5_bxM79wb_9FJ5zAm6S6q4_N4loKlyKm2oHwOphRi--mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/440571" target="_blank">📅 02:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440570">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a8fb8a764.mp4?token=bAxfwtXWdQwhnjnOfOKPBT0nPZKX-VSXDI3SC5rg5fXmYsxrAeHbGiZr5D3SvVWNdUqJxYDUX1wjnTWTAK5i49pLZE5GHTYGJcJRIqm3vmW7KyvoEUvYYetY0udH3iJLAIh90fDaCI_aR0mxlUyzUIJAxAleKr6mMfgxbDKYq4hc1MR_j20CBqu8svd4sX0vYALqGCzexInMe77AMHlaayPfEpUQrZvEScNYSrRD_3wsWfFqtYZc4qszKkfOLrYVDdNoU0yaeNR2q6kX96Zw9iEfzSkUcCpF4fOv-92vSD9Ol04k1UNOdAswXvdY21oA-xqXGSdQP0oC87pnjyjsrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a8fb8a764.mp4?token=bAxfwtXWdQwhnjnOfOKPBT0nPZKX-VSXDI3SC5rg5fXmYsxrAeHbGiZr5D3SvVWNdUqJxYDUX1wjnTWTAK5i49pLZE5GHTYGJcJRIqm3vmW7KyvoEUvYYetY0udH3iJLAIh90fDaCI_aR0mxlUyzUIJAxAleKr6mMfgxbDKYq4hc1MR_j20CBqu8svd4sX0vYALqGCzexInMe77AMHlaayPfEpUQrZvEScNYSrRD_3wsWfFqtYZc4qszKkfOLrYVDdNoU0yaeNR2q6kX96Zw9iEfzSkUcCpF4fOv-92vSD9Ol04k1UNOdAswXvdY21oA-xqXGSdQP0oC87pnjyjsrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد قدردانی مردم ارومیه از رزمندگان اسلام؛ دست خدا یارتان، علی نگهدارتان
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/440570" target="_blank">📅 01:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440569">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_7ZJa91rzR3InfuC_k7pl5rOk7lzP_LYrJateHFbEvYpZi5z0BKXB96F9o1vHtlrKdrsUAm0JJDQUsJ8inokmcg8rlWu4JvXxcl3Tr3sDMapxRIQDzHVv4lkhcno5uQbCFVH_DD1EDL2-qkTR0FtRcSMA_rFm7Ly9igJR4h6bKkld1uSzFgjaWrhvfwEUHvM-H9p9h3a0Gv70tunPHvgCE8pU5Egl-XoOhk-9Lff6Eba9uEtJQgJsQRyAKeckhls-KiiUjp0pJSlLHJq9wHy7FPJy2wzJYNxKmsQYBpu-xIhvtXZr3SIuib72sE0lQWoknMZB2aSAZSaJxmPuI5HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
توییت ولایتی خطاب به آمریکا
انتخاب با شماست:
🔸
توقف حماقت یا ورود به موازنهٔ ضابطه‌مند‌شدن دو تنگه!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/440569" target="_blank">📅 01:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440568">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎥
لحظۀ اعلام خبر شلیک موشک‌های ایرانی به سمت سرزمین‌های اشغالی توسط سخنگوی قوۀ‌قضاییه، در جمع مردم تهران در میدان تجریش  @Farsna</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/440568" target="_blank">📅 01:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440567">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ محکم بزن</div>
  <div class="tg-doc-extra">حاج ابوذر بیوکافی</div>
</div>
<a href="https://t.me/farsna/440567" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
محکم بزن، کفر و شرک رو باهم بزن
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/440567" target="_blank">📅 01:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440566">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">زلزلۀ ۳.۶ ریشتری هرمزگان را لرزاند
🔹
زمین‌لرزه‌ای به بزرگی ۳.۶ ریشتر حوالی بندر چارک در استان هرمزگان به وقوع پیوست و در برخی مناطق اطراف نیز احساس شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/440566" target="_blank">📅 01:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440565">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630a9342bd.mp4?token=qiofLE0d5pyDqCQfGUGRksad9_D6STcxsfG_Wa5UjAgf4UbdjpgM0lBTBiCe_4QHNhoUfv4q_H05kL_WjRUkRZfvh6ctn8GtFpQVNevdrloeoUlSqzh8ZQR1OXAHk3W7qhlhGrGhJKguDN94JYcHmz-a4j2u3oU4hD170HDOz2eoaOraQP1Dq6l4103fdhZ0MYVEs2C_httTTZCWGkeikaZsx7-Kq20MDD5ex6F91nQJrNlhpu8rer6C6RcMibtk0PYdQCZLTcaEadn6eYXpgUOsNAZl-DkicDjymCU1Xkv1abOpWcPy3j35Yg6-dgcoKaVzBITJWSiz8pkz4wqWtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630a9342bd.mp4?token=qiofLE0d5pyDqCQfGUGRksad9_D6STcxsfG_Wa5UjAgf4UbdjpgM0lBTBiCe_4QHNhoUfv4q_H05kL_WjRUkRZfvh6ctn8GtFpQVNevdrloeoUlSqzh8ZQR1OXAHk3W7qhlhGrGhJKguDN94JYcHmz-a4j2u3oU4hD170HDOz2eoaOraQP1Dq6l4103fdhZ0MYVEs2C_httTTZCWGkeikaZsx7-Kq20MDD5ex6F91nQJrNlhpu8rer6C6RcMibtk0PYdQCZLTcaEadn6eYXpgUOsNAZl-DkicDjymCU1Xkv1abOpWcPy3j35Yg6-dgcoKaVzBITJWSiz8pkz4wqWtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نظر مردم درباره پاسخ ایران به نقض آتش‌بس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/440565" target="_blank">📅 01:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440564">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یمن: پاسخ ایران معادلۀ «تجاوز بدون پاسخ» را ناکام گذاشت
🔹
پاسخ ایران، معادلۀ وحدت جبهه‌ها را بیش از پیش تثبیت کرد و تلاش اسرائیل برای تحمیل معادلۀ «تجاوز بدون پاسخ» در منطقه را ناکام گذاشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/440564" target="_blank">📅 01:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440563">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJ2zIpKtSNaQCkUuxDXMXO5z9jMWYVZlRUpIuNU_emzPfMVgvBwrWG2Ct4_NIFxkPVaKacP4CpfmKk8Xhgu4dFxUk51uY6IaHlLsWBnWDTq17kJ-F_GaWfnGFDU7Lmn_qUNrF3x-cD4x4WaHsC412bKD5QcT6se9m4Omi7l4P8Bbl1fbCA3EIF21pBxBEbo_5HVbrqwhxJL7xmmR8rIYtJItYxgqDfP1y1wabmfa6x-ucFKgZ5Qi_sRIE6EvesdMPh51lH1-BsqmM3p_6KDviCGPovpTkO6gckfUv8zNVaezRVXMe3hhqEEipGOdAMYs7AbqqQxRfFcsMMX4655Tog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی کمیسیون امنیت ملی مجلس: به حملات رژیم صهیونیستی پاسخ قاطع و دردآور خواهیم داد
🔸
امشب آسمان سرزمین‌های اشغالی را ببینید. @Farsna - Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/440563" target="_blank">📅 01:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440562">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93d0986b0c.mp4?token=Jwt2t_1aHdpnHGc2QGYFGZ-Fbce-qD28HaxSjxTDZEiS05oaI8smrMmGttyvn3XWbf5kbB7HMi8bh8XYxIJmY2EzY4pkyVNRdxR2qned4Q6eFRLFNK5cVBLDO9U1wC8uYL4IM-zSgKQ8E8v3JiCaOjtbpyGjFGx4ww_oAMoUh1FLK3JAcaBSJ7cEC_chRHi_jG3XXe3R7QGNEOjBr82K4dAye9ihxYY4rbzLPN9W9WmwEqH3E50XUaTgXklneRqQgn9piecD08Tl31VVojb88eB2SKijc83tcjUvuSrpIvMqrRt2ww_yQ_yST581tIp8QoUb_bQAHZcXTKe_utCfSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93d0986b0c.mp4?token=Jwt2t_1aHdpnHGc2QGYFGZ-Fbce-qD28HaxSjxTDZEiS05oaI8smrMmGttyvn3XWbf5kbB7HMi8bh8XYxIJmY2EzY4pkyVNRdxR2qned4Q6eFRLFNK5cVBLDO9U1wC8uYL4IM-zSgKQ8E8v3JiCaOjtbpyGjFGx4ww_oAMoUh1FLK3JAcaBSJ7cEC_chRHi_jG3XXe3R7QGNEOjBr82K4dAye9ihxYY4rbzLPN9W9WmwEqH3E50XUaTgXklneRqQgn9piecD08Tl31VVojb88eB2SKijc83tcjUvuSrpIvMqrRt2ww_yQ_yST581tIp8QoUb_bQAHZcXTKe_utCfSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شنیده‌شدن صدای رعدوبرق در آسمان تهران
🔹
براساس هشدار سطح زرد هواشناسی، از عصر یکشنبه تا صبح دوشنبه در برخی ساعات در تهران بارش باران، رگبار و رعدوبرق پیش‌بینی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/440562" target="_blank">📅 01:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440560">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e30d14c42.mp4?token=c2dNMVPVMBwVuYM4-7O_DC7owtrpQQi8zJo8wvzTDxh-3zHtlmF6z-vGSRm5PgHc88clYo5NSJWnylIqfN-3bCebvdIe51NB1-RR4soyDjLzru5oHReY2K9B7OqcR8hI4PPEpuiEUB5qQ2J4BCSbJzrAfTPB6cTdtQSyGk3eGHnTog6rT5Plabb-DsasuTJFRr709UVnTIXBWQ0cI0-9A8ke9n9H_QxAbUZBbCPAUV0kbNzLGVF33fFnftvQHexqJONGwdbUuGZKuKfQlWSwRzas34rf2uS8d-PvU_SooLN0DBhLkG_zGyD8RwTB6b27KziexY9sl_7Z3BA0l-JDQzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e30d14c42.mp4?token=c2dNMVPVMBwVuYM4-7O_DC7owtrpQQi8zJo8wvzTDxh-3zHtlmF6z-vGSRm5PgHc88clYo5NSJWnylIqfN-3bCebvdIe51NB1-RR4soyDjLzru5oHReY2K9B7OqcR8hI4PPEpuiEUB5qQ2J4BCSbJzrAfTPB6cTdtQSyGk3eGHnTog6rT5Plabb-DsasuTJFRr709UVnTIXBWQ0cI0-9A8ke9n9H_QxAbUZBbCPAUV0kbNzLGVF33fFnftvQHexqJONGwdbUuGZKuKfQlWSwRzas34rf2uS8d-PvU_SooLN0DBhLkG_zGyD8RwTB6b27KziexY9sl_7Z3BA0l-JDQzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ مردم به الوعده وفای سید مجید موسوی: خیالت از خیابان راحت سردار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/440560" target="_blank">📅 00:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440559">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40243c0011.mp4?token=H1vTb6f_NnJVlKNwZLF5RR3vq4wAh7cg23K1AYnz9JUIRHjQRB1tN4FKYpMPubwW4I3pP1TOFFKI7DHze9C6q6ZdprrPbBA8c1xnkkeCqARsU7re5RyjgudwG1WbPxR-xS3OWJDZDFwi1WAS0Jbtkqw_ID1LiP8ioVFNYthGcGX16zXnPHx0s0ocnmJ_k6XNG3Tt-WycbaSXIYUY1qyfd_HH2LLB4W1t-Cn_o9zWRHwrUQ2OgRxRk9MBNJPwQ9R8e1WURmRdF_mHNpL9HEtp64jAmrKH99rpGA5QakfXx-eCna2RbZhxG2CCtFWGlOJZEnCsW4NlEOXHrn3_Y_R1_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40243c0011.mp4?token=H1vTb6f_NnJVlKNwZLF5RR3vq4wAh7cg23K1AYnz9JUIRHjQRB1tN4FKYpMPubwW4I3pP1TOFFKI7DHze9C6q6ZdprrPbBA8c1xnkkeCqARsU7re5RyjgudwG1WbPxR-xS3OWJDZDFwi1WAS0Jbtkqw_ID1LiP8ioVFNYthGcGX16zXnPHx0s0ocnmJ_k6XNG3Tt-WycbaSXIYUY1qyfd_HH2LLB4W1t-Cn_o9zWRHwrUQ2OgRxRk9MBNJPwQ9R8e1WURmRdF_mHNpL9HEtp64jAmrKH99rpGA5QakfXx-eCna2RbZhxG2CCtFWGlOJZEnCsW4NlEOXHrn3_Y_R1_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شادی مردم لبنان از حمله موشکی ایران به انتقام حملات اسرائیل به بیروت
@FarsNewsInt</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/440559" target="_blank">📅 00:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440558">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
آمریکا بخش کنسولی را در قدس و تل‌آویو تعطیل کرد
🔹
سفارت آمریکا در قدس به تمام کارکنان آمریکایی و خانواده‌هایشان دستور داده است که به‌دلیل وضعیت امنیتی فعلی در محل خود پناه بگیرند.
🔹
سفارت همچنین بخش‌های کنسولی خود در قدس و تل‌آویو را در روز دوشنبه تعطیل کرد.
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/440558" target="_blank">📅 00:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440557">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌
🔴
وزارت خارجه: به‌دلیل نقض مکرر آتش‌بس، چند هدف در شمال اراضی اشغالی مورد ضربه قرار گرفت
🔹
متعاقب نقض‌ مکرر آتش‌بس مورخ ۱۹ فروردین و تکرار اقدامات تجاوزکارانه رژیم صهیونیستی علیه لبنان و جمهوری اسلامی ایران، از جمله از طریق همدستی با ارتش تروریستی آمریکا…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/440557" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440556">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌
🔴
وزارت خارجه: آتش‌بس در لبنان، بخش لاینفک تفاهم آتش‌بس مورخ ۱۹ فروردین ۱۴۰۵ بود و دولت آمریکا مسئولیت مستقیم در قبال نقض‌های آتش‌بس از سوی رژیم صهیونیستی و پیامدهای مترتب بر آن و نیز هر گونه افزایش تنش  در منطقه دارد. @Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/440556" target="_blank">📅 00:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440555">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
وزارت خارجه: عزم ملت ایران برای دفاع قاطع از امنیت و منافع ملی خود در هر نقطه‌ای که تشخیص بدهد، جدی است.  @Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/440555" target="_blank">📅 00:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440554">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
وزارت خارجه: عزم ملت ایران برای دفاع قاطع از امنیت و منافع ملی خود در هر نقطه‌ای که تشخیص بدهد، جدی است.
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/440554" target="_blank">📅 00:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440550">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c94c65b6.mp4?token=Bi8lXruyEu1CzDFstFCcCKt1tfM-Z2uQlVtB4BfVM9FagF48WsDYCciBcfgugVtajRprCgiz99mPNee2Dc7QV6_ORYezsps_ns3XUhtCsEaeiXA_B-CXH5u2eGBTX_WDotSBgxp73AktEv_OFUbR82bMK5uX8bzx33AZdFGYvgLpjMu4EmgxAdvzsf67UlUwI9EVWL1qNUrR4cHv9aUVuivWizpcsiOm5iA2VauO8ZIE88y8GAKrmyzifHDu534UuZrEUBTODT11krrFqxZgxkiSekzO3AXAtwAWMMSOAEutqUkpWkvl7yTqtav8vcXlxwsGnWVLeqyj-o58vyR_Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c94c65b6.mp4?token=Bi8lXruyEu1CzDFstFCcCKt1tfM-Z2uQlVtB4BfVM9FagF48WsDYCciBcfgugVtajRprCgiz99mPNee2Dc7QV6_ORYezsps_ns3XUhtCsEaeiXA_B-CXH5u2eGBTX_WDotSBgxp73AktEv_OFUbR82bMK5uX8bzx33AZdFGYvgLpjMu4EmgxAdvzsf67UlUwI9EVWL1qNUrR4cHv9aUVuivWizpcsiOm5iA2VauO8ZIE88y8GAKrmyzifHDu534UuZrEUBTODT11krrFqxZgxkiSekzO3AXAtwAWMMSOAEutqUkpWkvl7yTqtav8vcXlxwsGnWVLeqyj-o58vyR_Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
نوشته روی یکی از موشک‌های شلیک شده سپاه: ما درحال مبارزه با فاسدان جزیرۀ اپستین هستیم  @Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/440550" target="_blank">📅 00:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440549">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02f9735a5a.mp4?token=JuYQt8i1PngsqUxb9XT5JOfCPul-DZKIiy8OIb6bH-UKy6BMBDSLRTEVieJMveUPsngPk1-bLmgulmIqnGoTO3HWzs49br1DwdJNEA7zoQfvrkDhSgAEzmtJJ0ADl1J96V-WQrAoe-q_Bdg1TdzsYgS5PYywgiKrXAU9SFy7upeZ6oF-erefF-WdG62_iaMjOEKiQQ60Z23ocIrRWN09XmleBg0I2X45_oiwutTZ1M-t4bPZig0qcL50L3uiEOlz5dWbXUBELrp1udY_3qQl_Pp1XXKTu0igEVm3hXFCuch7Nm07TqvBgW3WQTqMjV70aEhAaO1_7NcJ8-6iYJ-qDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02f9735a5a.mp4?token=JuYQt8i1PngsqUxb9XT5JOfCPul-DZKIiy8OIb6bH-UKy6BMBDSLRTEVieJMveUPsngPk1-bLmgulmIqnGoTO3HWzs49br1DwdJNEA7zoQfvrkDhSgAEzmtJJ0ADl1J96V-WQrAoe-q_Bdg1TdzsYgS5PYywgiKrXAU9SFy7upeZ6oF-erefF-WdG62_iaMjOEKiQQ60Z23ocIrRWN09XmleBg0I2X45_oiwutTZ1M-t4bPZig0qcL50L3uiEOlz5dWbXUBELrp1udY_3qQl_Pp1XXKTu0igEVm3hXFCuch7Nm07TqvBgW3WQTqMjV70aEhAaO1_7NcJ8-6iYJ-qDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ اعلام خبر شلیک موشک‌های ایرانی به سمت سرزمین‌های اشغالی توسط سخنگوی قوۀ‌قضاییه، در جمع مردم تهران در میدان تجریش
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/440549" target="_blank">📅 00:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440548">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEI02u3gkK801RpA7uPJvmwkNvpKvYaG1n_FcGx7qK_NOfzbVn4dVKXJ45rF82MsTHFPvGW0_f_wNgjeZu0HS8z9FFuXcBAnh21V8-972JsNSaKzSg6MOhqitW_-ONoT41gyI_swuJIFwTB7I4ENj1CFocuXroU0CHW_y0gaqLl1gIwCSJijMswUiDjB7AxZYoCRxu2A50ERuMLOIczQq3oxDg5_79o-IF622DkrGTLcNYSPd-i9NbsXlMzSqs7NpY5do-af7-b5Zk-woC7BVRb-Fh_hTC0yq8_c6GmSLm6l0PfTR3r9wClVjTtp-cctQTv7Eui9yiCLRO_ssmp1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نمایندۀ رهبر انقلاب در شورای دفاع: صدای خروش ملت ایران را در آسمان تل‌آویو بشنوید
🔹
دریادار احمدیان: این صدای خروشان ملت ایران است که در آسمان تل‌آویو شنیده می شود، ایران و ایرانی زیر بار تحمیل اراده نمی‌رود. مسئولین کشور با اتکای الهی و پشتوانۀ مردم مبعوث، تا پیروزی نهایی ایستاده‌اند. ادامه مسیر فشار و تهدید، پاسخی قاطع‌تر و کوبنده‌تر در پی خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/440548" target="_blank">📅 00:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440547">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">استاندار کربلا: جسم ساقط شده در صحرای کربلا پهپاد است
🔹
سازمان هواپیمایی عراق سقوط هرگونه هواپیما در کربلای مقدس را تکذیب کرد.
🔹
نصیف جاسم الخطابی، استاندار کربلا نیز اعلام کرد که سقوط هواپیمای مسافربری صحیح نبوده و جسم سرنگون شده یک پهپاد بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/440547" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440546">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15ba3375c6.mp4?token=OIg9AUX33aD1Tjaac12a03gxACeLIo_-N3-irlSGyvHmrQLjf0JL1wlqVXvvsQQh5_AZbpNFSKvFzimzshf0SNl4bCRZeIwLI3D7kOeTkF59Rxj3qT6Hr8kZvjEmQozA_GVXzGKOWt6kKygRkAxjcyLD8YAaKZLSbUknmbXz3LCwL4uJihfna6qG_1mMoEF9msRba4EVNoPDvcdAttAEpdDIhky6ANVxp7_PdpxBysjGTdB7A15Mam4QBkgcoApnMtXWZEZtBjrzduV0p8iMUIoFW1-a9HTwpcUo6AXKwFnDrF4mBlbbkHHBtD0ToE9ixCnlB4hli6blrndYO0c39Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15ba3375c6.mp4?token=OIg9AUX33aD1Tjaac12a03gxACeLIo_-N3-irlSGyvHmrQLjf0JL1wlqVXvvsQQh5_AZbpNFSKvFzimzshf0SNl4bCRZeIwLI3D7kOeTkF59Rxj3qT6Hr8kZvjEmQozA_GVXzGKOWt6kKygRkAxjcyLD8YAaKZLSbUknmbXz3LCwL4uJihfna6qG_1mMoEF9msRba4EVNoPDvcdAttAEpdDIhky6ANVxp7_PdpxBysjGTdB7A15Mam4QBkgcoApnMtXWZEZtBjrzduV0p8iMUIoFW1-a9HTwpcUo6AXKwFnDrF4mBlbbkHHBtD0ToE9ixCnlB4hli6blrndYO0c39Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه شلیک موشک‌های ایرانی به‌سوی اراضی اشغالی  @Farsna</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farsna/440546" target="_blank">📅 00:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440545">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حزب‌الله: تجمع سربازان دشمن اسرائیلی در مجاورت قلعۀ تاریخی بوفورت با موشک و توپخانه هدف قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/440545" target="_blank">📅 00:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440544">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKNwZefe4BiSgvBhrdcCe3LVmDdMXtIhDjbCdCEAETdxp-IlEXJ7nQVO9qr_voIu89MmB6kV_4VsxAn26huR6JVZwhwn7DxrvSHADQgjBp6uU0xjqIo8-TrlsZZ6jWTp3Y_nFHEede-oixXVmGnkhMIwJmRKl8aP196P82RPBBI1dDYGm5Dwx5STDuer7xSjJQUeLuTNxPMSvxBi865SZnC0_P9mP1uG6-y-oJMtIPLmpOotkAkL0mrUT7PEVHFLH2RZWju8GreuObuZw98f9adbeC7KXiPUEJzzCnYLH_pzRjtorsNUOza1zPoNtfeyCLOmNUQGsZWJJfAlo8LWpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تماس‌های تلفنی عراقچی با وزرای خارجه انگلیس و ترکیه و عاصم منیر
🔹
سید عباس عراقچی وزیر امور خارجه در تماس‌های تلفنی جداگانه با ایوِت کوپر، هاکان فیدان، وزرای امور خارجه انگلیس و ترکیه و فیلد مارشال عاصم منیر فرمانده ارتش پاکستان در خصوص آخرین تحولات منطقه‌ای در پی پاسخ ایران به نقض مکرر آتش‌بس در لبنان توسط رژیم صهیونیستی گفتگو کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/440544" target="_blank">📅 23:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440543">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/831ee271e2.mp4?token=cr33BLNBL3gQqoUHDP8ZYVxDQ2Bz9KFrIY3q41mhlD3z6MOlNzjj1vvXZO-hAsUEbIkgiCDJvZiUe3rvrm3q_HFae0A1jZuLnlS31yhcqhYtmS_Sr9mcKVAcjgt7HY6tLLWLj_0cqyLi2IKYlg-fbTntltoE6EXff3NS6-_ECT7I-HybxKx1BNQEFUh2X_qYsxgryKI9ZrqnIU5jxK84HcmVhSpPxg79Xkomn669oYZBZJTSVTs19YhQWVF78ZKbIxOL9t5O7nKzB0nF_cMGSzhBZroDD_x7hhnHupIz7jwPsLaLvmsu-5zLuE_AfGIKY5m59DfkLgkMp0uVcQ5Nng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/831ee271e2.mp4?token=cr33BLNBL3gQqoUHDP8ZYVxDQ2Bz9KFrIY3q41mhlD3z6MOlNzjj1vvXZO-hAsUEbIkgiCDJvZiUe3rvrm3q_HFae0A1jZuLnlS31yhcqhYtmS_Sr9mcKVAcjgt7HY6tLLWLj_0cqyLi2IKYlg-fbTntltoE6EXff3NS6-_ECT7I-HybxKx1BNQEFUh2X_qYsxgryKI9ZrqnIU5jxK84HcmVhSpPxg79Xkomn669oYZBZJTSVTs19YhQWVF78ZKbIxOL9t5O7nKzB0nF_cMGSzhBZroDD_x7hhnHupIz7jwPsLaLvmsu-5zLuE_AfGIKY5m59DfkLgkMp0uVcQ5Nng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش زنده خبرنگار بی
‌
بی
‌
سی از بیروت؛ موشک‌های ایرانی موجب خوشحالی و هیجان لبنانی‌ها شد
🔹
پاسخ ایران خیلی زودتر از انتظارها انجام شد! همزمان، حزب‌الله هم رادارهای اسرائیل را هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/440543" target="_blank">📅 23:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440542">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r01O-UGFyJgddnos49BL7_5PPNM0lc_8fE7kMFw20YnJ4h6eO4JBZwgDYMdgpt8YnmJPRo7yDhhttegEfGZrOkrAShgOCcrQiJDRpA0mtYy8ztX-4qJCRcU0RX-VtLvyHjua-VYRj4xHnHIp0tdnBDYUXbqSFZq8E621fUrW9CsXZqlYOdEPxOUs-pA3frTSRl03KMa3ZFH7pQ_j5dsjPA1lS9_1a0xlUx2mUiqTtsBcEsPszDqqoRZmZpKv-RbAnvstYLZJ8ILdeW7Iw0yQteP0yNAjhKBD59u9IHNbgxSdHeBrpde3ckSrlz8ey-azMUgnawYBOkaAMwvw0UvHXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
لحظه شلیک موشک‌های ایرانی به‌سوی اراضی اشغالی  @Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/440542" target="_blank">📅 23:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440541">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEhyWtMkPcBZHYHe1wFoNIENa3llM2KkzyJDY5YWuCPuTrhUFWXdPDgTymeNdS1a_DoITJ6onHofK4TEikh_NHyeIB4NLUz_EOUhdNiIsAyXtu5zi2CTumihCleQWTpudnGhbdKy_3wUSGgoUpFHgE5dN3PKjgOHGuBlVMvZDz74jVmIzBZNDAo27hW1xoiP05PzT9Xn_wKIdpArUDxb1sfeYfcBzxmGbl04fBuPMYshQZJ3QtvWdkNTCcF0ii-ugfh20Jy2aKyeQPZxKY4RBD5XYUqFlVKrRew76F08c4Mv4pzP6CwF8aTm1X5PDwKRgdKvTcKwQbIWO8K88_UYYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی قرارگاه خاتم‌الانبیا: صهیونیست‌ها در صورت پاسخ به اقدام ایران با ضربات کوبنده روبه‌رو می‌شوند و حملات ویرانگر علیه رژیم و حامیانش آغاز خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farsna/440541" target="_blank">📅 23:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440540">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5132abcb.mp4?token=CZORrVRoMRHd-sWE0PRviAOThDc-5YMDCG6jQJdUQBlTE41UoBFVzb-IDtxepuAA7fi_IGRRnuGabboVskaKkCzWwgCOiGZKRBzZjxvqW_NcCPva83pE3MF-yjF2LbTW0ce1EIU7sLQlySqKH8Erf4NVoCRFNY5PfDyian_ybg16TFuu-j1UebOAJUCiFc-9uI7yvhOzDoTyQDmzGgsgXQCFYhyxDbxl5l_gPBopSM2OMZrci8IjVQdqIweDdMfoEzoybG2p83cis-1x7sHu5RpzkayScAUkS4zaHosU6bPj6AiEOZu73X1quVA2Y-0-y8bJ8yMwxbMtH2vi1DSDgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5132abcb.mp4?token=CZORrVRoMRHd-sWE0PRviAOThDc-5YMDCG6jQJdUQBlTE41UoBFVzb-IDtxepuAA7fi_IGRRnuGabboVskaKkCzWwgCOiGZKRBzZjxvqW_NcCPva83pE3MF-yjF2LbTW0ce1EIU7sLQlySqKH8Erf4NVoCRFNY5PfDyian_ybg16TFuu-j1UebOAJUCiFc-9uI7yvhOzDoTyQDmzGgsgXQCFYhyxDbxl5l_gPBopSM2OMZrci8IjVQdqIweDdMfoEzoybG2p83cis-1x7sHu5RpzkayScAUkS4zaHosU6bPj6AiEOZu73X1quVA2Y-0-y8bJ8yMwxbMtH2vi1DSDgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم انقلابی البرز خواستار مجازات صهیونیست ها شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/440540" target="_blank">📅 23:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440539">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/455b452e02.mp4?token=UgRsuZAaBGVPYqgkx8yTXYCHHwtmBMVPyB963KxdYKo0acUw7_uX5_lfPZHYHccw8VZZ4ljbCoK9v0B983HqJ5r03vkYWwCoKS2YUbjVqwpiYkt-189CqRWndbpkYts4QIb48iNePC7inlpN8VXjH8quSWNP9qepnBy1ARXRSvaUye_hwcsj5eM-p0h2QjL_uy7iRQ06Du9WdM7GtiqLJMKWe98A7eDQbpd5tVmJifph40iAI0YU4lAIdHpr_UXYYnpcKe2VbClpgrQ07GG3UtY_3QsRO9j9sxbDjAWyNcvBMBriJRBq-awEpfJkNpPA9qt_f5BfV3CrJLV1G_mqKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/455b452e02.mp4?token=UgRsuZAaBGVPYqgkx8yTXYCHHwtmBMVPyB963KxdYKo0acUw7_uX5_lfPZHYHccw8VZZ4ljbCoK9v0B983HqJ5r03vkYWwCoKS2YUbjVqwpiYkt-189CqRWndbpkYts4QIb48iNePC7inlpN8VXjH8quSWNP9qepnBy1ARXRSvaUye_hwcsj5eM-p0h2QjL_uy7iRQ06Du9WdM7GtiqLJMKWe98A7eDQbpd5tVmJifph40iAI0YU4lAIdHpr_UXYYnpcKe2VbClpgrQ07GG3UtY_3QsRO9j9sxbDjAWyNcvBMBriJRBq-awEpfJkNpPA9qt_f5BfV3CrJLV1G_mqKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه شلیک موشک‌های ایرانی به‌سوی اراضی اشغالی  @Farsna</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farsna/440539" target="_blank">📅 23:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440538">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oG5V-Gc0zUteRs1oai6N2mqUmm32OYkIBK-oFmrEBRpce0spih4Y3ntCQkGWKoKjkIaqHYU6AXMRJW-QZBT2K-n-YzcpolOpiZY3HybvFL84gqKdnRYEx6AlSGAtF5OhohAJSpQqzX_Y5fhw9Z-juEkEtWKYnUQ8Zj2Oh9UlX7C7ixYmFiaTkMF36qiJEMZbE55KB7k7cda0k6gXUerZjZdLkiW1a8EOUrQ9Iudpagz65mi_XOMwxm1T5fa2MYIPGFHChxDM1hrXBnqH8qpnWnaxaX-gunU1ruYWTFvEChXpDnKoA0rJbmhXhZCC0KP6N3U7cSBRmniWsN3DuZA0VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس: ترامپ به من خبر داد «الان دارم با نتانیاهو تماس می‌گیرم و به او می‌گویم که در پاسخ به ایران حمله نکند.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/440538" target="_blank">📅 23:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440537">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59bcd47814.mp4?token=UagVvGs-pzkC284o982KH6VwXN9cjZ8SLL23J-3sBOi_55QrsVii_hr1YtE4mJiQqIx-WONkGV5E_2JMaDBUvyMqiWIh355ESgKYESuh-SDL0EzuBiuMt41iG6hDZ2H-rmK3YIS_SZQy1jp0XAztJ41SSIhhCrMrW04qtwXlQZhSax2QH1XKjFDvBrKXQQIoz1i9GpN6pJz6UFRYRv2HQmOR9Bx5Pqzjd9ve_116CkTQGcQpVGkzvZD_UJ3zuBnxxyLge0jSH1I3gaUQslCGbM_6RtE86TJwfStwE2QKjfqshC-qJs3HfwmyAEBcbWzIWUTYcIQat3AKZy1uF6fbKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59bcd47814.mp4?token=UagVvGs-pzkC284o982KH6VwXN9cjZ8SLL23J-3sBOi_55QrsVii_hr1YtE4mJiQqIx-WONkGV5E_2JMaDBUvyMqiWIh355ESgKYESuh-SDL0EzuBiuMt41iG6hDZ2H-rmK3YIS_SZQy1jp0XAztJ41SSIhhCrMrW04qtwXlQZhSax2QH1XKjFDvBrKXQQIoz1i9GpN6pJz6UFRYRv2HQmOR9Bx5Pqzjd9ve_116CkTQGcQpVGkzvZD_UJ3zuBnxxyLge0jSH1I3gaUQslCGbM_6RtE86TJwfStwE2QKjfqshC-qJs3HfwmyAEBcbWzIWUTYcIQat3AKZy1uF6fbKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام جدید فرمانده هوافضای سپاه برای تشکر از ۱۰۰ روز ایستادگی مردم ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/440537" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440536">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d98783a22.mp4?token=VLCXVdNOISHBG0QMnQtSmlpQFlIG48-aGWUKH8oalc_mnnjJuIJz3A-eUKEYjT-DdAtDH3w9ytUkKSb9Xq2HEl4lr1OqeC6zT_324BXmRZXS5gdFrxqtBaoXyB1X9FmSmYKjs1RrNZtrp153RY2Mc82zEIcviOYndp4uTTOk9M9EBkMpupHnk5BZXc3rXfGhBfdzw74dYA2vn043KkiU10wU6w-d5rYLMHhUgbQXPLnPkIWVoabEYaBjK-DFpVMo9Do89hQ21V3m4YvhbU4BJX-04-bqMXnZqdkcBVFGimo0ZWnCPHFeG7ocjNJwKsckpjud6TqOhWGkIUMP0IfWhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d98783a22.mp4?token=VLCXVdNOISHBG0QMnQtSmlpQFlIG48-aGWUKH8oalc_mnnjJuIJz3A-eUKEYjT-DdAtDH3w9ytUkKSb9Xq2HEl4lr1OqeC6zT_324BXmRZXS5gdFrxqtBaoXyB1X9FmSmYKjs1RrNZtrp153RY2Mc82zEIcviOYndp4uTTOk9M9EBkMpupHnk5BZXc3rXfGhBfdzw74dYA2vn043KkiU10wU6w-d5rYLMHhUgbQXPLnPkIWVoabEYaBjK-DFpVMo9Do89hQ21V3m4YvhbU4BJX-04-bqMXnZqdkcBVFGimo0ZWnCPHFeG7ocjNJwKsckpjud6TqOhWGkIUMP0IfWhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: پایگاه هوایی رامات دیوید، هدف موشک‌های بالستیک قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farsna/440536" target="_blank">📅 23:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440535">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e388581ab5.mp4?token=iUHUteTGzl2Q8sGfhdhuVq4sk-L_cB2oSQq_fmRp8dBQ7EBa2xcLQcnmdfOXnaNnp0RfwJWwFyfyjfCmIK8D8ylhP8gHS_L_SsNE8VG2RvYHRlvTKdFDWXi_tsOuG7kGobAszsXkOhcPBZKdqzLbRD_dMmwyfxywm_M5zr06Ee1S0kP_4oFDQtBUKeeQOR-J6J0yLFDxvnEuvNnc8g1HIq75zfCX04KJecvkK4AXdwnJVJGwjRwlnuNtJRIJSLlaDJI2kT2sAA-Y76wblB9Sdzv6avtFrqk33bTv2RK7GqZjTy8XD-V3hbFnRUpiX_etqwJ_kCarNxvqtpncU4WEmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e388581ab5.mp4?token=iUHUteTGzl2Q8sGfhdhuVq4sk-L_cB2oSQq_fmRp8dBQ7EBa2xcLQcnmdfOXnaNnp0RfwJWwFyfyjfCmIK8D8ylhP8gHS_L_SsNE8VG2RvYHRlvTKdFDWXi_tsOuG7kGobAszsXkOhcPBZKdqzLbRD_dMmwyfxywm_M5zr06Ee1S0kP_4oFDQtBUKeeQOR-J6J0yLFDxvnEuvNnc8g1HIq75zfCX04KJecvkK4AXdwnJVJGwjRwlnuNtJRIJSLlaDJI2kT2sAA-Y76wblB9Sdzv6avtFrqk33bTv2RK7GqZjTy8XD-V3hbFnRUpiX_etqwJ_kCarNxvqtpncU4WEmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش مردم ارومیه به هدف قرارگرفتن رژیم صهیونیستی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/440535" target="_blank">📅 23:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440534">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/776082969d.mp4?token=oxbQuvIWLLofPZcFodEIvLOl_buoIrAolxCxOIAH4Zlzvc1Uuo4hkEnK3rf3feTgH6Ds65BC2OK0k5M_fiyIhLXg5elRPMeOqbRw5vaeDafSqyaw3-nKdAe5FaS8bSwiklrBIgWT34UGRtWBFcsN-ub3wgKg0zqZEApcARDPs1oSbgPrPi9H2HZ9cj6mtCGXEAVPyL5uhGbIecVdpdavrLL1ebo7oblmd6MXG8vnI1xnmkRYlLgP6B9QW9r6IncAJ678GGF_QiDVxEWjujUjYQep11jXnLvaGrnL2W4YvYjocQQhjDcbq4-9SJxjyWkNMxyDpH_GQUk-ytOeVStowQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/776082969d.mp4?token=oxbQuvIWLLofPZcFodEIvLOl_buoIrAolxCxOIAH4Zlzvc1Uuo4hkEnK3rf3feTgH6Ds65BC2OK0k5M_fiyIhLXg5elRPMeOqbRw5vaeDafSqyaw3-nKdAe5FaS8bSwiklrBIgWT34UGRtWBFcsN-ub3wgKg0zqZEApcARDPs1oSbgPrPi9H2HZ9cj6mtCGXEAVPyL5uhGbIecVdpdavrLL1ebo7oblmd6MXG8vnI1xnmkRYlLgP6B9QW9r6IncAJ678GGF_QiDVxEWjujUjYQep11jXnLvaGrnL2W4YvYjocQQhjDcbq4-9SJxjyWkNMxyDpH_GQUk-ytOeVStowQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها: سید مجید نقطه‌زن، تل‌آویو رو  شخم بزن  @Farsna - Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/440534" target="_blank">📅 23:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440533">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65a8892777.mp4?token=pc0QKNTy6J6H7FuehomX276-YBXpDe1E-0pJieBzE5M7p6c9trvTSI3thMXfOfk36KcyY8xyKiEI3EBNpe70p2h2ecJtKz6jrUCNRfhgl7oB-FBmoCaxDzs4TePQJYJc9idjU8wk1NdFOpGZrhFzsw9_dN1LpwNQ6hPvRLUje09elSoy4ImFvb67ce5yd8yDgJ_U1xzM637nLoOa9T9m9ouvIt360kjheixICJUfHO2wKuQNf-vMquzClaYwSb4CGIGU05h8I-_D306XaCFc3VhOfPwjUW1t_4T1nyOIDUwz4Cdscm1H_HvFiZuXU1p8SRBDDFGGyNDoVl6mayZDBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65a8892777.mp4?token=pc0QKNTy6J6H7FuehomX276-YBXpDe1E-0pJieBzE5M7p6c9trvTSI3thMXfOfk36KcyY8xyKiEI3EBNpe70p2h2ecJtKz6jrUCNRfhgl7oB-FBmoCaxDzs4TePQJYJc9idjU8wk1NdFOpGZrhFzsw9_dN1LpwNQ6hPvRLUje09elSoy4ImFvb67ce5yd8yDgJ_U1xzM637nLoOa9T9m9ouvIt360kjheixICJUfHO2wKuQNf-vMquzClaYwSb4CGIGU05h8I-_D306XaCFc3VhOfPwjUW1t_4T1nyOIDUwz4Cdscm1H_HvFiZuXU1p8SRBDDFGGyNDoVl6mayZDBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مردم در میدان انقلاب: سید مجید دیو رو بزن، تا صبح تل‌آویو رو بزن  @Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/440533" target="_blank">📅 23:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440532">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFfcpr4pDgFHr9zuo4ySa4srJR_zpS1TeqohPEdA8xVTs-CORqF1Hskr3L0ykh06ST0MfyLZHbmf8aVP-S9MdErRCvf8ibTQwPaXaVIuARBmrmTW9XrSJYxbWaZt0ThHAeM0Cpqnv41_nebNvNKcdxtpD-VSuaGX_WyLRmZYW6f8AggVvcifSqsNrHUGpXAHP2jNcINaWOgm88goetong0CD8wfdZi7jYjr40OPBOFVSdu-S8dnd5rVwm0XCI8Tjg8h7aI6IZibJxlKNv5UIAZAl-sbwON61ylS4uEq3vmhNtnV-mrcVx5kPDxcxTBZLM3eJWwCA2AaXQULxcblZAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقب‌نشینی ترامپ: حملات اسرائیل به لبنان با من هماهنگ نشده بود
🔹
ترامپ در گفت‌وگو با فاکس‌نیوز: از حملات اسرائیل به لبنان خوشحال نیستم و این حملات با هماهنگی ایالات‌متحده انجام نشده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/440532" target="_blank">📅 23:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440530">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcd8450fbe.mp4?token=R9NlHhIyzyLXCKQpstacf564BrrL7pOwt602O3x7yBXQfC1jrRG_Fdut0iSByI2nSorx4v-uV_LDkqVDxKbNCyOFL972LEbovSZxf4wZucU5QqtfhfLtbXW4AAWxGk4-EAzQtiqWoFijPwKimAN91I1LkLd1XQnmd-9963Pm-ybgImZLNfK5wv6XGbw7yhefRf5nLmRI7bpTx9gQ_J_7r2dF1FwpLVIv7VZgjeULlIs-gTToXe0VeEC50Jhw3twD_q1MBVjSp-rvl020UaQ-9sVvKYxtksSw4TaV-ZPbBDh0D1j9151z_AH5TBXoDVmr20Mw5SzrslwGlrhOT9DksA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcd8450fbe.mp4?token=R9NlHhIyzyLXCKQpstacf564BrrL7pOwt602O3x7yBXQfC1jrRG_Fdut0iSByI2nSorx4v-uV_LDkqVDxKbNCyOFL972LEbovSZxf4wZucU5QqtfhfLtbXW4AAWxGk4-EAzQtiqWoFijPwKimAN91I1LkLd1XQnmd-9963Pm-ybgImZLNfK5wv6XGbw7yhefRf5nLmRI7bpTx9gQ_J_7r2dF1FwpLVIv7VZgjeULlIs-gTToXe0VeEC50Jhw3twD_q1MBVjSp-rvl020UaQ-9sVvKYxtksSw4TaV-ZPbBDh0D1j9151z_AH5TBXoDVmr20Mw5SzrslwGlrhOT9DksA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش مردم در میدان انقلاب تهران به شلیک موشک به سمت اسرائیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/440530" target="_blank">📅 23:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440528">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPuqJ9yM_ZlApAnuyYJ-Qs9h9YiMfbimboCweT3SA063grYRt0bA6_i8sEShSKWbE_xNssncfden7B09xxdc2S7GfDTMjFo58m7-q1cSt-Fr1VdJBYbrAqiSWSl7Qh2hfE39BmcU963jVF0Z6PRQAOyC6z53EMQG3I1-OOkaMChOakp5MxBIjQQOdA1YsV7Dhu_ta8DfzdqJWVdrzzbuJLl-viEsP-YwS4-7L9YlZQ7UgTPgubz0ioPchsujy4BPCGbl06m6NVGsYu-NzCbeFwmwvN-kxyxs-xr9AzP_W7_--afw7UUyVsJCloUXYDzLjD2XvXyOTLw2ZvdepeKQmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نفَس رژیم متزلزل صهیونیستی به شماره افتاده است
@Farsna</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farsna/440528" target="_blank">📅 23:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440524">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izY56D3UZVj9-pATj82qwc243kZfYNvfxfsszJphXDWqbj1qCxSvoEMoV2FpiAV3Nnr8rc2padzXswmf3TSFgDme03T3JVjTTceBFDpowQMeUn5TYx2S45NiD_bAz8NsUUa6p0Yf_eNV_Y3Qtyg-TIf3EzhX6GIsjj5nGbp29ao6OGj0s0unQOxE5ocVGqXNLmFXajORQzPYYqt3RqWBR0-yahc_6GZcG3MwgpRd0HTNu4p-U9ZUyE8x5K253LwKRsbngf4ILQ_hoPpBelk0yZnu6eXNCacMLanMVbnUzVWj28u0UOqouuIyrp4Kf7ZrwamtIVvUj_VieXlPIjG13A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: توصیه‌ام به ایران این است، موشک‌هایتان را شلیک کردید و این کافی است. به میز مذاکره برگردید و توافق کنید.
@Farsna</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farsna/440524" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440523">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51355c6749.mp4?token=BY5gWvq86SFg68SjvGxPvWd0RtzBNwulm3_DAyTZBmaKVOBqYqxMcNCpdtlaoGnTtaZiQ_mnSFSI3BqlWsN-KLaCBMJC73RB4LurxC8xH-eltZr1wFW93N2cDIALn2NfAiQved2lE_idtVPCmRhChlIOFFvigJa7HvAwq2Nd7b6bDPOeTD9zgwN__vUUkkZqlCPlwzLBNmI0T35QheONCfKWE3bCO8BNf5SYrPJMzm9YXdBzcJs9uk1TOna6GukJgWmP-73QT5JV8ASmmEwUKtV_z4ZoF-b7s9N4mqsVPTy9CYcD3apIIV6WNJ9FHbhpYWZ_UoeTkhUBGCs9rFvysg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51355c6749.mp4?token=BY5gWvq86SFg68SjvGxPvWd0RtzBNwulm3_DAyTZBmaKVOBqYqxMcNCpdtlaoGnTtaZiQ_mnSFSI3BqlWsN-KLaCBMJC73RB4LurxC8xH-eltZr1wFW93N2cDIALn2NfAiQved2lE_idtVPCmRhChlIOFFvigJa7HvAwq2Nd7b6bDPOeTD9zgwN__vUUkkZqlCPlwzLBNmI0T35QheONCfKWE3bCO8BNf5SYrPJMzm9YXdBzcJs9uk1TOna6GukJgWmP-73QT5JV8ASmmEwUKtV_z4ZoF-b7s9N4mqsVPTy9CYcD3apIIV6WNJ9FHbhpYWZ_UoeTkhUBGCs9rFvysg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: پذیرش آتش‌بس توسط ایران در ۱۹ فروردین ماه مشروط به توقف آتش در تمام جبهه‌ها بود؛ لکن مثل همیشه امریکا و رژیم صهیونی به تعهد خود پایبند نبودند، هم تجاوزات و جنایات را در لبنان ادامه دادند و هم با تعرض مکرر به سواحل و شناورهای ایرانی در تنگهٔ…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farsna/440523" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440522">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: عملیات امشب صرفا یک اعلام اخطار بود و در صورت تکرار تجاوزات پاسخ‌ها گسترده‌تر خواهد بود و تمام اهداف آمریکایی-صهیونیستی در منطقه را در بر خواهد گرفت. @Farsna</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farsna/440522" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440521">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: در پاسخ به جنایت گستردهٔ رژیم غاصب صهیونی در جنوب لبنان و کشتار و آواره کردن گستردهٔ مردم مظلوم مناطق صور و نبطیه و سایر نقاط از جمله ضاحیهٔ بیروت پایگاه هوایی رامات دیوید، مبدأ این تجاوزها هدف موشک‌های بالستیک نیروی هوافضای سپاه قرار گرفت.…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farsna/440521" target="_blank">📅 23:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440520">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: پایگاه هوایی رامات دیوید، هدف موشک‌های بالستیک قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farsna/440520" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440519">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
آژیرها در سرزمین‌های اشغالی یک بار دیگر به صدا درآمد  @Farsna</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farsna/440519" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440517">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPuQHbOCr0MEq8PIYHbxqin2D_-FU8HQAdf0ABLaNFSNHDcDN2Wt0cgI7zgY1iVoNVqz2uqgcQfyUZOXqFNbU8U02IATClB5oCfDPdTvga36NB_8rQKGUDj4R0-7HHlY8ZVaJubjTeYJb9Y3TAQ9xbo7bWPyuqDpiXgc_VL1Nh4YqaYSx9sk7cmqOcU388IHnc2oI_32CY5nKbg6s9jjgtH1A8OA1ktPRNKCSf7XT1YTqKVdIAu0dDf5HTFjSMYxeuV_stTeqxBK1OQj2LW553M7wTkzReZK7RsJYbrM8i4EwIcoT559OywE4RyAeUy6_PpQpBLX9HnURevjPk5Xpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
محسن رضایی: ایران بارها اعلام کرده بود که نقض آتش‌بس و تجاوز به لبنان را برنمی‌تابد
🔹
امشب متجاوزان پاسخ خود را دریافت کردند؛ این پاسخ هشداری است تا دست از شرارت بردارند؛ هر اقدام جدید پاسخ کوبنده تر و هزینه‌هایی سنگین‌تر دارد.
@Farsna</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farsna/440517" target="_blank">📅 23:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440516">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5kdBbAM0ODt1vlRzmE5Ksyto-3fGDkpYqbfRE-yG39cyQz17d1gArcsW89ZHSJLI0D-K1yM4BwjYMuJ6mPs4F-ubLLo33exZzDSDlEhkEPt7xTC0zwBG3-WjH5NQXehFvGKFi_zUBNaAH3H7WYrgXvZBVEXAWrjejxJYz7DIDswjacKd6s9Zk54DuEdqpAwGXO3BH7aIshTcZep34DcOSoG6ubweHhg8tLTtY7-yrONlCcSefloQdUME2ZNTGIUk8q9KUoFuNXmPN2r9i9IwjKMKvm7uYKRp4U-pVf5tNgIsBWiDflctHtTzdHv7_xR-qFAuAPHGGvmTpeB8MJtCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آژیرها در سرزمین‌های اشغالی یک بار دیگر به صدا درآمد
@Farsna</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farsna/440516" target="_blank">📅 23:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440515">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTbSFcXXyoiC3ags4zEsRYuLgQl7pj6EYOrop0EMQLNNzI4Te-uWnhmbi3-SEJzIoJpq8T3o3Zp14LxqD95lnpalaSnmQyoH28sBRw-TT_qCB08tWpQAsQFzYTcugwpLuHy988EhWHxD98H4HuDVqc-qanJwNQ6Ne4jhJqYyVYx39o1B-zV3tQvdc3JIgfQESrn-KqKOubFgw_8bgTYmMUwX2Vm1LOfA7SRC-ydP6r7EtVA2im8CbGWeM1J7BQ2bai_MKyKHZ1fzIHOLs5suyHWVeoQvtEkZ4Iew75D3d8oBNllMAMNwGEQ21vpIOAwpvCvTaxzoldymf12ABijscw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام فرماندۀ هوافضای سپاه: الوعده وفا!
@Farsna</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farsna/440515" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440514">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‌
🔴
حملات موشکی حزب‌الله هم آغاز شد
🔹
پس از حملات موشکی ایران به فلسطین اشغالی، حزب الله هم دست به کار شد و شمال اراضی اشغالی را موشک‌باران کرد. @Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/440514" target="_blank">📅 22:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440513">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cfcdfd11c.mp4?token=PKVnjau7Dz9sHaNcgpbtluH01lPuY2jQHn1OFhaoIzEFK-o29V4p0-UWqH-sviELTQBu0HdY0oTXgPlsm07CSDSaqI5AKSOi1oDpCBj1ZEtvYTQNE-eIK9moJ9yJCgoRjTucO_BIJxIB4oUEDcUEA-xHavwKI-Y1ceOvDSZ7zBRY_FOxIN2BoXIgVahoXmY_CxvnX3VqgLTC_MT-FcLbj9TyUZYUCgP5rJLL0wID8d6pVRFj3ocS4qghPkP81B3oSech90drIWqpX7zw8X0ZCLgqiwra-uSDu1djyIOw9amninfpb-oQIj3uvmlfs1_A0u6P1W3uBEjaBTCqm01bTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cfcdfd11c.mp4?token=PKVnjau7Dz9sHaNcgpbtluH01lPuY2jQHn1OFhaoIzEFK-o29V4p0-UWqH-sviELTQBu0HdY0oTXgPlsm07CSDSaqI5AKSOi1oDpCBj1ZEtvYTQNE-eIK9moJ9yJCgoRjTucO_BIJxIB4oUEDcUEA-xHavwKI-Y1ceOvDSZ7zBRY_FOxIN2BoXIgVahoXmY_CxvnX3VqgLTC_MT-FcLbj9TyUZYUCgP5rJLL0wID8d6pVRFj3ocS4qghPkP81B3oSech90drIWqpX7zw8X0ZCLgqiwra-uSDu1djyIOw9amninfpb-oQIj3uvmlfs1_A0u6P1W3uBEjaBTCqm01bTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قم یک‌صدا؛ بزن که خوب میزنی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/440513" target="_blank">📅 22:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440512">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مدارس اسرائیل فردا تعطیل شد
🔹
شبکه ۱۲ اسرائیل: وزیر آموزش اسرائیل اعلام کرد تمامی مدارس فردا در اسرائیل تعطیل است.
@Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/440512" target="_blank">📅 22:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440511">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
آژیرها در اراضی اشغالی دوباره نواخته شدند  @Farsna</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farsna/440511" target="_blank">📅 22:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440510">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d8393634.mp4?token=KfEXsFSOz5SJVM4sgKTVNsqmKUCkV_kSQzNs-EY3Yot13_hOWACXxLuOcjJxMqjkdL9uQpKsRhIDql9XtHt2h726h1BOOcUCBVulc0zzlyuEUct5sJ-s8s_AbsIXNvW7Io4dmkfKpL-7j5tF6Oa3wqewzDOm2wUxPOhQacKM1QTILHucZih97qgRoLs70rdeyHvttUHgIb0chWsB1JThIpegCgPw1MmPPAX_6dXWyA049ajzJG73QCDPcQqYC4osTGWOkYDnh06cDN8uh6N7ye5rgbVuROKdDmxS2-qTOj1enw7EHX2lP6XJCFDz7b4i4Kqab_9FYHcrNF_Ezl3nGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d8393634.mp4?token=KfEXsFSOz5SJVM4sgKTVNsqmKUCkV_kSQzNs-EY3Yot13_hOWACXxLuOcjJxMqjkdL9uQpKsRhIDql9XtHt2h726h1BOOcUCBVulc0zzlyuEUct5sJ-s8s_AbsIXNvW7Io4dmkfKpL-7j5tF6Oa3wqewzDOm2wUxPOhQacKM1QTILHucZih97qgRoLs70rdeyHvttUHgIb0chWsB1JThIpegCgPw1MmPPAX_6dXWyA049ajzJG73QCDPcQqYC4osTGWOkYDnh06cDN8uh6N7ye5rgbVuROKdDmxS2-qTOj1enw7EHX2lP6XJCFDz7b4i4Kqab_9FYHcrNF_Ezl3nGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از
موشک‌های ایرانی بر فراز فلسطین اشغالی
@FarsNewsInt</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/440510" target="_blank">📅 22:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440509">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIx9hMPMsAA5olU0esWXKftE1y2fcqPc62VlXAo7S7dqY8Z1GcO4plVl7tysxNzN9EyTmiPGkQt_lZnBB_rAGuw4JnHFU1WNMHfminYaJ9_9T9VhG7EgsrWwWWtyE9Oil_4wYl2yOZGTSAYbQ8mII7F9UQjhmv4CEkgxg0UteLjUvlmPq_qlgBxlsPAJPO2SlpcnFQco-7DhUIHOqMKfivbldoQg0QsoGwf0M4UvGAx8UMCWaTikt0pBD4JN6DjTa0FJhFTQPa57sUhcyAvlVFpUV-qfx4Oz1foKyratHe6BTC77ozbK8cgjTd-E8mMIWSUcZPr3ihkryZbvGKocrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
گروه هکری حنظله با انتشار پیامی، از اجرای یک عملیات سایبری علیه رژیم صهیونیستی خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/440509" target="_blank">📅 22:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440508">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‌
🔴
فرمانده قرارگاه حضرت خاتم‌الانبیا (ص): ارتش صهیونیستی باید حملات خود به جنوب لبنان و ضاحیه را متوقف نماید و درصورت گسترش حملات خود به آن منطقه و یا پاسخ به اقدام ایران، با ضربات کوبنده‌تر و پشیمان‌کننده‌تری روبرو و حملات ویرانگری علیه رژیم و حامیان آن…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/440508" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440506">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2rpAuyprZjs51l5JbSjoAPcrM1GhStwCFOv-L3AmSzysuuBbdEvPAu35oD-ic7Zk2vz6439X26tCCrhI45f-SmppkCJw830GQcIRP7uua-C1Oh2NK58W8RC9nZS8MFmeLqPKw7V4VGKDm_ktuu7Ckehi_2y_hRAvgDae1PznlMNvviMfRu3lNKoAsM3CJxZj1v4nIvpqn6wRxrzJmRsjkKVqroRMfvFo705vp9qKxNeH1oOV9mOBjRqxPUnTBBgTXDkYUA4-w-CSlfNpIAzrhsrdPirwNvun2hA5DrfMhJs-9fg-m7j_oWQo6HMnxvln1A6fd4CkTdVAocsrEyPrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پست عراقچی در شبکه ایکس با تصویر پرچم‌های ایران و لبنان
@Farsna</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/440506" target="_blank">📅 22:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440505">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‌
🔴
ارتش رژیم صهیونیستی: موج جدیدی از موشک‌ها به سمت اسرائیل شلیک شده است. @Farsna</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farsna/440505" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
