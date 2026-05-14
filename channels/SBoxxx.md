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
<img src="https://cdn4.telesco.pe/file/ScVS9WaouBEUhiDAPfuN02G5rGo9T3ri4kFLrr1c82s8fFVS0whiGW9Y9gbZlA889u7UtAU10dXEm3ybrwfWFAkGfz_ogzoFAHjqLCCjai50oqS0TwAF5LnDVdthKleNslaQJgwSaqQuv-b0aLw1aLBfKIaM33KtrDBacp1IZQu1W-Cx8d7k5DXSP8DwN_d9KXBOAdiTRjBVDfqeuWF3IV_wUnfSH3sz2RkJRVunr-2pO4Ha1ltZgKYPfkRfKT29BM1h9z84d2MoM8ad9eyLgYsGPKNWS3igOajHcyF5cJjZzSYd015BwCDKlIoQFJZQZ-ujoWi4egLeQSFh4m-nVg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.85K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 21:13:13</div>
<hr>

<div class="tg-post" id="msg-16290">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اسرائیل سطح هشدار خود را به بالاترین حد ممکن افزایش داده تا برای احتمال جنگی تازه با ایران پس از بازگشت  ترامپ از چین آماده شود.</div>
<div class="tg-footer">👁️ 691 · <a href="https://t.me/SBoxxx/16290" target="_blank">📅 20:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16289">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اسرائیلی ها به این نتیجه رسیده اند که هر مدل ابتکارات نظامی که ضد حزب الله به کار برده و می برند تا زمانی که حمایت فنی و مالی ایران ادامه دارد در نهایت بی فایده خواهدبود.  از این رو بسیاری از آنها الان بر این باورند که تنها راه شکست قطعی حزب الله، تغییر حاکمیت…</div>
<div class="tg-footer">👁️ 767 · <a href="https://t.me/SBoxxx/16289" target="_blank">📅 20:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16287">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رئیس‌جمهور ترامپ می‌گوید چین توافق کرده ۲۰۰ هواپیمای بوئینگ بخرد.</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SBoxxx/16287" target="_blank">📅 19:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16286">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وزارت امور خارجه هند اعلام کرد که دیروز کشتی‌ای که پرچم هند را برافراشته بود در سواحل عمان مورد حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/SBoxxx/16286" target="_blank">📅 18:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16285">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شاید ما برخی کشتی ها را با پهپاد زده باشیم، برخی ها را با موشک بالستیک، برخی ها را هم با موشک کروز.
خب اینها می‌شود تفاوت‌های حملات ما.
اما یک شباهت بزرگ هم میان همه حملات ما وجود دارد و آن اینکه کشتی مورد تهاجم مال هر کشوری که باشد، دستکم ۲ ملوان هندی در جریان حمله ما کشته یا زخمی می شود.
سبحان الله !</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/SBoxxx/16285" target="_blank">📅 18:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16284">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⭕️
قیمت‌ «سیمکارت سفید» و «اینترنت پرو» در بازار سیاه چقدر است؟
🔹
اینترنت پرو و دسترسی بدون فیلتر از طریق کانال‌های غیررسمی و بازار سیاه فروخته می‌شود.
🔹
قیمت ۵۰ گیگ اینترنت پرو در بازار سیاه تا حدود ۱۲ میلیون تومان اعلام شده است.
🔹
سیمکارت‌های سفید با وعده اینترنت بدون فیلتر با قیمت‌هایی بین ۴۴ تا ۱۲۰ میلیون تومان فروخته می‌شوند.
🟢
https://t.me/SBoxxx</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SBoxxx/16284" target="_blank">📅 17:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16283">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔹
🔹
نشست مشترک رئیس جمهور چین و دونالد ترامپ برگزار شد
🔹
شی جین پینگ، رئیس جمهور چین، در نشستی در پکن به دونالد ترامپ، رئیس جمهور آمریکا، گفت: «ما باید شریک باشیم، نه رقیب»
🔹
ترامپ در سخنانش، از «رابطه فوق‌العاده» خود با شی تمجید کرد و گفت رهبران تجاری ایالات متحده برای «ادای احترام» به شی و چین در این شهر هستند
🔘
https://t.me/SBoxxx</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SBoxxx/16283" target="_blank">📅 14:45 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16282">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">۶ ماه پیش …
امروز مس دوباره ATH زد!</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/SBoxxx/16282" target="_blank">📅 14:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16281">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔹
چین با تغییر نام روبیو اجازه ورود او به پکن را داد
مارکو روبیو، وزیر امور خارجه آمریکا، که تحت تحریم‌های چین قرار دارد، با تغییر ترجمه نامش به «مارکو لو» توانست همراه رئیس‌جمهور ترامپ در نشست با شی جین‌پینگ در پکن شرکت کند. چین با این روش دیپلماتیک تحریم‌ها را لغو نکرده اما ورود او را ممکن ساخت.
روبیو به دلیل انتقاد از سرکوب‌های چین در هنگ کنگ و وضعیت اقلیت اویغور در سین‌کیانگ در دوران سناتوری‌اش تحریم شده بود. او همچنین از تصویب قانون پیشگیری از کار اجباری اویغور حمایت کرده بود
🟢
https://t.me/SBoxxx</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SBoxxx/16281" target="_blank">📅 13:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16280">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تنش‌های میان ترکیه با یونان دارد دوباره داغ می شود….</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/SBoxxx/16280" target="_blank">📅 13:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16279">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مقامات اسرائیلی به آکسیوس گفتند: «ما در انتظار تصمیم ترامپ برای از سرگیری جنگ، وضعیت حداکثری هشدار را در طول آخر هفته افزایش خواهیم داد».</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SBoxxx/16279" target="_blank">📅 13:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16278">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وزارت امور خارجه هند اعلام کرد که دیروز کشتی‌ای که پرچم هند را برافراشته بود در سواحل عمان مورد حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/SBoxxx/16278" target="_blank">📅 13:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16277">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">من 7.5 سال پیش گفته بودم که از اهداف اصلی ترامپ در تشدید تنش با ایران، دزدیدن مشتری های نفتی ما است که اینک دیگر به صورت کامل در حال تحقق است.</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/SBoxxx/16277" target="_blank">📅 12:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16276">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حسین شریعتمداری: بحرین خاک ماست و باید به ایران بازگردانده شود
شریعتمداری در روزنامه کیهان نوشت:
این جزیره ایرانی در تابستان سال ۱۳۵۰ و در جریان یک زد و بند خیانت‌آمیز میان شاه معدوم و دولت‌های انگلیس و آمریکا از ایران جدا شده است و از آن هنگام تاکنون یکی از اصلی‌ترین خواسته‌های مردم بحرین، بازگشت این استان جدا شده از ایران به سرزمین اصلی و مادری خود، یعنی ایران اسلامی است.</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SBoxxx/16276" target="_blank">📅 12:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16275">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
علی کیایی فر؛
کارشناس امنیت اطلاعات:
بانکها در جنگ ۱۲ روزه ، ازسرور یک مدرسه علمیه خواهران در قم هک شدند</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SBoxxx/16275" target="_blank">📅 12:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16274">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">در طرح جدید سپاه، کل منطقه بین این 2 خط تیره حوزه دریایی تحت کنترل ایران تعریف شده که ملاحظه می کنید بندر کلیدی فجیره نیز درون این حریم قرار گرفته است.  در واقع آمده اند تا خود فجیره این حریم را تعریف کرده اند تا امارات نتواند از این بندر صادرات جایگزین انجام…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SBoxxx/16274" target="_blank">📅 11:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16273">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cy4lok5tYaQ-BVxzSl-IUqUvHbydE3OGUnfKKgxljpI415UUyD3Bgg8qGjbkHAyi0DF8DyP19U_a3__tBaVwae_m5O5lAnHvu1cpHNejgoO6zyZtjWFF7NVZiJBLaGqEHPTcMn94v8H3vfVjkHAK0oRm7mBB7LeAejEu1GMJPdVi1tKJIHrJP4Ip4UbDEnTQEpAr79r0_VImkChnp-4lej2C0oHU4t9j9PYVsKIPXgRIUUktVi1R4x7b_lpCnZt3uTkKqqrtrpuERpyaFTRzt-RlXgJ6P43RaSt-Lkn7rkJpOmRorZlOfFON3O8ax1DvWMfFH7f6QCotQ2M_uW8hMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
بحران سیاسی بریتانیا و تأثیر آن بر پوند و دارایی‌های انگلیسی
بحران سیاسی بریتانیا و افزایش احتمال استعفای کییر استارمر باعث فشار بر پوند و افت بازارهای سهام انگلیس شده است.
سرمایه‌گذاران نگران‌اند که ادامه بی‌ثباتی سیاسی، هزینه‌های استقراض را افزایش داده و نوسانات بیشتری در دارایی‌های انگلیسی ایجاد کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/SBoxxx/16273" target="_blank">📅 11:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16272">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بحران برق در کوبا  کوبا در حال حاضر با یکی از شدیدترین بحران‌های انرژی در تاریخ معاصر خود روبه‌رو است. آنچه در ابتدا به‌صورت کمبودهای دوره‌ای برق آغاز شد، اکنون به یک وضعیت اضطراری سراسری تبدیل شده که با خاموشی‌های طولانی، کمبود سوخت و پیامدهای جدی اقتصادی…</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/SBoxxx/16272" target="_blank">📅 10:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16271">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بحران برق در کوبا
کوبا در حال حاضر با یکی از شدیدترین بحران‌های انرژی در تاریخ معاصر خود روبه‌رو است. آنچه در ابتدا به‌صورت کمبودهای دوره‌ای برق آغاز شد، اکنون به یک وضعیت اضطراری سراسری تبدیل شده که با خاموشی‌های طولانی، کمبود سوخت و پیامدهای جدی اقتصادی و انسانی همراه است.
در بسیاری از مناطق کشور، مردم روزانه تا ۲۰ ساعت قطع برق را تجربه می‌کنند؛ مسئله‌ای که تقریباً تمام جنبه‌های زندگی روزمره را مختل کرده است.
ریشه‌های این بحران در فرسودگی زیرساخت‌های برق کوبا و وابستگی شدید این کشور به سوخت وارداتی قرار دارد. بخش بزرگی از شبکه برق کوبا همچنان متکی به نیروگاه‌های حرارتی دوران شوروی است که چندین دهه عمر دارند و به‌شدت فرسوده و غیرقابل‌اعتماد شده‌اند. سال‌ها کمبود سرمایه‌گذاری، مشکلات نگهداری و کمبود قطعات یدکی، این سیستم را تا حدی تضعیف کرده که خرابی تنها یک نیروگاه بزرگ می‌تواند خاموشی‌های زنجیره‌ای گسترده‌ای در سراسر جزیره ایجاد کند.
این وضعیت در سال ۲۰۲۶ شدیدتر شد؛ زمانی که واردات سوخت کوبا به‌شدت کاهش یافت. ونزوئلا که به صورت تاریخی مهم‌ترین تأمین‌کننده نفت کوبا بود، به‌دلیل مشکلات اقتصادی داخلی صادرات خود را کاهش داد. هم‌زمان، ایالات متحده فشار بر کشورها و شرکت‌های صادرکننده سوخت به کوبا را از طریق تحریم‌ها و محدودیت‌های مالی افزایش داد. مقام‌های کوبایی اعلام کردند که ذخایر دیزل و نفت کوره کشور تقریباً به پایان رسیده و این مسئله توانایی اداره نیروگاه‌ها، سیستم حمل‌ونقل و ژنراتورهای اضطراری را مختل کرده است.
پیامدهای خاموشی‌ها بسیار فراتر از مسئله برق است. سیستم‌های توزیع آب به‌دلیل ناتوانی پمپ‌های برقی در عملکرد مداوم، مرتباً دچار اختلال می‌شوند. بیمارستان‌ها برای حفظ خدمات درمانی در طول خاموشی‌های طولانی با مشکلات جدی مواجه‌اند و کمبود امکانات سرمایشی، نگهداری مواد غذایی و داروها را تهدید می‌کند. حمل‌ونقل عمومی به‌دلیل کمبود سوخت بی‌ثبات شده و خدمات جمع‌آوری زباله در برخی شهرها تقریباً فروپاشیده است؛ مسئله‌ای که نگرانی‌های بهداشتی ایجاد کرده است.
بحران انرژی همچنین مشکلات اقتصادی گسترده‌تر کوبا را تشدید کرده است. صنعت گردشگری، که یکی از منابع اصلی ارز خارجی کشور محسوب می‌شود، به‌دلیل اختلال در فعالیت هتل‌ها و فرودگاه‌ها آسیب دیده است. تولید صنعتی نیز به‌شدت کاهش یافته و بسیاری از کسب‌وکارها بدون برق پایدار قادر به فعالیت عادی نیستند.
مسئولیت این بحران همچنان موضوعی سیاسی و بحث‌برانگیز است. دولت کوبا تحریم‌ها و محدودیت‌های سوختی آمریکا را عامل اصلی فروپاشی می‌داند. منتقدان اما دهه‌ها سوءمدیریت اقتصادی، نوسازی ناکافی زیرساخت‌ها و وابستگی بیش‌ازحد به تأمین‌کنندگان خارجی انرژی را از عوامل اصلی بحران معرفی می‌کنند.</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/SBoxxx/16271" target="_blank">📅 10:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16270">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ریزپهپادهای حزب‌الله   فیلم‌هایی از جنوب لبنان تایید کرده‌اند که حزب‌الله بارها اهداف ارتش اسرائیل، به ویژه تانک‌ها را هدف قرار داده است، در حالی که اسرائیل به عمق بیشتری در سرزمین‌های جنوب رود لیتانی فشار می‌آورد   گزارش‌ها تایید می‌کنند که یک حمله پهپادی…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/SBoxxx/16270" target="_blank">📅 09:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16269">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpzoZFIRr2WN1YKXSVxrrJsGQwg8ZDHbcB5Iz2FGgKErRfJ2ctwnt91wDnmOedCSdzRIbBcZ_A0MVa_60xu4YHPb9iyaS9piICEwZl-hnUsX8QwmshRVUzLIRiOMxTC0U5FQM0JuWbeYp3G6VDLT1iej6VaKVw7rJzrigrDuKRj_jmshmvTz0EAVXzDfXo3FeuGC-DcqQFnwy-9iXchsR_Hoxb_uyTpDelN5MYlWT20GYlSN2R8hCrfdL8x9WLwfOp_K41MoTMCpjWjL_xftZ-c7UE8E-K8h_fRhaduq7Yyke-mmUoJsSXQ1m9hzOUr2UuPsowO6II2O1GP3msRfNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 2 سال پیش آگاه است که بستن تنگه هرمز بیش از همه به سود روسها بوده و هست و چینی ها ابداً از ادامه مسدود بودن این تنگه سود نمی برند و لذا فشارشان بر جمهوری اسلامی برای پذیرش توافق کاملاً قابل توجیه است.  بد نیست بدانید اکنون بیش از 90%…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/SBoxxx/16269" target="_blank">📅 09:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16267">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqWFs0Wzk6I9NC0ygOqx8jzPRZm6-uzdhZ5SvoHKcM7I0nCZYGu5WZnq-4jcv4SH4ef_guH5XIMFpec-LAq5a3-eo7uLv89zBWvvMo-okB98E0Bjuw3zwpzPJoL-lVMSBiuPRdQ60Je_5EWEblDiXdRVQnZz3aLqmDVe-JbdakzSri9fSHFX6Fp6_CZiUyZrtW7tptBMFZ4FyvO69C2zEiI97a01MZp481a_eRXRscwW5j8pTn6u986zCe1glmVSwVDQLxW6rEUVEg11o6X-Np-_-0EqSzX8XQ6feUR7a8TypYUOZWShJOU813GogtW2fJwCieKVfMdrGkvh5T19tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خط لوله حبشان به فجیره بود که اماراتی ها می خواستند از آن استفاده کنند تا به تنگه هرمز بی نیاز بشوند که ولی خب.</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SBoxxx/16267" target="_blank">📅 09:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16266">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ایلان ماسک می‌گوید مشکل سوسیالیسم این است که «بعد از اینکه آن‌ها «ثروتمندان را خوردند»، گرسنه خواهند ماند.»</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/SBoxxx/16266" target="_blank">📅 09:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16265">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">چرا مخالفت ونس نمیتواند منجر به اخراج او از سوی ترامپ بشود؟!
در ساختار سیاسی ایالات متحده، رئیس‌جمهور نمی‌تواند معاون رئیس‌جمهور خود را برکنار کند، زیرا معاون رئیس‌جمهور صرفاً یک مقام اجرایی منصوب‌شده نیست، بلکه مقامی مستقل و منتخب در چارچوب قانون اساسی آمریکا محسوب می‌شود.
رئیس‌جمهور و معاون او به‌صورت مشترک در انتخابات سراسری و از طریق سیستم کالج الکترال انتخاب می‌شوند و به همین دلیل رابطه میان آن‌ها شبیه رابطه رئیس با یک کارمند کابینه نیست. وزرا و مقامات اجرایی توسط رئیس‌جمهور منصوب می‌شوند و او می‌تواند آن‌ها را عزل کند، اما معاون رئیس‌جمهور دارای مشروعیت انتخاباتی مستقل است و رئیس‌جمهور اختیار قانونی برای اخراج او ندارد.
معاون رئیس‌جمهور تنها در چند حالت می‌تواند از مقام خود کنار برود: استعفا، فوت، برکناری از طریق فرآیند استیضاح و محکومیت در کنگره، یا تبدیل شدن به رئیس‌جمهور در صورت ناتوانی یا مرگ رئیس‌جمهور.
البته رئیس‌جمهور می‌تواند از نظر سیاسی معاون خود را به حاشیه براند؛ برای مثال او را از جلسات مهم کنار بگذارد، اختیارات غیررسمی‌اش را کاهش دهد یا در انتخابات بعدی فرد دیگری را به‌عنوان معاون انتخاب کند، اما از نظر حقوقی امکان اخراج مستقیم معاون رئیس‌جمهور وجود ندارد.
این استقلال همچنین به متمم بیست‌وپنجم قانون اساسی مرتبط است که در موضوع ناتوانی رئیس‌جمهور، نقش مهمی برای معاون رئیس‌جمهور در نظر گرفته است.</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SBoxxx/16265" target="_blank">📅 09:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16264">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کره جنوبی:  «ما به شدت حمله به یک کشتی باری کره‌ای را محکوم می‌کنیم و قصد داریم پس از شناسایی مهاجم، به او پاسخ دهیم».</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SBoxxx/16264" target="_blank">📅 08:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16263">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ:   روابط آمریکا و چین بهتر از همیشه خواهد بود. تجارت از سوی آمریکا کاملاً متقابل خواهد بود.   آمریکا و چین آینده‌ای فوق‌العاده در پیش خواهند داشت</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/SBoxxx/16263" target="_blank">📅 08:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16262">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📌
شوک انرژی جنگ ایران و فشار تورمی بر آمریکایی‌ها  افزایش قیمت انرژی ناشی از جنگ ایران باعث شده تورم آمریکا دوباره اوج بگیرد و برای نخستین بار در سه سال اخیر، رشد دستمزدها از تورم عقب بماند.  افزایش هزینه سوخت، غذا و خدمات فشار بیشتری به بودجه خانوارهای آمریکایی…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SBoxxx/16262" target="_blank">📅 06:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16261">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ:
روابط آمریکا و چین بهتر از همیشه خواهد بود. تجارت از سوی آمریکا کاملاً متقابل خواهد بود.
آمریکا و چین آینده‌ای فوق‌العاده در پیش خواهند داشت</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SBoxxx/16261" target="_blank">📅 06:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16260">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🖋️
بستن تنگه هرمز به سود کیست؟!  برخی به اصطلاح نوابغ دنیای سیاست مدعی اند که در صورت هر گونه حمله نظامی به ایران، ما بایستی تنگه هرمز را مین گذاری کرده و مسدود کنیم.   در صورت مسدود شدن تنگه هرمز، جریان صادرات روزانه ۲۰ میلیون بشکه نفت و مقادیر معتنابهی LNG…</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16260" target="_blank">📅 22:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16259">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOXz5NPxVPDt4LH1kC1hXM82nuqfcxpW2ZX6pbFjk9AjxuYWSF__ODX93LQSskKW7lwOr5D2JygPNkKDGP677DdU6jkfc8AfgszehC63uArUQuSx7Zxi0qUMgeWcisPYHR8w9G7kc0-L-VGsuR5oKvsmQdiLQ-ygnDcO3qhygx6yPWZ3dWGscBNaNL7KkSEm1py_dYX55iSOjhH0evqxhCy8yDTacmOuy_zOj6xG4pSYoie6bQSoWuTKRVMHZ3y8Gd7zSW6gqvtgl6lAN0zBvqUmOOmZkQ-iQj9yiA5JMaa87uvXMtFMRGBHfDX_BWTVNFO4mzF5PtYufvfU_s_BZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
پولتیکو:  چین ایران را برای رسیدن
به یک توافق تحت فشار قرار داده است
نشریه پولیتیکو در گزارشی به نقل از یک مقام ارشد دولت ترامپ اعلام کرد انتظار می‌رود دونالد ترامپ در جریان دیدار با همتای چینی خود، پکن را در خصوص مسائل مربوط به ایران تحت فشار قرار دهد.
طبق متن این گزارش، یک مقام ارشد دولت ترامپ در این باره گفت: «انتظار دارم که رئیس‌جمهوری در طول دیدارشان، در رابطه با موضوع ایران بر شی فشار وارد کند.»
به گزارش پولیتیکو، ترامپ از رهبر چین می‌خواهد تا از نفوذ خود بر تهران استفاده کند؛ چرا که چین تامین‌کننده تجهیزات نظامی برای تهران و خریدار عمده نفت ایران بوده است. هدف از این فشار، وادار کردن حکومت ایران به پایان دادن به انسداد تنگه هرمز عنوان شده است.
همچنین یک مقام ارشد دیگر در کاخ سفید به طور جداگانه مدعی شده است که: «چین پیش از این نیز ایران را برای رسیدن به یک توافق تحت فشار قرار داده است.»
بیشتر بخوانید:
https://l.euronews.com/q0ZO</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/16259" target="_blank">📅 22:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16258">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMztSZ1Y-e7jn8-8x4yRl92OttL-8C23lgVEgrxsrO3XxPzlDvfrt3-IzkzFREWeC8QTgKmbEcOlAXlqg92DAVpHYLu1g91QrQG29kA_qYadP2Wp0-NGsPwjchaxitGdIzPsLGcdlF4saRqbgnRVHZ-hlhWLWbtckJ1ToeNXW9GcmzsB3MjswA0UVFC5OP0NcOs2Sb2AMfgKr-YmZGzBPFU95bQT3h5NETV-aSOAPJ5_vMi0ESopVIBvICSX6fXADk_6yVA9_5Br9L-ZHgKXVTUWaYjg3Cd4QwSP_n4YsTE-2cp5EqydDyEif6Ukj7-2VkvhFzeDaQu5PKNfR1Srlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗯
جی دی ونس ؛ معاون ترامپ
:
وقتی ترامپ در سفر هست و من اینجام ، حس اون بچه‌ی فیلم Home Alone رو دارم ، میام کاخ سفید، همه‌جا ساکته و خالیه، بعدش یادم میاد چه خبر هست</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16258" target="_blank">📅 22:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16257">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OF_oYYcd7_7Nb6zyK_ljAfW7rF5XpDi51bxnEdt18g7M3aFpdX3UW1bwDNVvouNdM_eNHK0slYMjRn6cAcex8iVRJy_J3yr8VZ_s1jZsXR7N_vjSRlJs-d1atCzCibm7AdHgtim6M6PqK_l4nYW85nE-TAsV3Utntr9xrTJ6HyK1RzRg8JCKTS8ELg2mTYEW3PPMm_DGp-Ud2FXCbEYNPOxPjFXb1WIZo32ioRPsSgUjPEOfYf-e-PdtDTKZA0h2e60fE7I3tYPWpHtuBBVXVw1Pod1kSZs6jFqDMUdDc8bPWJPWl-YktQAJh2_CfSbFd62o7EosrcmE5K7f-QKcdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند تحول اقتصادهای گروه ۲۰ در ۱۰ سال گذشته!
تنها کشوری که شاهد کوچک شدن اقتصادش بوده ژاپن است.</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16257" target="_blank">📅 21:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16256">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رویترز: عربستان سعودی و کویت در جریان جنگ با ایران، به اهداف شبه‌نظامیان وابسته به ایران در عراق حمله کرده بودند!
حملات عربستان توسط جنگنده‌های نیروی هوایی سلطنتی عربستان سعودی علیه پایگاه‌های شبه‌نظامی که برای حملات پهپادی و موشکی علیه کشورهای خلیج فارس استفاده می‌شدند، انجام شد.
منابع عراقی همچنین اعلام کردند که حداقل در دو نوبت حملات موشکی از خاک کویت به سمت عراق انجام شده است، اگرچه خبرگزاری رویترز نتوانست تعیین کند که آیا این موشک‌ها توسط نیروهای مسلح کویت یا ارتش ایالات متحده شلیک شده‌اند یا خیر.</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/16256" target="_blank">📅 21:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16255">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دفتر نخست‌وزیر اسرائیل تایید کرد که در جریان جنگ با ایران، نتانیاهو به صورت محرمانه به امارات متحده عربی سفر کرد و با رئیس اماراتی محمد بن زاید دیدار کرد.
این سفر مخفیانه منجر به یک پیشرفت تاریخی در روابط اسرائیل-امارات شد.</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SBoxxx/16255" target="_blank">📅 20:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16254">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">صلاح مملکت خویش خسروان دانند اما چیزی که من حس میکنم این است که یک «اجماع» بزرگی دارد شکل می گیرد که آخرش شاید به جماع عظیمی ختم بشود ولی خب.</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/16254" target="_blank">📅 19:57 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16253">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSN6np3oNYM8Ca5UrcvQJIxh4hlo6BygqbN2b-p1_fxkWWSr--XSnhdP5k_qHEsuau0WRJQnCwrn-27nuRKtOFcx433M9sBOZeVboqr2i5p5Z9EFmZTxbtWdqRc2t3wvVmLpMhQQEjg9CAebdCTVRdogUrMGNldy7a2zA9Un6rPFCaJ2qfFxToScVPi7bpHxe8BLUnPJpcr-ajiQvzTQGhiRmrt24fXzM2uwE60xx3VHh7RjQkc-butD-LBJra2xTYEyCM27pP7PebZyGnmzbJgFnrfBTiInvkwIKwMvtZcBlX54Kyr2mpx-ua5BEnVQJhfL7UrdMBAul9yPNN-vEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله پهپاد جدید پنهان‌کار خود را رونمایی کرد.  این پهپاد جدید که احتمالاً توسط چین تأمین شده، قادر به فرار از رادار و حرکت در میان ساختمان‌هاست، ۵ کیلوگرم مواد منفجره حمل می‌کند و طبق ادعای حزب‌الله، بردی در حد ده‌ها کیلومتر دارد.  ‌شبکه های رسانه‌ای حزب…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/16253" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16252">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
🇨🇳
نگاهی به تیم همراه دونالد ترامپ در سفر پکن</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/16252" target="_blank">📅 19:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16251">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbWRJSXsY9K-bPXvvVngmWpHzG5FQZTL8YpG4X2xhHCXL8SFaiM_BkSBbJnmS2JmdHR8h4JSRkc37wAkY4m4ws6hcRDAPRH_Hy9pc448lv40-lLAZp7_Ows_xPJF3ug39xG6qspUcW1fQ7bF3BBNPtqJ-Tp9hxnXYR_88iCtdEBv0L4GBIpUfc8ACWGPPWWl6Y4jdCxv7h9VSDJwVs3mmbh-6Bv-HLElZJEWliNjW2W-qySsFPVUzFxGjNHV2xfUhfpIm52cmLcf7sDMxyNLpIDIQ7LjT2keqpkc56HCHAnHIl__K5RkcwoBZdcfei-2NwRc6IWOY9msOcKvqCJylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇨🇳
نگاهی به تیم همراه دونالد ترامپ در سفر پکن</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SBoxxx/16251" target="_blank">📅 19:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16250">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/585750fa88.mp4?token=HO3-3uOpBTBe71zwPIrr8zlXZUSYah5zx9OEvlA9Hzv7JCbdYZiB8NqSKsKCea8qBsGyLwkhJWew6CJ4aySGPawnPHs-QrtIkLlDo48HYl5aAYNutdydMojK7B1Ql6A5Q4-34X6fKE1apArRhBhJz3puqpQIVT63nMxQxrpyxYNt-21twndv3-fgeHs_m27GPi43tZnn3OI5v5wkjKlqrYca7GFuoD9B-rzPhUld3a7icFbtSSHNu7MQv40hch5s3l913VIVSjGy1MmnzFs6ZR5kfE_EeP5r6jgPC9sPahIlKsUYj-C0Efi-UYKURp8BrVk_UXBrua64yR_Km8tP4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/585750fa88.mp4?token=HO3-3uOpBTBe71zwPIrr8zlXZUSYah5zx9OEvlA9Hzv7JCbdYZiB8NqSKsKCea8qBsGyLwkhJWew6CJ4aySGPawnPHs-QrtIkLlDo48HYl5aAYNutdydMojK7B1Ql6A5Q4-34X6fKE1apArRhBhJz3puqpQIVT63nMxQxrpyxYNt-21twndv3-fgeHs_m27GPi43tZnn3OI5v5wkjKlqrYca7GFuoD9B-rzPhUld3a7icFbtSSHNu7MQv40hch5s3l913VIVSjGy1MmnzFs6ZR5kfE_EeP5r6jgPC9sPahIlKsUYj-C0Efi-UYKURp8BrVk_UXBrua64yR_Km8tP4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتتاح نخستین نماینده رسمی اپل در افغانستان!</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SBoxxx/16250" target="_blank">📅 19:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16249">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYGDij59j0jzp25EjgCQeJ2Zo4UsTzpZ6W9LWa-gX4P5MzijrGcVZmUYPg-oE07dXUwuCRFbesKBCRCLuj_6CH3kVbIhmmj9G7fcdmyazjIRWSna3MMAnlDmlPPXPwvYKFEOuCbtbZKeOHPIDaG8wb_SQSWsU-I7WSow9PZ324oYra6nxFh0-Ip-7bAgibtn5dEWjDFB3blqDk4v3x8vETQ4Dpz1B5fv6qpX1xHhRUK3EQd0bTbPryesZyD4tsuJu7LE4Vo4nsrmsRYF6nsqSX1ky9XxEfjUP0FuDw-vRJ_6MyI5b3d7Db2Mhx1Vgq12HFRDU-C7pSO8aC0lLcnAXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاح نخستین نماینده رسمی اپل در افغانستان!</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SBoxxx/16249" target="_blank">📅 19:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16248">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">۸ سال پیش …</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SBoxxx/16248" target="_blank">📅 19:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16247">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">صلاح مملکت خویش خسروان دانند اما چیزی که من حس میکنم این است که یک «اجماع» بزرگی دارد شکل می گیرد که آخرش شاید به جماع عظیمی ختم بشود ولی خب.</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/16247" target="_blank">📅 17:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16246">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🟠
کارشناس امنیت اطلاعات
:
هیچ منطقی ندارد که منِ شهروند عادی که دشمن هیچ نیازی به اطلاعات و احاطه به من را ندارد ،  به اینترنت بین الملل دسترسی نداشته باشم ، اما مسئولی که حتی می‌تواند در لیست ترور دشمن باشد آزادانه به اینترنت دسترسی داشته باشد
دشمن آمریکایی-صهیونی تکنولوژی هایی دارد که حتی بدون اتصال فیزیکی و نرم افزاری می‌تواند حملات سایبری خود را به خوبی انجام دهد و این بسیار ساده لوحانه است که تصور کنیم با ایجاد یک شبکه اینترنت داخلی ، امنیت را به فضای سایبری کشور هدیه داده ایم
در همین ایام ، شرکت های زیرساختی که دسترسی شان به اینترنت بین الملل قطع بوده ، هدف حملات متعدد سایبری قرار گرفته اند
✈️
https://t.me/SBoxxx</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/16246" target="_blank">📅 14:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16245">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⭕️
استاد یکی از دانشگاه‌های کشور رفته سوالاتو اینطوری طراحی کرده تا هوش مصنوعی جوابشونو نده:
✅
با ما اخبار جنگی بروز باشید  @russiamilitery</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/16245" target="_blank">📅 14:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16244">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار جنگ ایران و آمریکا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_tCf8Q1QRWJzv3c0hqYta0fvkWPZAsYQqQWzUnboNlBgeYIaNj9c6YHqhBY9J4gMxtY7hN1bGGn6rouCOpt-5I8NfiCOmupf2M7e_mYxzR-OE81Aof8qjkSugpDq3qwcTI5sIPq19AAktSOUg6Xt0vRKanUiF3Nklpj1YlkzzxNb_X2rD4gENzkAEwA9sJ1wakLXvpJEDDhYCLTZJT1BwGjcBKgNK10Nc0nbNgqlVRKCzx_Fl7_rylCCyZ-b1CoKsbuRhxkjFsZe2bg2r1Uo31ZwXOob7ExUG-Ic9WeKayE2VIEXFMsL8qshXOJloOkYZAimHFKhfOR7PrH-mBMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
استاد یکی از دانشگاه‌های کشور رفته سوالاتو اینطوری طراحی کرده تا هوش مصنوعی جوابشونو نده:
✅
با ما اخبار جنگی بروز باشید
@russiamilitery</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/16244" target="_blank">📅 14:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16243">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چرا_آمریکا_به_سوی_جنگ_طولانی_با_ایران_می‌رود.pdf</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16243" target="_blank">📅 12:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16242">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhZw1yQs_rpdKD4GogiHoK0g0aXELjBezQt_v43u0tbpNYEshnLHZdBsVFaIQHqJPbZnDU_VkkKCP1wjYqCc95-59AzgNh6tKwZTGcE0k_n55lnEWTIeKd79wcNJJ3iBe7tx0lOjIvCknehxxUzO1Po6MdXwyYgTN_GkVpQHHvVfMJUb_z24xsayfmI6yXMHieQbXEbg5InEqWWazLtLTNHz06TfKuqb0VVJj_Y-qHS4bOeGZeSsi7PGRe7XHA7W8MfVdCUKF7AnupKE3ThqrIkrJ2jDSHRbPUXImpGFWo1Lzqb3j8NpAsu0_pu2bIuT31Rvfpw0feUP_X_PsrkkQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
شوک انرژی جنگ ایران و فشار تورمی بر آمریکایی‌ها
افزایش قیمت انرژی ناشی از جنگ ایران باعث شده تورم آمریکا دوباره اوج بگیرد و برای نخستین بار در سه سال اخیر، رشد دستمزدها از تورم عقب بماند.
افزایش هزینه سوخت، غذا و خدمات فشار بیشتری به بودجه خانوارهای آمریکایی وارد کرده و نگرانی‌ها درباره ادامه موج تورمی را تشدید کرده است.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/16242" target="_blank">📅 12:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16241">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEG1_WvzMfPtSEgyc2MSPJJQQrGfoyA9_S3TywUhuoHgHU2xRwPg1qreR4qM6WzfYihI4f_CcHhkTiotzzIbokBE5tdWtLopdJCA8z96RxHqmkyT-KZhJUxGKi--SEs64h1tjv5sYrOBo4aYUSCF-wBPlDkAEzPNJO5HbF1XTkbOpO1NGdLajZJK1lYf4p82Rbmq86PEgGFBBbLcUIEK52r4CfcJFoldW4ZntuyJjZnbMQ6ZazMUfqo8mgFMDFQCJFZkVFfcxAwAVOGbCUQaOlB-K1ht4Yi80clHFx30SI3M4zkI_jP2GR25SXuPrYe9_jjccmjBRDJQaeOcsgpT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جنگ ما با اسرائیل بیشترین آسیب را عربها دیدند!
سبحان الله!</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/16241" target="_blank">📅 10:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16240">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ می‌گوید ایلان ماسک، جنسن هوانگ مدیرعامل انویدیا، تیم کوک اپل و سایر مدیران ارشد شرکت‌های آمریکایی در هواپیمای ایرفورس وان به مقصد چین در حال پرواز هستند.</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/16240" target="_blank">📅 10:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16239">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOwGZ1kqEM1DwdaQh-X94TkFgSAKmci11aVERNT7d_6VZcC1w2BMdmB_EHD__f1byYuGpGsh1RvzUtDYjfQ8p5RkphNhb4Nc-aFIiBPETV6cImNozcnCrUZbY0qVLs5_U1OtW9Oc5aZWX-egw9pWbOnHgnpqAFma1yop2sR_jn3ZeB5RVg25-XWJkrmSGy1OQZ3lEAU8imNWK3xcguQaGdWQEIbghrt2zxQKkYqcaTO-g84J4WLqKXbQRaLKGJFcvXADPk9cG2npwHkLSJudwevGjtCE5xtL3p55Rh1wnr-XpR4bZ2geypH1yzB8eSYZ40TXuwuwURG-MPvwHdUIIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD -- H4  مسیر بعدی مدنظر پس از رسیدن به سقف کانال.  تحلیل تایم پایین تر در یادداشت بعدی...
💬
ارتباط با پشتیبانی : @cyclicalwavessupport
📌
کانال ما : @cyclicalwaves</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SBoxxx/16239" target="_blank">📅 10:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16238">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9MsTLdJLjtWfYX4yeRB0xrFAclhcxRlslscwYPhP0YK4XnegH_jJ0DVLwFKrgSVGPmuBqXk3uNDdDEjFFiEQQzxvsXtJ9DTVTh1LMfIfA78Ps61z9HaYEHOts8G815xZ8IJ4jy-kOWuVaypWIdSrt5hdqeuzwDOTQ1Rod2dF8ftGwz2tgLwhLRTnxyjB1TcmRwPgb74Fec85nO7xRbwKCXI1S5a6OmNpTeHNp8UfeoO6AjzHyfzGChsgQiRQUCIQT43t9rwemPsU_aKdjWi910AsZ_9ynDsglQj7E-jcQP8QZXvqSiyGWamaFeubY5HzfgaBRjoBS3GrodfWr0rVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD
-- H4
مسیر بعدی مدنظر پس از رسیدن به سقف کانال.
تحلیل تایم پایین تر در یادداشت بعدی...
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SBoxxx/16238" target="_blank">📅 10:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16237">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-text">ترامپ می‌گوید ایلان ماسک، جنسن هوانگ مدیرعامل انویدیا، تیم کوک اپل و سایر مدیران ارشد شرکت‌های آمریکایی در هواپیمای ایرفورس وان به مقصد چین در حال پرواز هستند.</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/16237" target="_blank">📅 09:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16236">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgIwyRgy7q1LgGqLGXsSwWSe2YjOoysiTqWmk763FqIIuuQnsiEeb4qQc21glzO9vvNK7rwuF7uKoYrlKK0kq5RoCs8WUMaPbJCqo-R6Pugu_VNABpeyfGHU1wLr-4r9mk6YYoU-tc5FVD6_KaiSqT52V54OETNh3kaR9nVHIrdMHxY07nVcLJzK0SRbYKaPs3FZ7-PsH3hMuVbtVzk6O5owoZ2Ca25mLEabZXJwA8uUqNNdgb-guA5WlirzLhK8N5LpQ862H1Z4DcUe_f3OzxkiVTsmmzs3Pmjn3QLzwgRZuY7ij_T5njhupoa0fJLRzUp3M7y88RHGgtZfV6WCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی منابع خبر از طرح حزب الله برای تصرف بیروت می‌دهند.</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16236" target="_blank">📅 07:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16235">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">لازم به ذکر است که این دو مستراح بزرگ تا ۱۹۷۱ با هم متحد بودند که سپس بنگالی ها با کمک هندی ها از فاکستان جدا شدند.</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/16235" target="_blank">📅 06:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16234">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نیویورک تایمز:  برآورد فعلی این است که حدود ۱۰٪ از پایگاه‌های موشکی ایران به طور دائمی توسط حملات آمریکا از کار افتاده‌اند.  ۹۰٪ باقی‌مانده پایگاه‌ها و سایت‌های پرتاب موشک در سراسر کشور «یا کاملاً یا تا حدی عملیاتی» باقی مانده‌اند و احتمالاً برای از کار انداختن…</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16234" target="_blank">📅 06:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16233">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پست جدید ترامپ !  استخر کاخ سفید را گفته تمیز کرده اند و این را برای رنده کردن دموکرات‌ها سوژه کرده است.</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/16233" target="_blank">📅 06:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16232">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نیویورک تایمز:
برآورد فعلی این است که حدود ۱۰٪ از پایگاه‌های موشکی ایران به طور دائمی توسط حملات آمریکا از کار افتاده‌اند.
۹۰٪ باقی‌مانده پایگاه‌ها و سایت‌های پرتاب موشک در سراسر کشور
«یا کاملاً یا تا حدی عملیاتی»
باقی مانده‌اند و احتمالاً برای از کار انداختن تنها با حملات هوایی بیش از حد مستحکم هستند.</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/16232" target="_blank">📅 01:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16231">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">زلزله های پیاپی در تهران!</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16231" target="_blank">📅 01:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16230">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چرا معادله روسیه—اوکراین برای چین—تایوان برقرار نیست؟</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16230" target="_blank">📅 01:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16229">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">When the Fake News says that the Iranian enemy is doing well, Militarily, against us, it’s virtual TREASON in that it is such a false, and even preposterous, statement. They are aiding and abetting the enemy! All it does is give Iran false hope when none should…</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16229" target="_blank">📅 01:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16228">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDonald J. Trump</strong></div>
<div class="tg-text">When the Fake News says that the Iranian enemy is doing well, Militarily, against us, it’s virtual TREASON in that it is such a false, and even preposterous, statement. They are aiding and abetting the enemy! All it does is give Iran false hope when none should exist. These are American cowards that are rooting against our Country. Iran had 159 ships in their Navy — Every single ship is now resting at the bottom of the sea. They have no Navy, their Air Force is gone, all Technology is gone, their “leaders” are no longer with us, and the Country is an Economic Disaster. Only Losers, Ingrates, and Fools are able to make a case against America! President DONALD J. TRUMP</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/16228" target="_blank">📅 01:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16227">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXAoMA1LC1inTbY9skiTvP2jJ_nAVBGbM-ZVNR-wTkbLuyiPPJzh6bz2dx0rGavC-xk3tzaxMCmYILZ0eXUcMWJLMaVGCh8yx-2fzQwmXb-8F_qSo1IL8vS0_3py0892lT3pcusKMK__2_ZCR81EnFEBDhIypx226AQCmSN94QWVQg665SzRwdtZiyLEwYEPDkQE_H2JTm80uca_FES4V-C7iA43xc_U-hg-5aaeqAeKayq25Id2QcC73ZQelWVljQa3S1s282CxCa_lEDA1cO_Q9fMO6W9f2Gvsfj58SqXHDNfVSBbDXiIQvZKUorApWUFHBFfc-ec68l59T9kMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#URA
— D
#سهام_خارجی
این یک فرصت ویژه ایرانیان خارج کشور است. صندوق ETF اورانیوم می تواند در قالب موج 5 خود دستکم 70 درصد رشد داشته باشد که در چارت می بینید.
نظر به مسخره بازی ما در تنگه هرمز، احتمال هجوم سرمایه ها به انرژی های جایگزین بالاست و انرژی هسته ای هم یکی از اینهاست.</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16227" target="_blank">📅 00:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16226">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">چرا_آمریکا_به_سوی_جنگ_طولانی_با_ایران_می‌رود.pdf</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16226" target="_blank">📅 00:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16225">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چرا_آمریکا_به_سوی_جنگ_طولانی_با_ایران_می‌رود.pdf</div>
  <div class="tg-doc-extra">347 KB</div>
