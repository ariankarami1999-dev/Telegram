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
<img src="https://cdn4.telesco.pe/file/FDV-TlqD8hcFIxULa7MZzl8HGhmL90mwI7NEpZe3qhiiLzkssm4CH3hUledV_Yf0LUKblsBBerFtYhsxJox_IQqJqmn8feW7TaTHQ07smAVzInZB4LWAXXai3wFR8cJlsyDG2YhDfUXqAzEudsal5TPPHzKdTUyH6Nd_qt4kuRc2BnkrIp7F88QbHMUdCq73sHv0l9lQLY8Vlx9BnvvaS1QHOESSMIqrhEU805T2lJ1D4dHxveq2Q7Mu3vGNqvZzltmBPt_N-v6MrRhv_aDE_b8U2jFg9sCkaagXwT-6YkkV8tucy51ilEzYhyBhSfaswBSQRV4GI00UogjCvwIa3g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 03:28:11</div>
<hr>

<div class="tg-post" id="msg-137078">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c21rkm5o5flq8ESk95yOVJxfyjsIxCXBHL5maZHdW8FtDis_6wmb0aT3UkOXjBkX215xPAa6pIcvoeYQzIVUMxPETD46CopNzRrzLTqdJ5Q2xBTxFfVTogbTrOcZbhjxxF89SuPBIUvED4PyyI7L7B6slctZzaa7KJO4bS1eZMdiEkY4O3Py5HNy3DjJA4X04gdtIE2Pd24RHaaAloIZtZLKUTQo1I_QtXmWC8ar20fSvBnRciHBew01463_dMrnwZyi_FIZkhVJBLZP9T7iJYOTDyS7jEAkRobw9nRaUbUl1CSEZW53P77GH0kJKKKBQkVP30UMRerGUW3DhTjozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
تقابل استعداد نوظهور اسپانیا با ستاره باتجربه ایتالیا؛ آزمونی بزرگ برای جودار!
🎾
Jodar -
🎾
Musetti
🎾
دیدار رافائل جودار و لورنزو موزتی، تقابل استعداد جوان با تجربه و کلاس بالای تنیس است. جودار با انرژی بالا و بازی هجومی به دنبال خلق شگفتی خواهد بود، اما موزتی با تنوع تاکتیکی، ضربات بک‌هند کم‌نظیر و تجربه بیشتر در مسابقات سطح بالا، روی کاغذ شانس بیشتری برای پیروزی دارد. اگر جودار بتواند فشار سرویس و ریتم بازی را حفظ کند، این مسابقه می‌تواند به یکی از جذاب‌ترین دیدارهای این مرحله تبدیل شود.
📌
مسابقه را فقط تماشا نکن؛ از هر امتیازش فرصت بساز و پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 683 · <a href="https://t.me/SorkhTimes/137078" target="_blank">📅 02:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137077">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
فووووووووری از قدوسی
✅
✅
منتظر یه خرید خوب باشید......
⚡️
⚡️
این همون خریدی هستش که خلیلی ازش حرف زد و گفت داره قطعی میشه و هوادار پسنده.....نامش آشناست......
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SorkhTimes/137077" target="_blank">📅 01:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137076">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
هالیلوویچ؟منتظر یک خرید خوب باشید.
🔴
🔴
الن هالیلیوویج در تمرین و اردوی پرسپولیس حضور نداشته و اخبار تمرین کردنش با تیم صحت ندارد
🔴
🔴
ایجنت او با مسوولان باشگاه صحبت هایی از مدتها قبل داشته و احتمالا در تست فنی شرکت خواهد کرد
🔴
🔴
هالیلوویچ به عنوان گزینه خرید…</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/137076" target="_blank">📅 00:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137075">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
هالیلوویچ؟منتظر یک خرید خوب باشید.
🔴
🔴
الن هالیلیوویج در تمرین و اردوی پرسپولیس حضور نداشته و اخبار تمرین کردنش با تیم صحت ندارد
🔴
🔴
ایجنت او با مسوولان باشگاه صحبت هایی از مدتها قبل داشته و احتمالا در تست فنی شرکت خواهد کرد
🔴
🔴
هالیلوویچ به عنوان گزینه خرید…</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/137075" target="_blank">📅 00:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137074">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
مرصاد سیفی و امیر جعفری دو گزینه نهایی تارتار برای حضور در دفاع چپ پرسپولیس هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/137074" target="_blank">📅 00:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137073">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
هالیلوویچ؟منتظر یک خرید خوب باشید.
🔴
🔴
الن هالیلیوویج در تمرین و اردوی پرسپولیس حضور نداشته و اخبار تمرین کردنش با تیم صحت ندارد
🔴
🔴
ایجنت او با مسوولان باشگاه صحبت هایی از مدتها قبل داشته و احتمالا در تست فنی شرکت خواهد کرد
🔴
🔴
هالیلوویچ به عنوان گزینه خرید…</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/137073" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137072">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🌀
🌀
🌀
اظهارات کنایه‌آمیز محسن خلیلی: تیم‌های دیگر هم دلسوز بازیکن گرفتن پرسپولیس هستن. برای جذب هر بازیکن تیم حقوقی ما بررسی می‌کنه تا محروم نشیم.
📎
📎
📎
خبرهای خوبی درباره انتقال یک بازیکن می‌رسه.
🤔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/137072" target="_blank">📅 00:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137071">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
تک گل پرسپولیس در دیدار دوستانه مقابل آلانیا اسپور
✔️
جادوی ارونوف و امضای علیپور؛ یک پایان بی‌نقص، حاصل نبوغ فردی اوستون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/137071" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137070">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
#فووووری   #شایعات
✔️
✔️
گفته میشه یک مدافع چپ جوان خارجی در اردوی پرسپولیس حاضر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/137070" target="_blank">📅 00:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137069">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
❌
آلن هلیلوویچ به تمرینات تیم در ترکیه اضافه شده و قراره بصورت بازیکن تستی تست بده و اگه اوکی باشه باهاش قرارداد ببندن
🖍
قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/137069" target="_blank">📅 00:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137068">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⚠️
⚠️
عادل فردوسی‌پور با این ویدیو از خودش دفاع کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/137068" target="_blank">📅 23:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137067">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2a693019.mp4?token=KyPmokBHpEaoHQloGZdHUv3312FyWDS4lMOyXDJ8HG20D-GYNKyAf6YgDC90hRZomkaW-s5rX2lqV2IHZ52zwS4gjTatcylvNWqWreYjr__qg06sCz7iLg9EaKOPdwX6p_WlIdCfLgX4gaVZKPjDSuWjA1lWgR4dlurtF9-oeCasyto_dEqbT-8-zkEzPejwXFjNi4TNRg2JvsMbYUllqldw9hFv2ItgPqHyuoLuB3acZuAN8VJdUewPyVcDz7HtJmF7tm7DoTB4ZoGYITgUm_rOV2sZhNWIS5pkIjVsE2lXRjzF0xWW0ng0iA0I749_E3nnT_kAOuuiHMbxVhu-TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2a693019.mp4?token=KyPmokBHpEaoHQloGZdHUv3312FyWDS4lMOyXDJ8HG20D-GYNKyAf6YgDC90hRZomkaW-s5rX2lqV2IHZ52zwS4gjTatcylvNWqWreYjr__qg06sCz7iLg9EaKOPdwX6p_WlIdCfLgX4gaVZKPjDSuWjA1lWgR4dlurtF9-oeCasyto_dEqbT-8-zkEzPejwXFjNi4TNRg2JvsMbYUllqldw9hFv2ItgPqHyuoLuB3acZuAN8VJdUewPyVcDz7HtJmF7tm7DoTB4ZoGYITgUm_rOV2sZhNWIS5pkIjVsE2lXRjzF0xWW0ng0iA0I749_E3nnT_kAOuuiHMbxVhu-TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
تک گل پرسپولیس در دیدار دوستانه مقابل آلانیا اسپور
✔️
جادوی ارونوف و امضای علیپور؛ یک پایان بی‌نقص، حاصل نبوغ فردی اوستون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/137067" target="_blank">📅 23:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137066">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
گفته می شود ایجنت ایرانی نزدیک به‌ عثمان‌ اندونگ به مهدی‌تارتار سرمربی تیم پرسپولیس گفته که اندونگ از سپاهان‌آفر دریافت کرده اما اگه او بخواد باپرداخت 600 هزار دلار میتواند رضایت نامه این بازیکن رو بگیرد و او رو به پرسپولیس بیاورد.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/137066" target="_blank">📅 23:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137065">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⚠️
⚠️
بندرعباس بوشهر قشم کیش آبادان و اهواز بامداد امروز شدیدا مورد حمله قرار گرفتن و گزارشات انفجار تو این چند شهر بسیار مهیب بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/137065" target="_blank">📅 23:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137064">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
🔴
🔴
درخشش علیرضا همایی‌فر در دیدار دوستانه؛ پرسشی جدی درباره روند استفاده از این بازیکن در پرسپولیس
⚽️
علیرضا همایی‌فر، بازیکن جوان پرسپولیس، در دیدار دوستانه روز گذشته تیم خود، عملکردی قابل‌توجه و امیدوارکننده از خود به جای گذاشت. همایی‌فر که توسط مدیریت سابق…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/137064" target="_blank">📅 23:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137063">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQbDtBZJvQ1KPRz36Mtq_r2nw6BO7QGKzVqdozk3NrnobP0cnRJ7OnGHzXWbeW2ARHkOWUtyY4IpatsJx0d3vQxmuntBrTEATEsuQfNFgk-bYBnN-8_e3BMCx6f2TmxUqAlYfFzdzcVEsL6b38x2olgMEp52rdDczf6fuAXfasVqvsoi1wcUJVNgtImd68ErN6rMiG817GHim8yjOucye3RHs3PlhrcKOfuz1EMcOVB7se6CCKhwynPrQboV2QCTnQCuvfL032WlA82yMwG0d_FzSOYlnqk9c1Y9DZWfijwmRPQ9wPGV3KvI0_c7mXIAAKSf9SG1ymSUDCpERKKWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
باشگاه پرسپولیس تندیس عالیشاه، سرلک و پورعلی‌گنجی رو ساخته تا در مراسمی ازشون تقدیر کنه
فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/137063" target="_blank">📅 23:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137062">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
❌
عملکرد تارتار در بازی های دوستانه
⚡️
۴ بازی
⚡️
4کلین شیت
⚡️
4برد
⚡️
7گل زده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/137062" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137061">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be-OVC5kMNdEPY67dWd6yvpJzhcz82ame8sI7cAEfPc0bHKRrX2CYvJ1DMITX_kGkI6EHStV2QnJwCvcHweJZRRnNRT48zLa3fATfnsZIqSO-_3X5KZpOQhHxpRb0SiWTrxCAflahoP2FDzK94pfOOHy5ATtxUN1yL9o-wIP1iqCEY2RIOsnD4_5bdbonUXzE6ssQSbKgHv9Vn7vm37AQ7jEfn50YyS089bYLBeKAm419fhYtC4VxafhZULmVpwHTHnAfRfjt0gbskyZ56DKp2FYIp-wuZvDvaTAMaezv1YiZVly4SFCMIGaQkaFKVw-yccqkemAYC59LaZQ-VPlgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شایعات؛ رامین رضاییان تمایل داره به پرسپولیس بیاد و تارتار هم بهش علاقه منده!
نظرات؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/137061" target="_blank">📅 21:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137060">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-VeI5iUqCNa7kJA7NGmR7ul7nyoZ7URfzflB0itjf6t21GHXEZUx59CLDmPnNTjOeaC4qo9LbhMAsHvGWFatRJrW32E0mu__BgcgPYkQ7fLH88FO83-tO8SOHNvox2lhr8UPhcx2JFwQgV0Z8A3zGuL4m04ZWL0kq1O85r7bTQ0_fWcgZT97BcKp8JNpukjkYVkNb0x0tWtoa0uziUiHsneEYBM-pzaKQP3S0uMIZ7F9GE-VkP6ngeBE82n0nT8UE62sqHcdtvxghhHY8fmOHq97v46xEeZJ9gRUT88v1oCfFbCftYQArVQ08GfgVnygbWjS8dvdrj5vClY_lYs6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
⚡️
پوریا لطیفی فر با نخستین تمرین، آمادگیش رو نشون داد طوری که خیلی ها جا خوردند. کلا هافبک با انرژی و دونده ای است که شاید بخشی از این خلا بازیساز رو بتونه پر کند
⚡️
⚡️
مهدی‌طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/137060" target="_blank">📅 20:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137059">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❗️
❗️
عیسی آل کثیر یه ویدیو از زمان حضورش تو پرسپولیس استوری کرده، پروفایلشم به عکس پرسپولیس برگردونده
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/137059" target="_blank">📅 20:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137058">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iu8wJbeWX2PqOgoa6tq1-_byP0HLuehmaF8cVleWb7xBKEDIxUlF2oU1M32b9vCmuYb_UR3DFno2wgcGVQ9WE6l5dlwj3DsrD7vaecRIWinTkpfe8wgthB9FjV6KxygVbxdK7cgZne_PC3RvqTr7iXb8omTUyGp-lvnkNADfnXqi6JfS9NCm_KvoG3Cj_Q0gC5_JIu2GgebruOxZDZnDX4K4zFGVTy3l1rtEaYMjg0ykUSKM_CVOpXIK2_z3xIRqicJEas_uSPeIjlwAXLRc2K_nJjIRYgZTWVfUj6dD4sXk3V-NiLd89NPNqXXNE2KCJUTnlG6t0Zb5mIvTVYwtsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عکس تیمی پرسپولیس برابر آلانیا اسپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/137058" target="_blank">📅 20:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137057">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⚡️
پرسپولیس به مانند بازی قبلی در دقیقه نود به گل رسید و بردهای یک بر صفر تارتار در دقیقه نود ادامه داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/137057" target="_blank">📅 20:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137056">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
🔴
🔴
توجه | مدارس و دانشگاه های استان تهران غیرحضوری شد
⬛️
استاندار تهران:
⬛️
با تصمیم کارگروه اضطرار آلودگی هوا تمامی مقاطع تحصیلی استان تهران بجز فیروز کوه روزهای سه شنبه ۴ آذر و چهارشنبه ۵ آذر غیر حضوری اعلام شد.
🟦
دانشگاههای استان تهران بجز فیروز کوه غیر…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/137056" target="_blank">📅 20:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137055">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-s0yl22q0n3WBlqGjUmP93AtLQwdopO1aZ5qSXruMiW0Smri16mMUhCtIzKliSnj11ZISrEQhMhbFSpDn0Yk1E0jkc2p9tJV4T_AprE-BU6j2YfJOtbqY2SOHchtvnDoZ4AnrS_J3ufIfXzUdAOyoPrkZrswPUdzRlqU0zg57v_th6-7dL_iDfTlkKgsvXRZNR6-pj1iBXPa4NHesTg2fmBfQJ-rqFRkVs0W5gZnhGIePD_TX_UtvzZfHVnWgRY5dA69M9-DU4f1whMgiETpJHSCvXj4nErtJXwqQpNDjQaph42KNiSw0bNKQKdDODhF6ZvOqQrtkH2gMEgypkuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
برنامه بازی‌های مقدماتی لیگ اروپا
⚽️
امشب لیگ اروپا بار دیگر با تقابل‌های حساس و تماشایی، فوتبال‌دوستان را پای گیرنده‌ها می‌نشاند. تیم‌ها برای صعود و نزدیک شدن به مراحل بالاتر، با تمام توان به میدان می‌آیند و همین موضوع نوید مسابقاتی پرهیجان و غیرقابل پیش‌بینی را می‌دهد. شبی پر از رقابت، گل، هیجان و لحظاتی که می‌تواند سرنوشت فصل بسیاری از تیم‌ها را تغییر دهد.
⚽️
بازی‌های امشب رو در
ربات وینکوبت
با ضرایبی شگفت‌انگیز همراه با ۵٪ شارژ بیشتر از طریق کریپتو پیش‌بینی کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/137055" target="_blank">📅 20:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137054">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⚡️
پرسپولیس به مانند بازی قبلی در دقیقه نود به گل رسید و بردهای یک بر صفر تارتار در دقیقه نود ادامه داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/137054" target="_blank">📅 20:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137053">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔄
🔄
🔄
جونم تیم ..پرسپولیس دقیقه نود گل اول و برتری و زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/137053" target="_blank">📅 19:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137052">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⚡️
نیمه اول دیدار دوستانه پرسپولیس و آلانیااسپور بدون گل به پایان رسید.  در حاشیه این بازی، محمد عمری و اورونوف در کنار محمدمهدی محبی روی نیمکت و زیر باران نشستند تا یک قاب جالب و متفاوت در ارزروم ثبت شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/137052" target="_blank">📅 19:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137051">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
آلن هالیلوویچ فردا در تمرینات پرسپولیس شرکت میکند.
🔄
مهدی طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/137051" target="_blank">📅 19:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137050">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⚡️
⚡️
تایید شد
🔻
🔻
آلن هالیلوویچ، بازیکن کروات با اصرار محسن خلیلی به ترکیه سفر کرده تا به صورت تستی در تمرینات پرسپولیس حضور پیدا کند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/137050" target="_blank">📅 19:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137049">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⚡️
⚡️
فرهیختگان: مذاکرات تراکتورسازی با الوحده بر سر قربانی به بن بست خورد ؛ چرا که زنوزی دنیال تخفیف هستش و قربانیم حقوق بالایی طلب کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/137049" target="_blank">📅 19:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137048">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyMbwjnjdy_yCcvN5bgWPEI4z0DX-fJ9oMtO_YH7I9uWUJ8mAo45jlSsbu_mwK06rlxL-fhLHSwmwp3Zb6yu4u5BQHklBuiQ-jMzVCVn57d2u6vb_CQxf0EPPHZVc7NgAca1B3URXnrg67hpOPRjSxqb1ev0XEdWSEarhNpci7VgogqSPa3A_VqFR_LXqMa3wnJmfv7oWGl9X8be0x8tXjyGCZGShBg2MQJwylTAw-LSdPXdxisqIvJTMOdvYKmzkEXGFV-7Q8FsScQXO_1lEB44STQUw7d9IbQ1k6VsHje90GU1Bk2967OCLWVX-Cto9jyY-pB7vokl59H6YwpUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
نیمه اول دیدار دوستانه پرسپولیس و آلانیااسپور بدون گل به پایان رسید.
در حاشیه این بازی، محمد عمری و اورونوف در کنار محمدمهدی محبی روی نیمکت و زیر باران نشستند تا یک قاب جالب و متفاوت در ارزروم ثبت شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/137048" target="_blank">📅 18:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137047">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🫥
🫥
با موندن امیررضا رفیعی پرسپولیس میتونه 5 بازیکن جدید در پست های دیگه بگیره
🔴
دفاع وسط
🔴
دفاع چپ
🔴
هافبک بازیساز
🔴
مهاجم
🔴
دفاع راست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/137047" target="_blank">📅 17:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137046">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
✔️
طبق اخبار دریافتی غیر رسمی : باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/137046" target="_blank">📅 17:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137045">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⚡️
⚡️
فوووووووووری
⏺
باشگاه خیبر خرم آباد رضایت نامه مهدی گودرزی رو 70 میلیارد تومن اعلام کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/137045" target="_blank">📅 16:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137044">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⚠️
⚠️
⚠️
تغییر ساعت برگزاری دیدار تدارکاتی پرسپولیس و آلانیااسپور
⏺
این مسابقه که پیش‌تر قرار بود از ساعت ۱۸:۳۰ برگزار شود، از ساعت ۱۷:۳۰ به وقت تهران آغاز خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/137044" target="_blank">📅 16:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137043">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✔️
✔️
✔️
طبق اخبار دریافتی غیر رسمی : باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/137043" target="_blank">📅 16:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137042">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT04ujgiDr_WW_0yaCjaZ0ZTz_SpeYm2zgv0rd8YyTWNRRe-TOnB8g5rkT1F2y8HmBfmfpUvkbpM5WJQhg6wRNWenZakpLrlGWOE3mUYLrJ3WQI2KsAZ2bRCB1xmit46QM1_c-nPGF_W2F7dKw7vbAar8k9DE707kR1DF5MhjutYFkz3rCnTZynDTHqUhzDUvus8q4vi0TVCrhF-4LwIakbx3THNifo7HcsAq1JSanPlFlEUSr0Ddntg1t-rdlfRubZpW5fltaLT1An9ZYX2o_dpKXVesNDjQaLZyDAi8ila9xFKJ2TVX9Q6ZVxTAt2kK2R4E5aVsGqKJQB2ie6VlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏐
اوج
هیجان و جذابیت با لیگ ملت‌های والیبال همراه با
اسپورت نود
🏐
پنجشنبه ساعت ۱۵:۰۰
[
لهستان
🇵🇱
🆚
🇺🇦
اوکراین
]
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
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/137042" target="_blank">📅 15:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137041">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
🇳🇱
رسانه‌ی هلندی:
🔴
آلن هالیلوویچ در آستانه پیوستن به پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/137041" target="_blank">📅 15:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137040">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_sU3dysQPoBuTdGOCse_VmEacGd6eLz2XwvbEQXWFiZyXPet1vbi92pT4tz1H2Dkkrr7oZaif9jPNS481IgKh4AElzxq0xNtpdyeW8JTlsSkn8gDqLSg41fbpndo_3Elhf_zYEM0w9tPcVDD4EowJduYEazzFrAJYuR-iAQle3unbZYNi0oYWkVHjMUO-sQcY2rDA_WN8i_iWthmtZ0_u8BwBUY1TPR5Flsq-TkBQrCMQkDKepadj0psikaK4ZheNONoMhLBD0ono1Jv9bW_0JY_eC4M51o37b31eOS5HW-bsnUNPZTiZaC8-KA2u9WscCJFMpDDyPBxgv3KVRm3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ورزشگاه دستگردی تهران حداقل تا‌ دوماه آینده بدلیل تعویض چمن در دسترس نیست و امکان برگزاری و میزبانی از تیم‌های تهرانی را ندارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/137040" target="_blank">📅 15:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137039">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
❌
حضور مسعود محبی در روسیه منتفی شد/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/137039" target="_blank">📅 15:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137038">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🏅
آلانیا اسپور حریف تدارکاتی بعدی پرسپولیس در ترکیه
▶️
با اعلام باشگاه پرسپولیس، شاگردان تارتار، روز پنج‌شنبه در دومین بازی تدارکاتی خود از اردوی آماده سازی پیش فصل در ترکیه، به مصاف تیم آلانیا اسپور خواهند رفت که خود را آماده فصل جدید رقابت‌های سوپر لیگ ترکیه…</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/137038" target="_blank">📅 15:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137037">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
تارتار گفته عیدی تو فاز هجومی خوب نیست و ازش راضی نیست  پ.ن مگه با نظر خود تارتار جذب نشده .مگه بازیکن خودش نبوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137037" target="_blank">📅 14:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137036">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
❌
❌
حریفان پرسپولیس در نیم فصل اول:
✔️
هفته اول: شمس‌آذر
✔️
هفته دوم: اس‌خوزستان
✔️
هفته سوم: تراکتور
✔️
هفته چهارم: ملوان
✔️
هفته پنجم: استقلال(میهمانیم)
✔️
هفته ششم: ذوب‌آهن
✔️
هفته هفتم: خیبر
✔️
هفته هشتم: صنعت نفت
✔️
هفته نهم: مس شهر بابک
✔️
هفته دهم: فولاد…</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137036" target="_blank">📅 13:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137035">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
#منهای_ورزش
✔️
باز هم جنوب باز هم مردم بی گناه
💔
❤️
✔️
شهید و ۲ زخمی در حملۀ آمریکا به محله چاهتنگو شهر قشم
✔️
دانشگاه علوم پزشکی هرمزگان: در حملۀ دشمن آمریکایی به منزل مسکونی در محلۀ چاهتنگو شهر قشم، پدر و مادر خانواده و یک کودک ۲ ساله به شهادت رسیدند و…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/137035" target="_blank">📅 13:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137034">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">📎
📎
📎
یه سوال پیش میاد اگه واقعا حس میکنید هنوز تو دفاع راست مشکل دارین پس عیدی چرا جذب شد؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/137034" target="_blank">📅 13:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137033">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/915de24844.mp4?token=CmcLpqGvp1x5TcwAPIqC2X1-y4wwH9TEtEK1khEH4tmOIRStvC8qA2pQd_SS5S_KU3iWGXerxOx22yDPEY90BrvnglzrD6hN-dDwfpbbb-c8RkcY-nT4XieyxjEgF0NhWPSm655L6FUfWgoTj5xaMjgB8FrZf4hD7w3-W2w8kn3lx75WjdTLQ4So9kgRzeOynKJXUy9JTTgPV4XwrjDpW-Gqfh6NR-9a712vhVSshduFk8svhqQZDTokm0Vk129N82qPKnq12OUdBply139AhhS8ldQzHYElTZroFmoxi4qq-ODK9NoTf4fm04h9vO36rdOQysKjcwlXjV6BgXU9z7QkjYULQqLdWiVFO9fAeIGyAz7hlMR8k5nl2myzU3bBV9i0dyiC5c4O8Son9sKXrNEDy5ti1Z_ZsBZpuJQwKdjCq3UICIRvLrJh2Yd3qSSqR0AMhRmN3_j8UAz_OHmauzRPpzDBFS0mo33yeTy_mO6lkwMa9FULlySrS0oMcw1I05T2ciEQvFN0XQnsTpOfD5a21lReLl4L2GBjwEy1rhVBVu7R-XaEBjumO3O8MhnXRaBO28lr3kze7dod8nSrcGQ2aDDNHqhPuZEYVltWrgJ77l1-GitiwOmlJlNBBxg-mxKxjfavngY34FWrBfp1TA8dFv6kYE2g0CkKanHttGo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/915de24844.mp4?token=CmcLpqGvp1x5TcwAPIqC2X1-y4wwH9TEtEK1khEH4tmOIRStvC8qA2pQd_SS5S_KU3iWGXerxOx22yDPEY90BrvnglzrD6hN-dDwfpbbb-c8RkcY-nT4XieyxjEgF0NhWPSm655L6FUfWgoTj5xaMjgB8FrZf4hD7w3-W2w8kn3lx75WjdTLQ4So9kgRzeOynKJXUy9JTTgPV4XwrjDpW-Gqfh6NR-9a712vhVSshduFk8svhqQZDTokm0Vk129N82qPKnq12OUdBply139AhhS8ldQzHYElTZroFmoxi4qq-ODK9NoTf4fm04h9vO36rdOQysKjcwlXjV6BgXU9z7QkjYULQqLdWiVFO9fAeIGyAz7hlMR8k5nl2myzU3bBV9i0dyiC5c4O8Son9sKXrNEDy5ti1Z_ZsBZpuJQwKdjCq3UICIRvLrJh2Yd3qSSqR0AMhRmN3_j8UAz_OHmauzRPpzDBFS0mo33yeTy_mO6lkwMa9FULlySrS0oMcw1I05T2ciEQvFN0XQnsTpOfD5a21lReLl4L2GBjwEy1rhVBVu7R-XaEBjumO3O8MhnXRaBO28lr3kze7dod8nSrcGQ2aDDNHqhPuZEYVltWrgJ77l1-GitiwOmlJlNBBxg-mxKxjfavngY34FWrBfp1TA8dFv6kYE2g0CkKanHttGo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
❌
بهترین خبر امروز: نوید قره داغی حرومزاده که دخترا رو کتک میزد، دستگیر شد.
🔴
امروز صبح موقع دستگیری نوید بیشرف ، این حیوون وحشی به سمت پلیسا حمله‌ور میشه. پلیسا هم سه تا تیر توی پاش و یه تیر توی دستش میزنن و حسابی کتکش زدن، اعضای محل هم هر کدوم یه انگشت توی کونش فرو کردن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137033" target="_blank">📅 13:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137032">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
شنیده میشه پرسپولیس دوباره رفته سراغ مسعود محبی و با پیشنهاد جدید دنبال جذب این بازیکن
🔹
محبی هنوز هیچ قراردادی با تیم روسی نبسته و امکانش جذبش هنوزم هست همه چیز بستگی به نوع مذاکرات و پیشنهاد مدیران تیم داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137032" target="_blank">📅 12:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137031">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎥
⚽️
ویدیو باشگاه از تمرین تیم با کپشن:
😀
از ضربه‌های تمام‌کننده تا واکنش‌های تماشایی؛روزهای پرانرژی پرسپولیس در ارزروم
❌
پ.ن حال پرسپولیس خیلی خوبه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137031" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137030">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🫥
🫥
با موندن امیررضا رفیعی پرسپولیس میتونه 5 بازیکن جدید در پست های دیگه بگیره
🔴
دفاع وسط
🔴
دفاع چپ
🔴
هافبک بازیساز
🔴
مهاجم
🔴
دفاع راست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/137030" target="_blank">📅 10:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137029">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
پیوستن پورعلی‌گنجی به الطلبه صحت ندارد
⚠️
⚠️
ساعتی پیش برخی رسانه‌ها از پیوستن مرتضی پورعلی‌گنجی، مدافع پرسپولیس، به تیم الطلبه عراق خبر دادند اما پیگیری‌های خبرنگار فارس نشان می‌دهد این خبر صحت ندارد.
⚠️
⚠️
پورعلی‌گنجی هیچ قراردادی با باشگاه الطلبه عراق امضا…</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137029" target="_blank">📅 09:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137028">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/137028" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137027">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⚡️
⚡️
امیررضا رفیعی قرارداد جدیدی را امضا خواهد کرد
🔻
🔻
رفیعی یک سال دیگر با پرسپولیس قرارداد دارد مشکلی برای همراهی این تیم نخواهد داشت اما احتمالا با تمدید قرارداد در جمع شاگردان مهدی تارتار حضور خواهد داشت و زیر نظر حسین اینانلو کار خود را دنبال خواهد کرد.…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/137027" target="_blank">📅 09:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137026">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🫥
🫥
🫥
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/137026" target="_blank">📅 09:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137025">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
رفیعی ماندنی شد
🔄
امیررضا رفیعی گلر جوان پرسپولیس ماندنی شد و به ارودی ترکیه ملحق می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/137025" target="_blank">📅 09:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137024">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
رفیعی ماندنی شد
🔄
امیررضا رفیعی گلر جوان پرسپولیس ماندنی شد و به ارودی ترکیه ملحق می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/137024" target="_blank">📅 08:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137023">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTI0XSClbbR-ay0b4XaV9I2Y1ji0-0AfryM2aIc4zOBYVplj4DpEDg7k1wOhejHBmkZipUy9LciEzpLQjFzdeGXKK580i2nTyQRMRAk0yG-ngikQX8uYRMNba5LmdV8WYLSWrGW4cAXqjoS8mQut7S9IqDH8aQBPlAyULH8e2q2WyT81jYQVKVRCDB78lkxht6O3LPTsVxYFEPHGKxjVgdYrFNOiQqequ5YFAWvwOmiKPdnwviy8HWUvH1TxzI7ZGfbgPfDfvuoOOIQsiRlYk7zXKciIdiES-2ScPdhDy-QkSO_9R8mbYqX6w_kauSyfCiyYGaO5biMtc4-A_bGrsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137023" target="_blank">📅 08:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137022">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtXE2Q801NugBP208v5RN9WYMVzkNxcgJo7bssEFwVQinPZ9uxJcWsZELnDC7Jw7hOlW6c9sIuIQQCRpIMXDElQ_SBnbrB594pu5L0ie_WBByFDz4P-6FhCKWqf3mEIQ8cGCnCN1zpiImTdij374e4sBAquex6w2uuj4_V1NTjOK5WqCoyL-MjmZHjvch2X1ejWNukHLDmdlH3214kYgiY3y8Mxb7zvZ-vQFWlwrAj0RYsDBKhhg8i1K6eq8wCqyySKs-P4Hkw0sX93gmLG1iIeDmIXQ6-oiu6YrFqxJnQ_TIwstJEMtpVcrHGg-5lw73Le_Mf5w9zipNhvfWFDVvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏐
اوج
هیجان و جذابیت با لیگ ملت‌های والیبال همراه با
اسپورت نود
🏐
پنجشنبه ساعت ۱۰:۳۰
[
ایتالیا
🇮🇹
🆚
🇺🇸
آمریکا
]
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
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/137022" target="_blank">📅 01:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137021">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De1ixxGiPnP_U9F7n3COcxMLeZJe-R5mMuijsiWdZHsWxeZXB3z-wjRnSwZ2ZaHsAghMEDx_VwJ7RoKFxVyNV1qwHCmxHrWtR0uMugHozf_Az62EXugFphV38I6YZdDjnqKPvyyPftkBWZWbOod6ci52vVVRo4T0LBAKFYiLvdxdtont15U9JF9nf3smUpmQDOae7QAhaaboig7NXZ_frAk2iQAtTgbvnxLFUNvfVvQSaQA_m3j4O8JlxJ1s_LawRIYPlosP4t9_LBg3KFpsttQNemUVOQ-d7CbrFArJOeWj5-HE47et7jCfr-tsRSixvktQ_osiu4Yep3kVEEHfew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
رفیعی ماندنی شد
🔄
امیررضا رفیعی گلر جوان پرسپولیس ماندنی شد و به ارودی ترکیه ملحق می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137021" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137020">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❤️
❤️
❤️
❤️
❤️</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137020" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137019">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⚡️
⚡️
پوریا لطیفی فر با نخستین تمرین، آمادگیش رو نشون داد طوری که خیلی ها جا خوردند. کلا هافبک با انرژی و دونده ای است که شاید بخشی از این خلا بازیساز رو بتونه پر کند
⚡️
⚡️
مهدی‌طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/137019" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137018">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
تراکتور از جذب قربانی منصرف شده و کناری گیری کرد /فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/137018" target="_blank">📅 23:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137017">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🫥
🫥
🫥
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/137017" target="_blank">📅 23:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137016">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
فرهیختگان: اولویت های تارتار در پست‌های مختلف
✔️
گلر: گوهری
✔️
دفاع راست: محرمی
✔️
دفاع وسط: افسرده
✔️
دفاع چپ: رزاق‌پور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/137016" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137015">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔽
مرتضی پورعلی گنجی با باشگاه پرسپولیس   به توافق رسید و قراردادش امروز فسخ میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/137015" target="_blank">📅 23:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137014">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔄
🔄
🔄
آنا: محمد قربانی با رضایت نامه 200 میلیارد تومنی به تراکتور سازی تبریز پیوست
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/137014" target="_blank">📅 23:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137013">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137013" target="_blank">📅 23:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137012">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
دنیل گرا در تمرین امروز هم حضور نداشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/SorkhTimes/137012" target="_blank">📅 22:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137011">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
شهاب زندی مدیرعامل نساجی:  با استقلال درحال مذاکره‌ایم، با توجه به بسته بودن پنجره شون اگه بر سر مباحث مالی به توافق برسیم این دو بازیکن آینده‌دار نیم‌فصل راهی استقلال میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/137011" target="_blank">📅 22:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137010">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⚠️
⚠️
⚠️
مدیرعامل باشگاه گل گهر سیرجان :
⚠️
⚠️
امیر جعفری مدافع چپ مدنظر باشگاه پرسپولیس قرار دارد اما تا این ثانیه به صورت رسمی با ما مکاتبات نشده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/137010" target="_blank">📅 22:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137009">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
دنیل گرا ۶ هفته از میادین دوره و ممکنه باشگاه باهاش فسخ کنه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/137009" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137008">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4994f708ed.mp4?token=TU17dcPVg6BDwTq-vKUyYKEdtchkrzObMqUaMRZQtZJZBsNQf8zZi6U9X60jk_HDARhmvqfOTKBJ99W0RQJfFJh0NZN63yBCwVEjDRQi1GHfQ0meUhR4SFJNglikIJ7gyit39Y6nBSC9m8bCT1QtQScxpu5F7F70qmeZ3gS5_2IkPYjJLGg5LMBrCrn3UgDRYsQxOOZeD7Ea8OguDBZggDFNiDiI8hZbhA5c83U0d1bMKa1B9rIbRL_GId2DHnOiffLIzfXNkHtU5zTjeVJfCP7LseCF5DOz29G0lRkfDzOaJzY5PSe2z3wvbX_HCDynMlN5Yo839ZvZiGbVM1uHWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4994f708ed.mp4?token=TU17dcPVg6BDwTq-vKUyYKEdtchkrzObMqUaMRZQtZJZBsNQf8zZi6U9X60jk_HDARhmvqfOTKBJ99W0RQJfFJh0NZN63yBCwVEjDRQi1GHfQ0meUhR4SFJNglikIJ7gyit39Y6nBSC9m8bCT1QtQScxpu5F7F70qmeZ3gS5_2IkPYjJLGg5LMBrCrn3UgDRYsQxOOZeD7Ea8OguDBZggDFNiDiI8hZbhA5c83U0d1bMKa1B9rIbRL_GId2DHnOiffLIzfXNkHtU5zTjeVJfCP7LseCF5DOz29G0lRkfDzOaJzY5PSe2z3wvbX_HCDynMlN5Yo839ZvZiGbVM1uHWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
تمرین سخت امروز شماره
1⃣
🧤
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/137008" target="_blank">📅 22:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137007">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
🔴
تارتار همچنان ولکن گل‌گهر نیست
✅
شایعات؛ باشگاه به دنبال امیر جعفری مدافع چپ گلگهر!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137007" target="_blank">📅 21:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137006">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EcK3lGoISh5UP-XJkbMSfvad4dYyZ5wX_M2nCsfWNnUef7U-yM-ZzdVF_jY4pc_WexF_EmVAlm7uKj7FtB0rGDAROBbSJbt_1WjZtY4ebvf5_IZX2rF--6P_0Uf5KTWiq75pwXNFY1CMZqVhTDQRy2hJfIgaNSrhXDinFgieVspVOXwv45yd-VBTkZ-zk8aIqwrlMBVq9w4nvzCdV9MUvXlB5ZL6xWYUDf0hfo8CLIZUJ5fcjUUswyeT3suOS3J7ObacxV5mQlWEGULOHhkvy2f2NHI0R1lW3kTL91ITw9xpcnImhwji88FumMCZ_yciY9kw0QQF9gk0Avk6tXvEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
شنیده میشه پرسپولیس دوباره رفته سراغ مسعود محبی و با پیشنهاد جدید دنبال جذب این بازیکن
🔹
محبی هنوز هیچ قراردادی با تیم روسی نبسته و امکانش جذبش هنوزم هست همه چیز بستگی به نوع مذاکرات و پیشنهاد مدیران تیم داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137006" target="_blank">📅 21:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137005">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
یاسین سلمانی ۲۰ دقیقه اخر بازی دیروز اومد زمین همه جا حضور داشت چه حمله چه دفاع
🗣
🗣
پاس گلشم روی یک ارسال تمیز شکل گرفت. با وجود اینکه جلوی چادرملو هم بهترین بازیکن زمین بود نکته عجیب اینکه چرا رسانه‌ها اصرار دارند مازاد بشه.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137005" target="_blank">📅 21:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137004">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdF8FC-xeIN4ghshL_Hta4JKzuFERg1u9lEbcW_0LfiQqbPLunP3-Q1e5nLDngXJxbOiy1nhDjWINMVj_JvZM-6x-ZAJ6bLODclaCmefarD9EIk0_NKYOnxff2EkyIn71hsI_WKAOcAs30aZeBR2DBCfcIQ7j0ZxvivH8E8Tn5jVI_v8qtx3XDHBtmRehOWWFcq8XcXBPCRPHraXi-fP7GWWgvsnVs-FEbdDE0WzmoD2BGRXs-rytI9lLT4Z2x0jyyul8q3t54FJs73VPqYDrl5nqXIdynl-hgCBCjlF3buXyNNPxgMwQ7wzawOC_9dswWdEfTL7iSrSz-7uJ7h3bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نگاهی به ۶ بازیکن ارزشمند لیگ برتر در سایت ترانسفر مارکت با حضور سه بازیکن از پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137004" target="_blank">📅 21:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137003">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlB4yv2swfiGbCsj59ip0TUJmwnb992t_gnYsFzNWvYOUEW1GTp83gmndurk4adHlIvswpjpqvPj0tY0hLqpFrkVVmftFwcqw-0WcA8PAu7kM8G39B3dt2c_0W9NGG4Gx9X2-sPLodGEyxF2j2GNOo9nM9CQFq2lgTx_wJJKz8XI-tSw88pdj5OHxoQe2sztptlhSxQjZpSx-G8UsYJQULgoeblpdxakagLknpoo8ICjWc7SpVS2DfnX9n3Lb3xXGdsADNmqBW6XHginx6u7i9x4eG5LNYTrSd3wcXL4PNStpj9KOsaytT9pJSHzN64094fQK0-v9CDWwOsX4MxYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
زیر و رو شدن چهره پرسپولیس پس از گذشت 2 سال
🟪
🟪
از ترکیب فیکس پرسپولیس مقابل مس رفسنجان در روز قهرمانی، تنها حسین کنعانی و استون اورونوف در این تیم باقی مانده اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/137003" target="_blank">📅 21:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137002">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🫥
🫥
🫥
تارتار امیدواره بیفوما و محمدحسین صادقی رو دوباره احیا کنه. بیفوما بعد از یه فصل ضعیف، تو بازی دوستانه اخیر گل زد و حالا فرصت داره خودش رو ثابت کنه. صادقی هم که فصل قبل فرصت کمی برای بازی پیدا کرد، امیدواره با اعتماد تارتار بیشتر بهش بازی برسه.
🌀
🌀
از…</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/137002" target="_blank">📅 20:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137001">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XN485V3dxf4j0PpnEDG5QMjMe9XEqt3MubwWRX8DnM-aWo7KYlE1UeKlhVlrGiBh6FSK65SN52E1V3cGo9UTVOg2AXQHmWoRHTd-XkJ15hcf-GzT6CwZghJl-AyF5JYEeKP7yKWzDlqC_pmLcy3WT34NhGW0zzgBea3k3jFgxfswITpI5aTvgUlvpkTwkf49YoPM2szchHIdRFXYmMBvyGQZR8ffXjYvOEp-dPBiX3LuFSJjeI-tRxC5tq1LwTf7drNLH8nl2UQJhN5_JaZ4Ft0OFQ8iydaLHATy8Krqjzelaf_PCao5Cav5y4Wlf2USOpR5s6kfZCRhU97pMW3NYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
اوج
هیجان مرحله برگشت مقدماتی لیگ قهرمانان اروپا همراه با
اسپورت نود
🇪🇺
شبی پرهیجان در مسیر رسیدن به لیگ قهرمانان؛ تیم‌ها برای یک گام دیگر به سوی مرحله بعدی به میدان می‌روند.
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
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/137001" target="_blank">📅 20:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137000">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc30274f9.mp4?token=UKojlm8spPO2IOfzhT8tfNJD0hA4l6myRgXB1cBc69w7k2r9sYQUFH0ax0Dp_3oW3RbO6ZVKr2rcFhWGnHztSVSVpK9Itb21hNgNC4DUi54I29kAjgPxg61zwpniOPxD9ZGevs4JS-s7pd8hygiZ1_L_1nHAtpmPMnPi4DlG4RWNldASY4yL4y16gw7DlDWxzwn6of0dD-bjGDcOdfvc0AoUOJMN23qHyJ69LpP0Leqqlxvej9XaVrQcYuoOY-qMWhlzBnR5pwLrKUI6rl82XYd0ysGdSV-JuLKncWwjfGLGiRhQjJh6th6f7D_eWbgGWybTq_CeT9GyP1oA7J-ZUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc30274f9.mp4?token=UKojlm8spPO2IOfzhT8tfNJD0hA4l6myRgXB1cBc69w7k2r9sYQUFH0ax0Dp_3oW3RbO6ZVKr2rcFhWGnHztSVSVpK9Itb21hNgNC4DUi54I29kAjgPxg61zwpniOPxD9ZGevs4JS-s7pd8hygiZ1_L_1nHAtpmPMnPi4DlG4RWNldASY4yL4y16gw7DlDWxzwn6of0dD-bjGDcOdfvc0AoUOJMN23qHyJ69LpP0Leqqlxvej9XaVrQcYuoOY-qMWhlzBnR5pwLrKUI6rl82XYd0ysGdSV-JuLKncWwjfGLGiRhQjJh6th6f7D_eWbgGWybTq_CeT9GyP1oA7J-ZUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
امین کاظمیان در حالی اولین بازی خود با پیراهن گل‌گهر را تجربه می‌کند که شماره ۱۰ گل‌گهر را بر تن کرده که نام تیکدری بر پشت پیراهن اوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/137000" target="_blank">📅 20:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136999">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⬇
⬇
بازگشت جنگ اعصاب به فوتبال
🔴
فوری - جواد نکونام به لیگ برتر برگشت
🤝
جواد نکونام پس از ساعت‌های طولانی مذاکره با باشگاه پیکان، به توافق نهایی با خودروسازان رسید تا پس از یک وقفه، دوباره به لیگ برتر برگردد و هدایت این تیم را برعهده بگیرد.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/136999" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136998">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2G5gWYdwp2orjf7ziaxXj7fHm0tWOYiz6EN2QHvL_lTDSNVcu7O8QuO_hvVvGmbCZubc3efNqSIaQq8OfKSnLU_lAbCkN3DtMdN2VEkaFmb_Ce9wvyPsjbxdWWbdZF2IMF5hTPkI73YZVNCFIEIMAiYPQpxeEAt_vb5urE__wEYdoHND5BC8jYQq03hPzaTk01Z9OBoSEuAEEGzUh9JJKpq-DFI-OZIxEbcHPp62A7x5Jy45PipRJaQ6-uNnvW7QMdjAdjpSTqJ1I7oYek4bnz3Xxt33XcCAFlR-sb-7zWaq0-UaUJgypRd6rJlqNAsrxtcw9Uy96Bmmu_0UpcoeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
در عربستان پول پارو کرد!
🇸🇦
کریستیانو رونالدو از زمان پیوستن به تیم النصر، مبلغ شگفت‌انگیز 625 میلیون یورو به عنوان حقوق و پاداش کسب کرده است.
😇
فوق ستاره پرتغالی در کمتر از چهار سال، ثروتی بی‌سابقه به دست آورده و او را به فوتبالیستی تبدیل کرد که بیشترین میزان درآمد را از قراردادهای خود در تاریخ این ورزش داشته است.
🟡
حقوق پایه (۳.۵ سال): ۵۹۵ میلیون یورو
🟡
پاداش برای ۱۲۹ گل: ۱۱ میلیون یورو
🟡
پاداش برای ۲۳ پاس گل: ۱ میلیون یورو
🟡
دو جایزه بهترین گلزن لیگ: ۸.۵ میلیون یورو
🟡
پاداش قهرمانی در لیگ: ۸.۵ میلیون یورو
⚡️
مجموع درآمد: تقریباً ۶۲۵ میلیون یورو
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/136998" target="_blank">📅 19:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136997">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4qax3dXtqWy_TDF6BmA8NRSIoF8IPDqkNA2jqeSEOOZtn3oXk0RwqoOw6H9_zZv0fyNm_S9_YEpjU3CkUwmGmfPZoBA7_YaQTX7YcYWrfRYP0wcQTZJEGAVGhFIt7zNPUsWgh75Ka2-09SJOZyscH59H51T9TcA2H6hcV7fwJBRf015c77yYUrSgkN8awth1qwn63A0LUqeXY9_7GJ8PpbbjKN8C_HxNtIT0l-KJ-sQo08F64QMis6X0WwwmmF08XkXye6rWW86A1BQD-_VR9qxMYllwTHuGiy4WFqkrsUeHStRwoMmTPrCe6Yqg1lD9gWd6pnV8-LWTxzMw9axRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👤
ممد مهتی امشب به اردوی پرسپولیس اضافه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/136997" target="_blank">📅 19:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136996">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌀
🌀
تارتار تو پست های دروازبان، دفاع راست ، دفاع چپ و دفاع وسط بازیکن میخواد/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/136996" target="_blank">📅 18:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136995">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⚡️
تارتار: حداقل به 4 خرید دیگر لازم داریم (دفاع چپ،دفاع میانی،گلر و مهاجم ) بازیکن می‌خوایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136995" target="_blank">📅 18:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136994">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
میرشاد ماجدی، رئیس هیئت فوتبال تهران:
◻️
مسئولیت استادیوم‌های تهران با من نیست. ورزشگاه‌های دستگردی و شهرقدس برای لیگ آماده هستند، اما درباره آزادی هنوز تصمیمی اعلام نشده است. زمان شروع مسابقات مشخص نیست و به وضعیت جنگ بستگی دارد.برگزاری منظم مسابقات،…</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/136994" target="_blank">📅 18:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136993">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⚡️
⚡️
پوریا لطیفی فر با نخستین تمرین، آمادگیش رو نشون داد طوری که خیلی ها جا خوردند. کلا هافبک با انرژی و دونده ای است که شاید بخشی از این خلا بازیساز رو بتونه پر کند
⚡️
⚡️
مهدی‌طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/136993" target="_blank">📅 18:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136992">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⚡️
⚡️
فوری/ دونالد ترامپ: در پاسخ به حملاتی که سپاه پاسداران به اردن کرده، ما ایران را به شدت مورد حمله قرار خواهیم داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/136992" target="_blank">📅 16:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136991">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⚡️
ترامپ: اگر توافق نشود، پل‌ها را ظرف دو ساعت و نیروگاه‌ها را در یک روز از بین می‌برم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/136991" target="_blank">📅 15:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136990">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔻
گل های محمدمهدی محبی خرید و ستاره جدید پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/SorkhTimes/136990" target="_blank">📅 15:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136988">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
🔴
🔴
باشگاه پرسپولیس با مبلغ ۵۰ میلیارد با وحید امیری تمدید کرده و حالا با توجه به جدایی و بدون اینکه بازی کنه، ۲۸ میلیارد میگیره و توافق می‌کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/136988" target="_blank">📅 15:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136987">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/136987" target="_blank">📅 15:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136986">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/136986" target="_blank">📅 15:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136985">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
🔴
🔴
🔴
توجه به پیوستن محمدرضا اخباری، احتمال بازگشت امیر رفیعی قوت گرفته است. برخلاف اخبار منتشره، باشگاه پرسپولیس، با احمد گوهری و سایر دروازه بان هایی که نام آن ها مطرح است مذاکره ای نداشته
🔴
رفیعی به مدیران پرسپولیس اعلام کرد توافقی جدا شود و باشگاه به او…</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/136985" target="_blank">📅 15:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136984">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
🔴
پوریا لطیفی فر ستاره 22 ساله تیم‌گل‌گهر با عقد قرار دادی چهار ساله رسما به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136984" target="_blank">📅 15:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136983">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">💠
💠
💠
✅
پرونده ایری و طاهری به حدی جنجالی و پرحاشیه شده که مدیران پرسپولیس فعلا هیچ رغبتی به توضیح ندارند
🌀
🌀
عصبانیت هواداران هم مزید بر علت شده تا برخی از مدیران ترجیح دهند اظهارنظری نداشته باشند.
🌀
🌀
وضعیت به گونه ای است که حتی جذب محبی هم موجب ارامش هواداران…</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/136983" target="_blank">📅 14:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136982">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
امیر روستایی مهاجم سابق پرسپولیس به سترة بحرین پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/136982" target="_blank">📅 14:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136981">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
شهاب زندی مدیرعامل نساجی:  با استقلال درحال مذاکره‌ایم، با توجه به بسته بودن پنجره شون اگه بر سر مباحث مالی به توافق برسیم این دو بازیکن آینده‌دار نیم‌فصل راهی استقلال میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136981" target="_blank">📅 14:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136980">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oovRSBaCE6fQqCjpkyTCrDWWOmzm-s7iXLCyRPb1Xh6WEXIqhW8vB_TZBbZ0m4h4BHU40RILoemrc_3F0UMvlKpWB2wtrD-gcLnmuFEgHhKhwMJZQnRsmZJtDptJ9Cwy4BPhnOsQQGrv4OL8fv-FRGRIX72aqVBYodOjznPF0lx937re46qH336sosma_y-JaQC3jHXjkjZ4eglDQ0mgYRH8mDoO5rbnWGhbTyoGp-Gu5sWmoRrzQK3fx-nTs4_q1v4xuD7EEW8iv0pnGZ-NORsfO6RdgqF7OLxyz9kcNP4K3OLp8gZyTAbyW2ep2zCEv5aEKyeKnoOOx1tzGfzH8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرحله حذفی لیگ ملت‌های والیبال از راه رسید!
🔴
نبردی حساس و تماشایی بین ترکیه و اسلوونی در پیش است؛ جایی که هر دو تیم با تکیه بر قدرت سرویس، دفاع روی تور و بازی تیمی، برای کسب برتری و نزدیک‌تر شدن به هدف خود به میدان می‌روند. دیداری که می‌تواند با رقابتی نزدیک و ست‌های نفس‌گیر همراه باشد.
🏐
اوج هیجان همراه با وینکوبت، چهارشنبه ساعت ۱۰:۳۰ دوتیم ترکیه
🇹🇷
-
🇸🇮
اسلوونی به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی بازی‌های لیگ‌ملت‌های والیبال با بیشترین آپشن ممکن همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/136980" target="_blank">📅 13:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136979">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
علی بازگشا، سخنگوی باشگاه پرسپولیس: «اینکه پیشنهادی آمده بی‌اطلاعم، اما ما می‌خواهیم اورونوف و سرگیف را حفظ کنیم.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/136979" target="_blank">📅 11:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136978">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔄
🔄
باشگاه نساجی: دانیال ایری و کسری طاهری رو دیگر به پرسپولیس نمیدیم. بانک شهر ما رو سرکار گذاشت. اگه با استقلال توافق کنیم اونارو به استقلال میفروشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/136978" target="_blank">📅 11:54 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
