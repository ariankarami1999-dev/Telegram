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
<img src="https://cdn4.telesco.pe/file/HooLQcLYjmNx5CmPU2viVWqINLNyrs6N0rNwQrd3-HDtjDXdEjm06scFSNx_hN_Tm8nuDS3lmoaenYj9rSkZwEeGUChopi0By_wjGs84G-8MG_F9C_5f4j1nwF-xyKiyC55eIcKWWZUT8twKqCNGqmCj1bdS0OvFLhdwlv9Rqkyz0xVPEcjV9wAfUbLoKig_6TxDB_k666nF9qFgobYCp_AExka5ezRXc4oJFeRUdKs2v5zTBUcQk2qNRuDufnxrQeRpveDCoxSCHj0jSiUgZrF3XWLSPNUJ8P9WuBfSWGse48e3GIdCGOV_FxSRGaC5IP5d6TIhn-1mzmeroZWUBQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.96K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 17:54:52</div>
<hr>

<div class="tg-post" id="msg-17001">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔻
برخی شنیده ها حاکی از تلاش گروهی از نمایندگان مجلس برای استیضاح وزیر ارتباطات به جرم اجرای دستور رئیس جمهور و بازگشایی اینترنت می باشد</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/17001" target="_blank">📅 14:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17000">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">📡
اینترنت پاکستان ، به دلیل اعتراضات مردم علیه حکومت ، در آستانه خاموشی قرار دارد</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/17000" target="_blank">📅 13:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16999">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✈️
پاول دوروف ؛ مالک تلگرام
:
فیلترینگ و محدودیت‌های اینترنتی، روسیه را به «حاکمیت دیجیتال» نزدیک‌تر نکرده، بلکه از آن دورتر کرده است.
به گفته دوروف، متخصصانی که می‌توانستند در روسیه سیستم‌عامل موبایل بسازند، به‌دلیل وضعیت خراب اینترنت، در حال ترک کشور هستند
او تأکید کرد تا زمانی که گوشی‌ها بر پایه سیستم‌عامل‌های آمریکایی مثل iOS و Android کار می‌کنند، حتی اپلیکیشن‌های «ملی» هم در برابر نظارت و سانسور از طریق بک‌دورها و فروشگاه‌های اپلیکیشن آسیب‌پذیر می‌مانند
دوروف این سیاست را «تغییر بسته‌بندی بدون تغییر اصل ماجرا» توصیف کرد و کنایه زد: مسئولی که به نام حاکمیت دیجیتال، اینترنت روسیه را خراب کرده و کشور را دهه‌ها عقب برده، شایسته دریافت مدال امنیت ملی از آمریکاست</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SBoxxx/16999" target="_blank">📅 12:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16998">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRpiGv14YyzLBCHc4pUFO-e6YtJ1k48TWZ2qYAl9dOjIFixvhfG1wvfAi8MkLEOE6Khtb2OBnbDIlmo8Q_j7uYJf92ZNK7YqecckTz7501xk31THPudI87NKlExeMebAiF-GilyPgEbDNivRj_dim7QMA-NRb4QEmo_1n7pKHH4kQmWTUj45l2ZZ6_5fPEtKS-OC0tNc2JheAcs9-sNrx48TFVxC3QjKlvXcoDpsZFoQX021tg7J90xE2Bs8Y4bwVKXiate11pvCguxx4XBCivaHPexSWlx1jwGn4cBZvmsdmk5hNtUadgr4uGvtxLlzKkSK0QDjTt1aApoGwc1N5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
اینترنت پاکستان ، به دلیل اعتراضات مردم علیه حکومت ، در آستانه خاموشی قرار دارد</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/16998" target="_blank">📅 12:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16997">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">این یعنی نه ایران و نه روسیه از این جهش بهای نفت حداکثر استفاده را نبرده اند؛ ما به دلیل محاصره دریایی آمریکا صادراتمان افت کرده (پست ریپلای شده را ببینید) و روسها هم به دلیل حملات سنگین پهپادی اوکراین.  عربها هم که عمدتاً ضربه دیده اند و لذا بزرگترین منفعت…</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/16997" target="_blank">📅 11:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16996">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ارتش لبنان اعلام کرده است که چندین نفر از پرسنل نظامی، از جمله یک افسر، در حمله هوایی اسرائیل که یک خودروی نظامی را در جاده الخالدیه–نبطیه هدف قرار داد، کشته شدند.  بر اساس گزارش‌های رسانه‌های لبنانی، این افسر دارای درجه سرتیپ بود.</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/16996" target="_blank">📅 11:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16995">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ارتش لبنان اعلام کرده است که چندین نفر از پرسنل نظامی، از جمله یک افسر، در حمله هوایی اسرائیل که یک خودروی نظامی را در جاده الخالدیه–نبطیه هدف قرار داد، کشته شدند.
بر اساس گزارش‌های رسانه‌های لبنانی، این افسر دارای درجه سرتیپ بود.</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/16995" target="_blank">📅 11:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16994">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دقت کنید که سنتکام می‌گوید که دوباره «سایتهای راداری نظارتی ساحلی ایرانی» را در گروک و قشم زده اند!  پیشتر اشاره شد چرا مهم است.</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/16994" target="_blank">📅 09:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16993">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فرماندهی سنتکام:   چند لحظه پیش، نیروهای مرکز فرماندهی مرکزی چهار پهپاد تهاجمی انتحاری  ایرانی که به سمت تنگه هرمز پرتاب شده بودند را سرنگون کردند.   پهپادهای ‌تهاجمی تهدیدی فوری برای ترافیک دریایی منطقه ایجاد کرده بودند. نیروهای آمریکایی پس از آن به سایت‌های…</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/16993" target="_blank">📅 09:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16992">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فرماندهی سنتکام:
چند لحظه پیش، نیروهای مرکز فرماندهی مرکزی چهار پهپاد تهاجمی انتحاری  ایرانی که به سمت تنگه هرمز پرتاب شده بودند را سرنگون کردند.
پهپادهای ‌تهاجمی تهدیدی فوری برای ترافیک دریایی منطقه ایجاد کرده بودند. نیروهای آمریکایی پس از آن به سایت‌های راداری نظارتی ساحلی ایرانی در گروک و در جزیره قشم برای دفاع در برابر حملات بیشتر حمله کردند.
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ به تهاجم بی‌دلیل ایران در چارچوب دفاع از خود آماده‌اند.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/16992" target="_blank">📅 02:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16991">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqxA1_2ly_P5UZ9c1luX-4vHRHvB9AFjvygSKeRvqP05YapST4Lo93DBfrUVwtGXp4RWs9dqYkmPnmsN5iWQl_5p1HWoShp00iK3lUjPArs-9c3k-7uuzMNb0ZMbC9AmbXe6mojqx7JCt-yljyF5yduTXPa_KJc7wbPzu-bvEbifqCO55ckqZUztXp1G1crEGZ-JARVeTp4rD1zSkJsojrChMz8QCfAJbAyZGRHYU6AS9flD6OdFc8MoLSKIRf-7Z0cvHlIgPwSg3v1D47BxD8JuWvicyMsMielBK22zudvYM3yFcr4B7Zg3aj_KgLonBIDgZT3OcIZO26jaj8z00Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضرات مداوماً از جهش تورم در آمریکا سخن میگویند و آن را سند موفقیت خود میزنند!
این هم تورم مواد غذایی در کشور خودمان!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/16991" target="_blank">📅 00:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16990">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فوری | ترامپ: در مدیریت پرونده ایران موفقیت بزرگی کسب خواهم کرد</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/16990" target="_blank">📅 23:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16989">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فوری | آکسیوس، به نقل از منابع: واشنگتن منتظر پاسخ رسمی ایران است و اختلافات باقی مانده را نسبتاً محدود توصیف می‌کند.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/16989" target="_blank">📅 22:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16988">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فوری | آکسیوس، به نقل از منابع: واشنگتن منتظر پاسخ رسمی ایران است و اختلافات باقی مانده را نسبتاً محدود توصیف می‌کند.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/16988" target="_blank">📅 22:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16987">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فوری | اکسیوس، به نقل از دو منبع: اختلافی بین واشنگتن و تهران بر سر اندازه و زمان‌بندی آزادسازی وجوه مسدود شده.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/16987" target="_blank">📅 22:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16985">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
محسن رضایی در گفت‌وگو با سی‌ان‌ان:
🔹
اگر ترامپ مذاکرات را جدی بگیرد، ۲۴ میلیارد دلار برای آمریکا مبلغ زیادی نیست.
🔹
اگر او می‌خواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتمادی است که ایران می‌خواهد به طرف مقابل داشته باشد.
🔹
این آزمونی…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/16985" target="_blank">📅 21:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16984">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
محسن رضایی در گفت‌وگو با سی‌ان‌ان:
🔹
اگر ترامپ مذاکرات را جدی بگیرد، ۲۴ میلیارد دلار برای آمریکا مبلغ زیادی نیست.
🔹
اگر او می‌خواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتمادی است که ایران می‌خواهد به طرف مقابل داشته باشد.
🔹
این آزمونی است که آمریکا باید از آن عبور کند و راه باز خواهد بود. این پول ماست، نه پول آمریکا.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/16984" target="_blank">📅 21:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16983">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دستیار ایرانی به سی‌ان‌ان گفت دیدار خامنه‌ای با ترامپ رخ نخواهد داد</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/16983" target="_blank">📅 19:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16982">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رضایی ایران هشدار داد که اگر آمریکا درگیری را از سر بگیرد، ایران «جنگ را» فراتر از خلیج فارس خواهد کشاند -</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/16982" target="_blank">📅 19:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16981">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کاخ سفید:  دیدار عراقچی- ویتکاف  گفت‌وگوی مستقیم ویتکاف و عراقچی در مسقط    «استیون ویتکاف، فرستاده ویژه ریاست‌جمهوری آمریکا، به همراه آن اسکاروگیما، سفیر آمریکا در عمان، امروز در مسقط با دکتر عباس عراقچی، وزیر امور خارجه ایران، گفت‌وگوهایی انجام دادند؛ این…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/16981" target="_blank">📅 18:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16980">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گروسی:   ایران و آمریکا به توافق نزدیک شده‌اند</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/16980" target="_blank">📅 18:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16979">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گروسی:
ایران و آمریکا به توافق نزدیک شده‌اند</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/16979" target="_blank">📅 17:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16978">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ایران دارای یکی از بزرگترین ناوگان های نفتکش دنیا بود اما با این وضعیتی که پیش می رود باید از شوتی های زحمتکش مرزهای شرقی و جنوب شرقی کشور برای انتقال نفت بهره ببریم!</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/16978" target="_blank">📅 16:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16977">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">Yinon_Plan.pdf</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/16977" target="_blank">📅 14:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16976">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">امیرحسین ثابتی:   آمریکا بعداز جام جهانی سنگین‌تر به ایران حمله خواهد کرد  ایران را تبدیل به غزه دوم خواهند کرد.  باید پیش‌دستانه پتروشیمی‌ها و زیرساخت‌های منطقه را بزنیم.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/16976" target="_blank">📅 13:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16975">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ایران_جنگ_را_برنده_نشد،_بلکه_چیز_خطرناک‌تری_را_به_دست_آورد.pdf</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/16975" target="_blank">📅 13:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16974">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBVW6R9a-U9QQSxbwx3N3YiAelU6YUK2lzwj2hQn9b8l8kYEQlf2KYxXb6oPzKS3AtVCMtV6m9hm4swHKqKWtp8J1yR0MBOQVtTGd2EyIuiYFClvsLSJ66K-kKKzsWQ6z1hoT4axLO8z-Pu2mSONEpEsIspsH86afgCSVQYL4nIbrRRPJgUUq8yYdF0qp96FakBa5WXgRqajHyECnf0JVFRFyj6wFYSNJHyhr_czYwdhoU5sWyPbNkMrWQ4NqGkALPkoC0yBPgev1dhxmWxie4Y_kz3dg3QFlPPv0kSFwrsKnwSf5CrkxuUm2-8GGNLjXP_J4qtJq8U_IUA6RlsUMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدرسگ ها چه اسم هایی برای بندرشان گذاشته اند!  بعد انتظار دارند حمله نکنیم!</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/16974" target="_blank">📅 13:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16973">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">عمان پس از انفجار در بندر فهل، بارگیری نفت را متوقف کرد  سلطنت عمان بارگیری نفت در پایانه بندر فهل در خلیج عمان را به طور موقت متوقف کرده است. به گزارش رویترز، دلیل این امر انفجار در منطقه بندر است.  بندر فهل یک نقطه صادرات اصلی نفت خام عمان است. اختلالات…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/16973" target="_blank">📅 13:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16972">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دقت کرده اید هر کسی میانجی این جنگ بی پایان ما با آمریکا و اسرائیل شد به خاک رفت؟!  راند اول قطر میانجی شد و همان روز ایران به قطر حمله کرد و چند ماه بعدش اسرائیل هم به قطر حمله کرد و در جنگ اخیر هم با حمله موشکی وحشتناک ایران به تاسیسات گازی راس الفان، بیشترین…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/16972" target="_blank">📅 13:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16970">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bnwHxLsAjtY5lPkYnwVrB7_TyI0c1hmkIZvJSCSkGDhXqJHP_0KLf5az2T9dSdNLGaKDssdwjqOUAo4MPQ35y4_w5Zi8Ltaf6F_hzpoCr6PO1QC8cyMgBG3OEo7wgimLwL-QXGCImsPnd8bzvj48Z0VpwTC6zxYZNcHuUBTHftC-DnseEs2N5Zrw6cHUfFmpxUmagHqG7ejNtxZRu8MJy0LOjG93f3aE-UPh4u03QgDTJ9SJrB9pD-Nf1v5N5_zbMFoHbRyJbSKSo6vwrpCyLUJAF1itvA9ojK84TW-iMXsLQptUSoFvcJS0O5019mWVKiqiUfjvzrD2L-lxDM_j_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXx-uYP0u0OMb2DA1t7uBeKA_1XeTtJ_yw3qqDKtOWTJUC661oYGtb1RFf7O2fpDHOvJXAmZ1agP3VBZ9vRVRiMe6WmKOtWM-hUtdKFOSfJfy98wMeQmcO9_CflM6Lq5Pxqj_vtm1fXYg7Ynl1KqaAhSFcvogvcQoTrRUn8b3eCL4eUex_du3ZVnY_y5tTBXgw87bv7KNv05kpbVRULeOtghM2VHYF6AWScECbK7maD3NLTmZyuq6NzP2bdgRroQsNu2WDyw95q-RNtxhclcN0-3ABimaEXHVkRnvua-tpjTRw_GDeRo6jzaME36mSAUb5xJTB0zx_FMUBNY5cv7rA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم با خر یوگا میکردید بهتر بود ولی خب</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/16970" target="_blank">📅 12:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16969">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اکنون ثابت شده که باکو میزبان گروه های تکاوری و جاسوسی اسرائیل در حین جنگ بوده اند، منتهی دولت پوزیده صرفاً به استمالت از آنها ادامه داده و حتی یک موشک و پهپاد به تاسیسات آنها برخورد نکرده است.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/16969" target="_blank">📅 11:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16968">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این پوزیشن را دیروز به همراهان پیشنهاد دادم.  کماکان بر این باورم که خریدها سبک باشد و کسانی که سنگین کریپتو دارند این فرصت خروجشان است.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/16968" target="_blank">📅 11:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16967">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBUUXOfTVRLUngp9ZeYubYvaZpr8zwJy466CqByO9arV-GLAPa2x8730mYT28Y0X-3fwiWqsWlVGjn0tbpVofxw4puuMXZn65_F_ULYdbWxdc6J_B2Ylh5WqWR4ZiiYRAP8Cpab0fz6B94ogGiiZJK_PohsqsnlegBcZdVsVYF7mJ7kOzPYVvQE4_buOZYmPtemEYotLQkQ_23d4NmS5DpVrajN1VqkGYbWJ5b_9nHSRikTCRJ9krJLafmDRn-T3TPUdZqE5l-Ozh9OE53VFNDsTmWUnn2lAEMGC-jLkKGXo9sVuiJJAy1nhWrqEFz7MLm4URFvNnNo_Yuy31SKnSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری باکو بین ۵۰ تا ۶۰ درصد از نفت اسراییل را تامین می‌کند و میزبان بسیاری شرکت‌های نظامی و امنیتی اسراییل هم هست اما تا کنون از ضرب حملات موشکی و پهپادی سپاه به دور مانده است.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/16967" target="_blank">📅 11:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16966">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ایران_جنگ_را_برنده_نشد،_بلکه_چیز_خطرناک‌تری_را_به_دست_آورد.pdf</div>
  <div class="tg-doc-extra">232.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/16966" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این‌گونه_دکترین_نتانیاهو_برای_ایران_فروپاشید.pdf</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/16966" target="_blank">📅 11:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16965">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دورویی اروپا در قبال اسرائیل: محکومیت‌های کلامی و خریدهای میلیاردی سلاح