</div>
<a href="https://t.me/SBoxxx/16225" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترجمه یادداشت تحلیلی Foreign Policy درباره احتمال فرسایشی شدن جنگ ایران</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16225" target="_blank">📅 00:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16223">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwTwz3HyKvjPmzUA9AAgCyl3eVkLf0PyxhNK9jYVO3NF_XeJlpquXJssnAHLEsS1eyuDBPPUV4ROwStn_G-mJ3l_VKYZISNhGA687sSZKA5qa9HKmNoYQntjq7DAX312BiflrccPc_xGjzbeUsSkM8o-7HvDIFJcFVZAh39EzXd8KaRTOzMDLW2wwEQ3ixJuD6lijo4Ckv3Inw-PK1xUgIKl_Qic_3nY9GtNVNg5DG0AlcWpgTLhuE6orFBhJRLbnU-bJKv0jJXC6K0snraP4x2SlclG6iQYZarbrFdQqkxbTC-Cthjo5HvyVuHctb2qK8m9ldN5WWlMg2bcUkl3qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای نخستین بار از سال 2023، رشد واقعی دستمزدها در آمریکا به دلیل جهش تورم ناشی از رشد بهای انرژی، منفی شد.</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/16223" target="_blank">📅 00:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16222">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">زلزله های پیاپی در تهران!</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/16222" target="_blank">📅 00:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16221">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3zdjbosj_fViTvxDIzCgRkNBd5AKvi7rFscjtcMvftzjS0iElBsGxEmuhqBBkmun-0vzUno8emkMB2u-HjTUisdlJwvnBAc9iIHUZvuls9fEoEmSd7re3TRkqyhdG5wN6EvFhTyiHVtzVPcrEw9obL6Dn_yLGAaDZLB_kx3cS3KFX3BhOzAOBl_4vJZfDNWQCZpfSt_Mtiu6j_3VKaENUWsCDNheQHa_4NToYXnhMJVkKQ80t-otwUZYpAgZySPmsRpwfIwx72giryqJ89wJaQM1lUygR7lXrDsx2v_Z7FbFAdPSgGwDyJ4m4HBBz0DdeMcJYUaqJXetxuX1YnRjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SBoxxx/16221" target="_blank">📅 22:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16220">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">منبعی به خبرگزاری فارس گفت که ایران وارد دور دوم مذاکرات با ایالات متحده نخواهد شد مگر اینکه چندین شرط برآورده شود، از جمله پایان جنگ‌های منطقه‌ای، لغو تحریم‌ها، آزادسازی دارایی‌های مسدود شده ایران، جبران خسارات جنگ و به رسمیت شناختن کنترل ایران بر تنگه هرمز.
بر اساس گفته‌های این منبع، تهران این مطالبات را اقدامات حداقلی برای اعتمادسازی می‌داند که پیش از آغاز هرگونه مذاکره جدید باید انجام شوند.</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SBoxxx/16220" target="_blank">📅 22:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16219">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/as8zrt37KBrvGlnndb4FstczS5dwMg-5tGbbXuhGiUMfDTbxskvPi-JvOQzKrQ6JfGHR_7JaC9k6M93Xn8S9b9bv777u2vBWilkci-IszcONUYppjgcaSpDoZqB3BGaMMNqwddfd-Ii7BZrW_QJKYe9l-FKapHMxvTP1MfdNFrg7Z8Z0DrdBSoZreuIqSsqXBpL9dj-gZVVmAjBGoTer_-rzubMO4wUZ33N1QXy2MixSjhqvPJQ2vxLMgmyjCFCFbdsVqUXD5foWvzciRxuAuOGLTtZ44HPRcQxiX3nMCoqC4o9hyF-zRYaWpbV00zYWmrmdzWrOr3TEnb9cyON8iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توزیع ملی شاخص فلاکت
📊
بالاترین  مربوط به ایلام و پایین ترین  مربوط به خراسان جنوبي</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/16219" target="_blank">📅 21:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16218">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inkFxhbG4-6zaT0drR_TA1s7PJaoIDajPj62LwWYSgdry7TyFKEGsHG9OPPQJtG6ve9SOkv9ExuMdPI107tuK8TY2bS5PEG3sQ3aadNJ6dLjRXBdYaVpxbxCWNrP4GSr2pt5zo78gENCQLIwzYd4JlgkvtM70M421Pec3Udgj6ntpGobfpv8CvEtpMC5pCA4JpdrUY_dC6UbOwvUtG9-wjgaygx_EMpbnATNZq3Hzr3GdkC7ni8DyyOnTR_hiNW2X1hnYZScRAWwQoZWI7gxdo6HachoU9tOEhmbeWZh2CT4wDfo6b9ev9cVKzbOY_Se2K1ZDbu9kuprbq8Yto4TqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هند قصد دارد یک بندر استراتژیک در یونان را به دست آورد.  بندر الکساندروپولی در نزدیکی مرز ترکیه  یکی از پربازدیدترین بنادر مدیترانه است.  شرکت هندی که در مذاکرات با یونان درگیر است به احتمال زیاد گروه آدانی است.</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16218" target="_blank">📅 21:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16217">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نتانیاهو از تشکیل اتحاد جدیدی علیه «محور شیعه بنیادگرا و محور سنی بنیادگرا» خبر داد.  این اتحاد شامل هند، یونان، قبرس، کشورهای آفریقایی، کشورهای عربی و کشورهای آسیایی خواهد بود.</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/16217" target="_blank">📅 21:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16216">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cpt6fvANiDjPxmoIbDXlO7CVbubOo0HJOidbMc84xaXA-DfVJXOdQn-RMiNomxXLBBThbgXZ7h63j7rHsAaMZKZEukcTT4c90qeBV3ADEj3M5dnlKG1YNUBYsiXvOHw2w89mb3_5NJx7KYlm_uoXzdPEEsvqQsBqCONJNzC6obm8It-fSEGVPj9mPNT1aXyDv9AZ5n5HaCHnsOVBcE5sSHphreYgAh5TwpGK5x7apFjFST-gtjb-ful-t7boljXBBUGPQK7_cyq9S1WBdPuf4Zl_siEILCYKBvuhTU7N2yHLMnzXt3onrFw_1-IkjHJkjE04h_qBuq5MHi3Q9hTbFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه تیم ها دارند تدارکات عالی برای جام جهانی میبینند ما هم داریم اینطوری با خودمان ور می رویم!</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/16216" target="_blank">📅 20:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16215">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ژاپن معاملات تسلیحات مرگبار را در جنوب شرق آسیا پیش می‌برد  وزیر دفاع ژاپن، شینجیرو کویزومی، روز دوشنبه در جاکارتا با همتای اندونزیایی خود، شمس الدین، یک پیمان همکاری دفاعی امضا کرد، و پس از به مانیل خواهدرفت؛ جایی که نیروهای ژاپنی در کنار نیروهای آمریکایی…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/16215" target="_blank">📅 19:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16214">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKiYLUppf2pFYIZmMM37-ag6b7MTZshFFNcQf4-qEP2cY9ufuwusu0jbk77rbQkgN3MLYJkCA3sef71kmJWzD4EhAnAG-Zn85zaXAqZkpIfnmdV5o9DLSTW7nK5L5nMFGw4-U6QIOfW9SDtt6QZVzAKcOMtFthtR7bGXvHZiVTBoDu8aX32-i35ioESawCB27yPp8RH5otrnFoZMZvU0OwYpWREx2SrWF8sEF2Ipi0Jx5a90VeWOuFMZQHX22Y19Kh5AbmMDO-vOrWi3MIYXnqRqEzN4jXfvBwvVS-Y5H5ia0kkQO58Jg4d8td_lkNzC74jpuHxvaC3juPiIbpIAhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SBoxxx/16214" target="_blank">📅 19:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16212">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-FyEDfBc33EztBE_DogAiNqlzblex1CjId99ouzrdt3TYdtyShy2IB3yq_NdSVQuWG_4dk73e_KGcx9rhtKQJTWiJwNETs_-05FFvR8S2muLrb-G-b0KIcXUoFy60RePHEi2BTrX_SvmBJjIrVz4wFkNV2bdGGSDZAOAYORucEKlrNJNOhEa0i8bpYfiS-ZjSo7TipgkxIIzeafubVoz7TnOFhGaKaCtKbG2y3U0NKjQFxxdI6Tfw-n0Gc-roQOXaEwRkwohVZ0YRUijXq5BIvRewKudYDZ8uACBPYJ39Ut7OiKirNyQRqfCuafHbwA1SO2Bv3CNq-IDqvmdEdADA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ !
استخر کاخ سفید را گفته تمیز کرده اند و این را برای رنده کردن دموکرات‌ها سوژه کرده است.</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16212" target="_blank">📅 19:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16211">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ درباره ایران:
ما صد در صد به گرد و غبار هسته‌ای دست خواهیم یافت و کل ماجرا را خواهیم گرفت.</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16211" target="_blank">📅 18:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16210">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترکیه یک کمپین عمومی در اروپا برای ترویج پیوستن کامل خود به اتحادیه اروپا آغاز می‌کند.  شورای روابط اقتصادی خارجی ترکیه (DEIK) نامه‌های سرگشاده‌ای را به سران کشورها و دولت‌های آلمان، فرانسه، هلند، اسپانیا، ایتالیا، لهستان و بلژیک در روزنامه‌های معتبر کشورهایشان…</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/16210" target="_blank">📅 18:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16209">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترکیه یک کمپین عمومی در اروپا برای ترویج پیوستن کامل خود به اتحادیه اروپا آغاز می‌کند.
شورای روابط اقتصادی خارجی ترکیه (DEIK) نامه‌های سرگشاده‌ای را به سران کشورها و دولت‌های آلمان، فرانسه، هلند، اسپانیا، ایتالیا، لهستان و بلژیک در روزنامه‌های معتبر کشورهایشان منتشر کرده است.
به گفته نیل اولپاک، رئیس DEIK، پیام این است که عضویت کامل ترکیه در اتحادیه اروپا به "استقلال استراتژیک اروپا" و همچنین امنیت جهانی کمک خواهد کرد.</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/16209" target="_blank">📅 18:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16208">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQCwdqKBsNgSfY3AGkJS-KGlYS1NISp0juCj031eOJ6FZDu2mvP1l6jlR-nE_r1wHwv7ETRieQjv55AKuqoj8BqCUSAAwmdAyOjuLYjha4psEVkDJHE4Cw-KWZsIu4ckMzwo_i8deUfE82B7M9hw8U9fufiYfWqlYR-W0SF8fHfMb5MSrxnnUTOzL2NXVqNUgicH_B_MuiV8nAYUqsfKcWBlt4-AfjKOBJvvgJtHZUi1rSZvIE5Y2Bxs-WWywNvyGmdbhbnExNB4dPNnTQxPlh-98GSot7NCdtxgbySGGyXqu47hfFcQ1VM8tYP0r-aYsDlfusZ7yeoPSMRDdrlrJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#US500CASH
-- H1
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16208" target="_blank">📅 18:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16207">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔹
وزیر خزانه داری ایالات متحده آمریکا
:
تنگه هرمز خودش باز خواهد شد</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16207" target="_blank">📅 16:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16206">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فرمانده عملیات استان کربلا:   نیرویی که در ماه مارس در صحرای نجف بود، اسرائیلی بوده و بیش از ۴۸ ساعت نماند.</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16206" target="_blank">📅 15:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16205">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حقیقتا «الکسیس میانرودان» لقب شایسته ای برای عراق نیست؟!  تل آویو - اسرائیل برای پشتیبانی از عملیات هوایی خود علیه ایران، یک پایگاه نظامی مخفی در صحرای عراق ایجاد کرد و حملات هوایی علیه نیروهای عراقی انجام داد که تقریباً در اوایل جنگ آن را کشف کردند.  به گفته…</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/16205" target="_blank">📅 15:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16204">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_sNNFEdLRshpls3ilUJxzHQWkQ5co6Yt6S4W8KQNgt5Bnz6vtD0kk1VvzPDu3uaHUc8MxgUwOUTo05kCXE8AZ1ySX_ulrj0UDHvIu1y7ZOuF8y76TW-amo9amiJmgcJMyUw1y3SONwbCRsvRaxEsIEKEMrXQZl3i1prdBYikwT7l3QMmpCAYivuS1_tVMHSLer4u05l1n0CARU1oPXBbLPnS0RwEbM8Rlf19J3bXXamK3iJsEGoCtFbCgL2CvbejVPtlY9ooo6E1bf7x0oWbGb848pLFMpACCqCeCnuTgq0JLuPrkUAHc21klcm4gKbw5CCgd8nAU9yVGE0xuG9Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از یک شرکت کننده در رزمایش ضد هلی برن «قائد شهید» سپاه محمد رسول اللّه تهران
به نظر می رسد احتمال عملیات زمینی یا هلی برن آمریکایی ها از دید سپاه پاسداران افزایش یافته است.</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/16204" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16203">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KP1mjiNLxSLEoSMD9KgNT8C4yuvcqM06em8a2NfWHbiCa3m22xGPYPyXXdM_-DFBP1autGAnLrmEgL8T6b_Y-jbcvFFBqr0v_4u1k4gIOWxSWyQkfS6xTTqijYkNXYzcZjHl-Lf-h7C-WadD0bSYb6X0rn43XNXHpkuIt5VVGphO_SP6wC7lDtq3CeXZ1hFOpXn_UUtDw-rQrcR2vgU81FgV-G_F22gtgVSictMQ5q1Wdecc9rAIwIPuxlcxKF4gKoDOPHPqrDNODP2K_80uMN-Ts9LQSmGci5j1i4lhJk4LvCnlAduolaBlqqf91a9FijZz3-U4ZBKdSIz44yWC9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان وابستگی کشورهای مختلف به واردات نفت + گاز طبیعی مایع صادراتی از تنگه هرمز
کشورهای شرق و جنوب شرق آسیا بیشترین آسیب پذیری را دارند و آمریکا (گوشه سمت چپ پایین) کمترین وابستگی را.</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/16203" target="_blank">📅 14:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16202">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAbB0qNonW-hm9UqyuNvb1T31YrGTVdIv2jIVetGwdcBBL8AEz3V1pPGM08T1Q2nx5uHU9-ozNzwHhr27vQitvLMrVjW5Kxz57zZxKvTRZ8fIY910SM1Z4jP83oh-CwP3CWEj_3sYckteESFa-_P9YBPPovpFGSvGK_klwThLa7z7XxkE3rrFCE6ObS6nl5vinilrwMOD40y0eRSzMjrAA-bab_2tHNYlqnGQaZ9KQajJgAHYCBHgA76xxOOz-n-_O07PXenFwCwtDRg2Dz_GMJ_5-tEiX6Ky4tRggkCsou4nZDX9oew0v4KN-c8Xtq0eN7XRUrblGYApYiI8ZtfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD
-- H1
در محدوده مدنظر یک اصلاح 4.5 درصدی داشتیم. اکنون طبق مسیر ترسیمی رشد بسیار عالی داشته و در حال نزدیک شدن به سقف کانال است. از اینجا احتیاط و نزدیک کردن تریل استاپ توصیه می شود.
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SBoxxx/16202" target="_blank">📅 13:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16201">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJ96aa5YvWY-JpGKoTDy-_GtuA95ozwCxewVRludbb_31gSob-xisfp1O8kXgOm73IPakLnm5W4sfoh0DWqT0uKFXU7wuMAobw76mf-qTgkG3OZlaTLD0-7KehA42DZEYdsebWrkUIqAfAEsGAWIBga4fdcr35iCVI7YIxeWOKsl9febwz-M8gLBjkcPgoFrowbqWiUX5IHGrZvUOaBvRsojyoFr73FWNRcPJjUhOzilpwu7eqCOnpQaAy2U4aEFmDmUO-CQK2_chlCYXI6hSHRzx_Pvi-DauZ8y6eoFO3gCBzS03uu7QRJVNxwWUkw4bNJB8WfZUEeLvaPmubXXEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD
-- H4
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/16201" target="_blank">📅 13:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16200">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9f00l8M8LJn7cByYxiRFS8Ei2oot10Y1UFlf4wR_qmdztd-BN9_zPLIEJQNzfAtuX9_0gJAp4rdFVlHt0FZ5YoAj_qif_C23a9QhHkQ74QxRhI0qgV2fOrwShF3lk-S7w5YwgIO2eNscwnouG-lO2i5rHiVZhyehZMI3vUjrU8qhVS4FXdFBTGOMt82hXFD7iD1gZvEtCCmr_pQ3gefq7x1LMivoR4wFIEuehnzH01umlqQ4wrTGuTfYNCtaYod8j9wiQsMC2dvwA7Fx7sXQ15XyT7fcaeoY4H8uRac4F0Fn3NU_jCyeaZeEPMHAabAj9NKsKUdpNDgWe-SYHNYKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ایران و فشار شدید روی ذخایر ارزی و طلای ترکیه !  طبق داده های معتبر، در یک بازه بسیار کوتاه—حدود دو هفته در دوره تشدید جنگ —بانک مرکزی ترکیه حدود ۲۰ تا ۲۲ تن طلا را به‌طور مستقیم فروخته و علاوه بر آن سوآپ‌هایی معادل ۳۰ تا ۴۰ تن طلا انجام داده است.   در…</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/16200" target="_blank">📅 13:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16199">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">CBS News:
پس از اعلام آتش‌بس میان تهران و واشنگتن در اوایل آوریل، ایران چندین فروند هواپیما به پایگاه هوایی "نورخان" پاکستان اعزام کرد.
این پایگاه نظامی از نظر استراتژیک حائز اهمیت است. منابع به سی‌بی‌اس نیوز گفته‌اند که پاکستان با اجازه پارک هواپیماهای نظامی ایران در خاک خود، احتمالاً آن‌ها را از حملات هوایی آمریکا مصون نگه داشته است.
محموله ارسالی شامل یک فروند هواپیمای شناسایی و جمع‌آوری اطلاعات آر سی-۱۳۰ نیروی هوایی ایران بود</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16199" target="_blank">📅 13:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16198">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">#ITA — D  اینکه سرانجام ترامپ برای 3 روز هم که شده میان روسیه و اوکراین آتش بس برقرار می کند و سفری به چین دارد که اینقدر دستکم از دید خودش امیدبخش است شاید همان گمانه زنی را تقویت کند که بزودی یک صلح بزرگ — یا دستکم وقفه ای اساسی در روند جنگ ها — در جهان…</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/16198" target="_blank">📅 13:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16197">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اگر آمریکا دوباره به ما حمله کند، با ۲ بار قبلی می‌شود ۳ بار !</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16197" target="_blank">📅 13:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16196">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">عضو کمیسیون امنیت ملی مجلس:
در صورتی که آمریکا دوباره به ما حمله کند، غنی سازی ۹۰٪ را استارت می‌زنیم!</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/16196" target="_blank">📅 13:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16195">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">Secret Box
pinned an audio file</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/16195" target="_blank">📅 07:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16194">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNoPh6jaipeuEpc9I8DUNOz4jFFsN_1QA4Nms8ErtGIzjPt1WziWF2Qr8POWehQvdvBpqLE_iAIqdwKlqfKVev4qT_jFimCIgC177VLSP-BLl3eTsbzDmDHih7Zy-ywKDhD6jQrncVwpqPjdwnJyhGXLAb3G7meT7GLmz8oA1H0yC_2t2pGqMeSmtKtKKagKs3n-P4m8wSn2WW2qDIUqAZs2HmXQ-NmuzstdvBfRaylb-0cjjkckgQ_G_uATrrbP2I-lb3dqjTWxSqX9pQwVLJ7vG4veMIuvl8JYqD-MJxHyg_fJb7jzu7p5pfMNLf1_dM7ns1wtA85OtXyKjWoKDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلی مایر از شبکه نیوزنیشن با دونالد ترامپ، رئیس‌جمهور آمریکا، درباره احتمال اقدام نظامی علیه ایران پیش از سفرش به چین گفت‌وگو کرد.
ترامپ از اظهارنظر در این باره خودداری کرد و گفت: «واضح است که در این مورد با شما صحبت نخواهم کرد.»
این در حالی است که گزارش‌های اکسیوس حاکی از آن است که دولت آمریکا در حال بررسی یک کارزار حملات محدود علیه ۲۵ درصد از اهداف شناسایی‌شده ایران است که تاکنون هدف قرار نگرفته‌اند، تا تصمیم‌گیرندگان ایرانی را به مذاکره بر سر برنامه هسته‌ای خود وادار کند</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/16194" target="_blank">📅 06:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16193">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/16193" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یک سری اینجا منتظرند چین هم به تایوان حمله کند مشابه آنچه روسیه با اوکراین کرد تا جبهه جدیدی ضد غرب و آمریکا شکل بگیرد و این سمت ما پیروز بشویم.  در یک صوتی توضیح میدهم که چرا به نظرم این ایده یک توهم کودکانه است.</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16193" target="_blank">📅 03:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16192">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSduco6JFXYli5EN_2ed9vBsfYGP4yUHPpa48Nmsvo1S_BgsFpYDN4uegujx4WzJecppQYyI5z8S6VSqzjHu6qBqgYW1OE2QncEm0Cy_JxDur1AWPQY3ni52OYDW3l4jv65xn4xha4uj2iq7zx0IbUsZKHQzX4g7b_l0bkEZGmNAUhBB-kCSzuf73rs1wFVt3iFoxihpvJqr_HIPIWTr-MFO19r5V-RoJ-CxHnmkz1Z75tpKGM9Qz2lpLx9gDCrRp3eNSDg6rciW8_usS-zuWRQTVpJ8WbDgRU1DPiz1TRR-O-ZyyMqLYzyZ5rPvw4Y4Rby8O1NTLOFztl0JDHGnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش ایرانی سی استار ۳ همچنان در نزدیکی بندر جاسک در حال سوختن است.
این شناور اواخر هفته گذشته در اثر حمله هوایی نیروی دریایی آمریکا در بندر آسیب شدیدی به بخش عقب آن وارد شد</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SBoxxx/16192" target="_blank">📅 02:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16191">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwuGieDWdZjU2vyQDoYKtnzuHVloTGeYX9CpWOXIt03imvpgMhWEAbLbZbg28Jos4Z3PMRF-ujmedgf_JL48d1MGt1Pm1WxonOVfGfHSeVrE5Oe8tyItPbeau4WJKrZASF__6Gs4tbBWWc7FVBH6u819--L78m5IHEgBKrwnxvWbWbH2wIa6e3gzVOruGaKNJ0VMDOku88uN_Rwla8ic1cXr-Q-Tu38449TEIlXuyUOVabHQI63efeeYWaFOycs1O-z2PMehAkm2pnUHX-kSql6jVTsgFEmo515MK6dsT2T2kxv4LFYad9qYZ9T6_hkibutaIpEKPe74juuTN7xIfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Rheinmetall — D  ببینید چه شد!  بیش از 23% ریزش پس از شکسته شدن خط روند.  به نظر می رسد واقعاً دستکم یک آتش بس موقت هم که شده داشته باشیم.</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16191" target="_blank">📅 02:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16190">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvVl2vjJPI6Nd7echXADsDzV51q80PNcU9BPJDGmC_rekkl-utjWyiravAyZxR18_kanRZ62NsVPpZeoQNS8N965KrmVl2yEEV-1-NlxZjRWE7XhOi542xms50J5QKo-8IY-kLgRPEnPRll1jSYP_gEXbgTM-84Y9ZxQ7MvtK5WV0HlFaG1gKWqSQXWM8bFOKf0M9soYAdLrxIrtHEEmyieH0YW8-CzxaLSC0L0YUw7g5_krXduGygMgZUwW8nEnTo8ysIqBPn_zEiq0pSKzmS6TrHAJZId3e_C2wdjybgz4tLquAKz9VocoM071jPGBoDAuVN0hZnx70dkeXolbWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ITA — W  به نظر می رسد این صندوق که شبیه ساز صنایع دفاعی آمریکا است در آستانه یک سقف اساسی قرار گرفته که به معنی کاهش تنشهای نظامی در آینده نزدیک است.  در صورت شکسته شدن کانال اخیر می توان با قطعیت گفت که فعلاً جنگ بزرگی در جهان نخواهیم داشت.</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/16190" target="_blank">📅 01:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16189">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObMYzdSMoRuVM2nCU698vZG-_QD5Ss3pthu1ywlG0BpOXjMevYQjI-Kzqieg3pfXvqc_n03r8Dg_ypzCGTmQHsbPWfUuu96Dn7R8dAQ1DLZh4up_9xJk2I5_VAcaz65BfsyH9GkKSEtFyn5qMwlkbuLGQUBZjZdJGJXek97A_gzeHX7K-t8HQTW8xx44TORBDYPpgVBYdbAi4ib9-FnAl-rhOzv3NhZFSS1ysEYeNR0kIht6aqWOpF0KteGqHtJVFl8Bli6A4k9T8GZeBEfAvT2gU-70yqxtiyjBMECrthMfq8dfgiCbOgGUDLopiojs7gQz4RxOituAaPVCVeWIcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سحرخیز</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SBoxxx/16189" target="_blank">📅 01:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16188">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0JTqVndtdWs0abhFW1iS0zGXEyPEDp4OGPg-hsUclWWx1UjQcK5J5IKY9Qx65kbIzsy5UKkFvkPOScOOAZSij25cIC56chq5Q7ioQesHJjjrAMh2wzIem7NWR49RfkagkWJqHGZHG_a1gaBw6-RDSSQSx4Xdq_Gp9JRp4HxhTPr_6DJX6qyu8x-RCMVAa6JVscDOagplPiBNiyV5Yvnngi9J3vAT1Vzzzy25d-HxqJ5KXBo7BKzsXOcnEM_r39QVQDoJLb_4e5SOUveDoQ1oTqOgXxkarD1-oQLEg7sC5zt-yrRlwxw2vsn1pgrFgjBcKLPqzA19-lWYecWFNJTIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سحرخیز</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/16188" target="_blank">📅 01:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16187">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uB-jMmTl19e5lEC2anCrqyJPDlRn6o6hz7rFcuqAbj7XvkQaPr-9913AF5cQbjsFUKxgIYSrNTjrEHkP0iVbU1MiXVgTUJcJbLeXCMK9-PDWNP6D9Lwhzt2KRQ8RqCo84hwamNQ4GSDlLwHfq2auw6IRoK8DWkCv4jOoWvTLn2Pvu0BMudwuUkf6x-jrYKnmBxueGT3bVhiswnPL3EBe4mDvXAgHaPzy0wfO1-2_ivD41l7_34FzK_xZE2Fy6p4ZQehpclGJJVHOQeLZmw3Y-Qv8rbeh808SAYZpBmDDvEK1PUsgPIxLphXXl6BKVfOEMfAiiU1dqqSPK6FqROWIQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نهال</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/16187" target="_blank">📅 01:41 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
