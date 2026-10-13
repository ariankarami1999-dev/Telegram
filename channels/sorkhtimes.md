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
<img src="https://cdn4.telesco.pe/file/NZf9GTd3-HoeHcy01KZj-tdBotdXIX5dqqoBneD59t5sjPKhzBQsbcdN2zxOGM8JAUnAS6oWGT0843YNdbbr5aAniiZQYqSt1wdqsY2wxCIUcIFkjsSAiRkSaO-Ijd5Zu_PYI-clNAjJvi2VjeAvOnZWcq-qmfFdtKxl_z5S8h5zW3FvyAsChEKMJybN4OB04wV1VKsKwWSbIzuAiXTwQ7KS0WXkKuXGoSE8leST1dcMAUGzNUsY28GAwDT0s1boWg63MMM4qkkfnh_uU9eR_bnTxUCyT7KGXZ5KUggPwbB9laFSJx-EfUq7Hr4C8yc_-lMnexKBJEM78ZLMTYawyw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 15:51:52</div>
<hr>

<div class="tg-post" id="msg-141395">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎙
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
◽️
عدم حضور در لیگ‌های معتبر؟ بازیکنانی که در امارات هستند با اسناد نشان می دهیم نسبت به بازی با مصر 25 درصد افت داشتند
◽️
تغییر در همکاران؟ نه چرا باید تغییر کنند؟/ در جلسه هیات رئیسه من 10 دقیقه توضیح دادم و یکی یک…</div>
<div class="tg-footer">👁️ 365 · <a href="https://t.me/SorkhTimes/141395" target="_blank">📅 15:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141394">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7WcvA_AoM2QmBwEmdJRLi4ge4NY-L0pVfFgjCSnV771xEffOjzSjTnWy7MvB07QpgVzqB3ufXqtTzYdHA3Bae8wCkYdYayN1owhUPJaUQAAoqd_qLh2eB0_GVw721xAiMnowidhUsow65DEUyygX3eFi_UmOcYi9S1KQz8ulE1SY_meLhmRq0y5JyfO6diI_qy-fo4Nz86fFhJ5UN464iGRlUP147-k_XgpZ-w2asLcjkXqmTZCn6ILrE89o1SEzx4yRulSw1lDdqjcGMztJljJZ0utnjHlHY80xHI49yyRtr-YOYfyCR0nkl5u_13-f2uVmt-oB0zxPnz0qmiNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دانیال ایری به تمرینات پرسپولیس برگشت.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 582 · <a href="https://t.me/SorkhTimes/141394" target="_blank">📅 15:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141393">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
حسین کنعانی در صورتی که فردا بتونه در تمرینات گروهی شرکت کنه مقابل خیبر بازی خواهد کرد اما اگه انفرادی تمرین کنه به بازی روز چهارشنبه نخواهد رسید
✍️
خبرگزاری فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 658 · <a href="https://t.me/SorkhTimes/141393" target="_blank">📅 15:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141392">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POlBb9QM8x5cS3NfakpnpnbkyUxxsKGjaQR54Joa8Ui-ztw2UkI5QrwgNRtomKu-_FORGhkxjj4rMzh3jDT1c0_S9CQNcy3Vp--dggwV5kojaHF6psr8RblAtqqDuRqWkwpEPN8sRx60Nat2P5M6gzzgdb6dfs5s9PI3UP--P_o65N0OXS309r704OTE6scq3ZRbnlboNiO3U_UPc6sjmveq66UNWIwYqR0ZQjCzVqMbm2RbtlI60W04XHrvSFLCC0xQHbcYgQyK32mxzSAxkZVIC69caLfV7QEpLtbfdvxYoIHY2jF1srSL-V_1LsQ7IfpwSxgEwQeS2StTGZ5Rig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
برنامه چهار دیدار معوقه هفته هفتم لیگ برتر
❌
پرسپولیس در دیدار معوقه هفته هفتم از ساعت ۱۷ روز چهارشنبه به مصاف خیبر خواهد رفت. پرسپولیس درصورت برد مقابل خیبر، با 19 امتیاز بالاتر از استقلال و تراکتور صدرنشین خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 708 · <a href="https://t.me/SorkhTimes/141392" target="_blank">📅 15:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141391">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
رسیدگی به پرونده محرومیت بیرانوند اول آبان در CAS
❌
❌
دادگاه عالی ورزش اول آبان‌ماه با حضور نمایندگان حقوقی علیرضا بیرانوند، پرسپولیس و فدراسیون فوتبال، دفاعیات طرفین درباره حکم محرومیت چهارماهه این دروازه‌بان را بررسی می‌کند. امکان حضور آنلاین نیز برای…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SorkhTimes/141391" target="_blank">📅 14:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141390">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
به ادعای خبرگزاری هفت ورزشی مهدی تیکدری از بازی کردن در‌دفاع چپ ناراضی است.
✍️
هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/141390" target="_blank">📅 11:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141389">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1d8d44f8.mp4?token=GzkrBI65Ucf3X9aFO7Dm8ZsKoKRcfv2hKo5V1bk9lqdkfqxpCYMquJ_l6gcLIHRFix6Tqq_Bhe1a6Md0W2xheEwKIinBWR4xgvIJkOy0f_9R9z2pGTUfluSnJjylDAe4BEocAeEiflfrdVOmqgYh7FgqZx7fnaQ0aBuH7s1Z8yuFYl5Ob8G7aDZT78SDzmdnl6URhCwGmvunzQp8U1Xb4KjQlGw7-v-3AZAu_GWfaMpAeQrL03_iCdvWcGL2I_9ZfxWmJxpzNOtSTugtIzeznvAC12Mll_3O4R7eWBJ3SUseY8Ac_9obCd-TovQOppqUQmDQ7DtFN8MyVGL6uzMeiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1d8d44f8.mp4?token=GzkrBI65Ucf3X9aFO7Dm8ZsKoKRcfv2hKo5V1bk9lqdkfqxpCYMquJ_l6gcLIHRFix6Tqq_Bhe1a6Md0W2xheEwKIinBWR4xgvIJkOy0f_9R9z2pGTUfluSnJjylDAe4BEocAeEiflfrdVOmqgYh7FgqZx7fnaQ0aBuH7s1Z8yuFYl5Ob8G7aDZT78SDzmdnl6URhCwGmvunzQp8U1Xb4KjQlGw7-v-3AZAu_GWfaMpAeQrL03_iCdvWcGL2I_9ZfxWmJxpzNOtSTugtIzeznvAC12Mll_3O4R7eWBJ3SUseY8Ac_9obCd-TovQOppqUQmDQ7DtFN8MyVGL6uzMeiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کلیدواژه همیشگی مصاحبه‌های بیرو
درصد، دلار، ماشین، میلیارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/141389" target="_blank">📅 10:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141388">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
افشاگری میثاقی از نامه وکیل آسانی و فسخ قرارداد با استقلال در تاریخ 14 جولای!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/141388" target="_blank">📅 10:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141387">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ri-FB9rVFvUPMJIp22WELMLmfVNtKGoBKrQFcQcEQvZyq1XC-odBUAofw2Pc2w36-Cv_rXCPDl6yGJkEN4jTHfnRLnJk_lfOKGfhAIFUwRVddU5mEQvHbxUDpB2wNnKbMF1N9-nMMQiJ9Bw4WOK2JkGNKzQheenKIe1B-hZClM84Lz4WUhrwX--MBttZamClMTCCx2REviq3ZeBP5WW4qKvJpER1gHB_rORQntkEhE7XJr4UzshOhI9sDMLN6Z1eu47-D6vDUtHLwAPfJI-RmBVGoaNa6Mgrb3p3QMc903qJ_aUcpOtpbRbFO8qMQ14wplwWnMhqMMWarqlVRDlv0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📘
⭕️
همین یک‌ قاب از تلویزیون و دوخطِ پشت‌سر میثاقی که نوشته « با اثر فوری فسخ کرده است» کافیه برای حقانیت شاکیان و غیرقانونی بودن این آلبانیایی شارلاتان. همین یک صحنه بسه و دیگر هیچ‌!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/141387" target="_blank">📅 10:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141386">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
افشاگری میثاقی از نامه وکیل آسانی و فسخ قرارداد با استقلال در تاریخ 14 جولای!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/141386" target="_blank">📅 09:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141385">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🎙
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
◽️
عدم حضور در لیگ‌های معتبر؟ بازیکنانی که در امارات هستند با اسناد نشان می دهیم نسبت به بازی با مصر 25 درصد افت داشتند
◽️
تغییر در همکاران؟ نه چرا باید تغییر کنند؟/ در جلسه هیات رئیسه من 10 دقیقه توضیح دادم و یکی یک سوال نکرد .من گفتم توضیح فنی و گزارش را دادم و اگر کاری نیست برویم چون قرار بود تصمیم گیری کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/141385" target="_blank">📅 09:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141384">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🎥
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
🚨
ماجرای بیرانوند و وساطت برای او در بحث سربازی؟ به هیچ عنوان، وقتی قانونی هست باید یکسان برای همه باشد
❌
بیرانوند باید شرایط قانونی سربازی را انجام دهد
❌
او تمرکز لازم را در این چند وقت نداشته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/141384" target="_blank">📅 09:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141383">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65a8965627.mp4?token=CnUXCCIfaZfdIydo6vQYcHaSJGBqgSHuwueEf-q-mLh0CIehpwAzQ4VuLsFOw6aSNPrQLmL8cXouDCqPyViYXW1CZ7nkB_x-OMDDCccF3CKR5xFtVkEc--esa5y7-7HpCaB0dOahMay7mZfgkfujrh3ptDs3FFPCD7Q44nNlTZwcIawtbN2k-Ut93lqDLCo4blAGNlDFUYkd1Kca4FDhmNm1-TNABKJrewtfUe8t1bPe1KxsCSqjkdz5de6ktYHzaxGYIINPOHZJyMLO0K0uapHyR6Z1JTIZ_ruQvOwnZMrS2UpkjWoJqsilqzXbZi96vNqowLECG_stL-kGdxm4-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65a8965627.mp4?token=CnUXCCIfaZfdIydo6vQYcHaSJGBqgSHuwueEf-q-mLh0CIehpwAzQ4VuLsFOw6aSNPrQLmL8cXouDCqPyViYXW1CZ7nkB_x-OMDDCccF3CKR5xFtVkEc--esa5y7-7HpCaB0dOahMay7mZfgkfujrh3ptDs3FFPCD7Q44nNlTZwcIawtbN2k-Ut93lqDLCo4blAGNlDFUYkd1Kca4FDhmNm1-TNABKJrewtfUe8t1bPe1KxsCSqjkdz5de6ktYHzaxGYIINPOHZJyMLO0K0uapHyR6Z1JTIZ_ruQvOwnZMrS2UpkjWoJqsilqzXbZi96vNqowLECG_stL-kGdxm4-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امیر قلعه‌نویی: کنعانی زادگان و علیپور؟ کاش تیم پزشکی بود و می گفتند که آنها مصدوم بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/141383" target="_blank">📅 09:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141382">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06a6489f2.mp4?token=UU2FfAoWd_R6FbwKUeFbcIX_HQnDheBNRl2988on8FbYgI75qM4wdCGg3cbYGkXEjTsvMJQnMH5xvJZ6CKCwIDA11gyQEp8kbaZn3HcwqqqabD4R1-Bc_Ud4C00Q5KaBaF2ZrnMzMWG28-hWeLDXjRh0huDBadz0rZPKv5Cpc8OWqxcfignj23Dsz2Ln474bYsDY2mnorn-dxLV91ruVJbibI9tWb9ox1paHUSSsLy2YRRLcgBM8KPZj2sw47Zydf6hZg00ayR0V5CrSuB0np9xFMwQkelRqndlUpOAWf624AxDFCD4XUH0QneQWz4oyUedT1YDoBei67FSpdRJfuC8L8HGJvhLwjBbE9Xjnuilv-B4T_3U8lvSaAwthZpurCZkN24sDXedVZ0rUrQHb37DxB_9BHPPNN2jenZB9LJEy69tt3A4_l0gHiRo14JwPs4PrIfNkmMEwgZhMgPdEcAQ6wzUI41p9-2ox45vVRpcrhsrqpX1gtfg1YLtphn1lMtbCjlIDErDdzlNDji9XKm7pAhVJ9T8omDuHw6mhRQQf70rWJ4UXyTym2RuWp9_jXd_d3ufAUNFDCwJYSVbgi0UWNOISuqqvK-d1auBZJ9PkYK0Z29KRU5HWBvzEBkhas7KydBNTRlWhMSTaHXNga9HeY6T24bl7NKzs-cMThwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06a6489f2.mp4?token=UU2FfAoWd_R6FbwKUeFbcIX_HQnDheBNRl2988on8FbYgI75qM4wdCGg3cbYGkXEjTsvMJQnMH5xvJZ6CKCwIDA11gyQEp8kbaZn3HcwqqqabD4R1-Bc_Ud4C00Q5KaBaF2ZrnMzMWG28-hWeLDXjRh0huDBadz0rZPKv5Cpc8OWqxcfignj23Dsz2Ln474bYsDY2mnorn-dxLV91ruVJbibI9tWb9ox1paHUSSsLy2YRRLcgBM8KPZj2sw47Zydf6hZg00ayR0V5CrSuB0np9xFMwQkelRqndlUpOAWf624AxDFCD4XUH0QneQWz4oyUedT1YDoBei67FSpdRJfuC8L8HGJvhLwjBbE9Xjnuilv-B4T_3U8lvSaAwthZpurCZkN24sDXedVZ0rUrQHb37DxB_9BHPPNN2jenZB9LJEy69tt3A4_l0gHiRo14JwPs4PrIfNkmMEwgZhMgPdEcAQ6wzUI41p9-2ox45vVRpcrhsrqpX1gtfg1YLtphn1lMtbCjlIDErDdzlNDji9XKm7pAhVJ9T8omDuHw6mhRQQf70rWJ4UXyTym2RuWp9_jXd_d3ufAUNFDCwJYSVbgi0UWNOISuqqvK-d1auBZJ9PkYK0Z29KRU5HWBvzEBkhas7KydBNTRlWhMSTaHXNga9HeY6T24bl7NKzs-cMThwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه‌نویی: در پست خدابنده‌لو، عزت‌اللهی، قربانی، حاجی‌عیدی و نورافکن را داریم و به همین دلیل دعوت نشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/141382" target="_blank">📅 09:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141381">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvdDtQsGYnxhKniOJYT8fSam3vupS_1TMVF04A0cpLnq-MR3BpuHh6HxtkIx7T0Qve5TTnoSc_-jjC8fXcPJfOnTQ5gdARju_PuhtchPmgeVLyaFgIL5Fi0syYUEIZiWearQcM94bnwlq8P3jI93DtG0p1koHI5VyHFW7xVn012ayuf4J3zDmy1wLWfDKGuVQINFyM9KM-bMgLSunkLEj2fUWI8mzxZShAlhXipCAcoLdOPU4wLZSYxaDlKcMQ4DXFPmDBEc-KvCCvYoJ1rEmazKfAGGO3-iA-62LYOTYIU_PQslybyY8RSXxHLAqFbJH47EHFV3V1IMEQQcYaeOeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
به رئیست بگو خر خودتی…دستتون رو شده؛۳۰ مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/141381" target="_blank">📅 08:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141380">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9HiDHD3T7LJAs8_byxYPR31qcTIHtoKrisCvhfnKEeDtJQwQzLKVVxnLXNlFRDpJ-YFiX5_MIyHmU8KArDAhfQTq6k7lYlu0uAcJhPJYsyChQHIAYLoU0CdAkIsOB3XmviCxSX9SCRrLjuAaT_zdd3xKccDFlldUhouHkZKxOeRLz9S0XD2z-dtvpPslRVUGGUm1buptbun0Zmpk33dkusbtdRS_uIKvj4xKE7YLqhVPyXnU5c2Dr-H4TAkx40sFiMzDFbeFQyUswcf1s0mlwSPzbvXRiVz5oprgxQpO1BJvfGMaEVfELJv6Tl5JHWHDJMaLGCrmAhczk4wiOvgow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فرداشب اروپا در تب‌وتاب شب‌های سرنوشت‌ساز؛ جایی که غفلت، تاوانی به قیمت امتیاز دارد!
🔥
⚽️
فرداشب آرسنال با ضریب ۱.۲۱ و اینتر با ضریب ۱.۲۳ از نگاه ضرایب، مدعیان اصلی پیروزی هستن؛ بارسلونا هم با ضریب ۱.۲۶ شانس بالایی مقابل گالاتاسرای دارد. تقابل اتلتیکو مادرید و منچستریونایتد با ضرایب ۱.۹۱ و ۳.۶۴، از جذاب‌ترین بازی‌های فرداشبه؛ درحالیکه ویارئال و ناپولی با ضرایب نزدیک‌تر، رقابتی متعادل‌تر رو نشون می‌دهد. دیدار لانس و اسپورتینگ هم اختلاف ضرایب چندان زیاد ندارند و همین موضوع، این مسابقه رو به یکی از دیدارهای قابل‌توجه کنداکتور تبدیل خواهد کرد.
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
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/141380" target="_blank">📅 01:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141379">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
گویا یحیی گل‌محمدی در یک قدمی سرمربیگری تیم ملی امید قرار گرفته است. فقط کاش یحیای عزیز حواسش باشد همه بازیکنان این تیم باید زیر 23 سال باشند. این دیگر اجباری است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/141379" target="_blank">📅 01:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141378">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⭕️
⭕️
⭕️
هومن هدایتی مشاور حقوقی ورزشی:
⭕️
استقلال تخلف کرده و باید منتظر حکم سنگین باشه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/141378" target="_blank">📅 00:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141377">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
با توجه به مصدومیت حسین کنعانی و دانیال ایری، زوج خط دفاعی پرسپولیس برابر صنعت نفت آبادان، محمدمهدی زارع و حسین ابرقویی هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/141377" target="_blank">📅 00:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141376">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
آسانی که مصدوم بود و جای رزاقی نیا اومد تو زمین ...خود آسانی مصدوم شد و از بازی خارج شد
😎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/141376" target="_blank">📅 23:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141375">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3890159133.mp4?token=CLcJu9DOewlA5ZRDmtPwWeZbCqoxXnvpIBABAFQ0uiwjMhxwmzVALIWsCqMtgwP36L59KazmIN0y__X5rz69taAls0xut0avbZmSeokmcVhr_ulzqNCpjFHno92nt5iy1CGBs6xadF7JNiJnHFJ-BTZTBVjYyxL8gh63_tpRpZhvTxcORA7bM5vcmTcOrpg4xEgM5re08cTWU7nmDtYDtRaJKxyXsdg-qjCwQAo77FohvcvqLbBJMPoGIMNioGXB6QtWLd1wKS__sF5mwmH7j-f4AH-Lg-ZrPLSoWolrV3GLXdD7m354Tm_0MJeoSmn6fv-g7znK3ufxrf9W_biG7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3890159133.mp4?token=CLcJu9DOewlA5ZRDmtPwWeZbCqoxXnvpIBABAFQ0uiwjMhxwmzVALIWsCqMtgwP36L59KazmIN0y__X5rz69taAls0xut0avbZmSeokmcVhr_ulzqNCpjFHno92nt5iy1CGBs6xadF7JNiJnHFJ-BTZTBVjYyxL8gh63_tpRpZhvTxcORA7bM5vcmTcOrpg4xEgM5re08cTWU7nmDtYDtRaJKxyXsdg-qjCwQAo77FohvcvqLbBJMPoGIMNioGXB6QtWLd1wKS__sF5mwmH7j-f4AH-Lg-ZrPLSoWolrV3GLXdD7m354Tm_0MJeoSmn6fv-g7znK3ufxrf9W_biG7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
گل شماره ۹۸۱ اسطوره رونالدو
❌
پ.ن فقط 19 گل فاصله تا آمار عجیب و غریب 1000 گل مانده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/141375" target="_blank">📅 23:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141374">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✖️
✖️
سیدحسین شریفی به عنوان مدیر صدور مجوز باشگاه پرسپولیس منصوب شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/141374" target="_blank">📅 23:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141373">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osMyJb6m7nJXPuZ1EVLcgD2WCOH7KBy-oY98xeZBddqiSHlMI4enEXCZ-BdW8wi-dayxUf2MRt2ijCbzF776PqCZmo3-rLsRAgYJzF_tnaxDfMh0gNNAXrAfIYy6CxR5nULTGymLNNC_wl52C5q2MFTt0PvgOSz2lVFv5Agopifvr3zMDhGDF43u6sxbCrL7zpqrSt8SqB2kxSnc52J_b0RJRaaIRvtcd6fLFrviis_m97B2Ky3YxzVdERbJnUHPxGlq9lqSbMekIj3is0lTI8x284lHDmeOCfX0ZE5QKJOgXyL7ejWuxtU0LgzTTChhqe3uEIYrXUAt9oWyKioPOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
زوج خط حمله مقابل خیبر
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/141373" target="_blank">📅 23:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141372">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GS1WJS0qQR8ToDwoE8uPoytp5DE_OlFCmcjjXyb3gAKghP6zAZUvao2nZ9zkQT0LMgfqJtyseoQ_SbNYU-yQHbl6R1ZNAIIwBKnFlv01uf96QDZmIPsuwul0bLXE5ujYh_1KpZK1jMjmHE0uEl1Fp7EiqOlvv1jW9s3ISFArmiekh1oF422BkFUX-Q_P7MO8Q1bejbMyh6Lfz8qQFhwUNcQkxT_RLeK74P3MV4BAZ4yCbtAzJogx_SmwnrWSzgR6HtKYSAQgiUyx_BEYI9RNQnAH0_9Dn5PA4aiOL63f5IP2wUQfCgSWNTJ1d41RrD_4M30hpyCNuhZerCzCb9wHEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
احمد کونِ دروازه‌بانه الغرافه واقعا اسمش برازندشه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/141372" target="_blank">📅 23:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141371">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
لعنت به این آسانی ...ده دقیقه اس اومده تو ..گل کیسه رو زد .با ی شوت دیدنی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/141371" target="_blank">📅 23:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141370">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
الغرافه گل مساوی و به موقع به کیسه زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/141370" target="_blank">📅 23:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141369">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
لعنت به این آسانی ...ده دقیقه اس اومده تو ..گل کیسه رو زد .با ی شوت دیدنی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/141369" target="_blank">📅 23:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141368">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
فوری/حوثی ها تهدید کردن اگه بازی النصر برگزار بشه ورزشگاه رو میزنن
❌
بزودی تمام ستارگان فوتبال از عربستان خارج میشوند
❌
العربیه:
❌
❌
نیرو های امنیتی بخاطر حمله حوثی ها سریعا رونالدو رو از ورزشگاه خارج و به یک جای امن منتقل کردن
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/141368" target="_blank">📅 22:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141367">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o35eiM3KE9bCDkoaF1A-3noYOO2nKxF5NeH3xnWjj59ZnY1YkA3X5ZM7I8z4NMGK1dq7M34mi5qnP8b1CNZ41HXfsCVSZuqV67btEgBn_9Sj6VAaiDVEF_MlwGCeSsDcYpXixcvJKiAC-kB8F-hwc98N1vtoMYoLIQCUGmJupb99YjsepNvFg7_J6SNFbSpBy0v9qhVqvlynpFi6aXW1m1SEVPGFsu9ZdwbTmSeWj-nwvfxK-bo1OXLou06-L9ul8FEuATEUk44h8SCfeIItVCBsptQC9gys2mI7mO2nh0DyjynpC6Y5UqhMbZJfFrS9-SUJa3JRRYM5fw1GlngZFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پویا اسمی مقابل خیبر هم دقایقی بازی خواهد کرد/
فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/141367" target="_blank">📅 22:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141366">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
فوری/حوثی ها تهدید کردن اگه بازی النصر برگزار بشه ورزشگاه رو میزنن
❌
بزودی تمام ستارگان فوتبال از عربستان خارج میشوند
❌
العربیه:
❌
❌
نیرو های امنیتی بخاطر حمله حوثی ها سریعا رونالدو رو از ورزشگاه خارج و به یک جای امن منتقل کردن
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/141366" target="_blank">📅 22:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141365">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔵
💙
🔥
نماهای دیدنی از سوپرشوت یاسر‌آسانی روی گل اول کیسه به الغرافه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/141365" target="_blank">📅 22:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141364">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
احتمالا بازی های تیم های بزرگ عربستانی هم مثل ایران به خاطر شرایط جنگی شرایط میزبانی و دیگه ندارع و تیم های عربی هم میزبانی خودش و باید به کشورهای ثالث ببره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/141364" target="_blank">📅 22:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141363">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
بازی کیسه و الغرافه هم شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/141363" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141362">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
‏بازی النصر عربستان و نفتچی ازبکستان به دلیل حمله حوثی ها به ریاض متوقف شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/141362" target="_blank">📅 22:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141361">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21384b098a.mp4?token=VC7NXrXW_GrKZSGG2ALkoo1zsVRg0peHFvqgitDjfEPbibDEnDBar7PcQnk3U2BwgtVVS8uvkxc5Y61n_e6Nsq9aWW_VPPaCnQ2YbzgGk37oinZGIM_eQzw_nDM2_JtjkYLl8qJ41Kw4wgEHqvOkY0qjFGacypLW8X7WNZmkQ898S36HovzJ3PlkqHS76mY3PO_q8Y9ixbddTdcp6hjBCZsSCp_16rG7mfJ3amhq1k3yc3yFrtofhuEWN0JAL3yt-dVJZJyKsDDJLjk0Qq5swt_UMAmAKhwylEThDCD14ikFh4PDE1SdMRE23gjmpqq53QBXGsEK2g5YMZlzNszwtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21384b098a.mp4?token=VC7NXrXW_GrKZSGG2ALkoo1zsVRg0peHFvqgitDjfEPbibDEnDBar7PcQnk3U2BwgtVVS8uvkxc5Y61n_e6Nsq9aWW_VPPaCnQ2YbzgGk37oinZGIM_eQzw_nDM2_JtjkYLl8qJ41Kw4wgEHqvOkY0qjFGacypLW8X7WNZmkQ898S36HovzJ3PlkqHS76mY3PO_q8Y9ixbddTdcp6hjBCZsSCp_16rG7mfJ3amhq1k3yc3yFrtofhuEWN0JAL3yt-dVJZJyKsDDJLjk0Qq5swt_UMAmAKhwylEThDCD14ikFh4PDE1SdMRE23gjmpqq53QBXGsEK2g5YMZlzNszwtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏بازی النصر عربستان و نفتچی ازبکستان به دلیل حمله حوثی ها به ریاض متوقف شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/141361" target="_blank">📅 22:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141360">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
واقعا ی بازی خواب آور و بی روح و سرد و مسخره ...بازی صفر صفر تمام شد ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/141360" target="_blank">📅 21:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141359">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
پایان نیمه اول |
🏆
هفته دوم لیگ نخبگان آسیا
🎙
تراکتور
0⃣
🆚
0⃣
الشمال
🇶🇦
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/141359" target="_blank">📅 21:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141358">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
حجت کریمی شلنگ رو گرفت رو بیرانوند
😂
❌
❌
حجت کریمی: بیرانوند سال گذشته 100 درصد قراردادش رو دریافت کرده، در حالی که طبق مصوبه سازمان لیگ تراکتور می‌تونست 70 درصد قراردادها رو پرداخت کنه. امسال هم بیرانوند 35 درصد گرفته، در حالی که بقیه بازیکنا 8 درصد دریافت…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/141358" target="_blank">📅 21:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141357">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnsVbS6JzlCdo8rwuos5Yn90Vm-9OYDGMDz2btIe7kscxYJLMAe01V4oa0pDtJt_8AZzLHK5MEt9pC-3v60nERtYrtU09cOVtk_1xcA8-jNMqcANJyy9nOQZAqhHDiQuaeIEkNB_cSYhb7sCdRaeGUQ-DKt5oKI3OiRLshfLOkDRTgif228tnuyo4ZtxxDXTxKr8yiraQRALuNhOS4T4Z28VdwFyr9TqN4cPPhFh803kL2t62FhqUkynU-QySDOCtA8DSy2di6N0zejkAFJEVhFHl2iPQyPIBED36hmwn5l7ABa_oTki9O5iIVUYBGoiTaKlNy85Ooy6RztjCHoViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/141357" target="_blank">📅 21:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141356">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
سرعت، برگ برنده پرسپولیس تارتار
🚨
فرمول تارتار، ضدحمله‌های سریع و برق‌آساست؛ پرسپولیس با چند پاس سریع از دفاع به حمله می‌رسد و حریف را غافلگیر می‌کند. البته تیم‌هایی که دفاع فشرده داشته باشن، می‌تواند این تاکتیک را سخت‌تر کند
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/141356" target="_blank">📅 20:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141355">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
فوری؛ کد سربازی علیرضا بیرانوند فقط برای فجر  صادر شده و راهی این تیم می‌شود. او به دلیل تأهل و داشتن دو فرزند کسری خدمت خواهد خورد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/141355" target="_blank">📅 20:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141354">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f780d2f1fd.mp4?token=sESvdoSPsGNXomm5nTsVEekoChaVBauZL7aI3rKkRwP0FfuesEpLObmHLiksfO3FwR8xY-g4uU0mq2IMZSdp5o5gtXTzemXEeFdO5tQvYVLGDiorbFT-FiNqkja2EcN0uz2hB8ewKFTgk6r-pzjZptrqmLD1jZb_vGiJCv0WTe4yT4eW7PfqQO4ohYJ03sWBH3T4bGFpjqFB4p00U1mPTo-eW-k1a7nlVr7-eTqfQjYLEbXPF8SwpqfUwsz6ltSlwrjtXPt194fiJpvcJSOxluRUX_59qcOyNv84FD4Bw7NACVnzVbp-Tl3XVrb7uAJk3xR2dIswe7OMVtadPVKm6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f780d2f1fd.mp4?token=sESvdoSPsGNXomm5nTsVEekoChaVBauZL7aI3rKkRwP0FfuesEpLObmHLiksfO3FwR8xY-g4uU0mq2IMZSdp5o5gtXTzemXEeFdO5tQvYVLGDiorbFT-FiNqkja2EcN0uz2hB8ewKFTgk6r-pzjZptrqmLD1jZb_vGiJCv0WTe4yT4eW7PfqQO4ohYJ03sWBH3T4bGFpjqFB4p00U1mPTo-eW-k1a7nlVr7-eTqfQjYLEbXPF8SwpqfUwsz6ltSlwrjtXPt194fiJpvcJSOxluRUX_59qcOyNv84FD4Bw7NACVnzVbp-Tl3XVrb7uAJk3xR2dIswe7OMVtadPVKm6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
پیمان حدادی، مدیرعامل باشگاه پرسپولیس، به مناسبت روز دختر در محل تمرین تیم فوتبال بانوان حضور یافت و با اهدای گل و هدیه به اعضای تیم، این روز را به دختران پرسپولیس تبریک گفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/141354" target="_blank">📅 20:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141353">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
بغداد بونجاح و ریاض محرز، دو ستاره الشمال در بازی امشب که شروع شده مقابل تراکتور غایب هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/141353" target="_blank">📅 20:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141352">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaraC8BDRpCHCDgudRJ8kXJidHS0zMiqGgZEO0gB8s_WptQm4ImnMcUlJQSybbSBc2D5ZspwMi-Cok4QFowghIPbIGjRa1NgVr7eDSV13KuDY8C9jOfwriPTkvxDmRiK9dloWpZMxrdrslvPSmygvvOvNfQx-WXq435DdjcyTpu0iIKAZMT3RVgcjg5AUCoPhxzI4KtfvAZa3rn3FdM8If0yJN5QLZvYPH71NAT7TeQe0M9mPJpd0HvmTxtPd38u9M1KVLP8mNklrLIPkB7L5E2XPjZ65WEVUga-ZsBOuQSgvN8kUb6keBjEFxutPMmMiAqhJIurfQQ7ifB2ZDbumA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
Al Gharafa
🆚
🔵
Esteghlal
⏰
Tonight 21:45
🏟
Thani Bin Jassim
🟣
الغرافه در ۸ بازی این فصل ۱۷ گل دریافت کرده؛ نقطه‌ضعفی که استقلال می‌تواند با حملات سریع از آن استفاده کند. استقلال با روند بدون شکست در ۹ بازی اخیر و برد ۳–۰ مقابل السد، از ثبات دفاعی و اعتمادبه‌نفس خوبی برخوردار است. با توجه به ضعف دفاعی الغرافه، گل‌زنی استقلال دور از انتظار نیست.
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
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/141352" target="_blank">📅 20:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141351">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
علی پروین: فوتبال این روزهای پرسپولیس من را یاد دهه ۶۰ می‌اندازد، این تیم قهرمان خواهد شد؛  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/141351" target="_blank">📅 20:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141350">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🆔
⭕️
⭕️
| ورزش‌سه:
🔴
❤️
پیمان حدادی در پرسپولیس ماندگار خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/141350" target="_blank">📅 19:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141349">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✖️
✖️
✖️
✖️
با توجه به درخشش مهدی تیکدری در پست دفاع چپ، پرسپولیس احتمالا بازیکنی در این پست جذب نمیکنه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/141349" target="_blank">📅 19:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141348">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🟣
تراکتور در مسیر قدرت‌نمایی؛ الشمال آماده غافلگیری!
🔥
⚡️
[ تراکتور
🔴
🆚
🔴
الشمال ]
⚽️
تراکتور با وجود شکست در بازی نخست آسیایی، در ۹ بازی اخیرش ۵ برد و ۲ مساوی داشته و از نظر دفاعی آمار قابل‌قبولی ثبت کرده است. الشمال با میانگین ۲.۲۲ گل زده در هر بازی، خط…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/141348" target="_blank">📅 19:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141347">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از آنا
🔹
باکیچ به دلایل فنی از لیست پرسپولیس کنار گذاشته شده و مصدومیتش کذب محضه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/141347" target="_blank">📅 19:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141346">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2fjtGLEjmnFYTMtSJpPOO0-O999ocpYFaTDZvlS7_dSfoQ_7jVy1xuHlLBh8HRzh8qtKDoG0r4qCd41DK7sjB8cC8rtk1i5hsHpFOwSWhwz3yCZKKh31wq_xR3qYeCh95XCe4s24Li4YGODJtR3uAp9xkB-HvqsJ4NCpMwIr5ORLCATTeK6qPI1XPtA7l9M5JwyL1VoDfVo74oftUXS8SYhOHxL28UPGqyUd5cEbFUw0i5W6MlLQHEazj1HdQbHYGotUCqLXhIm8qE3ZrVbGwDShKCJpMAsGNHe2cqyskIB_e8f4Dz7Zxaz_C8untrASHbQCoslHobHSWND3VI31A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گویا یحیی گل‌محمدی در یک قدمی سرمربیگری تیم ملی امید قرار گرفته است. فقط کاش یحیای عزیز حواسش باشد همه بازیکنان این تیم باید زیر 23 سال باشند. این دیگر اجباری است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/141346" target="_blank">📅 19:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141345">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azUroVQM-2EWTyUITtssBnJFw8bRnJ6Nd9sMQwFDwxO6ljChe_OWHsYNqbKkMbO8IoGHDxsO7M2KhrnwJr9nPPmSRw6rdaTw9n7bICMDQNo34vaia4iCkf1SdzXcpXu9neJ045y1TSGlUEBh78TEFICNdiAOsy_RRogaDiHQPWuwV9KrrpvGdmxSanHE164hSjcSMV-KdmkwcH5TjPJxZqsIepXJtJIrP924HtuwXRW-Xy6tTc9uZPph2nrG4ddGSsHqr5GEWMCerrtlExCzJlpW23HnKYJTTkLLO-o3FJoWVMjJFkm8zrgQTwnzPNeN4gHfcqqjQKuB4n3QEanRNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
مهدی‌تارتار به مدیران پرسپولیس اعلام کرده که اورونوف غیرقابل فروش است و این بازیکن باید در تیم بماند. تارتار معتقد است که با وجود سن و سال بیفوما، حضور اورونوف جوان در ترکیب تیم ضروری است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/141345" target="_blank">📅 19:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141344">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ev9SHMWpDOrWc3lw6Di9PsVBBLrd0mOjh2MwDBRPXBHVSjouoG5O6aPb-kCvGkC--ngv_N86VFZhDiaWg5eF7i5gaKktHGs6Zw-LmNTVNDjETRIvNt2wJvHH2tLuvPaljgqbVg00OcWifSOB2wV2Cg2QA39WZmrSeHWmAvmKTC8WCWS3gcbbt532KGQUIp9b6BNmK3KWnnkr5677juu98cefw8tfiBdNNrmcskuBliuKk6DXH6JPr5E_-RV8XXLscQSXSWuJWhKE7jsgKGzuJpbcnx0QDEpSPknCriu4S7KeZSMGvdy1xxvJ5YNf8nG84yMK4m6qiaercfhfYdandQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🆔
⭕️
⭕️
|
ورزش‌سه:
🔴
❤️
پیمان حدادی در پرسپولیس ماندگار خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/141344" target="_blank">📅 16:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141343">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
⭕️
⭕️
⭕️
ویدئویی که کاملا توضیح میده چطور یاسر آسانی واقعا فسخ کرده و پرسپولیس باید دنبال حقش باشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/141343" target="_blank">📅 16:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141342">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
رد درخواست پزشکی بیرانوند  اول آبان؛ اعزام به خدمت سربازی
🚨
🚨
ماجرای سربازی علیرضا بیرانوند سرانجام به پایان خود رسید و این دروازه‌بان باید چند روز دیگر عازم خدمت شود. دو درخواست پزشکی بیرانوند در این زمینه مورد بررسی قرار گرفت و‌ هر دو رد شد.
🚨
🚨
آسیب…</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/141342" target="_blank">📅 15:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141341">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
خسته نباشی آقای تارتار
🚨
🚨
🚨
با وجود انتقادهای ابتدای فصل، تارتار تونسته پرسپولیس رو به شرایط خوبی برسونه؛ از اعتماد به جوون ۱۷ ساله‌ای مثل پویا اسمی تا احیای بیفوما و خدابنده‌لو و مدیریت شرایط اورونوف. حالا سرخ‌ها با یک بازی کمتر، فقط یک امتیاز با صدر…</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/141341" target="_blank">📅 14:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141340">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
قضیه پرونده آسیب کتف، پرونده اعصاب و روان و خالکوبی بیرانوند در کمیسیون پزشکی پذیرفته نشد و به صورت قطعی از اول آبان سرباز محسوب میشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/141340" target="_blank">📅 14:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141339">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔄
🔄
هوشنگ نصیرزاده: پرسپولیس با شکایت از آسانی به CAS وقت خود را تلف می‌کند هیچ سندی علیه آسانی وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/141339" target="_blank">📅 14:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141338">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
❌
اول آبان؛ زمان برگزاری دادگاه پرسپولیس و بیرانوند در CAS
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/141338" target="_blank">📅 14:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141337">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfI0YspK-_PYHuarJVNbSbB_OaNaXg-34zMfNpjrTy6kJhixetg6l4kfwevHpYj0pp7i0j59x2tcDfR6tAFthL3TYU4u_2Yh4v4AXYPYhPgeR1Vq_xXq9pMXBRNODwQ9LUhzvyoDQKJ2DYoOLhex7z0rkl4AmHTkwbjbAzwiyMyki1Z5yNFM1_zy3VvyqZuU-5NlnyK6UDJikfz0NRsfJa6m-V3gLxc6qsA3omt5fSX5of0TO7PpSLrZag8A0V4ZrVF09wzO20Mpchvd4XjxniUeihbIY0MdOfvR_jcDzUi0iWxz380axuhQeSk7AJru7XfAbxiG8hOKZza87lQsYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
استقلال در دوحه؛ جدال آبی‌ها با الغرافه برای یک شب سرنوشت‌ساز!
🔥
⚡️
[
الغرافه
🟡
🆚
🔵
استقلال
]
⚽️
الغرافه در ۵ بازی اخیر ۸ گل زده اما ۱۲ گل دریافت کرده؛ استقلال با ثبت ۶ گل زده و فقط ۲ گل خورده، آمار دفاعی بهتری دارد. استقلال در ۴ بازی خارج از خانه فصل، هنوز شکست نخورده و فقط یک گل دریافت کرده؛ نکته‌ای مهم مقابل خط حمله الغرافه.
سناریوی محتمل: بازی نزدیک و کم‌گل با برتری نسبی استقلال در فاز دفاعی؛ الغرافه با استفاده از میزبانی فشار می‌آورد، اما استقلال روی ضدحملات شانس گل‌زنی دارد.
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
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/141337" target="_blank">📅 14:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141336">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
بیرانوند به کمیسیون پزشکی رفت؛ در انتظار اعلام وضعیت نهایی
🖍
علیرضا بیرانوند، دروازه‌بان تراکتور، روز گذشته در نخستین جلسه کمیسیون پزشکی در تبریز حاضر شد.
🖍
بیرانوند که به دلیل خالکوبی به کمیسیون پزشکی اعصاب و روان نظام پزشکی ارجاع شده، همچنین برای بررسی…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/141336" target="_blank">📅 12:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141335">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
باشگاه تراکتور به صورت رسمی به علیرضا بیرانوند اعلام کرده حق حضور در تمرینات بزرگسالان را هم ندارد و باید به تمرینات تیم امید برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/141335" target="_blank">📅 12:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141334">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyIUvYW8qsTuZf4ZfXk4RRwbsePieLpJimRUZ4yV1zzqMLuOkA5a6OZY-LotmwYwWAIs8znvNk4dvBuGMSNao_Ib_8DRSH--nPjCvqVp1IjS6_NalWQSj3kYndEAPq5EcRCR5CF7f_VOi8UnQ38I9oXPEtYf6snJCJQqKIUaTP3CV3on9dZh7d1h5K7obCVjmalDMS6p0kksJTUKFxjzjBXmeEF7Pt9PO2WmMMJFdydsZlTSF0NaiXlsi7x8SDGGzrgeehzyyXePDi4da3TrywL7tv19fI_eSLvB1j3TjY8bCfVbrawOADymX2HZoV90VNznvXjoIVBrX6OG3MesrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پوریا لطیفی فر در بازی با نفت نتواست عملکرد خوبی داشته باشد و مقابل خیبر نیمکت نشین خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/141334" target="_blank">📅 11:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141333">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🆔
| ورزش‌سه:
🔴
❤️
دانیال ایری از بعد بازی با خیبر در دسترس کادرفنی پرسپولیس خواهد بود
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/141333" target="_blank">📅 11:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141332">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEHL7I4dm-eNB-hP_lYbczfAvoa7FyhWMOKAyO3Hqtk2xto9z_vrUUGVF4mX_b_o6SY9HHTwYjZFs82k3rZnYTgAg-j-fkYyQU5iiE7ZKpWRGnqGBJxSUlIffTnguhI9n_XkIomoKn_AkIrAqmPXB88EQcXWUNcCd2yVI_4DmRbmIK08QlLQYx5AZExBbsYl7WtMeGGWMCmxTksGkOITtI7ItCsO3oxxLwzSJdvFHbzeDnbr7XJVmCVXNbtMOYBw4oYobkG2t4-17hvT_tvyorN8dhx8090UrUyTY5rrRfrx81BypJbk2brvm_GRrDsmANbjXAe6OgdETgWXNdSU0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اورونوف با به ثمر رسوندن 4 گل دیگه، تبدیل به برترین گلزن خارجی تاریخ باشگاه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/141332" target="_blank">📅 11:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141331">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
| فوتبالی:
❌
مدیران پرسپولیس در دوراهی تمدید یا فروش اورونوف قرار گرفته اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/141331" target="_blank">📅 11:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141330">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🎙
تاج :
✔️
امیدوارم ورزشگاه آزادی بهمن یا اسفند امسال وارد چرخه مسابقات لیگ برتر شود.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/141330" target="_blank">📅 11:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141329">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❤️
محبی؛ ترابیِ جدید برای اورونوف
⁉️
⭕
محمدمهدی محبی در ۷ بازی با ثبت ۲ گل و یک پاس گل، عملکرد قابل قبولی داشته است پاس گل اخیر او روی همکاری با اورونوف، نوید شکل‌گیری یک زوج جذاب را می‌دهد
🔴
محبی می‌تواند با تبدیل شدن به مکملی شبیه ترابی برای اورونوف، هم به…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/141329" target="_blank">📅 10:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141328">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TO_OEFfR_XL0ZOtbOLFTzYTAXpHm54QAcbI8TYMYg5CEChRHLEUAxkWXDWFyF-tEXSGM3e7s0K3eF0954m4wY3yyfrCdqnZdw016TwdTnSLof2TsMsq6BnbIrdqNKVdTwXXuMU61suHhdddszOJMQ33nBuNqMR4Wij7BBUQzXVyj5VCg65KQ1FyCxOJTMG1z2i7skVADpqyxebK5jZhXZRVv1d6yfpG7xjx5ITI3ODjT6ztnaIvGl2XXQ8jZLIrMUJ-y9JXAKvdcqO1TJSDD6SsvPv9rML1QfnEhMhg2hD5ARKhOV_Rr3NCjKJuXlc77qvMfSj5OqqgE9aXnFiE3xA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/141328" target="_blank">📅 09:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141327">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVdbmetEeINfr5qnuCGdz0N0ZghN92NKWHWucO0Yxfz-ILchcyoj-bOctwfmZpKO_uu7hRZeMGL6-QBaMy3g3p9atfvqzYiSN64HtUZxFLMiysmGKaA19eBJnjiP8XLsuA8RwOc4QgjDGIkMBe3KYbJRsVoEAI7DUxKsyqK6wghc-rFaHJn6Q6FZAcRQJ5GktIl_hopF3bt941aT9MCCOABopTx6sy_4R4W4Fczl56KwQ8NFoC17hcJbyirytN06xcX4je5feCxjThaT3cfeHibYsdY8Bqpn23t_Ab3ANA-KpLdVjIG2U7_H0mFm5l0p5r02R9EIaKAIj33_vwh_Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
تراکتور در مسیر قدرت‌نمایی؛ الشمال آماده غافلگیری!
🔥
⚡️
[
تراکتور
🔴
🆚
🔴
الشمال
]
⚽️
تراکتور با وجود شکست در بازی نخست آسیایی، در ۹ بازی اخیرش ۵ برد و ۲ مساوی داشته و از نظر دفاعی آمار قابل‌قبولی ثبت کرده است. الشمال با میانگین ۲.۲۲ گل زده در هر بازی، خط حمله خطرناکی دارد؛ اما میانگین ۱.۶۷ گل خورده نشان می‌دهد در فاز دفاعی آسیب‌پذیر است. تقابل قدرت هجومی الشمال با ساختار دفاعی تراکتور، کلید بازی خواهد بود؛ تراکتور شانس خوبی برای کسب امتیاز دارد، اما غافلگیری در ضدحملات دور از انتظار نیست.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
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
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/141327" target="_blank">📅 01:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141326">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🟥
واکنش علی بازگشا به شایعاتی که برای برهم زدن آرامش تیم ساخته شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/141326" target="_blank">📅 00:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141325">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKemoq-7A8WosTt9itt_H5RtK9YSH4qrWZHT7_mfbwb6LXid0XYNdJcQ8ep6otHPAaLGhdRa0OE60xNX1BIBOCFg2yBvFFvSQw-Bfo2qKskO6k_ocg8CJczGE4wcSiLGiiItW_TKvv-y5OHNTzkuirYWXPJFBVtp2N4nZOaNlJQ3CsHSgBAO-Xog8uQJz1MozWtedBThPk6OtjcGtbvmJn_Ll7jTVDcg6-SUDy8im9lAVtvuOKUX--qVGtMZQ9SpQ3KE0Q8YdByXMLW5lcB42nYnR2EiIpyWOa2gBw_GhYjl2EoeQssgK2IWOQ7AI99GoLIwb5d556dwBRxIbLDalg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
واکنش علی بازگشا به شایعاتی که برای برهم زدن آرامش تیم ساخته شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/141325" target="_blank">📅 00:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141324">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6166ade5b.mp4?token=LerNY1nwBL3xf9dIyq5CjWLTxGnYugcoRPlDzECk7MebttKto-LKZGY22svkfKjb4sZj7iQyxsW2RnMUiLL9JvciKz9tLmvJTzW1LO6DQmVSV36nReC1c1Raut5QOOtd6-y8omAkelWDWWsu2w8d-E3co0m_L4oKbCsRik1S7E2VqN4uj_cx5kSe3yKLiKYN_nMEG99XrShyRUfvog-n7ZJm91Ak1dgFoiTfkNb2RqEAg1cKBjyN1sbwghZvza7tjCI2OOduNkzCV4WIGOnwFlM9F7rjmfgBzN-G-eZhAdslNKW-FZyER27PHGk7QYVQjwDmDvHa3Glw80kq5-kkOYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6166ade5b.mp4?token=LerNY1nwBL3xf9dIyq5CjWLTxGnYugcoRPlDzECk7MebttKto-LKZGY22svkfKjb4sZj7iQyxsW2RnMUiLL9JvciKz9tLmvJTzW1LO6DQmVSV36nReC1c1Raut5QOOtd6-y8omAkelWDWWsu2w8d-E3co0m_L4oKbCsRik1S7E2VqN4uj_cx5kSe3yKLiKYN_nMEG99XrShyRUfvog-n7ZJm91Ak1dgFoiTfkNb2RqEAg1cKBjyN1sbwghZvza7tjCI2OOduNkzCV4WIGOnwFlM9F7rjmfgBzN-G-eZhAdslNKW-FZyER27PHGk7QYVQjwDmDvHa3Glw80kq5-kkOYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
⭕️
⭕️
⭕️
ویدئویی که کاملا توضیح میده چطور یاسر آسانی واقعا فسخ کرده و پرسپولیس باید دنبال حقش باشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/141324" target="_blank">📅 22:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141323">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
پشمااااااااااااااتون بریزه
‼️
🚨
🚨
🚨
با دستور مسعود پزشکیان رییس جمهور جمهوری اسلامی هواپیمایی مخصوص رییس جمهور برای سفر مستقیم استقلال به دوحه در اختیار تیم استقلال تهران قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/141323" target="_blank">📅 22:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141322">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcb792439.mp4?token=mwlr4WmSY9ojECvuUk5EfdPE-BstAYjRYTkp9rKzHiLnWjsI1OCFlmAYHQNaSHYsUqEk8wFi73eJV_KtmcLJLJtT3SXVFTww9QR26igtO7Wp6vUDoMBkQuycZOdu3WMZbtjgB-d5tQbxGLSTbHexSiEDFiVPH-HJjU09J56b6iMC2sWXYzfgc7E1tTnGrCaDcs3Czg-QiZhuo_X-Ko7X8f8aX2GF8UcSnS-AEW7sDMA18jzJtv5NG10K1EEsCvtLH0bmd2vjTVRyVW2rYaAwJyuKxMcLrDYKibtyBOxrV5otQydJ6w6h9cgIYYLGq8KXactHIbtadBvHk0cbO4SoTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcb792439.mp4?token=mwlr4WmSY9ojECvuUk5EfdPE-BstAYjRYTkp9rKzHiLnWjsI1OCFlmAYHQNaSHYsUqEk8wFi73eJV_KtmcLJLJtT3SXVFTww9QR26igtO7Wp6vUDoMBkQuycZOdu3WMZbtjgB-d5tQbxGLSTbHexSiEDFiVPH-HJjU09J56b6iMC2sWXYzfgc7E1tTnGrCaDcs3Czg-QiZhuo_X-Ko7X8f8aX2GF8UcSnS-AEW7sDMA18jzJtv5NG10K1EEsCvtLH0bmd2vjTVRyVW2rYaAwJyuKxMcLrDYKibtyBOxrV5otQydJ6w6h9cgIYYLGq8KXactHIbtadBvHk0cbO4SoTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
🎙
پیمان حدادی: از اول فصل تیم گرفتیم هر یک از تیم‌های فوتبال پرسپولیس گل بزنه، یک زندانی آزاد کنیم و تا الان ۴۳ زندانی رو آزاد کردیم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/141322" target="_blank">📅 22:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141321">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgNHf6ePNZPGikd6xVgFd1wp8W9fBDx8PbzjvJcG_HJUafB-jribnEf-JjCf7Y--Hq7igBo1HWiLn5hn6rwFdGZlEBaERDkFq6fHv8WTfuj5nfDRVUMwH-t_E2Vz9BIwn5GIwoZ1TetMxRgCe__7Kiii74gNkAPdIUeGWqafYZ3ld-VWBf1e_P4bjj1TKkiSDQwbGNvpEnhsZl2ypBVInqfkh7WUG_RG0gWYwDiRoV0FVF5qMmKzkvKHHhPkzcOlAoWjBZouVJ60p5Q3TIDHVVUFri6izLw0ASw3hhe_jQSlxP21MMmmYsEVzlCVbqR9Yrd_fGEIbWwdRkxi1WtLWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دانیال ایری از بعد بازی با خیبر در دسترس کادرفنی پرسپولیس خواهد بود/ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/141321" target="_blank">📅 22:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141320">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jc2-xxwsLgtCq2GaEbtkaJchPTmQrRX4UdcXiZRQZ8XOaqLsthkcyBKq8kXxdJdbu8a7-OObeyPJ9wNKri2XHIBM-jaIxncczUnkhbMf9q67wPnsWdW8Jn9-zNDxVkt--mLEKrPRfyranHi_FUB34-JWndueopZmn4EAJC_6DKmOzRBbgnsvgrr9vFpFCKSHXccga1uKpovtbllH5wRmhm1uBqw2OcVRNPcqNJbUoVOZ56mfbjKqcbroLZHF8GDnG6C53fu3d0dNxwx212dHe-PId7-9HpQ1L6W4phHp8Dby1wkIYl3tYn2QX_ikiZ9EpGEK0bZbAMrcYHHblswK6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حسین کنعانی در صورتی که فردا بتونه در تمرینات گروهی شرکت کنه مقابل خیبر بازی خواهد کرد اما اگه انفرادی تمرین کنه به بازی روز چهارشنبه نخواهد رسید
✍️
خبرگزاری فارس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/141320" target="_blank">📅 22:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141319">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBAcZCX8lPP-WokjUD2xoFvzV6h1Xjae6oQH-Bz0Ue-UknnIHLB90m694OloT-DWxwYue_aLacsyYnEG9HGuInMykOEc06aUfTetr5mqrCSdzNb0kKotsjR9zm0VJPhXxaJcIrBL4Un275yx679rm2BSX9luROZ5pX4tngZG3nMU-0pmavWFSure1TnDvmjF0GkJlgaYAIrvfKbMI2a4RVFCMv6BoJW-5ZEHKJOBPMWEOzjIyQsAxf_50WoSkk8TO1Yjq2Sgw7lnMkYNQFvQMcOCFRtsQmTkYj2n4IzN7_emTr7bM4GAPen1Kyrp5YgFxdMtyHBcly4FTP1htULmVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
فوتبالی: تارتار قصد دارد پست دنیل گرا را تغییر دهد و از او در پست هافبک تدافعی استفاده کند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/141319" target="_blank">📅 22:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141318">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
باشگاه انقلاب تهران به دلیل بی حجابی تعطیل شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/141318" target="_blank">📅 22:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141317">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoyEGO8yZU1-MgKImVYlCcrp8ROvSrc4tFIrlcklrYsdf-PwGDhzCK7bTvezUxnhazgbiRYtcRrTo0fApOA_dmOly_QJg166GPyEMfogKQdY7gneYx1HqrZpPfzKt7q91-AHKsiZk2H6tBNgUFrxbJCu3GoZVCHMMDb7iiHeo3sNAR1iQvk-1KBXBhngAWjgpL3q8ctoQ73y8HYdT6KfgjnN5Uqh4MTadM3MJ_PKz-ne5-l7QUyiyIR-NYtRTuuRdOqajPR0k9mXrjxPv-MCC-QYMqpxu5MiRIMeSppCQsUk2unmTGJh1p3Vta1hwJr4oV_JlPbC8rNprhqclE2Zkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بیانکونری در کمین ۳ امتیاز؛ کالیاری سدِ راه بانوی پیر!
🔥
⚡️
[
کالیاری
🔴
🆚
⚫️
یوونتوس
]
⚽️
یوونتوس از نظر کیفیت فردی و تجربه، دست بالاتر را دارد؛ اما کالیاری در خانه می‌تواند با پرس و ضدحملات دردسرساز شود. کلید بازی برای یووه، شکستن دفاع فشرده حریف و استفاده از موقعیت‌های ابتدایی است؛ هرچه بازی طولانی‌تر بدون گل بماند، فشار بیشتر می‌شود.
سناریوی محتمل: برتری یوونتوس در مالکیت و موقعیت‌سازی، با احتمال بردی نزدیک و کم‌گل.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
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
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/141317" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141316">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووووری
✨
میلاد محمدی در لیست مازاد تیم‌ بلاروسی قرار گرفته است و به زودی از این تیم جدا خواهد‌شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/141316" target="_blank">📅 19:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141315">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBli6yQCPnS5PXQ-nZHegRDsZrolapilSbdIoACc4nMaYgHKBgFGkEqWtz69xz9m3MxNI64kT3efsWJECSke1b21LtRgGWLVMufeXd3pzUFh0ltgASAnhUiLU6CR0j-DdlMIrlwZLKKpOvFY3XA_LyBBhQh14fXDHSui2OmqR9p_zpJXs8xm49kw1_sQ_6EjZJ2RogZaHxDwKpRZMX3rR86eSB9Nwelt0ap6exXZi4MmSr_szFqA23P_gKjxDHFvlOsP7T4qlzvYIQDWwLYv4BaXyUlCim4J5LM67XWiaLmSLixeNoMmtx9HcBeq8XBBn2aFGo1Vlwvm0syTx2lfrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
خسته نباشی آقای تارتار
🚨
🚨
🚨
با وجود انتقادهای ابتدای فصل، تارتار تونسته پرسپولیس رو به شرایط خوبی برسونه؛ از اعتماد به جوون ۱۷ ساله‌ای مثل پویا اسمی تا احیای بیفوما و خدابنده‌لو و مدیریت شرایط اورونوف. حالا سرخ‌ها با یک بازی کمتر، فقط یک امتیاز با صدر فاصله دارن.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/141315" target="_blank">📅 18:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141314">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
پرسپولیس بزودی اقدامات نهایی خود را برای جذب عباس کهریزی انجام خواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/141314" target="_blank">📅 18:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141313">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfLJ_RwsCbeF_5iwTI020hHcUhRiRFSNiNE1GvPhBED8qdRi59CJkhx-evEj0Zajuk7pLivm1QU7x8gpxrO1yneh7THJ22gJ27Cx4Ns1pCItdcARegkRbe4Id3Ewf5Khr9Bq0YV0-5fcxARKoNb5EJbu_-iUhZTc5MpjL86QElCKvsGTGeKw1aCpDSUb4SebamMNZf25_iYeByT_XbLM-eThUQHyJqGtqaJ4hRwUy97lTJPFgcTCudm4H1e1-Zj0GKuXK8e5uL9fSqvyrFV4_KhcZrH5ZAWX2fdwlYH7mo-oai-LVQ0WHSEhvvgLwZdGlCV5eDVjNo_9aucOHG0Ujw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
علیپور؛ کابوس همیشگی صنعت نفت
🔥
🔴
علی‌رغم بازگشت تازه از مصدومیت، علی علیپور در نیمه دوم وارد زمین شد و از روی نقطه پنالتی گلزنی کرد
🔴
او پیش از این دیدار ۶ بار دروازه صنعت نفت را باز کرده بود و با این گل، شمار گل‌هایش را به عدد ۷ رساند تا برترین گلزن تقابل‌های یک دهه اخیر پرسپولیس و صنعت نفت لقب بگیرد
👏
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/141313" target="_blank">📅 18:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141312">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
⚪️
⚽️
تاج: با یحیی گل‌محمدی برای هدایت تیم ملی امید به توافقاتی رسیده‌ایم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/141312" target="_blank">📅 18:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141311">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
✅
مهدی طارمی زمینه آزادی ۸ زندانی شد
👍
مهدی طارمی در طرح حمایت از حقوق اجتماعی و رفاه زندانیان نیازمند استان تهران، زمینه آزادی ۸ زندانی را فراهم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/141311" target="_blank">📅 16:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141310">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
فوری ؛ خبرگزاری ایسنا :
🔴
🔴
🔴
فیفا در جواب استعلام باشگاه استقلال ، پاسخ داده که یاسر آسانی رسما فسخ کرده است و بازی کردنش غیرقانونی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/141310" target="_blank">📅 16:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141309">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
با تصمیم زنوزی، علیرضا بیرانوند تا اطلاع ثانوی و پیش از سربازی خود در هتل تیم امید تراکتور مستقر خواهد شد و حق حضور در کنار تیم اصلی را نخواهد داشت
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/141309" target="_blank">📅 14:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141308">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
#شنیده_ها
⛔
⛔
استقلال با هواپیمای تشریفات دولتی ( ریاست جمهوری ) راهی قطر شده.
⛔
⛔
نکته: تحریم هوایی آمریکا شامل هواپیمای مقامات دولتی نمی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/141308" target="_blank">📅 13:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141307">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
#شنیده_ها
⛔
⛔
استقلال با هواپیمای تشریفات دولتی ( ریاست جمهوری ) راهی قطر شده.
⛔
⛔
نکته: تحریم هوایی آمریکا شامل هواپیمای مقامات دولتی نمی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/141307" target="_blank">📅 13:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141306">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
گفته میشه دولت قطر به تیم فوتبال استقلال قراره مثل آمریکا ویزا ساعتی بده تا این باشگاه برای بازی با الغرافه مشکلی نداشته باشه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/141306" target="_blank">📅 13:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141305">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FU5y_Wik_NcRidKi1S7ufzEYx49r7jqx39nbQQHb7Gvgtj2ovsEBTPRBDyJAzU949WDmcmbvcXEd9iXNK4Op4-Zq9WvAXYdSxS-1T1msfAWj16_ZO9BbzMh0342wR5maWxsv1Pt6lOiLyJzo2aJo0xXwRi8McXcr1nNMEhJspiYP1rfSzV3QJcBWfb8UQdc5ZfxhwSw1inZ7nGjoFlK-0eQSAfORTwe-CDGOhCask60hOgE7iNHHCYdItFBSukkQDRKdGCtB9DZViea_lb86VS6pZFYc0lTI3f38804HKQjClvc8sF5egq59UpISh64tC6uI5a9e2q0Ti3THTGKJ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیژن حیدری داور بازی‌ معوقه پرسپولیس - خیبر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
😀
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/141305" target="_blank">📅 13:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141304">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oy9QpnmesJwo3PNM32Lh8rgNO3SIpGpuZrnem5UIH-jGj5xP_k-WSD7d9VcDFGNeSW8UCmbYkub7zUQrA-vdhOwZnyrNrIoS73stsg-z77CqnJup0bohwEcdqxRfkIKJGrMx5AZW0Ira2idZTe-N3GRQYE2bi1HAL3kODkWvwk5oeZV20-soEM02IDSMVi3yfTM2vg-fnfEmpSkY00UBdUusd9jX0_-02XZbqaamaais0UCKULR6dnL2_FRvRojGrdsY25LsrvPiJktitI6aquIgK0bZG_cJcaeG29z9kzgUZeRJeykYz4KXH8KhaoLtBB36AaTjfrezIsbsyJi_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Liverpool
🆚
🔵
Man City
⏰
Tonight 19:00
🏟
Anfield
🟣
سیتی در ۵ بازی لیگ ۱۳ گل زده و با میانگین ۲.۶ گل، قدرت تمام‌کنندگی بالاتری نسبت به لیورپولِ ۷ گله داشته؛ در مقابل، قرمزها در آنفیلد از امتیاز میزبانی بهره می‌برند. غیبت الکساندر ایساک و کودی خاکپو می‌تونه قدرت هجومی لیورپول رو کاهش بده، درحالی‌که هالند با ۵ گل بهترین تهدید سیتی محسوب می‌شه.
از نظر مدل آماری Opta، شانس برد سیتی ۴۰.۷٪، لیورپول ۳۴.۶٪ و مساوی ۲۴.۷٪ برآورد شده؛ برتری آماری خفیف با سیتی است.
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
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/141304" target="_blank">📅 13:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141303">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjeWCYtGFKLvL_Q_PvXw0G011KjhJ_E_6V8PH75ZhSUOYZvpvX1Ai6ekua1Ia_yYyIJ_QgEMKG12rScqVv33WwtX_9cFuRd1TyXBfGmDdGclUb9AAW5VTRyX8iZFPuUf--9wEn9q3pEoU-opwj80BLbToI0Kai1IVteGN8u8l_KnG5acYvuUrckqbNgOE2MVpg-QwhyegtfDcQdTcYMCXP46UMSsvZZpnKIoO9gqJLvTD-pmJNdHq5EHAtqxjhvrdyLQROpiZUR9eVdscR1RVwcBaIBxlskLTAqSwraTAYSH87dQixgPnI8kGoj4BTnVoV_B-RurqD9auRi_d_-1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ابرقویی تارتار رو راضی نکرد؛ با بازگشت کنعانی و ایری، احتمالاً دوباره نیمکت‌نشین میشه.
🎙
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/141303" target="_blank">📅 12:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141302">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇮🇷
👤
🎙
برانکو ایوانکوویچ: می‌توانم بگویم بهترین نتایج ایران در 40 سال اخیر را من به دست آوردم؛ قهرمان بازی‌های آسیایی شدیم و به جام جهانی 2006 صعود کردیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/141302" target="_blank">📅 12:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141301">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
درخشش سرخ‌پوشان ازبکستانی پرسپولیس در رسانه‌های کشورشان!
🗣️
ایگور سرگیف با پاس گل در دقیقه ۵ و اوستون اورونوف با گلزنی در دقیقه ۸۴، نقش مهمی در پیروزی ۳-۱ پرسپولیس مقابل صنعت نفت داشتن.
🗣
درخشش این دو ملی‌پوش ازبکستانی مورد توجه رسانه‌های کشورشون قرار گرفته…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/141301" target="_blank">📅 12:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141300">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
⚽️
گل‌های پرسپولیس در بازی تدارکاتی دیروز مقابل فولاد هرمزگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/141300" target="_blank">📅 12:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141299">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
باشگاه با انتشار این ویدئو نوشت : نگاهی متفاوت به شانزدهمین گل ارونوف برای پرسپولیس
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/141299" target="_blank">📅 12:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141298">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf86a8d14.mp4?token=uCo6nmSHMBp_gSFPcTryTaLN0djp7t2ls-XlCz5ut_RUEtyDA3WgqPdMt3OqOFnaQRDQU257NcGrwJlHlvDD_cuoJDKH9vepBpKuvXr0QMK3WYRWLYcf4z6S3xnJ8DVPnX0_3PvAQsMB0lgoqAQMyTS2JuJdVOW6bRWAvxOgQHTzcdjVdOkbAzURUUdtAM_SEhMQU1P8EtTCTnZO5ZXpkorD8fNFg6becfjrwY6xHG5uiYmrUY97Thqfgz7FzUhbELk_XlStXo8p-Y7b91nPstgxvPl64UxLjApFQ6IvidiZAS5njqpbeH8guS-geMalip0M39tptzv_qgn6rAaubQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf86a8d14.mp4?token=uCo6nmSHMBp_gSFPcTryTaLN0djp7t2ls-XlCz5ut_RUEtyDA3WgqPdMt3OqOFnaQRDQU257NcGrwJlHlvDD_cuoJDKH9vepBpKuvXr0QMK3WYRWLYcf4z6S3xnJ8DVPnX0_3PvAQsMB0lgoqAQMyTS2JuJdVOW6bRWAvxOgQHTzcdjVdOkbAzURUUdtAM_SEhMQU1P8EtTCTnZO5ZXpkorD8fNFg6becfjrwY6xHG5uiYmrUY97Thqfgz7FzUhbELk_XlStXo8p-Y7b91nPstgxvPl64UxLjApFQ6IvidiZAS5njqpbeH8guS-geMalip0M39tptzv_qgn6rAaubQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
باشگاه با انتشار این ویدئو نوشت : نگاهی متفاوت به شانزدهمین گل ارونوف برای پرسپولیس
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/141298" target="_blank">📅 09:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141297">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-byaDr-RMts1_iDrlTaJve1Ma-5zZA_JDBdlEZA6Q4T4NMWYSvgyJEuh6I6q1LvLvl6m9c-SEkc_bcaFjOr9QhWHvsSRqRvlwdj_yBo2hqjU3qmRQTheZWncBg99YqRwodEh0E9XpAIstsgjyTCYgmtbMPPY0Pl6b5XQTYInWo1tCM3JRl83drOO4gT3Z_XGii_BIJXEmRQRo7XZMEYhw4GGUSZH-lxbc0mR8dJ6-I9kQVtIscQuvBLnKMuYJQIz0x6onr8Opu-Ky_oJRice41HkNRJBLhAEcVi_86wSWn4ultSHVw1-8iUZBjkc0oep8I7ueYG-iGidrrfKb4SRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهرآبادی از هفته‌ی بعدی فرصت بیشتری برای بازی کردن برای پرسپولیس دراختیار خواهد داشت.
✍️
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/141297" target="_blank">📅 09:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141296">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R12fohg2q0AtjEpZXx8Yz-LJ7aWMWAm7eZnV8T2n2vMsSgFRt-H9bHJJOv1kRcD6kB7KrXiAisgahz8bLdoAfIn2lw-_8hTm26i05hPKg_zgP5b4w-QeBRENfeEZUmb0BcBxFzLRiys-N4yE26GgLHdryZtxwkxtJwflxK6o8YYIKT5V1lfLtHIO2cG1_6YVur7EMPiShuw9nq3WvCyg5Dxwvl7SpM5_I6g5SkxzGF4-T0eJCx1edL3KA9sAMeLmZ5UXpW1QpyhMvto6nR8-mS-EaKCTWKWdM2fwEtwyxDVsVcPEeNjnP9AIsLOEjInN3Zb_M-4qQaXsZi-9LvJENw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/141296" target="_blank">📅 08:54 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
