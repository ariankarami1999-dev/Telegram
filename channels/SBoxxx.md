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
<img src="https://cdn4.telesco.pe/file/laffSY4yuB4hVz9J6dYcC2n365dmzAYqNKWIc3h2D1JSs-pWvsudktTYEZ_te1fdZOJfPBTIh3c2aek583FBi960ZI4Al61SqmZQJToiZhNXgZucqtkk3tkbf3Q-ZmP6iHcP4VhPB851UL_Qhjmu6jvNbL6__CD3Ev7IEyXq6krkdRGr8G76OMoCr_-9oni1LEu_7LEMPEpgxkulVajJ_cJ_SeL0mLhnn3V_acSLZxs_Al1D4pis5hQp7sa61O--xpwyKNNTgfw7BcsN5aSDerEvLxUyUtkXMA5r-aQy9Genbi860VH27LqCXrGpR7bthJvwIh8Fz54CLTiCI_BAXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 22:38:20</div>
<hr>

<div class="tg-post" id="msg-17051">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به رادیو ارتش گفت:  «شلیک‌ها از سوی ایران به سمت اسرائیل به معنای اعلام تجدید جنگ است».</div>
<div class="tg-footer">👁️ 522 · <a href="https://t.me/SBoxxx/17051" target="_blank">📅 22:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17050">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به رادیو ارتش گفت:  «شلیک‌ها از سوی ایران به سمت اسرائیل به معنای اعلام تجدید جنگ است».</div>
<div class="tg-footer">👁️ 648 · <a href="https://t.me/SBoxxx/17050" target="_blank">📅 22:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17049">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پرتاب موشک بالستیک به سمت شمال اسرائیل، حیفا.</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/SBoxxx/17049" target="_blank">📅 22:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17048">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پرتاب موشک بالستیک به سمت شمال اسرائیل، حیفا.</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SBoxxx/17048" target="_blank">📅 22:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17047">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">غریب‌آبادی، معاون وزیر خارجه ایران، در واکنش به گزارش‌هایی مبنی بر استفاده آمریکا از دارایی‌های ایران برای جبران خسارات جنگی به متحدان منطقه‌ای:   دولت‌های منطقه در موقعیتی نیستند که غرامت مطالبه کنند</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/17047" target="_blank">📅 21:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17046">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بازسازی کشورهای عربی با پول بلوکه شده ایران!  رویترز: واشنگتن دارایی‌های مسدود شده ایران را برای حمایت از بازسازی و تعمیر خسارات در اختیار متحدان خود قرار خواهد داد.</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/17046" target="_blank">📅 21:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17045">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ایران با صدور هشدار نوتام آسمان خود را  بست</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/17045" target="_blank">📅 21:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17044">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/17044" target="_blank">📅 19:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17043">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قطر یک اطلاعیه صادر کرده است که پروازها را از طریق فضای هوایی خود بازگردانی می‌کند و مسیرهای جایگزین برای هواپیماهای در حال حرکت از دوحه و فرودگاه‌های عربستان سعودی ارائه می‌دهد.
این دستور که از ۷ تا ۱۴ ژوئن اجرایی می‌شود.</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SBoxxx/17043" target="_blank">📅 19:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17042">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این رسانه گفته می شد تحت مدیریت شمخانی است.</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/17042" target="_blank">📅 19:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17041">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIfYSpFQSSCbZN4OmHR3r9MzbFQoGtM3WtlAyR5hWyqtIbrGKjqW2kAN2pPfAUEYdPhvbqkSzr0e8sRCzGvfIoqsAqjAzCtSjO-IEfJzXxNep2M8OQw8D1POVpyw8A4klShl67bVayXlXCEeD0XxYgIDKfIX9xiz7MTRnzekUAsM9BjeueEtWY_eBo3h1zYrs_WLltOEG5z5XPOA3mjeGkkvmSPSuahVaafcL1g2_TzYCnhKWc03_l-4nNp85G3_bRLT_u90phAT7DkJVIp2_rbgUUs5QQ_QAnLhBeJ9I5GGsTs_yN8ECijCyhdnRERU1LbOLMXKnG90rfzGDcqY4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/17041" target="_blank">📅 19:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17040">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجنگاوران</strong></div>
<div class="tg-text">🔸
آمریکا، قدرت اول نظامی جهان نتوانست...
امروز تحلیل‌گر های زیادی هستند که حرف هایشان را با این جمله که آمریکا با این همه ادعا و قدرت نظامی نتوانست اینکار و آنکار را بکند شروع می‌کنند و بر مبنای این گزاره شروع به توهم زنی می‌کنند.
مثل همیشه، شیطان در جزئیات است و مشکل آدم های ساده لوح و متوهم بی توجهی به جزئیات.
خیلی کار ها هست که آمریکا می‌تواند انجام بدهد اما انجام آن ها هزینه هایی دارد که صرفا در محاسبه هزینه و فایده، برای آن ها نمیصرفد.
باز کردن تنگه هرمز یکی از این کار ها است، فایده ی باز شدن تنگه فعلا برای آمریکایی ها به هزینه اقدام نظامی نمی‌صرفد. اینکه برخی، بسته شدن تنگه را نشانه ظهور قدرت دریایی ایران و تغییر معادلات جهانی عنوان می‌کنند، توهمی است که به راحتی می‌تواند باعث هزینه بیشتر برای کشور بشود، چرا که اگر باعث اقدام های جسورانه و افزایش هزینه برای انفعال آمریکا بشود، باعث تغییر در محاسبه ضرر/فایده و حمله مجدد به ایران می‌شود (البته که در قضیه تنگه هرمز آمریکا منفعل نشده و رویکرد هوشمندانه و بدون هزینه ای را پیش گرفته است).
این مسئله درخصوص تغییر رژیم نیز صادق است. خیلی ها دوست داشتند هزینه ای پرداخت نکنند و «عمو ترامپ» و آمریکا همه هزینه های تغییر رژیم در ایران را پرداخت کنند. حالا هرچقدر هم که برایشان توضیح بدهی که در تاریخ سابقه نداشته است که با حمله هوایی رژیمی تغییر کند و  حمله زمینی به ایران هم جزو گزینه ها نیست، بازهم آنچه دوست داشتند را باور می‌کردند و امروز که نتیجه را دیدیم، برخیشان می‌گویند آمریکا قدرت کافی نداشته است!</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/17040" target="_blank">📅 18:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17039">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">به حمله رژیم صهیونیستی به ضاحیه پاسخ دردآور خواهیم داد  سخنگوی کمیسیون امنیت ملی مجلس: امشب به آسمان سرزمین‌های اشغالی نگاه کنید.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/17039" target="_blank">📅 18:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17038">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تشکیل جلسه فوری شورای عالی امنیت ملی ایران</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/17038" target="_blank">📅 18:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17037">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تشکیل جلسه فوری شورای عالی امنیت ملی ایران</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/17037" target="_blank">📅 17:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17036">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ:   رهبری جدید ایران منطقی‌تر و باهوش‌تر است و (آیت‌الله) مجتبی خامنه‌ای بخشی از روند تصویب توافق شده است  اگر رهبر ایران بخواهد، من آماده‌ام که مستقیماً با او صحبت کنم، اما هنوز مستقیماً با او صحبت نکرده‌ام.  من این جنگ‌های بی‌پایان را دوست ندارم، و…</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/17036" target="_blank">📅 17:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17035">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">امروز اسراییل به ساختمانی در ضاحیه بیروت حمله هوایی انجام داد که گفته می شود تا ۵ کشته در پی داشته است.</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/17035" target="_blank">📅 17:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17034">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فوری | ترامپ به ان‌بی‌سی:   من محاصره دریایی ایران را جنگ نمی‌دانم، اما هر کسی که می‌خواهد آن را جنگ توصیف کند، انتظار دارم بتواند این کار را انجام دهد.  ایران روزی ۴۰۰ تا ۵۰۰ میلیون دلار بخاطر محاصره دریایی ما از دست می‌دهد .</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/17034" target="_blank">📅 17:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17033">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فوری | ترامپ به ان‌بی‌سی:   دلیل اعمال محاصره دریایی بر ایران این است که آن‌ها سعی کردند محاصره‌ای اعمال کنند و اکنون ما محاصره‌ای بر آن‌ها اعمال کرده‌ایم.</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/17033" target="_blank">📅 17:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17032">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ:   اگر به توافقی دست نیابیم، ارتش ایران را بیش از پیش تضعیف خواهیم کرد تا نیروهای ما بتوانند با اطمینان و امنیت کامل، اورانیوم را در اختیار بگیرند!  هیچ پولی را آزاد نکرده و هیچ تحریمی را کاهش نمی دهیم!  لبنان بخشی از توافق نیست!</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/17032" target="_blank">📅 17:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17031">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ:
اگر به توافقی دست نیابیم، ارتش ایران را بیش از پیش تضعیف خواهیم کرد تا نیروهای ما بتوانند با اطمینان و امنیت کامل، اورانیوم را در اختیار بگیرند!
هیچ پولی را آزاد نکرده و هیچ تحریمی را کاهش نمی دهیم!
لبنان بخشی از توافق نیست!</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/17031" target="_blank">📅 17:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17030">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ادعای رسانه اسراییلی: تعویق حمله به ضاحیه بیروت در پی مداخله آمریکا  سازمان رادیو و تلویزیون اسراییل  گزارش داد که طرح حمله نظامی به ضاحیه جنوبی بیروت به دلیل دخالت‌های طرف آمریکایی به تعویق افتاده است.</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/17030" target="_blank">📅 17:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17029">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سخنگوی وزارت خارجه و سخنگوی تیم مذاکره‌کننده اسماعیل بقایی در مصاحبه با سی‌ان‌ان:
ما چندین اختلاف نظر در مذاکرات داریم، که مسئله اصلی پذیرش حقوق ایران، از جمله حق غنی‌سازی، توسط ایالات متحده است.
از زمان اجرای آتش‌بس، آمریکایی‌ها چندین بار کشتی‌های تجاری ایرانی را در تنگه هرمز و آب‌های بین‌المللی هدف قرار داده‌اند.
وضعیت منطقه‌ای و آتش‌بس بسیار شکننده و خطرناک است و این وضعیت نتیجه رویکرد بی‌محابای ایالات متحده نسبت به منطقه و آتش‌بس است. نیروهای مسلح ایران با تمام قدرت به هر حمله‌ای پاسخ خواهند داد.</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/17029" target="_blank">📅 15:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17028">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">Secret Box
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/17028" target="_blank">📅 14:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17027">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnimTUsFRJn7I2IRk8e11wMsQIUcgrEuLvneD67HHmaFpGtcDD70GOUinzJoGN6F5MjZYlxRyzOUyFf8_sTDkQtEExyWnUr1bKmIRXTW-B3UJG7_v0kup4deBycB56aRtp9ZXbT2Rh99zPdRbymsEFM43zkqouhM9dzxjOhIUrlJGH6JkJUdCuR3KsxUhSU2KM1c3pH8-mkFVYPadz-3X2okoTIeQ1r-tWydG2T-6XV9CMohNEOquzTb2NyrN_cNYpV8nEl8FmFYnz3-PPjGElysoXHnLLVkymuZCW9Z3drYUb3lWfoSp2cfOMsdV4B8oC608_scyuAduoHr1is7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرانجام کتابی که وعده دادم درباره پیوند ژئوپولیتیک و بازارهای مالی ترجمه کنم، به چاپ رسید.
به نظرم در این شرایط که چندین جنگ همزمان در منطقه و جهان در جریان است و تنشهایی که میتواند بزودی تبدیل به جنگ های دیگری بشود، فقدان وجود یک دیدگاه تحلیلی چهارچوب بندی شده و متدیک به پویه های ژئوپولیتیکی منجر به ادراک نادرستی از بسیاری نوسانات بازاری شده و فرجامش افزایش میزان خطای تحلیلگران و معامله گران خواهدبود.
این کتاب را که پاسخی به این چالش است میتوانید
از اینجا سفارش داده و تهیه کنید.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/17027" target="_blank">📅 14:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17026">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ3nSxOR7z17GgFjZKvhEbVW4fz16NycRUI2rkX8U_GJgtl0aYRAWoUnFwsA2Ln3mZ42gh0TmQwris12kyWf6HouIG2l5SpwzjqnA_LaM-zOBiKkh0O6svpjExJiUGbTq2w22AkySx3yDt13hATRX3KY-yFOGpcf7enKurHrio6A-6N5VBC_lrPanPlQ7gxo6yBn4rl_HF5lVkSnX3JhdA4NAgob2E7B2VB8kMKUxANq6j68Q80vI2xZDwlTNhTiGxtFUCSiwQ9xeAUaRuVnhKzRAp9NYP_V-nxwQhcoTpS4tKtdPvPMp3YH-dR3JTqTjZCqXrtVEs_3V31aU77A3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▪️
خبر این است: وزیر کشور پاکستان پیش وارد تهران شد  مایلم یکبار دیگر صراحتا هشدار بدهم که ابداً نباید حسن نیت داشتن پاکستان را پذیرفت؛ پاکستان یکی از فاسدترین کشورهای دنیاست که توسط یکی از فاسدترین نظامیان دنیا اداره میشود. نظامیانی که وابسته سعودی، آمریکا،…</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/17026" target="_blank">📅 13:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17025">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دقت کنید که سنتکام می‌گوید که دوباره «سایتهای راداری نظارتی ساحلی ایرانی» را در گروک و قشم زده اند!  پیشتر اشاره شد چرا مهم است.</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/17025" target="_blank">📅 13:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17024">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بیانیه حماس در پی تیراندازی امروز ۲ تن از اعضایش در یک شهرک اسراییلی
«جنبش مقاومت اسلامی (حماس) عملیات تیراندازی قهرمانانه در مستعمره کوخاو یائیر، شمال قلقیلیه، و همچنین عملیات قبلی در تقاطع مستعمره افرات، جنوب بیت‌المقدس را تحسین می‌کند.
این دو عملیات در پاسخ به تهاجم مداوم اشغالگر به نوار غزه و سیاست‌های ادامه‌دار یهودی‌سازی، کشتارهای خارج از چارچوب قضایی، گسترش مستعمرات، بازرسی های بدنی و حملات علیه مردم فلسطینی در کرانه باختری و اورشلیم صورت گرفته است.
اشغالگر، هرچقدر هم در سرکوب و جنایات خود پیش برود، موفق به توقف موج مقاومت در کرانه باختری نخواهد شد. مردم ما مسیر پایداری و سرسختی را تا رسیدن به آزادی و بازیابی حقوق کامل خود ادامه خواهند داد.
ما در برابر تشدید سیاست‌های گسترش مستعمرات، مصادره زمین، کشتار، بازداشت، آوارگی و تروریسم مستعمره‌نشینان هشدار می‌دهیم. تأکید می‌کنیم که این جنایات امنیت یا ثباتی برای آن به ارمغان نخواهند آورد، بلکه منجر به تشدید بیشتر درگیری و مقاومت خواهند شد.
ما از جامعه بین‌المللی می‌خواهیم مسئولیت‌های خود را به عهده بگیرد، با جدیت برای توقف تروریسم اشغالگر علیه مردم و سرزمین ما تلاش کند، تهاجم آن را پایان دهد و رهبران جنایتکار آن را پاسخگو سازد.»</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/17024" target="_blank">📅 13:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17023">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">زلنسکی: روسیه عمداً سایت ذخیره سوخت هسته‌ای را در حمله‌ای «بسیار شنیع» هدف قرار داد</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/17023" target="_blank">📅 12:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17022">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">قطعی برق خانه‌ها از اواخر حرداد شروع خواهد شد  آرش نجفی، رئیس کمیسیون انرژی اتاق بازرگانی، صنایع، معادن و کشاورزی ایران: پیش‌بینی می‌شود که این روند از اواخر خرداد یا اوایل تیرماه آغاز شود و مردم ایران احتمالاً به مدت سه ماه با این شرایط درگیر خواهند بود که…</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/17022" target="_blank">📅 11:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17021">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXpDsrvQjPfoaNJV6al7QYwuQzQwIJNWLpT6yPLLM2E-Cq5onFPt109jXfW6bUwS_C-dpiKFY0-1fbPkLztA-Oi-LFodcWjfQke3sI5GPxJ3U85Kg24yU2iw54Lycu7Q5Q3gTZVypDeN78YkT8AKHIjX8eFcuOWz2JQFT3KCcj72tL5uwRLtqK4H5xOOMn7KP72u4fUh75rbp5LpwAwPDn6fuhLBzHDWAhOk_kEBl5XWRU6d5_aAUDuaHD_SMQsjjQSgwps5BdbXO05DXTAsJEE2P25mFmfMOyR1JDKklmgGJyG0MgMli4q-TQyZPGqpEGfiZf-_uKLU71sbOC8IKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فناوری_هوشمند،_جنگ_را_به_انتخابی_احمقانه‌تر_تبدیل_می‌کند.pdf</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17021" target="_blank">📅 10:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17020">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بازسازی کشورهای عربی با پول بلوکه شده ایران!  رویترز: واشنگتن دارایی‌های مسدود شده ایران را برای حمایت از بازسازی و تعمیر خسارات در اختیار متحدان خود قرار خواهد داد.</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17020" target="_blank">📅 10:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17019">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOj8yxihRYWEDRFNIEVfbzIaoLAWDVGnW3e2UEwV20IT23Ded-3n5_L9XLeExb2a082VLJqTJxYzZ1LnGPPikmxZQ7VkD0EsZlYf7EODEswAfLAwI9k9K2fbUTyLP_UY-hp2ytymFUF2edZrWVwVJ8AZxKyVli_eWUKhx8XbFGx0AVn6Gh6nGGQVka9bCok4PYqdYW9TxsF73AdNd-F5tNwGJHKozkdzhC_FslxEIIvBZjBvIN2ct_CcgxonuCWF7aSBi1emMXuDPqw-73sFZNmUWhvrWPRdLAOE4wl3IsvbOh0BVOHWA2AXFyA9fVo-1sHMH8VLPHxKUzWVgxbxvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازسازی کشورهای عربی با پول بلوکه شده ایران!
رویترز: واشنگتن دارایی‌های مسدود شده ایران را برای حمایت از بازسازی و تعمیر خسارات در اختیار متحدان خود قرار خواهد داد.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/17019" target="_blank">📅 08:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17018">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گزارش های اولیه از حمله آمریکا به مناطقی در جنوب کشور</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17018" target="_blank">📅 07:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17017">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گزارش های اولیه از حمله آمریکا به مناطقی در جنوب کشور</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/17017" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17016">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">باراک راوید خبرنگار اکسیوس:   دو منبع آگاه به جزئیات به من گفتند که معاون برکنار شده‌ی رئیس موساد، یک سال پیش بودجه‌ای به مبلغ یک میلیارد شِکل (حدود ۳۵۰ میلیون دلار) و تیمی متشکل از صدها نفر برای پروژه‌ی سرنگونی حکومت ایران دریافت کرد!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/17016" target="_blank">📅 01:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17015">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تبدیل ایران به یک دولت شکست خورده (Failed State) پلن B اسراییلی ها بود که ثابتی نیز به همین اشاره می‌کند   پلن A اسراییل، تغییر رژیم و کمک به روی کار  آمدن یک دولت غربگرای حامی اسراییل بود که فعلا شکست خورده است.  در این صوتی طولانی که ۸ ساعت پیش از آغاز جنگ…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/17015" target="_blank">📅 01:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17014">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uU3SLTX0V2gxrvZ2VgWonQCiVU1otCzLAQOYS-sQMkPsyvkWityYcF4z1OqOd7RshGcVTt4pPgsOq9mVVNZCEg1Y8HsU2YPlqS8Q_T1gx4PAo6tNbqsuBio3A9nizsfnHl-AYbKknEOvn_OBY0sXlD83iSksn2p_Mbn7aJbuC1on-siCoJXdTsgCP2Y60omNcP42z2UFrmB2XH7pBrNhARQ-fUb0c0SIOkW-99qmp2O_CuHZV871_QPxVE_HmwF920dE4aiAl1Q0Oh_klN8O5SfL4CJYBC86OtFP06jhRidNH01_ijysESF2Oe7HFh14Bay7rPADBYvUPr4Pb3FJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهش ثروت شخصی ترامپ به سطح 6.5 میلیارد دلار!</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/17014" target="_blank">📅 23:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17013">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">محمدجواد لاریجانی: رفتن آقای قالیباف به اسلام‌آباد غلط بود و هزینه‌ای بزرگ بود
▫️
ترامپ معتقد بود برجام کافی نیست برای همین آن‌را پاره کرد تا امتیازات بیشتری بگیرد.
▫️
دلیل آنکه آن‌ها در میانه مذاکرات حمله می‌کنند آن‌ است که ما وقتی مذاکره می‌کنیم به آن‌ها سیگنال می‌فرستیم که می‌توانیم با آن‌ها کنار بیاییم و برد-برد کار می‌کنیم که آن‌ها فکر می‌کنند اگر بیشتر فشار بیاورند، امتیازات بیشتری می‌گیرند.
▫️
نخست‌وزیر پاکستان، آدم خوبی است، اما لازم نیست ما و آمریکایی‌ها را مقابل هم قرار دهد تا مذاکره کنیم، باید میانجیگری بلد باشد.
▫️
اگر ما بخواهیم خودمان با آمریکا صحبت می‌کنیم نیازی به میانجی‌ نداریم. /صداوسیما</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/17013" target="_blank">📅 23:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17012">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نخستین سند قطعی دال بر خودکفایی کامل کشور در تولید تریاک</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/17012" target="_blank">📅 22:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17011">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">▪️
خبر این است: وزیر کشور پاکستان پیش وارد تهران شد  مایلم یکبار دیگر صراحتا هشدار بدهم که ابداً نباید حسن نیت داشتن پاکستان را پذیرفت؛ پاکستان یکی از فاسدترین کشورهای دنیاست که توسط یکی از فاسدترین نظامیان دنیا اداره میشود. نظامیانی که وابسته سعودی، آمریکا،…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17011" target="_blank">📅 21:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17010">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دقت کرده اید هر کسی میانجی این جنگ بی پایان ما با آمریکا و اسرائیل شد به خاک رفت؟!  راند اول قطر میانجی شد و همان روز ایران به قطر حمله کرد و چند ماه بعدش اسرائیل هم به قطر حمله کرد و در جنگ اخیر هم با حمله موشکی وحشتناک ایران به تاسیسات گازی راس الفان، بیشترین…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/17010" target="_blank">📅 21:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17009">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEp4w_7bcTqLPIugUPKY35FMHgjCueEydEqXId5kTggI5VH-Mwthv0xHkX6abrWTHLDBAW5rkrDoN04ukUXcJOArAIasPvPY-UpXeUWROy3AymDp-jIC_Fs5dpG_SZwQKaQB0iG7Dcab9OmijWwKztCcV1_K24Yrsw25pjDZ5YPC7LgL7KRqdMTLXOWkmCpbrp_GXS_3nFbCd50apLReHfNe0J5oSJVU80UzhELhD6VOZm3Yk8dlco9GrbGKwKQtJzZgJeQN8g2BRzxJq2DB10ucBOgNglUSvZdR3_-hWrq3zWUJT9gubZOwaTdbQXex6twfvvh_SCECGMZetq4jiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ایران در سال ۲۰۲۶ با یکی از شدیدترین فشارهای صادراتی خود در سال‌های اخیر روبه‌رو شده است. داده‌های منتشرشده توسط شرکت ردیابی نفتکش Kpler و منابع تخصصی بازار انرژی نشان می‌دهد که از زمان آغاز درگیری‌ها و تشدید محدودیت‌های دریایی در اواخر فوریه، توانایی…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17009" target="_blank">📅 20:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17008">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزیر کشور پاکستان، محسن نقوی، برای دیدار با مقامات ایرانی از جمله وزیر امور خارجه عباس عراقچی، وارد تهران شده است.
— خبرگزاری تسنیم</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17008" target="_blank">📅 20:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17007">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تروریستهای ازبک دولت الجولانی را تهدید کردند   گروهی از تروریستهای جهادی ازبک با انتشار بیانیه‌ای دولت سوریه را به اعمال فشار علیه خود و تهدید به بازداشت و اخراج از سوریه متهم کردند.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17007" target="_blank">📅 20:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17006">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">من بعید نمیدانم در این سفری که علامه جولانی به آمریکا داشته ، به پیشنهاد عربها از ترامپ دستوری جهت اخراج این وحوش اویغور و اوزبک و چچنی و … دریافت کرده باشد</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17006" target="_blank">📅 20:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17005">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWbrnfedIIHm5SIciVKpALwhF_74TGALCpRCgZaXmMTP-PLFW005sZq_2zoSkQIEJPC-C4JGzPUl4gcWmsah7gvPDgOpMw1X6GQ49kjwfZemzByICYj1huHhn1h_9EQQCTnGnnO-_i2jne0xC3fP-cAFKktQkiEc3xzDTHz5U8cz99jkrWNwM0XvzyE_cBUBjzQGzch7X1K6GnYz_Xhai8UlbKJ4UMM7yPjgifkpinEXTOzPOG250QbR6mTu8YxeW9rf-CiC2h5mq1C5HETGzHE1C_UjqffHrNvjEvvtxdzjUoYriebFYpPPMlV4xbvHr2swwP3flDS80HEo-KjIIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا چرا غیرقابل دانلود؟!</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/17005" target="_blank">📅 20:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17004">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شما ببینید وضعیت این منطقه گه گرفته چطوری است که پاکستانی که خودش در‌ همین مدت در غرب (بلوچستان)، شمال (وزیرستان) و شرق (هند) غرق در تنش و نکبت بوده حالا دارد برای ما میانجیگری می‌کند!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17004" target="_blank">📅 19:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17003">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پیروزی اوکراین با ربات ها و هوش مصنوعی !؟  در سال‌های اخیر، روایت حاکم بر جنگ روسیه و اوکراین حول محور بقای کی‌یف در برابر ماشین نظامی مسکو می‌چرخید. با این حال، شواهد میدانی و مواضع تحلیل‌گران غربی نشان می‌دهد که ورق به سود اوکراین برگشته و اکنون صحبت از…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17003" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17002">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxV11toQWISMYnjLEdJLNBS9FMfVApEI9h3h-KiUiDuzJRa8kHinm9vdtzj5gv5tzl26SQZ0-uIO23ptUP8To9wcs5NVu3CwWiUonBbg5KhXVKxzJ9K-mb1SrpzSw8-GDWZGvY0fW8CERxbnxV-I6qPfUPmuy0yHtR6Mi0IKVZA4EYO45mdVp21377vJhnT1cy-Q8rLn-Kz70-O6yR3teuZYlfefudV8Wj8uWwMacZvC5kCnZLEU1NG8LCoLt0waeMN2qC5HFTfLB2U3xffISg0g7K2W764x1NhWCUtZ5M4wflXAwasILrCsUbitRcIEIGx51TOYKRtJWsCb1QygZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
ربات ها درحال بازنویسی چهره جنگ امروز
♦️
رباتیک در میدان جنگ به عنوان نظامیان  برای کارهایی که بیش از حد معمول خطرناک، تکراری و یا با پیچیدگی خاص برای انسان است بکار میروند.
🔸
از هواپیماهای بدون سرنشین، عرضه به تانک های خودمختار به تانک های خودمختار، روبات…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/17002" target="_blank">📅 17:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17001">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔻
برخی شنیده ها حاکی از تلاش گروهی از نمایندگان مجلس برای استیضاح وزیر ارتباطات به جرم اجرای دستور رئیس جمهور و بازگشایی اینترنت می باشد</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/17001" target="_blank">📅 14:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17000">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">📡
اینترنت پاکستان ، به دلیل اعتراضات مردم علیه حکومت ، در آستانه خاموشی قرار دارد</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17000" target="_blank">📅 13:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16999">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✈️
پاول دوروف ؛ مالک تلگرام
:
فیلترینگ و محدودیت‌های اینترنتی، روسیه را به «حاکمیت دیجیتال» نزدیک‌تر نکرده، بلکه از آن دورتر کرده است.
به گفته دوروف، متخصصانی که می‌توانستند در روسیه سیستم‌عامل موبایل بسازند، به‌دلیل وضعیت خراب اینترنت، در حال ترک کشور هستند
او تأکید کرد تا زمانی که گوشی‌ها بر پایه سیستم‌عامل‌های آمریکایی مثل iOS و Android کار می‌کنند، حتی اپلیکیشن‌های «ملی» هم در برابر نظارت و سانسور از طریق بک‌دورها و فروشگاه‌های اپلیکیشن آسیب‌پذیر می‌مانند
دوروف این سیاست را «تغییر بسته‌بندی بدون تغییر اصل ماجرا» توصیف کرد و کنایه زد: مسئولی که به نام حاکمیت دیجیتال، اینترنت روسیه را خراب کرده و کشور را دهه‌ها عقب برده، شایسته دریافت مدال امنیت ملی از آمریکاست</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/16999" target="_blank">📅 12:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16998">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDhgRkW3QtVyVyYjL604Pz8cTqM_Mvz4T4kle-hkhCHt-3fRfEAJ9X8rgpCjq6j49vs0dBCuIImn-U6B3QKMJboKSmlmlN9ojnolF_g_sO4KvWH4HEnb-BjvwD8ljF8Rp0UjCyo7syMJHKHzvUSxCZ1Cu7_s6Ztw7vG6MHhPO6GfODsULNG-UfyOPScLzy2nZhSM_0lSOPf83gGAiYvGaUSQ53I5QKfFa1aCpOH515LaqC7E-Dh7dw_wsNjDRK6VIcJBd7GHB2HDAj4k5wX4ICUaSsqgUMpeKcH9DupQNw1pkn9jIgBga1sHrZGsaphqsoA5tnwUKejEvxK_DFFn6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
اینترنت پاکستان ، به دلیل اعتراضات مردم علیه حکومت ، در آستانه خاموشی قرار دارد</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/16998" target="_blank">📅 12:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16997">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">این یعنی نه ایران و نه روسیه از این جهش بهای نفت حداکثر استفاده را نبرده اند؛ ما به دلیل محاصره دریایی آمریکا صادراتمان افت کرده (پست ریپلای شده را ببینید) و روسها هم به دلیل حملات سنگین پهپادی اوکراین.  عربها هم که عمدتاً ضربه دیده اند و لذا بزرگترین منفعت…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/16997" target="_blank">📅 11:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16996">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ارتش لبنان اعلام کرده است که چندین نفر از پرسنل نظامی، از جمله یک افسر، در حمله هوایی اسرائیل که یک خودروی نظامی را در جاده الخالدیه–نبطیه هدف قرار داد، کشته شدند.  بر اساس گزارش‌های رسانه‌های لبنانی، این افسر دارای درجه سرتیپ بود.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/16996" target="_blank">📅 11:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16995">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ارتش لبنان اعلام کرده است که چندین نفر از پرسنل نظامی، از جمله یک افسر، در حمله هوایی اسرائیل که یک خودروی نظامی را در جاده الخالدیه–نبطیه هدف قرار داد، کشته شدند.
بر اساس گزارش‌های رسانه‌های لبنانی، این افسر دارای درجه سرتیپ بود.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/16995" target="_blank">📅 11:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16994">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دقت کنید که سنتکام می‌گوید که دوباره «سایتهای راداری نظارتی ساحلی ایرانی» را در گروک و قشم زده اند!  پیشتر اشاره شد چرا مهم است.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/16994" target="_blank">📅 09:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16993">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فرماندهی سنتکام:   چند لحظه پیش، نیروهای مرکز فرماندهی مرکزی چهار پهپاد تهاجمی انتحاری  ایرانی که به سمت تنگه هرمز پرتاب شده بودند را سرنگون کردند.   پهپادهای ‌تهاجمی تهدیدی فوری برای ترافیک دریایی منطقه ایجاد کرده بودند. نیروهای آمریکایی پس از آن به سایت‌های…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/16993" target="_blank">📅 09:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16992">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فرماندهی سنتکام:
چند لحظه پیش، نیروهای مرکز فرماندهی مرکزی چهار پهپاد تهاجمی انتحاری  ایرانی که به سمت تنگه هرمز پرتاب شده بودند را سرنگون کردند.
پهپادهای ‌تهاجمی تهدیدی فوری برای ترافیک دریایی منطقه ایجاد کرده بودند. نیروهای آمریکایی پس از آن به سایت‌های راداری نظارتی ساحلی ایرانی در گروک و در جزیره قشم برای دفاع در برابر حملات بیشتر حمله کردند.
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ به تهاجم بی‌دلیل ایران در چارچوب دفاع از خود آماده‌اند.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/16992" target="_blank">📅 02:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16991">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUHunhWpAlcU5RWcMb9OUp_MY345y42Th-G6D8fFwk9PdZCBTlSIi4FAEjzUPAq6-R-9f44mNqAoQ5_sEWtw2g0htG-00d6h44fWkZKIsXiP55RrfZqspLdO-HtboYdpwM1YMECKE-vsVs25V-Iv-MxTxB7k792rQpcpnIup6Fz8bKwcFGYy9OT5tW6XHlc2XtIq_Tb3PV_TapMY-YbtY-06TFKKccLs66sz3Zt4JW8rpAHLSQkyXk-iCZCkkWJjG7PORIh1jEq-qG2eMESonnba5glZGezUo3PeZSU64z37pOzq8cFfhVKrdtCyCbWlrqgGxMjGqfLk6gp1CRC-iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضرات مداوماً از جهش تورم در آمریکا سخن میگویند و آن را سند موفقیت خود میزنند!
این هم تورم مواد غذایی در کشور خودمان!</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/16991" target="_blank">📅 00:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16990">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فوری | ترامپ: در مدیریت پرونده ایران موفقیت بزرگی کسب خواهم کرد</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/16990" target="_blank">📅 23:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16989">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فوری | آکسیوس، به نقل از منابع: واشنگتن منتظر پاسخ رسمی ایران است و اختلافات باقی مانده را نسبتاً محدود توصیف می‌کند.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/16989" target="_blank">📅 22:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16988">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فوری | آکسیوس، به نقل از منابع: واشنگتن منتظر پاسخ رسمی ایران است و اختلافات باقی مانده را نسبتاً محدود توصیف می‌کند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/16988" target="_blank">📅 22:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16987">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فوری | اکسیوس، به نقل از دو منبع: اختلافی بین واشنگتن و تهران بر سر اندازه و زمان‌بندی آزادسازی وجوه مسدود شده.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/16987" target="_blank">📅 22:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16985">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
محسن رضایی در گفت‌وگو با سی‌ان‌ان:
🔹
اگر ترامپ مذاکرات را جدی بگیرد، ۲۴ میلیارد دلار برای آمریکا مبلغ زیادی نیست.
🔹
اگر او می‌خواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتمادی است که ایران می‌خواهد به طرف مقابل داشته باشد.
🔹
این آزمونی…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/16985" target="_blank">📅 21:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16984">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
محسن رضایی در گفت‌وگو با سی‌ان‌ان:
🔹
اگر ترامپ مذاکرات را جدی بگیرد، ۲۴ میلیارد دلار برای آمریکا مبلغ زیادی نیست.
🔹
اگر او می‌خواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتمادی است که ایران می‌خواهد به طرف مقابل داشته باشد.
🔹
این آزمونی است که آمریکا باید از آن عبور کند و راه باز خواهد بود. این پول ماست، نه پول آمریکا.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/16984" target="_blank">📅 21:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16983">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دستیار ایرانی به سی‌ان‌ان گفت دیدار خامنه‌ای با ترامپ رخ نخواهد داد</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/16983" target="_blank">📅 19:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16982">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رضایی ایران هشدار داد که اگر آمریکا درگیری را از سر بگیرد، ایران «جنگ را» فراتر از خلیج فارس خواهد کشاند -</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/16982" target="_blank">📅 19:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16981">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کاخ سفید:  دیدار عراقچی- ویتکاف  گفت‌وگوی مستقیم ویتکاف و عراقچی در مسقط    «استیون ویتکاف، فرستاده ویژه ریاست‌جمهوری آمریکا، به همراه آن اسکاروگیما، سفیر آمریکا در عمان، امروز در مسقط با دکتر عباس عراقچی، وزیر امور خارجه ایران، گفت‌وگوهایی انجام دادند؛ این…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/16981" target="_blank">📅 18:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16980">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گروسی:   ایران و آمریکا به توافق نزدیک شده‌اند</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/16980" target="_blank">📅 18:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16979">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گروسی:
ایران و آمریکا به توافق نزدیک شده‌اند</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/16979" target="_blank">📅 17:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16978">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ایران دارای یکی از بزرگترین ناوگان های نفتکش دنیا بود اما با این وضعیتی که پیش می رود باید از شوتی های زحمتکش مرزهای شرقی و جنوب شرقی کشور برای انتقال نفت بهره ببریم!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/16978" target="_blank">📅 16:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16977">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">Yinon_Plan.pdf</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/16977" target="_blank">📅 14:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16976">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">امیرحسین ثابتی:   آمریکا بعداز جام جهانی سنگین‌تر به ایران حمله خواهد کرد  ایران را تبدیل به غزه دوم خواهند کرد.  باید پیش‌دستانه پتروشیمی‌ها و زیرساخت‌های منطقه را بزنیم.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/16976" target="_blank">📅 13:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16975">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ایران_جنگ_را_برنده_نشد،_بلکه_چیز_خطرناک‌تری_را_به_دست_آورد.pdf</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/16975" target="_blank">📅 13:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16974">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMLI0jy0P4o3mfNiACfW2OdC0LUymh2oSF7Tn3-4lbhnp1G5sx2MuH3nwtNIYmprceda-jsw1-JUfmLP8pgwYzXHSOXpe1ojMhdshEeUCjvPHs9bHhQECBH4Ad3b0moFoDukK-Wwe5cE74-gPSMqUYh8jAyoCPUXuLEmV4tADKL7U6YumXYoSg9GfQtBm93CeYbi2QtPa4HlZPBhLV1cpmHtO5sax6-W8vPVXXnsPsU6ixZUrlhsREegXSX4N0opW3SeJD4c55oBaiP-O1SRzWpNzn6lS-go7v302MrHRqTVdmdrclK6ySEFHGezrAUCkhYcQgBPuAJK26RA8oXu6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدرسگ ها چه اسم هایی برای بندرشان گذاشته اند!  بعد انتظار دارند حمله نکنیم!</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/16974" target="_blank">📅 13:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16973">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">عمان پس از انفجار در بندر فهل، بارگیری نفت را متوقف کرد  سلطنت عمان بارگیری نفت در پایانه بندر فهل در خلیج عمان را به طور موقت متوقف کرده است. به گزارش رویترز، دلیل این امر انفجار در منطقه بندر است.  بندر فهل یک نقطه صادرات اصلی نفت خام عمان است. اختلالات…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/16973" target="_blank">📅 13:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16972">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دقت کرده اید هر کسی میانجی این جنگ بی پایان ما با آمریکا و اسرائیل شد به خاک رفت؟!  راند اول قطر میانجی شد و همان روز ایران به قطر حمله کرد و چند ماه بعدش اسرائیل هم به قطر حمله کرد و در جنگ اخیر هم با حمله موشکی وحشتناک ایران به تاسیسات گازی راس الفان، بیشترین…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/16972" target="_blank">📅 13:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16970">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SUjva7aYL9lmWJQrCuyU-qYlTtconh5SX2hnQbtZwDOofJ9kF2B3YAm1_dO7IMJOfl3qfaHGvIjFHTTLOdHFMAMiOGLbr_PuC8YmEBWiuTaIT6mEo0sLfdi2AkjFQ-X7F5H9C7K5m9vbQnQR6Sr-hvQTumSbtsYUjpedSZKtHQtKYcgW_YokONJT-NTrFYfRpez3GaHG963gtgvuzlS0cAl67fwlNre-tFYCXgJwp3E84RGknH9u_3cEESM5Mf9o3YVd002Usr-cc3gskwC8G9LJTd7wGWhp9Xxyva1aSlKThuAxo0Krjtj0uV0-ikUQxbQLIF6lNErBR4SS2KKyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVLRS9cznMHPO6BN2_KT77xypxnNPjdjf1gkwRLqs6oo4egFq9pptSI72nL0zjTvL6vAt34av8vXM6frDxHYgpamjJJ1Mr24LDhS553ts2wt3xFISGS8bwmRgbJTtMXItw34mXlFxvbnxpYNbv__TouaymTIWV10GPpuyjC_yIE-GZkbZKTXUim9McImznR8AS8URQtPtORNLpDLuoYYznfJdm8wb_CmUV6-D8kCwaLvBvUTEatKx072KjUl1HoO4axX0MYlIuq4jCl4wEo3d4ZllrI4O0qH4XQsDR2AXWD9Zq6L69alTdGLvR9bQjrWRmA2j8dMKjSgicd3d2_lZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم با خر یوگا میکردید بهتر بود ولی خب</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/16970" target="_blank">📅 12:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16969">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اکنون ثابت شده که باکو میزبان گروه های تکاوری و جاسوسی اسرائیل در حین جنگ بوده اند، منتهی دولت پوزیده صرفاً به استمالت از آنها ادامه داده و حتی یک موشک و پهپاد به تاسیسات آنها برخورد نکرده است.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16969" target="_blank">📅 11:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16968">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">این پوزیشن را دیروز به همراهان پیشنهاد دادم.  کماکان بر این باورم که خریدها سبک باشد و کسانی که سنگین کریپتو دارند این فرصت خروجشان است.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/16968" target="_blank">📅 11:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16967">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYK5lBPz8W6rpUQR8DXb-n42v2mhcY4Qy4-YRTgVoamr1iZoq9Cuu4wEYzlPUYAKS9hI9U7vHg4HwbPfUE2Fx3u2cEL24zukSDH1WQJUMhq_lW_K1JILJw5M7jLyCdvn9eYxnENLAhFbbhXd1TNy8SbfA4yUCRSmo-E-GL6ApO-HNH87NAls-WTjyHBUon-7xox11febkcrIa78s5TDYWMLXVSxEw46F7fkCepKyW6tE3KsJxG-r3R5DBwsE3xa7bxxPbdOo1Z_JYcz-Z1MLfGe9HjEBKXcTd4e3f08nhxfnaCVbrMyqQS5Dx5h3m85hr8GnZm9Fo2CweZQUiNZfMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری باکو بین ۵۰ تا ۶۰ درصد از نفت اسراییل را تامین می‌کند و میزبان بسیاری شرکت‌های نظامی و امنیتی اسراییل هم هست اما تا کنون از ضرب حملات موشکی و پهپادی سپاه به دور مانده است.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/16967" target="_blank">📅 11:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16966">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ایران_جنگ_را_برنده_نشد،_بلکه_چیز_خطرناک‌تری_را_به_دست_آورد.pdf</div>
  <div class="tg-doc-extra">232.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/16966" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این‌گونه_دکترین_نتانیاهو_برای_ایران_فروپاشید.pdf</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/16966" target="_blank">📅 11:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16965">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دورویی اروپا در قبال اسرائیل: محکومیت‌های کلامی و خریدهای میلیاردی سلاح
