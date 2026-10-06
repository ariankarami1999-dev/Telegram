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
<img src="https://cdn4.telesco.pe/file/S9B9kIyi8lXd4A0uVrKd9eP-V2Zpg4QTr1DILuCrm1-XtKv-MvKyNs9Ook7o56fyzg_DrTsEhqRgtsFHJ38OqtRtvy2ATwCoFgSUeDJN2kyHzaM6akIyov53CqehxTZb_iKTX0TRBvJOYMYMKtvSjCzGjqGSxQawwt9ed3iUiPQOrtkv89api_EHtntBX5MnsaKXKVo8T8RAqUmR-gODC7V8sfp0mghDZq5dV0Twmq19vhzWaHKPA8JKp92VvfZd1KNXZbKyi5GOZlYTHvhqDEUUzrcNH9FM3UJXoQqUwFliR8rm0dj1tA2dlg2o8CoZaE9WGxyDeNoqQJJQgxguvw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 11K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 17:18:01</div>
<hr>

<div class="tg-post" id="msg-21504">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فوری - قطر اعلام کرد که ایالات متحده و ایران همچنان در حال مذاکرات برای پایان دادن به جنگ هستند</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/21504" target="_blank">📅 15:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21503">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترکیه و پاکستان برای حمایت از عربستان سعودی در برابر یمن، توافق‌نامه مکه را فعال کردند
آنکارا و اسلام‌آباد متعهد شدند که به‌سرعت نیروهایی را به داخل خاک این پادشاهی اعزام کنند.</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/21503" target="_blank">📅 15:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21502">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کلا هر بدبختی در هر جای جهان باشد یک پایش هندی است مگر اینکه بنگلادشی باشد.</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SBoxxx/21502" target="_blank">📅 14:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21501">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خلبان آن هواپیمای فلای دوبی هم که داشت سقوط می‌کرد هندی بود!</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SBoxxx/21501" target="_blank">📅 14:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21500">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وزارت امور خارجه هند:
۱۲ خدمه یک کشتی تجاری با پرچم پاناما در حمله‌ای در سواحل عمان زخمی شدند که ۱۱ نفر از آنها هندی بودند</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SBoxxx/21500" target="_blank">📅 14:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21499">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و می توان در سطوح حمایتی خرید کرد.</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/21499" target="_blank">📅 14:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21498">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نشست کارشناسی بسیار جالب و دیدنی درباره روند جنگ ایران—عراق و فرصت هایی که برای پایان جنگ وجود داشته است:
https://www.aparat.com/v/goil745?playlist=27887251</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SBoxxx/21498" target="_blank">📅 14:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21497">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انصارالله ادعا می‌کند که در دو روز گذشته حمله دوم به فرودگاه سعودی را انجام داده است
انصارالله اعلام کرد که با یک موشک بالستیک به فرودگاه بین‌المللی ابها در استان عسیر عربستان سعودی حمله کرده و ادعا می‌کند که این ضربه باعث اختلال در ترافیک هوایی فرودگاه شده است.
یحیی سریع، سخنگوی نظامی انصارالله، گفت که ضربه موشکی «دقیق و مستقیم» بود و به شرکت‌های هواپیمایی بین‌المللی هشدار داد که از ادامه پروازها از طریق فضای هوایی سعودی خودداری کنند، زیرا به گفته او این فضا به «صحنه عملیات نظامی ما» تبدیل شده است. ریاض تاکنون به‌طور فوری این حمله را تأیید نکرده است.
این حمله پس از حملاتی رخ داده که انصارالله در شب دوشنبه به فرودگاه‌های جازان و نجران نسبت داده بود و پس از آن حملات، مصدومیت‌ها و خساراتی گزارش شده بود.</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/21497" target="_blank">📅 13:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21496">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فرانسه برای اولین بار موشک بالستیک جدید خود با قابلیت حمل سلاح هسته‌ای را از یک زیردریایی هسته‌ای آزمایش کرد</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/21496" target="_blank">📅 13:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21495">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikUdo9QwnaYscNiRn0Qaq-hOTFRz_F8NUvwPstsQ-i5cRmwJqtfAX_0BqjMtK0KjUSMWjAsaFyTBjWYkYtBCS9ZWR_YDQO68Jyq1Us1hWrozqspOxZ28GpzsNgUyH0dSyjvwq5aro-vB8zJ_dqkMVgTXpmfyxUgZSFfJCHz1Ogltucv8nhd2umOQdGnSwFLCFywk8zD3FbNGLOd8uAe5ftaRLxwamScKjNIAfNTW2yuw87Z_mXL3DIWhG7M1nT6lDraXwxl4kxD2Xh74DBD0Haa91Nx3Jsu-VBe3RFhN4QI2PrAoQbONU33LssSULG2Q68eysyygOzHo__nAC8v4UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر وقت یک نفر که ذهنش اسیر تفکر فرقه ای نشده  فهمید که میان توران بزرگ با اسرائیل بزرگ کدام بیشتر به زیان ماست و آن را بدون هراس بر زبان آورد آن وقت می توان امیدوار بود که پویه های ژئوپولیتیک بر محاسبات کلان سیاست خارجی کشور حاکم بشود و نه انگاره های وهمی…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/21495" target="_blank">📅 11:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21494">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">موسسه مطالعات جنگ درباره کوشش ایران برای بهبود و ارتقای توان موشکی خود:
ایران به احتمال زیاد در حال بازسازی و ارتقای توان خود برای هدف‌گیری اهداف نظامی دوربرد آمریکا در منطقه و کشتیرانی تجاری از طریق بهبود دقت، برد، سرعت و قابلیت‌های هدف‌گیری موشکی است. سخنگوی ارتش ایران، سرتیپ محمد اکرمی‌نیا، در مصاحبه‌ای با رسانه‌های ایرانی در ۴ اکتبر اظهار داشت که ایران در حال بهبود دقت، برد و سرعت همه موشک‌های خود است. اکرمی‌نیا افزود که ارتش باید برد موشک‌ها را افزایش دهد تا نیروهای آمریکایی در منطقه را هدف قرار دهد و اذعان کرد که نیروهای آمریکایی تا ۱,۰۰۰ کیلومتر دورتر از ایران جابه‌جا شده‌اند.
مقام‌های آمریکایی در ژوئیه ارزیابی کرده بودند که ایران نسخه‌های پیشرفته موشک بالستیک میان‌برد خیبرشکن را علیه پایگاه‌های آمریکا مستقر کرده است. این مقام‌های آمریکایی اشاره کردند که ایران این موشک‌ها را برای گریز از دفاع‌های آمریکایی از طریق مسیرهای پروازی متنوع، سرعت‌های متفاوت و مانورهای فاز پایانی، و از قابلیت پرتاب متحرک موشک برای ارتقای بقای پذیری و اثربخشی موشک تغییر داده است. ایران همچنین در آخرین حمله خود به نیروهای آمریکایی در اردن در ۹ سپتامبر موشک‌هایی با کلاهک‌های مهمات خوشه‌ای شلیک کرد. مهمات خوشه‌ای در ناحیه‌ای وسیع پخش می‌شوند و برای بیشینه‌سازی گستره خسارت طراحی شده‌اند، هرچند اثر هر گلوله‌ به‌صورت فردی را کاهش می‌دهند. ایران در حملات قبلی علیه اسرائیل از مهمات خوشه‌ای استفاده کرده است که عمدتاً برای جبران کمبود دقت در حملات موشکی بالستیک ایران انجام شده است.
اظهارات اکرمی‌نیا همچنین در پی اعلام ۲۱ سپتامبر دبیر شورای عالی امنیت ملی ایران، سپهبد محسن رضایی، مبنی بر اینکه ایران اخیراً یک موشک جدید با کلاهک مهمات خوشه‌ای را در حمله‌ای به ناو یو‌اس‌اس جورج واشینگتن آزموده و این سلاح در نزدیکی ناو هواپیمابر اصابت کرده است، مطرح شده است. گلوله‌های خوشه‌ای تقریباً به‌یقین نمی‌توانند یک ابرناو را غرق کنند، اما می‌توانند عرشه را آسیب بزنند و به این ترتیب عملیات پروازی را تا حدی و برای مدتی مختل کنند. رضایی احتمالاً به حمله ایران به ناو هواپیمابر آمریکا در ۹ سپتامبر اشاره می‌کرد. رسانه‌های ایرانی در آن زمان گزارش دادند که ایران از موشک بالستیک میان‌برد قاسم بصیر استفاده کرد که برد ۱,۲۰۰ کیلومتری دارد و کلاهک بازگشت قابل‌مانور آن برای گریز از پدافند هوایی طراحی شده است. اشخاص مطلع، 3 حمله موشکی بالستیک ایران به کشتی‌های جنگی نیروی دریایی آمریکا در اوایل سپتامبر را در گفتگو با وال‌استریت ژورنال در ۹ سپتامبر «خیلی نزدیک‌تر از حد انتظار» توصیف کردند.
ایران ممکن است این اصلاحات موشکی را بر حملات موشکی خود به کشتیرانی در تنگه هرمز اعمال کند. ایران از ۲۹ سپتامبر حملات تقریباً روزانه‌ای به کشتی‌های در حال عبور از تنگه انجام داده است. یک مقام آمریکایی همچنین در ۴ اکتبر به وال‌استریت ژورنال گفت که ایران توان خود را برای هدف‌گیری کشتی‌ها بهبود داده و خطر برای کشتیرانی در تنگه را در هفته‌های اخیر افزایش داده است. ایران ممکن است از شرکای خود برای بهبود قابلیت‌های هدف‌گیری خود پشتیبانی دریافت کند، چراکه به‌گزارش‌ها روسیه اطلاعات هدف‌گیری ارائه کرده و جمهوری خلق چین تصاویر ماهواره‌ای به ایران داده است که احتمالاً به هدف‌گیری ایران در طول این درگیری کمک کرده است.
ایران به احتمال زیاد با اولویت‌دادن به بهبود قابلیت‌های موشکی خود، در پی افزایش توان بازدارندگی خود در برابر حملات هوایی آمریکا به دارایی‌های ایرانی، تحمیل هزینه به ایالات متحده و حفظ ابتکار عمل راهبردی در این درگیری است. همان مقام آمریکایی همچنین در ۴ اکتبر به وال‌استریت ژورنال گفت که ایالات متحده کارزار خود علیه نفت‌کش‌های ایرانی را در واکنش به حملات ایران به کشتیرانی تجاری، پس از حمله ایران به پایگاه هوایی آمریکا در اردن متوقف کرده است. این مقام احتمالاً به حمله موشکی مهمات خوشه‌ای ایران به پایگاه هوایی موفق السلطی در اردن در ۹ سپتامبر اشاره می‌کند.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/21494" target="_blank">📅 11:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21493">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaKHP5sfyBnduMzxX6M6w_aBOOtodvB0tfB4PVY_XY26AFHzMnAbks4YcpiqfaV6cCiTYOzNbK4WYXZwlM4nEmR5khIYsjXXHOhI_8CT3ZGJugGJtXCJ7RjKKpqj-rDX6lPv_g11FK_Cui69gJlB3VcS27VzExn6Jq2ZHmz5bbFLJI_X68paky41AUxZtboob7mfLwUScbWPvQpe0Q6xDX8mc5hhQ2m28BuqCjPgBkoPXzWvaYe-RXEJDo1dCRQJwg5Zq_rq9X_gjN-jAj1SsjRbZwRGrSPbg0vNQvnMhrkwr0coHaVaCDzrFauvp6k5XXvOcYC8OafYQrP8GqJKGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueGap
نمایه FVC فرق خاصی با دیروز نکرده چون قیمت عملاً همانجا است.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/21493" target="_blank">📅 10:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21492">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiRwT9dtKFfGQC2E6_w6m404RFlm4qUJs3JyvXfM4Jt9AHE8eq9lLLGfTcEvuO3SUOShyvR_f0yCjMBSqbemtBnmmCmlrGE88BmE_PlSGhP8wbh-BIIPBq3qxEds2PxtrrKYFA1cKQNDr2_mZifBNad76rjP6LCE6EX_DhIneva2mlzGT_mQsksCnPeBqNeo81uQ-cZqrKmXgBBNDfKW6nTxblZWtEjfg9ZJCFviUq25M0DnZSXB1bgvp08hdeHEocQcbXdcB6t_sG9P66dSH1uXfkuojzWG9F_AyHF_Ha2S8xE51yFzJwcCl-DY0sTDE7SKy9p5bbt64CnvbUuO1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و می توان در سطوح حمایتی خرید کرد.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/21492" target="_blank">📅 10:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21491">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atYj7Y39shS2zLjohQz6dpqm7FBSwJ5ihONE_ja9m4ZKIaMZq-l750PdC2KVmXXZoXpsuYkNyU4i6nnnlZSqWmr9mG1H15EDYZS30Pp3TcMBh15XrIHcNZcq4L19MRn4DHoIVOsTA7KvASIjNM47jNjm_8sXcOBKd9v_FW40K6mo_wZnUEL6gx9ZXBOXU6tXxRsHN5pYFbaERu8QLEIr6FGWV8lOAx31sgW0b8QZZHlPSU847uIM1NhYz945UJfg-PdKmokJWQBSFIeIKSvsGzxB2sPR1mIWs0eoGO03ajZwwlzlNs-PwVhh1z2yAuIp1Pv4B8lNjzseoaL3ElR27Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، استفاده از اعدام با شلیک گلوله را برای مجازات نیدال حسن، که در پایگاه نظامی فورت هود در ایالت تگزاس، ۱۳ نفر را به قتل رساند، تایید کرد.
این اولین اعدام نظامی با شلیک گلوله از زمان پایان جنگ جهانی دوم خواهد بود.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/21491" target="_blank">📅 10:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21490">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DET5dd-Ba8qU0P2PZa0XDrxYhYIlrGnfyV_NmiKLlh2lrvzirNnBLP3JZET6mzbm0ojMYohL-Mv7JMJIIvp3SSWTSEWnQqUxd1aoX8U2n5BnXMYtmP-xbM85AyNfn7i_GXcdkx8Qvk4b7FWurZqPwH7jOaGOuvVHCwTSNYE2RRT5ddufUgkL2vBYyin7LhpIYA9uznJSywkdaBs_OnGwRAhB4c61lU6N06bmp5pEL3OPWB8pUn2l4cH3MvvVR5sYSweFZ_dCKfL6CEnt1_LTMSHEM_0broF0vSGL3_Y-7LOPvxgeViT7rJ9R3zCed2EfKlLaHed1bW887V_KVgk7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طاعونی که در روسیه از آزمایشگاههای قرمساقها نشت کرده، تا ۱۰۰ برابر کشنده تر از کروناست!</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SBoxxx/21490" target="_blank">📅 22:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21489">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">💥
«هدف بعدی اسرائیل ترکیه است»
پل کریگ رابرتز می‌گوید که پس از یک کمپین برای شیطانی‌نمایی ترکیه—مشابه آنچه علیه ایران انجام شد—آمریکا به نمایندگی از اسرائیل به ترکیه حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21489" target="_blank">📅 21:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21488">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گویا فاکستان دارد به صورت رسمی وارد جنگ ضد حوثی ها می شود.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21488" target="_blank">📅 19:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21487">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گویا فاکستان دارد به صورت رسمی وارد جنگ ضد حوثی ها می شود.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/21487" target="_blank">📅 19:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21486">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👤
مارکو روبیو، وزیر خارجه آمریکا
:
«ما طاعون روسیه را از نزدیک زیر نظر داریم و آن را به‌دقت رصد می‌کنیم. فکر نمی‌کنم دلیلی برای نگرانی و هراس وجود داشته باشد، اما قطعاً موضوعی است که باید با دقت و تمرکز بیشتری دنبال شود.»</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/21486" target="_blank">📅 18:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21485">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نیویورک تایمز:
بیش از ۲۰۰ پرسنل نظامی و اطلاعاتی ایالات متحده به عربستان سعودی اعزام شده‌اند تا مستقیماً به نیروهای مسلح این پادشاهی در هدف‌گیری سایت‌های پرتاب و تأسیسات ذخیره‌سازی موشک‌هایی که توسط جنبش مقاومت انصارالله یمن اداره می‌شوند، کمک کنند.
این مأموریت مشاوره‌ای مخفی شامل تیم‌های کماندویی است که در طول مرز عربستان-یمن مستقر شده‌اند و در کنار فرماندهان ائتلاف برای کمک به جمع‌آوری اطلاعات، تداخل در حملات فرامرزی و تقویت توانایی‌های دفاعی ریاض در برابر حملات انتقامی پهپادی و موشک‌های بالستیک، همکاری می‌کنند.</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/21485" target="_blank">📅 17:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21484">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کلیپی از کشتار نیروهای حوثی توسط سلفی های مورد حمایت عربستان   در ثانیه ۳۳ فردی که گزارش میداد می‌گوید باب المندب عربی است و نه فارسی ایران!</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21484" target="_blank">📅 17:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21483">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57336f8d3e.mp4?token=GpA68hFVxvvCtUsn5H7FHcaFlE9VGUVzkPkiZ7WXu_uAYp1zKIqsADckX535ZwSZYUJVNCJHTZAxBkTmAuOf71_3K-HOlaKQQ8wZAsOQduZ2JXX1T6fhg0KeWD1TLyGQiZMxbinUKMcEhtmj7r4CFwgs2iybIPYEJ67hA_O2b9pP0g62HTw8ZTyMGc0nv_2mMN28OgIvj1QTps4wJtbj5IcLdNnF_we-Jt-CYCPAOsJRWXynYSQnsEjUIEPZvG1nS4-woBz46RZoO3h3SptjwPyZ-4VezX5TZcQv4D2weYY1a9qZ6KOV8PK56xYYvmcQBIPBeXNJR24atkELSe13BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57336f8d3e.mp4?token=GpA68hFVxvvCtUsn5H7FHcaFlE9VGUVzkPkiZ7WXu_uAYp1zKIqsADckX535ZwSZYUJVNCJHTZAxBkTmAuOf71_3K-HOlaKQQ8wZAsOQduZ2JXX1T6fhg0KeWD1TLyGQiZMxbinUKMcEhtmj7r4CFwgs2iybIPYEJ67hA_O2b9pP0g62HTw8ZTyMGc0nv_2mMN28OgIvj1QTps4wJtbj5IcLdNnF_we-Jt-CYCPAOsJRWXynYSQnsEjUIEPZvG1nS4-woBz46RZoO3h3SptjwPyZ-4VezX5TZcQv4D2weYY1a9qZ6KOV8PK56xYYvmcQBIPBeXNJR24atkELSe13BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا توضیح داده بودم …</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21483" target="_blank">📅 17:44 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21482">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">— مقامات اسرائیلی پرونده‌ای علیه یک استاد ریاضیات دانشگاه که مردی در دهه ششم زندگی  و اهل پتاح‌تیکوا است به اتهام برنامه‌ریزی برای حملات گسترده علیه شهروندان عرب اسرائیل تنظیم کرده‌اند.
بر اساس دادخواست، هدف او اجبار به اخراج دائمی آن‌ها به اردن، لبنان و غزه بود.
او قصد داشت ۷۲ اسرائیلی یهودی را در ۱۲ گروه برای انجام حملات هم‌زمان جذب کند، با حمایت از عناصری در ارتش اسرائیل، از جمله حملات هوایی به مراکز جمعیتی عرب.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21482" target="_blank">📅 17:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21481">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اینجا توضیح داده بودم …</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21481" target="_blank">📅 15:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21480">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">احتمال اینکه کل داستان جنگ یمن در روزهای اخیر یک تله برای حوثی ها باشد وجود دارد…  توضیح خواهم داد.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21480" target="_blank">📅 15:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21479">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیدالله کریمی پور</strong></div>
<div class="tg-text">باب المندب؛ قدرت های بزرگ‌ بر می گردند؟!
وقتی ۲۹ شهریور(۲۰ سپتامبر)‌ نوشتم به زودی حوثی ها ناگزیر خواهند شد از باب المندب عقب نشینی کنند، سخت مورد نفد قرار گرفتم.  البته امروزه روز، مساله اصلی این نیست که حوثی ها شکست خوردند یا عربستان پیروز شد؛ بلکه مهم‌تر این است که باب المندب در حال خارج شدن از وضعیت اهرم یک بازیگر غیر دولتی(حوثی ها) و برگشتن به مرکز رقابت دولت های منطقه ای و قدرت های بزرگ‌ است.
پسگرفتن باب المندب از تسلط حوثی ها، در چارچوب بازآرایی ژئوپلیتیک ی پس از بحران ایران ـ آمریکا معنا دارد، نه صرفا یک عملیات جدید در جنگ یمن.
اگر باب‌المندب توسط مخالفین حوثی ها تثبیت شود و همزمان فشار بر هرمز ادامه پیدا کند، یک نتیجه بسیار مهم حاصل می‌شود:
دو گلوگاه دریایی خاورمیانه، به جای آنکه اهرم‌های مستقل ایران و حوثی‌ها باشند، ممکن است به تدریج تحت ترتیبات امنیتی چندجانبه عربستان، آمریکا و کشورهای غربی قرار گیرند. و این برای ایران از خود عملیات امروز مهم‌تر است؛ زیرا در آن صورت، عمق ژئوپلیتیک ی ایران در دو سوی شبه‌جزیره عربستان همزمان محدودتر می‌شود.
به لینک‌ زیر سری بزنید:
https://t.me/Karimipour_K/6256
#یدالله_کریمی_پور
#karimipour_kپ</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21479" target="_blank">📅 15:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21478">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خوش چشم:
اگر آمریکا بمب اتم بزند، ما هم پدر بمب‌ها را به آمریکا می‌زنیم</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/21478" target="_blank">📅 14:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21477">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">لوئیز ایناسیو لولا دا سیلوا و فلاویو بولسونارو به دور دوم انتخابات ریاست‌جمهوری برزیل راه یافتند
با شمارش نزدیک به ۹۹ درصد از آرا، بولسونارو ۴۷.۲۸ درصد و لولا دا سیلوا ۴۴.۸۷ درصد آرا را به دست آوردند.
دور دوم (Runoff) در ۲۵ اکتبر برگزار خواهد شد. این دور به این دلیل برگزار می‌شود که هیچ‌یک از نامزدها بیش از ۵۰ درصد آرا را کسب نکرده‌اند.
لولا دا سیلوا، رئیس‌جمهور فعلی، نماینده حزب کارگران چپ‌گرا است. فلاویو بولسونارو، فرزند جیر بولسونارو، رئیس‌جمهور سابق برزیل، نماینده حزب لیبرال است.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21477" target="_blank">📅 14:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21476">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اعتراضات گسترده در اسپانیا؛ خیزش علیه دولت چپ‌گرا و سیاست مهاجرتی سانچز  موج تازه اعتراضات در اسپانیا علیه دولت پدرو سانچز، نخست‌وزیر سوسیالیست این کشور، به یکی از جدی‌ترین چالش‌های سیاسی دولت او تبدیل شده است.   کانون اصلی اعتراضات، بحران مهاجرت در سئوتا،…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21476" target="_blank">📅 14:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21475">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">📌
بحران مالی فرانسه: قلب لرزان اروپا  فرانسه در پاییز ۲۰۲۶ با بدهی و کسری بودجه بی‌سابقه، افزایش هزینه تأمین مالی و رشد اقتصادی ضعیف روبه‌روست؛ وضعیتی که نگرانی‌ها درباره ثبات مالی دومین اقتصاد منطقه یورو را افزایش داده است.  در کنار فشار بازارها، بن‌بست سیاسی…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21475" target="_blank">📅 12:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21474">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKG3_dHvOEKfkPH15y8i-b2G4JrKfoe7JtGA4DtwK6NjEA7p1FfiqPV3didUbU48RwAEzEkomkvtMaS6P0VVF_TbCgklXgAaihZK9TOxlTLsgaNfHvp_MrCK5BpZ7kKdbv7nD_ZA1UyZPf8_1AZuhYVU8jPIsSyNUgJAF2q9TNnZhsmYDLRkZ7PxdhaXCJRnowZu_I0MBTooUS-Rz7X8JHyjMF1_cKmf1pkOFhf4iyJSuk4hbSp-iaQcyMT9wf-FikHJsdw4axz39X4URCWzxcIaY3dOtTKFNpP8NJdn_CRV5Ytgjvb0Dh6Zc0EXAoXP9IvPeluDG7-rYIve4VFubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
بحران مالی فرانسه: قلب لرزان اروپا
فرانسه در پاییز ۲۰۲۶ با بدهی و کسری بودجه بی‌سابقه، افزایش هزینه تأمین مالی و رشد اقتصادی ضعیف روبه‌روست؛ وضعیتی که نگرانی‌ها درباره ثبات مالی دومین اقتصاد منطقه یورو را افزایش داده است.
در کنار فشار بازارها، بن‌بست سیاسی و دشواری تصویب برنامه‌های ریاضتی، مسیر کاهش بدهی را پیچیده کرده و بحران مالی فرانسه می‌تواند به یکی از مهم‌ترین چالش‌های اروپا تا انتخابات ۲۰۲۷ تبدیل شود.
📎
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
✔️
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21474" target="_blank">📅 12:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21473">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGAV9VW5DCCkINnwLCumzf31pn1nDsImGSenjUQoDVNIghUClsMj-IgOld-Er68_aneg0tuK9SoGEcThIki5lcXVZlak6ANSyUQhTj3o4A8LBaLMeaErdm7JJO_6CNugkPVBBEKLiXJY7rw4wtYQonWs98LJOhI63_B08nSGPUrcry9Gq9Kwu_eSeOeIlmjauznzlUt1--Xhq_jnktlbW-PdPpt34Tv_DcWqRqkBwRo_pAJWGaEAU_k9puwEU8_3kM1-_QOjvjAKc1kTV_qLf9xf-eZi56FBLswZcC04SEq2tl8UsMuQUeOhAI4iaeJ3Vsa2NsfTCAOq38b7odLgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله  به گشت پلیس در بمپور  بر اساس گزارش‌های اولیه و به گفته منابع آگاه، یک گشت پلیس در شهرستان بمپور هدف حمله تروریستی قرار گرفته است. این منابع از شهادت یک نفر از نیروهای پلیس در این حادثه خبر داده‌اند.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21473" target="_blank">📅 10:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21472">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و پیش بینی می شود طلا رشد خوبی از همین محدوده ها به بالا داشته باشد. (دستکم 400 پیپ)</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21472" target="_blank">📅 10:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21471">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5I978k5fIPfjc0ayBjYox2wfdZSvBBqaRJDPMFXcxohnZ0X1_FtgBfVf25G9qqzRqv4rrzPlwO1VFBCZds2ZNGcrUqHkYn7ncWrNayyu-QbwQADdAYGd2yQSMuyBM2CK9jOi6rGkxjwhWqKgx2crmcUp2O07n6SEQK_grULZB2B-rm0D0dVRqCi1Zta93JwoDcxXpoCdRnGCnJQOMU72dxrytQ66WfNn0rr0ml93uUcwKCAgqAoRushd6zJBBbLZuawvHbECL1ZUCJ70i95YH028tDYXnUIlzNkH1Yt5o1Gq4XYPKo2e41Ikz5LFgyobn8UQj5nxw_Evnb36GZrbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC کماکان در سطوح پایینی قرار دارد و فضا برای رشد طلا هموار است.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21471" target="_blank">📅 10:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21470">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBOCsGlwPCwei8Etpy-9qjBKGheODDkDYSHDRfKaC8kVZX39tLmQdbN9bjf0ddPI6vzH-9avGrKNyfItLrBl2KasrUbkEw3QxELh9wdy2BljXkinu7G7DtPYfx2KJ_YK3KJbAi6qQXY8seEuPQJIfA2X0uxqihgV8HBHQLEgjO9T2AQN2McEmFZzJCFZ2Y9asLPrRNdLOrUky38iQKNOFBFnP0YsxyQQ9zKIzciR61eUHDH7KP3kQNHoa2s_U16k22t625YUdm99QT319TYUNE1txV-SqAO9uNlXHBND6ZZUHgeKoEFslnU4aI_UZqs_pLHhc_YSo7DQuVwI8W-2iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی قرار دارد و پیش بینی می شود طلا رشد خوبی از همین محدوده ها به بالا داشته باشد. (دستکم 400 پیپ)</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21470" target="_blank">📅 10:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21469">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وزیر اقتصاد:   تورم کاهش پیدا خواهد کرد و وضعیت تولید و ارز خوب خواهد شد</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21469" target="_blank">📅 10:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21468">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وزیر اقتصاد:
تورم کاهش پیدا خواهد کرد و وضعیت تولید و ارز خوب خواهد شد</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21468" target="_blank">📅 10:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21467">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21467" target="_blank">📅 09:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21466">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mz_xSFkax1j3UzG4va4-aAtk6QRs5QbQ33nuvRFV0m5NWeTSouuN74eLfbDaxG1QUlAXmbLFqCcH24NX_mZLxmHBukdXPdDr69hnq1_dXTeWpI1eWzJAYS3bM1me_MLtPqJ4_ThnLjLvIFajvpM574exByv_RJnPbX9RPSee0rCeqgzbB1ge8ctD40dEujdZkU3IHp4CElIUuAgWRiReYunDBuW6XE-qdKrT1f52ufPdQWwXmnZJi5VjwSXvb6RoCvuwAI5m9_o_nI98tIN8QOZ5axePaMk9nLGeDKqs1Ta3nLG5eNEmJmc9BZr2PmtdIOO9XVZaJ8F_fR9aNwmA2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/21466" target="_blank">📅 02:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21465">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حضور نظامی آمریکا در اسرائیل در حال افزایش است. در حال حاضر حدود ۳۰۰۰ سرباز در این کشور مستقر هستند و انتظار می‌رود نیروها و هواپیماهای بیشتری به آنجا اعزام شوند.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21465" target="_blank">📅 01:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21464">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">حضور نظامی آمریکا در اسرائیل در حال افزایش است. در حال حاضر حدود ۳۰۰۰ سرباز در این کشور مستقر هستند و انتظار می‌رود نیروها و هواپیماهای بیشتری به آنجا اعزام شوند.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21464" target="_blank">📅 01:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21463">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUPjABF8RWnhzsdMOeJYGs8dtPXkLxOLjEWq7IdXmVu5jwVt5tXAMXb14yd0jnS-vwQB9t2g1-kVA3Gt4g4182KU2l4IdFnNhwoP3DJzJkEEAWeGFjouKL6K5lWObO3TYR-TNTP2drDxL6sIBQuuTzTDy3vxcNrDUBdPslKuM6warepl9bWlGJ72BHEunVwthDbyDyVMj4pvCWXg0VU4sECamizBg-9FCZrrDNqtZCBN_Lgu2-MoXdQnb1FefGIw9JcSSVs2ArN8WzqI8DntUxANGhfyvuWGy5GhSNicrwYr2H_8CUDiFHeHogsC8xJoeYISqimFZfX1w8F9sDWmDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر سیاستهای ضدمهاجرتی ترامپ!
طی ۵۰ سال گذشته، دست‌کم ۲۳ میلیون نفر متولد آمریکای لاتین به ایالات متحده مهاجرت کردند. این بزرگ‌ترین جریان پیوسته مهاجرت در جهان به یک کشور بود که در سال‌های پس از کرونا به اوج رسید. دولت‌ها و مردم آمریکای لاتین به این موضوع — و به پولی که ساکنان جدید آمریکایی برای خانه می‌فرستادند — عادت کرده بودند.
سپس دونالد ترامپ دوباره به قدرت رسید. در سالِ منتهی به ژوئیه ۲۰۲۶، گمرک و حفاظت مرزی آمریکا در مرز جنوبی ۱۳۷ هزار مورد برخورد مأمورانش با مهاجران را ثبت کرد؛ یعنی ۹۴ درصد کاهش نسبت به همان دوره در سال ۲۰۲۴ که ۲.۴ میلیون برخورد ثبت شده بود. مسیر دارین — مسیر جنگلی از آمریکای جنوبی به پاناما — همین داستان را روایت می‌کند: عبور از این مسیر در همین دوره ۹۹.۹ درصد کاهش یافت. در کاستاریکا شمار مهاجرانی که به سمت شمال می‌روند تقریباً به صفر رسیده، در حالی که تعدادِ رو به جنوب به‌شدت افزایش یافته است (نمودار ۱). شلوغ‌ترین کریدور مهاجرتی جهان ساکت شده است.</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/21463" target="_blank">📅 01:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21462">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گزارش از صدای جنگنده های ارتش در آسمان تهران</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SBoxxx/21462" target="_blank">📅 23:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21461">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گزارش از صدای جنگنده های ارتش در آسمان تهران</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SBoxxx/21461" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21460">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">به نظر می رسد محاصره شهر راهبردی تعز در یمن از سوی حوثی ها تکمیل شده و کار نیروهای مورد حمایت سعودی در این شهر به پایان خود نزدیک می‌شود</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SBoxxx/21460" target="_blank">📅 19:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21459">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏ مهدی کوچک‌زاده نماینده تهران در جلسه امروز مجلس:   به خدا اگر از جهنم نمی ترسیدم خودم را جلوی بانک مرکزی آتش میزدم ‎ ‎</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SBoxxx/21459" target="_blank">📅 19:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21458">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏
مهدی کوچک‌زاده نماینده تهران در جلسه امروز مجلس:
به خدا اگر از جهنم نمی ترسیدم خودم را جلوی بانک مرکزی آتش میزدم
‎
‎</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SBoxxx/21458" target="_blank">📅 19:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21457">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0b5d6c545.mp4?token=XHz7F8_IOix0sAmoCTtjkg2cajcvPJymlriwOsAqub07mKK3WJMGs8S7a8CBmrTTAgxrBYh7xHk3PuVDV5R1EQrIPIy2SxgOofySwjG8b8orIMBm1f5ueV5BTYi40ndetR5kQakCnB8-mO3mFseTuQUNsFuWNx4ZWc6KbJvpNoGEgGzhM48PKquQroblhIwjRdAtPor-DPuW6v46M_htIdF9SMgF9f9VYWx2FM6tvzpYnwMqeqMzyPt1YtkIWK3nn79JThHQqKveIfYd63AF4w6mgZtlrIIkHzoqvDJSDSWQdRftwuDfVvTwXX2Td-Ix4Qnth1J72OYkZsWL4E304w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0b5d6c545.mp4?token=XHz7F8_IOix0sAmoCTtjkg2cajcvPJymlriwOsAqub07mKK3WJMGs8S7a8CBmrTTAgxrBYh7xHk3PuVDV5R1EQrIPIy2SxgOofySwjG8b8orIMBm1f5ueV5BTYi40ndetR5kQakCnB8-mO3mFseTuQUNsFuWNx4ZWc6KbJvpNoGEgGzhM48PKquQroblhIwjRdAtPor-DPuW6v46M_htIdF9SMgF9f9VYWx2FM6tvzpYnwMqeqMzyPt1YtkIWK3nn79JThHQqKveIfYd63AF4w6mgZtlrIIkHzoqvDJSDSWQdRftwuDfVvTwXX2Td-Ix4Qnth1J72OYkZsWL4E304w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکار بالن هواشناسی خودمان توسط نگهبانان غیور!
آقایان صیدی و رضا عصمتی!
احمق‌ها کجای این شبیه پهپاد آمریکایی است؟!
هر چه میزنید ناموسا ۱۰۰ گرمش را برای ما بیاورید</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SBoxxx/21457" target="_blank">📅 17:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21456">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گویا حاج عباس پرینت خیلی مهمی در نیویورک داشته.</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SBoxxx/21456" target="_blank">📅 16:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21455">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مدودف:  هرگز روابط خود را با جمهوری اسلامی ایران فدا نخواهیم کرد، فارغ از اینکه چه کسی از ما بخواهد این کار را انجام دهیم.  ما شرکای راهبردی هستیم و برای همیشه نیز این‌گونه باقی خواهیم ماند.</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SBoxxx/21455" target="_blank">📅 14:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21454">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مدودف:
هرگز روابط خود را با جمهوری اسلامی ایران فدا نخواهیم کرد، فارغ از اینکه چه کسی از ما بخواهد این کار را انجام دهیم.
ما شرکای راهبردی هستیم و برای همیشه نیز این‌گونه باقی خواهیم ماند.</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SBoxxx/21454" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21453">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سخنگوی ارتش ایران
گفت جنگ اخیر باعث شده تهران به این نتیجه برسد که باید
برد موشک‌های خود را افزایش دهد
و کار روی
سرعت و دقت موشک‌ها
نیز از هم‌اکنون آغاز شده است.
او گفت:
«در این جنگ به این نتیجه رسیدیم که
حتماً باید برد موشک‌هایمان را افزایش دهیم
و اکنون در همین مسیر حرکت کرده‌ایم.
نسل‌های آینده موشک‌های ما توانمندی‌های بیشتری خواهند داشت.
»
این مقام نظامی افزود که
دشمن اکنون در فاصله دورتری از سواحل ایران
و تا حدود
هزار کیلومتری
قرار دارد؛ بنابراین ایران به سامانه‌های
دوربردتر، از جمله موشک‌های کروز دوربرد
نیاز خواهد داشت.</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SBoxxx/21453" target="_blank">📅 14:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21452">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ولی حس می کنم باز فریب می خوریم و قیافه اونس میخورد یک بالا داشته باشیم.  دلار هم دارد پارابولیک بالا می رود و این مشکوک است.</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SBoxxx/21452" target="_blank">📅 14:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21451">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtB2_Ty2YeMddwY2HPcz7OatGGTjqBc2nDp0zBOVF0HAkk3hGm1Eo8Cj0jEj5dT_UT0zbFokmlUXn6i7d97caQUb3aT8rvBctf1wHwDD0FXivGULwlCLol4vp7OOvKLaZe2GKnyq-_Yop5yao-vKaVa9oUr9f36apybIhTe7FJuD2aaDHCvp4xZO84tgxaTp_e9h0yuTF7E99ja1Qudkk_VF0Jy9L4HD3xajQy5XHjQ0xx3mFTElZDAlgLM0HoXG1Dmjsu5YvenxByT4iuDThsNJQSNWSeN70GbldfEjUbGYVxe2fw4FBrx5cYibeQFAd8TUvjBRZybRIGmxMqCOSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک بار هم که شده فریب نخورید!</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SBoxxx/21451" target="_blank">📅 11:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21450">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شما ولی قبول نکنید</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21450" target="_blank">📅 11:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21449">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قالیباف:   آمریکایی ها برخلاف حرفایشان در رسانه‌ها، از طریق میانجی ها پیشنهادهایی مطرح کرده اند</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21449" target="_blank">📅 11:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21448">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">قالیباف:
آمریکایی ها برخلاف حرفایشان در رسانه‌ها، از طریق میانجی ها پیشنهادهایی مطرح کرده اند</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/21448" target="_blank">📅 11:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21447">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بفرمایید ؛  پست جدید ترامپ تو تروث:   «صبحِ شکوه: آیا ترامپ تو جنگ با ایران میره سراغ مدل کامل “شرمن”؟»</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SBoxxx/21447" target="_blank">📅 09:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21446">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چون نمی خواهم به وحشت افکنی متهم بشوم، فقط به شما توصیه می کنم این قسمت را درنظر داشته باشید و خود بیاندیشید که در «شرایط کنونی» که کشور تحت محاصره است و چپ و راست اتهامات تروریسم و .... به ما می بندند و همسایگان عرب نیز از حملات موشکی و پهپادی و حوثی ها و…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SBoxxx/21446" target="_blank">📅 09:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21445">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ: با کیم جونگ اون روابط خوبی دارم چون ۱۱۲ موشک هسته‌ای دارد  من ارتباط بسیار خوبی با کیم جونگ اون دارم. وقتی یک کشور ۱۱۲ موشک هسته‌ای در اختیار داشته باشد، خوب است که روابط خوبی با آن داشته باشی.  اما این تفاوت را در نظر بگیرید؛ ایران هرگز موشک هسته‌ای…</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SBoxxx/21445" target="_blank">📅 09:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21444">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M79D9TsUpkkDuCLE4ynej1J58Jzy_L_FbzdyDSTrv7wCq_eI4TmTViSLWumBr4T2kmMefpMDetjmZHgovJzJCtvovYGtZ3M7Wh0ziA0sEr1fODomYqNBw9WCamDrE4GGyRg7fZnHo2MCTGtGoekiOiPGeicwMtLYQmgBBUM-wO0__cKLeyiWeaY0BTa-tvTyIjFqSyyWhrBKTbqGIpfbnoMpA5fn1NcjL1MMi_Ppglf_weITr1cnWHbeEz3x3CZQmLwa1ZZAJFh2lj_Wd4gWdpncJ-JTYMOJMW0dD53jWIQ0LcikgU0vs8ecSmKY8cX_iL4KnOxn9nfkJx4JJxXkTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">report_onthe_nuclear_employment_strategy_of_the_united_states.pdf</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SBoxxx/21444" target="_blank">📅 09:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21443">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">report_onthe_nuclear_employment_strategy_of_the_united_states.pdf</div>
  <div class="tg-doc-extra">172.4 KB</div>
