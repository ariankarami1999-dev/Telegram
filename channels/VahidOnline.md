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
<img src="https://cdn1.telesco.pe/file/Dzd8VasrnjP1hZuJgZSIcmnGe1yna9UPLkpnz5CGjM1pmCCHV2QnvtKmUpXjGDh-lmvrOtG0DMZrArsb45zpKLXvCZ_pXqk5EDqY0PpqT4LgjjOmNExI8VBjUHacG3ywU_02_vxVsyqiW_FvdZ3Lzh4aNQwIrTp-yQlHgoo3qrBuDibHhRcVTBwS3QH5DWTELEnI3CZK6RyQrEiLVGMrI51iB7x59UjzboB7DRQe3J6rnm42MZxlGUdwXHsKxZc4-eiNOVD33Og81E1UwOsN4K77mFaavl-91gQnTSJjDdyQ99qJk5vddYrLfQXZ1t3UTnJvF1A2alQ41dpxrRqwAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.34M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 01:19:51</div>
<hr>

<div class="tg-post" id="msg-76811">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gKpaXn-yK3Xd2HKBDe1kQDC_hdcfZbKXxXzIY1Hplb-H-dDLhNBpxC0_dICQRQMdaw_aY9SL_wtYeUUS21Ghi53Ain_7_qRgh1Fc7IR-wHr8WYA_5W-VO-5Zy-sCoXGBSRfY_5XYw8ClqiGfx96Ll9aRrhu1JLmkhKAxRoz_QtGmZZ63GQAi1VNaOox7bnRbfHWUfH0ZM1tkW_EqNLTqFUCmI6tztcfLhsXj_1-ZlrzvFKgYBb9PJhF9ycan40OXX_BE_puq3ga9mjjVl5Tk8ynWwzWEyb91x-ykD-iiIUBsnH7e34-lELtNT2tEeaypKaTLCowe9o9to3jb4RUMDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی این که آمریکا اجازه نمی‌ده نفت بفروشند رو نقض تفاهم‌نامه خونده.
پیش‌تر آمریکا هم
گفته بود
چون به کشتی‌ها حمله کردند، لیاقت اجازه‌ای که به صورت موقت بهشون داده بودیم رو ندارند تا رفتار مناسبی مطابق تفاهم‌نامه نشون بدن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/VahidOnline/76811" target="_blank">📅 01:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76810">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sho7ptQ-4aUbCrZcYk7Di0bkyat1uZ7aDzlQt5JT5BBSGIXbXQ-0cAhMBsIjAsCPHaSzL0wnKXGg3kpQZu6e8n1o4wBH_Hzsii7pnBrnPiBVVnE4UX-ItEIuoSPJjt69YRbbSgHK3D0aFjcSCpgxxuTSIhjxSZHqSJYny234yTO1g4Fix27Ae9TsgvLcXaE8IQiKaKGHJOO3RF0CTFoVf22GFWAL9I7XYQfVQNgGNytQHiGbSHKvaczRgxwTl-_M1BADM-V1cFqs0D1kCnYP-q21qBj911wkT7DZJGJRPATrkz_BKH2-b9gf_uMgNIIt8BwBpO1XUTVmbjKcgVLhvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای فرماندهی مرکزی ایالات متحده آغاز به اجرای سلسله‌ای از حملات قدرتمند علیه ایران کرده‌اند تا به‌خاطر هدف قرار دادن و حمله به کشتی‌های تجاری با خدمه‌ای از غیرنظامیان بی‌گناه در یک آبراه بین‌المللی، هزینه‌های سنگینی تحمیل کنند. حملات آمریکا در پاسخ به حملات ایران به سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند. تجاوز آشکار ایران بی‌دلیل، خطرناک و نقض روشن آتش‌بس بود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/VahidOnline/76810" target="_blank">📅 00:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76809">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پیام‌های دریافتی تاییدنشده:
سیریک، صدای چندین انفجار پیاپی.
جزیره هنگام الان صدای چندتا انفجار بزرگ اومد تعدادش ۱۰ تا بیشتر بود
صدای انفجار درگهان (جزیره قشم) میاد ولی صداش کمه انگار دوره به اینجا
سلام وحید جان بندرعباس صدای انفجار
قشم صدای چندین انفجار اومد
نفهمیدیم از کجاست
قبلش صدایی شبیه صدای هواپیما میومد
صدای دو انفجار ۱۲:۳۵ بندرعباس
سلام وحید جان
ساعت ۰۰:۳۲
ما روستای سوزا تو قشم هستیم
اول صدای جنگنده اومد
و بعدم صدای ۵-۶ تا انفجار اومد.
سلام ساعت 12:35 بندرعباس صدای انفجار اومد 4 تا.
سلام کشتی سازی بندرعباس خیلی صدا وحشتناک اومد
سلام بندرعباس ۴ تا صدای انفجار تا الان
آپدیت:
صدا و سیما:
شنیده شدن ۶ انفجار در روستایی حوالی شهرستان قشم
دقایقی پیش صدای ۷ انفجار در محدوده روستای طاهرویی شهرستان سیریک شنیده شد.
فارس:
دقایقی پیش مردم در حوالی سیریک و قشم صدای چند انفجار شنیدند.
هنوز محل دقیق و منشأ این انفجارها مشخص نیست.
🔄
آپدیت:
بندرعباس ۴ تا انفجار دیگه
دوباره ۴تا تا الان
شد ۸ تا ۹ تا ۱۰ تا
من مرکز شهرم خیلی بده
سلام وحید جان
ساعت 12.30 صدای 5 انفجار شدید ذوالفقار قشم شیب‌دراز  نزدیک جزیره هنگام
سمت پایگاه هوایی بندرعباس انفجار شدید همین الان
وحید جان سلام همین الان ساعت ۱۲:۴۷ بندرعباس چندین صدای انفجار پشت سر هم اومد لرزید
الان بندر عباس سه چهارتا انفجار بزرگ
درود بندرعباس ۱۲:۴۵ چندین انفجار پشت سر هم
همین الان کلی صدای انفجار اومد بندرعباس 00:48
سلام خوبی، همین الان بندرعباس صدای ۳ تا انفجار قوی اومد ساعت ۰:۴۵
بندرعباس چندین‌تا صدای انفجار پشت سر هم اومد
00/48 قشم پنج شش تا انفجار قوی
00.48 بندرعباس چند صدای انفجار پیاپی
🔄
صدای انفجار پشت سرهم بندرعباس 12:50
هنوز ادامه داره
یک سر دارن میزنن ۰۰:۵۰
مجموعا بالای ۱۵ انفجار
۰۰:۵۰ صدای ۹ انفجار دیگه هم با صدای شدید از سمت پایگاه هوایی داره میاد
بندرعباس ساعت.همین الان چند تا صدای انفجار پشت سرهم اومد۴۸دقیقه بامداد چهارشنبه۱۷تیر
سلام همین الان صدای انفجار پیاپی و نور نارنجی بندرعباس
بندرعباس رو همچنان دارن میزنن
👀
صدای انفجار و پدافند پی در پی بندرعباس همچنان ادامه داره
همین الان بندرعباس
صدای انفجارهای شدید، پنج تا شش انفجار
کشتی سازی بندرعباس، اطراف بستانو رو زدن
سلام صدای انفجار بندرعباس بیشتر سمت اسکله ساعت۱۲:۵۰چهار صدا سمت شرق اینجا صدا نمیاد سمت غرب بندر اینجا صدا میادسمت اسکله
🔄
ساعت 12:57 انفجار دوباره بندرعباس
بندرعباس ۱۲:۵۸ همین الان صدای خیلیییییی شدیدی اومد
خیلی تو شهر بود انگار
اقا وحید بندرعباس یجوری زد شهر لرزید
پیا پی اسکله باهنر داره میزنه پشت سر هم صدا میاد
ساعت 57 : 0 صدای شدید انفجار در بندرعباس
00:58 دو تا سنگین تر زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/VahidOnline/76809" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76808">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F8FZKJX6_47O6zwHPWQ2G2YLBzsnuFvXvqAmswyHqX9I6vI_0w1cO0FMJqLblHphl1qGNCTvpXxNqdeX654NiaWDaVJCDiQQ-QwbTThKwxy89b3fDs9oMYRjeLiv6J-IBOYumniwLxk65I7t5dcR6cPjk0kYguhtLSfS_EYJ_G84k1bHjAtzdtxo3fd-zoXUGOcNZERJeRSA8_QvQ9I0rUhoRWxCeMKvvS1EWMKU9oCe7ZyIsE9x5R1NYeiNYRC0hV0xOCbCg-ZOms-dpA2pfm1vjCqPM37mlPqwiEr9JDAjHVjqTGIT39XV4v5_6GkW7ViPSyghIjeF4qXv_bOoJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا معافیتی را که به‌طور موقت تحریم‌های نفتی علیه ایران را تعلیق کرده بود، لغو کرد و اقدامات جمهوری اسلامی ایران در تنگه هرمز را «کاملاً غیرقابل قبول» خواند.
یک مقام آمریکایی به خبرگزاری فرانسه گفت: «اقدامات ایران در تنگه هرمز برای ایالات متحده کاملا غیرقابل قبول بود و با عواقبی روبه‌رو خواهد شد.»
این مقام آمریکایی گفت تفاهم‌نامه واشنگتن و تهران «کاملا مبتنی بر عملکرد طرف‌ها است» و هشدار داد که ایران تنها در صورتی از مزایا برخوردار خواهد شد که «رفتار مناسبی» نشان دهد.
مجوز معافیت از تحریم‌ها که حدود سه هفته پیش اعلام شده بود، در ابتدا به جمهوری اسلامی ایران اجازه می‌داد به مدت دو ماه نفت خام و محصولات نفتی و پتروشیمی را صادر کند، تحویل مشتریان دهد و درآمد حاصل از آن را به صورت ارزی از راه بانک مرکزی وارد ایران کند.
اقدام آمریکا پس از آن صورت گرفت که بنا بر اعلام ناظران دریایی و دولت قطر و عربستان، در فاصله چند ساعت سه نفتکش، از جمله یک کشتی حمل گاز طبیعی مایع (ال‌ان‌جی) متعلق به قطر، در تنگه هرمز هدف حمله قرار گرفتند.
@
VahidHeadline
وزارت خزانه‌داری آمریکا مجوزی را که ۳۱ خرداد برای تولید، تحویل و فروش نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران صادر کرده بود، لغو و از روز سه‌شنبه مجوز عمومی جدیدی را جایگزین آن کرد.
وزارت خزانه‌داری آمریکا اعلام کرد مجوز عمومی X به طور کامل لغو شده و مجوز عمومی X1 جایگزین آن شده است.
بر اساس مجوز جدید، شرکت‌ها تا ۲۶ تیرماه فرصت دارند معاملات مجاز بر اساس معافیت ۳۱ خرداد را خاتمه دهند، اما
از ۱۶ تیر خرید جدید یا بارگیری نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران ممنوع است.
اوفک همچنین اعلام کرد هرگونه پرداخت به اشخاص یا نهادهای تحریم‌شده باید به حسابی مسدود و دارای سود در ایالات متحده واریز شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 198K · <a href="https://t.me/VahidOnline/76808" target="_blank">📅 22:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76807">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga2W_Nt1OD6B8m-2C5Q9C_03RITn4Kh84mZ6Bj4Ewdb5e9gUEmUs3wfx-Wr-Io9d6oU6LfJwgf63uJLh1_S9C4U-tRwGViynvFOT8UZS9yeuTpfQG31gF2di8_F4NvidbNfSEiDwh0uDIK4g8fug_JIaoUAC_7PtYcxqUs6i2CEieclMz6rnFr8yegHlKiguxW-bzlMSx8zlV6ccA4JI2CHadHbgQDsvRDHFumdAeto2ZnoPzxHE38Xq_jnZBGTdbjF4qJxNCFfaCNDkawk-mNYdT6L61935fDV7M572o5-rX_Z2Bkp3goooLvuaSAebPL14OfimTzq04Nx3k_5bUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت قطر اعلام کرده است که در پی هدف قرار گرفتن نفتکش قطری در هنگام عبور از نزدیکی تنگه هرمز، کاردار ایران را به وزارت خارجه احضار کرده است.
در بیانیه وزارت خارجه قطر آمده است که این کشور حمله به کشتی خود را به‌شدت محکوم و آن را «نقض جدی ایمنی کشتیرانی بین‌المللی، تهدیدی مستقیم علیه امنیت عرضه جهانی انرژی و تخلف آشکار و صریح از قواعد حقوق بین‌الملل» می‌داند.
اعتراض قطر به ایران در قالب یادداشت اعتراض رسمی به محسن محمد قانع، کاردار سفارت ایران در دوحه و در محل وزارت خارجه قطر به او تحویل داده شده است.
وزارت خارجه قطر اعلام کرده که در این یادداشت از ایران خواسته است درباره این هدف‌گیری توضیحات فوری ارائه کند، اقدامات لازم برای جلوگیری از تکرار چنین حوادثی را بلافاصله انجام دهد و به‌طور کامل به قواعد مرتبط حقوق بین‌الملل پایبند باشد.
قطر همچنین اعلام کرد که این کشور تمامی حقوق خود را برای اتخاذ هرگونه تدبیر مناسب، مطابق با حقوق بین‌الملل، به‌منظور حفاظت از منافع و توانمندی‌های خود محفوظ می‌داند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/76807" target="_blank">📅 22:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76806">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTc7PTBk5DGCtWo2mOBE6NF0znaq0lRXjwF2PEBVmg-MLqHZ8orNSz7tyhdZQjUxmgssM7e12NmjnQJR2MTCChmC-b0qAwnjCA0CPm7B-Q2j8oKMvkj8j0rXv0jibOY81g7ldDuDLyVZgLn1rhPoTHR3aG5ByTAt9za9JiebfucZaCspzTiYF7hgmAvRx2jnvmxoazGXn2AyArfsK-yEFJaqM84gdRmi87ySddS0FsP7RMOo1TK01cUXBty7aJFww980q013K_tO9iMSC-GZGPa29pQcw4m3cNaG1jL-iXvmd6LkeeMDCBkEbYnDxYg5vhgAxrPHGmKW4RY0E9sNyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی، نماینده مجلس جمهوری اسلامی، در شبکه اجتماعی «ویراستی» نوشت: حالا که دونالد ترامپ در تیررس ماست و برای اجلاس ناتو به ترکیه آمده است، رسما و بدون تعارف، محل استقرار او را در ترکیه با موشک هدف بگیریم.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/VahidOnline/76806" target="_blank">📅 22:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76805">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oP6G5SD-zxAY6y0btqKsS-x8lMgxq0jix3Lv-VywtFii7AeXvjkRf8pZuOM3D_AcTn_zDCo99UWpIfZwdj1N4XcTHW0Kgam8cx0ehdcrIck0bi8lvYCydH2QqR_6Am214G51hdSQVpngU0vwVc8nT6mcYegL4-F2XeuTG1DDf82NeOBnbtg5E9z7ZUC1X3qoHDS8xQ8Jg1VsYIl4iiFexBeJi3iK_ac_KVKmnIq142Qo0gFbRcKqUWGPSVSiOUeZhFpUZNgcW6Tcq5mt7E492T3k1ZMmI05n_Oxe7qNRfo_irhpvbnpRVimf5Y8LC8raqML_tUsO-4V-SuFBEwO6Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر اسرائیل روز سه‌شنبه ۱۶ تیرماه در گفت‌وگو با شبکه سی‌ان‌ان گفت که با وجود اختلاف‌نظرهای گاه‌به‌گاه با دونالد ترامپ، رئیس‌جمهور آمریکا، درباره ایران، آن‌ها در مسائل کلان مربوط به نحوهٔ برخورد با تهران «هم‌نظر» هستند.
بنیامین نتانیاهو افزود که هنوز زود است درباره آنچه پس از امضای یک توافق صلح موقت میان واشینگتن و تهران رخ خواهد داد، اظهار نظر کرد.
او اظهار داشت: «رئیس‌جمهور معتقد است که می‌تواند برنامه هسته‌ای ایران را متوقف کند»، اما افزود که در این باره تردیدهایی دارد.
نخست‌وزیر اسرائیل می‌گوید: «در مسائل بزرگ هم‌نظر هستیم و گاهی هم اختلاف داریم، اما متحدان واقعی هستیم».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/76805" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76804">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lHH_LFvhuX52GYn3bbM0E-7gd05DtjF-A4fF9DI6UtrCR9OwdpSJ98V4n6LBC2lnI_RozbwCj1UakXs2vjPZfzW1DA0i68yslmlj8Lh3bgdaJkVpjWKy-laHNVAxp1pmgtAw8-D0CnBbdtfHUudh3WckyQf21Ir1nkQZEx63hSTCZAM_H-rVMdRanxQ6HU1OoEw08cpJC3CaInJV6GEez2OAr3nZSfRuJPMwNHoxgcN5nGSHQFmefimCrvyqzvOV_9ozzz-u9CLXiRP9Q8a5Fj87KU9tEKIDN92K0YVEuHP42sNz2MoEoEoDSQrMjXsLJKiaXXDDXcll5LrDvyeiLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی، روز سه‌شنبه ۱۶ تیرماه، به ان‌بی‌سی نیوز گفت حملات جمهوری اسلامی ایران در ۱۲ ساعت گذشته «تهاجمی» بوده و «نقض مستقیم یادداشت تفاهم» به شمار می‌رود.
به گفته این مقام، ارتش آمریکا امروز چندین پهپاد شلیک‌شده از سوی ایران را سرنگون کرده است. او همچنین با اشاره به حملات شب گذشته به دو نفتکش در محدوده تنگه هرمز، گفت که جمهوری اسلامی در این حملات از دو موشک کوتاه‌برد استفاده کرده است.
این مقام آمریکایی جزئیات بیشتری درباره محل وقوع این حملات یا میزان خسارت احتمالی بیان نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 198K · <a href="https://t.me/VahidOnline/76804" target="_blank">📅 20:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76802">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RYTUZqYHmmqPeZQzT4Ggu2OK-9-z54pMB2Se_WjFEye_qyNLlSeS3XkpJf0R_SZNxkRiAxF-fmX5b2iC5IB2PkGal7bzXU6Zd8EDWU8_PzYWGiPwwFx5RU_ylMuTy3fM5k8I73TSv8b2A6uE9Itu0qxU4hJ1L42XWaQwJwSS3J3xwErXU_HVAUsuY3lbcNUXR_3M1aPTk3GayZhZ_L0jVqrOm_YI09rpmfyzY2MiuI_0jwddTdIYt8rXDN7mx_3f5xezScCsIz3Kv0S-D1QOiQPMrJcrbjI9dzlVrsje1GG9dMnEiLlMu_tkPEd3GlLYBqj6fcm7UcvQDUjsfXdxig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3c7d37bab.mp4?token=lIZP-hqpGFBIf6LeQlAzEqWUTsAJ78_Zrc3cE6JYrK7wncydHy8Qc12jYp-_2soKkUHFkCoCffp7xuFWYamDfBxaWX_QLhAaP070YlnO6xH1WSDeQgzaJ0Xt72g52OPDM6RT-rBUdQQsLvNbjO8TBY-TMRric8aWTae4N3uin9jWaBKDf89tEwSnwcwTncVqARW3IXvHGMnQr62cKyHXXbWcTfyxQj_3Dd0ZleBCBL0VGqpJe7ML2SN4pJ0yh5KRlFAxAaZoMj3qhoc_s0hwGP_mt5KULf0Pza0qX7wJHOiGQgTwIP7eLakipctbOS0S7nDSUWQInxLxPioqwsYpSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3c7d37bab.mp4?token=lIZP-hqpGFBIf6LeQlAzEqWUTsAJ78_Zrc3cE6JYrK7wncydHy8Qc12jYp-_2soKkUHFkCoCffp7xuFWYamDfBxaWX_QLhAaP070YlnO6xH1WSDeQgzaJ0Xt72g52OPDM6RT-rBUdQQsLvNbjO8TBY-TMRric8aWTae4N3uin9jWaBKDf89tEwSnwcwTncVqARW3IXvHGMnQr62cKyHXXbWcTfyxQj_3Dd0ZleBCBL0VGqpJe7ML2SN4pJ0yh5KRlFAxAaZoMj3qhoc_s0hwGP_mt5KULf0Pza0qX7wJHOiGQgTwIP7eLakipctbOS0S7nDSUWQInxLxPioqwsYpSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه ۱۶ تیرماه در جریان سفر به آنکارا برای شرکت در نشست سالانه ناتو، در کنار رجب طیب اردوغان، رییس‌جمهوری ترکیه، بار دیگر از عملیات نظامی آمریکا و اسراییل علیه جمهوری اسلامی دفاع کرد و گفت این اقدام را نباید «جنگ» نامید، بلکه هدف آن «خلع سلاح هسته‌ای ایران» بود.
ترامپ با اشاره به نقش ترکیه در تحولات خاورمیانه گفت این کشور جمهوری اسلامی را «به‌خوبی می‌شناسد» و همراه با چند کشور دیگر، در تلاش‌ها برای پایان دادن به درگیری‌ها نقش مهمی ایفا کرده است.
او گفت اطمینان دارد رجب طیب اردوغان نیز خواهان دستیابی جمهوری اسلامی به سلاح هسته‌ای نیست.
رییس‌جمهوری آمریکا در ادامه با اشاره به روابط واشینگتن و آنکارا گفت: «این حتی جنگ هم نیست، یک عملیات نظامی است؛ خلع سلاح هسته‌ای ایران است.»
او همچنین با تمجید از توان نظامی ترکیه گفت این کشور می‌توانست وارد درگیری شود، اما چنین تصمیمی نگرفت.
ترامپ در بخش دیگری از سخنانش از عملکرد متحدان اروپایی آمریکا در ناتو انتقاد کرد و گفت از نبود حمایت آنها در جریان درگیری با جمهوری اسلامی «بسیار ناامید» شده است.
او اظهار داشت اگر نشست امسال ناتو در ترکیه برگزار نمی‌شد، شاید اصلا در آن شرکت نمی‌کرد و با اشاره به اردوغان، او را «دوست» و «رهبر بسیار قدرتمند» توصیف کرد.
رییس‌جمهوری آمریکا همچنین گفت ایالات متحده برای دفاع از اروپا در برابر روسیه هزینه‌های هنگفتی پرداخت کرده، اما در مقابل حمایت متقابلی دریافت نکرده است. به گفته او، در جریان تحولات اخیر عمدا واکنش متحدان را زیر نظر داشته تا مشخص شود آیا آنها نیز در مواقع لازم در کنار آمریکا خواهند ایستاد یا خیر.
ترامپ در این زمینه از بریتانیا، فرانسه، آلمان و ایتالیا نام برد و گفت مدت‌هاست این پرسش را مطرح می‌کند که آیا این کشورها نیز در صورت نیاز از آمریکا حمایت خواهند کرد یا نه.
@
VahidHeadline
رئیس‌جمهور آمریکا در عین حال تأکید کرد «ما به هیچ‌کس دیگری نیاز نداریم»، اما این پرسش را مطرح کرد که چرا آمریکا «تریلیون‌ها دلار در ناتو سرمایه‌گذاری کرده» تا از اروپا در برابر روسیه محافظت کند، بدون آن‌که چیزی در مقابل دریافت کند.
ترامپ گفت: «به نوعی داشتم دیگران را آزمایش می‌کردم تا ببینم آیا کنار ما خواهند بود یا نه، چون مدت‌هاست می‌گویم ما به آن‌ها کمک می‌کنیم، اما مطمئن نیستم آن‌ها برای ما چنین کنند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/76802" target="_blank">📅 18:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76801">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d41863b92e.mp4?token=H5vropMRrtoPra6aO4ZZu34LymTHCM9ezjqNOuzQR0KboH1xtLF351CrJmRJDzkipiulRsLa_MTS0Qb97n8ZR0frINrgnXtzg44li-aTrev5zqpxjR1iYRlbiYkaernbjt9dmseFEQk1W7GxBgSfyfp_bXmDZZUEjAlbO7DSK7u9Ass3EeuLTSy-gHc4tt55Bcd7zBenbFZqC7ns1sHBknTmYCDuGsPG2ayyZHBJNIBWLciDWjzWaWgiqsCb4zFhTMcUnBxnCkEdkHIXVEaHIyMiYmZG20RKhXpjkU-go_Q2EjVBLg8NXUuikoqs47_X6FZZ2Uq_l4PPrpZo6nIddw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d41863b92e.mp4?token=H5vropMRrtoPra6aO4ZZu34LymTHCM9ezjqNOuzQR0KboH1xtLF351CrJmRJDzkipiulRsLa_MTS0Qb97n8ZR0frINrgnXtzg44li-aTrev5zqpxjR1iYRlbiYkaernbjt9dmseFEQk1W7GxBgSfyfp_bXmDZZUEjAlbO7DSK7u9Ass3EeuLTSy-gHc4tt55Bcd7zBenbFZqC7ns1sHBknTmYCDuGsPG2ayyZHBJNIBWLciDWjzWaWgiqsCb4zFhTMcUnBxnCkEdkHIXVEaHIyMiYmZG20RKhXpjkU-go_Q2EjVBLg8NXUuikoqs47_X6FZZ2Uq_l4PPrpZo6nIddw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهوری ترکیه روز سه‌شنبه ۱۶ تیر، در نشست خبری مشترک با دونالد ترامپ، رئیس‌جمهوری آمریکا به مذاکرات جاری میان تهران و واشنگتن اشاره کرد و گفت که او و دولتش در تلاش‌اند که روابط آمریکا و ایران را به سطحی باثبات برسانند.
اردوغان در این نشست که در حاشیه اجلاس سران ناتو برگزار شد، تاکید کرد که این تلاش‌ها در راستای برقراری صلح جهانی خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/76801" target="_blank">📅 17:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76800">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KX_E1IEFKXhhIw-2JMXRRBMTuUwUUa12lH5bseBvJD2YffUrr1bzyXhcr5ZBTr-uHLE_P6T1H8xEutcqmBFVKnvohe3_le_DVk64rtOB1bvP5qMNUD65LB2MVs7gK34OL4PEqZ5luY3ZSR6TjdMirHB2U3jVnhCPH5FPot3qcD_NXqg_T5TnDZ_I2_Wk6qJVxVqn5wF2v5MHwJBpg5i9hyXSYHf-NGTMvtg40PZ9mIax8--9vqSFL0xEz-98ebg7ITD_tDppCsEFGzAdyxfjFKs1rNrzKTP8v0hrPgKjfp_9Tfar36SHnab2-aMz6Jy-gnynFiC0ETP7e2layOGIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا اعلام کرد یک نفتکش روز سه‌شنبه ۱۶ تیرماه هنگام عبور از تنگهٔ هرمز با یک پرتابهٔ ناشناس هدف حمله قرار گرفت.
این نهاد اعلام کرد نفتکش بر اثر این حمله دچار «آسیب سازه‌ای» شده، اما هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.
این حادثه یک روز پس از حمله به دو نفتکش، یکی حامل نفت خام عربستان سعودی و دیگری حامل گاز طبیعی مایع قطر، رخ داده است.
خبرگزاری رویترز حمله به آن دو کشتی را تأیید کرده و وب‌سایت اکسیوس به نقل از دو مقام آمریکایی گزارش داده بود که سپاه پاسداران دست‌کم دو موشک به سوی آن‌ها شلیک کرده است؛ ادعایی که جمهوری اسلامی تاکنون به آن واکنشی نشان نداده است.
سخنگوی وزارت خارجه قطر روز سه‌شنبه اعلام کرد هدف قرار دادن نفتکش قطری «الرکیات» در نزدیکی تنگه هرمز، حمله‌ای غیرقابل قبول به امنیت کشتیرانی بین‌المللی و تأمین جهانی انرژی است و ایران را مسئول حمله به آن دانست.
هنوز هیچ گروه یا کشوری مسئولیت حملات تازه به نفتکش‌ها در تنگه هرمز را بر عهده نگرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/76800" target="_blank">📅 17:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76799">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c18721dbe0.mp4?token=F8WoBBEes1VrsEV2eRupZ0cJt1SG0dlj8wdpoa7omUriK0j7Gmqkz1oPG5zMkBpkxBXDiVvFeeLPV47eZzEl7onk0tG2W5yQKI5K_msiTAQBA_gqXeIsE1Bb7nK3WX1GyrG6GJVmf0_YCV7sawM9k1aC0RwlnD_2fDvHpqsHWLZ2pD_lJ9i13yhWZEWKy0202ojv1SOFQoBzb4syx5-7qD2R1LXlCG4-LILeUufSmV6W3LhnDHfrgADXz8uEWhSPmMDh5_xxZ4_V2IlV71fJn09SuB7Dl2Enb9Xxzx8Ccb3QaHRXuclooC0YWC7rFOmbPNOmYF4ft1vxS_u8Zw16mw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c18721dbe0.mp4?token=F8WoBBEes1VrsEV2eRupZ0cJt1SG0dlj8wdpoa7omUriK0j7Gmqkz1oPG5zMkBpkxBXDiVvFeeLPV47eZzEl7onk0tG2W5yQKI5K_msiTAQBA_gqXeIsE1Bb7nK3WX1GyrG6GJVmf0_YCV7sawM9k1aC0RwlnD_2fDvHpqsHWLZ2pD_lJ9i13yhWZEWKy0202ojv1SOFQoBzb4syx5-7qD2R1LXlCG4-LILeUufSmV6W3LhnDHfrgADXz8uEWhSPmMDh5_xxZ4_V2IlV71fJn09SuB7Dl2Enb9Xxzx8Ccb3QaHRXuclooC0YWC7rFOmbPNOmYF4ft1vxS_u8Zw16mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری که در شبکه‌های اجتماعی منتشر شده گروهی از شرکت‌کنندگان در مراسم تشییع جنازۀ علی خامنه‌ای را نشان می‌دهد که به عباس عراقچی ، وزیر خارجۀ جمهوری اسلامی ایران، حمله کرده و او را «بی‌شرف» خطاب می‌کنند.
گروهی از هواداران نظام جمهوری اسلامی که با مذاکره و توافق با آمریکا مخالف هستند، اعضای تیم مذاکره‌کننده را به «سازشکاری» متهم می‌کنند. روز گذشته نیز تصاویری مشابه از حمله به مسعود پزشکیان در حاشیۀ تشییع جنازۀ علی خامنه‌ای منتشر شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/76799" target="_blank">📅 16:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76798">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZ36Wri3HuxdMnRdRrnKim5KHPBlKWE9bd0jbXeAN7nvoeJB6Eh00OEZFDxwxwB3DIQR700aK4Gee5c8DVpkPP125JBVxT6bpvBKMd0CDiDHq6AgQ_nj_JWNbA432HVCj7wxktjsxM06_1cKtFa928FtnrYBY3w3JqaQia7VyleNNovHpX9EIrCO3jdWi0QaWYV6vG4KiZHER_Z937S3sHlFyv9IKaaBVpSAwA_i7XDm7xJKK3MrinzsZzRcbWXFMD5dZWGFip4rFBWdq9bRyS6o_zvj99VfDM252Xr4CJEOEB25RSqBSgzYzE6_engc-cy2cZ-eDp2MRKiLzlgLbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با نزدیک شدن زمان انتقال تابوت علی خامنه‌ای به عراق برای اجرای مرحله تازه‌ای از مراسم تشییع رهبر پیشین جمهوری اسلامی، محمدرضا سیستانی، فرزند ارشد علی سیستانی، مرجع عالی‌قدر شیعیان در نجف، به دفتر علی خامنه‌ای اطلاع داده است که پدرش بر تابوت او نماز نخواهد خواند.
در همین حال، جواد شهرستانی، داماد و نماینده علی سیستانی در ایران، نیز در مراسم تشییع و نماز میت علی خامنه‌ای در تهران حضور نداشت.
پیش‌تر محمدکاظم آل‌صادق، سفیر جمهوری اسلامی در عراق، اعلام کرده بود که مراسم استقبال رسمی از پیکر علی خامنه‌ای شامگاه سه‌شنبه در شهر نجف برگزار خواهد شد و آیین تشییع عمومی نیز از ساعت ۶ صبح روز چهارشنبه در شهرهای نجف و کربلا ادامه خواهد یافت.
خودداری علی سیستانی از اقامه نماز میت بر پیکر علی خامنه‌ای در حالی صورت می‌گیرد که جمهوری اسلامی از زمان کشته شدن رهبر دوم خود، مجموعه‌ای از مراسم تشییع و وداع را در چند شهر ایران برنامه‌ریزی کرده و اکنون نیز در تلاش است این آیین را با برگزاری مراسم در شهرهای مذهبی عراق ادامه دهد.
غیبت مهم‌ترین مرجع شیعیان عراق در این بخش از مراسم، یکی از مهم‌ترین حاشیه‌های مرحله عراقی تشییع علی خامنه‌ای به شمار می‌رود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/76798" target="_blank">📅 16:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76797">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mTsVUP1Ig3rq5ZJ2mOWxpFHWL8uZ2lvjAHcnFlMNb0PM0ZY-_BVoa55fo1S1RXcGZ1_hDAgGsezBIKey_U798UaaIEYhYIIHf4bRuwi9ehgcpfPOcDtItmZt6yji-_OcVW5H8YslpGOKy2Haoi04ER-q-jtt-FmI6L_frnKnBCi7a5_J1stuKmtfcQdOlRSDa3N5EkOQ8Q-1Cy2cZ1Bjy9LtDdonf6lRO7L-k6It8L4XplTbu8Mo2da30Qp4nQj9DkCKnuyb2tmd7Oh8HASQXjyeCrhuJXJV09-X6ll1E20BEcTZJfWxcWZjD7zAOH0tx2RFaUDJbc8TF3sM3I3Dcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس به نقل از دو مقام آمریکایی گزارش داد که سپاه پاسداران روز دوشنبه دست‌کم دو موشک به سوی کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده است.
بر اساس این گزارش، دو کشتی در پی این حمله آسیب قابل توجهی دیده‌اند، اما هیچ تلفات جانی گزارش نشده است.
حمله گزارش‌شده پس از آن رخ می‌دهد که مهلت توافق یک‌هفته‌ای میان ایالات متحده و ایران برای توقف حملات در تنگه هرمز به پایان رسید.
اکسیوس می‌نویسد که ازسرگیری حملات ایران، تفاهم‌نامه‌ای را که کمتر از سه هفته پیش امضا شده بود، در معرض فروپاشی قرار داده است.
این منبع خبری می‌افزاید که
احتمال می‌رود ایالات متحده در واکنش، اهدافی در ایران را هدف حملات نظامی قرار دهد.
@
VahidHeadline
صداوسیمای جمهوری اسلامی به نقل از «برخی منابع» گزارش داد که «نفتکش الرقایات» متعلق به قطر، قصد داشت «با حمایت نیروی دریایی آمریکا» از مسیر عمانی تنگه هرمز عبور کند، اما «پس از بی‌توجهی به هشدارهای مکرر، هدف حمله قرار گرفته است.»
این گزارش تلویزیون حکومتی جمهوری اسلامی این‌گونه القا می‌کند که تهران این حمله را انجام داده است. با این حال، جمهوری اسلامی تاکنون به‌طور رسمی مسئولیت این حمله را بر عهده نگرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/76797" target="_blank">📅 16:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76796">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVokYKzJK7O2S3s4esaNUH299xRxICnHptJGsmSTaylyeTc9QoAn3srkpB-mbBocNs20jbvR2E1hCeVRvLihbZlGfn8JS4thZkjDMNx2XK9uvdy6MCB-SweBgx-_SUjgRP2hLZwwi6gs0X9P02zBfYZxV0bhIa2m8C5ryx0BMTxf_ibtJmYpZmOfWVfER1XOzQVmfP899PE-gKE39mZZP0Sd0ZM-aAmfOUzVII_DjULvOsnDM8g_MN0fZDAsOERRL4IHHKQxc1HZqiJ3_KIhhvtUwzfvPcLM2YXTHqNmXRuBnymxPMeHV1vO8EWFppNJrnF5YtiUej2oR0H0i6x4fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO)، بامداد سه‌شنبه ۱۶ تیرماه، اعلام کرد یک نفتکش در حدود ۱۵ کیلومتری شرق لیما (Limah) در سواحل عمان، هنگام حرکت به سمت جنوب، از سمت چپ بدنه هدف یک پرتابه ناشناس قرار گرفت.
به گفته این سازمان، این حادثه باعث آتش‌سوزی در نفتکش شد، اما تاکنون هیچ تلفات جانی یا آلودگی زیست‌محیطی گزارش نشده است.
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد مقام‌های مسئول در حال بررسی این حادثه هستند و به همه شناورها توصیه کرد هنگام عبور از این منطقه با احتیاط تردد کرده و هرگونه فعالیت مشکوک را به این سازمان گزارش دهند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76796" target="_blank">📅 03:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76795">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418508ca7a.mp4?token=bH-uFVMBeJ75aWdAaAm-LD-TgcvoL5wvh5CouGkBzbX7W_vSRfR8fwIm0Ge3OpDPDIDKh6M17IL-Rp5n7Dlgdp43_-rLUDgdc8Kcm1zJof2pTojd26ipE8BJhMERGr3mIdP6Dc_C6pF67_0n5eWBlRg4HdOXsdfl_WYankH3aTrOCBFa2RpSj_Z2J2xx8AGOQXof14NORZPKBlWlnWwruZN8WPiPfD8zxlwlf6GOoC34SZj-dDxY43wHvCIWHkIbSGgMCQXkTOQY_65ZP4zHRTnnaBQwKIEhggDa0nKCsdDiuUEhodvEXhgABDq36GkYh6c8_tmnWXdjh5SLS8HPLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418508ca7a.mp4?token=bH-uFVMBeJ75aWdAaAm-LD-TgcvoL5wvh5CouGkBzbX7W_vSRfR8fwIm0Ge3OpDPDIDKh6M17IL-Rp5n7Dlgdp43_-rLUDgdc8Kcm1zJof2pTojd26ipE8BJhMERGr3mIdP6Dc_C6pF67_0n5eWBlRg4HdOXsdfl_WYankH3aTrOCBFa2RpSj_Z2J2xx8AGOQXof14NORZPKBlWlnWwruZN8WPiPfD8zxlwlf6GOoC34SZj-dDxY43wHvCIWHkIbSGgMCQXkTOQY_65ZP4zHRTnnaBQwKIEhggDa0nKCsdDiuUEhodvEXhgABDq36GkYh6c8_tmnWXdjh5SLS8HPLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، گفت که از جانی اینفانتینو، رئیس فیفا، خواسته است اخراج فولارین بالوگون، مهاجم تیم ملی آمریکا، را بازبینی کند، زیرا به اعتقاد او خطایی که منجر به کارت قرمز شد، عادلانه نبوده است.
آقای ترامپ در جمع خبرنگاران در دفتر بیضی کاخ سفید گفت: «تنها کاری که کردم این بود که درخواست بازبینی دادم، چون فکر نمی‌کردم آن صحنه خطا باشد.»
او همچنین داوری را که این کارت قرمز را نشان داده بود، «افتضاح» توصیف کرد.
این اقدام بی‌سابقه، روند رسیدگی انضباطی فیفا را در کانون توجه جهانی قرار داده و با واکنش خشمگینانه بلژیک، رقیب آمریکا در دیدار روز دوشنبه برای کسب جواز حضور در مرحله یک‌چهارم نهایی، روبه‌رو شده است.
اتحادیه فوتبال اروپا، یوفا، هم به‌شدت از این تصمیم غیرمنتظره فیفا انتقاد کرده و آن را «بی‌سابقه، غیرقابل درک و توجیه» توصیف کرده است.
@
VahidHeadline
در ادامه واکنش‌های گسترده جهانی به رفع محرومت فولارین بالوگون، مهاجم تیم‌ ملی آمریکا، فدراسیون فوتبال بلژیک روز دوشنبه ۱۵ تیرماه اعلام کرد تصمیم فیفا برای صدور مجوز این بازیکن در رقابت مرحله یک‌هشتم نهایی جام جهانی را به چالش می‌کشد.
فدراسیون فوتبال بلژیک در بیانیه‌ای گفت از روند طی‌شده برای این تصمیم «عمیقا نگران» است و برای دفاع از «اصول بنیادین اخلاق، رقابت عادلانه و منافع فوتبال» به پیگیری این پرونده ادامه خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76795" target="_blank">📅 22:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76794">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f07511960e.mp4?token=ivNPpBBIEA9Rpr-IPwRXWA-zHd3qVC_Bo3YBUPkU0fUFijuPyqMbQ497qp-w9MOfeWTisXXlArJXlKKGj8VGZi-KYy7c1_aC9RBJoRvTZP6YlVY4zKM_T1leIiTvReNoqJDp2jxBqj7Nll1LH4ou2bJhZXVPyp-_juIGbVXDOWLEzHns35Bh8QUvYp_wGuW3N2HwEWAWIvv_QVs-PsBLSNRwQh4kzbiODiR1a6SugAUzPHEHy3seqHBS6qZVvcd1YEkzVtq4YW-5nC5w8PD0qZ8elAMEZS9M6spk9XGiVWEaHuAchIZUmMfGI_37e0JMu5kCvmFwsCTBOeqYfxmx3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f07511960e.mp4?token=ivNPpBBIEA9Rpr-IPwRXWA-zHd3qVC_Bo3YBUPkU0fUFijuPyqMbQ497qp-w9MOfeWTisXXlArJXlKKGj8VGZi-KYy7c1_aC9RBJoRvTZP6YlVY4zKM_T1leIiTvReNoqJDp2jxBqj7Nll1LH4ou2bJhZXVPyp-_juIGbVXDOWLEzHns35Bh8QUvYp_wGuW3N2HwEWAWIvv_QVs-PsBLSNRwQh4kzbiODiR1a6SugAUzPHEHy3seqHBS6qZVvcd1YEkzVtq4YW-5nC5w8PD0qZ8elAMEZS9M6spk9XGiVWEaHuAchIZUmMfGI_37e0JMu5kCvmFwsCTBOeqYfxmx3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه بار دیگر گفت: من به دنبال تغییر حکومت در ایران نیستم، هرچند این تغییر حکومت اتفاق افتاده است.
ترامپ افزود: حکومت اول از بین رفت، حکومت دوم از بین رفت. حکومت سوم معقول‌تر است. خواهیم فهمید.
@
VahidHeadline
دونالد ترامپ گفت آمریکا یا با ایران به توافق خواهد رسید یا «کار را تمام خواهد کرد.»
رئیس‌جمهور آمریکا در یک گفت‌وگوی تلویزیونی گفت قیمت نفت با وجود بسته شدن تنگه هرمز چندان بالا نرفت «آنقدر که ما نفت از آنها گرفتیم. مردم اصلا خبر نداشتند و همه اینها فقط در عرض یک ماه و نیم اتفاق افتاد.»
رئیس‌جمهور آمریکا بار دیگر تکرار کرد که کشتی‌های نیروی دریایی و تمام هواپیماهای نیروی هوایی ایران را از بین برده است: «در نهایت فهمیدند که دیگر رادار ندارند، چون سامانه‌های راداریشان نابود شده بود. بنابراین، آخر شب و در تاریکی آنها را هدف قرار دادیم.»
او همچنین گفت: «نیروی دریایی قدرتمند ما بزرگ‌ترین محاصره‌ای را که کسی ندیده اعمال کرد و در طول دو ماه حتی یک کشتی هم نتوانست از محاصره عبور کند. بعد نزدیک شدیم به اینکه شاید بتوانیم به توافقی برسیم پس محاصره را کاهش دادیم. نمی‌دانم، شاید هم به توافق برسیم.»
آقای ترامپ تاکید کرد که «به هر حال پیروز خواهیم شد. یا به توافق می‌رسیم، یا کار را تمام می‌کنیم.»
او گفت تمام کردن کار ایران کار آسانی است: «تمام کردن کار دشوار نخواهد بود. البته من ترجیح می‌دهم توافق شود، چون نمی‌خواهم ۹۱ میلیون نفر تحت تأثیر قرار بگیرند.»
«ما می‌توانیم ظرف یک ساعت پل‌هایشان را ویران کنیم. می‌توانیم شبکه تأمین انرژی را از کار بیندازیم. همه آن نیروگاه‌های بزرگ، زیبا و مدرنی را که ساخته‌اند. آنها پول زیادی داشتند اما حالا دیگر پولی ندارند. ما هیچ پولی به آنها نداده‌ایم اما می‌توانیم برق و نیروگاه‌های تولید برقشان را از کار بیندازیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76794" target="_blank">📅 18:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76792">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vN2Rp9vsRwmf5ug9l50hUSp-C5VkJmivOG3tYQDo39jReCj7PjANLugc1TsDX01dxVYeVboYK6dyBEWQtf-7MkzwCY8k0I_28tRkbhsZkEpcCmLMEJvLbX7oXnRhBFKM5-2yCPSSK0CaiTrxePlJNgpNRqXzMRH0gOzZZ-GXXBRJPKkY59D1ohs5x0tgGDcvI26XhwHQpPLyrzGvzoX-zCu9xeb6Tt36nelI_rF5gwfTy_f7laRQows2rR_fRvyPebqxGPvD3hG0OXCaOC0UmR8RkJ_lojtgxJ0CSJqPUAuBrlS9g6MwXJJTL_0EEJ2IsZN1r8R6FOdPwd_teDjdow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/26366fc1dc.mp4?token=XG3hs9w5PQW_soKQlACu8FcY2IXwj4c4xFd0u4MGpJOVAzGaZu0jbNBBJBItjauSqu3EjDG4wyDLRV1JC7B2obsxEBsHAX6KT1r46LWTv9LdMhk2eZI5GDyhXoz23dP6o31Om1cVKnx2hZt5lj7B_H5P-6nhWI8hQYORzVCPpa0SnQpmFHYNTRdMd90tHZaZarRI9sv8NPEU1SOs_v727OZpjrnkw4LN9IbZCu7vy5fuSXD0DtFYGBbY9JK0je3yKt7Wv1wOgXiYrDrxA4fLNBCOrgRKdUb--swFSZ32u56kUlMzTND2SnWsnqlY4bfWEafZDg1GtkSKsS8LRQFaTA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/26366fc1dc.mp4?token=XG3hs9w5PQW_soKQlACu8FcY2IXwj4c4xFd0u4MGpJOVAzGaZu0jbNBBJBItjauSqu3EjDG4wyDLRV1JC7B2obsxEBsHAX6KT1r46LWTv9LdMhk2eZI5GDyhXoz23dP6o31Om1cVKnx2hZt5lj7B_H5P-6nhWI8hQYORzVCPpa0SnQpmFHYNTRdMd90tHZaZarRI9sv8NPEU1SOs_v727OZpjrnkw4LN9IbZCu7vy5fuSXD0DtFYGBbY9JK0je3yKt7Wv1wOgXiYrDrxA4fLNBCOrgRKdUb--swFSZ32u56kUlMzTND2SnWsnqlY4bfWEafZDg1GtkSKsS8LRQFaTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیمای جمهوری اسلامی روز دوشنبه ۱۵ تیرماه تصاویری از حضور احمد جنتی، دبیر شورای نگهبان در مراسم تشییع پیکر علی خامنه‌ای منتشر کرد.
رسانه‌ها روز دوشنبه همچنین تصویری از محمود احمدی‌نژاد را در مراسم مرگ رهبر سابق جمهوری اسلامی منتشر کردند.
خبرگزاری فرانسه روز دوشنبه گزارش داده بود در حالی که مقام‌های جمهوری اسلامی تلاش کرده‌اند تصویری از وحدت در صفوف حکومت ارائه دهند، تاکنون هیچ‌یک از روسای جمهوری پیشین جمهوری اسلامی، که روابطشان با خامنه‌ای دچار تنش بود، در این مراسم‌ها دیده نشده‌اند.
مراسم تشییع جنازه علی خامنه‌ای پس از دو روز قرار گرفتن پیکر او در مصلای تهران از ساعت شش صبح دوشنبه ۱۵ تیرماه آغاز شد.
روز ۹ اسفندماه ۱۴۰۴، در موج اول حملات اسرائیل به تهران بیت علی خامنه‌ای به‌شدت بمباران شد،‌ به شکلی که تمام ساختمان‌های محوطه بیت با خاک یکسان شده بود و همین احتمال سالم ماندن جسد رهبر سابق جمهوری اسلامی را بسیار کم می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/76792" target="_blank">📅 16:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76791">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8v9nGCz5DrFy8puCzb1MgP7tAYWRdtogm7DLZBSelejV5f-2j95INeLpGqJeSWt9pnTD2IVmo53HEWhbQKNUJvg-iyP2-b397FgeyUyzqUQX-zkF2mpS0fDpD3EJE7xNbkEtZqw5BdrBXPqIHW5jbt93UQyWsec3bOnyFQQEF6cwsibKcTrNFHwquOnUG5Fq9sJCtQoELn3ZDbKDckf2GB0-lasfzAzBd4ol11plp1ipPm7ZkPD1sJsBPHj16gySyWNEJWQ6LGRIfrIXx95Rl0_Qddd5IMeNk6GFTlfMW9EEU1j2MmEmbni_L-_zlMrfkxe83Oh672UyDOZqUzwmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، آقای مهدی ناظر و خانم مهناز چاردولی، نامزد او، را به اعدام و ۱۰ سال حبس محکوم کرده است. همچنین خانم عاطفه ناظر، خواهر آقای مهدی ناظر، به ۱۰ سال حبس محکوم شده است. این سه نفر در تاریخ ۲۱ دی‌ماه ۱۴۰۴ در تهران بازداشت شدند.
@IranRights</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/76791" target="_blank">📅 16:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76790">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/neM0GnIlkPe8k5yz94bUTm8fnmWQDyBRL_7t_WjjF3hCykD6dxvqFFak40rlNK118kghUb892wMsJEthvpGjdzraHvNP0y5oSHbLMDArQleFkWnSNuZWZjrBffawwGChCHJVAHOryJcGl5Pz6xFUsGiEVCnl7XzTEZZvRfgVusaMMdHnrPkYT7UwVwBxUj2H-VpE-_3UlKkg1SjjviEehpskYmIcujdyg69sCgrA8kqj-MRT11hY_htYF9XzAkCE8sONUt3Uy6ATZ-KVkIm6SKwdkmi-Bev6P9WO4GhWg4XHhalwLvRYQ9jrgRROUcdJ_7MbXmnyGVyFaoFmKA1_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه روز یکشنبه ۱۴ تیر متن حکمی را منتشر کرد که در آن مجتبی خامنه‌ای، رهبر جمهوری اسلامی، غلامحسین محسنی اژه‌ای را برای یک دوره جدید پنج ساله به عنوان رئیس قوه قضائیه ابقا کرده است.
محسنی اژه‌ای از دهم تیر سال ۱۴۰۰ با حکم علی خامنه‌ای به این سمت منصوب شده بود و مدت پنج سال ریاست او بر قوه قضائیه به پایان رسیده بود. حکم رهبر جدید جمهوری اسلامی با امضا در تاریخ ۱۳ تیر منتشر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/76790" target="_blank">📅 19:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76788">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RbMuGQ74ZyLE1sYCDZcxrhrFeeQWAWXzv6T1j9CKDd833hWX5VW8vuyerEHot8bEw_FaJrI7OCEnj0hb4tp22uYzKXcczJN6Br05nLs722bsWft3DMV1NdJ5gOOl3F-7BfSyZ1nFN8h5-kJEGS5IGSnN0nS3RIsbPT7bsTQi47BwV8r0njVW9EdTeramtUKrqMmGzVp_LF5Ef3TzdjRD3hLF8n0Ym65i8oPwrt419DlJQ-xgenV18Dug-RPHvhiqr2Vcv_aR-LJ353IuC2i52Wct2hshIIPkEnHhVKqi-5T4BKOJn38klw06WQji-p_lehVWL6KeZ3rOwEBmjLjFug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15ac8211bb.mp4?token=lfOoUyw-RJG-n_L6o7lNSoabIbq6bvulyPmlG0HNwdX5rjSehBRSgfv66MmWquCoKOyA2mnZtVZJMuNgL27KKhoNob-B-y_3mMfrIpu7HLaR9ZoI9qQxVTiwKCVwDsjthgVspyt7RE4QYGcCaxKaG8mdMKRfGWjzG5rLq_kZQsj8GZ7aW2pWjTxEEx8VI7gOxlagd0sPl-4cq3CqjjCdxDiIx4DJD8idqfzpa1BRLg5ufH9cQ9jYKNGvPq4NP5MiZLoGhqUvpUsHKU2_wpcTrXT6OhrVB3ykhe3D_KZZCD50ZstzMCT0muEZXPh3m2U1NKYl-lOMBP1Hb0ngTpZzIA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15ac8211bb.mp4?token=lfOoUyw-RJG-n_L6o7lNSoabIbq6bvulyPmlG0HNwdX5rjSehBRSgfv66MmWquCoKOyA2mnZtVZJMuNgL27KKhoNob-B-y_3mMfrIpu7HLaR9ZoI9qQxVTiwKCVwDsjthgVspyt7RE4QYGcCaxKaG8mdMKRfGWjzG5rLq_kZQsj8GZ7aW2pWjTxEEx8VI7gOxlagd0sPl-4cq3CqjjCdxDiIx4DJD8idqfzpa1BRLg5ufH9cQ9jYKNGvPq4NP5MiZLoGhqUvpUsHKU2_wpcTrXT6OhrVB3ykhe3D_KZZCD50ZstzMCT0muEZXPh3m2U1NKYl-lOMBP1Hb0ngTpZzIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماز میت بر جنازه علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، روز یک‌شنبه، ۱۴ تیر رأس ساعت هشت صبح، توسط "آیت‌الله جعفر سبحانی" اقامه شد.
مراسم تشییع او بیش از چهار ماه پس از مرگش در حال برگزاری است.
اما نکته قابل توجه در این مراسم غیبت مجتبی خامنه‌ای است که از او به عنوان آیت‌الله یاد می‌شود و کمتر از ده روز پس از مرگ پدرش به عنوان رهبر تازه جمهوری اسلامی معرفی شد، اما در این مراسم حضور ندارد تا نماز میت را برای پدرش اقامه کند.
در این مدت طولانی از مجتبی خامنه‌ای نه فایلی صوتی منتشر شده و نه ویدئویی که نشان دهد او توانایی رهبری حکومت را دارد.
با این حال سه پسر دیگر علی خامنه‌ای، مصطفی و مسعود و میثم، که از روز ۹ اسفندماه سال گذشته یعنی آغاز جنگ تاکنون خبری از آنها نبود روز یک‌شنبه بر سر تابوت پدر خود حاضر شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 454K · <a href="https://t.me/VahidOnline/76788" target="_blank">📅 09:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76787">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyWOTESnLk5-LHfW2BKkPgjOBNXjM9j0j9g_Xm4NC3hLCuijQC1tnD_WQKEpqZi4wfyiIT08_-NMQl4SY8xjzhw8wZevj9GE2-9SXU1PqWA6_5t7iF5G49id_o-HxyUEJzPhspzVgKe1ZFVi5oTvyzUyYpjTAKVfUn2yoDSuJUSRKTJyAnOvaKvSVjbPMnMgPo7bcncli0EVme83wDp_mJNif6z5fjOgcuyVRWKLrPGtCQijotx0dCF-xTyr9bs28OCURy02UOzk4nlNH2p-NYsjz7xzTpJVDc78YOOjsViYBGBhXugYxgEeWTm6g3PjrEIW_CxL69i7yKCFUHvNzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا روز شنبه ۱۳ تیر، در گفتگو با وبسایت خبری آکسیوس، اشاره کرد که تصاویر مربوط به مراسم تشییع علی خامنه‌ای، رهبر پیشین جمهوری اسلامی را مشاهده کرده و از دیدن گریه افراد، متعجب شده است. او گفت:
از دیدن برخی ایرانیان که در مراسم تشییع گریه می‌کردند متعجب شدم چون گمان می‌کردم مردم از او متنفرند. شاید این اشک‌ها ساختگی باشد.
ترامپ پیش‌تر اعلام کرده بود که مذاکرات جاری میان تهران و واشنگتن، به‌دلیل برگزاری این مراسم یک هفته متوقف شده است. او در بخش دیگری از این گفتگو با اشاره به حضور اغلب چهره‌های سیاسی و نظامی جمهوری اسلامی در این مراسم گفت:
آن‌ها همه آن‌جا جمع شده‌اند. کار یک شلیک است! اما این کار را نمی‌کنم چون در آن صورت کسی برای مذاکره باقی نمی‌ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 452K · <a href="https://t.me/VahidOnline/76787" target="_blank">📅 23:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76786">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این مجله ۹ ماه قبل از سرنگونی حکومت صدام‌حسین در عراق و سپس اعدام او نیز عکس صدام حسین را روی جلد برده بود. معمر قذافی نیز از دیگر رهبران منطقه بود که ۶ ماه قبل از کشته شدن به دست معترضان، عکس او روی جلد تایم رفت.</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/76786" target="_blank">📅 19:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8eed8d3ddd.mp4?token=oDlkwjAMJkZAk8xROcYA-cjHchJjBwXy5_XqIhAjx9p2cocv8N8J2X56YIgRO4BtG6Ckr8I8PqSOtkP3sAnPU2LuvdhZfVGNMbVq8Rz2hGVqXN51iROC1qBq0LfxAh1xghiKZXMsUY4-9PElm_XO8aAc-TujX8kSjeUcDDpAIroBU2aJv0nK5ktVSugQsmAipuGMyc3h8T_7jFykP5umJzIGupgiq8yze7lWEEzLzBaL9s957fqeADVigUQT05XZYGItcvbWbskX_VvXTrdtybPEMZ2YE3mqEVQ4kwX_5VYsqI1ombD8-kvYjRP88Ie64s0bJLFqyeyOlmf_1xg0gA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8eed8d3ddd.mp4?token=oDlkwjAMJkZAk8xROcYA-cjHchJjBwXy5_XqIhAjx9p2cocv8N8J2X56YIgRO4BtG6Ckr8I8PqSOtkP3sAnPU2LuvdhZfVGNMbVq8Rz2hGVqXN51iROC1qBq0LfxAh1xghiKZXMsUY4-9PElm_XO8aAc-TujX8kSjeUcDDpAIroBU2aJv0nK5ktVSugQsmAipuGMyc3h8T_7jFykP5umJzIGupgiq8yze7lWEEzLzBaL9s957fqeADVigUQT05XZYGItcvbWbskX_VvXTrdtybPEMZ2YE3mqEVQ4kwX_5VYsqI1ombD8-kvYjRP88Ie64s0bJLFqyeyOlmf_1xg0gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رحیم صفوی: این یک جنگ موجودیتی است و مطمئنم که اسرائیل از بین خواهد رفت
یحیی رحیم‌صفوی، از فرماندهان پیشین سپاه پاسداران و مشاور مجتبی خامنه‌ای در حاشیه مراسم تشییع علی خامنه‌ای، با اشاره به درگیری میان جمهوری اسلامی و اسرائیل، آن را یک «جنگ موجودیتی» خواند و گفت دو طرف در نبردی قرار دارند که تنها یکی از آن‌ها می‌تواند در منطقه باقی بماند. او افزود: «من مطمئن هستم آنچه باقی خواهد ماند ایران است و آنچه از بین خواهد رفت اسرائیل است.»
او همچنین با مقایسه کشته شدن علی خامنه‌ای با واقعه عاشورا، مدعی شد کشته شدن او، «حرارتی» در میان مردم ایران، شیعیان و جهان اسلام ایجاد خواهد کرد.
رحیم‌صفوی در بخش دیگری از سخنانش ابراز امیدواری کرد که مجتبی خامنه‌ای راه پدرش را در حفظ «ایران قوی»، دور نگه داشتن سایه جنگ از کشور و پیشبرد توسعه ادامه دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/76784" target="_blank">📅 17:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/On2HcU1UV_JfZ5MPszBBHkkAzjiy-0l_2zurE3a18i_OmqMjZVAspX1TkyZaxRzT7DakVCTR4CYLA2TVRkKoo7adCPyQM1YYmX3eT1AjhDtMV23eBFYxR_4POssaey-TiJ_MIuyKxn-nEz5CAbgRv598Aq0-MRQiyIT7F06rLSiAD5Odz2w6SAPL7W27JaYurNaGnvdVSnjx_1L7X4ni4aO52a1l9HcixJl40P1O6x_kumuxNnrEKFo-oxNW1-rPkrcSKG0v-igidBEi9aMOb0p3u5tY5eTPAFKbMTl_8Xg6QiblkDGrlGoxdO1USoHC_2c34t6MDsfDAv3LwcZrBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ اعلام کرد به‌دلیل مراسم تشییع جنازهٔ علی خامنه‌ای، رهبر کشته‌شدهٔ جمهوری اسلامی، «یک هفته» به مقامات تهران فرصت داده است.
رئیس‌جمهور آمریکا در سخنرانی خود در مراسم دویست‌وپنجاهمین سالگرد استقلال آمریکا که شامگاه جمعه ۱۲ تیر به وقت تهران برگزار شد، گفت: «ایران را به‌شدت در هم کوبیدیم. آن‌ها برای توافق بی‌تاب‌اند. به‌شدت می‌خواهند به توافق برسند. ما به‌خاطر مراسم تشییع، یک هفته به آنها فرصت دادیم، چون آدم‌های خوبی هستیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/76783" target="_blank">📅 17:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76782">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_Z-75oWf7uZw4al0Oo3VGBSRloLeNxqLEWMz4JjY7-ew2la6OEFGVi1XuRfNghntiT4iHHA2-2LvbPE6EoSD1WctLk2hhRnrWwpN8_hjsoqd4OgjYUKKDCy76wP5aDgYeMdU1rm3SyvGwx3BQN0uxkqSVBTmXN305yIv5PyuQM9Ul1DQk_Y0QXmel8WbIenIlj3cYM9ePB48ROcYnUrNo4W2jMrnCq0phiVtVRIWIIc8mwWs7ayAmvqlEOtqCOz_OCX8Mf1zE_NX4-fORO1lxZl4aeaipyo4LO1nBSk9GeyBN_-racV5i9gOTi2uBetEdqSXlQHfhNlg4jK_Nos4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگین کیانی، عکاس مستند اجتماعی و مدرس عکاسی، از سوی دادگاه انقلاب بابل به یک سال حبس محکوم شد.
رسانه‌های حقوق بشری گزارش گزارش داده‌اند، شعبه اول دادگاه انقلاب بابل خانم کیانی را به اتهام «تبلیغ علیه نظام» به یک سال زندان محکوم کرده است. این حکم روز ششم تیرماه صادر و به او ابلاغ شده است.
نگین کیانی ۱۹ فروردین امسال در منزل پدری‌اش در بابل توسط نیروهای امنیتی بازداشت و یک روز بعد با قرار وثیقه آزاد شده بود.
این عکاس ۳۷ ساله پیشتر نیز به دلیل فعالیت‌های مدنی خود چندین بار احضار شده و با برخوردهای قضایی روبه‌رو بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/76782" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76781">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0Nko0NfvX8dsGBb-PCL4rf3cFVnCKWRUtQUBQ2wmUXaxVYzIGn4E8x3nSegzIC5DA38izPQAGsBdiW4sNIsdv_Oeh6sJzgP_E_QXnYZuQAUyEAixXcMAxQ3Ukz0CCv2h16JwIFxVX4sto-bWbDx-sTCNn7obOwvxvr07TtnaSakARC7bIkthbIBX1DA5upaqlS5l4XBFR7tAJ77d1AGJEaGX_TRgSse71CggoQbY_nlij3FNKoFGztHSsCktCGk-vO2yeb7JNdQdoMRGC9YIhx90os5cZZhbKNNYm611HskHEcQc639INS3UjnOVOzUOUuzGxkSakvh6eGGAVBhBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرنوش پارسی‌پور، نویسنده، مترجم، تهیه‌کننده و فعال اجتماعی ایرانی، امروز در بیمارستانی در حومه سانفرانسیسکو درگذشت.
خانم پارسی‌پور که از دهه ۷۰ خورشیدی در شمال کالیفرنیا زندگی می‌کرد، از هفته گذشته به علت سکته قلبی در بیمارستان بستری شده بود.
او در سال ۱۳۲۴ در تهران به دنیا آمد و اوایل دهه ۵۰ خورشیدی از دانشکده علوم اجتماعی دانشگاه تهران فارغ‌التحصیل شد. نخستین داستان بلندش، «سگ و زمستان بلند»، را نیز در تهران منتشر کرد.
خانم پارسی‌پور در دهه ۵۰ برای مدتی در تلویزیون ملی ایران کار کرد و سپس برای ادامه تحصیل ایران را ترک کرد، اما در سال ۱۳۵۹ به ایران بازگشت.
او مدت کوتاهی پس از بازگشت به ایران بازداشت شد و چهار سال را در زندان گذراند. پس از آزادی به ترجمه و کتابفروشی پرداخت، اما فشارها ادامه یافت و سرانجام به آمریکا مهاجرت کرد.
خانم پارسی‌پور در سال‌های اقامت در آمریکا نیز چند داستان بلند و ترجمه منتشر کرد.
شناخته‌شده‌ترین آثار او در ایران «طوبا و معنای شب» و در خارج از ایران «زنان بدون مردان» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 432K · <a href="https://t.me/VahidOnline/76781" target="_blank">📅 03:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76778">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XeispTHSt3oZCzCpn55TffLJlcyCNfqBKsT08eJWlggCnQT4IB1PP4mqqTYAvWJj1KDz2_w1qaZyC6Klj-34OPOssMZWUzAtlby0FcPHSgxASFkcY4tvvzYxRkrigqlLjwWWQKoqgaEQSab240grL-SV7-G0-_NeikfEYpT6m-9AbTeUsUMUKJFoOW1kzIV7CJOSbTHlnZ133RD_o5nrEiRn1hR0KSx_O2dVAlBp07ChuIp6ZGQr0zluvRET-9hvzqSU5KvPGqrtvnnRlyGf_uwackQ63pOuZbbaoX1tkk4ZdQwxJ2dP5tW7p6ySZo3li5EDOMbk1m2wB5SYc3MQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BWBhxsZlJsWbFcaJOOFUqx-bvQf8-v-Rp5hOaahPyOFfHX5_KP9jY9kqWI9kw-C2R_otBu2clXih6ZJfWgswfOt6z3GJQ_dnfokTDbIkGOqYBuUmtT870FRsWwZ0wevKp17b7OOsD8sNfezVMieDxzHJ29LM5K-uFwMfTwpT9c6XUzxdUi1s3p12eEMzKbucDHqYIU1qLAVCrNfX5rL0i0jX9qqVd5PG0NVbEraVdZx9zmKRzzAsJmshh6MjJ8RgzvqFATNRhFeu99d0BzmoWxEhmvyvsxH1qvl-v4x8NMjoSGZXwOl2Eoglw9Id0yOY3SjEoHAXYou5S3B9AtKA_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f3b6da11ae.mp4?token=awIY7Lnhni2UBfwZ1tyjBDSIUkfTyDEWCJhpfVpnY7dsR1HpqZgCNjwz_szL0ZCrjOFwi0QJ0bvgfJeRy5LDhX90eI6JV7XinLkdfynNXRfuLqkIdW_c9MoKsrJwiBYKWTaeLlpQ5zFmjyGeShwv9sqmwJoyoKkiXKqfmfUkDjmIpJ1Usj-lEiAKIxgX9hzeXkOXJoHQA_C8dzhqh0y7TrZ3jZ2L-FMusCw2GK-ThMNOqilQ8XEsKoxEsnIajA-GUcTkF63qtELO35vQafC1DXmfGUhUHv-nkq2V2ay1yafZTrNvEMAlWSSWE8aTCQGqCgESMJSBRovWbPGTmZU6sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f3b6da11ae.mp4?token=awIY7Lnhni2UBfwZ1tyjBDSIUkfTyDEWCJhpfVpnY7dsR1HpqZgCNjwz_szL0ZCrjOFwi0QJ0bvgfJeRy5LDhX90eI6JV7XinLkdfynNXRfuLqkIdW_c9MoKsrJwiBYKWTaeLlpQ5zFmjyGeShwv9sqmwJoyoKkiXKqfmfUkDjmIpJ1Usj-lEiAKIxgX9hzeXkOXJoHQA_C8dzhqh0y7TrZ3jZ2L-FMusCw2GK-ThMNOqilQ8XEsKoxEsnIajA-GUcTkF63qtELO35vQafC1DXmfGUhUHv-nkq2V2ay1yafZTrNvEMAlWSSWE8aTCQGqCgESMJSBRovWbPGTmZU6sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📡
@VahidOnline</div>
<div class="tg-footer">👁️ 448K · <a href="https://t.me/VahidOnline/76778" target="_blank">📅 19:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76777">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/555882678d.mp4?token=tR_qIdMN9z5cW8nKxVsL2zSwIjLt-7KNoRSB2xha0nAim-W6lQsJEKR8qumC0JF5NJnAWLyQhfJK2KWMmueatfrJVStnMyWs_KxHsMFleOyIT5TIRk1vUCZMq-uzNQZ26-HB4p-Ked3VAg7J-WteaEnSRiIljm0W5ELPLIkQrMgk9bhI4ayW-Sdj5IH0KIRGsRkP5pKtJ3JMzfqFGPLhfVt9tfLpvk_L3nB2-Vh13-qr45ZlKzLmZbl09Y5pQkLLmwU7e-Q2ReUsEdUS7yp_tmdvbrMosUuy3lMDd_mD4v-BvWZGOeYMpqbfUuLTTnmCJ7tMVKfVdi6Oc0F-a5L_3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/555882678d.mp4?token=tR_qIdMN9z5cW8nKxVsL2zSwIjLt-7KNoRSB2xha0nAim-W6lQsJEKR8qumC0JF5NJnAWLyQhfJK2KWMmueatfrJVStnMyWs_KxHsMFleOyIT5TIRk1vUCZMq-uzNQZ26-HB4p-Ked3VAg7J-WteaEnSRiIljm0W5ELPLIkQrMgk9bhI4ayW-Sdj5IH0KIRGsRkP5pKtJ3JMzfqFGPLhfVt9tfLpvk_L3nB2-Vh13-qr45ZlKzLmZbl09Y5pQkLLmwU7e-Q2ReUsEdUS7yp_tmdvbrMosUuy3lMDd_mD4v-BvWZGOeYMpqbfUuLTTnmCJ7tMVKfVdi6Oc0F-a5L_3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">[بنا بر تصاویر رسانه‌ها، مقام‌های مختلف در گروه‌های چند نفری در مقابل جعبه‌هایی که گفته می‌شود بقایای علی خامنه‌ای و تعدادی از اعضای خانواده‌اش در آن‌ها قرار دارند حاضر می‌شوند.]
رهبر ترکمنستان، روسای جمهور عراق، تاجیکستان، گرجستان، نخست وزیران پاکستان، ارمنستان، روسای مجلس جمهوری آذربایجان، عمان، قطر، عراق، ازبکستان، قرقیزستان، بنگلادش، مصر، وزراری خارجه نیکاراگوئه و کنگو و معاون رئیس شورای امنیت روسیه، رئیس اقلیم کردستان عراق، به همراه هیئتی از طالبان افغانستان و شبه‌نظامیان مورد حمایت ایران در عراق، یمن و لبنان و همچنین دبیرکل جهاد اسلامی فلسطین در مراسم ادای احترام شرکت کردند.
از نکات قابل توجه عدم حضور مقام بلندمرتبه‌ای از کشورهایی مانند چین، روسیه و ترکیه به عنوان حامیان جمهوری اسلامی ایران در این مراسم بود.
تاکنون تصویری از اعضای خانواده علی خامنه‌ای به جز هادی خامنه‌ای، یکی از برادرانش، در این مراسم منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 479K · <a href="https://t.me/VahidOnline/76777" target="_blank">📅 18:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76776">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y2nkEmE5xEqtCju8R2tawWo9D_Ao6IrZQgOVv_Mcrnb6DOz8bl1b2zxpmoJAJpp984GUaJow1qNqdWZGIiRRVWLRL5GrToT0HlbH0ZRh06J8zDJXPUZwahA8x-YcOqyyzOr85N-dEAy2kjeoDt0aimrHzvRVrlz2ZuHZbsucqq7-Rl4OFt2jLrVg9vs8zwqMwYvZ4vZSdJTI7qlXCJHLnDN6Qo9DG6sV3uR3EE33guJbr6ycr-iulj5NsbTki20dR-hQeYUWn0hPjGTyMeAzbYGb9bkgNjh2xM6ZV24AUPdZ7GAtoUTbDwCsfaPD6EsZNi28Yv0ufWIHtXWyI9ISfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سایت هرانا الهام زراعت‌پیشه، وکیل دادگستری، از سوی شعبه اول دادگاه انقلاب شیراز به شش سال حبس، دو سال ممنوعیت خروج از کشور و ابطال گذرنامه محکوم شده است.
بر اساس این گزارش، شعبه اول دادگاه انقلاب شیراز الهام زراعت‌پیشه را به اتهام «اجتماع و تبانی علیه امنیت ملی» به پنج سال حبس و به اتهام «تبلیغ علیه نظام» به یک سال حبس محکوم کرده است.
این دادگاه همچنین او را به مدت دو سال از خروج از کشور منع و گذرنامه‌اش را باطل کرده است.
الهام زراعت‌پیشه ۱۴ اردیبهشت ۱۴۰۵ در محدوده دادسرای اجرای احکام شیراز بازداشت شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/76776" target="_blank">📅 18:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76775">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Or55aUs2ALBKl6zL3PgHZlx_sbImwdyUa7SOJEfKslVOX1-7_2WUPInoRvDPHNl2xgCEb0nJrsCAJX51WAjCT-lk8dp3DElMm64mG5flta7HIF-445BjLuk98FMWe2t6uDazwkX7jbAqOkPXpoMwbhgmgNz-TqzDkxi-7BlrVtu61fHxteQyxo-5Xcfc-afLZS0lrLua_eqspWLkz-VqTz2AlWd5gPaMx6p2jmtiGhw7V2vEid4C5pZ6YrjfsA2f0ByAtTGFxdHiiSVu3bCvvj1guy_ER7FvieJZEQ9NbgxdwLyAvQPoXxYCyGivaVzRUY91BKDEcCr1HhH-l6xG9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارغوان فلاحی، زندانی سیاسی ۲۴ ساله محبوس در زندان اوین، از سوی شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، به اتهام «بغی» به اعدام محکوم شده است.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، با اعلام این خبر نوشت حکم اعدام فلاحی بر اساس ماده ۲۸۷ قانون مجازات اسلامی و با استناد به اتهام «بغی از طریق عضویت در گروه‌های مخالف نظام و اقدام مسلحانه» صادر شده است.
ارغوان فلاحی در جریان پرونده‌ای بازداشت شد که چند متهم سیاسی دیگر نیز در آن حضور دارند. نهادهای امنیتی جمهوری اسلامی او را به عضویت در گروه‌های مخالف حکومت متهم کرده‌اند.
منابع حقوق بشری می‌گویند او این اتهام‌ها را رد کرده و روند رسیدگی به پرونده‌اش با محدودیت در دسترسی به وکیل و برگزاری جلسات غیرعلنی دادگاه همراه بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/76775" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76774">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cFPhpG4QBhuuXuwr-_WoMvbZlJKk5TXlA5Cn1JmbQY8meD6Bv0R_WANajaQ_yAYapqoJBAMgVJc2rxGK5PnO4_h9XKuqjd0uY0b-SFylbgTduadj-Ho5oZG_m9Lxb0QWlXSVP4jCO3yBiGRbCsu7LDBU437IaX4biXV7Pflf4mtyqKC05ANDp-6QPuY6usUiOCRFwJwj-vKI5ycFwAWxKjqVSeRw-Aj5_c_LrdCE8DNLuUm_IZ0PqjDOAHX4yBZnVhVo_f-NhHKHGlNwXm3CzviSsuuciDrZ4wEyuBiz3T5KS5k-9OJykIUxJwUt_dycqvV57xm8S0DvbdagNAkM1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، بامداد جمعه ۱۲ تیرماه در گفتگو با شبکه سی‌ان‌بی‌سی گفت جمهوری اسلامی از نظر نظامی «کاملا شکست خورده» و مذاکرات میان تهران و واشینگتن ادامه دارد. او افزود: «فکر می‌کنم آن‌ها تقریبا با همه چیزهایی که ما نیاز داریم موافقت کرده‌اند» و ابراز امیدواری کرد این مذاکرات به نتیجه برسد.
ترامپ با مقایسه وضعیت کنونی با جنگ‌های گذشته آمریکا گفت برخلاف جنگ ویتنام، افغانستان و کره که سال‌ها ادامه داشتند، در چهار ماه نخست دولتش توانسته جمهوری اسلامی را از نظر نظامی شکست دهد. او گفت: «آن‌ها کاملا از نظر نظامی شکست خورده‌اند. هنوز چند موشک برایشان باقی مانده، اما اگر لازم باشد آن‌ها را هم از بین می‌بریم.»
رئیس‌جمهوری آمریکا همچنین گفت هفته گذشته پس از آنکه جمهوری اسلامی یک پهپاد را به سمت یک کشتی فرستاد، نیروهای آمریکایی سه بار مواضع آن را هدف قرار دادند و هفته پیش از آن نیز دو شب پیاپی حملات مشابهی انجام دادند. او افزود این عملیات‌ها هم‌زمان با ادامه مذاکرات انجام شده است.
ترامپ در بخش دیگری از سخنانش گفت آمریکا با استفاده از نیروی دریایی خود «دیوار فولادی» در اطراف ایران ایجاد کرده و «حتی یک کشتی هم نتوانست به ایران برسد.» او ادامه داد حکومت ایران با تورم ۳۰۰ درصدی، کاهش شدید درآمد و کمبود مواد غذایی روبه‌رو است و در صورت دستیابی به توافق، آمریکا می‌تواند گندم، ذرت و سویا را از طریق کشاورزان آمریکایی در اختیار ایران قرار دهد.
رئیس‌جمهوری آمریکا همچنین گفت «قدرت و جسارت» جمهوری اسلامی از بین رفته و با انتقاد از گزارشی در روزنامه نیویورک تایمز که نوشته بود ایران نسبت به چهار ماه قبل در موقعیت بهتری قرار دارد، افزود: «توان نظامی آن‌ها از بین رفته، رهبرانشان از میان برداشته شده‌اند، فرماندهان رده دوم و حتی برخی فرماندهان رده سوم از بین رفته‌اند، بنابراین نمی‌توان گفت امروز در وضعیت بهتری قرار دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 449K · <a href="https://t.me/VahidOnline/76774" target="_blank">📅 02:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76773">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ELT8fk37XQ8PgNHLF0Hy7g7grIL6608ycteoE_Q-0wyNhshorfeb8LX6iJCe_t23PPt_jBrrpjha9LD6jqkWnj4PcimXe6v9zl_GAcVNeCipOsAbETtYhkIBeD39PeAB31PZX-oKkwv-fLLx5EsW115rrRcRXQpgom2Nph3F8gBizQQygGbxDBeCvJ5yhB47rAgtNq38UOt4Q2HTh9AmTPkFr5ipoeASfi2DgXTQOOVQcQXwVlgvgVm6pMLt9R0VREuZZReLO5a89HwqyUAX3mfNRqbr7mWRhYzOWDR6D0zjjuVfB5bidy2mpuzVG1kDbsmpxAXvJ6LaKzT79Bp1zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"دارم خواب می‌بینم؟ سلام دنیای جدید!" ویدیو دریافتی از 'شادی جوانان شهر #گله‌دار در شهرستان مُهر استان فارس، یکشنبه ۱۰ اسفند' Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/76773" target="_blank">📅 16:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76772">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kB3C0LyFbSMnWYXZCw1LNUxYX3PgqfJAz8jc8WUCtViyorfMJnxbz5y0T40nyCGE8zSZFoxncBsTbntSBNhApCTgJIk2pgUnAKoLndPvuXkL-LKcnra0vXGHr_Ouq1MonTbsH1LlO3Yh6DZUY3-rf6YRNXxNkfsloGQHq8WvfhdGwv25qc3O3VNSZYKiEl_vuyq61EdHDG9mOAq-epmAG4VuOwaJyASmBCvR__k6hFYfMtuR4fs7mWaWfg8muOts_vUy8-boxm29WlkokvleS7BeF6D7f7D-fzlX9i13G7YeqZWsi5wV5vwgM0UMvafSZyfZJyiMYLXqdKU2heeq5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی کرابی (برسام) شامگاه ۲۱ دی‌ماه ۱۴۰۴ در منطقه سلسبیل تهران هدف شلیک مستقیم قرار گرفت و به کما رفت.
این جوان ۳۰ ساله که متولد سبزوار بود، بر اثر اصابت گلوله دچار مرگ مغزی شد و پس از یک هفته، در ۲۹ دی‌ماه ۱۴۰۴، در بیمارستان امام حسین تهران جان باخت.
پیکر او برای خاکسپاری به سبزوار منتقل شد.
ایران‌وایر مطلع شده است که به دلیل نقش بستن عنوان «جاویدنام» بر سنگ مزار او، مسئولان بنیاد شهید خانواده‌اش را تحت فشار قرار دادند تا این عنوان را به «شهید» تغییر دهند.
پس از آن‌که خانواده از پذیرش این خواسته خودداری کردند، سنگ مزار مجتبی کرابی (برسام) شکسته شد.
خانواده او نیز تصمیم گرفتند تا «روز آزادی» سنگی بر مزار این جوان کشته‌شده نگذارند.
مجتبی کرابی مربی بدنسازی، ورزشکار رشته فیتنس و داور رسمی پاورلیفتینگ بود.
یک منبع نزدیک به خانواده او به ایران‌وایر گفت: «مجتبی چند سال در کنار دایی‌اش، روح‌الله نصیری، از ورزشکاران نام‌آشنای خراسان رضوی، به‌صورت تجربی و آکادمیک آموزش دید و با تلاش و پشتکار توانست به‌عنوان مربی و داور رسمی پاورلیفتینگ، با مدرک معتبر، فعالیت حرفه‌ای خود را آغاز کند.»
او از هواداران تیم پرسپولیس بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76772" target="_blank">📅 16:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76771">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2c3ad4afb.mp4?token=Q-0bkKuM3d_KPgZqUf8iAYOF-RysshoEAEOESX5sWXD_-B6vD0VuwgTiVTmqmOdU_9cmhlIFBO4t1oJJjilyhWLtlH1n83E2ZySN3vNx83kyMh5vGr7Kr9TNt4vtCQqYbvmHaoW5EmKJpPzKC47hvCi00Ml6dhL5MLRr5aIXHRmBJaQZiyLGD0w_WcypcskckVhpPZ2LCGLpAOzYoZBFhzE3PtnUQvJ4B8wHQUoH6b094Hv3jI_N_64CThn61j45WLIUolRFBwWE8befqY-J9cPZxrAUDa-fOx-4przeysOH_0ew_NpfzQsZ4JPCr-Okp7YOabOFMwt-J3GWVcnFbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2c3ad4afb.mp4?token=Q-0bkKuM3d_KPgZqUf8iAYOF-RysshoEAEOESX5sWXD_-B6vD0VuwgTiVTmqmOdU_9cmhlIFBO4t1oJJjilyhWLtlH1n83E2ZySN3vNx83kyMh5vGr7Kr9TNt4vtCQqYbvmHaoW5EmKJpPzKC47hvCi00Ml6dhL5MLRr5aIXHRmBJaQZiyLGD0w_WcypcskckVhpPZ2LCGLpAOzYoZBFhzE3PtnUQvJ4B8wHQUoH6b094Hv3jI_N_64CThn61j45WLIUolRFBwWE8befqY-J9cPZxrAUDa-fOx-4przeysOH_0ew_NpfzQsZ4JPCr-Okp7YOabOFMwt-J3GWVcnFbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی می‌گوید گزارش‌های منتشره دربارۀ موافقت با دسترسی بازرسان آژانس بین‌المللی انرژی اتمی به سایت‌های هسته‌ای آسیب‌دیده «کذب است».
محمد باقر قالیباف در گفت‌وگویی تلویزیونی، که بخش دوم آن، شامگاه چهارشنبه ۱۰ تیر از تلویزیون رسمی جمهوری اسلامی پخش شد، با اشاره به قانون مصوب مجلس و مصوبۀ شورای عالی امنیت ملی جمهوری اسلامی، تأکید کرد که بر اساس قانون، «به هیچ عنوان دسترسی به سایت‌هایی که بمباران شده و آسیب دیده‌اند، داده نمی‌شود».
به گفتۀ مذاکره‌کنندۀ ارشد جمهوری اسلامی تعیین سطح دسترسی‌ها بر عهدۀ شورای عالی امنیت ملی‌ است و فراتر از آن، «هیچ امتیازی داده نخواهد شد».
محمدباقر قالیباف گفت بر اساس مصوبۀ شورای عالی امنیت ملی،‌ دسترسی بازرسان آژانس در حال حاضر به دو مورد نیروگاه هسته‌ای بوشهر و رآکتور تهران محدود است و به سایت دیگری دسترسی ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76771" target="_blank">📅 16:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76769">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DBygwqspA4r_Ot8PAKcpyDUgj66nAl2PjOvYrWWYbgt4epPmS0-00bh6gSTAzb2fSXdPZxJfr9l2TA1H_dhfcdSB-8IL2BvBLxZ8rtgLLWJ52lLvOC2xmW_2BkPZh_XhmL9Ttm0IM8OhVBRVJpcoLsW4yPhIkyvFu4aLb2EG6tE3AqjmOTkLDfE4D_iKMJA9NoHDZscLGEZcBKjL0fsbidCqGEm2u-U1WvA_72a76qFLPTxLDXYpmSEfRqlUJJJtRi-GnxbZsBGvfDwSZTLSKZSx5dAJl1iLHmfilqegLGw-d0fdzo80cM3tbPzGCXuMtpOds1K9y3g7-c8Ha6QFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ItAc_Twx3Fl6PM-yKdEfU3arKARUjrSWYtbqKv0fq7p5b7geex7WZJP68Xdi06Etx-LlaDVrq0Mwcrp-XufXi_0RN3i_mmX8WuebgTHTxmSYdD9VO6qePwAnYzRTvOVFHMxpAGDZaTAnMP1PTzpDBRnlQ8uk-568U1XMurnVXV82MoAgxbJfE3Yi6e8VMAeFqYBGwQ3xibI3GzcFVBQ-PHBPwAEeW6Q04nWWMF1gnUsIvF8_M-n9oRddKL1ftB3PTHeSb4Xf3k8eAHyMYh5vbgIU761OQJPDHinz5tvCttQVCrcyQeNQirWcQoNcbbBQFK0k6F6oO41omCTatOwpUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منابع امنیتی عراق از وقوع یک حملۀ پهپادی به اردوگاه گروه‌های کرد مخالف جمهوری اسلامی در منطقۀ کوی‌سنجاق در شرق اربیل خبر می‌دهند.
هنوز جزئیاتی از این حادثه منتشر نشده، اما طی روزهای اخیر چند عضو سپاه پاسداران و نیروی انتظامی جمهوری اسلامی در استان‌های غربی ایران از جمله کردستان هدف حملاتی قرار گرفته و کشته یا زخمی شده بوده‌اند. یک گروه مسلح کرد هم مسئولیت برخی از این حملات را بر عهده گرفته بود.
مقام‌های امنیتی جمهوری اسلامی طی روزهای اخیر، بار دیگر از مقام‌های عراق و اقلیم کردستان خواسته بودند که به حضور گروه‌های کرد مسلح مخالف جمهوری اسلامی در خاک اقلیم کردستان پایان دهند.
سپاه پاسداران طی ماه‌های اخیر بارها با موشک و پهپاد به پایگاه‌های گروه‌های کرد در اقلیم کردستان و عمدتاً در اطراف اربیل حمله کرده است.
در همین حال خبرگزاری فارس به نقل از «منابع محلی» از وقوع چندین انفجار در اربیل و سلیمانیه، و از جمله هدف قرار گرفتن مقر «حزب آزادی» با موشک بالستیک خبر داده است.
@
VahidHeadline
درگیری‌های مسلحانه میان نیروهای سپاه پاسداران و گروه‌های مسلح مخالف جمهوری اسلامی در اطراف شهرهای سردشت و پیرانشهر، شامگاه چهارشنبه ۱۰ تیر و بامداد پنج‌شنبه ۱۱ تیر، ادامه یافت و به کشته شدن چندین نفر انجامید.
سازمان‌ حقوق بشری هانا اعلام کرد این درگیری‌ها در مناطق مرزی آذربایجان غربی رخ داده است.
رسانه‌های نزدیک به حزب دموکرات کردستان ایران نیز اعلام کردند در جریان درگیری عصر چهارشنبه در نزدیکی روستای «قزقاپان» در اطراف پیرانشهر، پنج عضو این حزب کشته شدند.
خبرگزاری فارس، نزدیک به سپاه پاسداران، بدون ارائه جزئیات اعلام کرد شش عضو حزب دموکرات کردستان ایران در این درگیری‌ها کشته شده‌اند.
کانال تلگرامی صابرین‌نیوز، نزدیک به نهادهای امنیتی جمهوری اسلامی، نیز مدعی شد در دو درگیری جداگانه، ۱۱ نفر از اعضای گروه‌های مسلح مخالف جمهوری اسلامی کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76769" target="_blank">📅 16:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76768">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/azTNXaqLyijrw9hw2LxG8ajg00kUHJY0dnAaRGAM8HF9fEARzonhqNT5Z-XIrJ3B4WKbjv_344tyTUMwhl2CysI_Yms0bFxpi6wIbIMx-rP6HBJvRw2UwrGVjrdW6eydTndX1FJuS6mALiYn2DPjm1-KGqlCzXSg8U--kuj8hMTbMoxOc-_3bAmESmcxOZrEGOFfvujueSfhlig8lArl2v0A83x7-huGjer1MwRSHkn-GtUPwqRsNbErY63AfSoss-Hb5k3Cw-NghukkDDxW1HFpBnNB3aGmDcrtZb1PkxVydKA9c9rvzREUSAtVLUqv28LvfeMzQp7ICf2wPtTdiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت کرمانی، وکیل دادگستری، از بازداشت دوبارهٔ سپیده کاشانی و هومن جوکار، دو فعال محیط زیست که پیشتر سال‌ها در زندان بودند، خبر داد.
آقای کرمانی به وب‌سایت «امتداد» گفت مأموران امنیتی عصر روز چهارشنبه دهم تیرماه با حضور در منزل این زوج، ضمن ضبط تمام وسایل الکترونیکی، آن‌ها را بازداشت کردند.
به گفته این وکیل دادگستری، نیروهای امنیتی همچنین سیما کاشانی، خواهر سپیده کاشانی را نیز بازداشت کرده‌اند.
او افزود تاکنون مشخص نیست این افراد توسط کدام نهاد امنیتی بازداشت شده‌اند و با توجه به تعطیلات پیش‌رو و بسته بودن مراکز قضایی، نگرانی خانواده‌های آن‌ها افزایش یافته است.
از دلایل بازداشت این زوج گزارشی منتشر نشده است.
سپیده کاشانی و هومن جوکار از اعضای مؤسسه «حیات وحش پارسیان» هستند که به همراه چند فعال دیگر محیط زیست زمستان سال ۱۳۹۶ توسط اطلاعات سپاه بازداشت شدند.
کاووس سیدامامی از بازداشت شدگان این پرونده که تابعیت کانادا را هم داشت، چند روز پس از بازداشت، به طرزی مشکوک در زندان اوین جان خود را از دست داد و مدتی بعد سازمان اطلاعات سپاه پاسداران دیگر فعالان محیط زیست بازداشت شده را به «جاسوسی» و «همکاری با دول متخاصم» متهم کرد.
سپیده کاشانی در طی سال‌های زندان در نامه‌هایی اعلام کرد که در دوره بازداشت تحت «شدیدترین شکنجه‌های روحی و روانی، تهدید به شکنجه فیزیکی و تهدیدهای جنسی» و «تهدید به مرگ» قرار گرفته‌اند.
او در نامه خود نوشته بود که بازجویان این پرونده «ویدئوی جسد» کاووس سید امامی را برای شکنجه به او نشان داده‌اند، و همسرش، هومن جوکار، را برای تهدید و شکنجه به پای چوبه دار ساختگی بردند.
سپیده کاشانی و هومن جوکار پس از سال‌ها زندان، در فروردین ۱۴۰۳ در پی عفو از زندان آزاد شده بودند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76768" target="_blank">📅 16:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76767">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=g5PA05VhBrntqn9qSkwxxYFcrbSQ89OPSfwI57KpVBs2I3M5-cGHd1dNo5r-bC2hZhbXsjN8vCBJmJ_LvgLvC3FgJaFYXT6EdXvETlflGOlnUkZE_9s61jTfgUiqq1epQ76ZE0SjDn0O_zXvfP3WT9mCepInzwdZpuqgF_k9erP-Jixqe-psI_ZiJWUE1UgYI1ArDioAQYcHThVpcMuk26XhvDOkJTmyZSgsb0TAqg22sy-LAABuz67bglFnJVpsmRbHg3_lOEaloCmUBCpSEERH2TurDjx8jaGLp1q-mGrxkCAmKYzc1N0Rbyj2oADKZ_1gNW6xpJUXa8p86o-JIA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=g5PA05VhBrntqn9qSkwxxYFcrbSQ89OPSfwI57KpVBs2I3M5-cGHd1dNo5r-bC2hZhbXsjN8vCBJmJ_LvgLvC3FgJaFYXT6EdXvETlflGOlnUkZE_9s61jTfgUiqq1epQ76ZE0SjDn0O_zXvfP3WT9mCepInzwdZpuqgF_k9erP-Jixqe-psI_ZiJWUE1UgYI1ArDioAQYcHThVpcMuk26XhvDOkJTmyZSgsb0TAqg22sy-LAABuz67bglFnJVpsmRbHg3_lOEaloCmUBCpSEERH2TurDjx8jaGLp1q-mGrxkCAmKYzc1N0Rbyj2oADKZ_1gNW6xpJUXa8p86o-JIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامرضا نوری قزلجه،‌ ؛وزیر جهاد کشاورزی"، با تایید سخنان محمدباقر قالیباف دربارۀ خرید محصولات کشاورزی از شرکت‌های آمریکایی  در دوران ریاست‌جمهوری ابراهیم رئیسی گفت: برخی از قراردادهای کشاورزی از طریق منابع ارزی بلوکه شده ناشی از تحریم‌ها بود و آن‌ها نیز به شرکت‌های آمریکایی مجوز می‌دادند و از آن‌ها خرید می‌شد.
محمدباقر قالیباف شامگاه سه‌شنبه در یک گفت‌وگوی تلویزیونی به خرید محصولات کشاورزی از شرکت‌های آمریکایی در دولت ابراهیم رئیسی اشاره کرده بود. پخش سخنان مذاکره‌کننده ارشد جمهوری اسلامی در همین زمان از سوی تلویزیون حکومتی متوقف شد.
رئیس‌جمهور آمریکا روز دوشنبه اول تیرماه در گفت‌وگو با خبرنگاران در کاخ سفید در مورد آزادسازی دارایی‌های ایران که در تفاهمنامه جدید به آن اشاره شده، گفته بود:
پولی که آزاد می‌شود قرار است برای خرید مواد غذایی استفاده شود... آن هم صرفاً از طریق ایالات متحده و از کشاورزان ما.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76767" target="_blank">📅 18:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J3wurWI0p0ZvbktY2PfAcU7_DbL0UhcMjUk8r2DELovOtSUZssEwRgTAH2w0rEHiKy5iGoj-NfbOpY8urT0t8soA38Xqo0CLFfuPni291so9dQqTeVl_JrKq-SXuLjNVSahyi6jQtThmDBO5X_kqpUi4yvJfkN7G3ZrBgDHs0_KITKuW_F3QHGCcBLUCu2zsY-FHzyQEwqH3dcHAYXhwEVwo1lh_MltLXpaDM9MXbF4TGbfyZORPQZkbgZ7kNyfPmdJUBk8TmepTkBBO7imFRrJbYaA0BaWfeDrtrvnWhNLFnZjMXkpyncvI5WZeE3vtdJtN-JC0oVFISNVaSY-d8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TObywhuGiNgAQkYiE79R1w2veCub3qi8r_PuMQhKAj_UsO-QfipXHJX23EgkvZ7HwOI6LyABd5MHvrBNlWEamqTEhuuUxdrgNAyIpLcAsgXm869gNhIzEcDcd7ozPDQMzQr7OzFRTXheiSXSetFTw_fuGxWpdCnZF5o5przLfwAh5SV5IXyCUl1uNByLtJQX-JDt9mj-agc3rl1Acj_BvPZ_Yqn4ZVVyB8c-VV6TKzk-k_mDVLHSNyg95lrH6Ji4-Ks0r6JUX0Pec2Y_2uWN3dDWwDvzXdsXmbWXsJqHlEVA44vxAiQrmtvHqNhernTUSFBCMOGN_6pxHFx24Xrwkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور آمریکا روز چهارشنبه ۱۰ تیرماه از روند مذاکرات ابراز رضایت کرد و گفت این روند «بسیار خوب» پیش می‌رود.
دونالد ترامپ که در واشینگتن با خبرنگاران صحبت می‌کرد، افزود که آمریکا چند روز پیش حملات شدیدی به ایران انجام داد، اما نشست‌های اخیر دو طرف در قطر به‌خوبی برگزار شده است.
او همچنین اعلام کرد: «روند خلع‌سلاح هسته‌ای ایران به‌خوبی در حال پیشرفت است».
ترامپ افزود: «آن‌ها نشست‌های بسیار خوبی داشته‌اند و باید ببینیم چه خواهد شد».
این اظهارنظر ساعاتی پس از آن بود که رسانه‌ها از برگزاری «مذاکرات فنی» غیرمستقیم ایران و آمریکا در روز چهارشنبه در دوحه، پایتخت قطر، خبر دادند.
این مذاکرات با میانجی‌گری پاکستان و قطر برای اجرای تفاهم‌نامهٔ اخیر میان ایران و آمریکا انجام می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76765" target="_blank">📅 17:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76763">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dsqw2u-qzQEjuesUXOKJmXjMTuo1qKlIejNMNNan1wCpP-vfQu5zqRRQFtcPcyQPxRjpRH5WrSPitatfMLSg7HtcJ1FGvbSKrIUSYbLcKqizVZbh66R6Hc3dYRcqqBhYSjE2zCpNQU-ntWqUh2DnG9mJ3xQaCEnRou2dMm0x5qJlt_v_UVQz7k_RBfOCvJ9hbbf_swwiD2lED57gk4GiexOD-hW0FgbT_hrcYZs7vUc09PQgj_PF8an_-Zn2qO6QwAkVA8l9gna_tjVD6xugIGQz35uzr4kchbvik4hCcHiMckfn3IzaQwJvLtBGvGiUhOY2ACKdw_1WTZxD9XqX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PQoYH4On5_R2BSeBmN7Bgjprg8o-PPjUEJNqnmxlMp08pSDEwpQ5ovuaAK4ta2L1oEh7PAYgWj7DaX4aKTqSrx58xL0sIUZt6Ao04sIxDtm5-GAQVKI_Bd86cfs-vukRH3yozCxYvjM2icY4lEjK6d_IqyAUI8M5VV748LePwuFHhvG4h7fstiBfGC6PVfwLN2ohjQDKs0dLEsP_G9QWRtudHpXbPX9NOQim3Km2VEWYebjsrwo_Cik4U0YL-mvKnhtIyMMGRkMsGFjpQismZlp5R3mCFeuXqF1a5ADsl7I0eutZZn9BlK3TND17Oo45W5gTlWuWmOIJo6ixF9xlnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی که برای شرکت در نشست‌های مرتبط با اجرای تفاهم‌نامه ایران و آمریکا به دوحه سفر کرده است، اعلام کرد کارگروه‌های پیگیری اجرای تفاهم‌نامه و نیز مذاکره برای دستیابی به توافق نهایی تشکیل شده‌ اما هنوز مذاکرات در این قالب آغاز نشده است.
کاظم غریب‌آبادی بعدازظهر چهارشنبه دهم تیرماه، پس از دیدار با شیخ محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر خارجه قطر، به خبرنگاران گفت رایزنی‌ها برای تعیین زمان و محل آغاز مذاکرات از طریق میانجی‌‌ها ادامه دارد و در صورت فراهم شدن شرایط لازم، این گفت‌وگوها آغاز خواهد شد.
به گزارش خبرگزاری ایسنا، پس از این دیدار نیز نشست سه‌جانبهٔ مذاکره‌کنندگان ارشد ایران، قطر و پاکستان برای بررسی روند اجرای تفاهم‌نامه برگزار شد.
@
VahidHeadline
دیوان امیری قطر چهارشنبه در بیانیه‌ای اعلام کرد تمیم بن حمد آل ثانی، امیر قطر، در کاخ لوسیل با استیو ویتکاف و جرد کوشنر، فرستادگان آمریکا، دیدار کرد.
در این دیدار، آخرین تحولات منطقه، به‌ویژه روند مذاکرات میان آمریکا و جمهوری اسلامی در چارچوب یادداشت تفاهم دو طرف، و همچنین وضعیت لبنان بررسی شد. دو طرف بر اهمیت تثبیت آتش‌بس به‌گونه‌ای که وحدت، حاکمیت و ثبات لبنان حفظ شود، تاکید کردند.
در این بیانیه آمده است که امیر قطر بر ادامه تلاش‌های میانجی‌گرانه این کشور با مشارکت پاکستان و حمایت از همه مسیرهای گفت‌وگوهای ناشی از یادداشت تفاهم تا دستیابی به توافقی جامع و پایدار که امنیت منطقه و صلح بین‌المللی را تقویت کند، تاکید کرد.
دو فرستاده آمریکایی نیز از نقش قطر و پاکستان در پیشبرد مذاکرات و نزدیک کردن دیدگاه‌ها قدردانی کردند و بر تعهد آمریکا به ادامه روند مذاکرات و تلاش‌های دیپلماتیک برای دستیابی به توافقی جامع تاکید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/76763" target="_blank">📅 17:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76762">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dpFmUE9iQYmikZiqeC8DI6wxL4Et9i2GjSdHWZyGvZ1sO8xxertCZ0IT1HTvFw1sUvy8PVbU-liuY49OlZjPZfvm6bQfRmg0EJhUFM2he7281cXMeusvEJXtRreBUVtZgMaFGrDTizTILpqAmkr-LOrABlqqJmxVXlEhU3m6FWgeJByNzi0eX2gqcmrAzh5a6gV71z8c5pDKcqQx9guflCYPsdIy8Cm82Skb6R13EhrCoJq9mLjDWxwAEFmV86EdunsAdwtbuaqdy9kIOZ2HHg8fUi8M6umetRbEcHMD2htoh2RhK-2bRtTdi02vc86zCte7yTmYmAFov79vzqFZUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با ادامه برخوردهای قضایی و امنیتی با فعالان صنفی فرهنگیان، سه معلم  با احکام زندان و مجازات‌های تکمیلی روبه‌رو شدند و یک فعال صنفی دیگر نیز در استان فارس بازداشت شد.
بر اساس گزارش شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران، احمد علیزاده، معلم بازنشسته و فعال مدنی اهل آبدانان، از سوی دادگاه انقلاب ایلام به دو سال حبس تعزیری، یک سال ممنوعیت خروج از کشور، ابطال گذرنامه و یک‌هزار و ۸۰ ساعت خدمات عمومی رایگان محکوم شده است.
هم‌زمان، آزاده سالکی، معلم شاغل در شهرستان خواف و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، به پنج سال حبس محکوم شده است. بر اساس خبر منتشر شده، حکم اولیه او ۱۰ سال زندان بود که در مرحله تجدیدنظر به پنج سال کاهش یافت.
آزاده سالکی پس از بازداشت در دی‌ماه ۱۴۰۴، حدود یک ماه در بازداشت به سر برد و سپس با تودیع وثیقه سه میلیارد تومانی به‌طور موقت آزاد شد. گزارش‌ها همچنین حاکی است اجرای این حکم می‌تواند به اخراج او از آموزش و پرورش منجر شود.
این معلم پیش‌تر نیز در سال ۱۴۰۱، زمانی که در شهرستان تربت حیدریه مشغول تدریس بود، به دلیل فعالیت‌های صنفی و اظهاراتش در کلاس درس، به مدت یک ماه از کار تعلیق و سپس به شهرستان خواف منتقل شده بود.
همچنین جان‌محمد احمدی، معلم بازنشسته و رییس انجمن صنفی معلمان نورآباد ممسنی، روز سه‌شنبه ۹ تیرماه توسط نیروهای امنیتی بازداشت شد. تاکنون اطلاعاتی درباره محل نگهداری، نهاد بازداشت‌کننده یا اتهام‌های منتسب به او منتشر نشده است.
آریا نورانی، معلم رسمی آموزش و پرورش در شهرستان مانه خراسان شمالی، نیز در ارتباط با اعتراضات دی‌ماه ۱۴۰۴ به ۱۴ ماه حبس محکوم شد.
شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران با محکوم کردن این اقدامات، خواستار آزادی بازداشت‌شدگان، لغو احکام صادرشده و پایان دادن به برخوردهای قضایی و امنیتی با فعالان صنفی شده است.
در ماه‌های اخیر نیز روند برخورد با فعالان صنفی معلمان تشدید شده است. پیش‌تر شعبه سوم دادگاه انقلاب اهواز پنج فعال صنفی فرهنگی و کارگری خوزستان را به سه سال حبس تعلیقی و دو سال ممنوع‌الخروجی محکوم کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76762" target="_blank">📅 17:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76761">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SyzG62dHwhesVTG5eFvVLWPtgOyBBflSat7Om3-sg7kY10Xdet8WEII83tsVOwwcQQ-Zh5U7HInoNjPiMyVVpKFqNagx1EXYHxx7VBALutbOW8L5JtmWo5kna6hmGqKo72DkOY78ifnAexuIcW0DIaqpRNYiEZMiMURL0U7pEo-fRX4kc2gWB3aNSiQ1oFQRM9jHuJsEZZqzCd-JZL5DjmghVJPKGxTmRKNmlERjDRygGpdHKFXlfYONT9DvKN42BrZgXPfT6rm517ew-fsRWS59OoiUFiPQnTsPHKqZOZfBG9VEBVs5s2gLNsrxaDHr8THh_QbWFv3H1NNLLHr3qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس، معاون رییس‌جمهور آمریکا با انتقاد از منتقدان که خواهان حملات بیشتر به جمهوری اسلامی هستند، در یک برنامه تلویزیونی گفت: «دیدگاه آن‌ها این است که فقط بمب بریزید، باز هم بمب بریزید؛ اما واقعا نمی‌توانند توضیح دهند که هدف نهایی از این کار چیست.»
او افزود: «اما چیزی که رییس‌جمهور [ترامپ] می‌گوید این است حاضرم دستور حملات هوایی بدهم، و به‌وضوح هم نشان داده که در صورت لزوم این کار را انجام می‌دهد، اما فقط زمانی که این اقدام در راستای دستیابی به یک هدف مشخص باشد.»
او در بخش دیگری از اظهاراتش گفت: «یکی از چیزهایی که درباره ایرانی‌ها برایم هم جالب و هم آزاردهنده است این است که می‌گویند نه، هیچ گفت‌وگوی صلحی در جریان نیست، اما در همان حال مذاکرات فنی میان واشینگتن و تهران درباره توافق صلح در حال انجام است. این یک تاکتیک مذاکره یا شگرد ایرانی است که من آن را درک نمی‌کنم.»
@
VahidOOnLine
جی‌دی ونس، معاون اول رئیس‌جمهور آمریکا در مصاحبه‌ای با شبکه خبری فاکس گفته است «ایالات متحده در رابطه با ایران در موقعیت بسیار خوبی قرار دارد.»
او گفت: «ایرانی‌ها در هفته‌های گذشته، هیچ نفت‌کشی را هدف قرار ندادند و جریان نفت در تنگه هرمز برقرار است؛ بخشی از آن به این دلیل که رئیس‌جمهور(ترامپ) تصریح کرد که اگر ایرانی‌ها به کشتی‌ها حمله کنند ما مقابله به مثل می‌کنیم.»
آقای ونس همچنین گفت: «اگر مذاکرات موفقیت‌آمیز باشد که ما می‌خواهیم موفقیت‌آمیز باشد، شما ایرانی را خواهید دید که بطور دائمی متحول شده؛ تروریسم منطقه‌ای و بی‌ثباتی را تامین مالی نمی‌کند و جاه‌طلبی‌های هسته‌ای را بطور دائمی کنار می‌گذارد و درنتیجه اقتصاد جهانی دوباره از آن استقبال می‌کند. این نتیجه خوبی برای مردم آمریکا و کل منطقه است.»
او همچنین گفت:«از سوی دیگر اگر آنها رفتار مناسبی نداشته باشند و امتیازاتی را که ما می‌خواهیم ببینیم ندهند، هنوز برنامه هسته‌ای آنها نابود شده، توان متعارف نظامی نابود شده و آمریکا در مقایسه با آنها در وضعیت قوی‌تریست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76761" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76759">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/150c916f8f.mp4?token=h6E_UkioTuW2LhMXC0yxh8-OwOEBV8e32x8ONvUtwW7WriXqUD9ppD25KHu5zmRlVnyq58h9jew-5mxZ--oh6pdTpWRtJRYuCBhWVjvpa_FWIZW6tnNrkeqDYY2_icdMjLjGEV25XKikecu88_g1KiwZkIL8c13BbkKoreHGI7mSQozByabPKK2aNtewOkv3gDQQUqcqfk2XpBdgfn6nQ2JzeyVjVeGXt_NZV_eVv6NnKdD5JHLb7KoU1a2lP4IcPOt6v9IQqxPQlhaguepQk1NFtnXup6Z9BvbjInEnyqXxiZsTw5lIWGR8uRtlP2A_SeK2XWfx9TLqHtOG5o_kEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/150c916f8f.mp4?token=h6E_UkioTuW2LhMXC0yxh8-OwOEBV8e32x8ONvUtwW7WriXqUD9ppD25KHu5zmRlVnyq58h9jew-5mxZ--oh6pdTpWRtJRYuCBhWVjvpa_FWIZW6tnNrkeqDYY2_icdMjLjGEV25XKikecu88_g1KiwZkIL8c13BbkKoreHGI7mSQozByabPKK2aNtewOkv3gDQQUqcqfk2XpBdgfn6nQ2JzeyVjVeGXt_NZV_eVv6NnKdD5JHLb7KoU1a2lP4IcPOt6v9IQqxPQlhaguepQk1NFtnXup6Z9BvbjInEnyqXxiZsTw5lIWGR8uRtlP2A_SeK2XWfx9TLqHtOG5o_kEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد جمهوری اسلامی، شامگاه سه‌شنبه اعلام کرد در حال حاضر «اصلا مذاکره‌ای با آمریکا نداریم».
او در گفت‌وگویی با تلویزیون حکومتی ایران محاصره دریایی آمریکا علیه بنادر ایران را که بعد از آتش‌بس و از فروردین‌ماه آغاز شد، «شدیدترین نوع جنگ» خواند که به گفته او «مردم و نان مردم» را محاصره کرده بود.
قالیباف افزود که برداشته شدن این محاصره «از موفقیت‌های بزرگ» تفاهم‌نامه امضا شده بین ایران و آمریکا بود.
او اعلام کرد که مذاکرات فقط تا زمان امضای یادداشت تفاهم ادامه داشت و سفر به سوئیس برای گفت‌وگو درباره «اجرای بندهای» همین تفاهم‌نامه بود که ۲۵ خرداد بین ایران و آمریکا امضا شد.
@
VahidHeadline
قالیباف با طرح ادعای تسلط ایران بر تنگه هرمز در پی جنگ ۴۰ روزه هشدار داد که «نباید تنگه را به ضد خودش تبدیل کنیم».
او افزود: «تنگه هرمز زمانی ارزشمند است که روز‌به‌روز تردد در آن بیشتر شود، نه کمتر.»
@
VahidHeadline
پس از  آن که مصاحبه تلویزیونی محمدباقر قالیباف درباره جنگ، تنگه هرمز و مذاکرات با آمریکا، در میانه آن به طور ناگهانی قطع شد، مرکز رسانه‌ای مجلس شورای اسلامی اطلاعیه‌ای به رسانه‌های داخل این کشور فرستاده و به این موضوع اعتراض کرده است.
در اطلاعیه مرکز رسانه‌ای مجلس آمده است: «به اطلاع هم‌وطنان عزیز می‌رساند در راستای اجرای امر رهبری معظم انقلاب مبنی بر پیگیری شروط مشخص شده در یادداشت تفاهم اسلام آباد، جناب آقای دکتر قالیباف، رئیس قوه مقننه و رئیس هیئت مذاکره‌کننده کشورمان برای ارائه گزارش به مردم، گفتگویی تبیینی را طبق هماهنگی با سازمان صداوسیما انجام دادند که این گفتگو بیش از ۲ ساعت قبل از زمان پخش به آن سازمان تحویل داده شد؛ اما متاسفانه پخش این گفتگو از میانه آن متوقف شد».
در ادامه این اطلاعیه امده است: «این در حالی است که این گفتگو به شکل ضبطی بوده و کمترین وظیفه مسئولین سازمان صداوسیما این بود که اگر خلاف رویه ها تصمیم به عدم پخش بخشی از گفتگو داشتند، آن را با این مرکز هماهنگ می کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76759" target="_blank">📅 00:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgPDtwQyP33xxWY4nTg-b9CBoMwIDmTxwF4Qd5RYnn3KiUtuKdaFDhkYHlw3c0JNQlTOId9RCMSU8yx_bNXIqOsOudOVftJOZwb9S0BGuBI1AINN-8zNiki-9ZUtWwRvnfwyPT6E9I1Ei9RdsFvRnevuh1KvC0y4RQj71dDXAY3RSst0CsilnceFqQeceSZgXlPhqdRYhETG6tD4JyupCauRBk5AGPLvqqMTSuTf_cV4seOhtCeL9kkMKWB4ILQdUZOpd3bvcfumi0sPiHTQ1T2fM30W14lbJUVZ6zwp1eVUa01O3zIOrrAo5xfkd-EXVz2PWLz1duTeEOJ7tBsuSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌دیوان عالی آمریکا تلاش دونالد ترامپ، رئیس جمهور، برای لغو اعطای خودکار تابعیت به کودکانی که از والدین مهاجر فاقد مدارک قانونی در خاک آمریکا متولد می‌شوند را رد کرد.
آقای ترامپ و تیم حقوقی او تفسیری از قانون را درخصوص این اعطای تابعیت مطرح کرده بودند که تا همین اواخر هم در میان سیاست‌گذاران و کارشناسان حقوقی، حمایت چندانی نداشت وتوانستند آن را دیوان عالی آمریکا یعنی عالی‌ترین مرجع قضایی کشور برسانند.
با این حال، در نهایت اکثریت ۹ قاضی دیوان عالی حاضر نشدند سابقه قضایی ۱۵۰ ساله را کنار بگذارند و یا قوانین فدرال دیرینه و متن قانون اساسی آمریکا را به گونه‌ای جدید تفسیر کنند تا به نفع آقای ترامپ رأی صادر شود.
این شکست احتمالا برای آقای ترامپ ناامیدکننده خواهد بود و او را وادار می‌کند به دنبال راه‌های دیگری برای محدود کردن ورود مهاجران فاقد مدارک قانونی به آمریکا باشد؛ زیرا اگر این افراد هرگز به خاک آمریکا نرسند، موضوع اعطای تابعیت به فرزندانشان نیز اساسا مطرح نخواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76758" target="_blank">📅 21:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76757">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYLI7wctsaTo0pOEGuNEF-Syk5U_qnRiJZfzYoKbl_FvmUeS7dNlvxLAUIGporYjpyA6ICYg8_1cIdocIMP_7trxWjhbY7HOc4pmd-4w1CzSoXm0tHee5eelYtd4zH_0x531x5UMrCDyczHHeJRJJLqxoKGE2C06U_YnzfOvV7fhlSKQqerxELh0TkJ-Gl1FzkKG4IYIf4MdY8HzExINvhqV4EYLPqgNEZhIQRzsMbvncI8KJifh_DWM3nO1Rdu3m5d5HGmJsn2XYmGsisKbqfASChnw8CKtXdS-3J8qlRvBXEjB9Z8FkdCvzQDZSZCgZ5nB1hCiZPzMT8iYxYEVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه قطر، اعلام کرد استیو ویتکاف، فرستاده ویژه دونالد ترامپ در امور خاورمیانه، و جرد کوشنر، مشاور ارشد و داماد رییس‌جمهور آمریکا، روز سه‌شنبه برای گفت‌وگو با مقام‌ها و میانجی‌های قطری وارد دوحه شده‌اند.
ماجد الانصاری، سخنگوی وزارت خارجه قطر، گفت این دیدارها با هدف بررسی «تمامی مسائل منطقه‌ای» انجام می‌شود و موضوعاتی از جمله روند مذاکرات با ایران و همچنین لبنان را در بر می‌گیرد.
او با این حال تاکید کرد که ویتکاف و کوشنر برای مذاکره با هیات ایرانی به دوحه سفر نکرده‌اند و برنامه‌ای برای دیدار با نمایندگان تهران ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76757" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76756">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzuxtXLNB4ZyaqjrVHkJrwcuWlc6PBMbftKmc6zsuQ-BA4w7bl9gWavygozGNt_WxiPtcT-Wivoc6A-oPcJ4oRsBEd3nLgUSp6mmjhpRcnB9IUGwusYs6HgUQTXfIT1MbFGUU4P24KvHs8g6z_EttqXTR_vw9dUsZmDStpEMlL6MDZloTi--qMOvaSBCbUDH9f-t6U326SD5UOrNSD_HgGIHTnA8aLoLk_iivmwfBwvTXjfK1lpljLXsbol3dU3N4S0S1_TcEp6IkKKAs6sozErCcPQ6Zmez_djyiuH35Pb0NVdbSRcOS0wNmkZAGWAUkIh99J9iXLPtrcg5WgBGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه به نقل از چند منبع گزارش داد جمهوری اسلامی تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدودشده خود را دریافت خواهد کرد.
پیش‌تر سخنگوی وزارت خارجه قطر گفت تاکنون ۶ میلیارد دلار از دارایی‌های مسدودشده جمهوری اسلامی به ایران منتقل نشده است.
محمدجعفر قائم‌پناه، معاون اجرایی مسعود پزشکیان، نیز با اشاره به متن تفاهم‌نامه با آمریکا، گفت که چند میلیارد دلار به حساب جمهوری اسلامی در یکی از کشورهای خلیج فارس نشسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76756" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tYeJj3ivvO13ShiTADvoqaW1XUdSDzsGO6Yy6d7qqMg78gHcpev2Jxq-DlZ2--Abebw1Aom4WSSaQE1c4_5EVOBNUuaAQH38gCPBjcREDQgd4mMdwMDalB7UxDmhuCVIvulCrXYmrTFSaG6WvdcvSuoN5ku2sMMYZ5KD3VvGwDMCVKtg5YhNoXKj7R9BQLieGS5bcyDiWV1HVDz5l6Xfw_zz1nyTprKdKNHzrBXrKfAF8PrH8t7CHbcZDfo-kZWmmAu4NE2Jcx-vWl2aGLPoLPHVi3G2k0x393uYCxmFPI-Ato1RYB_woMXxbxeLIWtCU0_HUSXxHckFz5mbtKR4sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XRnG466X8w7oIJ-dH9R1udt1bwSFiyuWIbYprOarWrFrnzxlU1G9oZaJEUW6NyXK6R9yIqgAzzwxOgZqWvtu6G963VfaN294Azo3KAynEyTBIJaRoiuzzOkg5OJ9g9jdWCJ6N0ZIDbms4sO88Zyca2ixJX4tNyo5R-5VyuTDI3XVKrm3VfPOylGuWcSFOg7qxUzFar8suZfWxxEROqjArcE7wjONtoolQv8yQqcV-t91dngHLQFgsGKEImMjQH1FmBaNl0YBKayshCCOh1iI4matNGZ8jtDzWzqFJCFkZ46ES6bVTeSiptotQAbScYz9St-MXAdD1iLPnFODvnu_ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون اجرایی مسعود پزشکیان تأیید کرد که فرماندهان نظامی عضو شورای عالی امنیت ملی ایران و دو نمایندهٔ رهبر جمهوری اسلامی در این شورا نیز به تفاهم‌نامهٔ ایران و آمریکا رأی مثبت داده‌اند.
محمدجعفر قائم‌پناه روز سه‌شنبه نهم تیرماه اعلام کرد در جلسهٔ‌ شعام برای بررسی این تفاهم‌نامه، رئیس‌جمهور، رؤسای مجلس و قوه قضائیه، جانشین رئیس ستاد کل نیروهای مسلح، وزیر کشور، رئیس سازمان برنامه و بودجه، وزیر خارجه، فرمانده کل سپاه پاسداران، فرمانده ارتش، و دو نماینده رهبر جمهوری اسلامی در شورا،
یعنی سعید جلیلی و محمدباقر ذوالقدر، به این توافق رأی مثبت دادند.
او این را هم تأیید کرد که مجتبی خامنه‌ای، رهبر جمهوری اسلامی، دستور داده بود جلسهٔ شورای عالی امنیت ملی با حضور فرماندهان ارشد نظامی برگزار شود و در صورت رأی موافق سه‌چهارم اعضا تفاهم‌نامه پذیرفته شود.
اظهارات معاون اجرایی رئیس‌جمهور در حالی مطرح می‌شود که در روزهای گذشته، پس از انتشار پیام مکتوب مجتبی خامنه‌ای دربارهٔ تفاهم‌نامه، برخی چهره‌های مخالف مذاکرات از سعید جلیلی به‌عنوان «تنها مخالف» تفاهم‌نامه نام برده بودند.
@
VahidHeadline
به گفته معاون اجرایی رییس‌جمهوری، اعضای موافق این تفاهم عبارت بودند از: مسعود پزشکیان، رییس‌جمهوری، محمدباقر قالیباف، رییس مجلس، غلامحسین محسنی اژه‌ای، رییس قوه قضاییه، رییس ستاد کل نیروهای مسلح (که نام او پس از کشته شدن عبدالرحیم موسوی هنوز به‌طور رسمی اعلام نشده است)، اسکندر مومنی، وزیر کشور، حمید پورمحمدی، رییس سازمان برنامه و بودجه، عباس عراقچی، وزیر امور خارجه، فرمانده کل سپاه پاسداران (که نام او نیز تاکنون به‌طور رسمی اعلام نشده)، امیر حاتمی، فرمانده کل ارتش و دو نماینده رهبر جمهوری اسلامی در شورای عالی امنیت ملی.
قائم‌پناه همچنین از منتقدان داخلی تفاهم‌نامه انتقاد کرد و گفت کسانی که به این توافق رای مثبت داده‌اند، «کمتر از فرماندهان شهید نیستند» و نباید جایگاه یا صلاحیت آنان زیر سؤال برود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76754" target="_blank">📅 16:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjfQnMIZBftjUHIx7BpYjcbIbe_cZLo6YKmCxYnfmvv0E9hC77dsU-uKJf3Lt22U1mVeh4e1oDqirAfg7wNTEjYfooKLjZm86aWH8UfHuUUP3bK6L70lwtuSoWMQhBM-fGaFexUBgsZnG80KipHJFuaHb8cs5L-nVfcvxNXYaHKLEhaQsVytIU_0hMc4iAWEJQz8vzLit9s5kg1ImLCCYqKJq2FOIVRjiAkBhTIFBAXmFerIV2LyF_X0C9jSDTIArBMhbQ_VTvXTbHCo-5V2iUCVR8tk6DZXK4D5LvBf9f7vTj1MdfrBDddRxwv-xdcAMpVCa-zCpqu9klEObvqQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این تصویر، محمدرضا شاه پهلوی در جریان بازدید از بانک ملی ایران، با یوسف خوش‌کیش، رئیس وقت بانک ملی، گفت‌وگو می‌کند.
خوش‌کیش بعدها ریاست بانک مرکزی ایران را عهده‌دار شد و آخرین رئیس‌کل بانک مرکزی پیش از انقلاب ۱۳۵۷ بود.
پس از انقلاب، خوش کیش بازداشت شد و تنها طی سه روز محاکمه، با اتهاماتی از جمله «ثابت نگه داشتن ارزش ریال در برابر دلار آمریکا به مدت پنج سال»، به اعدام محکوم شد و بامداد ۲۴ مرداد ۱۳۵۹ تیرباران گردید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76753" target="_blank">📅 16:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76752">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxXDvgl9UF9LMzw7M8QkrQDVGAlHBEKszoZXKs0pYpELLIMRXddVed234OL-QmXouACtruQrZ7WNNlkeb4bLcPCrorhAyDtJ59HimXWYDNxuLRgoMc4WSLC5-8jSUhIG39uV6GVg481D1MfHT83fLEpOc9mynyMlvfQkVFdwzBxrwAFkmw2EzD4R3BkNaDziRQnrm7rwtTyjzuK9Gaae5G3Xd-mFQTsHgBvfYEGqdMcNc_aimJ0KJAZbXPAjvo1YsiZsYRreOZ_jPoAmnd-c12faSztXtYcnhZVjOjU4liL6jgEshCHV_gosoQqxWdD-AyNIA9TLmrk4QaEFjq60sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان مخالفان داخلی تفاهم‌نامهٔ ایران و آمریکا را به «همسویی با عملیات رسانه‌های معاند» متهم کرد و گفت «تمامی مراحل مذاکرات» با «هماهنگی کامل و مستمر» با رهبر جمهوری اسلامی انجام شده است.
رئیس‌جمهور ایران که روز سه‌شنبه ۹ تیر در دیدار با اعضای جامعه مدرسین حوزه علمیه قم همچنین گفت: «با وجود محدودیت‌ها و ملاحظات امنیتی موجود، متن نهایی توافق پس از بررسی‌های کارشناسی و امنیتی در مراجع ذی‌صلاح مورد ارزیابی قرار گرفت و در شورای عالی امنیت ملی نیز از حمایت قاطع اعضا برخوردار شد.»
این در حالی است که در روزهای اخیر مخالفت برخی طیف‌های سیاسی طرفدار حکومت با تفاهم‌نامه بالا گرفته و می‌گویند دولت، محمدباقر قالیباف، رئیس هیئت مذاکره‌کنندگان، و حتی برخی فرماندهان ارشد سپاه برخلاف نظر مجتبی خامنه‌ای این تفاهم‌نامه را تصویب کرده و پیش برده‌اند.
مسعود پزشکیان این دسته از مخالفان «جریان‌های همسو با عملیات روانی رسانه‌ّای معاند» خواند و گفت: «این‌ها تلاش می‌کنند با تخریب تیم مذاکره‌کننده و زیر سؤال بردن تصمیمات ملی، زمینهٔ تضعیف این دستاورد را فراهم کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/76752" target="_blank">📅 16:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76751">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQ4PbkttOwFegIQTGs4YYNJFIZkAisHi1lUvcVOlX1WzqLxieq4XneCOqpkMlhInz-MmFgVEXJGCs8pZinWkqc-0ntHW4XFgMXmMyvXOJACHbn97CYUC1JXRKbhns3gD62VIi2qrrRWAKWIF2Ip34qCAgTxFfjiFmA1461zoPAXzdLBeHynFmcvY1-R3SO1m6bXgYPErQa3FV3yRVO52hAok-k3D_Djfnl--e9LwWU-o1f-PArxanXMOdiUbRuk6HeEkW6mI2KRDVjDkNv_wUUHZ4YZP2t5dAR5twNpV_0eV2vGBVjb8R0h0aSSLOLctE4p3t1b8BPC305fdE1EVdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۴ روز از آغاز اختلال در شبکه خدمات برخی از بانک‌های کشور از جمله بانک‌های صادرات، تجارت، ملی و توسعه صادرات می‌گذرد؛ اختلالی که همچنان به‌طور کامل برطرف نشده و ارائه خدمات بانکی را با مشکل مواجه کرده است.
در این مدت، گزارش‌های مردمی از تداوم کندی، قطعی و ناپایداری سامانه‌های بانکی حکایت دارد؛ این در حالی است که مسئولان بانکی در روزهای گذشته بارها از رفع یا در آستانه رفع بودن مشکل خبر داده بودند.
ادامه این وضعیت موجب بروز اختلال در انجام تراکنش‌های روزمره از جمله انتقال وجه، دریافت حقوق و پرداخت اقساط برای بسیاری از شهروندان شده است.
هم‌زمان، کسب‌وکارهای خرد و متوسط نیز با مشکلاتی در دریافت مطالبات و انجام پرداخت‌ها مواجه شده‌اند؛ موضوعی که به گفته فعالان اقتصادی، بر روند فعالیت روزانه آن‌ها تأثیر گذاشته است.
در همین ارتباط، محمدرضا عارف، معاون اول رییس جمهوری، در جلسه‌ای با مدیران بانکی با اشاره به اختلال‌های اخیر گفت: «آنچه در بانک‌ها رخ داد نتیجه سهل‌انگاری در حوزه امنیت سایبری است و این موضوع قابل پیش‌بینی بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76751" target="_blank">📅 16:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76750">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ucX0sIqdmMpyh05_rJqjJM6saqKtqEQCEfLOFLmY3pLiE35f4vgTfkMyOGvuHkEiNtNX_uaUIiO32QqYtxLlt-zZYBvg6jwZDJciv8-Z24JqxTiCrekrV-ZSixH54JOoE93VcayFpcOXQXKGMhDy09vwSjcqRrZpZWcSgWxJPsPQQgvRzOr1Htzj7YvlKxkQkQJn--2FQ9ULrNf31c4Ka2mMlMojQ0rjoEuBvg8cnfaz7oQK6kW-2NpkMXMJVTcGBkrmiVBpFAYqHqiOW0krfnVmc9ua65EJsmx1H-5GzY-cqyNqRya9HNm6kvcyRVeGa__RYfJ5TUy_U2Vd-TSetw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضوانه احمدخان‌بیگی، فعال مدنی، جهت تحمل ادامه دوران محکومیت حبس، به همراه فرزند خردسال خود راهی زندان اوین شد.
براساس اطلاعات دریافتی هرانا، رضوانه احمدخان‌ بیگی، دوشنبه ۸ تیرماه، به همراه دختر خردسالش، مهفر لاله‌زاری که زیر دو سال سن دارد، برای تحمل ادامه دوران محکومیت حبس خود راهی زندان اوین شد.
این زندانی سیاسی در تاریخ ۲۸ شهریور ۱۴۰۳ جهت زایمان از زندان اوین به مرخصی اعزام شده بود.
رضوانه احمدخان بیگی و همسرش بهفر لاله زاری در دی ماه ۱۴۰۲ به اتهام اجتماع و تبانی علیه امنیت داخلی و تبلیغ علیه نظام به ۱۰ سال زندان محکوم شدند. این حکم در اسفندماه همان سال تأیید شد و بعد از پذیرش اعاده دادرسی و رسیدگی در شعبه هم عرض به ۲۱ ماه حبس کاهش یافت.
hra_news
فرحناز نیکخو، نیره بهنود، میترا برمچ و زهرا (هانا) غلامی، چهار زندانی سیاسی، پس از پایان دوران مرخصی خود به زندان اوین بازگشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76750" target="_blank">📅 16:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76749">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tG1g-_vFGyGekEeu3_zw0eU3iTJL2y7qlekdtbgFJ8WEQrPObuRopprYqLed36OVBvYEHfeJ2gvr0ksGMtufBb7w9dOoWagaJeCh87H14R62td1Fef7RshtRgajWyWSHn4v1Fm44CeKLq4SYQEXKjjHes-kRZ8Es4PAwzyt_u40J6HAhcIJilsBgDMTt3GbdnwG0w1pOhdhYCmpz_n0Q3d5gbpK8BnhkpyLMeGHzlIU5gUz0yi3f72I-cY-83wa9vOeSkAALHtN04onrB89iB_5AmztC9LNuDGpUgSJm9U3TXbpobJuxMNwrOPU4mD6_I7WTJBXWHRdhpbiL1UJfVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه استان کرمانشاه اعلام کرد دو تن از نیروهای بومی سپاه در شهرستان پاوه شامگاه دوشنبه در پی تیراندازی افراد مسلح «به درِ منزل‌هایشان» کشته و دو نفر دیگر زخمی شدند.
بر اساس گزارش خبرگزاری مهر به نقل از روابط عمومی سپاه استان کرمانشاه، این حمله مقابل منزل دو تن از نیروهای سپاه در پاوه رخ داده است. در این گزارش، عاملان حمله «افراد مسلح تروریست» معرفی شده‌اند.
منابع رسمی هویت دو عضو کشته‌شده سپاه را برهان کریسانی و خالد خالدی اعلام کرده‌اند.
همزمان، سازمان حقوق بشری هه‌نگاو گزارش داد که این حمله را گروهی تازه‌تأسیس به نام «خوری هیوا» (خورشید امید) بر عهده گرفته است. هه‌نگاو نیز نام دو کشته‌شده را خالد خالدی و برهان کریسانی اعلام کرده و نوشته است دو عضو دیگر سپاه در این حمله به‌شدت زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/76749" target="_blank">📅 08:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76748">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMFTz-JJBtXbp3iP4L1H4ltFa8bfJ2GCSxC8wGFvxI-GAeh1LIaIwF5_-GrqREpzYZfq-s4L08QKMugWWwa6o3i2vekUknWQdsVtyHVdBFsO2M4O5sS1v6L8OxqTnQXWt7tr9D4kb2UUjSbfBUkWrW1S0i9woFa7LbkbTwY-Ho21XI6cH9mHWUCRYo6cunzlBawy_NzwTEixUiujPZPObI1JWC9P3XhAL-jqcKyhlmD-t64nkcIivyMfJPYURiB8JucGkTFL47lxAM2XYuh3ccEw0FAwAunWimcuRc0kswMBumqyN59OIveEtLVypH_7KmK1CuC6YbS6qRp3WzUgUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت امور خارجه جمهوری اسلامی، روز دوشنبه انجام مذاکره با آمریکا در دوحه را رد کرد و گفت در روزهای آینده هیچ مذاکره‌ای انجام نمی‌شود.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، از درخواست ایران برای انجام مذاکره در قطر در روز سه‌شنبه خبر داده و سخنگوی کاخ سفید اعلام کرده استیو ویتکاف و جرد کوشنر به عنوان نمایندگان ایالات متحده عازم قطر می‌شوند.
بقائی در این باره اعلام کرد: «طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و این‌که نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.»
او در ادامه توضیح داد «هیئت کارشناسی» جمهوری اسلامی این هفته برای پیگیری آزادشدن دارایی‌های مسدودشده ایران بر اساس بند ۱۱ تفاهم‌نامه امضا شده میان ایران و آمریکا به قطر می‌‌رود.
ساعاتی پیش مسعود پزشکیان اعلام کرد که «شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76748" target="_blank">📅 21:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76747">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pcndxsElk4Ejl4lIKiDOdefByHBxRjEnggGBB4ku_kMpgOpFUx8Q_fKd5i0UaF68RkXPrxHKifCbsAI2JY3FzLiZV_5R10HEMJcSoGoI8HJNqWQXvn8t43XXaYMosNdGDGXdDkhewHmDheonakntjb1smnfDakFTmxN9Pqpzbzt4zzPV4CQKYCrPXn1DOtFJXDNC_3Y3N2iUJ8cB2pGV2m56IQxGKwQX-N-PkJ0uJGfWLtEHL6CCE3eiRba34CfbzvuErom9B-h0nFcWMuhVvjisSApUMwUagDAl3RfVoX1Yx919XovkhJGVUNO85jokyvR35uYGhDETE_7ZyQWj8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، گزارش داد محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه پاسداران، در یک «سانحه رانندگی بر اثر واژگونی خودرو» در یکی از محورهای استان کرمان کشته شد.
فارس نوشت پس از وقوع حادثه، نیروهای پلیس و اورژانس در محل حاضر شدند و اکبرزاده به مرکز درمانی منتقل شد، اما به دلیل شدت جراحات جان باخت.
این رسانه وابسته به سپاه افزود بررسی علت و جزئیات این سانحه از سوی مراجع ذی‌ربط آغاز شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/76747" target="_blank">📅 21:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76746">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geZupfH2E2aQsmDpjid97p5E-2XgqhdK0D7jWDZQQL8_MhEz9Ds2e2qxV9gpZSUDaTc2hUoNYfnHbWHamTnASwuODG1Vl6I11ONep5yGbeeBRWtzTZo3Aw7YHjSw1vqeRi3peND5Ea8oo3qMJwDgqTWRwa1AEXyTPdGDT8lgTk014RZAAGEOy9wTGaDxE0h6pqMn0hfylHLQIpdlDde4H8PHmcNAMD3otQrQW6qBtjnTP9mZEn3czUtEUX1UxgMNd48z4r0i_n3e4ANmlm2F3iqNu28EnrIpKqCrjIKsgpbaGkw2_SMzaXeUySIHXd_MEDbknphAP-LOWcpRswIf0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف میری، ۱۷ ساله شب چهارشنبه سوری در خیابان حافظ اصفهان با اصابت گلوله بسیج به سرش کشته شد.
یوسف میری سه‌شنبه ۲۶ اسفند ۱۴۰۴ هنگامی که در راه بازگشت به خانه بود با مادرش تماس گرفت تا برایش غذا گرم کند اما پیش از آن که به خانه برسد با شلیک گلوله به پشت سرش کشته شد.
یکی از دوستان یوسف به ایران‌وایر می‌گوید: به مادرش گفتند به اشتباه به پسرت شلیک شده و اگر جنازه‌اش را می‌خواهی بهتر است سکوت کنی تا جنازه را تحویل بدهیم.
دوست یوسف همچنین توضیح می‌دهد: مادرش مرتب یک جمله را تکرار می‌کند که بچه‌ام گرسنه و تشنه بود می‌خواست بیاید خانه شام بخورد ولی آن بی‌رحم‌ها نگذاشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/76746" target="_blank">📅 17:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76745">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eHnHyIYjZBMccWr4tJLn4-nA0Mm04L94CjglB456NiDeL7xRITyS_nxxO7BntlAtRrVBFYQOiuJoJ0KukC3DSdwds6vOQe3SSbEtKoomWcMh75Ys9EL6kro37GGzPpyvVQfw8fRVHAijya2sBseHdTeOM2Lgp9_EKcPHCnys7W03c7HFjYco39MloqZ9lVg86CFGM8jqWhBaIXAsyYhFro8Bn_srQPsYxVbTg96Xvy4r8G3yNt7zvEqINq0teNJ2bqA5kG68rFaPgoGfLJwtTDY5OYCWccsSX9G4OENZucIdIYAvYTXNpMI9cTHT8sUBg-W3Bg0DxwP7QYth3a6JjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدر البوسعیدی، وزیر امور خارجه عمان، روز دوشنبه در گفتگو با رادیو مونته‌کارلو بین‌المللی اعلام کرد که این کشور به آزادی عبور و مرور در تنگه هرمز و اعمال نکردن هرگونه «عوارض تردد» متعهد است. او تاکید کرد که اعمال چنین هزینه‌هایی به‌طور بین‌المللی ممنوع است و عمان به این مقررات پایبند باقی می‌ماند.
این اظهارات در حالی مطرح می‌شود که ایران نیز از برگزاری جلساتی میان مقامات تهران و مسقط برای بحث در مورد مدیریت آینده این آبراه، طبق مفاد یادداشت تفاهم ایران و آمریکا خبر داده است. با این حال، گزارش‌ها حاکی از آن است که دو کشور تاکنون پیام‌های متناقضی در خصوص عوارض و مسیرهای تردد در این گذرگاه حیاتی ارسال کرده‌اند.
وزیر امور خارجه عمان همچنین تاکید کرد که مسئولیت اصلی تضمین امنیت تنگه هرمز و پاکسازی مسیرهای کشتیرانی بین‌المللی از هرگونه خطر مین‌گذاری، بر عهده جمهوری اسلامی ایران است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76745" target="_blank">📅 17:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uhZ-9oXWitZhFHAZss_XtEVXah8-L-I0sFjQSpFkTy30QQPiRy0nLMhQ_-LgHFBhdxSCwfzZrGW2hZkWkxImRkmm8FhBIA0CJmmTmcJUk34-0Gbu3xZfZEJXvl3W6fEMhy0bj9eNdACKX9_EhgPOHtd1mH0VB5srVfLbl_Id3pjv7fA2lZlycHNNVAnQXtwKnyCalvDQO7LApt3FCL0RqzqUiw1s-BWOSu6S_wmm4LRwi5Tx3ckIclWNIo6LWZx1OqZClroy4jYO7Pt5oMdHUAWSCyd8y3P78dwZKPE9uak9jwoMyjWriedGJz299qAsX52CqytgEdbi7_TZ3D_9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AcOCtec57rmQylKpagq9LUkDwxBrsxVMyhgBW-cZnkAdT31gx5nI8pliI7Cz_VtwnxJWFu2gsrO_LdEhg1NiIvLN3Yc1pPBoCKZzevamY6t8u95J_YyQFvph78mDOLdVw3_h-tlxsEnjxVNhkWrcV5yQnLecAVEyImzHCSBty9mH2D4iq2S6lmyWbQmnpNcwXYhe7k_UX4bGKrdegcT5rNFsvChv-D28-bkpo_G4880AqU3OEJuiuUGjVfO83SBbzco6xpmAMLBdHCY-JRhYSVsuK8nrz7VYRcOcf6XKpJ9ywHrhHV3sANvx3dStMpNE0GSjhRk6hihoROACbSYafQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست عراقچی با فوتبال، ترجمه ماشین: از زمین فوتبال تا میز مذاکره و تا میدان نبرد، هر گامی که ما ایرانیان برمی‌داریم، بخشی از مبارزه‌ای بزرگ‌تر است: دفاع از شرافت و کرامت مردم عزیزمان. araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76743" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76741">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MpvDI1Ti0AHYY_lW2m8JBpHI9xs_q--GnYbCCgy3l5-WmzlECEUlQZuTvd9wTDJsr2IvP7XJWs1-Je_cs3ipfAYQckggZh3Ym2_tOGvKBt_E_HozWiuwRkzfGGQ1BeWCa_W-0_BsIS8d26yI4nWkVMuYgXsZ68UL9xXx0zoi3OCZRU7KKsFech_q68UCsLkkRwO5BfHXRge6jzVHgazyMi2nsOR5WMM8l76MPqUsuOATfr_nx0KNsyYfwkG1pwsy4x5hSco_0ZXp-rGSCGwueMyXzY414Z8uBKhfFPHaXL2hwn6r7xcJxdygSNzOYQ3D9eO_bry0ssiM8GKuiHy_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bJde77ojep_24sYgAojMDSd-_rfss-R5q2-jDCHkYXvQbXafhCbJlhyOaJ0w76Vc-j-_RGyHHQO5Wn6Xrb_68SEh98bimcbHqkgxgGDVRDxih67OoXbaG4eHDpmrixnHeb2Mm1dxHKF7CIppa7XCJ6ZFJZAXDaL8rCNd7ebiaVQTBnFSzQ3CvdM4G_lvV-D_UlhTDaUUcpUKfdzQQ-QJhThfL8ZIB0XiaSuPFz9muLgSM0HKFhMQzOfEY-tAU-yT0ahAwg5g3QaVj0Rrk_ig0z-gshUCj7o5dFDvpOLtBb9ff8GnwYmSoYr8MPBn9JO5w10y8Z_WZyYdGKU6dENefQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پستی نوشت: «ایران درخواست دیدار کرده است. (این دیدار) فردا در دوحه خواهد بود.»
پیشتر کاظم غریب‌آبادی، مسئول تیم فنی مذاکره‌کننده جمهوری اسلامی، گزارش برخی رسانه‌ها مبنی بر برنامه تهران و واشنگتن برای مذاکره در روز سه‌شنبه را تکذیب کرده بود.
کاظم غریب‌آبادی، مسئول تیم فنی مذاکره‌کننده ایران، امروز گفت: «هرچند رایزنی‌ها با قطر از جمله در خصوص پیگیری اجرای تعهدات طرف مقابل، طبق روال، در جریان است اما خبر برخی رسانه‌ها مبنی بر برگزاری گفتگوهای فنی کارگروه‌ها در دوحه تایید نمی‌شود.»
او در ادامه گفت که «اولین دور گفتگوهای فنی در چارچوب کارگروه‌های تعیین شده، با فراهم شدن شرایط و پس از توافق در خصوص تاریخ و محل آن، برگزار خواهد شد و رایزنی‌ها در این خصوص از طریق کشورهای میانجی ادامه دارد.»
@
VahidHeadline
«کارولین لیویت»، سخنگوی کاخ سفید اعلام کرد «استیو ویتکاف»، نماینده ویژه رییس‌جمهور آمریکا در امور خاورمیانه، و «جرد کوشنر»، مشاور ارشد پیشین کاخ سفید و مشاور غیررسمی «دونالد ترامپ» در امور خاورمیانه، روز سه‌شنبه در نشست دوحه با نمایندگان جمهوری اسلامی شرکت خواهند کرد.
@
VahidHeadline
ترامپ در پستی دیگر نوشت قیمت نفت خام وست‌تگزاس اینترمدیت به ۶۹ دلار رسیده و رو به کاهش است.
ترامپ در این پیام نوشت این قیمت از سطح پیش از آغاز «خلع سلاح هسته‌ای ایران» پایین‌تر آمده است.
@
VahidOOnLine
🔄
توییت خبرنگار اکسیوس:
به‌روزرسانی: یک مقام کاخ سفید می‌گوید فرستاده ویژه، ویتکاف، و جرد کوشنر امروز به دوحه سفر می‌کنند و روز سه‌شنبه با نخست‌وزیر قطر و دیگر مقام‌ها برای گفت‌وگو درباره توافق ایران دیدار خواهند کرد. روز چهارشنبه، تیم‌های فنی آمریکا و ایران به‌طور جداگانه با میانجی‌های قطری و پاکستانی دیدار خواهند کرد.
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76741" target="_blank">📅 16:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76740">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4sCUCy-_LIkXwACl72laCCD00JrrsLzMTxNLQiBgzIkuGCSc3UbjvTo6tgd-u6097tArVx_I4AjDjjSJgTMVUlFtp9h9RMSoFplzO8a4FZOufQ5akWEhzAj5CheZ78yYzcjfJCV80d5BnGsAR-x7c-s8P-UOb-iSqopHBy19xj9kXAWAoR-ecnkWe9fmFO1XoVhfXrSKheUa2RrIDt6gaO4N-vx_IjMJkw7-ESFLIvJLxCKZ-EA2n8oOeN599bRKa9CkyTViUlBxhSM1NTMfKglCAGWlG3lyvwVYPLJvKMMcIyoAuHNsbr67Z5GaSrhIVhgwpiSBL-2gUgeIKpbtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری اسلامی ایران روز دوشنبه هشتم تیرماه گفت: «براساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد».
مسعود پزشکیان در دیدار با شبیری زنجانی از مراجع تقلید شیعیان در قم گفت: «برای بازگشت بخش باقی‌مانده این منابع نیز پیگیری‌های لازم در حال انجام است».
او زمان مشخصی را برای آزادسازی این رقم اعلام نکرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/76740" target="_blank">📅 16:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76736">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SE0IyHtv_Q5IitxRvQSI4dP9g3Yxtm_QBkOH9EOMU50MZFCGzeGuqeKq3mXOnyLubENf2DfTx12_mMTlMj_hiowb20un6Rq-WS9JKDK6bNNp1a_7DA0FKNhICYkZgL358N9oGe8aBGIpl586qN_jdOl-b8sW8irynX9eF4LuXgpJh7jwZN0ABvcKfK4YrfE635JgMn8rz-QPp3aWYjoyZpJAhNxKSA3WVLYz4jscs5votVEXVgBx4L1pKoY60OpNRLMGMr_qs4g0I9phGzQVsy7OOpOjXFVQ2FQ4om7iQTU0vZkDmWN9W5MCAkuSFuTy65GXBWo_NjxX2VYwupm8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FKSTyXj3HUqjDMtpVaBTr7xnJ_gEnSnizjrP1m1dtmujiIlLmLoPmLUac5uKi65FSe7TfptObmgL97frwu4iLmCBbIpErX4uy55HVQUPDTDgJaaBKjsJzkC-UWame5MlEbs4-wgxXRx57Jdu91evBNa5PFVFCNxWa8tc70fZLpI92Exr-EEsfRmSwcPf-8IWBYasE7wvoqfI5zRXOX83B2WGqWKn2Pr0bXhe9p05Hvw6FZUOvWM1LTM2VaRZsYX4zOHcgoDhNbKEs0ZyNd7Uc06c0SN8HGuXn059WMoEYEZXtezzW-3k6QXDqWJlxBAiLxJizxnmq2d_wfngcSkLlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fZnoMXI-FlIP2Ro3VTXZX4LteU-QXP01hHpGuoasLtc78yiIi2QhAKOpXn3tzg7_id9ErEGUUtDOdlHEosQcLgfxlHXjJXet1JxA6L444tdSNMEGx6Y1r2vUCGiuaFlqcJsatvXeyM8vTghZK9WvDbdQ922VSlgQO8qsNaFIlNWrAYa2Y4qVvQvajomnd_yIhIWSJgufecwL2Vq2x5LM18dgf6Cb0Ep-4ieh8edPE4XuObsYKmy3wbuC6JQGNCuJcbgF2-BynXm1i0FhoKAJmyn5Nsp_ekRaoWPL_bJv4u2kAswLbdNhXC7b8WkqiV_RJX-5SDHH7gSYBD42-Uoi4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b61d44fd1.mp4?token=GXmIs58GsAvh54dJY7BD8rllkdXTkm6sShCW0HlFBs1_3MODrA0iwKcfHQnMuruPpE6f5phai4IQtDQX-9trrnu3D0J0EIs67O3XXnVywBBMyBgdlv7hI34b3h4sWJc13oHpkBfds3Ve1NOPZjIPBEpauaKCpEKmg7MWSNG-D1eLbbd1_TvUxcHEv3JlHAnyUgu-hiIHyMPyFBEXbc8QcYkCS7IXcyJmqT21bW7tyxKfk6tOUV3MraGcYzqks5qTsyGWvipZ6F7upEnOODgMXDVmptMYTG8pAyeZnOkuT5BVEzEDsn27ZsH06PXx4EsS-LQBj6qWKzlCg95qnGT3QwCt07ro6x5vZpfXuiTI-CGSbj316NP-DyXNGnnJdHKOjYY_XpelPYNRLtQUi7rQGkBTgfhmbOQl6u1zjzhUnU5DZI5Rd7W4LR0BcTei9kttIX6PYEwS088hKUggt_FJr0fq9p7LoyKqYlwNkvh_h1aohMiHCNzkpF4y0Uvy3ijUKaGhYp8x_Ta7fnp0AZM4zBHKyGi9FYQ_fTAM35HBck1q9rgg2AlhKM9Az4yMhL8Ac1rQicgFh-xpyatx4TBZ2OziATDr6YEBrihtue30xteR9rA_bm57xVPgGcb-69Ij35VSntL06-l-NO5_uxpyH_uEWzDKrGQDota4AoJRJ6s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b61d44fd1.mp4?token=GXmIs58GsAvh54dJY7BD8rllkdXTkm6sShCW0HlFBs1_3MODrA0iwKcfHQnMuruPpE6f5phai4IQtDQX-9trrnu3D0J0EIs67O3XXnVywBBMyBgdlv7hI34b3h4sWJc13oHpkBfds3Ve1NOPZjIPBEpauaKCpEKmg7MWSNG-D1eLbbd1_TvUxcHEv3JlHAnyUgu-hiIHyMPyFBEXbc8QcYkCS7IXcyJmqT21bW7tyxKfk6tOUV3MraGcYzqks5qTsyGWvipZ6F7upEnOODgMXDVmptMYTG8pAyeZnOkuT5BVEzEDsn27ZsH06PXx4EsS-LQBj6qWKzlCg95qnGT3QwCt07ro6x5vZpfXuiTI-CGSbj316NP-DyXNGnnJdHKOjYY_XpelPYNRLtQUi7rQGkBTgfhmbOQl6u1zjzhUnU5DZI5Rd7W4LR0BcTei9kttIX6PYEwS088hKUggt_FJr0fq9p7LoyKqYlwNkvh_h1aohMiHCNzkpF4y0Uvy3ijUKaGhYp8x_Ta7fnp0AZM4zBHKyGi9FYQ_fTAM35HBck1q9rgg2AlhKM9Az4yMhL8Ac1rQicgFh-xpyatx4TBZ2OziATDr6YEBrihtue30xteR9rA_bm57xVPgGcb-69Ij35VSntL06-l-NO5_uxpyH_uEWzDKrGQDota4AoJRJ6s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مبین یعقوب‌زاده یک سال بود که مادرش را از دست داده بود، زمانی که  تنها ۱۷ سال داشت، در ۱۷ دی ۱۴۰۴، در اعتراضات خشکبیجار رشت، با شلیک نیروهای امنیتی کشته شد.
🔸
سرگذشت کامل او را در یادبود امید بخوانید:
https://www.iranrights.org/fa/memorial/story/-9117/mobin-yaqubzadeh
@IranRights</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76736" target="_blank">📅 16:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76735">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ac12c0761.mp4?token=pb2D0a_Lm9PEeWymKLreDDX1tWuSsqyISLsfC_I_GOm5YFtdxqmBpwKeCixqP4JR6ID92YQq7KRS_pe91CjXPJIBCxWv-2ee-WkaFNd6Xnm-8zlG8mpHnbbz0IrPuorRUzX0x3WXaaCy8deyRz-6Xnfm0D_90YrBUmluqFYvOep9St2goXpJ94ZICKdKzHNvgZHIVrvo5vdiXVCJYdIgNARYhtUk3rGmLdQzC6tK-D300vDD52hYVLjfrPsCLYChBISMAGVqPIlQqcE0sUhTo708sRls2LSrlNjdMt2x3QApEmzqo2g_pqOjM69zksJrVFG0TCwpzaivG2NbDvwdSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ac12c0761.mp4?token=pb2D0a_Lm9PEeWymKLreDDX1tWuSsqyISLsfC_I_GOm5YFtdxqmBpwKeCixqP4JR6ID92YQq7KRS_pe91CjXPJIBCxWv-2ee-WkaFNd6Xnm-8zlG8mpHnbbz0IrPuorRUzX0x3WXaaCy8deyRz-6Xnfm0D_90YrBUmluqFYvOep9St2goXpJ94ZICKdKzHNvgZHIVrvo5vdiXVCJYdIgNARYhtUk3rGmLdQzC6tK-D300vDD52hYVLjfrPsCLYChBISMAGVqPIlQqcE0sUhTo708sRls2LSrlNjdMt2x3QApEmzqo2g_pqOjM69zksJrVFG0TCwpzaivG2NbDvwdSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
صدای بلند)
ویدیوی دریافتی با شرح کلی: "جنوب کشور، جنگ اخیر"
انفجارهای مهیبی در یک اسکله رو نشون میده.
از زمان و مکانش اطلاعات بیشتری ندارم، لینک یک صفحه اینستاگرام رو فرستادند که نسخه اصلی این ویدیو رو دیروز بعد از ظهر بدون هیچ توضیحی منتشر کرده و پست دیگری هم نداره.
Vahid
آپدیت:
در پیام‌ها میگن خرمشهره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/76735" target="_blank">📅 04:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/spik40YZ6jX42WMNd2F3WUKMD4P_M75LnN8rAVSOu9bDlvTK3d9LgwotSjrN0h5MJu-ZHeHHtgcbK3fLBlpPpiZ--bqV5uG7EQu_w3S1oFdp3Ga_z7ULqF1R3Dpr33PEK5ZnKZHaynCR537v_OwMlEshEFcL1eP0PtcKvfWjEB9UdLZv-fCBEg6PzPbWaggn9CXSGtBXqhoK6_c7LVr5Zga6aW3NqvrTra0SPQs3QtFS8gIS1cvS-jd_kMxRIZ9Y65afqU4edqodaeGUa_BSZDTfoQOAHtI_SbkBTGAIvMVj3oVp829YihXj7Ib2xV1yKXyxHUgUo2Cs9ZEYo02hLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس در نخستین ساعت بامداد دوشنبه هشتم تیرماه به وقت تهران (عصر یکشنبه به وقت آمریکا) به نقل از یک مقام ارشد آمریکایی گزارش کرد که ایالات متحده و ایران موافقت کرده‌اند که حملات علیه یکدیگر را متوقف کنند.
براساس این گزارش دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر دیدار کنند تا به اختلافات خود در مورد تنگه هرمز رسیدگی کنند.
براساس گزارش باراک راوید یک مقام ارشد آمریکایی گفت: «ما تصمیم گرفتیم تمام فعالیت‌های «رزمی» (جنبشی/kinetic) را متوقف کنیم».
همزمان یک مقام دیگر آمریکایی هم به آکسیوس گفت که هر دو طرف «فعلا» عقب‌نشینی خواهند کرد و «شناورها می‌توانند آزادانه حرکت کنند» چرا که قرار است گفتگوهای فنی ادامه یابد.
هر دو مقام آمریکایی و یک منبع سوم آگاه، دیدار برنامه‌ریزی‌شده برای روز سه‌شنبه را تایید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/76734" target="_blank">📅 00:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uBuXN70NAK_KNUpQfSWVhrOJ3B1Dc7E0QX-r8bED3m9cWIOdquivLVM7VqR5eXKIeZaubjb30dk5OALehaPuMEVt-etzdfjAL56mlDwJ1z1SyjkY9DMOiqGNRAAclFu3Iv7Wgq7zY7hDag03pvnPFoOErTOgWM7YMcCd_cMqpvvOQOCcb2MGhn3qg_qm-OtBZFypvyht4xXJEBT4G0TKZns7wQpFm3qCb9BIwal2LvDTkNWaK5WfcndR1Bt9zo31ghbgbdMg_eECZbatrfmlnvSGrSSCAuscYLKj0ENM9VcTOSHZDjJwLyRu8DKrll76U5pQlMVonqYs7bYGD_80lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از آن که روز شنبه - ششم تیر - نزدیک به سه‌چهارم اعضای مجلس ۸۸ نفره خبرگان رهبری در ایران، در بیانیه‌ای شبیه «فتوا» خواستار گرفتن انتقام کشته شدن علی خامنه‌ای، رهبر پیشین جمهوری اسلامی از دونالد ترامپ،‌ رئیس‌جمهور آمریکا و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، شدند، دبیرخانه این مجلس روز یکشنبه - هفتم تیر - در اطلاعیه‌ای، این بیانیه را «نامرسوم» خواند و درباره آن توضیحاتی داد.
در بیانیه روز شنبه که ۶۳ عضو مجلس خبرگان آن را امضاء کرده‌اند، آمده بود که اگر «مسلمانان متدین» به این رهبران آمریکا و اسرائیل دسترسی پیدا کنند، کشتن آن‌ها «وظیفه شرعی» آنان است.
اما در اطلاعیه روز یکشنبه دبیرخانه مجلس خبرگان آمده که هیئت رئیسه این مجلس مفاد منتشرشده را «غیرمعمول و نامرسوم» توصیف کرده و اعلام کرده است که محتوای آن به بررسی و بحث بیشتر نیازمند است.
به نظر می‌رسد،‌ اطلاعیه دبیرخانه مجلس از اختلاف نظر و شکاف میان هیئت رئیسه و بخش مهمی از اعضای این مجلس حکایت دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/76733" target="_blank">📅 20:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fhgXGlnIdz5VYdgqYoiCwIqBoayITEnozLcUBqL7xTW2JHptKECc41uEkxHeZSAQa215KmW3ZNcGsppuMpo9VSBPDdEekJc7kYUof8htjY2E8asHjkj2TDFhc49jHLKokexx0ogZ-Hre3htM6v3og70OtLE1JUt3tr-fy4h2_CsM73hBZE41oWa0MCFWeEW71Jj9sdp3PehcNUpJdawiqqToZ6qI4oPu4CrwhoKjSWmmiUBbA40MrVZW5GDrxUkSDJpUmyzK5m5KpPY0PyAGyXl060cRxup5iaHF_S0sYSvFsgsZDveqOJLdl5LDLRRopQSpcEuC2Zw4bLQw9k1RKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LO9nNP8G7pMmu_zuZ2VmbSvghJVQo-DgTSWxQsM3XoQTQOtoe7WO7FYhcJx2-LKjCmd6y9cmpdtPTXwGu_ZEfW3F3dlvvTerOuOOWla4txXYp1V2oppuEu7M-BWFi6L36NzBm_jzl1L0mk9TVNcgGXGCi-ICa6HpIuVMb4pseMtlfepiW1S9oXl7MiYZPYMCsU7fRA9hP5KjAE0CC5U20OZhAmwj6j3ZHBKxST4-20NGuqSDJQWTKY383QEKrhRd-vOa8iLh8S8T2h5SCwhPfh1ZzT5UHkA5_FEsmhf6h-puPc-SNhPd0PCw2651gH3c0AugmtZ4db6s3fgyZKDvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KouiRF6L2FXp0g8qyyTqKCXMiEU6WFmsnqcrUYD1WR2Wi0Ywm771rE72e1k7DWhYpMuDtjzGRMD9a1_ZjiyFEbE-fYVfzhmqYG5eMfdn3vnDb4RXL_UyRQWiuXgB-BOUzw4dWAQtypDYHe12LZGZ1scQ_4khjoew3CvBGjKLKNH26gbU7X5AdY2ED5tq_bR4Yz4uo13BtNJAFd7-QVwCRTZQT2TZ2gqesAo21XkoxtNsm96g59dWd67bxGxAIhD2DN9EUWpUegcvWVt1qmMYgMEAvZikhodm3lwuqVYOY458EGtSSi8dSANUKgsQyzwW-5TZOkPKS59Juws72BxqOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بحرین گفت که یک ساختمان مسکونی در استان محرق هدف پهپاد ایران قرار گرفته است اما مجروح یا مصدومی گزارش نشده است.
تصاویری که دفتر رسانه‌ای پلیس بحرین منتشر کرده است خساراتی را به طبقه فوقانی یک مجتمع آپارتمانی نشان می‌دهد.
ایران بامداد یکشنبه اعلام کرد که به تلافی حملات آمریکا، پایگاه‌های آن کشور در بحرین و کویت را هدف قرار داده است.
بحرین و کویت این حملات را محکوم کردند.
بحرین همچنین خواستار جلسه فوری شورای امنیت برای پاسخگو کردن ایران شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76730" target="_blank">📅 19:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pB39CiO7aIaR8tRgwS2u9DPxkx9h1519LD6pDpoBVzqQudCLNIZMihKsmUopKWRmKQe_6pEbRID2LoPKLPUF_hWUxqMwgVsUp-iYK7YthzuqzEW6BEWUAvkVktQ1imglAS8dvbXs5Z1_WyCppEPSE8UBgI20XuMTWyS0nM6rCYsBrpi3nQSbFuhhOdlJUH6piDVMQ8cTJgOJN1K26VJ54_MF8V7r3Hh46h0L9NaNbLjM7ree6U4OJwZ5yasOhxY7pnA5zNvPka2HLA62JmkPUQlpT1n6EapenU6Ds5hU3gMAX7gVKxhZKn3VDY5DZ56ngNgoeoKCyhUNsZlQcK0Zxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش قیمت دلار آمریکا و دیگر ارزهای خارجی در بازار آزاد روز یک‌شنبه، هفتم تیرماه، هم ادامه یافت.
روزنامه هم‌میهن خبر داد که قیمت دلار در بازار آزاد در روز یک‌شنبه به ۱۷۲ هزار تومان رسیده است.
این روزنامه قیمت یورو، واحد پول اتحادیه اروپا، را هم ۱۹۴ هزار و صد تومان ثبت کرد.
روز شنبه، ششم تیرماه، قیمت دلار آمریکا در بازار به ۱۶۶ هزار و ۷۰۰ تومان رسیده بود.
این افزایش قیمت بیش از پنج هزار تومانی در بازار دلار در حالی است که در پی امضای تفاهم‌نامه میان ایران و آمریکا، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان هم کاهش پیدا کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76729" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU3hD-YA8sF29PNdrZfjtQp-a0i2rrDUsJTPkqRI2Zu53bNOGQH2XmjCrLcCStsbbjw_FZT8NEi5839yPYb-VHAZzQY3RG9LjyWFNvw9_Hl2sx8UnHOORGyz-yU6y43BHAuVHtbrUm6YPdSr0AuubOlsbmnBzTU5hkklHashTREX1cd3VBcnRRvgPcirYZvOmfSb3HGQnZBlzSq9fPlEUYpuO0qok8ZlIhMCMJtOic34hjWRuPkOG0_iupx0oFLGJoqeaYV4f0lBx1Zb5RE0crK0q0fP8zcx0DckBM3ToZtVEr8oEtpP35_xMfpOYZGcmyGLp6vylP0tPA-hH19-sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای، سومین رهبر [اعلام شده] جمهوری اسلامی، در پیامی مکتوب به مناسبت هفته قوه قضاییه، از دستگاه قضایی خواست پرونده‌های مربوط به آنچه «جنایات آمریکا و اسرائیل» در جنگ‌های سال‌های ۱۴۰۴ و ۱۴۰۵ خواند را با جدیت در محاکم داخلی و بین‌المللی پیگیری کند.
او در این پیام که به مناسبت سالگرد هفتم تیر و هفته قوه قضاییه منتشر شد از قوه قضاییه خواست رسیدگی به پرونده‌های مربوط به جنگ را تا صدور و اجرای احکام ادامه دهد و مدعی شد چنین روندی می‌تواند از تکرار این‌گونه اقدامات جلوگیری کند.
مجتبی خامنه‌ای از زمان [اعلام] انتصاب به مقام رهبری جمهوری اسلامی تاکنون در هیچ مراسم عمومی، سخنرانی یا برنامه رسمی حاضر نشده [و صدا و تصویری هم از اون منتشر نشده] است. سایر مقام‌های حکومت تاکنون توضیحی درباره این موضوع ارائه نکرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76728" target="_blank">📅 17:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76727">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=deJ2BJ2iOwaYy-mLvxKugxTsJbdtpHc36RkL-SMD31Lw085WIfV7BuDnSrbsvtDLxzS4Nu9HH_vZjET4N0FmPTvroLQcWDIDPAW_9L24Arvirqn6w0sH-8NIsGAWA9VJpCuca8OZ9XWgmmaA0i3kcNzt54w3pzcYdhwX28DjA2F27EzMLcLv9_sLGANE_0yEhPRhWE1Wgwh6y44KdXF-91BmS_xLLXZFC3evZjBWTnJubhesmZyH-QwuXw49nQpm28PDTbeNX5iJOdwUDPcOqklOLrqtlwY-c2EP1uTtWlMcRac37_wVrcPTXLeuHaDbpfqu8GHTlV5yn3oVB0vBOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=deJ2BJ2iOwaYy-mLvxKugxTsJbdtpHc36RkL-SMD31Lw085WIfV7BuDnSrbsvtDLxzS4Nu9HH_vZjET4N0FmPTvroLQcWDIDPAW_9L24Arvirqn6w0sH-8NIsGAWA9VJpCuca8OZ9XWgmmaA0i3kcNzt54w3pzcYdhwX28DjA2F27EzMLcLv9_sLGANE_0yEhPRhWE1Wgwh6y44KdXF-91BmS_xLLXZFC3evZjBWTnJubhesmZyH-QwuXw49nQpm28PDTbeNX5iJOdwUDPcOqklOLrqtlwY-c2EP1uTtWlMcRac37_wVrcPTXLeuHaDbpfqu8GHTlV5yn3oVB0vBOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یک‌شنبه هفتم تیر در کنار همتای عراقی خود به آمریکا هشدار داد که «ایجاد ترتیبات موازی» برای تنگه هرمز «صرفاً به پیچیدگی اوضاع، افزایش تنش‌ها و تأخیر در بازگشایی این آبراه حیاتی منجر خواهد شد».
در پی امضای تفاهم‌نامه میان تهران و واشینگتن، آمریکا هفته گذشته مسیر دوم را برای عبور کشتی‌ها از تنگه هرمز معرفی کرد، مسیری در نزدیکی سواحل عمان که از دسترس ایران به دور است و می‌تواند رقیبی برای انحضار ایران بر این آبراه باشد.
در واکنش به این اقدام آمریکا، سپاه در دو روز گذشته به دست‌کم دو کشتی حمله پهپادی کرده که بلافاصله پاسخ ارتش آمریکا را به دستور دونالد ترامپ به همراه داشته است.
در واکنش به این رخدادهای تازه در خلیج فارس،‌ عراقچی که برای دیدار با مقام‌های عالی‌رتبه عراق به بغداد سفر کرده روز یک‌شنبه در نشست خبری خود با فواد حسین، همتای عراقی‌اش، چنین گفت: «بر اساس این تفاهم‌نامه و پس از رفع موانع، تنگه هرمز ظرف مدت ۳۰ روز تحت مدیریت انحصاری ایران به ظرفیت پیش از جنگ باز خواهد گشت و مسئولیت اجرای این ترتیبات تنها بر عهده جمهوری اسلامی است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76727" target="_blank">📅 17:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76726">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMhT-OrLHxV3yx1UucNbrsHCS8znjBWzM7NeiyHfy58nrs7iTIiAFQL1-_71hSOhhsdeKXhIP9xm9oan3djYSVRjEL-NDoLwdi0fsLK5rN6Y4dexJSJUHaaXr0vYea65XrdtskU1NRGsWuwaCXhFyFa11oPLnZAZEBTusx335xYjrs2sQWTVLgnuv6M4jTcwjjt0QVzTEc3ts5rUHF6V8CBXqx_x7hJPaNePm6R7AEaRLjTzXzLivzdvCrZga49jUYQJDIDdmCCanSCSvaihX0NRKN5KAM7uSLk77Yun413FGciqbydgg-Xswzbc3y3UgYOXI-yNBBHjTYqwnhxJeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تقی چنگلوایی» فعال محیط‌زیست و داوطلب مردمی اهل بهبهان، در جریان مهار آتش‌سوزی گسترده در «کوه بدیل» زاگرس جان باخت.
تقی چنگلوایی هنگام مشارکت در عملیات مهار آتش‌سوزی، بر اثر شدت آتش و حرارت بالا و در پی انفجار دستگاه دمنده‌ای که به دلیل کمبود امکانات برای اطفای حریق از آن استفاده می‌شد دچار سوختگی شدید شد و جان خود را از دست داده است.
رییس اداره محیط زیست شهرستان بهبهان در گفت‌وگو با شرق نیز تایید کرده است که آتش‌سوزی در منطقه شکار ممنوع بدیل واقع در شمال بهبهان هم مرز با منطقه حفاظت شده خائیز هشت شب جمعه پنجم تیرماه شروع شده و هنوز هم ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76726" target="_blank">📅 17:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76724">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">میثم پیرفلک، پدر کیان پیرفلک، که در جریان اعتراضات «زن،زندگی،آزادی» در ایذه کشته شد روز یکشنبه هفتم تیرماه پس از حذف ایران از جام جهانی در واکنش به حرفهای رامین رضائیان، نوشت: «خدا بخواد نمی‌شه که نمی‌شه آقای رضاییان.»
رامین رضاییان، پیشتر گفته بود: «اگر خدا بخواهد پیروز می‌شویم و دل مردم شاد می‌شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76724" target="_blank">📅 17:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vni_43zjovKBZ8x0chSGswKV4kndymEr0u-WdNv7fP9znNsppQsnhPiI3JF339hw7Kllekh1GQ4hbymDwfAaspe9OO57I9NGnIA7MM-xCRXyAVA5TrloegQlmDsQrZjp59II85r5-He8PVCHX6aJyEupuRghi1SB9pDO3FXrnMjNpeM30c3bBn99R5fDCcL8cxZcI_m8v6qUoSN4xwj1J9Ji0J0CSxDy_yp9k84n6IVs8z_5OGmYg7udIJuXAWh7-hTD7yZFZx-VChgxFT92DL2bPBYVOjMt9xkkr0Dg531t0hDhvTDuFtXDLEyrC9oBU-o3MA8wguLOT8W8EvB7EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار الجزایر و اتریش در مرحله گروهی جام جهانی فوتبال با تساوی سه بر سه پایان یافت؛
نتیجه‌ای که آخرین شانس تیم ایران برای صعود به مرحله حذفی را در آخرین ثانیه‌های مرحله گروهی جام از بین برد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/76723" target="_blank">📅 07:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76722">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NiCG60IJUPS4gibvJ00VTKxJ24exVyYIAApdXCfsieUpvemi1uxci4O_hAHNeoF7-EHG_W80uURWSqJLSh7Rq2oiSUrvTDt94W457raU4R_y3Ci72Er1JGaZoiJUCXMPQQcU03vy__hyu24J-APjBh6SG1W0sB_KRyufvUojdfGnwhHl9-7ot3SgzGkSDKApFasHLKJA3JX4zR6ul_sqHMCHBiH8WXHiFlSR64YwazpIMRZXrUOazra5NgbQcWjRPXUGFZWolWrJxiFpAbbU8DdL0C3j3NyOoquOQntjun87oFclTElBIeQnT0Vy6j-1byD41VlApmwTaKu4WItPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران، با انتشار بیانیه‌ای از حمله مشترک موشکی و پهپادی به مواضع ارتش ایالات متحده در منطقه خبر داد.
بر اساس این بیانیه، نیروهای دریایی و هوافضای سپاه در ساعت ۲ تا ۳ بامداد یکشنبه، ۷ تیرماه، هشت زیرساخت کلیدی ارتش آمریکا را در پایگاه «علی‌السالم» کویت و ناوگان پنجم دریایی در بندر «سلمان» بحرین هدف قرار داده‌اند.
سپاه این عملیات را «پاسخی قاطع» به حملات هوایی بامداد یکشنبه آمریکا به پنج پست ساحلی ایران در جنوب کشور دانسته و واشنگتن را به «نقض عهد» متهم کرده است.
در بخش دیگری از این بیانیه، با اشاره به اینکه کنترل ترتیبات عبور و مرور در تنگه هرمز بر اساس «تفاهم‌نامه اسلام‌آباد» بر عهده جمهوری اسلامی است، تاکید شده که از این پس با کشتی‌های متخلف قوی‌تر از گذشته برخورد خواهد شد.
سپاه پاسداران با هشدار به ایالات متحده اعلام کرده است که هرگونه تجاوز احتمالی بعدی، حتی اگر علیه اهداف کم‌اهمیت باشد، با پاسخی «خردکننده» مواجه می‌شود.
@
VahidOOnLine
متن خبر منابع حکومتی:
🔸
سپاه پاسداران خبر داد: عملیات قاطع موشکی و پهپادی در پاسخ به تجاوزهای آمریکا/ با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی بامداد یکشنبه با صدور بیانیه ای از پاسخ قاطع نیروهای دریایی و هوا فضای سپاه به تجاوزهای اخیر آمریکا خبر داد و تاکید کرد: من‌بعد با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه‌ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت. دشمن بداند نقض آتش‌بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
در ادامه این بیانیه خطاب به مردم عزیز و شرافتمند ایران اسلامی آمده است:
فرزندان غیرتمند شما در نیروهای دریایی و هوا فضای سپاه طی عملیات مشترک موشکی و پهپادی در ساعت ۲ الی ۳ بامداد امروز یکشنبه هفتم تیر ماه، با پرتاب موشک های بالستیک و پهپاد به سوی هشت زیرساخت مهم ارتش کودک‌کش آمریکا در پایگاه علی السالم کویت و ناوگان پنجم دریایی در بندر سلمان بحرین آنها را منهدم کردند و تجاوزهای اخیر آمریکا را با قاطعیت پاسخ دادند.
دشمن متجاوز که نقض عهد و پیمان شکنی در ذات او است، به بهانه مقابله نیروی دریایی سپاه با کشتی متخلف، اوایل بامداد امروز، به پنج پست ساحلی جمهوری اسلامی حمله کرده بود.
بر اساس تفاهم نامه اسلام آباد ترتیبات کنترل عبور و مرور در تنگه هرمز با جمهوری اسلامی است و من‌بعد با کشتی های متخلف قوی تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت.
دشمن بداند نقض آتش بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
🔹
و ما النصر الا من عند الله العزیز الحکیم
در خبری دیگر:
نیروی دریایی سپاه پاسداران بامداد یکشنبه هفتم تیرماه، با انتشار بیانیه‌ای در واکنش به حملات اخیر آمریکا اعلام کرد «شلیک‌های کور آمریکا به سیریک» معمای اشراف این نیرو بر تنگه هرمز را حل نخواهد کرد.
در این بیانیه آمده است شلیک به «متخلفان» راه عبور را به دیگر شناورها یادآوری می‌کند. همچنین با تهدید پایگاه‌های آمریکایی در منطقه تاکید شده است: «حساب پایگاه‌های آمریکایی منطقه جداست. جهنم را در این روزها تجربه خواهند کرد.»
@
VahidOOnLine
رویترز به نقل از یک مقام آمریکایی گزارش داد در پی حمله‌های موشکی و پهپادی جمهوری اسلامی به کویت و بحرین، هیچ گزارشی از تلفات نیروهای آمریکایی یا وارد آمدن خسارت یا آسیب عمده به تاسیسات آمریکا در خاورمیانه دریافت نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/76722" target="_blank">📅 04:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76721">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=rQ_Cnh68yEzn94b7GpLUYoR5-3D0p4FSCPNZjugm14bEsNp1y9Y-lmYoqlaTsdWFg8anrcIisOmLR0nMdcjq3Y_heqXtnjZsRyRvSpn1qF66XhI_j77Tp5xYz6hOLTLwdBN_lacZdtbrk39llhNxZm2NIdYziVfjbEJkfSBknVfCv8j-hk8_625YO6udrFqJljsi2oINMXhH0DVw4NidYlSPsSvLVfxa-mY18G51AIV-w9FB-RujsRNM-lnjQvecnJnPIQExdbsi7za94UeAVwQXKjYOgZYbxHKpemaLrY2I9nJopH7OP3BvV5pzaeEHpIl_McVToIAwViUQyAiCuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=rQ_Cnh68yEzn94b7GpLUYoR5-3D0p4FSCPNZjugm14bEsNp1y9Y-lmYoqlaTsdWFg8anrcIisOmLR0nMdcjq3Y_heqXtnjZsRyRvSpn1qF66XhI_j77Tp5xYz6hOLTLwdBN_lacZdtbrk39llhNxZm2NIdYziVfjbEJkfSBknVfCv8j-hk8_625YO6udrFqJljsi2oINMXhH0DVw4NidYlSPsSvLVfxa-mY18G51AIV-w9FB-RujsRNM-lnjQvecnJnPIQExdbsi7za94UeAVwQXKjYOgZYbxHKpemaLrY2I9nJopH7OP3BvV5pzaeEHpIl_McVToIAwViUQyAiCuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
سلام آقا وحید از منطقه [...] بندرعباس چندتا موشک بلند شد به سمت دریا رفت
سلام ساعت ۳:۳۹ صدای انفجار بندرعباس
یک دقیقه بعد: الان یکی دیگه هم زدن
درود همین الان اطراف بندرعباس دوتا صدای انفجار
ساعت ۳:۳۶ دقیقه
صدای دوتا انفجار از راه دور تو [...] بندرعباس شنیده شد، فاصله دور بود اما موج انفجار تو [...] حس شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76721" target="_blank">📅 03:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Wftbfk06w8hecEuienOzwTPcY-6Q1t9_vNWvi1iQZsCNUlEt2kRdfaGcsGYM78BtAoLdWu9juW6X9PmckkYoKmtkRBQypEFZN9Gds7rnBsB34jiXhlQQFX6SZmSZiR1Pmrji87V5Xi31M0JOxLJePfnWdfZyMKd5tdRBp-niEgT1hGD1tUV7jvHulaA2C_HCtC4QwCgiplaJ0JvExhx0RcM6f5vRL_vNSynUycxuIiUqSbBezUCwcYFHwFomtP35m8Fdbha_kUDR53mRVkQZuE5rfNFansAcq5p1R37KfSWgThDMCQLdW0YOblgTUEQZNYw2SO2rYlLMyh8MiQxstw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bSWbttv49pHywxR6IIBmaCBNw_nYzDOIbQgVSrA7-23lbfX4hSVTAMG42BuyHO0eM0Q4xNxCGQg1cJXnAYtonrfzqCibB3AB6I6CTuw443nHSr89BP-bdlvyseqxcSaLiKPbT_cVSS1_c35Qm6zM0Arqq8TN2YAN1JahbD1gak6LtOQMJxJX-9eIIfpPbK9EBXXkoN9wy_qE_SYdItza90Bbi1_NvlJKFYF8vsyLzzkxbKJxJlFwuQDYtQ7t6fItvOgaoK3FFzC83GAcqwHyvKQSRIK3jYuIEYiQ6ZIyg65Ggfyn2kAOt1OlJ8TDvbZ7z6I8yKjzjyjv5uggJwJg8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعلام هشدار در کویت
تصاویر دریافتی
ارتش کویت دقایقی پیش اعلام کرد که پدافند هوایی این کشور در حال حاضر «با حملات موشکی و پهپادی خصمانه» مقابله می‌کند.
@
VahidHeadline
دقایقی پیش‌تر پیام مشابهی درباره بحرین دریافت کرده بودم. الان:
وزارت کشور بحرین، بامداد یکشنبه، با انتشار اطلاعیه‌ای از به صدا درآمدن آژیرهای هشدار خبر داد و از تمامی مردم و ساکنان این کشور خواست تا ضمن حفظ آرامش، فورا به نزدیک‌ترین مکان امن پناه ببرند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76719" target="_blank">📅 03:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76718">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aJi4_ZN_e1qH0yre6dZGCdbUERaRhPR3uP6Et18-7fxy6rzq-KkICOUq6M6YHtycFz0DfAH9nRdD6y1yEQt3iWzrBfzKL8SCRM9n34B0tsh3mIs8BMfpaA-qgEBgJdfRSbVJM8eVbmTgIjqysBG7ewz4yjHGvlPx6TVoR9EBnT4OdV2UoFeNybOYHSTVPPiIBRahNgmjJX27l9bPe07f9vCIgbvHcD13hXeaWsVudf2RhF_3hyMvDevauG8QLjZA7GQuYsgdDcY8R2GFOzGOx8Yh6PCU3x967KMv0qbbw7bb0AqS7Fm2K-ES5Sq6xs3GiwpWMZMnLnptCoHFW1ckJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: در صورت ادامه نقض آتش‌بس، جمهوری اسلامی ایران دیگر وجود نخواهد داشت
ترجمه ماشین:
هواپیماهای ایالات متحده همین حالا محل‌های نگهداری موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند، چون بار دیگر توافق آتش‌بس را نقض کردند!
بسیار محتمل است که آن‌ها هرگز درس نگیرند!
ممکن است زمانی برسد که دیگر نتوانیم منطقی رفتار کنیم، و مجبور شویم کاری را که با موفقیت بسیار آغاز کردیم، از نظر نظامی به پایان برسانیم.
اگر چنین شود، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
رئیس‌جمهور دونالد ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76718" target="_blank">📅 02:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76717">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=mrdmgU_MTXzeuiHc7i3_Ch9k4nrLX0eXCYt5UqHuD_B431s1L1S8ZkHuagZqspc8Y4EHRQ9RHznR6Ol28YsogJbqyh4Fll1VVkEjr4PBVNmKpsrzYWNjEtN7oX9ti4oeIPzcceErNNyxPTp5wrZJt2dCceFkQbsNRRUemweYjnxS-2ZUrdAooZWxU8qN_Zbwt1lU_9RQ2foifNswdVrYhb7fMNMbPb1QSOyLfe2b0KbH3qgR5jhT-xA7Pt-qdbFvEFQ_hRyjc2ydICjKn0wCLmSV7-gpU_CQosyR26rsGvdACqLbF2L3ECBxTvIEVtA7cvWxiD3sSa6FL92lmtBtNg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=mrdmgU_MTXzeuiHc7i3_Ch9k4nrLX0eXCYt5UqHuD_B431s1L1S8ZkHuagZqspc8Y4EHRQ9RHznR6Ol28YsogJbqyh4Fll1VVkEjr4PBVNmKpsrzYWNjEtN7oX9ti4oeIPzcceErNNyxPTp5wrZJt2dCceFkQbsNRRUemweYjnxS-2ZUrdAooZWxU8qN_Zbwt1lU_9RQ2foifNswdVrYhb7fMNMbPb1QSOyLfe2b0KbH3qgR5jhT-xA7Pt-qdbFvEFQ_hRyjc2ydICjKn0wCLmSV7-gpU_CQosyR26rsGvdACqLbF2L3ECBxTvIEVtA7cvWxiD3sSa6FL92lmtBtNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یارو در «رسانه ملی» جمهوری اسلامی داره میگه چون کشتی‌ها قصد عبور از مسیر «ناایمن» رو داشتند سپاه اون‌ها رو هدف قرار داده بوده!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76717" target="_blank">📅 02:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76716">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=kLjEf-JAsGXOCkQk6VdmJ8Omtd5ng1RbK9z69DEg7irKCLi003TMfiYUrGerEizDOTCFV3-Yte9kHVzbnOlh6hvj-mJmHiuQP4a8wTi3LvurKeWtgBDqtn0TNLtDL3W2SY29e16cFmgtdMQK67pAIa3uFPR2sEcO-PoLZQ7fI6PSnzhAhw8OgN5JWdTlWSMUvLdu1IJQYTovzb9Wsqf7q1D3tV4yGPAKjRiKJrLqQucKF7K1vFjnntvficUYyTopffJDUhowAAa4BBfMKucH3hLLACbRjCDeAAheGGBehbL1T8HdTV35OzOrbQj7LniON-7KTCNFSQNvE_Yyi7YAxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=kLjEf-JAsGXOCkQk6VdmJ8Omtd5ng1RbK9z69DEg7irKCLi003TMfiYUrGerEizDOTCFV3-Yte9kHVzbnOlh6hvj-mJmHiuQP4a8wTi3LvurKeWtgBDqtn0TNLtDL3W2SY29e16cFmgtdMQK67pAIa3uFPR2sEcO-PoLZQ7fI6PSnzhAhw8OgN5JWdTlWSMUvLdu1IJQYTovzb9Wsqf7q1D3tV4yGPAKjRiKJrLqQucKF7K1vFjnntvficUYyTopffJDUhowAAa4BBfMKucH3hLLACbRjCDeAAheGGBehbL1T8HdTV35OzOrbQj7LniON-7KTCNFSQNvE_Yyi7YAxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکا پس از تازه‌ترین حمله ایران به کشتی تجاری، حملات بیشتری انجام دادند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) به دستور فرمانده کل قوا، روز ۲۷ ژوئن حملات بیشتری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا در پاسخ به حمله ایران به کشتی M/V Ever Lovely،
به ایران فرصت داده شد تا به توافق آتش‌بس پایبند بماند، اما این کشور چنین نکرد
؛ زیرا نیروهایش یک پهپاد تهاجمی یک‌طرفه را شلیک کردند که صبح امروز ساعت ۴:۳۰ به وقت شرق آمریکا به نفتکش M/T Kiku برخورد کرد. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز در حال عبور بود و بیش از دو میلیون بشکه نفت خام حمل می‌کرد.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه تعرض ایران علیه کشتیرانی تجاری، حملاتی انجام دادند. هواپیماهای نظامی آمریکا زیرساخت‌های نظارت نظامی ایران، سامانه‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات نگهداری پهپاد، و توانمندی‌های مین‌گذاری را هدف قرار دادند.
عبور کشتی‌های تجاری از تنگه هرمز ادامه دارد. نیروهای آمریکا همچنان هوشیار، مرگبار و آماده هستند.
CENTCOM
آپدیت:
بعدا ویدیوی بالا رو درباره این حمله منتشر کردند
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/76716" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KnVqSyC1k4Ez_tB6KxUSr05whPusT4Gl5WiP6-Ec6gwqJa_x4Di6pDCuDLeAZ2mOtY4xeKwFpfNYCLwludMG6umVUWOhJ8TFB-IG9jNdmIIgypfSpCPTpkTxCRCV2nuLSuje1y11Wio6joTRnKtejMxc14fBjhW8BBZssLpB_Arl3vbeBi0w_cnL5T_zALwGv25QaZrNPYRsyZj_-0ev0bJnFbhYMbK40jaSVYGY6ks2Av8WDdA_hAJRz8c-mPZgmiAUXiw_c5ZStgoHnXsvqtFnkai7Nlf6eWxhaRocctN5LLgV2UNZXjOdGfMLSrphchtBCBLAwgSpxqbQrUCmsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام رسمی ایالات متحده در گفتگو با خبرنگار آکسیوس تایید کرد که ارتش آمریکا، بامداد یکشنبه، هفتم تیرماه، در حال انجام حملات تلافی‌جویانه علیه اهدافی در منطقه تنگه هرمز است.
به گفته این مقام مسئول، این اقدام نظامی در پاسخ به حمله صبح شنبه به یک نفت‌کش تجاری در این آبراه حیاتی صورت گرفته است.
@
VahidOOnLine
پیش‌تر:
صدا و سیما: دقایقی پیش صدای چند انفجار در محدوده روستای طاهرویی سیریک شنیده شد
پیام‌هایی که من دریافت کرده بودم:
صدای چند انفجار.
طبق معمول انگار دوباره نیروی دریایی سپاه سیریک رو زدند.
سلام ساعت 12.41 صدای چند انفجار شدید بندرعباس
همین دو دقیقه قبل پایگاه دریایی سیریک هدف حمله موشکی
جوری زد که زمین لرزید
پایگاه دریایی طاهرویی سیریک رو هم زد
دوتا موشک صداش اومد رو دریابانی سیریک
دکل اسکله سپاه سیریک بعد چهار ماه موشک خوردن مداوم بلاخره امشب کج شد
قشم سمت سوزا صدای انفجار شنیده شد حدود ۱۲:۳۰
سلام وحید جان  تقریبا ساعت 00:45 صدای انفجار هرمزگان .قشم
تسنیم:
در اولین ساعات بامداد یکشنبه  صدای انفجارهایی در سیریک شنیده شده است.
برخی منابع مدعی شده‌اند که صدای انفجار در بندر طاهرویه بوده، اما هنوز هیچ منبع رسمی آن را تأیید نکرده است.
🔄
آپدیت ۱:۰۲
خبرنگار صداوسیما در سیریک به نقل از یک منبع آگاه نظامی: صدای انفجارهای شنیده شده مربوط به اصابت چند پرتابه به دکل مخابراتی در محدوده روستای طاهرویی سیریک است
💥
آپدیت ۱:۰۶
خبرنگار اکسیوس: یک مقام آمریکایی می‌گوید ارتش ایالات متحده در تلافی حمله ایران در صبح امروز به یک نفتکش تجاری، در حال انجام حملاتی علیه اهداف ایرانی در محدوده تنگه هرمز است.
آپدیت ۱:۱۲
خبرنگار صداوسیما در قشم به نقل از یک منبع آگاه: چند پرتابه در محدوده روستای مسن شهرستان قشم اصابت کرده است
آپدیت ۱:۱۷
صدا و سیما شنیده‌شدن دو صدای انفجار دیگر در شهرستان سیریک، منشاء صدا مشخص نیست.
آپدیت ۱:۴۱
صدا و سیما:
برخی منابع از شنیده شدن صدای چندین انفجار در بندرلنگه و بندر کنگ خبر می‌دهند
خبرگزاری صدا و سیما هنوز قادر به تایید قطعی این انفجارها نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76715" target="_blank">📅 00:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AUPPyjRmHMI-s45Cz8eBicbU7zxzp0KlvZSKEYU7jEbwA_JSB5wcNdHcwd5CWnyOW6WAK35GQvQr11rUaJZjw9CHrBUQaStTr2qajXTYNqbzExEq-h-6bgz7LSutl-KNsbH58zGl_tTBFC8DrGQYjZOdLzWoK32zgmrtpBbjpda0oK9C7pc0FcBlOWAQmmR_ibMQSxrT1ycYxtb8PkIJSQP0PHWht9uCWTf_ZTaB_mF6E4-bm1XFXzcmVq_eESItcm3PVSPdLBs69U3Lb8qcX1T8Pz3RAumiDjfEuUbwo47VDyRlmGprXTaOt3fxZeAHbtrFWxrHtNoG0Xu69vlCQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sd2mWH1i4yE06Dpc-PpU-cTZ2P_vzrbUqkbdidJn6QLgAwBpEa-ETgKiJaY9Q0QgTi0XcFvYES1iDKT2-ubYg07L1mykUta67UrnImL3KizSYWbxQ_5r63j0iFJoWKA0kgTrBSIGSZVamvKEYnnNQGuSKuJeLOm3r0-ubXomcN4knsEMpi_Fyu_d6KB8SBLl0rv4wLrN5SrpoMjPvbV524aiOe6ZweqSPnsiKNsARk1BsleJpP41pxtM1QMPdGW2c9xoF2-VsScsQx6tFjD-XwJA-ZyOhVOWgfdmHkDzRitb9LIDYHguW0ul1IsENYBuMGhRp-zTxSQOQdDMEINPIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه‌های ایران بیانیه‌ای با امضای جمعی از اعضای مجلس خبرگان را منتشر کردند که در آن می‌گویند بازگشایی تنگه هرمز «خلاف تعهدات مسئولان است و خطایی راهبردی شمرده می‌شود».
بر اساس این بیانیه که خبرگزاری‌های تسنیم و فارس، نزدیک به سپاه، آن را منتشر کرده‌اند، ۶۳ نفر از اعضای مجلس خبرگان تداوم حملات اسرائیل در لبنان و «عدم عقب‌نشینی»‌ ارتش این کشور از مناطق جنوبی لبنان را «نقض آشکار» تفاهم‌نامه ایران و آمریکا خوانده و نوشته‌اند بر این اساس بازگشایی تنگه هرمز «خلاف تعهد مسئولان است».
در بخش دیگری از این بیانیه نیز آمده است «بر هر ملکفی» که به دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، «دسترسی پیدا کند، واجب است آن‌ها را به درک واصل کند».
این گروه از اعضای مجلس خبرگان همچنین «تثبیت مدیریت تنگه هرمز و دریافت غرامت خسارت‌ها و بازگشت اموال بلوکه شده و رفع تحریم‌ها و خروج امریکا از منطقه» را از مطالبات رهبر جمهوری اسلامی برشمرده و هشدار داده‌اند که «هرگونه سهل انگاری در این زمینه» با واکنش مواجه خواهد شد.
این بیانیه در حالی منتشر می‌شود که اختلاف‌ها در درون طیف‌های سیاسی طرفدار حکومت بر سر تفاهم‌نامه در روزهای اخیر بالا گرفته تا جایی که روز شنبه، نمایندهٔ رهبر جمهوری اسلامی در سپاه، از منتقدان این توافق خواست با «ایجاد اختلاف و لغزش» باعث «سوءاستفادهٔ دشمن» نشوند.
تفاهم‌نامه ایران و آمریکا به‌گفتهٔ مسعود پزشکیان، رئیس‌جمور ایران، با رأی «بیش از ۹۰ درصد» اعضای شورای عالی امنیت ملی کشور شامل شماری از فرماندهان ارشد سپاه پاسداران تأیید و تصویب شده و مذاکرات برای اجرای آن آغاز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76713" target="_blank">📅 23:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76712">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=VG9PhFv7EfyFofGh4LvV0ifG8ADNqaYu2eazRXWsbfsk3zzeXU-ms-YNW-TmUVJjPmMIRwDI6DULEHfvKmV2KXiSQGllP5vjxraXAAEoEZhTlPTCjuSBcZXFbOOZESMct7Ee9ZAMjQTRt0J5JJ15Ed0MLpRgKrBr0SRhm5-wHWVaQjcfYwKkBWk3S3bLNtv-WDSDSTM8lWpS-lD3Xx2yd9F_2heDnCIdK3xVDrPN4PdeKrYeoKLw5mwAOmSBWkhUzyiVJgVHbZiPPtTzKX6PNTROen9nz_M_2mgOMpKQ-vB9gXYa5xu2JzlHLs6Ww_oMCI3p2c2DUg25KwK2cLa4MA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=VG9PhFv7EfyFofGh4LvV0ifG8ADNqaYu2eazRXWsbfsk3zzeXU-ms-YNW-TmUVJjPmMIRwDI6DULEHfvKmV2KXiSQGllP5vjxraXAAEoEZhTlPTCjuSBcZXFbOOZESMct7Ee9ZAMjQTRt0J5JJ15Ed0MLpRgKrBr0SRhm5-wHWVaQjcfYwKkBWk3S3bLNtv-WDSDSTM8lWpS-lD3Xx2yd9F_2heDnCIdK3xVDrPN4PdeKrYeoKLw5mwAOmSBWkhUzyiVJgVHbZiPPtTzKX6PNTROen9nz_M_2mgOMpKQ-vB9gXYa5xu2JzlHLs6Ww_oMCI3p2c2DUg25KwK2cLa4MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل در سخنرانی تلویزیونی خود ضمن اشاره به توافق اخیر با لبنان، آن را دستاوردی «بسیار بزرگ» توصیف کرد.
بنیامین نتانیاهو با تاکید بر اینکه اسرائیل در «منطقه امنیتی زرد» باقی می‌ماند و این مسئله ضامن امنیت این کشور است، خاطرنشان کرد که فشارهای مختلف برای خروج اسرائیل از این منطقه به نتیجه نرسیده است.
او با قدردانی از نقش دونالد ترامپ، رئیس‌جمهوری آمریکا و مارکو روبیو، وزیر امور خارجه این کشور، در تحقق این توافق، تصریح کرد که اسرائیل نه تنها "محور تروریسم ایرانی"، بلکه "محور سیاسی ایران" را نیز در هم شکسته است و افزود: «ما به دلیل ساده‌ای به چارچوب این تفاهمات رسیدیم: چون حزب‌الله را به شدت در هم کوبیدیم و حزب‌الله که منتظر کمک ایران بود، آن را دریافت نکرد».
بر اساس طرح پیشنهادی آمریکا که چارچوب توافق لبنان و اسرائیل بر آن بنا شده، نیروهای اسرائیل به‌صورت مرحله‌ای، کنترل مناطق مختلف را به ارتش لبنان واگذار می‌کنند و ارتش لبنان نیز مسئولیت جلوگیری از ورود اعضای مسلح حزب‌الله به این مناطق را برعهده می‌گیرد.
خواسته اولیه لبنان، خروج کامل نیروهای اسرائیل از مناطق جنوبی این کشور بود.
حزب‌الله لبنان، این توافق را «تحقیرآمیز» توصیف کرده و آن را فاقد اعتبار دانسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/76712" target="_blank">📅 22:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76711">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hrxn4UTpRo0r2kbDfxb68T1AYDvmum7HVeDvbfVwgTdhfYXYvVJerqaAIummPlmZ8JoAbTMe9G9PwlItl1ppozFRst2xcbsvOzrFLigkpRfNu31UsUUotqcWgBHZbIBzGjRGbEzZl9HOWuzK5cuFozPAQE0fnaV_EdZIoau5nIeasv81kp-xbxSiwlqii1lQ2hvygtS8KBXBMy-hC9Dc6YM8cNuXC-H9-s3wH4Kxs51eNvzsHZfmL0Y7fE1XWpM88MAxuBODELscedls7a-fqjjt8q0wN061QWPRLQC6ArO25-5TDLBhCmRc2haC5djtfT0FupSv2bBYuU7FgXKTGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی درباره قطع شدن برق در مناطق مختلف شرق تهران:
سلام وحید جان
به طور بی سابقه ای کل برق پیروزی و بلوار ابوذر رفته کلا خاموشه محله های این طرفا
توی قطعی برقیا هیچوقت اینجوری سابقه نداشته کل محله ها با هم بره کلا شرق خاموشه
سلام وحید
ما محله نیروی هوایی ، منطقه ۱۳ تهران هستیم. برقا رفته. و اینجور که از دوستان پرسیدم تا  خیلی جاها برق نداره، حتی برق  چراغ راهنمایی  رانندگی هم قطع شده.
مثل یه سری که توی جنگ برق ها قطع شد و حمله کرده بودن شده، چشم چشم رو نمیبینه
سلام وحید جان برق شرق تهران محدوده پیروزی کامل قطع شده
وحید برق  نارمک هم رفته
😐
😑
نارمکاز پشت بوم دیدم تا جایی که افق دید اجازه میده کلا شرق تو تاریکیه
برق سمت نظام آبادم کامل رفته همه جا تاریکه
داداش برق سبلان و نظام آباد و اینام رفته
سلام برق سبلان هم‌رفته
سلام، من میدون رسالت تهرانم، تا چشمم میبینه همه جا تاریکه
بجز مناطق خیلی دورتر
کل نارمک جنوبی بی برقیم
سلام ما نارمکیم ولی برق داریم
نارمک پایین هفت حوض برق هست
سمت رسالت و سرسبز رفته
سلام برق جنوب نارمک هم قطع شده فکر کنم پست دوشان تپه مشکل دار شده
وحیدجان ما نظام آبادیم ولی برق داریم
البته به بیمارستان امام حسین نزدیکیم
وحیدجان برق شهید کلاهدوز هم رفت همی الان
داداش ما کلاهدوزیم دو دقیقه پیش رفت
همه جا تاریکه
سلام وحید جان
محدوده شیخ بهایی تهران خیابان شیراز شمالی هم برق رفت
سلام وحید جان
تهرانپارس فلکه اول
ما برق داریم ولی دارم نگاه میکنم ی سریا ندارن!
برق خیایان شیخ بهایی شمالی رفت
انتهای تهران نو سمت اشتیانی و فلکه اطلاعات برق نداریم.
ما نیروهوایی هستیم برقا تا جایی که میبینیم قطعه
آقا برق وصله چرا الکی میگن شما هم میزارین مردم همه حالشون بده ترو خدا استرس بیخود ندین
برق خیابون مدنی،  نظام آباد همچنان قعطه
نارمک ۴۶ متری غربی برق رفته بود دو سه دقیقه هست که برگشته
نارمک جنوبی، حوالی میدان شقایق هم برق رفت.
سلامت میدان ۷۰ و سمنگان هم رفته بود.
الان بعد ۲۵ دقیقه اومد
وحید جان سبلان شمالی برق قطعه
سلام، زرکش وحیدیه برق قطعه
وحید جان سلام پیروزی چهارراه کوکاکولا برق داره اما کل خیابان نیروی هوایی برق رفته به طوری چشم چشم رو نمیبینه مردم با نور موبایل راه میرن
برق نظام‌آباد اومد
ندیدم مجیدیه رو بگند که برق رفته. اینجام نیست
منتها زنگ زدم و محله بقلی خواجه عبدالله برق هست.
سلام وحیدجان ما پیروزی سمت خیابون شیوا هستیم برق داریم
برق مجیدیه و خیابان کرمان از ۸.۲۰ دقیقه کامل قطع شده . تا چشم میبینه برق اطراف قطع شده
الان. نظام اباد محدوده شرقی امام علی خاموش بود همین الان اومد.
داداش برقا اومد فک کنم یه بانکی چیزی خالی کردن رفتن دیگه
🤣
وحید یرق پیروزی بلوارابوذر اومد
آپدیت: پیام‌هایی از وصل شدن برق در بعضی از مناطق داره میاد.
همز‌مان خبرگزاری فارس:
قطع برق تعدادی از مناطق تهران؛ دلیل مشخص شد
تعدادی از مناطق تهران از ساعاتی پیش با قطعی برق مواجه شدند.
پیگیری فارس از توانیر مشخص کرد، مشکل فنی در یکی از پست‌های ۲۳٠ شرق تهران علت قطعی برق است.
هم‌اکنون تیم‌های عملیاتی و فنی برای رفع مشکل در محل پست حاضر و درحال حل مسئله هستند.
آپدیت:
همچنان که خیلی‌ها پیام میدن که برق ما وصل نشده یک عده که برقشون وصل شده بود هم دارند پیام میدن که دوباره قطع شد. شاید به خاطر همون تعمیراته.
آپدیت ۰۰:۴۰ بامداد یکشنبه:
خبرگزاری تسنیم:
برق شرق تهران وصل شد
رجبی‌مشهدی، معاون وزیر نیرو از رفع خاموشی‌های شرق تهران خبر داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/76711" target="_blank">📅 20:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76710">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7IM3X1ci--iUj_0wVx32Vs-sl-z1xV3eJn0bmhVjpKghngtkFqoLihK5h2vJP3adCodOeEICKwiC1LYMrjwwcBwXdkVOPGbWEKJIEwM1jYcSxa3xpjogYdQBKd0WTcjxvfjoNozWW8OVbi6iEupiWdvNC-28dpQAV1PUFuKtv5XD86S14fDWOplrbOOSZTWLUoySfkTwrymsYPwy-agNGmYS4WqRmUh8KcnpZwz86kkCdQM67VarureZAVZ2LVBmSY0tHhoyhmf_0liyjozxF-jjNsf6RmeQepBGC5IRyUZsECKyR1z6I2y2V_fjbAEVcA89mBjz80ykEiUKDhchg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رسانه‌های ایران ارائه خدمات بعضی از بانک‌ها از صبح امروز (شنبه، ۶ تیر ۱۴۰۵) دوباره مختل شده است؛ خبرگزاری ایسنا به بانک‌های ملی و صادرات در این زمینه اشاره کرده است.
شرکت خدمات انفورماتیک این اختلال را مرتبط با حمله سایبری دانسته است. در اطلاعیه این شرکت آمده است:
بررسی‌های فنی نشان می‌دهد این اختلال در امتداد آثار حمله سایبری پیشین بر زیرساخت‌های فنی و سامانه‌های متمرکز بانکی پدید آمده است.
هفته گذشته اعلام شد تمامی اختلال‌های پیش آمده در بانک‌های تجارت، ملی و صادرات برطرف شده است.
اختلال هفته پیش باعث شده بود که در بعضی موارد، حتی انجام عملیات خرید با کارت‌های بانکی هم امکان‌پذیر نباشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76710" target="_blank">📅 17:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76709">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNnnfsbKGQcMKv8ySETkMwzylZkIjRTFko2ya4067G1YPr3MhSvCedqXYpuj1QW6c57ShJOyVw4NJkgZFh9bMIXkbTC6VMZXpLBXUbpv-XWR8t3WqMDgHK1JHTOGGQB9ij31ahiCz3ujRDHrbxhdIxgONILEt4KNUDAwKApkeuvJgxOwA-zjb-ct9m2Xmv4kN1QwX6jYH28Xlrex7Mv2Bba_eWVfzYCducHnThaX_0uUh9ceZk-DPFLfWuferR3Ob7g1FuIbReNu1lkE5HFyU0OFsMRmDmYq1vNppGyYR3RzOvARLDWPfosfS6ge5q2h_qnWApQssiQmoFk3uOPGBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهنام گلخنی، پدر احمد گلخنی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴، روز چهارشنبه ۴ تیرماه در باغباد‌ران از توابع استان اصفهان بازداشت شده و با وجود وعده آزادی، همچنان در بازداشت به سر می‌برد.
کمیته پیگیری خبر داد آقای گلخنی پس از آن بازداشت شد که
در استوری اینستاگرام خود از مردم دعوت کرده بود تا ظهر عاشورا بر سر مزار جان‌باختگان اعتراضات حضور پیدا کنند.
بنابر این خبر قرار بود او روز شنبه ۶ تیرماه آزاد شود، اما با گذشت این موعد، همچنان در بازداشت است و اطلاعی از وضعیت پرونده یا اتهام‌های احتمالی او منتشر نشده است.
احمدرضا (احمد) گلخنی، شهروند ۳۷ تا ۳۹ ساله اهل باغبادران، در جریان اعتراضات دی‌ماه ۱۴۰۴ جان باخت. او مقابل کلانتری باغبادران هدف شلیک مستقیم قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76709" target="_blank">📅 17:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76708">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzPQKi-cYqAT0eYPnhD6pD9sVYlJ05ccNwki9rVyv1yy_XGuYJiuirw8XTUsYM29YZvbye5n27j8T_Uw7TKrMWC3gdPEhtObZLZRhJ64PAKY4-9Z1WrJ2pkrIkB4LDvzgBuFmy1Lwix6zjv5wZT15410pvWgOryKt4olqWNi39Z5FMZXixk9-gJ1j_KtS9LNB5NGeqguY2_VCo6g9y3ZuxCjHwwnFsxeSAQ5OIxDXVOlZEmmecNcHbykqAmxHe8fF7G8VrrJAr2W8VUF7vWFFsOXDDc6pWzAyqm5M2eSqhjk71JVsCk0qx5NxgNnhn2lgEpPA2oPB16ZZI-YPUCDgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل شرکت شهر فرودگاهی امام خمینی از برقراری دوباره پروازهای میان ایران و امارات تا پایان هفته جاری خبر داد و گفت: ایرلاین‌های داخلی مقدمات راه‌اندازی مجدد مسیر دوبی را فراهم کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/76708" target="_blank">📅 17:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lVaW2hoGZ1-jeKTVTdsdnxGEF40kFkTsZuHsmarlM6DcuyMLD_l5wCyUiAjwVubBcyjHFQTR4_PufUsBZGRbOLIBMLhC4QIoOz-L5ab9I7vbyPs9YBYrzql2R_sz_bFH731tmI0-76I-IEF2K0jH4xTy1bPhMFZCpPJeKjFSstANwdtq1AVrz71TrkUfrd7d5shiF4ALWj_5KHoWeoW-D6avY91jp04lm_4FSi9e8nmaMvWTl1W-quMhqvAXuwpg1UH3xPDJBEZNO9E-Goo_FlOxhVTBNBIWp6WMJgm89XjIT-8GI1fOoHppJKvOEdiMGVxDJP2bNVF-9Yd3HFzQDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه بحرین در بیانیه‌ای اعلام کرد جمهوری اسلامی بامداد شنبه با چند پهپاد به خاک این کشور حمله کرده است. این وزارتخانه با محکوم کردن این حمله، آن را نقض حاکمیت بحرین و تعهدات جمهوری اسلامی بر اساس تفاهم‌نامه اسلام‌آباد با آمریکا دانست.
در این بیانیه آمده است حمله پهپادی، نقض آشکار حاکمیت بحرین، تهدیدی علیه امنیت شهروندان و ساکنان این کشور و مغایر با قوانین و عرف‌های بین‌المللی است. وزارت خارجه بحرین همچنین اعلام کرد ادامه حملات جمهوری اسلامی، هم‌زمان با تلاش‌های منطقه‌ای و بین‌المللی برای کاهش تنش، روند صلح را تضعیف می‌کند و نشان‌دهنده رویکردی برای بی‌ثبات کردن منطقه است.
وزارت خارجه بحرین با اشاره به تفاهم‌نامه اسلام‌آباد افزود جمهوری اسلامی متعهد به توقف دائمی عملیات نظامی و احترام به حاکمیت کشورهای منطقه شده بود، اما حمله اخیر به گفته این وزارتخانه، نشان می‌دهد تهران به تعهدات خود و جامعه بین‌المللی پایبند نبوده است.
بحرین همچنین با تاکید بر حق خود برای دفاع از حاکمیت، امنیت و ثباتش، از شورای امنیت سازمان ملل خواست مسئولیت خود را در اجرای قطعنامه ۲۸۱۷ و پاسخگو کردن عامل این حمله بر عهده بگیرد.
@
VahidOOnLine
یک مقام آمریکایی که نخواست نامش فاش شود، به وال‌استریت ژورنال گفت حمله بامداد شنبه، ششم تیرماه ایران به بحرین شامل دو پهپاد انتحاری (یک‌طرفه) بوده است.
این مقام مسئول اظهار داشت که یکی از پهپادها توسط یک سامانه پدافند هوایی زمین‌پایه سرنگون شد و پهپاد دیگر بدون ایجاد هیچ‌گونه خسارت یا تلفاتی، در محوطه یک فرودگاه دورافتاده فرود آمد.
همچنین گزارش شده است که یک پهپاد انتحاری به نفتکشی حامل دو میلیون بشکه نفت خام اصابت کرده و نیروهای آمریکایی دو پهپاد دیگر را که کشتی‌های تجاری را هدف قرار داده بودند، سرنگون کرده‌اند.
@
VahidOOnLine
پس از اعلام دولت بحرین مبنی بر حمله پهپادی جمهوری اسلامی ایران به خاک این کشور در روز شنبه ششم تیرماه، کشورهای حوزه خلیج فارس این اقدام را به شدت محکوم کردند.
این حمله ساعاتی پس از آن رخ داد که سپاه پاسداران از هدف قرار دادن مواضع نظامی آمریکا در پاسخ به حملات سنتکام در بندر سیریک خبر داده بود.
وزارت امور خارجه امارات با صدور بیانیه‌ای، این حملات را «نقض فاحش» حاکمیت بحرین و تهدیدی برای امنیت منطقه توصیف کرد.
وزارت امور خارجه قطر نیز ضمن محکومیت این اقدام، بر لزوم پرهیز از پیامدهای این حملات «غیرموجه» و تداوم مسیر دیپلماسی برای حفظ دستاوردهای یادداشت تفاهم اخیر تأکید کرد.
در همین حال، وزارت امور خارجه کویت این تجاوزات را تضعیف‌کننده خطرناک تلاش‌ها برای صلح دانست و بر همبستگی کامل خود با بحرین تأکید کرد. جاسم محمد البدیوی، دبیرکل شورای همکاری خلیج فارس (GCC) نیز این حملات «خائنانه» را که به گفته وی زیرساخت‌های غیرنظامی را هدف قرار داده، به شدت محکوم کرد. این تنش‌ها در حالی اوج گرفته که از دو شب پیش و با حمله سپاه به یک کشتی باری سنگاپوری، فضای امنیتی در تنگه هرمز به‌شدت بحرانی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/76707" target="_blank">📅 17:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sEK9wgKe3X5puTNHkZmFqQB4Ke16zeOQ1k1utR9wA2WL_Bh8FRQzOQZqZXq_gXmqKsDBjXLV8oZn4Omomd0Pz71JTsYQW6hWIm3D5mQ03kjaDgdwUZZzqHNbWapJ4sjUZLwqmmwsXrVkrXXaZteLuznjPVzR_JztEdTdBijl06bSgYXhgTw9X87dzuhR0oepbbLSWo_MQgn_PlmMxFRdJ5hPIm5no1VyOp2rx0TV89DKEkhUhsOFU81gbsd7IsKEAEfErzdIurFX8KsFKqZ-Nuu_LCgdhKGYdIayGAHIfI2RjWRDCICHqnFchnNX1n-GRP1hva6X1k8n_SrWL27rkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ می‌گوید بررسی‌های داخلی وزارت دفاع آمریکا نشان می‌دهد مجموعه‌ای از نقص‌ها در سامانه‌های اطلاعاتی و هدف‌گیری ارتش این کشور ممکن است در حملهٔ موشکی به مدرسه میناب نقش داشته باشد.
بر اساس گزارش بلومبرگ که روز جمعه ششم تیر منتشر شد، یک تحلیلگر اطلاعاتی متوجه شده بود ساختمانی که در پایگاه دادهٔ ارتش آمریکا به‌عنوان یک تأسیسات نظامی ثبت شده بود، در واقع به دبستان تبدیل شده است.
به‌نوشتهٔ بلومبرگ، منابع آگاه گفته‌اند این ارزیابی در سال ۲۰۱۹ در یک سامانهٔ دیجیتال ثبت شد، اما آن سامانه به پایگاه دادهٔ رسمی هدف‌گیری ارتش متصل نبود.
مقام‌های رسمی آمریکا تا کنون جزئیات این گزارش را تأیید یا رد نکرده‌اند.
بلومبرگ می‌نویسد تحقیقات پنتاگون همچنین بر ضعف‌های دیرینهٔ سامانه‌های اطلاعاتی ارتش آمریکا از جمله استفاده از پایگاه‌های دادهٔ قدیمی و نبودِ ارتباط کامل میان سامانه‌های مختلف متمرکز است. این گزارش می‌افزاید هنوز مشخص نیست فرماندهی مرکزی ارتش آمریکا، سنتکام، پیش از حمله از فرایند تکمیلی بازبینی اهداف استفاده کرده است یا نه.
وزارت دفاع آمریکا اعلام کرده است تحقیقات دربارهٔ این حمله همچنان ادامه دارد و جزئیات تازه‌ای ارائه نکرده است. دونالد ترامپ نیز گفته است ممکن است هرگز مشخص نشود چه کسی مقصر بوده و خود او هنوز مدرکی ندیده که قانعش کند آمریکا مقصر بوده است.
ایران می‌گوید در حملهٔ هوایی به مدرسهٔ میناب که ۹ اسفند پارسال در نخستین روز حملات آمریکا و اسرائیل به ایران صورت گرفت، دست‌کم ۱۷۵ نفر از جمله ۱۶۸ دانش‌آموز کشته شدند. شورای تشکل‌های صنفی فرهنگیان تأیید کرده که در این حمله بیش از ۱۰۸ دانش‌آموز کشته شده‌اند و گفته است معلمان هم در میان قربانیان این حمله بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76706" target="_blank">📅 17:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ed6foO1_vFgzG2xYK4tN0DweSeQTO3TlQKVAveULRx5KTaukcmr1QH-GE8QOaW6G_fufS2GDOm4YBZZSQ26zndJLkbehuvZyxNQ1bheWayVJKJE5LpQPhuIIFmygkID07PcSZmYgNm--bnDgah0vwl6AIclzAPDcz-T2BLgGgd78BKsM48r0pcPGid-AApkjdZRSq5HesHa-CCzJSXS-tsHcef5mwLHXp3PJvyhKCIpMZoQISaqfnPGoCkVe9VFR-wlFhOMHqm3Py3Mzj1WJdyYstfuMxsSPx7TLL7kQEj8dtbnXwA2tPM8hsa1LRNeIyNvYqJKO_6rkVvPwKUu4Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"یاسین محمودی، نوجوان ۱۶ ساله و اهل رفسنجان در استان کرمان، در جریان اعتراضات مردمی این شهر با شلیک مستقیم نیروهای حکومتی جان خود را از دست داده است.
بنابر اطلاع ایران‌وایر، یاسین محمودی روز جمعه ۱۹ دی‌ماه ۱۴۰۴ در خیابان طالقانی، ابتدای سه‌راه امیرکبیر رفسنجان، هدف شلیک مستقیم نیروهای حکومتی قرار گرفت.
گلوله به ناحیه شکم این نوجوان اصابت کرد و او بر اثر شدت جراحات جان باخت."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76705" target="_blank">📅 17:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76704">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z9bqC9w9wBqeYG9Z35GSq8T1yWLdXPctc20uqcVb_Wkb9BH1xXIor3wLe0S2UkAwTIWkRdJ1IGnd6CUIOPkcfEC4jLTOv3ZD5Z05HV0sa4joTbRBIG0wIn485iXCz5vjht-3VSWjgODBcTqPqwspE1hxUHl6b2E0_p3AdCLmtKby7sA77kZFeguKWXva4TlWWVaYo3Cbxn4THPgMthc-TseV5FnZd5TnrS8GlCl8VuFUtXfA-iJ4JNxZhp4QGumEj7vD8TkyY1UbNRhzlXIa0huvEWgc1k85K-SZEyEptO7OHkq7-Ggw3JEnkIfkoUInX_1gcxDBZLn50G_5blAYSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسابقه فوتبال ایران و مصر با نتیجه مساوی یک یک به پایان رسید.
بلژیک با پیروزی ۵ به یک بر نیوزیلند و مصر هم با ۵ امتیاز و به‌دلیل تفاضل گل کمتر، به عنوان تیم‌های اول و دوم به مرحله حذفی صعود کردند.
به این ترتیب صعود ایران به نتیجه بازی‌های غنا با کرواسی، ازبکستان با کنگو و الجزایر با اتریش گره خورده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76704" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76703">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=C11_p8e5oiFBOWnLmmjHgP95EVKbq_c3wecUUoaXxXIt_pi6kj0Wz8G89_uKlFCeae7XZDL0D4p-gcJWSeBvlhWaxzjk1tDUc9_5v7HnOgkJ6alyu2nH0hw5tQ-JI1ysmAe2yFiMnpk3ZQMGkGhzDh-cAVylH0_tdddwbJlcgqwEwqX27WdP2FOHQqRjdIdRe82YfqNz3bRE_Y94oX6BC-DoirMeQzFnDNUoCzm5J7wHolJLSC7Vc8pb8nyeAZnxNe2rcyxVznW6RnqiZ7Rb4rsPXZWmocyP5fFGmhKduz4m7JRWsJtweKwU5H_Z6y07SI_uXl_EGZM73YBIT5xl8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=C11_p8e5oiFBOWnLmmjHgP95EVKbq_c3wecUUoaXxXIt_pi6kj0Wz8G89_uKlFCeae7XZDL0D4p-gcJWSeBvlhWaxzjk1tDUc9_5v7HnOgkJ6alyu2nH0hw5tQ-JI1ysmAe2yFiMnpk3ZQMGkGhzDh-cAVylH0_tdddwbJlcgqwEwqX27WdP2FOHQqRjdIdRe82YfqNz3bRE_Y94oX6BC-DoirMeQzFnDNUoCzm5J7wHolJLSC7Vc8pb8nyeAZnxNe2rcyxVznW6RnqiZ7Rb4rsPXZWmocyP5fFGmhKduz4m7JRWsJtweKwU5H_Z6y07SI_uXl_EGZM73YBIT5xl8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم  ترجمه ماشین: حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری  تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی…</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/76703" target="_blank">📅 06:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76702">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncxGV30KCawqt7xdz-nRiZrDAlOXFDbzKZWhZIWnjvnoNwd3ODHY8A_x-4W6BPdLcK2D9X1kSWwpqDlw__mEVAhzBSheGtWM29DEByZFbq496xgSSwvzFI_Y5D8_1bzfvIM8lYFPPRBw_GL64p-Czr1oWBnIVr30VwilOlmQajj8_k8InzHYF_Gj6Z7xQRYIBgNYfOZ42w9gn9EulCW9J6Mv1_mQQyx7pRlLOrVTotgPLAXtWxtSGuFnJd2xtjnnfPqMB2FZTsK2dQXb2LmT3KWhw-qn58mo4utAJNqo0xMrGAMUGaMoDokAFY71O0n8CDyhUuze4GMOgshBMm6OoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌سپاه پاسداران اعلام کرد که نیروی دریایی این نهاد در واکنش به حملات آمریکا به سواحل ایران، مواضع ارتش آمریکا در منطقه را هدف قرار داده است.
در بیانیه روابط عمومی سپاه آمده است که آمریکا پس از حمله به یک کشتی تجاری در تنگه هرمز، به بهانه عبور این کشتی از مسیری که ایران آن را «غیرمجاز» می‌داند، حملاتی هوایی به سواحل ایران انجام داده است.
سپاه این حملات را نقض آتش‌بس و تعهدات آمریکا خواند و مدعی شد در پاسخ، «نقاط استقرار ارتش آمریکا در منطقه» هدف قرار گرفته‌اند. جزئیاتی درباره محل این اهداف، نوع حمله یا خسارات احتمالی منتشر نشده است.
در این بیانیه همچنین گفته شده است که بر اساس بند پنجم تفاهم‌نامه اسلام‌آباد، کنترل عبور و مرور در تنگه هرمز بر عهده ایران است.
سپاه هشدار داد که در صورت تکرار حملات آمریکا، پاسخ ایران گسترده‌تر خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/76702" target="_blank">📅 03:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76701">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/drE6f-fW9UJwjf1nMK9y3VVzdOm0KH0PKXzOal_zETVFWqb2xwhWl3M0uQz0v_JXwcSji91c3PWuR8vMat-p1lF065nJ7LyiNowjdUkYtkWXoMaIu3aW1h1G9Gq6qds5bN06j_A3JZRadMH5mi7sd8W-KFlHqAgCZOpcjuUkGQ2EU81FobyaIBifrmXEExWbhUeq5K57K_Y32MmAcoec0LBwOdlveaEH8hyDSnFXhI61KA9eoQhmDf5kqkrChZBmXuKKwMaszvqNoutkr93OBxAGe67alkP_r5nIO9f7-_k3yOQdtmFNg3Bzq5zk2gTT8-VMAGDn2qZIo2GLFWeYvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
رسانه‌های داخلی در ایران از درگیری مسلحانه میان نیروهای حکومتی و گروه‌های مخالف مسلح در «ایست بازرسی بانه - سقز» خبر دادند. گزارش‌های اولیه آنها حاکی از آن است که دو نفر از نیروهای حکومتی کشته‌ شده‌اند. همچنین گزارش شده است که پنج نفر دیگر نیز مجروح شده‌اند. جزئیات بیشتری منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/76701" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76700">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hSDyGGvFil-bLKWjNVSYJjUQMB1TaV_tEzsm2amdKAi9vznujTqplqnDJG5KK7WHp0biygaJV5nj9rJyb5UAI3znyFvb5-QXNpY4xJLXZ9QzyXKDQ0NYnJU5Roc5Y6wHahbl1orYswwhE-M1itajo5Rt7Qyup-eBbqUjfongJktiIBfoMxxewTgj0Ct9RgQCHwOgIOfgKCHm3iNmtwom4Uw-LFN7by8Km3NVljw7l4Pj7b4ywhxP33oTVxuI5DvKs_ZTfDlMZPBp7VLy9SSWFBr1Alpa0Dodkc6ztpwtg-WYgPIUTNM5IF2KIWWtummSusCDgcWpfLKDv-4kxk9P3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم
ترجمه ماشین:
حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آن‌که ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک‌طرفه به کشتی M/V Ever Lovely حمله کرد،
انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند.
این کشتی باری با پرچم سنگاپور، هنگام حمله ایران، در امتداد ساحل عمان در حال خروج از تنگه هرمز بود.
این تجاوز بی‌دلیل نیروهای ایرانی علیه کشتیرانی تجاری، آشکارا آتش‌بس را نقض کرد. افزون بر این، رفتار خطرناک ایران آزادی کشتیرانی را تضعیف کرد؛ آن هم در حالی که جریان تجارت به‌طور فزاینده‌ای از این کریدور حیاتی تجارت بین‌المللی عبور می‌کند.
نیروهای CENTCOM همچنان هماهنگی و پشتیبانی برای عبور امن کشتی‌های تجاری از این تنگه را فراهم می‌کنند. ارتش آمریکا همچنان حاضر و هوشیار است تا اطمینان حاصل کند که همه جنبه‌های توافق با ایران رعایت و اجرا می‌شود و کاملاً به قوت خود باقی است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/76700" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76699">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LIhHtifgqOuwUfb3JoH97MyGKl_2Wco2ceC0topnQjDcA3N-QN2hnTcGHm7ZA88bcJ4o78YljanJK-x4D2iJVlQ2itn58N-Cp-nYFrNcE1trxXWT9twJNEWUB30RTRpVHo3_XvC7Q2Ig_xGkDskfk0CFTsBDaVHtCBDrkbzelSrmLBkFm6OhyYY3BJj3nQhEiXRFkAUZ9bxZ78KxVvR4GQEwT25hkk39wHVRGAgjwwx2OVd-ifRgEpylmF8gvvxg1Uh4HkGYKmNYtjvJ0QQTaAkVZj_6_OyPC4fYNquoe8h2gFYhUJbZx2HnfYbGQmehU0VbKC763RcJ4Iunvl5Fbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
دقایقی قبل ؛ شنیده شدن صدای انفجار در طاهرویه سیریک
منشأ صدا هنوز مشخص نمی‌باشد.
اطلاعات تکمیلی متعاقبا اعلام می‌گردد.
من ساعت ۲۳:۳۰ این پیام‌ها رو دریافت کرده بودم:
اسکله طاهرو رو زد  ۳ ،۴ بار
زده بطرف تنگه
سیریک گروگ سه تا صدای انفجار
آپدیت:
تکمیلی| به گزارش خبرنگار صداوسیما در سیریک:
ساعت ۲۳ و پانزده دقیقه امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.
یک منبع آگاه نظامی علت این انفجارها را اصابت پرتابه به محدوده اسکله طاهرویی سیریک بیان کرد.
این منبع آگاه نظامی گفت: حدود ۵ ساعت پیش چند شلیک اخطار از شهرستان سیریک به شناورهای متخلف‌ در تنگه هرمز پرتاب شد.
همچنین شنیده ها از شلیک دو موشک اخطار ساعاتی پیش از حوالی کرپان به سمت تنگه هرمز حکایت دارد.
و
خبرنگار آکسیوس به نقل از یک مقام آمریکایی، جمعه‌شب، پنجم تیرماه، گزارش داد: «ارتش ایالات متحده حملاتی را در منطقه تنگه هرمز انجام داده است». پیش از این، صداوسیما از شنیده‌شدن سه انفجار در طاهرویه سیریک خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76699" target="_blank">📅 23:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83b030969e.mp4?token=eYP_tEYlef5B6bKmWYpsINoiBQxHIaeanis2vpWmPnf1oMgeYe6MDWjfySTYKhRuqqJn8hD2LYlXWEQXHfXc17V1s_vlcdqstP1oAV-dSW9UJ-H3gjkjNk4BGunQ3U-vCwoOBmgBZD6aVYjQ7_Q-IxfGLKdHDXIi2BiZ40VN8G_LdyVovc8UEWgWX7iDgHEyF3mtDiGxdu5mIWxEyAGmSKVeqHLRKfaHaPPj-2my8dlgQPVQJjyoA_g8s72ePoshj9nZHD7zOWXRHAAhZTI4mE-4YfaXB1JlkE3vkB-JWEuC2n3N1FwOgKa93QcANP5FoGEYWxozrPSF8x-N97U1OK9vj0SN0LGcfdfEw1ugTXvvWvO1I7yv8ri4FyFO2riQ7Vfz5k08MruCxuT2k3tjVrdkTeKKfiB6Vc5Pcfx788wlcjCZ63wMACqn4gGzcRXb4KPgolXQGFpHbaENG_J0UVkFaFlYtMMVt7u_dRQ_HJJkI9dyvfX8izKtC_eAp6KfsjoHFqq8_XLCEzwfKMYDnN7u93tR8mgbFNDRA47_y-kSXrSDw6MBezmYsex66eNmCQVxx2py3ifmGbuoRs44CNfHlzGLGJ01BJD9Ppoc1bodbJogrEchaZU8WaqtO2VvjFqDdQS2LuQ4izQYhiOG1Qn99NL1kfu9AiRzlx7i-Lk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83b030969e.mp4?token=eYP_tEYlef5B6bKmWYpsINoiBQxHIaeanis2vpWmPnf1oMgeYe6MDWjfySTYKhRuqqJn8hD2LYlXWEQXHfXc17V1s_vlcdqstP1oAV-dSW9UJ-H3gjkjNk4BGunQ3U-vCwoOBmgBZD6aVYjQ7_Q-IxfGLKdHDXIi2BiZ40VN8G_LdyVovc8UEWgWX7iDgHEyF3mtDiGxdu5mIWxEyAGmSKVeqHLRKfaHaPPj-2my8dlgQPVQJjyoA_g8s72ePoshj9nZHD7zOWXRHAAhZTI4mE-4YfaXB1JlkE3vkB-JWEuC2n3N1FwOgKa93QcANP5FoGEYWxozrPSF8x-N97U1OK9vj0SN0LGcfdfEw1ugTXvvWvO1I7yv8ri4FyFO2riQ7Vfz5k08MruCxuT2k3tjVrdkTeKKfiB6Vc5Pcfx788wlcjCZ63wMACqn4gGzcRXb4KPgolXQGFpHbaENG_J0UVkFaFlYtMMVt7u_dRQ_HJJkI9dyvfX8izKtC_eAp6KfsjoHFqq8_XLCEzwfKMYDnN7u93tR8mgbFNDRA47_y-kSXrSDw6MBezmYsex66eNmCQVxx2py3ifmGbuoRs44CNfHlzGLGJ01BJD9Ppoc1bodbJogrEchaZU8WaqtO2VvjFqDdQS2LuQ4izQYhiOG1Qn99NL1kfu9AiRzlx7i-Lk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش مرتبط با ایران در سخنرانی ترامپ به تشخیص ماشین
متن  زیرنویس:
https://telegra.ph/trump-06-26-4
بعضی از جملات:
ایران هرگز سلاح هسته‌ای نخواهد داشت. نمی‌گذاریم چنین اتفاقی بیفتد.
و به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، ایران امروز نه نیروی دریایی دارد، نه نیروی هوایی، نه توان پدافند هوایی، نه رادار، و عملا نه تولیدی. ظرفیت پهپادی‌شان ۸۲ درصد کاهش یافته است. ظرفیت موشکی‌شان ۸۰ درصد کاهش یافته است. پرتابگرهای موشکی‌شان ۹۰ درصد کاهش یافته است. رهبری‌شان یک بار کشته شده، و رهبری‌شان برای بار دوم هم کشته شده.
و دیگر هیچ‌کس نمی‌خواهد رهبر ایران شود. گفتند: «چه کسی می‌خواهد رئیس‌جمهور شود؟» بعد همه گفتند: «نه، ممنون.»
این کار باید در دوره ۴۷ ساله‌ای انجام می‌شد که آن‌ها با ترور حکومت کردند. و همین کار را کردند. با ترور حکومت کردند. وقتی مرد یا زن جوانی را می‌بینید که بدون پا یا بدون دست راه می‌رود، یا چهره‌ای که از بین رفته، این به خاطر بمب کنار جاده‌ای بود که ساخته شد؛ ساخته ژنرال سلیمانی، که من در دوره اولم او را کشتم. و آن یک کشتن بزرگ بود.
هنوز می‌توانند شلیک کنند؛ می‌دانید، دیروز یک پهپاد را به سوی یک کشتی بزرگ که وارد تنگه هرمز می‌شد شلیک کردند. چهار تا شلیک کردند. ما سه تای آن‌ها را ساقط کردیم. یکی از آن‌ها؛ فکر کنم؛ ما از دستش ندادیم. کسی آمدنش را ندید و به کشتی خورد و مقداری خسارت زد. اما نمی‌توانند چنین کارهایی بکنند.
و فراموش نکنید وقتی باراک حسین اوباما JCPOA را انجام داد. ببینید، اگر به آن نگاه کنید، باراک حسین اوباما؛ اسمش را شنیده‌اید؟ او فاجعه بود. فاجعه بود. او ۱.۷ میلیارد دلار پول نقد به آن‌ها داد. ۱.۷ میلیارد دلار پول نقد و ده‌ها میلیارد دلار. آن را به ایران داد. فکر می‌کرد می‌تواند دوستی آن‌ها را بخرد. و دقیقا برعکس شد. آن‌ها از پول استفاده کردند و موشک ساختند و هر چیز دیگری.
و من برجام را لغو کردم؛ توافقی که... همان توافق هسته‌ای ایران بود؛ فاجعه بود. ضمنا مدت‌ها پیش منقضی شده بود، اما من مدت‌ها قبل از انقضایش لغوش کردم. اگر این کار را نمی‌کردم، ایران سلاح هسته‌ای داشت. اگر ۱۰ ماه پیش بمب‌افکن‌های B-2 را نفرستاده بودم، آن‌ها سلاح هسته‌ای داشتند. ما آن تأسیسات هسته‌ای را نابود کردیم. بسیار مهم بود.
و آن وقت دیگر اسرائیلی نداشتید. اسرائیل نابود شده بود. می‌دانم در این اتاق طرفداران خوب اسرائیل زیاد دارید. و اسرائیل نابود شده بود و احتمالا خاورمیانه هم نابود شده بود. و ما... آن‌ها می‌توانستند ضربه‌ای بزنند. ما خیلی سریع نابودشان می‌کردیم، اما آن‌ها می‌توانستند به ما هم ضربه‌ای بزنند.
بازار سهام از زمان انتخابات ۷۳ رکورد تاریخی ثبت کرده است. و امروز شمار بیشتری از آمریکایی‌ها نسبت به هر زمان دیگری در تاریخ کشورمان مشغول کارند. این خیلی خوب است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76698" target="_blank">📅 23:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76696">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aKf6quDBLvhbm8pl3dKt28yS7Qzd8OTM1aLkAB_hxVidDuB-4M288JzPMaSKIdke507a-lb38Q2yhg60GmGL2vupmuoYHBvcG3XuPeVuQmXOr3325NNyGz_Eq8c-ftaRoRi6WeN7MA_EHt4Djv0JebIwfl84KEXKoHpMlj6NPTecAmeilhkccPkbFdtlAuZ1l48r0dq6bDfoKvZ-G1MsCfJ5y6gS8sbpDOjhkLwf25kKNvMe6SDKs_CErik-1O-DYvtkESvizjsAliqLQ2IPMtCnoe_nd_NxzEOO8CdHgIlMul7dqqQRbfW0rCi385x-tHK69q2Ek7Lf7tCXY1ZWqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GzrFOBNKHpe1AEKSPdcuoAfoyPTOXQ6fyCk1ejTsk1N_lQdDrPOO9txmgDTdgcaz8SjemTn1Qw4GGKc7_QRUgzVFBIH4dMQgk5CvbDp3PnIDPu4Vj52EO-ze_AGlF6bm6YClYBFx4fjNVtSeR2rbGmU6P3u1lf1jU8h1n9siiju4aglskqxW6cUQc_5cEtjd5GIMrCo45rPcbAom_i7_6H_029-_A0d0-Jx1bHXCilr9AAK88Kr8akwikVtqKMZ7SEHL9IER3BDkNMuluJDqjlaOT4B74bcdmmGxuABJwb9B6pDlB39UpdyCuy9AiWkFkmRKDIG1QKa0Bk4Y6Wy0mQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، پس از امضای توافق اسرائیل و لبنان در واشینگتن در بیانیه‌ای اعلام کرد: «این توافق دستاورد بزرگی برای اسرائیل است و مذاکرات طولانی در واشنگتن به نتیجه رسیده است. مهم‌ترین نکته این است که اسرائیل در منطقه امنیتی باقی می‌ماند و تا زمانی که حزب‌الله خلع سلاح نشود این وضعیت ادامه خواهد داشت.»
او افزود: «این توافق ضربه بزرگی به جمهوری اسلامی است و تهران تلاش می‌کند اسرائیل را به عقب‌نشینی وادار کند اما اسرائیل، لبنان و آمریکا تاکید کرده‌اند که جمهوری اسلامی و حزب‌الله در این روند نقشی ندارند.»
نتانیاهو تاکید کرد: «اسرائیل در منطقه امنیتی باقی خواهد ماند و اجازه ورود حزب‌الله یا غیرنظامیان به این گروه داده نخواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76696" target="_blank">📅 22:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76695">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=vMMBS1uZgZdBxcyY4UVUEQ6n2MSw1srxV0N9thbrrw2JWDmVWwnvuV77jmTEr2QIcBJZd3_Fa0PFaJL1IY1YYwWlI25FftcheAJkQNIiX2XD1x9fcS5MHMl-71PHrOCNPJqXdAtK63CekRxAjYUOAhnQXsL-vvWmjPO5R2qDDUGs5yl-J3ZKj_1ebV98lxRhsObCudn52R5HtrqUmPxC4u67wljavJIdmwT5c5Too96lbkP8yK_eNughOjqqYQyPP0jM-CxCBjXkdKVAOI_p2sHoDwuAmvQxiNZ7lU6dyI9NuZcjKK7WjRlrdbpP1YmImF9S8V55x-pN766HsRgn8g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=vMMBS1uZgZdBxcyY4UVUEQ6n2MSw1srxV0N9thbrrw2JWDmVWwnvuV77jmTEr2QIcBJZd3_Fa0PFaJL1IY1YYwWlI25FftcheAJkQNIiX2XD1x9fcS5MHMl-71PHrOCNPJqXdAtK63CekRxAjYUOAhnQXsL-vvWmjPO5R2qDDUGs5yl-J3ZKj_1ebV98lxRhsObCudn52R5HtrqUmPxC4u67wljavJIdmwT5c5Too96lbkP8yK_eNughOjqqYQyPP0jM-CxCBjXkdKVAOI_p2sHoDwuAmvQxiNZ7lU6dyI9NuZcjKK7WjRlrdbpP1YmImF9S8V55x-pN766HsRgn8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم.
ویدیوی بالا درباره ایران نیست.:
ترجمه ماشین: همان‌طور که دیدید، کمونیست‌هایی که اخیراً در شهر نیویورک انتخاب شدند، سوسیال‌دموکرات نیستند. آن‌ها می‌خواهند شیوه سنتی زندگی آمریکایی را کاملاً نابود کنند.
فروختن کمونیسم خیلی آسان است. همه‌چیز را نابود می‌کند، اما فروختنش خیلی آسان است. صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. می‌گفتم اجاره رایگان است؛ خانم‌ها و آقایان، از این به بعد لازم نیست هیچ اجاره‌ای بدهید. از این به بعد هر کسی خانه می‌خواهد، نگران نباشد؛ فقط خانه‌ای را که می‌خواهد انتخاب کند. همه غذای رایگان می‌گیرند؛ از این لحظه به بعد همه‌چیز رایگان است. همه به من رأی می‌دادند.
مشکل اینجاست که بعد از دو یا سه سال، کشور به منطقه‌ای فاجعه‌زده تبدیل می‌شود. کشور شکست می‌خورد. همیشه همین‌طور می‌شود. فروختنش خیلی آسان است. آن سال اول، آدم فوق‌العاده محبوبی هستید. همین حالا هم این اتفاق در نیویورک و کالیفرنیا دارد می‌افتد.
اما بعد شروع می‌کنید به زندگی در فلاکت. در فلاکت زندگی خواهید کرد. غذایی وجود نخواهد داشت. مسکنی وجود نخواهد داشت. ارتشی وجود نخواهد داشت. قانون و نظمی وجود نخواهد داشت. هیچ‌چیزی وجود نخواهد داشت. از هر نظر به ساکن جهان سوم تبدیل می‌شوید و همه رنج خواهند کشید یا خواهند مرد. رنج می‌کشید یا می‌میرید. این همان چیزی است که اتفاق می‌افتد. هزاران سال است که این اتفاق با نام‌های مختلف افتاده است.
به شما می‌گویم، من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. خیلی آسان بود. لازم نبود کار کنید؛ می‌توانستید در خانه بمانید. مشکل این است که چند سال می‌گذرد و کل آنجا فرو می‌پاشد. همیشه همین‌طور می‌شود؛ همیشه همین‌طور بوده است.
اما متأسفم که بگویم ترور کسانی که با آن‌ها مخالف‌اند، عنصر بسیار مهمی در ایدئولوژی آن‌هاست. ترور برای آن‌ها مسئله بزرگی است. آن‌ها حیوان‌اند. حیوان‌اند.
در خیلی از موارد باهوش نیستند، اما در بعضی موارد هستند. جذب پیرو برایشان آسان است، چون وعده‌هایی می‌دهند که خودشان می‌دانند نمی‌توانند عملی کنند. و دموکرات‌ها هم مقابله نمی‌کنند. برای همین احمق‌اند. مقابله نمی‌کنند. می‌ترسند. من شومر [احتمالاً اشاره به چاک شومر] را می‌بینم؛ از جنگیدن می‌ترسد. آدم‌هایی را می‌بینم که نسبتاً معمولی‌اند و آدم‌هایی که ما با آن‌ها مخالفیم؛ آن‌ها از جنگیدن می‌ترسند.
دموکرات‌ها چرخش عظیمی به چپ داشته‌اند. من به بعضی از کسانی که آن شب در نیویورک انتخاب شدند نگاه کردم. این‌ها از خیلی جهات آدم‌های احمقی‌اند؛ از بعضی جهات از نظر فکری احتمالاً نسبتاً باهوش‌اند، اما آدم‌هایی هستند که می‌خواهند کشور ما را نابود کنند. آن‌ها از کشور ما متنفرند. از مردم ما متنفرند. از حزب دموکرات متنفرند.
حزب دموکرات در دردسر بزرگی است، چون این ماجرا با نیویورک متوقف نمی‌شود. این مسیر، انتخاب شدن را بیش از حد آسان می‌کند. همه‌چیز، به نوعی، برای انتخاب شدن بیش از حد آسان است. بسیار خطرناک است، اما به‌زودی چیزی برایتان باقی نمی‌ماند. مشکل همین است.
از خیلی جهات، آن‌ها اجازه می‌دهند این افراد راه خودشان را بروند و هر کاری می‌خواهند بکنند. می‌گویند نمی‌خواهیم ریسک کنیم و حرف بدی بزنیم، چون می‌ترسیم اگر این کار را بکنیم شغل‌مان را از دست بدهیم. می‌ترسند انتخابات خودشان را ببازند، حتی اگر فقط به گفتن چیزی درباره این نسل تازه آدم‌های بیمار فکر کنند.
آن‌ها آن‌قدر باهوش یا سرسخت نیستند که با طاعونی که در جریان است بجنگند. این دارد درست جلوی چشم شما اتفاق می‌افتد. اگر همان‌طور که با جمهوری‌خواهان می‌جنگند، یا همان‌طور که با من می‌جنگند، با آن‌ها می‌جنگیدند، پیروز می‌شدند. آن‌ها ما را شکست ندادند، اما در برابر کمونیست‌ها پیروز می‌شدند؛ ولی شجاعت این کار را ندارند.
پس خودشان دارند کمونیست می‌شوند و به یک حزب کمونیست تبدیل می‌شوند. این‌ها سوسیال‌دموکرات نیستند. این‌ها کمونیست‌های سرسخت و بی‌خدا هستند. کمونیست‌های بی‌خدا هستند. همه کمونیست‌ها بی‌خدا هستند. به خدا باور ندارند.
به نظر من، این جدی‌ترین تهدید علیه کشور ما از زمان تأسیس آن، حدود ۲۵۰ سال پیش، است. این تهدید بزرگی برای کشور ماست.
درباره ایران هم:
ترامپ در کنفرانس سیاست‌گذاری ۲۰۲۶ ائتلاف ایمان و آزادی، گفت: نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. نمی‌توانیم بگذاریم این اتفاق بیفتد.
آن‌ها دارند از شدت نیاز برای رسیدن به توافق التماس می‌کنند. آن‌ها خیلی چیزها به ما می‌دهند. این باید در طول ۴۷ سالی که با ترور حکومت کرده‌اند انجام می‌شد.
رسانه‌های جعلی می‌گویند آن‌ها امروز خیلی قوی‌تر از چهار ماه پیش است اما آن‌ها اکنون خیلی چیزها به ما می‌دهند.
@
VahidOOnLine
📡
@VahidOnlin</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76695" target="_blank">📅 22:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76694">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=CSqkbVw9eVNizzpf9_o30Bu7LxB7R5MNkHceDka_x3VH02SZReWrp6CHgHqwnycB0mpAlD-PPqCSJAthC-KW4ju8KqPyw03y1hua6wNtxm-MIlMC8sZs1u693itfkYKIMn1chjEwaf3vrKUdC-DlmiDnEuxNyciQqTrXofSadoNvAScXk2Cw4HyIXVbhoIDHBH3iNvc_aSsv_9TPWJ5JbE53RwUHMr42PCVvTV31EOPecm4WZ4cCLTQVxN1WPn9xJCeefppZI8f0cbROyFQSFFU1xfLJfmguZbQX37XaWV_4P1UxsMMeFNb0NY77bd9Qec_GdZ-ah7aXBKNwliIpog" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=CSqkbVw9eVNizzpf9_o30Bu7LxB7R5MNkHceDka_x3VH02SZReWrp6CHgHqwnycB0mpAlD-PPqCSJAthC-KW4ju8KqPyw03y1hua6wNtxm-MIlMC8sZs1u693itfkYKIMn1chjEwaf3vrKUdC-DlmiDnEuxNyciQqTrXofSadoNvAScXk2Cw4HyIXVbhoIDHBH3iNvc_aSsv_9TPWJ5JbE53RwUHMr42PCVvTV31EOPecm4WZ4cCLTQVxN1WPn9xJCeefppZI8f0cbROyFQSFFU1xfLJfmguZbQX37XaWV_4P1UxsMMeFNb0NY77bd9Qec_GdZ-ah7aXBKNwliIpog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره‌کنندگان ایالات متحده، اسرائیل و لبنان پس از پنجمین دور از گفتگوهای دیپلماتیک، روز جمعه پنجم تیرماه، یک چارچوب سه‌جانبه را امضا کردند.
این مذاکرات شامل بررسی پیشنهادی با حمایت آمریکا بود که بر اساس آن، نیروهای اسرائیلی بخشی از قلمرو تحت اشغال خود را به ارتش لبنان واگذار کنند.
پیش از آغاز این دور از گفتگوها، لبنان خواهان خروج کامل نیروهای اسرائیلی از خاک این کشور بود؛ در حالی که برای اسرائیل، شرط اصلی هرگونه عقب‌نشینی، خلع سلاح کامل حزب‌الله و دریافت تضمین برای بازنگشتن نظامی این گروه به مناطق مرزی است.
روبیو در مراسم امضای این توافق‌نامه گفت: «این آغازِ آغاز است. کارهای زیادی در پیش داریم. امروز اولین قدم است و گاهی اوقات، اولین قدم سخت‌ترین قدم است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76694" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76692">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=TkZxFoQlUcfnKVXKbqwPEGGHf1x-LV-NGthGF-qRRfmgG3IJEVwvyv-qma14Kj9ow8s2Y7VmGRNLBejNlyZyduodwBWf00oUzvFJwdhL5NVSKrfsWUKFXA-8JUiompvwzEzZ3YQkXKV9Qpywm60IookG4H7Ut7AmG2kPlwd-P6wFFfCaeWOMxEJoTqH_yfFG0XkOvBb1Y81o85mt9zeC2W6KTwSNQI2i7PryGoGta2kcr2s042q0tE9rDz_jhKeghUsRAzbJkF_-dOp_58iLnacAzB4YvRXGWI9AW7dElyn4mFpzgAUhg9SeiUUeaJwWKTmzrOdqsAyGIUWr3g9nKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=TkZxFoQlUcfnKVXKbqwPEGGHf1x-LV-NGthGF-qRRfmgG3IJEVwvyv-qma14Kj9ow8s2Y7VmGRNLBejNlyZyduodwBWf00oUzvFJwdhL5NVSKrfsWUKFXA-8JUiompvwzEzZ3YQkXKV9Qpywm60IookG4H7Ut7AmG2kPlwd-P6wFFfCaeWOMxEJoTqH_yfFG0XkOvBb1Y81o85mt9zeC2W6KTwSNQI2i7PryGoGta2kcr2s042q0tE9rDz_jhKeghUsRAzbJkF_-dOp_58iLnacAzB4YvRXGWI9AW7dElyn4mFpzgAUhg9SeiUUeaJwWKTmzrOdqsAyGIUWr3g9nKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که امدادگران در ونزوئلا همچنان در جستجوی بازماندگان زلزله‌های ویرانگر شامگاه چهارشنبه در میان ساختمان‌های فروریخته هستند، تازه‌ترین گزارش‌ها، حاکی از کشته شدن بیش از ۵۸۰ نفر و زخمی شدن حدود سه هزار نفر بر اثر این حادثه است.
بیم آن می‌رود که شمار قربانیان بسیار بیشتر باشد. بسیاری بی‌خانمان شده‌اند یا به دلیل آسیب‌دیدگی و ناامن بودن ساختمان‌ها، از بازگشت به خانه‌های خود هراس دارند.
در کاراکاس، پایتخت ونزوئلا، و شهر ساحلی نزدیک آن، صدای افرادی که از زیر آوار ساختمان‌های فروریخته درخواست کمک می‌کردند، شنیده می‌شد.
پیش از این مقامات ونزوئلا گفته بودند که حدود ۳۰ پس‌لرزه هم پس از دو زلزله شدید روز چهارشنبه ثبت شده است.
در پی وقوع این زلزله سازمان زمین‌شناسی آمریکا هشدار داده بود که تعداد قربانیان این حادثه ممکن است به هزاران نفر برسد.
@
VahidHeadline
هم‌زمانی این زلزله با بازی برزیل و اسکاتلند در جام جهانی خیلی‌ها رو یاد فاجعه ۰۰:۳۰ بامداد پنج‌شنبه ۳۱ خرداد ۶۹ در استان گیلان انداخت که همزمان با بازی همون دو تیم در جام‌جهانی ۹۰ ایتالیا اتفاق افتاده بود.
زمین‌‌لرزه‌ای که حدود ۴۰ هزار نفر رو کشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76692" target="_blank">📅 19:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76691">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkH5G65SLkITLJHyQBUQJZnlMqfix8sCmqvgC2cV6kZQdJq6BK5Rm_QosfU8OEopfjqw_8cEYqhEd_VxX4j7d7GEx-3x-QujwNAZd7JUb-Tn6f5tU5Tfv5hSB0tXegompUjLZuw7TTYJW0lsvxEjUNlkJdYak7dvAnwO0REi_XqO065XJDlrG3PajrOBJmz8wmUlekIpmvYCAP_RnZV29sWytM5qNfFTTwPxhyifAKeVWRW3dmCiUsmwr6vSyEFNq-g7N566_N3v4YNI3hFUUL1FiNLs-00eefl6wkLCXJDtlqfNPF3WjhxfEWTxhG5ro2vLOEg8VeWvRu5JbJb6Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی گزارش داد که روز جمعه، پنجم تیرماه، سپاه پاسداران سه نفت‌کش خارجی را که قصد داشتند از مسیری «غیرمجاز» از تنگه هرمز عبور کنند، بازگرداند. این نفت‌کش‌ها تلاش داشتند از «کریدور جنوبی» استفاده کنند؛ مسیری که اخیرا عمان و سازمان بین‌المللی دریانوردی (IMO) به عنوان یکی از دو مسیر موقت برای تردد در این آبراه پیشنهاد داده‌اند.
جمهوری اسلامی با رد این توافق، مسیر پیشنهادی جدید را «غیرقانونی، غیرقابل‌قبول و بسیار خطرناک» خوانده و تاکید کرده است که تنها مسیر قانونی برای عبور از تنگه هرمز، همان مسیری است که پیش‌تر توسط تهران تعیین شده و از نزدیکی سواحل ایران می‌گذرد.
داده‌های ردیابی «مارین‌ترافیک» نیز نشان می‌دهد که سه نفت‌کش پس از حرکت در مسیر جنوبی تغییر جهت داده و بازگشته‌اند و سه کشتی دیگر نیز مسیر خود را به سمت شمال و آب‌های تحت نظارت ایران تغییر داده‌اند.
این در حالی است که به گزارش «لویدز لیست»، بسیاری از کشتی‌ها در هفته جاری از مسیر پیشنهادی عمان استفاده می‌کردند. این اقدامات همزمان با تنش‌های اخیر پیرامون مدیریت این آبراه راهبردی صورت می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/76691" target="_blank">📅 19:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76690">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BCvRU9Xlum9JgJ2nmKWl5c1X8O6Wv_U7p8LgHru2TwqPkZbFV2uYj5lWSShU39iOkMr05QRQjUMKiOytoMeuvlBfdlLQNiH141tqMUlxOYIYT94MEO3WQYgqq3qQQUChiLEZNqXII7gl4Co8PbA4klwgZ6kE3clCao_Xp79istkUFa7OsayMtHiLIOyQ1FcpMsah1TE8T-z32CwZJEkjdyoTFkOJAU8CZTq0Bk3cfgeAgK2KdfrU6Ujh0ffVFNLKIidJdZBCtphC5YOfi3wZ5rpIPfrKBkOYP-mE72TM7J8WgTiDuHXbbNW6prnJhnLycdG0711Wvhv74D6H8Sji2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
جمهوری اسلامی ایران دست‌کم چهار پهپاد حمله یک‌طرفه را به سوی کشتی‌هایی که در حال عبور از تنگه هرمز بودند شلیک کرد.
یکی از این پهپادها به‌طور مستقیم به عرشه بالایی یک کشتی بزرگ و بسیار گران‌قیمت حمل بار برخورد کرد. خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این نقض احمقانه توافق آتش‌بس ماست.
رئیس‌جمهور  دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/76690" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UntJ2sTX1BvAO2JBp4J9GFYjO9FtJaRI7Uas8H88ra1QshTFy2ayh1Yi3eMTTMwNO_pvk2VLJJw4UnoScPsmh95UhGum5wtgQjrDbIpoJe4M_GCIMNqQ1GnEecTZ7qrPYYygNsaIRPbXaLYG_qwBcwQOyyWNRrAP9lpkiNusVwvqWbVoEm6fhWM9zt65aGIXlKZhYS6MHJewh9dRGp7R66dz3dluPASUEJ1jf6kWH4485lrFYFp9-hwC4rAMqIEKepfV60WI8LfrpBGB5OQVHAfUEnoYYkb-1S0EFutxQr3hoAj2URk95jLUlqbgcvVNfgOX1LWhrZi3Bcnt1pPreA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرس تی‌وی، شبکه انگلیسی‌زبان صداوسیمای جمهوری اسلامی، روز جمعه خبر داد که میان ایران و ایالات متحده یک «کانال ارتباطی» در تنگه هرمز ایجاد شده تا از وقوع حوادثی که می‌تواند به تشدید تنش‌های نظامی منجر شود، جلوگیری کند.
این گزارش یک روز پس از آن است که جی‌دی ونس، معاون رئیس‌جمهور آمریکا، گفت واشینگتن و تهران قرار است این کانال ارتباطی را راه‌اندازی کنند و این اقدام را «دستاوردی مهم» خواند.
او در گفت‌وگو با وب‌سایت «آنهرد» گفت که ایران موافقت کرده تا یکی از نیروهای سپاه پاسداران را به دوحه، پایتخت قطر، بفرستد تا به گفته او «در کنار یکی از نمایندگان فرماندهی مرکزی ارتش آمریکا، سنتکام، مستقر شود» و از این طریق بخش زیادی از اختلافات حل و فصل شود..
شبکه پرس‌تی‌وی به نقل از یک منبع آگاه گفته است: «بر اساس بیانیه نهایی منتشرشده از سوی دو میانجی پس از مذاکرات هفته گذشته در زوریخ، این کانال ارتباطی با هدف جلوگیری از بروز حوادث در این آبراه راهبردی که ممکن است به درگیری نظامی منجر شود، و نیز برای اجرای مفاد ماده پنجم تفاهم‌نامه اسلام‌آباد ایجاد شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/76689" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
