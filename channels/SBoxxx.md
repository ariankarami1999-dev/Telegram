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
<img src="https://cdn4.telesco.pe/file/f2QgkBAyb1sOOVgTRyIA_RdXpPp5DHJFAo8jqbm8nODLAOgNW73V056vtbwpWlS5_hVNXFPpC4PqqAJkcexAs9qFerFqhJbW6BQCpEqyeArOldRXBXnPvXDoXMNWYlke3O0z3kbquRwU2VspZvKrA1bs8WkJWnD615XOXRvL_sOMNjGNc-jOCP7ANHRozIf7ohHj2swuWDO1SzP-PTkVKtaiizPsM6Lxh5pPspDT7aAywu6T_nNE1eoMEY_mRS7HCwQGiPGVzFpPG2fcLpHGGyZHaoFb-0CsWirfb4MtbSyflrXYT1ifa4buQkuYRAEDpcUmYojm9iWkoi0Lsua5LA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.2K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 18:03:59</div>
<hr>

<div class="tg-post" id="msg-18442">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سپاه پاسداران: مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی الازرق اردن درهم کوبیده شد.
🔹
رزمندگان هوافضای سپاه ساعت ۱۴:۲۰ بعد از ظهر امروز مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی دشمن در الازرق اردن را با ۱۰ فروند موشک بالستیک درهم کوبیدند.…</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SBoxxx/18442" target="_blank">📅 17:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18441">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سپاه پاسداران: مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی الازرق اردن درهم کوبیده شد.
🔹
رزمندگان هوافضای سپاه ساعت ۱۴:۲۰ بعد از ظهر امروز مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی دشمن در الازرق اردن را با ۱۰ فروند موشک بالستیک درهم کوبیدند.
🔹
در صورت تکرار تجاوز ارتش تروریستی آمریکا سایر پایگاه‌های آمریکا! در منطقه از آتش سنگین ما در امان نخواهد بود.</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/SBoxxx/18441" target="_blank">📅 17:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18440">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزیر دفاع یونان، نیکوس دندیاس:
یونان از این موضوع که ترکیه جنگنده‌های F-35 را دریافت کند، راضی نیست. یونان از این موضوع که ترکیه موتورهایی برای یک هواپیمای نسل جدید دریافت کند، راضی نیست.
ما یک سوال مطرح می‌کنیم: آیا این موضوع به منافع واقعی ایالات متحده آمریکا خدمت می‌کند؟ بله یا خیر؟ و البته، پاسخ این سوال بر عهده مردم آمریکا و دولت آمریکا است.
این موضوع قطعی است که برای دولت ایالات متحده، ناتو و به ویژه ثبات در دریای مدیترانه شرقی، از اهمیت بالایی برخوردار است.
بنابراین، آیا ارائه یک پلتفرم به یک کشور در دریای مدیترانه شرقی، بدون این شرط که این پلتفرم نباید علیه یک عضو متحد دیگر مورد استفاده قرار گیرد، به نفع ایالات متحده است یا خیر؟</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SBoxxx/18440" target="_blank">📅 15:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18439">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ارتش اردن اعلام کرد که ۸ موشک بالستیک ایرانی که به سمت خاک این کشور شلیک شده بودند را رهگیری کرد.</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/18439" target="_blank">📅 15:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18438">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انفجار در شیراز و کرمان</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/18438" target="_blank">📅 15:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18437">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">— دونالد ترامپ:  «به نظر من، اسرائیل نیروهای خود را از جنوب لبنان خارج خواهد کرد.»</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/18437" target="_blank">📅 14:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18436">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/18436" target="_blank">📅 14:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18435">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‍
💢
وزارت خارجه: حملات جنایتکارانه آمریکا نقض فاحش بندهای یک و پنج یادداشت تفاهم است
🔹
وزارت امور خارجه حملات تجاوزکارانه ارتش تروریستی آمریکا طی بامداد پنج‌شنبه ۱۸ خردادماه به چندین نقطه در استان‌های ساحلی جنوب و نیز دو پل در استان‌های شرقی در مسیر ریلی…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/18435" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18434">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/18434" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18433">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مانور کلاهک موشک ایرانی که دیشب به پایگاه آمریکا در کرانه های جنوبی خلیج فارس اصابت کرد.</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SBoxxx/18433" target="_blank">📅 14:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18432">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e86d2fb7c7.mov?token=oWcgHU7KjyXHoEb-R538kvq_Ail47fHTTyi6KWLmc9bgR16EUoaWF4mKLnjGw4pM6eY9-TS4CBd9PogMzlXM9elYLTHNjCVOPHrKTN2x7jCtOtPn8vUUZqa3kiPNYzgNgTWmFd5z_QS8fdAqkbpqLi5DVPM4TKrqhRAppURO6DWy4sEq9hYMVytbk5Ydxe_ZqdiKQXzVQCD0SgHid8ZRZ2tkcx5Mw3L4g9E52a2F2Tw_E0cTdwOPRSdzY8mpWZGZ-bq1xr0k7QedXpDcDuMNTJ6dBqv7mP0VhUWetwH_8C7ANLMeuQnKw0kJVQozqdmAPxX-vfPYHVgayv-XDbj7bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e86d2fb7c7.mov?token=oWcgHU7KjyXHoEb-R538kvq_Ail47fHTTyi6KWLmc9bgR16EUoaWF4mKLnjGw4pM6eY9-TS4CBd9PogMzlXM9elYLTHNjCVOPHrKTN2x7jCtOtPn8vUUZqa3kiPNYzgNgTWmFd5z_QS8fdAqkbpqLi5DVPM4TKrqhRAppURO6DWy4sEq9hYMVytbk5Ydxe_ZqdiKQXzVQCD0SgHid8ZRZ2tkcx5Mw3L4g9E52a2F2Tw_E0cTdwOPRSdzY8mpWZGZ-bq1xr0k7QedXpDcDuMNTJ6dBqv7mP0VhUWetwH_8C7ANLMeuQnKw0kJVQozqdmAPxX-vfPYHVgayv-XDbj7bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مانور کلاهک موشک ایرانی که دیشب به پایگاه آمریکا در کرانه های جنوبی خلیج فارس اصابت کرد.</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SBoxxx/18432" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18431">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_enJKiudEApCnYPvDN-e-SH13VACcROvSuDI3dZiGvNfeKT5jg-hJfm0ECm7A0xV58pqAtHEe87QygWfbRp9m54tj5tO-Mpvyv8VHOWun4ej9zax5zjoT3bVnCl89V8Flxh6XKzeXzU_Qe7LIP4itfaBcHXax3qN4TKIT5Shfp3_Nyl7MxuA3XMatyhnpP-4Zf0lIiaXscWQXhOp2It4PKL8VJETjBMq7wUsGuM6ZNNPGsfG3uCdDigLkcbgQYPMGIkyPpYxw33VrXHPpNTsX5hRsyQL8dEyvLmLifgSis_RIaG6bBTUHAbRFYw6JZDazppcHOd2ArO2CceYYNJ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با اینکه ترامپ برای عزیمت به ترکیه آماده می‌شد، مارکو روبیو، وزیر امور خارجه، و پیتر هیگست، وزیر دفاع، در دفتر بیضی‌شکل کاخ سفید، او را در جریان گزارش‌هایی قرار دادند مبنی بر اینکه ایران موشک‌های کروز و پهپادها را به سمت کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده و به سه فروند از این کشتی‌ها خسارت وارد کرده است.
ترامپ پرسید که آیا تهران هنوز به دستیابی به یک توافق نهایی متعهد است یا خیر، و پس از مشورت با مشاوران ارشد امنیت ملی خود، به این نتیجه رسید که اینطور نیست.
این جلسه، نقطه‌ی عطفی بود که باعث شد او طرح آتش‌بس را کنار بگذارد و مجوز حملات نظامی جدید و اعمال فشار اقتصادی مجدد بر ایران را صادر کند.
منبع: WSJ</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/18431" target="_blank">📅 13:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18430">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انفجار در بوشهر</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/18430" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18429">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuV70_bdLddf3S5qERSVvw9bAaZNYCoV33T23j1zATvHYNI6dPcTVvJinthAl3kg1lOlavia45uS2X2og8RxSxZiiA68cdWpzdzlO2WVIZmb3gTcWUAXkU2zCSwPUEo3VZDeDPmg70-qSZSu8XrPHLL1UvzP14FVpzkXFiBVjVlmbJU0SUMI1QSI45OhwzC_bfESB1JmzcZHVIYQnAxp_wnHOju3vLxOTC9kR0vWB2KU2rIhK2ebgQhi7qJg3BNcplKScxtlwEq7Efpx9BUtqHVLk81DDaPy-eZh4aV6eu8YpE0cO6myzmSD-BBiW_ju0ajuWp8TTxvEGKIIMyJ1LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.  پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/18429" target="_blank">📅 13:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18428">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عمدا جاهایی را دارند میزنند که در شکستن محاصره نقش داشتند و کریدورهای جایگزین برای ایران حساب می شدند.</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/18428" target="_blank">📅 12:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18427">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
🇮🇶
🇮🇷
✈
هواپیمای حامل پیکر آیت‌الله سید علی خامنه‌ای و خانواده به فرودگاه مشهد رسید.
📮
@IRKhbarFori</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/18427" target="_blank">📅 11:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18426">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبارفوری جنگ امریکا فوری/ خبرفوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3075b8e37.mp4?token=UhDpI_T7Bi2JukK4dREwAscXJyTYNz0NBy2fTmAbT40ZLQk_pnH8aDRrhHNNwEDOGl38QDhcq6ESCOwTNiqQu-FpOUh2tCZxetGgztntFkbB0akIqPDC_bi_IZnfXacfN6IJDdHP8bTCjVuRVXYftjt2-kvzHTUleVM9B4q_QzK3aXsOu8DFdId_6nRbj_cGVM3u0_kHOts91MbvE49KR8D_fAqf4qDTTfGQO4vcK2aJHNAthl4sMhHz8K5HJYr33rApC2og9FW9xFisIv_OzFBlVJmUrmk7Cqz8odYvZHBbMg6MGjTdChTaxFmiD5uGKKZWW_bp13XTd_uMJDVwqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3075b8e37.mp4?token=UhDpI_T7Bi2JukK4dREwAscXJyTYNz0NBy2fTmAbT40ZLQk_pnH8aDRrhHNNwEDOGl38QDhcq6ESCOwTNiqQu-FpOUh2tCZxetGgztntFkbB0akIqPDC_bi_IZnfXacfN6IJDdHP8bTCjVuRVXYftjt2-kvzHTUleVM9B4q_QzK3aXsOu8DFdId_6nRbj_cGVM3u0_kHOts91MbvE49KR8D_fAqf4qDTTfGQO4vcK2aJHNAthl4sMhHz8K5HJYr33rApC2og9FW9xFisIv_OzFBlVJmUrmk7Cqz8odYvZHBbMg6MGjTdChTaxFmiD5uGKKZWW_bp13XTd_uMJDVwqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇶
🇮🇷
✈
هواپیمای حامل پیکر آیت‌الله سید علی خامنه‌ای و خانواده به فرودگاه مشهد رسید.
📮
@IRKhbarFori</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/18426" target="_blank">📅 11:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18425">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبارفوری جنگ امریکا فوری/ خبرفوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25cd71dba4.mp4?token=CqOZctJ33ZafaJKJ-FZF8go01dGwVISTCIy7AVQERBlXZ3qJKJUhzObkmA7BidwCnvbq-jxMgeEW_Jng24Q9HRROdnIJ8Dva7n7-98eqqNMAUthXLv3oCK0uiebOi89CyPhb5VlNuERJdnG2fgKq_0cV_fluXh8syhxC2GineQK1s_bO2OszvuMzSgT_YK2XzpV7DcWd-X9XZVcU7q2TUsSISr0iHi6941xqgGZtzBbrsALgppFRPTxREPYkX7cMi60t9LB6K6YPIoQ22_HJUYP801iM0zy12sihCERgKmkV0ms590VjeC1iv0CUg8CfoigXq8DmiFm0ceAqAKY5hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25cd71dba4.mp4?token=CqOZctJ33ZafaJKJ-FZF8go01dGwVISTCIy7AVQERBlXZ3qJKJUhzObkmA7BidwCnvbq-jxMgeEW_Jng24Q9HRROdnIJ8Dva7n7-98eqqNMAUthXLv3oCK0uiebOi89CyPhb5VlNuERJdnG2fgKq_0cV_fluXh8syhxC2GineQK1s_bO2OszvuMzSgT_YK2XzpV7DcWd-X9XZVcU7q2TUsSISr0iHi6941xqgGZtzBbrsALgppFRPTxREPYkX7cMi60t9LB6K6YPIoQ22_HJUYP801iM0zy12sihCERgKmkV0ms590VjeC1iv0CUg8CfoigXq8DmiFm0ceAqAKY5hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇶
🇮🇷
🎬
هم‌اکنون هواپیمای حامل پیکر آیت‌الله خامنه‌ای و خانواده، فرودگاه نجف را به مقصد مشهد ترک کرد.
📮
@IRKhbarFori</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/18425" target="_blank">📅 11:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18424">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">چرا درگیری بعدی ایران و آمریکا احتمالاً جهش تاریخی نفت را تکرار نمی‌کند؟
درگیری نظامی میان ایران و آمریکا همواره یکی از بزرگ‌ترین ریسک‌های ژئوپلیتیکی بازار انرژی بوده است. هرگونه تهدید علیه تنگه هرمز، مسیر عبور بخش قابل توجهی از صادرات نفت خلیج فارس، در گذشته می‌توانست باعث جهش شدید قیمت نفت شود؛ زیرا بازار به اختلال ناگهانی در عرضه واکنش نشان می‌داد. اما شرایط بازار انرژی امروز نسبت به گذشته تغییرات مهمی کرده است و درگیری احتمالی آینده لزوماً به معنای تکرار شوک‌های نفتی تاریخی نخواهد بود.
یکی از مهم‌ترین عوامل، ایجاد مسیرهای جایگزین برای انتقال نفت در خارج از تنگه هرمز است. کشورهای تولیدکننده منطقه، به‌ویژه عربستان سعودی، امارات و عراق، در ماههای اخیر سرمایه‌گذاری‌هایی برای توسعه خطوط لوله، پایانه‌های صادراتی جایگزین و افزایش ظرفیت انتقال خارج از این آبراه انجام داده‌اند. این زیرساخت‌ها به بازار اجازه می‌دهد بخشی از نفت منطقه حتی در صورت اختلال در هرمز همچنان به بازارهای جهانی برسد. بنابراین، حساسیت بازار نسبت به تهدید بسته شدن کامل تنگه هرمز نسبت به گذشته کاهش یافته است.
عامل دوم، افزایش ظرفیت عرضه و انعطاف‌پذیری بیشتر بازار نفت است. تولیدکنندگان عضو سازمان کشورهای صادرکننده نفت (OPEC) و متحدان آن در قالب ائتلاف اوپک پلاس، در مقاطع مختلف توانسته‌اند با تغییر سیاست تولید، بخشی از شوک‌های عرضه را مدیریت کنند که یک نمونه جاری آن را با 3 بار افزایش تولید اخیر اوپک که آخرینش هفته پیش تصویب شد مشاهده می کنید. همچنین رشد تولید نفت شل در آمریکا باعث شده بازار جهانی نسبت به دهه‌های گذشته تنها به خاورمیانه وابسته نباشد.
از سوی دیگر، سمت تقاضا نیز تغییر کرده است. رشد خودروهای برقی، افزایش بهره‌وری انرژی، سیاست‌های کاهش مصرف سوخت‌های فسیلی و تغییر الگوی رشد اقتصادی چین باعث شده رشد تقاضای نفت کندتر شود. در نتیجه، هرگونه اختلال کوتاه‌مدت در عرضه ممکن است بیشتر به یک شوک موقت قیمتی تبدیل شود تا آغاز یک روند انفجاری پایدار.
موضوع مهم دیگر، پدیده «نابودی تقاضا» است. اگر قیمت نفت به‌سرعت افزایش یابد، مصرف‌کنندگان و صنایع واکنش نشان می‌دهند: استفاده از انرژی‌های جایگزین افزایش می‌یابد، فعالیت‌های انرژی‌بر کاهش پیدا می‌کند و اقتصاد جهانی با فشار رکودی مواجه می‌شود. تجربه بحران‌های قبلی نشان داده است که قیمت‌های بسیار بالا خودشان عاملی برای کاهش مصرف هستند.
البته این به معنای بی‌اهمیت شدن ریسک افزایش بهای نفت نیست. یک درگیری گسترده که تولید نفت ایران و دیگر کشورهای نفتی یا زیرساخت‌های اصلی منطقه را هدف قرار دهد، همچنان می‌تواند باعث جهش کوتاه‌مدت قیمت شود. بازارها به اخبار جنگی با سرعت واکنش نشان می‌دهند و عامل روانی می‌تواند قیمت‌ها را برای مدتی بالا ببرد.
اما تفاوت امروز با گذشته این است که بازار نفت ابزارهای بیشتری برای جذب شوک دارد. مسیرهای جایگزین صادرات، ظرفیت‌های ذخیره‌سازی، تولیدکنندگان جدید و تغییر رفتار مصرف‌کنندگان باعث شده‌اند احتمال تکرار جهش‌های تاریخی نفت در اثر یک درگیری منطقه‌ای کاهش یابد. در سناریوی درگیری بعدی ایران و آمریکا، احتمالاً واکنش بازار بیشتر یک جهش سریع و محدود خواهد بود، نه یک بحران انرژی مشابه دهه‌های گذشته.</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/18424" target="_blank">📅 11:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18423">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ارتش ایران:  «ما با استفاده از پهپادها، سامانه‌های پدافند هوایی پاتریوت در کویت، یک مرکز هشدار اولیه در قطر و تاسیسات ذخیره‌سازی سوخت ارتش آمریکا در بحرین را هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/18423" target="_blank">📅 11:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18422">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
حملات پهپادی ارتش به پایگاه‌های آمریکا در منطقه
🔺
روابط‌عمومی ارتش:  در پی تجاوز ارتش تروریستی آمریکایی مناطقی از کشور و یگان‌های ارتش و در پاسخ به آن جنایت،  ساعتی قبل و در ادامۀ حملات ارتش به پایگاه‌های آمریکا در منطقه، سامانۀ پاتریوت در کویت، آنتن ماهواره‌ای…</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/18422" target="_blank">📅 11:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18421">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">به گزارش اکسیوس، پهپادهای ایرانی دو کشتی تجاری را در تنگه هرمز هدف قرار داده‌اند.</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/18421" target="_blank">📅 11:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18420">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شبه نظامیان آزادی بلوچ یک حمله با بمب دست‌ساز (IED) و سپس یک کمین سنگین را علیه کاروانی متشکل از سه خودروی نیروهای امنیتی پاکستان در منطقه سچی واشوک، بلوچستان، انجام دادند.  خسارات سنگین جانی گزارش شده است.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/18420" target="_blank">📅 10:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18419">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مقر تیپ 110 سلمان فارسی نیروی زمینی سپاه در زاهدان بمباران شده است.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/18419" target="_blank">📅 10:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18418">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNaPh8z56akQyPnEsqG1hfDBMKdk7jirWEsA6KAOmAKX766xmvPEXu_KIRNfb3L9-jVXXWvzt8gFJyDuGddL_i4vx8_4LsOUVwt2t9IM_NowMDB1h1R2aHj_w2aU0fJ_ptrUDHr7nTeN4Dzk0R8at4E9OemqsRm6XV7mwjalWRUxLoWponnOhJpCFXeX7a1rJz11hCE3dfvOLOK-sVbKK1xerKPojUygWhR-4BVG6zjHsk0xjkWNEdzuvfjXQnbNGGBeD_L-NzuaePJOMeJbMmidSknY25Ug8mOZlEVdxfIfYMcqEmOdS70JAn2w_hhlfwbAbmBiX4F76M0sI7A_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح پایینی قرار دارد و ریسک پذیری پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/18418" target="_blank">📅 10:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18417">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18417" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 4
پنج شنبه 9 جولای 2026</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18417" target="_blank">📅 10:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18416">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بیانیه سپاه پاسداران انقلاب اسلامی   بسم الله قاصم الجبارین  قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ  ملت شریف ایران، ملت کریم و مجاهد عراق؛ آفرین بر شما مردمان مومن و بصیر…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/18416" target="_blank">📅 09:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18415">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کاخ سفید برای یک درگیری بالقوه طولانی‌مدت با ایران بر سر تنگه هرمز آماده می‌شود.
مسئولان آمریکایی می‌گویند مدت زمان این درگیری به اقدامات بعدی تهران بستگی دارد.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18415" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18414">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4mBjQyQ766AeJBgMMuHiCdKla_a25YMkYru5LGsYTH0xX2iiMEu8hpOArwN6rIvkELfW-EndYkK2MuUwKpHfrwbp2kI4oPiSwXUU3MLoQsoIHMfu8Yv1X9lXy_2PdMmOiMg0Qc5VZzIUu4_2tKU-QhQbVjY1gC4FAolCz4Vct6VrBz7sqkdthHKKeUCQF-siezZ_hY66__7QkA2Thh3816EIUX8CpMyyosImcu2Wfxea8nZmCv8VQkBVUtUiR25DZv_P3CHz0HOffNSgjXeGn7E8Sr4FsYiiLJFgW9QxN9XB8I9ie5GOmHfkDYrkLe1Ep2ge7MpHMT2cG6ovpROcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمدا جاهایی را دارند میزنند که در شکستن محاصره نقش داشتند و کریدورهای جایگزین برای ایران حساب می شدند.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/18414" target="_blank">📅 08:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18413">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">راه آهن جمهوری اسلامی ایران:   به دنبال حمله جنایتکارانه دشمن آمریکایی بامداد امروز به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.  برنامه ریزی لازم برای جابجایی مسافران محترم قطارهای متوقف شده در این مسیر، از…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/18413" target="_blank">📅 08:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18412">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">راه آهن جمهوری اسلامی ایران:
به دنبال حمله جنایتکارانه دشمن آمریکایی بامداد امروز
به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.
برنامه ریزی لازم برای جابجایی مسافران محترم قطارهای متوقف شده در این مسیر، از طریق ناوگان مسافری جاده ای به مشهد مقدس انجام شده است.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18412" target="_blank">📅 08:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18411">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">توییت محمدسامثینگ قالیباف</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/18411" target="_blank">📅 08:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18410">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeARId2g1HvUIYrFr9d3BLFDAqLwIWRIMP8Rv2dV-9OpreHFP4nrSVi8ptNc7-Wf6PwsQmPPCHcOlg1wrzbJe2RZd57PQG6RJlzlhgn-vXvjN3MOMovvEbcTibNxsWYIZSVaMu90Isc1gPu24ShrFYy0LUjSZ3gnKS3A_LZEKY9FtZ7kiCDmM-kzurehXyno05x8U8nrLnK6DLY4aYCBygc4V0pXIBAb8srlDq5j8I0AsIHN73Dr4pJMkqBZJMyTtLZPaZxXRbh0_PoBKHHgC63AQfk4hZhaMWMe2m1v4hrraRw7LTU4NJ6suk6Tzv-BqF9nZ2nnDCk__06QuFUacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت محمدسامثینگ قالیباف</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/18410" target="_blank">📅 08:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18409">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ایران به اهداف دشمن با نسبتی حداقل دو به یک حمله خواهد کرد -   تلویزیون خبرگزاری ایران، با استناد به یک منبع امنیتی آگاه.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/18409" target="_blank">📅 08:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18408">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بیانیه سپاه پاسداران انقلاب اسلامی
بسم الله قاصم الجبارین
قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ
ملت شریف ایران، ملت کریم و مجاهد عراق؛
آفرین بر شما مردمان مومن و بصیر و وفادار که با موقع‌شناسی و تشییع بی‌نظیر در تاریخ جهان قدر و منزلت ولایت الهی و عشق عمیق متقابل مردم و والی اسلامی با مرام امیرالمومنین (ع) را به رخ جهان کشاندید و با شعارهایتان یادآور شدید که هزینه تعدی به مرجعیت و ولایت فقیه مسلمانان بسیار سنگین خواهد بود.
هرچند این تشییع باشکوه به ویژه ۲۳ ساعت تشییع عاشقانه در گرمای شدید سرزمین عراق حبیب، مستکبران کاخ‌نشین را وحشت‌زده و آنها را به واکنش عجولانه به این قدرت نمایی مردم واداشت و آمریکای عهد‌شکن با زیر پا گذاشتن همه تعهدات بار دیگر نقاط متعددی از استان‌های ساحلی جنوب ایران و در اقدامی ضد مردمی دو پل در استان‌های شرقی به سوی مشهد مقدس را مورد تجاوز قرار داد تا اخبار این حماسه بی‌نظیر را تحت شعاع قرار دهد و این رویداد الهام بخش را از نظر مردم جهان پنهان دارد، غافل از اینکه این جنایات مردم جهان را بیدارتر و آنها را برای نقش آفرینی در مبارزه‌ با شیطان بزرگ مصمم‌تر خواهد کرد.
رزمندگان اسلام تجاوزهای ارتش کودک‌کش آمریکا را بی‌پاسخ نخواهند گذاشت.
در اولین مرحله از پاسخ تنبیهی علیه پیمان‌شکنان آمریکایی، رزمندگان نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی، ساعتی پس از حملات دشمن و نقاط مختلف کشور، زیرساخت‌ها و تاسیسات مهم دو پایگاه‌های استعماری اشغالگران آمریکایی در عریفجان و علی السالم کویت و جفیر و شیخ عیسی در بحرین را در هم کوبیدند.
سپاه پاسداران انقلاب اسلامی به ارتش کودک‌کش آمریکا اخطار می‌کند که در صورت تکرار تجاوز پاسخ‌های کوبنده ما به سایر پایگاه‌های آمریکایی در منطقه توسعه خواهد یافت.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18408" target="_blank">📅 08:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18406">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">به نظر شما ترامپ با این سه سگ (اردوغان، فیدان، کالین) چه صحبتی می تواند داشته باشد آن هم وقتی که جولانی هم دارد به اینها می پیوندد؟!</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18406" target="_blank">📅 02:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18405">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O84D0BgyQMosrRndKTDxK2i5UcRGBKUv76DxCb5vXfcgX4B2D_aQ8qP6tceiSCkYgP2KsUkCaZL68ixXo71MnmX6bbMFCu4QWE5fx-NA3H8V2rpm7s8731jPDJNLzrQfI9MehWR-b_St9d8r6uDNGnbnOE0JD3rcJQAwCqAdo9oIO6NF01ydi6FS9-47MgzZYXlWJPVlCw4V7W5DOYnqNRNPXlLkLpAwlO4xbeaAa59uH7V4GBf4XB_LyojDFmU5mWANDRM6MK8rWyz0mInU0aEdhRVhZJogXjsreEk1yZ5gkNbkJLZLU_NxvNYdY361wJuFr_3M8KY6XmgY6-zG5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در حال انتشار زنده ویدئوهایی از حملات آمریکا به ایران در امشب است</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18405" target="_blank">📅 01:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18404">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مقر تیپ 110 سلمان فارسی نیروی زمینی سپاه در زاهدان بمباران شده است.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18404" target="_blank">📅 00:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18403">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">زاهدان</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18403" target="_blank">📅 00:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18402">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ابوموسی</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18402" target="_blank">📅 00:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18401">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تماس شبکه خبر با اژدهای بندر!</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18401" target="_blank">📅 00:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18400">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZARCqazXy1s47Jp210TjO35mmnLpweN5woBScNpIQ28nX9MGt7NCY9JnJDN7qQ_Wlzm5u3fN93k84PpOhILsTOSKr4jsDWKwfopalSav1fUrxV_iyt95zSdBBOiSUQuxTA7JuX5t402C5BZ0IBLEIt_ak84Hv9cDDv4ve5cY6GHOs1pM3oORGMTjsaq08rwJqhWhu8Vh6r30fxJgZmcrQeTfmsOO5WntTB-WFrExN-Ob6pzQrCfFp-_dx0IC6ldR3eMy4pLgFP6MXWQm7IqoJ7xMxyc8oM7KMlcHsBJ3JrHN9HcVpMu6o2FBxoVyDG5y_wjGjmVEr29mFhejU3D4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18400" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18399">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گفته می شود تا 200 هدف امشب مورد اصابت موشک ها و بمب های آمریکایی ها قرار گرفته است.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18399" target="_blank">📅 00:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18398">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انتشار اخباری از آماده شدن پرتابگرهای موشکی سپاه</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18398" target="_blank">📅 00:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18397">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خارک، قشم</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18397" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18396">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تسنیم:
براساس برخی اخبار غیررسمی، پایگاه امام علی نیروی دریایی سپاه در چابهار توسط جنگنده‌های آمریکایی مورد هدف قرار گرفته</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18396" target="_blank">📅 00:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18395">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">عربستان سعودی در حال پیشبرد طرحی برای کنار زدن اسرائیل از کریدور اقتصادی هند-خاورمیانه-اروپا، معروف به پروژه «راه‌آهن صلح»، با تغییر مسیر این کریدور از طریق سوریه به جای اسرائیل است.
دو منبع به نقل از جروزالم پست</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18395" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18394">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کی حضرات می خواهند بفهمند که ادامه این مسیر احمقانه یعنی نابودی زیرساخت های باقیمانده کشور و سپس ایجاد یک دولت شکست خورده و نهایتاً تجزیه ایران؟!</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18394" target="_blank">📅 00:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18393">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کی حضرات می خواهند بفهمند که ادامه این مسیر احمقانه یعنی نابودی زیرساخت های باقیمانده کشور و سپس ایجاد یک دولت شکست خورده و نهایتاً تجزیه ایران؟!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18393" target="_blank">📅 00:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18392">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0qmIgI0Rn2o7Px7wWnmJxHNEsP70ZTxWspSyqmrca7Xr6vmMsMmlOAOppJ6rY1D1xAkk0iJuNGH2HFSxza_XRJR-segoe-7zJCAwPMNOnHCuaU38bfiZU_i6cruJ0gGzyWRc8zkF3KX1pla90Agv6sriC51MVscBoQeKOuxmF0SiQKcLkMHpqCUmXnD63sHCQjuLOwtGouQAxDHo_9i3TzMohsYj1DLHlYCQu4dJ7EE8YbdQ_e_0iTFXgqHZkKBGcFfINAuFAPGraYe4Fhl59RSxE76DG_WoFpMtYtIcFsrYIkTpwFuY_1Bn6kaMcpX4RobUtU42wLbSYxsEPJw_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروگاه برق چابهار ه زده شد و برق قسمتهایی از شهر قطع شده.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18392" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18391">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حمله به پالایشگاه ها هم آغاز شد...</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18391" target="_blank">📅 00:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18390">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حمله به پالایشگاه ها هم آغاز شد...</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/18390" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18389">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بوشهر، لاوان، چابهار….</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18389" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18388">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18388" target="_blank">📅 23:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18387">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">At the direction of the Commander in Chief, U.S. Central Command forces have started conducting additional strikes against Iran to further degrade their ability to threaten freedom of navigation in the Strait of Hormuz. The United States is holding Iran accountable…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18387" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18386">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromU.S. Central Command</strong></div>
<div class="tg-text">At the direction of the Commander in Chief, U.S. Central Command forces have started conducting additional strikes against Iran to further degrade their ability to threaten freedom of navigation in the Strait of Hormuz. The United States is holding Iran accountable for recent unjustified aggression against commercial shipping and civilian crews freely navigating a vital international waterway.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18386" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18385">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خبرگزاری آکسیوس :
ارتش آمریکا امشب حملات بسیار سنگین تری را به ایران انجام خواهد داد.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18385" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18384">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18384" target="_blank">📅 23:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18383">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">به نظر شما ترامپ با این سه سگ (اردوغان، فیدان، کالین) چه صحبتی می تواند داشته باشد آن هم وقتی که جولانی هم دارد به اینها می پیوندد؟!</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18383" target="_blank">📅 22:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18382">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">در ساعات اخیر، ایالات متحده شروع به استقرار مجدد هواپیماهای تانکر سوخت‌رسان در اسرائیل و خاورمیانه کرده است.
— خبرگزاری اسرائیل</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18382" target="_blank">📅 20:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18381">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">واکنش غریب‌آبادی، معاون وزیر خارجه به تهدید ترامپ به حملات بیشتر:    با ترامپ جنایتکار و قاتل باید با زبان خودش صحبت کرد، ظاهرا زبان زور را بهتر می‌فهمد   کاظم غریب‌آبادی، معاون حقوقی و بین‌الملل وزارت امور خارجه در شبکه اجتماعی ایکس نوشت: اظهارات امروز ترامپ،…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18381" target="_blank">📅 20:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18380">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">واکنش غریب‌آبادی، معاون وزیر خارجه به تهدید ترامپ به حملات بیشتر:
با ترامپ جنایتکار و قاتل باید با زبان خودش صحبت کرد، ظاهرا زبان زور را بهتر می‌فهمد
کاظم غریب‌آبادی، معاون حقوقی و بین‌الملل وزارت امور خارجه در شبکه اجتماعی ایکس نوشت: اظهارات امروز ترامپ، از توهین به ملت ایران تا تهدید به حملات بیشتر، نه نشانه اقتدار، بلکه اعتراف به شکست سیاستی است که سال ها بر زور، تحریم و تهدید بنا شده و نتوانست ملت ایران را به زانو درآورد. با ترامپ جنایتکار و قاتل باید با زبان خودش صحبت کرد، ظاهرا زبان زور را بهتر می فهمد!</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18380" target="_blank">📅 20:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18379">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ:  اردوغان، طرفدار پروپاقرص نتانیاهو و اسرائیل نیست.  اما او در آن جنگ دخالت نکرد.  او می‌توانست به راحتی وارد آن جنگ شود، اما به درخواست من، از آن جنگ کناره‌گیری کرد.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18379" target="_blank">📅 20:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18378">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ:
اردوغان، طرفدار پروپاقرص نتانیاهو و اسرائیل نیست.
اما او در آن جنگ دخالت نکرد.
او می‌توانست به راحتی وارد آن جنگ شود، اما به درخواست من، از آن جنگ کناره‌گیری کرد.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18378" target="_blank">📅 20:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18377">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اظهارات ترامپ درباره ایران:  به نظر من، جنگ با ایران دوباره آغاز نخواهد شد.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18377" target="_blank">📅 20:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18376">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فوری | ترامپ: حجم زیادی نفت از تنگه هرمز عبور می‌کند و ما به دنبال یک جنگ طولانی نیستیم.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18376" target="_blank">📅 20:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18375">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فوری | ترامپ: حجم زیادی نفت از تنگه هرمز عبور می‌کند و ما به دنبال یک جنگ طولانی نیستیم.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18375" target="_blank">📅 20:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18374">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فوری | ترامپ: حجم زیادی نفت از تنگه هرمز عبور می‌کند و ما به دنبال یک جنگ طولانی نیستیم.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18374" target="_blank">📅 20:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18373">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ خیلی صریح محمدباقر قالیباف رئیس مجلس ایران را به ترور و حذف فیزیکی تهدید کرده و او را "محمد یه چیزی..." (Muhammad Something) می نامد و با تمسخر می گوید اسم نصف ایرانی ها محمد یه چیزی است و ما می توانیم آنها را از فضا شناسایی کنیم و اگر نزدیک منطقه ذخیره…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18373" target="_blank">📅 20:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18372">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ درباره ایران:
می‌دانید؟ ممکن است من کشته بشوم.
من هدف شماره یک آن‌ها هستم.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18372" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18371">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اظهارات ترامپ درباره ایران:  آنها با نرخ تورم ۳۵۰ درصدی مواجه هستند. زمانی که جنگ آغاز شد، این نرخ ۵ تا ۶ درصد بود.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18371" target="_blank">📅 20:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18370">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اظهارات ترامپ درباره ایران:
آنها با نرخ تورم ۳۵۰ درصدی مواجه هستند. زمانی که جنگ آغاز شد، این نرخ ۵ تا ۶ درصد بود.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18370" target="_blank">📅 20:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18369">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ در آنکارا:
شرکت‌های لاکهید و راین‌متال از همکاری خود برای ساخت سامانه‌های موشکی تاکتیکی ارتش خبر دادند.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/18369" target="_blank">📅 19:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18368">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ایران به اهداف دشمن با نسبتی حداقل دو به یک حمله خواهد کرد -   تلویزیون خبرگزاری ایران، با استناد به یک منبع امنیتی آگاه.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/18368" target="_blank">📅 19:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18367">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ایران به اهداف دشمن با نسبتی حداقل دو به یک حمله خواهد کرد -
تلویزیون خبرگزاری ایران، با استناد به یک منبع امنیتی آگاه.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/18367" target="_blank">📅 19:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18366">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بر اساس بیانیه روابط عمومی ارتش ۸ نفر از نیروهای هوایی و دریایی ارتش جمهوری اسلامی ایران در پی حملات بامداد امروز رژیم آمریکا به بندرعباس و بوشهر به شهادت رسیدند.  سروان علی معینی از پایگاه شهید یاسینی بوشهر، ستوانیکم علی مهدی‌زاده، ستوانسوم حامددورای، استواردوم…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18366" target="_blank">📅 19:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18365">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwVQzRvLutcLs4ktuL0Foni4bbpvAHTOJNCWObC9kgIDykyExfyJvNPizATqhK97o49jad97N3FwIQuAVuGAcZFNe2dWJlctzPwn4WrZl3KGovw2dI_8aKeLaefdmS1vRjBv4OvgwwpdqDp3v3SMyVC_IZQXCISOBeMmRmEnzrMdYR2Mx7SkzYUhh18No0XBR8IuacZURY_9pubKwVuCjSlytit3qIJC4WWl04Ohj6P0o1G0TuXmNY0SFHEhJPn_40NFqVAL4s527OjVK1IwkngrrvsA-G-k1q_44jMVWczqIS9EDnoD4vFJV9XnKWGREmMc1lfQDKVMkOiQ-yxxvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس بیانیه روابط عمومی ارتش ۸ نفر از نیروهای هوایی و دریایی ارتش جمهوری اسلامی ایران در پی حملات بامداد امروز رژیم آمریکا به بندرعباس و بوشهر به شهادت رسیدند.
سروان علی معینی از پایگاه شهید یاسینی بوشهر، ستوانیکم علی مهدی‌زاده، ستوانسوم حامددورای، استواردوم امیرحسین قاسمی، استواردوم علیرضا زارعی ثانی و استواردوم علیرضا بالیده از پایگاه شهید عبدالکریمی بندرعباس و ناواستواردوم شهاب امیدی بزی و ناوی محمدجواد روانفر از منطقه یکم نیروی دریایی ارتش، در این حملات، به مقام شهادت نایل آمدند.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18365" target="_blank">📅 19:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18364">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ درباره احتمال اعزام نیروهای زمینی به ایران:
«چرا باید الان وارد عمل شوم؟ زمانی وارد می‌شوم که یا آن‌ها کاملاً از بین رفته باشند یا توافقی حاصل شده باشد.»</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18364" target="_blank">📅 18:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18363">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0Zkt5Y3ffcWC8uZawVJsizbdHtXUXFspyjktuf3nIWx5txLLTt5mmMYNnk98ae79ROJm818BnJDIAI-MnMpzQ7fTWSIVM2oXp3Gp6fhtrBK0NaC4RgE6sWgmdLjwDLkt4Wx4coHTNGoC9By4SMXjocv-i3Ot-4Mr7xjPXdQhh7s4gbL_1KddDv-IR70v-jF1bysYsGVg1DC96hS2J0-SZ8UmLlI1-1qtr8GddG1plvWRLsj0V1hqxdff7-Wg8k8Ab-wNloQNPtDEAQuqAd6vssiU0CpHNGQSjifCKgV_6DYPemzfi-Hc0VwCt7iewUFCgS6kh4rY_vDndrYSsfBFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک در سطح بسیار بالا قرار دارد و ریسک گریزی آشکاری در بازارهای مالی جریان دارد.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/18363" target="_blank">📅 18:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18362">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6UonUyL8LHQet0SMSwHQiOdSnvaXWRITKaKuVJ6xTtxxfW5eBFZBOskXv00mzVkxiF0xUEqNPgKhF7Cpun-w91VezwZXFpVd4OyydfkSBU2A7OFECNh7T2F0qTjmdeQe61_r9W4uvyxl1DZCNDMef7089RQI1Q-3hpeeBbbE6zLFt7m5awFUT-D4sdwpUc9PI4cgG-liT6wopU4Tb5z1XsKK-V9e1jRdXuh1U3_CEbpMrdd60ZuvOazJyqQ8qZvly1ytzJGrRH5Ei2ht6x5QQ3tt7MMd8bhRivoqRzlMkGBGdaNwaGP34qP73mZidyn8EVujy2hZzgOUxRtwfvayg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  در محدوده مشخص شده می شود به دنبال موقعیتهای خرید باشیم.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/18362" target="_blank">📅 18:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18361">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏یک مقام امنیتی بسیار بلندپایه اسرائیلی دقایقی پیش در مصاحبه‌ای اعلام کرد:
«دور بعدی تقابل با ایران، آخرین دور خواهد بود. ما از ابزارهایی استفاده خواهیم کرد که تا به امروز به کار نگرفته‌ایم؛ موضوعی که حکومت ایران برای بقا در برابر آن با دشواری جدی روبرو خواهد شد.»</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18361" target="_blank">📅 18:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18360">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">— دونالد ترامپ:
«به نظر من، اسرائیل نیروهای خود را از جنوب لبنان خارج خواهد کرد.»</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18360" target="_blank">📅 18:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18359">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">به نظر شما ترامپ با این سه سگ (اردوغان، فیدان، کالین) چه صحبتی می تواند داشته باشد آن هم وقتی که جولانی هم دارد به اینها می پیوندد؟!</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18359" target="_blank">📅 18:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18358">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ فکر می‌کند اسپانیا عضوی از BRICS است !  در دوره دوم ترامپ، مشاوران و نزدیکان ترامپ قطعا نقش برجسته تری خواهندداشت.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18358" target="_blank">📅 17:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18357">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ:
جمهوری‌ اسلامی ژاپن دیشب ۱۱ تا موشک به سمت ناو هواپیمابر ما شلیک کرد.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18357" target="_blank">📅 17:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18356">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ در مورد ایران:
احتمالاً امشب دوباره به شدت به آن‌ها ضربه خواهم زد.
به آن‌ها یک اخطار کوچک می‌دهم.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18356" target="_blank">📅 16:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18355">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پیروزی های ارتش طفرنمون روس ادامه دارد…
اوکراین می‌گوید امروز یک جنگنده سوخو-۳۵ روسی را در جبهه شرقی سرنگون کرد.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18355" target="_blank">📅 16:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18354">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f7979bdf1.mp4?token=N5yykRJW2yUNUvci6WltmdijiwtU2ZUGRrsWutRV1TCTIpY8lze0pejNfRLoUIWBzGastuzZe8U-5LvjPqW-0YHZEAAqMlCo2JtdjT9KtK46JKfH8YSRrZBGlTwZarEHfhzaPsASOeTSimJHh93XRjG54b-kmxjRPGPaUfIbdj7uKtgvfgBF0kDYb-gdkAL74nreTFc1T6WIsRwA9H09jb_ADNtoyle1SVgd0dWa8NZOdKF4Uj4GpQfNk6VTbuvW8Wpx2CY6w-z9Rrpn_9Cc3f78XoeupT9qVucvcNMeqjRmE1tNOQgPrH8o2IWInp_BlWpTfT7jn42n5fNrvbxeDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f7979bdf1.mp4?token=N5yykRJW2yUNUvci6WltmdijiwtU2ZUGRrsWutRV1TCTIpY8lze0pejNfRLoUIWBzGastuzZe8U-5LvjPqW-0YHZEAAqMlCo2JtdjT9KtK46JKfH8YSRrZBGlTwZarEHfhzaPsASOeTSimJHh93XRjG54b-kmxjRPGPaUfIbdj7uKtgvfgBF0kDYb-gdkAL74nreTFc1T6WIsRwA9H09jb_ADNtoyle1SVgd0dWa8NZOdKF4Uj4GpQfNk6VTbuvW8Wpx2CY6w-z9Rrpn_9Cc3f78XoeupT9qVucvcNMeqjRmE1tNOQgPrH8o2IWInp_BlWpTfT7jn42n5fNrvbxeDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بح بح!  موشهای نیل به دامان طبیعت برگشتند</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18354" target="_blank">📅 14:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18353">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">باور کنید برخی هستند که  مطمئناً این چرندیات امثال شریعتمداری و رسایی را ترجمه می کنند برای ترامپ می فرستند.  شریعتمداری و رسایی اگر هدفشان ترور ترامپ است چرا خودشان اقدام نمی کنند؟!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18353" target="_blank">📅 14:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18352">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6F88kzTDB99JYsGBJFLyf1l_TsnhDdwoGOskw_2Xo_mP6wtF4RF3rGtAMGso3i6dIOCujYQmO_jykvbXv0jrLE2Q9UolOLqMyozblFUqmEEbkeFd-yoJ5XQprArp_86ElpWXILscFrqJlFq9wSPdavOzMXVp9UMrrXiZuR1bQ2NjyPKbTRdh5UEMQVPUL1mg1qeRdsJpO11R5GP_lfDKatY-7q69IWcuhl3FIwVLsRmFmhwRO5FetxEQsdNcnw4-trr_QhlH5MG695dahY8mLW2556aqbzjKVIX7n8vSGzLxtWq3Z1NdTZZfyA-DVAHCSp-Rr6UU8eHOrIZphnrsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:  «ایران سعی کرده من را بکشد، اما من تا حالا خوش‌شانس بوده‌ام... فعلاً. من در تک‌تک فهرست‌های آن‌ها هستم. و تا اینجا، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18352" target="_blank">📅 14:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18351">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تا این لحظه،
هیچ منبع معتبری
(از جمله رویترز) خبری درباره
هدف قرار گرفتن نفتکش آمریکایی شورون (Chevron) در دریای سیاه
منتشر نکرده است.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18351" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18350">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYRAddy0bTHOcUs5JPKqlTrZhsmlXDKBJOaCaMv5K8oYVKQbHfoZqoJVBWjjsp4zUi4n9XiXWjWVN-Zg6-CRKwh8ME7WzsBC-PDnnLHNmUVYwXtB8SHCGenynLdKv2xks8BERTvST61C3m5p4-A9Hz0sga4boQHqe49JN_wEXyosEZYBQMAQ9zw3Nq7pbF3ISWcwV_cBARkWJu2z2Q17c3u9nb4n2gvTyuvJN1jGyljPWgosOS0h39yruEeSF5VhrTOl54EmTsa-urYlq6kUQ3DiVk1DBMxI4hKYmIPNPImSkpaYKvwxKBSCy6ecXVw2KR03kjfFd_gLU77emHpPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت برق کویت خبر داد که درپی برخورد ترکش‌های موشک‌های شلیک‌شده به‌سوی این کشور، تعدادی از خطوط انتقال برق آسیب دیده و از مدار خارج شده‌اند</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18350" target="_blank">📅 14:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18349">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وزارت برق کویت خبر داد که درپی برخورد ترکش‌های موشک‌های شلیک‌شده به‌سوی این کشور، تعدادی از خطوط انتقال برق آسیب دیده و از مدار خارج شده‌اند</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18349" target="_blank">📅 14:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18348">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca74a7b8d5.mp4?token=p9DeyufpQ7iOTYfjjl0ThLuSImpr-luMAReRzxCuNCxfARlVD33hltQ5ew9nOgH2GF774ln6ep6vpZ2H-jzS1XneJewRq7vfOYegdO8BdDmpqCR5lWfmamfzHC8w551rJSN51iX0YwyY5u9GaWxn-XhEwTujTv83P-R_h67xlTERczTESWIRU_iclsYkJypQxHjm_eHBjigHhQBNcfDEpcUJr2r24Wswh0ew-xH-OjzZrMca1zF9zqmvy8EWPWZXQ9Nx66GAOrwzme0xopAErtIRbbOTQSECBd5VAHfyMVm4Eejjl5HFUwgTcC4G4pFFP47T3blnXyTCuAYoheThkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca74a7b8d5.mp4?token=p9DeyufpQ7iOTYfjjl0ThLuSImpr-luMAReRzxCuNCxfARlVD33hltQ5ew9nOgH2GF774ln6ep6vpZ2H-jzS1XneJewRq7vfOYegdO8BdDmpqCR5lWfmamfzHC8w551rJSN51iX0YwyY5u9GaWxn-XhEwTujTv83P-R_h67xlTERczTESWIRU_iclsYkJypQxHjm_eHBjigHhQBNcfDEpcUJr2r24Wswh0ew-xH-OjzZrMca1zF9zqmvy8EWPWZXQ9Nx66GAOrwzme0xopAErtIRbbOTQSECBd5VAHfyMVm4Eejjl5HFUwgTcC4G4pFFP47T3blnXyTCuAYoheThkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  «ایران سعی کرده من را بکشد، اما من تا حالا خوش‌شانس بوده‌ام... فعلاً. من در تک‌تک فهرست‌های آن‌ها هستم. و تا اینجا، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18348" target="_blank">📅 14:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18347">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">عراقچی را در ایران فحش می دادند در عراق بشدت بزرگ داشتند!
فکر کنم عراقی ها چون دیده اند فامیلش عراقچی است فکر کرده اند ولی خب.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18347" target="_blank">📅 13:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18346">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ:
«ایران سعی کرده من را بکشد، اما من تا حالا خوش‌شانس بوده‌ام... فعلاً. من در تک‌تک فهرست‌های آن‌ها هستم. و تا اینجا، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18346" target="_blank">📅 13:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18345">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دوستان درباره تن ماهی پرسیده بودند؛
به نظرم زود است و می توانید از مرداد هر هفته پله ای بخرید.
تصور می کنم هنوز ذخایر نفتی آمریکا پر نشده و انبارهای مهماتشان هم.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/18345" target="_blank">📅 13:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18344">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فوری | اردوغان: موضع قاطع ترامپ در مورد تلاش‌ها برای دستیابی به توافق با ایران قابل تحسین است.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18344" target="_blank">📅 12:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18343">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ :   تفاهم تمام شد، نمیخواهم تعاملی کنم</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18343" target="_blank">📅 12:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18342">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lq0j23_6kWtyD3KN-Xd2xfiC7JbWwCyHVh1s94hI8uQ2kDUgNAhvcdwT6ndnSwjpAS1XWAEu9LiaoYJE6MK5xryHIcEkcsUHfhZqQL6IEQTXOjoDhfdbSkks3wZsOrKJGvZgOT4XjpcKI_X2TPBYMkXGyMF_ieO38Yc5Gk0XVs3MUtB7HiAigWRk9--kQGmVp7uAHnQ7-1wWce0p9zN-0_PhiKzJ0meJogcYYx2HjCazF-dxEIReVqQldDSggz2JP3Pjf-3_HkeqMiaGxUH7mT-kZqizkMFL4yC_JTmlpff2yBuOR9ftkg9RG0cJiyiPQPt-Wwby1bBYmtJPdO1zMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جولانی به آنکارا، ترکیه، سفر کرد تا در اجلاس 36ام ناتو شرکت کند.  قرار است او با ترامپ دیدار کند.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18342" target="_blank">📅 12:52 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
