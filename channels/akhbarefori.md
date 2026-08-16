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
<img src="https://cdn4.telesco.pe/file/djbIAeR2SgH0QLY90ep8InQ7S2x7dTt7vaf_Hd-HMmhSscdnBW5BfC4NoNUSKPvBdhwvqIILWFpVpype44retZSXUP-l0ki5J8aLZjlzHvcDk2t7Bcwy656O9lFQJT4hzJP96DDam0LdYPoV5GVhFQHrQtqI9CTL9OC8Jxy6XBQZf6O4wWLLdBsFxWUpTrbihJ8TY_6Dvt28k5uFD81sGVsSmK19bIdlDuDuaAQ3GA640CBurIiBkQjllf7pU-6GkdusZiEGhfFyDeX491J7XFkfugg_6ntBAuIu-LoDR9ftQ6v7bi8nWt2PhsCmw6kc_k1edCcizgizQ7QSnYfQNg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.14M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 02:41:14</div>
<hr>

<div class="tg-post" id="msg-681849">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taXJDbgsCzKZZBj_XcbH34yzo3MBTFzsQvVoQn0hNGLer4EyhS4lvzbx5VMNH0fuB66AWx1x1j2WMMevs4PZ-quvt6a5OE5YPgCAjXIKJJw9PVdOxTmnK7CcjtfWZH8DIvBgcH9XLd2bSAZP86xhervhBJ1eKGQIeRAc0h1cvfEHK8i8fYZe2hXQfXrn0chgVSU8LwjvtadYMkPinKEW_hBtioWFxAyu8rb-NcN1j2d-ZQOad4W81VcSrwQ_XVKbWNDXZsC4fFD_Q15gazqYFWBRJm_WM_Hu11u7wHQRcXkxUaDB69qQlz4e10huuCxNq1eYxQ7q9A1RYbokYrct5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
هر خانواده یک وام تا سقف ۵۰۰ میلیون
✅
بدون سود
✅
بدون ضامن
✅
بازپرداخت تا ۱۴ ماه
برای انجام ایمپلنت و سایر خدمات دندانپزشکی
برای دریافت اطلاعات بیشتر کلیک کنید
👇🏻
👇🏻
👇🏻
👇🏻
https://t.me/arameshdental
https://t.me/arameshdental</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/akhbarefori/681849" target="_blank">📅 02:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681848">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار درباره ایران: اتفاقات خوبی خیلی زود رخ خواهد داد
🔹
دونالد ترامپ در خصوص ایران مدعی شد: اتفاقات خوبی خیلی زود رخ خواهد داد. در واقع، آنها همین حالا هم رخ داده‌اند، چون یک کاری هست که ما نمی‌توانیم اجازه دهیم انجام شود: ما نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/akhbarefori/681848" target="_blank">📅 02:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681846">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
داماد ترامپ امروز با نتانیاهو دیدار می‌کند
🔹
ای بی سی نیوز به نقل از منابع اسرائیلی اعلام کرد که جرد کوشنر داماد دونالد ترامپ امروز دوشنبه با نتانیاهو نخست وزیر رژیم اسرائیل دیدار خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/akhbarefori/681846" target="_blank">📅 01:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681845">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
کدام صنف‌ها بیشترین و کمترین مالیات را پرداخت کردند؟
🔹
با محاسبه سرانه مالیات، پزشکان متخصص همچنان در صدر پرداخت مالیات قرار دارند، در حالی که نانوایان کمترین مالیات را به ازای هر مؤدی پرداخت کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/akhbarefori/681845" target="_blank">📅 01:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681844">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
اردوغان: اسرائیل آغازگر جنگ کنونی در منطقه است
رئیس‌جمهور ترکیه در مصاحبه با الجزیره:
🔹
اسرائیل عامل اصلی و بازیگر اصلی جنگ بوده و تل‌آویو همواره گزینۀ جنگ را تشویق کرده است.
🔹
ما نمی‌توانیم غزه را تنها بگذاریم. هر وظیفه‌ای که در قبال غزه برعهدۀ ما بوده، تا امروز انجام داده‌ایم و در ادامه نیز انجام خواهیم داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/akhbarefori/681844" target="_blank">📅 01:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681843">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تسنیم گزارش می‌دهد: تراستی‌ها؛ ابزار دور زدن تحریم یا گلوگاه جدید ارزی؟
🔹
واژه «تراستی» در سال‌های اخیر از یک اصطلاح تخصصی و کم‌استفاده، به یکی از واژه‌های پرکاربرد در ادبیات اقتصاد تحریم‌زده ایران تبدیل شده است؛ واژه‌ای که در ظاهر، از سازوکاری برای مدیریت دارایی و انجام مأموریت مشخص حکایت دارد، اما در عمل، در اقتصاد ایران به شبکه‌ای از واسطه‌های مالی و تجاری اطلاق می‌شود که مأموریت اصلی آنها فروش نفت، میعانات نفتی و فرآورده‌های پتروشیمی در شرایط انسداد کانال‌های رسمی بانکی بوده است.
🔹
شکاف در حکمرانی؛ اختیار در دست کیست؟
ریشه اصلی بحران تراستی‌ها را باید در دوگانگی میان مرجع صدور مجوز و مرجع پاسخگویی جست‌وجو کرد. در سال‌های گذشته، بخش‌هایی از فرآیند صدور مجوز یا واگذاری مأموریت‌ها در مسیرهایی انجام می‌شد که لزوماً با سازوکار سیاست‌گذاری ارزی بانک مرکزی هم‌راستا نبود، اما در زمان بروز مشکل، این بانک مرکزی بود که باید پاسخگوی آثار ارزی، نوسانات بازار و کمبود منابع می‌بود.
🔹
راهکار چیست؟ برای اصلاح این وضعیت، نخست باید اختیار و مسئولیت در یک نقطه متمرکز شود؛ یعنی بانک مرکزی تنها مرجع سیاست‌گذاری، صدور مجوز و نظارت بر این‌گونه سازوکارها باشد تا امکان پاس‌کاری مسئولیت از بین برود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/681843" target="_blank">📅 01:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681841">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
المیادین: اسرائیل در حال حملات توپخانه‌ای به شهر المنصوری در جنوب لبنان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/681841" target="_blank">📅 01:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681840">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c501c9e4.mp4?token=vpJWFTekccdnp3eDzZb61EvGOlqLaRokVnXXzghmTlbh-HUGkEgCnNApO0e0KIJd9KLc9m9h1FYeFJoZF6zDe4prbFZrUfGwNbxHWkHA3b8ou-KNTDRohYpQ9yh1mr9IUl1b4buUWBjhSfZj-I1dbTpmHqoWdiLpke86dyOPZAXi3bcUxDWwv2JCtjp2zU4pU4yDRbN8wQL6l3qBUAQGVxY8N4vtBFOkbgnFgM9FfVslUizHN8BlbqPgQpH2juHPKjHoxsuyHVeKhL4y7EzXYGfgnxEdrTcYUZL0KB3s_sllvddXSLf_J5sEW0qQL3igb_iuw5MRS8gvUnwIiQbdFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c501c9e4.mp4?token=vpJWFTekccdnp3eDzZb61EvGOlqLaRokVnXXzghmTlbh-HUGkEgCnNApO0e0KIJd9KLc9m9h1FYeFJoZF6zDe4prbFZrUfGwNbxHWkHA3b8ou-KNTDRohYpQ9yh1mr9IUl1b4buUWBjhSfZj-I1dbTpmHqoWdiLpke86dyOPZAXi3bcUxDWwv2JCtjp2zU4pU4yDRbN8wQL6l3qBUAQGVxY8N4vtBFOkbgnFgM9FfVslUizHN8BlbqPgQpH2juHPKjHoxsuyHVeKhL4y7EzXYGfgnxEdrTcYUZL0KB3s_sllvddXSLf_J5sEW0qQL3igb_iuw5MRS8gvUnwIiQbdFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری شگفت انگیز از تصویرسازی ابرها در آسمان نیوجرسی
🔹
ساکنان ایالت نیوجرسی آمریکا، تصاویری از این پدیده عجیب را منتشر کردند که ممکن است نشانه‌ای از بادهای شدید، باران شدید و رعد و برق باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/681840" target="_blank">📅 01:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681839">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک‌سوم مبتلایان به آنفلوانزا زیر ۱۵ سال سن دارند
قباد مرادی، رئیس مرکز بیماری‌های واگیر وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
بر اساس نظام دیده‌بانی عفونت‌های تنفسی مرکز مدیریت بیماری‌های واگیر، ۴.۴ درصد مراجعان سرپایی و ۵.۷ درصد مراجعان بستری، دارای علائم عفونت‌های تنفسی بوده‌اند.
🔹
تست آنفلوانزا در ۰.۷ درصد و تست کووید-۱۹ در ۲.۹ درصد افراد دارای علائم تنفسی مثبت بوده است اما هر دو بیماری در سطح پایینی قرار دارند.
🔹
۸۰ درصد آنفلوانزاهای در گردش از نوع B هستند و نزدیک به ۳۴ درصد مبتلایان زیر ۱۵ سال سن دارند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/681839" target="_blank">📅 01:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681838">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11395e9490.mp4?token=dN7qRlxQGTot_on_Ef_HFFEcdnzaIGHyqOZr2H-e-jXMgGtgz-XvJ5_oHtqeZeWuiUDzH4plERYbv6QHo0a9EnmwE5VzVAnjWz_E7-88SdPvfNKNL4MDgSydU8x1UPT4v2aKPLJHM_-FqtcqLERiefhHvGQ-WsH-rg4KQwqFcBEHoiYX9mRKtN4MiZgFGgUVoCN8sm4vEUX-G7B-izt12AsQbahfxkaiK47IPLrk28R94FKGjFdXwD_Z_qEBuwETb-ckhXPvpuffClHT1mnAbZgfZcZK8aE8bgUAqV9enydvcV8Dzd1CkapMfvNzW8-i01a__eOG0CF_PdYFm65AZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11395e9490.mp4?token=dN7qRlxQGTot_on_Ef_HFFEcdnzaIGHyqOZr2H-e-jXMgGtgz-XvJ5_oHtqeZeWuiUDzH4plERYbv6QHo0a9EnmwE5VzVAnjWz_E7-88SdPvfNKNL4MDgSydU8x1UPT4v2aKPLJHM_-FqtcqLERiefhHvGQ-WsH-rg4KQwqFcBEHoiYX9mRKtN4MiZgFGgUVoCN8sm4vEUX-G7B-izt12AsQbahfxkaiK47IPLrk28R94FKGjFdXwD_Z_qEBuwETb-ckhXPvpuffClHT1mnAbZgfZcZK8aE8bgUAqV9enydvcV8Dzd1CkapMfvNzW8-i01a__eOG0CF_PdYFm65AZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: هنوز نمی‌دانیم چرا با ایران وارد جنگ شدیم
روبن گالگو، سناتور آمریکایی:
🔹
ما از سربازان آمریکایی حمایت می‌کنیم که تلاش دارند ما را از این جنگ بیرون بکشند. اما رئیس‌جمهور هیچ طرح و برنامه‌ای نداشته و معلوم نکرده این جنگ چقدر گسترده است، چطور پیش می‌رود و چطور قرار است تمام شود. مأموریت ما دقیقاً چیست؟ ما هنوز نمی‌دانیم اصلاً چرا با ایران وارد جنگ شدیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/681838" target="_blank">📅 00:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681837">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hv2HkcIlK8S7TMtzOLCmoSOaWiD6KWrOegwC0a64yxQs_UNhT3QvTrEir2612bNPjgwuGYo-Oz6n2uNNj0PUHdTnPx2PAIBER3SGDtXEiPcAGf5A3NGGcXZ2wQWY8-lFAfg9I-BFKq2Xg8xkezmA3234sOKS6dXWDElURddtOX-pmaVA05JOt6muAE5KWFCYo_op5SC3omRlGYH9Ls0M82rCTNN6dJzWC9D8Yd5DQIa0oB1wcFF95RkXLXMT1736BgoHGKQJ0z_uSWO-2O-p3mSOdLrCkvKG091PaE1ukcHDLNd6BH6mpvp5lX-0yim3fdHfnza4J8l2XKHCSO6X_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: از رئیس‌جمهور کره جنوبی درباره تمایلس برای پیوستن به تلاش‌های ما برای خلع سلاح هسته‌ای ایران سوال کردم، اما پاسخ او به این درخواست منفی بود #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/681837" target="_blank">📅 00:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681836">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ترامپ: از رئیس‌جمهور کره جنوبی درباره تمایلس برای پیوستن به تلاش‌های ما برای خلع سلاح هسته‌ای ایران سوال کردم، اما پاسخ او به این درخواست منفی بود
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/681836" target="_blank">📅 00:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681835">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b38253a8.mp4?token=UwXdD0VtsgUE9q7Qet5UuQS2m_U_5qXMuvIhry565P7L9oxBXyZ1tpMZ3oaq0X5eLoYzGXyN5xe0-RPzpH2jpAcRAZ0bMvzHXsq8n-AZtsgoU039OJwFI61qcs98eLoPy2YonwJ0fh63mCdKku_HAP_rs3al6FPZOGWnJDW-wc4W3wiOXeoXWou4WQEO1RGivV6IqskWV-zTE3fQq7PcoNwKBedhjQvd7UZ_5BnUwwErRMqMCefDVrRCL-fyRe4_v89P4ZwZLOZsg4zq0cV032XoZ79mrgY7UqLvnPFdv-nlJlYCCmtX50BP-oDFMtbv3fFY1YnYsl3XYwkhEGVxnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b38253a8.mp4?token=UwXdD0VtsgUE9q7Qet5UuQS2m_U_5qXMuvIhry565P7L9oxBXyZ1tpMZ3oaq0X5eLoYzGXyN5xe0-RPzpH2jpAcRAZ0bMvzHXsq8n-AZtsgoU039OJwFI61qcs98eLoPy2YonwJ0fh63mCdKku_HAP_rs3al6FPZOGWnJDW-wc4W3wiOXeoXWou4WQEO1RGivV6IqskWV-zTE3fQq7PcoNwKBedhjQvd7UZ_5BnUwwErRMqMCefDVrRCL-fyRe4_v89P4ZwZLOZsg4zq0cV032XoZ79mrgY7UqLvnPFdv-nlJlYCCmtX50BP-oDFMtbv3fFY1YnYsl3XYwkhEGVxnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با چند قلم ساده دستگاهی برای سوخته کاری بر روی چوب بساز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/681835" target="_blank">📅 00:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681834">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBOMNB5TBg2WXw7nuqGiUW3YuDu11lGCuUlpN8NzsyB-woWDmeSrT1VmvfL-BJ1up570V2w0ctNU4AhmVBx7Ku-ADWfDkK3Apsa1n38-yUGuN55wL-qMeRPjhfxq_u6N8H8-xOQ2HGP2oXkXh-5BDFfg3RASNW3F3zBY6F9rlG-wgZJic_CPq2JNwdSZlNKbE24dhWmjGL41BKNlkgzIpEN3XzaptXWzvZecUB_COxHC18xPJoHSVrufigR-cKXwZUlyZERxgFhnGfYlADSyxmxDPQ4XyChn6VZybkMhUgLmiisAw7JLbg8grsjjHOkrwiO_VQIdzhjinSxlpTW51A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمایت ترامپ از توافق مکه
ترامپ:
🔹
بسیار خوشحالم که می‌بینم عربستان سعودی، ترکیه و پاکستان اخیرا و سرانجام توافق‌نامه دفاع مشترک مکه را امضا کرده‌اند. این نشان می‌دهد که چگونه خاورمیانه در حال اتحاد است و چگونه کشورها سرانجام قادر خواهند بود از خود به شیوه‌ای معنادارتر دفاع کنند. تبریک به رهبری بزرگ سه کشور ذکر شده. این یک گام بزرگ، جسورانه و مهم است.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/681834" target="_blank">📅 00:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681832">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خبر خوب؛ ۸۰ درصد سطح دریاچه ارومیه آب دارد
محمد کوهانی، دبیر ملی شبکه های محیط زیست کشور در
#گفتگو
با خبرفوری:
🔹
سال گذشته در تصاویر ماهواره‌ای صرفا یک لکه آبی از دریاچه ارومیه دیده می‌شد، اما امسال بیش از ۸۰ درصد سطح دریاچه آب دارد و حجم آب آن به ۲.۵ تا ۳ میلیارد مترمکعب می‌رسد.
🔹
در سال ۹۸ حجم آب دریاچه ارومیه به حدود ۵ الی ۶ میلیارد مترمکعب می‌رسید. تجربه این سال نشان داد حتی اگر سال پرآبی داشته باشیم، بدون وجود برنامه انسان‌محور در سال‌های آتی مجددا دریاچه را از دست خواهیم داد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/681832" target="_blank">📅 00:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681831">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
سناتور آمریکایی: ناو آبراهام لینکلن مشکلات عمیقی دارد
سناتور دموکرات آمریکایی:
🔹
واقعاً مشکلات عمیقی درباره وضعیت ناو آبراهام لینکلن وجود دارد.
🔹
ترامپ مشکلات را در رابطه با جنگ علیه ایران برنامه‌ریزی نکرده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/681831" target="_blank">📅 00:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681830">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
۶ دانشگاه ایرانی در جمع ۱۰۰۰ دانشگاه برتر جهان
🔹
تازه‌ترین رتبه‌بندی شانگهای ۲۰۲۶ منتشر شد و ۶ دانشگاه ایرانی در جمع ۱۰۰۰ دانشگاه برتر جهان قرار گرفتند.
🔹
دانشگاه تهران و دانشگاه علوم پزشکی تهران مشترکاً در بازه ۵۰۱ تا ۶۰۰، صدرنشین دانشگاه‌های ایران شدند.
🔹
دانشگاه صنعتی امیرکبیر نیز در بازه ۸۰۱ تا ۹۰۰ جای گرفت. همچنین دانشگاه علوم پزشکی شهید بهشتی، دانشگاه صنعتی شریف و دانشگاه تربیت مدرس در بازه ۹۰۱ تا ۱۰۰۰ قرار گرفتند. /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/681830" target="_blank">📅 00:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681829">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573c891f09.mp4?token=k4p9qQruifrbVpi_dr5DhzOZhUnUngugiNa9Gil7R7lpYHgW3gd9qVeQNs2_zVbZPdlRGXdzmxVGANxUWZMdqQEzGpsov8go3YiVcoYk5ZvZ8JuKVUMQ2-1q5ZUvfyIMksrNRhwdSnFVS5kRJTVL0vh6uwo8_l_pDwTavFyBWZg-x0iIIyMsjT5l9M_IjrV1Z1DIE2HlQ-Mbud9E3aHsZg_zMK8OUA_b8o8V9SuXbWcduSbUwk_jJVaxV9jK5iMydL7UtkIHEAEmgonAfvp1B4lHkKmHj7GL1qLZ0ys_WMMaUMNslpnUiJMJa5EkfLozgAhh_os9qzoxIbklDnqv3iyRmR_yOZYqmcpBoCeaRuE6R5E2ozRF3AHrKnmmJeuyQBCT1n5b_Y6k7G1J2xz8HfeTb7HmTIJGZUuxwlKH6abYPclgfktoUoJBqBnHtqLWTZrquaG81nx8RzXZgguVizy2Y3YR_9y6Rys8cpZx2uSRczCOMG1rWjpNJaCAwvOxw4V7TCbo7C21ZB-rCazqVFsNZteQuM504pFmkEikpZdx6uHkCdvzsATuLK0u7Z0_K6Lla_WHQ5G_nkPzP_UnNvzMaDpWxPKU_rLL1itfOt__f9fk5t9JZgYVCwsTxjsc5QIV3NfQ6vqcAtE3JYOyMw49l07PmERh22h3sfDva2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573c891f09.mp4?token=k4p9qQruifrbVpi_dr5DhzOZhUnUngugiNa9Gil7R7lpYHgW3gd9qVeQNs2_zVbZPdlRGXdzmxVGANxUWZMdqQEzGpsov8go3YiVcoYk5ZvZ8JuKVUMQ2-1q5ZUvfyIMksrNRhwdSnFVS5kRJTVL0vh6uwo8_l_pDwTavFyBWZg-x0iIIyMsjT5l9M_IjrV1Z1DIE2HlQ-Mbud9E3aHsZg_zMK8OUA_b8o8V9SuXbWcduSbUwk_jJVaxV9jK5iMydL7UtkIHEAEmgonAfvp1B4lHkKmHj7GL1qLZ0ys_WMMaUMNslpnUiJMJa5EkfLozgAhh_os9qzoxIbklDnqv3iyRmR_yOZYqmcpBoCeaRuE6R5E2ozRF3AHrKnmmJeuyQBCT1n5b_Y6k7G1J2xz8HfeTb7HmTIJGZUuxwlKH6abYPclgfktoUoJBqBnHtqLWTZrquaG81nx8RzXZgguVizy2Y3YR_9y6Rys8cpZx2uSRczCOMG1rWjpNJaCAwvOxw4V7TCbo7C21ZB-rCazqVFsNZteQuM504pFmkEikpZdx6uHkCdvzsATuLK0u7Z0_K6Lla_WHQ5G_nkPzP_UnNvzMaDpWxPKU_rLL1itfOt__f9fk5t9JZgYVCwsTxjsc5QIV3NfQ6vqcAtE3JYOyMw49l07PmERh22h3sfDva2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
پست اینستاگرام نوید محمدزاده با لباسی با طرح پرچم فلسطین
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/681829" target="_blank">📅 00:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681828">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ادارات مهران و دهلران دوشنبه تعطیل شدند
🔹
با توجه به تداوم موج گرما و افزایش دمای هوا، فعالیت ادارات و دستگاه‌های اجرایی، بانک‌ها به‌جز شعب کشیک و شرکت‌های بیمه در شهرستان‌های مهران و دهلران روز دوشنبه ۲۶ مردادماه تعطیل اعلام شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/681828" target="_blank">📅 00:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681827">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89ae3291b3.mp4?token=AA5nppeA3WFQAaX_q6A3KlxJ6bOASbjJI0n9mrzjkohlmmoWClpSzVTI07xMZABsSkZr94RRwhwLvDaewI5ndA-l4WQBUoHdYD0zwEjMZkJePlT8ou3hejEFCVi2JvFz2MuL6ldIPzTe66VNXWzeU3wTYXHFxeGKeQr01bZWlRbApqQnwfHxrl0OIDuktoltQg-f6V5q2u-7U7cherb40X4UYGNTYfGj9l0CnbdNkitida1xx7JSPl9N1QGrQEYpKF-eMndrmttQDfRi0QEWQcZfEl20Yjrx4lixWsCX1VMRDySQSSze7ZDWl-bOXFA12oMcPTjrYpSZw7SIykp3Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89ae3291b3.mp4?token=AA5nppeA3WFQAaX_q6A3KlxJ6bOASbjJI0n9mrzjkohlmmoWClpSzVTI07xMZABsSkZr94RRwhwLvDaewI5ndA-l4WQBUoHdYD0zwEjMZkJePlT8ou3hejEFCVi2JvFz2MuL6ldIPzTe66VNXWzeU3wTYXHFxeGKeQr01bZWlRbApqQnwfHxrl0OIDuktoltQg-f6V5q2u-7U7cherb40X4UYGNTYfGj9l0CnbdNkitida1xx7JSPl9N1QGrQEYpKF-eMndrmttQDfRi0QEWQcZfEl20Yjrx4lixWsCX1VMRDySQSSze7ZDWl-bOXFA12oMcPTjrYpSZw7SIykp3Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش اردوغان به جنگ احتمالی ترکیه با اسرائیل
رئیس جمهور ترکیه:
🔹
ما در مورد جنگ صحبت نمی‌کنیم، ما در مورد صلح صحبت می‌کنیم.
🔹
اما اگر کسی قصد حمله به ترکیه را داشته باشد، ترکیه در آن جنگ تردید نخواهد کرد و از آن فرار نخواهد کرد.
🔹
من این را با وضوح و صراحت کامل می‌گویم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/681827" target="_blank">📅 00:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681826">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
زندگی بدون سقف/ روایتی از زنان بی‌خانمان
🔹
زیرپوست شهر  زنانی زندگی می کنند که تنها سقفشان، آسمانِ شب است. این مستند، روایتی بی پرده از زنانی است که نه از روی انتخاب بلکه از جبرِ حوادث، خانه و امنیت خود را از دست داده‌اند و حالا در حاشیه  شهر، در نبرد با سرما و گرما و تنهایی به سر می‌برند. شاید تماشای این ویدیو، پنجره‌ای باشد به دنیایی که این روزها کمتر دیده می‌شود./ خبرفوری
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/681826" target="_blank">📅 00:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681825">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24a31969da.mp4?token=E0aPyRbqrhb4-_bTg1e_6F-Cg0cLJsGQo6hcsXP0XWZn5oP7pxbd1ajAKk73z13PhhW1WSTy27rGggHRx7tamWXD0vL8PjH13wFSS0ViNmHXaCQcY7unQWss4P9yp8tff9Ptfj9E_Fx22SBz3K_VIsNhUfqXELcAKZn_j8jnNq2WU9W_hhsTKNa_00lYzGXaUP3RCLS-BO6MI_UbQljCuRHMV9yMvFwoPge3tyLuEHstYetrsdk2Kqnwe2A3QLRzVyvg20GaXvT2-7yX-D9FxDcr5xGvOaf7F4l7iaaf-8wG4mU7yqsLayqshhkIwDmuZ1K-9dpEcbxpAE1ogp_hqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24a31969da.mp4?token=E0aPyRbqrhb4-_bTg1e_6F-Cg0cLJsGQo6hcsXP0XWZn5oP7pxbd1ajAKk73z13PhhW1WSTy27rGggHRx7tamWXD0vL8PjH13wFSS0ViNmHXaCQcY7unQWss4P9yp8tff9Ptfj9E_Fx22SBz3K_VIsNhUfqXELcAKZn_j8jnNq2WU9W_hhsTKNa_00lYzGXaUP3RCLS-BO6MI_UbQljCuRHMV9yMvFwoPge3tyLuEHstYetrsdk2Kqnwe2A3QLRzVyvg20GaXvT2-7yX-D9FxDcr5xGvOaf7F4l7iaaf-8wG4mU7yqsLayqshhkIwDmuZ1K-9dpEcbxpAE1ogp_hqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راحت ترین و سریع ترین راه برای درست کردن دسر با قهوه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/681825" target="_blank">📅 00:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681824">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای هیل: گزینه دیگر تسلیحات هسته‌ای ایران بمب‌های پلوتونیومی است
پایگاه خبری هیل مدعی شد:
🔹
ایران بیش از ۱۵ سال است که رآکتور بوشهر را اداره می‌کند. مانند همه رآکتورها، پلوتونیوم به عنوان محصول جانبی عملیات عادی، درون سوخت مصرف‌شده رآکتور به دام افتاده و انباشته شده است.
🔹
این پلوتونیوم هرگز قرار نبود در ایران باشد.  بیش از ۲۰ سال پیش، روس‌ها که رآکتور بوشهر را ساختند و سوخت آن را تأمین کردند قول دادند که سوخت مصرف‌شده را پس از خنک‌شدن و ایمن‌شدن برای حمل‌ونقل، خارج کنند. اما ایرانی‌ها این پیشنهاد را رد کردند.
🔹
اکنون، حدود ۲۱۰ تن سوخت مصرف‌شده حاوی بیش از ۲ تن پلوتونیوم در یک استخر نگهداری می‌شود. این مقدار برای ساخت بیش از ۲۰۰ سلاح نسل اول کافی است.
🔹
این پلوتونیوم یک مشکل بسیار پیچیده ایجاد می‌کند. نمی‌توان آن را بمباران کرد، زیرا این کار می‌تواند باران رادیواکتیوی با عواقبی در مقیاس قاره‌ای ایجاد کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/681824" target="_blank">📅 00:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681823">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5DfIkl2wVTB0qyHNK5nK9r9F-Y9pcgQb5Kom5LYjAABCrQGJC_aFp0souN0EVlgzh3VwfHRdBj68mGjh7-c4viDU8A3C_jPWpeBVNVwo6gfp6aDrzFfV76qar9VDhZO3UNpaa1V6p3qjgVUglZ5KsmxeR5xgvQYdfh3ipVeZN3l_FwAy-5h-ypGXhZD3gdB3boPvNDA6vxtdTipohNguiXaFADsZh_yUZRY97rjlhv4gyicGSCqoStQyd6SYUcta6tAoyNJJTLiHe0sCEZI1TYR-heyxLJ4d5_G6iAy31XaBDPSc2K5b5oXLKI35BmnQp5ttLQm3DYxMXJVZNfbNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسکات بسنت وزیر خزانه داری آمریکا از تحریم های آتی علیه ایران با هدف افزایش انزوای اقتصادی خبر داد
🔹
این اقدامات در کنار ادامه محاصره دریایی ایالات متحده در تنگه هرمز عمل خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/681823" target="_blank">📅 00:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681820">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q07vmieI57J91-4xDGASCElFQQ-5cR-KWdtxFr_BFmE1KkKED5-qjaL6i3blP_MgKLB87QE3or6Oex-BT49DAg9TyqL2Pw9yge-jOiN7Dsf2aPdJeaEfIls3qBseR1kRYpZZgUQ45yg2wGaSEOFC6_LnEr7NUWk-Vrt_aZY-gxAYQe-XFcThh2sf1VhLocOG1jEy4wrwbvdsZuJyX8Q79ai-ECvmYnHbKlZHmIW33VoEE9x4b3Vxjm5sTvKSoPiQ_gaSDeYEGZuzu4exeTrsyouFcU8raHP8VEWHjKyRfGV_4CuXm6jAy7G1LTJV4VyM81UD_uJ_PQUOvlRm1whnxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/akhbarefori/681820" target="_blank">📅 00:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681819">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
قالیباف: باید به نقطه‌ای برسیم که از چرخۀ تکرار جنگ و صلح خارج شویم
🔹
باید مراقب باشیم دستگاه محاسباتی ما مسئولین به خطا نرود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/681819" target="_blank">📅 23:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681818">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
پیام صریح به بازار پول؛ خبری از تزریق نقدینگی نیست
🔹
عملیات بازار باز هفته گذشته نشان داد بانک مرکزی همچنان کمتر از ۲۰ درصد تقاضای نقدینگی بانک‌ها را پوشش می‌دهد.
🔹
با وجود ثبت سفارش‌هایی در محدوده ۳۵۰ همت، میزان پاسخگویی بانک مرکزی از ۷۰ به ۶۰ همت کاهش یافت.
🔹
با احتساب اوراق سررسید شده، بانک مرکزی در مجموع نه‌تنها پول جدیدی به اقتصاد تزریق نکرد، بلکه حدود ۱۰ هزار میلیارد تومان منابع بانک‌ها را به‌ صورت خالص جذب کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/681818" target="_blank">📅 23:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681817">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2201eaa6.mp4?token=uqMLO9wgWtymsDLz-1zBL5huzNdrlFYpBc-jC91q2xBfLXwArUw4O7SXt5LyhblTTeIz8ORahX1YwxzziVLnRkkj4JrQqoAJT5o-ls1QDaW4O8z0ZIJU7FyuMIrR_oP_t8TQ-IcpRxlzh0ZiQ4-c2CsCzFsHw2NM3Sn2HLVRI5BotU93UvnnmGDHvfaGqCC0x1iPOYqoFfb2qCT7kz3Zhe99-4tEcL7_JBbuo_4DVlhR3mHvc4O4RaCBKw3x3AOdWVPqCqW7AF0Dw7j0QOvNtGJaoFBbI5bsCUf_eYVgK7XhA98tjOIa22eFRYnMIO5QyOvEHQqlvkEg_LX9RjC5LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2201eaa6.mp4?token=uqMLO9wgWtymsDLz-1zBL5huzNdrlFYpBc-jC91q2xBfLXwArUw4O7SXt5LyhblTTeIz8ORahX1YwxzziVLnRkkj4JrQqoAJT5o-ls1QDaW4O8z0ZIJU7FyuMIrR_oP_t8TQ-IcpRxlzh0ZiQ4-c2CsCzFsHw2NM3Sn2HLVRI5BotU93UvnnmGDHvfaGqCC0x1iPOYqoFfb2qCT7kz3Zhe99-4tEcL7_JBbuo_4DVlhR3mHvc4O4RaCBKw3x3AOdWVPqCqW7AF0Dw7j0QOvNtGJaoFBbI5bsCUf_eYVgK7XhA98tjOIa22eFRYnMIO5QyOvEHQqlvkEg_LX9RjC5LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک روش کاربردی برای تمیز نگه داشتن لوله‌ سینک ظرفشویی، که با استفاده از یک بطری پلاستیکی انجام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/681817" target="_blank">📅 23:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681816">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fba1d673c.mp4?token=fTQ4utrf3JK_QR0rIGIPkn757oW7Dr_V5CtbabNz8ifuHUPdvNl1vkIBs9L5w7N3hk8A0500f33QpYHdEHNpMYSoLHCOUExlyMB49tZt7eKhqFhoTZC_oTOC2moWvIRdwQoQAMHJAe5V8uLo-a-fUCPt_pSbQICVrxbmD54QbtnveWQFR4PUGEgJuSGie-I63HGsjt9-WclcPjywzxNVWScFy5-4RitxFCfgcQvkO4jdaxlLa11LJsktihgTWa66Tv71u2NSKrY4G0XKEoYo7DF5RyraSR48rywyY3xYk38ParA0DVNI3uweYVcRORmmgFzvjkd7SYjCAsC9rZq4iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fba1d673c.mp4?token=fTQ4utrf3JK_QR0rIGIPkn757oW7Dr_V5CtbabNz8ifuHUPdvNl1vkIBs9L5w7N3hk8A0500f33QpYHdEHNpMYSoLHCOUExlyMB49tZt7eKhqFhoTZC_oTOC2moWvIRdwQoQAMHJAe5V8uLo-a-fUCPt_pSbQICVrxbmD54QbtnveWQFR4PUGEgJuSGie-I63HGsjt9-WclcPjywzxNVWScFy5-4RitxFCfgcQvkO4jdaxlLa11LJsktihgTWa66Tv71u2NSKrY4G0XKEoYo7DF5RyraSR48rywyY3xYk38ParA0DVNI3uweYVcRORmmgFzvjkd7SYjCAsC9rZq4iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگترین هواپیمای برقی جهان برای اولین بار به پرواز درآمد
🔹
شرکت سوئدی-آمریکایی Heart Aerospace با موفقیت هواپیمای نمایشی X۱، یک هواپیمای تمام برقی با طول بال ۳۲ متر و وزن برخاست بیش از ۱۱ تن را آزمایش کرد.
🔹
این پرواز در شهر نیویورک انجام شد، ۲۷ دقیقه طول کشید و به ارتفاع تقریبی ۳۳۵ متر رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/681816" target="_blank">📅 23:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681815">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
معاون سیاسی سپاه: راهی که ترامپ می‌خواهد را خدا برا او بسته است
🔹
وقتی ملت ایران حق جهاد در راه خدا را ادا کرده، خدا هم راه سلطۀ کفار بر ملت ایران را می‌بندد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/681815" target="_blank">📅 23:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681814">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
ثانیه‌شمار کانال ۱۴ اسرائیل برای لغو تفاهم‌نامه تهران و واشنگتن
👇
khabarfoori.com/fa/tiny/news-3238221
🔹
تصاویر خلبانان ایرانی که در اسارت قطر هستند
👇
khabarfoori.com/fa/tiny/news-3238159
🔹
ترامپ دلیل کناره‌گیری سخنگوی کاخ‌سفید را اعلام کرد
👇
khabarfoori.com/fa/tiny/news-3238218
🔹
ماجرای خیانت همسر مهستی به او/ دوست صمیمی اش زندگی او را نابود کرد
👇
khabarfoori.com/fa/tiny/news-3238192
🔹
خواننده زن ایرانی در ۷۶ سالگی درگذشت
👇
khabarfoori.com/fa/tiny/news-3238031
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/681814" target="_blank">📅 23:42 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681813">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhQiwfVUbujw5gEtzY5SmxnAbzC9skJFvK_mWAjdkhUsQ6vc_ctVS0p3VZDL4Ffwu2bUwzogt2ZnYiRYQyyxL8vmuszQLRr_3JcufI3tnRbAnz_PWcbzU_4sHCjs43Dj1naE-k_nvxc3TIbIun9EXy6mFRI3nfAO5vGSF8wWhwfhUTr3NlMCJ1fZmP2wNRN-DfrCbHUU7nHJDB9Dfc5ic-3DBI0usBTumX_YVv19G5lGdzky9_DMFunub_pxu-0uyr_tKT8ODEZ6gh-37Jujet46Rqdks8Zy575cYTjvRUfUrQuR87ZAt9awX_EOpUY5r-pToTWO0D6ariwdFMvI5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن‌پست: متحدان عرب در جنگ ایران از آمریکا ناامید شدند
واشنگتن‌پست:
🔹
متحدان آمریکا به‌ شدت نگرانند که ترامپ نتواند دیپلماسی مورد نیاز برای تأمین صلح با ایران را مدیریت کند.
🔹
یکی از این مقامات بلندپایه عربی گفت خشم کشورهای خلیج فارس به بالاترین سطح از زمان آغاز حملات آمریکا و اسرائیل به ایران در فوریه رسیده است. ترامپ این جنگ را شروع کرد و ما بهای آن را می‌پردازیم./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/681813" target="_blank">📅 23:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681808">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qtqOk0yf_3yxhNT1VkiPFQj3kFDNSSsmsay4Co-HNsLH946kocmHh5x85ae_kGEfo8F5XHVuYpZfZUh8eMieWCWmUyr6xS0GZatTq30YCeD3fAB4RrfNyDEK8VJkE5QADGWMB33U3RtfiPvFIHbabO6rerB6PPGNMvmTpJZjSjX1Mvepfgb5vKS3WcE-y8ifurs3gpdnQVkrUxua4yxuo2XwQ-EOKHnOzs24sDruHh9Zs0iWuGq8SM1keyNWgF4Bpia2lyfF-6b7zQu-jjmjTYRfdp5pryb02hMIz3OUSxZZKf1unm-EOpPgKP8OYgLWTTzhN9fvjBOqfY6CtLCrdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pPaDjZ8mR8b1jSYupnW7mnSkUpB0Pgeos27lAc_dvrXTnOAAC9BC__Zc3iK3N__ZR_BpaVhyCEaWKryVhAAgAbopAmy0fQN-n2a47MPaceEkUoq5Tcst_lP-VZz4lLPA7HTNpf0gir31gQ4W5SDarJYZR-sa183MH1d2yFL4EvLASBQSuvgNsiLUmRTvATMvEzpdu7lOhXJALX406XRB8nDDZIaznlCEnbpSLkvW9-gVwzCjVRBc7giKkLligiX7rwcc2QlVxXTUxQgHlcgm_8RYzShazyuP2mZHL8V-oA4mSjzffEAUZLEtBoqOuj2YKW1pPUbn2KD_LWSg70Sdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfo47jPGcqTvkvA1uRnCnBEnQAOfPwn1lyfOXBL6Adr1Z97BsyNMUg_fbY5Hrw8olHno6kfNKsKIgeFebGO5QKPHum-O8buZgv0uf1p-tZhg_UrX2_JvtP0ehS3kpkk00w4WI79h3tRqPREx1ybkYuDF0NrcSqOfU_xwSCuvqfbWygY7tY1fdK_EuZBTeHFMzdK8bkzs1cdRdZ02LxHxvTMm3MKvOmt6jUuREyrp4N764-DTAq1kUFK2zchkzI4I91ao28xnMTaeDyt5P65s7JC9qgDpdTLjRA_4YnVu8AvU9Z2FUhaesbq7EtIABfWb1oJLvpZZKTmuFJKMXmvYmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UrQVOZogatYlQym5-Sc8KtFOi5asA-E6fFdOEcu7m8mr7ZLKBgbT3HCp0r4t9FlRlSe2pqkYrWSUOCy7O9tyq3s92jmmzoTZ-wL0f5jW-bra3smhm1sMlU2dY7DA1UOLdvkkJtwnu7iX0Wym5kmLy-TQHu5n_ruWzFantRH-Vnl-8KSoCNdO04VDZOJDpGt_teUZPSy2l2YYddMSDQ1AgqB8MV_HgPrRdM2wEUPLlq6CtxFGx_e9O-wcb8n9IxPG6vhBsitO5Dq2tUs9nCHkxxy5v1QnrSNgVB7flUnAcJYYvHAAgpZdKpW1e_iRjQS4DtXaoSG0Y52toNI02nB6sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYpkR_nhMeNxyDq5BAlRetF758M2X4G50qvrhsAQakx-5GG0SdZnA1MBiVUOGYArqh2p8ovKh4kJxtN7J0XlqPjYAddHUsCffHS4TPT2B4BZLMwVTgrZXmmLv0Lj13vIWIGIuVKmOlG2EEQQFOAS2Ya7S8MfkywFSzUJVIF6KEkoY1O82v_BLYvX-Avs8ZEGDIjDIEq-ntJSSnNKG6WLsmIDhEIEbC1k7KR-1V3Z7i219U4pycQZg7MyZDiEvwdOKhqGDZJFauEVPqOM3srHSSdHojgtlnvBQh2I8pjkHRA3c2sddCbDdnR5lc_XTZrQ9TOIrIoTJoh7Hk2Imps2-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عددهایی که ترامپ را می‌ترساند
🔹
جنگ ایران فقط میدان نبرد را تغییر نداده؛ قیمت نفت و بنزین را بالا برده و حمایت آمریکایی‌ها از ترامپ را هم به سرعت کاهش داده است.
🔹
اعدادی که در این اسلایدها می‌بینید برای ترامپ خطرناک است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/681808" target="_blank">📅 23:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681807">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b0e2e6f0.mp4?token=C5VfAmXGngFiTTx34bQMopEnexowGzMWj4g8N9RjqAO36_PDj5mC0pg3BOb85KOHWZlr4kA3vSir96BgoCDeZXzHz1ujMwGlB2Ex9FRlBo6_uiK5qUsFR79FkOhjk1Lmkp5JcUv9qATSKA1qJGvpliyKUcEUGvnCp5JyA52Voz_aw9AEkBSGs1E1ISvphy7Jndy5PxjL8rgDeoaNtdCB7Np-2ynZ0hG7_Xoz51aOuHzLpMEMRIyUc2fhou70M7u4XdOcfuC6SspTimhikvHSVVYDg0bTWKnqidcbQVHP-xwiEjajG9xKPGpqfzeN3VDm-pGGbN1thER5eNdYkEpX1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b0e2e6f0.mp4?token=C5VfAmXGngFiTTx34bQMopEnexowGzMWj4g8N9RjqAO36_PDj5mC0pg3BOb85KOHWZlr4kA3vSir96BgoCDeZXzHz1ujMwGlB2Ex9FRlBo6_uiK5qUsFR79FkOhjk1Lmkp5JcUv9qATSKA1qJGvpliyKUcEUGvnCp5JyA52Voz_aw9AEkBSGs1E1ISvphy7Jndy5PxjL8rgDeoaNtdCB7Np-2ynZ0hG7_Xoz51aOuHzLpMEMRIyUc2fhou70M7u4XdOcfuC6SspTimhikvHSVVYDg0bTWKnqidcbQVHP-xwiEjajG9xKPGpqfzeN3VDm-pGGbN1thER5eNdYkEpX1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت حضور یک شهروند ناشنوا در تجمعات شبانه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/681807" target="_blank">📅 23:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681806">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4940f4d822.mp4?token=dW6rv9gNuMm2rc4LbvxSSdxqu-Ed5F02qLBa1lMDMZU6KoSmeM3huiAfFnz1BnIeQq2p3FbzX6l_p0-fxT_ho7uId6XMiytmBi4vBLQcP20NEB3qwE7C5Efya1OxdWyS9D11n8vg2x7bbD9BDT54qecpc4hQ_8yqYr5ARNNdohNotaWs6vf7ZWXJ0-Bu4EPdaTjlmTAbB2Tity70Puhqxujuv9vhS20LjDR5Ta4QKg8YaHtKGXoXMOE8Snh-W4apLJ0fE4Kt5u7xaaUSsNcxEHny274Uo72E1eXjnCxBNxkkghbQMI7-9azbnwxivgDUWA0a5KcG7cgh7DBhUdkQyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4940f4d822.mp4?token=dW6rv9gNuMm2rc4LbvxSSdxqu-Ed5F02qLBa1lMDMZU6KoSmeM3huiAfFnz1BnIeQq2p3FbzX6l_p0-fxT_ho7uId6XMiytmBi4vBLQcP20NEB3qwE7C5Efya1OxdWyS9D11n8vg2x7bbD9BDT54qecpc4hQ_8yqYr5ARNNdohNotaWs6vf7ZWXJ0-Bu4EPdaTjlmTAbB2Tity70Puhqxujuv9vhS20LjDR5Ta4QKg8YaHtKGXoXMOE8Snh-W4apLJ0fE4Kt5u7xaaUSsNcxEHny274Uo72E1eXjnCxBNxkkghbQMI7-9azbnwxivgDUWA0a5KcG7cgh7DBhUdkQyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هند نخستین پهپاد تهاجمی بومی خود را با موفقیت آزمایش کرد
🔹
منابع خبری گزارش دادند که شرکت فناوری پهپاد هندی «کاوا یوایوی» اولین پهپاد تهاجمی خود به نام «دیویاسترا ام‌کی۳» را با موفقیت آزمایش کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/681806" target="_blank">📅 23:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681805">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Czej9R50dbOJXJ_mobRVXyuxpDQpX2Mx85T8Yff4NKNShmXhCFLTHs-FNNfeeumJdZVB0lKlNVEk8pVzzGJcm5cy1dQgjXukgQsqXNI7teRGKSTI1QnMZyjhpKT9vDFNht_8oT04WC085zcsaUMuEh1L7PBI49e9YD4_ciZeI03CcNnClg71E0Il7v3IeH2rTMS9EXZR4w0_uFaEvX4U7tzkWcRL6H_nX7JjzxTS7KDpyHnyQqySbgTnfLKQ5OVffsfFB8vCgu_vAQqFigxsIw1X3GJNEX8LXNH-9Vvg7oVSb3qKm7zMb3wLWYoza4Wlwbb6Zonz60FyKR5CqaBVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راشاتودی: صبر متحدان عرب واشنگتن در برابر راهبرد ترامپ لبریز شده است
🔹
عربستان سعودی، امارات، قطر، کویت و بحرین نسبت به راهبرد دونالد ترامپ در قبال ایران که «غیرقابل‌پیش‌بینی» ارزیابی می‌شود، نگران هستند.
🔹
پس از ماه‌ها درگیری و حملات، برخی از این کشورها حتی بازنگری در حضور نظامی آمریکا در خاک خود و جستجو برای یافتن اتحادهای امنیتی جدید را آغاز کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/681805" target="_blank">📅 23:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681804">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
امروز مردم ۳ هزار میلیاردتومان پول به بورس تزریق کردند
🔹
در جریان معاملات امروز، حقیقی‌ها بیش از ۳ هزار میلیارد تومان پول تازه به بازار سهام تزریق کردند و ارزش معاملات خرد به حدود ۳۹ همت رسید.
🔹
هم‌زمان، صندوق‌های درآمد ثابت با تراز نقدینگی منفی ۱.۸ همتی مواجه شدند و صندوق‌های طلا نیز ۲۳۴ میلیارد تومان ورود پول ثبت کردند؛ نشانه‌ای از افزایش تقاضا برای دارایی‌های ریسکی و طلا. /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/681804" target="_blank">📅 23:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681803">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ae83786da.mp4?token=v1CJN6cUrY4Wab5_ZZJnYyNT9jfhrUOkMeX8PbrN5gt5rrMICaM3vQ963Oy-7hUOS0BdPcUQsgk8jfKKPH7VPposGst-R_K9HLeWBbG_cuDrd6ZG29w3zesyQG_FxCO8IC61sYhYE2j0-uefTGYbvmM7RuzK5nZCXB0WcZfu7NISltes6VVSvCEc58R6JnivommjgjSffgQGwvzIeXnFE34sBXEh0sFWfHQMIaHeS1z4ZHeZbz3ZP5eif_Wa0Gd2gow5ifwf2Gpso3GXUn_-a4vATXy2pz0i3YY_Sa8bjDLJxWK6jPbICizMq_GZIMfHKIQQkPxqpHVaG7UyB-mp0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ae83786da.mp4?token=v1CJN6cUrY4Wab5_ZZJnYyNT9jfhrUOkMeX8PbrN5gt5rrMICaM3vQ963Oy-7hUOS0BdPcUQsgk8jfKKPH7VPposGst-R_K9HLeWBbG_cuDrd6ZG29w3zesyQG_FxCO8IC61sYhYE2j0-uefTGYbvmM7RuzK5nZCXB0WcZfu7NISltes6VVSvCEc58R6JnivommjgjSffgQGwvzIeXnFE34sBXEh0sFWfHQMIaHeS1z4ZHeZbz3ZP5eif_Wa0Gd2gow5ifwf2Gpso3GXUn_-a4vATXy2pz0i3YY_Sa8bjDLJxWK6jPbICizMq_GZIMfHKIQQkPxqpHVaG7UyB-mp0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار جوانی: دشمن بداند که نمی‌تواند اقدامات غافلگیر کننده‌ای را علیه ما انجام بدهد، او باید منتظر غافلگیری‌های راهبردی باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/681803" target="_blank">📅 23:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681802">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
سردار جوانی، معاون سیاسی سپاه: انتصابات انجام شده نوعی بازآرایی و کارآمدکردن دکترین دفاعی انقلاب اسلامی به اقتضای شرایط است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/681802" target="_blank">📅 23:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681801">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edeccab51d.mp4?token=RqeqNp1Mw7bvUZ3mDvZwkoiFSjSTOPNc89dIvCV38XJrPrtenS_6ftbyh8KtKFUoMmGBcO9HMWosqFe7MJxmpOXuXCjhoxzKA2bmP2tgS6T3QdItFGRcRNIj2HG1MyNxwOlKR2kWhkvnKoMnxE5RxNLtHbp2_bQPx6EfSAnYracL4weNrVu9d4G7LEHvdog-Xlyr5Eig0ZjHPn9p_KN24n7Uj-A3O5UNJmXq6OW-wkTb6kMHVnOD2rpBYzLbNclcTmuGqhy0hvYBNM_4jzD6f8fFuUHRkM4j8RgS4VK3vYrX0uYHn9WR6F2DK82z4pOxL2MEXlT6B3ykgXUmuI59Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edeccab51d.mp4?token=RqeqNp1Mw7bvUZ3mDvZwkoiFSjSTOPNc89dIvCV38XJrPrtenS_6ftbyh8KtKFUoMmGBcO9HMWosqFe7MJxmpOXuXCjhoxzKA2bmP2tgS6T3QdItFGRcRNIj2HG1MyNxwOlKR2kWhkvnKoMnxE5RxNLtHbp2_bQPx6EfSAnYracL4weNrVu9d4G7LEHvdog-Xlyr5Eig0ZjHPn9p_KN24n7Uj-A3O5UNJmXq6OW-wkTb6kMHVnOD2rpBYzLbNclcTmuGqhy0hvYBNM_4jzD6f8fFuUHRkM4j8RgS4VK3vYrX0uYHn9WR6F2DK82z4pOxL2MEXlT6B3ykgXUmuI59Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جوانی که با دست‌سازه‌هایش یاد شهدای کودک و نوجوان جنگ را زنده نگه‌ می‌دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/681801" target="_blank">📅 23:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681800">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
معاون سیاسی سپاه پاسداران انقلاب اسلامی: از سه منظر می‌توان به احکام صادره از جانب رهبر معظم انقلاب نگاه کرد
🔹
اول از منظر فضا و شرایط
🔹
دوم از منظر پیشینه و سوابق افراد
🔹
سوم از منظر مطالبات رهبر معظم انقلاب از افراد منصوب شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/681800" target="_blank">📅 23:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681799">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee142e9f9.mp4?token=kM-gmF-iZ6kK8THI2VcqfjwXqp-J0-G3vqCs5_7Gy33YVwN7Q6u-fyql5w29gtk8SwDR2pENsPb3rwGUDDlWh9Erg6cIfMf-tatas4UCehxp3NswTzCMhDPiLk6pHvw8SnLyFU-1bA3ksZArWnbMwvW5zFHj62RU7xBX3dIj6HJJWrJZHiY_ntkpFhKuLnNdNT67luV4f7r-v-NKshai76OpK9xLFjTsWA9oynqsO-DvQSgcbMjSFl73IPU0notTz246FjSfW5tX9vGewioExwVm102hJUw_-2fUnd6RwkHUkaxcr0Yu1SJeAYkhGiPOOy_hBm1OYGV4szRly71DLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee142e9f9.mp4?token=kM-gmF-iZ6kK8THI2VcqfjwXqp-J0-G3vqCs5_7Gy33YVwN7Q6u-fyql5w29gtk8SwDR2pENsPb3rwGUDDlWh9Erg6cIfMf-tatas4UCehxp3NswTzCMhDPiLk6pHvw8SnLyFU-1bA3ksZArWnbMwvW5zFHj62RU7xBX3dIj6HJJWrJZHiY_ntkpFhKuLnNdNT67luV4f7r-v-NKshai76OpK9xLFjTsWA9oynqsO-DvQSgcbMjSFl73IPU0notTz246FjSfW5tX9vGewioExwVm102hJUw_-2fUnd6RwkHUkaxcr0Yu1SJeAYkhGiPOOy_hBm1OYGV4szRly71DLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: ما در بُعد نظامی و سیاسی جنگ پیروز شدیم  رئیس مجلس:
🔹
ملت ما در یک جنگ ناجوانمردانه، مقابل دشمن آمریکایی و صهیونیستی شجاعانه ایستاد.
🔹
به‌عنوان یک خدمتگزار که به جزئیات آشنا هستم، با همه وجود می‌گویم ما در این جنگ، در بُعد نظامی و بُعد سیاسی، به معنای…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/681799" target="_blank">📅 23:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681797">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
معاون سیاسی سپاه: اقدامات ما تاکنون تدافعی بوده؛ ممکن است تهاجمی هم بشود  سردار جوانی:
🔹
نیروهای مسلح براساس احکام صادرشده، رویکردهای تحولی خواهند داشت و هر اقدامی برای دفاع از کشور، تأمین امنیت و خنثی‌سازی تهدیدات دشمن در زمان لازم انجام خواهد شد.
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/681797" target="_blank">📅 23:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681796">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
خیابان‌های اسرائیل در سایه انتخابات
🔹
بنر تبلیغاتی حزب لیکود، حزب سیاسی نتانیاهو، با تصویری از رهبر معظم انقلاب اسلامی، زهران ممدانی، رجب طیب اردوغان و شیخ نعیم قاسم و این نوشته در خیابان‌های اسرائیل مورد توجه کاربران قرار گرفته است: «آن‌ها می‌خواهند نتانیاهو…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/681796" target="_blank">📅 23:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681795">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
پزشکیان: این‌که برخی از بیرون گود صحبت کنند و خیال کنند حل مشکلات کار راحتی است درست نیست
🔹
ما حزبی و جناحی عمل نمی‌کنیم؛ هرکس می‌تواند مشکلی را حل کند وارد شود و قسمتی را دست بگیرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/681795" target="_blank">📅 23:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681793">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
پزشکیان: در نهاد ریاست‌جمهوری ۸۰ درصد در مصرف آب، برق و گاز صرفه‌جویی کردیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/681793" target="_blank">📅 22:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681792">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSnQ_tzOHNjl3E5PQNcVAANVaNAYaBe_VjvA1nRXOdyiHUki3fWPNrf2To7FRiJvnyuBgnnhkm5gUJdIEd-w4mg6VDDxlNomkKrTbN6STmlnvzIKQf9w_wV2XC4bvQaUPNiVrW9yNPTEwbLbatuvskmQfXtdLAiXPchM7-1rLQKq6z1Gx-LVTzez6LpaY2rNyQpgqnpyHjC5yaAe6KS5vZ70ItOm73_5BRHyg9JLxD7tD-1pAO8B5hH-TSL7qM3gIiaRd5-W5mgtOFPqGdR-zscWLLY5NZXDhDmnwtSEBUtkXwUH4w9yTUyW0PngkK1LvR0VYLqy94cb3Z3RXW9vxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«هم‌پی» راهکار پیشتازانه بانک اقتصادنوین برای آنکه چرخ تولید متوقف نشود!
🔹
بانک اقتصاد نوین همزمان با بیست‌وپنجمین سال فعالیت خود، طرح «هم‌پی» را برای پاسخ به مهم‌ترین نیازهای مالی تولیدکنندگان و فعالان اقتصادی ارائه کرده است؛ از تأمین حقوق و مواد اولیه تا فروش اعتباری و تأمین تجهیزات نیروگاه‌های خورشیدی
🔹
«هم‌پی» تلاشی است برای عبور از چالش نقدینگی و کمک به تداوم فعالیت و رشد کسب‌وکارها.
برای اطلاعات بیشتر:
https://enbank.ir/s/mfa9aC
☎️
02162740</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/681792" target="_blank">📅 22:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681791">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d651a948d.mp4?token=OZJ-KVc5aYDsIUpjmioqehc60gJqXsNbHLHxcRgrJ-glthbD2dGvNIfGNzP5ZKHpp3ret_fl61ByYqo-o2wIqwr8eYnLNnNti0gsOeB2lTFyuNvMSDjmyUn6OptnlNUWcaiML2KdSFYCxVXlzS4c4DexxC4ZLH5L73bpbmNFWa278n277adB7ShXnvfzpjEB9zZnwGEb8T4kRd6lDZLOV6JKpk3eYH1ilUHDSn9twsN0sItECW1Xvt1CN5E64Ghs2wbaVlU8TpSDzXzugmBeOXKDmET2f54n2UdO_0gyW626xoKS1ShTmlY4jAnuBR4wsRwifInVDe6AG0sEoHfltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d651a948d.mp4?token=OZJ-KVc5aYDsIUpjmioqehc60gJqXsNbHLHxcRgrJ-glthbD2dGvNIfGNzP5ZKHpp3ret_fl61ByYqo-o2wIqwr8eYnLNnNti0gsOeB2lTFyuNvMSDjmyUn6OptnlNUWcaiML2KdSFYCxVXlzS4c4DexxC4ZLH5L73bpbmNFWa278n277adB7ShXnvfzpjEB9zZnwGEb8T4kRd6lDZLOV6JKpk3eYH1ilUHDSn9twsN0sItECW1Xvt1CN5E64Ghs2wbaVlU8TpSDzXzugmBeOXKDmET2f54n2UdO_0gyW626xoKS1ShTmlY4jAnuBR4wsRwifInVDe6AG0sEoHfltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون سیاسی سپاه: اقدامات ما تاکنون تدافعی بوده؛ ممکن است تهاجمی هم بشود
سردار جوانی:
🔹
نیروهای مسلح براساس احکام صادرشده، رویکردهای تحولی خواهند داشت و هر اقدامی برای دفاع از کشور، تأمین امنیت و خنثی‌سازی تهدیدات دشمن در زمان لازم انجام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/681791" target="_blank">📅 22:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681790">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
موافقت مشروط حماس با نقشه راه مرحله دوم طرح صلح در غزه
🔹
هیئت حماس به ریاست خلیل الحیه در دیداری با میانجی‌گران و ضامنان توافق آتش‌بس در غزه که با میزبانی مصر برگزار شد، بر مواضع خود برای دستیابی به صلح پایدار تأکید کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/681790" target="_blank">📅 22:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681789">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56fae229f2.mp4?token=sZcAAd0gStZqrI4kH9EhEfqn2a2mjWKrCoo5rGZI91VyuYBgi4rjlqHSMnWcZ6OP1n63JDNwPvCMMLUV3qh7DPjLf4PYeEmLjXz4Q7AKzwR2F2Y1hVrvMTxSeqhOzNUs-M_TZbt-N8RTkVV7EuAlKO4MK3zgyKkbL4Pgkp0eVsfmKE7Tr7RGrzKV-o5NJeDrtnLX16RwBAexIeXnHZrcnqu0hqN5qzWgNGxjbzJ3HJ9P5WpSW-3655BgQgNZkIkMr5f-Hg0voLNlfPS14mkC4kRUMeId9IPan_eKDQU955CPagOwTsJnR0m5bKznFNtHDtE7XRQtsa0cT5zrSlMQjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56fae229f2.mp4?token=sZcAAd0gStZqrI4kH9EhEfqn2a2mjWKrCoo5rGZI91VyuYBgi4rjlqHSMnWcZ6OP1n63JDNwPvCMMLUV3qh7DPjLf4PYeEmLjXz4Q7AKzwR2F2Y1hVrvMTxSeqhOzNUs-M_TZbt-N8RTkVV7EuAlKO4MK3zgyKkbL4Pgkp0eVsfmKE7Tr7RGrzKV-o5NJeDrtnLX16RwBAexIeXnHZrcnqu0hqN5qzWgNGxjbzJ3HJ9P5WpSW-3655BgQgNZkIkMr5f-Hg0voLNlfPS14mkC4kRUMeId9IPan_eKDQU955CPagOwTsJnR0m5bKznFNtHDtE7XRQtsa0cT5zrSlMQjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: ما در بُعد نظامی و سیاسی جنگ پیروز شدیم
رئیس مجلس:
🔹
ملت ما در یک جنگ ناجوانمردانه، مقابل دشمن آمریکایی و صهیونیستی شجاعانه ایستاد.
🔹
به‌عنوان یک خدمتگزار که به جزئیات آشنا هستم، با همه وجود می‌گویم ما در این جنگ، در بُعد نظامی و بُعد سیاسی، به معنای واقعی کلمه پیروز شدیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/681789" target="_blank">📅 22:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681788">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ادعای وال‌استریت‌ژورنال: یک شرکت چینی، تامین مالی تهران را بر عهده دارد
وال‌استریت‌ژورنال:
🔹
شرکت هنگلی توسط امریکا متهم به وارد کردن عمده نفت خام ایران شده است؛ این شرکت پتروشیمی چینی، تجارت با ایران را انکار می‌کند. این پالایشگاه بزرگ چینی، تامین مالی تهران را بر عهده دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/681788" target="_blank">📅 22:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681787">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBab2CkvoIwSJZ__tkPgbvg6fOunF8v_Or_pTQDwUHAvhI-ofMat6Nm6ZNRGE61cSKeKDzpELAz4FQjte6BlMwKKIcnNjpZ8jnnrsUmlpsi74L02dPm2AF-B-DKzTx0VpLXlMn9gnXSm2zUGvAyTPuoowwJRd0VGwFndH30KbIJBjM4UG3tHpCbkdAAEMMONBQY0cn095ggeRZON55lNth1_kXgpOx_NVxfYrIWjZI2lGITnhCKrvewvq06yRaDqx2zg_Aey6L7hp0_GLuWE86nXoxAgVSDUhthFUomB5bY42eM-rHQ98be4zeK9wzl3aPy8pL94rh_g72aOpCETFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر سی‌ان‌ان: ترامپ می‌تواند تنها رئیس‌جمهور ایالات متحده باشد که جنگی را به تنهایی آغاز کند و آن را ببازد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/681787" target="_blank">📅 22:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681786">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90cedd77f.mp4?token=G4gsqAtZ2KmjwaPT5h8VBPAJolDqEXoXZn8Uy-FTH7umDwRApLPGDiZ54Yk6oPGVKkXl2WvhAUHWEHC2mKcL3ezTXlbkmxR_Qa-TZtJ-VLSDPKueZ15DNhIqoiSKQ7Xy3AvTZiyPzqdmLZC0zTKgnc-YyhwHn58QhR-nCd8LoslG8maCVFftmYmErXq8GY-1aMrbOXn84tzRIygQNydcqXWFsJw4Kn9X92KHr_YOg75LBGRwTHJwvlTJIl9YRRS9qT_3E7N3O7OQefV3UalSgoABfYd_cBISGx8rx6FPVgQUsy_6DhgHm5-Qf_4mNKy1U396i39R_ZTk8w4oITJgjJvLTJHGsXKE8qyZJsU4rv4ftij4Rwab9iseG3uEI_lLiwyFJOrlY1mRruhqMZhXq6jZ0eY2zHw4yI9rgaiQX7vo6HML9gpCPb3a1nT-7GmRkbvPisqOl6tI4ziOEENSfMlPFVKYK5KK27cFX8oxr7_1MCr0Og2_gXA6ayzAxHHonEIJexISmQorufwMxtA35GQVQbwGU9jvJynOS6zTF6THRJrolyZ_DIfd1S07NcIVck3Rfif3XgDt9Zi1UzhNP2rQtBkxNw1XlPw2uiLl8DLX23CPLeKTfqsBebvjMy022U_loaNIzOTBZNsQG4A_EbMxDnLFzAHNAD6jiSiawAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90cedd77f.mp4?token=G4gsqAtZ2KmjwaPT5h8VBPAJolDqEXoXZn8Uy-FTH7umDwRApLPGDiZ54Yk6oPGVKkXl2WvhAUHWEHC2mKcL3ezTXlbkmxR_Qa-TZtJ-VLSDPKueZ15DNhIqoiSKQ7Xy3AvTZiyPzqdmLZC0zTKgnc-YyhwHn58QhR-nCd8LoslG8maCVFftmYmErXq8GY-1aMrbOXn84tzRIygQNydcqXWFsJw4Kn9X92KHr_YOg75LBGRwTHJwvlTJIl9YRRS9qT_3E7N3O7OQefV3UalSgoABfYd_cBISGx8rx6FPVgQUsy_6DhgHm5-Qf_4mNKy1U396i39R_ZTk8w4oITJgjJvLTJHGsXKE8qyZJsU4rv4ftij4Rwab9iseG3uEI_lLiwyFJOrlY1mRruhqMZhXq6jZ0eY2zHw4yI9rgaiQX7vo6HML9gpCPb3a1nT-7GmRkbvPisqOl6tI4ziOEENSfMlPFVKYK5KK27cFX8oxr7_1MCr0Og2_gXA6ayzAxHHonEIJexISmQorufwMxtA35GQVQbwGU9jvJynOS6zTF6THRJrolyZ_DIfd1S07NcIVck3Rfif3XgDt9Zi1UzhNP2rQtBkxNw1XlPw2uiLl8DLX23CPLeKTfqsBebvjMy022U_loaNIzOTBZNsQG4A_EbMxDnLFzAHNAD6jiSiawAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رنگ سرخ بر روی پرچم‌های رژیم صهیونیستی
🔹
شماری از فعالان حامی فلسطین، امروز یکشنبه، پرچم‌های رژیم اشغالگر را در  «چهارراه روابی» واقع در شمال رام‌الله به رنگ قرمز در‌ آوردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/681786" target="_blank">📅 22:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681785">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332f90307c.mp4?token=ogZ4PZ-VLFvFSywSAJX1K3HIgtwPkjHo0HQkpAY7VhjBperJlH2p-UxlApk7RPtBpWOwjvjX_gDcrBjimvkXJnO265Sovc9TrmHRJo3YysOqGiC75b2SU9Nkl9p9E7ZArN7PGrytrw4iyVkWHIrW0JVv5pkP-MQi1B-mDVkuVWelUb-gd1bYbsTPQXai85vCXncDm2Ibkn9Mj3AZkD9J07X1a7galzQRbse34BH4bjCvwwpYtd9_bSI1QwPJzOstWKK91M0mGibNkD7xpLsU7_-Ij4CRu9faQdY-qfZn14Re4cCea1l0765KnsRnNl87HvCDVVZCvK1NTLHKYJax2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332f90307c.mp4?token=ogZ4PZ-VLFvFSywSAJX1K3HIgtwPkjHo0HQkpAY7VhjBperJlH2p-UxlApk7RPtBpWOwjvjX_gDcrBjimvkXJnO265Sovc9TrmHRJo3YysOqGiC75b2SU9Nkl9p9E7ZArN7PGrytrw4iyVkWHIrW0JVv5pkP-MQi1B-mDVkuVWelUb-gd1bYbsTPQXai85vCXncDm2Ibkn9Mj3AZkD9J07X1a7galzQRbse34BH4bjCvwwpYtd9_bSI1QwPJzOstWKK91M0mGibNkD7xpLsU7_-Ij4CRu9faQdY-qfZn14Re4cCea1l0765KnsRnNl87HvCDVVZCvK1NTLHKYJax2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: در نهاد ریاست‌جمهوری ۸۰ درصد در مصرف آب، برق و گاز صرفه‌جویی کردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/681785" target="_blank">📅 22:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681784">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3a28d146a.mp4?token=HXpdTpJaJ3PBqnMMvP98W1k56wjTW6wdDT6RvS9lUqkSwat3g2xGY0y7uCd__eS70aArqJMpFMpdu71gt5IHCS_3flNJWlleOOanyNZRShcSGKa6P7lmhiwV-gM9IjXrCwbA8Mq3REZikMpiEHaA7pljVhy1u32I48-zgIr0NfpO4mdy7s3Kjo-JQ1JvGNJKkKYRpfqaHrGf1IhhZH5_asVMtJecFUXjYAC973Sre4JgkgQkf9OIj1Kub_i8cA-AZwIDsUXKjXpyBhKJ-MVZQlIi2TKqCe_2T2AgZXBN_RGEHYChxkrkTZVk-mxWH_EgnQilwscUCWhFTH6qj5XmKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3a28d146a.mp4?token=HXpdTpJaJ3PBqnMMvP98W1k56wjTW6wdDT6RvS9lUqkSwat3g2xGY0y7uCd__eS70aArqJMpFMpdu71gt5IHCS_3flNJWlleOOanyNZRShcSGKa6P7lmhiwV-gM9IjXrCwbA8Mq3REZikMpiEHaA7pljVhy1u32I48-zgIr0NfpO4mdy7s3Kjo-JQ1JvGNJKkKYRpfqaHrGf1IhhZH5_asVMtJecFUXjYAC973Sre4JgkgQkf9OIj1Kub_i8cA-AZwIDsUXKjXpyBhKJ-MVZQlIi2TKqCe_2T2AgZXBN_RGEHYChxkrkTZVk-mxWH_EgnQilwscUCWhFTH6qj5XmKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکید رئیس‌کل بانک مرکزی بر پیگیری مسائل صادرکنندگان و پیمانکاران ایرانی در عراق
🔹
رئیس‌کل بانک مرکزی در دیدار با تجار، صادرکنندگان و پیمانکاران ایرانی در سفارت ایران در بغداد، مسائل و موانع فعالیت اقتصادی در بازار عراق را بررسی کرد.
🔹
موانع بازگشت ارز صادراتی، مشکلات تعرفه‌ای، مطالبات پیمانکاران و نیاز به ضمانت‌نامه حسن انجام کار از مهم‌ترین موضوعات مطرح‌ شده در این دیدار بود.
🔹
همتی با تأکید بر اهمیت بازار عراق برای فعالان اقتصادی ایران گفت این مسائل با جدیت پیگیری خواهد شد و بانک مرکزی برای تسهیل فعالیت صادرکنندگان و پیمانکاران ایرانی و افزایش هماهنگی میان دستگاه‌های دولتی و بخش خصوصی تلاش خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/681784" target="_blank">📅 22:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681783">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cd296c47d.mp4?token=qE1Surmma9HzA3L985A5JRoTelDxezhPMbMG377f2Gb3AhkHnn_DITbhMd4aqztELkNCGHt_cqYAKUPNU4TjPFYG0A6lCUI_kleDVLX58IqLeEQqBEzTVfviyQfBb_mzyce58g0aiZOXosIkr5GocuRkXRIBhvH9M3APeJdcPn6CM1YFN7iOwAqhSGFJlDo5ckkJ7kcEhmvjuevt3_V9Sk6RyKdcMp_xcfieznEB81z2BRPXzq_h7z4AN5KeQizO0EhHt1L-4aYVGyzUlkuWGgfnfl19Y9Be_TWweF2ryCPgeSVdCokiWWPpwL_iTCMGbUsA7wiC5MzDQCnCF7u5BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cd296c47d.mp4?token=qE1Surmma9HzA3L985A5JRoTelDxezhPMbMG377f2Gb3AhkHnn_DITbhMd4aqztELkNCGHt_cqYAKUPNU4TjPFYG0A6lCUI_kleDVLX58IqLeEQqBEzTVfviyQfBb_mzyce58g0aiZOXosIkr5GocuRkXRIBhvH9M3APeJdcPn6CM1YFN7iOwAqhSGFJlDo5ckkJ7kcEhmvjuevt3_V9Sk6RyKdcMp_xcfieznEB81z2BRPXzq_h7z4AN5KeQizO0EhHt1L-4aYVGyzUlkuWGgfnfl19Y9Be_TWweF2ryCPgeSVdCokiWWPpwL_iTCMGbUsA7wiC5MzDQCnCF7u5BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: باید با سرمایه‌گذاری روی فرزندان خود به توانمندی‌هایی برسیم که کسی جرئت نکند به خاک ما حمله کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/681783" target="_blank">📅 22:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681782">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b9644dc1.mp4?token=Ufp_gxiw_xHZQhLxE8yvOl8fyPxtXPI_IrYiPq0sy90sra7BF97i4kvrq7FCNbxfGkGUs5wvwy1MUTzoKqJkhZchwmwP6CBMWFzE-w0hS5vhOckEFVQyDRylij3jfGINSf12Zb9_E9bYN9BBZ3slHKLRVRoSRYLgUHP2nzJC8Ywcm7TBUJwpXKOYhEJzpMA7GUi8jy5gi3OqO0W2744oLirf50MmViqwl74CB0Nlsi1pa6_J6tZgX9FC8fQQlikebkIn4cgDUOVVPel-2-RQVFU1zU4F9t-9jWHXjUyYpmHgy7q-Q6e0pMQx-e82VRVgOcvnJSPm-OYUBQTwBaJJQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b9644dc1.mp4?token=Ufp_gxiw_xHZQhLxE8yvOl8fyPxtXPI_IrYiPq0sy90sra7BF97i4kvrq7FCNbxfGkGUs5wvwy1MUTzoKqJkhZchwmwP6CBMWFzE-w0hS5vhOckEFVQyDRylij3jfGINSf12Zb9_E9bYN9BBZ3slHKLRVRoSRYLgUHP2nzJC8Ywcm7TBUJwpXKOYhEJzpMA7GUi8jy5gi3OqO0W2744oLirf50MmViqwl74CB0Nlsi1pa6_J6tZgX9FC8fQQlikebkIn4cgDUOVVPel-2-RQVFU1zU4F9t-9jWHXjUyYpmHgy7q-Q6e0pMQx-e82VRVgOcvnJSPm-OYUBQTwBaJJQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان رو به مدیران: شما می توانید در روش آموزش تغییر ایجاد کنید
🔹
هر چیز که در جستن آنی، آنی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/681782" target="_blank">📅 22:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681781">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e3387030c.mp4?token=Mm2NIptUXtr21u7U3IA9-LbgmguRWjJR0wx4WaW0bt1vA4KLI5GVMBwqov8P30OR5VVZRt3bggYnyiLfRMeYagbdhity71-8pGaCDJ4dfWznjvUaLjKrqYDB6wNJICMNQ5rzjtvMGzcB7BbGrVFgkoTX8cu3L8ZVF73qWTtl8aPUmoBElMQEEuWEUprAtnTWwSmyUo_JPBesUv_ae5YtP6FHRp5Vm8svT8oD5dMPd6TeU5ktR64RLpzWC-bsACMNWT8CKYTPoDjDjkKpUyBp-qckVTzoPaeCFRgmM6wPhB1qokZwRJqCJtpme4uSClLqr-pD2UKsj4wuj0I9Bv2Jbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e3387030c.mp4?token=Mm2NIptUXtr21u7U3IA9-LbgmguRWjJR0wx4WaW0bt1vA4KLI5GVMBwqov8P30OR5VVZRt3bggYnyiLfRMeYagbdhity71-8pGaCDJ4dfWznjvUaLjKrqYDB6wNJICMNQ5rzjtvMGzcB7BbGrVFgkoTX8cu3L8ZVF73qWTtl8aPUmoBElMQEEuWEUprAtnTWwSmyUo_JPBesUv_ae5YtP6FHRp5Vm8svT8oD5dMPd6TeU5ktR64RLpzWC-bsACMNWT8CKYTPoDjDjkKpUyBp-qckVTzoPaeCFRgmM6wPhB1qokZwRJqCJtpme4uSClLqr-pD2UKsj4wuj0I9Bv2Jbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جدال بلژیک با بزرگترین آتش‌سوزی جنگلی ثبت‌شده در تاریخ  این کشور
🔹
بلژیک با بزرگ‌ترین آتش‌سوزی جنگلی ثبت‌شده در تاریخ مبارزه می‌کند.
🔹
این آتش سوزی تاکنون ۳۰۰۰ هکتار از زمین‌ها را سوزانده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/681781" target="_blank">📅 22:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681780">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6Nz0EqjrY6xU91-fsaoL1YygN78UlDGdctHhAa-br0LgU8FR-GTkP8B8y4fKYsVmcqK30i0RQx5dUcxjQK3QJA5jmM3jeya3tqFu3aHrvyFYZB5FxrVw7jjm4at-ofXcKnTHxO_bnRTTWNGXg1SiQrVaJTnzE1fWbEGe59IBRYV6aVSLbBE-fM502UTiZXV1bFLkP-pDjU6WKKPsX2Dr7JceWAweJ_M0muM-LvwuTwty4rhIoPSTMKg8c16Lb9poSdljjKHKWPceDLYjmgVGfhrYrrz_kQ0CSfTcfAmqSfi6RfPLQrdKrpUHQs5bmNXAPxm9vtp3U1d2XZ5cvA3lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برگزاری کارگروه ملی امام رضا(ع) با حضور تولیت آستان قدس رضوی و وزرای دولت در حرم مطهر رضوی
آیت الله مروی، تولیت آستان قدس رضوی:
🔹
آستان قدس برای اداره حرم مطهر و ارائه خدمات در داخل حرم، به بهترین شکل ممکن، نیازمند کمک دولت نیست؛ اما آیا تأمین پارکینگ در خارج از حرم نیز باید بر عهده آستان قدس باشد؟
🔹
سالانه حدود ۳۰ میلیون زائر به مشهد می‌آیند و هر زائر نیز دست‌کم مبلغی را در این شهر هزینه می‌کند. طبیعتاً گردش مالی حاصل از حضور این تعداد زائر، رقم قابل‌توجهی است، اگر از این گردش مالی و درآمدهای حاصل از آن مالیات دریافت می‌شود، انتظار ما این است که سهمی از این درآمدها برای توسعه زیرساخت‌ها و خدمات مورد نیاز زائران اختصاص پیدا کند.
🔹
انتظار داریم در حوزه حمل‌ونقل ریلی و جاده‌ای، به‌ویژه مسیر مشهد ـ تهران، شاهد یک جهش واقعی باشیم و زمان سفر ریلی این مسیر کاهش یابد.
🔹
از مسئولان درخواست می‌کنیم برنامه‌های مربوط به دهه پایانی ماه صفر را به‌عنوان یک موضوع مستقل ببینند و آن را صرفاً ذیل عنوان و سازوکار اربعین تعریف نکنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/681780" target="_blank">📅 22:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681779">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41e1af3ee.mp4?token=vSF8fBgVOuLbYVLrX_zPDWfTKJXBleAx0FL6W6zM8ZiIq7ZM9m0QUqn9i8sSj5PRWZUbUR4VCZfJa9ok8HYg0dU1aYJZSI8MizhhN2ox8K9GiI74SaMOgPIMzCzMA28Y14cpOi2-i39idIK_DWsYc42SgJNO58_NNmMOFXm99DPA9I3OkDyj-q3a_SC8APJmayhOaMylsMetLS99gfxGkeSRNjmsVECbSl7n3fPLoIgsq5-HZ5F9hHdM6nNlxl2kJq0BX3eGHkzNZylYqZn6Y3xSYLPH5m1hvxnw_vgVtyNDoLajFfjlnKCNQ4W8468CBw59a8-aV1xjw0yefScW9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41e1af3ee.mp4?token=vSF8fBgVOuLbYVLrX_zPDWfTKJXBleAx0FL6W6zM8ZiIq7ZM9m0QUqn9i8sSj5PRWZUbUR4VCZfJa9ok8HYg0dU1aYJZSI8MizhhN2ox8K9GiI74SaMOgPIMzCzMA28Y14cpOi2-i39idIK_DWsYc42SgJNO58_NNmMOFXm99DPA9I3OkDyj-q3a_SC8APJmayhOaMylsMetLS99gfxGkeSRNjmsVECbSl7n3fPLoIgsq5-HZ5F9hHdM6nNlxl2kJq0BX3eGHkzNZylYqZn6Y3xSYLPH5m1hvxnw_vgVtyNDoLajFfjlnKCNQ4W8468CBw59a8-aV1xjw0yefScW9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی دندان آخری قصد بیرون آمدن را ندارد باید اینگونه آن را بیرون آورد
!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/681779" target="_blank">📅 22:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681778">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
آموزش و پرورش آماده برگزاری حضوری کلاس مدارس در سال تحصیلی جدید است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/681778" target="_blank">📅 22:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681777">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnapptrip | اسنپ‌تریپ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAzVzMZ5ouN35IrEXIOFZGDanT2hKjPUKzGxVKlNEmN9sOWwvALxFRwjFHb8V8r2FlP6oP5ROMc_7QWAMXJFeu7i_ZgPSDezmtCPuJV-vKJANEnrOKEKW1Af70NMiSrVLlnxNCgCwXnK14xdPEvRaANyxEJuleBBGspNAfXayqoEmmx7WLLJzLs9yrm1BR3JptjZ4u083S_Giwdidwnls_m6gZ7ixvDUFpvmU1V--QN5KszIN3GzNUEUfnIVdm4Pf26Q5BkbVDqb1molvzc0MNWhDzZmzU2GOTInBbgjv9yqowDJKDRDYKLS93AeychctEs1xiIJ_qcTU0e2rMYW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
: پیش‌فروش بلیت قطارهای شهریور:
«
دوشنبه، ۲۶ مردادماه، ساعت ۸:۳۰ صبح»
🔺
تا ۵۰ هزارتومان تخفیف
با کد:
SHAHRIVAR
50
✅
خرید از وب‌سایت اسنپ‌تریپ و یا بخش «بلیت سفر» در اپلیکیشن اسنپ
🚂
خرید مستقیم:
https://snp.tips/40lda
🔹
@snapptrip</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/681777" target="_blank">📅 22:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681776">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
اعلام آمادگی جمهوری اسلامی ایران برای کمک به زلزله‌زدگان اندونزی
🔹
مسعود پزشکیان در پیامی به رئیس‌جمهور اندونزی ضمن همدردی با زلزله‌زدگان این کشور از آمادگی ایران به منظور ارسال کمک‌های بشردوستانه خبر داد.
🔹
متن پیام بدین شرح است؛
بسم‌الله الرحمن الرحیم
جناب آقای پرابوو سوبیانتو
رئیس‌جمهور محترم اندونزی
🔹
وقوع زمین‌لرزه شدید در شرق اندونزی و جان‌باختن و مجروح شدن جمعی از مردم آن کشور، موجب تألم خاطر شد.
🔹
اینجانب مراتب همدردی و تسلیت صمیمانه خود را به جناب‌عالی، دولت و ملت دوست اندونزی، به‌ویژه خانواده‌های داغدار و آسیب‌دیده، ابراز می‌دارم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/681776" target="_blank">📅 22:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681775">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9bvxX-Z8fn-xnLXxJkp8VfKeuFeugB48vzLFD8f_-8fFE6gI6CRLACRlcQjY-XaBeMDxKb4V-wzMdSV7oAEsHbDxkO492q17HRltCA7ylyQtImP37pA9CkDUQS7yFpgXAuZj4pU9K4LRWMW-g986UDOCd3YCVHmYPPpbn0it7xyEcdGpOBwyDPPqBU39naQmrtfq3Ujlb-Dc3pjjZ0hTQD1_-BxaR9r8sE7IcV3dTfn556WSRmuG7DaDZD4HpX3uyNt3O8qhf-xBy2PYnNin_JADu_uHbsm8TJVx5QMadhd7BdT3NtZnWYNvMXtK5xF9HFRsw6dGr4Z5TKH_3ymPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جعلی یک کاربر هندی درباره ایران سر از سخنرانی نتانیاهو در آورد
گلف‌نیوز:
🔹
این ادعا ابتدا از سوی یک حساب کاربری هندی منتشر و طی چند ساعت، توسط حساب‌های پرمخاطب اسرائیلی و سپس شبکه ۱۴ اسرائیل بازنشر شد. در نهایت نتانیاهو هم در سخنرانی خود به این ادعا استناد کرد.
🔹
فاکس‌نیوز نیز این ادعا را مطرح و آن را به‌عنوان نشانه‌ای بالقوه از نیات هسته‌ای ایران بررسی کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/681775" target="_blank">📅 22:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681774">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6162afaa76.mp4?token=GbZx-vXeVAzxXqtAQJ2sdWvxYH4TuWIP7OB4umn0M-B2UENMPoB3InqvSy-K9r_I0O_bt-qjK_vKksqsVcsk9fjxS6OO8DI1grHA-uFlYg40nMuf6BnbFeiPLO2IAUx35FBRvphyJ8cknxLx_iNyPneJ4Ar6RgbLalk_L1Z-uvcV57G-6YAymOWxcpdsMaSNEUWuHrr1V8kqGPib9W9WFqGNyLocBf4bR2L3Lm5taPCsgMUtkTMJeMTNdoAZj2YDZBijy1cP0woSVFob7jWEphEPBxiqJztriK6w5ymWoSt1Qg-Ja-z2kBqNrAuSyUpX7wJjEtKYCbycGMikaYIArA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6162afaa76.mp4?token=GbZx-vXeVAzxXqtAQJ2sdWvxYH4TuWIP7OB4umn0M-B2UENMPoB3InqvSy-K9r_I0O_bt-qjK_vKksqsVcsk9fjxS6OO8DI1grHA-uFlYg40nMuf6BnbFeiPLO2IAUx35FBRvphyJ8cknxLx_iNyPneJ4Ar6RgbLalk_L1Z-uvcV57G-6YAymOWxcpdsMaSNEUWuHrr1V8kqGPib9W9WFqGNyLocBf4bR2L3Lm5taPCsgMUtkTMJeMTNdoAZj2YDZBijy1cP0woSVFob7jWEphEPBxiqJztriK6w5ymWoSt1Qg-Ja-z2kBqNrAuSyUpX7wJjEtKYCbycGMikaYIArA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش تشخیص کابل شارژر اورجینال از فیک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/681774" target="_blank">📅 22:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681773">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
زخم اصلی اقتصاد
🔹
ما در میانه جنگ و تنش با آمریکا ایستاده‌ایم، جایی که اقتصاد ضعیف، می‌تواند به اندازه یک تهدید نظامی، امنیت یک کشور را به خطر بیندازد.
وقتی ارزش پول ملی زیر فشار است، تجارت دشوار می‌شود، هزینه تولید بالا می‌رود و سفره مردم کوچک‌تر می‌شود، دیگر نمی‌توان اقتصاد را با همان نسخه‌های دیروز اداره کرد.
🔹
اما زخم اصلی، عمیق‌تر از جنگ و تحریم است.
اقتصاد ایران سال‌هاست از بیماری مزمنی رنج می‌برد؛ دولتی که به‌جای داوری، خودش وارد بازی شده است.
فرقی نمی‌کند دولت، خود را عدالت‌خواه بنامد یا توسعه‌گرا، محافظه‌کار باشد یا مدعی بازار آزاد.
🔹
وقتی قدرت سیاسی از سیاست‌گذاری‌های کلان عبور می‌کند و به قیمت، تولید، تجارت، سرمایه‌گذاری و کوچک‌ترین تصمیم‌های اقتصادی دست می‌برد، حاصل اغلب یک چیز است؛ رقابت کمتر، رانت بیشتر و آزادی کمتر.
🔹
دولتی که به نام حمایت، قیمت تعیین می‌کند به نام عدالت، منابع توزیع می‌کند و به نام مدیریت، بازار را محدود می‌کند، دیر یا زود انگیزه تولید و سرمایه‌گذاری را فرسوده خواهد کرد.
🔹
در چنین اقتصادی، کارآفرین دیگر تمام فکرش معطوف به مشتری و نوآوری نیست، بخشی از ذهنش همیشه درگیر بخشنامه فردا، تغییر مقررات، مجوز، مالیات و تصمیم ناگهانی سیاست‌گذار است.
🔹
و درست همین‌جا، بخش خصوصی واقعی عقب می‌نشیند و جای خود را به انحصار، وابستگی و رانت می‌دهد. جایی که سود خصوصی می‌شود، اما هزینه‌اش بر دوش جامعه می‌افتد.
البته آزادی اقتصادی به معنای بی‌قانونی نیست. دولت باید قانون را حاکم کند، مالکیت را امن نگه دارد، امنیت ایجاد کند و با انحصار و فساد بجنگد.
🔹
اما مشکل از لحظه‌ای آغاز می‌شود که داور، خودش پیراهن بازیکن را به تن کند و بعد نتیجه مسابقه را هم تعیین کند.
🔹
رفاه با فرمان ساخته نمی‌شود با آزادی مبادله، رقابت، امنیت مالکیت و امکان خلق ارزش ساخته می‌شود.
🔹
شاید سؤال اصلی این نباشد که «کدام دولت بهتر اقتصاد را اداره می‌کند؟»
سؤال عمیق‌تر این است «چرا باید دولت تا این اندازه اقتصاد را اداره کند؟»
🔹
شاید برای نجات اقتصاد، پیش از آنکه چیزی به آن اضافه کنیم، باید دست از دخالت‌های اضافه برداریم.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/681773" target="_blank">📅 22:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681772">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-xZ8in2HVNPYX3JGuD4Ke53bhr9SYP11UNaHkqbdgnKOLzXC51Snhat4h_778VWq0kodT_E0ADEFNm7dRprXdWPgErlmOttHj2Szm2PG60UAq4-GXehEKGXeExZvW8FkPKXro5mtitGNx0h3EOi1z7qSLdzqfoNTmWhFaQB9VQcqZLW-uzEK7U3pcC1wj31K07mVrvGYf64uOdob3kArDJzZ3fSn5hQqxJXJhDTics7j3CZ2WJIWiV8k-4d9VUBOKdw50xn0i2uyrX5vhBIBvm4DFuvWMuuWgmY97FXhZrhPgFQBNbT_ATlGprE_GiajSCovOslZmrnUXL3fwsphA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بعضی رفتارها، آرام‌آرام فاصله می‌سازند؛ حتی میان نزدیک‌ترین آدم‌ها
🔹
امام علی(ع) در نهج‌البلاغه یادآوری می‌کند که خشمگین یا شرمنده‌کردنِ دیگران می‌تواند رشته‌ محبت و صمیمیت را سست کند. رابطه‌ها فقط با حضور حفظ نمی‌شوند؛ احترام، ملاحظه و حفظ حرمت آدم‌هاست…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/681772" target="_blank">📅 22:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681771">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عارف: دشمن می‌خواهد شکست نظامی خود را از طریق جنگ اقتصادی جبران کند
🔹
معاون وزیر نیرو: در تلاشیم دورهٔ زمانی صدور قبض‌های برق را کاهش دهیم
🔹
وزیر دارایی عراق: بستن تنگه هرمز اثرات مستقیمی بر اقتصاد عراق گذاشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/681771" target="_blank">📅 22:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681770">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
احتمال تشدید درگیری‌ها بین لبنان و اسرائیل
کانال ۱۲ تلویزیون اسرائیل به نقل از یک منبع امنیتی:
🔹
ارتش در پی وقایع ارتفاعات علی طاهر، خود را برای تشدید احتمالی تنش در لبنان آماده می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/681770" target="_blank">📅 21:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681769">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEUIS9FxuimFYIaZkoBF2tXaEmeC3LSKVMnSp9DVpTQUEkcbwe2376Kx08FdHLB8SXlLdaR8H2q78L35V446bRASgqzRrsELIAoYag3M7CeoEvNvwYh7Eo4J7o2nq-ciI3PULy3rIu9FCZM7ji5sXv_RIAeodvIvjm200dUPP5fjV3oS0ELTgmPuS-YnHoBFJV-rIvIavvZHa6c7tHntXo8ISE_vwk9P3JScR4LbImMiKeSI3PxkuT49XOIO3HVAjhiyTY3vIH64TgLiLcCkwKUk9FQ1Wul9LaK1t8VpCpKhzlUUx3hyTPbFB2i3yQlp72hZ-NIKzPdjkRjs51Rl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده توپ طلا در راه ایران؟
یکی از بزرگ‌ترین ستاره‌های فوتبال جهان در راه ایران است؛ اما هنوز هویت او رسماً اعلام نشده.
طبق اطلاعات منتشرشده، یکی از برندگان سابق توپ طلا قرار است به‌زودی در اتفاقی ویژه مرتبط با ایران حضور داشته باشد؛ ستاره‌ای که سال‌ها در بالاترین سطح فوتبال اروپا بازی کرده و افتخارات بزرگی در کارنامه دارد.
نزدیک شدن به پایان مهلت نقل‌وانتقالات لیگ برتر، گمانه‌زنی‌ها را بیشتر کرده؛ اما فعلاً هیچ نامی به‌صورت رسمی تأیید نشده است.
کدام ستاره در راه ایران است؟</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/681769" target="_blank">📅 21:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681768">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4a0d90a9.mp4?token=SArPQqRwHr7wAoSeVogczAu4HvdjBbaDwZIqyq202VZXRn9aIxW-L85N4Kkt2LhE9A_bcQn0UTqdAic01ap1U8y5j_RyJ2v6eYqstOLQcFzihqehmolSNSU5rQLiNSReN2mcKE_uHVGDNLTtWC88nxuPyfLSfywWmpPqrwrMw4RUuh9qqrGEYa9KIlWtYhEwCqeB4L4kGoCCvVBtJIjXwvrDEYmwqyodVxwSqhaF1YGZJLP0rzeBNWHtAXj2ZwCJTKmfIFdZv386ReoQYNaVqShpUcBQqq8qPyMMMGepHMV5-6SGf3USxNqSR5OwKHoLAvLvttSmky4SfyFfB-zodcABBav1KxeJF0XMYVZrMBkXA6PnAigEfgdqpixsBojFXPEZqyuZjP83OJBVF6WOwZGW2f4lphWpLSVhIusrXD9crWGpz0cTMhG8LvkwJhpuhqjYGHEwbWhGQdywNZ2KIC4e-H1TwwreSPBuuOvU8LzeWIiA05vut_lXBBaUlmv2Rwxm5L9LTAzB-Xd2U_V1CFFLpeepKyCa4_O6tR5TmBzMi5KSQ8kKQ5yJY5MPXYpVDXomATB_1CKA7pw58xj9Pp97GoAAtX7hMHg4_ZOoqDiO56yreI3rDTKN_AJacEgwIX4O9yzgjUPf4QD9YUUZf8myu2xcMgAE19FiKSlzYKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4a0d90a9.mp4?token=SArPQqRwHr7wAoSeVogczAu4HvdjBbaDwZIqyq202VZXRn9aIxW-L85N4Kkt2LhE9A_bcQn0UTqdAic01ap1U8y5j_RyJ2v6eYqstOLQcFzihqehmolSNSU5rQLiNSReN2mcKE_uHVGDNLTtWC88nxuPyfLSfywWmpPqrwrMw4RUuh9qqrGEYa9KIlWtYhEwCqeB4L4kGoCCvVBtJIjXwvrDEYmwqyodVxwSqhaF1YGZJLP0rzeBNWHtAXj2ZwCJTKmfIFdZv386ReoQYNaVqShpUcBQqq8qPyMMMGepHMV5-6SGf3USxNqSR5OwKHoLAvLvttSmky4SfyFfB-zodcABBav1KxeJF0XMYVZrMBkXA6PnAigEfgdqpixsBojFXPEZqyuZjP83OJBVF6WOwZGW2f4lphWpLSVhIusrXD9crWGpz0cTMhG8LvkwJhpuhqjYGHEwbWhGQdywNZ2KIC4e-H1TwwreSPBuuOvU8LzeWIiA05vut_lXBBaUlmv2Rwxm5L9LTAzB-Xd2U_V1CFFLpeepKyCa4_O6tR5TmBzMi5KSQ8kKQ5yJY5MPXYpVDXomATB_1CKA7pw58xj9Pp97GoAAtX7hMHg4_ZOoqDiO56yreI3rDTKN_AJacEgwIX4O9yzgjUPf4QD9YUUZf8myu2xcMgAE19FiKSlzYKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفتار عجیب یک شهروند شیرازی با خودروی آتش‌نشانی
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/681768" target="_blank">📅 21:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681767">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31a37ebdf.mp4?token=ZE3xms4BVooU6a7rL8pmH7bZ8xuvbxlBS25kra2m_nfoBS790moOuW5xsZGK-kNIQmkuA7Vm2YJgQ4-tXyCwnhQI5lM9RbM9xlpykHM00Xj-CqJQRtE2BLkYcSZtfhAC3rd8CZv4-NrEBXdqVHlL_OCGMixx8wvxp24x1BsHpeSkLRlY69qIZ21lCgTmt9Iy0alKjZ5wc4FZ4erRMZ_cdEQ9WsSfhE_t7tdtfkHups_VaqmsLu2cpHVHChGnuFn_Zpf8ZEUxun4Qz2V_31nLJptt2-CPFlnAOcX5q-8sCPb7y1U__c1uwhUzeqv8i9Zf3CaKDX_J7PZ4V-SpmOdaCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31a37ebdf.mp4?token=ZE3xms4BVooU6a7rL8pmH7bZ8xuvbxlBS25kra2m_nfoBS790moOuW5xsZGK-kNIQmkuA7Vm2YJgQ4-tXyCwnhQI5lM9RbM9xlpykHM00Xj-CqJQRtE2BLkYcSZtfhAC3rd8CZv4-NrEBXdqVHlL_OCGMixx8wvxp24x1BsHpeSkLRlY69qIZ21lCgTmt9Iy0alKjZ5wc4FZ4erRMZ_cdEQ9WsSfhE_t7tdtfkHups_VaqmsLu2cpHVHChGnuFn_Zpf8ZEUxun4Qz2V_31nLJptt2-CPFlnAOcX5q-8sCPb7y1U__c1uwhUzeqv8i9Zf3CaKDX_J7PZ4V-SpmOdaCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لطفا بذار ذهنت استفراغ کنه
🔹
با دیدن این تیتر تعجب نکنید و این ویدئو رو ببینید، شاید به شما کمک کرد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/681767" target="_blank">📅 21:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681766">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ID7nFBtHr6uvQSM9P0OF7he5VoBcHGy8SM9Mup_60UmQoSGTJj6fnOeSTA7Do5-8HjYR8f4px4mPdMlnkFkIP4ylkOIyNm3g3oPuMaeWII1r9uE8kQRf6X8-dackdNJlS0OND5AOXzZj_Di89yROQpmtsYpoN6RBpUUQG925Fmbfm08QBCPlyKv7v7lNo-HuiafBGMAmDDL7qACR4uO48Xvw6sUaI1BLGaGrrIphyIKs9A5tp3SveQq42HY63MAO5DCoTZOBu6fQH0OakxuvzqOEJr5qzCdk30tIc7eIs8EFZfW4C8v4RgKCclcR7JkzFd6yZ9HdaSyHvLAyDJVhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این صفحه و پیام صادر شده از آن درباره قطر که منتسب به فرمانده نیروی هوافضای سپاه است جعلی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/681766" target="_blank">📅 21:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681765">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e56aeee87.mp4?token=BiBVWD2c7KaPxgDEVGCH0CnFZkhckmbBRmKsoJBek1JcUZfxiqthc603xQ0Oe_z0_EqAqI8ZuM2JpqOl4hMm2kNRBGfpzSmO0ErsQTp5XSyudT3VCt9MUx5dGqkN9cgrwx1GVie2NeuQLcRE1i2rGCU7-A_FUn-_m2VSnyJ5aDVzisatIg1UqiwDXubPFidFppsVg63Ar2Xh1RMfqEribeoJJXoUo43vyAR6dwWYc3XxMQOcSq6ADxCcsTYBIKG1zCc2V1Er3mSKgUX3lg5kKwiSBoXnTu6_HnyoqJZbiUmI8Y8fP-9czz6RWS7eXH0sIJ-tdpETtCozAT8Ai7p5lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e56aeee87.mp4?token=BiBVWD2c7KaPxgDEVGCH0CnFZkhckmbBRmKsoJBek1JcUZfxiqthc603xQ0Oe_z0_EqAqI8ZuM2JpqOl4hMm2kNRBGfpzSmO0ErsQTp5XSyudT3VCt9MUx5dGqkN9cgrwx1GVie2NeuQLcRE1i2rGCU7-A_FUn-_m2VSnyJ5aDVzisatIg1UqiwDXubPFidFppsVg63Ar2Xh1RMfqEribeoJJXoUo43vyAR6dwWYc3XxMQOcSq6ADxCcsTYBIKG1zCc2V1Er3mSKgUX3lg5kKwiSBoXnTu6_HnyoqJZbiUmI8Y8fP-9czz6RWS7eXH0sIJ-tdpETtCozAT8Ai7p5lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نایب‌رئیس مجلس: از دولت درخواست می‌کنیم اصلاح قانون بودجه را در قالب لایحه برای مجلس آماده کند؛ مجلس آماده است بودجه‌ای با محوریت معیشت مردم و برای حل مشکلات آنان تصویب کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/681765" target="_blank">📅 21:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681764">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d120771984.mp4?token=ESt0m_URZ7KDKXGbpaoCBz1WJTsnhdo_y9gg-2c-d47ia6738_cGrCAL6AczXXuWRdoJyOfRiLMZ7jm2dYHI_XtKOKYFuRa3FJPFQ8TyBpDYYsBmvwk7CJP4FZPBbuNVtKgR57Ijrv_SK1dwPJQMoltOuP09a74Epv2JTAqg2Hb7TF3g5aSX1ITc6HTHA5N-79CKflHaRtRtO4XXAXPvPMHSckJZvyu5MbmDbiR7LsF8xl5z7A_JXyfm7WbkSvtAEdD_NEgC5qD4s9hIeBElfr-vmzt30sj6jkkWXGc2pWNjNTxUtuwdmCU5ilyl-v6e6sFJmO16jPqILQv0nqnpSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d120771984.mp4?token=ESt0m_URZ7KDKXGbpaoCBz1WJTsnhdo_y9gg-2c-d47ia6738_cGrCAL6AczXXuWRdoJyOfRiLMZ7jm2dYHI_XtKOKYFuRa3FJPFQ8TyBpDYYsBmvwk7CJP4FZPBbuNVtKgR57Ijrv_SK1dwPJQMoltOuP09a74Epv2JTAqg2Hb7TF3g5aSX1ITc6HTHA5N-79CKflHaRtRtO4XXAXPvPMHSckJZvyu5MbmDbiR7LsF8xl5z7A_JXyfm7WbkSvtAEdD_NEgC5qD4s9hIeBElfr-vmzt30sj6jkkWXGc2pWNjNTxUtuwdmCU5ilyl-v6e6sFJmO16jPqILQv0nqnpSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزۀ مقاومت: رژیم صهیونی درحال تلاش جدی برای تصرف مناطق و تاسیسات استراتژیک علی‌الطاهر است/ رزمندگان حزب‌الله لبنان با تلاش نظامیان صهیونیست برای پیشروی در ارتفاعات استراتژیک علی الطاهر مقابله و ده‌ها اسرائیلی را زخمی کردند./ ارتش رژیم صهیونیستی درپی ناکامی‌های خود بمب‌هایی را بر روی منطقه علی‌الطاهر انداخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/681764" target="_blank">📅 21:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681762">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ادعای بلومبرگ: انتقال مخفیانه نفت از تنگه هرمز توسط اعراب
ادعای بلومبرگ:
🔹
به گفته افرادی که از این محموله‌ها اطلاع دارند، انتقال نفت از طریق تنگه هرمز به‌صورت مخفیانه و بدون شناسایی، و سپس انتقال محموله‌ها به نفتکش‌های دیگر در خلیج عمان، با حداکثر ظرفیت ادامه دارد؛ این روند حتی با وجود حملات اخیر به کشتی‌ها متوقف نشده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/681762" target="_blank">📅 21:27 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681761">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc5b727823.mp4?token=EtIsahzErpiU5W1Fiv_7yni372p0aDqw07vo6lhMDjOvW9mcNsQ62-mhIO344e-_o1i4tCLrC1XhK7S5quv5kBrKOfE2KHxpxOdY_zxIg-xJOrRpNN4-eRNaUyAs6xnqQ_s_X-xxkFFA9pO4JEo_ZDRs4dRFXfSmnId4xL7YYbAWaMz172UhIfzdjh8NScB4MFXvWPp4VWeYBDX1GBiIGyAiEsNYMvQfoqMN0CJ_CPP2PHVj8U2zLFIGJvl0uU0QUJjfn9DjhX7JreREfYSzWRbpSotRANMBcfxsD46zUvhv1PpqxjBapqHMNjMhoaFinFfk72JY0fhqH6A0f1O2m4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc5b727823.mp4?token=EtIsahzErpiU5W1Fiv_7yni372p0aDqw07vo6lhMDjOvW9mcNsQ62-mhIO344e-_o1i4tCLrC1XhK7S5quv5kBrKOfE2KHxpxOdY_zxIg-xJOrRpNN4-eRNaUyAs6xnqQ_s_X-xxkFFA9pO4JEo_ZDRs4dRFXfSmnId4xL7YYbAWaMz172UhIfzdjh8NScB4MFXvWPp4VWeYBDX1GBiIGyAiEsNYMvQfoqMN0CJ_CPP2PHVj8U2zLFIGJvl0uU0QUJjfn9DjhX7JreREfYSzWRbpSotRANMBcfxsD46zUvhv1PpqxjBapqHMNjMhoaFinFfk72JY0fhqH6A0f1O2m4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجمع معترضان به نسل کشی اسرائیل مقابل موزه‌ای در اسپانیا
🔹
در شهر بیلبائو در اسپانیا، مردم در اعتراض به نسل‌کشی رژیم اسرائیل علیه فلسطین،  مقابل موزه گوگنهایم روی زمین دراز کشیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/681761" target="_blank">📅 21:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681760">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
جهش دوباره مسکن تهران؛ هر متر نوساز ۲۷۰ میلیون تومان شد
🔹
پس از حدود دو سال رکود سنگین، بازار مسکن تهران در نیمه دوم سال گذشته وارد فاز جهش شد.
🔹
متوسط قیمت آپارتمان‌های نوساز طی یک سال از حدود ۱۲۰ میلیون تومان به ۲۷۰ میلیون تومان در هر مترمربع رسیده است. متوسط قیمت واحدهای نوساز تهران به محدوده ۱۵۰۰ دلار در هر مترمربع نزدیک شده است.
🔹
این ارقام مربوط به واحدهای نوساز است و طبیعتاً از میانگین قیمت کل آپارتمان‌های تهران بالاتر محسوب می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/681760" target="_blank">📅 21:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681759">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVE8FYn0CR3PLvNCUvdc-9DCDBycCkB05MSbd7LyURoFgtUROQFC4CWS7m3k7TiDJxKv9OCOJTJKsxDjWzb_GKs2FQb8iU5_soPRwbIkvBNjnG2lgf-TCsFrZa3Eo2zd9mv_USRU_KK4oXEvcHLN62R5ZUBHga92WexsoNjOmrZKQIyl7lK4i7eCoHAE0MHhCkViBNDGIsiPeqD2MjnsxEoECbwJlTC3w7-RF-w7XGYQbNoQlrvI2EGJuGAzHN8OJ7EkMu_C9EGn9_qlNkkBQx-OiTbxd1Ef3QbstSmuRrEJzEXtV7l2ZCZYAVnRWnEH1y2nCV8KITUHnDhuY4maYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقایی امور خارجه ایران: واشنگتن کانادا را «ایالت پنجاه‌ویکم» خود می‌خواند
🔹
واشنگتن بر کالاهای کانادایی تعرفه وضع می‌کند، واشنگتن به کانادا توهین می‌کند و به‌دلیل دود ناشی از آتش‌سوزی‌های جنگلی، آن را به مجازات تهدید می‌کند؛ پاسخ اتاوا: متوجه شدم، قربان
🔹
در همین حال، اتاوا برای جلب رضایت واشنگتن، در جنگ غیرقانونی و انتخابیِ تحت رهبری آمریکا علیه ایران مشارکت می‌کند، پاداشش چیست؟
🔹
اینجا شب هاکی در کانادا نیست؛ اینجا تیم مزرعه‌ای واشنگتن است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/681759" target="_blank">📅 21:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681758">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بسم الله الرحمن الرحیم
یک مجموعه بزرگ فرهنگی و پذیرایی خوشنام درشهرمقدس مشهد و نزدیکی حرم مطهررضوی (محدوده چهارراه شهدا)
از افراد متدین، مومن، خوش برخورد، با ظاهری آراسته
در بازه سنی ۱۸ تا ۴۰ سال
با حقوق خوب و مبتنی بر شایستگی
(با غذا و مزایا )
به شرح زیر استخدام می نماید.
میزبان و خادم زائر در حوزه پذیرایی غذا و نوشیدنی
۴۰ نفر آقا و خانم
آشپز، کمک آشپز و پرسنل آشپزخانه ۲۰ نفر خانم و اقا
خدمات و نظافت  ۵ نفر خانم و اقا
صندوقدار حرفه ای ۴ نفر
از متقاضیان و واجدین شرایط دعوت می گردد حداکثر تا ساعت ۱۸ روز سه شنبه ۲۷ مرداد ماه ۱۴۰۵ رزومه عکس دار و مشخصات خود را به بله ، روبیکا یا  ایتای  شماره ی زیر ارسال نمایند.
📱
09120880710</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/681758" target="_blank">📅 21:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681757">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197ac01bef.mp4?token=j8ckyse4xQWPTf1pzbfbV-p2b0-RYpIi0tEUp843_JQnljkFiZw50AgRFGEuRwUMNCFlIeYKI2RESfaRlwdg2863Mo03RXjg6b0qdUHjOJUMoTZPPYwzCU9FZ_2YDWLtPtwr7PO8DuFx2JhAjFLYaRzG-J9IoVDNstkXzmEzvJH4OeZjiK9AtLCeL1ZMnQtKbk9eOMIt7ZkMLS8-b6BCGWkf1crXHCGry2KM15JBKwbM7bsJA0QrFW51wP63IEvSoJ081rcvGg21ytSmdgQ9Q5_pxeKKrFm_XG_On3HHp5hCw8YMAwb-LdsgDwFWn-zZvttc4OvSA9Sw9YW4EtXEojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197ac01bef.mp4?token=j8ckyse4xQWPTf1pzbfbV-p2b0-RYpIi0tEUp843_JQnljkFiZw50AgRFGEuRwUMNCFlIeYKI2RESfaRlwdg2863Mo03RXjg6b0qdUHjOJUMoTZPPYwzCU9FZ_2YDWLtPtwr7PO8DuFx2JhAjFLYaRzG-J9IoVDNstkXzmEzvJH4OeZjiK9AtLCeL1ZMnQtKbk9eOMIt7ZkMLS8-b6BCGWkf1crXHCGry2KM15JBKwbM7bsJA0QrFW51wP63IEvSoJ081rcvGg21ytSmdgQ9Q5_pxeKKrFm_XG_On3HHp5hCw8YMAwb-LdsgDwFWn-zZvttc4OvSA9Sw9YW4EtXEojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دلیل کناره‌گیری سخنگوی کاخ‌سفید را اعلام کرد
🔹
ترامپ در گفت‌وگویی با یک خبرنگار گفت که وی دریافت که کارولین لویت فرزندانش را بیشتر از ترامپ دوست دارد و این موضوع او را بسیار نگران کرده بود.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/681757" target="_blank">📅 21:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681756">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
راز عروج دو دختر نوجوان در تجربه‌ای میان زمین و آسمان
🔹
00:06:50 وسعت نگاه روح هنگام خارج شدن از جسم
🔹
00:16:00 پخش نور شاخه‌ای از آسمان بر مقبره شهدا
🔹
00:20:50 حضور ۴ فرشته با بال‌های نورانی
🔹
00:25:30 رؤیت شخصی با شکاف بر فرق سر و انگشتر زیبا بر دست
🔹
00:35:15 تأکید به آموختن مسائل دینی و ایمان به عالم غیب، قبل از دوران بلوغ
🔹
00:52:30 رد شدن دست از بطری آب و عدم توانایی برداشتن آن
🔹
01:02:20 ترسیدن از نگاه سلولی بر هیبت پدر
🔹
قسمت سی‌ودوم (روح و ریحان)، فصل پنجم
🔹
#تجربه‌گر
: رضوانه عرب نظرگاه/ ریحانه رشیدی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/681756" target="_blank">📅 21:01 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681755">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdfa90b88f.mp4?token=hjYSCnW7WL_xXWljKMAUsce-9qRvvEdI0tLIzFTxqOuAgS0LGgXs7dLjeHGMea5d4UeP3_qJMfEZk5Lx1AzkLxXaCAKF1FEEDznRvgNryIn2acn-sUtQJ_VOd7YbAIk-fnsihVHC6BxaOfdPE_LiWdOZoPB2SvMt12EIOUgFKq9EPB28RUHNs4Otx3LJc2GSNTb4ByTFzq21iHFl484BCK6VYvlOK3YxloN31AK6TnlWAffuSbCTVKDpcTM4TDiI_v_4XB8WzfLqPhcuI2G3ZG-d4Z7ZfDWbR5026MTsGCvyQr0TaT7EvssaC0SNBTlIknO8bJLMFIqSj81-FFRoUajUzN_Gzom8XTowrMwaAKAjeAyucMAnsh97E63LuozP4aYxJGdiAnPkc3kl0WzS8q3ePBaPmZ2CIvRLkswLbs9Ji-U3oPveMS_3-cSkLRd3Xqvvp3epOGJUToExPX93bcxntqF10mmG0SWEsysrRmYE40BnMagDDYc_4Oh-mWKUfvssMSlq-rEgGmLc8gAGo09SjlamYhU4f4gElF09euLW7U1mw6W_R1ytlYmgduqSw7crdz03UjCm9LVoNB7-xrfuWTpXsUbXRVgT_Klhs9yDxSF1x4OqAg0QnGYa5CMMgbSja2df-k31J8nZ9h1W27eBF3hccN9c43GmBJBIAmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdfa90b88f.mp4?token=hjYSCnW7WL_xXWljKMAUsce-9qRvvEdI0tLIzFTxqOuAgS0LGgXs7dLjeHGMea5d4UeP3_qJMfEZk5Lx1AzkLxXaCAKF1FEEDznRvgNryIn2acn-sUtQJ_VOd7YbAIk-fnsihVHC6BxaOfdPE_LiWdOZoPB2SvMt12EIOUgFKq9EPB28RUHNs4Otx3LJc2GSNTb4ByTFzq21iHFl484BCK6VYvlOK3YxloN31AK6TnlWAffuSbCTVKDpcTM4TDiI_v_4XB8WzfLqPhcuI2G3ZG-d4Z7ZfDWbR5026MTsGCvyQr0TaT7EvssaC0SNBTlIknO8bJLMFIqSj81-FFRoUajUzN_Gzom8XTowrMwaAKAjeAyucMAnsh97E63LuozP4aYxJGdiAnPkc3kl0WzS8q3ePBaPmZ2CIvRLkswLbs9Ji-U3oPveMS_3-cSkLRd3Xqvvp3epOGJUToExPX93bcxntqF10mmG0SWEsysrRmYE40BnMagDDYc_4Oh-mWKUfvssMSlq-rEgGmLc8gAGo09SjlamYhU4f4gElF09euLW7U1mw6W_R1ytlYmgduqSw7crdz03UjCm9LVoNB7-xrfuWTpXsUbXRVgT_Klhs9yDxSF1x4OqAg0QnGYa5CMMgbSja2df-k31J8nZ9h1W27eBF3hccN9c43GmBJBIAmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات خاص و پر از احساس بوسیدن دست مادرها در استودیو برنامه محفل ستاره‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/681755" target="_blank">📅 20:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681753">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d3798d25.mp4?token=t4CR8yyDjGHyp9dOZBl26k8vnSId0Oms6dq-933mWb2We8MIgJpr50X1zJ7SQNGNUlqj32ThKL7dCam91kQdR2iP0kVZamqYOaOvB7VtUobLZHCy6EsKrRG5vWsVwtIBoW2GMOa2Ym3D4zZGcBeSiORV7HV-GeOqVhYVMDRJ6z__mExGL8COl7UjfMiHrStYrPW9R6Qmnjos974Jb8qdzh2E04xAYXxxsMHahIlTk23Oud4YsLqDd-c681IiEYdPD7BjjwObSkhWki2p1wVmao5ptyMsavSis8ZM6Lb4SIKeppPkIxCGMT_zDJWrsIVknt_dMTukG7uIOUFrS7Oitg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d3798d25.mp4?token=t4CR8yyDjGHyp9dOZBl26k8vnSId0Oms6dq-933mWb2We8MIgJpr50X1zJ7SQNGNUlqj32ThKL7dCam91kQdR2iP0kVZamqYOaOvB7VtUobLZHCy6EsKrRG5vWsVwtIBoW2GMOa2Ym3D4zZGcBeSiORV7HV-GeOqVhYVMDRJ6z__mExGL8COl7UjfMiHrStYrPW9R6Qmnjos974Jb8qdzh2E04xAYXxxsMHahIlTk23Oud4YsLqDd-c681IiEYdPD7BjjwObSkhWki2p1wVmao5ptyMsavSis8ZM6Lb4SIKeppPkIxCGMT_zDJWrsIVknt_dMTukG7uIOUFrS7Oitg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار نوستالژیک چند نام ماندگار؛ وقتی خسرو شکیبایی، بهروز وثوقی هم‌نشین شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/681753" target="_blank">📅 20:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681751">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d6a33f311.mp4?token=EDkHd9SVML2byHJCwU9iquwB1H6AxeOQYxFwQklD8rnkZRUHANU_KToVjaCb7NPyVgOVFqrUHE6yG6GSZjI-BheZkyxIhwd02FrJSFf-tDGSyjtI6UYa2Xmh2V2Exd-3ebfzmutDOFIldRIvYvPoaemJaJUknb6p3btm5l1XdW1VuG8y_5izxlCzaX0RsnMRk-TZD-HxlitVnzPQzJCcF6mYv28fKCPz1bZb41OUSfBNsiTccteneW8JDXhRlgOjxI8P3Px1LA-SJczOu4N9pttgidszlwYI4cBlco51yt91PoM0Kjuto_bk0xC6oXIPa6gOSvuzIxXZnfEQAF9dmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d6a33f311.mp4?token=EDkHd9SVML2byHJCwU9iquwB1H6AxeOQYxFwQklD8rnkZRUHANU_KToVjaCb7NPyVgOVFqrUHE6yG6GSZjI-BheZkyxIhwd02FrJSFf-tDGSyjtI6UYa2Xmh2V2Exd-3ebfzmutDOFIldRIvYvPoaemJaJUknb6p3btm5l1XdW1VuG8y_5izxlCzaX0RsnMRk-TZD-HxlitVnzPQzJCcF6mYv28fKCPz1bZb41OUSfBNsiTccteneW8JDXhRlgOjxI8P3Px1LA-SJczOu4N9pttgidszlwYI4cBlco51yt91PoM0Kjuto_bk0xC6oXIPa6gOSvuzIxXZnfEQAF9dmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس پدافند هوایی سپاه: در روزهای اول جنگ ۶ تا ۷ پهپاد هرمس و هرون رژیم صهیونیستی همزمان بر فراز جنوب لبنان گشت‌زنی می‌کردند
🔹
با هدف‌قرارگرفتن این پهپادها در ایران، تعدادشان در جنوب لبنان به یک فروند رسید و حزب‌الله آزادی عمل بیشتری برای عملیات پیدا…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/681751" target="_blank">📅 20:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681750">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
لس‌آنجلس‌تایمز: رویکرد خفه کردن اقتصاد ایران توسط وزیر خزانه‌داری آمریکا رهبری می‌شود
ادعای لس‌آنجلس‌تایمز:
🔹
با نزدیک شدن به شش ماه جنگ با ایران پس از پیش‌بینی یک کمپین شش هفته‌ای ترامپ، گزینه‌های کمی برای پایان دادن به این درگیری دارد.
🔹
رویکرد فعلی، یعنی خفه کردن اقتصادی ایران، توسط اسکات بسنت، وزیر خزانه‌داری، رهبری می‌شود که در بررسی‌های پیش از جنگ ترامپ نقشی نداشت. گزینه‌ها عبارتند از تشدید نظامی، پذیرش پیروزی ایران از طریق یک مذاکره ساختگی و ادامه فشار اقتصادی./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/681750" target="_blank">📅 20:21 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681749">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ggniwys4WWKrz3RsRzaQfSLRkF0sSJoww0q0LBIuaEno2v_EK40G1vSffAsVnMpOfq44tf-bXkqFfSIkjkgZiqn8rcgy2S3Yb07xt8csRRAU3CnyPizgBIKdMfnFtfe3vOHF0MWxxQzbHljYT6J5Kk7n5edN4c9NQw1YkzLo4XKSiLtug-tFXPR4BJGQXaXjNTH8YwMZRPkfgc3GGn07OqmrOZGa0HBcyIr6XUMpMuTrUUbysjxL9nBpzHyO42jpfy57XGc9tQVTQhHKsYZG8uX1tp84NF3UaUzl8hqOuEJcpMVpqcxvRzVTcSLsgB0M3UZvvRqe_bKNubBWRzh8xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«به وقت ایران» همچنان پربیننده است/ محصول سازمان اوج در صدر مخاطبان تلویزیون
🔹
بر اساس آمار مرکز متا، «به وقت ایران» با ۲۰.۵ درصد مخاطب در تیرماه در صدر پنج برنامه پرمخاطب تلویزیون قرار گرفته است. این برنامه در آمار مرکز تحقیقات صداوسیما نیز ۲۴.۵ درصد مخاطب داشته و در تلوبیون، در روز ۳۰ تیرماه، به ۱۳ میلیون بازدید رسیده است.
🔹
«حسینیه معلی» با ۱۹ درصد، «جام ۲۶» با ۱۸ درصد و «پدر امت» و «سمت خدا» هرکدام با ۱۷ درصد در رتبه‌های بعدی قرار گرفته‌اند.
🔹
در کنار این آمار، یکی از نکات قابل توجه درباره موفقیت «به وقت ایران»، این است که این برنامه از تولیدات خارج از سازمان صداوسیما است و به همت سازمان هنری رسانه‌ای اوج تولید شده است./ فرهیختگان</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/681749" target="_blank">📅 20:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681740">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MR1RVyzGc9EMiSR0l2T35Eagl1QiOgrKyqQ4SsG4z7uGnfysZ1XnfcBEsaV48YvWO7oS0HxiUWAWUms-gVZdLYxGpZQFkhg2k5Vz5zUGL75965s1HwSgC0399GsSgVVaz0Y3ETnKzlYAh9NStoMMPPfrWY7seggDN4Fn8HfLxEYr-vKdaU1S3jJtafGKAYN5iSSw9mMrEjS8Tlnj11WkOQoXWTzjAytwGibVkv9TW2UVfomViqiKn1KWx2bO-3Giv1eNkc8KnrquyvYSmJaPEooq9nNPdjGCcCJb3BGX7ZCn4eqhXggWMBTj22KWAwdNb_IS7D48rFgcFpVONkkR1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfFWjSH9SJbWAoAP-aqSLYVADtSO1GwfUL42mFGlnF27HqXoP-GLRsg4jMQRHX153pe6TprEsZFnynnF8Vtf0ollonVxfUdCY_YR4TXOn0MljikcnCilKGwpNqvELT6OKs0MvF0yJ--abYPGauTO0BmT87EiuMtXI0HQkEknmU_LcGNWdhnjI9DW012aD_0LrGlZ6KREzIhs0Qxo2CjkpDIoeVwf9HvZHAsDchrg3Gu7lKWD0fyyjwOwTVQ3agWfB-cFSH9ctqT10AEyIIG_1BfXpEsiSLSuvl0-ugeeePd9FEZEzFjOGC8bpC2kI1nB_O2FUutz8m78nU2XKXLXFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کشورهایی که بیشترین فرصت‌های فریلنسری را ایجاد می‌کنند
🔸
آمریکا با اختصاص ۳۶.۸ درصد از سهم بازار، بزرگ‌ترین ایجادکننده فرصت‌های شغلی برای فریلنسرهاست و پس از آن بریتانیا، کانادا، استرالیا و آلمان قرار دارند.
🔸
اکثریت قاطع فریلنسرهای آنلاین در سراسر جهان را جوانان زیر ۳۰ سال تشکیل می‌دهند و «توسعه نرم‌افزار و فناوری» و «خدمات حرفه‌ای» اصلی‌ترین حوزه‌های فعالیت فریلنسرها جهان هستند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/681740" target="_blank">📅 20:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681739">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BU5bKugYiUHpl3muy4wSVhAtDPxBKGdjZvRY0EE6Oj5pHfHiUo4XjyUzyJpU8aJBYWlpJ01JGyW_52AO6rHE1yRxO4QPH6fkmtzg1adKDqhDdL_7KdEOKth9kBo2-MjyMs3aI7v5u9M9oFLwHVCiGJyMpUx7g8HyqGIOj2dS_da08LjgSApe0m4xyzVLB_R_xFuqnaEgA7pff0hMtg1P3yL9U31Uch1gfMfz59WjdNuOvl8qNGe0FGoM2ToRtZzG5m53zWr9c-4tz0_bQX5ZDKXWDdWXMosftxKaAmRxeZOw_c9kgJv5FpiJag8141Wb6_puUG-IF9Up3oJNBeIcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غذات شور، ترش یا بیش از حد تند شده؟ هنوز برای نجات طعمش دیر نیست؛ با چند ترفند ساده، تعادل را به غذا برگردون
👌
🍲
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/681739" target="_blank">📅 20:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681738">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkGyb8Jk-qogAyYOOC3xn6xxGYoFCx4UheRwnZ3vPGrsqUMF39kilTkTbZi01UEQ8aOBjf3LnOFshayn6qQKraHQKZgVcjyzxePlE0H6YP91Hw3mVXRs0ChgyiKCnsSPfdIbXg4MRqsuorV_3c8wRQfqpllwX-0y6_ocr4eqeEb8je7GF6R837aW3QRvM4Otl0JIp4caG8iguvar1Y2cKqcr1Youj2y_Bfp3eIaHZjHwGzv1cMjSxgXP557O11Rxr40d8pMKr68jKaReGdlvlWIUhK7DH1a6yQf3bbI1o3Wa4qf6Sq9GxWUEn3laKfccMElLxBqUSahSlWVqpkR4ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خیابان‌های اسرائیل در سایه انتخابات
🔹
بنر تبلیغاتی حزب لیکود، حزب سیاسی نتانیاهو، با تصویری از رهبر معظم انقلاب اسلامی، زهران ممدانی، رجب طیب اردوغان و شیخ نعیم قاسم و این نوشته در خیابان‌های اسرائیل مورد توجه کاربران قرار گرفته است: «آن‌ها می‌خواهند نتانیاهو شکست بخورد؛ پیروزی را به آن‌ها ندهید.»/ خبرفوری
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عبری دنبال کنید
👇
@AkhbareFori_HE</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/681738" target="_blank">📅 20:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681735">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlmfdOU60K7mpHl9KKbFvFdtL-fXYowJjoUuLPVTy2Uc8LkBM4Lz7XuDeaXp4raV4OR-5QE__ZRebZnxkknA4r7aPpIvYeW-A--iwf3QOpdWHBunuJDfZNWuIF1aK0K1hiH_3h70Wrg7DKJXjTWN1IYv3Of_kfPgav1fXjhLIVOrq0a2tJjhmJh_JWw-2x7Pjo-47c4lgMr4jlI29e2nVXEAfELEY2F32kVrDWm-ExOKOeXMXb6nCTj2tI4g-BxxxkVbQA7kL3YnKwtRBfXBeUahIx8xYRvr-i7m2v2RU6Ncwg7yWRF3RmUhJ3bpQPxA5lX6jXmB_eHIIEIZUECf2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ae368fe54.mp4?token=AIagbqTDEMBWihVPKRNXv6b1wsiN0FGRJWwyszjz_aIHuWZgmwU135-as9d3DX-3NVcj-VN6PZt4h8zV2Hjbsfd7D-_TyoRAemG3aBB3gkBkm8VjFeNMJsh7gPQGOtEfKIqX43IsvrYEsjAmEiU8n9OSNHaakEm1mqzPbCYtVsf8axIl2paTOcTYWasrD0ETG4y-1WJgwo-9kg1Hh1h-XMtljuQPxS1xB2R-BM1Iz6LnxfUZl_ex_yTe5yliTLV2CTt99G9BZAuVnih5e3yYu6MRznf01QWytXW623aebDPbgT4jB1ZOxYjNrwbP-Rtisr-zWWFth7bCIKXAAqR1UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ae368fe54.mp4?token=AIagbqTDEMBWihVPKRNXv6b1wsiN0FGRJWwyszjz_aIHuWZgmwU135-as9d3DX-3NVcj-VN6PZt4h8zV2Hjbsfd7D-_TyoRAemG3aBB3gkBkm8VjFeNMJsh7gPQGOtEfKIqX43IsvrYEsjAmEiU8n9OSNHaakEm1mqzPbCYtVsf8axIl2paTOcTYWasrD0ETG4y-1WJgwo-9kg1Hh1h-XMtljuQPxS1xB2R-BM1Iz6LnxfUZl_ex_yTe5yliTLV2CTt99G9BZAuVnih5e3yYu6MRznf01QWytXW623aebDPbgT4jB1ZOxYjNrwbP-Rtisr-zWWFth7bCIKXAAqR1UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره ای از آثار حملات یمن به تاسیسات نفتی جازان عربستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/681735" target="_blank">📅 20:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681734">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
پزشکیان: انتصابات مدیریتی باید علمی و فارغ از ملاحظات سیاسی باشد
🔹
انتخاب، ارزیابی و حتی عزل‌ونصب مدیران و اعضای هیئت‌مدیرۀ شرکت‌ها باید براساس شاخص‌های روشن، علمی و قابل سنجش انجام شود تا از شکل‌گیری هرگونه شائبه، حرف و حدیث و ملاحظات غیرکارشناسی جلوگیری شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/681734" target="_blank">📅 20:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681733">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aShMGDEj0sMHzU3TplYjCGQfXhzjnumfpe0YPFVz4dEUiAuJxz6DAgnX6CDnsbtES8J1FnXImPgGO5QnrO7g8I7HVXfEhMHUH9XtVBy6t8B9wKkQNdJbFoeQa24-8YGehstPF2-RLdKgzTVzQOwliskERRaCO9NONusAUVsqCCE3VnLW0WYtQwOaxgh6zaJV-mICWOAjIhpltktbWc4l_dldGJL5X71AeO59Li8VxJJIu3SZONjkgdn-5cao3qxHTuqz7JYJna8BhrlaJ4K5QO9202yfJqB6OWbl9Ux-k1NDhUbZYvlsfLc-mrV2QBYeH1WxI1QsEl5qK7ZU0kB7LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصمیم ملی
🔹
مسئله بنزین دیگر با تصمیم‌های مقطعی و ملاحظات کوتاه‌مدت حل نمی‌شود و به یک اجماع و تصمیم ملی نیاز دارد. هر تصمیمی که گرفته می‌شود، نباید بار آن ناعادلانه بر دوش مردم باشد. اصلاح قیمت، اگر ضرورت دارد، باید همزمان با اصلاحات اساسی در نظام مصرف و تولید سوخت انجام شود. خودروسازی ناکارآمد، خودروهای پرمصرف، ناوگان فرسوده و سیاست‌های نادرست، سهم بزرگی در افزایش مصرف دارند و باید اصلاح شوند. همچنین لازم است توزیع یارانه سوخت شفاف‌تر و عادلانه‌تر شود. مردم با یک تصمیم سخت همراه می‌شوند، اگر ببینند همه در هزینه و مسئولیت اصلاح شریک‌اند. بنزین نیازمند تصمیمی ملی است، تصمیمی همراه با انصاف، شفافیت و اصلاح واقعی.
🔹
هشتصدوسی‌‌وپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/681733" target="_blank">📅 19:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681724">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tO1G7LA46oLlBGR-l47h8vNB4sVXZnPGEryFwX8de8FaPRzbEiH8i55wRoQIwP4bjErg7LV8n7qC7B5265onjmADcX7p09vjmJqUdr8YdQJHY3lyOvgURKXMfB3yqG5KSsmmdYv5KwLxp8EuJNkCAxr2462qDu785mA56gJdfR3-P51DkBipyyzNAqzVIWDaTOculcBIEUts077E411pQdahPbp-FpxUkB8q0KL7-p-zk2RHE-SwSlxwU4LUoCWvBCAJfNo2NZF3wqsyiP_SGLuF2CbLNcESU_gnKxvQk6sKmX3l7gw1a4OH1dbaJHcD5LDvgk2D01teT5KoAHUJIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصوّبات مجلس براساس نیازهای مردم و معطوف به امیدآفرینی و آینده‌سازی کشور باشد
🔹
لازم است مصوّبات مجلس با مسائل اصلی کشور و نیازهای مردم نسبتی مستقیم و مشهود داشته باشد و معطوف به امیدآفرینی و آینده‌سازی کشور باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/681724" target="_blank">📅 19:37 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681723">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/920a41a2ca.mp4?token=jGhRtFubjZjaRZ1Jb80ibmJZq9LxV13YXI12mZmI8SXYeLLNJFy_-vCnnI0W0KPxTSOcdoeVqUbg3QGGG3LAmeA4AWkcEykzIa9xKE4s-NoB5mkV7YnQt_QxICIn2oPkKwzEzLTh2ba1ti9_jHDTbJSfGzkh7QNYPQbZ-M9Txf1DtB2ihhQJWr2P6OGl3JkzFH39gdl4s9ehipD--6CTCtzDdGh7Bhg7jyN7h_iw3sz3LtcNZVcJEevkh0tD2tE7IrUVuTj37TwEI8Ir1TjlZxxmR6valngYA9TkxEYvXCaoS_EZrBT-EqHWdYzAQUJJxFoGUwmnX-LkL8Gj2t8kUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/920a41a2ca.mp4?token=jGhRtFubjZjaRZ1Jb80ibmJZq9LxV13YXI12mZmI8SXYeLLNJFy_-vCnnI0W0KPxTSOcdoeVqUbg3QGGG3LAmeA4AWkcEykzIa9xKE4s-NoB5mkV7YnQt_QxICIn2oPkKwzEzLTh2ba1ti9_jHDTbJSfGzkh7QNYPQbZ-M9Txf1DtB2ihhQJWr2P6OGl3JkzFH39gdl4s9ehipD--6CTCtzDdGh7Bhg7jyN7h_iw3sz3LtcNZVcJEevkh0tD2tE7IrUVuTj37TwEI8Ir1TjlZxxmR6valngYA9TkxEYvXCaoS_EZrBT-EqHWdYzAQUJJxFoGUwmnX-LkL8Gj2t8kUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بلاگری که به مقدسات توهین کرده بود  دستگیر شد
🔹
در پی انتشار ویدیویی توهین‌آمیز در فضای مجازی از سوی یک زن بلاگر، با دستور مقام قضایی متهم شناسایی و دستگیر شد.
🔹
برای این فرد پروندۀ قضایی تشکیل شده و درحال رسیدگی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/681723" target="_blank">📅 19:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681722">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
کالابرگ مردادماه برای ۳ گروه حذف شد
🔹
از مردادماه زمان شارژ کالابرگ تغییر کرده؛ گروه اول پانزدهم، گروه دوم بیست‌وپنجم و گروه سوم پنجم ماه بعد می‌توانند از یارانه غیرنقدی استفاده کنند.
🔹
در نتیجه، سرپرستان خانواری با رقم پایانی کد ملی ۷، ۸ و ۹ کالابرگ مردادماه را دریافت نمی‌کنند./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/681722" target="_blank">📅 19:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681721">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رکود شدید بازار لوازم خانگی؛ مردم به جای خریدن تعمیر می‌‌کنند!
اکبر پازوکی، رئیس اتحادیه فروشندگان لوازم خانگی در
#گفتگو
با خبرفوری:
🔹
افزایش قیمت کالا، کاهش قدرت خرید مردم و شرایط اقتصادی باعث شده بازار لوازم خانگی با رکود شدیدی مواجه شود و مردم به جای خرید کالای جدید، بیشتر به سمت تعمیر وسایل خود بروند.
🔹
فروش مستقیم کالا توسط تولیدکنندگان و کارخانه‌ها در فضای مجازی و همچنین گسترش فروش اقساطی توسط فروشگاه‌های بزرگ، سهم کسبه را در بازار کاهش داده و فعالیت واحدهای صنفی را دشوار کرده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/681721" target="_blank">📅 19:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681720">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c80afa8283.mp4?token=OcM_4FKqZvPy0HmwSUhnDIMOQkfHYgekO1tv02T3-5d01AVXWCFXtwvpexPdyhwVAwfK-rR5goFM-zAbn0K9356vAaAMbNjtonLEEFvtU0Xf_0Mpdqnq4qaoXIFgLkJz4fVHRj3OmBZC_JkiMyVup1oqY43Og0wWJZaUO76EuDPQKmlL9ExwqyMfMx-C4JmvJFb78ggY8L-ANrqFZovkdgNXGrqjR6_ZcX0XobwQfaLFtzYvtpEqmnjMrWiF_cmHwFa9ud6oCD7nDSD9bZcah52Ui4MYkjlltKqpNYamzD1X-e9ZSCwyDshOSKpSWrq5V9dC-IwStzuw71DMMwWmXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c80afa8283.mp4?token=OcM_4FKqZvPy0HmwSUhnDIMOQkfHYgekO1tv02T3-5d01AVXWCFXtwvpexPdyhwVAwfK-rR5goFM-zAbn0K9356vAaAMbNjtonLEEFvtU0Xf_0Mpdqnq4qaoXIFgLkJz4fVHRj3OmBZC_JkiMyVup1oqY43Og0wWJZaUO76EuDPQKmlL9ExwqyMfMx-C4JmvJFb78ggY8L-ANrqFZovkdgNXGrqjR6_ZcX0XobwQfaLFtzYvtpEqmnjMrWiF_cmHwFa9ud6oCD7nDSD9bZcah52Ui4MYkjlltKqpNYamzD1X-e9ZSCwyDshOSKpSWrq5V9dC-IwStzuw71DMMwWmXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران؛ دلبر سه‌رنگ من
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/681720" target="_blank">📅 19:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681717">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-ml31d9E7wSy0jR4x3tnl-HtTIpcg1nSN4GedpTr7ZJYr9xo1e9gt4ZCBFbPiHYPvNygCoob1zJUHyYO-fL7j9h9T9LSwrQUMVaGGCiU0IQbIzmcixLf0iPRPF5gLqi2q_tfuhF2C5m39kJDXkM-91e_V97VO-EZFdjg8sCcq7MnEnIo-pbCyc3lUaWXdfxnY2sZfemBjCk2TbBO4JZj7lgJqUNLYN3MZ3l-NO-NTeo9odZaFOlz8rCDaL1WTHkqbCLETvSSJouufLBuQA3hOLD0QOhZk4XgufD0P0wOWqIkWQBzeYCFUEyRC8AQwtabeneSx9THGNDuOhr2gIeHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
همراهان گرامی؛ اگر با کمترین بودجه، کسب‌وکاری را در منزل راه‌اندازی کرده‌اید، روایتگر مسیر خود باشید.
🔸
یک پیام صوتی حداکثر ۳۰ ثانیه‌ای شامل نام، شهر، نحوه شروع و نتیجه کسب‌وکارتان، به همراه عکس کسب‌وکار برای ما ارسال کنید.
🔸
روایت شما می‌تواند الهام‌بخش کسانی باشد که می‌خواهند از صفر شروع کنند؛ بهترین ایده‌ها و محصولات نیز فرصت معرفی و تبلیغ در خبرفوری و کانال‌های زیرمجموعه آن را خواهند داشت.
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/681717" target="_blank">📅 19:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681715">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bi2yoe8SCxwFKh7sE08GSoOicvwB4NHVLQTfguHK-VqlTpXSTAwi2Dhu9wqdmnlY7FcMqQH-Z0V20MKfTtQVpyG66nYwP8aWTsozpR-LO2jGnulSz0e1Xk8yHRNTBYaf6N-YvHL6hiGQ-PqzAp87FgHEc8YUAgD8nmcK34-ABjHPF8OtaAQnryZraKICTO6whBB8TDNu91DbhR8FoTtPNM8uUQyJrPXGgGnFftopJV_LKvqw8rwBsOYdfLTtA1-LYw6o9h5Dydr4H8v74bFyS8AnJnEMogkaVqPTuGJdMmhEIAofw-msk5khIABtUw7SEUowTZeUXsAz3mkIi2LyAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاعری که نامش با نوگرایی، طبیعت و دگرگونی شعر فارسی درآمیخته است؛ نیما یوشیج
🔹
نیما یوشیج، از برجسته‌ترین شاعران معاصر ایران، تنها یک شاعر نبود؛ او آغازگر جریانی تازه در ادبیات فارسی شد و با شکستن قالب‌های سنتی، راهی نو برای بیان احساس، اندیشه و تجربه‌های…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/681715" target="_blank">📅 19:08 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
