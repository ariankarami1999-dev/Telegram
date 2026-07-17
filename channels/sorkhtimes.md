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
<img src="https://cdn4.telesco.pe/file/e8zjN7w8JGJmu-poBtrnMpWKpmwWog1meAAtnsUL6k1IMeQ0Cu3hUnYPL9n9b5sICKrH45WZZtowkTJ9aK03Aw3MNyNv43NRcIojLHQnRip_Qea52HdDg6E190xB4JHxhS4dohhosyv7-B3V_-Xcq2ATnjDMxarkmYCi-bMBFJneu6J0J5ONZk9p_9KEPtgXJYMWHG5E3fe2JmXIw6Hm6g_zd_ck6w2s7gVGJLWt28k8dMTcqMZM25p6MdfzzP0VWsLk1KyTs24TsngWq5uSNJveD_MBvqO-lX0JTqDpmGEbB5T3_Qxb9zc31gphFDKfid_PjoZCcWmCrd6kLVEwlw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 20:31:51</div>
<hr>

<div class="tg-post" id="msg-136031">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SorkhTimes/136031" target="_blank">📅 19:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136030">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
اولویت در دفاع چپ با میلاد محمدی است.او گفته اول طلبم را بدهید بعد تمدید.باشگاه هم گفته کارها همزمان انجام خواهد شد.محمدی هنوز توافق و امضا نکرده است.
🔴
الترناتیو میلاد محمدی رزاق پور از  فولاد است/قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SorkhTimes/136030" target="_blank">📅 19:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136029">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
فرهیختگان:
🔴
باشگاه تراکتور همزمان با علیپور و مغانلو درحال مذاکره است
🔴
شهریار به مراحل نهایی رسیده اما با علیپور بر سر مبلغ قرارداد تفاهم ندارد،
🔴
علیپور درخواست قرارداد بیش از 100 میلیارد تومان از باشگاه کرده که فعلا مورد پذیرش مدیران پرسپولیس قرار…</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/136029" target="_blank">📅 18:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136028">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووری از تسنیم
⏺
محمدرضا اخباری در آستانه عقد قرارداد با پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/136028" target="_blank">📅 18:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136027">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
#شایعات
‼️
با وجود توافق میلاد محمدی با پرسپولیس، مخالفت همسرش با زندگی در ایران مانع امضای قرارداد شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/136027" target="_blank">📅 18:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136026">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
مهدی تارتار پس از تمرین روز گذشته نام کاظمیان را در لیست مازاد قرار داد و قرار است کاظمیان فردا قراردادش را با پرسپولیس فسخ کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/136026" target="_blank">📅 18:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136025">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
🔹
تارتار کاظمیان رو گذاشت لیست مازاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/136025" target="_blank">📅 18:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136024">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">💢
💢
💢
پرسپولیس در حال مذاکره با محمدرضا اخباری برای گلر دوم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/136024" target="_blank">📅 17:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136023">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hseZSkSQLX-z2_JVyUw8MTdDWCtwH-OmEM8YxtX01XDnBxEdKcLAvD6NZcCybpCSh5t-fvsHyzpeqsviN93JqP8319wx_EDtNcABcJ1iY293k_5oXVK92tcPY8C5jRufWZqezrvPO7QruuswPGMYbPM85kdXdSoxMQ6F_wA6kZL0HQgeOS6ZDqkOf5bxwtv0EzLLPfoJt__Jn258uAfv3XzAFli5_WKNIF_DxemE_Vwv7dW5YU8sJhgw6FmaiTweQ4qCKqXURo8cnRy6okruaiBlcR49ABO1YryP2x9mM8n7rthM4g327_mWuqVw9doNlAC-22kA6F1sAUM2hXFc6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
رسمی؛ با توجه به پیروزی ژاپن برابر بلژیک بقا ایران در لیگ ملتها والیبال قطعی شد و حتی اگر دو بازی آخر خودشو ببازه سقوط نخواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/136023" target="_blank">📅 17:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136022">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">💢
کاظمیان + رفیعی میرن گل‌گهر پوریا لطیفی فر میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/136022" target="_blank">📅 17:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136021">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">💢
کاظمیان + رفیعی میرن گل‌گهر پوریا لطیفی فر میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/136021" target="_blank">📅 16:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136020">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❗️
❗️
جذب لطیفی فر کنسل شده است / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/136020" target="_blank">📅 16:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136019">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
تسنیم : سامان قدوس در لیست خرید پرسپولیس نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/136019" target="_blank">📅 16:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136018">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKkUVEvPzRmFtDlmGolsrb2biz7JOz-0AL-udBxX24V6PBFaVIxSuutiE2muOCQjCNV6IHHz-nVS-m5wMeMiFzyxWVB53OL9WMS03uXjHWidfsBfbrf9Uhm9bgFTqPX6DiVHvvq1ZoLg6N4RA5V3fXkrYbCiB6GNIxdRAf_6odxJdqr2JG6xFpZyOWaU0mBXmeYc1SgewpSshUGQExmf00FhiarWNdkJr3WMErC0r1npOkOpUrQuNqeG8g4vgZJDehPRsBca7OKMOFTOAhrPtyKaeKsmTjFvP0m2jOI7YpNyAGJmdIRFgWedXLgU8Zhwtb3k8NuiMv2pOVUuVupH_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تو 24 ساعت اخیر سرچ «لغو عضویت جانفدا» بیش از 5 هزار درصد افزایش داشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/136018" target="_blank">📅 16:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136017">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
تسنیم : سامان قدوس در لیست خرید پرسپولیس نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/136017" target="_blank">📅 15:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136016">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
❗️
اتحاد کلبا رقم‌ رضایت‌‌نامه سامان قدوس رو 500 هزار دلار تعیین کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/136016" target="_blank">📅 15:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136015">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
با جدایی سرلک، محمودی خواهان شماره ۱۰ برای فصل بعد شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136015" target="_blank">📅 13:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136014">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
✅
سامان قدوس در فهرست نقل‌وانتقالات باشگاه پرسپولیس قرار دارد و سرخپوشان به دنبال جذب او برای پست شماره ۱۰ و جایگزینی با رضا شکاری هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/136014" target="_blank">📅 13:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136013">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
چهارشنبه هم گذشت و اورونوف برنگشت !
❗️
روزهای پایانی هفته گذشته اعلام شد اوستون اورونوف ۲۴ تیر ماه به تهران برمی‌گردد اما هنوز خبری از این بازیکن ازبک نشده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/136013" target="_blank">📅 13:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136012">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
فوووووووووووری
😀
کانال 14 اسراییل: پل و راه اهن و فرودگاه و پادگان ها در جنوب ایران بمباران میشوند تا جنوب تسخیر شود. بزودی نیروهای امریکا وارد ایران میشوند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136012" target="_blank">📅 13:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136011">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
یا تمدید یا خداحافظی!!!  فرهیختگان: میلاد محمدی باید سریعاً تصمیم بگیره قراردادش رو تمدید کنه یا بره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/136011" target="_blank">📅 13:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136010">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
تیم پرسپولیس که قصد داشت فردا برای اردوی اماده‌سازی راهی شهر ارزروم ترکیه شود، با یک هفته تاخیر اردوی خارجی خود را برگزار خواهد کرد.
🔴
🔴
پرسپولیس روز ۳۱ تیر ماه برای این اردو تهران را به مقصد ارزروم ترک خواهد کرد و احتمالا دو هفته‌ای در این اردوی خارجی حضور…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/136010" target="_blank">📅 13:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136009">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136009" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">💛
آپدیت جدید اپلیکیشن اندروید MelBet
❗️
🎁
کد هدیه 100 دلاری:
giftcodeir
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
آموزش ثبت نام و واریز
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را فارسی کنید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/136009" target="_blank">📅 13:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136008">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">💛
چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت
💰
هنگام ثبت‌نام با وارد کردن کد هدیه giftcodeir بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/136008" target="_blank">📅 13:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136007">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djP-ubPkVyE_qHxpq-iGqd6xgHp2IYVCsoNJPqB4oDxesqn7j5LhDYigyWTRC7tTxALNdipSUcyX_QGZtFEIekMIBOR4XVZd7TEhd43FI_0lEG0rgnJ8_OZodOaeVknOi9TAJoNXUPZ0tTh76VCRx3B76wGAACAqaCKVCYhvQ5MTG05YK-4PPEKpHCWIxwOZY3Y_Jowf5AcIaGaOQi06Q414HRdML-Kz35FipvdL8idv-5XFbT8i6WqPgNd8eD60dqfanAnvQ5_Pz8VWhsGaLSZFRqvjHBfDu0K9y-ha_XUvh2sfYK0n-cmUQxqoiYnx3smyYSvYIMb-8Cd2Yp0gRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
چرا هیچ خبری از این بنده خدا نمیاد؟
❗️
حتی باشگاه پوستر خداحافظیم نزد براش
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136007" target="_blank">📅 12:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136006">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7N44HXqF-ajL0GSSD5HBW3Y1a0ufa4d3mhk5_cjIk9e2HavhkZMvRnoxw1Em59cOosrzb2SB5qXCq54NZylqDBIeYRTC10SuzswSnSGOgtdZo3wwtLVu2Y-Svdfr0ffDvFZFiSJocQSms5MOALN2je9KmffCqHuEZUDy2d9eI3YfwMQCLGR8LQVbmHJTEqhxTeg5O1zzcrVymIi_rjmzeuYHk4jVPrWr38LlU-xJnXaetSLf1xmw9GmZvus_ZTooGYXKkD1S3z0viADOxbehqnIGzAg7Q9PEna-bbmE8H9-GzCQHh1VPsNCqwUZOAlQ0U4-KRYEIRr8EcYcVyrz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری
/ فرهیختگان
🔴
با توجه به بندی که در قرارداد آسانی با استقلال وجود داره پرونده حضور این بازیکن در تیم های دیگر در لیگ ایران منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/136006" target="_blank">📅 12:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136005">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
ابوالفضل قاسمی به پرسپولیس پیوست
❌
#پسر_پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/136005" target="_blank">📅 12:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136004">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVvYS_f_tznA3I1LhX5GuVp61JIhWIobVei4J6E_wNC9dKhhcI2CwInx_VF4lnCnBXzop1eVNP0dcZXqvPdU88Q7UgoIlFU6D8JWT6opm6t7a-hBJRUTV71c4h5bq9mdH38jvWkq6LBcAjK3naplLayqDhIA_nE0s8kr5_w3HamH0x0M28KKlOslqwq3n1QLxhhl--mPonWwYCURwsYEzt2pxkyOj1qS453p9JHUQzmSAZmt0HV0yS8APmJ9hdwyrSFk7DTU6qg-S1E0-U-WpHNkvothqMXS7SwNCkcFJ_aILcJtz4LmzKjuy0LH0Nn2HxQzgDwZCAAnkza8cAU1ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابوالفضل قاسمی به پرسپولیس پیوست
❌
#پسر_پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/136004" target="_blank">📅 11:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136003">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
برای این نتایج ۱۴۰ میلیارد پاداش گرفت؛ واکاوی پاداش تعیین‌شده برای اعضای تیم ملی بابت راه‌یابی به جام جهانی؛ رقم قلعه‌نویی، ۴/۵ برابر قراردادش!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136003" target="_blank">📅 11:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136002">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
برای این نتایج ۱۴۰ میلیارد پاداش گرفت؛ واکاوی پاداش تعیین‌شده برای اعضای تیم ملی بابت راه‌یابی به جام جهانی؛ رقم قلعه‌نویی، ۴/۵ برابر قراردادش!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/136002" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136001">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
✅
فوری از سپهر خرمی: پوریا لطیفی فر به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136001" target="_blank">📅 11:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136000">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
فوووووووووووری
😀
کانال 14 اسراییل: پل و راه اهن و فرودگاه و پادگان ها در جنوب ایران بمباران میشوند تا جنوب تسخیر شود. بزودی نیروهای امریکا وارد ایران میشوند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/136000" target="_blank">📅 10:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135999">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
✅
باشگاه همچنان موفق به فسخ توافقی با بیفوما و گرا نشده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135999" target="_blank">📅 10:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135998">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
فوری از سپهر خرمی: دنیل گرا به طور قطع از پرسپولیس جدا میشه مگر اینکه به لحاظ مالی به توافق نرسن چون سلطان یه فصل دیگه قرارداد داره!
🔴
🔴
البته به نفعشه یه پولی بگیره و بره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/135998" target="_blank">📅 10:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135996">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">📌
۴۰۰ هزار دلار کمتر از ایری برامون تموم‌ شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/135996" target="_blank">📅 10:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135995">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
احتمال خیلی زیاد امیر رضا رفیعی به علاوه 60 میلیارد با لطیفی فر معاوضه میشه و توافقات انجام شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/135995" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135994">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXu0zze-hcq5P74IwKe4cE4U-X6lFrPiV1nJwEJx6Ns0-edfGVSOyACIS7-u2Bz3DRplYWw3YMv3NR23stjz2OJIxvl-q8nrXQtmvL27Cnt5gk0ivyOjKS4A2h79taG3SzVvbSdd56KDb_RboqiNNF8lKashbpHaDVVrhw2gBLTWz5v8cAehiGn2qzbI5d7SWUEIo9FFYMmXIABXrnxrWibtO8xKdy5CMeEHhSbr7KKVW09J3Q1xP9BJOUwzS-M0POri6wxSZ48rJ0YFZbkXb8Qfs3ABpXUMoY2nZ2bpepzVK1sxl299XRXisgZhVzyyz_RCpb5h6FkItmGB6suAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
برج ۸۰ متری کنترل دریایی چابهار در طی حملات آمریکا بطور کامل نابود شد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/135994" target="_blank">📅 09:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135993">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/135993" target="_blank">📅 09:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135992">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
داورهای بازی فینال و رده‌بندی جام جهانی مشخص شدند و علیرضا فغانی در هیچکدام از این دو دیدار حضور ندارد.
❌
بر اساس اعلام فیفا، اسلاوکو وینچیچ از اسلوونی دیدار فینال جام جهانی بین اسپانیا و آرژانتین را قضاوت خواهد کرد.
✅
همچنین ژسوس والنزوئلا از ونزوئلا،…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135992" target="_blank">📅 08:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135991">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔺
فیفا قضاوت دیدار فینال جام جهانی ۲۰۲۶ میان تیم‌های ملی اسپانیا و آرژانتین را به علیرضا فغانی سپرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135991" target="_blank">📅 08:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135990">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4GXogsoK3ZA8e5n7hdc40ZqAXGGFQNy8qCP4-TScOhonr6G4XO-idWe0KwX823VAJnlCkdSb4T6OYECMjyCxIPOJCg7P4I8rxrffhJql-apS8kqJaJCm2oqo34UwZN8xaI69Nm884rFhNQtktzTYdMEGZ6eV2V3gIxQYKmCLG9D6elFpwM--Ds5dgvlaea0-H4qD3oGZKuFjISMrnZrsRErC86Y7PgOXxr0rmHJ4oUmWUx43UBNiyRfhOIhgNTx-nr-D0uSBGylBQsh_VWPUa7k38yoIhGVL4kEyg3IhNdSzmRMIjcBG1bScLUihFWM3xTdgKvvjA1TeWK2wur2PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس ممکنه زندگی نده، ولی
شادی میده
عشق میده
اینه داستان سرخ...
❤️
‌
سلام صبح بخیر پرسپولیسیها؛
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/135990" target="_blank">📅 08:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135989">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135989" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/135989" target="_blank">📅 01:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135988">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGhNcUId5ZBBqexty8ohXSu3lJzkntAzFLSZIm4BK9rFDWR0Dkr0Z_yue0gPNzaq7Wq_CYW1JGGJyUfLkhMamkkUR1m2HBGPUP9l2n8lUexbbT6pt6Gt7CzFTno3qBQfIPbxVlt39E2Jkp-Dq9fMU6du8IH7dURmVl0ek247Y98n9tmNPwQQ74ODimjtgIbB59NTyqG3wI41XhynZIKnV7brwiUr-jnES7LZy75tVcvO8fffx4bPVRCfmOZTr2DMI5metv_OGbXIjdARI7TzCAsrlwlTU5ZRLmnbUy7j1B6Psica5i3th_74OwmuL_-njrFIsfHPU2MwGi16A120Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135988" target="_blank">📅 01:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135987">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135987" target="_blank">📅 00:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135986">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135986" target="_blank">📅 00:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135985">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
کوشکی و اسلامی توسط ترنسفرمارکت بازیکن آزاد اعلام شدند
🔴
از طرفی ایجنت هر ۲ بازیکن با ایجنت جلالی یکیه
👀
نظرتونه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/135985" target="_blank">📅 00:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135984">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/135984" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135983">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
✅
یه خبر نصف شبی فوری، شنیده ها:
🔴
برخی از کارشناسان حقوقی معتبر به باشگاه اطلاع دادن کسری طاهری میتونه برای پرسپولیس بازی کنه و باشگاه داره مجدد واسه جذبش تلاش میکنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/135983" target="_blank">📅 00:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135982">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
✅
خبرگزاری تسنیم : آمریکا رسما حمله به زیرساخت‌های ایرانو آغاز کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135982" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135981">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
آمریکا پل کهورستان بندر عباس را هدف قرار داد.
🔴
این پل، بندرعباس رو به شهرستان بندر خمیر و سپس به بندرلنگه و سایر شهرهای غرب استان متصل میکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135981" target="_blank">📅 00:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135980">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
آمریکا پل کهورستان بندر عباس را هدف قرار داد.
🔴
این پل، بندرعباس رو به شهرستان بندر خمیر و سپس به بندرلنگه و سایر شهرهای غرب استان متصل میکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135980" target="_blank">📅 00:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135979">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
آمریکا پل ارتباطی بندرعباس و شیراز در جنوب ایران را هدف قرار داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135979" target="_blank">📅 00:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135978">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
✅
خبرگزاری تسنیم : آمریکا رسما حمله به زیرساخت‌های ایرانو آغاز کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135978" target="_blank">📅 00:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135977">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❗️
فووووووووووووووووری
⏺
ارتش اسراییل: آمریکا در حال نابودی زیرساخت های جنوب ایران است تا به راحتی به آنها حمله زمینی کند و سپس به مرکز ایران برسد
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135977" target="_blank">📅 00:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135976">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
🚨
حملات در جنوب کشور شروع شده...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135976" target="_blank">📅 00:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135975">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
🔴
موج جدید حملات سنگین آمریکا به جنوب کشور آغاز شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135975" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135974">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdfkI8JWdxtYNrjYZo2e7fgwdIb02k7nm7SwTtelV2U6sA_uChljTlvnA_VuvwolKR13muapgZvPjy3qMQWFITvqwmZAV-hknHK8fIFQVMsFsFg0n6NWtLWaKB6Ck_x8TDkpIhOR8u7GfBpCvptl1W6BnR4Bwed7VBlxy51QrTuIN1ALIL2zgri1x-hdCaEilJ66uFk5wFol_LYzbHJDIQaEH691rnrQjTfwCHZoXJMZQjdLrmVv55W4yXz5KgWF1PSj5ja_3qeYGutbLfzQNHD8ymJwZ5EmwaC5EFhhc4eu3Uy5IDR75mIB3KTSA8Ijd2I8uOUjXdvk9nBP0bKZjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حضور رضا جباری در تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135974" target="_blank">📅 23:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135973">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOnIvU6LMgWq1cC4Dn_-TGsXA647shPut6WKJPpq4e9DptqyiTrwdiymVomDDkurCzukjt4E29tC1L_aosxsM_mnhcP_44pRBAyCa0Phy0t_J3C4jP_7vLH_NfDZIi1gq4J6WoAKENoXZgz0V5oAI0ZAgHKmJ7YesuZWd3I7ZxPC5TmwAwEXuHPbK9iAZhS4NXhBuKnozfUwnO7upvQSyhJIsMRbr1gGxmCyFNak0cMzcF8vvek-r-ge739NpWvkBZrOXvCByMUwtRYQ_16Wn0BjGcIkrBsLuom3g-B1qlujEXkFOFl01HKQGpf99-mCIhcY8_Mb8KwiFPQW2t7utQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش تصویری از تمرین امروز پرسپولیس
با حضور علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135973" target="_blank">📅 22:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135972">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
فرهیختگان:
✅
وحید امیری 38 ساله به پرسپولیس پیوست و کاپیتان اول پرسپولیس شد!
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/135972" target="_blank">📅 22:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135971">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESqGW-qf4iCB74uOe19qNGc-C3qUGL0s7Sb97spmH3-72R641vu0Mv58DzFxtDv4nIwFm5B3UryQo27lonUDrukVsUrG_Gn-CyBXfZmN4L4fjeMi_pLonUejNLHFTAhRF9qfIPahGEHWqJKpq38LCbgqYprUrT8sEyfFAU9xXw2NRCGX-w3J5cahaQzSvNVTItm5Ihm5iezsdks9Oy0DfotxnZI1v-AGmVQFHGz7wFoTny8DqLNgYQNeZEpuoESOc-zRjWtbPgUe-lpxti2HmDtXIdiaImw-Kz_v9XBB0jZlQqXpb3tK8YlSJIh8Ej3EGA5zaco8fyWJDeng65p9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرهیختگان:
✅
وحید امیری 38 ساله به پرسپولیس پیوست و کاپیتان اول پرسپولیس شد!
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135971" target="_blank">📅 22:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135970">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
صنعت نفت آبادان با برتری 2 بر 0 برابر نیروی زمینی در رده سوم جدول رده بندی ایستاد و حریف مس رفسنجان در دیدار پلی آف لیگ برتر شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/135970" target="_blank">📅 22:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135969">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">#شفاف_سازی
🫦
📌
ببینید دوستان لطفا به مطالب جهت دهی شده توجهی نکنید این مطالب رو رفقای اقای زندی میدن بیرون که باشگاه رو تحت فشار بزارن، همونطور که چند روز پیش گفتم و امروز هم اشاره کردم باشگاه خوب نساجی نقدا پول رضایت نامه ایری و طاهری رو پرداخت کرده که بتونن…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135969" target="_blank">📅 22:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135968">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">#شفاف_سازی
🫦
📌
ببینید دوستان لطفا به مطالب جهت دهی شده توجهی نکنید این مطالب رو رفقای اقای زندی میدن بیرون که باشگاه رو تحت فشار بزارن، همونطور که چند روز پیش گفتم و امروز هم اشاره کردم باشگاه خوب نساجی نقدا پول رضایت نامه ایری و طاهری رو پرداخت کرده که بتونن با دو سه برابر پرداختی شون به تیم های دیگه بفروشن این دوتا بازیکن رو…الان که باشگاه با علیپور تمدید کرده و زارع رو جذب کرده،مدیران نساجی الان زیرش زاییدن چون سپاهان سقف قراردادش ۴۵ میلیارد هست، استقلال بخره هم الان به کارش نمیاد، فولاد هم بودجش در حد سپاهانه… جز ما و استقلال کسی دنبال ایری و طاهری نبود که بخاد پول خوب بده الان به گوه خوردن افتادن مدیران شون ولی با این تفاوت که الان افتادن تو فضای مجازی و دارن کصشر تلاوت میکنن تا هجمه وارد کنن، بگن ما موز میدادیم کیلویی ۳۰۰ حدادی خیار خرید کیلویی ۲۰۰ اقایون جای این لاشی بازی ها بازیکن رو به قیمت بفروشید که اینجوری قهوه ای نشید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135968" target="_blank">📅 22:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135967">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❗️
قرارداد علی علیپور تمدید شد
❌
قرارداد علی علیپور، مهاجم باسابقه و ملی‌پوش پرسپولیس، پس از توافق با دکتر پیمان حدادی، مدیرعامل باشگاه، به مدت یک فصل دیگر تمدید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135967" target="_blank">📅 20:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135966">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jf8Wm3cGHk0MI6NaX0yI1WpsoSLXMbN9RktTZy3Ripe_m6WgSlpqJeQ2o354ZRmGHdGkldhS7dYirmAK4bXrYy1G_Cevldq7yp8UJwKkxUMrT9BVebhj19XJQBBtaIt9rnwVxV_VHwDZL3S-Bcz2kSa8TfajBN8GFkZKF2sD0Qs2bfVRZ34_iIiTddk2tEkr68Reu3H1cE_xDVmYXibSosyPBdy6Bdwn59uwXeRwtSBX-l2LKxa0LtxKyfCPhfnFbirIyE68aEWF4nLeFkovSkQxH5Vfl1dhmv3ZZ-mirB3tWzClONWGbx0u7E7P-_1Hbe10BKwdtx5Z5bsA0I4hWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه پاکستانی
😀
اکسپرس‌تریبیون:
❌
بعد از از بین رفتن تفاهم‌نامه بین آمریکا و ایران، پاکستان تلاش‌های خودشو برای کاهش تنش‌ها و ایجاد صلح بین این دو کشور متوقف کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135966" target="_blank">📅 20:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135965">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135965" target="_blank">📅 20:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135964">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
@ARON_TIP
@ARON_TIP</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135964" target="_blank">📅 20:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135963">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfnWkG0UidpvrlOfJDT7lL3C2abg-ZANHI7bkbYnEsNNRRaI8SX8WnLoanZChV07kodAf7yetgQ7gqhvoKGnuj_SuigTujd3XfCrrcsVPk16toE8kQdf5Ra8mEfQ8gCKNMbOL4Yfvqd1-0g5tBjGblc9DFv3SgBGOSHqKDyPMK_-oEsUtrgVgcRurIflwK8GFeP6yVBPqr2iXvlgdja57uP22p44jHkS5tNJTaeXex5GvJOQXyt19kb2EALb5ZnEhlkESspJkwhlK-AfTvmyS6So0t57rKFQKfcJkgHZpUNv3ypfeYbtXH-31cWNHr0o4aRJH_CQFp4TIyMqPWgbRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@aron_tip
@aron_tip
@aron_tip
@aron_tip
@aron_tip
@aron_tip</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135963" target="_blank">📅 20:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135962">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obfGDIgsUyi_5Z_mK8CBwKpumg00BD8GAztMGGmfmvOjnH-q7IEvPnv-qnz4blv4X32OA3Z8Y9anFlXGtg2FfEKreOAENLxpTV9z8pWRjbkhY35I8fdgXRzXp4fDAfGxDBpTylCP9dnjCIi4zcAZ9WRrB7t_-L6cpxQL3cHl5YJP3cNNpyDTYT7757QMzThpjEftWcWvfP4V4j1k5jQLNsKfnDCmdzsjQRAj3sSSDIJ0-5t4VLqQgdBfDGgNfmwMBqKoYejQFvTGCoOqSHmjwC9i8EPbh-yLSz4OJm8oUB_A1BBuaGgSLKClU-Itt3OsJTymj3S8a5V34U6O5BYFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تیم ملی والیبال امروز تو یه بازی جذاب 3-2 مقابل آلمان پیروز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135962" target="_blank">📅 20:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135961">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
❗️
فووووووووری
❌
فرهیختگان : اگر میلاد محمدی با باشگاه تمدید نکنه ، مدیران باشگاه از مدافع چپ جوونی که با اون به توافق نهایی رسیده‌اند ، رونمایی خواهند کرد
🔴
گفته می‌شود تمام اقدامات نهایی خرید جدید تیم انجام شده و این انتقال برای نهایی شدن تنها به یک امضا…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135961" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135960">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e071e1ff46.mp4?token=B8eG4mhb300iXezVwD1eURbMZQsoH2wYnXiezzNAJQS9rm7RVwYqzS0jTmoOXMfzgIce_WBTLjc60NhucVHyO81sUwnp7xl4guArF1Zp9SqXn7NvwBOABqMr9kpi04cRGpVVEqQYnENKXpeFcjmkbmSmQc5VetkGZOmSEqfUVskwXae2wyRU09qxsDOJtl2BXvOcp0rse0h95M0XaIuUeY3xwBDo-8asaYzHmT1bBbXZaD5NvY85gdVri42zBp8HY-pnJCGAEpsrlXo3d_lqMGdGLV2CbVyqQNLfnFOAPTGu9TBHM-Gky6nUWDz_pngWNSg5DSbOmg_Lvig5WN5YlkFYHW87bTDxyR1DqHVcDEARZLsxydk-GawQamygkXfWMISSG-o0oZOnFNOLovstRBWsMNFqe7YkOL1g9ympwyYcB63uBn88FqEQVCPrMWh0KM34dofdJZ2ZAfLUqlHrnL_9D28IDsFlmlTbceA22O0Fv7B8pEtMVVVnbOjJ6usuJoqxtFgFbUq-8jZ7uH24XuOIEBr0N8lXHC3W6GPudN5GDYyrLzZOtWihHB-vHSEq7_Be3wvziaFCzRa9HdJK2SCaPRSs9iLGWpZE31mRLM2Ir-EBHJJezIc-mpHUQqApauaGEL40Rf-nLJkj-wnHAbzhyNBqWwLiMWCZtvzXo3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e071e1ff46.mp4?token=B8eG4mhb300iXezVwD1eURbMZQsoH2wYnXiezzNAJQS9rm7RVwYqzS0jTmoOXMfzgIce_WBTLjc60NhucVHyO81sUwnp7xl4guArF1Zp9SqXn7NvwBOABqMr9kpi04cRGpVVEqQYnENKXpeFcjmkbmSmQc5VetkGZOmSEqfUVskwXae2wyRU09qxsDOJtl2BXvOcp0rse0h95M0XaIuUeY3xwBDo-8asaYzHmT1bBbXZaD5NvY85gdVri42zBp8HY-pnJCGAEpsrlXo3d_lqMGdGLV2CbVyqQNLfnFOAPTGu9TBHM-Gky6nUWDz_pngWNSg5DSbOmg_Lvig5WN5YlkFYHW87bTDxyR1DqHVcDEARZLsxydk-GawQamygkXfWMISSG-o0oZOnFNOLovstRBWsMNFqe7YkOL1g9ympwyYcB63uBn88FqEQVCPrMWh0KM34dofdJZ2ZAfLUqlHrnL_9D28IDsFlmlTbceA22O0Fv7B8pEtMVVVnbOjJ6usuJoqxtFgFbUq-8jZ7uH24XuOIEBr0N8lXHC3W6GPudN5GDYyrLzZOtWihHB-vHSEq7_Be3wvziaFCzRa9HdJK2SCaPRSs9iLGWpZE31mRLM2Ir-EBHJJezIc-mpHUQqApauaGEL40Rf-nLJkj-wnHAbzhyNBqWwLiMWCZtvzXo3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل چند ماه قبل پویا پورعلی به پرسپولیس با پیراهن گل‌گهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135960" target="_blank">📅 19:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135959">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664e6b20c6.mp4?token=BhFonQ3HyRC8upBi_-eNtD_B43iJYcfBj95wibFItz9dVjTuCyzdMEoq7q6kbfISotDqO1T7egYQfnAGuSG3tVhpYnqLo3K69zKPUi9sDNu3kAOUUHxJFhTo1pvC_zMOWv4u5l26PWrzyb9QwjlEvCaATPmP2Cor3Edokbs-lbxrIP5MD3Vscghc8QcfZNLdxiZ1DER5DXGsKzb1osx97Cmj4NEjkB1ps8-sxlXoVWG0VfA8o4CQMvyT8NSt-sRxtyJ6tNXbzvi9gy2mhxv7ufje-31nQODeaWhrbTi8VDlEOnNGwQVuhwpY0EglZKP0XhdoA1-DZW8dBS9JLs1gMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664e6b20c6.mp4?token=BhFonQ3HyRC8upBi_-eNtD_B43iJYcfBj95wibFItz9dVjTuCyzdMEoq7q6kbfISotDqO1T7egYQfnAGuSG3tVhpYnqLo3K69zKPUi9sDNu3kAOUUHxJFhTo1pvC_zMOWv4u5l26PWrzyb9QwjlEvCaATPmP2Cor3Edokbs-lbxrIP5MD3Vscghc8QcfZNLdxiZ1DER5DXGsKzb1osx97Cmj4NEjkB1ps8-sxlXoVWG0VfA8o4CQMvyT8NSt-sRxtyJ6tNXbzvi9gy2mhxv7ufje-31nQODeaWhrbTi8VDlEOnNGwQVuhwpY0EglZKP0XhdoA1-DZW8dBS9JLs1gMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب علیرضا، پسر نابینای ایرانی اينجوری با گل آرژانتین ذوق کرد
❤️
🔴
گزارشگر اختصاصی هم داره که پدرشه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/135959" target="_blank">📅 19:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135958">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
❗️
لیست تیم ملی امید اعلام شد.
❌
در این لیست 4 بازیکن از پرسپولیس به تیم ملی امید دعوت شدند.
🔴
امیرحسین محمودی
🔴
علیرضا همایی فرد
🔴
سهیل صحرایی
🔴
فرزین معامله گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135958" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135957">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
اردوی خارجی پرسپولیس در آستانه لغو
❗️
❗️
در حالی که تیم فوتبال پرسپولیس قصد دارد روز جمعه تهران را به مقصد ارزروم ترک کند تا یک اردوی دو هفته‌ای را در مسیر آماده‌سازی خود داشته باشد، هنوز شورای برونمرزی وزارت ورزش مجوزهای لازم برای برگزاری این اردو را صادر…</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/135957" target="_blank">📅 18:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135956">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
ورزش سه: تارتار به وحید امیری پیشنهاد داده به عنوان دستیار و مربی به کادرفنی پرسپولیس اضافه بشه؛ اما امیری فعلا دلش میخواد بازی کنه و دیروزم داخل ترکیب پرسپولیس قرار گرفت تا خودشو به تارتار ثابت کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/135956" target="_blank">📅 18:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135955">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eda321934.mp4?token=LkVMj_lXNWnL3CT-itSmeXEzNRjeovAh5lES8KcArcV_V6R7ISqBn2b-Ux9xSJsHaDI-BKiSfdQDmZFVUC3LHIr2h8Nv7wxWXAU0f96BfTTz9rUmZKYvUB_SmmJl_4YPw01aHACsuepgGm2IQRFNC_abCKbGafJRPlwqimNlLPkHtB-At3xzkAx1wNCRQr_bHAbDg0Miw7sBC5XJ8w3UJ07rK-RI8Atvinjj5h3wSDWcZqSIc0zQsh4FM6Jks2YfdDsisp1PAt4uEVvpdXswpu7D-CCTIp-Kaouf8zIKX5DRswVBmU4asZC9W8FTNMQ48jJouG1o0gSVY207_wx7gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eda321934.mp4?token=LkVMj_lXNWnL3CT-itSmeXEzNRjeovAh5lES8KcArcV_V6R7ISqBn2b-Ux9xSJsHaDI-BKiSfdQDmZFVUC3LHIr2h8Nv7wxWXAU0f96BfTTz9rUmZKYvUB_SmmJl_4YPw01aHACsuepgGm2IQRFNC_abCKbGafJRPlwqimNlLPkHtB-At3xzkAx1wNCRQr_bHAbDg0Miw7sBC5XJ8w3UJ07rK-RI8Atvinjj5h3wSDWcZqSIc0zQsh4FM6Jks2YfdDsisp1PAt4uEVvpdXswpu7D-CCTIp-Kaouf8zIKX5DRswVBmU4asZC9W8FTNMQ48jJouG1o0gSVY207_wx7gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فوووووووری
:
🔴
ماشاریپوف و نازون از استقلال جدا شدن :)
🔴
پ.ن فقط از استقلال ی سهراب مونده همه رفتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/135955" target="_blank">📅 18:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135954">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
✅
اورونوف چهارشنبه‌ وارد ایران خواهد شد.
🔴
پیشنهاد ۳/۵میلیون یورویی الشمال قطر صحت ندارد.پیشنهادی باشد هم با میلغ بسیار کمتری است و از قرارداد مالی او یک میلیون و ۴۰۰ هزار دلاری با پرسپولیس بیشتر نیست/قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/135954" target="_blank">📅 17:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135953">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
قدوسی در خبری فوری
❌
احمد نور میخواد برگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/135953" target="_blank">📅 17:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135952">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlngziOIlfg_RJK-MGzjimpVEqj9TkaFKh2doOk8YuxdLCbfWvs0dEqaYjFNoWkZmdv-NRIa6fn7waYRmzv0n6hTzPcGiF9cPm46w8T1Gb_cx_MtyaTMkfrejFpZ8-eUsBEmI4kITLYJqK-OMRd-qCRblbqGQlhy9qtqnx4m-oj25VpfBAkhs4V-qqmW3YreBGpCS1FWBIass9EWZg-2lE8Z0mo8ACGn-oz0vV0QYnrkWut-317ZksXGjliPfzZHmJc7cDhwwORCkatMv_XHaRjO5ealguOA3G9KpgweAHif0XYchehYRR1MWUHDvDLF_nHE0WGqv_h5zGbHawH8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ابوالفضل جلالی بعد از پیوستن به پرسپولیس یه میلیونی شد
🎉
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/135952" target="_blank">📅 17:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135951">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
✅
سامان قدوس در فهرست نقل‌وانتقالات باشگاه پرسپولیس قرار دارد و سرخپوشان به دنبال جذب او برای پست شماره ۱۰ و جایگزینی با رضا شکاری
هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/135951" target="_blank">📅 17:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135950">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
شایعات؛ محمدحسین اسلامی در حال مذاکره با پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/135950" target="_blank">📅 16:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135949">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
کوشکی و اسلامی توسط ترنسفرمارکت بازیکن آزاد اعلام شدند
🔴
از طرفی ایجنت هر ۲ بازیکن با ایجنت جلالی یکیه
👀
نظرتونه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/135949" target="_blank">📅 16:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135948">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/135948" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135947">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/135947" target="_blank">📅 16:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135946">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbFJ1FYAKKNvEXI20l2GHCHTr8-_oqaaOILBunbgKAsRlt_c1tr9TWexQRU5A6CaT_QwNymaf_krFtG0bMOZ740k6VJ97zIWpaI5KpcogZX4rWEAbNFZJ6XJW8w63Ld2RxQmPY4uD2cR5G9UWUGpjtogGfoRSCc2KyEwDdcRq5taQPm2VZ_9yAbtZmFwagIv5u8HxBGLqIJWcN7p-PtXMyoGLwdNEqbBwc-P8lkupLF-xP4yhRDeEDnhvwYNGaPtzpQz2Yvkp8ZzLX7t3k8fcJmQzTrc-nkxCCZ8PN41ZHtK9Fe6X4ndyrZC2xozBYOArxZxQAFHRuKvx7JVoY8JGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ایجنت مرتضی اومده مرتضی رو دوباره به لیست پرسپولیس اضافه کرده ؛ باشگاهم هنوز برای مرتضی پوستر خداحافظی نزده
😑
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/135946" target="_blank">📅 15:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135944">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahOWG5MNbdarTTV3Mpz9ShQoyFIaKHWsQWgNac-ciuxuyHqih3Sk0_s_8xo1SFDKbINZGf8KUIS0K_RjKG5jt_WYYRsHLRAkTSiAg46Xnlvj-U9impgWyUDmElPUa3A9kfqXUm-xGXQZvgAq4LsdfkSgK_TdrI3nOJTv1e-PV-tIeWvqQOkgUXNzuZeIzBYMPTx-qe2QfvCvi987Di_FA0viivXQ_9F7pR4slXoXtdLawTTBD4tNe-U9KaPWrnU_GOiX3pSjxwZLUgothv1AVRrKJujFG87AErFUaUp3N9XyJ9jo-vBtZulVun2xoPbEshKvWon8x47RuBvLVOZefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سامان قدوس؛ بمب بعدی پرسپولیس؟
🔴
🔴
ورزش سه: پرسپولیس برای جذب سامان قدوس هافبک ایرانی اتحاد کلباء امارات درخواست داده و این بازیکن در لیست خرید سرخپوشان قرار گرفته است.
🔴
🔴
قدوس که سابقه بازی در لیگ برتر انگلیس با برنتفورد و تیم ملی ایران را دارد، یکی از گزینه‌های جذاب پرسپولیس برای تقویت خط میانی محسوب می‌شود.
🔴
❌
باید دید مذاکرات پرسپولیس با ستاره کلباء به کجا می‌رسد و آیا شاهد یک انتقال بزرگ دیگر به جمع سرخ‌ها خواهیم بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/135944" target="_blank">📅 15:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135943">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
✅
عملکرد پویا پورعلی هافبک دفاعی جدید 30 ساله پرسپولیس در فصل گذشته لیگ برتر :
🔆
21 بازی ، 1 گل / نمره متریکا : 7/03
🔴
سابقه حضور در گل گهر، تراکتور، ملوان، ذوب آهن، فجر سپاسی، خونه به خونه، بادران، شهرداری جویبار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/135943" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135941">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGj0o8fRuJ15gYHiLFI7pRurgqEwS1am8LIcN82Z6jcUOKSVuiFdxdqjFgOIN5s0c983W-4bSyO6xQa6LQpVQUF8nrY56YnMO0tmz4cW6y308Te3GkPwfnqNIaXB0vgq-AMspYBbyNdxshqn-_TxDUjIjwhlRp7iaYsHr30vyXwpWalPgojblxUwmYwgPyljdDlARWzYuF5R1iOWsY9Z7t-2QlAsZfcEb-gkJL9ChAqu2OSBBCtOo8Y9q4S4OjMFB9z-48PA4uwDMdWYiQkdsmhuXOtxKzcISJWmQ-jUCnvMuMu8mn9meykpjyahlwyLD06sYbBwyqJTl-WoAyVmwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
فیفا قضاوت دیدار فینال جام جهانی ۲۰۲۶ میان تیم‌های ملی اسپانیا و آرژانتین را به علیرضا فغانی سپرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/135941" target="_blank">📅 15:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135940">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzIHrz2e_q-vVgBaALmLgXWfNeRzxyAh7veoIjSvR4gU3G9aRdREnF8fezKcXkDwiDn9C5jVz--5gnPe34jKKqwmuEjNvwAjhUCX7_A8VMO0_y0S_dtRsu3o09kMgZVrNQGY-dm434ODpNvKvEU5pNWC8c2ZHa42bgMhqJdTxkTDrR1CxOQF2ockCb5_IgasLD4R9LGtV7PeZt3N8XYzczgXiTlIYAV_1YCbU2UBoCpaTle0LC0JK4dq9KEBJXiFfpQ7m1zcVMAhsWDTFLFBXz7oegzgUZCQdCB-Te9zGqDdifyxmeF6eSqcfcMZsQMbOvhZtx1GEBp_0mHVQNtjTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز:
مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135940" target="_blank">📅 15:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135939">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝙷𝚊𝚓𝙼𝙰𝚑𝚍𝚒</strong></div>
<div class="tg-text">تو دور زمونه ای که فساد حرف اولو میزنه کسی که وظیفشو انجام میده باید قدردان خودشو پدر و مادرش بود...</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/135939" target="_blank">📅 15:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135938">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompourya</strong></div>
<div class="tg-text">دیگه نمیتونی زحمات یکی رو بگا بدی خیلیا به وضیفشون عمل نمیکنن</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135938" target="_blank">📅 14:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135937">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وظیفه اشه  دیگه دمت گرم نداره  مثه اینه مادر به بچه اش شیر بده بگیم دمت گرم مادر که به بچه تازه بدنیا اومده شیر میدی
😂</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/135937" target="_blank">📅 14:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135936">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahidreza. Sadeghpour</strong></div>
<div class="tg-text">وظیفه اشه
دیگه دمت گرم نداره
مثه اینه مادر به بچه اش شیر بده بگیم دمت گرم مادر که به بچه تازه بدنیا اومده شیر میدی
😂</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135936" target="_blank">📅 14:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135935">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دمت حدادی گرم که باج به شغال نمیدد</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135935" target="_blank">📅 14:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135934">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHamed 65442</strong></div>
<div class="tg-text">دمت حدادی گرم که باج به شغال نمیدد</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135934" target="_blank">📅 14:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135933">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHamed 65442</strong></div>
<div class="tg-text">دم بانک شهر گرم</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135933" target="_blank">📅 14:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135932">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🚨
❤️
پوریا پورعلی با عقد قرارداد دو ساله به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135932" target="_blank">📅 14:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135931">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
🚨
شنیده ها: امروز احتمالا ۲ رونمایی خواهیم داشت
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135931" target="_blank">📅 14:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135930">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
بااعلام سایت ترانسفر مارکت؛ باشگاه پرسپولیس بابت رضایت‌نامه محمد مهدی زارع 800 هزار دلار به باشگاه اخمت گروژنی روسیه پرداخت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135930" target="_blank">📅 14:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135929">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTiWW3GR3fIJaEs0H8yKhJ9E3wvbq38EklzxxrGwlxYsQn2Gaa-2LUa0RswLHAntAiEghZuQHF7h91tiGQg2a2zybbyRHFi1hyQN_swakdrqWUOxCnzFYwXC11dPRxx6RdDA9WDF3Nqc7tLx90N1sVlDB4r2yYfXOxrIrwL0-8U-hPmvHFUFkr5Gm5JnfeoVUJ1Up08kfuTxKyc6M8_ZFtrWiCU3f_vnELCTNHTzSMSLAmYpXSfVVNA4xvle3X9Nm5LgDFkQvLyNSkV3hbYiAKQEVAe0W0QvJISx7zGPaTsd1d3QTvgvrVmAGSXbnmkBT2xDPzJBj0wsC_ki6BoN8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام سایت ترانسفر مارکت؛ باشگاه پرسپولیس بابت رضایت‌نامه محمد مهدی زارع 800 هزار دلار به باشگاه اخمت گروژنی روسیه پرداخت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135929" target="_blank">📅 14:38 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
