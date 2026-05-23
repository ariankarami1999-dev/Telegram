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
<img src="https://cdn1.telesco.pe/file/ntj9LNnHDGzV9ssVfRfm86XgfbHGxvHKGhT9kW1K37B6h2KYaz9XAteXnTpiuGUfIheZNKxot8vHFN3EU0jBwCGkMgfXxARSaz2y3NV49yrDWFrNAUCZQ5TgvKLRaErj0b2Rz-m9x1Hpyqbfx-kEBBXPNj0vk7tDwinF7Z5dP5aZ2PEGwVgBM7Gdfqwf70w_65CudrES98KbDrn3g7DUcLPeQVTOhgw0CDLWDBmxXsd_C4ZaALFHtX4rAU2e7QziE2m9mk3RL9hK8Lc5fd9DKjTmpHIPTlir_csHwEW-wx4UKp5fcpQIt-tWmbCujNVtumqzFbqiNsGkGxSNJys0WA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.33M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 16:34:40</div>
<hr>

<div class="tg-post" id="msg-75633">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4LA03MAwuuFy1WMT8dSUvggIp8lVtmQr-vKGj4xUIYKntPM2sVX7BJj3tb72KIYrdlX19yvyQjKMPjgGF_KksV-WgeTu0OvbEMZ3g1W9qiN4urEHqMtjcnoCO-LvNUd-Vqz007V0WRXGNoND380RhkRwn5Txvlheh4sTFXvbJ7WUIU8s2hAnvthdGwHgLnrLHbEWIF9l1gC52Eqds6quBg4UujugovnaIKps1yGz7Ly_H6G7rIMXbLZdGS9c2TSAlMob1UjIviEDIt2VnmKMuoVU6lCEIW_t-zHmaTz2pscyLShdSFji51T0jUrfwVIvwXpozNHRVhQXZy-LK7gaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها در ایران از دیدار فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان با عباس عراقچی، وزیر امور خارجه ایران در شامگاه جمعه یکم خرداد خبر دادند.
بر اساس این خبر، دیدار این دو مقام تا پاسی از شب ادامه یافته و محور گفت‌وگوها «تلاش‌ها برای جلوگیری از تشدید تنش و خاتمه جنگ» و «راهکارهای تقویت صلح، ثبات و امنیت در منطقه غرب آسیا» بوده است.
جزئیات بیشتری از این دیدار منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/75633" target="_blank">📅 08:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75632">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTk_QBOuT2uf2x6VS2XuRLQewIiy-cWGNr5shqUrZoqdagLtZO6MwKQ5mu3R5HMdggi2ZW2B1epqS72Tqj3je-Ot1hlV07L5fX7XLjZZATrxeswuk5sGbZtQ0r4ku3wRI7JQCm9jEQqIBtcx4tOu6agMHl4igxb7I4m9a1Dw71GJXXcfI5w8mT4QROq54H0FlOMeBBgrCjD_U7qZAI0gW7TcvHtGmhzLScqXjse69sEBt2AdmYY-zfYh0AQ_6W8KLvwQb7z-R6l35XmP4pVZd1CxpFAh3NKQXrLvaMj0aRZhsu--qvWyBKs9ygeMG694Td96ckiV-Arbzv2_G6hXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت دونالد ترامپ اعلام کرد که سیاست‌های مهاجرت به آمریکا تغییر می‌کند.
در یک تغییر اساسی در سیاست‌های مهاجرتی آمریکا، دولت این کشور اعلام کرد خارجی‌هایی که قصد دریافت اقامت دائم یا همان گرین کارت را دارند، باید خاک ایالات متحده را ترک و از طریق کنسولگری یا سفارت آمریکا اقدام نمایند.
زک کالر، سخنگوی دفتر مهاجرت دولت آمریکا، گفت که این سیاست «نیاز به یافتن و اخراج» کسانی را کاهش می‌دهد که درخواست اقامتشان رد شده است.
از سوی دیگر وکلای مهاجرت و گروه‌های امدادی می‌گویند که این تغییر احتمالا به «جدایی بیش‌ازپیش خانواده‌ها» منجر خواهد شد و قربانیان قاچاق انسان هم مجبور خواهند شد «به کشورهای خطرناکی بازگردند که از آن گریخته‌اند.»
این تغییر سیاست تازه‌ترین اقدام آقای ترامپ در محدود کرد مهاجرت به آمریکا است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/75632" target="_blank">📅 08:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75631">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1CpDbqkvXpcgJZAXThI1JRRR4t-TSjiFwMUDt2tlehw_I3Qiab_q1MM1kTSeCEAcQod8UOjFVg-Y91Su0ZqIEtezkIyQ9pISBEANEK__pUjSOTyUBrku81LMt1Y-Rd4ysXNsmTTgPb9O9r0heEjzTXtEsWtlX4APdvh2CQXP3PnSPR4Hd4Wwg0D-jICiDUaE7q7WoS4WBYfJczINBZkIouFzQzk7Vjt-Q4fu2WmUj3f9OORQzLMS1R7a_ReCvB_CaMVQZH6DXyaYmcZw_ayrkIZgxrwz6P8hYx7FADuNNlJdldMZ11cDPSVnU6VutidbxGXiPihnrlvUh3HkXK23A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه «نیویورک‌پست» به نقل از منابع آگاه افشا کرد که ایوانکا ترامپ، دختر ۴۴ ساله دونالد ترامپ، هدف یک طرح ترور پیچیده از سوی یک تروریست تحت آموزش سپاه پاسداران انقلاب اسلامی قرار گرفته که با انگیزه انتقام‌جویی از کشته شدن قاسم سلیمانی طراحی شده بود.
بر اساس این گزارش، متهم که یک تبعه عراقی ۳۲ ساله به نام «محمد باقر سعد داوود الساعدی» است و به تازگی دستگیر شده، عهد کرده بود برای «به آتش کشیدن خانه ترامپ»، دختر رئیس‌جمهوری آمریکا را به قتل برساند.
منابع اطلاعاتی اعلام کرده‌اند که الساعدی حتی نقشه و جزئیات معماری عمارت ۲۴ میلیون دلاری ایوانکا ترامپ و همسرش جارد کوشنر در فلوریدا را در اختیار داشته و پیش از این با انتشار تصویری از موقعیت این خانه در شبکه اجتماعی اکس (توییتر سابق)، به زبان عربی تهدید کرده بود که «نه کاخ‌ها و نه سرویس مخفی آمریکا» نمی‌توانند از آن‌ها محافظت کنند و انتقام تنها مسئله زمان است.
وزارت دادگستری ایالات متحده اعلام کرده است که الساعدی از مهره‌های بلندپایه در حلقه‌های تروریستی وابسته به ایران و کتائب حزب‌الله عراق به شمار می‌رود که در تاریخ ۱۵ مه در ترکیه بازداشت و به آمریکا مسترد شد. او در ایالات متحده با اتهاماتی سنگین پیرامون هدایت و اجرای ۱۸ حمله و تلاش برای ترور در سراسر اروپا و آمریکا مواجه است؛ پرونده‌ای که شامل بمب‌گذاری در یک بانک در آمستردام، حمله با چاقو به دو شهروند یهودی در لندن، تیراندازی به ساختمان کنسولگری آمریکا در تورنتو و آتش‌سوزی عمدی در معابد یهودیان در بلژیک و هلند می‌شود.
این متهم که به دلیل وابستگی به قاسم سلیمانی او را مانند پدر خود می‌دانست، پس از کشته شدن سلیمانی در حمله پهپادی شش سال پیش آمریکا در بغداد، تحت آموزش‌های نظامی و اطلاعاتی ویژه سپاه پاسداران در تهران قرار گرفت و ارتباط نزدیکی نیز با جانشین او، سردار اسماعیل قاانی، برای تامین مالی شبکه‌های تروریستی خود داشته است.
اطلاعات فاش‌شده نشان می‌دهد الساعدی با وجود نقش برجسته‌اش در شبکه‌های تروریستی، حضور بسیار فعالی در شبکه‌های اجتماعی نظیر «اسنپ‌چت» و «اکس» داشته و تصاویری از رایزنی‌های نظامی خود با قاسم سلیمانی را نیز به اشتراک گذاشته بود.
او با تاسیس یک آژانس مسافرتی مذهبی و با سوءاستفاده از یک «گذرنامه خدمت عراقی» که سفر بدون تشریفات امنیتی و اخذ آسان ویزا را برای او ممکن می‌ساخت، به راحتی به کشورهای مختلف سفر کرده و با گروه‌های تروریستی ارتباط می‌گرفت.
الیزابت تسورکوف، پژوهشگر انستیتو «نیولینز» که خود ۹۰۳ روز در اسارت کتائب حزب‌الله بود، تایید کرده که روابط الساعدی با سلیمانی و قاانی فرصت بزرگی برای گروه‌های شبه‌نظامی عراقی ایجاد کرده بود. الساعدی که در زمان دستگیری در ترکیه در حال سفر به روسیه بود، هم‌اکنون در سلول انفرادی بازداشتگاه متروپولیتن بروکلین، در کنار دیگر زندانیان سرشناس نگهداری می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/75631" target="_blank">📅 04:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75630">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJAfFWdhyMkpmJWy_YLwS1WwIzYeRm-5FWb7vW45wq4k2R1lAlaKZFtdZVBEhonF_Riic1At7KjnvPAOiV9O4xjVKsukSqcV0iIdRsBhhtosvMi4uiaqQToptZVHybsiC9P_GyXzEed8QnEf1G9ECBs_exX-cGcpA-FGXGI_qQAulDcnHim9IIzHuaPKRvnKoFQ0jm-8yWysb47mT-5XoP4Fa_kNE5aAkSlDCBiPPGpEZMSyUEFV1Md5oy6AjrQ3jSeBSXjc-yTFOqxoZArZrEiTkb84vrWj64WR6co3SzVO1029AcHwDMxlD5eUQtanyXtY2-UGkfvd-14yTJFarw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس گزارش داد که آمریکا در حالی خود را برای دور تازه‌ای از حملات نظامی علیه ایران آماده می‌کند که تلاش‌های دیپلماتیک همچنان ادامه دارد.
به گزارش سی‌بی‌اس نیوز، منابعی که مستقیم در جریان برنامه‌ریزی‌ها قرار دارند می‌گویند که دولت ترامپ روز جمعه در حال آماده‌سازی برای حملات تازه بود هرچند تا عصر جمعه تصمیم نهایی گرفته نشد.
آقای ترامپ در پیامی در شبکه‌های اجتماعی اعلام کرد که «مسائل مربوط به دولت» مانع از حضور او در مراسم ازدواج پسرش، دونالد ترامپ جونیور در روز شنبه خواهد شد.
او قرار بود تعطیلات آخر هفته را در مجموعه گلف خود در ایالت نیوجرسی بگذراند، اما اکنون به کاخ سفید بازمی‌گردد.
چند منبع نیز گفته‌اند که برخی اعضای ارتش و جامعه اطلاعاتی آمریکا برنامه‌های تعطیلات خود را لغو کرده‌اند؛ اقدامی که در انتظار احتمال حملات تازه انجام شده است.
به گفته این منابع، مقام‌های دفاعی و اطلاعاتی آمریکا در حال به‌روزرسانی فهرست نیروهای آماده‌باش در پایگاه‌های خارج از کشور هستند؛ همزمان با خروج بخشی از نیروهای مستقر در خاورمیانه، در چارچوب تلاش برای کاهش حضور نظامی آمریکا در منطقه و نگرانی از واکنش احتمالی ایران.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/75630" target="_blank">📅 04:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75629">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/di49PUZn6TgsNQCFSsPnheNgxruGHOG267c0_lRRIBjre5Cxvm71pZoR0D0iBuDw17FyR9uM24APUtOPArpqKvNxOBfg-Xn06PMw0xXq-U31e5WD8Kpmi06NVscq6xb1VOKCr0aYtzt3C2vj7NNnl97fXp7tf7Vueh3axT_yCcw8bmNRp19gEMlS3cmp727-coeJKZsSG68ywO_TYIvn4yT6ojobS9sIpnT6zoqoTHy6HphVgE7sjQYuwfZHXlbjHfiwyy-nAvaJhZxFpQufoW2iIrJMMSpmqgRGRaVOjkweXAj-Qdizurw6AQNe8cXFiZf_L7opRzTR2oyYYHFDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه با تیم ارشد امنیت ملی خود در کاخ سفید دیدار کرد تا سناریوهای مختلف در صورت شکست مذاکرات و احتمال آغاز حملات جدید علیه ایران را بررسی کند.
در این نشست حساس که با حضور مقامات کلیدی از جمله جِی‌دی ونس، معاون رئیس‌جمهوری، پیت هگست، وزیر جنگ و جان راتکلیف، رئیس سی‌آی‌ای، برگزار شد، ترامپ در جریان آخرین وضعیت دیپلماسی قرار گرفت.
نشانه‌های جدی از تغییر برنامه آخر هفته رئیس‌جمهوری، از جمله لغو سفر به باشگاه گلف بدمینستر، بازگشت به واشنگتن و حتی عدم شرکت در مراسم عروسی پسرش، دونالد ترامپ جوان، نشان‌دهنده وضعیت اضطراری در کاخ سفید است.
منابع نزدیک به ترامپ می‌گویند او از روند کند مذاکرات ناامید شده و به سمت گزینه نظامی متمایل شده است، هرچند هنوز تصمیم قطعی برای از سرگیری جنگ اتخاذ نشده است.
در همین حال، تهران به کانون تلاش‌های دیپلماتیک «لحظه آخری» برای جلوگیری از شعله‌ور شدن دوباره جنگ تبدیل شده است.
عاصم منیر، فرمانده کل ارتش پاکستان، به عنوان میانجی اصلی، در سفری حساس وارد تهران شده و قرار است با احمد وحیدی، از فرماندهان کلیدی سپاه پاسداران دیدار کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/75629" target="_blank">📅 00:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75628">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bfj205fK1JtK0_PBNgVVT8euEfWJGD2BLsKGQ2GVD4AoCfCwgIxboftqH2SQxoQeCvm-3cfZqxusxv0vXGYiAhqFQwxu_ooazSiTuRzVrTIcqQPvoonRBqZwpHjNkdVRyKWpHycj39D_9Znl9nhK5sfIB-pdKa6lealUnOBUYQB9ubjIrFpAPD6dAMBmH37SZWVwtd8tT0_mgwSEecVpqHf8eeVohoduOMrqCOcoESKpNI-DAfK7T9ebzN4NgQkOkt1Zr_dNRfxmolu116HUnF2O6QFiumW0P0HoKc9dL9oU16D3DmBiymwoyVvE1kXfArjkwqxQb6cuAO0Zw8hAkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از یک منبع نزدیک به ترامپ نوشت که رییس‌جمهوری آمریکا در روزهای اخیر به‌طور فزاینده‌ای کلافه شده و احتمال انجام یک عملیات نظامی نهایی و گسترده را مطرح کرده است؛ عملیاتی که پس از آن بتواند اعلام پیروزی کرده و به جنگ پایان دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/75628" target="_blank">📅 22:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75627">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VY_TRQU1ApKr0NjOjKkJb54HykqAYj6xk1alTiXR15BeYX8PUD7VxlghVsJa3yQly5pDIzNN6jiDTgK90TaCH3DlDzqeQiE6Y1yMULWmkypFdaH9HHBml9xYawG9eEUBqrAhVc8yeFUmOcm8DDD6WecepFqrQme2KNxHQ5DIai8FKDWPokCWbDDyPyyRah2MmDIwqkuUDMoSnxIz6SJbxbGe6mgtcLoWT0jMfIFSvdxauHadcWvTHAwq8EIm4tCEj1uwyxXzegmxFJjAepAjusEeAkqPGeUHYu07MksDTx46S7kKCP2mV2bgEzLlN-YleHYlWMm-Jo3frgH33U1nqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی هیئت مذاکره‌کننده ایران با آمریکا روز جمعه گفت که موضوع پرونده هسته‌ای ایران در این مرحله مورد مذاکره نیست و از اختلاف نظر عمیق با آمریکا خبر داد.
اسماعیل بقائی گفت: «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
او گزارش‌ها درباره قریب‌الوقوع بودن توافق با آمریکا را رد کرد و اعلام کرد: «نمی‌توانیم بگوییم ضرورتاً به جایی رسیده‌ایم که توافق نزدیک است.»
بقائی بار دیگر موضع جمهوری اسلامی درباره برنامه هسته‌ای و اورانیوم غنی‌شده را تکرار کرد و گفت مواضع ایران قبلاً اعلام شده است.
@
VahidHeadline
سخنگوی وزارت خارجه ایران حضور هیئتی از قطر را در تهران تایید کرد
اسماعیل بقایی،‌ سخنگوی وزارت خارجه ایران تایید کرد که یک هیئت از قطر روز جمعه در تهران بودند و با عباس عراقچی وزیر خارجه ایران گفت‌وگو کردند.
او بدون ارائه جزئیات گفت که کشورهای مختلفی طی روزهای اخیر با وزیر خارجه گفتوگو کردند اما تاکید کرد که میانجی اصلی میان ایران و آمریکا همان کشور پاکستان است.
پیشتر رویترز به نقل از یک منبع آگاه گزارش داد که هیئتی از قطر در هماهنگی با آمریکا وارد تهران شده است.
قطر و امارات و عربستان سعودی سه کشوری بودند که آقای ترامپ روز دوشنبه گفت که به درخواست آنها فعلا حمله مجدد به ایران را متوقف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/75627" target="_blank">📅 22:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75626">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpjoLtVwB9bCR-7ErgujYzMT9W8A_Sb1e7XtojBKcNieV6GcTJ2gELo1RRDghqp0BTErAdgBAOVAkRCUV6XoC_WCUV1AdezJ5T93Pe5On01WpQgBkHXIuyMmQHG6IlRbFxVNvtv37EkA43pAcnkqBGdwgAff5YeDInXp78yc3cYLDdDer393pnICM5u3j60rvjHQsEFOVtuby7Py4C2pdiedCX9AMdl_BPtimrLkz93UE14Iq5ebUCLfPFfJdAxlbuX8u0IiLy2Petzoh4OiCOuOAXlvUXz3arTPe6mpN0noJBNuUDMXxOCS4lzn2UbxY0AQT44-ljv3HDDfizED4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از عاصم منیر، فرمانده ارتش پاکستان که امروز جمعه یکم خرداد۱۴۰۵ وارد تهران شد و مورد استقبال اسکندر مومنی وزیر کشور قرار گرفت. خبرگزاری آسوشیتدپرس پاکستان نیز به نقل از منابع امنیتی اعلام کرده‌اند که عاصم منیر در طول این سفر رسمی، درباره «مذاکرات جاری ایران و آمریکا و صلح و ثبات منطقه‌ و منافع دوجانبه دیگر» با مقام‌های ایران گفت‌و‌گو خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/75626" target="_blank">📅 22:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75625">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GPkthl53O78baM2lAwpZDcOPxfG9szhDA5s0-WiVGomGq4rcMae9tzz3IFkl8_NfWWuywWF7MqDf9BB-c0NfJqEegrZGHt4t-sAj4TXXJFt6iW5-jK4Z3Fvp8llROivAhqOynWtwG90zlN6y-lXNDS_N4xuTSyvQIbRk0YZZfmH3C8Rg4UwoQzdDYPZPwSVCV2y9_bN0aZI5-jNkQXZ44tGC5bNollM6DVe9cnlW-k54OzGF1oGsMkPScsVGrVL5gW-IfL-l1fbnzAEvrktSDe36-_1gNcS4hDfeP_2_P0sQ8P5fQQBAte-QVPAn_PQhaAI-Vpc5c0KXJDxmOpaXJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فاکس نیوز»: تولسی گابارد از پست خود به عنوان مدیر اطلاعات ملی آمریکا استعفا کرد.
AlArabiya_Fa
پست ترامپ، ترجمه ماشین:
متأسفانه تولسی گبرد، پس از آنکه عملکردی بسیار خوب داشت، روز ۳۰ ژوئن دولت را ترک خواهد کرد. همسر فوق‌العاده او، آبراهام، به‌تازگی به نوعی نادر از سرطان استخوان مبتلا شده و او، به‌درستی، می‌خواهد در کنار همسرش باشد و در حالی که این نبرد دشوار را با هم پشت سر می‌گذارند، به بازگشت او به سلامتی کمک کند. تردیدی ندارم که او به‌زودی بهتر از همیشه خواهد شد.
تولسی کار فوق‌العاده‌ای انجام داده و دلمان برای او تنگ خواهد شد. معاون اصلی و بسیار محترم او در دفتر مدیر اطلاعات ملی، آرون لوکاس، به‌عنوان سرپرست مدیر اطلاعات ملی خدمت خواهد کرد.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
از سوی دیگر رویترز به نقل از یک منبع آگاه از موضوع، نوشته که او ادعا کرده کاخ سفید خانم گابارد را برای کناره‌گیری «تحت فشار» قرار داده بود.
پیشتر اختلاف دیدگاه‌هایی بین رئیس‌جمهور ایالات متحده و مدیر امنیت ملی‌اش، بخصوص در قبال ایران بروز کرده بود. دونالد ترامپ در فروردین‌ماه هم اشاره کرده بود که از نظر او، تولسی گابارد در قبال برچیده‌شدن بلندپروازی‌های هسته‌ای ایران، «موضع نرم‌تری» دارد.
خانم گابارد بیش از یک سال پیش، پنجم فروردین‌ماه ۱۴۰۴ به کنگره گفته بود که ایران در حال ساخت سلاح هسته‌ای نیست.
مدیر اطلاعات ملی آمریکا که برای ارائۀ گزارش سالانۀ نهادهای اطلاعاتی ایالات متحده به همراه رئیس سی‌آی‌ای و مدیر اف‌بی‌آی در جلسه استماع سنا حاضر شده بود، تأکید کرد که بر اساس ارزیابی نهادهای اطلاعاتی، علی خامنه‌ای رهبر وقت جمهوری اسلامی، درباره تعلیق برنامهٔ تسلیحات هسته‌ای ایران، که در سال ۱۳۸۲ فرمان آن‌را صادر کرده بود، تجدیدنظر نکرده است.
با این حال خانم گابارد بعد از مدتی، موضع‌گیری خود در این زمینه را تغییر داد.
تولسی گابارد که مسیر سیاسی پرفراز و نشیبی داشته، پیش از پیوستن به حزب جمهوری‌خواه و ورود به دولت دوم دونالد ترامپ، عضو حزب دموکرات و نمایندۀ هاوایی در مجلس نمایندگان بود.
او هفت سال پیش، زمانی که خود را برای رقابت به‌عنوان نامزد حزب دموکرات در انتخابات رباست جمهوری آماده می‌کرد، گفت که در صورت پیروزی در این انتخابات، ایالات متحده را به توافق هسته‌ای با ایران باز خواهد گرداند.
خانم گابارد در آن زمان در گفت‌وگو با شبکه تلویزیونی فاکس‌نیوز هشدار داده بود که ایالات متحده در آستانه جنگ با ایران قرار دارد.
تولسی گابارد نخستین و تنها مقام ارشد امنیتی یا نظامی دولت دونالد ترامپ نیست که کناره‌گیری کرده یا وادار به کناره‌گیری شده است.
در آخرین روزهای سال ۱۴۰۴، جوزف کنت مدیر وقت مرکز ضد تروریسم آژانس امنیت ملی آمریکا، که مستقیماً از سوی دونالد ترامپ منصوب شده بود و زیر نظر تولسی گابارد انجام وظیفه می‌کرد، در مخالفت آشکار با جنگ ایران، کناره‌گیری کرد.
@
VahidHeadline
خبر یک ماه و نیم پیش:
ترامپ قصد داشت گابارد را اخراج کند
به گزارش وب‌سایت آکسیوس، دونالد ترامپ تا آستانه اخراج تولسی گابارد، مدیر اطلاعات ملی آمریکا، پیش رفته بود، اما مداخله لحظه آخری راجر استون، مشاور قدیمی و نزدیک او، مانع از این اتفاق شد.
دلیل خشم ترامپ به شهادت اخیر گابارد در کنگره بازمی‌گردد؛ جایی که او برخلاف انتظار، از جنگ با ایران حمایت تمام‌عیار نکرد.
طبق گفته منابع آگاه، ترامپ از اینکه گابارد در اظهاراتش اعلام کرده بود برنامه هسته‌ای ایران پیش از آغاز جنگ «منهدم» شده بود (موضعی که توجیهات ترامپ برای حمله را تضعیف می‌کرد)، به شدت ناراضی بود.
همچنین استعفای اعتراضی جو کنت، دستیار گابارد که جنگ را غیرضروری خوانده بود، بر آتش خشم ترامپ افزود.
در حالی که ترامپ در حال نظرسنجی از مشاورانش برای جایگزینی گابارد بود و وفاداری او را زیر سؤال می‌برد، راجر استون در تماسی تلفنی از او دفاع کرد. یک منبع نزدیک به آکسیوس گفت: «راجر معامله را جوش داد و تولسی را نجات داد.»
استون نیز بعدا در شبکه اجتماعی ایکس تایید کرد: «خوشبختانه به موقع اقدام کردم.» با این میانجی‌گری، گبرد فعلا در سمت خود ابقا شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/75625" target="_blank">📅 21:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75624">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oPGOv7746w-1MJPoMVfGT-BhLyRoX1TrV0F3vjEmSSTeZNxJ4xyBXJIqUxduH49iVI_vxhjbm4-yn_shY_3dV4t4sWvoU_PsKY8jTJG2SBk2Dt05J2RT0UCQ3K1xjvpBUqMFxpe0S5sARaJJIbmyTZA5iPuT8uQlivYUJ1w7E0Q6Kfj4pwH1era1HyKeAQRtAYtQDZDVj7zg38rfJXiBWyzIbw3URKc8mMmlxD2xDqTGNIGId3GZ_as2NC2MESICUQhKoTJ567EaMUC2lDefy0AKzuBg1GMxS8e_tgOJznExoJG6uZvC0EfsaiMdv4UFvZeOOO3CdroUfpW2AJ3Xvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست
ترامپ درباره شرکت نکردن در مراسم ازدواج پسرش
ترجمه ماشین:
با اینکه بسیار دوست داشتم کنار پسرم، دان جونیور، و جدیدترین عضو خانواده ترامپ، همسر آینده‌اش بتینا باشم، شرایط مربوط به دولت و عشق من به ایالات متحده آمریکا اجازه چنین کاری را به من نمی‌دهد.
احساس می‌کنم مهم است که در این دوره مهم زمانی، در واشینگتن دی‌سی و در کاخ سفید بمانم.
به دان و بتینا تبریک می‌گویم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
دیروز:
ترامپ با اشاره به مشغله‌های شدید خود گفت: «به پسرم گفتم الآن زمان‌بندی خوبی برای من نیست؛ موضوعی به نام ایران و مسائل دیگر را در دست دارم. این از آن مواردی است که اگر در عروسی شرکت کنم، توسط رسانه‌های اخبار جعلی سلاخی می‌شوم و اگر شرکت نکنم هم باز من را می‌کشند!»
@
VahidOOnLine
رسانه‌های امریکایی نوشته‌اند که دونالد ترامپ جونیور، ۴۸ ساله، قرار است در پایان هفته جاری با بتینا اندرسون، مدل و چهره اجتماعی ۳۹ ساله در یک جزیره خصوصی در باهاما ازدواج کند.
بر اساس گزارش‌ها، این زوج در ابتدا به برگزاری مراسم عروسی در کاخ سفید فکر کرده بودند، اما بعداً تصمیم گرفتند مراسم کوچک‌تری برگزار کنند. دلیل این تغییر، نگرانی از واکنش عمومی به برگزاری یک مراسم پرزرق‌وبرق در زمانی خوانده شده که امریکا با تنش‌های مربوط به ایران روبه‌رو است.
afintl
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/75624" target="_blank">📅 20:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75621">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjqMRu_Mk_9hR1CqSubOYUPs3CQxFdJLG68mwRJGCmamaCTFyXcHVzKPJwVbObsS9-LARXcwPZXQuZobvNxKHU-BCVUYwKKI-w54RFrofnAFFpCHKxc6Ic9I9SdMlrZiHtTutthYYm_iOJPGgQGrqAltlxHZ3s7AX0qq076NYdMcEyvxUgXiI2K-V-6DPwTY0jAGCLxvfyb7sPAvh9UDt_RyGKYof8F4o3Qe8mTl4Q41RJ1Pp_B8Wxq6Y5gYC8QvME5JqwsAz7rpztBqDFOlAyLO42rz0miIdthdlRIN9yFVeMcubdqFjAVzUT6w6g6iB_LnDwW84VApBlONhsKeeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twqWI969uDR7MuFN25RWHKJBB7-cLN-ct36StjfIlHwCHw5NRDqfGrWkEU3Y-jJn4emxAwgddh1Up2fDOZ0jHoISRER580zgmFcAWXpHWDUghtqwmeRGFfW3xwKeX4jo09Kre8PEqeCGZZVT6dlaWQzIIIM43N_SYKceDWu6cffNJHuVyc0DfEAzCxyln4g8fmV6AMid_a6rZxyvT0VZsbOphvVmPZvZ2KiwsNi3bS5kJpWWDQOVY6cKqZfvUJFCFYVopYK04MNs_QUm91Xv6nvYYCqJs14OIi9UicK0VCwLKKdm0dzvZeB6SA459iOjYI4IFXQKKAN0W_d55MEB-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WHsGDU10vW_rX0Li88DOzwslU8QTnyaJyRHP5AswEF6-UmI4F0yUJQbEgtzBTTT8RRM7fYk89_LdOrKCqrgk7KiscLV3xssoMqChuLwKEm5c1OmByYK0CokisDDeC-d2aL07dA-sWocK5iL0jGzjCcwDQB5HSKEiXJv8Ea_goRhBBvtfgLpspPWfQSemx_xrsoYiyjsj219HmpKJuqSczlX8dS90QbfSltE-pc-6gBR8Q8FNigkuJ0OSaTBDmmylgnWZyPRHdhOHIVSZ63vTZ6H8enUTd4IZhqvTMrhROoL9iM3W9Uhg3aeWJk1U7JTApSOAKq_HrlaRuyzD3KboTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
بنیاد عبدالرحمن برومند تا کنون ۶۵۵ مورد اعدام را در سال ۲۰۲۶  ثبت کرده است، که ۳۴ مورد که از آغاز ماه می تاکنون اجرا شده است.. آمار واقعی احتمالاً بسیار بیشتر از این رقم است. جمهوری اسلامی در حالی این اعدام‌ها را پشت درهای بسته اجرا می‌کند که  ۸۳ روزه است که اینترنت کشور قطع شده است. حاکمیت با قطع ارتباط جامعه از ۹ اسفند ۱۴۰۴  صدای زندانیان، خانواده‌ها و شاهدان عینی را به شدت سرکوب کرده و نظارت مستقل بر وضعیت حقوق بشر را به‌طور خاص دشوار ساخته است.
🔸
از آنجا که دستگاه قضایی همواره تنها بخش کوچکی از احکام مرگ خود را به‌طور رسمی اعلام می‌کند، قطع اینترنت داده‌های فعلی را به شدت محدود به منابع دولتی ایران کرده است. بنابراین کاهش در آمارهای ثبت‌شده، تنها نشان‌دهنده خفقان اطلاعاتی است، نه کاهش کشتار.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/75621" target="_blank">📅 18:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75620">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bPqcucaJCcrb7MouHJ_jV-Ivialw6lZJjvJTPgqBeVBY6NABXuYmF7FbpoeacdsvnXdOuyli8aX-jHZ0LQETgwHTQBGqj4NllOZb_UN3dfadC1VduapERQKfWjmEwPDfeRNipHpKzaczifv9LB_krC9Gbj2vSaTmVihuC2kCMMohXL2ZG5sAOy8yMJY6_ZTEXV3nun9AvkXSSNyAcxZyU3QNq9vMmMCdwhABSAaTtFYjHIbl_Uz4mtUHgoDFdMCKAW05li_SY9GY7vwRiiBG-GXUlEb9X9pwcZVOyIX5vbAh872CS9QfvgHRRq8l0CNlJjn1g116NE8P1zVLx6d7Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختر حسین ناصری:
MNaseri23595
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/75620" target="_blank">📅 18:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75619">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MH4ubX3GKv9bTb0LF3RTMzcuY9RDDuKPU2IWa3gV1Hkkn7VPanR26H8iO3HGaW5MHfbw1WZFxxANMNMt6h33X8CxUQKAixk2mvG_gPo-OaBOafp5CdHCT_PgWYgPdBa0mrLgLgsEhpxdKz27F8f76WFKbCgzW20W128XgcWifZUClJ0eh_mvjR2G1SXtQds7dqovxR0mZ86bEq6Y8TYSOXnhzRVxzD9VilGKiIjfwzsY9tImCqDgbnPveSAXlurOV5k0or6Enq3Shl6pfFjToqpNgRbXAE7wu03Or_XtJnqpDb05Kq9IHJfFRlwB__x6DY4IttsZ004PlFTjZtzn4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رسانه‌های دولتی پاکستان، فیلد مارشال عاصم منیر،‌ فرمانده ارتش این کشور راهی تهران شده است.
خبرگزاری اسوشیتد پرس پاکستان به نقل از منابع امنیتی گزارش داده است که فیلد مارشال عاصم منیر در طول این سفر رسمی، درباره «مذاکرات جاری ایران و آمریکا و صلح و ثبات منطقه‌ و منافع دوجانبه دیگر» با مقام‌های ایران گفت‌و‌گو خواهد کرد.
فرمانده ارتش پاکستان چهل روز پیش هم در تهران بود و با محمدباقر قالیباف و اعضای تیم مذاکره‌ ایران و آمریکا دیدار و گفت‌وگو کرده بود.
این در حالی است که وزیر کشور پاکستان هم برای دومین بار طی هفته اخیر به تهران رفته و در حال گفت‌وگو با مقامات ایرانی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/VahidOnline/75619" target="_blank">📅 17:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75614">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BXOazYje9DvSXD1-WHNQ_XakGXx8TD3CrJ4H6AtbeZg1gX5IEJgAnqsDgbRSWL6p-ORSBlfea_HtYErQnXAd-_-dDbzqRjp_ZQZO03Rha1pdaUxbcoN1MIzlMs1zHddHbfqv9nvgEe5Ntpa6TELkKzGe5NafezUuEfQrxbLW5iG0ypgiYckI32P4VcvZ5eYeuTVJS9vEhYojDtlyKvBOsnCxvn7ZdmdxEyAQ0F5AECnl9dcQqRyI09qdHgm4NbEyLsNqMnQnrBoC4J-iykJ0RXAu88MeA8hX3nhhl9huMmVs5z4jU2zDZ4aOa3UjiibcMVQol21QlcZ3wm3ZUAMMAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tkDo9FCZjKZUWdMArSSv1vIdelznyORaTzwqQiVVoa7srX5zDqycT6METEYUjij9CEMZ7Atz8UvP0T8EucK-jG5p2NgS-7U6_Yq0CYmRk1iojYKRFztrWkG1rz_LVB44aWZEB-LKFJ0ohBXA8jRfbp9rvWDVRHZIHkINultzf0c552fgwK06xroHrFPmy42d4_W_Fex7p1ch4e-U0a-0OVuNE1lcsC7V_-usccluS6G3wKxgPSMEZgoGYqVs17NEtkrGt-BhwvRFQRNLdYHFn8xhwRrTMHnpFEz9upeEojnsqomjObxcz0QuLuKVdl3z6jMGa9olI0jUiTknUaJsPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9fabcfc83.mp4?token=bP7ddbeMTNyyEmHQ5tXvvzjRIvkdRzt0k01S2K1hyyRebClgFI5E7Iy-Ioj_pm8qkelhZF5HIQ4GMAhCLVfMKaa-kSc32P7iMMC3czcVsmaXZWv_peitejN3HatL-U5_xsmuQ6g-ek5slWAr8hjr8fH1XDlOR0LKLzd6Hc181GZXapvBBNCTubogz-XHvXV4-k8yxf_-XLQNStY4Iy7dVouYrSw_M0bY2wTF-hgDG5qi5lFPjX_Wk0_cFtk09q4sKex9ZWdty3L4M1IvwLh6hvXNEJhaVV7s5AghBtp7ZgjEh9MdlDh2srSNBUoqs_JybIVuKM1FGbm_ufL1FRr82w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9fabcfc83.mp4?token=bP7ddbeMTNyyEmHQ5tXvvzjRIvkdRzt0k01S2K1hyyRebClgFI5E7Iy-Ioj_pm8qkelhZF5HIQ4GMAhCLVfMKaa-kSc32P7iMMC3czcVsmaXZWv_peitejN3HatL-U5_xsmuQ6g-ek5slWAr8hjr8fH1XDlOR0LKLzd6Hc181GZXapvBBNCTubogz-XHvXV4-k8yxf_-XLQNStY4Iy7dVouYrSw_M0bY2wTF-hgDG5qi5lFPjX_Wk0_cFtk09q4sKex9ZWdty3L4M1IvwLh6hvXNEJhaVV7s5AghBtp7ZgjEh9MdlDh2srSNBUoqs_JybIVuKM1FGbm_ufL1FRr82w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، در حاشیه نشست ناتو درباره مذاکرات جاری با جمهوری اسلامی گفت که واشینگتن در انتظار نتایج گفت‌وگوهای در حال انجام است؛ گفت‌وگوهایی که به گفته او نشانه‌هایی از پیشرفت داشته‌اند.
او افزود: «ما در انتظار نتایج این گفت‌وگوها هستیم که نشانه‌هایی از پیشرفت دارد. نمی‌خواهم در این باره اغراق کنم؛ تحرک محدودی صورت گرفته و این مثبت است، اما اصول اساسی تغییری نکرده است.»
وزیر خارجه آمریکا تاکید کرد که حکومت ایران هرگز نباید به سلاح هسته‌ای دست یابد و گفت: «برای تحقق این هدف، باید به مسئله غنی‌سازی و نیز موضوع اورانیوم با غنای بالا رسیدگی کنیم و افزون بر آن، موضوع تنگه هرمز را نیز مد نظر قرار دهیم.»
@
VahidOOnLine
مارکو روبیو، وزیر خارجه آمریکا، جمعه یکم خرداد در حاشیه نشست ناتو گفت جمهوری اسلامی در پی ایجاد نظامی اختصاصی برای اخذ عوارض در یک آبراه بین‌المللی است و تلاش می‌کند عمان را نیز به پیوستن به این سازوکار متقاعد کند. روبیو تاکید کرد که این اقدام «غیرقابل قبول» است.
او افزود: «هیچ کشوری در جهان نباید چنین چیزی را بپذیرد. من کشوری را نمی‌شناسم که جز ایران از آن حمایت کند.»
روبیو با اشاره به تحرکات دیپلماتیک در سازمان ملل متحد گفت قطعنامه‌ای با پیشنهاد بحرین در شورای امنیت مطرح شده که آمریکا در آن نقش فعالی داشته و به گفته او، بیشترین تعداد هم‌پیشنهاددهنده را در تاریخ شورای امنیت دارد. او هشدار داد چند کشور در حال بررسی وتوی این قطعنامه هستند و افزود: «این مایه تاسف خواهد بود.»
وزیر خارجه آمریکا تاکید کرد واشینگتن برای دستیابی به اجماع جهانی جهت جلوگیری از اجرای چنین طرحی تلاش می‌کند و گفت: «باید دید آیا سازمان ملل همچنان کارآمد است یا نه. ما می‌کوشیم از این مسیر به نتیجه برسیم.»
او تصریح کرد اگر اخذ عوارض در تنگه هرمز اجرایی شود، ممکن است در دیگر آبراه‌های مهم جهان نیز تکرار شود و افزود: «این قابل قبول نیست و نمی‌تواند رخ دهد.»
روبیو با اشاره به اهمیت تنگه هرمز گفت این آبراه برای کشورهای حاضر در نشست و نیز برای دیگر کشورها، به‌ویژه در منطقه هند-آرام، حیاتی است.
او در پایان با ابراز امیدواری نسبت به نتایج نشست ناتو گفت این دیدار زمینه را برای نشست رهبران در حدود شش هفته آینده فراهم خواهد کرد و افزود که تا آن زمان کارهای زیادی پیش رو است.
@
VahidOOnLine
مارکو روبیو، وزیر خارجه آمریکا، پس از نشست ناتو در سوئد درباره مذاکرات با تهران گفت: «همه ما دوست داریم توافقی با ایران شکل بگیرد که در آن تنگه‌ها باز باشند و ایران از جاه‌طلبی‌های هسته‌ای خود دست بردارد.»
او افزود: «این چیزی است که همه ما امیدواریم و همچنان برایش تلاش خواهیم کرد و همین حالا هم که با شما صحبت می‌کنم، کار و مذاکرات در این زمینه ادامه دارد.»
وزیر خارجه آمریکا با اشاره به این که باید یک «برنامه جایگزین» هم وجود داشته باشد، گفت که برنامه جایگزین در صورتی باید عملی شود که حکومت ایران از باز کردن تنگه‌ هرمز خودداری کند.
او گفت: «پس باید از الان درباره‌اش فکر کنیم. من امروز این موضوع را مطرح کردم. واکنش‌های تاییدآمیز زیادی دیدم. اما هنوز چیزی برای اعلام رسمی درباره اقدام مشخصی که در حال انجام باشد نداریم.»
وزیر خارجه آمریکا درباره برنامه جایگزین در صورت امتناع جمهوری اسلامی از بازگشایی تنگه هرمز افزود: «نمی‌دانم لزوما این می‌تواند ماموریت ناتو باشد یا نه، اما قطعا کشور‌های عضو ناتو می‌توانند در آن مشارکت کنند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/75614" target="_blank">📅 17:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75611">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZUmCWnf7Bx_EuYTHYGc0LWI6n68j1BPQSlzQX82MF7Z8nywWas6GBiXHBzfB7DJg8S_OlP5_OybeBCveVaNNEJ7dNOMTXKO5JacdwBjzGdUaxNEKyl1W1VuW1buCKK4M-3ozBkza40x8xoPZQtrhdNRAIQQqTljIHbQtS2VGppxIIEWUutZQkaRVKzEyDTg8WZgdc6Un73jsoP-eoAROmZezAAC4Ld7g2I245_jW9NYMiY3vfGpXqFYVM3pr-BmAQTt-I5WD4mBDUn6xcCjkMDBmhHG0CMjtIsl51v_fYHyn37Xsigz6NAg3VgG4VF8_pNtolLhZ4IRgRPB9a-ZV2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EHvY3LGNbu203RoeCDxWjVMMqHXrEsTRSGwKLLw2BKftJiWZMiikkRIevJJwGqpL_OLPgkjpyvrCeP0xfseYi9B8_WxFPGD3fUre9GTJUK72STndtyNCdBwAErDMuCBUDFMRQG5ox10NM0t_Am5AjJnek9jNZeWInHihOjgnHlaw89QKJTBo6EmDwGJ2O2Zqjus9acD73P_WeMGg-HqR6Z02qjwAyvaqdZ8hBheJbeTFqWL39MNtZjpZ36ObI5hFdfG0zzGgF6Mw2zYhZnKWE3tKYQ0Zleui-ApAHWvh03OnOBl3zYPc-hDaidIhXgEzhPsoDaXPAqdSpevDoNhbKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-ngJlhsxEGswIWlIv4_SFxVl75NdYJmLkjK_pphk1bHwp8bR1fQEgl2Yu_2oVrPPKdjvw2XHkOBytxjA-9dkI8bMO1KtDDvW5ar4mrLlgJbSO14l3f6LPtjrKuj7aisuJhqbk1oh4q-aoeFiOB3xEXSfbE6kOFXKyQ7gRmGuOD7BSRrZNDOJ3ALAkelsVkn2Rv4VGhsSSxYotg0vHSWiPxS9MFGSL2H_2ltTHPkYFYcoQPKgpelHbOqj9giediZEAdxkrFtYfICZv98FG1Y1W7SbEdDhXoQsSQzgFdCHPFOiOilAjXO-v-1Ys6EmuCn85NxkKJEJmuIyhHtjkx11g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اطلاعیه منوتو درباره پایان پخش برنامه‌ها
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/VahidOnline/75611" target="_blank">📅 17:41 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75607">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WmfZkuCkEkoFPo1zptxQfclIbW-Y3fOlJEF62lcPMRuI6EM1rsjGBFZFfA6wFjMSpoW-drKc-176NTXXyUpF1vGKe6eaubR2PWZSO5_AvyJA081_Q7sC8W2gMAge30eiX7AoP2vEbfRKknJgBbHS75vg1q-ZNkQTRZinl3t2TN9C-ikkRxh6EGc68k7RQ20bqznkZ0RSx7iCJVVSwGEw8UMgt_Qf-OIyUexw1e5ApblrUe-s2HR56DVwaSxkkodmG0GKL2jLd77ElWxqKGzEKM1nBcZoxKPWnxQ2F53977KnshwGq05EhFZDB6loPg_yc02b3AuxRgnTGEPjw7IYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M4GVS6W8HjNTizpMKS0x_hu-n3irg3i7TvMNPFIJp5E1L6L6zQGeOnFkmbHKJm5GCGeiXnqw9b2irUOQG4O_x2ApyikQBSvZ8qIhStiDDByNXwko1Jl6SzHj4SKeBZQilWY2Oe14H4OV1ukx9cgdrZOQyXgaE8SPnmruucpFAL_b2j0UU2wp0MvjyWA6hcrUECLCen4OtNF6aQTQOZW5hP0kPV3BZk1A3zsmfErtvYd6G0SamQZSy8faIgQhlkdXwu0QgiKXBOIjTWRx1NArO6PL8rqidnDrVy2CuElLT5C1abqHq3_KvIY0LTFHFjg7tEC5q2wQv1LODw3vi9gUsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/m9sb1xUQCIrG5ltooOK1ltxggXOfGYh11d7CMLeSV5Q46tgo5-iKIc0WQXvXJTdLuVYJhthqnsJscnrVFlwwhJsBGuJ4LnNiIyOkqaMHM7NDuyOxrHKr2cAtEsZXvgI2fIXuVlf8W0Uch3tKaFD7x0Z54JhVS-94LAAkJH5DRyz8U-tVmGXQi0zvI-6QW-zrr3SaNjTJ_MHXrFQjNR36ghPLIBTzxZnsydVhmADBh3aqo9eFME_2r5Gv0FjFWausrsh3jZOjKPjkVJuYSUMmmX5Kh1Br1qm2o0O-DpmStEWLDJn37f1x-mZgbVtxWJ5HUG21xDdJzIVZX5sRxv3kMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/abdcc0b736.mp4?token=EtS7jIA_Sk6cFG8yxRBxuF63dIFQG2Odg3XZ_IID9bL9XSn7HCXlOanRtW_AZt0eJ5Ncs1x_MdSXzzNxdipG1RXAG15XwVbxgeZEgxM3y4oj_Ftqp1rODM9hcNvKs8_cZD5O04FE0re7JFXim4rEtpeVJa4z5nCDStwDfCQm7kAJrs66dfwKOVGQFO7XLAycIa7FopQ2AewLQsMLNGeS9uVkN7gZtTSfKKWWR4ZtTMuCs5m5WS8SjvBEhtxFwU3hVMXZKPM66gk6ZRxFacMebgvR604wWuCQXvPfdITjlvhM0Zdiysf2VHIS76NY1RyrBtWzGa3D3bv3-9YH_KX5ww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/abdcc0b736.mp4?token=EtS7jIA_Sk6cFG8yxRBxuF63dIFQG2Odg3XZ_IID9bL9XSn7HCXlOanRtW_AZt0eJ5Ncs1x_MdSXzzNxdipG1RXAG15XwVbxgeZEgxM3y4oj_Ftqp1rODM9hcNvKs8_cZD5O04FE0re7JFXim4rEtpeVJa4z5nCDStwDfCQm7kAJrs66dfwKOVGQFO7XLAycIa7FopQ2AewLQsMLNGeS9uVkN7gZtTSfKKWWR4ZtTMuCs5m5WS8SjvBEhtxFwU3hVMXZKPM66gk6ZRxFacMebgvR604wWuCQXvPfdITjlvhM0Zdiysf2VHIS76NY1RyrBtWzGa3D3bv3-9YH_KX5ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم مستند «تمرین‌هایی برای یک انقلاب»، ساخته پگاه آهنگرانی جایزه «چشم طلایی» هفتاد و نهمین جشنواره فیلم کن را از آن خود کرد.
«لوئی دور» یا چشم طلایی، مهم‌ترین جایزه بخش مستند جشنواره فیلم کن است.
پگاه آهنگرانی جایزه‌اش را به مردم ایران تقدیم کرد و گفت: «(مردم ایران) با وجود تمام سرکوب‌هایی که در طول این سال‌ها تحمل کرده‌اند، هرگز از تلاش برای حقوقشان، آزادی‌شان و آرزوهایشان دست نکشیده‌‌اند و مطمئنم که آنها هرگز تسلیم نخواهند شد. مطمئنم و یک آرزو دارم که می‌خواهم اینجا بگویم: این‌که روزی دختر کوچکم لی‌لی و همه بچه‌های ایران در آینده‌ای نزدیک در ایرانی آزاد و دموکراتیک زندگی کنند.»
به گفته خانم آهنگرانی او با استفاده از آرشیوهای شخصی، ویدئوهای خانگی، تصاویر اعتراضات خیابانی، روزنامه‌ها و صداهای ضبط‌ شده، بیش از ۴۰ سال از تاریخ ایران را بازخوانی ‌کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/VahidOnline/75607" target="_blank">📅 17:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75606">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBR6ceWMbQspuGCDJBTOywc5_2DKLxEY9qwiwNz1NHaHsjFc02tRj-Noc5MII6BqORFD_adunGZyE9jXjTLTWjfglJZgQRF5ixOrkMq_jEjXCZBPJ_B8pZoqkSL7zUS-sXGVUR8Cksbs7sc3NEoQLdz21Ot_zNYzEBNWpTyz6f8786HwRAH97O7M0pmGrpH3WO70UhD83qYsI0EMHH3ex6koO9M7FKvrS8erqfJ_MSmvyXOv7lxfb8Dc9PT9M0JosLrkW1u6oRx--M2bH4KpWcKrw84ilYFFhDZHSve4Xfg_Vx5zsnJLPhLPmXk56ZGd0bzRGQICb5zpdVG4yLhqCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشورهای عرب حوزه خلیج فارس از جامعه جهانی خواستند که طرح جمهوری اسلامی برای مدیریت تنگه هرمز را رد کنند.
به گزارش بلومبرگ، در میانه مذاکرات دیپلماتیک سازمان بین‌المللی دریانوردی با ایران و عمان پیرامون بازگرداندن آزادی تردد و امنیت کامل کشتیرانی در این آبراه راهبردی، کشورهای عرب حوزه خلیج فارس طی نامه‌های به اعضای این نهاد زیرمجموعه سازمان ملل، نسبت به طرح جمهوری اسلامی موسوم به «نهاد مدیریت آبراه خلیج فارس» هشدار دادند.
پنج کشور عربستان، امارات، بحرین، کویت و قطر در نامه خود گفته‌اند که به رسمیت شناختن مسیر پیشنهادی جمهوری اسلامی می‌تواند یک «سابقه خطرناک» ایجاد کند.
سفیر ایران در فرانسه روز گذشته تأیید کرد که تهران با عمان درباره اعمال دائمی عوارض عبور در حال مذاکره است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/VahidOnline/75606" target="_blank">📅 17:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75605">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZW3Lz40IxD-wglobVDDw9di2-e9Eg87ja3SjR0bNXJ8zPeATqQwTOo78GFPdIcG2RdX_xAApWc-QJKKxklwmdAskSiDfEjEyEfc6ezTvrDTPF4UJUbCgOFt3K9RSLiN1m4_hhBt3KicFMVBvZC1MZ6o-LINfvYfHDdOMfn7Kzrkw3ic1kxxmSE0N9DE6QC2FXN3jqnfT5Y-d2le-jy3Awg9I9y1ccIOBeBfGJsDN1sTGvknWAJuYnRPZXvnNfaDZLi0WgQkbJEkt1T0yhOj1zhJLM-QTryzTDqBRXCTEJ02anITs_q_s2y4IuWMfoYYVZXGa-QGh2-hDaRAEi7uLJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد بین‌المللی ناظر بر وضعیت اینترنت، نت‌بلاکس، صبح جمعه اول خرداد اعلام کرد قطع گسترده اینترنت در ایران وارد هشتاد‌وچهارمین روز خود شده و بیش از هزار و ۹۹۲ ساعت است که دسترسی کاربران در ایران به شبکه‌های بین‌المللی همچنان قطع است.
این نهاد ناظر بر اینترنت نوشت با ادامه این وضعیت، شکاف‌های اجتماعی و اقتصادی عمیق‌تر می‌شود و هر ساعت از قطع اینترنت، ارتباط با جهان خارج را بیش از پیش به جایگاه، همراهی با حکومت و برخورداری از امتیاز وابسته می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/75605" target="_blank">📅 17:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75604">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB5GROuhbzT6OWO6Wn9KGW4et0ipujOKw2YuRp9AOg8pWMWWMkkE_qkRe0J-bSyDcfpPTNesOjb0yTtmjgS_GfmTbeuSnsgMMXxVUOkqMHoygrGLODEqjk5ogs-7VeCEKYPdBQXOd9afjuvKDtxyDtU7G71W1kqFXsK-2j9rplRkxtjC8h50XaFqQ94L7pSZeJSM3TsJje3wR5Kl4XDfGGCHv3p8MO5AyYzCpuFiGL4IWhtfninWPNj_Gi9VvmXSNUp0RzJNgTHTfgb8yGMJ1KCHH76MFWoiFn-AIV8yw7PnzdcRx-z0sDu9NW9wFxvRXe6wEiyvpWfWMFS6sZFTrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوان عالی کشور احکام اعدام محمدرضا مجیدی‌اصل و همسرش بیتا همتی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، را نقض کرد.
هرانا خبر داد که پرونده این دو متهم برای رسیدگی مجدد به شعبه هم‌عرض ارجاع شده است.
این دو پیش‌تر به همراه بهروز زمانی‌نژاد و کوروش زمانی‌نژاد با حکم صادرشده از سوی قاضی ایمان افشاری، رئیس شعبه ۲۶ دادگاه انقلاب تهران، از بابت اتهام «اقدام عملیاتی برای دولت متخاصم ایالات متحده و گروه‌های متخاصم» به اعدام محکوم شده بودند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/75604" target="_blank">📅 17:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75603">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23e07c2844.mp4?token=GeydV0PTLQ_qKRGXHwVTEXiF4FB5r_BysN0yzjcpeztJAhBuUT_tftyWJNha3-MZKNGtgnDcNiU_pqks-3xphAfj8ndGV33-0REypPMVcMZ5ACneECVYQGlwnR9bwurEI03ss_JJAMz2TXlOO3fB5GpL9Bv-PgDO9S82xGhxAo62k3UI_B0FiQWXD3KM9LgMz8VbpIlWMeRCA0rvURmY0dZRlYo6TzkFvPxY20roh74JadNr70DMMKXpSf159W4NSZFlKW_HK9vSs_k-BYpttRLWNk6uBH31zpu_lsEzAA_LcNgLEthSh0UUGPEIUP8_-fiFCZFcEbJ_OvTUzlkXWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23e07c2844.mp4?token=GeydV0PTLQ_qKRGXHwVTEXiF4FB5r_BysN0yzjcpeztJAhBuUT_tftyWJNha3-MZKNGtgnDcNiU_pqks-3xphAfj8ndGV33-0REypPMVcMZ5ACneECVYQGlwnR9bwurEI03ss_JJAMz2TXlOO3fB5GpL9Bv-PgDO9S82xGhxAo62k3UI_B0FiQWXD3KM9LgMz8VbpIlWMeRCA0rvURmY0dZRlYo6TzkFvPxY20roh74JadNr70DMMKXpSf159W4NSZFlKW_HK9vSs_k-BYpttRLWNk6uBH31zpu_lsEzAA_LcNgLEthSh0UUGPEIUP8_-fiFCZFcEbJ_OvTUzlkXWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویرسازی از مجتبی خامنه‌ای
وزارت جنگ آمریکا روز پنجشنبه ۳۱ اردیبهشت، با انتشار
ویدیویی
بر ضرورت افزایش بودجه دفاعی کشور تاکید کرد.
در این ویدیو که ترکیبی از صحنه‌های واقعی، گفته‌های پیت هگست، وزیر جنگ آمریکا و تصاویر کارتونی است، تصویری از مجتبی خامنه‌ای، رهبر جدید جمهوری اسلامی نیز در کنار یک سامانه موشکی دیده می‌آشود در حالی که یک پایش قطع شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/75603" target="_blank">📅 02:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75602">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hn3_yWGBmO0-9C1bUreyk6j0flz2Ior3RHum8hOp3m5epkAM0Tbtx-cKr7X9eCsBiZRrLQ4eCgRWKNEklransfo6Fdz93J1AzvIEVaO1YTKb-i2NRbgmVpXZyt4O3wuAjcDD5Iq4HTUvN5pVTOVG0XrubthzbrmWiuVmew84V_NgR-Nzn2qKp6jxEfsqcPQFCcjwtrYSWe0_VFoxUPzNFxDKO-FXZrg8nXW93nmV-Lp2BWOqcS25HuuWkUXhoncxsHUxHgDYuiOYCF8ubnX1gDL1yHTMR01DTcwOeAwdPOf0RcQhx5Kcqm5k3bbfj3MNcD3gFFh409pascoIyYWIFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
در تازه‌ترین تحولات بحران ایران و مذاکرات جاری، یک منبع بلندپایه به «العربیه» گفت که فرمانده ارتش پاکستان امشب راهی تهران نخواهد شد؛ این در حالی است که پیش‌تر گزارش‌هایی درباره احتمال سفر او در چارچوب میانجی‌گری‌های منطقه‌ای منتشر شده بود.
قرار بود عاصم منیر، رئیس ستاد ارتش پاکستان، امروز پنج‌شنبه در سفری رسمی وارد تهران شود؛ هم‌زمان با انتظارها برای تحویل پاسخ ایران به تازه‌ترین پیشنهاد آمریکا برای توقف جنگ و دستیابی به توافق میان ایران و ایالات متحده.
alarabiya
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/75602" target="_blank">📅 23:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75601">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9702fd683.mp4?token=UibaONSdqdThkQXcMT_o9wDIPECZcCQQzvpx63U09gPeotVY40GJbP7bCX95lRMN6roISI1pJVdyVuRDN8s8fb_Sljzo61PuufwMgryVeu5hraZTiQcR9IM35r2z25vxHdiZUDroNmXpnhgT2UZ8wEJwGBy1J-8QHuXXMvgt2As1Ehjk53ckWYxoxvF6ec32s-J8iuwe3IxXE629jn-OluiOgdMLaa6B3RJNZ66uW34PSORfhD4j6RRRyjzvc-VsI0o5aAqS8nL9VKOZbuSKgYAasSnspjfDNUFLfrPib6d24bzxrP3yqyR8sEaK5JclcniNq2SvNbvJNHWpLoWt3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9702fd683.mp4?token=UibaONSdqdThkQXcMT_o9wDIPECZcCQQzvpx63U09gPeotVY40GJbP7bCX95lRMN6roISI1pJVdyVuRDN8s8fb_Sljzo61PuufwMgryVeu5hraZTiQcR9IM35r2z25vxHdiZUDroNmXpnhgT2UZ8wEJwGBy1J-8QHuXXMvgt2As1Ehjk53ckWYxoxvF6ec32s-J8iuwe3IxXE629jn-OluiOgdMLaa6B3RJNZ66uW34PSORfhD4j6RRRyjzvc-VsI0o5aAqS8nL9VKOZbuSKgYAasSnspjfDNUFLfrPib6d24bzxrP3yqyR8sEaK5JclcniNq2SvNbvJNHWpLoWt3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در گفتگو با خبرنگاران در کاخ سفید تاکید کرد که هیچ کشتی‌ای بدون تایید ایالات متحده اجازه ورود به ایران یا خروج از آن را ندارد و نیروی دریایی آمریکا در این زمینه عملکرد فوق‌العاده‌ای داشته است.
ترامپ با اشاره به خسارت‌های سنگین مالی جمهوری اسلامی در پی این اقدامات گفت: «بر اساس پیش‌بینی‌ها، آن‌ها روزانه ۵۰۰ میلیون دلار ضرر می‌کنند؛ رقم بسیار زیادی است و چه ۲۰۰، ۳۰۰ یا ۵۰۰ میلیون دلار باشد، آن‌ها در حال از دست دادن پول گزافی هستند.»
رئیس‌جمهوری آمریکا با تاکید بر لزوم آزادی کشتیرانی افزود: «خواسته ما این است که این آبراه بین‌المللی، باز و آزاد باشد. تنگه هرمز یک مسیر دریایی بین‌المللی است، هیچ‌کس نباید در آن عوارض وضع کند و ما اجازه چنین کاری را نخواهیم داد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/75601" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75600">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/011b067e31.mp4?token=tyGPtrvL1vDwWPNDNDH5aBtu1hwoW05YY62adzOuWjpU_DLRQAbZnpYGolF5aqXhzqbehmL1XfLsRdYvqMHFop8tra7_sOS1M-89GqfO6vfMpmvcts6cXpsShMCxl-aPBui03gEOM03hACAMnAsw7rQlV-1B52m5si0gOZm_i-FhdLgAOg1FD99EsQWPpfX0srogUvphtjSWRNZ-8e6yFlwfNMRUUXJVP67gLIQs7eJXxo074C3eCD7LtIYq9IudcxnVHLLl44c8WZCWwOkopv_oBEXxbSyaF9vPL5tPM7PkWYhIb-uw2ZsFka0FMajKWD3jF2H0J5NABJrrjt10og" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/011b067e31.mp4?token=tyGPtrvL1vDwWPNDNDH5aBtu1hwoW05YY62adzOuWjpU_DLRQAbZnpYGolF5aqXhzqbehmL1XfLsRdYvqMHFop8tra7_sOS1M-89GqfO6vfMpmvcts6cXpsShMCxl-aPBui03gEOM03hACAMnAsw7rQlV-1B52m5si0gOZm_i-FhdLgAOg1FD99EsQWPpfX0srogUvphtjSWRNZ-8e6yFlwfNMRUUXJVP67gLIQs7eJXxo074C3eCD7LtIYq9IudcxnVHLLl44c8WZCWwOkopv_oBEXxbSyaF9vPL5tPM7PkWYhIb-uw2ZsFka0FMajKWD3jF2H0J5NABJrrjt10og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمید رسایی هم تلویحا وجود یا عاملیت داشتن مجتبی خامنه‌ای در تصمیم‌گیری‌ها رو زیر سوال برد.
بعد از شعار جماعت در لحظه 01:48 ، یک بچه میگه: مرگ بر دیکتاتور!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75600" target="_blank">📅 22:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75599">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/afe365b1c4.mp4?token=M5vvph7An08AUnvN-ELYyIc3WT4jSqK6iaJC2LtSm7skUNBnPtiG29LmNtHof2sKgBAP25UCXsPaoyAZLSJtP9pzd6hjYwMl9y-VDe_foE_Ab_EafnLx4lFB6YCyCqsbeosHKKtY8z5U3rae5Fxse2OOcHbjVa-9eIfkYZjcsdDL85BQcgEHl0-5Qy39W9ydkYCtlhwnsjBwYNyXkUp_zdg-VTYlBfl5kqmH3hdjk6vu26USWpfqFqQALQvM4o0LiBABAggVJms2G2XLbcB86-QmixlIFc4i9eJ90CjOvMAOar-dwyjMTbxn7pc-PJ0UlZl8DAfvsHdokG0RQFM4Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/afe365b1c4.mp4?token=M5vvph7An08AUnvN-ELYyIc3WT4jSqK6iaJC2LtSm7skUNBnPtiG29LmNtHof2sKgBAP25UCXsPaoyAZLSJtP9pzd6hjYwMl9y-VDe_foE_Ab_EafnLx4lFB6YCyCqsbeosHKKtY8z5U3rae5Fxse2OOcHbjVa-9eIfkYZjcsdDL85BQcgEHl0-5Qy39W9ydkYCtlhwnsjBwYNyXkUp_zdg-VTYlBfl5kqmH3hdjk6vu26USWpfqFqQALQvM4o0LiBABAggVJms2G2XLbcB86-QmixlIFc4i9eJ90CjOvMAOar-dwyjMTbxn7pc-PJ0UlZl8DAfvsHdokG0RQFM4Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهور آمریکا، در کاخ سفید گفت: «جمهوری اسلامی قرار نیست سلاح هسته‌ای داشته باشد. ما نمی‌توانیم اجازه بدهیم.»
او افزود که در صورت دستیابی جمهوری اسلامی به سلاح اتمی، «در خاورمیانه جنگ هسته‌ای به راه خواهد افتاد، و آن جنگ به اینجا خواهد رسید، آن جنگ به اروپا خواهد رفت.»
رییس‌جمهور آمریکا تاکید کرد: «ما نمی‌توانیم اجازه دهیم چنین اتفاقی بیفتد، و چنین اتفاقی هم نخواهد افتاد. قرار نیست اتفاق بیفتد.»
ترامپ درباره محاصره‌ بنادر جنوبی ایران از سوی آمریکا نیز گفت: «کنترل کامل تنگه هرمز را در دست داریم. این محاصره ۱۰۰ درصد موثر بوده است. هیچ‌کس نتوانسته عبور کند. مثل یک دیوار فولادی است.»
او افزود: «هیچ کشتی‌ای نتوانسته بدون تایید ما عبور کند. و نیروی دریایی کار فوق‌العاده‌ای انجام داده است. و هیچ کشتی بدون تایید ما به ایران نمی‌رود یا از ایران خارج نمی‌شود.»
ترامپ درباره اورانیوم غنی‌شده ایران نیز گفت: «ما اورانیوم بسیار غنی‌شده را می‌گیریم. ما به آن نیاز نداریم. احتمالا بعد از اینکه آن را بگیریم نابودش می‌کنیم، اما اجازه نخواهیم داد آن‌ها (مقامات جمهوری اسلامی) آن را داشته باشند.»
دونالد ترامپ، رییس‌جمهور آمریکا پنج‌شنبه در کاخ سفید به خبرنگاران گفت که ایالات متحده خواهان دریافت عوارض در تنگه هرمز نیست.
پیشتر مارکو روبیو، وزیر خارجه آمریکا اعلام کرد که اجرای سیستم اخذ عوارض در تنگه هرمز از سوی جمهوری اسلامی، دستیابی به توافق دیپلماتیک را غیرممکن خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/75599" target="_blank">📅 20:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75597">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1e56ee3c30.mp4?token=JaM-G75PTxl0PERSd93lRYDHKQeFBK3KIMqyi6F_LZCJ5fdtlrFiLklc9_Re6xf8XZvn8iMFoWEjs-6o3LO4IjdTgvh9XLXIiwHfiY3U_A_NBAXLYtwsQwRSwTOC_XO0cbHA5MuGvbAtmHir-Wcc3ywQEbow6mf8J6sgexyzHO4OY5HqM0ZJrRGfVrFW-Wgsqz5tzOw6Pkxxn3LRoPkFbViNDJLsYqASUtV9e39zeeXUtGu45TSG02E5Lbq8FNpBd8Cu3dUsKRNyKo63EeF11-OF9MD3YDt7iV2AlZh6N4RcOQPTst2q2y3LJ4KEkVXD0auIq154Ke-KMMcoDaLsiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1e56ee3c30.mp4?token=JaM-G75PTxl0PERSd93lRYDHKQeFBK3KIMqyi6F_LZCJ5fdtlrFiLklc9_Re6xf8XZvn8iMFoWEjs-6o3LO4IjdTgvh9XLXIiwHfiY3U_A_NBAXLYtwsQwRSwTOC_XO0cbHA5MuGvbAtmHir-Wcc3ywQEbow6mf8J6sgexyzHO4OY5HqM0ZJrRGfVrFW-Wgsqz5tzOw6Pkxxn3LRoPkFbViNDJLsYqASUtV9e39zeeXUtGu45TSG02E5Lbq8FNpBd8Cu3dUsKRNyKo63EeF11-OF9MD3YDt7iV2AlZh6N4RcOQPTst2q2y3LJ4KEkVXD0auIq154Ke-KMMcoDaLsiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، روز پنج‌شنبه اعلام کرد اگر تهران طرح دریافت عوارض برای عبور از تنگه هرمز را اجرا کند، رسیدن به یک توافق دیپلماتیک میان ایالات متحده و ایران غیرممکن خواهد شد.
او در گفت‌وگو با خبرنگاران گفت: «هیچ‌کس در جهان از سیستم عوارض‌گیری حمایت نمی‌کند. چنین چیزی نمی‌تواند اتفاق بیفتد. غیرقابل قبول خواهد بود. اگر آنها همچنان دنبال اجرای آن باشند، رسیدن به یک توافق دیپلماتیک غیرممکن می‌شود. بنابراین اگر بخواهند چنین کاری انجام دهند، این تهدیدی برای جهان است و کاملاً غیرقانونی است.»
او همچنین خبر داد که در مذاکرات با تهران برای پایان دادن به جنگ آمریکا و اسرائیل علیه ایران، «پیشرفت‌هایی» حاصل شده است و به گفته او «نشانه‌های خوبی وجود دارد»، اما واشینگتن با «سیستمی روبه‌روست که خودش تا حدی دچار شکاف و چنددستگی است.»
وزیر خارجه ایالات متحده با اشاره به این که مقام‌های ارشد پاکستان به عنوان میانجی مذاکرات امروز به تهران سفر خواهند کند، گفت: «ترجیح رئیس‌جمهور آمریکا این است که یک توافق خوب حاصل شود... من اینجا نیستم که بگویم حتماً چنین اتفاقی خواهد افتاد، اما اینجا هستم که بگویم ما هر کاری بتوانیم انجام می‌دهیم تا ببینیم آیا می‌توانیم به توافق برسیم یا نه.»
او در عین حال افزود که اگر یک توافق خوب حاصل نشود، دونالد ترامپ «به‌روشنی گفته است گزینه‌های دیگری هم دارد.»
پیش از این گزارش‌هایی درباره سفر روز پنجشنبه فیلد مارشال عاصم منیر، رئیس ستاد ارتش پاکستان، به تهران منتشر شده است. خبرگزاری‌های رسمی ایران این خبر را یک روز پس از آن منتشر کردند که وزیر کشور پاکستان، برای دومین‌ بار طی هفته جاری وارد تهران شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/75597" target="_blank">📅 19:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75596">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HPKArq05r8pZi3YJ9BBSSGHCAUrR_WVZZPw9XzbluCUKrijqdYFe-hs7Rd4BROfHITohW18QH6HuYgcEFvfxbajJ9QshPw1m8XcJUCJQmJuayGdr30CZHWD8T8TYbygpwWF-d0dVfrVb9iYhCmExpF0T0IdaNfOY1GYiZ5l0Q_c06ADGyRzctVGVUN8cS-SonBAXGB9hlXjneCGDj0LzpbLZcaceHKF5rPctyhqpfxpKOVgo2pnimQtduRwsBW1aPqVAWKt7acgiV-v8K-BzGp7A49mJCQuhuJ2wzF0LeHrj-9ig4gcy330FB2y0Vh7wARNPFFisX4QNSv3R76ROEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار فاکس نیوز به نقل از یک منبع آگاه از روند مذاکرات خبر داد که کاخ سفید گزارش خبرگزاری رویترز مبنی بر این‌که مجتبی خامنه‌ای دستور داده اورانیوم با غنای بالا در ایران باقی بماند را رد کرده و آن را نادرست دانسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/75596" target="_blank">📅 18:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75595">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rjxV5SB_h6OXyZK8uM3wjI6o08vzSbXL9L0y7B0BdxyBqUj7QJDWqBCJh_TUU4Pja4hPN8wud9LPNdhK6HKlwiZfDZTsy_4ZvbIwy4zFgTMoMjh2ATfdHIHQI-QJbFz8CczE4wa-6MKHyIIgCCDq9cRRL_qt-Td-cLetX9dl7BILe1ewFsur01MCGVQKSLQSuz0ZVFx7tJDoSbvp5ejlXqIEfFqnkC-H0EBmf7wJYNNX5afAWmkz-vdJiBP5sap8VGEeMFmIyOo8Lw00yuz-yYoQBR2cr0OEV4XPoaorvUPkDS-l46ef-hImM6OQWRkwTq9CEqar1vXAcRm3BGVDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه تحقیقی FTM هلند در
گزارشی
نوشته که توماس اردبرینک، خبرنگار هلندی نیویورک‌تایمز و شبکه NOS در ایران، همزمان مشاور شرکت آبجوسازی هینکن هم در ایران بوده و برای این کار ماهانه تا یک‌سال ۵ هزار یورو دریافت می‌کرد. اردبرینک دریافت مبلغ را انکار کرده.
طبق این گزارش این روزنامه‌نگار به طور منظم کارهای جانبی (پروژه‌ای) برای این شرکت آبجوسازی در ایران انجام می‌داده است و نه تنها کارمندان اعزامی و بازدیدکنندگان را در تهران می‌گردانده، بلکه گفته این شرکت آبجوسازی را با وکلا و مشاوران محلی نیز مرتبط کرده است.
FSeifikaran
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/75595" target="_blank">📅 18:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75594">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjE4uQYRnMF70QNZaA8QvKRUlziPwNHrz1vhKBhResLOi5Do3uITW7Q3Tbx9IsHdqUmHB3NZm4cqrxkXwiDyEaPmHCBp8N0GGUCCW1pgGFXqCIrFSkOJ9oBiRmU83jrxIxg5Rvddk_s8PGgVcPLxEfIcTrY9ZqegQ4NZRHobx_A_N8epHyGwEY_cND-Q-lV7qRmyFDs90mKFEggz3yGQlsDm6NHcQVtlcH7B1qbTmIm5VuTLHkb4MhmxL8PqhW-TgiGGSz5slGQzADbViYpHXd3xpEBWWBMOhbRaPqW1pDkbGeRpRAlLdP5SZayOTyN1530Rx7UoJKAyUb6WlwzF-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انور قرقاش، مشاور ارشد رئیس دولت امارات متحده عربی، می‌گوید که برخی رفتارهای ایران در سال‌های گذشته باعث کاهش اعتماد میان کشورهای منطقه خلیج فارس شده است.
او در پیامی در شبکه اجتماعی ایکس نوشت که کشورهای منطقه طی سال‌های طولانی با «رفتارهای زورگویانه و تهدیدآمیز» ایران روبه‌رو بوده‌اند؛ رفتارهایی که به بخشی از واقعیت سیاسی خلیج فارس تبدیل شده است.
آقای قرقاش همچنین تاکید کرد که شکاف میان مواضع تند و ادعاهای دوستی از سوی ایران، باعث از بین رفتن اعتماد و اعتبار شده است «و امروز، پس از تجاوز وحشیانه ایران، حکومت ایران تلاش می‌کند واقعیت تازه‌ای را که از یک شکست آشکار نظامی به‌وجود آمده تثبیت کند؛ اما تلاش برای کنترل تنگه هرمز یا تعرض به حاکمیت دریایی امارات متحده عربی چیزی جز خیال‌پردازی و آرزوهای دست‌نیافتنی نیست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/75594" target="_blank">📅 17:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75593">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f4f44e0c.mp4?token=gB0SUuYBWV-m8dWmtG-LP3DieO-Q6egMXYgD607qWiRMkbh1XQwWoS1IX381s_qgy6PqO-OHgLBrvlVUqXd5qvGRxRiYOOf-S4aLcGN418Rh05SFM25ThjZEpHxejAIjmdCsOM2jST3VA6FRLbm-nlFuFYyPn1odAskHLH9hhKWBh7cKhp3_lrrqBSO19x_Ts3sWF2-vuiDJ51fjXOlqxeV6N8ya369NVGKp2SzsQzyqp7AJg2qXHKI9xzWYZL5XY6sM2PmpVOb_yStCM1_GW-Z4WZu-fv2KM0ApM_yO2MTQG_0ZOcjVG5RweGixmDLA_J9QwzK9EIHlchoN4ST7gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f4f44e0c.mp4?token=gB0SUuYBWV-m8dWmtG-LP3DieO-Q6egMXYgD607qWiRMkbh1XQwWoS1IX381s_qgy6PqO-OHgLBrvlVUqXd5qvGRxRiYOOf-S4aLcGN418Rh05SFM25ThjZEpHxejAIjmdCsOM2jST3VA6FRLbm-nlFuFYyPn1odAskHLH9hhKWBh7cKhp3_lrrqBSO19x_Ts3sWF2-vuiDJ51fjXOlqxeV6N8ya369NVGKp2SzsQzyqp7AJg2qXHKI9xzWYZL5XY6sM2PmpVOb_yStCM1_GW-Z4WZu-fv2KM0ApM_yO2MTQG_0ZOcjVG5RweGixmDLA_J9QwzK9EIHlchoN4ST7gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بریتانیا از توافق تجاری ۵ میلیارد دلاری با کشورهای خلیج فارس رونمایی کرد؛ توافقی که در بحبوحه تنش‌های منطقه‌ای پس از جنگ ایران، به گفته لندن «پیامی از ثبات و اعتماد» به بازارها می‌دهد.
این توافق با شورای همکاری خلیج فارس شامل عربستان، امارات، قطر، کویت، عمان و بحرین است و قرار است سالانه حدود ۳.۷ میلیارد پوند به اقتصاد بریتانیا اضافه کند.
لندن می‌گوید ۹۳ درصد تعرفه‌های کشورهای خلیج فارس برای کالاهای بریتانیایی حذف می‌شود؛ از جمله محصولات غذایی، خودرو، صنایع هوافضا و الکترونیک.
در مقابل، بریتانیا نیز برخی تعرفه‌ها را کاهش می‌دهد، هرچند نفت و گاز کشورهای عربی پیش‌تر هم بدون تعرفه وارد بریتانیا می‌شد.
فعالان حقوق بشر از نبود بندهای الزام‌آور درباره حقوق بشر در این توافق انتقاد کرده‌اند و آن را «عقب‌گرد اخلاقی» توصیف کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/75593" target="_blank">📅 17:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75592">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gz8qrndUGzsV5vb15yeOPrx4pqnbyPxfY5JXRKNPcLtf7qlaVk5JmD2fUCy77gofpMTDXyP_7EfwUh3n-g2SxFmYmjlARxhCbcAnp94fFKlIyTH9pOTl-5cymZsSwuIscdT7t6vGhH063pAkm9JxO7ldul54HMWDXjwyTp3_PYwKVVyJFIdqyTYtJ2_ohz65K9DT9ECUyNL9Myxypkc8Gb-RIByZOrp9ZbHAYb14e8obcBDA9LzFSewxNkrPLSPOfP5WsbrZUlQIhTXb7Q4a_6PZlP9kH3nVcMzVYZxGBNTsKkhHje6AaiFbjZiIN7lIagJMEOFSOlXe4CkinFmFqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی یزدی‌خواه، نایب‌رییس کمیسیون فرهنگی مجلس، گفت در شرایط فعلی تصمیمی برای بازگشایی اینترنت جهانی وجود ندارد و محدودیت‌ها با «ملاحظات امنیتی» ادامه خواهد داشت.
یزدی‌خواه قطع اینترنت جهانی را به مصوبات شورای عالی امنیت ملی نسبت داد و گفت این تصمیم به‌دلیل «مسائل امنیتی، امنیت کشور و حفظ جان افراد» گرفته شده است.
با وجود اینکه نت‌بلاکس اعلام کرده خاموشی اینترنت در ایران وارد هشتادوسومین روز خود شده، یزدی‌خواه گفت بیش از ۹۰ درصد نیازهای مردم در وضعیت فعلی برآورده می‌شود و مراجعات گسترده‌ای در اعتراض به قطع اینترنت وجود ندارد.
او همچنین گفت در قالب طرح موسوم به «اینترنت پرو»، تاکنون بیش از یک میلیون نفر دسترسی دریافت کرده‌اند؛ طرحی که منتقدان آن را مصداق اینترنت طبقاتی و تبعیض‌آمیز می‌دانند، زیرا دسترسی به اینترنت جهانی را به گروه‌های خاص محدود می‌کند و شهروندان عادی را از حق برابر دسترسی آزاد به اینترنت محروم نگه می‌دارد.
نایب‌رییس کمیسیون فرهنگی مجلس همچنین گفت شرکت‌های صادرات و واردات، مراکز علمی و پژوهشی، آزمایشگاه‌ها و برخی اصناف در صورت نیاز می‌توانند برای دسترسی به اینترنت بین‌الملل اقدام کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/75592" target="_blank">📅 17:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75591">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cj7vAzmlQmwlBYITpXgzXQMSINWlmywvMgEpEODKK5hjEvEncXR0Ktbn7Vjb5KBUMthY2gnmcEaOuRbvKKMoHXI_re6rewa3JI6e-q04kfnQpmbSK3s2xp9Ub80QsEy1Zu7oEzKOPXv7qfH2PXz-6ER47lbCRyIHars-alYMfJkpVDCNGpwZ_UC34L3PmlrwH2gqhfpKM90CexAwN32TO4C1niZCMQhkkKvpNR_Uxzju-qkbUTaXpgLIMPV7h-yIB93AtBxo-Y6hiQq7W6XwT9SIhzpNfPd1hLcjXW-pR7gyZFoDKo7sUyhPl5GK0ozH6AJOJEa6d6bHfMKyvsPZsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع ارشد در حکومت ایران گزارش داد مجتبی خامنه‌ای، رهبر جمهوری اسلامی، دستور داده ذخایر اورانیوم با غنای بالا نباید از ایران خارج شود.
به گفته این منابع، این دستور موضع تهران را در برابر یکی از اصلی‌ترین خواسته‌های آمریکا در مذاکرات برای پایان دادن به جنگ آمریکا و اسرائیل علیه جمهوری اسلامی سخت‌تر کرده است.
مقام‌های اسرائیلی نیز به رویترز گفته‌اند دونالد ترامپ به اسرائیل اطمینان داده هر توافق احتمالی باید شامل خروج ذخایر اورانیوم غنی‌شده از ایران باشد.
یکی از منابع ایرانی به رویترز گفت دستور رهبر جمهوری اسلامی و اجماع در ساختار حاکمیت این است که ذخایر اورانیوم غنی‌شده نباید از کشور خارج شود.
به گفته منابع رویترز، مقام‌های جمهوری اسلامی معتقدند انتقال این مواد به خارج، جمهوری اسلامی را در برابر حملات احتمالی آینده آمریکا و اسرائیل آسیب‌پذیرتر می‌کند.
@
VahidOOnLine
دقایقی پس از این خبر رویترز بهای نفت در بازارهای جهانی نزدیک به دو دلار افزایش یافت.
قیمت هر بشکه نفت خام برنت دریای شمال بعدازظهر پنجشنبه ۳۱ اردیبهشت‌ماه در بازارهای اروپایی از ۱۰۵ دلار به بیش از ۱۰۷ دلار افزایش یافت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/75591" target="_blank">📅 17:53 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75590">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEG3QYktNh4Qmwo9ywfrwcIG--oNnhZ9sMga8tLy1tk1Ok279bm5Ag5GQ5-_NyBB4BvQy5XxnOGq54W_ekoKwVXzplS8o0bmVZsp25mncb5pmLKsOG5iGhNLxOWJOUxFfbEbLDHFpyq2F7o6YcsisOR-JOPcjeZCuHv6LOF52PLVlIuD8Cu8DLYvkKWrG-FCR_CQ-G6FT2c4ej2b24kK769aeHPzgUjV60HDT4CCPoL6_1tSD4qTrPGq5lpm8Ts9hBeV3AzVHo9qvjaVPin_cXLiHJDRz902KpqdkW-utlaWBILPsT8pjv9IBGQSSogQ2CrDz-npman3N5tllbBYJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی کابی‌زاده، شهروند ۴۷ ساله و پدر یک دختر بود که در اعتراضات دی‌ماه در استان خوزستان بازداشت و پس از انتقال به مرکز درمانی به دلیل منع رسیدگی جان باخت. او دختری به نام حلما دارد.
بر اساس اطلاعات رسیده به ایران اینترنشنال از افراد مطلع از خانواده او، مهدی کابی‌زاده در اعتراضات اهواز به دست ماموران بازداشت شد و سپس به دلیل بیماری خونی و روده به بیمارستان منتقل و بستری شد. با این حال، مسئولان بیمارستان به دلیل سابقه حضور او در اعتراضات و بازداشتش از رسیدگی و درمان کافی خودداری کردند که موجب جان باختن او شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/75590" target="_blank">📅 17:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75589">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QrPtwc-S_6Yx5jhU0C2T6zHX9XQiNcOhRN4ea-qZkvD3Tfc50ide_-GhPR8mf_-eH9HY12ljf8GitPOlLtRsWYJ62eyz8hEciAyUMUQ0skuipRHqjorjUKv3TXEb-PZkFBqbyLHjvPtSH8HT6yDweDR7YbomiV_8snFQI2czYsY8ekFtK287_uJWeOWD0W2FCTmoRpTtJ9lYJHbKlPj5m-s97l7sHVnLO_0OSXXkgh5rNidmaeFzVoZ-iKAvYNYrrj9WD0TcufR-PW2eCtBL6cpTIVLb46f3IxXSyUrHN5WEqZoYALGjRtjMcD8DoIn0EC6hnhoQSXMlJGdWIQdcIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی دو زندانی را به اتهام عضویت در «گروه‌های تروریستی تجزیه‌طلب» و «قیام مسلحانه از طریق تشکیل گروه‌های مجرمانه» اعدام کرد.
ارگان رسمی دستگاه قضایی ایران، میزان، هویت این دو نفر را رامین زله و کریم معروف‌پور معرفی کرده و نوشته که آنها صبح روز پنج‌شنبه، ۳۱ اردیبهشت، اعدام شدند.
میزان نوشته که رامین زله «پس از طی دوره‌های آموزشی از طرف گروهک ماموریت پیدا کرده بود تا در ناآرامی‌های کشور به عنوان لیدر شرکت کند».
ارگان رسمی قوه قضائیه ایران همچنین نوشته که این دو نفر «اعتراف» کرده بودند که «برای ترور فرمانده پایگاه سپاه یکی از شهرستان‌های غرب کشور» با یکدیگر «همکاری» داشته و برای این کار، «سلاح» نگهداری می‌کردند.
از زمان حملات آمریکا و اسرائیل به ایران، جمهوری اسلامی اجرای احکام اعدام را افزایش داده است و در برخی روزها چند نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75589" target="_blank">📅 09:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75588">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/622e876399.mp4?token=h4t2BCfKiRcZg9VN3sW7MMtMwU6fUjgKkP91k5frA8uLJRy_bATuV5jJAljLgKxEX54LAF8T-61SN703_Ei4GCwjXFEurSGXcfJN2X4Zk5hRMtIMoNA0RYYaeteQf_1BLGp9fclr3Wf3EqQoZ35IFmw46kov2tRv3lvtzd3PId4VNu-eBsXtnu29uaejWCiVb4ms7GA2aG34goIXWqNJ6TXX0yeOcCR-kyGYpOfSIuj7aI8tTEDxF8Rzc_Z7A-aUetM2DiMMcMbrOc9mYUzV3Je5vPIn6QgD1LC0iJk9FOJrUcbcW9aL1lQ-wS77yFeGgHE0QLcptowms-rw0QH0Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/622e876399.mp4?token=h4t2BCfKiRcZg9VN3sW7MMtMwU6fUjgKkP91k5frA8uLJRy_bATuV5jJAljLgKxEX54LAF8T-61SN703_Ei4GCwjXFEurSGXcfJN2X4Zk5hRMtIMoNA0RYYaeteQf_1BLGp9fclr3Wf3EqQoZ35IFmw46kov2tRv3lvtzd3PId4VNu-eBsXtnu29uaejWCiVb4ms7GA2aG34goIXWqNJ6TXX0yeOcCR-kyGYpOfSIuj7aI8tTEDxF8Rzc_Z7A-aUetM2DiMMcMbrOc9mYUzV3Je5vPIn6QgD1LC0iJk9FOJrUcbcW9aL1lQ-wS77yFeGgHE0QLcptowms-rw0QH0Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'کمور، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/75588" target="_blank">📅 03:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75587">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SJM82GEJqAu8EKyhAMjqrwtA9QZdj2CDaAsvIXcefD4Q3KfpGI3OJE2uSO6y7jkyiYj89tk981ahYYl6Xl5Fdz6fOJE3dR1BKwISUtI1_iaLCzbjwtuqH1sTFrVGZJx3uM1QJiEUVQvY8NjKx10T9jRKx6ThVrKVqTfL5hWt5rLwVoEQmdOSzx4po7pmU-_BGRjqkM9SYqXFwiZ5lbBdk9kd_ZRu1CH5rTmtkTxm4YhR2hINYsqdeWFVAb6cDn1xhGAE1rt45Ly8ibQQzSOugUftaO5gwgRWRatzz5cqJ98AHcyNipxQxoY-tB_5JYZwvnbBeuEk3-Bd-4kOGMQKuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب رسمی کاخ سفید در شبکه اجتماعی ایکس، روز چهارشنبه ۳۰ اردیبهشت در پُستی، عکسی از رئيس جمهوری آمریکا، دونالد ترامپ را منتشر کرد که زیر آن تصاویری از «دشمنان خنثی‌شده آمریکا بدست پرزیدنت دونالد جی. ترامپ» دیده می‌شود.
در این پست تصاویری از علی خامنه‌‌ای رهبر کشته‌شده جمهوری اسلامی، نیکلاس مادورو رهبر دستگیر‌شده ونزوئلا، رائول کاسترو رهبر سابق کوبا، و ابو بلال المنوکی از رهبران داعش که به جای تصویرش پرچم داعش نشان داده شده، منتشر شده است.
کاخ سفید در مورد کاسترو، روی تصویر او نوشت که علیه او کیفرخواست صادر شده است. در مورد مادورو روی تصویر او نوشت که دستگیر شده است. و در مورد علی خامنه‌ای و ابو بلال المنوکی روی تصاویر آن‌ها نوشت که «کشته‌ شدند.»
حساب رسمی کاخ سفید افزود: «عدالت اجرا خواهد شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75587" target="_blank">📅 03:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75586">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DIeC76zDKEBQqXkWqmNrQ0yxCXUh2hFZNrSFI_5SUVM15x_xlpeIejKgRpyhvU8lTNCb4DRk-1bCYq_Bp1Lrj295lisI6Tzy_P0WHVcZPvKXgTw5UOxt-0RMdhOoRwggP6pkkctWSvL7R47zjo9EcbUsNb0jZ_OdOlnGt7b0m3Dm-hfeEgPds0p_N0dR_q8qkAAUkPLZCeKIH6uACx_3WImmyaBwjCLX18qwVrVTILrRLXNr2FPGEsdb7BOnFbLHZw3EAYBZRh2MxkSeiGxWT44gi0-JStQQEWM4j7O_o4CoxuFgzGaCsFwK90kidGg_9bFyNLPrAOWUNB6xE-8W1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه اسرائیل هیوم به نقل از «منابع آگاه» نوشت جلسه چهارشنبه ۳۰ اردیبهشت در کاخ سفید درباره ایران با اختلاف‌نظر شدید میان مقام‌های ارشد دولت آمریکا همراه شد، اما رییس‌جمهوری آمریکا در نهایت، خلاف نظر وزیر جنگ و وزیر امور خارجه، و همسو با دیدگاه جی‌دی ونس و فرستادگان ویژه‌اش، ادامه مذاکرات با جمهوری اسلامی را تایید کرد.
این روزنامه راستگرا نوشت ارزیابی مارکو روبیو، وزیر امور خارجه، و پیت هگست، وزیر جنگ آمریکا، این بود که در این مرحله، بدون اعمال فشار قابل‌توجه، از جمله تهدید به حمله و تشدید تحریم‌های اقتصادی، نمی‌توان از جمهوری اسلامی امتیاز گرفت. در مقابل، ونس معتقد بود تازه‌ترین پیشنهاد تهران نشانه‌ای از انعطاف است و می‌تواند زمینه حرکت به سوی یک توافق اولیه را فراهم کند.
منابع آگاه از این جلسه به اسرائیل هیوم گفتند که استیو ویتکاف و جرد کوشنر، فرستادگان ویژه دونالد ترامپ نیز در این گفت‌وگو از موضع ونس حمایت کردند.
آنها پیش از این جلسه با رهبران عمان، قطر و عربستان سعودی گفت‌وگو کرده بودند.
به نوشته این رسانه تنش در این جلسه زمانی شدت گرفت که ترامپ از ونس و فرستادگان انتقاد و آنها متهم کرد که رویکردشان به جمهوری اسلامی امکان می‌دهد زمان بخرد و به تصویر ایالات متحده و نهاد ریاست‌جمهوری آسیب بزند. ونس با لحنی قاطع پاسخ داد که دولت باید به دنبال پایان دادن به این کارزار نظامی، بازگرداندن سربازان به خانه، کاهش قیمت نفت و تمرکز بر مشکلات داخلی آمریکا باشد؛ پاسخی که حاضران را غافلگیر کرد.
اسرائیل هیوم در ادامه این گزارش به گفت‌وگوی ترامپ با رهبران منطقه اشاره کرد و به نقل از دو منبع نوشت که رهبران اسرائیل و امارات متحده عربی، همزمان با تاکید بر ضرورت حفاظت از تاسیسات حساس خود در قبال حملات احتمالی جمهوری اسلامی، از پیش گرفتن «سیاست‌های سخت‌گیرانه» علیه جمهوری اسلامی حمایت می‌کنند.
در مقابل، رهبران عربستان سعودی و قطر ترجیح می‌دهند از بازگشت به درگیری‌ها پرهیز شود.
این روزنامه همچنین به نقل از یک مقام آمریکایی درباره تماس تلفنی ترامپ با نخست‌وزیر اسرائیل نوشت که نتانیاهو از رفتار جمهوری اسلامی و احتمال وقت‌کشی تهران ابراز سرخوردگی کرد، در حالی که ترامپ بر پیچیدگی شرایط و دشواری‌هایی پیشِ رو تاکید داشت. با این حال رییس‌جمهوری آمریکا بار دیگر گفت که به رفع تهدید هسته‌ای حکومت ایران متعهد است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/75586" target="_blank">📅 02:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75584">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OFhhh9iIpn1Y9Zzk_4vaZx00e8mK3Vl_GoVUZPJiqWPZ5NdMt8o0yoqZRN5J7CKCOaHrRPVw2XBCL9nvpiZMM6tsgHc3fkoOz0k9DN6w5tan5hgMkA0ZYoYgay1s7M5y6WyX-euKxXKoNdFdSQH-fLWXzGXcIX0f6aLzIwUbfy-lpaGqWM1UuBt4pkUOllm1GuadCTC-tw3pTua0V-CdaA_WVW3EtaQrMZiI_-3ESJ1lfxZi6tNJTG3H-DfroU2ZC5zNWtwUgQRNQsHvtlj7FseIEffZtUhJC45_b3wxtcECZQd0agv6WUn4AwwMRueZItrKy3Ij3eveo_LXHs4hOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4e82522f4.mp4?token=IdQ_bxAFxjMToSw_0qCSL9QlSXkQvTqdOPt7335sIR5WE00A4QfmkOHIrIHxBt_swPkYjLhrkmWeTS9RJMBSm1k7IoOiCaXDyx12pyWMgc8WaBNenatGSLi23R3VcwLH1eTdPvZJ6u_SMxRPOqcyRZd98njtJq6_g6PHZIbwLssmDzNatcwD9WcIBGAx_IRraxhgRksxKmHevr1CKRShQt6ZwFp9EjKjdI9QhZdnqlsNRBlwZakvkW3zq-aHTO22eDZwnHUZc2pQyEgwAN8lLPPp5zqAkVQ1PRGU9LQqC3zRcSl4jwKaXogHi0vPwev2BkqzCK-pTct8WG-qaqkiXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4e82522f4.mp4?token=IdQ_bxAFxjMToSw_0qCSL9QlSXkQvTqdOPt7335sIR5WE00A4QfmkOHIrIHxBt_swPkYjLhrkmWeTS9RJMBSm1k7IoOiCaXDyx12pyWMgc8WaBNenatGSLi23R3VcwLH1eTdPvZJ6u_SMxRPOqcyRZd98njtJq6_g6PHZIbwLssmDzNatcwD9WcIBGAx_IRraxhgRksxKmHevr1CKRShQt6ZwFp9EjKjdI9QhZdnqlsNRBlwZakvkW3zq-aHTO22eDZwnHUZc2pQyEgwAN8lLPPp5zqAkVQ1PRGU9LQqC3zRcSl4jwKaXogHi0vPwev2BkqzCK-pTct8WG-qaqkiXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، شامگاه چهارشنبه گفت حاضر است «چند روز» برای رسیدن پاسخ ایران به پیشنهاد واشینگتن درباره توافق پایان جنگ صبر کند اما هشدار داد که این پاسخ باید «۱۰۰ درصد درست» باشد.
او بعد از سخنرانی در جمع دانشجویان نظامی به خبرنگاران گفت اگر پاسخ ایران درست نباشد، تشدید تنش به سرعت رخ می‌دهد و افزود: «ما آماده پیش‌روی هستیم. باید جواب‌های ۱۰۰ درصد درست و خوبی بگیریم.»
ترامپ اعلام کرد که آمریکا در حال حاضر با افراد «خیلی خوبی» از طرف ایرانی مواجه است که «استعداد و قدرت ذهن» دارند؛ افرادی که به گفته او جایگزین رهبران پیشین ایران شده‌اند.
این اظهارات ساعتی بعد از آن است که سخنگوی وزارت خارجه ایران اعلام کرد تهران در حال بررسی طرح پیشنهادی جدید آمریکا است.
این طرح توسط اسلام‌آباد به دست مقام‌های جمهوری اسلامی رسیده است؛ همزمان با سفر وزیر کشور پاکستان به تهران.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/75584" target="_blank">📅 23:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75582">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B5E33lMZHHZCRrwuWVp3Uu-gy8jZckTqQZDqWn80FPuJC5TZHk2qGog6e-kjLBJGVtBdO9uypa-clLly9u9nx-I_5-zqi6L7neFZWusJaw8f-n_mOosrbmjqsPzOLsAgqVPzKee-zGw4Rz9phXs-J3lbfh-ttEhPMuuu74kpeOVtgpVnbKJ1t4HS0r5bT3WLPUfpdmNZrOCz9s0EvSaY9GyokSfearPUSDJrJcpQso0yqIFqe96ihPCdy8d5CmQPXHN2-NL6eClmNHNXIHMIIzIA2u9fwegB-_olJaPPKyUF5ZICqTJ4wYYcPuOx0WAjhHEAl0FJnx4ru_-l4vYwZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NGn0UDHwEnOpYaHkStYa_TbnbeNJt_Ym8qnJk46mxNczSuAkrY1MWSAE5ouH3bVmpxFd3QDFEgQC7HhMGrF3raWVd28sIXK6f5ET0-bVv5OH0ttYzcQ_DVJ1ze1j3UYwneDaWbAaRiRM0kCCPzidGjQ6QUGoGecFMIxEZ4-A3nJz23MoQ9Vgdjqjmh4b-wjTdliIUER-9FkVOUz89EQi6cVi7WLHrnu1oaGP7v9dU5Icca2MgDGhNBvsw-H0cOw_MDNZYXPLMFiokI3rHuphOA5dsBVHs3ZD9f1m_zqHSIM7pmOf4zgyixzsFBzgHBAVBWfiJdolTyUL69LQki2lEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آکسیوس در گزارشی اختصاصی اعلام کرد دونالد ترامپ در تماس تلفنی طولانی و «دشوار» خود با بنیامین نتانیاهو، از تلاش میانجی‌ها برای تدوین یک «تفاهم‌نامه» خبر داده است. بر اساس این طرح، آمریکا و جمهوری اسلامی با امضای این تفاهم‌نامه رسما به جنگ پایان داده و یک دوره ۳۰ روزه را برای مذاکره درباره برنامه هسته‌ای ایران و بازگشایی تنگه هرمز آغاز می‌کنند.
به گفته دو نفر از منابع آکسیوس، این پیشنهاد با مخالفت شدید نخست‌وزیر اسرائیل مواجه شده و دو رهبر درباره مسیر پیش‌رو اختلاف‌نظر جدی دارند. یک مقام آمریکایی وضعیت نتانیاهو را پس از این تماس، «بسیار خشمگین و آشفته» توصیف کرد.
آکسیوس به نقل از منابع خود نوشت سفیر اسرائیل در واشنگتن نیز نگرانی شدید نتانیاهو از این گفتگو را به اطلاع قانون‌گذاران آمریکایی رسانده است؛ هرچند سخنگوی سفارت این موضوع را تکذیب کرد. یکی از منابع با اشاره به بدبینی همیشگی نتانیاهو به روند گفتگوها گفت: «بی‌بی همیشه نگران است.» کاخ سفید و دفتر نخست‌وزیری اسرائیل از اظهارنظر در این باره خودداری کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/75582" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75581">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7a02e28e7c.mp4?token=kChQdIOOZfV_7th8CJu1i8bGncQVOUuPgBPE8mKwTLAoLZtUYLhEshqVqina0K_wd8_B_ZHP0rhcq2G0Ylr0FD5iQyJ2PKnmK4NYQOySOfP4W9z6ULKsZdoHLG0jQFQ1RznXwRm37hyVNoqWbh26-wssH2TMl9dBRmbSOuQFohDHZqvAOVTpS3vlaIV-LVKX-4q0MPS4yhjnJOeQOUroijKdW0JwYdeDE4ismPvQSRy6cXlAy9kdgDfpYpGnPvXBAlDjUQ2IThshC0e5ZzLMfagUbAyRYm_5qhK_UkR7fqDa_6GfDyUz5F1UJXXqzpiVKu5d0YPwFi5bODMaY6wCZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7a02e28e7c.mp4?token=kChQdIOOZfV_7th8CJu1i8bGncQVOUuPgBPE8mKwTLAoLZtUYLhEshqVqina0K_wd8_B_ZHP0rhcq2G0Ylr0FD5iQyJ2PKnmK4NYQOySOfP4W9z6ULKsZdoHLG0jQFQ1RznXwRm37hyVNoqWbh26-wssH2TMl9dBRmbSOuQFohDHZqvAOVTpS3vlaIV-LVKX-4q0MPS4yhjnJOeQOUroijKdW0JwYdeDE4ismPvQSRy6cXlAy9kdgDfpYpGnPvXBAlDjUQ2IThshC0e5ZzLMfagUbAyRYm_5qhK_UkR7fqDa_6GfDyUz5F1UJXXqzpiVKu5d0YPwFi5bODMaY6wCZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز چهارشنبه ۳۰ اردیبهشت با تاکید بر این‌که نیروی دریایی و هوایی ایران از بین رفته‌اند، گفت اکنون تنها سوال این است که آیا آمریکا برای تمام کردن کار بازمی‌گردد یا جمهوری اسلامی پای امضای یک سند (توافق‌نامه) خواهد آمد.
ترامپ که در مراسم فارغ‌التحصیلی آکادمی گارد ساحلی آمریکا سخنرانی می‌کرد، گفت: «همه چیزِ آن‌ها از دست رفته است؛ نیروی دریایی‌شان نابود شده، نیروی هوایی‌شان از بین رفته و تقریبا همه‌چیزشان را از دست داده‌اند. اکنون تنها سوال این است که آیا ما پیش می‌رویم تا کار را تمام کنیم، یا اینکه آن‌ها یک سند را امضا خواهند کرد؟ باید ببینیم چه پیش می‌آید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/75581" target="_blank">📅 20:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75580">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kmz9crgxllzQZxcwLBj_V2orZ6JTOGL_arfkC5DQ2Rk49W2b8w_xBnIlrd75AACiQ1a2HCnu-g1GiShpIEeq3wA5Fka1OrddSDFOS8YiOpbdjuWRhmD4PG6bpoEqz8HEH8G6PrLOMJ2LfZRCrGWSumA09ZQ1tb3GtJFCk78JIAVgqnJuVchktMszJ-wTcHrBCvWGIAStgsYaEAU1bd03C7DKIKsjU6Q9b8o7whL7b5K_Gu-Z-abZY3PjtDZKp0gYeW5eW2hDVDuhx0ZuLGka5Z1oNTWbeQcZOQcfZMOyxv3zNlkGXzdHAw6Q7ZDBMSf76t7y64D062Rmv-fuiKxslQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت، چهارشنبه ۳۰ اردیبهشت پس از اظهارات خوش‌بینانه دونالد ترامپ درباره مذاکرات با جمهوری اسلامی بیش از پنج درصد کاهش یافت.
بهای نفت برنت به ۱۰۵ دلار و ۷۰ سنت رسید؛ زیرا معامله‌گران به نشانه‌هایی واکنش نشان دادند که حاکی از نزدیک‌تر شدن واشینگتن و تهران به توافقی است که می‌تواند از دور تازه حملات جلوگیری کند و نگرانی‌ها درباره اختلال طولانی‌مدت عرضه در خاورمیانه را کاهش دهد.
ترامپ گفت مذاکرات با جمهوری اسلامی در «مراحل نهایی» قرار دارد، اما هشدار داد اگر تهران با توافق صلح موافقت نکند، آمریکا ممکن است حملات بیشتری انجام دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/75580" target="_blank">📅 20:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75579">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxsTPo6XqRefFlBQE4kisrXzZZq9JsUBPWUwGIF9vbSBtskMrSZgAn2ZvyiSyAcLd-ggM0RaJm97t1tRLvk2UuXcjgpJSm8VroMCiMGthatGlu4XAXE9Oz0tGCh3nsUsvv6NUCTe_121a7T7K1retWXjRmQo9F4pZSSlnZWdpIaueLHv84mbesO7N-QRpT5csQxtsWQnIr8TS_ia7BZ_lgfjFs4AUkXtj0neJ68wgIaIlKxW6Ef50fxI4bSEvWlhBjzoWGkx3jGqo250U91xpygIkWd4E0p1TGGbsp03C_yeKSSfP7ZUstQ48MRDwW4LLS-Iw1AjAmD2aZIH_mHDgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیصل بن فرحان، وزیر خارجه عربستان سعودی، نوشت ریاض از تصمیم رییس‌جمهوری آمریکا برای دادن فرصت دوباره به مذاکرات با جمهوری اسلامی به‌منظور دستیابی به توافقی که به پایان جنگ و بازگشت امنیت و آزادی کشتیرانی در تنگه هرمز به وضعیت پیش از ۹ اسفند ۱۴۰۴ منجر شود، قدردانی می‌کند.
او همچنین از تلاش‌های مستمر پاکستان برای میانجی‌گری در این زمینه تقدیر کرد و در شبکه ایکس نوشت عربستان سعودی امیدوار است جمهوری اسلامی از این فرصت برای جلوگیری از «پیامدهای خطرناک تشدید تنش» استفاده کرده و فورا به تلاش‌ها برای پیشبرد مذاکرات پاسخ دهد.
وزیر خارجه عربستان سعودی افزود هدف از این تلاش‌ها، دستیابی به توافقی جامع است که صلح پایدار در منطقه و جهان را محقق کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/75579" target="_blank">📅 19:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75578">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=dJKAJMfD78mXDPd5_q0GkGqriEH8hbtnBQIJz7c1604EF7JXZXJ-0YUJLiXRSbku_oRvp0-QyFISi8fQQy5NP7DDLIXzUQeos-Fsoc0ZlfKcQbhLd7j3jqAFwIJlKWemseqMCVEsdPi0npGyLilvuga9mS-jEHskO9Mq4474l9Rcg95Bjsb-cqG824jSX7nnPoTswWh6cPEAqo_L4itbGixiGJzQOKZxJpKe6qqqjnwEnALMiXt-VUaJAbuuP_zpYQZ3s4wAefs7MpFGSqjuIo0CMuKINB3Ti5a7m3mq15sHzwB1yqR5i2zAPRmP6hMDRGWb3UN8BVPz2awvTtlLTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=dJKAJMfD78mXDPd5_q0GkGqriEH8hbtnBQIJz7c1604EF7JXZXJ-0YUJLiXRSbku_oRvp0-QyFISi8fQQy5NP7DDLIXzUQeos-Fsoc0ZlfKcQbhLd7j3jqAFwIJlKWemseqMCVEsdPi0npGyLilvuga9mS-jEHskO9Mq4474l9Rcg95Bjsb-cqG824jSX7nnPoTswWh6cPEAqo_L4itbGixiGJzQOKZxJpKe6qqqjnwEnALMiXt-VUaJAbuuP_zpYQZ3s4wAefs7MpFGSqjuIo0CMuKINB3Ti5a7m3mq15sHzwB1yqR5i2zAPRmP6hMDRGWb3UN8BVPz2awvTtlLTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/75578" target="_blank">📅 18:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75577">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a0e7e12e55.mp4?token=MHVwYKMpzFkBQSuTBjnhsS9A28nm0a5GBeuNk99h40UqUe4VMGi1NYLxM7kjS6GXJR-qm17C6_UzuaH4zOkP0g7U8twGxwQxxJ1xNQiG3d6iCEDiTl2cLsouOWSB5aqH2nZ1dZNQQaNXzQBDszmk8W90Z2JJDH6cJ_OYq3CON5U1tLa3ayV1RtzvIc-4A7CQWIVqI7-n_BdQoepegeF2DTLIWwDM0YCUYVG2BYPeiCkvLhotp0FGmHgRI1CRq2rUEGB_LHCdyoXE4479oHJXtlA6mkfregrMIK1W4QGmtMH3_szD2n6rRocGHIMiqSBce6XslNnByYXBjd4qNh1elQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a0e7e12e55.mp4?token=MHVwYKMpzFkBQSuTBjnhsS9A28nm0a5GBeuNk99h40UqUe4VMGi1NYLxM7kjS6GXJR-qm17C6_UzuaH4zOkP0g7U8twGxwQxxJ1xNQiG3d6iCEDiTl2cLsouOWSB5aqH2nZ1dZNQQaNXzQBDszmk8W90Z2JJDH6cJ_OYq3CON5U1tLa3ayV1RtzvIc-4A7CQWIVqI7-n_BdQoepegeF2DTLIWwDM0YCUYVG2BYPeiCkvLhotp0FGmHgRI1CRq2rUEGB_LHCdyoXE4479oHJXtlA6mkfregrMIK1W4QGmtMH3_szD2n6rRocGHIMiqSBce6XslNnByYXBjd4qNh1elQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، پیش از ترک واشنگتن به مقصد کانتیکت، در گفتگو با خبرنگاران در فرودگاه به تشریح وضعیت تقابل با ایران و گزینه‌های روی میز پرداخت.
او با اشاره به وضعیت داخلی ایران مدعی شد: «در حال حاضر خشم زیادی در ایران وجود دارد، زیرا مردم در شرایط بسیار بدی زندگی می‌کنند. ناآرامی و تلاطمی در آنجا جریان دارد که قبلا نظیرش را ندیده‌ایم؛ باید دید چه پیش می‌آید.»
ترامپ در پاسخ به سوال خبرنگار درباره احتمال انجام یک «توافق محدود برای تمدید آتش‌بس» گفت: «ما این شانس را امتحان می‌کنیم. من عجله‌ای ندارم؛ هرچند موضوع انتخابات میان‌دوره‌ای مطرح است، اما در حالت ایده‌آل ترجیح می‌دهم به جای افراد زیاد، آدم‌های کمتری کشته شوند.»
رئیس‌جمهوری آمریکا همچنین با ابراز تردید درباره نیت مقامات تهران گفت: «من متعجبم که آیا آن‌ها واقعا خیر و صلاح مردم خود را می‌خواهند یا خیر؛ رفتار آن‌ها نشان می‌دهد که به فکر مردم نیستند، در حالی که باید خیر و صلاح کل منطقه را در نظر بگیرند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/75577" target="_blank">📅 18:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75574">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QNWfxJbfffbzLIsxw_WU8SaRiyRYhFjtfMV1ISxB0wXYCl6D_WoHL4JEjYWlGsVhPV3r5g1j8wAJ6z9rX4-E-YLi-HU_OZk_YSktxx6AlhR_qs299EkDRGtZyND2YPokQ6r2lleLnKLSa5fHDRwSHYrmA4Zhv1peDfZ7rpSyaAKGqyF30xa1rgK7sPqcueeStpQJUb44yu5nl93S_2ZhUC7xwTpJ3ZjvK9ApGvAHKqk_UTdzJ71q2m0WHw3H7tzrdve6qxBDsemX6PyT1JuAwc05fMvhoZUnpm3uhxn5ZhMVObDILpQRy3xGpBKO20hon9cMpnypdBHEsH0K_AEOTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OI3fVRR6ampokkzchSqePsZMi2jkQt3EWiltOBkv-e3THSlGV1OLmSGjbUgh9cMUrUtSu2GgTDsjcIcYfnXyKESQ0tpX1an0lxO8M3uqiObiuDJZRcGBfugw-W-eZKSnJxCjOB6-P9p7u4wbw-p9doqSFgSlFFfBQpIp-TDxvW-ayT9yiSytZSCz6ERaHiOKCUd_jpiKi02d-0viUkdOmxtk1MC01BEMbKtiK5pKSGUU4ZVKCRb6usBPfDRBKzLrWZhGXu6WCyUxZxQUMlobtZT2Y6jvz9x2EiNaB7ZZJmvdrkxBjhaN6fGWWPqun0dJr8bxKCY00yNIYSteWU90vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b8d594fa0.mp4?token=D4vJRrjcCKOD-L4JLRwAXv1kDpNwJgssVFW9nSa56c4LHHkXBUwkNrBn3SC02992LMdXz6sBvr9OALHxk6RT9loOimYKKzqwV7Z7CjAtbTjJnyWAu56j9U8WgPp5O-Qm7b3ZD01TQ8TfKjlHgeXx9A4S5xU8PUgl8DIH4XxQVF4hkZ6GNrAupb4Q4lLHQCRzxBsbOUg00eWErMVUGUHmWl3JC7ne3xjGRzxMDVyZqceBsPUr3PT4x1BhF2uztWAQY9Z4nQUWSUdmlqRrlmyLhsX912K0P7vZMTKzF_VWRXvNZiy5s64D5PUfy2Dzw0282J7Ou_4K0rz04lyG7njz9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b8d594fa0.mp4?token=D4vJRrjcCKOD-L4JLRwAXv1kDpNwJgssVFW9nSa56c4LHHkXBUwkNrBn3SC02992LMdXz6sBvr9OALHxk6RT9loOimYKKzqwV7Z7CjAtbTjJnyWAu56j9U8WgPp5O-Qm7b3ZD01TQ8TfKjlHgeXx9A4S5xU8PUgl8DIH4XxQVF4hkZ6GNrAupb4Q4lLHQCRzxBsbOUg00eWErMVUGUHmWl3JC7ne3xjGRzxMDVyZqceBsPUr3PT4x1BhF2uztWAQY9Z4nQUWSUdmlqRrlmyLhsX912K0P7vZMTKzF_VWRXvNZiy5s64D5PUfy2Dzw0282J7Ou_4K0rz04lyG7njz9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت امور خارجه جمهوری اسلامی، روز چهارشنبه ۳۰ اردیبهشت‌ماه درباره گمانه‌زنی‌ها راجع به سفر عباس عراقچی به نیویورک گفت:  «وزیر خارجه ایران برای شرکت در نشست شورای امنیت سازمان ملل درباره صلح و امنیت بین‌المللی دعوت شده، اما حضور او هنوز قطعی نیست.»
به گفته سخنگوی وزارت امور خارجه جمهوری اسلامی «این نشست به ریاست دوره‌ای چین در شورای امنیت، روز پنجم خرداد برگزار خواهد شد، اما با توجه به برنامه کاری فشرده وزیر امور خارجه»، تصمیم نهایی درباره سفر هنوز گرفته نشده است.»
این اظهارات پس از آن مطرح شد که علی خضریان، عضو کمیسیون امنیت ملی مجلس، در یک برنامه تلویزیونی نسبت به احتمال سفر عراقچی به نیویورک برای مذاکره درباره تنگه هرمز انتقاد کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/VahidOnline/75574" target="_blank">📅 18:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75572">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EjVA5G5g74T2d-FyaRHqhLwnX-xzlt-SYxU7HNbMP_rFcJT-I5jB2pRBXrmJR98dNrX5o2k_d1L13RlZJJ0IUAkMk9Ee8XZxAxRCxSwmJp-Gn01AWnSdCLb1wAxbkLst55G3_NdsthJJkSpybudm-qqi1ZmgV4pkN1cJUr0EhFROQB_KG2-NqAsAUWQ2R-MDpoZQGcyk_oV_svH07wYsR0R-zeXnQ97QL-en1sVih2_wmY4pEH9RJ6P0ua2I6SH3WbstOWecv-EfWGqY59t5g4wp1D7S_dELfsrV9pEabjZ7AVdfXU41X48QyBaypSzUMn-FCAJVHtUcy8-weTCWcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qLcanxteys3RTkcOvhOTEsKA-vq3CT9WJEcBmP1v2DTwO6YP3lwM0Qxk4YyOxetNcyJNNWjC7owQg2tQsAJ02XBTyVeN-9cbq10lTNo7JBleGONHOeGNs_l7jwZaYkGKo5oc3749ySdhDIjApXKCCjB7S8-Jx7BxlTXXd734EMAyBYQxxKfhZUkyF0lg_0Cg8254FNyftARY7fb34MvVBriaMGpOUrn04wxPHdDhC2ffMA8jM5dIzhe6ygaO9LDRWkg2TIUcpmlJOVyNdKkP0c0MqoJs2ZBFHdFOZF52sYRn1jrDVh9AM4gkaCuY1ocYY-SgOSkaLfAi7Y2N-HrE8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری قوه‌قضائیه گزارش داد رشید مظاهری، دروازه‌بان پیشین تیم ملی فوتبال و استقلال تهران، «هنگام تلاش برای خروج غیرقانونی از مرزهای غربی ایران بازداشت شده است.»
میزان در این گزارش رشید مظاهری را متهم کرده که «قصد داشته با تغییر چهره و پرداخت رشوه به ماموران مرزبانی از کشور خارج شود.»
قوه قضائیه به زمان بازداشت این بازیکن پیشین تیم ملی فوتبال ایران اشاره نکرده است.
رشید مظاهری پس از کشتار معترضان در ۱۸ و ۱۹ دی، با انتشار ویدیویی در پنجم اسفند، علی خامنه‌ای را مسئول کشته‌شدن معترضان معرفی کرده بود. پس از انتشار آن ویدیو، تا مدت‌ها خبری از وضعیت او منتشر نشده بود.
خبرگزاری میزان گزارش کرده که مظاهری در «بند عمومی زندان» به سر می‌برد و قرار است به اتهام‌های «پرداخت رشوه به مامور دولت»، «فعالیت تبلیغی برخلاف امنیت ملی در شرایط جنگی» و «اقدام به عبور غیرمجاز از مرز» محاکمه شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/75572" target="_blank">📅 17:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75571">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W9v7P-qpjjqz0D-HsHf4eaL4GtvG9k1rJanDdtbJ2Bl2OcPO_0NoZDNkyTBbPD4d6E2yU1JSB6BDJnvppud6Bm2s8bdJZEyP0PYu5mN8Nxo7LaFzcMrDw6nVRiwXWve7rGZyI7fdoTA4siDulw_zWqIm4pBqM_Iibrm5CDuDQavtgQB7fl4ACijUNq8H_D4RTFqTQ4aA1io-RMXdWaUtBaPJfLAMHvnwzmGopILZ0M-EgSQiL3KoIzCRjPxeRl2bnJ0OITKEb671X2ccBC2vLaSHyZ-vk14ycHHDuN8GTMYaUEuTxRhEY-z8KF4OVMEL6u70TXAL1CyRyQpZ_FSEfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در میانه اختلال در مسیرهای رسمی تجارت و فشار بر زنجیره تأمین صنایع، سازمان توسعه تجارت ایران واردات برخی مواد اولیه پتروشیمی و پلیمری را از طریق رویه‌های کولبری و ملوانی مجاز اعلام کرد.
این تصمیم نشان می‌دهد بحران تأمین مواد اولیه در صنایع پایین‌دستی به مرحله‌ای رسیده که حکومت برای جبران کمبود، به مسیرهای مرزی و غیرمتعارف متوسل شده است.
اما این تصمیم پرسش‌های جدی ایجاد می‌کند. مواد اولیه پلیمری و پتروشیمی کالای مصرفی ساده نیستند؛ واردات آنها نیازمند حجم بالا، کنترل کیفیت، استاندارد، ردیابی منشأ، بیمه، حمل‌ونقل تخصصی و تسویه تجاری منظم است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/VahidOnline/75571" target="_blank">📅 17:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75570">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m48c8Nd10TvXP-kjFSS1UBELz7OMhJpO1xJul0uODxhxyTtoUVYDzjEpRHC3Jxbt1HeDyvSfhbDrzKB4uGc55ocAt6nhDYkUrzARMbqzuSYAHo4UiyG6H9aEoIh8YmX_ifgSpcOg1fZh9fDIIZMukCXi575NWvbJwgXvdQv-1k34O_LpcjoOMSZ_GQ8nNNOBsKHfgrir-q8gdlxss37hfJSUySB3pE8hdXxNZnTfLw8pxs_b065U0XNeuPFW7LZP9CBy2acUFr9DkfQuhlXtGFx3hS9SULxGU-EuA39GxbJclotEHPwjiYx2FhwFxtyNpzHTo7Ff66f9Nh_nhfCNQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران با انتشار بیانیه‌ای تهدید کرده که در صورت آغاز دوباره جنگ آمریکا و اسرائیل علیه ایران، جنگ «به فراتر از منطقه کشیده خواهد شد.»
در این بیانیه با اشاره به تهدیدهای دونالد ترامپ و مقام‌های اسرائیل برای حمله مجدد به ایران آمده: «اگر تجاوز به ایران تکرار شود جنگ منطقه‌ای که وعده داده شده بود، این بار به فراتر از منطقه کشیده خواهد شد و ضربات کوبنده ما در جاهایی که تصور آن را ندارید شما را به خاک سیاه خواهد نشاند.»
عباس عراقچی، وزیر خارجه ایران هم در واکنش به اظهارات تهدیدآمیز دونالد ترامپ، رئیس‌جمهور آمریکا، درباره احتمال از سرگیری حمله نظامی به ایران، در شبکه ایکس نوشته «با درس‌هایی که آموخته‌ایم و دانشی که به دست آورده‌ایم، مطمئن باشید بازگشت به میدان جنگ با شگفتی‌های بسیار بیشتری همراه خواهد بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/VahidOnline/75570" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75569">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtI0MTeuwGyxnLu_crlK4imVWn-6RSYNmCjGp0FM8KG-pk5xa-u50bGJhfewsSB-55CM4oMGsTVTRbF-54GH74aY94CGZRT67ZwfxoP3fhRqia8_oCG_ndiBW-PyEMeX6ssuBPvn-D4Ck7lj-og6nfVx1taLlEyUq9EOxJDm-Pyf_uxb0yyZFD1K3UNRsYk8w3PK9RfVHo_YTM_UskWPK_OHIbe-MUBDmCBPUD_V3xGB6cVofUV8JeRW_80obEDBnMaE4L190-RZdqLt45rgoTm_hrqTj0BGkJy-fDS94weA7Xlb8rHEmRZFe9dkjbozfwj4l2HgYyLzTHMoc-zQvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران روز چهارشنبه ۳۰ اردیبهشت خبر دادند که محسن نقوی، وزیر کشور پاکستان، وارد تهران شده است. او روز ۲۶ اردیبهشت نیز به ایران سفر کرده بود.
خبرگزاری ایسنا اعلام کرده که برنامه و اهداف سفر این مقام ارشد پاکستانی در ایران «مشخص نیست». خبرگزاری تسنیم نیز گزارش داده که آقای نقوی در بدو ورود به تهران با وزیر کشور ایران دیدار کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/VahidOnline/75569" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75568">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gF6BjzW8qh-xi91jq_sIe-dBWttfluX_hcMmatFL-FdQofSb7SOR1Q1fqBwbN6D0K-04bnn9cWyDzGPEybsVg-8UXp2UV7uv0EBWAZPvDKjz9icD699WOnwYHtw5rvI2PfueNzpe2z3T0nziWVZmzxZ9Y-_YXv-02UEL2m3LRWw4SmdwURUI1qT1G1gaZ0qmahWZ-BTomXMvIrT18GhyLUnMGyYyEfrGgqLKKjyOr6cJC5-AoAxt0eFOfXpnxbel4AclQyMBI7lxPPRt8PF52xCF4HXYpqFBuHmAeNZe340yNCB1tS0sK8sJ8Kycz9ibVtDzNiHhYiAh_zc5GHi1wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها در ایران از اجرای حکم اعدام قاتل الهه حسین‌نژاد، که جسد او اوایل خرداد سال گذشته در بیابان‌های اطراف تهران پیدا شد، خبر می‌دهند.
عصر چهارم خرداد ۱۴۰۴ الهه حسین‌نژاد ۲۴ ساله از سالن زیبایی که در آنجا مشغول به کار بود، بیرون آمد تا به خانه‌اش در اسلامشهر برود، اما ناپدید شد و وقتی خانواده‌اش اعلام شکایت کردند بررسی‌های تیم جنایی نشان می‌داد الهه از میدان آزادی سوار یک خودروی عبوری شده است.
جست و جوها برای یافتن الهه سرانجام پس از ۱۱ روز نتیجه داد و با دستگیری راننده خودرو به نام بهمن ۳۷ ساله و اعتراف به قتل الهه، جسد او در بیابان‌های اطراف تهران پیدا شد. متهم نیز پس از محاکمه به اعدام محکوم شد.
این قتل جنجال زیادی درباره امنیت زنان در ایران به پا کرد و تا مدت‌ها رسانه‌ها درباره آن مطالب مختلفی منتشر می‌کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/VahidOnline/75568" target="_blank">📅 17:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75567">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VPzYAdXFvaIE2_Ti3P_0I3e-iOnamothPMqF2EDFmwvIo8xhQ9xcK8GKXvBEBOZJ-m9JFJ7Je4ECL0_oHzZKOhCKGmm3vbB7pbqhUcaYILzkitvmQzEX0kuz_q7NS4yi6ppYVM6j_v5VmxpNnVTWnJosfW8lkFfcDfwHTg8S0l8oSX-mimj-Ayz8zcfzozh7gv6RU8x9fq0nImdwOnCcUbpzRtYDk4qZKTV6SGbaDGsrEo6oWnQnUY1IjtluoMCW63iSwpYVse3YU9xbEpuJw_-V9cuwD0005RQxpQ5gAeKZqsGbEl3VrFG4IG4dX9fWo3T92XzreI7hw4dXIokMSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حقوق بشری گزارش دادند دادگاه کیفری تهران پس از رسیدگی دوباره به پرونده شهرک اکباتان، سه معترض بازداشت‌شده در این پرونده را به دیه و پنج سال حبس محکوم و سه معترض دیگر را از اتهام مشارکت در «قتل عمد» تبرئه کرد. حکم اعدام این شش تن پیش‌تر در دیوان عالی کشور نقض شده بود.
سایت هرانا چهارشنبه ۳۰ اردیبهشت گزارش داد شعبه ۱۳ دادگاه کیفری یک استان تهران، میلاد آرمون، علیرضا کفایی و امیرمحمد خوش‌اقبال را بابت اتهام «مشارکت در قتل عمد» آرمان علی‌وردی، از نیروهای بسیج، محکوم کرد. هر یک از آن‌ها به پرداخت سهم مساوی از دیه کامل یک انسان و پنج سال حبس محکوم شده‌اند.
طبق گزارش هرانا، نوید نجاران، حسین نعمتی و علیرضا برمرزپورناک، سه متهم دیگر این پرونده، به دلیل «فقدان مدارک دال بر وارد کردن ضربه به ناحیه مشخصی از بدن علی‌وردی» از اتهام مشارکت در قتل عمد تبرئه شدند.
این حکم ۱۵ بهمن سال گذشته صادر و سه‌شنبه ۲۹ اردیبهشت به وکلای این افراد ابلاغ شده است.
این شش شهروند معترض در آبان ۱۴۰۳ از سوی همین شعبه به اعدام محکوم شده بودند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/75567" target="_blank">📅 17:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75566">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d4724dd573.mp4?token=UUEhea5cynFgG2GD1F-osoQDTzvsRUqbas-xhVfG6lcsxqJvolhDf3ubBJ94Dv6tzOnjI3laJIp61dlKG_awgkNMcmC9VyajrhFIKqnjeMZZjcklvVwjri0sotFHfEV-ZjV8S_mNdiJ0712rjrjxNnfaozSSDXu07QtByQEbCDkFtoXmnIa-6B_bb6r84WHrz7ZKzbuuFidmnpHRcrsfcgPblFHQbyByD9InybOnWnmY5drkiSPHpbry2mavkonVAPNQiydfF7XVxr0TdhqO4uqXrxjba58jX_m2SjpWm5iWV6L-TygJ-icPQuxfo6F6kQ5IzQGFsiaqid4ypUSiSg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d4724dd573.mp4?token=UUEhea5cynFgG2GD1F-osoQDTzvsRUqbas-xhVfG6lcsxqJvolhDf3ubBJ94Dv6tzOnjI3laJIp61dlKG_awgkNMcmC9VyajrhFIKqnjeMZZjcklvVwjri0sotFHfEV-ZjV8S_mNdiJ0712rjrjxNnfaozSSDXu07QtByQEbCDkFtoXmnIa-6B_bb6r84WHrz7ZKzbuuFidmnpHRcrsfcgPblFHQbyByD9InybOnWnmY5drkiSPHpbry2mavkonVAPNQiydfF7XVxr0TdhqO4uqXrxjba58jX_m2SjpWm5iWV6L-TygJ-icPQuxfo6F6kQ5IzQGFsiaqid4ypUSiSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوتین هم به خدمت شی رسید.
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75566" target="_blank">📅 07:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75565">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GJuLQde3XLbJHml6r6ut_ea6hYkDPkBupPLKej7X1BEVfv93034Rhzudyt5qzU-c22aS2vdCkS9sVRYiYK5IhqcrvoAMhXoh4X38u4X5LgIlwu3sgyLVzruPPgV0d3Cf7b9N9tynIF3-ybct7QOqazva8lhYQnVgL0RQGtbJL43-frQdo_yGEYizccXRYyENm6N0uPVmkWpD2ixFAs-pioBFSp9KlXyx9N7NjBAynAg3MzSwZvplYZMjf7qUoVnGHhRWPEu5hUWfEHZZf13lvssgq1pVQHXbd1gdKFHQw0f2kJA5wN82HgMo2ZEfND7Me-LwkDgoOufPeFdbc2geLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین
تیتر نیویورک‌تایمز: هدف اولیه جنگ، روی کار آوردن رئیس‌جمهور تندروی پیشین به عنوان رهبر ایران بود
بخش‌های خبری مطلب:
به گفته مقامات آمریکایی، حمله اسرائیل که با هدف آزادی محمود احمدی‌نژاد از حبس خانگی در تهران طراحی شده بود، بخشی از تلاش‌ها برای تغییر رژیم و به قدرت رساندن او بود.
چند روز پس از آنکه حملات اسرائیل در آغازین روزهای جنگ، رهبر ایران و سایر مقامات ارشد را به قتل رساند، پرزیدنت ترامپ علناً اظهار داشت که بهتر است «شخصی از درون» ایران کنترل کشور را به دست بگیرد.
اکنون مشخص شده است که ایالات متحده و اسرائیل با در نظر داشتن شخصیتی خاص و بسیار غافلگیرکننده وارد این درگیری شدند: محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران که به دلیل دیدگاه‌های تندرو، ضداسرائیلی و ضدآمریکایی‌اش شناخته می‌شود.
اما بر اساس گفته‌های مقامات آمریکاییِ مطلع از این موضوع، این طرح جسورانه که توسط اسرائیلی‌ها تدوین شده بود و با آقای احمدی‌نژاد نیز درباره آن مشورت شده بود، به سرعت با شکست مواجه شد.
مقامات آمریکایی و یکی از نزدیکان آقای احمدی‌نژاد اعلام کردند که او در روز اول جنگ بر اثر حمله اسرائیل به خانه‌اش در تهران - که برای رهایی او از حصر خانگی طراحی شده بود - مجروح شد. آن‌ها گفتند که او از این حمله جان سالم به در برد، اما پس از این خطر جانی، نسبت به طرح تغییر رژیم دلسرد و ناامید شد.
او از آن زمان تاکنون در انظار عمومی دیده نشده است و مکان و وضعیت فعلی او نامشخص است.
...
اینکه آقای احمدی‌نژاد چگونه برای مشارکت در این طرح به کار گرفته شد، هنوز در هاله‌ای از ابهام قرار دارد.
...
سخنگوی موساد، سازمان اطلاعات خارجی اسرائیل، از اظهارنظر در این باره خودداری کرد.
...
مقامات آمریکایی گفتند که این حمله - که توسط نیروی هوایی اسرائیل انجام شد - به منظور کشتن نگهبانان مراقب آقای احمدی‌نژاد و به عنوان بخشی از طرحی برای رهایی او از حبس خانگی صورت گرفت.
این حمله آسیب چندانی به خانه آقای احمدی‌نژاد که در انتهای یک کوچه بن‌بست قرار داشت، وارد نکرد. اما پاسگاه امنیتی در ورودی کوچه مورد اصابت قرار گرفت. تصاویر ماهواره‌ای نشان می‌دهد که آن ساختمان ویران شده است.
در روزهای پس از آن، خبرگزاری‌های رسمی روشن کردند که او جان سالم به در برده است، اما «محافظان» او - که در واقع اعضای سپاه پاسداران انقلاب اسلامی بودند و همزمان وظیفه محافظت و نگهداری او در حبس خانگی را بر عهده داشتند - کشته شده‌اند.
مقاله‌ای در نشریه آتلانتیک در ماه مارس، با استناد به منابع ناشناس نزدیک به آقای احمدی‌نژاد، نوشت که رئیس‌جمهور پیشین پس از حمله به خانه‌اش از حصر دولتی آزاد شده است؛ این مقاله آن رویداد را «در عمل یک عملیات فرار از زندان» توصیف کرد.
پس از انتشار آن مقاله، یکی از نزدیکان آقای احمدی‌نژاد در گفتگو با نیویورک تایمز تأیید کرد که آقای احمدی‌نژاد این حمله را به عنوان تلاشی برای آزادی خود تلقی کرده است. این فرد مطلع گفت که آمریکایی‌ها آقای احمدی‌نژاد را شخصی می‌دانستند که می‌تواند ایران را رهبری کند و توانایی مدیریت «وضعیت سیاسی، اجتماعی و نظامی ایران» را دارد.
این فرد مطلع اظهار داشت که آقای احمدی‌نژاد می‌توانست در آینده نزدیک «نقش بسیار مهمی» در ایران ایفا کند و اشاره کرد که ایالات متحده او را شبیه به دلسی رودریگز می‌دید؛ کسی که پس از دستگیری آقای مادورو توسط نیروهای آمریکایی در ونزوئلا قدرت را به دست گرفت و از آن زمان همکاری نزدیکی با دولت ترامپ داشته است.
...
در چند سال گذشته آقای احمدی‌نژاد سفرهایی به خارج از ایران داشته است که به گمانه‌زنی‌ها دامن زده است.
به گزارش مجله نیولاینز، او در سال ۲۰۲۳ به گواتمالا و در سال‌های ۲۰۲۴ و ۲۰۲۵ به مجارستان سفر کرد. هر دو کشور روابط نزدیکی با اسرائیل دارند.
ویکتور اوربان، نخست‌وزیر مجارستان در آن زمان، روابط نزدیکی با آقای نتانیاهو دارد. در طول این سفرها به مجارستان، آقای احمدی‌نژاد در دانشگاهی مرتبط با آقای اوربان سخنرانی کرد.
او تنها چند روز قبل از آغاز حملات اسرائیل به ایران در ژوئن گذشته از بوداپست بازگشت. زمانی که آن جنگ درگرفت، او حضور علنی کمرنگی داشت و تنها چند بیانیه در شبکه‌های اجتماعی منتشر کرد. سکوت نسبی او در مورد جنگ با کشوری که آقای احمدی‌نژاد مدت‌ها آن را دشمن اصلی ایران می‌دانست، مورد توجه بسیاری در شبکه‌های اجتماعی ایران قرار گرفت.
...
nytimes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/75565" target="_blank">📅 06:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75564">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FbD1tPRmk2SGdddFMQe6XBeozZO49MGXeAsp7WwwZ0Vx38QddyLTiXMy1Xd5TTYi8Qpu1U23QUv4pDv1gasZacZueSCYYDEzv5S7wMSHr0EClxtMmJ21LiXObmIk9rkYJam2tyWSqiJBCeomkmwovv8GcEm805si482byPJFwDGy0pr5MmyNyS3sv7sl2g7HBl1KKxkrxMmHf3Ypd6YM2mBLxmGb7RN-eQ17LVTzSn3FsiYWhZHb2T78Ytry1wb2g2MWltTJ1mHznTqWPy7m0yGK9OAuteHkbDZ0dg6-Txk0FLtPMHncOg3pLp4gZsqhSY3pDBNUA-ijulD3I3VtbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در یک سخنرانی در کاخ سفید گفت  ایران قرار نیست به سلاح هسته‌ای دست پیدا کند. نمی‌توانند سلاح هسته‌ای داشته باشند. ما نمی‌توانیم چنین چیزی را تحمل کنیم و آن را تحمل نخواهیم کرد.
او گفت ما نیروی دریایی آن‌ها را نابود کردیم. نیروی هوایی آنها از بین رفته است. سامانه‌های پدافند هوایی آنها از بین رفته است. تمام تجهیزاتی که برای جنگ استفاده می‌کردند از بین رفته است. تقریبا همه چیز از بین رفته است.
ترامپ افزود: نمی‌خواهم بگویم رهبران آنها از بین رفته‌اند، چون بیان آن چندان خوشایند نیست، اما واقعیت همین است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/75564" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75563">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G6Nx2gFF1ex7j4jJIC1QQc5qUfgeSxTwEhHpTpEfvJxgdeT5qZimRxq0wdcBVKORucvwqT2hFjsLinkIIjnw7_S7TkC_b7QYqCewWuK3S-UJmXY5NECvtyEUEoAa7B8kJsVoNs5dVFt3aqaNkNtaNwQDRx57MtkQOafKAhB2gKBYFp8uuXPTBgf9ewmz2QpjNCCW9CUiTHTtVj5yKxUbfop8Cc2N95xyVksuQrjSG4cLQlP3EXrI8Lvd_Cd2yaicEttZTTLVUsDKVjV5EeFQqbIpansBj1mYxcZBLFQgdU-sRhVTa0t-9pA6_ze01wi_2G9o37fDqYJtiFvFNr75ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه در قشم
آپدیت:‌
تصویر بالا:
#زلزله
به بزرگی ۴٫۷ در عمق ۲۰ کیلومتری بندر لافت در جزیره قشم هرمزگان
پیام‌های دریافتی:
سلام وحید دو زلزله شدید بندرعباس رو لرزاند
ساعت ۳:۱۱ دقیقه بندرعباس زلزله اومد
همین الان ساعت ۳:۱۲ دوبار به مدت ۱۵ ثانیه وحشتناک بندرعباس لرزید
من بندرعباس هستم دو بار لرزید
زلزله اومده خیلی بد بود
زمین لرزه نسبتا شدید ساعت ٣:١٠ بامداد بندرعباس
بندرعباس هستم فکر کردیم باز زدن دقیقا ۲۰ ثانیه همه جا میلرزید
چند دقیقه پیش زمین لرزه نسبتا شدید اومد دوبار تو فاصله خیلی کم بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/75563" target="_blank">📅 03:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75562">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v6DwTvNH9hJNcIBhp_Ja2oTL9EKfDBafm0p6klkxDLbiZW3K4HcrlguYbQAR6dasrupduvaDauiGmIDvrMeQ_7NiPcqHxXyaWzu8Ft0CP6YCdZh3YrMCItK7sRvG9KrujxrbSQMe_IiyV7OLdy0k_Ency7XK1jJhAPzkwJBCz6WHY24gCG9DjR8-R9E1gp1eClDu3lQgtUU28CFs5pbjGfAqXAa4sK-DQj84QgexKmDGqk905om-7owwxL3sf8QAKq_OhWgi_d70noQmTtvfB0IjJ0c8IPl1ypDfmxhWKRYTk4DKyT_EcuFreUA0uf1r1V1flZ1Yrw7wX0vnx_HSiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا روز سه‌شنبه قطعنامه‌ای را برای توقف اقدام نظامی در ایران پیش برد.
پیش بردن این قطعنامه پس از آن صورت گرفت که سناتور جمهوری‌خواه، بیل کسیدی از لوئیزیانا، به آن رای مثبت داد. کسیدی چند روز پیش، در رقابت‌های درون حزبی ایالتی برای ادامه حضورش در سنا، به نامزدی که از حمایت ترامپ برخوردار بود، باخت.
به گزارش سی‌ان‌بی‌سی، با وجود اینکه قطعنامه اختیارات جنگی با نتیجه ۵۰ به ۴۷ به تصویب رسید، اما هنوز احتمال کمی برای تبدیل شدن به قانون دارد. این قطعنامه باید ابتدا در سنا به تصویب نهایی برسد، سپس مجلس نمایندگان به رای بدهد و سپس نیز، دونالد ترامپ به احتمال قریب به یقین، آن را وتو خواهد کرد.
@
VahidHeadline
چهار جمهوری‌خواه هم‌حزبی ترامپ همراه با همه دموکرات‌ها به جز یک نفر، به آن رای مثبت دادند. سه سناتور جمهوری‌خواه نیز در رای‌گیری غایب بودند.
باوجود تصویب این آیین‌نامه، حتی اگر قطعنامه‌ای در سنا با ۱۰۰ عضو هم به تایید برسد، کار دشواری در مجلس نمایندگان خواهد داشت که تحت کنترل جمهوری‌خواهان است و پس از آن نیز باید دو‌سوم رای کنگره و سنا را داشته باشد تا بتواند گزینه وتوی احتمالی رئیس‌جمهور را دور بزند.
طبق قانون اختیارات جنگی آمریکا مصوب ۱۹۷۳ که در واکنش به جنگ ویتنام تصویب شد، رئیس‌جمهور آمریکا تنها ۶۰ روز می‌تواند بدون مجوز کنگره عملیات نظامی انجام دهد و پس از آن باید یا جنگ را متوقف کند، یا از کنگره مجوز بگیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/75562" target="_blank">📅 02:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75556">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RsJ0_A8eTXrW8qgq9Ha5tC-4ck9CmoN1xm-hCSlGKwTP8OWJSe1DPJMt1x4AFG_lyI3YE1ydcL5XbQcitkAH4sJo7o4XdGZFBD6ufMx2T7a1r8fcbkAZqYIFFPtxQNK5MKJtG6ULp2dBQbSj4CFnVRDMLriUtoQ6Eh8d_ztFCK6ad9vW2kRC7KRQjaWidh6e-z-iHMo1gBlEkvgYSCv__fILySibIP6UD4PiPcwy1p7khC93eh0ujRKthoCHm3JKM7KIVHt4rywIJ66_5hFCHc4_YcjbFOmUP0oKfzW81W3--l0JCsNoxJJSMC_PhISO4nhrLKh7a4XkvZvVaRSuHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jJThOU4LQgKV4i25yHJekhM5f8mlw4Qtm3BFPE_nrAJJ44bNG4nyLn2RxHt7TK9VcjaEn2HmC9elXr3h0Skv-48-4u55HCgbz25sG8x7F68DrJP_wtZaW1rtWrXGTvTkKyd8Twm_oohkOhWt8ls1RAlhtT3pw24X7UhjxKFqNo7LaFg1TJK9mpOGJAtn4o-HJzs_F28MnmuMJ2AO-Orkv419YVpE7Z5-lNKIFnwZq5IWrnUGVTnIwLvyDGc0iwXNWjgU7SX41Xb5Jw2gGvxcc-InSha41y7bhOPVOvHFIo6T_cmK33ZUcqTfvlbDFlPLzfIcF74fEbrAusqDr5aP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Roc7nnKlHHO_PmCXtOBchvzaN87W5rufYCMoDWWt3NbcFeV5n8LSr4-ccMeZKonvvInNaIxkmNj9hu2aGrg3LPanALmL0qto9eyX7gjcjR96fT8jGondghvnTDhkqSpwFrJJB0W4ciCOvl3ibTJoJ8nf_8ylg0Srze4P4MVMDZ90I1zs0OzSnZH2WuuRWGj6xyKlMUJOt9FWv11m7G8GhR8vNu5DoKG7GueQqCQ3YVgLvwUDBpnD865KRn7ewD0mJxHciJnAS830NDq5NIwAfVA05Fp3HObBVhgp6OB0D5xH4MyqAJZ9b5gFgSVPf_LA2-6db3Ru8UdTcEptAclPuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hSAfCRi1wHLbiClznqqPK6pKtXGc20Ld9fQm1DGwyK9zB1Y43ZVcJumiI5MizCalnxCN4pEb_Oqj8UWCPSQUfV5n4bOT_-fZha8OmXmZ1xlDPVNvVmhix38y_hv5Tdemn9a9VIhi7AVO_omqCWXu9mGkxgOPDrt4z04RPqJvHZVuHX8rZ7sA0FKwF2azqSU0GcAq0o0UsqX0nk5avrrSFTlN1rpYTgLinWSEGk6SvsO1oLtNbwzCkm6E5G8bqNU-3DQn9YRHq3CEVAOxlms-WgRUcaoVITqIPSYuv3eWg1Zd3c3tIQgUgM-pXq5Zg_TWiAb7dzwt6pAiN3jejH99mA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97d125f04d.mp4?token=SFZ1XTGfZju9enklm9Xvq5k8lqT4-zD1QAsl-tO_2K6yrHW6NNLDEp5Ys9YtJRaj-_04I27lPajMd724Jye9i5jO5GWyQsHU47ykI3Sq9ELospUentMG4mneoT_OI_UR_7kZ5jHFykLVMfw-Js9IVf2nrSvxij9CVaUwyfrVOCghxMF-YYjqJjEcr5H6rvZ0FRcu6c_6C0D-Hc5wIWIbSFtH61cZ5pfyfKmuEHP-fHJyVrst4I1cdjMYhkP8NpuRfDxFo60aZ5nX1VfHcMLLf785_lsNxWwAGMSfS_1R2BWc9MLdWj101p8GKsYVxkq56NqmP1uZ-AmXrx6BFneDpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97d125f04d.mp4?token=SFZ1XTGfZju9enklm9Xvq5k8lqT4-zD1QAsl-tO_2K6yrHW6NNLDEp5Ys9YtJRaj-_04I27lPajMd724Jye9i5jO5GWyQsHU47ykI3Sq9ELospUentMG4mneoT_OI_UR_7kZ5jHFykLVMfw-Js9IVf2nrSvxij9CVaUwyfrVOCghxMF-YYjqJjEcr5H6rvZ0FRcu6c_6C0D-Hc5wIWIbSFtH61cZ5pfyfKmuEHP-fHJyVrst4I1cdjMYhkP8NpuRfDxFo60aZ5nX1VfHcMLLf785_lsNxWwAGMSfS_1R2BWc9MLdWj101p8GKsYVxkq56NqmP1uZ-AmXrx6BFneDpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهور آمریکا، گفت واشینگتن و تهران پیشرفت زیادی در گفت‌وگوهای خود داشته‌اند و هیچ‌یک از دو طرف خواهان ازسرگیری کارزار نظامی نیستند.
ونس افزود: «ما فکر می‌کنیم پیشرفت زیادی داشته‌ایم. تصور می‌کنیم مقام‌های تهران نیز می‌خواهند به توافق برسند.»
او گفت آمریکا می‌تواند کارزار نظامی را از سر بگیرد، اما «این چیزی نیست که ترامپ یا ایران می‌خواهند.»
ونس همچنین گفت: «فکر می‌کنم جمهوری اسلامی می‌خواهد توافق کند، اما تا زمانی که توافق امضا نشود، نخواهیم دانست.»
@
VahidOOnLine
جی‌دی ونس اعلام کرد که دولت ترامپ برای دستیابی به توافقی جهت پایان دادن به جنگ تلاش می‌کند، اما او همچنان شاهد وجود شکاف و گسست در میان سران ایران است و موضع مذاکراتی تهران شفاف نیست.
معاون رییس‌جمهور آمریکا گفت: «خودِ ایرانی‌ها هم دقیقا مطمئن نیستند که می‌خواهند در چه مسیری حرکت کنند؛ آن‌ها در حال حاضر کشوری چندپارچه و دارای شکاف هستند.»
او در ادامه افزود: «در ساختار حاکمیتی این کشور، رهبر وجود دارد و در رده‌های پایین‌تر از او نیز مقامات زیادی هستند که بر روند مذاکرات نفوذ دارند. به همین دلیل، گاهی اوقات اصلا مشخص نیست که موضع واقعی تیم مذاکره‌کننده چیست.»
ونس  با اشاره به اینکه هنوز روشن نیست این تشتت آرا ناشی از ضعف در هماهنگی است یا سوءنیت، تاکید کرد که نتیجه این وضعیت، ایجاد فرآیندی مبهم و سردرگم‌کننده بوده است. ونس در پایان گفت: «با اطمینان می‌گویم که گاهی درک این نکته که ایرانی‌ها دقیقا می‌خواهند از این مذاکرات به چه هدفی دست یابند، بسیار دشوار است.»
@
VahidOOnLine
جی‌دی ونس گفت اعضای تیم مذاکره‌کننده جمهوری اسلامی برخی ویژگی‌های ایرانیان، از جمله «هوش و سختکوشی» را دارند، اما همزمان مواضع «بسیار تندروانه» نیز در میان آن‌ها دیده می‌شود.
معاون رئیس‌جمهوری آمریکا با توصیف ایران به‌عنوان «تمدنی بزرگ و پرافتخار» گفت مردم ایران «شگفت‌انگیز» هستند و جامعه ایرانی-آمریکایی در ایالات متحده نیز نمونه‌ای از این ویژگی‌ها را نشان می‌دهد.
او در عین حال افزود گاهی مشخص نیست تهران دقیقا چه هدفی را از مذاکرات دنبال می‌کند و ساختار تصمیم‌گیری در جمهوری اسلامی را «چندپاره» توصیف کرد.
ونس همچنین بار دیگر تاکید کرد واشنگتن اجازه نخواهد داد جمهوری اسلامی به سلاح هسته‌ای دست پیدا کند و هدف مذاکرات، جلوگیری بلندمدت از بازسازی توان هسته‌ای جمهوری اسلامی است.
@
VahidOOnLine
جی‌دی ونس اعلام کرد: «فکر می‌کنم ما در حال حاضر فرصتی داریم تا رابطه‌ای را که طی ۴۷ سال گذشته بین ایران و ایالات متحده وجود داشته است، بازتنظیم کنیم.»
معاون رئیس‌جمهوری آمریکا که در نبود کارولین لویت، سخنگوی کاخ سفید، مسئولیت نشست خبری روزانه را بر عهده داشت، در ادامه افزود: «این همان چیزی است که رئیس‌جمهوری از ما خواسته و ما به تلاش در این مسیر ادامه خواهیم داد. اما برای این کار، همراهی هر دو طرف لازم است (یک دست صدا ندارد).»
ونس با تبیین خطوط قرمز واشنگتن تاکید کرد: «ما به توافقی که به ایرانی‌ها اجازه دسترسی به سلاح هسته‌ای را بدهد، تن نخواهیم داد. بنابراین، همان‌طور که رئیس‌جمهوری ترامپ به من گفت، ما در حالت آماده‌باش کامل نظامی هستیم. ما تمایلی به پیمودن این مسیر [از سرگیری جنگ] نداریم، اما اگر مجبور شویم، رئیس‌جمهوری آمادگی و توانایی پیشبرد آن را دارد.»
@
VahidOOnLine
ونس افزود که به‌تازگی با آقای ترامپ صحبت کرده و رئیس‌جمهور آمریکا تأکید کرده است که مسئله اصلی برای آمریکا این است که ایران هرگز نباید به سلاح هسته‌ای دست پیدا کند.
ونس یادآوری کرد که اگر چنین اتفاقی بیفتد، کشورهای حاشیه خلیج فارس نیز به‌دنبال سلاح هسته‌ای خواهند رفت و سپس کشورهای دیگر جهان هم همین مسیر را دنبال خواهند کرد.
او گفت: «ما می‌خواهیم تعداد کشورهایی که سلاح هسته‌ای دارند محدود باقی بماند، و به همین دلیل ایران نمی‌تواند سلاح هسته‌ای داشته باشد.»
وقتی از ونس پرسیده شد که آیا ممکن است روسیه مالکیت اورانیوم غنی‌شده ایران را در اختیار بگیرد، او پاسخ داد: «این در حال حاضر برنامه دولت ایالات متحده نیست. ایرانی‌ها هم چنین موضوعی را مطرح نکرده‌اند.»
@
VahidHeadline
جی‌دی ونس همچنین گفت واشینگتن می‌خواهد جمهوری اسلامی فرایندی را بپذیرد که تضمین کند ایران حتی سال‌ها بعد از دوران ریاست‌جمهوری ترامپ هم نتواند توان هسته‌ای خود را بازسازی کند.
او گفت: «ما می‌خواهیم نه فقط تعهد به عدم دستیابی به سلاح هسته‌ای را ببینیم، بلکه می‌خواهیم تعهدی برای همکاری در یک فرایند ببینیم تا اطمینان حاصل شود که نه فقط اکنون، نه فقط وقتی دونالد ترامپ رئیس‌جمهور است، بلکه سال‌ها بعد هم ایرانی‌ها به دنبال بازسازی توان هسته‌ای خود نباشند.»
او افزود: «این چیزی است که ما در مذاکرات در تلاش برای رسیدن به آن هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75556" target="_blank">📅 22:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75555">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83fd4e1acd.mp4?token=F5r7H6xQttu3O_wg7NaXGuUlW8fPxitrT2cqrFPokWZzGZrvYEMSsYRgyI0txmcDt47itqR7eueETYwj2RNthYHEQqqKBBQ-TOQPEUK9kaX7yBxiJVuITInGkwVK3nL3H1VvDXHTADgEGPw3cdxVNJfrYq9iWrc_Q7G9xQdXUhMZtPP10mw4Wi4DtQZwh4X-_1dNZ7ot11USrkkD2LV5lTxHT-mXPZt9MOivOI0sGJknQcjFO8X2T7Krqubp6uRfg1xojDDI4IfUqbOThNr2r31vdSWIS7rUWWhRICsCAGqx2uFxf7_rqHC_du0mr9puU1-g3m_uJeV5UoBFDfa1_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83fd4e1acd.mp4?token=F5r7H6xQttu3O_wg7NaXGuUlW8fPxitrT2cqrFPokWZzGZrvYEMSsYRgyI0txmcDt47itqR7eueETYwj2RNthYHEQqqKBBQ-TOQPEUK9kaX7yBxiJVuITInGkwVK3nL3H1VvDXHTADgEGPw3cdxVNJfrYq9iWrc_Q7G9xQdXUhMZtPP10mw4Wi4DtQZwh4X-_1dNZ7ot11USrkkD2LV5lTxHT-mXPZt9MOivOI0sGJknQcjFO8X2T7Krqubp6uRfg1xojDDI4IfUqbOThNr2r31vdSWIS7rUWWhRICsCAGqx2uFxf7_rqHC_du0mr9puU1-g3m_uJeV5UoBFDfa1_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهور آمریکا سه‌شنبه به خبرنگاران در کاخ سفید گفت ممکن است مجبور شویم دوباره به  ایران ضربه بزنیم، مطمئن نیستم.
او گفت منظورم این است که دو یا سه روز، شاید جمعه، شنبه، یکشنبه، چیزی در این حدود، شاید اوایل هفته آینده؛ یک بازه زمانی محدود، چون نمی‌توانیم اجازه دهیم آن‌ها سلاح هسته‌ای جدید داشته باشند.
رییس‌جمهور آمریکا ادامه داد که او دوشنبه تنها یک ساعت با تصمیم‌گیری برای انجام یک حمله فاصله داشت، اما این حمله را به تعویق انداخت.
او افزود جمهوری اسلامی برای رسیدن به توافق التماس می‌کند.
ترامپ درباره جنگ گفت: «همه به من می‌گویند این کار محبوب نیست، اما من فکر می‌کنم خیلی محبوب است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/75555" target="_blank">📅 18:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75554">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1d001deba.mp4?token=YMFaHqw56uNCGBNYr55opvDCrlb9hWVQeMiLEDvYXUIzC2j1VYBOPMNTq5PmqMVFZRZ_Dy9Uz6WbdtUEw8Bh9iKQ1eBSdSkfNOAt79UTEFGSW5Hez7m23FOdeMmcodENwgqs2872K-PXk4YBulkzLzKdIftNq0y60SyFd8F25yAvVmXUY40iME48PZ4wubaxTEk6AodKclsEL_InW7OJVg276EI4UM2ER4wn8vmn0z56xQihN7z_0iikqPYuwULzz3zpS3M6N1bdSoS5PxfnuHoIghEdesBFWGJ9JjUbFsghqLc-0lPmjUpZTLvXR_rTJJvfhrlJqV7LcyScxVkAqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1d001deba.mp4?token=YMFaHqw56uNCGBNYr55opvDCrlb9hWVQeMiLEDvYXUIzC2j1VYBOPMNTq5PmqMVFZRZ_Dy9Uz6WbdtUEw8Bh9iKQ1eBSdSkfNOAt79UTEFGSW5Hez7m23FOdeMmcodENwgqs2872K-PXk4YBulkzLzKdIftNq0y60SyFd8F25yAvVmXUY40iME48PZ4wubaxTEk6AodKclsEL_InW7OJVg276EI4UM2ER4wn8vmn0z56xQihN7z_0iikqPYuwULzz3zpS3M6N1bdSoS5PxfnuHoIghEdesBFWGJ9JjUbFsghqLc-0lPmjUpZTLvXR_rTJJvfhrlJqV7LcyScxVkAqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی کارزار ایران‌اینترنشنال برای یافتن هویت پیکر جاویدنامان در بیمارستان الغدیر تهران، ویدیویی از لحظه قتل جاویدنام آیدا عقیلی به دست ما رسیده است.
آیدا عقیلی، ۳۴ ساله، شامگاه ۱۸ دی ۱۴۰۴ در شرق تهران با شلیک دو گلوله ماموران به سرش کشته شد که پیکر او را پیچیده در پتویی چهارخانه در حیاط پشتی بیمارستان الغدیر یافتند.
@
VahidOOnLine
مربوط به این تصاویر تکان‌دهنده: @
VahidOnline
این ویدیوی دلخراش: @
VahidOnline
اعتراض‌های چهارشنبه ۱۷ دی:@
VahidOnline
#بیمارستان_الغدیر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/75554" target="_blank">📅 17:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75553">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Akbarpour🔥نیما</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1-0F-Kot4HXLv_kWTLriRRFtcUEAVX8z5VO5jtNTMBXw7eyJ5n1oncIxJWWelh_lNdJkPsAo8fU4K4Fj0HJmLwc_oC2MjSSHRQ6fJZZj5FyGmO6Y-cV7cQx0GXG8XQP_U27uCZmKg5Lh4GCtIfw7BL32OBIqG-ecDtVEt8UBCfNqi-EiBjpcjBHBT8q1UXbo0dReQT4lCD2-zo6bw-mFPCZcx41tOBT9iTFEExw6Wi9yp_1GV5P5tvuK8KNSJoLi-y7NE9lN1X1n48BdVPPSNoLuw_1GaummpdlvTIA2mLWYPizIhykyDagN5I-3PSQ0CZzj_8tzL0b2OvfguvX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرش زاد
:
آمار نشون می‌ده در سه ماه گذشته یک پاکسازی طبقاتی دیجیتال در ایران رخ داده. در این مدت سهم اندروید از ترافیک اینترنت ۲۵٪ افت و آیفون ۱۸۰٪ رشد داشته. این به معنی خروج میلیون‌ها کاربر طبقه متوسط و پایین از فضای آنلاینه. اونی که آیفون داره از پس هزینه کانفیگ یا اینترنت پرو برمیاد، اونی که نداره، اونقدر دغدغه مالی مختلف داره که عطای اینترنت رو به لقاش می‌بخشه.</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/75553" target="_blank">📅 17:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75552">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaZJ2dPvE2ezD3P5_cFTHc8zvcwX70aC9wMdcObUclsgOBh1eu852QnIPNDnARWZGN9amYZb0_7lYXlQV6Az_KkeyOzFbr6KRkgKBSQ32w8Vjz2BTdkVt7nx9CynhM33sa4MHE-5h3RVbc3Fsy2voUyQnRZkelZnww6Em3TO_PlJz4WBwKWtAaO0ACaEdAiT7M1DzyKFHQa5TuJ54PoktO1JH7J3EQ5-b9QPJbbyuuB9KWDl1AnR9YecsEKs_3I5W7oEGq7Arj8eZjqTQoNqhF222_YY7wW2VZ58ojM1nno4X10AArqJ1c7Gt_GO1Ss5CQO8hN3RF-KrNLNVkS10aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری دولتی ایرنا در گزارشی تصویری با عنوان «مهر مادری به عمر چهل روز»، داستان زنی را منتشر کرد که در جریان جنگ ۴۰ روزه، سرپرستی یک نوزاد رهاشده در بیمارستان را برعهده گرفته است.
در این گزارش، برای نخستین‌بار تصاویری از یک زن ایرانی بدون پوشش سر منتشر شد؛ موضوعی که بازتاب گسترده‌ای در افکار عمومی یافت.
با این حال، دقایقی پس از انتشار این گزارش، چهار تصویری که در آن زن بدون پوشش سر دیده می‌شد، از خروجی وب‌سایت ایرنا حذف شد.
@
VahidHeadline
+ بحث‌هایی دیگر:
twitter
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/75552" target="_blank">📅 17:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75550">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNgSrGxjEEMaXoL8BDfVBqiGUxS0y-T7XtU5kI6K4tnoGlPos8JAaGbg3T3MxwVebL8BYnarwmW8MaovGK0D6-Sj5Wp7GTDvC40cS7jHZE4tZ7svtGMFSnPHSZ2f4vJGci8WWxO_LzKUjOEhoDNWOyIX_8nm_4tiv-AqnjI_jkAZWMmLRKMmAnyrVZNlmitluOx7BdHYlwJ73-nzdaufA-i4KM61uQXp5yrrVCmimwB4tSn3XNcaGVXJI9I8UA5-PW036XT_l-1sfCuMsVvD2EUBKenUxs8dPazRCFzbTcyH5Q-6RZ4u7sgC5EXrJ-rkfPq3DuFUhnQVsbDlpQUOvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایووت کوپر، وزیر خارجه بریتانیا روز سه‌شنبه ۲۹ اردیبهشت هشدار داد که جهان دیگر نمی‌تواند بیش از این برای بازگشایی تنگه هرمز صبر کند  و ادامه بسته‌ماندن آن امنیت غذایی کشورهای آسیب‌پذیر را با بحران جدی‌تری روبه‌رو می‌کند.
وزارت خارجه بریتانیا روز سه‌شنبه اعلام کرد کوپر در کنفرانس جهانی مشارکت‌ها در لندن، با اشاره به پیامدهای بحران جنگ ایران بر انرژی، کود کشاورزی و قیمت مواد غذایی، خواستار فشار فوری بین‌المللی برای بازگشایی تنگه هرمز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/75550" target="_blank">📅 17:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75549">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2DEylq_fKCmrK8xvrhMiUqn8kCY8y3PL16dHvkEMaSc2_dMDW-iQnNS6hkvgHdbw7zCXNyj_G8BPavhIokdTeGEEJ4LaIvja51l5dLh_QPpljnYL3rS2-gf63xGg7k1P9Ea_FpVqlO3_QELLfS43wdJ-HsDGBbm_Pz0bUbsNuS8XDOs1G9YtHB-7a79jQVN_v_MMCQl8Zs1aP1O4510iX8e4ZhHijLEERa4Um4QFarn6R5bP71eHJ2O2WRIzQlaanUZBtRWENS_JZEo4ABmBTn9TqfpBot7L2sYJb92B2nyozq6weBxUv7COhvgCWzDZf0bHlWwA1SsV_UjxB_29g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه ایران می‌گوید تهران در پیشنهادهای اخیر خود به آمریکا برای پایان جنگ میان دو کشور، خواستار برخورداری از حق غنی‌سازی، خاتمه جنگ در تمام جبهه‌ها از جمله لبنان و خروج نیروهای آمریکایی از محیط پیرامونی ایران شده است.
کاظم غریب‌آبادی که روز سه‌شنبه ۲۹ اردیبهشت برای ارائه گزارشی در مورد روند مذاکرات میان تهران و واشینگتن، در کمیسیون امنیت ملی و سیاست خارجی مجلس حاضر شده بود، از دیگر شروط ایران را «رفع محاصرهٔ دریایی آمریکا، آزادسازی اموال و دارایی‌های ایران، تأمین خسارت‌های وارد شده در جنگ توسط ایالات متحده جهت بازسازی و خاتمه تمامی تحریم‌های یکجانبه و قطعنامه‌های شورای امنیت» اعلام کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/75549" target="_blank">📅 17:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75548">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4gcxjQ6LwoRJlhVFrIyip_SkzVBGt_YHrAr6UHDRvgs2zmCd5csI0M9HAsEpXv86dH3jp0qXqhQnJ8J3keZDvNm9ffEKNDw8VQPgaiR-tlN_ShAkW8aJe3Tn6IATecWCGYC01pILIQav54TqMrg8nDheK5jMxB38qtXbt0I07Y0XXWdqMnOCvHNaQvVyEgV0asPtFIu6B0YY_YJwBymz9hp4JCj1vfJNI2ELLTBtyINS9tZZdS7PQaySfrz0jx0zfh0UvC5HhHJC66voySvPMEUt2iAGRjc7zE_sSTwSbe6hD4FT7xKrSnv1IYpoK1ey4Qg_mPt2bspWp2UQlBQbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان «کمک به گروگان‌ها در سراسر جهان» دوشنبه شب اعلام کرد شهاب دلیلی، زندانی سیاسی و کاپیتان پیشین شرکت کشتی‌رانی ایران، پس از آزادی از زندان اوین از طریق ایروان به واشینگتن منتقل شده و به خانواده‌اش پیوسته است.
این سازمان اعلام کرد دلیلی پس از گذراندن بیش از یک دهه «بازداشت غیرقانونی» در ایران، اکنون در سلامت کامل قرار دارد.
شهاب دلیلی که ساکن آمریکا بود، سال ۱۳۹۵ خورشیدی برای مراسم خاکسپاری پدرش به تهران سفر کرده بود اما هنگام بازگشت توسط نیروهای امنیتی بازداشت شد.
خانواده او گفته بودند جمهوری اسلامی او را با اتهام‌هایی از جمله «جاسوسی» و «همکاری با دولت متخاصم» به ۱۰ سال حبس محکوم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/75548" target="_blank">📅 17:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75547">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOi-VzPLPEBH_6FDceRqTLO1q7S-QSY8rpFmip8qZ5EthtbQI6Hx2QKYRsQKTBzGUiAAiZC3HsB0b8AUZey4e-uD8yWN7JqsGjLJ8-vmkq6MNc41YNHDtHl0PVIrkQadlnUmVMg6pE2qq4ZBJ9E8vT-AmREhTSwTUsV_qsLN_TRark5jfb8hvtqH5GzUZC9-iEgfebj89rmEerMETlQmca0gzIVDhxjzakCXsp0RxEJPgEdWoW0lqyQr2-INlMIgC-HF7OVxE3KsV5wW4kcKCcuYZWsLvm9xsG757_OJs7Lgj4OSE-X6WC3jndXOwjcW7X-4ahQG5K7H-RRBs_b4og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامد تیزرویان، عکاس حیات‌وحش و فعال محیط زیست، در ساری بازداشت شده است.
به گفته زینب رحیمی، روزنامه‌نگار حوزه محیط زیست، آقای تیزرویان روز ۱۴ اردیبهشت ۱۴۰۵، بازداشت شده و موبایل و دیگر وسایل الکترونیکی او ضبط شده است.
اتهام مطرح‌شده علیه آقای تیزرویان «اجتماع و تبانی با هدف اقدام علیه امنیت ملی» عنوان شده است.
بازداشت او در پی انتشار مطالبی انتقادی درباره کشتار معترضان در دی‌ماه و همچنین اعتراض به اعدام‌ها در شبکه‌های اجتماعی صورت گرفته است.
آقای تیزرویان از عکاسان برجسته و سرشناس حیات وحش است و ثبت عکس‌های کمیاب از حیات وحش ایران از جمله خرس قهوه‌ای و مرال به عنوان گونه‌های‌ در معرض خطر انقراض، بخشی از کارنامه کاری این عکاس حیات وحش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/75547" target="_blank">📅 17:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75546">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FZ0fjX4T9Ld1cZsHe0gHrMJN2mgQH_lh8eWjBQXDNl_N13_EwBCJs45SaBoIbOu55pMh2fKzeRN4PuQxyjMpVqo-GDDZlUFQ7D2IhGf40WX7CDIznOM_8ApcVPvrhvyeSrggKOoQVF521h9FvbU6sDhsNb6alm4dm_VY4QLUOfZ29byAvGg51ownzhpExL_2nZo0X5RgVf9aLkRbAg9lZvYoVSErJySJmDQaIfMOaeWe-Vj4bkzfueAPYPibVYMK-guPSVJ7Nkf6CoG6tWUYWeVKhMzFGRbOaefbvuGC8w9-anXNFbcGbqLsu7qrJBbl7u7O9emgR3HWUQeOEncUjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر صدا و سیمای جمهوری اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/75546" target="_blank">📅 23:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75545">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v_278mFiSWnOB02Kv3zvi-pFVrf8ayyivPGisW8RrwxK2Hr3lExtKkjM1urx0f4hc679hppWaSGK1HF_Zs080Sz0RM48QbwoEPP4XtX0tRVjuGwtbKPo_jeX_qxDHZKXL5GuNS9wfR6r4QHM8OjEOPGJi39dd-LKkfmEcN-y95cwauRj6LocQE0BN1LF0ae97qq6jLunrSx7q04fMEovGbUDiv_IRtatpZilcgAZVy5rA6MFw-X_Ea7zeLIxpVhl6Y6l-4AJZvnHd63m1KanP4r3OYxDgxE2AlXOgkB8UPw0QUyIQT9WC_cvpd2wl8K4wnnWPnhFgItvXNc0PoWwKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: حمله فردا را به تعویق انداختم
پست ترامپ ترجمه ماشین:
از سوی امیر قطر تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی  محمد بن سلمان آل سعود و رئیس امارات متحده عربی محمد بن زاید آل نهیان، از من خواسته شده است حمله نظامی برنامه‌ریزی‌شده ما علیه جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازم؛
زیرا مذاکرات جدی اکنون در جریان است
و
به باور آن‌ها، به‌عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همچنین همه کشورهای خاورمیانه و فراتر از آن بسیار قابل قبول خواهد بود.
این توافق، نکته مهمی را در بر خواهد داشت: هیچ سلاح هسته‌ای برای ایران!
بر اساس احترامی که برای رهبران نام‌برده قائلم، به وزیر جنگ، پیت هگست، رئیس ستاد مشترک ارتش، ژنرال دانیل کین، و ارتش ایالات متحده دستور داده‌ام که حمله برنامه‌ریزی‌شده فردا به ایران را انجام ندهیم؛ اما همچنین به آن‌ها دستور داده‌ام که آماده باشند، در صورت حاصل نشدن یک توافق قابل قبول، در یک لحظه و بدون درنگ، حمله‌ای کامل و گسترده علیه ایران را آغاز کنند.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/75545" target="_blank">📅 22:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75544">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b-KDXvGUWDNokZKE4ElZokSxaKrziI3J03Ow_39y_qvpfu9Fqy2X-FR7eB0LLnHV5lypGHYnT0TE2ZmI5D9UQ-O_ZRlbVRgR9_nU-MhOjOfdKd4JsKx3TuD6tuLz9OaWy2C7V0mI1NufANo67Tbn__NM3W0rVcDlwqQP4J3IOv_7zFG0RLSwPK3kXO_wFY52ZoILeRJm8hp8nGG8UAXS0b4ycVQSfi2IEBc3Kt-rKOozUQ7fnyUiwxktjemP3ocxCCNQMyZS6tOQclQBYt3RmdfABX0mKcw7W-5ZRXeOVOmmDeyDgS43NORnGFo-1hpACEo8G-jg2IU_6P8GkLQLgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا، روز دوشنبه در گفتگو با نیویورک پست اعلام کرد که پس از دریافت آخرین پاسخ ناامیدکننده تهران در مذاکرات توافق صلح، «به هیچ وجه حاضر به دادن امتیاز» به ایران نیست.
ترامپ در مصاحبه تلفنی کوتاه، ضمن ابراز نارضایتی از آخرین پیشنهاد تهران گفت ایران می‌داند «به‌زودی چه اتفاقی خواهد افتاد».
به گزارش نیویورک پست، وقتی از ترامپ درباره اظهارنظر روز جمعه‌اش مبنی بر اینکه مایل به پذیرش تعلیق ۲۰ ساله غنی‌سازی اورانیوم ایران است سوال شد، جواب داد: «در حال حاضر به هیچ وجه آماده دادن امتیاز نیستم».
ترامپ ادامه داد: «من واقعا نمی‌توانم در این مورد با شما صحبت کنم. چیزهای بسیار زیادی در حال رخ دادن است».
رئیس جمهوری آمریکا همچنین گفت از تهران «ناامید یا کلافه» نشده، اما هم‌زمان تأکید کرد ایران به‌خوبی آگاه است که ایالات متحده می‌تواند فشار بیشتری وارد کند.
ترامپ گفت: «می‌توانم به شما بگویم آن‌ها بیش از هر زمان دیگری خواستار توافق هستند، زیرا آن‌ها می‌دانند ما...به‌زودی چه اتفاقی قرار است بیفتد».
وقتی درباره ادعاهای منابع منطقه‌ای مبنی بر اینکه ایران تلاش می‌کند در قبال هر دو مسئله هسته‌ای و بازگشایی تنگه هرمز در برابر واشنگتن «سیاست صبر و انتظار» پیش بگیرد، سوال شد، ترامپ گفت «چنین چیزی نشنیده است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/75544" target="_blank">📅 21:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75543">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iXKFQQ-42MnlSndql5VR8Tm3cZ7XwTM-xPbyB2x1Oiqbu4uYdoosgVwcIYzk0i--_Jv4HTkh60wKdyyDO1J56-oNzRHdzKPhukjDxbbdum7zJf1DK-CophRdnzqOJrn0DZMM1HoVx6y3oL_YAVPP_ckG9LOogOpht0dsNdtWId22Edv2dse0TbDwGjuaN2tdo13-E31Xuq2vkMuRfJJ45mJB5JdeCetwrwZKqRu2WwJ3PkHIw-p-eKT0RdRCeEpRaozVOUizzucdBj8qfjgyQMeFDFF98HuT70tHfQgkqnt2i3cFU27ynwXrYQ2N117yOCTqBE-KulqUX6bYvFnvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، دوشنبه گفت که آمریکا در حال صدور یک مجوز عمومی ۳۰ روزه برای فراهم کردن دسترسی موقت به آن بخش از نفت روسیه‌ است که در دریا سرگردان مانده است.
بسنت در شبکه ایکس نوشت: «این تمدید، انعطاف‌پذیری بیشتری فراهم خواهد کرد و ما با این کشورها همکاری خواهیم کرد تا در صورت نیاز، مجوزهای مشخص صادر کنیم.»
او افزود: «این مجوز عمومی به ثبات بازار فیزیکی نفت خام کمک خواهد کرد و اطمینان می‌دهد که نفت به آسیب‌پذیرترین کشورهای از نظر انرژی برسد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75543" target="_blank">📅 21:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75541">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v00b6dG449brKHdCi2HyCz5kfhTjQ7x8GyUQkMveg9CYOlVlOhNTceZAoZA5yVXvF_kEWztk6I1h0bM1m-go2uwJwTcTtnuYqAlkCPsUAv3JuL3jVG2zf3iXQktv1XXQEy7NZqENZ6GQFAyrQEpaP2nLGuDdpJcY1szUei18GpAZGkKkX1KjVqqWdgHce9vjJkpXhtaYn0E5bH8d1QNbyd-yZrvFKtyNeTjKsoFeGLJDZiW1BP-Wmn1KGOmZorURgE66wWkgIbw7cwRlLMptNyzlSQsD_G5tdk-fmGIZGc_lIiEl6vmURepxBnD7rtLwf7u7FAPLEkK3B7GPOJaDNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FqOPaI-amKodsRkCzEpy6aNjZtalrv9b8Qtrcx5LXvBw_fINNuoMComZKfjAwTmzOK3sm87Yt9L3fhnvBJfkezKZBmHs9OcIpnQxXgXaKDOVxgF5yXFkMmuO8IySY2oSugw6yIZuLeu9qoh2fZsIKTSqjDTCt7Mfa7VqBsLwISCFfRMhMLg2PaF5kmzQJvjKnMfjcqdTp_gpbakEkmp9z959QYLYfXFgLA7eGUFCEE3rSzOu9Z4P17MXeKyRM5_hpd0LTdaRSdMykRQ2Qq21pJtAJXrWEy9zcguFWPjofBN55Ha7Kcz8HR5vk2LKCJfqibyJAWohZ0Nxy3eYQVLRHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وب‌سایت اکسیوس، روز دوشنبه ۲۸ اردیبهشت ۱۴۰۵ به نقل از یک مقام ارشد آمریکایی و یک منبع آگاه گزارش داد که تهران پیشنهاد تازه‌ای برای توافق ارایه کرده، اما کاخ سفید آن را «پیشرفت معنادار» ندانسته و برای دستیابی به توافق کافی نمی‌داند.
به گفته مقام ارشد آمریکایی، اگر ایران موضع خود را تغییر ندهد، مذاکرات «از طریق بمب‌ها» ادامه خواهد یافت.
بر اساس  گزارش اکسیوس، مقام‌های آمریکایی می‌گویند دونالد ترامپ خواهان دستیابی به توافقی برای پایان جنگ است، اما هم‌زمان به دلیل رد بسیاری از خواسته‌های واشنگتن از سوی ایران و خودداری تهران از ارایه امتیازهای قابل‌توجه در برنامه هسته‌ای، گزینه ازسرگیری حملات را نیز بررسی می‌کند.
دو مقام آمریکایی گفته‌اند ترامپ قرار است روز سه‌شنبه نشست تیم ارشد امنیت ملی خود را در اتاق وضعیت کاخ سفید برگزار کند تا گزینه‌های نظامی را بررسی کند.
آکسیوس گزارش داده پیشنهاد تازه ایران که شامگاه یک‌شنبه از طریق میانجی‌گران پاکستانی به آمریکا منتقل شده، تنها تغییرات محدودی نسبت به نسخه قبلی دارد.
بر اساس این گزارش، در پیشنهاد جدید، توضیحات بیشتری درباره تعهد ایران به نساختن سلاح هسته‌ای آمده، اما هیچ تعهد مشخصی درباره توقف غنی‌سازی اورانیوم یا تحویل ذخایر اورانیوم با غنای بالا ارایه نشده است.
در حالی که رسانه‌های دولتی ایران گزارش داده بودند آمریکا در جریان مذاکرات با لغو برخی تحریم‌های نفتی موافقت کرده، مقام آمریکایی به آکسیوس گفته است هیچ کاهش تحریمی «رایگان» و بدون اقدام متقابل از سوی ایران انجام نخواهد شد.
این مقام آمریکایی همچنین گفته است: «ما واقعا پیشرفت زیادی نداشته‌ایم. اکنون در نقطه بسیار حساسی قرار داریم و فشار بر ایران است تا به شکل درستی پاسخ دهد.»
او افزوده است: «زمان آن رسیده که ایرانی‌ها امتیاز واقعی بدهند. ما به گفت‌وگوهای جدی، دقیق و جزیی درباره برنامه هسته‌ای نیاز داریم. اگر این اتفاق رخ ندهد، گفت‌وگو از طریق بمب‌ها انجام خواهد شد و این مایه تاسف است.»
در ادامه این گزارش آمده است که ایران و آمریکا هنوز مذاکرات مستقیم درباره جزییات توافق ندارند و گفت‌وگوها به‌صورت غیرمستقیم برای رسیدن به چارچوبی مشترک ادامه دارد.
این مقام آمریکایی مدعی شده که ارایه پیشنهاد تازه از سوی ایران، با وجود تغییرات اندک، نشان می‌دهد تهران نگران اقدام نظامی بیشتر آمریکا است.
در مقابل، مقام‌های ایرانی همواره تاکید کرده‌اند که این ترامپ است که برای دستیابی به توافق عجله دارد و زمان به سود ایران پیش می‌رود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/75541" target="_blank">📅 20:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75540">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SSxOIgFAa5K46QjRGrH3OdtytydfLb1WSVVzt3JEYVANfQoZYx6Y0mxkhN_I3g92fUohQvuVfX8YQ_CcDDBmQS6o9CWSsVRHdVuBFT59UQxI0UXLAOwqicrYGYxWEgXHiUn1cJsN8LcrU2UqHSINmYLkgdU0IwlJ8PWBNLf1lPjCyhwcPRBMJn2z65nhs4zoKPqBDlfrBpeUV_m6QqkNMc5Bkc1ECjzHIrSBC4lj2uRzvZYxd2K1SulCvqJACUQ6iL1OOpfRsOfOQDtA3zwVo9OT5l1lhAvijH2EPAizgiVjjh9VtOxI4VUF-s15Yt7h6M3c6ONcTPHuX4fxEeFGFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در قعر دریا آرمیده است، و نیروی هوایی‌اش دیگر در میان ما نیست، و اگر تمام ارتشش از تهران خارج شود، سلاح‌ها را زمین بیندازد و دست‌ها را بالا بگیرد، هرکدام فریاد بزنند «تسلیمم، تسلیمم» و در حالی‌ که پرچم سفیدِ نمادین را دیوانه‌وار تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌اش همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده باشکوه آمریکا بپذیرند، نیویورک تایمزِ رو به افول، چاینا استریت ژورنال (وال‌استریت ژورنال!)، سی‌ان‌انِ فاسد و اکنون بی‌اهمیت، و همه دیگر اعضای رسانه‌های اخبار جعلی، تیتر خواهند زد که ایران پیروزی‌ای استادانه و درخشان بر ایالات متحده آمریکا به دست آورد و حتی رقابت نزدیکی هم نبود.
دموکرات‌های احمق و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آن‌ها کاملاً دیوانه شده‌اند!!!
پرزیدنت دونالد جی ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/75540" target="_blank">📅 20:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75539">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEAPdKkU4QC68Sq2b1rcufnA0CQnTC0Ja-VqOx8gM48aIT8urFnlrZjfh5oo83a9QTAEHmHB1T8-vMD6Fmx3E-TG4Odfr7GBipq9dY1YDF_NFPTAcakREG2H_DOrLIsiM9jsauoWBZQrUAYtJRJOgpz7SZFbIUkyypQV928hfhMWPfyiH85W-N8wn4uSFTjBn9-qZWX1S3y6KP9CjcSluAZxlfFUmbiG0xyUaxnkR7mfn7YmAE6-SgYZEnyFkbCO0nZ1VwwlrHIP2_qQbara10qu-9QQvYzl5AKZql1jGBqn2M3n3UBBQ8I7TubXJQbNLnbR6HmtMwNWvZ2BzMcqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیر مرکز روابط عمومی وزارت بهداشت جمهوری اسلامی، روز دوشنبه ۲۸ اردیبهشت مدعی شد که در حمله اسراییل به بیت خامنه‌ای «اتفاق خاصی» برای مجتبی خامنه‌ای نیفتاده و زخم‌های او نه چهره‌اش را مخدوش کرده و نه به قطع عضو انجامیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/75539" target="_blank">📅 19:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75538">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcTS1URjQzrIzGZaIE9hFqBw503y8THE53qtI8YcfwQBSWKc3qcfLhZQ16wnkET2ciqrKqcHEtNZWab5zuiq5kARjoV-bh8ixQE5qfCRXUMXgnnbsg7YAtaL3ED690StB2kY5nTQBhwqRUB8JbCEsS6a6MUUHBSUMGx9RQbHXh-YFX70loz1FagdVJEiabafr7wNIXLDl-Aj9HYveIjOr9j7AkHVYju1a0RhaBRbid0LlZrMBtiJ1_XWdDGzfzDpTErCck0FWooKQhwbyRuEonhUobu5Qh2XyUjiM2Ma6AJX6mIYyuB9-avXh1e-F1HMYONZdjFnEEAM5aBBMyz-JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردریش مرتس گفت که «ما حملات هوایی تازه ایران به امارات و دیگر شرکا را به‌شدت محکوم می‌کنیم.»
صدر‌اعظم آلمان در شبکه اجتماعی ایکس، حمله به «تاسیسات هسته‌ای» را تهدیدی برای ایمنی مردم سراسر منطقه خواند.
امارات متحده دیروز گفت که در حمله پهپادی، ژانراتور برق بیرون محوطه نیروگاه هسته‌ای براکه در نزدیکی ابوظبی آتش گرفته است. امارات در بیانیه‌هایش نامی از کشوری نبرد و فقط گفت پهپاد از «مرز غربی» وارد شده بود.
آقای مرتس در این پست نوشت که «ایران باید وارد مذاکره جدی با آمریکا شود، از تهدید همسایگان خود دست بردارد و تنگه هرمز را بدون هیچ محدودیتی مجددا باز کند.»
اظهارات آقای مرتس درباره مذاکرات ایران و آمریکا اخیرا به تنش لفظی او با دونالد ترامپ منجر شد. او گفته بود مذاکره‌کنندگان ایران آمریکا را «تحقیر» کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/75538" target="_blank">📅 17:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75536">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J08kowP9jQBb5vfEwVYv0uO7s8AeOq4yhw73RVyD7ggANNz0cShqRN5rAzUobdzPQzOFkMVNCofiQkiNW4Pp9oVQD_5VPpo_B4ZV5rpU0ZyYNlslhaUDE137S9-Isx-OFhuakIW9m3jqgyrbUFyALhErt7J7dQ_MeSUg7G8JrOEvxxPGVBM6NcOrOPMERlfCei5E7mkJ9crqdvmMp7FX9R8KSujJmiAOGWAm0z9nbv57BnTl6pQXIIP0mL0FEC2q_MheYCGbkesm8Ad6Pp-hYNYNK3ftJqZxvdq20KplvP0WWNzbv1brg-95LqX0ZyYq0A1xql6KDVOIHTXJZ7o5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SUr_ZgcTFrAgqZgq3XMqKeT11I8l7PgiiYWeWFs9xAO91W4AfdyoUAR9dp-V9pttpTwkpGeyr8GPhLcXIG9mu-SzCcc1CoxtSryI3oGPVK1NhzXIRNUVxSZpp6YTSA5NkO-FG6BqGmbdfpIFrISJaJ47rn9CzfDFUFXxNi1t8CD44ey4Q54XUGpBQje5885GxxHcsU10J-GCW8sKrwb_nspO7LuoIyTCAEnhvSJ8Z2VzETVgGO2_RR-9UAFj1JyB-T9_LvXpNfoqbDsBS0ZQBBUOfASyRj7peBj6zCSJ4QdCESaY_iMUbI71hi2fHkmDJnCj_p5Mvvypsd3sNqJLaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، روز دوشنبه ۲۸ اردیبهشت ماه به نقل از «یک منبع نزدیک به تیم مذاکره‌کننده» جمهوری اسلامی نوشت که تهران «جدیدترین متن خود را در ۱۴ بند به واسطه پاکستانی تحویل داده است و میانجی پاکستانی آن را به آمریکایی‌ها ارائه می‌کند.»
ساعتی پیش از انتشار این خبر رویترز به نقل از یک مقام پاکستانی گزارش کرده بود که اسلام‌آباد یکشنبه شب طرح پیشنهادی اصلاح‌شده جمهوری اسلامی ایران را به واشنگتن تحویل داده است.
@
VahidOOnLine
خبرگزاری العربیه، روز دوشنبه ۲۸ اردیبهشت ماه، بر اساس «جزئیات درزکرده» از آخرین نسخه پیشنهادی ایران به آمریکا، از مجموعه‌ای از خواسته‌ها و پیشنهادهای تازه تهران که بر آتش‌بس، تنگه هرمز و پرونده هسته‌ای تمرکز دارد، خبر داد.
طبق این گزارش، ایران خواستار یک آتش‌بس طولانی‌مدت و چندمرحله‌ای شده و همچنین درخواست کرده بازگشایی تنگه هرمز به‌صورت تدریجی و با تضمین‌های امنیتی انجام شود.
بر پایه این اطلاعات، تهران به‌جای برچیدن کامل برنامه هسته‌ای، با یک توقف طولانی‌مدت فعالیت‌های هسته‌ای موافقت کرده است. همچنین پیشنهاد شده انتقال ذخایر اورانیوم غنی‌شده به‌جای آمریکا، به‌صورت مشروط به روسیه انجام شود.
العربیه همچنین گزارش داده ایران از مطالبه دریافت غرامت عقب‌نشینی کرده، اما به‌جای آن خواستار تسهیلات و امتیازات اقتصادی شده است.
بر اساس این گزارش، ایران همچنین خواهان دریافت چندین تضمین بین‌المللی برای هرگونه توافق احتمالی است و تلاش دارد پرونده دریایی و موضوع تنگه هرمز را از پیچیدگی‌های مربوط به مذاکرات هسته‌ای جدا کند.
در بخش دیگری از این گزارش آمده است تهران خواستار نقش‌آفرینی پاکستان و عمان در مدیریت هرگونه تنش یا اصطکاک احتمالی در تنگه هرمز شده و همچنین بر استفاده از ادبیات و چارچوب سیاسی‌ای تاکید دارد که امکان «حفظ وجهه سیاسی جمهوری اسلامی» را فراهم کند
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/75536" target="_blank">📅 17:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75535">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYDXrT71ND15mlt_zb7HJQbTRQi0v_hoaxGh9Ifq2g1ytGsjxG61thgHi-H-AIueOF-v_7z1bkXGBfhnzHgpSMwrj35KqagK73ICxUiOYi2QeLZ-kgCSEBhx7shf5jfBtyhjNP9dyQlO1B-Re7nTupmxMWzhCCw9fwjbf5VJQkMQaSMsmveDYXxq9X1hPHkzDFtIfI5mhIc3BBQE3yjf3oVUaz9Sl-XKstgy0L0Po1RcCgohRZcXC0qqxScJsLyqTLc3qz-9V_fvEbaJYnJOJvsnKgcjxlKTq5p2TgFON_fIpyx1O5E1Kp3YSd7GtbwWfnf1oZ2DdZoaxuyFJF9XwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرگزاری تسنیم وابسته به سپاه پاسداران، روز دوشنبه ۲۸ اردیبهشت، به نقل از یک منبع نزدیک به تیم مذاکره‌کننده گزارش داد آمریکا در متن جدید پیشنهادی خود، برخلاف متون پیشین، پذیرفته است تحریم‌های نفتی ایران را «در طول دوره مذاکرات» به‌طور موقت تعلیق کند.
به گفته این منبع، آمریکایی‌ها در متن جدید با «تعلیق موقت» (Waive) تحریم‌های نفتی ایران موافقت کرده‌اند. «ویو» به معنای معافیت یا چشم‌پوشی موقت از اجرای تحریم‌ها است و به معنای لغو کامل و دائمی آن‌ها محسوب نمی‌شود.
بر اساس این گزارش، تیم مذاکره‌کننده ایرانی همچنان بر این موضع تاکید دارد که لغو همه تحریم‌های ایران باید بخشی از تعهدات آمریکا باشد. در مقابل، واشنگتن پیشنهاد داده است معافیت‌های مرتبط با اوفک (دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا) تنها تا زمان دستیابی به تفاهم نهایی اعمال شود.
به گزارش تسنیم، این تغییر در متن جدید آمریکا نسبت به پیشنهادهای قبلی، تحول تازه‌ای در روند مذاکرات به شمار می‌رود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/75535" target="_blank">📅 17:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75534">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNPmdIm93gUX7OlOzbelhaR2QyZMj-dq1pqUmfnT_emqKox09-fmKdm7K98Xzi3zB9jgxYqotVgMCjcD3yw04Y5isqaf6I_7CtEltosq7mIeW2_fblj-QWiqhGa5bOu3YwtqKDhQJcPFX8s4wQVnDkdLPtuA40bNPXNoqSfqROkvcT2n5j6t2ndTu-AcxAYTwxgcswhcUPYx_czf_QrIsKtZD3rnLp8G963gHHjL6i_4omllVW872ZXnDCBXcKh1_czwWugbBAxELGI5GWIr6QlWS4UgCuOL_FzbaEdEyhycM0PGQu_1_z5ErXnaYAEU1RjmYhV_KnR_ZqRaxDDc1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از منابع آگاه گزارش داد پاکستان در چارچوب پیمان دفاعی خود با عربستان سعودی، ۸ هزار نیروی نظامی به همراه یک اسکادران جنگنده و سامانه پدافند هوایی به این کشور اعزام کرده است.
به گزارش رویترز، این نیروها از توان عملیاتی برخوردارند و با هدف حمایت از عربستان سعودی در صورت ازسرگیری حملات علیه این کشور مستقر شده‌اند.
این تحرک نظامی در حالی صورت می‌گیرد که پاکستان نقش اصلی میانجی‌گری میان تهران و واشینگتن را بر عهده دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/VahidOnline/75534" target="_blank">📅 17:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75533">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL_p6IFnvrWXFp3TrDdlL1VLcfP3Ox-RwfoehWywLsXV6J5s0RSJL2-0Ba7WzbmuuDpwgaOJnZhviF7ojPE0b91x8i1Y4dbsAjsJfzxZ1jNjP6z4PsCWlUro0Nd62d9xFo-blZUfuarYxGTls6lHcgl4fhM0j5cdpV8G4U6J3bAxtVDPpNsdYkMbOXd-qimgzMQwUW6vKobsisUJkyF365yza2DQ0k-M8ig-slcoe_YJGKkXzhxTpjhbIZRBPIJw4RbvKpqfbpE_0M8UzO831c3s_pvESDvrvL3Kpvymjr4_s8VXwBIgBwkJmyxkljYSh8E2rK3N867kpK4slPiQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس کل دادگستری آذربایجان غربی روز دوشنبه ۲۸ اردیبهشت از توقیف اموال ۱۲۹ نفر در این استان با اتهامات امنیتی خبر داد.
ناصر عتباتی از این افراد با عنوان «گروهک‌های ضدانقلاب و تجزیه‌طلب» نام برد و آن‌ها را به «اقدامات ضدامنیتی و همکاری با کشورهای متخاصم» متهم و اعلام کرد که اموال آن‌ها به «نفع ملت» مصادره شده است.
دادگستری آذربایجان غربی اسامی این افراد را اعلام نکرده و برای اتهامات علیه این افراد شواهد و مدارکی ارائه نداده است.
پیش از این نیز گزارش‌های متعددی از توقیف اموال شماری از روزنامه‌نگاران، فعالان سیاسی و مدنی، هنرمندان، ورزشکاران و چهره‌های شناخته‌شده با اتهامات مشابه منتشر شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/75533" target="_blank">📅 17:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75532">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQsd1LkUUNE79r20BF8h5IeXUpsuI45HLtdn_6h5sLrQaM1XJI0n8bVIcML9NqnNHCbVauTFxtO2YSBfmNSkbKQoSVStTPVoPG_V06ko0xZ3YqXEzU2wmFUxMOxnvMlvoFwy3wH6T57eYPSDPgbQ4YLeomJuKnzPDv_cmg56j1RCmK5QZew59RTTEI9FkgyKFNxX5X79nw6IeBEDTWq9ZfrZMV2mpUiOnBQpkJyiANlYhaV7gMT2Eo7mJcz0iy-NUnRWczyzvD-JbIE0q8s9_BynL7sqYC2f3Eo_OTDXa1LUZ717prx3RRXXmd9Kr5XgEQ706Ey5nNPtl6eV7NGpnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا می‌گوید مقامات حکومت ایران برای امضای توافق با آمریکا «می‌میرند».
او در گفت‌و‌گو با نشریه تجاری «فورچون» افزوده با این حال آنها در جریان مذاکرات، «روی یک چیزی توافق می‌کنند»، اما «بعد یک کاغذی برایتان می‌فرستند که هیچ ارتباطی با توافقی که کرده‌اید ندارد. من می‌گویم: ‘شما دیوانه‌اید؟’»
ترامپ در این گفت‌و‌گو همچنین بر این نکته تأکید کرده که مقامات جمهوری اسلامی «مدام فریاد می‌زنند» و سروصدا می‌کنند، اما در عمل «تشنه توافق» هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/VahidOnline/75532" target="_blank">📅 17:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75530">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FXGUTFJEugwB3YeZ9G3zEo6uoXlI50s0xR90Ip6m8AOwr5TdPvhhYaE8XSX4bf98u2maNw7NJYoHG8TEvwOIQyu3UD1Qz5IvpW4Ex9Ot3AcYeojEwNAzK9sEAtXBr0mzY8ZNTpFZ7b3tA6web5UF1XJ9MhCQVJIfLr89A9wwTfpj7ZQ1wMq3z0cRaoHXhBcjOxnuA1akXQatbslRM5FMzvM0ZMqhUfa8GTGMH0gG6-03BCSWJ6kFcItOrM2E9tlEDrdK8P80_hxHc4m6mvwYaOm_DxPIYSAWkkfEWz9AIFsGtikS7GgtjDO3HOL0SF9hHpanFifWyfVsZ7H0igXv5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WqnuKW8yLXThqLDbk98AfsHEehFNoBcyrvZAoT4IaWBtrUmPfjZsIwy4ec8YrOqaJAQ5Rw3cSqKouI3ZDWn_i8wFk7XlFXjfK9pkzdOBz-ZxyIdzct6JxBSoxlry2d6gUxmT3jAwXDEDqU1dtPMiS_RpIeY150Kj0Gc_QeQk2-LGM3JUePO6IWc2Mol57wjnMEp1FklUH_myOeAorXyt5wA-J6KvW7MYh3cGSz1OFAIoEH8d2FNF7pzrtg7RlBsrfHprPM-hHI0PkoOwNoijv-JLBDkztdz3yNGyqxcck9-_k0t6lze3Xw6_iGCKAvJAY1EnKuJomqysvcMHAdp_yg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سخنگوی وزارت خارجه ایران می‌گوید روند مذاکرات تهران و واشینگتن، «ادامه‌دار» است و حکومت ایران از ایالات متحده، «اصلاحاتی» در پاسخ به طرح پیشنهادی خود دریافت کرده است.
اسماعیل بقائی در نشست خبری روز دوشنبه ۲۸ اردیبهشت گفت: هفته گذشته، علی‌رغم این‌که طرف‌های آمریکایی به‌صورت علنی اعلام کردند طرح پیشنهادی ایران مردود است «اما ما از طرف میانجی پاکستانی مجموعه نکات و ملاحظات اصلاحی را از نظر آن‌ها دریافت کردیم».
او افزود ایران بعد از این‌که طرح ۱۴ بندی خود را ارائه کرد، «طرف آمریکایی ملاحظاتش را مطرح کرد. متقابلاً ما نیز ملاحظات خود را مطرح کردیم. از روز بعد از ارسال نقطه‌نظر آمریکایی از طرف پاکستان، ما با مجموعه‌ای از پیشنهادات طرف مقابل مواجه شدیم که در این چند روز بررسی شد».
سخنگوی وزارت خارجه ایران به‌دلیل آنچه تبادل «نقطه‌نظرات متقابل» طرفین به یکدیگر نامیده، تأکید کرد که «بنابراین، روند [مذاکرات ]از طریق پاکستان ادامه دارد».
بقائی جزئیاتی در مورد اصلاحات مدنظر ایالات متحده ارائه نکرد.
@
VahidHeadline
او همچنین آمریکا را به «خیانت به دیپلماسی» متهم کرد و گفت واشینگتن دیگر «به‌عنوان یک طرف معتبر» در عرصه بین‌المللی تلقی نمی‌شود.
سخنگوی وزارت خارجه جمهوری اسلامی تاکید کرد تهران در مذاکرات با آمریکا همچنان خواهان آزادسازی دارایی‌های بلوکه‌شده ایران و دریافت غرامت جنگی است و این مطالبات را «حق ایران» توصیف کرد.
بقایی همچنین درباره تردد کشتی‌ها در تنگه هرمز گفت موضوع ترتیبات جدید امنیتی در این آبراه صرفا «مالی» نیست و هدف اصلی، حفظ امنیت تردد دریایی و صیانت از «حاکمیت ملی ایران» است.
او همچنین در واکنش به گزارش حمله به یک کشتی کره جنوبی در تنگه هرمز، بدون اشاره مستقیم به عامل حمله گفت «نباید عملیات‌های پرچم دروغین را دست‌کم گرفت» و مدعی شد هنوز مشخص نیست این حادثه توسط چه بازیگری در منطقه انجام شده است.
@
VahidHeadline
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی، در پاسخ به پرسشی درباره گزارش‌ها از قصد امارات متحده عربی برای حمله به جمهوری اسلامی و سفر مقام‌های اسرائیلی به این کشور گفت: «ما قرار نیست با گزارش‌ها این واقعیت را از یاد ببریم که تهدید اصلی کدام طرف است.»
بقایی با تهدید کشورهای منطقه از جمله امارات متحده عربی گفت: « اماراتی‌ها از اتفاقاتی که در دو سه ماه اخیر افتاد باید درس بگیرند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/VahidOnline/75530" target="_blank">📅 17:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75529">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPHhYoVXmU8xxTpA4tZrRAKWITPKRebmp8RRJ3siqskl9wymVQAQlgvleJlLVms3iOzJZYFy129Wclc2rlIbxJLgKIC_C7IGNGQboeJV2jRfr5K5JbiRjSICebLo8CixN_vdr_Wx-XPHBezQH9IMowQbkn1DZ-iwCTJCJiYTnqUlq9IAIFt-Y8WTiygdmqk0gRtSG8XHdx-VazI3Jok1nqbn8hqVsXFUtKbPL32j45AV3DFdMX2PeVQsMxCKTkmvmzpFEOMh-2edkXzUgNfBkFYU1q3Oa2Bez27djO2FGVRKSBcvWWxqggfI3yOOzj3tQSv_59fHGytksKe7SoQ1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نت‌بلاکس» نهاد ناظر بر آزادی اینترنت اعلام کرد قطعی و محدودیت اینترنت در ایران وارد هشتادمین روز خود شده و مدت این خاموشی تاکنون از ۱۸۹۶ ساعت عبور کرده است.
نت‌بلاکس همچنین گزارش داده که هم‌زمان با ادامه محدودیت‌های اینترنتی، محتواهایی در حمایت از حکومت، شبکه‌های اجتماعی در ایران را پر کرده است.
بر اساس این گزارش، برخی شهروندان ایرانی که تلاش کرده‌اند به اینترنت موسوم به «سیم کارت سفید» یا اینترنت ویژه (اینترنت پرو) دسترسی پیدا کنند، گفته‌اند از آن‌ها خواسته شده سهمیه مشخصی از پست‌های تبلیغاتی روزانه در حمایت از حکومت را در صفحات اجتماعی خود منتشر کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/VahidOnline/75529" target="_blank">📅 17:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75528">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rhlvdTdMOKALJJbn4CQnM5898ZBuXY-x4LbtmNY32J11iczoNJjOCnL5APW5C6sm50vd3iEksrGaxLbHNy8zjK05bcPghOqxEU7O3EbkXCKKENIw-OnhEMc1lmIZba-We9FO_dFuN9qztmrn3z9IelBUhxjkGzX9k23DSauzmZ_hzV7kdLwj4SW_sCj_Ft60tLX2V-lcpcYlBl0oFgdR5Az2RS_9Ali76gTmK23D01yOw_amb23zi-_nOMCA0aYVeLDVAAnX9-7TQSzcNzINzcw_n6dOQifLg_E0cqFomDpYoAy7KQzDTfkog3Xatb47_UuVmWiaaBSUdjcl0HPX_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عفو بین‌الملل روز دوشنبه ۲۸ اردیبهشت گزارش داد که ایران در سال ۲۰۲۵ تعداد «بی‌سابقه» دو هزار و ۱۵۹ نفر را اعدام کرده است؛ رقمی که باعث افزایش آمار جهانی تا بالاترین سطح از سال ۱۹۸۱ به این سو شده است.
این سازمان مستقر در لندن اعلام کرد که در سال ۲۰۲۵ دست‌کم دو هزار و ۷۰۷ نفر در سراسر جهان اعدام شده‌اند، هرچند اعدام‌های انجام‌شده در چین در این آمار لحاظ نشده است.
عفو بین‌الملل گفت «هزاران اعدام» در چین، که بیشترین استفاده را از مجازات اعدام در جهان دارد، انجام شده، اما جزئیات به‌دلیل «محرمانه بودن داده‌های دولتی» در این کشور کمونیستی نامشخص است.
این سازمان افزود که آمار جهانی سال ۲۰۲۵، شامل اعدام‌ها در عربستان سعودی، کویت، مصر، یمن، سنگاپور و ایالات متحده، نسبت به مجموع سال ۲۰۲۴ بیش از دو سوم افزایش داشته است.
در این گزارش آمده است: «این روند بیشترین شدت را در کشورهایی داشته که مقامات در آن‌ها با محدود کردن فضای مدنی، خاموش کردن صداهای مخالف و بی‌اعتنایی به حمایت‌های مقرر در قوانین و استانداردهای بین‌المللی حقوق بشر، کنترل خود بر قدرت را تشدید کرده‌اند».
به نوشته عفو بین‌الملل، «افزایش بی‌سابقه اعدام‌های ثبت‌شده در ایران» در حالی رخ داده که مقام‌های جمهوری اسلامی، به‌ویژه پس از جنگ ۱۲ روزه تابستان پارسال با اسرائیل، «استفاده از مجازات اعدام را به‌عنوان ابزاری برای سرکوب و کنترل سیاسی تشدید کرده‌اند».
عفو بین‌الملل و دیگر گروه‌های حقوق بشری گفته‌اند که پس از اعتراضات گسترده ضدحکومتی در دی‌ماه پارسال و همچنین پس از آغاز جنگ با اسرائیل و ایالات متحده در اسفندماه، استفاده از مجازات اعدام در ایران افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/75528" target="_blank">📅 17:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75527">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzmSw141ladyEIUglSLO4bieFdkI_V8z7vJFXaCW57wh1NID0uddw1E9CU9srFX8BLM3i-yeFp8ac4s2nioJRKCqeiSrz49bVlB1CvqXX1ocWSa2G5BYZeu6xY56dGsJquo81JPH2HEd1ZxreSuFEr45D06K_CzXbkt-FJN-bcKhH1ECSZ4NjnmJzl7JERdLZIW6zt5-k6PtZv5u6RUknVIfynOIZMHAtRb3h6GPRQDovW3O0yDBBYxpaWxbG2exZ11gI38i4xRvrE6WSVe6nrL07BszUKe86pDzLOIK4SwT31NR5li51kMqte7uw3dE2PZ-JDMS0LifIpNBlh-W3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی افزایش تنش‌های ژئوپولیتیک در خلیج فارس و نگرانی از تداوم فشارهای تورمی، قیمت نفت در بازار جهانی انرژی افزایش یافت.
قیمت نفت برنت در روز دوشنبه ۲۸ اردیبهشت با رشد ۱.۲ درصدی به بیش از ۱۱۱ دلار در هر بشکه رسید و نفت خام وست تکزاس اینترمدیت آمریکا نیز با افزایش یک درصدی بیش از ۱۰۸ دلار معامله شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/75527" target="_blank">📅 08:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75526">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ryFYJgiekc61vk13VkGFaEeFXkX-jJn9GONtsZxq9UmS7Fudo5Is1b24byodpokt-_uGvJbC1NqVWDW8zsY-AByGYXagPjH3K-nyUY9bbxFeVfWY_b4AKtmbvEsDm0NjS_fDUXNvOgQuF5HNZ4aP9t22UXobVv-aFYTNv_P11sMLX66zeKZ0aQgtutKvHiUcqDiA4xsBcAahn4ifxNZaEsFcUfNa_QpLibu3WcbMAl_tHzF7UlbGzF3Lw2Yjqbb4AG32zJokac02mgRN1T_dBvbJuNdOzw7qebQ6P5h62Ss4iB4-iX82VWrsl4S6QYyeyAaWzDQCnxcGPNxWg9sZlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا در مصاحبه با ان‌بی‌سی در پاسخ به مجری که از او درباره بازگشت «پروژه آزادی» (هدایت امن کشتی‌ها از تنگه هرمز از سوی ارتش آمریکا) و از سرگیری کارزار نظامی پرسید گفت: «ما پروژه آزادی را به درخواست پاکستان متوقف کردیم.»
روبیو افزود: پاکستان به ما گفت اگر پروژه آزادی را متوقف کنید، ما فکر می‌کنیم که می‌توانیم به توافق برسیم.»
او گفت که ما پذیرفتیم و رئیس‌جمهور هم دیپلماسی را ترجیح می‌دهد.
با این حال روبیو گفت ما در حال خارج کردن ناوشکن‌ها از تنگه هرمز بودیم که دیدید رژیم ایران آنها را هدف قرار داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/75526" target="_blank">📅 08:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75524">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EDXkw7JgnOzwCOmvynxylMyYIT2bWjXm43f-bUIOtlEYumcct8su9R5xJzZEIauwfjbgP0o7oGOFfMEC7Iw3JNclW_ntuibf6UjFvTqMNegdogdOfIMyKop5dMJ6Bx6m-jUt0Nfwdlrx0LdhVOzknmmDevAkC7_e-vCsU83Owt_V_0dwnLgx8_YPjonhleqGSePbXJckkK4IPHS7mG5_fMfTV7Aey9eYDfaQ4ECPukyQzYDz_exC4r0VxhxcJNYWY-eXJCCWQqNhNTXIqTv2e-_e1SUxtyEUi8LzDMkSWVasGO3zRpEN4puWrBj_Fydg17NUlXi95hKOB3pyLZSHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ترامپ به فاصله چند دقیقه‌ چندین تصویر مرتبط با ایران را در تروث‌سوشال بازنشر کرد.
ترامپ همچنین یک تصویر جدید از پرچم آمریکا را منتشر کرد که در پس‌زمینه آن نقشه خاورمیانه به مرکزیت ایران قرار دارد و از همه کشورهای همسایه فِلِش‌هایی به سمت ایران نشان داده شده است.
او همچنین چند تصویر و پویانما را بازنشر کرد که ناوها و پهپادهای آمریکایی را در حال هدف قرار دادن پهپادها و قایق‌های تندرو جمهوری اسلامی نشان می‌دهد.
@
VahidOOnLine
طرحی که سه‌شنبه از قایق‌های جمهوری اسلامی
پست کرده
بود رو
دوباره
منتشر کرد. ساعتی پیش‌تر اون
انیمیشن دیروزی
رو هم
دوباره
پست کرده بود. تصویر ساختگی یا طرح گرافیکی دیگری هم
منتشر کرده
با عنوان اینکه نفتکش‌های خالی برای خرید نفت به آمریکا می‌آیند.
اون پستش
علیه اوباما و بایدن با طرح گرافیکی قایق‌هایی با پرچم جمهوری اسلامی در کف دریا رو هم دوباره
منتشر کرده
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/75524" target="_blank">📅 00:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75523">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ggv-bBDXCVqU2FqgGSqGpGC0pLr9jkI0EJjpdbZJv_R8_LNfwuEljzh-mosF2vnNJDIqv1bAuo4ev30cXwke29o9JcU722h42G3XuKFIit0YsdfNggF3poL-N9b-fuce3zFmsp9Mpz7C4T1DwG99sIknBXGvnafpurvK2RWaf9O5wDT-GHTtFCnl67Bt254_Dmqa1ZPF4NEnGnK-cwB7Sp77JW3c3IY3V4ZXW8Bt76bLRukPN5eapfBFzYOCnk1Y24pYlGboUjS2Ha-Rd0ORi0sdGAXzwcKNJJ_7RR5uvinBp_LQyUkTDKkZw2krypP1zhQfCPStpDEnoGSALVz0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکی المالکی، سخنگوی رسمی وزارت دفاع عربستان سعودی، یکشنبه ۲۷ اردیبهشت‌ماه اعلام کرد سه پهپاد پس از ورود به حریم هوایی این کشور از سمت حریم هوایی عراق رهگیری و منهدم شدند.
سرلشکر ترکی المالکی تاکید کرد وزارت دفاع عربستان سعودی حق پاسخ‌گویی را در زمان و مکان مناسب برای خود محفوظ می‌داند و تمامی اقدامات عملیاتی لازم را برای مقابله با هرگونه تلاش جهت نقض حاکمیت، امنیت و سلامت شهروندان و ساکنان این کشور انجام خواهد داد.
وزارت دفاع عربستان سعودی افزود این کشور برای مقابله با هرگونه تلاش جهت نقض حاکمیت و امنیت خود، اقدامات عملیاتی لازم را اتخاذ خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/75523" target="_blank">📅 00:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75522">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT8hBl-DnbF7SFt5SCgMQL7TShJXajfkRK-gFWb9aq6jdbA-Ge4mQiz8V4lNpmzMRtVZMVuDTDpbT_oGFbjlTOLZIjaOqYOGA5nfwWo-b0C7b5JeFaLtpyuFOZDgQer-hpVLDVJbLVvBBFAALkcTufPN21W6_JGKB47uOB6uN2LS8ugoR9R5y50Mneu_W0usWT9yqQ3g2DmuJ08r588dKR8_AJbwvbwA4A7fVBljMVfwbsGKRtmqayUO1l9cKHn3IOw3YaOqjVIUg39h8L07en_XezAoFvw5882UW-mxOgAVBtvATeYu_aioNrB0sZMXAlqcwErH7gX-HZBKwykejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح روز یکشنبه ۲۷ اردیبهشت ۱۴۰۵ یک دستگاه اتوبوس در محور عسلویه به کنگان، پس از پلیس راه سیراف، واژگون شد و جان هشت نفر از کارکنان مجتمع گاز پارس جنوبی را گرفت. پانزده نفر دیگر نیز  در جریان این حادثه مجروح و به بیمارستان منتقل شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/75522" target="_blank">📅 22:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75521">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YbMrlzbKUMZcQJYNWZtCiKpbOH16GG5HvWwI2RAcwKDIUq-aB5Y9t_3LGSUpTNebmPxicf0zxUeae2uTe0JUjdstqegot-HNGzyDPpUD24_EGtzKJtvVaXlKTIV40qMfPO5Nks-rUJzMBNNZ5nxNdDRd5cbheWGdCVhDIX4ttkKxKdiJJk-5NWw2tQ37mhT5o8C5Rf-KSZ4GCe5q03PghY8NkKCd_CFEwS-7_ysnSAV0x_IH8MznpbCnFjbMM-vODghErUiVL_L1ngNqopDAEc1ewVDn9P_cz0317d1q41o033fEFwZQd_gSU8Bjz-5r_liXlXmWRETD2DCossxVng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
زمان برای ایران به‌سرعت در حال سپری شدن است و بهتر است هرچه زودتر اقدام کنند وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان حیاتی است.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75521" target="_blank">📅 20:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75520">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clYbbxECpRQQut-3tDCJoGQM8II5Y9CzXYSljdIJu8FtbHzdZ5POmFnkTj4Y8jFIEs58l_YJw30A6KFy9zF69_WOknCLY-34KsSmWXzDZY4C4wrFob-rOCRywP_xyC58QzY5fiv4nbiUa1tm6DfA8LcxF3cAZuL_Ypp-GWNOb1kW9HK0p11RTybonq5o4ZXtZNQagF7GDio3LVWBf7n8Rphw2IocXexNGj0gzlDR4rt9AiWWsNWkldy985Aj7k_DxpcWkmsPgfGdoQZjHBKWLdRaKBWsRKEbUpNDcTAsdgwPwPU7IEdFllqOQxrGxKxo-UqgO3KjoHJw-LzypynNLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دفتر بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد او روز یکشنبه و دقایقی پیش از برگزاری نشست امنیتی، در تماس تلفنی با دونالد ترامپ، درباره جنگ با ایران گفتگو کرده است.
به گزارش تایمز اسرائیل، این تماس در شرایطی که گزارش‌ها درباره آمادگی آمریکا و اسرائیل برای ازسرگیری جنگ با ایران منتشر شده است.
بر اساس گزارش رسانه‌های اسرائیلی، دو طرف در این تماس درباره احتمال ازسرگیری جنگ با ایران و همچنین سفر اخیر ترامپ به چین گفتگو کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/75520" target="_blank">📅 20:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75516">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LWrAub1qXW9sUVAj4rtCf6--TGQns3cqRLLyTft-pZPNau22hsfQLrc-MYR5XqqBUn1jUBy9-_yDF95X1piAn9Rhe3gz-NrIyNLUqtoglRCHN0MloLIOG25Tj5d3SUWjffLbaDBlBL8BxMKWdn_tPbyr1-slKqunp1YuWwduf0GrtMhEbmZdtz4fkbWPORp7uyQ5decGFQLKhlltqPetiYnSlatAbDRZjLKOwSuYlouw30MQ9Wwjo6Z1IDXd-JABHNKBtDJr63_XztNDJREeS8Ji0JdOqedbBAbV8ZBzxQ5KM---a3W7N83om-gxgteyz_4QXRJQUWddAnZhBDmkNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fC-pzolmWQzvg7Vz8GI-LhwRS9bJXjpAi_DH1_IeEILbUSqvpGDNTAbkuaNcLJYeUBCPU2DOBnzIt0XlcjXUARsN-wuSfHyqpb24vTJP7QlArJvULnk_cmaaH1Bptvdz0WEIhYRGgAf-H9Se864RigKB3aaPmeKCLEf3eawP20eeDcsBTldY9Xyw0HathvqpPVyg_WA9xLqXxlVcXFjQ11BEmDFk52-JiWjpF2pF-y9e4cYtZZme5aXGZ9nDgGcNiCugxlpuTRWiCpAwxsArFxl2QKQ6mxXPI-Rx1scd7U7-UEjlpaDAW9Gg6qUApM3aLOjLgpiCvqkK-3UTjca4bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qXvG0_0tLzF9toWgQ5uRZUmOol_ncnLkMVatCge6hO4WHRz2trToz_e6kUzbrpUN135n7k5H2IxbGAoEqdDPm2odmTXjS6d2TTx3pZ0pMJiXASWj7sgjaj2DhwqcE-Re4eIllUA5TFHSU3ewH8LwEtmT7wQN05PaDOLcFZrQeyNsXB5lCC7LlS6X_LvnWv3VzZbH7q3OLc07W9eoFfdHX_pTETtHmkCcTKbJiMXPKmWpR14brpkZYOiYGvu2S10bozbsmazW4FhIEJh0nfH6oSUqdIYgKD1zXiG5g3xb_Gpk_hmbBcSCvXW44gfQzBD3AKdyNACdBkAl1aAy1I2J4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fv_l9BZc9NvO2aK9bfsPg9Z4O8wqLcjLBk3uAXVg93D2lJgxDU3lvfjAVqpJW6IHWK-d7ZYIzN7nXgNVL_4FROsqPyDAK3CJN3fa2sA1CKPT3myQzRr8Ztp6CuNePk3bmHZoWt7kM3OC-D-c2iYrIbDsIW2Z0u-5auz3cU-z0KHODOHA5r6FpL7CTMyExB7XAvbMJeen2Bp-06vFZVPU_ofVIAixJzuCfykZyMCoK9Fv4Od1VfXYuxqySsuK0SUAWpfjhwFApDJqUcqFLC2peRoplTAenrOXsUD1wXNvhs1SLBnq5WKntgXTEqwmmncDd161tspRCrC79tGYdRh6yA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">drpezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/75516" target="_blank">📅 18:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75514">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HiFM3WqTzMGQvhHIP1zSF5LT4wjgkN_q_4uuKdTJNv51St9uQ1CCIttpkfGrXs0v5RqxtMAL3026-abXPEJhL58-Q53FYR0sD4pF0sxrgZcwvY_BqmDLMiNVOpo0uj_CWIf5A41eZV3od4zCQG4drJTCuVTIlE9pG-ml27dm3zl7qzzZopiorelLKBmYWiSxgvGu46kDRmIoJAOFuHodAWBvuHbj-dzrdY1RUtLArPuCgUytVjQIw3n8szm5Z4a0WwYdQ7dTw37wvC6kcESeP45UWn8MeNNEbSR5zlbvfVCxOY5hHP7GlkQLoy-ctJAjfAVxBuzC1D_xjMdoeaLD2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uIfSGiLkvoNCoPFZjtlHZHYpVTWKeK2O22ZMKiH-3o9KrSw9y82W61MwR3JiNlLQolnvs1VETrbrjNvfDoDRU1HzPkUiop3Cj9S6sH_juLW_ZROZN4EntcMp80gxGbHbH-xhCqGlFo2WtxfWhjVI4tmL6UVgb930moXBUcxJx4ABu9e4lH_gfnouX_oWK2v6mqLrOoPgtN9i6amPVGOTV6lNTluqr2IRQQfpKta7twnPVEiyqWKHUhuKNZ0hAgEQC4xgSzC8a2_91RPZfFRDbhDN-9Umc16c-B3YrydhxfDFTAYSc1tKTAW1FoPary7G8ZmEsi8susSRYgzKr45yKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن نقوی، وزیر کشور پاکستان، عصر امروز با محمدباقر قالیباف، رئیس مجلس ایران در تهران دیدار و گفت‌وگو کرد.
رسانه‌های ایرانی و پاکستانی گزارش داده‌‌اند که آقای نقوی برای از سرگیری مذاکرات به ایران سفر کرده است.
گفته شده او حامل پیام‌ آمریکاست و پاسخ ایران را هم دریافت خواهد کرد.
به گفته سفارت پاکستان در تهران، آقای نقوی دیروز پس از ورود به تهران «نزدیک به سه ساعت در نهاد ریاست جمهوری حضور داشت» و اسکندر مومنی، وزیر کشور، و عباس عراقچی، وزیر امور خارجه نیز «در جریان این دیدار در نهاد ریاست جمهوری حضور داشتند.»
علاوه بر این، محسن نقوی «دیداری خصوصی» با مسعود پزشکیان داشت که «حدود ۹۰ دقیقه به طول انجامید و با حضور وزیر کشور ایران همراه بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/75514" target="_blank">📅 17:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75513">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAWZMJzPwcu17jNf8h9SMjOP4ycHkAxEg1b0HkhLjo6X2V_nhbuynkQgEvg2vN7O6pdBgKCt3K4TNzt_-p63sb8SmfelTEu32awF-sL97fqcdOelElFgUmRpbbBOHu8Mg5adIDmS9CCxOYg_hXcowR9M81w5b5SXvfRfhOnj8V0rhhTt2n7olYFToP7nHxfSPy8ev9tSbaR_fW6y4irVujW3Yu4aBEGc1BnLl7LuDdtX4X9aoSO8FYy0ZO9lCbQEd7jGvNkZklkCaTInSeLtfao_oJU9hCkCGnZFdEKKTiVTNJvnnBc2EtC-RtQ_SomL-E_MbsmIZY3VAVcm1Qa3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس با انتشار متنی مدعی شد جزئیاتی از پاسخ آمریکا به پیشنهادهای ایران در جریان مذاکرات به دست آورده است؛ گزارشی که در آن از پنج شرط اصلی واشنگتن برای توافق با تهران سخن گفته شده است.
براساس شنیده‌های فارس، شروط اعلام‌شده از سوی آمریکا شامل موارد زیر است:
۱- عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا
۲- خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا
۳- فعال ماندن تنها یک مجموعه از تاسیسات هسته‌ای ایران
۴- عدم پرداخت حتی ۲۵ درصد از دارایی‌های بلوکه‌شده ایران
۵- منوط‌شدن توقف جنگ در همه ساحتها به انجام مذاکره
به گفته فارس، در مقابل، ایران انجام هرگونه مذاکره را منوط به تحقق پنج پیش‌شرط اعتمادساز دانسته است: «پایان جنگ در همه جبهه‌ها به‌ویژه لبنان»، «رفع تحریم‌های ضدایرانی»، «آزادسازی پول‌های بلوکه‌شده ایران»، «جبران خسارات ناشی از جنگ» و «پذیرش حق حاکمیت ایران بر تنگه هرمز».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/75513" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75512">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cecgCq8O8mDgp9M5XGv7oZpxU6TAFJR7Vwy_QkA4ho8J5P06MJ3bjVIQFvpLJtz8ZDW-sloCc91YZBtoqBKJiBQaWJpdDQt3ibwZN1WjVqDIPSDlq83am7r1af1UukIDXROQV2b6VULNqLaP1qSo9flQq_9Bz5gJCaEfJC5O66u0zqmt1actwxuElVbzaPVNpLJ6WQK8mnTL5943jX52lQ03P3DzX4fgt-LzXUiwciPSRtEJBWlGhh4D46EnHyD44bVanRPNQczAWUEoH5hv0sQSltheHfyzIV5Pf-FDc0WoFwr-xiaUKcdgySW7NpOcjCjAz9O3AXskOlC66NCTJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، در کانال تلگرامی خود اعلام کرد که کتاب «قدرت مذاکره» او به چاپ پنجم رسیده و در چاپ جدید این کتاب، بخش جدیدی با عنوان «دیپلماسی زیر آتش» درباره روند «مذاکرات غیرمستقیم با آمریکا در جنگ ۱۲ روزه» به آن افزوده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/75512" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75511">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGaj1A3Oxr8W2kegDzGlDqFyCGagw94tOC_yFA50jWwV8YeIllU5VQNnUM0TEK8b5h1JwFCIP77eO9YLik099nv8tzvYtiBPx-1Wg6YrxBuyy6Zmpqk1pa24UYRrP4bXJ0VTQm_T8H03Jz1QkeHsL6FCVIuN2ie2WjLcgkBY7Veu32-pU54T2DCt7o00WUNw8F2En7s9LX0NS21EW_SBXehpdHZ2T5M2sVzuD5B3YwpQ1kfranmfyOaKoIIWKaMGufSyovIy05n6nAwglkZ18nAe2mT7W-DtDaiGWmExYqGldx49JVzwALhI5wsHy531mlLPEF8Pq0tO_pMKvztZLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره رسانه‌ای ابوظبی روز یک‌شنبه ۲۷ اردیبهشت در شبکه‌های اجتماعی از وقوع آتش‌سوزی در نیروگاه اتمی براکه در امارات متحده عربی خبر داد.
این آتش‌سوزی پس از حمله پهپادی به نیروگاه اتمی برکه در منطقه الظَفرَه آغاز شده، اما کشته و مجروح بر جا نگذاشته است.
بر اساس توضیح اداره رسانه‌ای ابوظبی، این حریق در ژنراتور برق خارج از محدوده پیرامون نیروگاه به راه افتاده و بر ایمنی سایت اثر منفی نداشته است.
در پی آغاز حمله مشترک آمریکا و اسرائیل به خاک ایران، امارات متحده عربی به بزرگ‌ترین هدف حملات تلافی‌جویانه سپاه پاسداران تبدیل شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/75511" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75510">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAyOZR7kV01Wz5ERY-mB-R17xuJioLWICXew-mSn_gsVqLOKL2iw_RQz00SRTLXKJ85obfqsWdu0vEbuc_tb5vN71Dymwlb6ceBBZ9rPMApWMBEIECyFeqytDxu6EHlauvsaatFk-WPsYqyydo0URcE4ogtuWo1wx8uP4OTUf20XNckCn3J4H2R45swG1O8Swfkt7JShMJJjaiPCK_jZuoWCiX5dgUOfc03BMoXmnWhYTEV4culKmLu_P5ZFrmeI7nGtibVk1dWOS212H_5JyB-SMkfiHK35J2fndypZxtxoUjT2nP1jjgC3xnDIPglGKYfx4nS5-wS5zvuAUWbvzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، نزدیک به سپاه پاسداران، روز یک‌شنبه ۲۷ اردیبهشت نوشت که محمدباقر قالیباف، رئیس مجلس شورای اسلامی و عضو سابق سپاه، به عنوان نماینده ویژه ایران در امور چین تعیین شده است.
این خبرگزاری امنیتی بدون هیچ توضیح دیگری تنها نوشته است:‌ «پیشتر علی لاریجانی و عبدالرضا رحمانی‌ فضلی چنین مسئولیتی را برعهده داشتند.»
🔸
در این خبر نه توضیح داده شده که چه کسی یا چه نهادی قالیباف را به این سمت منصوب کرده است و نه برهه کنونی چه اهمیتی دارد که حکومت تصور کرده است به این نماینده ویژه نیاز دارد.
اعلام تعیین قالیباف به عنوان نماینده ویژه در امور چین دو روز پس از دیدار رسمی رئیس جمهور آمریکا از کشور چین رخ می‌دهد که در آن یکی از موضوعات گفت‌وگو ایران و تنگه هرمز بود.
کاخ سفید روز پنجشنبه ۲۴ اردیبهشت اعلام کرد دونالد ترامپ، رئیس‌جمهور آمریکا، و شی جین‌پینگ، رئیس‌جمهور چین، در دیدار خود درباره گسترش همکاری‌های اقتصادی، باز ماندن تنگه هرمز و جلوگیری از دستیابی ایران به سلاح هسته‌ای گفت‌وگو و توافق کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/75510" target="_blank">📅 17:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75509">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oRahUVodvuFw9KLUKgWSL1F0gWx528kOqNKeX-ht5QmXKdTh5nJC4D2UpNBeIucDczTwCnS05caqGXdj2cWA3KPxzmh73UAbWbAuPUtG5u3D0Kd2sgplr5-TYsnsT1UR-MgOwa9q8lMhCBUcTgWCQGjtctzKfWfYr3zEFa_pMltIBiPmdA09ux-OowSJ6MCzE5chKGWl0VRwI_Xe7WpzCZ-J0MTFDaDbn5D2dOjdVRbT-uEiLLEgltElDW0I2Fnqdo2XmXL-ajTR0inRHQq2D2tV-Bo3PP6T5Y4Q4G_sUkoGnp809gwDG2A5qC85stppWzsxMThzRapTcVJhyGR2Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه دادگاه صادق ساعدی‌نیا، مدیر کافه‌های زنجیره‌ای ساعدی‌نیا که در اعتراضات سراسری دی ماه گذشته به همراه پدرش، محمدعلی ساعدی‌نیا، بازداشت شده بود در دادگاه انقلاب قم برگزار شد.
کافه‌های ساعدی‌نیا از جمله کسب‌وکارهایی بود که در اعتراضات دی ماه پارسال که با اعتراض بازار به نابسامانی اقتصادی آغاز شد، مغازه‌هایشان را تعطیل کردند.
نماینده دادستان قم در این جلسه آقای ساعدی‌نیا را به «فعالیت تبلیغی یا رسانه‌ای برخلاف امنیت کشور»، «اقدام عملیاتی برای گروه‌های معاند نظام از طریق انتشار استوری و فعالیت مجازی و حضور در تجمعات غیرقانونی و تعطیل کردن کافه‌ها و مغازه‌های خود در کل کشور و تشویق تعدادی از کارکنانش در ارتکاب جرایم علیه امنیت کشور» متهم کرد.
به گفته نماینده دادستان و قاضی، موارد اتهامی بر مبنای اطلاعاتی است که از محتوای لوازم الکترونیکی ضبط شده از آقای ساعدی‌نیا و از جمله تصاویر و چت‌های او در واتساپ استخراج شده است.
نماینده دادستان گفت که آقای ساعدی‌نیا در واتساپ خود «برنامه‌ریزی برای تعطیلی کافه‌ها را همزمان با صدور فراخوان دشمن به مشورت گذاشته بود.»
قاضی به او گفت: «شما با فراخوانی که داده‌اید با اقداماتی که انجام داده‌اید، این تعداد جوان را به این مهلکه وارد کرده‌اید و نظام متحمل صدمات زیادی شده است. چطور می‌توانید جبران کنید؟»
@
VahidHeadline
نماینده دادستان، مواردی از جمله فعالیت‌های ساعدی‌نیا در فضای مجازی، تهیه کلیپی از یکی از کارکنانش با نوشته «جاوید شاه» روی دست، ایجاد و مدیریت گروه واتساپی کارکنان کافه‌ها، انتشار پیام صوتی درباره خاموش کردن گوشی برای جلوگیری از ردیابی، حضور برخی کارکنان در اعتراضات و برنامه‌ریزی برای تعطیلی کافه‌ها و کارخانه‌ها همزمان با فراخوان‌های اعتراضی را از مصادیق اتهامات مطرح‌شده علیه او عنوان کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/75509" target="_blank">📅 17:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75507">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SnuKZ8TJfJAPO-Az56IigSFf-qbqX58oqqo5Dpb-rU5yZpyRPFObzx3zsLYkIUCVoUVvDdas7TKw6ej-J9j8Gjj83aBrzCopzghuFqPxuhHD1v0r_vhWok_4qnmfcpJsicVwR3ntiqXghn1iM0V1bZTUYSuga52Tz9bhaVI-1aZfrLREFUdGAsoT4Bzc1du7witfCWWMRJfN09u7AdvuClZ4ALd3ECULaVA3pjcQQqoAdlL-Uj8nw53UoLf889EK0VXTyoMfY1o2MBzUlnnbM54lZ1cA_VpAB7Vm178DNm-UzXjdvrGZ-yWni6dA0snNOpglOsjwwk6P2KuCOTPI5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز شنبه تصویری گرافیکی از خود در کنار یک فرمانده نظامی بر عرشه یک ناو جنگی، در فضایی طوفانی و در میان شناورهایی با پرچم جمهوری اسلامی، در شبکه اجتماعی تروث‌سوشال
منتشر کرد
که روی آن نوشته است: «این آرامش پیش از طوفان بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/75507" target="_blank">📅 23:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75506">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2db463b161.mp4?token=H32fJk6duInuHETaXbiXkPCUBgTgg4D9c0f77WlD_mM9zbARjiHS9li9B2ZGHT-_jT7IY2m_SVxiOjvZWwx91igkyFPGi7mCgJEGmGHN_mo4ihW_CTIO1novU_bndtU6EgDz8LondBWIlWR2LtzfqEMCsuD_YvsmOjj6egj9jjmi-rj0mP0L8DzoutHR-pHkKNcM2lfTtht6ypC-nBU5lNqBChx6knW9G-mqEn6crlP9smBnmpq5AhM83LilJea1xzkqhFxfiqPX1Sto0j8szQhf_FEf0ZyQ7T6iaINLVIEmHfXDryOBC8nYrnWhX_Or5Lh_O3OjZR-DgIDiw2dNdw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2db463b161.mp4?token=H32fJk6duInuHETaXbiXkPCUBgTgg4D9c0f77WlD_mM9zbARjiHS9li9B2ZGHT-_jT7IY2m_SVxiOjvZWwx91igkyFPGi7mCgJEGmGHN_mo4ihW_CTIO1novU_bndtU6EgDz8LondBWIlWR2LtzfqEMCsuD_YvsmOjj6egj9jjmi-rj0mP0L8DzoutHR-pHkKNcM2lfTtht6ypC-nBU5lNqBChx6knW9G-mqEn6crlP9smBnmpq5AhM83LilJea1xzkqhFxfiqPX1Sto0j8szQhf_FEf0ZyQ7T6iaINLVIEmHfXDryOBC8nYrnWhX_Or5Lh_O3OjZR-DgIDiw2dNdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، انیمیشنی در تروث سوشال
منتشر کرد
که در آن به ناو آمریکایی دستور شلیک به هدفی با پرچم جمهوری اسلامی را داده و می‌گوید: «در فهرست اهداف‌مان قرار دارد، آتش!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/75506" target="_blank">📅 21:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75501">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t-M5ZWXIwxICxuVWYSL4x3SHwMWgQgmuorbsW-CwR4R_DGNg2CIFtoSaVt2qoeOH8SgJ8OF7YWjtoFNF0CD3IUBKgbsVwXMrXD5PmPJVt9VeSYAn-2cY-Ous7dxqo1Ao3nuZtnLaJNl8xOd6eLCCFiWZvbFCk2OAiOHht2Bx9Kf0JvidTfKtOjU6rPrZzD1yB3K0c9OUyLBsY27gbyHBlIMancZ55koDDkDbWjJhERP3DbPNYX6yRj92JsgicJ3O2XZoCjK9OnHS0OS4Sr8LwunSueom8VgzaoZM5kA5AL2nGCmElmUyxPuqV2kpHoRMZ0SVF3LJ-hwVPlvlEsK70g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OGbDfGaJDjtkNGTQZDuDqL1qxHZ2JheB8yABBlAIhv-Qq6qVIz9H28jBYqsziM8wQkQPxJKpdt2G-iBON6bpp5ulCa5Nlk9JejvjMLOeyjciESQJWfzqREzzmTZzZ1zwzjTg8XoQ7RFMBVxsUqdgmArAP0RUpC8dtQNHX6hAg6irxY8Ee4pUqhc4JkI2I3K_jQFjsUT9Y58Io78pASF3BrELTc4WbhDRTHucTzhJyNRYqRwUXsbJkaJM7ktWdwvrXYPTropiOgdzc3MSfzTGYR-rUKpEW-vQaAwg0k9EnHOk7jWtsxmVh9a4CNaSbiy9zHxLM0zVnv4MlYMdMsw67w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D4XrmUcB2gbW8E7FPVlEMAXG-NgQGBSBCAaJ2NetlPVfsDB3T0U89S5Kvf0S_2CmcPsFheen-jxAbX2rBz-bu3y5rZ3Mxsd3c1x5F4hvXJ8gAKBPSdwdv1XfZ4P5AYMb7-xDqr6DIvBoscm-sC5aofghtn6Z8zLu6EnbhTVeyjenE5gknp2jQG1e62bNeAOyuHJ51DAZjpPnrufEI5JOLdFIoHvUOLj2kOG2B6mNjs8Wiry1ORb9aezRJ_xPmtuWFDe2e5pain-ujQ662Hlky6NNorjB3FX9LyXPtv-MgGmrXg_ZIa0jzxNceWk1C05zmRje21ioeZJKPTPE7u_WMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eaoLMW0E4_Ko6cP98WCqCrgDIWO1R9LYrHRYaXmO0Y-QsMbYTMNvlQN3uK4ydgZ7LEU_PkHEMhAQn9rqx6vDXl_A-jnhpVyhJzDeuhYrVEFZRT5L1JPLucTTNqNUsuFlRp696DeIULPGrYKzWU28UjHsDCJEgBBWUfV4fXXqrY4kaJsOHpapoFphxwBEM-ykyuGHD43b12UK6d7WPorZ_qcW2NOGicEuaZvwCMKJdbhrXJbo7d5CQSSrxbAW2Fq6g9th2E5iwrxDlpJpfxn6mqM709P73R4TwnLyQ1ldiskQWPREHB9gk9D_E_ZI3ixGU_p0R-NpLBbdtVpfxLxG6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fcb834d170.mp4?token=bXDyWSTdD9HSiBD_EmvC3OK9MGWEqMI-TfMBmXopZFtw1sKiY4REPKsZGutsdZ6Obijg4EAEzpldm90_H6FjZ-_E_9IgNkWGV9r-Jlh12mWnhx3Ml3xTn_nMVdWjIctQrBWou_0G6Ew-yKRZLoCjPH_4YQHWXhYOMNeLrcg3jAZPuyBLUPJUPjH3xXazkvP2qF0l1fmKq_7PGOfncNpoLJnKBomJVHIQcUZ4Iyfd8reE7tV1V15QhQQ7O2zaDL3xrpwqFc8vompBb5LiiBQyQ7i_7ahqOAb9Qb3EsyO-JQdbI-0F5WQwktE3ggL4zd-sGC7gLS8p1f0P0tgUqWY2FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fcb834d170.mp4?token=bXDyWSTdD9HSiBD_EmvC3OK9MGWEqMI-TfMBmXopZFtw1sKiY4REPKsZGutsdZ6Obijg4EAEzpldm90_H6FjZ-_E_9IgNkWGV9r-Jlh12mWnhx3Ml3xTn_nMVdWjIctQrBWou_0G6Ew-yKRZLoCjPH_4YQHWXhYOMNeLrcg3jAZPuyBLUPJUPjH3xXazkvP2qF0l1fmKq_7PGOfncNpoLJnKBomJVHIQcUZ4Iyfd8reE7tV1V15QhQQ7O2zaDL3xrpwqFc8vompBb5LiiBQyQ7i_7ahqOAb9Qb3EsyO-JQdbI-0F5WQwktE3ggL4zd-sGC7gLS8p1f0P0tgUqWY2FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر جمیله شفیعی:
JamilehShafiei
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/75501" target="_blank">📅 17:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75500">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffe0351e23.mp4?token=OivxfPIOTsHQsOZbgNKOlphnNWxZF2bie_saljS5bP1KRdG71hH7nRnz2e-4IkEyDXqOjDAcYNZMIlwCrhfxN9jVgXOyZNGdhdFdXVZIizvTyFcBXCzNUir5YGnG9EDplTE1arwtSKIWro2wpSSTfRtqE6tTIx1Uw8Z5YFMwYDHQUyAeuwSRxeZugK9ViPO6kZwts6NNNjUNTQKq2EFjRYcn4EhRG69EFh9V4C4T9PYHTSnQlEc2nEWI8Ku5mtCidnBRxJgAHUUU9TWRohjoYe44YHZhbAYCYfFsCJ--06th5m1Tj6Sd7HjIWtg3uxQ9eiOPpFhkguhpW09utp0VlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffe0351e23.mp4?token=OivxfPIOTsHQsOZbgNKOlphnNWxZF2bie_saljS5bP1KRdG71hH7nRnz2e-4IkEyDXqOjDAcYNZMIlwCrhfxN9jVgXOyZNGdhdFdXVZIizvTyFcBXCzNUir5YGnG9EDplTE1arwtSKIWro2wpSSTfRtqE6tTIx1Uw8Z5YFMwYDHQUyAeuwSRxeZugK9ViPO6kZwts6NNNjUNTQKq2EFjRYcn4EhRG69EFh9V4C4T9PYHTSnQlEc2nEWI8Ku5mtCidnBRxJgAHUUU9TWRohjoYe44YHZhbAYCYfFsCJ--06th5m1Tj6Sd7HjIWtg3uxQ9eiOPpFhkguhpW09utp0VlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"مجری شبکه سه تلویزیون: یک راکت ۲۰۰ دلاری می‌تواند کل ارتش آمریکا را در منطقه به زانو درآورد"  ویدیو با تیتر بالا در منابع جمهوری اسلامی منتشر شده و خانعلی‌زاده متوهم رو نشون میده که مطابق معمول چرندیاتی در سطح خودش میگه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/75500" target="_blank">📅 17:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75499">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46bd8e2257.mp4?token=E9TwslJLAxGhZiH33GknaTxS7wc38wNaFAw6I9mog4dPsSixA2ZNAW98fXAWX9wDImHpV753b4qGn7SoYI5zXJoK-kiyniaAFLxXGnkwwXAog_3jyyp-8isHBQX8iq7r91AZmFP_jHZXtKkkjrmN9GsaxslWEF-iwPJ2bMt9_ASdzySN-mP_ZHsxE1bHpCMJAfdsQY7N0DCNVazQUJLUzPF60AnKhuax9nCfIrw-BMoYBCRv_uxXUo5RuOTjV-uXjgrIoWRBj3Qztn_fUbun58oSd3abQ-lgQHsE8tV2haE3JcZgei30FM7jQ7NcFDiQNMfPqNvC8C7GuaC7gtIC-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46bd8e2257.mp4?token=E9TwslJLAxGhZiH33GknaTxS7wc38wNaFAw6I9mog4dPsSixA2ZNAW98fXAWX9wDImHpV753b4qGn7SoYI5zXJoK-kiyniaAFLxXGnkwwXAog_3jyyp-8isHBQX8iq7r91AZmFP_jHZXtKkkjrmN9GsaxslWEF-iwPJ2bMt9_ASdzySN-mP_ZHsxE1bHpCMJAfdsQY7N0DCNVazQUJLUzPF60AnKhuax9nCfIrw-BMoYBCRv_uxXUo5RuOTjV-uXjgrIoWRBj3Qztn_fUbun58oSd3abQ-lgQHsE8tV2haE3JcZgei30FM7jQ7NcFDiQNMfPqNvC8C7GuaC7gtIC-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در یک برنامه زنده تلویزیونی که از شبکه افق صداوسیما پخش شده است، مجری برنامه با اسلحه واقعی به پرچم امارات متحده عربی شلیک می‌کند.
در این برنامه که موضوع آن درباره آموزش شلیک با اسلحه کلاشنیکف است، فردی که لباس نظامی به تن دارد و صورت خود را با ماسک پوشانده است مراحل آماده‌سازی اسلحه و شلیک گلوله را به مجری آموزش می‌دهد.
مجری برنامه هم در مرحله شلیک تصمیم می‌گیرد به پرچم امارات که در بنر مربوط به دکور استودیو، شلیک کند.
@
VahidHeadline
صدا و سیمای جمهوری اسلامی جمعه چند برنامه پخش کرد که در آنها مجریان در بخش‌های استودیویی با در دست داشتن تفنگ ظاهر شدند و کار با سلاح‌های سبک آموزش داده شد. مجریان در این برنامه‌ها اعلام کردند که در صورت لزوم به جنگ خواهند پیوست.
این برنامه‌ها که دست‌کم در سه بخش پخش شد، در رسانه‌های داخلی بازنشر و در شبکه‌های اجتماعی با واکنش‌هایی همراه شد. برخی کاربران شبکه‌های اجتماعی این بخش‌ها را نشانه‌ای از بسیج در شرایط جنگی توصیف کردند.
جکسون هینکل، مفسر سیاسی آمریکایی، در شبکه اجتماعی ایکس نوشت تلویزیون دولتی ایران نحوه استفاده و شلیک با کلاشینکف را به‌عنوان «آمادگی برای تهاجم زمینی آمریکا» نشان می‌دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/75499" target="_blank">📅 17:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75498">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSiArARhLvoOu3pFF9WH0NpiwrP3IDvDcozZ6VSs1ibc-4BY5QnLoaxkeNXV_gTnT8_sIeHYuOZrdOthwJFI5020KHGcDO-fsmT7bWz7F2UwPSu9ObdRRHNI-pW7rUIlyPmS-3Moqp2rFA9bNEQIBvkV0DBSICkQUp26DRwDQNifUMYHczp6qR9wl11b5MOPMtFh6d8hyJmah3C2Zbk1Vpj8sFfuoJcht1iCCFyh2VZ178ylMSZPFhRHpXom3ErO1z7ToqDFLTyWOoyP9owC3sERSVFDVzpFKd24u4tPlY4X5wLU2j1uULqk88k4mH911uNdPOhHHF6oPD6cA4xg0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه وابسته به قوه قضائیه جمهوری اسلامی اعلام کرد اموال ۵۱ نفر در استان یزد، با دستور قضایی و به اتهام آنچه «خیانت به وطن» و «همکاری با دشمن» خوانده شده، توقیف شده است.
بر اساس این گزارش، پرونده این افراد در ارتباط با قانون موسوم به «تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی علیه امنیت و منافع ملی» در حال رسیدگی است و مقام‌های قضایی مدعی شده‌اند دارایی‌های توقیف‌شده قرار است برای «حفظ حقوق عامه» و بازسازی اماکن آسیب‌دیده از جنگ هزینه شود.
اموال توقیف‌شده شامل حساب‌های بانکی، دارایی‌های منقول و غیرمنقول، سهام شرکت‌ها و حتی اموال وکالتی عنوان شده است.
طبق گزارش میزان، از میان این ۵۱ نفر، ۲۰ نفر در داخل کشور حضور دارند و ۳۱ نفر دیگر در خارج از کشور به سر می‌برند.
این اقدام در ادامه موج تازه‌ای از مصادره و توقیف اموال شهروندان و مخالفان سیاسی صورت می‌گیرد؛ روندی که در عمل به ابزاری برای فشار، ارعاب و مصادره دارایی افراد تحت عنوان‌های سنگینی مانند «خیانت» و «همکاری با دشمن» تبدیل شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/75498" target="_blank">📅 17:01 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
