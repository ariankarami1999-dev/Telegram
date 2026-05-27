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
<img src="https://cdn4.telesco.pe/file/Eh98jeztykIUJ13-IGr-8Ye0_IZWdCBtRygvPkqV49v_ocQO1XkiTAlnMe-FGskVCpdgul-537QZXgLRyfNZJSm4xy4JNfVLPp9CsLxBjWR6e9310A2WZpV-0K6s4Csbgaq5gj1Gy4-ZUF3FpU5WBB-a8h7pXg-X7NYLPrgnw8HPlqJ85HmsNw_cy0Dko3OPWzP1BWfl86ecAjsrcHr1KpyWMDBaa3B72GAhf5vyQbS4xRjpNtBFLPM8PJeWf50vHtzZkLSXOwqRpiuxj_0XQN0zkDymHXv3UruUZaL_6U2JxBLu-ay_Oyc2yHJTr9A0JkjgKdO44nfkOEwSgugCAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.7K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 17:51:40</div>
<hr>

<div class="tg-post" id="msg-132324">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎙
🔴
پیمان حدادی، مدیرعامل پرسپولیس درباره اتفاقات چند ماه اخیر حول باشگاه:
۱۲باشگاه به صورت کتبی گفتند بازی‌ها برگزار نشود!
بازی‌ها باید کامل برگزار شود و در همین اردیبهشت هم می‌توانستند برگزار کنند.
امیدوارم نمایندگان ایران براساس جدول پایانی و پس از ۳۰هفته، معرفی شوند
در پرونده بیرانوند علاوه بر منافع ملی باید منافع هواداران پرسپولیس هم در نظر گرفته شود،برای بازی با ملوان به دادگاه CAS شکایت کردیم.
به هیچ بازیکنی اجازه ندادیم که سر تمرین نیاید پرداختی‌های پرسپولیس نسبت به بقیه تیم‌ها بیشتر است.
نمی‌دانیم آیین نامه نقل و انتقالات برای فصل بعد چگونه است، برخی می‌گویند می‌توانید بازیکن خارجی بگیرید برخی می‌گویند نمی‌توانید یا ممکن است دوباره سقف قرارداد تعیین کنند.
کمیته اجرایی AFC پانزدهم اردیبهشت جلسه دارد و ممکن است سهمیه فوتبال ایران ۱+۲ شود
درحال حاضر محسن خلیلی با حفظ سمت، وظایف پیروانی را انجام می‌دهد، نام وحید امیری و کمال کامیابی‌نیا برای سرپرستی تیم مطرح نشده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 547 · <a href="https://t.me/SorkhTimes/132324" target="_blank">📅 17:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132322">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
‼️
واعظی، مدیر رسانه‌ای استقلال: تیم ششم جدول نباید دنبال رفتن به لیگ نخبگان باشد. آن‌ها حتی در جام حذفی هم نیستند. ما حتی شانس قهرمانی در جام حذفی هم داریم. پرسپولیس فقط فرافکنی می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/SorkhTimes/132322" target="_blank">📅 16:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132321">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔰
سرویس VIP
🔰
5 گیگ 400T
10 گیگ 700T
20 گیگ 1150T
25 گیگ 1350T
40 گیگ 2T
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SorkhTimes/132321" target="_blank">📅 16:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132320">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
‼️
واعظی، مدیر رسانه‌ای استقلال: تیم ششم جدول نباید دنبال رفتن به لیگ نخبگان باشد. آن‌ها حتی در جام حذفی هم نیستند. ما حتی شانس قهرمانی در جام حذفی هم داریم. پرسپولیس فقط فرافکنی می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/SorkhTimes/132320" target="_blank">📅 15:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132319">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
‼️
واعظی، مدیر رسانه‌ای استقلال: طبق قانون، صدرنشین باید به لیگ نخبگان برود. حتی اگر ما هم نرویم، پرسپولیس که رده ششم جدول است، کجای کار است که اعتراض می‌کند؟ تراکتور، گل‌گهر، سپاهان و چادرملو حق اعتراض دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/SorkhTimes/132319" target="_blank">📅 15:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132318">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
پیشنهاد رسمی باشگاه پرسپولیس به رئیس سازمان لیگ: حالا که‌مجوز حرفه‌ای باشگاه سپاهان صادر نشه استقلال و تراکتور رو به لیگ نخبگان آسیا بفرستید و ما رو هم به سطح دو لیگ قهرمانان آسیا.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/SorkhTimes/132318" target="_blank">📅 15:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132317">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز
🔴
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس هنوز باشگاه وارد نقل و انتقالات نشده و منتظر اوسمار هستند!
♦️
لیموچی و هر اسمی که به گوشتون خورده در حال حاضر هیچکدوم شون صحت ندارن و تا این لحظه باشگاه هیچ مذاکره ای با گزینه ای نداشته به بازار گرمی ها توجهی نکنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/SorkhTimes/132317" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132316">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
🔴
شنیدم اقای کشوری فرد گفته هیچ باشگاهی جز پرسپولیس و مدیرعاملش اعتراضی نسبت به عدم برگزاری لیگ نداره…!حالا که یک فرد دلسوز داخل باشگاه هست که برای احقاق حق باشگاه میجنگه و پاپس نمیکشه اقایان بی تابی میکنن و تاب سربلندی پرسپولیس رو ندارن.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/SorkhTimes/132316" target="_blank">📅 15:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132315">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
🔴
شنیدم اقای کشوری فرد گفته هیچ باشگاهی جز پرسپولیس و مدیرعاملش اعتراضی نسبت به عدم برگزاری لیگ نداره…!حالا که یک فرد دلسوز داخل باشگاه هست که برای احقاق حق باشگاه میجنگه و پاپس نمیکشه اقایان بی تابی میکنن و تاب سربلندی پرسپولیس رو ندارن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/SorkhTimes/132315" target="_blank">📅 15:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132314">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
وزیر ارتباطات: اهتمام رئیس‌جمهور به بازگشایی اینترنت و احیای ثبات ارتباطی، نشانه‌ای روشن از عقلانیت و ایستادن در کنار مردم است. ملت ایران شایسته ارتباط آزاد، آینده‌ای روشن و اقتصادی پویا است .
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SorkhTimes/132314" target="_blank">📅 15:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132313">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
محمد حسین صادقی: در پرسپولیس بدشانس بودم
🔺
وقتی بازیکنی به پرسپولیس می‌آید، طبیعتاً نیاز به زمان دارد تا خودش را با تیم هماهنگ کند و به ترکیب اصلی برسد. واقعیت این است که در چند برهه زمانی از این فصل، آماده قرار گرفتن در ترکیب ثابت بودم، ولی مصدوم شدم. …</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/SorkhTimes/132313" target="_blank">📅 14:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132312">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
وزیر ارتباطات: اهتمام رئیس‌جمهور به بازگشایی اینترنت و احیای ثبات ارتباطی، نشانه‌ای روشن از عقلانیت و ایستادن در کنار مردم است. ملت ایران شایسته ارتباط آزاد، آینده‌ای روشن و اقتصادی پویا است .
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/SorkhTimes/132312" target="_blank">📅 14:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132310">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
حالا که مسئولان باشگاه پرسپولیس خواستار برقراری #عدالت برای دادن سهمیه آسیایی شدند زمان این رسیده ما هواداران سنگ تمام را برای باشگاه عزیزمان بگذاریم
◽️
در تصویری که منتشر کردیم خواستار رسیدن سهمیه آسیایی به باشگاه عزیزمان پرسپولیس شده‌ایم و کمپینی به راه…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/SorkhTimes/132310" target="_blank">📅 14:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132309">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0ISr4cDgMz4tkDFpcQxuQkxIUzO0OTrHb41VfkduNnMLDduHROE0fEweh2jE7C923gfaeeEm7ap4f6OO9N2RqJgXr23YPQOHY2mUEnPXexD4DNFAvebadHvB_37x7wZLImuh9Y8EyhjpeHDJdJt03pAbUW75OMMCRl1Wwryl-vMlDqzggPO0Qfgv7sCDu77YYp3_0bfYcA0FUIe_mH5Cc2ht-TUGHWBbDWRNe87bOU-M1QxTGLN-uBD2_5rstoXxacj9pQSmjVfz3DeEWktRorrEKQh-Pu13QHR3GSH2pSOolZqg1RGzeL0xDuH05Zzfq8asQfmwVgEZW9Qjicdqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حالا که مسئولان باشگاه پرسپولیس خواستار برقراری
#عدالت
برای دادن سهمیه آسیایی شدند زمان این رسیده ما هواداران سنگ تمام را برای باشگاه عزیزمان بگذاریم
◽️
در تصویری که منتشر کردیم خواستار رسیدن سهمیه آسیایی به باشگاه عزیزمان پرسپولیس شده‌ایم و کمپینی به راه انداختیم
◽️
از تمامی دوستانی که در این حوزه فعالیت دارند از کانال یک‌نفره تا کانال و پیج میلیون نفری خواستار نشر دادن این کمپین و تصویر بالا هستیم
#پرسپولیس_آسیایی
#سهمیه_آسیایی_حق_پرسپولیس_است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/SorkhTimes/132309" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132308">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCwJujpcn0iiGVjVRV1lvJpwnc6QRvFrEJ0PW2xy9FGajol1A-CPAoKk56MA7bzmANFjZhIxb5NCnP9GGiCEqngQxI7QVIldj_E5b7CEr9xM9odpROZ0TYXY6fUqsWUbi1N2um3PlxhhInQax_XaAYo7f6UJ4TWr3kx9eqn3BWqkFRao7hbTF50zIorvaHztepO7dr-7taglwwx4kEeLfG--DRY6d2M-PSHTgnk946F7cLXMd7xpv5PgDhus5SNbmRT5yBazxCK51Cbajak8x1upKaiAkk7LXPZt2ow6BgpGNNr25ntdUnmAjNFXljvUCNFYToGiarmw4VwsEEJVSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
بونوس خوش‌آمدگویی
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران جدید، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/SorkhTimes/132308" target="_blank">📅 14:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132307">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
درخواست پرسپولیس از CAS
2 امتیاز استقلال و تراکتور را کم کنید
❌
پرسپولیسی‌ها سال گذشته پس از اینکه کمیته انضباطی فدراسیون فوتبال، باشگاه ملوان را در دیدار با استقلال و تراکتور به دلیل استفاده از یک بازیکن غیر مجاز (سینا خادم پور) بازنده اعلام کرده بود، از ملوان شکایت کردند و خواستار اجرای همین قانون برای خود شدند اما این شکایت در کمیته انضباطی و استیناف رد شد.
❌
باشگاه پرسپولیس اکنون و در شرایطی که قرار است نمایندگان ایران در آسیا براساس جایگاه‌شان در جدول مشخص شود، از دادگاه CAS درخواست کرده تا زمان رسیدگی به این پرونده و اعلام رای نهایی، به دلیل شرایط خاص موجود دستور توقف رای کمیته انضباطی صادر و فعلا تا مشخص شدن تکلیف پرونده پرسپولیس، 2 امتیاز داده شده به استقلال و تراکتور کسر شود.
❌
شنیده ها حاکی از آن است که دادگاه CAS نیز در این باره از فدراسیون فوتبال استعلام گرفته تا بعد از آن درباره درخواست پرسپولیس تصمیم بگیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/SorkhTimes/132307" target="_blank">📅 14:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132306">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpqkBWQWwLd-4OO_JFmKmvYguMMTnzArPec3ntjoAqgKCUOmpk9A0-kyYQicLpKtZRKFCLoxEfiFY1evp-EfQU2cr0XHYvyNhFiMTQ6sp5R9YjvFAvl2NghfZygrSaMM05XRPF0BI45ufJPCsQpUEIYCgjbVqgDItB2WWO9NleHXgB_2HKTMAlmdlLo5Lc2y6qTON2-SVxssqQgIIoiqiTgVYycpS5jc5kU8d1fqsAb2_hOrzywY8fJQ6SJ0mo591BAkh4tt-AZgV2Tziy0lmSmaubDdlwaV2clFDuphp4WbI6lngNiB5chA-vOowXfwb1ib6b04rNDtqhSAC8vRfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🟢
یک فروشنده در تیخوانا مکزیک، برچسبی با تصویر تیم ملی فوتبال ایران را نشان می‌دهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SorkhTimes/132306" target="_blank">📅 13:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132304">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
وزیر ارتباطات: اهتمام رئیس‌جمهور به بازگشایی اینترنت و احیای ثبات ارتباطی، نشانه‌ای روشن از عقلانیت و ایستادن در کنار مردم است.
ملت ایران شایسته ارتباط آزاد، آینده‌ای روشن و اقتصادی پویا است .
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SorkhTimes/132304" target="_blank">📅 13:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132303">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
سردار آزمون به زودی با انتشار یک پیام عذرخواهی به تیم ملی بازخواهد گشت.  #خبرنگار_فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SorkhTimes/132303" target="_blank">📅 12:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132302">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
ایسنا: مهدی لیموچی در آستانه پیوستن به پرسپولیس قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SorkhTimes/132302" target="_blank">📅 12:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132301">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
طبق برخی خبرهای ضدونقیض؛ تندورهای حکومت فشار زیادی آوردن تا مجددا اینترنت بسته بشه و هر لحظه امکان داره این اتفاق بیفته. اگه کاری مهمی دارید سریعتر انجام بدید. چون هیچی قابل پیش بینی نیست.
✅
هنوزم بسیاری از آی پی ها فیلتره و اینترنت اختلال زیادی داره.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SorkhTimes/132301" target="_blank">📅 12:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132300">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
باشگاه با یک بازیکن از سپاهان به توافق نهایی رسیده و این بازیکن داره فشار میاره که با این تیم فسخ کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SorkhTimes/132300" target="_blank">📅 12:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132299">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
علت کندی شبکه اتصال زیاد است به مرور پایدار میشه
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SorkhTimes/132299" target="_blank">📅 11:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132298">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
مهدی هاشم نژاد وینگر ۲۴ساله تراکتور:فکر می‌کنم خط خوردن من ترور شخصیتی بود. دوستانم در تیم ملی گفتند که خط خوردن من برای آن‌ها باورکردنی نیست.بعد از مصدومیت قلی زاده همه فکر می کردند فیکس باشم اما دعوت هم نشدم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SorkhTimes/132298" target="_blank">📅 11:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132297">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
مدیران باشگاه پرسپولیس در روزهای گذشته با ایجنت پوریا شهرآبادی ، مهاجم جوان گلگهر جلساتی برگذار کردند و خواهان شرایط جذب این بازیکن شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SorkhTimes/132297" target="_blank">📅 11:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132296">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
شهاب زاهدی که به تازگی بازیکن آزاد شده؛ تمایل دارد به پرسپولیس بازگردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SorkhTimes/132296" target="_blank">📅 11:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132295">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
✅
مهدی لیموچی در آستانه پیوستن به پرسپولیس قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SorkhTimes/132295" target="_blank">📅 11:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132294">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
نماینده محمد امین حزباوی امروز پیشنهاد مالی‌ مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SorkhTimes/132294" target="_blank">📅 11:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132293">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🟡
فسخ لیموچی با سپاهان؟
▫️
به احتمال فراوان مهدی لیموچی به دلیل عدم گرفتن دستمزد خود در سپاهان با این تیم فسخ خواهد کرد و مقصد احتمالی وی پرسپولیس خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SorkhTimes/132293" target="_blank">📅 11:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132292">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ma6HOfcAFIG_9yK_JmzqBa_AXyP9pKjIBUuDOfFO3kI7O2Z2N-6UqYSzosGyMOLQqiE6Lhf4byNKT7HnC7CWdaTALlDxomleD8cKiw0JIUD9jJpyTVZ9oifS5AdSkkZ6yGlMpwwKF5o18C2AczmJauJl1nin0EUsGPO6ZyrnsguvFDPooTYSrTqj1vSt2-fYssVvMKa9j11cscHbSLentLiuX-3CLHN9ldvm0MmLR4CrBhZcZcay5fOOhlK53n87OE-rZF03rg3NVNderiPrdHfRURgtDE6N5-vARvP34kshqRFrkhZukD3c-wl7d4o_gHo3FNF8V5l7fxFgT-lSlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهاب زاهدی که به تازگی بازیکن آزاد شده؛ تمایل دارد به پرسپولیس بازگردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SorkhTimes/132292" target="_blank">📅 09:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132291">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
🇮🇷
جهانبخش نزدیک به یک‌ماه است که مصدوم است!
⚪️
مصدومیت علیرضا جهانبخش فعلا مرتفع نشده و این بازیکن فعلا امکان همراهی تیم ملی را ندارد. این در حالی است که 23 روز از مصدومیت جهانبخش سپری شده اما این بازیکن همچنان شرایط تمرین ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SorkhTimes/132291" target="_blank">📅 09:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132289">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlPZMLhCxeDHPpgmLEFnBzbyyS9l-urWpIwSwL35G9qoSUrR2Piu4nR_0QTG_oLUdNpQM1hxw7hI3YmywCCwDmeHwiif3OWmJLiYKa1pSEqvWaMZZrLmBAxO8uVWeMY1n80OTxEiylQfxN8ENk2jbZJLVw_hk4aw1Z6cjYZBQOeHiFG-wmYYsh1z9G3nMnOhG8TTeNl6aIY5Y5uS9bGMCxpY9HMFnvx623TV9llQBs2iwWYYQsD1-qvd2HsiY5ig7MwlUcibrhpYAZVrTDLDfmRKuVPF2_KSyjCfSAMuQYUMYt1oa1JTjbLmVYjTu1cB6lJnKylGJv3H9MIlcLPmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت فعال شد!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد سایت وینکوبت شوید:
👇
🟣
ywincob.com
🟣
ywincob.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/132289" target="_blank">📅 01:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132288">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
کارشناس صدا و سیما : وصل شدن اینترنت متوقف میشه و دستور رییس جمهور اجرا نمیشه چون خلاف دیوان عالیه.
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SorkhTimes/132288" target="_blank">📅 01:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132286">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b15265d538.mp4?token=mE6idckFMHl2p5VJD6mHU_QvXEX8FB2KF7Z19GNn6XMk-VWBjqrvkhIEizGHJJHFGfEbW51jnUPOrJx24PSJEx0h9DFuZIvQd4CcpuFQsV214k0c_BXTpx643iIpxIhHvo3y3qaoGVgzDRV-m72BpCtnPMm0IKW0tHx80ZpWi5zOsEIcqep00D-BelWkdhQgrPKyd39Ni0lHu_yRoWcPvLlb4OtEZ0ZKTo1Q0MG8Sykr7cTU0wH26L7T8jJfARJ6_XteDm3zr1gw1rtLpXu9v9eFK3nFQBx8fpwgK6-m5z0Og2dobMuwZ_KR6eiGtToh3iDnIYom5aPgHo-a_3gQzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b15265d538.mp4?token=mE6idckFMHl2p5VJD6mHU_QvXEX8FB2KF7Z19GNn6XMk-VWBjqrvkhIEizGHJJHFGfEbW51jnUPOrJx24PSJEx0h9DFuZIvQd4CcpuFQsV214k0c_BXTpx643iIpxIhHvo3y3qaoGVgzDRV-m72BpCtnPMm0IKW0tHx80ZpWi5zOsEIcqep00D-BelWkdhQgrPKyd39Ni0lHu_yRoWcPvLlb4OtEZ0ZKTo1Q0MG8Sykr7cTU0wH26L7T8jJfARJ6_XteDm3zr1gw1rtLpXu9v9eFK3nFQBx8fpwgK6-m5z0Og2dobMuwZ_KR6eiGtToh3iDnIYom5aPgHo-a_3gQzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| نورالدین الدغیر خبرنگار الجزیره در تهران:
🔻
همه چیز انجام شده، چیزی باقی نمانده جز امضای توافق
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/132286" target="_blank">📅 01:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132285">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP9t7gk6BwCSZi-M1jXaOAV7N7RExxxNpQbLDnv-FupDmJ_wmIQhO5whOeVnkHEmstpq4o1Pox3QRE-qptI08phKJZLj0sZ1eiv6fHLgSOIAnVhI2ZGmmAt4w5AMxXf7pf-WEDG3-ZtKr8HWy9dqIThfig0sx8ZGs569_YLJmbyy1vs-T6BfsFD3vf7mfQDRjE147q8uMV7VrFxM9fgCnZu2AuTN6ufiBe9dAuL-gONP0Oxtgu-uWSlDu81pBHXMZTUzxgQ27x4rVYXdcAGcAsiQG8HP_CDmcxsDNlUelLMFbcr2c2cIpMHd1Fw4-sJflI-Ry9hA0JLb5Kn50mPVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🔺
فیفا اوکی داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SorkhTimes/132285" target="_blank">📅 00:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132284">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔹
سهراب بختیاری زاده فصل آینده نیز سرمربی کیسه میماند
😍
✍️
خبرگزاری ایران ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SorkhTimes/132284" target="_blank">📅 00:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132283">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
با معرفی نمایندگان ایران در آسیا؛ پرسپولیس شکایتش‌ را به فیفا می‌برد
🔴
به دنبال معرفی نمایندگان ایران در فصل بعدی رقابت‌های آسیایی، باشگاه پرسپولیس اعتراض خود را در این خصوص با ثبت شکایتی به فیفا خواهد برد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SorkhTimes/132283" target="_blank">📅 00:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132281">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
سرعت اینترنت در زمان قطعی بیشتر از وصل بودنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SorkhTimes/132281" target="_blank">📅 23:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132279">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🟥
فروش سیگار
به صورت نخی ممنوع شد تا
جوونا دیگه راحت به سیگار دسترسی نداشته باشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/132279" target="_blank">📅 23:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132278">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❗️
اینترنت سراسر کشور وصل شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SorkhTimes/132278" target="_blank">📅 23:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132277">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
شایعات
🔴
مدیران باشگاه پرسپولیس با درخواست ویژه اوسمار با مهدی هاشم نژاد ستاره تراکتور وارد مذاکره شدند
‼️
قرارداد این بازیکن با تراکتور به پایان رسیده و هم اکنون بازیکن آزاد است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/132277" target="_blank">📅 23:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132276">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
نت بلاکس: اینترنت ایران کامل برگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SorkhTimes/132276" target="_blank">📅 23:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132275">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🟥
تیم ملی ایران برای هر بازی جام جهانی فقط چند ساعت ویزای ساعتی آمریکا را دریافت می‌کند و بلافاصله پس از مسابقه به مکزیک بازمی‌گردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SorkhTimes/132275" target="_blank">📅 23:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132274">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
یک بخش از صحبت مهدی تاج اشتباهه.
🔴
اونجایی که میگه اگر‌ کمپ تمرینی تیم ملی به مکزیک بره، مشکل ویزا حل خواهد شد!
🔴
ربطی نداره!
🔴
شما کمپ تمرینی رو به موزامبیک هم ببری، برای برگزاری سه مسابقه باید وارد خاک امریکا بشی و در نهایت به ویزای این کشور نیاز داری.…</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/132274" target="_blank">📅 23:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132273">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
الان چیو دقیقا وصل کردید؟! مردم ۹۹ درصدشون قطع هستن…!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SorkhTimes/132273" target="_blank">📅 23:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132272">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
ارزش امیرحسین محمودی ستاره ملی پوش پرسپولیس به 500 هزار دلار رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SorkhTimes/132272" target="_blank">📅 22:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132271">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
به روزرسانی جدید :  اتصال مردم به اینترنت بین الملل به ۸۶ درصد سطح عادی رسید و در حال افزایشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SorkhTimes/132271" target="_blank">📅 22:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132270">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نت بلاکس: اینترنت ایران کامل برگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SorkhTimes/132270" target="_blank">📅 21:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132269">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULdfoPx2cNdSvp8QRRttpZonVm0MM26m_AXZqQ2C701tA_gPfq-GcpCmUPFrA_5Rkri_03ISclADl1twMk9anh5_WSvTIVYYNHghWg7TboUayQ7WAGJ4GjbR1llf9YJr52ETLmcsw6hiMixFZXDgPpv8IhZGDkCt2fa6p0ok4tA9D1QStrEaBPE1etPzqqMdSiDwAMlOWd0y4PnCMlYj5QDgbzdUjodmoNylIAyWGdTRFujkWn3kYBSR6vx-AfAp3NSccwu9CcfzXr2UFEMWwUkjQL-6cPcuK2uZlSF5l_O-X1MA0KPpHVLfe98bHHJvsZ2SsCgIcEJiXbK80AiGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نت بلاکس: اینترنت ایران کامل برگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SorkhTimes/132269" target="_blank">📅 21:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132268">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIn3czSOufU-X95b_m9hG9ez6Hmoyk7nA9ACOG-JfR_Y5LNTt4qvMRaYdVxFqyr4yXjBWtgBAe48Y0Dts6PsJwDkVfc4yQhW-NugGSIOxf_Iib0aHPuwCZvhwgqdM4tsMwY1THxke3KBEdzjpGFJUnZkC0aBamr0Kmf7KkbOmkd7az10ZZjreKI0OYYUpmkGBQI31lA_LC9OykmrYWOr9PcVL0rWub2MSw49Mofc4FjVUjVlac60nywxtsENbPB9XKAqvP1Bup985WyKv3dT2uK0zuJdFi7uLn27NYhsYwMc53Bq6guDZWSI4MUTe63izk7d7uQhEroQrAye42H6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی سریع و مستقیم به وینکوبت
🟢
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی انجام می‌شود:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🟢
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SorkhTimes/132268" target="_blank">📅 21:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132267">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
💢
🇮🇷
🤝
🇺🇸
📰
الجزیره به نقل از یک منبع آگاه: میانجیگری قطر به توافق آمریکا و ایران بر سر دارایی‌های مسدودشده تهران منجر شد!
🚫
به لطف توافق بر سر این موضوع که برای ایرانیان از اهمیت بالایی برخوردار بود، احتمال قوی وجود دارد که توافق میان آمریکا و ایران فردا اعلام…</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SorkhTimes/132267" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132266">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
وزارت ارتباطات:
🖍
اینترنت گوشی های همراه هم تا ساعاتی دیگه وصل میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SorkhTimes/132266" target="_blank">📅 20:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132265">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
‼️
وضعیت اتصال اینترنت بین‌الملل کشور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SorkhTimes/132265" target="_blank">📅 19:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132264">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZYoAZmSDXTRvju4smjyZVri3RFgNw7dZhAIxOFdiTv8DjiHmU0axuiodJ0acRu_y9_mtnxEGXvdkgcrKPw3ajXTX4T7erFQCi5_KvnWKGJbCz-g2Vis9iYm_xL4K_UVgAA4Ok3uoK6THtzueUFqveoRa7W4qT5daZABqH7AXhNUOZ0MIwnjG40fYbbzPG5yNxCmGwd6xL77HkM90-RwlYilF2TQ_PVHwaNxkcEQnlZlZHiedA22Ype7AeXu75xYr-uJ6S2szn1utiLkdVSfPaUYiCWLrzgX_TO_joMlO8nbhwh3ocza-1XyLtneIMOPgvOrTJI4NDCRCepJWjCG4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‼️
وضعیت اتصال اینترنت بین‌الملل کشور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SorkhTimes/132264" target="_blank">📅 19:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132263">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔽
وزارت قطع ارتباطات:اینترنت همراه، امروز (سه‌شنبه ۵ خرداد) وصل می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SorkhTimes/132263" target="_blank">📅 19:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132262">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗️
تسنیم : یحیی گل‌محمدی به جز باشگاهای عراقی یه پیشنهاد مالی خوب هم از تراکتور داره و ممکنه بره تبریز!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SorkhTimes/132262" target="_blank">📅 19:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132261">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSoKfFxq70pJuoEkpBooK7rrdWBRBR1Fh-m6_HfO2uN-GQGKgFKs1Ti3Ic8r05uUKfCwig4a2TyccFJogzQbJNR_mbwaWnO0ZRBRRSKR_M_Cay5TViyupePFq2JBbkHLlo8_SW7I4-2PrxOdi3t2KRBuFHp2AfzDO0gdKslu7diL0yMg_cII_2ovWlwPCZExWComBEbsrC24o6l-kZpInxdLhThL2q5ZZsN8FIwSIQ3Iaf-9xY61GFHJHM1sTC27UwNGPoKCiMzalbFRWUCobMqlyElsDTgyQypDfbKk1UuqmcSd8Hvc5wnL54P5hPP5i_PcetSaEcWiot1onqiC7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شایعات
🔴
مدیران باشگاه پرسپولیس با درخواست ویژه اوسمار با مهدی هاشم نژاد ستاره تراکتور وارد مذاکره شدند
‼️
قرارداد این بازیکن با تراکتور به پایان رسیده و هم اکنون بازیکن آزاد است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SorkhTimes/132261" target="_blank">📅 17:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132258">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
پس از ۸۸ روز قطعی و ثبت رکورد تاریخی ۲۰۹۳ ساعت انزوای دیجیتال، نت‌بلاکس لحظاتی پیش تایید کرد که اتصال اینترنت در ایران در حال بازگشت است.  وضعیت فعلی در یک نگاه:
🔹
اینترنت خانگی و ADSL: اکثر شرکت‌ها وصل هستند.
🔹
اینترنت TD-LTE: ایرانسل و مبین‌نت وصل شدند.…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/SorkhTimes/132258" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132257">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
تیم فوتبال دهوک عراق به یحیی گل محمدی پیشنهاد داده اما یحیی میخواد تو ایران مربیگری کنه!/فارس
🚮
امپرور جان لطفا هر گورستونی میری طرف های خیابون شیخ بهایی آفتابی نشو…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/SorkhTimes/132257" target="_blank">📅 17:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132256">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
دوستان از برخط به online شدنتون مبارک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/SorkhTimes/132256" target="_blank">📅 17:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132255">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
دوستان از برخط به online شدنتون مبارک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/SorkhTimes/132255" target="_blank">📅 16:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132254">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
خوشحالیم که دوباره آنلاین شدید
❤️
🔴
خوش برگشتید؛  امیدواریم تا شب دیتاسنتر ها هم متصل شوند تا کسایی که وایفای خانگی هم ندارند به اینترنت متصل شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/SorkhTimes/132254" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132253">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
نت بلاکس:
🔻
نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/SorkhTimes/132253" target="_blank">📅 16:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132252">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AS-WtFUv7LJl3jtpbyt6HRDh6kNo9sTG-i745kwCA46tppGL8ON1IZzET2uLRYV8cE--GE_IpZG5vTsptmYk9h3dq1J0cLBG0q2YnVlbl4lIUy89TjeF7tT4iVY9tjBSmXisL-REbQ9ZOv4DnUaa8_XOB-kfPUy9i0oyUOi6jL3uVFql8pvsepXdmzSrhVhZr9XRCrhIm4XnCGRWh7qHbG_jvx2fczrD-CdVzU27JCjUAoMdZX1zk2EG7DCajejINCLVXsJiDpKv0kiapKah36Gl-aEieu9X_9Xkcf6bZktruEo8o-OmCSRLC7Z9Vp-erm_DeXrsOovXLCnKnv2QHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نت بلاکس:
🔻
نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/SorkhTimes/132252" target="_blank">📅 16:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132251">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
خوشحالیم که دوباره آنلاین شدید
❤️
🔴
خوش برگشتید؛  امیدواریم تا شب دیتاسنتر ها هم متصل شوند تا کسایی که وایفای خانگی هم ندارند به اینترنت متصل شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/SorkhTimes/132251" target="_blank">📅 16:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132250">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‼️
خبرنگار «انتخاب» دقایقی پیش کسب اطلاع کرد که ۴ نفر شاکی حقیقیِ «توقف اتصال اینترنت بین‌الملل» هستند. این ۴ نفر که گرایش سیاسی آن‌ها کاملاً مشخص است و تحت راهبری یک مقام ابقا شده‌ی دولت رییسی، دست به شکایت زده‌اند، عبارتند از کامیار ثقفی، رضا تقی پور، رسول جلیلی و محمد حسن انتظاری!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/SorkhTimes/132250" target="_blank">📅 16:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132249">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwHDOL9ozB7VKQNo8KBN32eMdhC0va5t-GDt7UejtkYTfiNqi9Fh-cJYj51dJH-_YTY6esvVZ7Hrq-nWWv3WRa1lbdfICEqfu333PRiFs7_6dXrFB_j4fXghwYt5pwYyi9J1zqFmgWSaKtMhG2cSSGFK1sJHc-_-pCPFt3AAhF-N5_HOCQAaONyJhi2LVk8WfsVnWKr5c2VpK6jwJeZOUaROgJ76HaleWxge7yLYG0XGXNZV99QP5GBy9qS5QqpRPlLkPPUPwd3LRXIP5AYIjfiVEKFQEbPH2fJEARe5BHeOetbSARHfXTkzL_xvmg2HqvoDLi_E8H7W436Zl-g4AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
بازگشایی اینترنت به دیتاسنترها رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/SorkhTimes/132249" target="_blank">📅 16:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132248">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
نت خونگی وصل شده .تست بگیرید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SorkhTimes/132248" target="_blank">📅 15:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132247">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا ۲۴ ساعت آینده
🔺
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی تدریجی اینترنت…</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SorkhTimes/132247" target="_blank">📅 15:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132245">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoGxFW1_hMmkjKD-ss7qUTFeypKBrY0fhJKEQmCcL-ToBW-jd2ss0-QklHOkE7vpmySe4GWrvwX5R5Fz_vcuZCajCebUnZ8WJz44dXYYVy1ro2QXNr8GuPVaQBvXoL95TAXiQDa0S-m_vcpZZecUJimmhshkAcP5M84I2tor6ercY0q_rQYl2hwb4TrMWo7Sr-mQ4BOmCubzhDc4Fk3qip-Exu8Y6PSWIvbcY2D0jbZi4ts9nZ9gnfhhV7uA-lGPAYkZae-GgY0THBiN6xFb-WBny4Bb1lTxrIqlzcIM8_MvWVIczrg4rOOpm0oru1ucbMwHtpTM-34ebPyL9bFkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
فسخ لیموچی با سپاهان؟
▫️
به احتمال فراوان مهدی لیموچی به دلیل عدم گرفتن دستمزد خود در سپاهان با این تیم فسخ خواهد کرد و مقصد احتمالی وی پرسپولیس خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/SorkhTimes/132245" target="_blank">📅 13:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132244">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا ۲۴ ساعت آینده
🔺
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی تدریجی اینترنت تا دقایقی دیگر خبر داد و گفت:
🔺
دسترسی کامل مردم به اینترنت تا ۲۴ ساعت آینده میسر می شود. بر اساس اعلام یک منبع مطلع، برخی سرویس‌ها و پیام‌رسان‌های بین‌المللی نیز به‌تدریج و در چارچوب فازهای بعدی بازگشایی شبکه، در دسترس کاربران قرار خواهند گرفت و در فاز اول بازگشایی قرار ندارند.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/SorkhTimes/132244" target="_blank">📅 13:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132242">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c57ee64b0.mp4?token=Uum4U7qs8p4r3wp6--_PMlHUoCt9_66gInz6MY7pCreTnPA7lYjKX1lBygtVtixLSD-N145hW0QTGkSFTD6pAAQgYz4Qon_O2FlvLYBG4K1kz8DYTb5PpuBe1A9KswGlzSOV_kkuWWRE8Z6HZqYXiMcBKPCKp8p6pLeOMZhtRRlKf6M7zM5ModSNGsro0ZUMCgJtGvQzn2JUATRsfh63ol2DqiixI-SM243jRbORUyOgFFNY5d5aKWf_eAb12XehvVUhpgEYxHIbb-o5w87-yYUfILmJh62Pd5rdm-AZUsx1CKbxCJ1xohxArpJ0JIM3G-5aRCXmDr6Ymvx__eVFYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c57ee64b0.mp4?token=Uum4U7qs8p4r3wp6--_PMlHUoCt9_66gInz6MY7pCreTnPA7lYjKX1lBygtVtixLSD-N145hW0QTGkSFTD6pAAQgYz4Qon_O2FlvLYBG4K1kz8DYTb5PpuBe1A9KswGlzSOV_kkuWWRE8Z6HZqYXiMcBKPCKp8p6pLeOMZhtRRlKf6M7zM5ModSNGsro0ZUMCgJtGvQzn2JUATRsfh63ol2DqiixI-SM243jRbORUyOgFFNY5d5aKWf_eAb12XehvVUhpgEYxHIbb-o5w87-yYUfILmJh62Pd5rdm-AZUsx1CKbxCJ1xohxArpJ0JIM3G-5aRCXmDr6Ymvx__eVFYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کانفیگ فروشا وقتی از خواب پا میشن و تلگرامو باز میکنن که خبر هارو بخونن:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/SorkhTimes/132242" target="_blank">📅 12:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132241">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
وزیر ارتباطات: با دستور رئیس‌جمهوری و پس از برگزاری ۳ جلسه فشرده کارشناسی، فرایند بازگرداندن اینترنت کشور به وضعیت قبل از دی‌ماه ۱۴۰۴ آغاز شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/SorkhTimes/132241" target="_blank">📅 11:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132240">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
وزیر ارتباطات: با دستور رئیس‌جمهوری و پس از برگزاری ۳ جلسه فشرده کارشناسی، فرایند بازگرداندن اینترنت کشور به وضعیت قبل از دی‌ماه ۱۴۰۴ آغاز شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/SorkhTimes/132240" target="_blank">📅 11:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132239">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k12Ydv_QyrP7p_LJbxWQisM1jU767JOUMftLe4GtC6Ujg8y7yxLtqQZOH6EVfQLUWC13fR9Vmngi3yHti8L6mucHhFpv0WrvLt1-STqmS5_JtB143IupkCBbO57rxdxYr8Z9s97uDAB_YOzc_FADhYyDAEjdgs__gOT_4QZxPV7LCCmutPbpB8Mai3o5s5zqqMoF3FKMXlyp2aqjjZsHR0D2duInCq8g5kA8_eilqrLIBkMDPR4DJXU2P-t3Bi_MmbUphdK7RfMXf0apg_GxKceBFaHcuzGnPk0Y5tZR8hrf7CloPGFA7kthXrRCXKpMM6G8YBG0wqkG_QsUTMolPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسبت به دیروز وضعیت اینترنت بهتر شده و از ۲ درصد به ۳ درصد رسیده
😂
خوب نتیجه میگیرم در آستانه بازگشت نت هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SorkhTimes/132239" target="_blank">📅 11:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132238">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❗️
ایسنا:   دستور باز شدن اینترنت از فردا اجرا میشه
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/SorkhTimes/132238" target="_blank">📅 10:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132237">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
شهاب زاهدی قرارداش را با باشگاه آویسپا فوکوئوکا ژاپن تمدید کرد و خبر از بیخ گوشمون گذشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/SorkhTimes/132237" target="_blank">📅 10:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132236">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulZt61_ZMdS2czuPtpi34uL3T2mMSYqVT2tFsYqTDfXuiKnbioxgX2AJ76MWBDaenBQ_VSj4yoi7lDwBY4OC1KKa6TpLgAMKCJZMEW-tlp67OVTgYILFDUTwbaFKoM9MCctbhEqJJF4pkZwvT2H02wSjz6cXfhr5MNkN8eWO86EI85-4FKq7L3JrH9Ntd5MFrs5CNYpxAChaySJAMqnWQmA34DOU9j7IHPsocIR85yHPYEcyMWWDL3YNu24UCSoic090JIpATGXweL0Kh1LPllknJYQvHdDTEZGw-j7p-unLWAvAcyGwr4m73lVYzNFrRjN1few8St0WQFYAUCW1Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا ساعاتی است جیمیل در دسترس کاربران ایران قرار گرفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/SorkhTimes/132236" target="_blank">📅 10:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132235">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvSahx_8PyGXNxwyYT4Yy9CGfaRwbe06kOil8AbUFTOhvAUbVhDhe7F85Yqb6oOhroXC4tnNIqhoIL_SVhX-sB0tqdsgWKsh0CF1F5cplQcDc7P8syWo110TnoXEEM4_ejwzojqiSGSFHbb-ophZQdk9w6BRwZvoUVAfsN4YKMTGJrIdOe969Ng60O7SPVL6QMhdrMt2sLNswRBVmjeyY3HHpd1R1T2qmAkl3ICe3OAzRtKKWhbMl1TK4nzQpJyo0AsqcP5yDaLH6HJwkUKwZ5uXXtUvzQp1Y5oyL5H5Stu-kuymk3ZmpJmzWSneHal8bFIs1QqnkS3zmyhPOGWRjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صفحه اینترنت پرو از سایت همراه اول حذف شد
✅
شکست رسمی اینترنت پرو
همراه اول صفحه ویژه اینترنت پرو رو حذف کرد
✅
روسیاهی موند به اونا که خریدن
🖕🏾
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/SorkhTimes/132235" target="_blank">📅 10:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132233">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AahBFHHiP8oh1_1sEV9-cJXyjvq7gtZXVxvvJPR55kaHxyLCQ_2rn3PY3Mk2nucysCFDbFk4azt0xJH3C_RsQq90RzHS_R0CXo8ykc5fJGeLupM0DkO6Y4LWciy5y3wwXX4rvEgXBW9XZhMEFJwUQhjqcxgcv8uPLdTOP15YSRdoX16pGcLpjAu-7RaM4hPEB-t4sjca88NXeqiMJx_T9f6Uksvy3dugysydnbEvjmptwdXGqgwWRgFhtkxnrMKA4yDXFiSSw5m1ZToTNh-t7R2Pn4dNkaKVwRlc3NnOMbfL7xJQ1_W63RhW2p0orh3jT-ttBSpAYhkXfsk6nTFFZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
از بین شهریار مغانلو و علی علیپور؛ یکنفر از لیست نهایی تیم ملی برای جام جهانی 2026 خط خواهد خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/132233" target="_blank">📅 10:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132232">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❗️
ایسنا:   دستور باز شدن اینترنت از فردا اجرا میشه
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/SorkhTimes/132232" target="_blank">📅 10:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132231">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXb-ttY38QW-CELTln9IWa7pnKk8XCbNaCe56Z4S9xL0uv3GyM_o413GaheuwVw_d9CF1tNKNLXr9eIGz5hhRhziGUUZvkc1Hyj-wbiibL0rzsP9qYwL8abFnU7TSsxJpqepyGHjnJL_3s_y3Y-4sJ1gL2Px2bKpNUPry66lh2mANpUbLa3StUjYwp6kCXOc9ysPI6ghf0JQchLfzEqXJ_WgGb-D314O0g8YWsalfzbIKsTZgwjZ6c9y9kQl0nLIgnA1O6TfQ8QtYbTBj88AqFhhAAF4t7Vwb4VT6J-xnSeXGpLnjL6S1VThNAvR29hfraAQmphYKQNSl8zpkIe8vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ارزش امیرحسین محمودی ستاره ملی پوش پرسپولیس به 500 هزار دلار رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SorkhTimes/132231" target="_blank">📅 09:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132230">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1Z3GAw4PVoHRImyw4_LGdH3oYUula_mRAyVjGiUkpIYYI8AK8N4tqadtJxFbVn9r6xkhh_JhXMrlJyeDx5O_Ll8dslf62zaQT5uKPtmQdkRUJ9yNZS5FuCsJg5KIYHfozO_uw4Xv90qf69Dtmn3L9BlANvQLtXuCBrFbpiO4cFFoBHmr8yyWT4c49o9KMcpmgZKheIAY6baG3c5LBBkVCOZEcue2HsbE32knaxHj16i-Piy3z-dYIzbi4D-nqkL-H6GHXahDxXdHDrYMLKY0D4xDS3vSnG6cxYn6UAH1Lw4e_DU_ZupJNUi-UOqU0fYDx7pebgtEUjj5ic9nWzWGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شایعات حاکی از این داره که سردار آزمون به زودی به تیم ملی برمیگرده....!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/SorkhTimes/132230" target="_blank">📅 09:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132228">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a864573491.mp4?token=kZYcc2cMtLq-9z9OnXOcAPg6DoNIbOfQtH7SedkTgRTmT4nyE6czjZs7DnXtkhxpgNygobk0Uou2XBhMMtKsNkSZ3gDYZnEHAyVF6Qj3Mt8-8riQeolcfHImfOUOPGehFCVzC7jlTWwgEjip_UBa5QOSztxFvcmw1CtCG8qsYDUsMFFZMm_id1cTp6cb91doTojxqVpi890KSLHdhTx6rtcXKgB_AECKYmEWt0uyb--BZjE0xIquAoGs11sVifCLY6OPuleDCzR9fJ1CnGNNZqLOj8QNsSc1u6iVSlTU0QD_BKFGG_9OiTcIC-ldBMcSIZxIDyAmi9mjVRnTVTvCwA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a864573491.mp4?token=kZYcc2cMtLq-9z9OnXOcAPg6DoNIbOfQtH7SedkTgRTmT4nyE6czjZs7DnXtkhxpgNygobk0Uou2XBhMMtKsNkSZ3gDYZnEHAyVF6Qj3Mt8-8riQeolcfHImfOUOPGehFCVzC7jlTWwgEjip_UBa5QOSztxFvcmw1CtCG8qsYDUsMFFZMm_id1cTp6cb91doTojxqVpi890KSLHdhTx6rtcXKgB_AECKYmEWt0uyb--BZjE0xIquAoGs11sVifCLY6OPuleDCzR9fJ1CnGNNZqLOj8QNsSc1u6iVSlTU0QD_BKFGG_9OiTcIC-ldBMcSIZxIDyAmi9mjVRnTVTvCwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوری
| ترامپ:
🔻
«اورانیوم غنی‌شده (غبار هسته‌ای!) یا فوراً به ایالات متحده تحویل داده خواهد شد تا به خاک آمریکا برده شده و منهدم گردد، یا ترجیحاً با هماهنگی و همکاری جمهوری اسلامی ایران، در همان مکان منهدم شود،
🔻
یا در مکانی دیگر که مورد قبول باشد، با نظارت کمیسیون انرژی اتمی یا نهاد معادل آن بر این فرآیند و رویداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/SorkhTimes/132228" target="_blank">📅 01:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132227">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔹
کالدرون: کاش می‌شد کارم را در پرسپولیس تمام کنم
🔴
اگر می‌ماندید پرسپولیس قهرمان می‌شد؟
فکر می‌کنم تیم در آن زمان شرایط بسیار خوبی داشت و ای‌ کاش می‌توانستم کاری را که شروع کرده بودم را به پایان برسانم، اما متأسفانه این اتفاق نیفتاد. به نظرم ما تیم را در مسیر درستی قرار دادیم و یحیی گل‌محمدی هم پس از حضورش کار خوبی بر پایه‌هایی که گذاشته بودیم انجام داد.
🔴
پس به خوبی پیگیر اوضاع پرسپولیس هستید!
در این سال‌ها تغییرات زیادی در سطح مربیان و مدیران باشگاه رخ داده و پرسپولیس همیشه باشگاهی پرتحرک بوده است. بازیکنان زیادی هم تغییر کردند؛ بعضی از بازیکنان مهم زمان من مثل شجاع خلیل‌زاده، مهدی ترابی، احمد نوراللهی و علیرضا بیرانوند از تیم جدا شدند و برخی مثل حسین کنعانی، علی علیپور رفتند و دوباره برگشتند؛ بعضی دیگر مثل محمد انصاری امروز مسئولیت مهمی در باشگاه دارند.
🔴
خبرهای بود مبنی براینکه باشگاه پرسپولیس در پائیز سال گذشته قصد داشت شما را دوباره بازگرداند؛ مذاکراتی صورت گرفت؟
همیشه شایعاتی وجود دارد، اما شایعه فقط سر و صداست. تنها واقعیت این است که در حال حاضر من سرمربی پرسپولیس نیستم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SorkhTimes/132227" target="_blank">📅 01:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132226">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f501face.mp4?token=UAzFkdRrQdfvBrxcSYUhIJvcBBMvgokRPqgILEJEIydETmYrz7VYGa5rCcypFw8XgKJg9cN8UF4hPSwvShE9Qak96TSt21C0Nw-8YfW542I45ZLWNBHi7KT4BDBeYkA6ysTnU23tgFtz36ks1t5f4im4ImhWjkqLdSrPfyZoEELS9VTdhodFQSMBq6TKhwhgXsmlu_zVjPX_Eom2zB0Dl-8vZ5lxH9o9SFTWhpt21i8i86mQ2zFj3bLnkmAqb6vLqj9oePQaRfIVXB4qzwA4LKeHMNATLTrTxJcHUkaq1yuq12ygIk1zuOotf3YgM3qK24BYhBQwR-viTgtHAbqaiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f501face.mp4?token=UAzFkdRrQdfvBrxcSYUhIJvcBBMvgokRPqgILEJEIydETmYrz7VYGa5rCcypFw8XgKJg9cN8UF4hPSwvShE9Qak96TSt21C0Nw-8YfW542I45ZLWNBHi7KT4BDBeYkA6ysTnU23tgFtz36ks1t5f4im4ImhWjkqLdSrPfyZoEELS9VTdhodFQSMBq6TKhwhgXsmlu_zVjPX_Eom2zB0Dl-8vZ5lxH9o9SFTWhpt21i8i86mQ2zFj3bLnkmAqb6vLqj9oePQaRfIVXB4qzwA4LKeHMNATLTrTxJcHUkaq1yuq12ygIk1zuOotf3YgM3qK24BYhBQwR-viTgtHAbqaiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
بازگشا سخنگوی باشگاه پرسپولیس: پرسپولیس برای برگزاری مسابقات اعلام آمادگی کرده است هم زیر ساخت داریم هم پشتوانه مالی
🔸
این نمی شود که بعضی تیم‌ها بیایند نامه بزنند که ما نمی توانیم در لیگ بازی کنیم و بعد همین تیم‌ها هم توسط فدراسیون برای آسیا انتخاب شوند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/SorkhTimes/132226" target="_blank">📅 00:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132225">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiEB0Wi1puFPg30YgGQaJuRwm0XuiBhMNukP5Dj3l9tOOvFBpre3jJ2dS6tTQgxLtyssHptLwX_NOEjwkYKeVdQssBDjLNOxyi96iscx5EkFnsHDtoo8lctvPKwEbGRvzXkdt9jqjx0tPTXg-6wu1j3qfLAZH8P0dSFd-VthwT2nwp9V7AjzW-iuNOYK7_YZn2fydsi0QqTpx-mQI9YSqdjHQXTBA2wbs2lxZPXLvVFAECXOInvU8bTLz8D8hvuvU7NwcVYdZnr1puZ77s_wk47JAAFkn0jjUBV4qmZCjNUQortQlim6eJXTcW3Y10hGjrzdVLBPsjTI2bsevMcsbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق آخرین آپدیت ترانسفر مارکت امیرحسین حسین زاده جای ارونوف رو در صدر با ارزش ترین بازیکن لیگ برتر گرفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/SorkhTimes/132225" target="_blank">📅 00:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132222">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تو بندر عباس صدا توافق میاد</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/SorkhTimes/132222" target="_blank">📅 00:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132221">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
الجزیره:  احتمالا توافق بین آمریکا و ایران، فردا (سه‌شنبه) رسما اعلام میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/SorkhTimes/132221" target="_blank">📅 00:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132220">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تو بندر عباس صدا توافق میاد</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/SorkhTimes/132220" target="_blank">📅 23:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132219">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
سه نمایندهٔ ایران در آسیا مشخص شدند
✅
استقلال، تراکتور و سپاهان ۳ نماینده فوتبال ایران در آسیا خواهند بود. این تصمیم را هیئت‌رئیسه فدراسیون با توجه به جدول کنونی لیگ برتر اتخاذ کرده.
❌
اگر سپاهان موفق به اخذ مجوز حرفه‌ای نشود در آن‌صورت تیم‌های رتبه‌های بعدی…</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/SorkhTimes/132219" target="_blank">📅 23:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132217">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihKbBpTP9yw05wFjrVkCbz5WL9a38IRZfeKf8e9kACIyeO2mRV2JGPw2CTKcQhT-lBeBpSvYd34UUwppysjxJ4ZvvySYK2vesKqL-ohOgX9fdQ9xQoc5bbIJF1ROmrQhwXIlHmyRe88yn7SykMX6QyPoVAOkxFc_O8aGBYKHMLoKQHSvaONtgx00diwKDTSQW0wkl-BQhNFdHDSKoy1O5m6inFpRkXzCHHArS-4cZldOXgzJqgELiTh6rZyTDi8b7_KmXwqpdWVLdsNJR2DML331G9yfEyX3FW9d66inAbqOFSvQHANFIadLKg1_wTEFXI2EyhVvHYe81oTGSijigQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
پیام‌ نیازمند در جدیدترین آپدیت سایت ترانسفرمارکت با ارزش ترین گلر ایران شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/SorkhTimes/132217" target="_blank">📅 23:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132215">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
👈
نورالدین الدغیر خبرنگار الجزیره: احتمال دارد اسرائیل پیش از هر توافق ایران و آمریکا، دست به یک عملیات نظامی بزرگ در لبنان بزند
🔴
با هدف استفاده از فرصت زمانی باقی‌مانده تا توافق ایران و آمریکا.
🔴
یا برای به شکست کشاندن توافقی که بر توقف جنگ در جبهه لبنان…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SorkhTimes/132215" target="_blank">📅 22:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132214">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
واکنش باشگاه پرسپولیس به معرفی سه تیم اول جدول به عنوان نمایندگان ایران در آسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SorkhTimes/132214" target="_blank">📅 22:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132213">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
و بلاخره بعد از نود روز وصل شدن نت بین الملل و شاهد خواهیم بود ...حال الان کانفینگ فروش و خریدارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/SorkhTimes/132213" target="_blank">📅 22:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132212">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTB-kyfm0nshhR0SlhlFkpH-buF6AsCjM5l_bDuWfcaoCB7bvYrD4WQ-_swIWinPXPS2JRANvMBJJe8CilJUnrJlCL-mrrXXh6ojiqiCGbamm7VslrgYNUlUcuON_NsZCkCGVJwtRrG4kvS47iXGXfgm5Mu4rW3Z2NBvUt9TPYq_EHF__VKCe79_anOCxxriaLij7W80gbQz6HfqtOicycjiLQY7oQyCuGYt4Rk1nALpaWicB17loES_8a9_pw52N3IXHAXYFKGniasULbaaeEumH9ayuc_7KpTbXVYzUcYmKyMabV95UjTHG2sTzpVZD_SF1-CbLPVvuNHaSBKU2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
واکنش باشگاه پرسپولیس به معرفی سه تیم اول جدول به عنوان نمایندگان ایران در آسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/SorkhTimes/132212" target="_blank">📅 22:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132211">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
🚨
خبرگزاری های داخلی خبر دادند که اینترنت بین‌الملل از فردا به تدریج در سراسر کشور وصل می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/SorkhTimes/132211" target="_blank">📅 22:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132210">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
فووووری/ مدیر روابط‌عمومی وزارت قطع ارتباطات خبر داد: رئیس‌جمهور دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SorkhTimes/132210" target="_blank">📅 22:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132207">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
ادعای عاصم منیر:
🟢
توافق ایران و آمریکا در آستانه نهایی شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/SorkhTimes/132207" target="_blank">📅 22:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132206">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
فووووری/ مدیر روابط‌عمومی وزارت قطع ارتباطات خبر داد: رئیس‌جمهور دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SorkhTimes/132206" target="_blank">📅 21:53 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