</div>
<a href="https://t.me/SBoxxx/21443" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این فیلم از این ماده چپول مزدور را ببینید تا بعدا بگویم چه توطئه ای در کار است</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21443" target="_blank">📅 09:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21442">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">توطئه در کار است؛
توطئه بزرگ در کار است؛
توطئه ها در کار است!</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21442" target="_blank">📅 08:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21441">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ: با کیم جونگ اون روابط خوبی دارم چون ۱۱۲ موشک هسته‌ای دارد  من ارتباط بسیار خوبی با کیم جونگ اون دارم. وقتی یک کشور ۱۱۲ موشک هسته‌ای در اختیار داشته باشد، خوب است که روابط خوبی با آن داشته باشی.  اما این تفاوت را در نظر بگیرید؛ ایران هرگز موشک هسته‌ای…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SBoxxx/21441" target="_blank">📅 08:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21440">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ: با کیم جونگ اون روابط خوبی دارم چون ۱۱۲ موشک هسته‌ای دارد
من ارتباط بسیار خوبی با کیم جونگ اون دارم. وقتی یک کشور ۱۱۲ موشک هسته‌ای در اختیار داشته باشد، خوب است که روابط خوبی با آن داشته باشی.
اما این تفاوت را در نظر بگیرید؛ ایران هرگز موشک هسته‌ای نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/21440" target="_blank">📅 08:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21439">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">— وزیر دفاع بریتانیا:
«حکومت ایران نیت‌های خصمانه دارد و تهدیدی برای کشور ما و متحدان ما محسوب می‌شود.
تحقیقات در مورد پایگاه هوایی RAF Fairford ادامه دارد و چندین سرنخ در حال پیگیری است و این موضوع بسیار جدی است.
ما پس از رسیدن به نتیجه‌گیری قطعی در مورد RAF Fairford، به یک پاسخ مناسب فکر خواهیم کرد».</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/21439" target="_blank">📅 00:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21438">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👨‍💻
کارشناس صداوسیما:
چین ارسال تصاویر ماهواره‌ای به ایران را متوقف کرده است
چین به ایران گفته ابتدا مشکل خود را با آمریکایی‌ها حل کنید</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SBoxxx/21438" target="_blank">📅 23:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21437">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">1-USA 2-PRC 3-N/A 4-IRI</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SBoxxx/21437" target="_blank">📅 19:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21436">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">1-USA
2-PRC
3-N/A
4-IRI</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SBoxxx/21436" target="_blank">📅 19:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21435">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">الهام علی‌اف، رئیس‌جمهوری آذربایجان  : «آمریکا و چین دو ابرقدرت جهان هستند و هیچ ابرقدرت سومی وجود ندارد.</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SBoxxx/21435" target="_blank">📅 19:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21434">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">الهام علی‌اف، رئیس‌جمهوری آذربایجان
: «آمریکا و چین دو ابرقدرت جهان هستند و هیچ ابرقدرت سومی وجود ندارد.</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SBoxxx/21434" target="_blank">📅 19:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21433">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ادعای بِسنت درباره ایران:
برای اولین بار در تاریخ، از زمانی که شروع به استخراج نفت کردند، این هفته هیچ نفت روی آب نخواهند داشت. آنها هیچ درآمدی نخواهند داشت.</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SBoxxx/21433" target="_blank">📅 18:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21432">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حملات سنگین حوثی ها به تاسیسات نفتی آرامکو در عربستان</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SBoxxx/21432" target="_blank">📅 13:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21431">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">— پلیس بریتانیا دو شهروند ایرانی به نام‌های رحمان صالحی، ۳۵ ساله، و سلام احمدیان، ۳۶ ساله را دستگیر کرده است که متهم به توطئه برای هدف قرار دادن جامعه یهودی در منطقه منچستر پیش از یوم کیپور هستند.
این دو نفر به «آماده‌سازی برای ارتکاب عمل تروریستی یا کمک به دیگری در ارتکاب عمل تروریستی» در منچستر، در تاریخ ۲۰ سپتامبر یا قبل از آن، متهم شده‌اند.</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SBoxxx/21431" target="_blank">📅 08:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21430">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUGePB6gOQGHsW4rtvFhN0MlhP0jgLaU_WpSmUAxGbJeIcrgBoGXVRa5p_j9CKTSa8CAsonFe9H9UDonfYiZ23E-HCuZZCy5loxB6xoeTKqyQezIJrfNnyeRJNa-5BR4uAD34phZoE3Y_FsNwBS0WN4hJXQlgU0KqETzY4LFWpn6emPPygzywZHcLhDCXDaeoBgMRRTFGvl6gAe-Koo-yZ-cRvjP8iHMWuyW4Ee_agSLZFuX-j5AoaE2TSLXYGQaNiAdatZjHrNfbQXP2NKCUG4z5n3_V5iv42iFz58g-7jxCjJfAS1FkQRccs4yOI8yYCVusiHp4XIX2vEsEXevnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی عجیب است.   خود ترامپ در مارس ۲۰۱۹ منطقه جولان را به عنوان بخشی از خاک اسراییل به رسمیت شناخته آن وقت سفیرش در ترکیه صحبت از «اشغال» جولان می‌کند!  حدس میزنم عمر سیاسی  — و شاید زیستی — تام باراک (که عرب تبار است) بزودی به پایان برسد.</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SBoxxx/21430" target="_blank">📅 02:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21429">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ادعای جدید ترامپ:  یکی از دلایل بمباران ایران، مقابله با مواد مخدر بود  به گفته رئیس جمهور ایالات متحده بمب‌ها مستقیما از مجراهای هوایی وارد "کارخانه‌های مواد مخدر" شدند.  ترامپ مدعی شد که در این تاسیسات فعالیت هسته‌ای و فعالیت مرتبط با مواد مخدر انجام می‌شد…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SBoxxx/21429" target="_blank">📅 22:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21428">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ادعای جدید ترامپ:
یکی از دلایل بمباران ایران، مقابله با مواد مخدر بود
به گفته رئیس جمهور ایالات متحده بمب‌ها مستقیما از مجراهای هوایی وارد "کارخانه‌های مواد مخدر" شدند.
ترامپ مدعی شد که در این تاسیسات فعالیت هسته‌ای و فعالیت مرتبط با مواد مخدر انجام می‌شد و این "کارخانه‌های مواد مخدر و هسته‌ای" به‌شدت هدف قرار گرفتند.
بر اساس گزارش رسانه‌های آمریکا این نخستین بار است که ترامپ به طور مستقیم از "کارخانه‌های مواد مخدر" در ایران به‌عنوان یکی از اهداف حملات هوایی آمریکا نام می‌برد.</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SBoxxx/21428" target="_blank">📅 22:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21427">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">«چرا جنگ می شود و چگونه؟!»</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/21427" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نشست لایو لغو شد.  در یک پادکست مفصل، خواهم کوشید اوضاع را از دید خودم بررسی کنم.</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/SBoxxx/21427" target="_blank">📅 17:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21424">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حمله با سلاح سرد به یک روحانی در رشت؛ ضارب متواری است</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SBoxxx/21424" target="_blank">📅 16:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21423">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تا پیش از NFP به نظرم در همین باکسی که از پریروز تشکیل شده بازی کند. پس اکنون که در سقف باکس هستیم می توانیم با تارگت های 4155 و 4141 بفروشیم و استاپ را پشت همین باکس قرار بدهیم (حدود 4220)</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SBoxxx/21423" target="_blank">📅 15:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21422">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">به نظر می رسد برای موج 5، مدل سوریه و ایجاد جزیره های گریز از مرکز درون کشور برنامه ریزی شده ا ست.</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SBoxxx/21422" target="_blank">📅 15:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21421">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fb5b5a1b.mp4?token=gUibPpBHFmzSDuLoWhsUNNh7uiTzRuDewJxbxsOYrxdoO8UdvK9aSzVdBICIyJQWTcqThkRHDpWF0lu5DrHJSDFhSmY1jplSf28v5sduXnsa1Fq-y8HF7UQhEJXdy8Vvm9RQkMvHeG4pvyhAKf_Xs4yEyYRCMS2gxZCu9gC4tACLpxiwWq7KPBAW-AmFTaUWGpVz4B1wVvLJUNZr0tl9ucgc5fT8-1OmBvTYmF3FO892uzUMlzkAJ7VurvHCz7q-fApF8eSguu5uHOQGAKXT-nXn5Agkaq2LzOhZkMSjXCKSKFXHUxhRWSy16JCEblOuIfNKtZM85SbpsWUFYE3KCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fb5b5a1b.mp4?token=gUibPpBHFmzSDuLoWhsUNNh7uiTzRuDewJxbxsOYrxdoO8UdvK9aSzVdBICIyJQWTcqThkRHDpWF0lu5DrHJSDFhSmY1jplSf28v5sduXnsa1Fq-y8HF7UQhEJXdy8Vvm9RQkMvHeG4pvyhAKf_Xs4yEyYRCMS2gxZCu9gC4tACLpxiwWq7KPBAW-AmFTaUWGpVz4B1wVvLJUNZr0tl9ucgc5fT8-1OmBvTYmF3FO892uzUMlzkAJ7VurvHCz7q-fApF8eSguu5uHOQGAKXT-nXn5Agkaq2LzOhZkMSjXCKSKFXHUxhRWSy16JCEblOuIfNKtZM85SbpsWUFYE3KCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جانوران تبهکار Afro-Arab در فرانسه دوباره شورش کرده و در حال کشتار و آتش سوزی و ویرانگری هستند!</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SBoxxx/21421" target="_blank">📅 15:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21420">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">جانوران تبهکار Afro-Arab در فرانسه دوباره شورش کرده و در حال کشتار و آتش سوزی و ویرانگری هستند!</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/21420" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21419">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">واشنگتن پست:
وزارت جنگ آمریکا برای اعزام 20 هزار نیروی نظامی دیگر ارتش آمریکا به خاورمیانه آماده می‌شود.</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SBoxxx/21419" target="_blank">📅 13:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21418">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">صداوسیما:
درگیری مسلحانه سپاه با تروریست‌ها در راسک
برخی منابع از درگیری مسلحانه میان نیروهای امنیتی و عناصر گروهک تروریستی در یکی از روستاهای شهرستان راسک در جنوب سیستان‌ و بلوچستان خبر دادند.
نیروهای امنیتی در حال پاکسازی منطقه و بررسی اوضاع هستند.
تاکنون جزئیات بیشتری درباره وضعیت عناصر تروریستی منتشر نشده است.</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SBoxxx/21418" target="_blank">📅 12:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21417">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddEO0H91UbMV1Zw6ubx9c5s9h7_A0FDQ4RM09auJKFmHHCY5keJI2vsLhMnpCQUVd2QwBux24ZOtPdjTFa1s39P9gFA-jpGlEymK_UntnX1K70FPxZ-mJ2IRQHT1HnbOIAeCz0bhOsrxg5fRRGp-taRAHESUJ8SGuhC4GiEu2kruSND1_iLhR8_PnHJQtS0rtQ-KddwmzZDYgAfcyD5OjdITZXcLDwaSL8Sk69YZ0yzHT5cqoL1W_GW3k0rFbmICsXfaEZfcDYz14RB1ujNkmScWPdqBkeO3rjHGuCM1EZ3KevR4w5YshFvw9_6CvgDLpFKvt9qDBfxQhnEUXEeIRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از NFP به نظرم در همین باکسی که از پریروز تشکیل شده بازی کند. پس اکنون که در سقف باکس هستیم می توانیم با تارگت های 4155 و 4141 بفروشیم و استاپ را پشت همین باکس قرار بدهیم (حدود 4220)</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SBoxxx/21417" target="_blank">📅 11:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21416">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agPALqsFhXNoK9dH25zqzKFmwD_4yQ7kgHLBlwEYk8zfigsCUYPUIZlIwzoPXsFxuRBdxnMpGBuLmM-AQdJEUueNgoRdjCBxyO1ky4ipN4uzom2TBuSjZfsfPlDnmIqaXiN7Y3abNrgfbejUxNEjGkGSQVkVAZB5joBTVH6jJnOCfkvzxoOA47ClKWjng-mN5tWUhWqLVH8-uGFWEsQB5Uj2aO4h237ps4C9xsFTNZHtzYoSXjpLzdQpeAFbdNNJ7EaGueggyqBya1_ADLzJm7uQP64kUhrWfVxMIbYipBRCjysBZ2xAfF8zgiNBjd7BkJQeRVXOH2XWTka2zBBU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueGap
نمایه FVC هم تغییر خاصی نسبت به پریروز و دیروز نداشته است چون عملاً قیمت همانجایی است که دیروز بوده</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SBoxxx/21416" target="_blank">📅 11:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21415">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uciAWbpZwiu6Y4Fsie4JelPDVXshjlVqJ-LYi_bR8rSn1Q3BWOTy365ndWte3NzgOtygs9OxxY7dd_w9a4gAOFjHEjICZVVacubM42Wfy4rQj2XDSctunoY9mkpC-cNyfOd0oPvdYi_LeajuiAsHZLN-tXQLL7y1MQpofE-Ka4V6uDvLKH-qd5eNUMUrPPaZqH_Byg-boQ43cjsbTO4mkFYonFjzFmKEQvMtfftTbv6Ha1R7Enslqdp2Spe3Y92JuMCJ6wict-iOP4H6X3LFMI8m2vJT2g5mPB91J4XVVbz-6ntCBN59Qu7dhsypR83-JIZLgATql_0O62SRxVrnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح متوسط به بالا قرار دارد.</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SBoxxx/21415" target="_blank">📅 11:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21414">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اگر دوباره به پایین برگشت، تنها روی محدوده دوم ۴۱۴۸ ورود مجاز است.</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SBoxxx/21414" target="_blank">📅 09:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21413">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شخصی قصد انجام عملیات انتحاری در مسجدالحرام داشته که کمربند انفجاری وی فعال نمی شود و توسط نیروهای امنیتی سعودی دستگیر شد</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SBoxxx/21413" target="_blank">📅 00:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21412">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شخصی قصد انجام عملیات انتحاری در مسجدالحرام داشته که کمربند انفجاری وی فعال نمی شود و توسط نیروهای امنیتی سعودی دستگیر شد</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SBoxxx/21412" target="_blank">📅 00:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21411">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51530cf576.mp4?token=aXl6lKSUAq_L9nJwel7WfEbvt-Yp5o5wuYcMvVVCa27HF8aiD3pLy87rE_UqbsMCr3JUBTh-XcrWlpVLNH366GYyfapfpB_FhgXCGQih02jIIx1jcjCwgpMZd5T_CP8dlaF3j966qwzjEGF6t_riIyMnoEbOUnAx56Yqv3CX5aP9HvXZ_5cJRvGT2AO_ZkM0jV2P-W9Pu98Ywb9Wcd6a9ak_gKxYK7frWNEv5heGS7v9tWNXhz6H5CgsPvc4C8yiMk0UjHgDIFp96XcJMezbyBJq6VEtQ5g1z6fh9m5WFz-cN4Tlelr2NTi66ffWNaaJHtoXAj5vHGitccrIgYqe4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51530cf576.mp4?token=aXl6lKSUAq_L9nJwel7WfEbvt-Yp5o5wuYcMvVVCa27HF8aiD3pLy87rE_UqbsMCr3JUBTh-XcrWlpVLNH366GYyfapfpB_FhgXCGQih02jIIx1jcjCwgpMZd5T_CP8dlaF3j966qwzjEGF6t_riIyMnoEbOUnAx56Yqv3CX5aP9HvXZ_5cJRvGT2AO_ZkM0jV2P-W9Pu98Ywb9Wcd6a9ak_gKxYK7frWNEv5heGS7v9tWNXhz6H5CgsPvc4C8yiMk0UjHgDIFp96XcJMezbyBJq6VEtQ5g1z6fh9m5WFz-cN4Tlelr2NTi66ffWNaaJHtoXAj5vHGitccrIgYqe4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شخصی قصد انجام عملیات انتحاری در مسجدالحرام داشته که کمربند انفجاری وی فعال نمی شود و توسط نیروهای امنیتی سعودی دستگیر شد</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SBoxxx/21411" target="_blank">📅 00:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21410">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارشگر:
«آیا ایران در حادثه پایگاه هوایی فرفورد دخالت داشت؟»
ترامپ:
«به نظر می‌رسد که بله.»</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SBoxxx/21410" target="_blank">📅 00:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21409">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ادعای وزیر خزانه‌داری آمریکا:
جمهوری اسلامی در یکماه گذشته حتی یک قطره نفت هم نفروخته است!</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SBoxxx/21409" target="_blank">📅 23:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21408">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هدف قرار گرفتن شرکت آرامکو در شهر ینبع عربستان</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SBoxxx/21408" target="_blank">📅 23:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21407">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مقام ایرانی:
ادعاهای بلومبرگ در مورد پیشنهاد هسته‌ای ارائه شده توسط ایران به طرف آمریکایی در جریان گفتگوها با میانجی‌گران نادرست است</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SBoxxx/21407" target="_blank">📅 23:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21406">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سوپرنفتکش ۲.۵ میلیون بشکه‌ای در تنگه هرمز هدف قرار گرفت</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SBoxxx/21406" target="_blank">📅 23:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21405">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔹
معاون وزیر ارتباطات
:
اگر استفاده از استارلینک گسترده شود ، در مواقع بحران مجبوریم تمام برق را قطع کنیم تا مودم های استارلینک هم از کار بیفتد؛ چراکه حکمرانی اینترنت را نخواهیم داشت</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SBoxxx/21405" target="_blank">📅 23:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21404">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مقامات ایالات متحده به الجزیره:  ناو هواپیمابر یو‌اس‌اس تئودور روزولت به همراه گروه ضربتی خود، پایگاه سن دیگو را ترک کرده و به سمت خاورمیانه در حرکت است.  تا پایان نوامبر، ۳ ناو هواپیمابر و ۲ گروه ویژه حملات آبی-خاکی در اطراف ایران مستقر خواهند شد.</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SBoxxx/21404" target="_blank">📅 20:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21403">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ:  به زودی با حمله به ایران، ما صلح را در جهان ایجاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SBoxxx/21403" target="_blank">📅 18:27 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
