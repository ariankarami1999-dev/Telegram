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
<img src="https://cdn4.telesco.pe/file/qVKtTtaQs8NtqspdAxpgljvwLJ3urYk0B6hzFfbaa7azqy_hQDtoWwBfZWXNcRsxHEedhi9gYnnBA49Q3OsE9ue4hN4L86VfpBWsU6E0C2Nf5BaARbE1b5rMYTBV-E8BEMOtXE9eeFgNy5NX9UwvtVvVY1LaWYAPKl3FSReuAeE04sx8bj7qKKDuL_7U7GlOrUWEwUSkS2e5saPn7szmnlx62Ue0jrP66akwr0Ssb-erdVeK3dAv6Y2lMCseApTGM0bguE-ORniYqGdbqL9BBtc3jlXbldOQpdsE8ZUgfRf0VzVaohKCQ1LBR7eByxV_lCqYbUFdSD3HJ-46pXHNig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.94M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 14:03:13</div>
<hr>

<div class="tg-post" id="msg-653358">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
راز رفتار متفاوت ترامپ در چین فاش شد!
🔹
ترامپ را که همه با تحقیر، داد و رفتار تهاجمی می‌شناسند… چرا مقابل چین ناگهان آرام، حساب‌ شده و حتی مودب شد؟
🔹
جواب شاید نه در سیاست، بلکه وسط تحولات ترسناک چین پنهان شده باشد.
🔹
این ویدئو نشان می‌دهد چرا حتی آمریکا هم مقابل «ابرکارخانه جهان» محتاط حرف می‌زند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 699 · <a href="https://t.me/akhbarefori/653358" target="_blank">📅 13:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653357">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqKep6-HwqBmh-2b5CXFx17LuCqDubfL7FS7fUaNutiSd1qS8EVywWYLsPNxt-tChrQjuZsv2eaITMXzcDfAWL5fW7aBA2EYxtwrRekXaxwflixYse5xfciaRHPwrkZFkfgq7buR1JNnT2iozc9UpQtQZpMxnPY6MSuFc1ec3o2H0ABq8qEHnrwowD8xWg7KgFQhcricPZbJEXGBm0uQ6RKU5Jfo4SveYP5ePr_N6S2UVrEwgoZp-PQmhXp4MLJ_2xIZNpVzzjgJf3_4VOKowlXzbVQ_b52MiBEgajJexi27WT_rVQvhoFukQuXYLbgQJgqq70UC-EC-QS_H-r89zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات ادعایی گفتگوی پر تنش ترامپ و نتانیاهو بر سر ایران
یک مقام آمریکایی به سی‌ان‌ان:
🔹
نتانیاهو روز سه‌شنبه گفتگوی پرتنشی با بنیامین نتانیاهو داشت. ناامیدی خود را ابراز کرد و به ترامپ گفت که معتقد است به تعویق انداختن حملات مورد انتظار یک اشتباه بوده و رئیس‌جمهور باید طبق برنامه ادامه دهد.
🔹
یک منبع اسرائیلی: در طول این مکالمه یک ساعته، نتانیاهو خواستار از سرگیری اقدام نظامی شد. مذاکرات جاری، نتانیاهو را ناامید کرده است. نتانیاهو استدلال کرده است که تأخیر فقط به نفع ایرانی‌ها است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/akhbarefori/653357" target="_blank">📅 13:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653356">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
اسامی ادارات پرمصرف برق اعلام عمومی می‌شود
🔹
معاون وزیر نیرو: به ادارات پرمصرف برق، اول اخطار داده می‌شود و در صورت تکرار و رعایت نکردن، فهرست اسامی مشترکان پرمصرف برق به صورت عمومی اعلام می‌شود.
🔹
در مناطق غیرگرمسیری یک ساعت قبل از تمام شدن کار باید دستگاه های سرمایشی خاموش شوند.
🔹
در صورت رعایت نشدن مصوبه، برق آنها قطع می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/akhbarefori/653356" target="_blank">📅 13:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653355">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
الجزیره به نقل از یک منبع پاکستانی:
🔹
مقامات ایرانی از پاکستان زمان خواسته‌اند تا خواسته‌های آمریکا برای مذاکره را ارزیابی و بررسی کنند
🔹
اورانیوم غنی‌شده، گره اصلی در مذاکرات آمریکا و ایران است.
🔹
فرمانده ارتش هنوز در پاکستان است و سفر او به ایران بستگی به نتایج سفر وزیر کشور دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/akhbarefori/653355" target="_blank">📅 12:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653354">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
واکنش کوثری به اقدام امارات برای دور زدن تنگه هرمز؛ آنجا را زیر آتش می‌بریم
اسماعیل کوثری، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
قبل از جنگ به امارات نامه دادیم که این مکان ‌هایی را که در اختیار آمریکا گذاشته‌اید اگر بر علیه ما استفاده کنند، ما هم این حق را داریم که برعلیه آنها شلیک کنیم.
🔹
می‌خواهند لوله بکشند خب بکشند، اما این گونه نیست که بگوییم پایگاه‌های آن‌ها در امن و امان است و حتما به ضرر خودشان می شود.
🔹
اینها می‌خواهند بگویند چون ایران تنگه هرمز را کنترل می‌کند، ما هم استفاده نمی‌کنیم و به آن طرف لوله می‌کشیم.
🔹
ما هم می‌گوییم حالا که شما این کار را می‌کنید؛ یعنی می‌خواهید به آمریکا و رژیم اشغالگر اجازه بدهید که از سرزمین شما بر علیه ما استفاده کنند. ما هم هیچ موقع گذشت نمی‌کنیم که آنها به راحتی بیایند و آنجا را قطعا زیر آتش موشک‌های خودمان می‌بریم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/akhbarefori/653354" target="_blank">📅 12:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653353">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
آمریکا تهدید کرده که ویزای هیئت فلسطینی در سازمان ملل را لغو می‌کند، مگر اینکه «ریاض منصور»، سفیر فلسطین، از نامزدی خود برای معاونت مجمع عمومی سازمان ملل انصراف دهد!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/akhbarefori/653353" target="_blank">📅 12:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653352">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
۲۰ ملوان ایرانی ساعتی پیش به میهن بازگشتند
🔹
سفیر ایران در پاکستان: از اقدام انسان‌دوستانه و خیرخواهانه دولت محترم پاکستان برای پیگیری آزادی ۲۰ ملوان ایرانی که به دلیل توقیف کشتی‌شان در آب‌های سنگاپور در وضعیت نامناسبی قرار داشتند، صمیمانه قدردانی می‌کنم.
🔹
در این راستا، از تلاش‌های خستگی‌ناپذیر نخست‌وزیر محترم و وزارت امور خارجه پاکستان، به‌ویژه معاون نخست‌وزیر و وزیر امور خارجه و سایر نهادهای ذی‌ربط، تشکر می‌کنم.
🔹
این ملوانان پس از تلاش‌های دیپلماتیک از سنگاپور به اسلام‌آباد منتقل و ساعاتی پیش به میهن عزیز خود بازگشتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/akhbarefori/653352" target="_blank">📅 12:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653351">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bikMjEExAnP13-qEPrRpRcJgyti18QktuBk9A2fSxyR62uUN56RNLEBhboQ6tmPaWPYZv05IzFmpL77D-xHR7l7SLnstOvamq4GfIXLguncsBpSinvdOyehIAVA8V4pMxO1oCSoPXqzA7x2hnsmpi6uY9QWFXt2DsRcKfGtUpy6rDBjQIn1FliPc3ege_hGxeAFsUyuFy_EVLEabWH3nEemIaWrTrEqziF8DX6u5RUXSAHJ_3pT3Ym9NjGCOGuRzQUKVXX4smysx06dn3pTTDv44W-iWj91bsQmCtnNxMDogVoJ7aqJDGVRVJDakkzw5XLXTcRI0ZSJm-prB1gLQWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عملیات شکار پرنده‌های آمریکایی
🔹
۴۲ پرنده آمریکایی در جنگ با ایران از مدار عملیات خارج شدند؛روایتی از هزینه واقعی جنگ در آسمان خاورمیانه.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/653351" target="_blank">📅 11:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653350">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkHsfLQO9cS30_Iyny0EsBpBT0qcglPy8icnOVq6rrDgxX4sfFO82_SZlAeodyHOI2yyBpIDL4xTPX21VOT1sR-gGKdJTpW_DKSLJY152iI3f2W5oQ98hylB1NbNvW9EVAXLJjFdnqYaRL8IQJ1dI7biQiK5YB1pUIaaIh73pW-XSvsYUZLivy0uQreYanLZf6UzoWquiVeuvVh-3NWzdXiE3DWMfFZyvhuROPxSJTiakteK-F8WY1oaQQyfnthi_1RysEo2_fVqbb_zrAch7sgDBkVySrhu4t6utMubO9mxzWLgTBGFSLjLZk4H4MHjp2_Z8jR2JTRgO2CcAsTS5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهر گناه؛ چگونه با وجود جنگ، تجارت جنسی در هتل‌های دبی رونق دارد؟
🔹
به واسطه جنگ و تنش‌های اخیر بسیاری از کسب‌وکارها در دبی با کاهش شدید مشتری، افت فروش و رکود گردشگری روبه‌رو شده‌اند؛ اما در میان این بحران، بازار تجارت جنسی همچنان فعال و حتی پررونق باقی مانده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3216745</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/akhbarefori/653350" target="_blank">📅 11:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653349">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bc0005ed4.mp4?token=jgWLnUowRKD7OBHGXUAR21OoLugkxCYgYJXAsgsQmmQc1NsX3OrVmSd03Y4T1E4qckM0rCnObO0OOIaRyiqG6X7AczP9r4s7xXBJgFa79JrpoRo_FMqOMo2ltPNrU0LMmigJhIRB5pTZHopyFxTlWXN63LNF0cOWx4ne9mGFbwGqnx7HtoC1NuQ1gG_Nrc9zMccTMegtOFiKPzifRSj1IUiLZ4wW_hP0zDFQ2HGYWNpNmIHvNbXlDFkLNPidv_k99Pjk8-xyluMYXvCUqDwN5c0sBrcSwDnI4jcewzEAT1uzsiqgqZr-Q20AE6vJRQK4Zr-hnbdQPVc9t--pFstZ6YUOeCvjfMR3R8hj7KLFr3wO-TDqtB2O3wYjhi4fQPQveBR49qCVs6ckG6h3QNXXLBc5WdXCzm6uJat3UmheB0nLn79vvdHsr9JP_XEA174HQsFapLlpHbl0miT4tWGTKmseW9G-Tu3mCqxQcX_tg_oGvu1J9JEyomXMK6f_PjJExkDPnOxX8Lz5MLQLYgJ0hBC2TcWjdAHRrHRBDVuRPvvv2j0D3QoxM680M7cerDiF1JUZ3QlAA0CSzFATtq7uoFtFBGw-aOL9Ddi2D1HXM8_Pyw2xUHd8A30Sh3_w8tWMTH4TmRXzrBuq_6jjULNqe1-pH6NSi5dC3b4GgM-Ftgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bc0005ed4.mp4?token=jgWLnUowRKD7OBHGXUAR21OoLugkxCYgYJXAsgsQmmQc1NsX3OrVmSd03Y4T1E4qckM0rCnObO0OOIaRyiqG6X7AczP9r4s7xXBJgFa79JrpoRo_FMqOMo2ltPNrU0LMmigJhIRB5pTZHopyFxTlWXN63LNF0cOWx4ne9mGFbwGqnx7HtoC1NuQ1gG_Nrc9zMccTMegtOFiKPzifRSj1IUiLZ4wW_hP0zDFQ2HGYWNpNmIHvNbXlDFkLNPidv_k99Pjk8-xyluMYXvCUqDwN5c0sBrcSwDnI4jcewzEAT1uzsiqgqZr-Q20AE6vJRQK4Zr-hnbdQPVc9t--pFstZ6YUOeCvjfMR3R8hj7KLFr3wO-TDqtB2O3wYjhi4fQPQveBR49qCVs6ckG6h3QNXXLBc5WdXCzm6uJat3UmheB0nLn79vvdHsr9JP_XEA174HQsFapLlpHbl0miT4tWGTKmseW9G-Tu3mCqxQcX_tg_oGvu1J9JEyomXMK6f_PjJExkDPnOxX8Lz5MLQLYgJ0hBC2TcWjdAHRrHRBDVuRPvvv2j0D3QoxM680M7cerDiF1JUZ3QlAA0CSzFATtq7uoFtFBGw-aOL9Ddi2D1HXM8_Pyw2xUHd8A30Sh3_w8tWMTH4TmRXzrBuq_6jjULNqe1-pH6NSi5dC3b4GgM-Ftgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودداری شرکت قطعه ساز کروز از تحویل قطعات به سایپا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/akhbarefori/653349" target="_blank">📅 11:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653348">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43cc421836.mp4?token=TAYvDZG8b0hsPWRxUIO_BlY2KGrcDfpAvCeQ3hD7kV-9W6jcMNQyTtplboKBuQDMVkPEjlydsG90j1q3tv3P4x_HPflsoAMFMYqy4KmctSOulooYhOXH14LO2iiIZ25z09kFuyj6ZcURRvyEvR-YV7B51RkfTEFyL-Qdqki0KnKRMPaEcwWpeg7nBnY4DD2Ws0BiavK0Z4Abix9lcb-3uwY4AtDtrVwPl4Ho2hGU0GKZsabYQXxpaDWMyfdyNWIAb9UGkjIevkoU1MQ0JNpTIGYhLp0l0KVxJlXHR6wS1K87EMUAiRB81jOoboB9zxgoT3_kTUT9w3pkuNK6xgJ6bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43cc421836.mp4?token=TAYvDZG8b0hsPWRxUIO_BlY2KGrcDfpAvCeQ3hD7kV-9W6jcMNQyTtplboKBuQDMVkPEjlydsG90j1q3tv3P4x_HPflsoAMFMYqy4KmctSOulooYhOXH14LO2iiIZ25z09kFuyj6ZcURRvyEvR-YV7B51RkfTEFyL-Qdqki0KnKRMPaEcwWpeg7nBnY4DD2Ws0BiavK0Z4Abix9lcb-3uwY4AtDtrVwPl4Ho2hGU0GKZsabYQXxpaDWMyfdyNWIAb9UGkjIevkoU1MQ0JNpTIGYhLp0l0KVxJlXHR6wS1K87EMUAiRB81jOoboB9zxgoT3_kTUT9w3pkuNK6xgJ6bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توقف اسکرول. شروع کاوش.
به بهترین کانال‌های تلگرام غوطه ور شوید—انتخاب شده، دسته‌بندی شده و تنها یک کلیک فاصله.
🗂
کل کاتالوگ را اضافه کنید</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/akhbarefori/653348" target="_blank">📅 11:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653347">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQ8G5OtYt53cDCkhZLl1MUYlrvIBsSuUWjioI8lz0fJXPLZUiOlDt9wYsZ4LLc38-GiOvlOTzOpIyCUKb1yMsWabduD8Xt6NVmf7lKYjZG1AwZgNL9unwuF7t54UZQP3Z46Blj1OojgdwbPGbZvMmnJ5s1h7HpJ7RNP_NwYjhEqVwrJ_g8xhyN4g4-I6xQePPeJZsSSzh0XNkrwIkA0u16stQoIfFEf4_QSMZeL15Nt6bWGGr5GiqIr7SFn_YgaVvyelAOjAVWYI-YdJ5z7u8aNDxJHFNqcD7PdkhPN3ScUI2mnSUyVbWmJFjOYMIWnmGy1GxaoBuXDLh2QKIgWnww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اطلاعات آمریکا: ایران به‌سرعت در حال بازسازی پایگاه صنعتی نظامی‌‌اش است
🔹
ارزیابی‌های اطلاعاتی آمریکا نشان می‌دهد که ایران سریع‌تر از انتظارات در حال بازسازی پایگاه صنعتی نظامی خود است و تولید پهپادها را از سر گرفته است.
🔹
«ایران در طول آتش‌بس شش هفته‌ای که از اوایل آوریل آغاز شد، بخشی از تولید پهپادی خود را از سر گرفته که نشان می‌دهد به سرعت در حال بازسازی برخی از قابلیت‌های نظامی تضعیف‌شده‌اش در اثر حملات ایالات متحده و اسرائیل است» این بخشی از گزارش امروز به استناد اظهارات «دو منبع مطلع از ارزیابی‌های اطلاعاتی ایالات متحده» است.
🔹
طبق این گزارش به نقل از چهار منبع آگاه، «بازسازی توانایی‌های نظامی، از جمله جایگزینی سایت‌های موشکی، سامانه‌های پرتاب و ظرفیت تولید سیستم‌های تسلیحاتی کلیدی که در جریان جنگ نابود شدند، به این معنی است که اگر آمریکا بمباران را از سر بگیرد، ایران همچنان تهدیدی قابل توجه برای متحدان منطقه‌ای واشنگتن است».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/akhbarefori/653347" target="_blank">📅 11:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653346">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904502ae0f.mp4?token=FalXlY-J0Evhk9iotqUgj90Di7ZAp1jCSw_CU2QDNNAgCQg_To1twVgK4REwZw9sv1dQsTlk4NET0OadTqFPCKGNalgYv2lHMP4IUYfQalIybDUEfUtr7O1JYdhAl7Hg7h6WPbZj7aCWV2qTVAPKaSMPDs35cVSpvDskgTIZWwUI9CerjomS92PJhb1auDQGOfij_eOH3P4AtXr8WPtXcM0KZlKQ6Xmjf_-2TFPCMq7bJMNvfzqwE2fNSMr2H0LLpfD0BCWzGJl2nDAnkB8EaJY2j3qnhlNpcQAG9zr_XS23jsC-7OC2SlzGK6wVraR-6JJIE3W6DxrUa7n7smSs_Lo04nZ5ccrnzDnJmU_qqEVOXBTRDSrs6UV4cwBDXvoilJ_0x02DrV59ZSgwASpf9TdjM9iYcPBNP6RGHqvTA3KuFf07_yrce301lHt_sjgt-sDZEU8g-edDp5fp8-ZKBwo4cHR3xOJcwxBK722oWCtHhUELXq0evk5Zp42A5V_QdxKaZx0T-6GyLN5DJUlxmErEUrQURIe9FNm0tGSAgW06MqqsgLb5pJ-C7wXFkHlylE6vFNq687OYRJtdEqMXvcXc64VruZmIdzz8OtgyQakl5t3qdt834uLLzf7jTlhMD4Qip529LoLUX9DaQZfbhfJ3Hng2lN_oWDISgaNTE8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904502ae0f.mp4?token=FalXlY-J0Evhk9iotqUgj90Di7ZAp1jCSw_CU2QDNNAgCQg_To1twVgK4REwZw9sv1dQsTlk4NET0OadTqFPCKGNalgYv2lHMP4IUYfQalIybDUEfUtr7O1JYdhAl7Hg7h6WPbZj7aCWV2qTVAPKaSMPDs35cVSpvDskgTIZWwUI9CerjomS92PJhb1auDQGOfij_eOH3P4AtXr8WPtXcM0KZlKQ6Xmjf_-2TFPCMq7bJMNvfzqwE2fNSMr2H0LLpfD0BCWzGJl2nDAnkB8EaJY2j3qnhlNpcQAG9zr_XS23jsC-7OC2SlzGK6wVraR-6JJIE3W6DxrUa7n7smSs_Lo04nZ5ccrnzDnJmU_qqEVOXBTRDSrs6UV4cwBDXvoilJ_0x02DrV59ZSgwASpf9TdjM9iYcPBNP6RGHqvTA3KuFf07_yrce301lHt_sjgt-sDZEU8g-edDp5fp8-ZKBwo4cHR3xOJcwxBK722oWCtHhUELXq0evk5Zp42A5V_QdxKaZx0T-6GyLN5DJUlxmErEUrQURIe9FNm0tGSAgW06MqqsgLb5pJ-C7wXFkHlylE6vFNq687OYRJtdEqMXvcXc64VruZmIdzz8OtgyQakl5t3qdt834uLLzf7jTlhMD4Qip529LoLUX9DaQZfbhfJ3Hng2lN_oWDISgaNTE8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا جنگ با پذیرش پایان صنعت هسته‌ای ایران تمام می‌شود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/akhbarefori/653346" target="_blank">📅 11:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653345">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
سایت اسرائیلی واللا: فرمانده تیپ ۴۰۱ که در لبنان به شدت مجروح شده بود، پس از عمل جراحی برای خارج کردن ترکش‌ها در ناحیه سر، همچنان تا این لحظه بیهوش و با تنفس مصنوعی زنده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/akhbarefori/653345" target="_blank">📅 11:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653344">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">همخوانی مردم میدان انقلاب در سالروز شهادت رییس جمهور شهید آیت الله رئیسی
خواهران:
آری؛ چون شهیدِ جمهور
سرباز دین خدایم
من هم خادم‌الرضایم
برادران:
مثل رهبر شهیدم
در این جبهه جانفدایم
من هم خادم‌الرضایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/akhbarefori/653344" target="_blank">📅 11:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653343">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee64f10908.mp4?token=LF6RiPv-k87Q7vOZE3fPTSkgHL8B2GMH4Q2E9k9idM0qOmvvUv4OHSXstYEa-_KwF92nDqs4Q74mYkVBuD8N6_xnkTrwxDsBvukzPH9pV72rzjCaN3Jm1I_i2C0966LRN6f9Go49W12NrOxYNdcXM6YRiHPY4TCEnAgJTQ-CmdSL56TPVr4Iors-3Sjqt0EKTsuHdOcTSJLH8-coAu0LV95JNQNdFBXqLtR6Chvm0-ZND_TRbR1_Xf_FNzcgzNjQ5uD9bYARZVhA3qIYP8uzTBSFHU8pBVSHOta2L7zXaWjXeUvpZ2Cwl7NCHAS1r3_tVLiIAJTZVjaauMRf4mxeGok_pK5rYsS3eoblUxBssGrKEZLLWRsf0qLL1l46pmgbloIS7X2UyAU4QKadIxCS4JjrDFfYX6MZZTL5UsaDRI5DIg5DepmcvTTXJBsAG9a1F_VKump5CNrWXOLWrFAW4L5hutKqenD_l4wuwghGVAqVk7CAwr4ZlAqQ5hVJpXSHhzed0LJCMqqq0j7CO4F_wIuWmgrbf4GpUa8yDoF8HjDHhAbO0fQyJJ4VoXMom_juBqxJBwe4us3gm3nm85bXUkIybKqWSwaL6jOBv3IZqV_tZfdQ34Q_uD9mOP0M605ciJjxsCnW9zcxkLGxOCOCMqjzLHLgihbJbv8CNQRPVa4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee64f10908.mp4?token=LF6RiPv-k87Q7vOZE3fPTSkgHL8B2GMH4Q2E9k9idM0qOmvvUv4OHSXstYEa-_KwF92nDqs4Q74mYkVBuD8N6_xnkTrwxDsBvukzPH9pV72rzjCaN3Jm1I_i2C0966LRN6f9Go49W12NrOxYNdcXM6YRiHPY4TCEnAgJTQ-CmdSL56TPVr4Iors-3Sjqt0EKTsuHdOcTSJLH8-coAu0LV95JNQNdFBXqLtR6Chvm0-ZND_TRbR1_Xf_FNzcgzNjQ5uD9bYARZVhA3qIYP8uzTBSFHU8pBVSHOta2L7zXaWjXeUvpZ2Cwl7NCHAS1r3_tVLiIAJTZVjaauMRf4mxeGok_pK5rYsS3eoblUxBssGrKEZLLWRsf0qLL1l46pmgbloIS7X2UyAU4QKadIxCS4JjrDFfYX6MZZTL5UsaDRI5DIg5DepmcvTTXJBsAG9a1F_VKump5CNrWXOLWrFAW4L5hutKqenD_l4wuwghGVAqVk7CAwr4ZlAqQ5hVJpXSHhzed0LJCMqqq0j7CO4F_wIuWmgrbf4GpUa8yDoF8HjDHhAbO0fQyJJ4VoXMom_juBqxJBwe4us3gm3nm85bXUkIybKqWSwaL6jOBv3IZqV_tZfdQ34Q_uD9mOP0M605ciJjxsCnW9zcxkLGxOCOCMqjzLHLgihbJbv8CNQRPVa4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خدمات مترو و اتوبوس تهران تا چه زمانی رایگان است؟
🔹
شهردار تهران: به علت اینکه در شرایط کنونی نمی‌توان مجدد خدمات اتوبوس و مترو را پولی کنیم تا تعیین تکلیف طرح ارائه شده در شورای شهر تهران خدمات اتوبوس و مترو رایگان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/akhbarefori/653343" target="_blank">📅 10:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653341">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLv0sWyexIfRQHLyYmrFbMgCarW5B-eeRsn0Zt7VU2Z6OXv3NVsFAXvlSHwhiZQEy4yPe2y5WkkE8_Rr-kkdhmgOCumIlOin7PfospFkb07Pl6qvhL-KqGCpRYuJ7UXgovleClDm_dpg0a76cscwgye_0qt0ls6DCa4RpReKbDoefMNYhSopTEq3rbMXcirqHIMZ8kAeniWLWgv6_j_dPpsQ_wdtihbdm6tMLzH5B6vNUQEVSMsLJrvSgl11wDYfRlOlG1azH8vOzhURS9pxbn1g0wvyfuCTZb1jU1rMMHpiigi4daC1EQCv8qol3GNGggTCUR4zTAWL588Si8Z_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a3utNg7CyGubtyXbUtqE59sBAPCkeOG5Hkay3WvsSgckojB7mrbQQcjHfo0XwazKlyYZMYnOS4fZvDwS8txaKuKpznuoHOi8om9yBuDm_0LDhNhxp6lmDMJU5gUxBiLyGSyus-4mtfNKh6GXGWvun1oqUjEZ3iBorid1adgjRZluemm8YHGHikxIxPldyr5vrCu5nvcx3BNggTO6ksOX7xX4dolg7fB6DGyXsneGE5rW9aNJXrypFOtvDagFp9yZmx9D-qyjQ3gEDUSd5YQptJcwBoRSVH-Z1llWeRQbpAkwDuRAjxkpQD3s9BtdTtrPFLi87M7tlYnKXgIVhKkJsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
زمین می‌تواند خانه‌ای سبز باشد یا انباری از زباله؛ تفاوتش در انتخاب‌های ماست  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/akhbarefori/653341" target="_blank">📅 10:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653340">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U72MmivYrk18SkSDffJ9trWWYE-an21Cs51Nh2YnivVcOZ_40Vs--t1MMEdCwNOc5ZFUf-XR07V8QwbQDcrBx2O_gVp-h2Flewni6A8zo_2d7a2WVeNpsU3_0A4nfAtWwpTODkWu0OAU_R_hlYrA71cbD8OB7anikJBGw85wYjvPSdTqKCG4xWDMjP0hU1Vk-f-WZNfSakJmpbzXkVuYS_8j2kFidsFz2LETcWGjzDUOXiSRv3HilrKbD3UIA4x_k4KQqeJBFGwm60q7M0aF361s8yT_eWwJ9gkrsueKn2MJWFon7srDXsScqxRwEDsAEVx7EwMwRiTIL5_PR-t0bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراف زنجیره‌ای افسران اسرائیلی: ماندن در لبنان بی‌فایده است
🔹
رسانه‌های عبری امروز تصویری شفاف از بحران ارتش اسرائیل در جنوب لبنان ترسیم کردند. از اسرائیل هیوم و «هاآرتص تا معاریو و والا همگی از زبان افسران خط مقدم روایت می‌کنند: مأموریت نامفهوم، استراتژی نامعلوم، ناتوانی در برابر پهپادها و در یک کلام: یأس و ناامیدی.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/akhbarefori/653340" target="_blank">📅 10:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653339">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHxVN-ak9pDG0vlAw_yhtSJHNWqEFQNVZh92eblFld-u0DfmnKxtqBvRNbC1EM0pHUX5YBcnF_5j2C9BmU72-QJwksicZ16q_sJp8D0MaBpNRES75srdkX0CT75pH7rjn8iPZg6Y4pHt_cyaiKLpuwgwlMVKtcvkyTDIywtb4PbU0_0Le0DcTWMVsLadTfwm2iH0CKyp2O16u9G4MxdSjb6e25H-yPdhNSiE_ZKuNEMTIilzLLtSowKcdu2OvZZXzntNB5eM9eCmRGMKYDotZrhFtnfxkJVl3hrla6mrqHi2gild4RXi0ksbCZRV6ulTo_CB-I8Y1ZD4Ha8am1siEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اردوغان خطاب به ترامپ: حل اختلافات واشنگتن و تهران امکان‌پذیر است
🔹
رئیس‌جمهور ترکیه در گفت‌وگوی تلفنی با همتای امریکایی خود، ضمن استقبال از تمدید آتش‌بس میان امریکا و ایران، تأکید کرد: دستیابی به یک راه‌حل معقول برای پایان دادن به اختلافات دو کشور امکان‌پذیر است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/653339" target="_blank">📅 08:59 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653338">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jp-IM8rdQ9gQULKV5XeUNOODJxHcc24HpoEvnPE7b7iSDG_ZJNmyUKUIxEaABnPCzlIET8AjDMwbqI52Q0rF10_vVXacANAz7fkQb0IRfkc3wbar8XQz2E-xjUK-0SM9i0PF5QC5Q4JR07b8lvOHRPPH6Oea_pDEKT9FxNfnIAKpTAduoDhTi9YJKXLzcxnPNELlYb-m-5hSW-OhZEd8JdPV26AS66O_HJ8n2QnpjYQ7lxgeLtaxClN0pwx7Vl_fzH5IdbnJcA3Rw_bpZMAshnkKeEwyFdMgMfX9SpQtYUlqpXR0I7gVH8q9BtIK6Rcm3WB2TM9_hIn_tMI3VDIrgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهر بررسی کرد؛
🔹
بحران تنگه هرمز؛ بازنده واقعی محاصره دریایی کیست؟
🔹
تنگه هرمز به عنوان گذرگاه حیاتی عبور نفت جهان پس از تجاوزات ۴۰ روزه علیه خاک ایران و متعاقب آن، انسداد آن از سوی جمهوری اسلامی و نیز محاصره دریایی از طرف آمریکا، دوباره در مرکز توجه جهانی قرار گرفته است.
🔹
از نگاه ناظران، بحران تنگه هرمز نه تنها یک تنش اقتصادی است، بلکه یک چالش بزرگ سیاسی و دیپلماتیک نیز برای آمریکا و متحدانش ایجاد کرده است.
🔹
پس از آغاز تجاوزات و تقلای واشنگتن برای کنترل مسیر اصلی انرژی جهان، متحدان سنتی آمریکا در ادامه همکاری با کاخ سفید دچار تزلزل جدی شده‌اند؛ وضعیتی که پیامدهایش فراتر از میدان نبرد انعکاس یافته‌است.
🔹
بحران هرمز نشان داده که هزینه‌های سیاسی این محاصره برای آمریکا و متحدانش بسیار فراتر از میدان جنگ است؛ تردید متحدان، فشار برای راه‌حل‌های دیپلماتیک و واکنش‌های جهانی نسبت به استراتژی‌های یکجانبه‌گرایانه آمریکا و ستیزه‌جویی رژیم صهیونیستی همگی ساختارهای سنتی همکاری را تحت فشار قرار داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/653338" target="_blank">📅 08:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653337">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af6e54b6e3.mp4?token=Be_1PqCm8tU4V5AbRMCVFwSsvm2gzuBVA1TtAGBGZELY19c5W-priRtXC_IKeCHqq_NqKNY5OX0N5sKoje_GMOxzevyLVZ9QxXZeLQ2zXEwb-kTvGqxQZ-KkpwL029y0cN7oKgDnna1zwyZ4hI4dn_M4K90U6eVf6qfvjYfRAAImO0V7E8nsLWtxtzbmHrmppSm7Tu9JP9sbRz8cfsBvJryupWWR04KBbdz76xH67263zyp-LqgP2pXdm9q7mXT-wfN0uhkh8d8PtFO1wZGAN7AWA-SkQ8gf050SoHvRZvEJzdeS55FNjoOolrWhlSfb_j_CmyMB10gnmkvJLg4FZVAlqnXD-tZ6PeTPv9K5mPIs6HsDS0MeB_Ix5groJ5RXIg7tBgxojr_C55cXk2cERVfneN0RgfV6Ce7HR_67KHSfNevQSo1wXPEP6LuhsIKtjoHd8CeWk0O-dUzu1xZVWn5OIyH2H6IBdVKb0PIByHUu3gkM3L05RfhDYBr_wLvBjTSOWKYUpp3KEMsgsZKi9ZtUX7XFvfAdABL2Io1rZpdQutMvBqCxUxnK19k1ViC9nTM9CfpNqtcMlKBPqCJD0T1vDXA4mZwhABedwfz4CVXzGPkBLStS2zOpiPp6nwOjKyCvDCAOyiHhEnTfUUtFlx4toT7SaWHZGoAQACXG3OM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af6e54b6e3.mp4?token=Be_1PqCm8tU4V5AbRMCVFwSsvm2gzuBVA1TtAGBGZELY19c5W-priRtXC_IKeCHqq_NqKNY5OX0N5sKoje_GMOxzevyLVZ9QxXZeLQ2zXEwb-kTvGqxQZ-KkpwL029y0cN7oKgDnna1zwyZ4hI4dn_M4K90U6eVf6qfvjYfRAAImO0V7E8nsLWtxtzbmHrmppSm7Tu9JP9sbRz8cfsBvJryupWWR04KBbdz76xH67263zyp-LqgP2pXdm9q7mXT-wfN0uhkh8d8PtFO1wZGAN7AWA-SkQ8gf050SoHvRZvEJzdeS55FNjoOolrWhlSfb_j_CmyMB10gnmkvJLg4FZVAlqnXD-tZ6PeTPv9K5mPIs6HsDS0MeB_Ix5groJ5RXIg7tBgxojr_C55cXk2cERVfneN0RgfV6Ce7HR_67KHSfNevQSo1wXPEP6LuhsIKtjoHd8CeWk0O-dUzu1xZVWn5OIyH2H6IBdVKb0PIByHUu3gkM3L05RfhDYBr_wLvBjTSOWKYUpp3KEMsgsZKi9ZtUX7XFvfAdABL2Io1rZpdQutMvBqCxUxnK19k1ViC9nTM9CfpNqtcMlKBPqCJD0T1vDXA4mZwhABedwfz4CVXzGPkBLStS2zOpiPp6nwOjKyCvDCAOyiHhEnTfUUtFlx4toT7SaWHZGoAQACXG3OM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متکی: با اولین شلیک آمریکا، جنگ زمینی را آغاز کنیم
🔹
وزیر امور خارجه پیشین کشورمان پیشنهاد کرد اگر آمریکایی‌ها جنگ سوم را آغاز کردند، با اولین شلیک آن‌ها، ما جنگ زمینی را آغاز کنیم؛ یعنی رزمندگان ما به گرفتن پایگاه‌های آمریکا در منطقه، با گرفتن اسرا، مصادره دارایی‌ها و امکانات نظامی‌شان اقدام کنند، این عمل، توصیه مقام معظم رهبری را در رابطه با غرامت‌هایمان نیز عملی خواهد کرد؛ زیرا اکنون ماه‌هاست که می‌گوییم غرامت باید پرداخت شود، اما هیچ پاسخی دریافت نمی‌کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/akhbarefori/653337" target="_blank">📅 08:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653336">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
۲ تروریست عضو تشکیلات مخفی گروهک‌های تروریستی تجزیه‌طلب به دار مجازات آویخته شدند
🔹
رامین زله فرزند کمال و کریم معروف‌پور فرزند کمال عضویت در گروهک‌های تروریستی تجزیه طلب، به جرم تشکیل گروه با هدف برهم زدن امنیت کشور، قیام مسلحانه از طریق تشکیل گروه‌های مجرمانه ، تیراندازی و اقدام به ترور در راستای اهداف گروهک تروریستی پس از رسیدگی به پرونده‌ در مراجع قضایی و تایید حکم در دیوان عالی کشور به دار مجازات آویخته شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/akhbarefori/653336" target="_blank">📅 08:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653335">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCpfU-uKigS-LQmoQzr8k16yVB5UAnoTkpTJao2Bs6sg-2vQP662IPP4-WXlXW0LE63M8AbnVqG7_s7fxZbtdR-8s7iCRrhmyDTH4ypVz8sUMnl3xDEg_4cn00HSoJgcfLttHdwibzqEphl0N7SyrHb6lfFaeabcs0rEa_dwQpnzhpsnvlNTKb5SoMq6H3hNZCe9N-bKZcLrc0iOgZNETatF-z26SvUxohTBloFRuxqdaUxmbmmAf7u1pz75-1urnWSA06zUxltdlatB9jLX6qpXWQqPogomXjrChO0lf9ZeDoA6p5xZV5ypS69mHeKhNBA-kqQ-JxT0w4EEWqUhBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ولایتی: نقشه کریدورهای منطقه را نه با تهدیدهای واشنگتن، بلکه با واقعیت‌های میدانی تهران می‌نویسند
🔹
مشاور رهبر معظم انقلاب اسلامی در امور بین الملل: اکنون نقشه کریدورهای (راهگذرهای) منطقه را نه با تهدیدهای واشنگتن، بلکه با واقعیت‌های میدانی تهران می‌نویسند.
🔹
ترامپ در پارادوکس «تهدیدهای روزانه ایران» و «مشتریان عصبانی پمپ‌بنزین‌های آمریکا» گرفتار شده؛ او برای مهار تورم داخلی خود محتاج ثبات بازار و کاهش قیمت انرژی است.
🔹
از سوی دیگر، تغییر محاسبات در قفقاز و کمرنگ شدن واژه تحمیلی «کریدور ترامپ»(زنگزور)، نشان داد که اکنون نقشه کریدورهای (راهگذرهای) منطقه را نه با تهدیدهای واشنگتن، بلکه با واقعیت‌های میدانی تهران می‌نویسند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/akhbarefori/653335" target="_blank">📅 08:30 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653333">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">قسمت بیست‌و‌سوم - پادکست کافئین</div>
  <div class="tg-doc-extra">بهرام چوبین</div>
