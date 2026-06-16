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
<img src="https://cdn4.telesco.pe/file/Z2wavl9CF3feAbtAZItZc3LGziFz6td2DJSh5O1auGFJZ7Jk79QBSVKAfHmdlSGGn7ilLtUzR9ShOc0RwmoIJbOTG69N-kc1mjmAZLZahl4fu8K9hY3cxgw8CteCWdvxMVS5k_7p0fOCbUTQejOcqzH-BI-nzdMhFlpaIOCdoUwVI2Ex4kLKrN6yfqLE0LHQOkssC6o4EZjwhP4r5QSVKIjAEXZLUGb9pqS9qVUD9hUV62cQj3Cw5AQYBzZPsP6IpxbYm-Axha0Aq5YciL0c8qNix__aQBWiUII1Py5NyWJAf9-a1g-rj1yx7lLE81HrnqqJ_DTuTNcg6c589X9Brw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 16:53:27</div>
<hr>

<div class="tg-post" id="msg-133676">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❗️
❗️
خبر پیشنهاد به اسکوچیج دارد فراگیر و جدی می شود.
🔴
تکلیف کادر فنی را مشخص کنید بعد بازیکن بگیرید.اینکه فلانی خیلی خوبه و همه مربیان او را می خواهند استدلال زیبایی نیست.دو فصل اخیر هم با همین فرمول تیم بسته شد و یک سوم خریدها هم با نظر گاریدو و هاشمیان…</div>
<div class="tg-footer">👁️ 791 · <a href="https://t.me/SorkhTimes/133676" target="_blank">📅 16:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133675">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
انتقاد مهدی طارمی از ندادن ویزا به برخی از اعضای تیم ملی:
❗️
فیفا به ما گفته است که همین الان لس آنجلس را ترک کنید/ در صورتی که ما باید فردا صبح ریکاوری انجام می دادیم/ حقیقت را بگویم شرایط برای ما فاجعه است، هیچ ارتباطی با فیفا نداریم/ رییس فدراسیون و نایب…</div>
<div class="tg-footer">👁️ 852 · <a href="https://t.me/SorkhTimes/133675" target="_blank">📅 16:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133673">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
امروز صبح در فرودگاه لس‌آنجلس، مهدی طارمی و سعید الهویی هنگام بازگشت به تیخوانا، چند ساعت توسط مأموران نگه داشته شدند و از آن‌ها بازجویی شد. در نهایت، پس از پیگیری‌های فیفا و فشارهای فدراسیون فوتبال، اجازه خروج برای آن‌ها صادر شد.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/SorkhTimes/133673" target="_blank">📅 16:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133672">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚠️
⚠️
فوووری از ورزش سه: کسری طاهری مهاجم روبین‌کازان با پرسپولیس به توافق نهایی رسیده و بزودی از او رونمایی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SorkhTimes/133672" target="_blank">📅 15:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133671">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
مهدی لیموچی در یکقدمی پرسپولیس/ایلنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SorkhTimes/133671" target="_blank">📅 15:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133670">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
✅
با اوسمار هنوز تمدید نکردن ولی با بازیکنای مدنظرش مذاکره کردن و تهشم رفتن به یه مربی خارجی گفتن بیا تیم ما/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SorkhTimes/133670" target="_blank">📅 14:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133669">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxN5k10rjUccY2eL5zpcHzOxBwp_Sf8lnrmjd8f1ZVaU9M0-ZdNiqH0ZNm61b-sC1y4wSZnSgwbyDIFLyxAJ4TJ7Gctz3Xbnajh3AoBmWmoy8D35CsgVdX0Hq_VmryxdL2P_YYx5PEf6MZcVW007IuMjvsZjbiSmCdc0WF3bKpktt3FT_8JXQLx6NzjVF-nnlgpl_kCy9gifjCHFKUBKiXEo3N5KHxP5P9I9DhS_vaxAJVhRm6gSgk3dHjr_4yDocMKgvahjqmllW8GjlzaOp0EG5LZmcsVsKGfQDPicUpyDfLgfApXkiirnLEEdYOxNPSdsU4ZbW0J8iaoXUtZJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امروز صبح در فرودگاه لس‌آنجلس، مهدی طارمی و سعید الهویی هنگام بازگشت به تیخوانا، چند ساعت توسط مأموران نگه داشته شدند و از آن‌ها بازجویی شد. در نهایت، پس از پیگیری‌های فیفا و فشارهای فدراسیون فوتبال، اجازه خروج برای آن‌ها صادر شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/133669" target="_blank">📅 14:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133668">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GG0X6nWPveLilH1Rw2SAfQF8ROUvsFaVcGUgZT5T2UX_1ahRO0w7wM6XHY85CqvmLk08sErY2TJAn9LbFIPSjWTLmNsOnXZp5k6Kj-uJuXtK_Pi59aX2jFdokF5wsJyTM-KM5zFMTNKo3LEDHLwCE6EBdQYDdRfbgYqe1y_SvLyXcUlKuH88litQl-MICxqknwWK72SwW0L8jGLsKakIO5ktR5OJPMeLag90P9keMxAxoihyx5lXBKuQweTzCRSKpVTC_90O3g_ttkqMWaDTO1f9tcJ31wjWi1KrziFNl8sjf8dB0lpKj39lm36A1RwHAxNzEgS0rw1nxqxG21QEng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قلعه‌نویی همینو قاب می‌کنه میزنه دیوار منزل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SorkhTimes/133668" target="_blank">📅 14:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133667">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❗️
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو…</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SorkhTimes/133667" target="_blank">📅 14:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133666">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rjD1TQXAJVC2UWaUsXkeP_2thIxW7KdcfG8rSsW11Oh9Ynr5KVmMTuiYNmVtwAl89trRkgugY4f07Vjp-HggcuekEshk69AzwDi_w3Yxxe-elxtmEM72cP6L8U-dK8t8ksQ3J_xTVPJEd962-drMwFsYzr3JM_7S50OTnMQbYlEmbjpCXY7j1NJAjsXFq3Hay9sBxVGrnGruaX0h5HJLYJ9cIBuYF7kHGU3K33UQxBI5G3uYOg2qYMUi2-CAKFIaX8cEFw1nQToBsjZu-5kb-zYsj-a9g0seiSM5PZ01UIxxw9aJgvHOZxeIkQjCHJr98HU1bH6QJeY4EtJTbkXdiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بونوس ویژه جام‌جهانی وینکوبت ادامه دارد!
🎁
۱۵٪ بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا هفته آینده دوشنبه ۱ تیرماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SorkhTimes/133666" target="_blank">📅 14:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133665">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❗️
❗️
فرهیختگان: لیست خرید پرسپولیس شامل طاهری، یوسفی، لیموچی، زارع، محبی، نوراللهی، مغانلو، ایری و اون یکی محبی هستش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SorkhTimes/133665" target="_blank">📅 14:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133664">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCwZzcy0nNuHrMC31S7RyuuKSuICE7-4FiM8Nniml7bDxMabp--czMjiJgWwZPxODt9Sp3IvfALHoYubQfHjwOkxC-e3zmVS_vDaPMCBAcKz5vYhctGnej6CSiEkocM1DxJdr6pb8DG08dzpw6Zx5Ag0QQ1tqV0plG30QKZfZrqYtLs1_z3VY-yZRTa-BRCGTkyd91SM0tAigZtmCbIW-ywLanwZNsK6NHTipcLqI1BOKDPhLH09HMtuMVejIovU3OJDBkvctod2HEiGYvqlaRmK7gAdEGWQAjGWl3qAPgbfIrSDR1KFSmaOzg5IzWOvBrFy4DRHKM_KIoTHno7b5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🫪
برگ ریزون
😳
🔽
دروازه بان کیپ ورد که جلوی اسپانیا کلین شیت کرد توی کمتر از ۱۲ ساعت فالوراش از ۵۰ کا شد ۶ میلیون
🔥
🔥
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SorkhTimes/133664" target="_blank">📅 14:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133663">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
یکی از نزدیکان احمد نور به ما گفت؛ احمد تو ایران فقط و فقط لباس پرسپولیس رو بر تن می کنه
🔴
همه ما زیاد از این حرف ها شنیدیم اما تو این مورد، مادامی که پرسپولیس خواهان احمد نور باشه، این هافبک تو ایران انتخاب اول و آخرش مشخص است.///طاهرخانی
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/133663" target="_blank">📅 14:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133662">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
ترامپ: من به تغییر رژیم اعتقاد ندارم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/133662" target="_blank">📅 13:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133661">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
✅
ترامپ: تلاش‌هایی برای تغییر رژیم در ایران صورت گرفت، اما موفق نشدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/133661" target="_blank">📅 13:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133660">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇺🇸
🇺🇸
ترامپ: من علاقه ای به تغییر رژیم در ایران نداشته و ندارم. تحریم های ایران طبق توافق برداشته می شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SorkhTimes/133660" target="_blank">📅 13:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133659">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4Y4CvaLjQafSPzrkpfYvGcAIt066cL7M1EC0PvxcdtI3MIvaWohlDpwZR4h0ArRDVea7fKOv402NhjWhzb5zn86Wfs4ISjSSSRAP46ulpUQjuB7titZnpiv9nivM-_Gt4WTuF2pFHTZhILaX6vXuWmQjg7QAZLL0tAWg3HEOEKreG2qbBtosvOrmqwotA-JMVjmLHCDf21wSc2OnX9C4wpWRljmQckBMj10lsVgVXv7DcjQokSWRUBtYgYIvJ8KKagza4oOuhywipu8PJ2PCU5wviWaVRdvsd1hL8LT42GYWhKrh4sX-5wsM2mHy8apsrh4SagS3NrE__y0jwSjBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو کشت انجام میدی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/133659" target="_blank">📅 12:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133658">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/402b94c148.mp4?token=cYi4h5mzgvO3CtEKWmWvoc60520jU7z4cf2QdetZkz-5RCU-lAmTRDcaI4GH4FXHFoH3T9GFD-LWlWUJo82oICSABarqVIc2JiaXSGl5p9WqRXr7PhH5_AOVpaFXu4OgOCHFJlIejtb7XEIz1cKIqicmNt2v0gi9kGRVaa67UKEFpKs8PWfsVTC7M5ZdKRkxfRad6BcPra_PL4Y2QHVW1-vN51yyZ9LkJX0V8GxHVLePfVZP1U3s2En8Q8sMDpckdimLjaqAajhNKF9Kgxex2EMU-BdSzV_3-P2eMMvnMwHPhKLuOzYOk6hYKXT8hywgY73QsjYj98KGLCgFC1C96A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/402b94c148.mp4?token=cYi4h5mzgvO3CtEKWmWvoc60520jU7z4cf2QdetZkz-5RCU-lAmTRDcaI4GH4FXHFoH3T9GFD-LWlWUJo82oICSABarqVIc2JiaXSGl5p9WqRXr7PhH5_AOVpaFXu4OgOCHFJlIejtb7XEIz1cKIqicmNt2v0gi9kGRVaa67UKEFpKs8PWfsVTC7M5ZdKRkxfRad6BcPra_PL4Y2QHVW1-vN51yyZ9LkJX0V8GxHVLePfVZP1U3s2En8Q8sMDpckdimLjaqAajhNKF9Kgxex2EMU-BdSzV_3-P2eMMvnMwHPhKLuOzYOk6hYKXT8hywgY73QsjYj98KGLCgFC1C96A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
انتقاد مهدی طارمی از ندادن ویزا به برخی از اعضای تیم ملی:
❗️
فیفا به ما گفته است که همین الان لس آنجلس را ترک کنید/ در صورتی که ما باید فردا صبح ریکاوری انجام می دادیم/ حقیقت را بگویم شرایط برای ما فاجعه است، هیچ ارتباطی با فیفا نداریم/ رییس فدراسیون و نایب رییس را نداریم و برای مثال آنالیزور تیم مجبور است کار رسانه انجام دهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/133658" target="_blank">📅 12:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133657">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
✅
با اوسمار هنوز تمدید نکردن ولی با بازیکنای مدنظرش مذاکره کردن و تهشم رفتن به یه مربی خارجی گفتن بیا تیم ما/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/133657" target="_blank">📅 12:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133656">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‼️
مهدی ترابی: در گذشته زیاد آهنگای تتلو گوش میدادم و تتلیتی بودم، اسطوره ورزشیم علی دایی هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/133656" target="_blank">📅 11:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133655">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
این شادی گل جنجالی محبی که به شکل اسلحه به دست هواداران بوده، به سوژه رسانه های خارجی تبدیل شده و خیلیا این خوشحالی رو تهدید کردن آمریکا تلقی کردند و سعی دارن این بازیکن رو محروم کنند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/133655" target="_blank">📅 11:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133654">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❗️
❗️
احتمالاً اسکوچیچ سرمربی بعدی پرسپولیسه/طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/133654" target="_blank">📅 09:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133653">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‼️
اسکوچیچ مربیه خوبیه هیچ شکی نیست ولی 2 میلیون دلار ففط خودش مسلمون ها؟! چقدر مگه روش میخاید بخورید البته حق دارن تعداد بالاست
😄
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/133653" target="_blank">📅 09:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133652">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV1kKpi79-Z6NZg8oaYPv298m3UlUjgHAXmYS5PHwO8hADftghDEXtSO8WLP9Q762ij7e3SKA9w9ozPgTqggocNAjIulHxHbzGi6Glbf9mutjm_J5fipEK1h290dhz5yztKlxdLKfkUbm19ATbvtdIhhhKueBrfjiZkcVtSm0KdpJzzVYrAYBDUe8eR2WGoyv8Amn1YVzCrVRtvdmUxHfRY8VU2_FQkFk7tiTkVky6KiUejy6lixlT8kdgUadxrccYqUi5VXueC5gGHzodyPurQceUMAITO-6TgNpYo6B6uYZqHtWa1OPe8aH4kYXajyaNQK-slPSJyS5FUkjABTRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
استادیوم سوفی لس‌آنجلس که بازی ایران و نیوزلند توش برگزار شد گرونترین استادیوم جهانه و تو ۴ سال با ۵.۵ میلیارد دلار هزینه ساختنش و سقفش از بدنه ورزشگاه جداست و بزرگترین نمایشگر ۳۶۰ درجه ورزشی دنیا با کیفیت 4K رو داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/133652" target="_blank">📅 09:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133651">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=Y3vvJyNfZdbCNpN6IUA025XHGgfFAaak4_PTWSo55cBm6zpwRCqhDhEj8_Q0QZ9gNKa3NmFnPkOknFsDXDBmfgppupRlaj4xBnHKlAEHh9Q8YZcHoQMvQwjpAhOjdD0ec3O5wmRPmShZitz_XfnlGgIS1V7OoDnoHZBGf9gq5m4q33YoZMVLLXtxnvZLT2KZxw7ZynXiagBSUGXO0vr-fM8796pdYDVV7itvgBSYUDGtYwe69vvO5SkZNM1ZjiAVGOK18Tqd0dCBiAw3nn0T_6H_oSq5qzlw-6wbXIVgaN_T1qwDDpvY_rtZPihmGq_cSkVIua3Eb0rY17hvj0v45A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=Y3vvJyNfZdbCNpN6IUA025XHGgfFAaak4_PTWSo55cBm6zpwRCqhDhEj8_Q0QZ9gNKa3NmFnPkOknFsDXDBmfgppupRlaj4xBnHKlAEHh9Q8YZcHoQMvQwjpAhOjdD0ec3O5wmRPmShZitz_XfnlGgIS1V7OoDnoHZBGf9gq5m4q33YoZMVLLXtxnvZLT2KZxw7ZynXiagBSUGXO0vr-fM8796pdYDVV7itvgBSYUDGtYwe69vvO5SkZNM1ZjiAVGOK18Tqd0dCBiAw3nn0T_6H_oSq5qzlw-6wbXIVgaN_T1qwDDpvY_rtZPihmGq_cSkVIua3Eb0rY17hvj0v45A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
این شادی گل جنجالی محبی که به شکل اسلحه به دست هواداران بوده، به سوژه رسانه های خارجی تبدیل شده و خیلیا این خوشحالی رو تهدید کردن آمریکا تلقی کردند و سعی دارن این بازیکن رو محروم کنند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/133651" target="_blank">📅 09:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133650">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
اینفانتینو به رختکن ایران آمد
🔴
تمجید رئیس فیفا از عملکرد تیم ملی در بازی برابر نیوزیلند و گلایه قلعه‌نویی از رفتار میزبان علیه ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/133650" target="_blank">📅 09:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133649">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378c7d7f9a.mp4?token=F4e7xfCqNXmKbn3R2LZ60Xt7MNYVdrtV8Jw8GfcfQJSVvZqbxlAdxN-4aiyNh7ddEBGlfuwBzUV8dLT_001PH5qc7-4vXPKV9VtQBsmWLjbZGqSZf8BA1NMp8zTaYOJ2kkX1ZTPB8z9nL3ke9I_758OyMwptDSppwxWqRl30gIi57NVH_fNrfFRlvQX-4tG6NcktxqhmRbEdJPXeV3RSEhwIjGyhHSE5qthuiepQYkOq0Xh0tTGTZF3dG2wGJddBoKnBMZdReBOk8r82Gb-U4UhvfSPrOv_BVfbBQ8mbVE5MImKUnxglo7EUVLTmmRUCYDWHGjjGccqBP9NPDqyNoRFANJQKJzboDiWzJqn_oSNPff3Xk51mibSRjhTKNyFBS8A2pMz9ClI5RhNYsvCDpTLMw_EtyOcg9huII6uN-z4vH6mZ0ZVAk1aiZk6LcfoxtRvyrlyWPTOxbKciUQjIkrcviSU-lggmGjUHvKgLKlMijDi9lYOtxI-uJAnCQwX-k4ZBrltHYWW41wp2SuhgMP4rrUy0a9b1SNx2IBU5om4nfR0FJpCOvlF3DbwzDnlgclNh7aCFoP9QQbcl0eoIJythstIVdu3Qzcxyy0WSW3h8IzqKNfEmd53BgdsrFbbupnG0SH1HfD16yze0opxI6_8ws7CFpATkEmmRusmzezY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378c7d7f9a.mp4?token=F4e7xfCqNXmKbn3R2LZ60Xt7MNYVdrtV8Jw8GfcfQJSVvZqbxlAdxN-4aiyNh7ddEBGlfuwBzUV8dLT_001PH5qc7-4vXPKV9VtQBsmWLjbZGqSZf8BA1NMp8zTaYOJ2kkX1ZTPB8z9nL3ke9I_758OyMwptDSppwxWqRl30gIi57NVH_fNrfFRlvQX-4tG6NcktxqhmRbEdJPXeV3RSEhwIjGyhHSE5qthuiepQYkOq0Xh0tTGTZF3dG2wGJddBoKnBMZdReBOk8r82Gb-U4UhvfSPrOv_BVfbBQ8mbVE5MImKUnxglo7EUVLTmmRUCYDWHGjjGccqBP9NPDqyNoRFANJQKJzboDiWzJqn_oSNPff3Xk51mibSRjhTKNyFBS8A2pMz9ClI5RhNYsvCDpTLMw_EtyOcg9huII6uN-z4vH6mZ0ZVAk1aiZk6LcfoxtRvyrlyWPTOxbKciUQjIkrcviSU-lggmGjUHvKgLKlMijDi9lYOtxI-uJAnCQwX-k4ZBrltHYWW41wp2SuhgMP4rrUy0a9b1SNx2IBU5om4nfR0FJpCOvlF3DbwzDnlgclNh7aCFoP9QQbcl0eoIJythstIVdu3Qzcxyy0WSW3h8IzqKNfEmd53BgdsrFbbupnG0SH1HfD16yze0opxI6_8ws7CFpATkEmmRusmzezY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
قلعه‌نویی: این بازی بهترین بازی دور اول بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/133649" target="_blank">📅 09:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133648">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FopiHk5RFdF5VYGsCGRjKaKoDLqNMXywcMLNPRCIUf4-_B4Mng2MvB1B6q8uJpoyXBH_o5ypoKAL6ZdL48ARcN7V0Bx0KQOws1WIMQUkbSTtv_p-MK-OlHxyrn30QK2YZfbcjGZYKC855CNKuXPoo-Nkt52VpftjWk1xKbN88bYmT7y-lOQczsGI-hmbizoQqWO2bkZKzeIijNpih0qqVIPsU14Cdeeg_lS2bTmdlKbF-ZhR1frBgqqFjNzMw2AVPJMy9qa8hlG5_4f9x1sglf-f2GkZ1OwXLpMD0ajOvX1O-hsW3pk_TAIdcT4s0keeVZmPhk_sqq5qD0O1ndAkrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
70 هزار و 108 نفر تماشاگر بازی ایران - نیوزیلند در استادیوم سوفای بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/133648" target="_blank">📅 09:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133647">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKHy-7nBumjPW1RZB576j-3iNxy3JlDVvZqCZnwA8JWkR490NCJjcOU1_C8tI3PZKJ3xoir6qZ4YDDa3GDLczim76m8-UJumGHk2VaXhKELz_cPoqB4dm6ewDigFIxE2cRA0CvvFchger0zH1MQBt0k7YACghjg9UtVeBfcXMv5A9ZLkrWYdKsuhI0LWuwskLdYgPJ0CsmggWsLYMW1AQc_7DXJhiRW3Psvxcl4vWN6NNn6wQcGyaAGxwXZJxyFzxRmWAamTeZBbciRyfdLlKxXhmyqiJXLcXy-T7UHr0Bwe6u9bpkDmaj0KrFrJmDUwGwGOGWLS_36o20Wc2CXutg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
تصاویری از هواداران ایرانی به یاد «شهدای مدرسه میناب» در استادیوم سوفای لس آنجلس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/133647" target="_blank">📅 09:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133646">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2RdwqU3GpEdGsnI6E7xBIJO8mNfJwFyYZ1lxvK3kJVijCApxIkgsC1OivJB2_lr693WCv0TlgDhMsU-58C6qMY80lS6J_9VlBvcwfuZ8oE2o4gqoP_fRGSePNKGVm8c9ZNHXApjwgiqFUgGkAM7gE1Iu9xGj7-x1dOX3ntf9MvaEQI3xEoEoOhhwcd76wBF5LfGUGvTL0X3SznrjfYPWtDrW6c36mH4SmZRPAsybRSIxEcn3m8Cnn1ApBY5cQ25bRy_J82bAkDCQjjvimgx0Rxgw7icwBWmAfL_WztsDV5IhQoCY_LRV3QQ5BVl-7dUOLmBMzksPO0oj7dtgG-wqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بونوس ویژه جام جهانی وینکوبت ادامه دارد!
⚪️
IRAN -
⚪️
NEW ZELAND
⚫️
جام‌جهانی گروه G
⏰
سه‌شنبه ساعت ۰۴:۳۰
🏟
استادیوم سوفای
🎁
۱۵٪ بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا هفته آینده ۱ تیر ماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SorkhTimes/133646" target="_blank">📅 06:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133645">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
🔴
و تمام بازی مساوی تمام شد و حیف که از این نیوزیلند ضعیف ما سه امتیاز و نگرفتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/133645" target="_blank">📅 06:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133644">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
گل دوم هم زدیم و شد دو بر دو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/133644" target="_blank">📅 06:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133643">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
دو توپ دو گل برای نیوزیلند ....آقای نعمتی سلطان سوتی   پ.ن دو توپ آورده دو گل زده نیوزیلند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/133643" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133642">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❗️
بریم برای نیمه دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/133642" target="_blank">📅 05:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133641">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
هر چی دارن باید بزارن ..راحت میشه سه امتیاز این بازی و گرفت ...تیم سختی نیست نیوزیلند ..مهمترین 45 دقیقه ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/133641" target="_blank">📅 05:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133640">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
نیمه دوم قایدی و علیپور و حسین زاده میتونن کمکمون کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/133640" target="_blank">📅 05:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133639">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
راحت و با تمرکز بیشتر میشه سه امتیاز این بازی و قشنگ گرفت ..نیوزیلند تو دفاع خیلی ضعیفه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/133639" target="_blank">📅 05:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133638">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇷
گل اول ایران به نیوزیلند توسط رامین رضاییان در دقیقه (32)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/133638" target="_blank">📅 05:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133637">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
نیمه اول یک بر یک تمام شد ‌تو بازی که یک گل زدیم ..یک گل آفساید و یک تیرک ..و عالی بودیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/133637" target="_blank">📅 05:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133636">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❗️
❗️
گل تساوی و خداروشکر زدیم ...این نیوزیلند و میشه برد ...در دفاع ضعف دارن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/133636" target="_blank">📅 05:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133635">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
همچنان توپ و زمین دست ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/133635" target="_blank">📅 05:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133634">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
✅
ما داشتیم خوب بازی میکردیم که نیوزیلند گل اول و زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/133634" target="_blank">📅 05:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133633">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
بازی و خوب شروع کردیم .و سرحال نشون داده تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/133633" target="_blank">📅 04:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133632">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇷
❤️
کم کم بریم برای بازی تیم ملی ایران در جام جهانی 2026....انشالله تیم کشورمون ببره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/133632" target="_blank">📅 04:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133631">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVHUiGAjSSJ8Sq5cxuAUsCht1cnateYc2WGiWbuk6DvGGlgY2YVGVNOmvCzGuVUacaPUHUD2ZxoCTNS2J96WavMjuFhgSaKIKJLG1HcAcA9DmAn-CEJ0j643h8Nh0rWiMacSTV8iJz0EMqglqaXvKkk-MarwomePwMmdR56psZN9z_bCVh8sevkIqrJe1ZqtJ161OdDTyWldO02BY0aFc0iXe8sQawZcAjbYug-EJ8Zi9o5MNACZ68xOzaCok9RKIAiJ22CO5rbfP6cxzpSQmgfiLVGvym8yjvtQ0rqEujF9Z53pzRzP80QpBMNE-a-vvUppyf1vvkzLpAR1Ptr-Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هم اکنون ورزشگاه مملو از تماشاگر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/133631" target="_blank">📅 04:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133630">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🤍
📸
تصاویری از هواداران ایرانی روی سکوهای استادیوم سوفای برای حمایت از تیم ملی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SorkhTimes/133630" target="_blank">📅 04:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133629">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UINYGC2WAJgAgzMbcFZS-PLpn-dzG0F9UZRhc-bzhaJPWAwSm_OAf4SM5DUVvPkkmTxKleNhJ-Tph5H-F4wrqFD8T_vT6nyFBLoF-8q48avrlxpSIPTIrmFe1xdiDgtqmgVNJA7qg0QZA2zQoBXYK7HMWC9hzumi3zDI42J3ZIQ77HcbOud35XN2f12Aq3-0NPWM3e4NbhpbzcOVNRLQ9dAX9jbteuz8HBCZL-4I1O8AkFa_LD_AZVr_52x2TGQfK2OdHLRLL4PjYAONkaEtcEN7ju4qZVzaTzTBagniKtvEdvD6xw3VJ_coYaK4ouNZXnj1OhcQ-PNQov9yiHcy_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤍
📸
تصاویری از هواداران ایرانی روی سکوهای استادیوم سوفای برای حمایت از تیم ملی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/133629" target="_blank">📅 04:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133628">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❗️
جو و حواشی امشب ورزشگاه شاید صداوسیما رو مجبور به سانسورهای شدید و یا حتی قطع تصویر بکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/133628" target="_blank">📅 04:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133627">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
تیم های آسیایی تا الان عالی بودن  اگه قلعه نویی نرینه به آمار شون
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SorkhTimes/133627" target="_blank">📅 04:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133626">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❗️
🔻
وزیر ورزش:
🔹
در جام جهانی پرچم غیررسمی بیاورند یا شعار بدهند، سرپرست تیم مسئولیت دارد که بازی را متوقف کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SorkhTimes/133626" target="_blank">📅 03:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133625">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
حرکت اتوبوس تیم ملی به سمت ورزشگاه سوفای
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/133625" target="_blank">📅 03:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133624">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
حرکت اتوبوس تیم ملی به سمت ورزشگاه سوفای
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/133624" target="_blank">📅 03:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133623">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgsunDqCDS0cYd0DC-xAt5I1LSdE5ZaB2GFLjeK7_fe6k8eLbHvfShqTq7CyjNZiHJbLJDJhrzAAOji00wT77eSMqEfJuS6Qc1unG02p47wZrW_CdrtCnnkS8iYAgUp48yesylKpgJxURrOw0umzNl0whytN2LMYX1aku5bi-vTeEQbLf4A32k-HJkaeiGgfvUEaG97QIJFurdjzu5VSG3N9aCSzJqBk3A0NqYJ2CX24EtwiRIL9iiZaait3f2l7iYPEpFU8gBt-J7npWpeoCcFKN_jVctcmp5MZmGCf7Tg0Is7T-FF9oHOATvxCnl261BCC8ujvuKLH65MyX-r5LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
گرون‌ترین ورزشگاه جهان در تسخیر ایرانی‌ها
❌
این استادیوم 70 هزار نفریه که فقط 5 هزار بلیط از نیوزیلندی‌ها فروش رفته و 65 هزار ایرانی قراره امروز بازی رو از نزدیک ببینن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/133623" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133622">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8709c9d008.mp4?token=jvaQ3CBY1sTHjvmQOGyXo4-gyVJGxJFYyTrbQOdezhBTk1fc8Iog7japuoU9ZtqIFCjsq3nt6Rh9osI0lol0I4oNKt9cG8CO24v5kjyQxVd6GyYasg0ZqVuDlujWFhsmwQQ-sp0BiooUvEDxuPNFcBYXy0wzEoje7nyrDREA1d1tk_01XNBy9H9D_MP3ULRnLGJJt7xjPSAwG2QmBhRt9tMpudw6EeE9akFP5519zij1UguaIQb6ONA7oiuuddcHP6rE6jYE3TgwyiUPLErPqAbAko2qVIt0xngMqGURzOAcoJsmLjjF7xwnasqTez5dxDgVw_H3Nz8jWwOqvg8uUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8709c9d008.mp4?token=jvaQ3CBY1sTHjvmQOGyXo4-gyVJGxJFYyTrbQOdezhBTk1fc8Iog7japuoU9ZtqIFCjsq3nt6Rh9osI0lol0I4oNKt9cG8CO24v5kjyQxVd6GyYasg0ZqVuDlujWFhsmwQQ-sp0BiooUvEDxuPNFcBYXy0wzEoje7nyrDREA1d1tk_01XNBy9H9D_MP3ULRnLGJJt7xjPSAwG2QmBhRt9tMpudw6EeE9akFP5519zij1UguaIQb6ONA7oiuuddcHP6rE6jYE3TgwyiUPLErPqAbAko2qVIt0xngMqGURzOAcoJsmLjjF7xwnasqTez5dxDgVw_H3Nz8jWwOqvg8uUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرکت اتوبوس تیم ملی به سمت ورزشگاه سوفای
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SorkhTimes/133622" target="_blank">📅 02:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133621">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
جو بیرون ورزشگاه سوفی آمریکا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SorkhTimes/133621" target="_blank">📅 02:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133620">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186dc9ec7b.mp4?token=eWTlXi1GoZY0T-jMWuqs3HX9mMpLBZDDtDEMv5IxYnOEL0WA-86f9t0bqclczDPagFkzL2s0mQtEtHdcJyCAUEZjoinBNjE4d_CKaX6H70vfteVE-KnTTfiEz-KabukLpks7W0QEmFer93H8EsvzfPL1gf28y5_QVro6Exofs5wGUQrjpJObetlA9CSCCwvk23-g_C1ReYkCkUKtUGIR8rWyMld8BKXBr9fPYkvguXzjm9tk1zK9vAeJd92FDqOx7KksHuep871hsZFrk1uY2apEEJvv9ISjj2t8UrbOTKBMT2psFIUOST7YLCrIqffnRj5uEjqkTpbicrZ3BTfmVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186dc9ec7b.mp4?token=eWTlXi1GoZY0T-jMWuqs3HX9mMpLBZDDtDEMv5IxYnOEL0WA-86f9t0bqclczDPagFkzL2s0mQtEtHdcJyCAUEZjoinBNjE4d_CKaX6H70vfteVE-KnTTfiEz-KabukLpks7W0QEmFer93H8EsvzfPL1gf28y5_QVro6Exofs5wGUQrjpJObetlA9CSCCwvk23-g_C1ReYkCkUKtUGIR8rWyMld8BKXBr9fPYkvguXzjm9tk1zK9vAeJd92FDqOx7KksHuep871hsZFrk1uY2apEEJvv9ISjj2t8UrbOTKBMT2psFIUOST7YLCrIqffnRj5uEjqkTpbicrZ3BTfmVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
جو بیرون ورزشگاه سوفی آمریکا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SorkhTimes/133620" target="_blank">📅 02:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133619">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
جو و حواشی امشب ورزشگاه شاید صداوسیما رو مجبور به سانسورهای شدید و یا حتی قطع تصویر بکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SorkhTimes/133619" target="_blank">📅 02:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133618">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❗️
ورزشگاه لس آنجلس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SorkhTimes/133618" target="_blank">📅 02:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133617">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
⏱
پایان نیمه اول
🇸🇦
عربستان ۱ - ۰ اروگوئه
🇺🇾
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/133617" target="_blank">📅 02:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133616">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❗️
هلند و ژاپن مساوی کردن
✅
تا اینجای کار تیمای آسیایی خوب بوده عملکردشون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SorkhTimes/133616" target="_blank">📅 02:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133615">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4hpdgK7ALaCyED5_Ph7WkVda9hNEgvC6_Shk76mujGOihwwAi6sqZAp1AZAjRO6M0uh0ZQspg3f1Oix1R5HsP18ib3mj8R-QMY7__j8sc07rTHXk2Xi0kV6c197JXRaPmqf05g_6j5AA_ZMizKGrqAgkVCL9KyBdGIjsAgrX0220xkMQQZMPvvRE214N938QagPwUjllXVgb9ANBfJCAsSYnEhy97DU4W0k32EsTmgVlzOF_HoF_IPU-VQiIEOncGM33zmmzOm6_O47lodykSwiP98sUCmFj_3wgVQcF4f-Tqc82HCYZTCVngkE62Pe_qCyulr-u0XeZHpp5PU1HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بونوس ویژه جام جهانی وینکوبت ادامه دارد!
⚪️
IRAN -
⚪️
NEW ZELAND
⚫️
جام‌جهانی گروه G
⏰
سه‌شنبه ساعت ۰۴:۳۰
🏟
استادیوم سوفای
🎁
۱۵٪ بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا هفته آینده ۱ تیر ماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/133615" target="_blank">📅 02:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133614">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
محمد سیانکی گزارشگر صدا و سیما جمهوری اسلامی راهی آمریکا شده و قرار است هر سه بازی تیم ملی را در جام جهانی گزارش کند
🫥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/133614" target="_blank">📅 02:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133613">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbRgDANqVHqMQTYbBi1-HKEYISfQh_vudJO_4buAzlqecF1C7DHswKfFIEyQw2o3RitGcZHE37PNepyARDfsebhY1Z30tSnGTNvEgmSFhb-NH-r-_qlMIlEfC9ES5nVfgh1Urqs5JkOSZaZq_n3zc6gYUEi_KQ3C96uIUKSFKGjGqPtZZLkb6k9SYHQZnl_lp7hOm63Wqav4QVpsbonLO-uQO1kH3p4ac4e51Uk4MWqVNqv5etV9bV2MNLi7ztX9TYr47ERi9bQE7uS-1D48BsU2bnogF57F1flq5CeqLi89SIdVAT7QjOvLGr4uT1D7FErUyUcuCL_K41QR5BaZew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ورزشگاه لس آنجلس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/133613" target="_blank">📅 02:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133612">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
جام جهانی| کیپ‌ورد نخستین شگفتی جام جهانی ٢٠٢۶ را رقم زد؛ ماتادورها پشت سد کیپ‌ورد؛ لقمه‌ای که از گلوی اسپانیا پایین نرفت
❗️
اسپانیا صفر - کیپ‌ورد صفر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/133612" target="_blank">📅 01:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133611">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
فوری و رسمی/هم اکنون محاصره دریایی آمریکا علیه ایران کاملا برداشته شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/133611" target="_blank">📅 00:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133610">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
جام جهانی 2026؛ تساوی رقبای ایران در گام نخست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/133610" target="_blank">📅 00:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133609">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmfo2qcf_I_9E1z48dME6MyaSEYcOX2egTPoe20BJC77z2xu0r03pw0if_unO48HBKLT7HSIUlc-XDHHtTgejQ3lviTNYEDLmFRwUx9dalbEIoK_63PqxMkp8mHzNf-Jp4eKjIg9iA6xXNbA8UcG-xQKRBqH7s_lbr5sblMEzpLb8lqFYSWawMSE15CCUDMhaJGstmVaWDwjwGD8b3f62tHcjzkqBSeBWdpK5ZsGAv5iYkHsDOJ0xcfC66pIHkk_9lcJPkTNFVE6mGOMtpaxi5TqY_aoBzX9Ps8CD3EuNLK34bmoOOj49DWBXUPE7CmFY8znj9RGiJD3tBBgCyFuAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جام جهانی 2026؛ تساوی رقبای ایران در گام نخست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/133609" target="_blank">📅 00:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133608">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cb4BWE_ZYdeVGa1a953kmYyaN9FwtFVZesoTb4bKPnWPN-BTYHFBvvnBGxbLZ2CClD4XkHNS1iD3ieB_CdWpSy3_QEMmXinn_bfwsGNM1bAR8L-XVrfzfCiMM5ovn22vZWv_yqoqh0-hEpaSaJjwCBVCJUzfSAxOEZkrsBBuQz0xzoLm2Q0RPzDeckfiCCovCEvfZ_FV2RFGupIMQMdSspANu1NZuFQCauVRs1QFd8nO7Qf_ntcAuqBnSOpu2zeABqp8zuI1jrSfmZVcxYXfWr_ZB3kXXEAUr_L7wxIfgoUjI-qESivv8NXgDQfj2ODkTAmPMxN9ZomEAcJvDd1ImA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
رسانه RNZ نیوزیلند در گزارشی اعلام کرد تنها 5 هزار نیوزیلندی بلیط دیدار امشب این تیم مقابل ایران رو خریداری کردند و حدود 60 هزار صندلی دیگر استادیوم سوفی لس‌آنجلس در اختیار ایرانیان خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/133608" target="_blank">📅 23:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133607">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
🔻
وزیر ورزش:
🔹
در جام جهانی پرچم غیررسمی بیاورند یا شعار بدهند، سرپرست تیم مسئولیت دارد که بازی را متوقف کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/133607" target="_blank">📅 23:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133606">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6241f18205.mp4?token=kH2q-SBZm_SKoBN1YorflReLN1F3g8r2StON00mpSAUlGIwBDXfmAh_62UESZ-mtw5jAriJ1A6Z2S6AzicvCagPrEvMQxtIgJLFHOCDRRfGkuEl64fGuFQW6xPm6pF7QTajNeISrbY3PeNuB3IvQKOvmourovfJtYpf5D8ShEmdPwjW5AXpVAsyxq_Mky0_Kr1xW5Ot8NbIbPlfclv6W9dxbKUbLn1QxV7GdNvvPW8gOzItwaHSZw6SVOJv3E7aRySdhChWwsur_m4ixSb8mfcNP6PhLp0vbJhHOgVbe8aRhi5imJynm9vD8a1LiGLLR3iHvqhyj2gKQTZawtjY3oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6241f18205.mp4?token=kH2q-SBZm_SKoBN1YorflReLN1F3g8r2StON00mpSAUlGIwBDXfmAh_62UESZ-mtw5jAriJ1A6Z2S6AzicvCagPrEvMQxtIgJLFHOCDRRfGkuEl64fGuFQW6xPm6pF7QTajNeISrbY3PeNuB3IvQKOvmourovfJtYpf5D8ShEmdPwjW5AXpVAsyxq_Mky0_Kr1xW5Ot8NbIbPlfclv6W9dxbKUbLn1QxV7GdNvvPW8gOzItwaHSZw6SVOJv3E7aRySdhChWwsur_m4ixSb8mfcNP6PhLp0vbJhHOgVbe8aRhi5imJynm9vD8a1LiGLLR3iHvqhyj2gKQTZawtjY3oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خداداد عزیزی : از طریق یکی از دوستان با پرسپولیس صحبت هایی شده، من اگه بسته بودم همینجا جلوی دوربین میگفتم بستم، هنوز قراردادی امضا نشده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/133606" target="_blank">📅 23:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133605">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
خداداد عزیزی: با پرسپولیس صحبت کردم اما هنوز قراردادی بسته نشده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/133605" target="_blank">📅 22:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133604">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
اولین بمب نقل‌وانتقالاتی با دود قرمز!
🔴
🔴
کسری طاهری بازیکن تیم روبین کازان به توافق نهایی با پرسپولیسی‌ها رسیده است و به زودی از او رونمایی می‌شود.
🔴
🔴
ستاره ۱۹ ساله فصل گذشته پیکان که البته به صورت قرضی برای این تیم به میدان می‌رفت و تحت قرارداد روبین کازان است،…</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/133604" target="_blank">📅 22:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133603">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇺🇸
سی‌ان‌ان: ترامپ از حملات اسرائیل به لبنان به‌شدت خشمگین بود و در تماس تلفنی با نتانیاهو از الفاظ رکیک استفاده کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/133603" target="_blank">📅 22:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133602">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">#جام_جهانی
😀
کنداکتور آنلاین جام جهانی فوتبال امروز و بامداد فردا:
😀
اسپانیا
🆚
کیپ ورد
🇨🇻
⏱
ساعت ۱۹:۳۰
🇧🇪
بلژیک
🆚
مصر
🇪🇬
⏱
ساعت ۲۲:۳۰
🇺🇾
اروگوئه
🆚
عربستان
🇸🇦
⏱
ساعت ۱:۳۰
🇮🇷
ایران
🆚
نیوزلند
🇳🇿
⏱
ساعت ۴:۳۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/133602" target="_blank">📅 22:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133601">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
🔴
خداداد عزیزی با حضور در باشگاه پرسپولیس قرارداد شو امضا کرد و رسماً سرپرست پرسپولیس شد / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/133601" target="_blank">📅 22:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133600">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⚠️
⚠️
فوووری از ورزش سه: کسری طاهری مهاجم روبین‌کازان با پرسپولیس به توافق نهایی رسیده و بزودی از او رونمایی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/133600" target="_blank">📅 22:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133599">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341342c2ca.mp4?token=dHsKJhPBUK--W7_K1RvDtdzZ5nlkk4sZxzCOONNFL99MSf74bFyZzMcg1I0WYUvUlAWDjZtGYSeEpm2E7Tjt3reZAcIWACxG1IALcMZGFok0tu6GQdpmS1y-s6dBqCR6Xa2-T4uS6GuXTt5g34vUIzp1JBNZm4lulRXQHaVIYlUINqBrIlmFsMixo3s1Uw3sJx_QYwc8rNfR7MVM2sdgj6XqrC0jxck6MC5ZhbBJNvM0bKM56K3BpAHtA_BQReNIl9-QX-3wMlGPJbVHOhOiIwE6UQeMmihdkH_sNvMdBxrlKrvvboxQEmtVWJoCJskHXytuPsJe-vwNry2KDpRhRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341342c2ca.mp4?token=dHsKJhPBUK--W7_K1RvDtdzZ5nlkk4sZxzCOONNFL99MSf74bFyZzMcg1I0WYUvUlAWDjZtGYSeEpm2E7Tjt3reZAcIWACxG1IALcMZGFok0tu6GQdpmS1y-s6dBqCR6Xa2-T4uS6GuXTt5g34vUIzp1JBNZm4lulRXQHaVIYlUINqBrIlmFsMixo3s1Uw3sJx_QYwc8rNfR7MVM2sdgj6XqrC0jxck6MC5ZhbBJNvM0bKM56K3BpAHtA_BQReNIl9-QX-3wMlGPJbVHOhOiIwE6UQeMmihdkH_sNvMdBxrlKrvvboxQEmtVWJoCJskHXytuPsJe-vwNry2KDpRhRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تو بازی آلمان و ایتالیا در لیگ ملت‌ها، لوکا پورو بازیکن ایتالیا هنگام زدن آبشار بلند میشه و میگه:
یاهووووو
😂
😂
😂
😂
😂
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/133599" target="_blank">📅 21:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133598">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
جام جهانی| کیپ‌ورد نخستین شگفتی جام جهانی ٢٠٢۶ را رقم زد؛ ماتادورها پشت سد کیپ‌ورد؛ لقمه‌ای که از گلوی اسپانیا پایین نرفت
❗️
اسپانیا صفر - کیپ‌ورد صفر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/133598" target="_blank">📅 21:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133597">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">📸
تصاویری از نخستین تمرین پرسپولیس با حضور اوسمار ویرا پس از بازگشت به تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/133597" target="_blank">📅 21:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133596">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
گروه H ؛ جام‌جهانی 2026
🔴
پایان نیمه اول بازی    اسپانیا
🇪🇸
0️⃣
🏆
0️⃣
🇨🇻
کیپ ورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/133596" target="_blank">📅 21:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133595">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAq-F20MrY6l5HJTIB7pVwxETgtmImLkJ_1krrfqrQMvTriJ9vUpNFNlBS6-GqLMHoOckWNe4D1Ls6jpwniA9P9cxMJiUkB-hTHzNiuBHOeXlV38ya9FHEsGi8CvI_avvEn8n9pNwdNUyRwnUn_41OricbtkBc5xOS9GBJQIhi8i533C61op3awou39lLLa9oNZWSd7aeYUIIrR98Se13AAXql2K33aZJ0fpJ4IYcyGrSSFRTbau6bSbx2_nlnshyXYUckhGHHY7Lhy1XZyfTBnFlWWIUwIy8_ZIZTgt99bI3jiEYg1CATR84fbDGR5Zhb7FfAC3rWjiJIuN-bR3kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
گروه G جام‌جهانی ۲۰۲۶
[
ایران
🇮🇷
🆚
🇳🇿
نیوزیلند
]
⏰
بامداد سه‌شنبه ساعت ۰۴:۳۰
🏟
استادیوم سوفای
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/133595" target="_blank">📅 21:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133594">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">📸
تصاویری از نخستین تمرین پرسپولیس با حضور اوسمار ویرا پس از بازگشت به تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/133594" target="_blank">📅 21:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133593">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qj65iASi8PHae4YtufuZf6AKqVHhpOuz2UPHw_L3IijD4ux515wutnZ4FB8MWE5nOX2P4iJao3nHAK1-a0AJHVVTZUHw98zfeAObRg7QrcGlmXhrGdRP3pXGftp52zEJgPu130m7J2NNTsTnnAB7E2CtrXzh8Yg_193YqtOphiz-bqMOBLvo4QI7FlsIqyn2RjwAGuWoqcLx-UHsjNj2wdlN7IRV35VNIXOET5HSitUavxiROj7bRVW7vXzOSs0SZzRzeTxEpFgIUl3V_EsXeCUGwJLmrVk8SkfFRm24FnzLRpm7r-GrBLM6n_pT3RykqhbfBuYUOpd4XYomv3RENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
تصاویری از نخستین تمرین پرسپولیس با حضور اوسمار ویرا پس از بازگشت به تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/133593" target="_blank">📅 20:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133592">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇷
❤️
امشب ساعت 4:30 صبح بازی ایران مقابل نیوزیلند برگذار میشه
🔸
بیدارید یا خواب؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/133592" target="_blank">📅 20:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133591">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">#جام_جهانی
😀
کنداکتور آنلاین جام جهانی فوتبال امروز و بامداد فردا:
😀
اسپانیا
🆚
کیپ ورد
🇨🇻
⏱
ساعت ۱۹:۳۰
🇧🇪
بلژیک
🆚
مصر
🇪🇬
⏱
ساعت ۲۲:۳۰
🇺🇾
اروگوئه
🆚
عربستان
🇸🇦
⏱
ساعت ۱:۳۰
🇮🇷
ایران
🆚
نیوزلند
🇳🇿
⏱
ساعت ۴:۳۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/133591" target="_blank">📅 20:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133590">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">#شفاف_سازی
‼️
خداداد عزیزی،پژمان راهبر،رضا فیض بخش و فرزاد حبیب الهی شق کردن اسکوچیچ رو بیارن…هرچیزی گفتن بهتون کصشره شخص خداداد عزیزی پشت این موضوعه و همه میدونن ارتباط و رابطه بین این افراد نام برده چیه…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/133590" target="_blank">📅 20:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133589">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtFKnJpWWj-Yy1dDlCwGcbfNl7YDzSVPATxcBjk9iCuZx98BghjF2Ji-Kik9F0t6C2yCvqLfnVa-ZQ65UknsU5Df21s7yelDRfapvhulgaRBhWv-7QkAGNYPPK7f7QsCOgsOTYFSEIe9s0NEDT-epR4EwkVs9634x8nzp4mzY2g-eZeHAioQplZKDjRefbzeALcyBguG5AN3PnU2p5l_ZAwnJ2i0pOPhNdMbtg6GdtcDEAfHEHNJQoEW5CyjR6JnsLxYm7wBWHLWdJQXP3fedqi7A5Y_nMxQPQSeVdBG5eJ67SYQr8bNHQFaVpUjMHzw6rFUwyCWz91-K1C7NNGgzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
⚠️
فوووری از ورزش سه: کسری طاهری مهاجم روبین‌کازان با پرسپولیس به توافق نهایی رسیده و بزودی از او رونمایی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/133589" target="_blank">📅 20:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133588">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
🏆
مدیر برنامه کسری طاهری امروز صبح‌ و‌ عصر بامدیریت دو تیم استقلال و پرسپولیس جلسه‌ای مهم برگزار خواهد کرد تا مقصد نهایی کسریِ 19 ساله برای فصل بعد مشخص شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/133588" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133587">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‼️
با این تفاسیر مدیرعامل و هئیت مدیره چیز خره…. از این به بعد اقای احمدی برامون تیم میبنده
😄
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/133587" target="_blank">📅 20:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133586">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">#شفاف_سازی
‼️
خداداد عزیزی،پژمان راهبر،رضا فیض بخش و فرزاد حبیب الهی شق کردن اسکوچیچ رو بیارن…هرچیزی گفتن بهتون کصشره شخص خداداد عزیزی پشت این موضوعه و همه میدونن ارتباط و رابطه بین این افراد نام برده چیه…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/133586" target="_blank">📅 20:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133585">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
با این تفاسیر مدیرعامل و هئیت مدیره چیز خره…. از این به بعد اقای احمدی برامون تیم میبنده
😄
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/133585" target="_blank">📅 20:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133584">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
باشگاه پرسپولیس با خداداد عزیزی به توافقات نهایی دست یافت و بزودی از وی به عنوان جانشین پیروانی معرفی خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/133584" target="_blank">📅 20:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133583">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
تیوی بیفوما امروز از دبی به استانبول میره و فردا صبح میاد تهران تا در تمرینات شرکت کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/133583" target="_blank">📅 18:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133582">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxT_b-Djvie6xw2wdZXIbQBKRzDJYO8URXK-iq8hJyT7o6F1NBG2u7TTyste9QS1r4aT5hmo4XPWcgMWAw5P3_aD9u_eVJTjJSX-cFgxieQp-yopxTwrbje0szyBjW_Xfjc0RCVHXQavuqjGaltW1nuNeX3SjbAh4P5pxVumdmATnEy8OQD7XZfFf57vjVkcOug6JZadrL1_TzKm2jJCDo0Ggr3Wjrn-7GfDElIAQxA-XPfmymIMlliR8y5PuB8ii-YxD-O9qMx14dCDhcWbBFMslINT3kZOaURSAAj4JWsSIxXO4zcAxdrp9LbEsPi_WUtAjxMS6ZzQLaQUrDOMHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عادل فردوسی‌پور در برنامه خود درحال گفتگو با دین هویسن ستاره رئال‌مادرید است
😳
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/133582" target="_blank">📅 18:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133581">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
رئیس جمهور: بیش از ۹۰ درصد اعضای شعام با توافق با آمریکا همراهی کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/133581" target="_blank">📅 18:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133580">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇷
❤️
#فوری | نیویورک تایمز:
🔸
محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، و عباس عراقچی، وزیر امور خارجه، برای امضای توافق با جی‌دی ونس، معاون رئیس‌جمهور، به ژنو سفر خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/133580" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133579">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
🔴
خداداد عزیزی با حضور در باشگاه پرسپولیس قرارداد شو امضا کرد و رسماً سرپرست پرسپولیس شد / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/133579" target="_blank">📅 17:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133578">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
اتفاق خاصی نیوفته خداداد طی روزای آینده با قرارداد مالی خوبی پرسپولیسی میشه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/133578" target="_blank">📅 17:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133577">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
❗️
خبرگزاری فوتبالی :
🔴
🔴
اوسمار به مدیران پرسپولیس اعلام کرده برای شرکت در تورنمنت سه جانبه به ایران برگشته و برای ادامه‌ی همکاری در فصل بعد باید فکر کنه و از خانواده‌اش مشورت بگیره.
🔴
🔴
باشگاه هم به خاطر این که فصل بعد در صورت نیومدن اوسمار به مشکل نخورن؛…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/133577" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133576">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
✅
اوسمار به مدیرای گفته برای فصل بعد باید فکر کنه و با خانوادش مشورت کنه و باشگاه به صورت موازی مذاکره با یه گزینه‌ی داخلی و دو گزینه‌ی خارجی رو پیگیری میکنه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/133576" target="_blank">📅 14:21 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
