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
<img src="https://cdn4.telesco.pe/file/j6PzST_iXo0RLwSp6uOcTIH6kHpNRA1-buwUXEUmAwo4mIBlPO1MPk4s67Z2IMKhw1NI7xJYoU9wCS1AeGblvPJDtfswE3bQLOOMSICfQ2IncnsKpVo5tOOIhx0v75IiOQB5qvWOL6KCuwCVOz-1aywQMB3ay2UWevX879SIvkYhrZTwWJBzR1BLabAk1QKy_NVOJ1J_Uk3t7vSJGwN4pvnAiCR0OdnioyFjLhIRNZSFvZ0aP7QCCn2rd90baKrB4inLI8ARr1p_6Ib3OAXAmhNJQsaDeHATClAoyWcWTagtGhKGmaLHajj1Lg1h_S2eouwI8TjJWPtlVrKo2M2F-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.5K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 19:04:48</div>
<hr>

<div class="tg-post" id="msg-19530">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">روسیه حدود 30 هزار تن بنزین از مراکش وارد کرده است تا کمبود سوخت ناشی از حملات پهپادی اوکراین به پالایشگاه‌های بزرگ را جبران کند.</div>
<div class="tg-footer">👁️ 333 · <a href="https://t.me/SBoxxx/19530" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19529">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfMVMwh2tjjfPFhXx_IpSFfjcbsqNV9xobwvfLVf26eRcopTV3DL4dPYAWF6cbGqX-M2TU2rP405IfXvQMWVxX3c7jPRvpJJ8cM34FTFDjtiEmSjg7xQ0vN0CGysBKWlqcxbooj7_yb2-77fGrlkGL0VnAjmH5ozNH6n68VKOHQEZ_QfR17WNa9gq8mcOneYd12wRIOQwFn181-CtpXs8Ouhlm7RoSjxFJZqcEhAPDuewGWua-BRFxxNAa9y1w9W-KNFsTFxbieUElpNY5UJ7KeDqVkLbiahqV-2mfiAz6rIG7Bu3tU-onjB8RmrtnasE7bY00GXXsTpNw7KhI_78A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه ممنوعیت صادرات بنزین را تا سال ۲۰۲۷ تمدید کرد!</div>
<div class="tg-footer">👁️ 331 · <a href="https://t.me/SBoxxx/19529" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19528">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اسرائیل طرح "هیئت صلح" رئیس جمهور ترامپ را که هدف آن خلع سلاح حماس بود، رد کرد. این کشور مدعی است که این طرح برای اسرائیل قابل قبول نیست و اسرائیل هر حقی را برای هدف قرار دادن و کشتن افراد در غزه دارد.</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/SBoxxx/19528" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19527">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">این اسپانیایی ها 700 سال زور زدند تا عربها و بربرها را از خاکشان بیرون بریزند؛ چپ ها در 2 سال دوباره همه آن کوششها را بر باد دادند!
چپ = نکبت</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/SBoxxx/19527" target="_blank">📅 17:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19526">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یک زن وحشت‌زده در سئوتا درخواست کمک از نیروهای نظامی می‌کند و می گوید: "ما تنها هستیم":  ما به حضور نیروهای نظامی در خیابان‌ها نیاز داریم. آن‌ها اینجا نیستند.  ما تنها هستیم.  چطور ممکن است من نترسم؟ من می‌لرزم. این یک تهاجم است.</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SBoxxx/19526" target="_blank">📅 17:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19525">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/SBoxxx/19525" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19524">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlwBwLoH_E_-460M1QDDiZyeq_ZqkpjqrBx1AT-Y2dDEqZEufPvP_E0NZl7bpFN3Hq8sT4m7erBLHyyKh1Jono_9HVrM5v6rolT4ULGaZoe7NfMe7yZLC0GL6qlvEXr_-fVR4lGaiuXwDf4qEQqhgD6OSrXIPOkGMA2Xat8Ka3YlkBQ94tYpeVqGLk23BHrVlgrO-26JIWPIkXY0wMjO0xgHmllMKoTtlYORsiqO_5EAXi48Pu_hd6mhPNsewPBs5wiu1O2mdcjs_kuTPp-Et--UCTvSTRrWm6U1okDVw3SvIq9uPQuljYNV3VhUh00ZbQ0bS3aONwHiuSGHCRQWlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز بسیار بالاست و پیش بینی می شود طلا (و شاخص های سهام) زیر فشار فروش بروند. (خصوصاً شاخص های سهام)</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SBoxxx/19524" target="_blank">📅 17:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19523">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ:
"جنگ با ایران به خوبی پیش می‌رود. ایالات متحده ضربه‌ای سنگین به ایران وارد می‌کند و ما به سادگی به پیروزی ادامه می‌دهیم</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/19523" target="_blank">📅 17:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19522">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/19522" target="_blank">📅 17:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19521">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تنگه ای که استراتژیک نخواهد ماند  وقتی گفته می شود ایران‌ استراتژیک‌ است، بخش مهمی از این‌ گزاره به دلیل اشراف جغرافیایی ایران بر تنگه هرمز است. چون دستکم‌ یک پنجم انرژی فسیلی سالانه جهان از آن می گذرد. ولی گلدن ساکس مدعی است که تا امروز ۷ خط برای دور زدن…</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/19521" target="_blank">📅 16:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19520">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pskd7x3Lzgf-C-yV_TK5V7Oxo9Dvp7ce5QiW5TfgPSp4ODdGgSDcBBRIId4LiegkRuVTK0Da7XIPzP3v91GG_iCrnsQ0cI0ojNXq1xohcLUkwEIqEaJ2LAphDo-yb-6UoWwjOO1XzQh3BkH2elzTqLWahblzdZrx044pEjFnJw5SjBYieQTyNcJBzML8uFPzXPZdh5kn0WNbSBdwSZ3w4JkG3TjSSYKc_Rz_hSWOmLOcVDKCi5CJxJMbU_dTkd7HzZ6OulgAaed2pRAfLOCQ3MusSt1jRCVHik1lSUarjOJaWjTk45T610xmEjGKSzgbjX0-nx77PgIse7fv4oTsVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عصر اقتصاد دانش بنیان، تنگه بندی و گردنه گیری تنها منجر به انزوا و تیپا خوردن خود عامل می‌شود و اندونزیایی ها خیلی سریع فهمیدند که این لقمه برای دهانشان بزرگ است ولی خب.</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/19520" target="_blank">📅 16:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19519">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZwgRO16lPIQym42yuMPiwa1V18fEyXEONii_lZWAk4wVNq6tPUlQoXB-lhQ1uhJvSQQk_LGBemRocQRJu9smDmq6XMJLS5hltgdiAU3hXtACXE_o7u15_W6xJyuldv8isf5dPtmDvr6GsUN3YfLxcC2IqiD0ldX0eiFtnugIC8ehaT7FCmkPIWe_PIpz0ruw6qyxdt_1e-Fv-FqYIAdaaLqu6wB8m7I04si7NszNqomXA8l2_Z8YO4XgoC5e6XwIjL2W9uaH8GKjfKcn62T6v_g_DRIR-NzOLJYjuCvpogZSOTwYG_nDpyFzEMxwtmHVJosbiFBsCJIJe1Tgo_WBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری نظامی اسرائیل-مراکش و پیام راهبردی به مادرید  همکاری نظامی اسرائیل و مراکش دیگر صرفاً یک رابطه تجاری در حوزه صنایع دفاعی نیست؛ این همکاری به تدریج به یکی از مهم‌ترین مؤلفه‌های معادلات ژئوپلیتیکی غرب مدیترانه تبدیل شده است. از انتقال فناوری پهپادهای…</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/19519" target="_blank">📅 15:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19518">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 16</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19518" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 16
جمعه 31 جولای 2026</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/19518" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19517">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یک کشتی حمل گاز قطری که میخواسته از مسیر تعیین شده ایران عبور کند توسط آمریکا متوقف شد!</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SBoxxx/19517" target="_blank">📅 14:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19516">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ایالات متحده و اسرائیل در حال بررسی محاصره زمینی ایران برای افزایش فشار اقتصادی هستند!  این پیشنهاد به دنبال متقاعد کردن کشورهای همسایه — از جمله افغانستان، ارمنستان، آذربایجان، عراق، پاکستان، ترکیه و ترکمنستان — برای محدود کردن یا بستن گذرگاه‌های مرزی با…</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/19516" target="_blank">📅 13:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19515">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ایالات متحده و اسرائیل در حال بررسی محاصره زمینی ایران برای افزایش فشار اقتصادی هستند!
این پیشنهاد به دنبال متقاعد کردن کشورهای همسایه — از جمله افغانستان، ارمنستان، آذربایجان، عراق، پاکستان، ترکیه و ترکمنستان — برای محدود کردن یا بستن گذرگاه‌های مرزی با ایران است تا واردات و صادرات این کشور را محدود کند.
این پیشنهاد در کنار سایر گزینه‌ها از جمله حفظ محاصره دریایی، از سرگیری حملات نظامی یا پیگیری یک توافق دیپلماتیک مورد بحث قرار گرفت.
طرفداران این راهبرد استدلال می‌کنند که انزوای اقتصادی بیشتر می‌تواند دولت ایران را تضعیف کند، اگرچه تحلیلگران اشاره می‌کنند که اجرای یک محاصره زمینی با توجه به مرزهای زمینی طولانی و ارتباطات منطقه‌ای گسترده ایران بسیار دشوار خواهد بود.
— تلگراف</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/19515" target="_blank">📅 13:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19514">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گفته می‌شود عربستان سعودی در حال آماده‌سازی یک تهاجم نظامی بزرگ علیه حوثی‌ها است که برنامه‌های آن می‌تواند شامل عملیات دریایی در دریای سرخ و حمله زمینی در یمن مرکزی باشد.
این اقدام پس از حملات حوثی‌ها به تأسیسات نفتی عربستان و محاصره کشتیرانی عربستان توسط این گروه صورت گرفته است.
منبع: گاردین</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/19514" target="_blank">📅 13:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19513">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
روز دوم تهاجم مراکشی ها به اسپانیا آغاز شد. خیلی از اسپانیایی ها از پادشاه اسپانیا خواسته اند پدرو سانچز را خلع کند و ارتش اسپانیا را به مرز های جنوبی بفرستد.
✍🏻
Desert Eagle
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/19513" target="_blank">📅 12:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19512">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار نظامی ایران و جهان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ff08dba4f.mp4?token=M2vPV7jingSFZt02NpPvTHKkziAKLAWjE6p9pvhjM6xCO_bOf1R_-Z4zGvS3Y9sy6TO_RW96j6HTUe0FN-yGLg0Tw-4swCerW_wAi1EGkrh1-RbYv1zz1T2a3DCcusTBfT2gt9g9nlUxHsmFk8jjY2Zrr7RkaAPO_SseZnmGsqMRwNOjAWwaeedjNH8XZasZMgeI_LCAMOmzxoKW1lqXeqz0uEl5gbD88TzNK2WP2I4lrF2Mbz8BJ3Cuy1w9Sqrtx21TtlwIxurM3W8HipNPsxLN1BG_zUtll-LEXihvUK7PmFzckiKOrDBPfXhORjM5bKKVjEa3pPUzOLBIDXyJ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ff08dba4f.mp4?token=M2vPV7jingSFZt02NpPvTHKkziAKLAWjE6p9pvhjM6xCO_bOf1R_-Z4zGvS3Y9sy6TO_RW96j6HTUe0FN-yGLg0Tw-4swCerW_wAi1EGkrh1-RbYv1zz1T2a3DCcusTBfT2gt9g9nlUxHsmFk8jjY2Zrr7RkaAPO_SseZnmGsqMRwNOjAWwaeedjNH8XZasZMgeI_LCAMOmzxoKW1lqXeqz0uEl5gbD88TzNK2WP2I4lrF2Mbz8BJ3Cuy1w9Sqrtx21TtlwIxurM3W8HipNPsxLN1BG_zUtll-LEXihvUK7PmFzckiKOrDBPfXhORjM5bKKVjEa3pPUzOLBIDXyJ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
روز دوم تهاجم مراکشی ها به اسپانیا آغاز شد.
خیلی از اسپانیایی ها از پادشاه اسپانیا خواسته اند پدرو سانچز را خلع کند و ارتش اسپانیا را به مرز های جنوبی بفرستد.
✍🏻
Desert Eagle
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/19512" target="_blank">📅 12:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19511">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bckTSMBeY8MLsCjfoY2QnVprQ_FHIMdZOWASkjaI3WmLgOtF2o198SKi8EsfcmSW3-KEmqKgxYyvd7j9ueWUQso-Je8nQ2yu1KX9ElwSPoaUD_VaRrgWwa1j4MR3ofjH-90gGoAY0EBHtPnxNLhU1qX0OnpzbM7AQzd8YhExjaF_-lvF16AY6BwWcv2rdjWvZkHizGHCvymzmojEgFd2Rinmf2K9HU68-t9TNtQDypubabfx-tolxSQIfuIzJv5hnPQGAK9aIF2uLrHhI4llj19veWhCQ2BIvhrq0dRJX6S2VZHQHlDqYGo9blUaRwW2KeYq4BIpv_oGcfDfuq2Iog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/19511" target="_blank">📅 12:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19510">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خب سیگنال پایان موج 2 از 5 دارد صادر می شود:
استاد خوش چشم: فک نکنم‌ دیگر جنگ بشود</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/19510" target="_blank">📅 12:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19509">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پلیس:  زائران بازگشت از اربعین را به روزهای پایانی موکول نکنند</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/19509" target="_blank">📅 11:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19508">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پلیس:
زائران بازگشت از اربعین را به روزهای پایانی موکول نکنند</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/19508" target="_blank">📅 11:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19507">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/19507" target="_blank">📅 11:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19506">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyFXfRNoqlaxV56bDhHn163FhayJFojIaqhaVh3cJwuh-aMyWJBecrhagD4qeJ7ddo6NRJG8liKZJpDYJcPlHGTpWcyFB7RvSzg71Jl4KCjn0H6U3NhWC6v1CYCtz0HMx6PmnQcvdsw9zii2u-ay8ubBwQRC45U8iGF8PlfkK2yzLCkRw7OkQcoitZN5f44O0sGtJYWGg-DxI1STN2XBmso5qBUpnpeo8AmglIiYlksfucmslJ_NUsb4EdqXiEBNiUkMCEVpSKg68ymydebdBjLlEaNSuKtof5ZE6Ak-z4GafzGMCOjZnYTrWsZr463nZzsEDft18RXVlNUiSWFHPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز بسیار بالاست و پیش بینی می شود طلا (و شاخص های سهام) زیر فشار فروش بروند. (خصوصاً شاخص های سهام)</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/19506" target="_blank">📅 11:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19505">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afWQRPlAAHjYlHyY0y7lbLY2amo_Beu7Jx1db-aIXtF-dp-yKGU0nkep7xNArOJNshNRwIw7jDhERT4W9tgnz2z_H_KpiEQ0-iVneMjxknWJgtSIshomKVKn7LFMXX5-VAMXkLoZwk4WvhkAWOyUlVKGeBpRaG8WUyi1i3y2sbLOkEaE35-PcPfV0QaTOMpamao9HUOfx1gUYyTa2kOfaJiM4ucft3zLIaPe7_xo26HqSEOITZLM1NnMD7-GY_UT3I3QUpSDypYY9HObcDCS6_vVWjOy_a439BGJTKECsDIZwQomqO0rkbB6C4xMT10hH46GRMwXbflbpusd3YmNtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح میانه پایین است و حالت رنج برای طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/19505" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19504">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شلیک موشک از ایران</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/19504" target="_blank">📅 10:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19503">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مجری
: آیا می‌دانید چند روس در این جنگ کشته شده‌اند؟ آیا تخمینی دارید؟
زلنسکی
: مجموع تلفات روسیه ۱,۶۰۰,۰۰۰ نفر است و حدود ۷۰۰,۰۰۰ نفر کشته شده‌اند. تقریباً.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/19503" target="_blank">📅 10:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19502">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">قالیباف:
ایالات متحده هر روز دست‌های خود را با جنایت جدیدی آلوده می‌کند؛ حمله تروریستی به خانه‌های مسکونی غیرنظامیان در جزیره قشم ادامه‌ای بر فجایع میناب و لامرد است.
آمریکایی‌ها عادت کرده‌اند که با ریختن خون بی‌گناهان، برای ضرباتی که در میدان نبرد دریافت می‌کنند جبران کنند.
آن‌ها بهای آن را خواهند پرداخت.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/19502" target="_blank">📅 10:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19501">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ اعلام کرد که حماس به طور کامل سلاح‌های خود را تحویل داده و غزه «در دستان یک دولت فلسطینی جدید که در خدمت مردم خود است» قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19501" target="_blank">📅 02:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19500">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مجری فاکس نیوز:
آیا کشورهای دیگر در منطقه که توسط ایران مورد حمله قرار گرفته‌اند، در حال تماس و تمایل به شراکت با اسرائیل هستند؟
نتانیاهو:
بیشتر از آنچه فکر می‌کنید. بیشتر از آنچه می‌توانم بگویم.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19500" target="_blank">📅 01:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19499">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نصب سیم خاردار روی پنجره ها از سوی مردم اسپانیا برای مقابله با موج سرقت و جنایت مهاجرین آفریقایی</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19499" target="_blank">📅 01:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19498">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THb73ViXAh_Jf0dHwWEOC5vAwvlUgr87H2y6DMOXXFT_654ww8o-Nkto1RJ6vgwWwJQ6Rc_VyfzuzMwbBEQ8UdZ_cjyC04wCFVyhUAM0iTFV2VuNhORVgBXkOyIOP3DnKgeCL8U0neiclDFR8WcJRwqbWWfvpMx-VRoZvB4TYMsVpJi6VBoARGYw83CzA8WVkBMYf1PP6E7xDTVjx5HpNzr4xvOkAx4fCjgzm3n1-o7Nz3oXfIPt8Y8FNztVGJnWx2pYfp-DhHpby3tKEDCUyg8bx0qJ3RC381q_Vz3fs92WnaC9KBxBMXTsZcKhWyPYM4hRnUl24dfOKT2h4FMqsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19498" target="_blank">📅 01:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19497">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">▶️
Snow-like dust covers towns across southern Lebanon following violent Israeli explosions.  @PressTV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19497" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19496">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPress TV</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d0fce5d57.mp4?token=ccUfI1Kw-bYg-dh6kpirIlWxRExhMviK1-2D75RVUsB7xbjD4cSsKnez2W9NqyR0xCOY8lIPXQV1jqgiifqHGm2liZVdqJQDkyIg8z28fDsYysW6kLrsaDZ3d75NPeQ_lVKW0dCHQ1BgBIZCfzCt_wmmZh61sUjPtP5FawGJXxabZPaxxqChYfa4Xj5Njv9qCw5ltUmywZhllG3kLmNZeb4IWHrHXHzTd2K9qoYY7LoIn7xj1lVS2kHFTxIHCx1fN1AqD-eB-msUh8KBrQo8NJZfOQhyKq4Gg8mJ-24B1FfYSM98UA2mXWVbLI1PuDjyiWWUNPqarT2xUdiyvi8V6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d0fce5d57.mp4?token=ccUfI1Kw-bYg-dh6kpirIlWxRExhMviK1-2D75RVUsB7xbjD4cSsKnez2W9NqyR0xCOY8lIPXQV1jqgiifqHGm2liZVdqJQDkyIg8z28fDsYysW6kLrsaDZ3d75NPeQ_lVKW0dCHQ1BgBIZCfzCt_wmmZh61sUjPtP5FawGJXxabZPaxxqChYfa4Xj5Njv9qCw5ltUmywZhllG3kLmNZeb4IWHrHXHzTd2K9qoYY7LoIn7xj1lVS2kHFTxIHCx1fN1AqD-eB-msUh8KBrQo8NJZfOQhyKq4Gg8mJ-24B1FfYSM98UA2mXWVbLI1PuDjyiWWUNPqarT2xUdiyvi8V6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
Snow-like dust covers towns across southern Lebanon following violent Israeli explosions.
@PressTV</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19496" target="_blank">📅 01:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19495">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه ایران:  "مصر یک دوست و شریک مهم در منطقه است و امنیت آن برای ما از اهمیت بالایی برخوردار است.  ما همگی باید در برابر توطئه‌ها و عملیات‌های فریبکارانه اسرائیل که با هدف تضعیف صلح منطقه‌ای طراحی شده‌اند، هوشیار باشیم.  تهدید آشکار،…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19495" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19494">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">به نظر می رسد مصر هم کم کم به لیست اهداف مشروع ما بپیوندند.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19494" target="_blank">📅 00:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19493">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">عربستان سعودی ائتلاف چندملیتی برای محافظت از مسیرهای دریایی کلیدی را اعلام کرد
عربستان سعودی تشکیل یک
ائتلاف دفاع دریایی چندملیتی
را اعلام کرده است. هدف تضمین آزادی ناوبری و مسیرهای تجاری بین‌المللی در
تنگ باب‌المندب
، در
دریای سرخ
و در
خلیج عدن
است.
بر اساس وزارت دفاع سعودی،
۱۴ کشور
در حال حاضر از این ابتکار حمایت می‌کنند:
بحرین، جیبوتی، مصر، اردن، کویت، مالدیو، پاکستان، قطر، سومالی، سودان، ترکیه، یمن، عربستان سعودی و شورای رهبری ریاست جمهوری یمن.
بر اساس وزارتخانه، سایر کشورهایی که در مشورت‌ها شرکت کردند، در مرحله نهایی رای‌گیری‌های سیاسی داخلی برای پیوستن به ائتلاف هستند.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19493" target="_blank">📅 21:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19492">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">— منابع یمنی معتقدند که عربستان سعودی در حال آماده‌سازی برای یک تهاجم نظامی بزرگ علیه حوثی‌ها از طریق دریا و احتمالاً از طریق خشکی در یمن مرکزی است تا گلوگاه صادرات نفت خود را در دریای سرخ جنوبی آزاد  کند.
— گاردین |</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19492" target="_blank">📅 21:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19491">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وزارت دفاع آمریکا، قرارداد ۵۸ میلیارد دلاری برای سیستم پدافند هوایی پاتریوت به شرکت لاکهید مارتین اعطا کرد.
این قرارداد به ارزش تا ۵۸.۶ میلیارد دلار، مربوط به موشک‌های رهگیر پاتریوت است و تولید این سیستم را تا سال ۲۰۳۲ افزایش می‌دهد. این اقدام در حالی صورت می‌گیرد که درگیری‌های مداوم در ایران و اوکراین، ذخایر سامانه‌های پدافند هوایی آمریکا را کاهش داده است.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19491" target="_blank">📅 20:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19490">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">329.6 KB</div>
</div>
<a href="https://t.me/SBoxxx/19490" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 15</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19490" target="_blank">📅 20:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19489">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19489" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19488">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">در صنعا توفان و رعد و برق شده، فکر کرده اند عربستان حمله کرده !</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19488" target="_blank">📅 19:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19487">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رهبر حوثی‌های یمن، عبدالملک الحوثی، درباره عربستان سعودی:
آن‌ها دام‌ها را نابود کردند؛ شترها و گوسفندان. حتی حیوانات بارکش و الاغ‌ها نیز از رژیم سعودی در امان نبودند.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19487" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19486">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19486" target="_blank">📅 18:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19485">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-ju_rwPn0ReGIULEw0IQAGQwAHLrFFJbEeSy5x9mIsRHFnA1-xv0SG_NJi8-Nj9Y3pTCH0T1pFLj-cn_0MnCKHZKoRUWsns3vgP9oLIT6ZWsfmzIWHliy9cpFR8a41juvou1bMVQMPBzjxddzjNdqDWtIj9yfKU3APpjEOKZvUyQO6-pES9QjpucqdL7oNgMYLB2KfPLxU55FLx6MAYGvK4KOEu-QS4xjFHdVBDW5QQ1C_VvQh3r-KOJg8Fo_9IzKOTXAQr80nyVqG9XeySMfGABfnsSEExd_1hCeeT_nhkgI3hnhypUmEYwHsjaNZOPvPH5v6ByI309GB-Tg0nTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما ببینید در روزهای اخیر اینها به لیست اهداف مشروع ما افزوده شده اند:  — بلغارستان — بریتانیا  — اوکراین</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19485" target="_blank">📅 18:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19484">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUXP0I7-5NrdkJf_gkBYdJ-Kn5tSHhcB_qraUr5pb1PFwju-DAm3eWf-hCx2IDa152nWT35bs4T53aUaKjVXEAPGa13h8yT2i-vQoWqTtmmTKcnClTb0e4ph-VUWzYkU4O8GLpSTpKiCxx1oWJbm2kF7d9r_eoYW7OzGDUYiMWdksA7is_OXLeqyqJXRBwt8TrHTJ6wpTVgMNkb_EhRjv2VObQgsHGwJ9_vj-8R-2XLmyiwl83lBu-GDZz5NZ8Cro8FsvyTqV0lrHHEdVdIYoID5l69YMiBONKhkQOsfLwGaF9r2SWVpc_B8kJL2uMU_WzyjYTAylOPiwpb3arfSnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19484" target="_blank">📅 18:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19483">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">روسیه ممنوعیت صادرات بنزین را تا سال ۲۰۲۷ تمدید کرد!</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19483" target="_blank">📅 18:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19482">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">— مشاوران و اعضای کابینه ترامپ گزینه‌هایی برای انجام عملیات نظامی گسترده‌تر علیه ایران را به وی ارائه دادند.
— فاکس نیوز</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19482" target="_blank">📅 18:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19481">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سپاه پاسداران: ایران پایگاه هوایی الازرق را در پاسخ به حمله آمریکا به قشم، با نابودی سه فروند اف-۳۵ حمله کرد
سپاه پاسداران انقلاب اسلامی حمله موشکی انتقام‌جویانه به پایگاه هوایی العزرق در اردن را پس از حمله آمریکا به خانه‌های مسکونی در جزیره قشم اعلام کرد.
طبق بیانیه سپاه، این حمله به منطقه استقرار و محل نگهداری اف-۳۵ هدف قرار گرفت و سه فروند از هواپیماهای اف-۳۵ را نابود کرد و سه فروند دیگر را به شدت آسیب رساند. چندین افسر آمریکایی و پرسنل فنی نیز کشته شدند.
سپاه گفت که این عملیات در پاسخ به حمله آمریکا به قشم انجام شد که منجر به زخمی شدن اعضای یک خانواده محلی، از جمله کودکان، شد.
در این بیانیه همچنین از اردنی‌هایی که با حضور نظامی آمریکا در کشورشان مخالف هستند، تشکر شد و گفته شد که موضع آن‌ها فشار بر نیروهای آمریکایی را افزایش داده است.
سپاه در پایان با تأکید بر ادامه عملیات علیه حضور نظامی آمریکا در منطقه، بیانیه خود را به پایان رساند.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/19481" target="_blank">📅 14:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19480">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کشته شدن ۳ عضو سپاه پاسداران در حمله آمریکا به زنجان</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19480" target="_blank">📅 14:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19479">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 15</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19479" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 15
پنجشنبه 30 جولای 2026</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19479" target="_blank">📅 13:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19478">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgV1CfJIAhUGDo1cKlTIibxtmZBV3ZdBLpTz5GA0Yv0D0HoG7bvZbbQdMcMx30BOyX9ph0KFLYxUuqj4R-TecsjFwvK_oIuAXb2N286KSLmoaR_wX0PjcQu6M5pEzPSQSWL14-s5XyKxECxF6u_L5AD0vbKCDso-cEaVC6qclPd8nqGHWnVSt1p6DqFKTZPrCDDH4ja9XyHLCpPNqLGT-Abn0lV9oZE06BcI0f_bbftDGNZ2xffTbGDKlsPlM214Ab-UkVjtX90nSH8-hbuVSJoeQgUmP3LMqvC1IAk4HG7FuoE-hMWiSjQgJlYo3wMXkqboPY4WcbRTCievZiiROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لینک نشست دیروز با نیما</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/19478" target="_blank">📅 12:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19477">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8eacd406a.mp4?token=MunsSUdBx8QUaJx3Wtji3Us3abtEpBKrbk_5PzMG-neL-F86pEYBsThQSlmoyKrwEm_F5EJQyIc1ngeOm9ELrQkapSFo55iaN3dnuKsn3Uz_MsydCZQSFxManXNUP-XCHwQ3EAETzVcmFCVQxpeXva8gonPmcoNRh_rcMtxiFEbsWnCIR9wEhBFRzutSg_NKS4SXneXm2wwif2DLlwhxzPO7KoxR5uT_uQj0LCu44kNX1rzmcYjtGTPFAyWiRSkuNeKJxWNeRVA0421zye72RKW8GXaT2wfLdotxg1la15VKAfqtUpjNIi_t4JKpUQBpRKifkOO87hkloZgS5d4byw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8eacd406a.mp4?token=MunsSUdBx8QUaJx3Wtji3Us3abtEpBKrbk_5PzMG-neL-F86pEYBsThQSlmoyKrwEm_F5EJQyIc1ngeOm9ELrQkapSFo55iaN3dnuKsn3Uz_MsydCZQSFxManXNUP-XCHwQ3EAETzVcmFCVQxpeXva8gonPmcoNRh_rcMtxiFEbsWnCIR9wEhBFRzutSg_NKS4SXneXm2wwif2DLlwhxzPO7KoxR5uT_uQj0LCu44kNX1rzmcYjtGTPFAyWiRSkuNeKJxWNeRVA0421zye72RKW8GXaT2wfLdotxg1la15VKAfqtUpjNIi_t4JKpUQBpRKifkOO87hkloZgS5d4byw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبور موشک های زمین به زمین اتکمز آمریکایی بر فراز شهروندان کویتی به سمت شهرهای خوزستان</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19477" target="_blank">📅 11:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19476">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diiKsv7TIuNKhkKzaHKIcYDHT8Sbi1dWhswTigbfHAHQup2sNiF0X-56Eq-_gwwN4Tn3_KhNQ8KSM2qEwr0FP25TEQ5oEZuSfhT_dhaC_rgrihxy0TEccOQah4RP5uiunQCQxibWUqPq6PpmwlgXknZ8yCSajhGxYFBkXsgio_g9bQfTYnaOh38EJWPUwsvNoc9EMb-VS2zNZLu0GnhMckk_-jPZvufItzrzPx-2r1TIFk4Vt0ync7C7gFD2KUCrXGxBSf_PGzWuZiNPNukEPGBaIIxiHBLNkSEhnwkY2z44uLRI3vE2o8oPkYw_VStvuHVumfj1WqNzz2d9Wn83qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این همان حرامزاده ای است که دختران را در لایوهای خودش کتک می زد و به آنها اهانت می کرد که خوشبختانه به این روز افتاده و تا مدتها نخواهدتوانست شرارت کند.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19476" target="_blank">📅 11:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19475">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahLOh0WXS3Urvw9S-amWzdZLLKU7hdFStUJziq88xW5DI1A83LHKo9QT-81fd_bfNkWokFWabnmWFLPPkprxtq_9zWYLhHsZy9lgSlztRnkzYNj09rrbPJkPk84VENRztNRnBzmBeH1G8nofPcR4nP3-BRCwLWKsY4GG4w9K2SdYN7tvdo0wGyU1TPQ91DDmbQmAtnQPvSDDbtZgUeNLI4k97C0cv-kF_CdSaLDqlUHse5uqB0YUhTW4xXcuLrpv8HLOYiLByYcrT3jqZzIlCJ808rrl9hz1Yhr66Slng-k5BnCHfxLxhnVClHKOpRCX3Bh4uYV8kDxc4d1YrNl0IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدها چهره سیاسی، حقوقی و عمومی اردنی، نامه‌ای سرگشاده امضا کرده‌اند و خواستار خروج نیروهای آمریکایی از اردن شده‌اند.
آن‌ها حضور آمریکا را یک خطر امنیتی، سیاسی و اقتصادی می‌دانند که این کشور را به جنگی می‌کشد که تمایلی به آن ندارد.
این یک اقدام نادر و علنی است در کشوری که به شدت سرکوب‌گرانه با مخالفان برخورد می‌کند.
اکثر رسانه‌های اردنی از انتشار این نامه خودداری می‌کنند، و برگزارکنندگان هشدار می‌دهند که امضاکنندگان ممکن است به زندان محکوم شوند.
خشم عمومی در حال افزایش است، زیرا ایران همچنان به هدف قرار دادن حدود ۴۰۰۰ سرباز آمریکایی مستقر در اردن ادامه می‌دهد.
آژیرها در سراسر کشور به صدا در می‌آیند، و بقایای موشک‌های رهگیری شده در مناطق مسکونی سقوط می‌کنند.
این هفته، در پارلمان، یکی از نمایندگان به دلیل پیشنهاد تسلیت برای سربازان آمریکایی که در خاک اردن کشته شده‌اند، مورد انتقاد شدید قرار گرفت.
یکی دیگر از اعضا، ارتش آمریکا را به کشتن "کودکان، زنان و سالمندان" متهم کرد.
دولت همچنان به این ائتلاف متعهد است، عمدتاً به این دلیل که واشنگتن سال گذشته ۱.۶۵ میلیارد دلار کمک اقتصادی و نظامی به اردن ارائه کرده است.
اما جنگ بخش گردشگری اردن را نابود کرده است که تا ۱۸ درصد از درآمد سالانه دولت اردن را تشکیل می دهد
منبع: نیویورک تایمز</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19475" target="_blank">📅 11:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19474">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5MwvoInAZHC3vmpYspGyAQ6hPKq0cosUyeNkGUBYEHg2P9arNh5hz2Si3W8IUh-sFRwEOGDFHRdXUh5Upf-4dIiX7BMuSKhoS-Zf9q6nLprTEPADvCr1RwcouzIbijKr5nFpVlFn5Rgu56snFpQbsPeC-IVjNCJbhLmDG2XkGNEWel7bgOfhAEf0F0zPrSiOzXwRZovlH_t3EXlSwXUanPjSpRU2LMvu3mwk3HpgXddO9j3x1aNv_ApmH9lbQMQFzRv2Baqq2jTrPrfKaDKC05FSVFqBRbfEmqXxXPOOsfdes8i2qxJeUkvllDdBvrZeVWbEbckHxeQbL17D6g5RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهداف حمله پریشب حمله مشترک سعودی و آمریکا به پایگاه های حشدالشعبی در عراق</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19474" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19473">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سپاه پاسداران:
با استعانت از خدای متعال، متجاوز همین امروز تنبیه خواهد شد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19473" target="_blank">📅 11:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19472">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMVTrXM7nxmk3IYJhEoIyzmnMWTxQb09NalNVKMaJ6shzwKkNXHU-1lUMP8Cl7kolEkgJ9Q0eKZbDPbx0eT-oySN64YaamCrk-O3BHbvlBvRADgyjIACT2yc_GFs1DsqGEwaPL7fppuRP-0IglRQYya9MlCIk_HWKvYuOTulmvLATdX3lYeC0v1iJXAA5mqO4WiA1ZxFKs9Jbt15fop0yDprc8eciOeZuRecfP2DSH3SmWwOHUhW_0pYrp3IhK7ZaKiSZCz7d31fYdLUHES_XBaUNfYMYeUcylV-9jfEtiAFABIrpYtERL_Yo3J1PGu20ViNovGAuBBgOl_Ykn5u2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح میانه پایین است و حالت رنج برای طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19472" target="_blank">📅 11:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19471">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19471" target="_blank">📅 10:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19470">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پرسش: اوایل این ماه، رئیس‌جمهور ترامپ در مصاحبه‌ای با یک خبرنگار گفت که در رابطه با شما، همه می‌دانند که چه کسی رئیس است، یعنی خودش. او کسی است که تصمیم‌گیری‌ها را انجام می‌دهد. آیا شما هم این‌طور فکر می‌کنید؟
نتانیاهو: خب، شما می‌دانید که در آمریکا اغلب می‌گویند ترامپ هر کاری را که من می‌گویم انجام می‌دهد. و در اسرائیل، اغلب می‌گویند من هر کاری را که او می‌گوید انجام می‌دهم.
و گاهی اوقات، این مسائل توسط هر کسی، از جمله رئیس‌جمهور، در بحث‌های عمومی مطرح می‌شوند. اما حقیقت این است که ما شرکا هستیم. ما متحد هستیم.
او شریک ارشد است. این کشور ایالات متحده آمریکا است. بیایید این را فراموش نکنیم. و من شریک فرعی هستم، اما من نخست‌وزیر اسرائیل هستم.
و وقتی لازم باشد، من برای دفاع از منافع کشورم و امنیت کشورم، این کار را انجام می‌دهم.
منبع: خبرگزاری ABC News</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19470" target="_blank">📅 10:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19469">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نتانیاهو:
ترامپ اساساً سه گزینه پیش رو دارد: اول، دستیابی به یک توافق؛ دوم، ادامه محاصره؛ سوم، اقدام نظامی.
هر چیزی که منجر به پایان برنامه هسته‌ای ایران شود، چیزی است که ما می‌خواهیم. این هدف مشترک ماست.
س: وقتی با ترامپ در کاخ سفید ملاقات کردید، آیا تلاش کردید او را متقاعد کنید تا حملات به ایران را از سر بگیرد؟
نتانیاهو: در واقع نه. این یک تصویر کاریکاتوری یا تصویری اغراق‌آمیز است. این درست نیست.
ما در واقع تمام سه احتمال را بررسی کردیم، و من فکر می‌کنم که این کار را به صورت شفاف و در بین دوستان و متحدان انجام دادیم.
و این تصمیم اوست. این تصمیم اوست.
منبع: خبرگزاری ABC News</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19469" target="_blank">📅 10:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19468">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شب گذشته یک منزل مسکونی در قشم مورد اصابت پرتابه آمریکایی ها قرار گرفت  احمد نفیسی معاون استانداری هرمزگان از حمله دشمن به یک منزل مسکونی در محله چاه‌تنگو شهر قشم خبر داد و گفت: تیم‌های امدادی در حال جست‌وجو برای یافتن دو یا سه فرد محبوس‌ در زیر آوار هستند.…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19468" target="_blank">📅 09:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19467">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فیلم سنتکام از هدف قرار دادن اهداف در حمله بامداد
چند پرتابگر متحرک نیز دیده می شوند</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19467" target="_blank">📅 09:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19466">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حمله موشکی ایران به اردن</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19466" target="_blank">📅 09:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19465">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شب گذشته یک منزل مسکونی در قشم مورد اصابت پرتابه آمریکایی ها قرار گرفت
احمد نفیسی معاون استانداری هرمزگان از حمله دشمن به یک منزل مسکونی در محله چاه‌تنگو شهر قشم خبر داد و گفت: تیم‌های امدادی در حال جست‌وجو برای یافتن دو یا سه فرد محبوس‌ در زیر آوار هستند.
احمد نفیسی خاطرنشان کرد: جزئیات تکمیلی این حادثه و وضعیت افراد گرفتار، پس از پایان عملیات امدادی و ارزیابی‌های میدانی اطلاع‌رسانی خواهد شد./ایرنا</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/19465" target="_blank">📅 09:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19464">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شهرهای مورد حمله قرار گرفته از ساعت 3.5 بامداد
🔹
قشم
🔹
اهواز
🔹
بندرعباس
🔹
آبادان
🔹
اروندکنار
🔹
شادگان</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19464" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19463">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شهرهای مورد حمله قرار گرفته از ساعت 3.5 بامداد
🔹
قشم
🔹
اهواز
🔹
بندرعباس
🔹
آبادان
🔹
اروندکنار
🔹
شادگان</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19463" target="_blank">📅 09:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19462">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حمله به آبادان</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/19462" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19461">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpDe-NUUX8pOjuAsRfzRK7lsHKko8Mm3GQ_D0Cz81elQXsOA8MLoYihdchsJrXQfvo33BV2nZkij3DCJCKpK6EwRFga1gM26t3vLCDKeOthz9BSMCJR8XAHNJ3V5KAFsMA3CVmqG0Kl8OtN7lMiikFqz8XlWANB9ZVoTEExONZo26w4xNa-uSLl8XhrAFUkB44jzEe_cavX91DwevShvtqS3SlxaF0aqs49O5ji2P3W5vIdh7CIZJEDQMAfmXGNqkJ8cpwZju8fPQm1DFendmf4_b7-DxFFMY0dvWdDQvG8izeIgbWEcmUoqYyskGHElKd1B03xl7COZD-Rco-e77A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات آمریکا تایید شد</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/19461" target="_blank">📅 02:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19460">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">چندین انفجار در ریاض، عربستان سعودی، و بسته‌شدن باند فرودگاه پادشاه خالد در ریاض.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/19460" target="_blank">📅 01:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19459">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجار در اردبیل و ارومیه (تایید نشده)</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/19459" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19458">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddFWussafIBdCiyWa_sIMyG2fJNNFJJxwkTguQyE818gO-fwRp4_yYckp86o3UlObIz-IFG8gXhnsCMSvG5Gqv7k9L0lXO_Treowa3B_SJJk2GCtwhc0p5wNvidU4pIhUlHpnxDVt5f-TSPyRdRhXuAnWEGRK_VDU0gR6_GL_Di6_T1tX-x7lEWi3IilTbtloRKHjZXaqc2qxut5DFJKIwpVL_INX9dTGtLGzYkCbR9F8aKd_kJvxHOAxQheWKqLaaoycSDN-P6emLf8YrjUqfsbYHp2IyHaxFOFVgomUpD5UX1MbCMTdJGncfIkeiuJJ8yTMU8GnJ7UAxQSzcWDHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا که اخیراً محبوب حضرات شده بود و چهره یامال را روی موشک ها میزدند، اعدام های اخیر در ایران را محکوم کرده و خواستار تعویق اعدام های برنامه ریزی شده شد.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/19458" target="_blank">📅 00:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19457">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5Q0XhEXhhO5y3oIpqDQBaKP2F6jZJjcHePO66dpF7zy5n0J-KYLxSu71RNBCgnepEClHfE9BPGkiWsfJ-4aKbIOs1EboRmSsY0G3OmM00NoOUUKIvEUS6Z1wuApOuAQ4gQkzkZoWTg1EFEkr-C-hCmZXSiVRuDYMLdDCVFrY8YbZ9EZOvDWsDSWIg_aHTeYSY3Ktl30TYuMEZ11a2G_SAVOYUzzNO1vGx7vISCJR7zHKaXwASVn7QCR9VxyV_XkYb4DduH12VFa-jcaiOz2F9n4nOo3seWxni9dJFcT3EzaWZ6Vd6sqjqHgrCRMW36b-ZtOOs6TNjg6rr0trplkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا که اخیراً محبوب حضرات شده بود و چهره یامال را روی موشک ها میزدند، اعدام های اخیر در ایران را محکوم کرده و خواستار تعویق اعدام های برنامه ریزی شده شد.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/19457" target="_blank">📅 00:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19456">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRDDWplA7XX43uhQiIxoc814Bkr-HHtJ4jfHw2-xxOH1Ty_9uJ2aR8GizcQtAhD4oFjzTOCwr9qFeQ7cp5lw9xOT6E2KvzNh0XPgU2dlJGhWluENMJ8W9S77bEuBHXUw1CSDFfkkPQOkbJyLw6mH8FoM6R3oyGeIhGGm87cr7peb-RjMUnMa8xVtr2hP39J0IYvkfhIrY6soQVC53C_lfYDCQgLrYq82SfsKsAsUUmHGDXgI8r1xRwZNHCLwzA4V1odhUGtkyx__77Fy1E1m60ofqyXY1yan9gSrxRSxF2ocCYACKuTGyOLQfG7fVLvY6eDV_T8WsLVPYG_MX5iO-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیدوارم آن یک هواپیمایی که نزدیک تهران است جنگنده نیروی هوایی ما باشد.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19456" target="_blank">📅 00:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19455">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر
به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19455" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19454">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FodQ4sLEeYuuTbnldKqDjjPtTD4CLznxmF39ez-M6IZlNbGU7jPIgkcLayJ9tFYDlx9ZfzoML8yJqRNTf_Lrn5B1RCInnx3-TBsrGqMT40muDvXYTEdkle3d3b-PELdlEg0GXRiKXPF4GNsXn-tLMUG9yQ7c5KUI7azrqqjVMk1LlQpwHICpzmEKxpF5B6zSsqFcPIGZNo5i8yYursTMRg62j3d_L72OYbbKv5vZV2wkQBaCw0Ukd4cUmI4skUN5furljTJQ1NVbglYH0pRTz88MvGRDX-wX_cIAGy05lVMegLHhQNb1nwCAYRn0zWizCsmDAcEu2JPb0nn4atrqmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز هم در وضعیت مناسبی قرار دارد و انتظار رشد طلا می رود.  دقت کنید که امشب نشست سرنوشت ساز FOMC را هم داریم که سناریوهای موجود در این یادداشت بررسی شده است.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19454" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19453">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3185a6e49f.mp4?token=VIHhjZBBvN8bA37GdzpXrVK0pWp8wJUu7Rmio8znlsJk_acuEN6smuXEOBa1dDZwrqBf09Cc7jU1gEGh81rdl0u1tWrydK0iPAX5e0XaM1lKVSwcrnwkadib_yw-kLkiGWW0u1oXjU13OErs5VyT8wEujVOei6DrevjgFpA1QPc-XQYq8JpgH_YSOSy2r2-Bwd-ziV0IFx71-OKo2GTUV-NrWyRnDvVvepNV0n6FjT6AsQXiEEWH5GkUAi1UZ1XunWgqsSJiOHG_yb9QyQBEH8mDVhI58q8pqiDUfXMUlP48z3iUx55jyfm-MSEXPY6XKyBjMVkmUf6wu-EFQk1u7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3185a6e49f.mp4?token=VIHhjZBBvN8bA37GdzpXrVK0pWp8wJUu7Rmio8znlsJk_acuEN6smuXEOBa1dDZwrqBf09Cc7jU1gEGh81rdl0u1tWrydK0iPAX5e0XaM1lKVSwcrnwkadib_yw-kLkiGWW0u1oXjU13OErs5VyT8wEujVOei6DrevjgFpA1QPc-XQYq8JpgH_YSOSy2r2-Bwd-ziV0IFx71-OKo2GTUV-NrWyRnDvVvepNV0n6FjT6AsQXiEEWH5GkUAi1UZ1XunWgqsSJiOHG_yb9QyQBEH8mDVhI58q8pqiDUfXMUlP48z3iUx55jyfm-MSEXPY6XKyBjMVkmUf6wu-EFQk1u7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک غیرنظامی اردنی به طور تصادفی، فیوز انفجاری یک پهپاد انتحاری ایرانی مدل "شاهد" که سقوط کرده بود را هنگام بررسی آن، منفجر کرد.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19453" target="_blank">📅 00:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19452">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
ارتش اسرائیل آماده حمله سراسری و بزرگ به ایران است</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19452" target="_blank">📅 00:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19451">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارش‌هایی از پرتاب موشک بالستیک از اطراف یزد در مرکز ایران</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19451" target="_blank">📅 00:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19450">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ درباره ایران:  آن‌ها می‌دانند که این اتفاق (حمله) در راه است. از ما می‌خواهند که این کار را نکنیم.  دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/19450" target="_blank">📅 23:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19449">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ:
آندی برنهام باید به مهاجرت اشاره کند زیرا این موضوع بریتانیا را نابود می‌کند.
آن‌ها از آفریقا، آمریکای جنوبی و بخش‌های مختلف آسیا می‌آیند و در حال حمله به اروپا هستند.
این یک حمله است و بریتانیا مظنون اصلی است.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19449" target="_blank">📅 23:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19448">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iX4DZGCuPZwykShgJXNADS3ceFyWePLUyTZ7-4cDq5F3pMH21WzHxuoWSuL4v_aoLXA9rM7erZaghLjDopYt3dKPu-zS9WE_SSLavrm_XoX67VMVLKzuctf2l33XEgqswl4xyh_VbrzAqR9Ybt9JWQ20r7XdxwfwMSFM1rRwHpgsp3Fa_PbFdt7qv_dpkQ9b-m-PXTMiK92P-Pdv7nh2CfP7N-T7bPEZqfS-vwNEoUaC_kAW_8KVQVEPI8vxpg-F-ozUC9sSCeZXMDIGbiPaJFeyiOqa0CDvhQo42a_JoEFMpBiN0HWTBPURi7SWGWG5c71qMngRGkgZP0HggNz14g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19448" target="_blank">📅 22:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19447">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها می‌دانند که این اتفاق (حمله) در راه است. از ما می‌خواهند که این کار را نکنیم.
دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19447" target="_blank">📅 22:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19446">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ درباره ایران: آن‌ها را به شدت ضربه خواهیم زد، نوبت ماست.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19446" target="_blank">📅 22:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19445">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">علت رشد طلا در چند دقیقه اخیر:
مقامات امنیتی مصر به شبکه خبری "الحدث" اعلام کردند که هیچگونه حمله‌ای در بندر دمیاط رخ نداده است. آن‌ها مدعی هستند که این حادثه یک آتش‌سوزی بوده که در بخش موتور یک کشتی از رده خارج شده رخ داده است. - خبرگزاری "کان" اسرائیل.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19445" target="_blank">📅 20:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19444">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یک مقام ارشد از یکی از کشورهایی که در این میانجی‌گری نقش دارند: کسی که تصمیم‌گیری‌ها را انجام می‌دهد، فرمانده سپاه پاسداران انقلاب اسلامی است. - خبرگزاری کانال ۱۲ اسرائیل،</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/19444" target="_blank">📅 20:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19443">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انفجارات در اردن!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19443" target="_blank">📅 20:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19442">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رئیس‌جمهور ترکیه، اردوغان:
دولت فعلی اسرائیل که تحت تاثیر جنگ قرار دارد، با تحریکات و اقدامات سازمان‌یافته خود، همچنان منطقه ما را به سمت بی‌ثباتی سوق می‌دهد.
اسرائیل با نادیده گرفتن حقوق اساسی بشر و زیر پا گذاشتن قوانین بین‌المللی، به تدریج و گام به گام، سرزمین‌های فلسطینی را اشغال می‌کند.
اشغالگری اسرائیل، سکونتگاه‌های غیرقانونی آن، و سیاست‌های آوارگی، ارعاب و سرکوب علیه فلسطینیان در کرانه باختری – همانطور که در غزه انجام داده است – منبع اصلی مشکلات در منطقه ما هستند.
هزینه این تجاوز نه تنها توسط برادران و خواهران فلسطینی ما، و نه تنها توسط مردم لبنان، بلکه توسط مردم با ادیان مختلف و کل منطقه پرداخت می‌شود.
به عنوان مثال، به دلیل درگیری‌ها در منطقه ما، عرضه جهانی نفت، یکی از بزرگترین شوک‌های تاریخ را تجربه می‌کند.
متاسفانه، این فقط نفت نیست. قیمت بسیاری از مواد اولیه کلیدی در بازارهای جهانی، از جمله گاز طبیعی، کودها، سوخت دیزل و محصولات پتروشیمی، نیز به سرعت افزایش یافته است.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19442" target="_blank">📅 20:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19441">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نتانیاهو:  من همین الان یک گفتگوی تلفنی با آقای پیتر هگست، وزیر دفاع، به پایان رساندم.  او نکته جالبی را با من در میان گذاشت. ایشان به من گفتند:   «ما به جهان نگاه می‌کنیم و کشورهایی وجود دارند که اراده مبارزه در کنار ایالات متحده را دارند، اما از توانایی…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19441" target="_blank">📅 20:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19440">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXJX2dWinsw4xYlrYt7y0NSXZiuEpKc7WHcIBWc7IdkhhUIyJmB2GiJxhSVi8nXbNvg8DED4OGs9oBkrtr9upkqtZ-rDbjcNFGkgxU4nnCdZ5BHo0wR5-bzGBkv-4CIKRwBV0hqkqy5hxz_dxQs5QKxw3WbnkZzJrPE1YYC2WwL7QL_Bv-JoAD0sTiDQLUzh9zIaXKZ1_J5t-LmD8Uf_X6ZoDbgemsuW0MzXWlSOn9F3xLvwwfyfwVYg7Q7j9-xyCrRzHN0z94LbOtm7sWxq1n9hv7s3HUemATC5ZN9fAWEmWaLQl8PpmQa_290etuDnb6Xbq92B7LJrJt1aEIO5wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:
من همین الان یک گفتگوی تلفنی با آقای پیتر هگست، وزیر دفاع، به پایان رساندم.
او نکته جالبی را با من در میان گذاشت. ایشان به من گفتند:
«ما به جهان نگاه می‌کنیم و کشورهایی وجود دارند که اراده مبارزه در کنار ایالات متحده را دارند، اما از توانایی لازم برخوردار نیستند. و کشورهایی وجود دارند که توانایی لازم را دارند، اما اراده لازم را ندارند اما فقط در اسرائیل است که ما هم اراده و هم توانایی را مشاهده می‌کنیم.»</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19440" target="_blank">📅 20:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19439">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مقامات اسرائیلی می‌گویند نتانیاهو در جلسه روز سه‌شنبه با ترامپ در کاخ سفید، نقشه‌هایی را ارائه کرد که میزان نفوذ اسرائیل و ترکیه را در سوریه مقایسه می‌کرد.
بر اساس اطلاعات ارائه شده، اسرائیل حدود 0.1 درصد از خاک سوریه را تحت کنترل دارد، در حالی که ترکیه حدود 5 درصد را کنترل می‌کند.
نتانیاهو از این تصاویر برای مقابله با فشارهای قبلی آمریکا استفاده کرد، از جمله تماس تلفنی ترامپ در اواسط ماه جولای که از اسرائیل خواست نیروهای خود را از سوریه و لبنان خارج کند.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19439" target="_blank">📅 19:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19438">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19438" target="_blank">📅 19:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19437">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یک مجتمع شناور ذخیره‌سازی گاز طبیعی مایع (LNG) متعلق به یک شرکت آمریکایی و دارای پرچم جزایر مارشال، در شهر دمیاط، مصر، مورد حمله حداقل یک پهپاد قرار گرفت.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19437" target="_blank">📅 19:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19436">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یک مجتمع شناور ذخیره‌سازی گاز طبیعی مایع (LNG) متعلق به یک شرکت آمریکایی و دارای پرچم جزایر مارشال، در شهر دمیاط، مصر، مورد حمله حداقل یک پهپاد قرار گرفت.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19436" target="_blank">📅 19:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19435">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به خبرنگاران گفت:
«ایران در حال حاضر تقریباً ۱۵۰۰ موشک بالستیک در اختیار دارد.»</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19435" target="_blank">📅 19:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19434">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مقاومت اسلامی عراق با محکوم‌کردن حمله آمریکا به حشدالشعبی در کربلا، به دولت عراق تا ۲۳ صفر مهلت داد تا توانایی خود را در دفاع از کشور نشان دهد.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19434" target="_blank">📅 18:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19433">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مقاومت اسلامی عراق اعلام کرد که انتقام خود را از حملات اخیر ایالات متحده تا پس از مراسم اربعین به تأخیر می‌اندازد تا امنیت میلیون‌ها زائر مختل نشود.   این گروه هشدار داد که حملات علیه نیروهای ایالات متحده اجتناب‌ناپذیر است و گفت که در صورت لزوم عربستان سعودی…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19433" target="_blank">📅 18:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19432">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مقاومت اسلامی عراق اعلام کرد که انتقام خود را از حملات اخیر ایالات متحده تا پس از مراسم اربعین به تأخیر می‌اندازد تا امنیت میلیون‌ها زائر مختل نشود.
این گروه هشدار داد که حملات علیه نیروهای ایالات متحده اجتناب‌ناپذیر است و گفت که در صورت لزوم عربستان سعودی نیز می‌تواند هدف قرار گیرد.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19432" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19431">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رسانه‌های ایرانی گزارش دادند که 4 عضو سپاه پاسداران از کاشان در حملات مشترک آمریکا و عربستان سعودی که در طول شب به سایت‌های حشد الشعبی در عراق اصابت کرد، کشته شدند.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19431" target="_blank">📅 17:59 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
