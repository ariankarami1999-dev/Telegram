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
<img src="https://cdn4.telesco.pe/file/vtADaINdUsgJ6_UqxQh3PqFseAoSOQL24-lz_BF8IWWFNgPi5DpS7-tfzEqH97k0lWwxjGSaQe-YKemQbLfIEzP1KFoZmZ8RXtJkwXa54Y5Py1pPUC13Uf2_1DPcEES0wW60YSYR28B6uflKOE5ME_gvCgLhpO6WMD72HHIaA_-14NRCFKwlx7om3TM2eETn6mVm8qAA0sxinjeKN_X7b-tBPZt4WF7Y1nJR_B8DvLfGduSWwiBmoKnWaRLKAJ5Igp_iKy11R1WIQB6hkXyfE9M1FX37v-mhLt9JnYp61_tXNiMPaJarJbfKxeJWh9eCLFnz0mfvOpHwp1iD9QGaEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.2K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 18:12:24</div>
<hr>

<div class="tg-post" id="msg-18727">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آیا چین آماده دوره پسا-پوتین در روسیه می شود؟!  به نوشته وال استریت ژورنال، چین به آرامی روابطی را در داخل روسیه ایجاد می‌کند که فراتر از پوتین است و با مقامات و نخبگانی ارتباط برقرار می‌کند که پس از رفتن او، آینده این کشور را شکل خواهند داد.  روسیه هم متوجه…</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/18727" target="_blank">📅 15:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18726">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIi5HGLziJenhxdgIlAvpyv6T0GxysexjaUDxm4KiTwtAhwZGYYwa204plbad1qo7wRa3qkvoSC8SPgrOeLIdulyCLcM6V6VlAlMR13mpJ1pnvjsQeQuDOMsVzL3iTWCLEFxlJMzIQMCawn63xTKeGjqfhyPq4ok04hIiu8fLtwBg5pOcouA1FgOGxDNYzu9IMVaktYxMDIDrFa7XK-UbXhDDDRp4p83ZrFYlQYaVFT47TklMgOlpapz5LC1jI2Pe7Py3VecKyV48EpGI0OhKRAafD8yiUGOJS8p7ODzxd_SpA3eYoNSevSRW2f164mJIWfVOqWosYM7PzPnCMVddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا چین آماده دوره پسا-پوتین در روسیه می شود؟!
به نوشته وال استریت ژورنال، چین به آرامی روابطی را در داخل روسیه ایجاد می‌کند که فراتر از پوتین است و با مقامات و نخبگانی ارتباط برقرار می‌کند که پس از رفتن او، آینده این کشور را شکل خواهند داد.
روسیه هم متوجه تلاش‌های جاسوسی فزاینده چین در میان مقامات دولتی رده میانی شده است، اما مسکو تمایلی به مطرح کردن این موضوع با پکن ندارد، زیرا از آسیب رساندن به این رابطه می‌ترسد.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/18726" target="_blank">📅 15:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18725">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شهادت ۳ نفر در شهرستان حاجی‌آباد بندرعباس
🔹
بر اساس پیگیری‌های خبرنگار تسنیم از استانداری هرمزگان، حمله به مناطق غیرنظامی در غرب بندرعباس و شهرستان حاجی‌آباد تأیید شد.
🔹
در روستای سیدجوذر به یک ساختمان محیط زیست حمله شده که ۳ نفر به شهادت رسیدند.</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/18725" target="_blank">📅 14:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18724">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StZf7Vy_TCTiTtbIPQpSN7oCI06IUpRuAJcYyU5BORr4YWE-aHEuFNwA6v36REFst9epgF-CIjURVmiDgkPvearPaxwSuG_AkclgY3Fd8UJ5TcSwiMTY-BZC_wmqQitmhROXujTTeXqhkPqvlg51E2ArHJGQYL6xihiDUHY3z0K13IMV4bXyTlwVPjtiTPLpUQsxNuvYaiekE_AYPvlRyEHiCWmEOEj9472_GEhIhvjhd6fVH6yfzXxAQSESPFkRF8rwOS0_vCxi0gIUKEu_FiK20zZ2Kd6bA-mHunTBiousxYNj47BD7K3xB4MO2lLjvvyyPLOI-KtaC-SP3U6T2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضایی که دیشب به ترامپ توصیه کرده بود برود نگهبان قبر لیندسی گراهام بشود، همان دیشب از هیات رییسه کمیسیون امنیت ملی مجلس کنار گذاشته شد!</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/18724" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18723">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پاکستان از عربستان وام گرفته تا بدهی اش به امارات را بدهد!  مستراح گدایان!</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SBoxxx/18723" target="_blank">📅 14:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18722">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بر اساس گزارش‌های رسانه‌های دولتی ایران، حملات هوایی آمریکا به چهار نقطه در شهر بوشهر، ایران، انجام شد.</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SBoxxx/18722" target="_blank">📅 14:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18721">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ضربه قایقهای انتحاری آمریکا به تاسیسات صنایع دریایی مواردی را آشکار کرد. ارتفاع قایق نهایت 2.5-3m باشد که رادارها سطحی توام با کلاتر دریایی کمی دیرتر قایق را میگیرند اما  باز هم چندین کیلومتر فرصت دارند (رادارهای پر ارتفاع؟).از آن سو ج.ا مدیریت شبکه محور روی عبور قایقهای خودی ندارد، میتواند با آنها اشتباه بگیرد.
نظارت آمریکاییها با پهپاد از آسمان، گشتیهای سپاه را هم تحت رصد دارد که با یک عملیات شبکه محور از میان چند جزیره ایرانی به خوبی عبور کرده و خود را به سادگی به بطن صنایع دریایی رسانده است. در موقعیت شبهای بحرانی احتمالا گشتی ها سپاه و نظارت انسانی ساحلی هم کاهش می‌یابد، زیرا ریسک عملیاتی بالایی با توجه به تسلط هوایی آمریکاییها وجود دارد. در کل شکست عملیاتی جدی بود و رخنه‌های بزرگی را آشکار کرد.
@Exciton_missile_program
🚀</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/18721" target="_blank">📅 13:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18720">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">توییت سازمان اطلاعات سپاه!  به تاریخ ها دقت کنید؛ مشخصاً راهبرد سپاه این است که این تاریخ های حساس برای آمریکایی ها خالی از جنگ نباشد.  از همین تقویمی که در پست ریپلای شده قرار دادم استفاده شده است.  11 ژوئن = تاریخ آغاز جام جهانی 3 نوامبر = انتخابات مجالس…</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/18720" target="_blank">📅 13:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18719">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دلار خرید دارد همینجا با تارگت ۲۴۰ الی ۲۶۰ هزار تومان</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/18719" target="_blank">📅 13:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18718">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9AQPUspNJM5K3Js3sy-Q92jVjWZShFuiCty8UvL4tF206RDTk36rlc_5uu6EJR3KNyDDWFEPsKI3Pj_oz-iQF-xm_bTwtVi47w_zOk_-DmV6eGzssSWkW4lKf-4ewpGXSoSquZU96VQbgTEOmgA1LbH_pjAMfJblmec3xESShSiUmxwWfjQebZszPfdv00avJFaWkWU0mmIXEZJKBCTkNuOQkgCxPvJR8XoQxZh2pwoqZ2hoM20ap9NDQCE7SL73lec3RqV3Hy04ECdKwEwRB74CqBWd_nM8nCD8zT4yyzpUR5bT7MM2nTJxD3KNeuzCCSJ5OGXYHiGVeCkmQkdgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی قرار دارد.
با توجه به انتشار خبر کلیدی تورم، اساساً این ساعات برای معامله مناسب نیست.</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/18718" target="_blank">📅 12:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18717">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18717" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 7
سه شنبه 14 جولای 2026</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/18717" target="_blank">📅 12:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18716">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پاسخ چمران به سوالی درباره قطعی برق بدون اطلاع قبلی:   اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/18716" target="_blank">📅 10:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18715">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یک نفر دایرکت داده خدا لعنتشان کند؛ دیشب ‌پیک اول را زده بودم برق رفت همه جا تاریک شد فکر کردم کور شده ام!</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18715" target="_blank">📅 10:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18714">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزارت دفاع امارات:   در حادثه نفتکش «مومباسا»، یکی از خدمه کشته و ۸ نفر دیگر، از جمله ۴ نفر با وضعیت وخیم، زخمی شدند</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/18714" target="_blank">📅 10:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18713">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وزارت دفاع امارات:   در حادثه نفتکش «مومباسا»، یکی از خدمه کشته و ۸ نفر دیگر، از جمله ۴ نفر با وضعیت وخیم، زخمی شدند</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18713" target="_blank">📅 02:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18712">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وزارت دفاع امارات:
در حادثه نفتکش «مومباسا»، یکی از خدمه کشته و ۸ نفر دیگر، از جمله ۴ نفر با وضعیت وخیم، زخمی شدند</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18712" target="_blank">📅 02:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18711">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گزارشگر: شما ماه‌هاست که ایران را بمباران می‌کنید. آیا این وضعیت عادی جدید است؟
ترامپ: ما ۱۹ سال در ویتنام بودیم در حالی که فقط ۴ ماه است که ما اینجا هستیم.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18711" target="_blank">📅 02:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18710">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ادعای وزارت دفاع امارات:
دو نفتکش اماراتی در مسیر جنوبی تنگه هرمز با دو فروند موشک کروز ایرانی هدف قرار گرفتند</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18710" target="_blank">📅 02:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18709">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">قطعی برق در دمای 40 درجه به نظرم خیلی زیبنده ابرقدرت 4 دنیا نیست ولی خب.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/18709" target="_blank">📅 01:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18708">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">راه قدس از بحرین می گذرد!</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18708" target="_blank">📅 01:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18707">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجار در بحرین!</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18707" target="_blank">📅 01:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18706">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تلویزیون ایران: دو انفجار در جزیره کیش، در جنوب کشور، رخ داد.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18706" target="_blank">📅 01:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18705">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ:  محمد Something آنجا وجود دارد که نیاز به بیل دارد.  بیل‌ها به شما کمک نمی‌کنند. بزرگترین ماشین‌آلات دنیا هم به شما کمک نمی‌کنند.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18705" target="_blank">📅 00:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18704">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ادعای ترامپ:
عملیات نظامی علیه ایران ممکن است بین دو هفته تا سه هفته ادامه داشته باشد
کوه کلنگ ممکن است یک هدف احتمالی برای یک ضربه بزرگ و سنگین، درست به درِ ورودی باشد.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18704" target="_blank">📅 00:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18703">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز جمعه ۱۰ ژوئیه به طور رسمی کنگره را از ازسرگیری عملیات نظامی علیه ایران مطلع کرد و تعهدات خود را طبق قانون اختیارات جنگی انجام داد.
این اطلاع‌رسانی پس از ازسرگیری حملات آمریکا به اهداف نظامی ایران و بازگشت محاصره دریایی این کشور صورت می‌گیرد که در واکنش به حملات مداوم ایران به کشتیرانی تجاری در تنگه هرمز و علیه منافع و شرکای منطقه‌ای آمریکا انجام شده است.
طبق قانون اختیارات جنگی ۱۹۷۳، رئیس‌جمهور موظف است ظرف ۴۸ ساعت از ورود نیروهای مسلح آمریکا به درگیری یا شرایط قریب‌الوقوع، کنگره را مطلع کند.
این اطلاع‌رسانی به خودی خود مجوز اقدام نظامی نیست، اما الزامات گزارش‌دهی این قانون را برآورده می‌کند و کنگره نقش نظارتی خود را حفظ می‌کند</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18703" target="_blank">📅 00:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18702">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ درباره ایران:
حفظ تفاهم نامه نوعی آزمون بود.
آن‌ها به این آزمون احترام نگذاشتند.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18702" target="_blank">📅 00:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18701">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آسمان کلیر، پرواز چند جنگنده خودی در اطراف تهران!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18701" target="_blank">📅 23:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18700">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPFavhlhAPIupeCV8mYPjneLoOCoFgVmevisHt9W_Z30tDSKnuFso6fXug21CTek5qL_NRLtArPHsg4VOl_GGEHA_wcOIDYIxCv1mhuhJWxlrUuaNChRraDmunVO8S9uE586ahdVk9TrbznK97rWKOHHom8LIl6I4zQ8uZU5yWdEskLKMSkXh8-JOgS0R8xS2hbkMMNWwd15r9L2DXh3MfPp48Ir-hHxMyKcPA13ujPuJrUplOR_GpEZyiD395-54so67HRJnz1Wel07FmFDLArsRfwubLTqSSGdU-bUt0F9eF_rF6cm9C4cmJU6h7QtUH7Oji0DxlNFGxzN9_641A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسمان کلیر، پرواز چند جنگنده خودی در اطراف تهران!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/18700" target="_blank">📅 23:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18699">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یحیی سریع سخنگوی نیروهای مسلح یمن:
در پاسخ به تجاوز جنایتکارانه سعودی، نیروهای مسلح یمن با تعدادی موشک بالستیک و پهپاد، عملیات نظامی را با هدف قرار دادن فرودگاه بین‌المللی ابها انجام دادند
به همه شرکت‌های هواپیمایی در مورد پرواز از طریق حریم هوایی عربستان سعودی هشدار می‌دهیم و از آنها می‌خواهیم تا زمان لغو محاصره فرودگاه بین‌المللی صنعا، هشدارهای ما را جدی بگیرند.
ما از جمهوری اسلامی ایران به خاطر کمک‌هایش به جمهوری یمن در لغو محاصره ناعادلانه فرودگاه بین‌المللی صنعا و تسهیل پروازهای بشردوستانه به و از فرودگاه، صمیمانه تشکر می‌کنیم
.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18699" target="_blank">📅 23:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18698">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18698" target="_blank">📅 23:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18697">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش‌های ایران از موج انفجارها در چندین مکان در جنوب
منابع ایرانی از وقوع سری انفجارها در چندین مکان در بخش جنوبی کشور گزارش می‌دهند.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18697" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18696">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ارتش آمریکا اعلام کرد که از ساعت ۲۰:۰۰ به وقت گرینویچ فردا، محاصره دریایی تمام بنادر ایران را آغاز خواهد کرد
.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18696" target="_blank">📅 21:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18695">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نیویورک تایمز: ترامپ رسماً کنگره را از سرگیری جنگ علیه ایران مطلع کرد</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/18695" target="_blank">📅 21:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18694">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عقل ندارند. خب الان کله زرد می‌گوید من ۲۰ درصد میگیرم ده درصدش یعنی ۲ درصدش را میدهم به شما!</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18694" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18693">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">عباس آقا عراقچی:  رئیس‌جمهور ایالات متحده کاملاً حق دارد. هر کس که عبور امن و ایمن کشتی‌های تجاری از تنگه هرمز را تضمین کند، باید برای این خدمت عوارض دریافت کند.  ایران همیشه نگهبان تنگه بوده و تا ابد نیز باقی خواهد ماند.  ۲۰٪ البته خیلی زیاد است. ما منصف…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/18693" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18692">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ:   تنگه هرمز باز است و باقی خواهد ماند، چه با ایران و چه بدون آن.   ما محاصره ایران را که به این دلیل نامگذاری شده است که فقط کشتی‌ها یا مشتریان ایران را از ورود یا خروج باز می‌دارد، دوباره اعمال می‌کنیم.   تمام کشورهای دیگر می‌توانند از تنگه به صورت…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18692" target="_blank">📅 21:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18691">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بوی یک حمله همه جانبه به نیروهای موسوم به محور مقاومت می آید:  — حمله پلیس عراق به منازل عناصر سیاسی نزدیک به ایران — ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی — توافق دولت لبنان و اسرائیل برای پایان حیات نظامی حزب الله — آماده شدن نیروهای مخالف حوثی ها…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18691" target="_blank">📅 21:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18690">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmvjxk29tJsos_Ims8uYDLjKgtwVPzbCPrWOrEiFtvSDgcyPXttL5VaybDzyRvwh1g2aF7KU4Bm3KhI0Cqhz0OENtnsh-WS5JrkaJKGOQMNTTKFWDOS5sJHf64u5mFoL8elOQpvYmviczLLhvPXpOmE6J0SY8cKeR58n4UoXhf28eSPV5tZ9pDjALqSiT6sTRr_VqoWl-AAKpAXeF6_xhtvkyWMaPEkcI0FbPwcNNGvDUUZycrHs3XKe1-V9NJs3G1Op0yMF0io5XuRe0wCzRoAyN9avjujLTAkSMWKkSL-Xe0xD8FFktNgn_16ngmN-jpfXMbFHO3U-lorr7nhQ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18690" target="_blank">📅 21:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18689">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزارت حمل و نقل یمن: حملات دشمن سعودی و هدف قرار دادن فرودگاه صنعا، تلاشی عمدی برای محروم کردن هزاران بیمار و مسافر از ابتدایی‌ترین حقوق تضمین شده‌شان است.
🔹️
ما از سازمان ملل متحد، جامعه بین‌المللی و سازمان‌های بشردوستانه بین‌المللی می‌خواهیم که مسئولیت خود…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18689" target="_blank">📅 20:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18688">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حوثی ها با موشک بالستیک پاسخ سعودی ها را داده اند.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18688" target="_blank">📅 20:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18687">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">— گزارش‌هایی از انفجارها در استان عسیر عربستان سعودی منتشر شده است که فرودگاه بین‌المللی ابها در آن قرار دارد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18687" target="_blank">📅 20:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18686">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">— گزارش‌هایی از انفجارها در استان عسیر عربستان سعودی منتشر شده است که فرودگاه بین‌المللی ابها در آن قرار دارد.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18686" target="_blank">📅 20:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18685">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وزیر امور خارجه آرژانتین، پابلو کیرنو، ساکنان جزایر فالکلند را "جمعیتی که به طور مصنوعی وارد این منطقه شده‌اند" توصیف کرد و از بریتانیا خواست تا مذاکرات مربوط به حاکمیت این جزایر را آغاز کند.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18685" target="_blank">📅 20:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18684">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256741d101.mp4?token=L1fEc0FY-crGtV72xUKptr37TlUeCCwoZXGsHeiUQVccj-peSErIZE3xWUj198G3fn3QcXd0NVRfpjAmYxtllKmdxgvdhxBpQ4KWhv0j7UFEON92dF2MEXOva-_mgKDul_wPjulgXmHqzskLMa_sIPPZOGd2X-i11r7CFjV6fCYkrSAjJE_aFJaDkD1AA1Og3kJ233iNVNTJDerTtFuO9pxEvCi1fdK1w21uoYEPtklq-C96WOl-ab_fZD9ah8H5HPGM9UnLf0P2OTNd4e4YSEV04d59TmT93RmoRpxqa2buIlZ2nhOj0YL0qosKK9scvunVxESa_Lt5MAz40LwdqDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256741d101.mp4?token=L1fEc0FY-crGtV72xUKptr37TlUeCCwoZXGsHeiUQVccj-peSErIZE3xWUj198G3fn3QcXd0NVRfpjAmYxtllKmdxgvdhxBpQ4KWhv0j7UFEON92dF2MEXOva-_mgKDul_wPjulgXmHqzskLMa_sIPPZOGd2X-i11r7CFjV6fCYkrSAjJE_aFJaDkD1AA1Og3kJ233iNVNTJDerTtFuO9pxEvCi1fdK1w21uoYEPtklq-C96WOl-ab_fZD9ah8H5HPGM9UnLf0P2OTNd4e4YSEV04d59TmT93RmoRpxqa2buIlZ2nhOj0YL0qosKK9scvunVxESa_Lt5MAz40LwdqDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی آمریکا:   برای اولین بار، یک پایگاه دریایی ایرانی در بندرعباس را با استفاده از قایق‌های بدون سرنشین انتحاری مورد بمباران قرار دادیم.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/18684" target="_blank">📅 18:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18683">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فرماندهی مرکزی آمریکا:   برای اولین بار، یک پایگاه دریایی ایرانی در بندرعباس را با استفاده از قایق‌های بدون سرنشین انتحاری مورد بمباران قرار دادیم.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18683" target="_blank">📅 18:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18682">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فرماندهی مرکزی آمریکا:
برای اولین بار، یک پایگاه دریایی ایرانی در بندرعباس را با استفاده از قایق‌های بدون سرنشین انتحاری مورد بمباران قرار دادیم.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18682" target="_blank">📅 18:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18681">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مارکو روبیو:
دیوان کیفری بین‌الملل در پی آن است که به داوری پاسخگو و بدون پاسخگویی از قانون جهانی جدید تبدیل شود — که توانایی تعقیب و دستگیری شهروندان ما را به دلخواه دارد و حاکمیت آمریکا را به صورت وجودی تهدید می‌کند.
ما به دیوان کیفری بین‌الملل معنای کامل عزم آمریکا را آموزش خواهیم داد.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18681" target="_blank">📅 18:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18680">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ در مورد ایران:   خمینی رفته است. پسر او ۹۰٪ رفته است.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18680" target="_blank">📅 18:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18679">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ:   تنگه هرمز باز است و باقی خواهد ماند، چه با ایران و چه بدون آن.   ما محاصره ایران را که به این دلیل نامگذاری شده است که فقط کشتی‌ها یا مشتریان ایران را از ورود یا خروج باز می‌دارد، دوباره اعمال می‌کنیم.   تمام کشورهای دیگر می‌توانند از تنگه به صورت…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18679" target="_blank">📅 18:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18678">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پوتین: پاسخ روسیه به حملات دشمن متقابل و چندین برابر قدرتمندتر خواهد بود.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18678" target="_blank">📅 18:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18677">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دبی برنامه‌ریزی برای ساخت بندر جدید برای دور زدن تنگه هرمز دارد</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18677" target="_blank">📅 17:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18676">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ:
تنگه هرمز باز است و باقی خواهد ماند، چه با ایران و چه بدون آن.
ما محاصره ایران را که به این دلیل نامگذاری شده است که فقط کشتی‌ها یا مشتریان ایران را از ورود یا خروج باز می‌دارد، دوباره اعمال می‌کنیم.
تمام کشورهای دیگر می‌توانند از تنگه به صورت عادلانه و آزاد استفاده کنند.
ایالات متحده آمریکا از این به بعد به عنوان «نگهبان تنگه هرمز» شناخته خواهد شد، اما به همین دلیل و به عنوان مسئله‌ای از عدالت، به میزان ۲۰ درصد از تمام محموله‌های حمل‌ونقلی، برای هرگونه هزینه‌ای که برای انجام وظیفه تأمین امنیت و ایمنی در این بخش بسیار ناپایدار جهان لازم باشد، جبران خسارت خواهد شد.
فرآیند و تشکیل این ساختار بلافاصله آغاز می‌شود.
از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18676" target="_blank">📅 17:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18675">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ستاد مرکزی خاتم‌الانبیای ایران:
ما تحت هیچ شرایطی اجازه نخواهیم داد که ایالات متحده در مدیریت تنگه هرمز دخالت کند؛ نه اکنون و نه هرگز.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18675" target="_blank">📅 16:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18674">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ در مورد ایران:
خمینی رفته است. پسر او ۹۰٪ رفته است.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18674" target="_blank">📅 16:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18673">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ:
ما دیشب ضربه خیلی سختی به آن‌ها زدیم. هر بار که آن‌ها یک پهپاد می‌فرستند، ما ضربه خیلی سختی به آن‌ها می‌زنیم. اما ما یک توافق داشتیم؛ چیزی که هیچ‌کس نمی‌داند این است که ما یک توافق داشتیم، کار تمام شده بود، و بعد آن‌ها توافق را شکستند. آن‌ها همیشه توافق را می‌شکنند. ما تا به حال ۱۰ بار با این افراد توافق داشته‌ایم. بنابراین ما فقط قرار است ضربه خیلی سختی به آن‌ها بزنیم. و ما این تنگه را حفظ خواهیم کرد و احتمالاً آن را اداره می‌کنیم، ما تبدیل به "نگهبان تنگه" می‌شویم؛ شاید اسمش را بگذاریم "فرشته نگهبان تنگه". و ما باید هزینه‌ای که برای این کار می‌کنیم را پس بگیریم. وقتی این کار را انجام دهیم، پولمان را پس خواهیم گرفت چون کشورهای دیگری که طرف ما هستند بسیار ثروتمندند. و از ما انتظار نمی‌رود که این کار را مجانی انجام دهیم، برخلاف کاری که سال‌ها انجام دادیم. می‌دانید، ما برای ۵۰ سال یا بیشتر از این تنگه محافظت کردیم و هیچ‌وقت پولی بابت آن دریافت نکردیم. آن‌ها همه پول‌ها را به دست آوردند و ایالات متحده فقط... می‌دانید، هیچ... شگفت‌انگیز است. ما هیچ‌وقت سودی نبردیم. ما مجانی از آن محافظت کردیم. اما حالا که می‌خواهیم از آن محافظت کنیم، قرار است بابت محافظت از آن پول بگیریم، پول زیادی هم بگیریم. ما فقط می‌خواهیم هزینه‌ای که برای انجام تمام این کارها و به خطر انداختن نیروهایمان صرف می‌کنیم، جبران شود. اما ما در واقع مردم را در خطر قرار نمی‌دهیم، ما واقعاً داریم نجاتشان می‌دهیم.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18673" target="_blank">📅 16:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18672">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ :
ما قصد داریم‌ حملات جدی تری علیه ایران انجام دهیم</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18672" target="_blank">📅 16:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18671">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ:  ۵.۲٪ از روسای جمهور کشته می‌شوند و  به ۸.۵٪ با گلوله شلیک می شود.  رئیس جمهور بودن خطرناک است.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18671" target="_blank">📅 16:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18670">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این بنده خدا واقعا باورش شده ما برنامه ترورش را داریم!  یک نفر به او بگوید ما از سال 1367 هنوز سلمان رشدی را نتوانسته ایم کامل بکشیم.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18670" target="_blank">📅 15:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18669">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ درباره تنگه هرمز:
ما تنگه هزمز را حفظ خواهیم کرد. احتمالاً آن را اداره خواهیم کرد.
ما نگهبان تنگه خواهیم شد و وقتی این کار را انجام دهیم، برای آن جبران خسارت خواهیم شد.
ما به مدت ۵۰ سال از تنگه محافظت کردیم و هرگز بابت آن پولی دریافت نکردیم. ما بیهوده از آن محافظت کردیم، اما اکنون پول درخواهیم آورد.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18669" target="_blank">📅 15:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18668">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">در‌ این صوتی وضعیت خر تو خر یمن را توضیح داده بودم .</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/18668" target="_blank">📅 15:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18667">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وزارت حمل و نقل یمن: حملات دشمن سعودی و هدف قرار دادن فرودگاه صنعا، تلاشی عمدی برای محروم کردن هزاران بیمار و مسافر از ابتدایی‌ترین حقوق تضمین شده‌شان است.
🔹️
ما از سازمان ملل متحد، جامعه بین‌المللی و سازمان‌های بشردوستانه بین‌المللی می‌خواهیم که مسئولیت خود…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18667" target="_blank">📅 15:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18666">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دولت بریتانیا سپاه پاسداران انقلاب اسلامی را در فهرست سازمان‌های تروریستی قرار داد که بر اساس آن، عضویت در این نهاد، شرکت در نشست‌های آن و حمل نماد آن در انظار عمومی جرم کیفری خواهد بود.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18666" target="_blank">📅 15:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18665">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وزارت حمل و نقل یمن: حملات دشمن سعودی و هدف قرار دادن فرودگاه صنعا، تلاشی عمدی برای محروم کردن هزاران بیمار و مسافر از ابتدایی‌ترین حقوق تضمین شده‌شان است.
🔹️
ما از سازمان ملل متحد، جامعه بین‌المللی و سازمان‌های بشردوستانه بین‌المللی می‌خواهیم که مسئولیت خود…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18665" target="_blank">📅 15:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18664">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">به نظر می رسد زمان حمله نیروهای مورد حمایت سعودی یا امارات به حوثی ها نزدیک است.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18664" target="_blank">📅 14:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18663">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دلیگانی، نایب‌رئیس اول کمیسیون اصل ۹۰ مجلس :    تحویل (ترامپ و نتانیاهو) به ایران، باید یکی از بندهای مذاکرات می‌بود</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18663" target="_blank">📅 14:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18662">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دلیگانی، نایب‌رئیس اول کمیسیون اصل ۹۰ مجلس :
تحویل (ترامپ و نتانیاهو) به ایران، باید یکی از بندهای مذاکرات می‌بود</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18662" target="_blank">📅 14:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18661">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پزشکیان:  آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18661" target="_blank">📅 13:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18660">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فنلاند یک شهر زیرزمینی در زیر هلسینکی ساخته است که می‌تواند تقریباً یک میلیون نفر را محافظت کند.   زیر هلسینکی، یک شبکه گسترده از ۵۵۰۰ پناهگاه ضد بمب وجود دارد که می‌تواند تقریباً یک میلیون نفر را در صورت جنگ یا حمله هسته‌ای محافظت کند.  اکثر این پناهگاه‌ها…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18660" target="_blank">📅 12:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18659">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فنلاند یک شهر زیرزمینی در زیر هلسینکی ساخته است که می‌تواند تقریباً یک میلیون نفر را محافظت کند.   زیر هلسینکی، یک شبکه گسترده از ۵۵۰۰ پناهگاه ضد بمب وجود دارد که می‌تواند تقریباً یک میلیون نفر را در صورت جنگ یا حمله هسته‌ای محافظت کند.  اکثر این پناهگاه‌ها…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18659" target="_blank">📅 12:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18658">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sb65bD58cJBPfgh28TrzuGhvr-ijhVFH_IB7fGNRru56X0bs2HOehb1kgPNGZFzBFilZ0QcXh5QNpmHhcwDaWjwD5mEiPcKVsdr3Rv7sPxNSGOieuWhhj2O5nRzvlG-ds1LiAS1uaKtgh4eW3UJbu7-xjyvj--IKfCn7DMOZqAbn-AJcD4cIscPj59lsIv_pftJQtdZwpFl3GN64ae23E6lqG995PsjdohkmL0DBeLAKERrB61kHZwVbgmhyIoWX8mCCT1mxITMbIhV_NLiZC4ZQ8ZjPkUTncQsqjhG8RNRq883_1qLOfslh28aBQ7uOs6SjQA9ZSPrN2wkSdmfnfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فنلاند یک شهر زیرزمینی در زیر هلسینکی ساخته است که می‌تواند تقریباً یک میلیون نفر را محافظت کند.
زیر هلسینکی، یک شبکه گسترده از ۵۵۰۰ پناهگاه ضد بمب وجود دارد که می‌تواند تقریباً یک میلیون نفر را در صورت جنگ یا حمله هسته‌ای محافظت کند.
اکثر این پناهگاه‌ها برای اهداف روزمره مانند سالن‌های ورزشی، زمین‌های بازی، استخرهای شنا و حتی فضاهای تمرین برای گروه‌های موسیقی راک مورد استفاده قرار می‌گیرند، اما می‌توانند به سرعت به پناهگاه‌های اضطراری تبدیل شوند.
منبع: The Times</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18658" target="_blank">📅 12:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18656">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار نظامی ایران و جهان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/732e84f6ce.mp4?token=DMRQfLtSmxtKLinXf6qv5sY4VyCG0vKuhTmEMELE1UR0rhEE9zS1DVAjR_FonP9FZKa7ealT05rItJsUILHyfgTmCWH-E3ppzU7S77BsLcWRr9taSBdNQLGdSZm7_EDXnHUMi_1YP3w8S-jLW6_OTpslGWsM_yvxM0Io2ImG58cMhVG66mJfm9HLGemrzjVixBE-Tc_7NY6elCNaDuCwyzcQ8kg6EQkuCIG_9FXgcknXzhph9BYMNB6sX2dJD_m_-qQ63CJTPW6zooyNluRrsp0t6eB19r0pYD7ybe02BSt1uSf9RouT7y0MnBdCFFVGSYH1Esw_hi3kxGInU9OW6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/732e84f6ce.mp4?token=DMRQfLtSmxtKLinXf6qv5sY4VyCG0vKuhTmEMELE1UR0rhEE9zS1DVAjR_FonP9FZKa7ealT05rItJsUILHyfgTmCWH-E3ppzU7S77BsLcWRr9taSBdNQLGdSZm7_EDXnHUMi_1YP3w8S-jLW6_OTpslGWsM_yvxM0Io2ImG58cMhVG66mJfm9HLGemrzjVixBE-Tc_7NY6elCNaDuCwyzcQ8kg6EQkuCIG_9FXgcknXzhph9BYMNB6sX2dJD_m_-qQ63CJTPW6zooyNluRrsp0t6eB19r0pYD7ybe02BSt1uSf9RouT7y0MnBdCFFVGSYH1Esw_hi3kxGInU9OW6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قاسمیان: شما نباید بگید آآآمریکاااا بی دوووووو ، باید بگید آمریکا بی دو. یعنی باید با تحقیر بگی
✍🏻
exxon
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/18656" target="_blank">📅 12:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18655">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پزشکیان:  آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/18655" target="_blank">📅 12:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18654">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پزشکیان:  آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18654" target="_blank">📅 12:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18653">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5052358e.mp4?token=e7Q-YXrVgNffNjgsnzhMEWqDl7pY7NVxeyJ_ocisza5_6mH01tky-Cr4d0XlvKGGXOGVett29O3sFXVaZniOsgMO88GQcPj2fZT3Fs9dpuZ7F8GG5r1Gdo60Mjol2t1732QszPgxx_s4w1mQgpIsgdZ_15sQ5qKlmiUxmYhkqwVYldugDv0WI4iBSvB2YAQCwJhVYs68KBHw6y6dHrDXnecXY-pxN4BkabkCpiRLzNbR9d1WWQVPCwKMemt5ZDzb3KB97ATBIkaYNpqzX5_pSILbIPBRuHbmlZTCpOaZgtwJPxM9oVFHy_oVyvCrTQOVcVulVpRT8LRhCzXBPbNa7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5052358e.mp4?token=e7Q-YXrVgNffNjgsnzhMEWqDl7pY7NVxeyJ_ocisza5_6mH01tky-Cr4d0XlvKGGXOGVett29O3sFXVaZniOsgMO88GQcPj2fZT3Fs9dpuZ7F8GG5r1Gdo60Mjol2t1732QszPgxx_s4w1mQgpIsgdZ_15sQ5qKlmiUxmYhkqwVYldugDv0WI4iBSvB2YAQCwJhVYs68KBHw6y6dHrDXnecXY-pxN4BkabkCpiRLzNbR9d1WWQVPCwKMemt5ZDzb3KB97ATBIkaYNpqzX5_pSILbIPBRuHbmlZTCpOaZgtwJPxM9oVFHy_oVyvCrTQOVcVulVpRT8LRhCzXBPbNa7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
آمریکایی ها ما را نکنند — تحریم — ما هم کاری به آنها نداریم و حتی با آنها هم برادریم!</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18653" target="_blank">📅 12:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18652">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔹
حسین شریعتمداری، مدیرمسوول و نماینده ولی‌فقیه در روزنامه کیهان، در یادداشتی، بابت مرگ لیندسی گراهام، به عزراییل، گلایه کرده که چرا:   «پیشدستی کردید و قبل از ما حسابش را رسیدید... از خدا اجازه می‌گرفتید و کمی صبر می‌کردید تا این عنصر پلید را با دست خود راهی…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18652" target="_blank">📅 12:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18651">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knc4QYp7mEiddcLoCJ9ykDdn-_yTMfFompGQUHadBlyhdHwEDUnmUTXBrr2g9fc8nn5Yjp8PwN4lsBraF7tNqL78jtmuJwV41Kck0yX23-rNxNqrG5sdbNeBNIhxAIvL92L0wRuyeQt-nhvSuUYn5H3wqw_zSpuJEiDAww_vpG_kPyhemBYEw86yiuDRMm854rN5EC0Rf5mT4zuRMc3y9bI7825apbcoKA3ymn-5mbr8ygv3ETc15Rf0alUyH50TyH92toEnDNzJZ48nchly2pmB-GyQPapToqHo1cWQ_SY4fpEZEuLZqoJM3IYB3gN4ljrBBTkFiF5QmmBHLAVmcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
حسین شریعتمداری، مدیرمسوول و نماینده ولی‌فقیه در روزنامه کیهان، در یادداشتی، بابت مرگ لیندسی گراهام، به عزراییل، گلایه کرده که چرا:
«پیشدستی کردید و قبل از ما حسابش را رسیدید... از خدا اجازه می‌گرفتید و کمی صبر می‌کردید تا این عنصر پلید را با دست خود راهی جهنم کنیم.»</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18651" target="_blank">📅 12:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18650">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va3o5XJEO3kBCfptmci5kpjRPsz2gIsYqrlRi7fICN1xA8rm9evYJoEQDyxZsm6_Jk6Sm3pblo8vZtiCh_M_EO6sm-iwmvni9iLRMkas0wIp3W-XGrebt6qTKqx7_IOlZG4cOAGHRZrUR9xa4WVtQ5QMo85oBy8cFFB-AAobseMpjMSUSGDeF-FwrvB35UmQlarwy2qSzwUAv8lvt5rVZKA9V6BK9uIjkNX9rBxQiQHhVDaNtfLWA5JXHfSSInIT_K6_qLK-YPganXtkS29YXRf5c6VAx2BHT2cWanldYaG6TaxJgqxBwx5wxADdoAjH8ZS3n9M8b8pRc92PzZ6z1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک در این لحظه کاهش اساسی یافته و کاهش تنش ها را پیش بینی می کند.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/18650" target="_blank">📅 11:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18649">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سومین پرواز از سوی دولت روسیه از مسکو به سمت ایران به پرواز در حال انجام است.  هواپیماهای توپولوف ۱۳۴ معمولاً برای انتقال افراد مهم و مقامات رده‌بالا استفاده می‌شوند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18649" target="_blank">📅 11:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18648">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران در مورد فوت لیندسی گراهام:
عزرائیل عدالت را جاری می‌کند.
برای چنین فردی که میراث زندگی‌اش سرشار از کینه و حمایت از تجاوز بود، چیزی جز یک سابقه تاریک در ذهن مردم باقی نخواهد ماند.
مرگ این سناتور پرخاشگر و با دهان گزنده، قطعاً قلب هیچ فرد آزاده‌ای را آزرده نخواهد کرد.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18648" target="_blank">📅 11:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18647">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به نظر می رسد نیروهای آمریکایی دیشب از مهمات ویژه برای تخریب تونل‌ها استفاده کردند تا یک پایگاه موشکی زیرزمینی را در نزدیکی شهر دزفول، در پایگاه چهارم شکاری نیروی هوایی  مورد حمله قرار دهند.</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SBoxxx/18647" target="_blank">📅 11:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18646">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سنتکام:
موج دیگری از حملات را علیه ایران به پایان رساندیم
تامپا، فلوریدا —
فرماندهی مرکزی ایالات متحده (CENTCOM) در ۱۲ ژوئیه موج جدیدی از حملات تهاجمی علیه ایران را به پایان رساند و با استفاده از مهمات دقیق، ده‌ها هدف در چندین مکان را هدف قرار داد تا توانایی ایران در ادامه حمله به کشتیرانی بین‌المللی که از تنگه هرمز عبور می‌کند را تضعیف کند.
نیروهای CENTCOM به سیستم‌های دفاع هوایی نظامی ایران، سایت‌های راداری ساحلی، توان موشکی و پهپادی و قایق‌های کوچک حمله کردند و برای اولین بار از هواپیماهای جنگنده ایالات متحده، کشتی‌های دریایی، پهپادهای حمله هوایی یک‌طرفه و پهپادهای حمله دریایی یک‌طرفه استفاده کردند.
تنگه هرمز یک مسیر دریایی حیاتی برای تجارت جهانی است. ایران کنترل آن را در دست ندارد.
نیروهای ایالات متحده برای اطمینان از اینکه آزگان دریانوردی برای کشتیرانی تجاری باقی می‌ماند، حتی با وجود تهاجم بی‌دلیل، آزار و اذیت، تهدیدات و اعلامیه‌های خودسرانه مداوم ایران، آماده و مهیا شده‌اند.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18646" target="_blank">📅 10:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18645">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آغاز خاموشی‌های برنامه ریزی شده در کشور!   مدیر امور مشتریان شرکت توانیر با اشاره به برنامه‌ریزی خاموشی‌های احتمالی:   این برنامه‌ها دو روز قبل اعلام می‌شوند و برای دو روز آینده نیز برنامه قطعی برق در کشور اطلاع‌رسانی شده است.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18645" target="_blank">📅 10:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18644">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آغاز خاموشی‌های برنامه ریزی شده در کشور
!
مدیر امور مشتریان شرکت توانیر با اشاره به برنامه‌ریزی خاموشی‌های احتمالی:
این برنامه‌ها دو روز قبل اعلام می‌شوند و برای دو روز آینده نیز برنامه قطعی برق در کشور اطلاع‌رسانی شده است.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18644" target="_blank">📅 10:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18643">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5sc59Luh2usSalKo6ieKJD57lQau7cXtUpPzDqjNIzRd7orgqf2KxjhjCriPqqbzfi6EH267kpmqRwGdvCuIrGnvDR4-QGJaNX-eFGyBWPuMVvxSIDzjoOfrt8mOicbrlLC1zFbYBDY2Rvmhh5ORalZv6KclHJ8E2L8Mlmi9s0CC3vq9m1n1vZ1bRlcdeYJAsPx9ZStjXIks-sAbUYUH75-bXq-3oHj-LIAk8vmSqEKGpfE5F89cgbsUUesYgryjzXFEE3IA0vCeGF54rbREJ_ORq8ZMMA2sqDdiXxjVAVMDz6h39huc2LFzNJFnXXGTKHgEVXlkKv98GST-Usw4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک در این لحظه کاهش اساسی یافته و کاهش تنش ها را پیش بینی می کند.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/18643" target="_blank">📅 09:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18642">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18642" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 6
دوشنبه 13 جولای 2026</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18642" target="_blank">📅 09:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18641">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزیر امور خارجه آرژانتین، پابلو کیرنو، ساکنان جزایر فالکلند را "جمعیتی که به طور مصنوعی وارد این منطقه شده‌اند" توصیف کرد و از بریتانیا خواست تا مذاکرات مربوط به حاکمیت این جزایر را آغاز کند.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18641" target="_blank">📅 09:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18640">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزیر امور خارجه آرژانتین، پابلو کیرنو، ساکنان جزایر فالکلند را "جمعیتی که به طور مصنوعی وارد این منطقه شده‌اند" توصیف کرد و از بریتانیا خواست تا مذاکرات مربوط به حاکمیت این جزایر را آغاز کند.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/18640" target="_blank">📅 09:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18639">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3L_KiORkgC7r7STAxg1wiu_7v7nhLieH9ePgl4FESjy_uZPizvZjok7n2dlELe0A2kDbpgorKFd9ahY2ryLhW3hc2hEHnSgmoxPinknST82qXU_rjHPvHnSpp67MytHqClST-4XzrD2kukRAET_iPyF58VOBlXlQe_JAJmkGZGUPX1hFTGXhyWbr91K91IHbpYsUUXLAOS68oZi09Fs11Zj-djDzKk2FK6tg2Wg-tHB43CESPdufoIwy8j3Yy0o3abOl5qbMAIown7Ka57H8NSDndvaDIbPf2qDI665UqyXCPzTlUT4cyOP2gVIkbxjqBBJZJNrDEnqS89WPpQb8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گستره جغرافیایی حملات دیشب آمریکایی ها</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/18639" target="_blank">📅 08:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18638">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">— سپاه پاسداران:
«در مرحله چهارم عملیات «چشم در برابر چشم»، نیروهای زمینی قهرمان سپاه پاسداران پایگاه موشکی زمینی به زمینی ارتش ایالات متحده در کویت را هدف قرار دادند و دو پرتابگر موشکی هیمارس و انبارهای مهمات را آتش زده و به طور کامل نابود کردند».</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18638" target="_blank">📅 08:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18637">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده اعلام کرد که برای اولین بار از شهپادهای دریایی انتحاری  برای هدف‌گیری دارایی‌های ایران استفاده شده است</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18637" target="_blank">📅 08:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18636">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سومین پرواز از سوی دولت روسیه از مسکو به سمت ایران به پرواز در حال انجام است.
هواپیماهای توپولوف ۱۳۴ معمولاً برای انتقال افراد مهم و مقامات رده‌بالا استفاده می‌شوند.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18636" target="_blank">📅 08:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18635">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آمریکایی ها دارند با هیمارس و از کویت، شهرهای خوزستان را شخم می زنند!</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18635" target="_blank">📅 02:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18634">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mg2RLHB-Tj8jwkfiiAlccXd5bQu9mUHENU6dusv8tG4uCCDTylPo98MVPBxBioJ6OGfUQbZ0OV7aYDN3HbwUT0yw_u0nIn0BqsHscG53vVEfXz44fWAgLI51hhbftGTAROHWM2GCHHy13FrHqYWZDixKW8vjulEAiKof4vsbUWGXIyOvfgshaAX3noYGDzxSpn9gvo42yTSNJzZin2y6HVdN8zPEzqEurKEfQaGDnuYd6ophhKF7moTCEELuTRYB7-C5jVmDrY98iQlhqa5kKf0viQUp8TpASOofQ9O18YmcUPSoz2B2KehgKjZHwSLBPe96iwLeE11wZI96nquXUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربها وقتی میفهمند دوباره ما برای آزادی قدس داریم خودشان را میزنیم!</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/18634" target="_blank">📅 02:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18633">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:  هشدار فوری به تمامی شهروندان و ساکنان کویت، بحرین و امارات متحده عربی:  با توجه به تبعیت حاکمان شما و استفاده از برخی مناطق مسکونی در کشورهای مذکور برای شلیک موشک‌های زمین‌به‌زمین به‌سوی ایران، از شما می‌خواهیم نهایت احتیاط را…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18633" target="_blank">📅 01:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18632">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
هشدار فوری به تمامی شهروندان و ساکنان کویت، بحرین و امارات متحده عربی:
با توجه به تبعیت حاکمان شما و استفاده از برخی مناطق مسکونی در کشورهای مذکور برای شلیک موشک‌های زمین‌به‌زمین به‌سوی ایران، از شما می‌خواهیم نهایت احتیاط را به خرج دهید.
در صورتی که هرگونه سامانه یا سکوی پرتاب موشکی در نزدیکی مناطق مسکونی خود مشاهده کردید، لطفاً در اسرع وقت آن منطقه را ترک کنید. همچنین از پایگاه‌ها و تأسیسات نظامی آمریکا فاصله بگیرید و از نزدیک شدن یا عبور از اطراف آن‌ها خودداری کنید.
از تمامی شهروندان و ساکنان درخواست می‌شود این مناطق را فوراً تخلیه کرده و بدون هیچ‌گونه تأخیر به مکانی امن و با فاصله مناسب منتقل شوند تا جان و امنیت خود را حفظ کنند. ما پیش‌تر بارها و به‌طور صریح به حاکمان شما درباره خطرات ادامه این مسیر و به بازی گرفتن سرنوشت مردمشان هشدار داده بودیم.
با این حال، آنان تصمیم گرفتند به مسیر تبعیت کورکورانه ادامه دهند و تصمیماتی را اجرا کنند که نه بازتاب‌دهنده اراده مردمشان، بلکه تحمیل‌شده از خارج از مرزهایشان و در غیاب هرگونه حاکمیت واقعی است. بنابراین، مسئولیت کامل تمامی پیامدهایی که در نتیجه این مسیر به وجود خواهد آمد، بر عهده آنان خواهد بود.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18632" target="_blank">📅 01:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18631">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سنتکام:
ساعت ۵ بعدازظهر به وقت شرقی امروز، نیروهای فرماندهی مرکزی ایالات متحده آغاز به انجام حملات بیشتری علیه ایران کردند تا توانایی آن‌ها برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که به صورت آزادانه از تنگه هرمز عبور می‌کنند را تضعیف کنند. فرمانده کل قوا دستور این حملات را برای پاسخگویی نیروهای ایرانی صادر کرده است.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/18631" target="_blank">📅 01:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18630">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">برای عربها تفاوتی که جنگ برایشان به ارمغان آورده این بوده که پیش از جنگ اسراییل آن سو مشغول کار‌ خیر با ایشان بود و ما ادعا میکردیم میخواهیم از شر جهود رهایشان کنیم اما اکنون خودمان هم از این سو مشغول مالش شان شده ایم.  همین</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18630" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18629">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انفجاراتی متعدد در نزدیکی شهر سیریک در ایران شنیده شد: تلویزیون دولتی.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18629" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18628">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32bc32908f.mp4?token=VauOItbHO1Kzay_2a5eGsgsZfAf68EC5DAEXUrrXHVnb2A6P5TdY6ulY9lRxQrXc2IcxeS5FGbUrHjM027lRCrFTLnldB5ikRyjHy_3_wAHKkvXtfWRdPSx4G1jEvPoiqw0z9ynoqQd5qgIJ5mgLlAq5bYN3qCiatzLyrGYKG0q9ByIyHh0hXUlBbNDTzMTWSU2r4PDPnJ4ZYWBnHLZM8GI2YMDuLrnn6bEyncw9G301qaPxGlkO4cBxyjV9IZBaWa3_xh77ncoJDRCVhh3wzKgqiBTgiTUpcSZAK2jdrMDkhhHTQB8jeooy-QVkOvbLParPRng1RtdQUlFV7cvBJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32bc32908f.mp4?token=VauOItbHO1Kzay_2a5eGsgsZfAf68EC5DAEXUrrXHVnb2A6P5TdY6ulY9lRxQrXc2IcxeS5FGbUrHjM027lRCrFTLnldB5ikRyjHy_3_wAHKkvXtfWRdPSx4G1jEvPoiqw0z9ynoqQd5qgIJ5mgLlAq5bYN3qCiatzLyrGYKG0q9ByIyHh0hXUlBbNDTzMTWSU2r4PDPnJ4ZYWBnHLZM8GI2YMDuLrnn6bEyncw9G301qaPxGlkO4cBxyjV9IZBaWa3_xh77ncoJDRCVhh3wzKgqiBTgiTUpcSZAK2jdrMDkhhHTQB8jeooy-QVkOvbLParPRng1RtdQUlFV7cvBJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا این  هواداران نروژی و انگلیسی را دارم میبینم یک جوری فوتبال میبینند انگار هیچ چالش و مشکل دیگری در زندگی شان نیست!</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/18628" target="_blank">📅 00:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18627">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سنتکام:
🚫
ادعا: تبلیغات ایران امروز ادعا کرد که سه نظامی آمریکایی در کویت بر اثر حملات ایران کشته شده‌اند. این ادعا نادرست است.
✅
واقعیت: هیچ گزارشی مبنی بر کشته یا مجروح شدن نظامیان آمریکایی در این منطقه وجود ندارد. تمام پرسنل در وضعیت سلامتی هستند.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/18627" target="_blank">📅 00:04 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
