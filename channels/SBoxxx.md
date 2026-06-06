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
<img src="https://cdn4.telesco.pe/file/J6JF_LgI10-tfdw1a34k-ZUcLlvQcN3vyftkfmG4Wpmnlcm9yy8KZ1vyMJBUxNcgYkTxTOGpgP8HEC5-tHggvYgf8m0tyJ4swkV2NY810wapBQvGGMgBnrL_7-CI3cLjYafC9x4UveWNMEW1-nlH02w_H4CIWqOvnrc-Cdzjf1ZTCzgNRSMSomE0xAArzA5UTPJ3euIKZYmPNOaca4gfcLQC12P4tdT7gCS6hbIoZp1wjjoqQgKMert39SHv4SqMlAHWXyx64PmnpWZdRpAp6T1WPrdDh_AtuYYxp7EH6cy7CqcGXObooXL-bKpYPoV4W6VDsj4p-4AA6f_JYVD3Kg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.97K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 01:05:00</div>
<hr>

<div class="tg-post" id="msg-17016">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">باراک راوید خبرنگار اکسیوس:   دو منبع آگاه به جزئیات به من گفتند که معاون برکنار شده‌ی رئیس موساد، یک سال پیش بودجه‌ای به مبلغ یک میلیارد شِکل (حدود ۳۵۰ میلیون دلار) و تیمی متشکل از صدها نفر برای پروژه‌ی سرنگونی حکومت ایران دریافت کرد!</div>
<div class="tg-footer">👁️ 353 · <a href="https://t.me/SBoxxx/17016" target="_blank">📅 01:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17015">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تبدیل ایران به یک دولت شکست خورده (Failed State) پلن B اسراییلی ها بود که ثابتی نیز به همین اشاره می‌کند   پلن A اسراییل، تغییر رژیم و کمک به روی کار  آمدن یک دولت غربگرای حامی اسراییل بود که فعلا شکست خورده است.  در این صوتی طولانی که ۸ ساعت پیش از آغاز جنگ…</div>
<div class="tg-footer">👁️ 343 · <a href="https://t.me/SBoxxx/17015" target="_blank">📅 01:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17014">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uU3SLTX0V2gxrvZ2VgWonQCiVU1otCzLAQOYS-sQMkPsyvkWityYcF4z1OqOd7RshGcVTt4pPgsOq9mVVNZCEg1Y8HsU2YPlqS8Q_T1gx4PAo6tNbqsuBio3A9nizsfnHl-AYbKknEOvn_OBY0sXlD83iSksn2p_Mbn7aJbuC1on-siCoJXdTsgCP2Y60omNcP42z2UFrmB2XH7pBrNhARQ-fUb0c0SIOkW-99qmp2O_CuHZV871_QPxVE_HmwF920dE4aiAl1Q0Oh_klN8O5SfL4CJYBC86OtFP06jhRidNH01_ijysESF2Oe7HFh14Bay7rPADBYvUPr4Pb3FJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهش ثروت شخصی ترامپ به سطح 6.5 میلیارد دلار!</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/SBoxxx/17014" target="_blank">📅 23:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17013">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">محمدجواد لاریجانی: رفتن آقای قالیباف به اسلام‌آباد غلط بود و هزینه‌ای بزرگ بود
▫️
ترامپ معتقد بود برجام کافی نیست برای همین آن‌را پاره کرد تا امتیازات بیشتری بگیرد.
▫️
دلیل آنکه آن‌ها در میانه مذاکرات حمله می‌کنند آن‌ است که ما وقتی مذاکره می‌کنیم به آن‌ها سیگنال می‌فرستیم که می‌توانیم با آن‌ها کنار بیاییم و برد-برد کار می‌کنیم که آن‌ها فکر می‌کنند اگر بیشتر فشار بیاورند، امتیازات بیشتری می‌گیرند.
▫️
نخست‌وزیر پاکستان، آدم خوبی است، اما لازم نیست ما و آمریکایی‌ها را مقابل هم قرار دهد تا مذاکره کنیم، باید میانجیگری بلد باشد.
▫️
اگر ما بخواهیم خودمان با آمریکا صحبت می‌کنیم نیازی به میانجی‌ نداریم. /صداوسیما</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/SBoxxx/17013" target="_blank">📅 23:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17012">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نخستین سند قطعی دال بر خودکفایی کامل کشور در تولید تریاک</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/17012" target="_blank">📅 22:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17011">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">▪️
خبر این است: وزیر کشور پاکستان پیش وارد تهران شد  مایلم یکبار دیگر صراحتا هشدار بدهم که ابداً نباید حسن نیت داشتن پاکستان را پذیرفت؛ پاکستان یکی از فاسدترین کشورهای دنیاست که توسط یکی از فاسدترین نظامیان دنیا اداره میشود. نظامیانی که وابسته سعودی، آمریکا،…</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/17011" target="_blank">📅 21:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17010">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دقت کرده اید هر کسی میانجی این جنگ بی پایان ما با آمریکا و اسرائیل شد به خاک رفت؟!  راند اول قطر میانجی شد و همان روز ایران به قطر حمله کرد و چند ماه بعدش اسرائیل هم به قطر حمله کرد و در جنگ اخیر هم با حمله موشکی وحشتناک ایران به تاسیسات گازی راس الفان، بیشترین…</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/17010" target="_blank">📅 21:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17009">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqEz3Z7kixg5gmFcIRi7LcyK3JWHPdj6SiQH0lRRuyrdX3GGfAiCN0ucSLyXRjyakNBEMyhgwH00XlyabyMUJ4d8eL0j63EE4pe8D5zUFVhwGItS0a_7KE61idx8K6D2iW8JznkfRJsdiVIgBjcca8g23VMsXuo2b4VWMOYB2gcrrim739n7mlE33Nyqa6rWk-yUlm-nwiFhbh-VtIF1uSY2oNWbXYDCi35X_YuNmJdI4TYys4NR3gDq944yjFHoP3IUHoOgq_1anG1HyACLm433k_C6JIQNzWjhd6h5WD5YIg1fZfUlSj4OIdprfc84AnQMBmqqQNzOTNIg8BgT1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ایران در سال ۲۰۲۶ با یکی از شدیدترین فشارهای صادراتی خود در سال‌های اخیر روبه‌رو شده است. داده‌های منتشرشده توسط شرکت ردیابی نفتکش Kpler و منابع تخصصی بازار انرژی نشان می‌دهد که از زمان آغاز درگیری‌ها و تشدید محدودیت‌های دریایی در اواخر فوریه، توانایی…</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SBoxxx/17009" target="_blank">📅 20:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17008">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وزیر کشور پاکستان، محسن نقوی، برای دیدار با مقامات ایرانی از جمله وزیر امور خارجه عباس عراقچی، وارد تهران شده است.
— خبرگزاری تسنیم</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/17008" target="_blank">📅 20:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17007">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تروریستهای ازبک دولت الجولانی را تهدید کردند   گروهی از تروریستهای جهادی ازبک با انتشار بیانیه‌ای دولت سوریه را به اعمال فشار علیه خود و تهدید به بازداشت و اخراج از سوریه متهم کردند.</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/17007" target="_blank">📅 20:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17006">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">من بعید نمیدانم در این سفری که علامه جولانی به آمریکا داشته ، به پیشنهاد عربها از ترامپ دستوری جهت اخراج این وحوش اویغور و اوزبک و چچنی و … دریافت کرده باشد</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/17006" target="_blank">📅 20:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17005">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIXhvo6czSzRCxxuKxHW_UtuUHtfhFAJPWdWW0qV0lmqTEBdL-BtvY1Vtvrw8ZCtv0QxyxifOdQCNZobNH01Cp8j6cMxTpqL6NzbwPfxjMv73Xo3ILlsw3obBampOBUjGMRqqM3QqKJ5NW_nEY5rrCw5PQhAslryoWXARu9qZ0yMPAdPYMfYO2hzi3mr-wczYmrKBaZHYg67mdYLOaKmT9lk4JKaWkZ0GMlR4-OwgGiLLgo3BNa7Kt-9H8bzZ9W2YZSmUJlZaLVFAOSOmaBmSqgUf0rkV3PwAzDBiFMQjbvXdZ4tCfnbXfekYQDj-sgBlk158NgauvcKChkdTRWP6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا چرا غیرقابل دانلود؟!</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SBoxxx/17005" target="_blank">📅 20:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17004">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شما ببینید وضعیت این منطقه گه گرفته چطوری است که پاکستانی که خودش در‌ همین مدت در غرب (بلوچستان)، شمال (وزیرستان) و شرق (هند) غرق در تنش و نکبت بوده حالا دارد برای ما میانجیگری می‌کند!  سبحان الله!</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/17004" target="_blank">📅 19:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17003">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پیروزی اوکراین با ربات ها و هوش مصنوعی !؟  در سال‌های اخیر، روایت حاکم بر جنگ روسیه و اوکراین حول محور بقای کی‌یف در برابر ماشین نظامی مسکو می‌چرخید. با این حال، شواهد میدانی و مواضع تحلیل‌گران غربی نشان می‌دهد که ورق به سود اوکراین برگشته و اکنون صحبت از…</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SBoxxx/17003" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17002">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRAC50F90hB3U65HaZBp5BN6HdNxQJblM7iLIb2_LVRzf2Tcm9AfeNMjXQulr5pZVVEIru5pjE9VWWO2v4CG0eZN0OAjsosNr-gLdfvb3--vzjcefGTcrefn_DcvwYX-cLwbamofOV_vFBKyJWsXQksFj9cfFNSc3_9IsQA1lLYatsiY5kbvMj58ncmVeY27Y5e3Wh1uaL2r1UliCoJ8ehm2lCxRQ5i8lmp7ijyNKDh1MojV7UcnbU6kQj9L9Ac1V_p2tqRhvlYhRp7YZcL2m-lb_x1zJrtnp9fiZwUeNNMJ-jYFDOUBGR0Qk01140rNkKbPAJ1_M7jjtZzAqqYqLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
ربات ها درحال بازنویسی چهره جنگ امروز
♦️
رباتیک در میدان جنگ به عنوان نظامیان  برای کارهایی که بیش از حد معمول خطرناک، تکراری و یا با پیچیدگی خاص برای انسان است بکار میروند.
🔸
از هواپیماهای بدون سرنشین، عرضه به تانک های خودمختار به تانک های خودمختار، روبات…</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/17002" target="_blank">📅 17:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17001">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔻
برخی شنیده ها حاکی از تلاش گروهی از نمایندگان مجلس برای استیضاح وزیر ارتباطات به جرم اجرای دستور رئیس جمهور و بازگشایی اینترنت می باشد</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17001" target="_blank">📅 14:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17000">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">📡
اینترنت پاکستان ، به دلیل اعتراضات مردم علیه حکومت ، در آستانه خاموشی قرار دارد</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17000" target="_blank">📅 13:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16999">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✈️
پاول دوروف ؛ مالک تلگرام
:
فیلترینگ و محدودیت‌های اینترنتی، روسیه را به «حاکمیت دیجیتال» نزدیک‌تر نکرده، بلکه از آن دورتر کرده است.
به گفته دوروف، متخصصانی که می‌توانستند در روسیه سیستم‌عامل موبایل بسازند، به‌دلیل وضعیت خراب اینترنت، در حال ترک کشور هستند
او تأکید کرد تا زمانی که گوشی‌ها بر پایه سیستم‌عامل‌های آمریکایی مثل iOS و Android کار می‌کنند، حتی اپلیکیشن‌های «ملی» هم در برابر نظارت و سانسور از طریق بک‌دورها و فروشگاه‌های اپلیکیشن آسیب‌پذیر می‌مانند
دوروف این سیاست را «تغییر بسته‌بندی بدون تغییر اصل ماجرا» توصیف کرد و کنایه زد: مسئولی که به نام حاکمیت دیجیتال، اینترنت روسیه را خراب کرده و کشور را دهه‌ها عقب برده، شایسته دریافت مدال امنیت ملی از آمریکاست</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16999" target="_blank">📅 12:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16998">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRpiGv14YyzLBCHc4pUFO-e6YtJ1k48TWZ2qYAl9dOjIFixvhfG1wvfAi8MkLEOE6Khtb2OBnbDIlmo8Q_j7uYJf92ZNK7YqecckTz7501xk31THPudI87NKlExeMebAiF-GilyPgEbDNivRj_dim7QMA-NRb4QEmo_1n7pKHH4kQmWTUj45l2ZZ6_5fPEtKS-OC0tNc2JheAcs9-sNrx48TFVxC3QjKlvXcoDpsZFoQX021tg7J90xE2Bs8Y4bwVKXiate11pvCguxx4XBCivaHPexSWlx1jwGn4cBZvmsdmk5hNtUadgr4uGvtxLlzKkSK0QDjTt1aApoGwc1N5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
اینترنت پاکستان ، به دلیل اعتراضات مردم علیه حکومت ، در آستانه خاموشی قرار دارد</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/16998" target="_blank">📅 12:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16997">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">این یعنی نه ایران و نه روسیه از این جهش بهای نفت حداکثر استفاده را نبرده اند؛ ما به دلیل محاصره دریایی آمریکا صادراتمان افت کرده (پست ریپلای شده را ببینید) و روسها هم به دلیل حملات سنگین پهپادی اوکراین.  عربها هم که عمدتاً ضربه دیده اند و لذا بزرگترین منفعت…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16997" target="_blank">📅 11:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16996">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ارتش لبنان اعلام کرده است که چندین نفر از پرسنل نظامی، از جمله یک افسر، در حمله هوایی اسرائیل که یک خودروی نظامی را در جاده الخالدیه–نبطیه هدف قرار داد، کشته شدند.  بر اساس گزارش‌های رسانه‌های لبنانی، این افسر دارای درجه سرتیپ بود.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/16996" target="_blank">📅 11:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16995">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ارتش لبنان اعلام کرده است که چندین نفر از پرسنل نظامی، از جمله یک افسر، در حمله هوایی اسرائیل که یک خودروی نظامی را در جاده الخالدیه–نبطیه هدف قرار داد، کشته شدند.
بر اساس گزارش‌های رسانه‌های لبنانی، این افسر دارای درجه سرتیپ بود.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/16995" target="_blank">📅 11:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16994">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دقت کنید که سنتکام می‌گوید که دوباره «سایتهای راداری نظارتی ساحلی ایرانی» را در گروک و قشم زده اند!  پیشتر اشاره شد چرا مهم است.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/16994" target="_blank">📅 09:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16993">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فرماندهی سنتکام:   چند لحظه پیش، نیروهای مرکز فرماندهی مرکزی چهار پهپاد تهاجمی انتحاری  ایرانی که به سمت تنگه هرمز پرتاب شده بودند را سرنگون کردند.   پهپادهای ‌تهاجمی تهدیدی فوری برای ترافیک دریایی منطقه ایجاد کرده بودند. نیروهای آمریکایی پس از آن به سایت‌های…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/16993" target="_blank">📅 09:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16992">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فرماندهی سنتکام:
چند لحظه پیش، نیروهای مرکز فرماندهی مرکزی چهار پهپاد تهاجمی انتحاری  ایرانی که به سمت تنگه هرمز پرتاب شده بودند را سرنگون کردند.
پهپادهای ‌تهاجمی تهدیدی فوری برای ترافیک دریایی منطقه ایجاد کرده بودند. نیروهای آمریکایی پس از آن به سایت‌های راداری نظارتی ساحلی ایرانی در گروک و در جزیره قشم برای دفاع در برابر حملات بیشتر حمله کردند.
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ به تهاجم بی‌دلیل ایران در چارچوب دفاع از خود آماده‌اند.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/16992" target="_blank">📅 02:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16991">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUHunhWpAlcU5RWcMb9OUp_MY345y42Th-G6D8fFwk9PdZCBTlSIi4FAEjzUPAq6-R-9f44mNqAoQ5_sEWtw2g0htG-00d6h44fWkZKIsXiP55RrfZqspLdO-HtboYdpwM1YMECKE-vsVs25V-Iv-MxTxB7k792rQpcpnIup6Fz8bKwcFGYy9OT5tW6XHlc2XtIq_Tb3PV_TapMY-YbtY-06TFKKccLs66sz3Zt4JW8rpAHLSQkyXk-iCZCkkWJjG7PORIh1jEq-qG2eMESonnba5glZGezUo3PeZSU64z37pOzq8cFfhVKrdtCyCbWlrqgGxMjGqfLk6gp1CRC-iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضرات مداوماً از جهش تورم در آمریکا سخن میگویند و آن را سند موفقیت خود میزنند!
این هم تورم مواد غذایی در کشور خودمان!</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/16991" target="_blank">📅 00:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16990">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فوری | ترامپ: در مدیریت پرونده ایران موفقیت بزرگی کسب خواهم کرد</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/16990" target="_blank">📅 23:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16989">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فوری | آکسیوس، به نقل از منابع: واشنگتن منتظر پاسخ رسمی ایران است و اختلافات باقی مانده را نسبتاً محدود توصیف می‌کند.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/16989" target="_blank">📅 22:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16988">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فوری | آکسیوس، به نقل از منابع: واشنگتن منتظر پاسخ رسمی ایران است و اختلافات باقی مانده را نسبتاً محدود توصیف می‌کند.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/16988" target="_blank">📅 22:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16987">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فوری | اکسیوس، به نقل از دو منبع: اختلافی بین واشنگتن و تهران بر سر اندازه و زمان‌بندی آزادسازی وجوه مسدود شده.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/16987" target="_blank">📅 22:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16985">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
محسن رضایی در گفت‌وگو با سی‌ان‌ان:
🔹
اگر ترامپ مذاکرات را جدی بگیرد، ۲۴ میلیارد دلار برای آمریکا مبلغ زیادی نیست.
🔹
اگر او می‌خواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتمادی است که ایران می‌خواهد به طرف مقابل داشته باشد.
🔹
این آزمونی…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/16985" target="_blank">📅 21:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16984">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
محسن رضایی در گفت‌وگو با سی‌ان‌ان:
🔹
اگر ترامپ مذاکرات را جدی بگیرد، ۲۴ میلیارد دلار برای آمریکا مبلغ زیادی نیست.
🔹
اگر او می‌خواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتمادی است که ایران می‌خواهد به طرف مقابل داشته باشد.
🔹
این آزمونی است که آمریکا باید از آن عبور کند و راه باز خواهد بود. این پول ماست، نه پول آمریکا.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/16984" target="_blank">📅 21:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16983">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دستیار ایرانی به سی‌ان‌ان گفت دیدار خامنه‌ای با ترامپ رخ نخواهد داد</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/16983" target="_blank">📅 19:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16982">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رضایی ایران هشدار داد که اگر آمریکا درگیری را از سر بگیرد، ایران «جنگ را» فراتر از خلیج فارس خواهد کشاند -</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/16982" target="_blank">📅 19:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16981">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کاخ سفید:  دیدار عراقچی- ویتکاف  گفت‌وگوی مستقیم ویتکاف و عراقچی در مسقط    «استیون ویتکاف، فرستاده ویژه ریاست‌جمهوری آمریکا، به همراه آن اسکاروگیما، سفیر آمریکا در عمان، امروز در مسقط با دکتر عباس عراقچی، وزیر امور خارجه ایران، گفت‌وگوهایی انجام دادند؛ این…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/16981" target="_blank">📅 18:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16980">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گروسی:   ایران و آمریکا به توافق نزدیک شده‌اند</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/16980" target="_blank">📅 18:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16979">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گروسی:
ایران و آمریکا به توافق نزدیک شده‌اند</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/16979" target="_blank">📅 17:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16978">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ایران دارای یکی از بزرگترین ناوگان های نفتکش دنیا بود اما با این وضعیتی که پیش می رود باید از شوتی های زحمتکش مرزهای شرقی و جنوب شرقی کشور برای انتقال نفت بهره ببریم!</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/16978" target="_blank">📅 16:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16977">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">Yinon_Plan.pdf</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/16977" target="_blank">📅 14:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16976">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">امیرحسین ثابتی:   آمریکا بعداز جام جهانی سنگین‌تر به ایران حمله خواهد کرد  ایران را تبدیل به غزه دوم خواهند کرد.  باید پیش‌دستانه پتروشیمی‌ها و زیرساخت‌های منطقه را بزنیم.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/16976" target="_blank">📅 13:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16975">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ایران_جنگ_را_برنده_نشد،_بلکه_چیز_خطرناک‌تری_را_به_دست_آورد.pdf</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/16975" target="_blank">📅 13:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16974">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBVW6R9a-U9QQSxbwx3N3YiAelU6YUK2lzwj2hQn9b8l8kYEQlf2KYxXb6oPzKS3AtVCMtV6m9hm4swHKqKWtp8J1yR0MBOQVtTGd2EyIuiYFClvsLSJ66K-kKKzsWQ6z1hoT4axLO8z-Pu2mSONEpEsIspsH86afgCSVQYL4nIbrRRPJgUUq8yYdF0qp96FakBa5WXgRqajHyECnf0JVFRFyj6wFYSNJHyhr_czYwdhoU5sWyPbNkMrWQ4NqGkALPkoC0yBPgev1dhxmWxie4Y_kz3dg3QFlPPv0kSFwrsKnwSf5CrkxuUm2-8GGNLjXP_J4qtJq8U_IUA6RlsUMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدرسگ ها چه اسم هایی برای بندرشان گذاشته اند!  بعد انتظار دارند حمله نکنیم!</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/16974" target="_blank">📅 13:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16973">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عمان پس از انفجار در بندر فهل، بارگیری نفت را متوقف کرد  سلطنت عمان بارگیری نفت در پایانه بندر فهل در خلیج عمان را به طور موقت متوقف کرده است. به گزارش رویترز، دلیل این امر انفجار در منطقه بندر است.  بندر فهل یک نقطه صادرات اصلی نفت خام عمان است. اختلالات…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/16973" target="_blank">📅 13:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16972">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دقت کرده اید هر کسی میانجی این جنگ بی پایان ما با آمریکا و اسرائیل شد به خاک رفت؟!  راند اول قطر میانجی شد و همان روز ایران به قطر حمله کرد و چند ماه بعدش اسرائیل هم به قطر حمله کرد و در جنگ اخیر هم با حمله موشکی وحشتناک ایران به تاسیسات گازی راس الفان، بیشترین…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/16972" target="_blank">📅 13:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16970">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l9K0HGneMVuYUn9i6zOuC7nguA2JlIKzpnd2Ofq3UuFgTIOGGHGWFQ2fFNaF9F_GGwqAxfr91xh2pjRNyPfpNaQlEQ3Cc5tltqOArgpOgjn4FhPhJi9PaNQjPttL3h6BradpokhVvXp8nUq7ON3-cxgbAgbUkbOuMxCLObKD7y_roXxoQwU8nyiCSS74qf72e3NduJV6-1u1qckJd60mESfHTuF4b4EitsoO6FteQ3viKb7j5Cb_wEoVmEGSwnlfDqIDSFMZWd0pfrhs1mx4LKvd1kaIXlEZDCDcbrROeh4EPoff71-zMyInlZEEXVesexeM6ihE3r4xaihoKBuD7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXx-uYP0u0OMb2DA1t7uBeKA_1XeTtJ_yw3qqDKtOWTJUC661oYGtb1RFf7O2fpDHOvJXAmZ1agP3VBZ9vRVRiMe6WmKOtWM-hUtdKFOSfJfy98wMeQmcO9_CflM6Lq5Pxqj_vtm1fXYg7Ynl1KqaAhSFcvogvcQoTrRUn8b3eCL4eUex_du3ZVnY_y5tTBXgw87bv7KNv05kpbVRULeOtghM2VHYF6AWScECbK7maD3NLTmZyuq6NzP2bdgRroQsNu2WDyw95q-RNtxhclcN0-3ABimaEXHVkRnvua-tpjTRw_GDeRo6jzaME36mSAUb5xJTB0zx_FMUBNY5cv7rA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم با خر یوگا میکردید بهتر بود ولی خب</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/16970" target="_blank">📅 12:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16969">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اکنون ثابت شده که باکو میزبان گروه های تکاوری و جاسوسی اسرائیل در حین جنگ بوده اند، منتهی دولت پوزیده صرفاً به استمالت از آنها ادامه داده و حتی یک موشک و پهپاد به تاسیسات آنها برخورد نکرده است.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/16969" target="_blank">📅 11:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16968">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">این پوزیشن را دیروز به همراهان پیشنهاد دادم.  کماکان بر این باورم که خریدها سبک باشد و کسانی که سنگین کریپتو دارند این فرصت خروجشان است.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/16968" target="_blank">📅 11:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16967">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doGiEjzB36jHjwM33Hok2HR7V5-HOys-LvsvHyw_SK2SlZw307Vc2wiAdeJOmYmA_QDPbR84VJfMDQmtk2p5We51xiKOoaaHM_u2P5FDsTM-1nkHCvInd9tRqtH8mkAxcpEVIAVC-rnTlaHBHzM9egsZCiJmLhLFerWBfW8Bq5LbhTYcGsRgsW1bf1SWwlO3135pW9-Dd3oDLwbEt9ELEI2WfFV8WOsK4IDVDykV7M2J-NDp0T_geqklG_JZXykDh4aHnHwV2kcsxeHquuJp_mBQ_dNyeRyXxSRokoMTx_2UQI2gEqg3UoKP-g9NTLt_tMsSKjwCCYfBFVA-tivXoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری باکو بین ۵۰ تا ۶۰ درصد از نفت اسراییل را تامین می‌کند و میزبان بسیاری شرکت‌های نظامی و امنیتی اسراییل هم هست اما تا کنون از ضرب حملات موشکی و پهپادی سپاه به دور مانده است.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/16967" target="_blank">📅 11:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16966">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ایران_جنگ_را_برنده_نشد،_بلکه_چیز_خطرناک‌تری_را_به_دست_آورد.pdf</div>
  <div class="tg-doc-extra">232.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/16966" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این‌گونه_دکترین_نتانیاهو_برای_ایران_فروپاشید.pdf</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/16966" target="_blank">📅 11:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16965">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دورویی اروپا در قبال اسرائیل: محکومیت‌های کلامی و خریدهای میلیاردی سلاح
