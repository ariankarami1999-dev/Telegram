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
<img src="https://cdn4.telesco.pe/file/TFVI06otTWwqb3qYvcO7VHKFGXtD7EtWSsg1kLAwT_t7qJ2E7Y0yY1KHmMutoPd2xfgPm-JO2NOwWYZ29S05au9Atroaq4cKUa67gPkewEOSGQXdbBWMzFiJO4x8vpCOBNlCgnjE6_nzAxkP9nDCHgHcMMKJz4r7DoN15e5QI5-hUlWjJa7TaIAAmKkgrN5BosaoF-G3N6ZxmQb5aPr4j34FyR1R7KnT-6RjH--XWyi-yRx9vWIMq34MZ8gfejtnwehzeBYt7JQyqjVuTkJ-9Xn6L9_g4h73ZZiu3aYSgGuy_du34h3XEnj5zCXJdUJWog8Wn74gjAGkW7hQMv0kew.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.5K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 20:25:31</div>
<hr>

<div class="tg-post" id="msg-19372">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کاخ سفید:  رئیس‌جمهور ترامپ جلسات خود را در دفتر بیضی شکل با رئیس‌جمهور زلنسکی و نخست‌وزیر نتانیاهو به پایان رساند.  هر دو جلسه مثبت و سازنده بودند!</div>
<div class="tg-footer">👁️ 618 · <a href="https://t.me/SBoxxx/19372" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19371">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">برنامه امروز دیدارهای ترامپ در کاخ سفید</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SBoxxx/19371" target="_blank">📅 20:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19370">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">باز این پفیوزها می خواهند تندروهای داخلی را تحریک کنند تا تنگه را ببندند و قیمت نفت بالا برود و غرب از کمک بیشتر به اوکراین که خشتک روسها را بر کله شان کشیده منصرف بشود.</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SBoxxx/19370" target="_blank">📅 20:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19369">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">باز این پفیوزها می خواهند تندروهای داخلی را تحریک کنند تا تنگه را ببندند و قیمت نفت بالا برود و غرب از کمک بیشتر به اوکراین که خشتک روسها را بر کله شان کشیده منصرف بشود.</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SBoxxx/19369" target="_blank">📅 18:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19368">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">📌
چرا سهام شرکت‌های نیمه‌رسانا سقوط کرد؟ بررسی عوامل پشت پرده اصلاح بزرگ در سهام تراشه‌ها  افت سهام نیمه‌رساناها نتیجه ترکیبی از نگرانی درباره رقابت چین، ارزش‌گذاری بالای سهام و شناسایی سود پس از رشد چشمگیر صنعت هوش مصنوعی بود.  این ریزش فعلاً بیشتر به بازتنظیم…</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/19368" target="_blank">📅 18:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19367">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpY8BuP7sXgHvUy6ygpdEnvOHJhBkKFxQrENF2m-XLOyaSbMhr6bxVpwsiNmLTuYGQkzCV2qQ6P90ZApGuX8AjrPsYnLHYE28cLSYTB8TTShedyTcQCckTP6sqEdiBYSigyKKqUw5N3FaJKjhzWVKKj8gRviv8utX8Oko9xOAB8jSslLR0kXl831l3uriAHKulwQV6cMvweuOi6BVYGo9Pl5vq59x5Y1HjUGnuNBMZ1yA4dgY_XtBtGUFDegjfqaPKunSB0m-F9wbzMO9sMj4YSRDjYn32hadGHjdQ9OoTtl-X7o5ZgOny9Jhb5fCwzTLiP9GetS3VT-_tK60aNPyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا سهام شرکت‌های نیمه‌رسانا سقوط کرد؟ بررسی عوامل پشت پرده اصلاح بزرگ در سهام تراشه‌ها
افت سهام نیمه‌رساناها نتیجه ترکیبی از نگرانی درباره رقابت چین، ارزش‌گذاری بالای سهام و شناسایی سود پس از رشد چشمگیر صنعت هوش مصنوعی بود.
این ریزش فعلاً بیشتر به بازتنظیم انتظارات بازار شباهت دارد و تداوم آن به توان شرکت‌ها در اثبات سودآوری واقعی سرمایه‌گذاری‌های هوش مصنوعی بستگی دارد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SBoxxx/19367" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19366">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ادعای رسانه های روسی:
یک مقام ایرانی به ما گفت تهران قطعاً به صورت نظامی به حمله اوکراین به یک کشتی ایرانی در دریای کاسپین پاسخ خواهد داد.</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/19366" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19365">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حمله دیروز یمنی ها به مبداء خط لوله شرقی-غربی عربستان یعنی تاسیسات نفتی ابقیق انجام شده.  سعودی ها کوشیده بودند با این خط لوله وابستگی خود به صادرات از تنگه هرمز را کاهش دهند که با این تشدید تنش یمنی ها روبرو شده اند.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/19365" target="_blank">📅 14:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19364">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شما ببینید چقدر سرعت تحولات ژئوپولیتیکی بالا و تاثیرگذاری آن روی پارامترهای اقتصادی از جمله احساسات مصرف کننده و تولیدکننده بالاست که امروز موسسه ING در
تحلیل گزارش مثبت دیروز IFO آلمان
چنین نوشته:
Normally, three consecutive increases in the Ifo index points would be a reason to party, celebrating increasing optimism in German businesses and higher hopes for an economic rebound in the second half of the year. However, in this highly volatile geopolitical environment, even leading indicators have become rather outdated.
Today’s Ifo index reading probably reflects more the initial relief after the US-Iran Memorandum of Understanding than the recent surge in energy prices.
ترجمه:
به‌ طور معمول، سه افزایش متوالی در شاخص ایفو دلیلی برای جشن گرفتن است؛ چراکه نشانه‌ای از افزایش خوش‌بینی در کسب‌وکارهای آلمانی و امید به بهبود اقتصادی در نیمه دوم سال است. با این حال، در محیط ژئوپلیتیکی بسیار ناپایدار کنونی، حتی شاخص‌های پیشرو نیز تا حدودی از اعتبار افتاده‌اند.
ارقام امروز شاخص ایفو احتمالاً بیش‌تر بازتاب‌دهنده آرامش اولیه پس از تفاهم‌نامه آمریکا و ایران است تا افزایش اخیر قیمت‌های انرژی.</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/19364" target="_blank">📅 14:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19363">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">311.2 KB</div>
</div>
<a href="https://t.me/SBoxxx/19363" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 14</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SBoxxx/19363" target="_blank">📅 14:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19362">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وزیر دفاع اسرائیل:  در دور آخر درگیری‌ ها جنگنده‌ها و سوخت‌رسان‌های آمریکایی از اسرائیل پرواز می کردند اما ایران همه را زد جز ما</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/19362" target="_blank">📅 14:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19361">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وزیر دفاع اسرائیل:
در دور آخر درگیری‌ ها جنگنده‌ها و سوخت‌رسان‌های آمریکایی از اسرائیل پرواز می کردند اما ایران همه را زد جز ما</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/19361" target="_blank">📅 14:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19360">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:  ما اجازه نمی‌دهیم اردوغان سوریه را علیه ما تقویت کند. ما می‌دانیم چگونه منافع اسرائیل را دفاع کنیم.  در حال حاضر هیچ درگیری نظامی مستقیم بین اسرائیل و ترکیه وجود ندارد و ما تمایلی به ورود به چنین درگیری‌ای نداریم.  اما اردوغان…</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/19360" target="_blank">📅 13:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19359">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزیر انرژی اسرائیل، الی کوهن: ما دخالت‌های ترکیه در سوریه را نخواهیم پذیرفت.
🔹
اگر ترکیه پایگاه‌هایی در سوریه ایجاد کند، ما نیز اقدام خواهیم کرد تا پایگاه‌هایی را در داخل خود سوریه ایجاد کنیم</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SBoxxx/19359" target="_blank">📅 13:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19358">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وزیر امور دیاسپورای اسرائیل، آمیخای چیکلی:  «ترکیه اردوغان و سوریه الشرع اکنون بسیار نگران‌کننده‌تر از ایران هستند.  دوران امپراتوری شیعه ایران به پایان رسیده است. محور جدید، محور اخوان المسلمین ترکیه، سوریه و قطر است».</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SBoxxx/19358" target="_blank">📅 13:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19357">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وزیر انرژی اسرائیل، الی کوهن: ما دخالت‌های ترکیه در سوریه را نخواهیم پذیرفت.
🔹
اگر ترکیه پایگاه‌هایی در سوریه ایجاد کند، ما نیز اقدام خواهیم کرد تا پایگاه‌هایی را در داخل خود سوریه ایجاد کنیم</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/19357" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19356">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 14</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19356" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 14
سه شنبه 28 جولای 2026</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/19356" target="_blank">📅 12:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19355">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">برنامه امروز دیدارهای ترامپ در کاخ سفید</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/19355" target="_blank">📅 12:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19354">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رویترز: در پیشنهاد عمان، تهران کنترل انحصاری تنگه هرمز را در اختیار نخواهد داشت
خبرگزاری رویترز به نقل از یک منبع آگاه گزارش داد عمان پیشنهادی را به جمهوری اسلامی ارائه کرده است که بر اساس آن، سازوکاری مشترک میان کشورهای منطقه برای مدیریت تنگه هرمز، با دریافت کارمزدهای داوطلبانه، ایجاد شود. بر پایه این پیشنهاد، جمهوری اسلامی کنترل انحصاری این آبراه راهبردی را در اختیار نخواهد داشت.
پیشنهاد عمان از حمایت کشورهای منطقه برخوردار است و بر اساس الگوی تنگه مالاکا تدوین شده است؛ الگویی که در آن استفاده‌کنندگان از آبراه به صورت داوطلبانه در تامین هزینه‌های ناوبری، حفاظت از محیط زیست و عملیات جست‌وجو و نجات مشارکت مالی می‌کنند.</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SBoxxx/19354" target="_blank">📅 12:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19353">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUJNmeYMvQD1yV4KOZ4EGkWuYTI8dpL5duUD-jQeyUf_6v1tfJPsLfpMsYdhPYs-hpfky0zoFojBWwL6E5pLBi-U5hmEnwnCewukwGPxZJY07dWzxZpawigsAke3zLXaDfttOSgIpoqUe2W-iKFcxJkiYNGpmx6I84RHzovkPpihO_T-88Qk6-nS6ZipwdT3fj8zgy-pblkEYs1mkbxIRq15oEubCfqyNsdRp95A-W-VOLMLvc56sJmaTZ5WhDMzB3o3LftFRMnzz8rRQtqcnVWWZkjHGdJz3mY36m26dDBk0iLqsLftOSzUxx1hlZwtLha9C-rcMOXYm0nye5yjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخریب تأسیسات گاز پارس جنوبی عمق بحران ناترازی انرژی در ایران را چند برابر کرده است!
خروج ناگهانی ۲۳۰ میلیون متر مکعب از ظرفیت تولید روزانه گاز، شوک شدیدی به رگ‌های حیاتی اقتصاد و رفاه عمومی وارد آورده است. این رخداد، ناترازی مزمن گاز را از یک چالش مدیریتی و ساختاری به یک بحران ملی و اضطراری تبدیل کرده و پیامدهای این ویرانی به سرعت در دو جبهه حیاتی خود را نشان خواهدداد: سفره و آسایش مردم در بخش گاز شهری، و شریان‌های اقتصادی در بخش صنایع سنگین مانند فولاد.
سقوط مصرف در بخش گاز شهری
گاز شهری خط قرمز دولت‌ها برای حفظ رضایت عمومی است. با این حال، کسر بخش بزرگی از تولید، پایداری شبکه توزیع را در شهرهای بزرگ و مناطق سردسیر به لرزه درآورده است. افت فشار شدید در شبکه‌های خانگی، قطع پراکنده گاز در نقاط انتهایی شبکه و لزوم جیره‌بندی پنهان انرژی، نخستین پیامدهای ملموس این بحران هستند.
دولت برای جلوگیری از خاموشی مطلق خانه‌ها، مجبور به کاهش ارسال گاز به نیروگاه‌ها خواهدشد. این تغییر مسیر، نیروگاه‌ها را به سمت سوزاندن مازوت و گازوئیل سوق می‌دهد. نتیجه این زنجیره، تشدید آلودگی هوا در کلان‌شهرها و به خطر افتادن سلامت عمومی است. به عبارتی، شهروندان هزینه این تخریب را یا با سرمای خانه‌ها یا با استنشاق هوای آلوده و یا هر دو پرداخت می‌کنند.
فلج شدن صنعت فولاد و زنجیره‌های تولید
بخش عمده‌ای از بار سنگین این کسری به دوش بخش مولد اقتصاد، به‌ویژه صنعت فولاد، افتاده است. تولید فولاد در ایران به شدت وابسته به فرآیند احیای مستقیم و مصرف گاز طبیعی به عنوان ماده اولیه و سوخت است. قطع یا محدودیت شدید گاز صنایع به معنای توقف کوره‌ها و کاهش چشمگیر حجم تولید است.
کاهش درآمد و صادرات
افت تولید فولاد، ارزآوری کشور را کاهش داده و ارز غیرنفتی را محدود می‌کند.
کاهش سود کارخانه‌ه:
توقف خطوط تولید، هزینه‌های ثابت را بالا برده و سودآوری شرکت‌های بورسی را کاهش می‌دهد.
بحران در صنایع وابسته
کمبود فولاد خام، صنایع خودروسازی، ساختمان‌سازی و لوازم خانگی را نیز با جهش قیمت مواجه می‌کند.
سرایت بحران به سیمان و پتروشیمی
علاوه بر فولاد، صنایع سیمان و پتروشیمی نیز در صف نخست آسیب قرار دارند. پتروشیمی‌ها که گاز را به عنوان خوراک مصرف می‌کنند، با توقف تولید و فسخ قراردادهای صادراتی روبرو شده‌اند. کارخانه‌های سیمان نیز با قطع گاز به سمت مازوت‌سوزی رفته‌ و خواهندرفت که هزینه‌های حمل‌ونقل و تولید آن‌ها را به شدت افزایش داده و قیمت نهایی ساخت‌وساز را بالا می‌برد.
نتیجه‌گیری
تخریب‌های ناشی از جنگ، ساختار آسیب‌پذیر انرژی ایران را با چالشی بی‌سابقه روبرو کرده است. جبران ۱۰۰ میلیون متر مکعب از این ظرفیت در ماه‌های آینده، تنها یک مُسکن موقت است. تا زمانی که زیرساخت‌ها به طور کامل بازسازی نشوند و سرمایه‌گذاری کلان در بهینه‌سازی مصرف رخ ندهد، ناترازی گاز مانند سایه‌ای سنگین بر سر رفاه خانگی و رشد صنعتی کشور باقی خواهد ماند.</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/SBoxxx/19353" target="_blank">📅 12:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19352">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axaQlMJBv6sJG0hcIXbRd1E5Nme04Fhyi_zptcWkSoxquFcp4jUS6hBpS0OIFCXsQZnr-puoxhxLajODHTc6VEzzCN9VKexHVDZxx_v-7lvNqZ88FSOTZH5n9mhwQWf7-WhenuLTDpm5vj6vkIiHsVS7NyFzQ6EEOKaMn9xYqLFyJN8kgVns21K7VgK6tcg0G62487_sLKlLnEvjTtjVNsWU4sBIPRdcwnD4yKNwLi8Ipb4ed-fEn0wwXXYMFBIMS7dhM4Hpe3UcCvr6sA1u4JDGCvjmy9saNOK9oZjszWr8HVqdZkK5bNnAWbGywUgf8ynvyWEYDUfSNPitBMiMtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز سطح شاخص ریسک ژئوپولیتیک افت محسوسی داشته و پیش بینی می شود که رشد خوبی در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/19352" target="_blank">📅 11:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19351">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhsmc-_UPeyrFF49IHUgUZc8svqIPDjJjZNqpLmYRwRTwu8kzZxV79QboKyvQ-I4-b2yRZLH0o34UfAbVA3DQc2S9xFXml9To7exytpNN66sr4_VAG6o8W1uDdNxFuRBIKGp7YVrF0KtX8tKhFDuZ6AnWZe0vB9SQP0_IKLW_sBxgyxJGQ_DHrJvOsCF8vCp-jAtTDzTRtF4-YzNTrB7T7x50vxmOqWlp7WE7dJvpbK_jNUGXEjindp3GSyBXEx9amlO7PWYKSKz-4Nb4KS94DkybnGNM6FkIa0dAjTDdrZPmBaKhJORneRE5rojYIMQCpNBt6qrSDkDzgWfSDn9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا زلنسکی هم به آمریکا همزمان با نتانیاهو سفر خواهدکرد تا دیدار مشترکی با ترامپ داشته باشند!</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/19351" target="_blank">📅 11:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19350">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c9893728.mp4?token=cCKFq33D-dCSAMF3u-DVrrb1OaLcwh2Os0wfkGMlaGSBsCzhBdpREfXDig4Ai-PSWU6i0f9aNW4Q2YQjQS2wUv_d5c9Bkm7ut3sNJb9kUyZfctRx1TEnGDZ8BJDJOS2VLIgoNIy_0MfXo3IRdusZ9O_PeccY1H_2imUahx2SR9vwu44Obb69z7MCHUF1-21gBWqRQbx3Xj1tW2C1ryX7L5j0dZ0y68inkjyORA_s0kKGKL-hG9WyZgHizPP_QyYdILTXcZ24iOLW-OeUYAbh2_pQE1DQiLeEF8g1Qp5S2q8pbetM-tC9IeZcw8oDGCD3TTk8ohalIFAov_eHlVcgOIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c9893728.mp4?token=cCKFq33D-dCSAMF3u-DVrrb1OaLcwh2Os0wfkGMlaGSBsCzhBdpREfXDig4Ai-PSWU6i0f9aNW4Q2YQjQS2wUv_d5c9Bkm7ut3sNJb9kUyZfctRx1TEnGDZ8BJDJOS2VLIgoNIy_0MfXo3IRdusZ9O_PeccY1H_2imUahx2SR9vwu44Obb69z7MCHUF1-21gBWqRQbx3Xj1tW2C1ryX7L5j0dZ0y68inkjyORA_s0kKGKL-hG9WyZgHizPP_QyYdILTXcZ24iOLW-OeUYAbh2_pQE1DQiLeEF8g1Qp5S2q8pbetM-tC9IeZcw8oDGCD3TTk8ohalIFAov_eHlVcgOIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسائه ادب فرج الله دباغ — اوباش فراری معروف به سروش — به ساحت استاد موسی غنی نژاد</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/19350" target="_blank">📅 11:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19349">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW3kw1xjLx8zQwl4Rqm7PATeTTtXtaNqWbSA1S3tw-eBwqEhq9LGwBbtkv_nGQD4gw37yNdKb9xtI9YFHaGoLh5Y_qQM0WPDj1i4lFQUNX5a9PCQbD2d8TfP8kt3IT9pGTLqBasNylOba8oGHUlv_gMqUQvZ9kObgngk4v6gqTEpPRrCjuylzo-hbVj3GXWTdvWmliGIadVVx2zYI3JqsOpV_iBoDfSBlIJPSGz5JtMrIa6zUzeF1BXYC6POLrs3tSmlEF4pcSerhGlKZc5QAQNrZh8aoT8kjWhOwIXOs_k23OA3TP9_Zo50VsDawKlgM8WwZqJLcmZDh2B9ulzldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسائه ادب فرج الله دباغ — اوباش فراری معروف به سروش — به ساحت استاد موسی غنی نژاد</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/19349" target="_blank">📅 11:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19348">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bv6SI8vbdI0ylvA7bSKwKsYpV_3LN4-boGLoIXAjA0AUztadjdat6HCW6qdFjKfmagmeZCYZnKY-thO1SPKMpS2yCKTPugpDhSIV5dJumtBvIqOsNGB3bc1q1GQmdjQ6WkxvUwpnLqVfOS_nAl6Pk2GKHiH2glbHQdAUK0bEwfaFiSzr1OVMir2TAfiz9dBSlfODa8S_40JWe99aYnjDhUbB4gVrCeB6MiYR0T2Q4RVnJ2n0prxfg33y5gr12NWwJyNDjsnzTl4JbSxQPSm4bFEMoSRutphK0NmngvKwc97aTjnyLrM6GSIYOxivxQOhvNCg_Yg6d9deeql4MGIPKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله دیروز یمنی ها به مبداء خط لوله شرقی-غربی عربستان یعنی تاسیسات نفتی ابقیق انجام شده.
سعودی ها کوشیده بودند با این خط لوله وابستگی خود به صادرات از تنگه هرمز را کاهش دهند که با این تشدید تنش یمنی ها روبرو شده اند.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/19348" target="_blank">📅 11:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19347">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ:
ایران می‌گوید: "لطفاً، لطفاً،  محاصره دریایی را بردارید."</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/19347" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19346">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc3554F2LmZeUm3I7noAZ9pQCnM44C0XV7XhXTKkqf-Yu7gjUOjRDv0KfZe4vP-DXI7LfLFqR8tf9qHAELWjvf9C3bAsl8BUmZZAqXGdHs5IAthwoc5wwiofDzi1D49LBe02c4jIm30ERdcziTtRPQSfRmd80iHSOy5Hto03WEWehm1BYO3bjMrWaRidS_odBlhXTNGBksLTXJAa1WI3jpfVMI_pGOM_E1Z1T8f9tZxzg7qjx5qcMQVzDdk7JCvhARrVux2q6E10Fq9pOsqH0tTwgsh3EaTYDmkaICfa984pZqsCpwf6SND1PSCKPo4ne4TGEfNmtRD7J48xhvU__A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه محموله جدیدی از موشک‌های کورنت و پرتابگرهای کنترل از راه دور به یگان‌های خط مقدم تحویل داد.
این سامانه پیش‌تر علیه تانک‌های لئوپارد و چلنجر، خودروهای زرهی بردلی، استحکامات و مراکز فرماندهی استفاده شده است. تجهیزات پرتاب جدید به خدمه اجازه می‌دهد در فاصله از پرتابگر و در پناهگاه شلیک کنند.
شرکت روستک اعلام کرد کورنت هزاران هدف را در نبرد منهدم کرده است.
موشک کورنت-ای‌ام با کلاهک سنگین با قابلیت نفوذ ۱۱۰۰ تا ۱۳۰۰ میلی‌متر زره همگن نوردیده پس از زره واکنشی، تهدیدی برای تانک‌های مدرن است. هدایت لیزری آن در برابر اختلالات الکترونیکی و نوری مقاوم است. پرتابگرهای خودکار می‌توانند اهداف را پس از قفل ردیابی کنند. برد این سامانه علیه اهداف زرهی تا ۸ کیلومتر و با موشک‌های انفجاری تا ۱۰ کیلومتر است.
تجهیزات کنترل از راه دور خطر قرارگیری خدمه در معرض آتش متقابل، توپخانه و پهپادهای اف‌پی‌وی را کاهش می‌دهد. این سامانه روی خودروها، خودروهای سبک، چهارچرخ‌ها و سکوهای رباتیک نصب می‌شود</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19346" target="_blank">📅 04:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19345">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بر اساس بیانیه فرماندهی مرکزی ایالات متحده، از زمان اعمال مجدد محاصره کشتی‌ها به بنادر ایران، دو فروند کشتی برای اطمینان از رعایت قوانین از کار افتاده، دو فروند کشتی بازرسی شده و ۱۷ فروند کشتی تغییر مسیر داده‌اند</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19345" target="_blank">📅 03:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19344">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رسانه‌های محلی گزارش می‌دهند که شماری از پهپادها، احتمالاً ساخت ایران یا تحت حمایت ایران، در اربیل عراق و مناطق اطراف آن رهگیری شده‌اند. هم‌زمان، سامانه‌های ضد راکت، توپخانه و خمپاره در اربیل فعال شده‌اند</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19344" target="_blank">📅 01:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19343">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDqqsv-UAxgFOjEW8J-OD0u7VmeyDEF2TOfrew02D8tUeNZOXUegeZ7vfVmNdnFspQeDBCI8UkvTSHQCr3e91klnWDWl6SMz08Kiqks0S15hTzjJrgBzuNlZCqHaES3SLmBkY4htfqWTVXFOFgyhXsH5gErftrdNJvXqPrg-mSO_KfRPKTjRSPr59kNJ6B5fdtKbdczQZ9DtWPU31O28TxEOKxaB4Qp6EzhX_yvAif5W_FUut8k_5A8WHtpkjVYQ479vjuIq5sBfkz8occaTkjrZURJ1H8eR1Aqja_4ZpYdDPHF3yvp2WPwFmWx-eM3sRzXBczGLoCu7GiMtZ6v6Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک بالستیک Lora در خدمت ارتش یونان!  به زودی، نیروهای مسلح یونان به موشک‌های بالستیک هدایت‌شونده دقیق لورا از اسرائیل مجهز خواهند شد. این موشک‌های بالستیک نه تنها توسط نیروی هوایی یونان بلکه توسط نیروهای زمینی این کشور در سراسر جزایر اژه و مدیترانه یونان…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19343" target="_blank">📅 00:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19342">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">عمده خاک اوکراین در برد موشکهای ایرانی قرار داد</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19342" target="_blank">📅 00:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19341">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یادداشتی خواندنی از یورونیوز درباره ایزنکوت و حزب ش.  لینک</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19341" target="_blank">📅 00:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19340">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76775f04b.mp4?token=UfNJdVf1nNrvqvOLw--9UrsrRUuO7SqvqrVySL5gX5jmf9Ne84LcdU_D3sqbTq6cJYPIENn6c67sVBHf0AZCEJf5Yo_opbw58kJRdXS9NC02k4AiNI8qjMslAGToZmAOjqxIg6XXr3dlqoyhM0uV9AXnRyzoufIuNYLyvZ7aSDvf_AAsdOKq5l-B6iRHglLf7tFZCDtQxZy2EppQ9i-q1UmFSioLhxhrMD4mO3Ltmb4sCLVeX4NZllsj76-9Zc9LCJfwT0uCymLWbj76h8Q0hbeamxN5BKA3IKFGubxOC9Otyn5-loIiWpz8tXLl-ZaSg7nsP5qGoYVk8mT2e6nH1m__d3PeDBtPLV7jkNWrQ5DqLc68tr1vrEAeLX0ltJ8SI4JoQ0_HTJ1In99SEMUjB5reXUwanEbTz3it2m9_zd0xgT2myGPw1JEVXjkDwvQbO6C3f_t1Caf-SP8Zqr-zUc9wObABrXz7E6sW0Mnx6UHq_OLGRbL3f0mFPDBI_89eHaB09Y9oJjfIwMVBXC1M0jfv7fvnBkZvAw8VRrm5JA-9pbJ_azpvrmyKDuaLdhdjmrUcK3ke3tXwL4om9hK1cdGe72A4gYv6ScmbZBhpLyopftvnwzEOvCexvRiXS6qwW56g-j5hb29IMb-8TZWPIJYlE4JTDVxOkDhH458_e7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76775f04b.mp4?token=UfNJdVf1nNrvqvOLw--9UrsrRUuO7SqvqrVySL5gX5jmf9Ne84LcdU_D3sqbTq6cJYPIENn6c67sVBHf0AZCEJf5Yo_opbw58kJRdXS9NC02k4AiNI8qjMslAGToZmAOjqxIg6XXr3dlqoyhM0uV9AXnRyzoufIuNYLyvZ7aSDvf_AAsdOKq5l-B6iRHglLf7tFZCDtQxZy2EppQ9i-q1UmFSioLhxhrMD4mO3Ltmb4sCLVeX4NZllsj76-9Zc9LCJfwT0uCymLWbj76h8Q0hbeamxN5BKA3IKFGubxOC9Otyn5-loIiWpz8tXLl-ZaSg7nsP5qGoYVk8mT2e6nH1m__d3PeDBtPLV7jkNWrQ5DqLc68tr1vrEAeLX0ltJ8SI4JoQ0_HTJ1In99SEMUjB5reXUwanEbTz3it2m9_zd0xgT2myGPw1JEVXjkDwvQbO6C3f_t1Caf-SP8Zqr-zUc9wObABrXz7E6sW0Mnx6UHq_OLGRbL3f0mFPDBI_89eHaB09Y9oJjfIwMVBXC1M0jfv7fvnBkZvAw8VRrm5JA-9pbJ_azpvrmyKDuaLdhdjmrUcK3ke3tXwL4om9hK1cdGe72A4gYv6ScmbZBhpLyopftvnwzEOvCexvRiXS6qwW56g-j5hb29IMb-8TZWPIJYlE4JTDVxOkDhH458_e7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راه حل قطعی پایان جنگ پیدا شد!
استراتژیست نابغه ایرانی — مستر قرهی — موفق شدند با استعانت از خدای تبارک و تعالی و نیز هوش خدادادی و سرشار خود راهکاری فوری برای تسلیم آمریکا و کله زرد ریقو پیدا کنند:
سرش (سر فضاپیما) را کج کنیم تا بخورد به آمریکا و مردم آمریکا ضد ترامپ شورش کنند!</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19340" target="_blank">📅 23:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19339">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_otr8T9_IRuVuY4POwxHasXzuj4gAUBjh7FXlVPh5U5hu18geHbl4Yyb4XdbTJEd2qLpIT3Gr0D7t9fu90SvS_iYyX6Li8_200bg9x57iU5JUUxfEBgNzo4LWeG9ChiEzJl-5kP25dQdTD-N-I1AL95DijhtJnZqsGDqe69RWjapX8JAdXOphVf_DSg9hXoGSK6zA3iOEeOqMnCSFUjcXMIFeHbWGV3HGNt4eijDNq4pAwA69NboQBYou_bRsJwJ0xxyNNMz41lT3lycCmn33J3GNhVQIgbcWX-ftCSp1fYxgdHI1mcMIeFaRYaTUQNKPFssWL_mU76YRhEI-Ip4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19339" target="_blank">📅 20:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19338">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اظهارات ترامپ درباره ترکیه:  ترکیه علاقه‌ای چندانی به اسرائیل و بنیامین نتانیاهو ندارد اما ترکیه برای من بسیار ارزشمند بوده است.  به هر حال، ترکیه یک کشور بسیار قدرتمند است. فوق‌العاده و با یک ارتش بسیار بزرگ.  ارتش آن‌ها تجهیزات بسیار خوبی دارد.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19338" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19337">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دقیقاً طبق تحلیلی که ارائه شد آمریکایی ها نخستین پس گردنی را به اردوغان زدند و علیرغم همه وعده های ترامپ، گویا تحویل جنگنده های اف-35 به ترکیه متوقف شده است.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19337" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19336">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJNllDirtB-11w6FXHx1OgO6Z2EgVKRsCrPtRm-wuzHrykm5pnVb404D4kgXOFTKU8Ga6EAmSulqLHtlfJDkntLPiDFhuWTdoU6-lHZFH6Yr97n1HbBh0QMkaDSXbRUkKycK2sUXqrZF_Hk_iqhkRc3pMM4pFujrIEydSaB4ZO7LksPUiE5F29TVlBajkyx7QNLz-TAFGriVkJDQZOn-1G4mIjwtg9_jfYEMN36ufpgs00Yo_uPKNBgrXG6j7hMiAuvwWycvoEmhZGZCBq8Uvabxh7DDz56VQdtcvIcJ5T3mmf29AYMvUSnnctrab_k77NwA5sEJefD5EP3HmrfqpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19336" target="_blank">📅 20:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19335">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پدرسگ ما خودمان دزدهایی داریم 100 درجه بهتر از تو.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19335" target="_blank">📅 20:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19334">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ:  ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.  این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19334" target="_blank">📅 20:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19333">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ:
ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.
این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19333" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19332">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">عاقبت به خیری
😄</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19332" target="_blank">📅 20:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19331">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19331" target="_blank">📅 19:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19330">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ca9O8cqogANZSu90awvsmmfqdRjBVzrGLX4iundJp2YGO951fRYJIS9u25rO2TBL9BLYB-OqfIvqZSUwgh9v_cFFYkojnkLwZpdetDjlt6LQnjeqaJJnSiaK8aP2Onev1xASbeqd3pCkQd8EOz83f9qVQeEM4CjzAS29_P_XmFATaV69BvyH_gnUs8C67ZY82puPbEuysrhSySXZi_RZuOr_KavGDnn8VD-ZyXLKzSOotr1UlnKRqwwvjIwEaehrG0RKyjDZMCfq4rVuo2d00AqXjEQRKWtApZB6sLqKx4k5MbRUVhbkQxmAEdRajN_u9ApZPH5zUKgM_clOq6FziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:   به درخواست میانجی‌ها به مذاکره فرصت دوباره دادم.   فرصت زیادی به مذاکرات نمیدهم.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19330" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19329">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ:
به درخواست میانجی‌ها به مذاکره فرصت دوباره دادم.
فرصت زیادی به مذاکرات نمیدهم.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19329" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19328">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">276.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19328" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 13</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19328" target="_blank">📅 17:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19327">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارش هایی تایید نشده از وقوع انفجارهایی در عربستان و هدف‌قرارگرفتن تاسیسات نفتی این کشور.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19327" target="_blank">📅 16:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19326">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxNdn3H7ia5cJvZHhxMzSPUo3ShoC9FIFomKIIOlXojWHuh76pA21_B4nMF-OEvk_4v12GHJatrnHiAjH46PeVdH9IIsq0tGy4ZD6UroUWjDRfu7PkOP0sdJwH_zPXS9-bYNaUQve82H7KaPP5dak4aULUVGNV-DDlc_p57NY5HUByvjAxQHAaABcjTocOG1UOvqpUVklCVfIhxxXTH_9e7HN08CvszDp_W3nnv7n-ucQzYOMRpRfRiInR8Vak5RnRXQg6FaE_le9x5K3d8tSCDVxlgpAjwQtNDK0AdcHg8mCX92L2W6PiiLcBVNPknc0PkUH3-Owj08mUdZ6a4SOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
بازار اوراق قرضه پیش از فدرال رزرو رأی خود را صادر کرده است
افزایش بازدهی اوراق خزانه‌داری آمریکا نشان می‌دهد بازارها با نگرانی از بازگشت تورم، کسری بودجه و رشد بدهی دولت، انتظار دارند نرخ‌های بهره بلندمدت برای مدت بیشتری بالا بمانند.
تنش‌های خاورمیانه، جهش قیمت نفت و تعرفه‌های جدید این نگرانی را تشدید کرده و باعث شده بازار اوراق پیش از تصمیم فدرال رزرو، عملاً موضع خود را درباره ماندگاری فشارهای تورمی اعلام کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19326" target="_blank">📅 16:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19325">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وزارت امور خارجه ایران:  «عواقب حمله به کشتی ایرانی برای شما غیرقابل پیش‌بینی است.  پیامدهای اقداماتی که زلنسکی انجام داده، بر چندین کشور در سراسر جهان تأثیر خواهد گذاشت.»</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19325" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19324">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.  آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19324" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19323">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.
آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات اسرائیلی، آتش‌سوزی در حومه تالوسا و مارکابا درگرفت.
یک پهپاد اسرائیلی چند بمب صوتی بر شهر منصوری رها کرد، در حالی که سربازان اشغالگر اسرائیلی به چند خانه در بیت یحون آتش زدند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19323" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19322">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
نتانیاهو، اطلاعات به‌روز در مورد پیشرفت ایران در جهت دستیابی به بمب هسته‌ای را به ترامپ ارائه خواهد داد.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19322" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19321">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 13</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/19321" target="_blank">📅 14:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19320">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 13</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19320" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 13
دوشنبه 27 جولای 2026</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19320" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19319">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19319" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19318">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1N4Lnp-CLvL7aJYvDIC1MWmd9MCkdbyDgiBd79GdhTii5V4GK-pAtkbIPPvqaitflPwP3RsAoiJ5zTLfGaSH39XhoXKPYtSvrQaTg4AwayQPgQfKG4w82iyQNgJqtNTWHDzH465zt4GT3hl6lPEMmCF8HbB6dCLJEOC_nLbPfA1R3gi6rvoZ6NQpvRDQQsmX93g_lNki7SJ6bQpbeLjYvMl0xnndkF573-z6fm-Q_tMaczlHkx5diLmxekHklOvc_LCNGylhgYDk2fIJ2UxAZ1jLxtAQUV7vEIZ9OaLEI5g1n1GV842JC_RNF96cOC1ZEHZjBu40ooilR9IyqJN5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۸ سال پیش در چنین روزی مجاهدین اسکل خلق میخواستند سوار بر تانک های چرخدار برزیلی از مرز با عراق تشریف ببرند تهران را آزاد کنند که خوردند به تور کبراهای هوانیروز در تنگه چهارزبر و مارجین کال شدند.
#تاریخ</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19318" target="_blank">📅 13:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19317">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.  هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/19317" target="_blank">📅 12:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19316">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.
هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19316" target="_blank">📅 12:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19315">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19315" target="_blank">📅 12:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19314">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpfsPL7wlYymu7RL9JWF78jrhfkZQHoOHsGfUaJ4iS9eK4BQzWpKbZTSkPcS9ppbQ_WUamMYwQfQd0cqXXdmdltrgkrAW7dPPiouF1Ky5DjIV5kW81dWwU3-uqy_OclzmQh-ZaMw3kbWx_IgdLSC8QJf065ZE4sgwzbGFSvq0dthlOHufgPmDAbuUoGveS-4QhiycuOy2bJr8nyxpbnoEpDHoQahOCqM5x953Pb0KQ85XaIgkQ8geWr4_0YJ2b9OUHWngZGdStXkZHV1oIk-mEXiWMg7t_q8kJXBhkierzQtY2AjskzFWzmEnKJerhffkhY20ypwwSiqt6AmBlHdyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19314" target="_blank">📅 11:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19313">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19313" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19312">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گزارش نیویورک تایمز، مقامات آمریکایی نگران هستند که پوتین و شی جین‌پینگ ممکن است کمبود مهمات ایالات متحده ناشی از جنگ با ایران را در محاسبات خود برای اقدامات بعدی‌شان در نظر بگیرند؛ این اقدامات شامل اوکراین و اروپا برای روسیه و همچنین تایوان برای چین خواهد بود.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19312" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19311">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-ti4Kqh305X4YVIMGkRAyrDldmwL8Tmc8bdpqOqdTtXPi1kVPFwnSGvF8pk27wbFcEiWmBkp6ttksjIcw3ip_XCSQ4W7tD9B-Tk80hq0wmgYiunVhm2iIk6tbp82S-mNaKGd5uI9nXTatRCzSwgFdXvSr6U1BKzTkYm5rpNH2JT9FE4IydAoJxpizS4Wn8sjf-f9a2WuSvYAYJMtkrT2z8GWzvscky4Qi1DW9KTeGUEfjzf21zkib3z42mQiBP9yt3urjNHT68T1DUibWXwt2cKA5dPFWRQul2o9XL1gWoSlrJSfcKEXg-r0yvp5jEmNpvNws4AJyxXMWpfGgh_tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حوثی ها و اخلال در مسیر جایگزین صادرات نفت عربستان
با ادامه تنش‌ها در تنگه هرمز و دریای سرخ، عربستان سعودی برای صادرات نفت خود بیش از گذشته به مسیر دریای سرخ و کانال سوئز وابسته شده است. ریاض از زمان آغاز جنگ با ایران، با استفاده از خط لوله شرق–غرب، بخش عمده نفت خود را به پایانه‌های دریای سرخ منتقل کرده و صادرات از این مسیر را از حدود
۷۰۰ هزار بشکه
به
۴.۹ میلیون بشکه در روز
افزایش داده است؛ رقمی معادل نزدیک به
۵ درصد عرضه جهانی نفت
. از این مقدار، حدود
۳.۵ میلیون بشکه در روز
از تنگه باب‌المندب، عمدتاً به مقصد آسیا، عبور می‌کند.
اما حملات اخیر حوثی‌ها به کشتی‌های سعودی، این مسیر جایگزین را نیز با خطر مواجه کرده است. در نتیجه، بخشی از نفت عربستان ناچار است از
کانال سوئز
یا حتی با دور زدن
دماغه امید نیک
در جنوب آفریقا به بازارهای آسیایی برسد؛ مسیری که
۲۰ تا ۳۰ روز
به زمان حمل‌ونقل می‌افزاید و هزینه‌های حمل و بیمه را به‌طور قابل توجهی افزایش می‌دهد.
در سه هفته نخست ژوئیه، حجم عبور نفت از کانال سوئز به بالاترین سطح خود در
دو سال و نیم گذشته
رسید و انتقال نفت از طریق خط لوله
سومد
مصر نیز نسبت به ماه قبل
۵۰ درصد
افزایش یافت. با این حال، محدودیت عمق کانال سوئز باعث می‌شود نفتکش‌های غول‌پیکر نتوانند با بار کامل از آن عبور کنند و ناچار به تخلیه بخشی از محموله و انتقال آن از طریق خط لوله سومد یا استفاده از نفتکش‌های کوچک‌تر شوند.
در همین حال، ایران پیش‌تر هشدار داده بود که در صورت تشدید اقدامات آمریکا، ممکن است
باب‌المندب و دریای سرخ
را نیز هدف قرار دهد. به همین دلیل، تحلیلگران هشدار می‌دهند که با محدودتر شدن مسیرهای صادرات نفت، توان بازار جهانی برای مقابله با هرگونه شوک جدید عرضه کاهش یافته است. در شرایطی که قیمت نفت برنت به حدود
۹۷ دلار
رسیده و برای مدتی از
۱۰۰ دلار
نیز عبور کرده بود،
گلدمن ساکس
احتمال افزایش قیمت تا
۱۲۰ دلار
را مطرح کرده است.
#ژئوپولیتیک
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19311" target="_blank">📅 07:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19310">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RW_8y7nqi35RcAczKbpe-atMC90WlU7tGCcZ6Dc5pHoBQFez4D0MN71NYq2ZpfRbViDYzkLsu4yTW1FdyG__lFgukHMpJMuZLJlILLwJjbReKC-P6YE1A-9mBI3ThP0kFa41SJa8FQoEc3lc7nPUbK9pildKdP1zooMUgLNrE5boug0kNgjjQKVKXTzbsO20yi4yF74ZDKiFLtaedQoRyJCsIQwSQch2gyUYP560OBV2Tvl16jKm-5R0VOV3-OivYo29qaAGdjyvqblORyU136mydMDkMhZ3fnEh3A7IUH_xKQibExFQh-BTRKlnnTuHt4EtuuHG3ykOhiIBQOpUFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:
برخی از حاکمان خلیج فارس به صورت پنهانی به ایران پول می‌دهند تا در آرامش زندگی کنند. برخی دیگر در حال عمیق‌تر کردن پیوندهای دفاعی با کشورهایی مانند
ترکیه
و پیوندهای اقتصادی با
چین
هستند.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19310" target="_blank">📅 02:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19309">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19309" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19308">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19308" target="_blank">📅 01:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19307">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس شورای اسلامی:
▪️
هرگونه حمله به ایران همیشه هزینه‌ای دارد و این موضوع امروز نیز صادق است؛ آمریکا و اسرائیل به خوبی از این موضوع آگاه هستند.
▪️
اوکراین نیز ممکن است به زودی درک کند که ایران اقدامات را بدون پاسخ رها…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19307" target="_blank">📅 01:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19306">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">▪️
لیست کسانی که اشتباه محاسباتی داشته‌اند همچنان در حال افزایش است</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19306" target="_blank">📅 01:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19305">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19305" target="_blank">📅 01:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19304">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2PGsSvvauDZgotviK0oof9ZAXdgD93m64JnJ1MZ8SYtQyDI7HfFvJfyTCEeXm_QF_Pb1c8oo9YKP_J53gRy1vXLsNKuVPb_VObZWYyp-FN9zw-SlN4gwxr2qY58MEMdQFE6lHLWPYjkpmhRmKXRctLPiqTDqLzAChPJefQNEnX6l3Y0Z8fZ1GhVbLKWYW19OrDtU9kwrg3D7tOJB-kc6BZ2Nq4McPgJI16GBQeSZovaE4A4qFuDKrFCgnPwwlJubL7bw4QAj6ZTaU33Pi1nfnttAXkDrjkEw2W-pnrdw8uEfJ5tElGQLYwDsO8w7GB3pUnwPFw6m2z9LlS7y3BaTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشایی نفت با گپ 7 درصدی منفی!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19304" target="_blank">📅 01:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19303">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwAqqX1vtjd9dJfKEopEZnZYB6FpnHiUhPWO8YxzqZ3ads8WMaQI4rmAadVR8X9mpJVVXTvNHzpXUL6OYBGszlSZdYw1hTQpESuMcoxd3Y99biLfwxl6uMLx17gT7eabbNm73CLmYnFtQ8ML8L-EncQz66AOLQE6nC0_hmIuyVgzclwDhISw34vAstnevVXjGr8K5vx5WjcqqLEkjwN2MLEIyA4iYSO8PEixXMNe-hOXe_88yxY5ZwF0d1gumYLqU2W_zAu986Ze3aHwHLjVk3R-rZQ0LIH_gtJNRLkimW_1AwPv6p6XIDsGCeZYEW6A-vH3s0d5paVVhrb_6PBkuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از جنگنده جدید دوسر بدون دم توسط ترامپ</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19303" target="_blank">📅 01:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19302">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxTRFUCUUbaq5dE4McEeIxZpa4t9A93klL5jN0AKOWD0gTuj-hohkriStmzJhYNJZAbIVUq-PfWVDzFM7-268Yf5kp_4rg5r-enbxStQTagFuPKKSgojCIO8JkJvfeetMw6c_JQVfh_KyMlwf51xFvl2oZTza_c0BxRur01pExQAeWPRSGZ10UL2WbtHM0_2nwBkW8q9FY4V_7rp44jGj1akamlrStpCzyfBVYCh3nxoG1rG0p3C4qrGqAMj2CDL0HDrnqwA97g8oQbZtzRjchhkmncVkROXvp0VKeoWmmEepwNDYI8Vk6TVLlUulvmM2iVp1U6tG7kaUat04JOslA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19302" target="_blank">📅 01:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19301">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOPZE3oMxcEaFdkjdQaRjnmOupdq14_j_MCYsRT6XeXffCAJSVst3ssTvIWnLbQWLB3JbkOfEcIlaW63LJkzCmWhlybVxeXk3Q7Bi3lrjV4KGv3ctLYA9wRyTkaPCQWyaPl0-Q9Uz5UbgMS3qfQFhGXWcliT9c4fLUV5ojcrkavLLJSqp6J2fIpcLfd38ozHuVwTBiKZ-Hfk2syU45AeYtgIlKTabwmuo8x0e7fuO31ZQcS5BC-z-OcH9zPXqBszF8dMboFm0nYVtGYxu7LtUd2EtrjImk3YtZ8V6lWWRygfjrBwn4Ga30eKfHhI3almk3hxmb73aVRxdbh2WAH99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ول کن نیست!  اشاره به زدن موتور نفت کش های ایرانی که می خواهند محاصره دریایی آمریکا را بشکنند</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19301" target="_blank">📅 01:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19300">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رهبری ایران در نامه ای کتبی اعلام کرد:
در برابر اسرائیل و آمریکا راهی جز جهاد و مقاومت پیش رو نمانده است.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19300" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19299">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وال استریت ژورنال:
الکس هولدر، فیلمساز مستندی که به زودی درباره لیندسی گراهام منتشر می‌شود، گفته که این سناتور در هفته‌های پایانی زندگی‌اش به تدریج خسته‌تر به نظر می‌رسید.
وقتی هولدر پرسید که آیا او خوب است یا نه، گراهام پاسخ داد که برای خوابیدن زمانی ندارد زیرا هنوز باید رژیم ایران را سرنگون کند، به میانجی‌گری صلح بین روسیه و اوکراین کمک کند و روابط عربستان سعودی و اسرائیل را تا پایان سال عادی‌سازی کند.
بر اساس گفته‌های الکس هولدر، فیلمساز، لیندزی گراهام به تدریج نسبت به هر دو دولت ترامپ و هم‌حزبی‌هایش در جمهوری‌خواهان به دلیل جنگ با ایران ناامید شده بود.
گراهام گفت که با «تعداد زیادی از افراد در داخل» که با درگیری آمریکا مخالف بودند، درگیر شد و افسوس خورده که مقامات کمی از دولت به‌طور عمومی از این تعارض دفاع می‌کنند.
«تعداد بسیار کمی از افراد در دولت این جنگ را تبلیغ می‌کنند. من شوکه‌ام،» گراهام گفت.
هولدر گفت که گراهام همچنین پس از اینکه رئیس‌جمهور در ژوئن یک توافق مقدماتی با ایران امضا کرد، از ترامپ ناامید شد.
در مصاحبه نهایی آن‌ها که چند هفته پیش از مرگ گراهام در یک مغازه باقلوا در کلمبیا، کارولینای جنوبی انجام شد، سناتور گفت که ترامپ بیش از حد مردد شده است.
«او اجازه می‌دهد این موضوع از دست برود،» گراهام گفت. «باید بروم و با او صحبت کنم.»
در اوایل مارس، لیندسی گراهام پیش‌بینی کرده بود که رژیم ایران ظرف «سه تا چهار هفته» کنترل شهرها را از دست خواهد داد و مشارکت بیشتر اعراب «تکانه‌ای تقریباً غیرقابل بازگشت» ایجاد خواهد کرد.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19299" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19298">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVvmIPLiU7rD6w77-LcqzPp0FzaxDhyWmB-YdrX2W2Ip_KpHhTLJIgViu3CyA51aqmxF0OSkRdQh6M-ltv_q8dysMPz3ebkZRwX830j98Tpz4J1OCV-q3VJ135dQyQrmSBKKMRjT6DEpMg4BQ7gZOgK0PIBDIJxLv3ibdNNRuXuh7EUvYQ5XJq2J9PAvFr6kLZ7-FQAoephT9wA_T3CY02qxEYowsXQWIlgN4yQQai2M46idsSoQkh4vf9gkIGRbaWZ3bFyXt9Sg01i7J1iRj-JPrswkeoyfdfXtnilxwNSo0mPgqb_jnvSP4delQmUai-rg4rTH8sZLU4_7IREyWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آن عرب ها کیستند؟!</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19298" target="_blank">📅 23:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19297">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ub3grX5Sb48-DIHTL0gTmQxa_J3S1vCv2muC57ctmIytDo0RHGP5EC46iM7W2HU-eGoerm3bqcv0jgxVur3ttWBxwrOBVHsopb5xpxf2P-EGQK_tp6acSNL3UK-dVyTS67O1JIC6PKM-HuO8D4vpCQ12o1H9_8u_QFV5egOwSkBh9AdUawWg-y_089fAd_1RTt6bJSMhIe7Bz3RtbkMjT0ykWuqnWmqmupPLmSB14GaPdxaOQ1YcvAb6UTg37zMb9gUGfAPszjKNG1xEQHltxpwId2lUWErpskPpNwjpWjresG439OxDxese5TOniuVewSKJ6q1X8uDGW6_IilPiXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19297" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19296">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRRVbqdLK0XuagMpx9_cr-4ktLPt6-SOBohU8rG-n_S3m-OFFbmEr5uNHl_8AEF82rvvDk66D6wXtAuqZ8pYt9lBANrZu4uH6WlO3WaCYp9zGZNvHzPf2fR1UsNabbZEb7uEChVjODLhT5psCZWYVsfyZRS9yvuuhSCwjE-JaBfZ4IrEvFOKvelPp9bNc9P9xBrnEelfQ5LZlyxOxwtuC5UTYWdoeHAm4PT7qoi-ba1XoXlG2dPjLfOc_Eyif2aN6OFqwX4dTWYWLy7Nm2nZSFiY0ULWOWAMANbr9ETmLDge3HecXLT0ehFvM62-_Td1o-k2J-SVj7cSTg6qTMcj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ!</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/19296" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19295">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قشنگ دارند به نتانیاهو پاس گل انتخاباتی می‌دهند!  میانگین IQ وکلای ملت را دوست دارم.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19295" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19294">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19294" target="_blank">📅 22:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19293">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نماینده های مجلس شورای اسلامی با لایحه ای مبنی بر اینکه که از امروز تمامی شهروندان اسرائیلی اهداف نظامی مشروع محسوب شوند موافقت کردند</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19293" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19292">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXQMgtk6AqW_V-sUd_fHogKgFTSpKF90Uoy-7UcCHTYvFlvC1ErHqD3sHibGehXegAhrreZLb-6UqloM2g1yxa4nnZtIYsyl9psv5cEDsDDtvpyr6qoj0EFaYmZr37EzDGg_a6HX-lgpv1ODYs8Vx0VCwz_AwyMJwmjGTE3UrfVY49PgaNyWIibC1Z9sg69PIAMiTacTzCY92f5J9pbUap8rtCEj196vZQ-_zDXHsgxVrwyYR7Ng_2d6VZXz2d3PtMBBKjINen_GH53u5Egckg8JI_LvduhXY4VVL2Es7rE6lX3H_wcERF56sqxvmp36yaysvhaArXXGRAgoIb4yNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب رئیس اول مجلس ایران علی نیکزاد هشدار داد که «عمل گستاخانه دولت اوکراین بدون پاسخ نخواهد ماند».</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19292" target="_blank">📅 21:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19291">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHFz2ue1cEnQ-ALJ9T5S67nzjVwZWukHb8tqRZqtH_twEPzgHiOXYFG3It4QzJgdvBvO9hTSahPu8zZbgj08aUo0KkyYjU8RE3nJGDkrPfSUPiblYqEfgKSF3DdhrCMNqRMYDD8lyxLMC_IYpImOPvZKWv8lqOUdYERoLzHNUmzncNQ2xTer04i_KoGQQvt1Q8YqdxUVGcIYLuVzIOPbHUyQf5n9cDZKCLMAe98vRFhimNkHSqT7xjtd5WU6W0B8JiF8GiETSE5F6RFiDngJYEFvBN7vDP8DFIpxPh5WMa2-HAFMAfofwDUWlZCj7PGvU_aNT9hkI5I508kdd9j1Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انصارالله یمن:  یک فروند پهپاد آکینجی متعلق به ارتش عربستان را بر فراز استان الجوف سرنگون کردیم.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19291" target="_blank">📅 21:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19290">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آکسیوس:   فرمانده سنتکام «برد کوپر»، توصیه کرده که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به حد نهایی کارایی خود رسیده است.  به گفته این منابع، توصیهٔ کوپر (فرماندهٔ سنتکام) به همراه مشورت‌های دیگر مشاوران، بر ترامپ در روز جمعه برای توقف…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19290" target="_blank">📅 21:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19289">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سپاه با زدن پایگاه های زمینی آمریکایی ها در منطقه به نظرم دارد می کوشد تا تاریخ حمله را به جلو بیاندازد و نگذارد آمریکایی ها بسیج و تدارک کافی داشته باشند.  وقتی می دانید حریف می خواهد حمله زمینی کند خب طبیعی است پایگاه هایش را بزنید تا نتوانند آرایش مناسب…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19289" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19288">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcQPBC8PodvdTdxgkC9z97kD7ksqseVeRmFX3fQxdMPqXgM11_DfhD3fzblzvjMXMeo3ws3hI9e_cX2oPWCLHcbE2NgPSSLsqGg_tlo5EXwR5sefcWrpCcW_JJHMdPCGVd6DMqVYx7A2Q66vH6mvrIBvGsk-Q2jRGjdzFxROLeYQbW_pfVZ6BcVL70pAC-LXb2vd948HSNm_hKF3UytsW-aqhN6DjdweYbnAFCVQzlRF5vpPu_OniUFzM7F_bYSHFcnU22uKAE9LrG74jxdBiQ7Kv2DQntvyt4khCUJSBIZZb9t5rGZBKhefAQVBPFzqoxaBfknLeLWjB_JtDTFSHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت های پیشا—گشایش نمادهای مهم در بازارهای مالی
ریزش سنگین بهای نفت برجسته است.
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19288" target="_blank">📅 20:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19287">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">عراقچی:
زلنسکی به دستور اسرائیل به کشتی تجاری ایرانی حمله کرد تا اروپا را به جنگ بکشاند
‎</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19287" target="_blank">📅 19:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19286">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وقتی میگوییم اندیشه چپ باعث زوال عقل (و البته شل شدن ناموس) می‌شود یعنی این!  شاید فکر کنید این صفحه دفتر دیکته سید محمدطاها ۶ ساله از مندآباد باشد، اما نه! این نامه غلامحسین ساعدی به معشوقه اش طاهره کوزه گران است.  لابد با خودش فکر میکرده چه کار بامزه ای…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19286" target="_blank">📅 19:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19285">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU2rJn_IU8C1Ai73j3QklqHkj_EiaOx6CRh03aMhANbcT0XBOCbDfFxfh34sI9FAVbqZjabyChXypX0AaP0qOjb2r3U0_VGiSP5cmOgy-vyCEpBH2U9_dTGdpjyO5rrlhhaoY_7kelvMYNr_Aht9SID6_tb_JLkLLLK8IkIxCwdbS_XoSYTxpNV-3eE5EEPOZ5EUW9VWC4ilbbEu5_lUUhIyoaG8SJf5Z5MpP-iWpwrzwACXSL7zgrtsbjKEQcel5LHVffTaJG8Mju5Uxs49PHGVBdDd74PoyTHeiGMGCVU2Wul8BoCtfpKJbz-Fpa-sixccle5DGzWJZ7E6GmhbPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توئیت عجیب عضو کمیسیون انرژی مجلس:
فقط نفت!</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19285" target="_blank">📅 19:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19284">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfhPBrvHeQv0-cw4CtM83fGCfDtRa3_lHILThw2SHp-fLYr520I2BpWfNP8eY0t4D7o8p_xLoFIkn_vwXki-cZG8ZC3zDd5FzYv_xk6o-fj0Ixml3LzLmb97hE7elzbnnld6Aq9CAeponGXZucQfA6LPjQj1CS8xDmy83teyXgUplAj5v7LKMn4TAAqsj0qcpwGXmlxlj3_21ctnkCp9lDQu9oQgrojMUYu43hOVM6yf5F5UqM89RxS0NaPIqObucgrMb16WlKY4c-RMP8_PXFnnZHluunWmd8oOZHagi2_qbolgM55vyk2AnHwczWPmw3uwAVSEyTSqGHpGDWVx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استالین و بریا!
بریا رییس سازمان اطلاعاتی شوروی در حین جنگ جهانی دوم بود که هم حمله هیتلر را به درستی خبر داد و هم با سرقت علمی از آمریکایی ها، برنامه تسلیحات هسته ای روسها را به نتیجه رساند.
جالب اینکه او پس از مرگ استالین در سال 1953 اعدام شد!
#تاریخ</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19284" target="_blank">📅 19:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19282">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نتانیاهو به فاکس‌نیوز:
جنگ زمانی پایان می‌یابد که نظام ایران سقوط کند یا چنان تضعیف شود که ضرورت پایان دادن به برنامه هسته‌ای خود را درک کند.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19282" target="_blank">📅 18:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19281">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=YWbLqthJuprkfOpSmmVmVVaqPA4RxAEkfFEjuVEm09HZu1qA05fMrLOsfetS0ufBGTbHA-zSqPvPyo4ya6s-H5U0FVHpsbrbekkvegx7Uwsj9RJrOVbkntI-OFz9zox_qx3QAKayCqP3WQC5W1x6w5wWjoqxWUg0phtg4mnfuB2EZWyVGOoFIBm8UaDd6XwCLqjNAHq53Zq8fDzsnPAJxjxgktWw-Gvk1l0yB2nHIHhWHAJBAi7YJl2PcCXs8tIz6Deq4Ul9XTvit54-3-1GnZ3EsdbVXgoWKSC3viOJN9zVUHuSlEeGQzl0m2q8UX_WkwFeJZ2lC2hxqJZfMopMnQEAZN4O9mr9VxaqalVieo2NULYoH2O0wTUM4G0CuIMYhmGjWGp_0AwqH7xNT8XRHuJTw1ul5jfitO9uQyUBSGT5y7EQH1BSjEqXK5-9hYpeY18zwfA0Doj3MLf4wNAIiz7oPiApDfszCg6ZfaNzkQLWNQT8Oirv9y6Nhd9ooWHC39yKR3a4UddWmlD2K8_eAAXKt4S4loz7xVCI6KGejQuvIJUWXUFpRHCyexsbsKZHd60i2ulIDBSOyAPWPMT6fSmylHmM5HBM02SAsAOOAd2FG4AU-5rO1Gq3Rs_7bP4Zu4fM9J7aEYZVWd1EzSCknC3o9Uv-VB1RT2RfE5LjKQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d5b002cb.mp4?token=YWbLqthJuprkfOpSmmVmVVaqPA4RxAEkfFEjuVEm09HZu1qA05fMrLOsfetS0ufBGTbHA-zSqPvPyo4ya6s-H5U0FVHpsbrbekkvegx7Uwsj9RJrOVbkntI-OFz9zox_qx3QAKayCqP3WQC5W1x6w5wWjoqxWUg0phtg4mnfuB2EZWyVGOoFIBm8UaDd6XwCLqjNAHq53Zq8fDzsnPAJxjxgktWw-Gvk1l0yB2nHIHhWHAJBAi7YJl2PcCXs8tIz6Deq4Ul9XTvit54-3-1GnZ3EsdbVXgoWKSC3viOJN9zVUHuSlEeGQzl0m2q8UX_WkwFeJZ2lC2hxqJZfMopMnQEAZN4O9mr9VxaqalVieo2NULYoH2O0wTUM4G0CuIMYhmGjWGp_0AwqH7xNT8XRHuJTw1ul5jfitO9uQyUBSGT5y7EQH1BSjEqXK5-9hYpeY18zwfA0Doj3MLf4wNAIiz7oPiApDfszCg6ZfaNzkQLWNQT8Oirv9y6Nhd9ooWHC39yKR3a4UddWmlD2K8_eAAXKt4S4loz7xVCI6KGejQuvIJUWXUFpRHCyexsbsKZHd60i2ulIDBSOyAPWPMT6fSmylHmM5HBM02SAsAOOAd2FG4AU-5rO1Gq3Rs_7bP4Zu4fM9J7aEYZVWd1EzSCknC3o9Uv-VB1RT2RfE5LjKQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی جالب است؛  از 6 کشوری که شدیدترین بحران های انرژی را تجربه می کنند، 4 کشور در منطقه ددخیز خواهرمیانه هستند و 3 تایشان (سودان، سوریه و یمن) در ژنده پارچه ای که به عنوان پرچم رسمی معرفی کرده اند، رنگ های نجس و نحس پان عربیسم (سیاه، سفید و سرخ) دارند</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/19281" target="_blank">📅 16:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19280">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19280" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19279">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/19279" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19278">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8aVganCUmXUMXcOTMSSeNxzO3rB_PVORfcl_yO4ZGdjQKJz9QX54oEQ_qNgbGmABOq-3vSwG8BSNYAXePWp2ZmIzjDr01nuEkBcQemWMxVM84s9C0Bigq2Z2fdPkxsG-EG1tk4-JDF1SqpR6qJptFGlXsi-M2q1MbDfq3cJ-Xx3fgKzpb3UsCbaJyZM4F4cd6MFxM0u3kt9ltUPNzmofQMxqMGG_-cS8cdP50NLPGPPX4phbgiQMdiFkGXKb6Wwj2ejILo3VYFaURDo3ZfxF2irvUWjvKAkh8H1xTndvD5ICBAaZWeMHJMoc0nMjitKpyHU6YXEqToK_yL3BCdmow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19278" target="_blank">📅 14:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19277">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">روس‌ها نوعا عادت دارند انتقامهایشان بی رحمانه ، مبهم، نامتقارن و شکنجه مانند باشد.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19277" target="_blank">📅 14:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19276">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وقوع دومین حادثه دریایی در دریای سرخ
سازمان عملیات تجارت دریایی انگلیس از دریافت گزارش حمله به یک نفتکش در آب‌های نزدیک سواحل یمن خبر داد.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19276" target="_blank">📅 14:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19275">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">برای نخستین بار در جهان!  کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19275" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19274">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=ZBuad6T28_Nu9Zf-1HjHXmuikPPaDi7isYyP0qNA6UBTGbHE4e6Se6GRQWHMwxJeLwu0FBYgvtA0E1rVGRHk4xOX_E9xREHFUuYry8Y86emzjmx9ifKzIdjMCdP1IWy8l-545_C_QAmTyHvYl5t6ca-0ndAmGZok_aHMzaKllhVRHEhYT21H8m9oIpWNo5dD8sHz4ij1U6EXiRzqbeNpfbPr90VaV7iNqh30Kw3aQTpK30hLseuHvuUTYBRNrbL5h50EaTukBmyIYGJoyd5PsGI6HiuEiLckqBJlH0KPhCCc3Zz2Y_nvOmTyDwwB0HVpbaoGwBYnWfiQ5FrQepRB-hNxKNndBIiiEWRsshZRgQJ2rtIPj5bmNUT9YWv_Am66Nqv8ZfFaReErU9pSu6Lq3AVHxCTeUzrqEMO_IYJsIXqxyys1-jkmkIWDBJbiHvz9V_saHBW-dZa5TdCiuzylKkNk6m-xBLcFpL43JLSBVQpOxYFaCnCRVTdhbyyUR3mINzZQOZ3sbq2OJ8Sm8fB7O5Y_Z_ppbkRC5GRuksOLLPa8IdPC3a4D11UozEJ0_AzOgDDNJvd85hhypG4rQeJRVA1_DBg55QmHbbMbewPI6aLMHB2VzKriqQ-WaZUt_hlnQDQPUr9k8Q-h4Ogjn212UQgrP1Gu0YalDh5AynbBA6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/312e3c4284.mp4?token=ZBuad6T28_Nu9Zf-1HjHXmuikPPaDi7isYyP0qNA6UBTGbHE4e6Se6GRQWHMwxJeLwu0FBYgvtA0E1rVGRHk4xOX_E9xREHFUuYry8Y86emzjmx9ifKzIdjMCdP1IWy8l-545_C_QAmTyHvYl5t6ca-0ndAmGZok_aHMzaKllhVRHEhYT21H8m9oIpWNo5dD8sHz4ij1U6EXiRzqbeNpfbPr90VaV7iNqh30Kw3aQTpK30hLseuHvuUTYBRNrbL5h50EaTukBmyIYGJoyd5PsGI6HiuEiLckqBJlH0KPhCCc3Zz2Y_nvOmTyDwwB0HVpbaoGwBYnWfiQ5FrQepRB-hNxKNndBIiiEWRsshZRgQJ2rtIPj5bmNUT9YWv_Am66Nqv8ZfFaReErU9pSu6Lq3AVHxCTeUzrqEMO_IYJsIXqxyys1-jkmkIWDBJbiHvz9V_saHBW-dZa5TdCiuzylKkNk6m-xBLcFpL43JLSBVQpOxYFaCnCRVTdhbyyUR3mINzZQOZ3sbq2OJ8Sm8fB7O5Y_Z_ppbkRC5GRuksOLLPa8IdPC3a4D11UozEJ0_AzOgDDNJvd85hhypG4rQeJRVA1_DBg55QmHbbMbewPI6aLMHB2VzKriqQ-WaZUt_hlnQDQPUr9k8Q-h4Ogjn212UQgrP1Gu0YalDh5AynbBA6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای نخستین بار در جهان!
کشف قله تنگه هرمز توسط اژدهای بندر</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19274" target="_blank">📅 13:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19273">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">در حالی که اساساً مزیت پهپادها در کوچکی و سطح  مقطع کم راداری آن است، ترکها رفته اند یک پهپاد غول پیکر (همین آکینچی) ساخته اند که ابعادش دو برابر یک فیل است!  طولش 20 متر و عرضش 12.3 متر و 5.5 تن هم وزن دارد!  قیمت آن هم بسیار گزاف بوده و بین 5 تا 6 میلیون…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19273" target="_blank">📅 13:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19272">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rqyn0jvG-m4fOHgCZQjlZgBIWqqr5Z_PxRQvsU6lRi3_91HMJ-5n6YXJ54-WF7mqCr0G2JUI19Ab3gH2JLYMnQ2bFWsi0Rd3o2DR7aOmQX-8EOFvP-gG3N75CbP-TiyBFrhisu89IukJLs4NZeDcNc7EVqxV1t3XAwDJx0XVUM3ZwivWDV6gTOrbfKlG1gO_1P434gu00yaBOT7MbULNhrdizV9VLpYFQydjuFIz76-wntM590d7WoOZawv9_obN3gTN3w-EJIFkx6zZEHHDCIxG2vH_n1t3jURFMs1YinargnnEMpmUqII361tRa-0ygmvTfvJH5CsqAJ8rtyIIIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان بالای مهمات پدافند موشکی آمریکایی ها در جنگ با ایران</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19272" target="_blank">📅 13:32 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
