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
<img src="https://cdn4.telesco.pe/file/OQdFS8p7admIQ0dQJUIAhcgxEIYB-MWg6Hz2_WksEfOBMutrdeLYyYNyxB7sYsXl25UJjWq4-4wkffKK7Pl6g1hZD2LYS1vLZZBv6XmQX6WwyiT7wpGyaXZaxZu-jTBTyMpDl0IJZJTjXMieFgIVA1TYVWGJnfsJ21EgzBAVRtsYfbAU27itIeDXrQk8eH2Ld7x32sLD-oBAZNptMHYxDcoZsoeAEy9jRZt96X98YmD6lxyYKGK-0BE74ZG1XBTpcEHNv6UEUdwUXR7SCM3aPzg9uFfSJahFJ5LIpeJyFtLVrOy2W_o1idD3VbDFERdfo1HzhMiXfFZc64MifLfJiQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 15:03:20</div>
<hr>

<div class="tg-post" id="msg-132179">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umUxa70bsHfH6e0DIZQU2hZfHfOZJKL0U9H9QoKncLlwxcCMvJusS1O46rBYl1KMcacan9E4rUvv5jSQko9q-hISiX_Ru7_fQYwwZgakG4dW6jf_lKa49_hLL86KFJu5MnF8kbvcc077glPh9tQ5EK5kWOtGHL4z3QDnAm829fprjrmrBf-oHPEaDvi9Vf1NWxU6F-Pr5q7vdWetjVD6qJ7W5VsU0rZ5JldKqS3Oyc7ueoB6bx5sLaCa-o2a3DFYQ1IVLzO0hXTgK9xPivwRNyvITNFT4w7n0X9XZG9LuDNAFf7SFsj6pGQZvQuBg2MCOx5dxd8asKUEw_z3W1GNSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرزیدنت ترامپ : یا توافقات من با رژیم ایران بزرگ و بسیار مهم خواهد بود و یا اصلا این توافقات انجام نخواهد شد و به جنگ باز خواهیم گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 314 · <a href="https://t.me/SorkhTimes/132179" target="_blank">📅 14:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132178">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Awp18ng6t_CncfjmdoiBCnVONg_AobMJ4kTCDsPfeh2tRLXKm1tuF3hbnXt-tg_3Sz5m_KwR-cZvKwGtA2yj51FxMaQQGOoRWLJZ2XZu27UAaLJOSuGJwS_j3vHEnLjsgKSC6BtPNOiscnHNpzssMZfW7GGbM4jKlUbnOf7CkAe7KujdfDKnpDjWueKb1O9tUHdjQDB95c_12R6dfq3ABW4TJZSwQDkIKNJXzG8gAAnL3yvHDAAiCX_t-TGg9xHcQSJ6kl2yScvxXtCMD0HX5YT0kIK33lOd31hm3CfOlb6V-4f3zUU87a9CSfnyeQpQdHJ2li-9MgEz7Gb11uMyyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی هاشم نژاد یکی از بهترین بازیکنان چندفصل اخیر فوتبال ایران که توسط قلعه نویی خط زده شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 339 · <a href="https://t.me/SorkhTimes/132178" target="_blank">📅 14:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132177">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpnBVDkfR34pQOiW6kUpdch1o7i7aIfIz455TmJcUNehTiAwjUvsnwi9VaUEQdMI9NMOW97-aPKm8K8dkOdxNY83oRDuyjmQMbx470AghOOn3p-gdHZO_2olP1itipPPiUKDqksXIH2CARwa1HfuwUn98HBYBGoi5n58jGof4J6CIS9IKSOt07A8wuonnX1-R_xK3X41xx9vJ_hDUaHYT-JMk9xaNjWGiz0m3i7oJybFdHYuwuyJAPImsaihxPpKROMnFTPjbea12cZhgPKoQXx9VzGYp-FI5XkgEEQYjUDAQ0sPg2ov5XAXdo-72DuXr2WZIm64RVUyFOKEWV7u3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت فعال شد!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 328 · <a href="https://t.me/SorkhTimes/132177" target="_blank">📅 14:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132176">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
یک منبع به فارس: در این جلسه برقراری اتصال اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف تصویب و برای تأیید به دفتر رئیس‌جمهور ارسال شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 435 · <a href="https://t.me/SorkhTimes/132176" target="_blank">📅 14:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132175">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
فوری؛ علی علیپور قبل از اینکه بره همراه تیم ملی ترکیه با مدیران تراکتور جلسه ای برگزار کرده و به توافقاتی رسید اما امیدواره بره جام جهانی و با قیمت بالاتر لژیونر بشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 563 · <a href="https://t.me/SorkhTimes/132175" target="_blank">📅 13:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132174">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
یک منبع به فارس: در این جلسه برقراری اتصال اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف
تصویب و برای تأیید به دفتر رئیس‌جمهور ارسال شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 539 · <a href="https://t.me/SorkhTimes/132174" target="_blank">📅 13:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132173">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔰
سرویس VIP تک کاربره
🔰
1 گیگ 190
2 گیگ 380
3 گیگ 570
5 گیگ 950
10 گیگ 1700
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 612 · <a href="https://t.me/SorkhTimes/132173" target="_blank">📅 12:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132172">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری/ بازگشایی اینترنت بین الملل مصوب شد
🔹
سیتنا خبر داد: ستاد راهبری و ساماندهی فضای مجازی صبح امروز دوشنبه (چهارم خردادماه) به ریاست دکتر عارف معاون اول رئیس جمهور تشکیل جلسه داد و بازگشت اینترنت به وضعیت قبل از دی ماه 1404 مصوب شد.
🔹
این مصوبه برای رییس جمهور ارسال شد و در صورت تایید رئیس جمهور جهت اجرا برای وزارت ارتباطات ارسال خواهدشد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 594 · <a href="https://t.me/SorkhTimes/132172" target="_blank">📅 12:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132171">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔰
آف ویژه سرویس VIP
🔰
🔥
10 گیگ 1.8T فقط 1.4T
🔥
50 گیگ فقط و فقط 5.5T
🚀
50 گیگ به قیمت 40 گیگ…
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود  جهت خرید از پیوی =>  @Winstn_Churchill</div>
<div class="tg-footer">👁️ 655 · <a href="https://t.me/SorkhTimes/132171" target="_blank">📅 11:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132170">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
اینترنت بین‌المللی تا یک هفته آینده در دسترس قرار می‌گیرد
🔴
مشاور وزیر و رئیس پارک فناوری اطلاعات و ارتباطات کشور از احتمال دسترسی و اتصال به اینترنت بین‌المللی در هفته آینده خبر داد و گفت شرکت‌های فناور با دریافت IP ویژه، اکنون از اینترنت بین‌المللی بهره‌مند…</div>
<div class="tg-footer">👁️ 645 · <a href="https://t.me/SorkhTimes/132170" target="_blank">📅 11:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132169">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔰
آف ویژه
سرویس VIP
🔰
🔥
10 گیگ
1.8T
فقط 1.4T
🔥
50 گیگ فقط و فقط 5.5T
🚀
50 گیگ به قیمت
40
گیگ…
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 644 · <a href="https://t.me/SorkhTimes/132169" target="_blank">📅 11:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132168">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esHMTq9lrRjmZuBojxBRCHWeVmFoP8YGL1guIXslzlmGFasTxwojrgjOdmA8OSOLbdx59RJHFnKztqcvmTojIw_4rzoY_2_Xdzel0Qskx2liVmOLeiPza7YCm5GoY5zhPuaOOpTesEZo0XF_DcgVckGNgpBDzx6OiSBIfpUlciOo0RkR4IjJW_nRQSALrQE_Lfyz921d1odqESScXciOw-YEyYioE9Y1HWOBKnpBO_Vc_ri6wpQSLqUM7CFCSvMR4N1WZni-N8gER0QzLDONhFkmaR4K-XmltCKKghpQS-kpx25DJi44GhwR9HDY6LBG2poa-I4vC5joc1NSgR1GKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فاکس‌ نیوز :
ترامپ برای رسیدن به توافق نهایی ۷ روز‌ دیگر به ایران زمان داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 635 · <a href="https://t.me/SorkhTimes/132168" target="_blank">📅 11:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132167">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
سردار آزمون به زودی با انتشار یک پیام عذرخواهی به تیم ملی بازخواهد گشت.  #خبرنگار_فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 729 · <a href="https://t.me/SorkhTimes/132167" target="_blank">📅 11:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132166">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
رشیدی کوچی نماینده سابق مجلس:   معتقدم این هفته اینترنت به حالت قبلی باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 727 · <a href="https://t.me/SorkhTimes/132166" target="_blank">📅 11:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132164">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
به نقل از منابع فوتبال 360 مدیران باشگاه پرسپولیس
از همین حالا تماس های خودشو با مهدی لیموچی و آریا یوسفی برای جذبشون در تابستان آغاز کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 791 · <a href="https://t.me/SorkhTimes/132164" target="_blank">📅 10:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132163">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGlHM0mMr01WQnwXoxO6li3ZnL-Nb4h_HJgzXAZwevRbCZirv0cYxszUSVUAuuOD7HfWM0npHyL7gUysJSjRVLQsOQbVRSIWmnV1s-pOAQMguuR4yhcSo2IR_5w9s-kexXUjeAmjPabOv_Bb46DF790fIIAU7yI40brEw9OTW9sLew29OvDyzmhvVZztuyFxHPDhSVu6iVJq80wg1sIO4EsrxTZFwKmeJZEbRpYt8T83MC9pYzYLIZ2k4tJrifC72g9uMujnuVe0p5WVk7SeHThFzQZVfVUSW7hXOgGi1gizGPQjnGeaihi48TGTA_cT1Dk_JjOSHVyDAufuGpucfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مدیران باشگاه‌ تراکتور تا‌به اکنون مجوز جدایی مهدی ترابی ستاره خود را صادر نکرده‌اند و بعید بنظر میرسد این بازیکن در پنجره نقل و انتقالاتی بازهم به پرسپولیس بازگردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 778 · <a href="https://t.me/SorkhTimes/132163" target="_blank">📅 10:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132162">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
فوووووری/ خبرنگار فارس حاضر در اردوی تیم ملی: امیرحسین محمودی در لیست نهایی تیم ملی برای جام جهانی قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 766 · <a href="https://t.me/SorkhTimes/132162" target="_blank">📅 10:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132160">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=rzl3eXqLOHCpptiZlMXW9hYbUAxpMsgLV9xnD8NkCxCfYAB0hg_17DpwxULHqENKhG7leCFxiZRiNLknQQbZgqXJ0dqnlooCwlsT6sEXb_dWTQIFz-3F250SjH2jJH6kEbCuZqWDA9crZ7yysuOem2-g7ZR569q7pR1f4l_kOgj0Za2G6hvYLC2jhHCCy1dV8BGdf3Bd-LNzb3xQUXhYwl33pr2Qtzu2G3xFtRJXpH38RcM-nliJ4kd514qS7l0tVj7QUFKUUx7aufo-9AEUp2YdA3roJuTJWoaonJwFER3VnWSImfJF89DpejeeuHxF8l1StpNY1_sdnbSJifFqHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=rzl3eXqLOHCpptiZlMXW9hYbUAxpMsgLV9xnD8NkCxCfYAB0hg_17DpwxULHqENKhG7leCFxiZRiNLknQQbZgqXJ0dqnlooCwlsT6sEXb_dWTQIFz-3F250SjH2jJH6kEbCuZqWDA9crZ7yysuOem2-g7ZR569q7pR1f4l_kOgj0Za2G6hvYLC2jhHCCy1dV8BGdf3Bd-LNzb3xQUXhYwl33pr2Qtzu2G3xFtRJXpH38RcM-nliJ4kd514qS7l0tVj7QUFKUUx7aufo-9AEUp2YdA3roJuTJWoaonJwFER3VnWSImfJF89DpejeeuHxF8l1StpNY1_sdnbSJifFqHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- همه اون لحظه‌ای که سایت نصفه لود میشه و VPN قاطی میکنه رو تجربه کردیم، مخصوصاً وقتی وسط بازی یا ثبت پیش‌بینی باشی.
😑
- ربات رسمی تلگرام وینکوبت کارو راحت و ورود به سایت رو آسون کرده:
👇
-
🤖
@Wincobet_bot
-
🤖
@Wincobet_bot
- برای کسایی که بیشتر وقتشون توی تلگرامه، خیلی کاربردیه.</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/132160" target="_blank">📅 01:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132158">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5lmHnM7mQFUHLkmj5A3OUNtF8ix42SLTI6JetOyfdsCxky6VxzjlAaj45fNXmiWq67FBozHYdJDoMHkFY8jxelClwO9jMJHO6lLdpgbwsIUDAaZtoJrfkGOYmtijINwIggCeDgrGTCq9LSiIJlHnSGcAA-0XthBr1iGTilOexdqOknYhSkfq22UDx7jdWrmyoVUsRYZRJ-jAk8mtUzytBoWK8wqPjcQwTNEN5JDYyspMrjfEYROJxxnF9wN34p_Fmb-vHQ76HM_Qek-PaS5Ximg2i549hTidy3q14EqJXlmAWegdze60Hv4MwZkF65lDfOHsFf_RLp45OZs25JNpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇺🇸
کانال 12 عبری: نتانیاهو در تلاشه تا توافق رو بهم بزنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/132158" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132157">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❗️
رسانه‌های داخلی: آمریکا مانع آزادسازی پول‌های مسدود شدست، احتمال لغو کلی توافق وجود داره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/132157" target="_blank">📅 00:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132156">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
علیرضا جهانبخش و مهدی طارمی در اردوی تیم‌ملی از امیر قلعه‌نویی درخواست کرده اند سردار آزمون را ببخشد و او را به تیم ملی دعوت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/SorkhTimes/132156" target="_blank">📅 23:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132155">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
نماینده محمد امین حزباوی امروز پیشنهاد مالی‌ مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/132155" target="_blank">📅 23:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132154">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📣
#شنیده‌ها
🗣
🇮🇷
محمدامین حزباوی از باشگاه پرسپولیس پیشنهاد رسمی دریافت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132154" target="_blank">📅 23:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132153">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oylRpp4sAhjdcj_n0nbyrZiDN88-7eXGgTtQZLa8L2MF-PrklV13bHG_WDZ2OJAKGyksF-WEUBwnMD7LRJJAoM_74Ft_cx-0hEv1oirhTRYQDC9wX3xj5u4ND2t6YomNLcaRCjvYarm6VbwSq0lcOD42LI2EEOwywKexoENBn0iAJ3taNp-EbxwbHto7TlplPw21w1pFJbsuVm1bW28oyEI0-7yk63pS1QZxz_NCOQBhtKSpLMcINmX-If1N5c_RnqSnIXBpAeMol4mGDegnBg6zTAs114ouGBXelBl8EvFeKczKIyM5aC7ObcdsuS3k9wcb1ysOFyFb_FJPg6wi6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مدیران باشگاه پرسپولیس قصد دارند درصورت افزایش بودجه؛ قرارداد ابرقویی نژاد را از لحاظ مالی افزایش دهند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/132153" target="_blank">📅 23:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132151">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
جوزالم پست: ایران در اصل با یک توافق آتش‌بس با ایالات متحده موافقت کرده است که بر اساس آن، اورانیوم بسیار غنی‌شده خود را از بین خواهد برد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132151" target="_blank">📅 22:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132150">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r92Hm4IvdI-kyPV1rWDfbLuP6Sqd9411rBNMuT5pNwyKywFhv6RIfb5Xdxsiv32H-coAlBHqKAQK0vSxxMXON8JU_zDRWLayGajHV0WU6XPC6WNKtdUPqNpsoXaz4hY-1Fscu7XomvdHlqLBIYlTD1a1mN6yb5YvW5sapcUpsIEePxVlQZ4kyY2twBsZO2IXj48nILKCPUu9kVMYA1GyKjYi4hwpf3RO1D-ZNVz3Te2vpYyqqPlM1VGI24TvKZLytQeEe6Ih07rY_HmLMJPkN27P1TUKCU8r4fwfhVnpIaGBD1I3pJlROvapQ-etOswgbqQRDgCDTH6o7y46Elm9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیرضا جهانبخش و مهدی طارمی در اردوی تیم‌ملی از امیر قلعه‌نویی درخواست کرده اند سردار آزمون را ببخشد و او را به تیم ملی دعوت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132150" target="_blank">📅 22:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132149">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uX6FzSRS_3GXV8sK-5Ux8KYv_q_xI-XBrspnG4QutW34Ab91oF2mHmmuBhRfZwXZ-xvTvG78avjKZTwyIRBOn1oXnOaJSibl3ejT1muz3S6b3x9-fVj7IbVUMmv8dbuDu-oKJKxDL1UPq_tT7NMD4IDw96XlOu6HwVzhlJL6FoXYot7DMt5N5Nb_c6NLw_eeje9EQHgZBrKyN3jLHOT891Yk-e5fVsukQ-o0ULzTSsHglkFXMKJX_NjOcfBDnt6bugw05GzBiprWLZnuTNj_r6XIwmiU2ZI19LckVA9WuaJ7xLdHk4TUHXql4-70Fzkgfd1beAdFpPr3ugfgNeedMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت فعال شد!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/132149" target="_blank">📅 22:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132148">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
فووووووووووووری
🚨
علی علیپور در آستانه عقد قرارداد با باشگاه تراکتور سازی تبریز قرار دارد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/132148" target="_blank">📅 22:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132147">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فرهیختگان: علیپور از پرسپولیس خواسته رقم قراردادش از همه ایرانیای لیگ بالاتر باشه و اگه موافقت کنن بعد جام جهانی تمدید میکنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/132147" target="_blank">📅 22:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132145">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8eQnWgoT7BMQu5p42GPczoDFYfrUjGMzQT2sWV1LDgftGNrPqNPsT8MO0hvLCEesNIVAGwVx38Oebw2uJHL3h6XKfNPYbBAt-67kpEyDuur4AzL4STEbyFmFtVUp9_YZGqe3oHy6qSoxYixF0lXVjyYoUFAkvrkm56-PGMTYYLj2rxzyynk6RM237ouEP0hkkX8WIqSRzNfdL2GeLsQC6ZrxdYS64zcpvyg-fP7zobnkPCr_V18RU0gRF2DYz68phuifn6U2ou5WaN3B-in7dgxppULUxVMRRyXVtMXCm8-K4EULnkQqNKFyH7VVO9NfMsoItVEyNhuGBsTeZk1mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖍
سایت فوتی رنکینگ ، چادرملو رو به عنوان نماینده ایران در لیگ دو آسیا معرفی کرد
😐
😟
😟
😟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132145" target="_blank">📅 21:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132144">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffe4f5232d.mp4?token=rQICuyLBFknvPajXObe9cAnMXSqLTUo5zF6wbTJxvPpgEMNK2sWUdhFytfPAO08t9Kln98yWD6p16yq4yx6VeJv0ktu6rDbUPhGlxYU5EDU_-uYmOfQXrL63I9XLGNVT2hwURY_DnS01xaZgl7eNbky2X27-cC46OYC7FHuWGCR1irxDSeIns-RLATaJq4VyQdaTcfgyyoUuJRxKjZw98I1g7TMP-hzUAqFAwQzCzMAv9-TP1WlNkm1tMfPwflnsIrc1Pr0-bOFHprYkdD2UD2fPRYBhR5rLOqzD_vfUNUYlcBvvNzxraGl7-UzPr7ZAy3eIg_xwZuOAGxHDmUdLkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffe4f5232d.mp4?token=rQICuyLBFknvPajXObe9cAnMXSqLTUo5zF6wbTJxvPpgEMNK2sWUdhFytfPAO08t9Kln98yWD6p16yq4yx6VeJv0ktu6rDbUPhGlxYU5EDU_-uYmOfQXrL63I9XLGNVT2hwURY_DnS01xaZgl7eNbky2X27-cC46OYC7FHuWGCR1irxDSeIns-RLATaJq4VyQdaTcfgyyoUuJRxKjZw98I1g7TMP-hzUAqFAwQzCzMAv9-TP1WlNkm1tMfPwflnsIrc1Pr0-bOFHprYkdD2UD2fPRYBhR5rLOqzD_vfUNUYlcBvvNzxraGl7-UzPr7ZAy3eIg_xwZuOAGxHDmUdLkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی علیپور امروز تو بازی دوستانه درون تیم ملی به این شکل پنالتی خراب کرد تا شایعه خط خوردنش از لیست تیم ملی تقویت بشه!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/132144" target="_blank">📅 21:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132143">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
فارس: باشگاه پرسپولیس قصد تمدید قرارداد میلاد محمدی را ندارد و به احتمال زیاد از جمع سرخپوشان جدا شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/132143" target="_blank">📅 20:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132142">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a133b9505.mp4?token=uWgNpMwJnt5U10Llph-mGg5Kaq2giQAndsQkpk6PZYeeAKaxuxHpdcyZQw2NalbR5UFVwV6tRAy0KD6wHbMDvzUuZCcnX60rqKh7tzWn9_21cPRZ_c1A6azBRPVzTURW49TdnrZpi5gvrntiBT-1NoxaL7joOdz1sJLCWOEtWVZDUOEKsWT1uDwkKyoY53LJbsnTX6HUPNmm1JfgyWTMzXCQbd9Dg4Q0RCwbXcOHE94Z9M6100OUtOqTwVX1Kh68ZzaPjw9py8BIppgVe_PVN4Vt0kKyCrYh3RMCHmI5afxeRUoabvzzNT69khrpeHSdPj_rRwYyumM2jmT5b8ORZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a133b9505.mp4?token=uWgNpMwJnt5U10Llph-mGg5Kaq2giQAndsQkpk6PZYeeAKaxuxHpdcyZQw2NalbR5UFVwV6tRAy0KD6wHbMDvzUuZCcnX60rqKh7tzWn9_21cPRZ_c1A6azBRPVzTURW49TdnrZpi5gvrntiBT-1NoxaL7joOdz1sJLCWOEtWVZDUOEKsWT1uDwkKyoY53LJbsnTX6HUPNmm1JfgyWTMzXCQbd9Dg4Q0RCwbXcOHE94Z9M6100OUtOqTwVX1Kh68ZzaPjw9py8BIppgVe_PVN4Vt0kKyCrYh3RMCHmI5afxeRUoabvzzNT69khrpeHSdPj_rRwYyumM2jmT5b8ORZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پاس گل امیرحسین محمودی تو بازی دوستانه درون تیمی امروز تیم ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/132142" target="_blank">📅 20:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132141">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQ-PCBgsuiqFaT9SHVn_pZz_g6qnCpTBljhO7sqJGVUbHOcvQOt3b3BYAE2qktQzEhuhMn3zHd4fqlYpQv2Br_pSkNvg3jfB7h4-SjPGWCQzEQu4otz9nMAM6C6yxwkUwWrjyiQ63DyqSMXkJRVFFwCAKW00I_F4onylI_TGFDBdCGPg81FtnAYokH7PeOc0il0wSfAGaLwk0o-GcP4Ubs1ljYecaGukEPZgYLacyZYpJ6saypt24MYtR81zTWXjtHKGkFQb1MQe1ZiksSkvbHhc9eagu9VvzAYtRWs1djyvQjpuxD2TME3x4atbv9qOlHzNzhC8WOEeJGpperkP2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جوزالم پست: ایران در اصل با یک توافق آتش‌بس با ایالات متحده موافقت کرده است که بر اساس آن، اورانیوم بسیار غنی‌شده خود را از بین خواهد برد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/132141" target="_blank">📅 20:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132140">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚫
افکت اتفاقی :
❌
توافق ایران و آمریکا میگن ۶۰ روزه است، بازی‌های جام جهانی ۵۶ روز دیگه تمام می‌شوند
‼️
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SorkhTimes/132140" target="_blank">📅 20:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132139">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7Q9SmsfD6US595PKLsJIrlAC7EjAD8W6pXHVjWafsQqWSSvhm8Z4drZc4bC9K4qvY0rOwZ-m5Vr94n7mKZxfdR-XXtVmSZ3r9VUDkSRm3kahFb6a55PFpvQw5U4kqI-Go6zoljoNIyArkONXwWpZRrrHgqfi2rmtl-tOXuiNFSkzIMCgJm34dImv1pDeyoeSss5ru56keBbexvTAC9xzwUGu6SU4oCGdNm153wy3Ilp4LOq9UG1dqigdMeynX40OrGkHvfzbLS612-6WBoiMsVgNdb02z730rD1Yb4ksWZBwXJEYv7qTt-3NuFfGWbB73PYGkulnRumH4xq2kjU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ‌ حرف های امروز‌ پزشکیان که گفته بود آماده ایم‌ به جهان اطمینان بدیم که به دنبال سلاح هسته ای نیستیم رو ریپوست کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/132139" target="_blank">📅 20:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132138">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">😏
😏
😏
بابایی مدیرعامل چادرملو: اگه سپاهان مجوز حرفه‌ای نگیره ما از پرسپولیس جلوتریم و ارجحیت داریم و باید آسیایی بشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132138" target="_blank">📅 19:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132137">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚫
افکت اتفاقی :
❌
توافق ایران و آمریکا میگن ۶۰ روزه است، بازی‌های جام جهانی ۵۶ روز دیگه تمام می‌شوند
‼️
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/132137" target="_blank">📅 19:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132134">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
تمام اعضای هیات رییسه فدراسیون فوتبال درخواست ویزای امریکا کردند!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/132134" target="_blank">📅 18:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132132">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
شبکه ۱۲ عبری به نقل از منابع:
🔻
اسرائیل کاملاً از پیشرفت مذاکرات آمریکا و ایران غافلگیر شده درحالیکه همه نهادهای امنیتی بازگشت جنگ را پیش‌بینی می‌کردند
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/132132" target="_blank">📅 17:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132131">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
شبکه ۱۲ عبری به نقل از منابع:
🔻
اسرائیل کاملاً از پیشرفت مذاکرات آمریکا و ایران غافلگیر شده درحالیکه همه نهادهای امنیتی بازگشت جنگ را پیش‌بینی می‌کردند
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/132131" target="_blank">📅 17:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132130">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
پاکستان تفاهم ایران و آمریکا را بدون نیاز به حضور طرفین اعلام رسمی می‌کند
🔴
به گفته این منابع، توافق اولیه و احتمالی میان واشینگتن و تهران تحت عنوان رسمی «اعلامیه اسلام‌آباد» نام‌گذاری خواهد شد.
🔴
این منابع تصریح کردند که توافق اولیه در واقع یک «یادداشت…</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/132130" target="_blank">📅 17:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132129">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❗️
جنگ هم رسما تمام شد ..امیدوارم دیگه بهونه ای نباشه و نداشته باشن که نخوان اینترنت بین الملل وصل کنن ..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/132129" target="_blank">📅 16:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132128">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
حمید رسایی: به هیچ عنوان اجازه نمیدیم اینترنت بین الملل وصل بشه
😐
😐
😐
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/132128" target="_blank">📅 16:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132126">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
رشیدی کوچی نماینده سابق مجلس:   معتقدم این هفته اینترنت به حالت قبلی باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/132126" target="_blank">📅 16:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132125">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
رشیدی کوچی نماینده سابق مجلس:
معتقدم این هفته اینترنت به حالت قبلی باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SorkhTimes/132125" target="_blank">📅 15:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132124">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
فوری از سیتنا، پایگاه اخبار اینترنت:
احتمالا تا هفته آینده
اینترنت بین الملل
متصل میشه
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SorkhTimes/132124" target="_blank">📅 15:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132122">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏅
🏅
با اعلام رسمی afc استقلال و تراکتور به عنوان نمایندگان ایران در لیگ نخبگان مشخص شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SorkhTimes/132122" target="_blank">📅 14:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132121">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🏅
🏅
با اعلام رسمی afc استقلال و تراکتور به عنوان نمایندگان ایران در لیگ نخبگان مشخص شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/132121" target="_blank">📅 14:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132120">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wt8GciGTr7CiCo0d23NN_vwT5IEI9fFEhLX6kACpNsuWwkhfguhdNwDNmchcGw0UayteLECx0gtjd9zAPNEG0tGt3FWLOq8pKIDBgsyhhc9FyOkX3P9KPVTb2Mc_5USSyG0Oo7s08zUsW5Omp_05GaZKQn51Abt_MilCUU_Fzm2EJJry6QgA-Y8Wc7ajIJEbI6lV6kzDR1dWjA6KjeA-XR-9jq36N_peAP9s0WS5PcdiGa_VmYONtFAQw5kWfo66Y9r-LZ8MUEezKJ9FKW06gVTM2h4XYQ5FlPTYkH54ja5AxPsJZRfesZPtCBgfS1sUKqIAwAQGdFJRNXI_v_M2-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
🏅
با اعلام رسمی afc استقلال و تراکتور به عنوان نمایندگان ایران در لیگ نخبگان مشخص شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SorkhTimes/132120" target="_blank">📅 14:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132119">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c85e6431c.mp4?token=otcn1uxHkGv3LEyNh3cbNdWuP4HZYXSVxnKMU3j0nLwgQvHATJl1QvAOJU4Ivl2n_-5yo00V-mp0yuxeWS-ASwER7Ev8QzRP3-IIqr7Z7lhGZxR2zIiPsRGs2VDkvoN3pSWM_BTzgsltYc7imMIETvNyeIDcHg6daeAHuRwIk-Lgz23uoPGP7IASJuqxPpWqpS7Hw3TEr_Ttzlm2KoFunaKmDx8_mc6LWS7tsYi4NBg-s04_mX-IqlWY5QhfFbnDAPSklf5OIGZ7b-wZvuWdSthVuIzM22ePI7UfCUnzkOA_jiR5ErAZlxGFc1JjX7mWuGO7OgmTyPLOvvuzp4HwfxsG5_KYhGxBzTBb1LMIDVu6Id821T5z30RfgpvWEBR9PzljacHBwwy07Zwtgrt47Dwgvs_EvoWr4icI23TmF9OBiXOI_ehlC39wq03SgjyZH6OFB-fIx_27vvnPVErB5_gUinhPbLjOb41n4P6YfgM0dKAmfQJaZ3liVTi3OiXnxbr2yQPgA2aJcUHLBLwCZMS6Xop3_uhalfop8lMZMdzyFBX7bjqfWZBOSKpdIkrBMERx83baesdRuVubTq8ohqkNeOm-G5dXjHXCakJqQddh7zUaoN4MgNqiaxv98R0bKisRgw4cmWjmNVbxxm-cUKAhXULDeOTtY3ikxwVVdJo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c85e6431c.mp4?token=otcn1uxHkGv3LEyNh3cbNdWuP4HZYXSVxnKMU3j0nLwgQvHATJl1QvAOJU4Ivl2n_-5yo00V-mp0yuxeWS-ASwER7Ev8QzRP3-IIqr7Z7lhGZxR2zIiPsRGs2VDkvoN3pSWM_BTzgsltYc7imMIETvNyeIDcHg6daeAHuRwIk-Lgz23uoPGP7IASJuqxPpWqpS7Hw3TEr_Ttzlm2KoFunaKmDx8_mc6LWS7tsYi4NBg-s04_mX-IqlWY5QhfFbnDAPSklf5OIGZ7b-wZvuWdSthVuIzM22ePI7UfCUnzkOA_jiR5ErAZlxGFc1JjX7mWuGO7OgmTyPLOvvuzp4HwfxsG5_KYhGxBzTBb1LMIDVu6Id821T5z30RfgpvWEBR9PzljacHBwwy07Zwtgrt47Dwgvs_EvoWr4icI23TmF9OBiXOI_ehlC39wq03SgjyZH6OFB-fIx_27vvnPVErB5_gUinhPbLjOb41n4P6YfgM0dKAmfQJaZ3liVTi3OiXnxbr2yQPgA2aJcUHLBLwCZMS6Xop3_uhalfop8lMZMdzyFBX7bjqfWZBOSKpdIkrBMERx83baesdRuVubTq8ohqkNeOm-G5dXjHXCakJqQddh7zUaoN4MgNqiaxv98R0bKisRgw4cmWjmNVbxxm-cUKAhXULDeOTtY3ikxwVVdJo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
موزیک ویدیو رسمی جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/SorkhTimes/132119" target="_blank">📅 14:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132117">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فرهیختگان: مشکل اورونوف همون همیشگیه و چاره ای جز مراعات کردن نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/132117" target="_blank">📅 14:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132116">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
خرید اروپایی پرسپولیس خبرساز شد
⏺
شبکه ورزشی «M4 Sport» که مهم‌ترین رسانه ورزشی مجارستان محسوب می‌شود، در گفت‌وگویی با گرا اعلام کرد این بازیکن تصمیم حضور در پرسپولیس را بر اساس «حس درونی» خود گرفته و معتقد است حضور در فوتبال ایران می‌تواند چالش مهمی در دوران حرفه‌ای‌اش باشد.
⏺
گرا در بخشی از مصاحبه خود گفته دوست دارد هرچه زودتر در ورزشگاه آزادی و مقابل هواداران پرسپولیس به میدان برود و این موضوع را یکی از جذاب‌ترین تجربه‌های فوتبالی خود می‌داند.
⏺
در گزارش‌های منتشرشده همچنین آمده که این مدافع مجارستانی امیدوار است با درخشش در پرسپولیس دوباره جایگاهش را در تیم ملی کشورش تثبیت کند.
⏺
رسانه‌های مجارستانی از گرا به عنوان بازیکنی یاد کرده‌اند که حضور در فوتبال ایران را سکوی جدیدی برای ادامه مسیر حرفه‌ای خود می‌بیند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SorkhTimes/132116" target="_blank">📅 14:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132114">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTFE2pyyFv0o_hIyPG5JkikTTYdk0y5ih9OM276DSwsjZE8G04IeU4qArLy7rw_DxAAHtYfC_RG1A7DPzsXHQpUsOR4g8IVGR3fIIDL4XTFNw76I6ObRUKYzhzrW9uuPVwShnr60u2IHWzFj8gKGV__MhLNQUFpzunepDD3vKb1o2FcwdPDFxXsqBpceZeKqoFUKIrVcBgqB0Yx3-Kr6je1diuGDiYlLn2txyU-1_DUfNtuygUN_LMlGkXJY9hQRkoFkFYMNMvIB28W4Iz6HbU_M1QBJ5ikTHyzqLtdpS_H3rV7-BMT9eHQ1k4q38ToAopfXrbijRm3fDSlZMyLgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🚨
بزرگترین ریسک حقوقی باشگاه پرسپولیس ختم به خیر شد
🔺
شرکت سیما کیش حدود ۱۲۰۰ میلیارد‌ ادعا علیه باشگاه داشت که رفع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/132114" target="_blank">📅 13:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132112">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
ورزش‌سه: محمودی بشدت آمادست و احتمالا راهی جام جهانی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132112" target="_blank">📅 11:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132111">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
تا قبل 21 خرداد حکم علی بیرو بیاد از جام جهانی محروم میشه / خبر ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/SorkhTimes/132111" target="_blank">📅 11:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132110">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
⛔️
احتمال محرومیت بیرانوند از حضور در جام‌جهانی؛
💯
حضور روی سکوها به‌جای زمین چمن!
⚠️
با شکایت باشگاه پرسپولیس درخصوص پرونده علیرضا بیرانوند به CAS و پیگیری شدید سرخپوشان تهرانی، درصورت صدور رای محرومیت بیرانوند طی روزهای آینده، دروازه‌بان تراکتور جام‌جهانی…</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/132110" target="_blank">📅 11:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132108">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3azlEqaRbD7pMkEVxrve3neS3ykZqnAncw45VKenKIzlzYDnljHvs-XGUcUtRqbHIXQaXj9OhvADks2Y2udI0hx3T_UqkenqtEV0KBSgHILRgvZ_1ZUHJj6V-KdR63rkfLjSpYh8Ris0h4Q9H1ARRyoYqE6f5rbBsWo4QdAYyMbJdhy3qNOsdcrwmklBuq_bfAiDx7MHAyNfa8edi7Scm1Vu-Vw4FHnqWlYND0Dyngw9TeIhh7zt-N8l7MGuqi97cDiZBfiFlvzJ-HAGWTlWgGEqnB51dnEgwP1cRbQQ_vqbapVlhcbjwngmKefwesr13J3VLs-YD4OEPdIwFz0Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این روزا قبل از پیش‌بینی بیشتر از خود بازی باید نگران این باشی که VPN وصل میشه یا نه.
😀
ربات تلگرام وینکوبت دقیقاً برای همین شرایط خوبه چون کل سایت داخل خود تلگرام اجرا میشه و دیگه لازم نیست هی بین سایت و VPN درگیرشی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
میتونی مستقیم وارد بازی‌ها و کازینو شی، پیش‌بینی ثبت کنی، واریز و برداشت انجام بدی و همه‌چی خیلی سریع‌تر و راحت‌تر انجام میشه.
🟣
آدرس دائمی سایت:
wincobet.com</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SorkhTimes/132108" target="_blank">📅 10:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132107">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
باشگاه پرسپولیس برخی نفرات سپاهان  را مدنظر دارد چرا که این باشگاه به بازیکنان گفته نمی توانیم مبالغ قراردادها را پرداخت کنیم ک نهایت پرداختی ما ده تا ۲۵ میلیارد خواهد بود و سقف پرداختی هم برای چند نفر است.
🔴
از  مهدی لیموچی،امین حزباوی و  آریا یوسفی به…</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/132107" target="_blank">📅 10:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132106">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
باشگاه پرسپولیس برخی نفرات سپاهان  را مدنظر دارد چرا که این باشگاه به بازیکنان گفته نمی توانیم مبالغ قراردادها را پرداخت کنیم ک نهایت پرداختی ما ده تا ۲۵ میلیارد خواهد بود و سقف پرداختی هم برای چند نفر است.
🔴
از  مهدی لیموچی،امین حزباوی و  آریا یوسفی به…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/132106" target="_blank">📅 10:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132105">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">📣
#شنیده‌ها
🗣
🇮🇷
محمدامین حزباوی از باشگاه پرسپولیس پیشنهاد رسمی دریافت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SorkhTimes/132105" target="_blank">📅 10:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132104">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
باشگاه پرسپولیس برخی نفرات سپاهان  را مدنظر دارد چرا که این باشگاه به بازیکنان گفته نمی توانیم مبالغ قراردادها را پرداخت کنیم ک نهایت پرداختی ما ده تا ۲۵ میلیارد خواهد بود و سقف پرداختی هم برای چند نفر است.
🔴
از  مهدی لیموچی،امین حزباوی و  آریا یوسفی به…</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/SorkhTimes/132104" target="_blank">📅 10:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132103">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
الحدث:
🔴
ایران و آمریکا به دشمنی طولانی مدتشون پایان دادن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/SorkhTimes/132103" target="_blank">📅 01:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132102">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❗️
الحدث:
🔴
ایران و آمریکا به دشمنی طولانی مدتشون پایان دادن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/SorkhTimes/132102" target="_blank">📅 01:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132101">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
❌
آکسیوس:
🔽
توافق‌نامه همین الان توسط دو طرف امضا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SorkhTimes/132101" target="_blank">📅 01:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132100">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
علی هاشم خبرنگار الجزیره: طبق گفته منابع من، پیش‌نویس پیشنهادی که قرار است نهایی شود شامل موارد زیر است:
❌
پایان جنگ در همه جبهه‌ها از جمله لبنان
❗️
آزاد شدن میلیاردها دلار از دارایی‌های مسدود شده ایران
❌
لغو محاصره دریایی آمریکا و گشایش تنگه هرمز
🔽
خروج…</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/SorkhTimes/132100" target="_blank">📅 01:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132098">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
تاج رئیس فدراسیون فوتبال: طی جلساتی که با مدیران فیفا داشتیم به جای آمریکا به کمپی در مکزیک خواهیم رفت تا اردوی خودمان را برگزار کنیم/ با این کار مشکلات ویزا حل می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SorkhTimes/132098" target="_blank">📅 01:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132096">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇺🇸
ترامپ :   من در دفتر بیضی شکل کاخ سفید هستم جایی که به تازگی تماس بسیار خوبی با رئیس‌جمهور محمد بن سلمان آل سعود از عربستان سعودی، محمد بن زاید آل نهیان از امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر…</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/SorkhTimes/132096" target="_blank">📅 00:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132095">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
فرهیختگان: پرسپولیس بجای سپاهان به عنوان نماینده سوم اسیایی خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/132095" target="_blank">📅 00:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132093">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
ترامپ :   من در دفتر بیضی شکل کاخ سفید هستم جایی که به تازگی تماس بسیار خوبی با رئیس‌جمهور محمد بن سلمان آل سعود از عربستان سعودی، محمد بن زاید آل نهیان از امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر…</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/132093" target="_blank">📅 00:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132092">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfOkyeKFCBIvflFyDp1N0F18lstbv6xqkA5n9cOev_nxHRACeEyUbuolEFQsUviY4m4uhHvwzxbGQZUXQ1vYFJWK0KGfj5C2T_t1hWQY65SPjQYzHPy3PMpg7YavWOeui3EPmUYTqfDZQahNKAPRRLv3EMjPMg6LRcmxSKPdhkW1oQrWRj-PvVJFFjDRuYJLfrcJCmkNN94QdOjEaQC-B5IoqHQBEzXiVycnx0Uqyez33OoZD_1eBOJZnm-NIJKJM4iuQvQWg48bgULyJcv1o1ieTEqEg0FlkkuMPw7d9-TRt_3zjlZ9EMXK3gNIEKRQEAEvrvSbqe5Q_TU4r9XoKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ :
من در دفتر بیضی شکل کاخ سفید هستم جایی که به تازگی تماس بسیار خوبی با رئیس‌جمهور محمد بن سلمان آل سعود از عربستان سعودی، محمد بن زاید آل نهیان از امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر، فیلد مارشال سید عاصم منیر احمد شاه از پاکستان، رئیس‌جمهور رجب طیب اردوغان از ترکیه، رئیس‌جمهور عبدالفتاح السیسی از مصر، پادشاه عبدالله دوم از اردن و پادشاه حمد بن عیسی آل خلیفه از بحرین داشتیم، درباره جمهوری اسلامی ایران و همه موارد مربوط به تفاهم‌نامه‌ای درباره صلح.
یک توافق تا حد زیادی مذاکره شده است که منوط به نهایی شدن بین ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگر ذکر شده است. به طور جداگانه، من تماسی با نخست‌وزیر بیبی نتانیاهو از اسرائیل داشتم که به همان صورت بسیار خوب پیش رفت. جنبه‌ها و جزئیات نهایی توافق در حال حاضر در حال بحث است و به زودی اعلام خواهد شد.
علاوه بر بسیاری از عناصر دیگر توافق، تنگه هرمز باز خواهد شد.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/132092" target="_blank">📅 00:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132091">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
#فوری | الحدث:
🔻
پیش‌بینی‌هایی مبنی بر اعلام نهایی شدن توافق صلح بین واشنگتن و تهران ظرف ۲۴ ساعت آتی، وجود دارد.
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SorkhTimes/132091" target="_blank">📅 23:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132089">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
باشگاه پرسپولیس برخی نفرات سپاهان  را مدنظر دارد چرا که این باشگاه به بازیکنان گفته نمی توانیم مبالغ قراردادها را پرداخت کنیم ک نهایت پرداختی ما ده تا ۲۵ میلیارد خواهد بود و سقف پرداختی هم برای چند نفر است.
🔴
از  مهدی لیموچی،امین حزباوی و  آریا یوسفی به…</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/132089" target="_blank">📅 23:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132088">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
خبر رسیده دو بازیکن تیم سپاهان 10 روز پیش با ارسال نوتیس به باشگاه سپاهان در آستانه فسخ قرارداد خود با این باشگاه قرار دارن و مدنطر پرسپولیس هستن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/132088" target="_blank">📅 23:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132087">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❗️
👈
ادعای کانال ۱۴ اسرائیل: چند منبع معتبر تأیید می‌کنند که ایران با برخی از درخواست‌های کلیدی ایالات متحده موافقت کرده است و کمتر از ۲۴ ساعت دیگر اعلام توافق انجام خواهد شد که به تهران چند ماه فرصت می‌دهد تا کاملاً تسلیم شود
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/132087" target="_blank">📅 23:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132086">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❗️
#فوری | ادعای الحدث به نقل از یک منبع عالی‌رتبه:
🔴
تنها ساعات کمی تا اعلام توافق بین آمریکا و ایران فاصله است
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SorkhTimes/132086" target="_blank">📅 22:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132085">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
کمپ تیم‌ملی رفت مکزیک و فقط برا بازیا میان امریکا...کل فاصله ما با مکان بازی‌های ما در لس آنجلس 55 دقیقه با پرواز است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SorkhTimes/132085" target="_blank">📅 22:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132084">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
تاج رئیس فدراسیون فوتبال: طی جلساتی که با مدیران فیفا داشتیم به جای آمریکا به کمپی در مکزیک خواهیم رفت تا اردوی خودمان را برگزار کنیم/ با این کار مشکلات ویزا حل می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/132084" target="_blank">📅 22:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132083">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
🚨
🚨
عصر ایران نوشت: سفارت آمریکا به طارمی،شجاع خلیل زاده و احسان حاج صفی ویزا نداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/132083" target="_blank">📅 21:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132082">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
روزنامه اعتماد : به احتمال بسیار زیاد در این هفته رفع انسداد اينترنت مصوب شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/132082" target="_blank">📅 21:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132081">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❗️
👈
ترامپ، در گفت‌وگو با سی‌بی‌اس نیوز:  مذاکره‌کنندگان ایالات متحده و ایران «بسیار به نهایی کردن یک توافق» برای پایان دادن به جنگ بین دو کشور نزدیک‌تر شده‌اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132081" target="_blank">📅 21:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132079">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
بر اساس گزارشات منتشر شده از فایننشال تایمز با اصرار و همچنین تلاش بدون وقفه اسلام آباد آتش بس بین ایالات متحده و مقامات رژیم ایران به مدت 60 روز دیگر تمدید خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/132079" target="_blank">📅 19:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132078">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
باراك راوید خبرنگار Axios
🔴
همه چیز پنجاه پنجاه است و دونالد ترامپ هم میتواند بمب باران را شروع کند و هم میتواند به خواسته عاصم مونیر آتش بس 60 روزه را اعلام کند و او امشب قرار است در این مورد با تیم خود مشورت کند و تصمیم بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/132078" target="_blank">📅 19:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132077">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🟥
ترامپ: شانس توافق یا جنگ 50/50 است امروز با نمایندگان خود دیدار میکنم و تا فردا تصمیم میگیرم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SorkhTimes/132077" target="_blank">📅 19:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132076">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🟥
ترامپ: شانس توافق یا جنگ 50/50 است امروز با نمایندگان خود دیدار میکنم و تا فردا تصمیم میگیرم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132076" target="_blank">📅 19:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132075">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
هیئت پاکستانی بعد از دریافت جواب ایران به پیشنهاد آمریکا به پاکستان برگشتن و احتمالا تا امشب این جواب به آمریکا منتقل میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132075" target="_blank">📅 19:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132074">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❗️
فرهیختگان: دعوت شدن مغانلو جای روزبه یعنی قلعه‌نویی از عملکرد مهاجمان راضی نیست و احتمالا یکی از بین علیپور و مغانلو خط بخورن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132074" target="_blank">📅 18:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132073">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
دروازه‌بان سابق پرسپولیس درگذشت
🔺
شکرالله آغاسی، دروازه‌بان پیشین تیم فوتبال پرسپولیس، دار فانی را وداع گفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/132073" target="_blank">📅 17:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132071">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❗️
فووووووووووووری
🔴
مدیران فدراسیون فوتبال تیم فوتبال پرسپولیس را برای شرکت در مسابقات سطح دو آسیا به afc صادر خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/132071" target="_blank">📅 16:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132070">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
دقایقی پیش اسکای نیوز ادعا کرد که میانجی پاکستانی موفق شد بر مانع پرونده هسته‌ای ایران غلبه کند.
🔴
الان امریکا کوتاه اومد یا ایران؟
🤔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132070" target="_blank">📅 16:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132069">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
سردار دورسون از تراکتور و سپاهان پیشنهاد دریافت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/SorkhTimes/132069" target="_blank">📅 16:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132068">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
باشگاه پرسپولیس اعلام کرد هیچ مصالحه ای با باشگاه تراکتور درباره علیرضا بیرانوند نخواهد کرد و پرونده را ادامه می‌دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/SorkhTimes/132068" target="_blank">📅 16:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132064">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‼️
حمله تند وزیر ارتباطات به مخالفین اتصال مجدد اینترنت: این نگاه قیم معابانه به مردم چیست؟ کی گفته اینترنت را باید خلاصه در دو پیام‌رسان بدانیم؟
❌
ستار هاشمی وزیر ارتباطات:صحبت هایی که در رابطه با نقد دسترسی مردم به اینترنت آزاد می شود، نگاه قوه عاقله کشور نیست. ان‌شالله اینترنت برای آحاد مردم و به صورت عادلانه برقرار می شود.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SorkhTimes/132064" target="_blank">📅 15:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132063">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
نورالدین الدغیر خبرنگار الجزیره در تهران:
🔴
وساطت‌ها بین تهران و واشنگتن به مرحله‌ای رسیده که یکی از سران منطقه‌ای به طور مستقیم برای پر کردن شکاف‌ها وارد عمل شده.
🔴
ظهور قطر در این لحظه حساس به طور مستقیم و بر اساس اطلاعات و منابع موجود، نه صرفاً به عنوان…</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/132063" target="_blank">📅 14:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132062">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⏺
نیویورک تایمز :
🔴
فیفا قصد دارد دوباره ورود پرچم «شیر و خورشید» ایران پیش از انقلاب و لباس‌های مرتبط با آن را به ورزشگاه‌های جام جهانی ۲۰۲۶ ممنوع کند. این پرچم در جام جهانی ۲۰۲۲ قطر هم محدود شده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/132062" target="_blank">📅 14:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132061">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
عراقچی: به توافق نزدیک نیستیم. زیاده خواهی های‌ آمریکا مانع پیشرفت مذاکراته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/132061" target="_blank">📅 14:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132060">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
شبکه CBS آمریکا: آمریکا به‌زودی به ایران حمله خواهد کرد.هر لحظه ممکن است حمله‌ای رخ دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/SorkhTimes/132060" target="_blank">📅 14:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132058">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
یزدی‌خواه، نایب‌رئیس کمیسیون فرهنگی مجلس :
🔴
مسئولین دل‌سوز کشور به این نتیجه رسیدن که وصل کردن اینترنت به صلاح همه‌ی مردم نیست و فعلا قرار نیست اینترنت بین‌المللی رو برگردونیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/SorkhTimes/132058" target="_blank">📅 11:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132057">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
شایعات: ویزا شجاع خلیل زاده، مهدی طارمی و احسان حاج‌صفی بخاطر خدمت تو سپاه پاسداران صادر نشده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/132057" target="_blank">📅 11:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132055">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
رسمی؛ روزبه چشمی به علت مصدومیت جام جهانی را از دست داد و شهریار مغانلو جایگزین این بازیکن در لیست تیم ملی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/SorkhTimes/132055" target="_blank">📅 09:32 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
