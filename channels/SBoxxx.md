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
<img src="https://cdn4.telesco.pe/file/A013jTh73nirskfkb83HKedSC9ce9NIuZHKcfQtK5628b9oyTHFgfcBJkGkZmdOa_yqCuLGRtNyf5nE8f4YyOZGUjIcREaMmeyiLID3wvWhKKzxy1k867g3vp9jH05eUIW1K3Q0Wg0tkyijOY1h5cvaQsFSaQQ3liLZuOYcRTX36Bl01iz7SXwMP6qxvMQcm106ZfSzwsz_s5uSYTEvx8e7CfqsrRL38cAt89NsoW2XVaXYO2lEHhKuFgYbfsu14lmeH6pVcuAjHYYcTBbnTzmYtMtm2Rcy85xxsy7yYc8cx8RlYBgrtHOqiRmfl9IRFPeLQW9lTKCYPniEbAQbaeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 19:21:46</div>
<hr>

<div class="tg-post" id="msg-19916">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ:   ایرانی‌ها با ما بازی می‌کنند، در اتاق‌های جلسات موافقت می‌کنند و در رسانه‌ها رد می‌کنند.</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SBoxxx/19916" target="_blank">📅 18:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19915">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ: ایالات متحده می‌تواند به زودی با قدرت بسیار زیاد به ایران حمله کند.</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SBoxxx/19915" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19914">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqSKBK4fQ578NIOFU-6gOw3TvL1_RTdzWviHZhhM4AWGGE_FxsU-N7-kDzaQsd44bLjLKioxyvVjXE5bX-RzWfNHLRMYYXsCn_Ypk7lTHvOmmZ4SkA-fZF77d55tKGBPupX81I3pS8s1WVZ7fEl3PKky1S0oP1gAogz3Eo-YOV21AUMPFw4VnawZc9_iT7WRBPKe-RUD7WPnGB1gdk0DqbAsV4OL9hca1tkI9REB_eIutQnWyVKnaHGfh3GxXGzMyWykHhXoTDslDDOlrMGIWcibG-Yw-jfYMrE7lPUhE77ntULBPwQETVz-2Hx5DLpUbXMDmqWTlRlk2IxHyjxc8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط کم‌سابقه قتل در آمریکا
داده‌های جدید مربوط به نیمه نخست سال ۲۰۲۶ تصویری کم‌سابقه از وضعیت امنیت شهری آمریکا ارائه می‌کنند. بر اساس داده‌های Major Cities Chiefs Association که در نمودار نیز منعکس شده، در شماری از شهرهای بزرگ آمریکا میزان قتل به‌شدت کاهش یافته است.
این کاهش‌ها صرفاً محدود به چند شهر نیست. تحلیل داده‌های MCCA نشان می‌دهد که قتل در مجموعه شهرهای بزرگ آمریکا در نیمه نخست ۲۰۲۶ نسبت به مدت مشابه سال قبل حدود ۱۷.۲ درصد کاهش یافته است؛ بنابراین با یک روند گسترده‌تر در سراسر کشور مواجه هستیم، نه صرفاً یک اتفاق محلی.
یکی از عواملی که می‌توان در این تحول مورد توجه قرار داد، تغییر شدید سیاست مهاجرتی دولت آمریکا تحت رهبری دونالد ترامپ است. دولت ترامپ از آغاز دوره دوم ریاست‌جمهوری خود سیاستی بسیار سختگیرانه‌تر در قبال ورود غیرقانونی، بازداشت و اخراج مهاجران غیرقانونی اتخاذ کرده است. بر اساس آمار ارائه‌شده از سوی کاخ سفید، دولت در کنار کاهش شدید عبورهای غیرقانونی از مرز جنوبی، تعداد اخراج‌ها و بازداشت‌های مهاجرتی را نیز افزایش داده است.
از منظر سیاسی، دولت ترامپ این سیاست را مستقیماً بخشی از برنامه بازگرداندن امنیت عمومی معرفی می‌کند. افزایش فعالیت ICE، تمرکز بر افراد دارای سابقه کیفری، مقابله با شبکه‌های تبهکاری و کارتل‌ها و کاهش شدید ورود غیرقانونی، همگی می‌توانند از دیدگاه دولت نوعی افزایش بازدارندگی ایجاد کنند. داده‌های موجود نیز نشان می‌دهد اجرای سیاست‌های مهاجرتی در دوره ترامپ به‌طور محسوسی تشدید شده است؛ برای مثال، یک تحلیل مبتنی بر داده‌های ICE نشان می‌دهد تعداد بازداشت‌های ICE در مقطعی از سال ۲۰۲۶ نسبت به نیمه دوم دوره بایدن چند برابر شده است.
با این حال، نباید از نمودار فوق یک رابطه علّی قطعی میان سیاست مهاجرتی ترامپ و کاهش قتل استخراج کرد. روند کاهش جرم پیش از آغاز دولت دوم ترامپ نیز شروع شده بود و خود آکسیوس نیز تأکید می‌کند که کاهش جرم در دوره پایانی دولت بایدن آغاز شده و سپس در دوره ترامپ ادامه یافته است. علاوه بر این، عوامل متعددی مانند افزایش یا بهبود عملکرد پلیس، تغییر الگوهای باندهای جنایتکار، وضعیت اقتصادی، کاهش خشونت پساکرونا و سیاست‌های محلی می‌توانند در این روند نقش داشته باشند.
با این وجود، از منظر سیاسی می‌توان استدلال کرد که سیاست «مرزهای بسته‌تر، اخراج سریع‌تر و برخورد سخت‌تر با مجرمان» یکی از مؤلفه‌های محیط امنیتی جدید آمریکا است. کاهش ۶۰ درصدی یا بیشتر قتل در چندین حوزه قضایی، همراه با افت ۱۷.۲ درصدی در شهرهای بزرگ، نشان می‌دهد که آمریکا در حال تجربه یک چرخش مهم در شاخص‌های خشونت شهری است. بنابراین، حتی اگر هنوز برای نسبت‌دادن این تحول به یک سیاست مشخص زود باشد، دولت ترامپ اکنون می‌تواند این آمار را به‌عنوان شواهدی از موفقیت رویکرد امنیت از طریق اعمال قانون و کنترل مهاجرت در برابر منتقدان خود مطرح کند.</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SBoxxx/19914" target="_blank">📅 18:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19913">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ:
ایالات متحده می‌تواند به زودی با قدرت بسیار زیاد به ایران حمله کند.</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/SBoxxx/19913" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19912">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">خواجه آصف وزیر دفاع پاکستان، گفته است که ایالات متحده و ایران به توافقی در مورد تنگه هرمز نزدیک می‌شوند، با وجود اینکه هر دو طرف اخیراً مواضع سخت‌تری را در مذاکرات اتخاذ کرده‌اند.  او گفت: "به نظر می‌رسد که اوضاع به نفع صلح پیش می‌رود."</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/19912" target="_blank">📅 16:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19911">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">محسن رضایی:
تمام توانم را برای افزایش قدرت ایران به کار خواهم گرفت</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/19911" target="_blank">📅 16:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19910">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خواجه آصف وزیر دفاع پاکستان، گفته است که ایالات متحده و ایران به توافقی در مورد تنگه هرمز نزدیک می‌شوند، با وجود اینکه هر دو طرف اخیراً مواضع سخت‌تری را در مذاکرات اتخاذ کرده‌اند.  او گفت: "به نظر می‌رسد که اوضاع به نفع صلح پیش می‌رود."</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/19910" target="_blank">📅 16:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19909">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خواجه آصف وزیر دفاع پاکستان، گفته است که ایالات متحده و ایران به توافقی در مورد تنگه هرمز نزدیک می‌شوند، با وجود اینکه هر دو طرف اخیراً مواضع سخت‌تری را در مذاکرات اتخاذ کرده‌اند.
او گفت: "به نظر می‌رسد که اوضاع به نفع صلح پیش می‌رود."</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/19909" target="_blank">📅 16:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19908">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یک نفت کش که قصد داشته محاصره دریایی آمریکایی را بشکند هدف آتش نیروهای آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/19908" target="_blank">📅 16:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19907">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بازآرایی ساختار نظامی و امنیتی ایران؛ حرکت به سوی فرماندهی متمرکزتر و مقاوم‌تر
ایران پس از تجربه جنگ‌های ژوئن ۲۰۲۵ و بهار ۲۰۲۶ در حال بازطراحی بخش‌هایی از ساختار نظامی و امنیتی خود است؛ بازآرایی‌ای که به نظر می‌رسد مستقیماً از آسیب‌پذیری‌های آشکارشده در جریان حملات آمریکا و اسرائیل، به‌ویژه عملیات هدف‌گیری فرماندهان ارشد، ناشی شده باشد. مهم‌ترین تحول در این روند، تلاش برای ادغام ستاد کل نیروهای مسلح و ستاد مرکزی خاتم‌الانبیا است. ستاد کل مسئول سیاست‌گذاری و راهبرد نظامی و خاتم‌الانبیا مسئول فرماندهی عملیات مشترک در زمان جنگ است. جدایی این دو نهاد از سال ۲۰۱۶ یکی از منابع بالقوه موازی‌کاری در ساختار فرماندهی محسوب می‌شد و اکنون ادغام آنها می‌تواند با هدف ایجاد یک زنجیره فرماندهی کوتاه‌تر و منسجم‌تر انجام شود.
منطق این ادغام، صرفاً اداری نیست. ساختار جدید می‌تواند هماهنگی میان ارتش و سپاه را افزایش داده، کاغذبازی و بوروکراسی نهادی را کاهش دهد و سرعت تصمیم‌گیری در شرایط جنگی را بالا ببرد. اهمیت این مسئله پس از حملات «سر بریدن» بیشتر شده است؛ حملاتی که با حذف فرماندهان ارشد، توانایی ایران برای هماهنگی عملیات تلافی‌جویانه را مختل کردند. بنابراین، ایرلت ظاهراً در حال حرکت از مدلی است که در آن بخشی از ظرفیت فرماندهی به افراد و نهادهای متعدد وابسته است، به سوی ساختاری که بتواند حتی پس از حذف بخشی از رأس فرماندهی نیز به فعالیت خود ادامه دهد.
انتصابات جدید نیز همین جهت‌گیری را تقویت می‌کنند. علی عبداللهی علی‌آبادی در رأس ستاد کل قرار گرفته و هم‌زمان نقش او در خاتم‌الانبیا، وی را در مرکز ساختار فرماندهی مشترک قرار می‌دهد. سوابق او در سپاه، فرماندهی انتظامی، وزارت کشور و ساختار ستاد کل، ترکیبی از تجربه نظامی و امنیت داخلی را فراهم می‌کند. در کنار او، کیومرث حیدری، با سابقه فرماندهی نیروی زمینی ارتش و فعالیت در خاتم‌الانبیا، به لایه بالای ستاد کل اضافه شده است.
در سپاه نیز تثبیت احمد وحیدی در مقام فرمانده و انتصاب مصطفی ایزدی به‌عنوان معاون فرمانده، نشان‌دهنده بازسازی سریع زنجیره فرماندهی پس از ترور محمد پاک‌پور است. انتخاب ایزدی، که اخیراً مسئول حوزه سایبری و تهدیدات نوظهور خاتم‌الانبیا بوده، می‌تواند بیانگر اهمیت فزاینده جنگ مدرن، حوزه سایبری و تهدیدات نوظهور در معماری دفاعی جدید ایران باشد. انتصاب حسین طائب به فرماندهی بسیج نیز نشان می‌دهد که بازآرایی نظامی با لایه امنیت داخلی و بسیج اجتماعی پیوند خورده است.
در سطح امنیت ملی نیز تغییر دبیر شورای عالی امنیت ملی و جابه‌جایی مشاوران ارشد، بخشی از همین روند تمرکز قدرت و هماهنگ‌سازی ساختار تصمیم‌گیری است. در مجموع، تصویر ارائه‌شده در انتصابات اخیر حاکی از آن است که ایران پس از تجربه آسیب‌پذیری فرماندهی در جنگ‌های اخیر، در حال ایجاد ساختاری متمرکزتر، یکپارچه‌تر و کمتر وابسته به یک فرد یا نهاد منفرد است؛ ساختاری که هدف آن افزایش سرعت واکنش، هماهنگی ارتش و سپاه و حفظ تداوم فرماندهی در صورت تکرار حملات علیه رأس هرم نظامی است.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/19907" target="_blank">📅 16:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19906">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwkD7RGV2DJDzLX2Sxo6YO3qATsZScr_MHiiHUQr70aKi_lBMCV-IlCiuZDt-mcVcdmtP9zFZY5vQ6V-WmaypJhWkPeAAvcZppeIi8H7lOVRvKzc7ruwPtVRnVDciSjsy_BdVb9t48jbYlO_pP2xXy2MpGzEqMiWxqYhzcdC7o07oJU6QOYNp7vm6ctorR8aOaDyp9E6zkWNxm1d_nnz2x7YCS_xRMRr7UauNHRznEJ8Lp5jP3ngMYcqHvMg-t8NIWcEvrmdA9XomiuMjfUgXIRlbpYw6CwH_XIYhKat5zLPpdWdQKfyGQfjAPop9A_9B8KWZ9d95mo9SCLctfAkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه درگیری های میان انصارالله و نیروهای دولت رسمی یمن</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/19906" target="_blank">📅 15:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19905">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845af07e2f.mp4?token=K05_L8hWlURJPl0jDKnpabURjIReZOWuhA9CPPuCKHNxMBA2ch61nKDx6UBRgq6jbijBTspvNXvbE3Mrisld5nUklRyywXvz996TjboR4ePcaDeIv_wqZpA_NevXjDmE-uo9ATypaOnTcwQ6vqZytv7Fx5dZWhT91B8Zuh7CMdebqL0oyeH3mggxxTtsIdPJZQf3p4OPQKvmga3ds0bnsfshI-LuU3BlIccpPQrUsz1LyvQa1zerE8rpVh44yNEvZ2QTwjyU7CsOT47NSoHoGNYxJEkZUoVE_-N6CKGy5LHMZWcnHZpN32FVvqJZLmo7eUCXr_ywSoTBkAAlrQIQMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845af07e2f.mp4?token=K05_L8hWlURJPl0jDKnpabURjIReZOWuhA9CPPuCKHNxMBA2ch61nKDx6UBRgq6jbijBTspvNXvbE3Mrisld5nUklRyywXvz996TjboR4ePcaDeIv_wqZpA_NevXjDmE-uo9ATypaOnTcwQ6vqZytv7Fx5dZWhT91B8Zuh7CMdebqL0oyeH3mggxxTtsIdPJZQf3p4OPQKvmga3ds0bnsfshI-LuU3BlIccpPQrUsz1LyvQa1zerE8rpVh44yNEvZ2QTwjyU7CsOT47NSoHoGNYxJEkZUoVE_-N6CKGy5LHMZWcnHZpN32FVvqJZLmo7eUCXr_ywSoTBkAAlrQIQMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل بن گویر:  برای هر اشک یک مادر اسرائیلی، هزار مادر لبنانی باید بگریند. تمام لبنان باید بسوزد!</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/19905" target="_blank">📅 14:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19904">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">302.8 KB</div>
</div>
<a href="https://t.me/SBoxxx/19904" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 23</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/19904" target="_blank">📅 14:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19903">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">صد رحمت به جنگ (تحلیل ژئواکونومیک محاصره دریایی)  مجیدرضا حریری، رئیس اتاق بازرگانی ایران و چین، طی گفتگو با خبرآنلاین با تاکید بر ضرورت فوری پایان یافتن محاصره دریایی بنادر جنوبی ایران توسط سنتکام، گفته است: این محاصره باید پایان یابد؛ با مذاکره، خواهش، تهدید…</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/19903" target="_blank">📅 14:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19902">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آیا صادرات نفت ایران از مسیر ریلی می‌تواند جایگزین صادرات دریایی شود؟   در هفته‌های اخیر گزارش‌هایی منتشر شده مبنی بر اینکه ایران در حال بررسی استفاده از مسیرهای ریلی برای انتقال نفت خود به چین، به‌ویژه از طریق خاک افغانستان و آسیای مرکزی، است. این ایده در…</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/19902" target="_blank">📅 14:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19901">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 23</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19901" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 23
سه شنبه 11 آگوست 2026</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/19901" target="_blank">📅 13:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19900">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارشگر: گفتید این آخرین شانس ایران است. حالا چه؟  ترامپ: خواهید دید.</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/19900" target="_blank">📅 11:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19899">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lijRtFBOJkQq-jY0Law0l5AYlAJs-h4T-XaZdwhNTPUv_GEphd0KV5fuEa0qp4p0wGKpODEdAVXJluTyiWQWL8LKSutdGFVcLV2TPKaDGyEczPTawA8ZmyxhtCfJ5uOGa3WYtf6IibXD-24lh782mHvIZe1vz1H_fZapshishA2_2JW-4rRKz4ND4hhsUarw0iAv33rxhV8s7VmgGODd50oQoB6fwLCTVwVA5XuZfjtOb5jPCiBe3kTJnNuBfwjpAU7ilCmT0hqe6RKrdC1Ra6gA9ylx_v87xPzOXGlaKXJntPvK8fPOcU7CC0D9wOVeH4rjh8fcxSkhU2WKkPUEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه ای قرار دارد. در چنین شرایطی سیگنال قوی خرید یا فروش صادر نمی شود و بهترین راهبرد از دید من خرید در سطوح حمایتی پایین تر است.</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SBoxxx/19899" target="_blank">📅 11:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19898">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDDR2m60NkIhEf5f2fLHjep6Ukiajs8NJYyZtgRAQxRhmQq50VezaHP8L2Ui5lJrn24AfvHnmWoa21NA4hV0x1KG69iZqauA6-v2NHo-Yq3dLPpEQ4n5OW68rtDHQ6COM3677ydYEIk4XEmsOYApxxR9uwHyMqyy6jgTmTc2N4YIGS5QGDSEipN0hLTKDWg_KT59Nm-Lc7O8YZAi--aPaMuSMYd2eKATP3YYnD5SvdCj-I80RDVCB_R-s2ifmSEp1G3i1Z5cWkMfnkr-N5Aq7Vp495UirRho3Itq5gL2y9k1HBXQ-PW1zQhagUaW2WnlctgSfRN2o1iXXxW6Ub33bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با برجسته کردن بیگانگی فرهنگی امثال این چپول عرب تبار با فرهنگ غربی غالب در آمریکا به دنبال کاهش امکان شکست جمهوریخواهان در انتخابات نوامبر است.</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SBoxxx/19898" target="_blank">📅 11:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19897">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انزوای روزافزون در جهان   کاهش اهمیت راهبردی خاورمیانه برای واشنگتن و برونسپاری مدیریت خاورمیانه به اعراب مسلمان  قدرت گیری روزافزون ترکیه و محور اخوانی  نیاز به حضور مستقیم در بازی کریدورها</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/19897" target="_blank">📅 11:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19895">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qxHtrt9wl382FFQc0wu6pt0XBOn4MlL6EE8c8XNZPrCSS9_J7bZjLUH1YMAEM5tbwhUqe_AFqTPfMWYgVzMQR2MEj6CtMrBs87UgrZYP_QUqV7GYigso7Q1xH5GdW7kwkqBdBy8btXTfJifYezJdMBnhiy6Blh7KJnphmZN-L3LVye91VBw4j3u-W4ZJ6WMyK2za1C3Uw6RfEk_BAMqmNRM_nDsUI8wMNPZLBv0V37zb2f5LZraEbqDYDHdXQshOucizXsyQfbR-Pu12vZc2S2oLsVBUKAhKslrFsnaKqzs-fixM9n1C8QzohJulEKkyZlhTwXC6B6vdEZEF7ZeFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aA3-u5tVDEmn7wjPJMhmCRY8DBwoqNMS1SAiTsF_GMfISrM-ALHDf_xwRtGfN38f7lZ6qou7dDeY_FtSAz7507imPE-8t7DbFzHh_Y0bP6wEZ3tezo8NTvyqK_LlCKbM3YzV7nce7LOsz6eA3h7RCLDFdnA8kxudifhdEGF4rBpaoGAe4nWVtvtTqJMpmiddLwqNyz884CnAH2qSYo-3ouJpuq31amDCidoftcYlDCLY6Yd4ETt73IpS5exByVdKLt7xMKyTt5VxFZbdS0QGjXszOsT3XF6TODcCJf-kjJyVQsL59XGWVJmGbohVG1JR59alL_5mrYtgF0aF4PQEuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گزارش واشنگتن پست، دونالد ترامپ، رئیس‌جمهور، ماه گذشته پس از نشست ناتو، به دلیل تهدید ترور از سوی ایران، به صورت مخفیانه با یک هواپیمای C-32A نیروی هوایی ایالات متحده از آنکارا، ترکیه، خارج شد، در حالی که کاخ سفید به صورت عمومی اعلام می‌کرد که او با هواپیمای…</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/19895" target="_blank">📅 11:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19894">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">انصارالله یک کشتی تجاری عربستان را در باب المندب زد و ۳ نفر کشته شدند.</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/19894" target="_blank">📅 10:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19893">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فعلاً 2 کشور در خواهرمیانه با ائتلاف «مکه» مخالف هستند: ایران و اسرائیل</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/19893" target="_blank">📅 03:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19892">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">طبق گزارش واشنگتن پست، دونالد ترامپ، رئیس‌جمهور، ماه گذشته پس از نشست ناتو، به دلیل تهدید ترور از سوی ایران، به صورت مخفیانه با یک هواپیمای C-32A نیروی هوایی ایالات متحده از آنکارا، ترکیه، خارج شد، در حالی که کاخ سفید به صورت عمومی اعلام می‌کرد که او با هواپیمای…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/19892" target="_blank">📅 02:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19891">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbPLeR1AZtfRlcK7YCvSUwa8NuLusZZ9T6IBVMx-wJ7OVzbsNeDYnCFn3JVtG0FyZhvCqwwuwzp730kTLP6SRo9FW_WE3f4p6O2E9SdNKGUZKAvuf4vG18WaJS8Swu9m9eFAon-27foLvFsnAyomb3MYWO97mH0eVTw32c8dnM2TozQbRHcD9ynBq_4FwxLFNhXCcGmj-iXeeCh6JcWc6sJYwwhhibbnfw_rksYR25IBVCCm7GJJBsZBHsykp-5otKDNQpwK-Iv8LZ9K9j_ACu6ptq0_xwG2swdmOlRMO728SY9mee0RmIOcx9hduWPzbBiMP2M0wVfhIY2xJK-JYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفته می‌شود ایران در جریان سفر ترامپ، رئیس‌جمهور آمریکا به ترکیه، تلاش کرده است او را ترور کند.  اطلاعات ارائه شده توسط یک منبع خارجی که به مقامات آمریکایی در مورد این توطئه ادعایی هشدار داده بود، باعث شد تا در آخرین لحظه، هواپیمای مورد استفاده رئیس‌جمهور…</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/19891" target="_blank">📅 02:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19890">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMB7ULj3j6tlpuIiMXhA_7sW2krTVLagx1BCuJtr2qRHCzz6R5dIP3GnC9A4Luv7bzmlF7ss6gtPgj5AVGSH-kC1-YNix5mWNub-yFkeO_6eq4IOW3vya0dggORBJfcBLY324B6MOk5E9qGiBBGNp9T46TPzM7EadNPAbdEy9WGrlKVRAQ85zupMQXpEA1OvwzX-dsJAbgTSbR3kinDbWlVOptpjTsep_N5MMyExOKMCowlBVUnbQTbtEgPxhHIcKxyUQQrdp4NazDXLLpz0X0jnBReRGo_jvwHz4fKqvakflAuoB5eDAPzMi78Nv-DyqbwqJBJ8tFxUbswg41mGvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلاً 2 کشور در خواهرمیانه با ائتلاف «مکه» مخالف هستند: ایران و اسرائیل</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/19890" target="_blank">📅 02:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19889">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ra58AcigViuGeIFs9n9VnuZ4s2W1iRxoRagDA8ObgQBdjT6Uia5E_BZC_IOD7jASlqgI8D476W-7MZMTrLCZ0U0T7_5DXPN9J8Kssr7TD6Ih_MQtAQIGTk59tlk3TLgja0AGtDXZ-3HcVZlu3VbgqmqYrClrMNHgt2u9GO7EvsisM8VybMGcuJ2I_q1biHBtKn41z3hBIyZ8rFXNBtI4wkd0vpC7rrUnfHETyfXnYetj0BUHwbqdtkoxjshNIMcRvj4bese3f2-l0FrSKvzKkdaArzunFIRdxVH9QAv-eDJDzrxYkqQ-IXDIaYW57WMyzKDoID_0EMeITbaKSANEIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زمان آغاز جنگ ، ایران بیش از ۲۰۰۰ حمله هوایی، موشکی و پهپادی در سراسر خاورمیانه انجام داده و حداقل ۲۰ سایت مورد استفاده ارتش ایالات متحده در هشت کشور را آسیب رسانده است.
این حملات تا ۱۳ میلیارد دلار خسارت به تجهیزات ایالات متحده و تأسیسات نظامی وارد کرده است.
بیش از ۴۲ هواپیمای نظامی ایالات متحده نیز آسیب دیده یا نابود شده‌اند، از جمله چندین فروند که در پایگاه‌های هوایی پارک شده بودند.</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/19889" target="_blank">📅 01:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19888">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e06c6847.mp4?token=tsQoZlJTLuYEhXuwIGagwFzoN6yTN_UoCRIkfseuhBeaf40dWkkLJCgQ7Ho4uCqzDoaJuhCaS87uLKusuBle7IQFg-nL_ywkHu7iFzhp8_H4O6TZ7f_nE9FBrWDEiYrUd8d_Uk-qrS73keB3Cin4RPvioKopN4xzf1kRGP4uX9rmBUooT-Opx79gqMyUElyHaImVxaTxA7Jqu888xkLwyuhjjN1d9-8LrnjnP3uwlTvaWpepxTnJh1KQ9Y8PtnGHc-8waH9JJGJH8gxy46BxEiPhOE66wQ_UxaOkiMVXL9qGpMVqgxO-dxwQLOU6gl9FzNyVZZTps3TxkKV5x2903w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e06c6847.mp4?token=tsQoZlJTLuYEhXuwIGagwFzoN6yTN_UoCRIkfseuhBeaf40dWkkLJCgQ7Ho4uCqzDoaJuhCaS87uLKusuBle7IQFg-nL_ywkHu7iFzhp8_H4O6TZ7f_nE9FBrWDEiYrUd8d_Uk-qrS73keB3Cin4RPvioKopN4xzf1kRGP4uX9rmBUooT-Opx79gqMyUElyHaImVxaTxA7Jqu888xkLwyuhjjN1d9-8LrnjnP3uwlTvaWpepxTnJh1KQ9Y8PtnGHc-8waH9JJGJH8gxy46BxEiPhOE66wQ_UxaOkiMVXL9qGpMVqgxO-dxwQLOU6gl9FzNyVZZTps3TxkKV5x2903w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز زمینی بچه های تیم New Castle !
همه هم پنج سانت و ده سانت و …</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/19888" target="_blank">📅 01:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19887">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ درباره ایران:  آن‌ها می‌توانند دردسر درست کنند، اما ورشکسته هستند. پولی ندارند.  ایران کاملاً ورشکسته است. آن‌ها به سربازانشان حقوق نمی‌دهند.  تورم آن‌ها ۳۰۹ درصد است.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19887" target="_blank">📅 00:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19886">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گزارشگر: گفتید این آخرین شانس ایران است. حالا چه؟  ترامپ: خواهید دید.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19886" target="_blank">📅 23:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19885">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارشگر: گفتید این آخرین شانس ایران است. حالا چه؟
ترامپ: خواهید دید.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19885" target="_blank">📅 22:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19884">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ایران_تا_چه_اندازه_می‌تواند_تنگه_هرمز_را_به_یک_سلاح_ژئوپلیتیکی_تبدیل.pdf</div>
  <div class="tg-doc-extra">538.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19884" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکات بسنت در مورد تنگه هرمز:  تنگه هرمز دیگر هرگز به وضع سابق خود باز نخواهد گشت، زیرا ایرانی‌ها از آن به عنوان یک گلوگاه استفاده کرده‌اند، یا تلاش کرده‌اند از آن به همین منظور استفاده کنند.  آنچه در 2 سال آینده شاهد خواهیم بود، این است که تنگه هرمز از اهمیت…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19884" target="_blank">📅 22:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19883">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuEmC3G8gEYLkyolnyCfwGzS1uZMDDiux9vssIahYa5ulKR553Utq3ofkLWv6Ui7WEk0TSv5kfhu86QP4ujw_cAe2KWWqlaRKkVlBW1pMBcHt6OWQMxSLdZwtw6aMYjAWv5TkHQcd4Wsd43bYbdSl8MhFJKAqdZ8k67NbrCD7k1GKo8xU-Xs9ZnHq0AyICnUqAhkdn-G7fil3YWDR6sYbBoOadmKIEDuzgEkN0FkzAKG6xdqvMyTKaVBEGvW2cOPB3BWeJ91G6EcKWx6hvvUhPB7JQvmXbk6ASt9W6BaHYFQ_Js1U78izloh8-hxjNnEQ07uSkjZs3NvOYiLxhL8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح پایینی است و لذا اصلاح های محتمل نزولی طلا خرید دارد.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19883" target="_blank">📅 21:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19882">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">302.5 KB</div>
