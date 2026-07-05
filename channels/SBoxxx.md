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
<img src="https://cdn4.telesco.pe/file/PtnkoKpKt8mxMXeKHNGUdhD42EUMsPo_cjZoBh88XjUDU-uVJB86Vz6626R4Qi4zJTfqlQb_4B11gmoksOcl1m6wEvD5cvRYgCo0GQf8yGiPfkgvrgJZ2rhMmo4xz5-tiaYJtX7EGp9LdUee4472Arv8k3W7HQpxxrzmNZLyHLUnaoysTlxbFPGTRK8ppoIiMvRAXXh8bxwB4HfwKFt6DYX_xmZ6JAXERVtFm3EytIaGopjoIClNDQ-AvMeO1DCXfAetTLSFBM7x1ECdNLas9n2p2jmjLvt6n8l_T1Wo1s05nX2EfU0sJAumYZigSrlmLv2gI64cDhDAzmbupiw3Pw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 14:06:16</div>
<hr>

<div class="tg-post" id="msg-18225">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قالیباف، در مراسم تشییع رهبر سابق ایران:  «ثمره خون خامنه‌ای آزادی بیت المقدس خواهد بود».</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/SBoxxx/18225" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18224">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SBoxxx/18224" target="_blank">📅 12:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18223">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کلا خاطره خوبی از محاسبه خسارات و جمع آوری شواهد نداریم.
بار پیش
هم که جناب عراقچی داشتند خسارات اشتباه محاسباتی اسراییل در جنگ ۱۲-روزه را محاسبه می‌کردند که اشتباه محاسباتی بعدی روی داد و اصلا محاسبات ما به هم ریخت.</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/SBoxxx/18223" target="_blank">📅 12:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18222">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/18222" target="_blank">📅 12:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18221">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:
"ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/18221" target="_blank">📅 12:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18220">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">Trump Accounts
سرمایه‌گذاری بر نسل آینده یا
پروژه‌ای سیاسی؟
دولت دونالد ترامپ با معرفی طرح «Trump Accounts» تلاش کرده است ایده‌ای را به اجرا بگذارد که در ظاهر، حمایت از آینده مالی کودکان آمریکایی را هدف قرار داده است. بر اساس این برنامه، برای هر کودک واجد شرایط، حسابی سرمایه‌گذاری ایجاد می‌شود و دولت برای نوزادان متولدشده در بازه زمانی تعیین‌شده، مبلغ اولیه‌ای را به این حساب واریز می‌کند. دارایی این حساب‌ها نیز در صندوق‌های شاخص کم‌هزینه سرمایه‌گذاری می‌شود تا در بلندمدت از رشد بازار سهام بهره‌مند شود.
طرفداران این طرح معتقدند که ایجاد سرمایه از ابتدای زندگی می‌تواند فرهنگ پس‌انداز و سرمایه‌گذاری را در جامعه آمریکا تقویت کند. از نگاه آنان، حتی یک سرمایه اولیه نسبتاً کوچک نیز در صورت رشد مستمر بازار، می‌تواند هنگام ورود فرد به بزرگسالی به منبعی برای تأمین هزینه تحصیل، خرید نخستین مسکن یا آغاز یک کسب‌وکار تبدیل شود. این رویکرد همچنین می‌تواند وابستگی شهروندان به کمک‌های مستقیم دولت را کاهش داده و مشارکت آنان در اقتصاد و بازار سرمایه را افزایش دهد.
در مقابل، منتقدان بر این باورند که اثر واقعی این برنامه به توانایی خانواده‌ها برای واریز مبالغ بیشتر به حساب فرزندانشان بستگی دارد. از این منظر، خانواده‌های پردرآمد بیش از دیگران از مزایای رشد سرمایه برخوردار خواهند شد و در نتیجه، شکاف ثروت میان طبقات مختلف جامعه ممکن است کاهش نیابد و حتی در بلندمدت افزایش پیدا کند. همچنین برخی ناظران، انتخاب نام «Trump Accounts» را اقدامی با رنگ‌وبوی سیاسی می‌دانند که می‌تواند این برنامه را به بخشی از میراث سیاسی رئیس‌جمهور تبدیل کند.
در مجموع، موفقیت یا شکست «Trump Accounts» به عملکرد بازارهای مالی، میزان مشارکت خانواده‌ها و نحوه اجرای مقررات آن وابسته خواهد بود. اگرچه این طرح می‌تواند گامی در جهت گسترش سرمایه‌گذاری عمومی باشد، اما قضاوت نهایی درباره آثار اقتصادی و اجتماعی آن تنها پس از گذشت چند سال و مشاهده نتایج عملی امکان‌پذیر خواهد بود.</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/18220" target="_blank">📅 11:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18219">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رئیس‌جمهور فرانسه ماکرون:
فرانسه دارایی‌های ضد مین را به خاورمیانه اعزام کرده است، از جمله به‌ویژه دو کشتی  ویژه جستجوگر مین
همراه با دو ناوچه و یک هواپیمای گشت دریایی، این دارایی‌ها آماده هستند تا در کنار شرکای ما، به از سرگیری کامل کشتیرانی و تضمین ایمنی ترافیک در تنگه هرمز کمک کنند</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/18219" target="_blank">📅 08:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18218">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔻
پناهیان ؛ مشاوره ریاست نهاد نمایندگی رهبر در دانشگاه‌ها :
حاضریم تمامی منافع ملی را فدای خونخواهی رهبر شهیدمان کنیم</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18218" target="_blank">📅 23:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18217">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔻
بابک زنجانی
:
به زودی خونخواهی رهبر شهید شروع خواهد شد و آن خون خواهی اقتصادی است</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18217" target="_blank">📅 23:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18216">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ایران قصد دارد به چین تعرفه‌های ترجیحی برای تنگه هرمز ارائه دهد
تهران قصد دارد به چین و سایر کشورهای دوستانه تعرفه‌های ترجیحی برای هزینه‌های عبور و مرور ورودی تنگه هرمز اعطا کند.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18216" target="_blank">📅 22:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18215">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">به گزارش کانال 15 اسرائیل، دونالد ترامپ از اسرائیل خواسته است که فعالیت‌های نظامی خود را در لبنان افزایش ندهد، زیرا نمی‌خواهد این امر در مذاکرات جاری او با ایران دخالت کند.
به همین دلیل،  نتانیاهو یک عملیات نظامی که پیش از این برای منطقه علی‌الطاهر برنامه‌ریزی شده بود، را به تعویق انداخته است.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/18215" target="_blank">📅 22:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18214">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رئیس‌جمهور عراق:   عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18214" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18213">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رئیس‌جمهور عراق:
عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18213" target="_blank">📅 21:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18212">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، گفت که آمریکا می‌توانست رهبران ایران را که برای مراسم تشییع آیت‌الله علی خامنه‌ای، رهبر پیشین، جمع شده بودند، هدف قرار دهد، اما این کار را انجام نمی‌دهد زیرا می‌خواهد مذاکرات هسته‌ای را حفظ کند.  «همه آن‌ها آنجا هستند. با یک…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18212" target="_blank">📅 20:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18211">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، گفت که آمریکا می‌توانست رهبران ایران را که برای مراسم تشییع آیت‌الله علی خامنه‌ای، رهبر پیشین، جمع شده بودند، هدف قرار دهد، اما این کار را انجام نمی‌دهد زیرا می‌خواهد مذاکرات هسته‌ای را حفظ کند.
«همه آن‌ها آنجا هستند. با یک شلیک [می‌توانیم همه آن‌ها را از بین ببریم]، اما این کار را نخواهیم کرد زیرا در آن صورت کسی برای مذاکره باقی نخواهد ماند»</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18211" target="_blank">📅 20:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18210">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اردوغان به اسرائیل هشدار داد: "نباید اجازه داد اسرائیل منطقه را در خون غرق کند."
رئیس‌جمهور ترکیه، اردوغان، در سخنانی مشترک با نخست‌وزیر پاکستان، لحن تندی علیه اسرائیل اتخاذ کرد.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18210" target="_blank">📅 20:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18209">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">باز این پفیوزها می خواهند تندروهای داخلی را تحریک کنند تا تنگه را ببندند و قیمت نفت بالا برود و غرب از کمک بیشتر به اوکراین که خشتک روسها را بر کله شان کشیده منصرف بشود.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18209" target="_blank">📅 18:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18208">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترکیه با موفقیت موشک بالستیک TAYFUN Block-3 را علیه هدف کشتی متحرک با سرعت هایپرسونیک آزمایش کرد.
شرکت ROKETSAN یک آزمایش آتش‌زنده از موشک بالستیک TAYFUN Block-3 انجام داد و با موفقیت یک کشتی سطحی بدون سرنشین آزاد در حرکت را در دریا با یک سر جنگی زنده با سرعت هایپرسونیک هدف قرار داد.
هدف حدوداً ۷ متری — که یک قایق ماهیگیری کوچک بود — با آنچه شرکت آن را «دقت جراحی‌گونه» توصیف کرد، نابود شد.
این آزمایش نخستین مورد از این دست است که در آن یک موشک بالستیک که با استفاده از سر جستجوگر برای هدایت در مرحله پایانی، یک کشتی سطحی متحرک را در دریا درگیر و هدف قرار می‌دهد.
ترکیه می‌گوید این نخستین یکپارچه‌سازی چنین سر جستجوگری بر روی یک موشک بالستیک در داخل کشور است و یکی از تنها چند نمونه در سراسر جهان — قابلیتی که به طور موثر یک موشک بالستیک را به یک سلاح ضد کشتی تبدیل می‌کند.
سرعت پایانی هایپرسونیک TAYFUN آن را تا حد زیادی در برابر پدافند‌های متعارف دفاع هوایی مصون می‌سازد.
نسخه Block-3 پیشرفته‌ترین نسخه از برنامه موشک بالستیک توسعه‌یافته داخلی ترکیه را نشان می‌دهد.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18208" target="_blank">📅 18:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18207">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یک کارشناس:
به نظر می‌رسد که ایران در مراسم تشییع جنازه رهبر خود هر هیئت خارجی را با یک آیه قرآن مرتبط کرده است که هدف سیاسی خاصی را دنبال می‌کند.
عربستان سعودی: آیه ای درباره دو ارتش که در جنگ با یکدیگر روبرو می‌شوند، یکی مومن و دیگری غیرمومن.
ترکیه: آیه ای که کسانی را که در راه خدا می‌جنگند، بر کسانی که "نشسته"اند، برتری می‌بخشد.
دولت لبنان: آیه ای درباره افرادی که در صورت درخواست، از انجام فداکاری خودداری می‌کنند.
حزب الله: به آنها گفته شد "ضعیف نشوید یا غمگین نشوید، شما برتر هستید."
حماس: آیه ای که مردانی را که عهد خود را با خدا وفا کردند، مورد تقدیر قرار می‌دهد، "برخی از دنیا رفته‌اند، و برخی دیگر در انتظارند."
حوثی‌های یمن: آیه ای که به مومنانی که بدون سستی جنگیدند، ستایش می‌کند.
قطر: آیه ای درباره بخشش و لطف الهی، که به عنوان اشاره‌ای به نقش میانجی‌گری این کشور خوانده شد.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/18207" target="_blank">📅 13:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18206">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اظهارات مدودف، نخست‌وزیر روسیه:  ایران به جای سلاح‌های هسته‌ای، سلاح دیگری را کشف کرده است که از نظر قدرت، نه ضعیف‌تر از سلاح‌های هسته‌ای است و آن، تنگه هرمز است.  بحث‌ها حول این موضوع است که چگونه باید به توافقی دست یافت تا این تنگه در آینده به چه صورت عمل…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18206" target="_blank">📅 13:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18205">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جناب الکساندر سرگین هستند از گه خورهای اعظم که بیرون گود نشسته و به ما میگویند لنگش کن!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18205" target="_blank">📅 13:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18204">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSCzZkl4h74BEa0NDXQOy-vmxXsI0PPJGTDcOLn9wB1JqqW9QVR6gnT4u2YmBoZXLEjT4UUDOVimx2OclBhE6W6elOhLYdlV2noz6HhOk8RuTZA4ib6ooIJ_KRIAXOqQDifBkMQ1p3NKBb15aKzHc-hWs52ZKzuYOC-o82Z_8ku3MTfltmcrOYydxZItUFOshtDQAdN-jgbdhl0P1kaPRhlFH04xfQCQ1Najy0uiLkCgvlpvtRP7pW_w2AHrqnpNbeeCkwc8T_2AmFmqVxrV3Nmz-7iwS5VIMi7iD_DG4JTR3hJrM3uRoCAZtY8KCK2ScObAkwg1slABwkXj9Ft5GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس ترنس هست اما نجس هم هست؟!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18204" target="_blank">📅 12:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18203">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رسانه‌های غربی:
عمان قصد دارد پای کشورهای‌اروپایی را به تنگه‌ی هرمز باز کند و از آنجا که ایران قرارداد تقسیم تنگه را با عمان به امضا رسانده دیگر حق قانونی برای جلوگیری از این موضود ندارد.
در اولین قدم نیروی دریایی فرانسه قصد دارد در تنگه هرمز مستقر شود</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18203" target="_blank">📅 10:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18202">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">امروز پوتین با لباس نظامی با رسانه ها گفتگو کرده و عملاً می خواهد از اعتبار و جایگاه خود دفاع کند.  حس خوبی ندارم....</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18202" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18201">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ
:
ما مناقشه با ونزوئلا را در یک روز حل و فصل کردیم و ضربات بسیار سختی به ایران وارد کردیم.
طرف ایرانی بسیار مشتاق است و به هر طریقی به دنبال دستیابی به یک توافق سیاسی با ما است.
ما از روی حسن نیت به ایران یک هفته فرصت دادیم تا عملیات را متوقف کند تا مراسم تشییع جنازه برگزار شود.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18201" target="_blank">📅 09:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18200">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbbPFbmd5Hdy9igkE4zsohkGIXRZ3gZr0oisFjuKBFy9BpP50tClO4lC6KkAZoaMTQWzsCbJ0ywuVOI8dISc3m-m1n4iQls6XJYMvnSREaoRWHOTXqAXuijol0N8ZuspkDSpF1BKcR2wlWa01iJMwXs3QYq3MJ1o9VNfmC_jlZPvzwu8avUzqUid9PiFa1RkXkR4ZT8kiAvXPLpx9MrFNJZjrQ4xKyHoa5Vnwcdi5PQNuqlQLz8UxxS3TEdcjxTyloXhF49uYeXtGBbA4WK_fFnlwWQpI_Cdl-zt-Yf-VPUmEwUVrOrFoGcZBEAS9vWhm81Y18oEMDmsT6UOkvZoFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر جنگ هسته ای؟!
ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. د
ر ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی»
عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که نزدیک‌ترین فاصله به نقطه نمادین فاجعه جهانی در تاریخ است. این سازمان، تضعیف امنیت بین‌المللی، ضعف چارچوب‌های کنترل تسلیحات و رفتارهای فزاینده پرخاشگرانه قدرت‌های بزرگ را به عنوان دلایل اصلی این تصمیم ذکر کرد.
یکی از واضح‌ترین نشانه‌های این تضعیف، افزایش بکارگیری اصطلاحات هسته‌ای در گفتمان سیاسی و پوشش رسانه‌ای است. عباراتی مانند «حمله هسته‌ای»، «ضربه هسته‌ای»، «تهدید اتمی» و «تشدید هسته‌ای» بسیار بیشتر از چند سال پیش به کار می‌روند. در حالی که عبارت «حمله اتمی» بیشتر با اوایل جنگ سرد مرتبط است، گزارش‌های مدرن ترجیح می‌دهند از اصطلاحاتی مانند «حمله هسته‌ای» و «تهدید هسته‌ای» استفاده کنند. این تغییر نه تنها نشان‌دهنده تغییر زبان، بلکه نگرانی مجددی است که سلاح‌های هسته‌ای دوباره در محاسبات استراتژیک نقش مرکزی پیدا کرده‌اند.
جنگ در اوکراین نقش عمده‌ای در این روند داشته است. از آغاز این درگیری، مقامات روسی بارها امکان استفاده از سلاح‌های هسته‌ای را مطرح کرده‌اند، در حالی که دولت‌های غربی و تحلیلگران درباره اعتبار این تهدیدات بحث کرده‌اند. بولتن به طور خاص اشاره کرده است که جنگ روسیه و اوکراین با تحولات نظامی بی‌ثبات‌کننده و ارجاعات مکرر روسیه به سلاح‌های هسته‌ای همراه بوده است، که خطر محاسبه نادرست بین کشورهای دارای سلاح هسته‌ای را افزایش داده است. شکست‌های نظامی اخیر و فشارهای اقتصادی رو به رشد، بحث‌ها درباره گزینه‌های استراتژیک روسیه را تشدید کرده‌اند. گزارش‌ها و تحلیل‌ها بر فشارهایی که یک درگیری طولانی‌مدت بر تولید صنعتی، تحریم‌ها و زیرساخت‌های انرژی تحمیل کرده است، تأکید داشته‌اند. این فشارها باعث شده است که برخی تحلیلگران گمانه‌زنی کنند که مسکو ممکن است برای بازدارندگی از مداخله بیشتر غرب، بیشتر به سیگنال‌های هسته‌ای متکی شود. با این حال، فعلاً و در شرایط کنونی گمانه‌زنی درباره تصمیمات آینده روسیه نباید با شواهدی مبنی بر استفاده قریب‌الوقوع از سلاح‌های هسته‌ای اشتباه گرفته شود. کارشناسان نظامی و سیاسی عموماً چنین گفتمانی را بیشتر ابزاری برای اجبار و بازدارندگی می‌دانند تا نشانه‌ای قابل اعتماد از استفاده نزدیک از سلاح‌های هسته‌ای. با این حال کمبود گسترده بنزین و گازوئیل یا صف‌های طولانی سوخت در سراسر روسیه  بشدت روی روحیه و غرور ملی روسها تاثیر منفی گذاشته اند و برای نخستین بار از سال 2006 به این سو، مردم روسیه تصور می کنند استانداردهای کیفیت زندگی شان رو به نزول نهاده است. این مسئله روی پوتین و هیات حاکمه روسیه فشار می آورد تا دست به اقدامات تهاجمی تری برای تسلیم کردن اوکراین و ناتو بزنند که یکی از آنها می تواند بهره گیری از سلاحهای کشتار جمعی باشد.
از سوی دیگر، ناکامی نسبی آمریکا در دستیابی به همه اهداف نظامی اش در ایران نیز می تواند از دیگر حوزه هایی باشد که نهایتاً ترامپ را به استفاده از سلاح های هسته ای وادار کند. در این حوزه می توان به اشاره ترامپ به راهبرد «شرمن» استناد کرد که استعاره ای از یک استراتژی ویرانگر مخرب با تلفات بالا برای به تسلیم کشاندن دشمن می باشد. (
لینک
)</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18200" target="_blank">📅 02:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18199">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJfLy5HVgrBKiimqMiTUMHerd4Y5tFRJEqm9T-KDeqq_4iZn8_kqNkYOjiQXpQhk9Mg2YZwn4yzbzZ6Z5sAHSrHC6s5sC_bHmtlTNF43JNoXXEAPVf4xl2-GtIX12w3oay2L8Kx3SVZjnox2fiUUWybWOng70uhhGogjKJBVH0ac5aqPCRgrFkmLnMcLVCh9CyOUbGY56dsT82MZ6boIkqayAuGex2u-VQR_fc8ttH8_TsDM7q2jr5piQ_ao1O8eQQ5k0PLOLb7uKxC94TSBNbfuKJNWrBkboOz6Wa5Z03Hy6O6_6gokUFxK3vU6UmXz97QQ_zDOZVcyAJ0TFvMu4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در اینجا گفته شد که پوتین مانند گربه ای در گوشه اتاقی بسته گیر افتاده و این خطرناک است</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18199" target="_blank">📅 01:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18198">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TU7pm_ywvhRp3-Q_2M7_qyQ1vg1ZBZU8m7Xvi43q4L42n8XeozF7DKtlfUSecJr_0DE1-6g3r6xagJrYcSZHXojh0HpQm5aLX5cdK5FR34OyGtOTThJLwme4510aPK_ahOk7HXvkVjz7qfAFQEAlyMeXyJsSJg-XQ-rPYuOmDgdYBr3BsX-d31P2rvdxfuVt54DThm2aZVN8A9p5Xb0_lac8vFEAymqWdRnmG0AgmS9QqGiNercwhCPSwF4z39k8G4IHWkbvo2GAAPf5Nls7kjtvc4p2ED9FQYx33c9aGSR73NfVUSqWKYHZP0t8KkoV5IIxkMrWFJDS2QWoDiKYPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 1  جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18198" target="_blank">📅 01:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18197">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دونالد ترامپ در آخرین افشای مالی سالانه خود گزارش داد که در سال ۲۰۲۵ حداقل ۱.۴ میلیارد دلار از کسب‌وکارهای مربوط به ارزهای دیجیتال و میم‌کوین‌ها درآمد داشته است. ارزهای دیجیتال به‌وضوح بزرگ‌ترین منبع درآمد او بوده‌اند.   این گزارش همچنین نشان داد که او ۲۶…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18197" target="_blank">📅 22:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18196">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 1  جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18196" target="_blank">📅 22:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18195">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.  پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18195" target="_blank">📅 22:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18194">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">امام جمعه کرج:   اورانیوم غنی‌شده را رها نمی‌کنیم وتنگه هرمز را رها رها نمیکنیم</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18194" target="_blank">📅 20:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18193">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">امام جمعه کرج:
اورانیوم غنی‌شده را رها نمی‌کنیم وتنگه هرمز را رها رها نمیکنیم</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18193" target="_blank">📅 20:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18192">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">موسسه رتبه‌بندی فیچ، ریسک‌های مرتبط با ایران برای بخش‌های شرکتی در سطح جهان را مجدداً ارزیابی کرد
از دید این موسسه، شکنندگی توافق موقت ۶۰ روزه، به همراه عدم مشارکت اسرائیل، نشان می‌دهد که درگیری خاورمیانه همچنان تهدیدی برای صادرکنندگان شرکتی محسوب می‌شود.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18192" target="_blank">📅 20:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18191">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نتانیاهو و ترامپ توافق کردند که به زودی در ایالات متحده با یکدیگر دیدار کنند - رسانه‌های اسرائیلی.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18191" target="_blank">📅 20:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18190">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نتانیاهو و ترامپ توافق کردند که به زودی در ایالات متحده با یکدیگر دیدار کنند - رسانه‌های اسرائیلی.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18190" target="_blank">📅 20:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18189">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWeYPzVVmBsR_ZQlxeLn18v78JL76o577osYQLS7m6IvWrBDqSQIy2825TmPtQ8qnU6u712telH4YqWWLFaP_fiaUjhHzF25CB8IXbewE7XBA-bcpJAuQX1lrfV67Dcrism5LQKhUTmac3k0bq4lxlb22WUwP5whUGfadIbA6xMckVjFbyZpSzFxVx7RiJviOJZM2Qxm1PnllH3qFY_ExIj8OMVciFAV2y1jpXPb4knQUYl1ACdMqSaCnxg8XHgRYQSkNTyrejoCCy9X1vt4v8hNL59dc57haJfyPBEoj8E1mfr20oaoRFTtGfClbYQ6jB_K4u0o_64q8RKkCTeVdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه اندازی ساختمان عظیم وزارت دفاع مصر!
افتتاح مجموعه «هشت‌ضلعی» (The Octagon) به‌عنوان مقر جدید وزارت دفاع و فرماندهی راهبردی مصر را می‌توان یکی از مهم‌ترین نمادهای تحول ساختاری نیروهای مسلح این کشور در دهه اخیر دانست. این مجموعه عظیم که در پایتخت اداری جدید مصر ساخته شده، قرار است تمامی ستادهای اصلی نیروهای مسلح را در یک مرکز واحد گرد هم آورد و با بهره‌گیری از سامانه‌های پیشرفته فرماندهی، کنترل، ارتباطات و مدیریت اطلاعات، سرعت و هماهنگی تصمیم‌گیری‌های نظامی را به شکل قابل توجهی افزایش دهد.
ساخت چنین مرکزی تنها یک پروژه عمرانی نیست، بلکه بخشی از راهبرد بلندمدت قاهره برای تبدیل ارتش مصر به نیرویی مدرن، شبکه‌محور و آماده مقابله با تهدیدات متنوع منطقه‌ای است. طی سال‌های گذشته، مصر سرمایه‌گذاری گسترده‌ای در نوسازی تجهیزات نظامی، توسعه صنایع دفاعی و خرید سامانه‌های پیشرفته از کشورهای مختلف انجام داده و اکنون ایجاد یک مرکز فرماندهی یکپارچه، حلقه تکمیل‌کننده این روند محسوب می‌شود.
از منظر ژئوپلیتیکی نیز افتتاح «هشت‌ضلعی» پیام مهمی برای بازیگران منطقه دارد. مصر در سال‌های اخیر تلاش کرده جایگاه خود را به‌عنوان یکی از قدرت‌های اصلی نظامی و امنیتی خاورمیانه و شمال آفریقا تثبیت کند. تمرکز فرماندهی نیروهای زمینی، دریایی، هوایی و پدافندی در یک مجموعه واحد، ضمن افزایش کارآمدی عملیاتی، توان مدیریت بحران‌های هم‌زمان در جبهه‌های مختلف را نیز تقویت می‌کند.
همزمان، انتقال وزارت دفاع از مرکز سنتی قاهره به پایتخت اداری جدید، نشان‌دهنده اهمیت این شهر در ساختار آینده حکومت مصر است. دولت مصر با انتقال تدریجی نهادهای حاکمیتی به این شهر، در پی ایجاد مرکز سیاسی، اداری و امنیتی جدیدی است که از زیرساخت‌های مدرن و استانداردهای بالای حفاظتی برخوردار باشد.
در مجموع، افتتاح «هشت‌ضلعی» را باید فراتر از افتتاح یک ساختمان نظامی ارزیابی کرد؛ این پروژه نماد ورود نیروهای مسلح مصر به مرحله‌ای جدید از سازماندهی، فرماندهی و آمادگی عملیاتی است و می‌تواند بر موازنه قدرت و معادلات امنیتی منطقه نیز تأثیرگذار باشد.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18189" target="_blank">📅 20:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18188">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حوثی ها می‌گویند جنگنده‌های سعودی را از آسمان یمن بیرون کردند زیرا سعی در جلوگیری از فرود یک هواپیمای مسافربری ایرانی در صنعا داشتند.
آن‌ها هشدار دادند که اقدامات آینده سعودی با حملات به فرودگاه‌های سعودی و سایر اهداف حیاتی پاسخ داده خواهد شد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18188" target="_blank">📅 18:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18187">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">از زمانی که روس‌ها تلگرام را محدود کرده اند و ایلان ماسک هم استفاده دزدانه شان از استارلینک را محدود کرده، توان آفندی پهپادی ارتش ظفرنمون مسکووی بشدت کاهش یافته است.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18187" target="_blank">📅 16:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18186">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اسرائیلی ها، تاسیس پایگاه نظامی از سوی ترکیه در عمق خاک سوریه را به عنوان تهدیدی برای خود ارزیابی می کنند!  حملات ویرانگر اسرائیل ضد پایگاه T-4 نیز در همین راستا ارزیابی می شود.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18186" target="_blank">📅 15:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18185">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruVfjNgV1o8DEM6IKP6FYIX8LS0mM0nyvMqrD2p2N9489Q3hln6Vt_JWvfLA_ndVxnMIkZ5asHItGgLXY19Fo0ZbVn1jdeNwxphNJBfS8sKmxmAIdhiLVrNLRQ76j8CJ8sHbVYSI5nFGvrrLrvJAoX6aI-BiJJw17WQ4d56wtMKvFg_4aoVSi0cnqKWLk3UGOd9yAE6BIL93rm3GNHyo7NadZHMsw7H3jldrVbbNAViP84RtHmNiq0crq7BC9EKpUAT9U0mPOdTszm9F7QDa5HGq-hm_2rRt7BA8WnJWmPX0PXH-A2Cwzu5gkFFoIzbhLz4iYV7swBbRHX2PluOvHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس فرق این دوره ۶۰ روزه با بعدش این است که ممکن است بعدش آمریکا عوارض عبور بگیرد!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18185" target="_blank">📅 13:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18184">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-poll">
<h4>📊 مدت زمان و محتوای پادکست مطلوب است:</h4>
<ul>
<li>✓ کوتاه تر — بازاری تر</li>
<li>✓ کوتاه تر — بدون تغییر محتوا</li>
<li>✓ بدون تغییر در مدت زمان — بازاری تر</li>
<li>✓ بدون تغییر در مدت زمان و محتوا</li>
</ul>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 1  جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18184" target="_blank">📅 11:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18183">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 1
جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18183" target="_blank">📅 11:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18182">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJP0sX-3ONoo6H6_qctwCJ-lsltMZtpHZbleT030vVZBS0EW7KN09pKY4R98BJuPCqAuIa0kMdyGQVTqj_kdXM246Zkc56wx5gMrEg4KzgAMpgIkK1O1C_dz1cFNOHfh4Z5M1V02jBMBvTVrjjgF0xnomzhJwpPZlZPm0ZzeBK103DqlrWqAD3Poo3dwzbMZDOE-SlfeOk1nz0JcnV9F_Y-CvBa1aS0Xn9yRHld1xwcXIbRubuibLfDTb7qlqPtpiGtOgXPFbtmn81tG3KXCkxDfceSqUe1LpjBW6kBH_XZW_X859qL020OqGgERe48itl2dZGRzroQgaTdmeYZWGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز نسبتاً پایین است و ریسک پذیری ملایم پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18182" target="_blank">📅 10:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18181">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18181" target="_blank">📅 10:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18180">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تحلیل مهدی خانعلی‌زاده از مخالفین توافق با آمریکا از وضعیت اجرای تفاهم‌نامه پایان جنگ در روز چهاردهم</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18180" target="_blank">📅 10:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18179">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تحلیل مهدی خانعلی‌زاده از مخالفین توافق با آمریکا از وضعیت اجرای تفاهم‌نامه پایان جنگ در روز چهاردهم</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18179" target="_blank">📅 10:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18178">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rojl-r00C3DBFbuwqWVgyF41Y32Qm6n6l79fXzpaQchR6nVDavZCQqtyDd04tsSsz6sKDrWCoUSbQsd5JSE2wbFsKGFBzX4b_SfEOBKVin3N4eZt5sZlxNJh31NpNnxwHacayfMOzyDNv1H5tqhvmUBsOtje1r1amPrpHEkdXk0yTX_ejMEH06pcYrhSBJRVXRorBG7ZSNGBN5LQtSU1Ovrzfh4Pg_kfgJrndIDam74SgxHv0-xfAiIBMRCTx9Gg88BWzMrtEa3TPwLBQDBsaSQVuTwc5MgdBtzwekFoYJykq4ufgNyhRj3RjCsBJa39hZJQ65O4lN0FcbCO3ejJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیل مهدی خانعلی‌زاده از مخالفین توافق با آمریکا از وضعیت اجرای تفاهم‌نامه پایان جنگ در روز چهاردهم</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18178" target="_blank">📅 10:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18177">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">همکاری نظامی اسرائیل-مراکش و پیام راهبردی به مادرید
همکاری نظامی اسرائیل و مراکش دیگر صرفاً یک رابطه تجاری در حوزه صنایع دفاعی نیست؛ این همکاری به تدریج به یکی از مهم‌ترین مؤلفه‌های معادلات ژئوپلیتیکی غرب مدیترانه تبدیل شده است. از انتقال فناوری پهپادهای انتحاری و سامانه‌های شناسایی گرفته تا تولید مشترک برخی تجهیزات نظامی در خاک مراکش، شواهد نشان می‌دهد که تل‌آویو در حال سرمایه‌گذاری بلندمدت بر ارتقای توان نظامی رباط است.
این تحول زمانی اهمیت بیشتری پیدا می‌کند که در کنار سردی بی‌سابقه روابط اسرائیل و دولت چپ‌گرای اسپانیا قرار گیرد. دولت مادرید در دو سال گذشته از منتقدان جدی سیاست‌های اسرائیل در غزه بوده، از به رسمیت شناختن کشور فلسطین حمایت کرده و در مجامع بین‌المللی مواضعی اتخاذ کرده که با مخالفت شدید تل‌آویو روبه‌رو شده است. (لینک ها:
یک
|
دو
|
سه
) طبیعی است که این تنش سیاسی، بر محاسبات راهبردی اسرائیل نیز تأثیر بگذارد.
در چنین فضایی، افزایش توان نظامی مراکش پیامدهایی فراتر از شمال آفریقا دارد. مراکش همچنان ادعای حاکمیت بر سئوتا، ملیله و چند قلمرو اسپانیا در سواحل آفریقا را حفظ کرده است. هرچند رباط بارها تأکید کرده که این موضوع را از مسیرهای سیاسی دنبال می‌کند، اما از نگاه بسیاری از ناظران اسپانیایی، تجهیز ارتش مراکش با فناوری‌های پیشرفته اسرائیلی، موازنه قوا در غرب مدیترانه را به زیان اسپانیا تغییر می‌دهد. پرسش نمایندگان حزب راست گرای Vox ووکس در پارلمان اسپانیا درباره آمادگی این کشور در برابر پهپادهای انتحاری ساخت مشترک اسرائیل و مراکش نیز بازتاب همین نگرانی است.
سیاست بین‌الملل، برداشت بازیگران نیز به اندازه نیت آنها اهمیت دارد. حتی اگر انگیزه اصلی اسرائیل اقتصادی یا ژئوپلیتیکی باشد، نتیجه عملی آن افزایش فشار امنیتی بر کشوری است که در سال‌های اخیر یکی از منتقدان اصلی سیاست‌های تل‌آویو در اروپا بوده است. از این منظر، تسلیح مراکش را می‌توان نه لزوماً «مجازات» اسپانیا، بلکه پیامی راهبردی در راستای بازآرایی موازنه قدرت در غرب مدیترانه دانست؛ بازآرایی‌ای که به‌طور طبیعی هزینه‌های راهبردی بیشتری را بر مادرید تحمیل می‌کند و می‌تواند بر محاسبات آینده دولت اسپانیا در قبال اسرائیل نیز اثرگذار باشد.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18177" target="_blank">📅 01:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18176">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff61a516b.mp4?token=grMbOMd_o0sr4DwjKsha8YSgZ8Mrckdi7xCklyOwWBFkH5-4v1jih0vDneEDOGXGgDwQzfThGjtUE7y6VOZoWUPO0wiAXV1YpGkldHAd9nc-n3Nbay-sBFvG9WRRiInTJERIMht30_NSGyXSx0Zw7anJvoJCTDUv0pcL8eId7k1xr95XJSK6kLvCkaLJ-UGZtqW8Z7QkqcGxqzNl_T-fx9LfbExFKTqVTa0vBGBobpGj31PZb-0DgqeJjXUDDytx10T0DcWAzyt4yhO8pbNWc298-FvHt2jC0eLKB1sfAfTLbDRzmiPB_1GZhb_svzWfj3VUJlPZAfAL_0JLBCHOMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff61a516b.mp4?token=grMbOMd_o0sr4DwjKsha8YSgZ8Mrckdi7xCklyOwWBFkH5-4v1jih0vDneEDOGXGgDwQzfThGjtUE7y6VOZoWUPO0wiAXV1YpGkldHAd9nc-n3Nbay-sBFvG9WRRiInTJERIMht30_NSGyXSx0Zw7anJvoJCTDUv0pcL8eId7k1xr95XJSK6kLvCkaLJ-UGZtqW8Z7QkqcGxqzNl_T-fx9LfbExFKTqVTa0vBGBobpGj31PZb-0DgqeJjXUDDytx10T0DcWAzyt4yhO8pbNWc298-FvHt2jC0eLKB1sfAfTLbDRzmiPB_1GZhb_svzWfj3VUJlPZAfAL_0JLBCHOMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  ما رادارهای ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند.  ما چند شب قبل دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18176" target="_blank">📅 01:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18175">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ:
ما رادارهای ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند.
ما چند شب قبل دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18175" target="_blank">📅 01:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18174">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مسؤولان آمریکایی نگران بودند که اسرائیل ممکن است در طول مذاکرات صلح حساس در بهار امسال، از جمله وزیر امور خارجه عباس عراقچی و رئیس مجلس محمدباقر قالیباف، رهبران مذاکره‌کننده ایران را ترور کند.
با نگرانی از اینکه چنین حمله‌ای مذاکرات را متوقف کرده و جنگ را دوباره شعله‌ور کند، واشنگتن از کشورهای منطقه خواست تا ایران را از این خطر آگاه کنند.
ایران اقدامات امنیتی گسترده‌ای برای محافظت از هیئت خود انجام داد، از جمله اسکورت نظامی و تغییر برنامه‌های سفر پس از دریافت اطلاعاتی درباره احتمال حمله اسرائیلی.
منبع: نیویورک تایمز</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18174" target="_blank">📅 22:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18173">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-poll">
<h4>📊 در‌ جنگ میان ترکیه و اسراییل دوست دارید:</h4>
<ul>
<li>✓ پیروزی ترکیه</li>
<li>✓ پیروزی اسراییل</li>
<li>✓ جنگ فرسایشی بدون برنده</li>
<li>✓ من Gay هستم و دوست دارم جنگ نشود</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18173" target="_blank">📅 22:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18172">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18172" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18171">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وزیر امور خارجه ترکیه، هاکان فیدان:
سیاستمداران آمریکایی تا زمانی که حمایت از اسرائیل به منافع خودشان خدمت کند، از اسرائیل حمایت می‌کنند.
این پویایی آن‌قدر طولانی شده است که همسویی بین حمایت از اسرائیل و پیشبرد منافع ایالات متحده به عنوان یک فرض دائمی تلقی شده است.
با این حال، برای اولین بار از زمان نسل‌کشی در غزه، تحلیل‌هایی که ظهور کرده‌اند به نتیجه متفاوتی اشاره دارند: «سیستم موجود در حال کار علیه منافع ماست.»
هیچ‌کس ادامه سیستمی را نمی‌خواهد که در نهایت علیه منافع خودشان کار می‌کند.
در سراسر جهان، از دانشگاه‌ها تا روزنامه‌ها، احساسات ضد اسرائیلی به‌طور چشمگیری افزایش یافته است.
چرا؟ زیرا مردم می‌بینند که اسرائیل آشکارا در حال ارتکاب کشتار است و در هر جایی که اقدام می‌کند، نقش بی‌ثبات‌کننده‌ای ایفا می‌کند.
در گذشته، آن‌ها می‌توانستند این موضوع را با چند مانور رسانه‌ای ساده پنهان کنند. اکنون، دیگر نمی‌توانند آن را پنهان نگه دارند.
اسرائیل در حال حاضر به دنبال یک دشمن جدید است.
تا زمانی که اسرائیل — یا هر بازیگر دیگری — به روش‌هایی عمل کند که با منافع ملی و منطقه‌ای ما در تضاد است، ما هیچ دلیلی برای ترسیدن، مردد شدن یا عقب‌نشینی نداریم.
ما مشکلی با رویارویی نداریم. اگر به آنجا برسد، برای ما مسئله‌ای نیست.
اسرائیل فقط مشکل من نیست؛ مشکل جهان است.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18171" target="_blank">📅 21:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18170">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وزیر دفاع اسرائیل:
ارتش اسرائیل باید برای انجام جنگ مستقل علیه ایران آماده شود.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18170" target="_blank">📅 21:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18169">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">عبدالمجید حکیم الهی، نماینده رهبر ایران در هند، گفت که به دلیل نگرانی‌های امنیتی، بعید است آیت الله مجتبی خامنه‌ای در مراسم تشییع جنازه پدرش شرکت کند.
وی افزود که آیت الله مجتبی خامنه‌ای مایل بود نماز میت را اقامه کند، اما مقامات امنیتی این کار را بسیار خطرناک دانسته‌اند.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18169" target="_blank">📅 21:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18168">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تولید نفت خام کویت در ژوئن به طور میانگین ۱.۶۵ میلیون بشکه در روز بود در مقابل ۵۷۸,۰۰۰ بشکه در روز در ماه مه</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18168" target="_blank">📅 19:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18167">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🩵
کاتز ؛ وزیردفاع دولت اسرائیل
:
ما درحال توسعه لیزرهای فضایی برای تهاجم خارج از جو زمین هستیم
يسرائيل كاتز ،  اعلام کرد دولت اسرائیل در حال توسعه لیزرهای فضایی به منظور توانایی حمله در فضا است.
به گزارش اورشلیم ،پست کاتز در نشستی با خبرنگاران نظامی گفت: یکی از اهداف اصلی که نخست وزیر و من تعیین کرده ایم این است که برترین استعدادها را جذب کنیم تا امروز هیچ کشوری توانایی اجرای حمله در فضا را نداشته است. ما باید در برخورداری از این توانایی کشور پیشرو جهان باشیم
او افزود: اگر به این هدف دست یابیم این امر میتواند برتری بازدارندگی، توانایی حمله و انهدام و دیگر برتری های راهبردی ما را در برابر دشمنانی که از منابع گسترده برخوردارند تضمین کند
کاتز پنجشنبه گذشته گفته بود اسرائیل مصمم است به بازیگر پیشرو در زمینه توانایی حمله از فضا تبدیل شود با این حال این نخستین بار بود که به طور مشخص از لیزرهای فضایی نام می برد
اسرائیل هم اکنون نیز در این حوزه از کشورهای پیشرو به شمار میرود و سامانه موسوم به پرتو آهنین (Iron Beam) را به عنوان یک لیزر فضایی مستقر در زمین تولید کرده است
سامانه پرتو آهنین که اواخر سال گذشته به ارتش اسرائیل تحویل داده شد نقطه عطفی تاریخی به شمار میرود زیرا نخستین سامانه دفاع لیزری عملیاتی جهان است که میتواند راکتها پهپادها و خمپاره ها را با هزینه ای بسیار کمتر از رهگیرهای سنتی، خنثی کند</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18167" target="_blank">📅 16:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18166">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فرمانده سپاه پاسداران قم
:
تمهیدات زیادی اتخاذ کردیم اما بصورت قطعی نمی‌دانیم در مراسم تشییع رهبرانقلاب چه اتفاقی خواهد افتاد</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18166" target="_blank">📅 15:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18165">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دور بعدی مذاکرات آمریکا و ایران در ۱۸ ژوئیه (۱۶ روز دیگر) آغاز می‌شود.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18165" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18164">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔻
غضنفری ؛ نماینده مجلس
:
یک شبه کودتای سیاسی علیه رهبری نظام درجریان است - تجمعات شبانه نباید جمع شود</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18164" target="_blank">📅 13:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18163">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دلار ۱۷۷۰۰۰ تومان!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18163" target="_blank">📅 11:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18162">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjeb-UFk0D2CepxA-wabdZdo-A3m_i0X-zigKQlcbl65dSlcigPJFk_waIIqbFXK9-OuaRmOapR1zwHvgGZg5Bi_HSGWOMnD5xtdj33_9BxTxQu9vnDVOyfFTV28zYWBPusbda_3Rq-r3ItTnbMPGcsEXMBX_cILtjVjs1rZwZlWIC2d8jg4CzmG2U0_w9wQvotQAWwe6e-9iQUHRWecVt92NY6hx9WNphW4DwE1NiRVCu6b8VpdzrMmLqhRosRnQqAYp7ieWFzGb6kQHforVYsP9ZynO1o1TUGiAtRfzWmrt2eJn3SyOqlXzyPoIqRp3SvE39QK4_6zAK7lD-vbrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیکی برای امروز در سطح بالایی قرار دارد.
توصیه می شود با توجه به انتشار گزارش NFP، امروز با کمترین حجم معامله کنید.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18162" target="_blank">📅 09:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18161">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">جهش انفجاری معاملات شخصی ترامپ در سه ماهه نخست ۲۰۲۶!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/18161" target="_blank">📅 01:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18160">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گویا گروه‌های مسلح تجزیه طلب کردی با حزب الله طاق زده شده اند.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/18160" target="_blank">📅 01:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18159">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آمریکا رسماً توافق‌نامه‌ای برای ساخت سفارت دائمی در اورشلیم امضا کرد.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18159" target="_blank">📅 00:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18158">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سقوط بالگرد MH-60S Seahawk نیروی دریایی ایالات متحده در دریای عرب
ناوگان پنجم ایالات متحده اعلام کرد که یک بالگرد MH-60S Seahawk نیروی دریایی ایالات متحده که به ناو هواپیمابر USS George H.W. Bush اختصاص داده شده بود، اوایل روز چهارشنبه در دریای عرب فرود اضطراری انجام داد.
سه نفر از چهار خدمه در وضعیت پایداری پیدا شده‌اند. جستجو برای یافتن نفر چهارم در حال انجام است.
ناوگان پنجم اعلام کرد که هیچ نشانه‌ای مبنی بر اینکه این وضعیت اضطراری ناشی از اقدام خصمانه بوده باشد، وجود ندارد و علت آن در دست بررسی است.
این دومین سقوط بالگرد نظامی ایالات متحده در منطقه در هفته‌های اخیر است.
یک بالگرد AH-64 آپاچی ارتش در 9 ژوئن در خلیج عمان سقوط کرده بود که ترامپ گفت که نیروهای ایرانی آن را سرنگون کردند و خدمه توسط یک قایق بدون سرنشین Corsair نجات یافتند.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/18158" target="_blank">📅 20:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18157">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">جی‌دی وانس در مورد ایران:  چند روز پیش چند بمب روی آنها انداختیم. می‌دانید چرا؟ چون ایرانی‌ها به کشتی‌های تجازی شلیک می‌کردند.  چند بمب انداختیم، اهرم فشار اعمال کردیم و در عوض در سه روز گذشته، عبور و مرور تجاری آزاد داشته‌ایم.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/18157" target="_blank">📅 20:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18156">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جی‌دی وانس در مورد ایران:
چند روز پیش چند بمب روی آنها انداختیم. می‌دانید چرا؟ چون ایرانی‌ها به کشتی‌های تجازی شلیک می‌کردند.
چند بمب انداختیم، اهرم فشار اعمال کردیم و در عوض در سه روز گذشته، عبور و مرور تجاری آزاد داشته‌ایم.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18156" target="_blank">📅 19:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18155">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">موجودی نفت خام آمریکا در ذخایر استراتژیک نفت (SPR) در هفته گذشته به پایین‌ترین حد از ماه مه ۱۹۸۳ رسید - EIA|</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18155" target="_blank">📅 18:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18154">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ذخایر نفتی آمریکا و جنگ با ایران  آمریکا از ذخایر راهبردی نفت به‌عنوان ابزاری برای مدیریت شوک‌های بازار و کنترل فشار انرژی استفاده کرده و کاهش اخیر این ذخایر باعث شده بازسازی آن‌ها به یکی از اولویت‌های مهم واشنگتن تبدیل شود.  برخی تحلیلگران معتقدند کاهش تنش…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18154" target="_blank">📅 18:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18153">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/po0UqvK5nIDBeahT1HN_lR0gbtMP0fsAiZLc1_0uanNPwIs-zxcYMRKjz2hTlg8ooNANpzI8MmlFlcnp4auClnF932NJoUTeYNZ2yV0vIhN-5cILcYBlwmWaVpIQBKhscDNOAh0u9Q7jEDEwck-KcbihVNNWQbM8e05koXRZ08XwsMLObn7ssS0J3UmIQE33Wri4R6VyVeDICpSQDml8OJxPt0NvogxxWaPvjZZ7MoEWjoX8uISmOce6PFfGIfMz-jiwCGZs8j2TRiXOWgpE39uok6bzf8x1CLnzY3apiD_FiNa98wZdmuqPzzD5sHkoTZm1nX0bVkIUkbHrjw7_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای سومین روز متوالی ، امانوئل مکرون با عینک آفتابی دیده شده است.
به نظرتان کار آن عفریته زنش است یا صبیه وجیهه رفیق بهزاد؟!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/18153" target="_blank">📅 15:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18152">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گفته می‌شود با اجرایی شدن این توافق، قیمت چص فیل در سرزمینمان بزودی ۹۰ درصد سقوط می کند</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18152" target="_blank">📅 15:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18151">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">به گزارش العربیه، آمریکا و ایران به توافق اولیه برای آزادسازی ۳ میلیارد دلار از دارایی‌های مسدود شده ایران دست یافتند.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18151" target="_blank">📅 15:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18150">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">#GRI  شاخص Geopolitical Risk Index برای امروز در حالت Clear قرار دارد و احتمالاً شاهد افزایش جریانات ریسک پذیری خواهیم بود.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18150" target="_blank">📅 15:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18149">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPHVTFDt_p-Cd-ruK4dEQAIOQ3a3Of9ndWOAjjcbr6LQ6tsJ3IYawIBrWGujwsoeK0Ne6q9qjfpbdMFZpRDk5aXOgeapWOJvu9fjxh32rWuqaGOs11BjytvxqKUH410NSoEkC8wzkhSCdjjDlF2nKs5TFsXtYT4sRjuc7dIwNYHZ-9AvzAzl6727wKDDNnNpHivc0Rw0hAGhzAAhPzDbLvui4WJ4AQiXg36Z3Rp6ypR9CGdRJd9at7h_o4oswloC9sLajtPHC54ZVEtoUp7X1Rg3KLrZpnbM0OMspvDWGfGu5rffRaFRtqQ69Ij1XgYv1X0m5ih13mLI1Njjp8D3wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشد دارایی های ریسکی و افت بهای نفت!</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18149" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18148">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtT7RzEfbaHWUGPNlHfv_M-uEtN8K7d7cobYirwZm7_DUXCeKlhcmMPwSka2s6urZQZQoy8luGeA3RGlLk0goOnYMdzIfWgAs70Dja7_Fzpy7i4By2R85r67HZg0KLXPlUc1fAOhnL20XFzf_QjnSi7NbiY5jm05kvVDXtnNRuJLUN9WF3U15pWGvxDxnreXguPfjYjfyJkJc3R_NEDP_RdvLv_r484tdLaLmLaI4ORxh1GyfiIRSy4G-0vIzuXH9Ydbp7pETUBYO8fT6ypwinw20gsKrZoJmhtOIrbHie15eAskVYTjmlhMQYGE-eqgWPkDCoCXJexQ8xrVO7JWTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص Geopolitical Risk Index برای امروز در حالت Clear قرار دارد و احتمالاً شاهد افزایش جریانات ریسک پذیری خواهیم بود.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18148" target="_blank">📅 14:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18147">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">عراقچی در پاسخ به تهدید کاتز برای ترور رهبر جدید ایران:
شرایط تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است.
رئیس‌جمهور آمریکا متعهد شده است که حیوانات خانگی خود را در تل‌آویو ساکت نگه دارد. اگر آنها به ارباب خود توجه نکنند، ایران به آنها درس خواهد داد.
هر تهدیدی علیه مردم و رهبری ما پاسخ فوری و قدرتمندی دریافت خواهد کرد.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/18147" target="_blank">📅 14:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18146">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c5e5e0c5.mp4?token=AGCUXMKhOjIrbykHJOl8V7862IRG0ayVlcxyxWdOvQWtUqaUovXQjz86PelnIubWD1I-cee0IGyqv9iPecOK1dyW0J-2cXQKaiV32xhXuq3sVW9eto-R8Gzc3q5PeGrVoes_AmTPQ-1RsyymLxOtm0ESo6J7zf8RMryycNaphEDx51eeid_R9yF-Y479Iy1TxhkBz70ui6-hLV-PnaoaxjwfM_SjmpFXksK-SY6D-dBxqJNKPzj3cE4mSZJMUy-bboJVZIOAAKnCRHnEKw90ISQgIou_DtEYtMp2iRF47182xjaP-5p9jqwziljxuX48-VhBsg86CoyQUlMrAAcrBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c5e5e0c5.mp4?token=AGCUXMKhOjIrbykHJOl8V7862IRG0ayVlcxyxWdOvQWtUqaUovXQjz86PelnIubWD1I-cee0IGyqv9iPecOK1dyW0J-2cXQKaiV32xhXuq3sVW9eto-R8Gzc3q5PeGrVoes_AmTPQ-1RsyymLxOtm0ESo6J7zf8RMryycNaphEDx51eeid_R9yF-Y479Iy1TxhkBz70ui6-hLV-PnaoaxjwfM_SjmpFXksK-SY6D-dBxqJNKPzj3cE4mSZJMUy-bboJVZIOAAKnCRHnEKw90ISQgIou_DtEYtMp2iRF47182xjaP-5p9jqwziljxuX48-VhBsg86CoyQUlMrAAcrBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ذخایر نفتی آمریکا و جنگ با ایران  آمریکا از ذخایر راهبردی نفت به‌عنوان ابزاری برای مدیریت شوک‌های بازار و کنترل فشار انرژی استفاده کرده و کاهش اخیر این ذخایر باعث شده بازسازی آن‌ها به یکی از اولویت‌های مهم واشنگتن تبدیل شود.  برخی تحلیلگران معتقدند کاهش تنش…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18146" target="_blank">📅 14:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18145">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">محبوبیت فردریش مرز  به پایین‌ترین میزان خود رسیده است!  بنا بر گزارش بیلد و با استناد به داده‌های مؤسسه تحقیقاتی INSA، حدود دو سوم آلمانی‌ها از عملکرد صدر اعظم فریدریش مرز ناراضی هستند.  این رسانه اضافه می‌کند که حدود ۷۰٪ از شهروندان آلمان از عملکرد دولت ناراضی‌اند.…</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/18145" target="_blank">📅 14:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18144">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">💳
اعتراض عضو فقهای شورای نگهبان به بازشدن اینترنت بین‌الملل
🔹
مدرسی یزدی
:
باز گذاشتن شبکهٔ جهانی اینترنت بدون ملاحظات کارشناسی دقیق از جانب متخصّصان متعهّد، به انواع بهانه‌هایی که نمی‌تواند جبران‌کنندهٔ آسیب‌های همراه آن باشد ـ از قبیل آنکه کسب مردم آسیب می‌بیند یا حقّ مردم است یا خلاف وعدهٔ انتخاباتی رئیس‌جمهور محترم است ـ کاری بسیار خطرناک است. این کار، اقتصاد کشور، امنیّت شغلی مردم، امنیّت داد‌و‌ستد‌های تجاری، امنیّت نهاد‌های مهمّ کشوری و امنیّت شخصیّت‌های مؤثّر نظام و سلامت روانی اقشار مختلف مردم به‌ویژه نوجوانان و جوانان را در تیررس دشمن آمریکایی صهیونی قرار می‌دهد</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18144" target="_blank">📅 13:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18142">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8kBQF45ZGxraHw0NNRrznJLfFzmQTK48AgdaMLSh1WAIGJyOGdUfBzuxp5bK3j4V9dc2z-HOMaGbcOqT7l6OZ08A3sSZvjJroZpwGSdq1bKbXQB-Nhc-2pPJt0PTz22tQ_V6j38w15YtIHpuoEGoV70HjjZtlTja_MRiIfLtjwohBTuW2U_AqdDm3D9zGQ17mIklsowwojA8KUogkuKc7oTxHV-SNqzxcnnlA852yGcXDBLhsYyshEdCL0o2K59zfGL3tOItLsKN02hQptZFC2KgqWv8Dv7qt9nLXttW-Bch7FHTXE8_2J-kMGNNmQ37CLoAe1b87ZldUkqfwhRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖌
از امروز اینجا پادکست های روزانه ژئوپولیتیک و بازارهای مالی ارائه خواهدشد.  یک شاخص ریسک ژئوپولیتیکی هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18142" target="_blank">📅 12:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18141">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18141" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🖌
از امروز اینجا پادکست های روزانه ژئوپولیتیک و بازارهای مالی ارائه خواهدشد.  یک شاخص ریسک ژئوپولیتیکی هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18141" target="_blank">📅 11:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18140">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">Secret Box
pinned «
🖌
از امروز اینجا پادکست های روزانه ژئوپولیتیک و بازارهای مالی ارائه خواهدشد.  یک شاخص ریسک ژئوپولیتیکی هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.
»</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/18140" target="_blank">📅 11:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18139">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🖌
از امروز اینجا پادکست های روزانه
ژئوپولیتیک و بازارهای مالی
ارائه خواهدشد.
یک
شاخص ریسک ژئوپولیتیکی
هم طراحی کرده ام که هر روز 2 بار در ساعت های 10 و 18 بروزرسانی می شود.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18139" target="_blank">📅 11:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18138">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fdau58IMoE-zzLi6nJf0k_PnGeiekp-FUOaNuvfZqMhEj48zxpT9fk9qvrXZ4ENVyJX6asgPerxKH6ssqAE-HYYp_q4Vmy6KB95r5IfXWpwZr3TNc67W6NMrjwua3T-kwWLqk_eYb33CQTDmnO5uFUiUh4zRgQEb-x5TyUxvXSyZmt08LLhOZeZjj2GMkitCXLFdiuIlPNi6S1qNLmjryuKqITlWTEoOb4WmMXSmwP5Gfn30kGnbQjQMubBnY5G3x__aLpcfD_9-54kbzSi8HzayTlFzthxaIdt8XvVvjuNle3RiOJomBBaHlrPED10YSLmlXGrXCETdaVUAwSk7gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اظهارات جدید قاسمیان:   واشنگتن را اشغال کنید؛ ترامپ را دستگیر کنید و به ایران بیارید</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18138" target="_blank">📅 10:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18137">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اظهارات جدید قاسمیان:
واشنگتن را اشغال کنید؛ ترامپ را دستگیر کنید و به ایران بیارید</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18137" target="_blank">📅 10:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18136">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvFLIlxBHZJ5Xdz6hccI-2gO1HIirIl7gQAytIO8aNeBiKjoLIN4eAQLezOxwS1lMAZemYQiQgDUTvug1tHDit_WvRwEbGQ8qvZU9V6bQ7ksTdIZ87nh3ryVvhdgBRU8OnUpObza8Sa5eXvTiLYqtNvVQZ5gjxd1ppyW44WgyE1Zg6uhqjqtnKUxzZVMj0ymMUqp7cbqPzzXQCnvvF7XNAmyHl4lJpTWcn6kKIHqLqjYFXIFYkUxN704UtYgCMPz9f6yfSpXc9-znz5OTD0P-jK1ivKIssPk5gEyImctRCpiEfR9F69KkJFwzRK4KYCj2_n-rTfiV0X_HEHwD-cnPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18136" target="_blank">📅 10:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18135">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0ar7sKcPVRQKBMsH_VCXcgSv-kWp0osB1V_WbeIXw0nQBnMK6GdSsdPoHQkIehgUIxc8dGLak9vgSquwwINgrkxbVklwT6x4NO1E-wTj4d7mc8L1HxIKfVJcc8fRiolMtGC4IQo6LleuX_CrcF-3tCNw2OpYN8UB8-21Q9cD4UxZ8eWP00-GtL65pfAnJCaYEq3r9va5H7u0fJ4G12LmOQXqlR-C6ks49tQU0jj2ETFFbjBQMk_oUca0ZbvQ8IWQCQUMW5YwDsiNBeKE5IxCp4x_McGJeJSerAPVHgop1bKEDU_JwGvVmXJwkJ-jTCk9rA0Ksh4tq-t7Ffdsv7dNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد دو ناو آبی‌ـ‌خاکی آمریکا، باکسر و پورتلند، در حال حرکت به سمت خاورمیانه هستند.
این دو ناو معمولا برای انتقال نیرو و عملیات آبی خاکی و ... مورد استفاده قرار می‌گیرند.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18135" target="_blank">📅 10:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18134">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فراخوان‌هایی برای اسکان مجدد در غزه پس از مصاحبه نتانیاهو
بنیامین نتانیاهو در مصاحبه‌ای با «پاتریوت‌ها»، بازگشت به اسکان یهودیان در غزه را رد نکرد، که این موضوع باعث شد قانون‌گذاران برای تبدیل این چشم‌انداز به واقعیت و اصلاح «ظلم تاریخی» جدایی سال ۲۰۰۵ فراخوان دهند.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18134" target="_blank">📅 09:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18133">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">— دو عضو سپاه پاسداران در یک حمله مسلحانه در شهرستان پاوه در غرب ایران کشته شدند و دو نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18133" target="_blank">📅 09:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18132">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46100c7aab.mp4?token=dsDNwuMSvxNs-C2Ms4cBj0FJ5CFUEeBXpH5bhHfARvncDTZuZXiy0dj9IrfzH0RMHlMcdlaSrvdDjdbeAsdzbcp8b5kV63P85WX-NqRids15rBsQ4yPhVOdMIKJY9ksjbZHtYGPZsEGO_lAe1I76mk2VYsM_EhUlpJmDqHwwVWi3apBupiLKrI5ga4mArWKL0dqv5S_6f5lH-0R2tSSnyhmdAS07Gg9fqqMMCl94x4ZcOzPg8JhzDYebFhq_Dk6r03nwaEdsHQbjpYBXarcst2R0eN5_RKHxVSIp9geeXL5569Xfnt3PsXyho0d-Qouw5RONWTIbFCCMbWRF6i1YPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46100c7aab.mp4?token=dsDNwuMSvxNs-C2Ms4cBj0FJ5CFUEeBXpH5bhHfARvncDTZuZXiy0dj9IrfzH0RMHlMcdlaSrvdDjdbeAsdzbcp8b5kV63P85WX-NqRids15rBsQ4yPhVOdMIKJY9ksjbZHtYGPZsEGO_lAe1I76mk2VYsM_EhUlpJmDqHwwVWi3apBupiLKrI5ga4mArWKL0dqv5S_6f5lH-0R2tSSnyhmdAS07Gg9fqqMMCl94x4ZcOzPg8JhzDYebFhq_Dk6r03nwaEdsHQbjpYBXarcst2R0eN5_RKHxVSIp9geeXL5569Xfnt3PsXyho0d-Qouw5RONWTIbFCCMbWRF6i1YPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد خوش چشم:
«یک چیزی از آقای حاجی زاده بگویم که احدالناسی نمیداند جز خانواده اش
که آنها هم به من نگفتند!»</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/18132" target="_blank">📅 23:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18131">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">جِی‌دی ونس درباره ایران:  یکی از چیزهایی که درباره ایرانی‌ها برایم هم جذاب است و هم ناامیدکننده، این است که آن‌ها می‌گویند «نه، نه، نه، هیچ گفت‌وگوی صلحی در جریان نیست»، اما گفت‌وگوهای فنی بین ایالات متحده و ایران درباره توافق صلح در حال انجام است.  این یک…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18131" target="_blank">📅 23:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18130">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ادای تنگ ها را درنیاورید و بگذارید رستم بخسبد</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18130" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18129">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">قالیباف رئیس مجلس ایران:
تحریم‌های نفتی برداشته شده و ما نفت را ۲۰ درصد گران‌تر می‌فروشیم</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18129" target="_blank">📅 22:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18128">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3db8e4f93.mp4?token=WzDm0BIBsJy52T2gPLHwnkquczSEwS70W8gBOkMnFmmIeZQl7VxxeExX9H4QTzG06nzrwS71tFuVpgbQ_7UcfxsUWsQ-ezzui_cjo6ajE79XPLfYzEnqMjiLndbAu5iZTri6PwAII2IpY9aN4lGgPCfTGqXbQlWB80hdufbUMTESVOAcPNYjcWRNfBUchuZWVc6FSEi22AgZ_0jOjz-Ne9IjfhoA4Ty0q5R0DzTLgTP9oBAducDnAXjeTJhRmG0NuX7-XyYWpP36JD4xGUK5qWv-Necsd6YK5Y06zzrXZjcPEvYJxdePVEJxMjbPBoxnXfbK6TCdbnFs-4bMpBkWx5VkJJGQcmgJ45zzOA7IgHf3kgL-JH-66kdWJ5OvcvdPPBgVrl7JtZ7HqQ__NKqcrsKHqDMPKXjNJbk-UzKFnjgLi1xe7Jj0LpWCj3m38uzvjRb0uHEEveYAT3JMWQljVArDwZqWC4vm_WAyTCRlW-U8S6u60bHlpeE6ORO52Fh9684gNziyu1jIYdJUQR76d6SHWO_TqHsadoxonTk-ng-v5agd1aVUafDVIxpKtPNcPDkkgxhc6O32DzCRfeVruIfIuWcawgp0FrOQDSf6G1mfGT1ZuyEYgj1WwEDnDsAxm2tJ6FN7aEdUwGHhukBYgOoQ4ebC12AjC7NpSyfAJsk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3db8e4f93.mp4?token=WzDm0BIBsJy52T2gPLHwnkquczSEwS70W8gBOkMnFmmIeZQl7VxxeExX9H4QTzG06nzrwS71tFuVpgbQ_7UcfxsUWsQ-ezzui_cjo6ajE79XPLfYzEnqMjiLndbAu5iZTri6PwAII2IpY9aN4lGgPCfTGqXbQlWB80hdufbUMTESVOAcPNYjcWRNfBUchuZWVc6FSEi22AgZ_0jOjz-Ne9IjfhoA4Ty0q5R0DzTLgTP9oBAducDnAXjeTJhRmG0NuX7-XyYWpP36JD4xGUK5qWv-Necsd6YK5Y06zzrXZjcPEvYJxdePVEJxMjbPBoxnXfbK6TCdbnFs-4bMpBkWx5VkJJGQcmgJ45zzOA7IgHf3kgL-JH-66kdWJ5OvcvdPPBgVrl7JtZ7HqQ__NKqcrsKHqDMPKXjNJbk-UzKFnjgLi1xe7Jj0LpWCj3m38uzvjRb0uHEEveYAT3JMWQljVArDwZqWC4vm_WAyTCRlW-U8S6u60bHlpeE6ORO52Fh9684gNziyu1jIYdJUQR76d6SHWO_TqHsadoxonTk-ng-v5agd1aVUafDVIxpKtPNcPDkkgxhc6O32DzCRfeVruIfIuWcawgp0FrOQDSf6G1mfGT1ZuyEYgj1WwEDnDsAxm2tJ6FN7aEdUwGHhukBYgOoQ4ebC12AjC7NpSyfAJsk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیریت Secret Box حدود ۲ سال پیش این ایده را مطرح کرد که این روانی عوضی را در قالب یک معامله بکشند که هم برای ایران خوب بود و هم برای اسراییل و اتفاقا ۴ ماه بعد این فراخوان لبیک گفته شد اما سوگمندانه ناموفق بود!  مردک حمال یک دیوانه کامل است و می‌توان او را…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/18128" target="_blank">📅 20:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18127">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وال استریت ژورنال:
اولویت‌های متضاد ایران مذاکرات صلح آمریکا را به خطر می‌اندازد</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18127" target="_blank">📅 20:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18126">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نتانیاهو رفته از جنوب لبنان بازدید کرده!
از این جهت خیلی شبیه احمدی نژاد است؛
منتهی احمدی نژاد سفرهای استانی اش به شهرهای ایران بود اما نتانیاهو عمدتاً به مناطق تصرف شده کشورهای دیگر سفر می کند (غزه، سوریه، لبنان....)</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18126" target="_blank">📅 18:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18125">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اسپوتینک:  اختلاف با عربستان، جنگ ایران و تله هرمز عواملی که ممکن است امارات متحده عربی را به سمت خروج از اوپک سوق داده باشد  دکتر ممدوح جی. سلامه، اقتصاددان پیشکسوت نفت، به اسپوتنیک گفت: «مدت‌ها قبل از جنگ ایران، امارات متحده عربی به دلیل اختلاف با عربستان…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18125" target="_blank">📅 18:09 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