اروپا این روزها در قبال اسرائیل دو چهره متفاوت به نمایش می‌گذارد: چهره‌ای سیاسی که با محکومیت‌های پرسر و صدا و قطعنامه‌های نمادین، خود را مدافع اخلاق و حقوق بشر معرفی می‌کند، و چهره‌ای نظامی که در سکوت، میلیاردها دلار سلاح از همان کشور می‌خرد. سیاستمداران اروپایی با برگزاری کنفرانس‌های مطبوعاتی و رای دادن به تحریم‌های نمادین، سعی دارند تصویر یک قاره متعهد به ارزش‌های انسانی را به نمایش بگذارند، اما در پشت پرده، ژنرال‌ها و مسئولان نظامی با امضای قراردادها، واقعیت دیگری را رقم می‌زنند.
در ۲۶ مه ۲۰۲۶، شرکت البیت سیستمز اسرائیل اعلام کرد که سفارشات معوقه‌اش برای اولین بار از ۳۰ میلیارد دلار فراتر رفته است؛ رقمی که حتی پنج سال پیش هم غیرقابل تصور بود. در میان این اعلامیه، قراردادی ۱.۴ میلیارد دلاری با یک کشور اروپایی ناشناس برای مدرن‌سازی نظامی در حوزه‌های زمینی، هوایی و جنگ الکترونیک به چشم می‌خورد.. این در حالی است که کشورهای اروپایی با صدای بلند، صادرات سلاح به اسرائیل را متوقف کرده‌اند، تحریم‌های جزئی را مطرح می‌کنند و شرکت‌های اسرائیلی را از نمایشگاه‌های دفاعی اخراج می‌کنند.
اسپانیا صادرات سلاح به اسرائیل را متوقف کرد، چند کشور عضو ناتو تحریم‌هایی را پیشنهاد دادند و البیت سیستمز پس از اعتراضات از نمایشگاه یوروناوال فرانسه اخراج شد. اما در عمل، همین کشورها در سکوت، به خرید سلاح از اسرائیل ادامه می‌دهند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/16965" target="_blank">📅 10:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16964">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD2iLEGYj8DH_BDdwOJW2AHx-XKL5lxlvIXv-WSWcgyuUrM6IyCrIKuE-acENQSeUKLRNr_zlsgMYJgjnIAIMZxJolmx9IVfdUIhk1-MDgJID6_qN-nnrE9Sd-lniRvHTnAV5b2r1is_1bASS7mNTb7uh1QrGBWIhQ4ZPAoR0L-bnhj171WaDN1ZQuujP8hgGoXI9fX5JwRhONoZE3m7DsttzIApqOfrjgQ5CiewfwzR5cAYYaSvhNYFt3VGofNvqNO3bEgVuXLJrB6Gcybc120GTKbLxCzmWwa8Fh1hfUxUbZPjCvxaUdpB2lYA9El9hfqUB3FUEhXE50LuAzdKaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشتر گفته بودم که یکی از انگیزه های اسراییل از تعقیب پروژه تغییر رژیم در ایران ایجاد یک کریدور داوود بزرگ است که او را از امتداد آویزان بودن به آمریکا برای تامین امنیت ملی اش بی نیاز کند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/16964" target="_blank">📅 10:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16963">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">به گزارش بلومبرگ، بریتانیا و فرانسه تقریباً طرحی را برای اجرای عملیات مین‌روبی در تنگه هرمز، پس از توافق احتمالی بین آمریکا و ایران بر سر آتش‌بس دائمی، نهایی کرده‌اند.
این طرح یک تلاش چندملیتی خواهد بود و پس از بیش از یک ماه نشست‌های چندجانبه به رهبری دو کشور انجام می‌شود.
به گفته افراد مطلع از این طرح، این عملیات شامل ۱۵ کشور خواهد بود که پرسنل نظامی و تجهیزات خود را به مأموریت اختصاص می‌دهند و برای جلوگیری از درگیری، ارتباط مستقیم با ایران حفظ خواهد کرد</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16963" target="_blank">📅 09:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16962">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خواننده Secret Box از یک سال پیش آگاه بود که دلیل زدن هوانیروز و پایگاه ها و پاسگاه های مرزی ارتش و سپاه در مرزهای غربی، گشودن فضا برای ورود نیروهای مسلح کرد به داخل کشور بود.  اما چرا این طرح آن گونه که باید و شاید عملیاتی نشد؟!  بخوانید:   موساد سلاح‌های…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/16962" target="_blank">📅 00:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16961">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بشدت به همین سناریو که 2 ساعت پس از آغاز جنگ اشاره کردم، ایمان آورده ام. تقریباً تردیدی برایم نمانده که مدل «فروغ جاویدان» صدام را این بار نتانیاهو با پژاک و گروههای مشابه ش میخواهد اجرا کند.  نکته بدتر اینکه در صورت موفقیت این طرح و با ورود نیروهای شبه نظامی…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/16961" target="_blank">📅 00:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16960">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">محسن رضایی:
امیر قطر و ولیعهد عربستان دارند خودشان را با واقعیات تنظیم می‌کنند اما امارات، بحرین و کویت همچنان فکر می‌کنند قدرت آمریکا مثل قبل خواهد بود. این‌ها فکر نکنند که اگر این روش را ادامه دهند ما بعد از جنگ رهایشان خواهیم کرد. اگر امارات و کویت با صهیونیست‌ها همراه هستند باید ابوظبی و بوبیان را به عربستان و عراق بدهند!</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/16960" target="_blank">📅 00:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16959">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8DJ0LRkM7bNbq-iIF89OkZqSl7TuiUM7ceLOCDTXejiffdVXYd83uyzxM69SwRsILZyHh7IC7ZjhKkeCKM8eOLFm6B70pemCCnCeiB2Yg8SAtEshXZxOkXgUddZtzKMyn_6WGkFETGaLRYcfUTe_EVAVDUNZibg_xUgYmxB5KWBcz7coY_cw2GSrkV4bo-NxxlNMQ-wcAV1JILB0R75TMyzDPuEHw7TUDNq7W_7sm8tbCpmpsdW-LrKd9qqKAOtu_ickOJLlj2Bm5L91W6f8RE0ogqRwQ1o18AtQo6upc3k1rvBBLAt8pDBN8DrJXMvfY3iPt9ZIf3x9Eqhnsu3gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یعنی نه ایران و نه روسیه از این جهش بهای نفت حداکثر استفاده را نبرده اند؛ ما به دلیل محاصره دریایی آمریکا صادراتمان افت کرده (پست ریپلای شده را ببینید) و روسها هم به دلیل حملات سنگین پهپادی اوکراین.  عربها هم که عمدتاً ضربه دیده اند و لذا بزرگترین منفعت…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/16959" target="_blank">📅 21:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16958">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ایران و روسیه یک تفاهم‌نامه همکاری به ارزش ۲۵ میلیارد دلار در بخش هسته‌ای امضا کردند - تسنیم نیوز</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/16958" target="_blank">📅 20:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16957">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رویترز:   روسیه برای اولین بار اذعان کرد که تولید نفت این کشور در سال جاری کاهش یافته    این اعتراف در زمانی مطرح می‌شود که اوکراین در ماه‌های اخیر حملات پهپادی و موشکی خود را به تأسیسات انرژی روسیه تشدید کرده . آژانس بین‌المللی انرژی تخمین زده که تولید نفت…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/16957" target="_blank">📅 20:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16956">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">صنعت نفت ایران در سال ۲۰۲۶ با یکی از شدیدترین فشارهای صادراتی خود در سال‌های اخیر روبه‌رو شده است. داده‌های منتشرشده توسط شرکت ردیابی نفتکش Kpler و منابع تخصصی بازار انرژی نشان می‌دهد که از زمان آغاز درگیری‌ها و تشدید محدودیت‌های دریایی در اواخر فوریه، توانایی…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/16956" target="_blank">📅 20:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16955">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G65XBGOger4teZlwaat1zslAT-bGLITesp9mCqs1IWUhxjPAJ8x3pRCX9ZZnBvj0lwnw676zRDY_CJMkDPeE2Ajk20s3yBR5aMzKq8tPdJioQ6skCOC3Ve2IBx090SQC7-7d3MGeQCyi6TVGjSLAb63wFD7m6kHDJhtY1rjsTRTq7u3gRx82j9VeW0u1hhFfSAQG3em2TZB7jKWLLBnHZ_JSmVwXgfuRWcr9Ro6S0O17qSFmLCnkBXYioj-v-d6AnzVz1i-SmMl4-3pba5cWbxvZHA56JxdR6kxJVqx0lHJeBnfksKSAIhsQGs81fmd-jViERdTcCxM2NPDhpLVB-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:   در حال حاضر، ما کنترل کامل ۶۰ درصد از نوار غزه را در دست داریم و دستور من رسیدن به ۷۰ درصد است... ابتدا ۷۰ درصد. از همان شروع می‌کنیم</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/16955" target="_blank">📅 19:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16954">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حالا اینجا همه حضرات میگفتند ترامپ دست خالی از چین برگشت!</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/16954" target="_blank">📅 19:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16953">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔥
ثمره دیدار ترامپ و شی/ سپر چینی جلوی جهش قیمت نفت را گرفت
🔹
فایننشال تایمز نوشت که کاهش ۴ الی ۶ میلیون بشکه‌ای واردات نفت چین و استفاده این کشور از ذخایر نفت خود، منجر به کاهش تقاضا در بازار نفت و کاهش قیمت شده.
🔹
خاویر بلاس خبرنگار بلومبرگ می‌نویسد که…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/16953" target="_blank">📅 18:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16952">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6tMUMgu2UpxQoO4mQnHu7Cb0Rhx_WBGJ9XEOcKvEpDsoCFFPsq6WCnogc2MRu7xC09l75Rqh5R1kIV5Ch5KpcNcmdrUU2ilZ-GQ5_Au1TLuHjar-0AhSdfmXV8d6FDdctiea8KyEEzwazmgsYkAkDl772pjzEeYx6faYR3ZJhHJUOqYuZg-pJ13v0Qd4bYGTvZOQsXJHYscaRAJlqcKGkWbELcaadq2DDyyv31FfK_cYQyGGgnJ8myjr9QpZhHHNVRBbxLqCTTVczqLU9WaTVnj1S18eelXA0kE7DeiQUYxAMg6jcdxOtglLz9awCvR_rCwRfXDohfNywa9ZX0EhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/16952" target="_blank">📅 18:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16951">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D72G1YW_Bb2U5z-szVHpyW2aR6INf1QQq5pRUeUUn6YUSYfVWxxs5JXqMlNXcVE51sXO1BAsj5Tct6_GN1MjZa7MDUc46wS14BgnI6CrO8qEpmh4RFLVBvLp5XQ-9nOZqRBUICGYXMqEwR-JsuzMHj4Q-HbdCikWteLuhr59_ufPmqBj7nCRKS08qEZ4hltqUrIfZoafbzKLmWwnX4XFOe5PipWjJK6h6YryKsw1_QVhfy0OlNSMIjtqSnzSZo3JeUd-s0ms1Y1FhY1JynanuXx_5BF0Ys3DZn5SIxSCZrEvSefPwNTsfKbBguOfLEaMiz0zS46WswY3rsviD3E60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/16951" target="_blank">📅 17:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16950">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی (IAEA) اعلام کرد که نتوانسته به تأسیسات هسته‌ای ایران (به جز بوشهر) برای انجام فعالیت‌های راستی‌آزمایی میدانی دسترسی پیدا کند.
این موضوع نگرانی‌ها درباره خطرات اشاعه هسته‌ای را افزایش داده است.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/16950" target="_blank">📅 17:43 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
