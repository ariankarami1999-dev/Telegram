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
<img src="https://cdn4.telesco.pe/file/EgDCOS65lr_9VKhDIC0xXSfsnC18aIFYGQZan4v6MCVTq6OLTbUD0ZqcAIihWSVoKknGC-HOV7fG07zjVZNTCVC3z-hhlBATq9vFclOixne5HTpC-hjp2ichRG8eT28ajpZfHnh29hpiI_58ExZVzRBloFMASohu08CRJStESWI6X9HG_Xg-Z3fOBWiJhs8OjyNDpWJFeH8koUKy0o6xP-LtsgMed3cet8a3MyMXOF3_93e7_fbowc79BiJXH8n3XDsDMNStji3b6udh8IBasiuVJ4aJJIIl36c6Yg7F9WWc8bvpM6QIXdJgDX74h-cLi5Aa4v-KNdP72tbDplRQWQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 23:30:39</div>
<hr>

<div class="tg-post" id="msg-140589">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 940 · <a href="https://t.me/SorkhTimes/140589" target="_blank">📅 23:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140588">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
تاجرنیا: از سازمان لیگ تقاضا دارم قهرمان فصل قبل لیگ برتر را اعلام کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/140588" target="_blank">📅 23:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140587">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
🔴
فارس:
⬇
بودجه پرسپولیس در فصل جاری ۳ هزار میلیارده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SorkhTimes/140587" target="_blank">📅 22:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140586">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
✔️
✔️
بازگشت اورونوف به تمرینات پرسپولیس
✔️
با اعلام باشگاه پرسپولیس، اوستون اورونوف به تمرینات این تیم بازگشت. این وینگر ازبکستانی در فیفادی به اردوی تیم ملی کشورش دعوت نشد و کاناوارو ترجیح داد روی نام او قلم قرمز بکشد.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SorkhTimes/140586" target="_blank">📅 22:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140585">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/140585" target="_blank">📅 21:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140584">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
‼️
🔴
ادعای جنجالی کریمی: خودسرانه برای بیرانوند دفترچه پست کردند؛ در تلاش‌ برای معافیت پزشکی او هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SorkhTimes/140584" target="_blank">📅 21:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140583">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/140583" target="_blank">📅 21:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140582">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SorkhTimes/140582" target="_blank">📅 21:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140581">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SorkhTimes/140581" target="_blank">📅 21:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140580">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/140580" target="_blank">📅 20:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140579">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/140579" target="_blank">📅 19:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140578">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
🎤
بخش اول صحبت های حامد کاویانپور مدیرفنی آکادمی پرسپولیس بعد از دیدار با امید سایپا
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/140578" target="_blank">📅 19:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140577">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⭕️
قسمت جالب سربازی بیرانوند اینه که همین آقا دو ماه پیش علیه علی دایی استوری گذاشته بود: «من هیچ‌وقت از رانت استفاده نکردم»
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/140577" target="_blank">📅 19:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140576">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140576" target="_blank">📅 17:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140575">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
سازمان لیگ مجددا کارت بازی علیرضا بیرانوند رو به مدت یک ماه تا پایان مهر ماه برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان میتونه که در بازی هفته هشتم با استقلال تیمش رو همراهی کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140575" target="_blank">📅 17:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140574">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140574" target="_blank">📅 17:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140573">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
اوستون اورونوف و مارکو باکیچ هم اکنون در ترکیه حضور دارند و اگه مشکل پروازشون حل شه تا شب به تهران میرسند    «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/140573" target="_blank">📅 17:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140572">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vr_4U-1NAVTagh3XkoeppDbU72-N9KunROcnUeSIwjx6H9YENSHKCsfQZHJIRXBZUkpC43v7ZxYa0VvlWhdDYJVBi_5cBmlvBvIvQBygXucYQIDwCHgBxrTlw9U2Dt8ARmMnAF2dyOu-nOJ9ETiQ-1Bgg45RbGuF4zp56-S8wIQ7MwFor5HZs3x2_M1JK-4r-rDQ_XDNLsma01valLP8zuhqxEn2UNGILV2S7RYHqLqnk4SIA3MM8U9-4fdkwPKzXVEJPpu_XSs6hEm-UihImEjOH3uLukZLYqpYqFaNy6J80V5PjvXPPiw1bOr4RYbDTjT2UC6YVkIs6h3mFIfrVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/140572" target="_blank">📅 16:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140571">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🔴
فوری؛ معافیت علیرضا بیرانوند از اعزام به خدمت سربازی، ۱ ماه دیگر تمدید شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/140571" target="_blank">📅 16:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140570">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_AyaFp9-t2D3tPxWX62E-Do4kT2NnOrsnd2vfFGZw261KVejjoshli0SihNhJ1-XFgCtnvrYiHAhmA3BDQsiKxG94F1lYj7c03SxnrAPcRStP1B_bClV1gbRG51GD9WjWOY2pM0bteGWDV0S8gFyoDPqUnH67jnNL3zJeIdHdVK3TZjz6VpfkqIivoHjg6-W8POhM7qJPD5kg20bBu3S4BhfbjGhwm2Y7C3V9WNM2NAFGWgRduhWj5cgQJ2sTmkQHb9-jDxgwDfNbRmQJiTEaaMVSxQPHdFoVC6pu61_d8VtZxJEKEn5CeAlgLBT1CnlDgr95Dme-mCYdmxi8Umlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از بدنسازی امروز پرسپولیس؛ شاگردان تارتار فردا استراحت خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/140570" target="_blank">📅 16:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140569">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/140569" target="_blank">📅 16:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140568">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🔴
فوری؛
معافیت علیرضا بیرانوند از اعزام به خدمت سربازی، ۱ ماه دیگر تمدید شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/140568" target="_blank">📅 15:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140567">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/140567" target="_blank">📅 15:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140560">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/140560" target="_blank">📅 14:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140559">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEBu0rjJLzOzu3QhltTvMfxwAA4cY4LuEexJXYGGGIpdjlvHUPt_CSYJQQtcfqglv556sq9Hwk_-8q1dLaJPpp8tlOBnMa9ZHsHW7nfIkNyL0FPTfsZ1faV8lWZnnAiy4D12Zq_BdHkRScxhmv1vX9qBvrr7HTSpQ7Phbmm988ME4UyTpkb03v1VR8CFHaDc23XLdghkBBGNqWwY6XODdGH4UqJJxN30sPHl37hPAIX301pZdrBixHeCyBMPsuAjPoEsD3rSq35pBJKlva7kEeSCeyKM4WAsSlY7ftTqy9_SjwuaSHnL_FXJzz3MqPUo0i-yfCbdXxtNAL2pDf26Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیم قلعه‌نویی واقعا عجیبه!
❌
بازیکنی که از جام جهانی خط میزنه رو کاپیتان میکنه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/140559" target="_blank">📅 14:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140558">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⚡️
⚡️
تاج اعلام کرد امسال دیگه سقف بودجه وجود نداره، اما فیرپلی مالی اجرا می‌شه.
⚖️
طبق این قانون، باشگاه‌ها باید قرارداد بازیکنا و هزینه‌هاشون رو منتشر کنن و اگه این کار رو نکنن، سازمان لیگ خودش منتشرشون می‌کنه. همچنین باشگاه‌های زیان‌ده فصل بعد با محدودیت…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140558" target="_blank">📅 13:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140557">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
فوتبالی:
✔️
✔️
گفته می‌شود فدراسیون برای جانشینی عبدی با گزینه‌هایی مثل فرهاد مجیدی و مجتبی حسینی وارد مذاکره شده و باید دید در نهایت چه کسی هدایت تیم امید را برعهده می‌گیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140557" target="_blank">📅 13:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140556">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140556" target="_blank">📅 13:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140555">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
علیپور و کنعانی‌زادگان ابتدای هفته آینده تست پزشکی می‌دهند
✔️
نتایج این تست‌ها وضعیت بازگشت دو بازیکن به تمرینات را مشخص می‌کند‌ و پرسپولیس امیدوار است هر دو به دیدار ۱۷ مهر مقابل صنعت نفت آبادان برسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140555" target="_blank">📅 10:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140554">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140554" target="_blank">📅 10:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140553">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140553" target="_blank">📅 10:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140552">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
❌
سه وکیل خارجی باشگاه بعد از دیدن مدارک جدید در پرونده آسانی اعلام کردن، درصد پیروزی پرسپولیس تو پرونده زیاده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140552" target="_blank">📅 09:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140551">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQKvWrwWgEMNU9C8aqN80_lAm1BY7FzNKNM9wsmQmvprjK9k3f1xOcy2F2Unyg7JnYpQcAaNlX8jCxFMFG3x2bXCQPlbBvQwxFlJkZ06wqMy7vzocWUD09ZlPu8kw323CqTEONYXH2DUFAbDtL8m_b3QI3qIqmdVrIlj2hhGc0ZV0xZ6VsUbZgz9Q7q9SdwJu4UQKh04oIaZJYEB9Uc45oq34NyuceZUWf2TbONYiLHDt7CAtPyW2GEt0SsFfTpgLtc-DzYlLboV-wvcpt6eE938BP3BSh2qk5oC2dNYSEiXGI3cBWHZBsdn1YnbjHBTBATmHdZOSBBTDncnnkCv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140551" target="_blank">📅 09:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140550">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srsOVRUHnKj0nXd5s4aHrwXz-FifjpJq8VbMv7QtUh-0MNrEuYKEUZqJ7ioVwDi3XBxkLeUF7emJ2a97K9Ikr5rvsskXZebeHy5YgWETAYjsRGFs3fOojhrjHKZeSygyh1pGsOch0AqXPnF6_BYc3jSdKzAn5k9rEuuzznaQWODlTmjN-OX4owo3gS0Bgbo5CrAZvEcMxqet9kvx8IIxdHZ99EFO9ejFz8AwGsj2u0Jj8RwX_vpq5w4qpFUAoQURTd3TtwV7ZHebyLF8fX3SrcTFc3SFDYRdkqEMGsm9V9IU124uauCO4rgLRnTv-r8MNAxYVxCpKOO49yP32oIoVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140550" target="_blank">📅 01:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140549">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASINgTwpTewXrqY00gnelIcgmsPVystys_oEtuIX6yGqFn0sXgEalZ_nHekGFKwQWcUH3U0pw_28g_a0ThGgwDyDbYyA-x7vl_oCRBfx5YVqSm5R7i08tBSXx1_fISfMwnb4QtAuTzqP0vt7pRB9RdhJyxVWFly44ZLjuSQwh775eum5buy4EIVnhG17JkjY0cFZtv-vsBoqxkb_EmY5NjINf5K6-Kuba27UGLo_I8TE_6HPuJCfzbpAgAH08htqPjesnyUbsmGlY6oriMxJH7TCMFqlomMiQrL5AGBAy6poipeeXbKPZGSaxwToTGcTKaV0yJNE-BId6sihdjO3wA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140549" target="_blank">📅 00:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140548">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGWuBJOSh4B-f6A3iImAu-iGOvtp7CXMI1qDWyLEBJWe1HjYdbNwDP5mymvNZTmS6OwrUPs4b5Wz7xT6eRcvdICgylRdEtXUiTGAzXJv5aNlFeoNgXNbZJOvw5cgAVSfIGmSRjXrEg6fv-DaY55_hhmRwBsBhzmD5o6LgC_sna7dui3gu954KpNYJ6awRJZlQ2p0K2r1eujHBNSkL2jxjZaafCLZNfLmGMMqUtoHVC42pdNZGI4CVkKyIp7bjoJ3_rRF5Hjwg1wS_gcN5KQZjb9RWFWm5J35coxN5iBKUWx06CUmnBaATzvOOVtZEbD5J1DmmhQdSZHlcGDGlWVXVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نتایج هفته دوم لیگ برتر بانوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140548" target="_blank">📅 00:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140547">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔻
پرسپولیس قید جذب اندونگ رو زد
🔻
باشگاه پرسپولیس به خاطر ریسک بالای این انتقال و دور بودن اندونگ از شرایط بازی، تصمیم گرفت بی‌خیال جذب این هافبک گابنی بشه
🔻
طبق شنیده‌ها، تا این لحظه تراکتور تنها تیمیه که همچنان دنبال جذب اندونگه و نکونام هم روی این انتقال…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140547" target="_blank">📅 00:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140546">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpEu0j2WnzQZatAmA_jw0T2ZkQaqLQaZJaZIs-IMerye-5ylFsA9CMbLr276hnEPVHpqfZiuEfk1QCllyww44hr5OoPG3cW3bxLdppVlboSkc2H6ExVcDyJdCVilX5_NEne9k4AMJAVKFK5m-kmjhvNSCuX1fgA7e84dI9zSbRSLZ_AnqKC1amKraKK5ZVb3NbFvAB4uj59iShTPXRQIqyq4Qv2kpISByLOgY1Naaqyju7sYRy86BLddJ82Vo29_LwhtQPzRFhAHVz4W443vtM4asJPYIdfYB4tB1h4uSXz6-Fs3ccpG7w3dRlGbp5fBRF_5FG0qndyQsRRwZOww7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یه سری شایعات از بازگشت اسکوچیچ به تیم ملی در حال انتشاره که نه تایید می‌کنیم و نه رد می‌کنیم.
/فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140546" target="_blank">📅 23:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140545">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⭕️
نتایج ۲۰ بازی اخیر ایران با قلعه نویی ؛ ۸ برد - ۷ مساوی - ۵ باخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140545" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140544">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
برخی اعضای هیات رییسه فدراسیون فوتبال هم از امیر قلعه‌نویی راضی نیستند و خواهان اخراج او هستند اما مهدی تاج تمام قد حامی او است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140544" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140543">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⭕️
👀
صدای پای اسکوچیچ به گوش می‌رسد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140543" target="_blank">📅 23:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140542">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
✔️
چیت ساز، معاون وزارت ارتباطات :
🗣
حتی تو شرایط جنگی هم اینترنت قراره برقرار بمونه و همین که الان اینترنت وصله، نشون میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه؛
✔️
✔️
اینترنت پایدار و باکیفیت جزو حقوق اولیه مردمه و خدمات ارتباطی…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140542" target="_blank">📅 23:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140541">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⭕️
گاریدو یکی از گزینه‌های تیم‌ملی برای  جانشینی امیر قلعه‌نوعی هستش
😐
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140541" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140540">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
غایبان پرسپولیس در دیدار دوستانه امروز
⏺
حسین کنعانی، علیپور، عمری، ابوالفضل جلالی و حسین ابرقویی، باکیچ، ارونوف، نیازمند، زارع، محبی، محمودی، ایری، لطیفی فر و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140540" target="_blank">📅 23:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140539">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHMZW4AD5P5dkwZUOetyMYELwnOK3qazKS_oXRdSX1UcI7DP6woDZ_5RJrfjjN26GdKT2WUDPW43bw0lbhMQbppfn40VaCHl3TMGQs2cTJrRU8qJZPpTIxu0Sh-O7YE6vARbp3fQZhwxAsBUic81UzytWzde1kQkTumNKNgSM9hnBHZDax-J7ox9u5NVGFiUfwtvozdk2teMmYrhRXyikS3mTtvthq1ZJPkSicvGr5_L2zbQKgPQ46JdqGnqcthN42nsInVM_21iOqTfuI93tgvd_K4veOIzNo7eRCrReG0WmvPMco-jVk_fX4r5uTkc9mvQwyXCtTG4HHty8twyFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تولد مهدی تارتار
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140539" target="_blank">📅 21:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140538">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
مهدی تارتار با بازگشت میلادمحمدی مخالفت کرد/تارتار همچنان رزاق پور را میخواهد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140538" target="_blank">📅 21:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140537">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/140537" target="_blank">📅 20:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140536">
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
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140536" target="_blank">📅 20:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140535">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHNCCMJPC92g2KlzM7v8Gjd2Bhndja6DSnpGQi2_UAlVTDPM1-VHwziY_AgTWBLs_5kZn9vejTUSX3-hchJ-NvpWnPqJHH1Amj0DmRUtUu-VtW64aLcyuF-s9ByxbJq40p7Ffv8T1AKU7hqjPG1K4tWm264iqcHc4OOb184Jchy12c21FNczNcO0SUPPjdzidamZFtIKAF2NBu_8z9CzFvecPHwrl0OAVkvSWi39hkxNLdYDSv8XD_9ZVpdYTpOGfG4U7-xvS_D3JzHheJ_Qev2noqA8ey38X-avPgy99KZt8ofCASk64OMy4pdQG5W3BCkjBr7zy1LRE1BuVOGifg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140535" target="_blank">📅 20:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140534">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84e7380b8.mp4?token=E73hq9J3VqabA32p1mNTyzOPYAzqJ8pOX-aRipQjrC8anM6y5H5GozRTS6qXQxvyQFJTwyMMI7eA-lV5rzVK_ZhvAXXCoZ7PRxywqy_Zv9_UkTmZqscyZJPuG3lxaTy9fJFjtc8zJ_Bf1u8arj7NDT7V9DCqyei8q5thSOQp3buvSNPzp9bhqnVt9eo5SZEKKkyInDfbsp3MigyUY_twrtFvSwUlia8CFI-RWESeloYZKrt7X7Nb4435BM5vtq43tKvmSwfhLVVMzo0tKm86lp06M3xVGPyMSdUtk78PpynLz5yidshmxwGW1RzDGIA0bIkIFvwPaNB2h-r5K4ysbnCUv4HyJLzN4SJYAcDaGmZgAkSODgjOYAAeYMbS3U9Aa5WJlzbp5xXUIH9_lmGnmuEvEHKPnFyNOz2bHIIsqntKbLi7tIzVTs3X4fbYy91nuS5TdNL_lgeC2ifwt_DcwixB9nrjlkVooY5VqB1clxlQaxQGHSCnWlsSMXmiKpASbuiKlLqQDfi-LnNWsZuc7r-J5YZaPDX0Z3DO5w5gGzEHn1t0WB2xmjcx0fGhj8_Dd5-zFtay0YhZN_rJINDzVQ8f3nN0DO98cQJVqYRFgCoqyx1eRQ360Wxy0SgbkgwOEMPuIjpj6PKvs92ABtqJ3n_MT5P2mYpPeU-DeqzyAzU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84e7380b8.mp4?token=E73hq9J3VqabA32p1mNTyzOPYAzqJ8pOX-aRipQjrC8anM6y5H5GozRTS6qXQxvyQFJTwyMMI7eA-lV5rzVK_ZhvAXXCoZ7PRxywqy_Zv9_UkTmZqscyZJPuG3lxaTy9fJFjtc8zJ_Bf1u8arj7NDT7V9DCqyei8q5thSOQp3buvSNPzp9bhqnVt9eo5SZEKKkyInDfbsp3MigyUY_twrtFvSwUlia8CFI-RWESeloYZKrt7X7Nb4435BM5vtq43tKvmSwfhLVVMzo0tKm86lp06M3xVGPyMSdUtk78PpynLz5yidshmxwGW1RzDGIA0bIkIFvwPaNB2h-r5K4ysbnCUv4HyJLzN4SJYAcDaGmZgAkSODgjOYAAeYMbS3U9Aa5WJlzbp5xXUIH9_lmGnmuEvEHKPnFyNOz2bHIIsqntKbLi7tIzVTs3X4fbYy91nuS5TdNL_lgeC2ifwt_DcwixB9nrjlkVooY5VqB1clxlQaxQGHSCnWlsSMXmiKpASbuiKlLqQDfi-LnNWsZuc7r-J5YZaPDX0Z3DO5w5gGzEHn1t0WB2xmjcx0fGhj8_Dd5-zFtay0YhZN_rJINDzVQ8f3nN0DO98cQJVqYRFgCoqyx1eRQ360Wxy0SgbkgwOEMPuIjpj6PKvs92ABtqJ3n_MT5P2mYpPeU-DeqzyAzU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
صحبت‌های کنایه‌آمیز توتونچی، مجری برنامه شب‌های فوتبالی به تیم‌ ملی فوتبال: دمتان گرم! در کمتر از 48 ساعت 7 گل از کره شمالی و ازبکستان خوردیم..!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140534" target="_blank">📅 19:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140533">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
❌
❌
❌
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140533" target="_blank">📅 19:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140532">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
❌
❌
❌
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140532" target="_blank">📅 19:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140531">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18169032d.mp4?token=I6iilpiQU7DjgHk7xVV-OA2uydrcILoi9NLroAGgRYKS0Tv-wmq4UMaCKWFIqD286wKtJWXpR3wYCfhe_na8X6RwUQ0L0nhyskGN-Op8bvlPVLvEPsl0ANsL3uAr5oXq12EDGuUAsyrrl36AiLFmsagU4tglLp9vk9Ps8mtLVUr5aTQpmRuNU184miVHlZwBoNqO32Vmyb4CKTNMM5yglcYb1pA6OQ3QHlY6u3hSaOLD4iegoJnBgAc0pFu5OvHcr31KWyzy5GHU2ZYVaL9ZcPAQWJCUSPGl8BG8JDxFxLp-E59elFUacif4HNYx-dJ5y-rrsXk6by4F_kzDEUWRZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18169032d.mp4?token=I6iilpiQU7DjgHk7xVV-OA2uydrcILoi9NLroAGgRYKS0Tv-wmq4UMaCKWFIqD286wKtJWXpR3wYCfhe_na8X6RwUQ0L0nhyskGN-Op8bvlPVLvEPsl0ANsL3uAr5oXq12EDGuUAsyrrl36AiLFmsagU4tglLp9vk9Ps8mtLVUr5aTQpmRuNU184miVHlZwBoNqO32Vmyb4CKTNMM5yglcYb1pA6OQ3QHlY6u3hSaOLD4iegoJnBgAc0pFu5OvHcr31KWyzy5GHU2ZYVaL9ZcPAQWJCUSPGl8BG8JDxFxLp-E59elFUacif4HNYx-dJ5y-rrsXk6by4F_kzDEUWRZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل های بازی بانوان پرسپولیس چهار - صفر ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140531" target="_blank">📅 19:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140530">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
پایان نیمه نخست  بازی دوستانه
✔️
پرسپولیس صفر ـ چادرملو صفر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140530" target="_blank">📅 19:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140529">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🖼
عکس تیمی پرسپولیس پیش از دیدار تدارکاتی با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140529" target="_blank">📅 17:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140528">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KA9rC-uljRgnO_ZxmBBWBmzNvt8f9zEYg2GnfLMrSebsWckQ-yCwb-RPlNSKIOOdLlsrbr4UU7ExmtXzWQcbjMVfmpit4I5HAdx41eoFYmJ1F4gSUViSaj_D__i-Em46cGYXBXJHEP5IIJvoiHDgI5AJVxMwQ-zFUUuWN7Igu_UnPdeM3DbnvbQp9bDl2UHXrGhQHzraCZ8An01TypfHAjQFU3fTfupSsgJkoD5waGqP00koYsMWolFprJNFANHl5E98WmKH9DVxHbUpBmTY-tVpANcCq5btsY6z4HQJTK2M2cNi3Wu6bnab-iC60_mOeeX32LvLsNRft0cyD4IDNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پیمان حدادی که بازی پرسپولیس و چادرملو را در ورزشگاه کاظمی تماشا می‌کرد همزمان بازی تیم فوتبال بانوان پرسپولیس با ملوان رو هم با گوشی دنبال می‌کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140528" target="_blank">📅 17:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140527">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsU81Q8fVFbCjM-ivxvA5dZJmYd2O6LBCkRniQMP-_mgEAv1BkV_GfOFtghylBBQjIzJoudFang-yHMEjBXV49h__xKtS5iJdwTYT8JbUAzQZU2IIhbn0kULBab9nrM1X7aCgFzQuM1QPNh3odkpnqAV6jKID_HfsraKALpgjGRrqoLUlbuHFxdEuTfc8mfA-vxdoIWReMwKqaZDX_wVIv9bKix8c6QzVeevjcpj7O2pXPLKd3G61uEOGTK-t-MgCCHc5H9RwXhmnWEaQo6L6PlI5ytJyjIr6nK83e5Rly-2CXBUZ3kVVeQtl7oksl5uibai0cRm5eAHwYeM_OEEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عکس تیمی پرسپولیس پیش از دیدار تدارکاتی با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140527" target="_blank">📅 17:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140526">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
پرسپولیس فردا بعدازظهر در دیداری تدارکاتی به مصاف چادرملوی اردکان می‌رود. با تصمیم کادر فنی دو تیم این بازی پشت درهای بسته برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140526" target="_blank">📅 17:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140525">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyxNT7as-zSQ8SKah3Qskmhwte6cS-ysPaaJ4gXmxHGmiUJ0t1k2x-w4hDIjK1roJrJw7emEMR_XQHnKfDfxkRaj1FfNV1S2YAnaM9ZNDAlASG7s8fHl1Y4UbBRr6f03Nwu_Q126Cj4xS8brt7aVeolbahI6Kd9blUwbkRYXx1MejOypRBY2PFGeMh9ISnGC1uGlvrprKANNKxcw44R97UkzhPI9oKp0BcdjZXwI9z6RrSwmmJ5Vbd01cdjThPVTlQ88bcXev_Ut3i2bX_i6QP_n3hqO96KGqv5s3_8e4uj9fohBX9z2bDR0k8GGK78I2Sy_W8kW_U4xc-XJDL6svA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140525" target="_blank">📅 15:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140524">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🇮🇷
🎙
جواد خیابانی: تا دلتون بخواد تیم ملی با قلعه‌نویی به ازبکستان باخته. سال به سال دریغ از پارسال. تیم از جام جهانی حذف شد، رفتن فرودگاه استقبال!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140524" target="_blank">📅 15:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140523">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
🤩
فرهیختگان: بزودی قرارداد اوستون اورونوف با پرسپولیس با دستمزد 2.2 میلیون دلاری تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140523" target="_blank">📅 14:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140522">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmAe6TIcE337flQmhwquYRSUXrhbJ2M-cI0qGZKeTzqY4qy-E-S5AV3FdpkpmuSWZ-cJAhuzo54bcKuJz-F_7pDtM31I5gWvJ_Otcb0Q3GpVaklwJSucQotKw0TQjvpXMhNr_HEEM8D2pgvKT92VXZmvIMyD08ZsA08DQ9ro6Y2vlbMQuS5xWL-KTHmJuNzqwiIg8wrpKtrPiUYOdelnyJMdxHv_p2EN1NYcih4HOLC9YKeoRNBl5L5RFDYBlY41d6cUYyIO6jZKN1TWBCMTGlEbAnrBRbiNitcKuxpScXX1v7uK0Rjd2asGx5h-XYEZ65yhDOkIhJ-1wtpzsBFGhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری؛ ترامپ: تمایل دارم با دکتر پزشکیان در سازمان ملل دیدار کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/140522" target="_blank">📅 14:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140521">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
حسین عبدی بعد از بازگشت تیم امید به ایران و در فرودگاه از سرمربیگری این تیم استعفا و اعلام کرد که دست فدراسیون فوتبال را برای انتخاب مربی باز می‌گذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140521" target="_blank">📅 14:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140520">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🤝
🤝
مدیربرنامه‌های فرهان جعفری: فرهان اوایل دی‌ سربازی‌‌اش به‌پایان‌ میرسه و میخوایم توافقی که هم منافع او حفظ شود هم منافع باشگاه خوب ملوان حفظ شود از این تیم جدا شیم.
❌
❌
فرهان از دو باشگاه پرسپولیس و استقلال آفر دریافت کرده و در پنجره نیم فصل راهی یکی از…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140520" target="_blank">📅 13:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140519">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=aCZEFIeu7HVj8fC7yzkJAOPgpeATSTYLEHDrVHKIkLoGQ8B0ef7tGcX1pohHqKz038aQ_24TcDz2V-5Ep6hFLiQu7yz1SiF-UF6oqGt6X5JYRwqeUnKTE3mb8fWHHWFUh6FQtAvm5ip0Vx3XsobwZ_s9oZZ6zAjYHBcBVYKcgeUXWhBdYIivFsh4vuIeTXNMnvP8q2hoCKXkOABhQ4MLc6dfUQnLUuY-cBPAXmizT9igKKhgoImzMa-XmL9LQ5seaEX-2SQn3UHfG4eE3LIS1xquu9BGVcZ_1_ofogrp1qZOP9oK2y1gCdyMwIuuv8FONxFqiyC7X5GMNFpthKP8aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=aCZEFIeu7HVj8fC7yzkJAOPgpeATSTYLEHDrVHKIkLoGQ8B0ef7tGcX1pohHqKz038aQ_24TcDz2V-5Ep6hFLiQu7yz1SiF-UF6oqGt6X5JYRwqeUnKTE3mb8fWHHWFUh6FQtAvm5ip0Vx3XsobwZ_s9oZZ6zAjYHBcBVYKcgeUXWhBdYIivFsh4vuIeTXNMnvP8q2hoCKXkOABhQ4MLc6dfUQnLUuY-cBPAXmizT9igKKhgoImzMa-XmL9LQ5seaEX-2SQn3UHfG4eE3LIS1xquu9BGVcZ_1_ofogrp1qZOP9oK2y1gCdyMwIuuv8FONxFqiyC7X5GMNFpthKP8aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🟥
بازیکن تیم‌ملی اسرائیل دیشب بخاطر این شادی بعد گل مقابل اتریش با کارت قرمز اخراج شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140519" target="_blank">📅 13:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140518">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoBjeSiBl4ZxPdVEVBDr3132FQijl9nbKgZu8V3GRV7lrE0KOhwOq7xs7ld3_Q2I9qFGbctAZvy_i6FGN28t5y0QxrtQyGokOrbkudjNI2BNxrlWzZziGWgHx_HYZGP1ToVA40rPUqS9DEIYmmECauf__WIhmWAkI_f-yu9qa7UzCAq88nvsrqhVFKM1s1EjGyGzGrCLb3goO6SDM8XaIsX67escpnKnwd0nyOwpZuJEcmXSZWBWwAr4zSZ9SiRxcgmxbF6MxSHNQBpXVHElSKnlioVD5zf-YPm3SJPqBOCF7GU1gAa3M5V9W7N6q-ok9UWG0SWRacS2jV2eeP63Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140518" target="_blank">📅 13:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140517">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
جواد نکونام؛ مهدی ترابی به دیدار حساس‌فردا باپرسپولیس رسید اما مهدی هاشم نژاد بدلیل مصدومیت این دیدار رو از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140517" target="_blank">📅 13:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140516">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrBgiGVASqSMuDn-we8eH3dHNFecT6ZIDGSgQ0zMfhdu_1HYQURSuRg8HI9S1pp6hMrpxnS8ZBjPHgVDo3aC-v2S7h6qxqZbssKhZEA-uANvalTRW-Su9aDEBTBiB8UGEgwWKoUGIpFBVfoDbtJ-hFKZ9Q7YcyQ34uh-qK06Ib2hKJ5_QJmv9P1axdx8ay7g2IDDn9xlmX16AWYJbZXE2pnlR9Rwflc8vb1-XaSqNv4cSdSe0pbt3PobfYRc7k--HRIMOc_n9UT0C7r_O2Ee-0FudPaNtxxDSsGjvWpege5xdgvR9cd-FzlAs-vz-fWIFvvoZX7dWnrifNKsHuTA_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/140516" target="_blank">📅 11:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140515">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⭕️
⭕️
#فوری | ترامپ:
🔻
مقامات آمریکایی به مدت سه ساعت با یک هیئت ایرانی دیدار کردند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140515" target="_blank">📅 11:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140514">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
✔️
✔️
محمدحسین صادقی، وینگر ۲۲ ساله پرسپولیس، در نیم‌فصل به‌صورت قرضی از این تیم جدا خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140514" target="_blank">📅 11:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140513">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⚪️
⚪️
⚪️
مهدی تیکدری در غم از دست  دادن دایی خود عزادار شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140513" target="_blank">📅 11:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140512">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140512" target="_blank">📅 11:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140511">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVkPqxRgSKC4AWWfXJ0EoJee2hZzktANKjYOWFkpgiIhstHY7qaAqyJSIEbcyX-ia663xad64JT02rsBHJ2HX9ySCLBgsnMkdxYkoKFc7HujDQxVCmNAl7NEM7uE_Q4rHJLBuRagoGBjd_gDMrT9Hsinr65KSBW1nu058jO30cnMVo93_YNoVWmoUagwoUkzUb5qCfN6ke2QDSvAEnfSdl3YD-gNtS4nVOss9Vwibdz3BlDpD1ljy95xoqs7gFzUgznFwbU-XP7qPkPVf0gFDWBxhI4osPOUx3PkOW3Fw5sSVM0AE56CEwfQzCo8eNQzhQgqZm6yavVPXl_XmwEWtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140511" target="_blank">📅 10:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140510">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iScSKl9TwmPOlcyyzQId7B1xjEtig2jWgxm7k6ExFjvwMoBdVYZtQC5QS_bD0Z5KOOygJRamw2iv_WxNCL7YGFIm1AvZFbLBF6ZatcIMe4jCTXbSKGivzWmGdSO3WBkkuUxnSjG9rkl9yMOACmoQHI_bLnJi0rj86w9YVhB9vG2ui8YKViemacGLYIlrzIvl1EKqNXtROQMx5cPPp1_2sPErCoW3ZW2s9vX34n9exYZJScw1v8_OoxC2N-X45b7SFb1aeJmdd6NUNn1hQn8K2tsHzfHqke7BxYFVKUnjmhve-ez1qXc8GR1wdks2MOgjihVG1EHE4Qs6c9Q6OyRmQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
علیپور و کنعانی‌زادگان ابتدای هفته آینده تست پزشکی می‌دهند
✔️
نتایج این تست‌ها وضعیت بازگشت دو بازیکن به تمرینات را مشخص می‌کند‌ و پرسپولیس امیدوار است هر دو به دیدار ۱۷ مهر مقابل صنعت نفت آبادان برسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140510" target="_blank">📅 10:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140509">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
حسین عبدی بعد از بازگشت تیم امید به ایران و در فرودگاه از سرمربیگری این تیم استعفا و اعلام کرد که دست فدراسیون فوتبال را برای انتخاب مربی باز می‌گذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140509" target="_blank">📅 10:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140508">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
حسین عبدی: از مردم ایران عذرخواهی می‌کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140508" target="_blank">📅 10:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140506">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCvdO49ykXetrZ6UL0rsEpdmDhQJKyoXN-CUvO-6Ghpdp8zFW48FuPcVMBkcmgrVxat9mA99PEk_2pA_ldeNja73zByaxyhSK-xqaiSNCe6yp3W-C_0e4O4KVAFAkXaf6ZEqGbj_XAXnMjBZl__VIK9DhCozo_MM5ZgSztuO6csMk5GBn1hhsHjivMYuEAhcGX2uzDJa66PGePnC3DnIc0yAdsKOOEstRIYos9Up0z4d3isbiZ62W3jtRmWLgoyqDP_gGrqAU2Ep7gIEqlxSja7C2fFcfIa1n_f4e4JWe9VrZ3nGkwA-N8eCaiiyF0ldeG-ffcwK7TDwHrKnHEBSBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140506" target="_blank">📅 01:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140505">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⭕️
⭕️
⭕️
فوتبالی: جام حذفی به‌دلیل فشردگی تقویم مسابقات و برنامه تیم ملی و امید برگزار نمی‌شود. سهمیه‌ آسیایی هم بر اساس جدول نهایی لیگ برتر تعیین خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140505" target="_blank">📅 23:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140504">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAmoJ46fn_drZI1UgVHmPdFo6lkA_ooELs32iuRGt6vpaBVimfq6N5tuK2p39MWCeWCTt_Guawz-jpVXdjFpdjZN_WBEGFmpzL-VjAntH6PYFKygOmVDqkTINdcrDme7lMRLKcf08qGmJeAhrqvzGEogZEjivIAH811m0uN-eUSHl2bjipf-ItlhflcmfxHyqRBw0c6d8iJDmQYKspktCs4FElG6QO4Vo-sNNHm1DhiFsDSV_xSk41CgfgYbvo99poj3KmMiIRa1FVPF9xwKK6ZR5qxgeejJ7kPoZ33hI0_OekcLAa8R0HrHWIQrp0idh_Vt5fFyDfcP0fqo3FI4mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎉
جشن تولد آقاکریم برا محمود خان و آقامهدی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/140504" target="_blank">📅 23:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140503">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/199c169158.mp4?token=tfmtF2M8LTIpnABZSjGyLA5r83_OUqxKWh1BPePU4VGGPnKQ6xGhnFzjlQcraLUv31Z5d8-sEuZxt9ljs23yp4w8pKNsrow2O8EOg2mOfwmS9MZYTruJxN8n5TCj0L2AYDrph4eof15dyt361g_TlbLQiD5-G6oZ92MHQaKwBdIf6E79GRGXhhjumqLth1XBb_fJ_twV6kpmci6qMIP8Q5Vnjh3bK9YfAeVYgvErIl_aJHHp_RCuqzdHiIF7zO88PgwS5YBp-3FbDWpv_kt0Ev3pppFMrS60Sk1Sm4MdpcDTJACL9q9nCuaVv_S654nEV08scF69tn4EOv0uo9F6h3g5cDNyi2R7dVVYv0TQJ-cLa1rTnaA_JGzD6jnB7xpfzi4aOGPq4D00bqk3qGvtEUDHkAToQZgseVP7iyaDEasuqMBMg7eISBX_GNc2sD0Mhg0Z0-H_f7uQBSRL0ZEa5o_NWPaC0YjkD10B9BDAUjJfb-MUT7osi0_3BqeIPf8SXNDH1j2Secf6xeuELQLwAZr74S0_a209dHz-Frl_ptgDr_CfHFwk28B4dD1-LNWtq9dZ0MIic-zIXu3TifXSZ4f4GW4VnClT-uCcRv7Q2DiXJ0nVapyIDI5_P_oCvV2BYFmWmwcikHAbiALei5ZrF-1A7bo_QiyHPdCKp8U9LWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/199c169158.mp4?token=tfmtF2M8LTIpnABZSjGyLA5r83_OUqxKWh1BPePU4VGGPnKQ6xGhnFzjlQcraLUv31Z5d8-sEuZxt9ljs23yp4w8pKNsrow2O8EOg2mOfwmS9MZYTruJxN8n5TCj0L2AYDrph4eof15dyt361g_TlbLQiD5-G6oZ92MHQaKwBdIf6E79GRGXhhjumqLth1XBb_fJ_twV6kpmci6qMIP8Q5Vnjh3bK9YfAeVYgvErIl_aJHHp_RCuqzdHiIF7zO88PgwS5YBp-3FbDWpv_kt0Ev3pppFMrS60Sk1Sm4MdpcDTJACL9q9nCuaVv_S654nEV08scF69tn4EOv0uo9F6h3g5cDNyi2R7dVVYv0TQJ-cLa1rTnaA_JGzD6jnB7xpfzi4aOGPq4D00bqk3qGvtEUDHkAToQZgseVP7iyaDEasuqMBMg7eISBX_GNc2sD0Mhg0Z0-H_f7uQBSRL0ZEa5o_NWPaC0YjkD10B9BDAUjJfb-MUT7osi0_3BqeIPf8SXNDH1j2Secf6xeuELQLwAZr74S0_a209dHz-Frl_ptgDr_CfHFwk28B4dD1-LNWtq9dZ0MIic-zIXu3TifXSZ4f4GW4VnClT-uCcRv7Q2DiXJ0nVapyIDI5_P_oCvV2BYFmWmwcikHAbiALei5ZrF-1A7bo_QiyHPdCKp8U9LWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140503" target="_blank">📅 22:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140502">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab25e53c97.mp4?token=Fam6qdyU4K7-AeSgXM-txxABgp5cPDZdVphXQFJ7vH5Dy2Ic_K5Yi3x_oiZqBGCW53jN5VC1Wfs1Sch8w_DEvMxLs-FE74EmdCPxLQ9bHdux2LLGmrtPgj2anCuqt2aGqDtXx17LgWJ0-SyF0wd2U-VdYrk93NeF0k6cfUV9Ht2PtLXnq8ai9TowsV6SIW1u5beeqwhvx9HXeW2t5Bd-OCc2nLS56uIwRGTloR7ZvaFBhJthcnxtMtKGIvmO6iJmoN8roqD5F0BexbCFzprWefL5onrumdIVcAbHPAeq5-l19gDbeYG4VJiTVcL3SI3wUB9mKhjGShCOiIEplUFJ0aN7KCmld-oUY9vUCXo3jkNDig4B9oi5jS0DqVYy43Bxr6iu14tOfqn-be228PN_lPefjGZ7WK8tpIphvGQ54SnGcPijjwTDi3netZsf-B6SRkcnbBeRRIUxfEjRrzUDTHzozk-OpyJEGBfVtZSGbWiutXsqGzHfUj_mvhC37-2mSFlHnfXPGDViM1Bl0H6qv7M6hpPTyQ4ELuLgSM2pZE_BA5ur1LevDRWEodQcvqMCOAvUBzKDJYxW24cROwfDmemsN6ICpsl34Vy4fdanw2TdKvpcIWnRG2n4uhLgCbZJeqhkcdg8wbwmsPlY98iXhfXBbCtDNvdPVuVLZw4xmrM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab25e53c97.mp4?token=Fam6qdyU4K7-AeSgXM-txxABgp5cPDZdVphXQFJ7vH5Dy2Ic_K5Yi3x_oiZqBGCW53jN5VC1Wfs1Sch8w_DEvMxLs-FE74EmdCPxLQ9bHdux2LLGmrtPgj2anCuqt2aGqDtXx17LgWJ0-SyF0wd2U-VdYrk93NeF0k6cfUV9Ht2PtLXnq8ai9TowsV6SIW1u5beeqwhvx9HXeW2t5Bd-OCc2nLS56uIwRGTloR7ZvaFBhJthcnxtMtKGIvmO6iJmoN8roqD5F0BexbCFzprWefL5onrumdIVcAbHPAeq5-l19gDbeYG4VJiTVcL3SI3wUB9mKhjGShCOiIEplUFJ0aN7KCmld-oUY9vUCXo3jkNDig4B9oi5jS0DqVYy43Bxr6iu14tOfqn-be228PN_lPefjGZ7WK8tpIphvGQ54SnGcPijjwTDi3netZsf-B6SRkcnbBeRRIUxfEjRrzUDTHzozk-OpyJEGBfVtZSGbWiutXsqGzHfUj_mvhC37-2mSFlHnfXPGDViM1Bl0H6qv7M6hpPTyQ4ELuLgSM2pZE_BA5ur1LevDRWEodQcvqMCOAvUBzKDJYxW24cROwfDmemsN6ICpsl34Vy4fdanw2TdKvpcIWnRG2n4uhLgCbZJeqhkcdg8wbwmsPlY98iXhfXBbCtDNvdPVuVLZw4xmrM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
حین سخنرانی پزشکیان، نماینده‌های: ایالات متحده آمریکا ، بریتانیا ، آلمان ، فرانسه ، اسرائیل ، سوریه ، لبنان ، عربستان ، مصر ، امارات ، الجزایر ، لهستان ، سوئد ، دانمارک ، کانادا ، ژاپن ، جمهوری آذربایجان , مالزی ، نیوزیلند ، استرالیا ، جمهوری خلق کنگو ،…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140501" target="_blank">📅 22:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140500">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=HSP4HBVeP9JjnLgssgtgQ08AOBKJLGiGxkg2UHD75Jtttz9YxekHzOrXb-I9V6NX8M9Q2ateV6cjGjm2Q5ybi5DnXLvy77aANPWtMwLBGVWDhq1ZQbbfYsjFyeh_DHCF27xMrJYfijALhGgPevhNuWAAuvNC-GPgKmPToP0VEnkiphgHulIA0F5EWJhfPwcNyEGro2A424wllMBvF9TjtMXzMv6i966zf5MNDMWaEja_0uf_AVoHhv8YFS6rqkIq5mHnBSf6MjZsaF3bnEsdapvtMMdeE63sXSVNX5OVZMJBhUx7nJF1mO71M9iu2H0Kpb2iTTz-ZVGL9jzeeogtKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=HSP4HBVeP9JjnLgssgtgQ08AOBKJLGiGxkg2UHD75Jtttz9YxekHzOrXb-I9V6NX8M9Q2ateV6cjGjm2Q5ybi5DnXLvy77aANPWtMwLBGVWDhq1ZQbbfYsjFyeh_DHCF27xMrJYfijALhGgPevhNuWAAuvNC-GPgKmPToP0VEnkiphgHulIA0F5EWJhfPwcNyEGro2A424wllMBvF9TjtMXzMv6i966zf5MNDMWaEja_0uf_AVoHhv8YFS6rqkIq5mHnBSf6MjZsaF3bnEsdapvtMMdeE63sXSVNX5OVZMJBhUx7nJF1mO71M9iu2H0Kpb2iTTz-ZVGL9jzeeogtKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcIQ9IOAR-2wu4cr1dyarrzN0Hon-Qo8DaRjvVQ73MDwtTqQKSkL7dB6M2sEOX_lNfyDR98W_HTib0gS3l_qFUdR1IG5ginfdnw8AQ7nEIZZ5rnKRRQNn_KqeW-RbEp1V2fdVxVIrjIl21sgY7fXMRCHhrjD4nOzI0bN_dVK5alM6EbNI32kplFgs6l5wyNhd_IXd1-Sh4APV-dZUKFJRGD7NibdY69n22I0u5PN86gMOt5chy3RmeWvgE7uKZAjXE9FxkpmA50U6TRz1m8txE6MAzh6vh6-qF0cRMfgVI21pIxiC2_gkSCBvT907ixykQjtNM7MXYbQIxysVZw8jA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=QSKpnCHqk5tS-kxPSfyCicO9oG68jKkXPWNHnn-6qVTqzvTOj6NIwHLji4w-NmGLLkA0dUxveNbCwWIi94-4ELrST58nrdJPIm3awe7E6Q5BLhwFIPAumYoCKqs3uFufBxxb8gpAeU_h7J9-v80dA0gaGPKeU6MoizjPh7Fw8AkDZbA0aBUQ6ONRZf9b1xamQ6N54fs8d4A5yTh3ik6J36lmbUEzViikovMhD6woA8Kn1NHE7ClxOHxBdP1OM57INgL_wMM06QeLvy5boDKb-Iz7UV3e44zbMwz5vFnaMXTNLuZMNAqw2UQARiG6llPXvl2wVZvbaBAc7Tx6nqM8l2drYZ5_nWzk7gHbNY7Xpz_JUaydHDbBE_GglRgsrQGmT3Ygcjg9sqgci8-k74XthLqVmGlDIXTP9WQ_iNpPP9N_cdgbcNuT7bJBdlocfVVK37ePtj4hfKBjbHUgyVT0nJQacpg0e0ifPAi6DL2WNv0p8f33h8l0tpKryp8EHkPWkdneFwsUGZHWeVMoK7gFXz_r_gFgDCU_9sY2aM85au4lOrzm5vEDftGrk15uuqHgS0qVDa5xBiyRWx2kRhTOGvkz-sFJyeWXGByu-ywQak6OwUFm5y39KraZu4Aby2U89svhAWqQj4uCOlELOS21EngxO8TQRDTZlseFX-w44M8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=QSKpnCHqk5tS-kxPSfyCicO9oG68jKkXPWNHnn-6qVTqzvTOj6NIwHLji4w-NmGLLkA0dUxveNbCwWIi94-4ELrST58nrdJPIm3awe7E6Q5BLhwFIPAumYoCKqs3uFufBxxb8gpAeU_h7J9-v80dA0gaGPKeU6MoizjPh7Fw8AkDZbA0aBUQ6ONRZf9b1xamQ6N54fs8d4A5yTh3ik6J36lmbUEzViikovMhD6woA8Kn1NHE7ClxOHxBdP1OM57INgL_wMM06QeLvy5boDKb-Iz7UV3e44zbMwz5vFnaMXTNLuZMNAqw2UQARiG6llPXvl2wVZvbaBAc7Tx6nqM8l2drYZ5_nWzk7gHbNY7Xpz_JUaydHDbBE_GglRgsrQGmT3Ygcjg9sqgci8-k74XthLqVmGlDIXTP9WQ_iNpPP9N_cdgbcNuT7bJBdlocfVVK37ePtj4hfKBjbHUgyVT0nJQacpg0e0ifPAi6DL2WNv0p8f33h8l0tpKryp8EHkPWkdneFwsUGZHWeVMoK7gFXz_r_gFgDCU_9sY2aM85au4lOrzm5vEDftGrk15uuqHgS0qVDa5xBiyRWx2kRhTOGvkz-sFJyeWXGByu-ywQak6OwUFm5y39KraZu4Aby2U89svhAWqQj4uCOlELOS21EngxO8TQRDTZlseFX-w44M8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140495" target="_blank">📅 20:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140494">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=vCx2EodEw6vIqccKY-wGait2q9p2Iit5oeUUXYFix20yUMWKfYoHpNB9qWi1tdpBpMTUWxMvx54b6Vvhd0NG8-zm6tBF1eCU-QdKf71ialEpUYfzbYrbV3uwJFigh_SlwJcXNe2ZIo8UN4NuDvj_Z99PImOsPtboBv2ALdF_2HkfAugcOo2wWgOltxEfcdfrrQxufIfIfY07XdEuK1YWD_MBFnEggJsEHuez3o1WgILb6KlxDesZN_zaEU6awpuk8XT1mGcvMRVtKDzyFDeZwo0t7K4XXnMrSu-fPz3apGcG3YL-qcv79Ir8CH1gZhY-ocVpnXoE2uG6ADrdYSCiEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=vCx2EodEw6vIqccKY-wGait2q9p2Iit5oeUUXYFix20yUMWKfYoHpNB9qWi1tdpBpMTUWxMvx54b6Vvhd0NG8-zm6tBF1eCU-QdKf71ialEpUYfzbYrbV3uwJFigh_SlwJcXNe2ZIo8UN4NuDvj_Z99PImOsPtboBv2ALdF_2HkfAugcOo2wWgOltxEfcdfrrQxufIfIfY07XdEuK1YWD_MBFnEggJsEHuez3o1WgILb6KlxDesZN_zaEU6awpuk8XT1mGcvMRVtKDzyFDeZwo0t7K4XXnMrSu-fPz3apGcG3YL-qcv79Ir8CH1gZhY-ocVpnXoE2uG6ADrdYSCiEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
💚
حمله شدید خیابانی به تیم ملی امید و کنایه به قلعه‌نویی: بازیکنان کره‌شمالی نه مدل مو داشتن نه قیافه آنچنانی می‌گرفتن ولی اومدن مارو درب و داغون کردن، بازیکنان ما چی یکیشون 20 میلیارد میگیره یکیشون 800 میلیارد میگیره اما دوهزار بازی نمیکنند و تحقیر میشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140494" target="_blank">📅 20:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140493">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfUa1CdOcu-3SfHpSbfmlz5LD9d6Lcx8RMI4sphB20-bsSAltuZzGzb--vWfOelgZhLvnc7vmChEGplugYavf0GURYZmEBIb1tU5FHgQpWjHz9q9WdZurs7Of0ps-DANoGfDGuElNHePayW7ObtQ3tevVk_14EIJXAk5V-8iiHyi8XsrNW0wRNFvxx5JEOa6DWjwk41x7DdF8iGDlXkPJIOp3-o_zieTX0FL-9_q5CQo-nZ5ZPkJvu_Wey-N88d2U-pj33jaVRnvMdI-rJrRZtV_bOne0szvZlNsUBlQ9oRpv3xOlnzEk7jiy1qEOpwMvrw2zXQQo4HYcLaOvT5gKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140493" target="_blank">📅 20:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140492">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
✅
✅
سرگیف، اورونوف، آشورماتوف و ماشاریپوف از لیست ازبکستان خط خوردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140492" target="_blank">📅 19:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140491">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
دو گل خوردیم .اونم آقایون شجاع و بیرانوند تقدیم کردن و دوتنه تیم ملی و نابود کردن   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140491" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140490">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⚡️
⚡️
⚡️
عالیشاه از دو سه سال قبل با خانومش هست، مثل کریس و جورجینا و حالا امشب عروسی میکنن، قرار نیست اتفاق خاصی بیفته، عروسی صرفا یه جشنه و قبلا با عقد رسمی شدن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/140490" target="_blank">📅 19:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140489">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
این بازی ساعت 17/30 انجام میشه و بلاخره روی ماه اقای درگاهی رو میبینیم ...ببینیم چه جور بازیکنی هست   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140489" target="_blank">📅 18:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140488">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/140488" target="_blank">📅 16:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140487">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140487" target="_blank">📅 16:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140486">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
ترکیب ایران مقابل ازبکستان اعلام شد
⏺
علیرضا بیرانوند، سامان فلاح، علی نعمتی، صالح حردانی، احسان حاج‌صفی، سعید عزت‌اللهی، امید نورافکن، محمدمهدی محبی، آریا یوسفی، مهدی طارمی و دنیس درگاهی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140486" target="_blank">📅 16:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140485">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
✅
ورزش سه : زارع امروز جلو ازبکستان فیکسه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140485" target="_blank">📅 16:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140484">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
مهدی ترابی بازیکن32ساله باشگاه تراکتور که دچارپارگی رباط‌صلیبی شد هفته آینده پای مصدومش رو به تیغ جراحان خواهد سپرد و تا اوایل اردیبهشت ماه سال بعد دور از میادین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140484" target="_blank">📅 16:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140483">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
فدراسیون به باشگاه گفته که مدرکتون برای یاسر آسانی کمه و اون مدرک اصلی و قوی که ما میخایم رو ندارید شما ، حالا باشگاه از طریق یکی از ایجنت های ایرانی یاسر آسانی یه مدرک فوق العاده قوی رو کرده که فسخ رسمی این بازیکن با استقلال رو نشون میده و فدراسیون هم…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140483" target="_blank">📅 16:28 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
