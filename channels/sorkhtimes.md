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
<img src="https://cdn4.telesco.pe/file/vNCYc-W48NkS_oqt_oN0-7rYV_yLHGSmwP7sYn0D5pdTUQQXmBffbnwMoHGtUxOKoeY-8nI9BwS5IXbgoEWsy6bSSEJXBgEw5hMfTCnetWbqzR5AA4I-P-W0kz5UHGDC348ykSvZTpbab45gXrDUZzP9_oNA8coLH-GogfRyW3fmcrV46ZqpxlBfm6OiyH9cfsCwXxVdEfugFDK5er207wFhMt1lNHR4VuAolSuKn243zJvcfkJdCVu10DjuhPUaORnplIWanpEKilMcUA31rrwlXUlRtDY0aP8pPHqqxtAgJmdeDLcsXE2mWHrHC0hDCFGYSRda3MWPlw5uyzrrvA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 09:25:37</div>
<hr>

<div class="tg-post" id="msg-139026">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
📌
ورود سریع | مسیر ساده | دسترسی مستقیم
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/139026" target="_blank">📅 01:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139025">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/au0bg_ZG4NSZjID02vDA597FAZaRxkTPkytuGOE6OpYeMdJ2cM5Fqg4NfQrJfxCF0XvMagYYRH83sj6uVibNVtS2vDdkBjQefQppAdUz7PunPiwfrzoW1cMcXOT4yMiQbRqpXkRTtZ_yRVO6AyirMcQMGinTnb7ZhuoepxU18e_XpdfH4u0c3Z5JqbbBAOhMxeknCrPcMDKa7N4ZvTrEVmZaPHjufpzS2suClIR1dNNnZj2CriXIB0GmPOVHvIz_ay61ylL7bQff6zVIMYYQMD45fGzs8PpxoQBcZvDdqYscSz5I3BqVooJO7cFQaefYrh21zWjnfIcLUDAgbssNKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⛔️
عدنان کوستوویچ
فصل گذشته دستیار تارتار بود و این رزومه ایشونه، آقا مهدی چون توهم توطئه داشتن ایشونو گذاشته بودن کنز بچینه سر تمرین و اجازه نمیدادن تو مسائل فنی ورود بکنه
و به همین خاطر عدنان نیم فصل رفت ذوب آهن؛فقط خاستم بگم انشالله که خیره
👀
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/139025" target="_blank">📅 00:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139023">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAZELPsVS064pl4bfB99Qqg-jWmPoo5W0ta97N0kGw9FZJ4WMmMc4_0sk5amz8xPzALOVaC9W9oiZQg2KaFw4qw4yzU4AQLB4ymP1SxmvwKxyJ-Uj3t8y4kgRrLJi34Yo59NkjjHMeCyFwukahm1Bx9mBZggKuNWhWZYgDTSpVu86t2jm8oglrUBg3S6sUUQ1UQozemCtCPB2zlhnJDq-RNPu-cgwx-LZsJ0V8-0PmzBI5EOAYAonREoHtgy3Zd3V-soevnPqm7vxOy-f4XnPU2BhAEIhKCAIvE4VJs2onCk0svWhx5-iDfpz-WFGBYi2MdP7bzG8TATexjVMQN3_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
📊
نقل و انتقالات کامل پرسپولیس در فصل جدید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/139023" target="_blank">📅 00:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139022">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🇹🇷
در هفته اول لیگ ترکیه، فنرباغچه با هدایت اسماعیل کارتال در برابر گنچلربیرلیغی با نتیجه 2 بر 1 شکست خورد !
❌
فقط باید اسی کارتال باشی با اون همه ستاره هفته اول ببازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/139022" target="_blank">📅 00:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139021">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
پرسپولیس امکان جذب بازیکن خارجی ندارد چون ۵ خارجی دارد و  طبق قوانین جدید به شرطی می توانست خارجی جذب کند که با دو خارجی فسخ کتد.گرا و بیفوما هم مازاد بودند که با هیچ کدام شان توافق نشد و هر دو ماندنی شدند
❌
❌
در پست دفاع چپ که دغدغه اصلی تارتار است و هافبک…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/139021" target="_blank">📅 00:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139020">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
پنجره نقل‌وانتقالات فوتبال ایران بسته شد
❌
پنجره نقل‌وانتقالات فوتبال ایران در ساعت 23:59 چهارشنبه 4 شهریور بسته شد و باشگاه‌ها دیگر امکان ثبت قرارداد با بازیکنان تحت قرارداد را در این پنجره نخواهند داشت.از این پس، تنها بازیکنان آزاد در صورت داشتن شرایط…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/139020" target="_blank">📅 00:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139019">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEqeNZm-PpMrdqyOh9zPm8pvh_vu4IMVe39d9basbZNsZWAqBZLe1Mqls-jvUGUCxQf0LNv_eeTV8WCWFwc5D-QXU2DQl6QYaD5qFInJz9sKaQsNbmF2qxxveedbizGqY03OVoCK4vHSR65m29WvUjQ4aiUcWMeNIjlXRHi3UhWrv18wsNsrPGUDYv-ACGtRikvGShoRHv-ZKpclG6NqKTPdcCUVL_2gXap8Zg---sGgJB0RtZbys3tgCl7-MvEfoJ22Ii2mCi9xuAiwND5V8yCFxumVwJf-ZHum8S9O-pz0eTApPHTpVIIPBpy0d0NlALp5YnqiXQDg1xJjrUBE8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🤩
استوری حدادی، مدیرعامل پرسپولیس برای حمایت از ایری و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/139019" target="_blank">📅 00:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139018">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAmhMpF9S_qNOi0SpAAmS93OmnauZnarHImL_BwXzIIFX0JNdFBhDNF14SNXmTkMG4mvLavpd8wmvIZjcr6CmOIymO33TW0P9F-vpz7Gd2zuV9tN7dX9fbwiHu1tx81EoKkyNh7gdtmjWMTPUzNIufGuk0JGOwwmm1FLeAmP_FFUcZoNqPaHUcKbt0Rbrs4bIOgZpEtkGkDZMs1C28OIIjp3V6qakA3j1h6qpx1y_y5hj5qpkjmCxT_WefNmdwrcc0fHzwtZCSwV6DDzirxKkddn0F4AMSFQ7Aar04V82lzK5K5STmxAJmPbx5PEj9FEjbjE2xa9NMnddGf50nW_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پنجره نقل‌وانتقالات فوتبال ایران بسته شد
❌
پنجره نقل‌وانتقالات فوتبال ایران در ساعت 23:59 چهارشنبه 4 شهریور بسته شد و باشگاه‌ها دیگر امکان ثبت قرارداد با بازیکنان تحت قرارداد را در این پنجره نخواهند داشت.از این پس، تنها بازیکنان آزاد در صورت داشتن شرایط قانونی می‌توانند با تیم‌ها قرارداد امضا کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/139018" target="_blank">📅 00:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139017">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
پرسپولیس از جذب ابوذر صفرزاده انصراف داد / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/139017" target="_blank">📅 23:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139016">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
محمد نوری چه فازی گرفته و صحبت های جالبی می‌کنه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/139016" target="_blank">📅 23:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139013">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
‼️
وقتی میگیم پشت بازیکن جوان تیم باشید کفتارها در کمین هستند واسه این چیزا
✔️
✔️
سایت فوتبالی و چیا فوادی توی ۲۴ ساعت اخیر پنج تا پست پشت هم علیه دانیال ایری با کلید واژه مدافع ۱۰۰۰ میلیاردی کار کردن تا کمر بازیکن جوان پرسپولیس بشکنند
✔️
✔️
دشمنی این بیشرفا…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/139013" target="_blank">📅 23:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139012">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
🔴
تصاویری از سیل آخرالزمانی و وحشتناک امروز نپال که باعث شد صدها نفر کشته و ناپدید بشن!
❌
ویدیو عمق فاجعه رو به خوبی نشون میده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139012" target="_blank">📅 21:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139011">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
گرشاسبی، مدیرعامل فولاد: رامین رضاییان به فولاد علاقمند بود و در اتفاقی جالب به فولاد برگشت. قرارداد او هم زیر ۱۰۰ میلیارد تومان است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139011" target="_blank">📅 21:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139010">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
نقل و انتقالات تابستانی پرسپولیس به پایان رسید و این تیم دیگر بازیکنی جذب نخواهد کرد ...
📰
مهدی طاهرخانی خبرنگار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139010" target="_blank">📅 21:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139009">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/bd751b7046.mp4?token=YMhif67dOpmpYPtzEOng0V79nDoINxs8SyhIuzUJq5I23xFVt_LQyQtrb00vMn0ouJixL6co78DZVOhVr4pTCiNZRnPVmiGrUuP9I5w7EnMxQlT-G3RZ9pLpoYRZCu2u-cplz3kw8K3Z21N__MiyFbomMFpEsGzAGapa8CfOEvY_LhckbNLgC5coUvYjVb05NDkjkJe2FprY99SFrCVR6KyeasSrENZj-XpuHYUt8p5h-zyxjThRFYcVXqWdhagqse0Y427g0Y4CjTPtoCEDd9HcPvWWYHWOBN_OpNXoWsdtwV8eudT1vSjSTcx1OxAxtZhQvQdCc8_ftSmGFKzthg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/bd751b7046.mp4?token=YMhif67dOpmpYPtzEOng0V79nDoINxs8SyhIuzUJq5I23xFVt_LQyQtrb00vMn0ouJixL6co78DZVOhVr4pTCiNZRnPVmiGrUuP9I5w7EnMxQlT-G3RZ9pLpoYRZCu2u-cplz3kw8K3Z21N__MiyFbomMFpEsGzAGapa8CfOEvY_LhckbNLgC5coUvYjVb05NDkjkJe2FprY99SFrCVR6KyeasSrENZj-XpuHYUt8p5h-zyxjThRFYcVXqWdhagqse0Y427g0Y4CjTPtoCEDd9HcPvWWYHWOBN_OpNXoWsdtwV8eudT1vSjSTcx1OxAxtZhQvQdCc8_ftSmGFKzthg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇲🇾
شهاب زاهدی تو بازی امشب جوهور دارالتعظیم تو لیگ مالزی برای تیم‌ش ۴ گل زد و در آخر ۹-۰ برنده شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139009" target="_blank">📅 21:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139008">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e98b3d3c67.mp4?token=gofSZ6Cd5aRJcOOXbugviHJcHYGPE31nM34ilcWrBp0DKj0Sn-mxfdR5mgoQORrNbBoM1EayAdnnwqpp1cjQuZlDaIvhiRXrdtVPuLxv1-GrAZ7WZM3PO97H0A0UqBaIFvthfbKNB_qMFqlKKuorUE8y45dSN5qM9j1338yvQdF7-lyFPBUHa_5zf5xlS8gL-J8vRz3Uuf9HBHlM0wSROL25U5TAZ0hisVZ9EKKWnI9OqlVTZDCRsbRabE5pn5VCt-7j6mUCLP-Eel-y9sXpTadXosftls4sR8U81_UzPJFreasFStRRBeNg7qzvNMDOwc8lf9lRfw3Nv_90UnA8ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e98b3d3c67.mp4?token=gofSZ6Cd5aRJcOOXbugviHJcHYGPE31nM34ilcWrBp0DKj0Sn-mxfdR5mgoQORrNbBoM1EayAdnnwqpp1cjQuZlDaIvhiRXrdtVPuLxv1-GrAZ7WZM3PO97H0A0UqBaIFvthfbKNB_qMFqlKKuorUE8y45dSN5qM9j1338yvQdF7-lyFPBUHa_5zf5xlS8gL-J8vRz3Uuf9HBHlM0wSROL25U5TAZ0hisVZ9EKKWnI9OqlVTZDCRsbRabE5pn5VCt-7j6mUCLP-Eel-y9sXpTadXosftls4sR8U81_UzPJFreasFStRRBeNg7qzvNMDOwc8lf9lRfw3Nv_90UnA8ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
منهای ورزش
✔️
عکسی از افزایش عجیب و غریب قیمت دارو.
🔄
شما دیگه سرما هم نمیتونید بخورید. چون یه بسته آموکسی سیلین شده ۸۷۶ هزار تومن!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139008" target="_blank">📅 21:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139007">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
اسپورت عراق: یحیی گل محمدی به شدت به جذب محمدرضا سلیمانی که 18 ماه بود بازی نکرده بود علاقه‌مند و تاکید داشت بود و الان این بازیکن به علت عملکرد به شدت ضعیف‌ای چه از خودش نشون داده سران دهوک عراق میخوان در لیست خروج بزارنش ولی باید تمام قراردادش رو پرداخت…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/139007" target="_blank">📅 21:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139006">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a657a5ef3.mp4?token=vbXTd88YOUmShu56idUyAvLb2ORUzfLbS0dMhWBIVuTeVc_jx_rsd68HOuwJ5jMRKFpZVVNch_e8UC20s0XfGPJGvBYK_-IA5xObSkw_ENfylzBx62DEKL95utM3MjJQgUoRuuSL8F-YZa4ojgjhNGisvmx-Czv5BgKmoB0D4P8CPZ6WUfJaCTvjMjTuXFBjKdlkjaapIEl6Twma5A9DDSwHmtW6zXBMDVJoCLOmWY2Hz7BxrB15FkAms7W58SljI8khOeE01-yQMERuwmCUlZR_aRlyzCoy7v40_l9MxLhN4ZlVG2yq_av6XhNITtAdmdQerqMlfmy2VHjYkLqkvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a657a5ef3.mp4?token=vbXTd88YOUmShu56idUyAvLb2ORUzfLbS0dMhWBIVuTeVc_jx_rsd68HOuwJ5jMRKFpZVVNch_e8UC20s0XfGPJGvBYK_-IA5xObSkw_ENfylzBx62DEKL95utM3MjJQgUoRuuSL8F-YZa4ojgjhNGisvmx-Czv5BgKmoB0D4P8CPZ6WUfJaCTvjMjTuXFBjKdlkjaapIEl6Twma5A9DDSwHmtW6zXBMDVJoCLOmWY2Hz7BxrB15FkAms7W58SljI8khOeE01-yQMERuwmCUlZR_aRlyzCoy7v40_l9MxLhN4ZlVG2yq_av6XhNITtAdmdQerqMlfmy2VHjYkLqkvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
شهردار تهران: قصد داریم 3 ورزشگاه 40 تا 100 هزار نفری در تهران احداث کنیم که شامل همۀ ورزش‌ها باشد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139006" target="_blank">📅 21:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139005">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">#توجه
👎
❤️
دوستان تو این پنجره هیچ خرید جدیدی نداریم، به اسامی‌که دارن لینک میشن هیچ توجهی نکنید باشگاه الکی لیست رو با بازیکن های معمولی پر نمیکنه…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139005" target="_blank">📅 20:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139004">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">#توجه
👎
❤️
دوستان تو این پنجره هیچ خرید جدیدی نداریم، به اسامی‌که دارن لینک میشن هیچ توجهی نکنید باشگاه الکی لیست رو با بازیکن های معمولی پر نمیکنه…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139004" target="_blank">📅 20:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139003">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">روز اولی که میخاستن این ترسو رو بکنن مربی همین چراغی مخالف بود  ببین جیشده صدا چراغی هم در اومده چراغی جان نمیشه با این اقای دکتر حدادی  صحبت کنی این تارتار بخدا لایق دستیاری هم نیست  دیوونم کرده با این رفتارهای مسخره اش</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139003" target="_blank">📅 20:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139000">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSaeid</strong></div>
<div class="tg-text">روز اولی که میخاستن این ترسو رو بکنن مربی همین چراغی مخالف بود
ببین جیشده صدا چراغی هم در اومده
چراغی جان نمیشه با این اقای دکتر حدادی  صحبت کنی این تارتار بخدا لایق دستیاری هم نیست  دیوونم کرده با این رفتارهای مسخره اش</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139000" target="_blank">📅 20:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138999">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‼️
🔴
باشگاه یک ماه در تلاش بود تارتار رو راضی بکنه به کادرفنی دستیار خارجی اضافه بشه اما هر بار تارتار مخالفت میکرد و بهانه تراشی میکرد، امروز دیگه به همه ثابت شد باید کادر فنی تیم تقویت بشه.
‼️
👤
آقای تارتار کلا بلد نیست با خارجی ها ارتباط بگیره و همینم موجب…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/138999" target="_blank">📅 20:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138998">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
🔴
باشگاه یک ماه در تلاش بود تارتار رو راضی بکنه به کادرفنی دستیار خارجی اضافه بشه اما هر بار تارتار مخالفت میکرد و بهانه تراشی میکرد، امروز دیگه به همه ثابت شد باید کادر فنی تیم تقویت بشه.
‼️
👤
آقای تارتار کلا بلد نیست با خارجی ها ارتباط بگیره و همینم موجب بروز مسائل حاشیه ای میشه، ایشون کلا توهم توطئه داره تو هر تیمی که بوده…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/138998" target="_blank">📅 20:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138997">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
فووووووووووووری از آنا
🚨
مدیران باشگاه پرسپولیس از جذب ابوذر صفرزاده انصراف دادند و خبر مذاکرات مجدد با این بازیکن رو رد کردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/138997" target="_blank">📅 20:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138996">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
در جلسه امروز تارتار با حدادی، سرمربی پرسپولیس تأکید ویژه ای به جذب ابوذر صفرزاده کرده و از ساعتی پیش جلسات نهایی برای جذب این بازیکن آغاز شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/138996" target="_blank">📅 20:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138995">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
✔️
فوری و مهم
🗣
🗣
سازمان نظام وظیفه اعلام کرد قانون معافیت بازیکنان تا نیم‌فصل لغو شده است. بر اساس این تصمیم، علیرضا بیرانوند تنها تا ساعت ۲۴ امشب فرصت دارد قرارداد خود را فسخ کند؛ در غیر این صورت، او باید برای گذراندن دوران خدمت سربازی به تیم نیروی زمینی…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/138995" target="_blank">📅 20:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138994">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
تلاش بیرانوند برای تعویق سربازی تا بهمن
🔹
علیرضا بیرانوند در تلاش است با استناد به مهلت قانونی یک‌ساله پس از فارغ‌التحصیلی مقطع کارشناسی ارشد، خدمت سربازی خود را تا بهمن‌ماه ۱۴۰۵ به تعویق بیندازد تا بتواند تا زمان برگزاری جام ملت‌های آسیا ۲۰۲۷ در تیم تراکتور…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/138994" target="_blank">📅 20:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138993">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
نقل و انتقالات تابستانی پرسپولیس به پایان رسید و این تیم دیگر بازیکنی جذب نخواهد کرد ...
📰
مهدی طاهرخانی خبرنگار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/138993" target="_blank">📅 20:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138992">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/138992" target="_blank">📅 20:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138991">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVJDuDNohyjSiujCMPCltKHF3TtFYNCIjZJiDnuVP35xbHClG986g4b1OwVgTY2i1NfRZwQ-mk05P26w-oc9_Z1WB0ePHJ4zCsJb-PcUoI8niV3zZZJp0eU6s6fGXJMNGrbIBbhQEFzGpR6uAyvpzwjrDA1Z59c6bNzGdnlZRyQlXqhN1fcIF35VoDiwZnVWLHbJGRu_AQLF5MxRj6-XCAeiPtJ-q4V9_4XLxUPNt22QGY5zQOEU7QXDfqORYSNB34PRRo6oWluwUkBbB7DeDALXkDW0NxgVPMIZum2-iUgWCNLGrYemyhGb6IWyiXNJWSiMYLQveoMODKPNZ5UdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لیون و فنرباغچه؛ جدال برای یک‌قدم بزرگ
دوتیم، یک شب حساس و پر از هیجان
کدوم تیم امشب صعود خواهد کرد؟
[
لیون
⚽️
🆚
⚽️
فنرباغچه
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/138991" target="_blank">📅 19:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138990">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
⚡️
⚡️
⚡️
علیرضا همایی‌فر، یعقوب براجعه و محمدحسین صادقی از جمله بازیکنانی هستند که احتمال دارد در ساعات پایانی نقل‌وانتقالات از پرسپولیس جدا شوند و به صورت قرضی راهی تیم‌های دیگر شوند
✍️
🗞
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/138990" target="_blank">📅 17:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138989">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
در جلسه امروز تارتار با حدادی، سرمربی پرسپولیس تأکید ویژه ای به جذب ابوذر صفرزاده کرده و از ساعتی پیش جلسات نهایی برای جذب این بازیکن آغاز شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/138989" target="_blank">📅 16:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138988">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
✔️
✔️
جلسه مدیرعامل و سرمربی پرسپولیس برگزار شد
✔️
✔️
جلسه پیمان حدادی، مدیرعامل باشگاه پرسپولیس، با مهدی تارتار، سرمربی تیم، برگزار شد و در جریان آن آخرین شرایط تیم و همچنین برنامه‌های پیش‌رو مورد بحث و بررسی قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/138988" target="_blank">📅 16:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138987">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">💢
💢
💢
طبق پیگیری ها، جلسه مدیران باشگاه پرسپولیس و مدیران باشگاه خیبر از دقایقی پیش آغاز شده است و تا ساعات دیگر احتمالا قرارداد صفرزاده با پرسپولیس امضا میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/138987" target="_blank">📅 16:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138986">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/138986" target="_blank">📅 16:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138985">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/138985" target="_blank">📅 16:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138984">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/138984" target="_blank">📅 16:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138983">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
ایجنت دنیل گرا:
✔️
«دنیل به قراردادش با پرسپولیس پایبند است و بعد از پشت سر گذاشتن مصدومیت، با تمام توان برمی‌گردد.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/138983" target="_blank">📅 16:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138982">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
کوپال ناظمی و موعود بنیادی فر دو گزینه اصلی برای قضاوت دربی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/138982" target="_blank">📅 16:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138981">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
✔️
شنیده میشه امروز از بین این ۳ گزینه، یکی سرخ‌پوش میشه!
🔴
ابوذر صفرزاده
🔴
ابوالفضل رزاق‌پور
🔴
امیر جعفری
⏳
باید دید کدوم اسم در نهایت پرسپولیسی میشه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/138981" target="_blank">📅 15:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138979">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
✔️
پرسپولیس نا امید از جذب قربانی در تلاش است از بین رزاق‌پور، جعفری و صفرزاده یکی را جذب کند. فولاد پیشنهاد معاوضه رزاق‌پور با همایی‌فرد را مثل پیشنهاد معاوضه با بیفوما و ۸۰ میلیارد پول رد کرده. رحمتی مخالف جدایی جعفری است و خیبر خواهان معاوضه ابرقویی و…</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/138979" target="_blank">📅 14:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138978">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kGu3AaLmixEkLuFvMmIn_0kXSBKxJ3ChR9tyHj8jCheJ-BqE11oCB05ICxJkxgB2BV9tjeuLerbO3Cwn36ri4JuSRSVJtaIaW-mxo28Ui46SctxXs_P_VUkZ-MH3RoACRaixEfTIbHIcy8HS1C80WkQ2mCGInhT4p8FaX9azv4kVjJpf0KXNl92DLU2KPGEK2-cGA_DiyXXycFSTET9S3ezjNZRk5xYKoVd-Th3sYd4bbzv9VN2D-J_9lObufTvp-G99Lwp1q92qYXOYFIdcMcDDdhzt2KTCUOoZPQMbTsZ8ARpxBzwbwuOtAsl8K1EoAA5CJiqBXnvsI51TVFbqsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
وقتی میگیم پشت بازیکن جوان تیم باشید کفتارها در کمین هستند واسه این چیزا
✔️
✔️
سایت فوتبالی و چیا فوادی توی ۲۴ ساعت اخیر پنج تا پست پشت هم علیه دانیال ایری با کلید واژه مدافع ۱۰۰۰ میلیاردی کار کردن تا کمر بازیکن جوان پرسپولیس بشکنند
✔️
✔️
دشمنی این بیشرفا برای امروز دیروز نیست برمیگرده به محرومیت عیسی ال کثیر در آسیا
✔️
✔️
پشت جوانان تیم باشید نذارید رسانه های وابسته به کیسه نابودشون کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/138978" target="_blank">📅 13:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138977">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⚪️
هادی چوپان: مجتبی خامنه‌ای پرچمدار دفاع از ایرانه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/138977" target="_blank">📅 13:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138976">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P082x9Lq-P1suaNNutTU8bSQ1zQhAIWHcHMy4aglLcj5SygmKxY3eK5vts1Ohkwk43n_HV80u5cqYjL77JkJQP4-KlNDFbJFh2E4FfhG30b46rj5G96fgRlWJqkwlTHPEkTer8LHnBPi7KzbZbr-Mmh7Z9uDLQdN6zkfN9IBtwvUpvr5Gt2fWA6wpcy8_k426ppiSuzo-qX1KU_lhSnHNEJR6QEZhBYcsNI80FrSdw-bSETmCAg5-0ZEz7wPrxbWVbmkA3Y4Rn1egm3A6XGqxYkXwZmfmD7oMxDnU4OuzmegxSF8JTynFM2Q-vfTaD3g9XUv4pGtBGA-cAM5d4DJ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رئال در خانه؛ سه امتیاز برای کهکشانی‌ها یا یک غافلگیری بزرگ؟
امشب؛ بازی‌ای برای شکار بهترین انتخاب‌های پیش‌‌بینی!
[
رئال‌مادرید
⚽️
🆚
⚽️
رئال‌سوسیداد
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/138976" target="_blank">📅 12:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138975">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
امیر عرب‌باقری داور دیدار تراکتور و پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/138975" target="_blank">📅 10:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138974">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
سپاهان از استقلال شکایت می‌کند
❌
❌
باشگاه سپاهان به دلیل استفاده از یاسر آسانی در دیدار مقابل استقلال از آبی‌های تهران شکایت خواهد کرد.
❌
❌
این در حالی است که چند روز قبل سخنگوی سازمان لیگ استفاده استقلال از یاسر آسانی را قانونی دانسته بود.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/138974" target="_blank">📅 10:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138973">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
✔️
مدیریت دوباشگاه‌پرسپولیس و نساجی مازندران امروز بر سر پیوستن قرضی کوروش اژدها کش به جمع شاگردان مجتبی‌حسینی به توافق‌نهایی رسیدند و اژدهاکش با عقدقرار دادی یک‌ساله به نساجی  مازندران پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/138973" target="_blank">📅 09:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138972">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/138972" target="_blank">📅 09:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138971">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
✔️
منابع مطلع میگن پرسپولیس علاوه بر رزاق‌پور، جعفری و صفرزاده، با چند گزینه دیگه هم وارد مذاکره شده.
✔️
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/138971" target="_blank">📅 09:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138970">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🗣
🗣
🗣
باشگاه پرسپولیس در آستانه توافق نهایی و جذب امیر جعفری است اما بخاطر باخت روز گذشته و ترس از واکنش هواداران، برای رونمایی تردید دارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/138970" target="_blank">📅 09:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138969">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
دلیل نیمکت‌نشینی اورونوف مقابل تراکتور؛ پرس نکردن!
✔️
تارتار از مشارکت کم اورونوف در پرس و کارهای دفاعی ناراضیه و معتقده مهاجما باید بعد از لو دادن توپ، برای پس گرفتنش بیشتر تلاش کنن.
⌛️
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/138969" target="_blank">📅 09:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138968">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSKEF-02zG1rDFL6pAHF2VgDsfVvM8ZXzJhlkEAsVxuChzZl5cJrSz6msmiZWCL6PhMAIdeNXBQb8G3lXqpp6W2YdwFfCMinyLdPtfrxWELGu4aftApN8LeTzNuFidJ4vuOaShPcaeG0zoGib6L5OWEwZ4xdcHEKP-T-GbrRr0H18wynI9k7IfjjUNWFfzIKq_LzuGOuiDEEq9E8Ji2JG0_0Y-QFQkOYpR0XTWNkmAlGp3gz5y6qYg26YEWyDv3F9da6GHffvkptjxguyp9tov6Qpnt1x-05VHJZNAJe8oZHB-OJajnOjflPgxrE6S9C9h9-DCG5kM0CQjC1_Ny9fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/138968" target="_blank">📅 09:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138967">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
📌
ورود سریع | مسیر ساده | دسترسی مستقیم
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/138967" target="_blank">📅 01:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138966">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
دلیل غیبت محمودی در لیست تیم ملی امید این بود که او در اردوی قبلی تیم در کایسری ترکیه شرکت نکرد و حالا عبدی برای حفظ نظم تیم این تصمیم رو گرفت/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/138966" target="_blank">📅 00:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138965">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
باشگاه پیشنهاد معاوضه همایی فر+پول  رو با رزاق پور به  فولاد داده اما مطهری قبول نکرد بااین حال باشگاه هنوز پیگیر جذب رزاق پوره و میخواد تا 48ساعت اینده این انتقالو رسمی کنه!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/138965" target="_blank">📅 00:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138964">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
وحید فاضلی، مربی تیم پرسپولیس: اگر از بازی مقابل تراکتور درس نگیریم به معنی ضعف کادرفنی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/138964" target="_blank">📅 00:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138963">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/138963" target="_blank">📅 00:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138962">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
با اعلام باشگاه اوستون ارونوف در بازی دوستانه امروز مصدوم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/138962" target="_blank">📅 23:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138961">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79b9a82ba6.mp4?token=gYuegYx31xqzbwOQOLv5dOkFuKRUBF9eQlyy7_-IyQDlA5ta7g7G_BBeA28O75RHtoYZ8dpnujmcA48pvFfw0gd9fIpYbiP3MWKry-TADPEj4qSzsQEtSvfCuLP1BFe5XLKywJaTeXWgZK6yG6oiVTJEeNcmCx_aHJbDKiEwmR8DDWhAsilXCb8TB4ut927SGZdf6nat_hb1os15fQpzyP_c_gewslcRWVlDOstsTL2VOjhr6DGUEfbdZF92CWA8XEQwyyFZ1tycSGWqslLJ_degqYuxHNNbke7zjVaMZOdNx1BYWsfXEFnjbxDTYy70b5-zzcWHbp7wqUKpXRheAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79b9a82ba6.mp4?token=gYuegYx31xqzbwOQOLv5dOkFuKRUBF9eQlyy7_-IyQDlA5ta7g7G_BBeA28O75RHtoYZ8dpnujmcA48pvFfw0gd9fIpYbiP3MWKry-TADPEj4qSzsQEtSvfCuLP1BFe5XLKywJaTeXWgZK6yG6oiVTJEeNcmCx_aHJbDKiEwmR8DDWhAsilXCb8TB4ut927SGZdf6nat_hb1os15fQpzyP_c_gewslcRWVlDOstsTL2VOjhr6DGUEfbdZF92CWA8XEQwyyFZ1tycSGWqslLJ_degqYuxHNNbke7zjVaMZOdNx1BYWsfXEFnjbxDTYy70b5-zzcWHbp7wqUKpXRheAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ممبینی : به عنوان دبیر کل فدراسیون فوتبال تا الان نمی دانم چه کسی گفته است که تورنمنت سه جانبه برگزار شود/  هیچ کسی هم نمی گوید که من گفتم و اصلا نامه ای هم در این زمینه وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/138961" target="_blank">📅 22:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138960">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
✔️
وحید فاضلی، مربی پرسپولیس: اینجا هستیم که فاصله‌مان با هواداران و ابهامات کمتر شود و بیشتر همدل شویم. از داوران انتظار عدالت داریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/138960" target="_blank">📅 22:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138959">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
در فاصله 8 روز تا شهراورد پایتخت؛ با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138959" target="_blank">📅 22:39 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138958">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فاضلی: مربیگری بی‌رحم است؛ آقای تارتار با هدف بردن، تعویض‌هایش را انجام داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/138958" target="_blank">📅 22:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138957">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
وحید فاضلی:
🔄
🔄
مانند یک هوادار دوآتشه دوست داشتیم بازی را ببریم و تمام تصمیمات را با قلب و ذهنمان گرفتیم، اما روزهایی هم هست که آن استراتژی‌ها درست از آب درنمی‌آید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/138957" target="_blank">📅 22:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138956">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
فاضلی دستیار تارتار :
🔴
اسکواد پرسپولیس بالانس نیست و ناقصه ، حداقل به دو تا سه خرید لازم داریم
🗣
🗣
ببین وضعیت چقدر بده که دستیار و مربی تیم اومده مصاحبه کرده داد میزنه بازیکن میخوایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/138956" target="_blank">📅 22:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138955">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✖️
✖️
برتری پرسپولیس در دیدار تدارکاتی برابر تیم امید
✔️
✔️
پرسپولیس امروز در دیداری تدارکاتی به مصاف امیدهایش رفت که این دیدار در نهایت با برتری دو بر صفر شاگردان تارتار به پایان رسید.
✔️
✔️
پوریا شهرآبادی در دقیقه ۷۱ و ایگور سرگیف در دقیقه ۸۶ گل‌های پرسپولیس…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/138955" target="_blank">📅 20:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138954">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
❌
#فووووووووری از قدوسی
🔄
🔄
یکی از بین امیر جعفری و ابوذر صفرزاده طی دو روز آتی به پرسپولیس می‌پیونده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/138954" target="_blank">📅 20:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138953">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
🚨
الوحده در پست قربانی بازیکن خرید
⚪️
باشگاه الوحده امارات با پرداخت 3 میلیون دلار رضایت نامه آدام چرین، هافبک اسلوونیایی پاناتینایکوس رو گرفت و این بازیکن برای عقد قرارداد با الوحده وارد ابوظبی شد /سدد امارات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/138953" target="_blank">📅 20:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138952">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJ2LTkYC_kIRgpWiCJFb8t1eVkTA8rW677AU4g-owLaK-fYVRo3bExVJHgHOZLv8_RZs0ncyYBbE2UhyNnu6YEcJyFzJX2ZaqK5IYJ1eAeTycqGTGnA02WSFonjfwlIaibxqei0wZKyQn5fcy3yP8gWEVsbOnKAdF6mKe76cT1GYFARKnYClBV5bVYGAsBG-MwLlSaB8kwqegIvdK29I0AXx6XQpIVCj7sfqMXK4K3FIkKnC4RckxFpIf5lBiA4o_CLrrftKBTZez9SIKs_IXd-ULVBMso_cYCa1BWtls5y-XouuRppdHcH_zxd2aHGfAT7LNYe_x22EVNBOPUGj_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
✔️
۷۲ ساعت سرنوشت‌ساز برای پرسپولیس؛ تلاش برای جذب گزینه‌های نقل‌وانتقالاتی
✔️
✔️
در حالی که تنها ۷۲ ساعت تا پایان پنجره نقل‌وانتقالات تابستانی باقی مانده، باشگاه پرسپولیس تلاش می‌کند پرونده جذب گزینه‌های مدنظر خود را نهایی و ترکیب تیم خود را تکمیل کند.…</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/138952" target="_blank">📅 20:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138951">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
با اعلام باشگاه اوستون ارونوف در بازی دوستانه امروز مصدوم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/138951" target="_blank">📅 20:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138950">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
✔️
اورونوف و سرگیف هیچ مشکلی با تارتار ندارن/برنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/138950" target="_blank">📅 20:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138949">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InB3-qBt56xxvEmoFJ29Tgox6n4WupY3DBHbt-s6JiRmjIUb6Y-oiwYOYngVKTIVe4qIQnAm050XQK8Ls3_380bBCJwjO7mPAsolRCgS393RlhDUffCRd3y7EZx8Kf1Hw8UxV6vxj2g0c4voNlxce2wX4EXxnPP31_jm5RYgXI50AtUH-jeqLQgQb3pEzki7aI5KqmIUipC6yXJLPnd2lQLYQzq_jAqDYTvm5UuZVkZ1sPWwq4H4_Mz0WmaJa2xivg0e2VaNDD1paC_YDw0c_PKQHEVjBr9UyE70g9YmdlQ0V7hnxVadhSHXqfFjk5G8x397hQelBV3nak1lnroEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یک دوئل نزدیک در مستایا؛ جایی که کوچک‌ترین اشتباه می‌تونه سرنوشت بازی رو عوض کنه بتیس دست بالا رو داره یا والنسیا غافلگیر می‌کنه؟
[
والنسیا
⚽️
🆚
⚽️
رئال‌بتیس
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/138949" target="_blank">📅 20:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138948">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🗣
🗣
تارتار:اورونوف و سرگیف به دلایل فنی نیمکت نشین بودن و من این تصمیم و گرفتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/138948" target="_blank">📅 19:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138947">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEiY26EO3VSA9ZeIBsvv6i6FfzEeTVqxe2Slwf9X9mRBmCkKHBde75krUDTMdUu6qT_3tN51CWXJzoLJF0JHSEFptWSr9qRnf0U2m4cNuf70_L1COBhjpn-TfRA5Wu2t38Ug6VZh98PtfsJwYkAOJXVDSO_iOni8f81zBm-NaN52Q6pNicenNsXR6BZAtcD9gbEiL4mnDz7mK65aQqvbyXRAHT3BPo0vP26KL5RA9RIjf_5dW4-yzCKsubRtjU7v5kc3bpuoKx0Zr4rzMJcs0N0FQjHUNaR7WOMlfViE0vo_7xVN8YrEEcrw6LHbxvS8G_HKWRFhAp5DlZ7XiKL2Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✖️
برتری پرسپولیس در دیدار تدارکاتی برابر تیم امید
✔️
✔️
پرسپولیس امروز در دیداری تدارکاتی به مصاف امیدهایش رفت که این دیدار در نهایت با برتری دو بر صفر شاگردان تارتار به پایان رسید.
✔️
✔️
پوریا شهرآبادی در دقیقه ۷۱ و ایگور سرگیف در دقیقه ۸۶ گل‌های پرسپولیس را در این دیدار به ثمر رساندند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138947" target="_blank">📅 19:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138946">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
امیر عرب‌باقری داور دیدار تراکتور و پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/138946" target="_blank">📅 17:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138945">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
پرسپولیس در آخرین پیشنهاد خودش به باشگاه فولاد برای جذب رزاق‌پور ، دو بازیکن+ پول پیشنهاد داده است!
💣
🔻
همایی فرد + انتقال قرضی صادقی + 100 میلیارد پول پیشنهاد است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/138945" target="_blank">📅 17:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138944">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKhLkAOQWzRqDST779xffl6LfBhplhXlEtt2p4bk31V3Diad1jl9p6hjY4C-oJaGi5HVpiBKzDQWL-eDztkp5xoVcBzBuzgZZreY1nptOcw-xrdzZgl0xRuTpsw48myzQwH5D1DYLlr4ZHqE0LiRkObbn7kNKgum0mlFoJMmBN3BdIcW_Sk58rMu1R0a6K2uBh53yYKd_0aLUilsGJRTr2ZDPF9RCL5FVn3IQY5h8E9NWEkVyiKTL9AenQm0x3Kms4GGBDosUi0jP7fvis6ZcFzAfqKv3hW8Mj0anV-Ki6t-n52C7EiKS4J-k2o_LDf8cW1scxAUtoJ8RRk2whzfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
مرتضی پورعلی گنجی از دانیال ایری حمایت کرد
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/138944" target="_blank">📅 17:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138943">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
با اعلام امیرحسین روشنک مسئول برگزاری کننده لیگ برتر؛ دربی پایتخت ۱۲ شهریور ماه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/138943" target="_blank">📅 17:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138942">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
🔴
🔴
ظاهراً درگیری تارتار با اورونوف سر اینه که این بازیکن در تمرینات دوندگی لازم رو نداره و برای دفاع به عقب برنمیگرده
❌
❌
بازیکن ها درباره اورونوف گفتند که این بازیکن به خاطر اینکه مصدوم نشه تو تمرینات صد خودشو نمیزاره و با بی‌خیالی تمرین می‌کنه و بیشتر ریکاوری…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/138942" target="_blank">📅 17:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138941">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
✔️
عارف معاون اول رئیس جمهور: گران شدن بنزین در محدوده 80 هزار تومان قطعی است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/138941" target="_blank">📅 17:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138940">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbV7olpixoOyuDCR401VtuxbXjh9gnU8rL1f7TAgMINdkMdRY4d0_4vOVsTv9Mqhe-fYbZjnwSPxPxaCJrrit-boXabkSDnB7yY5WEpXX4RDxni46YiEvs4VrmOwp4Mc8cZwLhsvrPP5iRm6U5IkKQoVsern4FkJKhTBZM_X3rpawzyghRalTmvoHwxrdRHd6ciE7CUdaTilmj96Qzhzwk54xGzBq-tfqaf4KUDzDoa34LPvfHGVh4CpkRZ5YoBmKwEEKXooSI6F86rJ7uSZmXGZ3LNo_k7GnrPF3BU-mma-bpHDCIqjmYAdEtbQHXIeF-7u4_iyv8-hA5S8FFa9DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
💙
❤️
بااعلام‌رسمی سازمان‌لیگ؛ ظرفیت هواداران استقلال و پرسپولیس در شهرآورد یازده شهریور 50 50 خواهد بود و قانون 90 10 اجرا نخواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/138940" target="_blank">📅 17:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138939">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkH9vkvLnvUIwwr8KBAibAdS8B8yTdB30kEL1h5HX0HvDMI4du1cDk67fTnBw66M7rtdGYThycLR4ZXlBvXapEyjFID3RMajZnSvqWuyhr59hxJQrYhbwdhFu9P5LgaLHtshjMgkfM-ln-98lss5T_ACwbQp3HT5gRv67-qDJ_WqEZG8cwnw_3IrdjcGVI1gnFq6UMB6_0tcKfXaNk9Dut7CjVpTROUEWNoOWAw3f7KEJuQdZEXu63jfd8sWyxBjXqAK8FhktGXXvpBAGXXx092ErwvmeYT081zH7LE4T91oaHLegKSPJKPNjR_hkYSo3BBBXbuYjYNnwK61umPptg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
استوری مشترک بازیکنان پرسپولیس بعد از شکست برابر تراکتور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/138939" target="_blank">📅 17:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138938">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1236791415.mp4?token=XmCQiJJrQfptL_v58NL0YgfiyGMhFVqLOXBvNEEH8Fqg2BR6QfFo6Thf3hqlqQCOU1WvuQBiCZQEYHS6BR_SwZfOfOiGhIW6-x0YaO7MLQM8Ckew6BQ31OzwydfKOy1H7iwHOE8dnBLMpRhx_RLMrezeN6cnQebU5DgSykuxfztY3KyKNQLj6dyGGp4OCnUeHXIfyiyZUYK8Vz9LqOSABwFarmZEOtGqjd4mSA6nGzfDLigQY9fIwl2PmJq15HsD2UqWK05fEmjBfexrvySU7z8YOljN3RI2We6cUsGjky6YXZhJcGRaFaKmqJSI_uHHGwpNczwfYHakjmrv4X2vdbCz0wR4Wwn0MLEUBC1aSqWdgMbQpAXVZsWdpOTUBZ99mKECiI-F-Y2mp6llp3x9FXF7mx8O4Ez3KxyLo1KAUjor2FZoC3PUUMDDq97DoGJsRZTfY-_QAT0gbj7aw1lHXom3jo-uqDRcuvqdTBlhL77g9uZYsnplUeWKllMNCx9U00uS8vZ0Jz-0rNtNEhDPJSS6z7ZgWdkHm6ZjX4jBYIBgIqXj9MlMdOGQuBELMn0Q2EMBYjHAyvEh3OODiIR8Wq3Bldo0PcRX5oDZIrglgF7qBgO0lXbpdKrY9PFTU-3Y8mR--o5TCeon321J2sROZpGYHKlUiBBB5yhSX-maKtE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1236791415.mp4?token=XmCQiJJrQfptL_v58NL0YgfiyGMhFVqLOXBvNEEH8Fqg2BR6QfFo6Thf3hqlqQCOU1WvuQBiCZQEYHS6BR_SwZfOfOiGhIW6-x0YaO7MLQM8Ckew6BQ31OzwydfKOy1H7iwHOE8dnBLMpRhx_RLMrezeN6cnQebU5DgSykuxfztY3KyKNQLj6dyGGp4OCnUeHXIfyiyZUYK8Vz9LqOSABwFarmZEOtGqjd4mSA6nGzfDLigQY9fIwl2PmJq15HsD2UqWK05fEmjBfexrvySU7z8YOljN3RI2We6cUsGjky6YXZhJcGRaFaKmqJSI_uHHGwpNczwfYHakjmrv4X2vdbCz0wR4Wwn0MLEUBC1aSqWdgMbQpAXVZsWdpOTUBZ99mKECiI-F-Y2mp6llp3x9FXF7mx8O4Ez3KxyLo1KAUjor2FZoC3PUUMDDq97DoGJsRZTfY-_QAT0gbj7aw1lHXom3jo-uqDRcuvqdTBlhL77g9uZYsnplUeWKllMNCx9U00uS8vZ0Jz-0rNtNEhDPJSS6z7ZgWdkHm6ZjX4jBYIBgIqXj9MlMdOGQuBELMn0Q2EMBYjHAyvEh3OODiIR8Wq3Bldo0PcRX5oDZIrglgF7qBgO0lXbpdKrY9PFTU-3Y8mR--o5TCeon321J2sROZpGYHKlUiBBB5yhSX-maKtE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
🔴
کشوری فرد دبیر سازمان لیگ فوتبال ایران:
🔴
سهمیه هواداران در دربی استقلال و پرسپولیس ۵۰-۵۰ است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/138938" target="_blank">📅 17:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138937">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TX5cb9Op2scfyKtt4v8RY3DqJeW7XDDap2Z6nmwDZrjXsTMbAAx3e3RBcS0bCtVHL1E4J5LkJ3Vfy--PeWxt1xBDSTHWr8T-lR0e3qi8AtBrsiPyGMw_rThkh3Vrr9a8S3BqpqExXaRWJs80ntzuh_qQPXTIDPLwTX-_xikqsrn-DklwncLRgxnIYg6c1KfYITyKA_q1RtzbXKTySLBqoyTsrk0rhZOodtbhAdoJDA0V9dVJ0GOV51bWWaqAO3MhU-ogWRAdsxBybZx68f-wPfOZg0XAp1a4CsN7p_6qS3vHGvroGK_QS5Mb6AyDA2nPxC6iMFqORoV366oNQdkpDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
آقای تارتار به بهانه جوانگرایی فشار در رو ننداز روی جوون‌های تیم، عامل صدرصد باخت «دلایل فنی» شما بود نه هیچ‌کدوم از بازیکنان جوان تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/138937" target="_blank">📅 17:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138936">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGlEoQVeyYFUKsBPeVxWC677Buo3TYSyC1Q0KQLYEMnvIgU-IC_qAiJ43MWHu_VnO2Gy0wrnSYLGFYCC0pBrWP9RwZUMqoyDYQ20tgK28extiVW2tQDWZQ7wjPU1f43TeRLCsOYZB8dgbP1NYnFJ4du8Dk1MoWnROWKhefUlD4MgXtpJJk-KYCEuzlbwnb8l02QSkXIL--XG_wVgZoTtpJ9t068_IiiEcnGwx7wIC-LCth6lQhOMPNov4amWMw_X0MMil4VnNssjDP-16hz5hy0-xOhacCVkSneMXxaYZefeEx6qRL1DQLENiiwvrEUcksBFK6HuzB0xzZYPn2cxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
امشب؛ چند بازی با چند مسیر متفاوت برای پیش‌بینی
🔥
⚽️
از تقابل حساس الاتفاق و النصر تا بازی‌های جذاب چمپیونشیپ و لالیگا؛ کنداکتور امروز ترکیبی از بازی‌های پرموقعیت، دوئل‌های نزدیک و دیدارهایی با برتری نسبی مدعیان است.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای امشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/138936" target="_blank">📅 17:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138935">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
💢
💢
💢
💢
شنیده میشه که اورونوف و تارتار به مشکل خوردن و به واسطه کنعانی اورونوف کوتاه اومده و فعلا خودشو نگه داشته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/138935" target="_blank">📅 13:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138934">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✖️
✖️
✖️
ابوالفضل جلالی در گفتگو با مجری فوتبال برتر گفته مصدومیتش جدی نیست ده روزه برمیگرده و احتمال خیلی زیاد دربی در ترکیب پرسپولیس قرار خواهد گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/138934" target="_blank">📅 13:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138933">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
بازی بعدی
✔️
هفته چهارم
⚪️
شنبه ۷ شهریور
🔴
پرسپولیس - ملوان
🔴
ساعت ۱۹:۱۵
🔴
ورزشگاه شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/138933" target="_blank">📅 11:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138932">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
❌
علوی سخنگوی فدراسیون فوتبال: سرباز شدن بیرانوند؟ تاریخ بازی کردن او تا 31 شهریور در کارتش که در اختیار سازمان لیگ است درج شده و بعد از آن سرباز خواهد شد اما اگر نامه دیگری بیاید این تاریخ می تواند آپدیت شود و بیرانوند تا جام ملتها می تواند در تراکتور بازی…</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/138932" target="_blank">📅 11:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138931">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
✔️
✔️
۲۴ساعت تا پایان  پنجره نقل و انتقالات تابستانی…پرسپولیس هر بازیکن و میخواد بگیره باید امروز سه شنبه بگیره وگرنه بعدش فقط بازیکن آزاد می‌تونه بگیره بازیکن آزادی که مثل همیشه ی مدت بازی نکرده و مثل هندوانه سربسته اس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/138931" target="_blank">📅 10:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138930">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
✔️
گویا دیشب تو رختکن حال دانیال ایری خوب نبود و ازبس گریه میکرد شرایطش اوکی نبود. بزرگ ترای تیم هرچی سعی میکردن ارومش کنن فایده نداشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/138930" target="_blank">📅 10:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138929">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
فوتبالی: ایری تو رختکن گریه میکرده و بزرگترای تیم بهش روحیه دادن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/138929" target="_blank">📅 10:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138928">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
باشگاه پیشنهاد معاوضه همایی فر+پول  رو با رزاق پور به  فولاد داده اما مطهری قبول نکرد بااین حال باشگاه هنوز پیگیر جذب رزاق پوره و میخواد تا 48ساعت اینده این انتقالو رسمی کنه!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/138928" target="_blank">📅 10:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138927">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⚠️
آقای جاکش بخای ترسو بازی بکنی تیم میبازه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/138927" target="_blank">📅 10:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138926">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
همه شواهد و مدارک حاکی از سرباز شدن علیرضا صفربیرانوند پس از بازی با پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/138926" target="_blank">📅 10:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138925">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❤️
❤️
صبحی که بازی و باختیم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/138925" target="_blank">📅 09:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138924">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔵
دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
🔗
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
📌
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/138924" target="_blank">📅 02:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138923">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
آقای تارتار! بازی هفته قبل تراکتور با سپاهان را ندیدی؟ چطور دقایق پایانی حواس تیم تا این حد پرت شد؟ مشکل اورونوف چیست؟‌ شفاف به هواداران بگویید. پرسپولیس نباید بازنده میشد دو برد اول چندان مهم نبود اما این شکست خیلی غیرقابل هضم بود. به امید بازگشت هرچه…</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/138923" target="_blank">📅 00:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138922">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
✔️
✔️
۷۲ ساعت سرنوشت‌ساز برای پرسپولیس؛ تلاش برای جذب گزینه‌های نقل‌وانتقالاتی
✔️
✔️
در حالی که تنها ۷۲ ساعت تا پایان پنجره نقل‌وانتقالات تابستانی باقی مانده، باشگاه پرسپولیس تلاش می‌کند پرونده جذب گزینه‌های مدنظر خود را نهایی و ترکیب تیم خود را تکمیل کند.…</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/138922" target="_blank">📅 00:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138921">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
فوتبالی: ایری تو رختکن گریه میکرده و بزرگترای تیم بهش روحیه دادن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/138921" target="_blank">📅 00:27 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
