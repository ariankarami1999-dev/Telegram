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
<img src="https://cdn4.telesco.pe/file/Kg87VKarncqgkm8QpXvt91sKZ1ANKTgg08HI9G3zF4Kmr8UGxQmJwUxUGThgygdY-CbphDf8UWngmdklL25Tf23xfbTazrYM7aU8adMLSlPYm42BRWNuGOkHxXDMOKnaiy0bZ79NlEwk-G2akS_-IpoCKS6muwGrfiisTUlKxjo8H2FNeX7UOtEBLYyLhqEn9z6jN_nwNdOIlj70eMenVJdeMDq2ffu3xUM3UEALJl54foCUYHx-VIRm_fjTDQQRirxSBbjLTl3A5o5FYyYCpW1xvXL1MejOosPd1ijBWi6BsP1WWNDnvMWn50PZd1c4c9hH7ARHU8gn6crMZtilIw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.5K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 01:08:36</div>
<hr>

<div class="tg-post" id="msg-19495">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه ایران:  "مصر یک دوست و شریک مهم در منطقه است و امنیت آن برای ما از اهمیت بالایی برخوردار است.  ما همگی باید در برابر توطئه‌ها و عملیات‌های فریبکارانه اسرائیل که با هدف تضعیف صلح منطقه‌ای طراحی شده‌اند، هوشیار باشیم.  تهدید آشکار،…</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/SBoxxx/19495" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19494">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">به نظر می رسد مصر هم کم کم به لیست اهداف مشروع ما بپیوندند.</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SBoxxx/19494" target="_blank">📅 00:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19493">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SBoxxx/19493" target="_blank">📅 21:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19492">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">— منابع یمنی معتقدند که عربستان سعودی در حال آماده‌سازی برای یک تهاجم نظامی بزرگ علیه حوثی‌ها از طریق دریا و احتمالاً از طریق خشکی در یمن مرکزی است تا گلوگاه صادرات نفت خود را در دریای سرخ جنوبی آزاد  کند.
— گاردین |</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SBoxxx/19492" target="_blank">📅 21:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19491">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وزارت دفاع آمریکا، قرارداد ۵۸ میلیارد دلاری برای سیستم پدافند هوایی پاتریوت به شرکت لاکهید مارتین اعطا کرد.
این قرارداد به ارزش تا ۵۸.۶ میلیارد دلار، مربوط به موشک‌های رهگیر پاتریوت است و تولید این سیستم را تا سال ۲۰۳۲ افزایش می‌دهد. این اقدام در حالی صورت می‌گیرد که درگیری‌های مداوم در ایران و اوکراین، ذخایر سامانه‌های پدافند هوایی آمریکا را کاهش داده است.</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/19491" target="_blank">📅 20:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19490">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">329.6 KB</div>
</div>
<a href="https://t.me/SBoxxx/19490" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 15</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/19490" target="_blank">📅 20:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19489">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/19489" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19488">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">در صنعا توفان و رعد و برق شده، فکر کرده اند عربستان حمله کرده !</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/19488" target="_blank">📅 19:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19487">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رهبر حوثی‌های یمن، عبدالملک الحوثی، درباره عربستان سعودی:
آن‌ها دام‌ها را نابود کردند؛ شترها و گوسفندان. حتی حیوانات بارکش و الاغ‌ها نیز از رژیم سعودی در امان نبودند.</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/19487" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19486">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/19486" target="_blank">📅 18:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19485">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICtpbGXJfmrC1ii6U-EKa8oYff2h4Tb9ri-MwHz-z_uuvm4tGTEfsg9WmGNjsyVcc5uy6mhVppSmGJq1bD20VYmLrEaxgcDFPVXDfEMhGpfZ-0W5PEEYuzi-7-Hb38LcJwp8QvMHaSCzBokZAdOTBRNQ8inyAPNc62zxw76mrwPKdvJfkq65BIKhmEUNCK9mWTb1JJmnR11vz-aq_7kN_jCxucnem35_Ru2w0bSOkZpyrT2_D4WeR_LMGv2LLSv2oQXsnHCKiNceIzlPT2CgGososZFO_6jyYjmGEReHTqeDrhcRxEN3whpRvxUDPU8xBx-tO_x0laEwMcYuCWeUhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما ببینید در روزهای اخیر اینها به لیست اهداف مشروع ما افزوده شده اند:  — بلغارستان — بریتانیا  — اوکراین</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/19485" target="_blank">📅 18:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19484">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i05BOmMExO-ghRp-eg6iKraNsMMVgfgIoF92PVvZyrabLWRO_1SDSK7PRwvIHgsNXBEo4DJXP2cfjKE1Gv2Gtt3C9YqkC_ddJvwPCrkfHvqKCNF0kN3JAoyRLqiGUSpOQUbB4rXUbKrvuxqd2lwN_NoZOpKyR9PAkaLDhDcfoOIma5pdjgvN1IsUtZGiptYMKSUsyFViBm4KCu4A_aZjup3QHblXQj6HKEd0ZrecQbbXhWWuzhZ7xd2pNtEtptLtytVBxGQASFhkaiSqg6qNyUtdwU36lVZD__FoHfdhA5XCfqkdhCz5Cp-jNV9qrk3ZmNo7NJi1HTP8Y-L452r1WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/19484" target="_blank">📅 18:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19483">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">روسیه ممنوعیت صادرات بنزین را تا سال ۲۰۲۷ تمدید کرد!</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/19483" target="_blank">📅 18:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19482">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">— مشاوران و اعضای کابینه ترامپ گزینه‌هایی برای انجام عملیات نظامی گسترده‌تر علیه ایران را به وی ارائه دادند.
— فاکس نیوز</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/19482" target="_blank">📅 18:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19481">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سپاه پاسداران: ایران پایگاه هوایی الازرق را در پاسخ به حمله آمریکا به قشم، با نابودی سه فروند اف-۳۵ حمله کرد
سپاه پاسداران انقلاب اسلامی حمله موشکی انتقام‌جویانه به پایگاه هوایی العزرق در اردن را پس از حمله آمریکا به خانه‌های مسکونی در جزیره قشم اعلام کرد.
طبق بیانیه سپاه، این حمله به منطقه استقرار و محل نگهداری اف-۳۵ هدف قرار گرفت و سه فروند از هواپیماهای اف-۳۵ را نابود کرد و سه فروند دیگر را به شدت آسیب رساند. چندین افسر آمریکایی و پرسنل فنی نیز کشته شدند.
سپاه گفت که این عملیات در پاسخ به حمله آمریکا به قشم انجام شد که منجر به زخمی شدن اعضای یک خانواده محلی، از جمله کودکان، شد.
در این بیانیه همچنین از اردنی‌هایی که با حضور نظامی آمریکا در کشورشان مخالف هستند، تشکر شد و گفته شد که موضع آن‌ها فشار بر نیروهای آمریکایی را افزایش داده است.
سپاه در پایان با تأکید بر ادامه عملیات علیه حضور نظامی آمریکا در منطقه، بیانیه خود را به پایان رساند.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19481" target="_blank">📅 14:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19480">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کشته شدن ۳ عضو سپاه پاسداران در حمله آمریکا به زنجان</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19480" target="_blank">📅 14:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19479">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19479" target="_blank">📅 13:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19478">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwGbeCxKraa7e6UQHIKbMxCVdjY4zzq78jptdzcBlwsAvb3GlmpQVT4CDTJYBO6vu_F6ut_5DLjiOWTq3cTK6qAA-bidDzB7I7FJVg_Q4BfACPRWnfyrAEo8pKT70avytZIaByVvWd6CPd85aQqS5yuqiFLA4hAJUdwS_kCk4tSxQtqqCIFycwMXjICBoSw-GjhHh4kDBAB2JvkxswDTJpLK0NMR-uy4SkM-eYcnMjXELtGPO1KtIrhhDiniP9SXTmUidiP-Jj1ItfMUmKhHcbe4QBloaB1XUSJDHZv1cFlJEyz4RfNY-51uZZ2Y8OY6P-JesNe71dSnO5F5EkGbaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لینک نشست دیروز با نیما</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19478" target="_blank">📅 12:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19477">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8eacd406a.mp4?token=Nbtts1XfrD729VJ5ywGwa-b4j_5GKPfDyr1ZzXzlna7y6M16T_54G1pwbmmGkQuYRfsaSG759yk_SmfpFlOF2eBaG9pnrKzKVpXUWLQ3-GgsOYpoWqaUnKzeLNueg6ZsZOVHljZN5K-ZexZWIWdb2stQhmV6Mmc0jOxQk8clVmQYR7lyVB4USODYoxfSHkrHxiwFp-ZTAQhFAThkAwFgnzdy5uif8LC9TD74mdPl4y_GhFmC_1beIXW15bYJg_Ff-0zz4zJZdFgjFlwkzw38ZSStrjVBz8GJEkMy0WjgVNJ8EiJIHZ5O0nwaXTrmed-Ne6i4geCSfFFl93-Ea0rtRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8eacd406a.mp4?token=Nbtts1XfrD729VJ5ywGwa-b4j_5GKPfDyr1ZzXzlna7y6M16T_54G1pwbmmGkQuYRfsaSG759yk_SmfpFlOF2eBaG9pnrKzKVpXUWLQ3-GgsOYpoWqaUnKzeLNueg6ZsZOVHljZN5K-ZexZWIWdb2stQhmV6Mmc0jOxQk8clVmQYR7lyVB4USODYoxfSHkrHxiwFp-ZTAQhFAThkAwFgnzdy5uif8LC9TD74mdPl4y_GhFmC_1beIXW15bYJg_Ff-0zz4zJZdFgjFlwkzw38ZSStrjVBz8GJEkMy0WjgVNJ8EiJIHZ5O0nwaXTrmed-Ne6i4geCSfFFl93-Ea0rtRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبور موشک های زمین به زمین اتکمز آمریکایی بر فراز شهروندان کویتی به سمت شهرهای خوزستان</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19477" target="_blank">📅 11:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19476">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0Z0PbuiMZnDtwcurh6V-gJZ_jwItul-H4CWMmTmuMnIGSum8UGJd9bBVVlq-putJC7km0XsuI3c4ttQCBe8iYSiQuYXOdnkVM7_TJLcDayQ36UC39zumkYYMUBi2ALxdsl6EcaIAa4PJJjqs_YRp2HbD0bBT2FBPvjr7jIhQT96I1IqcS7iVwKGHNRKYJsoc20zWGanLJwiO6l0uowrFrU9QGZ0cE34kr6c1XLzqnvdZKoCf8nevvoV6hOFiRVSNYiTfqCBWhv_WycDRrGKP2AOBlL_CahYhIDrG1YFUgOUPHcLDIkjkJVYsk9l8yx-6xrADSDsbdvYSIa9l2hgNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این همان حرامزاده ای است که دختران را در لایوهای خودش کتک می زد و به آنها اهانت می کرد که خوشبختانه به این روز افتاده و تا مدتها نخواهدتوانست شرارت کند.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19476" target="_blank">📅 11:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19475">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhDcbGfmKpzF181DV2f6gZXhpDpVIOk9vkIuzoI-VxqqYiAAIA_pmo5xjFpkoBHfXBT29eb_17FkWIFFh1FiLjG08RjBXHPJAvvknTBfoJkwUcVVlsadxzgQl3z20eiEjqR8T7C7g18PgW_4AyOL_qzWckjXNoE-ta_s4TF-Y-8yr0n8bSwAuyeLjJZQVZuXqOF439fsSz-JsZphKCV9qQv5X6-a3PQKNQNV3i4uqLE6Qlw67B1vGv3iXCOa16AUduXn9UFfBZDHsHtKzZ3T7DVPMPy6DXDLd__iMOKOhBIV25vY-hsj55xKMKnfGjGvJI4NshIOvc42Ctr1VUKQuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/19475" target="_blank">📅 11:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19474">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-xVlZ6l2gic-d18GpJzLZeMUUWNZMhW53sft70QSRi65iFDH-VM8gc-H9a6ZkBsGDI8p51yUuKjoiTx0hJNNrHyiumNXbb7cSkAP92rFNShBlfNZuVxfef-c0IEVQya5TrA_WLe3ffLjkwhgqQwawtiQrN0PMTww18e2mnico_7KeODsusBPDeIe2DHWj1ZtUXBfI55rL7d64aiVcUbDQmmFJV6w9pn4mRAsjzjLo2Cr_rVXkwKoPUd-Ms-fk-b8QWfW_g46KBwGyvtFzAmAefVsHK52giVvch1JY5raCBZOgD-Uh3xUGsH9gOJPVyMO76y4D4xNBsfLNZq-lvj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهداف حمله پریشب حمله مشترک سعودی و آمریکا به پایگاه های حشدالشعبی در عراق</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19474" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19473">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سپاه پاسداران:
با استعانت از خدای متعال، متجاوز همین امروز تنبیه خواهد شد.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19473" target="_blank">📅 11:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19472">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vipeNuwlNS9_cNDx9w-cwD-xd2g6fhP448mGG8zcHBsxEjeHHXYUDU739tje4ta_kA3VDMd7YTtYxnBHaBiREnv4aIVVrPTGAxTMtSBzq_d05kevCVeGzfHX6X6CqVRVno5BSldVPuEtOtLW7seAJDgjgiT5lHDfuB3t02uXBFlnBfykTc8-22cFTFzLQ6vSqOA71FWCKS8dqxMPvqz0FXZfJc43o9sNKYhzfOcX4hUXQ-yrJ61R1e3Zk0y_m_U9MX_4nfaUgPOJyphvt8a3E622q6kt697WAcBEv5mqHPPGhNWijnwakSDgXXqhUtD-nMtZy7rxJmYk-uRQBwMXCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح میانه پایین است و حالت رنج برای طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19472" target="_blank">📅 11:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19471">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19471" target="_blank">📅 10:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19470">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پرسش: اوایل این ماه، رئیس‌جمهور ترامپ در مصاحبه‌ای با یک خبرنگار گفت که در رابطه با شما، همه می‌دانند که چه کسی رئیس است، یعنی خودش. او کسی است که تصمیم‌گیری‌ها را انجام می‌دهد. آیا شما هم این‌طور فکر می‌کنید؟
نتانیاهو: خب، شما می‌دانید که در آمریکا اغلب می‌گویند ترامپ هر کاری را که من می‌گویم انجام می‌دهد. و در اسرائیل، اغلب می‌گویند من هر کاری را که او می‌گوید انجام می‌دهم.
و گاهی اوقات، این مسائل توسط هر کسی، از جمله رئیس‌جمهور، در بحث‌های عمومی مطرح می‌شوند. اما حقیقت این است که ما شرکا هستیم. ما متحد هستیم.
او شریک ارشد است. این کشور ایالات متحده آمریکا است. بیایید این را فراموش نکنیم. و من شریک فرعی هستم، اما من نخست‌وزیر اسرائیل هستم.
و وقتی لازم باشد، من برای دفاع از منافع کشورم و امنیت کشورم، این کار را انجام می‌دهم.
منبع: خبرگزاری ABC News</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19470" target="_blank">📅 10:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19469">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نتانیاهو:
ترامپ اساساً سه گزینه پیش رو دارد: اول، دستیابی به یک توافق؛ دوم، ادامه محاصره؛ سوم، اقدام نظامی.
هر چیزی که منجر به پایان برنامه هسته‌ای ایران شود، چیزی است که ما می‌خواهیم. این هدف مشترک ماست.
س: وقتی با ترامپ در کاخ سفید ملاقات کردید، آیا تلاش کردید او را متقاعد کنید تا حملات به ایران را از سر بگیرد؟
نتانیاهو: در واقع نه. این یک تصویر کاریکاتوری یا تصویری اغراق‌آمیز است. این درست نیست.
ما در واقع تمام سه احتمال را بررسی کردیم، و من فکر می‌کنم که این کار را به صورت شفاف و در بین دوستان و متحدان انجام دادیم.
و این تصمیم اوست. این تصمیم اوست.
منبع: خبرگزاری ABC News</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19469" target="_blank">📅 10:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19468">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شب گذشته یک منزل مسکونی در قشم مورد اصابت پرتابه آمریکایی ها قرار گرفت  احمد نفیسی معاون استانداری هرمزگان از حمله دشمن به یک منزل مسکونی در محله چاه‌تنگو شهر قشم خبر داد و گفت: تیم‌های امدادی در حال جست‌وجو برای یافتن دو یا سه فرد محبوس‌ در زیر آوار هستند.…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19468" target="_blank">📅 09:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19467">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فیلم سنتکام از هدف قرار دادن اهداف در حمله بامداد
چند پرتابگر متحرک نیز دیده می شوند</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19467" target="_blank">📅 09:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19466">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حمله موشکی ایران به اردن</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19466" target="_blank">📅 09:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19465">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شب گذشته یک منزل مسکونی در قشم مورد اصابت پرتابه آمریکایی ها قرار گرفت
احمد نفیسی معاون استانداری هرمزگان از حمله دشمن به یک منزل مسکونی در محله چاه‌تنگو شهر قشم خبر داد و گفت: تیم‌های امدادی در حال جست‌وجو برای یافتن دو یا سه فرد محبوس‌ در زیر آوار هستند.
احمد نفیسی خاطرنشان کرد: جزئیات تکمیلی این حادثه و وضعیت افراد گرفتار، پس از پایان عملیات امدادی و ارزیابی‌های میدانی اطلاع‌رسانی خواهد شد./ایرنا</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19465" target="_blank">📅 09:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19464">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19464" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19463">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19463" target="_blank">📅 09:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19462">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حمله به آبادان</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19462" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19461">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbDejjPFPEpF8sE2XP0pz66x8VWD0QPaxltmnRiX0Ki761Qiym19oLFo-no3S4ewsmrZjuUb7eAry8MuqpzerJebe2RGX4RP4VQHImPsoR153epAPxNBGThr9U73UvFJK6AWofC6o0-Gtd4aoKIJLTPl1uI8mOrB4MP9O7AWElixBijQA3ABGzdBEb9okPer2dEGEWGjFdW26fn5avzGuN0b_F3H_FJoP3LXSrsSAsFY5a1eC4Vrmmr2F8oWTRUkfOKe67exOeELhcUcI_cKZe7MRid2pMJYUmNtY2tiBezhYhW13qtN1FeVeqWCK2bEEuDJGSNlVM5n7bzC2BfRkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات آمریکا تایید شد</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/19461" target="_blank">📅 02:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19460">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">چندین انفجار در ریاض، عربستان سعودی، و بسته‌شدن باند فرودگاه پادشاه خالد در ریاض.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/19460" target="_blank">📅 01:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19459">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انفجار در اردبیل و ارومیه (تایید نشده)</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/19459" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19458">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngCDfv3UOEMuHrLYtcLAbm_304IgmNZSJhH5FaQLm7bjILDMqS7B_LndOG0e_s4xS9zLB-j-5xgqirMK8mrUl1phPdxiMduHKVUpZ6mCoA7grtd72P_p1f33qIf-BEaV9LpwNwnk9Qfba3MY972qIqG8oDEBIzD7QXPELw_6dzi6OL-4WcBnYYBldm8o_puteaUQo1R899BfIwKY_g12ZlxB9Mhf8ggrvJ5It7mRCuQrZ1c_nFMD6KO3vcV2aofmlIB-dTXP2MxZlaG5Kdd11yCYtkv3JX9-C6V60xGeb_F1q5FVEyhbtFWc5Am-wBIdLFTPAZiUtmVTmoP2eGKZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا که اخیراً محبوب حضرات شده بود و چهره یامال را روی موشک ها میزدند، اعدام های اخیر در ایران را محکوم کرده و خواستار تعویق اعدام های برنامه ریزی شده شد.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19458" target="_blank">📅 00:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19457">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONi6ImkgQqLz9ePbvHZpiORgwp0qReMm3HH7e9e-LTcg_up-eJOgtHaMOqHKmhOJPtubDC8AVZPXUE-uYb6gV4B2tKSo1FDBY84FnEsBAt5nIno05xKGGLYCBT1dcingbibbFTCB_5oucbJVgJxS-s2i62ux8AL83mPioeITG1NAzIvMiTn9RtbkCbfYqTqFYP-OJM0Ew85FTIlSKb1qAzBEUJK1MdxcX5HUsc825BR3CnP7KH_XYa6BbTyiAcwbhscUaou3_qOm0WBNxFCUMf0UqDbesWo8TCyqtkhorsto9iAjENSjACLU96KyZS0TBYOVHzj5MRaTtMq97EQ_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا که اخیراً محبوب حضرات شده بود و چهره یامال را روی موشک ها میزدند، اعدام های اخیر در ایران را محکوم کرده و خواستار تعویق اعدام های برنامه ریزی شده شد.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/19457" target="_blank">📅 00:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19456">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uK-b1reWTdNL-LLJU1SeoWUbTJ32tudOGH-omgwWXvcOJaWmt5RL_crMGZ6J_H--qI6X4uMCcVWZMYpooaqb1oX0zCduONKrE0oSFMlhryaX-jCxSj5bt0DfuIyPSY0fGXCSIaX21DjClChl8Z4ihjc3Tk-jwHJ-PpkxYE4-VwzOTXj1N7p30FUTosEMDg-8UUOANeIZb_dnPeTdJ79RYA9UI3ZvcztK1J9rOBXDuxLu7e_R_qTQmsyBbaX6ALs7jI_8tu83jlpWX4RqoxNLWet9CqrzbMMhbwSWtDKwuohi3V8cWEuUOQU9aTRYSsJ-AZcbnvgC6tPkbiOuIoVYUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیدوارم آن یک هواپیمایی که نزدیک تهران است جنگنده نیروی هوایی ما باشد.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19456" target="_blank">📅 00:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19455">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر
به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19455" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19454">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlSfklmWHEHLiEfNJJoRo0BYRgH78_2yh3QsvKi-LtRMvVnzjQ6P2jCQFRvweUPm1GPBp7HMQlCr3xfkqj3Sg_JZVwPMxOYXBe-1lUjB3T_2xhs3UmqIGy-rrQQ5RlrT9qeTftlk4iy2KUPLKY740WCbcEAVeT6Mb9S-9GIQv0NVYQkPZTvduHxENEvDGm1kVkkqD2LGS_uilWZNVVn7zaKKki_w6OsKyKyI4q6pK-ZCLdKH4rXx4JcmmdDkBRfuXb7xxvS7xTuWECWOWJ3Z3jvIrQKviC6tcshvuQREnKcTZHcLYPvDpas0PmbhkPL_E4KyF72j5T_ihX6TRZC5PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز هم در وضعیت مناسبی قرار دارد و انتظار رشد طلا می رود.  دقت کنید که امشب نشست سرنوشت ساز FOMC را هم داریم که سناریوهای موجود در این یادداشت بررسی شده است.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19454" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19453">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3185a6e49f.mp4?token=YUALPLjF-5f0RPvMY3P-yB4xND5rkA4mTpSQeSrtsIdUD47uOmkjFl2y5v0d4GY07tJ0Ix0me-KvIgEvB5zms8IsgSfNkwFq7f11BPMsiXuda_B1UepPLVn8pfiwRLb4XOeeXWRYXbittqb6GXIZfILBoJIjIvDwSDvX4bJiNpLhAT0zUYcsh9Yol9ajtaSfwnZ4DG1dvKshfZxxUVtbvRs9wBamJPGz5woDA8NvjuLwDLkgs3h4WQQcakOfKuVgQhzdJpFHpF7vkfwXP7p5T2rTHzabm_Zxfu-HpT3YgTmb3xQeV2DoQR74UP2-NsJ8fTRoXXZC7QwQ4-H67T5gVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3185a6e49f.mp4?token=YUALPLjF-5f0RPvMY3P-yB4xND5rkA4mTpSQeSrtsIdUD47uOmkjFl2y5v0d4GY07tJ0Ix0me-KvIgEvB5zms8IsgSfNkwFq7f11BPMsiXuda_B1UepPLVn8pfiwRLb4XOeeXWRYXbittqb6GXIZfILBoJIjIvDwSDvX4bJiNpLhAT0zUYcsh9Yol9ajtaSfwnZ4DG1dvKshfZxxUVtbvRs9wBamJPGz5woDA8NvjuLwDLkgs3h4WQQcakOfKuVgQhzdJpFHpF7vkfwXP7p5T2rTHzabm_Zxfu-HpT3YgTmb3xQeV2DoQR74UP2-NsJ8fTRoXXZC7QwQ4-H67T5gVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک غیرنظامی اردنی به طور تصادفی، فیوز انفجاری یک پهپاد انتحاری ایرانی مدل "شاهد" که سقوط کرده بود را هنگام بررسی آن، منفجر کرد.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19453" target="_blank">📅 00:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19452">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
ارتش اسرائیل آماده حمله سراسری و بزرگ به ایران است</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19452" target="_blank">📅 00:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19451">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گزارش‌هایی از پرتاب موشک بالستیک از اطراف یزد در مرکز ایران</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19451" target="_blank">📅 00:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19450">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ درباره ایران:  آن‌ها می‌دانند که این اتفاق (حمله) در راه است. از ما می‌خواهند که این کار را نکنیم.  دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19450" target="_blank">📅 23:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19449">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ:
آندی برنهام باید به مهاجرت اشاره کند زیرا این موضوع بریتانیا را نابود می‌کند.
آن‌ها از آفریقا، آمریکای جنوبی و بخش‌های مختلف آسیا می‌آیند و در حال حمله به اروپا هستند.
این یک حمله است و بریتانیا مظنون اصلی است.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19449" target="_blank">📅 23:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19448">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5e9lOnigrOTsKv2hqL9EX4sOGvCxaQaT74fimLkSkvXHOowW6u2O3lBn9FXg7IfKDV_28ztXuyMPxoI5PQ3Lb5kphWfTofyI0M8nAnkTPnsrgl6XdzOobONcEgJWs-TCJMHNhJIqbyAw-a53Unr9GF6gcUnQMoPvE9WQBjIkXawMHAD-aqg7Uhhuyk-QzZqbWCL7JGPvfdGsApNkimpxZFPRUHrMaiyGcsUXzHfVkfGj-UDOXmQDRHKrli2P0N3fe6th4k3JQnu8UvcYo5pKldcQaPfThmEcBRGhYBYtiyykcCqPTqcTraxHAzcQh3yYOfUE5GzyPeFC52VtwxQrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19448" target="_blank">📅 22:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19447">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها می‌دانند که این اتفاق (حمله) در راه است. از ما می‌خواهند که این کار را نکنیم.
دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19447" target="_blank">📅 22:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19446">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ درباره ایران: آن‌ها را به شدت ضربه خواهیم زد، نوبت ماست.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19446" target="_blank">📅 22:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19445">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">علت رشد طلا در چند دقیقه اخیر:
مقامات امنیتی مصر به شبکه خبری "الحدث" اعلام کردند که هیچگونه حمله‌ای در بندر دمیاط رخ نداده است. آن‌ها مدعی هستند که این حادثه یک آتش‌سوزی بوده که در بخش موتور یک کشتی از رده خارج شده رخ داده است. - خبرگزاری "کان" اسرائیل.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19445" target="_blank">📅 20:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19444">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یک مقام ارشد از یکی از کشورهایی که در این میانجی‌گری نقش دارند: کسی که تصمیم‌گیری‌ها را انجام می‌دهد، فرمانده سپاه پاسداران انقلاب اسلامی است. - خبرگزاری کانال ۱۲ اسرائیل،</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19444" target="_blank">📅 20:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19443">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انفجارات در اردن!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19443" target="_blank">📅 20:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19442">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رئیس‌جمهور ترکیه، اردوغان:
دولت فعلی اسرائیل که تحت تاثیر جنگ قرار دارد، با تحریکات و اقدامات سازمان‌یافته خود، همچنان منطقه ما را به سمت بی‌ثباتی سوق می‌دهد.
اسرائیل با نادیده گرفتن حقوق اساسی بشر و زیر پا گذاشتن قوانین بین‌المللی، به تدریج و گام به گام، سرزمین‌های فلسطینی را اشغال می‌کند.
اشغالگری اسرائیل، سکونتگاه‌های غیرقانونی آن، و سیاست‌های آوارگی، ارعاب و سرکوب علیه فلسطینیان در کرانه باختری – همانطور که در غزه انجام داده است – منبع اصلی مشکلات در منطقه ما هستند.
هزینه این تجاوز نه تنها توسط برادران و خواهران فلسطینی ما، و نه تنها توسط مردم لبنان، بلکه توسط مردم با ادیان مختلف و کل منطقه پرداخت می‌شود.
به عنوان مثال، به دلیل درگیری‌ها در منطقه ما، عرضه جهانی نفت، یکی از بزرگترین شوک‌های تاریخ را تجربه می‌کند.
متاسفانه، این فقط نفت نیست. قیمت بسیاری از مواد اولیه کلیدی در بازارهای جهانی، از جمله گاز طبیعی، کودها، سوخت دیزل و محصولات پتروشیمی، نیز به سرعت افزایش یافته است.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19442" target="_blank">📅 20:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19441">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نتانیاهو:  من همین الان یک گفتگوی تلفنی با آقای پیتر هگست، وزیر دفاع، به پایان رساندم.  او نکته جالبی را با من در میان گذاشت. ایشان به من گفتند:   «ما به جهان نگاه می‌کنیم و کشورهایی وجود دارند که اراده مبارزه در کنار ایالات متحده را دارند، اما از توانایی…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19441" target="_blank">📅 20:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19440">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoteIFk91eG-O4_Gtw0j6FHSwNg9Lb3vZHDdhPrHl6l6FVDfHp0re8o--XXbafOaVnBDMePJ0f19W6yymdjjcM23hLO6sH-1aDCuJ26s2xxBHOhYTRCDl-KlnBllsK7_uGa8TMrdk5FrUjcHeKepvwC0BrJW07XsQQicLZdt3k0Q9ZbjLNoS9gMojZW0-dG7slXjiO5I9aYOj5P80JbzpRXt5FK6M58ljQd9gmWWF6_25Ind1UKSBUX_63GRJZEJuNamGL4AUXK_6fwJxXZcrzgwfOlzbnfcPonpmX2-ezSYaNh4j9uAFCQxjYZLRgnJQ5oLb-vKLl4sqPupxy3Ddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:
من همین الان یک گفتگوی تلفنی با آقای پیتر هگست، وزیر دفاع، به پایان رساندم.
او نکته جالبی را با من در میان گذاشت. ایشان به من گفتند:
«ما به جهان نگاه می‌کنیم و کشورهایی وجود دارند که اراده مبارزه در کنار ایالات متحده را دارند، اما از توانایی لازم برخوردار نیستند. و کشورهایی وجود دارند که توانایی لازم را دارند، اما اراده لازم را ندارند اما فقط در اسرائیل است که ما هم اراده و هم توانایی را مشاهده می‌کنیم.»</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19440" target="_blank">📅 20:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19439">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مقامات اسرائیلی می‌گویند نتانیاهو در جلسه روز سه‌شنبه با ترامپ در کاخ سفید، نقشه‌هایی را ارائه کرد که میزان نفوذ اسرائیل و ترکیه را در سوریه مقایسه می‌کرد.
بر اساس اطلاعات ارائه شده، اسرائیل حدود 0.1 درصد از خاک سوریه را تحت کنترل دارد، در حالی که ترکیه حدود 5 درصد را کنترل می‌کند.
نتانیاهو از این تصاویر برای مقابله با فشارهای قبلی آمریکا استفاده کرد، از جمله تماس تلفنی ترامپ در اواسط ماه جولای که از اسرائیل خواست نیروهای خود را از سوریه و لبنان خارج کند.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19439" target="_blank">📅 19:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19438">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19438" target="_blank">📅 19:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19437">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یک مجتمع شناور ذخیره‌سازی گاز طبیعی مایع (LNG) متعلق به یک شرکت آمریکایی و دارای پرچم جزایر مارشال، در شهر دمیاط، مصر، مورد حمله حداقل یک پهپاد قرار گرفت.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19437" target="_blank">📅 19:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19436">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یک مجتمع شناور ذخیره‌سازی گاز طبیعی مایع (LNG) متعلق به یک شرکت آمریکایی و دارای پرچم جزایر مارشال، در شهر دمیاط، مصر، مورد حمله حداقل یک پهپاد قرار گرفت.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19436" target="_blank">📅 19:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19435">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به خبرنگاران گفت:
«ایران در حال حاضر تقریباً ۱۵۰۰ موشک بالستیک در اختیار دارد.»</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19435" target="_blank">📅 19:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19434">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مقاومت اسلامی عراق با محکوم‌کردن حمله آمریکا به حشدالشعبی در کربلا، به دولت عراق تا ۲۳ صفر مهلت داد تا توانایی خود را در دفاع از کشور نشان دهد.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19434" target="_blank">📅 18:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19433">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مقاومت اسلامی عراق اعلام کرد که انتقام خود را از حملات اخیر ایالات متحده تا پس از مراسم اربعین به تأخیر می‌اندازد تا امنیت میلیون‌ها زائر مختل نشود.   این گروه هشدار داد که حملات علیه نیروهای ایالات متحده اجتناب‌ناپذیر است و گفت که در صورت لزوم عربستان سعودی…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19433" target="_blank">📅 18:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19432">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مقاومت اسلامی عراق اعلام کرد که انتقام خود را از حملات اخیر ایالات متحده تا پس از مراسم اربعین به تأخیر می‌اندازد تا امنیت میلیون‌ها زائر مختل نشود.
این گروه هشدار داد که حملات علیه نیروهای ایالات متحده اجتناب‌ناپذیر است و گفت که در صورت لزوم عربستان سعودی نیز می‌تواند هدف قرار گیرد.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19432" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19431">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رسانه‌های ایرانی گزارش دادند که 4 عضو سپاه پاسداران از کاشان در حملات مشترک آمریکا و عربستان سعودی که در طول شب به سایت‌های حشد الشعبی در عراق اصابت کرد، کشته شدند.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19431" target="_blank">📅 17:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19430">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نتنياهو امروز با پیت هگست، وزیر دفاع ایالات متحده، دیدار خواهد کرد.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19430" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19429">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حمله موشکی ایران به اردن</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19429" target="_blank">📅 17:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19428">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcibGnhR4Ti-OXn1ApE7fqrJSpWKRdEgvvPj6okPfUESffhP1t5aRe7x-vVZVszL5WmXN_KkAY5zD31WmnlcDAMC4YshMQsopFXevdwI-IJTLJvxQpbjjCN5YMZtvO83hCgmMLeP2pXYTnS1-jXJGButl9wEwXce0MIvIe118osE-4KKwR9KAEyztiSv_E3jBbt6tnnJXrBpxhf5QjeCsS8awXnjVehnzoYi-6khx3m21hRxAzwOzjKrMI3onLr7-IdLZXpRhwszS8wr0oJoTqW7E0SvvV9lbKiaJm7E4YGLlHZ8B--wa9ds51ns_wX-qcS9ZnHMTbbO6q3uniiClg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای وزارت خارجه در هدف قرار گرفتن مواکب زائران حسینی در حملات دیشب سعودی و آمریکا!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19428" target="_blank">📅 16:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19427">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19427" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19426">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19426" target="_blank">📅 16:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19425">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انتظار می‌رود که اسرائیل امروز به حزب‌الله پاسخ دهد، اما این پاسخ احتمالاً مناطق جنوبی بیروت را هدف قرار نخواهد داد.
— کانال 14 اسرائیل</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19425" target="_blank">📅 16:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19424">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده:  «حمله دیروز ایران یک غافلگیری بود و نیروهای ما تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.»</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19424" target="_blank">📅 16:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19423">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده:
«حمله دیروز ایران یک غافلگیری بود و نیروهای ما تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.»</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19423" target="_blank">📅 16:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19422">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وزیر دفاع اسرائیل:  در دور آخر درگیری‌ ها جنگنده‌ها و سوخت‌رسان‌های آمریکایی از اسرائیل پرواز می کردند اما ایران همه را زد جز ما</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19422" target="_blank">📅 14:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19421">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پرتابه دشمن به استان آذربایجان غربی برخورد کرد - فارس</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19421" target="_blank">📅 14:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19420">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مطمئنم امین سهامداره  @Piknikanalyst</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19420" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19419">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fjvnYo8hVwIjjDQjY40xDTKGRpwbEVuSmLtbSFPKEGiWjK0nzuY0MAaT0jzoPenx6PEUy80stgxzugN8zwcCbFUhnRSswhaAtSW_DYMCGHi5dkoLFGqkSb0KV4GyVtm_hN1v22XRVg8uFByi5zJU2KoGfgntqz-GbMIW2pw3nvqG_cQ1VvC_uRAb0113ahtd087dAsdXrodV49KVb53xfHFaC4ockxCUPjutKH3DqdwjPYZxO8CmpwAJYbegX8_S4iAxSaRvW14hU9tRAB4EDXymEeF88xMMW0Zht1VDrWo-OiNOIH-ZLLzmTUgYjcb9tTwaqB7ocSI8humr7KmOtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطمئنم امین سهامداره
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19419" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19418">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نیروی هوایی ایران اعلام کرد که جسد سرتیپ مجید کاظمی، خلبان جنگنده بمب‌افکن سوخو-24MK که در تاریخ 2 مارس توسط جنگنده‌های F-15QA نیروی هوایی قطر سرنگون شد، پیدا شده است و طی چند ساعت به کشور بازگردانده خواهد شد.  نیروی هوایی ایران همچنین افزود که مقامات همچنان…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19418" target="_blank">📅 11:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19417">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlCQO6DWtVf3AnggOBD107OzHpsIDdisaiyncdBmq7oI2UW920MJTwsKFdjvQJX7a_6fmvGiMNVTphr8YCcDUdTQJPDV5-cIsJQ0II8q792R5azTMfpLPuWtEFb2AC0yWHcHQErBRApjxShL0CEn381qFFbcM2hagwMbjj6jihmNFYluNY8BQfj4Ljo77qCq5HZnYLLTHchjU3qCyg7gngVthJ6yX5OA2tT75FPvSkIfCP30f7j882tEjFZ7tZhd7R95pLEn_DhQX-3rITyh3FmXLZ9fG7uHxxHUBqg0Oyw75CIX6OS1WcS6LGW6mzJSjO0KqQTxGVrbgjLeocpRtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران تأیید کرد که تعدادی از ناوگان بمب افکن‌های سوخو-۲۴MK اش سرنگون شده‌اند.  این هواپیماها در حملاتی در عراق و سپس قطر شرکت کرده بودند اما سرنگون شدند.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19417" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19416">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a40b3b45d.mp4?token=k-kBm3CLFDglIH3jzzuxDxOhvnB1kZoAFdrsaPMIatM_l4PEum5U9wAjdRaWhnoJARcp5ndCuMeRIts_c7a43WdOgH5Uq40Rq4OlTqKYbvlCUVYAx8-czI18L2RRvYfMln76kTzWQ4d0AMDfJqnk4_i3FkXHJ3dp4b_vEnbTIP57DJruv4UDD0Q-vaF6v4mKsntNDWIBiEJJNLs7GReERcTZKlz9jW6TrJzy-U6hoZgsKkxKiNxc06qYpt_slQu4b3y1KjNx8Qns50QhLv_Xn1rI4MbaYXKOwCTGchEpSlmvJa2xzEJHoyO9Q0I1UjnP-r0AgRr5j2LGni4jE-DJPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a40b3b45d.mp4?token=k-kBm3CLFDglIH3jzzuxDxOhvnB1kZoAFdrsaPMIatM_l4PEum5U9wAjdRaWhnoJARcp5ndCuMeRIts_c7a43WdOgH5Uq40Rq4OlTqKYbvlCUVYAx8-czI18L2RRvYfMln76kTzWQ4d0AMDfJqnk4_i3FkXHJ3dp4b_vEnbTIP57DJruv4UDD0Q-vaF6v4mKsntNDWIBiEJJNLs7GReERcTZKlz9jW6TrJzy-U6hoZgsKkxKiNxc06qYpt_slQu4b3y1KjNx8Qns50QhLv_Xn1rI4MbaYXKOwCTGchEpSlmvJa2xzEJHoyO9Q0I1UjnP-r0AgRr5j2LGni4jE-DJPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمار تلفات حمله عربستان به حشدالشعبی  ۱۰ کشته از تیپ ۳۰ شَبک ۲ کشته از تیپ ۲۴ حشد الشعبی</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19416" target="_blank">📅 11:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19415">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T27lMyn9x1ME8ixD7qIyM8N8gWK1fP_kNh3EyZSM3Tl8URNOZXu9JcKJY0hIozAEE49Ai3jyqTmTEd5wXq1EwN2NsK8nPANS2hYO9D8m_DdB97sqdKEG-Xcti3OewXugCshX89GBiG46gZc-ZVJKcXbT3Lk9DBKXIAG6BbMUKvofcJrYGSfChDHqDAPJLzlXqOP2zfhdsAZmvvGCzyJf982yY5KnK0pHG2FLxoGMre08jfV7vzj3bbQU9O8GXQSNNoykq4Dh6Y5geEmBgIVgmlZIi0E5-Nob1nH0ceniJhn981coPj4V4VqlrlEN7Vla72pNT7R5-Mgp-GC8En6eFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز هم در وضعیت مناسبی قرار دارد و انتظار رشد طلا می رود.
دقت کنید که امشب نشست سرنوشت ساز FOMC را هم داریم که سناریوهای موجود
در این یادداشت
بررسی شده است.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19415" target="_blank">📅 11:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19414">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خب مثل اینکه «درنظر داشته» حمله کند  ایران، پس از حمله اوکراین به یک کشتی ایرانی در دریای خزر، یک حمله نمادین با موشک‌های بالستیک به یک بندر اوکراینی در دریای سیاه را مد نظر قرار داد.  اما گفتگوی تلفنی بین وزرای امور خارجه ایران که در آن این حمله به عنوان…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19414" target="_blank">📅 10:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19413">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خب مثل اینکه «درنظر داشته» حمله کند  ایران، پس از حمله اوکراین به یک کشتی ایرانی در دریای خزر، یک حمله نمادین با موشک‌های بالستیک به یک بندر اوکراینی در دریای سیاه را مد نظر قرار داد.  اما گفتگوی تلفنی بین وزرای امور خارجه ایران که در آن این حمله به عنوان…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/19413" target="_blank">📅 10:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19412">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyknFg-ILUmZdjPYpQgzxaEI0kcNJPjFYrxUBbotxF_dKdaVHAeLROR3XePmH0N1DYI3x8n_ExnrTdVfx_IbbVWoTwmCyF_sofIdq8m7_6mH0UfFjcj70QZdO5_4JJ2GqY8vT-lQrdGy3T17dlwlXTeZ67qv3__m9hMW7UajYW8LfA_ktH1I3XWcVFgJvgqQCbihuUlO18TzQByT6Q6s_c0Bk3Oe26-v_qZQtrST7mzPzEE1fnc2AhFFu-p_s-sg6pxrLEnr1QKIgcs5QDV9udnObZVvhx9VzWGCvODCUwWf10pZ1QLxskiBf_PHjfQssXTy0jWzN_J1KlynVv3nsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: ایران، یک حمله تلافی‌جویانه به یک بندر اوکراینی انجام داد.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19412" target="_blank">📅 10:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19411">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBKHnfOnUkD1Qy3Z8QmGEiL6SVdyeBSuOzCuPxTPiephx3y66qoVGecr0T21P_SoRSkIxaDqYeW9t2nz-MdQGVdZ0cA171QK7BArMBuF--FO3hP2ka5_3t6jr4ogiNnxRYNGUyQ2pleobEJYtf7CZkY9hwEtda1qBEwS0h-K5UnfX7kEFGpwV1uHuDNOHa8OJEdal33hSaPYaEJ23WyOzUmvrfRFQimj7ja5FhCp1a5NwH3rnk-fLMsShLZYAeOSD1nJHGa8vCnPprIbinV9yA8c1IEoAtJvCDhQRcongVvi-HYw-E7CtgeMdrHbsaAS6Mv3-XV3WYuUtDX9RyM6bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌ها، ایران قرار است در یک قرارداد به ارزش 60 تا 70 میلیون دلار، 300 تا 400 دستگاه موشک دوش‌پرتاب چینی (مدل‌های QW-12 و FN-16) دریافت کند. اولین محموله‌ها طی چند هفته آینده از طریق شهر اورومچی و از طریق پاکستان به ایران ارسال خواهند شد.
این قرارداد از طریق یک واسطه مستقر در هنگ‌کنگ به نام "Zhongqing Baoshang" انجام می‌شود.
چین و پاکستان این گزارش را رد کرده‌اند.
منبع: رویترز</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/19411" target="_blank">📅 10:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19410">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTeN-bz1W-OPJvBZZco_F-XEW_jQRQ44ouRjpewLqon5tAlYm4AXkwYf_5Lhf24l_9mA5Djp9DcL9TQ0aLhuyZ94DZskJzDsm8nNPCwNlSS1ZiddTO1KIlwNHYo3NDp254L3xXlAW-JRaCmWjlvzL8fxeljCLQHvsdKFx-BGdbZT-y_-_HW0x0f5QcuNRlEgkhgrqWidl5pP82zNlh8Rs-zqFWcFsbdiU0tLyGpzZE6SGV3lryNUqaIryXRMQPvo1_olXSuWIhSH7vSUn-7f1Uv9O2u-Iz29KGMY6VY7djRcud52SRjOeOu3VeKXQmugx6IVJiyC4g4bMjA8lUDlIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: ایران، یک حمله تلافی‌جویانه به یک بندر اوکراینی انجام داد.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19410" target="_blank">📅 10:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19409">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیویورک تایمز: ایران، یک حمله تلافی‌جویانه به یک بندر اوکراینی انجام داد.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19409" target="_blank">📅 10:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19408">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حملات عربستان به عراق !  گویا نیروهای حشدالشعبی هدف قرار گرفته اند.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/19408" target="_blank">📅 09:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19407">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7Ov9tdtcFQmIG2s6LSu6WnEd59REbkp32rWn7iMn4L1ezZztqvv_5e8KUxzYE7LuEjRljAWx2O68v0sq6zXcQ2MuwoXvOMkIdqYp3euVwloHm6Zcy3DXQ0AYgO_yS06UvC36igUpAp83FL4_EB8mn18nol2C-G9WmmEf4krekEGO0eQWz_kcvaen4JjN-np3jrOPTRqx3AtwBvFholuveJqzNOsD3bPJI3sRFYmmTC8nsn_f3s8TSvbL94eQsfd9RWpUP8Ap7qrNEoQUXuZX1bsgXOqF6Cn-6sdAhzXw7HoPYEYn3tQMatOQA8HVDdYQ3Xj3V0ZHqbrxyrS0YHHTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
فدرال رزرو در دوراهی حساس؛ تثبیت نرخ بهره یا افزایشی که پیام انقباضی ندارد؟
محتمل‌ترین سناریو برای نشست فدرال رزرو، تثبیت نرخ بهره است؛ هرچند افزایش ۲۵ واحد پایه‌ای با لحنی داویش نیز همچنان یکی از گزینه‌های جدی بازار محسوب می‌شود.
واکنش بازارها به تصمیم فدرال رزرو بیش از خود نرخ بهره، به پیام کوین وارش بستگی دارد و مسیر دلار، طلا، اوراق و سهام را تعیین خواهد کرد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19407" target="_blank">📅 09:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19406">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حملات عربستان به عراق !
گویا نیروهای حشدالشعبی هدف قرار گرفته اند.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19406" target="_blank">📅 03:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19405">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvqI2gjq3CjC9lW5f1KL7G2BK0i52QRrFliTeiya1V17ErrezkhzVCE3CUqF3XWNF1gE-3ldf2kBC8QqwE761i55YAUMILbogOQRVD6Rtpa0hhHKUbvtwvVnLQNdZ3NnNZcfUcQC7Y4EEbzprg-zVz4oPCaE4vyqxS7D2jyKB4a08UwrM3TOlyh07X85Mi7hdpQzkbklp9eki-AVp6UI9r3WzyfgPW65pQgC4SY6Nrhq-t_sOK0f99ovo8uuFwrE4Gy3TfYyGLMZezyZTmZ2dtXknJA9A4Cl_6AlRt3om0WxnrXRki7WChhEv8xC4av3lsDWVttD_bM4vvMF93EzzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/19405" target="_blank">📅 02:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19404">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTbOY4z8oLpDi52ahtAo8SNhotYUNZwLmG0imDJRuN83-vLsLSSIA-jI-CxOq8fp68itazX0rz7FqK5Q0lZ74T7ea6bRG7eyra7hwRebI-vVnnf_v5_TXjGSpZODc28G8guw38qvFO9T0ngVMA-UpwtiNDko2C74kRO-mFx3srntXHlgyJb9xJU0rc73uRcFwNxFoEOd3fJkkY4491i1o-pvk3XWyJFPn3q64IDiRJH9tJ7JtG9eMQrmyTpahSojjfVta1uwKnDQK9NlLMm4CkNEq_57giW3xvsUcKOEovwNNj6fAHVcvWKVnDrlAMstZDkrmdBYsvQ6hRyari6vJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه جنگنده های ما پرواز نمی کنند و این یعنی احتمال حمله هوایی بالاست.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19404" target="_blank">📅 02:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19403">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mf16-MddrvmlWsgLsJ9NeK42iJhzgfmifIbYbUCCKCdkuwojkJCITHnn3wVuLKEM9iRv-Yt_q0biOsWdbwcTQP83a5EOu8p7eQNoB4ywphYnJiqsSRhr53OE-J_pKd6RpKkgyIbS3UBpZzlf-ZrHIYqr_CYBCuZjg3IFl_lxKbiGuTel33uApvnCAM8iKSU50rbg2qGSam62RZRxLc1Z-LckFghG-fZpUqaP4Mz81Lm0b_RAyaaoz8PKwf5ly81RjAt6LQwGbpyvsFKUSE-h2pGCvKScIpl4_CA0OwZajuP3DzdVUWlK4gUS3WEJ_ZPr36OU0bnTbm0atWMOBHQKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلاً قیمت نفت بیش از 5% پرواز کرده</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19403" target="_blank">📅 02:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19402">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دیدید؟ همه گویا رهگیری شدند!</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19402" target="_blank">📅 01:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19401">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtKRKQBCFPaxhJBDRpxQRvlQbMRVp9_3QnbGREMDDQ8Rs0Tt2Ary6evuh_0M5PookFLrqtZ0JrDxkTsewGV5AiZ9H-3NZnC6PyWygZMoyIUaKxJQP6Qk0Be-SPea7OMrleBvSKvNt9qC5Ig_QT4Lr6cK3t-ugslbTABRrR2dkXeL6nYKP712Hth1oCZmdDt84qHYrFGUce9Cj9OToTfffdMZB_1Lnwt2U77lYIRW10pX9KQRb7Nf_mTnl_8tvRsHIcul9NUlc4jdJUny6uVXYlp037M0IHLqjRLpk4S5O0RBf3SUoncRFuIerxbu_EquQeX8IDxjgi1PEPZUBjkENg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدید؟ همه گویا رهگیری شدند!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19401" target="_blank">📅 01:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19400">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اگر هدف پایگاه الازرق باشد هیچ اتفاقی نمی افتد.  مگر اینکه یک پایگاه الاحمر نامی را بزنند تا در هم کوبیده شود.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19400" target="_blank">📅 01:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19399">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">صبح ها اعدام داریم، ظهرها قطع برق، شب ها جنگ!
بعد برخی آمده اند تولدم را به من تبریک گفته اند!
وا بدهید لطفاً.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19399" target="_blank">📅 01:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19398">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rq4jxalZkXc9y3CBNdASVYzWivl1nbEJiXiO4Yj-FK4TzcAUEYz3gB4ofrre74cYR__NNlHsreqFq8S20iORvjYiCJoqUvZIXgHC1qbPA4_eHMAtewcHc1-ttHnQgvWXhQVc87Qw06ae2h8zUQBOuM0GdlWV3Cio_rS7VwnIcsfxKlbZwbtPAxJQsVOhTN2di2tJb6FwfknlFNRZ-HB97NyQlPLtqXTgS7iTVswIF9FMLbpjXMJQt14IlDYNLV2SKtbPBBuDniGQoM7HmSSfP-1vklsrQHKF6uoJxT9y2ugxOgXfoRMv2-0PoLw7iUf_9p1mS8kWPv5MN8PJfQw1hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جا دارد دوباره گوش جان بسپاریم به آوای روح بخش بانو لورا برانیگن که زینت بخش این شبهای پرکت خواهرمیانه است.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19398" target="_blank">📅 01:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19397">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">جا دارد دوباره گوش جان بسپاریم به آوای روح بخش بانو لورا برانیگن که زینت بخش این شبهای پرکت خواهرمیانه است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19397" target="_blank">📅 01:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19396">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مقصد گویا اردن است.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19396" target="_blank">📅 01:35 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
