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
<img src="https://cdn4.telesco.pe/file/XGPjN6iDDvlF36BxpIbKJCAM1I_B4lkDcU8sD0Rxpo6ta4_3BU8iZQegmZvgsTK0EVBP2Gt6dgD4ouxlRPrZugqZNsluAVjbaPorTawDZpPGT43efdiQLXGnrCTMm9V9hoXkruQY0_3UUWXjgz3cmm67fGIKyjKnHreVVx3XfPnc4-hQGYS_IttutZ2A3Q6w6kx-LxV05vg42CaHhdsdpVL1Ok2MluVEFwDCa-wMJufGXSBWi4qTPWy4e5rFYRh6HkUlyFXBKeBb92c9TQbSTUcxnqbzdHi6QczU21GZ2CwSqYjhfyW1SJP3yPje1FhBmyDOUqd7dSwBHCV58jV7FQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.23M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 21:14:30</div>
<hr>

<div class="tg-post" id="msg-657448">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تهدید شبکه‌ای، پاسخ شبکه‌ای می‌خواهد
تحلیلی کوتاه بر اقدام نظامی ایران در ۲۴ ساعت گذشته
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/657448" target="_blank">📅 21:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657447">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
لغو پروازهای «ایر فرانس» به اسرائیل
🔹
در پی تداوم تنش‌ها، شرکت هواپیمایی «ایر فرانس» نیز به جمع شرکت‌هایی پیوست که پروازهای خود به مقصد سرزمین‌های اشغالی را به حالت تعلیق درآورده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10 · <a href="https://t.me/akhbarefori/657447" target="_blank">📅 21:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657446">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzDP2IH1-Vkbd23Al153-qlKqt9qUZ7DwLy_5PT8xxZEGJBKPcb-3Wb7BynpGMs5qlP57NNgrin-J1EJLShr9aUJ3rlDOXj8x3bBJoVdGeLU_Jy20IKo4jwrEW7XuFJrOOrQr7JfycI5uPDGaVi2igsPwKOd-6asf0KB4NFUa6BKnAfnKgSt0kWiRe79G5Fi0JEIC4JQtlJm6hV2mRnnaZbvsEj-RVHkcYKkK4SsNXK5kF_NWJIotSKgKLYK3aBXkpvVstGZJg4xKGVqdpZqRqF6uKsKFcegYXsXeUuepJpttk9rhwE-u1Kw8itZe5T-AiuoEmnzJO5TseV3zXmy2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
المانیتور: آمریکا شب گذشته در رهگیری موشک‌های ایران به اسرائیل کمک کرد
المانیتور:
🔹
ارتش آمریکا در تلاشی برای کند کردن آخرین رگبار موشک‌های بالستیک ایران به سمت اسرائیل شلیک شد، موشک‌های رهگیر پدافند هوایی شلیک کرد.
🔹
به گفته یک مقام آمریکایی که نخواست نامش فاش شود، واحدهای آمریکایی در منطقه در دفاع از خود موشک‌های رهگیر شلیک کردند. چند صد پرسنل نظامی آمریکایی در اسرائیل حضور دارند.
🔹
مقامات نظامی آمریکا هنوز در حال بررسی این موضوع هستند که آیا تلاش‌های رهگیری در سرنگونی موشک‌های ورودی مؤثر بوده است یا خیر./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/akhbarefori/657446" target="_blank">📅 21:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657445">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
قالیباف: صحبت‌های رئیس‌جمهور آمریکا دربارهٔ یادداشت تفاهم، مخالف بخش‌های توافق شده بود که نشان داد آن‌ها نه دنبال آتش‌بس هستند و نه دنبال گفت‌وگو
🔹
باید برای دفاع از حقوق ملت ایران پاسخ قاطع می‌دادیم که به لطف الهی نیروهای مسلح ما با اقتدار به وظیفه خود…</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/akhbarefori/657445" target="_blank">📅 21:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657444">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‌
♦️
قالیباف: هدف مذاکرات پایان جنگ و ایجاد امنیت پایدار است، نه عادی‌سازی با آمریکا
🔹
به مردم عزیز اطمینان می دهم که با قدرت از حقوق مردم ایران دفاع می کنیم.
🔹
‌ما نه می‌خواهیم با وادادگی پیش برویم و نه با شعارزدگی بلکه باید با اقتدار و عقلانیت ایرانی به‌دنبال…</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/akhbarefori/657444" target="_blank">📅 21:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657443">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
قالیباف: نقض آتش‌بس و محاصرهٔ دریایی، علت تنش‌های اخیر بود
🔹
نه دیپلماسی مانع عملیات نظامی است، نه عملیات مانع دیپلماسی
🔹
میدان نظامی، میدان دیپلماسی، میدان حضور مردم و میدان خدمت به مردم تار و پود یک پیکره واحد هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/akhbarefori/657443" target="_blank">📅 21:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657442">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
قالیباف: نقض آتش‌بس و محاصرهٔ دریایی، علت تنش‌های اخیر بود
🔹
نه دیپلماسی مانع عملیات نظامی است، نه عملیات مانع دیپلماسی
🔹
میدان نظامی، میدان دیپلماسی، میدان حضور مردم و میدان خدمت به مردم تار و پود یک پیکره واحد هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/akhbarefori/657442" target="_blank">📅 20:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657441">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
بحرین عزاداری برای آیت‌الله خامنه‌ای را ممنوع کرد
ادعای المانیتور:
🔹
بحرین اعلام کرد که عزاداری برای آیت‌الله علی خامنه‌ای، رهبر فقید ایران، در مراسم عاشورای این ماه ممنوع است./خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/akhbarefori/657441" target="_blank">📅 20:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657440">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ادعای ترامپ: به نتانیاهو گفتم برابر ایران تنها هستی  سگ زرد:
🔹
به نتانیاهو گفتم بسیار مراقب رفتارهایت باش، چرا که ممکن است خیلی زود خودت را برابر ایران تنها ببینی. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/akhbarefori/657440" target="_blank">📅 20:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657439">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
خضریان، عضو کمیسیون امنیت ملی مجلس: جمهوری اسلامی دیگر نقض آتش‌بس در لبنان و جنوب ایران را تحمل نخواهد کرد/ موشک‌های ایرانی به اهدافی اصابت کردند که بتوانند به حزب‌الله در جنگ کمک کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/657439" target="_blank">📅 20:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657438">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ادعای ترامپ: به نتانیاهو گفتم برابر ایران تنها هستی
سگ زرد:
🔹
به نتانیاهو گفتم بسیار مراقب رفتارهایت باش، چرا که ممکن است خیلی زود خودت را برابر ایران تنها ببینی.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/657438" target="_blank">📅 20:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657437">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قاضی‌زاده هاشمی: اگر لبنان سقوط کند، ایران در امان نخواهد ماند
سید امیرحسین قاضی‌زاده هاشمی، در
#گفتگو
با خبرفوری:
🔹
باید دید چرا آمریکا برای اسرائیل می‌جنگد، به همان دلیل ایران برای لبنان می‌جنگد چرا که اگر لبنان سقوط کند، ایرانی هم باقی نخواهد ماند. لبنان باید بداند حرف‌های مزخرفی که رئیس‌جمهور و دولتمردانش می‌زنند، اشتباه است و متاسفانه این خود فروخته‌‌ها در همه کشورها هستند.
🔹
لبنانی‌ها هم باید بدانند که اگر ایرانی نباشد، لبنانی قبل از او نخواهد بود. تا زمانی که یک سرباز اسرائیلی در جنوب لبنان مستقر است، این نبرد نباید پایان یابد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/657437" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657436">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4ec30c567.mp4?token=rR7e5Hx6RbQhijo8gqnntmeXoOgU3jdsyAlQ12JOihj-Tq2yzd2bjsJiWi5-ZL9GFF1PYtGNpmobt5QH2wCR66mORjCp4pdLE8AKa6kTtfvejnn0s9dtDrJxQt179d9tYLISfpv5C-ix4uZO7fCGr1jDriP8sZVocvxQb0QW4xLE-ScFgzKJmFEynsJZToKyhUjcv8u3Cbr2fX3qjMlg-6ODMcZy4Idf4cpiFt907dkQD1ksQz4biBZzir-EBi9orMxnilpUEDdySZf6knnQsJu2bcdzxK3TUHHTBHe-At0TX9aQ2QmAirXpYwMFgDJHC3g59P1fPLrSisRnbl0SEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4ec30c567.mp4?token=rR7e5Hx6RbQhijo8gqnntmeXoOgU3jdsyAlQ12JOihj-Tq2yzd2bjsJiWi5-ZL9GFF1PYtGNpmobt5QH2wCR66mORjCp4pdLE8AKa6kTtfvejnn0s9dtDrJxQt179d9tYLISfpv5C-ix4uZO7fCGr1jDriP8sZVocvxQb0QW4xLE-ScFgzKJmFEynsJZToKyhUjcv8u3Cbr2fX3qjMlg-6ODMcZy4Idf4cpiFt907dkQD1ksQz4biBZzir-EBi9orMxnilpUEDdySZf6knnQsJu2bcdzxK3TUHHTBHe-At0TX9aQ2QmAirXpYwMFgDJHC3g59P1fPLrSisRnbl0SEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه‌های آخر الزمانی از زلزله‌های فیلیپین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/657436" target="_blank">📅 20:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657435">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
برخی کاربران مدعی شده‌اند که دارایی‌شان در چند صرافی رمزارز خارجی، به بهانه تحریم و بدون هشدار قبلی مسدود شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/657435" target="_blank">📅 20:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657434">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd07775b9.mp4?token=U81fcqM4EaKTsshJievKknUC9W2bqeyCDs2obl0BRgyp6htYn-PCXGbLTl2VOWtNKUQXAthNhrHOfSkwEgCF8umHXanAPkR5_L1f0hSv8BGENnzvT5Rk-FEQY9oQXotwCFCATCkhuwpBNyUGcV8wezIDy1hh9gk0_xn03Cu02ID6aOn0vBoyQa72PCvCvttrUoGLO2nbdmRm2mMp0DU1w98tFqUbHIOWScvxwFG-DgjCPb7W4GVFd2OT-7SBnyJwcyFVVPJH7VwgmmHDbYnw5qdEPu4avqRi53-TDK422NYU2Pch18jBhLpByrufqwb1J6mXOAL9C-GxjIY72JC4dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd07775b9.mp4?token=U81fcqM4EaKTsshJievKknUC9W2bqeyCDs2obl0BRgyp6htYn-PCXGbLTl2VOWtNKUQXAthNhrHOfSkwEgCF8umHXanAPkR5_L1f0hSv8BGENnzvT5Rk-FEQY9oQXotwCFCATCkhuwpBNyUGcV8wezIDy1hh9gk0_xn03Cu02ID6aOn0vBoyQa72PCvCvttrUoGLO2nbdmRm2mMp0DU1w98tFqUbHIOWScvxwFG-DgjCPb7W4GVFd2OT-7SBnyJwcyFVVPJH7VwgmmHDbYnw5qdEPu4avqRi53-TDK422NYU2Pch18jBhLpByrufqwb1J6mXOAL9C-GxjIY72JC4dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفتار تحقیرآمیز آمریکایی‌ها با اعضای تیم ملی فوتبال سنگال
🔹
انتشار تصاویر و گزارش‌ها از لحظه ورود اعضای تیم ملی فوتبال سنگال به خاک آمریکا و برخورد نامناسب و تحقیرآمیز مقامات آمریکایی با آنان، موجی از واکنش‌ها و انتقادات را به همراه داشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/657434" target="_blank">📅 20:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657433">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a531b5b25.mp4?token=EVGbUTYAiaxrCkjRADVWaZqbUlcftrJRVeFoB0zKGWBu7SyjXaq7SxRmDIuQUDBkrYCjaO_kEq6WWXkSDdiocAjQ6jeIyyq8Jg4gad_3vQ3yY4z7p61SBmyBtJZ4aLiCDJabTitF8LSvqIKKlB5CPfSluVAKBj9uVZoCF5imQ4I7fNXgLQhm2eGcyhSWaUbui0n_obxrGE10NikW9FxsLH-1JcLU0hHKLo4jWxHKVOEw3iyEvg7RMwN0jIJK8pb3e3qZmNSIDSLvZxA1WDrPMeBQGAhkrY8cVe9sW68JsK9H_qkflG1xGBdGcbSiwR1qy75cYaKDAa8RisTeJ64jzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a531b5b25.mp4?token=EVGbUTYAiaxrCkjRADVWaZqbUlcftrJRVeFoB0zKGWBu7SyjXaq7SxRmDIuQUDBkrYCjaO_kEq6WWXkSDdiocAjQ6jeIyyq8Jg4gad_3vQ3yY4z7p61SBmyBtJZ4aLiCDJabTitF8LSvqIKKlB5CPfSluVAKBj9uVZoCF5imQ4I7fNXgLQhm2eGcyhSWaUbui0n_obxrGE10NikW9FxsLH-1JcLU0hHKLo4jWxHKVOEw3iyEvg7RMwN0jIJK8pb3e3qZmNSIDSLvZxA1WDrPMeBQGAhkrY8cVe9sW68JsK9H_qkflG1xGBdGcbSiwR1qy75cYaKDAa8RisTeJ64jzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقاد ممدانی از نحوه میزبانی دولت تروریستی آمریکا  در جام جهانی
🔹
زهران ممدانی، شهردار نیویورک را به دلیل نحوه مدیریت جام جهانی، محدودیت‌های سفر و رد درخواست‌های ویزا برای تیم‌ها و دیگران مورد انتقاد قرار داد.
🔹
جام جهانی قرار است جشنی برای کل جهان باشد، در حالی که خلاف این را در این رویداد ورزشی شاهد هستیم.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/657433" target="_blank">📅 20:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657431">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29a218a22.mp4?token=DGcM24EYPcf6cMLkGAWyZoLFBdxNyH6GKQYZcFl7hitEZg7pBIX4FV5IT3iVAB-_N5UgGsmwUQlrrXs2B9pj_ILByycps0T61T0Vt9SAZnrcGKKDYlxUxkOWwkBpQ0bBqHO-oSpy3wMD7SspDvXTVr4ry3NKWJUZ4ob6QNRALVBEp2_X-HlVs70rC2ZRzYyg25FeCRXflYYOf2sHMrrR0ce8duwTKio5JHw-WpBGGinPLCERpOYzjktD__YUowqpwWuWwl4JsFa8hoiWnchR2L4wCK7FerP4qfuW_0ESbekZ0Nrmsc_HgVfWj5NiIc36OEueWiTIej1FC38UcqTANLyed1nwxt0b_1dPdsFS8WeS7CsNr1bVY9pz6X1vslFcMoyJQIVUb2Q5MeG5Qy9lVBh7foCaicEU1vdvZFBB5Pr2TI1ebraTP6iTvRdaaIqOEkSgFk1W8wYXaMWE8SYDSFPdDIQCmvWtkBKSbpoU8DG7FduGx3OSPl6-OGZdcw0zTkFeMIeyyNe9g5MFgOdQCuEabNEVJK7WTyNkvcsyLrIHjU384Y1J8-e7B8_4jw-62kacWxSWyYDJRagrQuZynfIJWgLRV7sjKk1VKNMaiE_lrtXDY97mllaJtuSDhNlKpI4Xl8dkQIlt6LF2s8nh7jrUEuzgic3x_IXXHECNyCk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29a218a22.mp4?token=DGcM24EYPcf6cMLkGAWyZoLFBdxNyH6GKQYZcFl7hitEZg7pBIX4FV5IT3iVAB-_N5UgGsmwUQlrrXs2B9pj_ILByycps0T61T0Vt9SAZnrcGKKDYlxUxkOWwkBpQ0bBqHO-oSpy3wMD7SspDvXTVr4ry3NKWJUZ4ob6QNRALVBEp2_X-HlVs70rC2ZRzYyg25FeCRXflYYOf2sHMrrR0ce8duwTKio5JHw-WpBGGinPLCERpOYzjktD__YUowqpwWuWwl4JsFa8hoiWnchR2L4wCK7FerP4qfuW_0ESbekZ0Nrmsc_HgVfWj5NiIc36OEueWiTIej1FC38UcqTANLyed1nwxt0b_1dPdsFS8WeS7CsNr1bVY9pz6X1vslFcMoyJQIVUb2Q5MeG5Qy9lVBh7foCaicEU1vdvZFBB5Pr2TI1ebraTP6iTvRdaaIqOEkSgFk1W8wYXaMWE8SYDSFPdDIQCmvWtkBKSbpoU8DG7FduGx3OSPl6-OGZdcw0zTkFeMIeyyNe9g5MFgOdQCuEabNEVJK7WTyNkvcsyLrIHjU384Y1J8-e7B8_4jw-62kacWxSWyYDJRagrQuZynfIJWgLRV7sjKk1VKNMaiE_lrtXDY97mllaJtuSDhNlKpI4Xl8dkQIlt6LF2s8nh7jrUEuzgic3x_IXXHECNyCk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحلیل‌گر اسرائیلی در واکنش به ادعای دروغ ترامپ: هیچ عملیات نظامی توسط اسرائیل بدون کسب تاییدیه رسمی از آمریکا انجام نمی‌شود. ایران آمریکایی‌ها و اسرائیلی‌ها را جبهه‌ای واحد می‌بیند و اهداف آمریکایی را نیز هدف قرار می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/657431" target="_blank">📅 20:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657430">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای عجیب سرافراز: یک سال است که جلسات شورای فضای مجازی برگزار نشده!
محمد سرافراز، عضو شورای فضای مجازی در
#گفتگو
با خبرفوری:
🔹
شورای عالی فضای مجازی هیچ‌گاه در مورد قطع کردن اینترنت مصوبه‌ای نداشته و در ضمن حدود یکسال هم هست که جلسه این شورا تشکیل نشده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/657430" target="_blank">📅 20:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657429">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
سنتکام: یک نفتکش مرتبط با ایران را متوقف کردیم
اطلاعیه فرماندهی مرکزی ایالات متحده:
🔹
نیروهای آمریکایی در ۸ ژوئن یک نفتکش خالی را در خلیج عمان، پس از آنکه این کشتی با تلاش برای حرکت به سمت یک بندر ایرانی، محاصره مداوم علیه ایران را نقض کرد، از کار انداختند.
🔹
جنگنده اف-۱۸ پس از آنکه خدمه یک نفتکش از دستورالعمل‌ها پیروی نکردند، مهماتی را شلیک کرد که به موتورهای آن آسیب رساند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/657429" target="_blank">📅 20:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657428">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/52f18c222e.mp4?token=owb61rxqLZRDuK76kE1DV9js7mqGslj-GElu69xerMVFa46yGIoU9luu3KiQoHNps7wkLufwcG37rFwxI7-J4LCNF3H61iAW0oCqhf8Ys7Cc17ihy5jAXsh_YyOnQxJ0Pugon8uj7YSgrVhEKsOPpGCevKJQ4-DvlwudNc_BeaZ4QgpNUqqzXFGa-oObvHVHTcAhl7mAPAoDmKOosRNctDOr_vMCJF4K_AOuRQlKv6L8j-juETtkolNAiAwQYcBkOaLmuyBVfWcyf51Y0cYZQeRjbXg83Qwh-VY507AJrMnOl-Jd9JBQEMzoYVqLxMU_x6kpt6mCu9BJOGpae7E4EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/52f18c222e.mp4?token=owb61rxqLZRDuK76kE1DV9js7mqGslj-GElu69xerMVFa46yGIoU9luu3KiQoHNps7wkLufwcG37rFwxI7-J4LCNF3H61iAW0oCqhf8Ys7Cc17ihy5jAXsh_YyOnQxJ0Pugon8uj7YSgrVhEKsOPpGCevKJQ4-DvlwudNc_BeaZ4QgpNUqqzXFGa-oObvHVHTcAhl7mAPAoDmKOosRNctDOr_vMCJF4K_AOuRQlKv6L8j-juETtkolNAiAwQYcBkOaLmuyBVfWcyf51Y0cYZQeRjbXg83Qwh-VY507AJrMnOl-Jd9JBQEMzoYVqLxMU_x6kpt6mCu9BJOGpae7E4EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گروسی در پاسخ به سوالی درباره ۱۷ حمله به تاسیسات ایران: من در این باره چیزی برای گفتن ندارم/ نماینده ایران حق دارد اعتراض کند اما من با آن‌ها موافق نیستم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/657428" target="_blank">📅 19:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657427">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
بازگشت فضای هوایی کشور به شرایط عادی
«شیرودی» رییس سازمان هواپیمایی:
🔹
پیرو اعلام مراجع ذی‌ربط مبنی بر پایان عملیات نظامی و با عنایت به هماهنگی‌های انجام‌شده، فضای هوایی کشور به شرایط عادی بازگشته و عملیات هوانوردی مطابق با اطلاعیه‌های هوانوردی (نوتام) صادره، از سر گرفته خواهد شد.
🔹
با فراهم شدن شرایط ایمن و انجام هماهنگی‌های لازم با نهادهای ذی‌ربط، محدودیت‌های پروازی رفع شده و فعالیت‌های هوانوردی کشور طبق برنامه در حال بازگشت به روال عادی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/657427" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657426">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/859333bc25.mp4?token=SdMvGwU9D5WUE0fySOZmXtDnnNSnu1orZ-Myw8fLvxupx-sDGZzebS_D-HppIenP1oHAa5RxpDXf1vK_I0Aco1aHqMEOp6lgVDHgLTLtckd3Wfi8QmFhGCK8je7yuEbSYJl0e-jJraYTqmWqM5pZ5XhHFl-ZJN2fqg_bJ0DvjCrZi5aBix68yddxBhAhm9ClEOTIOZmGZHKatrEwcZqMwIKB3RokWWGGFFB8XIEVsGr1IglrTRAJZaXAdrm2nMKo_FRFmotplTTL_mXB5SARj5Ak7qoTi62ywVhmzR7F6FKDlR1vIrd0P25TSihkcv2n707fbXm0-MnWAn6f88QFFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/859333bc25.mp4?token=SdMvGwU9D5WUE0fySOZmXtDnnNSnu1orZ-Myw8fLvxupx-sDGZzebS_D-HppIenP1oHAa5RxpDXf1vK_I0Aco1aHqMEOp6lgVDHgLTLtckd3Wfi8QmFhGCK8je7yuEbSYJl0e-jJraYTqmWqM5pZ5XhHFl-ZJN2fqg_bJ0DvjCrZi5aBix68yddxBhAhm9ClEOTIOZmGZHKatrEwcZqMwIKB3RokWWGGFFB8XIEVsGr1IglrTRAJZaXAdrm2nMKo_FRFmotplTTL_mXB5SARj5Ak7qoTi62ywVhmzR7F6FKDlR1vIrd0P25TSihkcv2n707fbXm0-MnWAn6f88QFFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قوانین جدید فیفا در جام‌جهانی ۲۰۲۶
🔹
فیفا به جهت افزایش سرعت و جذابیت بازی برای تماشاگران تغییرات جدیدی را برای مسابقات جام جهانی ۲۰۲۶ اعمال خواهد کرد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/657426" target="_blank">📅 19:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657425">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
گروسی: جنگ، بازرسی‌های آژانس در ایران را متوقف کرد
مدیرکل آژانس انرژی اتمی:
🔹
آغاز جنگ علیه ایران در فوریه ۲۰۲۶ باعث توقف تمامی فعالیت‌های راستی‌آزمایی میدانی آژانس در ایران شد.
🔹
آژانس نزدیک به یک سال است به تأسیسات هسته‌ای آسیب‌دیده در جریان جنگ ۱۲ روزه دسترسی ندارد. حدود ۴۴۰ کیلوگرم اورانیوم غنی‌شدۀ ایران از زمان جنگ ۱۲ روزه تاکنون تحت راستی‌آزمایی آژانس قرار نگرفته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/657425" target="_blank">📅 19:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657423">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9yCjse5w-V2gPHCV8ZsQr1gQj4OzENuFSPACA-WNyl_UN_nDq9CKoiBMcQ7yuyXi2vUcLFK0GdR632OurBKKvBx4ab-EbHU7wQUn3c0nLoua7GWNLEay3679daxMtBKouoIhlcwz6_GZosSpbMmEDgdH089FNCIAEzjXyYzRbSOBhXsAKMKEXigG2LD8PiWziHryhHKUNhtqZXRQT4aQvjcCoqCWZobvDLcosC4gcOQer6wdu3bZpv4gNf25Kvbzdrrb-Inl1zg4PIdJWNAqkaBe60x9MkRgG2spIffENrIuFP0y8il39SxSwYgNo-E0liBcWhRBi2D5LodRtBy9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش متجاوز رژیم صهیونیستی هشدار تخلیه شهرک زقوق المفدی در جنوب لبنان را اعلام کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/657423" target="_blank">📅 19:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657422">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBAQcCen9-kd7hqcIbpvF0JMtjxjBkStlqGdcyLM09X8L7DN3xmrq4NkCWDw7CYvrBS8uTJwGFMb5nDbL8ufD-F6m32EddRvCpLR7Hnmi9aAUcdWGCfyZw6AbiYX6rMYXm-3CnQsBKQ7Gp0TGmS1h6qSGlWZmNjUO-QHWm5AW0wuzqGelPyvVEpqTJWqNjpAdxd8YPYzQ11u62HgOph6WqKoMwbQS_TK7hlCvxd17cjG6Xwv3rs_muIiXjUTUs2XhqlyRJyemsEOxA80yt3K1JfcX9vBcXtGJSxd73LI1Ja6MYj0PTImHo9ZMeS9mKnAqTM0mVxSTTq4MRYf-f2y_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روسیه برای شهروندان خود در اسرائیل هشدار صادر کرد
🔹
سفارت در اطلاعیه‌ای که روز دوشنبه منتشر شد، اعلام کرد که روس‌هایی که در حال حاضر در اسرائیل هستند باید احتیاط کنند و از دستورالعمل‌های مقامات محلی پیروی کنند.
🔹
این سفارتخانه اعلام کرد که هیچ گزارشی مبنی بر زخمی شدن روس‌ها در نتیجه حملات موشکی ایران دریافت نکرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/657422" target="_blank">📅 19:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657421">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
به صدا درآمدن آژیر خطر در شمال فلسطین اشغالی همزمان با کنفرانس خبری نتانیاهو
🔹
همزمان با اظهارات تهدیدآمیز نتانیاهو علیه حزب الله، آژیرهای هشدار در مناطق شمالی سرزمین‌های اشغالی در پی نفوذ پهپاد حزب الله فعال شدند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/657421" target="_blank">📅 19:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657420">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9efaf273c.mp4?token=pNaBiSDdISm95jEndk2pFKYDjraN76BWBD49P3QFgytVyWijlQq8QtysjbDuWtOKVMBLxJMgOwET28v4j7Oecwp4sJoapZ7ydh4Kby2JMHrLfDyU7BztIBJkWBup0Zo7mzKFQhs-_3RoFW0WFnfABjc3P4UulaGogizh_AR07QgqEKVl1FBdgRaSsqplbog01ig4ytkXpTTezCfxecmNgbYNFw6on2-2MZA-1-GGo-ZPyTVY9K5Oiw1EK2PAOdzHpmZrfr7VFOrP7WKUibep3ffPNZdjE-ocDw6yGgKAsv9BsxC0zCAdUa_75afmupVnS31sXSJ7l9n-KojrqxwdUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9efaf273c.mp4?token=pNaBiSDdISm95jEndk2pFKYDjraN76BWBD49P3QFgytVyWijlQq8QtysjbDuWtOKVMBLxJMgOwET28v4j7Oecwp4sJoapZ7ydh4Kby2JMHrLfDyU7BztIBJkWBup0Zo7mzKFQhs-_3RoFW0WFnfABjc3P4UulaGogizh_AR07QgqEKVl1FBdgRaSsqplbog01ig4ytkXpTTezCfxecmNgbYNFw6on2-2MZA-1-GGo-ZPyTVY9K5Oiw1EK2PAOdzHpmZrfr7VFOrP7WKUibep3ffPNZdjE-ocDw6yGgKAsv9BsxC0zCAdUa_75afmupVnS31sXSJ7l9n-KojrqxwdUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بوم‌کشی؛ نخستین مستند جنایت آمریکا و اسرائیل علیه محیط زیست ایران
اولین مستند تصویری ایران درباره «بوم‌کشی» (Ecocide) ساخته شد. این فیلم به سفارش اداره کل محیط زیست شهرداری تهران، آثار مخرب حملات آمریکا و رژیم صهیونیستی بر منابع آب، خاک، تنوع زیستی و سلامت مردم را بررسی می‌کند.
از آلودگی تأسیسات انرژی تا تخریب جزیره شیدور، این مستند جنایت جنگ علیه محیط زیست را روایت می‌کند.  «بوم‌کشی» از شبکه‌های صداوسیما پخش می‌شود.
https://www.aparat.com/v/vheh27v</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/657420" target="_blank">📅 19:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657419">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ادعای نتانیاهو: اسرائیل فعلاً از حمله به ایران خودداری می‌کند #Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/657419" target="_blank">📅 19:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657418">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntntr-K_fZ4LvrLyKmPCfFwnRSn4iqNXxbbbzAjgyHHruqpflcGZbi34HVolqSiCiTYI_e8rNgZ06gX2GMn3Rh9plpg1bzQ7P-tF4-QUe2TSxlMeghU8K8V1DEYchrX1veMT-z7m3xqwzXMatksOqEja31wQ3HDCzpUWItrkC4nAXgp5sg-uXPC-CcFVKoUK--hCtCbXE6kRxINuYArjvQn4TB1R4NcbRVK9uKsf6Zwb3n1pLUHTWhqrbVugNc4aXw76l6crv5yLVUxTyt7xxFu7q92M8R_dc4zcUhnkxQJqQrsBRqN2wFp8jjgjBlmbTfEo-HTLCs3gxo9D1HszSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی: ایران عضو کنوانسیون حقوق دریاها نیست
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/657418" target="_blank">📅 19:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657417">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
نتانیاهو: ماموریت ما با حزب‌الله هنوز تمام نشده است  ادعای نخست وزیر رژیم صهیونیستی:
🔹
یک سال پیش ما یک حمله تاریخی علیه اراده ایران برای نابودی ما با بمب هسته‌ای آغاز کردیم.
🔹
ایران و حزب‌الله تلاش کردند معادله جدیدی را به ما تحمیل کنند و ما آن را نخواهیم…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/657417" target="_blank">📅 18:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657416">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7918af41cc.mp4?token=Ann4wINXlZIvXz5OaVvSUXSt_u1IiF8Zz2d2JDM5ZWhXZiS2unn4l7RNesQe-HNCZnGRKV7sg0wVBIiBZyA4UFHhL6LUNH4ng4NYY5rDxWk27YtT-IsJK8oeBHUchcGJ_RH3uD54PGe_Crb_JI3SZN4w9VE09DrBImWw_N_U4vCjPr1bH-DCzNaUHm6nWvS5B-LAo28XmQM60WoxF0OYdXiW1Vi0qJGwvnNXwXYPahgTnRo1JR7nMbebloeKqumycHsXinJIHy_M8xSu0OW5goGO_ILbS555ZdERwmXnce1Yh78ibQFz8EYtH55X-YLs1WYJjzJqau7Sc-kOBmOE_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7918af41cc.mp4?token=Ann4wINXlZIvXz5OaVvSUXSt_u1IiF8Zz2d2JDM5ZWhXZiS2unn4l7RNesQe-HNCZnGRKV7sg0wVBIiBZyA4UFHhL6LUNH4ng4NYY5rDxWk27YtT-IsJK8oeBHUchcGJ_RH3uD54PGe_Crb_JI3SZN4w9VE09DrBImWw_N_U4vCjPr1bH-DCzNaUHm6nWvS5B-LAo28XmQM60WoxF0OYdXiW1Vi0qJGwvnNXwXYPahgTnRo1JR7nMbebloeKqumycHsXinJIHy_M8xSu0OW5goGO_ILbS555ZdERwmXnce1Yh78ibQFz8EYtH55X-YLs1WYJjzJqau7Sc-kOBmOE_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو: ماموریت ما با حزب‌الله هنوز تمام نشده است
ادعای نخست وزیر رژیم صهیونیستی:
🔹
یک سال پیش ما یک حمله تاریخی علیه اراده ایران برای نابودی ما با بمب هسته‌ای آغاز کردیم.
🔹
ایران و حزب‌الله تلاش کردند معادله جدیدی را به ما تحمیل کنند و ما آن را نخواهیم پذیرفت. من متعهد می‌شوم که ایران سلاح هسته‌ای نخواهد داشت.
🔹
رژیم ایران پس از پاسخ ما، از حمله به ما منصرف شد. اگر رژیم ایران همان اشتباه را تکرار کند، ما با قدرت پاسخ خواهیم داد.
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/657416" target="_blank">📅 18:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657413">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVv622Jp5dWmnTEX1q7nH39-EMsPVbemNyvtgNVhch71RfVcLzrsCZWOCdfoToXWxQlnJNqES7sScQvxWWTUmZ9uVnxXJ37mfN8Q2Do_oesw3_FMZir3AsDG5XFP1T3MiR9RqmV2RlA9FR0G3d76HoPfqFz9IMZ8gw9hllZjdYVkRBpIJS67SgyyI2cng7qMz5fGJC-Tkw8UDHvkYNFD688P-AlNnCX_FXtJa1WUz01XvEHriXTlFLA1D36TxJ3NOmKJXzynk5aVe39BpqIChuD_dCyfnI6yfy8XRfF2X47YLZsPwDcDNChhl4r3Lw0suoXrP74D8o4YPeR45tWIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/657413" target="_blank">📅 18:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657412">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIIWLdcv_Uwt2wfCbsWTOqcQPNq0GW6-Wxx611w_otn0mfjF5USkgY2jv0YlqAeyFTo7zBGCL6R_CvgWebSJIhATcA5urQGx009MlD6vzJUcRflySGhUWwIQRen1dMoyj1cYfjEQ2vO03bWzQl22A59rcqojEs5jThHH3krXKZc8xjx4E9V3sFNUilSXUTrDbC1-oXzwcnF0QnBHvZiCXJG1VaihSTBB1-yob-VVjr_snmHNILbK01Emqb5RoMM9NMqHP_XDKo3zB_ZJy3IJobLr72L6rtwSkawcHJqLqwE2ne4Q1gEPQtAURegTEJ8TfS1f0WxyLKXCxvn1iUHbYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر فرهنگ: کنار هم بودن ایران و لبنان راهبرد ضروری دفاعی است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/657412" target="_blank">📅 18:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657411">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
تداوم تجاوزات رژیم صهیونیستی به جنوب لبنان
🔹
جنگنده‌های رژیم صهیونیستی دقایقی پیش شهرک «دیر قانون رأس‌العین» در منطقه صور واقع در جنوب لبنان را هدف حمله هوایی قرار دادند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/657411" target="_blank">📅 18:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657410">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
نتانیاهو تا دقایقی دیگر بیانیه مهمی صادر می‌کند
🔹
دفتر نخست‌وزیر اسرائیل اعلام کرد بنیامین نتانیاهو ساعت ۱۸:۱۵ به وقت محلی برای مردم و رسانه‌ها سخنرانی خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/657410" target="_blank">📅 18:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657409">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-jRss7hedsQgolw5mJQYSU_6If3ul_HGa9bUJQQbjDintEbPnzczPoOU5GPfzQPmmxxIe6YErgbIjLcif7r3PxkCepqu3F4kSRpUc5f5OpWRA7XPr_BZX19zzEm-7g4CsWNhaOsV_BBpP-xdAXvnsdy4FosTvrdRRql46nZipwukBC-D6H0EdA3zB3ho7BvZ7KB3kIUKxdfL37YdOZWt6TroXPUF1qvLzlmqwtUDNWvcmHZxJKoresCd8if0RT8iand4XMTw4GE_e4W4hvSJPyuhP2RJRs9nHqxWzV33HDENf0hthfi2SMcvVrja3ejr1lbVLsGUsPMkX5Lu42D6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرایا اولیاء الدم: دولت از حریم هوایی عراق صیانت کند
سخنگوی نظامی مقاومت اسلامی «سرایا أولیاء الدم»:
🔹
حریم هوایی عراق در معرض نقض مکرر از سوی رژیم غاصب صهیونیستی قرار دارد، آن هم در حالی که هیچ خبری از موضع رسمی، آشکار و قاطع عراق در سطح مسئولیت‌پذیری ملی نیست. نمی‌توان از حاکمیت عراق با بیانیه و شعارها صیانت کرد بلکه این امر مستلزم مواضع عملی و اقدامات بازدارنده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/657409" target="_blank">📅 18:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657408">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
خبرنگار الجزیره: آمریکا از طریق میانجی منطقه‌ای برای جلوگیری از گسترش عملیات‌ها و حفظ شتاب مذاکرات، تلاش می‌کند
نورالدین الدغیر خبرنگار الجزیره در تهران:
🔹
قاعده می‌گوید مذاکره زیر آتش، راهی برای گرفتن امتیاز در سیاست است. آنچه ایران به دنبال آن است، تحمیل معادله توقف جنگ در لبنان با تمام جزئیات آن در هر توافقی با واشنگتن است.
🔹
و آنچه اکنون در حال رخ دادن است، تلاش آمریکایی از طریق میانجی منطقه‌ای برای جلوگیری از گسترش عملیات‌ها و حفظ شتاب مذاکرات است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/657408" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657407">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp2fAkFb6YcrvKV3wwSAbknpdJ1oyLl6ppzg8hd8pnH5Jwx-5Pep9Pv11T7O9X2KVfZab7Uj49njxacjFNTbRuGZKRyyMyFZOKSYvkXo4pOJMrL2tISpVgKLMrWpB5kf7nfiro7GDhf7D_u71hNmixBfv582PAwDJGXWO5iH5q4sREJGtKBZYFZXXXfGjWp5hFeTxyh2h809pWAzjUw7oXkDdpL7LE-FCjAbVj5RzQLY1ttgHg29umaMQenf8QTzr-3nPtDTdIBt_RFjrfrfncbHBDNM-M9w2aloZUqNBzqgej8X0HyDJiQqGC-gXF1wu-tw_3D4hdtzJe2bEK-3tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف، رئیس مجلس:‏ معادلهٔ آتش‌‌بس روی کاغذ و نقض مکرر آن در میدان را بر هم زدیم
🔹
تا زمانی که ارادهٔ واقعی برای اعتمادسازی نداشته باشید، پاسخ ایران همین خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/657407" target="_blank">📅 18:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657406">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
گزارش‌ها از وقوع حادثه در سواحل عمان
🔹
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از بروز یک حادثه امنیتی جدید در آب‌های نزدیک به عمان خبر داد.
🔹
این نهاد دریایی اعلام کرد حادثه‌ای در فاصله ۲۸ کیلومتری شمال‌شرقی «جزیره مصیره» در کشور عمان رخ داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/657406" target="_blank">📅 18:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657405">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
تصاویری از حملات موشکی یمن به اهداف مهم در «یافا» اشغالی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/657405" target="_blank">📅 18:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657404">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hh2SRunJLjcdHP1g9Fe72glomLkqjxwDFl_KjicHuz1m3DbtMbEEWCw_nY0J3g-rMn-2MXWKaQPi80jis50W7dTjcJAWw59jCC3B3FaydUC2rcWspRHG_mTPIqUvMpIdCMTfgOBaSXIEc11I96-2MoZ9wkAQ6gAjJjeVWduS4ih54WdAy5CM_TJ13UzLIKJ-GcF-45uJdfBbm6ltQi97hTbhnfFdA4Q0Rn2p8lfHJEKpjC4rp9ZwaFV5XrWSTgqmBrhQLJr_OgBROIydqxLzeXRbVN2bjH9tsgtA_Gub6QWwcPhhu2Q-V4k1GvPRhn_0Cuagpe1JYLo11KQ2xN587Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: اگر ائتلاف شیطانی صهیونی آمریکایی دیگر بار دست از پا خطا کند، منطقه برایش جهنم خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/657404" target="_blank">📅 17:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657403">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
پردۀ شایعات ترور مقامات نظامی و سیاسی چیست؟
🔹
همزمان با آغاز حملات اسرائیل به برخی نقاط کشور، موجی از اخبار و شایعات درباره ترور، مجروح شدن یا هدف قرار گرفتن مقامات سیاسی و نظامی در فضای مجازی منتشر شد.
🔹
تجربۀ درگیری‌های اخیر نشان می‌دهد که این اخبار صرفاً با هدف ایجاد هیجان رسانه‌ای منتشر نمی‌شود و یکی از مهم‌ترین هدف آن‌ها تحریک جامعه به تولید داده‌های ارتباطی است/فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/657403" target="_blank">📅 17:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657402">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
گروسی:‌‌‌ هفته گذشته بازرسی معمول از نیروگاه بوشهر انجام شد
‌
مدیرکل آژانس در نشست شورای حکام:
🔹
در فوریه ۲۰۲۶، آژانس به دلیل درگیری نظامی، انجام تمام فعالیت‌های راستی‌آزمایی میدانی در ایران را متوقف کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/657402" target="_blank">📅 17:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657401">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
الجزیره: هم‌اکنون باز هم نقض آتش بس و حمله هوایی اسرائیل به شهر صور در جنوب لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/657401" target="_blank">📅 17:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657400">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOLwGEjRqftAJm1gRmij11twsOzpZ9cgFaw6w7taGFSvB5A48zD-2UeNYGEKYDb2daxxDTTgt_HpFQohv0aWbkjoFiPDvbgq4HR7SQMnUbCQMdS44UzsmuyMXsP2_vc8oFZlR2Mg3HUVXEzM5R5sbxlPhU4sjAY_sflws1qvF1_9kwIgFvuSt4ZFYaqHYwPZ2HN8oUG-sirNuzGDFcx0xN0BREyIfaC4k_KW7_1icipClZtfANQvFZVH2kN_YguzVPRChMDnJGf8WbekIFdXsttCsDrt65b48dlstv6-3nZlgm8JLbFQIJGFL2QW9Hdis1hpSc6bK3CP7ozoFFgdOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اختلاف واشنگتن و لندن بر سر سرنوشت جزایر دیاگو گارسیا
رویترز به نقل از تلگراف:
🔹
کاخ سفید در حال بررسی طرحی برای خرید جزایر چاگوس از موریس و کنترل پایگاه راهبردی «دیگو گارسیا» است.
🔹
این طرح در پی اختلاف نظر با دولت بریتانیا مطرح شده؛ زیرا واشنگتن با برنامه لندن برای واگذاری حاکمیت این مجمع‌الجزایر به موریس مخالف است و موقعیت این پایگاه را برای امنیت ملی آمریکا حیاتی می‌داند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/657400" target="_blank">📅 17:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657399">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
نخست وزیر پاکستان دقایقی قبل در پیامی در شبکه اجتماعی ایکس در واکنش به تحولات جاری منطقه‌ای ناشی از نقض آشکار آتش‌بس توسط آمریکا و ادامه تجاوزگری رژیم صهیونیستی در لبنان نوشت: از همه طرف‌ها می‌خواهیم که خویشتن‌داری کنند و به صلح فرصت دهند زیرا این هدف نهایی در شرف دستیابی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/657399" target="_blank">📅 17:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657398">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ایران از هفته پیش گفته بود پاسخ می‌دهد
ناصر ایمانی، کارشناس مسائل بین‌الملل در
#گفتگو
با خبرفوری:
🔹
ایران از هفته پیش اعلام کرده بود که اگر لبنان مورد حمله قرار بگیرد، پاسخ خواهد داد و این از نظر ایران نقض آتش‌بس است.
🔹
آتش‌بس که برقرار شد شامل لبنان هم می‌شد اما متاسفانه نه‌تنها صهیونیست‌ها اجرا نکردند بلکه آمدند بخش‌هایی از جنوب لبنان را اشغال و بخش‌هایی را تخریب و کشتار کردند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/657398" target="_blank">📅 17:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657397">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
لهستان، فرودگاهش را به روی زلنسکی بست
🔹
لهستان که همواره از حامیان کی‌یف به شمار می‌رفته، در اقدامی خبرساز، استفاده زلنسکی، رئیس‌جمهور اوکراین و دیگر مقامات اوکراینی از فرودگاه خود در ژشوف را ممنوع کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/657397" target="_blank">📅 17:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657396">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCzERuyVCZNJKTRl1bh99L70TJ70g3Cio-xeJXbrvQ8adBMXv6fwFlCrYm5Lfb0zu61_AXwoLV9rwaUs1QDFoFZ0kO0C-SuR64n6gPqGXTl4NJhhpWK3BVBromr_hQl3Y8BkPRuu-7YlYtjQ2dbDQmEL-cTppwXv3eTmgaSYMl2gbAZHmjNAlE6Y8tirF5pIrrt6Kam8qb02QLZIdkuBRX_MhiBNdLn9L-wjIU2hVsprq-LzfT-qgjkPvEMXH70GwyZ44hbPXNHpruWVMI7B9b9o3ksvRpOwmf9mAcQBSTKz79xchQxuhuNBzFK4X6WNNRzsyHO5WnMLI5Ldjhr9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران معادلات منطقه را جابه‌جا کرد | حمله ایران به اسرائیل؛ آیا قواعد بازدارندگی در خاورمیانه تغییر کرد؟
🔹
درگیری دیروز و امروز میان ایران و اسرائیل می‌تواند یکی از مهم‌ترین تحولات ژئوپلیتیکی سال‌های اخیر در خاورمیانه باشد؛ تحولی که پیامدهای آن احتمالا به‌مرور زمان آشکارتر خواهد شد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3221488</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/657396" target="_blank">📅 17:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657395">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
سی‌ان‌ان به نقل از یک مقام آمریکایی: ادعای اسرائیل مبنی بر اینکه آمریکا موشک‌های بالستیک ایرانی شلیک‌شده به سمت اسرائیل را رهگیری کرده، صحت ندارد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/657395" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657394">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
وزارت دفاع عربستان سعودی: آنچه درباره هدف قرار گرفتن پایگاه الأمير سلطان در الخرج منتشر شده است، «صحیح نیست»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/657394" target="_blank">📅 17:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657393">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AueKdaCqRGSJP34W-LavWxrqmWMTO50cgX0SVmVcjOC5Ax03sUgya6j2ebAb6NZKG-uxVlm6W0-M3WQDgISnbPlqxKfd58sTCDi6dAWj57RHl-QZgSTU6jN4CUhP-Yr9GNziqycKDNG_k3rxn02AErrdBDw3_7jBmrNlwTSLQh4fwGAuSnliJm-5RxpLFNG7zg_BT8XENgEKjFHjDt9fJi3XOfSdWcT6X8Cqm8W2dLhmXD80FjJK_ZjmoUGml2ewvWuE1kTJuRpZULVUKHaLyhSbKH29LgX2_rfPuq9DFjrQ4SH6GrPf803DLhhv2JIPQ2M_Dw3PLWkuQSfvTmEYYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/657393" target="_blank">📅 17:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657392">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
نتانیاهو جلسه امنیتی برگزار خواهد کرد
🔹
به گزارش تایمز اسرائیل، بنیامین نتانیاهو، نخست‌وزیر رژیم اسرائیل امشب ساعت ۹ به وقت محلی جلسه کابینه امنیتی را در بحبوحه درگیری با ایران و حزب‌الله برگزار می‌کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/657392" target="_blank">📅 17:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657391">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ازسرگیری پروازها در فرودگاه بین‌المللی دمشق
سازمان هوانوردی غیرنظامی سوریه:
🔹
فعالیت‌ها و پروازها در فرودگاه بین‌المللی دمشق از سر گرفته شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/657391" target="_blank">📅 16:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657390">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/077152c1ab.mp4?token=DgyFP8qUTYfmfyi2kPjf60qZDGCeSuB3HBf500dHe2cZKuqdYuLBW-ReWMRdrguhTEMGhJTdsfgV9b733DTWvmWdj9JgpqWZSfz-e559WKx545uEU25ckPfETPAWjEqmiMpeUrZDwfmYZjowmpWwWS76NZS7XEvHo7ZYePBF9qma2XqGOWkS1OnN19pvKBiW6TXMhiIVnjsfcfLMCTXIZ4JAAMF-sj1XLgcEFJoSG0l9Q0EAxa86DphMhR6GDKxcqrL-ML7978JsFphGYNMe2ZqEucv7O3BtX60_gTUfPl-Ci5uOAPUXrE4PuJS_NeuLU2-KTcEXCaG0wQwkqxyAsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/077152c1ab.mp4?token=DgyFP8qUTYfmfyi2kPjf60qZDGCeSuB3HBf500dHe2cZKuqdYuLBW-ReWMRdrguhTEMGhJTdsfgV9b733DTWvmWdj9JgpqWZSfz-e559WKx545uEU25ckPfETPAWjEqmiMpeUrZDwfmYZjowmpWwWS76NZS7XEvHo7ZYePBF9qma2XqGOWkS1OnN19pvKBiW6TXMhiIVnjsfcfLMCTXIZ4JAAMF-sj1XLgcEFJoSG0l9Q0EAxa86DphMhR6GDKxcqrL-ML7978JsFphGYNMe2ZqEucv7O3BtX60_gTUfPl-Ci5uOAPUXrE4PuJS_NeuLU2-KTcEXCaG0wQwkqxyAsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: تنگه هرمز مال ایران و کشور عمان هست، به هیچ قدرتی اجازه دخالت نمی‌دهیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/657390" target="_blank">📅 16:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657389">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: بند ارجاع ایران به شورای امنیت از قطعنامه آمریکا حذف شد
لارنس نورمن، خبرنگار وال‌استریت‌ژورنال:
🔹
پیش‌نویس قطعنامه آمریکا در نشست شورای حکام آژانس پس از اصلاح، به قطعنامه مشترک آمریکا و سه کشور اروپایی تبدیل شده است.
🔹
در قالب یک مصالحه، بند مربوط به ارجاع فوری پرونده ایران به شورای امنیت سازمان ملل از متن پیش‌نویس حذف شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/657389" target="_blank">📅 16:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657388">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5a518dd2.mp4?token=Na46LzKAqCZ64qxrLEvQNSADrNEaLvs7y9s6YZSUHqWq90JMjrnapSAaIvgdWrZKb7Oa_cNIfgjR7mWnAc2_hoaM4kOLUfp6bIn1XoOiEbCcoM-weyVpPMmeCLrPq4Ma4y5y8l8PpOf-JGBAMTlxeAn0iwBB2ycpOdBJa6BRqpF3kPN4S5tiGd20YRAgPBfU0CzkxuIAUuwNBIbm6D7tcESnob5zXnRa6bcPWxgJ3gODXE6Kfp7OJH9t9QZMG0XZtGAYBa_RsmDtiApyptKzzzoakKYG06CHw3AHDnAEZvdxMRbmdyYLZFc2dcGsY6mBRx-tt1S016G0gSQbqmiveiIAFWwlb-lkuYgNR3j_AmJ0lh-8Izisph_gTnxlQAHQaJrmSxSyLWXgpfHqLcVTgQfto1tyAj9o3z96NedfPBvi011o-uPOYRlTetf_GcUmJVDJdRE9LgrwkBnh2xs4ST82zKYlNLMdtJJlEwhKsDSlTXqSWPchxWIj8GK-DpngQ9x5LLjkQiM6DLDNCFlNSdbBQu5-wXwWVm5xlti7SUF5cnzpPEm4B-9QwVc126eU4sYmyX5iJOuEuf115gEv-LRVGwDqDaUv83u6nY9vd7cvfDTMGAUUM05m_sP7G7kGsd5_wmElRGfRZUHKmpBB8dotlucHdHP8gohkYZxUs0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5a518dd2.mp4?token=Na46LzKAqCZ64qxrLEvQNSADrNEaLvs7y9s6YZSUHqWq90JMjrnapSAaIvgdWrZKb7Oa_cNIfgjR7mWnAc2_hoaM4kOLUfp6bIn1XoOiEbCcoM-weyVpPMmeCLrPq4Ma4y5y8l8PpOf-JGBAMTlxeAn0iwBB2ycpOdBJa6BRqpF3kPN4S5tiGd20YRAgPBfU0CzkxuIAUuwNBIbm6D7tcESnob5zXnRa6bcPWxgJ3gODXE6Kfp7OJH9t9QZMG0XZtGAYBa_RsmDtiApyptKzzzoakKYG06CHw3AHDnAEZvdxMRbmdyYLZFc2dcGsY6mBRx-tt1S016G0gSQbqmiveiIAFWwlb-lkuYgNR3j_AmJ0lh-8Izisph_gTnxlQAHQaJrmSxSyLWXgpfHqLcVTgQfto1tyAj9o3z96NedfPBvi011o-uPOYRlTetf_GcUmJVDJdRE9LgrwkBnh2xs4ST82zKYlNLMdtJJlEwhKsDSlTXqSWPchxWIj8GK-DpngQ9x5LLjkQiM6DLDNCFlNSdbBQu5-wXwWVm5xlti7SUF5cnzpPEm4B-9QwVc126eU4sYmyX5iJOuEuf115gEv-LRVGwDqDaUv83u6nY9vd7cvfDTMGAUUM05m_sP7G7kGsd5_wmElRGfRZUHKmpBB8dotlucHdHP8gohkYZxUs0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از صد شب شما مردم بگویید...
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/657388" target="_blank">📅 16:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657385">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df2aa9553.mp4?token=sUW6an4XM1v5qWHoHEHEsYgLpMoPxjMqnPeTIVMVETZdG1d87oHjhOH07pU7-WnF5XYWpm7yhxe9fFTInP_XNdd2RL5r-x8KyWEa5Cg8VrOZiGn647sdxIEhGZ_wjxO9A8P65Fbdy7ImN9J9s_3X5z0jyGsEclkFj-y4pT4__oeER_w0pKOMS7rcUYTqb8BaoQ8_QjIjQtjh3A0u1E-d5lWlKORJspeSceZu88F_ODf4KJJEjBP-AeU1BoojkOMxjhRU_8u4Z6VPSGOfXbQl1rVnNTzgAQQep1VStfXb2v_X23fd2ER4fBh4Z1nLOSAEHnSQLy1On9Qr3H9_19GJMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df2aa9553.mp4?token=sUW6an4XM1v5qWHoHEHEsYgLpMoPxjMqnPeTIVMVETZdG1d87oHjhOH07pU7-WnF5XYWpm7yhxe9fFTInP_XNdd2RL5r-x8KyWEa5Cg8VrOZiGn647sdxIEhGZ_wjxO9A8P65Fbdy7ImN9J9s_3X5z0jyGsEclkFj-y4pT4__oeER_w0pKOMS7rcUYTqb8BaoQ8_QjIjQtjh3A0u1E-d5lWlKORJspeSceZu88F_ODf4KJJEjBP-AeU1BoojkOMxjhRU_8u4Z6VPSGOfXbQl1rVnNTzgAQQep1VStfXb2v_X23fd2ER4fBh4Z1nLOSAEHnSQLy1On9Qr3H9_19GJMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشکر شهروندان لبنانی از ایران پس از حمله شب گذشته
🔹
پس از حمله ایران در پاسخ به نقض آتش‌بس و حمله به ضاحیه جنوبی بیروت، برخی شهروندان لبنان با انتشار تصاویر موشک‌های ایرانی از ایران تشکر کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/657385" target="_blank">📅 16:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657384">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
اعلام جزئیات مراسم وداع و تشییع پیکر رهبر شهید انقلاب اسلامی
معاون امنیتی انتظامی استانداری خراسان رضوی:
🔹
برنامه تشییع و وداع با پیکر مطهر رهبر شهید از تهران آغاز خواهد شد. پس از ۳ روز وداع و یک روز تشییع پیکر مطهر در تهران، یک روز تشییع در قم انجام می‌شود و پس از آن نیز یک روز تشییع در مشهد انجام می‌شود.
🔹
بر اساس مصوبه ملی، هر گونه اطلاع‌رسانی درباره زمان و جزئیات دقیق مراسم تشییع توسط دفتر حفظ و نشر آثار رهبر شهید انقلاب اسلامی اعلام خواهد شد.
🔹
تدفین پیکر مطهر در مشهد صورت می‌گیرد. البته مراسم تشییع و تدفین، همزمان صورت نمی‌گیرد. پس از برگزاری مراسم تشییع، مراسم تدفین در حرم مطهررضوی در شرایط مناسب صورت خواهد گرفت./ اخبار مشهد
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/657384" target="_blank">📅 16:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657383">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
لغو تمام پروازهای کشور تا اطلاع ثانوی
شرکت فرودگاه‌ها و ناوبری هوایی ایران:‌
🔹
در پی صدور اطلاعیه رسمی هوانوردی (NOTAM) توسط سازمان هواپیمایی کشوری مبنی بر بسته‌شدن فضای پروازی غرب کشور، تمامی پروازهای فرودگاه‌های سراسر کشور تا اطلاع ثانوی لغو شده و انجام نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/657383" target="_blank">📅 16:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657382">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
۱۵ نفر در پی حملات اخیر رژیم صهیونیستی مجروح شدند؛ تاکنون هیچ شهیدی گزارش نشده است
رئیس سازمان اورژانس کشور:
🔹
۱۴ نفر از آنها مربوط به شهرستان ماهشهر در استان خوزستان و یک نفر نیز از شهر تهران هستند.
🔹
یک نفر همچنان در بیمارستان بستری است و ۱۴ نفر از مجروحان پس از دریافت خدمات درمانی و اقدامات لازم، ترخیص شده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/657382" target="_blank">📅 16:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657381">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
رژیم صهیونیستی مدعی توقف تجاوزات به ایران شد
یک مقام ارشد اسرائیلی مدعی شد:
🔹
عملیات تجاوزکارانه علیه ایران به دستور «دونالد ترامپ» متوقف شده است اما این رژیم همچنان به تشدید حملات در لبنان ادامه خواهد داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/657381" target="_blank">📅 16:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657380">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
احتمال تأخیر در برخی پروازهای حج تا ۷۲ ساعت
رئیس سازمان حج و زیارت:
🔹
با توجه به شرایط پروازهای بازگشت حجاج احتمال تاخیر در برخی پروازها حتی تا ۷۲ ساعت وجود دارد.
🔹
برای فردا (سه‌شنبه ۱۹ خرداد) ۱۰ پرواز پیش‌بینی شده که امیدواریم بخش عمده آن‌ها انجام شود.
🔹
روند بازگشت حجاج با سرعت بیشتری ادامه یابد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/657380" target="_blank">📅 16:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657377">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qr3Bwyn87ipesRV7tQgW6QxBGXTiZjGC83hX_lohw_lFAumasOCcnDLElqO_ljsilrOloTRf5sqVTaTyZKPRKk5FCnjm8TqEyI0Mw7LOuf3Rwc85cxJ0h0rILT2uNZcfa_5XNXcSW4X1PTkRn0rWUlMFUQ-FWEHdsWPQwMXRXK06ou7Rvk7Bn3ro84Lugo4qWo_oLEiSMwiMz8n-hFdLA84HTu9dfNc8TN4RgKeEcEXgkJtHMkbT2iVm149-cTYcEbQpHpjLLRkbD41R_hA1JGZnOgRZ6RqaLYvRclVNa30dWsKQeXl8EJObzfgwVePBmida5MgJOaGw7fO0GZEhcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzoV9losd0BwGg2ssCFBjwUJEqk3B0m-024H66zsb-zLgyrHKNp60r4kYXlHN6E4bdxrlcC8Sp6Tn2h0pDFnlL04EObF57ht0ytUfinJAqLWumPIlUHFKmteMFnLkhrtrqzhHVtqn92Tvhe2NnVXZvaEjaHmkY7XQ1iGWbehKB7qPvYdIAHLbhQDQOdum2Hbx7M7mgcwgaD6hACdcW0nC3AqCjha3OQ2IJv5clxofUgIFaLohBlVRs5iUlHNjj6NNwIY8UIVxyoZTINROoObJv_w8stteBxeqXCkprsMYWjfemZNF_TRqfXDqRebZ3sM5m_zipwVF43nodA5Fd6P1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J581VRCZoW_BQ8f3jk_OSJp6p9m0SARuK-6gC65DN-X3CiTQ2ejuEVP56U0Hw2v66AQ5ONFpTZhGC1fYuY_HPbMBpY_K7zHv6FnwhmzunkKIG9qEl75t3IUiqMm7XcQpeZiTeRL42VrGFjT5w56k4Na4HOxwCtcnRbR62PKpAC_x_nxsJNZ74UMnB2MZl1dzDcXg-RKgb9QwQeFg-DI5f-R14Dg9lH8vJLaAbylTJJiSMse6s7BAT8nqdIydw3bsKg51Z2P0ZmOW-jGW2PPCzOPsjYSqF2iq0vdgMpWtE_iM02ORNqvESd0tImX7Kbw_p4c9MY9YVeFx-TOvvjaUug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هشدار درباره مارهای سمی در کمپ تیم سوئیس پیش از جام جهانی ۲۰۲۶
🔹
فدراسیون فوتبال سوئیس با نصب تابلوهای هشدار «منطقه مارهای سمی» در اطراف کمپ تمرینی خود در کالیفرنیا، به بازیکنان و اعضای تیم درباره حضور مارهای جرس هشدار داد.
🔹
این کمپ در منطقه کارمل ولی سن‌دیگو، زیستگاه طبیعی این مارها قرار دارد و از اعضای تیم خواسته شده برای جلوگیری از هرگونه حادثه از ورود به مناطق طبیعی اطراف کمپ خودداری کنند.
#جام_جهانی_۲۰۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/657377" target="_blank">📅 15:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657376">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
آتش‌نشانی تهران: هیچ حادثه مرتبط با جنگ در پایتخت گزارش نشده است
سخنگوی آتش‌نشانی تهران:
🔹
از بامداد شب گذشته تاکنون هیچ مأموریتی مرتبط با جنگ یا حملات احتمالی در استان تهران به این سازمان واگذار نشده و در سطح شهر نیز حادثه یا آسیب مرتبطی ثبت نشده است.
🔹
صداهای شنیده‌شده در برخی مناطق منشأ غیرجنگی داشته و اورژانس و سایر دستگاه‌های امدادی نیز وقوع حادثه‌ای در این زمینه را گزارش نکرده‌اند./ جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/657376" target="_blank">📅 15:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657375">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkF4X1ocqkXs1LmvPtcldJOYu4bkzTvNzlXruYFXX76mKf0yJx2KOpPnS1GFmzpC2I7go7QFYJvawu6oUWD_f6hvFuM3228QP20uCskgcM95eHpdxipz72KGnHb4RWf3EVzZuM-ObmTUuY5DGn0HJjk_x-FrOBYj8q8Ga1EMcDzh1Kg8uxhYNEa49UxiRPHqR4ArZ20q5jbG_fEZ9a_98aFhZvy2BKb0Eg-YBeC_whZqch7_1FMXvkztOkmdqd_juQbKJdqSH1kW-sm87K0eYS_jRyKGXQfTgJl69mHseSHm7gx4qXya-5R7rKuRgdbWcT7cY62ah-v-IkJVGGCF7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آژیرهای هشدار در شمال اراضی اشغالی در پی حمله موشکی حزب‌الله به صدا در آمدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/657375" target="_blank">📅 15:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657374">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ادعای کانال ۱۴ به نقل از منبع صهیونیستی: نتانیاهو تماسی با ترامپ انجام داد که آن را «خوب» توصیف کرد
🔹
نتانیاهو می‌گوید تماس با ترامپ از نظر مواضع «هماهنگ» بود؛ اسرائیل اجرای «معادله ضاحیه» را متوقف نخواهد کرد.
🔹
شلیک به سمت شهرک‌های اسرائیلی با بمباران ضاحیه مواجه خواهد شد. /انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/657374" target="_blank">📅 15:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657373">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT_cDKdbCZZfa89R8S8D7Y2cZqkioBixIgtGYCXmyjTL1iGjQpJLMSVdrztg9dHiunpob4J_ZPIUR53SBmQvBnhV4G8KnScYc6sSIKTWi2B-SOVFPIcTjHk4MYLYvewbpThdYVi25105TPsI_EiEQKIstbS5xZmS7qYOpGwt536mez2LIu1WLdbfNZpds3UGqxikDf3bmZTSP73FsU2BZ09lFoc7GLasjyl07Q5bgWFPokmiLEED35BpK7Yy78RMlc1dx_9EsGhQiH4PcdgPuIFAPtFGmcA0xp4dtFtb5mzOL60GeCvx8m1cRx4lZTzkBJqOo2KWhtdYg8O0s0wlJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله هوایی رژیم اسرائیل به منطقه مسکونی در صور لبنان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/657373" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657372">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdRvC77Q-Nj8RZx2TmrXYX7rj6YutlkFx88aPJWzEmjqdMVfhGLdv480lAum589Fc47NgtzFL0Ycj8wCAHAqRqPbXZU4APPQFOyqxDGLWSB26UMOCmhWXxI_c0PtSAEAnhpgdm271FMbeQPPRry5ENrckzjpqYgg5qwKYBrpLGT8S-1IQ7O1xYfdrgpoa-uApWUlhEV7jcuKhTQDcq0TN7LdOjM6fiCNx5rTe4BLN54aVmxOppSKnDlSM-dzpjor6D9_qioHNQ-fT_eoyVfhpYr9tymVjj5OrrO6vBbI98TisN1H7f26H5Um1O9n-Fuws3_HKbzd2vRmfQRW73sq_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله هوایی رژیم اسرائیل به منطقه مسکونی در صور لبنان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/657372" target="_blank">📅 15:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657371">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
فرمانده کل ارتش: در صورت تکرار تجاوز، پاسخ شدیدتری می‌دهیم
سرلشکر امیر حاتمی در پی نقض مکرر آتش‌بس از سوی دشمن و صد روز مقاومت ملت ایران:
🔹
دشمن با عهدشکنی نشان داد به توافق پایبند نیست، اما حضور و ایستادگی مردم روحیه نیروهای مسلح را برای دفاع از کشور تقویت کرده است.
🔹
فرمانده کل ارتش با تأکید بر آمادگی کامل ارتش جمهوری اسلامی ایران هشدار داد مسئولیت تجاوز رژیم صهیونیستی بر عهده آمریکا است و در صورت تکرار شرارت‌ها، پاسخ ایران شدیدتر خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/657371" target="_blank">📅 15:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657370">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqMmsOjRudaViTuHN5XqN5bn6LS1uzJ-1XeTjUCjDaUqiGqZKrUmmoFqFtggwIN7uMeZ-op-Xd2lBdlhhIFy49517VI2y4xGoGuMhyOVA1jLwW3lDYZ4qbFCMbL0U14zXurwzgmUSTLaUhSj8qMbDYHqN3Qz4nnAC1Isp12fWExLxaA_hC-uqdM1_Avte6YXoM_1WLNeGp-XsLIQcF4jN76LlpZ-pwI1RQGfYRDvtva51Xtm8MWgbPwLDdWjTnQA8fFJXx6bZkh_WX5eTEE9MOD0N5rBUKnyFuN70pCNTU2_nnasNOWYwemxSQU3gI8VGmndgxAVZuTklGUwL_Y66Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای تعرض یک ملی‌پوش ایرانی به دختر ۱۴ ساله در ترکیه
دیلی‌میل:
🔹
یک فوتبالیست ملی‌پوش ایرانی در جریان اقامت تیم در هتلی پنج‌ستاره در ترکیه، با اتهامی جدی از سوی خانواده یک دختر ۱۴ ساله بریتانیایی روبه‌رو شده است.
🔹
پدر این دختر مدعی است بازیکن مذکور پس از گرفتن عکس، از طریق تلفن همراه دخترش برای خود پیام فرستاده و سپس پیشنهاد رفتار نامناسب داده است.
🔹
به گفته او، خانواده موضوع را از مراجع قانونی پیگیری می‌کنند و مدعی‌اند پیش‌تر نیز شکایت مشابهی درباره یک دختر ۱۵ ساله مطرح شده است؛ گفته می‌شود مسئولان هتل همکاری لازم برای ارائه تصاویر دوربین‌ها را انجام نداده‌اند./ رکنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/657370" target="_blank">📅 15:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657369">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0270d3c6ba.mp4?token=G7jHfF6kX6MjWIzE59OuMkwSaZxMuaxrIt8oEo9QhoiyGyt8tR9l0VBX2zz6A4G2VU9DjG3excXqt3oChyuv-JLbIPqqPTR4ucfeS3sMUqB3F1VrRtBFqRl4-HVWVPj5zZwHVzMU4uyZHsFHlqB2xQ747_-aQootrsXtTmybPyiYEa_Q8LOeg-YN2Dcby0sydYYfN5F-beZThv776uePjiEfF1IY7qmxzQ6dU7O_27C5JWz9Kw0ckAq4fr1OkFSh-MKA7G-oN37JPnQUWXgYM2imZr_M9YytoFYVUwBF0dHR3dsS3qvUrebPrvZXZ5qh6cPgk4lpvlMfLOZFDX21wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0270d3c6ba.mp4?token=G7jHfF6kX6MjWIzE59OuMkwSaZxMuaxrIt8oEo9QhoiyGyt8tR9l0VBX2zz6A4G2VU9DjG3excXqt3oChyuv-JLbIPqqPTR4ucfeS3sMUqB3F1VrRtBFqRl4-HVWVPj5zZwHVzMU4uyZHsFHlqB2xQ747_-aQootrsXtTmybPyiYEa_Q8LOeg-YN2Dcby0sydYYfN5F-beZThv776uePjiEfF1IY7qmxzQ6dU7O_27C5JWz9Kw0ckAq4fr1OkFSh-MKA7G-oN37JPnQUWXgYM2imZr_M9YytoFYVUwBF0dHR3dsS3qvUrebPrvZXZ5qh6cPgk4lpvlMfLOZFDX21wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عراقی خبر از حمله پهپادی به پایگاه‌های تجزیه طلب‌ها در کردستان عراق دادند/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/657369" target="_blank">📅 15:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657368">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">📷
ادعای شهربانو منصوریان با انتشار تصویر دست زخمی خواهرش: رئیس فدراسیون ووشو با چاقو به الهه حمله کرده!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/657368" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657367">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
۱۲ اصابت از شب گذشته تا کنون؛ هیچ مصدوم و شهیدی گزارش نشده است
سخنگوی جمعیت هلال احمر:
🔹
از ساعت ۴ صبح بامداد امروز دوشنبه ۱۸ خرداد، کشور ما مورد حمله دشمن صهیونیستی قرار گرفت.
🔹
تا این لحظه ۱۲ اصابت در کشور به ثبت رسیده است؛ هیچ شهید و مصدومی به ثبت نرسیده و آماده‌باش هلال احمر ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/657367" target="_blank">📅 15:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657366">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3lUChKlGg3UspVdjZVp23GNfvfcsM6vVQxMGQ2glYTMZ5aoSO_dLrkvCFqiLFl2_sHyhihpRGz6R3F4ZjEPCrwMl6H8rgiX-QzVow6K87plkhH7JsxdSE5D_bHMs-Jwpu0_fWNtcKBcuqDU2CDZFKLAp3HvfGGBQi1EoEW--avUQ3DjIAQFgvqeUiO2pKy6QmX9qa-UYSCuIutrzhkpHWs7o51tRvop08L-lk8xbguXAtsE3Nc-rGwVAz7nv1jmUlQ7Bo2rlRzm_hMqm0FLA61aTw0d6NE2YNPyU0K1esp272nc8V-noa2qBsLBRZNtB-82dX16eJTYFNVjfaZO7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: دیپلماسی و دفاع دو بال قدرت ملی‌اند؛ نه میدان را ترک کرده‌ایم و نه میز مذاکره‌را
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/657366" target="_blank">📅 15:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657365">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSMwFhwhmfJV5SfUlPJqIOdXgntr-mcuqFjizr7k1iQdd1w4uXTZ13C_aqL8XK74DNyjKQVj1Abh6EWWHCdBhh97yzijpWU2YNz2uyDYbFQWRrVpkhQYshQeaOJ7oaw8SSxFEn52lfzTvWBmxDeLgzFvE7sJuSWg98rvRPZemJHQWSXHCnoDEgj0h2Uw3UepB3PoBJRIYT-TOIuScm4ShAGWEj3B_Kfk5THNQMaxz0fFI0br0OKwEUk1xpweD6rffwj5LZl5fvm5tOpl3k0cAnK4BQ8ra5ee3MkFHPdZcV0b23InxtpDoXJP2F4ncgVUMYatksSl1Z2khHoBqRQ5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هواپیمای اماراتی در مهر‌آباد فرود آمد
🔹
داده‌های ناوبری پروازها، تردد یک فروند هواپیما از مبدا امارات به مقصد تهران را در آسمان ایران رصد کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/657365" target="_blank">📅 15:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657364">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
کانال ۱۲ رژیم: تماس تلفنی جدید بین ترامپ و نتانیاهو
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/657364" target="_blank">📅 15:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657363">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
عراق آسمان خود را به روی پروازها بازگشایی کرد
سازمان هوانوردی غیرنظامی عراق:
🔹
حریم هوایی این کشور برای پروازهای ورودی و خروجی در همه فرودگاه‌های عراق دوباره بازگشایی شده و پروازها از سر گرفته شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/657363" target="_blank">📅 15:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657362">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2att15hk28xM6ppf6r8lMe5FeEvnxtYZNad3LD08n8h_Guirbu5i9mBWpHqUkGw0SYM9x2ZEzVcMNBlPMJK-_pJ124nlnrraWkBfDTX4r2pztAKmN3HOjoLGKBBxHkgI6hcaIllss0HJFrtO7Wrdfzsqc7Ie7NVZtWwtmrq-jyFBJ6LGry7f_y7_Ecv9WmNFQMzSV_kODNGHmCJ-X-Iydl-vxR2XCFjyGlLIxsQATRp7JfgOx2eo9GMjUOiElAedTm1709Pi0ZdR5cDd-hRy-E8uOTzqTSbT6yZB-B20n8wNKKensW2nCPjjtuyDbDJ4WKpksYKuDreIJnhTmH-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت به ۹۴.۷۴ دلار کاهش یافت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/657362" target="_blank">📅 15:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657361">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): در پی تجاوزات و شرارت‌های رژیم سفاک صهیونیستی در جنوب لبنان و منطقه ضاحیه که با حمایت آمریکای جنایتکار صورت گرفت، نیروهای مسلح مقتدر جمهوری اسلامی ایران در راستای حمایت از مردم مظلوم لبنان، پاسخی دردناک به این رژیم دادند.…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/657361" target="_blank">📅 15:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657359">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3jhc7uOWB2T90HTnCcev0Mb5WNU7oiX2Ghg1gFeLEgk2BJRDkz1cwwz3b_7QXna6paId_Bn4B-P3RTUMHSrcPkr9LnI56EQ2CVmslE_XK7bM4XrmO2VKUZfYjnRQJFZMipfqN_vtGU9t4300fgfmCrabzBo77pMGebk4qo-LsXhGNb7Z1Kz4tauMhoKbLwJ23SzVtdDMk5g5KG7HfzcOcrqJxNRcMG5OhhK6MjyKTXv8_vU4qCrZ1O-4sjf8tAM3bkAVvVyb0PfuLj8Vj-_nxpKbYm1CBtBz5M6b1e6ZT1Z2WKWMi6la9KGwC6oF2BsEUtmQx9ujBpXZBZg_wiG2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر فدراسیون فوتبال
🔹
۳ روز مانده تا شروع جام‌جهانی ۲۰۲۶
#جام_جهانی_۲۰۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/657359" target="_blank">📅 14:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657358">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
اسرائیل هیوم به نقل از منابع ادعا کرد: رژیم صهیونیستی و آمریکا پیامی را به ایران مبنی بر این امر انتقال داده‌اند که اگر ایران مجدداً حمله نکند، حملات بیشتری علیه ایران صورت نخواهد گرفت
/ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/657358" target="_blank">📅 14:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657357">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خبرفوری
pinned «
♦️
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): در پی تجاوزات و شرارت‌های رژیم سفاک صهیونیستی در جنوب لبنان و منطقه ضاحیه که با حمایت آمریکای جنایتکار صورت گرفت، نیروهای مسلح مقتدر جمهوری اسلامی ایران در راستای حمایت از مردم مظلوم لبنان، پاسخی دردناک به این رژیم دادند.…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/657357" target="_blank">📅 14:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657356">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص):
در پی تجاوزات و شرارت‌های رژیم سفاک صهیونیستی در جنوب لبنان و منطقه ضاحیه که با حمایت آمریکای جنایتکار صورت گرفت، نیروهای مسلح مقتدر جمهوری اسلامی ایران در راستای حمایت از مردم مظلوم لبنان، پاسخی دردناک به این رژیم دادند.
🔹
پاسخی که رژیم جعلی صهیونیستی و حامیان آن باید از آن درس عبرت گرفته باشند.
🔹
بر این اساس، توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما تاکید می‌شود که در صورت تداوم تجاوزات و شرارت‌ها، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/657356" target="_blank">📅 14:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657355">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7c1768271.mp4?token=PizbC7t1tkFSNl-vI4MLXWBb5Z9oYRBdFr07UBY6628lDdHn56tPweygz7GTP6RVbI79xD9PE-sU0sHJvvlbpVujaUEj1hb21R73P6BTNJdcRkH03A-q8DVCkpkr76ICvSu6mGioBRrUb8jJFEx0tfjJpH9gGnIjqK6vlc2UgCX-Ys7QK2GIiF4k3ZmaRYoYfGbBuDnRPLQdrbFuENA3_GLmj02qSjMmobGGc4HFU11DWvftkQOXGcSvp7fMxe100IUpCrMC-kISY_TdlXlI8oHDIk6GZ0C1wNiV6gveb1FrMy6ZkDGU-k9CS5S_zOAVJuFQDBfIog21s0bavyqVGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7c1768271.mp4?token=PizbC7t1tkFSNl-vI4MLXWBb5Z9oYRBdFr07UBY6628lDdHn56tPweygz7GTP6RVbI79xD9PE-sU0sHJvvlbpVujaUEj1hb21R73P6BTNJdcRkH03A-q8DVCkpkr76ICvSu6mGioBRrUb8jJFEx0tfjJpH9gGnIjqK6vlc2UgCX-Ys7QK2GIiF4k3ZmaRYoYfGbBuDnRPLQdrbFuENA3_GLmj02qSjMmobGGc4HFU11DWvftkQOXGcSvp7fMxe100IUpCrMC-kISY_TdlXlI8oHDIk6GZ0C1wNiV6gveb1FrMy6ZkDGU-k9CS5S_zOAVJuFQDBfIog21s0bavyqVGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ شناوری بدون اجازهٔ ایران حق عبور از تنگهٔ هرمز را ندارد
شناور سرفرماندهی نیروی دریایی سپاه:
🔹
به تمامی شناورها اعلام می‌شود، ورود هرگونه شناور کشورهای متخاصم به تنگهٔ هرمز ممنوع است و در صورت مشاهده بی‌درنگ مورد هدف قرار می‌گیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/657355" target="_blank">📅 14:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657354">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
پلیس: انتشار و بازنشر اخبار، تصاویر و ویدئوهای کذب یا تحریف‌شده در فضای مجازی ممنوع بوده و شهروندان باید اخبار را فقط از منابع رسمی دریافت کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/657354" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657353">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ادعای اسرائیل درباره بازداشت «جاسوس ایران»
پلیس و شین‌بت رژیم صهیونیستی:
🔹
فردی را که برای ایران در اسرائیل جاسوسی می‌کرده بازداشت کرده‌اند.
🔹
به گزارش تایمز اسرائیل، مظنون مردی حدود ۳۰ ساله است که گفته می‌شود حدود پنج ماه با یک مأمور ایرانی به‌صورت آنلاین در ارتباط بوده و در ازای دریافت پول، برخی مأموریت‌های امنیتی را پذیرفته است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/657353" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657352">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-RAIIq0oR9T6mNatuflcUtA19uph9GMZFVaSn6oeaRjxd8Q5HdM7qF0SAxDzUUed1RtvAg41_a9oQjDNFJJlwsA29nMsSKun72m48DvBOj8e3IOfX9tkc4bEV9ORcwRy8p70q93wmgSjA7yd7At25qnjsOwyfL3yqMf_tf0COfIMu1kCE4JRYvyXYVPPtkrOd3ckdcCYHCq7pjMKUMYe_NaBZAna_J-CSWxfcp-XMxV9emkrbVlZdRUNcP2cwZNTnklg3E9GY49AOHLIubg9q2sDOom9H_cNsy8Hgb5rBeeaupCYPb9Dj9BFOF8HyR6v7uvxtR8ds4Yxbhcn9AoNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا اینترنت قطع می شود؟
🔹
حالا که جنگ مجددا شروع شده ممکن است اینترنت بین الملل دوباره قطع شود. ممکن است بانیان ارتباطات آنلاین و مسئولان امنیتی کشور استدلال کنند که ممکن است قطعی اینترنت به نفع کشور بوده و ارتباط جاسوس ها و ماموران امنیتی اسرائیل و آمریکا را مختل کند و جلوی ارسال فیلم و مدرک به رسانه های دشمن را بگیرد.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3221470</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/657352" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657351">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f5954bc90.mp4?token=mO35-7hDcl61AqI8b3Vl30dBxPfXf0pp3ZbKN6KCJrWACry0vHYZm7D_QMhiTgfvjBPH4e4T8un5Vl1b9l2_seuZI0HH7I0c8yfuwyrpWS-QWGLdRkZ7L96-8JB_i9sS46NlCKq0Q8RtPy-ppHQ8nkdZNjMfkF8zhIhFO9K-N1qQUlftR8ItqlSwirACFicJTVRHiePCDz2AzXgIjE1o1NeE7j5C7THuuQFW2QtoXC6JVbRls5uWE0E9jhTs900M97sKEog7x0elgUpLCGABg6cu9bMEtncgGEgnANAW5V_vmHVoMFb5EMemtPRmHBAa0h0KRIGJL7T-E8jjAKYghoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f5954bc90.mp4?token=mO35-7hDcl61AqI8b3Vl30dBxPfXf0pp3ZbKN6KCJrWACry0vHYZm7D_QMhiTgfvjBPH4e4T8un5Vl1b9l2_seuZI0HH7I0c8yfuwyrpWS-QWGLdRkZ7L96-8JB_i9sS46NlCKq0Q8RtPy-ppHQ8nkdZNjMfkF8zhIhFO9K-N1qQUlftR8ItqlSwirACFicJTVRHiePCDz2AzXgIjE1o1NeE7j5C7THuuQFW2QtoXC6JVbRls5uWE0E9jhTs900M97sKEog7x0elgUpLCGABg6cu9bMEtncgGEgnANAW5V_vmHVoMFb5EMemtPRmHBAa0h0KRIGJL7T-E8jjAKYghoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحلیلگر الجزیره: ایران بی‌توجه به واکنش آمریکا پاسخ قاطعی به قمار اسرائیل در بیروت داد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/657351" target="_blank">📅 14:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657350">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ادعای گروسی: ایران باید به تعهدات خود پایبند باشد
🔹
رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی: ایران باید به تعهدات خود عمل کند و از فعالیت‌های غیرقانونی خودداری کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/657350" target="_blank">📅 14:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657349">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhkUegO5xSArJZJM09kwJWZgHY1exjRM6zVuTT_3408LTeA5Sz9byHqTPNdUC_iCV4_Kq0BXEIZ1JovINOzkUByBpA0S1JuaPZ8wuwWMAJlgG2xygnVv1QRAmHQSN52A1V8Ir_kBY0d_VBYkP5qyI9GgSYJLaEHnVfrA54iTnrLltbA0UmsiA35nv5mVBO6MXEB7KPbfyVe2mAwqG5MnHUxvfrDoDATLD5xrkw5VchdPwdSdp6cfTKrpZO440G_IteqaRzBu6n07zjfR4GK6waS-EAy2xLCPAkE_rbji_14vbK7ENM-pexI5EaJP2Ou4bxki5_8XFv-ZifVGLijxmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمین‌لرزه‌ای به بزرگی ۴ ریشتر در عمق ۱۰ کیلومتری زمین، مهرانِ ایلام را لرزاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/657349" target="_blank">📅 14:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657348">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سفیر سابق ایران در امارات: آمریکا وارد درگیری با ایران نمی‌شود
محمدرضا فیاض، سفیر سابق ایران در امارات در
#گفتگو
با خبرفوری:
🔹
شواهد نشان می‌دهد که دولت امارات در یک مجموعه‌ای قرار گرفته که شاید خودش راضی نباشد اما مجبور است که با دیگران هم‌صدایی و مشارکت کند.
🔹
آمریکایی‌ها امارات را تسخیر کردند و پایگاه‌ها متعلق به آمریکا است و باید دید آمریکایی‌ها چه شیطنتی خواهند کرد. ورود آمریکا به جنگ اسرائیل و ایران به مصلحتش نیست و این کار را نمی‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/657348" target="_blank">📅 14:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657347">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWGxpquioKStFX6o-_R2i5nXJcwdIlHFdHBQotmw82jf3lXZcmPqqkSGy-oVQohdaTbHZI-tG-dAHLqHjAbD5IpIuQMpy0QKAYMk4x4CypBThUinrKHhvaJdRk922iGIhWTBvsBzX0JqeSgEUoVKMaiknyxEpjmWQZVsXDMX65J7z1LqBYGlKfDmLOw8jNqXT938qFzPgyWp0YGf6TsWjl80d9OR7lBI3RQsalNRiK8966G1Gs7Q1kSpOBcT4iiyA_3hD3_2VtFHlGrpnoRI2iunzRwDGOZjcbSdg55DBGcELrWDOoH0RCiv3IWypQQ-TYzmsPLJD2kecXSEyoBSoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت سفارت ایران در ارمنستان بعد از حملات ایران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/657347" target="_blank">📅 14:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657346">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnXW140TfwX1euEOdqrrRq3qrNJeQb0dnjUdpYPQGIVIe_Y3yp6vbElH4bqMuaiERWp0WJEaF80YLT2Wcb8F5PwsB6qJrsmqPHd0PH0cLboQcPpgIQKDZ0NCYZhM1X3e-nry1gIwfZC_M2RQb4nw0BZxNUuwQqwbQrTosDUhSqRV-kEub53NNOD-pyVPNslPmgtqF7X7sukB2dtglWcz7eg8qh-8ysbfhEwFz17GBT3Z-KVud8lv07zYov2rMcRciWplUeP-3YrinwzK7YcwWHl6kz5Ry0cPwvKFOb5ePyiO72tK4fNNaZ5VkWjVKZcrNLjmKdR6TuZqkb9acppmQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری که شبکه CNN از ریزش سنگین بازارهای سهام شرق آسیا (کره، ژاپن، هنگ‌کنگ) به دلیل آغاز دوباره درگیری‌ها میان ایران و اسرائیل منتشر کرده است!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/657346" target="_blank">📅 14:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657345">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cefSN9gkv8x22Rjeih07JxlXKST27BOJneeFu_4hypgSt3QklxGbVPVUh7qXcfw3jZCdHEa3vB1i8pQuJmqvyWuaN46deVg7su1tCPQIgoSQCYYQwiRfUHL-Gs47uda28RSFyVv0TET12l7QvH-SzNmRZFsgELofaG3QIc3wk318CZAa6uRbw9Azj1ol1jzF7gnKvT7kk1PhiNXHCTuZTfufLvDhru43d_HWjermtEiJPaWuQOD8aMUyybM7euA3WbxUoDATjccVjXukUDFN4IyoeoMtXLzCo41Cj5jg9l7sMxjYiS33X0lQvMO2EMuvp_ALd_YwZjjTuD95cN4dEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: اسرائیل و ایران باید فوراً درگیری را متوقف کنند #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/657345" target="_blank">📅 14:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657343">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
جروزالم‌پست: ایران سه سلاح هسته‌ای دارد!
روزنامه صهیونیستی جروزالم‌پست ادعا کرد:
🔹
ایران در عمل از دو «سلاح هسته‌ای» غیرقابل انکار استفاده می‌کند و جنگ کنونی غرب با تهران، بر سر خلع سلاح از این دو سلاح است، نه بمب اتم.
🔹
اولی توانایی ایران در بستن تنگه هرمز (عبورگاه ۲۰ درصد نفت جهان) است که قیمت نفت را ۴۵ درصد و بنزین آمریکا را ۴ دلاری کرده است.
🔹
«سلاح دوم» نیز موقعیت جغرافیایی ایران در قلب اوراسیا و کریدورهای حیاتی چین و روسیه است که برتری دریایی آمریکا را دور می‌زند.
🔹
بمب اتم تنها «سومین سلاح» و بی‌اهمیت‌ترین آنهاست. /خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/657343" target="_blank">📅 14:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657340">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: اسرائیل و ایران باید فوراً درگیری را متوقف کنند #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/657340" target="_blank">📅 13:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657339">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
اروپا تحریم‌های جدیدی علیه ایران اعمال می‌کند
🔹
اتحادیه اروپا در اقدامی خصمانه علیه جمهوری اسلامی ایران، برای  نخستین بار با ادعای نقض آزادی ناوبری دریایی، تحریم‌هایی علیه ایران اعمال خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/657339" target="_blank">📅 13:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657338">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69212ac3a2.mp4?token=Zg6k94XIbObl3djF-MGZt-bUvCYpodn4w_bW8DTERGKpUAOsrQ_kaffvI9AYpic7yd2tnsDIeXyVGMWlVGIqWN2I1VV5nv_E15LqkOMKGHJxFLTUAVJV5eMQVRtD9s-zwSFcRqbMyAfpDG774kiQAuQOe_XLSL9Boe1CR6DYcp3uWv6n15SVvfESWmEsQybUA8L_E3s0-3dqEBm-NKfxknTbksAS77DIQb-kUia83ldxZ1g67Wt3EDPJFhKJsUOmMGgk63FObbClTAt1RelIAkWVfzusyjFWSjZXV4IbpsHq0Q7JslcmTlLsMMXQCpRfTE4UPUY3olU9B7XOzaelHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69212ac3a2.mp4?token=Zg6k94XIbObl3djF-MGZt-bUvCYpodn4w_bW8DTERGKpUAOsrQ_kaffvI9AYpic7yd2tnsDIeXyVGMWlVGIqWN2I1VV5nv_E15LqkOMKGHJxFLTUAVJV5eMQVRtD9s-zwSFcRqbMyAfpDG774kiQAuQOe_XLSL9Boe1CR6DYcp3uWv6n15SVvfESWmEsQybUA8L_E3s0-3dqEBm-NKfxknTbksAS77DIQb-kUia83ldxZ1g67Wt3EDPJFhKJsUOmMGgk63FObbClTAt1RelIAkWVfzusyjFWSjZXV4IbpsHq0Q7JslcmTlLsMMXQCpRfTE4UPUY3olU9B7XOzaelHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک کشتی هندی در دریای عرب دچار آتش‌سوزی شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/657338" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657337">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e62e35608.mp4?token=smR-j6_aCUZcc1QY8AQx03S3U6Kwu7V-b9ntfwomj_u3Ge0ALSYqnF8tdj102zJPnpUGQl1AB_Iql-dfA2pXFuwta0r5VIyWOrbS4anQ04ZDBSAkAYtLtu0hXaj_sbLaNAUIyJvbdxKWWXZKzxaAn0honBZTQIvPNd4_bje3f2WI2nN9FWb3msuHojgGHMczIVDEMXPZlNFxIXr3r0wQ-aZooK0YfJDAlgvPehvMgjVp-CyElxtqfpyoAzbblOG6WE_9IcwAqpG-P2WH5suhc6UyNvUJniNa7fsjWGSjYOWD6jHdYmAnDP9KXT9hHAEaHeUndUdookVvKnvI0c2QiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e62e35608.mp4?token=smR-j6_aCUZcc1QY8AQx03S3U6Kwu7V-b9ntfwomj_u3Ge0ALSYqnF8tdj102zJPnpUGQl1AB_Iql-dfA2pXFuwta0r5VIyWOrbS4anQ04ZDBSAkAYtLtu0hXaj_sbLaNAUIyJvbdxKWWXZKzxaAn0honBZTQIvPNd4_bje3f2WI2nN9FWb3msuHojgGHMczIVDEMXPZlNFxIXr3r0wQ-aZooK0YfJDAlgvPehvMgjVp-CyElxtqfpyoAzbblOG6WE_9IcwAqpG-P2WH5suhc6UyNvUJniNa7fsjWGSjYOWD6jHdYmAnDP9KXT9hHAEaHeUndUdookVvKnvI0c2QiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع زلزله ۷.۸ ریشتری در فیلیپین
🔹
زمین لرزه ای به بزرگی ۷.۸ ریشتر جنوب فیلیپین را لرزاند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/657337" target="_blank">📅 13:51 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