اروپا این روزها در قبال اسرائیل دو چهره متفاوت به نمایش می‌گذارد: چهره‌ای سیاسی که با محکومیت‌های پرسر و صدا و قطعنامه‌های نمادین، خود را مدافع اخلاق و حقوق بشر معرفی می‌کند، و چهره‌ای نظامی که در سکوت، میلیاردها دلار سلاح از همان کشور می‌خرد. سیاستمداران اروپایی با برگزاری کنفرانس‌های مطبوعاتی و رای دادن به تحریم‌های نمادین، سعی دارند تصویر یک قاره متعهد به ارزش‌های انسانی را به نمایش بگذارند، اما در پشت پرده، ژنرال‌ها و مسئولان نظامی با امضای قراردادها، واقعیت دیگری را رقم می‌زنند.
در ۲۶ مه ۲۰۲۶، شرکت البیت سیستمز اسرائیل اعلام کرد که سفارشات معوقه‌اش برای اولین بار از ۳۰ میلیارد دلار فراتر رفته است؛ رقمی که حتی پنج سال پیش هم غیرقابل تصور بود. در میان این اعلامیه، قراردادی ۱.۴ میلیارد دلاری با یک کشور اروپایی ناشناس برای مدرن‌سازی نظامی در حوزه‌های زمینی، هوایی و جنگ الکترونیک به چشم می‌خورد.. این در حالی است که کشورهای اروپایی با صدای بلند، صادرات سلاح به اسرائیل را متوقف کرده‌اند، تحریم‌های جزئی را مطرح می‌کنند و شرکت‌های اسرائیلی را از نمایشگاه‌های دفاعی اخراج می‌کنند.
اسپانیا صادرات سلاح به اسرائیل را متوقف کرد، چند کشور عضو ناتو تحریم‌هایی را پیشنهاد دادند و البیت سیستمز پس از اعتراضات از نمایشگاه یوروناوال فرانسه اخراج شد. اما در عمل، همین کشورها در سکوت، به خرید سلاح از اسرائیل ادامه می‌دهند.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/16965" target="_blank">📅 10:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16964">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOaGFwo02ik4LECgIWxaLbGfiCUrytaDwpgTBqufcxDc6c8tJ3sgsAxF6sx_70texRY52m1PrOh3bZy5QNYtn3B0bNIsdXkn-iAMJPp-DZ7eI3zIkbNB1tQW_wb2Gqn9hSTT4sacX-GaOreayAXdhsmLFUj-UEebZ4e1-pGb8VDwK-hf2odmUo-q2Vv0QPUjmHd69MjZwSPwxFwT_fnrmOxE91fRq--aenAfrxbylvC1l6JX4bnjVzUwsNLTzC2NG-I8bIjPQt3Z7gL_1hXI9r7vaYxRjjhNDRRnEuz2zFS5i1OeOlfAVhkBMJKl16UxziTFLuy7DBZI0tKpgi_sIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشتر گفته بودم که یکی از انگیزه های اسراییل از تعقیب پروژه تغییر رژیم در ایران ایجاد یک کریدور داوود بزرگ است که او را از امتداد آویزان بودن به آمریکا برای تامین امنیت ملی اش بی نیاز کند.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/16964" target="_blank">📅 10:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16963">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">به گزارش بلومبرگ، بریتانیا و فرانسه تقریباً طرحی را برای اجرای عملیات مین‌روبی در تنگه هرمز، پس از توافق احتمالی بین آمریکا و ایران بر سر آتش‌بس دائمی، نهایی کرده‌اند.
این طرح یک تلاش چندملیتی خواهد بود و پس از بیش از یک ماه نشست‌های چندجانبه به رهبری دو کشور انجام می‌شود.
به گفته افراد مطلع از این طرح، این عملیات شامل ۱۵ کشور خواهد بود که پرسنل نظامی و تجهیزات خود را به مأموریت اختصاص می‌دهند و برای جلوگیری از درگیری، ارتباط مستقیم با ایران حفظ خواهد کرد</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/16963" target="_blank">📅 09:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16962">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خواننده Secret Box از یک سال پیش آگاه بود که دلیل زدن هوانیروز و پایگاه ها و پاسگاه های مرزی ارتش و سپاه در مرزهای غربی، گشودن فضا برای ورود نیروهای مسلح کرد به داخل کشور بود.  اما چرا این طرح آن گونه که باید و شاید عملیاتی نشد؟!  بخوانید:   موساد سلاح‌های…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/16962" target="_blank">📅 00:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16961">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بشدت به همین سناریو که 2 ساعت پس از آغاز جنگ اشاره کردم، ایمان آورده ام. تقریباً تردیدی برایم نمانده که مدل «فروغ جاویدان» صدام را این بار نتانیاهو با پژاک و گروههای مشابه ش میخواهد اجرا کند.  نکته بدتر اینکه در صورت موفقیت این طرح و با ورود نیروهای شبه نظامی…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/16961" target="_blank">📅 00:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16960">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">محسن رضایی:
امیر قطر و ولیعهد عربستان دارند خودشان را با واقعیات تنظیم می‌کنند اما امارات، بحرین و کویت همچنان فکر می‌کنند قدرت آمریکا مثل قبل خواهد بود. این‌ها فکر نکنند که اگر این روش را ادامه دهند ما بعد از جنگ رهایشان خواهیم کرد. اگر امارات و کویت با صهیونیست‌ها همراه هستند باید ابوظبی و بوبیان را به عربستان و عراق بدهند!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/16960" target="_blank">📅 00:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16959">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vK6vzLffPjdVkEf0vT7IJnelySH1yuVY8jw9A2uk6Dy293HJcgXN398Ez4sYcUYBfvGhUmwbovjZxTdwXUne6O3DG_66bywq6plS616yjRxN5_18qcml8M7EqQDB1sBCY_h_OReqpfN32VLviJ-N71H6n2by9RiUT1F8r78_eKbr6zhfU_6iZfbp2n2hqH2HRqrlxNcH4m77-nhYUg5whLMNldYqy2nFJw8fBH2tuTCfji9Izmd1wOY2sxjPj-Koxhr9qYocKbylA8L3hud6sObYb6Phr_-wj_l3_u8WDUemYVb57tD_pe5Yh3capWsGchbIFseR8TmwM-yFl3l10g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یعنی نه ایران و نه روسیه از این جهش بهای نفت حداکثر استفاده را نبرده اند؛ ما به دلیل محاصره دریایی آمریکا صادراتمان افت کرده (پست ریپلای شده را ببینید) و روسها هم به دلیل حملات سنگین پهپادی اوکراین.  عربها هم که عمدتاً ضربه دیده اند و لذا بزرگترین منفعت…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/16959" target="_blank">📅 21:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16958">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ایران و روسیه یک تفاهم‌نامه همکاری به ارزش ۲۵ میلیارد دلار در بخش هسته‌ای امضا کردند - تسنیم نیوز</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/16958" target="_blank">📅 20:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16957">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رویترز:   روسیه برای اولین بار اذعان کرد که تولید نفت این کشور در سال جاری کاهش یافته    این اعتراف در زمانی مطرح می‌شود که اوکراین در ماه‌های اخیر حملات پهپادی و موشکی خود را به تأسیسات انرژی روسیه تشدید کرده . آژانس بین‌المللی انرژی تخمین زده که تولید نفت…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/16957" target="_blank">📅 20:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16956">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">صنعت نفت ایران در سال ۲۰۲۶ با یکی از شدیدترین فشارهای صادراتی خود در سال‌های اخیر روبه‌رو شده است. داده‌های منتشرشده توسط شرکت ردیابی نفتکش Kpler و منابع تخصصی بازار انرژی نشان می‌دهد که از زمان آغاز درگیری‌ها و تشدید محدودیت‌های دریایی در اواخر فوریه، توانایی…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/16956" target="_blank">📅 20:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16955">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIvoPfBLbXbW-ELFRztlSlsk9hc6TruASyt7SDMPaNGnjvhimgz9RekNroJ4kDTkrtvwL1hmje1BhWjDQq82XWzD8QKhJpjGyttPLrSErUBdjDgLNx4khnsx8GYr478AK3XvclDVktxGXmCvaBfPIEib5KMcX0d1X8d6sAM_eEgTG3XlZHPihYYM9g1defSvZZ5U6KN_WJN75j-YEpkpBvEZjZN7_TZV5rI0RN59ICTHMoWIPjRm1QkOV2Do_cz6df2qt9JjE2ita_GZNkM7F8QOBuwI5w6capu4-azPBsucqPxQa4W-Nhtqpnzc3xSVuQPx6QGyoTke6en1fIeQ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:   در حال حاضر، ما کنترل کامل ۶۰ درصد از نوار غزه را در دست داریم و دستور من رسیدن به ۷۰ درصد است... ابتدا ۷۰ درصد. از همان شروع می‌کنیم</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/16955" target="_blank">📅 19:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16954">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حالا اینجا همه حضرات میگفتند ترامپ دست خالی از چین برگشت!</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/16954" target="_blank">📅 19:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16953">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔥
ثمره دیدار ترامپ و شی/ سپر چینی جلوی جهش قیمت نفت را گرفت
🔹
فایننشال تایمز نوشت که کاهش ۴ الی ۶ میلیون بشکه‌ای واردات نفت چین و استفاده این کشور از ذخایر نفت خود، منجر به کاهش تقاضا در بازار نفت و کاهش قیمت شده.
🔹
خاویر بلاس خبرنگار بلومبرگ می‌نویسد که…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/16953" target="_blank">📅 18:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16952">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCzS3QdGQUD4AhJx3nKOCaSPpulnmBIL3-PZ6rOFhpDtF1URfZqOhfVALqmvVpnODRiTKT-4aNXscn0edr3MDykbkPF3vJXGqClH3L-uyAtmd9vvc8jd8ki2x_1OZiTwVrbZ8zh0EUSOXNMIsFLe3csLJ5ennn7BBZnM4lIJ7BFJSCFFzuqqJ1kLuz6yycDHdu8T3-gjP8TEceErYaL7M2AgcUi8rRLBmq_XrWbYnjh1Tz_AhHCU9hh-tWnYuZkFJaHl6eMypRWXeCmn8E80fTvFaf0G8nihSzR4Jh2rxmBOKXCV-Bf-w3CkZTccRnfelB1Q9rOEznZdiaRW5F-bRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/16952" target="_blank">📅 18:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16951">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAYgW6kmQzuu1SOSY1mNZNguIIZ36Q-TKylTmJ6E0m51kMFFS4S-0cHZvE3ypQmsk93072IgugAP_HWiDOBQ_RLD44bE4nSDZ4PPBoIaKYgrybJC4XY8EzFLkxjgGUZau8DpsmFtOVVrL47RurWslMY2lD2bT4K7mlaP2D0euzcxNrGIG7F6xXOSYqEZxZ8PQKtBEAIkxbsCaniK9QGKIgZk47f05Kr_TzIgOw56I5717l_-JIJMjYkyMGnny8n9A9w_6VjwIMEPX5XugSJ8z5WDmZqUFSFSx7d7LOiMpZUeYAszaMTp3S1Yy1W5im6ejv7b8TWhHu31NpFp8H8nZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/16951" target="_blank">📅 17:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16950">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی (IAEA) اعلام کرد که نتوانسته به تأسیسات هسته‌ای ایران (به جز بوشهر) برای انجام فعالیت‌های راستی‌آزمایی میدانی دسترسی پیدا کند.
این موضوع نگرانی‌ها درباره خطرات اشاعه هسته‌ای را افزایش داده است.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/16950" target="_blank">📅 17:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16949">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سپاه پاسداران:
شرط اولیه ما برای پذیرش آتش بس در جنگ منطقه‌ای، آتش بس در تمامی جبهه‌ها از جمله لبنان بوده است.
دشمن می‌بایست با فوریت حملات خود به مردم لبنان را متوقف کند، و سریعاً با تخلیه سرزمین‌های اشغال شده لبنان به پشت مرزهای بین المللی عقب نشینی نماید و تمامیت ارضی لبنان را به رسمیت بشناسد.
هیچ آرامشی در منطقه بدون عقب‌نشینی صهیونیست‌ها از مناطق اشغالی لبنان برقرار نخواهد شد
همه ما با تمام وجود از ملت لبنان حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/16949" target="_blank">📅 17:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16948">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPZbdMpDj-6m7kakod1gCbhmjL3LHgMblEDZApOTIekjN4LqqKIKqgUO8xnJZdPvbZaziT5udzF4s8ExOjDnkvO-Vtl7sD7mkguX0FkGu03bj-GnklsRmGIvlMAWJ7D91gYYLJ_nMFIIDjB4FA22anZgTCN4ckYJg4UDA-KLjnsYUc_pi8PU5nzT3AsNWr4_6WhiDX0Pvdc94Q2HW_R15XoTfHkStsgXUs2TzSOsYkr7kZv60NFEJrN92vBunWO5wmzI8m1phy_TJSNZcwHMnv7AUoyREk4IxUo9xps1bikrmFXP1alWmjvm-Aaw79HrGtQAP46rgZnQuW9l5-F08A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:
تصویر روی جلد این هفته: «نسل جدیدی از سوسیالیست‌ها قصد دارند اقتصاد را با کنترل قیمت‌ها، مالیات‌های سنگین بر ثروت و موجی از ملی‌سازی‌ها دگرگون کنند.
این جریان که با خشم ناشی از غزه تقویت شده، با سرعتی چشمگیر در حال جذب رأی‌دهندگان است.»</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/16948" target="_blank">📅 16:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16947">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce28a3a45.mp4?token=INNEei8I9hcIokHFy0idX_h0JFJubF4gdIV6Ee660I5wx7qLQfgLQleNU6eZELckEsCgQFxBol6xqf1mrLlvmMuzhSPiP5yCji0bkIgeeN-6DLiGwIx7FRPClyimx4jszmROrPvZZdN8kV27Q4aUbWupkKtrzZU7LdKFl6F6QtkXUoZn9pGt7MEXUGAzPkm9eIOKNZ4m-wVWHqIQUxVf0bxlCf8ROJi8P5_9RHM9r9bcUJI5nPlEVS4dmntLBLSlyZxLFqaIiVOkKz4OJqzEQe2I9RN_1pZ-Vmm-WmgJJqbiqNs0CUoaHk32CDX7SD8NcV14CVQzzsiLRUgw2v6t3Kx7QMRyPKeKfpgRDhP9LQJtx4UqOa0GMYowIfMGqmcIhQ3xnH5K5HzlG1fFveeg13ynMi9KWeML2wdwyyXY3UmUDjMpq_raf4wGH2LB9_GbxzD4KX4lfpTufP5qpf_MJTv8VMZH9vR3E-RFXQUriAslFbMsIdxVOZMMF5kehO3y-6I8BjCkHzDCs0KKNoFjYpFF8zvRjcIDexZnfWszOMvBJNvc2kFinNnjIE2ohQY8y_R_acUD9cNwCVfu1THja0N3nLCwAe_1aSsQiBgVZBZ4uXUC_q2FY7c5qylaBfP5AYSt9LMwKLR89rv9dMy-jZIGkLfxhrZ6Ni2S-4wQQ_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce28a3a45.mp4?token=INNEei8I9hcIokHFy0idX_h0JFJubF4gdIV6Ee660I5wx7qLQfgLQleNU6eZELckEsCgQFxBol6xqf1mrLlvmMuzhSPiP5yCji0bkIgeeN-6DLiGwIx7FRPClyimx4jszmROrPvZZdN8kV27Q4aUbWupkKtrzZU7LdKFl6F6QtkXUoZn9pGt7MEXUGAzPkm9eIOKNZ4m-wVWHqIQUxVf0bxlCf8ROJi8P5_9RHM9r9bcUJI5nPlEVS4dmntLBLSlyZxLFqaIiVOkKz4OJqzEQe2I9RN_1pZ-Vmm-WmgJJqbiqNs0CUoaHk32CDX7SD8NcV14CVQzzsiLRUgw2v6t3Kx7QMRyPKeKfpgRDhP9LQJtx4UqOa0GMYowIfMGqmcIhQ3xnH5K5HzlG1fFveeg13ynMi9KWeML2wdwyyXY3UmUDjMpq_raf4wGH2LB9_GbxzD4KX4lfpTufP5qpf_MJTv8VMZH9vR3E-RFXQUriAslFbMsIdxVOZMMF5kehO3y-6I8BjCkHzDCs0KKNoFjYpFF8zvRjcIDexZnfWszOMvBJNvc2kFinNnjIE2ohQY8y_R_acUD9cNwCVfu1THja0N3nLCwAe_1aSsQiBgVZBZ4uXUC_q2FY7c5qylaBfP5AYSt9LMwKLR89rv9dMy-jZIGkLfxhrZ6Ni2S-4wQQ_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗
رهبر حزب‌الله نتیجه مذاکرات مستقیم لبنان-اسرائیل را رد کرد!</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/16947" target="_blank">📅 15:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16946">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انصافاً ترامپ خدایگان دروغ، دغل بازی، فریب و سخنوری است.
زاده خرداد است و ...
(امیررضا هم زاده خرداد است و میدانم این یعنی چه)
سبحان الله!</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/16946" target="_blank">📅 15:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16945">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gX1224pCitoDx5OE_wKFmP5JWCm4AaqYHTXjPCWCpSDNjosM1Qkf4YeD95ifY04611uVVM7dyJcDzEMGt1YWBVHS1YfbsFd2sWnLpTRCMn4EnL83X59kAHXqC6WsxnX40ioImIHUSvqd3bB-1qbqokucIk2Y9PnsdtiTqoJJysfa5rHTCI-Wtci1R83lC55fp44eFlcyczs90nO5ifOuSNYsU7npwmmSJPNTCBZ3EjYhIxuSc8pr3UJbhTQbjFQx5XttCN0_h7tEmKwpdTFr5CmAq6EgzjmeerPNCA9OBTpbSkZbmtLQ-CamOvdr5r3NuSGPEIFpkkHJitMZCla2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/16945" target="_blank">📅 15:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16944">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗
رهبر حزب‌الله نتیجه مذاکرات مستقیم لبنان-اسرائیل را رد کرد!</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/16944" target="_blank">📅 15:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16943">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sn0lGlTgJyv69VQFFJHtuLE_gKqj3D_cAFOVQZUgNpQ03nwSDK2Qff1WaNEy0dsnX59881hGd-EnJX1NGh6Qsg-eeEp1enBly0LRWQmbgop42COscx3S_PFPlYJpJWDBD08xFMncCjmFAS0uIpnTclOtIiw1ePDkHVUIarAgqaeWDFpfKhjuTygaauDMg-1R_BnxDdZqGQzv8ZodimRawblXXlXRKi2kXOHGs1pz0oxWDth66QZXVg8XXKNiwZd4e2ZAmfgyax_hhlsVLD_TVbb7XE39LV3vXCJCp071Mr4NJ5B-yC-AuqXTryplSGXenss03pX4Eu3s4SHpduQuhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضایی حصرشکن | حصر ترامپ رو بشکن!</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/16943" target="_blank">📅 15:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16942">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">از منظر حقوق بین‌الملل، «محاصره دریایی» یکی از شدیدترین اشکال اعمال زور میان دولت‌ها محسوب می‌شود و در صورت اجرا علیه یک کشور مستقل، به‌طور معمول در زمره اقدامات خصمانه با ماهیت نظامی قرار می‌گیرد.
بر اساس منشور ملل متحد، اصل بنیادین در روابط بین‌الملل منع توسل به زور است (ماده 2 بند 4). تنها دو استثنا برای استفاده مشروع از زور وجود دارد: دفاع مشروع در برابر حمله مسلحانه (ماده 51) و اقدام جمعی تحت مجوز شورای امنیت. بنابراین، اگر ایالات متحده یا هر دولت دیگری اقدام به محاصره دریایی بنادر ایران کند، این اقدام از منظر حقوقی صرفاً یک «اقدام اقتصادی یا فشار سیاسی» تلقی نمی‌شود، بلکه به‌طور مستقیم در چارچوب «استفاده از زور مسلحانه» قرار می‌گیرد.
در حقوق بشردوستانه بین‌المللی، به‌ویژه بر اساس قواعد عرفی و راهنمای سان‌رمـو درباره حقوق جنگ دریایی، محاصره زمانی مشروع تلقی می‌شود که در بستر یک مخاصمه مسلحانه موجود انجام شده باشد، اعلام و اطلاع‌رسانی شده باشد، و به‌صورت مؤثر اجرا گردد. به بیان دیگر، محاصره دریایی ذاتاً یک ابزار جنگی است، نه ابزار صلح.
از این رو، اگر چنین اقدامی علیه ایران در شرایط غیرمجاز حقوقی (بدون مجوز شورای امنیت یا بدون وقوع حمله مسلحانه قبلی) انجام شود، می‌تواند به‌عنوان «اقدام متخاصمانه شدید» (hostile act) تلقی شود که ظرفیت ایجاد «وضعیت مخاصمه مسلحانه بین‌المللی» را دارد. در حقوق بین‌الملل معاصر، حتی بدون اعلان رسمی جنگ، وقوع چنین سطحی از درگیری کافی است تا قواعد جنگی فعال شوند.
در نتیجه، محاصره دریایی یک کشور نه صرفاً یک ابزار فشار، بلکه از نظر حقوقی یک اقدام با ماهیت جنگی است که می‌تواند به تشدید فوری تنش و ورود طرفین به درگیری مسلحانه منجر شود، مگر آنکه تحت چارچوب‌های محدود و مشروع بین‌المللی انجام شده باشد.</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/16942" target="_blank">📅 15:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16941">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">عجب فریبی و عجب تاثیری در کاهش بهای نفت!</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/16941" target="_blank">📅 15:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16940">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0uwdieuG9dhjZU0Lrm2dVe8zNOxpvL7i78OOO032YgubG9Lxqf0JxQbJAsUA-8aUlyNwJ628dQ7m1acAmqxVI8Hn1SZp58jZhfX2YOsNZvp52V1shFXdNKam4CarbXEqn1uUQlVYdoZuQY0onFcwh0s9ls9F_MlMy3GsOLi-mtfM8MlAMT3lFsriO7kKJxfu64Okv3566LGMajTy6Stqdn-Z-o-7HwO-b3D0_0h6ysbCuL_HraMSxFowM_4VXuSJZyiE7uTZtif3-Kjwa7TMpfXVGwH_zYA8tx-ng--2kffzDtMX3OcFzvEqwPGbR-pGD57lEIygQHmyxDhk2T-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلا رفت برای این سناریو که عصر گفتیم…؟!</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/16940" target="_blank">📅 15:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16939">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ به دستیارانش گفته است که جنگ با ایران را از سر نخواهد گرفت مگر اینکه نیروهای آمریکایی کشته شوند.  — وال استریت ژورنال</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/16939" target="_blank">📅 15:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16938">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کاندولیزا رایس — وزیر امور خارجه پیشین آمریکا :
«جنگ علیه ایران جنگی محدود بوده و نتیجه آن احتمالاً قطعی نخواهد بود، اما برای ایجاد خاورمیانه‌ای بسیار بهتر کافی بوده است.»</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/16938" target="_blank">📅 12:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16937">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔹
بازداشت جمشید قمی، مدیرعامل ۶۳ ساله شرکت ایران تِک ، به اتهام تأمین تجهیزات آمریکایی برای تأسیسات هسته‌ای و نظامی ایران</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/16937" target="_blank">📅 11:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16936">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ به دستیارانش گفته است که جنگ با ایران را از سر نخواهد گرفت مگر اینکه نیروهای آمریکایی کشته شوند.
— وال استریت ژورنال</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/16936" target="_blank">📅 10:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16935">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، گفت که فشار شدیدی به ایران وارد شده و مذاکرات با ایران به خوبی پیش می‌رود. او احتمال توافق تا پایان هفته را مطرح کرد، هرچند اشاره کرد که ممکن است دو تا سه هفته دیگر نیز طول بکشد.
به گزارش فارس به نقل از یکی از اعضای تیم مذاکره‌کننده تهران، گفتگوها بین ایران و آمریکا همچنان ادامه دارد و هنوز تصمیم نهایی گرفته نشده است.
یکی از اعضای تیم رسانه‌ای هیئت مذاکره‌کننده ایران، طرحی چهار مرحله‌ای برای توافق با آمریکا ارائه کرد: ۱) پایان جنگ، ۲) اقدامات عملی در مورد تنگه، ۳) تحریم‌ها و مسائل هسته‌ای، ۴) تشکیل کمیته نظارت</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/16935" target="_blank">📅 09:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16934">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOrjx5WpzVTlSovLAdC4Ek2VFBDnIBiFDz2urqhF11aJcig-ECnIUBhGWexhV9RpDzCRk8e_nG13Ae5K2GEEp92jQN-AhUbENhvNiNIah0W6mfNkI3T3Qb-w9apS7KyNQlVXxitSh3LEkIAec2aUzE1RVLkvEGBQtqJFZY0Lvo5d9TEiXJln5c8HxFSUuogOWe5bk6CsKfb40YIEDB2ZzJmyhh1aiWe-AbQYOr3ikDXzIjc2xeH1DwIuB8fV3J60yROXnpn6Gx9fTyeItjQADMl2rAaWNF_Xv1zK3fSRCWhW1ou1gun6sBQ6cBrtWkjDm1By423xD-zTyhsDamXVlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ایران در سال ۲۰۲۶ با یکی از شدیدترین فشارهای صادراتی خود در سال‌های اخیر روبه‌رو شده است. داده‌های منتشرشده توسط شرکت ردیابی نفتکش Kpler و منابع تخصصی بازار انرژی نشان می‌دهد که از زمان آغاز درگیری‌ها و تشدید محدودیت‌های دریایی در اواخر فوریه، توانایی ایران برای رساندن نفت به بازارهای جهانی به شدت کاهش یافته است.
پیش از این تحولات، ایران روزانه حدود ۲ میلیون بشکه نفت خام، میعانات و فرآورده‌های نفتی صادر می‌کرد. اما اکنون نشانه‌های روشنی از افت صادرات و تولید مشاهده می‌شود. بر اساس آمار اوپک، تولید نفت خام ایران در آوریل ۲۰۲۶ به حدود ۲.۸۵ میلیون بشکه در روز رسیده که نسبت به سطح پیش از بحران حدود ۳۵۰ هزار بشکه در روز کاهش نشان می‌دهد. برخی برآوردها حتی افتی نزدیک به ۴۰۰ هزار بشکه در روز را گزارش کرده‌اند.
در بخش صادرات، کاهش شدیدتر است. Kpler برآورد می‌کند که بارگیری نفت در پایانه‌های صادراتی ایران به حدود ۶۴۰ هزار بشکه در روز سقوط کرده است. نشریه تخصصی MEES نیز گزارش می‌دهد که این رقم از ۱.۶۴ میلیون بشکه در روز در ماه مارس به کمتر از ۵۰۰ هزار بشکه در روز در ماه مه کاهش یافته است. همچنین از ۶ مه به بعد برای مدتی هیچ محموله‌ای از پایانه اصلی صادرات نفت ایران در جزیره خارک ثبت نشد.
با این حال، صادرات نفت ایران هنوز به طور کامل متوقف نشده است. چین همچنان روزانه بیش از یک میلیون بشکه نفت ایران دریافت می‌کند، اما بخش عمده این نفت از ذخایر شناور انباشته‌شده در آب‌های آسیا تأمین می‌شود، نه از محموله‌های تازه صادرشده از ایران. این ذخایر نیز به سرعت در حال کاهش هستند. برآورد Kpler نشان می‌دهد که حجم ذخایر شناور ایران از آغاز بحران ۳۳ میلیون بشکه کاهش یافته و به حدود ۸۹ میلیون بشکه رسیده است.
در نتیجه، مسئله اصلی دیگر صرفاً کاهش صادرات روزانه نیست، بلکه سرعت تخلیه ذخایر شناور ایران است. اگر روند فعلی ادامه یابد، تحلیلگران Kpler هشدار می‌دهند که طی ۶۰ تا ۷۰ روز آینده بخش عمده نفت در دسترس برای تحویل به چین مصرف خواهد شد و ایران ممکن است ناچار شود تولید خود را تا حدود ۱.۷ میلیون بشکه در روز، نزدیک به سطح مصرف داخلی، کاهش دهد.
چنین سناریویی می‌تواند درآمدهای نفتی کشور را به پایین‌ترین سطوح سال‌های اخیر برساند و فشار اقتصادی قابل توجهی بر ایران وارد کند.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/16934" target="_blank">📅 01:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16933">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ:
در توافق پیش‌رو، به ایران اجازه دستیابی به سلاح هسته‌ای داده نخواهد شد و پس از امضای این توافق، تنگه هرمز به سرعت بازگشایی می‌شود.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/16933" target="_blank">📅 00:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16932">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
دونالد ترامپ
:
در اون منطقه از دنیا ( خاورمیانه ) ،  آتش‌بس یعنی وقتی طرفین دارند با شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنند
﻿</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/16932" target="_blank">📅 00:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16931">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نیروی دریایی ارتش، "مرکز فرماندهی و کنترل" شرارت های ارتش آمریکا علیه کشورمان را هدف قرار داد
🔹
در پی شرارت ها علیه شناورهای تجاری ایرانی در دریای عمان و نقض مقررات تنگه هرمز از سوی ارتش متجاوز آمریکا، نیروی دریایی ارتش، مرکز "فرماندهی و کنترل " این شرارت…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/16931" target="_blank">📅 23:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16930">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خبر کوتاه بود و دلخراش: محمدرضا شهبازی مورد تجاوز قرار گرفت
😄
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/16930" target="_blank">📅 22:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16929">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صدای انفجار در بحرین</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/16929" target="_blank">📅 22:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16928">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">به نظرم دسته خوبه را داده اند به سپاه که هر وقت میزند واقعاً بازارها به هم میریزند و دسته خرابه هم به ارتش داده اند برای وقتی که نفت را Short می کنند.
(باز بپرسید شورت چیست)</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/16928" target="_blank">📅 22:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16927">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نمیدانم این حمله های ما چطوری است که تا خبرش بیرون می آید نفت میریزد و طلا بالا می رود!
سبحان الله!</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/16927" target="_blank">📅 22:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16926">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نیروی دریایی ارتش، "مرکز فرماندهی و کنترل" شرارت های ارتش آمریکا علیه کشورمان را هدف قرار داد
🔹
در پی شرارت ها علیه شناورهای تجاری ایرانی در دریای عمان و نقض مقررات تنگه هرمز از سوی ارتش متجاوز آمریکا، نیروی دریایی ارتش، مرکز "فرماندهی و کنترل " این شرارت…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/16926" target="_blank">📅 22:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16925">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اطلاعیه نیروی دریایی ارتش: ساعاتی قبل مرکز فرماندهی و کنترل شرارت‌های ارتش آمریکا در یک ناوشکن آمریکایی در دریای عمان هدف قرار گرفت</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/16925" target="_blank">📅 22:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16924">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اطلاعیه نیروی دریایی ارتش:
ساعاتی قبل مرکز فرماندهی و کنترل شرارت‌های ارتش آمریکا در یک ناوشکن آمریکایی در دریای عمان هدف قرار گرفت</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/16924" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16923">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">عراقچی:   آنچه در ۲ روز گذشته حمله به بیروت را متوقف کرد، در درجه اول قدرت مقاومت لبنان و توان نیروهای مسلح ایران بود  وقتی کار به جایی رسید که نیروهای رژیم صهیونیستی می‌خواستند به ضاحیه جنوبی بیروت حمله کنند، موضع قاطعی گرفتیم و نیروهای مسلح ما آماده پاسخ…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16923" target="_blank">📅 22:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16922">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">عراقچی: من مطمئنم که مسئله سفیر ما در بیروت حل خواهد شد، ما به حکمت دوستان و مسئولان دولت لبنان اعتماد داریم</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/16922" target="_blank">📅 22:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16921">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وزیر خارجه ایران: تماس‌های ما با آمریکا قطع نشده است، اما در مذاکرات پیشرفتی حاصل نشده است - المیادین.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/16921" target="_blank">📅 22:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16920">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزیر خارجه ایران: تماس‌های ما با آمریکا قطع نشده است، اما در مذاکرات پیشرفتی حاصل نشده است - المیادین.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/16920" target="_blank">📅 22:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16919">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWOo_M1ihNsi295NMygPyqoRxAg8XsWhP39qK_xwHgxC7QA-qHYqHswK_T36fd9ayi3z-Eweus4-V6QqHt0owS1A5veWtGOy5FBhs5N6e7SlMRk6te_f86HP7KW7tVxU7jmqnUND5uwI9BX1kFSMEgWM86xfmi7p8w-h4VP8d-2uPVbcJ_IVhelN7NWmqccDMh7rXWc9zJKBaUyaqGQJn5mqGLUFH39Cem3T8A0YQXSUKsLMh3XqExQlwyV4h4WZ20Cg1EYmiJKEQwwHsPsLieIjI6OftgnjWpRZ3SwJwb7eTQl-mOh-gZYD-yPIr4yuR3xhQ-Br5nRityjrZ2E9kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم تخریب پایگاه «علی السالم» آمریکایی ها در کویت
تصویر سمت راست مربوط به آشیانه ها و تصویر سمت چپ مربوط به انبارهای سوخت</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/16919" target="_blank">📅 19:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16918">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">روبیو:
به عنوان بخشی از سیاست خارجی ما و به دلایل متعدد، ما به صورت علنی درباره اینکه آیا اسرائیل سلاح‌های هسته‌ای در اختیار دارد یا خیر، بحث نمی‌کنیم.
ما پاسخ بهتری به کنگره درباره اینکه آیا اسرائیل سلاح‌های هسته‌ای در اختیار دارد یا خیر، ارائه خواهیم داد، مشروط بر اینکه آن‌ها درخواست پاسخ به صورت محرمانه را مطرح کنند.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/16918" target="_blank">📅 18:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16917">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شرایط جوری شده که اسرائیل عرب های لبنان را می زند و ما هم در پاسخ عرب های کویت را می زنیم که در حین آن هندی ها کشته می شوند</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/16917" target="_blank">📅 18:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16916">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd2b300c77.mp4?token=VH0fVNEbE38or8wdkznsEkzWJnrWhEj54kkLlLHH20yi0SrNo9bpSVo637Fswj36waAWCAhWSxn3ZbHmeLqGTKxTAZZMvCdFNFWzOGhbVVHDXW7HYwiRcYKJst-pGC28ePETe5MLgl96eM2Hr-H3Uts0P-JHmMeUhw7wPZ3F-Qi0fV5G3xh0JwijGslGkXA7Ah7JHMOuPmsvpqL5EKyX2zu6BUxch9oubPbGsoy2p7rbdsZwyOLOCoB5v4GCCMBaF-Qgsq2jcNprny5kJeBPkZ1d-wzwhGfqQBsyw98dMRhSGC_8Bzh6xW50f_9plSnP8qsP367L277ISNzWSHp3NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd2b300c77.mp4?token=VH0fVNEbE38or8wdkznsEkzWJnrWhEj54kkLlLHH20yi0SrNo9bpSVo637Fswj36waAWCAhWSxn3ZbHmeLqGTKxTAZZMvCdFNFWzOGhbVVHDXW7HYwiRcYKJst-pGC28ePETe5MLgl96eM2Hr-H3Uts0P-JHmMeUhw7wPZ3F-Qi0fV5G3xh0JwijGslGkXA7Ah7JHMOuPmsvpqL5EKyX2zu6BUxch9oubPbGsoy2p7rbdsZwyOLOCoB5v4GCCMBaF-Qgsq2jcNprny5kJeBPkZ1d-wzwhGfqQBsyw98dMRhSGC_8Bzh6xW50f_9plSnP8qsP367L277ISNzWSHp3NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رومن گافمن: از زخمی ۷ اکتبر تا رئیس موساد  سرلشکر رومن گافمن، مدیر تازه منصوب شده موساد اسرائیل (که در ژوئن ۲۰۲۶ سوگند یاد کرد)، به عنوان یکی از ارشدترین افسرانی ظاهر شد که به طور فعال با نیرو‌های حماس در حملات ۷ اکتبر ۲۰۲۳ درگیر شد.   گافمن که در آن زمان…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/16916" target="_blank">📅 17:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16915">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رییس جدید موساد!  رومن گوفمن، سرلشکر متولد بلاروس و از نزدیک‌ترین چهره‌های مورد اعتماد بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از ۲ ژوئن ۲۰۲۶ ریاست موساد را بر عهده گرفته است.   گوفمن که پیش از این به‌عنوان منشی نظامی نتانیاهو فعالیت می‌کرد، اکنون در رأس مهم‌ترین…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/16915" target="_blank">📅 17:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16914">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بلومبرگ :
مقامات غربی می‌گویند خطر تداوم  مخفیانه ساخت سلاح‌های هسته‌ای توسط ایران اکنون بالاتر از آن چیزی است که قبل از حملات نظامی ایالات متحده و اسرائیل در ژوئن ۲۰۲۵ بود.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/16914" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16913">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شاید باورتان نشود ولی حمله دیشب ما به کویت یک کشته داشته که آن هم ….   …یک کارگر هندی بوده!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/16913" target="_blank">📅 16:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16912">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شاید ما برخی کشتی ها را با پهپاد زده باشیم، برخی ها را با موشک بالستیک، برخی ها را هم با موشک کروز.  خب اینها می‌شود تفاوت‌های حملات ما.  اما یک شباهت بزرگ هم میان همه حملات ما وجود دارد و آن اینکه کشتی مورد تهاجم مال هر کشوری که باشد، دستکم ۲ ملوان هندی در…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/16912" target="_blank">📅 16:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16911">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رئیس‌جمهور لبنان حملات ایران به کویت و بحرین را محکوم کرد</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16911" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16910">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رئیس‌جمهور لبنان حملات ایران به کویت و بحرین را محکوم کرد</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/16910" target="_blank">📅 16:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16909">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBZ2BbuWimVok9yF38080aUrzZJv-icmqfCuts7nLC3E0rAvNIYzgoBFp2Bdumi8mL0-MD564CEp7KwThOTlp5A9mT0GZ57-Lfast_iULDHQUfYMl7akwp8mBk7XhTB6yS-QpSvbVDwk1x_FW2LAUTM7-9vPuY1S2axmPXU3E2SYW4hlQnZvRV4pQ9ni88EkHJjvQrysQqEhNN26NmvmPcXCkGezMajsQELqzq32F6KMw0_cXtCoIq9XyC87qE5RCasVZznHS4EPupiMVe_Th3Bh_4lo59F8PvpK4tzYYaJjjdZtbbMP3cn6gROinGns3VQ4qFL6jws6yXVxO9YScw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروه «مختار-007» ولی گفت که به شرط آتش بس در لبنان حاضر است سلاح های خود را تحویل دهد.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/16909" target="_blank">📅 15:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16908">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شما ببینید وضعیت این منطقه گه گرفته چطوری است که پاکستانی که خودش در‌ همین مدت در غرب (بلوچستان)، شمال (وزیرستان) و شرق (هند) غرق در تنش و نکبت بوده حالا دارد برای ما میانجیگری می‌کند!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/16908" target="_blank">📅 14:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16907">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ایران ۶ موشک بالستیک به پایگاه آمریکایی در کویت شلیک کرد  سپاه پاسداران انقلاب اسلامی حداقل ۶ موشک به پایگاه هوایی علی السالم، محل استقرار نیروهای آمریکایی، شلیک کرد. تصاویر، صداهای انفجار و تلاش‌های رهگیری بر فراز کویت را نشان می‌دهد.  رسانه‌های ایرانی می‌گویند…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/16907" target="_blank">📅 14:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16906">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">در این پست و پستهای ریپلای شده اش گفته شد که هدف اصلی ترامپ «تحقیر» شدید جمهوری اسلامی است و این مسخره بازی امروزش هم که میخواهم رهبر ایران را ببینم و اینها هم در همان راستا است.  عجیب است که ولی عده ای مونگول کماکان تصور می‌کنند هدف ترامپ سرنگونی نیست و مثلا…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/16906" target="_blank">📅 14:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16905">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fErqjn93_VV3GD_JZJ7_fEKHgZTdC05lDNVqZneHF6lK-cOFtaUfVq2o1fFZ02MHCn_GgZJs3I5K4nelzPHcJRrYPvXgOVO7DjvPKFVSC4EsoiYI-_ZXrOpbELhjoZYfI-uussaoru5RW_5BLdewCZU2YGMvjz5IOpBfMPtjpghoV749OByBC_p73qR4X4MOVNSlJCuaG0dL-HoEZJ1k1qIjHw_f1vrn5s5BczK11jx3ZVtqVIj1AvYXKSOyB_ic1fDRTHPTImwYqg_bVR3cl_UzqDhqXDn6GpaIgf84JRMIJ2PFLQ0AIcWMeK6KpBg6SLzhSRNFvWMkQ8jRJWbF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر کوتاه بود و دلخراش:
محمدرضا شهبازی
مورد تجاوز قرار گرفت
😄
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/16905" target="_blank">📅 14:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16904">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اینجا گفته بودم که هدف ترامپ تنها شکست ‌‌و تسلیم ایران نیست بلکه تحقیر جمهوری اسلامی نیز هست  به عنوان حکومتی که ۴۷ سال نمادهای قدرت و غرور آمریکایی را هدف قرار داده، جمهوری اسلامی از دید ترامپ بایستی پیش از شکست، شدیدا تحقیر بشود.  — تسخیر سفارت آمریکا و…</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SBoxxx/16904" target="_blank">📅 14:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16903">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ:
رهبر جمهوری اسلامی با مذاکرات موافقت کرده است.
اوضاع با ایران به سرعت در حال پیشرفت است و بسیار خوب خواهد شد.
ممکن است در مقطعی با او دیدار کنم.
ممکن است محاصره ایران تا روز کارگر برداشته شود</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SBoxxx/16903" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16902">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3Z320gQr8L0w3PuYDvecqHXOx3A_llUXVm_xH1OyrxTk1M6xzolKpl68pavbEAodvl7f70FAVEc0L27IC3sZG5uDpcD8ylhUrpunsClgHMUA_bvZCyMnNw-xykH2r9qSLl03-IHXuvEOeduA7QxSEB40r8FyTkFWBOUn1mVF2eZxIkGOtRnLhU5mKhjJ7B3_QnkpjhMNBOIfvcZmpsOnEoKRUmiRNAYRV1GQ5O8PGGcYsipjSSdImPAB125Kzpxy8gMW5OHSifSFPcv8bBNElSFrqLbI7qMIhFYSf9BvtWwZnCqli4Q038XTwXnW1eXIh8UvW3gFBoHhhdj7ln81w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تخریب ۱۱۰۰ مترمربع از آیینه کاری و گچ کاری کاخ گلستان در طی جنگ ۴۰ روزه</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/16902" target="_blank">📅 13:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16901">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اصحاب کهف با خلع سلاح گروه‌های مقاومت مخالفت کرد  گروه «اصحاب کهف» که از گروه‌های مقاومت عراقی وابسته به «مقاومت اسلامی» است، روز سه‌شنبه ۲ ژوئن با درخواست‌های سیاسی برای تحویل سلاح گروه‌های مسلح مخالفت کرد و تأکید نمود که استناد به حمایت مرجعیت از این روند،…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/16901" target="_blank">📅 12:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16900">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇨🇳
پروژه نظارتی چین با هوش مصنوعی: شناسایی منتقدان دولت پیش از اقدام سیاسی
🔸
شرکت چینی Geedge Networks که در زمینه ساختن نرم‌افزارهای امنیتی فعالیت دارد، اکنون تمرکز خود را روی تحلیل رفتار شهروندان گذاشته است
🔺
طبق اسناد فاش‌شده‌، این شرکت درحال استفاده از مدل‌های هوش مصنوعی برای تحلیل داده‌های موقعیت مکانی، الگوهای استفاده از اینترنت، تماس‌های تلفنی و حتی تاریخچه تماشای فیلم و مطالعه کتاب شهروندان است
🔸
هدف نهایی این پردازش‌ها، ساخت پروفایل‌های رفتاری دقیق برای شناسایی «نیت» افراد است تا سیستم بتواند کسانی را که ممکن است در آینده به منتقدان دولت تبدیل شوند، شناسایی کند. براساس صورت‌جلسه یکی از نشست‌های این شرکت، تمرکز محققان روی «کشف اطلاعات مضر» است؛ حزب کمونیست چین معمولاً از این عبارت برای توصیف نارضایتی‌های سیاسی یا محتوای مخالف دولت استفاده می‌کند</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/16900" target="_blank">📅 12:14 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
