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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 23:41:06</div>
<hr>

<div class="tg-post" id="msg-19493">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SBoxxx/19493" target="_blank">📅 21:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19492">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">— منابع یمنی معتقدند که عربستان سعودی در حال آماده‌سازی برای یک تهاجم نظامی بزرگ علیه حوثی‌ها از طریق دریا و احتمالاً از طریق خشکی در یمن مرکزی است تا گلوگاه صادرات نفت خود را در دریای سرخ جنوبی آزاد  کند.
— گاردین |</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/19492" target="_blank">📅 21:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19491">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزارت دفاع آمریکا، قرارداد ۵۸ میلیارد دلاری برای سیستم پدافند هوایی پاتریوت به شرکت لاکهید مارتین اعطا کرد.
این قرارداد به ارزش تا ۵۸.۶ میلیارد دلار، مربوط به موشک‌های رهگیر پاتریوت است و تولید این سیستم را تا سال ۲۰۳۲ افزایش می‌دهد. این اقدام در حالی صورت می‌گیرد که درگیری‌های مداوم در ایران و اوکراین، ذخایر سامانه‌های پدافند هوایی آمریکا را کاهش داده است.</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/19491" target="_blank">📅 20:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19490">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">329.6 KB</div>
</div>
<a href="https://t.me/SBoxxx/19490" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 15</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/19490" target="_blank">📅 20:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19489">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SBoxxx/19489" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19488">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">در صنعا توفان و رعد و برق شده، فکر کرده اند عربستان حمله کرده !</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/19488" target="_blank">📅 19:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19487">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رهبر حوثی‌های یمن، عبدالملک الحوثی، درباره عربستان سعودی:
آن‌ها دام‌ها را نابود کردند؛ شترها و گوسفندان. حتی حیوانات بارکش و الاغ‌ها نیز از رژیم سعودی در امان نبودند.</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/19487" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19486">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SBoxxx/19486" target="_blank">📅 18:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19485">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICtpbGXJfmrC1ii6U-EKa8oYff2h4Tb9ri-MwHz-z_uuvm4tGTEfsg9WmGNjsyVcc5uy6mhVppSmGJq1bD20VYmLrEaxgcDFPVXDfEMhGpfZ-0W5PEEYuzi-7-Hb38LcJwp8QvMHaSCzBokZAdOTBRNQ8inyAPNc62zxw76mrwPKdvJfkq65BIKhmEUNCK9mWTb1JJmnR11vz-aq_7kN_jCxucnem35_Ru2w0bSOkZpyrT2_D4WeR_LMGv2LLSv2oQXsnHCKiNceIzlPT2CgGososZFO_6jyYjmGEReHTqeDrhcRxEN3whpRvxUDPU8xBx-tO_x0laEwMcYuCWeUhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما ببینید در روزهای اخیر اینها به لیست اهداف مشروع ما افزوده شده اند:  — بلغارستان — بریتانیا  — اوکراین</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/19485" target="_blank">📅 18:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19484">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i05BOmMExO-ghRp-eg6iKraNsMMVgfgIoF92PVvZyrabLWRO_1SDSK7PRwvIHgsNXBEo4DJXP2cfjKE1Gv2Gtt3C9YqkC_ddJvwPCrkfHvqKCNF0kN3JAoyRLqiGUSpOQUbB4rXUbKrvuxqd2lwN_NoZOpKyR9PAkaLDhDcfoOIma5pdjgvN1IsUtZGiptYMKSUsyFViBm4KCu4A_aZjup3QHblXQj6HKEd0ZrecQbbXhWWuzhZ7xd2pNtEtptLtytVBxGQASFhkaiSqg6qNyUtdwU36lVZD__FoHfdhA5XCfqkdhCz5Cp-jNV9qrk3ZmNo7NJi1HTP8Y-L452r1WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/19484" target="_blank">📅 18:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19483">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">روسیه ممنوعیت صادرات بنزین را تا سال ۲۰۲۷ تمدید کرد!</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/19483" target="_blank">📅 18:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19482">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">— مشاوران و اعضای کابینه ترامپ گزینه‌هایی برای انجام عملیات نظامی گسترده‌تر علیه ایران را به وی ارائه دادند.
— فاکس نیوز</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/19482" target="_blank">📅 18:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19481">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سپاه پاسداران: ایران پایگاه هوایی الازرق را در پاسخ به حمله آمریکا به قشم، با نابودی سه فروند اف-۳۵ حمله کرد
سپاه پاسداران انقلاب اسلامی حمله موشکی انتقام‌جویانه به پایگاه هوایی العزرق در اردن را پس از حمله آمریکا به خانه‌های مسکونی در جزیره قشم اعلام کرد.
طبق بیانیه سپاه، این حمله به منطقه استقرار و محل نگهداری اف-۳۵ هدف قرار گرفت و سه فروند از هواپیماهای اف-۳۵ را نابود کرد و سه فروند دیگر را به شدت آسیب رساند. چندین افسر آمریکایی و پرسنل فنی نیز کشته شدند.
سپاه گفت که این عملیات در پاسخ به حمله آمریکا به قشم انجام شد که منجر به زخمی شدن اعضای یک خانواده محلی، از جمله کودکان، شد.
در این بیانیه همچنین از اردنی‌هایی که با حضور نظامی آمریکا در کشورشان مخالف هستند، تشکر شد و گفته شد که موضع آن‌ها فشار بر نیروهای آمریکایی را افزایش داده است.
سپاه در پایان با تأکید بر ادامه عملیات علیه حضور نظامی آمریکا در منطقه، بیانیه خود را به پایان رساند.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19481" target="_blank">📅 14:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19480">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کشته شدن ۳ عضو سپاه پاسداران در حمله آمریکا به زنجان</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19480" target="_blank">📅 14:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19479">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19479" target="_blank">📅 13:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19478">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwGbeCxKraa7e6UQHIKbMxCVdjY4zzq78jptdzcBlwsAvb3GlmpQVT4CDTJYBO6vu_F6ut_5DLjiOWTq3cTK6qAA-bidDzB7I7FJVg_Q4BfACPRWnfyrAEo8pKT70avytZIaByVvWd6CPd85aQqS5yuqiFLA4hAJUdwS_kCk4tSxQtqqCIFycwMXjICBoSw-GjhHh4kDBAB2JvkxswDTJpLK0NMR-uy4SkM-eYcnMjXELtGPO1KtIrhhDiniP9SXTmUidiP-Jj1ItfMUmKhHcbe4QBloaB1XUSJDHZv1cFlJEyz4RfNY-51uZZ2Y8OY6P-JesNe71dSnO5F5EkGbaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لینک نشست دیروز با نیما</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19478" target="_blank">📅 12:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19477">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8eacd406a.mp4?token=Nbtts1XfrD729VJ5ywGwa-b4j_5GKPfDyr1ZzXzlna7y6M16T_54G1pwbmmGkQuYRfsaSG759yk_SmfpFlOF2eBaG9pnrKzKVpXUWLQ3-GgsOYpoWqaUnKzeLNueg6ZsZOVHljZN5K-ZexZWIWdb2stQhmV6Mmc0jOxQk8clVmQYR7lyVB4USODYoxfSHkrHxiwFp-ZTAQhFAThkAwFgnzdy5uif8LC9TD74mdPl4y_GhFmC_1beIXW15bYJg_Ff-0zz4zJZdFgjFlwkzw38ZSStrjVBz8GJEkMy0WjgVNJ8EiJIHZ5O0nwaXTrmed-Ne6i4geCSfFFl93-Ea0rtRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8eacd406a.mp4?token=Nbtts1XfrD729VJ5ywGwa-b4j_5GKPfDyr1ZzXzlna7y6M16T_54G1pwbmmGkQuYRfsaSG759yk_SmfpFlOF2eBaG9pnrKzKVpXUWLQ3-GgsOYpoWqaUnKzeLNueg6ZsZOVHljZN5K-ZexZWIWdb2stQhmV6Mmc0jOxQk8clVmQYR7lyVB4USODYoxfSHkrHxiwFp-ZTAQhFAThkAwFgnzdy5uif8LC9TD74mdPl4y_GhFmC_1beIXW15bYJg_Ff-0zz4zJZdFgjFlwkzw38ZSStrjVBz8GJEkMy0WjgVNJ8EiJIHZ5O0nwaXTrmed-Ne6i4geCSfFFl93-Ea0rtRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبور موشک های زمین به زمین اتکمز آمریکایی بر فراز شهروندان کویتی به سمت شهرهای خوزستان</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19477" target="_blank">📅 11:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19476">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0Z0PbuiMZnDtwcurh6V-gJZ_jwItul-H4CWMmTmuMnIGSum8UGJd9bBVVlq-putJC7km0XsuI3c4ttQCBe8iYSiQuYXOdnkVM7_TJLcDayQ36UC39zumkYYMUBi2ALxdsl6EcaIAa4PJJjqs_YRp2HbD0bBT2FBPvjr7jIhQT96I1IqcS7iVwKGHNRKYJsoc20zWGanLJwiO6l0uowrFrU9QGZ0cE34kr6c1XLzqnvdZKoCf8nevvoV6hOFiRVSNYiTfqCBWhv_WycDRrGKP2AOBlL_CahYhIDrG1YFUgOUPHcLDIkjkJVYsk9l8yx-6xrADSDsbdvYSIa9l2hgNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این همان حرامزاده ای است که دختران را در لایوهای خودش کتک می زد و به آنها اهانت می کرد که خوشبختانه به این روز افتاده و تا مدتها نخواهدتوانست شرارت کند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19476" target="_blank">📅 11:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19475">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19475" target="_blank">📅 11:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19474">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-xVlZ6l2gic-d18GpJzLZeMUUWNZMhW53sft70QSRi65iFDH-VM8gc-H9a6ZkBsGDI8p51yUuKjoiTx0hJNNrHyiumNXbb7cSkAP92rFNShBlfNZuVxfef-c0IEVQya5TrA_WLe3ffLjkwhgqQwawtiQrN0PMTww18e2mnico_7KeODsusBPDeIe2DHWj1ZtUXBfI55rL7d64aiVcUbDQmmFJV6w9pn4mRAsjzjLo2Cr_rVXkwKoPUd-Ms-fk-b8QWfW_g46KBwGyvtFzAmAefVsHK52giVvch1JY5raCBZOgD-Uh3xUGsH9gOJPVyMO76y4D4xNBsfLNZq-lvj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهداف حمله پریشب حمله مشترک سعودی و آمریکا به پایگاه های حشدالشعبی در عراق</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/19474" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19473">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سپاه پاسداران:
با استعانت از خدای متعال، متجاوز همین امروز تنبیه خواهد شد.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19473" target="_blank">📅 11:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19472">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlfMYU26OzEbA52DTw3pz7wOXh6Z2Ao48livi20psETVy7SbgelcGL6QRNJOpiaHn0CDPOIKSJCDPLYG9MoHCkPme7fTtL_1jyY2hQ3nXItNZzB3cFSPcrzCEqzNpv20MAmZebzyn-3N82p4QHlBd2kNXOhsvOq7wvsdeF7nQaxbwYBL8ijrLDLt_LKW623aTX758yag3AsbP-BNKxoLSVQHGmQVhXptX71Z3CvsiEhidQ2CIb004QqpMZ0ffmeOWVVpRM6xuMfQ35bfm0U7Jc9eiaeL89tAXI0OQn8vS8T29sj01lQoWbhQeQeLLU4-dkZlFh8JALGgC7cTnFtMHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح میانه پایین است و حالت رنج برای طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19472" target="_blank">📅 11:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19471">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19471" target="_blank">📅 10:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19470">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پرسش: اوایل این ماه، رئیس‌جمهور ترامپ در مصاحبه‌ای با یک خبرنگار گفت که در رابطه با شما، همه می‌دانند که چه کسی رئیس است، یعنی خودش. او کسی است که تصمیم‌گیری‌ها را انجام می‌دهد. آیا شما هم این‌طور فکر می‌کنید؟
نتانیاهو: خب، شما می‌دانید که در آمریکا اغلب می‌گویند ترامپ هر کاری را که من می‌گویم انجام می‌دهد. و در اسرائیل، اغلب می‌گویند من هر کاری را که او می‌گوید انجام می‌دهم.
و گاهی اوقات، این مسائل توسط هر کسی، از جمله رئیس‌جمهور، در بحث‌های عمومی مطرح می‌شوند. اما حقیقت این است که ما شرکا هستیم. ما متحد هستیم.
او شریک ارشد است. این کشور ایالات متحده آمریکا است. بیایید این را فراموش نکنیم. و من شریک فرعی هستم، اما من نخست‌وزیر اسرائیل هستم.
و وقتی لازم باشد، من برای دفاع از منافع کشورم و امنیت کشورم، این کار را انجام می‌دهم.
منبع: خبرگزاری ABC News</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19470" target="_blank">📅 10:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19469">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نتانیاهو:
ترامپ اساساً سه گزینه پیش رو دارد: اول، دستیابی به یک توافق؛ دوم، ادامه محاصره؛ سوم، اقدام نظامی.
هر چیزی که منجر به پایان برنامه هسته‌ای ایران شود، چیزی است که ما می‌خواهیم. این هدف مشترک ماست.
س: وقتی با ترامپ در کاخ سفید ملاقات کردید، آیا تلاش کردید او را متقاعد کنید تا حملات به ایران را از سر بگیرد؟
نتانیاهو: در واقع نه. این یک تصویر کاریکاتوری یا تصویری اغراق‌آمیز است. این درست نیست.
ما در واقع تمام سه احتمال را بررسی کردیم، و من فکر می‌کنم که این کار را به صورت شفاف و در بین دوستان و متحدان انجام دادیم.
و این تصمیم اوست. این تصمیم اوست.
منبع: خبرگزاری ABC News</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/19469" target="_blank">📅 10:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19468">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شب گذشته یک منزل مسکونی در قشم مورد اصابت پرتابه آمریکایی ها قرار گرفت  احمد نفیسی معاون استانداری هرمزگان از حمله دشمن به یک منزل مسکونی در محله چاه‌تنگو شهر قشم خبر داد و گفت: تیم‌های امدادی در حال جست‌وجو برای یافتن دو یا سه فرد محبوس‌ در زیر آوار هستند.…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19468" target="_blank">📅 09:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19467">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فیلم سنتکام از هدف قرار دادن اهداف در حمله بامداد
چند پرتابگر متحرک نیز دیده می شوند</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/19467" target="_blank">📅 09:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19466">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حمله موشکی ایران به اردن</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/19466" target="_blank">📅 09:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19465">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شب گذشته یک منزل مسکونی در قشم مورد اصابت پرتابه آمریکایی ها قرار گرفت
احمد نفیسی معاون استانداری هرمزگان از حمله دشمن به یک منزل مسکونی در محله چاه‌تنگو شهر قشم خبر داد و گفت: تیم‌های امدادی در حال جست‌وجو برای یافتن دو یا سه فرد محبوس‌ در زیر آوار هستند.
احمد نفیسی خاطرنشان کرد: جزئیات تکمیلی این حادثه و وضعیت افراد گرفتار، پس از پایان عملیات امدادی و ارزیابی‌های میدانی اطلاع‌رسانی خواهد شد./ایرنا</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19465" target="_blank">📅 09:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19464">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19464" target="_blank">📅 09:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19463">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19463" target="_blank">📅 09:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19462">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حمله به آبادان</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19462" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19461">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLQD5VaTtgyRaiu3c5e-j0nCDfQDNWH3l4DLpAmtg_-QUNWBHwmbtXajk5WkpCrG39wgZhr4W67cCfbMvk_1-m4ExSdxKMTPGmox2rqirKhdM0NCZ0o452unO1cvBhy7RExEQvcawCbXmeesdTSbZQ6246kl6iHtIjO-yOywRAFjkcdOIfHHI8lDvkJRMSsK3CU14tr9tOYonnJxF1DWfTFHTgw2L2KBluCP1q7YKnoQW8aUy-O-tFJM40tUULPF1Ln6Oi-2xxXwfxLBodRY-Mc9C0tqdPaNbX2tj2v6qi2rGCPWFm2_zXaq7_1ZL54RE9_ReFZvM6Zh_PCPQMs3pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات آمریکا تایید شد</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19461" target="_blank">📅 02:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19460">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">چندین انفجار در ریاض، عربستان سعودی، و بسته‌شدن باند فرودگاه پادشاه خالد در ریاض.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19460" target="_blank">📅 01:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19459">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انفجار در اردبیل و ارومیه (تایید نشده)</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19459" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19458">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sr29ev6Hto0P7A9U8YY8_QcEoJydiK2Yi1IMrsadrXlRjxTZ2pUFbgQavuqg5qJBNgdnQbWtLilHNDEenxHck3Q3VFIkxnJrRvgTvmoT_Q8Wvl7s4Awj2AbHu4bnC43IpyTc32m5QvvbDhRRh9rLa3zhtvIGC9ntFGiYIeiISNJRm7hLAjJbmOyWFTqCHeghyxFXIAhvpz3cbOedTAB1ahlsWnYBLBXMIDAQThf6h9UR_KMpwkihES1FNzW-h5Z3GqDaqvC6k6djecP31jarmWd4NTLOgsRiH-6uzQm7IpFT0O2jDB4AUEaFw2LXKKFB0N3ht_zyAYCu2Uu5QYjjvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا که اخیراً محبوب حضرات شده بود و چهره یامال را روی موشک ها میزدند، اعدام های اخیر در ایران را محکوم کرده و خواستار تعویق اعدام های برنامه ریزی شده شد.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/19458" target="_blank">📅 00:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19457">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOuK9W0sj_pgmK9WTtehTpsxGZsKWuYxW-N3dDHXu3lPpEey4J7T1O_ZB_0qg9_dnNjHuHVsLvlcJOkGRVVnXXToakx9rToyf-Mbu_a7cIDD8dv7NFM4nKU1RuffAK7UpZa-4mriHxOBPlVEo9RtCo7o3VJ6c84VgX_5Qwdo0gmujHhRNf3Y8sZLUxXZnNvJKvuAqam7h18g13CqXqWAOa3J-Czb8F59LLiLokY3v_T8Qrm4f_Q4ltL6ZxBaGhh8MY_XdigXR1SkRvjiGz4ggnW93NtaMpChBF6Fiw1it4nRs4w4GWEbJdCrpE6fWKOp3l12kWlwzWsIH5M34nvSQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا که اخیراً محبوب حضرات شده بود و چهره یامال را روی موشک ها میزدند، اعدام های اخیر در ایران را محکوم کرده و خواستار تعویق اعدام های برنامه ریزی شده شد.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/19457" target="_blank">📅 00:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19456">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMj_p9KeamzBcSvQPX41nGO7Yvn7nPulqN4vSYvO2amiMSd7dtu6afDaFL9Ufl2RJFIArSb2mH9JPeMLdRIqLuXTKr59Wwga-iaCOPeqa0t00WEeDdzj7QmHLjFdn1jVW8bGWuB07-0x2IwrLt4PRcvYm7ct47wT20X6bfsBqJlNQgT4MaiJL6pC_HAWVNGwx6Ujkfaiwqpa9j7pyOau9FvjBDiR3mzMn5EiYZJbqLlBC1PSu0JAZzii27xEIK3h33O4z5PDUuGiqBNmK7tcJClH1KKxNyi5HAw8ieUqm4vi_G5pFms8zFarF6NV3jr_pQRctTAt3kZmhw082v018Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیدوارم آن یک هواپیمایی که نزدیک تهران است جنگنده نیروی هوایی ما باشد.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19456" target="_blank">📅 00:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19455">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر
به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19455" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19454">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1qvdwVIJCtTXqL3TWWcB3k7rwT5w_IjX8DRd2W1JSQcPLv2PoQQe1GqtSCKr8rZot7m0SgNcjC40ZL5jyrF27NIsxz29z9SklkFkTgFlOkOudRjMuWtYSKit6HJy2dAP5vY0_520dsOvLiix71jK0cyckQSP_kgTgIsYA1XaMTFSpXUJixZ3sVS3xGn17vC4cB1-IkcTcmvhwvBK-Xx6hL_OoTltLPPLIjmpRnd4KZV35duHZYUglNcifeBQrbu6D0xNlPF2QApRFbajQIkpxQJspOjOuQgmAIbgG9F8DOFiKdNLdNJM7L3AYMXZrozbqG-za9d7RfqFTZOsrLeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز هم در وضعیت مناسبی قرار دارد و انتظار رشد طلا می رود.  دقت کنید که امشب نشست سرنوشت ساز FOMC را هم داریم که سناریوهای موجود در این یادداشت بررسی شده است.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19454" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19453">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3185a6e49f.mp4?token=nDnlBRAJ_bL-o6gTac4dAB10mcrWaNldHXA_sJRmUHtbolIJdvyt5eEi2CxNMxFRGnxMU62nv1__YbwY3r2WQqbsBuZ3_zdnorSKrWHE5GVf0fzjY1bCtXLPSoGdvStPG98vfKzR0cF3OqDLngjXXfVzJkbFAuCwg1medwYfFsIOhP2rmBImY3Qi9JbFW7GhF0dKklprv-u2GeJf3vkk5iABlMhv6yXGGiZ1oUrlQXpJWDe3EoVQkJERb3lcA4Dhl2NeXX9qnF46CMCj_pLh2xldDhlN8rx6QIXFfe9WUlJVFR1nANrQS2m31DrvzlCnZtz0VEENnLu_SbV8UEiPJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3185a6e49f.mp4?token=nDnlBRAJ_bL-o6gTac4dAB10mcrWaNldHXA_sJRmUHtbolIJdvyt5eEi2CxNMxFRGnxMU62nv1__YbwY3r2WQqbsBuZ3_zdnorSKrWHE5GVf0fzjY1bCtXLPSoGdvStPG98vfKzR0cF3OqDLngjXXfVzJkbFAuCwg1medwYfFsIOhP2rmBImY3Qi9JbFW7GhF0dKklprv-u2GeJf3vkk5iABlMhv6yXGGiZ1oUrlQXpJWDe3EoVQkJERb3lcA4Dhl2NeXX9qnF46CMCj_pLh2xldDhlN8rx6QIXFfe9WUlJVFR1nANrQS2m31DrvzlCnZtz0VEENnLu_SbV8UEiPJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک غیرنظامی اردنی به طور تصادفی، فیوز انفجاری یک پهپاد انتحاری ایرانی مدل "شاهد" که سقوط کرده بود را هنگام بررسی آن، منفجر کرد.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19453" target="_blank">📅 00:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19452">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
ارتش اسرائیل آماده حمله سراسری و بزرگ به ایران است</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19452" target="_blank">📅 00:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19451">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گزارش‌هایی از پرتاب موشک بالستیک از اطراف یزد در مرکز ایران</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19451" target="_blank">📅 00:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19450">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ درباره ایران:  آن‌ها می‌دانند که این اتفاق (حمله) در راه است. از ما می‌خواهند که این کار را نکنیم.  دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19450" target="_blank">📅 23:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19449">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ:
آندی برنهام باید به مهاجرت اشاره کند زیرا این موضوع بریتانیا را نابود می‌کند.
آن‌ها از آفریقا، آمریکای جنوبی و بخش‌های مختلف آسیا می‌آیند و در حال حمله به اروپا هستند.
این یک حمله است و بریتانیا مظنون اصلی است.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19449" target="_blank">📅 23:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19448">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiqSKSnt07dGIb4c5H1Q0hYs_s31gsjEYk8H2iiU3acctPqIesxYEVGJZOZGWx9YcQX_hEo7x7tXvw1nrb-n7L-33ayuAxZ5hXafd4339kFnkPa10kNK9Xd3zKTrYJ2-UuENbea6jPKrQ19emLK-1AKXk-w4LcEA4MiyuMNoQnyrI9Ywp1hQaRYzqxyc_PIcWsQbkJxcbNZytpMefh6if56TZuJzf85DDFaZYGF7Yxt648fh48me229ji49LP8DGZbujqPjVynt1Usqt1PWYw-5HBKZ6OXqXzR2WGKsm4c90DSkq_vpRcA4WEokagYF8ajaNPBnPw0qeStGwnb5xmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19448" target="_blank">📅 22:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19447">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها می‌دانند که این اتفاق (حمله) در راه است. از ما می‌خواهند که این کار را نکنیم.
دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19447" target="_blank">📅 22:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19446">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ درباره ایران: آن‌ها را به شدت ضربه خواهیم زد، نوبت ماست.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19446" target="_blank">📅 22:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19445">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">علت رشد طلا در چند دقیقه اخیر:
مقامات امنیتی مصر به شبکه خبری "الحدث" اعلام کردند که هیچگونه حمله‌ای در بندر دمیاط رخ نداده است. آن‌ها مدعی هستند که این حادثه یک آتش‌سوزی بوده که در بخش موتور یک کشتی از رده خارج شده رخ داده است. - خبرگزاری "کان" اسرائیل.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19445" target="_blank">📅 20:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19444">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یک مقام ارشد از یکی از کشورهایی که در این میانجی‌گری نقش دارند: کسی که تصمیم‌گیری‌ها را انجام می‌دهد، فرمانده سپاه پاسداران انقلاب اسلامی است. - خبرگزاری کانال ۱۲ اسرائیل،</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19444" target="_blank">📅 20:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19443">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجارات در اردن!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19443" target="_blank">📅 20:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19442">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رئیس‌جمهور ترکیه، اردوغان:
دولت فعلی اسرائیل که تحت تاثیر جنگ قرار دارد، با تحریکات و اقدامات سازمان‌یافته خود، همچنان منطقه ما را به سمت بی‌ثباتی سوق می‌دهد.
اسرائیل با نادیده گرفتن حقوق اساسی بشر و زیر پا گذاشتن قوانین بین‌المللی، به تدریج و گام به گام، سرزمین‌های فلسطینی را اشغال می‌کند.
اشغالگری اسرائیل، سکونتگاه‌های غیرقانونی آن، و سیاست‌های آوارگی، ارعاب و سرکوب علیه فلسطینیان در کرانه باختری – همانطور که در غزه انجام داده است – منبع اصلی مشکلات در منطقه ما هستند.
هزینه این تجاوز نه تنها توسط برادران و خواهران فلسطینی ما، و نه تنها توسط مردم لبنان، بلکه توسط مردم با ادیان مختلف و کل منطقه پرداخت می‌شود.
به عنوان مثال، به دلیل درگیری‌ها در منطقه ما، عرضه جهانی نفت، یکی از بزرگترین شوک‌های تاریخ را تجربه می‌کند.
متاسفانه، این فقط نفت نیست. قیمت بسیاری از مواد اولیه کلیدی در بازارهای جهانی، از جمله گاز طبیعی، کودها، سوخت دیزل و محصولات پتروشیمی، نیز به سرعت افزایش یافته است.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19442" target="_blank">📅 20:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19441">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نتانیاهو:  من همین الان یک گفتگوی تلفنی با آقای پیتر هگست، وزیر دفاع، به پایان رساندم.  او نکته جالبی را با من در میان گذاشت. ایشان به من گفتند:   «ما به جهان نگاه می‌کنیم و کشورهایی وجود دارند که اراده مبارزه در کنار ایالات متحده را دارند، اما از توانایی…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19441" target="_blank">📅 20:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19440">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m01FsVYh5omhtXisMnNEG3YXm_p8LrFn2-LBkcqhugkFTTUakXe_YpItyD3niQbYV5Uv4ha-JlAbj_2fIWKjkQpKM7RYeAIAPz47Ejmvbfu3HOn8ucCQTJNfI6XR4boVqmsaYzjVMVsUHGNBP836POEXGhgsS4chI5N2XB5W_vtpv7evqFUQobQfgKimaS5j9glcIobCDabOJMgELpxHY_CSzKiQrHq_G3R1kt3SdGetKfHdCXQRjANvuw4nW_zNmj53_4qYfFIUp_-N4qGdg0rboqOSQ4S8tOcWJrvQ8Fw-30vg2rgCktRrreCSUJExXwypvAcCr08nkf2b5z-Spw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:
من همین الان یک گفتگوی تلفنی با آقای پیتر هگست، وزیر دفاع، به پایان رساندم.
او نکته جالبی را با من در میان گذاشت. ایشان به من گفتند:
«ما به جهان نگاه می‌کنیم و کشورهایی وجود دارند که اراده مبارزه در کنار ایالات متحده را دارند، اما از توانایی لازم برخوردار نیستند. و کشورهایی وجود دارند که توانایی لازم را دارند، اما اراده لازم را ندارند اما فقط در اسرائیل است که ما هم اراده و هم توانایی را مشاهده می‌کنیم.»</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19440" target="_blank">📅 20:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19439">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مقامات اسرائیلی می‌گویند نتانیاهو در جلسه روز سه‌شنبه با ترامپ در کاخ سفید، نقشه‌هایی را ارائه کرد که میزان نفوذ اسرائیل و ترکیه را در سوریه مقایسه می‌کرد.
بر اساس اطلاعات ارائه شده، اسرائیل حدود 0.1 درصد از خاک سوریه را تحت کنترل دارد، در حالی که ترکیه حدود 5 درصد را کنترل می‌کند.
نتانیاهو از این تصاویر برای مقابله با فشارهای قبلی آمریکا استفاده کرد، از جمله تماس تلفنی ترامپ در اواسط ماه جولای که از اسرائیل خواست نیروهای خود را از سوریه و لبنان خارج کند.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19439" target="_blank">📅 19:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19438">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19438" target="_blank">📅 19:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19437">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یک مجتمع شناور ذخیره‌سازی گاز طبیعی مایع (LNG) متعلق به یک شرکت آمریکایی و دارای پرچم جزایر مارشال، در شهر دمیاط، مصر، مورد حمله حداقل یک پهپاد قرار گرفت.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19437" target="_blank">📅 19:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19436">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یک مجتمع شناور ذخیره‌سازی گاز طبیعی مایع (LNG) متعلق به یک شرکت آمریکایی و دارای پرچم جزایر مارشال، در شهر دمیاط، مصر، مورد حمله حداقل یک پهپاد قرار گرفت.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19436" target="_blank">📅 19:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19435">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به خبرنگاران گفت:
«ایران در حال حاضر تقریباً ۱۵۰۰ موشک بالستیک در اختیار دارد.»</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19435" target="_blank">📅 19:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19434">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مقاومت اسلامی عراق با محکوم‌کردن حمله آمریکا به حشدالشعبی در کربلا، به دولت عراق تا ۲۳ صفر مهلت داد تا توانایی خود را در دفاع از کشور نشان دهد.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19434" target="_blank">📅 18:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19433">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مقاومت اسلامی عراق اعلام کرد که انتقام خود را از حملات اخیر ایالات متحده تا پس از مراسم اربعین به تأخیر می‌اندازد تا امنیت میلیون‌ها زائر مختل نشود.   این گروه هشدار داد که حملات علیه نیروهای ایالات متحده اجتناب‌ناپذیر است و گفت که در صورت لزوم عربستان سعودی…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19433" target="_blank">📅 18:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19432">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مقاومت اسلامی عراق اعلام کرد که انتقام خود را از حملات اخیر ایالات متحده تا پس از مراسم اربعین به تأخیر می‌اندازد تا امنیت میلیون‌ها زائر مختل نشود.
این گروه هشدار داد که حملات علیه نیروهای ایالات متحده اجتناب‌ناپذیر است و گفت که در صورت لزوم عربستان سعودی نیز می‌تواند هدف قرار گیرد.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19432" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19431">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رسانه‌های ایرانی گزارش دادند که 4 عضو سپاه پاسداران از کاشان در حملات مشترک آمریکا و عربستان سعودی که در طول شب به سایت‌های حشد الشعبی در عراق اصابت کرد، کشته شدند.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19431" target="_blank">📅 17:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19430">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نتنياهو امروز با پیت هگست، وزیر دفاع ایالات متحده، دیدار خواهد کرد.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19430" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19429">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حمله موشکی ایران به اردن</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19429" target="_blank">📅 17:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19428">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mE_5_0SWUaTaLnVIWVAWr3MglhSRAfD5s2cvKIBdDba5hIcyUwmjgMOO-4pZV-C3Q6KTwtMmvMsteSjrwIyu-8xXxEIWk73U3TQS2zEHoFdA0vqv01s_P3DWUMJxXaJs4Ww4zbNn8uuGv-gxIPwI05K0RTHzmwotpCRceXUFkrp8doCDLyO0dayQj_1u5WVgpOj63pWPFbu27FT37ey6f-wm-r7igzy3P1zE2uzAsmojB92VeG8boFb5eZoXn0wftHOiAnb_ncBHcdpD4TGeEf4BA4SQAAkn0Yw8dcNC87dm5ReaXDLEoScyIA3SET9k7dCTRddhNfF53cwKei1b_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای وزارت خارجه در هدف قرار گرفتن مواکب زائران حسینی در حملات دیشب سعودی و آمریکا!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19428" target="_blank">📅 16:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19427">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19427" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19426">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19426" target="_blank">📅 16:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19425">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انتظار می‌رود که اسرائیل امروز به حزب‌الله پاسخ دهد، اما این پاسخ احتمالاً مناطق جنوبی بیروت را هدف قرار نخواهد داد.
— کانال 14 اسرائیل</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19425" target="_blank">📅 16:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19424">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده:  «حمله دیروز ایران یک غافلگیری بود و نیروهای ما تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.»</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19424" target="_blank">📅 16:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19423">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده:
«حمله دیروز ایران یک غافلگیری بود و نیروهای ما تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.»</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19423" target="_blank">📅 16:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19422">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وزیر دفاع اسرائیل:  در دور آخر درگیری‌ ها جنگنده‌ها و سوخت‌رسان‌های آمریکایی از اسرائیل پرواز می کردند اما ایران همه را زد جز ما</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19422" target="_blank">📅 14:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19421">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پرتابه دشمن به استان آذربایجان غربی برخورد کرد - فارس</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19421" target="_blank">📅 14:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19420">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مطمئنم امین سهامداره  @Piknikanalyst</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19420" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19419">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CTHs4NTbavM-_VDllnx3uxMneLq-U6pM0xgYh0VJEfQwK1qIqCo5qsEMEu8vhhlJ2gN0QS5ps-tYPI7fTXpJaS6TE-YvdR57lXoV-wizzBk_XuCivRJ8zuIwXuZD4xNt0bkcUFSdVIRhGoyWNMo4Vlabbk1nqjzATcPYpkUSPcVbHyJHGppk2jDl5XKM9y2wtODVlKyJqFuOOZBqpq1Hst1r2AvUXnPcDwls_UJMBCP420D49jFew3MvH-SDXGB6BOHpqHz8u3QTMB00kjIjzlq_fXka0I_2SZVakNEI_iWDjHY0IJS6fxz-2sI__Tip9kERrzkv4q5H6StkGppM9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطمئنم امین سهامداره
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19419" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19418">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نیروی هوایی ایران اعلام کرد که جسد سرتیپ مجید کاظمی، خلبان جنگنده بمب‌افکن سوخو-24MK که در تاریخ 2 مارس توسط جنگنده‌های F-15QA نیروی هوایی قطر سرنگون شد، پیدا شده است و طی چند ساعت به کشور بازگردانده خواهد شد.  نیروی هوایی ایران همچنین افزود که مقامات همچنان…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19418" target="_blank">📅 11:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19417">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ynl-V8ZXYBd9JToRI8ItBeEUVJ3p_Q7nWfMBEo3NzmtOSzgsH_uzQh3XyAiDUtip-pExoV7ayb-WqfjcfLtU0IyN27LEQrlBg1XIJzTuXdFoTWiQk5IOXZPNWofps43nMgjYv0dEKWFlh6lAGAOb4p89CYu9HACSw6HyaouwQoJfRF96aU-JLb3ic2y6khb3UrovbeQE_nq7tTF4FiMHqwiOUF7_-ANZPEIQzU0729hnLMJ8o7_a_1wG_kfeYVYQo-daG6JMaLToCT64Svje7Ox2atggUfgfo-mhz1e_Vx_FKRJudXjKyAOlBgqkPhD9FLf73IQ9m8DpSuxEyB_hEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران تأیید کرد که تعدادی از ناوگان بمب افکن‌های سوخو-۲۴MK اش سرنگون شده‌اند.  این هواپیماها در حملاتی در عراق و سپس قطر شرکت کرده بودند اما سرنگون شدند.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19417" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19416">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a40b3b45d.mp4?token=TEww9XiB_c6r9Jwrq9uvQhBzz3S_LkloflbCLDJJORFWo-mg_rrWB0ZzqhtTlH53vtHgBYGQaFWe-CoUx81l8io0l2cYCexCc3QMxHtlCoa4oFfC8rr2S89zU7mnoffJO6H6yiaRM_JgjNw7LxvLgrCw6kubhLcDdWgdTHvLz8HApYXLv5yF2-OmBNWI7hon46E6i7lKXxCdQ1Q7uDgLqp2doxx13t8EvRkB208aDuwN-uBg8PCkqglhRoMBrgoDteMXGZgzGr2E2i75wSrNXmDq6qBUYHo_BDqiBzW4tsOoHm5G5QKV-8KnvXzKiMXI5gDOlo0HHts1_V47XkHA1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a40b3b45d.mp4?token=TEww9XiB_c6r9Jwrq9uvQhBzz3S_LkloflbCLDJJORFWo-mg_rrWB0ZzqhtTlH53vtHgBYGQaFWe-CoUx81l8io0l2cYCexCc3QMxHtlCoa4oFfC8rr2S89zU7mnoffJO6H6yiaRM_JgjNw7LxvLgrCw6kubhLcDdWgdTHvLz8HApYXLv5yF2-OmBNWI7hon46E6i7lKXxCdQ1Q7uDgLqp2doxx13t8EvRkB208aDuwN-uBg8PCkqglhRoMBrgoDteMXGZgzGr2E2i75wSrNXmDq6qBUYHo_BDqiBzW4tsOoHm5G5QKV-8KnvXzKiMXI5gDOlo0HHts1_V47XkHA1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمار تلفات حمله عربستان به حشدالشعبی  ۱۰ کشته از تیپ ۳۰ شَبک ۲ کشته از تیپ ۲۴ حشد الشعبی</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19416" target="_blank">📅 11:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19415">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ny3tVsGmNmi4pq-aYXxbs5BIyk9OseZroTmjfeBL9Qx2V7_S1HVS_LhtWSB6AifYuswbdK-HfkUvs84snX1NwFQftg3wOPyfNU-7hSRmGOpVQDSs7KwPQjmnO8kS9TZN5rWw0n3QnBo56iwPRvhvNq7GjhceyrU7QM1EqPeXumk5qTMXFD0eZpoH7bldZ_97xMYH2dcYirXsU5cgkyd4F4xrMJpRT_VFLfNt0ZP5x_yAr1q1cFVRKokYFL1iJKb3fZY92QZugGyuycJeJKWiQUpjl-AFJ7geAn_-s78_Ya2uT9SzJGqPT3KlRbaMD3ElN57D0HVW2MjTV8rSOHGIAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز هم در وضعیت مناسبی قرار دارد و انتظار رشد طلا می رود.
دقت کنید که امشب نشست سرنوشت ساز FOMC را هم داریم که سناریوهای موجود
در این یادداشت
بررسی شده است.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19415" target="_blank">📅 11:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19414">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خب مثل اینکه «درنظر داشته» حمله کند  ایران، پس از حمله اوکراین به یک کشتی ایرانی در دریای خزر، یک حمله نمادین با موشک‌های بالستیک به یک بندر اوکراینی در دریای سیاه را مد نظر قرار داد.  اما گفتگوی تلفنی بین وزرای امور خارجه ایران که در آن این حمله به عنوان…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19414" target="_blank">📅 10:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19413">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خب مثل اینکه «درنظر داشته» حمله کند  ایران، پس از حمله اوکراین به یک کشتی ایرانی در دریای خزر، یک حمله نمادین با موشک‌های بالستیک به یک بندر اوکراینی در دریای سیاه را مد نظر قرار داد.  اما گفتگوی تلفنی بین وزرای امور خارجه ایران که در آن این حمله به عنوان…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/19413" target="_blank">📅 10:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19412">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCqJiw4u1UyWM8Q1AQJbEF8g_tb-L6Kk74vH-xP7uRXmnRk1p8ehsFdBVPdeNO0-MTdWTEP81MRjnkS0OfgB6eamJJUk6EESTfJbiVmxbLQSvBrgTZy8YIocd_msyfH-Pjve-M2WtC5Rdn94JV7Klbxl61wVfAkt1Cbw7IjTVOU1ACABmeL415fVI7NV57igss3WCWQBeEa5wyyq4GFKUVP6AduEvqHB4mlAMJ_8YTyYa_xGMuTnIvMuk9DEY243vZ98XRnBW_5iN2yTAj8kU7QvJJcglAv6-tiTo5jIZy27egPrLJr2yVGEMSqCXQ9Mxz2FEkEA6vKwZwl74H1shQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: ایران، یک حمله تلافی‌جویانه به یک بندر اوکراینی انجام داد.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19412" target="_blank">📅 10:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19411">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otFMW2V_ZKxdp5_gS62BO0YlQVxbR-xEwc121T1PEXEmBUYjne2lO-rRDm_qdOzPQXVP0z4gkfLj9C2mXTkVq9ZxhEXnYzfEddrVR4_GSlrFvBaxIs6xYwl8WO7MYwYmTvXPb6afuIwZOMa8zhE-UzYKzlxo8VeUyBIML2MQaAHtiWpXhwyNWGNwdazpGm-E6sz-vhdBqUPUkK7UrBVubu0d4GA0G_rycxR9-jN1r8dO6oRchmebkkEKqfx56i44udTUjh4j3-8vaQlP5EoUR15F-2kflHZMsBKIXiK2R9NrFzuRTK3ALbye8bno5__E5aCWtii36XRgBWKw2_sEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌ها، ایران قرار است در یک قرارداد به ارزش 60 تا 70 میلیون دلار، 300 تا 400 دستگاه موشک دوش‌پرتاب چینی (مدل‌های QW-12 و FN-16) دریافت کند. اولین محموله‌ها طی چند هفته آینده از طریق شهر اورومچی و از طریق پاکستان به ایران ارسال خواهند شد.
این قرارداد از طریق یک واسطه مستقر در هنگ‌کنگ به نام "Zhongqing Baoshang" انجام می‌شود.
چین و پاکستان این گزارش را رد کرده‌اند.
منبع: رویترز</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/19411" target="_blank">📅 10:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19410">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNCbm6-QXscD68XsiVboq6-q_2WODM5LrJvU3JJv4SFNEixkeN7gf0MmUxaxKgFaUvamAz0RtGPB84JxPoP4TOI0vX1PZc80JlSepg6VJeaf3HEf7XBxZ5zzABRhxzTwFKCUy5uQWgpp013NoPR121VrReFv-cwoeFLQ3TtJeRYseGQIIDaZLOQsASaumReaS0iI9T8ZFk6jsx72_DaVnNmIDPgWjNztizYrBfe5PYrSfVKgHzAu5GdxZFRoIWgqVs0KRa7IecCphKOlJKAxBgDXmDuGfti5-skdhqIbBhM7g_iQ2JuaODuN0tLHJ0rPf-ZzKy8x7-BnCxbARg9pfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: ایران، یک حمله تلافی‌جویانه به یک بندر اوکراینی انجام داد.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19410" target="_blank">📅 10:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19409">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نیویورک تایمز: ایران، یک حمله تلافی‌جویانه به یک بندر اوکراینی انجام داد.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19409" target="_blank">📅 10:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19408">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حملات عربستان به عراق !  گویا نیروهای حشدالشعبی هدف قرار گرفته اند.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19408" target="_blank">📅 09:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19407">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaB5PL3k4wxTXJlBjrvMamNTaL6pOfFRQHAXtin4zIJvnDB3DTyIzf4iFlGF3x4JiWUTIpF4F_cJE1Uk2w0nuPaGYr8goFlHLv6cjbyjgrZf0sTAviy-ouByAj836WuGvzbEz713iIUfQfqiqjYf_fLWRu7Y5xtxXwvyvkgnJtUw_hqggZgyB1FqxfTiE2HDJIuj7eFowzw0zym2DiuxX8nmMYuo13vLnLUnuHy9eKwj1DtRcCOPPGQArE6qnupuIzTFWHLIEJzxBCWUoJvcM1bOkTuABT3bFeVgJh7TuYajK7oEqUn008199CuBmFE_1RTYYoS9kEolThdZxYoJqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حملات عربستان به عراق !
گویا نیروهای حشدالشعبی هدف قرار گرفته اند.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19406" target="_blank">📅 03:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19405">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogcWh-Unycn4QkH8sOdI9cou7UibRwCdpbvnvUnk8_wyQrLZasYU1-Fy8utjdny6vW6nuEgT8qT7CoHDddAxL2uF-lKHHoJV5FBS5j3nWjNgbqu2tp8u3W-mr18OzqqfPCrgMQI0stUgu-pyZxTxuUS8NzVwDs4-mebmt6mt9Q0hNiTYe9qog3M_wruVn3SNPwFj7glx45rVqzjE0WIsAhOJEKH03quBkbkIBpQyUshQoqDpQnSdnVdjsHKLYyNcas4Ctqco2XaY2RbzHLTDEeJ2_oXQ01De6LG1Rfnqez6anVLEvXb35Y3ONucj31VsbJt8KINTHh4kMBpVwjMwWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/19405" target="_blank">📅 02:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19404">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQNwH1seG8PNU0iK4htVlKvHxRC4QXS_YVLCiXoj03JuW_4eFIHsvTY8fnioPzQuAMS1lYdtQgCMWbIh6r-3AFxmUfHhdyIaPamFCCGAnOzv7_CPwcdcP10bLxt00rr9QqPEmXfz9ckqpkgVCZdmlhDC4aA0T24W_xwBCrSWXFq2csvZFB4nQ1kNmHC49wBBJVCcyhhMfkrdKdaM_Oxnbg4QVvnxnGQd2ngcKFe6B1RshhAehZhz8KSraoelB0A9nTx_Ap4l_c_cd6WUUNpVPNufMSIsSRWH4-1MlRZnASIMIdilac0CFdxl-4B08A27CsV-Y04CH-X963UWHMRNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه جنگنده های ما پرواز نمی کنند و این یعنی احتمال حمله هوایی بالاست.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19404" target="_blank">📅 02:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19403">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrqcOd-xYkiI5PsRkf9xmwRUnZX5KOk7WKfLQbMwXhoJUp3Wp7zpDXvWR4Uk5DeudVgkvbn5ciy1FZzhe1qB5mBis9AONrKiD0O_VY5kzqZsUB73OUAqxmsvM532ZLExCgcU8ay38SGftVaCdPOjV2y27uofd4QHft0cxSztNgZGmSHmkmPmknIqKShsHR26X_4joH3thcsopbKwqQO47oQuA7Amc6zUx9IfuohKVJ3HkbM7oS2i1gIMBziYm1Jej8LgDUB3Lu1bAZHHaEZR8y2SvGTZ0WuXigF9NcNac25sSuNm-8H6ydEEy2MavRCJAzSZMmWqzGOAoiEPg1O-JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلاً قیمت نفت بیش از 5% پرواز کرده</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/19403" target="_blank">📅 02:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19402">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دیدید؟ همه گویا رهگیری شدند!</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19402" target="_blank">📅 01:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19401">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ot8sUyrVY8DySGykYcYPoLioQ8G4H5FUtAdS5j1QP-XvOB7g3WNX1rITqFM69tiGDBkTrif7LjAlvbo05NCEA9tQdlk2MI2fjiJD5l_f6aj0K6J59ZIQ6R1lHnhhEhHRVIzbakfUL8_FRvF4VIW1JKfuvdrUav0sz2c65gunZ3K3CFs0vB_SlcfLii2IpeuNMOIdxL6xQiKLxkvKO4vyKzAuP4XI3MY7ifRU-l444pCU-z_nQe1YNtLxl2uMosdg9ZGRnW5zvk5c9bj59xmeOjros5gjnZXA25Y6OBYgrju--vRrLpVzK0WMYMK5B0ZzYZirEG_nLOkhNXsL2UkKIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدید؟ همه گویا رهگیری شدند!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19401" target="_blank">📅 01:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19400">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اگر هدف پایگاه الازرق باشد هیچ اتفاقی نمی افتد.  مگر اینکه یک پایگاه الاحمر نامی را بزنند تا در هم کوبیده شود.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19400" target="_blank">📅 01:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19399">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">صبح ها اعدام داریم، ظهرها قطع برق، شب ها جنگ!
بعد برخی آمده اند تولدم را به من تبریک گفته اند!
وا بدهید لطفاً.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19399" target="_blank">📅 01:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19398">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvXQT80tRRDRSKhf1SASYqmkq66nriVQ7WZ88vMQ38P-1EW_d2WVjhKJlCSChTA5FcU8OQ4l--L5g2Mm1dslRLnI6HO-K1NYHtdV0TXtGlmFYoG4y1hJq_4nttTEjN_8J7J38_aGuFQw1cwgWZaob_sYFgGWU4n-i8K4NbyxXfj4ssdl87vN49JUJuCl2efbWPkOvz9l7arVM4G0V4M4cguv2h9x5XHjQoleiTMyFJuHRnyXYPyDFvKr5tm6uwHyZNZp0lpsVtPgvygItKE4h_ZMUr-5TLOXDPY6yo9A0odT0YQrbKtodNXLAr2xU-uSMnpPXn__76dTkaQZKmanCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جا دارد دوباره گوش جان بسپاریم به آوای روح بخش بانو لورا برانیگن که زینت بخش این شبهای پرکت خواهرمیانه است.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19398" target="_blank">📅 01:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19397">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">جا دارد دوباره گوش جان بسپاریم به آوای روح بخش بانو لورا برانیگن که زینت بخش این شبهای پرکت خواهرمیانه است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19397" target="_blank">📅 01:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19396">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مقصد گویا اردن است.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19396" target="_blank">📅 01:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19395">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">به نظر داریم وارد موج 2 از 5 می شویم و موج 1 از 5 تمام شده است.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19395" target="_blank">📅 01:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19394">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گیِرْت وِلدِرْس، چهره راست‌گرای هلندی:
من آرزو می‌کنم که در اروپا افراد بیشتری مانند بنیامین نتانیاهو وجود می داشتند!</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19394" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
