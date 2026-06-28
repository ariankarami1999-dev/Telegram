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
<img src="https://cdn4.telesco.pe/file/a2l-I55Ldkag-wHHYKEQHBH0oWbmialpkOhQxDpMyvgobnGOQihjm7ziFRgChQWESm6OCrvljtDrzTgtnWWWsrj4NG54Dz4Jkcc64JIUpAyhuqxo3_Uem_qfgjzlb6_zRHC4L4EqaHq7xLa8lMjBKHA07RtJYYa5hARBpv475b9nNXqF7kJfCUi5-Vcl7HD92saZIAZUtXZ1zhkg-_xShS1UwKarI-iGAjuhOmTAoimML2FAYLaMtbZnMJ1CldfIQsC_8CXypo3PrA8RAFTsaz2_DJEOBX77-xg7Yw1Vr9JUOxsWP7odACHJzRn4yyfDll9nIA_Te85u_bJGNnB3AQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.22M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 21:36:53</div>
<hr>

<div class="tg-post" id="msg-664374">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
جدایی روح از بدن در میان شعله‌ها؛ روایت متفاوت یک تجربه نزدیک به مرگ
🔹
00:06:00 ماجرای سوختگی کامل بدن در حیاط منزل
🔹
00:12:40 تفکیک بوی سوختگی هر قسمت  توسط روح
🔹
00:19:00 انتظار ملک‌الموت برای همراهی روح بی‌نتیجه ماند
🔹
00:35:00 هدایت شدن به مسیر گمراه توسط موجود ناشناخته و حیله‌گر
🔹
00:42:00 رؤیت هیبت عظیم اسب سوار در بیابان دلهره‌ام را به پایان رساند
🔹
00:54:00 تعیین حریم برای من، توسط اسب حضرت ابالفضل (ع)
🔹
01:09:40  بازگشت به دنیا با دعای خاله در حرم مطهر امام رضا(ع)
🔹
قسمت بیست‌وچهارم (آتش)، فصل چهارم
🔹
#تجربه‌گر
: محسن اسکندری
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/akhbarefori/664374" target="_blank">📅 21:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664373">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/akhbarefori/664373" target="_blank">📅 21:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664372">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
گزارش شهرداران کلانشهرهای کشور در حوزه بازسازی جنگ/ طراحی مسابقه ای بین المللی برای طراحی یادمان ویژه شهدای میناب
نصرتی معاون عمران وزیر کشور و رییس سازمان شهرداری ها و دهیاری:
🔹
با همفکری شهرداران کلانشهرها راهکارهایی برای تامین منابع مالی برای بازسازی خسارات جنگ دنبال می شود.
🔹
یادمانی برای جنایت مدرسه میناب و شهدای مظلوم دانش آموز، طی مسابقه ای بین المللی تهیه و اجرا خواهد شد.
🔹
جشنواره شهید باکری برای تقدیر از شهرداری ها و دهیاری های برتر برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/akhbarefori/664372" target="_blank">📅 21:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664371">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da10dc61f3.mp4?token=cN1OuqnMPedurZG0b6kNeB0BEKSnsRhjrdqO1uCZNOYzJfok0m980hvpxDVDb0xXCDFYZZmIWlbiHZRv0u-nwfIam-_eHnydwVtZ8Ernwzsw4Nwzo2bPvCB6THuOxpE59zA4_ACFoC-3qbPrjKZ43Uzw_lfujcKbT3Juxz8nY8L6LwnHCJTnPnQvtewv1iGsDHAjRKgbhZS050jJp1JAEWMlbBfuZccrDExRq9MEREhzkxkyEGFic57yLd0FgkKiE1neZKNI0DHuJUXCJqytxc6P48TNYV84oPisJ883pcuTFCHPg4eyps2MjBDvwLXprbgyPvNB8q2Xtb-D8jm0tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da10dc61f3.mp4?token=cN1OuqnMPedurZG0b6kNeB0BEKSnsRhjrdqO1uCZNOYzJfok0m980hvpxDVDb0xXCDFYZZmIWlbiHZRv0u-nwfIam-_eHnydwVtZ8Ernwzsw4Nwzo2bPvCB6THuOxpE59zA4_ACFoC-3qbPrjKZ43Uzw_lfujcKbT3Juxz8nY8L6LwnHCJTnPnQvtewv1iGsDHAjRKgbhZS050jJp1JAEWMlbBfuZccrDExRq9MEREhzkxkyEGFic57yLd0FgkKiE1neZKNI0DHuJUXCJqytxc6P48TNYV84oPisJ883pcuTFCHPg4eyps2MjBDvwLXprbgyPvNB8q2Xtb-D8jm0tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس پلیس راهور: جاده‌های تهران در روز تشییع رهبر شهید مسدود نمی‌شود
🔹
فقط به شکل مقطعی پیرامون محل برگزاری مراسم محدودیت‌هایی وجود دارد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/akhbarefori/664371" target="_blank">📅 21:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664370">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای جنجالی نماینده مجلس: ارتباطات ناصحیح عباس علی‌آبادی مانع از استیضاح او شده!
حبیب قاسمی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
باتوجه به شرایطی جنگی که در کشور به‌ وجود آمد، وزارت نیرو اقدامات لازم را برای مدیریت قطعی برق انجام نداد و اگر مجلس باز شود این مطلب بیان می‌شود که چرا در بحث توسعه و زیرساخت‌ها، انحصارطلبی وزارت نیرو باعث شده که مشارکت بخش خصوصی به حداقل برسد.
🔹
بارها موضوع استیضاح وزیر نیرو در مجلس مطرح شده ولی ارتباطات ناصحیح وزیر، مانع از استیضاح او شده است.
🔹
هزینه حق انشعاب‌ها به‌صورت غیرقانونی و سرسام آور توسط وزارت نیرو در سه مرحله افزایش داده شد و از مبلغ ۷-۸ میلیون تومان به ۱۵-۱۰ میلیون و در نهایت به ۵۰ میلیون تومان افزایش یافت.
@TV_Fori</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/akhbarefori/664370" target="_blank">📅 21:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664369">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8586c87e09.mp4?token=Hqo7WHCS0JFMkcYQHxPJACcgJGrGzAY1B04qXcNxwpFZycUAPHewOMY4QrVIxD3-xwSrkvIGtavSi2CWiR4bvD7HZoC32B-xU8NoBin7kJpolVrZ-XqXvcYT5QnJJ0cFA-WUKTzoSQUC-a4t7BgpaOy_YUIZIWZsvWAFkHdq8JegSwtyGu7LZHSINtobzgeL6AVOCKP7FjcC4VSv68vfdRVzA8wX8cgs4WD3srjY4voK4O8C7VASTrPxSOGX8beai-EVKWcgZqTc7EEYr_Hvq19RXSSwXW1dceqWkYXPu8udHVdzgV9Qy34YqRdLhdnkrM6c9WGt4755ClZetBKIvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8586c87e09.mp4?token=Hqo7WHCS0JFMkcYQHxPJACcgJGrGzAY1B04qXcNxwpFZycUAPHewOMY4QrVIxD3-xwSrkvIGtavSi2CWiR4bvD7HZoC32B-xU8NoBin7kJpolVrZ-XqXvcYT5QnJJ0cFA-WUKTzoSQUC-a4t7BgpaOy_YUIZIWZsvWAFkHdq8JegSwtyGu7LZHSINtobzgeL6AVOCKP7FjcC4VSv68vfdRVzA8wX8cgs4WD3srjY4voK4O8C7VASTrPxSOGX8beai-EVKWcgZqTc7EEYr_Hvq19RXSSwXW1dceqWkYXPu8udHVdzgV9Qy34YqRdLhdnkrM6c9WGt4755ClZetBKIvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تو چه حکمی میدی؟!
قصاص یا بخشش؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/664369" target="_blank">📅 21:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664368">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
سید عباس عراقچی وزیر خارجه ایران در بغداد با علی فالح الزیدی نخست وزیر عراق دیدار و رایزنی کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/664368" target="_blank">📅 21:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664367">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGqc3-1xPM-u2gYDNAyAzMV06ehy6dRneM0Jyrf5l_ECYgATPk4emZaUfBW0eJIArPvXjiXpEZmDdTZdqfu4jqpptfEeeV2LRFiaLH2_OvMv9JXqSdPJTSFi-sFJA-ftNJSRu81IiWsnA1erT3-zv18SwHpokWHMpPjdoDkzRCAqIiu9QTj05tJPGyQ4fDNbRDr8r08KIfPILe-OydbD32yHqkR-PfLN6xQ2ZbZTmFj5R_4PJufSmzsCbybx0Hga2BAs0BoAcd11Kxj-3RQH8uao6nn_yIF7IKGQ1vmltNpBS-N1hVv99GH0gRCkHUDUplhgipeNq3UJBDcfVsXj-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیشترین شانس قهرمانی در جام جهانی ۲۰۲۶ از نظر Opta
🔹
فرانسه در صدر جدول؛ آمریکا در جایگاه یازدهم.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/664367" target="_blank">📅 21:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664366">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEJZe3FJ26GfNbQMLXd5a6ileLDzKXwqQd151qWpkThVElTHeoiUmFMQhOAxfKEc-ouN90jSpqLKGCwGJP9hIosF0fIXinVzAbuFnyixFqXgMIgY6TS1QbXiwxONj4TYzspkAzF0KGXxOHW9Gon6WQprbFHJoVJk72uZVSoWD1BDe1Kk60R6eE1OHKpy8jKP484nFvn_wUh6zgODe7jB5IFv_7H_GZtwCQOefSwm1RcSjsJ7pjt4vxxZ-NKBLxNc0ip90vLiSbrSuKinQUz8l3lecFpOQViRPd3y9i2kv1TDCuOkF0XhNNeBYhy7ec_LQpZMnzWkXcIccqca8D6wBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نکاتی که باید قبل از امضای اجاره‌نامه بهش توجه کنی وگرنه ضرر میکنی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/664366" target="_blank">📅 21:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664363">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بانک‌ها در خط مقدم تاب‌آوری
🔹
جنگ امروز فقط نظامی نیست؛ از حملات سایبری تا عملیات روانی، هدف اصلی اختلال در زندگی روزمره و فرسایش اعتماد عمومی است.
🔹
در این میان، شبکه بانکی یکی از مهم‌ترین زیرساخت‌های حیاتی کشور است که حفظ پایداری آن فقط یک مسئله فنی نیست و به آرامش اقتصادی و اجتماعی جامعه گره خورده.
🔹
تجربه اختلال‌های اخیر نشان داد با وجود فشارها، استمرار خدمات پایه بانکی و همراهی مردم می‌تواند نقش مهمی در عبور سریع‌تر از بحران و خنثی‌سازی اثر تهدیدها داشته باشد.
🔹
در چنین شرایطی، سرعت اطلاع‌رسانی، شفافیت بانک‌ها و استفاده مردم از مسیرهای رسمی، به یک مؤلفه کلیدی در مدیریت بحران و حفظ ثبات شبکه مالی کشور تبدیل شده است.
مشروح خبر در لینک زیر
👇🏼
khabarfoori.com/fa/tiny/news-3226382</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/664363" target="_blank">📅 21:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664361">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwafO5yCiLLqAkwv4vCOShH8TqqG8Nsv-0j03UoHo1O7rFB9t2kkoDGh8pjiVrFluoN1YPk9DKEgBYnBugnie0bPkpwQXk5n-4Htu7kIhjk7ZM4RDWuXzmdR7HPjyoGG2Y4F8djkHbrULlkX4d079SemRygJJq7H1YkQApUMbVN6huGthZhggNFLR2-pbKV4duZoJKZcMJmahUdwnEAxqkWTz_UV6Fd1nKTQUCogyeBI7eicDDezk-s0sdjn4duUPcQ0M0NttjxPNTk6nycRpWZJsTOzQIPwlQcl1gYjNmCC1y-ubcVcg0WB9lAGlS-5_FrsUdwj9v-zQqgJ9804mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقایی: «حمایت فنی» غربی‌ها پوششی برای تجاوز علیه ایران است
🔹
سخنگوی وزارت امور خارجه در سالگرد بمباران شیمیایی سردشت، کشورهای غربی (آلمان، آمریکا، انگلیس و فرانسه) را عامل اصلی تجهیز صدام به سلاح‌های ممنوعه بودند.
🔹
بقایی تأکید کرد همان ادبیات فریبنده «کمک‌های فنی و لجستیکی» که در آن زمان برای توجیه جنایات صدام به کار می‌رفت، امروز نیز ابزاری برای توجیه اقدامات خصمانه علیه ایران است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/664361" target="_blank">📅 20:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664360">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
تکنیک جدید وزارت نیرو برای کاهش اعتراض‌ها به قطعی برق؟
🔹
گزارش‌های متعددی از قطعی پراکنده و بدون اطلاع قبلی برق در شهرهای مختلف منتشر شده است.
🔹
بسیاری از مغازه‌داران می‌گویند این خاموشی‌های ناگهانی باعث از کار افتادن یخچال‌ها و اختلال در زنجیره سرد فروشگاه‌ها…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/664360" target="_blank">📅 20:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664359">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1sypLng0BUfRSxa85pwhaZrewt_KCAH34AQe2WjlrIHPdRHbcTOoKrXWiw_OV2PAMZqsyPX2aKaCpBQjKEHa116q26OZgOtFd0ye9I5rXhhqyt-7-klVJfRcYyD8msI2VP2X1F96glnyzIh7kh1cEQHuooJtyY7YrM_Hw5hx5l6satfgxHuvMy1xr8ItsVIYPfz83dlWql965iWu1JtjNcYFxgz5xs7RLM4sx2nenxS1rQ2FTnKn7Q_egyCFNSiUuhAqkhrQNdqBjQkQaQqL9-mn_-SuZXYWikM-FuD9b8dLqy2Jggk5_Vnjib-DBtiehHR8JV9iO2lo1HoxycKVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری جالب از عثمان دمبله بازیکن تیم ملی فرانسه و همسر محجبه‌اش
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/664359" target="_blank">📅 20:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664358">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nN1uvFLJYIocImwK27dLX_0nCrvHcrumtjt5jsAOaYEL2DcbUhL4EfZsz58ljeb7gnP6RHe7PtD27EetEFEtA7FauoPJhdbnBmEdHeyHQRRqNVVFVIoXQWvU83GSpinAk2jBzUzyV36cZNlRfVmaOn3hpb96saEv4QM_L2YOYzQD6vs0tDPxoyEi5kENUmH49Z4UiF6DAHiX0rYLjm2jRm05-TdhiPdcJ7DTRaREJupR8IBEIHkvltuJI_ddx-SmZRqbnkqRKmUogbCjmsODYwut3wSLndfPvjewA5DQQRBhfp02scZtJ03QF6OuDYgdopoN9yKVEQPp9Yq5NNAzZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان عبور کشتی‌ها از تنگه هرمز همچنان اختلاف بسیاری با میزان تردد سال گذشته دارد
🔹
بر اساس داده‌های «PortWatch»، میزان تردد در تنگه هرمز در ژوئن ۲۰۲۶ با کاهش چشمگیری نسبت به دسامبر ۲۰۲۵ مواجه شده است؛ به‌طوری‌که تعداد تانکرهای نفت از ۱۱۵۰ به ۵۰ فروند و کانتینرها از ۴۰۰ به ۴۰ مورد رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/664358" target="_blank">📅 20:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664357">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت بهداشت: مصوبهٔ رایگان بودن بستری کودکان زیر ۷ سال همچنان به قوت خود باقی است
🔹
وزارت کشور قطر: یک شهروند قطری بر اثر اصابت ترکش عملیات نظامی در منطقه کشته شد
🔹
انگلیس اجرای تفاهمنامه ایران و آمریکا را خواستار شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/664357" target="_blank">📅 20:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664356">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff799e747e.mp4?token=FPzM_BbFXUyWFRpdGyvSzauULNRy81t-bAJmhasQwiikn3Lo0gzXO1GyTwzUNdkzy3wL8sn0utJpUBicFP5bQxvbjIEMJbTyr0noxM5m2g1OmjLmiLIOPT4XGbqpPe70ZrmgSSp_EAQIIhGbYvtdRU6DM4UxRQtipsBDv-MoJH2-QwE30astgc-_5ItiPET-yFE1Ks418tEKrkU9E13liA1yXlZQtOV-jlWZQ22QUA79hO1YyHywYFFp84ytRMinOafv1oQLdVchSSis8_LZBqDQE04MwrMa8klGtMrsPHO-gCvocdFzCZ2T1uVWqL0heWRzy8Cu8ooJ_LiE67jMCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff799e747e.mp4?token=FPzM_BbFXUyWFRpdGyvSzauULNRy81t-bAJmhasQwiikn3Lo0gzXO1GyTwzUNdkzy3wL8sn0utJpUBicFP5bQxvbjIEMJbTyr0noxM5m2g1OmjLmiLIOPT4XGbqpPe70ZrmgSSp_EAQIIhGbYvtdRU6DM4UxRQtipsBDv-MoJH2-QwE30astgc-_5ItiPET-yFE1Ks418tEKrkU9E13liA1yXlZQtOV-jlWZQ22QUA79hO1YyHywYFFp84ytRMinOafv1oQLdVchSSis8_LZBqDQE04MwrMa8klGtMrsPHO-gCvocdFzCZ2T1uVWqL0heWRzy8Cu8ooJ_LiE67jMCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریس مورفی، سناتور دموکرات: ترامپ بزرگترین تهدید برای آمریکاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/664356" target="_blank">📅 20:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664355">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmIRfY4p5a4--1VVpq46wPG1Fw8hbhMNlAKcGJqoYBPcJ7HV4qx16ZNuNox8sbzXk6wHBB4f00cArQLFHMd8PGykY_wBgKH9GKUN4x5KLEQIVFbWod3DeOWSIH6b82-QiodZ_3BJH5W9cZgqqAmL_O06dlzMY0nbKcekFmcP7tuvImzNlk9qe9AJQ-BfmCsefIqxklL4a_K5ffYRkKx4yswuwQp3fRX4kQAtQz5EBGxGFgvZ6bmQcG_9Mbll58BVRohJQLMGRF1qMq3ouz3542YFt_lA6V7Cz-cYxNxv-FnNUmjz-9ejslhw6zSuyrJKUmw10xlKtCYlQB4do9Q-NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم‌های صعود کرده و حذف شده از هر قاره
🔹
از قاره آسیا فقط ژاپن به مرحله بعدی راه‌یافته.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/664355" target="_blank">📅 20:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664354">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
تمدید آخرین مهلت ثبت‌نام آزمون‌های نهایی
وزار
ت آموزش و پرورش:
🔹
مهلت ثبت‌نام برای ایجاد و ترمیم سابقه تحصیلی را تا پایان سه‌شنبه نهم تیرماه تمدید کرد؛ این آخرین فرصت داوطلبان برای ثبت‌نام است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/664354" target="_blank">📅 20:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664352">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/liN-hnyI4H8u2puo6JIjxQgW2UGdTAJM27AeE0eMRwQEiVSWK2UqMjnf3i8rFSnaZ0Uck_5FjZqFDUIUmORKZ-BIGrZCKm4L7nP7gn76_8V0Cfg61tw1DNpFrXSbWuxa1OQ9JEU5XrPCTXbN7zExlZHwT4fjxE2pTGKdCWIVwuq69F-7hep1PNlVNKz9ojQX6Vnd1ePrpOZFzl-0TVyrJkbY6mqYUPuvb44xatobRsLAf9LDC8a0VRv7sPFmoJgf3rbC2gyJvTHc2EtQn4jdaXBbOIvCHh0aGDeHZ9GBExDMT42zb8wLajpmYtKK7CPzo5TM0GVxdZkCLrrOl2I5SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FC2xLNnBDCQ4Bxb_FaekbAUlEhMA6PmW8PbzQymozx-4Mdo2hEt42abyHBWW-KIrltNRlcx6jAzoKgAVJNkx_UJSrcYisSXc5vqBL6kUxOCSd9enPm_ZOVM1-EZ7tb5HMo3YaNYzAg0mCLEXNc8EM7a67MM8eNR2NOnCGesVnFrpUGWCwFkSHKalnjKkJNfEMRy3T8wz4zzTO0EAp1X20E2AvWH5mnIGT1_CfhUpGzXt55pBXIKHaA7vD4QyenW1zTNPRi3a_HDWUQGx_acJoYFiVE3OIvULV1KNw70Zt9i75d_BMXWkUsN4bDJF59dBQbDvgx7ukkcO-XF2F3ZFXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چرا وقتی تاثیر نماز را در زندگی‌مان حس نمی‌کنیم باید نماز بخوانیم؟ برای پاسخ این کتاب را بخوانید
!
🔹
اگه تا حالا نماز برات فقط یک «وظیفه» بوده، این کتاب نگاهت رو عوض می‌کنه. «چگونه یک نماز خوب بخوانیم؟» از علیرضا پناهیان نشون می‌ده نماز می‌تونه منبع واقعی انرژی، آرامش و معنا در زندگی باشه. کتابی کوتاه و ساده اما تکان‌دهنده برای تجربه یک ارتباط زنده‌تر با خدا.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/664352" target="_blank">📅 20:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664351">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4Gb1e63sXIPyoCucLaFNf1pm4AiXIXZ4Kqbo-hmDv0-BaJeTRvkvv3B-V_X8q-5WMmQEAyWLPQKA__HxQ9U_Kqi_zbYjSUEzUFq5iSrsaamvIjCIxnhiIDxVplXQCFfNTd4vipzsUCmDOyxXF5fsfgHz287fNjGT9giCxDjkrv2oMdhVwi3E8ArULtLyTYTRB-RfMmsmdR9ebAR4h8KAAIqwXX5wwgFG8pNTVefdjn1iZm51QKi07C2ozs0H1CMumT-LwAvYZft6RcimxoSsL-AeJYnvF8jrBxjqipyuyMscwdbbx7O7YY0zXQ0p5A7MMfxjPr_6IvnQW_R8Fw-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨
☀️
این تابستون
یخ خریدت آب می‌شه!
🔥
✅
تا ۸۰٪ تخفیف خرید آنلاین و حضوری
✅
خرید تو ۴ قسط
✅
امکان خرید نقدی با امکان بازگشت وجه تا ۱۵٪
✅
امکان خرید از بیش از ۳۰ هزار فروشگاه
✅
خرید از بیش از ۲ میلیون کالا
✅
خرید راحت حضوری فقط با اسکن یه بارکد
☀️
برای شروع تابستون آماده‌ای؟
😎
⁩⁩
⬅️
از لینک زیر خرید تابستونت رو انجام بده:
👇🏻
https://l.snpy.ir/auukx
https://l.snpy.ir/auukx</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/664351" target="_blank">📅 20:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664350">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42a2aed935.mp4?token=P0qTz7J6onDvm-nhxFTeaQ2-WF6yHIQqB0iC2hrneoFuxp0vAojftuTSYYLzw47Wd87TWDQHtGH6BmhRO4n0OU1jGmkTYxanemcX8vGKSuRjZmyZZ6OvCiHcDD5AB_c6ZRtpKKFRFjkIerRkdyh5RDSW-ADMEB7QSIjtUYDBacS3J4tLUtjQOJSpFxNwLiKtPWnribx6MXPeO_dERaxC6WcyqGAyDoTQVgVbwgecB1zKNtFvmyvKJRAj_8hN2uHes8lN1uqb4nuYYNTvvRR975Aa1KuXH-uU0uiabMlgn6jnzypKAJX8KSoPtGgs5gJK5nBBhb8ZI_tILwyCGJre_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42a2aed935.mp4?token=P0qTz7J6onDvm-nhxFTeaQ2-WF6yHIQqB0iC2hrneoFuxp0vAojftuTSYYLzw47Wd87TWDQHtGH6BmhRO4n0OU1jGmkTYxanemcX8vGKSuRjZmyZZ6OvCiHcDD5AB_c6ZRtpKKFRFjkIerRkdyh5RDSW-ADMEB7QSIjtUYDBacS3J4tLUtjQOJSpFxNwLiKtPWnribx6MXPeO_dERaxC6WcyqGAyDoTQVgVbwgecB1zKNtFvmyvKJRAj_8hN2uHes8lN1uqb4nuYYNTvvRR975Aa1KuXH-uU0uiabMlgn6jnzypKAJX8KSoPtGgs5gJK5nBBhb8ZI_tILwyCGJre_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در یک دقیقه سبک‌های مختلف نقاشی‌ را
یاد بگیر
🎨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/664350" target="_blank">📅 19:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664349">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
توقف مذاکرات واشنگتن و تهران در سوئیس
ادعای وال‌استریت‌ژورنال به نقل از منابع آگاه:
🔹
مذاکرات برنامه‌ریزی‌شده میان واشنگتن و تهران که قرار بود این هفته در سوئیس برگزار شود، به دلیل ازسرگیری درگیری‌ها لغو شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/664349" target="_blank">📅 19:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664348">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ستون نویس بلومبرگ: تردد کشتی‌های حامل انرژی در تنگه هرمز تحت نظارت آمریکا
ادعای خاویر بلاس:
🔹
چهار کشتی (دو نفتکش و دو حمل‌کننده گاز مایع) با سامانه شناسایی روشن، در حال ورود به خلیج‌فارس از مسیر عمانی هستند.
🔹
این ترددها تحت نظارت سنگین نیروهای دریایی و هوایی آمریکا انجام می‌شود؛ واشنگتن در تلاش است تا این مسیر دریایی را باز و فعال نگه دارد./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/664348" target="_blank">📅 19:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664347">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
گرانی به نوزادها هم رسید
🔹
در حالی که هزینه‌های نگهداری از نوزادان ماه‌به‌ماه افزایش می‌یابد، حالا سازمان غذا و دارو از افزایش قریب‌الوقوع قیمت شیرخشک خبر داده است.
🔹
برای بسیاری از خانواده‌ها، شیرخشک یک کالای انتخابی نیست، بلکه یک نیاز حیاتی است و هر افزایش قیمت، مستقیما هزینه‌های زندگی آن‌ها را سنگین‌تر می‌کند.
🔹
اگر قرار است قیمت‌ها افزایش یابد، انتظار می‌رود همزمان راهکاری موثر برای حفظ دسترسی خانواده‌ها به این کالای ضروری نیز ارائه شود./ تیترتجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/664347" target="_blank">📅 19:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664346">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f218dcc87.mp4?token=mf9FNJQlUED4oHSKvtIFL_peIfP8J8zqkXYFaqrwfw-3DK_6qf4ClW3YzU5AhChpuUQZeDYAlqMrbq9QiJMpbBonHK71i2V2QiNK0Xt0IGzMFVdsJSfnCwSkcsdRPsWeUaVHfjrz1PJiQJx44TiuEk1-7DJSovOt7ByP32hAXrltrw7a2kVOfD066aqogDEmcincXyzoUksdSkkRdR0Ezi4trhTNdJhF9Iee6hTFOnx2hB7tp2L7Fa8SoUs-Hgk5c5uDiI0cWJ4pUhZJnkZA87zZMlDELsCzVidk65cF7VHGaPXjA6VpG6xNvKAtLQCUYXuTXOQvgxdufJp2kCA2fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f218dcc87.mp4?token=mf9FNJQlUED4oHSKvtIFL_peIfP8J8zqkXYFaqrwfw-3DK_6qf4ClW3YzU5AhChpuUQZeDYAlqMrbq9QiJMpbBonHK71i2V2QiNK0Xt0IGzMFVdsJSfnCwSkcsdRPsWeUaVHfjrz1PJiQJx44TiuEk1-7DJSovOt7ByP32hAXrltrw7a2kVOfD066aqogDEmcincXyzoUksdSkkRdR0Ezi4trhTNdJhF9Iee6hTFOnx2hB7tp2L7Fa8SoUs-Hgk5c5uDiI0cWJ4pUhZJnkZA87zZMlDELsCzVidk65cF7VHGaPXjA6VpG6xNvKAtLQCUYXuTXOQvgxdufJp2kCA2fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه‌ای جالب از برخورد صاعقه به برج ایفل در فرانسه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/664346" target="_blank">📅 19:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664345">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqIaZTtysxUjJ80pD7OcW5RbhNWwGZ_k_AVqCPGYoc4vBuQeEZLOdKM9-QA_Ptof00_NXxGUMR4ymAFO9AsfAcdIPfzC8_U7ZXvaMjnPSsK7YXeEhvZJs4I8tU0r_i4ackhnYyuV-MibdPVt4_eAFM3Vp5tpKYPCRxGAYTyQlnMHd8qUg6ZMiggmU2zmw_7URBYCIuSeMfekXCnudQFLRAnc9zGHgI6d4q65GDV6GHRLaSU2KkKnHzgi-_FPQFJ_3qku57h0cT3DNigNbQcxpDorAL4ecCjcBl9i3nbCQnpP6aEjgIfMSznXS4Up0beIl_bI3Sd6pMjKH-7_HVs99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش جهانی دسترسی به برق در مقابل بحران دسترسی در آفریقا
🔸
شمار کل افراد محروم از دسترسی به برق در سراسر جهان از ۱.۳۵ میلیارد نفر در سال ۲۰۰۰ به ۶۷۵ میلیون نفر در سال ۲۰۲۳ کاهش یافته است.
🔸
برخلاف روند کاهشی جهان، در منطقه زیرصحرای آفریقا آمار افراد بدون برق از مرز ۵۰۰ میلیون نفر فراتر رفته است.
🔸
بیشترین موفقیت در این بازه ۲۳ ساله متعلق به منطقه جنوب آسیا بوده که توانسته سهم بزرگی از جمعیت محروم خود را به شبکه برق متصل کند.
@amarfact</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/664345" target="_blank">📅 19:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664343">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f7hs52pbXj4aIKoPMJQ2y-HjUHkKdIcekFTuci4cZUaB26QFBb7HBU775YNmjZfddC32h9Xg2F4E6Jc0y1WtmlGr_Rifl6I3HSubdWrZWao47lQxt9iqDsuSceXj9_ncVO-ft-EuYJuqkK2In-Ogsj1lvPvMcl1dAIwLvMxI8w7jLSdt2hyT90GZHhT8BVo1TbCgNv_eOKwAmcFWD-zMs2TmlHleeu6_X2hrzULvpiGqTEyxhFWLYOpvbusyY8XIwkZnhGoPP9zPETVrhT9aDZhp632_5azhjd7WdHQv31FNwPxFsz4E0NJOBYFnYH3FdNL71dh1xlGDlWXz9jIevw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EXwFj0BP6MKMqXmhpaKw0pTuDRIlP_ZSVZM0cBRgwrad5M_72RIf2Ld_0EHBUcBmrUBGcpkgNgczvHrNEmaGIwlPVbYUTmYqpEEc5WL0_e61khpJfETHyMLYfHgPVmhsvBcVQNswcJi2CIfXTB0GsM8iKK-RXivWKFGcTIUWK47L6Lw7vMe_UnaVTHAh1lBTsM7k5f2idfI7N39hPqiNHNQqO5hx6MAkYVlZxIhUzQIrT8hjoxm-VgSX7aAiHbRn7AERQrZQdutBPxYctVIKb19j02le0d5mVJSFghomQoUctKWlHIKhiU4MpkozZeK6Xct9MuJNqENMTZiodByUVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تشکیل گنبد گرمایی گسترده در ایالات متحده
🔹
تصاویر ماهواره‌ای نشان می‌دهد یک گنبد گرمای گسترده دوقلو در سرتاسر ایالات متحده در حال شکل‌گیری است. این گنبد گرمایی شرایط گرم و مرطوب بغرنجی را برای مردم آن منطقه رقم خواهد زد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/664343" target="_blank">📅 19:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664342">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubEDVGqDbOqxwKB9wBpbbrwPt5Rstb_QhjxR21MCPLz4ZZfPEV3h0W14dd-SLBRVcXgHt2J9ziVe8BcgjdpaFxgZ2SWSvOZ_gMVV-AJZPs24-hW9gD8dnkaasekjAn4AzQf652dDl5E9Ko98BuP_MKvV4CMZ2sHJQ33lb-DgNbu1ZYaLEBF8sxn60LYESdE_VVhbtw9qRBcYCZ9Dyg1XzNJxXx4nvioKRV9zLPj78yeSbwLoed4pnaf1IKVxcowzkg7ISRBtLC-lWpcLq7LPl-h5HgHa3zlIGYXYTJCgsOA9kOzDtVzGH_u1aM75PLu3YIP1SBcM6-LRQgScnFoLqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صف پمپ‌بنزین‌‌ روسیه‌ که در پی حمله موشکی اوکراین به پالایشگاهشون اینقدر طولانیه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/664342" target="_blank">📅 19:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664341">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c8332b4.mp4?token=PWABwZxQVAIyyes3ZncggkDftgbaCh5CU-gCSs45stfy23-bSF8EIzrJ7LqoEIfgFgA1e1sV1nl9koW6vBOW9CFcsRhTWNYx3fevTrm3w9gVbBemBjZmYwiPkhIna2xioShpTugMTMkj9jvf4-XPPubaZ4Ib5K6h-4n5S2LAnFJF4_tFCP_oal8fnx11xtvSLFmn9AiK7izm4PZ3QBKJO5Rpwy-OKZVP2hBQ7f94es0zEOKDdBoWhwdIDuAQjdDKk9qn_rdVfryW3xaLVS7V5mIGHDd9TNkO68rd7uSkLJdFKSwHE5nag-T477-2DdtHurqFYRdEseBb7j-C6sSlxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c8332b4.mp4?token=PWABwZxQVAIyyes3ZncggkDftgbaCh5CU-gCSs45stfy23-bSF8EIzrJ7LqoEIfgFgA1e1sV1nl9koW6vBOW9CFcsRhTWNYx3fevTrm3w9gVbBemBjZmYwiPkhIna2xioShpTugMTMkj9jvf4-XPPubaZ4Ib5K6h-4n5S2LAnFJF4_tFCP_oal8fnx11xtvSLFmn9AiK7izm4PZ3QBKJO5Rpwy-OKZVP2hBQ7f94es0zEOKDdBoWhwdIDuAQjdDKk9qn_rdVfryW3xaLVS7V5mIGHDd9TNkO68rd7uSkLJdFKSwHE5nag-T477-2DdtHurqFYRdEseBb7j-C6sSlxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزاداری مورد پسند امام زمان چه ویژگی‌هایی دارد؟
/ مدار
برای تماشای این برنامه کلیک کنید
👇
https://www.aparat.com/v/dod34p6
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/664341" target="_blank">📅 19:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664340">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
افشاگری رسانه عبری از معاملات محرمانه نظامی اسرائیل با قطر و عربستان
روزنامه اسرائیلی هاآرتص:
🔹
صنایع نظامی اسراییل طی سال‌های اخیر سامانه‌های دفاعی پیشرفته، تجهیزات جنگنده‌های اف-۱۵ و سامانه حفاظت هوایی هواپیماهای تشریفاتی را در اختیار قطر و عربستان سعودی قرار داده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/664340" target="_blank">📅 19:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664337">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9pLr-UD8-Oesq_U7p133DF59PFwdkSGkgrHL4YahIfTdlr2p0nKn-m3vanFyTEc5-uLmxbGOMcn9S9RYfJmjCMuxahwbs48Zf7pSHKFV5wLWDTOh2CuDJD9PgtlajHy-CfxXLUCWU5qBQz9YBif3FUoT2xdkg3quT_wreWWY1WLMCz3Jy3EK3nnE-Cjzd8M8r8DSuzObbWvfl_5ueXXwvnAev0cL2Z_MIVzEzaMlER94KWddbHVTMNOThef1KR7NRRO_SCtc__QYxUIUtnExeqL_cjVMnL8T3OgSSQFDdfmI5TWBO0z5T3U-5mykh0ErWH0bCIZRsDZznmtj3vLVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQK8PXGSUOQQSRrDRg9HduoTWj0UImBVX-aGM3cEpj1v8WDoRjRlPOK0ULgJlYQ3lH4XcNNrKmzz722iriD0GMpi9KcXqvcq1zWnUTw3nLIvj8SnlmplLmE_tUGwi9Vk_YbkXWtoM1ehJfjchwyXv041_3XWTCD9crgouDxDzfaCBajktIghdFXgnzW9rGBfma7JLbNCX8QcCvyh-IR_3jKMWZc3q_Q2AyrLBa2mBDhfD1GuQUu71jCSIJADgPtZB66r_UooNPsupbfNhG6U3lDRKilB8mGAo02-NlVPc2uU8jammo5Wqs4DTN3htqd5T4Ta2yCd4Wn7lcTQTK16Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRxHtUaXDlPLxAfmpP2q5Fim0t1MmvsUg2Z7QIK6rOIwQ4n3Fgif0D0kqtJuULApAnD2Fz6euBvnMWzD2_Fxim5it9lrd_lNp7Z7BMCtmmcwbMb5ZovQQmv2Spq9QGyZMuVDw-ryOEfHNsVFnawzf3scxwyrlqOlZFJYkptJTtLbBufyuR1ZH8_dIy5A57tj9J0cS9PjOmSs35iRkoIPoLuFpZOeDJRuyNw-wgLSVK4Qf7g4tni4P4YpwzZgZ9wjnFOQBuxO9qWVzc3V87zFzTnihVkv8LtG31ucjy-yO0_qs2SJx4pvdomm2ZrMzLI_bNCg-WSdyn6LeGa1CBKqQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
واکنش فعالان رسانه‌ای بعد از انتشار پیام رهبر انقلاب
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/664337" target="_blank">📅 19:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664336">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZQJzjcmcU1ipyIAfUCZzXempLMINftutH5hRJicpWZJ03aMBcTOagtH_k3SRkE2B5U8E_l_JXf50rf9_ONEq-he_U1qbV6eM3ZwrvAjAT_xx5TKXW5EuaEzOrz2ZSJEmgaJE05BJzSgsg2DiFXeX9F33mvZktG3JILxD74giFtZ0zT1ZkEijc8v2XME3Lcxg-ai6_haAMbf9NIF7RlHdC9acKSyNKpRxgqlbCOB4Pn4eufgt0MJ5rYvLo9voWZT3IoFVi34PcqMoh66iOebEbd59ZppOMawkboZdYSSgsGsprV3-4TYMuKdA8AusM_GE0DQhJ3BNaF-V0fuV6CHdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز سلامتی در یک حبه سیرترشی
🧄
😉
🔹
سیرترشی، فقط یک چاشنی خوشمزه نیست؛ اگر چند سال رسیده باشد، در طب سنتی به‌عنوان یک ماده غذایی ارزشمند شناخته می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/664336" target="_blank">📅 19:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664335">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lz5a1pSlZ7J3fLttkEJie81Qo6-6pyjFQkXTfY4TvSVRZI0gSx_zW6KiFK9Bazu6yIEib5lg4WRRK2H2frLh9rLlvCgGQUcM-L6nX-ftw6qM_2F10bMhelFiTrtZDpIOmH4nRbD39QvowAD-CF61yHwLWUybao8Z2ncw9WwLiEaaOKqLMh_Nv5JffZO7X7YwNL9F2X89E48wSjN3cSeuinw_r-Q1UbHgFM-nFI_mk4mc2KazbTYZFSAgHewdu--MufZ0g5ngCgfAUpqJe6emVtg079jN6suACNLlmC7wqRe46bOXoXThhYbD6-Dg1PpzHfdEDpA3MwN66LVBUpQMjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/664335" target="_blank">📅 19:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664333">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
آغاز پیش‌فروش بلیت اتوبوس برای جابه‌جایی عزاداران رهبر شهید از فردا
رئیس سازمان راهداری و حمل‌ونقل جاده‌ای:
🔹
پیش‌فروش بلیت اتوبوس برای تاریخ ۱۲ تا ۱۵ تیر به مقصد تهران؛  ۱۵ و ۱۶ تیر به مقصد قم و ۱۶ الی ۲۰ تیر به مقصد مشهد انجام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/664333" target="_blank">📅 18:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664332">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
قیمت غذای دانشجویی آزاد می‌شود
🔹
از ترم آینده، یارانه غذا مستقیم به کیف پول دانشجویان واریز می‌شود؛ دانشجویان نسبت به تورم، ناکافی بودن اعتبار و محدودیت مراکز طرف قرارداد نگرانند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/664332" target="_blank">📅 18:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664331">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
افزایش ۴۰۰ درصدی تعرفه برق کشاورزی!/ ۹۰ درصد مطالبات گندم‌کاران پرداخت نشده‌ است
سلحشور رئیس کمیسیون کشاورزی اتاق بازرگانی مشهد:
🔹
تعرفه برق کشاورزان در برخی موارد نسبت به سال گذشته تا ۴۰۰ درصد افزایش یافته است. تاکنون حدود ۱۰ درصد مطالبات گندم‌کاران در خرید تضمینی پرداخت شده است.
🔹
قیمت نهاده‌های تولید اعم از کود و سم و لوازم آبیاری تحت فشار، بیش از ۱۰۰ درصد افزایش پیدا کرده است.
🔹
عدم پرداخت به موقع مطالبات، می تواند باعث کاهش انگیزه کشاورزان برای تحویل محصول به شبکه رسمی شود و ️این موضوع می تواند پای دلالان را در موضوع خرید گندم باز کند./ اخبارمشهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/664331" target="_blank">📅 18:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664330">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4209601e02.mp4?token=rVCk0oRfed4SNpKVXM9JOWHNw14Z_2qby-uhVGaK_C87YEb46uqKGVyEuKCoH8S0-47ckZaZ3t1XT-N-GRnW3C8CMBm7nu-xpBsdiSxslmF7gIczMIGoOfVaTM530Nk8ICSkO0S0l93E6OXol6bXzkIK5nRZqGtGNSXX-Lb2UIomi7eYM4gmL-7qNZeor_P4rgGiue4kawsKkj7Bn0aCUCD5tskKIg0SHoLiUE1kVOGhqqftNwf9x9lIVawi9OPsWB24FjHnMMlFcgCfl-mUYBFds2oBDIHaMm8M9BenJVjpH4tKAHrWHxSAZjNQazCHojb9ZD2GcruMcUScJ31WOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4209601e02.mp4?token=rVCk0oRfed4SNpKVXM9JOWHNw14Z_2qby-uhVGaK_C87YEb46uqKGVyEuKCoH8S0-47ckZaZ3t1XT-N-GRnW3C8CMBm7nu-xpBsdiSxslmF7gIczMIGoOfVaTM530Nk8ICSkO0S0l93E6OXol6bXzkIK5nRZqGtGNSXX-Lb2UIomi7eYM4gmL-7qNZeor_P4rgGiue4kawsKkj7Bn0aCUCD5tskKIg0SHoLiUE1kVOGhqqftNwf9x9lIVawi9OPsWB24FjHnMMlFcgCfl-mUYBFds2oBDIHaMm8M9BenJVjpH4tKAHrWHxSAZjNQazCHojb9ZD2GcruMcUScJ31WOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رضا پهلوی: حمله آمریکا و اسرائیل به ایران حاصل اقدامات من بود
رضا پهلوی:
🔹
یکی از دلایل عمده برخورد جهانی با ایران به ویژه حمله آمریکا و اسرائیل حاصل سفر ۲ سال پیش من به اسرائیل بود و به آن‌ها گفتم مردم ایران دشمن شما نیستند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/664330" target="_blank">📅 18:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664329">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKDrE2JrL4kvfe9xBUqPDNw3-uaQd0lZnrgHnQLCIt8SrGpCYMSsM8gfFzt5PHfKEwB9ytccwSyVpRz8_8rOKHSF8BBgNjQqFG5dDssLW6IrBrIarwh2JixS9lQBwlZGiTXrB4McTLa2WHTb0KzP2RExhF_U72c7eV7U8tbbO8uCbcMlAqwiaBw5xTwWw2ky7vfcQjYbC6XFAW3-nAvKG_Fol3DBWoVlooRwQzzaNT75VnBMxgZdIKjICGPSCdfZv7U2yHFBFjbOtHsBwK-is7X0gyK9C7C8mh4tkcklVQ1Qzx-Kjx-dyRp8VvIcugf7he1et5MflZZfx22F5kpu8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تایید صلاحیت برای خرید تلویزیون در دهه شصت
🔹
دهه شصت خريد تلویزيون سياه و سفيد مستلزم تحقيقات بود و اسامی واجدين شرايط از طريق روزنامه های كثيرالانتشار اعلام می‌شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/664329" target="_blank">📅 18:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664328">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32592ca1dd.mp4?token=LXKmYZmXOWIhEBKa88QDHpaJu27b_LllnZy3KRADuh67tu7etvjaneXIm8HKnH-PsSUAhB9IQ07mBX2R6fNDg_5KjkHSarQFKX82yiPMRMzq8vdYM1VrkJM2ASSTJsy9pZXUuXcq1QAABd-HZwydhT0KITlAK1-861oTxbwFOe3ErY7pZZ57kL3byAEmzBKWXWVuJKQhKRdDjidM_rTD9LuoLVF5tpCCTAtUV8aOzmM5EXj3Mb9tZ-xkB_x0aiYheifaFyXWZRk_9W4Ks5m7QSKkYdpjxegVWwFiSFURP0Og6_O2JCbyCluwD4Ec6wLAzqOFHCynqsOPZ9dfqzmfyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32592ca1dd.mp4?token=LXKmYZmXOWIhEBKa88QDHpaJu27b_LllnZy3KRADuh67tu7etvjaneXIm8HKnH-PsSUAhB9IQ07mBX2R6fNDg_5KjkHSarQFKX82yiPMRMzq8vdYM1VrkJM2ASSTJsy9pZXUuXcq1QAABd-HZwydhT0KITlAK1-861oTxbwFOe3ErY7pZZ57kL3byAEmzBKWXWVuJKQhKRdDjidM_rTD9LuoLVF5tpCCTAtUV8aOzmM5EXj3Mb9tZ-xkB_x0aiYheifaFyXWZRk_9W4Ks5m7QSKkYdpjxegVWwFiSFURP0Og6_O2JCbyCluwD4Ec6wLAzqOFHCynqsOPZ9dfqzmfyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
♦️
سپاه چه مراکز و تجهیزات آمریکایی را هدف قرار داد؟  سیمیاری، کارشناس مسائل امنیتی و نظامی:
🔹
در عملیات امروز، ۸ نقطه مرتبط با نیروهای آمریکایی شامل شیلترهای راهبردی، مرکز کنترل و داده‌پردازی دریایی، برج‌های دیدبانی، سامانه‌های راداری و ارتباطی در پایگاه…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/664328" target="_blank">📅 18:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664327">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4gvComh7LxssjwkEqz37i94cql-nMlrTh92nziclDdW-uhs4E2ivZS81QCUOePhQpt2CGs9A8O6TXBladtBDsz57HI3xspsnRfXZ3j399kceV_GVbWOqdX3Jtg-AYiIxiGMLH_4QV-KSXfC4_C3UfvLtH_AItUlikejqLcYkkaBO7xqlFDN7xgWlZitU9BKcC4qQe4Bn2aoZqRIoPsYzsyhG1HSmZxumRkiReULe8DEJ2hMVQf9hlUeSn7V51Hpav-htA2BG6tIqR4uyBnX2j4zmUQbgEz6_XOMXmHM256p1ge-k6WQWK6mSl-rZRy4QE4s5P4Bna3dl3lhqbY-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حسین صدقیانی؛ پدر فوتبال ایران که احتمالا او را نمی‌شناسید!
🔹
او اولین کاپیتان و مربی تیم ملی ایران و از پیشگامان فوتبال کشور بود. فوتبال را پس از آشنایی با این ورزش در اروپا به ایران آورد و نقش مهمی در گسترش آن داشت. صدقیانی پایه‌گذار نسل نخست فوتبالیست‌های…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/664327" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664326">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07250fe20c.mp4?token=li6CjlA5XE88srbJGzODPoqyzJWV-4D1nZoLjQdaReh1CJOc2lrkKJsiDGhHW7lh7DMYOdD62twskWRE_g3v-7_bP7cTBc7u1QI3FrNO86GAwKALpX0Soo1V3CkThxMGIVIhJ_B1koh7kW5L5Zz-y4mECgyhE1NUpkyXm3Q_s0LIdUOAg3e3IduIXxG4CRpccIz_7KT7Xxj29GAPf5d9vQawJ-jPc5fQWYTotX0errIb31rXQE5KehWF0abYhWydTQJMTuwlLYqI_XiEtnFN_ozTRQIzMFZWJ3B1Tcrytntz_kF4xsfSfNsZtnxZYEVyo9rBwUtVmISvaKJbVPfvTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07250fe20c.mp4?token=li6CjlA5XE88srbJGzODPoqyzJWV-4D1nZoLjQdaReh1CJOc2lrkKJsiDGhHW7lh7DMYOdD62twskWRE_g3v-7_bP7cTBc7u1QI3FrNO86GAwKALpX0Soo1V3CkThxMGIVIhJ_B1koh7kW5L5Zz-y4mECgyhE1NUpkyXm3Q_s0LIdUOAg3e3IduIXxG4CRpccIz_7KT7Xxj29GAPf5d9vQawJ-jPc5fQWYTotX0errIb31rXQE5KehWF0abYhWydTQJMTuwlLYqI_XiEtnFN_ozTRQIzMFZWJ3B1Tcrytntz_kF4xsfSfNsZtnxZYEVyo9rBwUtVmISvaKJbVPfvTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شگفتی مهندسی در ژاپن، تخریب ساختمان بدون کوچک‌ترین صدا و آلودگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/664326" target="_blank">📅 18:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664325">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUm8PVgyQWqek8p1ZGqtIyxeSUQa5GrbFYdm4lZx-lP81BvRfvX-B7ss5WM_waLFIruXZysYstsB0-apfmgWzBjy0ihurvzbTV8aAfcZz8LxLcc-IvApCUZbKrODZoOhroPc8FoI2QD1FCP-B6R7vBpvU7ILStvoSVvqzpN7fOdoYj11Cj3SbqUnKaxlppNNvy1FRF3flaeMnKLxyDdj2mWdnm8uJ4bofYvsf5lZB6lZQax_6xG0URn32vTeg5JC-1Tmhpp-veGohiwNZOjxUsnSrtYHteHOaieFrTYc0m2hWGum17eVX5__w-oj_JojUuDwAN1H4KU38tmFxDbBsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواره بدرقه یار
▪️
از تمامی هنرمندان، عکاسان، اصحاب رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود تا با ارسال آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور در سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» شرکت نمایند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگو تایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبر فوری ارسال کنند.
▪️
به برگزیدگان هر بخش، جوایز ارزنده‌ و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق آیدی
@Badraghe_yar
در تمام پیام‌رسان‌ها ارسال کنید
برای کسب اطلاعات بیشتر به کانال رسمی سوگواره در تمامی پیام رسان‌ها مراجعه کنید
@Badragheyar</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/664325" target="_blank">📅 18:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664324">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
گزارش آکسیوس از اهداف پشت پرده مذاکرات دولت لبنان با رژیم صهیونیستی در واشنگتن
🔹
مذاکرات هیئت‌های اسرائیلی و لبنانی در واشنگتن با هدف کاهش نفوذ حزب‌الله در لبنان است.
🔹
ورود پرونده لبنان به مذاکرات ایران و آمریکا، اسرائیل و دولت لبنان را غافلگیر کرده و همزمان واشنگتن با تماس‌های مکرر مقامات ارشد خود با نتانیاهو و جوزف عون، در تلاش است به خواست دونالد ترامپ، توافقی را تا پایان هفته نهایی کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/664324" target="_blank">📅 18:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664323">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 اگر برای انجام کاری به یک اداره دولتی مراجعه کنید و احساس کنید حق شما رعایت نشده، معمولاً چه می‌کنید؟</h4>
<ul>
<li>✓ پیگیری می‌کنم، چون از حقوقم اطلاع دارم</li>
<li>✓ فقط کمی پیگیری می‌کنم چون روند آن را سخت می‌دانم</li>
<li>✓ اطلاع زیادی از حقوقم ندارم؛ همان روال را می‌پذیرم</li>
<li>✓ ترجیح می‌دهم پیگیری نکنم تا کارم به مشکل نخورد</li>
</ul>
</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/664323" target="_blank">📅 18:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664322">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a900854f.mp4?token=kJSPPoWLmCpDZRZIAvzSNBfMHgSm0J3gYaFnjZQUNkrbH2Na42TNMOZiK_FloNlxpGxxto8i4FS4py3b27G4MEMoce5SYe-MVRAbdwt0PnrX0TFXgtBjNHDkwz3Mcn-LanMIZHTWkSQKzITH8825lFUhI4ExfcWJKwyfk-6f5d-im86mdOlyuucGGaMU6oB4BPhgzm4MJdVtt0MBPRRmdAw5lDzDp9G9BBrT2xNUZ-YWdrDYjgRGYXGpWquEHcKK4XP6yV1lg1JFdf3cEkFfq629VjNtasNKWH7ZyRW6gcJ3lgIOt_zH5pKdqBQuifo_pPRdt5pGXQyLPL6EP4RFpwXjwdLu5wgVy4mfo1Z42j8WWpjpbXr6H5e-2vOP50GFo4n7B58AJcxRtl314l8OkbLLj_NLfwXT4sQq7esrGz7ORW7PNtBbjzzU9Ay4_PQdnjxiG9yRBUmGkaZYmVBp8UIfN3WdYDAaF6xvUr-UNs-_HEgYyCzzludJTFkT3jo48GPUtKqvqEdg7YVYLsAqVXIewq-z6N9l2gbSyXOfpV1OGOEdSP3Fjbt-w7A52E_DfkSlp3QYU_i-rUKHjdxljuboDsi18i-u1AZtI3Rj50yLGoYrCokGw1dic6HfIXwzZkPNW_EU3d34ULukHZO3kQPCfSkQNBM4rS7A2e_GoPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a900854f.mp4?token=kJSPPoWLmCpDZRZIAvzSNBfMHgSm0J3gYaFnjZQUNkrbH2Na42TNMOZiK_FloNlxpGxxto8i4FS4py3b27G4MEMoce5SYe-MVRAbdwt0PnrX0TFXgtBjNHDkwz3Mcn-LanMIZHTWkSQKzITH8825lFUhI4ExfcWJKwyfk-6f5d-im86mdOlyuucGGaMU6oB4BPhgzm4MJdVtt0MBPRRmdAw5lDzDp9G9BBrT2xNUZ-YWdrDYjgRGYXGpWquEHcKK4XP6yV1lg1JFdf3cEkFfq629VjNtasNKWH7ZyRW6gcJ3lgIOt_zH5pKdqBQuifo_pPRdt5pGXQyLPL6EP4RFpwXjwdLu5wgVy4mfo1Z42j8WWpjpbXr6H5e-2vOP50GFo4n7B58AJcxRtl314l8OkbLLj_NLfwXT4sQq7esrGz7ORW7PNtBbjzzU9Ay4_PQdnjxiG9yRBUmGkaZYmVBp8UIfN3WdYDAaF6xvUr-UNs-_HEgYyCzzludJTFkT3jo48GPUtKqvqEdg7YVYLsAqVXIewq-z6N9l2gbSyXOfpV1OGOEdSP3Fjbt-w7A52E_DfkSlp3QYU_i-rUKHjdxljuboDsi18i-u1AZtI3Rj50yLGoYrCokGw1dic6HfIXwzZkPNW_EU3d34ULukHZO3kQPCfSkQNBM4rS7A2e_GoPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شروع کوچ اجباری مستأجران به حاشیه شهر با شروع تابستان!/ دستگاه‌های نظارتی برای کنترل اجاره‌بها توانایی لازم را ندارند
/ مدار
این گفت‌وگو را در آپارات ببینید
👇
https://www.aparat.com/v/gqj0f3m
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/664322" target="_blank">📅 18:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664321">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">گاهی قشنگ‌ترین روایتِ نذر، کنار هم بودن و از دل بخشیدن است..
تهیه و توزیع شله نذری در روز تاسوعا توسط جمعی از همکاران خبرفوری
اجرتون با صاحب این روزها
🌿
#هیئت_قرار
#گزارش_تصويری
| تیرماه ۱۴۰۵
@Heyate_gharar</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/664321" target="_blank">📅 18:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664320">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌
♦️
سپاه چه مراکز و تجهیزات آمریکایی را هدف قرار داد؟
سیمیاری، کارشناس مسائل امنیتی و نظامی:
🔹
در عملیات امروز، ۸ نقطه مرتبط با نیروهای آمریکایی شامل شیلترهای راهبردی، مرکز کنترل و داده‌پردازی دریایی، برج‌های دیدبانی، سامانه‌های راداری و ارتباطی در پایگاه علی‌السالم و ناوگان پنجم آمریکا هدف قرار گرفته و منهدم شده‌اند.
🔹
سختی بازسازی این مراکز باعث شده که پنتاگون دنبال اسقاط بسیاری از مراکز تروریستی در منطقه و نیز تغییر محل آن‌ها باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/664320" target="_blank">📅 18:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664319">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77125ab336.mp4?token=WQs8LrTsWvwbgzuXDbNuV4jaxkY6AtmqY5oHwQ1faaUav1ju41UBntPr6qFwtspUX4b4p6vxP_1dd830oVtfjJppuUDhVGmXN0EEEXD_bAGae44k-0b5izGC1aao4uoJlZjV3cfRsg0lPPLTBHbc6ro48ppOiWxrCE2TmeUAcgsZvISVGF_XEN-Qeezy_5nF8LectNiLbqawUaE3ahrDCHWpYa-Yt06WCrIPBSEw59WdPRzk7lml1YIxoYXjo3_rRv0FqRUhJQZGqZLFDCimxLgtOZichoc6Lh3HIX3jR_lKUAZx3AHMz7hvdd_muKwDABuOz1fddIUknojSQraE4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77125ab336.mp4?token=WQs8LrTsWvwbgzuXDbNuV4jaxkY6AtmqY5oHwQ1faaUav1ju41UBntPr6qFwtspUX4b4p6vxP_1dd830oVtfjJppuUDhVGmXN0EEEXD_bAGae44k-0b5izGC1aao4uoJlZjV3cfRsg0lPPLTBHbc6ro48ppOiWxrCE2TmeUAcgsZvISVGF_XEN-Qeezy_5nF8LectNiLbqawUaE3ahrDCHWpYa-Yt06WCrIPBSEw59WdPRzk7lml1YIxoYXjo3_rRv0FqRUhJQZGqZLFDCimxLgtOZichoc6Lh3HIX3jR_lKUAZx3AHMz7hvdd_muKwDABuOz1fddIUknojSQraE4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی سازمان ثبت اسناد و املاک: کسی اگر در سامانه ثبت اسناد ادعای دروغ کند به ۲۰ درصد رقم ملک مورد ادعا جریمه خواهد شد
🔹
قولنامه‌های مستاجری زیر ۲ سال نیازی به ثبت در سامانه ندارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/664319" target="_blank">📅 18:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664318">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0688eec0e.mp4?token=J_zF86ya1XD22Bfj1YR82MygTb7hZtPvKNXQSfWA3sqe9Y89C0ffP2UGv3W7q_7_FQNeo82s66pUbQvNC6feQpccouyQiwpXghw281-iLK9Gjn5MEANzTpAxd_D2vIaBAPdPdTZzdmaC8AZ7q8f4kY3Sw5ZQqo5Ns5esmztWMOrGaPMzzWYrqpCmSBnEBSx75uQ--6Xlbg6zYv6jiR6IDRYQZEm8PTU-9iXRTMiXIQVxsU6cwLCW33gE16hitdL841q9MysP9Md9syCp5gvG1Q5ZsbXyD2TSPdLYZE2DjGefMbqdtR-jS8swyIV85-DKZSwF5-Skdi9DmjU-BN8u7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0688eec0e.mp4?token=J_zF86ya1XD22Bfj1YR82MygTb7hZtPvKNXQSfWA3sqe9Y89C0ffP2UGv3W7q_7_FQNeo82s66pUbQvNC6feQpccouyQiwpXghw281-iLK9Gjn5MEANzTpAxd_D2vIaBAPdPdTZzdmaC8AZ7q8f4kY3Sw5ZQqo5Ns5esmztWMOrGaPMzzWYrqpCmSBnEBSx75uQ--6Xlbg6zYv6jiR6IDRYQZEm8PTU-9iXRTMiXIQVxsU6cwLCW33gE16hitdL841q9MysP9Md9syCp5gvG1Q5ZsbXyD2TSPdLYZE2DjGefMbqdtR-jS8swyIV85-DKZSwF5-Skdi9DmjU-BN8u7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دود و غبار دوباره بر فراز کارخانه سیمان تهران
🔹
فیلمی که امروز از محدوده میدان غنی‌آباد ضبط شده، انتشار حجم قابل توجهی از دود و غبار از محدوده کارخانه سیمان تهران را نشان می‌دهد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/664318" target="_blank">📅 18:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664317">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de251a27f9.mp4?token=rc9Qf8R15y10LQqEYpFRl9Dgqm_h418Kz1o-kttSgpRQIDG4BUSDu498cWAtIipt8_JneYbP6sS5Xw3WtpGE0mEqetTTWdcnJpPSSgR5Q8WN2TA2IvNtjJi9X4bPvnHNQ1JSsOeKdP8ttEielQfLyp6chtXz5gMUUEyP6RYK73GBlXUF35lAyGh2EZYtEa9FtDq0Xyvx_-qTDvnFSvCCjNTDmyyy51QwH1Hv31NkS1UtQvwv2OsTkN9s3_wgCoCv2jBZCO5bwx6tNL77i0_fH2LfGcTQwweqrWtTGtXpapjNkyPTJfASwJ5EjLoj0hLQ_4Ipk4iGLfMroI9xXybpe41wWrhG_95cqg4t-FiHb2HNVxIe5SBTPonzz_ZOhh4ixqmyyi1B_T6NGd6IfFApKYN9_1m_5s5jd9BY3cBsjysedEhFq8SI1SJ7DqlHjYH6S9Rv9qqD9NoJhFh9SwOHxRdBwp4ZG6OeH2ueraWNytcrmD5NDLfhBpw8ScIdWJGWHPrw6E03ppqJxFqMbIzGe2iGwM_aTUFRi3vmDMbPyGs8-Jw6iiGkdB7OD_NrdJSJcRfVubLDnC8Xmm5g4q56seRj04VmTPqZKnU687AmV_LoINvKEuyDyt9NUAjkjhD4yEdj3wfZXd3jvWUbMUBHSGySPLhZUFhAv-xkRnDNtso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de251a27f9.mp4?token=rc9Qf8R15y10LQqEYpFRl9Dgqm_h418Kz1o-kttSgpRQIDG4BUSDu498cWAtIipt8_JneYbP6sS5Xw3WtpGE0mEqetTTWdcnJpPSSgR5Q8WN2TA2IvNtjJi9X4bPvnHNQ1JSsOeKdP8ttEielQfLyp6chtXz5gMUUEyP6RYK73GBlXUF35lAyGh2EZYtEa9FtDq0Xyvx_-qTDvnFSvCCjNTDmyyy51QwH1Hv31NkS1UtQvwv2OsTkN9s3_wgCoCv2jBZCO5bwx6tNL77i0_fH2LfGcTQwweqrWtTGtXpapjNkyPTJfASwJ5EjLoj0hLQ_4Ipk4iGLfMroI9xXybpe41wWrhG_95cqg4t-FiHb2HNVxIe5SBTPonzz_ZOhh4ixqmyyi1B_T6NGd6IfFApKYN9_1m_5s5jd9BY3cBsjysedEhFq8SI1SJ7DqlHjYH6S9Rv9qqD9NoJhFh9SwOHxRdBwp4ZG6OeH2ueraWNytcrmD5NDLfhBpw8ScIdWJGWHPrw6E03ppqJxFqMbIzGe2iGwM_aTUFRi3vmDMbPyGs8-Jw6iiGkdB7OD_NrdJSJcRfVubLDnC8Xmm5g4q56seRj04VmTPqZKnU687AmV_LoINvKEuyDyt9NUAjkjhD4yEdj3wfZXd3jvWUbMUBHSGySPLhZUFhAv-xkRnDNtso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سانحه برخورد قطار با خودرو در جنوب عراق
🔹
در پی توقف یک خودرو روی ریل، قطاری در یکی از خطوط ریلی جنوب عراق با آن برخورد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/664317" target="_blank">📅 17:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664316">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
بیانیه جمعی از اعضای مجلس خبرگان رهبری پیرو پیام راهگشای رهبر انقلاب   بسم الله الرحمن الرحیم مردم بصیر و انقلابی ایران اسلامی با عرض تسلیت ایام عزای سالار شهیدان و اصحاب باوفای آن حضرت و آرزوی سلامت و طول عمر با عزت رهبر معظم انقلاب اسلامی(مدظله‌العالی)…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/664316" target="_blank">📅 17:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664315">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
گرما در فرانسه نزدیک به یک سوم جنگ ایران و آمریکا کشته گرفت
🔹
مقامات بهداشتی فرانسه اعلام کردند که حدود ۱۰۰۰ نفر در پی گرما در هفته گذشته جان خود را از دست داده‌اند. این درحالی است که بیشینه دما در فرانسه هنوز به دمای خوزستان و سیستان و بلوچستان نرسیده است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/664315" target="_blank">📅 17:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664313">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m2EGZqYSchc7sSGPXjS27Xu7IYVWmheHx_X4BEzW5x3nXNGApP4ZEegMt660AvBh-P9lTZwXpEZ8ALIUMcjtU3f1wGC3FI92iqQSmN-iqK9vkHKaBU1ddW1iv4b27zZizsLWEWAKZuk69Vj0x355UARzjiBJaxl9VWXCq8C5uUJzqQAwhFdjcWQQBi0nZhWPTlicRIgAOFVI3oSYeoACdYEJrBx2I_8oHkOaANx_11P6P-zpSuZ3JjDRAPXMXLPW6IfbRW1XGdDQm-515U5mIgoRek3aiVsBmmD4wckvmhSDUeO6woNcVKFx1P2W6L79ygh4VSeltPlNDOmgOk_s-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uac6isuWphyOWlqc89FMnksSTCx2PRyqyPNftkWjLmalNEHXmojvgwx9s1MMEMipbbl7SauU_mFdtaiaWRpsr69R0l4VIlN4Y_QTPhe63qz658w-O0XPHcYY4dRRvz8nekSBtOG9HwUJLn51BcwrADahUTAgtmNtxiI7qfr6Sqsz-kVXF3XD9q_tL5meXo-Y_vTD1op2zDyr34z6UUYLd9VDFCj8YSJkOBKDTcqq3LDcJIOKRilCXhf2ZhTw5TD0QeqbHqJM7wpcpQ6ADhdzUhO-Qcdn5x9l5o3zhMqK8okI7GDJ4M7mDi_ZMOP6unRv8SjsYV5o6V52zaBtEOHzdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قایم‌باشک زیر شقایق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/664313" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664312">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iooNyZVB-3YV3SGFI_EH1cGurDVxioVj07j1IOOc8uzDbo4KBgbYK4Nv3Dq9ruMqvwwViyA4XgYNClsLTsz_NyLCTCOFgo7ZKhHouQKs-hte1VdlT-a5rXwMW75e5NJR6b_DGCbEfDExYVaCVaVe9nhXLkfuGMDPkmy2avzbXcOPNmghwWRv8L7lYAuyw2NaOJwvgEyz66n5DQIAhCniIKkg7yw0Ha_t-8bSjBLLNpHND0wDcNzHkS2Drdwgtql_3ukup8S7ECT-tVVsPfFneMDBkI7rv9ewWqp67n2Qgy93fw3_OlNyOZ1sTwkkPZysv_tScp0D7OGmwowOBBx7sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تفاوت بالکن، ایوان و تراس در آپارتمان
در یک نگاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/664312" target="_blank">📅 17:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664311">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
لیگ ملت‌های والیبال/ پایان ست سوم
🔹
ایران ۲ - ۱ کوبا
🇮🇷
۲۵ | ۲۵ | ۲۰
🇨🇺
۲۲ | ۲۱ | ۲۵
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/664311" target="_blank">📅 17:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664310">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ce8a9944a.mp4?token=RKrtuVNWNM0VQXkBgYDL5ImW4XtcO4Axwzqga5KN9OOyS88ESPidlzUfXIZg7_HvWYqDc6aSK94RLfKo-QvzMSQHkMIOFQ4Yv44osYdsjd8fZ5Kc9-9WByoNFD2_ecyYFw3wtF1gZ4aw2ng6WVC3EgckPeZk50TA11PXzuhickz_m-jXYcYJJw5U6Eut3I8oa4BGeLBlg05CGBpD6QxIV0ltL41aBDFM6N2IzTqyhXHJmggqg77AIteza9Wah1hD2TW38COFXk_ImWa5gcHvK332-J2V98lQyA9Tv9Z6AVxWOn0S8-NGZ8J9tiMG7hflx9riAvNUmNE1wQudNlg7Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ce8a9944a.mp4?token=RKrtuVNWNM0VQXkBgYDL5ImW4XtcO4Axwzqga5KN9OOyS88ESPidlzUfXIZg7_HvWYqDc6aSK94RLfKo-QvzMSQHkMIOFQ4Yv44osYdsjd8fZ5Kc9-9WByoNFD2_ecyYFw3wtF1gZ4aw2ng6WVC3EgckPeZk50TA11PXzuhickz_m-jXYcYJJw5U6Eut3I8oa4BGeLBlg05CGBpD6QxIV0ltL41aBDFM6N2IzTqyhXHJmggqg77AIteza9Wah1hD2TW38COFXk_ImWa5gcHvK332-J2V98lQyA9Tv9Z6AVxWOn0S8-NGZ8J9tiMG7hflx9riAvNUmNE1wQudNlg7Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرتاب اجسام مشکوک از هواگرد اسرائیلی در جنوب لبنان
🔹
منابع محلی در جنوب لبنان از فعالیت یک هواگرد اسرائیلی و پرتاب اجسام مشکوک در آسمان منطقه خبر دادند. جزئیات بیشتری درباره ماهیت این اجسام یا پیامدهای احتمالی آن منتشر نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/664310" target="_blank">📅 17:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664309">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
تکنیک جدید وزارت نیرو برای کاهش اعتراض‌ها به قطعی برق؟
🔹
گزارش‌های متعددی از قطعی پراکنده و بدون اطلاع قبلی برق در شهرهای مختلف منتشر شده است.
🔹
بسیاری از مغازه‌داران می‌گویند این خاموشی‌های ناگهانی باعث از کار افتادن یخچال‌ها و اختلال در زنجیره سرد فروشگاه‌ها شده و خسارت‌هایی به کسب‌وکارشان وارد کرده است.
🔹
پیش‌تر معاون وزیر نیرو گفته بود که نگرانی جدی درباره خاموشی‌های گسترده وجود ندارد
#برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/664309" target="_blank">📅 17:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664308">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
قالیباف: با جدیت پیگیر خاتمۀ جنگ در لبنان هستیم
رئیس‌مجلس در تماس تلفنی با همتای لبنانی:
🔹
در گفت‌وگوهای هفتۀ گذشته در سوئیس یکی از مهم‌ترین موضوعات بحث پایان جنگ در لبنان و حاکمیت و تمامیت ارضی این کشور بود.  هدف ما خاتمۀ جنگ در لبنان، بازگشت آوارگان به خانه و کاشانۀ خود و رفع اشغالگری و خروج رژیم صهیونیستی از سرزمین لبنان است و با جدیت پیگیر این موضوع هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/664308" target="_blank">📅 17:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664307">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
تردد خودروهای پلاک مناطق آزاد کیش و قشم در هرمزگان به‌ صورت رسمی آغاز شد
🔹
ثبت ۳۷۶ زمین‌لرزه در کشور طی خردادماه؛ سهم استان تهران ۹ مورد بود
🔹
روزنامه آبزرور از تلاش نخست‌وزیر مستعفی انگلیس، برای تصدی پست دبیرکلی ناتو در سال ۲۰۲۸ خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/664307" target="_blank">📅 17:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664306">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e2f8e78d.mp4?token=UMkO7USLefmrET5teKQUWb9D4udVTwZo7F2VOvwmD05jNLnwcvDeozJrottn9jmbB8jQOFfFuVQSvps68isss9bk5s7j78_0MFItP1D5c6lwYKlZXfSElWr7XiFdZKOCYufMqlO00tjU4mMKyObT9_EKqzq6PWi3D-Hq8u9n6tuqoiuSInviSMosTyjG_EUzhy5pLQ9ch3gJLGjOBDZtF2Lvp6h0Eax3aH5UDOBJen0Glw1Xpuq0uSUC9lu1CEXMX0m-mGfvGnCruFJsjFdl44UPjnPxjRgwlJUItJG4u8bn6SqI0RuujYq5OYXhiVDSHgKfzBo9_0bZCKhJwRYmCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e2f8e78d.mp4?token=UMkO7USLefmrET5teKQUWb9D4udVTwZo7F2VOvwmD05jNLnwcvDeozJrottn9jmbB8jQOFfFuVQSvps68isss9bk5s7j78_0MFItP1D5c6lwYKlZXfSElWr7XiFdZKOCYufMqlO00tjU4mMKyObT9_EKqzq6PWi3D-Hq8u9n6tuqoiuSInviSMosTyjG_EUzhy5pLQ9ch3gJLGjOBDZtF2Lvp6h0Eax3aH5UDOBJen0Glw1Xpuq0uSUC9lu1CEXMX0m-mGfvGnCruFJsjFdl44UPjnPxjRgwlJUItJG4u8bn6SqI0RuujYq5OYXhiVDSHgKfzBo9_0bZCKhJwRYmCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساعتِ صفر؛ تقاصی که گریزی از آن نیست
🔹
ما نه فراموش می‌کنیم و نه می‌بخشیم؛ تنها منتظر لحظه‌ای هستیم که عدالت حکم کند. هر ثانیه‌ای که می‌گذرد، یک قدم به حساب نهایی نزدیک‌تر می‌شویم.  #WillPayThePrice  #تقاص_خواهید_داد #خونخواهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/664306" target="_blank">📅 17:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664305">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7Lf6wYF3hWWRaowJpyhnofAHkjombsUmpdXLtl6r0ZvhLMovc-k3DnKtQLv1xP7b-RKo9cnIuc8W47vqHXVwd51eAhzwjwQR1jsX__kC9rODcfYGn5UUHWDVok6HeJi9OGi3qBZfg0eNFmKaqpI0inxil_nunBLxo5nhvSiKSBqRw7urRfmzGrPDVfhHUNMLjTU9goN9G9tlinJJ4Ugz7hOQYGrB2cjzBfjZHhJkEqOl19Mlu1-kvwPQs9_v5W6_wcKXRGIsmd6aLREuHPToU3uAteUUQHS3KAq_lwmJ-8pTund-qU41tMszHJh-Eq6lKY8LPNZaTpnSUnR9wbnVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکاوی مبانی فقهی، قرآنی و کلامی
#خون‌خواهی
در اسلام
با ارائه؛
▫️
آیت‌الله محمدباقر تحریری
▫️
آیت‌الله علی‌اکبر رشاد
▫️
حجت‌الاسلام والمسلمین دکتر عبدالحسین‌خسروپناه
دوشنبه ٨ تیرماه ١۴۰۵
ساعت ٨:٣٠ الی ١٢:٣٠
تهران، میدان فلسطین؛
سالن اجتماعات سازمان تبلیغات اسلامی
جهت ثبت‌نام، مشخصات و میزان تحصیلات خود را تا ساعت ٢٢ روز یکشنبه ٧ تیرماه ١۴۰۵ به شماره ۰٩٢٢۶٢۰١٨١۵ پیامک کنید.
#ظرفیت_محدود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/664305" target="_blank">📅 16:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664303">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
سفیر آمریکا هم ایران را تهدید کرد
ادعای والتز، سفیر آمریکا در سازمان ملل:
🔹
اقدامات ما در صورت نیاز برای نابودی زیرساخت‌های مورد استفاده ایران برای کنترل هرمز ادامه خواهد یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/664303" target="_blank">📅 16:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664302">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
لیگ ملت های والیبال| پایان ست دوم  ایران ۲ -  کوبا صفر
🇮🇷
۲۵ | ۲۵
🇨🇺
۲۲ | ۲۱
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/664302" target="_blank">📅 16:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664301">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83b9209944.mp4?token=aKFJ6DWtcDl5JDdrMNaNPM9Elbx4aMK7IPxeninnecATZ3_1Qn8YH2N4y3qViOqqVsN33fA1g6lNNthPtjGLdpYy6xRojLZyFgBhjOp7pGAok_Y7xeL6_zuqmAU8poXMMBohdKhKkgMq7J7pBNkqnJAXuq0Eg6zn7ylL-yvW_2vkPH0x4PIyH_jdh9dNWNoQn5fQp0UnSBKbMp4nOTEwfPmYPuq2WysyLyZ8IrySY_WSZjWWm5PQs4kAmYSaerCysOHXLA-6ysblhc_0i8L6YB_NdDeydQif7wG4z5tBv2frsnoS_ezsjuuKtQYNGdObsjB4OUS6tjWOJdmjIqGRjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83b9209944.mp4?token=aKFJ6DWtcDl5JDdrMNaNPM9Elbx4aMK7IPxeninnecATZ3_1Qn8YH2N4y3qViOqqVsN33fA1g6lNNthPtjGLdpYy6xRojLZyFgBhjOp7pGAok_Y7xeL6_zuqmAU8poXMMBohdKhKkgMq7J7pBNkqnJAXuq0Eg6zn7ylL-yvW_2vkPH0x4PIyH_jdh9dNWNoQn5fQp0UnSBKbMp4nOTEwfPmYPuq2WysyLyZ8IrySY_WSZjWWm5PQs4kAmYSaerCysOHXLA-6ysblhc_0i8L6YB_NdDeydQif7wG4z5tBv2frsnoS_ezsjuuKtQYNGdObsjB4OUS6tjWOJdmjIqGRjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رواق کشوردوست تعطیل
شد
🔹
رواق کشوردوست به دلیل حضور ساختارشکنانه‌ جمعی از کفن‌پوشان تعطیل شد. این گروه که روز عاشورا از مشهد به تهران رسیدند، تحت عنوان «خون خواهی از رهبر شهید»، ضمن جلوگیری از برگزاری مراسم روزانه رواق و حضور عموم مردم عزادار رهبر شهید و با سردادن شعارهای تند علیه مسئولان، باعث بر هم خوردن فضای حضور عموم مردم شدند.
🔹
به همین دلیل، برگزارکنندگان این مراسم تصمیم به تعطیلی رواق گرفتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/664301" target="_blank">📅 16:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664300">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-9GoGFrCpf-i7Wz--GhcGKc3HI59ecRiWhu6JRaLlEy83GN0MwQSS7kM3fpMf7m9FIqvLBQewSG_nraeOOegSnBvIcR8UhvRN9Fo5IszWssfxwncmm0GOrpirrzKSWp2Xo9Wt0X4E3RePnz3jx9VXK9zykMECEpES7mWK6QMN75D8kp2D6o2AyxmJxl2R0p3M2a94GYyOAWXi-3-T-SWzdaa4PsKAwurINj1Cqs8hjZEffN5UE-QVaqvBTFos1vgDkyLTubsfRwY-KDFTDRrOLesbYRHOQd2np-04IEdAGRqSAvDWMi6iI2TtEk5ONvv6NpBSQ3_YYwGDA4vf65Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتش‌زدن تابلوهای تبلیغاتی توافق با رژیم صهیونیستی در لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/664300" target="_blank">📅 16:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664299">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
پزشکیان: باید برای مواجهه با سناریوهای احتمالی آماده باشیم
رئیس‌جمهور:
🔹
سرمایهٔ اجتماعی و انسجام ملی مهم‌ترین عامل ناکامی دشمن در تحقق اهداف راهبردی خود بود. دولت نیز همگام با نیروهای مسلح و مردم، با بسیج کامل ظرفیت‌های اجرایی، مدیریتی و خدماتی کشور، تلاش کرد آثار و تبعات جنگ برای مردم به حداقل برسد.
🔹
در سایهٔ رهنمودهای رهبری و مسئولیت‌هایی که به دولت واگذار شد، دستاوردهایی در حوز‌ه‌های مختلف از جمله ثبات نسبی در لبنان و برخی گشایش‌های اقتصادی حاصل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/664299" target="_blank">📅 16:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664298">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/929b4f703a.mp4?token=PTxZL6sR2osG5Ob-M-ApCZVd_T2YnjI6EJStVBhbgXPCdEegBZ6d-DzJsoDMkXgDg4crxwFLz5tt_utrv8duAWhcYubF6M-VvTXAvJrXTBVC81P6m0aVugx815JLWXJcAhdbjsAVFpYQf_XrHPLIkw0gvd2p4DqnCbE1jLBC5GcTdKoozEQV2E92w43etJw1aSDuiMMFN2p_pv_LBHlRKH0__aVo861hKuzBJuyckGU6rljpbXWyLi9ccSwopyB6ZBcbAE_SEiqNxAnGOf40tF3wV7LH8cg97FqEK7hc58Ho8vAcCbUfp_Xr5x3ovJQoEoSDI0GWi6ngAuR0dA6nPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/929b4f703a.mp4?token=PTxZL6sR2osG5Ob-M-ApCZVd_T2YnjI6EJStVBhbgXPCdEegBZ6d-DzJsoDMkXgDg4crxwFLz5tt_utrv8duAWhcYubF6M-VvTXAvJrXTBVC81P6m0aVugx815JLWXJcAhdbjsAVFpYQf_XrHPLIkw0gvd2p4DqnCbE1jLBC5GcTdKoozEQV2E92w43etJw1aSDuiMMFN2p_pv_LBHlRKH0__aVo861hKuzBJuyckGU6rljpbXWyLi9ccSwopyB6ZBcbAE_SEiqNxAnGOf40tF3wV7LH8cg97FqEK7hc58Ho8vAcCbUfp_Xr5x3ovJQoEoSDI0GWi6ngAuR0dA6nPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۲ راز پول جمع‌کردن چیه؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/664298" target="_blank">📅 16:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664297">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه بین المللی نجم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebee81128.mp4?token=Sr5C2hJvO0OerHWUiOzCIHqMkCfXNLFoovOmufEoHN09X1rFsuMVMAknMKagL7iNHhKIGx5XiFZilTmiAZKdnZXUU5d7LLIaLOxZU0bSng7tcmwjIb1qWk3BZcSqV8ccF6pC-FG6yQIh_M63TicDrEufUKPBxB6Mpu9a1Uh9mO3HK-QfkIUuWikyEb4d21AKG1mgOM51fSFjRTztdzhMRCcP2uYhnFzie-ifQyVPECqE-Bmyz-cvlDLYV1a0qZq5l-w9N_WmDa2vJo9gbjUUUjWZF9UithszahAesuhjvL8bYIt4_jhHt2TgC3qNe6pHPDzoQfkj1ciGPdbSbpyKrLCZvSz6FvngUPyAa3Jz39EapoNHNLfxrMK3iElnhrDSFWJ5JLhRSAoJ_lxwxLBcTEAK-JpEA3eutT2Pt5xZ30XTCRytyqMCBuen0WHNqsmNfvI45WvAMxXPufHvr2EffP7Z8QDlAph4UMXNSaYFeqWMeytj6NpvKPxoxwbEmURC6dtHIzN_jGcC4x3dJE7eAkRuABOQoIFOLsKavGkkawqdjTVDo7z7suo7kwVkr1SaC08zUJevLiM2NOmQkFkhozqqh1iz_GdZwFbj3yEFFH9jMEPQlSZrFmdNCOKHvz1kvclrPKbAYdTxz9a-dauF0pIP0VnKmhZeqLzm0tyIKQI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebee81128.mp4?token=Sr5C2hJvO0OerHWUiOzCIHqMkCfXNLFoovOmufEoHN09X1rFsuMVMAknMKagL7iNHhKIGx5XiFZilTmiAZKdnZXUU5d7LLIaLOxZU0bSng7tcmwjIb1qWk3BZcSqV8ccF6pC-FG6yQIh_M63TicDrEufUKPBxB6Mpu9a1Uh9mO3HK-QfkIUuWikyEb4d21AKG1mgOM51fSFjRTztdzhMRCcP2uYhnFzie-ifQyVPECqE-Bmyz-cvlDLYV1a0qZq5l-w9N_WmDa2vJo9gbjUUUjWZF9UithszahAesuhjvL8bYIt4_jhHt2TgC3qNe6pHPDzoQfkj1ciGPdbSbpyKrLCZvSz6FvngUPyAa3Jz39EapoNHNLfxrMK3iElnhrDSFWJ5JLhRSAoJ_lxwxLBcTEAK-JpEA3eutT2Pt5xZ30XTCRytyqMCBuen0WHNqsmNfvI45WvAMxXPufHvr2EffP7Z8QDlAph4UMXNSaYFeqWMeytj6NpvKPxoxwbEmURC6dtHIzN_jGcC4x3dJE7eAkRuABOQoIFOLsKavGkkawqdjTVDo7z7suo7kwVkr1SaC08zUJevLiM2NOmQkFkhozqqh1iz_GdZwFbj3yEFFH9jMEPQlSZrFmdNCOKHvz1kvclrPKbAYdTxz9a-dauF0pIP0VnKmhZeqLzm0tyIKQI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اختصاصی| نظر مردم کابل پیرامون امنیت افغانستان در زمان طالبان
🔸
گزارش اختصاصی خبرنگار نجم از خیابان‌های شهر کابل
🔸
مردم افغانستان: قبلا در افغانستان انتحاری بود، راهزن بود، شبها نمی توانستیم بیرون بیاییم، جاده‌های بین شهرهای مختلف ناامن بود اما امروز امنیت کاملا برقرار است و به همراه خانواده‌مان می‌توانیم در ساعات و نقاط مختلف تردد کنیم و بازار بهتر شده است.
محرمانه‌های حوزه بین‌الملل را در نجم بخوانید
👇
👇
@naajm_ir</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/664297" target="_blank">📅 16:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664296">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
زمان شروع و پایان امتحانات دانشجویان تغییر کرد
🔹
زمان شروع امتحانات پایان ترم دانشجویان دانشگاه تهران از روز پنجشنبه ۱۱ تیرماه به روز شنبه، ۲۰ این ماه موکول شد.
🔹
پایان امتحانات پایان ترم دانشجویان دانشگاه تهران نیز از روز یکشنبه ۲۹ تیرماه به روز شنبه سوم مردادماه به تعویق افتاد و همچنین روز دوشنبه پنجم مردادماه پایان امتحانات دروس عمومی می‌باشد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/664296" target="_blank">📅 16:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664295">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9fb97667.mp4?token=IKophT1VnXS3LfZa2KV-5m7GKR9q4G_mCdEz1RIzj4RLWrTxkz3EYOlHKhsiTY4OqlNei1WpZYavIn5XmAf24NKsXZeRH-4rM-SLtym7qGZ7-6mkmYdLMZAIk3g98G4ELlZxsKap5hXSCW-5bS-1KnwMP3V5EXyKZfhKHVigNm43qEx2fTvGfX_9to8A6UouE550rbi1toNJe4yz4CY_B8fZOOZF2WIN5Y4i7qgbK0wIYAe4AE8ZGeg6SlwWlsOxGaIZszL9ktP8DDPuITUCUd5ZW_zBq7fpGpbGLKcc2Cp6ieEiho6FqijOA8iolYs0MxY-CqvV91s06CiBb52ngw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9fb97667.mp4?token=IKophT1VnXS3LfZa2KV-5m7GKR9q4G_mCdEz1RIzj4RLWrTxkz3EYOlHKhsiTY4OqlNei1WpZYavIn5XmAf24NKsXZeRH-4rM-SLtym7qGZ7-6mkmYdLMZAIk3g98G4ELlZxsKap5hXSCW-5bS-1KnwMP3V5EXyKZfhKHVigNm43qEx2fTvGfX_9to8A6UouE550rbi1toNJe4yz4CY_B8fZOOZF2WIN5Y4i7qgbK0wIYAe4AE8ZGeg6SlwWlsOxGaIZszL9ktP8DDPuITUCUd5ZW_zBq7fpGpbGLKcc2Cp6ieEiho6FqijOA8iolYs0MxY-CqvV91s06CiBb52ngw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای جنجالی درباره یک عروسی؛ حضور ۱۱ دوست پسر عروس، مراسم را به درگیری کشاند!
🔹
بر اساس این ادعا، داماد ابتدا تصور می‌کرد این افراد از بستگان عروس هستند، اما پس از مشاهده رفتارهای صمیمانه برخی از آن‌ها، میان دو خانواده تنش ایجاد شده و مراسم به درگیری ختم می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/664295" target="_blank">📅 16:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664294">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3cc34ee6.mp4?token=jiZfR_LEf4WEF9wkwguXS1rksHXYnU3OC8RzXPSFDMaBq6xR36AJ7KMi5BYvBcbi244JBs2Iwb7BIYRkJVnPR_75mFFROVLnT_hrgEAuuvqEB3wjvo8DjB7snlP954XGfpdwyr5rvyZ879cmB_YWrrP-i7XZ1hz2XnlCxLS92AdEcy-wX_vJSR6G8nLge1-DaUhJQbtvKT9izYjcETlkIuyER4EcZzGQHLkyPU6TMwcJeVZ780om_0-dxxRmGj_A7Ukns-nQJf2rYzPrHW3euOoA58LN2zrK6727tNHtipnxS9SOngnv2U62TTZ4H2s5jMeOJ_0Z3z_OAnEaIzpwHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3cc34ee6.mp4?token=jiZfR_LEf4WEF9wkwguXS1rksHXYnU3OC8RzXPSFDMaBq6xR36AJ7KMi5BYvBcbi244JBs2Iwb7BIYRkJVnPR_75mFFROVLnT_hrgEAuuvqEB3wjvo8DjB7snlP954XGfpdwyr5rvyZ879cmB_YWrrP-i7XZ1hz2XnlCxLS92AdEcy-wX_vJSR6G8nLge1-DaUhJQbtvKT9izYjcETlkIuyER4EcZzGQHLkyPU6TMwcJeVZ780om_0-dxxRmGj_A7Ukns-nQJf2rYzPrHW3euOoA58LN2zrK6727tNHtipnxS9SOngnv2U62TTZ4H2s5jMeOJ_0Z3z_OAnEaIzpwHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابان‌های تل‌آویو از ترس بمب‌گذاری بسته شد
🔹
پس از انفجار خودروی بمب‌گذاری‌شده در حولون، نیروهای امنیتی رژیم صهیونیستی خیابان‌هایی در تل‌آویو را به‌دلیل احتمال وجود خودروی بمب‌گذاری‌شده دیگر مسدود کردند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/664294" target="_blank">📅 16:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664293">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
لیگ ملت های والیبال| پایان ست اول  ایران ۱ -  کوبا صفر
🇮🇷
۲۵ |
🇨🇺
۲۲ |
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/664293" target="_blank">📅 16:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664291">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2a9f660e.mp4?token=BYdowkFpiogERbomzvf80si_uR_LZPuWVBaQg2RIeeGmFhhN74O6QssrNT5ehNqqhBRqhc-q_f2XCPzW1fU6krwIlYcZbOb_h_asvDpwAka-OXZsa3ahdI9q7a40pHOeclHybbHPkAOteKBZ8vtvlPUUtfJf1vmYg1lBbybQKv7TOBHDQMnBNQPtZLn-VBfvYqjqhPEJ7jvXoaT3siAx7m8cS4U98u6TvRtN_Qc97qAoslClIW5UOVWtBAgC-zXJwzkTXh8OXzM0yZTuClA3vItY7bxbaZL7MAyDu96XHo4SBY385WecIYAnnH7F5r_HT3q4pi3vjfvEZ01Zv9hEUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2a9f660e.mp4?token=BYdowkFpiogERbomzvf80si_uR_LZPuWVBaQg2RIeeGmFhhN74O6QssrNT5ehNqqhBRqhc-q_f2XCPzW1fU6krwIlYcZbOb_h_asvDpwAka-OXZsa3ahdI9q7a40pHOeclHybbHPkAOteKBZ8vtvlPUUtfJf1vmYg1lBbybQKv7TOBHDQMnBNQPtZLn-VBfvYqjqhPEJ7jvXoaT3siAx7m8cS4U98u6TvRtN_Qc97qAoslClIW5UOVWtBAgC-zXJwzkTXh8OXzM0yZTuClA3vItY7bxbaZL7MAyDu96XHo4SBY385WecIYAnnH7F5r_HT3q4pi3vjfvEZ01Zv9hEUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتفاق عجیب در مشگین شهر؛ ورود سیل به داخل یک پاساژ
#اخبار_اردبیل
در فضای مجازی
👇
@akhbarardebill</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/664291" target="_blank">📅 16:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664290">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
مردم نگران پیامدهای اختلال‌ اخیر بانکی نباشند   بانک مرکزی:
🔹
در پی اختلال‌ ایجادشده در بخشی از خدمات بانکی، بانک مرکزی از نخستین ساعات وقوع این شرایط، موضوع آثار ناشی از این اختلال‌ در امور جاری مردم و فعالان اقتصادی را در دست بررسی قرار داده است و حمایت…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/664290" target="_blank">📅 16:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664288">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a65fff145.mp4?token=SiK4323shFjbIzxlUMiXV2HSHmbJS7u-9apq456Q3doLWCccxluJdsV66IfTxr_UuOePhTfOQMLGc3eIoAqb5kpSe0pu7XrBopm7JC3S7JRXUv0vrRBAKwh09PNsluK8inrSgNzbozuCbTaqeTuGMxojjz0f9ZbE0bzXfer09Gu0FGbxg9kk1yd4NhJ_o6PdZCUOrClffcjbCKl05h-d-BQYuMqpMq2GgriRMDiMpV0PDSv6Dhl87cwtKeemzNpsI2e7eUIg4Bz3YWIvuuy4mFv_6ekRqz_rJDnHKwP_rKfkxfiAUp5V_KtN_emtrdZgD2nJZkc7ZPKXSLJfjYSpgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a65fff145.mp4?token=SiK4323shFjbIzxlUMiXV2HSHmbJS7u-9apq456Q3doLWCccxluJdsV66IfTxr_UuOePhTfOQMLGc3eIoAqb5kpSe0pu7XrBopm7JC3S7JRXUv0vrRBAKwh09PNsluK8inrSgNzbozuCbTaqeTuGMxojjz0f9ZbE0bzXfer09Gu0FGbxg9kk1yd4NhJ_o6PdZCUOrClffcjbCKl05h-d-BQYuMqpMq2GgriRMDiMpV0PDSv6Dhl87cwtKeemzNpsI2e7eUIg4Bz3YWIvuuy4mFv_6ekRqz_rJDnHKwP_rKfkxfiAUp5V_KtN_emtrdZgD2nJZkc7ZPKXSLJfjYSpgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابان‌های تل‌آویو از ترس بمب‌گذاری بسته شد
🔹
پس از انفجار خودروی بمب‌گذاری‌شده در حولون، نیروهای امنیتی رژیم صهیونیستی خیابان‌هایی در تل‌آویو را به‌دلیل احتمال وجود خودروی بمب‌گذاری‌شده دیگر مسدود کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/664288" target="_blank">📅 15:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664287">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
سید صادق خرازی: یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور قرار گرفت!
🔹
شهید سید کمال خرازی را به صورت استنشاقی در بخش عمومی ترور کردند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/664287" target="_blank">📅 15:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664286">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/037836dcf2.mp4?token=XkXv5iD0a91aVOrYJWlOZsx0_kH0haSPOuh7myBxw91Aw9zn9U18mHuVjopeghSkwDKJNYsTCJYEjZLezKrSyUDHP76RX5On9GYIZgZ6TNvLzQJDfEcPMZnteX4vVq_bR5iXBd4JHhFrwYn8fSVa5f4cTrW84FL_-nHCXCHsrcmrUfu-r-bkY8tPHb7z9drPezRtYzP9LusBzHcG7hycn7xYbkbr5jN5eamPUvyIBbIXORoJu2H_BJB4B0crr9O_A-bhyAOYSsi9oO1cL4uVkmRlutXTt_PWWRs9B8k1ZEtMa4_VUFIaHQaYCF7caohtDo6E_YzPQDCY4sWwJ_ADqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/037836dcf2.mp4?token=XkXv5iD0a91aVOrYJWlOZsx0_kH0haSPOuh7myBxw91Aw9zn9U18mHuVjopeghSkwDKJNYsTCJYEjZLezKrSyUDHP76RX5On9GYIZgZ6TNvLzQJDfEcPMZnteX4vVq_bR5iXBd4JHhFrwYn8fSVa5f4cTrW84FL_-nHCXCHsrcmrUfu-r-bkY8tPHb7z9drPezRtYzP9LusBzHcG7hycn7xYbkbr5jN5eamPUvyIBbIXORoJu2H_BJB4B0crr9O_A-bhyAOYSsi9oO1cL4uVkmRlutXTt_PWWRs9B8k1ZEtMa4_VUFIaHQaYCF7caohtDo6E_YzPQDCY4sWwJ_ADqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ذوب‌شدن چراغ‌های راهنمایی در اروپا
🥵
🔹
موج گرمای ۴۰ تا ۴۵ درجه در آلمان و ایتالیا باعث تغییر شکل و ذوب‌شدن چراغ‌های راهنمایی و آسیب به زیرساخت‌های شهری شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/664286" target="_blank">📅 15:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664285">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vh2uiY2wK0DjEnmgEsfSTI5A9fb3cqz7F1U0fZs1W6IU1bI7gEaU1qqIOt5QbJqQoW_uChLEKQ-tNCaViUqeZrV-kfwwCO1ZT8XIgK4n1uHiQ6XMaQT2LCC80NHSKdmgRWGOcDBTz8fuvBY6PaE0oG2hGwE0JxdSkvA2yaPCzYgKpY2p0-NWLCbbAWdBI_uzPjF_E_1yzax914PQZBThqFc_Lk_tH9v0CowQuGCFi0oqZdXK4Dq2Fd3mAAf5jt59nEY5tjPJfssGrYhoA-OGaeM3QZ2nbcEqCnsmkj2did3gOt68w9ztvldMAml2cjNTfL3uiK8TlbPw0x0IgCFKNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرگ خانواده فوتبالیست آرژانتینی در زلزله ونزوئلا
🔹
لوکاس ترخو، فوتبالیست آرژانتینی، در پی وقوع دو زمین‌لرزه در ونزوئلا همسر و دو فرزند خود را از دست داد؛ پیکر قربانیان این حادثه پس از ۷۴ ساعت جست‌وجو از زیر آوار بیرون کشیده شد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/664285" target="_blank">📅 15:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664284">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
لیگ ملت های والیبال| پایان ست اول
ایران
۱
-  کوبا
صفر
🇮🇷
۲۵ |
🇨🇺
۲۲
|
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/664284" target="_blank">📅 15:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664280">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGK1-o1D7r3At_-MIVDgu3Bz7kvRdPvvCLNuDDXs73WPox12iC6FyhJkTa7eoTkMUZcqEnbIsjDUwISpqrOgpKAxQAXjnNxNk65o9pBG8uEQF0gVR8zhVo6nGIejr2G7YcZnWiPZk_5L8nai-uT3uK_WXkl8XIubFzvPUlhTGNVQeTC6Hzj1NeuMukMPo8vuKHGoDMRUCRHh0dgITKQCt4LPqrOzdBzn20p2YDEjprxww4flr9lZOF2XPgMeWBk5xK5SEeACGnYNVLI5NsLgisTOPPc0MoRqgyZ4pzyAP24YF1IvY4I9el23qKKYun010_L-M9Vde_Y47NuTcd76JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cb9bDO2ZsjQ-uXgQW0Wo29v7-zD1l4XnlTyFNavT8k_ytgU0vg2aiy0qK4IrU5yvLeKER1T2DeawCT95tRnrwfQH2B11tfPAtoTKmpB0BuBw9mLJLBufJIXnoraLce1pOFKhFhW-wMxDXHSQxDdVPxGycHGe8dTtmey0MMPFAXOuCghZfRJ4Po9l6ESeedVJuFwwbYcuUp0oQtv3eWkr3Gsqyq7d1zaCQmjiRrwhFZ3zs7RrMMoadmdjmO5AVuF5lNmP21lChHvAtrePA46jxKV9grS5qa1AIqdtrK8-45DzCuHSURoSpiNWJlgKitLW5AjQlvwKCteQj0HTwdvkXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kfz7Hldz1-9BBk-fIts0oK_VKrDRTiTGE5Uhaayg89mdYvyQvH7zWhgl8i3IlCpBAcbjewJ_3idC_uFe5FLj5IDQ_02k3-YfouJL3qggMhuD3TpzBwNcYhSKLgT7Eb-c3E6fTbuMeJvPJvz8pizXKDH_BJef9VI98FQDCo_a1_WH8_1LRCuf__732yLSeWB0y8QNQidAT9apakiBeed7ajCjRpP2BbDRzva-3GBBzxYXj62jilqeQTWnhJWjcOS3iE9Es-yXUsB5Q0Z7HtHyQQONT2pEBbAVaYi38FQsSO_-QjSbX9VcxaxLFK-AQyxMEPGkUWH89B_T8v0LkuwVDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4C7S4Gy94qy5MWHYsCvLQQTt6CYHNGPWeRhu6aqn5Htl10sE6Zo748Oxx4RT8nuFgYujMhSjiRX4hdcuK1VF1AiRsSHFTD64a8B8RLAAzd7VfVDJBnHvcaOgtvekNr45x7jQ6g6j_D0VDdrRhu68B_9KB7o-0pbGalmk4_Y-_gsBN3sSgdupDMYspKN14qPQuU69xsJ35wwhmNzsOyecnlHF-oKOy1_ElKtBEzhuaqqhkPwKzZFvBT9MuEN2qkr0ZU_gSuXK7zab1aAYvV7G1gp7uh0IzwoBqeffQ_yx5FMvLHCCwmAFsmGzlzUDCclG0owYVELPDXkTARK4xsxIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
وعده‌های بی‌جای مسئولین، برق خانه مردم را قطع می‌کند #برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/664280" target="_blank">📅 15:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664278">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635706bbe7.mp4?token=Aa65AqjvfF7nmsCpko2Nn_D5oKl80ZgngDsrHOmW9M_Sk35mCa3gYk90rPeTHTvFbm2HW0uottrGcEWNhodzFE-qGrfVqPSp5U5o4hOsrx2i7iy1T2AfvykjB4o4JHRn1NSlUmnzVz12tlQvFYBxthaULVbObQaWpToh8w_ayjfoK6Q7n3SZvf-EvzuKracz-KIKuAIEWlw830K7TrUT8FKGkberGtoWUdyjGtienrDWWlz5TfMNEkPQFFTnN05UVHmOXZqexlRg_MgM1v_Z71aTPBAmmy4vKsLZfTJtjMSYP2rl26OTh0WBFq2Pa_YLME3zp_nY9y1egRnOZgJskpCWLOL63kRxyeACB_ToPnHhrh_CAe5r9IY_7M3Io7ILz1deTkfyG1rsTu_AQ5eIhkl_5wHHca3xQAsW6LzJKmD2diQlfpjYuXSw8U3qwsZomxJ35ZJ7-OrfFqum3Rlx3vwSwY95TE-N8FlzBCVhck3rPvi0PO9TEH7s8BPYpw08UXyqDXdRQ58JXZb08s9w85E0Gth42lftvfIBTlpdm22xVVNPepuBt_nK1mhdo6fXjvIcqBccLT7BhDJZSi2odyAWwNposNjrsuC8edO5x_sPiygKaNA0P3UkcMID3L7EbfSyRsdoDXs-oZkUgbUFqdvbWRBiExJvj06714X9Ips" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635706bbe7.mp4?token=Aa65AqjvfF7nmsCpko2Nn_D5oKl80ZgngDsrHOmW9M_Sk35mCa3gYk90rPeTHTvFbm2HW0uottrGcEWNhodzFE-qGrfVqPSp5U5o4hOsrx2i7iy1T2AfvykjB4o4JHRn1NSlUmnzVz12tlQvFYBxthaULVbObQaWpToh8w_ayjfoK6Q7n3SZvf-EvzuKracz-KIKuAIEWlw830K7TrUT8FKGkberGtoWUdyjGtienrDWWlz5TfMNEkPQFFTnN05UVHmOXZqexlRg_MgM1v_Z71aTPBAmmy4vKsLZfTJtjMSYP2rl26OTh0WBFq2Pa_YLME3zp_nY9y1egRnOZgJskpCWLOL63kRxyeACB_ToPnHhrh_CAe5r9IY_7M3Io7ILz1deTkfyG1rsTu_AQ5eIhkl_5wHHca3xQAsW6LzJKmD2diQlfpjYuXSw8U3qwsZomxJ35ZJ7-OrfFqum3Rlx3vwSwY95TE-N8FlzBCVhck3rPvi0PO9TEH7s8BPYpw08UXyqDXdRQ58JXZb08s9w85E0Gth42lftvfIBTlpdm22xVVNPepuBt_nK1mhdo6fXjvIcqBccLT7BhDJZSi2odyAWwNposNjrsuC8edO5x_sPiygKaNA0P3UkcMID3L7EbfSyRsdoDXs-oZkUgbUFqdvbWRBiExJvj06714X9Ips" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت ونزوئلا بعد از زلزله های مهیب چندروز پیش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/664278" target="_blank">📅 15:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664276">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0lSW-c-FCMBGx2CbaFV-dNfXXJpzPi__pNVpRZRjLN8Fs3LR4mdtja6IdnPEJZQwBgHD-A-xreI28fdK8G7eKPT-0GbJa-Y5aW-a4gWlCiPXcnftatydrP7jXcljAWHAzqPDlTo69-LKQLpkJvF63TDZwaCT87hmD3bmYsbH-Lx-WCqq2-pf1IaDSOglXtdE-zzHn1hbiS7U_MPMfx9Yv9MlkJMrMDVWZrfAwzSsNUWUCv_T6TpN_N8Nk-n3QnGsqLzvUvxt6iqY9yorqUXXP7R1YhvekBuXY_2tjRE4duN1bSD72LYqng0s26cXXfTkEFJpC94cSO3iyzaBw_DSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جکسون هینکل، فعال سیاسی و رسانه‌ای آمریکایی: فیفا از هر ترفندی برای متوقف کردن تیم ایران استفاده کرد؛ فیفا یک سازمان صهیونیستی همجنسگراست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/664276" target="_blank">📅 15:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664275">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICWiszix4imzQj-kVWBWKwxTReG9ey4RdZHCCbwSXOUx7QCP-_42PpgDL7EhSVzegN7UBUvJFbI4GrRWKCpX5YivyubZT8kJFnSOjvicbyESVWkNhYGs_g6l5nLBvXcrAe4n15DVHoD2p6b8SaAsPjlg3VKYvXQSttNlSWntQJr7bmlbMFQIQyXYIPbtBRCGUCehOrIGZdDgDE5To2dBOyw2EPgfaubIzpmhB-4DuxO046G7ZKgeNFppiZq7RHNPQmKlozZmoc9mO-ybDy-oPX1SCA0FvtbJt91Py_RqQeJd3BThDuUpmvyWlo2CvbXTtKU1OaSdO64ZXCyv3iyDug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ دقیقه استفاده، ۵۰۰ سال آلودگی
🔹
یک بطری پلاستیکی را فقط چند دقیقه استفاده می‌کنیم، اما همان بطری می‌تواند صدها سال در طبیعت باقی بماند، به میکروپلاستیک تبدیل شود و در نهایت دوباره به سفره غذای ما برگردد  شماهم به این پویش بپیوندید
👇
#نه_به_پلاستیک @Ertebat_baforii</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/664275" target="_blank">📅 15:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664274">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6zClQ8JD_wpZv1bROvxYQ00MffYn4RW9-NtTKTS5NxbA_SRH5zP039p9JoZPGzjMai3Fi8tkZsLwfgcsFTcht6CFWVdGQIgffJC356C6soH4l4xbHQV2bMoFSICKVQWY2aOmmE-8tR_dNozmjbECm7eBjjjGaZGsm-a8wysQDkiLezKi_0OK-_HYskk5mOIqzIdcj17UHcUnOrz_pJZh-tGyvPXBXao7eVNEDeu2VPvSYJEeMaQd9bX3Yok64SL73myW6Ka2XFDO9GZdfkLbDqkcdf-6DhXx73lFjceigLm8gysiLOPzxI4XLe8gSdJGDY03K3eUhIF2IoI4ydkFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کمجا‌چوب مرجع تخصصی مبلمان تخت خوابشو و تخت های تاشو
✅
فروش ویژه تخفیف نقد و اقساط
مبلمان ال و تخت خوابشو
سرویس های خواب تاشو
کابینت و سرویس خواب
جهت رزرو و ثبت سفارش و بازدید حضوری
☎️
02122141020
☎️
02143000098
جهت بررسی محصولات با ما در ارتباط باشید
🧨
❗️
https://t.me/kamja_ir
https://t.me/kamja_ir</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/664274" target="_blank">📅 15:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664273">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
دادگستری استان تهران: تعاونی اعتباری منحل شده و در حال تصفیه مولی‌الموحدین هیچ گونه ارتباطی با موسسه خیریه با همین نام ندارد
🔹
روابط عمومی دادگستری کل استان تهران در پی برخی برداشت‌های نادرست از اظهارات رئیس‌کل دادگستری استان تهران درباره پرونده «مولی‌الموحدین»، توضیحاتی را منتشر کرد.
در این اطلاعیه آمده است:
خبر اعلام شده از سوی علی القاصی، رئیس‌کل دادگستری استان تهران، درباره صدور حکم ضبط اموالی به ارزش بیش از ۲۰۰ هزار میلیارد تومان، مربوط به پرونده «تعاونی اعتباری مولی‌الموحدین» است که پیش‌تر با این عنوان ثبت شده و در حال حاضر منحل شده و در فرآیند تصفیه قرار دارد و اموال آن نیز به بانک ایران‌زمین منتقل شده است.
🔹
تعاونی اعتباری مولی‌الموحدین هیچ‌گونه ارتباطی با «مؤسسه خیریه مولی‌الموحدین علی بن ابیطالب (ع)» که در استان کرمان در حوزه امور خیریه فعالیت دارد، نداشته و خبر مذکور ناظر به آن مجموعه نیست.
🔹
توضیح حاضر به منظور تنویر افکار عمومی و جلوگیری از هرگونه برداشت نادرست منتشر می‌شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/664273" target="_blank">📅 15:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664272">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e7054476.mp4?token=rsWunR_yb5Ifye5VX38zXutHchnFLRqSDIK0gRBVT63sLyp-V64SFOgVaMKknMD1v49xXifAxEHiNR8ToKYjrnOYq7t23QrnnbQ4HHxrD4Y5aUkCyCkYM2gp6Jdacm3IQAPXCpEwE5JMD7WnpHJmUzfmrmdr87HBPkw8syvRprvDBwzooR-GIcrGwNxkfaCbjmSb-Gv6bWvPtu6LAezeqoCf9gDPO-AAAsxumhXgnZTrQJwxykWpMpSdZNYDqGMp-8xuC9zyrO_sqI2w3M1ClsyKigTTJ3mOGoiIkDBKNIoYFdrRHOa-YIQj2aumUEC3V1C6C5SJBohTUYIqNjy-qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e7054476.mp4?token=rsWunR_yb5Ifye5VX38zXutHchnFLRqSDIK0gRBVT63sLyp-V64SFOgVaMKknMD1v49xXifAxEHiNR8ToKYjrnOYq7t23QrnnbQ4HHxrD4Y5aUkCyCkYM2gp6Jdacm3IQAPXCpEwE5JMD7WnpHJmUzfmrmdr87HBPkw8syvRprvDBwzooR-GIcrGwNxkfaCbjmSb-Gv6bWvPtu6LAezeqoCf9gDPO-AAAsxumhXgnZTrQJwxykWpMpSdZNYDqGMp-8xuC9zyrO_sqI2w3M1ClsyKigTTJ3mOGoiIkDBKNIoYFdrRHOa-YIQj2aumUEC3V1C6C5SJBohTUYIqNjy-qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اهرام جیزه، مصر
🇪🇬
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/664272" target="_blank">📅 14:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664271">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiLRzelanxYlQDg7WH06SdiV_zvuoD0knvWOZcVzTFmXulUJT9-9J2rczpSnsx829KFNOzzsT7h88HuGHcQauXD4fLHtEGlVR0VLRPuQPwKJjfIfcCMIPiCkFuohZpie4YfvnsQfd11Rg6SgQz2wjDNRfeGvHGatGrv1G3SJV6Kl372yd-DUY0tTiYKt1M2psNkgF0lwI5QBTqoP0aWQy8V4C2GYbXuzZhRoQheVAFuEVola_DrQ2VdMNRhg-4YUjefiMx8P2gjNwrvJ1ZUvl9tFuxnmRkMe3-nQG0m1r--OxlcX5QB5fKvPOhR-wiviU11O9Izb0bKr24YOQOFg4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان دسترسی به خدمات سلامت در کشورهای مختلف چقدر است؟
🔹
کانادا با کسب امتیاز ۹۲ از ۱۰۰، بالاترین میزان دسترسی به خدمات سلامت را در میان کشورهای منتخب دارد.
🔹
ایران با نمره ۸۱، وضعیت مطلوبی در شاخص پوشش همگانی سلامت دارد و بالاتر از کشورهایی مثل ترکیه و عمان ایستاده است.
🔹
افغانستان با امتیاز پایین، یکی از  کشورهایی است که کمترین میزان دسترسی به پوشش همگانی سلامت را دارد.
🔹
اگرچه برخی کشورهای آفریقایی پایینترین میزان را به خود اختصاص داده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/664271" target="_blank">📅 14:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664268">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KbFepfWTiTJNigWkKEjP1d_3NBnO6EL-zDrnK4z_K4qBtd9pAlCXi8ByejVaEVXYkc-6LyF5SetYHNECTQF1QSfwIfeyH5swDq5QXLElgef_AWWqQ53jtA38uzC5St0STgJ91EyR68XyjlYaYZu8dT-9wp_sBvGZs8dKAsHMx6HqNbq_-NagLgD8S-Xf1krlP6y2JfTTyCjTynsWGbl-Kz8H83Sw5Kucohz8OhMzXT7-Xx0_in-QYGfWdkqRAPDG5OvRzdsFgTILfkvEgvtnTw-EqpuRjkGDAja7BC7rs0VjtdMnLf5BLd-s-rDGX0VjoYagTJIVkmZkziu9K-FpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSy0awH4jZpD2joUPIXkEo9w2Isk13StW6RgB4RSydH09HfH4zVkHF3baxjkxugF_wiaHVXtyDOLI4rb-oeDtfV-inrgEvEyvlrzLQPr8gOdnqUfcTa1Hgs434aVnc5BI2vT7KdkMRGP23B2I63MPPCTIUo1Q_KuU5C75d4jgaT9kOPQkvLH1CNq8u0pzlgKL1Ahgtr2T_plbBk1H_Ik3hrYOgrjlNS2n2OGVEzgteMLpgeShA1RARVt2lVfXsXHH1Mp47C3-MMkV1ICaEJAVjMH_xdEXDlH-t_UtXXjCZXNNap69bVRlJV4DRwkaY-AGUkwj20-TkPeTqr5G1dq9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سید عباس عراقچی وزیر خارجه ایران در بغداد با علی فالح الزیدی نخست وزیر عراق دیدار و رایزنی کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/664268" target="_blank">📅 14:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664263">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
توقیف تمام اموال ساعدی‌نیا در نوشهر
دادگستری نوشهر:
🔹
اموال ساعدی‌نیا در نوشهر به‌دلیل اتهام حمایت از اغتشاشات و ارتباط با جریان‌های معاند، با حکم قضایی توقیف و برخی دارایی‌های او از جمله یک کافه در شهر پلمب شد.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/664263" target="_blank">📅 14:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664261">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yh423HnbMt6Y1oe4n-j-IL9N5a5XsZaG49jkv0I6swj61GdD7a0ExnzOiOP6SLuX3tf-lQmcgqNnNpWBxk75t6YTz2CcNBIiT7siciPirUKadg3fZhaTyiw2i2IuXZEeEwXLQ1-O6laIomEu_UAiGc_yuOuZszk5P7odO4dKQmX-lJ8vimcdw6PvyRelBykpl14LDUdQ1V94Kf_T_7HlaqCk3W6f7dykH_TmSBDqLRqYV_5lxArxIZdKIBZ0CPjSf7dNv9o0Y21odp_XTWr5X3582Nkl_GJdELXQs-dNztp6p3fwPgAkgufbD1n9nlQih0pCqMIQjHhU-V2DmpdLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور علیرضا بیرانوند در میان بهترین دروازه‌بان‌های مرحله گروهی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/664261" target="_blank">📅 14:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664260">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkmgGWaGX4ethjbguG8lnpHkQIb5XwArH9kL2e-BZ4JZQ02fU37mK_31p-G0gYAae0fssODLcPoefBstBm2DWCrs4n1I014mDyYMod1ZVx0XMEL6OxSUFKOzK3JmHxuhvPfiAGJvu3UFxBuMP4tV3GxJVyVm6uLnso5VKLe4uKqr-XH4TrQ-Anu4bCNI7npCmVgDjkyeG_AiIamWRAqAofkOdtRH8YtKK1eeVsKiByMyw_LYpeYLEfIAWhuMFi45QIjl0RkT8OqJ0C-C5fvvK9uUPYgaXOfIIwEmCIBQhFfboOLPoo--7kgE2n4CtSf-A3uZJcSHgQDuY8m7iOJAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امتحان نیست، ولی بد نیست معنی کلمه «مالیات» رو بلد باشی
🔹
هر روز یک واژه برای فهم بهتر جهان #واژه_کاوی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/664260" target="_blank">📅 14:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664259">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tle12Z-jqC3gXczH1yWNIhxJvYF40GvpB9jUf1GWBwySm9YxKCL7cFb5HqHtpbnzoAlKa0A98DSZMYMVabZOKaOJRW4VIZLeW8bRl_sS37_S3Hcq_6_uJGOGGfbS6z037WzqUuO7sKjuVHSDbM-Rc8daRJeWezwlrne03cqdtHVUs9uJ8_E311Cq5H701O4YhkTp4FWIbfkkcEZR-QrP4POYoYjOinLWWcQpYAxVKi4OUW3gkui3PWCyJl3VnR-Z6EzG71WqPNIZB50qQpvgFIEuLth84hBN0ECQ8umNGHgYmnGzHPgJYhvd5yP4ZfzLY4RHxs11R8Q5G-1aOWzrAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سید عباس عراقچی وزیر خارجه ایران در بغداد با علی فالح الزیدی نخست وزیر عراق دیدار و رایزنی کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/664259" target="_blank">📅 14:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664257">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3oWHTyotPuLiJTpGS6l9SjSbfZgW_-a1CDjsuIthUCtIB9of2jbwfsImjRLqymMiMPIZ7ey109dE4nuL5SoPqCOvIJ3_GGo9zP3c7gyTM6zo_34Ge7A8A4jPA14O6EEr7bMIouACxKaDH3IlSaCuKkGGuZF57lNo_xNMFl2_hh2OY1_6dApjRuBELM6kllJaIIz2c_NKfizMnb7vtsWMcp0OPpzvrOCBMe8QAr2k4bkcUqTTamzdxA_dDdF5fls5XMz4E6MKzZt9Top9dHba7XeowlE6cBOqBrFxIEMXMs2qXipDvHgI11K4w1fNVPnkVQnxFMRaFSkz0hn6V7riA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
حضور مهدی طارمی در میان بازیکنانی که در مرحله گروهی جام جهانی ۲۰۲۶ بیشترین تعداد تقابل‌های مستقیم با حریفان را با موفقیت پشت سر گذاشته‌اند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/664257" target="_blank">📅 14:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664256">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEGZVcGsJ7wCfXvzfcwYyiip6U08hHm1kicTkQW0XsB-bwpQvdITK4FuYQasJzWqPlpRPpCUOAPHpXUEyQc1Bik1bJrYNrf3kzPKJ4ZZYwgnhMTH7Sxh5_QA7H2380VD9WkTwGgv84yg10KmDp6PQgwtiDpV8TpmisEH445GCeb03ONSC6Mn3DUP55TzAb0-n7ILxNxBrhkonswFC7yMrrrbhDbvGKhh9dGRtJojKy7kcPHdcje0ALbV5vJCbHFK4MagHf9aJyBrRk8-cuNn7AgMYwZTvRjPdGacklvYToYDRmXSSDsFT01-qgTRS9-BXkhfkaZCR2Y5a10z5SLnlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وعده‌ها کنتور می‌اندازند!
🔹
با وجود وعده وزیر نیرو مبنی بر نبود خاموشی در سال جاری، قطعی‌های مکرر در نقاط مختلف کشور خلاف این ادعا را نشان می‌دهد.
🔹
مردم انتظار دارند مسئولان به جای انکار این واقعیت پاسخگو باشند و راهکار ارائه دهند. #برق_مردم_کجاست
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/664256" target="_blank">📅 14:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664255">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPEsCBo8zhBkX7R-ufzR0qJkd0DTi_HKC4_ZFF8PwbA39OeYrDiJqL80zu3NKa-uOoa8zwZdiryoNi1emXr0mpu3YgkurL8dbepJe3bCkYYgZR4932NcGt0iH71zuaCRF-d8J0XgPB8rUg_oaX_knimOMK9NOsqT6PdgfvrZbIi1_AOVgQRQtxQ9h6hPjGkq3Hox_1quHW1JdLEbkGOLspvPXiaz1X_upbE0WFjf9Bg7KS6o0RaDa2FpD_l72DLhxXokLKKaDzyhAr03oNBpz6u2TwCcXgQmqNhzPOhOV0j6v4AvoTBhqpK0YaVc-5_3HTE0vH7sOuGK61651oU27Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای
پیشگیری از گرمازدگی چه کنیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/664255" target="_blank">📅 14:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664254">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔹
ثانیاً لازمه‌ی توجّه و اهتمام به اجرای دستور رهبر شهید انقلاب در آخرین دیدار مسئولان قضائی با ایشان در تیرماه سال گذشته نسبت به رسیدگی به جنایات صورت گرفته در جنگ تحمیلی دوم، تسرّی دادن آن به جنگ تحمیلی سوم و پیگیری مستمر آن تا وصول به حکم و واگذاری اجرای…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/664254" target="_blank">📅 14:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664253">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وچهارم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای محسن اسکندری که در سانحه آتش‌سوزی روح از بدنش جدا شده و توسط موجود عجیب و حیله‌گری در بیابان برزخی هدایت می‌شود تا اینکه به ناگاه متوجه اشتباه بودن راه و حقه آن موجود شده و از خداوند طلب نجات می کند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: محسن اسکندری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/664253" target="_blank">📅 14:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664248">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
متن کامل پیام رهبر انقلاب اسلامی به مناسبت هفته قوّه قضائیه و سالگرد شهادت آیت‌الله بهشتی و یارانش
📝
بسم‌الله الرّحمن الرّحیم
🔹
ایّام مصیبت آلُ‌الله و شهادت حضرت ثارالله صلوات‌الله‌وسلامه‌علیه‌وعلیهم‌اجمعین و یاران باوفایشان را به همه‌‌ی ملّت ایران و امّت…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/664248" target="_blank">📅 14:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664247">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
متن کامل پیام رهبر انقلاب اسلامی به مناسبت هفته قوّه قضائیه و سالگرد شهادت آیت‌الله بهشتی و یارانش
📝
بسم‌الله الرّحمن الرّحیم
🔹
ایّام مصیبت آلُ‌الله و شهادت حضرت ثارالله صلوات‌الله‌وسلامه‌علیه‌وعلیهم‌اجمعین و یاران باوفایشان را به همه‌‌ی ملّت ایران و امّت اسلامی تسلیت میگویم.
🔹
نهضت و قیام حسینی برای اقامه‌ی حق و اصلاح امّت و مقابله با ظلم و ستم، قلّه‌‌ی بلند تاریخ در تقابل حق و باطل، و عدل و ظلم است و درسهایی بس ارزشمند و فراموش نشدنی برای همه‌ی آزادگان جهان دارد. خون سیّدالشّهداء علیه‌السّلام را خون خدا می‌نامند که در رگهای عالم جاری شده و حماسه‌های حیات‌بخش می‌سازد. نهضت و انقلاب اسلامی ایران، از آن‌رو که شعبه‌ای برگرفته از همین سرچشمه‌ی نورانی است، باید همواره در پی دستیابی به اهداف قیام حسینی باشد. هفتم تیر هر سال یادآور شخصیت برجسته‌ی انقلاب و آن کسی است که با قرار گرفتن در رأس قوّه‌ی قضائیه در این جهت تلاش بی‌وقفه‌ای را در پیش گرفت تا آنگاه که با جمعی از یاران مخلص انقلاب شهد شهادت را نوشیدند و مظلومیت او و عدد هفتاد و دو شهید همراهش تأییدی بر حسینی بودن این نظام و معمارانش گردید.
🔹
شأن قوّه‌ی قضائیه در نظام جمهوری اسلامی ایران، پاسداری از حقوق مردم و احیاء حقوق عامّه و آزادیهای مشروع، مبارزه با مفاسد، اجرای عدالت، و اقامه‌‌ی حدود الهی و نظارت بر اِعمال قانون است. ثمره‌ی موفقیت در این مسیر، علاوه بر کسب رضایت الهی، تقویت اعتماد مردم به این رکن نظام خواهد بود. انتظار بحق از همه‌ی قوا، دستگاه‌ها و نهادهای مسئول آن است که همواره عملکرد خود را با تراز مطلوب نظام مقدّس جمهوری اسلامی و شأن والای ملّت، تنظیم و بازآرایی کنند. در این زمینه قوّه‌ی قضائیه جایگاهی کم‌نظیر و بلکه بی‌بدیل برای اصلاح روند امور و به حرکت درآوردن سایر بخشهای نظام دارد که این مستلزم پیگیری روند اصلاح و بازسازی در داخل خود این قوّه نیز می‌باشد. اکنون انتظار عمومی جامعه آن است که شاهد تأکید عملی بر این امر در عملکرد قوّه‌ی قضائیه باشند. به‌ گونه‌ای که تحوّل قضائی، از کلمات درج شده در سند تحوّل و طرح‌ها و نقشه‌های راه، به فعلیّت رسیده و جلوه‌های آن در همه‌ی عرصه‌های مربوطه، از اتاقهای مجتمع‌های قضائی و جلسات دادگاه‌ها تا محیط‌های عمومی و فضای اجتماعی نمایان گردد؛ آنچنان که مردم آثار مثبت آن را در زندگی روزمره‌ی خود در قاطعیت مقابله با انواع مفاسد، کاهش تضییع حقوق، سرعت رسیدگی، ارتقاء سلامت و اِتقان آراء قضات، و دسترسی آسان‌تر به شاخص‌های عدالت مشاهده نمایند. در این تصویر از قوّه‌ی قضائیه باید اجرای عدالت به پایه‌ای برسد که هر مظلومی آن را مأمن خود بداند و بخصوص کسانی که به‌نوعی از قدرتی برخوردارند، جرأت تعدّی به حقوق دیگران را نداشته باشند و باب سفارش و توصیه در آن به طور کلّی مسدود شده و داشتن آشنا در بخشهایی از آن هیچ مزیّتی بشمار نیاید.
🔹
البته احقاق حقوق ملّت، تنها در مسائل فردی خلاصه نمیشود و انواع حقوق عامّه و اجتماعی آنان، از حقّ امنیت اقتصادی و دسترسی عادلانه به فرصت‌ها تا حقّ برخورداری عادلانه از مواهب طبیعی، محیط زیست سالم، آزادیهای مشروع، و حکمرانی کارآمد نیز از زمره‌ی مسائل مهم در جهت گسترش عدالت قلمداد می‌گردد.
از جمله یکی از مهمترین مسائل حقوقی و قضائی مربوط به همه‌‌ی ملّت ایران در این برهه‌ی زمانی، پیگیری و احقاق حقوق تضییع شده‌ی آنان در اثر جنایات مجرمان بین‌المللی و مستکبران و تجاوزکاران جهانی بخصوص در سالهای ۱۴۰۴ و ۱۴۰۵ می‌باشد.
🔹
از خون شهدای مظلوم جنگ تحمیلی دوم و سوم تا صدمات و لطمات جسمی و روحی و مادّی و معنوی وارد شده به کشور عزیزمان و هر یک از آحاد ملّت مظلوم ایران در داخل و حتّی خارج از کشور؛ از کودک‌کشی‌ها و جنایات جنگی بی‌سابقه در میناب و لامِرد تا حمله به مراکز درمانی و خدماتی؛ از کشتار نوزادان چند روزه تا کهنسالان عزیز؛ و در رأس همه‌ی‌ آنها شهادت شخصیت بی‌بدیل، گوهر بی‌همتا و یگانه دوران، پیشوای مجاهد عظیم‌الشّأن اعلی‌الله‌مقامه‌الشریف، هر کدام پرونده‌ای از صدها و بلکه هزاران پرونده حقوقی مهم را تشکیل میدهد که در محاکم قضائی داخلی و بین‌المللی باید با جدّیت دنبال شود. آنچه مسلّم است گریبان جنایتکاران را بایستی گرفت و آنان را به سزای اَعمال مجرمانه‌شان رساند.
🔹
نکته‌ی مهم در این مقوله، اوّلاً اعترافات و حتی افتخار وقیحانه‌ی بعضی از سران دشمن امریکایی، صهیونی به این جنایتها است که قطعاً اقرار به جنایت محسوب گشته و مقدّمات احقاق حقوق تضییع شده‌ی ملّت را به شکل مناسبی فراهم ساخته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/664247" target="_blank">📅 14:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664246">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlXDlKl1_YWHnuYVTbyXJfAsbUyLZg-IVdXVX1fl5Z73bGPAw_ld3jsGsoKEfsi3Mm_kdJNNBTTalBTHme2V7M8bpH7H0C--1cz_6iWYBKsyeta2-nZ89gJERED3bkTWcsQsjAc1zqQqkiBtL_ZV5jmjUaJNi_lzu1EiDQKXL1QOxaXzKIgyqLnFPYgGhgYkIgD-ITRbL2YjrQUjJqzbz-kf82az8UBixbYUXOXkIu7E0EuhL0sjWcvZxJozIoDUh1DbXMlwRYRmqcK1cc_jVm7iOINy7dWUOpdLVVB26l9qegl1uup-5pMGkyQCYIDOutcOjuIrR-qlcDyzP9Dl1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ظریف: بازی‌های سیاسی را کنار بگذاریم
محمدجواد ظریف با یادآوری آخرین دیدارش با شهید سیدکمال خرازی:
🔹
دو هفته مانده به جنگ، دکتر خرازی به من گفت «کمی آرام باش».
🔹
خون شهدا برای ایران خودباوری به ارمغان آورده و باید از این فرصت برای ساختن آینده کشور استفاده کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/664246" target="_blank">📅 13:58 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
