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
<img src="https://cdn4.telesco.pe/file/c8t7Vfz7xkamrB74f8ZPrnRexo_L8pG5clGPdHOQM7WqYUkCPSCWZC5k1eEIHcu8fYABfyTvCdc2hhZ0AUZzA4HRz_ouDvXaiiXfIr3qz_m24In6HW9MjFiYfbNo3rUDWxtrRkHyIDEMRykVEephAHOVc5DQygm0W0lF6j4HOAv1h1lXRdeUVjTWjeSRQbsatGwlDJwx7g8JY0qo4qWZHlBPjGdEqDICVHIkUZgVKrWp1WWYJ_S9kWoQbLp3sTgntrl85vKl82vGfaMsQLrxTsEigXLcBtcT9NEHNTbHuJdt574gxsLtVJ6lVYandhsA_MpMCvJ2m-Yp2Re8PG7aqg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 21:14:38</div>
<hr>

<div class="tg-post" id="msg-140651">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
افشین قطبی نزدیک‌ترین گزینه به هدایت تیم امید است.
🤝
فوتبال ۳۶۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 260 · <a href="https://t.me/SorkhTimes/140651" target="_blank">📅 21:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140650">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
✅
واکنش فدراسیون فوتبال به اظهارات تاجرنیا درباره جام قهرمانی فصل گذشته
❌
❌
اظهارات علی تاجرنیا، رئیس هیئت‌مدیره استقلال، درباره وعده اهدای جام قهرمانی فصل گذشته به این باشگاه، با واکنش جدی فدراسیون فوتبال مواجه شده است.
❌
❌
پس از موج واکنش‌های مجازی و اعتراض…</div>
<div class="tg-footer">👁️ 383 · <a href="https://t.me/SorkhTimes/140650" target="_blank">📅 21:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140649">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
همه هواداران پرسپولیس از مدیران باشگاه عاجزانه تقاضا دارن تا ماجرای یاسر آسانی رو تا ته تهش پیش برن.
🔺
آخرش اینه که یه پولی میخواییم بدیم و رای هم صادر نشه به نفعمون، این همه پرونده بوده که هزینه کردیم و باختیم، اینم روش
🔺
دقیقا از روزی که فهمیدن…</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/SorkhTimes/140649" target="_blank">📅 19:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140648">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
پاسخ مثبت پرسپولیس به برگزاری جام حذفی بدون ملی‌پوشان
❌
باشگاه پرسپولیس با برگزاری رقابت‌های جام حذفی حتی در صورت غیبت بازیکنان ملی‌پوش موافقت کرده و خواهان برگزاری این مسابقات در فصل جاری است.
❌
با توجه به فشردگی برنامه مسابقات و حضور ملی‌پوشان در اردوهای…</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SorkhTimes/140648" target="_blank">📅 18:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140647">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✖️
گفته میشود باشگاه پرسپولیس برای تمدید قرارداد 5ساله با امیرحسین محمودی و 3ساله با پیام نیازمند به توافق رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/140647" target="_blank">📅 18:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140646">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
✔️
✔️
✔️
❌
جواد عطایی، سامان نقیبی، ابوالفضل شیرازی، محمد حسین پژوهان،‌ پوریا آزاد رنجبر و محمدامین دهقانی بازیکنان تیم‌های جوانان و امید پرسپولیس بودند که امروز در ترکیب سرخپوشان به میدان رفتند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/140646" target="_blank">📅 17:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140645">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ct_ou6uSFYOxNw3utQJqQnwrCQfUgbE-aItwlszDgNsyUBhPnmwzZm7V7NSThnxTG6NlgpObHI9nv1-DL8MTPsvOYv6LVvoLFcaqfgp_a2SljTZsdOkWcUM49EwVrPSqJHfFAXudXpAUQVkwZrmQTXQAvLmstDRcrvhLe3PIPyZ9kiN1jv3repO0cjX4dLNsGgF5b_QFQQTxoKbw2WbUE-_5a6U1URsU7UzK09i7RDVzinRDJjwu8j4ctVe3isHY6rmxAct5Vs2hSJ010plBeNQk2qOgdRVXuy5sRgDsOJXzjUQxRFFtV0Oe6wSKfzdTGvPyvdl11C_i5WfgHLDihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
آتزوری در برابر ترکیه؛ نبردِ کنترل و غافلگیری!
🔥
⚡️
[
ترکیه
🇹🇷
🆚
🇮🇹
ایتالیا
]
⚽️
تقابل دو سبک متفاوت؛ ترکیه با بازی مستقیم و انتقال‌های سریع می‌تواند دردسرساز شود، اما ایتالیا در کنترل توپ و سازماندهی دفاعی دست بالاتر را دارد. باتوجه به کیفیت دو خط دفاع، نیمه اول می‌تواند محتاطانه و کم‌گل دنبال شود و جزئیات کوچک روی نتیجه اثر بگذارد.
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
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/140645" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140644">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
#رسمی؛ صابری عضو هیئت ‌مدیره پرسپولیس شد
⚪️
⚪️
با استعفای اردوبادی، حسین صابری به‌عنوان عضو جدید هیئت مدیره پرسپولیس معرفی شد. سمت دقیق اعضای هیئت ‌مدیره در جلسه آینده مشخص و بعد از نهایی شدن در کدال اعلام می‌شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/140644" target="_blank">📅 16:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140643">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
مدیران پرسپولیس آماده ارائه پیشنهاد تمدید قرارداد ۴ ساله به اوستون اورونوف هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/140643" target="_blank">📅 16:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140642">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
❌
فوری؛ بیژن مرتضوی که چند ماه پیش در فینال جام جهانی برنامه اجرا کرد، پس از چند دهه حضور در امریکا دقایقی پیش وارد ایران شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/140642" target="_blank">📅 15:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140641">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
بیفوما با ساخت ۱۲ موقعیت گل، یکی از خلاق‌ترین بازیکنای این فصل لیگ بوده
🔥
🔴
اگه نصف موقعیت‌هایی که ساخته تبدیل به گل می‌شد، با اختلاف بهترین پاسور لیگ بود!   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/140641" target="_blank">📅 15:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140640">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/140640" target="_blank">📅 15:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140639">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
💢
💢
✔️
✔️
مدیران باشگاه پرسپولیس هفته گذشته‌ مذاکرات برای تمدید قرارداد پنج ستاره آغاز کردند
❌
پیام نیازمند
❌
محمدحسین کنعانی زادگان
❌
تیوی بیفوما
❌
اوستن اورنوف
❌
ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/140639" target="_blank">📅 13:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140638">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
جلالی دوباره مصدوم شد
‼️
🔹
ابوالفضل جلالی در جریان تمرینات اخیر پرسپولیس بار دیگر دچار مصدومیت شد. البته شنیده می‌شود مصدومیت جلالی جدی نیست و بیشتر به گرفتگی عضلانی شباهت دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/140638" target="_blank">📅 13:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140637">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/140637" target="_blank">📅 11:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140636">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
اجرای بیژن مرتضوی در کنار ارکستر فیلارمونیک بین نیمه بازی فینال جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/140636" target="_blank">📅 11:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140635">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccc2b8cd01.mp4?token=rbn8DFC3I8Wc2bEExnpsdJeh3sRzY6NSxIXlUusfk8zLLADzwB593twFu8rT8R5xbG6ncULJAR5XyJXTNEx7hB8h3XT6BsXfqOd4_IStn4Mx_fzAuDiRvU1kzFLXRH8AUXy-0fyxnDFhF-jXwmbzdfPBaTr0kr8jrsUNEM57GMJSR8kbVRPveYasbf-u7xs7S7mPq0-wFyniMOOy1yz4yPUhEeCSvSRpmw5aS2046_W9tw_iw5T2jYlcvheLNiivGQdZZ71X0kPzc6-JsnDh-yGQptz5v3qYMk2wPPK-o7DStTXP9HKQzZLO38mSQ1Wk76W0GyXdwi38DG4D7THWxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccc2b8cd01.mp4?token=rbn8DFC3I8Wc2bEExnpsdJeh3sRzY6NSxIXlUusfk8zLLADzwB593twFu8rT8R5xbG6ncULJAR5XyJXTNEx7hB8h3XT6BsXfqOd4_IStn4Mx_fzAuDiRvU1kzFLXRH8AUXy-0fyxnDFhF-jXwmbzdfPBaTr0kr8jrsUNEM57GMJSR8kbVRPveYasbf-u7xs7S7mPq0-wFyniMOOy1yz4yPUhEeCSvSRpmw5aS2046_W9tw_iw5T2jYlcvheLNiivGQdZZ71X0kPzc6-JsnDh-yGQptz5v3qYMk2wPPK-o7DStTXP9HKQzZLO38mSQ1Wk76W0GyXdwi38DG4D7THWxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دلداری خیابانی به بیرانوند قبل خدمت رفتن
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/140635" target="_blank">📅 11:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140634">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
فوری؛ باشگاه پرسپولیس درخواست مدیر برنامه‌های یاسر آسانی از پرسپولیس، پس از فسخ قرارداد با استقلال را هم به مدارک خود اضافه کرده و خیلی امید دارد که سندی بر فسخ قرارداد آسانی باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/140634" target="_blank">📅 11:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140633">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
رسمی:با استعفای حسین عبدی موافقت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/140633" target="_blank">📅 11:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140632">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/140632" target="_blank">📅 09:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140631">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
فوری؛ باشگاه پرسپولیس درخواست مدیر برنامه‌های یاسر آسانی از پرسپولیس، پس از فسخ قرارداد با استقلال را هم به مدارک خود اضافه کرده و خیلی امید دارد که سندی بر فسخ قرارداد آسانی باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/140631" target="_blank">📅 09:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140630">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
❌
مدرک جدید پرسپولیس در پرونده آسانی، پیشنهاد رسمی اینجنت او به پرسپولیس بود.
❌
❌
بعد فسخ، این پیشنهاد ارائه شد با این مضمون که او با استقلال فسخ کرده و پرسپولیس می‌تواند برای جذبش اقدام کند.
❌
❌
مدرک از این معتبرتر ؟ / اگر باشگاه پرسپولیس با رقم عجیب و غریب…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/140630" target="_blank">📅 09:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140629">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✖️
✖️
#فوروووووی
✅
سپاهان به جمع مشتری های ایرانی بشار رسن در نیم فصل اضافه شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/140629" target="_blank">📅 09:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140628">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HssPXGgbwr2BBx0pMrpMpFWrrHVL2mj-6DNJ213gtTAR7opT6GSauz_yCn8YKaN05-injx5AqqKynkN1xnGaYhZ-xS_IPnW0P1K9vbvzBG0SeZhKaSRwGl1GcLcuMAhvazyNu7J9EX1CQBguemjlj-n1wP8tsrD_zzK0IxsNB6vVX7eTXiccPMHRmBm0-scUjLO5r7-AEj8_iVkmmQ8Stnb1pIKKMyI1apnyiNCbN3UeJUX_8SaThCW7NQnZD-BPHRxvUHQCHeWtXG2HUueEx1oPwFzBKgLIR0s3wFjiOVUIvw53TlhX-IJhmS5Bw6UGjB1z822ESYGGDQVwAYfRLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/140628" target="_blank">📅 08:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140627">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pk_qSSUfhbWZ-docbf-Ir2NDBoQ0h1u2i9mMrGG2qk4KnVntfkfHaPRd_nvZye94fPQo4WAoWa3q_CR3AJ9MnljDxFmERt0hNcCbwk52IfhQuaEgiuUMrpCnE9fiO5aKezu4utSEv2Fdnz-U-Wgv1hs-fNuOyiZQqEb3tyAdGddwAhAaS1y5wPvZ11gpE_JN0_YYmAAYsAhh_aokGzYl1ZPuECowZdy8MBw6iRU0HhW3Dai2Jihn2jFbzWlOAAPwUoSVRyttpx2RbbK2FIv_-4l7xQD_ycPU0Yh4Jyt-9O9JMc9A6VbqiFLYb8C6mo_GMpDxEHh-WX5lYaIoqebLwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد جذاب خروس‌ها و شیاطین‌سرخ؛ جایی برای اشتباه نیست!
⚡️
[
بلژیک
🇧🇪
🆚
🇫🇷
فرانسه
]
⚽️
فرانسه در ۵ تقابل اخیر مقابل بلژیک شکست نخورده و هر دو تیم هم شروع خوبی در این دوره داشته‌اند؛ بلژیک ایتالیا را ۲-۰ برد و فرانسه ترکیه را ۱-۰ شکست داد. بازی در بروکسل است و بلژیک با فشار تماشاگران احتمالاً شروع تهاجمی‌تری خواهد داشت، اما فرانسه در انتقال سریع بسیار خطرناک است. با توجه به ۵ برد متوالی فرانسه در تقابل‌های اخیر، سناریوی بازی نزدیک و کم‌گل محتمل‌تر به نظر می‌رسد.
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
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140627" target="_blank">📅 01:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140626">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/den-tTNIuMhdwvtyVNlL7RwM6SmajUTOVAT4L2vSUKbYnDWNuhO3ApLd5fwi2vG_NjqHcLWjKVYIGEyGs26hD2nMHcqgqAHqzuj55RZzj_4Li0I7gH82IsVrjkDwoDKsKcur7bRY_W8zY1_ZkJ97MfXXYeaeJwnJFLxlRDAG4vPgiIY_XWyN18lixflWxfMQBSdxUJHOlxQe1StW1SYky8atSWinwpV-Oba0yezIX81r-sG5zGWnUmZCmwo6gBS6i0kW-pM_oUO_GPXZ3sGWj30zgTp2kzfLruGonVgbQGIJhDqfEPng6QoLupT_tG5-TGBF7-N2BcG7WI6jmep3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️
🔴
با دستور پیمان حدادی، شورای هواداری تشکیل شد تا صدای هوادارا رو به باشگاه برسونه و پیگیر خواسته‌هاشون باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140626" target="_blank">📅 23:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140625">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRqTQ-QxGMCnO0zVu4HK274ZQnea-8RGX8ouZQv9E96B9qW4kSAwn2RVpznyjKqroRxtOhSutbsYVLRFBdovGkypeYgpjRhuNGvsi2xR6twAgIjoO-2U2x01YXt9oQZB41nYh31ou2FXuCs7jqmc7ksnIJn4zCAp3wNWBZvm_SP8021-WJ4DFPsRNOe2kGcUJ1TIXRX7a2hzpsDJRZL3PMSbz16eAxGoRqL_R1A1l4yrUgTMyC-LoZvqopxjBnr90g0LLMW5vlMCve5WSVnEaRL5JXvja-z8lKENOoS4BrKgiMJ8C8Z-6KeGxfhkmhPvi2LLcGsMdPP-k1BmQw3AmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☑️
آقای فکت رسانه‌ای شما خواهشا از آسیا و سهمیه صحبت نکن که خودت با اون باخت ۷تا مقابل الوصل به اندازه کافی آبرو ریزی کردی بعدشم از سهمیه ای صحبت میکنی که بهتون هبه شده مثل پنالتی های معیشتی‌تون
❌
❌
شمایی که باشگاهت که با وجود ۶-۷ تا خوردن تو آسیا حرف از تخصص می‌زنین ، هنوز ۷-۸ هفته مونده به پایان لیگ خودتون قهرمان میدونین و دارین گدایی میکنین، جام ندیده های بدبخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140625" target="_blank">📅 23:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140624">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
❌
❌
❌
❌
❌
❌
❌
🚨
اورونوف در تعطیلات موفق شده ریکاوری خوبی رو پشت سر بگذاره و از نظر روحی و بدنی دیروز  آماده نشون داده
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140624" target="_blank">📅 23:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140623">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140623" target="_blank">📅 23:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140622">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfce03f041.mp4?token=Iuu29px1KUyVZl2mZBAHn4IAwYYAeqVer1x1AkUpmzRLVSpF2IgYaVPHgVkbY8O-F0UrO_nSQ2LaC7A6CbVH-74LkZryy8w8sIaKdhtguD-fhzCo2E9_rQAbYLztg_ZhHSGBg9kUTD_B3YXCGm-lQPTUjRXV4KqVh9C-TfCeAZ7GHx--xo_v-th923wu7iT9xYhyrt5IiMMhwvksWBtgawezk-Iwpdryz9FNPQk5m4FFunzBxiMnfgJiep4ENShqpQilSmoZGxHZLuiJVV6vvav4fDnh9BKEhKk1Osk-7eciyKCPC71nwWGAfVl3140ZvbPEdpL_m5NwyOVcLnepkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfce03f041.mp4?token=Iuu29px1KUyVZl2mZBAHn4IAwYYAeqVer1x1AkUpmzRLVSpF2IgYaVPHgVkbY8O-F0UrO_nSQ2LaC7A6CbVH-74LkZryy8w8sIaKdhtguD-fhzCo2E9_rQAbYLztg_ZhHSGBg9kUTD_B3YXCGm-lQPTUjRXV4KqVh9C-TfCeAZ7GHx--xo_v-th923wu7iT9xYhyrt5IiMMhwvksWBtgawezk-Iwpdryz9FNPQk5m4FFunzBxiMnfgJiep4ENShqpQilSmoZGxHZLuiJVV6vvav4fDnh9BKEhKk1Osk-7eciyKCPC71nwWGAfVl3140ZvbPEdpL_m5NwyOVcLnepkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
مدل موی عجیب و غریب یک بازیکن در کونکاکاف
▶️
#ویدیو
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140622" target="_blank">📅 22:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140621">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm6t2IwoEMuCCNpn99apxeL6zj9-_hwjs7eDRh4Rbzo4zWD7_girtdw-O6EFn8eqTZ21a7PpdzDPKh_9u-EGSglAXr6Ai9roqgUojGmCPcfkSAhDS1cSK6Mm0gnAGw6CC7IxAo072zpSUsxamViaqrBLDYrnNGdnSxAoD3tM2fkEclSB8R2n-fLRurJVj768kbPTb6WNB3UL6mglGVP3xN1bKW-8HA1L9Y112DL9qX-PxLCjJc3tNim4T69pcyOTfcSru2yAEmaSm1Q5rVavRPOOygrpqsM50Ks4-yNxmoTG4CMR9nrjfoSQDGkI6j_cUU5Vi4jEFcby6JKWGs-MfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#
یادآوری
❌
وقتی قهرمانی پرسپولیس در کرونا درمیان بود‌، منطقِ اعتراض‌شون ٣٠ امتیاز باقی مونده و احتمالِ امتیاز از دست دادن پرسپولیس بود
🚨
حالا که پای قهرمانی خودشون درمیانه، ٢۴ امتیاز باقی‌مونده و احتمال امتیاز از دست دادن خوشون رو ندید میگیرن گدایی جام دارن‌. چرا آنقدر بی‌حیایید‌
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140621" target="_blank">📅 21:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140620">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
تیوی بیفوما:
✅
• سرعتم روی گل به ملوان ۳۷ کیلومتر بود/ سال گذشته اتحاد تیمی نبود و شرایط خوبی نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140620" target="_blank">📅 21:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140619">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⭕️
⭕️
ابوالفضل رزاق پور مدافع چپ تیم فولاد: از پرسپولیس آفر دریافت‌کرده‌ام‌اگه دو باشگاه به توافق کامل برسن درنیم‌فصل راهی این باشگاه خواهم شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140619" target="_blank">📅 21:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140618">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
🚨
هفت ورزشی؛  به استقلال خیانت شد؛ برگ برنده پرونده آسانی به دست پرسپولیس رسید!
🖍
ایجنتی که به باشگاه استقلال رفت و آمد دارد، مدرکی به دست باشگاه پرسپولیس رسانده که برگ برنده این باشگاه در ماجرای شکایت از یاسر آسانی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140618" target="_blank">📅 20:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140617">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsTQ90jDZxqgpOQprJkaiGkVfrQC00jT1OupA2adarUHmtdMObs_Pdy3aosURp3kQvQ-QshT4OmVK_aCZXgoqQIYRW5Tnl0sLJf9beM1uyITioG6TGEHiBHokedbPbygqbBNoy5mvbExT7jrfu2ZiGpTrpoUfT-zn4aiH8QpUxu4WeE2USXJp5_cHD9bC-wb_JBcuZimiFrhm_sRApaN6SqChXhR91Jk2q-BqZWebZyRA2Kkl2-BQUvQr2BNzxuMuvzkz3z7l5MchfVHUfm9e1EzXSdiK0mjjDiRDnD34VigVPqX-8SAfgEgAZEx_eIxJrvxmxfaXY8sFP_GYjsWQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد ستاره‌ها؛ شبی برای تماشای فوتبال در بالاترین سطح
⚡️
[
نروژ
🇳🇴
🆚
🇵🇹
پرتغال
]
⚽️
نروژ با تکیه بر قدرت هجومی و انتقال‌های سریع، می‌تواند بازی را به دوئلی فیزیکی و پرموقعیت تبدیل کند. پرتغال با مالکیت بیشتر و کیفیت بالاتر در یک‌سوم هجومی، به‌دنبال کنترل ریتم و استفاده از فضاهای پشت خط دفاع خواهد بود.
سناریوی محتمل: گلزنی هردو تیم بسیار بالا می‌باشد.
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
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140617" target="_blank">📅 20:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140616">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⭕️
⭕️
⭕️
دنیل گرا مدافع راست خارجی پرسپولیس به تهران بازگشته و اماده حضور در تمرینات گروهیه/قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140616" target="_blank">📅 19:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140615">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
بالاخره انتظارها به سر رسید و دنیل گرا پس از پایان مصدومیت، طی یک یا دو روز آینده به تمرینات گروهی تیم پرسپولیس اضافه خواهد شد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140615" target="_blank">📅 18:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140614">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
زنوزی علیه کیسه
❌
زنوزی: کیسه خیلی جام دوس داره بیان من پولش رو بدم  برن منیریه برای خودشون جام بخرن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140614" target="_blank">📅 18:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140613">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⭕️
⭕️
فارس: آرای هیأت رئیسه فدراسیون به قهرمانی استقلال ۷ رأی مخالف و ۴ رأی موافق داشته و به این ترتیب احتمالأ جام به این تیم اهدا نمیشه :)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140613" target="_blank">📅 18:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140612">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
فدراسیون به باشگاه گفته که مدرکتون برای یاسر آسانی کمه و اون مدرک اصلی و قوی که ما میخایم رو ندارید شما ، حالا باشگاه از طریق یکی از ایجنت های ایرانی یاسر آسانی یه مدرک فوق العاده قوی رو کرده که فسخ رسمی این بازیکن با استقلال رو نشون میده و فدراسیون هم…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140612" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140611">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140611" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140610">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏅
تأکید مخالفت باشگاه تراکتور به اعلام نام استقلال به عنوان قهرمان فصل گذشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140610" target="_blank">📅 18:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140609">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijw2I9uOmRHBFLvo_RnLypuDDgosbfiJOsqaDN8FI4soVrhmr9gHwVVqjJsqWVdPR1Bf385lQEObqG7r1aqmBCsqjT-KYcM88qnzf8jw9EVOGM-tyuuvVS5S7F_RfGaOLLbnxed_hPlQTSm8FTxg267bqBMDnbqeMMN6wutclHTne6EqEOll0aFS2pnaAkbBhlyxC0BdA_VNhVXD8m1lTBapeKd6_MPcicb8afEsE4LmrI7UlHxRhJFfj1XkPtJAv1wB19Cj9t35E9UbS9O8LQba4OnfoLmUoMp-gjiKFIAu6URYEoDpatcRkO7ieKZpLJams-qBSS9vaUlXpi3eKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
تأکید مخالفت باشگاه تراکتور به اعلام نام استقلال به عنوان قهرمان فصل گذشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140609" target="_blank">📅 16:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140608">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
❌
علیرضا بیرانوند سربازه و معافیت نخورده و هر بازی که انجام بده غیر مجاز هستش / مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140608" target="_blank">📅 16:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140607">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic1dpA8kentTRjZiUwmwYymr6ToivW3OzsmOHMuitKiPt5yKcjXsMGu8-OTpUrjzDyZY0GeFa43nrzuXLeKTGGl8-G_5wcuoLl36ljho_j1TqtCGi1GW1fLmKqIqk3C_vOnB3IaHdN2PUmBtw_fVDJ5FFOT07XLbbxbDFCdDbR2hr2yORilDkVbF6ASaS-begnD9BOFkTjFDbL_xJFQ9MWGw7yXG_2MNWVNoLf0yjH4LO66RrWeSCPEk49epA045xoBoluu7l72wldZsBGLhEeaUoTUxAa1ds6LYW5bwjIwLJbivNJpG9WDTCVa2DCcH7AKOvhdt_4q7sGtbgUO3jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Norway -
🇵🇹
Portugal
⏰
Tonight 22:15
🏟
Ullevaal Stadion
🇪🇺
نبردی بین فوتبال مستقیم و مالکیت هوشمند؛ جایی که هر اشتباه می‌تواند معادله بازی را عوض کند. پرتغال با تکنیک و کیفیت در یک‌سوم هجومی خطرناک‌تر است، اما نروژ روی انتقال سریع و قدرت خط حمله می‌تواند ضربه بزند. انتظار می‌رود بازی با ریتم بالا دنبال شود و جزئیات در محوطه جریمه، تعیین‌کننده برنده باشد.
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
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140607" target="_blank">📅 16:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140606">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
سازمان لیگ مجددا کارت بازی علیرضا بیرانوند را به مدت یک ماه تا پایان مهر برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان می تواند  در بازی هفته هشتم با استقلال تیمش را  همراهی کند.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140606" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140605">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
باشگاه پرسپولیس با برگزاری رقابت‌های جام حذفی در تعطیلات جام ملت‌ها و بدون حضور ملی پوشان موافقت کرد/ورزش‌سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140605" target="_blank">📅 15:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140604">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
باشگاه پرسپولیس با برگزاری رقابت‌های جام حذفی در تعطیلات جام ملت‌ها و بدون حضور ملی پوشان موافقت کرد/ورزش‌سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140604" target="_blank">📅 15:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140603">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
❌
فووووووووری از ورزش سه
🚨
اولین خرید پرسپولیس در نیم فصل مهدی حسینی مدافع‌ وسط ۱۹ ساله شمس آذر خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140603" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140602">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🤝
🤝
مدیربرنامه‌های فرهان جعفری: فرهان اوایل دی‌ سربازی‌‌اش به‌پایان‌ میرسه و میخوایم توافقی که هم منافع او حفظ شود هم منافع باشگاه خوب ملوان حفظ شود از این تیم جدا شیم.
❌
❌
فرهان از دو باشگاه پرسپولیس و استقلال آفر دریافت کرده و در پنجره نیم فصل راهی یکی از…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140602" target="_blank">📅 15:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140601">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
طبق شنیده ها
❌
ابوالفضل جلالی مجدد دچار مصدومیت شده و بزودی مدت زمان دوری او از میادین مشخص خواهد شد
😰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140601" target="_blank">📅 11:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140600">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⚡️
⚡️
⚡️
رضا شکاری مجوز بازی نداره و صرفاً در لیست بازی قرار داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140600" target="_blank">📅 11:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140599">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
امسال جام حذفی برگزار نمیشه و تیم های اول تا چهارم سهمیه آسیا خواهند گرفت!///فوتبالی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140599" target="_blank">📅 09:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140598">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⚡️
⚡️
⚡️
رهایی کاپیتان سابق پرسپولیس از بیماری سرطان
⚡️
⚡️
سید محمد پنجعلی کاپیتان سال‌های دور پرسپولیس، مدتی را به دلیل درگیری با بیماری سرطان زیر نظر پزشکان بود.
⚡️
⚡️
خوشبختانه شماره ۵ پیشین سرخپوشان موفق به شکست بیماری سرطان شده است
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140598" target="_blank">📅 09:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140597">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">😰
محمد احمدزاده، سرمربی اسبق ملوان: یه مقام استقلال‌ به من زنگ زد و رشوه ۵۰ میلیونی به من دادن که به استقلال امتیاز بدم تا پرسپولیس قهرمان نشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140597" target="_blank">📅 09:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140596">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
✅
✅
مذاکرات پرسپولیس با بشار رسن در حد واسطه‌ها در جریان بوده و هنوز به مرحله مستقیم نرسیده است. / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140596" target="_blank">📅 09:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140595">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
✔️
بازگشت اورونوف به تمرینات پرسپولیس
✔️
با اعلام باشگاه پرسپولیس، اوستون اورونوف به تمرینات این تیم بازگشت. این وینگر ازبکستانی در فیفادی به اردوی تیم ملی کشورش دعوت نشد و کاناوارو ترجیح داد روی نام او قلم قرمز بکشد.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140595" target="_blank">📅 09:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140594">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMwVsFC_c3IsXHH_QHnIoAzz4i70RIQyZqVEorvZZ_HhJ8eAftxTFrdlL2hpgC8GOCYfKwbCZPsze0mblNDC0tjKDCmPkAjMby62xBZKcqdZJgIWKlNnec6Z4TXEwdQKQh_K2tvfGwbO0czJOQEZ6-yHtCX8V6CBGkMjE1ezd6auS_zSAztpnLtZuT9viv5uB11KhzrLl1VSHl0VmzF1IYF11IBK48he16DIYEzEpBx1klk0mx4XrcEgXR0LiKnDf7Mi5D4vtwDTAvzRb5GplMNlXkpVJBlNOPe0852ScjgKXoJsq_5ZkNmmwF1SYfDN2oAp_Hg2G_yHvaxPiT1Tcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140594" target="_blank">📅 09:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140593">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZnpVgELoCs3UZh_JWi9E-9xAMnpvgfK0kss8g2BmIeLMoOmU0b0XMOmLTe1hwEPdmsBjiRQdspU0MkKEt5x2-vTeCpo5IIVJ43b7rk2xjoThE5EfD3-s_wevycWuNAG6xy6xmb8QLZs4mpx28FO3SLQu6rgVRbe116X6PthREYF54ZvqQxbM3j0CSnvHXAzh296JDIBajcNU8dUNNBZ9kMr5zNWyp36BuS_a-sc6W3g4CEvdFoz9-BbycM_DRALNa7JtTOfPuDqLg9cZnJLu9u9OFQrg0C_KNA3KyD9Zd-03pVZQW6YlTTOI_yzSN3zZmBIxY-mo9rMTn83Fh3T7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140593" target="_blank">📅 02:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140592">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
✅
✅
فشار شدید امریکا علیه ایران
✔️
✔️
امارات، ترکمنستان و تاجیکستان ۳ کشور جدیدی هستند که حریم هوایی خودشون رو به روی هواپیماهای ایرانی تحریم کردند !
❌
مکزیک برزیل و بقیه کشور ها هم رسما تحریم کردند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140592" target="_blank">📅 00:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140591">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/140591" target="_blank">📅 00:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140590">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/140590" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140589">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/140589" target="_blank">📅 23:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140588">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
تاجرنیا: از سازمان لیگ تقاضا دارم قهرمان فصل قبل لیگ برتر را اعلام کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140588" target="_blank">📅 23:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140587">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
🔴
فارس:
⬇
بودجه پرسپولیس در فصل جاری ۳ هزار میلیارده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140587" target="_blank">📅 22:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140586">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
✔️
بازگشت اورونوف به تمرینات پرسپولیس
✔️
با اعلام باشگاه پرسپولیس، اوستون اورونوف به تمرینات این تیم بازگشت. این وینگر ازبکستانی در فیفادی به اردوی تیم ملی کشورش دعوت نشد و کاناوارو ترجیح داد روی نام او قلم قرمز بکشد.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140586" target="_blank">📅 22:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140585">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/140585" target="_blank">📅 21:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140584">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
‼️
🔴
ادعای جنجالی کریمی: خودسرانه برای بیرانوند دفترچه پست کردند؛ در تلاش‌ برای معافیت پزشکی او هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140584" target="_blank">📅 21:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140583">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UswdoZj0PnsCfV745RTZyVbY5LVwZq7E_3RenJAv7nd9udVUg7iFoqIyb_JGnbZNtrOHcGLJgnX8eTwj3uIAi3sOpBHZOjQtSJAfA0aVFy36YCdfvCbxtbv987FoaZkqCJujjDV3eC0_AQWH7ii5-RrMBk8q8Vw5KL_edp07gdgYVgSW7zB2FK5x17gJjtcJNvKGeZCyX_Z39UV3Z96YnDT0BifJK_xPF75m7NZpve5DrN7FtsW2qDzo5-Ot-HteRz566votm8bP0cCBntHRVl4cN08On2JHQxNnHirRJfkyGRilhT9U9qstFWYytUzRnt8YbRh2lsjJiNvvJ5TnBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
❌
افشاگری فنونی‌زاده از قلعه‌نوعی‌‌:
‼️
من با سند‌ و مدرک به شما می‌گویم ۱۷ تا مربی در عرصه‌های مختلف ملی و باشگاهی که سابقه استقلالی دارند، توسط قلعه‌نویی به‌صورت مستقیم یا غیرمستقیم روی نیمکت تیم‌های مختلف ملی و باشگاهی نشسته‌اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140583" target="_blank">📅 21:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140582">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140582" target="_blank">📅 21:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140581">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140581" target="_blank">📅 21:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140580">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzMt5ahlX5Nm_hov9tAfU6-JaM09KLqzHbsvwCi_P50djAZ2x3F5eQtzQG0WmGXJW5OiGrfxJIXjtNnNPRwBUb20xtXE7vIFuAFLWKKDjWTe_yN7xMABVMyFv4qiPNUFyKqDKkW_P__VqYWJQRwp2GpESnU2p5ULvXBmM-EfzpMPAHTJgA13qJgNhadOGgz-d5Vya6RYnjzUeNtkpCZ5GBN6QcxHb8ij2BbQmhgYLP0fShXswBwDZ1TrIJJ_HWyrAYelWcU2fiBLAmlWz1or8LKBCj_vixmmr4pSXk7JEP-PsRLfmoDR7W0oOc5-lYqOjn5izxu9PL5FeCCkbPqlww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140580" target="_blank">📅 20:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140579">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140579" target="_blank">📅 19:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140578">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
🎤
بخش اول صحبت های حامد کاویانپور مدیرفنی آکادمی پرسپولیس بعد از دیدار با امید سایپا
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/140578" target="_blank">📅 19:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140577">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⭕️
قسمت جالب سربازی بیرانوند اینه که همین آقا دو ماه پیش علیه علی دایی استوری گذاشته بود: «من هیچ‌وقت از رانت استفاده نکردم»
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140577" target="_blank">📅 19:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140576">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/140576" target="_blank">📅 17:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140575">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
سازمان لیگ مجددا کارت بازی علیرضا بیرانوند رو به مدت یک ماه تا پایان مهر ماه برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان میتونه که در بازی هفته هشتم با استقلال تیمش رو همراهی کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/140575" target="_blank">📅 17:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140574">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/140574" target="_blank">📅 17:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140573">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
اوستون اورونوف و مارکو باکیچ هم اکنون در ترکیه حضور دارند و اگه مشکل پروازشون حل شه تا شب به تهران میرسند    «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140573" target="_blank">📅 17:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140572">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoVqQrlZoITDDDTbgKsnzYftMF7j_AaBEpWcLjvXfaumm0gGbUKBAQu4z_6pdbwReGxt2RTCMEadvUKmLX2_pQrhOBEezXGV9Xx9MAAiEuiWBDQAoYO1hngMWkxnCVHjeuFdFjJemY9KIzktelJvh_zAnt570giwPBvZWR8C3lj2dispyzVSv5i_88zT-UnrI8o7rKwS4BQQbWCettPq5N57uFMqvbA5KcZYChqOCT6Ie5qMSECUBbu6mNfapQmZ8OLyGy-ChE-T_fsQ6lI9Y_PL7-rWBlS8RSdUCpkGwksrESzjL2jXa6dajsiNz4TPttORgENjuvKpBZCP7y10Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140572" target="_blank">📅 16:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140571">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🔴
فوری؛ معافیت علیرضا بیرانوند از اعزام به خدمت سربازی، ۱ ماه دیگر تمدید شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140571" target="_blank">📅 16:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140570">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARHPHhdV2UXb_mp55YBzTwY2ZO1csNfFP_LnuxcDucQCvAarGjWciAR20KjL5ecjNPR2IActS-C5XW6fB1sC3ecsAPtYcsuuFNie9RZpC2DUlzzyFaxrUq7zgKY3KjzjG2_fffaLJEezWFX07WvPkO953IUPtcFRrnlAmls6XGKAS7VR3Lmvqtipbrvosx3hOizydeztjkVk9r25diTewOAhQgH_eaYazssOO_EFWhdU8iuB5mcZFh6hNq0N1u9LqASDttUyTc_ZqBLq9YA_YjjSA0TaZ1CPmbws8QIqaYanq1dh8X6ytKeUp4yxl4QoXhF7UKg8hqawo8wSoXU_XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از بدنسازی امروز پرسپولیس؛ شاگردان تارتار فردا استراحت خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140570" target="_blank">📅 16:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140569">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=MynVpyG27W8se00Toqr_bXB3rxKOnW0YVghDzzHYFpkETEPSQ05nBHtY7wPRqahFYm1HmxZwdYVB3hHU9PYzNNftZKzYXthhxKZpm_nrH7TWWb_BLjwkXlpwM-w8waZuN1TAa69e-WM3hCoH77aV9GU_zQw-ZF7vuN5JfztHSME7GhMwwYxljyUaGN2abH3jEMwzM2VpAceTUihkRemWDIhiWL5YhW9bzNQLzlUQ9uU9u0RmrOybo5cwY5jyHKnpszifulVX5vbSrpGDFjbwJKOpjHKz0T1iLfZsDCavtLYiZ-pPgKKeL2lMu4dWlxKKXByMJ4Gfbo2spCsxVOYdVatN7Yiji2bUg1ynU6-7kJHrRY-o9v99_es623eDk3EVqVsmJ_wUEADmRl4UuSS9b8OywcTfKgt6V-6SyiKz6OqyRFjp6ynyo75gulZ-DelQIPc4bA6-kyqppg3cIcpNf2cIKHgYAdvh4SgDKK8kxap4moED8pQZvc4_P-uhXllwhdJ7C59Rp2MajYtAXE1gj9Phtq2fcSxEiKr_mpf93BGFdlTukZc3UXCa4942LiTyikamQu_NPwZWm5R-2RQzL74QdgJGAa4-7G9E0yc2HwVVanBfx671B95xEVDjzaTns1esUj7G7QJVu7KShrjdQm20Wr4cIwJOFMDKYgo1SnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=MynVpyG27W8se00Toqr_bXB3rxKOnW0YVghDzzHYFpkETEPSQ05nBHtY7wPRqahFYm1HmxZwdYVB3hHU9PYzNNftZKzYXthhxKZpm_nrH7TWWb_BLjwkXlpwM-w8waZuN1TAa69e-WM3hCoH77aV9GU_zQw-ZF7vuN5JfztHSME7GhMwwYxljyUaGN2abH3jEMwzM2VpAceTUihkRemWDIhiWL5YhW9bzNQLzlUQ9uU9u0RmrOybo5cwY5jyHKnpszifulVX5vbSrpGDFjbwJKOpjHKz0T1iLfZsDCavtLYiZ-pPgKKeL2lMu4dWlxKKXByMJ4Gfbo2spCsxVOYdVatN7Yiji2bUg1ynU6-7kJHrRY-o9v99_es623eDk3EVqVsmJ_wUEADmRl4UuSS9b8OywcTfKgt6V-6SyiKz6OqyRFjp6ynyo75gulZ-DelQIPc4bA6-kyqppg3cIcpNf2cIKHgYAdvh4SgDKK8kxap4moED8pQZvc4_P-uhXllwhdJ7C59Rp2MajYtAXE1gj9Phtq2fcSxEiKr_mpf93BGFdlTukZc3UXCa4942LiTyikamQu_NPwZWm5R-2RQzL74QdgJGAa4-7G9E0yc2HwVVanBfx671B95xEVDjzaTns1esUj7G7QJVu7KShrjdQm20Wr4cIwJOFMDKYgo1SnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
ادعای جنجالی کریمی: خودسرانه برای بیرانوند دفترچه پست کردند؛ در تلاش‌ برای معافیت پزشکی او هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140569" target="_blank">📅 16:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140568">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🔴
فوری؛
معافیت علیرضا بیرانوند از اعزام به خدمت سربازی، ۱ ماه دیگر تمدید شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140568" target="_blank">📅 15:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140567">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faac5ebeb7.mp4?token=WMNNQAkBonrwZbZo6LHhzf7frXB1EBs9p_TuzRetO7BGBSrLR1mUqL346ZEV98aywk8jCAJK3aX9IyGWItRwHVNnIO5YLgEcjuex9nqXqIH4o4mVggFIGGVE9X7W45E5AzTf9__Y07kP6kMsXZDplDFc8GrxykLjCGX8tEVR_XMr7zy8Ynkqa1gcLQ5mwY3A4QviMt68Mb8sqEccqDzwqhZvDjhrSKIz_k9ABQGY8Dq8ZuAsB8mN_Y3WYexaDPmmKLpc-8OBFtwP08ziDAoxVEWdZ1G_xIBud9wyrjxs6Jvou5xLzdihlEipLkc6rrv7tka8QNW0mnhiPGr-fY0XlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faac5ebeb7.mp4?token=WMNNQAkBonrwZbZo6LHhzf7frXB1EBs9p_TuzRetO7BGBSrLR1mUqL346ZEV98aywk8jCAJK3aX9IyGWItRwHVNnIO5YLgEcjuex9nqXqIH4o4mVggFIGGVE9X7W45E5AzTf9__Y07kP6kMsXZDplDFc8GrxykLjCGX8tEVR_XMr7zy8Ynkqa1gcLQ5mwY3A4QviMt68Mb8sqEccqDzwqhZvDjhrSKIz_k9ABQGY8Dq8ZuAsB8mN_Y3WYexaDPmmKLpc-8OBFtwP08ziDAoxVEWdZ1G_xIBud9wyrjxs6Jvou5xLzdihlEipLkc6rrv7tka8QNW0mnhiPGr-fY0XlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حضور پیمان حدادی مدیرعامل پرسپولیس در ورزشگاه درفشی‌فر برای تماشای دیدار امیدهای پرسپولیس و سایپا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140567" target="_blank">📅 15:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140560">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3qwxJALvQyUKDvZmhgbU8gc9Tnk3q3T2uQlZ8kiYQwGplYL-wwyXTgkZbu32MGGxQj2OA4XiIvM-XttJ-jx4HhAfBMX2Xojwt2tWcm9bAcwyxNh8m4fA1nUomms_cLzjfncJjmImRJnc2b1ooJU_maknF7EQ60dT33AawhaoLa9tFOsEcxqWqxyBoS6b8FRQtaVKRPYblpHLvx9z4blVbCDGw5p0ehYvchKBZ7uxYrhxGnNp9pj02e2O5MaguQFBBTcCUe-jEMRGW09cImlPfRRREXH1aJt9FKqVy26HSmiaBzMNIK9kMXFPT2WFQz0GANK41w7wpq-GJaKEUhi8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140560" target="_blank">📅 14:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140559">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JW6nrAQd4bsgxwfmY6YZvzcb1gZHsFvDEmwQi4NR2PMp49y0T6FDJL7Q6QjRL94mBvcIOpM37y8r8exC5dTq0J4GynftuFeZv-5MYUQbsRYlR4NsDyF4pj6lplZKwAaMEJpqyklCNgvHjj4oTUTO8l4jpbR3L56lK8YyFp6UI4D2XnqLGQXuHMNZ2kKc1KgWP9dpSL7Ta0vhzMbaIzZSfCyc2i_UndChhgpRqo6x6F6QqCoJLd-zMg00vB71m66TPoBL9cHt8JOR4ZwzaK75TetFgaTLGBqXFcMaP4Y6_pvw2_2gRroRAX8to66s-vohzScdQoVkn8nYib7xbEG35g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیم قلعه‌نویی واقعا عجیبه!
❌
بازیکنی که از جام جهانی خط میزنه رو کاپیتان میکنه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140559" target="_blank">📅 14:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140558">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⚡️
⚡️
تاج اعلام کرد امسال دیگه سقف بودجه وجود نداره، اما فیرپلی مالی اجرا می‌شه.
⚖️
طبق این قانون، باشگاه‌ها باید قرارداد بازیکنا و هزینه‌هاشون رو منتشر کنن و اگه این کار رو نکنن، سازمان لیگ خودش منتشرشون می‌کنه. همچنین باشگاه‌های زیان‌ده فصل بعد با محدودیت…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140558" target="_blank">📅 13:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140557">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
فوتبالی:
✔️
✔️
گفته می‌شود فدراسیون برای جانشینی عبدی با گزینه‌هایی مثل فرهاد مجیدی و مجتبی حسینی وارد مذاکره شده و باید دید در نهایت چه کسی هدایت تیم امید را برعهده می‌گیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140557" target="_blank">📅 13:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140556">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140556" target="_blank">📅 13:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140555">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
علیپور و کنعانی‌زادگان ابتدای هفته آینده تست پزشکی می‌دهند
✔️
نتایج این تست‌ها وضعیت بازگشت دو بازیکن به تمرینات را مشخص می‌کند‌ و پرسپولیس امیدوار است هر دو به دیدار ۱۷ مهر مقابل صنعت نفت آبادان برسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140555" target="_blank">📅 10:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140554">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140554" target="_blank">📅 10:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140553">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9S9zVwomYlZvDGih-5V2N3j1cXyXKS-OkjwNsEiHeoIK_LffZSbtiXoQFHdwjImPTV-iblrt4eTNk_WFb_RJqUtt5-_s2tPqxWvwpcTUGbOlUMFfZHMnLwArrxyVcPX2rquEvrdeQjGI1qKkIxQyyB3Nk5F4oS0fARtNxYon_8D9TXtazhmJB450D5ERvBT1Cg5yv4WGRA6CPnllIG_naVsp0BqV23ly_D8PbR41kd_YHVJtndZrcQL3K25TQtlZygQidi0yoZBWBGx3PrLcs1QkFgWV9kBU9Jsrq2zfGwYiIQklIdLGtRd48Uanq_lE0qYsRi_hbymfxdEN_hzIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
⚡️
باشگاه استقلال در پرونده فابیو کاریله که فقط اومد یه سلام کرد و رفت به پرداخت ۴۰۰ هزار دلار محکوم شده است.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140553" target="_blank">📅 10:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140552">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
❌
سه وکیل خارجی باشگاه بعد از دیدن مدارک جدید در پرونده آسانی اعلام کردن، درصد پیروزی پرسپولیس تو پرونده زیاده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140552" target="_blank">📅 09:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140551">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJUAJAZvWxhvNHfIKjwrAQMcCQIORNmddeKjoMW_vAA8vovXG8dtvMPcYzZ59UC_BZMYy7iQjmFMkx-_eScqct-Jxdv4mB0Xl3um1FY2UZoVmCE19xZ62Qv3nLXGJjVr2mz4Lha6CF2p0tTfRk7jwXjg-R70U9tkOHsc-of9tDkBC2qIfPhDRH4LI4z5s_o0YqRMAEXdBPlKAZBk3XEgp_5cvc94jkSUVxsSAxDbmMv04XYIa32fRE7kdPXOjli-CsepI3LvzIOR8J4GeLFjwhqE7gH4Gvy9wLgAh4Ycu2t1ntlzWkJx9IwFtPH_lWLXI7QRJQA2YkC5Sj2fCunqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140551" target="_blank">📅 09:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140550">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuZXQveQbdZwtM1d7S-VL5ToeKsnq-Ht1RdNWUEXqB-8GdIZijZ2ek7_eXLFwCMISNSYwANblBLvOR8NFxZbEEglzRGGWVvI3HQZpdauqZRkOfbfNSU19mIbuNOwlA2HRtAhjpo6Ve4n38XbiA9ViLWF-VQGnmeKRTZDz8ZDT7mB0UWgXkTq2fbVR-li14qVo_P4NsStlwJ269X92DL0mx3bkTe5HVfaogv29zxKHJXOAInGc5QSxDvQQm9q5ULpyRGTX3dKfclD_K-CL99JywIpM3rOc0anBVbX7bHk0n6GFzRqYAG2jL2XSAIAy5ggIh5fxDlxgF3u3tM2OJmhWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140550" target="_blank">📅 01:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140549">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnrRR8RURKtA5SRSMiZUsCWoEPGQcLx9xVgrB7X2ZIpDqVyxwmkeDjDqui5Gzfa-gtqKV_B7kIRS_5xy7pI-lqnejCvOFR-k0wFtXbD_tgP45xW6CExRaII0P9PyUiVjjUsmB7IFjK0V9NIWhxEBBc9mCtly_KkEtM0rUKEfW1VjSPQ_sD4Syp-V8Koke5R_PfD7uoB02QQ_HTdVgwCvApOzoN4QvDrVbeZ6kA8LOwrDhspZ7TlqAfTzjU2NWRbuDwHkN_OQvND0IibxddyGoLa5_t20T6tuQJBAL7j9_iX3GpR6UWJGbERWHIsR07dsaVXb6SV6s6dmZcjwpHJhDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140549" target="_blank">📅 00:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140548">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1qmo4uW1Vccxw6DjWCKdDm4KvCJawTOxRe1KRNPNFmXTRMsdoL1l3n8f-X0wYrUOrl4OJWgfBayETq-KDGZV47X9cdjyZWKOCgH-xrJzIypPFXUmXwU6OV997mP_g-pBYO2Xop74zIluTXuoP8U0dL_-Xv9hoGPPAvvcQZMVxOwLJnQrD_-1Z53_ctgTMeXF4HSc9gyXYEflKDBKz8gXfgBnL2jFgkzbooIqFhR0P8zaVg_5D2iufhd3uVrOqAodykuGp_2olz2h1d2IB-FfdaESCF0j4ickFW5cpQTz3tPT8VmPYQRgbva6b-Td98WfPIwSRpamiS6AJ0y5GNYkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نتایج هفته دوم لیگ برتر بانوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140548" target="_blank">📅 00:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140547">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔻
پرسپولیس قید جذب اندونگ رو زد
🔻
باشگاه پرسپولیس به خاطر ریسک بالای این انتقال و دور بودن اندونگ از شرایط بازی، تصمیم گرفت بی‌خیال جذب این هافبک گابنی بشه
🔻
طبق شنیده‌ها، تا این لحظه تراکتور تنها تیمیه که همچنان دنبال جذب اندونگه و نکونام هم روی این انتقال…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140547" target="_blank">📅 00:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140546">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gF7Gjjj7WhKqcOJGiO2DYecdhhvHd880wFrslokss-ieDTvSn-02zqqwtuBwdbsAahfAtU8AbHc0d1d8qpZsUVQNXI3G5Ixl0nCsNHFCWFbl-pvYppwJoQF_D2heizahCWR2H-XAiTCXK7kTUSXkxGBy0q0X7akZs_wTWbWolNlZp9cc1G-1miDp63m68t8Bu2GUlS6-D_J11UEfFBmlnEYyF9zzxM0h22-Bik2LjVAS6aPdPF6mC1cR4M3pSQY7kiDWWqq2PwckWLoNFgmuPIHM3R_8aBsNRJJWJFmHDlO2R74V32HCBpQaZsZ2cfBLoWvs5G8r75Nid7SCk2pgdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یه سری شایعات از بازگشت اسکوچیچ به تیم ملی در حال انتشاره که نه تایید می‌کنیم و نه رد می‌کنیم.
/فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140546" target="_blank">📅 23:42 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