</div>
<a href="https://t.me/akhbarefori/653333" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
بهرام چوبین؛ و پادشاهِ شکاک
🗓
وقتی در سازمان یک نیروی «ستاره» داریم، چگونه غرور کاذبِ مدیریتی می‌تواند حکمِ نابودیِ کسب‌وکار را امضا کند؟ و چرا برای یک نیرویِ متخصص، مهارت‌های سخت (Hard Skills) هرگز جایگزینِ سیاست‌ورزی و درکِ قواعدِ بازی نمی‌شود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/akhbarefori/653333" target="_blank">📅 07:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653331">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee3868b761.mp4?token=NYCi7_1C8GMycgpgu1Ek6BsmAJEO9ShPhEhZ048NHIJE5AQv_TJex02aXRykP98XlPNS5GRkXUwJB_In4beH31vHr_UunXWFLXlme51r3MybgOwuYtlAbiSgFGnFDI31KZiKxbI6Byjf9ek4aOsq3xmg7yxBoaOXxwKu4PG7673EawX90KxboCcG_YVvMbu7HzUDdwp3jqvg9LesngxtJgyFXc2pgDf7AqFs2NVVhpPYiCzrtdWrxZ7RIoToAFvd5ZYdQ9rs8sEOtgC2WHVx1dtrzrvcWUzClmD316pO5MJ4uzQk66WQR9nQdzOZHNWjAiN78mPVNkMSPy3ibz5OrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee3868b761.mp4?token=NYCi7_1C8GMycgpgu1Ek6BsmAJEO9ShPhEhZ048NHIJE5AQv_TJex02aXRykP98XlPNS5GRkXUwJB_In4beH31vHr_UunXWFLXlme51r3MybgOwuYtlAbiSgFGnFDI31KZiKxbI6Byjf9ek4aOsq3xmg7yxBoaOXxwKu4PG7673EawX90KxboCcG_YVvMbu7HzUDdwp3jqvg9LesngxtJgyFXc2pgDf7AqFs2NVVhpPYiCzrtdWrxZ7RIoToAFvd5ZYdQ9rs8sEOtgC2WHVx1dtrzrvcWUzClmD316pO5MJ4uzQk66WQR9nQdzOZHNWjAiN78mPVNkMSPy3ibz5OrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهرام چوبین و تراژدیِ مدیرانِ کوته‌فکر
#پادکست_کافئین
| قسمت بیست‌و‌سوم
☕️
در این اپیزود به سراغِ سرداری رفتیم که تنها با ۱۲ هزار نفر، ماشین جنگیِ یک ارتشِ چند صد هزار نفری را در هم شکست، اما قربانیِ ناامنی، پارانویا و عقده‌های شخصیِ پادشاه خود، شد.
بهرام چوبین ثابت کرد که تحقیرِ یک نیروی نابغه، چگونه می‌تواند پایه‌های یک امپراتوری را ویران کند.
هر روز صبح با یک شات غلیظ از تاریخ آمادهٔ شروع روزتان باشید!/مدار
از اینجا ببینید و بشنوید
👇
https://www.aparat.com/v/elhxc81
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/akhbarefori/653331" target="_blank">📅 07:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653330">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzhaxBV13vLXbZIZqUM7ITamYXoyvzjk-MgSBO27rRS4IOqGvIVUfNfv2we2cgYSEY1g_GHeu4o-fp2SAVUL5u0Y4l-Y9SS2R7RTNLVAKnG2iDTHJwX4tvxP-QwJ-KHy81gWsE4VXJxCast4h9Wob9hH2aduH_nwliYfv3ZwnwUuYDQzColmPHp1uVaigzyTXO8U-hrCCvzWyn8hIXuNlHrYdhz1kXZyy9Ue-Vnk1Wp98A_tgepTs58MhAi4c4PjRhkwde7unjBVDM4FCA_HIO3pCePqsCLdb-eUC9j5dQEtaZVXrifZJ3k6Ni6me4KPrI6CXAg7Mm6doAzVlvnZag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۳۱ اردیبهشت ماه
۴ ذی‌الحجه ۱۴۴۷
۲۱ می ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/akhbarefori/653330" target="_blank">📅 07:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653329">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ایروانی: رژیم صهیونیستی بزرگترین قاتل غیرنظامیان در جهان است
🔹
سفیر ایران در سازمان ملل در نشست شورای امنیت سازمان ملل درباره حفاظت از غیرنظامیان گفت: شورای امنیت به دلیل کارشکنی یک عضو دائمی که خود متجاوز است، در انجام مسئولیت‌های خود در مواجهه با این نقض های فاحش شکست خورده است.
🔹
شورای امنیت نباید در برابر تهدیدهای مکرر و روزانه رئیس جمهور ایالات متحده علیه ایران، از جمله تهدید صریح بمباران ایران و بازگرداندن ایران به عصر حجر، نابودی زیرساخت‌های انرژی، اقتصادی و صنعتی کشور، هدف قرار دادن دانشمندان هسته‌ای و مقامات ارشد ایران و حتی لفاظی‌ و تهدید بر نابودی تمدن ایران، ساکت یا بی‌تفاوت بماند.
🔹
رژیم صهیونیستی بزرگترین قاتل غیرنظامیان در جهان است و شایسته هیچ پاسخی نیست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/akhbarefori/653329" target="_blank">📅 05:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653328">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
فرستاده ترامپ: زمان بازگشت و تقویت حضور نظامی آمریکا در گرینلند است
🔹
فرستاده ویژه رئیس‌جمهور آمریکا در امور گرینلند، در جریان اولین سفر رسمی خود به این جزیره راهبردی، بر لزوم احیای جایگاه پایی و تحکیم حضور آمریکا در این منطقه تاکید کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/akhbarefori/653328" target="_blank">📅 05:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653327">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ایروانی: شورای امنیت نباید در برابر تهدیدهای مکرر ترامپ ساکت بماند
🔹
سفیر و نماینده دائم جمهوری اسلامی ایران نزد سازمان ملل گفت: شورای امنیت نباید در برابر تهدیدهای مکرر و روزانه رئیس جمهوری آمریکا علیه ایران ساکت یا بی‌تفاوت بماند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/akhbarefori/653327" target="_blank">📅 04:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653326">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
مدارس سمپاد برای دانش‌آموزان دهک‌های ۱ تا ۴ درآمدی رایگان شد
🔹
رئیس سازمان ملی پرورش استعدادهای درخشان: حق‌الثبت برای دانش‌آموزان دهک‌های ۱ تا ۴ درآمدی به طور کامل رایگان است.
🔹
دانش‌آموزان تحت پوشش کمیتۀ امداد امام خمینی(ره) نیز در زمان ثبت‌نام آزمون‌های ورودی از پرداخت هرگونه هزینه معاف هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/akhbarefori/653326" target="_blank">📅 04:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653325">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
همسر یکی از اعضای کاروان صمود: هیچ خبری نداریم که زنده هستند یا نه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/653325" target="_blank">📅 00:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653324">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9MzOiGkmlEaks2vojjVYh-3x1peHFELNGBUlnyy6Bc8ZDUP0NeOpfRvkiB_bmOWmO_uZlbHkOFCSP695Zw-64IpAtfMBQkk7LMzP8MzVAm_P9zy0p0uj3E_p9Olpg2KwZ3ZyevQgVA0YJPAz2obqZCt_kHTStnvq0OMWXRviyfuzUE6A7WEllrqWXIh4431uguxJK7YSuWsZPcrhi82TB0yVHvCXszUObXMMgmXpeQ1neVrzHL6uBzwAlfzkDG2iW5NW6CDcY5rt1u5d2ySp2ojrT0zZoHHxyYpAO7Wtvc4YTMuXFOUdCPjxZW2RZW0YVZ4LYAwAJY2fuaOjxpgOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کاربر در فضای مجازی
چرا خط های سفید احراز هویت نمی شوند ؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/653324" target="_blank">📅 00:30 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653323">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPXWMzbTIqO_Q2uy8MOseZwiveq8mkLvszmZBOnTXxIWAV3CXUFmty4tSVATsple39dM7iG2pRitAEJoxqGd7NXcMMsMm8_n7pwRBOZ0sk_hVd2EOybsCKWjctqFiYOgmo1UMnM63gSy9pAJ91pDqztV8aPP0PR8csorepGfJ-wpwA49XSgU1mfVe3EMFzor_v3AISQ6zABmO7pF--wYpcId8hv6ylXxzi9NHuP67AY4Dk2K1YHf_dd-Uz8A4hvowGQazZWQu7ljEAAa-toVxffo91jaWWE_Gr4LO0o72ivgAGR-4NocKHT7S-1W-LcJYAWNwMxYFMDdR3RjGwIS4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه دیگه کسب و کار های زیادی نجات پیدا کرده چرا یه عده عصبی اند؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/653323" target="_blank">📅 00:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653319">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7OuJ4OIqcidaYNJfSFzzd2S8hJT7B1MC-FVwFMpr8Q692ompasMeeXW7InbR9ygM9iscHSgRgs6npWBvdlEUD4Oiu3wGT3PqARr-rjKp7QWisB1HYxToT38B9le4bFcNgDcm7ze5sjGJOxW_E0lKQbqi41Ndjzey24D64sMpNsRHesC1T3Rhd0s7aXT6zL3j5IW8kU9SiEwpX-cGzIHoUvXvrEkjj6GmDUGbC9md793hfNNdwOTWPvybUf7z_I7k1uDy_OTR91Ia-8Rp9RCSZd8aijhatLU8weDL2d1atI148ILjQd234BKPQMch56t088oAR9sCoYdMPQ-WOtFIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N44oKwFRV47fKumTj9q459Cshiv7PLZ3rMxJKlVufg37apw17pspGZM1F3Nf319GA9X6ni-NgGcISQ8_Wkz4RcUGxiG8-QUzyTL0A4QxDtSmXkkgz03k7bauvyp-HCBW2TR7KOrMx3Jyf6MkdZQApFpBj8UcRA8WN2k-22DO6hE4DXtyNpM0SHq4vLqubtycDySpc1Hs2U8sDyv3VknctbceD0RLdN1b_Lk2kgm7Jow1YBVwnlg7Q80aXadKNFcfP7nhhnH7zzXCgc-bZJ48rjhr2JYDglcEaHR9fZu6jqqd8rQXhz6BloZVwSEI3fiMEgc7rsp7HC3lUMl7k6iQ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJPa5qOZROydddbLyuL3dhHW5yV3Ncz_wK-dEaY-2DHoXVSge46eH967kJkDgxriHbBM9g68ra8dldS9mQo72WCxEbAJnW-gG5EMq_VqlDI93KXeWC8x_jHwSboso80kwETXy36ciBQ8uIgW3rylJ3pafqftHQSagF1QU6yfB2a-Nh4uJgqYnvB94WBH2Vt9aXgwLdairudK-fjMR1Od2SpgVk4NDk3dPHuZlbcGjDJJxyXfECSO_WnESPKf8qy-WSB2nc3huK7emDCyZNiHoxmH54YEObfOpzSu_SEX1B1qHcLpFYAs5g5hhIMCaCVh-NJeoV8-H5lLJ9RfvQ2uIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tR2bYfJ_lnFdYnWhAeUdi40IzH0nHCNmnmrKAF9Hw3YeL2_tb3Kidn77Vxj1bGMxZv8MhU21m67FSCKAGLVanrLtozWy6D_sqHMrSoH479Xtb2Oxdcu3Xj1S-r5I2c_8uAjKs9hW1J_0Hy3V43OYEB_PmoKewuKTjw_PZzuJR8XCWq9aPF32eRD8fqkNLkb9cJwYALrGdgKzCu35n447T_0J0YIVtNrr3OOehvqPsNgnYx6E4DtwQY-nMoAXXq4VOJraB4H5PuyZy7rb4_siMLSyHpidmlsFmHZMsF1fjs48i4jQbHAultmKk3HD4NC8R8NoN4nT_z8yUCidZoPQnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شیراز در حصار ریزگردها
🔹
با ورود سامانه گردوغبار به استان فارس، امروز وضعیت شاخص آلودگی هوای شیراز با ثبت عدد ۴۵۰ در وضعیت خطرناک قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/653319" target="_blank">📅 23:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653318">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQBBbZltERBRDdAjZ3gS5q3Hx3GGvMxO2i7ToSnX2tCeWStmm4jv5xgoPbcLCX6xPm2hWD9AjW-lVbM8do-w5sSfqTwa71T2Cze8Ag0SR5v9vIhnrX8wcp1eHFScpnG1ydrTmqLBrNL7fGxfzM6PlVUgseDsgFcj5tQ9eD9q-oNhpLq57sylRC47jykEbUWT7R1oO1UWLzUC12tYGUS_c5F67KINFX62Z_PNbzBaYjMqjM8DW92u1rXSN8qOglRj5-lEQTEjbXLk3J1du5ZLz0St1OY3bvYIhSqsHKja-RhISZCmIE-NNspPv5I-p-b_UQhJQT0V3PHtFLooYLmGKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیکی: عملیات نظامی پرهزینه آمریکا در تنگه هرمز شکست خورده است
🔹
روزنامه ژاپنی نیکی نوشت: بیش از ۱۶۰ نفتکش در خلیج فارس گیر افتاده‌اند، زیرا ایران کنترل خود را بر  تنگه هرمز افزایش داده است.
🔹
عملیات نظامی پرهزینه ایالات متحده در بازگرداندن عبور و مرور پایدار در این آبراه مهم شکست خورده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/653318" target="_blank">📅 23:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653317">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
دلیل عقب‌نشینی ترامپ فاش شد | ایران به توانمندی نظامی تازه‌ای رسیده است
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3216606</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/akhbarefori/653317" target="_blank">📅 23:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653316">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
پلیس سیستان و بلوچستان از هلاکت ۲ نفر از عوامل شهادت ستوان سوم امیرحسین شهرکی که عصر امروز در سراوان به شهادت رسیده بود خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/653316" target="_blank">📅 23:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653315">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f94bdb13.mp4?token=M4lVT2xL_E7I6id-dsRaCLRjDw8qHT16-l2HWNq2OCgVA0XcqeydnZR59lQFgJFgcWBhRDm4CYVSithnlTO4mgDh9-geHJfkoHXp8VC6pMr-aUTmgqjK9qoafW_M8rkSDWW4MVoUj9NZ7scFEWnacFe1tL3GCp6_lipyDRF20AoaQEW5Ivq_wkN92jM--QmKn6fF6Mc_6peLI-8IK84Oca-CUrdI1vYtDJXqJW_0-YFVuqSnO4XA6Ng5efUE3DqgFeMwiK0YvDyIM9aaKrHJAWF5krzdKBxc0SQP-ejtPmiYRTkAsQnzWV2U52US5uJvlwTE0aDQsObgdzcLWi3VCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f94bdb13.mp4?token=M4lVT2xL_E7I6id-dsRaCLRjDw8qHT16-l2HWNq2OCgVA0XcqeydnZR59lQFgJFgcWBhRDm4CYVSithnlTO4mgDh9-geHJfkoHXp8VC6pMr-aUTmgqjK9qoafW_M8rkSDWW4MVoUj9NZ7scFEWnacFe1tL3GCp6_lipyDRF20AoaQEW5Ivq_wkN92jM--QmKn6fF6Mc_6peLI-8IK84Oca-CUrdI1vYtDJXqJW_0-YFVuqSnO4XA6Ng5efUE3DqgFeMwiK0YvDyIM9aaKrHJAWF5krzdKBxc0SQP-ejtPmiYRTkAsQnzWV2U52US5uJvlwTE0aDQsObgdzcLWi3VCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عاصم منیر، فرمانده ارتش پاکستان، در راه تهران
🔹
عضو کمیسیون امنیت ملی مجلس: عاصم منیر فردا حامل پیام جدیدی از سوی آمریکا به ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653315" target="_blank">📅 23:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653314">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i19CC4aDb0xFyCWt77U2N87SNZKUd-4Qdp0GHZaUdl-ItSPYRmQq4FjJ-RjJ5b5GVSYtyRRbIXyT64QqOGxNhY8fBF5iXn1L_ZadybSWk5diPKVPOLM2eUOzmCzogsfGf-iuskRnKL7uGbqAYvovD9yL0KPc4PB3-QzMQch0BcScapAJ-k5QRoOtD5A1tFrOj3R7umTGZp-zOLk35ge4UEBoAaivifUyQvMw_QstXjg2wqFm8lECEP4RP4ZZRUacDIBgroz1L1E6fEv2rTkfOdN-SMhSXMfjcg-0WyvbAUT5NBt7UgZs-Z0xMqjmE7u3Bnv1oZSOcr_OaQa6EwlC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیش از ۸۷ فعال در اعتراض به ربوده شدنشان توسط رژیم اشغالگر و در همبستگی با ۹۵۰۰ اسیر فلسطینی در زندان‌های این رژیم، دست به اعتصاب غذا زدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/akhbarefori/653314" target="_blank">📅 23:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653313">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
معاون نیروی دریایی سپاه: دست به ماشه‌ایم
🔹
اگر ترامپ در ذهن خود فکر می‌کند که با زور و ناو می‌تواند تنگه هرمز را باز کند بداند که همان نیروی دریایی که گفتی از بین رفته، تو را در قعر دریا فرو خواهد برد.
🔹
دشمنان ما بدانند اگر فکر می‌کنند با زدن زیرساخت این ملت عقب‌نشینی خواهد کرد، اشتباه محض است و این ملت در این ۴۷ سال نشان داد که خاک می‌خورد اما خاک نمی‌دهد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/akhbarefori/653313" target="_blank">📅 23:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653312">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
احتمال اصلاح برنامهٔ توسعه و بودجه ۱۴۰۵
🔹
رئیس کمیسیون زیربنایی مجمع تشخیص: باتوجه‌به شرایط جنگ در راستای اصلاح برنامه ۵ ‌ساله و بودجه ۱۴۰۵ بررسی‌هایی انجام و پیشنهادهایی آماده شده است.
🔹
همچنین جلساتی برای تهیه پیشنهادها جهت تدوین پیش‌نویس سیاست‌های کلی پساجنگ برای بازسازی و اصلاح برنامه‌ها برگزار شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/akhbarefori/653312" target="_blank">📅 23:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653311">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
از کنار داغ‌ترین خبرها و گزارش‌های امروز ساده عبور نکنید
🔹
احتمال اعلام توافق نهایی ایران و آمریکا تا ساعات آینده
👇
khabarfoori.com/fa/tiny/news-3216395
🔹
رمزگشایی از پیام مهم سپاه به آمریکا
👇
khabarfoori.com/fa/tiny/news-3216611
🔹
گزارش جنجالی یک رسانه آمریکایی درباره رئیس دولت نهم؛ دوران گذار با احمدی نژاد!/ ادعاهای عجیب نیویورک تایمز درباره حصر و مجروح شدن او
👇
khabarfoori.com/fa/tiny/news-3216619
🔹
عکس فوتبالی شکیرا اینستاگرام را منفجر کرد
👇
khabarfoori.com/fa/tiny/news-3216595
🔹
استقبال متفاوت پکن از ترامپ و پوتین | پنج نشانه روشن از دو نوع رابطه
👇
khabarfoori.com/fa/tiny/news-3216539
🔻
ویدئوهای جذاب را در آپارات خبرفوری ببینید
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/akhbarefori/653311" target="_blank">📅 23:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653310">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tno-s0DuRgdZAvnSDbc3MBT_EtY4goIYCQKeo6u2Nk13s5B3T3Y-ksWg7cgTm1wKnOokDhMZDIpHDq1MNR_QPmcxEtGu-tJqShHlh5pM6yAnYxEqWFv8yv41IfvEhDBWoRCZQMH4yQQWp1l1cEUvkasDSzNHigDPnyUC5b0yrcBEalFe4nC321iUU75oT8vmDSr-Athee76OZg4qlaEZOpj0UNdvoaxX7i-Uc3P-dvYkH0Z4uoCSvOi25x5Zt18VyIKLyY7oivavhBdolTfLe0iljoScI_-D1pA5j7mmfR_vKyAhc2uMKxk27SKyo2CJVMLr3PXHqX80uLR0FehNbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکورد ۴۲ ساله شکسته شد؛ سقوط ۱۷.۸ میلیون بشکه‌ای ذخایر نفت آمریکا
🔹
آخرین آمار از کاهش بی‌سابقه ذخایر نفت خام آمریکا حکایت دارد. در هفته گذشته، مجموع ذخایر تجاری و استراتژیک (SPR) این کشور با ۱۷.۸ میلیون بشکه کاهش مواجه شد.
🔹
این رقم، بزرگ‌ترین کاهش هفتگی از سال ۱۹۸۲ (اوّلین سال ثبت داده‌ها) تاکنون محسوب می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/akhbarefori/653310" target="_blank">📅 23:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653309">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f94115f3.mp4?token=I2sZcE46KtLXVbH8KUQsn8gx7cfuCGC7Gt2Xql4wOPBSYZkTKbtLXqRQJXG6UQPQe1G3myeHQRuSQcxJIzb2TRVoBGcQkKmgPDETRWB2kUWe3c01lgkliYx4WHlNrK4dof4L9rccAH3FL388Inn-MAouY_Ce2DObLpXYuzHQDUnChdwYRHcshjJMweRL6DVoxNLX4iJX5z379DawW9ynRgzR_pm6tCkmN4tCv6UjwULE7BbIzpqmG9Tg5-KOApby693h1odlMdQwOW4oRKFlSHXOV5ruAo9o4w7PpqSo-t96lZh1A3nypQNg3veaidhbNmurdmt82pQUTx1r4FtZ5lSxfKmpeU-lUb_4opC-oE6ZcB6hNq8y_hdw0GqIdXnOs33pm2tllB7BT7fc_PnlpsXNCnsnvNbCSg2AieOokfy_dyABME6cpnRVhx0vNVdBZ7yixnmFQrc0eKh2Hv0N4mQLOvBsXxJvzBo1NQDr2FcARqcMdHxzX99NekhYk429QBbP8442saqQYtxqHWz9cc__IlNGY7Lnf_Y9YSb8uoUPI_D1Rxn9mS8PoBKh8rCWMyrliOtp1UBTXdbv5cUuL8KlMwqpQCiuGWnkEAK9g0M85p3G2nNevlKKyyIzm3Jd47sa94uo9UOzjHXR6VUTkAtQdQw8Ra_m2RKWWn8f9rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f94115f3.mp4?token=I2sZcE46KtLXVbH8KUQsn8gx7cfuCGC7Gt2Xql4wOPBSYZkTKbtLXqRQJXG6UQPQe1G3myeHQRuSQcxJIzb2TRVoBGcQkKmgPDETRWB2kUWe3c01lgkliYx4WHlNrK4dof4L9rccAH3FL388Inn-MAouY_Ce2DObLpXYuzHQDUnChdwYRHcshjJMweRL6DVoxNLX4iJX5z379DawW9ynRgzR_pm6tCkmN4tCv6UjwULE7BbIzpqmG9Tg5-KOApby693h1odlMdQwOW4oRKFlSHXOV5ruAo9o4w7PpqSo-t96lZh1A3nypQNg3veaidhbNmurdmt82pQUTx1r4FtZ5lSxfKmpeU-lUb_4opC-oE6ZcB6hNq8y_hdw0GqIdXnOs33pm2tllB7BT7fc_PnlpsXNCnsnvNbCSg2AieOokfy_dyABME6cpnRVhx0vNVdBZ7yixnmFQrc0eKh2Hv0N4mQLOvBsXxJvzBo1NQDr2FcARqcMdHxzX99NekhYk429QBbP8442saqQYtxqHWz9cc__IlNGY7Lnf_Y9YSb8uoUPI_D1Rxn9mS8PoBKh8rCWMyrliOtp1UBTXdbv5cUuL8KlMwqpQCiuGWnkEAK9g0M85p3G2nNevlKKyyIzm3Jd47sa94uo9UOzjHXR6VUTkAtQdQw8Ra_m2RKWWn8f9rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با پشتوانه مردم می‌توانیم مقابل آمریکا و اسرائیل بایستیم؛ ما آینده خوبی داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/akhbarefori/653309" target="_blank">📅 23:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653308">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1xnmIcde9g3h73P9Zse3Ly-Y3zO0Q5RRuEbV7MWiSVva1KlSoU7HMQnN5Lxvde5SDVYGVE_SjckNPA-zNQh7h2hUbNPqdJMeOZHSZ116Q_dbHsWg5bPe41E9pdAONqQGt9MjRQmrXzUX7UcGevLWaxuXUAHkg4CYORyLKGOP-TUU-Qco5DuZBEFhC6I0ZgWiIolHHyjee69SJ-Cwg-JKS6IEd6AMPSMK2InMVEUaRTEPGNq28kfmIONyH0_zG6YpAwaP5yqBOWEuNrZt4Jgm9FePSiK_9itNarZSb8Q10ydhWwg7hOT3_TayDRco0LvuVb7PF1mCNcM5BjC68ikgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشنهاد تمدید خودکار قراردادهای اجاره‌خانه روی میز سران قوا
🔹
وزیر راه‌و‌شهرسازی: پیش‌نویس مصوبه‌ای شامل تعیین سقف برای افزایش اجاره‌خانه‌ها و تمدید خودکار قراردادها تهیه و به نشست سران ۳ قوه ارسال شده است که در صورت تصویب، بلافاصله ابلاغ و اجرایی خواهد شد.
🔹
تعیین نرخ دقیق در استان‌های مختلف برعهده شورای مسکن استان‌ها خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/653308" target="_blank">📅 23:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653307">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">قسمت بیست‌و‌سوم - پادکست کافئین</div>
  <div class="tg-doc-extra">بهرام چوبین</div>