</div>
<a href="https://t.me/SBoxxx/19882" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 22</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19882" target="_blank">📅 21:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19881">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آمریکا پس از سوگند یاد کردن آبلاردو د لا اسپریلا، که با حمایت ترامپ به عنوان رئیس‌جمهور انتخاب شد، متعهد به ارائه یک میلیارد دلار کمک به کلمبیا شده است.  او وعده «جنگ تمام‌عیار» علیه تروریسم مواد مخدر، سرکوب نظامی سخت‌گیرانه‌تر علیه گروه‌های مسلح و روابط امنیتی…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19881" target="_blank">📅 20:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19880">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ:
🔹
من متوجه شدم که نمایندگان جمهوری اسلامی ایران درخواست غرامت برای خساراتی که در طول درگیری نظامی پنج ماه گذشته به آنها وارد شده است، دارند (درگیری که به این دلیل آغاز شد که "آنها نباید سلاح هسته‌ای داشته باشند"). با این حال، این موضوع در هیچ یک از…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19880" target="_blank">📅 20:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19879">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شرایط ایران برای باز کردن تنگه هرمز</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19879" target="_blank">📅 20:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19878">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔖
واشنگتن پست :
پنتاگون به مدیران صنایع دفاعی ۲۱ روز فرصت داد تا طرحی برای تولید سریع تسلیحات ارائه کنند</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19878" target="_blank">📅 18:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19877">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IX1k3CIiKVls-rzKybc4f6WH00R5tecrOCszOo_uTNrh6IRm9ntH_AxM_9dgfv_rOeKpjxR0jM1kE7n_9W9ZM0Mf10DQ7FzwylxoK1Qk9vkiDGBAIzAAHad2vccQGW-cDdpV0vj9FlYJaXqu-iyPAYlXMxy-_SgL9M9N2dhp9dVP371xa2Jpe633PnHbnd6hZoBwcpCP8VdlFwwt6-VG4zoJWViExbIrbNOVHuMVaHvSbi-CGySOn_8gCs-lyauuPLZBxNiW87cYsIdv-TwTDdDRmuJE3yjdMyiT6OEx7PxLZXyuqqQkMXJXlguud8Ty4sDythrbzAR3_TQXRR1Y1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
قانون «لیندسی گراهام»؛ تشدید فشار بر روسیه و ایران و آغاز یک جنگ اقتصادی با پیامدهای جهانی
قانون لیندسی گراهام با هدف تشدید فشار اقتصادی بر روسیه و ایران، تحریم‌ها را فراتر از کشورهای هدف برده و خریداران انرژی آنها، به‌ویژه چین و هند، را نیز تحت فشار قرار می‌دهد.
اجرای این سیاست می‌تواند جریان تجارت انرژی، قیمت نفت، تورم، نرخ بهره، دلار و بازارهای جهانی را تحت تأثیر قرار دهد و تحریم‌ها را به ابزاری برای شکل‌گیری یک جنگ اقتصادی گسترده‌تر تبدیل کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/19877" target="_blank">📅 16:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19876">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLbgi8QkweGfmvVatbX5QIo_wd8zb_V5tBNAOKFCr3tV040RCvW0-zRAdLZXSCs4mAFIVkFjXniT1bLgYCKr5nNCnob3QDjAspp3WIgZn9m1PiJhGN8QVfqx7jjhNVIxwvRiQbs-RIFe3q3mcjnH6oghnr_ITxpjYJg7v23aha7YPlmLZjudgjY5IkmOMsUeRtPkcHffpcerGZzSQ5IYt0_h7HLk57SEvmPAEGffmtMVwWPH0aMriCJV74OsBQXxuT98l2xEfLJmbIHGAeEYt9MTMmlsRAO2wSEKs4Ov5pDQI-VxmXLkKs7JCMRN0BeXm2dUIIhmE0cNkHt06zeW7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان:  علم را اگر بتوانیم توسعه بدهیم نیازی به نفت و گاز نداریم. ﻿</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19876" target="_blank">📅 16:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19875">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 22</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19875" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 22
دوشنبه 10 آگوست 2026</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19875" target="_blank">📅 14:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19874">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">— وزارت کشور عراق:
«هر پهپادی که بدون مجوزهای لازم پرتاب شود، به عنوان عملی تروریستی تلقی خواهد شد».</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19874" target="_blank">📅 13:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19873">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19873" target="_blank">📅 13:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19872">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فعلاً 2 کشور در خواهرمیانه با ائتلاف «مکه» مخالف هستند: ایران و اسرائیل</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19872" target="_blank">📅 12:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19871">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مایک والتز، سفیر ایالات متحده در سازمان ملل:  "عربستان سعودی، ترکیه، پاکستان و احتمالاً مصر در حال تلاش برای تشکیل یک ائتلاف دفاعی برای مقابله با ایران هستند."</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19871" target="_blank">📅 12:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19870">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbi_sv6a-tU6TzU-cr74hIgj6rWaksKbje0h2WJCRgRvmBdAoXeFKjIJuZP3sXqj8qv3fuGpO4qBeZToXA8YLiXHRRrsbQyYJaqxAy4oMmAwSMSgQhwTpau_4yioLpdrF6kI9c9cIfMgTpBQK-HztcsfoSvG1a-Hd2acby-FZfWrO5vZB5h3D_h-b2Ao7zVHwL1WNgL-IlW0d0t9SL1VSMKyRXwyeLq0G-GmA9PxXx_5dvtXzPSCi9TXH9-FPb3vPpfdMUO7p1jGeJdnoUNc3K1-BY8GhhsPDjDuqGMCO5zsXnuKwZpkwZvzGrrCF1ofInqOiGxGWoufW3HZ2JFHLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل جدیدترین و پیشرفته‌ترین زیردریایی خود را از آلمان تحویل گرفت
شرکت آلمانی
ThyssenKrupp Marine Systems (TKMS)
در اواخر ژوئیه ۲۰۲۶ زیردریایی جدید اسرائیل،
INS Drakon
، را در شهر کیل تحویل نیروی دریایی اسرائیل داد. این زیردریایی، ششمین فروند از خانواده
Dolphin
و سومین نمونه از نسل ارتقایافته
Dolphin II
در ناوگان زیرسطحی اسرائیل محسوب می‌شود.
دراگون با طول حدود
۷۳ متر
و جابه‌جایی بیش از
۲ هزار تن
، بزرگ‌ترین زیردریایی ساخته‌شده برای نیروی دریایی اسرائیل تاکنون است. این زیردریایی توسط شرکت آلمانی TKMS ساخته شده و از سامانه پیشران مستقل از هوا (
AIP
) بهره می‌برد؛ قابلیتی که امکان ماندگاری طولانی‌تر در زیر آب و انجام مأموریت‌های پنهانی در فواصل دور را فراهم می‌کند.
ارزش این زیردریایی در منابع مختلف حدود
۵۰۰ میلیون یورو
برآورد شده است. طراحی پیشرفته، برد عملیاتی بالا، سامانه‌های شناسایی مدرن و ظرفیت حمل تسلیحات مختلف، INS Drakon را به یکی از مهم‌ترین عناصر قدرت دریایی اسرائیل تبدیل می‌کند.
ورود این زیردریایی به ناوگان اسرائیل تنها یک ارتقای فنی نیست، بلکه پیامی راهبردی درباره حفظ برتری دریایی این کشور در محیط امنیتی متغیر خاورمیانه و شرق مدیترانه محسوب می‌شود.
در سال‌های اخیر، افزایش حضور نظامی ترکیه در شرق مدیترانه، توسعه نیروی دریایی این کشور، برنامه‌های مربوط به زیردریایی‌های جدید و رقابت بر سر نفوذ منطقه‌ای، اهمیت توان زیرسطحی اسرائیل را افزایش داده است. زیردریایی‌هایی مانند
INS Drakon
به اسرائیل امکان می‌دهند تا یک ظرفیت پنهان، دوربرد و مقاوم برای جمع‌آوری اطلاعات، عملیات دریایی و ایجاد
بازدارندگی در برابر رقبای منطقه‌ای حفظ کند.
اگرچه اسرائیل و ترکیه در مقاطع مختلف روابط امنیتی و نظامی داشته‌اند، اما اختلافات ژئوپلیتیکی دو کشور در موضوعاتی مانند شرق مدیترانه، منابع انرژی دریایی، سوریه و نفوذ منطقه‌ای، باعث شده است که هر دو طرف به تقویت توان نظامی و دریایی خود ادامه دهند.
تحویل
INS Drakon
را می‌توان بخشی از راهبرد بلندمدت اسرائیل برای حفظ برتری کیفی در حوزه دریایی و تضمین آزادی عمل در یکی از حساس‌ترین مناطق ژئوپلیتیکی جهان دانست؛ منطقه‌ای که رقابت قدرت‌های منطقه‌ای در آن به‌طور فزاینده‌ای در حال افزایش است.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19870" target="_blank">📅 12:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19869">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وزیر امور دیاسپورای اسرائیل، چیکلی:  اتحادیه مکه یک تحول بسیار خطرناک و نگران‌کننده است.  عربستان سعودی اساساً روی دیوار نشسته بود. آن‌ها قبلاً یک توافق دفاعی با پاکستان داشتند، اما به محض اینکه با ترکیه‌ای‌ها که در تقابل مستقیم با ما هستند و این تقابل می‌تواند…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/19869" target="_blank">📅 12:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19868">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بقائی:
بازگشایی تنگه هرمز به لغو محاصره دریایی آمریکا مشروط شد</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19868" target="_blank">📅 11:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19867">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcTtU6b1ONc8p-h7pl1_lHsKiDoIF1F_DzMNGSeMdtE9E9_pHty9kCFr5oCOVSHDjM4w6101imnLX5-1lcHIK3oFzk37y0S7MZV2n7CektS1KkbigUJZx_qMuU5QPCi7671_dSCVHQezNuyGRDwHLuxdsiPn6wCzFDcDEYsq9xlfol4qNDQzYeqNQ-QAy2L4yWd25rgGuJ6yHa5GK1_RMddzYBMgg8AaSC_BTvgwPoRzs9B-T9T32pYIv2DOg8QK0CXdFEs1_R1K6XTBk162a6jLfFQi-FmGEvDUjpR_51m3n2A0w97JBC_x19GNufPZuDc61T8VPJahHJA6Eyz_qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح پایینی است و لذا اصلاح های محتمل نزولی طلا خرید دارد.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19867" target="_blank">📅 11:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19866">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GhSKLCREHTqS30bKCZveARCKktAXoIVCLIa0VCt-v8qdnNBHQFay3aoVcYc9PN23LMYIu65moBNu4p2paF-y-aJGFnjR7alkztIvCITpehNb6cfwrEPrdJlWHT1Fc5C_ZxK2aXwp_pK4VDgu_f7AsowHasIDp3hy6C1gPCgahJlSeemW-EgHACxg2_LjzyyqQwHpFg70rgX4xFj8VPf_ZZ2SEMQIUXFRocIvVRRMg-kJWFwiInh2aUShZivYCzyKoGZSmVcV3jvLqKdooUw2bU_-tzk-cT5h-lS7OEnZym00usLCCRH8UUnqcUzsO3Y9IBZojKh7FUw9iM9O2f6rsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بشکه تاپاله
که گازشو لیلاز خورده
آبشو میثاقی
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/19866" target="_blank">📅 10:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19865">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سرنگونی یک پهپاد ناشناس در جنوب کشور توسط پدافند</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19865" target="_blank">📅 03:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19864">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">احتمال پیوستن مصر به توافقنامه سه جانبه عربستان، ترکیه و پاکستان   «هاکان فیدان» وزیر خارجه ترکیه مدعی شد که مصر ممکن است به این توافقنامه مشترک به محض حل و فصل برخی مسائل فنی بپیوندد.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19864" target="_blank">📅 02:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19863">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سرنگونی یک پهپاد ناشناس در جنوب کشور توسط پدافند</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19863" target="_blank">📅 01:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19862">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ما فقر شرافتمندانه داریم پدرسگ!  در ضمن علم بهتر است از ثروت!</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19862" target="_blank">📅 01:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19861">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ما فقر شرافتمندانه داریم پدرسگ!
در ضمن علم بهتر است از ثروت!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19861" target="_blank">📅 01:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19860">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7dUyysSO62STMuZgyfyFx6AEMpBN01al36-LiG3g_0bFAqspB4lvISudQjGVt3SpOdj0Js8Xn9J33H0Qs8kymtBCYMnDtUIV8mdAwQbdZWWU7N7p93xzAEV1SUeQ4gP9S-xNmJHPczLhsK7Tfw1Ark5o1SabzuZyvFTefeKOgqCfo-37fMSCssdywLa3KlDi0uUMrn6UVz3VvxzeAKuFZYPvoocj9WbJsXIYqWUZH7MCk6erRsjDotNIvHo2iuzy6Goq28Iv3HgH_N66HGdrdefUSGGWJYo6V7IX9CFati1e9vRTiD1g9YKfrIo-5nxiuItR_6R8PcNmK6dkUJJ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتصاب محسن رضایی به عنوان دبیر شورای عالی امنیت ملی با حکم پزشکیان  معاون ارتباطات و اطلاع‌رسانی دفتر رئیس جمهور:   با حکم ریاست جمهوری اسلامی ایران دکتر مسعود پزشکیان، محسن رضایی به عنوان دبیر شورای عالی امنیت ملی منصوب شد  سیدمهدی طباطبایی نوشت؛   نظر به…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19860" target="_blank">📅 00:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19859">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBYY2QQJZdRzvHKIgFbJ6x-nD4xtMaaHVu71oILllVzVFzjQH2uFfivH1rFxq6oaz6iQfMyGJui4nzbiKZfpdtQcCNXZhdzKFopPyDEYVA_qt-vbpI0JHauNxqcwBoXRdOOpmUYlEcNpRO6n7uR7vqo_c7tPyf7ubkK_zQvQDQsy0ZOGX5rRAuWXSJY9nNzuIITrIbx5TF2dJaLHMtpV3VksGeMBZ6pj4LvXe_pLnmMtupo3cQnb0-Kuj2WAJkkm6Ljz0BN3T05GsXaXya_UTTU7N5h_w8FOUsbW1EK7NLZd1P75y7cp6tb9Vy-8_laP-3rqdQvP_C1YLy_y96yHjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درباره ایران:  ما فقط در حال مذاکره نیمه‌کاره با آن‌ها هستیم. ما صرفاً ایران را با تورم عظیم و واقعیت اینکه پولی ندارند، زیر نظر داریم.  منبع: آکسیوس</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19859" target="_blank">📅 00:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19858">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بزنید شبکه آی فیلم سریال آیینه عبرت
عینا شرایط امروز ماست
سبحان الله!</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19858" target="_blank">📅 00:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19857">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شلیک از سیریک به سمت کشتی هایی در هرمز</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19857" target="_blank">📅 00:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19856">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">هواپیماهای جنگنده آمریکایی دو فروند هواگردی را که در حال نقض منطقه پرواز ممنوعه بر فراز ملک ترامپ در نیوجرسی بودند، متوقف کردند.  رئیس جمهور ترامپ در سلامت کامل است.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19856" target="_blank">📅 22:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19855">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بنا به گزارش‌ها، ایالات متحده فشار خود را بر اسرائیل برای کاهش درگیری‌ها در غزه، لبنان و ایران افزایش داده است.  واشنگتن خواسته است که اسرائیل حملات خود را کاهش دهد، از مواضع بیشتر در جنوب لبنان عقب‌نشینی کند و طرح اعزام نیروهای چندملیتی به غزه را پیش ببرد.…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19855" target="_blank">📅 22:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19854">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بنا
به گزارش‌ها، ایالات متحده فشار خود را بر اسرائیل برای کاهش درگیری‌ها در غزه، لبنان و ایران افزایش داده است.
واشنگتن خواسته است که اسرائیل حملات خود را کاهش دهد، از مواضع بیشتر در جنوب لبنان عقب‌نشینی کند و طرح اعزام نیروهای چندملیتی به غزه را پیش ببرد.
اسرائیل با برخی از این درخواست‌ها مخالفت کرده است. نتانیاهو گفته است که ارتش دفاعی اسرائیل به مقابله با تهدیدها ادامه خواهد داد و اسرائیل این گزینه را برای حمله به ایران حفظ می‌کند، در صورتی که ایران از سرگیری فعالیت‌های هسته‌ای یا توسعه موشک‌های بالستیک را آغاز کند.
منبع: شبکه ۱۲ اسرائیل</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19854" target="_blank">📅 22:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19853">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59886795a.mp4?token=eLdsKawNhIRKwseeebf5rRb2wC2PT_8JMH1GTBV2cdTs1P602QBgOunmVEMNkoqMU3Mt9kNOFagPD8mosc_yxAWFGOzqiIi-4FJeAkvbXuVBQx6kn0rPheqwEnx45LeCMDat1zp3NXaxJf0eIUK2-DegQtdL1e0TGiSjzP6PJRiloavn6eAj3IQ_xL3qoUfHJrpgJOF371Lu_kejE98KQ-rlciiuE6-PLV8l1UcB_ZiVVZp5JzK-_WCOHStDZRbRcG8OBgKvVLx5S-m6_tq1_1KOtfu5X5XJxlZHIMrsVjtmvD9Ka4NgVhbJ_8Gkd8v-kfDY2SDdfvW_GRFQw9qCYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59886795a.mp4?token=eLdsKawNhIRKwseeebf5rRb2wC2PT_8JMH1GTBV2cdTs1P602QBgOunmVEMNkoqMU3Mt9kNOFagPD8mosc_yxAWFGOzqiIi-4FJeAkvbXuVBQx6kn0rPheqwEnx45LeCMDat1zp3NXaxJf0eIUK2-DegQtdL1e0TGiSjzP6PJRiloavn6eAj3IQ_xL3qoUfHJrpgJOF371Lu_kejE98KQ-rlciiuE6-PLV8l1UcB_ZiVVZp5JzK-_WCOHStDZRbRcG8OBgKvVLx5S-m6_tq1_1KOtfu5X5XJxlZHIMrsVjtmvD9Ka4NgVhbJ_8Gkd8v-kfDY2SDdfvW_GRFQw9qCYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19853" target="_blank">📅 21:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19852">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🟤
«محسن رضایی» نماینده رهبر معظم انقلاب در شورای عالی امنیت ملی شد.    شنیده‌ها حاکیست که آقای محسن رضایی به عنوان نماینده رهبر معظم انقلاب به ترکیب شورای عالی امنیت ملی کشورمان ملحق شده است. بر این اساس، هم‌اینک آقایان محسن رضایی و سعید جلیلی به عنوان نمایندگان…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19852" target="_blank">📅 21:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19850">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🟤
«محسن رضایی» نماینده رهبر معظم انقلاب در شورای عالی امنیت ملی شد.    شنیده‌ها حاکیست که آقای محسن رضایی به عنوان نماینده رهبر معظم انقلاب به ترکیب شورای عالی امنیت ملی کشورمان ملحق شده است. بر این اساس، هم‌اینک آقایان محسن رضایی و سعید جلیلی به عنوان نمایندگان…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19850" target="_blank">📅 21:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19849">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔥
توقف ۲۲ روزه صادرات نفت ایران از خارک
🔹
ویندوارد: خط صادرات نفت ایران از جزیره خارک، تحت تاثیر محاصره دریایی آمریکا، برای بیست‌ودومین روز متوالی متوقف مانده.
🔹
هر سه پایانه غربی، LPG و شرقی خارک همچنان بدون بارگیری هستند. @khate_energy</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19849" target="_blank">📅 20:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19848">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7c7abbdc.mp4?token=RUAVlPv_r5xvFxCV69UZg8u1TcqM7Z3HDUTtGaIYmiR9dzVoFIuUTQWCbPkoLnXIQ-MpUEiqESG4t2wHx9Je_5c6sQgxOC_p9Rwi7hAQy578kfWvGct-GCmfwBVm7AMqNBYA6tK_DUz5aecT9bErgUwDDMBjG2BIvgvZtJ4u6Bvp1SRLB3ZuLZR7HUqFlPRgjbLutt_TobhWw5B2UjC7aKq1YHlCQQTexHwHphEdKD6QR1rE77iEm-YsBgPpQuLYo-F2RyqgDdsRbkHJP6kkoVq1i8u6Nc1mvsupWOplsMarg3yRkhL-89ew3E6PJpLK2s3WNo410cjByX3_obmyHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7c7abbdc.mp4?token=RUAVlPv_r5xvFxCV69UZg8u1TcqM7Z3HDUTtGaIYmiR9dzVoFIuUTQWCbPkoLnXIQ-MpUEiqESG4t2wHx9Je_5c6sQgxOC_p9Rwi7hAQy578kfWvGct-GCmfwBVm7AMqNBYA6tK_DUz5aecT9bErgUwDDMBjG2BIvgvZtJ4u6Bvp1SRLB3ZuLZR7HUqFlPRgjbLutt_TobhWw5B2UjC7aKq1YHlCQQTexHwHphEdKD6QR1rE77iEm-YsBgPpQuLYo-F2RyqgDdsRbkHJP6kkoVq1i8u6Nc1mvsupWOplsMarg3yRkhL-89ew3E6PJpLK2s3WNo410cjByX3_obmyHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باز همین که ۲ سانت عسل هم داشته خیلی خوب بوده</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19848" target="_blank">📅 20:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19847">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ایالات متحده توانسته صادرات نفت ایران را فلج کند – فایننشال تایمز   این روزنامه با استناد به داده‌های ماهواره‌ای گزارش می‌دهد که ایران حدود یک هفته است که در جزیره خارک نفت خام را در نفتکش‌ها بارگیری نکرده است.   این جزیره اصلی‌ترین پایگاه ترانزیت نفت کشور…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19847" target="_blank">📅 19:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19846">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پزشکیان:  علم را اگر بتوانیم توسعه بدهیم نیازی به نفت و گاز نداریم. ﻿</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19846" target="_blank">📅 18:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19845">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پزشکیان:
علم را اگر بتوانیم توسعه بدهیم نیازی به نفت و گاز نداریم.
﻿</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19845" target="_blank">📅 18:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19844">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حالا باید ببینیم ائتلاف «مکه» پاسخ می‌دهد یا صرفا برای دوشیدن گاو شیرده حجاز و نجد تشکیل شده.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19844" target="_blank">📅 18:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19843">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وال استریت ژورنال:
ترامپ امیدوار بود که بازگشایی تنگه هرمز به او راهی برای اعلام پیروزی و پایان دادن به درگیری با ایران بدهد، حتی بدون توافق هسته‌ای. اما تهران خواسته‌های خود را به شدت افزایش داده است.
ایران خواهان خروج نیروهای آمریکایی از منطقه، لغو محاصره دریایی، برداشتن تحریم‌ها، آزادسازی دارایی‌های مسدود شده و دریافت میلیاردها دلار غرامت جنگی پیش از بازگشایی کامل تنگه است.
این موضوع گزینه‌های کمتری را برای ترامپ باقی می‌گذارد. به نظر می‌رسد ایران معتقد است واشنگتن برای خروج اشتیاق دارد و از توانایی خود در به هم زدن تنگه هرمز و جریان جهانی نفت به عنوان اهرم فشار استفاده می‌کند.
با قیمت بنزین در ایالات متحده حدود ۴ دلار برای هر گالن و نزدیک شدن به انتخابات نوامبر ، ترامپ انگیزه‌های قوی برای به دست آوردن یک توافق دارد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19843" target="_blank">📅 16:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19842">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حمله نفتی آمریکا به گرینلند!
روزنامه انگلیسی گاردین:
یک شرکت نفتی آمریکایی با نام «گرینلند انرجی» با تجهیزات کامل در سواحل شرقی گرینلند پهلو گرفته و قصد دارد با ۶۰ میلیون دلار، دو حلقه حفاری کند.
دولت گرینلند هشدار شدیداللحنی به شرکت نفتی صادر و اعلام کرد که هیچ گونه مجوزی برای این عملیات صادر نشده.
مسئولان این شرکت آمریکایی ادعا می‌کنند که منطقه «جیمسون لند» ممکن است حاوی نفت خامی به ارزش یک تریلیون دلار باشد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19842" target="_blank">📅 15:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19841">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نتانیاهو:  ما می‌دانیم چگونه در برابر بزرگترین دوستانمان، حتی در صورت لزوم، بر موضع خود بایستیم.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19841" target="_blank">📅 14:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19840">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نتانیاهو:  اسرائیل سند ۱۵ بندی شورای صلح غزه را رد می‌کند.  ارتش اسرائیل تا زمانی که حماس «به‌طور واقعی» خلع سلاح نشود، هیچ گونه عقب‌نشینی‌ای را انجام نخواهد داد.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19840" target="_blank">📅 14:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19839">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نتانیاهو:
اسرائیل سند ۱۵ بندی شورای صلح غزه را رد می‌کند.
ارتش اسرائیل تا زمانی که حماس «به‌طور واقعی» خلع سلاح نشود، هیچ گونه عقب‌نشینی‌ای را انجام نخواهد داد.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19839" target="_blank">📅 14:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19838">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🟤
«محسن رضایی» نماینده رهبر معظم انقلاب در شورای عالی امنیت ملی شد.    شنیده‌ها حاکیست که آقای محسن رضایی به عنوان نماینده رهبر معظم انقلاب به ترکیب شورای عالی امنیت ملی کشورمان ملحق شده است. بر این اساس، هم‌اینک آقایان محسن رضایی و سعید جلیلی به عنوان نمایندگان…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19838" target="_blank">📅 14:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19837">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">منابع غیررسمی تاکید دارند محسن رضایی دبیر شورای عالی امنیت ملی ایران شده است</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19837" target="_blank">📅 14:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19836">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e51206b9fc.mp4?token=S79w7AiL9qntYSA085cVj3eKMurXL9bDXdXjpIasOFXUaiQ_sEacj9ssa6urDvDMaVaPO08dXXa1WuvjfBLs4Sd7oyWu9hvACdiVN42Soq5NNbLduh-TvH32tdRrPQoCSv7xvM8QTSKoB3dB_RLBGoCTRfBww9jGJoDcO329PFR7Uv4tDL7Wz-279N2j91hgebqtW9RF0pwcF8nxeVG2BmElzrHJyzAIIn9XgbM-eG267yZAOXI7ogT1o1lwP9CaSKmW4WrMN3mMLKGzHixCO7kjyyR5yGsE34rd4h4tV9rmZDYfvjdi8gQpS7_VJeQpYhWnEM5tce1j2eJVg4FgLg3VBcRSwXnILi1Blk8tiTvgrKIfjlN41qbx7aArTCc7L1T6yAG0Dx75zvLsJ2kZf31o2WfqpWxW67S0Rggq7woHu11YF8PBWSDalQ_NMjSTtC1tp-oY3hhRa5LDRqvj_1xxxO4Y8tKBhO6qyueFNzkdI7V0YaiD8gGgcgj_ZWatJDOD3oWFE7lfwDpzQLOapdSILat8D-V3QGPKYAngyXisu5TflV7uP3BuImFWiOf9ri-eH9OVA3SNmHFClSWZXMM99iRu2S5Tvre1SfIUyTUorP4YO-VSMOl9HL1XDiegFUzIyDitl0cMZI_QalSo26vNf5lpFGYZ6rGcfB9oOzc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e51206b9fc.mp4?token=S79w7AiL9qntYSA085cVj3eKMurXL9bDXdXjpIasOFXUaiQ_sEacj9ssa6urDvDMaVaPO08dXXa1WuvjfBLs4Sd7oyWu9hvACdiVN42Soq5NNbLduh-TvH32tdRrPQoCSv7xvM8QTSKoB3dB_RLBGoCTRfBww9jGJoDcO329PFR7Uv4tDL7Wz-279N2j91hgebqtW9RF0pwcF8nxeVG2BmElzrHJyzAIIn9XgbM-eG267yZAOXI7ogT1o1lwP9CaSKmW4WrMN3mMLKGzHixCO7kjyyR5yGsE34rd4h4tV9rmZDYfvjdi8gQpS7_VJeQpYhWnEM5tce1j2eJVg4FgLg3VBcRSwXnILi1Blk8tiTvgrKIfjlN41qbx7aArTCc7L1T6yAG0Dx75zvLsJ2kZf31o2WfqpWxW67S0Rggq7woHu11YF8PBWSDalQ_NMjSTtC1tp-oY3hhRa5LDRqvj_1xxxO4Y8tKBhO6qyueFNzkdI7V0YaiD8gGgcgj_ZWatJDOD3oWFE7lfwDpzQLOapdSILat8D-V3QGPKYAngyXisu5TflV7uP3BuImFWiOf9ri-eH9OVA3SNmHFClSWZXMM99iRu2S5Tvre1SfIUyTUorP4YO-VSMOl9HL1XDiegFUzIyDitl0cMZI_QalSo26vNf5lpFGYZ6rGcfB9oOzc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرکز مطالعات سیاسی وزارت خارجه!</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19836" target="_blank">📅 14:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19835">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">منابع غیررسمی تاکید دارند محسن رضایی دبیر شورای عالی امنیت ملی ایران شده است</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19835" target="_blank">📅 13:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19834">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ با برجسته کردن بیگانگی فرهنگی امثال این چپول عرب تبار با فرهنگ غربی غالب در آمریکا به دنبال کاهش امکان شکست جمهوریخواهان در انتخابات نوامبر است.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19834" target="_blank">📅 12:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19833">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MupVkrtFU_Vg-5I2_D878YW7KcnaI43EHuE9XYhxwfy_NrsN2vu8nXhVv5QRsVVTx_dOEkXTvVFFbhPMxk8KgZy3MmetwNLnCTaSbleWdjQx00BeJ-jWTDNaya_Inwz97lQq-KJvgDqdPuWUxcTy3C9F0wMhJtSORF03YbYPyuFhjjJE_OY3yYGj9Buz3feJfZK_isW5hUAx7jY3G99S8_GsSkwn1EOFaZlC25WNrPP_xU84e3Uv1CArLgT1lVg4IOWyDtD7P7ndgLUq1BmKlpsZy8Qq0595L5uhX1q-JuYto8ddH2uikq03gfwRnV_tqR2jrkv9kdYTStT6Vv2scg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه بوزینه ای که میبینید، متعلق به جناح چپ حزب دموکرات هستند که اخیراً در انتخابات حزبی دموکراتها به پیروزی رسیده اند.  این روند ادامه یابد، دستکم 10 تا 15 درصد از کرسیهای کنگره آمریکا به جناح بوزینگان خواهدرسید و این یعنی دموکراتها برای تصویب هر طرحی نیاز…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19833" target="_blank">📅 11:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19832">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">طبق گزارش‌های لبنانی، ترکیه از سوریه و حزب‌الله خواسته است تا در یک جلسه با یکدیگر دیدار کنند. ترکیه همچنین اعلام کرده است که آماده مشارکت اقتصادی و نظامی در چارچوب یک نیروی است که در لبنان مستقر خواهد شد.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19832" target="_blank">📅 11:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19831">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">به لطف خدا، پالایشگاه آرامکو در عربستان را با پهپاد هدف قرار دادیم!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19831" target="_blank">📅 11:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19830">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">به لطف خدا، پالایشگاه آرامکو در عربستان را با پهپاد هدف قرار دادیم!</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19830" target="_blank">📅 11:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19829">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19829" target="_blank">📅 11:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19828">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a7c5e0be.mp4?token=uWG30GpQHtDDpIR3MVSgPH6dbR_0fKUTzHqfJFrevfBY0NE2aHHaKid9V4rdN7al3iuq_dJ_lneb7alK5HcjDopoT6bHVtBqTjTbHcJ9adKlkG2Sr-00GZbRuamtNqZegATt5Uej6POeAlCkBlk38F0RhZR6puwFKo9qsGQOEyALrxTkhwsaOHnv6-dAHWriRVdVfUxRMrkbqtRCK23mfp0h-2auMnRkH7Y7R0LEy0lVw6dMvDqMRpXD8FAyJqBrAbt42F2qVNrv_RXEl71sNkoC35yf3N-Tzh7KgUPDzeALJeZp2Leeeh64X9CYmowShmf3YUn9sHFrVQ_C3D_rgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a7c5e0be.mp4?token=uWG30GpQHtDDpIR3MVSgPH6dbR_0fKUTzHqfJFrevfBY0NE2aHHaKid9V4rdN7al3iuq_dJ_lneb7alK5HcjDopoT6bHVtBqTjTbHcJ9adKlkG2Sr-00GZbRuamtNqZegATt5Uej6POeAlCkBlk38F0RhZR6puwFKo9qsGQOEyALrxTkhwsaOHnv6-dAHWriRVdVfUxRMrkbqtRCK23mfp0h-2auMnRkH7Y7R0LEy0lVw6dMvDqMRpXD8FAyJqBrAbt42F2qVNrv_RXEl71sNkoC35yf3N-Tzh7KgUPDzeALJeZp2Leeeh64X9CYmowShmf3YUn9sHFrVQ_C3D_rgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ظاهرا اوضاع جو خواب آلو خراب است و بزودی به خواب ابدی خواهدرفت.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19828" target="_blank">📅 02:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19827">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ظاهرا اوضاع جو خواب آلو خراب است و بزودی به خواب ابدی خواهدرفت.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19827" target="_blank">📅 02:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19826">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">محاصره اقتصادی | فعال شدن گروه های جدایی خواه</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19826" target="_blank">📅 02:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19823">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1xUWFS_IbbLdsOd1MmqZ2_b8_FdSioga7YE2IP2D5zuQ277gEL8QzHzCAVuACb6A9hx7Qu3Xf9uzqoJA-c39CX8L1fEetIUqZBVum7WtnlexkwzkCSqwNCk4BHCqGEVtmooBOLPydCIem7E0G70LRQQFZN8ukBSXYPR6NdCZQzdkK3ro_fIGoEnvHxqWFF1cZj1AeWSl6mhpD_IYgf-mSVB46vq9VbIsnepFpkDVsK8d6l75Igjm8UfFwZUcN_FrBI66DO_2bx4kHtV1rw9ZDzof-TSKCudDAA6P7h6EWIRCLuLR5Risx0mmdlG7sSg5Jm4vKiNAZ3YD-dRKB_cWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r6TLh3NLJ4fx94CTdq-Ra18rlDTVepU27F3n-JuK_Kc-qqYTA1BOTqzHqRRTrohw54q5rnDjS9lzk25slyPTbY_mdMXBD1sZX8VVUdWuXYNvkx2tqlcW_s_p55EsgFoaqjguayDmsYJuu7nH41LUIVPIJCN0STOOEtNmQMMTsodpCFEKKxpG2vfeUhlTQE3NNyHP8VL-KRWcCqv0J5bf6mNjNmobV_yfmmAHJJ5_pNWTxCr1nNgPunFQh7ByauAsNL0CBDEIqOFRgwpM1TI0WvAOmrvL6U5U9zsZ8CB2ERgUX49JXNHxNhQPd0Ms65n9PFxS2Bu0pAdRGys0xn6KrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ef3PUvF3URzOs9Bu5kussm4HbkWbvCYlp7q2TlmVBlurdJ2Ugh3RaIONoUL0CHqZ6IN1J5EkIEIRF5jcbdh7H7AI1BrMx1Rwkb1r0BYdNijiM0akWS6WRg8IynM_Jdh_Day1T81LGNrV_6oPqsQbLX1bE2tUuWEA8s6Tq8hMqPPlaDEMiikwcjXJLQd3lZkvghmfrJocYp06fwSpyJojtV2Qo_5hEhOny4-bOGY6927CySr6WreMLzlbl4SrED5BqdHbOddgWcbzrcgUUrAFXweadpEWTJpUEYNNswxKDn9-mKXqAgnv4vbNdk7xT-0W0saMdvs71r9vq5NN1h8wDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این سه بوزینه ای که میبینید، متعلق به جناح چپ حزب دموکرات هستند که اخیراً در انتخابات حزبی دموکراتها به پیروزی رسیده اند.
این روند ادامه یابد، دستکم 10 تا 15 درصد از کرسیهای کنگره آمریکا به جناح بوزینگان خواهدرسید و این یعنی دموکراتها برای تصویب هر طرحی نیاز به استمالت این جانوران خواهندداشت.
بیخود نیست ترامپ و دیگران — حتی برخی دموکراتهایی که کامل عقل خود را از دست نداده اند — از خطر کمونیسم در آمریکا می گویند.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19823" target="_blank">📅 01:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19822">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBJfLlTlQF4t3ybqpq9fVdLll0l81_iXqDS0eExoseeGSaBoGO0Jhu4NpAHQjivrZlEfZm0ypVekcdttc_ow_m237ARxlSHImXzDPsNdTAwhtYyD7Ajac4mtEpmNv4RYVQhjdfP-rJOf0m3ERbWA3Rkkd6chMrEDqFxFO9TEiiBGQ_SUAov00YI3Dbk_3nzKglYR3bXTTNkAj4FB4lq2xzE8c-3KysRAFbWwv_DGFDgt2Kp1nYuyzJhgPMluM3PB7LLtlwqjgWkAyXMAm-E-H8MLz5yHSXAbdOOfSxSYQPszLCiSOuisTJNqwCy9ReH4QINmXbZrgBPCAcTmaJK-kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسئول ارشد سابق در پنتاگون و مدیر ارشد در مرکز اسکروفت در مورد ذخایر تسلیحاتی ایالات متحده:  «محاسبات مربوط به مهمات برای ایالات متحده بسیار جدی است،» او گفت. «با هر عملیات هوایی علیه اهداف ایرانی و حملات تلافی‌جویانه بعدی ایران، ایالات متحده توانایی‌های حیاتی…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19822" target="_blank">📅 01:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19821">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الی کوهن، وزیر انرژی اسرائیل، درباره ایران:
به نظر من، از دیدگاه ما، بهتر است هیچ توافقی وجود نداشته باشد. ما می‌توانیم به اعمال فشار بر ایران ادامه دهیم.
و من به شما می‌گویم که، با کمک خدا، در دو یا سه سال آینده، رژیم ایران سقوط خواهد کرد.
به یاد داشته باشید که این ماجرا از کجا شروع شد—ما اطمینان حاصل کردیم که تمام بذرهایی را بکاریم که منجر به سقوط این رژیم خواهد شد.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19821" target="_blank">📅 00:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19820">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آتش توپخانه‌ای نیروهای دفاعی اسرائیل علیه ارتفاعات علی‌الطاهر، لبنان.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19820" target="_blank">📅 00:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19819">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزیر خارجه ترکیه، هاکان فیدان، درباره روسیه و اوکراین:  وقتی جنگ فرسایشی در جبهه به فرسایش در پشت خطوط جبهه تبدیل می‌شود، مسئله به این تبدیل می‌شود که آیا به عنوان یک ملت ادامه خواهید داد یا خیر. شما از هر آخرین راه حلی که در اختیار دارید استفاده می‌کنید.…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19819" target="_blank">📅 22:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19818">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اول فکر کردم گوشی را وارونه گرفته ام تا اینکه خانه ها را دیدم!  بوی سلاح هسته ای می آید!</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19818" target="_blank">📅 22:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19817">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT8kTFCUpThH-4sWwOT-BRnd4qSGDHRh35u7brECFaIuBh6GIMxOh1pkkHEbWVdhVflS5oa58t03OYRilotaS4DkzD7OKzL5kgpCCHRzhUrhDmQdxowtBHO2YyKDB76DeaZgajMrVs6DJDl-mHLC4pTBwCdZuMiIUzrwqT5RymQIUkyYj7_2f9OIDnFPotZtpZeY0ueRSa2o1r9aBISoAjy8wfwJcjwdhBDRU4NkLfr6Pu1HRyTBLl7P9iyXJimUIaP0Hv7J3MH4r_JTnXqsma_8zNk1QMKcxR6NHBbEB12cNF4NedqjpI10QcnKHSCRx3mwAYPzLDsYlyoJ3akwWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19817" target="_blank">📅 22:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19816">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سه کله پوک معلوم نیست چی امضا کرده اند که جرات نمیکنند علنی اش کنند.  ترکیه بخواهد در جنگی ضد هند هسته ای شرکت کند، بند ۵ ناتو عملا برایش کار نخواهد کرد و فقط موشک هسته ای خواهدخورد.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19816" target="_blank">📅 21:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19815">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حاجی‌دلیگانی، نماینده مجلس:
قدرت چهارم جهانیم و حق وتو می‌خواهیم</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19815" target="_blank">📅 21:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19814">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کانال ۱۳ اسرائیل:  اسرائیل در حال آماده‌سازی برای حمله به ایران به تنهایی است   نیروهای دفاعی اسرائیل برنامه‌های خود برای اقدام مستقل را حفظ کرده‌اند در حالی که واشنگتن به سمت خروج دیپلماتیک از جنگ پیش می‌رود.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19814" target="_blank">📅 21:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19813">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانال ۱۳ اسرائیل:
اسرائیل در حال آماده‌سازی برای حمله به ایران به تنهایی است
نیروهای دفاعی اسرائیل برنامه‌های خود برای اقدام مستقل را حفظ کرده‌اند در حالی که واشنگتن به سمت خروج دیپلماتیک از جنگ پیش می‌رود.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19813" target="_blank">📅 21:10 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
