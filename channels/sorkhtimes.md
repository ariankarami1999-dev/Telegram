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
<img src="https://cdn4.telesco.pe/file/nBXE8GDzQwgQletVowe28iQN2FnmT99t00mSV3TZ0bMks3czizjWjhJbIwmTcAI1siENorOWZFkOSMl33nXOZOmzG9XKlq_Sdt9E4JtH7sgy_QXz6us2FfP7wpTAmbFAdvzbjiJ7eMPQ95phthkicjm2witM99E708ZpWWpPAEyv3tdR8EPbTZeY9fsaXZNqMpT9y8M2U27iR5n7ca4FMvSe2YSbDwIM9e_OJqZ8CegjoPsMQuW6ncaFgfgKG190SuisE4lO_-QiKt05VtG6J_A0IzNvKfKq8iD1EmrsLVHZwLyEAf9JG7CHZsukjVJKx1sU4VuYqF5odGtxd3u0NQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 15:20:27</div>
<hr>

<div class="tg-post" id="msg-138862">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
فوری، با اعلام مهدی تاج سهیمه آسیایی ایران در فصل آینده لیگ نخبگان به 3 تیم افزایش یافت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SorkhTimes/138862" target="_blank">📅 13:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138861">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔄
❤️
❤️
پیج باشگاه 10 میلیونی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SorkhTimes/138861" target="_blank">📅 13:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138860">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔄
❤️
❤️
پیج باشگاه 10 میلیونی شد
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/138860" target="_blank">📅 12:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138859">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
❌
حجت کریمی مدیرعامل باشگاه تراکتور:
🔴
سخن‌گوی سازمان لیگ اشرافیتی به موضوع نداشت هم‌چنان درحال رایزنی با فدراسیون هستیم تا بازی تراکتور و پرسپولیس با تماشاگر برگزار شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/138859" target="_blank">📅 09:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138858">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔄
🔄
فوووووووری
✔️
مهدی تاج: ورزشگاه آزادی نیم فصل دوم در اختیار پرسپولیس و استقلال است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/138858" target="_blank">📅 09:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138857">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGKE6q6Vu_mrjwTxRaSjWzi7pJir8oc9XOjNrCrwNYhUcuNGTHqLKjb9JwezhHuZENQmR3h-UVD4nDe7ZSWMYltXDsW8tNGJ7sBt4wIG7R-QYrjnLIaDszYH2kKumeGVEF8_Ljje8HCcuWLvsL9c209vgWaRM6FbnZW4sZCNenTIU0hABaGqoBVXe8ZpuSpO74tmFuIYqYZq8cLSYC2bECP85syDrUO5qnHdxtQC6wrmCLCXU-eRrch1_ijPb56AyXXpeoWI18Mtjyc2jXUpV69oy3xbpW4A-Mlzx0q02UBKrghn0rMWrvpNF7tXOSE6vK4F2pJ_1lnduDDUAOD7Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
ترکیب احتمالی پرسپولیس مقابل تراکتور از دید ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/138857" target="_blank">📅 09:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138856">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
فراز کمالوند: یک بازیکن از پرسپولیس برای معاوضه با ابوذر خواستم و اگه اتفاق خاصی نیفته بزودی این انتقال انجام میشه!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/138856" target="_blank">📅 09:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138855">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
تارتار:
🗣
🗣
فیفادی که نیست‌؛ به تیم امید که هیچی به هیچکس بازیکن نمیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/138855" target="_blank">📅 09:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138854">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
🔴
🔴
🔴
صبحی که ی بازی سخت و نفس‌گیر داریم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/138854" target="_blank">📅 09:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138853">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🟢
تنها فقط تا پایان دوشنبه برای بونوس ویژه SCARABTEMPLE فرصت باقی مانده!
🔵
همین حالا با هر بار شارژ حداقل
۱ میلیون تومان، اسپین رایگان متناسب با مبلغ شارژ
دریافت کن!
🔵
شارژ بیشتر؟ اسپین بیشتر!
🔵
هر چرخش، شانس دریافت جوایز نقدی
📌
فرصت محدوده؛ زمان زیادی باقی نمونده!
🔗
اسکرب‌تمپل
، با یک سیستم اسپین پرهیجان و جوایز متنوع:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/138853" target="_blank">📅 01:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138852">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
مخالفت با معاوضه و انصراف پرسپولیس یا مصاحبه ساختگی ؟
❌
❌
فراز کمالوند در واکنش به مصاحبه منتشر شده از سوی وی پیرامون پیوستن ابوذر صفرزاده به  به پرسپولیس به شرط معاوضه با بازیکن مدنظرش به رسانه باشگاه خیبر گفته:
❌
❌
من هرگز چنین مصاحبه‌ای انجام نداده‌ام…</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/138852" target="_blank">📅 23:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138851">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c596c40e2b.mp4?token=mQ9eVEbTlIEV7-BwmbwSiLjm4gBz74hFMFYpq8-nV8vOgQtqR_RcZxH_IwnROxbGSF6IuGD5wlVcHHfSYeYdQIeQByu9Br_ZGVJftzFPAacQprzCewWq0N3QCpW5BYU_9GNiF7jgWLKOFd84C-J056BaIWhoVvXVeE3Thzvl4YVinb16zo2_FScc2WzgdoIhVJvlsc7NbcI1QgpKfM2GhoFE_WjyWnumi--3nVFF5vsiopvhRAH4rr37FcM-3RWZ5Jsd2lrAjZnuOZDC3KWcvfzxqwsBqdETF9G95GfFD4W1QFF1d2yir6bJ1gm7OkBdGhfwmpLSI6E5O9yhCfxq2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c596c40e2b.mp4?token=mQ9eVEbTlIEV7-BwmbwSiLjm4gBz74hFMFYpq8-nV8vOgQtqR_RcZxH_IwnROxbGSF6IuGD5wlVcHHfSYeYdQIeQByu9Br_ZGVJftzFPAacQprzCewWq0N3QCpW5BYU_9GNiF7jgWLKOFd84C-J056BaIWhoVvXVeE3Thzvl4YVinb16zo2_FScc2WzgdoIhVJvlsc7NbcI1QgpKfM2GhoFE_WjyWnumi--3nVFF5vsiopvhRAH4rr37FcM-3RWZ5Jsd2lrAjZnuOZDC3KWcvfzxqwsBqdETF9G95GfFD4W1QFF1d2yir6bJ1gm7OkBdGhfwmpLSI6E5O9yhCfxq2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخی هواداران ترتر جلوی هتل پرسپولیس جمع شدن و دارن سروصدا ایجاد میکنن تا مانع استراحت بازیکنان پرسپولیس بشن!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/138851" target="_blank">📅 23:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138850">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
فوووووووووری از ورزش سه؛
🔻
سرگیف و علیپور زوج خط حمله
🔴
بیفوما فیکس خواهد بود
🔴
اورونوف نیمکت‌نشین
🔻
تیکدری دفاع راست
🔴
عیدی دفاع چپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/138850" target="_blank">📅 23:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138849">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
رونمایی از کیت دوم پرسپولیس به یاد کودکان مظلوم میناب
پ.ن نظرتون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/138849" target="_blank">📅 23:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138845">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O7BW4Ww2_9AbtN_oDaGo5hAm8el-Mekb5Y5LNTZjvepmQhJrIOEsPlQ74By51ehzT7eXH_NeHBaidYcY2_2GfAhXO5sBiq0MLtmHEvgsbWLKX1XDsRk05Cc_pTGKhXmt0e99niqbW73y1EVCTVbqQsvu37pNaL9sUdvdFWgcoyBpu0EEuG4YCiirWxcgRr868jHfRT31QpDZb1nPzbf7c7Sx6VMA17UY3lgdC6fqzI0dDZOrUJ1qkyIjRLje0jWDqmzqyyJzTzpYgHHZiBZI1FGC1Z1zCFeM7slO5SClZK7U6DDAPjG6B9AN-TkleprPotyF0OfQZ3duEtww26uhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ucMdS_-RwEJggPysVhC6JcGPwcts7GazrTtVSUegVPeBBcSQJvA6jAHWUT5gkBXMg01C-SHKJhlWADkknZvvRLWlRxrLmWnxCCNdoKGNs7C8IHMP4-gOqbyRxxrD5LH-OVW2NUU-eiCo4bGEngbhdqKr9BVfCde4f2kWjK00U4JqA0ThGlsT14Iz93L9-cMAzY1JL3mKyX1r54avL7gkYZXL7Qga_m70FhXjdpZBMHF1Lvm-9IF1XLbxMxBaZKTqbBkO3smsR38UXT9pJ92mfP-L1g2wpxWqXBe6Z9T4YQKMbt7n9bzyXOjGDc-kxE1eC3q4uFpiOThNdQ_OLaEbqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hYEiccYGsY3sy3BCFL0q5z5owwTmXsYZdzPR_ywF3rnzvABcLQo-y9JQyKWHvqKjpYDHXQ2qqb7vOjyfLRQMlPUVUAymVWt-Q5Qzg7SXaY3jpiCToGmd1T_F8ctY9VygwZX2t0FWBNdRDON-iadrD7zw4GIge310k9UP3TIGhaFDGq7Jf4E4nW9V_EC9BDg9wmCx-KbpJwyAaZMc4ot8gj14zNpLv3Ki2WG11-dBA8SESbjAL2wyKDyF21KXhk5yNHNMKCTdgZ0QHvzPgZedTgb5gsDuFE0HiKCCqysrJPbFHt53pucRTNOjJMG8D6Vx9n1YWbO8IP3Vriykcwtaog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1E1bsVW8R5DW2R_3fe9rrvD9qAY9Uvzl6FM5DxgJSjwUdRT_E7pdB8SKd-bHqP6BJzC-0LdSHZdLYq-3ClKf92-J8DKALbzVcbevNCKd9kOxV3hIzzDkp1W8NZqxT-ZesYrUrswZrfPb9um7-mosQREKb7WjjsD1rCF8HbxNRYjWvSrau79Og5nGf4wXijJxdLb83c2Kkg9aA5ds4WKVPdn0Bsb7Z4DVoGsdEYFHiQe7mRSbpcv4eGGIm_l1N-2aYWM3v8OPGAE0A1ZP5sTlIR2kY90jO1R42kX6naqLes_FBk3eagbR50oVikQ5tuG7R09gNd3tHy2Yz0AHC2UOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
💢
پیراهن فصل‌جدید بعد از ادیت نهایی رونمایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/138845" target="_blank">📅 23:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138844">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
🔴
ترکیب احتمالی پرسپولیس مقابل تراکتور از دید فوتبالی:
🔴
نیازمند
🔴
تیکدری کنعانی زارع عیدی
🔴
پورعلی خدابنده‌لو
🔴
بیفوما محبی
🔴
سرگیف علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138844" target="_blank">📅 23:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138843">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🤝
🤝
🤝
کمالوند، سرمربی خیبر: ابوذر بازیکنی است که به کار پرسپولیس می‌آید
✔️
✔️
ابوذر صفرزاده از خریدهای خوب امسال ماست و من به باشگاه اعلام کردم تنها به شرطی که مانع جدایی او نخواهم شد که با پرسپولیس برای خرید یک بازیکن جدید به توافق برسیم.
✔️
✔️
ابوذر بازیکنی…</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/138843" target="_blank">📅 22:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138842">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
میثاقی: کمیته انضباطی شکایت مس شهربابک و نساجی مازندران رو رد میکنه و گفتن آسانی مشکل نداره و هرکسی اعتراض داره بره cas
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/138842" target="_blank">📅 22:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138841">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🤝
🤝
🤝
کمالوند، سرمربی خیبر: ابوذر بازیکنی است که به کار پرسپولیس می‌آید
✔️
✔️
ابوذر صفرزاده از خریدهای خوب امسال ماست و من به باشگاه اعلام کردم تنها به شرطی که مانع جدایی او نخواهم شد که با پرسپولیس برای خرید یک بازیکن جدید به توافق برسیم.
✔️
✔️
ابوذر بازیکنی…</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/138841" target="_blank">📅 21:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138840">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPBMsjpyVmc_aIOg1eAEHkW50pnV3_0VPbQy69-nP5r0ZqJzTLjdOaFWaqZMRR1k-bjZCVPI-tCCcVkFs_WgMsVEOLealbOXwkgOKpq2j5KlHFjFCsEp1ojnlk9woRXV1cCzrdQaRVqmOxDXECVFNtVSddkPK78yq77_oSHnlDSANxD58h-lfSgW6DNCNCJns03QMUZtIG14g9KGC8ZK0IMRMKo48yx3BFNEj3wNuGn0RPhQ6wEXjrPntyxWzdaavzhOOf071BWbqu7qGtjuLL6ZhzG7VkP9s0G6Jr_v05pdH5EJyuTasbdbVtlrnzrb1i7sSkQDtixxMZVqMa0XvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام ترانسفرمارکت؛
علیرضا عنایت‌زاده به صورت قرضی به مس شهربابک پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/138840" target="_blank">📅 21:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138839">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0i0rPmV1W0yhgM3PcyIttsWxISnGZVXYfkzp1FhYPZKfDzazoaDLaIHFlKuWimjLTaBTBnC8ulUOiyuV7IDOs1pB-3LGKbPj8X8RVQBYvgFyKrdJMHjhJ3zsAcVvAV9j8mPY_PdPuxyi_ioYksm33giC9BCILAseB2UW8ClNCcNSiawLcyLA3n3xBavh9ykj-kuJY5ZAauzLCycqIpexR0aRn44WLeg2KYsPJqVtso_9Hbs8RPhs3MUakHtBsx2S2Zypcy0cGlWOvkZv93yIsGbS437lhVjeo1oFDzGHsjOmps8RVDMRqo5gcuUymR93QvmC-vekgDwO7kKSKla-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
نتایج بازی‌های امروز هفته 3 لیگ برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/138839" target="_blank">📅 21:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138838">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
❌
کیسه دو بر صفر از سپاهان جلوعه.....
❌
❌
سپاهان خیلیییی شخمیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/138838" target="_blank">📅 21:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138837">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
🔴
ترکیب احتمالی پرسپولیس مقابل تراکتور از دید فوتبالی:
🔴
نیازمند
🔴
تیکدری کنعانی زارع عیدی
🔴
پورعلی خدابنده‌لو
🔴
بیفوما محبی
🔴
سرگیف علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/138837" target="_blank">📅 21:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138836">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
✔️
✔️
۷۲ ساعت سرنوشت‌ساز برای پرسپولیس؛ تلاش برای جذب گزینه‌های نقل‌وانتقالاتی
✔️
✔️
در حالی که تنها ۷۲ ساعت تا پایان پنجره نقل‌وانتقالات تابستانی باقی مانده، باشگاه پرسپولیس تلاش می‌کند پرونده جذب گزینه‌های مدنظر خود را نهایی و ترکیب تیم خود را تکمیل کند.…</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/138836" target="_blank">📅 21:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138835">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
حضور هیچ بازیکنی در ترکیب پرسپولیس تضمینی نیست و تارتار از روی عملکردشون در تمرینات ترکیب میچینه/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/138835" target="_blank">📅 21:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138834">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYcppC6Dilw2TCqwz8SG7vZAVYD--6jOcqNC2m6RDRJKOYg7jx498ziumzqHZpzSkNfO53B2X8D-eu1Gr5PlqjW9AL652IkI4j6iM-mLOXkmof2-hqz9SxcrFlIetv4u0mZfrI07qfzvji8uuWp_cw8vCm0KoPStDwmiklQTvd6aivziiw6S2q1YjzV6bM_xQziHyKkXcbEVzlO1oMIqtGnPHKUEXjb2vhhIX22lWmV2HE-9vHfLaHmGP19d1ZYFkLMQROwqJGxaarBQ_9dsts-f4AEBlZRsFkSwGzwjXTsu2S07qy9VMeYSSNnIirLjlBrTGInNdP35kCH3JlYLDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تنها فقط تا فرداشب فرصت برای بونوس ویژه بازی Scarab Temple باقی مانده!
🔵
کاربران اسپورت‌نود می‌توانند با هر بار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود ‌اسپین رایگان کازینو دریافت کنند.
🔵
هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد! با هر چرخش، شانس برنده شدن جوایز نقدی را دارید؛ جوایزی که بدون هیچ قید و شرطی مستقیماً به موجودی اصلی شما اضافه می‌شوند.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
📌
نسخه جدید سایت:
Sportn5b2.com
📌
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138834" target="_blank">📅 21:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138833">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🤝
🤝
🤝
کمالوند، سرمربی خیبر: ابوذر بازیکنی است که به کار پرسپولیس می‌آید
✔️
✔️
ابوذر صفرزاده از خریدهای خوب امسال ماست و من به باشگاه اعلام کردم تنها به شرطی که مانع جدایی او نخواهم شد که با پرسپولیس برای خرید یک بازیکن جدید به توافق برسیم.
✔️
✔️
ابوذر بازیکنی…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/138833" target="_blank">📅 21:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138832">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
با اعلام فراز کمالوند سرمربی خیبر خرم آباد ابوذر صفرزاده به پرسپولیس خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/138832" target="_blank">📅 21:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138831">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
تارتار:
🗣
🗣
فیفادی که نیست‌؛ به تیم امید که هیچی به هیچکس بازیکن نمیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/138831" target="_blank">📅 20:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138830">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
فوری؛ بیانیه کمیته انضباطی علیه استقلال تراکتور و گلگهر: ندادن بازیکن به تیم ملی در هر رده سنی به هر دلیلی تخلف حساب میشه و حضور بازیکنان حاضر در لیست در اردو ملزمه و هر تیمی سرپیچی کنه باهاش به شدت برخورد میشه و بازیکنان از حضور در لیگ برتر محروم میشن و…</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/138830" target="_blank">📅 20:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138829">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
نکونام:
❌
تارتار با گرفتن سهمیه آسیایی با گل‌گهر کار بزرگی کرد و حضورش روی نیمکت پرسپولیس هم نشون میده که واقعاً لیاقت این جایگاه رو داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/138829" target="_blank">📅 20:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138828">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
جواد نکونام؛ مهدی ترابی به دیدار حساس‌فردا باپرسپولیس رسید اما مهدی هاشم نژاد بدلیل مصدومیت این دیدار رو از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/138828" target="_blank">📅 20:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138827">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
✔️
وضعیت عمری امیدوارکننده شد
❌
❌
وضعیت محمد عمری که در دیدار مقابل استقلال خوزستان دچار مصدومیت شده بود، بهبود پیدا کرده و شرایط این بازیکن امیدوارکننده‌تر از روزهای گذشته است.
❌
❌
عمری امروز تست نهایی پزشکی را پشت سر خواهد گذاشت تا مشخص شود می‌تواند پرسپولیس…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/138827" target="_blank">📅 20:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138826">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
❌
فوری از عطا حسینی فرد نزدیک به تراکتور:
✅
هاشم نژاد و ترابی به بازی پرسپولیس نخواهند رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/138826" target="_blank">📅 20:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138825">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
حسینی قشنگ داره بازی و برای کیسه در میاره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/138825" target="_blank">📅 20:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138824">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
سیدحسین حسینی: این توپ ها تازه به لیگ آمده و هنوز به این توپ‌ها عادت نکردم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/138824" target="_blank">📅 20:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138823">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
▶️
⚽
به گزارش رسانه «سرخ تایمز» جذب محمد قربانی به دلیل مخالفت باشگاه الوحده به انتقال او به باشگاه های ایرانی منتفی شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/138823" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138822">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
با اعلام فراز کمالوند سرمربی خیبر خرم آباد ابوذر صفرزاده به پرسپولیس خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/138822" target="_blank">📅 18:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138821">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
✔️
پرسپولیس به دنبال جذب ابوذر صفرزاده مدافع چپ سابق تارتار در ملوان بندر انزلی/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/138821" target="_blank">📅 18:51 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138820">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
فوری؛ بیانیه کمیته انضباطی علیه استقلال تراکتور و گلگهر: ندادن بازیکن به تیم ملی در هر رده سنی به هر دلیلی تخلف حساب میشه و حضور بازیکنان حاضر در لیست در اردو ملزمه و هر تیمی سرپیچی کنه باهاش به شدت برخورد میشه و بازیکنان از حضور در لیگ برتر محروم میشن و…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/138820" target="_blank">📅 18:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138819">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
❌
استقلال، تراکتور و پرسپولیس اعلام کردن قرار نیست بازیکن به تیم امید بدن! با این حساب ۱۰ ۱۲ تا بازیکن از این لیست خط میخوره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/138819" target="_blank">📅 18:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138818">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🤥
🤥
#شنیده ها
👀
مهدی تارتار قصد دارد در دیدار مقابل تراکتور از سیستم 3 دفاعه برای مهار شهریار مغانلو و حسین زاده استفاده کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/138818" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138817">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
همه شواهد و مدارک حاکی از سرباز شدن علیرضا صفربیرانوند پس از بازی با پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/138817" target="_blank">📅 16:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138816">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
پرسپولیس تا پایان نقل و انتقالات ۲ بازیکن دیگه جذب میکنه/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/138816" target="_blank">📅 16:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138815">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azIVlsV1jXwNt_E_LCEC0RjDe38jgm3YG9ZUG1g0pO3KDqjJFX8YmcHNmfe7gvFkUaBRvn86TJoJpznxWZbRr7d3qAF8I3dJGIF-1p2KTMWkyKkE4k1C2DD7mYwFY6QGehXuyqQ_a97Oy9IaHoLzsFnrwYdXjbamYFpaOHJ_VV-sNrbqZhUdCt3_JOdOQA_HdPUFRVpmzZV5xhA7KkEIEGxwreBLozyU01fXhY3gb1iq4VuPx1WfHV70vMLZTvN5BcGbh_z81h9BlHtJCXKv0uwp11NeuCTSQbbxZF1Kh5rRNvgvgwUUut_uQHwHAhWeyO5oyJBFRk_TGAiIf4Wn4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
همه شواهد و مدارک حاکی از سرباز شدن علیرضا صفربیرانوند پس از بازی با پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/138815" target="_blank">📅 14:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138814">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
مدیریت پرسپولیس در تلاشه تا ۷۲ ساعت آینده قربانی و امیر جعفری رو جذب کنه
🔴
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/138814" target="_blank">📅 14:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138813">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
✔️
خبر سرباز بودن بیرو به هیئت فوتبال آذربایجان شرقی ابلاغ شد
👍
بر اساس آخرین استعلام هیئت فوتبال آذربایجان شرقی از سازمان نظام وظیفه، معافیت تحصیلی علیرضا بیرانوند تا اول مهرماه ۱۴۰۵ اعتبار دارد، اما طبق مقررات فعلی، او تا پایان نقل‌وانتقالات (چهارم شهریور)…</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/138813" target="_blank">📅 14:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138812">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
❌
فووووووووری
🚨
محمد عمری به دلیل کشیدگی از ناحیه آرنج دیدار برابر تراکتور را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/138812" target="_blank">📅 14:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138811">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTBEbx2rL4M93FtYvZeJZQ8UcQburEp0_iLbPB-ULqowB-NF3z_I1DKz9Wgcu1G_eD2bOFlEJ6nPeIhZmUSqNzOb1Xd1JlmcQlbzMk2E9sn4dspaj56aJLj7Uf9_rbY7pEDISSJbxeT6TmfHbTftq6kx8ABz-IvHpSXhGEGgdg4GjYy6SxsCL54v6lF-oXJW3j7YPlDSr0VKuV8Mg1eMiPOj64UrgDaLJoBlISLYtsEV47cy3bfrbT2lujOMwloolzjXKrFnGrAKhPRzZBOBR3xcRzfjAucmIkNFnQbTDKc_vm0U9xtAWfGkMEb41iAp3MaCtCWgRbiMkbmmfTOjmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبرد مدعیان در شهر قدس!
استقلالِ آماده مقابل سپاهانِ مدعی؛ یک بازی حساس که می‌تونه معادلات بالای جدول رو از همین هفته تغییر بده!
[
استقلال
⚽
🆚
⚽
سپاهان
]
🔵
بونوس ویژه بازی Scarab Temple در اسپورت‌نود، کاربران می‌توانند با هربار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود اسپین رایگان کازینو دریافت کنند.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/138811" target="_blank">📅 14:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138810">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🟧
🟧
اطلاعیه‌سازمان‌نظام‌وظیفه: بازیکنانی که مشمول خدمت سربازی هستند تنها میتونن در دو تیم لیگ‌برتری‌فجرسپاسی و ملوان بازی کنند و امکان گذروندن خدمت سربازی در تیم نظامی وجود نداره. علیرضا بیرانوند هم اگه معافیتش رو به هر شکلی تمدید نکنه تنها تا 4 شهریور فرصت…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/138810" target="_blank">📅 13:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138809">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
❌
فووووووووری
🚨
محمد عمری به دلیل کشیدگی از ناحیه آرنج دیدار برابر تراکتور را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/138809" target="_blank">📅 13:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138808">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
مدیریت پرسپولیس در تلاشه تا ۷۲ ساعت آینده قربانی و امیر جعفری رو جذب کنه
🔴
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/138808" target="_blank">📅 13:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138807">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
پرسپولیس همچنان در به در دنبال مدافع چپ ..این معضل ادامه داره.. کسی برای جذب نیست ...رایزنی ها ادامه داره ///قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/138807" target="_blank">📅 13:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138806">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/138806" target="_blank">📅 13:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138805">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/138805" target="_blank">📅 13:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138804">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
باشگاه الوحده امارات جواب آخرین نامه پرسپولیس رو هم نداد و به نظر میرسه قربانی در الوحده موندنی شده / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/138804" target="_blank">📅 11:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138803">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
الوحده با 3 بازیکن تهاجمی به توافق رسیده و تا زمانی که لیستش و خالی نکنه امکان عقد قرارداد جدید نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/138803" target="_blank">📅 11:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138802">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
🇮🇷
عکس یادگاری یحیی گل‌محمدی و علیرضا منصوریان در حاشیه دیدار دوستانه دهوک و الطلبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/138802" target="_blank">📅 11:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138801">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
خبرنگار اسپورت امارات: قطعی شد محمد قربانی از الوحده جدا خواهد شد و به ایران باز میگردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/138801" target="_blank">📅 11:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138800">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Njkrs2ttvlaCUg1uHZhxKMT3Z-HpOhypIfjOSPm7N7sd3UTHZO76lbvoePNxFNLp14ZSd53vfnDUL6FGSece_BJ8znWcqmdRHgBFzcGvfXz8Fz13d2GhXqMOjDPhcHX_BzZGeKawcqmjwSHaX1EznbrViHRlohVbZL17hzc5xLk5ferXz91A2WmOe9jBwsU81WbLBbiDhoI__lLENHv_HnN02r90PL7ajOaE-9EuemGtaLxbvuaut0tgad1_JqXWD-vt8Q5JgaVe-eahUl8bDx0kDEfIH3ciHeNtF76XGcPAwqAWLjMftrTSh9qVw_xNNaPG2NUnjLm8bvUBHuUR-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ایجنت دنیل گرا:
✔️
«دنیل به قراردادش با پرسپولیس پایبند است و بعد از پشت سر گذاشتن مصدومیت، با تمام توان برمی‌گردد.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/138800" target="_blank">📅 09:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138799">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
🚨
العازی‌ خبرنگار اسپورت‌ امارات:
👀
🇮🇷
محمد قربانی دراین پنجره‌ از تیم‌الوحده‌امارات جدا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/138799" target="_blank">📅 09:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138798">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
🚨
العازی‌ خبرنگار اسپورت‌ امارات:
👀
🇮🇷
محمد قربانی دراین پنجره‌ از تیم‌الوحده‌امارات جدا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/138798" target="_blank">📅 09:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138797">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ed_qTmGTPqrCwT8xRu4fLEHgA9T76s0dFOHCUJSt6J5Z7wLBzwQqkw8H0iqczY9hLleEOaTvs3Sx3lrNkCjxSrymLqlBWgF8d1_MuofUgCWyvOGPzsZQERWtO6LmbCiuLfYkomH0Yy6eet1-pSE3_aSVpjqRBIyjB3Lp1-exU8noqkoaUdvkdBieWgWTyMKEghPLo8xDxsOTv7l0fxtTSkgXNa2ju2WrXu8LRdkW1qLs3of4cnzhNswrwc039g4J3N4tkbI-SaSo4imY0crh2PW6lNqAn8hksQ3IPXegNeQIkrDLXGSgfyp7FcWu8Nk2D5HS70-TOvb08Dye-CaRLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/138797" target="_blank">📅 09:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138796">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDeV-V7xuX4_D0uJ3LXPXaBCL2HW6oSFN1VPF3ieui40QVq1JQYYSXjxZ9KA6iaYXtHVihd4Yxzx8ZZnWWMvQ8P6ggpA5Ie048EruTD6MANlp_s66zhMVzWsQ46_kinbTFTiqR5KIAHmVlFVQAVJLVJv9477f5jC_O_dP_EpOAW03sRDbMZbVbEB3P_RY4Pyk6dZILwf5noSUJEoeYQrNqSMOL-sA7JUx5HrXzpf9TlIeT48GlxPgyasg--iFOMqnGwPHvk0njdmeqQsLwXyuGAkON8sRcngHMcfF-NJQLK6KSVbPMEPqZ4PCvlzW9l1kOhbSZqWc9v4e4vMWOVTxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بونوس ویژه بازی Scarab Temple
🔵
کاربران می‌توانند با هر واریز واجد شرایط، متناسب با مبلغ واریزی خود برای بازی Scarab Temple چرخش رایگان دریافت کنند.
در عکس فوق شرایط دریافت چرخش این بونوس ویژه توضیح داده شده! هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
📌
نسخه جدید سایت:
Sportn5b2.com
📌
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/138796" target="_blank">📅 01:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138795">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⚽
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/138795" target="_blank">📅 01:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138794">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
پرسپولیسی‌های تراکتور:
🗣
علیرضا بیرانوند - شجاع خلیل‌زاده - فرشاد فرجی - دانیال اسماعیلی‌فر - مهدی شیری -صادق محرمی - محمد نادری - مهدی ترابی -شهریار مغانلو
🗣
تراکتوری‌های پرسپولیس:
✔️
مهدی تیکدری - پویا پورعلی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/138794" target="_blank">📅 00:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138793">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
❌
لیست تیم ملی امید برای شرکت در مسابقات آسیایی ناگویا اعلام شد
🗣
🗣
دانیال ایری، پوریا لطیفی فر و پوریا شهرآبادی از پرسپولیس به تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/138793" target="_blank">📅 00:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138792">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⚽
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/SorkhTimes/138792" target="_blank">📅 00:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138791">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
✅
✅
فقط تا چهارشنبه پنجره نقل و انتقالاتی بازه و تکلیف قربانی باید معلوم بشه.بعد از چهارشنبه دیگه فقط میشه بازیکن آزاد گرفت   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/138791" target="_blank">📅 23:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138790">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
انقلاب در الوحده پس از دو شکست!
🔴
مدیران باشگاه الوحده پس از دو شکست پیاپی در شروع لیگ دست به اقدام تاریخی زدن و در یک روز با سه بازیکن خارجی سطح بالا توافق کردن و به زودی از اونها رونمایی میکنن
🔴
با توجه به جذب این سه بازیکن به زودی دو بازیکن خارجی از…</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/138790" target="_blank">📅 22:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138789">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
علی قلی‌زاده: امیدوارم سال آینده در پرسپولیس باشم!
💬
فصل گذشته تمام کارهای انتقال من به پرسپولیس انجام شده بود اما ناگهان ورق برگشت/ باشگاه لخ‌پوزنان امروز یک‌رقم می‌خواست و فردا رقم رضایت‌نامه را افزایش می‌داد/ به هرحال این ماجراها بین باشگاه‌ها طبیعی است/…</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/138789" target="_blank">📅 22:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138788">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
انقلاب در الوحده پس از دو شکست!
🔴
مدیران باشگاه الوحده پس از دو شکست پیاپی در شروع لیگ دست به اقدام تاریخی زدن و در یک روز با سه بازیکن خارجی سطح بالا توافق کردن و به زودی از اونها رونمایی میکنن
🔴
با توجه به جذب این سه بازیکن به زودی دو بازیکن خارجی از…</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/SorkhTimes/138788" target="_blank">📅 22:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138787">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1145503d.mp4?token=XW0sCP7kSvwuC62bItDpfm8N4GhNPraKlOCfuRN6Fa6wvoUkxLyaw3y9ixJRv5BgnkZ9dm1oUWHtlctSJ_iE-NSE_7rPUYrMr5wkLu0lXC5GVby1uiz2fxgu9gnppsOx4hgGqmNBARx-d9WCVg2Ecj88hN7Ma_i_27tz2Ym6WrOosvYcqRwWUHx_f4MXQydSVTdHg0XbLowytcEVWDiCtloqg_JlwI9uq0CH2Q6kiLQgltPE24BcD86Zbe0vJFtjY5c1oPALs29GeK7dtXlhcABaEkw3PbVLgn4t7sBCct9xRMIkmsyU7IYbe_KADTDt3GUcZHZI7YPzp7VMBlKsFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1145503d.mp4?token=XW0sCP7kSvwuC62bItDpfm8N4GhNPraKlOCfuRN6Fa6wvoUkxLyaw3y9ixJRv5BgnkZ9dm1oUWHtlctSJ_iE-NSE_7rPUYrMr5wkLu0lXC5GVby1uiz2fxgu9gnppsOx4hgGqmNBARx-d9WCVg2Ecj88hN7Ma_i_27tz2Ym6WrOosvYcqRwWUHx_f4MXQydSVTdHg0XbLowytcEVWDiCtloqg_JlwI9uq0CH2Q6kiLQgltPE24BcD86Zbe0vJFtjY5c1oPALs29GeK7dtXlhcABaEkw3PbVLgn4t7sBCct9xRMIkmsyU7IYbe_KADTDt3GUcZHZI7YPzp7VMBlKsFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
علی قلی‌زاده: امیدوارم سال آینده در پرسپولیس باشم!
💬
فصل گذشته تمام کارهای انتقال من به پرسپولیس انجام شده بود اما ناگهان ورق برگشت/ باشگاه لخ‌پوزنان امروز یک‌رقم می‌خواست و فردا رقم رضایت‌نامه را افزایش می‌داد/ به هرحال این ماجراها بین باشگاه‌ها طبیعی است/ امیدوارم سال آینده در پرسپولیس حضور داشته باشم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/138787" target="_blank">📅 22:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138786">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
❗️
قلی زاده: فکر نمیکنم تو ایران برای تیمی جز پرسپولیس بازی کنم ؛ چون قلبا پرسپولیسیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/138786" target="_blank">📅 22:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138785">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLJdtuirZ0cYs1v9OXNOJdS74c7TneQj2mt6OiyMjr-2_jywkJHHue9_3bR4zHmCv9B2dmNA5CVjyvwvNtjM08lySBcjyjLuAEuPUhq9TbFADHOVNcSMOLcNRN5Ga1n_bKyz2IUhRWl3sgaVggQlJF1CloS5qW0OwM81bDPFtB8pjbvbCfk-niWc-k_MHpq6WAlDQaP59tqBaS8xTd-b2oXXVZ8tr-jRylAW-VfKXL6UEKcuDhG08-qSdIzMkn-4-5wxm1Qr5JuPpC9zBVjUR8dkF_BEre1QhWbRlZ97gTqE3NvhrW0ch47Prtk0SClxF4DYXo2EubST0M7k5cNepg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بازگشت آقای خاص؛ شروع دوباره کهکشانی‌ها!
🔥
- رئال مادرید در اولین آزمون فصل، مهمان اسپانیول؛ آیا مورینیو با ۳ امتیاز برمی‌گردد؟
[
اسپانیول
⚽️
🆚
⚽️
رئال‌مادرید
]
🎁
بونوس ویژه بازی Scarab Temple در اسپورت‌نود، کاربران می‌توانند با هربار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود اسپین رایگان کازینو دریافت کنند.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🌐
نسخه جدید سایت:
Sportn5b2.com
🌐
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/138785" target="_blank">📅 22:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138784">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">💢
💢
🚨
مدیران باشگاه الوحده امارات پس از شکست در دیدار امروزشان به دنبال جذب دو بازیکن خارجی جدید هستند و از همین روز از نماینده محمد قربانی دعوت کرده اند فردا برای جدایی و فروش این بازیکن به باشگاه برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/138784" target="_blank">📅 21:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138783">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/138783" target="_blank">📅 21:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138782">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✔️
✔️
✔️
رسمی شد؛ مهدی طارمی به الوصل امارات، حریف استقلال‌ و تراکتور در لیگ نخبگان آسیا پیوست.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/138782" target="_blank">📅 21:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138781">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb-8LZYwYqnsPs3Jy7OGqnFmvsGqG3312u6JrQQyq8gQBPsWWDBgS2-TGCVeqg0vb5fEkLbM7LoMEVQlg_IKDp0NpNfj5pK1Zf9kTz8dEt50fZwQ6byXrQ_3zpvY4vu8wmNg8VNOjZcWcnVgxffllIRJz9ytDyMWpHucoGXinb7Q3yRCyJeBq9RHqa2A2P8kOdF7byepImMy3daChCyqNQ0aSSGF2loJWsWR_RFFNr2yGB5avv-JB8vAZJfa-j7TpU2GecsmWhumJfL7rFxmV72fVhB4JwS_ujYeeD-uZpEZAFXkyElNFdfBCelb6Frq7DUY87tN8GYcT6FJr-UAdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/138781" target="_blank">📅 21:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138780">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrgPAIct_N87KxPqQLUKwmDu4ZrULSahKPRWhQhpwQ34-yprKAB2LnP2doDXYmTHpJ_xeu1-fED9-y57AAZ76wFoLv1HZEFmiCwgCnLV2GsCYNg04vdBroOB7Bb2xjtQV7YbQFY_S70fwxNxAoTcdojFQB8VSyCqO0RzLBl-OAS-JXkKb79PZZYdg_AZ_NZbf9jIeS7vuET71_6vJaMda1TAOXKHmiJDTowftAelTWgZjgbb4beP4wkSYWTS8wUFQJg487haAkaN6agdWmK_-SjFO2i_LRgjK7AjPwRIPmCOQ2Jw6zDKJBlOw2T_luwx0vGZ35q01-m99C-OAdk5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🔹
سمیه آوج، الهه افشاردوست، سمیه اسماعیلی و کیمیا عباس‌زاده با امضای قراردادهای خود به تیم بانوان باشگاه پرسپولیس پیوستند.
🗣
✍️
همچنین قرارداد الهام عبدالرحمانی نیز برای دو فصل دیگر تمدید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
‌</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/138780" target="_blank">📅 20:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138779">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
❌
لیست تیم ملی امید برای شرکت در مسابقات آسیایی ناگویا اعلام شد
🗣
🗣
دانیال ایری، پوریا لطیفی فر و پوریا شهرآبادی از پرسپولیس به تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/138779" target="_blank">📅 19:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138778">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
❌
لیست تیم ملی امید برای شرکت در مسابقات آسیایی ناگویا اعلام شد
🗣
🗣
دانیال ایری، پوریا لطیفی فر و پوریا شهرآبادی از پرسپولیس به تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/138778" target="_blank">📅 18:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138777">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dk93kMKNHeAmIjN7yppHy3wk6QC-_k68hdAvzKBnVQLOkpJ1H8q9WMfPgqvFf2nm98PNMVOsSQJLewBYfyvhlu51EYKgAOSpDCMH3njdO5aRJNeXCNofl06yzhP6XZ0t6NhRGtRe9k8uEXEvhedQfgbyhAdcOQQtmFyIB40SVfMfYlTyBVhyFzZx1Jjlc6dLQ_os5dqxkJ1KeoNdlZGsGHNffNvZ_Q2JyMAJ8Rv5eEqw-VaJSafQHS05Ej_V-P5xXvJO-rucah1nJskfRdXqNkjayz-x5nxO-plgr86pizdDGpkHvRNMs2IKRsd7919C2WgBck2W_MsilqMNAoZqTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هواداران ملوان در واکنش به سرباز شدن علیرضا بیرانوند، کمپین نه به بیرانوند را راه انداختند!
👍
👍
👍
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/138777" target="_blank">📅 18:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138776">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔄
🔄
بازی با پرسپولیس آخرین حضور بیرانوند در تراکتور؛ بیرو در راه فجرسپاسی!
✔️
✔️
علیرضا بیرانوند به گفته مسئولان نظام وظیفه باید از اول مهرماه راهی خدمت سربازی شود. این در حالی است که بیرانوند اکنون در تراکتور حضور دارد و نقل‌و‌انتقالات تابستانی فوتبال ایران…</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/138776" target="_blank">📅 18:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138775">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
امیر عرب‌باقری داور دیدار تراکتور و پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/138775" target="_blank">📅 18:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138774">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
✅
✅
فووووووووووووری
🚨
انتقال امیر جعفری به پرسپولیس کنسل شد و گل گهر مخالفت کرد  / ورزش سه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/SorkhTimes/138774" target="_blank">📅 15:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138773">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⚽️
⚽️
⚽️
⚽️
از بین ابرقویی، تیکدری یا عیدی یکی دفاع چپ پرسپولیس مقابل تراکتور خواهد بود/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/138773" target="_blank">📅 15:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138772">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
فوووووووری / فارس :
❌
جدایی رزاق پور از فولاد منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/138772" target="_blank">📅 15:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138771">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
✔️
رسمی شد؛ مهدی طارمی به الوصل امارات، حریف استقلال‌ و تراکتور در لیگ نخبگان آسیا پیوست.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/138771" target="_blank">📅 15:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138770">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
رسانه‌های‌یونانی: باشگاه‌‌الوصل امارات 1.5 میلیون‌دلار بابت رضایت‌نامه مهدی‌طارمی به باشگاه المپیاکوس یونان پرداخت خواهد کرد. با خودِ مهدی طارمی هم 6.5 میلیون‌یورو بسته‌اند برای دوفصل!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/138770" target="_blank">📅 15:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138769">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
علیرضا بیرانوند هیچ راه فراری برای نرفتن به سربازی نداره و قطعا مهر ماه سرباز میشه
😂
/ تسنیم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/138769" target="_blank">📅 15:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138768">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🟧
🟧
اطلاعیه‌سازمان‌نظام‌وظیفه: بازیکنانی که مشمول خدمت سربازی هستند تنها میتونن در دو تیم لیگ‌برتری‌فجرسپاسی و ملوان بازی کنند و امکان گذروندن خدمت سربازی در تیم نظامی وجود نداره. علیرضا بیرانوند هم اگه معافیتش رو به هر شکلی تمدید نکنه تنها تا 4 شهریور فرصت…</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/138768" target="_blank">📅 14:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138767">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsT4k1uZ11N7Xk9zy1D1oGZR-nu86-6PnJDaHBBVzHDp2zLdHj53WGOaYqXa60arHXGhydCam54sJTowVxENPgCxnfDA3MbqoKO-UYexARyiNjUly8C4oxZPAw2Y6x_qkkOrTZ0nWh2SNsxiVN7Gx303z2Prc0kyU0Vnad8hgZyajvUx8f0-V-PXBp1fNw4eiSOIiRYi0smQM-hUpU_p4hrJ8TagBUw6wNCaFKavFUWNulw7SDKXN9RhWssyLGkN5utucbc8-g8qScea410vEYpZ-EkmofjjFqqTik920bwSys8MpipPJPwZIZ0slDhsNxl-HooyRTcDOkDXMSPPrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟧
🟧
اطلاعیه‌سازمان‌نظام‌وظیفه: بازیکنانی که مشمول خدمت سربازی هستند تنها میتونن در دو تیم لیگ‌برتری‌فجرسپاسی و ملوان بازی کنند و امکان گذروندن خدمت سربازی در تیم نظامی وجود نداره. علیرضا بیرانوند هم اگه معافیتش رو به هر شکلی تمدید نکنه تنها تا 4 شهریور فرصت داره راهی ملوان با فجر بشه چون پنجره بسته بشه دیگ نمیشه.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/138767" target="_blank">📅 14:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138766">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
❌
فووووووووری
🚨
محمد عمری به دلیل کشیدگی از ناحیه آرنج دیدار برابر تراکتور را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/138766" target="_blank">📅 13:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138765">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
حضور پرسپولیس در مرکز پزشکی و فیزیوتراپی فدراسیون کشتی
✔️
بازیکنان تیم فوتبال پرسپولیس پس از دیدار برابر استقلال خوزستان، با حضور در مرکز پزشکی ورزشی و فیزیوتراپی کمپ تیم‌های ملی کشتی، به ریکاوری پرداختند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/138765" target="_blank">📅 13:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138764">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔻
🔻
🔻
میثاقی: احتمال داره حسین زاده و بیرانوند به همراه تیم ملی امید راهی بازیای ناگویا شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/138764" target="_blank">📅 13:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138763">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
بخش رسانه‌ای تیم ملی: مسدود شدن سایت و برنامه فوتبال 360 عادل فردوسی پور هیچ ارتباطی به سرمربی تیم ملی ندارد و ایشان نه شکایتی کرده نه هیچ عملی انجام داده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/138763" target="_blank">📅 12:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138762">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
قدوسی: علیرضا بیرانوند گفته نه تنها سربازی نمیرم بلکه نیم فصل با استقلال برای فصل آینده قرارداد میبندم
😀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/138762" target="_blank">📅 12:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138761">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9TZcQ-YJg5pUWpCajR2ljX5qWRHZDMNwBJcdXCPGiJax-TyexUFTJPF4wcWXGOKWE52jH-ZJN0S_vmvkcwu8HMUUAft7B6XBRLT5IxLyKNr0LC_cz1EvUUjoc9lo0hqikL_FgtNwdjoMXUqdWVNBeo4SUINi89z8CKZVUjYwuWcC-v4BAxN_-Uifm3aU25plr4AgyK2rY9CzFFHac9ZS4spu01vPkuvbzfdINF46Vi9rK-uPkOhC2wBG8zOGk06cIg8Fo3jZ-U91UNPf2gW1bGzlWj2OU1_ka4BEb3KT2IR5Pof-K3Sb3ZusrbHAYK8oweZZ57crUxU71Ahx7O1bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نبرد غول‌ها برای اولین جام فصل!
دورتموند در خانه مقابل بایرن؛
- امشب کدام تیم جام را بالای سر می‌برد؟
وقتشه پیش‌بینی‌تو ثبت کنی!
⚽️
فینال سوپرکاپ آلمان
[
دورتموند
⚽️
🆚
⚽️
بایرن‌مونیخ
]
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🌐
نسخه جدید سایت:
Sportn5b2.com
🌐
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/138761" target="_blank">📅 12:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138760">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e244643a2.mp4?token=oO5bNkd6MWu6e5zBRAnAEvpsn2PFzPLdLINioVVPH7qg5ZXZJyU2GRK7cMIiitN_Ac6u0YoWesiGMylZwmSQpWwpz6bjCuRjLUO5DWXwjKxmXfuifHar_pQEADJ0woCJhaAva6mmDOoMfNmECIiOywd_reg8bYulvAfIbDNBXNOoAgOnUJ0y1yiN3MqL3SgbhkzMgzary3W_1bFmNdL8CApdwz0ksLjqKTNYBtIue61tEjRtLCv6U0S4HGVguzoo5s00bB7Ja6ey4EaamCRtnHl91c9z-JWNmEgu2ZozbMewgCZE93f4qfDytmSRNYxxfwuH5w7-xHFJ4HQqDEGxYh5NV0DYKzJUnAJHVGISPBGFOrLNol7rjvYxc1trVqSsnirbjJnNUsGMkEp10FHCD7JMHgqbcoYeuF4Le4HLXI6bZvoBDtirDXZA9LHf46_aismJTGGKKDkkVsHbyi7byqQqZz0aBEr0UBEqdiu3gKhf6KSWz3bRmCm_AnpOMl_xydxtVqgVUJbdj5OKMIJrh8m9D3a0oiOnWiURu0S8cW-Qo58OjH51Rvtrv0fjavL_sgWisNZR-94gYphzqCsPBwqpwW-8OljnqnyMHISoVorxhLIjYlz9Gp7-YR7GcqkHknbZzKVUhz0yVXQPvRoSkqw5K04aLWcEUKz-jJ98rzo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e244643a2.mp4?token=oO5bNkd6MWu6e5zBRAnAEvpsn2PFzPLdLINioVVPH7qg5ZXZJyU2GRK7cMIiitN_Ac6u0YoWesiGMylZwmSQpWwpz6bjCuRjLUO5DWXwjKxmXfuifHar_pQEADJ0woCJhaAva6mmDOoMfNmECIiOywd_reg8bYulvAfIbDNBXNOoAgOnUJ0y1yiN3MqL3SgbhkzMgzary3W_1bFmNdL8CApdwz0ksLjqKTNYBtIue61tEjRtLCv6U0S4HGVguzoo5s00bB7Ja6ey4EaamCRtnHl91c9z-JWNmEgu2ZozbMewgCZE93f4qfDytmSRNYxxfwuH5w7-xHFJ4HQqDEGxYh5NV0DYKzJUnAJHVGISPBGFOrLNol7rjvYxc1trVqSsnirbjJnNUsGMkEp10FHCD7JMHgqbcoYeuF4Le4HLXI6bZvoBDtirDXZA9LHf46_aismJTGGKKDkkVsHbyi7byqQqZz0aBEr0UBEqdiu3gKhf6KSWz3bRmCm_AnpOMl_xydxtVqgVUJbdj5OKMIJrh8m9D3a0oiOnWiURu0S8cW-Qo58OjH51Rvtrv0fjavL_sgWisNZR-94gYphzqCsPBwqpwW-8OljnqnyMHISoVorxhLIjYlz9Gp7-YR7GcqkHknbZzKVUhz0yVXQPvRoSkqw5K04aLWcEUKz-jJ98rzo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
حضور پرسپولیس در مرکز پزشکی و فیزیوتراپی فدراسیون کشتی
✔️
بازیکنان تیم فوتبال پرسپولیس پس از دیدار برابر استقلال خوزستان، با حضور در مرکز پزشکی ورزشی و فیزیوتراپی کمپ تیم‌های ملی کشتی، به ریکاوری پرداختند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/138760" target="_blank">📅 11:39 · 31 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
