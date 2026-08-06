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
<img src="https://cdn4.telesco.pe/file/MQzecT129vJMjJQK61M83UMzTBM3L9koVe2nSs53FnRXaFSzyBPGIVUXIsswtknQ6msqT4r_sihH9-0Dgl6NJGvJNXplyM7U9fuPuo_okKvVuMM3v49NHPmuvAjBJ7-6UxXKCLQYQ5kEHoo4mvT50i4TJ_ptazSnZsFvH_MYq2Zx_v2vMV3PJ-RfakJsKEKLvjltCV7h9Drc4A00_oFGtKCrYGJ_PEMlXsSmn7rVykTPJKT7ZTGahwjSCK2MhlT4AyaWyU4fjYITR5Nr7OvuA1ror3lUMb-sGQCVDQC0up8BhiiMJ42BhzyKjrd4A_Hl5t4JZcca9xrq3S7T10RN2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 18:14:03</div>
<hr>

<div class="tg-post" id="msg-19738">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بیانیه صادر شده توسط نیروهای مسلح یمن
به نام خداوند بخشنده مهربان
خداوند متعال فرمود: {هیچ تجاوزی جز بر ستمگران نیست.}
دشمن جنایتکار سعودی در ادامه تجاوز و محاصره خود علیه مردم عزیز یمن ما که نزدیک به ۱۲ سال است ادامه دارد، شاهد تجمعات نظامی گسترده سعودی در مراحل پایانی خود بوده است که هدف آن تشدید درگیری علیه استان‌های آزاد شده و مردم یمن برای منصرف کردن آنها از موضع خود در مورد پایان دادن به محاصره ظالمانه است.
بنابراین:
نیروهای مسلح ما یک عملیات نظامی گسترده و دقیق را با هدف قرار دادن مراکز تجمع نیروهای دشمن سعودی در مناطق الرویک، العبر، الثانیه و سایر اردوگاه‌های متعلق به لشکرهای اضطراری اول و سوم، با استفاده از تعداد زیادی موشک بالستیک و پهپاد انجام دادند. این عملیات منجر به موارد زیر شد:
* کشته و زخمی شدن صدها مزدور دشمن سعودی.
* انهدام و آتش زدن تعداد زیادی از اردوگاه‌ها، مراکز تجمع نیروها، انبارها و تسلیحات دشمن سعودی در منطقه الوادیعه در شرق کشور.
* انهدام تعداد زیادی از خودروهای نظامی موجود در اردوگاه‌های هدف قرار گرفته.
نیروهای مسلح یمن به دشمن جنایتکار سعودی نسبت به هرگونه اقدام تجاوزکارانه علیه کشور و مردم ما هشدار می‌دهند و عواقب هرگونه تشدید اوضاع را متحمل خواهند شد. به گمراهان و فریب‌خوردگان در میان مردم خود توصیه می‌کنیم که اردوگاه‌های دشمن سعودی را ترک کرده و قبل از اینکه خیلی دیر شود به خانه‌های خود بازگردند.
به مردم عزیز یمن در تمام استان‌ها اطمینان می‌دهیم که نیروهای مسلح کاملاً آماده مقابله با هرگونه تشدید اوضاع هستند. از همه مردم خود می‌خواهیم که هوشیار باشند و با هرگونه تجاوز سعودی مقابله کنند و به مراکز تجمع نیروهای سعودی در هر کجا که باشند حمله کنند.
ما به استراتژی «محاصره در برابر محاصره» تا زمان رفع محاصره کشورمان ادامه خواهیم داد.
خدا ما را کافی است و او بهترین سرپرست، بهترین محافظ و بهترین یاور است.
زنده باد یمن آزاد، با عزت و مستقل!
پیروزی از آن یمن و همه آزادگان این ملت باد!
صنعا، ۲۳ صفر ۱۴۴۸ هجری قمری
صادر شده توسط نیروهای مسلح یمن</div>
<div class="tg-footer">👁️ 335 · <a href="https://t.me/SBoxxx/19738" target="_blank">📅 18:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19737">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 404 · <a href="https://t.me/SBoxxx/19737" target="_blank">📅 18:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19736">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حملات سنگین اسرائیل به جنوب لبنان آغاز شد.</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/SBoxxx/19736" target="_blank">📅 16:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19735">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نیروهای انصارالله یک پایگاه نظامی متعلق به نیروهای "دفاع وطن" که به عربستان سعودی وفادار هستند، در منطقه "الودعیه" را مورد هدف قرار دادند که در اثر آن دستکم ۵۰ نفر کشته شدند.</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/19735" target="_blank">📅 16:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19734">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اسرائیل و افسانه تجزیه ایران  در ایران امروز، مدتی است که افسانه‌پردازان، بی‌ وقفه تکرار می‌کنند که اسرائیل در اندیشه تجزیه ایران است. چگونه ممکن است کشوری با جمعیتی نزدیک به یک‌نهم ایران، مساحتی حدود یک‌هشتادم، در فاصله بیش از هزار کیلومتری هوایی و نزدیک…</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/19734" target="_blank">📅 13:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19733">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اسرائیل و افسانه تجزیه ایران
در ایران امروز، مدتی است که افسانه‌پردازان، بی‌ وقفه تکرار می‌کنند که اسرائیل در اندیشه تجزیه ایران است.
چگونه ممکن است کشوری با جمعیتی نزدیک به یک‌نهم ایران، مساحتی حدود یک‌هشتادم، در فاصله بیش از هزار کیلومتری هوایی و نزدیک به سه هزار کیلومتری زمینی (آن هم با چند کشور مهم حائل بین راهی)  قادر باشد کشور ـ تمدنی چند هزار ساله را تجزیه کند؟
این در حالی است که موضع رسمی اسرائیل نیز چنین ادعایی را تایید نمی‌کند. بنیامین نتانیاهو در رویکرد علنی خود، از جمله در سال ۲۰۲۶، شایعات مربوط به تلاش اسرائیل برای تجزیه ایران را رد کرد. خوب یا شوم، رویکرد رسمی بی بی متوجه جمهوری اسلامی است، نه تقسیم ایران.
ولی اگر روزی همبستگی ملی ایرانیان چنان فرسوده شود که کشوری این چنین کوچک و غیرهمسایه بتواند سرنوشت ایران رقم بزند، دیگر  مساله، قدرت اسرائیل نیست؛ مساله، ضعف درونی ایران است. هیچ قدرت خارجی، حتی اگر ابرقدرت باشد، نمی‌تواند کشوری را تجزیه کند؛ مگر آنکه شکاف‌های داخلی، پیش‌تر پایه‌های آن را سست کرده باشد.
از همین رو، روایت «اسرائیل در پی تجزیه ایران است» بیش از آنکه یک تحلیل استراتژیک باشد، افسانه‌ای سیاسی است؛ افسانه‌ای که گاه برای بزرگنمایی تهدید بیرونی و به حاشیه راندن مسائل و کاستی‌های درونی ساخته و بازتولید می‌شود. تاریخ نیز یک درس روشن دارد: یکپارچگی سرزمینی و مردمان کشورها را پیش از هر چیز، همبستگی ملی، مشروعیت سیاسی، حکمرانی کارآمد و رضایت شهروندان حفظ می‌کند، نه صرفاً ترس از دشمن خارجی.
#یدالله_کریمی_پور
#karimipour_k</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SBoxxx/19733" target="_blank">📅 13:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19732">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 20</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19732" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 20
پنجشنبه 6 آگوست 2026</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/19732" target="_blank">📅 13:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19731">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TW0FbheoMuX9ffU5dyK3D7drsUYof83Wou3IV6X3fxeX2ACTS41c7HmOcsl4RDlobZvCc8v16xWCqZDAEhTndaSoUx7GTxNEnJ1a-sUNyfzPAYyK50rAF_aQA6LQPYH0okNpzBgPWcWlMPVDxJ4fP2sUTFph6L3zP-_V6PfKY4828rWIfwTP2Lni4JJN_37eTzG89EByE4rwK8QRYZVSVIS-Z3zOFF7QTfjcLv07XM9bokexVmPHqftbdctK07x4pMVLmZc63nFJqi0Yfl4SUfFwy_4tNkFY0_-omuYbDk7kLPhQ0FJW0VOwoq4gLTnZrbyXR9Q3rvEvbxIfn-F23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/19731" target="_blank">📅 12:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19730">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9jgPZJfCpeTAilM3SO6x8rue_-Aa4yTIC0VAq-MPPZT9L51eaHjeZlMxnNIGLKv6m4LCCl9leL5C-t0g7kVVYb5U5rNG0k4Xmh4VQ5U5B31f3sElUuIARTs3WiyuwMsuUMih0JrHl1BL1FxVAsewNRQAApkdZHYndqyX53K_8-MxDcpb2-vPwg2msV8HyJkOrDBUAso_Ce0sKZZxIiR35vCzhiYtQ88ST5fNvIa07lY2XIrK7zMG_28Zz2W6jqkNTzZdJE5a6DZiiiS31gMb2BWK5-unem_LFl-hkyVwYbbvN5Zx2WTRNoR0TpfJiSpgRjwd2tFKyZSmvwzQBaXnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفته می شود با دیدن این عکس، ترامپ از نابودی زیرساخت های ایران صرف نظر کرده است.</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/19730" target="_blank">📅 12:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19729">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg0ZeNrbn4xgsGASF7kMJ5p0fdmj8XMpK4LnlfH5N9Kl6FRFxF8_dPcTyTdzE2v1P-2bJ9Nyh9Z_Wbms2c08qe8X4arYZUZD3qbx662hrzPaSfLpsjhXdNo7Sb5QB6xOIzhWjaBVM4Eayb-QjpPLF4IaUXYmNqfjPcLjO5gcninMSU62Tu0XsDyTicngmAkpdk2YJgK_IJpU0E8x3pW6emPrPVDWuhjiWKxEbCAZ3LPQYKNruQLZZj7zcZfbQcWHZ8W6zxt0cstcwXPXxcrTrG4R2qhqTPH6jQy-_4k9ltnOXb6ywr7_B8Ynupfjesxe98Y7_afArEQCC65ic-wsTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه قرار دارد. پیش بینی می شود طلا امروز مقداری افت اصلاحی داشته باشد (با توجه به رشد GRI از دیروز) اما دوباره به سقف (4300) حمله ور بشود (با توجه به افت میانگین شاخص GRI در روزهای گذشته)</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/19729" target="_blank">📅 11:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19728">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سبحان الله!  هندی ها حتی در باشگاه های بدنسازی شان هم ممکن است غرق بشوند!  (ماشالله چه بدن هایی هم ساخته اند در باشگاه)</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/19728" target="_blank">📅 10:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19727">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d8645934.mp4?token=IyiOpKvXeWWDr8s8R2crz38vQPneB-y1c1fRFetnUgQHL4_zfn9yIgE6O_LYt0XZjv3BvJOWVgk8zuSYa-mQv2U4MGE-iwt40M4zo9B2-KjQZgFYBDbAg_GFca-xDzv61RftiEIirsx1azUoWT-ufz3E6jKK6WE2JqO24MvWOP_PzRV29klqqK7wUFNCnwvL4cJweCH4AAhJEtUuXAhLFt3Cfb1BAaHlvlPPq6pi2BhSSFb3gtR285t_1onFkbq2XYo49Ut1o9JjD1tX3z5bIwlQX9ekUdS4itJUZsfVlShg_bqICcvA-DHUubaqQRD4DUyuBngAvRlArzagegJSZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d8645934.mp4?token=IyiOpKvXeWWDr8s8R2crz38vQPneB-y1c1fRFetnUgQHL4_zfn9yIgE6O_LYt0XZjv3BvJOWVgk8zuSYa-mQv2U4MGE-iwt40M4zo9B2-KjQZgFYBDbAg_GFca-xDzv61RftiEIirsx1azUoWT-ufz3E6jKK6WE2JqO24MvWOP_PzRV29klqqK7wUFNCnwvL4cJweCH4AAhJEtUuXAhLFt3Cfb1BAaHlvlPPq6pi2BhSSFb3gtR285t_1onFkbq2XYo49Ut1o9JjD1tX3z5bIwlQX9ekUdS4itJUZsfVlShg_bqICcvA-DHUubaqQRD4DUyuBngAvRlArzagegJSZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این جنگ تمام هم که بشود باز هندی ها غرق خواهندشد.</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/19727" target="_blank">📅 10:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19726">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:
ما گزارشی از حادثه‌ای در ۹ مایل دریایی جنوب شرقی کومزار در عمان دریافت کرده‌ایم.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19726" target="_blank">📅 04:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19725">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ در مورد ایران:  ایران به ما احترام می‌گذارد. آن‌ها به ما احترام می‌گذارند.  ما در حال صحبت هستیم. ببینیم چه اتفاقی می‌افتد.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19725" target="_blank">📅 01:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19724">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ در مورد ایران:
ایران به ما احترام می‌گذارد. آن‌ها به ما احترام می‌گذارند.
ما در حال صحبت هستیم. ببینیم چه اتفاقی می‌افتد.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19724" target="_blank">📅 01:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19723">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtOnazEQLSPnSsa_NqhdsQoV8bya-X3-bopC5IVSPvb_1iuR88CDSJ0uk3-uxkgH0_RCGmKfQplMRc2I6sOIeSkKudt2h-dPWnrukeI-i4HQe5igdPiHU9clTJREpGW0sODepwwoU0pH-0f-ez7pOakl0MlYcVMJhTSu2f_aQdrx1gAbYwxUHG1zXZJ4ufHw_9_a7nSbJXRrZDDIwN4sMeU3H9AlLyMwcpMxl5dLwDcdkFqZEzoGKON1kolXkj-3xpU9_TCS4lcF9p70oK9wZVlFELUD22pDSuHXk_pQSLUJLh786Q_a1FDnXwTfDuP5H12nctUe9cxTAowuINQZhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAUUSD
— H4
میتوان چنین ساختاری برای طلا متصور بود.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19723" target="_blank">📅 23:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19722">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRPzNNaiBqtCskSoqrd3OdgCidUEMYfaHAV7_9uPDYJSowqeOe36KYkbW2ccgdnmpMij7VxD543HfDdmQ7K2xWE9DSBZ7PxyKjQI3-BxOsglCjI1RKSuKPYu7G5YZ9qtHbcQRFlHseQSeHWfek_03l5ehrW1PoZsJrlpzPgU8dDPGYLEKVoxNiVBF8XpHuraNXUUBEZ3R73PoQ6e4TeXoEIUF_reX_26eCG5vI3vTdjlTA7rLadpeE63tZVaLh8QtrmyK0sCy1s5F-yhhEHwgGweqwlqCL2571yXxc6zIDYWE58O7zSeQISKwSRUKD7TFf2drDKcVaSgHst8SoUmRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح پایینی قرار دارد و ادامه جو ریسک پذیری پیش بینی می کند.  (شخصاً با توجه به اینکه:  — عمده رشد امروز در سشن آسیا روی داده — پس فردا گزارش NFP داریم — اعتمادی به توافق ایران و آمریکا ندارم  اینجا خریدار نیستم و پله ای…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19722" target="_blank">📅 22:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19721">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رئیس‌جمهور ایران، مسعود پز‌شکیان:  هر چقدر هم که فکر می‌کنم، نمی‌توانم هیچ دلیل منطقی پیدا کنم که چرا آن‌ها رهبر، فرماندهان و دانشمندان ما را به قتل رساندند.  بسیاری از فرماندهان و دانشمندانی که به قتل رسیدند، حتی صاحب خانه هم نبودند.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19721" target="_blank">📅 22:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19720">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رئیس‌جمهور ایران، مسعود پز‌شکیان:
هر چقدر هم که فکر می‌کنم، نمی‌توانم هیچ دلیل منطقی پیدا کنم که چرا آن‌ها رهبر، فرماندهان و دانشمندان ما را به قتل رساندند.
بسیاری از فرماندهان و دانشمندانی که به قتل رسیدند، حتی صاحب خانه هم نبودند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19720" target="_blank">📅 22:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19719">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVc1q9c4LhgFefO9f3Cu_7aCe3eKnTZ0y4HD2hYfiTN255E1R7GRTeEVJF_kSX9rkVcGBX7ErEgigQE_cs7M728Yv7v9-xR5nktG3JAw6eq5MRHpOTdWq-bFUWBOjQ1FtE-pPAYHyMPdyjAgTW3Jb6r_BPVQdjKFn0HW_8PXwtgX0_9vwoGTU2a7tHKZNq5sA94zTKHRYmuxo16tBwTmUB3_70dZ-kpLNqwG1QIL41EK8VnJ41fNMjoGRlq3j-fRHUa37ToGzIGBevzTslzI4Qm3jEF1Of0975zjrFaw4yA9M6QLIKB8v658Ou3mvnOZ3DOUKRmwvwIGo7plQQb-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  محسن رضایی: منتظر نفت ۱۵۰ دلاری طی روزهای آینده باشید.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19719" target="_blank">📅 21:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19718">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">روسیه به طور فزاینده‌ای از موشک‌های پدافند هوایی S-300/S-400 در نقش‌های حمله زمینی استفاده می‌کند که تهدیدات شبه بالستیک سریعی را ایجاد می‌کند که رهگیری آن‌ها دشوار است.
طبق اطلاعات استخباراتی اوکراین ذکر شده در تحلیل، روسیه حدود 200 موشک RM-48U تبدیل‌شده را در سال 2025 تولید کرده و قصد دارد بیش از 480 موشک را در سال 2026 تولید کند.
این موشک‌ها دقت کمتری نسبت به اسکندر دارند اما تعداد اهداف پرسرعتی را که اوکراین باید در برابر آن‌ها دفاع کند، افزایش می‌دهند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19718" target="_blank">📅 21:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19717">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">غریب‌آبادی:   موضوع دریافت هزینه توسط ایران در تنگه هرمز بستگی به تصمیم مقامات عالی نظام و رفتار آمریکا دارد.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19717" target="_blank">📅 21:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19716">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">غریب‌آبادی:
موضوع دریافت هزینه توسط ایران در تنگه هرمز بستگی به تصمیم مقامات عالی نظام و رفتار آمریکا دارد.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19716" target="_blank">📅 21:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19715">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فوری | معاون وزیر امور خارجه ایران: پیام‌هایی از ایالات متحده دریافت کرده‌ایم که نشان می‌دهد این کشور آماده است تا به تعهدات خود بازگردد.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19715" target="_blank">📅 21:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19714">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فوری | معاون وزیر امور خارجه ایران: پیام‌هایی از ایالات متحده دریافت کرده‌ایم که نشان می‌دهد این کشور آماده است تا به تعهدات خود بازگردد.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/19714" target="_blank">📅 21:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19713">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رائفی‌پور:   ایران به اردن حمله کرد و ۶ جنگنده اف ۳۵ را نابود کرد چون قرار بود به مراسم اربعین و مواکب حمله کنند</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19713" target="_blank">📅 20:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19712">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رائفی‌پور:
ایران به اردن حمله کرد و ۶ جنگنده اف ۳۵ را نابود کرد چون قرار بود به مراسم اربعین و مواکب حمله کنند</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19712" target="_blank">📅 20:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19711">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">منابع عربی گزارش حمله موشکی به بحرین را منتشر کردند - خبرگزاری مهر.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19711" target="_blank">📅 19:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19710">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">منابع عربی گزارش حمله موشکی به بحرین را منتشر کردند - خبرگزاری مهر.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19710" target="_blank">📅 19:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19709">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">این تحلیل درست 4 روز پس از پایان جنگ 40-روزه ارائه شد و همچنان بر اعتبار آن افزوده می شود و خواهیم دید روزی می رسد که تنگه هرمز را فقط خودمان استفاده خواهیم کرد.  از همه کریدورها که محروم ماندیم و سهممان .... های باقر شد این هم از تنگه هرمز!</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19709" target="_blank">📅 19:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19708">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJp4CcKY0EBPZbYlD3ImsFqgUjt88yBtq6d6kW0HQAifvb7EU5cOfSavL-tm_lTzk8IoIMxt-71A5Z69ss75s5f8KnQMvsaWQwDmcEvifhXWxTOv7nSJ1ZHkSEwzNnFwibvfSdlEtlaipnwqqzem8r0kOi1WWY0zBKPRmmsi1HBj0ex0qLPVWUMXpa_Y2jExozhvCQ6s6hrGE1-rufsnbLuMJh_Es4Xkxb38Ql2ltBpk_S_aHLfcbDkR7KztqRGphy3zEJy7Poev40Fq8zSCAm1JLsIiOD-gup-nXaU6aVVkrYL_N_ybdhMx8RojA3ZxuGsxVUOJ7-EjGpa4dceUfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
طرح جدید اسراییل برای ساخت
پایگاه‌های نظامی در جنوب لبنان
روزنامه هاآرتص گزارش داد که رژیم صهیونیستی حدود ۲۳۰ کیلومتر مربع از خاک لبنان را همچنان در اشغال دارد و قصد دارد بر روی ویرانه‌های روستاهای تخریب‌شده، پایگاه‌های نظامی جدید احداث کند.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19708" target="_blank">📅 18:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19707">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/19707" target="_blank">📅 18:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19706">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">طبق وب‌سایت وزارت خزانه‌داری ایالات متحده، ایالات متحده تحریم‌های مرتبط با ایران را لغو کرده است.  منبع: رویترز</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19706" target="_blank">📅 18:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19705">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فوری | یک مقام ارشد ایرانی به الجزیره گفت: هرگونه بستن یا باز کردن تنگه هرمز به اقدامات واشنگتن بستگی دارد.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19705" target="_blank">📅 18:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19704">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">طبق وب‌سایت وزارت خزانه‌داری ایالات متحده، ایالات متحده تحریم‌های مرتبط با ایران را لغو کرده است.
منبع: رویترز</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19704" target="_blank">📅 17:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19703">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">منابع فلسطینی گزارش می‌دهند که حماس، واحدهای سازمانی، فعالیت‌های مخفیانه و عملیات امنیت سایبری خود را به ترکیه منتقل می‌کند، در حالی که قطر به میزبانی رهبری این سازمان و فعالیت‌های عمومی آن ادامه خواهد داد.
— روزنامه جروزالم پست</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/19703" target="_blank">📅 17:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19702">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پیش‌نویس قانون ترکیه برای حمایت از خلع سلاح و بازگشت به زندگی عادی اعضای سازمان پ.ک.ک
ائتلاف حاکم ترکیه، روز چهارشنبه، یک پیش‌نویس قانون را به پارلمان ارائه کرد که هدف آن پیشبرد روند صلح با حزب کارگران کردستان (پ.ک.ک.) است. این قانون شامل حمایت‌های قانونی برای بسیاری از اعضای سابق این سازمان و تعلیق مجازات‌های زندان برای برخی از افرادی است که به عضویت در پ.ک.ک. متهم شده‌اند.
این قانون‌گذاری، که انتظار می‌رود در اواخر این هفته توسط پارلمان تصویب شود، به دنبال پایان دادن به درگیری‌های دهه‌ها طولانی با تسهیل بازگشت هزاران نفر از اعضای سابق پ.ک.ک. است که در حال حاضر در شمال عراق مستقر هستند.
بر اساس این قانون پیشنهادی، سازمان اطلاعاتی MIT ترکیه مسئول بررسی و تأیید خلع سلاح این گروه خواهد بود، در حالی که یک کمیته متشکل از معاون رئیس‌جمهور، چندین وزیر و رئیس MIT، بر روند تسلیم و تحویل سلاح‌ها نظارت خواهد کرد.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/19702" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19701">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مقامات آمریکایی تأیید کردند که هرگونه توافق احتمالی با ایران، به طور قطعی تضمین خواهد کرد که تهران کنترل مسیر کشتیرانی تنگه هرمز را به دست نخواهد گرفت.</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/19701" target="_blank">📅 16:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19700">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کونستانتینوس فلوروس، رئیس ستاد سابق ارتش یونان:  هر کسی که پا به خاک یونان بگذارد، ابتدا سوزانده خواهد شد، و سپس ما از او می‌پرسیم که کیست.  این تنها واکنش مناسب به تهدیداتی مانند: "ما یک شب سر می‌رسیم" یا "ما به جزایر شما قدم خواهیم گذاشت" است.  منبع: Proto…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/19700" target="_blank">📅 16:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19699">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_mSUUQqTJTfrgA2NuMRmFzVjy-VF1FpvxsVrOi9BY-zzScOor3VtPeVAi7ApoIewdilxJGOH1ir1XpSg47XgPpyPKyKq7GqAyyakKYikpBUJhFfhIjqJEcyCI5g9XzZMsO7Hy7EsGFjLgOle6-XhCXpuNRRgrtmiH5uDMHj0Oa3j-aFGAxGcXrMunIl_tiFU2oVSgRmGjeSbZrumP_INnlutsMMgKFramRzl_4d5VZvc3JL3GCWroUEAtxZA8UB9ZyqOMDxt6sjN_y67WL9n90j6xSvZ8KRjIATa5o_FX4p43WzH5hQa15LiMf8K3hTv0YcwIKuZrMJGKSgbIn_bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنش‌های میان ترکیه با یونان دارد دوباره داغ می شود….</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/19699" target="_blank">📅 16:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19698">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5EJRzss0EtFpZDZ6KVmz3nFN-K5eVUSxo4KoGgmLGlDn0PkGfSbnAh1i4uAQAxHof3RqV1FqrWqYPF-xyL7RyPhKYa1fL6_WPVR6wWSKpl2r5sJKWYFU2YdUKcuQyNH5nSSIGqBDVnUlMulVtw8PJgHxVcuyZYA7c8n0H7ZVMxTgYDHPTQe1HkFGaUQrqyU6VAg7zDVZUXcPzx_ObUHlZjj4CHx8bKoVl8Rgr8l1RFCjI0iGT3czJVseXOn_duYm_aIpjU7_Qg25Wsnadbvoa3QDgrSpEbHqFX2BndzyWKsd1HtHZJY7OAr9V3fe8XTNIwXyvfiFwLkLLNHOCnjvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این فیلم را ببینید!  در حالی که همه هنرمندان و تماشاگران (از جمله بهروز وثوقی افسانه ای) به صورت ایستاده سرود میهنی «ای ایران» را همخوانی می‌کنند، «نون میم» با آن چهره و ریخت هیستریک ش  مثل بزهای کوهی به در و دیوار خیره شده و گویی در سالن تئاتر دنبال یونجه…</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/19698" target="_blank">📅 16:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19697">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یک مقام ارشد خلیج فارس گفت که احتمال اینکه آمریکا و ایران تا روز جمعه به یک توافق موقت برسند، ۵۰ درصد است، اگرچه هنوز گروه‌های تندرو کلیدی ایران موافقت خود را اعلام نکرده‌اند.
— سی‌ان‌ان</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/19697" target="_blank">📅 16:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19696">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یک جا آرام می شود، 13 جای دیگر جنگ می شود</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/19696" target="_blank">📅 16:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19695">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شب های خواهرمیانه !</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/19695" target="_blank">📅 16:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19694">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نیروهای دفاعی اسرائیل (IDF) یک هشدار "فوری" برای تخلیه ساکنان روستای المنصوری در جنوب لبنان صادر کرده است، این اقدام قبل از حملات هوایی انجام شده است.
ارتش اسرائیل:
«حزب‌الله توافق آتش‌بس را نقض کرده است و ارتش با قاطعیت علیه آن اقدام خواهد کرد.»</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/19694" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19693">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ارتش اسرائیل برای حمله ای سنگین به جنوب لبنان آماده می شود.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/19693" target="_blank">📅 16:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19692">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حادثه دریایی جدید در دریای سرخ</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/19692" target="_blank">📅 15:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19691">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">422.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19691" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 19</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/19691" target="_blank">📅 15:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19690">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 19</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19690" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 19
چهارشنبه 5 آگوست 2026</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/19690" target="_blank">📅 14:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19689">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ژاپن در حال بررسی ادغام سیستم‌های هوش مصنوعی ساخت آمریکا، از جمله سیستم هوشمند Maven شرکت Palantir و Lattice شرکت Anduril، در نیروهای دفاعی خود است تا فرآیند تصمیم‌گیری نظامی را تسریع کرده و همکاری با نیروهای آمریکا را بهبود بخشد.  برای کاهش وابستگی به فناوری‌های…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/19689" target="_blank">📅 14:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19688">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6QkUEmrNgs7IVsqNBGqmXKA1tc-VjTdF0zRmJuLGdJfWBMSqaiYWzvrM3OBzNQj5FtMr1t27jkxw1HrT54Vu_lEKLsjmARfYmEzl4fgg3fYneclEJisSk4Vt91f643bzCAUoqul3KsTwbo8VVRXgBBzwFQTQviYME6_7R39-2AyEpgCUJDVHyOpYZAmOhkZSnhxWyp4mZtATMjJL3DkoBwn9Jf9JUVU9x-IpLjvQ9V1K1CStP3hfeRuEpJqLpuVp85iaKpeZTbwDi-RGm3edBRf1eiTotM-TuGbdkvhPdWZujofn3m1JpjD2dOc9fJTaUEQ9p8erzOSwMQAoIoIrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوشش ژاپن در تقویت توان دفاعی  ژاپن با تأکید وزیر دفاع خود، شینجیرو کویزومی، بر لزوم تقویت و تحول توان نظامی این کشور با «حسی بی‌سابقه از فوریت و بحران» اصرار می‌ورزد. گزارش سالانه سفید دفاعی ژاپن، منتشرشده در ۴ اوت ۲۰۲۶، بار دیگر بر تهدیدات فزاینده چین، کره…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19688" target="_blank">📅 14:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19687">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گزارش صداوسیما درباره مذاکرات بر سر بازگشایی تنگه هرمز:  "توافق احتمالی ایران و عمان درباره ترتیبات عبور شناورها از تنگه هرمز هیچ ارتباطی با باز شدن فوری این تنگه ندارد؛ باز شدن تنگه هرمز منوط به تغییر رفتار و تصحیح تخلفات آمریکا است و در صورت ادامه تخلفات…</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19687" target="_blank">📅 12:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19686">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">صداوسیما  به نقل از یک منبع مطلع:  توافق احتمالی ایران و عمان در باره ترتیبات عبور شناورها از تنگه هرمز هیچ ارتباطی با باز شدن فوری این تنگه ندارد</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/19686" target="_blank">📅 12:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19685">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترور ناموفق ترامپ!</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19685" target="_blank">📅 12:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19684">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">صداوسیما  به نقل از یک منبع مطلع:
توافق احتمالی ایران و عمان در باره ترتیبات عبور شناورها از تنگه هرمز هیچ ارتباطی با باز شدن فوری این تنگه ندارد</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/19684" target="_blank">📅 12:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19683">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqsJnKU6adI8seLgkLLRJfl4Yu4w3N8UzMfvG407YgZVLjqNl4n4QlNJXhZRAhiBTXCk_INToteVwMqLr_oBYoJeGGhDhJqevoCjJ3KV796tNH852tkG1JbA3O8rQpELS1uleUQthtqwT54timfYigvO_pze5b-SKPSOXYfmo91qWUwFCpIn3pKOIMoCHyCaAZ6R1ePW_ZE5XGMjcjDqsEG6pxYOb7f1LmCyuBYiBHCpk2Z7qZajqpCZ0owMx_zyqRcwjNHPpCAVBjwLsNOWduH6CotGVIgi8N7nJPyA5nYH8KkWZ8oGc6qcbEG8AeThY-5LOfOZs4Smgj5O8XMiKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح پایینی قرار دارد و ادامه جو ریسک پذیری پیش بینی می کند.
(شخصاً با توجه به اینکه:
— عمده رشد امروز در سشن آسیا روی داده
— پس فردا گزارش NFP داریم
— اعتمادی به توافق ایران و آمریکا ندارم
اینجا خریدار نیستم و پله ای می فروشم)</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19683" target="_blank">📅 11:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19682">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حوثی‌ها مدعی هستند که با موشک‌های بالستیک، تانکر نفتی سعودی به نام «وفا» را در دریای سرخ شمالی، در نزدیکی ساحل ینبع مورد هدف قرار داده‌اند و ادعا می‌کنند که اصابت مستقیم رخ داده است.
این هشتمین تانکر نفتی سعودی است که از زمان آغاز محاصره دریایی در تاریخ ۲۲ جولای، مورد هدف قرار گرفته است، و حوثی‌ها مدعی هستند که ۲۹ تانکر سعودی دیگر را نیز مجبور به بازگشت در دریای سرخ و دریای عرب کرده‌اند.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19682" target="_blank">📅 11:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19681">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msxezPcFRo7sZT8fFt0kUvVcLPZlGRz0VwJE7GQirjZ9h944efcfDFtuY1zgy-O5HqYPbL-y-1p0woaV9yeIRxCbbm8exTbw459ttSTuMgQVD16LfG5Jm7Ozp966ErNs1MK5RUMgqVAqRMkgUn5B09RALVyMXyWLCKcrUSkJXwJy5L33T3MLxmaAUZjWZCDjLkQQa-HLm4GQOUFPojTzu3DZN_JyJa-NDSfLyjfh4SsiCzxola9ASmIe-aF6T1zNAGDntIP8UZU3EAZiGCKdTCVo2kxZ-h3L-L-ODlDsEvpUN9yAlwuLv3psRHs0yYmm1bnobuPEe-DzqaYgMYONjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید جدید ایران برای قدرت هوایی آمریکا
خرید موشک‌های شانه‌پرتاب چینی توسط ایران و پیامدهای آن برای عملیات‌های آمریکا
چین در حال ارسال ۳۰۰ تا ۴۰۰ دستگاه موشک دفاع هوایی شانه‌پرتاب (MANPADS) از نوع QW-12 و FN-16 به ایران است. این معامله که ارزش آن ۶۰ تا ۷۰ میلیون دلار برآورد می‌شود، قرار است طی هفته‌های آینده از طریق پاکستان و به صورت هوایی یا زمینی تحویل ایران گردد. این موشک‌ها، با هدایت مادون‌قرمز، قادرند پهپادها، بالگردها و جت‌های آمریکایی را که در ارتفاعات پایین پرواز می‌کنند، تهدید کنند.
هدف اصلی ایران از این خرید، بازسازی دفاع هوایی کوتاه‌برد پس از پنج ماه حملات مکرر آمریکا و اسرائیل است. این حملات، آسیب‌پذیری‌های زیرساخت‌های نظامی ثابت ایران را آشکار کرد. موشک‌های جدید، به ایران اجازه می‌دهند تیم‌های سیار و پراکنده‌ای را در اطراف سایت‌های استراتژیک مستقر کند که امضاهای راداری بسیار کمی دارند و شناسایی و نابودی آن‌ها دشوار است.
از نظر فنی، QW-12 با سر جنگی ۱٫۴۲ کیلوگرمی و برد ۰٫۵ تا ۶ کیلوگرم قادر است اهدافی را در ارتفاع ۱۰ متر تا ۴ کیلومتر درگیر کند. جستجوگر مادون‌قرمز آن می‌تواند جت‌ها را در فاصله بیش از ۹ کیلومتر تشخیص دهد و احتمال نابودی در شلیک اول آن بیش از ۸۰٪ است. FN-16 نیز برای درگیری کوتاه‌برد با پهپادها، بالگردها و هواپیماهای کم‌ارتفاع طراحی شده است.
این معامله، علاوه بر توافق قبلی ایران با روسیه برای خرید ۵۰۰ پرتابگر وربا و ۲۵۰۰ موشک به ارزش ۵۹۱ میلیون دلار (تحویل تا ۲۰۲۹)، توان دفاعی ایران را به‌طور چشمگیری افزایش می‌دهد. چین و پاکستان این گزارش را تکذیب کرده‌اند، اما دونالد ترامپ اعلام کرد که چنین ارسال‌هایی مغایرت مستقیم با قول شی جین‌پینگ دارد.
آمریکا در حال حاضر با کمبود پهپادها مواجه است. از آغاز عملیات در ایران، ۳۰ فروند MQ-9 Reaper سرنگون شده‌اند. با در نظر گرفتن خسارات جنگ یمن، آمریکا یک‌سوم از ناوگان ۱۳۵ فروندی خود را از دست داده است. خط تولید Reaper در ۲۰۲۵ متوقف شده و هر فروند ۵۶ میلیون دلار قیمت دارد، بنابراین جایگزینی آن دشوار است.
این موشک های دوش پرتاب نمی‌توانند هواپیماهای بلندپرواز را تهدید کنند، اما پهپادها و بالگردهای آمریکایی را در ارتفاعات پایین در معرض خطر قرار می‌دهند. برای مثال، در آوریل ۲۰۲۶، یک موشک دوش پرتاب ایرانی به یک بالگرد HH-60W آمریکایی اصابت کرد. همچنین، یک A-10 و یک F/A-18 در ماموریت‌های کم‌ارتفاع آسیب دیدند.
این موشک‌ها، به دلیل سیار بودن و عدم نیاز به رادار، قادرند حمله‌های غافلگیرانه انجام دهند. آمریکا برای انجام ماموریت‌های ISR (اطلاعات، نظارت، شناسایی) و جستجوی نجات رزمی (CSAR) مجبور است در ارتفاعات پایین پرواز کند، که این امر آن‌ها را در معرض تهدید قرار می‌دهد.
در نتیجه، ایران با استفاده از این موشک‌ها می‌تواند هزینه‌های جنگ فرسایشی را برای آمریکا در ارتفاعات پایین افزایش دهد. اگرچه آمریکا آسمان ایران را کنترل می‌کند، اما ایران می‌تواند با تیم‌های پراکنده موشکی پدافندی، عملیات‌های آمریکایی را پیچیده و پرهزینه‌تر کند.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19681" target="_blank">📅 08:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19680">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">به عنوان بخشی از این توافق که بین کشورهای ساحلی ایران و عمان در حال مذاکره است، ترافیک ورودی از طریق یک مسیر شمالی واقع در آب‌های سرزمینی ایران وارد تنگه هرمز خواهد شد.
ترافیک خروجی از آب‌های عمان «با هماهنگی با ایران» (یعنی با مجوز صریح از نیروی دریایی سپاه پاسداران انقلاب اسلامی) خارج خواهد شد.
این توافق موقت به مدت ۶۰ روز طول خواهد کشید، در طی آن هیچ عوارض یا هزینه‌های دریایی دریافت نخواهد شد. در عرض ۳۰ روز، هر دو طرف تلاش می‌کنند مین‌ها را از مسیر میانی تنگه هرمز پاکسازی کنند و به یک حل و فصل دائمی نهایی دست یابند.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19680" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19679">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دونالد ترامپ
:
ضربه واقعی هنوز در راه است و امیدواریم مجبور به استفاده از آن نشویم.
آنها دوست ندارند این را بپذیرند، اما می‌دانید، کمی نگران‌کننده است. شما به مردم می‌گویید که ما مذاکرات خوبی داریم، و بعد کسی از ایران می‌آید و می‌گوید: "ما ملاقات نکرده‌ایم." این یک دروغ است. آنها می‌خواهند معامله کنند
سوال: اگر ایران دوباره عقب‌نشینی کند، آیا این پایان کار است؟
ترامپ: خب، اگر آنها دوباره عقب‌نشینی کنند، ضربه بسیار بسیار سختی خواهند خورد.
تنگه خیلی زود باز خواهد شد، یا خیلی محکم به آنها ضربه زده خواهد شد و تنگه باز خواهد شد. آنها با من تماس گرفتند و خیلی مودبانه گفتند: "لطفا، می‌توانیم صحبت کنیم؟"
سوال: چه زمانی می‌گویید دیگر بس است؟ و آیا راهی برای بازگشت ایران وجود دارد؟
ترامپ: من وقت زیادی دارم
ما کنترل کامل تنگه هرمز را در دست داریم.
روز خیلی خوبی بود. ایرانی‌ها دوست ندارند این را بگویند. آنها همیشه ادعا می‌کنند که ما در مورد آن بحث نکردیم. اما مردم فهمیده‌اند که این درست نیست.
اگر تنگه هرمز باز شود و به هر حال تا حدی باز است.
قیمت بنزین به ۲.۵۰ دلار در هر گالن کاهش می‌یابد.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19679" target="_blank">📅 07:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19678">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ:
گفت‌وگوهای بسیار خوبی با ایران داریم.
تنگه هرمز به‌زودی باز خواهد شد یا ایران هدف ضربه‌ای فوق‌العاده سنگین قرار می‌گیرد</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/19678" target="_blank">📅 07:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19677">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0pNVE90S-VFpRZYT53dlbf_EM4rHug7WOOLjp4AlyUjpXKZfSVEaXBp6v3w5RArDxvcJjVQRSWNcMYBzhscvtr7SQ1oUoiTbucuHOhnRJg9H3LZ3Ko3FsNaeZOrCRw0ee0Pn00eDM4jwt787PSKEncA7KPbymZoENiDZ2KptAOd1EZ79u8eZwiTvWWGBPzrzXal-w5BeJzSXRxRuru0bdQmEp__YyoaEgn2ZQnaGHS9QwwQhQWT6GxyKxokxb7HnDrrJIHYmtp5pOErMocbWmgwsRJB4JWyeMxGXGNtgRyigAyyBWADcdMW08cnnR4EEAAxGRVD2njB3orxblnlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژاپن پس از آنکه کشتی‌های جنگی چینی، به همراه یک کشتی روسی، در داخل منطقه‌ای که توکیو آن را منطقه اقتصادی انحصاری (EEZ) خود در نزدیکی جزیره اوکینوتوری می‌نامد، رزمایشی با گلوله‌های جنگی انجام دادند، به چین اعتراض کرد.  ژاپن اعلام کرد که این رزمایش طبق قوانین…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19677" target="_blank">📅 07:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19676">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ارتش ایالات متحده تقریباً ۸۰ درصد از پیشرفته‌ترین موشک‌های رهگیر THAAD خود را مصرف کرده است
سی‌ان‌ان</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19676" target="_blank">📅 04:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19675">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شب های خواهرمیانه !</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19675" target="_blank">📅 03:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19674">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حملات هوایی عربستان به صنعا</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19674" target="_blank">📅 03:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19673">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترور ناموفق ترامپ!</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19673" target="_blank">📅 02:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19672">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حملات هوایی عربستان به صنعا</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19672" target="_blank">📅 02:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19671">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سنتکام
:
مسیر جنوبی از تنگه هرمز همچنان برای تمام کشتی‌های تجاری که به دنبال عبور از این آبراه بین‌المللی هستند، آزاد و باز است.
در طول سه ماه گذشته، نیروهای ایالات متحده به بیش از ۱,۰۰۰ کشتی در عبور موفقیت‌آمیز از تنگه، علی‌رغم تهاجم بی‌دلیل ایران، کمک کرده‌اند و این عبورها امروز نیز ادامه دارند.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19671" target="_blank">📅 02:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19670">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzmXyfML24XWNkt3QVUYclmj11yrSejyUefryQ88rb-4rDTnENxXe9bml_LmquEdIC2SCDRYamf3OTdne6WYRpeNomBVCs3-p0CNPJr8kYxqygMU6m9Qgh87mG27RKlw2Ekn3YG-0aWv_dPt4l0eKQx7hyavxLcPKrwh2b2IrN_zRi8MJcmFmbS6_S-cTbxVVeH9ls1SkjmZSXZfB8tRwYscfwoLeG1C0XhP7ugQV-hEcDZx7dJeAXFGzjMUr8gpimwUZiRLNXLV6JgK8Jjh-NFzYnjIe6pxO_MWXN2lRETC_Y0-fMZTjxPTQtGcv_-Toedvca-pZ7-6VZQd-iHN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگه های مهم دریایی جهان و میزان نفت عبوری از آنها
ابتدا تنگه مالاکا و سپس هرمز.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19670" target="_blank">📅 01:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19669">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">روبیو، وزیر امور خارجه آمریکا: پیشرفت‌هایی در مذاکرات با ایران حاصل شده، اما هنوز توافق نهایی وجود ندارد.  روبیو گفت: «ما در مذاکراتی بین عمان و ایران در مورد بازگشایی تنگه هرمز برای تردد کشتی‌های تجاری شرکت داریم» و افزود: «امیدواریم این اتفاق به زودی رخ…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19669" target="_blank">📅 01:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19668">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2q_5IsxBlJ3T3d12TyZS9_QuiF70rhE8vzzKs0SXxtUlquwR7nNoABln7MNaWHclkHEMu7iA5-Rk3O-YvUz2a7FZ6aem3iGuvcGFsy2lEkK0n0iOCpKtiYkIYW23slWF94N7I6l_sWAbZIXD9WUV__S_RvhFWjut-rq9wYH4yTEwb36RAQoFOf_pTTKRMm0tCw08AaqL_-qEP8fOksKu40S-O3Yr_yz8d6i-UX2xSmbpYSE9yNv7xlVhS-D0DoF0Gb2xY_Hy6AmilU7d0GlKM7uGKWKaXaz0NvXlC8N9aMKJwhGmgbxwT1EaTKhz0INorNsIyDGu2KyW67ee1qiXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح بالایی است. پس از رشد مناسبی که طلا از کف دیروز داشته، توصیه می شود امروز با احتیاط برخورد بشود و بالای 4090 اگر برود قطعاً محدوده فروش است.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19668" target="_blank">📅 01:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19667">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlcZ-s0saBy71nm-DNcydRJSnfIRlXMksftAeoRVlxY2pW5Lgt72Obd4u1j2g8bVaoRksGe7UyPiLpnCL4-_SRxQCUof5lCdtsSVcUxSZf7KtpfP-PGYDoJPEVVGF2kZfktq67ntI3g6C0qeQgHYv1w-LyQ8opxxNlMR4fTApBw3psu9BdgQrSTLjyMmQsD25RwLT79ZbJINf3_74H_1NbQ-sJENpHm46hGbTF1FXshVxGJWWlTRtBGTkw7h1lehyn9qY-SjjSiLwNTrPKIEZJhGNnf8IS2kARe__A2G4F9YoDTuczblfLxIzXiNIhCUl1wzPNXAUcTRxTzts2PCkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
احیای بخش تولید آمریکا شتاب می‌گیرد  شاخص ISM تولید آمریکا در ژوئیه به ۵۵.۶ رسید و رشد همزمان تولید، سفارش‌های جدید، اشتغال و صادرات نشان داد که بخش صنعت پس از سال‌ها ضعف وارد مسیر احیا شده است. با وجود این بهبود، فشار هزینه‌های تولید، اختلالات زنجیره تأمین…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19667" target="_blank">📅 00:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19666">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ایران در حال بررسی طرحی برای بازگشایی تنگه هرمز از طریق ایجاد یک صندوق داوطلبانه است که توسط کشورهای خلیج فارس و کشورهای اروپایی که به این مسیر وابسته هستند، تأمین مالی می‌شود.  به جای اعمال عوارض رسمی، این صندوق هزینه‌های ناوبری، حفاظت از محیط زیست و خدمات…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19666" target="_blank">📅 23:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19665">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ایران در حال بررسی طرحی برای بازگشایی تنگه هرمز از طریق ایجاد یک صندوق داوطلبانه است که توسط کشورهای خلیج فارس و کشورهای اروپایی که به این مسیر وابسته هستند، تأمین مالی می‌شود.
به جای اعمال عوارض رسمی، این صندوق هزینه‌های ناوبری، حفاظت از محیط زیست و خدمات جستجو و نجات را پوشش خواهد داد، مشابه مدل موجود در تنگه مالاکا.
این پیشنهاد که به گفته منابع از عمان حمایت می‌شود، می‌تواند یک راهکار قانونی فراهم کند، زیرا قوانین بین‌المللی اجازه دریافت عوارض عبور اجباری در گلوگاه‌های کلیدی کشتیرانی را نمی‌دهند.
منبع: تلگراف</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19665" target="_blank">📅 23:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19664">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7wpS47fJYqJV94W_fgQdjRlcTgfws-U-ibpeRQLngylNbw5hrb2zxWT1VaoSgQL9yJfXDIkfL8XGLWbXV8yZ3QtTpEZBw55DOqyBM6q89zCoRK-aBUG0Sagp_on_kpmJjcEAV2ULtK2sw03oHPrtzgKopWRhBEzvJ6zOO1BVWGD8F6cJu9k6f9YYWFbVUajDpJCmBX8KzIiLqYfVmQUvhm5rLwmKM6C4b4trVxT0ceL7CI7XvhOuN9YwEWmQUxigzrvL7S8ExsKeuEU6V_nJ6iaV1r2yn7clwOCvgWa58JBI_jTNkELhHi01exGJB3MX0japuKjit9uqyO74F0P9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
سوپر اپلیکیشن بله بعنوان اولین لژیونر اپ های داخلی وارد اپ استور شد</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19664" target="_blank">📅 22:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19663">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ایران سیگنال داده است که مایل به بازگشایی تنگه هرمز است، اما در عین حال حق دریافت هزینه‌های عبور، تضمین‌های امنیتی در برابر حملات آینده، پایان محاصره دریایی ایالات متحده و تخفیف تحریم‌های نفتی ایالات متحده را مطالبه می‌کند.  منبع: WSJ</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19663" target="_blank">📅 22:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19662">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ایران سیگنال داده است که مایل به بازگشایی تنگه هرمز است، اما در عین حال حق دریافت هزینه‌های عبور، تضمین‌های امنیتی در برابر حملات آینده، پایان محاصره دریایی ایالات متحده و تخفیف تحریم‌های نفتی ایالات متحده را مطالبه می‌کند.  منبع: WSJ</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19662" target="_blank">📅 21:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19661">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">روبیو، وزیر امور خارجه آمریکا: پیشرفت‌هایی در مذاکرات با ایران حاصل شده، اما هنوز توافق نهایی وجود ندارد.  روبیو گفت: «ما در مذاکراتی بین عمان و ایران در مورد بازگشایی تنگه هرمز برای تردد کشتی‌های تجاری شرکت داریم» و افزود: «امیدواریم این اتفاق به زودی رخ…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19661" target="_blank">📅 21:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19660">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19660" target="_blank">📅 21:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19659">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سبحان الله!</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19659" target="_blank">📅 20:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19658">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEhJiQ5KRPdRcT3EvTqyHjGfH4cFZqEf76FEMOi-h7w1wBGeNl-wrZB_4v0vEyDM8XA4Ewzjx3rh511QKpME8fUPHqnEj_kwSCvbZi64O7v3gneZkx_OdzfYTF2Gk_mi3nKW1fCohbIytJ3xhfn4wvhKorsVJ_57FV8LVd1zyw2Y_4yd6nq7oLI5dA7FJ3MeYY-PdqsuuS0JtufNtSWhangL3rtU3fjCleNFOdMUJp4YXAWlvru6ZiB7UH5EzUf9p5KCdj9SG79zmGC0jUtWN87HPnK2k7qkwLmtlzbGZjQNq8BJxoaKR0EC5JSlAI60Ig55XOGra0QKEQNz6CIDGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  محسن رضایی: منتظر نفت ۱۵۰ دلاری طی روزهای آینده باشید.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19658" target="_blank">📅 20:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19657">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">روبیو، وزیر امور خارجه آمریکا: پیشرفت‌هایی در مذاکرات با ایران حاصل شده، اما هنوز توافق نهایی وجود ندارد.
روبیو گفت: «ما در مذاکراتی بین عمان و ایران در مورد بازگشایی تنگه هرمز برای تردد کشتی‌های تجاری شرکت داریم» و افزود: «امیدواریم این اتفاق به زودی رخ دهد.»</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19657" target="_blank">📅 20:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19656">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ایران در حال بررسی اجازه دادن به کشورهای اروپایی برای خنثی‌سازی مین‌ها در تنگه هرمز است، امتیازی که می‌تواند بخشی از یک توافق برای عادی‌سازی حمل‌ونقل دریایی در این مسیر و تسهیل مذاکرات صلح با ایالات متحده باشد.
ایران بارها به‌طور علنی اعلام کرده است که اجازه نخواهد داد کشورهای خارجی در تلاش‌های خنثی‌سازی مین در این مرکز حیاتی حمل‌ونقل نفت و گاز طبیعی مایع‌شده مشارکت کنند. با این حال، طبق گفته دیپلمات‌هایی که با این وضعیت آشنا هستند و به شرط ناشناس بودن درباره مسائل حساس صحبت کردند، تهران در جلسات خصوصی در هفته‌های اخیر موضع خود را تعدیل کرده است.
وزارت خارجه ایران بلافاصله به درخواستی برای اظهار نظر پاسخ نداد.|</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19656" target="_blank">📅 19:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19655">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">غرق شدن کشتی هندی در ساحل یمن  به‌گزارش برخی منابع یک کشتی هندی در فاصله ۱۳ مایلی جنوب حدیده، توسط نیروهای انصارالله مورد حمله قرار گرفته است. این حمله با استفاده از یک قایق انتحاری انجام شد و در نتیجه، کشتی غرق شد.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19655" target="_blank">📅 18:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19654">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حتی وقتی کشتی طوری ش نمی‌شود، هندی ها تلفات می‌دهند</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19654" target="_blank">📅 18:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19653">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">العربیه : تا ساعات آینده بیانیه بازگشایی تنگه هرمز، رفع محاصره و از سر گیری مذاکرات اعلام می‌شود</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19653" target="_blank">📅 18:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19652">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">323.7 KB</div>
</div>
<a href="https://t.me/SBoxxx/19652" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 18</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19652" target="_blank">📅 16:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19651">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 18</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19651" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 18
سه شنبه 4 آگوست 2026</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19651" target="_blank">📅 15:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19650">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گروه حوثی‌های یمن اعلام کرده‌اند که یک حمله دقیق با استفاده از پهپاد علیه یک "هدف حساس" در فرودگاه نجران در عربستان سعودی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19650" target="_blank">📅 14:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19648">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vxcc_G3GumBG1SIdA619vaA39VCO_xNbdshWu3azZkk2uiN78Wht-z4H0lpaUWdY_1hTFEluagM5iJnpuayCWcGxMlRyGbMQc553y85PBqI7PjChx15wYGqx7mr-a2X0Qc86Js1UPRUOzL4Obv5mUfV9rViNd8ddMVmv6WTNYRWyX5Yd3q9EEpfU_GAq8UeavanRAD1JI2Txf22l-tTFp68vnw-ysOmSdwMyHQNiJGLnEIzVo8Vucwp4BAV2ARSsl--e-IEWpi0TcAmKB_bYulJ6PuJAGHxzP_kC9lPoD4EeDNnkbyCRd_8EUqKoXQLACaW7Mpn-Hl_6Wvl801tG0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gbx82FM67UkH66bqZpfDi9KqRFhzij-y_FU2A117lWrltlbUr0Cx5d9RNDRaSU63XLupZGcgVwRMFAnKC1UR8puxqpFQLyqUtzkhRpbYxLQWXbJk-1OsqfTg4v9DDNE_5RJ6iI2wLbxmma5Ka3XXb_ZwrkuwPkGmqKcrNLL4wij1RB6RW3TrGz9wE1B-NAIKqy9yUWMWiCyVkrWwA-tK7LvAbGp8FsFdAJPCoAzIvofkcw37DbCCjsRyow564m9hkvPv2nmH0LfgUGJrEbkcrGQ9t0OpfrmZg5j9RKZJqJggF7cK_-sL91DjA16GimjADo6UMqVgCrEosDbH-nmTow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بهره‌برداری از آسیب‌پذیری‌های داخلی آمریکا
محاسبات ایران تا حد زیادی انتخابات میان‌دوره‌ای آمریکا را نیز در نظر گرفته است. تهران بر این باور است که دونالد ترامپ، رئیس‌جمهور آمریکا، در شرایط افزایش قیمت سوخت و کاهش حمایت عمومی، تمایل چندانی به ادامه دادن یک جنگ نامحدود ندارد.
این درگیری شش‌ماهه تاکنون به کشته شدن ۱۸ نظامی آمریکایی از ماه فوریه منجر شده و فشار نمایندگان جمهوری‌خواه در کنگره برای ارائه یک راهبرد روشن جهت خروج از جنگ را افزایش داده است</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19648" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19647">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEoli0ZrFi_6Y7EEJyvwLd4cl78wiIYpK_I3u7z3qrlQpKtnSx9V57Lp9kBqum3kpZbQfNHZV1Yk8lzprP4fwY-rtHam5y0SmY96j8mtYKJHzVv7ZiEKusQzVWQTopYm3j971veHUdevP72EkaPa6JWUO971czfq81qIl7hQj6W3msrkwecmJBWBFaqA71Edozknrv-_PzV2lM5c1PRXeUjxzI8isjp-mYHxlANbW0VSaZ6P9CobDLL7w0hM3e07Vkxsg6NOtEWG7TuaHwOWYUs4_QzLK8KPPzUgf5hQVfuYVQUpPPKOCDT697Jokn-9sG_xUZAcVJM6ZgHX_Ept7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشتی به قلم « احمد کوچاک»
ایران روی اخلال اقتصادی برای وادار کردن آمریکا به امتیازدهی حساب باز کرده است
ایران در حال اجرای یک راهبرد فرسایشی حساب‌شده در سراسر خاورمیانه است و با استفاده از مسیرهای کشتیرانی جهانی و زیرساخت‌های انرژی به‌عنوان ابزار فشار، تلاش می‌کند اراده واشنگتن را فرسوده کند. تهران بر این باور است که افزایش هزینه‌های اقتصادی در نهایت آمریکا را به دادن امتیازاتی درباره کنترل تنگه هرمز وادار خواهد کرد.
تهران در حال اجرای یک کارزار فرسایشی حساب‌شده علیه ایالات متحده است و کریدورهای تجاری و شبکه‌های انرژی خاورمیانه را به نقاط اصلی اعمال فشار تبدیل کرده است. این راهبرد از رویارویی مستقیم نظامی پرهیز می‌کند و در عوض بر افزایش هزینه‌های اقتصادی و لجستیکی ادامه این تقابل متمرکز است.
رهبران ایران بر این باورند که می‌توانند واشنگتن را پشت سر بگذارند؛ به این معنا که هزینه حفاظت از کشتیرانی بین‌المللی برای آمریکا و متحدانش را آن‌قدر افزایش دهند که در نهایت پذیرش خواسته‌های دیپلماتیک تهران برای واشنگتن کم‌هزینه‌تر از ادامه وضعیت موجود باشد.
گسترش نقشه تهدید
عملیات ایران دیگر به تنگه هرمز محدود نمانده و میزان تحمل آمریکا در برابر اختلال در چندین گلوگاه دریایی را هم‌زمان آزمایش می‌کند. اکنون تهدیدها دریای سرخ، تنگه باب‌المندب و زیرساخت‌های انرژی عربستان سعودی را نیز دربر گرفته‌اند.
این پراکندگی جغرافیایی، نیروهای دریایی بین‌المللی را وادار می‌کند مأموریت‌های اسکورت و حفاظت دفاعی بیشتری انجام دهند؛ اقدامی که منابع غرب را فرسوده می‌کند، بدون آنکه الزاماً توازن نظامی منطقه را تغییر دهد.
مایکل نایتس از مؤسسه واشنگتن می‌گوید:
«ایران از همان ابتدا تلاش کرده است با گسترش گزینه‌های تشدید تنش خود، آمریکا را در این زمینه پشت سر بگذارد؛ به‌گونه‌ای که همیشه بتواند هر هفته چیز جدیدی ارائه کند: جغرافیای جدید، نوع جدیدی از سلاح یا نوع جدیدی از هدف.»
بهره‌برداری از آسیب‌پذیری‌های داخلی آمریکا
محاسبات ایران تا حد زیادی انتخابات میان‌دوره‌ای آمریکا را نیز در نظر گرفته است. تهران بر این باور است که دونالد ترامپ، رئیس‌جمهور آمریکا، در شرایط افزایش قیمت سوخت و کاهش حمایت عمومی، تمایل چندانی به ادامه دادن یک جنگ نامحدود ندارد.
این درگیری شش‌ماهه تاکنون به کشته شدن ۱۸ نظامی آمریکایی از ماه فوریه منجر شده و فشار نمایندگان جمهوری‌خواه در کنگره برای ارائه یک راهبرد روشن جهت خروج از جنگ را افزایش داده است.
چرخش به سمت دیپلماسی
واشنگتن در حال حاضر برخی عملیات تهاجمی برنامه‌ریزی‌شده خود را متوقف کرده و به دنبال امکان آغاز مذاکرات با میانجیگری عمان است. این تغییر رویکرد پس از رایزنی‌های فوری با متحدان منطقه‌ای، به‌ویژه عربستان سعودی، صورت گرفته است؛ متحدانی که خواستار کاهش تنش برای حفاظت از دارایی‌های آسیب‌پذیر انرژی در خلیج فارس شده‌اند.
دولت آمریکا در این توقف تاکتیکی، دولت اسرائیل را نیز به شکل محسوسی در حاشیه قرار داده و ثبات در خلیج فارس را در اولویت قرار داده است.
با وجود گشایش دیپلماتیک، اختلاف اصلی بر سر تنگه هرمز همچنان حل‌نشده باقی مانده است. آمریکا خواستار آن است که این آبراه به‌عنوان یک مسیر بین‌المللی باز باقی بماند، در حالی که ایران بر حاکمیت مدیریتی خود و حق دریافت عوارض عبور تأکید دارد. اما تهران حاضر نیست از موضع ضعف وارد مذاکره شود و با استفاده از تهدید به گسترش اختلال اقتصادی تلاش می‌کند برای خود اهرم فشار ایجاد کند.
ری تاکیه، مشاور پیشین وزارت خارجه آمریکا، می‌گوید:
«اگر قرار باشد مذاکره‌ای انجام شود، ایران شرایط آن را تعیین خواهد کرد.»
در نهایت، رویارویی کنونی بیش از آنکه صرفاً یک تقابل نظامی باشد، آزمونی برای تاب‌آوری نهادی دو طرف است. ایران بر این باور است که ساختار داخلی آن می‌تواند تحریم‌های طولانی‌مدت را برای مدت بیشتری تحمل کند تا ائتلاف تحت رهبری آمریکا بتواند نوسان دائمی در تجارت جهانی و بازارهای انرژی را تحمل کند.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19647" target="_blank">📅 13:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19646">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارش‌ها از شنیده شدن صدای انفجاری در شهر صنعتی شمس‌آباد، واقع در جنوب تهران، خبر می‌دهند.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/19646" target="_blank">📅 13:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19645">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPaSfEysv8arZLJhbdCpjHmNeU3eL1qp7etqJE75wpTz5vt3RYXVad-pkGqAzcnXCuhijt-nKU951BMlvy42AyguUKt79TIYdCJ6vTeJsBbr1uieRHascUChh8GXsAgTUe-FqKVZqwnbAEOeiKaDkFkBIaczI2TvS0t7M0Bm1pS2tsD2K99_Ov20_aLK2EaUfULUAT35ERgzczP2Ct4Mtk3pV6urLACej53BbKSbiD10z6ptrGmWIZHUZ3uIw6ler8n8G5VfizVSUVKrQNpc8qpzIoQ8Cg8E1aByb5o-9-sxqK_us80oERsvuNsduN1umQd0MuIUeVeGjtUlWRMVxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در حال احیای صنعت آمریکا است و این مسئله در گزارش درخشان دیروز PMI کارخانه ای آمریکا بازتاب یافت.  یادداشتی در این خصوص منتشر خواهدشد.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19645" target="_blank">📅 13:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19644">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3M0_nCAlfuoFYbDtcvGM8Y8imKJezhKAJEQzsHdMH3DVJoXNuExzKJ4RaCmXYHhX_XKo4OvOOf5eJtiTHScBmXW7qh8kh1BEPY4agDvgXXGNyF8d1CYav8mLPGGGZrXJ8hxtJi0cGvmztzlgcuSNTLryaX_RkLK4anBskoDc40jUR09Mx6knHKrx06x6TZm0z6gJJ4B8WtjrbiComjqMINFySnr3zvAKJ-N6XwIU2nWrCIXmj0o0V0u-VBP5UKZN_IBTJ8Vf7GZybAHyGXeC_uBn9y2QHGY6XVkThFJJ7UYRJk3E9Vo_ej7ilUhkFQ3KlG3kZgjazYTGzyIu6GEMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Geomarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19644" target="_blank">📅 11:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19643">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azNFptcWnpPJwo9Pd4UJuO7IcGHNkPiuftUB71ng9qbGklK4oiiebJmJBn044v9aMg2Ie2-cjq3uIlgWNP1DrpY2VyvsfD5E_TqRohUOiKQQPZp4PH7r0s5P5_ebnSOlrmpFPr5nfQAcVv6K_ZSepyT9DZdUz0br-sqgZTHGG35i992HKpKXyLIuZ9z12FLTumzDfzM5wIqM8C-_WuLTrubjlUnw3vwppe80fnNR0ZfsVj3QY_ZS-EKqqayDKLxzoYwXCdC9ifDJk03nfDqdZAQvu2HE08ufz1p2PklFBRUc8cNNh5BQOwvvkagjwJSbNxuZPS2-nQGkUTtP7S6v8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح بالایی است. پس از رشد مناسبی که طلا از کف دیروز داشته، توصیه می شود امروز با احتیاط برخورد بشود و بالای 4090 اگر برود قطعاً محدوده فروش است.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19643" target="_blank">📅 11:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19642">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRaoqQ_Z8pq_QTMjZ5-v3uMnIKj2qsFCDWIOlVgqQq1aGIIQrhPaibvOGI1PPVPl-oeNcQvbFfsmFdD-yKoC08FPzMPbFR4Or_QaRvZX4Ql77OWdEZUfihBWZBWXAomSbuh5YcNQ4NM_KY_wdIKX_N0n1TkBhHHtczZsn7yyrJkICP6WGJSG2ZN-T_uJjJM-MJX4NIPI-wHOWQs5wGxbZuHAuJtFTwPd-x4AEEcHzl0JS8Dq8A-giLiqTjTSN5T4RRz_qtk8Iw0F6n7yk_RSdl9Vcm83ihotZYzDQhEtvrM_1jtsQbYmuT-6w8TWzUEiWkVJS46-_jyJ80EG4heOWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
آیا بخش تولیدی اقتصاد آمریکا در دوران ترامپ احیا شده است؟   داده‌های اخیر PMI نشان از رونق و رشد چشمگیر بخش تولیدی آمریکا در اوایل ۲۰۲۶ دارد که می‌تواند ناشی از سیاست‌های حمایتی و استراتژیک دولت ترامپ باشد.  با این حال، این بهبود به دلیل کاهش اشتغال و تغییر…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19642" target="_blank">📅 10:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19641">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ایران و عمان به توافقی نزدیک شده‌اند تا پس از ماه‌ها اختلال، مجدداً تردد کشتی‌ها را از تنگه هرمز از سر بگیرند.
مهم‌ترین مسئله مورد اختلاف این است که این توافق پیشنهادی می‌تواند به ایران نفوذ بیشتری بر این آبراه بدهد.
مقامات ایرانی می‌گویند که کشتی‌هایی که وارد خلیج فارس می‌شوند، از یک مسیر نزدیک به ایران عبور خواهند کرد و هزینه‌ای را پرداخت می‌کنند که بین ایران و عمان تقسیم می‌شود. در مقابل، مقامات آمریکایی این ادعا را رد می‌کنند و می‌گویند که ایران هیچ اختیاری برای دریافت هزینه یا کنترل تردد نخواهد داشت.
منبع: نیویورک تایمز</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/19641" target="_blank">📅 10:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19640">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moQwjUPWoKpv6S0MXx3CvJFEEorfOqaB7YWL2SVsVWhYQGWnjRDWyJ7Q7jUckBpXvMqNdqpmC6vy2SfOSReM_WCxE9jxVkNRiuPYoAlSQaCyKH32XhXy9d_qAq-Ruc0_6aS0d0XmgfrlyoaG4sHVelNE1jsq9S_1MMvqQsetyegE-ZLW0stFS6qRTZ4jt7ydthG_h9EvC-i_RPir4EZk4fPoFNFvTPTZww38GTLflQTEwtBJcp2LojXVII5m-5cOuT14jHSbWNG9R9sHAyMoH3PIfMHk_RDHtOso-aI5fzefzTwxaP6kPhQXr7Za817ARRD_cfg6fjVXBllLRXV0oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار پایینی قرار دارد و پیش بینی می شود که طلا رشد مناسبی (دستکم در حد 400 پیپ) را تجربه کند.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/19640" target="_blank">📅 00:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19639">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">#USOIL — H2  محسن رضایی: منتظر نفت ۱۵۰ دلاری طی روزهای آینده باشید.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/19639" target="_blank">📅 00:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19638">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSG13osgoYYk9NrfLHlj6q4Vodi8fSbpeaAuI_7r11vmpzDQ-szgVRGCxo_h_FGg5fNhSTZQvQX-Cj8-JrZ6VnmRCjYoB-puNfMqpqOpJ6kdDyxpp6rUBAwIpmw6m6CunBim8PfpZnO9jXXXqz4rMKZmF9zyZRK9cEOuR2uEJ6EQI-Rn7Sxr-mVefV2BlOfb6iswIkaeO6_wqWJbGnx4yvnPGBE-94Z1pDPsRmeHcwz42dOjO1pIhJbcs5ed6iwF_1PQ5qKiMAxT2qjVRs5vD1uQb59MyIvdWIvqRK7eENDif1IjwPmq5nfL7vpDcXq-9b3N8QBu_zEkeFfCARCpgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  به نظر تارگت 2 را می شود دستکم 120 درنظر گرفت.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/19638" target="_blank">📅 00:31 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