</div>
<a href="https://t.me/akhbarefori/653307" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
بهرام چوبین؛ و پادشاهِ شکاک
🗓
وقتی در سازمان یک نیروی «ستاره» داریم، چگونه غرور کاذبِ مدیریتی می‌تواند حکمِ نابودیِ کسب‌وکار را امضا کند؟ و چرا برای یک نیرویِ متخصص، مهارت‌های سخت (Hard Skills) هرگز جایگزینِ سیاست‌ورزی و درکِ قواعدِ بازی نمی‌شود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/akhbarefori/653307" target="_blank">📅 22:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653306">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd95c8661.mp4?token=dXs55NQccUDUO95_Jrx86Fzxywyx4i7P74xkrb74omHN09iKU_lRsGUrbVpt_b651CdUCRcn7_XNtJoUF7qPViuVkyr7G8OE4-b8zjzt5CIXkW5MSD19JQnnvctVU0jykGomGZjVJ7zJr8OjVCCYNh2OlpJKthDBLuuxnAKIfNwQK6GD2NqiUoy-KRMMIGRUwmCim4kWYtOG5I7M9Ma1Rv2Bjv43-JtcfhefCENRzP5qRJaAFICoNofhEUqQ5uAjoah5zybYOHZQYwKridmkFOMGWkERvLwTgWWN4GueyggQkfK6LQmq_GFSfkfOyfpg7to5Y78mjgGlGLRbNuxejw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd95c8661.mp4?token=dXs55NQccUDUO95_Jrx86Fzxywyx4i7P74xkrb74omHN09iKU_lRsGUrbVpt_b651CdUCRcn7_XNtJoUF7qPViuVkyr7G8OE4-b8zjzt5CIXkW5MSD19JQnnvctVU0jykGomGZjVJ7zJr8OjVCCYNh2OlpJKthDBLuuxnAKIfNwQK6GD2NqiUoy-KRMMIGRUwmCim4kWYtOG5I7M9Ma1Rv2Bjv43-JtcfhefCENRzP5qRJaAFICoNofhEUqQ5uAjoah5zybYOHZQYwKridmkFOMGWkERvLwTgWWN4GueyggQkfK6LQmq_GFSfkfOyfpg7to5Y78mjgGlGLRbNuxejw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهرام چوبین و تراژدیِ مدیرانِ کوته‌فکر
#پادکست_کافئین
| قسمت سی‌ام
☕️
در این اپیزود به سراغِ سرداری رفتیم که تنها با ۱۲ هزار نفر، ماشین جنگیِ یک ارتشِ چند صد هزار نفری را در هم شکست، اما قربانیِ ناامنی، پارانویا و عقده‌های شخصیِ پادشاه خود، شد.
بهرام چوبین ثابت کرد که تحقیرِ یک نیروی نابغه، چگونه می‌تواند پایه‌های یک امپراتوری را ویران کند.
هر روز صبح با یک شات غلیظ از تاریخ آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtube.com/@caffeinepodcast2025?si=yIYlag9mUMtn0O8D
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/akhbarefori/653306" target="_blank">📅 22:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653305">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgIOfsouFE6Qtq72nFqxSXG3YdNGiJ9Ahy0F5y9N5M886qeqT1s970X5g9abtK64doqzzAfbDkp760Dbs15__3STkpLfjzzo2qgeY-2lHxwGonlHg6X9olUqs63d7C1kIr0iDOHLO77vGryag0AEeybLKeKfTBsV-vGNCM5CpTGr8OlbjIyGXmaZet4MLY8J-M6UDnzgLRDc6F0OPqaJWbjPNiclH99j4izT4QkmG3P00zEMpU9EigH6RnE2THGjDN8E4nI1r2db-KxWH8-strH2rZ0zQQNKN2D12Zu_yijp6KOdieXt2AXAyheQYrEeRrMGSai2HCdiT9OjnqG81g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مک‌گورک: سوال مهم این است که جهان چگونه می‌تواند با بسته‌ماندن طولانی تنگه هرمز سازگار شود
🔹
فرستاده پیشین آمریکا در امور خاورمیانه: درباره ایران، سوال کلیدی دیگر این نیست که این وضعیت چه زمانی پایان می‌یابد؟ بلکه این است که جهان چگونه می‌تواند خود را با بسته ماندن طولانی‌مدت تنگه هرمز تطبیق دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/akhbarefori/653305" target="_blank">📅 22:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653304">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6ed86ac2.mp4?token=qAo8VawF5fc_TSAA0I7R9GfJE9KYYoFery6Di-DIH889jrnQIzy89z3X-7qQ77PmYiTNFwlcERMc2n9WJRehv9OkbpdjRZHL1ngDmCYnMnXYAbVcFF_3hWmdqeoqZ1oFqYPozei8EioLWgLtLYeuV2R3nWd1P7II1nIzCQKVB0NNwDj3Swpi9KxVa3Qet89b-V_D5O33e7ZyXqxVQxR2zwenfia2FNMAY0TOJVUorP41tQYIQVa3mdusPAHpUSAqsPee9lYY5AbANLu_VhL1nJ4vWJd_NaQ_HjUvmddI-BpYdkMdwxNC8elUFG_RKwWbOq25ucJwOQs8-RSJjSC77w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6ed86ac2.mp4?token=qAo8VawF5fc_TSAA0I7R9GfJE9KYYoFery6Di-DIH889jrnQIzy89z3X-7qQ77PmYiTNFwlcERMc2n9WJRehv9OkbpdjRZHL1ngDmCYnMnXYAbVcFF_3hWmdqeoqZ1oFqYPozei8EioLWgLtLYeuV2R3nWd1P7II1nIzCQKVB0NNwDj3Swpi9KxVa3Qet89b-V_D5O33e7ZyXqxVQxR2zwenfia2FNMAY0TOJVUorP41tQYIQVa3mdusPAHpUSAqsPee9lYY5AbANLu_VhL1nJ4vWJd_NaQ_HjUvmddI-BpYdkMdwxNC8elUFG_RKwWbOq25ucJwOQs8-RSJjSC77w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زاکانی: پشت سرمان بمباران بود اما ما به آسفالت کردن خیابان ادامه می دادیم
🔹
آمریکا نباید احساس کند که می تواند کشور ما را به کشوری جنگ زده تبدیل کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/akhbarefori/653304" target="_blank">📅 22:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653303">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5H2tpZfzoeHHqaTORzTddr6-lxrf2g1ct2bCuFOO5QqBVVEVDDVLHvD4-_tJ8XcYZOnIMLlS4bAS-sHn_VZsE6ViE7xCKGSNik6zmBAXia_fAZpcQI-NPimOXg_U7QzHOSU5oDZKK5u7PWKIwZdD14JWKnYCXWVcWgXS_H-lirOGnyXdE-ZSlGAkyLiQbclTtycMTgan4G_yLemuVY2QN4Vqt6eUYYqr63Cbyk8jMRgYZmdMP9aq6Wk7a7WlNWkAebNFZq5NohC6FLOWtYP3QC_tOLmPUos0LVi7W9VlHn-SGQ8Nrd3XtukIB3G2pyL8zZVfvBVjr7ypPjEwWZHKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنس بدنه گوشی‌های آیفون تغییر می‌کند
🔹
اپل قصد دارد از نسل بعدی آیفون، تیتانیوم را برای جنس بدنه کنار بگذارد. منبع این تغییر، عملکرد ضعیف این فلز در مدیریت حرارت است که باعث داغ شدن بیش از حد دستگاه می‌شود.
🔹
در مقابل، نام فلز مایع (Liquid Metal) به عنوان جایگزین اصلی مطرح شده است. این آلیاژ که با ریخته‌گری دقیق تولید می‌شود، استحکام فوق‌العاده، مقاومت در برابر خوردگی و انعطاف‌پذیری بالایی دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/akhbarefori/653303" target="_blank">📅 22:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653302">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACzsjStI2mOh18Rt_i0TP0DEkZCOPaHETyAW2NXlnFMN2UgIaKWhG_qE7PgN58kibJHIOxuDIbn8D590ye7kmcfIW8bwUbNbAa1LNezNyhhJTzRaRsmhg0XTHJwKCj2Ejfb8i0fT4_c2R4tzz8ZEBKbmzTSsxxoAv5Z1Uoz_uw6-FpLiXpblJ6ztCSl4tRwpqSMzqKMbL7EhotMF2sb6wUzlflL1VT4lowSNvXPzs_7vN23qiLPgnnqkbq1YcYCqxCDhrs_wbHYuHX6EZnqb7Wve7Mpbfb0J6M68JvHIAMQdYsHaiXn_mmEZk8ljaAXpL_Bw2RrKUpTEvOtsGgJp3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قاآنی: پیروزی‌های ناوگان صمود ادامه دارد
🔹
دیوارهای تزویر آزادی های تمدن غرب را فروریخت و فاشیست صهیونیست را بیش از پیش رسوا ساخت.
🔹
فلسطین را باز به کانون توجه جهانیان بازگرداند.
🔹
رژیم صهیونسیتی مغلوب را که به تشدید سرکوب و جنایاتگری دست زده، سریع‌تر از قبل به نقطه پایان نزدیک کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/akhbarefori/653302" target="_blank">📅 22:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653301">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
واشنگتن تایید کرد؛ سقوط ۴۲ فروند هواپیمای نظامی آمریکا در ایران
گزارش جدید سرویس تحقیقات کنگره آمریکا:
🔹
از آغاز جنگ علیه ایران، دست‌کم ۴۲ فروند هواپیمای نظامی آمریکا از جمله جنگنده و پهپاد، منهدم یا آسیب دیده‌اند. بر اساس این مطالعه، برآورد هزینه وزارت جنگ آمریکا برای عملیات در ایران نیز به ۲۹ میلیارد دلار افزایش یافته است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/akhbarefori/653301" target="_blank">📅 22:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653300">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
فرماندار جیرفت از کاهش شدید سهمیه آزاد جایگاه‌های بنزین این شهر از ۲۵۰ به ۸۵ لیتر در روز خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/akhbarefori/653300" target="_blank">📅 22:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653299">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
معاون بنیاد شهید: حقوق فرزندان شهدا دوباره به حساب مادران واریز می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/akhbarefori/653299" target="_blank">📅 22:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653298">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دارو داریم، اما مریض نمی تواند بخرد!
همایون سامه‌یح نجف‌آبادی، رییس کمیته داروی کمیسیون بهداشت مجلس در
#گفتگو
با خبرفوری:
🔹
متاسفانه مشکلات دارویی کشور رو به افزایش است که دلایل مختلف خود را دارد.
🔹
قیمت داروی پلاویکس (مورد استفاده در سکته و جراحی قلب) طی ۲ تا ۳ سال از حدود ۷۰ تا ۸۰ هزار تومان به حدود یک میلیون و ۳۶۰ هزار تومان رسیده است.
🔹
داروی ایرانی این دارو با نام «اسویکس» در حال حاضر در دسترس نیست و فقط نمونه خارجی در داروخانه‌ها موجود است؛ به همین دلیل با وجود موجود بودن دارو، بسیاری از بیماران توان خرید آن را ندارند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/akhbarefori/653298" target="_blank">📅 22:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653296">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/758abff899.mp4?token=hwZ78iMtsIZVQVWzHkl2LV888yvE1S61Mo22aeNWBN2SClXRarbQeoOOJRl8VnQIumsgT1bC7f444enDgnbJwI9Fbre92PCIz06-KrUi1r0S1xsPt24J6RMQ8hFS_5FBrgzKLNNtbsRK1TZITxnil5VyaEYN3m5z4McDgkoE2kCLfwTePfLDua66afhnX4s8d21u6Xc42-uvlpLlMLYIHNSszLg3UDpPktDKI-ZX6bV7XZL83KZ7TfKPe6yfMYVTppcBnnaP4WmCVeAbay5uJb9KczH2j8-dF3w_8ztg3rnL0Q7UcjMl8F8lIdpfZszjND5PeRjRp-x6EH6rRJUX439XF7L1LgZq_IwGY2pzTx-U0ppwFJm2FOvMjqQKCzZ35H4hWYSOG-Z7yj74Ck7YWWS_kWxCx0oZAomNtdjiRy9AsWQMaDFvf7e2Chivqk0pSso1f9_OFDn-_gz8kdeTk7s3C35c-5GjWZPi2cYvxw-5_u9HrSGmWrHcbbfP6j-a13kRdHl9c2-1SlC_ZvxBHRW4BGU_lhUJ3CMkpcVnIlXLozTY6fr2JTJCAPFGrZeDCBPA57c7pDTakMqHX2k3xW1FTT3IrA9oeVTOs0Ndcet_M3KIWYDz8z72WEuQUFrvr95yznsrcp5q6mLsGzB39NrFR8YOERuffl9T5h927c8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/758abff899.mp4?token=hwZ78iMtsIZVQVWzHkl2LV888yvE1S61Mo22aeNWBN2SClXRarbQeoOOJRl8VnQIumsgT1bC7f444enDgnbJwI9Fbre92PCIz06-KrUi1r0S1xsPt24J6RMQ8hFS_5FBrgzKLNNtbsRK1TZITxnil5VyaEYN3m5z4McDgkoE2kCLfwTePfLDua66afhnX4s8d21u6Xc42-uvlpLlMLYIHNSszLg3UDpPktDKI-ZX6bV7XZL83KZ7TfKPe6yfMYVTppcBnnaP4WmCVeAbay5uJb9KczH2j8-dF3w_8ztg3rnL0Q7UcjMl8F8lIdpfZszjND5PeRjRp-x6EH6rRJUX439XF7L1LgZq_IwGY2pzTx-U0ppwFJm2FOvMjqQKCzZ35H4hWYSOG-Z7yj74Ck7YWWS_kWxCx0oZAomNtdjiRy9AsWQMaDFvf7e2Chivqk0pSso1f9_OFDn-_gz8kdeTk7s3C35c-5GjWZPi2cYvxw-5_u9HrSGmWrHcbbfP6j-a13kRdHl9c2-1SlC_ZvxBHRW4BGU_lhUJ3CMkpcVnIlXLozTY6fr2JTJCAPFGrZeDCBPA57c7pDTakMqHX2k3xW1FTT3IrA9oeVTOs0Ndcet_M3KIWYDz8z72WEuQUFrvr95yznsrcp5q6mLsGzB39NrFR8YOERuffl9T5h927c8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عقب نشینی‌های پی در پی پس از به پاکردن آتش جنگ بی‌محاسبه؛ این حکایت حال و روز رئیس‌جمهور آمریکاست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/akhbarefori/653296" target="_blank">📅 22:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653295">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سه پیشنهاد برای خروج آمریکا از بحران ایران
🔹
یک تحلیل راهبردی در نشریه The Hill اذعان کرده است که آمریکا پس از حمله به ایران، نه تنها به پیروزی نرسیده، بلکه تنگه هرمز را نیز از دست داده است.
در این تحلیل، سه اولویت برای توقف بحران ارائه شده:
🔹
ائتلاف بین‌المللی برای بازگشایی تنگه هرمز با مشارکت اروپا (قابلیت مین‌روبی) و چین (بزرگترین خریدار نفت ایران)
🔹
احیای کنترل تسلیحات و میز مذاکره با حضور آمریکا، ناتو، روسیه، چین و ایران
🔹
گسترش پیمان ابراهیم با پیشرفت ملموس در مسیر تشکیل کشور فلسطین و گنجاندن عربستان./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/akhbarefori/653295" target="_blank">📅 22:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653294">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2pwg3b55BpTC6pLc8NAK2kSKAoBUcoSBBijmiceWCmDpq7YfblhiKbnuXhOQ6DN9y5hcVR2azd0u_kMhEZmjYwQxBUt7a3LAEtky97DB1nbSWKhJMOmLb4-u8_bgQf_dXmNSI8AUu0I6rcI0av8jz-rCu3LPSEiVe-MyAj5QNZW1rfTWdaQ6sRtO2GmyokSC3gECzFenM23GogunOPUB9p0_1OiR437X3wK_n80HFEY4AHtgt_mafHAMaimrJlLFetq-gUuZB2Yzq1pOSfx-1egUVVoRKfqQ7sjATCt5RQGLmNA_mfr6cFZdkpQsv3udUIr3Gs5L5YWDwD6wQXjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزت زمانی؛ معاون سازمان تبلیغات اسلامی در نشست خبری پویش «جان ایران»: پس از انتشار پیام رهبر انقلاب، تاکنون بیش از ۷۴۵۰ گروه مردمی در لبیک به فرمان ایشان، حمایت خود را از پویش جان ایران اعلام کرده‌اند و این بیعت مردمی پس از جمع‌آوری امضاها تقدیم ایشان خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/akhbarefori/653294" target="_blank">📅 22:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653293">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9052bbd568.mp4?token=LK1ZYof7Cv85mSKBCoel8uYzklJLOVr36vvv5Y1_-CpZBsA0mBsDUPft1WTdWoYH81BK8iv9X-IcqQuqwcucI3EkPNcqQLE-J_IRAZ30y8K2PciBYyk1-fG5FPE1lFB_xmuxQL1jfh0n91XU3yG-yHPwfepYtms_-45ebaTc66tuSpFXarlyLcKKImLLOT0AOoIQkd15nUwvdJPktZPyWsG96pMe1I0L9afwABoSAeTsqt7eRv3rSoFxHerrCn94fItnoZjyE1y330sAPA83pFGedR9Kg1h3xwovuFtfuStiJEEDMojUT_b0Ifn2FEDla2e3PbJgmDAHhHZwLAKBBRHLPoLH04loUZF8gaGuS6xNq7rchWU4asRshx8rQ-pNZ04xmxWq1JKZ3wOKUkmrz-efMql5T-WFpx5xqr0R2p6ZZ50XOJ25xCv_w8NkTHDR7h2wc1gqHY7u9Jn09yMy5DLd2e3KC0gg2dpuTaonLcFln0qp1cm2sznqlvVJzI2twhHCGUDSVlCFmTXo0VCMzXG-O5Xd8W7rGlm6dcgit0DsniXIFKm7n8o8_Cw_kAUKXCbJWXnxSiCJ1nTAaBdX1i3EgNlj5sJ2LpPVXW2uKpRZ8HB3rbknpXmFSJ2rkSN0ZFGqZfU16FB3CWA2n3kK0hmP2L52XdHSl8sjnRTxPO0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9052bbd568.mp4?token=LK1ZYof7Cv85mSKBCoel8uYzklJLOVr36vvv5Y1_-CpZBsA0mBsDUPft1WTdWoYH81BK8iv9X-IcqQuqwcucI3EkPNcqQLE-J_IRAZ30y8K2PciBYyk1-fG5FPE1lFB_xmuxQL1jfh0n91XU3yG-yHPwfepYtms_-45ebaTc66tuSpFXarlyLcKKImLLOT0AOoIQkd15nUwvdJPktZPyWsG96pMe1I0L9afwABoSAeTsqt7eRv3rSoFxHerrCn94fItnoZjyE1y330sAPA83pFGedR9Kg1h3xwovuFtfuStiJEEDMojUT_b0Ifn2FEDla2e3PbJgmDAHhHZwLAKBBRHLPoLH04loUZF8gaGuS6xNq7rchWU4asRshx8rQ-pNZ04xmxWq1JKZ3wOKUkmrz-efMql5T-WFpx5xqr0R2p6ZZ50XOJ25xCv_w8NkTHDR7h2wc1gqHY7u9Jn09yMy5DLd2e3KC0gg2dpuTaonLcFln0qp1cm2sznqlvVJzI2twhHCGUDSVlCFmTXo0VCMzXG-O5Xd8W7rGlm6dcgit0DsniXIFKm7n8o8_Cw_kAUKXCbJWXnxSiCJ1nTAaBdX1i3EgNlj5sJ2LpPVXW2uKpRZ8HB3rbknpXmFSJ2rkSN0ZFGqZfU16FB3CWA2n3kK0hmP2L52XdHSl8sjnRTxPO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت شیرینِ مادری که ۶ فرزند دارد
از سختی ها و خوشی های مادر بودن در برنامه «جان ایران» شبکه سه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/akhbarefori/653293" target="_blank">📅 22:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653291">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 52</div>
</div>
<a href="https://t.me/akhbarefori/653291" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه پنجاه‌ودوم
رائفی‌پور:
🔹
0:07:20 تفسیر ۷ نام جهنم در قرآن
🔹
0:19:00 تفاوت عذاب گناهکاران در کتاب تورات و زردتشت و اسلام
🔹
0:41:20 ویژه بودن اسامی اهل بیت در حروف ابجد
🔹
1:05:30  تفسیر ۱۱ بخش خطبه غدیر از ابتدا تا ظهور
🔹
1:46:30 بیعت با حضرت علی (ع) ۳ روز به طول انجامید
🔹
2:07:00 چرا یهودیان در قرآن لعن شده اند
🔹
2:14:00 خداوند حامی دشمنان صهیونیست هاست
#دعای_ندبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/akhbarefori/653291" target="_blank">📅 22:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653290">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
تروریست‌های سنتکام در اطلاعیه‌‌ای مدعیِ تعرض به «یک نفتکش مرتبط با ایران» شدند/ نفتکش بدون آسیب همچنان درحال حرکت است
🔹
سنتکام در اطلاعیه‌‌ای، مدعی شد مسلحینِ این گروهک تروریستی ساعاتی پیش، وارد یک نفتکش حامل پرچم ایران شده و پس از «بررسی»، از آن خارج شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/akhbarefori/653290" target="_blank">📅 22:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653289">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
اکسیوس: قطر پیش‌نویس توافق جدیدی برای کاهش تنش‌ها میان تهران و واشنگتن ارائه کرده است
🔹
هیئت دیپلماتیک ویژه‌ای از سوی قطر در اوایل هفته جاری برای پیگیری این پیش‌نویس به تهران سفر کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/akhbarefori/653289" target="_blank">📅 22:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653288">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d5bde06c.mp4?token=VBbdVhyQl6IFKRH0fzRENG4NWqR_ttjFgCIp0Av3zS7M26yjyli7kw9SslzIrYHFRjQcgvDR6g87niJVkA6aNzVi4dw3_PsY1QUoLNcmrwXJU-LHqXipLl8R2CmOKKHYYaOFpThD0Cu6quUOvEIhtmSLMpE08LKsns0t_heLkqMY_r0FtP18EbqkMYmXSjY4mlaj20WvQOpx8sQbqkUYZsxy-JqpKTu6iznUrQRcbMygWgcFguUsIgFm_XmBEUTsR5uHaFb_hm69hx8e3l96LIiuJAsQG55SzDv9eaCYB62I46UzgNU30BaM-AMoJb7uTh7-9DgJdK2Ko1YvTTFsLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d5bde06c.mp4?token=VBbdVhyQl6IFKRH0fzRENG4NWqR_ttjFgCIp0Av3zS7M26yjyli7kw9SslzIrYHFRjQcgvDR6g87niJVkA6aNzVi4dw3_PsY1QUoLNcmrwXJU-LHqXipLl8R2CmOKKHYYaOFpThD0Cu6quUOvEIhtmSLMpE08LKsns0t_heLkqMY_r0FtP18EbqkMYmXSjY4mlaj20WvQOpx8sQbqkUYZsxy-JqpKTu6iznUrQRcbMygWgcFguUsIgFm_XmBEUTsR5uHaFb_hm69hx8e3l96LIiuJAsQG55SzDv9eaCYB62I46UzgNU30BaM-AMoJb7uTh7-9DgJdK2Ko1YvTTFsLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عدد واقعی جمعیت ایران چقدر است؟
🔹
تازه‌ترین داده درباره جمعیت ایران منتشر شد، نکته حائز اهمیت تعداد افرادی است که در سن ازدواج قرار دارند. از دیدن دو عدد در این بسته تعجب خواهید کرد!
@Tv_Fori</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/akhbarefori/653288" target="_blank">📅 21:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653287">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eao8ME2m2Uz60ngKrAKaZGPXuGzmrxDwvZnkpXlBX4UJ5JhxHbtKfPDtcclqudZJYcUq-DTpS0ZtIC5ZQ262UwfyAJD9IApmpqEzsVMA3oHSixrl3eftVCDBEXlkVtRL1h1MbSc_-44UjfHc94UuIBk5L9rGTuJnUyzb8GJiQwxSabWIOev6QNjjSyoB14yZoxc9HppmvGbkFzwtMc9vewdR-eWOCrzrkvhfvNu0JWH2b3RFNU0Oriv7iBxHAPiukSLKPkCVN6FQfr0lMBxS-oZBvGaGFoXFr5rem-ZJBisE7BFexW4djaZxPc9YlGIlXQOs9xZv77CP2jn7n-vwSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استقبال متفاوت پکن از ترامپ و پوتین | پنج نشانه روشن از دو نوع رابطه | از صرف چای تا موسیقی پیشواز
🔹
چند روز پس از سفر دونالد ترامپ، رئیس‌جمهور آمریکا، به پکن، این بار ولادیمیر پوتین، رئیس‌جمهور روسیه، وارد چین شد و با شی جین‌پینگ دیدار کرد.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3216539</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/akhbarefori/653287" target="_blank">📅 21:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653286">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66d570f341.mp4?token=srdhxH44Z0RGRWjLMLCaAoXCckMp6cBxjMjK4KvamRe-4nvFND4VyNcEnUWqHM1TbG1HfI8UKsZ8qIlNRm6fUkTq2cxhZNcmxW7-qc7OdnW_sxtkOr0_YdTNNlrFnq-N802XOi3wxMoxdGftzYelMgaLf1yQa9TR9dk9XriB5KTiy4EKkfh-jhsj_J0_XXTd142qBCkv_s1rcwccahFAI1uJJinQdHRm3v2CtubmxTT8A-sjjrUF86aN_WEofKgCfoxqG49x41f_ubIuODyA3dSecqGZxwza8DrxIRb2ZqgS7s6w2UVKfThK1hEn79WhKyPPzFmwLyljqgwkC3ut9rkrbrQlFD_akVSvJOQ3cgMZ2N2bSiuesHc2EvJ4pcz-QyVL3jAPIvIcZq9RRUq1fpqhDzzwAp6rs0Prr70v-mRCLMkq8Hf2T_wcWXTY3Qc1NStAEEjCCY5So3fxFvrgJ3G5gJiHsJV3SLq2vKU7jS82X-cMLGx23DkXh1bsA4kFlN3w1ZLfWTO_waaz-zV-hEzqVyKNnPd3eYFALMyP9d5DtSMCxYTcW8o7swxEbjT5_C2SsDvn1yrIO7jnOAOveEwbJoJLZeNwccBl1_ffKcyZf6Sx5D-Az-HWfJralqiNJooiw5LAXKelbOhhzySR87uHtzF4P2X62LofsxpaPq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66d570f341.mp4?token=srdhxH44Z0RGRWjLMLCaAoXCckMp6cBxjMjK4KvamRe-4nvFND4VyNcEnUWqHM1TbG1HfI8UKsZ8qIlNRm6fUkTq2cxhZNcmxW7-qc7OdnW_sxtkOr0_YdTNNlrFnq-N802XOi3wxMoxdGftzYelMgaLf1yQa9TR9dk9XriB5KTiy4EKkfh-jhsj_J0_XXTd142qBCkv_s1rcwccahFAI1uJJinQdHRm3v2CtubmxTT8A-sjjrUF86aN_WEofKgCfoxqG49x41f_ubIuODyA3dSecqGZxwza8DrxIRb2ZqgS7s6w2UVKfThK1hEn79WhKyPPzFmwLyljqgwkC3ut9rkrbrQlFD_akVSvJOQ3cgMZ2N2bSiuesHc2EvJ4pcz-QyVL3jAPIvIcZq9RRUq1fpqhDzzwAp6rs0Prr70v-mRCLMkq8Hf2T_wcWXTY3Qc1NStAEEjCCY5So3fxFvrgJ3G5gJiHsJV3SLq2vKU7jS82X-cMLGx23DkXh1bsA4kFlN3w1ZLfWTO_waaz-zV-hEzqVyKNnPd3eYFALMyP9d5DtSMCxYTcW8o7swxEbjT5_C2SsDvn1yrIO7jnOAOveEwbJoJLZeNwccBl1_ffKcyZf6Sx5D-Az-HWfJralqiNJooiw5LAXKelbOhhzySR87uHtzF4P2X62LofsxpaPq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گفت‌وگوی تلفنی رهبر شهید انقلاب حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه با همسر شهید رئیسی، پس از حادثه سقوط بالگرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/akhbarefori/653286" target="_blank">📅 21:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653285">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05e0804ab.mp4?token=Mk4SKdzma1-j6n7qFDPAClhqKuVIBkjIvoNkkViW5Onr6YHOJEYoF_OauPX7yEpoIOC0jwk8MuaZBaqMEHq_MgtCdyZBOnUfPfNfsE6i10bw6RtnzhHhNbhIAlryEoLb34_Lz_tbcNrJ7qx_-MLrx2Trppa1076vILch5hF02KOEdk9n53QOqZYSzOhufV7ZY3qdHH3yTQrR33dfouQywrJxnaoBrsxsENBlNsovXi6i2EgY56_DISz6OsHm6IZh1UfArwDNx7M84DdU1WIP6VSjvtCq6ipaE31yApQbNJlkhIfWc4uPVZJHFvo2OpEBB0trfL6krhvEkPWkBUyuTQENavylVoXSPeS76HPGNMRSRZ7EIubwF7JWUBfIoMIZI_jPn_6wXcHoO1v0kz8qKVt_94P9qbG7Xod-qN5eCDDBJ6n53uqdNsI-ChciWyzkAnHmWH0kCQRxD5vZq-HVVO5pmZP_pLma96YdbA1ZCSePRpBlabLmBoYxHy9GePE3tg_tzUGgJC0_FxD0VY_7oydalT3UqQISXhirc-7F18-V6Q0fu_F4nI7xB4TS1kr9lHi6Baw_zCgkbHU7eF7vEyi1EjZGiaHPw-NFcGbsMuRl4Cycj9kglylD-depEV-JViGvI8QJWneggEhv6KegLj_BJ4vI5Xln3Sz7z_xY2q0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05e0804ab.mp4?token=Mk4SKdzma1-j6n7qFDPAClhqKuVIBkjIvoNkkViW5Onr6YHOJEYoF_OauPX7yEpoIOC0jwk8MuaZBaqMEHq_MgtCdyZBOnUfPfNfsE6i10bw6RtnzhHhNbhIAlryEoLb34_Lz_tbcNrJ7qx_-MLrx2Trppa1076vILch5hF02KOEdk9n53QOqZYSzOhufV7ZY3qdHH3yTQrR33dfouQywrJxnaoBrsxsENBlNsovXi6i2EgY56_DISz6OsHm6IZh1UfArwDNx7M84DdU1WIP6VSjvtCq6ipaE31yApQbNJlkhIfWc4uPVZJHFvo2OpEBB0trfL6krhvEkPWkBUyuTQENavylVoXSPeS76HPGNMRSRZ7EIubwF7JWUBfIoMIZI_jPn_6wXcHoO1v0kz8qKVt_94P9qbG7Xod-qN5eCDDBJ6n53uqdNsI-ChciWyzkAnHmWH0kCQRxD5vZq-HVVO5pmZP_pLma96YdbA1ZCSePRpBlabLmBoYxHy9GePE3tg_tzUGgJC0_FxD0VY_7oydalT3UqQISXhirc-7F18-V6Q0fu_F4nI7xB4TS1kr9lHi6Baw_zCgkbHU7eF7vEyi1EjZGiaHPw-NFcGbsMuRl4Cycj9kglylD-depEV-JViGvI8QJWneggEhv6KegLj_BJ4vI5Xln3Sz7z_xY2q0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه‌ای که این خبر را شنیدم...
🔹
در سالروز شهادت شهید رئیسی، صدای مخاطبان خبرفوری را می‌شنویم؛ روایت‌هایی از لحظه‌ای که خبر شهادت شهید راه خدمت آیت‌الله رئیسی منتشر شد و قلب میلیون‌ها ایرانی را متاثر کرد.
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/653285" target="_blank">📅 21:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653284">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
شکار دو تانک مرکاوا توسط حزب‌الله
🔹
حزب‌الله: دو تانک مرکاوا در شهر حداثا در دو عملیات مورد اصابت قطعی قرارگرفت؛ همچنین حملات موشکی به تجمعات پشتیبانی دشمن انجام شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/653284" target="_blank">📅 21:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653283">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
جنگ با ایران ۳۰۰ دلار از جیب هر آمریکایی کم کرد
🔹
از زمان شروع جنگ ایران، قیمت بنزین در آمریکا به میانگین ۴.۵۰ دلار در هر گالن رسیده و مصرف‌کنندگان تنها در ۱۰ هفته گذشته، ۴۲ میلیارد دلار اضافی برای بنزین و گازوئیل پرداخت کرده‌اند.
🔹
به طور متوسط، هر خانواده آمریکایی بیش از ۳۰۰ دلار بیشتر از حالت عادی برای سوخت هزینه کرده است.
🔹
این پژوهش توسط «آزمایشگاه راه‌حل‌های اقلیمی» و «پروژه هزینه‌های جنگ» دانشگاه براون انجام شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/akhbarefori/653283" target="_blank">📅 21:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653281">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63ea7c9e7.mp4?token=ofBDi_FQ-2K7x9RyMyVSnaqKxnKKQU3rl-esyZ5U3UoLs58enApkSqBXLTut-eCNJY85QIIuF4iuvHdIeUk_ce7sLXw5PEt3V5aKAzf1pGkvYoiyIkT1Uy2b6Ei-cI-xq7w2iHve8-JibBxh3otTzCXRrfG3vZE-FHMhMysd8E9A5I08o93cQ72it4HWtFoc7cGaxcq7kx-c3TI2IbRKoK7fhMx_hDRFe5Id6MolZSrcvBuJnROz10p_RyKamNjMXIbP3Kl_QZqMKhVR_YEHrI_c92TYJGjBiOXKAuWiR0eKV7zae6rF0_oVFfVwyIJfZSMpo5pglbrIkxKRz6OzqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63ea7c9e7.mp4?token=ofBDi_FQ-2K7x9RyMyVSnaqKxnKKQU3rl-esyZ5U3UoLs58enApkSqBXLTut-eCNJY85QIIuF4iuvHdIeUk_ce7sLXw5PEt3V5aKAzf1pGkvYoiyIkT1Uy2b6Ei-cI-xq7w2iHve8-JibBxh3otTzCXRrfG3vZE-FHMhMysd8E9A5I08o93cQ72it4HWtFoc7cGaxcq7kx-c3TI2IbRKoK7fhMx_hDRFe5Id6MolZSrcvBuJnROz10p_RyKamNjMXIbP3Kl_QZqMKhVR_YEHrI_c92TYJGjBiOXKAuWiR0eKV7zae6rF0_oVFfVwyIJfZSMpo5pglbrIkxKRz6OzqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفتار وحشیانه با کاروان صمود، برای رژیم صهیونیستی دردسرساز شد
🔹
سفرای رژیم در جهان یکی پس از دیگری احضار می‌شوند
🔹
بعد از بازداشت کاروان صمود توسط نظامیان رژیم صهیونیستی و برخورد‌های زننده و انتشار تصاویر آن در رسانه‌های جهان، بار دیگر جنایات وحشیانه رژیم تیتر یک رسانه‌های دنیا شد.
🔹
همزمان با این تحولات، دولت‌های دنیا مخصوصا کشورهای غربی، یکی پس از دیگری سفرای رژیم صهیونیستی را احضار و بابت این رفتار خشن بازخواست می‌کنند.
🔹
تا کنون ایتالیا، کانادا، فرانسه و هلند سفیر اسرائیل را در کشورهای خود به دلیل رفتار غیرقابل قبول با فعالان بازداشت شده کاروان ناوگان جهانی صمود احضار کرده‌اند و با توجه به فشار افکار عمومی، پیش‌بینی می‌شود دولت‌های بیشتری، دست به این اقدام بزنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/akhbarefori/653281" target="_blank">📅 21:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653279">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573359b1bc.mp4?token=N85IgcYG_VHYaufh-m3qeM5-IFb8KqO_cAZTSdT0Jt7YQGoLC0JMygeXUSx5Qg94vK8x6nJUQmNJNjvm0DFy9B3gibrImM0Z4gBcbsM6gc7dLOcVSLBhrl8oP2IE41ykhZQ4eXTR1f5ij--D_0EM9LjesEPeYHW1aTgtS8HFxW-N1Z5J6bB__1sV9uDxRgbMeYY-lCS5HHWZNagRF4HXjwTsAE4H1FUFq8gmrv3Xve0WIIyWMmSmMSffjTRUX6fEbFTyhie8eA6g74iwhXUH6SwNUH_UatFZ06FwlEooJn-RBGpj91ub9C8uleQ7jBlvnS9cNhMlB4y4_e06BTHmvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573359b1bc.mp4?token=N85IgcYG_VHYaufh-m3qeM5-IFb8KqO_cAZTSdT0Jt7YQGoLC0JMygeXUSx5Qg94vK8x6nJUQmNJNjvm0DFy9B3gibrImM0Z4gBcbsM6gc7dLOcVSLBhrl8oP2IE41ykhZQ4eXTR1f5ij--D_0EM9LjesEPeYHW1aTgtS8HFxW-N1Z5J6bB__1sV9uDxRgbMeYY-lCS5HHWZNagRF4HXjwTsAE4H1FUFq8gmrv3Xve0WIIyWMmSmMSffjTRUX6fEbFTyhie8eA6g74iwhXUH6SwNUH_UatFZ06FwlEooJn-RBGpj91ub9C8uleQ7jBlvnS9cNhMlB4y4_e06BTHmvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر نیرو: معادل مصرف چند کشور کسری برق داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/akhbarefori/653279" target="_blank">📅 21:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653278">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avKVuLsd0xAn-gAAXcF2UYqVzMgoalXUGwdmNyoI7bDKKLAtk5PKnVw3wgLSgtWdse-Jfni85655sUpZQWbBeYzNM2YXNUCmJ8NxvNVHoFbfy5TJorMaSqufqIavVcSDChQQZNcSlX-2wbd_2TegCLuVvBZJ2Ash_O7qJHlLGYylX-lKEPcmTRFMo-9vENRpO1yF_M9sSe7W_3jEpv5LYTUKfr0i6OT1saAkSgInPrsWK_3ikxQwLWJWRNeQluCwamiuafIkGFJ4ixJmpwFQffPm-8bUyI9w-sFQ5Wsi_n1-kIr-RVx80CtfLXvpC1YmUbnu3sii3vMvKL5zvqlYPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عواقب جنگ با ایران و کمبود کود شیمیایی، اروپا را مجبور به استفاده از «کود گاوی» می‌کند
🔹
گزارش پولیتیکو نشان می‌دهد که اتحادیه اروپا قصد دارد برای مواجهه با کمبود قریب‌الوقوع کود شیمیایی، به کود دامی روی بیاورد.
🔹
جنگ آمریکا و اسرائیل علیه ایران باعث اختلال در کشتیرانی از طریق تنگه هرمز شده که حدود یک‌سوم کود شیمیایی جهان را تأمین می‌کرد.
🔹
اما برخی مقامات اتحادیه اروپا هشدار داده‌اند که اتکای بلندمدت به فضولات گاو کافی نخواهد بود. هربرت دورفمن می‌گوید: «کود دامی می‌تواند یک کمک باشد، اما هرگز نمی‌تواند جایگزین کودهای بر پایه اوره و نیتروژن شود.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/akhbarefori/653278" target="_blank">📅 21:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653277">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqbpG4eOSbyZxpOBiipJ0_K25yrUmjbFFZtYNRLFwtAgsdVxJJ8EOh0LZDdVVEw104if0ztOJQpw5ovOKr7SEltm9POgXrfcRy6PVo3QxFYiIZhcHv0cU0oA5LtnU1UcDTxzrRToAwpzbg07Kxu0pTTLcifdIIRHQrLo4hAttS87bTeVhyhnkCtqewaRZWzuTgGtU42i9w5fVWt4ukrb_5C_HnFv9A2mMwH7HloBSDttEz_JbKEDqHffT99E7_SeTli9Id8EzvFHpqzk9iIbMZRAXBotC7uGEZlD8CUYQaC34kgC2PrF2qEKk3pf-UlSVhaBa6U4nw7sqDDgQXsRIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سهم گروه‌های کالایی مختلف از میزان ترانزیت از تنگه هرمز
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/akhbarefori/653277" target="_blank">📅 21:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653276">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ادعای آکسیوس از گفت‌وگوی پرتنش ترامپ و نتانیاهو درباره ایران
🔹
پایگاه خبری آکسیوس به نقل از منابع آگاه از تماس تلفنی «دشوار و پرتنش» میان دونالد ترامپ و بنیامین نتانیاهو درباره تلاش تازه برای دستیابی به توافق با ایران خبر داد.
🔹
دو طرف در این تماس درباره ابتکار جدید برای رسیدن به توافق با تهران گفت‌وگو کردند که به گفته منابع، فضای آن «سخت و چالش‌برانگیز» بوده است.
🔹
یک منبع اعلام کرد نتانیاهو پس از پایان تماس، در وضعیت خشم قرار داشت.
🔹
به گفته یک مقام آمریکایی، ترامپ به نتانیاهو اطلاع داده میانجی‌ها در حال تدوین سندی هستند که واشنگتن و تهران برای پایان دادن به جنگ آن را امضا خواهند کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/akhbarefori/653276" target="_blank">📅 21:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653273">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8zTehZGabJH68yqMli8T2GsxhPOcKqnuMBxFT_Uql6A3TVnMS1FM-sy2vBrBObBi8NR11s3dUM-Kxf7t9BQ3XfxgFuQ-86OHfNYwehOCl1yLBPHZhxexOfO2Fwya7JYctsXPHxPjSAgm_kpVC3h0bVK0VWzGyYn8c10IsEm-aAM0Ew41P-B_3IodefNIjb8-d9uhnRe86mW6tooGx22qycMmeLt3_JWjSvcaJZCEFXHCFIqYe6iFs4darVhDhykLHgUalbhUJfN2CDvQv3VmLcnpnoMSn3KxUyKv8ecuUCXzqONKFe8l6IS_D1NYBilbjTvzUGxMkifPwMqm0HthQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه پاکستانی: عاصم منیر فردا به تهران می‌رود/ احتمالا خبر مهمی در راه است
روزنامه ابزرور پاکستان:
🔹
فیلد مارشال سید عاصم منیر، رئیس ستاد ارتش، به عنوان چهره‌ای کلیدی در روند دیپلماتیک ایران و آمریکا، فردا به ایران می‌رود. در طول این سفر احتمالی، انتظار می‌رود اعلامیه‌ای مبنی بر تأیید تکمیل پیش‌نویس نهایی توافق منتشر شود.
🔹
این سفر می‌تواند به عنوان یک نقطه عطف دیپلماتیک سطح بالا باشد، جایی که تکمیل نسخه نهایی توافق ممکن است رسماً اعلام شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/akhbarefori/653273" target="_blank">📅 21:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653272">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
امارات وقف آمریکا شد!
🔹
آمریکا نقشه‌ای مرموزانه کشیده، جریان خارج شدن امارات از اوپک را حتما شنیده‌اید. پشت این اتفاق اما نقشه‌ای کاملا حساب شده است.
🔹
شاید جنگ با ایران هم برای همین نقشه اتفاق افتاد!
🔹
ماجرا چیست؟ در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/akhbarefori/653272" target="_blank">📅 21:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653271">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOFeOH2meMMHqtg7QlinhEHiI0AwIhSEY0IfslJzlo_AAuNXyqMYuwniq4BsHA40xBFMVLeFXS8B1EqOIOaONCGt-T0UowwKefeA3D5bH-qjikn4Fq2yKnGsrxp201tUxV6iZMKumRkiE37rpib-KmFsmUqla5Le8_4Z35EiGfwTexbHg2KWod3vXstY7A1drjOb2CfebSj_74Za9WjHpo8MJ90_TT93BpdPRYxOA4bEsv1xYZvls3ExXyOsoKbq0VGp9jDGnUFdO3tqxarW4-8-gMJWD10xZa_70wgLABSIxLCF_2DLLgMZ8Yu9cvZKb7wLxJN9zj6M6BfsKFEN2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی در پاسخ به ترامپ: ایران شگفتی‌های زیادی برای آمریکا دارد؛ برای هر سناریو آماده هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/akhbarefori/653271" target="_blank">📅 20:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653270">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWSa7u7XyLPRQaTou_XJBf56AiSq0P3YF9oS1anIHxc-gu7pSqVvZ66ZtLAvQXE2AZGROgYftFKV2zToUu_ajYTpao22PRkLLShJW-r1uCMcCfsqkZQpGrdoWb5s3ip9jgmSDJzsKc0vsKBo8q3abgJs3Vvo2HY3tJd7DUVSMjlbaOUW6lBs3P5CEp_1amItcFT36B5CS5IPB_JyHbzXRZb755nOdQf7ZV05IVx8EV1pP-4KICjkWY8T-MHny-HYpNQwpo6TvU_-qXzgaJFRpTinYt3VsXMw9nx3gJfcZZSXXrEiqE3OUoqGSZ__brisgBsIm6e8rHS9Gm6TntzrXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبیعت روی تخت بیمارستان افتاده
🔹
هر تکه پلاستیکی که بیرون می‌آوریم، یک نفس تازه به زمین برمی‌گردانیم.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/akhbarefori/653270" target="_blank">📅 20:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653269">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: در این مرحله متمرکز هستیم بر خاتمه جنگ در همه جبهه‌ها، از جمله لبنان
🔹
مطالبات ما مشخص است؛ موضوع مرتبط با آزادسازی اموال بلوکه‌شده ایران، مباحث مرتبط با راهزنی دریایی و اقدامات ایذایی که علیه کشتیرانی جمهوری اسلامی ایران انجام می‌دهند، این‌ها مواردی است که خیلی روشن از ابتدا بیان شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/akhbarefori/653269" target="_blank">📅 20:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653268">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4nGaDCPJ2WjW2g7ZpMYthxrMaUZMUkVF11n_pL4UMCMLcAneCBvpI2bv5MPBMYJtwyEUt-kpQBPnz5Ze2Lag0mae8EM7vsjQj2IMa-wacmTbuteRNobCY9mT_9wZad2Y1FL0s3F0EeeB9CnIA0Alh5uZx0Eu4j-39tlQihXmafHrv6t0P54FNUIsqtlS3vQBCeQus_pcfWmXFfpzTk-aDNc4vrvGdxAWs0L7XqphRPVFsaG4EXWmoZQOFbwZ0OI8faFr2WORFB7WiNexm2qr33JzOWrAqPWwIgh38-sk6P2fQsg00CXu5Shql2k36vbDLsxRyfmW_P2J1gGr2MiAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در ادامه موضوع ارتباط شرکت فیلیپس با اسرائیل و جاسوسی این برند صهیونیستی
🔹
بخش دیگری از این مقاله قابل توجه است:
🔹
«شرکتی مانند فیلیپس علاوه بر این در سراسر جهان فعال است، ویجور (افسر اطلاعاتی هلندی) اضافه می‌کند:
🔹
«نه تنها در هلند، بلکه همچنین در کشورهایی مانند عربستان سعودی، لبنان و امارات متحده عربی. این موضوع به شدت برای سرویس‌های اطلاعاتی اسرائیل مهم و مرتبط است. همچنین به این دلیل که بسیاری از فلسطینیان بلندپایه و صاحب‌مقام به این کشورها پناه می‌برند تا درمان‌های پزشکی‌ای را دریافت کنند که در غزه و کرانه باختری امکان انجام آن‌ها وجود ندارد.»
🔹
حالا جالب اینکه؛ نمایندگی ایران فیلیپس در سال ۲۰۲۳ عنوان best seller یا همون بهترین فروشنده در حوزه تجهیزات پزشکی (همان سی‌تی‌اسکن و ام‌آرآی و آنژیوگرافی و...) را کسب کرده! در نظر بگیرید که چقدر دستگاه در ایران فروخته و کار گذاشته شده است!
🔹
حضور مأموران سابق اطلاعاتی اسرائیل در توسعه نرم‌افزارهای داده‌های حساس پزشکی شرکت فیلیپس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/akhbarefori/653268" target="_blank">📅 20:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653267">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe81d225d0.mp4?token=CHpiZv8LNiugEB2sAP9D1cwAyxF773qKT-UQ0KZVaGWJYONKRSiuLEHhZh4c1Z1tk-IFUQbDFcwYxWMJF8JcCJmBGhaXVd_E7S1X0EgmP05rRlXLGHvflDxjzMKM0xCLr7JBh6c0BcvhJKzC4x-ynBJE8XmTPIxftPM7hSI8fiBLohVwu5PwPZzico-XYUG4FlItOsP8Yj9HKpOcWTzcyJD0YOibukZ6hNKivl9QKFFGQhVBrVVPnq6_Da2C9BbLjSFkwWEbtuuEL1EnEBqBQ3XfdF331KLF9dGvzMgOUpvSmtc-Z9CBSjnnVh1OdRdv9JDrwfv20TSXTxQI2R2jIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe81d225d0.mp4?token=CHpiZv8LNiugEB2sAP9D1cwAyxF773qKT-UQ0KZVaGWJYONKRSiuLEHhZh4c1Z1tk-IFUQbDFcwYxWMJF8JcCJmBGhaXVd_E7S1X0EgmP05rRlXLGHvflDxjzMKM0xCLr7JBh6c0BcvhJKzC4x-ynBJE8XmTPIxftPM7hSI8fiBLohVwu5PwPZzico-XYUG4FlItOsP8Yj9HKpOcWTzcyJD0YOibukZ6hNKivl9QKFFGQhVBrVVPnq6_Da2C9BbLjSFkwWEbtuuEL1EnEBqBQ3XfdF331KLF9dGvzMgOUpvSmtc-Z9CBSjnnVh1OdRdv9JDrwfv20TSXTxQI2R2jIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: آمریکا با «راهزنی دریایی» زنجیره تأمین انرژی جهان را مختل کرده است
🔹
سخنگوی وزارت امور خارجه با محکوم کردن اقدامات اخیر واشنگتن، آن‌ها را نقض صریح حقوق بین‌الملل و عامل اصلی ناامنی در آب‌های آزاد دانست.
🔹
اقدامات غیرقانونی آمریکا نه تنها در منطقه خلیج فارس و تنگه هرمز تنش‌زا بوده، بلکه موجب اخلال در زنجیره تأمین انرژی و سوخت در اقصی نقاط جهان شده است.
🔹
جامعه جهانی باید واشنگتن را برای پایان دادن به «راهزنی دریایی» و رفتارهای خلاف عرف بین‌الملل تحت فشار بگذارد.
🔹
این موضوع به عنوان یکی از محورهای اصلی در تمامی تبادل پیام‌ها و گفتگوهای اخیر، از سوی جمهوری اسلامی ایران به طور جدی پیگیری می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/akhbarefori/653267" target="_blank">📅 20:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653266">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
حنظله: در صورت خطای دشمنان به شبکه‌های دیجیتال و انرژی آنها حمله می‌کنیم
🔹
گروه هکری حنظله: در صورت ارتکاب هرگونه تجاوز یا بی‌مبالاتی از سوی آمریکا و رژیم صهیونیستی، حملات سایبری ویرانگر فراملیتی علیه زیرساخت‌های انرژی و دیجیتال کشورهای خصم اجرا خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/653266" target="_blank">📅 20:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653265">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: نسبت به موضوع حاکمیت ایران بر تنگه هرمز تاکید داریم
🔹
قاعدتا هزینه تامین امنیت دریانوردی تنگه هرمز نیز باید پرداخت شود.
🔹
طبق حقوق بین‌الملل مجاز هستیم که تنگه هرمز را برای کشورهایی که آن‌ها را برای خود تهدید می‌دانیم باز نکنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/akhbarefori/653265" target="_blank">📅 20:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653264">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsLm7y7c3dgn7ars835oRWU-hyVkRSu-v7uEq20gM-DflODZWtAcXuLYKtEDaB_ewQYU6YnkUn9RRsOMof7JVmH61yswF-v3AmfGk5Xo3O2qE49nTZ9gicKC_y4osd3V51pUXskvRv3hk1az5CQPRJZDIzm1Rec_YRb15OjnZhNGPkfSVFv8-vM0n1IubGabrl8Wqim7U9cR11KAr_OfTsZk8Dc5ZVlEHRUmZQXzLpd3BR8lzYWQbR5ikOBg06S-AbFFxH3t5NimQEVTYeizk8MLJyfFb0IoeqU8ucSql-cvqMuNaMl7v_pOWiMBZKG-GMhzRk307ElkkIa-03iXVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گره بگشایید
🔹
رهبر انقلاب اسلامی به مناسبت دومین سالگرد شهادت شهید رئیسی و بزرگداشت شهدای خدمت پیامی اعلام نمودند. ایشان فرمودند: امروز شکر نعمت انسجام ملت و دولت و تمامی دستگاه‌های جمهوری اسلامی، در تقویت انگیزه و خدمت مضاعف و مجاهدانه‌ی مسئولان، گره‌گشایی از مسائل و دغدغه‌های مردم خصوصاً در عرصه اقتصادی و معیشتی، حضورهای میدانی و مستقیم، و تعریف نقش جدّی برای مردم بعثت‌یافته در مسیر پیشرفت کشور و حرکت امیدوارانه به‌سوی آینده‌ی روشن است.
🔹
هفتصدوپنجاه‌وپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/akhbarefori/653264" target="_blank">📅 20:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653263">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
العربیه مدعی شد: دور بعدی مذاکرات ایران و آمریکا پس از موسم حج در اواخر ماه می در اسلام‌آباد برگزار خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/akhbarefori/653263" target="_blank">📅 20:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653262">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
مجاهدان حزب‌الله: تا اخراج اشغالگران آرام نخواهیم گرفت
🔹
مجاهدان مقاومت اسلامی لبنان در نامه‌ای خطاب به دبیرکل حزب‌الله تصریح کردند که ضربات مقاومت به ارتش رژیم صهیونیستی ادامه دارد و تا زمان اخراج اشغالگران از خاک لبنان، آرام نخواهند گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/akhbarefori/653262" target="_blank">📅 19:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653261">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg2DIehjTLBXfxkpmD0N9nkgMzFZobIzjKc9t43B8LyKPoWiuigsoLHDQO10YTZE4JbI4UMpdq83sjnXQlyoO40uIpfS11wbwb7y14Uuj2Sh3A744UEkBtAVDazqLdDXaKRXzsxFGsS_kdJVRM3I8nElIlPNr__GOk0XLTqMmaInCHql4jNYzqvcQZ32cWqxH2N_DZiDI2qx2g_10ZiM0DHFNCMc6TXN9VpBV7Mdxe02N8X_d-ms2M5xj9471HqqslMak_PXvUkhumFlIC85oYWuJjhv7d6bfMdGtFWUxa6LGoHoIP6fKz8kI0APkXY-_nFxHKZTuYswpcUJw2Rg7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رمزگشایی از پیام مهم سپاه به آمریکا/ آماده برای جنگ در بیرون خاورمیانه/ «چراغ خطر» روشن شد/ این مناطق در تیررس موشک های ایران هستند!
🔹
در جنگ قبل، موشک ها و پهپادهایی به سمت دیگو گارسیا، مدیترانه، قبرس، ترکیه و ... شلیک شدند. این شلیک ها اگرچه غالبا مورد تایید قرارگاه خاتم و سپاه پاسداران قرار نگرفتند اما نشان دادند که ایران می تواند در صورت نیاز، مناطقی بیرون خاورمیانه و غرب اسیا را هدف قرار دهند.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3216611</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/akhbarefori/653261" target="_blank">📅 19:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653260">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ترامپ: ممکن است لازم باشد به ایران ضربه سخت‌تر بزنیم
🔹
رئیس‌جمهور آمریکا در سخنرانی خود در ایالت کانکتیکات درباره ایران گفت: «ما به آنها سخت ضربه زدیم. ممکن است لازم باشد سخت‌تر ضربه بزنیم اما شاید هم نه»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/akhbarefori/653260" target="_blank">📅 19:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653259">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIv3HiMEkoYiT7EiFwCWsGhaGoyp8Uw6r75eI6ZGiw_GskTjeDRINzqXqa1MVpaFxgVvXMzMsc2lZm5AeF3b_2NwMTbJHoSFPhPmQB4Uv-sKCOqYZZctOYe6w95Eurx9VsZO1iVSP5StqoGtfxi0Huu9BFaZyPUWopxpRqEnVA0-lMhUi_EN0tBdmC383Jc1BQfnwpMlXbYxD-v9qIgtDGTXUS2OSqniZ_32p3UUZ61K_ELGMhTd2FRK1ZatCVxmcIpWj2Ia8wj5nXLdtQJIf7hoHqjnSSJOUSUzA2N5q2wo4skRb2lHLpuEPX9SHic_aCOjP6H1OyGyIgj10IEHEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سهمیه وام قرض‌الحسنه برای زندانیان نیازمند اعلام شد
🔹
بانک مرکزی در راستای اجرای قانون بودجه سال ۱۴۰۵، سهمیه هزار میلیارد تومان تسهیلات قرض الحسنه ویژه زندانیان زن و زندانیان نیازمند را به بانک‌های عامل ملی، تجارت، ملت و صادرات ابلاغ کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/akhbarefori/653259" target="_blank">📅 19:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653258">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ccda1ed3b.mp4?token=HlDKCut-Vs-WMw34WhzLKXlIxbDmb_OUMj5mPQiPTnosvxqhzdpad_I4-WptgtXpS5NpIaN9rxqF11XZxa2gg-BCStYroHAndy8ZaCKCC7RTJn-Hff4YPXfa6VBCu1WFa9Nuhm2R6dE8AGGGFV7f76-yLbD9nNInqKuPobU7YNPALf5sYxNWN2jDqWulSc4MLJBWtGAl4eROXzOelb_s8JJyXMbShSp1lD8SCEttD9ACiPyaFQ2MzkWZc-ElyYUHa02Ne28ag58_Vq6__fptjTHW94IwQOdbD62EDDgHD7Vu1-pQt0yiLeaAQwu46CQ0TDJYkqT7HnzzVPizJOyHiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ccda1ed3b.mp4?token=HlDKCut-Vs-WMw34WhzLKXlIxbDmb_OUMj5mPQiPTnosvxqhzdpad_I4-WptgtXpS5NpIaN9rxqF11XZxa2gg-BCStYroHAndy8ZaCKCC7RTJn-Hff4YPXfa6VBCu1WFa9Nuhm2R6dE8AGGGFV7f76-yLbD9nNInqKuPobU7YNPALf5sYxNWN2jDqWulSc4MLJBWtGAl4eROXzOelb_s8JJyXMbShSp1lD8SCEttD9ACiPyaFQ2MzkWZc-ElyYUHa02Ne28ag58_Vq6__fptjTHW94IwQOdbD62EDDgHD7Vu1-pQt0yiLeaAQwu46CQ0TDJYkqT7HnzzVPizJOyHiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: کار را در ایران تمام می‌کنیم یا آنها سندی را امضا می‌کنند
🔹
رئیس‌جمهور آمریکا در سخنرانی خود در ایالت کانکتیکات برای چندمین بار به دوگانه توافق-تهدید نظامی روی آورد.
🔹
او مدعی شد: «هم‌اکنون در ایران همه چیز از دست رفته، نیروی دریایی‌شان نابوده شده، نیروی هوایی‌شان از بین رفته، تقریبا همه چیز نابود شده.»
🔹
وی اضافه کرد: «تنها مسئله این است که آیا ما کار را تمام می‌کنیم یا اینکه آنها پای یک سند را امضا خواهند کرد. ببینیم چه اتفاقی می‌افتد.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/akhbarefori/653258" target="_blank">📅 19:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653257">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXsVuTdi0wRgwTeI0hLv0SZ6qp01WEpD02e2yscxGSu5B1k_qrh1-J43E4lbbNiV4MjCdQ5CW3DzHFw8-AmiLPf3uc22u0tuXBih-vYRhIwwpROddgphbkhYsTdQeiGo9GF3v3EtIgrBW7J4oCYHJ8PY2-zUV9mY8_fVmfe8cqi3m2tbivgFhrEnwG7mIEnxkxQUoTRdBoPzASIS07-Wxb7Z2SkKJ7ngIl_QZhlEpX-NfM_svULVyD60cgn5SOE2KdHp9PxlxcB_ANiIJOl4lgPoxUK2STtwT2RlBi-MFUMokgSNmBb81bQUiJOOv7PsxsWkmei8rEWqGvpCMQHNhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معنای جدید «دیکتاتور»
🔹
فایننشال تایمز: ترامپ و پسرانش «برای همیشه» از حسابرسی مالیاتی معاف خواهند بود.
🔹
وزارت دادگستری آمریکا به ترامپ، خانواده و مشاغل او، مصونیت از حسابرسی‌های مالیاتی می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/akhbarefori/653257" target="_blank">📅 19:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653247">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gM6JQcZrlPapjPaoKRS8KjaIt8qXScdB9kireE6Toguy84XL-sfK7lAjjXasbAMTjr6RoTqEx0prDE-UrNRw0gIgoAouxzMwUfirNxlHXyDrSSMZ759QT3Xs5iwbS9fTHOnJvRx0HF2u9JE0RvqlTzmzfoo3wN2EPLz6dPNum0OC4nZq9qUnm7cEtmMpHfbU6sbYCTixavYH3CMQTkfyMBlof6kkADtp9OwQhLHU9O7-3Rd-QiYW09vG-SfUiOYVXnKc54lEjh3SgyzqpH92PAREBAz1LTagdgRU7f5uKay65QQ02NuSfODgy7gAqf9EKqxWsrg592Op6TfHDHPRCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BskZddYP_JW-SlmJG84Ox8DvMioH7m_NSAuHF0Fr4ULez-2Aj5ltHccMdAlL9H2tPw9St9xmOqWNfIVsjqz4zPTrCsln3-UjjvUhpMXu-aRAkuuf2vprv_OD14CuCk9GenMXyjB9mGk84XKXYU6nQtYB8sKY0H4EHSUVubSMWMQJkf0UQmbgLheaSxjA_n6LVHZecXdr3Wbm1QXZ667JAUaoCCQ4DSI0iBwL5fLGGFRMS09-EFzB0or2ICNO7cBEDpfB-174iQe133Hjngr8ReMP8-jda_GUSRXGBJAtOdU2ykk_7y_0Jo9hy5A_wzvInVFDqWszWqImsrfqD51Itw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYyNAJhKvTtgTlAU4kCvMycIDMiUm9sspUawUBhiDx2uhNt6zZp4Unh_UBcFQn19M5Xsj1fGubfCp6v9O53EnfQetTkwNJ_pWAazbukn3vuIuijMqWdKDh73c5FfFOb5_ZVngR3gRAStpHKPYJg-thTLqcZZyPDWDMM81lyQYwjom79LS-ybM45ZJ-vvqWy7Su0lTQq10_WIEjj73op3DON7JGh9Jk62Nu4H7uLo5aPhqYUSSz6CLOeIEWaGjHxBZIwa-RuBHSDhhY_gR7uVBzm7x2V7-rGY_zeWU5jN4K8weE9NLefZKZn1gQanCbZ_1xjJm4AeEOq8qnUHM3zHCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVPsqO97S1FVFrMbb-zkwq4z2XocXxK9tmEpxCc5JVHDFkRsFfth6W1dGxX1WVkaXmIVPWxPJabzpwUiYwEJWfEnLuh5MUNQXyGqZ8iAOUkvMOLZtqIdnY9IxY37zwX5yy7K2MrTGc6a9MlzB2h5roULNFYTNObHsvZ10d5mwVyoZeHeaFFNOUih7eG_DIpiuax0okreh2_dNrrmHgggit7PhxtBuHp0oWhB4rZkD2c-1oENCxsgxTMCxgjcqDfWNFSL9bb4ydPtbLIKvETh-klkBudYDARIqULpTjmQmxfZOGTeEnTk0MJzOcSSaHqcU1T_8PeyrqYj_UQu6WYKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/budCALh4Y8ZbMUhWTOFRFhzyZNAUiKCtOHrsPxw-rrBqs6DkCYgS84uVrZsnaF0cgIhWJMEFuZYosQaHQcjveNRZSy3jfzR2PcOt4W7MkRrFdLCJiDA1JqNkeVk4P7Ros4hcFU_iBWbsKEx2KY7Be0IwSqPWQwPVGrsrFd7hVJwvtBDDhYlH7N-nEeoIObq8ma5ReU3eHpx0JKzhEoZyv4ZRMsc97qbb5wXkeRnfslF4L6RimJ2QIUGkIopwqJiLrsv2QJnjjtk8UMCyKqdJp1ZQMa7FWkaClTnlfEW1mxlUDkdTCTvMRoJt8Rf5qZj1UcSJx_IwZ0mcqj9pJIrIdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IMCPzSp7kgFdI1Xvz3PtP7nnxldquaPMkDnElV0odlEB69x1HXTgEJMN54SpPsiOCjbBepnhoBIPq7eQfib_e3-kOrgy5xVizqW1MCewXCrQes5G9DOiyIf1nGa3PF_PwfEGn28Ut5lr4eHxiiAH0z0iuBAermr9onGlVU7H2P6uh1QXDwgr7UB20Ea-iflG1owzoN87zl954Tu8l9U7ev6Do6h3O4wqzfr5LhimOXHS4Jbh6NOultXYDBR09ame_c9WSgmH5OUq247BBUiCYRziWLP9TIxhCxVlqhpLr8ZiGRaJxqePNghMGgYRhPzmjKwhlOwnsYQb59f41OT1BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bbaG1VEr5sqWniAXiPpDu3XO1Ws8vlFwMaGeXRBsrHXh-PLRcI8YUpOi7irCBDmGreuwgt8dhEoMIKt6NNp3dlKeR3xFqRc7rwRUsuv9hxx7pMcBrc3zd0XzIJtPUOaaFEDgYmIAOk98oD72pKf3LYvNfvbqtPdXn45X4t4TqdIytmp6BxEtyi24hwvn44YE-DZ3XElpr4TmQ1J-4Vm4BGzLJ0bl-HsyJ5J8t4Aowz8L6mbYWkJmAiacSUfOg9yabWBiIRgQkHNaIgjg2VS7SaFovP91MZqc9Y9iISFz3dZB-Y12x2SyLRLMxxVWChmmcAcdBbVXgIBvFjlZVSxtZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lm5jAi4vp5JOEzI09O23q2_e-XpsKPalXfApacQJI43_0pYeHEFweYhWxEAZGMwY64fM7BHfTSmpKxVo1W247VPc9hb2ILVoxPorDDoeY3pfCDQSuhoy5DRAJe7IDMpsVA0TUyOmQ7VL9R6UAJQMSSifphX_869E7wbBq8oitQHSObGJ4ftWLKaC5KGeelBugxxCpEZHg3V8x3wFugv4lJ4g8nuXKMYr6WljvrkUaGV5CkvzBWf9OqwJWRB4pCTKogxzhwb9U1pSYqIXk_YuiZgM2pV_9KSy5F4yaEny8AUJrGPT6V-lYH02NkCyK99eFEvRVSTLMI2HSI1W1vtzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gD0BFW-m_sgXo0vYlP7VS_X9PcDZ0LMHeGmvjUouZtvkRRQKFOcJtAA3eK_1raYD9NYZ8Ya8Q5f43tfXiywrlnP0Cn4XVRbfI2JuBOLH8s581mSgJZasFxku53hQwNHKccnWakZHCwhR9-L1HYH3eWn3dY0lEnN819rMg-1OjXwS2-LGFeyRV6__oNfItfDsrUu22lT8YrMfdf_4kgeFf7bhHOj-DSkWPRRmF-WtQ9iPOdE8ppsTzuACecnhc0Lu1NRlVUe55_w-KjDRDLHklomSZJQaiMYDpaYg-Q35vRfWtZbjrDKHzoylSVXSmj7LMMc5_PkVbJ__V_-8WqM15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SwfI7ZdYPJRxC7l1aZmyGreiYS8gObTtzcn4XVCFbTMV7n6CP_qV901u_KoJ-lCLklxHkXbE95MClVPJs04CO9LaFDoZcZWbm-tDP8J2GToDv7DFfeHUlKo9F9t2q3KZqveEFIi1fUEXroopg8ORG7gIyObpCL7RSolID9vtD9KyZ0tO6OEermrBUJRVrUHoUlMNnNpWjVjG_4qwWU7HIIu7T-jVgJ-scIjI8EWFVKrXnlCgqyD_Uw1u62RvelBbIidPWFunubAt2XODhILRhyHVzRRlwQztAphVbn5mLavuM4gOEWVhlnVQxomxqcKbUFRdxK8v0fdo30kjQvWCuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت همدلیِ واقعی
💫
✨
#همدلی
اینجا یک شعار نیست… یک جریان واقعی است.
#هیات_قرار
با همراهی شما مردم عزیز، ۳ رأس گوسفند را قربانی کرده و گوشت آن را  در راستای حمایت از خانواده‌های ایرانی میان خانواده‌های حائز صلاحیت توزیع می‌کند.
این جریان، با شما زنده است
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/akhbarefori/653247" target="_blank">📅 19:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653246">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
معاون ارتباطات دفتر رئیس‌جمهور: افزایش رقم کالابرگ تقریباً قطعی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/akhbarefori/653246" target="_blank">📅 19:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653245">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/588caef96d.mp4?token=tOgeE8dSPXWsGkjGt4O7X1YblCsgfpAD6JTiQNZpybNY1SHDKhXSZBreFnFu68TL9qf-BKOwnR_l3vLLq5gzT1ov5CwutvngxayswATJn7jUVbzmnSiNduL49qNyNDWFQFRo1NyfWby0Qp9QiBw2wdJ0utBpvhGj0voLvJjaSLy6FVPVXrqkvwVmDtNR5755yRNJmZhHGyKfE07MQlNMmzTfMATnLZM0C_klYixYNxc1kJ20Upg9rhTdbk9bMg_IRSdVuwlOz8O0XXEu0y8iAdR2DAC2RDm2nZA6-wWBXTYwJAcTF7okP4KuL2KdZoAowB4HeBtjr0U2Ct6FT9VOiSxOpaUQnpArEth75b7YmEIf_HD6ytDOM8R1DqlKY9z7q0OCPqfQ_YNQZC4wl7Fdw9-7j2TnhbPH43q_g_bppuuebj15HY6MBO4PVql92N3PePzFCQBPGqKPkd1fOayHQGJxg_s8O_sF__srMH5au-4CC8Wywj-Oalw6zXhyGR2sitnb7av8AoCC2_C-gIothd5btduSRAyGNo1iqYzMJoctsbcAaBnFKNRTkO4PArNg7W8DScRAbGKPCvcyYzwtYMyMbX18ABU3pC0srXWhbQ6d0KAwGjo-yf0Hu9-akH6mG93NCZFd2Vo6epHRB9inBkvJoAsBEMXixML4F3GL4iI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/588caef96d.mp4?token=tOgeE8dSPXWsGkjGt4O7X1YblCsgfpAD6JTiQNZpybNY1SHDKhXSZBreFnFu68TL9qf-BKOwnR_l3vLLq5gzT1ov5CwutvngxayswATJn7jUVbzmnSiNduL49qNyNDWFQFRo1NyfWby0Qp9QiBw2wdJ0utBpvhGj0voLvJjaSLy6FVPVXrqkvwVmDtNR5755yRNJmZhHGyKfE07MQlNMmzTfMATnLZM0C_klYixYNxc1kJ20Upg9rhTdbk9bMg_IRSdVuwlOz8O0XXEu0y8iAdR2DAC2RDm2nZA6-wWBXTYwJAcTF7okP4KuL2KdZoAowB4HeBtjr0U2Ct6FT9VOiSxOpaUQnpArEth75b7YmEIf_HD6ytDOM8R1DqlKY9z7q0OCPqfQ_YNQZC4wl7Fdw9-7j2TnhbPH43q_g_bppuuebj15HY6MBO4PVql92N3PePzFCQBPGqKPkd1fOayHQGJxg_s8O_sF__srMH5au-4CC8Wywj-Oalw6zXhyGR2sitnb7av8AoCC2_C-gIothd5btduSRAyGNo1iqYzMJoctsbcAaBnFKNRTkO4PArNg7W8DScRAbGKPCvcyYzwtYMyMbX18ABU3pC0srXWhbQ6d0KAwGjo-yf0Hu9-akH6mG93NCZFd2Vo6epHRB9inBkvJoAsBEMXixML4F3GL4iI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس مسائل بین‌الملل: در ۴۰ روز جنگ نظامی نفت می‌فروختیم و وضعیت اقتصادی کشور بهتر بود اما الان در آتش‌بس تحت محاصره دریایی هستیم و فروش نفت ایران هم آسیب دیده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/akhbarefori/653245" target="_blank">📅 19:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653244">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fe887bed7.mp4?token=kGhL_T0lxq8qBrJJyNfKGYxKKUTm6tNtJlB885ScfJ4zl6cA1ziWs6NJftYSOzJ8MY8QgrTtVROhObGrRi4-yZQaRgPyFR7n1CxFnxdkSR3gnvvcbEHJzELOcc5gmQWmQBY3QS3SrJIItf2Qce-BlF7Kun1CMlewYWUvfKNIUBdk1edIpnUa53zbq1gKReWtRRiuHQaGuhmnJpYbBijDod1AjEC9PzhAP71_WODUSJ_1ZJDBgET57IdUZHURJ_v0ukE0s1h5_7zOKo-kp4IZcERW5-7RyDSLFV5-wfXQUEW6XuCusXISQ4fqMzTjZQho4blMcFN-a4muwf7gVSVcrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fe887bed7.mp4?token=kGhL_T0lxq8qBrJJyNfKGYxKKUTm6tNtJlB885ScfJ4zl6cA1ziWs6NJftYSOzJ8MY8QgrTtVROhObGrRi4-yZQaRgPyFR7n1CxFnxdkSR3gnvvcbEHJzELOcc5gmQWmQBY3QS3SrJIItf2Qce-BlF7Kun1CMlewYWUvfKNIUBdk1edIpnUa53zbq1gKReWtRRiuHQaGuhmnJpYbBijDod1AjEC9PzhAP71_WODUSJ_1ZJDBgET57IdUZHURJ_v0ukE0s1h5_7zOKo-kp4IZcERW5-7RyDSLFV5-wfXQUEW6XuCusXISQ4fqMzTjZQho4blMcFN-a4muwf7gVSVcrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر اقتصاد: رویکرد وزارت اقتصاد رشد قابل‌توجه بهروه‌وری به کمک اقتصاد دیجیتال است
سیدعلی مدنی‌زاده در حاشیه جلسه کارگروه ویژه اقتصاد دیجیتال هیات مقررات‌زدایی:
🔹
بحث اقتصاد دیجیتال باتوجه به رویکرد بنیادی افزایش بهروه‌وری در اولویت وزارت اقتصاد قرار دارد.
🔹
اقتصاد دیجیتال نقشی بسیار کلیدی در افزایش بهروه‌وری همه حوزه های اقتصادی کشور دارد و ما امیدورام که با توسعه اقتصاد دیجیتال رشد بهره‌وری اقتصاد کشور را به میزان قابل‌توجهی افزایش دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/akhbarefori/653244" target="_blank">📅 19:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653243">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
معاون وزیر خارجه: ترس اسرائیل از کشتی کمک‌رسان، ترس از آشکار شدن جنایت است
🔹
غریب‌آبادی: رژیم کودک‌کش صهیونیستی کشتی‌های حامل کمک انسانی به غزه را متوقف می‌کند، آمریکا هم فعالان مرتبط با ناوگان کمک‌رسانی را تحریم می‌کند و نام این همدستی را «امنیت» می‌گذارد.
🔹
در این منطق وارونه، غذا و دارو تهدید است، کمک‌رسانی جرم است و محاصره‌ای که کودکان را گرسنه نگه می‌دارد، «دفاع» نامیده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/akhbarefori/653243" target="_blank">📅 19:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653242">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
تیراندازی اشرار به خادمان امنیت در سراوان
🔹
یک پلیس به شهادت رسید
🔹
دقایقی قبل سرنشینان مسلح یک دستگاه خودرو سواری به سمت خادمان امنیت در یکی از محورهای مواصلاتی شهرستان سراوان تیراندازی کردند.
🔹
متاسفانه در پی این اقدام شرورانه ستوان سوم «امیرحسین شهرکی» به شهادت رسیدند.
🔹
اشرار مسلح تحت تعقیب پلیس قرار گرفته و در منطقه پیرامونی طرح امنیتی و انتظامی در حال اجراست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/akhbarefori/653242" target="_blank">📅 19:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653241">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
اسپانیا: اسرائیل وحشیانه رفتار کرد، باید رسما عذرخواهی کند
🔹
وزارت امور خارجه اسپانیا: آنچه بر سر اعضای ناوگان آزادی به دست اسرائیل آمد، وحشیانه است و ما خواستار عذرخواهی رسمی اسرائیل هستیم.
🔹
احضار کاردار اسرائیل به عنوان اعتراض به اقدامات غیرقابل قبول علیه شرکت‌کنندگان ناوگان آزادی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/akhbarefori/653241" target="_blank">📅 19:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653240">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
بقائی: وقتی پای مقابله با یک متجاوز به میان می‌آید، همه متحد می‌شویم
🔹
سخنگوی وزارت خارجه در گفتگو با روزنامه فوليا د سائوپائولو برزيل: مردم نسبت به قبل از جنگ امیدوارتر شده‌اند. انگیزه بیشتری برای ایستادگی، تاب‌آوری و مقاومت دارند و فکر می‌کنم این یکی از جنبه‌های مثبت جنگ بود، چون ایالات متحده و اسرائیل باعث شدند ایرانی‌ها متوجه شوند که در برابر تجاوز خارجی چقدر می‌توانند متحد و مصمم باشند.
🔹
ممکن است اختلاف‌نظرها و اختلافات زیادی داشته باشیم اما وقتی پای مقابله با یک متجاوز خارجی به میان می‌آید، همه متحد می‌شویم. احتمالاً مردم را در خیابان‌ها و میدان‌های مختلف دیده‌اید.
🔹
در حال حاضر ما با ناامنی‌ای روبه‌رو هستیم که به دلیل تجاوز ایالات متحده و اسرائیل علیه ایران به کل منطقه تحمیل شده است.
🔹
باید به یاد داشته باشیم که تنگه هرمز پیش از ۲۸ فوریه، زمانی که ایالات متحده و اسرائیل اقدام تجاوزکارانه خود را آغاز کردند، باز بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/akhbarefori/653240" target="_blank">📅 18:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653239">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
امنیت و ایمنی تنگه هرمز برای ایران از هر کشور دیگری مهم‌تر است
🔹
آنچه ما می‌خواهیم مطالبه نیست، بلکه حقوق ما است.
🔹
نیروهای مسلح ما در صورت هرگونه ماجراجویی از سوی آمریکا و اسرائیل، فوراً و با تمام قوا پاسخ خواهند داد.
🔹
هیچ تهدید قریب‌الوقوعی از سوی ایران علیه آمریکا وجود نداشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/akhbarefori/653239" target="_blank">📅 18:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653238">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
رئیس اتحادیه بنکداران مواد غذایی: از عید نوروز تاکنون قیمت روغن خوراکی صنف و صنعت و خانوار در دو مصوبه دولت افزایش یافته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/akhbarefori/653238" target="_blank">📅 18:18 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
