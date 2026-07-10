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
<img src="https://cdn4.telesco.pe/file/f2QgkBAyb1sOOVgTRyIA_RdXpPp5DHJFAo8jqbm8nODLAOgNW73V056vtbwpWlS5_hVNXFPpC4PqqAJkcexAs9qFerFqhJbW6BQCpEqyeArOldRXBXnPvXDoXMNWYlke3O0z3kbquRwU2VspZvKrA1bs8WkJWnD615XOXRvL_sOMNjGNc-jOCP7ANHRozIf7ohHj2swuWDO1SzP-PTkVKtaiizPsM6Lxh5pPspDT7aAywu6T_nNE1eoMEY_mRS7HCwQGiPGVzFpPG2fcLpHGGyZHaoFb-0CsWirfb4MtbSyflrXYT1ifa4buQkuYRAEDpcUmYojm9iWkoi0Lsua5LA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.2K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 13:54:21</div>
<hr>

<div class="tg-post" id="msg-18471">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دو نکته:  — از این میان ما سومی (J-20) را داریم. (البته ماکت ش)  — آخری (جنگنده کان یا خان ترکیه) فقط یک مشکل کوچک دارد و آن اینکه موتورش هنوز پیدا نشده که انشالله این هم حل می شود.</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SBoxxx/18471" target="_blank">📅 13:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18470">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIJ6WuK-azZ2oSroSNOdxkjupRKqVeURUP4ZZDSmGxx1-_rQVx7zL2Hw-wQK7jqIN5Uj0xXzufuzCmKiynfvUtqZqEMzsqFHbPDaDUoC58MIXRp99o1XnJBwutji37Qf32WjCjsxaQBRS1qG4pb56stuWqYy2mTtlWwOC0jPOGK1tIqksoJl9O8QHO4mG6Dn39DcYT-RScgFGWS7DCRjLMwr9MvDvxnZcQoEo0bnVBw3ILlHliwVBSFJMTULl_oSNJjjPszP_57MYIBzOPkXsMVKU5Xj3VgPLFKH2x9DNu04eLHC2KSU4STTGKwU9NLP5-o2ZqUlsQvNcgLCaIYh6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا افرادی با لباس نظامی به نیروهای بسیجی مستقر در یک ایست بازرسی حمله کرده و دستکم ۲ نفر را کشته اند.</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/SBoxxx/18470" target="_blank">📅 12:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18469">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الشرق الاوسط: حماس جلسات رهبری خود را از قطر به ترکیه منتقل می‌کند.
در ماه‌های اخیر، این گروه بخش قابل توجهی از فعالیت‌های سیاسی خود را به ترکیه منتقل کرده است، در حالی که قطر سال‌ها به عنوان مرکز اصلی فعالیت‌های سیاسی آن عمل می‌کرد.</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SBoxxx/18469" target="_blank">📅 12:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18468">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WU11CcmhdC4NElE9MB6vwDClyVIG344FMGr_jsnD_DUBbiZr6ouv1fogxLH3Tao86MFvbvrIc-_3FumfTI-2tT0HhiHMV4A-TAJE4Uoj-G7syT9kHqZkXej9f0l3SW1unLpCA5hdHmbhyGlGOQSGuvuvztnruIqRO7AEBsZIxWPBiEPST0R3Gatwf0-OZaDz0M7ljA3u5NPG6HFi0CZWMu6SD1idELB9AHdHC4vvWeUIbs6kPeKVrPToIT4CCzWs3fqb-4JH2dKC9Z0jMeEuK3zpZ0xhzFYS6-YW7XHFK1gmvjqzob6OMu3wmXdseBjhT6oZD4SDn8VUS7PCGf1jbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک در میانه بازه خود قرار دارد و پیش بینی می شود یک اصلاح نزولی در دارایی های ریسکی داشته باشیم که عمیق و شدید نباشد.</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/18468" target="_blank">📅 12:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18467">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18467" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 5
جمعه 10 جولای 2026</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SBoxxx/18467" target="_blank">📅 12:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18466">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یک مقام آمریکایی به شبکه CNN گفت که ایالات متحده و ایران در حال انجام مذاکرات غیررسمی برای کاهش تنش‌ها هستند، این در حالی است که پس از یک سری حملات متقابل، این مذاکرات در جریان است.
ایالات متحده در حال حمله و سپس توقف است، به این امید که از تشدید بیشتر اوضاع جلوگیری کند و به دیپلماسی فرصت عمل دهد. در عین حال، واشنگتن برای انجام حملات بیشتر امشب، در صورت لزوم، آماده‌سازی‌ها را انجام می‌دهد.
بر اساس گزارش Axios، دونالد ترامپ "به شدت به دنبال راهی برای خروج از جنگی است که آمریکایی‌ها از آن حمایت نمی‌کنند."
پاکستان و قطر نیز در تلاش هستند تا هر دو طرف را به میز مذاکره بازگردانند. میانجی‌ها معتقدند که حملات اخیر ایران در تنگه هرمز، توسط جناح‌هایی در داخل رهبری ایران صورت گرفته است که با توافق‌نامه همکاری مخالفت دارند و در تلاش برای تضعیف آن هستند.</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/18466" target="_blank">📅 11:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18465">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o25uhgFsqBArQGFmAZneczZ5JwUHZ9TKrSZPyqKUCBf2BBSXRFnBLX7Kdi0S74WvKl-jBipO153f8OFE3JshM0AL7jvI3OrB_tBcMKJRevsvQ33lUpn7WLvvUdDrAsRa5quGWd3Wo1yFzbB4tFNgi9nQf73_H7SIp6E_3mrVHlBvmRJ3pa6NAdESI3P9wc0xthIo8Xedu96Vr_lKlTSsMsUJXpX1DORDLbWhoZg9el3uFB2tdEkeNbCnQ88QBeJ3IpLM7ME_MTF5v2jsXxRMcrmO56AeCJUeRbVLntQYnLv_oztRyC6nZz8BCk5_NnYpQ52nNwibXPoyaIQYmlf6LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک که از صبح پایین بود و منجر به رشد طلا و افت دلار و نفت شده بود، اکنون جهش کرده و پیش بینی می شود در ساعات آینده در بازارهای مالی شاهد یک موج ریسک گریزی باشیم.</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/18465" target="_blank">📅 11:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18464">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uX9Vm7VVfP0HhikqITM3yat0KnGlFjxNg9J6oODO7mKltSGAeemYUsdZn_Qx-1i32sb23g-WS-L4mO-_oybQqNEN-g4_mTdyPGPtjzPEY-ONYuw2SWs_EGweMiP9UrQsFrG8ucRkLqUidJD1VGBSxHAETa8deX7YegDu1_cYtBsYSf1tdx4jZ2m_yf_rdVMFg97k9_-1u9WtqZBdi_NtKZd9ZgOGjc7UBSz1_eT3I5q6lP1mWbOTE2G_0d2_nPU7bOQ-T-kKbmJPC3Mbk1I3WTxIk0DbPNPus8cW9krlNl2KL63GMJs4AaBJlNFvkRhh5nH_xnkntpCnH26Ju33v7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگ-۲۹ همراه؛ جنگنده‌ای واقعی اما با محدودیت‌های مهم
انتشار تصاویر اسکورت هواپیمای حامل پیکر رهبر پیشین ایران توسط یک فروند میگ-۲۹، موجی از بحث‌ها را در فضای مجازی به راه انداخته است. برخی کاربران مدعی شده‌اند که این هواپیما در واقع یک
میگ-۲۹UB
، یعنی نسخه آموزشی دو سرنشینه، بوده و به همین دلیل از رادار بی‌بهره است. بررسی مشخصات فنی نشان می‌دهد که این ادعا تا حد زیادی صحیح است، اما نتیجه‌گیری برخی مبنی بر اینکه این هواپیما «جنگنده واقعی نیست» نادرست و اغراق‌آمیز است.
نسخه MiG-29UB برای آموزش خلبانان طراحی شده و به دلیل نصب کابین دوم، رادار اصلی N019 از دماغه آن حذف شده است. در نتیجه، این هواپیما توانایی کشف و درگیری فراتر از میدان دید (BVR) را مانند نسخه‌های تک‌سرنشینه ندارد و نمی‌تواند از موشک‌های هدایت راداری به همان شکل بهره ببرد. این موضوع، توان رزمی آن را در نبردهای هوایی مدرن کاهش می‌دهد.
با این حال، حذف رادار به معنای از دست رفتن کامل قابلیت رزمی نیست. میگ-۲۹UB همچنان از دو موتور قدرتمند RD-33، عملکرد پروازی مشابه نسخه استاندارد، توپ داخلی و امکان حمل برخی تسلیحات، به‌ویژه موشک‌های کوتاه‌برد حرارتی مانند R-73، برخوردار است. بنابراین این هواپیما همچنان قادر به انجام مأموریت‌های رهگیری دیداری، گشت هوایی، آموزش رزمی و اسکورت تشریفاتی است.
در مأموریتی مانند همراهی هواپیمای حامل پیکر یک مقام بلندپایه، هدف اصلی معمولاً نمایش اقتدار، احترام نظامی و ایجاد جلوه‌ای نمادین است، نه مقابله با یک تهدید هوایی پیچیده. از این رو، استفاده از یک فروند MiG-29UB برای چنین مأموریتی امری غیرعادی محسوب نمی‌شود.
در مجموع، اگرچه میگ-۲۹UB فاقد رادار است و از نظر توان رزمی با نسخه‌های عملیاتی میگ-۲۹ برابری نمی‌کند، اما همچنان یک هواپیمای جنگنده با قابلیت‌های قابل توجه است و نمی‌توان آن را صرفاً یک «هواپیمای آموزشی» فاقد ارزش رزمی دانست.</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/18464" target="_blank">📅 11:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18463">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سوزاندن ترامپ لگویی خندان دیشب در مشهد!</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/18463" target="_blank">📅 11:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18461">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IzRwJEX0y6MxPRuwhSW8Lhm0UAri_OqywsfRvQmKnPBsvqoGScmSNdCOxrp1o2F5m4bSJDoflioOsnuKDuLISwdUrkdLfrR_wo-4VI-yZj0oGHdaqD9aHjzIWC5CGs8tmQ19QUG3UaKgyhF9Cza6fZqAZbJckqe7xlU2fkKfnDo62jwSunFU183g9UvbhPZVn3-F4H8ylZ37L4ujJj7HOv9tDox5ZqscM8xajgMmzAHAhPC2MrtmOxaTL0zZLSTq9pSEKZLVrmfkA7mUIR1vqkINI3k_97FS5AxsnTh73tK29uNAR7iBSI3BHb_hdN3Ie_XJXhtPN4h6qoUlWnHMIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RpYx96RcSHtT4YzMkyv9XeVJBMxwnIT8tW0I8YuyBHFcFwcunQMsSYpVCzu3t_VVITzDCXTeUkBP1dm1B9U9hKW8egQq0jKbA9izbv42dw5aEM5MRusZ8tnJCmKYlEeg0bVCtpGfvLBTuOtg7yWzAiv8XBCohe1y6AduVx6SmzJKMMVK4LSylck_cspf6vkhQx8TPTNkyerVsV25IGKRjqj7UAh6kUMjwqvukth6xevc9cCh1L2h8vEiIblIcvHiTnWGZfHRnCVpP6ossmvrmIcw3qS2soKMap9UfItTuadpSm7zaFOgLW2UVbzhqT1ZPr4HbRySZo9MyU8VdBgOlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر چه فکر می کنم به نظرم چهره آقای نجاتی در عکس سه نفره هم هست!</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SBoxxx/18461" target="_blank">📅 10:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18460">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترکیه سیستم پدافند هوایی S-400 خود را به یک کشور خلیج فارس – احتمالاً امارات متحده عربی یا قطر – فروخته است.  جزئیات نهایی شب گذشته نهایی شد و انتظار می‌رود امروز یک اطلاعیه رسمی منتشر شود.  منبع: عبدالکادیر سلوی، روزنامه‌نگار ترکیه‌ای (روزنامه حریت)</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/18460" target="_blank">📅 10:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18459">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وزیر دفاع یونان، نیکوس دندیاس:  یونان از این موضوع که ترکیه جنگنده‌های F-35 را دریافت کند، راضی نیست. یونان از این موضوع که ترکیه موتورهایی برای یک هواپیمای نسل جدید دریافت کند، راضی نیست.  ما یک سوال مطرح می‌کنیم: آیا این موضوع به منافع واقعی ایالات متحده…</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/18459" target="_blank">📅 10:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18458">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وال‌استریت ژورنال:
بر اساس اطلاعاتی که اسراییل ارائه کرده، ایران طرح جدیدی برای ترور ترامپ طراحی کرده است.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18458" target="_blank">📅 01:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18457">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHvGOXFOV9rY9k4i5pNdnNtFPGKFww2mUa_iMMZes5zgiM9ti0KaiO0azZiMvj0gG1hbvE6YCyqFA9naNLOsgiNV6aqBc6sHW7xdfyZx3NR_D9VCsh3XgKK9zrw9TdQSXITBqT3zqSDLYSKygpKN9aZb6cgLP4QILD-ZW93oGQl5vKYAkPwcONL-14k08ESIAQ_cTpsIw3kR6vP55iIRAw64L8CGwRG1JZAeHxXvuFQSj7Qffgc_GLSaXzchHtzid4funVcOjx7VgXYuujaKlEoe7bk7_qYmPvFJwuVT_MxfiQ1LVpGnZWcROSp6UACo2Aj2nnkTK3Dg5D3ZRQXWDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا افرادی با لباس نظامی به نیروهای بسیجی مستقر در یک ایست بازرسی حمله کرده و دستکم ۲ نفر را کشته اند.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18457" target="_blank">📅 00:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18456">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انتشار اخباری تایید نشده از تیراندازی در اطراف حرم امام رضا</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18456" target="_blank">📅 00:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18455">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انتشار اخباری تایید نشده از تیراندازی در اطراف حرم امام رضا</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18455" target="_blank">📅 00:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18454">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تیم فرانسه به روزی افتاده که بلوندشان شده امباپه!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18454" target="_blank">📅 23:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18453">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فرماندار کنارک:
منطقه نظامی نیروی دریایی در دو مرحله هدف حمله دشمن قرار گرفت
ایرنا</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18453" target="_blank">📅 23:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18452">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">برخی گزارش‌های اولیه حاکی از یک ترور هدفمند در اهواز علیه علیرضا خدادادی، مشاور قرارداد استانی ولی‌عصر سپاه پاسداران در اهواز، استان خوزستان، ایران است</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/18452" target="_blank">📅 22:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18451">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اگر کار آمریکا نباشد ۲ گزینه باقی می ماند:  — اسراییل — امارات</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18451" target="_blank">📅 22:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18450">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">آمریکایی ها هر گونه حمله جدید را منکر شده اند</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/18450" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18449">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گزارش‌هایی مبنی بر حملات هوایی آمریکا در شهرهای اهواز، چابهار و بوشهر منتشر شده است.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18449" target="_blank">📅 22:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18448">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گزارش‌هایی مبنی بر حملات هوایی آمریکا در شهرهای اهواز، چابهار و بوشهر منتشر شده است.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18448" target="_blank">📅 21:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18447">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انفجار در بوشهر!</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/18447" target="_blank">📅 21:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18446">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انفجار در چابهار !</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/18446" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18445">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فوری | رئیس ستاد مشترک نیروهای مسلح اسرائیل: ما به هر کسی که بخواهد به ما آسیب برساند، با قدرت پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/18445" target="_blank">📅 19:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18444">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک که از صبح پایین بود و منجر به رشد طلا و افت دلار و نفت شده بود، اکنون جهش کرده و پیش بینی می شود در ساعات آینده در بازارهای مالی شاهد یک موج ریسک گریزی باشیم.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/18444" target="_blank">📅 19:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18443">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ON64Y-8eagCSKm8FjL-6nildbLoSCnW3dFeRuq3VjNKLsBG98WxSn_Ar0sfPZuR0YpW0mp5LTlzmS8FSrYwdLTqz-FnzpUxTkQJeUXBRDY0IPxnyXj0-KmCedubjRxtwUgejxgXljbD9Re76urfZClY1DSoHP5j6NsMvRasgfJCnlqY9vdRlPzpt2PsD0YGhOepqWMRX6xfkDzXNlRMD0EsV0d9Jd-Z7mLB05CJ6_9an2cX3pfm5YYL37tI2tRbPCL82IaaEloBqvNvKwjpJjS9iA0XH8T6uaeyWM5hR512TXqLNLGiWRMwCPTlqxnC61eSNd4mXmqPdWyTPEHIKkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح پایینی قرار دارد و ریسک پذیری پیش بینی می شود.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18443" target="_blank">📅 19:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18442">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سپاه پاسداران: مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی الازرق اردن درهم کوبیده شد.
🔹
رزمندگان هوافضای سپاه ساعت ۱۴:۲۰ بعد از ظهر امروز مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی دشمن در الازرق اردن را با ۱۰ فروند موشک بالستیک درهم کوبیدند.…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18442" target="_blank">📅 17:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18441">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سپاه پاسداران: مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی الازرق اردن درهم کوبیده شد.
🔹
رزمندگان هوافضای سپاه ساعت ۱۴:۲۰ بعد از ظهر امروز مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی دشمن در الازرق اردن را با ۱۰ فروند موشک بالستیک درهم کوبیدند.
🔹
در صورت تکرار تجاوز ارتش تروریستی آمریکا سایر پایگاه‌های آمریکا! در منطقه از آتش سنگین ما در امان نخواهد بود.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18441" target="_blank">📅 17:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18440">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وزیر دفاع یونان، نیکوس دندیاس:
یونان از این موضوع که ترکیه جنگنده‌های F-35 را دریافت کند، راضی نیست. یونان از این موضوع که ترکیه موتورهایی برای یک هواپیمای نسل جدید دریافت کند، راضی نیست.
ما یک سوال مطرح می‌کنیم: آیا این موضوع به منافع واقعی ایالات متحده آمریکا خدمت می‌کند؟ بله یا خیر؟ و البته، پاسخ این سوال بر عهده مردم آمریکا و دولت آمریکا است.
این موضوع قطعی است که برای دولت ایالات متحده، ناتو و به ویژه ثبات در دریای مدیترانه شرقی، از اهمیت بالایی برخوردار است.
بنابراین، آیا ارائه یک پلتفرم به یک کشور در دریای مدیترانه شرقی، بدون این شرط که این پلتفرم نباید علیه یک عضو متحد دیگر مورد استفاده قرار گیرد، به نفع ایالات متحده است یا خیر؟</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18440" target="_blank">📅 15:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18439">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ارتش اردن اعلام کرد که ۸ موشک بالستیک ایرانی که به سمت خاک این کشور شلیک شده بودند را رهگیری کرد.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18439" target="_blank">📅 15:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18438">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجار در شیراز و کرمان</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18438" target="_blank">📅 15:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18437">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">— دونالد ترامپ:  «به نظر من، اسرائیل نیروهای خود را از جنوب لبنان خارج خواهد کرد.»</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18437" target="_blank">📅 14:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18436">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18436" target="_blank">📅 14:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18435">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‍
💢
وزارت خارجه: حملات جنایتکارانه آمریکا نقض فاحش بندهای یک و پنج یادداشت تفاهم است
🔹
وزارت امور خارجه حملات تجاوزکارانه ارتش تروریستی آمریکا طی بامداد پنج‌شنبه ۱۸ خردادماه به چندین نقطه در استان‌های ساحلی جنوب و نیز دو پل در استان‌های شرقی در مسیر ریلی…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18435" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18434">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18434" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18433">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مانور کلاهک موشک ایرانی که دیشب به پایگاه آمریکا در کرانه های جنوبی خلیج فارس اصابت کرد.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18433" target="_blank">📅 14:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18432">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e86d2fb7c7.mov?token=VaSXey-CRFCs2bxMU3_iGidNmgogR7OkC64gKxCk4WU0V8e6qi3XnE3NgmQuelzgO51WtCGNF9_o7jZqCMIyQSZeCfNQiEjVTai1AgQLoVTdWAXenTAhuU5WqcI9wsbXfUZ54l77traqgil32u55x1u5i2_9HbRSsHa5nmE0nBj2P2ZGsl2zkXdT-g8J4TL98VabdQHyC99gFYlggOPDzkBwhw3KPqYQyVMB1BFeHIDeoKs1NTgxlVh-E4JL8sAN0KnXGrJCK0Of94hWIRvqryJPkCgTjclfKv0vMfx555QeDP1zudMR1IVHHQpqG3xjZLE3jOosLj0XPz7UlackzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e86d2fb7c7.mov?token=VaSXey-CRFCs2bxMU3_iGidNmgogR7OkC64gKxCk4WU0V8e6qi3XnE3NgmQuelzgO51WtCGNF9_o7jZqCMIyQSZeCfNQiEjVTai1AgQLoVTdWAXenTAhuU5WqcI9wsbXfUZ54l77traqgil32u55x1u5i2_9HbRSsHa5nmE0nBj2P2ZGsl2zkXdT-g8J4TL98VabdQHyC99gFYlggOPDzkBwhw3KPqYQyVMB1BFeHIDeoKs1NTgxlVh-E4JL8sAN0KnXGrJCK0Of94hWIRvqryJPkCgTjclfKv0vMfx555QeDP1zudMR1IVHHQpqG3xjZLE3jOosLj0XPz7UlackzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مانور کلاهک موشک ایرانی که دیشب به پایگاه آمریکا در کرانه های جنوبی خلیج فارس اصابت کرد.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18432" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18431">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZCjZgjWh2owUsN3CtVO1I-5ut1MfogNPpjS2jxSvwEhqu3Leu-rnLbqhLNJuFGlhrJOOlU8iMfeVVMTBT0e1WgGXMMnOepKcWUmNVyUmuEbTyLx8A5ZtCHqtnTu_ZXrT5AKwHGI98TNUhXl4hVQW2lEWWLKCVR-BLBv3nWwkvuP_apCjZ1uNG4jNbB5TDBiAUKKyHyc62cNMxFPPXHKpG0Pl3TesY4udaBeatWIytFQAZTaBqysLumcTsiOTqIBOlTF1_vJyvd9_6LWzrTWLGCirvOUKdgtn6Sr24xP-oT7WvW74INbsBfxPg9NRmf0Bk9lmyPGMNuHoCmaPp-1hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با اینکه ترامپ برای عزیمت به ترکیه آماده می‌شد، مارکو روبیو، وزیر امور خارجه، و پیتر هیگست، وزیر دفاع، در دفتر بیضی‌شکل کاخ سفید، او را در جریان گزارش‌هایی قرار دادند مبنی بر اینکه ایران موشک‌های کروز و پهپادها را به سمت کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده و به سه فروند از این کشتی‌ها خسارت وارد کرده است.
ترامپ پرسید که آیا تهران هنوز به دستیابی به یک توافق نهایی متعهد است یا خیر، و پس از مشورت با مشاوران ارشد امنیت ملی خود، به این نتیجه رسید که اینطور نیست.
این جلسه، نقطه‌ی عطفی بود که باعث شد او طرح آتش‌بس را کنار بگذارد و مجوز حملات نظامی جدید و اعمال فشار اقتصادی مجدد بر ایران را صادر کند.
منبع: WSJ</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18431" target="_blank">📅 13:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18430">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجار در بوشهر</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18430" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18429">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWc1CGvH4vUH4q2m1kxcx29DFNYRBoVzs_giEbKkRjstFA6HWN6cZaZsVWrLHxp6ISjx0qJaTsCHg6WUX789R1t41JXqDoLLqWLFCI2o4XJZQb_tvSNlxXJEPn2yHT6WcoQSuRtQxkrDKhd7luPfmxWYrjoo8zr8-0aO0utoMZAgoPmls3Jec1CpN-TfWS1nQtFPeP0Vor1JuPBLbWQH16VvVwHNegJD-uC6ab7moO5-lDa1pYGnkR7K8rT_sRR5G8XNn46amBMza7oMAdxv_XeqtMgxKf69tZOB35b_6Fsq0hLgBWa36c35zBbrdeybWOGFc2FncaYQFgLo6KpqgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.  پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/18429" target="_blank">📅 13:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18428">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عمدا جاهایی را دارند میزنند که در شکستن محاصره نقش داشتند و کریدورهای جایگزین برای ایران حساب می شدند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18428" target="_blank">📅 12:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18427">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
🇮🇶
🇮🇷
✈
هواپیمای حامل پیکر آیت‌الله سید علی خامنه‌ای و خانواده به فرودگاه مشهد رسید.
📮
@IRKhbarFori</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18427" target="_blank">📅 11:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18426">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبارفوری جنگ امریکا فوری/ خبرفوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3075b8e37.mp4?token=R71h_RVzWSQyoX2H4A1K7FscHysZ0FiCjsXhggtE3vrWEG1_NR-gF54_fkjHo3X4UjJbilE2tBxJy6NEuCq4qcR0x11k147jGmoiLSh5yrJduxXx-hCkrudkHgWx-OG4KZY9t76OxVjU6p-6af3g75mm4Qd59phBshqCsZ50h9E0y24aFRQ7V8K4gPaC55kDT5L8nr01xSIg-fVPToXZnY93y5hPRiG8MaYy5D-bSIq7ebCSGjfO5iq9-4lQgO9f9kq__ivZFtw6O0IL3O_PTXzAdpFavQ9IS2gUIO5ZxLzjeBxf9Jv3azFfjTS-iBO4HRGRi4Kds_MhiaPWEkzJaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3075b8e37.mp4?token=R71h_RVzWSQyoX2H4A1K7FscHysZ0FiCjsXhggtE3vrWEG1_NR-gF54_fkjHo3X4UjJbilE2tBxJy6NEuCq4qcR0x11k147jGmoiLSh5yrJduxXx-hCkrudkHgWx-OG4KZY9t76OxVjU6p-6af3g75mm4Qd59phBshqCsZ50h9E0y24aFRQ7V8K4gPaC55kDT5L8nr01xSIg-fVPToXZnY93y5hPRiG8MaYy5D-bSIq7ebCSGjfO5iq9-4lQgO9f9kq__ivZFtw6O0IL3O_PTXzAdpFavQ9IS2gUIO5ZxLzjeBxf9Jv3azFfjTS-iBO4HRGRi4Kds_MhiaPWEkzJaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇶
🇮🇷
✈
هواپیمای حامل پیکر آیت‌الله سید علی خامنه‌ای و خانواده به فرودگاه مشهد رسید.
📮
@IRKhbarFori</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18426" target="_blank">📅 11:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18425">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبارفوری جنگ امریکا فوری/ خبرفوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25cd71dba4.mp4?token=b9rppcjTVNaCzdIjoy1d1IKOwN8FZKnNQgcWwNfbDFAnaufL678rouxc-ZrNSY1TLXlWebBzGx9ZDO-dHBrrdALgf95hXNVkx5SGjPyDWsgUXxL5qJb7RuElHXZd5ZBqgR_uiLfIEvNKp1kAHRz8doRls56TqhFC0y6nAHZB1Lsykd_ua1Y2SMaHiTO2wehRg-4rVey8xo2XMa-TUkqSxru-__hX5OjocY1T95gYkzV-jBj8LctllCsaXrc3CZIaKLgDlnEgPLEmngGOIMrMmSAhzcm1wpv22d7Gsx723zPejfGbXEwCGgBNvZvptA6GgKJrdFSlLnt3low_M35W5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25cd71dba4.mp4?token=b9rppcjTVNaCzdIjoy1d1IKOwN8FZKnNQgcWwNfbDFAnaufL678rouxc-ZrNSY1TLXlWebBzGx9ZDO-dHBrrdALgf95hXNVkx5SGjPyDWsgUXxL5qJb7RuElHXZd5ZBqgR_uiLfIEvNKp1kAHRz8doRls56TqhFC0y6nAHZB1Lsykd_ua1Y2SMaHiTO2wehRg-4rVey8xo2XMa-TUkqSxru-__hX5OjocY1T95gYkzV-jBj8LctllCsaXrc3CZIaKLgDlnEgPLEmngGOIMrMmSAhzcm1wpv22d7Gsx723zPejfGbXEwCGgBNvZvptA6GgKJrdFSlLnt3low_M35W5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇶
🇮🇷
🎬
هم‌اکنون هواپیمای حامل پیکر آیت‌الله خامنه‌ای و خانواده، فرودگاه نجف را به مقصد مشهد ترک کرد.
📮
@IRKhbarFori</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18425" target="_blank">📅 11:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18424">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">چرا درگیری بعدی ایران و آمریکا احتمالاً جهش تاریخی نفت را تکرار نمی‌کند؟
درگیری نظامی میان ایران و آمریکا همواره یکی از بزرگ‌ترین ریسک‌های ژئوپلیتیکی بازار انرژی بوده است. هرگونه تهدید علیه تنگه هرمز، مسیر عبور بخش قابل توجهی از صادرات نفت خلیج فارس، در گذشته می‌توانست باعث جهش شدید قیمت نفت شود؛ زیرا بازار به اختلال ناگهانی در عرضه واکنش نشان می‌داد. اما شرایط بازار انرژی امروز نسبت به گذشته تغییرات مهمی کرده است و درگیری احتمالی آینده لزوماً به معنای تکرار شوک‌های نفتی تاریخی نخواهد بود.
یکی از مهم‌ترین عوامل، ایجاد مسیرهای جایگزین برای انتقال نفت در خارج از تنگه هرمز است. کشورهای تولیدکننده منطقه، به‌ویژه عربستان سعودی، امارات و عراق، در ماههای اخیر سرمایه‌گذاری‌هایی برای توسعه خطوط لوله، پایانه‌های صادراتی جایگزین و افزایش ظرفیت انتقال خارج از این آبراه انجام داده‌اند. این زیرساخت‌ها به بازار اجازه می‌دهد بخشی از نفت منطقه حتی در صورت اختلال در هرمز همچنان به بازارهای جهانی برسد. بنابراین، حساسیت بازار نسبت به تهدید بسته شدن کامل تنگه هرمز نسبت به گذشته کاهش یافته است.
عامل دوم، افزایش ظرفیت عرضه و انعطاف‌پذیری بیشتر بازار نفت است. تولیدکنندگان عضو سازمان کشورهای صادرکننده نفت (OPEC) و متحدان آن در قالب ائتلاف اوپک پلاس، در مقاطع مختلف توانسته‌اند با تغییر سیاست تولید، بخشی از شوک‌های عرضه را مدیریت کنند که یک نمونه جاری آن را با 3 بار افزایش تولید اخیر اوپک که آخرینش هفته پیش تصویب شد مشاهده می کنید. همچنین رشد تولید نفت شل در آمریکا باعث شده بازار جهانی نسبت به دهه‌های گذشته تنها به خاورمیانه وابسته نباشد.
از سوی دیگر، سمت تقاضا نیز تغییر کرده است. رشد خودروهای برقی، افزایش بهره‌وری انرژی، سیاست‌های کاهش مصرف سوخت‌های فسیلی و تغییر الگوی رشد اقتصادی چین باعث شده رشد تقاضای نفت کندتر شود. در نتیجه، هرگونه اختلال کوتاه‌مدت در عرضه ممکن است بیشتر به یک شوک موقت قیمتی تبدیل شود تا آغاز یک روند انفجاری پایدار.
موضوع مهم دیگر، پدیده «نابودی تقاضا» است. اگر قیمت نفت به‌سرعت افزایش یابد، مصرف‌کنندگان و صنایع واکنش نشان می‌دهند: استفاده از انرژی‌های جایگزین افزایش می‌یابد، فعالیت‌های انرژی‌بر کاهش پیدا می‌کند و اقتصاد جهانی با فشار رکودی مواجه می‌شود. تجربه بحران‌های قبلی نشان داده است که قیمت‌های بسیار بالا خودشان عاملی برای کاهش مصرف هستند.
البته این به معنای بی‌اهمیت شدن ریسک افزایش بهای نفت نیست. یک درگیری گسترده که تولید نفت ایران و دیگر کشورهای نفتی یا زیرساخت‌های اصلی منطقه را هدف قرار دهد، همچنان می‌تواند باعث جهش کوتاه‌مدت قیمت شود. بازارها به اخبار جنگی با سرعت واکنش نشان می‌دهند و عامل روانی می‌تواند قیمت‌ها را برای مدتی بالا ببرد.
اما تفاوت امروز با گذشته این است که بازار نفت ابزارهای بیشتری برای جذب شوک دارد. مسیرهای جایگزین صادرات، ظرفیت‌های ذخیره‌سازی، تولیدکنندگان جدید و تغییر رفتار مصرف‌کنندگان باعث شده‌اند احتمال تکرار جهش‌های تاریخی نفت در اثر یک درگیری منطقه‌ای کاهش یابد. در سناریوی درگیری بعدی ایران و آمریکا، احتمالاً واکنش بازار بیشتر یک جهش سریع و محدود خواهد بود، نه یک بحران انرژی مشابه دهه‌های گذشته.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/18424" target="_blank">📅 11:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18423">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ارتش ایران:  «ما با استفاده از پهپادها، سامانه‌های پدافند هوایی پاتریوت در کویت، یک مرکز هشدار اولیه در قطر و تاسیسات ذخیره‌سازی سوخت ارتش آمریکا در بحرین را هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18423" target="_blank">📅 11:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18422">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
حملات پهپادی ارتش به پایگاه‌های آمریکا در منطقه
🔺
روابط‌عمومی ارتش:  در پی تجاوز ارتش تروریستی آمریکایی مناطقی از کشور و یگان‌های ارتش و در پاسخ به آن جنایت،  ساعتی قبل و در ادامۀ حملات ارتش به پایگاه‌های آمریکا در منطقه، سامانۀ پاتریوت در کویت، آنتن ماهواره‌ای…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18422" target="_blank">📅 11:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18421">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">به گزارش اکسیوس، پهپادهای ایرانی دو کشتی تجاری را در تنگه هرمز هدف قرار داده‌اند.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/18421" target="_blank">📅 11:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18420">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شبه نظامیان آزادی بلوچ یک حمله با بمب دست‌ساز (IED) و سپس یک کمین سنگین را علیه کاروانی متشکل از سه خودروی نیروهای امنیتی پاکستان در منطقه سچی واشوک، بلوچستان، انجام دادند.  خسارات سنگین جانی گزارش شده است.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18420" target="_blank">📅 10:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18419">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مقر تیپ 110 سلمان فارسی نیروی زمینی سپاه در زاهدان بمباران شده است.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18419" target="_blank">📅 10:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18418">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyJcb6BX1FWwihSjZfK6luR9grKg7ckFlHl1R3-ifgJEVY2xVmaRN5mZKf9l7P9fn2gw9yxKvi_-zsVgEhkMQ70zeAgWUkHxJUC9lFNjzKbWghi4pBau-tM5J8T_5tAKFBkSwGRe-S1qE-Zw5oaX5zMFEddxhauqVl9tsXT6xePtUL7fg8SlvD0w7Zl_9lMBm2L3_yy8QIjzwT5FKXLqvJjaXz98Ks2ezB1kVtK9dJKC185vi_cOxtLefHmUbItpZJ8QKsb7ZIrAOUvzTcVYNWI2Wou7FtxFjXjjtT337xmjyCP-5eyoAsyxHlYUa5WtL_sehIIewOFhFe5cmEiFkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح پایینی قرار دارد و ریسک پذیری پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18418" target="_blank">📅 10:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18417">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18417" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 4
پنج شنبه 9 جولای 2026</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18417" target="_blank">📅 10:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18416">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بیانیه سپاه پاسداران انقلاب اسلامی   بسم الله قاصم الجبارین  قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ  ملت شریف ایران، ملت کریم و مجاهد عراق؛ آفرین بر شما مردمان مومن و بصیر…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/18416" target="_blank">📅 09:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18415">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کاخ سفید برای یک درگیری بالقوه طولانی‌مدت با ایران بر سر تنگه هرمز آماده می‌شود.
مسئولان آمریکایی می‌گویند مدت زمان این درگیری به اقدامات بعدی تهران بستگی دارد.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18415" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18414">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlqPoH04BnK5q2VhoZnQHTOISx-uhUoQcAQX_7ThKLg0DfWwW5fHSHoQMl6moD9YaxS909jQH66TnARvlW1jRhkzO52yMXDGQk7fity8gZt08-w_dS_hEOptaMksMYTFUWnkMOBvlzq6OeEmK3coqVQ30yuo96oAnu2tk0LcoQ0sOXFtCLflLdZJl7wLcbjg3XkF-b5rI8hdfP88-p7jClzg3v78fbDVvJ8_fLdUdLrVZuA_JQB5yHEU23wPQ0df6N0KEYaBHBD8XCpeDn11fPPicVrYl8Pwa1HSWPrwssJyc0VHykY3P7kE5YN778BrGtngB6TTVF1NQqiGKuqAgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمدا جاهایی را دارند میزنند که در شکستن محاصره نقش داشتند و کریدورهای جایگزین برای ایران حساب می شدند.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18414" target="_blank">📅 08:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18413">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">راه آهن جمهوری اسلامی ایران:   به دنبال حمله جنایتکارانه دشمن آمریکایی بامداد امروز به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.  برنامه ریزی لازم برای جابجایی مسافران محترم قطارهای متوقف شده در این مسیر، از…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/18413" target="_blank">📅 08:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18412">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">راه آهن جمهوری اسلامی ایران:
به دنبال حمله جنایتکارانه دشمن آمریکایی بامداد امروز
به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.
برنامه ریزی لازم برای جابجایی مسافران محترم قطارهای متوقف شده در این مسیر، از طریق ناوگان مسافری جاده ای به مشهد مقدس انجام شده است.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18412" target="_blank">📅 08:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18411">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">توییت محمدسامثینگ قالیباف</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18411" target="_blank">📅 08:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18410">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yt7Zo6zFbzSGsVrqbRt0ZCRT8Rvmk0EzOGLSt50JLpERA1bfW9rGGUxvPog8DfNqtEOSFpw7WY9vLvKF-IQMelTmU9OqTwuYZs7W9XFiTWZMxLEqB2uE8svhNq55-jwnMel-PBFkvK9gJZJ3f2O5E6MmGT3LTkA8YEGBqdPml2QKu0iWLTvKTfOVpcv4IadHvooym-QvN3efEn30xmJgmLtKsU2e6eg17xY37nA0yrKcLGPaQ_U4TraCF6D4zq9wapN_eDfPQIdNW6JXHqegFcw05qJ7iH3B8AdQYTD1nBB73glS3r5OU1NvXV88XfjMqZbJH_rMkAkOfABv-dQcSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت محمدسامثینگ قالیباف</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/18410" target="_blank">📅 08:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18409">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ایران به اهداف دشمن با نسبتی حداقل دو به یک حمله خواهد کرد -   تلویزیون خبرگزاری ایران، با استناد به یک منبع امنیتی آگاه.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/18409" target="_blank">📅 08:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18408">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بیانیه سپاه پاسداران انقلاب اسلامی
بسم الله قاصم الجبارین
قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ
ملت شریف ایران، ملت کریم و مجاهد عراق؛
آفرین بر شما مردمان مومن و بصیر و وفادار که با موقع‌شناسی و تشییع بی‌نظیر در تاریخ جهان قدر و منزلت ولایت الهی و عشق عمیق متقابل مردم و والی اسلامی با مرام امیرالمومنین (ع) را به رخ جهان کشاندید و با شعارهایتان یادآور شدید که هزینه تعدی به مرجعیت و ولایت فقیه مسلمانان بسیار سنگین خواهد بود.
هرچند این تشییع باشکوه به ویژه ۲۳ ساعت تشییع عاشقانه در گرمای شدید سرزمین عراق حبیب، مستکبران کاخ‌نشین را وحشت‌زده و آنها را به واکنش عجولانه به این قدرت نمایی مردم واداشت و آمریکای عهد‌شکن با زیر پا گذاشتن همه تعهدات بار دیگر نقاط متعددی از استان‌های ساحلی جنوب ایران و در اقدامی ضد مردمی دو پل در استان‌های شرقی به سوی مشهد مقدس را مورد تجاوز قرار داد تا اخبار این حماسه بی‌نظیر را تحت شعاع قرار دهد و این رویداد الهام بخش را از نظر مردم جهان پنهان دارد، غافل از اینکه این جنایات مردم جهان را بیدارتر و آنها را برای نقش آفرینی در مبارزه‌ با شیطان بزرگ مصمم‌تر خواهد کرد.
رزمندگان اسلام تجاوزهای ارتش کودک‌کش آمریکا را بی‌پاسخ نخواهند گذاشت.
در اولین مرحله از پاسخ تنبیهی علیه پیمان‌شکنان آمریکایی، رزمندگان نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی، ساعتی پس از حملات دشمن و نقاط مختلف کشور، زیرساخت‌ها و تاسیسات مهم دو پایگاه‌های استعماری اشغالگران آمریکایی در عریفجان و علی السالم کویت و جفیر و شیخ عیسی در بحرین را در هم کوبیدند.
سپاه پاسداران انقلاب اسلامی به ارتش کودک‌کش آمریکا اخطار می‌کند که در صورت تکرار تجاوز پاسخ‌های کوبنده ما به سایر پایگاه‌های آمریکایی در منطقه توسعه خواهد یافت.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18408" target="_blank">📅 08:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18406">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">به نظر شما ترامپ با این سه سگ (اردوغان، فیدان، کالین) چه صحبتی می تواند داشته باشد آن هم وقتی که جولانی هم دارد به اینها می پیوندد؟!</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18406" target="_blank">📅 02:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18405">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mINnwCxUCA0EM2GGCyN5BT4aUGOW0hI_XNupdistGLfS97wosLX1rQT4Tuzu3235N3WzCc3YZTV4x6kdhXxy7MFC2seyirZ4NuXCEzn9lCWP4Ne0wCDv23Kpnd6nNQadH7n3zxlXyU8ZLbbwC2gFjH2vKy1cT5_Mn4eLW6wbBl9xXFcqVK1KVZz-6AAdGQFJ34deXMkhqVb6JIdc7kGthVurquHlvEsMRl1OTw9PvT1yMPngTlXv0nM0dfEJmE3DMyCHKcrp1P-kPuitYtTrLZO8sLAgi4eHYjF90Y3aQsbnMR53kmo0BRVmmv1iwEYD4HYQhu7B_YdeYjfCMfdRYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در حال انتشار زنده ویدئوهایی از حملات آمریکا به ایران در امشب است</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18405" target="_blank">📅 01:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18404">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مقر تیپ 110 سلمان فارسی نیروی زمینی سپاه در زاهدان بمباران شده است.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/18404" target="_blank">📅 00:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18403">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">زاهدان</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/18403" target="_blank">📅 00:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18402">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ابوموسی</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18402" target="_blank">📅 00:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18401">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تماس شبکه خبر با اژدهای بندر!</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18401" target="_blank">📅 00:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18400">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu_CK4ATAnVoDNV3fuwP8Hao8eiTaHuH2Lmtocev-6EGrlgIIBXa4aun8trxfBxGc_yXMerbP4c1UtiPYkdzqTcbUc5Olm_eOS2oGvLnBYAD3NlfZb2A2E_YVTiwsRr6xZpUifao1X5rZnm1RY-p2zoEuMJIFdeBBtNsFkiRCc3ZUGPbEH90C4jO3SodqIRVVjpBQNZX4XtW4U6sFFhM3U_Zwk2y6GhKMBsfILFAKL375CvwZUyVaWPHSHdaW2f-JEc-DB9ClYH2h1_SuXfgoBf7KfV6_i4kowFD-CpaaFpf3tlhuDEFtO-sjKzMAACPxxJ0Se9MvGLObKoTp2ugfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/18400" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18399">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گفته می شود تا 200 هدف امشب مورد اصابت موشک ها و بمب های آمریکایی ها قرار گرفته است.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/18399" target="_blank">📅 00:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18398">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انتشار اخباری از آماده شدن پرتابگرهای موشکی سپاه</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18398" target="_blank">📅 00:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18397">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خارک، قشم</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18397" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18396">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تسنیم:
براساس برخی اخبار غیررسمی، پایگاه امام علی نیروی دریایی سپاه در چابهار توسط جنگنده‌های آمریکایی مورد هدف قرار گرفته</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18396" target="_blank">📅 00:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18395">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عربستان سعودی در حال پیشبرد طرحی برای کنار زدن اسرائیل از کریدور اقتصادی هند-خاورمیانه-اروپا، معروف به پروژه «راه‌آهن صلح»، با تغییر مسیر این کریدور از طریق سوریه به جای اسرائیل است.
دو منبع به نقل از جروزالم پست</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18395" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18394">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کی حضرات می خواهند بفهمند که ادامه این مسیر احمقانه یعنی نابودی زیرساخت های باقیمانده کشور و سپس ایجاد یک دولت شکست خورده و نهایتاً تجزیه ایران؟!</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/18394" target="_blank">📅 00:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18393">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کی حضرات می خواهند بفهمند که ادامه این مسیر احمقانه یعنی نابودی زیرساخت های باقیمانده کشور و سپس ایجاد یک دولت شکست خورده و نهایتاً تجزیه ایران؟!</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/18393" target="_blank">📅 00:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18392">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnNsJiJf6RT-1dGNfxtGZSIqA6zypy6TjUrKR3LiNugxc7cnYYd_FB_VJGNjpazgwxLZimK2d0enIPjNktvTLR8gj3PjpviaRnPRNJGkDjlqa0YA6MgX-1Hv3cfTCtY3IgtORhIG847jWOTEey076qF12VCsqwwwJaob-gt2alTHH1lUM7AwTFprKl4DAym-ir-2erDZ_ZvZWQh-JQ_gBUuWgkyxzNU-5OUf4i-fPtPbjUMqHrL0auqIwVvjYveBbLUueXl238yEUVovFqmkUMrFyMgRm-0oPCTa9jS6_GwH_Gng-6z1PvdAXkHB3AJ_VP-3K3cFHCGjJUTb4EEvLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروگاه برق چابهار ه زده شد و برق قسمتهایی از شهر قطع شده.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18392" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18391">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حمله به پالایشگاه ها هم آغاز شد...</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18391" target="_blank">📅 00:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18390">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حمله به پالایشگاه ها هم آغاز شد...</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/18390" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18389">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بوشهر، لاوان، چابهار….</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/18389" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18388">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18388" target="_blank">📅 23:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18387">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">At the direction of the Commander in Chief, U.S. Central Command forces have started conducting additional strikes against Iran to further degrade their ability to threaten freedom of navigation in the Strait of Hormuz. The United States is holding Iran accountable…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18387" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18386">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromU.S. Central Command</strong></div>
<div class="tg-text">At the direction of the Commander in Chief, U.S. Central Command forces have started conducting additional strikes against Iran to further degrade their ability to threaten freedom of navigation in the Strait of Hormuz. The United States is holding Iran accountable for recent unjustified aggression against commercial shipping and civilian crews freely navigating a vital international waterway.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18386" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18385">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبرگزاری آکسیوس :
ارتش آمریکا امشب حملات بسیار سنگین تری را به ایران انجام خواهد داد.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18385" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18384">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/18384" target="_blank">📅 23:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18383">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">به نظر شما ترامپ با این سه سگ (اردوغان، فیدان، کالین) چه صحبتی می تواند داشته باشد آن هم وقتی که جولانی هم دارد به اینها می پیوندد؟!</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18383" target="_blank">📅 22:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18382">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">در ساعات اخیر، ایالات متحده شروع به استقرار مجدد هواپیماهای تانکر سوخت‌رسان در اسرائیل و خاورمیانه کرده است.
— خبرگزاری اسرائیل</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/18382" target="_blank">📅 20:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18381">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">واکنش غریب‌آبادی، معاون وزیر خارجه به تهدید ترامپ به حملات بیشتر:    با ترامپ جنایتکار و قاتل باید با زبان خودش صحبت کرد، ظاهرا زبان زور را بهتر می‌فهمد   کاظم غریب‌آبادی، معاون حقوقی و بین‌الملل وزارت امور خارجه در شبکه اجتماعی ایکس نوشت: اظهارات امروز ترامپ،…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18381" target="_blank">📅 20:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18380">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">واکنش غریب‌آبادی، معاون وزیر خارجه به تهدید ترامپ به حملات بیشتر:
با ترامپ جنایتکار و قاتل باید با زبان خودش صحبت کرد، ظاهرا زبان زور را بهتر می‌فهمد
کاظم غریب‌آبادی، معاون حقوقی و بین‌الملل وزارت امور خارجه در شبکه اجتماعی ایکس نوشت: اظهارات امروز ترامپ، از توهین به ملت ایران تا تهدید به حملات بیشتر، نه نشانه اقتدار، بلکه اعتراف به شکست سیاستی است که سال ها بر زور، تحریم و تهدید بنا شده و نتوانست ملت ایران را به زانو درآورد. با ترامپ جنایتکار و قاتل باید با زبان خودش صحبت کرد، ظاهرا زبان زور را بهتر می فهمد!</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18380" target="_blank">📅 20:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18379">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ:  اردوغان، طرفدار پروپاقرص نتانیاهو و اسرائیل نیست.  اما او در آن جنگ دخالت نکرد.  او می‌توانست به راحتی وارد آن جنگ شود، اما به درخواست من، از آن جنگ کناره‌گیری کرد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/18379" target="_blank">📅 20:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18378">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ:
اردوغان، طرفدار پروپاقرص نتانیاهو و اسرائیل نیست.
اما او در آن جنگ دخالت نکرد.
او می‌توانست به راحتی وارد آن جنگ شود، اما به درخواست من، از آن جنگ کناره‌گیری کرد.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18378" target="_blank">📅 20:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18377">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اظهارات ترامپ درباره ایران:  به نظر من، جنگ با ایران دوباره آغاز نخواهد شد.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18377" target="_blank">📅 20:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18376">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فوری | ترامپ: حجم زیادی نفت از تنگه هرمز عبور می‌کند و ما به دنبال یک جنگ طولانی نیستیم.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18376" target="_blank">📅 20:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18375">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فوری | ترامپ: حجم زیادی نفت از تنگه هرمز عبور می‌کند و ما به دنبال یک جنگ طولانی نیستیم.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/18375" target="_blank">📅 20:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18374">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فوری | ترامپ: حجم زیادی نفت از تنگه هرمز عبور می‌کند و ما به دنبال یک جنگ طولانی نیستیم.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18374" target="_blank">📅 20:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18373">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ خیلی صریح محمدباقر قالیباف رئیس مجلس ایران را به ترور و حذف فیزیکی تهدید کرده و او را "محمد یه چیزی..." (Muhammad Something) می نامد و با تمسخر می گوید اسم نصف ایرانی ها محمد یه چیزی است و ما می توانیم آنها را از فضا شناسایی کنیم و اگر نزدیک منطقه ذخیره…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18373" target="_blank">📅 20:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18372">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ درباره ایران:
می‌دانید؟ ممکن است من کشته بشوم.
من هدف شماره یک آن‌ها هستم.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18372" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18371">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اظهارات ترامپ درباره ایران:  آنها با نرخ تورم ۳۵۰ درصدی مواجه هستند. زمانی که جنگ آغاز شد، این نرخ ۵ تا ۶ درصد بود.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18371" target="_blank">📅 20:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18370">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اظهارات ترامپ درباره ایران:
آنها با نرخ تورم ۳۵۰ درصدی مواجه هستند. زمانی که جنگ آغاز شد، این نرخ ۵ تا ۶ درصد بود.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18370" target="_blank">📅 20:00 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
