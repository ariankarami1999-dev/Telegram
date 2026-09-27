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
<img src="https://cdn4.telesco.pe/file/mpizN3Id1xxYauX668NMja-wCPRhcvWgciZCnr9TQNNCd5HjfNM3bNQah0oZW7FsJRq5PFMM8CAWViYX9ZiwDP-wd8LtJOoPGKpivlJcOabnlnA4ZXI7HzCmEOeiKKEgZn7fcILsJgTVbZK6e17n-SwRT6A8NCIyEPYqo5Lnm_gfWxbIs_lLCxBoWmmTyvbpX7O5bLdXK3cmkOvRMSUd7iGD-4p_z8rlzj236Zis2od4IKR9UP_2TrKkbeb8yZpj1W2eWDenmOm0xq_lQHZ3HfPIOG9rMI4r3Av0m3yVZogt6Uij2vM0G163gpeF8L6cRAYR8JRcL3QDyv4SJR26jQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 05:06:40</div>
<hr>

<div class="tg-post" id="msg-140593">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItZr1W2Ya1RHeuH3eYpIHZGzT5d5ejpwPXU9hKog4uHp9ktGreWKWGXBY3GUFgkFZc2nXlgInz7sYYzGaKtDcsuvIkpABqe_Q1jWqOh1Pk56eufQ4-pkDRwbSAfsoDDNA1K5wdWsKeX5uaW4npZoUDR3aws3Arovt3W0B7tWDTj-W6pW0Mste1E5gJ606FdIrtIoxf9w7IZqkYVwMej75icS4kEh5CR2JIFHgHoVyrWzzhC-le6w2amp5CmIBaWqSzrn_e7p2A3AruGcPS9SoB5274ptDrll7pu4Ie-fUP7MRRMfPNVvR7Z5doIJZrGcciKnpBwzctkOVj9h-0ZgEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
فرداشب لیگ ملت‌های اروپا پرهیجان دنبال خواهد شد؛ بازی‌هایی که روی کاغذ ساده‌ان، اما داخل زمین قطعا داستان فرق می‌کنه
🔥
⚡️
⚽️
فرداشب چند تقابل نزدیک و پرریسک روی میز داریم؛ از برتری‌های نسبتاً مشخص آلمان و اتریش تا نبرد کاملاً متعادل نروژ و پرتغال. در بازی‌های ساعت ۱۹:۳۰، هلند و دانمارک دست بالاتری دارند، اما صربستان و ولز می‌توانند معادلات را تغییر دهند. در ادامه، آلمان مقابل یونان و اتریش مقابل کوزوو از نظر اعداد شرایط بهتری دارند، در حالی‌که ایرلند با اسرائیل و نروژ با پرتغال نزدیک‌ترین دوئل‌های شب هستند. یک شب شلوغ با چند بازی که اختلاف روی کاغذ، لزوماً تضمین‌کننده نتیجه در زمین نیست.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 490 · <a href="https://t.me/SorkhTimes/140593" target="_blank">📅 02:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140592">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
✅
✅
فشار شدید امریکا علیه ایران
✔️
✔️
امارات، ترکمنستان و تاجیکستان ۳ کشور جدیدی هستند که حریم هوایی خودشون رو به روی هواپیماهای ایرانی تحریم کردند !
❌
مکزیک برزیل و بقیه کشور ها هم رسما تحریم کردند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SorkhTimes/140592" target="_blank">📅 00:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140591">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⭕️
⭕️
قرار شده جام قهرمانی در ازای بدهی ۷۰۰ هزار دلاری فدراسیون به هلدینگ، به استقلال تحویل داده بشه!
✔️
✔️
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SorkhTimes/140591" target="_blank">📅 00:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140590">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SorkhTimes/140590" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140589">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/140589" target="_blank">📅 23:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140588">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
✔️
تاجرنیا: از سازمان لیگ تقاضا دارم قهرمان فصل قبل لیگ برتر را اعلام کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/140588" target="_blank">📅 23:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140587">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
🔴
فارس:
⬇
بودجه پرسپولیس در فصل جاری ۳ هزار میلیارده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/140587" target="_blank">📅 22:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140586">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
✔️
بازگشت اورونوف به تمرینات پرسپولیس
✔️
با اعلام باشگاه پرسپولیس، اوستون اورونوف به تمرینات این تیم بازگشت. این وینگر ازبکستانی در فیفادی به اردوی تیم ملی کشورش دعوت نشد و کاناوارو ترجیح داد روی نام او قلم قرمز بکشد.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/140586" target="_blank">📅 22:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140585">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
#فوری | ترامپ در سازمان ملل:
🔻
با تصمیمی بزرگ در مورد ایران روبه‌رو هستم؛ توافق یا نابودی کامل
‼️
🔻
آیا به توافقی دست یابیم که به این کشور اجازه دهد به ملتی بسیار بزرگ‌تر تبدیل شود، یا اینکه آن را به‌طور کامل نابود کنم
⁉️
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/140585" target="_blank">📅 21:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140584">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
‼️
🔴
ادعای جنجالی کریمی: خودسرانه برای بیرانوند دفترچه پست کردند؛ در تلاش‌ برای معافیت پزشکی او هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/140584" target="_blank">📅 21:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140583">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFryFVHPF5A2OmawIRoVpmy6LINTBnGC6K7tGfl7DaIziphi3z_epIp-901q6cZ8Bv9Sg1_i3VpXrheW7IQVx3yuYZ0vCvrrup9oqbZUYTeLBy5sgx44joQOpYRaFJ10YlnfhJa98mx8q1crPUXYFlfI2UVFd3U1Vg6Tt8lOFR1_E-4wGInxNLcIOcbgKSic9Z52wYZgciB9_9UnnycXcDBmS6GITfzWV1ghHTzV__YfEI89fspugDlwECJSlkK0YBRzXhLg2qCtBiCld9DhKOOjo9YdVICjEUTEc5P9bLA34M6pxGOtFCQ-Xs0rkXob5ldO4n0Ay64S6N1T4_DgnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
❌
افشاگری فنونی‌زاده از قلعه‌نوعی‌‌:
‼️
من با سند‌ و مدرک به شما می‌گویم ۱۷ تا مربی در عرصه‌های مختلف ملی و باشگاهی که سابقه استقلالی دارند، توسط قلعه‌نویی به‌صورت مستقیم یا غیرمستقیم روی نیمکت تیم‌های مختلف ملی و باشگاهی نشسته‌اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/140583" target="_blank">📅 21:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140582">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
❌
با دعوت احسان حاج‌صفی به اردوی تیم ملی این بازیکن در صورتی که مقابل ازبکستان و روسیه حتی یک دقیقه بازی کنه رکورددار بازی با پیراهن ایران خواهد بود و از علی دایی و جواد نکونام عبور خواهد کرد
✔️
جواد نکونام ـ 149 بازی ملی
✔️
علی دایی - 148 بازی ملی
✔️
احسان…</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/140582" target="_blank">📅 21:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140581">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/140581" target="_blank">📅 21:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140580">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/II4iaU7qK0xCcYp5L8H7kwLMdKKs7OtVqMF0XebVjFSBgIuS16xHqyr9APHS9qSktwBS2JPI3C1-iHiau6_t9ghCk44U6E4EL0UaJRrevtut_aCmlyDakwoHUQoV0Mjoz74RVC9RZQVkH8Icyh9sMcqdKPDbP-qzIOPZuLsV1kPtYIjU26PflznNRHATudnHyLGYABJEUbWUbl-r3G0rOQO5E2atdIOQ7eRupEFC48aQ6tae5bdlLje37slB04eKlzi_oac1Bc-G-WNvBSUDxpAiwpWob_vL_g5kFPVHWoe3HesXrZmNNLYM8ZQJNbfjUYa7CCWJuiHFiEwEd-G_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
England -
🇪🇸
Spain
⏰
Tonight 22:15
🏟
Wembley
🇪🇺
اسپانیا با ثبات بیشتر در کنترل بازی و خط میانی منسجم‌تر وارد ومبلی می‌شود؛ در مقابل، انگلیس روی سرعت انتقال و کیفیت ساکا، بلینگام و کین حساب می‌کند. غیبت رایس، پالمر و چند مهره دیگر می‌تواند تعادل انگلیس را تحت‌تأثیر قرار دهد، در حالی که اسپانیا با هسته اصلی قهرمان جهان و اروپا حفظ شده است. از نظر فرم، اسپانیا در ۵ بازی اخیر ۵ برد داشته و انگلیس ۴ برد و یک شکست ثبت کرده؛ بنابراین انتظار یک بازی نزدیک با موقعیت‌های دو طرف منطقی است.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/140580" target="_blank">📅 20:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140579">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/140579" target="_blank">📅 19:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140578">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
🎤
بخش اول صحبت های حامد کاویانپور مدیرفنی آکادمی پرسپولیس بعد از دیدار با امید سایپا
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140578" target="_blank">📅 19:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140577">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⭕️
قسمت جالب سربازی بیرانوند اینه که همین آقا دو ماه پیش علیه علی دایی استوری گذاشته بود: «من هیچ‌وقت از رانت استفاده نکردم»
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140577" target="_blank">📅 19:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140576">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140576" target="_blank">📅 17:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140575">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
سازمان لیگ مجددا کارت بازی علیرضا بیرانوند رو به مدت یک ماه تا پایان مهر ماه برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان میتونه که در بازی هفته هشتم با استقلال تیمش رو همراهی کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140575" target="_blank">📅 17:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140574">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140574" target="_blank">📅 17:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140573">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
اوستون اورونوف و مارکو باکیچ هم اکنون در ترکیه حضور دارند و اگه مشکل پروازشون حل شه تا شب به تهران میرسند    «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140573" target="_blank">📅 17:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140572">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vr_4U-1NAVTagh3XkoeppDbU72-N9KunROcnUeSIwjx6H9YENSHKCsfQZHJIRXBZUkpC43v7ZxYa0VvlWhdDYJVBi_5cBmlvBvIvQBygXucYQIDwCHgBxrTlw9U2Dt8ARmMnAF2dyOu-nOJ9ETiQ-1Bgg45RbGuF4zp56-S8wIQ7MwFor5HZs3x2_M1JK-4r-rDQ_XDNLsma01valLP8zuhqxEn2UNGILV2S7RYHqLqnk4SIA3MM8U9-4fdkwPKzXVEJPpu_XSs6hEm-UihImEjOH3uLukZLYqpYqFaNy6J80V5PjvXPPiw1bOr4RYbDTjT2UC6YVkIs6h3mFIfrVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140572" target="_blank">📅 16:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140571">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🔴
فوری؛ معافیت علیرضا بیرانوند از اعزام به خدمت سربازی، ۱ ماه دیگر تمدید شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140571" target="_blank">📅 16:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140570">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2Hkki-gfZrLjI_FIozaK4MXL7Aj-_6fxeQDPp2LekQLZ5gbBlRvlD_buz_KuYgaPpM9oPS-wVRax_A_wInMLxJ0pTdKFmUqKaAEVmyu5X69t9Wz3x46P0k0au1SAhyBZwpL-cpu7MsR7jQo8mw1xjk7OLK02IJ9QAOl5K0BOijKe_zs7c3mTOBIm2ft7rikdxUgWVfHAfKJtlH3hoYNQP94ghiocUr9tfjdPrsTe3okWZWE3HMRwNcxIT4-HaxdcbgP0dsLXHisxAdTFqZWJCcZO72S47O1zSjJig0qGKohsV32qd9n9VgFO49hckMvnOcIQnKUrXEEWnD_JEs94w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از بدنسازی امروز پرسپولیس؛ شاگردان تارتار فردا استراحت خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140570" target="_blank">📅 16:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140569">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=XNchXJUmb_J-sudIRM2l-y_ScWg7IKoQ1qawOtkU1hfeP6tApGXmhf_6Bp0gadIQ51KaVV8ZMjlu1-UNVfJ9_-bnQElbIACAILxBCeC7HLu5hiezEXUDX8-LCA7M41c865HVjR59BucrULWUBaPOSrFHUv8sKR4-GRH-rm9Epe0wnDe5TamDR6nDDCHL4zX0ljSAA4VtMtHTZbToejLvRg2lKC_ZVqvVIWavPq9HJQyJzJjdoPWeBIPrj1GC-1WrYmrNik_E5K-eUd8crmBxoa9wZ7odDf8MHuUGWOXpBSMs9Cby6bEyZLc8zLXkwRsH3grSITTbyAVxy96B7gk51VrBs8bttPXuj_MuWXjjL1o2b7PwTOEElJ8orP1z9cjrszJnWS7kqLsRYXayjzvTsv47CQ5BEfPHw9UE6in0NT_Si8djA4bIC6PMowz1L08AeGhq93SsteeHIX8ugHEhM6Uht2LO1BL7irBHi8_zZq4fSxoyR7x0wrUDPFTcET85MSdTsXcPfRyq3ipBvjAyQweGOaPKShnIKXOih-fdn2xupIWkIsfx3UJrYlncFJmrowfJg6Ax2R50elH7D0LptSpDY8VxYoYRGIu4gKeP06SiWl5qXvLeiZ2ovVFHFqh-WXMoRdSbt2ln_OQBBQBeF5sH9tC9zA6U5sagFGf5emM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=XNchXJUmb_J-sudIRM2l-y_ScWg7IKoQ1qawOtkU1hfeP6tApGXmhf_6Bp0gadIQ51KaVV8ZMjlu1-UNVfJ9_-bnQElbIACAILxBCeC7HLu5hiezEXUDX8-LCA7M41c865HVjR59BucrULWUBaPOSrFHUv8sKR4-GRH-rm9Epe0wnDe5TamDR6nDDCHL4zX0ljSAA4VtMtHTZbToejLvRg2lKC_ZVqvVIWavPq9HJQyJzJjdoPWeBIPrj1GC-1WrYmrNik_E5K-eUd8crmBxoa9wZ7odDf8MHuUGWOXpBSMs9Cby6bEyZLc8zLXkwRsH3grSITTbyAVxy96B7gk51VrBs8bttPXuj_MuWXjjL1o2b7PwTOEElJ8orP1z9cjrszJnWS7kqLsRYXayjzvTsv47CQ5BEfPHw9UE6in0NT_Si8djA4bIC6PMowz1L08AeGhq93SsteeHIX8ugHEhM6Uht2LO1BL7irBHi8_zZq4fSxoyR7x0wrUDPFTcET85MSdTsXcPfRyq3ipBvjAyQweGOaPKShnIKXOih-fdn2xupIWkIsfx3UJrYlncFJmrowfJg6Ax2R50elH7D0LptSpDY8VxYoYRGIu4gKeP06SiWl5qXvLeiZ2ovVFHFqh-WXMoRdSbt2ln_OQBBQBeF5sH9tC9zA6U5sagFGf5emM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
ادعای جنجالی کریمی: خودسرانه برای بیرانوند دفترچه پست کردند؛ در تلاش‌ برای معافیت پزشکی او هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/140569" target="_blank">📅 16:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140568">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🔴
فوری؛
معافیت علیرضا بیرانوند از اعزام به خدمت سربازی، ۱ ماه دیگر تمدید شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140568" target="_blank">📅 15:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140567">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faac5ebeb7.mp4?token=nahicHSv8PO4m-D7GMZ0jOCe1otLKamaeQpXnpqFWoaG35OnepGs0JVYq7CRUHu-4fmMWuNgRf-Su5yrCmgh75AgfIv96uIeAyZkVSZ_UVBJ3I1iOJGRx61KZyo53-atGIskD8iurZbr9XAm7U4WobTwXnGt-qzHWmUcH-vrgV7b6uf6vyU8l8kmNTo6BENecco5dpvz6VT1UKHMEVnhMO7sKSu4s5xQaq2dosyVLQqfLcF8e_nTK2gDgwQEVhF3HeVqexIUR-kMpDax4367GyBe5myi6yK0p_GHJ-YPYFfe7wBj4O9eGNagiPUwoG5qoAaOJE7lGwMF2YpSzkeauA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faac5ebeb7.mp4?token=nahicHSv8PO4m-D7GMZ0jOCe1otLKamaeQpXnpqFWoaG35OnepGs0JVYq7CRUHu-4fmMWuNgRf-Su5yrCmgh75AgfIv96uIeAyZkVSZ_UVBJ3I1iOJGRx61KZyo53-atGIskD8iurZbr9XAm7U4WobTwXnGt-qzHWmUcH-vrgV7b6uf6vyU8l8kmNTo6BENecco5dpvz6VT1UKHMEVnhMO7sKSu4s5xQaq2dosyVLQqfLcF8e_nTK2gDgwQEVhF3HeVqexIUR-kMpDax4367GyBe5myi6yK0p_GHJ-YPYFfe7wBj4O9eGNagiPUwoG5qoAaOJE7lGwMF2YpSzkeauA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حضور پیمان حدادی مدیرعامل پرسپولیس در ورزشگاه درفشی‌فر برای تماشای دیدار امیدهای پرسپولیس و سایپا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140567" target="_blank">📅 15:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140560">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boTm_NrIrZhts-okiQyEGvgNVHkIFZzYNKtaupVB_sogZFn5vcjaX61DR4htRpjbkkYCAyN2n5zTrWid3qLh7aSGHWgA8pV_DBGz3vIrYbgidCNxAdA-tPlEdcb_lJS-fo7M-oa03zmWKM_z1Z5Kw43rclYQjiOYuQzKzd7cfSsMnOWWxaFlHzp0_HoMao0lbbMRyzoyhJxYgMYbB4OBKjBwiuNhOVm0cmWfYCUruM3kOUTlLpJdGHqhhLosTxxh4py7NvnxZE6h-suNdMoc1fw0rFtQoOVTJj1urnd8rDa1Z6NEcsTvfmL2eZ9luunxtJjWbgzM1VxInHwe3eZuJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد بزرگ در اوج هیجان؛ اسپانیا و انگلیس برای یک شب تماشایی
⚡️
[
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🆚
🇪🇸
اسپانیا
]
⚽️
اسپانیا با میانگین مالکیت ۶۴٪ و حدود ۱۹ شوت در هر بازی، از نظر کنترل و خلق موقعیت دست بالاتر را دارد؛ انگلیس هم میانگین ۱۳.۵ شوت و ۲.۵۶ گل زده در هر بازی ثبت کرده است. با توجه به فرم هجومی دو تیم، انتظار بازی با موقعیت‌های متعدد می‌رود؛ در عین حال هر دو خط دفاعی در هفته‌های اخیر آمار گل‌خورده پایینی داشته‌اند. تقابل در ومبلی و شروع لیگ ملت‌ها، این مسابقه را به نبردی نزدیک و تاکتیکی تبدیل می‌کند؛ جایی که جزئیات می‌تواند تعیین‌کننده باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140560" target="_blank">📅 14:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140559">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEBu0rjJLzOzu3QhltTvMfxwAA4cY4LuEexJXYGGGIpdjlvHUPt_CSYJQQtcfqglv556sq9Hwk_-8q1dLaJPpp8tlOBnMa9ZHsHW7nfIkNyL0FPTfsZ1faV8lWZnnAiy4D12Zq_BdHkRScxhmv1vX9qBvrr7HTSpQ7Phbmm988ME4UyTpkb03v1VR8CFHaDc23XLdghkBBGNqWwY6XODdGH4UqJJxN30sPHl37hPAIX301pZdrBixHeCyBMPsuAjPoEsD3rSq35pBJKlva7kEeSCeyKM4WAsSlY7ftTqy9_SjwuaSHnL_FXJzz3MqPUo0i-yfCbdXxtNAL2pDf26Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیم قلعه‌نویی واقعا عجیبه!
❌
بازیکنی که از جام جهانی خط میزنه رو کاپیتان میکنه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140559" target="_blank">📅 14:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140558">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⚡️
⚡️
تاج اعلام کرد امسال دیگه سقف بودجه وجود نداره، اما فیرپلی مالی اجرا می‌شه.
⚖️
طبق این قانون، باشگاه‌ها باید قرارداد بازیکنا و هزینه‌هاشون رو منتشر کنن و اگه این کار رو نکنن، سازمان لیگ خودش منتشرشون می‌کنه. همچنین باشگاه‌های زیان‌ده فصل بعد با محدودیت…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140558" target="_blank">📅 13:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140557">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
فوتبالی:
✔️
✔️
گفته می‌شود فدراسیون برای جانشینی عبدی با گزینه‌هایی مثل فرهاد مجیدی و مجتبی حسینی وارد مذاکره شده و باید دید در نهایت چه کسی هدایت تیم امید را برعهده می‌گیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140557" target="_blank">📅 13:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140556">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
در صورت تشکیل تیم (ب) پرسپولیس، گزینه‌های سرمربیگری:
⏺
محمد نصرتی
⏺
اسماعیل حلالی
⏺
محسن بنگر
⏺
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140556" target="_blank">📅 13:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140555">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
علیپور و کنعانی‌زادگان ابتدای هفته آینده تست پزشکی می‌دهند
✔️
نتایج این تست‌ها وضعیت بازگشت دو بازیکن به تمرینات را مشخص می‌کند‌ و پرسپولیس امیدوار است هر دو به دیدار ۱۷ مهر مقابل صنعت نفت آبادان برسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140555" target="_blank">📅 10:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140554">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">#فوری
🚨
✅
⭕️
⭕️
⭕️
با تصویب شهرداری نوشهر؛ امتیاز لیگ دویی این تیم به پرسپولیس تهران واگذار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140554" target="_blank">📅 10:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140553">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ogs5jiDEi5j64Twf2pSJMQqzSpEXRnsZHr0wheJJ5SYGV8fAjMcYBu0-eEKzE8C_Ps01a3qYIXbft9zeLtaaIEGKPGfzyZNq2O7150hI_i2NzLHAFNBe_kNrcxl7cf41OfWhctGpE66E1b0QLPtYFaOwUM9807nU85dT0sw_v9vWVnUG_jTu5V5nuJHleZSTiv1Ma7RjNXSWfoV0MCyI4t55ro_k5sH36xlqMCEk0DBIYmfpgqmVIdqim9tQw6PF62HCr76qE8JTrBH6IbKvMOPgOVIRPhCWqYGAC9z6-UFzv-4SyPcTiYkR-m8rsrqMHckA27qBH-TJadHQd0YJHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
⚡️
باشگاه استقلال در پرونده فابیو کاریله که فقط اومد یه سلام کرد و رفت به پرداخت ۴۰۰ هزار دلار محکوم شده است.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140553" target="_blank">📅 10:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140552">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
❌
سه وکیل خارجی باشگاه بعد از دیدن مدارک جدید در پرونده آسانی اعلام کردن، درصد پیروزی پرسپولیس تو پرونده زیاده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140552" target="_blank">📅 09:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140551">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQKvWrwWgEMNU9C8aqN80_lAm1BY7FzNKNM9wsmQmvprjK9k3f1xOcy2F2Unyg7JnYpQcAaNlX8jCxFMFG3x2bXCQPlbBvQwxFlJkZ06wqMy7vzocWUD09ZlPu8kw323CqTEONYXH2DUFAbDtL8m_b3QI3qIqmdVrIlj2hhGc0ZV0xZ6VsUbZgz9Q7q9SdwJu4UQKh04oIaZJYEB9Uc45oq34NyuceZUWf2TbONYiLHDt7CAtPyW2GEt0SsFfTpgLtc-DzYlLboV-wvcpt6eE938BP3BSh2qk5oC2dNYSEiXGI3cBWHZBsdn1YnbjHBTBATmHdZOSBBTDncnnkCv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140551" target="_blank">📅 09:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140550">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZB4vVdgV7Ry4poZdEJbgA7smn_SJEn4r-aItODUMVrH4QjzqbthOcw4Vuu2GqT0ScmLiZpAoxIH8D4TmAqYXz1bqYcJmiO7n0mAjKVmB3gSyVBmcWCkCyrLaEWqJ5E8oQwWK6moKxz1kzGPxaC1JeX8_Jzq1vEwy7-dC8TjPUR-nB1lZo2lhYhRgLx1DJNMY5qeC929lGIq1b_57KrnkwgPkSEPiJ7YnaeOxFM04yVgNcfHa5J3oO_J8w8iQx-19I4jMreGHG-Ud58_PE_8oskuZ-J6ZZASjpxeG26dcUbEy8QXd-c6s0Pt3UsedhJiIup41win-ZF2cxmNFqgD3cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
شبِ حساس لیگ ملت‌های اروپا
🔥
⚽️
فرداشب چند تقابل جذاب در برنامه است؛ از جدال نزدیک اسلوونی و اسکاتلند تا رویارویی مدعیانه چک و کرواسی. آلبانی با توجه به ضرایب، شرایط بهتری مقابل بلاروس دارد و سوئیس هم برابر مقدونیه شمالی دست بالا را دارد. اما حساس‌ترین بازی شب، انگلیس و اسپانیاست؛ دیداری که می‌تواند از نظر فنی و نتیجه، متفاوت‌ترین مسابقه این کنداکتور باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فرداشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140550" target="_blank">📅 01:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140549">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIGOH2THHkJykD71PuLz_mwCXYzgvjIHS0M-MOmeqJLQveF2dxD5AEPadC23TAdwj4a-eM5CyoWApQpHZuYvBp0aFU0Y7esLRo1MyfaqIGVsSaQBElPJEjdAuKrT08N1-8JTlfFF4AI66LSGr0kzRxfbAhVEVlCDWthWwUNXVEJ4e6JNCtRVQdu4grUhR-CnToIJAZF3FsAKf3vLdvNKe-LHozDlNrTSngoNCEHbWVnDyt75uc0oy613-FBZ-dQ4KRNIZX5Cg4rIZLWuVxzpu3ArbxwVXWrsqRv0teZVJ1Pwb1mqXhkevhcr3pTm3mkyUSPqPRTTZKql5BaWGADvlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
اعتماد ویژه تارتار به جوانان آکادمی
🔻
مهدی تارتار در دیدار تدارکاتی امروز مقابل چادرملو نشان داد که برای بازیکنان جوان و محصولات آکادمی پرسپولیس اهمیت ویژه‌ای قائل است
🔴
در این مسابقه، ۷ بازیکن جوان آکادمی فرصت حضور در ترکیب را پیدا کردند تا خود را در سطح تیم بزرگسالان محک بزنند
🔴
این فرصت می‌تواند سکوی پرتابی برای جوانان پرسپولیس باشد؛ حالا نوبت آنهاست که با ارائه بهترین عملکرد، اعتماد کادرفنی را پاسخ دهند و مسیر خود را برای حضور بیشتر در تیم اصلی هموار کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140549" target="_blank">📅 00:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140548">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvAHI6Bo9UxYWIBo-5Rd7hxNKUotZhCz8791Fspndoifjy-6F4r3MgJx-wFe6tqtzHjeRvJjAcuumX0XE-Qhv2XCXInp7R8DzWJNkMTSRzbfNDT9ab_QYp3xMtPFTk-Jpvkn06QRhy6FlicHSf6n2vLx8i6YPTr1kN69qhQEwCtyKgtEWpg-QcUCkjO2umz2MgUxiiyvPr373zQIWUN-rtY_bC1YBMG3uHPigR_ILcjSG4sy-2JYEIoR-nsQHPZTswiL9OYb7dEU5g8SueABHttaqTC5pm9Y1DpMjceq0PBR8kUswG7rdS2I3RrUprj6fPrWp9DlgWGdpLrzH20bYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نتایج هفته دوم لیگ برتر بانوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140548" target="_blank">📅 00:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140547">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔻
پرسپولیس قید جذب اندونگ رو زد
🔻
باشگاه پرسپولیس به خاطر ریسک بالای این انتقال و دور بودن اندونگ از شرایط بازی، تصمیم گرفت بی‌خیال جذب این هافبک گابنی بشه
🔻
طبق شنیده‌ها، تا این لحظه تراکتور تنها تیمیه که همچنان دنبال جذب اندونگه و نکونام هم روی این انتقال…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140547" target="_blank">📅 00:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140546">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPPU6FPysc7OhzyAPmnuyPdCXwqYta3gOjTZ-A3UcEQ4u9QPdxM26mX69Tx3urzZ8jnBRS5aPisElUzsHUID0o6L-ftyoAFEIQjb0KoSrc12YAtFdRsW6BBxa_7h4VzMTSp9CHlBmfDBxAp6U7Fqsh4GYLdLZPvTCR_PgUYWnaRwQ8ggpmh2RoUACL3Bfl7Fo0yqoHvcGXu8NulQvdwyZWDzerrRF65HQFp4MdqeayKHAjIc2B002TchObPBRNSk3YmGnXNVbIzggHFDiQllhp5xfJaV3DPANvl9TQByzmZJZxsYTX6LGy8LfHx_6Won0WMSegtbhhR-l0BO6MqSgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یه سری شایعات از بازگشت اسکوچیچ به تیم ملی در حال انتشاره که نه تایید می‌کنیم و نه رد می‌کنیم.
/فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140546" target="_blank">📅 23:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140545">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⭕️
نتایج ۲۰ بازی اخیر ایران با قلعه نویی ؛ ۸ برد - ۷ مساوی - ۵ باخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140545" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140544">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
برخی اعضای هیات رییسه فدراسیون فوتبال هم از امیر قلعه‌نویی راضی نیستند و خواهان اخراج او هستند اما مهدی تاج تمام قد حامی او است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140544" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140543">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⭕️
👀
صدای پای اسکوچیچ به گوش می‌رسد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140543" target="_blank">📅 23:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140542">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
چیت ساز، معاون وزارت ارتباطات :
🗣
حتی تو شرایط جنگی هم اینترنت قراره برقرار بمونه و همین که الان اینترنت وصله، نشون میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه؛
✔️
✔️
اینترنت پایدار و باکیفیت جزو حقوق اولیه مردمه و خدمات ارتباطی…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140542" target="_blank">📅 23:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140541">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⭕️
گاریدو یکی از گزینه‌های تیم‌ملی برای  جانشینی امیر قلعه‌نوعی هستش
😐
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140541" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140540">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
غایبان پرسپولیس در دیدار دوستانه امروز
⏺
حسین کنعانی، علیپور، عمری، ابوالفضل جلالی و حسین ابرقویی، باکیچ، ارونوف، نیازمند، زارع، محبی، محمودی، ایری، لطیفی فر و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140540" target="_blank">📅 23:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140539">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ur6GaaNvWEmcJocpAzG-bB1rguc4I4S-EWrOeqQQFwtbjctBgcTQYq7IlDHmUFjihArfpx4KxUtzoojziyl52MIbQbS4ARPLiEKJRUzXo6-pr2u9KGg1w2vz-RIo5a6W926n58vIGqXnUB3Nl-zrv1ScYEgMAzJ-TaZMgjzfdYHCZsG7lGiBZaw2yJJQkOPbeKoRn-yLwE2dNqgWgfMycakJsLDIKAY1iIRcF4qpZjBf1uqgtwHCNOqh1Hgy5ZepUagQmSGTI6JeZ6WkMfi5NY-btvVrrVGf2HQPcVKH8twYhHq1dS7I1WI9uDFeqHkbGP5GcqMlGXSA561KIGnbdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تولد مهدی تارتار
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140539" target="_blank">📅 21:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140538">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
مهدی تارتار با بازگشت میلادمحمدی مخالفت کرد/تارتار همچنان رزاق پور را میخواهد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/140538" target="_blank">📅 21:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140537">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140537" target="_blank">📅 20:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140536">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
غایبان پرسپولیس در دیدار دوستانه امروز
⏺
حسین کنعانی، علیپور، عمری، ابوالفضل جلالی و حسین ابرقویی، باکیچ، ارونوف، نیازمند، زارع، محبی، محمودی، ایری، لطیفی فر و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140536" target="_blank">📅 20:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140535">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWoHq7TE1blTl4gMFezDqEy0aX-2ig303ajEXix3RZ-nYp82lotjxOOOkT4EwDsOYae7vFRh4u17vyl2fgLfYIy-_HG5NgwE6-Tyuj0ocurkPejPYgn4Zvyd-z86kmptUJY1NiJW3GkdNH9rVJGzhE_Lbhr6Tqh62WhvJoT34U15bkdaIrXzsobpfYGOnHKq7WDKQkisNjn8dG8kskxOesjxdWv-K9M7TwOnp3SKqa0UL9FA4d9SkH8fEiUFdtHrGDoU5Mua9jZl1Z5GcDJo4bKlqbELR1qzluzfL4EEBaY2qHYfbUUgW6NPEBX-PQ62asGCbxKy-lMSNKV55x0M4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
ترکیه - فرانسه؛ جدال پرتنش در قلب استانبول!
[
ترکیه
🇹🇷
🆚
🇫🇷
فرانسه
]
⚽️
ترکیه در خانه با تکیه بر فشار و انتقال سریع می‌تواند فرانسه را تحت فشار بگذارد، اما غیبت چالهان‌اوغلو و ییلدیز روی تعادل تهاجمی میزبان اثر دارد. فرانسه با حضور امباپه، دمبله و اولیسه از نظر کیفیت فردی دست بالاتری دارد، هرچند اولین بازی زیدان و تغییرات ترکیب دفاعی می‌تواند هماهنگی را تحت تأثیر قرار دهد. باتوجه به فرم دو تیم، بازی می‌تواند نزدیک و پرموقعیت باشد.
سناریوی محتمل: گلزنی هر دو تیم و برتری نزدیک فرانسه.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140535" target="_blank">📅 20:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140534">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84e7380b8.mp4?token=E73hq9J3VqabA32p1mNTyzOPYAzqJ8pOX-aRipQjrC8anM6y5H5GozRTS6qXQxvyQFJTwyMMI7eA-lV5rzVK_ZhvAXXCoZ7PRxywqy_Zv9_UkTmZqscyZJPuG3lxaTy9fJFjtc8zJ_Bf1u8arj7NDT7V9DCqyei8q5thSOQp3buvSNPzp9bhqnVt9eo5SZEKKkyInDfbsp3MigyUY_twrtFvSwUlia8CFI-RWESeloYZKrt7X7Nb4435BM5vtq43tKvmSwfhLVVMzo0tKm86lp06M3xVGPyMSdUtk78PpynLz5yidshmxwGW1RzDGIA0bIkIFvwPaNB2h-r5K4ysbjt7sJTDRkITovhaq0FnObA33iRdW1X_DVXJjvsUQp6NuEutnSPLqaBRCG1xlftzwmQGXaVw2T26GDLNfH7tkLl8-AoRRXrQ-DTW9pW7m_3J83q3ltAGxPE2kqvRNAL0Wc3ZQytz52CStuENxrD3FFVIUkMP77NeQDZ91_F3X-uLup91BklP5P3OD2vwXeakdf_UoETJ9fA2z-DRZ5VGWkwhUaCo50MNFlNiuwVnTYWav71uLwT6Ctx1XRK9HRFy4r1HuRgtCHeDn2tVC12bwK66GewHuRoVtMvHi5oV88CVaY2XLllOWWlFLBCM2Tr-KzE-2y7A2MZLpzMnQsPw778" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84e7380b8.mp4?token=E73hq9J3VqabA32p1mNTyzOPYAzqJ8pOX-aRipQjrC8anM6y5H5GozRTS6qXQxvyQFJTwyMMI7eA-lV5rzVK_ZhvAXXCoZ7PRxywqy_Zv9_UkTmZqscyZJPuG3lxaTy9fJFjtc8zJ_Bf1u8arj7NDT7V9DCqyei8q5thSOQp3buvSNPzp9bhqnVt9eo5SZEKKkyInDfbsp3MigyUY_twrtFvSwUlia8CFI-RWESeloYZKrt7X7Nb4435BM5vtq43tKvmSwfhLVVMzo0tKm86lp06M3xVGPyMSdUtk78PpynLz5yidshmxwGW1RzDGIA0bIkIFvwPaNB2h-r5K4ysbjt7sJTDRkITovhaq0FnObA33iRdW1X_DVXJjvsUQp6NuEutnSPLqaBRCG1xlftzwmQGXaVw2T26GDLNfH7tkLl8-AoRRXrQ-DTW9pW7m_3J83q3ltAGxPE2kqvRNAL0Wc3ZQytz52CStuENxrD3FFVIUkMP77NeQDZ91_F3X-uLup91BklP5P3OD2vwXeakdf_UoETJ9fA2z-DRZ5VGWkwhUaCo50MNFlNiuwVnTYWav71uLwT6Ctx1XRK9HRFy4r1HuRgtCHeDn2tVC12bwK66GewHuRoVtMvHi5oV88CVaY2XLllOWWlFLBCM2Tr-KzE-2y7A2MZLpzMnQsPw778" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
صحبت‌های کنایه‌آمیز توتونچی، مجری برنامه شب‌های فوتبالی به تیم‌ ملی فوتبال: دمتان گرم! در کمتر از 48 ساعت 7 گل از کره شمالی و ازبکستان خوردیم..!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140534" target="_blank">📅 19:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140533">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
❌
❌
❌
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140533" target="_blank">📅 19:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140532">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
❌
❌
❌
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140532" target="_blank">📅 19:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140531">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18169032d.mp4?token=hZuL3y9Y0KFjKdJ0urErSICnIzK_AR9coBR6nVdEWkhntAeUQGck2JWyBUVRnak2g7xRcDPUALjauFBlYyE2T42gVDlTpnWQ_0urOd_PRYc0B6-hTxRQ5lraggX4XFEAV_zQpoPuZXceMM_rUpbus84zDT-rL9wyfIq-ua1nPfXgEOJ6HNuZH4bgN15HwepPXYHzUCkUYZ-jDKi_QNsmFGzuATNoyYOn9xAgYLKlCAZfHAkBavoGbWvbihlVgMnN9jnl5qP-1ypEZqnOWwxwUNZyP_5eV8OxgXzIni9sR3b-jhEX3GAB7POVG-P_XifQYPq77-3dqtNBgUwbeNbTVTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18169032d.mp4?token=hZuL3y9Y0KFjKdJ0urErSICnIzK_AR9coBR6nVdEWkhntAeUQGck2JWyBUVRnak2g7xRcDPUALjauFBlYyE2T42gVDlTpnWQ_0urOd_PRYc0B6-hTxRQ5lraggX4XFEAV_zQpoPuZXceMM_rUpbus84zDT-rL9wyfIq-ua1nPfXgEOJ6HNuZH4bgN15HwepPXYHzUCkUYZ-jDKi_QNsmFGzuATNoyYOn9xAgYLKlCAZfHAkBavoGbWvbihlVgMnN9jnl5qP-1ypEZqnOWwxwUNZyP_5eV8OxgXzIni9sR3b-jhEX3GAB7POVG-P_XifQYPq77-3dqtNBgUwbeNbTVTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل های بازی بانوان پرسپولیس چهار - صفر ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140531" target="_blank">📅 19:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140530">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
پایان نیمه نخست  بازی دوستانه
✔️
پرسپولیس صفر ـ چادرملو صفر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140530" target="_blank">📅 19:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140529">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🖼
عکس تیمی پرسپولیس پیش از دیدار تدارکاتی با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140529" target="_blank">📅 17:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140528">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2i3eLF3UzOFuYA9ohyDo-sYHXlRrOnjRBVPQ8SpRY5l4seX5D7Tk8biWjS4HuYEGJRveA0BQKO5jaH2qAXH3umIXP6iWNzdI77ZS-8rUBiJcdzfgcUAtnlDPQhafIZ80Fb0yeMc8DNVQQF017xY5VZa1VzKZKq8wAVsOxEGxoOHJS1LvHt_OCLtTV9O4AXKr4CbjOeH5KklPU37egzMHQczG3xaw1Gp7DWAQXtRyTy1Pxn-O_JsrINalINPaLD7Dk68uMloo00gsQ9SSaBqp6qDvI33WswDinZmfxWE_ltYt39LSWojC29bUGoAOfP2cTZrtuvPtm0srINUGGEUrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پیمان حدادی که بازی پرسپولیس و چادرملو را در ورزشگاه کاظمی تماشا می‌کرد همزمان بازی تیم فوتبال بانوان پرسپولیس با ملوان رو هم با گوشی دنبال می‌کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140528" target="_blank">📅 17:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140527">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdkVckSAJTXe24virrJqeaasBdCD4qVc9GvFTs4ZE5AKRamvZZhgeV0zxs68_8JYxSKfSzKkZBAx1MkiOtpjRwbH0I6Oe56_Cc38LXKuOdflq8-6WWqH-GTRq-2WlYnY-oTEteVTvczQqk3s_bapN0UBOY2eFcW9PdCiJM2WmIZPSZrcS__-NCzAXCSUCv_1UDCm_OVtZcd_HDjWMXwb0wtB89x4TuKr2iDhasWoZ1uzg_ZixV-YbSXgHYBiqQPC_lts0bd8-QQz9e93anKQG2TfaXbLXJHQ9F9C1D4yqIT6UQf5kaDIN_2eAMNrwifJwTbVGIgFbnyb84do6KptHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عکس تیمی پرسپولیس پیش از دیدار تدارکاتی با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140527" target="_blank">📅 17:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140526">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
پرسپولیس فردا بعدازظهر در دیداری تدارکاتی به مصاف چادرملوی اردکان می‌رود. با تصمیم کادر فنی دو تیم این بازی پشت درهای بسته برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140526" target="_blank">📅 17:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140525">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYWP6vuKkTFyUhxyrfhVezCsQjfZX_ZxaVpQD6Mc59SmXeb9BwQCYYO29YvzhBHTMpqdl_CVZNXiQpbqCYlBN_B9RKKyzuyMNUy2jO4Ob-a6uVBsqs-3niOiJb94lO9R2ivW67pWvIIY5Q8J3bOidJ8lTv-y9IVKKafrMjitWv0Rgcq4w1TaI_2gXB_izjvhUvrcXN0G2x_zHiCOdkGfSYwKQGt7sVGIvIy_3WteYNDA0sDWcGNWj6W0wbBs_KRzdEtUQOwRIcac_UYF1AbnhHl88sU5361YxKOGddzsBJK_47vem9j77L2Ni8bMsa7R-qger7odnhvTX3LTsa5WQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با توجه به حذف دیروز امیدها؛
❌
❌
میراثِ قهرمانی «برانکو» با تیم امید در بازی‌های آسیایی بوسان ۲۰۰۲ دست‌نخورده باقی ماند...
❌
❌
این آخرین قهرمانی امیدهای ایران بود و ۲۴ ساله هرگز دیگه هیچ مربی نتونسته تکرارش بکنه تا بزرگی کار برانکوِ کبیر بیشتر به چشم بیاد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140525" target="_blank">📅 15:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140524">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🇮🇷
🎙
جواد خیابانی: تا دلتون بخواد تیم ملی با قلعه‌نویی به ازبکستان باخته. سال به سال دریغ از پارسال. تیم از جام جهانی حذف شد، رفتن فرودگاه استقبال!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140524" target="_blank">📅 15:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140523">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
🤩
فرهیختگان: بزودی قرارداد اوستون اورونوف با پرسپولیس با دستمزد 2.2 میلیون دلاری تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140523" target="_blank">📅 14:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140522">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDIfho-P90cwnUUm5Z7FHRfvxow7QwA8yVUzPC_RUvJhRKvFUqZbJt0qpfY3Zr3IWY0d0SuKWRRKW5ft7PwIVao1v7mSRxGSGHZmas7z8Pk1GvO0PyMZJ-0EYPAofabISRQ_CGs4q1Cd2vgzrnWpoB654JryfsXEvrnvc0sTFbu7WYk7aSeW1YRvynAAcELwy16iH5dtd673jJbMm-TlFdYU9L7IdOggCmX5Y0NjcDhmJXu4k_g1eG3h_0yqYtlJv--fMphK1dVFmZp2mlQpuyxSqpTyr9-1LlUxsVtA9vLn1k_h7UZkIzZanf-S3hrk7z2Wyvc2tmxainlbAi1W-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری؛ ترامپ: تمایل دارم با دکتر پزشکیان در سازمان ملل دیدار کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/140522" target="_blank">📅 14:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140521">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
حسین عبدی بعد از بازگشت تیم امید به ایران و در فرودگاه از سرمربیگری این تیم استعفا و اعلام کرد که دست فدراسیون فوتبال را برای انتخاب مربی باز می‌گذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140521" target="_blank">📅 14:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140520">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🤝
🤝
مدیربرنامه‌های فرهان جعفری: فرهان اوایل دی‌ سربازی‌‌اش به‌پایان‌ میرسه و میخوایم توافقی که هم منافع او حفظ شود هم منافع باشگاه خوب ملوان حفظ شود از این تیم جدا شیم.
❌
❌
فرهان از دو باشگاه پرسپولیس و استقلال آفر دریافت کرده و در پنجره نیم فصل راهی یکی از…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140520" target="_blank">📅 13:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140519">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=RtAyE08u23CTIoUIQChDZ3iv1ZYlkNub2oRTVf5baQj2Z5ShoGmV1LpKclbwgEFz-qFchmJ2SdMeuPNFIpgn_sIgeg2V75kIM4AHShdiq5lJGWG7__urRIZfQmS10wBDFNtkqD4_7DN629B5Nqb726wQb8n5DT_q9oPqP-f9DhMKaG90oGd7Nfo5dydkOb2luf2MzU7MkV5G0nRpPL4hx1av7aBiqk28GzuHGj0JyotWtrs_nTeehpd25TOmAvXthAT1Vz1uBXCMvatnIS60Q-inSsX0cqpYoqD2wSDMC-3-C9f7VuXx-KVhpFywG2-kdRmk8gJDw80eQr9fugz_Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=RtAyE08u23CTIoUIQChDZ3iv1ZYlkNub2oRTVf5baQj2Z5ShoGmV1LpKclbwgEFz-qFchmJ2SdMeuPNFIpgn_sIgeg2V75kIM4AHShdiq5lJGWG7__urRIZfQmS10wBDFNtkqD4_7DN629B5Nqb726wQb8n5DT_q9oPqP-f9DhMKaG90oGd7Nfo5dydkOb2luf2MzU7MkV5G0nRpPL4hx1av7aBiqk28GzuHGj0JyotWtrs_nTeehpd25TOmAvXthAT1Vz1uBXCMvatnIS60Q-inSsX0cqpYoqD2wSDMC-3-C9f7VuXx-KVhpFywG2-kdRmk8gJDw80eQr9fugz_Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🟥
بازیکن تیم‌ملی اسرائیل دیشب بخاطر این شادی بعد گل مقابل اتریش با کارت قرمز اخراج شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140519" target="_blank">📅 13:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140518">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsMVB0XX63mO_BvL2exAnRhwleOjK-49n1yciYI8UB_DNVHJv3wb4051nlbxOLbNR7rkXyFz9fXI-0wIBjb8sGYmWi12r50JCp47bD3f2_MGmK9kb-nVS33rxc71AZt3uzAasiYFTmD0vjznzeAvDNGZUjdNZJv6s74JQ5AA3LTc2MLhsnoTNdpi98sVn0kAzF3e-iFt4MiX595vw3IcEHYYVk8FYGi_2hcni9VVbgZFx8PFZGWxwxfcqMFz6MwapNHYFGqgi1NE5qQy6LR-Vlf5j070vLrBVMIZwDGiM8Gz0nb0FRdeJfswQlXURMyQ6DPu1hWXUgLZO_75-aZdgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
🚨
✅
⭕️
⭕️
⭕️
با تصویب شهرداری نوشهر؛ امتیاز لیگ دویی این تیم به پرسپولیس تهران واگذار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140518" target="_blank">📅 13:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140517">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
جواد نکونام؛ مهدی ترابی به دیدار حساس‌فردا باپرسپولیس رسید اما مهدی هاشم نژاد بدلیل مصدومیت این دیدار رو از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140517" target="_blank">📅 13:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140516">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncs4DpxF7HnLMP4rT0U1wm9hN7st9eRCdw0nPxcP5TjeuBODk8cMkN9nQin8dF5Tr9GFZ16drvLz5KRpS4PT5STU-FZ1pgTK73Tpp9OtDjvHOYYTU0OTpXtuyqRhuOan3-YpYLFUA4vOuQ1BAkRbteyFpxFi8a-ePvvBCOZqX7-sEWWH_fnOpEMXdRpeq57Z6-xZL9LGEZVzYFLA8tsw41MS4iU8S7Mt8Z5Wk-JesZC1nxyDJuy2mqRUvOd2TmkM9ivDOkQNnteyHTGDuTYcc8la42fhxMKFN7bGxZMnqjU2__zj1juv_ZllZJ1aBC8BfXZ5-k6ZcFAp8C6SOgryow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
گاریدو یکی از گزینه‌های تیم‌ملی برای
جانشینی امیر قلعه‌نوعی هستش
😐
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/140516" target="_blank">📅 11:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140515">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⭕️
⭕️
#فوری | ترامپ:
🔻
مقامات آمریکایی به مدت سه ساعت با یک هیئت ایرانی دیدار کردند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140515" target="_blank">📅 11:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140514">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
✔️
✔️
محمدحسین صادقی، وینگر ۲۲ ساله پرسپولیس، در نیم‌فصل به‌صورت قرضی از این تیم جدا خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140514" target="_blank">📅 11:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140513">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⚪️
⚪️
⚪️
مهدی تیکدری در غم از دست  دادن دایی خود عزادار شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140513" target="_blank">📅 11:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140512">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140512" target="_blank">📅 11:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140511">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4VGOiXPbRYLJYon7HHrDfu4Oun_K2P730jd19V8vIC3dN5Bd0egOMjesYNSU9PcJQJXLuXyDEgLdKpCjd-qZwquuxOiqXMUEYmGZ6rfcROmPeIWGJrkXddDbO8TTfZgfNkYoM0XhN_wnU2tBpYSX1gdFP6yzHrgy-8xfu1abqed9u1O7_ih1aSt6p2v7TQhgL1CP4Nw78LcoKXn47l114LFzbrB-KQU51aCAZIa28rZq95ywymI8LqE0VZRCAeMMp9mx_gbSJ4-RYzWazIG1FzdPEHDW_6ZL2QDAbO0hWigdjq5b0xSUHg8oaU8EIJCI7jRPYy1dMSHRcoakkoBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
پرسپولیس قید جذب اندونگ رو زد
🔻
باشگاه پرسپولیس به خاطر ریسک بالای این انتقال و دور بودن اندونگ از شرایط بازی، تصمیم گرفت بی‌خیال جذب این هافبک گابنی بشه
🔻
طبق شنیده‌ها، تا این لحظه تراکتور تنها تیمیه که همچنان دنبال جذب اندونگه و نکونام هم روی این انتقال اصرار داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140511" target="_blank">📅 10:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140510">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsftPNtXKomIu8pzPoBEVtabsENx0cULuCuRDHo390jINqAJoG-V4RcSW7W4jkdzlRyqhhjLc5_ajzEPS5cpFCTcLdjiZ-_Q3-A4OUYG1XI7js9q3qUBL61rnu_oct5muZ4G767uqbTE0iezVeIYaYP2BoI7qx0pE-FhAqhPuUWBvVQhX86Rn6hODscmuLrOYzc7-bJsGK2H0Ba-IzXb25Kf8cBJMkHXeVQ37c8FqUVhDSe0yGSdcUWvXKIqqXBENaYmN7fqqe0W3PpBZjrgzr7sDB6dHYa17GibfoQG5YtjHh65dYb0Q_innROhP1GghHh2WiWCEoJ8RVn2hsDOnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
علیپور و کنعانی‌زادگان ابتدای هفته آینده تست پزشکی می‌دهند
✔️
نتایج این تست‌ها وضعیت بازگشت دو بازیکن به تمرینات را مشخص می‌کند‌ و پرسپولیس امیدوار است هر دو به دیدار ۱۷ مهر مقابل صنعت نفت آبادان برسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140510" target="_blank">📅 10:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140509">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
حسین عبدی بعد از بازگشت تیم امید به ایران و در فرودگاه از سرمربیگری این تیم استعفا و اعلام کرد که دست فدراسیون فوتبال را برای انتخاب مربی باز می‌گذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140509" target="_blank">📅 10:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140508">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
حسین عبدی: از مردم ایران عذرخواهی می‌کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140508" target="_blank">📅 10:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140506">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrcCe8c4T0w49W60Pn_vXsKzY-jBzhqihBLg2HPsUF2ZDf3OkF8QMNIwCdM2pK6JEjHXm_JQGiCAWT-c5xoAlLyaXSHVOOeU4wFlUNXSi8dYrKRI4DOMj3woxSIjmvGppGHIMLgzi8XjUoI9vCCvjePmoqwDMYJUqJP3xxtlTybKeMgWhrMGRWasTPLDTHb8oewYc9HkMfjXsoJ-RNSvFfJBAlJLotBSsCGVNA89UmOco7mbNRb9QRRsiPLkHoFkly84LwQ5fiqjaAuxBrr9x75vETF7PzH7Mtj_KkjCo7mNBEtLx14qUvVR1hO4pHW03pYADvpkrwrEZtIEUwRo3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ITALY -
❤️
BELGIUM
⏰
Tonight 22:15
🏟
Stadio Olimpico
🇪🇺
ایتالیا با بازگشت مانچینی و ترکیبی جوان‌تر، بازی را احتمالاً با مالکیت و فشار از کناره‌ها شروع می‌کند. بلژیک با حضور بازیکنانی مثل دی‌بروینه همچنان در انتقال سریع خطرناک است، اما غیبت تروسار، دوکو و کورتوا روی کیفیت ترکیب اثر دارد. آخرین تقابل رسمی دو تیم با برتری ۱–۰ ایتالیا تمام شد و تقابل قبل‌تر هم ۲–۲ بود؛ بنابراین بازی‌های اخیرشان نزدیک بوده است.
نقطه کلیدی بازی: عملکرد ایتالیا در پرس و کنترل دی‌بروینه مقابل ضدحملات بلژیک؛ احتمالاً جزئیات و توپ‌های دوم تعیین‌کننده خواهند بود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140506" target="_blank">📅 01:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140505">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⭕️
⭕️
⭕️
فوتبالی: جام حذفی به‌دلیل فشردگی تقویم مسابقات و برنامه تیم ملی و امید برگزار نمی‌شود. سهمیه‌ آسیایی هم بر اساس جدول نهایی لیگ برتر تعیین خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140505" target="_blank">📅 23:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140504">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYEFYICljA6gTXdwy4AH2DjlKF43-1SHe2bw3U_s_8YNxOnB4Ih7fdcqGJz-TyiA9g3uWoFJ2cL9kkpDKXOMRF6Rnp7S49CfNRnwo85i7slguii0pHuTJaEdxPGzaqGpWVWa9LOaI0p2VboBzHZA1a0MZw4VT4IpXqAh5fLCLXTpccjpao2cxF62uvAqKif7r_su3n88lZXiAIM2AlTJkGcL-8W5WEQmNeGHPoxH6tayFP7bwmW7RLjcdgBuECnhTnwon12abCc8Lklnwu6t71LixutZxrbn0_ICaMNl6gpxbBQDi9kyeoeTWMUQ1NiIVNZbizSk5IGmQVDms7fPJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎉
جشن تولد آقاکریم برا محمود خان و آقامهدی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140504" target="_blank">📅 23:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140503">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/199c169158.mp4?token=KyzfFcrrughCtQA2fN63cIXT1kX1eUw2fgAQSDSTfyG3LxD24bV7GrmRd19lW2y8lLRbqjZOMT8s12tmdBwMyKgWL7vtZbxUmeveDJqoNv9RwMxDLBIndvlr6f7qmoLaaJ4j0yF80lrtjMwHixoT0w96KTxsAR8mFshYxfrgUpXa57GT2T9ZmChp8GUyC4u_9MvIQwvpBrfSOWNvg-YIa7_NuxcQB1sbpwnZy-OVzsp0ZfCAMvh5RH6-Gon3dHZFzar_DGl6DgXLfu1x3iCDAhcV1LWEb60UJfafQa8jtNgrU4V9h77XokfzWvynQHSZvtgvOWO4mRYRhtW0bHnr3UzqADRXEQS5HzFM_7pWQbnwoI0F4vtT5uoaZRlKIWJ9_v69TdWW01w3qphCCG6cEF6U6M4LY3CSiNMgA0rQY1DLcwAqYritkmJYmh2wYSqF6rzHq-GORnYWJGHbvf-aFmLegnK2zsimX4l02cNXWDI5o0N6yxCxPExppNQhjL8wXoQugMtBvZj9Pq16FAQDbXRgKB40jqXlKg1dNZdmd7tt_2UzonPkd2-4UNUMGzvLPWXiO69T-JcyRufx6th-W2rYlUuyX1QVeeFHej5MO22Xug534xc1qeBS2YMT72EZycDNwYCX-mZ41HaGcMIQeRkMmR-TuPuAse80jEJ_XVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/199c169158.mp4?token=KyzfFcrrughCtQA2fN63cIXT1kX1eUw2fgAQSDSTfyG3LxD24bV7GrmRd19lW2y8lLRbqjZOMT8s12tmdBwMyKgWL7vtZbxUmeveDJqoNv9RwMxDLBIndvlr6f7qmoLaaJ4j0yF80lrtjMwHixoT0w96KTxsAR8mFshYxfrgUpXa57GT2T9ZmChp8GUyC4u_9MvIQwvpBrfSOWNvg-YIa7_NuxcQB1sbpwnZy-OVzsp0ZfCAMvh5RH6-Gon3dHZFzar_DGl6DgXLfu1x3iCDAhcV1LWEb60UJfafQa8jtNgrU4V9h77XokfzWvynQHSZvtgvOWO4mRYRhtW0bHnr3UzqADRXEQS5HzFM_7pWQbnwoI0F4vtT5uoaZRlKIWJ9_v69TdWW01w3qphCCG6cEF6U6M4LY3CSiNMgA0rQY1DLcwAqYritkmJYmh2wYSqF6rzHq-GORnYWJGHbvf-aFmLegnK2zsimX4l02cNXWDI5o0N6yxCxPExppNQhjL8wXoQugMtBvZj9Pq16FAQDbXRgKB40jqXlKg1dNZdmd7tt_2UzonPkd2-4UNUMGzvLPWXiO69T-JcyRufx6th-W2rYlUuyX1QVeeFHej5MO22Xug534xc1qeBS2YMT72EZycDNwYCX-mZ41HaGcMIQeRkMmR-TuPuAse80jEJ_XVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هر جا رفتیم اوت شدیم؛
🎙
درخشان: مشکل، ساختار فوتبال ماست
🟢
سال‌هاست فوتبال ما به قهقرا رفته است
🟢
آیا لژیونرها فوتبال ما را ارتقا داده‌اند؟
🟢
بی رو در بایستی ما فقر فرهنگی فوتبال داریم
🟢
ساختن 10 برابر نیرو، بیشتر از تخریب می‌خواهید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140503" target="_blank">📅 22:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140502">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab25e53c97.mp4?token=cuxrH2pOe-af1XUOL-yorQbOu-FlcpPIbov4hgVw9NCJ7ddH7Qcr7NSTVJ-zpYRnYK_r5E-L72TBt6Bq36pvs6QPEJ2tfnYxTIfuM-JaTlAhUL3nPPQnD1WYNVKF2nTXRWgUQ9dqkSIRIzbAveUM1eVzOrWHLhNIvtenaAqTbwV8F1DCqucoCkKvGDJRmeHGK_4_Ek-O8u3J8uAum8Lhof_VLFmh6kntZuB7yEfDnPgOd0taPPn-u4hExW_j3BHBHskjjmFfLTcTeEqB919sQPydl6Jhcw8ankFzBC2RNU_KrbrIGZxCJICt5UORtIfnKFuo5dELVHlzuWKTnNIw5kldZxjR1Uoe0Ik0ZfzCKGcBmwh22W1aU10KEMv7bYwhycZvqgQaEHl8Az7pc_pptxmvye8lJndP57NnpjWSGYXv5MZnwuDyXALfzeScwJzL7wHsoBjUnb67ILnofG5qhRXyI8sJWwYpfvcD5RDYsbmCpwrSQePxtPaUF5sBMIr7HZSHYCCXMKsUkXdTBDkhDuklU5aYl912kDIS072R7ftoan2IPqB3RGbPIyBgmgTnaQcZqVy5of5_kyBrjuTvhdqnHvUNQ1S_5tk69QWTPkiBjTxD1PQmbZxY1eA9z4sUB6AIJhYAjXZV2mltpiCLfhzgxEHeKZd7MVwpx_VGI0Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab25e53c97.mp4?token=cuxrH2pOe-af1XUOL-yorQbOu-FlcpPIbov4hgVw9NCJ7ddH7Qcr7NSTVJ-zpYRnYK_r5E-L72TBt6Bq36pvs6QPEJ2tfnYxTIfuM-JaTlAhUL3nPPQnD1WYNVKF2nTXRWgUQ9dqkSIRIzbAveUM1eVzOrWHLhNIvtenaAqTbwV8F1DCqucoCkKvGDJRmeHGK_4_Ek-O8u3J8uAum8Lhof_VLFmh6kntZuB7yEfDnPgOd0taPPn-u4hExW_j3BHBHskjjmFfLTcTeEqB919sQPydl6Jhcw8ankFzBC2RNU_KrbrIGZxCJICt5UORtIfnKFuo5dELVHlzuWKTnNIw5kldZxjR1Uoe0Ik0ZfzCKGcBmwh22W1aU10KEMv7bYwhycZvqgQaEHl8Az7pc_pptxmvye8lJndP57NnpjWSGYXv5MZnwuDyXALfzeScwJzL7wHsoBjUnb67ILnofG5qhRXyI8sJWwYpfvcD5RDYsbmCpwrSQePxtPaUF5sBMIr7HZSHYCCXMKsUkXdTBDkhDuklU5aYl912kDIS072R7ftoan2IPqB3RGbPIyBgmgTnaQcZqVy5of5_kyBrjuTvhdqnHvUNQ1S_5tk69QWTPkiBjTxD1PQmbZxY1eA9z4sUB6AIJhYAjXZV2mltpiCLfhzgxEHeKZd7MVwpx_VGI0Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
نتانیاهو تقریبا برای یک سالن خالی سخنرانی کرد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140502" target="_blank">📅 22:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140501">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
حین سخنرانی پزشکیان، نماینده‌های: ایالات متحده آمریکا ، بریتانیا ، آلمان ، فرانسه ، اسرائیل ، سوریه ، لبنان ، عربستان ، مصر ، امارات ، الجزایر ، لهستان ، سوئد ، دانمارک ، کانادا ، ژاپن ، جمهوری آذربایجان , مالزی ، نیوزیلند ، استرالیا ، جمهوری خلق کنگو ،…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140501" target="_blank">📅 22:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140500">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
✔️
✔️
✔️
✔️
تکرار تورنمنت سه‌جانبه؛ دو بازی دوستانه در برنامه پرسپولیس
❌
در جریان تعطیلات پیش روی مسابقات لیگ برتر، شاگردان مهدی تارتار تا پیش از ادامه مسابقات لیگ برتر، دو بازی دوستانه با چادرملو اردکان و گل گهر سیرجان برگزار می کنند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140500" target="_blank">📅 22:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140499">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
✔️
#فوروووووی
❌
با اعلام حدادی جام حذفی برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140499" target="_blank">📅 21:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140498">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=CqyTL_QwsYrqiIDVmif-B7_v1-Dv_gMCZKJfkRgTUkGC70Ms0rwSMZa0ioqzr18TZPvQ4mFjFbtKu8oxOQsHTLu-tVjDBk31WmwrS8B11oIS2a-qF7HOvXB7LfKNt_nEysQRG1ozWxUteq9X59KkmH9ypzpHQI8T0kY6NY9WPO1tXMxR2JOrN0_S1zL9w6L9q7JnP4IlTKiYTwo8JkFmh4LBFuv24h0SQ1RbtwOvRRBelGSOg8RBaZwVEZ4UjL_l02hVFK93y5yixR1QklhxlFLhcxxCNmYoz18SiLdsC6jFZwu8NdyGmP6-ZUgZ2zHZFPJgY32SIRCBKESGQiNNtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=CqyTL_QwsYrqiIDVmif-B7_v1-Dv_gMCZKJfkRgTUkGC70Ms0rwSMZa0ioqzr18TZPvQ4mFjFbtKu8oxOQsHTLu-tVjDBk31WmwrS8B11oIS2a-qF7HOvXB7LfKNt_nEysQRG1ozWxUteq9X59KkmH9ypzpHQI8T0kY6NY9WPO1tXMxR2JOrN0_S1zL9w6L9q7JnP4IlTKiYTwo8JkFmh4LBFuv24h0SQ1RbtwOvRRBelGSOg8RBaZwVEZ4UjL_l02hVFK93y5yixR1QklhxlFLhcxxCNmYoz18SiLdsC6jFZwu8NdyGmP6-ZUgZ2zHZFPJgY32SIRCBKESGQiNNtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجید جلالی: میلیون‌ها دلار خرج مربی خارجی شده اما برای ایرانی‌ها هزینه نکرده‌ایم به همین دلیل است که می‌گویم قلعه‌نویی از مورینیو بهتر است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/140498" target="_blank">📅 20:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140497">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhO896yfqM9Y3Pes28oyVHXuBhwR20TkitOeTfa9vbQWhzu78dGwgRNOQQVHy5xbcczRN4rzTxjG0Jg0kfRNTkyZZO1TCIiIxdfrKiZ7Zyl2hWEoR1htfe3C_cddXxSCxtjnYbvG-sbz02PLxrMu_jNiOCOblLuXsWMzRm6eUzItiT9w00wbnibJOFzBZm_R-mf3dx2h_RzDKICwaT-hE1jnly5hw_IIWxObhfnkPYZU2FKUJ_4BHRnf1lWVHBQe5EHf2lsolEJEVwxNcuSsmfksLxW0oScs5xjGeKK4juZdv7_Z5bIHBoABHsDTgspNO1g7h-ikwGQcGiJNdgC7MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🎙
جواد خیابانی: تا دلتون بخواد تیم ملی با قلعه‌نویی به ازبکستان باخته. سال به سال دریغ از پارسال. تیم از جام جهانی حذف شد، رفتن فرودگاه استقبال!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140497" target="_blank">📅 20:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140496">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=vPxiI1Aga5rnW-3yFM993J862-ODT0K7_m3z-IRWu0_kqAmRsay7G7TRqW7bGdmOC0R2UpFflbycjVAgCwXx4Ms7A6rqhtlkVylCC4yKH4tC-C29_CPavJ9rJXFxwrXhR6X_b0EEjZu4iPjFQurZiANmFZf-1xivu31gKVWKG7AiCTvoEOhdNzOl0u53_sKZ2mtEY590W1UkYjixw-UODw_KM94oefvntExnnDEwEp4bjLFhjQz53ut0bZBSu7H_lhrKc_mV8XRpsTjAzaSFSKyFaghm972Cv3hOCBeRSZi2gOfEDBiXynQZi-V4TEZLuI5ehyOfxWZLbXir2H2eqjKNVMaAtdo1g2TWLh4CWVch5jScWCpO_kXWcHuEVrxgOVJp0Qry6gWY4j_3XkGNrwbEao-bxYiEqvR0pdCZrKO0OOn6f2Y40GQUyCSMjs4Yot4JFEK0xEbQjKZ5JQna8kGcQJ3gCZ99GnP-6vY7SIbr4Wjk-q2LxAB6UrT1dn_ATRQ0JytBeSURxvOLX90uoMi7uR3BRktC_Q-JEPVawi0lxEsMN006ozf8hu9coIEJKGnQh5PZ_mIi3wkG4JmDzcl9yxRlxgJMuCBoSBr-J_wkXJYVOLpyckx75tCVUnmcGPHTiIT7ozsqtdUjAvRVdXpjNhbfHXLIPEYNBKfz5nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=vPxiI1Aga5rnW-3yFM993J862-ODT0K7_m3z-IRWu0_kqAmRsay7G7TRqW7bGdmOC0R2UpFflbycjVAgCwXx4Ms7A6rqhtlkVylCC4yKH4tC-C29_CPavJ9rJXFxwrXhR6X_b0EEjZu4iPjFQurZiANmFZf-1xivu31gKVWKG7AiCTvoEOhdNzOl0u53_sKZ2mtEY590W1UkYjixw-UODw_KM94oefvntExnnDEwEp4bjLFhjQz53ut0bZBSu7H_lhrKc_mV8XRpsTjAzaSFSKyFaghm972Cv3hOCBeRSZi2gOfEDBiXynQZi-V4TEZLuI5ehyOfxWZLbXir2H2eqjKNVMaAtdo1g2TWLh4CWVch5jScWCpO_kXWcHuEVrxgOVJp0Qry6gWY4j_3XkGNrwbEao-bxYiEqvR0pdCZrKO0OOn6f2Y40GQUyCSMjs4Yot4JFEK0xEbQjKZ5JQna8kGcQJ3gCZ99GnP-6vY7SIbr4Wjk-q2LxAB6UrT1dn_ATRQ0JytBeSURxvOLX90uoMi7uR3BRktC_Q-JEPVawi0lxEsMN006ozf8hu9coIEJKGnQh5PZ_mIi3wkG4JmDzcl9yxRlxgJMuCBoSBr-J_wkXJYVOLpyckx75tCVUnmcGPHTiIT7ozsqtdUjAvRVdXpjNhbfHXLIPEYNBKfz5nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🎙
جواد خیابانی: تا دلتون بخواد تیم ملی با قلعه‌نویی به ازبکستان باخته. سال به سال دریغ از پارسال. تیم از جام جهانی حذف شد، رفتن فرودگاه استقبال!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140496" target="_blank">📅 20:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140495">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=F0kJFBeoL88_t5qjbDpRUsEYmVJf2CpWSg7TJlP0hSwy3DRttcP6iqYGUDo6TRPHgxFMeYksYK3kOptwrYXfjQZuel_TTnq1m26I256qHU90C4NLD9iQ-UTn4Wr36CKfOFYIAdqVMMSfFZ5UIi4ZmIBx2cqLJaBayvGm38N3Cs9skc4UTh4EfByMwXEXNUig-rT2gaEW21lCZ4uO-CfXlxs0dde5Y9XvXtT8urRxQ78srgHtjrDzfJIi_bLR3m4fjkSZ5dJ-7OirqgepmS37kZ7zpSQdaRyVykufJWbEZ9xSSj_fUpGAiWJfmPQvmA7g4V8XFOG8AtuACN1ZTrB0kTReXy_RTT3oLMmmYOXcaElN-OiGtiZBAx_bG2J1Ac2AQY0QUzgUMdIhsN1oAOHuulBc_sh0Q527Lsj75kGRLroDLtGa3hLY27S1zC_6mtFOvJFccSvhok9Q55yd-3b-NOGh1Ozt_-GP-FtPVtvjq1Q-Teo8zq5He0Q7aAXcvTDaJkQO83F-76YWQ7qjaSyJy7CjkJM2-5cBt-r1TfWd8c7fDYPeoBfcdw4Ey_OODMZB9V9OThsHBxjyW46IYUYQuMUaM7Iq6AGq6nRbqVAmXQ9LpzXNFJBX0b4EjqtzSn4jN2exotohm0OzLSqfkcjqzmVkKw0uWuLgMvL7bFx4U7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=F0kJFBeoL88_t5qjbDpRUsEYmVJf2CpWSg7TJlP0hSwy3DRttcP6iqYGUDo6TRPHgxFMeYksYK3kOptwrYXfjQZuel_TTnq1m26I256qHU90C4NLD9iQ-UTn4Wr36CKfOFYIAdqVMMSfFZ5UIi4ZmIBx2cqLJaBayvGm38N3Cs9skc4UTh4EfByMwXEXNUig-rT2gaEW21lCZ4uO-CfXlxs0dde5Y9XvXtT8urRxQ78srgHtjrDzfJIi_bLR3m4fjkSZ5dJ-7OirqgepmS37kZ7zpSQdaRyVykufJWbEZ9xSSj_fUpGAiWJfmPQvmA7g4V8XFOG8AtuACN1ZTrB0kTReXy_RTT3oLMmmYOXcaElN-OiGtiZBAx_bG2J1Ac2AQY0QUzgUMdIhsN1oAOHuulBc_sh0Q527Lsj75kGRLroDLtGa3hLY27S1zC_6mtFOvJFccSvhok9Q55yd-3b-NOGh1Ozt_-GP-FtPVtvjq1Q-Teo8zq5He0Q7aAXcvTDaJkQO83F-76YWQ7qjaSyJy7CjkJM2-5cBt-r1TfWd8c7fDYPeoBfcdw4Ey_OODMZB9V9OThsHBxjyW46IYUYQuMUaM7Iq6AGq6nRbqVAmXQ9LpzXNFJBX0b4EjqtzSn4jN2exotohm0OzLSqfkcjqzmVkKw0uWuLgMvL7bFx4U7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💛
🎙
حمله جواد خیابانی به امیر قلعه‌نویی: باید چیکار کنیم که کادرفنی تیم ملی تغییر کنه؟ نتیجه افتضاحی بود. آقای قلعه‌نویی نمیتونی تیم رو جمع کنی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140495" target="_blank">📅 20:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140494">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=LHKEeDEnDNSM1cCUbGLVAhwsQfZEhQiUnTouXzQr637DiIsDeEvPKvvS-d7Ku9G03c65CBfeVJIJckGhGYEhXQi-27ZiDqSFnl7m6zYtBaW9e7br2s87LynmdICe4xoSUksL6v_yrte7D4s2IO7655rqaGhrEIvf89lzRexlywG6OuONerbBI3ZELILIf2AD3yjZoCqfzs5dJKFpt4itAsB9PL-SSrkrqjBxeSILxbxVskRaIgwJigAWSLNuSYRl-ZyQRWfykXoUN5z_wW5oSB8QRVgdQMf_lF9erIuMpRznpnk_RdDEG3p0FFC96ASEeBCxJWH4MnshPX6mfTRVKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=LHKEeDEnDNSM1cCUbGLVAhwsQfZEhQiUnTouXzQr637DiIsDeEvPKvvS-d7Ku9G03c65CBfeVJIJckGhGYEhXQi-27ZiDqSFnl7m6zYtBaW9e7br2s87LynmdICe4xoSUksL6v_yrte7D4s2IO7655rqaGhrEIvf89lzRexlywG6OuONerbBI3ZELILIf2AD3yjZoCqfzs5dJKFpt4itAsB9PL-SSrkrqjBxeSILxbxVskRaIgwJigAWSLNuSYRl-ZyQRWfykXoUN5z_wW5oSB8QRVgdQMf_lF9erIuMpRznpnk_RdDEG3p0FFC96ASEeBCxJWH4MnshPX6mfTRVKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
💚
حمله شدید خیابانی به تیم ملی امید و کنایه به قلعه‌نویی: بازیکنان کره‌شمالی نه مدل مو داشتن نه قیافه آنچنانی می‌گرفتن ولی اومدن مارو درب و داغون کردن، بازیکنان ما چی یکیشون 20 میلیارد میگیره یکیشون 800 میلیارد میگیره اما دوهزار بازی نمیکنند و تحقیر میشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140494" target="_blank">📅 20:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140493">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpUfjhVWebs7rQiDBvY8DlUhhbc_uqngRipw6Tn3S1AKaMiCJBO-rE-S_UZKDUZfPa5DGKZX9EvSVmMPPttvGY-VT6KsnlwYbYIBhy0C57XxDqWURMI6Pt2GYksnrynlBXYeB3eJsgBusghGI-vBcJIZhaWkF5XSh9ir_lQYLFKZ1bV9QnEVSexDcil4MB_jO4uVDGHlocDbPuPHreM5jw5qHwZtUmGiqbaYHHWeBtt0ToLFbFm5Kl_OOHslG6suB2Xkau6RYVLgyYWmwI8F106z6_G3pWuQeVS6Gc7ZTbCfLsD1CcfiLE2fOn40EfUGgECeeMaMIo6nZd9kqwOs8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Netherlands -
🇩🇪
Germany
⏰
Tonight 22:15
🏟
Johan Cruijff Arena
⚽️
آلمان و هلند در شروع لیگ ملت‌های ۲۰۲۶/۲۷؛ دیداری که از نظر آماری کاملاً نزدیک است. هلند در ۱۰ بازی اخیر میانگین ۲.۲ گل زده و ۱.۹ گل خورده داشته، در حالی‌که آلمان ۲.۴ گل زده و فقط ۱.۲ گل خورده است. در تقابل‌های اخیر هم آلمان دست بالاتر را داشته؛ ۳ برد و ۳ تساوی در ۷ رویارویی اخیر و آخرین بازی دو تیم با برتری ۱-۰ آلمان تمام شده است. از نظر روند گلزنی، هر دو تیم پتانسیل بالایی برای گل دارند؛ ضمن اینکه تغییر سرمربی در هر دو تیم، یعنی نخستین بازی رسمی یورگن کلوپ و ژاوی، می‌تواند بازی را از نظر تاکتیکی غیرقابل‌پیش‌بینی‌تر کند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140493" target="_blank">📅 20:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140492">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
✅
✅
سرگیف، اورونوف، آشورماتوف و ماشاریپوف از لیست ازبکستان خط خوردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140492" target="_blank">📅 19:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140491">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
دو گل خوردیم .اونم آقایون شجاع و بیرانوند تقدیم کردن و دوتنه تیم ملی و نابود کردن   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140491" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140490">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⚡️
⚡️
⚡️
عالیشاه از دو سه سال قبل با خانومش هست، مثل کریس و جورجینا و حالا امشب عروسی میکنن، قرار نیست اتفاق خاصی بیفته، عروسی صرفا یه جشنه و قبلا با عقد رسمی شدن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/140490" target="_blank">📅 19:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140489">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
این بازی ساعت 17/30 انجام میشه و بلاخره روی ماه اقای درگاهی رو میبینیم ...ببینیم چه جور بازیکنی هست   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140489" target="_blank">📅 18:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140488">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
✅
با اعلام باشگاه دوا یونایتد بانتن اندونزی، اوسمار ویرا هدایت این تیم را برعده گرفت
❌
این تیم فصل گذشته در لیگ اندونزی هفتم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/140488" target="_blank">📅 16:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140487">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
❌
سعید الهویی : قائدی چون گفت بهترین مربی هایی که باهاشون کرده مجیدی و استراماچونی هستن دعوت نشده تیم ملی
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140487" target="_blank">📅 16:54 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