اروپا این روزها در قبال اسرائیل دو چهره متفاوت به نمایش می‌گذارد: چهره‌ای سیاسی که با محکومیت‌های پرسر و صدا و قطعنامه‌های نمادین، خود را مدافع اخلاق و حقوق بشر معرفی می‌کند، و چهره‌ای نظامی که در سکوت، میلیاردها دلار سلاح از همان کشور می‌خرد. سیاستمداران اروپایی با برگزاری کنفرانس‌های مطبوعاتی و رای دادن به تحریم‌های نمادین، سعی دارند تصویر یک قاره متعهد به ارزش‌های انسانی را به نمایش بگذارند، اما در پشت پرده، ژنرال‌ها و مسئولان نظامی با امضای قراردادها، واقعیت دیگری را رقم می‌زنند.
در ۲۶ مه ۲۰۲۶، شرکت البیت سیستمز اسرائیل اعلام کرد که سفارشات معوقه‌اش برای اولین بار از ۳۰ میلیارد دلار فراتر رفته است؛ رقمی که حتی پنج سال پیش هم غیرقابل تصور بود. در میان این اعلامیه، قراردادی ۱.۴ میلیارد دلاری با یک کشور اروپایی ناشناس برای مدرن‌سازی نظامی در حوزه‌های زمینی، هوایی و جنگ الکترونیک به چشم می‌خورد.. این در حالی است که کشورهای اروپایی با صدای بلند، صادرات سلاح به اسرائیل را متوقف کرده‌اند، تحریم‌های جزئی را مطرح می‌کنند و شرکت‌های اسرائیلی را از نمایشگاه‌های دفاعی اخراج می‌کنند.
اسپانیا صادرات سلاح به اسرائیل را متوقف کرد، چند کشور عضو ناتو تحریم‌هایی را پیشنهاد دادند و البیت سیستمز پس از اعتراضات از نمایشگاه یوروناوال فرانسه اخراج شد. اما در عمل، همین کشورها در سکوت، به خرید سلاح از اسرائیل ادامه می‌دهند.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/16965" target="_blank">📅 10:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16964">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V56_ecqaAXOmdJN60ygOxmRNz_DrVCKXL92vk3zi4IuIUq97uBqqEWiFS1Z02r85N0--Zz3A-Id3cU6wzdKugbKbW_zAlzlk0xSFlmx6KH9IzFBHGDpB7w0RuaBfZOWj4kiMyLrLt1Fu0hjtYMtYxVcaWUpVDQOrNCL2dOjsCZRPEcCCplb6H9erDBExL9YFcAvE35ygsInnRaGyeRcbUOjIZsFWN4k218U5UIrphlq0zNsjhlg5Et2PVJQQYpH_5mKMEc9zFMKkByDD7S6nlJhG45nWyrYgDjbI7MPuPSbRkkd7BWSn4dqzi140xeePswkJZc-kbls8TtFLJB6dFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشتر گفته بودم که یکی از انگیزه های اسراییل از تعقیب پروژه تغییر رژیم در ایران ایجاد یک کریدور داوود بزرگ است که او را از امتداد آویزان بودن به آمریکا برای تامین امنیت ملی اش بی نیاز کند.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/16964" target="_blank">📅 10:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16963">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">به گزارش بلومبرگ، بریتانیا و فرانسه تقریباً طرحی را برای اجرای عملیات مین‌روبی در تنگه هرمز، پس از توافق احتمالی بین آمریکا و ایران بر سر آتش‌بس دائمی، نهایی کرده‌اند.
این طرح یک تلاش چندملیتی خواهد بود و پس از بیش از یک ماه نشست‌های چندجانبه به رهبری دو کشور انجام می‌شود.
به گفته افراد مطلع از این طرح، این عملیات شامل ۱۵ کشور خواهد بود که پرسنل نظامی و تجهیزات خود را به مأموریت اختصاص می‌دهند و برای جلوگیری از درگیری، ارتباط مستقیم با ایران حفظ خواهد کرد</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/16963" target="_blank">📅 09:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16962">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خواننده Secret Box از یک سال پیش آگاه بود که دلیل زدن هوانیروز و پایگاه ها و پاسگاه های مرزی ارتش و سپاه در مرزهای غربی، گشودن فضا برای ورود نیروهای مسلح کرد به داخل کشور بود.  اما چرا این طرح آن گونه که باید و شاید عملیاتی نشد؟!  بخوانید:   موساد سلاح‌های…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/16962" target="_blank">📅 00:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16961">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بشدت به همین سناریو که 2 ساعت پس از آغاز جنگ اشاره کردم، ایمان آورده ام. تقریباً تردیدی برایم نمانده که مدل «فروغ جاویدان» صدام را این بار نتانیاهو با پژاک و گروههای مشابه ش میخواهد اجرا کند.  نکته بدتر اینکه در صورت موفقیت این طرح و با ورود نیروهای شبه نظامی…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/16961" target="_blank">📅 00:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16960">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">محسن رضایی:
امیر قطر و ولیعهد عربستان دارند خودشان را با واقعیات تنظیم می‌کنند اما امارات، بحرین و کویت همچنان فکر می‌کنند قدرت آمریکا مثل قبل خواهد بود. این‌ها فکر نکنند که اگر این روش را ادامه دهند ما بعد از جنگ رهایشان خواهیم کرد. اگر امارات و کویت با صهیونیست‌ها همراه هستند باید ابوظبی و بوبیان را به عربستان و عراق بدهند!</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/16960" target="_blank">📅 00:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16959">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBKkBTUAcIffL0HrDHR6xn_GSTdFBz8sI9cUWgx1ty_p4N22Fz8ynXnavIfYhEafAzHvZpiuCDzrgyUtQasTtMNzelkTr7DxqwB24m4UG9qPO-ru_9VEcvNA7ijBBChdUFy4Kn2xXZG9MAA6jIeHEIB_HcttV9zsNupEzvOMyGCCGGkgASd0TqZTwTqMBWvPNQSKjHfsIxxMfouRWTGucITb84RW5GcsYzkb3z-TGO7UQAfe4G25SPh-6K-MAIk7qlyCfrtvSRPS_w7g1imRiHo398NsReAwT4Lyr6diFjh-gm9NWl3FqfzTmHea_t1hWoGYGUvxjDJTTFJMv7lzuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یعنی نه ایران و نه روسیه از این جهش بهای نفت حداکثر استفاده را نبرده اند؛ ما به دلیل محاصره دریایی آمریکا صادراتمان افت کرده (پست ریپلای شده را ببینید) و روسها هم به دلیل حملات سنگین پهپادی اوکراین.  عربها هم که عمدتاً ضربه دیده اند و لذا بزرگترین منفعت…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/16959" target="_blank">📅 21:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16958">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ایران و روسیه یک تفاهم‌نامه همکاری به ارزش ۲۵ میلیارد دلار در بخش هسته‌ای امضا کردند - تسنیم نیوز</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/16958" target="_blank">📅 20:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16957">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">رویترز:   روسیه برای اولین بار اذعان کرد که تولید نفت این کشور در سال جاری کاهش یافته    این اعتراف در زمانی مطرح می‌شود که اوکراین در ماه‌های اخیر حملات پهپادی و موشکی خود را به تأسیسات انرژی روسیه تشدید کرده . آژانس بین‌المللی انرژی تخمین زده که تولید نفت…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/16957" target="_blank">📅 20:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16956">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">صنعت نفت ایران در سال ۲۰۲۶ با یکی از شدیدترین فشارهای صادراتی خود در سال‌های اخیر روبه‌رو شده است. داده‌های منتشرشده توسط شرکت ردیابی نفتکش Kpler و منابع تخصصی بازار انرژی نشان می‌دهد که از زمان آغاز درگیری‌ها و تشدید محدودیت‌های دریایی در اواخر فوریه، توانایی…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/16956" target="_blank">📅 20:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16955">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_TaTBUmD3P4H1VrzCIzr2U7OQ1DOkIpyFG4dNSxZW0G57Hfa3wEL6Iwz_LJdzuj9rMT7TEfdsnFAD3KMtWo5mRLuQnTQub86v8vEJ36pqf3BKx4yDQRadCiO7wlCQHWmPDx0Clfjw_AWgHMYz0PLySzWMiJB5KtK2QTEhuOQ0QImWf8F-KiDOquA_kPjnJC8XKgteEYoJrO_gmREN-XrW362ZGgCbEozJHE-62J47XzdhPKxEEXtl2xzqCEz9BpKJhVvNXnsKdMuKtI63_OvA4s9n3mcAjkFQLIredF17TRfJoqSL7spVpSUAGBo1JfzzFil9DbmovPLjv9zDJw2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:   در حال حاضر، ما کنترل کامل ۶۰ درصد از نوار غزه را در دست داریم و دستور من رسیدن به ۷۰ درصد است... ابتدا ۷۰ درصد. از همان شروع می‌کنیم</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/16955" target="_blank">📅 19:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16954">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حالا اینجا همه حضرات میگفتند ترامپ دست خالی از چین برگشت!</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/16954" target="_blank">📅 19:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16953">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔥
ثمره دیدار ترامپ و شی/ سپر چینی جلوی جهش قیمت نفت را گرفت
🔹
فایننشال تایمز نوشت که کاهش ۴ الی ۶ میلیون بشکه‌ای واردات نفت چین و استفاده این کشور از ذخایر نفت خود، منجر به کاهش تقاضا در بازار نفت و کاهش قیمت شده.
🔹
خاویر بلاس خبرنگار بلومبرگ می‌نویسد که…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/16953" target="_blank">📅 18:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16952">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8Iutc6iIDNIY9vSA9ZHK7QBVDdBbpuIzyuimsCqOW8DAML1tw3Z7izb7PR0E5Dy1gTKaL-LUJ3lkfJbbyP3WdsN79fU41SR5JDIz4ICEJ7nWlRVAWojkDwKnq9cpmAxT38Y6oerpHaehtCoFgMueeGflcWTelEmNKOUcMM9M_wEazSx-a6LGvGdpJJUdV5xhXtSVKbHzhcl92VfxVLMiSC0zSqBTU0RIxtdE907_9bET-AV5sYct3fhcSXNqPCR-E7oddY1PUTsOoDAnRtG8QKKHFZporOClOMFBuL9lGprQGfvHF_yg-KYO4wC54XhJExh4q_4NSO75-Ga5h5afw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ثمره دیدار ترامپ و شی/ سپر چینی جلوی جهش قیمت نفت را گرفت
🔹
فایننشال تایمز نوشت که کاهش ۴ الی ۶ میلیون بشکه‌ای واردات نفت چین و استفاده این کشور از ذخایر نفت خود، منجر به کاهش تقاضا در بازار نفت و کاهش قیمت شده.
🔹
خاویر بلاس خبرنگار بلومبرگ می‌نویسد که اگر چین واردات نفت را کاهش نمی‌داد:
۱- قیمت نفت خیلی خیلی بالای ۱۰۰ دلار می‌رفت.
۲- فدرال رزرو مجبور به افزایش نرخ بهره می‌شد و وال استریت کاملاً نابود می‌شد.
۳- رئیس‌جمهور ترامپ در مذاکرات با ایران کاملاً تحت فشار زمان قرار می‌گرفت.
🔹
به گزارش خط انرژی، برنامه دولت پزشکیان برای توسعه روابط با چین چیست؟
@khate_energy</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/16952" target="_blank">📅 18:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16951">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAYgW6kmQzuu1SOSY1mNZNguIIZ36Q-TKylTmJ6E0m51kMFFS4S-0cHZvE3ypQmsk93072IgugAP_HWiDOBQ_RLD44bE4nSDZ4PPBoIaKYgrybJC4XY8EzFLkxjgGUZau8DpsmFtOVVrL47RurWslMY2lD2bT4K7mlaP2D0euzcxNrGIG7F6xXOSYqEZxZ8PQKtBEAIkxbsCaniK9QGKIgZk47f05Kr_TzIgOw56I5717l_-JIJMjYkyMGnny8n9A9w_6VjwIMEPX5XugSJ8z5WDmZqUFSFSx7d7LOiMpZUeYAszaMTp3S1Yy1W5im6ejv7b8TWhHu31NpFp8H8nZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/16951" target="_blank">📅 17:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16950">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی (IAEA) اعلام کرد که نتوانسته به تأسیسات هسته‌ای ایران (به جز بوشهر) برای انجام فعالیت‌های راستی‌آزمایی میدانی دسترسی پیدا کند.
این موضوع نگرانی‌ها درباره خطرات اشاعه هسته‌ای را افزایش داده است.</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/16950" target="_blank">📅 17:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16949">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سپاه پاسداران:
شرط اولیه ما برای پذیرش آتش بس در جنگ منطقه‌ای، آتش بس در تمامی جبهه‌ها از جمله لبنان بوده است.
دشمن می‌بایست با فوریت حملات خود به مردم لبنان را متوقف کند، و سریعاً با تخلیه سرزمین‌های اشغال شده لبنان به پشت مرزهای بین المللی عقب نشینی نماید و تمامیت ارضی لبنان را به رسمیت بشناسد.
هیچ آرامشی در منطقه بدون عقب‌نشینی صهیونیست‌ها از مناطق اشغالی لبنان برقرار نخواهد شد
همه ما با تمام وجود از ملت لبنان حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/16949" target="_blank">📅 17:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16948">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPZbdMpDj-6m7kakod1gCbhmjL3LHgMblEDZApOTIekjN4LqqKIKqgUO8xnJZdPvbZaziT5udzF4s8ExOjDnkvO-Vtl7sD7mkguX0FkGu03bj-GnklsRmGIvlMAWJ7D91gYYLJ_nMFIIDjB4FA22anZgTCN4ckYJg4UDA-KLjnsYUc_pi8PU5nzT3AsNWr4_6WhiDX0Pvdc94Q2HW_R15XoTfHkStsgXUs2TzSOsYkr7kZv60NFEJrN92vBunWO5wmzI8m1phy_TJSNZcwHMnv7AUoyREk4IxUo9xps1bikrmFXP1alWmjvm-Aaw79HrGtQAP46rgZnQuW9l5-F08A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:
تصویر روی جلد این هفته: «نسل جدیدی از سوسیالیست‌ها قصد دارند اقتصاد را با کنترل قیمت‌ها، مالیات‌های سنگین بر ثروت و موجی از ملی‌سازی‌ها دگرگون کنند.
این جریان که با خشم ناشی از غزه تقویت شده، با سرعتی چشمگیر در حال جذب رأی‌دهندگان است.»</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/16948" target="_blank">📅 16:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16947">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce28a3a45.mp4?token=INNEei8I9hcIokHFy0idX_h0JFJubF4gdIV6Ee660I5wx7qLQfgLQleNU6eZELckEsCgQFxBol6xqf1mrLlvmMuzhSPiP5yCji0bkIgeeN-6DLiGwIx7FRPClyimx4jszmROrPvZZdN8kV27Q4aUbWupkKtrzZU7LdKFl6F6QtkXUoZn9pGt7MEXUGAzPkm9eIOKNZ4m-wVWHqIQUxVf0bxlCf8ROJi8P5_9RHM9r9bcUJI5nPlEVS4dmntLBLSlyZxLFqaIiVOkKz4OJqzEQe2I9RN_1pZ-Vmm-WmgJJqbiqNs0CUoaHk32CDX7SD8NcV14CVQzzsiLRUgw2v6t3Kx7QMRyPKeKfpgRDhP9LQJtx4UqOa0GMYowIfMGqmcIhQ3xnH5K5HzlG1fFveeg13ynMi9KWeML2wdwyyXY3UmUDjMpq_raf4wGH2LB9_GbxzD4KX4lfpTufP5qpf_MJTv8VMZH9vR3E-RFXQUriAslFbMsIdxVOZMMF5kehO3y-6I8BjCkHzDCs0KKNoFjYpFF8zvRjcIDexZnfWszOMvBJNvc2kFinNnjIE2ohQY8y_R_acUD9cNwCVfu1THja0N3nLCwAe_1aSsQiBgVZBZ4uXUC_q2FY7c5qylaBfP5AYSt9LMwKLR89rv9dMy-jZIGkLfxhrZ6Ni2S-4wQQ_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce28a3a45.mp4?token=INNEei8I9hcIokHFy0idX_h0JFJubF4gdIV6Ee660I5wx7qLQfgLQleNU6eZELckEsCgQFxBol6xqf1mrLlvmMuzhSPiP5yCji0bkIgeeN-6DLiGwIx7FRPClyimx4jszmROrPvZZdN8kV27Q4aUbWupkKtrzZU7LdKFl6F6QtkXUoZn9pGt7MEXUGAzPkm9eIOKNZ4m-wVWHqIQUxVf0bxlCf8ROJi8P5_9RHM9r9bcUJI5nPlEVS4dmntLBLSlyZxLFqaIiVOkKz4OJqzEQe2I9RN_1pZ-Vmm-WmgJJqbiqNs0CUoaHk32CDX7SD8NcV14CVQzzsiLRUgw2v6t3Kx7QMRyPKeKfpgRDhP9LQJtx4UqOa0GMYowIfMGqmcIhQ3xnH5K5HzlG1fFveeg13ynMi9KWeML2wdwyyXY3UmUDjMpq_raf4wGH2LB9_GbxzD4KX4lfpTufP5qpf_MJTv8VMZH9vR3E-RFXQUriAslFbMsIdxVOZMMF5kehO3y-6I8BjCkHzDCs0KKNoFjYpFF8zvRjcIDexZnfWszOMvBJNvc2kFinNnjIE2ohQY8y_R_acUD9cNwCVfu1THja0N3nLCwAe_1aSsQiBgVZBZ4uXUC_q2FY7c5qylaBfP5AYSt9LMwKLR89rv9dMy-jZIGkLfxhrZ6Ni2S-4wQQ_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗
رهبر حزب‌الله نتیجه مذاکرات مستقیم لبنان-اسرائیل را رد کرد!</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/16947" target="_blank">📅 15:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16946">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انصافاً ترامپ خدایگان دروغ، دغل بازی، فریب و سخنوری است.
زاده خرداد است و ...
(امیررضا هم زاده خرداد است و میدانم این یعنی چه)
سبحان الله!</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/16946" target="_blank">📅 15:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16945">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQMrebU5HS96X0MB9DXwjR6bqQY4hp5_5u2KM6FptRzoZAMPIyOvgnaMXYxYymAeHpKWjjTuFSJfVI5j9Zv6PDbNGt6RVm2DJ-8d0tMFuA60vyjp-9tN-oNp17kIkbWODs3hvXVZXOL_ffnLbBSwqDrn9YUCFzaJKcFKlOp35mD2nen0J9KKQFoD5AUxT1MU9LN8PFcz09oX6OhwRBsrxwldzOdBdRrGFPmRn2Kth0yDrLKBVnMFVZsnFc6D2Plz6s9wn1NRlIlaKW6LCbyz-nKyQXgQdCZF097Ep9SEbvdUYwwIMOnFdUgCqFHkKXAfUTdj94paMReQu3esBED2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/16945" target="_blank">📅 15:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16944">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗
رهبر حزب‌الله نتیجه مذاکرات مستقیم لبنان-اسرائیل را رد کرد!</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/16944" target="_blank">📅 15:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16943">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sn0lGlTgJyv69VQFFJHtuLE_gKqj3D_cAFOVQZUgNpQ03nwSDK2Qff1WaNEy0dsnX59881hGd-EnJX1NGh6Qsg-eeEp1enBly0LRWQmbgop42COscx3S_PFPlYJpJWDBD08xFMncCjmFAS0uIpnTclOtIiw1ePDkHVUIarAgqaeWDFpfKhjuTygaauDMg-1R_BnxDdZqGQzv8ZodimRawblXXlXRKi2kXOHGs1pz0oxWDth66QZXVg8XXKNiwZd4e2ZAmfgyax_hhlsVLD_TVbb7XE39LV3vXCJCp071Mr4NJ5B-yC-AuqXTryplSGXenss03pX4Eu3s4SHpduQuhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضایی حصرشکن | حصر ترامپ رو بشکن!</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/16943" target="_blank">📅 15:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16942">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">از منظر حقوق بین‌الملل، «محاصره دریایی» یکی از شدیدترین اشکال اعمال زور میان دولت‌ها محسوب می‌شود و در صورت اجرا علیه یک کشور مستقل، به‌طور معمول در زمره اقدامات خصمانه با ماهیت نظامی قرار می‌گیرد.
بر اساس منشور ملل متحد، اصل بنیادین در روابط بین‌الملل منع توسل به زور است (ماده 2 بند 4). تنها دو استثنا برای استفاده مشروع از زور وجود دارد: دفاع مشروع در برابر حمله مسلحانه (ماده 51) و اقدام جمعی تحت مجوز شورای امنیت. بنابراین، اگر ایالات متحده یا هر دولت دیگری اقدام به محاصره دریایی بنادر ایران کند، این اقدام از منظر حقوقی صرفاً یک «اقدام اقتصادی یا فشار سیاسی» تلقی نمی‌شود، بلکه به‌طور مستقیم در چارچوب «استفاده از زور مسلحانه» قرار می‌گیرد.
در حقوق بشردوستانه بین‌المللی، به‌ویژه بر اساس قواعد عرفی و راهنمای سان‌رمـو درباره حقوق جنگ دریایی، محاصره زمانی مشروع تلقی می‌شود که در بستر یک مخاصمه مسلحانه موجود انجام شده باشد، اعلام و اطلاع‌رسانی شده باشد، و به‌صورت مؤثر اجرا گردد. به بیان دیگر، محاصره دریایی ذاتاً یک ابزار جنگی است، نه ابزار صلح.
از این رو، اگر چنین اقدامی علیه ایران در شرایط غیرمجاز حقوقی (بدون مجوز شورای امنیت یا بدون وقوع حمله مسلحانه قبلی) انجام شود، می‌تواند به‌عنوان «اقدام متخاصمانه شدید» (hostile act) تلقی شود که ظرفیت ایجاد «وضعیت مخاصمه مسلحانه بین‌المللی» را دارد. در حقوق بین‌الملل معاصر، حتی بدون اعلان رسمی جنگ، وقوع چنین سطحی از درگیری کافی است تا قواعد جنگی فعال شوند.
در نتیجه، محاصره دریایی یک کشور نه صرفاً یک ابزار فشار، بلکه از نظر حقوقی یک اقدام با ماهیت جنگی است که می‌تواند به تشدید فوری تنش و ورود طرفین به درگیری مسلحانه منجر شود، مگر آنکه تحت چارچوب‌های محدود و مشروع بین‌المللی انجام شده باشد.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/16942" target="_blank">📅 15:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16941">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">عجب فریبی و عجب تاثیری در کاهش بهای نفت!</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/16941" target="_blank">📅 15:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16940">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0uwdieuG9dhjZU0Lrm2dVe8zNOxpvL7i78OOO032YgubG9Lxqf0JxQbJAsUA-8aUlyNwJ628dQ7m1acAmqxVI8Hn1SZp58jZhfX2YOsNZvp52V1shFXdNKam4CarbXEqn1uUQlVYdoZuQY0onFcwh0s9ls9F_MlMy3GsOLi-mtfM8MlAMT3lFsriO7kKJxfu64Okv3566LGMajTy6Stqdn-Z-o-7HwO-b3D0_0h6ysbCuL_HraMSxFowM_4VXuSJZyiE7uTZtif3-Kjwa7TMpfXVGwH_zYA8tx-ng--2kffzDtMX3OcFzvEqwPGbR-pGD57lEIygQHmyxDhk2T-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلا رفت برای این سناریو که عصر گفتیم…؟!</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/16940" target="_blank">📅 15:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16939">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ به دستیارانش گفته است که جنگ با ایران را از سر نخواهد گرفت مگر اینکه نیروهای آمریکایی کشته شوند.  — وال استریت ژورنال</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/16939" target="_blank">📅 15:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16938">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کاندولیزا رایس — وزیر امور خارجه پیشین آمریکا :
«جنگ علیه ایران جنگی محدود بوده و نتیجه آن احتمالاً قطعی نخواهد بود، اما برای ایجاد خاورمیانه‌ای بسیار بهتر کافی بوده است.»</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/16938" target="_blank">📅 12:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16937">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔹
بازداشت جمشید قمی، مدیرعامل ۶۳ ساله شرکت ایران تِک ، به اتهام تأمین تجهیزات آمریکایی برای تأسیسات هسته‌ای و نظامی ایران</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/16937" target="_blank">📅 11:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16936">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ به دستیارانش گفته است که جنگ با ایران را از سر نخواهد گرفت مگر اینکه نیروهای آمریکایی کشته شوند.
— وال استریت ژورنال</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/16936" target="_blank">📅 10:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16935">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، گفت که فشار شدیدی به ایران وارد شده و مذاکرات با ایران به خوبی پیش می‌رود. او احتمال توافق تا پایان هفته را مطرح کرد، هرچند اشاره کرد که ممکن است دو تا سه هفته دیگر نیز طول بکشد.
به گزارش فارس به نقل از یکی از اعضای تیم مذاکره‌کننده تهران، گفتگوها بین ایران و آمریکا همچنان ادامه دارد و هنوز تصمیم نهایی گرفته نشده است.
یکی از اعضای تیم رسانه‌ای هیئت مذاکره‌کننده ایران، طرحی چهار مرحله‌ای برای توافق با آمریکا ارائه کرد: ۱) پایان جنگ، ۲) اقدامات عملی در مورد تنگه، ۳) تحریم‌ها و مسائل هسته‌ای، ۴) تشکیل کمیته نظارت</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/16935" target="_blank">📅 09:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16934">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOrjx5WpzVTlSovLAdC4Ek2VFBDnIBiFDz2urqhF11aJcig-ECnIUBhGWexhV9RpDzCRk8e_nG13Ae5K2GEEp92jQN-AhUbENhvNiNIah0W6mfNkI3T3Qb-w9apS7KyNQlVXxitSh3LEkIAec2aUzE1RVLkvEGBQtqJFZY0Lvo5d9TEiXJln5c8HxFSUuogOWe5bk6CsKfb40YIEDB2ZzJmyhh1aiWe-AbQYOr3ikDXzIjc2xeH1DwIuB8fV3J60yROXnpn6Gx9fTyeItjQADMl2rAaWNF_Xv1zK3fSRCWhW1ou1gun6sBQ6cBrtWkjDm1By423xD-zTyhsDamXVlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ایران در سال ۲۰۲۶ با یکی از شدیدترین فشارهای صادراتی خود در سال‌های اخیر روبه‌رو شده است. داده‌های منتشرشده توسط شرکت ردیابی نفتکش Kpler و منابع تخصصی بازار انرژی نشان می‌دهد که از زمان آغاز درگیری‌ها و تشدید محدودیت‌های دریایی در اواخر فوریه، توانایی ایران برای رساندن نفت به بازارهای جهانی به شدت کاهش یافته است.
پیش از این تحولات، ایران روزانه حدود ۲ میلیون بشکه نفت خام، میعانات و فرآورده‌های نفتی صادر می‌کرد. اما اکنون نشانه‌های روشنی از افت صادرات و تولید مشاهده می‌شود. بر اساس آمار اوپک، تولید نفت خام ایران در آوریل ۲۰۲۶ به حدود ۲.۸۵ میلیون بشکه در روز رسیده که نسبت به سطح پیش از بحران حدود ۳۵۰ هزار بشکه در روز کاهش نشان می‌دهد. برخی برآوردها حتی افتی نزدیک به ۴۰۰ هزار بشکه در روز را گزارش کرده‌اند.
در بخش صادرات، کاهش شدیدتر است. Kpler برآورد می‌کند که بارگیری نفت در پایانه‌های صادراتی ایران به حدود ۶۴۰ هزار بشکه در روز سقوط کرده است. نشریه تخصصی MEES نیز گزارش می‌دهد که این رقم از ۱.۶۴ میلیون بشکه در روز در ماه مارس به کمتر از ۵۰۰ هزار بشکه در روز در ماه مه کاهش یافته است. همچنین از ۶ مه به بعد برای مدتی هیچ محموله‌ای از پایانه اصلی صادرات نفت ایران در جزیره خارک ثبت نشد.
با این حال، صادرات نفت ایران هنوز به طور کامل متوقف نشده است. چین همچنان روزانه بیش از یک میلیون بشکه نفت ایران دریافت می‌کند، اما بخش عمده این نفت از ذخایر شناور انباشته‌شده در آب‌های آسیا تأمین می‌شود، نه از محموله‌های تازه صادرشده از ایران. این ذخایر نیز به سرعت در حال کاهش هستند. برآورد Kpler نشان می‌دهد که حجم ذخایر شناور ایران از آغاز بحران ۳۳ میلیون بشکه کاهش یافته و به حدود ۸۹ میلیون بشکه رسیده است.
در نتیجه، مسئله اصلی دیگر صرفاً کاهش صادرات روزانه نیست، بلکه سرعت تخلیه ذخایر شناور ایران است. اگر روند فعلی ادامه یابد، تحلیلگران Kpler هشدار می‌دهند که طی ۶۰ تا ۷۰ روز آینده بخش عمده نفت در دسترس برای تحویل به چین مصرف خواهد شد و ایران ممکن است ناچار شود تولید خود را تا حدود ۱.۷ میلیون بشکه در روز، نزدیک به سطح مصرف داخلی، کاهش دهد.
چنین سناریویی می‌تواند درآمدهای نفتی کشور را به پایین‌ترین سطوح سال‌های اخیر برساند و فشار اقتصادی قابل توجهی بر ایران وارد کند.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/16934" target="_blank">📅 01:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16933">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ:
در توافق پیش‌رو، به ایران اجازه دستیابی به سلاح هسته‌ای داده نخواهد شد و پس از امضای این توافق، تنگه هرمز به سرعت بازگشایی می‌شود.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/16933" target="_blank">📅 00:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16932">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
دونالد ترامپ
:
در اون منطقه از دنیا ( خاورمیانه ) ،  آتش‌بس یعنی وقتی طرفین دارند با شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنند
﻿</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/16932" target="_blank">📅 00:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16931">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نیروی دریایی ارتش، "مرکز فرماندهی و کنترل" شرارت های ارتش آمریکا علیه کشورمان را هدف قرار داد
🔹
در پی شرارت ها علیه شناورهای تجاری ایرانی در دریای عمان و نقض مقررات تنگه هرمز از سوی ارتش متجاوز آمریکا، نیروی دریایی ارتش، مرکز "فرماندهی و کنترل " این شرارت…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/16931" target="_blank">📅 23:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16930">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبر کوتاه بود و دلخراش: محمدرضا شهبازی مورد تجاوز قرار گرفت
😄
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/16930" target="_blank">📅 22:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16929">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">صدای انفجار در بحرین</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/16929" target="_blank">📅 22:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16928">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">به نظرم دسته خوبه را داده اند به سپاه که هر وقت میزند واقعاً بازارها به هم میریزند و دسته خرابه هم به ارتش داده اند برای وقتی که نفت را Short می کنند.
(باز بپرسید شورت چیست)</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/16928" target="_blank">📅 22:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16927">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نمیدانم این حمله های ما چطوری است که تا خبرش بیرون می آید نفت میریزد و طلا بالا می رود!
سبحان الله!</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/16927" target="_blank">📅 22:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16926">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نیروی دریایی ارتش، "مرکز فرماندهی و کنترل" شرارت های ارتش آمریکا علیه کشورمان را هدف قرار داد
🔹
در پی شرارت ها علیه شناورهای تجاری ایرانی در دریای عمان و نقض مقررات تنگه هرمز از سوی ارتش متجاوز آمریکا، نیروی دریایی ارتش، مرکز "فرماندهی و کنترل " این شرارت…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/16926" target="_blank">📅 22:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16925">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اطلاعیه نیروی دریایی ارتش: ساعاتی قبل مرکز فرماندهی و کنترل شرارت‌های ارتش آمریکا در یک ناوشکن آمریکایی در دریای عمان هدف قرار گرفت</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/16925" target="_blank">📅 22:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16924">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اطلاعیه نیروی دریایی ارتش:
ساعاتی قبل مرکز فرماندهی و کنترل شرارت‌های ارتش آمریکا در یک ناوشکن آمریکایی در دریای عمان هدف قرار گرفت</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/16924" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16923">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">عراقچی:   آنچه در ۲ روز گذشته حمله به بیروت را متوقف کرد، در درجه اول قدرت مقاومت لبنان و توان نیروهای مسلح ایران بود  وقتی کار به جایی رسید که نیروهای رژیم صهیونیستی می‌خواستند به ضاحیه جنوبی بیروت حمله کنند، موضع قاطعی گرفتیم و نیروهای مسلح ما آماده پاسخ…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/16923" target="_blank">📅 22:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16922">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عراقچی: من مطمئنم که مسئله سفیر ما در بیروت حل خواهد شد، ما به حکمت دوستان و مسئولان دولت لبنان اعتماد داریم</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/16922" target="_blank">📅 22:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16921">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزیر خارجه ایران: تماس‌های ما با آمریکا قطع نشده است، اما در مذاکرات پیشرفتی حاصل نشده است - المیادین.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/16921" target="_blank">📅 22:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16920">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزیر خارجه ایران: تماس‌های ما با آمریکا قطع نشده است، اما در مذاکرات پیشرفتی حاصل نشده است - المیادین.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/16920" target="_blank">📅 22:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16919">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlgCLFNBTXafByVyNYbI0T-o1QaBBfglv2KjCaJU4ZgbgX0Z2o0irysBsThimAqeG2QxYXcK_eetDoBCIjmfjS691UOe-ndTUvrEpBVhVrn3lKktEUMFgx_LqOezpqr2i2pv9Etp1ZpIvIAnI84lQQJm2XHYCkpiZg1D3ycn0T1UkfmkfAfKuuJ3qRPM-4we-QVHZKYmE_1BtESF4mxkGdRYBKiTHiO8UQYeOIJEYZdFvxrm3cS3GBEsW2ZgEVi_HzuKE11FtvseFNUB_Af-uPKcOJMF-4WaKYMD1wPVlbPwdLQhFWjxgL_ElREK50f8HPTHm69F9_dFe7xF3iEzEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم تخریب پایگاه «علی السالم» آمریکایی ها در کویت
تصویر سمت راست مربوط به آشیانه ها و تصویر سمت چپ مربوط به انبارهای سوخت</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/16919" target="_blank">📅 19:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16918">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">روبیو:
به عنوان بخشی از سیاست خارجی ما و به دلایل متعدد، ما به صورت علنی درباره اینکه آیا اسرائیل سلاح‌های هسته‌ای در اختیار دارد یا خیر، بحث نمی‌کنیم.
ما پاسخ بهتری به کنگره درباره اینکه آیا اسرائیل سلاح‌های هسته‌ای در اختیار دارد یا خیر، ارائه خواهیم داد، مشروط بر اینکه آن‌ها درخواست پاسخ به صورت محرمانه را مطرح کنند.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/16918" target="_blank">📅 18:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16917">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شرایط جوری شده که اسرائیل عرب های لبنان را می زند و ما هم در پاسخ عرب های کویت را می زنیم که در حین آن هندی ها کشته می شوند</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/16917" target="_blank">📅 18:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16916">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd2b300c77.mp4?token=nuYKqz7SZDcMe5zOc6TJO2K5jhcs794OpFBzJ6yexFWF5BZVQvhGPYTE7KgtR_tLADqD4impzsk2X31-8phth-IDeP8CBWDvhGz-KUJiEBBJNmvmvPTOiovQt6KdmvpII6OsBUxKkZUNTl9jqDMaL1HDtZokzu3z1M5E6vZ0Qu_u-qRaKjwwj2zLTGLyTbLhGywtegpOoqvHamvPT2xHKRfGjKBLKIl4tIkaO7nAeoc1u10LViueajBVKR8DsBxYmwmmyQVdMJELESq2hhGjbKSW75cmsvRt0-fN2zoI74zGYLQ9l8rvK9LdoTolQUeS8_XTnTF4bVqX-Dg7ZmYnGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd2b300c77.mp4?token=nuYKqz7SZDcMe5zOc6TJO2K5jhcs794OpFBzJ6yexFWF5BZVQvhGPYTE7KgtR_tLADqD4impzsk2X31-8phth-IDeP8CBWDvhGz-KUJiEBBJNmvmvPTOiovQt6KdmvpII6OsBUxKkZUNTl9jqDMaL1HDtZokzu3z1M5E6vZ0Qu_u-qRaKjwwj2zLTGLyTbLhGywtegpOoqvHamvPT2xHKRfGjKBLKIl4tIkaO7nAeoc1u10LViueajBVKR8DsBxYmwmmyQVdMJELESq2hhGjbKSW75cmsvRt0-fN2zoI74zGYLQ9l8rvK9LdoTolQUeS8_XTnTF4bVqX-Dg7ZmYnGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رومن گافمن: از زخمی ۷ اکتبر تا رئیس موساد  سرلشکر رومن گافمن، مدیر تازه منصوب شده موساد اسرائیل (که در ژوئن ۲۰۲۶ سوگند یاد کرد)، به عنوان یکی از ارشدترین افسرانی ظاهر شد که به طور فعال با نیرو‌های حماس در حملات ۷ اکتبر ۲۰۲۳ درگیر شد.   گافمن که در آن زمان…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/16916" target="_blank">📅 17:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16915">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رییس جدید موساد!  رومن گوفمن، سرلشکر متولد بلاروس و از نزدیک‌ترین چهره‌های مورد اعتماد بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از ۲ ژوئن ۲۰۲۶ ریاست موساد را بر عهده گرفته است.   گوفمن که پیش از این به‌عنوان منشی نظامی نتانیاهو فعالیت می‌کرد، اکنون در رأس مهم‌ترین…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/16915" target="_blank">📅 17:15 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
